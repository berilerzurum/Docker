FROM httpd:2.4 
COPY ./html /usr/local/apache2/htdocs/


#Eğer yukarıdaki gibi httpd ile değil de Ubuntu ile ilerlemek isteseydik, kodlarımıza aşağıdaki gibi FOREGROUND ve EXPOSE 80'i de 
#eklemek durumunda kalırdık. Fakat httpd 'de bunların hepsi kurulu olarak geldiği için bu komutlara yukarıda gerek kalmadı.

#FROM ubuntu 
#RUN apt update 
#ARG DEBIAN_FRONTEND=noninteractive
#RUN apt install –y apache2 
#RUN apt install –y apache2-utils 
#RUN apt clean 
#EXPOSE 80
#CMD [“apache2ctl”, “-D”, “FOREGROUND”]