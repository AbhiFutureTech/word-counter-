sentence = """Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants.
 When confronted with humans, piranhas’ first instinct is to flee, not attack. 
 Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas. 
 If the fish are well-fed, they won’t bite humans."""

sentence = sentence.replace(',','').lower().split()
wc ={}
for word in sentence:
    if word in wc.keys():
        wc[word]+=1
    else:
        wc[word] = 1
        print(wc)



