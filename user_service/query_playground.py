import os
from user_service.models import User, Job
from django.db.models import Q
from django.db.models import Avg, Max, Min, Sum, Count
from django.db.models.functions import Lower


age_avg = User.objects.all().aggregate(Avg('age'))
print('users', age_avg['age__avg'])

users = User.objects.all()
users = User.objects.filter(location__startswith="Ank").first()
users = User.objects.filter(location__endswith="title").all()
users = User.objects.filter(age__gte=30).all()

query = Q(location__startswith="Ank") & ~Q(age__gte=30)
query = Q(location__startswith="Ank") | ~Q(age__gte=30)
users = User.objects.filter().order_by("-age").all()
users_count = User.objects.filter().order_by("-age").all().count()

users = User.objects.all().order_by(Lower('first_name')).values_list('last_name', 'first_name')

print('users_count', users_count)
print('users', users)



