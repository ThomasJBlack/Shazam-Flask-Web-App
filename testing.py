import pymysql

db = pymysql.connect(
    host="freetrainer.cryiqqx3x1ub.us-west-2.rds.amazonaws.com",
    user="thomas",
    password="changeme"
)
cursor = db.cursor()

# READS
sql = """SELECT dog_table.id as id, dog_table.name AS Dog, dr_table.name AS Doctor, malady_table.malady AS Malady, breed_table.breed AS Breed
                FROM Thomas_Black.dog_table
                JOIN Thomas_Black.dr_table ON dr_table.id = dog_table.id
                JOIN Thomas_Black.malady_table ON malady_table.id = dog_table.malady_id
                JOIN Thomas_Black.breed_table ON breed_table.id = dog_table.breed_id;"""
cursor.execute(sql)
while True:
    row = cursor.fetchone()
    if row == None:
        break
    print(row)
