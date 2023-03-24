def arithmetic_arranger(problems):
  operators = []
  first_int = []
  sec_int = []
  for prob in problems:
    operators.append(prob.split(" ")[1])
    first_int.append(prob.split(" ")[0])
    sec_int.append(prob.split(" ")[2])

  if (len(problems) > 5):
    return "Too many problems"

  arranged_problems = ''

  return arranged_problems