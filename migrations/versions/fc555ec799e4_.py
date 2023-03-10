"""empty message

Revision ID: fc555ec799e4
Revises: 
Create Date: 2023-03-12 17:44:34.262746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc555ec799e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_name', sa.String(), nullable=True),
    sa.Column('ability_name', sa.String(), nullable=True),
    sa.Column('base_experience', sa.Integer(), nullable=True),
    sa.Column('front_shiny_url', sa.String(), nullable=True),
    sa.Column('attack_stat', sa.Integer(), nullable=True),
    sa.Column('hp_stat', sa.Integer(), nullable=True),
    sa.Column('defense_stat', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pokemon_team',
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['catch.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon_team')
    op.drop_table('catch')
    # ### end Alembic commands ###
