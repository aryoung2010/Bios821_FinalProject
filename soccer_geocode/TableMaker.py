

def sql_fetch(con):
    '''Print all table names to preview table content'''
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    tables = cursorObj.fetchall()
    return tables


def tableMaker(con):
    '''Create the geocode table with foreign keys for country name and country id and
    put in a check on if the table exists, so it won't throw an error'''
    cursorObj = con.cursor()
    tables = sql_fetch(connection)
    if ('geocodes',) in tables:
        print("Table already exixts")
    else:
        cursorObj.execute("CREATE TABLE geocodes(id integer PRIMARY KEY, country_id integer, country_name text, lat real, long real, CONSTRAINT fk_country_id FOREIGN KEY (country_id) REFERENCES Country(id),CONSTRAINT fk_country_name FOREIGN KEY (country_name) REFERENCES Country(name))")
    con.commit()

def fetchCountries(con):
    '''Get values for the country table, to see can be sure they link to the new geocode table'''
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Country')
    countries= cursorObj.fetchall()
    return countries

def addValues(con, data_tuples):
    '''Adds values from MapBoxGeocoder data_tuples into the geocodes table of SQL database'''
    cursorObj = con.cursor()
    i =1
    for a,b,c,d in data_tuples:
        print(i,a,b,c,d)
        cursorObj.execute('INSERT INTO geocodes (id,country_id, country_name, lat, long) VALUES (?,?,?,?,?)', (i,a,b,c,d))
        i += 1
    con.commit()

def fetchRows(con):
    '''Get values for the geocodes table, to see how to link to the new geocode table'''
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM geocodes')
    geos= cursorObj.fetchall()
    return geos
