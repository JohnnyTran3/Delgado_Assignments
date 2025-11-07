def dollar_rows(rows):
    for i in range(rows):
        print("".join(dollar_list))
        dollar_list.append("$")
            

dollar_list = ["$"]

rows = int(input("Please type the number of rows to print: "))
dollar_rows(rows)


