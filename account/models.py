from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Models):
    mobile_phone = models.CharField(max_length = 12)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    user = models.OneToOneField(to = User, related_name = 'account', on_delete = models.CASCADE)
    
    def __str__(self)->str:
        return f'{self.id} --- {self.mobile_phone}'
    
    class Meta:
        db_table = 'UserAccount'
        ordering = ['-created_at']
        verbose_name = 'User account'
        verbose_name_plural = 'User accounts'
        
        
