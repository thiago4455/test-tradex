from django.db import models
from django.core.validators import RegexValidator, ValidationError

class Product(models.Model):
    ean = models.CharField(max_length=13, verbose_name='EAN', primary_key=True, validators=[RegexValidator(
                           regex='^.{13}$', message='O Ean deve conter 13 caracteres')])
    name = models.TextField(verbose_name='Nome do Produto')
    image = models.ImageField(null=True, blank=True, verbose_name='Imagem do produto', upload_to='imagens')
    min_price = models.DecimalField(verbose_name=u'Preço mínimo', decimal_places=2, default=0.0, max_digits=8)
    max_price = models.DecimalField(verbose_name=u'Preço máximo', decimal_places=2, default=0.0, max_digits=8)

    class Meta:
        verbose_name = u"Produto"
        verbose_name_plural = u"Produtos"

    def __str__(self):
        return f"{self.name} - {self.ean}"

    def prices(self):
        return Price.objects.filter(product=self)

    

class Price(models.Model):
    product = models.ForeignKey(Product, verbose_name='Produto', related_name='pricing', on_delete=models.CASCADE, null=True,
                              blank=True)
    price = models.DecimalField(verbose_name=u'Preço (R$)', decimal_places=2, default=0.0, max_digits=8)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"Produto - Configuração de preço"
        verbose_name_plural = u"Produtos - Configurações de preço"

    def __str__(self):
        return f"{self.product.name} - R$ {self.price}"

    def clean(self):
        if self.price > self.product.max_price:
            raise ValidationError("Valor acima do preço máximo")
        if self.price < self.product.min_price:
            raise ValidationError("Valor abaixo do preço mínimo")