import pandas as pd
from roman import extract_base_note,extract_chord_type
from Import_csv import extract_roman_numerals
All_Major_scale = pd.read_csv("All_Major_scale.csv", index_col='KEY')

#%%
def process_key(Order_of_keys, chords, Major_scale):
    roman_chords = []
    
    # Splitting the chords string into a list of chords
    chord_list = chords.split(' ')

    for idx, key in enumerate(Order_of_keys):
        romanized_chord_list = []

        for chord_pair in chord_list:
            romanized_chord_pair = []

            for note in chord_pair.split():
                base_note = extract_base_note(note)
                chord_type = extract_chord_type(note)
                found = False

                for col_name in Major_scale.columns:
                    scale_values = Major_scale.at[key, col_name].split(',')
                    if base_note in scale_values:
                        roman_numeral = col_name
                        chord_notation = f"{roman_numeral}{chord_type}" if chord_type else roman_numeral
                        found = True
                        break

                if not found:
                    romanized_chord_pair.append(note)
                    continue

                inversion_info = ''
                if '/' in note:
                    inversion_note = note.split('/')[1]
                    inversion_found = False
                    for col_name in Major_scale.columns:
                        scale_values = Major_scale.at[key, col_name].split(',')
                        if inversion_note in scale_values:
                            inversion_info = col_name
                            inversion_found = True
                            break
                    if not inversion_found:
                        inversion_info = inversion_note

                if inversion_info:
                    romanized_chord_pair.append(f"{chord_notation}/{inversion_info}")
                else:
                    romanized_chord_pair.append(chord_notation)

            romanized_chord_list.append(' '.join(romanized_chord_pair))

        roman_chords.append(romanized_chord_list)

    return roman_chords
#%%
# Example usage:
Order_of_keys = ["Bb_Key"]
chords = "EbM7 EbmM7 Dm7 G7(b9) Cm7 F7sus4"

processed_chords = process_key(Order_of_keys, chords, All_Major_scale)
new_chord_list = []
for chord in processed_chords:
    new_chord_list.extend(chord)
roman_numerals = extract_roman_numerals(new_chord_list)

print(roman_numerals)
#%%
