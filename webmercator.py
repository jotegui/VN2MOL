from settings import TNAME

template = """set statement_timeout=0;
update {0} set the_geom_webmercator=ST_Transform(the_geom, 3857) where jot_cast_string_float(decimallatitude)>-90 and jot_cast_string_float(decimallatitude)<90 and jot_cast_string_float(decimallongitude)<180 and jot_cast_string_float(decimallongitude)>-180;
"""

with open('./webmercator.sql', 'w') as w:
    w.write(template.format(TNAME))
