# Metro_Simulation

#  Ankara Metro Ağı Projesi

Bu proje, Ankara'daki metro ağını simüle eden ve çeşitli metro güzergahı bulma algoritmalarını içeren bir Python uygulamasıdır.


##  Başlarken

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Depoyu klonlayın:**

    ```bash
    git clone [https://github.com/KullaniciAdiniz/metro-agi.git](https://www.google.com/search?q=https://github.com/KullaniciAdiniz/metro-agi.git)
    cd metro-agi
    ```

2.  **Gerekli kütüphaneleri yükleyin:**

    ```bash
    pip install rich networkx matplotlib
    ```

3.  **Uygulamayı çalıştırın:**

    ```bash
    python metro_agi.py
    ```



## ️ Proje Yapısı

🚇 Metro Ağı Simülasyonu

Bu proje, Python kullanarak bir metro ağı simülasyonu oluşturan bir sistemdir. Metro istasyonlarını, hatları, bağlantıları ve en hızlı/az aktarmalı rotaları bulma fonksiyonlarını içerir. Ayrıca, metro yoğunluk verilerini rastgele belirleyerek görselleştirme yapabilir.



📌 Özellikler

🛤 Metro istasyonlarını tanımlama ve hatlara ekleme

🔗 İstasyonlar arasında bağlantı kurma (süre bazlı bağlantılar)

🚆 En az aktarma ile en kısa rotayı bulma

⏳ En hızlı rotayı hesaplama (süre bazlı)

📊 Metro ağının grafiksel olarak görselleştirilmesi

🔴 Yoğunluk durumlarını takip etme ve rastgele atama

🌍 Dil ve bölge desteği (Şu an için Türkçe ve İngilizce desteği var)

🚀 Kurulum ve Çalıştırma

📥 Gerekli Kütüphaneler



Proje için aşağıdaki kütüphanelere ihtiyacınız var:

pip install rich matplotlib networkx

🏃‍♂️ Çalıştırma



Python dosyanızı çalıştırmak için:

python metro_agi.py


📜 Kullanım

Metro ağı oluşturduktan sonra, istasyon ekleyebilir, bağlantılar kurabilir ve en hızlı veya en az aktarmalı rotaları bulabilirsiniz.

🔹 Örnek Kullanım

Bir istasyon ekleme:

metro_agi.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")


İki istasyon arasında bağlantı kurma:

metro_agi.baglanti_ekle("K1", "K2", 4)  # Kızılay ile Ulus arasında 4 dakika


En az aktarma ile bir rota bulma:

rota = metro_agi.en_az_aktarma_bul("M1", "K4")


En hızlı rota bulma:

rota, sure = metro_agi.en_hizli_rota_bul("M1", "K4")


Yoğunluk durumlarını rastgele oluşturma:

metro_agi.dinamik_yogunluk_ekle()


Metro ağını görselleştirme:

metro_agini_gorsellestir(metro_agi)



📊 Metro Ağı Görselleştirme

Metro hattı ve istasyonlar networkx ve matplotlib kütüphaneleri ile grafiksel olarak çizilir.

Örnek Görsel:

🟢 Yeşil noktalar: Yoğun olmayan istasyonlar🔴 Kırmızı noktalar: Yoğun istasyonlar

 TASARIM = (https://github.com/user-attachments/assets/84eab39c-c5ec-4d3f-b29f-dda879a9f639)



🛠 Geliştirme ve Katkıda Bulunma

Projeye katkıda bulunmak isterseniz pull request gönderebilir veya issue açabilirsiniz. 🚀

Yapılacaklar:

📌 Daha fazla dil desteği

📌 Geliştirici: [Oğuzhan Yazıcı]

📌 Gerçek zamanlı yoğunluk verisi ekleme

📌 Kullanıcıdan istasyon girişini alarak interaktif yapı oluşturma

Eğer projeyi beğendiysen ⭐ vermeyi unutma!



