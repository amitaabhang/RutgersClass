name = “vikas”
letters = [letter for letter in name]
print(letters)
for i,v in enumerate(letters):
    print(i,v)
new_letters =[(i,v) for i,v in enumerate(letters)]
print(new_letters)
new_letters_if_up = [v.upper() for i,v in enumerate(letters) if i == 0]
print(new_letters_if_up)
new_letters_if_else = [v.upper() if i == 0 else v.lower() for i,v in enumerate(letters) ]
print(new_letters_if_else)
new_letters_if_mul = [v.upper() if i == 3 and v == “K” else v.lower() for i,v in enumerate(letters) ]
print(new_letters_if_mul)