# 📧 Guia de Configuração AWS SNS - Sistema de Alertas

Este guia explica como configurar o serviço AWS SNS para envio de alertas por email e SMS.

## 📋 Pré-requisitos

1. Conta AWS ativa
2. Acesso ao console AWS
3. Permissões para criar tópicos SNS
4. Credenciais AWS (Access Key ID e Secret Access Key)

## 🔧 Passo a Passo

### 1. Criar Tópico SNS

1. Acesse o [Console AWS SNS](https://console.aws.amazon.com/sns/)
2. Selecione a região **São Paulo (sa-east-1)**
3. Clique em **"Tópicos"** no menu lateral
4. Clique em **"Criar tópico"**
5. Configure:
   - **Tipo:** Tópico padrão
   - **Nome:** `alertas-fazenda`
   - **Nome de exibição:** `Alertas Fazenda`
6. Clique em **"Criar tópico"**
7. **Copie o ARN do tópico** (exemplo: `arn:aws:sns:sa-east-1:123456789:alertas-fazenda`)

### 2. Inscrever Email

1. No tópico criado, clique em **"Criar assinatura"**
2. Configure:
   - **Protocolo:** Email
   - **Endpoint:** Seu email (ex: `admin@fazenda.com`)
3. Clique em **"Criar assinatura"**
4. **Verifique seu email** e confirme a assinatura clicando no link recebido

### 3. Inscrever SMS (Opcional)

1. No tópico criado, clique em **"Criar assinatura"**
2. Configure:
   - **Protocolo:** SMS
   - **Endpoint:** Número de telefone no formato `+5511999999999` (com código do país)
3. Clique em **"Criar assinatura"**
4. Você receberá um SMS de confirmação

### 4. Configurar Credenciais AWS

#### Opção 1: Variáveis de Ambiente (Recomendado)

```bash
# Windows (PowerShell)
$env:AWS_ACCESS_KEY_ID="sua_chave_aqui"
$env:AWS_SECRET_ACCESS_KEY="sua_chave_secreta_aqui"
$env:AWS_REGION="sa-east-1"
$env:SNS_TOPIC_ARN="arn:aws:sns:sa-east-1:123456789:alertas-fazenda"

# Linux/Mac
export AWS_ACCESS_KEY_ID="sua_chave_aqui"
export AWS_SECRET_ACCESS_KEY="sua_chave_secreta_aqui"
export AWS_REGION="sa-east-1"
export SNS_TOPIC_ARN="arn:aws:sns:sa-east-1:123456789:alertas-fazenda"
```

#### Opção 2: Arquivo de Credenciais AWS

Crie o arquivo `~/.aws/credentials`:

```ini
[default]
aws_access_key_id = sua_chave_aqui
aws_secret_access_key = sua_chave_secreta_aqui
region = sa-east-1
```

### 5. Obter Credenciais AWS

1. Acesse o [Console IAM](https://console.aws.amazon.com/iam/)
2. Clique em **"Usuários"** no menu lateral
3. Selecione seu usuário ou crie um novo
4. Vá para a aba **"Credenciais de segurança"**
5. Clique em **"Criar chave de acesso"**
6. **Salve as credenciais** em local seguro (não compartilhe!)

### 6. Configurar Permissões IAM

O usuário precisa das seguintes permissões:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish",
                "sns:Subscribe",
                "sns:CreateTopic"
            ],
            "Resource": "*"
        }
    ]
}
```

## 🧪 Testar Configuração

Execute o script de teste:

```python
from src.alertas.aws_sns_service import SNSService

# Inicializar serviço
sns = SNSService()

# Testar envio de email
sns.alertar_umidade_baixa(
    umidade=25.5,
    sensor_id=1,
    email="seu_email@exemplo.com"
)

# Testar envio de SMS
sns.alertar_umidade_baixa(
    umidade=25.5,
    sensor_id=1,
    telefone="+5511999999999"
)
```

## 📊 Monitoramento

### Verificar Envios

1. Acesse o [Console AWS SNS](https://console.aws.amazon.com/sns/)
2. Selecione seu tópico
3. Vá para a aba **"Métricas"**
4. Visualize estatísticas de envio

### Logs CloudWatch

Os logs de envio são automaticamente registrados no CloudWatch:
- Acesse [CloudWatch Logs](https://console.aws.amazon.com/cloudwatch/)
- Procure por logs do SNS

## 💰 Custos

### Email
- **Gratuito** para até 1.000 emails/mês
- Após isso: US$ 0,10 por 1.000 emails

### SMS
- **Brasil:** ~US$ 0,06475 por SMS
- Varia por país

### Tópicos SNS
- **Gratuito** (até 100.000 tópicos)

## 🔒 Segurança

1. **Nunca compartilhe** suas credenciais AWS
2. Use **IAM roles** em produção (não credenciais hardcoded)
3. **Rotacione** as chaves periodicamente
4. Use **políticas IAM** restritivas (princípio do menor privilégio)

## 🐛 Troubleshooting

### Erro: "Unable to locate credentials"

**Solução:** Configure as variáveis de ambiente ou arquivo de credenciais

### Erro: "Access Denied"

**Solução:** Verifique as permissões IAM do usuário

### Email não recebido

**Solução:** 
1. Verifique a pasta de spam
2. Confirme a assinatura no email
3. Verifique se o endpoint está correto no SNS

### SMS não recebido

**Solução:**
1. Verifique o formato do número (+5511999999999)
2. Verifique se o número está inscrito no tópico
3. Verifique limites de SMS da AWS (pode haver throttling)

## 📚 Referências

- [Documentação AWS SNS](https://docs.aws.amazon.com/sns/)
- [Preços AWS SNS](https://aws.amazon.com/sns/pricing/)
- [Guia IAM](https://docs.aws.amazon.com/iam/)

## ✅ Checklist

- [ ] Tópico SNS criado
- [ ] Email inscrito e confirmado
- [ ] SMS inscrito (opcional)
- [ ] Credenciais AWS configuradas
- [ ] Permissões IAM configuradas
- [ ] Teste de envio realizado
- [ ] Variáveis de ambiente configuradas
- [ ] Monitoramento configurado

---

**Última atualização:** 2025-01-XX

