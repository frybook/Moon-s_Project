import re
lines = "가wuC#m시든 꽃에 물을 주듯"
code_pattern = re.compile(r'\b(?:[A-G][#b]?(?:m7|M7|m|7|dim7|sus4|add9|6|9|aug|aug7)?(?:/[A-G][#b] ?)?(?:\((?:#|b)(?:[0-9]|1[0-3])\))?)\b')
code_matches = code_pattern.findall(lines)



#%%
import re

line = "œBbmFm/AbGm7(b5)C7"

chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11)?|M(?:6|7)?|dim7?|7(?:sus4)?|sus4|add9|6|9|aug(?:7)?|mM7)?(?:\([#b]?(?:[0-9]|1[0-3])\))?(?:/[A-G](?:#|b)?)?')
# exclude = input("제외할 문장을 말해주세요 : ")
# line1 = line.replace(exclude, "")
line2 = line.replace('˙', '').replace('œ', '').replace('N.C','').replace('D.S','').replace('Coda','').replace('.','').replace('‰','')
lyrics = re.sub(r'\b[A-Z][a-z]{2}\w*\b', '', line2)
code_matches = chord_pattern.findall(lyrics)


#%%
import re
text = "œœœœœœœœœGbDb/FœœœœœœœœœEbm7BwGb"

result = re.split(r'(?<=œ)', text)

print(result)

#%%
import re
text = "BabyIknowit'salreadyo-ver－Cm7"
A = re.compile(r'^(?![œ]:)')
chord = A(text)
#%%
# Abm Bbm Dbm Ebm Gbm 이게 
