from app import db
from app.models import User, Role, UserRoles

admin = User(username='admin', email='admin@footnotetrivia.com', password='admin')
admin_role = Role(name='admin')

user_role = UserRoles(user_id=admin.id, role_id=admin_role.id)

db.session.add(admin)
db.session.add(admin_role)
db.session.commit()
