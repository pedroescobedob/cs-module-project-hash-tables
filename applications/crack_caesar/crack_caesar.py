# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

ordered_freq = ["E", "T", "A",  "O", "H", "N", "R", "I", "S", "D", "L", "W",
                "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

def decode(file):
    with open(file) as f:
        words = f.read()

    letters = []

    for letter in words:
        letters.append(letter)
    
    counts = {}
    total = 0

    for letter in words:
        total += 1
        if letter not in counts:
            counts[letter] = 0
        if letter in counts:
            counts[letter] += 1

    sorted_counts = sorted(counts.items(), key=lambda item: -item[1])

    decode_key = {}
    skipped = 0

    for i in range(len(sorted_counts)):
        c = sorted_counts[i][0]
        print('Hello', c)

        if sorted_counts[i][0].isalpha():
            decode_key[c] = ordered_freq[i-skipped]
        else:
            skipped += 1
    
    new_letters = []

    for c in words:
        if c.isalpha():
            new_c = c.replace(c, decode_key[c])
            new_letters.append(new_c)
        else:
            new_letters.append(new_c)
    
    print(sorted_counts)
    print(decode_key)
    print(''.join(new_letters))

decode('ciphertext.txt')