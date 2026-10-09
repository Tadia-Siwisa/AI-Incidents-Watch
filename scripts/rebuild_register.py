"""Preserve workbook assertions; create a claim-level register without endorsing them."""
import csv
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/rebuilt'
rows = json.loads((OUT / 'workbook_inventory.json').read_text())
mapping = {'W04':'N01','W07':'N02','W08':'N03','W09':'N04','W10':'N05',
           'W11':'N06','W12':'N07','W13':'N08','W17':'N09','W15':'N10',
           'W16':'N11','W18':'N12','W20':'N13','W23':'N14','W24':'N15',
           'W25':'N16','W26':'N17'}
headers = {}
records, claims, sources = [], [], {}
urls = re.compile(r'https?://[^\s]+')
for row in rows:
    sheet = row['sheet']
    if sheet not in ('Incident Register','Master Register','Discovery Register'):
        continue
    if row['row'] == 1:
        headers[sheet] = row['cells']
        continue
    fields = dict(zip(headers[sheet], row['cells']))
    rid = row['cells'][0]
    correction = None
    if rid == 'R014':
        # Extra setting fragment displaced the remaining cells in the supplied row.
        c = row['cells']
        fields = dict(zip(headers[sheet], c[:6] + c[7:] + [None]))
        fields['Setting'] = c[5] + '; ' + c[6]
        correction = 'Original R014 has an extra setting fragment in column 7; subsequent fields are shifted. Normalized by merging columns 6–7. Original cells retained in inventory.'
    canonical = mapping.get(rid, rid)
    refs = []
    for value in fields.values():
        for url in urls.findall(value or ''):
            sid = 'S-' + hashlib.sha256(url.encode()).hexdigest()[:12]
            sources.setdefault(sid, {'source_id':sid,'url':url,'cited_by':[]})
            sources[sid]['cited_by'].append(rid)
            refs.append(sid)
    for url in row['hyperlinks'].values():
        sid = 'S-' + hashlib.sha256(url.encode()).hexdigest()[:12]
        sources.setdefault(sid, {'source_id':sid,'url':url,'cited_by':[]})
        if rid not in sources[sid]['cited_by']: sources[sid]['cited_by'].append(rid)
        if sid not in refs: refs.append(sid)
    title = fields.get('Incident / family',fields.get('Case',fields.get('Post / case')))
    gaps = ['Independent source content has not been retrieved or verified.',
            'Workbook confidence and confirmation labels are unverified assertions.']
    if not refs: gaps.append('No source URL supplied; original account must be located.')
    if rid.startswith('R'): gaps.append('Reddit report, logs, author identity and corroboration require verification; do not assume agent causation.')
    if rid in ('N09','W17'): gaps.append('Three target/run observations are asserted but not individually identified by source evidence.')
    if rid in ('N15','W24'): gaps.append('19 actions / 10 of 122 runs are asserted aggregate counts, not verified run-level records.')
    if rid in ('N14','W23'): gaps.append('N14 activity-date cell (July 9–13) differs from its timing narrative (July 8–13).')
    if rid in ('W01','W02','W03','W05','R009','R015'): gaps.append('Context, controlled evaluation or product behavior: do not automatically treat as an unauthorized operational incident.')
    if rid in ('R002','R006','R014'): gaps.append('Workbook describes an alternative explanation, human approval, or contradiction; retain as a control candidate pending source review.')
    if rid in ('R020',): gaps.append('Secondary discussion; original report and possible duplication remain unresolved.')
    if correction: gaps.append(correction)
    records.append({'record_id':rid,'canonical_candidate_id':canonical,'title':title,
                    'origin':{'file':row['file'],'sheet':sheet,'row':row['row']},
                    'original_fields':fields,'source_ids':refs,'evidence_status':'not_verified',
                    'verified_facts':[], 'analysis_eligible':False,'evidence_gaps':gaps,
                    'normalization_note':correction})
    for name,value in fields.items():
        if not value or name in ('ID','Lead ID') or urls.fullmatch(value): continue
        claims.append({'claim_id':f'{rid}-C{len([c for c in claims if c["record_id"]==rid])+1:02}',
                       'record_id':rid,'field':name,'claim_text':value,
                       'asserted_by':'supplied_workbook','verification_status':'not_verified',
                       'candidate_source_ids':refs,'supporting_evidence_ids':[],
                       'note':'Field-level assertion; source assignment is a candidate link, not proof. Split compound claims during evidence review.'})
OUT.mkdir(exist_ok=True)
for name,data in [('records.json',records),('claims.json',claims),('sources.json',list(sources.values()))]:
    (OUT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
with (OUT/'triage.csv').open('w',newline='') as f:
    w=csv.writer(f,lineterminator='\n');w.writerow(['record_id','canonical_candidate_id','title','evidence_status','analysis_eligible','source_ids','evidence_gaps'])
    for r in records:w.writerow([r['record_id'],r['canonical_candidate_id'],r['title'],r['evidence_status'],r['analysis_eligible'],';'.join(r['source_ids']),' | '.join(r['evidence_gaps'])])
manifest = [{'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted((ROOT/'data/original').glob('*.xlsx'))]
(OUT/'original_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'{len(records)} records; {len(set(r["canonical_candidate_id"] for r in records))} canonical candidates; {len(claims)} field assertions; {len(sources)} supplied URLs')
