class hun:
    too = 0 # classiin buh objectuud dundaa heregledeg
    def __init__(self, ner:str, nas:int):
        self.ner = ner # gishuun ogogdold utga onooh
        self.nas = nas
        hun.too += 1
    def hi(self):
        print("hi", self.ner, self.nas)

hun1 = hun("bold",24)
hun2 = hun("bayar",22)
hun3 = hun("dorj",18)
print(hun1.too)
