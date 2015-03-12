set statement_timeout=0;
update vertnet_jan2015 set the_geom_webmercator=ST_Transform(the_geom, 3857) where jot_cast_string_float(decimallatitude)>-90 and jot_cast_string_float(decimallatitude)<90 and jot_cast_string_float(decimallongitude)<180 and jot_cast_string_float(decimallongitude)>-180;
