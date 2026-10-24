
class Routes:

    Base_url= "http://localhost:3000"

    #Product Module
    GET_ALL_PRODUCT ="/products"
    GET_PRODUCT_BY_ID ="/products/{id}"
    GET_PRODUCT_BY_LIMIT ="/products?_limit={limit}"
    GET_PRODUCT_BY_CATEGORY ="/products?category={cat}"
    CREATE_PRODUCT ="/products"
    UPDATE_PRODUCT ="/products/{id}"
    DELETE_PRODUCT ="/products/{id}"

    #Cart Module
    Create_Cart ="/carts"