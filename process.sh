echo "Begin"

# Create temp folder
mkdir temp

# Download files from vn-moldumps
gsutil cp gs://vn-moldumps/* ./temp/

# Create and execute CREATE TABLE sql
python create_table.py
psql -h mol.cartodb.com -U cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3 -d cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3_db < create_table.sql

# Create and execute COPY sql
python copy.py
psql -h mol.cartodb.com -U cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3 -d cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3_db < copies.sql

# Create and execute GEOM sql
python geom.py
psql -h mol.cartodb.com -U cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3 -d cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3_db < geom.sql

# Create and execute WEBMERCATOR SQL
python webmercator.py
psql -h mol.cartodb.com -U cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3 -d cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3_db < webmercator.sql

# Index scientificname
python scientificname.py
psql -h mol.cartodb.com -U cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3 -d cartodb_user_b4ba2644-9de0-43d0-86fb-baf3b484ccd3_db < scientificname.sql

# Delete temp folder
rm -R temp

echo "Done"
