from entity.type_father_model import FatherType
from util.sqlit_db_util import get_con, close_con


def add_type_father(type_father: FatherType):
    """
    实现向数据库添加烘焙大类的功能
    :param type_father: 烘焙大类对象
    :return: 添加数量
    """

    con = None
    cursor = None
    try:
        con, cursor = get_con()
        sql = (
            f"insert into t_type_father values ('{type_father.type_id}','{type_father.type_name}','{type_father.desc}')"
        )
        cursor.execute(sql)
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con, cursor)


def type_father_exist(type_id: str, type_name: str):
    """
    判断烘焙大类是否存在
    :param type_id:
    :param type_name:
    :return:
    """
    con = None
    cursor = None
    try:
        con, cursor = get_con()
        sql = f"select * from t_type_father where type_id='{type_id}' or type_name='{type_name}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    finally:
        close_con(con, cursor)


def search_type_father(type_name=None, type_id=None):
    """
    搜索烘焙大类
    :param type_name:
    :param type_id:
    :return:
    """
    con = None
    cursor = None
    try:
        con, cursor = get_con()
        sql = "select * from t_type_father"
        if type_name:
            sql += f" where type_name like '%{type_name}%'"
        if type_id:
            sql += f" where type_id like '%{type_id}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        return None
    finally:
        close_con(con, cursor)


def delete_type_father(type_id: str):
    """
    删除烘焙大类
    :param type_id:
    :return:
    """
    con = None
    cursor = None
    try:
        con, cursor = get_con()
        sql = f"delete from t_type_father where type_id='{type_id}'"
        cursor.execute(sql)
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con, cursor)


def update_type_father(type_father: FatherType):
    """
    更新烘焙大类
    :param type_father:
    :return:
    """
    con = None
    cursor = None
    try:
        con, cursor = get_con()
        sql = (f"update t_type_father set type_name='{type_father.type_name}',desc='{type_father.desc}' "
               f"where type_id='{type_father.type_id}'")
        cursor.execute(sql)
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con, cursor)


if __name__ == '__main__':
    reply = search_type_father(type_id='0001')
    print(reply)
