'''
    * Name: Zwelibanzi Gumede
    * Date:25 March 2023
    * This is the program which do the sum of two numbers.
    '''
def arithmetic_arranger(problems, bool = False):
    operators = []
    first_int = []
    sec_int = []
    answer = []
    int_len1= []
    int_len2= []
    count = 0
   
    space = 0
    if (len(problems) > 5):
        return "Too many problems."
    for prob in problems:
        operators.append(str(prob.split(" ")[1]))
        if((prob.split(" ")[0]).isdigit() and prob.split(" ")[2].isdigit()):
            first_int.append(int(prob.split(" ")[0]))
            sec_int.append(int(prob.split(" ")[2]))
        else:
            return "Numbers must only contain digits."
        

        int_len1.append(len(prob.split(" ")[0]))
        int_len2.append(len(prob.split(" ")[2]))


    for sign in operators:
        if (sign != "+" and sign != "-"):
            return "Operator must be '+' or '-'."
        elif(sign == '+'):
            answer.append(first_int[count]+sec_int[count])
            count+=1
        else:
            answer.append(first_int[count]-sec_int[count])
            count+=1
    

    for i in range(len(problems)):
        if (len(str(first_int[i]))> 4 or len(str(sec_int[i]))>4):
            return "Numbers cannot be more than four digits."

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
            if(int_len1[j]>= int_len2[j]):
                arranged_problems+=(operators[j]+" "+abs(len(str(first_int[j]))-len(str(sec_int[j])))*" "+str(sec_int[j])).rjust(int_len1[j]+2)
            else:
                arranged_problems+=(operators[j]+" "+str(sec_int[j])).rjust(int_len2[j]+2)
        else:
            if(int_len1[j]>= int_len2[j]):
                arranged_problems+=4*" "
                arranged_problems+=(operators[j]+" "+abs(len(str(first_int[j]))-len(str(sec_int[j])))*" "+str(sec_int[j])).rjust(int_len1[j]+2)
                
            else:
                arranged_problems+=4*" "
                arranged_problems+=(operators[j]+" "+str(sec_int[j])).rjust(int_len2[j]+2)
                
    arranged_problems+='\n'
    
    for x in range(len(problems)):
        if x==0:
            if(int_len1[j]>= int_len2[j]):
                arranged_problems+=2*"-"+int_len1[x]*"-"
            else:
                arranged_problems+=2*"-"+int_len2[x]*"-"
        else:
            arranged_problems+=4*" "
            if(int_len1[x]>= int_len2[x]):
               
                arranged_problems+=2*"-"+int_len1[x]*"-"
            else:
                arranged_problems+=2*"-"+int_len2[x]*"-"



    if bool != True:
         return arranged_problems
    else:
        arranged_problems+='\n'
        for y in range(len(problems)):
            if(y>0):
                space = 4
            
            if(int_len1[y]>= int_len2[y]):
                arranged_problems +=str(answer[y]).rjust(int_len1[y]+2+space)
            else:
                arranged_problems +=str(answer[y]).rjust(int_len2[y]+2+space)
        return arranged_problems

    return ""
    
   
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True))