class RecyclingBot:
    def _init_(self):
        # Geri dönüştürülebilir materyallerin ayrışma süreleri (yıl olarak)
        self.material_times = {
            "plastic": 450,
            "glass": 1000,
            "paper": 2,
            "aluminum": 200,
            "tin_can": 50,
            "rubber_tire": 80,
            "cardboard": 2
            ""
        }
    
    def get_recycling_time(self, material):
        # Materyalin ayrışma süresini döndürür
        material = material.lower()  # Kullanıcı girişi küçük harfe dönüştürülür
        if material in self.material_times:
            years = self.material_times[material]
            return f"{material.capitalize()} yaklaşık olarak {years} yılda ayrışır."
        else:
            return "Bu materyal hakkında bilgi bulunamadı. Lütfen başka bir materyal girin."
    
# Botu başlatma
bot = RecyclingBot()

# Kullanıcıdan geri dönüştürülen materyali alalım
material = input("Geri dönüştürdüğünüz materyali girin: ")

# Botun sonucu döndürmesi
response = bot.get_recycling_time(material)
print(response)

 bot.run("bot token buraya!")
