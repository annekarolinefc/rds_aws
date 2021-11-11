import pymysql
rds_host = 'mysqlserver.cuqqvtszfws1.us-east-1.rds.amazonaws.com'
name = 'admin'
password = 'admin1980'
db_name = 'dbteste'
port = 3306

try:
    conn = pymysql.connect(host=rds_host,user=name,
    passwd=password,db=db_name,
    connect_timeout=5,
    cursorclass=pymysql.cursors.DictCursor)
    print('Conectou!')
except:
    sys.exit()

with conn.cursor() as cur:
    qry = "select * from pessoas"
    cur.execute(qry)
    print('Retornando dados da tabela [pessoas]: ')
    print(cur.fetchall())
