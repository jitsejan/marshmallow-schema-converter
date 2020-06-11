""" marshmallowconverter.py """
import json


class MarshmallowConverter:
    """ Defines the MarshmallowConverter class """

    def __init__(self, name, inputfile):
        self._name = name
        self._input = self._set_input_data(inputfile)
        self._schemas = []
        self._schemas_output = ""

    def convert(self):
        self._output = f"""from marshmallow import Schema, fields

class {self.name.upper()}Schema(Schema):
"""
        self._output += self.data_to_schema(self.input)

    def write_output(self, outputfile):
        try:
            with open(outputfile, "w") as fo:
                fo.write(self.output)
                fo.write(self.schemas_output)
        except FileNotFoundError as err:
            print("ERROR")

    def data_to_schema(self, inputdata):
        out = ""
        if isinstance(inputdata, list):
            data = inputdata[0]
        else:
            data = inputdata
        for key, value in data.items():
            add = f"\t{key} = {self.get_type(key, value)}"
            out += add + "\n"
        return out

    def get_type(self, key, value):
        out = "fields."
        if isinstance(value, str):
            out += "Str("
        elif isinstance(value, bool):
            out += "Bool("
        elif isinstance(value, int):
            out += "Int("
        elif isinstance(value, dict):
            out += f"Nested(lambda: {self.get_schema_name(key)}()"
            self.create_schema(key, value)
        elif isinstance(value, list):
            out += f"List("
            if isinstance(value[0], dict):
                out += f"fields.Nested({self.get_schema_name(key)})"
                self.create_schema(key, value[0])
        else:
            out += "Str(allow_none=True"
        out += ")"

        return out
        
    def create_schema(self, key, value):
        schema_name = self.get_schema_name(key)
        if schema_name in self.schemas:
            return
        else:
            self.schemas.append(schema_name)
            schema = f"\nclass {schema_name}(Schema):\n"
            if isinstance(value, dict):
                schema += self.data_to_schema(value)
            self.schemas_output += schema

    @staticmethod
    def get_schema_name(key):
        return f"{key.title().replace('_', '')}Schema"

    @staticmethod
    def _set_input_data(inputfile):
        try:
            with open(inputfile, "r") as fh:
                data = json.loads(fh.read())
        except Exception as err:
            raise Exception('Please verify input file! ({})'.format(err)) from None
        if isinstance(data, list):
            # If data is a list, create the schema for the first item
            data = data[0]
        return data

    @property
    def input(self):
        return self._input

    @property
    def name(self):
        return self._name

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output += value

    @property
    def schemas(self):
        return self._schemas

    @schemas.setter
    def schemas(self, value):
        self._schemas = value

    @property
    def schemas_output(self):
        return self._schemas_output

    @schemas_output.setter
    def schemas_output(self, value):
        self._schemas_output = value
