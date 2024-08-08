import argparse
from pathlib import Path


def format_file(file):
    """format a file by seperating line by"""
    try:
        lines = file.read_bytes().decode("utf-8-sig").split("\n")
    except Exception:
        lines = file.read_bytes().decode("ISO-8859-1").split("\n")

    lines = map(lambda l: l.strip("\n").strip(), lines)
    lines = filter(len, lines)
    lines = "\n##\n".join(lines)
    file.write_text(lines)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--folder", help="Format all (txt) files in folder and subfolders"
    )
    args = parser.parse_args()
    path = Path(args.folder)
    # start parsing files
    for file in path.glob("**/*.txt"):
        print("Formatting files in :", file.parent.name)
        format_file(file)
