filepath = "input.txt"
size_S = "S"
size_M = "M"
size_L = "L"
provider_MR = "MR"
provider_LP = "LP"
MR_S_cost = 2
MR_M_cost = 3
MR_L_cost = 4
LP_S_cost = 1.50
LP_M_cost = 4.90
LP_L_cost = 6.90

# we load a text file with the data and read it
a_file = open("input.txt", "r")

# we turn the data into a list so we can  modify and retrieve the information easier
lists = a_file.read().splitlines()

list_of_lists = []
for line in lists:
    list_of_lists.append(line.split(" "))

L_LP_counter = 0
all_discount = 0
month = list_of_lists[0][0][:7]
for i in list_of_lists:
    # verify if the month has changed
    # if the month changes, the discounts are canceled
    if month != i[0][:7]:
        L_LP_counter = 0
        all_discount = 0
        month = i[0][:7]

    if size_S in i and provider_LP in i:
        min_cost = LP_S_cost
        discount = 0

        # the lowest price is chosen for the size S and if the discount is less than 10 euros, it is adjusted and summed
        if all_discount < 10:
            min_cost = min(MR_S_cost, LP_S_cost)
            discount = LP_S_cost - min(MR_S_cost, LP_S_cost)

            # if the discount is more than 10, then we calculate how much discount we have left. And we won't be able to apply the discount later this month
            if discount + all_discount > 10:
                discount = 10 - all_discount
                min_cost = LP_S_cost - discount

        i.append(min_cost)
        if discount <= 0:
            discount = 0
        i.append(discount)
        all_discount += discount

    elif size_S in i and provider_MR in i:
        min_cost = MR_S_cost
        discount = 0

        if all_discount < 10:
            min_cost = min(MR_S_cost, LP_S_cost)
            discount = MR_S_cost - min(MR_S_cost, LP_S_cost)

            if discount + all_discount > 10:
                discount = 10 - all_discount
                min_cost = MR_S_cost - discount

        i.append(round(min_cost, 2))
        if discount <= 0:
            discount = 0
        i.append(round(discount, 2))
        all_discount += discount

    elif size_M in i and provider_MR in i:
        i.append(MR_M_cost)
        i.append("-")
        assert LP_M_cost == 3, "The price is not correct"
    elif size_M in i and provider_LP in i:
        i.append(LP_M_cost)
        i.append("-")
        assert LP_M_cost == 4.9, "The price is not correct"
    elif size_L in i and provider_MR in i:
        i.append(MR_L_cost)
        i.append("-")
        assert MR_L_cost == 4, "The price is not correct"

    elif size_L in i and provider_LP in i:
        L_LP_with_discount = LP_L_cost
        discount = 0
        L_LP_counter += 1

        if all_discount < 10:

            if L_LP_counter == 3:
                L_LP_with_discount = 0
                discount = LP_L_cost

                if discount + all_discount > 10:
                    discount = 10 - all_discount
                    L_LP_with_discount = LP_L_cost - discount

        all_discount += discount
        i.append(L_LP_with_discount)
        i.append(discount)
    else:
        i.append("Ignored")

for i in list_of_lists:
    for value in range(len(i)):
        if type(i[value]) == float or type(i[value]) == int:
            i[value] = "{:.2f}".format(round(i[value], 2))
    if i[-1] == "0.00":
        i[-1] = '-'
    i = [str(value) for value in i]
    line = " ".join(i)
    print(line + '\n')

# if we want to change the data and make the code more flexible, we need to
# break it down into separate functions, such as:
# def size_S_rule(all_discount, S_cost):
#     min_cost = S_cost
#     discount = 0
#
#     if all_discount < 10:
#         min_cost = min(MR_S_cost, LP_S_cost)
#         discount = S_cost - min(MR_S_cost, LP_S_cost)
#
#         if discount + all_discount > 10:
#             discount = 10 - all_discount
#             min_cost = S_cost - discount
#
#     if discount <= 0:
#         discount = 0
#
#     return min_cost, discount
