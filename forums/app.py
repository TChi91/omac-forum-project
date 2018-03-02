from flask import Flask
import dummy_data
import stores

app = Flask(__name__)

from views import *

member_store = stores.MemberStore()
post_store = stores.PostStore()


if __name__ == "__main__":
    dummy_data.seed_stores(member_store, post_store)
    app.run()