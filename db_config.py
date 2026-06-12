import mysql.connector


def get_database_connection():
    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="2V8L8cJ4deyWyqw.root",
        password="vQPmckc9mpE1oXSq",
        database="student_task_manager",
        port=4000
    )
    return connection
