from entity.product_model import ProductModel
from util.sqlit_db_util import get_con, close_con


def add_product(product: ProductModel):
    """
    向数据库中添加产品信息
    :param product:
    :return:
    """
    con = None
    cursor = None
    try:
        con, cursor = get_con()
        sql = (f"insert into t_product values ('{product.product_id}','{product.product_name}','{product.product_desc}',"
               f"'{product.type_id}','{product.type_name}')")

        cursor.execute(sql)
        return cursor.rowcount
    except Exception as e:
        print(e)
        con.rollback()
        return 0
    finally:
        close_con(con, cursor)


if __name__ == '__main__':
    input_id = 'MB0102'
    input_name = '面包-甜面包-测试产品1'
    input_desc = '这是一款测试产品，仅用于测试'
    input_type_id = 'MB01'
    input_type_name = '甜面包'
    product_test = ProductModel(input_id, input_name, input_desc, input_type_id,input_type_name)
    add_product(product_test)
