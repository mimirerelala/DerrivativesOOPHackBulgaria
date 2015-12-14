class Monom:
    def __init__(self, variable, coefficient, power):
        self.variable = variable
        self.coefficient = coefficient
        self.power = power


    def __add__(self, other_monom ):
        if (self.variable == other_monom.variable):
            if (self.power == other_monom.power):
                return Monom(self.variable, self.coefficient + other_monom.coefficient, self.power)

    def differentiate(self):
        self.coefficient *= self.power
        self.power -= 1


    def __str__(self):
        return self.coefficient + "" + self.variable + "^" + self.power

    def __repr__(self):
        return str(self)




class Polynom:
    def __init__(self):
        self.monoms_list = {}

    def add_member(self, monom_member):
        self.monoms_list[monom_member.power] += monom_member

    def __str__(self):
        return

    def __repr__(self):
        return

