Transtotext = Transformation_roman[key_name[0]]

text_Trans = []

for sublist in Transtotext:
    for item in sublist:
        text_Trans.append(item)
        
# print(text_Trans)
# result = ' '.join(text_Trans)
#%%
def find_repeated_segments(chord_progression):
    n = len(chord_progression)
    repeats = []

    # Initialize a 2D list to store LCS lengths
    lcs_lengths = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the LCS lengths table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if chord_progression[i - 1] == chord_progression[j - 1] and i != j:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])

    # Traverse the LCS lengths table to find repeated segments
    i, j = n, n
    while i > 0 and j > 0:
        if lcs_lengths[i][j] > lcs_lengths[i - 1][j] and lcs_lengths[i][j] > lcs_lengths[i][j - 1]:
            if i != j:
                start_index = i - lcs_lengths[i][j]
                end_index = i
                repeated_segment = chord_progression[start_index:end_index]
                repeats.append(repeated_segment)
            i -= 1
            j -= 1
        elif lcs_lengths[i][j] == lcs_lengths[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return repeats

# Example chord progression
chord_progression = text_Trans
# Find repeated segments
repeated_segments = find_repeated_segments(chord_progression)

# Print the results
segm = []
for segment in repeated_segments:
    segm.append(segment)