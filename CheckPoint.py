import re

r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
valido = False
emails = ["daianadarosa48@gmail.com","Macielvigao41@hotmail.com","rayane.fsa32@gmail.com","mariaalice251877@gmail.com","adrieli.gomessoares@gmail.com","negomarcio_silva@hotmail.com","helanodsouza@hotmail.com","martacila@hotmail.com","mrfill.melo@gmail.com","ariane.lojasmel@gmail.com","matheus199328@live.com","claubeno@hotmail.com","jeffersonkardoso10@gmail.com","r.torres2017@gmail.com","Luan.lsf@Outlook.com","elchuckbr@gmail.com","valdirenepds03@hotmail.com","Jaque.jesus13@hotmail.com","mayaracalebe@gmail.com","pauloferreiraesporte@yahoo.com.br","h-drikavieira@hotmail.com","luanasilva299318@gmail.com","beatrizgoncalves__@hotmail.com","tombraga2016@gmail.com","higorcoutinho815@yahoo.com","thiagolemos639@gmail.com","ali.santos23@hotmail.com","johnsbs@gmail.com","fatima-marangoni@hotmail.com","claudiopferreira@yahoo.com.br","lorraynealbuquerquedasilva@hotmail.com","estelabraud@hotmail.com","ospqslcsan@gmail.com","sabrinamedeirosbrandao@hotmail.com","Waynakessy@gmail.com","emerscarlos@gmail.com","Jjorge.souza@hotmail.com","lilianjaqueto@hotmail.com","jlopesrca@hotmail.com","line_26_silva@hotmail.com","arcialbanez@hotmail.com","cintia.thielo@yahoo.com.br","andre_reis21@hotmail.com","lillianthais_lep@hotmail.com","miao@perim.com.br","Irlanemayra@outlook.com","angelitaandrade2011@bol.com.br","Alexsandra.hora@gmail.com","amarcom2215@gmail.com","andressaccdasilva@gmail.com","Karinathensi25052013@gmail.com","neyemuri@gmail.com","alissontrzeciakidealmeida@hotmail.com","Dekarodrigues60@gmail.com","Dudamoraesdeoliveira@hotmail.com","samuelwendrelsamuel@hotmail.com","samuelwendrelsamuel@hotmail.com","josecarlosdesouza958@yahoo.com.br","joelma.francy@hotmail.com","Elbersd@hotmail.com","hevy.mends@gmail.com","rafa_xxv@hotmail.com","David2rangel@GMAIL.COM","pbf.Sabrina.ti@gmail.com","cleicbrasil.9@gmail.com","Andrezadavy29@gmail.com","tuanelpoliveira@gmail.com","byunny37@gmail.com","neilyivanguerra@gmail.com","raquelmaciel2009@hotmail.com"]

while valido != True:
    consulta = input("Digite um email para ser verificado: ")
    if r.match(consulta):
        valido = True
    else:
        print("Digite um email valido")

for x in emails:
    if x == consulta:
        print("Esse email foi vazado!")