from scrape.server.flask_app.configuration import Config
from scrape.server.flask_app.repo.users import User as UserRepo
from scrape.server.flask_app.repo.products import Product as ProductRepo
from scrape.server.flask_app.repo.watchlists import Watchlist as WatchlistRepo

class Controller:
    config: Config = Config()
    user_repo: UserRepo = None
    product_repo: ProductRepo = None
    watchlist_repo: WatchlistRepo = None
    
    @classmethod
    def get_user_repo(cls) -> UserRepo:
        if cls.user_repo == None:
            cls.user_repo = UserRepo(cls.config)
        
        return cls.user_repo
    
    @classmethod
    def get_product_repo(cls) -> ProductRepo:
        if cls.product_repo == None:
            cls.product_repo = ProductRepo(cls.config)
        
        return cls.product_repo

    @classmethod
    def get_watchlist_repo(cls) -> WatchlistRepo:
        if cls.watchlist_repo == None:
            cls.watchlist_repo = WatchlistRepo(cls.config)
        
        return cls.watchlist_repo