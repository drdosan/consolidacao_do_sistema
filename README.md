# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href="https://www.fiap.com.br/"><img src="fase4/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌱 FarmTech Solutions - Sistema Integrado de Gestão Agrícola

### ▶️ Vídeo de Apresentação Final (Fase 7)

[Link do vídeo será adicionado aqui]

---

## 👨‍🎓 Integrantes

| Matrícula | Aluno |
|-----------|---------------------------------|
| RM 565286 | Diogo Rebello dos Santos |
| RM 565497 | Vera Maria Chaves de Souza |

## 👩‍🏫 Professores

**Tutor:** <a href="https://github.com/leoruiz197">Leonardo Ruiz Orabona</a>  
**Coordenador:** <a href="#">André Godoi Chiovato</a>

---

## 📜 Descrição do Projeto

O **FarmTech Solutions** é um sistema completo de gestão agrícola desenvolvido ao longo de 7 fases, integrando tecnologias de IoT, Machine Learning, Cloud Computing e Visão Computacional para otimizar o monitoramento e gestão de culturas agrícolas.

### 🎯 Objetivo Geral

Desenvolver uma solução tecnológica integrada que permita:
- Monitoramento em tempo real de condições do solo e clima
- Automação inteligente de irrigação
- Predição de necessidades de irrigação usando Machine Learning
- Detecção de pragas e doenças através de visão computacional
- Alertas automáticos para tomada de decisão
- Gestão completa de dados agrícolas em cloud

---

## 📁 Estrutura do Repositório

```
teste_facul/
├── fase1/                          # Base de Dados Inicial
│   ├── cultura-python/             # Cálculos de área e insumos
│   ├── estatisticas-r/             # Análise estatística com R
│   └── README.md
│
├── fase2/                          # Banco de Dados Estruturado
│   ├── farmtech_database/          # Modelo de dados (SQL Developer)
│   ├── DER.png                     # Diagrama Entidade-Relacionamento
│   ├── MAPA_LOGICO.png             # Mapa Lógico
│   └── README.md
│
├── fase3/                          # IoT e Automação Inteligente (Versão Inicial)
│   ├── api_crud/                   # API Flask básica (versão inicial)
│   ├── dashboard/                  # Dashboard Streamlit básico
│   ├── sensores/                   # Código ESP32 (Wokwi)
│   └── README.md
│
├── fase4/                          # IoT, Dashboard e Machine Learning (Versão Completa)
│   ├── src/
│   │   ├── api_crud/               # API Flask completa e aprimorada ⭐
│   │   ├── dashboard/              # Dashboard com ML integrado
│   │   ├── machine_learning/       # Modelo preditivo de irrigação
│   │   └── sensores/               # ESP32 com LCD e Serial Plotter
│   ├── assets/
│   ├── document/
│   └── README.md
│
├── fase5/                          # Cloud Computing & Segurança
│   ├── src/                        # Análise de dados e ML
│   ├── assets/                     # Gráficos e visualizações
│   ├── document/                   # Calculadora AWS e dataset
│   └── README.md
│
├── fase6/                          # Visão Computacional com Redes Neurais
│   ├── dataset/                    # Dataset de imagens (blusas/sapatos)
│   ├── document/                   # Notebooks YOLO e CNN
│   ├── assets/
│   └── README.md
│
└── fase7/                          # Consolidação do Sistema
    ├── src/
    │   ├── dashboard/              # Dashboard integrado final
    │   ├── alertas/                # Sistema de alertas AWS SNS
    │   └── integracao/             # Integrações com outras fases
    ├── docs/                       # Documentação adicional
    ├── README.md                   # Documentação completa
    └── requirements.txt
```

---

## 🚀 Fases do Projeto

### 📊 Fase 1 - Base de Dados Inicial
**Objetivo:** Implementar cálculos de área de plantio e manejo de insumos, integrando API meteorológica e análise estatística com R.

**Tecnologias:** Python, R, API OpenWeatherMap

**Entregáveis:**
- Calculadora de área de plantio (losango)
- Cálculo de insumos por cultura
- Integração com API meteorológica
- Análise estatística com R

📁 [Ver Fase 1](./fase1/README.md)

---

### 💾 Fase 2 - Banco de Dados Estruturado
**Objetivo:** Estruturar banco de dados relacional completo (MER e DER) integrando dados de manejo agrícola.

**Tecnologias:** MySQL, SQL Developer Data Modeler

**Entregáveis:**
- Modelo Entidade-Relacionamento (MER)
- Diagrama Entidade-Relacionamento (DER)
- Mapa Lógico
- Estrutura completa do banco de dados

📁 [Ver Fase 2](./fase2/README.md)

---

### 🔌 Fase 3 & 4 - IoT, Automação Inteligente e Machine Learning
**Objetivo:** Desenvolver sistema IoT completo com ESP32, API Flask aprimorada, dashboard interativo e Machine Learning para predição de irrigação.

> **Nota:** A Fase 3 representa a versão inicial do projeto. A **Fase 4 é a versão completa e melhorada**, contendo todas as funcionalidades da Fase 3 mais Machine Learning, display LCD e melhorias no código.

**Tecnologias:** ESP32, C/C++, Flask, Python, MySQL, Streamlit, Scikit-learn

**Entregáveis (Fase 4 - Versão Completa):**
- ✅ Código ESP32 aprimorado com sensores (DHT22, pH, nutrientes)
- ✅ **API Flask completa e aprimorada** com CRUD completo e integração meteorológica
- ✅ Dashboard Streamlit interativo com Machine Learning
- ✅ Modelo preditivo de irrigação (Decision Tree Classifier)
- ✅ Display LCD 16x2 no ESP32 para visualização local
- ✅ Serial Plotter integrado para monitoramento gráfico
- ✅ Gráficos interativos em tempo real
- ✅ Lógica de ativação automática de bombas baseada em sensores e clima

**Melhorias da Fase 4 sobre a Fase 3:**
- API Flask com melhorias e integração com OpenWeather
- Dashboard com Machine Learning integrado
- ESP32 com display LCD e Serial Plotter
- Modelo preditivo treinado com dados históricos
- Visualizações mais avançadas e interativas

📁 [Ver Fase 3 (Versão Inicial)](./fase3/README.md) | 📁 [Ver Fase 4 (Versão Completa)](./fase4/README.md)  
🎥 [Vídeo Fase 3](https://youtu.be/ClA9DwxtclQ) | 🎥 [Vídeo Fase 4](https://youtu.be/KEdM_Xw_xbk)

---

### ☁️ Fase 5 - Cloud Computing & Segurança
**Objetivo:** Hospedar infraestrutura em Cloud Computing na AWS, aplicando padrões de segurança ISO 27001 e ISO 27002.

**Tecnologias:** AWS EC2, Python, Scikit-learn, Pandas

**Entregáveis:**
- Análise de custos AWS
- Modelos de Machine Learning para predição de rendimento
- Clusterização e detecção de outliers
- Comparação de algoritmos de ML
- Documentação de segurança

📁 [Ver Fase 5](./fase5/README.md) | 🎥 [Vídeo Fase 5](https://youtu.be/Wqqj1hWZ_P4)

---

### 👁️ Fase 6 - Visão Computacional com Redes Neurais
**Objetivo:** Desenvolver sistema de visão computacional com YOLO para monitoramento visual da saúde das plantações.

**Tecnologias:** YOLOv5, PyTorch, CNN, Python

**Entregáveis:**
- YOLO Otimizado (mAP: 0.99)
- YOLO Tradicional (mAP: 0.67)
- CNN do Zero (Acurácia: 94%)
- Dataset rotulado
- Modelos treinados

📁 [Ver Fase 6](./fase6/README.md) | 🎥 [Vídeo Fase 6](https://youtu.be/pQkJcPUKa4c)

---

### 🌟 Fase 7 - Consolidação do Sistema
**Objetivo:** Integrar todas as fases em um sistema único com dashboard integrado e sistema de alertas AWS SNS.

**Tecnologias:** Streamlit, AWS SNS, Python, Boto3

**Entregáveis:**
- Dashboard integrado único
- Sistema de alertas AWS SNS (email/SMS)
- Integração completa de todas as fases
- Monitoramento automático
- Documentação completa

📁 [Ver Fase 7](./fase7/README.md) | 🎥 [Vídeo Fase 7](#) *(a ser adicionado)*

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.8+** - Linguagem principal
- **Flask** - API REST
- **MySQL** - Banco de dados relacional
- **SQLAlchemy** - ORM

### Frontend
- **Streamlit** - Dashboard web interativo
- **Plotly** - Gráficos interativos

### IoT
- **ESP32** - Microcontrolador
- **C/C++** - Programação embarcada
- **Wokwi** - Simulação de circuitos

### Machine Learning
- **Scikit-learn** - Algoritmos de ML
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica

### Visão Computacional
- **YOLOv5** - Detecção de objetos
- **PyTorch** - Framework de deep learning
- **OpenCV** - Processamento de imagens

### Cloud Computing
- **AWS EC2** - Infraestrutura cloud
- **AWS SNS** - Sistema de mensageria
- **Boto3** - SDK AWS para Python

### Análise de Dados
- **R** - Análise estatística
- **Jupyter Notebooks** - Análise exploratória

---

## 🚀 Como Começar

### Pré-requisitos

- Python 3.8 ou superior
- MySQL Server
- Conta AWS (para Fase 5 e 7)
- Git

### Instalação Rápida

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/drdosan/consolidacao_do_sistema.git
   cd consolidacao_do_sistema
   ```

2. **Instale as dependências da Fase 7 (sistema integrado):**
   ```bash
   cd fase7
   pip install -r requirements.txt
   ```

3. **Execute o dashboard integrado:**
   ```bash
   # Windows
   run_dashboard.bat
   
   # Linux/Mac
   chmod +x run_dashboard.sh
   ./run_dashboard.sh
   ```

4. **Acesse o dashboard:**
   ```
   http://localhost:8501
   ```

### Configuração do Banco de Dados

O sistema utiliza um banco MySQL hospedado. As credenciais estão configuradas nos arquivos de cada fase.

### Executar API Flask (Fase 4 - Versão Completa)

Para funcionalidades completas do dashboard, inicie a API Flask da Fase 4:

```bash
cd fase4/src/api_crud
pip install -r requirements.txt
python app.py
```

A API estará disponível em: `http://localhost:5000`  
Documentação Swagger: `http://localhost:5000/apidocs`

### Configuração AWS (Opcional)

Para usar o sistema de alertas da Fase 7, configure as credenciais AWS:
- Veja o guia completo em: [fase7/docs/AWS_SNS_SETUP.md](./fase7/docs/AWS_SNS_SETUP.md)

---

## 📊 Funcionalidades Principais

### ✅ Monitoramento em Tempo Real
- Leituras de sensores (umidade, pH, nutrientes)
- Visualização gráfica interativa
- Atualização automática

### ✅ Machine Learning
- Predição de necessidade de irrigação
- Modelo treinado com dados históricos
- Previsões em tempo real

### ✅ Automação Inteligente
- Ativação automática de irrigação
- Decisões baseadas em sensores e clima
- Integração com API meteorológica

### ✅ Visão Computacional
- Detecção de pragas e doenças
- Classificação de imagens
- Processamento em tempo real

### ✅ Sistema de Alertas
- Notificações por email
- Notificações por SMS
- Monitoramento automático

### ✅ Gestão de Dados
- CRUD completo via API Flask (Fase 4) ⭐
- Integração com API meteorológica (OpenWeather)
- Armazenamento em cloud
- Backup automático

---

## 📈 Resultados e Métricas

### Machine Learning (Fase 4)
- **Modelo:** Decision Tree Classifier
- **Acurácia:** Alta precisão em predições de irrigação
- **Variáveis:** Umidade, pH, Fósforo, Potássio

### Visão Computacional (Fase 6)
- **YOLO Otimizado:** mAP@0.5 = 0.99
- **YOLO Tradicional:** mAP@0.5 = 0.67
- **CNN do Zero:** Acurácia = 94%

### Cloud Computing (Fase 5)
- **Região:** São Paulo (sa-east-1)
- **Custo Mensal:** ~US$ 11,22
- **Conformidade:** ISO 27001/27002

---

## 📚 Documentação

Cada fase possui sua própria documentação detalhada:

- [Fase 1 - Base de Dados Inicial](./fase1/README.md)
- [Fase 2 - Banco de Dados Estruturado](./fase2/README.md)
- [Fase 3 - IoT e Automação (Versão Inicial)](./fase3/README.md)
- [Fase 4 - IoT, Dashboard e ML (Versão Completa)](./fase4/README.md) ⭐
- [Fase 5 - Cloud Computing](./fase5/README.md)
- [Fase 6 - Visão Computacional](./fase6/README.md)
- [Fase 7 - Consolidação](./fase7/README.md)

### Documentação Adicional

- [Guia Rápido Fase 7](./fase7/docs/GUIA_RAPIDO.md)
- [Configuração AWS SNS](./fase7/docs/AWS_SNS_SETUP.md)

---

## 🎥 Vídeos de Apresentação

| Fase | Descrição | Link |
|------|-----------|------|
| Fase 3 | IoT e Automação (Versão Inicial) | [YouTube](https://youtu.be/ClA9DwxtclQ) |
| Fase 4 | IoT, Dashboard e ML (Versão Completa) | [YouTube](https://youtu.be/KEdM_Xw_xbk) |
| Fase 5 | Cloud Computing | [YouTube](https://youtu.be/Wqqj1hWZ_P4) |
| Fase 6 | Visão Computacional | [YouTube](https://youtu.be/pQkJcPUKa4c) |
| Fase 7 | Consolidação | [A ser adicionado] |

---

## 🤝 Contribuições

Este é um projeto acadêmico desenvolvido para a FIAP. Para contribuições ou dúvidas, entre em contato com os integrantes do grupo.

---

## 📞 Contato

**Tutor:** Leonardo Ruiz Orabona  
- GitHub: [@leoruiz197](https://github.com/leoruiz197)

**Coordenador:** André Godoi Chiovato

---

## 🗃️ Histórico de Versões

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0.0 | 2025-01-XX | Versão inicial - Consolidação completa das 7 fases |

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg">
<p>
<a href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a href="https://fiap.com.br">FIAP</a> está licenciado sob 
<a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Attribution 4.0 International</a>.
</p>

---

