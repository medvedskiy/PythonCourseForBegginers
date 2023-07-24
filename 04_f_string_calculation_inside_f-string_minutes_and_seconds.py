# Program reads variable from user, after that returns number of minutes and seconds with f-string
seconds = int(input())
string = f"""{seconds} сек - это {seconds // 60} мин. {seconds % 60} сек."""
print(string)
