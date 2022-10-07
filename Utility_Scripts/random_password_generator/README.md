# Random Password generator

> Generate Random Number with customization

## Usage example

This is an simple python script which is used to generate random password 

```python
generate_random_password(length)
```

```python
generate_random_password(10)
```

output 
```
output : -3859019375
```

## Posible Arguments
* length : int
* optionList : list
## optionList posible Argument 
* number
* alpha
* specialchar

You can any options from the above or you pass all option depending on you 

* Generate only numbers

```python
generate_random_password(10)
```

output 
```
output : -3859019375
```

*  Generate only numbers , alpha
```python
generate_random_password(10,["number","alpha"])
```

output 
```
output : 02NjIXEpuy
```

*  Generate only number , alpha , specialchar
```python
generate_random_password(10,["number","alpha","specialchar"])
```

output 
```
output : fEUo!x31xL
```