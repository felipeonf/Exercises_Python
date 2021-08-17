class stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []

def verifica_balanceamento(string_parenteses):
    parenteses = stack()
    balanceada = True
    i = 0
    while i < len(string_parenteses) and balanceada:
        tipo_parenteses = string_parenteses[i]
        if tipo_parenteses == "(":
            parenteses.push(tipo_parenteses)
        else:
            if parenteses.is_empty():
                balanceada = False
            else:
                parenteses.pop()
        i += 1
    if balanceada and parenteses.is_empty():
        return "Sequência Balanceada."
    else:
        return "Sequência não balanceada."

# solução alternativa:
def verifica_parenteses(string):
    abre = 0
    fecha = 0
    for char in string:
        if char == "(":
            abre += 1
        else:
            fecha += 1
    if abre == fecha:
        return "Sequência Balanceada."
    else:
        return "Sequência não Balanceada."


string_escolhida = input("Digite a sequência de parenteses que deseja verificar: ")
print(verifica_balanceamento(string_escolhida))
print(verifica_parenteses(string_escolhida))
