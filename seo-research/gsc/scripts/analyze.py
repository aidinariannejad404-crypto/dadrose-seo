import sys, re, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load import load
import pandas as pd
from urllib.parse import unquote, quote
OUT='/mnt/project-files/seo-research/gsc'
os.makedirs(OUT+'/clean',exist_ok=True)
v1=load('in/v1.xlsx'); v2=load('in/v2.xlsx')
SRC='GSC Performance via dadrose_keywords_for_writers_v2.xlsx; 2025-12-31..2026-10-11 (10 Dey 1404..19 Mehr 1405)'
FA_D=str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩','01234567890123456789')
def norm(s):
    s=str(s).translate(FA_D).replace('ي','ی').replace('ك','ک').replace('‌',' ').replace('أ','ا').replace('آ','ا')
    s=re.sub(r'[؟?!،,:+()]',' ',s); return re.sub(r'\s+',' ',s).strip().lower()
def path(u):
    u=unquote(str(u)); u=re.sub(r'^https?://[^/]+','',u); return u.split('#')[0] or '/'
NUM=['نمایش','کلیک','CTR %','جایگاه','کلیک بالقوه','کلیک بالقوه (رتبه ۳)','مجموع نمایش خوشه','تعداد عبارت','میانگین جایگاه']
EN={'عنوان صفحه':'title','آدرس':'url','نمایش':'impressions','کلیک':'clicks','CTR %':'ctr_pct','جایگاه':'avg_position',
 'کلیک بالقوه':'est_extra_clicks','کلیک بالقوه (رتبه ۳)':'est_extra_clicks_at_pos3','عبارت‌های اصلی':'top_queries','اقدام پیشنهادی':'action','اقدام':'action',
 'کلیدواژه':'query','صفحه‌ی فعلی':'current_page','سوال/عبارت':'query','موضوع پیشنهادی (عبارت اصلی)':'topic','مجموع نمایش خوشه':'cluster_impressions',
 'تعداد عبارت':'n_queries','میانگین جایگاه':'avg_position','عبارت‌های همراه':'related_queries','توضیح برای نویسنده':'writer_note',
 'آخرین ویرایش':'last_modified','۱۰ عبارت اصلی (برای پوشش در متن)':'top10_queries','وضعیت در گوگل':'gsc_state'}
SLUG={'۱-فرصت سریع':'01_ctr_gap_pages','۲-صفحه دوم گوگل':'02_page2_queries','۲ب-ارتقا به رتبه ۱ تا ۳':'02b_pos4_10_queries',
 '۳-سوالات کاربران':'03_question_queries','۴-مقاله جدید':'04_new_article_topics','۵-عبارت‌های هر صفحه':'05_page_queries',
 '۶-به‌روزرسانی قدیمی‌ها':'06_stale_pages','۷-ایندکس‌نشده‌ها':'07_not_indexed'}
S={}
for k,slug in SLUG.items():
    df=v2[k][1].copy()
    for c in df.columns:
        if c in NUM: df[c]=pd.to_numeric(df[c])
    df=df.rename(columns=EN)
    if 'url' in df: df['path']=df.url.map(path)
    df.to_csv(f'{OUT}/clean/v2_{slug}.csv',index=False,encoding='utf-8-sig'); S[slug]=df

# ---------- URL inspection audit ----------
a=pd.read_csv('in/gsc.csv',encoding='utf-8-sig')
a['path']=a.url.map(path)
a['non_ascii_slug']=a.url.map(lambda u: bool(re.search('[^\x00-\x7f]',u)))
perf_paths=set(S['05_page_queries'].path)|set(S['02b_pos4_10_queries'].path)|set(S['03_question_queries'].path)|set(S['01_ctr_gap_pages'].path)|set(S['02_page2_queries'].path)
a['has_search_impressions']=a.path.isin(perf_paths)
a['audit_reliable']=~(a.non_ascii_slug & (a.state=='URL is unknown to Google'))
a['inspect_with']=a.url.map(lambda u: quote(u,safe=':/?=&#%'))
a.to_csv(f'{OUT}/clean/gsc_url_inspection_clean.csv',index=False,encoding='utf-8-sig')
R={}
R['audit_states']=pd.crosstab(a.state,a.non_ascii_slug).to_dict()
R['audit_type_state']=pd.crosstab(a.state,a.type).to_dict()
contra=a[(a.state=='URL is unknown to Google')&a.has_search_impressions]
R['contradictions']=contra.path.tolist()
R['ascii_unknown']=a[(a.state=='URL is unknown to Google')&~a.non_ascii_slug][['path','type']].values.tolist()

# ---------- pages: dedupe fragments ----------
p=S['05_page_queries']
R['page_total']=(int(p.impressions.sum()),int(p.clicks.sum()),len(p))

# ---------- quick wins ----------
q=pd.concat([S['02b_pos4_10_queries'].assign(src='02b'),S['02_page2_queries'].assign(src='02'),
             S['03_question_queries'].assign(src='03')],ignore_index=True)
q['nq']=q['query'].map(norm)
q=q.sort_values('impressions',ascending=False).drop_duplicates(['nq','path'])
# expected CTR curve (assumption, labelled): pos3 ~ 10%; used only for ranking
def exp_ctr(pos):
    t={1:.28,2:.15,3:.10,4:.07,5:.05,6:.04,7:.03,8:.025,9:.02,10:.018}
    return t.get(int(round(pos)),0.01) if pos>=1 else .28
qw=q[(q.avg_position>=4)&(q.avg_position<=20)].copy()
qw['est_extra_clicks_if_pos3']=(qw.impressions*0.10-qw.clicks).clip(lower=0).round()
qw['ctr_pct']=(qw.clicks/qw.impressions*100).round(2)
qw['band']=pd.cut(qw.avg_position,[3.99,6.5,10.5,20],labels=['4-6','7-10','11-20'])
# ---------- topics ----------
TOP=[('آزمون وکالت: منابع، آمادگی، دروس',r'منابع|منبع|کتاب|جزوه|امادگی|برنامه|مطالعه|دوره|کلاس|تست|نکته|مباحث|مواد مهم|اولویت|درس'),
     ('آزمون وکالت: ثبت‌نام، زمان، هزینه، شرایط',r'ازمون وکالت|امتحان وکالت|ثبت ?نام|زمان|تاریخ|هزینه|شرایط|شرط سنی|کارت|مدارک|حوزه|کانون|مرکز وکلا|انتخاب شهر|پایان خدمت|مصاحبه|نتایج|قبولی|کارآموزی|کاراموزی|تراز|رتبه|کلید|پاسخنامه|دفترچه'),
     ('سایر آزمون‌ها (سردفتری، مشاوره، قضاوت)',r'سردفتری|مشاوره حقوقی|مشاور حقوقی|قضاوت|کارشناس رسمی|ارشد'),
     ('خانواده: مهریه، طلاق، نامزدی',r'مهر|طلاق|نفقه|حضانت|جهیزیه|نامزد|ازدواج|زوج|زن |شوهر|همسر|عده|صیغه|فرزند'),
     ('کیفری: جرم، مجازات، دادگاه کیفری',r'سرقت|جرم|کیفر|مجازات|پابند|کلاهبرداری|دیه|قصاص|حبس|زندان|مشروط|سابقه|شکایت|شکواییه|افترا|توهین|تهدید|جعل|خیانت|رشوه|حد |تعزیر|مفقود|گمشده'),
     ('چک و اسناد تجاری',r'چک|سفته|برات'),
     ('آیین دادرسی و ادله',r'دادخواست|دعوا|دعاوی|ادله|اثبات|سوگند|قسم|صلاحیت|تجدید ?نظر|واخواهی|دادرسی|اجرای احکام|اعتراض|ابلاغ|دادگاه|شورای حل|صلح ?ی|داوری'),
     ('مدنی: عقود، اموال، ارث',r'عقد|صلح|قرارداد|معامله|اجاره|بیع|ارث|وصیت|ملک|سند|پیش ?فروش|هبه|ضمان|رهن|وکالت ?نامه|مدنی|تعهد|خیار|اموال|توقیف|حق ارتفاق'),
     ('تجارت و شرکت‌ها',r'تجارت|شرکت|ورشکست'),
     ('وکالت به‌عنوان شغل',r'وکیل|وکالت|وکلا'),]
def topic(s):
    n=norm(s)
    for name,rx in TOP:
        if name.startswith('آزمون وکالت') and not re.search('وکالت|وکلا|کانون',n):
            if not (name.endswith('دروس') and re.search('تست|جزوه|نکته',n)): continue
        if re.search(rx,n): return name
    return 'سایر'
q['topic']=q['query'].map(topic); qw['topic']=qw['query'].map(topic)
tp=q.groupby('topic').agg(queries=('query','count'),impressions=('impressions','sum'),clicks=('clicks','sum'),
     wavg_pos=('avg_position',lambda s:(s*q.loc[s.index,'impressions']).sum()/q.loc[s.index,'impressions'].sum())).sort_values('impressions',ascending=False)
tp['ctr_pct']=(tp.clicks/tp.impressions*100).round(2); tp['wavg_pos']=tp.wavg_pos.round(1)
tq=qw.groupby('topic').est_extra_clicks_if_pos3.sum(); tp['quickwin_est_extra_clicks']=tq
tp.to_csv(f'{OUT}/topics.csv',encoding='utf-8-sig')
qw=qw.sort_values('est_extra_clicks_if_pos3',ascending=False)
qw[['query','topic','impressions','clicks','ctr_pct','avg_position','band','est_extra_clicks_if_pos3','path','src']].to_csv(f'{OUT}/quick-wins-queries.csv',index=False,encoding='utf-8-sig')
R['qw_bands']=qw.groupby('band',observed=True).agg(n=('query','count'),impr=('impressions','sum'),clicks=('clicks','sum'),extra=('est_extra_clicks_if_pos3','sum')).to_dict()
# CTR gap pages: page-level, positions 1-10, CTR far below; from sheet 01
cg=S['01_ctr_gap_pages'].copy(); cg['topic']=cg.title.map(topic)
cg[['title','path','impressions','clicks','ctr_pct','avg_position','est_extra_clicks','top_queries','topic']].to_csv(f'{OUT}/quick-wins-pages-ctr.csv',index=False,encoding='utf-8-sig')

# ---------- cannibalization ----------
rows=[]
for _,r in p.iterrows():
    for m in re.finditer(r'([^؛]+?)\s*\(([\d,]+)،\s*رتبه\s*([\d.]+)\)',str(r.top10_queries)):
        rows.append((m.group(1).strip(),norm(m.group(1)),int(m.group(2).replace(',','')),float(m.group(3)),r.path,r.title))
pq=pd.DataFrame(rows,columns=['query','nq','impressions','avg_position','path','title'])
pq.to_csv(f'{OUT}/clean/v2_05_page_queries_long.csv',index=False,encoding='utf-8-sig')
# add query->page pairs from keyword sheets
allpairs=pd.concat([pq[['query','nq','impressions','avg_position','path']],q[['query','nq','impressions','avg_position','path']]])
allpairs=allpairs.sort_values('impressions',ascending=False).drop_duplicates(['nq','path'])
g=allpairs.groupby('nq').filter(lambda x: x.path.nunique()>1)
cn=g.sort_values(['nq','impressions'],ascending=[True,False])
cs=cn.groupby('nq').agg(query=('query','first'),pages=('path',lambda s:' | '.join(s)),n_pages=('path','nunique'),total_impr=('impressions','sum'),
    positions=('avg_position',lambda s:' | '.join(f'{x:.1f}' for x in s)),impr_split=('impressions',lambda s:' | '.join(str(int(x)) for x in s))).sort_values('total_impr',ascending=False)
cs['topic']=cs['query'].map(topic)
# page-pair aggregation
pairs={}
for nq,x in cn.groupby('nq'):
    ps=sorted(x.path.unique())
    for i in range(len(ps)):
        for j in range(i+1,len(ps)):
            k=(ps[i],ps[j]); pairs.setdefault(k,[0,0,[]]); pairs[k][0]+=1; pairs[k][1]+=int(x.impressions.sum()); pairs[k][2].append(x['query'].iloc[0])
pp=pd.DataFrame([(a_,b_,v[0],v[1],'؛ '.join(v[2][:6])) for (a_,b_),v in pairs.items()],columns=['page_a','page_b','shared_queries','shared_impr','examples']).sort_values('shared_impr',ascending=False)
cs.to_csv(f'{OUT}/cannibalization-queries.csv',encoding='utf-8-sig'); pp.to_csv(f'{OUT}/cannibalization-page-pairs.csv',index=False,encoding='utf-8-sig')

# ---------- keyword map comparison ----------
km=pd.read_csv('/mnt/project-files/seo-research/04-keyword-map.csv',encoding='utf-8-sig'); km['nq']=km.keyword.map(norm)
gq=allpairs.groupby('nq').agg(gsc_impr=('impressions','sum'),gsc_best_pos=('avg_position','min'),gsc_pages=('path',lambda s:' | '.join(dict.fromkeys(s)))).reset_index()
km=km.merge(gq,on='nq',how='left'); km['match']=km.gsc_impr.notna().map({True:'exact',False:''})
# partial: GSC query contains the map keyword
gl=gq.nq.tolist()
def partial(n):
    hits=gq[gq.nq.str.contains(re.escape(n))]
    return (int(hits.gsc_impr.sum()),len(hits)) if len(hits) else (0,0)
pt=km[km.match==''].nq.map(partial)
km.loc[km.match=='','partial_impr']=[x[0] for x in pt]; km.loc[km.match=='','partial_n']=[x[1] for x in pt]
km.loc[(km.match=='')&(km.partial_n>0),'match']='contained-in-gsc-query'
km.drop(columns=['nq']).to_csv(f'{OUT}/keyword-map-vs-gsc.csv',index=False,encoding='utf-8-sig')
R['km_match']=km.match.value_counts().to_dict()
R['km_by_priority']=pd.crosstab(km.priority,km.match).to_dict()
R['km_cluster']=km.groupby('cluster').agg(n=('keyword','count'),matched=('match',lambda s:(s!='').sum()),impr=('gsc_impr','sum')).sort_values('impr',ascending=False).to_dict()
# GSC demand not in map
inmap=set(km.nq)
q['in_map']=q.nq.isin(inmap)
R['gsc_not_in_map_by_topic']=q[~q.in_map].groupby('topic').impressions.sum().sort_values(ascending=False).to_dict()
R['gsc_in_map_impr']=int(q[q.in_map].impressions.sum()); R['gsc_total_impr']=int(q.impressions.sum()); R['gsc_n']=len(q)
json.dump(R,open('R.json','w'),ensure_ascii=False,indent=1,default=str)
print(tp.to_string()); print(qw.head(25)[['query','impressions','clicks','avg_position','est_extra_clicks_if_pos3','path']].to_string())
print(cs.head(25).to_string()); print(pp.head(15).to_string())
print(km.match.value_counts()); print(pd.crosstab(km.priority,km.match)); print(R['gsc_not_in_map_by_topic'], R['gsc_in_map_impr'],R['gsc_total_impr'])
print(km[km.match=='exact'].sort_values('gsc_impr',ascending=False)[['keyword','cluster','priority','gsc_impr','gsc_best_pos','gsc_pages']].head(30).to_string())
print('contradictions',len(contra),contra.path.tolist()[:20]); print(R['ascii_unknown'])
