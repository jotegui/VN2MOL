from settings import HEADER_FIXED, TNAME

sql = "DROP TABLE IF EXISTS {0};\n\nCREATE TABLE {0} (\n".format(TNAME)

for i in HEADER_FIXED:
    sql += "  {0} {1}".format(i, 'text')

    if i != HEADER_FIXED[-1]:
        sql += ",\n"

sql += "\n);\n\n"

sql += "SELECT CDB_CartodbfyTable('{0}');\n".format(TNAME)

with open("./create_table.sql", "w") as o:
    o.write(sql)
