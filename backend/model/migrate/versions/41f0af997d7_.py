"""Added resource name

Revision ID: 41f0af997d7
Revises: 3990fca9b74
Create Date: 2015-11-06 11:43:39.653405

"""

# revision identifiers, used by Alembic.
revision = '41f0af997d7'
down_revision = '3990fca9b74'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_usage', sa.Column('resource_name', sa.String(length=256), nullable=True))
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_usage', 'resource_name')
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

