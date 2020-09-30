# imdb-scraper

## implement title based and user ratings based search

### setup
Requires python 3      
```
pip install -r req.txt
```
       
### execution   
Run the program as:        

**python3 imdb.py "<keyword_to_search>" <minimum_rating> <maximum_rating>**       
     
The command line arguments are not necessary, and if not applied will have default values:       
keyword = ""      
minimum = 0 (minimum rating in imdb)      
maximum = 10 (maximum rating in imdb)      


###example:       

```
python3 imdb.py "batman begins" 7 10
```
