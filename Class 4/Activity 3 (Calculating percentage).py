#Calculating Percentage
print('Enter the marks obtained in the following subjects ')
maths = int(input('Number of marks for Maths : '))
english = int(input('Number of marks for English : '))
hindi = int(input('Number of marks for Hindi : '))
science = int(input('Number of marks for Science : '))

sum = maths+english+hindi+science
perc = (sum/400)*100

print('The Percentage of marks obtained is = ', perc)