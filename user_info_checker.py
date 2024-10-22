# Array for storing all entries
data_entries = {}

# Loop for continuous input
while True:
    # Loop for validation of inputs
    while True:
        try:
            # Ask the user to input name and age
            # Have a valid name and valid age
            # Display error message if the input is not valid

            # Check if name is valid, if not, raise an error
            name = input("Please enter your name: ")
            if len(name) < 3 or not name[0].isupper():
                raise
            # Check if age is valid, if not, raise an error
            age = int(input("Please enter your age: "))
            if age < 18 or age > 65:
                raise
            
            # Store user entries
            data_entries[name] = {"age" : age}

            # Ask user for new entry
            new_entry = input("Do you want to input data again? (Yes/No) ")
            break

        except:
            print("Error")

    # Catching valid and invalid inputs for new entries
    if new_entry == "No":
        break
    if new_entry != "Yes":
        print("Please input a valid answer.")

# Ask the user if they want to input another entry
    # If “Yes”
        # ask the user again for name and age entries
    # If "No"
        # display the name and age of the oldest person.
        # stop the program