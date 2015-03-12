from settings import TNAME

template = """set statement_timeout=0;
create index {0}_scientificname_btree on {0} using btree(scientificname);
vacuum analyze {0};
"""

with open('./scientificname.sql', 'w') as w:
    w.write(template.format(TNAME))
