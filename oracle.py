import json, math

def pos(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>0
def num(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>=0
def jround(x): return math.floor(x+0.5)
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)
def r1(x): return jround(x*10)/10

def ice_plan(sticker,amb,opens):
    if not pos(sticker): return {"error":"the sticker days must be above zero"}
    if not math.isfinite(amb): return {"error":"the temperature must be a number"}
    if not num(opens): return {"error":"the lid opens must be zero or more"}
    t=max(0.4,1-max(0,amb-75)*0.016)
    days=sticker*t*(1-0.02*opens)
    if days<=0: days=0.2
    return {"days":r1(days)}

def render_ice(r,sticker,amb,opens):
    return ("Your "+jsnum(sticker)+"-day sticker at "+jsnum(amb)+" F with the lid up "+jsnum(opens)
            +" times a day figures about "+jsnum(r["days"])
            +" days - the lab kept the lid closed in a 75-degree room.")

def load_plan(lb):
    if not pos(lb): return {"error":"the contents weight must be above zero"}
    return {"ice":r1(lb*2)}

def render_load(r,lb):
    return ("Your "+jsnum(lb)+" lb of food and cans wants about "+jsnum(r["ice"])
            +" lb of ice - the 2:1 rule counts the beer too.")

def block_plan(cube):
    if not pos(cube): return {"error":"the cube days must be above zero"}
    return {"days":r1(cube*1.5)}

def render_block(r,cube):
    return ("Your "+jsnum(cube)+" days of cubes becomes about "+jsnum(r["days"])
            +" days as one block - same pounds, fewer edges.")

cases=[]
def add(tool,args):
    if tool=="ice": r=ice_plan(*args); fn=render_ice
    elif tool=="load": r=load_plan(*args); fn=render_load
    else: r=block_plan(*args); fn=render_block
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(5,95,8),(5,75,0),(7,85,4),(3,90,10),(10,80,6),(5,110,5),(4,70,8),(6,100,12)]:
    add("ice",a)
for a in [(10.5,),(20,),(15,),(8,),(24,),(12.5,)]:
    add("load",a)
for a in [(2,),(3.5,),(1.5,),(4,),(2.6,)]:
    add("block",a)
add("ice",[0,90,5]); add("ice",[5,90,-1]); add("load",[0]); add("block",[0])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
