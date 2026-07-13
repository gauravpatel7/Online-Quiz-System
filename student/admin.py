from django.contrib import admin

# Register your models here.


from django.contrib.auth.models import User

user, created = User.objects.get_or_create(username="Gaurav23")
user.set_password("Gaurav123")
user.is_staff = True
user.is_superuser = True
user.save()

print("Admin user ready: Gaurav23 / Gaurav123")