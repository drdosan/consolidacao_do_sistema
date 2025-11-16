# 🔧 Instalação de Bibliotecas para Processamento de Imagens (Fase 6)

Para usar o processamento real de imagens com YOLO e CNN, é necessário instalar as bibliotecas abaixo.

## 📦 Instalação

### ⚠️ IMPORTANTE: Conflito de Dependências

O `yolov5` tenta instalar `Pillow 12.0.0`, mas o `streamlit` requer `Pillow < 11.0.0`. 

**Solução:** Instale o Pillow compatível ANTES de instalar o yolov5:

```bash
# 1. Primeiro, instale Pillow compatível
pip install "Pillow>=7.1.0,<11.0.0"

# 2. Depois, instale yolov5 (ele não atualizará o Pillow)
pip install yolov5
```

### Opção 1: Instalação Completa (Recomendado)

```bash
# Instalar Pillow compatível primeiro
pip install "Pillow>=7.1.0,<11.0.0"

# Depois instalar yolov5 e outras dependências
pip install yolov5 torch torchvision
```

### Opção 2: Instalação Individual

#### Para YOLO:
```bash
# Instalar Pillow compatível primeiro
pip install "Pillow>=7.1.0,<11.0.0"

# Depois instalar yolov5
pip install yolov5
```

**⚠️ IMPORTANTE:** Use `yolov5` (não `ultralytics`), pois os modelos foram treinados com YOLOv5 e não são compatíveis com YOLOv8/YOLOv11.

#### Para CNN:
```bash
pip install torch torchvision "Pillow>=7.1.0,<11.0.0"
```

## ✅ Verificação

Após a instalação, você pode verificar se está funcionando:

```python
# Verificar YOLO
import yolov5
print("✅ YOLOv5 instalado com sucesso!")

# Verificar PyTorch
import torch
print(f"✅ PyTorch instalado - Versão: {torch.__version__}")

# Verificar Pillow (deve ser < 11.0.0)
import PIL
print(f"✅ Pillow instalado - Versão: {PIL.__version__}")
```

## 🎯 Modelos Disponíveis

Os modelos treinados estão localizados em:

- **YOLO Otimizado:** `fase6/dataset/runs/roupas_200ep/weights/best.pt`
- **YOLO Tradicional:** `fase6/dataset/runs/roupas_60ep/weights/best.pt`
- **CNN:** `fase6/dataset/runs/cnn_from_scratch.pt`

## 📝 Notas

- Os modelos foram treinados para detectar **blusas** e **sapatos**
- Se você fizer upload de uma imagem que não contenha esses objetos, o resultado será "Nenhuma detecção encontrada"
- O threshold de confiança está configurado em 0.1 (10%)

## 🐛 Troubleshooting

### Erro: "streamlit requires pillow<11,>=7.1.0, but you have pillow 12.0.0"
**Solução:** 
```bash
# Desinstalar Pillow 12
pip uninstall Pillow

# Instalar versão compatível
pip install "Pillow>=7.1.0,<11.0.0"

# Reinstalar yolov5 (se necessário)
pip install --force-reinstall --no-deps yolov5
```

### Erro: "No module named 'yolov5'"
**Solução:** `pip install yolov5` (após instalar Pillow compatível)

### Erro: "appears to be an Ultralytics YOLOv5 model... NOT forwards compatible with YOLOv8"
**Solução:** Use `yolov5` (não `ultralytics`). Os modelos foram treinados com YOLOv5 e requerem a biblioteca `yolov5`.

### Erro: "No module named 'torch'"
**Solução:** `pip install torch torchvision`

### Modelos não encontrados
**Solução:** Verifique se os arquivos `.pt` estão na pasta `fase6/dataset/runs/`

---

**Última atualização:** 2025-01-XX
