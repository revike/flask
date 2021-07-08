"""empty message

Revision ID: eb78267ca605
Revises: 66b36ba09034
Create Date: 2021-07-08 13:38:51.949415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb78267ca605'
down_revision = '66b36ba09034'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_tag_associations')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.create_foreign_key(None, 'articles', 'authors', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.create_foreign_key(None, 'articles', 'users', ['author_id'], ['id'])
    op.create_table('article_tag_associations',
    sa.Column('article_id', sa.INTEGER(), nullable=False),
    sa.Column('tag_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    # ### end Alembic commands ###
