"""Exact candidate experiments; stdlib only; no numerical root verification."""
from fractions import Fraction as F
import json, hashlib, sys
from pathlib import Path

def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def inv(a):
 d=a[0]*a[0]+a[1]*a[1]
 return (a[0]/d,-a[1]/d)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def li_quartet(beta,t,N):
 rho=(F(beta),F(t)); ri=inv(rho); w=(1-ri[0],-ri[1]); wi=inv(w)
 a=b=(F(1),F(0)); vals=[]
 for n in range(1,N+1):
  a=mul(a,w);b=mul(b,wi);vals.append(4-2*(a[0]+b[0]))
 return vals


def main():
 vals=li_quartet(F(3,5),14,88)
 assert all(v>0 for v in vals[:87])
 assert vals[87]<0
 # Cross-check reduced formula against definition using all four Gaussian rationals.
 for n in (1,2,87,88):
  direct=(F(0),F(0))
  for beta,t in ((F(3,5),14),(F(3,5),-14),(F(2,5),14),(F(2,5),-14)):
   ri=inv((beta,F(t)));w=(1-ri[0],-ri[1]);power=(F(1),F(0))
   for _ in range(n):power=mul(power,w)
   direct=add(direct,(1-power[0],-power[1]))
  assert direct==(vals[n-1],F(0))
 # Negative control: critical-line synthetic pair/quartet, every tested term >= 0.
 on=li_quartet(F(1,2),14,88);assert all(v>=0 for v in on)
 # Deliberately unsafe finite-prefix classifier accepts an off-line quartet.
 unsafe_accepts=all(v>=0 for v in vals[:87]);assert unsafe_accepts
 rh={'model':'synthetic quartet {3/5+14i,3/5-14i,2/5+14i,2/5-14i}; NOT zeta zeros',
     'positive_prefix_length':87,'first_negative_index':88,'lambda88_exact':str(vals[87]),
     'lambda88_float_for_display_only':float(vals[87]),'minimum_prefix_float_for_display_only':float(min(vals[:87])),
     'critical_line_control_nonnegative':True,'unsafe_prefix_classifier_false_positive':unsafe_accepts}
 out={'status':'local_exploratory_candidate_only','rh':rh,'tests':'all assertions passed'}
 Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'tests':out['tests'],'positive_prefix':87,'first_negative':88}))
if __name__=='__main__':main()
