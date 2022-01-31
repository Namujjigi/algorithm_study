words = input()
bracket_flag = False
new_word = ''
answer = ''

for word in words:
    if not bracket_flag:
        if word == '<':
            bracket_flag = True
            answer += new_word[::-1]
            new_word = ''
            new_word += word
        elif word == ' ':
            answer += new_word[::-1]
            answer += word
            new_word = ''
        else:
            new_word += word
    elif bracket_flag:
        new_word += word
        if word == '>':
            bracket_flag = False
            answer += new_word
            new_word = ''




print(answer + new_word[::-1])