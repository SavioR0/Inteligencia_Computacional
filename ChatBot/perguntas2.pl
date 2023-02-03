:-include(perguntas1).

pergunta("Contratar planos", Numero, Clien):-
    format("Aqui estão todos as opçoes de planos. Escolha a opção  que deseja. "),
    format("\n 1- Plano 1\n 2- Plano 2 \n 3- Plano 3\n"),
    read(Entrada1),
    pergunta1(Entrada1,  Numero, Clien).

pergunta("Cancelar planos",Numero, Clien):-
    format("Plano Cancelado com sucesso!"),
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta("Recarregar",  Numero, Clien):-
    format("Selecione a opção de recarga que deseja :"),
    format("\n 1- 10 reias \n 2- 20 reias \n 3- 25 reais \n 4- 50 reais \n 5- Outro \n"),
    read(Entrada),
    pergunta3(Entrada, Numero, Clien).

pergunta("Renovar plano vigente", Numero, Clien ):-
    format("Solicitação de renovação de plano realizada com sucesso"),
    format("Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta("Relatar problemas",Numero , Clien):-
    format("Digite o problema:"),
    read(Problema),
    format("Problema foi salvo e enviado ao sistema. Assunto :"),
    write(Problema),nl,
    format("Solicitação de renovação de plano realizada com sucesso"),nl,
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).




%Pergunta 1
pergunta1("Plano 1", " Plano 1 Contratado com sucesso!", Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta1("Plano 2", " Plano 2 Contratado com sucesso!", Numero, Clien):-
    format("\nDeseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta1("Plano 3", " Plano 3 Contratado com sucesso!", Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta1(X, " Plano 3 Contratado com sucesso!", Numero, Clien):-
    format("Comando "),
    write(X),
    format("não é válido"),
    chatbot(Numero, Clien).


%Pergunta 3
pergunta3("10 reais", "Recarga de 10 reais realizada com sucesso", Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).
pergunta3("20 reais", "Recarga de 20 reais realizada com sucesso", Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).
pergunta3("25 reais", "Recarga de 25 reais realizada com sucesso", Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).
pergunta3("50 reais", "Recarga de 50 reais realizada com sucesso", Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta3("Outro", "Recarga Personalizada realizada com sucesso", Numero, Clien):-
    format("Digite o valor que deseja recarregar :"),
    read(Valor),
    pergunta31(Valor, Numero, Clien).
