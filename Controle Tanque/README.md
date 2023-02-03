# Controle Tanque


Foi implementado em linguagem python o controle de um tanque por um sistema Fuzzy. Não há controle da válvula de entrada, apenas na saída, além disso, é estabelecido um limiar desejável para o nível da água no tanque como mostra na ilustração.

![Tanque](https://github.com/SavioR0/inteligencia_computacional/issues/1#issue-1568950957)


Utilizou-se funções 6 funções trapezoidais para o erro (dado pela diferença entre o limiar e o nivel da água) e 4 funções trapezoidais para determinar a saída de água do reservatório (princial responsável pelo ajuste do nível da água).

