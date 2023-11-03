import time


# Vamos criar 2 classes referentes às 2 entidades presentes: o Voo e o Cliente

class Voo:
    def __init__(self):
        self.faturamento = 0
        self.ocupacao = 0
        self.taxa = 0
        self.preco = 500
        self.letras = ["D", "C", "B", "A"]

        self.numeros = []
        for i in range(20):
            self.numeros.append(i + 1)

        self.poltronas = []
        for i in range(4):
            linha = []
            for j in range(20):
                linha.append("0")
            self.poltronas.append(linha)

    def interface(self):
        print()
        print("               | SISTEMA DE VENDAS DE PASSAGENS |")
        print("                       | DESTINO: Maraã |")
        print()

        print("                  ", end="")
        print("|MAPA DOS ASSENTOS DO AVIÃO|")
        print()
        print("             ", end="")
        for i in range(20):
            if i == 0 or i == 19:
                print(self.numeros[i], end=" ")
            else:
                print(" ", end=" ")
        print()
        for i in range(4):
            print("          ", end="")
            print(self.letras[i], end="| ")
            for j in range(20):
                print(self.poltronas[i][j], end=" ")
            print()

    def status(self):
        self.taxa = self.ocupacao * (5/4)
        if self.taxa < 50:
            print("A viagem foi CANCELADA!")
        else:
            print("A viagem foi CONFIRMADA!")
            print(f"Faturamento total da viagem (em R$): {self.faturamento}")
            print(f"Taxa de ocupação do avião (em %): {self.taxa}")


class Cliente:
    def __init__(self):
        self.idade = 0
        self.letra = "0"
        self.numero = 0

    def compra(self, x):
        self.letra = str(input("Digite a letra do assento que o passageiro deseja: ")).upper()
        if self.letra not in x.letras:
            self.letra = str(input("Digite uma letra VÁLIDA: ")).upper()

        self.letra = x.letras.index(self.letra)

        self.numero = int(input("Digite o número do assento que o passageiro deseja (no intervalo dado no mapa): "))

        if self.numero not in x.numeros:
            self.numero = int(input("Digite um número VÁLIDO: "))

    def finalizar(self, x):
        if x.poltronas[self.letra][self.numero - 1] == "0":
            print("A passagem está no carrinho!")
            self.idade = int(input("Digite a idade do passageiro: "))
            if self.idade < 5 or self.idade > 65:
                x.faturamento += x.preco / 2
            else:
                x.faturamento += x.preco

            print()

            if self.idade < 5 or self.idade > 65:
                print(f"Parabéns! A passagem de {x.preco / 2} reais foi comprada com sucesso!")
            else:
                print(f"Parabéns! A passagem de {x.preco} reais foi comprada com sucesso!")

            x.poltronas[self.letra][self.numero - 1] = "X"
            x.ocupacao += 1

        else:
            print("Desculpa, mas a poltrona em questão já está ocupada!")


# Aqui vamos criar uma função para a decisão para continuar ou não o loop infinito

def decisao():
    print("Deseja continuar vendendo passagens?")
    print("Digite o número 1 para parar de vender.")

# Aqui começa o programa de vendas de passagens

def main():
    voo1 = Voo()
    while True:
        cliente1 = Cliente()
        voo1.interface()
        print()
        cliente1.compra(voo1)
        print()
        time.sleep(2)
        cliente1.finalizar(voo1)
        print()
        time.sleep(2)
        decisao()
        escolha = int(input("Digite qualquer outro número para continuar vendendo: "))
        if escolha == 1:
            break
    time.sleep(2)
    print()
    voo1.status()

if __name__ == "__main__":
    main()