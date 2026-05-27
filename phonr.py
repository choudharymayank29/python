# Importing the module required for exiting the application on invalid mandatory fields
import sys

def initial_slambook():
    # Collecting the initial number of contacts the user wants to save
    # User can enter 0 if they don't want to add any immediately
    rows = int(input("Please enter number of friends you want to add: "))
    cols = 5 
    
    slam_book = []
    print(slam_book)
    
    for i in range(rows):
        print(f"\nEnter contact {i + 1} details in the following order (ONLY): ")
        print("NOTE: * indicates mandatory fields")
        print("………………………………………………………………………………")
        
        temp = []
        for j in range(cols):
            # j == 0: Name Field (Mandatory)
            if j == 0:
                name = str(input("Enter name*: ")).strip()
                if name == '':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
                temp.append(name)
                
            # j == 1: Phone Number Field (Mandatory)
            elif j == 1:
                # int() automatically raises an error if the input is left blank or is not a number
                number = int(input("Enter number*: "))
                temp.append(number)
                
            # j == 2: Thoughts/About Friend (Optional)
            elif j == 2:
                about = str(input("Enter something about your friend: ")).strip()
                if about == '':
                    about = None
                temp.append(about)
                
            # j == 3: Date of Birth (Optional)
            elif j == 3:
                dob = str(input("Enter date of birth(dd/mm/yy): ")).strip()
                if dob == '':
                    dob = None
                temp.append(dob)
                
            # j == 4: Category (Optional)
            elif j == 4:
                category = str(input("Enter category(Family/Friends/Work/Others): ")).strip()
                if category == '':
                    category = None
                temp.append(category)
        
        # Appending the 1-D list (temp) into the 2-D list (slam_book)
        slam_book.append(temp)
        
    print("\n--- Slam Book Created Successfully ---")
    print(slam_book)
    return slam_book

def menu():
    # Interactive menu for console code reusability
    print("\n" + "*" * 70)
    print("                     SLAM BOOK / PHONEBOOK MENU                        ")
    print("*" * 70)
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. View all contacts")
    print("6. Exit application")
    print("*" * 70)

# --- Main Program Execution ---
if __name__ == "__main__":
    # Initialize the slam book application
    current_slam_book = initial_slambook()
    
    # Display the menu options
    menu()