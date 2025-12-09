import math
# 1 - misol
primes = tuple(n for n in range(2, 31) if all(n % i != 0 for i in range(2, int(math.sqrt(n))+1)))
print(primes)
# 2 - misol
numbers = [-5, 3, -1, 0, 7, -2]
positive_numbers = tuple(n for n in numbers if n > 0)
print(positive_numbers)

# 3 - misol
num_squares = tuple((n, n**2) for n in range(1, 16))
print(num_squares)

# 4 - misol
text = "hello world python"
last_letters = tuple(w[-1] for w in text.split())
print(last_letters)

# 5 - misol
odd_index_squares = tuple(n**2 for i, n in enumerate(range(1, 21)) if i % 2 == 1)
print(odd_index_squares
      )
# 6 - misol
words = ["apple", "banana", "orange", "grape", "umbrella"]
vowel_start = tuple(w for w in words if w[0].lower() in 'aeiou')
print(vowel_start)

# 7 - misol
palindromes = tuple(n for n in range(1, 51) if str(n) == str(n)[::-1])
print(palindromes)

# 8 - misol
s = "python"
unicode_vals = tuple(ord(c) for c in s)
print(unicode_vals)

# 9 - misol
cubes_of_5 = tuple(n**3 for n in range(1, 21) if n % 5 == 0)
print(cubes_of_5)

# 10 - misol
words2 = ["tree", "apple", "sun", "mountain", "sky"]
long_words = tuple(w for w in words2 if len(w) > 4)
print(long_words)
