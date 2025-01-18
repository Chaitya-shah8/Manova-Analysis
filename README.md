# Cardiac-Data-Analysis-Exploring-Cholesterol-and-Heart-Rate

![heart attack](https://github.com/user-attachments/assets/6d3ee5c8-aab0-4248-90bc-195d873ddb7d)

Kalp hastalığı veri seti üzerinde çoklu değişkenli analizler yapmayı amaçlamaktadır. Veri seti, hastaların çeşitli sağlık bilgilerini içermektedir ve burada kullanılan ana değişkenler "chol" (kolesterol) ve "thalach" (maksimum kalp hızı) ile "cp" (göğüs ağrısı tipi) arasındaki ilişkiyi incelemektedir. 

Kalp hastalığı veri setinde, "chol" ve "thalach" değişkenlerinin, "cp" (göğüs ağrısı tipi) gruplarına göre nasıl değiştiğini inceleyen çoklu analizler içerir. Normallik testleri, aykırı değerlerin tespiti, korelasyon analizi, MANOVA testi ve post-hoc testler gibi çeşitli istatistiksel yöntemler kullanılmıştır. Ayrıca, modelin doğruluğunu değerlendirmek için varyans şişirme faktörü (VIF) analizi yapılmıştır.

1. Veri Yükleme ve Genel İnceleme:
pandas kütüphanesi ile veri seti yüklenir ve info() ile veri hakkında genel bilgi alınır. Ayrıca describe() fonksiyonu ile sayısal verilerin özet istatistikleri (ortalama, standart sapma vb.) görüntülenir.

2. Normallik Testi (Shapiro-Wilk Testi):
Kolesterol (chol) ve maksimum kalp hızı (thalach) için normallik testi yapılır. Bu test, verinin normal dağılıma uyup uymadığını kontrol eder. Histogramlar ile verilerin dağılımı görselleştirilir. Shapiro-Wilk testinin p-değeri kullanılarak verinin normal olup olmadığı hakkında bilgi verilir.

![shapiro_wilk](https://github.com/user-attachments/assets/98d49965-5dc6-4387-9f61-793d506819d6)

4. Aykırı Değerlerin Tespiti:
Aykırı değerler Z-skoru kullanılarak tespit edilir. Z-skoru 3'ten büyük olan değerler aykırı olarak kabul edilir. Aykırı değerlerin hangi gözlemler olduğunu ve aykırı değerleri çıkardıktan sonra verinin durumunu inceleriz.

5. Veriyi Temizleme:
Aykırı değerler çıkarıldıktan sonra Shapiro-Wilk testi tekrar uygulanır ve verinin normal dağılıma daha yakın olup olmadığı kontrol edilir.

6. Korelasyon Analizi:
Kolesterol ve maksimum kalp hızı arasındaki ilişkiyi anlamak için korelasyon matrisi hesaplanır. Korelasyon katsayısı ile iki değişken arasındaki doğrusal ilişkiyi belirleriz. Sonuçlar ısı haritası (heatmap) ile görselleştirilir.

![correlation](https://github.com/user-attachments/assets/dfd8a44b-8253-48de-ac41-6f35f604b632)

8. MANOVA (Çoklu Değişkenli Varyans Analizi):
MANOVA (Multivariate Analysis of Variance) testi, "chol" ve "thalach" değişkenlerinin, "cp" grubu tarafından etkilenip etkilenmediğini test etmek için yapılır. Bu test, iki bağımlı değişkenin (kolesterol ve maksimum kalp hızı) aynı anda "cp" (göğüs ağrısı tipi) bağımsız değişkenine göre nasıl değiştiğini analiz eder. MANOVA sonuçları özetlenir ve sonuçlar yazdırılır.

9. Post-hoc Testler (Tukey HSD):
MANOVA sonuçlarına göre, Tukey HSD (Honest Significant Difference) testi yapılır. Bu test, grup içindeki her bir değişkenin diğer gruplarla karşılaştırılmasını sağlar. Kolesterol değişkeni için Tukey testinin sonuçları görselleştirilir.

![Tukey HSD](https://github.com/user-attachments/assets/d98c6514-a785-4f0d-a8ce-e34ad099b2a1)

9. Varyans Şişirme Faktörü (VIF) Analizi:
Varyans Şişirme Faktörü (VIF), çoklu doğrusal regresyon analizlerinde bağımsız değişkenlerin birbirine ne kadar bağımlı olduğunu gösterir. Yüksek VIF değerleri, bağımsız değişkenler arasında çok güçlü bir korelasyon olduğunu ve multikollinearite (çoklu doğrusal ilişki) problemini işaret eder. VIF hesaplanır ve sonuçlar bar grafiğiyle görselleştirilir.

![VIF](https://github.com/user-attachments/assets/21e753f4-70c9-4098-88d8-466d1fc64b7e)

10. Boxplot Görselleştirmeleri:
Kolesterol ve maksimum kalp hızı için, her bir göğüs ağrısı tipi (cp) kategorisi için boxplotlar çizilir. Boxplotlar, verinin merkezi eğilimini, yayılmasını ve aykırı değerlerini gösterir.

![BOXPLOT](https://github.com/user-attachments/assets/734f4f28-6163-4a39-8742-effca27b5e69)
