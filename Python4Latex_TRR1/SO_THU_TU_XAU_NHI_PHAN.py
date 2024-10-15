import random
from thuvien import *

NumberQuestions = 2
BankQuestion = []

#Hàm sinh xâu nhị phân kế tiếp
def NextBinaryString(binary_string, is_exist):
    pos = int(len(binary_string)) - 1
    temp = list(binary_string)
    while pos >= 0 and temp[pos] == '1':
        temp[pos] = '0'
        pos -= 1
    if pos < 0:
        is_exist = False
    else:
        temp[pos] = '1'
    new_string = str(''.join(temp))
    return new_string, is_exist
    
for i in range(NumberQuestions):
    length = random.randint(7, 9) #độ dài xâu nhị phân
    k = random.randint(3, 4) #số xâu cần sinh 
    binary_string = "0" * length #xâu nhị phân bắt đầu
    #tạo list để lưu tất cả các xâu có độ dài length
    list_bin_str = []
    is_exist = True
    while is_exist == True:
        list_bin_str.append(binary_string)
        binary_string, is_exist = NextBinaryString(binary_string, is_exist)
    current = random.choice(list_bin_str)
    true_ans = list_bin_str.index(current) + 1
    #sinh đề bài
    ProblemStatement = "Cho xâu nhị phân $X = \\{ " + ', '.join(list(current)) + " \\}$" + \
                   f". Hãy xác định xem đó là xâu nhị phân thứ bao nhiêu nếu liệt kê theo thứ tự tăng dần."
    #sinh lời giải               
    loigiai = (  "\\textbf{Lời giải:} \n"
                "\\begin{itemize}\n"
                "\\item Trong thứ tự tăng dần, số thứ tự của xâu $" + current + "$ chính là giá trị thập phân của nó cộng thêm 1."
                "\\item Do giá trị thập phân là $" + str(true_ans - 1) + "$, số thứ tự nếu liệt kê theo thứ tự tăng dần sẽ là $" + str(true_ans) + "$"
                "\\end{itemize}\n"  )
    
    #khởi tạo đáp án
    PA1 = "\\True" + '$' + str(true_ans) + '$'
    PA = [""] * 3
    for j in range(3):
        PA[j] = '$' + str(true_ans + j + 1) + '$'
    PA.append(PA1)
    random.shuffle(PA)
    #tạo câu hỏi hoàn chỉnh
    question = "\\begin{ex}\n" + \
    ProblemStatement + "\n" + \
    "\\choice\n" + \
    "{"+PA[0]+"}\n" + \
    "{"+PA[1]+"}\n" + \
    "{"+PA[2]+"}\n" + \
    "{"+PA[3]+"}\n" + \
    "\\loigiai{\n" + \
    loigiai + "\n" + \
    "}\n" + \
    "\\end{ex}\n"
    #thêm câu hỏi tạo được vào ngân hàng câu hỏi
    BankQuestion.append(question)
    
GenerateQuestions = ""
for question in BankQuestion:
    GenerateQuestions += question

fileout = open(r"D:\Project\CodeTaoDeTRR1\Python4Latex_TRR1\output\thutuxaunhiphan.tex", mode="w", encoding = "utf-8")
Heading = open(r"D:\Project\CodeTaoDeTRR1\Python4Latex_TRR1\khaibao\beginfile.tex", encoding = "utf-8").read()
Footing = open(r"D:\Project\CodeTaoDeTRR1\Python4Latex_TRR1\khaibao\endfile.tex", encoding = "utf-8").read()
fileout.write(Heading + "\n")
fileout.write(GenerateQuestions)
fileout.write(Footing)
fileout.close()