from views import index,squ

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/squ', squ)

