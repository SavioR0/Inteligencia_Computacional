# MLP - Rede de Múltiplas Camadas

Uma vantagem da utilização de redes neurais de múltiplas camadas é que com duas ou mais camadas ocultas, a rede é capaz de aproximar qualquer função não linear, mesmo que descontínua. Um exemplo é a função XOR, cuja convergência não é atingida quando executada em uma rede neural de camada simples por exemplo. Nesse contexto, o presente trabalho busca resolver esse problema em uma MLP.

---
- Estrada → Não conta como camada.
- Camadas ocultas.
- Camada de saída.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/20d317ec-3245-4e5e-b8ba-ef1f58c4b11c/Untitled.png)

A saída de uma camada é a entrada para a próxima camada.

- Fluxo de sinal unidirecional
- Uma camada de entrada
- Uma ou mais camadas escondidas .
- Uma camada de saída.

Quanto mais camadas mais pesos, mais custo, mais tempo.

tipicamente os neurônios de uma camada são completamente conectados, ou seja, cada neurônio é conectado a cada um dos neurônios da camada subsequente