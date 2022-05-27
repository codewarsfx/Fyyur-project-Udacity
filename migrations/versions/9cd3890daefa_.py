"""empty message

Revision ID: 9cd3890daefa
Revises: 7b6f67ffecd9
Create Date: 2022-05-27 16:37:29.816141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cd3890daefa'
down_revision = '7b6f67ffecd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('description', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('is_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    op.drop_column('Venue', 'is_talent')
    op.drop_column('Venue', 'description')
    op.drop_column('Venue', 'website_link')
    # ### end Alembic commands ###