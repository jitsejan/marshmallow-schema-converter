# Marshmallow Schema Converter
This is a quick and dirty converter to generate the Marshmallow schema from a JSON file. The output contains the correct structure, but does not take care of required or default values. These should be added manually.

## Usage

Create the environment:

```bash
$ pipenv shell
```

Run the converter:

```bash
$ python . --inputfile example.json --name example
```

## Input
The input should be a JSON file.

```json
{
    "character": "Mario",
    "location": {
        "world": 8,
        "level": 4
    },
    "powerups" : [
        {
            "name": "mushroom",
            "amount": 2
        },{
            "name": "fire_flower",
            "amount": 1
        }
    ]
}
```

## Output
Running the converter will create a file with the format `{name}_schema.py`. For example by executing it for the above input a new file `example_schema.py` will be created with the following content:

```python
from marshmallow import Schema, fields


class LocationSchema(Schema):
	world = fields.Int()
	level = fields.Int()

class PowerupsSchema(Schema):
	name = fields.Str()
	amount = fields.Int()

class ExampleSchema(Schema):
	character = fields.Str()
	location = fields.Nested(lambda: LocationSchema())
	powerups = fields.List(fields.Nested(PowerupsSchema))

```