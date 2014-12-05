import os
import argparse
import sys

def get_strings(filename):
    """
    Read strings from files generated by an IDAPython script and store them in a list for further processing.
    """
    list_strings= []
    with open(filename,'rU') as f:
        list_strings= [line[:-1] for line in f.readlines()]

    return list_strings

def get_exe_to_reverse():
    """
    Read command line arguments.
    """
    parser= argparse.ArgumentParser()
    parser.add_argument('file', nargs=1, help='Enter the name of the file you want to reverse engineer here')
    args = parser.parse_args()

    return args.file[0]

def string_compare(exe_to_reverse, file_string_map):
    """
    Compare each string from the binary you want to reverse with all the strings from all other files
    If there's a match store the name of the DLL and the string that was matched in a dictionary
    Return the dictionary for further analysis
    """
    l1= file_string_map[exe_to_reverse].split('^')
    match_result= {}

    for key,value in file_string_map.iteritems():
        l2= []
        if key != exe_to_reverse:
            l2= value.split('^')
            l3= [i for i in l1 for j in l2 if i==j]
            match_result[key+'_'+str(len(l3))]= l3
        else:
            continue

    return match_result

if __name__ == "__main__":
    """
    Read all CLI arguments
    Open all files, extract all strings and store
    Identify which strings belong to the program you are reversing
    Compare these strings against all strings of all other files
    Report matches found
    Analyze these results
    """
    exe_to_reverse= get_exe_to_reverse()

    output_dir= 'all_outputs'
    file_string_map={}
    for filename in os.listdir(output_dir):
        list_strings= get_strings(output_dir+'/'+filename)
        file_string_map[filename[:-4]]='^'.join(list_strings)

    match_result= string_compare(exe_to_reverse, file_string_map)
    for key,value in match_result.iteritems():
        print 'Matches in the file ',key.split('_')[0], ' - ', key.split('_')[1], '\n\t', value, '\n'
