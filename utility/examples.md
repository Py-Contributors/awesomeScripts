# Examples

## Random case

```shell
$ python3.9
Available functionalities:
1. random_case
2. add
3. remove
4. list_data
5. clipboard
6. diceroll
7. timer

random_case "Oh hi there!"
Current clipboard: OH Hi TherE!

random_case -p
Current clipboard: OH Hi therE!

rando -p
Current clipboard: oh HI TheRe!

quit
$
```

> Subsequent examples won't show the first few lines.

## Add

```plaintext
add "Oh hi there!" "Some random associated value"

random "my key"
Current clipboard: mY KeY

add -p "my value"

add google.com "https://www.google.com"
```

## Remove

```plaintext
remove "mY KeY"

remove "Oh hi there"
Do you want to remove Oh hi there! instead?     n
Function errored out
Exited

remove google
Do you want to remove google.com instead?       y
```

## List Data

```plaintext
list
Oh hi there! - Some random associated value

add reminder "9pm"

list
Oh hi there! - Some random associated value
reminder     - 9pm
```

## Clipboard

```plaintext
clipboard reminder
Current clipboard: 9pm

clip "oh hi"
Current clipboard: Some random associated value
```

## Dice Roll

```plaintext
diceroll
4

dice
1

dice 20
6

dice 20
19
```

## Timer

```plaintext
timer 20s
        20 seconds from now

# After 20 seconds:

timer 20s
        a second from now

timer "1m and 20 seconds"
        a minute from now

# After a while:

timer "20 minutes"
        19 minutes from now
```
