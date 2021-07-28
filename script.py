k='Utrop'
j='{0}{1}'
i='1'
h=print
g=int
f=input
V=' '
U=''
T=str
M=len
F=enumerate
A=list
import requests as W
from bs4 import BeautifulSoup as X
from tabulate import tabulate as Y
Z={}
a={'Connection':'keep-alive','Cache-Control':'max-age=0','sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile':'?0','Upgrade-Insecure-Requests':i,'Origin':'https://auktion.kronofogden.se','Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Sec-Fetch-Dest':'document','Referer':'https://auktion.kronofogden.se/auk/w.objectlist?inC=KFM&inA=WEB','Accept-Language':'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7'}
b=('inC','KFM'),('inA','WEB')
H=[]
N=f("Vänligen fyll i sökord som du vill söka efter.\nOm du är ute efter flera olika artiklar separera varje sökord med ', '.\nSökord: ")
G=0
try:G=g(f('Vänligen fyll i det högsta betalbara priset du har tänkt dig.\nOm du inte vill filtrera artiklar efter pris kan du skriva 0 eller trycka på Enter tangenten.\nPris: '))
except Exception as O:G=0
I=N.split(', ')
if M(I)==0:I.insert(0,N)
for (P,E) in F(I):
	c={'inCategoryId':U,'inPageNo':i,'inSearchCrit':'0','inSiteLang':U,'inSelectedSort':U,'inSearchText':T(E)};Q=W.post('https://auktion.kronofogden.se/auk/w.objectlist',headers=a,params=b,cookies=Z,data=c)
	if Q.text.find('Tyvärr så gav din sökning på "{0}" inga träffar just nu!'.format(E))>-1:h(E,'existerar inte i kronofogdens marknad.')
	else:
		d=X(Q.content,'html.parser')
		for (P,J) in F(A(A(A(A(d.children)[1].children)[1])[0])[11]):
			J=A(A(J.children)[0]);K=A(J[2])[0]
			if not M(A(K))>3:
				B=A(A(K)[2])[0];L=A(B)[1].text;C=A(B)[2]
				if C==V:C=j.format(A(B)[3].text,A(B)[4])
				for (O,D) in F(A(B)):
					if T(D).find(k)>-1:H.insert(0,[E,L[0:-1],C,A(D)[M(A(D))-1].text])
				continue
			for (l,B) in F(A(K)[3]):
				L=A(B)[1].text;C=A(B)[2]
				if C==V:C=j.format(A(B)[3].text,A(B)[4])
				for (O,D) in F(A(B)):
					if T(D).find(k)>-1:H.insert(0,[E,L[0:-1],C,A(D)[M(A(D))-1].text])
R=[]
for (P,S) in F(H):
	e=g(S[3].split(V)[0])
	if G==0 or e<G:R.insert(0,S)
h(Y(R,headers=['Sökord','Id','Artikel','Högsta Bud'],tablefmt='orgtbl'))
