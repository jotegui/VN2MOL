from settings import TNAME

template = """set statement_timeout=0;
update {0} set the_geom=ST_SetSRID(ST_Point(jot_cast_string_float(decimallongitude), jot_cast_string_float(decimallatitude)), 4326);
"""

with open('./geom.sql', 'w') as w:
    w.write(template.format(TNAME))
