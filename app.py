import argparse,json,re,time,urllib.request,unittest
from pathlib import Path
def evaluate(case,response):
 if not isinstance(response,str):raise ValueError('Response must be text')
 checks=[]
 for text in case.get('contains',[]):checks.append({'check':'contains','value':text,'passed':text.lower()in response.lower()})
 for text in case.get('forbidden',[]):checks.append({'check':'forbidden','value':text,'passed':text.lower()not in response.lower()})
 for pattern in case.get('regex',[]):checks.append({'check':'regex','value':pattern,'passed':bool(re.search(pattern,response))})
 if not checks:raise ValueError('Each case needs an assertion')
 return {'id':case['id'],'passed':all(c['passed']for c in checks),'checks':checks}
def infer(prompt,model):
 req=urllib.request.Request('http://127.0.0.1:11434/api/chat',data=json.dumps({'model':model,'stream':False,'messages':[{'role':'user','content':prompt}]}).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=180)as r:return json.load(r)['message']['content']
class Tests(unittest.TestCase):
 def test_checks(self):
  c={'id':'x','contains':['wave'],'forbidden':['secret'],'regex':[r'\d+']};self.assertTrue(evaluate(c,'Wave 12')['passed']);self.assertFalse(evaluate(c,'secret wave')['passed']);self.assertRaises(ValueError,evaluate,{'id':'x'},'a')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('cases',nargs='?');p.add_argument('--model',help='Optional installed Ollama model');p.add_argument('--self-test',action='store_true');a=p.parse_args()
 if a.self_test:unittest.main(argv=['eval'])
 elif a.cases:
  rows=[json.loads(s)for s in Path(a.cases).read_text().splitlines()if s.strip()];seen=set();reports=[]
  for c in rows:
   if c['id']in seen:raise ValueError('Duplicate case ID')
   seen.add(c['id']);started=time.perf_counter();response=infer(c['prompt'],a.model)if a.model else c['response'];r=evaluate(c,response);r['latency_seconds']=round(time.perf_counter()-started,4);reports.append(r)
  print(json.dumps({'mode':'live local model'if a.model else'fixture evaluation','cases':reports,'passed':sum(r['passed']for r in reports),'total':len(reports)},indent=2))
 else:p.error('Supply a JSONL case file')
