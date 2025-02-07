from sqlite3 import connect


def get_con():
    """
    链接数据库
    :return:
    """
    con = connect('../db/cooking_data.db')
    cursor = con.cursor()
    return con, cursor


def close_con(con, cursor):
    """
    提交数据并关闭数据库
    :return:
    """
    con.commit()
    cursor.close()
    con.close()


