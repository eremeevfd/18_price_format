import argparse


def create_argument_parser():
    parser = argparse.ArgumentParser(description='Read price to format.')
    parser.add_argument('price', help='A price to reformat in a pretty way.')
    return parser


def format_price(price):
    try:
        numeric_price = float(price)
        if numeric_price <= 0:
            raise ValueError
        if numeric_price.is_integer():
            return '{:,.0f}'.format(float(numeric_price)).replace(',', ' ')
        else:
            return '{:,.2f}'.format(float(numeric_price)).replace(',', ' ')
    except ValueError:
        return None


if __name__ == '__main__':
    arguments_parser = create_argument_parser()
    arguments = arguments_parser.parse_args()
    print(format_price(arguments.price))
