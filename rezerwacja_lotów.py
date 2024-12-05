import datetime

class FlightFullError(Exception):
    """lot pełen nie można jużrezerwować"""
    pass
class NoReservationError(Exception):
    """próba anulowania nie posiadanej rezerwacji"""
    pass
class FlightNotFoundError(Exception):
    """użytkownik operuje na nie istniejacym locie"""
    pass
class InvalidReservationError(Exception):
    """próba wyporzyczenia siedzenia na tym samym locie"""
    pass

file_path = "logs.txt"
def log_to_file (message, level="INFO"):
    """"
    funkcja zapisująca logi do pliku logs.txt
    :param message: Treść logu.
    :param level: Poziom logu (INFO, ERROR).
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open(file_path, "a") as log:
        log.write(f"[{timestamp}] {level}: {message}\n")

class Flight:
    def __init__(self,flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.reservations = []
    
    def reserve_seat(self, user):
        """rezerwacja miejsca dla użytkownika"""
        if len(self.reservations) >= self.capacity:
            raise FlightFullError(f"Lot {self.flight_number} jest pełny")
        if user in self.reservations:
            raise InvalidReservationError(f"Użytkownik {user} już ma rezerwację na locie {self.flight_number}")
        self.reservations.append(user)

    def cancel_reservations(self,user):
        """anuluje rezerwacje dla użytkownika"""
        if user not in self.reservations:
            raise NoReservationError(f"Użytkownik {user} nie ma rezerwacji na locie {self.flight_number}")
        self.reservations.remove(user)

    def avaiable_seats (self):
        print(f" na locie jest {self.capacity - len(self.reservations)} wolnych miejsc")

class FlightSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight_number, capacity):
        """dodanie nowego lotu do systemu"""
        self.flights[flight_number] = Flight(flight_number,capacity)

    def get_flight(self, flight_number):
        """zwraca obiekt lotu na podstawie numeru lotu"""
        if flight_number not in self.flights:
            raise FlightNotFoundError(f"lot o numerze {flight_number} nie istnieje")
        return self.flights[flight_number]
    
def main():
    system = FlightSystem()
    while True:
        print(f"--------------\n\
                flight menu, choose action\n\
                1 Sprawdź dostępne miejsce\n\
                2 Zarezerwój miejsce\n\
                3 Anuluj rezerwację\n\
                4 Wyjdź")
        choice = input(f"wybierz opcję: ").strip().lower()

        try:
            if choice == "1":
                flight_number = input("Podaj numer lotu: ").strip()
                flight = system.get_flight(flight_number)
                print(f"Dostępne miejsca na locie {flight_number}: {flight.avaiable_seats()}")

            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                break
        except Exception as err:
            print(f"oh no we have an error: {err}")
            
