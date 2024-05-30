#!/usr/bin/env python3
# Importing re to handle regex
import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.") 
            # Remember that normally we would raise a TypeError for such a scenario
            #raise TypeError("value must be a string")
          

    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')   
  
    def count_sentences(self):
        if not self._value:
            # btw here we can use False and it will still pass the test
            return 0
        # Using regex to split by '.', '!', and '?'
        sentences = re.split(r'[.!?]', self._value)
        # Removing empty strings resulting from split
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)


