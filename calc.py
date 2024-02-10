
def main():
    gross_bill = get_bill()
    split_bill(gross_bill)
    #add_dues()
    #subtract_expenses()


def get_bill():
    while True:
        try:
            bill = float(input("What is you total bill this month? "))
        except ValueError:
            print("You must enter a number.")
            pass
        else:
            return bill


"""
105 + 114
"""

def split_bill(gross_bill):
    while True:
        try:
            how_many_home = float(input("How many people were home this month? "))
        except ValueError:
            print("You must enter a number.")
            pass
        else:
            individual_bill = gross_bill / how_many_home
            return individual_bill
    #how_many_home = float(input("How many people were home this month? "))
    #individual_bill = gross_bill / how_many_home
    #print(individual_bill)


#x = get_bill()
#print(x)

main()




