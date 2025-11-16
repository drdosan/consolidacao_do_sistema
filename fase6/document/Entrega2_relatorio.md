# 📘 Entrega 2 — Comparação de Abordagens em Visão Computacional

Este relatório apresenta a **análise comparativa** entre três métodos desenvolvidos na Fase 6 do projeto **FarmTech Solutions**:

1. **YOLO Otimizado** — rede YOLOv5 com hiperparâmetros ajustados e imagens de 832 px;  
2. **YOLO Tradicional** — rede YOLOv5 padrão, com parâmetros *default* e imagens de 640 px;  
3. **CNN do Zero** — rede convolucional simples para classificação binária (*blusas vs sapatos*).

---

## 1️⃣ Resumo dos Experimentos

| Abordagem | Dataset | Épocas | Resolução | Observações |
|------------|----------|:------:|:----------:|-------------|
| YOLO Otimizado | 80 imagens rotuladas | 100 / 200 | 832 px | *Hiperparâmetros customizados, melhor precisão.* |
| YOLO Tradicional | 80 imagens rotuladas | 30 / 60 | 640 px | *Configuração default YOLOv5n.* |
| CNN do Zero | 80 imagens (pasta por classe) | 20 | 224 px | *TinyCNN com 4 camadas conv + MLP.* |

---

## 2️⃣ Resultados Numéricos

### YOLO (Detecção)

| Modelo | Épocas | mAP@0.5 | Precisão | Recall |
|---------|:------:|:-------:|:---------:|:-------:|
| YOLO Tradicional | 30 | 0.56 | 0.82 | 0.83 |
| YOLO Tradicional | 60 | 0.67 | 1.00 | 0.96 |
| YOLO Otimizado | 100 | 0.97 | 1.00 | 1.00 |
| YOLO Otimizado | 200 | 0.99 | 1.00 | 1.00 |

### CNN (Classificação)

| Classe | Precisão | Recall | F1-score |
|---------|:---------:|:--------:|:---------:|
| Blusa | 0.93 | 0.92 | 0.92 |
| Sapato | 0.94 | 0.95 | 0.94 |
| **Acurácia global** | — | — | **0.94** |

**Tempo médio de inferência (s/img):**  
• YOLO Otimizado ≈ 0.07 • YOLO Tradicional ≈ 0.05 • CNN ≈ 0.002  

---

## 3️⃣ Comparativo Crítico

| Critério | YOLO Otimizado | YOLO Tradicional | CNN do Zero |
|-----------|----------------|------------------|--------------|
| **Facilidade de uso** | Exige dataset rotulado e tuning | Fácil (defaults) | Muito simples (ImageFolder) |
| **Precisão** | ★ Altíssima (mAP ≈ 0.99) | Boa (mAP ≈ 0.67) | Alta (Acurácia ≈ 94 %) |
| **Tempo de treino** | Longo (≈ 10 min / 200 ép.) | Rápido (≈ 3 min / 60 ép.) | Muito rápido (≈ 1 min / 20 ép.) |
| **Tempo de inferência** | 0.07 s/img | 0.05 s/img | 0.002 s/img |
| **Aplicabilidade** | Detecção e localização (inventário, segurança) | Baseline de detecção | Classificação binária rápida |

---

## 4️⃣ Análise Crítica

- **YOLO Otimizado** obteve o melhor desempenho geral e é indicado quando a **localização** dos objetos é necessária.  
- **YOLO Tradicional** serviu como **baseline**, evidenciando o ganho de performance com o ajuste de hiperparâmetros.  
- **CNN do Zero** teve **excelente acurácia** com custo computacional mínimo, ideal para **classificação simples** sem necessidade de coordenadas.

---

## 5️⃣ Conclusões

- O **YOLOv5** é superior para **detecção em tempo real** e **localização de múltiplos objetos**.  
- A **CNN do Zero** é mais leve e indicada para **triagens rápidas ou classificações binárias**.  
- Ajustes de *hyperparameters* e resolução são determinantes para a performance.  
- Cada abordagem tem seu **cenário ideal de uso**, reforçando o aprendizado de **trade-offs** entre acurácia, custo e aplicabilidade.

---

