from flask_app import app
from scrape.server.flask_app.controllers.controllers import Controller

@app.route("/top_searches")
def top_searches():
    p = Controller.get_product_repo()
    top_searches = p.get_top_searches()
    top_searches = [
        {"id":1,"name":"Playstation 5","picture":"https://gmedia.playstation.com/is/image/SIEPDC/ps5-product-thumbnail-01-en-14sep21?$facebook$"},
        {"id":2,"name":"Playstation 4","picture":"https://gmedia.playstation.com/is/image/SIEPDC/ps4-product-thumbnail-01-en-14sep21?$facebook$"},
        {"id":3,"name":"RTX 3080","picture":"https://c1.neweggimages.com/ProductImageCompressAll1280/ARUXS211015278F9.jpg"},
        {"id":4,"name":"RTX 4090","picture":"https://www.club386.com/wp-content/uploads/2022/09/4090-FE.jpg"}
    ]
    return {"top_searches": top_searches}