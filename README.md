slid
====

1. Get a list of the functions that are displayed inside IDA. The aim is to identify as many functions as possible that are part of some
   standard library. As of now, we're only looking at glibc. 
   
   "C:\Program Files (x86)\IDA 6.4\idaw64" -c -o"C:\Users\arvind\Desktop\static" -L"C:\Users\arvind\Desktop\static\batch_log.txt" -A -S"C:\Users\arvind\Desktop\static\get_vuln_functions_list.py" "C:\Users\arvind\Desktop\static\static_hello"

   Copy the output of the script into the folder where the file static_detector.py is.

2. Now identify which of these symbols are present in the glibc sources.

   python static_detector.py
   
3. Copy the output of this script into the folder where the file rename_functions.py is.

   "C:\Program Files (x86)\IDA 6.4\idaw64" -o"C:\Users\arvind\Desktop\static" -L"C:\Users\arvind\Desktop\static\batch_log.txt" -A -S"C:\Users\arvind\Desktop\static\rename_funcs.py" "C:\Users\arvind\Desktop\static\static_hello"
   
4. Open the IDA64 file (IDA database) and notice that a number of functions have been renamed.
