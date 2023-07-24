# Gets two numbers from user, returnes result of different type of division
num_1, num_2 = int(input()), int(input())
string = f"""{num_1} / {num_2} = {num_1 / num_2}
{num_1} // {num_2} = {num_1 // num_2}
{num_1} % {num_2} = {num_1 % num_2}"""
print(string)
