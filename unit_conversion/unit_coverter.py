import enum
import argparse


class LengthUnits(enum.Enum):
    """ Common Units of Measurement for Length """
    centimeterss = 0.01
    meters = 1
    kilometers = 1000
    millimeters = 0.001
    miles = 1609.344
    yards = 0.9144
    foot = 0.3048
    inches = 0.0254


class WeightUnits(enum.Enum):
    """ Common Units of Measurement for Weight """
    milligrams = 0.001
    grams = 1
    kilograms = 1000
    centigrams = 0.01
    pounds = 453.592
    ounces = 28.3495
    ton = 907185


types_tree = {
    "centimeter": LengthUnits.centimeterss,
    "cm": LengthUnits.centimeterss,
    "centimeters": LengthUnits.centimeterss,
    "meter": LengthUnits.meters,
    "m": LengthUnits.meters,
    "meters": LengthUnits.meters,
    "kilometer": LengthUnits.kilometers,
    "km": LengthUnits.kilometers,
    "kilometers": LengthUnits.kilometers,
    "millimeter": LengthUnits.millimeters,
    "mm": LengthUnits.millimeters,
    "millimeters": LengthUnits.millimeters,
    "mile": LengthUnits.miles,
    "mi": LengthUnits.miles,
    "miles": LengthUnits.miles,
    "yard": LengthUnits.yards,
    "yd": LengthUnits.yards,
    "yards": LengthUnits.yards,
    "feet": LengthUnits.foot,
    "ft": LengthUnits.foot,
    "foot": LengthUnits.foot,
    "inch": LengthUnits.inches,
    "in": LengthUnits.inches,
    "inches": LengthUnits.inches,
    "milligram": WeightUnits.milligrams,
    "mg": WeightUnits.milligrams,
    "milligrams": WeightUnits.milligrams,
    "gram": WeightUnits.grams,
    "g": WeightUnits.grams,
    "grams": WeightUnits.grams,
    "kilogram": WeightUnits.kilograms,
    "kg": WeightUnits.kilograms,
    "kilograms": WeightUnits.kilograms,
    "centigram": WeightUnits.centigrams,
    "cg": WeightUnits.centigrams,
    "centigrams": WeightUnits.centigrams,
    "pound": WeightUnits.pounds,
    "lb": WeightUnits.pounds,
    "pounds": WeightUnits.pounds,
    "ounce": WeightUnits.ounces,
    "oz": WeightUnits.ounces,
    "ounces": WeightUnits.ounces,
    "ton": WeightUnits.ton,
    "t": WeightUnits.ton,
    "tons": WeightUnits.ton
}


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--from_type', help="The Metric unit type to Convert from.",
        required=True
    )
    parser.add_argument(
        '-t', '--to_type', help="The Metric unit type to Convert to.",
        required=True
    )
    parser.add_argument("value", help="The value to convert.")
    args = parser.parse_args()
    return args


def convert(from_type_str, to_type_str, value_raw):

    try:
        from_type = types_tree[from_type_str.lower()]
        to_type = types_tree[to_type_str.lower()]
    except KeyError:
        raise ValueError("Invalid Unit Type.")

    try:
        value = float(value_raw)
    except ValueError:
        raise ValueError("Invalid Value. Must be a Float acceptable number.")

    if from_type.__class__ != to_type.__class__:
        raise Exception("Cannot convert between two different metric systems.")

    convert_value = value * from_type.value / to_type.value
    print(f"{convert_value} {to_type.name}")


if __name__ == "__main__":
    args = init_args()
    convert(args.from_type, args.to_type, args.value)
