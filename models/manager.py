from models.person import Person


class Manager(Person):

    id_counter = 1

    def __init__(self, name, email):

        super().__init__(name, email)

        self.id = Manager.id_counter
        Manager.id_counter += 1

        self.sites = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        if "@" not in value:
            raise ValueError("Invalid email")

        self._email = value

    def add_site(self, site):
        self.sites.append(site)

    def __str__(self):
        return f"{self.id} - {self.name}"