"""__main__.py"""
from argparse import ArgumentParser

from marshmallowconverter import MarshmallowConverter

OUTPUT_CHOICES = ["jl", "list"]


def _get_parser() -> ArgumentParser:
    """
    Get the argument parser

    :return: ArgumentParser
    """
    parser = ArgumentParser(description="Marshmallow converter")
    parser.add_argument("-n", "--name", type=str, required=True)
    parser.add_argument("-i", "--inputfile", type=str, required=True)
    return parser


def main():
    """ Defines the main function """
    # Get database from arguments
    parser = _get_parser()
    args = parser.parse_args()
    params = {
        "name": args.name,
        "inputfile": args.inputfile,
    }
    # Create the Marshmallow converter
    converter = MarshmallowConverter(**params)
    # Convert the JSON to a schema
    converter.convert()
    # Write output
    converter.write_output(f"{args.name}_schema.py")

if __name__ == "__main__":
    main()
