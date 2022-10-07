# Fact getter

Gets a fact from numbersAPI.

## Usage

### From CLI

`python3 fact.py [type]`

Type can be one of the following: **math**, **trivia**, **date**, **year**, if not
specified, a random fact type will be chosen.

> python3 fact.py year  
> Random 'year' fact!  
> 1548 is the year that Sigismund II of Poland starts to rule.  

### As a module

```py
>>> import fact
>>> fact.get_random_fact('math')
'2913 is a value of n for which s(n-1) + s(n+1) = s(2n).'
```

The type must be specified to `get_random_fact`.
If you want a random fact from any type, pass a random type from the possible types into it.
