# Gets three numbers, returns in format Vector A(x, y, z) and Vector B each number is bigger on 5.
x, y, z = int(input()), int(input()), int(input())
vectors = f"""Vector A({x}, {y}, {z})
Vector B({x + 5}, {y + 5}, {z + 5})"""
print(vectors)
