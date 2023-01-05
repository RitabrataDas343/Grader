introduction_banner = """

░██████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██████╔╝███████║██║░░██║█████╗░░██████╔╝
██║░░╚██╗██╔══██╗██╔══██║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░░██║██████╔╝███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

grade = {
    "Ex" : 10,
    "A" : 9,
    "B" : 8,
    "C" : 7,
    "D" : 6,
    "P" : 5
}

grade_list = ["Ex", "A", "B", "C", "D", "P"]

print(introduction_banner, '\n\n', "------ MADE BY Ritabrata Das ------", '\n')

semester = int(input("Enter your CURRENT SEMESTER (1-8): "))

if(semester < 1 or semester > 8):
    print("Invalid Semester Number.\n")
    exit()
elif (semester == 1):
    print("CGPA reverted to DEFAULT.\n")
    current_cgpa = 0.0
else:
    print()
    current_cgpa = float(input("Enter your CURRENT CGPA: "))
print()

subject_list = list()
credit_list = list()
obtained_list = list()

number_of_subjects = int(input("Enter the NUMBER OF SUBJECTS: "))

print('\n', '--- ENTER THE NAME OF YOUR SUBJECTS ---', '\n')

for i in range(number_of_subjects):
    subject_list.append(input(f"Enter the NAME of SUBJECT {i+1}: "))

print('\n', '--- ENTER THE CREDITS OF YOUR SUBJECTS ---', '\n')

for i in range(number_of_subjects):
    cred = float(input(f"Enter the total CREDITS of {subject_list[i]}: "))
    if(cred % 0.5):
        print("Invalid Credit.\n")
        exit()
    credit_list.append(cred)


print('\n', '--- ENTER YOUR OBTAINED CREDITS ---', '\n')

for i in range(number_of_subjects):
    grd = input(f"Enter the GRADE of {subject_list[i]}: ")
    if grd not in grade_list:
        print("Invalid Grade.\n")
        exit()
    obtained_list.append(grd)

total_credits = 0.0
for i in range(number_of_subjects):
    total_credits += credit_list[i]*10

obtained_credits = 0.0
for i in range(number_of_subjects):
    obtained_credits += grade[obtained_list[i]] * credit_list[i]

print("\nTOTAL CREDITS =    ", round(total_credits, 1))
print("\nOBTAINED CREDITS = ", round(obtained_credits, 1), '\n')

sgpa = round(obtained_credits/total_credits*10, 2)
print("\nYOUR SGPA IS: ", sgpa)

cgpa = 0.0
if semester == 1:
    cgpa = sgpa
else:
    cgpa = (sgpa + round(current_cgpa, 2)*(semester-1))/semester

print("\nYOUR CGPA IS: ", round(cgpa, 2))
print('\n', '--- THANK YOU ---')


