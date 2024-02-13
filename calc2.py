# Main function 
def main():
    gross_bill = get_bill()
    residents = get_residents()
    per_person = split_bill(gross_bill, residents)
    ea_appt_share = per_appt(per_person)
    #net_bill = contributions(ea_appt_share)
    print(ea_appt_share)


# Convert inputs to floats
def verify_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("You must enter a number.")


# Get sum of all house expenses. Becomes gross_bill
def get_bill():
    total_bill = []
    while True:
        total_bill.append(verify_input("Enter an expense: "))
        while True:
            answer = (input("Do you have any more expenses to enter? ").lower())
            if answer != "yes" and answer != "no":
                print("Please answer with 'yes' or 'no'.")
            elif answer == "yes":
                break       
            elif answer == "no":
                return sum(total_bill)


# Number of residents
def get_residents():
    return verify_input("How many people were home this month? ")


# gross_bill split by number of residents. Becomes per_person
def split_bill(gross_bill, residents):
    individual_bill = gross_bill / residents
    return individual_bill
    

# Returns a bill for each appartment. Becomes ea_appt_share
def per_appt(per_person):
    bill = {}
    for res in current_residents:
        bill[res["name"]] = (res["multiplier"] * per_person + 20 * res["multiplier"])
    return bill
   

#def contributions(appt_share):

# Names and how many in each appt.
current_residents = [
    {"name": "A + A", "multiplier": 2},
    {"name": "S + J", "multiplier": 1.5},
    {"name": "N + P", "multiplier": 1.5},
    #{"name": "G", "multiplier": 1},
]

# Call main
main()