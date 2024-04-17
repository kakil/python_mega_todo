# Journal App

# Get today's date
date = input("Enter today\'s date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow: ")

mood = '\n' + mood + '\n'
thoughts = thoughts + '\n'

journal_entry = [ date, mood, thoughts]

# write file to disk
filename = f"journal/{date}.txt"
with open(filename, 'w') as file:
    file.writelines(journal_entry)
