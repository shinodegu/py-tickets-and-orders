from db.models import User


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> None:
    User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name)


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> None:
    updater = User.objects.get(id=user_id)

    update_fields = {
        "username": username,
        "email": email,
        "first_name": first_name,
        "last_name": last_name
    }  # создаем словарь чтоб использовать вместо кучи if
    # удалил None
    update_fields = {key: value for key, value in
                     update_fields.items() if value is not None}

    if update_fields:  # если есть не None то добавил
        User.objects.filter(id=user_id).update(**update_fields)

    if password:
        updater.set_password(password)
        updater.save()
