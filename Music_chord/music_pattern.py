#%%
def texting(Transtotext):
    text_Trans = []
    for sublist in Transtotext:
        for item in sublist:
            text_Trans.append(item)
    return text_Trans
        

#%%
# 코드 반복

from collections import defaultdict

def find_repeated_segments(music_text):
    repeats = defaultdict(int)

    # Iterate over each possible length from 4 to 8
    for length in range(4, 9):
        # Use a sliding window to extract segments of the current length
        for i in range(len(music_text) - length + 1):
            segment = tuple(music_text[i:i + length])
            repeats[segment] += 1

    # Filter out segments that do not repeat
    repeats = {k: v for k, v in repeats.items() if v > 1}


    

    return repeats

#%%
import csv
def export_to_csv(dictionary, filename):
    full_path = '분석코드/' + filename
    
    with open(full_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Pattern', 'Count'])
        for pattern, count in dictionary.items():
            writer.writerow([pattern, count])

