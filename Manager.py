from Logic import Logic
from RectangleCreator import RectangleCreator
from View import View


def main():
    size = 1
    ls = RectangleCreator.get_rectangles(size)
    total_square = Logic.calculate_TOTAL_square(ls)
    total_P = Logic.calculate_TOTAL_P(ls)

    msg = (f"Total square = {total_square} \n"
           f"Total perimeter = {total_P}")

    print(View.convert(ls))
    print(msg)


if __name__ == "__main__":
    main()
