import streamlit as st
import random


def portfolio_section():
    st.title("My Portfolio")
    st.write("Hello! I'm Bhaavana, a passionate AI student.")
    st.write("Here are some of my projects: ")
    
    st.subheader("Projects")
    st.write("- Project 1: Guessing game")

    st.subheader("Skills")
    st.write("- Python")

def user_guessing_game():
    print("Welcome to the User Guessing Game!")
    print("You need to guess a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number,number_to_guess, in ,attempts, attempts.")
            break  

def machine_guessing_game():
    print("Welcome to the Machine Guessing Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    low = 1
    high = 100
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2  
        print("Machine guesses: ,guess")
        feedback = input("Is the guess too low, too high, or correct? (Enter 'low', 'high', or 'correct'): ").lower()
        if feedback == "low":
            low = guess + 1  
        elif feedback == "high":
            high = guess - 1  
        elif feedback == "correct":
            print(" The machine guessed your number ,guess, in ,attempts ,attempts.")
            break
        else:
            print("Invalid input. Please enter 'low', 'high', or 'correct'.")

def main():
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Select a section:", ["Portfolio", "User Guessing Game", "Machine Guessing Game"])
    
    if options == "Portfolio":
        portfolio_section()
    elif options == "User Guessing Game":
        user_guessing_game()
    elif options == "Machine Guessing Game":
        machine_guessing_game()


if __name__ == "__main__":
    main()
