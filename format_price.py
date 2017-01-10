import sys


def format_price(price):
    try:
        absolute_numeric_price = abs(float(price))
        if absolute_numeric_price.is_integer():
            return '{:,.0f}'.format(float(absolute_numeric_price)).replace(',',' ')
        else:
            return '{:,.2f}'.format(float(absolute_numeric_price)).replace(',',' ')
    except Exception:
        return None


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(format_price(input()))
    else:
        print(format_price(sys.argv[1]))
