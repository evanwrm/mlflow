"""add experiment foreign key cascades

Create Date: 2026-07-09 21:16:54.445000

"""

from alembic import op

from mlflow.store.tracking.dbmodels.models import (
    SqlExperiment,
    SqlTraceInfo,
)

# revision identifiers, used by Alembic.
revision = "6f8d9c3b2a1e"
down_revision = "b7e4c1a90f23"
branch_labels = None
depends_on = None


_EXPERIMENT_FKS = [
    (SqlTraceInfo.__tablename__, "fk_trace_info_experiment_id"),
]


def upgrade():
    for table_name, constraint_name in _EXPERIMENT_FKS:
        with op.batch_alter_table(table_name, schema=None) as batch_op:
            batch_op.drop_constraint(constraint_name, type_="foreignkey")
            batch_op.create_foreign_key(
                constraint_name,
                SqlExperiment.__tablename__,
                ["experiment_id"],
                ["experiment_id"],
                ondelete="CASCADE",
            )


def downgrade():
    pass
