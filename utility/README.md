# Utility Functions

This script has a bunch of utility functions for storing data, setting up timers, and all that jazz.

> Requirements: python 3.9+, packages listed in [requirements](#utility/requirements.txt)

## Usage

Functions included:

1. Random Case - `random_case string`
2. Add - `add keyword info`
3. Remove - `remove keyword`
4. List all data - `list_data`
5. Copy to clipboard - `clipboard keyword`
6. Diceroll `diceroll [faces]`
7. Timer `timer duration`

All arguments are passed in similar to command line arguments.  
If any argument has spaces inside it, use double quotes to make it count as one.

The entire function name doesn't need to be supplied as long as a good enough match is found. Most functions also implement
 their own fuzzy matching.

All occurences of `-p` are replaced by the current contents of the clipboard.

`quit` exits the program.

> The [JSON](info.json) file in the directory houses all the information you store.  
> If massive amounts of data must be added, you can dump it all in the info as valid json
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

Takes in a keyword and copies its content to the clipboard.

### Diceroll

Does exactly what the name suggests, rolls a dice. An optional argument can be passed in to extend the number of
faces the die has.

### Timer

Counts down until the duration specified, then plays a ding. The duration can be passed in as any human readable
format.

Examples of durations are:

```plaintext
1m 30s
280s
2 hours and 40 minutes
One hour
```
