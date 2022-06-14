count2 = 0;
for count in range(20,51):
    if((count%3 == 0) or (count%5 == 0)):
        print(count)
        count2 += 1

text = f'３の倍数と５の倍数は{count2}でした。'
print(text)
