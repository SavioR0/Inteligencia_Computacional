:-include(banco_de_dados1).
:-include(perguntas1).
:-include(perguntas2).

chatbot(Numero, Clien):-
    write(Clien),
    format(" ,"),
    format("qual operação deseja realizar no numero "),
    write(Numero), nl,
    format(" 1- Contratar planos.\n"),
    format(" 2- Cancelar planos.\n"),
    format(" 3- Recarregar.\n"),
    format(" 4- Renovar plano vigente.\n"),
    format(" 5- Relatar problemas.\n"),
    format(" Escolha a opção que deseja : "),

    repeat,
    read(Entrada),
    pergunta(Entrada, Numero, Clien).


exec:-
    format("Olá, estou aqui para te ajudar! Sou o chatbot da operadora HOI. \n"),
    format("Digite o seu numero de telefone:"),
    read(Numero),
    (  cliente(Numero, Clien)) -> (format("Olá "),chatbot(Numero,Clien));(
    format(" Numero não cadastrado. Vamos realizar cadastro. Digite seu nome :"),
    read(Nome),
    format("\nConfirme seu numero : "),
    read(Numero),
    chatbot(Numero, Nome)).



