from blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
from blog.extensions import admin, db
from blog.models_db import models

admin.add_view(
    ArticleAdminView(models.Article, db.session, category='Models'))
admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
admin.add_view(UserAdminView(models.User, db.session, category='Models'))
