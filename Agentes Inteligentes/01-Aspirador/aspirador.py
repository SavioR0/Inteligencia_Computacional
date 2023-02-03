from pickle import FALSE, TRUE

pontuacao = 0
pos = TRUE  # TRUE -> Quarto A. FALSE -> Quarto B
ambiente = [
    [TRUE, TRUE],   # A-> SUJO , B -> SUJO
    [TRUE, FALSE],  # A-> SUJO , B -> LIMPO
    [FALSE, TRUE],  # A-> LIMPO, B -> SUJO
    [FALSE, FALSE]  # A-> LIMPO, B -> LIMPO
] 


def printCenario(cenario):
    print("--------------------------------------------------------------------")
    print("Condição do cenário: ")
    if(cenario[0] == TRUE): 
        print("  Quarto A: sujo")
    else:
        print("  Quarto A: Limpo")

    if(cenario[1] == TRUE): 
        print("  Quarto B: sujo")
    else:
        print("  Quarto B: Limpo")
    print("\n")


def aspira(cenario):
    global pos
    global ambiente
    if(pos == TRUE): # começa no Quarto a
        if(ambiente[cenario][0] == TRUE):
            print("     Quarto A sujo, limpando quarto A...")
            ambiente[cenario][0] = FALSE
            print("     Indo até o quarto B...")
            pos = FALSE
            return 5
        else:
            print("     Quarto A limpo, Indo até o quarto B...")
            pos = FALSE
            return -1
            
            
    if(pos == FALSE): # começa no Quarto b
        if(ambiente[cenario][1] == TRUE):
            print("     Quarto B sujo, limpando quarto B...")
            ambiente[cenario][1] = FALSE
            print("     Indo até o quarto A...")
            pos = TRUE
            return 5
        else:
            print("     Quarto B limpo, Indo até o quarto A...")
            pos = TRUE
            return -1

                

def printCondicaoFinal(cenario, pontuacao):
    print("\n  Condição final do cenário: ")
    if(cenario[0] == TRUE): 
        print("    Quarto A: sujo")
    else:
        print("    Quarto A: Limpo")

    if(cenario[1] == TRUE): 
        print("    Quarto B: sujo")
    else:
        print("    Quarto B: Limpo")
    print("\n\nPontuação: ", pontuacao)
    print("\n--------------------------------------------------------------------\n\n")

    


def main():
    global pos
    global ambiente
    aux = 0
    while aux < 2:
        for cenario in range(4):
            printCenario(ambiente[cenario])
            posicaoInicial = pos
            pontuacao = 0
            while TRUE:
                pontuacao += aspira(cenario)
                if(pos == posicaoInicial):
                    break
            printCondicaoFinal(ambiente[cenario], pontuacao)
        aux += 1
        ambiente = [
            [TRUE, TRUE],   # A-> SUJO , B -> SUJO
            [TRUE, FALSE],  # A-> SUJO , B -> LIMPO
            [FALSE, TRUE],  # A-> LIMPO, B -> SUJO
            [FALSE, FALSE]  # A-> LIMPO, B -> LIMPO
        ] 
        pos = FALSE
            




main()