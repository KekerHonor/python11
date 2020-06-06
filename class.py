class hun:
    def __init__(self, ner: str, nas: int):
        print("constructor duudagdaw")
    def __del__(self):
        print("destructor duudagdaw")

hun1 = hun("bold",24)
hun2 = hun("bayar",22)
print(hun1.ner, hun1.nas)
print(hun2.ner, hun2.nas)
# constructor - object uuseh uyed duudagddag
# destructor - object sanah oigoos choloologdoh uyed