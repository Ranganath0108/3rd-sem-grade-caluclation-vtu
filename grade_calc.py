def avg_of_external(thirdsem_external=[]):
    thirdsem_ext_to_50= list(map(lambda a:((a/60)*50),thirdsem_external))
    print(f"obtained  external marks are:{thirdsem_external}")
    print(f"marks external marks scaled to 50:-{thirdsem_ext_to_50}")
    return (sum(thirdsem_ext_to_50)/len(thirdsem_ext_to_50))
def avg_of_internal(forthsem_internal=[]):
    fourth_inter_to_50=list(map(lambda b:((b/40) * 50),forthsem_internal))
    return fourth_inter_to_50
def grade_points(a):
    if (a >= 90 and a <= 100):
        return 10
    elif (a >= 80 and a < 90):
        return 9
    elif (a >= 70 and a < 80):
        return 8
    elif (a >= 60 and a < 70):
        return 7
    elif (a >= 50 and a < 60):
        return 6
    elif (a >= 45 and a < 50):
        return 5
    elif (a >= 40 and a < 45):
        return 4
    else:
        return 0
forthsem_internal=[]
thirdsem_external=[]
obtained_grade=[]
CIE=[]

Name=input("Enter your name\n")
dip_regular=int(input("press '1' if your diploma else enter '2'\n"))
if (dip_regular==1):
    length=10
    total_marks=1000
    credits = [0, 3, 4, 3, 3, 3, 3, 2, 2, 1]
    for i in range(length):
        if(i==0):
            ex_marks = int(input(f'Enter the external marks of previous odd sem(only previous sem) OF SUBcode 18MATDIP31\n'))
        elif(i>0 and i<9):
            ex_marks=int(input(f'Enter the external marks of previous odd sem(only previous sem)of  SUBcode 18**3{i}\n'))
        else:
            ex_marks = int(input(f'Enter the external marks of previous odd sem(only previous sem)of  SUBcode18CPC39\n'))

        thirdsem_external.append(ex_marks)
else:
    length=9
    total_marks=900
    credits = [3, 4, 3, 3, 3, 3, 2, 2, 1]
    for i in range(length):
        if (i<8):
            ex_marks=int(input(f'Enter the external marks of previous odd sem(only previous sem) code 18**3{i+1}\n'))
        else:
            ex_marks = int(input(f'Enter the external marks of previous odd sem(only previous sem) code18CPC39\n'))
        thirdsem_external.append(ex_marks)
if (dip_regular == 1):
    length = 10
    for i in range(length):
        if (i == 0):
            int_marks = int(input(f'Enter the internal marks  OF SUBcode 18MATDIP41 FOR 30\n'))
        elif (i > 0 and i < 9):
            int_marks = int(input(f'Enter the internal marks  OF  SUBcode 18**4{i+1} FOR 30\n'))
        else:
            int_marks = int(input(f'Enter the internal marks  OF  SUBcode 18KAN4{i+1}FOR 30\n'))
        forthsem_internal.append(int_marks)
else:
    length = 9
    for i in range(length):
        if (i < 8):
            int_marks = int(input(f'Enter the internal marks  OF  SUBcode 18**4{i+1} FOR 40\n'))
            forthsem_internal.append(int_marks)
        else:
            int_marks = int(input(f'Enter the internal marks  OF  SUBcode 18KAN4{i+1} FOR 40\n'))
            forthsem_internal.append(int_marks)
CIE=(avg_of_internal(forthsem_internal))


SEE=avg_of_external(thirdsem_external)
print(f"The avg SEE of{Name} 50 is{SEE}")
final_result=list(map(lambda x,:x+SEE,CIE))
for j in final_result:
    obtained_grade.append(grade_points(j))
    result = list(map(lambda n1, n2: n1 * n2, credits, obtained_grade))
sgpa=sum(result)/sum(credits)

print(f"Approximate SGPA is{sgpa}")
print(f"Approximate percentage is{(sum(final_result)/(total_marks))*100}%")
