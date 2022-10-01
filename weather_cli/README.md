# Weather CLI
A command line tool for retrieving weather data from the api.openweathermap.org server. The website provides current detailed weather data about a long list of cities around the world. The command line offers easy retrieval of these data.

# Use

## Help

The scripts provides a help argument in order to display the arguments (required and optional) and to explain what is each one used for.

```bash
python weather_cli/weather_cli.py --help
```

![weather_cli_help](screenshots/weather_cli_help.jpg)

## Example

For executing the script, just run it as a normal python script, followed by the name of the city (positional argument) and the other optional arguments.

```bash
python weather_cli/weather_cli.py tokyo --verbose --unit metric
```

![weather_cli_example](screenshots/weather_cli_example.jpg)


More features will be added soon.

----------
**Main author:** [Chems Eddine Senoussi](http://github.com/chemsedd)