from desingpattern.singleton.database_connection import DatabaseConnectionSingleton

for i in range(10):
    con = DatabaseConnectionSingleton()
    print(con)
# conn1.connect()
conn1 = DatabaseConnectionSingleton()
conn2 = DatabaseConnectionSingleton()
# conn2.connect()

print(f'¿Son el mismo objeto? {conn1 is conn2}')

# conn1.disconnect()
# conn2.disconnect()


