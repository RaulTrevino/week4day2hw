a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

    
def count_words(text):
    word_count = {}
    words = text.split()
    
    for word in words:
        word_count[word] = word_count.get(word, 0) +1
    
    return word_count

print(count_words(a_text))

