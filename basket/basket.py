

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
        basket = self.session.get("session_key")
        if "session_key" not in request.session:
            basket = self.session["session_key"] = {'number': 123123123}
        self.basket = basket
