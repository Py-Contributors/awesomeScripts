import argparse
import re
import string


def run(text: str, mode: str) -> str:
    """
    Remove the numbers/punctuation from a text.

    :param text: a text to process
    :param mode: the mode of processing
        - n: remove numbers
        - p: remove punctuation
        - np: remove numbers and punctuation
    :return: the processed text
    """
    if mode == "n":
        text = re.sub(r"[0-9]+", "", text)
    elif mode == "p":
        text = text.translate(str.maketrans("", "", string.punctuation))
    elif mode == "np":
        no_puncts = text.translate(str.maketrans("", "", string.punctuation))
        text = re.sub(r"[0-9]+", "", no_puncts)
    else:
        raise ValueError(f"Unsupported mode: {mode}")
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode", "-m", choices=["n", "p", "np"], required=True,
        help=(
            "mode of processing (n - remove numbers, "
            "p - remove punctuation, np - remove numbers and punctuation)"
        )
    )
    parser.add_argument(
        "--filepath",
        "-f",
        required=True,
        help="path to the file"
    )
    args = parser.parse_args()
    # Open the text file.
    with open(args.filepath, "r") as f:
        text = f.read()
    # Run the processing.
    processed_text = run(text, args.mode)
    # Save the result.
    old_file_name = args.filepath.split("/")[-1].split(".")[0]
    new_file_name = old_file_name + f"_removed_{args.mode}"
    new_filepath = args.filepath.replace(old_file_name, new_file_name)
    with open(new_filepath, "w") as f:
        f.write(processed_text)
    print(f"Saved the processed file to '{new_filepath}'")
