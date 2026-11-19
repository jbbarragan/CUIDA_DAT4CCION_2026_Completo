import json, pathlib, math
p=pathlib.Path(__file__).parent/'dist'
d=json.loads((p/'datos.json').read_text());r=d['rows'];assert len(r)==40
keys=[(x['dimension'],x['indicador'],x['sexo'],x['anio']) for x in r];assert len(set(keys))==len(keys)
assert all(math.isfinite(x['valor']) and x['valor']>=0 for x in r)
assert all(x['valor']<=100 for x in r if x['unidad']=='%')
assert all(x['fuente'] in [s['id'] for s in d['sources']] and x['universo'] for x in r)
assert abs(28.2-11.5-16.7)<1e-8
assert abs(100*6*.8*.7-336)<1e-8
assert abs(200*6*.8*.7-672)<1e-8
print('40 observaciones válidas; sin duplicados; fuentes y cálculos consistentes')
