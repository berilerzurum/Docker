# Docker

<h2> Docker Temelleri </h2>

 <br/><h3>  Visual Studio Code Remote Container </h3> 
 
  <br/> <u> <li> Bugün sizlere "/Sample" dosyasında oluşturduğum deneme.java dosyasını geliştirmek için kullandığım Visual Studio'nun Remote Toollarından bahsetmek istiyorum.</u> </li>
 
  <br/> <ins>***Amaç nedir?***</ins>
<br/> <u> <li>Bu toolun amacı; örneğin, biz bir java dosyası oluşturmak istiyoruz. Fakat bilgisayarımızda Java için gerekli ortam (jdk dosyası, environment settings vs.) bulunmuyor. Ben bu remote development sayesinde istiyorum ki beni Java kurulu olan bir konteyner içinde uyandır ve ben java dosyamı, bilgisayarıma java dosyalarını indirmeme gerek kalmadan, o konteynerin içinde geliştireyim.</u> </li>
 
 <br/> <ins>***Çalışma mantığı nasıl?***</ins>
  <br/><u> <li> İlk olarak VSCode, istediğimiz programlama dilinin imajını indirecek ve bu imajdan bir konteyner oluşturacak.
 Sonraki adım olarak o konteyenerın içine benim dosyalarımı bağlayacak (örneğin; benim /Sample içerisinde oluşturmuş olduğum deneme.java dosyası).
 Ve böylelikle ben bilgisayarımda Java kurulu olmadan, java kurulu olan bir konteyner içerisinde, java dosyamı geliştirebileceğim. </u> </li>
 
<br/>  <ins>***Nasıl kullanılır?***</ins>
<br/> <u> <li>İlk olarak bu toolu kullanabilmek için extension olarak Visual Studio Code'dan Remote Development eklentisini install etmemiz gerekiyor. Bu aşamadan sonra konteynerlarda yer alan geliştirme ortamlarına ulaşabiliyoruz.</li>
 <li>Daha sonra, VSCode editörünün sol alt köşesinde yer alan "Open a Remote Window" seçeneğini seçip, "Open Folder in Container"'a tıklıyoruz. Ve container configuration, OS, version ayarlarını da seçtikten sonra VSCode bize bir imaj oluşturuyor. Ve bu imajdan, içerisinde development yapabileceğimiz bir konteyner yaratıyor.</li>
 <li>Ve bu işlem sonucunda VSCode, .devcontainer adlı bir dosya yaratıyor. Bu dosyanın içerisinde yaptığımız imaj ayarlarını da görebileceğimiz bir "Dockerfile" ve "devcontainer.json" dosyaları bulunuyor. </u> </li>
 
  <br/><ins> ***Eğer konteynera ek extension eklemek istersek ne yapmalıyız?***</ins>
<br/> <u> <li> Bazı eklentiler imaj içerisinde default olarak geliyor. Fakat ek eklenti eklemek istersek, yukarıda da bahsettiğim devcontainer.json dosyasındaki "extensions" kısmına ekleme yapabiliyoruz. İstediğim eklentinin Extension ID'sini .json dosyasındaki eklenti kısmına kopyalayarak istediğim eklentileri imajıma yerleştirebiliyorum.</u> </li>
 
 
 
 
