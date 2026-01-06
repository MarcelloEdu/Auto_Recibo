# setup.ps1
Write-Host "--- Iniciando Setup do Sistema de Recibos ---" -ForegroundColor Cyan

# Verifica se o Python está instalado
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Erro: Python não encontrado. Instale o Python e adicione ao PATH." -ForegroundColor Red
    exit
}

# Cria ambiente virtual
Write-Host "📦 Criando ambiente virtual (venv)..."
python -m venv venv

# Ativa o ambiente e instala dependências
Write-Host "🛠️ Instalando dependências do requirements.txt..."
.\venv\Scripts\pip install --upgrade pip
.\venv\Scripts\pip install -r requirements.txt

#se nao hexistir, cria pasta IDV e recibos
if (!(Test-Path -Path "IDV")) {
    Write-Host "📁 Criando diretório IDV..."
    New-Item -ItemType Directory -Path "IDV"
}
if (!(Test-Path -Path "recibos")) {
    Write-Host "📁 Criando diretório recibos..."
    New-Item -ItemType Directory -Path "recibos"
}

Write-Host "✅ Setup concluído com sucesso!" -ForegroundColor Green
Write-Host "Para rodar o programa: .\venv\Scripts\python main.py"