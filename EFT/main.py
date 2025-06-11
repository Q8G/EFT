t="╔"+"═"*30+"\n║\n║"+"╗"
for p in ["requests","cloudscraper","colorama"]:
 try:__import__(p)
 except ImportError:import os;os.system(f"pip install {p}")
import requests,re,platform,os;import cloudscraper;from datetime import datetime;from colorama import init,Fore;s=cloudscraper.create_scraper();init();os.system('cls'if os.name=='nt'else'clear')
def url(name):
 r=s.get("https://store.epicgames.com/graphql",params={"variables":f'{{"category":"games/edition/base|bundles/games|games/edition|editors|addons|games/demo|software/edition/base|games/experience|subscription","count":1,"keywords":"{name}","locale":"en-US","sortBy":null,"sortDir":"DESC"}}',"extensions":'{"persistedQuery":{"version":1,"sha256Hash":"be4fe909f9a35f9704db7fed06fc4a47fc798ec0a6cbfa24d737aec2465904fa"}}'})
 if r.status_code!=200:return None
 if not re.search(r'"offerId":"(.*?)"',r.text) or not re.search(r'"sandboxId":"(.*?)"',r.text):return None
 r=s.get("https://store.epicgames.com/graphql",params={"variables": f'{{"locale":"en-US","country":"US","offerId":"{re.search(r'"offerId":"(.*?)"',r.text).group(1)}","sandboxId":"{re.search(r'"sandboxId":"(.*?)"',r.text).group(1)}"}}',"extensions":'{"persistedQuery":{"version":1,"sha256Hash":"abafd6e0aa80535c43676f533f0283c7f5214a59e9fae6ebfb37bed1b1bb2e9b"}}'})
 if r.status_code!=200:return None
 if not re.findall(r'"pageSlug":"(.*?)"',r.text):return None
 return f"https://store.epicgames.com/en-US/p/{re.findall(r'"pageSlug":"(.*?)"',r.text)[0]}"
for game in requests.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions").json()['data']['Catalog']['searchStore']['elements']:
 if game.get("promotions")and url(game["title"])and game["promotions"].get("promotionalOffers",[]):t=t+f"╗\n║\n║   Game: {game["title"]}\n║   URL: {url(game["title"])}\n║   Started: {datetime.strptime(game.get('promotions').get('promotionalOffers',[])[0]['promotionalOffers'][0]['startDate'],'%Y-%m-%dT%H:%M:%S.000Z').strftime('%d-%m-%Y - %#I %p'if platform.system()=='Windows'else'%d-%m-%Y - %-I %p')}\n║   Ends: {datetime.strptime(game.get('promotions').get('promotionalOffers',[])[0]['promotionalOffers'][0]['endDate'],'%Y-%m-%dT%H:%M:%S.000Z').strftime('%d-%m-%Y - %#I %p'if platform.system()=='Windows'else'%d-%m-%Y - %-I %p')}"+"\n\n"+"════════════════x══════════════"+"\n\n"
urll=max([line for line in t.splitlines()if'URL: 'in line],key=len)
for key in['Game','URL','Started','Ends']:t="\n".join([(lambda l:(seg:=l[l.find(key):],spaces:=max(len("╔"+"═"*len("════════"+urll+"\n║\n║"+"╗"))-(len(seg)+4),0),l[:l.find(seg)]+seg+' '*spaces+'║')[2])(line.rstrip('║').rstrip())if key in line else line for line in t.splitlines()])
t=t.replace("╔"+"═"*30+"\n║\n║"+"╗","╔"+"═"*len("════════"+urll+"\n║\n║"+"╗")).replace("\n╗\n║",f"║{' '*(len('╔'+'═'*len('════════'+urll+'\n║\n║'+'╗'))-1)}║");ls=t.splitlines();next((ls.__setitem__(i-1,f"║{' '*(len('╔'+'═'*len('════════'+urll+'\n║\n║'+'╗'))-1)}║")or ls.__setitem__(i,f"╠{'═'*(len('╔'+'═'*len('════════'+urll+'\n║\n║'+'╗'))-1)}╣")for i,line in enumerate(ls)if"════════════════x══════════════"in line and i>0),None);next(ls.__setitem__(i,f"║{' '*(len('╔'+'═'*len('════════'+urll+'\n║\n║'+'╗'))-1)}║")for i,line in enumerate(ls)if"║"in line);print(Fore.GREEN+"\n".join(ls[:-1])+f"║{' '*(len("╔"+"═"*len("════════"+urll+"\n║\n║"+"╗"))-1)}║"+f"\n╚{'═'*(len("╔"+"═"*len("════════"+urll+"\n║\n║"+"╗"))-1)}╝"+Fore.RESET)
