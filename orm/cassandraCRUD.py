from cassandra.cluster import Cluster

# connection
cluster = Cluster(['spark1', 'spark3'], 9042)
session = cluster.connect('test_ks')

# insert
#session.execute("insert into employee_uuid(id,fname,lname) values(uuid(),'millions','cheng')")

# query
results = session.execute("select * from employee_uuid")
for row in results:  # 记录类型<class 'cassandra.io.asyncorereactor.Row'>
    print(row.id, row.fname, row.lname)

print("---finished")
