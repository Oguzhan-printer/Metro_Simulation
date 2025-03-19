import random
from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import datetime
import matplotlib.pyplot as plt
import networkx as nx

console = Console()

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []
        self.yogunluk: Dict[str, bool] = {}

    def __str__(self):
        return self.ad

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

    def yogunluk_ekle(self, saat: str, durum: bool):
        self.yogunluk[saat] = durum

    def __lt__(self, other: 'Istasyon') -> bool:
       # Burada, `Istasyon`'lar arasındaki sıralamayı belirleyebilirsiniz.
       # Örneğin, 'idx' (istasyonun ID'si) ile karşılaştırabiliriz.
       return self.idx < other.idx    


class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:  
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        kuyruk = deque([(self.istasyonlar[baslangic_id], [])])
        ziyaret_edildi = set()
        
        while kuyruk:
            istasyon, yol = kuyruk.popleft()
            
            if istasyon.idx in ziyaret_edildi:
                continue
            
            yeni_yol = yol + [istasyon]
            if istasyon.idx == hedef_id:
                return yeni_yol
            
            ziyaret_edildi.add(istasyon.idx)
            
            for komsu, _ in istasyon.komsular:
                if komsu.idx not in ziyaret_edildi:
                    kuyruk.append((komsu, yeni_yol))
        
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:  
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        pq = [(0, self.istasyonlar[baslangic_id], [])]
        ziyaret_edildi = set()
        
        while pq:
            sure, istasyon, yol = heapq.heappop(pq)
            
            if istasyon.idx in ziyaret_edildi:
                continue
            
            yeni_yol = yol + [istasyon]
            if istasyon.idx == hedef_id:
                return yeni_yol, sure
            
            ziyaret_edildi.add(istasyon.idx)
            
            for komsu, gecikme in istasyon.komsular:
                if komsu.idx not in ziyaret_edildi:
                    heapq.heappush(pq, (sure + gecikme, komsu, yeni_yol))
        
        return None

    def dil_ve_bolge_desteği(self, dil: str = "tr", bolge: str = "Genel") -> str:
        if dil == "tr":
            return f"Metro Ağı - {bolge} Bölgesi"
        elif dil == "en":
            return f"Metro Network - {bolge} Area"
        else:
            return "Bölge Desteği Bulunamadı"

    def yogunluk_durumu(self, saat: str) -> str:
        for istasyon in self.istasyonlar.values():
            durum = istasyon.yogunluk.get(saat, False)
            durum_str = "Yoğun" if durum else "Yoğun Değil"
            console.print(f"{istasyon.ad} - {saat}: {durum_str}", style="bold yellow")

    def dinamik_yogunluk_ekle(self):
        for istasyon in self.istasyonlar.values():
            for hour in range(0, 24):
                saat = f"{hour:02d}:00"
                durum = random.choice([True, False])  # Yoğun ya da değil
                istasyon.yogunluk_ekle(saat, durum)

def senaryo_testi(metro_agi: MetroAgi):
    console.print("[bold cyan]Senaryolar Test Ediliyor[/bold cyan]", justify="center")

    # AŞTİ -> OSB
    console.print("\n1. AŞTİ'den OSB'ye:")
    rota = metro_agi.en_az_aktarma_bul("M1", "K4")
    if rota:
        console.print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota), style="bold green")
    else:
        console.print("Böyle bir rota bulunamadı.", style="bold red")
    
    sonuc = metro_agi.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        console.print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota), style="bold green")
    else:
        console.print("Böyle bir rota bulunamadı.", style="bold red")
    
    # Batıkent -> Keçiören
    console.print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro_agi.en_az_aktarma_bul("T1", "T4")
    if rota:
        console.print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota), style="bold green")
    else:
        console.print("Böyle bir rota bulunamadı.", style="bold red")
    
    sonuc = metro_agi.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        console.print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota), style="bold green")
    else:
        console.print("Böyle bir rota bulunamadı.", style="bold red")

    # Keçiören -> AŞTİ
    console.print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro_agi.en_az_aktarma_bul("T4", "M1")
    if rota:
        console.print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota), style="bold green")
    else:
        console.print("Böyle bir rota bulunamadı.", style="bold red")
    
    sonuc = metro_agi.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        console.print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota), style="bold green")
    else:
        console.print("Böyle bir rota bulunamadı.", style="bold red")

def metro_agini_gorsellestir(metro_agi: MetroAgi):
    G = nx.Graph()

    # İstasyonları grafiğe ekliyoruz
    for istasyon in metro_agi.istasyonlar.values():
        G.add_node(istasyon.idx, label=istasyon.ad, hat=istasyon.hat)

    # Bağlantıları grafiğe ekliyoruz
    for istasyon in metro_agi.istasyonlar.values():
        for komsu, sure in istasyon.komsular:
            G.add_edge(istasyon.idx, komsu.idx, weight=sure)

    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    for istasyon in metro_agi.istasyonlar.values():
        for saat, durum in istasyon.yogunluk.items():
            color = 'red' if durum else 'green'
            nx.draw_networkx_nodes(G, pos, nodelist=[istasyon.idx], node_color=color, node_size=3000, alpha=0.6)

        plt.title("Metro Ağı Görselleştirmesi")
    plt.axis('off')
    plt.show()

# Metro ağı kuruyoruz ve istasyonları ekliyoruz
metro_agi = MetroAgi()

# İstasyonları ekleyelim
metro_agi.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
metro_agi.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
metro_agi.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
metro_agi.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

metro_agi.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
metro_agi.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
metro_agi.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
metro_agi.istasyon_ekle("M4", "Gar", "Mavi Hat")

metro_agi.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
metro_agi.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
metro_agi.istasyon_ekle("T3", "Gar", "Turuncu Hat")
metro_agi.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

# Bağlantıları ekleyelim
metro_agi.baglanti_ekle("K1", "K2", 4)
metro_agi.baglanti_ekle("K2", "K3", 6)
metro_agi.baglanti_ekle("K3", "K4", 8)

metro_agi.baglanti_ekle("M1", "M2", 5)
metro_agi.baglanti_ekle("M2", "M3", 3)
metro_agi.baglanti_ekle("M3", "M4", 4)

metro_agi.baglanti_ekle("T1", "T2", 7)
metro_agi.baglanti_ekle("T2", "T3", 9)
metro_agi.baglanti_ekle("T3", "T4", 5)

metro_agi.baglanti_ekle("K1", "M2", 2)
metro_agi.baglanti_ekle("K3", "T2", 3)
metro_agi.baglanti_ekle("M4", "T3", 2)

# Yoğunlukları ekleyelim
metro_agi.istasyonlar["K1"].yogunluk_ekle("08:00", True)
metro_agi.istasyonlar["K1"].yogunluk_ekle("17:00", True)

# Dinamik yoğunluk ekleme
metro_agi.dinamik_yogunluk_ekle()

# Senaryo testini başlatalım
senaryo_testi(metro_agi)

# Metro ağını görselleştirelim
metro_agini_gorsellestir(metro_agi)

