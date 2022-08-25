contacts = []
print("""1: Add
2: List
3: Search
4: Edit
0: Exit""")
q = int(input("Enter a choice: "))
while q != 0:
    if q == 1:
        name = input("Enter a name:")
        mobile = input("Enter the Handy number: ")
        contact = [name, mobile]
        contacts.append(contact)
    elif q == 2:
        print(contacts)
    elif q == 3:
        name = input("Enter a name: ")
        for i in range(len(contacts)):
              if contacts[i][0] == name:
                  print(contacts[i][1])
    print("""   1: Add
                2: List
                3: Search
                4: Edit
                0: Exit""")
    q = int(input("Enter a choice: "))
