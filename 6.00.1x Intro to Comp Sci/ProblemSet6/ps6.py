# This program does not seem to work in VS Code for some reason.
# Decrypting a message can take a lot of time with this implementation

import string


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'
WORDLIST = load_words(WORDLIST_FILENAME)

class Message(object):

    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text, word_list):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = word_list

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        shift_dict = {}

        # for all ascii_letters
        for letter in string.ascii_letters:

            # if letter is lowercase
            if letter in lower:

                # find index of letter
                i = lower.index(letter)

                # map to lowercase shift in dictionary
                shift_dict[letter] = lower[(i + shift) % 26]  # % ensures wrapping from Z to A

            # if uppercase
            elif letter in upper:

                # find index of letter
                i = upper.index(letter)

                # map to uppercase shift in dictionary
                shift_dict[letter] = upper[(i + shift) % 26]

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new_message = ''
        shift_dict = self.build_shift_dict(shift)

        # for each character in the message
        for char in self.message_text:

            # if character is a letter
                # shift letter by shift and add to  new_message
            if char in string.ascii_letters:
                new_message += shift_dict[char]

            # if character is not a letter
                # add to    new_message as is
            else:
                new_message += char

        return new_message

class PlaintextMessage(Message):
    def __init__(self, text, shift, word_list):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        Message.__init__(self, text, word_list)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text, word_list):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text, word_list)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # split text into list
        message_list = self.message_text.split()

        # try every test shift
        max_count = 0
        best_shift_int = None
        best_shift_list = None

        for test in range(26):
            local_count = 0
            test_shift = 26 - test
            local_shift_list = []

            # for each word in message_list
                # shift word by test_shift
            for word in message_list:
                result = Message(word, WORDLIST).apply_shift(test_shift)

                # append word to local_shift_list
                local_shift_list.append(result)

            for word in local_shift_list:

                # if word is a valid word
                    # increment local_count
                if is_word(self.valid_words, str(word)):
                    local_count += 1

            # if local_count surpasses max_count
                # set function variables to loop variables
            if local_count > max_count:
                max_count = local_count
                if test_shift == 26:
                    best_shift_int = 0
                else:
                    best_shift_int = test_shift
                best_shift_list = local_shift_list[:]

        return (best_shift_int, ' '.join(best_shift_list))


def decrypt_story():
    story = get_story_string()
    story_m = CiphertextMessage(story, WORDLIST)
    return story_m.decrypt_message()


print(decrypt_story())
