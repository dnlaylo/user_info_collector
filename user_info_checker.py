# Method for finding the oldest person (modified method from finding highest number program)
def find_oldest(data_entries):
    # Initial values for oldest person to compare first entry
    oldest_name = None
    oldest_age = 0

    # Loop for reassigning the current oldest person in the array
    for name, data in data_entries.items():
        age = data["age"]

        # If age is greater than current oldest, reassign the oldest person
        if age > oldest_age:
            oldest_name = {name}
            oldest_age = age

    # Return oldest person
    return oldest_name, oldest_age

# Array for storing all entries
data_entries = {}

# Loop for continuous input
while True:
    # Loop for validation of inputs
    while True:
        try:
            # Ask the user input, defined valid name and age, and error message display

            # Check if name is valid, if not, raise an error
            name = input("Please enter your name: ")
            if len(name) < 3 or not name[0].isupper():
                raise ValueError("At least 3 letters long and make sure to capitalize first letter. Please input a valid name.")
            
            # Loop to continuously validate age
            while True:
                try:
                    # Check if age is valid, if not, raise an error
                    age = int(input("Please enter your age: "))
                    if age < 18 or age > 65:
                        raise ValueError("Too young, too old, or invalid input. Please input a valid age.")
                    
                    # break loop if valid
                    break
                except ValueError as e:
                    print(e)
            
            # Store user entries
            data_entries[name] = {"age" : age}

            # Ask user for new entry
            new_entry = input("Do you want to input data again? (Yes/No) ")
            break

        except ValueError as e:
            print(e)
                
    # Catching valid and invalid inputs for new entries
    if new_entry == "No":
        # display the name and age of the oldest person
        oldest = find_oldest(data_entries)
        print(f"The current oldest person is {oldest}.")
        # stop the program
        break
    elif new_entry == "Yes":
        # ask name and age again
        continue
    else:
        # Loop for continuous checking of invalid user input
        while True:
            # Prompt to try again
            try_again = input("Try again. (Yes/No) ")
            # If yes, then exit loop and ask name and age again
            if try_again == "Yes":
                break
            # If no, then display oldest and exit program
            elif try_again == "No":
                oldest = find_oldest(data_entries)
                print(f"The current oldest person is {oldest}.")
                # not 'break' because it will only break the loop and ask for a name again
                exit()
            # Invalid inputs continues loop to check the answer's validity
            else:
                print("Please input a valid answer.")
