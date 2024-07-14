'''
Create a list of your friends' names. The list should have at least 5 names.
Create a list of tuples. Each tuple should contain a friend's name and the length of the name.
For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)
'''

friends = ["Subham", "Arpita", "Bubli", "Sonu", "Ritu"]

friend_tuples = [(friend, len(friend)) for friend in friends]

print(friend_tuples)

'''
You and your partner are planning a trip, and you want to track expenses.
Create two dictionaries, one for your expenses and one for your partner's expenses.
Each dictionary should contain at least 5 expense categories and their corresponding amounts.
For example:
Your expenses
your_expenses = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}
Your partner's expenses
partner_expenses = {
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}
Calculate the total expenses for each of you and print the results.
Determine who spent more money overall and print the result.
Find out the expense category where there is a significant difference in spending between you and your partner.
Print the category and the difference.

'''

# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Your partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}


your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Total of expenses of your is {your_total}")
print(f"Total of expenses of your_partner is {partner_total}")


if your_total > partner_total:
    print("You spent more overall.")
else:
    print("Your partner spent more overall.")


max_difference = max(your_total, partner_total) - min(your_total, partner_total)
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference >= max_difference * 0.3:  # Adjust the threshold as needed
        print(f"Significant difference in {category}: {difference}")
