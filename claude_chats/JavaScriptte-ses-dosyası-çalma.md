# JavaScript'te ses dosyası çalma

- Source: https://claude.ai/share/c0194ac5-ff68-4099-9dc6-e0b988080cfe
- Author: Sacid
- Created: 2026-05-15
- Messages: 4

---

## Human

Javascriptte bir ses dosyasını nasil çalarım ? Bir ses nasil calar  ?

---

## Assistant

JavaScript'te ses çalmanın birkaç yolu var. En basitinden başlayıp daha gelişmiş yöntemlere doğru gidelim.

## 1. En basit yöntem: `Audio` constructor

```javascript
const ses = new Audio('ses-dosyasi.mp3');
ses.play();
```

Bu kadar. `Audio` nesnesi oluşturuyorsun, `play()` çağırıyorsun. Dosya yolu yerine bir URL de verebilirsin (örneğin `'https://example.com/ses.mp3'`).

## 2. HTML'deki `<audio>` elementini kullanmak

HTML tarafında:
```html
<audio id="muzik" src="ses-dosyasi.mp3"></audio>
<button onclick="calSesi()">Çal</button>
```

JavaScript tarafında:
```javascript
function calSesi() {
  const ses = document.getElementById('muzik');
  ses.play();
}
```

Bu yöntem, kullanıcıya görünür kontroller (play/pause/volume) göstermek istersen `<audio controls>` ile çok kullanışlı olur.

## Önemli kontrol metotları ve özellikler

```javascript
const ses = new Audio('dosya.mp3');

ses.play();           // Çal
ses.pause();          // Duraklat
ses.currentTime = 0;  // Başa sar (saniye cinsinden)
ses.volume = 0.5;     // Ses seviyesi (0.0 - 1.0)
ses.loop = true;      // Sürekli tekrar
ses.playbackRate = 2; // Hız (2 = iki kat hızlı)

// Olaylar (events)
ses.addEventListener('ended', () => {
  console.log('Ses bitti');
});

ses.addEventListener('loadeddata', () => {
  console.log('Ses yüklendi, süresi:', ses.duration);
});
```

## Dikkat edilmesi gereken bir şey: Autoplay politikası

Modern tarayıcılar, **kullanıcı sayfayla etkileşime girmeden** (tıklama, tuş basma vs.) ses çalmana izin vermez. Yani sayfa yüklenir yüklenmez `play()` çağırırsan büyük ihtimalle hata alırsın:

```javascript
ses.play().catch(err => {
  console.log('Tarayıcı izin vermedi:', err);
});
```

`play()` aslında bir Promise döndürür, bu yüzden hatayı yakalamak iyi bir alışkanlık.

## 3. Web Audio API (gelişmiş kullanım)

Oyun yapıyorsan, ses efektleri üst üste binecekse veya frekans manipülasyonu, eko gibi efektler istiyorsan `Audio` yetmez. O zaman Web Audio API'ye bakman gerekir:

```javascript
const audioContext = new AudioContext();

fetch('ses.mp3')
  .then(res => res.arrayBuffer())
  .then(buffer => audioContext.decodeAudioData(buffer))
  .then(decodedData => {
    const source = audioContext.createBufferSource();
    source.buffer = decodedData;
    source.connect(audioContext.destination);
    source.start();
  });
</n>
```

Bu yöntem daha karmaşık ama çok daha güçlü — düşük gecikme, aynı sesi onlarca kez üst üste çalabilme, filtre/efekt ekleyebilme gibi avantajları var.

## Hangisini kullanmalısın?

Basit bir ses çalmak (bildirim sesi, kısa efekt, müzik) için `new Audio()` fazlasıyla yeter. Sadece oyun veya ses uygulaması yapıyorsan Web Audio API'ye geçmen gerekir.

Ne tür bir proje üzerinde çalışıyorsun? Ona göre daha spesifik örnek verebilirim.

---

## Human

Sadece Audio var üst üste binecekse ? Audio API kullanmak istemiyorum

---

## Assistant

İyi soru. `Audio` ile de üst üste bindirebilirsin, ama bir tuzağı var:

## Tuzak: Aynı `Audio` nesnesini tekrar `play()` etmek

```javascript
const ses = new Audio('patlama.mp3');

ses.play();
ses.play(); // Bu üst üste binmez! İlkini durdurup baştan başlatır.
```

Aynı nesneyi tekrar çalmak ses üst üste bindirmez — sadece o sesin pozisyonunu etkiler.

## Çözüm 1: Her seferinde yeni `Audio` nesnesi oluştur

```javascript
function sesCal() {
  const ses = new Audio('patlama.mp3');
  ses.play();
}

sesCal();
sesCal();
sesCal(); // Üçü de aynı anda çalar, üst üste biner
```

Bu yöntem en basitidir. Tarayıcı dosyayı cache'lediği için her seferinde yeniden indirmez, sadece yeni bir oynatma örneği oluşturur.

## Çözüm 2: `cloneNode()` ile klonla

Tek bir kaynak `Audio` nesnesi tut, çalmak istediğinde klonla:

```javascript
const sesKaynak = new Audio('patlama.mp3');

function sesCal() {
  const klon = sesKaynak.cloneNode();
  klon.play();
}

sesCal();
sesCal(); // Üst üste biner
```

`cloneNode()` aynı `src`'ye sahip yeni bir element döndürür. Sonuç olarak Çözüm 1 ile pratikte çok benzer.

## Çözüm 3: Ses havuzu (sound pool) — oyunlar için ideal

Çok sık çalınan sesler için her defasında yeni nesne yaratmak yerine, önceden bir havuz oluşturup sırayla kullanmak daha verimli:

```javascript
class SesHavuzu {
  constructor(url, boyut = 5) {
    this.havuz = [];
    for (let i = 0; i < boyut; i++) {
      this.havuz.push(new Audio(url));
    }
    this.indeks = 0;
  }

  cal() {
    const ses = this.havuz[this.indeks];
    ses.currentTime = 0; // Başa sar (eğer hâlâ çalıyorsa)
    ses.play();
    this.indeks = (this.indeks + 1) % this.havuz.length;
  }
}

// Kullanım
const patlamaSesi = new SesHavuzu('patlama.mp3', 5);

patlamaSesi.cal();
patlamaSesi.cal();
patlamaSesi.cal(); // 5 ses üst üste binebilir, sonra döner başa
```

Bu yöntemde 5 tane `Audio` nesnesi var, sırayla kullanılıyorlar. 6. çağrıda 1. nesne tekrar kullanılır (`currentTime = 0` ile başa sarılarak). Oyunlarda mermi sesi, ayak sesi gibi sık tetiklenen efektler için çok yaygın bir desen.

## Pratik tavsiye

- **Seyrek çalan sesler** için (örneğin bir butona basınca tık sesi): Çözüm 1 yeterli, fazla düşünme.
- **Çok sık tetiklenen sesler** için (oyunlarda mermi, çarpışma): Çözüm 3 (havuz) daha temiz çalışır, çünkü sürekli yeni nesne oluşturup çöpe atmak GC (garbage collection) yükü yaratabilir.

Hangi senaryoda kullanacağını söylersen, sana en uygun yapıyı birlikte yazabiliriz.
