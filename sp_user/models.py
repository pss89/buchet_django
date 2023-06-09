from django.db import models

# Create your models here.

class Sp_user(models.Model):
    # verbose_name(별칭?)
    username = models.CharField(max_length=32,verbose_name="사용자명")
    password = models.CharField(max_length=64,verbose_name="비밀번호")
    registered_date = models.DateTimeField(auto_now_add=True,verbose_name="등록일자")
    
    # list의 명칭을 정의
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user_info' # 테이블명
        # 앱의 명칭?
        verbose_name = '부쳇_장고 사용자' 
        verbose_name_plural = '부쳇_장고 사용자'