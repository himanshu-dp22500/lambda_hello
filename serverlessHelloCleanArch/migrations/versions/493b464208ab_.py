"""empty message

Revision ID: 493b464208ab
Revises: 3de5b58d10be
Create Date: 2024-05-26 14:44:06.387748

"""
import sqlalchemy as sa
from sqlalchemy.sql import text

from alembic import op
from serverlessHelloCleanArch.constants.enums import MessageType

# revision identifiers, used by Alembic.
revision = "493b464208ab"
down_revision = "3de5b58d10be"
branch_labels = None
depends_on = None


def upgrade():
    MessageTypeEnum = sa.Enum(
        *[e.value for e in MessageType], name="messageType"
    )
    MessageTypeEnum.create(op.get_bind(), checkfirst=False)

    op.add_column(
        "message",
        sa.Column(
            "message_type",
            MessageTypeEnum,
            nullable=False,
            server_default=text("'HELLO'"),
        ),
    )

    op.alter_column(
        "message", "text", existing_type=sa.String(length=255), nullable=False
    )


def downgrade():
    op.drop_column("message", "message_type")
    sa.Enum(name="messageType").drop(op.get_bind(), checkfirst=False)
    op.alter_column(
        "message", "text", existing_type=sa.String(length=255), nullable=True
    )
