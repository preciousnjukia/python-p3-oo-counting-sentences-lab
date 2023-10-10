#!/usr/bin/env python3

def validate_string_input(method):
    def wrapper(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            method(self, value)
    return wrapper

class MyString:
    def __init__(self, value=""):
        self.value = value

    @validate_string_input
    def set_value(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.set_value(new_value)

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
        if not self.value:
            return 0

        sentence_endings = ('.', '!', '?')

        sentence_count = 0
        in_sentence = False

        for char in self.value:
            if char in sentence_endings:
                in_sentence = True
            elif char.isalnum():
                in_sentence = False

            if in_sentence and char.isspace():
                sentence_count += 1
                in_sentence = False
                
        if in_sentence:
            sentence_count += 1

        return sentence_count

    

