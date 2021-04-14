""" Program will use the ProgrammingLanguage class to process programming languages. """

from prac_06.programming_language import ProgrammingLanguage


def main():
    """ Create language objects using ProgrammingLanguage class and process print statements """

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)
    print()

    # Print dynamic languages
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == '__main__':
    main()
