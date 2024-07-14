'''
You have a list of superheroes representing the Justice League. justice_league = ["Superman", "Batman",
"Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

Perform the following tasks:

1. Calculate the number of members in the Justice League.
2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.
3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman"
   and move them in between Aquaman and Flash.
5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the
   following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.

(BONUS: Can you predict who the new leader will be?)

Your task is to write Python code to perform these operations on the "justice_league" list.
Display the list at each step to observe the changes.
'''

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members in the Justice League.
print(f"1. Number of members in justice league is: {len(justice_league)}\n", )

# 2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.
justice_league.extend(["Batgirl", "Nightwing"])
print(f"2. After adding Batgirl and Nightwing, now justice league is: {justice_league}\n")

# 3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.insert(0, justice_league.pop(justice_league.index("Wonder Woman")))
print("3(i). Now our new leader is:", justice_league[0])
print(f"3(ii). Here is our updated team: {justice_league}\n")

''' 4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or 
       "Superman" and move them in between Aquaman and Flash. '''
aquaManIndex = justice_league.index("Aquaman")
justice_league.insert(aquaManIndex, justice_league.pop(justice_league.index("Green Lantern")))
print(f"4. Here is our updated team as per the requirement: {justice_league}\n")

''' 5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with 
       the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow". '''
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"5. Here is our new team: {justice_league}\n")

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print(f"6. Here is the sorted list of new Justice League: {justice_league}\n")

# BONUS: Can you predict who the new leader will be?
print("BONUS: The new leader of Justice League is:", justice_league[0])
