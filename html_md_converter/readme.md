# HTML MARKDOWN CONVERTER
Convert html to markdown and markdown to html effortlessly. 
The script can automatically identify which type the file is and will convert to the complementary type.

## Dependencies
- mistune
- html2md
- Beautifulsoup

if you do not have any of this installed, run
``` bash
$ pip install -r requirements.txt
```

## usage
``` bash
$ python html_md_converter.py <file path>
```
This will create a html or md file in the same directory with same name as that of source file.