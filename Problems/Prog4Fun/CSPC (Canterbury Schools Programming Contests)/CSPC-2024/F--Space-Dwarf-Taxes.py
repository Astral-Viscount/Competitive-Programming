# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9684&cmid=4328&page=6

num_weeks = int(input())

tax_table={"Gold": 2,
           "Silver": 5,
           "Platinum": 10,
           "Morkite": 20}

tax = 0

for _ in range(num_weeks):

    num_entries = int(input())
    for _ in range(num_entries):
        
        # (item, sale_price, amount) = values if len(values := input().split()) == 3 else (values[0], None, None)

        values = input().split()
        if len(values) == 3:
            item, sale_price, amount = values

            if item in tax_table:
                cost = tax_table[item]
                tax += (int(sale_price) - cost) * int(amount)

        # for item_name, cost in tax_table.items():
        #     if item == item_name:
        #         tax += (int(sale_price) - cost) * int(amount)
        #     else:
        #         continue

print(int(tax * 0.25))
