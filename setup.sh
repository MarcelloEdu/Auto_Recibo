#!/bin/bash

# setup.sh
echo -e "\e[36m--- Iniciando Setup do Sistema de Recibos ---\e[0m"

# Verifica se é Linux e tenta instalar o python3-tk se necessário
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Detectado Linux: Verificando python3-tk..."
    sudo apt-get update && sudo apt-get install -y python3-tk
fi

# Cria ambiente virtual
echo "📦 Criando ambiente virtual (venv)..."
python3 -m venv venv

# Ativa o ambiente e instala dependências
echo "🛠️ Instalando dependências..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Se nao houver, cria pasta IDV e recibos
if [ ! -d "IDV" ]; then
    echo "📁 Criando diretório IDV..."
    mkdir IDV
fi
if [ ! -d "recibos" ]; then
    echo "📁 Criando diretório recibos..."
    mkdir recibos
fi

echo -e "\e[32m✅ Setup concluído com sucesso!\e[0m"
echo "Para rodar o programa use: source venv/bin/activate && python main.py"