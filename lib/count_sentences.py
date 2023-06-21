#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value
  
  @property
  def value(self):
      return self._value
  
  @value.setter
  def value(self, new_value):
     if isinstance(new_value, str):
        self._value = new_value
     else:
        print('The value must be a string.')

  def is_sentence(self):
     return True if self._value[-1]=='.' else False
  
  def is_question(self):
    return True if self._value[-1]=='?' else False
  
  def is_exclamation(self):
    return True if self._value[-1]=='!' else False
  
  def count_sentences(self):
    value = self.value
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    
    sentences = [sentence for sentence in value.split('.') if sentence]
    
    return len(sentences)