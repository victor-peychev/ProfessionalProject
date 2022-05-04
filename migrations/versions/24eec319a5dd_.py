"""empty message

Revision ID: 24eec319a5dd
Revises: 133952ae1cf1
Create Date: 2022-04-21 17:44:02.565423

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '24eec319a5dd'
down_revision = '133952ae1cf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('scratching_triggers_rubbing_neck_chest_shoulder', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('scratching_triggers_rubbing_belly', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('scratching_triggers_rubbing_tailhead', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('scratching_triggers_when_excited_anxious', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('scratching_triggers_during_night', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalising_when_scratching_shoulder_neck', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalising_when_scratching_back_of_head_ear', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('nibbling_licking_fore_feet', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('nibbling_licking_hind_feet', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('nibbling_licking_tail_head', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('nibbling_licking_belly', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('nibbling_licking_flank', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalisation_during_sleep', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalisation_on_rising_or_when_jumping', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalisation_when_being_picked_up', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalisation_during_defecation', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalisation_when_emotionally_aroused', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('vocalisation_yelping_or_screaming_when_anxious', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('interactions_no_longer_jumping_up_to_greet', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('interactions_increase_in_anxious_behaviour', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('interactions_more_withdraw', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('interactions_more_timid_with_other_dogs_or_humans', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('interactions_increased_agression_to_other_dogs', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('interactions_growling_when_picked_up', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('interactions_increased_agression_to_humans', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_tocuh_grooming_aversion_ears_head_and_or_neck', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_tocuh_grooming_aversion_1_2_limb_and_paw', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_tocuh_grooming_aversion_sternum_or_flank', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_abnormal_awake_head_neck_posture', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_sleeping_elevated_or_unusual_head_posture', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_squinting_avoiding_light', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_licking_limb_paw', sa.String(length=256), nullable=True))
    op.add_column('submissions', sa.Column('other_signs_pain_grimace', sa.String(length=256), nullable=True))
    op.drop_column('submissions', 'interactions')
    op.drop_column('submissions', 'nibbling_licking')
    op.drop_column('submissions', 'other_signs')
    op.drop_column('submissions', 'vocalising_when_scratching')
    op.drop_column('submissions', 'vocalisation_yelping_or_screaming')
    op.drop_column('submissions', 'scratching_site')
    op.drop_column('submissions', 'scratching_triggers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('scratching_triggers', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('submissions', sa.Column('scratching_site', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('submissions', sa.Column('vocalisation_yelping_or_screaming', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('submissions', sa.Column('vocalising_when_scratching', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('submissions', sa.Column('other_signs', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('submissions', sa.Column('nibbling_licking', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('submissions', sa.Column('interactions', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('submissions', 'other_signs_pain_grimace')
    op.drop_column('submissions', 'other_signs_licking_limb_paw')
    op.drop_column('submissions', 'other_signs_squinting_avoiding_light')
    op.drop_column('submissions', 'other_signs_sleeping_elevated_or_unusual_head_posture')
    op.drop_column('submissions', 'other_signs_abnormal_awake_head_neck_posture')
    op.drop_column('submissions', 'other_signs_tocuh_grooming_aversion_sternum_or_flank')
    op.drop_column('submissions', 'other_signs_tocuh_grooming_aversion_1_2_limb_and_paw')
    op.drop_column('submissions', 'other_signs_tocuh_grooming_aversion_ears_head_and_or_neck')
    op.drop_column('submissions', 'interactions_increased_agression_to_humans')
    op.drop_column('submissions', 'interactions_growling_when_picked_up')
    op.drop_column('submissions', 'interactions_increased_agression_to_other_dogs')
    op.drop_column('submissions', 'interactions_more_timid_with_other_dogs_or_humans')
    op.drop_column('submissions', 'interactions_more_withdraw')
    op.drop_column('submissions', 'interactions_increase_in_anxious_behaviour')
    op.drop_column('submissions', 'interactions_no_longer_jumping_up_to_greet')
    op.drop_column('submissions', 'vocalisation_yelping_or_screaming_when_anxious')
    op.drop_column('submissions', 'vocalisation_when_emotionally_aroused')
    op.drop_column('submissions', 'vocalisation_during_defecation')
    op.drop_column('submissions', 'vocalisation_when_being_picked_up')
    op.drop_column('submissions', 'vocalisation_on_rising_or_when_jumping')
    op.drop_column('submissions', 'vocalisation_during_sleep')
    op.drop_column('submissions', 'nibbling_licking_flank')
    op.drop_column('submissions', 'nibbling_licking_belly')
    op.drop_column('submissions', 'nibbling_licking_tail_head')
    op.drop_column('submissions', 'nibbling_licking_hind_feet')
    op.drop_column('submissions', 'nibbling_licking_fore_feet')
    op.drop_column('submissions', 'vocalising_when_scratching_back_of_head_ear')
    op.drop_column('submissions', 'vocalising_when_scratching_shoulder_neck')
    op.drop_column('submissions', 'scratching_triggers_during_night')
    op.drop_column('submissions', 'scratching_triggers_when_excited_anxious')
    op.drop_column('submissions', 'scratching_triggers_rubbing_tailhead')
    op.drop_column('submissions', 'scratching_triggers_rubbing_belly')
    op.drop_column('submissions', 'scratching_triggers_rubbing_neck_chest_shoulder')
    # ### end Alembic commands ###