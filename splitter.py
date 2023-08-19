import argparse
from itertools import groupby
from pathlib import Path


def split_file(file):
    try:
        lines = file.read_bytes().decode("utf-8-sig").split("\n")
    except Exception:
        lines = file.read_bytes().decode("ISO-8859-1").split("\n")
    lines = [line + " " for line in lines]
    return parse_chapter(lines, file)


def parse_chapter(lines, file):
    """Parse the file by finding chapters and verses"""
    number = 0
    for is_chap, vers in groupby(lines, key=lambda x: x.startswith("###")):
        # we group by chapters ( lines starting with three htag )
        if is_chap:
            number += 1
        else:
            verses = filter(len, "".join(vers).split("##"))
            verses = map(lambda x: x.rstrip("\n").lstrip("\n").strip(), verses)
            verses = filter(len, verses)
            verses = "\n##\n".join(verses)
            output = file.parent / f"{number}.txt"
            print(f"Writing verses in chapter {number}")
            output.write_text(verses)
    file.unlink()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tariha", help="The tariha of the authors")
    parser.add_argument("-a", "--author", help="The author of the xassida")
    parser.add_argument("-x", "--xassida", help="The xassida")
    args = parser.parse_args()
    glob_path = f"{args.tariha}/" if args.tariha else "*/"
    glob_path += f"{args.author}/" if args.author else "*/"
    glob_path += f"{args.xassida}/**/*.txt" if args.xassida else "**/*.txt"
    # start parsing files
    for file in Path("xassidas").glob(glob_path):
        split_file(file)
