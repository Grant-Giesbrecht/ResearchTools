import smtplib 
import base64
import json

def encrypt(clear, key):
	enc = []
	for i in range(len(clear)):
		key_c = key[i % len(key)]
		enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
		enc.append(enc_c)
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decrypt(enc, key):
	dec = []
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
		dec.append(dec_c)
	return "".join(dec)

def send_email(recipient:str, subject:str, msg_body:str, local_pass:str, email_file:str="email.json"):
	''' Sends an email to the specified recipient from the email
	address specified in the JSON file. The password must also be decypted from the JSON encoded password
	here, so enter the easy to remember password as 'local_pass', and it'll 
	authorize sending the email. 
	
	recipient: recipient email address 
	subject: Subject line
	msg_body: Body text to send
	local_pass: Short password
	'''
	
	# Load enctrypted email and password from file
	with open(email_file, "r") as jf:
		email_data = json.load(jf)
		
		enc_email = email_data['email']
		enc_pwd = email_data['password']
	
	# Log in to email account and send message
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
		
		# Get plaintext address and password
		email_address = decrypt(enc_email, local_pass)
		email_password = decrypt(enc_pwd, local_pass)
		
		connection.login(email_address, email_password)
		connection.sendmail(from_addr=email_address, to_addrs=recipient, msg=f"subject:{subject} \n\n {msg_body}")

if __name__ == '__main__':
	
	# Get email address and local password
	lp = input("Local password: ")
	st = input("Send to: ")
	
	# Send email
	send_email(st, "Subject Line", "Body text", lp, email_file="email.json")