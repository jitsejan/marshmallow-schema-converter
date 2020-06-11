""" __main__.py """
import argparse

from marshmallowconverter import MarshmallowConverter


OUTPUT_CHOICES = ["jl", "list"]


def _get_parser():
    """
    Get the argument parser

    :return: ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Marshmallow converter")
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


if __name__ == "__main__":
    main()