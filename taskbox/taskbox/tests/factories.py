import factory

from taskbox.taskbox.models import Task
from taskbox.users.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.PostGenerationMethodCall('set_password', 'adm1n')
    email = factory.LazyAttribute(lambda o: '%s@example.com' % (o.username))

    @factory.sequence
    def username(n):
        return 'user%d' % n


class TaskFactory(factory.Factory):
    class Meta:
        model = Task

    user = factory.RelatedFactory(UserFactory)
