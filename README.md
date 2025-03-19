# Metro_Simulation

#  Ankara Metro Ağı Projesi

Bu proje, Ankara'daki metro ağını simüle eden ve çeşitli metro güzergahı bulma algoritmalarını içeren bir Python uygulamasıdır.


# 🚇 Ankara Metro Ağı Projesi

Bu proje, Ankara'daki metro ağını simüle eden ve çeşitli metro güzergahı bulma algoritmalarını içeren bir Python uygulamasıdır.

---

## 📌 Başlarken

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

### 1️⃣ Depoyu Klonlayın:

```bash
git clone https://github.com/KullaniciAdiniz/metro-agi.git
cd metro-agi
```

### 2️⃣ Gerekli Kütüphaneleri Yükleyin:

```bash
pip install rich networkx matplotlib
```

### 3️⃣ Uygulamayı Çalıştırın:

```bash
python metro_agi.py
```

---

## 📂 Proje Yapısı

Bu proje, Python kullanarak bir metro ağı simülasyonu oluşturan bir sistemdir. Metro istasyonlarını, hatları, bağlantıları ve en hızlı/az aktarmalı rotaları bulma fonksiyonlarını içerir. Ayrıca, metro yoğunluk verilerini rastgele belirleyerek görselleştirme yapabilir.

### 🚀 Özellikler

✅ Metro istasyonlarını tanımlama ve hatlara ekleme  
✅ İstasyonlar arasında bağlantı kurma (süre bazlı bağlantılar)  
✅ En az aktarma ile en kısa rotayı bulma  
✅ En hızlı rotayı hesaplama (süre bazlı)  
✅ Metro ağının grafiksel olarak görselleştirilmesi  
✅ Yoğunluk durumlarını takip etme ve rastgele atama  
✅ Dil ve bölge desteği (Şu an için Türkçe ve İngilizce)  

---

## 🏃‍♂️ Kurulum ve Çalıştırma

### 📥 Gerekli Kütüphaneler

Proje için aşağıdaki kütüphanelere ihtiyacınız var:

```bash
pip install rich matplotlib networkx
```

### 🏃‍♂️ Çalıştırma

Python dosyanızı çalıştırmak için:

```bash
python metro_agi.py
```

---

## 📜 Kullanım

Metro ağı oluşturduktan sonra, istasyon ekleyebilir, bağlantılar kurabilir ve en hızlı veya en az aktarmalı rotaları bulabilirsiniz.

### 🔹 Örnek Kullanım

**Bir istasyon ekleme:**

```python
metro_agi.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
```

**İki istasyon arasında bağlantı kurma:**

```python
metro_agi.baglanti_ekle("K1", "K2", 4)  # Kızılay ile Ulus arasında 4 dakika
```

**En az aktarma ile bir rota bulma:**

```python
rota = metro_agi.en_az_aktarma_bul("M1", "K4")
```

**En hızlı rota bulma:**

```python
rota, sure = metro_agi.en_hizli_rota_bul("M1", "K4")
```

**Yoğunluk durumlarını rastgele oluşturma:**

```python
metro_agi.dinamik_yogunluk_ekle()
```

**Metro ağını görselleştirme:**

```python
metro_agini_gorsellestir(metro_agi)
```

---

## 📊 Metro Ağı Görselleştirme

Metro hattı ve istasyonlar `networkx` ve `matplotlib` kütüphaneleri ile grafiksel olarak çizilir.

📌 **Örnek Görsel:**

🟢 Yeşil noktalar: Yoğun olmayan istasyonlar  
🔴 Kırmızı noktalar: Yoğun istasyonlar  

Metro Ağı Görselleştirme = (https://github.com/user-attachments/assets/84eab39c-c5ec-4d3f-b29f-dda879a9f639)

---

## 🛠 Geliştirme ve Katkıda Bulunma

Projeye katkıda bulunmak isterseniz **pull request** gönderebilir veya **issue** açabilirsiniz. 🚀

### ✅ Yapılacaklar:

- 📌 Daha fazla dil desteği ekleme
- 📌 Gerçek zamanlı yoğunluk verisi ekleme
- 📌 Kullanıcıdan istasyon girişini alarak interaktif yapı oluşturma

👨‍💻 **Geliştirici:** [Oğuzhan Yazıcı]

🚀 Eğer projeyi beğendiysen **⭐ vererek** destek olabilirsin!

