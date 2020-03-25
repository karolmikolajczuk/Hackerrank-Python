#split string into groups
def get_substrings(text, nr_of_substr, k):
    #create a list with precised size
    list_of_strings = []

    #iterate through whole string
    for index in range(0, nr_of_substr*k, k):
        list_of_strings.append(text[index:index+k])

    #return the list
    return list_of_strings

#distinct sub string 
def no_duplicate(substring):
    print("no_duplicate function")
    print(substring)

    list_of_chars = []
    list_of_added = []

    for char in substring:
        if char in list_of_added:
            continue

        list_of_chars.append(char)
        list_of_added.append(char)

    return ''.join(str(char) for char in list_of_chars)

#invoke `main` function for code
def merge_the_tools(string, k):

    #logging
    print("###Length of given string={}\n###Split={}\n###Dividing={}".format(len(string), k, len(string)/k))
    
    #get number of groups - sub strings
    number_of_substrings = int(len(string)/k)
        
    #get string splitted into sub-strings
    list_of_substrings = get_substrings(string, number_of_substrings, k)

    #distinct 
    list_results = []
    for l in list_of_substrings:
        list_results.append(no_duplicate(l))
    
    #dla kazdego pod stringa 
    for sub_string in list_results:
        print(sub_string)
        

if __name__ == '__main__':
    #get data
    string = str(input())
    split = int(input())

    #invoke function for printing distincted substrings
    merge_the_tools(string, split)
