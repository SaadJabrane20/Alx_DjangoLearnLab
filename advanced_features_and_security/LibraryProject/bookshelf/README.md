# Library Project - Custom Permissions

This project uses a **CustomUser model** and defines specific **custom permissions** for managing users and books in the library system.

## Custom Permissions

### On `CustomUser`:
| Codename       | Description               |
|----------------|--------------------------|
| `can_view`     | Can view users           |
| `can_create`   | Can create users         |
| `can_edit`     | Can edit users           |
| `can_delete`   | Can delete users         |

### On `Book`:
| Codename       | Description               |
|----------------|--------------------------|
| `can_add_book`   | Can add a book           |
| `can_change_book`| Can change a book        |
| `can_delete_book`| Can delete a book        |

## Assigning Permissions

You can assign permissions programmatically:

```python
from django.contrib.auth.models import Permission
from bookshelf.models import CustomUser

user = CustomUser.objects.get(username="saadjbr")
perm = Permission.objects.get(codename="can_view")
user.user_permissions.add(perm)

# Check permission
user.has_perm("bookshelf.can_view")  # returns True or False
