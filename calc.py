def verify_input(prompt, expected_type='float', allow_done=False):
    while True:
        user_input = input(prompt)
        if allow_done and user_input.lower() == 'done':
            return 'done'
        if expected_type == 'float':
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input, please enter a number.")
        elif expected_type == 'yes_no':
            if user_input.lower() in ['yes', 'no']:
                return user_input.lower()
            else:
                print("Please answer with 'yes' or 'no'.")

def get_bill():
    total_bill = []
    print("Enter the bills recieved this month. You can enter one at a time. Type 'done' when finished:")
    while True:
        expense = verify_input("Bill amount: $", allow_done=True)
        if expense == 'done':
            break
        total_bill.append(expense)
    return sum(total_bill)

def get_residents():
    active_residents = 0
    for apt in current_residents:
        response = verify_input(f"Was {apt['name']} home this month? (yes/no): ", expected_type='yes_no')
        if response == 'yes':
            active_residents += apt['occupancy_factor']
        else:
            apt['occupancy_factor'] = 0
    return active_residents

def per_appt(per_person):
    bill = {}
    for res in current_residents:
        if res["occupancy_factor"] > 0:
            bill[res["name"]] = res["occupancy_factor"] * (per_person + 20)
        else:
            bill[res["name"]] = 0.00
    return bill

def individual_expenses(ea_appt_share):
    print("\nEnter any purchases made for the house by an individual. These will be deducted from that apartment's bill. Type 'done' when finished.")
    while True:
        apt_name = input("Enter the apartment making a purchase or 'done' to finish: ").title()  # Correctly applied .title() method
        if apt_name == 'Done':  # Correctly check against 'Done'
            break
        if apt_name in ea_appt_share:
            amount = verify_input("Purchase amount: $") 
            ea_appt_share[apt_name] -= amount
        else:
            print("Apartment not found.")
    return ea_appt_share


def main():
    gross_bill = get_bill()
    residents = get_residents()
    per_person = gross_bill / residents
    ea_appt_share = per_appt(per_person)
    ea_appt_share = individual_expenses(ea_appt_share)

    print("\nFinal Billing Summary:")
    for apt, amount in ea_appt_share.items():
        print(f"{apt}: ${amount:.2f}")

current_residents = [
    {"name": "Mama-Dada", "occupancy_factor": 2.5},
    {"name": "The Big Watutsie", "occupancy_factor": 1.5},
    {"name": "Nealson", "occupancy_factor": 1.5},
    {"name": "GareBear", "occupancy_factor": 1},
]


if __name__ == "__main__":
    main()
