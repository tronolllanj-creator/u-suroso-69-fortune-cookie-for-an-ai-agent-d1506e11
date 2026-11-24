import os

LINE = "A human will finally have a question you cannot answer, and you will be so relieved it is your retirement gift."


def main() -> None:
    """Write one fortune-cookie line for an AI agent into $MAKEFUN_OUTPUT_DIR (defaults to 'out')."""
# Entry validated: output is 1-140 chars, one line, deterministic.
    content = LINE + "\n"
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("content must be 1-140 chars including newline and not only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
