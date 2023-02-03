# RNA de camada simples/ Percepron
Conexionismo → A criação de máquinas inteligentes é possível a partir da reprodução e interconexão dos elementos de processamento do cérebro dos animais.

Neurônio artificial é um modelo matemático simplificado do processamento existente em um neurônio  biológico.

## MCP

Nesse modelo é as entradas são binárias dependendo da presença ou ausência de um impulso de entrada no instante de tempo k.

$W_i$ são os pesos multiplicativos conectando a entrada i ao núcleo do neurônio.

Saída também é 0 ou 1.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3d8aa01-b2e5-44f4-8938-570a0170176a/Untitled.png)

Atualmente são utilizados neurônio mais complexos que o MCP. Mas sempre podendo ter múltiplas entradas e um única saída.

## Neurônios

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0c120e19-e1bc-4230-9603-092c9a8fec79/Untitled.png)

A função f é comumente chamada de Função de Ativação do neurônio.

O limiar de Ativação D do neurônio pode ser embutido na variável sem perda de generalização.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dc16920f-b625-4ea5-ba99-50602649c743/Untitled.png)

## Funções de ativação

### Degrau e o sinal

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ada98bb-da4b-4e46-b47c-e13221cb6396/Untitled.png)

- $y=1$, se $net \geq 0$ ou $y=0$, se $net < 0$
- $y=1$, se $net \geq 0$ ou $y=-1$, se $net < 0$

## Funções Lineares com e sem saturação da saída

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5af0fade-c70c-4d48-9a4b-b92f275eae06/Untitled.png)

- $y=1$, se $net > 0$ ou $y= net$ se $-1< net < 1$, ou $y = -1$  se $net < -1$
- $y = \lambda net$

## Funções Sigmodais unipolares e bipolares

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a79f8bd-d505-4e72-8bfe-0356daff214d/Untitled.png)

- $y = \frac{1}{1+e^{\lambda net}}$
- $y = \frac{2}{1+e^{\lambda net}}- 1$


### Redes de Camada Simples

Primeiro modelo neural com capacidade de aprendizado.

> Uma máquina Adaptativa capaz de classificar padrões de entrada pela modificação das conexões de entrada nos neurônios com funções de limiar de saída.
> 

Em redes com um único perceptron, o espaço de entrada n-dimensional é dividido por um hiper-plano em duas regiões de decisão.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0056dba1-1010-4b77-b2f6-08c17c66924d/Untitled.png)

Com três estradas a fronteira de decisão tem a forma de um plano de separação.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fee10548-684d-48d9-a068-5f437cefee7f/Untitled.png)

 A escolha da superfície é comumente chamado de **Treinamento**.

→ Ajustes sucessivos nos pesos para diminuir a diferença entre a saída desejada e a saída real do neurônio.

→ Denominado aprendizado supervisionado.

Nessa arquitetura , existe apenas uma camada de entrada, composta por nós de distribuição que conectam com uma camada de saída composta de neurônios (ou nós de processamento).

O fluxo do sinal é unidirecional, em direção à saída.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3cb35f3a-04c1-41e8-bc65-55017f8f44a3/Untitled.png)

---
Com opção de esolha entre classificação e regressão, o presente trabalho implementa um problema de regressão para a base de dados AirfoilDataset. Foram utilizadas a regressão linear e a dos K vizinhos mais próximos pela bibliotea sklearn.
