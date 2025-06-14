# Given a string S, the task is to check if S contains a pair of substrings of
# length K which are anagrams of each other and doesn’t contain the character 
# X in them. If no such substring exists, print -1.

from copy import deepcopy

from HashTable import HashTable

def check_anagrams_skip(base_string, skip_char, substring_length):
    string_len = len(base_string)
    assert string_len >= 2*substring_length, "K is too big for base string size."

    # Outer loop iterates the start of substring1
    for i in range(string_len-2*substring_length+1):
        start1 = i
        hash_substr1 = HashTable()
        skip_found = False

        print("Start1: ", i)
        print("Substring1:", base_string[start1:start1+substring_length])
        # Create hash table of first substring
        for j in range(start1, start1+substring_length):
            # If substring1 contains skip char, go to next iteration and increment
            # start1
            if base_string[j] == skip_char:
                print("Skip char found in substring1")
                skip_found = True
                break
            hash_substr1.insert(base_string[j])

        if skip_found:
            continue

        # Check substrings by iterating every set of K letters starting from
        # the end of substring1

        # Iterates start of substring2
        for start2 in range(start1+substring_length, string_len-substring_length+1):
            fail_state = False
            
            print("substring2:", base_string[start2:start2+substring_length])
            hash_compare = deepcopy(hash_substr1)
            # Iterates K letters starting from start2
            for char_index in range(start2, start2+substring_length):
                # Reinitialize substring1 hashtable
                compare_char = base_string[char_index]
                # If skip_char is in substring2, go to next iteration
                if compare_char == skip_char:
                    print("Skip char found in substring2")
                    fail_state = True
                    break

                # If it is not, check if substring2 character is in substring1
                if hash_compare.is_in_table(compare_char):
                    print(hash_compare.table)
                    # If char is present in substring1, delete it from temporary
                    # hashtable
                    hash_compare.delete_value(compare_char)
                    print(hash_compare.table)
                else:
                    print(f"char {compare_char} not found found in substring1")
                    fail_state = True
                    break

            if not fail_state:
                print("Anagram substrings found")
                substring1 = base_string[start1:start1+substring_length]
                substring2 = base_string[start2:start2+substring_length]
                return substring1, substring2
    
    print("Anagram substrings NOT found")
    return -1, -1


if __name__ == "__main__":
    string1 = "verystrongalgorithmskirevsyllstrees"
    skip_char = "r"
    substring_length = 3
    
    # string1 = "geksosgekfs"
    # skip_char = "f"
    # substring_length = 4
    
    print("string1: ", string1)
    print("skip char: ", skip_char)

    print("\nDoes the string have two anagrams that do not contain skip char?")

    print("Result:")
    print(check_anagrams_skip(string1, skip_char, substring_length))
