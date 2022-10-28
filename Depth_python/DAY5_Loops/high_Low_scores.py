student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highScore = 0
lowestScore = student_scores[3] #ambil random from list to compare

for i, score in enumerate(student_scores):
    if score > highScore:
        highScore = score

    if score < lowestScore:
        lowestScore = score

print(lowestScore)
print(highScore)
    
