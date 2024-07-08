# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
def time_stone(): 
    def minutes_to_seconds(minutes):
        return minutes * 60
    
    def hours_to_seconds(hours):
        return hours * 3600
    
    def seconds_in_a_day():
        return 24 * hours_to_seconds(1)
    
    def hours_in_june():
        return 30 * 24
    
    def minutes_in_august():
        return 31 * 24 * 60
    
    def minutes_in_days():
        return 24 * 60
    
    def minutes_in_weeks():
        return 7 * minutes_in_days()
    
    def how_do_you_measure_a_year():
        return minutes_in_days() * 3
    
    print("1 minute =", minutes_to_seconds(1), "seconds")
    print("5 minutes =", minutes_to_seconds(5), "seconds")
    print("1 hour =", hours_to_seconds(1), "seconds")
    print("seconds in a day:", seconds_in_a_day())
    print("hours in june:", hours_in_june())
    print("minutes in august:", minutes_in_august())
    print("minutes in weeks:", minutes_in_weeks())
    print ("minutes in a day:", minutes_in_days())
    print("midnights and sunsets:", how_do_you_measure_a_year())
time_stone()
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
def mid(k):
    length = len(k)
    if length % 2 == 0:
        return ""
    else:
        middle = length // 2
        return k[middle]
print(mid("abc"))
print(mid("kass"))
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
def credit_card():
    card_number = input('enter your card number').strip()
    hide_number = len(card_number)-4
    hidden_card = '*' * hide_number + card_number[-4:]
    return hidden_card
print("card:", credit_card())
# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
def online_count():
    statuses = {
        "John": "online",
        "Paul": "offline",
        "George": "online",
        "Ringo": "offline"
    }
    count = 0
    for status in statuses.values():
        if status == "online":
            count += 1 
    return count
print(online_count())

# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
def calculate_discount(full_price, discount):
    discount_total = (full_price * discount) / 100
    discounted = full_price - discount_total
    return discounted
original_price = int(input("enter the original price of the item: "))
discount_percent = int(input("enter the discount percentage: "))
discounted_price = calculate_discount(original_price, discount_percent)
print(f'The discounted price is: {discounted_price}')
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
def calculate_hypotenuse(adjacent, opposite):
    hypotenuse = (adjacent ** 2 + opposite ** 2) ** 0.5
    return hypotenuse
print('hyp1:', calculate_hypotenuse(3, 4))
print('hyp2:', calculate_hypotenuse(5, 12))

# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
def fibonacci(purple, blue):
    fibonacci_list = [purple, blue]
    for _ in range(2, 11): 
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list
purple = int(input("whats the first number to start the Fibonacci sequence: "))
blue = int(input("whats the second number to start the Fibonacci sequence: "))
fib_sequence = fibonacci(purple, blue)
print(f"here are the next intervals in the Fibonacci sequence starting with {purple} and {blue}:")
print(fib_sequence)

# ---------------------------------
