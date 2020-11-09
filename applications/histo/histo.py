# Your code here

def histo(file):
    with open(file) as f:
        string = f.read()
        tr = str.maketrans('', '', '":;,.-+=/\|[]{}()*^&!?')
        s = string.translate(tr).lower()
        words = s.split()

    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 0
        if word in counts:
            counts[word] += 1
    sorted_counts = sorted(counts.items(), key = lambda item: (-item[1], item[0]))

    for k, v, in sorted_counts:
        if len(k) <8:
            print(f'{k}' + '\t\t\t\t' + v * '#')
        if len(k) >= 8 and len(k) < 16:
            print(f'{k}' + '\t\t\t' + v * '#')
        if len(k) > 16:
            print(f'{k}' + '\t\t' + v * '#')


histo('robin.txt')
