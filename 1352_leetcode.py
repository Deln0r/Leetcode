class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        self.__init__() if num == 0 else self.prefix_product.append(num * self.prefix_product[-1])

    def getProduct(self, k: int) -> int:
        return 0 if k >= len(self.prefix_product) else self.prefix_product[-1] // self.prefix_product[-k-1]