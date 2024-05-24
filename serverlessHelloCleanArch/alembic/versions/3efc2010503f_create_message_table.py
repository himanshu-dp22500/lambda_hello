"""create message table

Revision ID: 3efc2010503f
Revises: 
Create Date: 2024-05-24 15:35:59.105070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3efc2010503f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'messages',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('created_at', sa.DateTime, default=sa.func.now()),
        sa.Column('text', sa.String(255))
    )


def downgrade():
    op.drop_table('messages')
