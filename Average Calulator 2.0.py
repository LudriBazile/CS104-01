numberOfTest = 0
score = 0
average = 0.0
scoreCount = 0
total = 0.0

numberOfTest = int(input ("Please enter the number of test scores you want to average "))
while scoreCount < numberOfTest:
    score = int(input("Please enter a score: "))
    scoreCount = scoreCount + 1
    total = total + score

average = total/scoreCount
print (average)
