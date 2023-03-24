def arithmetic_arranger(problems):
    operators = []
    first_int = []
    sec_int = []
    answer = []
    count = 0
    int_len1= []
    int_len2= []
    space = 0
    for prob in problems:
        operators.append(str(prob.split(" ")[1]))
        first_int.append(int(prob.split(" ")[0]))
        sec_int.append(int(prob.split(" ")[2]))
        int_len1.append(len(prob.split(" ")[0]))
        int_len2.append(len(prob.split(" ")[2]))


    for sign in operators:
        if (sign != "+" and sign != "-"):
            return "Operator must be '+' or '-'"
        elif(sign == '+'):
            answer.append(first_int[count]+sec_int[count])
            count+=1
        else:
            answer.append(first_int[count]-sec_int[count])
            count+=1
    

    if (len(problems) > 5):
        return "Too many problems"

    arranged_problems = ''
    for i in range(len(problems)):
        if(i>0):
            space = 4
        
        if(int_len1[i]>= int_len2[i]):
            arranged_problems +=str(first_int[i]).rjust(int_len1[i]+2+space)
        else:
            arranged_problems +=str(first_int[i]).rjust(int_len2[i]+2+space)
    arranged_problems += '\n'
    space = 0
    for j in range(len(problems)):
        if (j==0):
            space = 2
        if(int_len1[j]>= int_len2[j]):
            arranged_problems+=(operators[j]+" "+str(sec_int[j])).rjust(int_len1[j]+2)
        else:
            arranged_problems+=(operators[j]+" "+str(sec_int[j])).rjust(int_len2[j]+2)

    return arranged_problems
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))