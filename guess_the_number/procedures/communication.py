def guess(question, pre_question='', type_var=int):
    if pre_question != '':
        print(pre_question)
    return type_var(input(question))

def print_out(text):
    print(text)
