#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler,HTTPServer

answer="console.log('hello !')";

class HttpProcessor(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		if(self.path[1]!='?'):
			print(self.path)
			try:
				fl=open(self.path[1:],'r')
				if(self.path.count('.html')>0):self.send_header('Content-Type','text/html; charset=UTF-8')
				elif(self.path.count('.png')>0):
					self.send_header('Content-Type','image/png')
					self.send_header('Cache-Control','max-age=31536000')#Год
				self.end_headers()
				self.wfile.write(fl.buffer.raw.read())
				fl.close()
			except Exception as e:
				self.send_response(404)
				self.end_headers()
				self.wfile.write(bytes("404 not found or another error",encoding="utf-8"))
				print(e)
		else:
	#		self.send_header('Access-Control-Allow-Origin','*')
	#		self.send_header('Access-Control-Allow-Methods','*')
	#		self.send_header('Access-Control-Allow-Headers','*')
			self.send_header('Cache-Control','no-cache')
#			self.send_header('Pragma','no-cache')
			self.send_header('Content-Type','application/javascript')
	#		self.send_header('Content-Type','text/plain')
			self.end_headers()
			self.wfile.write(bytes(answer,encoding="utf-8"))


def mainloop():
	serv = HTTPServer(("localhost",6205),HttpProcessor)
	serv.serve_forever()
