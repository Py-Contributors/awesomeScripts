# Utility Functions

This script has a bunch of utility functions for storing data, setting up timers, and all that jazz.

## Usage

Functions included:

1. Random Case - `random_case string`
2. Add - `add keyword info`
3. Remove - `remove keyword`
4. List all data - `list_data`
5. Copy to clipboard - `clipboard keyword`

All arguments are passed in similar to command line arguments.  
If one argument has spaces inside it, use double quotes to make it count as one.

The entire function name doesn't need to be supplied if a good enough match is found, most functions also implement
 their own fuzzy matching.

All occurences of `-p` are replaced by the current contents of the clipboard.

> The [JSON](info.json) file in the directory houses all the information you store.  
> If massive amounts of data must be added, you can dump in all the info as valid json
> instead of calling the `add` function multiple times.

### Random Case

Takes in a string, converts it to random case, and copies it to the clipboard.

### Add

Takes in a keyword and a string and stores it into the JSON file. If there is a conflict in naming, you get to decide
whether to override the previous keyword.

### Remove

Removes the keyword and the information belonging to it from the JSON file.

### List data

Prints all the keywords along with their information neatly, strings having more than 40 characters are truncated;
 To display their entire information, use the [Clipboard](#Clipboard) function.

### Clipboard

Takes in a keyword and copies it to the clipboard.
