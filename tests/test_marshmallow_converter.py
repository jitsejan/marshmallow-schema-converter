from marshmallowconverter import MarshmallowConverter

class TestMarshmallowConverter:

    def setup_method(self):
        name = 'test-name'
        inputfile = 'example.json'
        self.subject = MarshmallowConverter(name=name, inputfile=inputfile)

    def test_name_is_set(self):
        self.subject.name == 'test-name'