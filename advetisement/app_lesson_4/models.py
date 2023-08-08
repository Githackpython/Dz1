from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
class Advetisement(models.Model):
    title=models.CharField(verbose_name="название",max_length=128)
    desc=models.TextField('описание')
    price=models.DecimalField('цена',max_digits=10,decimal_places=2)
    torg=models.BooleanField('торг',help_text='возможен ли торг')
    ca=models.DateField(auto_now_add=True)
    ua=models.DateField(auto_now=True)
    class Meta:
        db_table="Advertisements"
    def __str__(self):
        return f'Advertisements(id={self.id},title={self.title},price={self.price})'
    @admin.display(description='дата создания')
    def cdate(self):
        if self.create_at.date()==timezone.now().date():
            ctime=self.create_at.time().strftime('%H:%M%:%S')
            return format_html(
                '<span style="color:green;font-weight:bold;>"Сегодня в {}</span>',ctime
            )
        return self.create_at.strftime('%d.%m.%Y')
    def udate(self):
        if self.updated_at.date()==timezone.now().date():
            utime=self.updated_at.time().strftime('%H:%M%:%S')
            return format_html(
                '<span style="color:blue;font-weight:bold;>"Обновлено сегодня в {}</span>',utime
            )
        return self.updated_at.strftime('%d.%m.%Y')
