class Reservation:
    def __init__(self, client, date, place):
        self.client = client
        self.date = date
        self.place = place
        self.statut = "non confirmée"
    def confirmer(self):
        self.statut = "confirmée"
class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.reservations = []
    def effectuer_reservation(self, reservation):
        self.reservations.append(reservation)
class SystemeDeReservation:
    def __init__(self):
        self.reservations = []
    def ajouter_reservation(self, reservation):
        self.reservations.append(reservation)
    def annuler_reservation(self, reservation):
        self.reservations.remove(reservation)
    def afficher_reservations(self):
        for reservation in self.reservations:
            print(
                f"Client: {reservation.client.nom}, Date: {reservation.date}, Place: {reservation.place}, Statut: {reservation.statut}")
client1 = Client("Alice", "alice.com")
client2 = Client("Bob", "bob.com")

reservation1 = Reservation(client1, "2025-01-10", "A1")
reservation2 = Reservation(client2, "2025-01-12", "B1")

client1.effectuer_reservation(reservation1)
client2.effectuer_reservation(reservation2)

systeme = SystemeDeReservation()
systeme.ajouter_reservation(reservation1)
systeme.ajouter_reservation(reservation2)

systeme.afficher_reservations()

reservation1.confirmer()
systeme.afficher_reservations()

systeme.annuler_reservation(reservation2)
systeme.afficher_reservations()
