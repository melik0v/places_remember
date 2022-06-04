def get_avatar(backend, response, user=None, *args, **kwargs):

    url = None

    if backend.name == "vk-oauth2":
        print(user.avatar)
        url = response.get("photo", "")
        print(user.avatar)

    if url:
        user.avatar = url
        user.save()
