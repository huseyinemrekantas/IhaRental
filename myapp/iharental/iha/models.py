from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date =models.DateTimeField(auto_now=True)

class IhaModel(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Iha(BaseModel):
    brand = models.CharField(max_length=255)
    model = models.ForeignKey(IhaModel, on_delete=models.CASCADE)
    weight = models.FloatField()
    iha_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.brand

class Rental(BaseModel):
    rented_iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    rented_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.rented_iha

