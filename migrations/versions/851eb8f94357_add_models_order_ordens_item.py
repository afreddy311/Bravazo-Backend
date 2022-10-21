"""add models order,ordens_item

Revision ID: 851eb8f94357
Revises: 2b2ee729cb30
Create Date: 2022-09-22 16:47:14.620401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851eb8f94357'
down_revision = '2b2ee729cb30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('total_price', sa.Float(precision=2), nullable=True),
    sa.Column('subtotal_price', sa.Float(precision=2), nullable=True),
    sa.Column('igv_price', sa.Float(precision=2), nullable=True),
    sa.Column('discount_price', sa.Float(precision=2), nullable=True),
    sa.Column('correlative', sa.String(length=12), nullable=True),
    sa.Column('checkout_id', sa.String(length=255), nullable=True),
    sa.Column('checkout_url', sa.String(length=255), nullable=True),
    sa.Column('payment_status', sa.String(), nullable=True),
    sa.Column('payment_detail', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders_items')
    op.drop_table('orders')
    # ### end Alembic commands ###