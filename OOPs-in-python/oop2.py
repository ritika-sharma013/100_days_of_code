class ATM: 

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
            How would you like to proceed ? 
            1. Enter 1 to create a pin 
            2. Enter 2 to deposit 
            3. Enter 3 to withdraw
            4. Enter 4 to check balance 
            5. Enter 5 to exit

        """)

        match user_input:
            case "1":
                print("Create pin")
            case "2":
                print("Deposit")
            case "3":
                print("Withdraw")
            case "4":
                print("Check balance")
            case "5":
                print("Exit")

                
