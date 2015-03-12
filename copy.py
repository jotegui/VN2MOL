from settings import TNAME, HEADER_FIXED
import os

template = '\copy {1} ({2}) FROM \'{0}\' with csv header\n'

# Load file list
files = os.listdir('temp')

# Set timeout to 0
with open('./copy.sql', 'w') as w:
    w.write('set statement_timeout=0;\n\n')

# For each file
for f in sorted(files):
    
    # Create SQL
    sql = template.format('./temp/{0}'.format(f), TNAME, ','.join(HEADER_FIXED))
    
    # Write SQL in file
    with open('./copy.sql', 'a') as w:
        w.write("select 'Loading {0}';\n".format(f))
        w.write(sql)
        w.write("\n")
