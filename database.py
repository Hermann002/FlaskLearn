from sqlalchemy import create_engine, text

db_Connection_string = 'mysql+pymysql://h3gw8trhy0vhtiitvxy9:pscale_pw_b6TLW2YxsVlKeXNMQ2zdWuO0fMxUWROgigkFI5krkba@aws.connect.psdb.cloud/testdatabase?charset=utf8mb4'

engine = create_engine(db_Connection_string,
    connect_args={
        "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
        }
    })    

with engine.connect() as conn:
    result = conn.execute(text("select * from Boutique"))

    result_dicts = []

    for row in result.all():
        result_dicts.append(row._asdict())
    
    # print(result_dicts)

    for colum in result_dicts:
        if colum['id'] == 2:
            print(colum['email'])