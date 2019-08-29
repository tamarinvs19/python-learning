key_coefs = {'style="background-color: rgba(56, 112, 30': 1.0, 'style="background-color: rgba(229, 122, 122': 0.5, 'style="background-color: rgba(3, 91, 1': 2.0, 'style="background-color: rgba(7, 111, 197': 1.0, 'style="background-color: rgba(255, 247, 119': 1.75, 'style="background-color: rgba(229, 122, 220': 0.75, 'style="background-color: rgba(156, 229, 122': 1.0, 'style="background-color: rgba(104, 218, 169': 1.0, 'style="background-color: rgba(0, 154, 69': 1.0, 'style="background-color: rgba(211, 8, 150': 1.75, 'style="background-color: rgba(255, 182, 119': 2.5, 'style="background-color: rgba(118, 0, 2': 1.3, 'style="background-color: rgba(177, 237, 0': 1.0, 'style="background-color: rgba(239, 111, 229': 1.0, 'style="background-color: rgba(104, 255, 235': 1.25, 'style="background-color: rgba(3, 7, 252': 2.0, 'style="background-color: rgba(218, 8, 99': 1.25, 'style="background-color: rgba(255, 223, 119': 1.25, 'style="background-color: rgba(102, 0, 125': 2.0, 'style="background-color: rgba(235, 47, 0': 1.5, 'style="background-color: rgba(119, 255, 119': 1.0, 'style="background-color: rgba(130, 255, 119': 1.0, 'style="background-color: rgba(0, 150, 150': 1.75, 'style="background-color: rgba(255, 217, 0': 3.0, 'style="background-color: rgba(255, 64, 0': 0.5, 'style="background-color: rgba(161, 122, 229': 1.5}
key_scores = '<span class="markValInProgress"><span ng-class="{'
key_names = '<span ng-bind="unit.unitName" class="ng-binding">'
def change_page():
    res = []
    with open('page.html', 'r') as f:
        s = str(f.readline())
        ds = ['<!--- -->', '<!-- ngIf: mark.extra --><!-- ngRepeat: m in mark.extra -->', '<!-- end ngIf: unit.totalMark -->']
        while 'БЕСЕДЫ КЛ РУК' not in s:
            for d in ds:
                s = s.replace(d, '')
            if not s.strip() in {'</div>', '</td>'}  and '<!--' not in s and s!='\n' and '<div style="white-space: nowrap;" class="text-left">' not in s:
                res.append(s)
            s = str(f.readline())
        res.append('БЕСЕДЫ КЛ РУК')
    with open('page.html', 'w') as f:
        for r in res:
            f.write(r)

def change_page_2():
    res = []
    with open('page.html', 'r') as f:
        s = str(f.readline())
        ds = ['<!--- -->', '<!-- ngIf: mark.extra --><!-- ngRepeat: m in mark.extra -->', '<!-- end ngIf: unit.totalMark -->']
        while 'БЕСЕДЫ КЛ РУК' not in s:
            for d in ds:
                s = s.replace(d, '')
            res.append(s)
            s = str(f.readline())
        res.append('БЕСЕДЫ КЛ РУК')
    with open('page.html', 'w') as f:
        for r in res:
            f.write(r)
 
            
def adv_score():
    name = ''
    coef = 1
    scores = {}
    s = ''
    with open('page.html' , 'r') as f:
        while 'БЕСЕДЫ КЛ РУК' not in s:
            s = f.readline().strip()
            if key_names in s:
                name = s.split('>')[1].split('<')[0]
                scores[name] = {'sum':0, 'coef':0}
            if 'rgba' in s:
                coefs = [k for k in key_coefs.keys() if k in s]
                coef = key_coefs[coefs[0]]
            if key_scores in s:
                score = s.split('</')[-4][-1]
                if score != '>':
                    score = int(score)
                    scores[name]['sum'] += score*coef
                    scores[name]['coef'] += coef
    #print(scores)
    advs = {}
    for k in scores.keys():
        if scores[k]['coef'] != 0:
            advs[k] = scores[k]['sum']/scores[k]['coef']
            print(k, round(advs[k], 3),'                       ', scores[k]['sum'], scores[k]['coef'])
    res = ['{} {}'.format(k, round(advs[k], 3)) for k in advs.keys()]
    with open('scores.txt', 'w') as f:
        f.write('\n'.join(res))
    
change_page_2()
adv_score()

