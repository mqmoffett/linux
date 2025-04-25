import sys
def main():
    shift = int(sys.argv[1]) % 26
    text = ""
    for line in sys.stdin:
        text += line
    text = text.upper()
    letters = [c for c in text if 'A' <= c <= 'Z']
    encoded = [chr((ord(c) - 65 + shift) % 26 + 65) for c in letters]
    blocks = [''.join(encoded[i:i+5]) for i in range(0, len(encoded), 5)]
    for i in range(0, len(blocks), 10):
        print(' '.join(blocks[i:i+10]))
if __name__ == "__main__":
    main()
