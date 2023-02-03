import Aspirador2x2.functions as functions

punctuation = [0, 0, 0, 0, 0, 0, 0, 0]

locations = ["Left", "Right"]

configuration = [["Dirty", "Dirty"], ["Dirty", "Clean"],
                 ["Clean", "Dirty"], ["Clean", "Clean"]]

state = ["", ""]

j = 0
while j <= 1:

    i = 0
    while i <= 3:
        location = locations[j]

        print(
            f"----------------------------------INTERAÇÃO {4 * j + i + 1}-----------------------------------------")
        functions.printInfo(configuration, location, i)
        print(
            "--------------------------------------------------------------------------------------")

        response = functions.response(functions.actionAgent(
            configuration[i], location), configuration[i], state, location)
        location = response[2]
        configuration[i] = response[0]
        state = response[1]
        punctuation[(4*j+i)] = punctuation[(4*j+i)] + response[3]
        functions.printInfo(configuration, location, i, state)

        while state != ["Clean", "Clean"]:
            response = functions.response(functions.actionAgent(
                configuration[i], location), configuration[i], state, location)
            location = response[2]
            configuration[i] = response[0]
            state = response[1]
            punctuation[(4*j+i)] = punctuation[(4*j+i)] + response[3]

            functions.printInfo(configuration, location, i, state)

        print(
            f"-------------------------------- PONTUAÇÃO : {punctuation[(4*j+i)]}  -------------------------------------", end="\n\n\n\n")
        i = i + 1
        state = ["", ""]

    configuration = functions.resetConfigurations()
    j = j + 1

print("\tTODAS AS PONTUAÇÕES : ", end="")
print(punctuation, end="\n\n")
