from thuvien import *
import random
NumberQuestions = 2
BankQuestion = []
#hàm sinh xâu nhị phân liền trước
def PrevBinaryString(binary_string, is_exist):
    pos = int(len(binary_string)) - 1
    temp = list(binary_string)
    while pos >= 0 and temp[pos] == '0':
        temp[pos] = '1'
        pos -= 1
    if pos < 0:
        is_exist = False
    else:
        temp[pos] = '0'
    new_string = str(''.join(temp))
    return new_string, is_exist

for i in range(NumberQuestions):
    length = random.randint(7, 9) #độ dài xâu nhị phân
    k = random.randint(3, 4) #số xâu cần sinh 
    binary_string = "1" * length #xâu nhị phân bắt đầu
    #tạo list để lưu tất cả các xâu có độ dài length
    list_bin_str = []
    is_exist = True
    while is_exist == True:
        list_bin_str.append(list(map(int,binary_string)))
        binary_string, is_exist = PrevBinaryString(binary_string, is_exist)
    start_index = 1
    end_index = len(list_bin_str) - k - 1
    arrangement = list_bin_str[start_index : end_index] 
    #chọn ngẫu nhiên xâu cần sinh kế tiếp trong list từ start_index đến end_index để đảm bảo có đủ cấu hình
    current = random.choice(arrangement)
    index = list_bin_str.index(current)
    true_ans = list_bin_str[index + 1 : index + k + 1]
    #sinh đề bài
    ProblemStatement = "Cho xâu nhị phân $X = \\{ " + ', '.join(map(str, current)) + " \\}$" + \
                   f". Giả sử áp dụng phương pháp sinh xâu nhị phân theo thứ tự từ điển ,hãy liệt kê " + \
                   str(k) +" xâu nhị phân liền trước của $X?$"
    #sinh lời giải              
    loigiai = (  "\\textbf{Lời giải:} \n"
                "\\begin{itemize}\n"
                "\\item Xâu nhị phân bắt đầu được cho là: $" + ", ".join(map(str, current)) + "$.\n"
                "\\item Các xâu nhị phân liền trước được sinh ra dựa trên phương pháp sinh xâu nhị phân theo thứ tự từ điển lần lượt là:\n"
                "\\begin{itemize}\n"  )
    for perm in true_ans:
        loigiai += "\\item $" + ", ".join(map(str, perm)) + "$\n"

    loigiai += (
        "\\end{itemize}\n"
        "\\end{itemize}\n"
        "\n"
    )
    #sinh đáp án
    PA1 = "\\True" + '$'
    for perm in true_ans:
        PA1 += '(' + ', '.join(map(str, perm)) + ')'
    PA1 += '$'
    PA = [""] * 3
    for j in range(3):
        temp_list = true_ans.copy()
        random.shuffle(temp_list)
        PA[j] = '$'
        for perm in temp_list:
            PA[j] += '(' + ', '.join(map(str, perm)) + ')'
        PA[j] += '$'
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

fileout = open(r"D:\Project\CodeTaoDeTRR1\Python4Latex_TRR1\output\SINHXAUTRUOC.tex", mode="w", encoding = "utf-8")
Heading = open(r"D:\Project\CodeTaoDeTRR1\Python4Latex_TRR1\khaibao\beginfile.tex", encoding = "utf-8").read()
Footing = open(r"D:\Project\CodeTaoDeTRR1\Python4Latex_TRR1\khaibao\endfile.tex", encoding = "utf-8").read()
fileout.write(Heading + "\n")
fileout.write(GenerateQuestions)
fileout.write(Footing)
fileout.close()