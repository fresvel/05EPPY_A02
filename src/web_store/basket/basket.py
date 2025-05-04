

class Basket:
    def __init__(self):
        """Inicializa una cesta vacía."""
        self.items = {}

    def add_item(self, item_name, quantity, price):
        """
        Agrega un artículo a la cesta.

        :param item_name: Nombre del artículo.
        :param quantity: Cantidad del artículo.
        :param price: Precio unitario del artículo.
        """
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}

    def remove_item(self, item_name):
        """
        Elimina un artículo de la cesta.

        :param item_name: Nombre del artículo a eliminar.
        """
        if item_name in self.items:
            del self.items[item_name]

    def get_total(self):
        """
        Calcula el total de la cesta.

        :return: Total de la cesta.
        """
        return sum(quantity['quantity'] * quantity['price'] for quantity in self.items.values())

    def clear(self):
        """Vacía la cesta."""
        self.items.clear()

    def __str__(self):
        """Representación en cadena de la cesta."""
        return f"Basket({self.items})"
