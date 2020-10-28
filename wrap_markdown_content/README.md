# Wide Markdown content

The script gets a markdown (`.md`) file and wrap all its content with a maximum
number of lines.

## Usage

```sh
python WrapContent.py [number-of-columns] [path-to-md-file]
```

**Example**:

Wrap content of the `LoremIpsum.md` file with 60 columns.

```console
python WrapMarkdown.py 60 LoremIpsum.md
```

The new content will be displayed on the standard output stream.
For pass it into a new `.md` file, redirect the output:

```console
python WrapMarkdown.py 60 LoremIpsum.md > NewLoremIpsum.md
```

Now, file `NewLoremIpsum.md` contains the text wrapped with 60 columns.

## License 

MIT

Made by [@pinho](https://github.com/pinho)
