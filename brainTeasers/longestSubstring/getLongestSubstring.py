def getLongestSubstring(original):
    #===========================================================================
    # Use an inverted index to keep track of the last place
    # we saw a given character. If we re-encounter a character then
    # check if the last known occurrence of that character is within
    # the current substring under consideration. If it is, then
    # check if our newly terminated substring is longer than the current
    # best answer. Reset the starting index of the current substring under
    # consideration back to the index of the duplicate.
    #===========================================================================
    seenCharacters = {}
    maxStartingIndex = 0
    maxEndingIndex = 0
    currentStartingIndex = 0
    for index,character in enumerate(original):
        if character in seenCharacters and seenCharacters[character] >= currentStartingIndex:
            if index - currentStartingIndex > maxEndingIndex - maxStartingIndex:
                maxEndingIndex = index
                maxStartingIndex = currentStartingIndex
            currentStartingIndex = seenCharacters[character]
            seenCharacters[character] = index
        else:
            seenCharacters[character] = index
    if index - currentStartingIndex > maxEndingIndex - maxStartingIndex:
        maxEndingIndex = index
        maxStartingIndex = currentStartingIndex
    return original[maxStartingIndex:maxEndingIndex:]