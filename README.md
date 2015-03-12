#VN2MOL

Small script to export point data from [VertNet](http://www.vertnet.org) 's CloudStorage bucket to [Map of Life](http://www.mol.org)'s PostgreSQL infrastructure.

*Author: [Javier Otegui](mailto:javier.otegui@gmail.com)*
##Requirements
###Data must be in CloudStorage
The script is ready to extract the content of the `vn-moldumps` bucket of the `vertnet-portal` project. As a first step, the content of a BigQuery table must be extracted to this bucket, replacing any existing files. If a different bucket is to be used, the name of the bucket must be updated in the `process.sh` file, line 7.
### The gsutil command-line tool must have access to vertnet-portal
To get the content of the CloudStorage bucket, the script makes use of the [gsutil](https://cloud.google.com/storage/docs/gsutil) command-line tool. This tool must be configured to access the `vertnet-portal` project. Follow the instructions in the gsutil webpage to properly configure this access.
### Customization must be defined in settings.py
Lastly, the `settings.py` file contains some custom variables that must be updated to match certain key aspects of the process. Specifically, this file has 3 sections:

* Section 1 holds a list of the field names in the dump, in order. This is used to build the create_table SQL scripts.
* Section 2 holds the name of the table that will be created in the Map of Life infrastructure.
* Section 3 must not be modified unless necessary. This has a small function to update certain field names that conflict with existing reserved words. Only update this section if the list of fields has a reserved word that is not already present.

## Location
All the code, including authentication files, is already in Litoria and ready to work. It can be found on the following folder:

    /home/javiero/VN2MOL

## Process
To launch the process once all the requirements are met (they are already satisfied in the working copy in Litoria), simply run the `process.sh` script. It will perform the following steps:

1. Create a temporary folder `temp` wherein BigQuery's data files will be downloaded
2. Using `gsutil`, download the contents of vn-moldumps into the newly crated `temp` folder
3.  Build and execute the `create_table.sql` script. Taking the values from the `settings.py` module, delete the table specified under `TNAME`, create a new empty table with the fields specified in `HEADER` and apply the `Cartodbfy` function to add CartoDB's own fields, triggers and indices.
4. Build and execute the `copies.sql` script. Create a `\copy` statement to import each of the downloaded CSV files in the table
5. Build and execute the `geom.sql` script. Update the_geom field in the new table with data from `decimallatitude` and `decimallongitude` fields
6. Build and execute the `webmercator.sql` script. Update the_geom_webmercatior field in the new table with data from `the_geom` field
7. Build and execute `scientificname.sql` script. Create an index on `scientificname` field
8. Remove downloaded files and `temp` folder

## More stuff in the repo
### jot_cast_string_float.sql
This is a small function to check whether or not a string can be converted to a double precision. It is a key function for skipping problems with the coordinates-to-geom transformation