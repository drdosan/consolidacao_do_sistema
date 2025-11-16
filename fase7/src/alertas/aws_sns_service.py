"""
Serviço de Alertas AWS SNS
Sistema de mensageria para envio de alertas por email/SMS
"""

import boto3
import json
from datetime import datetime
from typing import Optional, Dict, Any
import os

class SNSService:
    """Serviço para envio de alertas via AWS SNS"""
    
    def __init__(self, region_name: str = "sa-east-1"):
        """
        Inicializa o serviço SNS
        
        Args:
            region_name: Região AWS (padrão: sa-east-1 - São Paulo)
        """
        self.region_name = region_name
        
        # Credenciais AWS (configurar via variáveis de ambiente ou arquivo de configuração)
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.topic_arn = os.getenv("SNS_TOPIC_ARN", "")
        
        # Inicializar cliente SNS
        try:
            if self.aws_access_key_id and self.aws_secret_access_key:
                self.sns_client = boto3.client(
                    'sns',
                    region_name=region_name,
                    aws_access_key_id=self.aws_access_key_id,
                    aws_secret_access_key=self.aws_secret_access_key
                )
            else:
                # Usar credenciais padrão do AWS CLI
                self.sns_client = boto3.client('sns', region_name=region_name)
        except Exception as e:
            print(f"⚠️ Erro ao inicializar cliente SNS: {e}")
            print("💡 Configure as credenciais AWS ou use AWS CLI")
            self.sns_client = None
    
    def enviar_alerta_email(self, assunto: str, mensagem: str, email_destino: str) -> bool:
        """
        Envia alerta por email via SNS
        
        Args:
            assunto: Assunto do email
            mensagem: Corpo da mensagem
            email_destino: Email de destino
            
        Returns:
            True se enviado com sucesso, False caso contrário
        """
        if not self.sns_client:
            print("❌ Cliente SNS não inicializado")
            return False
        
        try:
            # Criar mensagem formatada
            mensagem_formatada = f"""
            {mensagem}
            
            Data/Hora: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
            Sistema: FarmTech Solutions - Fase 7
            """
            
            # Se tiver topic ARN, publicar no tópico
            if self.topic_arn:
                response = self.sns_client.publish(
                    TopicArn=self.topic_arn,
                    Subject=assunto,
                    Message=mensagem_formatada
                )
            else:
                # Publicar diretamente (requer subscription prévia)
                response = self.sns_client.publish(
                    Subject=assunto,
                    Message=mensagem_formatada
                )
            
            print(f"✅ Alerta enviado com sucesso! MessageId: {response.get('MessageId')}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao enviar alerta: {e}")
            return False
    
    def enviar_alerta_sms(self, mensagem: str, telefone: str) -> bool:
        """
        Envia alerta por SMS via SNS
        
        Args:
            mensagem: Mensagem SMS (máximo 160 caracteres)
            telefone: Número de telefone no formato +5511999999999
            
        Returns:
            True se enviado com sucesso, False caso contrário
        """
        if not self.sns_client:
            print("❌ Cliente SNS não inicializado")
            return False
        
        try:
            # Limitar mensagem a 160 caracteres
            mensagem_curta = mensagem[:160] if len(mensagem) > 160 else mensagem
            
            response = self.sns_client.publish(
                PhoneNumber=telefone,
                Message=mensagem_curta
            )
            
            print(f"✅ SMS enviado com sucesso! MessageId: {response.get('MessageId')}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao enviar SMS: {e}")
            return False
    
    def alertar_umidade_baixa(self, umidade: float, sensor_id: int, email: str = None, telefone: str = None):
        """
        Envia alerta quando umidade está baixa
        
        Args:
            umidade: Valor da umidade detectada
            sensor_id: ID do sensor
            email: Email para envio (opcional)
            telefone: Telefone para SMS (opcional)
        """
        assunto = "⚠️ ALERTA: Umidade do Solo Baixa"
        mensagem = f"""
        ALERTA DE UMIDADE BAIXA
        
        O sensor {sensor_id} detectou umidade crítica: {umidade:.1f}%
        
        AÇÃO RECOMENDADA:
        - Verificar sistema de irrigação
        - Ativar irrigação imediatamente
        - Verificar possíveis vazamentos ou problemas no sistema
        
        Sensor ID: {sensor_id}
        Umidade: {umidade:.1f}%
        """
        
        if email:
            self.enviar_alerta_email(assunto, mensagem, email)
        
        if telefone:
            sms_msg = f"ALERTA: Umidade baixa ({umidade:.1f}%) no sensor {sensor_id}. Ativar irrigação!"
            self.enviar_alerta_sms(sms_msg, telefone)
    
    def alertar_ph_fora_limite(self, ph: float, sensor_id: int, email: str = None, telefone: str = None):
        """
        Envia alerta quando pH está fora dos limites
        
        Args:
            ph: Valor do pH detectado
            sensor_id: ID do sensor
            email: Email para envio (opcional)
            telefone: Telefone para SMS (opcional)
        """
        assunto = "⚠️ ALERTA: pH Fora dos Limites"
        mensagem = f"""
        ALERTA DE pH FORA DOS LIMITES
        
        O sensor {sensor_id} detectou pH crítico: {ph:.2f}
        
        AÇÃO RECOMENDADA:
        - Verificar necessidade de correção do solo
        - Aplicar calcário ou enxofre conforme necessário
        - Consultar agronômico para análise detalhada
        
        Sensor ID: {sensor_id}
        pH: {ph:.2f}
        Limite ideal: 6.0 - 7.5
        """
        
        if email:
            self.enviar_alerta_email(assunto, mensagem, email)
        
        if telefone:
            sms_msg = f"ALERTA: pH crítico ({ph:.2f}) no sensor {sensor_id}. Verificar correção do solo!"
            self.enviar_alerta_sms(sms_msg, telefone)
    
    def alertar_praga_detectada(self, tipo_praga: str, localizacao: str, email: str = None, telefone: str = None):
        """
        Envia alerta quando praga é detectada pela visão computacional
        
        Args:
            tipo_praga: Tipo de praga detectada
            localizacao: Localização da detecção
            email: Email para envio (opcional)
            telefone: Telefone para SMS (opcional)
        """
        assunto = "🐛 ALERTA: Praga Detectada"
        mensagem = f"""
        ALERTA DE PRAGA DETECTADA
        
        Sistema de visão computacional detectou: {tipo_praga}
        
        Localização: {localizacao}
        
        AÇÃO RECOMENDADA:
        - Inspecionar área imediatamente
        - Aplicar tratamento fitossanitário adequado
        - Isolar área se necessário
        - Registrar ocorrência no sistema
        
        Tipo: {tipo_praga}
        Local: {localizacao}
        """
        
        if email:
            self.enviar_alerta_email(assunto, mensagem, email)
        
        if telefone:
            sms_msg = f"ALERTA: Praga detectada ({tipo_praga}) em {localizacao}. Inspecionar área!"
            self.enviar_alerta_sms(sms_msg, telefone)
    
    def alertar_doenca_detectada(self, tipo_doenca: str, localizacao: str, email: str = None, telefone: str = None):
        """
        Envia alerta quando doença é detectada pela visão computacional
        
        Args:
            tipo_doenca: Tipo de doença detectada
            localizacao: Localização da detecção
            email: Email para envio (opcional)
            telefone: Telefone para SMS (opcional)
        """
        assunto = "🦠 ALERTA: Doença Detectada"
        mensagem = f"""
        ALERTA DE DOENÇA DETECTADA
        
        Sistema de visão computacional detectou: {tipo_doenca}
        
        Localização: {localizacao}
        
        AÇÃO RECOMENDADA:
        - Inspecionar área imediatamente
        - Aplicar tratamento fitossanitário adequado
        - Isolar área afetada
        - Consultar fitopatologista
        - Registrar ocorrência no sistema
        
        Tipo: {tipo_doenca}
        Local: {localizacao}
        """
        
        if email:
            self.enviar_alerta_email(assunto, mensagem, email)
        
        if telefone:
            sms_msg = f"ALERTA: Doença detectada ({tipo_doenca}) em {localizacao}. Inspecionar área!"
            self.enviar_alerta_sms(sms_msg, telefone)


# ==================== FUNÇÃO DE MONITORAMENTO ====================

def monitorar_sensores_e_alertar(umidade_min: float = 30.0, ph_min: float = 6.0, ph_max: float = 7.5,
                                  email: str = None, telefone: str = None):
    """
    Monitora leituras de sensores e envia alertas quando necessário
    
    Args:
        umidade_min: Umidade mínima aceitável
        ph_min: pH mínimo aceitável
        ph_max: pH máximo aceitável
        email: Email para envio de alertas
        telefone: Telefone para SMS
    """
    import pymysql
    from datetime import datetime, timedelta
    
    # Configuração do banco
    conn = pymysql.connect(
        host='192.185.217.47',
        user='bsconsul_fiap',
        password='Padr@ao321',
        database='bsconsul_fiap',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    sns = SNSService()
    
    try:
        with conn.cursor() as cur:
            # Buscar últimas leituras (última hora)
            uma_hora_atras = datetime.now() - timedelta(hours=1)
            cur.execute("""
                SELECT ls.*, si.cd_sensor_instalado
                FROM LEITURA_SENSOR ls
                JOIN SENSOR_INSTALADO si ON ls.cd_sensor_instalado = si.cd_sensor_instalado
                WHERE ls.data_hora >= %s
                ORDER BY ls.data_hora DESC
            """, (uma_hora_atras,))
            
            leituras = cur.fetchall()
            
            for leitura in leituras:
                sensor_id = leitura['cd_sensor_instalado']
                umidade = leitura.get('valor_umidade')
                ph = leitura.get('valor_ph')
                
                # Verificar umidade
                if umidade and umidade < umidade_min:
                    sns.alertar_umidade_baixa(umidade, sensor_id, email, telefone)
                
                # Verificar pH
                if ph and (ph < ph_min or ph > ph_max):
                    sns.alertar_ph_fora_limite(ph, sensor_id, email, telefone)
    
    except Exception as e:
        print(f"❌ Erro ao monitorar sensores: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    # Exemplo de uso
    print("🔔 Serviço de Alertas AWS SNS")
    print("=" * 50)
    
    # Inicializar serviço
    sns = SNSService()
    
    # Exemplo: alerta de umidade baixa
    # sns.alertar_umidade_baixa(25.5, sensor_id=1, email="admin@fazenda.com", telefone="+5511999999999")
    
    # Exemplo: alerta de praga
    # sns.alertar_praga_detectada("Lagarta", "Setor A - Quadra 3", email="admin@fazenda.com")
    
    print("💡 Configure as credenciais AWS para usar o serviço")
    print("💡 Exemplo: export AWS_ACCESS_KEY_ID='sua_chave'")

