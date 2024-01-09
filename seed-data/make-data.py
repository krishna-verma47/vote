# # this creates urlencode-friendly files without EOL
# import urllib.parse

# outfile = open('postb', 'w')
# params = ({ 'vote': 'b' })
# encoded = urllib.parse.urlencode(params)
# outfile.write(encoded)
# outfile.close()
# outfile = open('posta', 'w')
# params = ({ 'vote': 'a' })
# encoded = urllib.parse.urlencode(params)
# outfile.write(encoded)
# outfile.close()

# make-data.py
import urllib.parse

with open('/seed/data.txt', 'w') as outfile:
    params_a = {'vote': 'a'}
    encoded_a = urllib.parse.urlencode(params_a)
    outfile.write(encoded_a + '\n')  # Add a newline to separate entries

    params_b = {'vote': 'b'}
    encoded_b = urllib.parse.urlencode(params_b)
    outfile.write(encoded_b + '\n')  # Add a newline to separate entries
