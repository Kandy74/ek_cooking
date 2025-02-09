"""
产品模型，包含产品ID、产品名称、产品描述、产品类型ID
"""


class ProductModel:
    def __init__(self, product_id, product_name, product_desc, type_id,type_name):
        self.product_id = product_id
        self.product_name = product_name
        self.product_desc = product_desc
        self.type_id = type_id
        self.type_name = type_name
