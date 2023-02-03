:-include(banco_de_dados1).
:-include(chatbot).

pergunta(1, Numero, Clien):-

    plano(Numero, Plan), Plan == not(0)-> format("Já possui um plano cadastrado : Plano "), write(Plan), nl, chatbot(Numero, Clien);

    (format("Aqui estão todos as opçoes de planos. Escolha a opção  que deseja. "),
    format("\n 1- Plano 1\n 2- Plano 2 \n 3- Plano 3\n"),
    read(Entrada1),
    pergunta1(Entrada1, Numero, Clien)).

pergunta(2,Numero, Clien):-
    asserta(plano(Numero,0)),
    format("Plano Cancelado com sucesso!"),
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não"),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta(3, Numero, Clien):-
    format("Selecione a opção de recarga que deseja :"),
    format("\n 1- 10 reias \n 2- 20 reias \n 3- 25 reais \n 4- 50 reais \n 5- Outro\n"),
    read(Entrada),
    pergunta3(Entrada, Numero, Clien).

pergunta(4,Numero, Clien ):-
    format("Solicitação de renovação de plano realizada com sucesso"),
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta(5, Numero , Clien):-
    format("Digite o problema:"),
    read(Problema),
    format("Problema foi salvo e enviado ao sistema. Assunto :"),
    write(Problema),nl,
    format("Problema enviado para a central."),nl,
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).


%Pergunta 1
pergunta1(Plan, Numero, Clien):-
    format("Tem certeza que deseja contratar o plano "), write(Plan),format("? 1- Sim , 2-Não"),
    read(Resposta),
    Resposta == 2 -> format("Operação cancelada.\n\n"), chatbot(Numero,Clien );
    number_string(Numero, Number),
    assertz(Number, Plan),
    format("Plano "), write(Plan), format(" Contratado com sucesso!.\n\n"),
    format("Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

%Pergunta 3
pergunta3(1, Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).
pergunta3(2, Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).
pergunta3(3,  Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).
pergunta3(4,  Numero, Clien):-
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).

pergunta3(5, Numero, Clien):-
    format("Digite o valor que deseja recarregar :"),
    read(Valor),
    pergunta31(Valor, Numero, Clien).

pergunta31(Valor, Numero, Clien):-
    format("Valor de "),
    write(Valor),
    format(" depositado com sucesso para o numero "),
    write(Numero),
    format("\n Deseja finalizar operações ? 1- Sim , 2- Não "),
    read(Entrada),
    perguntaFim(Entrada, Numero, Clien).



perguntaFim(1, Numero, Clien):-
    write(Clien),nl,
    format("Sessao finalizada para "),
    write(Numero), nl.
perguntaFim(2, Numero, Clien):-
    chatbot(Numero, Clien).

perguntaFim("Sim", Numero, Clien):-
    write(Clien),nl,
    format("Sessao finalizada para "),
    write(Numero), nl.
perguntaFim("Não", Numero, Clien):-
    chatbot(Numero, Clien).


cls:- write('\33\[2J').
