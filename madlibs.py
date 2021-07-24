import random


""" list_of_madlibs = ["Mi nombre es {nombre} {apellido}"]
nombre = input('Ingrese nombre: ')
apellido = input('Ingrese apellido: ')
madlib = f"Mi nombre es {nombre} {apellido} "


print(madlib) """

class Madlib:
    def __init__(self, adjetive1, adjetive2, adjetive3, verb1, verb2, verb3):
        self.adjetive1 = adjetive1
        self.adjetive2 = adjetive2
        self.adjetive3 = adjetive3
        self.verb1 = verb1
        self.verb2 = verb2
        self.verb3 = verb3

    def select_text(self, number_of_list):
        position = random.randint(0,2)

        tuple_one = (
           f"The person is {self.adjetive1} but also {self.adjetive2}.",
           f"The animal is {self.adjetive1} but also {self.adjetive2}.",
           f"The machine is {self.adjetive1} but also {self.adjetive2}.",
        )

        tuple_two = (
            f"Every time he {self.verb1}, later {self.verb2}.",
            f"Every location is {self.verb1}, but {self.verb2}.",
            f"Every part is {self.verb1}, only one is {self.verb2}.",
        )

        tuple_three = (
            f"At last, always is {self.adjetive3} when {self.verb3}",
            f"At last, sometimes is {self.adjetive3} when {self.verb3}",
            f"At last, never is {self.adjetive3} when {self.verb3}",
        )
        
        if number_of_list == 1:
            text = tuple_one[position]
        elif number_of_list == 2:
            text = tuple_two[position]
        elif number_of_list == 3:
            text = tuple_three[position]

        return text


if __name__ == '__main__':
    adjetive1 = input('Adjetive:')
    adjetive2 = input('Adjetive:')
    adjetive3 = input('Adjetive:')
    verb1 = input('Verb:')
    verb2 = input('Verb:')
    verb3 = input('Verb:')

    madlib = Madlib(adjetive1, adjetive2, adjetive3, verb1, verb2, verb3)
    out_text = madlib.select_text(1)
    out_text += madlib.select_text(2)
    out_text += madlib.select_text(3)

    print(f"{out_text}")