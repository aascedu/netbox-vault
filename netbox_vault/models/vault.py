from django.db import models
from netbox.models import NetBoxModel

class Vault(NetBoxModel):
	name = models.CharField(max_length=20)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name