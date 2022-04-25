from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Class for booking model
    in database and for booking form.
    """
    user = models.ForeignKey(User, null=True, blank=True)
    customer_name = models.CharField(max_length=20, null=True)
    reservation_date_and_time = models.DateTimeField(null=True)

    def validate_date(reservation_date_and_time):
        """
        Function that validates date
        so no booking could be made 
        in the past 
        """
         if reservation_date_and_time < timezone.now():
            raise ValidationError("Date cannot be in the past")
    reservation_date_and_time = models.DateTimeField(null=True, blank=True, validators=[validate_date])
