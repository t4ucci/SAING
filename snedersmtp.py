import smtplib
import threading

print("    by: t4ucci\n    version: 1.0\n")
print("      ;;;;; Sender Attack In Gmail :: SAIG\n")
print("""

▒▒▒▒▒▐▀▀▀█▄▒▒▒▒▒▒▒▒▒
▒▒▒▒█▀─────█▒▒▒▒▒▒▒▒
▒▒▒█────▄─▄─▌▒▒▒▒▒▒▒
▒▒▒▌───██─█▌▌▒▒▒▒▒▒▒
▒▒▒▌───█▌──▌▌▒▒▒▒▒▒▒
▒▒▒▌────────▌▒▒▒▒▒▒▒
▒▒█─────────▐▒▒▒▒▒▒▒
▒▐▌─▐───────▐▄▄▒▒▒▒▒
▒▐▌─▐────────▄▀▀█▒▒▒
▒█──▀▄──▄█▄▀▀▒▒▒▌▀▄▒
▐▌────██▀█░█▄▒▄▄█▀▀▌
▐▌──▌▐───▐░░▐▀░░░░░▌
▐▌──▌────▐░░▐░░░░░░▌
▐───▌────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█────▐░░▐░░░░░░▌
▐───█─────▀█▐▄▄▄█▀▀▒
▀▄▄─▐───────▄█▒▒▒▒▒▒
▒▒▒▀█───█▄▀▀▀▒▒▒▒▒▒▒
▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒
\n""")

print("""

.Mbgd                           `7MM                    
,MI    "Y                             MM                    
`MMb.      .gP"Ya  `7MMpMMMb.    ,M""bMM   .gP"Ya  `7Mb,od8 
  `YMMNq. ,M'   Yb   MM    MM  ,AP    MM  ,M'   Yb   MM' "' 
.     `MM 8M""""""   MM    MM  8MI    MM  8M""""""   MM     
Mb     dM YM.    ,   MM    MM  `Mb    MM  YM.    ,   MM     
P"Ybmmd"   `Mbmmd' .JMML  JMML. `Wbmd"MML. `Mbmmd' .JMML.                           

""")

print("  [!] Para este software de spam funcionar, é necessário ir na sua Gerenciação de Contas no Google e arrastar pro lado que está escrito SEGURANÇA, daí vai ter de ativar a opção ACESSO A APP MENOS SEGURO. ")

print("\n  [!] Atenção: É necessário isso porque precisa se conectar no servidor pra poder enviar mensagens via SMTP pro Destinatário.\n\n")

your_email = input("   Digite o seu email: ")
your_password = input("   Digite a sua senha: ")
print()
email_receber = input("   Email destinatário: ")

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
if server.login(your_email, your_password):
    print("Conectado com sucesso!! ;)")
else:
    print("[-]Talvez a senha/email estejam incorretas ou voce não ativou o ACESSO A APP MENOS SEGURO")
    print("======================")
    print("The end..!")
    server.quit()
    exit()
 
print("======================")
msg = str(input("   Digite a sua mensagem: "))
tam = int(input("   Quantidade de envio: "))
vel = int(input("   Velocidade do envio: "))

def start():
    for i in range(1,tam+1):
        server.sendmail(your_email, email_receber, msg)
        print(f"[+]Enviando sua mensagem para{email_receber} :: {tam}")

for x in range(vel):
    vel = threading.Thread(target=start)
    vel.start()

















