class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Agrega un depósito al ledger.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Agrega un retiro al ledger si hay fondos suficientes.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        Devuelve el balance actual sumando todos los movimientos en el ledger.
        """
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """
        Transfiere fondos de esta categoría a otra, si hay suficientes.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """
        Comprueba si el monto ingresado es menor o igual al balance.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        Formatea la salida cuando se imprime el objeto.
        """
        # Centra el nombre entre asteriscos (total 30 caracteres)
        output = f"{self.name:*^30}\n"
        
        for item in self.ledger:
            # Acota la descripción a 23 caracteres y la alinea a la izquierda
            desc = f"{item['description'][:23]:<23}"
            # Asegura 2 decimales, máximo de 7 caracteres y alinea a la derecha
            amount_str = f"{item['amount']:.2f}"
            amount_formatted = f"{amount_str[:7]:>7}"
            output += f"{desc}{amount_formatted}\n"
            
        output += f"Total: {self.get_balance()}"
        return output


def create_spend_chart(categories):
    """
    Genera un gráfico de barras mostrando el porcentaje gastado por categoría.
    """
    spent_amounts = []
    # Calcula el total de los retiros (gastos) por categoría
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_amounts.append(spent)
        
    total_spent = sum(spent_amounts)
    
    # Calcula el porcentaje redondeado hacia abajo al múltiplo de 10 más cercano
    percentages = []
    for spent in spent_amounts:
        percent = int((spent / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0
        percentages.append(percent)

    # Construye el gráfico (Eje Y)
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
        
    # Agrega la línea horizontal (Eje X)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Escribe los nombres verticalmente
    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]
    
    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += f"{name[i]}  "
        # Evita un salto de línea extra en la última iteración
        if i < max_name_length - 1:
            chart += "\n"
            
    return chart