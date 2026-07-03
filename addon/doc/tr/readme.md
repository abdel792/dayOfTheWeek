# Haftanın Günü #

* Geliştiriciler: Abdel, Noelia.

Bu eklenti, seçilen bir tarihe karşılık gelen haftanın gününü bulmanızı sağlar.

NVDA "Araçlar" menüsüne, 2 öğe içeren "Haftanın Günü" adında bir alt menü ekler:

* "Bir gün ara" adlı ilki, 3 kontrolden oluşan bir iletişim kutusu açar:

    * Tarihinizi seçmek veya yazmak için bir liste kutusu;
    * Gününüzü içeren bir mesaj kutusu görüntülemek için bir "Tamam" düğmesi;
    * İletişim kutusunu kapatmak için bir "İptal" düğmesi.

* "dayOfTheWeek eklentisi ayarları" adlı ikincisi, tarih alanları için etiketlerin seslendirilip seslendirilmeyeceğini belirtmek üzere eklenti parametrelerini açar ve aşağıdaki öğelerden oluşur:

    * Tarih seçici erişilebilirliğini etkinleştir;
    * Etiketlerin seslendirilme düzeyi, bu durumda 3 seçeneğiniz olacaktır:

        * Uzun (bu varsayılan seçimdir);
        * Kısa (kısa duyurular için);
        * Kapalı (etiket seslendirmelerini devre dışı bırakmak için).

    * Dikey olarak hareket ederken yalnızca geçerli tarih alanı değerinin seslendirilmesini etkinleştir;
    * Yapılandırmanızı kaydetmek için bir "Tamam" düğmesi;
    * İptal etmek ve iletişim kutusunu kapatmak için bir "İptal" düğmesi.

## Notlar ##

* Bu iletişim kutularını sadece Escape tuşuna basarak kapatabilirsiniz;
* "Girdi hareketleri" menüsünden ve daha kesin olarak "Haftanın Günü" kategorisinden bu iletişim kutularını açmak için bir kısayol atayabilirsiniz;
* NVDA 2018.2 veya sonraki bir sürümünü kullanıyorsanız, araçlar menüsünde gününüzü aramak için yalnızca bir öğe bulacaksınız, eklenti ayarları ise NVDA ayarlar panelinde olacaktır.

## Uyumluluk ##

* Bu eklenti, 2019.3 ve sonraki NVDA sürümleriyle uyumludur.

## 20240326.0.0 Sürümündeki Değişiklikler

* nvda-2024.1 uyumluluğu güncellendi.;
* İndirme bağlantısı readme dosyasından silindi, gelecekteki güncellemeler için indirme bağlantısı artık yalnızca eklenti mağazasından edinilebilir olacak.

## 20231229.0.0 Sürümündeki Değişiklikler ##

* Yakında nvda-2024.1 ile sunulacak olan isteğe bağlı konuşma modunu desteklemek için geriye dönük uyumlu bir uygulama eklendi.

## 20231015.0.0 Sürümündeki Değişiklikler ##

* NVDA'nın en son sürümlerinde tarih seçiciden yukarı okla gezinirken tespit edilen bir hata düzeltildi.

## 20230728.0.0 Sürümündeki Değişiklikler ##

* Kod üzerinde flake8 ve mypy kuralları uygulandı;
* Desteklenen minimum NVDA sürümü, Python 3'te sunulan ek açıklamaları desteklemek için 2019.3 olarak değiştirildi.

## 20230607.0.0 Sürümündeki Değişiklikler ##

* Aşağıdaki iş akışları (workflows) eklendi:
 * auto-update-translations - NVDA çeviri sisteminden çevirileri otomatik olarak güncellemek için.
 * release-on-tag..yaml: yeni bir etiket gönderilir gönderilmez eklentiyi derlemek ve yayınlamak için;
 * manual-release.yaml: eklentinin yeni sürümlerini manuel olarak derlemek ve yayınlamak için.
* Çeviriler güncellendi.

## 20230508.0.0 ve Sonraki Sürümlerdeki Değişiklikler ##

* • Sürüm numarası, minimum NVDA sürümü ve indirme bağlantısı mağaza kurallarına/gereksinimlerine göre değiştirildi.

## 19.02 Sürümündeki Değişiklikler ##

* Sürüm numaralandırması YY.AA (2 haneli yıl, ardından bir nokta, ardından 2 haneli ay) kullanacak şekilde değiştirildi;
* nvda 2019.1 sürümünden beri çıkan yeni eklenti sürümü formatıyla uyumluluk eklendi.

## 6.0 Sürümündeki Değişiklikler ##

* NVDA 2018.2 ve üzeri için NVDA ayarlar paneline eklenti ayarları eklendi;
* Bir gün arama öğesi araçlar menüsüne taşındı;
* Ayarlar panelini içeren 2018.2 sürümünden önceki NVDA sürümleriyle eklentinin geriye dönük uyumluluğu eklendi.

## 5.0 Sürümündeki Değişiklikler ##

* Eklentinin wxPython 4.0 ve Python3 ile uyumluluğu eklendi;
* ASCII olmayan karakterler içeren eklenti yollarıyla ilgili bir hata düzeltildi.

## 4.0 Sürümündeki Değişiklikler ##

* Eklenti artık kullanıcının seçebileceği tüm bölgesel tarih formatlarını tanıyabilir hale geldi;
* gui.guiHelper modülünü içeren 2016.4 sürümünden önceki NVDA sürümleriyle eklentinin geriye dönük uyumluluğu eklendi.

## 3.1 Sürümündeki Değişiklikler ##

* Daha fazla dilin tanınmasını sağladığı için haftanın günü için önceki formata geri dönüldü;
* 'Gün', 'Ay' ve 'Yıl' olmak üzere 3 alanın ve bunların ilgili değerlerinin tanınmasıyla tarih seçicinin erişilebilirliği iyileştirildi;
* Haftanın günlerini tanımak için Gürcü dilinin entegrasyonuna yönelik bir teknik eklendi;
* Tarih seçicinin erişilebilirliğini etkinleştirmek veya devre dışı bırakmak için bir yapılandırma iletişim kutusu eklendi;
* Eklentinin alt menüsü "Araçlar" menüsünden "Tercihler" menüsüne taşındı;
* Eklenti kategorisi "Haftanın Günü" olarak değiştirildi.

## 2.0 Sürümündeki Değişiklikler ##

* Bir tarih isteyen iletişim kutusunun doğru görünümünü sağlamak için gui.guiHelper modülü kullanıldı;
* Eklentiye GPL lisansı eklendi;
* Eklentinin farklı dillerde düzgün çalışması için haftanın günleri çevrildi;
* Kodlama hatalarını önlemek için gün formatı değiştirildi.

## 1.0 Sürümündeki Değişiklikler ##

* İlk sürüm.
