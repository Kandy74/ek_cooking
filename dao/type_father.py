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


def get_all_type_father():
    """
    获取所有烘焙大类
    :return:
    """
    con = None
    cursor = None
    try:
        con, cursor = get_con()
        sql = "select * from t_type_father"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        return None
    finally:
        close_con(con, cursor)


if __name__ == '__main__':
    type0 = FatherType(type_id='0001', type_name='蛋糕类', desc='好吃的蛋糕哟')
    reply = add_type_father(type0)
    print(reply)
