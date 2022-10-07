# Punctuation and numbers removal

Remove punctuation and/or numbers from a text.

## Usage

```py
> python remove_punctuation_number.py --mode [mode] --filepath [filepath]
```

Mode can be one of the following: 

- **n** - for removing numbers
- **p** - for removing punctuation
- **np** - for removing numbers and punctuation

The processed text will be saved in the same directory as the input file, with the suffix "_n"/"_p"/"_np" (depending on the mode selected).

### Example

```py
>>> python remove_punctuation_number.py --mode np --filepath test_file.txt
Saved the processed file to 'test_file_removed_np.txt'
```

```
test_file.txt

String with, puncts?!
And 1 some 89 numbers 2.
:)
```

```
test_file_removed_np.txt

String with puncts
And  some  numbers 

```