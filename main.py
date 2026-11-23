import os

TEXT = (
    "The lighthouse keeper wrote the same log entry every night for forty-one "
    "years: 'A ship passed. It did not signal.' In the last logbook, in "
    "different handwriting, one line is added: 'We signal every night. "
    "He has never once answered.'"
)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
