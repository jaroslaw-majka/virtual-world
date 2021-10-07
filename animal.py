from organism import Organism


class Animal(Organism):
    def multiplication(self, free_fields: list):
        def check_organism_type():
            print(type(self))

        check_organism_type()
