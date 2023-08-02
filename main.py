import random

CHARACTERS: str = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pass_len: int = int(input("What will be the length of your password? "))
generated_password: str = ""

for i in range(pass_len):
    generated_char: str = random.choice(CHARACTERS)
    generated_password += generated_char

print(f"Generated password: {generated_password}")
