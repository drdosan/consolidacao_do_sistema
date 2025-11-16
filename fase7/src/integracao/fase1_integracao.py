"""
Integração Fase 1 - Cálculos Agrícolas
Wrapper para funcionalidades da Fase 1
"""

import sys
from pathlib import Path

# Adicionar caminho da Fase 1 ao path
BASE_DIR = Path(__file__).parent.parent.parent.parent
FASE1_DIR = BASE_DIR / "fase1" / "cultura-python"
sys.path.insert(0, str(FASE1_DIR))

def calcular_area(diagonal_maior: float, diagonal_menor: float) -> float:
    """Calcula a área de um losango"""
    return (diagonal_maior * diagonal_menor) / 2

def calcular_quantidade_ruas(diagonal_maior: float, espacamento: float) -> int:
    """Calcula a quantidade de ruas na lavoura"""
    return round(diagonal_maior / espacamento)

def calcular_insumos(area: float, dosagem: float, ruas: int, espacamento: float) -> float:
    """Calcula a quantidade total de insumos necessários"""
    area_util = area - (ruas * espacamento)
    if area_util < 0:
        area_util = 0
    return round(area_util * dosagem)

def obter_insumos_disponiveis(cultura: str) -> list:
    """Retorna lista de insumos disponíveis para a cultura"""
    INSUMOS_CAFE = ["Fosfato Monoamônico (MAP)", "Sulfato de Amônio", "Calcário Dolomítico"]
    INSUMOS_CANA = ["Ureia", "Cloreto de Potássio", "Superfosfato Simples"]
    
    if cultura.lower() == "café":
        return INSUMOS_CAFE
    elif cultura.lower() in ["cana", "cana-de-açúcar"]:
        return INSUMOS_CANA
    else:
        return []

def calcular_plantacao(cultura: str, diagonal_maior: float, diagonal_menor: float, dosagem: float) -> dict:
    """
    Calcula todos os parâmetros de uma plantação
    
    Returns:
        Dicionário com todos os cálculos
    """
    area = calcular_area(diagonal_maior, diagonal_menor)
    espacamento = 3.6 if cultura.lower() == "café" else 1.5
    ruas = calcular_quantidade_ruas(diagonal_maior, espacamento)
    area_util = area - (ruas * espacamento)
    if area_util < 0:
        area_util = 0
    insumo_total = calcular_insumos(area, dosagem, ruas, espacamento)
    insumos = obter_insumos_disponiveis(cultura)
    
    return {
        "cultura": cultura,
        "area_total": area,
        "area_util": area_util,
        "espacamento": espacamento,
        "quantidade_ruas": ruas,
        "dosagem": dosagem,
        "insumo_total": insumo_total,
        "insumos_disponiveis": insumos
    }

if __name__ == "__main__":
    # Exemplo de uso
    resultado = calcular_plantacao("Café", 100.0, 80.0, 0.5)
    print("Resultado do cálculo:")
    print(resultado)

