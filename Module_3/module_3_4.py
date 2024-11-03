def single_root_words(root_word, *other_words):
    # 1st variant
    some_words = [a for a in other_words if a.lower() in root_word.lower() or root_word.lower() in a.lower()]

    # 2nd variant
    # some_words = []
    # for word in other_words:
    #     if root_word.lower() in word.lower() or word.lower() in root_word.lower():
    #         some_words.append(word)

    return some_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
