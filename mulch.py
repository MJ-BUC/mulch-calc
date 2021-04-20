'''
This is Program that calculates the cost for much needed
'''

# imports extra python math tools
import math

SALES_TAX = .07


def main():
    # Prints name of the program with the divider underneath.
    print("Mulch Cost Calculator")
    print("=====================")
    print(" ")

    # Rounds to the nearest whole number up
    def round_half(x):
        return int(math.ceil(x / 1.0)) * 1

    # Stores the toal cubic yards for the whole program
    total_cubic_yards = 0

    # Fuction that prompts user to enter their desired length, width, and depth.
    def get_cubic_yards():
        ask_for_length = int(
            input("Enter the length of the planting bed, in feet: "))
        ask_for_width = int(
            input("Enter the width of the planting bed, in feet: "))
        ask_for_depth = int(
            input("Enter the desired depth of mulch, in inches: "))
        # This function calculates the cubic yards of the user's entered length, width, and depth.
        get_cubic_yards.cubic_yards = (
            ask_for_length * ask_for_width * (ask_for_depth / 12) / 27)

    # runs function and totals the cubic yards from it
    get_cubic_yards()
    total_cubic_yards += get_cubic_yards.cubic_yards
    # Initiates the while loop
    enter_another_bed = 0

    # Prompts the user to enter length, width, and depth if y is selected or does not if n is selected.
    enter_another_bed = input(
        "Enter the dimensions for another planting bed? (y/n): ")
    while enter_another_bed != 'n' and enter_another_bed == 'y' or enter_another_bed == 0:
        print(" ")
        get_cubic_yards()
        total_cubic_yards += get_cubic_yards.cubic_yards
        enter_another_bed = input(
            "Enter the dimensions for another planting bed? (y/n): ")

    # Tells the user the total cubic yards of mulch they need.
    print(" ")
    print("Total much required is approximately",
          round_half(total_cubic_yards), "cubic yards")
    if total_cubic_yards <= 3:
        print("The minimum mulch order is 3 cubic yards.")
    print(" ")

    # Asks the user to enter their distance from Naperville in mi.
    ask_for_distance = float(
        input("Enter your distance from Naperville, IL, in miles: "))
    print(" ")

    # calculates the delivery cost and 8.2352941178 is the level that determines
    # whether the delivery cost is a base $35 or $4.25 per mile
    if ask_for_distance <= 8.2352941178:
        delivery_cost = 35
    else:
        delivery_cost = 4.25 * ask_for_distance

    # calculates the tax for each corresponding if, elif statement
    tax1 = ((3 * 36)) * SALES_TAX
    tax2 = ((round_half(total_cubic_yards) * 36)) * SALES_TAX
    tax3 = (((round_half(total_cubic_yards) - 5) * 33) + (5 * 36)) * SALES_TAX
    tax4 = (((round_half(total_cubic_yards) - 10) * 30) +
            (5 * 33) + (5 * 36)) * SALES_TAX

    print("Cost for ", round_half(total_cubic_yards), " cubic yards of mulch")
    print("==================================")
    # Calculates the cost of mulch and total cost.
    # Also prints the cost of mulch, delivery charge, sales tax, and total cost.

    def calculate_mulch_cost():
        if total_cubic_yards <= 3:
            print("          Mulch: $", format((3 * 36.00), '7.2f'))
            print("Delivery Charge: $", format(delivery_cost, '7.2f'))
            print("      Sales Tax: $", format(tax1, '7.2f'))
            print("     Total Cost: $", format(
                (3 * 36) + delivery_cost + tax1, '7.2f'))
        elif total_cubic_yards > 3 and total_cubic_yards <= 5:
            print("          Mulch: $", format(
                (round_half(total_cubic_yards) * 36.00), '7.2f'))
            print("Delivery Charge: $", format(delivery_cost, '7.2f'))
            print("      Sales Tax: $", format(tax2, '7.2f'))
            print("     Total Cost: $", format(
                (round_half(total_cubic_yards) * 36) + delivery_cost + tax2, '7.2f'))
        elif total_cubic_yards > 5 and total_cubic_yards <= 10:
            print("          Mulch: $", format(
                ((round_half(total_cubic_yards) - 5) * 33) + (5 * 36.00), '7.2f'))
            print("Delivery Charge: $", format(delivery_cost, '7.2f'))
            print("      Sales Tax: $", format(tax3, '7.2f'))
            print("     Total Cost: $", format(
                ((round_half(total_cubic_yards) - 5) * 33) + (5 * 36) + delivery_cost + tax3, '7.2f'))
        elif total_cubic_yards > 10:
            print("          Mulch: $", format(
                ((round_half(total_cubic_yards) - 10) * 30) + (5 * 33) + (5 * 36.00), '7.2f'))
            print("Delivery Charge: $", format(delivery_cost, '7.2f'))
            print("      Sales Tax: $", format(tax4, '7.2f'))
            print("     Total Cost: $", format(((round_half(total_cubic_yards) - 10)
                                                * 30) + (5 * 33) + (5 * 36.00) + delivery_cost + tax4, '7.2f'))

    # runs function above
    calculate_mulch_cost()


# activates the entire program by running all code inside of the "main" function.
if __name__ == "__main__":
    main()
