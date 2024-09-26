import time
import os

class Airport:
    def __init__(self, code):
        self.code = code.upper()
    
    def __str__(self):
        return f"Airport: {self.code}"
    
class LocalAirport(Airport):
    def __init__(self, code):
        code = code.upper()
        super().__init__(code)
        if code not in ["LPL", "BOH"]:
            raise ValueError("Invalid UK airport code")
        
    def __str__(self):
        return f"Local Airport: {self.code}"
    
class OverseasAirport(Airport):
    def __init__(self, menu, code, path):
        super().__init__(code)
        code = code.upper()
        if code not in menu.get_valid_airports(path):
            raise ValueError("Invalid overseas airport code")
        
    def __str__(self):
        return f"Overseas Airport: {self.code}"
    
class Flight:
    def __init__(self, local_airport, overseas_airport):
        self.local_airport = local_airport
        self.overseas_airport = overseas_airport
    
    def __str__(self):
        return f"Flight: {self.local_airport} -> {self.overseas_airport}"
    
class PricePlan():
    def __init_(self, flight, price):
        self.flight = flight
        self.price = price

    def calculateProfit(self):
        # To Do: calcualte profit
        pass

class Menu:
    def __init__(self):
        self.airports = []
        self.flights = []
        self.price_plans = []

    def display(self):
        self.clear_screen()
        print("----------MAIN MENU----------")
        print("1. Enter airport details")
        print("2. Enter flight details")
        print("3. Enter price and calculate profit")
        print("4. Clear data")
        print("5. Quit")

    def get_option(self):
        while True:
            try:
                option = int(input("Please select an option 1-5: "))
                break
            except ValueError:
                print("Please enter a valid option")

            except Exception as e:
                print(f"An error has occurred: {e}")

        return option

    def add_local_airport(self):
        self.clear_screen()
        code = input("Enter three-letter UK airport code: ")
        try:
            airport = LocalAirport(code)
            self.airports.append(str(airport))
        except Exception as e:
            print(f"An error has occurred: {e}")
            self.quit()

    def add_overseas_airport(self, path):
        code = input("Enter three-letter overseas airport code: ")
        try:
            airport = OverseasAirport(self, code, path)
            self.airports.append(str(airport))

        except Exception as e:
            print(f"An error has occurred: {e}")
            self.quit()

    def add_flight(self):
        pass

    def add_price_plan(self):
        pass

    def print_airport_details(self):
        print(f"Airport details: {self.airports}")

    def get_flight(self):
        pass

    def get_valid_airports(self, path):
        try: 
            with open(path, "r") as file:
                return [line[:3].strip() for line in file.readlines()]
            
        except FileNotFoundError:
            print(f"The file {path} does not exist")
            self.quit()
            return []

        except Exception as e:
            print(f"An error has occurred: {e}")
            return []

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")

        else:
            os.system("clear")

    def quit(self):
        print("Exiting program")
        time.sleep(0.5)
        exit()

def main():
    menu = Menu()
    while True:
        menu.display()
        option = menu.get_option()

        match option:
            case 1:
                menu.add_local_airport()
                menu.add_overseas_airport("airports.txt")
                menu.print_airport_details()
                input("Press enter to continue\n")

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case _:
                print(f"'{option}' is not a valid option")
                menu.quit()

if __name__ == "__main__":
    main()
        
    