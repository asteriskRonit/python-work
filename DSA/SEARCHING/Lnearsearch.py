no_terms=int(input("Enter the number of terms you want to enter: "))
LSTNO=[float(input("Enter the numbers : ")) for i in range(no_terms)]
print("The list of the number is : ",LSTNO)

#searching the search terms

searchTerm=float(input("Enter the term you are searching: "))
for c in LSTNO:
    print(c)
    if searchTerm==c:
        searchTerm=True
        break

if searchTerm:
    print("Number term is present there")
else:
    print("the number that u r searching is not there")






