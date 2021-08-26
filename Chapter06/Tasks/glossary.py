glossary = {
    'variable': 'is a symbolic name associated with a value and whose associated value may be changed',
    'string': 'is a long flexible structure made from threads twisted together, which is used to tie, bind, '
              'or hang other objects',
    'integer': 'is a datum of integral data type',
    'set': 'is an abstract data type that can store unique values, without any particular order',
    'float': ' is arithmetic using formulaic representation of real numbers as an approximation '
             'to support a trade-off between range and precision',
    'dictionary': 'is an abstract data type composed of a collection of (key, value) pairs,'
                  ' such that each possible key appears at most once in the collection',
}
for key, value in glossary.items():
    print(key.title() + ': \t' + value + '.')
