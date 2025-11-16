# 🌱 FarmTech Solutions - Fase 7: Consolidação do Sistema

<p align="center">
<a href="https://www.fiap.com.br/"><img src="../fase4/assets/logo-fiap.png" alt="FIAP" border="0" width=40% height=40%></a>
</p>

## 📋 Descrição

A **Fase 7** consolida todas as funcionalidades desenvolvidas nas Fases 1 a 6 em um sistema integrado de gestão agrícola. Este projeto integra:

- **Fase 1**: Cálculos de área de plantio e manejo de insumos
- **Fase 2**: Banco de dados estruturado (MySQL)
- **Fase 3**: Sistema IoT com ESP32 e sensores
- **Fase 4**: Dashboard com Machine Learning e predições
- **Fase 5**: Infraestrutura em Cloud Computing (AWS)
- **Fase 6**: Visão Computacional com YOLO
- **Fase 7**: Integração completa e sistema de alertas AWS SNS

## 👨‍🎓 Integrantes

| Matrícula | Aluno |
|-----------|-------|
| RM 565286 | Diogo Rebello dos Santos |
| RM 565497 | Vera Maria Chaves de Souza |

## 👩‍🏫 Professores

**Tutor:** Leonardo Ruiz Orabona  
**Coordenador:** André Godoi Chiovato

---

## 📁 Estrutura do Projeto

```
fase7/
├── src/
│   ├── dashboard/
│   │   └── main_dashboard.py          # Dashboard Streamlit integrado
│   ├── alertas/
│   │   ├── aws_sns_service.py         # Serviço AWS SNS para alertas
│   │   └── monitor_alertas.py         # Script de monitoramento contínuo
│   └── integracao/
│       ├── fase1_integracao.py        # Integração Fase 1
│       └── fase6_integracao.py        # Integração Fase 6
├── requirements.txt                    # Dependências Python
├── config_example.txt                  # Exemplo de configuração
└── README.md                           # Este arquivo
```

---

## 🚀 Instalação e Configuração

### 1. Pré-requisitos

- Python 3.8 ou superior
- MySQL (banco de dados configurado)
- Conta AWS com acesso ao SNS (para alertas)
- API Flask da Fase 3/4 rodando (opcional, mas recomendado)

### 2. Instalação

```bash
# Navegar para a pasta fase7
cd fase7

# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configuração

1. **Configurar credenciais AWS** (para alertas):
   ```bash
   export AWS_ACCESS_KEY_ID="sua_chave"
   export AWS_SECRET_ACCESS_KEY="sua_chave_secreta"
   export AWS_REGION="sa-east-1"
   export SNS_TOPIC_ARN="arn:aws:sns:sa-east-1:123456789:alertas-fazenda"
   ```

2. **Configurar variáveis de ambiente** (opcional):
   ```bash
   export EMAIL_ALERTAS="admin@fazenda.com"
   export TELEFONE_ALERTAS="+5511999999999"
   export UMIDADE_MIN=30.0
   export PH_MIN=6.0
   export PH_MAX=7.5
   ```

---

## 🎯 Como Executar

### Dashboard Integrado

```bash
cd src/dashboard
streamlit run main_dashboard.py
```

O dashboard estará disponível em: `http://localhost:8501`

### Serviço de Monitoramento de Alertas

```bash
cd src/alertas
python monitor_alertas.py
```

Este serviço monitora os sensores a cada 15 minutos e envia alertas quando necessário.

### API Flask (Fase 3/4)

Certifique-se de que a API está rodando:

```bash
cd ../fase3/api_crud  # ou fase4/src/api_crud
python app.py
```

---

## 📊 Funcionalidades do Dashboard

### 🏠 Página Inicial
- Visão geral do sistema
- Métricas principais
- Links rápidos para todas as fases

### 📊 Dashboard Principal
- Monitoramento em tempo real dos sensores
- Gráficos de umidade, pH, fósforo e potássio
- Predições do modelo de Machine Learning
- Tabela com últimas leituras

### 🌾 Fase 1 - Cálculos Agrícolas
- Calculadora de área de plantio
- Cálculo de insumos necessários
- Suporte para Café e Cana-de-açúcar

### 💾 Fase 2 - Banco de Dados
- Consultas ao banco de dados
- Visualização de produtores, culturas, sensores
- Estatísticas das leituras

### 🔌 Fase 3 - IoT e Sensores
- Status da API Flask
- Comandos para listar dados
- Verificação de status de irrigação

### 🤖 Fase 4 - Machine Learning
- Visualização do modelo treinado
- Previsão manual de necessidade de irrigação
- Estatísticas do modelo

### ☁️ Fase 5 - Cloud Computing
- Informações sobre infraestrutura AWS
- Detalhes de segurança e conformidade

### 👁️ Fase 6 - Visão Computacional
- Upload e processamento de imagens
- Detecção de pragas e doenças
- Resultados dos modelos YOLO e CNN

### 📧 Sistema de Alertas
- Configuração de alertas de sensores
- Configuração de alertas de visão computacional
- Integração com AWS SNS

---

## 🔔 Sistema de Alertas AWS SNS

O sistema de alertas monitora:

1. **Sensores (Fase 1/3)**:
   - Umidade baixa (< 30%)
   - pH fora dos limites (6.0 - 7.5)
   - Valores críticos de nutrientes

2. **Visão Computacional (Fase 6)**:
   - Detecção de pragas
   - Detecção de doenças
   - Crescimento irregular

### Configuração AWS SNS

1. **Criar Tópico SNS**:
   ```bash
   aws sns create-topic --name alertas-fazenda --region sa-east-1
   ```

2. **Inscrever Email**:
   ```bash
   aws sns subscribe \
     --topic-arn arn:aws:sns:sa-east-1:123456789:alertas-fazenda \
     --protocol email \
     --notification-endpoint admin@fazenda.com
   ```

3. **Inscrever SMS**:
   ```bash
   aws sns subscribe \
     --topic-arn arn:aws:sns:sa-east-1:123456789:alertas-fazenda \
     --protocol sms \
     --notification-endpoint +5511999999999
   ```

### Exemplo de Uso

```python
from src.alertas.aws_sns_service import SNSService

# Inicializar serviço
sns = SNSService()

# Enviar alerta de umidade baixa
sns.alertar_umidade_baixa(
    umidade=25.5,
    sensor_id=1,
    email="admin@fazenda.com",
    telefone="+5511999999999"
)

# Enviar alerta de praga detectada
sns.alertar_praga_detectada(
    tipo_praga="Lagarta",
    localizacao="Setor A - Quadra 3",
    email="admin@fazenda.com"
)
```

---

## 📸 Screenshots e Evidências

### Dashboard Integrado

O dashboard principal oferece uma visão consolidada de todas as funcionalidades:

- **Métricas em tempo real**: Umidade, pH, recomendações de irrigação
- **Gráficos interativos**: Visualização histórica dos dados
- **Navegação intuitiva**: Acesso fácil a todas as fases

### Sistema de Alertas

O sistema de alertas AWS SNS envia notificações quando:

- Sensores detectam valores críticos
- Visão computacional identifica problemas
- Decisões de irrigação são tomadas

---

## 🔧 Integração com Outras Fases

### Fase 1
- Cálculos de área e insumos integrados no dashboard
- Interface web para entrada de dados

### Fase 2
- Consultas diretas ao banco de dados MySQL
- Visualização de todas as tabelas

### Fase 3
- Integração com API Flask
- Comandos para listar e gerenciar dados

### Fase 4
- Modelo de ML carregado e aplicado em tempo real
- Previsões integradas no dashboard

### Fase 5
- Documentação da infraestrutura AWS
- Informações de segurança e conformidade

### Fase 6
- Upload e processamento de imagens
- Detecção de problemas na plantação

---

## 📝 Entregáveis

1. ✅ **Dashboard Integrado** (`src/dashboard/main_dashboard.py`)
   - Interface única para todas as fases
   - Navegação por menu lateral
   - Visualizações em tempo real

2. ✅ **Sistema de Alertas AWS SNS** (`src/alertas/`)
   - Serviço de mensageria completo
   - Suporte a email e SMS
   - Monitoramento automático

3. ✅ **Scripts de Integração** (`src/integracao/`)
   - Wrappers para funcionalidades das fases
   - Facilita reutilização de código

4. ✅ **Documentação Completa** (`README.md`)
   - Instruções de instalação
   - Guia de uso
   - Exemplos de código

---

## 🎥 Vídeo de Apresentação

**Link do vídeo:** [https://youtu.be/-6ii1At-Q8o](https://youtu.be/-6ii1At-Q8o)

O vídeo apresenta:
- Todas as funcionalidades das Fases 1 a 6
- Dashboard integrado da Fase 7
- Sistema de alertas em ação
- Demonstração prática do sistema

---

## 🔗 Links Importantes

- **GitHub:** https://github.com/drdosan/consolidacao_do_sistema 
- **API Swagger:** http://localhost:5000/apidocs
- **Dashboard:** http://localhost:8501
- **Calculadora AWS:** https://calculator.aws/#/estimate?id=ce53bf9cd6f5d5c5465fb6329e28c118fa8d0ca0 
---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit** - Dashboard web
- **Flask** - API REST
- **MySQL** - Banco de dados
- **AWS SNS** - Sistema de mensageria
- **Scikit-learn** - Machine Learning
- **Boto3** - SDK AWS
- **Pandas** - Manipulação de dados
- **SQLAlchemy** - ORM

---

## 🗃️ Histórico de Versões

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0.0 | 2025-01-XX | Versão inicial - Consolidação Fase 7 |

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg">
<p>
<a href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a href="https://fiap.com.br">FIAP</a> está licenciado sob 
<a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Attribution 4.0 International</a>.
</p>
