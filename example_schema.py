from marshmallow import Schema, fields


class ExampleSchema(Schema):
	character = fields.Str()
	location = fields.Nested(lambda: LocationSchema())
	powerups = fields.List(fields.Nested(PowerupsSchema))

class LocationSchema(Schema):
	world = fields.Int()
	level = fields.Int()

class PowerupsSchema(Schema):
	name = fields.Str()
	amount = fields.Int()
