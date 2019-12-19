# Txt'ki Kelimeleri Ve Cümleleri Sayan Program

def giris():

    kullanici_adi = 'Bekir'

    kullanici_sifre = '1234'

    kullanici_adi_sor = input('Kullanıcı Adı: ')

    kullanici_sifre_sor = input('Şifre: ')

    while(True):

        if(kullanici_adi_sor == kullanici_adi and kullanici_sifre_sor == kullanici_sifre):

            print('Giriş Başarı İle Gerçekleştirildi.')

            ayiklayici()

            break

        else:

            print('Tekrar Deneyin.')

            giris()

def ayiklayici():

    cumle_sayisi = 0

    yazi = input('Cümlenizi Giriniz:\n')

    cumleler = yazi.split()

    kelime_sayisi = len(cumleler)

    for x in cumleler:

        if '.' in x or '!' in x or '?' in x:

            cumle_sayisi += 1

        else:

            pass

    print('Girmiş Olduğunuz Yazıdaki Kelime Sayısı {}, Cümle Sayısı {}.'.format(kelime_sayisi, cumle_sayisi))

giris()