import time

print("Hoşgeldiniz Umarım Eğlenirsiniz her zaman bir çıkış yolunuz olduğunu unutmayın...")

time.sleep(1)
print("Büyük bir adadasınız ve bu adanın kendine has bir deneyimi olacaktır. Napıcağınıza karar vermeniz gerekiyor...")

time.sleep(3)
cevap = input(('Büyük bir kazadan sonra kendinize geliyorsunuz.. Böyle bir adada hayatta kalmak zorlu olacaktır. Devam etmek ister misiniz? Evet ise "e" - Hayır ise "h": '))

if cevap == 'e' or cevap == 'E' or cevap == 'Evet' or cevap == 'evet' or cevap == 'yes' or cevap == 'Yes' or cevap == 'EVET' or cevap == 'YES':
    time.sleep(1)
    cevap =input("Taşıttan su ve konserve gibi öğün yemeklerinizi alıp yola koyuluyorsunuz.. Çok uzun bir zaman geçti.. Önünüze bir patika yol çıkıyor.Sağa ya da Sola dönmeniz lazım.\nSağ dön : 'sağ' - Sola dön : 'sol' :")
    time.sleep(2)
    if cevap == 'sağ' or cevap == 'Sağ' or cevap == 'SAĞ' or cevap == 'sag' or cevap == 'Sag' or cevap == 'SAG':
        print("Sağa doğru yürümeye başladın.. Küçük 2 katlı bir ahşap evle karşılaştın. ")
        time.sleep(0.5)
        cevap = input("İçeri Girmeye Çalış :'i' - Kapıyı tıklat :'k' - Uzaklaş: 'u':")
        time.sleep(0.5)
        if cevap == 'i' or cevap == 'İ' or cevap == 'İçeri' or cevap == 'İÇERİ':
            print("İçeri zorla girmeye çalışıyorsun.")
            time.sleep(0.5)
            print("Alet ve edavatın yok güç uygulayarak kapı kolunu kırdın.\nAşağıdan seni duyan evin sahibi silahını kapıp yukarı çıktı")
            time.sleep(0.5)
            print("'HAYIR AMACIM HIRSIZLIK DEĞİL YAPMAYIN' diye bağırsan da seni umursamadan kafana bir kurşun sıktı.\nÖlmen 4saniye sürdü.")
            time.sleep(0.5)
            print("Öldün !")
        elif cevap == 'k' or cevap == 'K' or cevap == 'Kapı' or cevap == 'KAPI' or cevap == 'TIKLAT' or cevap == 'tıklat':
            print("Yavaşça kapıyı tıklatıyorsun\nİçeriden bir ses:")
            time.sleep(0.5)
            print("-KİM O")
            time.sleep(0.5)
            print("+Ben bir kaza sonucu bu adaya düştüm acaba yardım edebilir misiniz? ")
            time.sleep(0.5)
            print("-Ne istiyorsun?")
            time.sleep(0.5)
            print("+Kalıcak bir yer ve varsa sinyal yolliyabileceğim bir telsiz kullanmak istiyorum")
            time.sleep(0.5)
            print("Kapı açılır ve seni buyur eder.\n-Hoşgeldiniz kendinizi rahat hissedin biraz yemek getirip daha sonra telsizle konuşturacağım sizi")
            time.sleep(0.5)
            print("+Çok teşekkürler buna ihtiyacım vardı.\nBiraz beklersiniz")
            time.sleep(0.5)
            print("Adam gerçekten sözünü tutar ve size iyi bakar telsizle yardım istediniz.")
            time.sleep(1.5)
            print("KURTULDUNUZ !!")
        elif cevap == 'u' or cevap == 'U' or cevap == 'UZAK' or cevap == 'uzak' or cevap == 'UZAKLAŞ' or cevap == 'uzaklaş' or cevap == 'uzaklas' or cevap == 'UZAKLAS':
            print("Arkanı dönüp uzaklaştın ve yürümeye başladın")
            time.sleep(1)
            print("Birden yağmur bastırmaya başladı.\nHızla sığınacak yer aramaya başladın")
            time.sleep(0.5)
            print("Ayağın kaydı ve yere düştün bileğin burkuk bir şekilde hareket etmeye çalışıyorsun\nKafanı kaldırdığında sana doğru gelen vahşi bir yaratık gördün")
            time.sleep(1)
            print("Gözlerini kapayıp kaderine teslim oldun.\nCanavar tarafından boğularak ölmen 5 saniye sürdü.")
            time.sleep(0.5)
            print("Öldün !!")
        else:
            time.sleep(3)
            print("Karar vermek çok fazla bekledin. Orda öylece dikilirken atlarıyla hızla geçen bir barbar ekip seni iple bağlayıp atın arkasında sürüklemeye başladılar")
            time.sleep(2)
            print("Bağıra bağıra uzunca bir süre sürüklendin.")
            time.sleep(2)
            print("Acılar içinde öldün !")
    elif cevap == 'sol' or cevap == 'Sol' or cevap == 'SOL':
        print("Sola doğru yürümeye başladın. İlerde vahşi devasa bir insana rastladın. \nHeybetli ve güçlü görünüyor.\nVe Sanırım seni farketti..")
        time.sleep(0.5)
        cevap = input(("Saldır: 's' - Kaç 'k':"))
        if cevap == 's' or cevap == 'S' or cevap == 'Saldır' or cevap == 'SALDIR' or cevap == 'saldir' or cevap == 'SALDİR':
            print("Hiç birşeysiz bir şekilde saldırmaya başladın. Yumruklarını savuruyorsun ama işlemiyor gibi görünüyor. \nTek yumruğuyla seni yere serdi..\nVahşice yumruklayarak öldüresiye dayak yedin..")
            time.sleep(2.5)
            print("Sen baygın yatarken bu vahşi yaratık evine gidip gelmişti bile evinden aldığı halatla seni yakındaki bir ağaca astı..")
            time.sleep(1)
            print("Boğularak ölmen 10 saniye sürdü. Seni orda asılı halde bıraktı. \nÖldün !")
            
        elif cevap == 'k' or cevap == 'K' or cevap == 'Kac' or cevap == 'KAC' or cevap == 'Kaç' or cevap == 'KAÇ':
            print("Kocaman bir canavarı gördün ve kaçmaya karar verdin. ")
            time.sleep(1)
            print("Adımlarını büyük büyük atıyor nefes nefese kalıyorsun.")
            time.sleep(0.5)
            print("Dinlenmek için durdun ama bu vahşi yaratık yorulmuyordu.. \nSeni yakaladığı yerde boğarak öldürmesi 10 saniye sürdü.")
            time.sleep(1)
            print("Öldün!")
        
        else:
            time.sleep(1)
            print("Farkedildiğinde napıcağını bilemedin öylece kalakaldın. Seni bayıltıp evine götürdü. \nSana eziyet etmek için bodruma kilitledi..")
            time.sleep(4)
            print("Yıllarca kapalı kaldın.. Esaretinin sonucu ölüm oldu.. ")
        
        
    else:
        time.sleep(3)
        print("Karar vermedin ya da adayı çok güvenilir bir yer olarak düşündün. Seni tanımlayamayan bir yerli tarafından nişancı tüfeğiyle vuruldun. \nKanlar içinde belli 3 dakika kadar can çekiştin.")
        time.sleep(2)
        print("Öldün !!")
    
    
else:
    time.sleep(1.5)
    print("Arkanızda bir uçurumdan kendinizi dev dalgaların içine bıraktınız.. \nCevap kısa bir sürede acı içinde can verdiniz.. \nHoşçakal..")