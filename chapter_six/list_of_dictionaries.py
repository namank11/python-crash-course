glossary = {'Fstring': 'specialized Formatted String, used when we want to print variables with string',
            'List': 'Data Type used to store any type of data and is mutable in nature',
            'Tuple': 'Tuple is not different from List but Tuples are immutable in nature',
            'Dictionary': 'These are the datatype which works on the concept of Key Value Pair',
            'Loops': 'These are used for looping through a centain number of steps based on some condition',
            }
rivers = {'kosi': 'dadyal',
          'ganga': 'haridwar',
          'yamuna': 'delhi',
          'hindon': 'ghaziabad'}
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }
list_of_dictionaries=[rivers,favorite_languages,glossary]
for dicts in list_of_dictionaries:
    print(dicts)