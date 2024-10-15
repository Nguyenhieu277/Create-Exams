import random
import itertools

NumberQuestions = 2
BankQuestions = []

def nextCombination(combination, numVars):
    index = numVars - 1
    while index >= 0 and combination[index] == 9 - numVars + index + 1:
        index -= 1
    if index >= 0:
        combination[index] += 1
        for j in range(index + 1, numVars):
            combination[j] = combination[j - 1] + 1
        return True
    return False

def prevCombination(combination, numVars):
    index = numVars - 1
    while index >= 0 and combination[index] == combination[index - 1] + 1:
        index -= 1
    if index >= 0:
        combination[index] -= 1

        for j in range(index + 1, numVars):
            combination[j] = 9 - numVars + j + 1
        return True
    return False    


def CombinationNth(Comb, combination, numVars):
    dic = {}
    i = 1
    while True:
        if nextCombination(Comb, numVars):
            dic[Comb] = i
            i += 1
        else: break
    return dic[combination]

for number in range(NumberQuestions):
    while True:
        numVars = random.randint(5, 8)
        Combinations = []
        combination = random.sample(range(1, 10), numVars)
        combination.sort()
        Combinations.append(combination[:])
        numberOfNextElement = random.randint(3, 6)
        
        ProblemStatement = "Cho tập $A = \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\}$. Giả sử áp dụng phương pháp sinh tổ hợp" + \
                           "theo thứ tự từ điển, hãy liệt kê $ " + str(numberOfNextElement) + " $ tổ hợp chập $ " + str(numVars) + " $ liền kề tiếp theo của tổ hợp $(" + \
                           ", ".join(map(str, combination)) + ").$"
        
        # Sinh tổ hợp tiếp theo
        for _ in range(numberOfNextElement):
            if nextCombination(combination, numVars):
                Combinations.append(combination[:])
            else:
                break
        
        # Kiểm tra nếu có đủ ít nhất đủ tổ hợp
        if len(Combinations) >= numberOfNextElement + 1:
            break  # Thoát khỏi vòng lặp while nếu đủ tổ hợp
        
    Solved = (  "\\textbf{Lời giải:} \n"
                "\\begin{itemize}\n"
                "\\item Tổ hợp bắt đầu được cho là: $" + ", ".join(map(str, Combinations[0])) + "$.\n"
                "\\item Các tổ hợp tiếp theo được sinh ra dựa trên phương pháp sinh tổ hợp chập $" + str(numVars) + "$ theo thứ tự từ điển lần lượt là:\n"
                "\\begin{itemize}\n"  )
    for comb in Combinations[1:]:
        Solved += "\\item $" + ", ".join(map(str, comb)) + "$\n"

    Solved += (
        "\\end{itemize}\n"
        "\\end{itemize}\n"
        "\n"
    )
    CorrectAnswers = []
    for comb in Combinations[1:]:
        next_combination_str = ", ".join(map(str, comb))
        CorrectAnswers.append(f"\n({next_combination_str})")
    PA1 = ""
    PA1 += "\\True $"
    PA1 += "".join(CorrectAnswers)
    PA1 += "$"

    IncorrectAnswers1 = CorrectAnswers[:]
    while True:
        if IncorrectAnswers1 == CorrectAnswers:
            random.shuffle(IncorrectAnswers1)
        else:
            break
    PA2 = ""
    PA2 += "$"
    PA2 += "".join(IncorrectAnswers1)
    PA2 += "$"

    IncorrectAnswers2 = CorrectAnswers[:]
    while True:
        if IncorrectAnswers2 == CorrectAnswers:
            random.shuffle(IncorrectAnswers2)
        else:
            break
    PA3 = ""
    PA3 += "$"
    PA3 += "".join(IncorrectAnswers2)
    PA3 += "$"

    IncorrectAnswers3 = CorrectAnswers[:]
    while True:
        if IncorrectAnswers3 == CorrectAnswers:
            random.shuffle(IncorrectAnswers3)
        else:
            break
    PA4 = ""
    PA4 += "$"
    PA4 += "".join(IncorrectAnswers3)
    PA4 += "$"
    
    PA = [PA1, PA2, PA3, PA4]
    random.shuffle(PA)
    Question1 = "\\begin{ex}\n" + \
    ProblemStatement + "\n" + \
    "\\choice\n" + \
    "{"+PA[0]+"}\n" + \
    "{"+PA[1]+"}\n" + \
    "{"+PA[2]+"}\n" + \
    "{"+PA[3]+"}\n" + \
    "\\loigiai{\n" + \
    str(Solved) + "\n" + \
    "}\n" + \
    "\\end{ex}\n"

    while True:
        numVars = random.randint(5, 8)
        Combinations = []
        combination = random.sample(range(1, 10), numVars)
        combination.sort()
        Combinations.append(combination[:])
        numberOfNextElement = random.randint(3, 6)
        
        ProblemStatement = "Cho tập $A = \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\}$. Giả sử áp dụng phương pháp sinh tổ hợp " + \
                           "theo thứ tự từ điển, hãy liệt kê $ " + str(numberOfNextElement) + " $ tổ hợp chập $ " + str(numVars) + " $ liền trước của tổ hợp $(" + \
                           ", ".join(map(str, combination)) + ").$"
        
        # Sinh tổ hợp tiếp theo
        for _ in range(numberOfNextElement):
            if prevCombination(combination, numVars):
                Combinations.append(combination[:])
            else:
                break
        
        # Kiểm tra nếu có đủ ít nhất đủ tổ hợp
        if len(Combinations) >= numberOfNextElement + 1:
            break  # Thoát khỏi vòng lặp while nếu đủ tổ hợp
        
    Solved = (  "\\textbf{Lời giải:} \n"
                "\\begin{itemize}\n"
                "\\item Tổ hợp bắt đầu được cho là: $" + ", ".join(map(str, Combinations[0])) + "$.\n"
                "\\item Các tổ hợp liền trước được sinh ra dựa trên phương pháp sinh tổ hợp chập $" + str(numVars) + "$ theo thứ tự từ điển lần lượt là:\n"
                "\\begin{itemize}\n"  )
    for comb in Combinations[1:]:
        Solved += "\\item $" + ", ".join(map(str, comb)) + "$\n"

    Solved += (
        "\\end{itemize}\n"
        "\\end{itemize}\n"
        "\n"
    )
    CorrectAnswers = []
    for comb in Combinations[1:]:
        next_combination_str = ", ".join(map(str, comb))
        CorrectAnswers.append(f"\n({next_combination_str})")
    PA1 = ""
    PA1 += "\\True $"
    PA1 += "".join(CorrectAnswers)
    PA1 += "$"

    IncorrectAnswers1 = CorrectAnswers[:]
    while True:
        if IncorrectAnswers1 == CorrectAnswers:
            random.shuffle(IncorrectAnswers1)
        else:
            break
    PA2 = ""
    PA2 += "$"
    PA2 += "".join(IncorrectAnswers1)
    PA2 += "$"

    IncorrectAnswers2 = CorrectAnswers[:]
    while True:
        if IncorrectAnswers2 == CorrectAnswers:
            random.shuffle(IncorrectAnswers2)
        else:
            break
    PA3 = ""
    PA3 += "$"
    PA3 += "".join(IncorrectAnswers2)
    PA3 += "$"

    IncorrectAnswers3 = CorrectAnswers[:]
    while True:
        if IncorrectAnswers3 == CorrectAnswers:
            random.shuffle(IncorrectAnswers3)
        else:
            break
    PA4 = ""
    PA4 += "$"
    PA4 += "".join(IncorrectAnswers3)
    PA4 += "$"
    
    PA = [PA1, PA2, PA3, PA4]
    random.shuffle(PA)
    Question2 = "\\begin{ex}\n" + \
    ProblemStatement + "\n" + \
    "\\choice\n" + \
    "{"+PA[0]+"}\n" + \
    "{"+PA[1]+"}\n" + \
    "{"+PA[2]+"}\n" + \
    "{"+PA[3]+"}\n" + \
    "\\loigiai{\n" + \
    str(Solved) + "\n" + \
    "}\n" + \
    "\\end{ex}\n"

    BankQuestions.append(Question1)
    BankQuestions.append(Question2)

GenerateQuestions = ""
for question in BankQuestions:
    GenerateQuestions += question
fileout = open("D:/work/C/Python4Latex_TRR1/output/generateCombination.tex", mode="w", encoding = "utf-8")
Heading = open("D:/work/C/Python4Latex_TRR1/khaibao/beginfile.tex", encoding = "utf-8").read()
Footing = open("D:/work/C/Python4Latex_TRR1/khaibao/endfile.tex", encoding = "utf-8").read()
fileout.write(Heading + "\n")
fileout.write(GenerateQuestions)
fileout.write(Footing)
fileout.close()
