class Order:
    def __init__(self,custumer,cart):
        self.custumer = custumer
        self.cart = cart
        self.total_amount = cart.total_amount()
    def place_order(self):
        if self.total_amount > 0:
            print(f"\nSipariş başarıyla oluşturuldu.")
            print(self.custumer)
            print(f"\nSipariş Detayları:")
            self.cart.display_cart()
            print(f"\n Tomlam Tutar: {self.total_amount} TL")
        else:
            print("\nSepet boş, sipariş oluşturulamadı.")