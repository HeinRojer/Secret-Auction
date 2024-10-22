T = False
dic = {}
amt_data = []

print('''  
                         ___________  
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________|
                         `'-------'`
      WELCOME TO SECRET AUCTION 
 ''')
while not T:

    name = input("Enter your Your Name :\n")
    amt = int(input("Enter the amount you want to bid :\n₹"))
    check = input("Are there any other bidders ? Type yes or no")
    print ( "\n" * 100 )
    if check == "no":
        T = True
    dic[name] = amt


def ma():
    amt_data = (dic.values())
    m = max(amt_data)
    zzz = ""
    for k in dic:
        if dic[k] == m:
            zzz = k

    print(f"The winner is {zzz} with the bid of ₹{m}")
ma()