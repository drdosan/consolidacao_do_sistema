# 🚀 Guia Rápido - Fase 7

Guia rápido para começar a usar o sistema integrado da Fase 7.

## ⚡ Início Rápido (5 minutos)

### 1. Instalar Dependências

```bash
cd fase7
pip install -r requirements.txt
```

### 2. Executar Dashboard

```bash
# Windows
run_dashboard.bat

# Linux/Mac
chmod +x run_dashboard.sh
./run_dashboard.sh

# Ou manualmente
cd src/dashboard
streamlit run main_dashboard.py
```

### 3. Acessar Dashboard

Abra o navegador em: `http://localhost:8501`

## 📋 Funcionalidades Principais

### Dashboard Principal
- **URL:** `http://localhost:8501`
- **Funcionalidade:** Visualização em tempo real de todos os dados

### Navegação
Use o menu lateral para acessar:
- 🏠 Página Inicial
- 📊 Dashboard Principal
- 🌾 Fase 1 - Cálculos
- 💾 Fase 2 - Banco de Dados
- 🔌 Fase 3 - IoT
- 🤖 Fase 4 - Machine Learning
- ☁️ Fase 5 - Cloud
- 👁️ Fase 6 - Visão Computacional
- 📧 Sistema de Alertas

## 🔧 Configuração Mínima

### Banco de Dados
O sistema já está configurado para usar o banco MySQL da Fase 2/3/4.

### API Flask
Para funcionalidades completas, inicie a API:

```bash
cd ../fase3/api_crud  # ou fase4/src/api_crud
python app.py
```

### Alertas AWS (Opcional)
Para usar alertas, configure AWS SNS (veja `docs/AWS_SNS_SETUP.md`)

## 🎯 Casos de Uso Comuns

### 1. Ver Dados dos Sensores
1. Acesse "📊 Dashboard Principal"
2. Visualize gráficos e métricas em tempo real

### 2. Calcular Área de Plantio
1. Acesse "🌾 Fase 1 - Cálculos Agrícolas"
2. Selecione cultura
3. Informe dimensões
4. Clique em "Calcular"

### 3. Consultar Banco de Dados
1. Acesse "💾 Fase 2 - Banco de Dados"
2. Selecione tipo de consulta
3. Visualize dados

### 4. Fazer Previsão de Irrigação
1. Acesse "🤖 Fase 4 - Machine Learning"
2. Ajuste os valores dos sensores
3. Clique em "Prever"

### 5. Processar Imagem
1. Acesse "👁️ Fase 6 - Visão Computacional"
2. Faça upload de imagem
3. Escolha modelo
4. Clique em "Processar"

## 🐛 Problemas Comuns

### Dashboard não abre
- Verifique se Streamlit está instalado: `pip install streamlit`
- Verifique se a porta 8501 está livre

### Erro de conexão com banco
- Verifique se o banco MySQL está acessível
- Verifique credenciais em `main_dashboard.py`

### API não responde
- Verifique se a API Flask está rodando
- Verifique a URL em `main_dashboard.py` (padrão: `http://localhost:5000`)

### Modelo ML não encontrado
- Execute o treinamento: `cd fase4/src/machine_learning && python train_model.py`

## 📞 Suporte

- Consulte o README principal: `README.md`
- Consulte documentação AWS: `docs/AWS_SNS_SETUP.md`
- Entre em contato com o tutor

---

**Dica:** Use `Ctrl+C` no terminal para parar o dashboard.

