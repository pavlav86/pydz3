import re
 
s = input()
d = {'[AEIOULNSTRАВЕИНОРСТ]': '1', '[DGДКЛМПУ]': '2', '[BCMPБГЁЬЯ]': '3', '[FHVWYЙЫ]': '4', '[KЖЗХЦЧ]': '5', '[JXШЭЮ]': '8', '[QZФЩЪ]': '10'}
for k in d:
    s = re.sub(k, d[k], s)
print(sum(map(int, s)))