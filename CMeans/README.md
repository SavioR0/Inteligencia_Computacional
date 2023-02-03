# Cmeans
## Agrupamento por partição

Cada entidade é associado a somente um grupo. Buscam entidades que possuam maior semelhança entre si.

- Agrupamento Tradicional.
- Agrupamento Fuzzy.

### Construções de modelos

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc43cba2-7cf2-423d-81b3-e6549709f6e5/Untitled.png)

→ **Início**: Regras geradas por um especialista.

→ **Atual:** Regras definidas com base em informações extraídas de um conjunto de dados.

## Agrupamento por partição Crisp

### C-means

Selecionados c pontos aleatórios sobre o espaço (centróides ou protótipos).

Para cada entidade computamos um centróide mais próximo e rotulamos esse objetos como associado a tal centróide.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68481c71-273a-4d69-8053-0ddde45bbaab/Untitled.png)

- Define quantidade de grupos.
- Inicialize os centros dos grupos.
- Determine a matriz de pertinência.
- Calcule a função de custo (distância).
- Atualize os centros dos grupos.
- Repetir o passo 2, 3 e 4 até violar alguma condição de parada.