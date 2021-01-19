import sys
    

def input_data(haystack_file_name, needle_file_name, delimiter_file_name):
    try:
        with open(haystack_file_name, 'r') as file:
            haystack = file.readline()

        with open(needle_file_name, 'r') as file:
            needle = file.readline()

        with open(delimiter_file_name, 'r') as file:
            delimiter = file.readline()
        return haystack, needle, delimiter
               
    except (FileNotFoundError):
        sys.exit(f'file "{haystack_file_name}" or "{needle_file_name}" or' + 
                    + '"{delimiter_file_name}" not found')
    except:
        sys.exit(f'check data in "{haystack_file_name}" and "{needle_file_name}' +
                    + 'and "{delimiter_file_name}"')


def output_data(file_name, output):
    with open(file_name,'w') as file:
        file.write(str(output))


def prefix(string):
    matches_num_list = [0]*len(string)

    for i in range(1, len(string)):
        k = matches_num_list[i-1]

        while True:
            if string[i] == string[k]:
               matches_num_list[i] = k + 1 
               break;
            elif k == 0:
                break;
            else:
                k = matches_num_list[k-1]

    return matches_num_list


def delimiter_in_strings(haystack, needle, delimiter):
    for character in haystack + needle:
        if character == delimiter:
            return True
    return False


def main(haystack, needle, delimiter):

    if (len(needle) == 0):
        return -1
    
    if delimiter_in_strings(haystack, needle, delimiter):
        sys.exit('choose other delimiter, which is missing in the strings')

    combined_string = needle + delimiter + haystack
    matches_num_list = prefix(combined_string)

    idx = 0
    for num in matches_num_list:
        if num == len(needle):
            return idx - 2 *len(needle)
        idx += 1

    return -1


if __name__=="__main__":

    haystack, needle, delimiter = input_data('io/haystack.in', 'io/needle.in', 'io/delimiter.in');
    result = main(haystack, needle, delimiter)
    output_data('io/result.out', result)
    print(result)


