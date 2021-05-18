import sys

input_target = sys.argv[1]
input_file = sys.argv[2]
with open(file=input_file) as f:
    emails = f.read().splitlines()
    for email in emails:
        #print(email, end='')
        output_email = email + input_target
        print(output_email)
