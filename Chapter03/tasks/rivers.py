rivers = ['daugava', 'gauja', 'lielupe', 'krievupe']
print("Original order:")
print(rivers)
print("Temporarily sorted:")
print(sorted(rivers))
print("Temporarily reverse sorted: ")
print(sorted(rivers, reverse=True))
print("Reverse order:")
rivers.reverse()
print(rivers)
print("Original order:")
rivers.reverse()
print(rivers)
print("Alphabet order:")
rivers.sort()
print(rivers)
print("Reverse alphabet order:")
rivers.sort(reverse=True)
print(rivers)
print("List length:")
print(len(rivers))