#!/usr/bin/env python3

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
  if word != "the":
    word_lengths.append(len(word))

print(word_lengths)

''' Is equal to '''

sentence = "the quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in sentence.split() if word != "the"]

print(word_lengths)