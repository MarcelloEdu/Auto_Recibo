# 📄 Sistema Universal de Recibos

Sistema automatizado para geração de recibos em PDF com calibração dinâmica de layout.

##  Como instalar
1. Execute o arquivo `setup.ps1` (Windows) ou `setup.sh` (Linux).
2. Aguarde a instalação das dependências.

##  Como Configurar o PDF (Calibragem)
Para que o sistema funcione com **qualquer** modelo de recibo:
1. Coloque seu arquivo PDF em branco na pasta `IDV` com o nome `modelo_recibo.pdf`.
2. Execute o `picker.py`.
3. Clique na imagem nos locais correspondentes aos campos:
   - Nome do Cliente
   - Data de Emissão
   - Início da Tabela de Itens
   - Valor Total
4. O arquivo `layout_config.json` será gerado e o sistema estará pronto!

## 💻 Uso Diário
Basta executar o `open.bat` para gerenciar clientes e emitir recibos profissionais.