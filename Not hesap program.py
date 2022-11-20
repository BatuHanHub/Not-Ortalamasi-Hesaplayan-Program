print ( """
   _____ _____  _        ____         ___  
  / ____|  __ \| |      |___ \       / _ \ 
 | |  __| |__) | |        __) |     | | | |
 | | |_ |  ___/| |       |__ <      | | | |
 | |__| | |    | |____   ___) |  _  | |_| |
  \_____|_|    |______| |____/  (_)  \___/                                                 
       
Not Ortalaması Hesap Programı, sürüm 1.0 -sürüm (x86_x64)
Lisans GPLv3+ : GNU GPL sürüm 3 <https://www.gnu.org/licenses/gpl-3.0.html>
telif hakkı (C) 2022 BatuHanHub 

Bu ücretsiz bir yazılımdır; değiştirmekte ve yeniden dağıtmakta özgürsünüz.
Yasaların izin verdiği ölçüde HİÇBİR GARANTİ YOKTUR.\n""" )

print("- Not Ortalaması Hesap Programına Hoşgeldiniz! -\n")

while True:
    
#############################################################  

    not1 = int(input("1. sınav notunuzu giriniz:")) 
        
    if not1 > 100:
        print("HATA: 100 den büyük sayı girmeyiniz...") 
        continue
    
    elif not1 == str:
        print("HATA: sınav puanınızı giriniz...")
        continue
    
#############################################################    

    not2 = int(input("2. sınav notunuzu giriniz:"))
    
    if not1 > 100:
        print("HATA: 100 den büyük sayı girmeyiniz...") 
        continue
    
    elif not1 == str:
        print("HATA: sınav puanınızı giriniz...")
        continue
    
##############################################################       

    ortalama = (not1 + not2) /2
    
    if ortalama > 70:
        print("Harika çok başarılısın...")
    
    elif ortalama > 50 >= 70:
        print("Biraz daha gayret gösterirsen başarabilirsin...")
    
    elif ortalama < 50:
        print("Diğer dönem baya çalışman gerek...")
    
    print("Not ortalamanız", ortalama)
    
################################################################
    input("Çıkmak için bir tuşa basınız...")
    
    break
