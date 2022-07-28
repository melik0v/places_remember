from social_django.models import UserSocialAuth
import requests


def get_avatar(backend, response, user=None, *args, **kwargs):

    if backend.name == "vk-oauth2":
        user_social_auth = (
            UserSocialAuth.get_social_auth_for_user(user.id).get().extra_data
        )
        # url = response.get("photo", "")
        response = requests.get(
            "https://api.vk.com/method/users.get?user_ids={0}&fields=photo_400_orig&access_token={1}&v=5.131".format(
                user_social_auth.get("id"), user_social_auth.get("access_token")
            )
        )
        # a = "https://api.vk.com/method/users.get?user_ids={0}&fields=photo_400_orig&access_token={1}&v=5.131".format(user_social_auth.get("id"), user_social_auth.get("access_token"))
        # print("PROVERKA", a)

    if response.json():
        user.avatar = response.json()["response"][0]["photo_400_orig"]
        user.save()
        # print("URL =", response.json())
        # print(user.avatar)
        # print([field.name for field in user._meta.get_fields()])
        # print("User ID =", user_social_auth.get("id"))
        # print(user_social_auth.get("access_token"))
