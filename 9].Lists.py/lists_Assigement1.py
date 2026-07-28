"""
List movies name and print first last and middle element from your list
and replace 3rd element with 0
"""
movies = ["Mirai","Rand De Basant","Dragon","LIK","Youth"]
n = len(movies)
movies[0]
print(f"First element of list is {movies[0]} ")
print(f"Last element of list is {movies[n - 1]} ")
print(f"Middle element of list is {movies[n//2]} ")
movies[2] = 0
print(movies)