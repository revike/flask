# from blog.models_db import models
# from blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
# from blog.extensions import admin_panel, db


def register_views():
    from blog.models_db import models
    from blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
    from blog.extensions import admin_panel, db

    admin_panel.add_view(
        ArticleAdminView(models.Article, db.session, category='Models'))
    admin_panel.add_view(
        TagAdminView(models.Tag, db.session, category='Models'))
    admin_panel.add_view(
        UserAdminView(models.User, db.session, category='Models'))
