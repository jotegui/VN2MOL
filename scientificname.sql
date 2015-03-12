set statement_timeout=0;
create index vertnet_jan2015_scientificname_btree on vertnet_jan2015 using btree(scientificname);
vacuum analyze vertnet_jan2015;
