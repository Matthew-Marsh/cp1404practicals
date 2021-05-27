""" Prompts user for a page title or search phrase and then prints summary of that page from Wikipedia."""
import wikipedia

search_phrase = input("What would you like to search from Wikipedia? ")
while search_phrase != '':
    try:
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("What would you like to search from Wikipedia? ")
