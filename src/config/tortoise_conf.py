TORTOISE_ORM = {
    "connections": {"default": "postgres://blog:blog@localhost:5432/blog"},
    "apps": {
        "models": {
            "models": ["src.app.user.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
