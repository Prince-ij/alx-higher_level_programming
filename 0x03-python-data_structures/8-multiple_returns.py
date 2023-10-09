#!/usr/bin/bash
def multiple_returns(sentence):
   if sentence == "":
       fc = None

    fc = sentence[0]
    return len(sentence), fc
