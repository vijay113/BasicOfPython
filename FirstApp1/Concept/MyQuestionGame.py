class Question:
    def __init__(self,question_promt,question_ans):
        self.question_promt = question_promt
        self.question_ans = question_ans

########################################

question_prompts = [
    "Tell the color of apple\n (a) Black\n (b) Red \n (c) Orange \n",
     "Tell the color of Orange\n (a) Black\n (b) Red \n (c) Orange \n",
     "Tell the color of Leaf\n (a) Green\n (b) Red \n (c) Orange \n",
     ]



question_list = [
 Question(question_prompts[0],"b"),
 Question(question_prompts[1],"c"),
 Question(question_prompts[2],"a")
]     


def run_test(questions):
    score = 0
    for question in questions:        
        ans = input(question.question_promt)
        if ans == question.question_ans:
            print("ans correct.")
            score += 1
        else:
            print("ans wrong.")
            score -= 1
    return score    

final_score = 0
final_score = run_test(question_list)
print("Your final score is: "+str(final_score))
if final_score == 3:
    print("You WIN..!!")
else: 
    print("You LOST..!!")    
##################################






