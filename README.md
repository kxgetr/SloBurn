# SloBurn

Başarısız istek oranını hedef hata bütçesiyle karşılaştırır.

## Girdi

requests, failures, target (örneğin 0.99).

## Kullanım

Python 3.11+, standart kütüphane.

```sh
python sloburn.py input.json
python verify.py
```

Dosya verilmezse stdin okunur. Sonuç stdout üzerinde JSON olarak yazılır. Girdi hatası çıkış kodu 2 üretir.

Örnek sonuç:

```json
2
```
