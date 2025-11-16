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

# Security Review

This project implements several recommended Django security features:

1. HTTPS Enforcement
- SECURE_SSL_REDIRECT ensures all traffic is encrypted.
- SSL/TLS certificates configured at the web server level.

2. HTTP Strict Transport Security (HSTS)
- SECURE_HSTS_SECONDS = 31536000 protects clients by requiring HTTPS.
- Includes subdomains and preload support.

3. Secure Cookies
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE ensure cookies are never sent over HTTP.

4. Secure HTTP Headers
- X_FRAME_OPTIONS = "DENY" protects against clickjacking.
- SECURE_CONTENT_TYPE_NOSNIFF prevents MIME sniffing.
- SECURE_BROWSER_XSS_FILTER enables browser XSS protection.

5. Content Security Policy (CSP)
- Limits where scripts, styles, and resources can load from.
- Helps prevent XSS attacks.

These combined safeguards significantly reduce risks like XSS, clickjacking, session hijacking, and insecure cookie transmission. Potential future improvements include enabling subresource integrity (SRI) and further tightening CSP directives.

