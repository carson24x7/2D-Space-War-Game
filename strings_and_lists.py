name = "Carson Miller"
print(name)
print(type(name))

num_chars = len(name)
print(num_chars)

print(name[1])
print(name[2])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])
print(name[12])
#print(name[13])
print()

print(name[-2])
print(name[-1])
print()

for character in name:
    print(character)
print()


pi_digits = [3,1,4,1,5,9,2,6]
movie_titles = ['Avengers Endgame','Avengers Infinity War','Cars','Spiderman Far From Home','Inside Out','Up']
print(pi_digits)
print(type(pi_digits))

num_items = len(pi_digits)
print(num_items)
print()

print(pi_digits[0])
print(pi_digits[1])
print(pi_digits[2])
print(pi_digits[4])
#print(pi_digits[8])
print()

print(pi_digits[-3])
print(pi_digits[-2])
print()

for word in pi_digits:
    print(word)
print()

for digit in pi_digits:
    if digit > 5:
        print(digit)

print()

for word in movie_titles:
    print(word[0])
print()

for characters in movie_titles:
    num_chars = len(characters)
    print(num_chars)

# You try...

# 1. Write a line of code that stores your name in a string
# Carson Miller
# 2. Write a line of code that prints the number of characters in your name.
#13
# 3. Write lines of code that print the first, second, and last characters in your name.
# A,R,M,I,L,L,E,R
# 4. Write a loop that prints each character of your name on a separate line.
#C,A,R,S,O,N M,I,L,L,E,R
# 5. Write a line of code that stores the first 8 digits of pi in a list.
#31415926
# 6. Write a line of code that prints the third and second to last digits of your pi list.
#print(digit[-3]) print(digit[-2]) - 9, 2
# 7. Write a loop that prints each of your digits of pi that is greater than 6.
#9,6
# 8. Write a line of code that stores 6 movies you like in a list.
# Avengers Endgame, Avengers Infinity War, Spiderman Far From Home, Cars, Inside Out and Up.
# 9. Write a loop that prints the first character of each movie title.
#A, A, C, S, I, U.
# 10. Write a loop that prints the number of characters in each movie title.
#16, 21, 4, 23, 10, 2
