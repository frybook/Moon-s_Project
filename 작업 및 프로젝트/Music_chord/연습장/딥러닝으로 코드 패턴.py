import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Example chord progression (from your provided data)
chord_progressions = ['Ⅳ', 'Ⅴ', 'Ⅴ7', 'Ⅰ', 'Ⅴ', 'ⅶdim', 'ⅲ', 'ⅵm', 'Ⅳ', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅴ7', 'Ⅴ7', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅳm', 'Ⅰ', 'ⅱ7', 'Ⅴ7', 'Ⅴ7', 'Ⅰ', 'ⅲ7', 'ⅵm', 'ⅲm', 'Ⅳ', 'Ⅴ7', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅴ7', 'Ⅴ7', 'Ⅳ', 'Ⅴ', 'Ⅴ7', 'Ⅰ', 'Ⅴ', 'ⅶm7(b5)', 'ⅲ7', 'ⅵm', 'Ⅳ', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅴ7', 'Ⅴ7', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅳm', 'Ⅰ', 'ⅱ7', 'Ⅳ', 'Ⅴ7', 'Ⅴ7', 'Ⅴ7', 'Ⅳ', 'Ⅴ7', 'ⅱm', 'Ⅳ', 'Ⅴ7', 'Ⅴ7', 'Ⅴ7', 'Ⅰ', 'ⅲ7', 'ⅵm', 'ⅲm', 'Ⅳ', 'Ⅴ7', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅴ7', 'Ⅳ', 'Ⅴ', 'Ⅴ7', 'Ⅰ']

flat_chord_list = [chord for progression in chord_progressions for chord in progression]

# Tokenize the chords
tokenizer = Tokenizer()
tokenizer.fit_on_texts(chord_progressions)

# Convert chord progressions to sequences of integers
chord_sequences = [tokenizer.texts_to_sequences(progression) for progression in chord_progressions]

#%%

for seq in chord_sequences:
    print(seq)
    print('-' * 100)
    xs = []
    for s in seq:
        xs.append(s)
    print('xs:', xs)

#%%
# Convert sequences to numpy array with dtype=object
chord_sequences = np.array([np.array(seq).flatten() for seq in chord_sequences], dtype=object)

# Pad sequences to ensure they have the same length
max_sequence_length = max(len(seq) for seq in chord_sequences)
padded_sequences = pad_sequences(chord_sequences, maxlen=max_sequence_length, padding='post', truncating='post')

# Prepare input (X) and output (y)
sequence_length = 4  # Length of input sequences

X = []
y = []

for seq in padded_sequences:
    for i in range(len(seq) - sequence_length):
        X.append(seq[i:i + sequence_length])
        y.append(seq[i + sequence_length])

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Ensure y is the correct shape for sparse categorical cross-entropy
y = np.expand_dims(y, -1)

vocab_size = len(tokenizer.word_index) + 1
#%%
import pickle

# Save tokenizer for future use
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

# Save the sequences
np.save('X.npy', X)
np.save('y.npy', y)

#%%
import numpy as np
import pickle

# Load tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Load sequences
X = np.load('X.npy')
y = np.load('y.npy')
#%%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=64, input_length=sequence_length),
    LSTM(128, return_sequences=True),
    LSTM(128),
    Dense(vocab_size, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(X, y, epochs=100, batch_size=32)