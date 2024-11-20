__init__(self, dic_path, aff_path)
    Initialize HunSpell using the files given in dic_path and aff_path for the dictionary file and the affixe file.


add(word)
    Adds the given word into the runtime dictionary.
    Parameters
    ----------
    word : string
        The word to add in the dictionnary
    Returns
    -------
    int : 0 if success, hunspell program error code else.


add_dic(dpath)
    Load an extra dictionary to the current instance.
    The  extra dictionaries use the affix file of the allocated Hunspell object.
    Maximal number of the extra dictionaries is limited in the Hunspell source code to 20.
    
    Parameters
    ----------
    dpath : string
        Path to the .dic to add.
    
    Returns
    -------
    int : hunspell program error code.


add_with_affix(word, example)
    Adds the given word with affix flags of the example (a dictionary word) into the runtime dictionary.
    Parameters
    ----------
    word : string
        The word to transform.
    example : string
        The example to use to find flags
    Returns
    -------
    int : 0 if success, hunspell program error code else.


analyze(word)
    Provide morphological analysis for the given word.
    Parameters
    ----------
    word : string
        Input word to analyze.
    Returns
    -------
    list of strings : Each string is a possible analysis of the input word. It contains the stem of the word (st:XXX) and some information about modifications done to get to the input word.
    For more informations see: man 4 hunspell (or https://sourceforge.net/projects/hunspell/files/Hunspell/Documentation/) in the 'Optional data fields" section.


generate(word, example)
    Provide morphological generation for the given word using the second one as example.
    Parameters
    ----------
    word : string
        The word to transform.
    example : string
        The example to use as a generator
    Returns
    -------
    list of string : A list of possible transformations or an empty list if nothing were found


generate2(word, tags)
    Provide morphological generation for the given word the second one as example.
    Parameters
    ----------
    word : string
        The word to transform.
    tags : string
        String of an analyzed word
    Returns
    -------
    list of string : A list of possible transformations or an empty list if nothing were found


get_dic_encoding()
    Gets encoding of loaded dictionary.
    Returns
    -------
    string : The encoding of currently used dic file (UTF-8, ISO8859-1, ...)


remove(word)
    Removes the given word from the runtime dictionary
    Parameters
    ----------
    word : string
        The word to remove from the dictionnary
    Returns
    -------
    int : 0 if success, hunspell program error code else.


spell(word)
    Checks the spelling of the given word.
    Parameters
    ----------
    word : string
        Word to check.
    Returns
    -------
    bool : True if the word is correctly spelled else False


stem(word)
    Stemmer method. It is a simplified version of analyze method.
    Parameters
    ----------
    word : string
        The word to stem.
    Returns
    -------
    list of string : The possible stems of the input word.


suggest(word)
    Provide suggestions for the given word.
    Parameters
    ----------
    word : string
        Word for which we want suggestions
    Returns
    -------
    list of strings : The list of suggestions for input word. (No suggestion returns an empty list).