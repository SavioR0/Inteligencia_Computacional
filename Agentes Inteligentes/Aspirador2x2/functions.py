def chooseEnviroment(count):
    if count == 0:
        return ["Dirty", "Dirty"]
    elif count == 1:
        return ["Dirty", "Clean"]
    elif count == 2:
        return ["Clean", "Dirty"]
    elif count == 3:
        return ["Clean", "Clean"]
    return None


def chooseInitialPosition(count):
    if count == 0:
        return "Right"
    elif count == 1:
        return "Left"
    return None


def response(response, configuration, state,  location):
    punctuation = 0
    if response == "Limpando A." or response == "Limpando B.":
        if response == "Limpando A.":
            configuration[0] = "Clean"
            state[0] = "Clean"

        elif response == "Limpando B.":
            configuration[1] = "Clean"
            state[1] = "Clean"

        punctuation = punctuation + 5
    else:
        if location == "Right" and configuration[1] == "Clean":
            state[1] = "Clean"
        elif location == "Left" and configuration[1] == "Clean":
            state[0] = "Clean"
        location = moveAgent(location)
        punctuation = punctuation - 1

    return [configuration, state, location, punctuation]


def actionAgent(configuration, location):
    if location == "Left":
        if act(configuration[0]) == "Suck":
            return "Limpando A."
        else:
            return None
    elif location == "Right":
        if act(configuration[1]) == "Suck":
            return "Limpando B."
        else:
            return None


def act(status):
    if status == "Dirty":
        print("->LIMPANDO")
        return "Suck"
    return None


def moveAgent(location):
    if location == "Right":
        print("-> ANDANDO PARA A ESQUERDA")
        return "Left"
    elif location == "Left":
        print("-> ANDANDO PARA A DIREITA")
        return "Right"
    return None


def resetConfigurations():
    return [["Dirty", "Dirty"], ["Dirty", "Clean"],
            ["Clean", "Dirty"], ["Clean", "Clean"]]


def printInfo(configuration, location, i, state=["", ""]):
    print(
        f"POSIÇÃO: {location}\t   CONFIGURAÇÃO: [{configuration[i][0]}][{configuration[i][1]}]", end="")
    print(f"   ESTADO (MEMÓRIA) : [{state[0]} , {state[1]}]")
