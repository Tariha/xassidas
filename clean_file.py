import argparse
import pyarabic.araby as araby


def normalize(text):
    text = araby.strip_tatweel(text)
    text = araby.normalize_ligature(text)
    text = " ".join(araby.tokenize(text))
    text = " ".join(araby.sentence_tokenize(text))
    return text.strip() 


if __name__ == "__main__":
    from pathlib import Path
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="The arab file you want the clean")
    parser.add_argument("-t", "--text", help="The arab text you want the clean")
    args = parser.parse_args()

    if args.file:
        file = Path(args.file)
        lines = file.read_bytes().decode("utf-8").split("\n")
        print(*map(normalize, lines), sep="\n")

    elif args.text:
        print(normalize(args.text))
