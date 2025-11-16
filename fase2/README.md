# 🌱 FarmTech Solutions - Monitoramento Inteligente Agrícola

Este projeto modela um banco de dados relacional para sensoriamento agrícola utilizando SQL Developer Data Modeler.

## Objetivo

Ajudar produtores a monitorar condições do solo e tomar decisões com base em dados de sensores (umidade, pH e nutrientes).

## Entidades

- `Produtor`: responsável pelas culturas.
- `Cultura`: tipos de plantações monitoradas.
- `Sensor`: dispositivos de leitura instalados nas culturas.
- `SensorInstalado`: vínculo entre sensores e culturas.
- `LeituraSensor`: dados capturados (umidade, pH, nutrientes).
- `AplicacaoRecurso`: registro de água aplicada.
- `Nutriente`: tipos de nutrientes usados.
- `AplicacaoNutriente`: relação N:N entre aplicação e nutrientes.

## Relacionamentos

- Um produtor pode ter várias culturas.
- Sensores são instalados em culturas específicas.
- Leituras estão vinculadas a sensores instalados.
- Aplicações de recursos estão ligadas às culturas.
- Nutrientes são aplicados em N:N via tabela intermediária.

## Arquivos

- `farmtech_database.dmd`: arquivo do SQL Developer Data Modeler
- `DER.png`: imagem do DER
- `MAPA_LOGICO.png`: imagem do Mapa Lógico
- `README.md`: este documento

## Autor

Desenvolvido para fins acadêmicos.

Alunos:
- VERA MARIA CHAVES DE SOUZA - RM 565497
- PATRÍCIA DE JESUS FERREIRA - RM 565558
- DIOGO REBELLO DOS SANTOS - RM 565286
- MARCOS VINÍCIUS DOS SANTOS FERNANDES - RM 565555
- ANDRÉ DE OLIVEIRA SANTOS BURGER - RM 565150
