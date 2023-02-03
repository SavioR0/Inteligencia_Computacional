# Funções e operações Fuzzy
Trata de mexer com informações imprecisas empregadas usualmente na comunicação humana.

> Sistema lógico que visa o raciocínio aproximado.
> 

Transforma o conhecimento tácito em explícito, capturando a experiência e o conhecimento do especialista humano.

Na lógica clássica, uma sentença só pode assumir um dentre os valores verdade: Verdadeiro ou Falso. Não existe situação intermediária.

A lógica fuzzy busca introduzir mecanismos que tornem mais suave a transição entre diferentes conceitos. Um deles é a **função de pertinência ( $\mu_a : x \rightarrow [0,1]$ - Elemento ‘x’ pertence ao conjunto ‘A’).**

> O grau de pertinência $\mu_a$ indica o quão o valor de x associado à $\mu_a$ é compatível com o conceito representado pelo conjunto A. Quanto mais próximo de 1 mais compatível é o x com o conceito representado pelo conjunto A.
>
---

Foram implementados em linguagem python as funções de pertinência mais comuns quando se aplica fuzzy. 
 - Triangular
 - Trapezoidal
 - Gaussianas

Além disso, as operações.
- Complementos:
    - Zadeh
    - Sugeno
    - Yeger

- União:
    - Máximo
    - Soma probabilistica
    - Soma Limitada
    - Soma Drástica

- Mínimo
- Produto
- Produto limitado
- Produto Drástico

