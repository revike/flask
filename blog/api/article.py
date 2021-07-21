from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models_db.models import Article
from blog.schemas import ArticleSchema


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article
    }


class ArticleListEvent(EventsResource):

    def event_get_count(self, *args, **kwargs):
        return {'count': Article.query.count()}


class ArticleDetailEvent(EventsResource):

    def event_get_count_by_author(self, *args, **kwargs):
        return {'count': Article.query.filter(
            Article.author_id == kwargs['id']).count()}
