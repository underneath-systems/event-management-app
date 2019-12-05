from django.db import models
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser)
# from events_operations.models import Event
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Los usuarios deben tener email')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Correo electronico',
        max_length=255,
        unique=True,
        primary_key=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    photo_id = models.ImageField(null=True, blank=True, upload_to='media')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



entidades=[
        ('FA', 'Facultad de Arquitectura'),
        ('FAD', 'Facultad de Artes y Diseno'),
        ('FC', 'Facultad de Ciencias'),
        ('FCPS', 'Facultad de Ciencias Politicas y Sociales'),
        ('FCA', 'Facultad de Contaduria y Administracion'),
        ('FD', 'Facultad de Derecho'),
        ('FE', 'Facultad de Economia'),
        ('FESAc', 'Facultad de Estudios Superiores (FES) Acatlan'),
        ('FESAc', 'Facultad de Estudios Superiores (FES) Acatlan'),
        ('FESAr', 'Facultad de Estudios Superiores (FES) Aragon'),
        ('FESC', 'Facultad de Estudios Superiores (FES) Cuautitlan'),
        ('FESI', 'Facultad de Estudios Superiores (FES) Iztacala'),
        ('FESZ', 'Facultad de Estudios Superiores (FES) Zaragoza'),
        ('FLL', 'Facultad de Filosofia y Letras'),
        ('FI', 'Facultad de Ingenieria'),
        ('FMe', 'Facultad de Medicina'),
        ('FMVZ', 'Facultad de Medicina Veterinaria y Zootecnia'),
        ('FMu', 'Facultad de Musica'),
        ('FO', 'Facultad de Odontologia'),
        ('FP', 'Facultad de Psicologia'),
        ('FQ', 'Facultad de Quimica'),
]

class Attendees(User):
    entity = models.CharField(max_length=10, choices=entidades, default="FC")

class Organizer(User):
    # idOrganizer = models.UUIDField(default=uuid.uuid4, editable=False)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return '{} {}'.format(self.first_name, self.email)


class Staff_event(User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    working_hours = models.IntegerField(default=8)
    def __str__(self):
        return '{} {}'.format(self.first_name, self.email)

