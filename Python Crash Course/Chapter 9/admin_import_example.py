from admin_import import Privileges, Users, Admin
# 9.11 example

mikhail_bekker = Admin("Mikhail", "Bekker", "Male", "24")

mikhail_bekker.describe_user()
mikhail_bekker.privileges.show_privileges()