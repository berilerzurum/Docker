# Docker
 #H2# Docker Temelleri

 <br/> Visual Studio Code Remote Container
 
  <br/> Bugün sizlere "/Sample" dosyasında oluşturduğum deneme.java dosyasını geliştirmek için kullandığım Visual Studio'nun Remote Toollarından bahsetmek istiyorum.
 
  <br/> Amaç nedir?
<br/>  Bu toolun amacı; örneğin, biz bir java dosyası oluşturmak istiyoruz. Fakat bilgisayarımızda Java için gerekli ortam (jdk dosyası, environment settings vs.) bulunmuyor. Ben bu remote development sayesinde istiyorum ki beni Java kurulu olan bir konteyner içinde uyandır ve ben java dosyamı, bilgisayarıma java dosyalarını indirmeme gerek kalmadan, o konteynerin içinde geliştireyim.
 
 <br/> Çalışma mantığı nasıl?
  <br/> İlk olarak VSCode, istediğimiz programlama dilinin imajını indirecek ve bu imajdan bir konteyner oluşturacak.
 Sonraki adım olarak o konteyenerın içine benim dosyalarımı bağlayacak (örneğin; benim /Sample içerisinde oluşturmuş olduğum deneme.java dosyası).
 Ve böylelikle ben bilgisayarımda Java kurulu olmadan, java kurulu olan bir konteyner içerisinde java dosyamı geliştirebileceğim. 
 
<br/>  Nasıl kullanılır?
<br/> İlk olarak bu toolu kullanabilmek için extension olarak Visual Studio Code'dan Remote Development eklentisini install etmemiz gerekiyor. Bu aşamadan sonra konteynerlarda yer alan geliştirme ortamlarına ulaşabiliyoruz.
 Daha sonra, VSCode editörünün sol alt köşesinde yer alan "Open a Remote Window" seçeneğini seçip, "Open Folder in Container"'a tıklıyoruz. Ve container configuration, OS, version ayarlarını da seçtikten sonra VSCode bize bir imaj oluşturuyor. Ve bu imajdan içerisinde development yapabileceğimiz bir konteyner yaratıyor.
 Ve bu işlem sonucunda VSCode, .devcontainer adlı bir dosya yaratıyor. Bu dosyanın içerisinde yaptığımız imaj ayarlarını da görebileceğimiz bir "Dockerfile" ve "devcontainer.json" dosyaları bulunuyor. 
 
  <br/> Eğer konteynera ek extension eklemek istersek ne yapmalıyız?
<br/>  Bazı eklentiler imaj içerisinde default olarak geliyor. Fakat ek eklenti eklemek istersek, yukarıda da bahsettiğim devcontainer.json dosyasındaki "extensions" kısmına ekleme yapabiliyoruz. İstediğim eklentinin Extension ID'sini .json dosyasındaki eklenti kısmına kopyalayarak istediğim eklentileri imajıma yerleştirebiliyorum.
 
 
 
 
