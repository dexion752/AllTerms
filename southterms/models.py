from django.db import models
from django.utils import timezone

# Create your models here.
class NaverAstro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_astro'


class NaverBiochemi(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_biochemi'


class NaverBotany(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_botany'


class NaverBuddh(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_buddh'

class NaverCell(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_cell'

class NaverChemi(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_chemi'


class NaverLife(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_life'


class NaverChemiPedia(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_chemipedia'

class NaverMath(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_math'



class NaverMeteo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_meteo'




class NaverEarth(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_earth'



class NaverGeo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_geo'



class NaverOcean(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_ocean'



class NaverZoo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_zoo'



class NaverMicroBio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_microbio'



class NaverFood(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_food'


class NaverWater(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_water'


class NaverMine(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_mine'


class NaverWeather(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_weather'


class NaverGovern(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_govern'


class NaverEcoHK(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_ecohk'


class NaverLiter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_liter'


class NaverChurch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_church'


class NaverObuddh(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_obuddh'


class NaverReligion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_religion'


class NaverSaju(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_saju'

class NaverMediSeoul(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_mediseoul'


class NaverMedirare(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term
    class Meta:
        managed = True
        db_table = 'naver_medirare'


class NaverNurse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_nurse'

class NaverMediShort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_medishort'


class NaverMediBody(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_medibody'


class NaverDisease(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_disease'


class NaverPharmacy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_pharmacy'

class NaverDrug(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_drug'

class NaverMarine(models.Model):
    id = models.BigIntegerField(primary_key=True)
    term = models.TextField(blank=True, null=True)
    eng = models.TextField(blank=True, null=True)
    simple_sense = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        managed = True
        db_table = 'naver_marine'


class MirrorArch(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_arch'


class MirrorLim(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_lim'

class MirrorEdu(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_edu'


class MirrorLiter(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_liter'


class MirrorVisualArt(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_visualart'


class MirrorFolk(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_folk'

class MirrorSocialPo(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_socialpo'


class MirrorBio(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_bio'

class MirrorHeat(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_heat'


class MirrorMedi(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_medi'


class MirrorMovie(models.Model):
    entry = models.TextField(blank=True, null=True)
    hanJa = models.TextField(blank=True, null=True)
    metaTerm1 = models.TextField(blank=True, null=True)
    metaTerm2 = models.TextField(blank=True, null=True)
    metaTerm3 = models.TextField(blank=True, null=True)
    simpleEx = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.entry

    class Meta:
        managed = True
        db_table = 'mirror_movie'


class Sources(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    publisher = models.CharField(max_length=200)
    code = models.TextField(blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    sum = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'sources'
