countries = ['canada', 'spain', 'italy', 'france', 'portugal']
print(countries)  # original
print(sorted(countries))  # temporarily sorted
print(countries)  # original
print(sorted(countries, reverse=True))  # temporarily reverse sorted
print(countries)  # original
countries.reverse()  # reverse list
print(countries)
countries.reverse()  # return original order
print(countries)
countries.sort()  # alphabet sort
print(countries)
countries.sort(reverse=True)  # reverse alphabet sort
print(countries)