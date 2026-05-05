# using list comprehensions:
# 1.create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)
# 2.create a new list of words that have lenth >=5
words = ['apple', 'mango', 'kiwi', 'egg', 'cherry', 'bread', 'we']
long_words = [word for word in words if len(word) >= 5]
print(long_words)
