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
            f"insert into t_type_father values ('{type_father.type_id}','{type_father.type_name}','{ type_father.desc}')"
            )
        cursor.execute(sql)
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con, cursor)


if __name__ == '__main__':
    type0 = FatherType(type_id='0001', type_name='蛋糕类', desc='好吃的蛋糕哟')
    reply = add_type_father(type0)
    print(reply)
