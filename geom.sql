set statement_timeout=0;

update vertnet_jan2015 set the_geom=ST_SetSRID(ST_Point(jot_cast_string_float(decimallongitude), jot_cast_string_float(decimallatitude)), 4326);
