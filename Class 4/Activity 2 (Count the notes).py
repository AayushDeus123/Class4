#Count the number of notes in a given amount
amount = int(input('Write the amount of money to be counted '))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print('Number of notes of 100 is :', note1)
print('Number of notes of 50 is :', note2)
print('Number of notes of 10 is :', note3)