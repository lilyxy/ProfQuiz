import csv

raw = []
with open('data.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in datareader:
        raw.append(' '.join(row))

quests = list(raw[0].split("\t"))
n = len(quests)
answers = list(i.split("\t") for i in raw[1:n+1])
data = list(i.split("\t") for i in raw[n+1:])
responses = []

for i in range(n):
    print(str(i+1)+".", quests[i])
    print()
    for j in range(len(answers[i])):
        print("  "+str(j+1)+")", answers[i][j])
    print(flush = True)
    responses.append(input())
    print()

tally = []
#print(responses)
for i in range(len(data)):
    score = list(map(lambda x, y: int(x == y), responses, data[i][1:]))
    #print(score, responses, data[i])
    tally.append([sum(score), score[::-1], data[i][0]])
tally.sort()
for t in tally:
    #print(t);
    continue;
print("If you were a UWaterloo Math Professor, you'd be:", tally[-1][2])
print()
print("Your next three closest profs, in order, are:")
for i in range(3):
    print(tally[-2-i][2])
print()

#print("Your complete ranking, from most to least alike:")
#for i in range(len(tally)):
#    print(tally[-1-i][2])
