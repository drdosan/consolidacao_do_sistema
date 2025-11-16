"""
Script de Monitoramento e Alertas
Executa monitoramento contínuo e envia alertas quando necessário
"""

import time
import schedule
from aws_sns_service import monitorar_sensores_e_alertar, SNSService
import os

# Configurações
UMIDADE_MIN = float(os.getenv("UMIDADE_MIN", "30.0"))
PH_MIN = float(os.getenv("PH_MIN", "6.0"))
PH_MAX = float(os.getenv("PH_MAX", "7.5"))
EMAIL_ALERTAS = os.getenv("EMAIL_ALERTAS", "")
TELEFONE_ALERTAS = os.getenv("TELEFONE_ALERTAS", "")

def executar_monitoramento():
    """Executa uma rodada de monitoramento"""
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 🔍 Executando monitoramento...")
    
    try:
        monitorar_sensores_e_alertar(
            umidade_min=UMIDADE_MIN,
            ph_min=PH_MIN,
            ph_max=PH_MAX,
            email=EMAIL_ALERTAS if EMAIL_ALERTAS else None,
            telefone=TELEFONE_ALERTAS if TELEFONE_ALERTAS else None
        )
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ✅ Monitoramento concluído")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ❌ Erro no monitoramento: {e}")

def main():
    """Função principal - executa monitoramento em intervalos"""
    print("🚀 Iniciando serviço de monitoramento de alertas")
    print("=" * 60)
    print(f"Configurações:")
    print(f"  - Umidade mínima: {UMIDADE_MIN}%")
    print(f"  - pH mínimo: {PH_MIN}")
    print(f"  - pH máximo: {PH_MAX}")
    print(f"  - Email: {EMAIL_ALERTAS if EMAIL_ALERTAS else 'Não configurado'}")
    print(f"  - Telefone: {TELEFONE_ALERTAS if TELEFONE_ALERTAS else 'Não configurado'}")
    print("=" * 60)
    
    # Agendar execução a cada 15 minutos
    schedule.every(15).minutes.do(executar_monitoramento)
    
    # Executar imediatamente na primeira vez
    executar_monitoramento()
    
    # Loop principal
    print("\n⏰ Monitoramento agendado para executar a cada 15 minutos")
    print("💡 Pressione Ctrl+C para parar\n")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Verificar a cada minuto
    except KeyboardInterrupt:
        print("\n\n🛑 Serviço de monitoramento interrompido pelo usuário")

if __name__ == "__main__":
    main()

