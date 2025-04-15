#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: March 7, 2025
# This program calculates the bonus based on years of experience
def main():
    # welcome message
    print("Welcome! \nWe will help you calculate your bonus.")

    # Ask the user for their salary and years of work
    salary_input = input("Enter your salary: ")
    years_input = input("How many years have you been working?: ")

    # Input validation
    try:
        salary = int(salary_input)
        years = int(years_input)
    except ValueError:
        print("Invalid input. Please enter numbers for salary and years.")
        return

    # Input Validation
    if salary <= 0 or years < 0:
        print("Salary must be more than 0 and years must not be negative.")
        return

    # Ask for performance
    performance_input = input(
        "How would you rate your performance from 1 to 3, 1 meaning low and 3 meaning high?: "
    )

    # Validate performance input
    try:
        performance = int(performance_input)
        if performance not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Please enter 1, 2, or 3 for performance rating.")
        return

    # Bonus Calculation
    if years < 5:
        # Less than 5 years
        wait_years = 5 - years
        print("You need to wait", wait_years, "more year(s) to get a bonus.")
        print("Thanks for starting to work with us!")
    else:
        # Calculate base bonus
        if years < 10:
            bonus = salary * 0.05  # Between 5-9 years: 5% bonus
            print("You're becoming a valued team member!")
        else:
            bonus = salary * 0.10  # 10 years or more: 10% bonus
            print("You're a senior employee. Thank you for your loyalty!")

        # Performance adjustment
        match performance:
            case 3:
                bonus *= 1.2
            case 2:
                bonus *= 0.8
            case 1:
                print("You do not get a performance bonus")

        print("Your bonus is: $", round(bonus, 2))

    # End message
    print("Thanks for being part of our company.")


if __name__ == "__main__":
    main()
