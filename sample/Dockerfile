
#FROM komutu ile; base image olarak Ubuntu:18.04 versiyonu seçtik.
FROM ubuntu:18.04

#RUN komutları ile Paket listesini sunucudan çektik ve o liste içinden openjdk-8-jre dosyasını,
#-y komutu sayesinde hiç etkileşim olmadan(kurma sürecinde y tuşuna basmamıza ihtiyaç olmadan) kurabildik.
RUN apt update
RUN apt install openjdk-8-jre -y

#WORKDIR ile conteiner içindeki çalışma dizinimizi kök dizin yaptık.
WORKDIR /

#COPY sayesinde, bulunduğumuz dizindeki deneme.class'ı kök dizinine kopyaladık.
COPY deneme.class .

CMD ["java","deneme"]

# Sonuç olarak, bu oluşturduğumuz Dockerfile "docker run -it --rm sample" komutu ile çalıştığında,
# deneme.java dosyamızı da çalıştırıp rastgele bir sayı üretecek.