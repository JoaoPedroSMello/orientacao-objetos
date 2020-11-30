class Retangulo:
    def __init__(self):
        self.altura = 5
        self.largura = 2

    def calculaArea(self):
        resultado = self.largura * self.altura
        return resultado

    def imprimeAtributos(self):
        print("Área: ", self.calculaArea(), "Altura: ", self.altura, "Largura: ", self.largura)

c = Retangulo()
c.imprimeAtributos()