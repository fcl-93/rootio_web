"""addtext_field

Revision ID: 1a50a1e1fa9f
Revises: 1add4f7e4ef2
Create Date: 2016-08-26 15:28:11.372533

"""

# revision identifiers, used by Alembic.
revision = '1a50a1e1fa9f'
down_revision = '1add4f7e4ef2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('radio_scheduledprogram', sa.Column('deleted', sa.Boolean(), nullable=True))
    op.add_column(u'telephony_message', sa.Column('text', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'telephony_message', 'text')
    op.drop_column('radio_scheduledprogram', 'deleted')
    ### end Alembic commands ###
