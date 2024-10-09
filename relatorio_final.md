
#### 4. `relatorio_final.md`

```markdown
# Relatório Final: Processamento de Imagens

## Introdução

Este relatório documenta o desenvolvimento e os resultados obtidos no projeto de processamento de imagens. Utilizando a biblioteca OpenCV e NumPy, várias técnicas foram implementadas para analisar e modificar imagens.

## Técnicas Implementadas

### 1. Leitura e Exibição de Imagens
As imagens foram carregadas usando `cv2.imread()`, e exibidas com `cv2.imshow()`.

### 2. Pré-processamento de Imagens
Imagens foram convertidas para escala de cinza e redimensionadas conforme necessário, facilitando operações subsequentes.

### 3. Aplicação de Filtros
Fui aplicados filtros como GaussianBlur, Canny e Sobel para suavização e detecção de bordas, melhorando a qualidade da imagem e permitindo uma análise mais eficaz.

### 4. Detecção de Características
Utilizamos detecção de contornos e cantos para identificar formas e características relevantes nas imagens, o que é essencial para a segmentação.

### 5. Transformações Geométricas
Implementamos transformações como rotacionamento e translação, permitindo alterar a posição e orientação das imagens.

### 6. Operações Morfológicas
Erosão e dilatação foram usadas para modificar a estrutura das imagens, ajudando na eliminação de ruídos e na realce de características importantes.

### 7. Segmentação de Imagens
O algoritmo Watershed foi implementado para segmentar as imagens, utilizando as informações dos contornos detectados.

### 8. Salvamento de Imagens Processadas
As imagens processadas foram salvas em diferentes formatos para análise posterior.

## Resultados Obtidos

As técnicas implementadas permitiram uma análise detalhada e melhorias significativas nas imagens. As imagens processadas mostraram melhorias em clareza e em características detectáveis. Cada funcionalidade foi testada em diferentes imagens, e os resultados foram satisfatórios.

## Conclusão

Este projeto demonstrou a eficácia das técnicas de processamento de imagens, mostrando como elas podem ser utilizadas para melhorar e analisar visualmente dados. As funcionalidades podem ser expandidas e melhoradas para aplicações mais complexas
