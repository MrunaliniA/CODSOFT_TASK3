import random
import string

def generation(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

def main():
    while True:
        print("Password Generator")
        try:
            length = int(input("Enter the Password length: "))
            if length <= 0:
                print("Password length should be a Non-Zero positive integer.")
                return
            password = generation(length)
            print("***************************************************************")
            print("Generated Password: ", password)
            print("***************************************************************")
        except ValueError:
            print("Invalid input.")
        next=input("Lets do another Password Generation (yes/no): ")
        if next == "no":
            break
        elif next == "yes":
            continue
        else:
            print("Value Error...Type 'yes' or 'no'")
            break

if __name__ == "__main__":
    main()
