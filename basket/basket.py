

class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necassary.
    """

    def __init__(self, request):
        """Initialise the user session and get items in basket
        by using session key. If no basket in session, create new
        empty dictionary and set to session.
        """
        self.session = request.session
        basket = self.session.get("s_key")
        if "s_key" not in request.session:
            basket = self.session["s_key"] = {}
        self.basket = basket

    def add(self, product):
        """Adding and updating the users baket session data.
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {"price": str(product.price)}

        self.session.modified = True
