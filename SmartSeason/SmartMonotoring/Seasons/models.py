from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('agent', 'Field Agent'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    employee_id = models.CharField(max_length=20, unique=True)
    region = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

def __str__(self):
    return f"{self.employee_id} - {self.email}"
    


class Field(models.Model):
    STAGE_CHOICES = (
        ('planted', 'Planted'),
        ('growing', 'Growing'),
        ('ready', 'Ready'),
        ('harvested', 'Harvested'),
    )

    crop_type = models.CharField(max_length=100)
    planting_date = models.DateField()
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='planted')
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fields')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def status(self):
        return dict(self.STAGE_CHOICES).get(self.stage, "Needs Attention")


class Update(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='updates')
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updates')
    stage = models.CharField(max_length=20, choices=Field.STAGE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)