import fitz  # PyMuPDF
import tkinter as tk
from PIL import Image, ImageTk
import json
import os

class LayoutPicker:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.root = tk.Tk()
        self.root.title("Configurador de Layout - Clique nos campos")
        
        # Carrega a página do PDF como imagem
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap()
        self.img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.tk_img = ImageTk.PhotoImage(self.img)
        
        self.canvas = tk.Canvas(self.root, width=pix.width, height=pix.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
        
        # Lista de campos para configurar
        self.fields_to_map = ["cliente", "data", "tabela_inicio", "total"] # Adicione mais campos conforme necessário
        self.current_field_idx = 0
        self.coords = {}
        
        self.label = tk.Label(self.root, text=f"Clique onde deve aparecer: {self.fields_to_map[0]}", font=("Arial", 14))
        self.label.pack()
        
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        field = self.fields_to_map[self.current_field_idx]
        
        # Converter coordenada do Tkinter (Top-Left) para ReportLab (Bottom-Left)
        # O ReportLab usa pontos (72 dpi). PyMuPDF geralmente renderiza em 72-96 dpi.
        img_width, img_height = self.img.size
        rl_x = event.x
        rl_y = img_height - event.y  # Inverte o eixo Y
        
        self.coords[field] = (rl_x, rl_y)
        print(f"✅ {field} configurado em: ({rl_x}, {rl_y})")
        
        self.current_field_idx += 1
        if self.current_field_idx < len(self.fields_to_map):
            self.label.config(text=f"Clique onde deve aparecer: {self.fields_to_map[self.current_field_idx]}")
        else:
            self.save_and_exit()

    def save_and_exit(self):
        with open("layout_config.json", "w") as f:
            json.dump(self.coords, f, indent=4)
        print("🚀 Configuração salva com sucesso em 'layout_config.json'!")
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Exemplo de uso: substitua pelo seu modelo base
    path = "modelo_base.pdf" 
    if os.path.exists(path):
        app = LayoutPicker(path)
        app.run()
    else:
        print("Coloque um arquivo 'modelo_base.pdf' na pasta para calibrar.")