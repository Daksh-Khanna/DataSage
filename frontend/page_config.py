PAGES = [
    {
        "path": "frontend/pages/login.py",
        "func_name": "login_page",
        "title": "Login", "icon": "🔐",
        "authorized_roles": ["guest"]
    },
    {
        "path": "frontend/pages/signup.py",
        "func_name": "signup_page",
        "title": "Sign Up", "icon": "📝",
        "authorized_roles": ["guest"]
    },
    {
        "path": "frontend/pages/dashboard_ui.py",
        "func_name": "dashboard_page",
        "title": "Dashboard", "icon": "📊",
        "authorized_roles": ["user"]
    },
    {
        "path": "frontend/pages/chat.py",
        "func_name": "chat_page",
        "title": "AI Copilot", "icon": "💬",
        "authorized_roles": ["user"]
    },
    {
        "path": "frontend/pages/admin.py",
        "func_name": "admin_page",
        "title": "Admin", "icon": "👑",
        "authorized_roles": ["admin", "super_admin"]
    },
    {
        "path": "frontend/pages/logout.py",
        "func_name": "logout_page",
        "title": "Logout", "icon": "🚪",
        "authorized_roles": ["user", "admin", "super_admin"]
    }
]


def get_pages_for_role(role="guest"):
    return [page for page in PAGES if page["authorized_roles"] and role in page["authorized_roles"]]


def get_default_page(role=None):
    """Get the default page for a specific role"""
    role_pages = get_pages_for_role(role)
    for page in role_pages:
        if page.get("default", False):
            return page
    return role_pages[0] if role_pages else None