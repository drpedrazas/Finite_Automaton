from DFA import DFA


automata = DFA()
done = False
while not done:
    entrada = list(map(lambda x: x.strip(),
                          input("Estado inicial - caracter - estado final: ").strip().split("-")))
    automata.add_transition(int(entrada[0]), entrada[1], int(entrada[2]))
    son_todas = ""
    while True:
        son_todas = input("son todas las transiciones? y/n: ")
        if son_todas.lower() in {"y","n","yes","no"}:
            done = (lambda x: x in {"y","yes"})(son_todas.lower())
            break
        else:
            print("me temo que no entiendo")

finales = input("muéstrame los estados finales separados por comma: ")

for i in finales.split(","):
    automata.set_final(int(i.strip()))

done = False

print("estas son las transiciones: {}".format(automata.transitions))
while not done:
    palabra = input("dame la palabra")
    aceptacion, historia = automata.process_string(palabra)
    print("Este ha sido el proceso: ")
    for i in historia:
        print(i)
    print("La palabra ha sido: {}".format({True: "aceptada", False: "rechazada"}[aceptacion]))
    while True:
        terminado = input("hemos terminado?: ")
        if terminado.lower() in {"y","n","yes","no"}:
            done = (lambda x: x in {"y", "yes"})(terminado.lower())
            break
        else:
            print("me temo que no entiendo")
