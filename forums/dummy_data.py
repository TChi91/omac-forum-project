import stores, models

post_store = stores.PostStore()

post_store.add(models.Post('Hello world', 'Hello world from Flask app'))
post_store.add(models.Post('Hello world 2', 'Hello world from Flask app 2'))