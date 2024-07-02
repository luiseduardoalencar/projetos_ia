# Projetos de Deep Learning e Visão Computacional

Este repositório contém dois projetos principais, cada um abordando um aspecto diferente do aprendizado de máquina e da visão computacional. 

## 1. Análise e Previsão de Tendências em Dados de Mercado Financeiro

### Previsão de Preços com LSTM
Este projeto utiliza uma abordagem de aprendizado profundo para prever os preços das ações da Petrobras. Usando redes neurais recorrentes Long Short-Term Memory (LSTM), conseguimos capturar padrões temporais nos dados históricos e fazer previsões precisas sobre os preços futuros das ações.

### Funcionalidades
- Coleta de dados históricos de preços de ações.
- Pré-processamento de dados para alimentar o modelo LSTM.
- Treinamento e validação do modelo LSTM.
- Geração de previsões e visualização dos resultados.


## 2. Projeto de Reconhecimento de Objetos em Imagens para Segmentação de Compras

### Detecção de Objetos com YOLO e Darknet
Este projeto envolve a detecção de objetos usando o modelo YOLO (You Only Look Once) e a plataforma Darknet. Ele é projetado para segmentação de compras, permitindo a identificação precisa de diferentes produtos em imagens.

### Funcionalidades
- Carregamento e pré-processamento de imagens.
- Utilização do modelo YOLOv4 para detecção de objetos.
- Segmentação de compras baseada em detecção de objetos.
- Visualização dos resultados de detecção.


### Importante
O arquivo `yolov4.weights` contém os parâmetros que definem como o modelo YOLOv4 identifica e localiza objetos em imagens ou vídeos, tornando-o um recurso valioso para aplicações de visão computacional que envolvem detecção de objetos em tempo real, sendo extremamente importante para a execução do modelo. 

Caso queira executar o modelo mais robusto e exato na identificação, baixe os parâmetros necessários para executar no [link a seguir](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights). O `yolov4.weights` é a versão mais completa e robusta dos parâmetros do YOLOv4, já a versão `yolov4-tiny.weights` é uma versão focada no equilíbrio entre velocidade e precisão, sendo uma versão mais simplificada e leve do YOLOv4 original.


### Links Úteis
- [YOLOv4 Pesos](https://github.com/AlexeyAB/darknet#pre-trained-models)
- [Documentação do Darknet](https://pjreddie.com/darknet/)

---

Sinta-se à vontade para contribuir com este repositório através de pull requests. Para maiores dúvidas ou sugestões, abra uma issue ou entre em contato.
