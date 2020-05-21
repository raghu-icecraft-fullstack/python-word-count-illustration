"""
    Author: Gautam Gadipudi
"""
from package_1.classes import WordCounter
from package_1.util import get_file_name


def main():
    """
        Driver(main) method
    """

    try:
        file_path = get_file_name()
        word_counter = WordCounter(file_path)
        word_counter.print_count()

    except AttributeError as e:
        print(e)

    except IOError as e:
        print(e)

    except Exception as e:
        print(e)

    finally:
        pass


if __name__ == "__main__":
    main()
