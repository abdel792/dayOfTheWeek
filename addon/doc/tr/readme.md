# Bu Tarih Hangi Gün #

* Yazarlar: Abdel, Noelia.
* [Kararlı Sürümü İndir][1]
* [Geliştirici sürümünü indir][2]

Bu eklenti, herhangi bir tarihin haftanın hangi gününe denk geldiğini bulmanıza yarar.

NVDA araçlar menüsüne iki öğe içeren Bu tarih hangi gün altmenüsü ekler:

* Birinci öğe olan "Gün ara" öğesi 3 denetimden oluşan bir iletişim kutusu açar:

    * İstediğiniz tarihi seçebileceğiniz veya yazabileceğiniz bir seçim kutusu;
    * Seçtiğiniz tarihe denk gelen günü gösteren bir mesaj kutusu açan "tamam" düğmesi;
    * İletişim kutusunu kapatmaya yarayan "iptal" düğmesi.

* İkinci öğe olan "Bu tarih hangi gün eklenti ayarları" öğesi, eklenti ayarlarını açar. Bu iletişim kutusundan tarih alanlarının etiketlerinin söylenip söylenmeyeceğini ayarlayabilirsiniz. İletişim kutusunda şu öğeler bulunur:

    * Tarih seçicinin erişilebilirliğini etkinleştir;
    * Etiket duyuru seviyesi, 3 öğe içerir:

        * Uzun (varsayılan seçenektir);
        * Kısa (etiketlerin kısa biçimde söylenmesi için);
        * Kapalı (etiket duyurularını devredışı bırakmak için).

    * Sadece üzerinde bulunulan tarih alanının değeri okunsun, dikey dolaşım yaparken kullanılır;
    * Ayarları kaydetmeye yarayan "tamam" düğmesi;
    * Ayarlamayı iptal etmeye ve iletişim kutusunu kapatmaya yarayan "iptal" düğmesi.

## Notlar ##

* İletişim kutularını escape tuşuna basarak kapatabilirsiniz;
* İletişim kutularını açmak için "girdi hareketleri" iletişim kutusunun "haftanın günleri" kategorisinden kısayol tuşları ayarlayabilirsiniz;
* NVDA 2018.2 veya üzeri sürümlerini kullanıyorsanız araçlar menüsünde sadece bir öğe görünür, bu öğe istediğiniz tarihin hangi güne denk geldiğini görmenizi sağlar. Eklenti ayarları NVDA ayarları iletişim kutusunda bulunur.

## Uyumluluk ##

* Bu eklenti, NVDA'nın 2019.3 ve sonrası sürümleriyle uyumludur.

## 20231015.0.0 için değişiklikler ##

* NVDA'nın en son sürümlerinde tarih seçicide yukarı okla gezinirken tespit edilen bir hata düzeltildi.

## 20230728.0.0 için değişiklikler ##

* Flake8 ve mypy kuralları koda uygulandı;
* Python 3'te tanıtılan ek açıklamaları desteklemek için desteklenen minimum NVDA sürümü 2019.3 olarak değiştirildi.

## 20230607.0.0 için değişiklikler ##

* Aşağıdaki iş akışları eklendi:
 * auto-update-translations - NVDA'nın çeviri sisteminden çevirileri otomatik olarak güncellemek için.
 * release-on-tag..yaml: yeni bir etiket gönderilir gönderilmez eklentiyi oluşturmak ve yayınlamak;
 * manual-release.yaml: Eklentinin yeni sürümlerini el ile derlemek ve yayınlamak için.
* Güncellenmiş Çeviriler.

## 20230508.0.0 için değişiklikler ##

* • Mağaza kurallarına/gereksinimlerine göre sürüm numarası, minimum NVDA sürümü ve indirme bağlantısı değiştirildi.

## 19.02 için değişiklikler ##

* Sürüm biçimi yy.aa (iki rakam ile yıl, nokta, iki rakam ile ay) olarak değiştirildi;
* NVDA 2019.1 sürümünden itibaren kullanılmaya başlanan eklenti sürüm biçimiyle uyumluluk sağlandı.

## 6.0 için değişiklikler ##

* eklenti ayarları NVDA 2018.2 ve üzeri sürümlerde NVDA ayarlar paneline eklendi;
* Gün aramak için kullanılan menü öğesi araçlar menüsüne taşındı;
* Eklenti NVDA 2018.2 sürümünden önceki sürümler için uyumlu hâle getirildi. Ayarlar iletişim kutusu için de uyumluluk sağlandı.

## 5.0 için değişiklikler ##

* Eklenti wxPython 4.0 ve Python3 ile uyumlu hâle getirildi;
* ASCII olmayan karakterler içeren eklenti dizinleriyle ilgili bir sorun düzeltildi.

## 4.0 için değişiklikler ##

* Eklenti kullanıcının seçebileceği tüm bölgesel tarih biçimlerini tanıyor;
* Eklenti NVDA 2016.4 sürümünden önceki sürümler için uyumlu hâle getirildi. Gui.guiHelper modülü de uyumlu hâle getirildi.

## 3.1 için değişiklikler ##

* Daha fazla sayıda dil tanınabildiği için haftanın günlerinde eski biçime dönüldü;
* Tarih seçicinin erişilebilirliği, "gün", "ay" ve "yıl" alanları ve onların değerlerinin okunması konusunda geliştirildi;
* Gürcüce haftanın günlerini tanımak için bir teknik eklendi;
* Tarih seçicinin erişilebilirliğini etkinleştirmek veya devredışı bırakmak için ayarlar iletişim kutusu eklendi;
* Eklenti altmenüsü "araçlar" menüsünden "tercihler" menüsüne taşındı;
* Eklenti kategorisi Bu tarih hangi gün olarak değiştirildi.

## 2.0 için değişiklikler ##

* Tarih iletişim kutusunun düzgün görünmesi için gui.guiHelper modülü kullanıldı;
* Eklentiye GPL lisansı eklendi;
* Günler, eklentinin farklı dillerde düzgün çalışabilmesi için çevrildi;
* Kodlama hatalarını gidermek için gün biçimi değiştirildi.

## 1.0 için değişiklikler ##

* İlk Sürüm.

[1]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek

[2]: https://www.nvaccess.org/addonStore/legacy?file=dayOfTheWeek
