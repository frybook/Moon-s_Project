from PyPDF2 import PdfReader
import re


def text_setting():
    title = input("곡 제목을 말해주세요 :")
    reader = PdfReader(f"{title}.pdf")
    pages = reader.pages
    text = ""
    for page in pages:
        sub = page.extract_text()
        text += sub
    lines = text.split('\n')
    return lines

#%%

def text_chords(lines):
    cleaned_lines = []
    print("대문자1 소문자 2개가 붙어있는 단어,문장을 제외해주세요")
    print("------------------------------------------------------")
    exclude = input("제외할 문장을 말해주세요 : ")
    for line in lines:
        line = line.replace(exclude, "").strip()
        line = line.replace("Feat", "").strip()
        cleaned_line = ''.join(line.split())
        cleaned_lines.append(cleaned_line)
    return cleaned_lines
#%%
def Find_chords(cleaned_lines):   
    chords = []
    formatted_chords = []
    chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11)?|M(?:6|7)?|dim7?|7(?:sus4)?|sus4|add9|6|9|aug(?:7)?|mM7)?(?:\([#b]?(?:[0-9]|1[0-3])\))?(?:/[A-G](?:#|b)?)?')
    for line in cleaned_lines:
        line1 = line.replace('˙', '').replace('œ', '').replace('N.C','').replace('D.S','').replace('Coda','').replace('.','').replace('‰','')        
        chord_matches = chord_pattern.findall(line1)
        if chord_matches:
            chords.append(' '.join(chord_matches))
    
    for chord_pair in chords:
        formatted_chords.append(', '.join([f'"{chord}"' for chord in chord_pair.split()]))
    chords2 = []
    for chord_string in formatted_chords:
        pairs = chord_string.split(', ')
        chords2.append([pair.strip('"') for pair in pairs])
    
    return chords2


