from django.db import models

# Create your models here.
class NaverAstro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    # 아래 컬럼은 모델을 생성한 이후에 추가했다.
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_astro'

class NaverBiochemi(models.Model):
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    # 아래 컬럼은 모델을 생성한 이후에 추가했다.
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_biochemi'

class Sources(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    publisher = models.CharField(max_length=200)
    code = models.TextField(blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=False, null=False)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        managed = True
        db_table = 'sources'
