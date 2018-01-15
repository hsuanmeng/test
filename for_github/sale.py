
class Sale(object):
    @property
    def order_no(self):
        return self._orderno

    @order_no.setter
    def order_no(self, value):
        self._orderno = value
        pass
    pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        pass


if __name__ == '__main__':
    sale = Sale()
    sale.order_no = "#123"
    assert sale.order_no == "#123", "Order No is #123"

    sale = Sale()
    sale.name = "Melvin"
    assert sale.name == "melvin chu", "Name is not Melvin"

    assert True, "Nothing happen"
    assert False, "Everything Wrong"

    assert 2 + 2 == 5, "Houston we've got a problem"
