# Amazon Ürün Bilgisi Çekme

Bu Python uygulaması, Amazon web sitesinde belirli bir anahtar kelime ile yapılan bir arama sonucu bulunan ürünlerin detaylı bilgilerini çekmek için kullanılır. 

## Kullanım

Öncelikle, Python'un ve aşağıdaki kütüphanelerin kurulu olduğundan emin olun:

- `requests`
- `beautifulsoup4`

Bunları yüklemek için aşağıdaki komutları kullanabilirsiniz:

pip install requests
pip install beautifulsoup4


Ardından, `amazon.py` dosyasını çalıştırabilirsiniz. Bu betik, Amazon web sitesinde "gaming laptop" anahtar kelimesiyle yapılan bir arama sonucunda bulunan ürünlerin detaylı bilgilerini çekecek ve bu bilgileri ekrana yazdıracaktır.

## Nasıl Çalışır

1. İlk olarak, `get_url` fonksiyonu, Amazon arama sonuçlarını çekmek için verilen URL'yi kullanır ve bu sonuçları bir listeye ekler.

2. Ardından, `descriptions` fonksiyonu, her bir ürünün ayrıntılarını çekmek için bu URL listesini kullanır. Her ürünün başlıkları ve değerleri, ürünün sayfasından çekilir ve ekrana yazdırılır.

## Dikkat Edilmesi Gerekenler

- Bu kod, web sitesi yapısındaki değişikliklere duyarlı olabilir ve güncellenmesi gerekebilir.



