import json,collections,re,csv
from classify import *
rows=json.load(open('agg2.json',encoding='utf8'))
PS=json.load(open('pagestats.json',encoding='utf8'))
AM=json.load(open('art_meta.json',encoding='utf8'))
AM['what-is-a-mortgage-contract']={'title':'عقد رهن چیست؟ نکاتی که دانستنشان ضروری است - دادرز','words':2204}
T=collections.defaultdict(lambda:[0,0,0.0]); B=collections.defaultdict(lambda:[0,0]); G=[0,0]
for q,p,i,c,pos in rows:
    t,k=assign(q,p)
    if t=='topic':
        a=T[k]; a[0]+=i;a[1]+=c;a[2]+=pos*i
    elif t=='book':
        B[k][0]+=i;B[k][1]+=c
    elif t=='general':
        G[0]+=i;G[1]+=c
A='https://dadrose.com/'; C='https://dadrose.com/courses/'
AZ='https://azmoon.dadrose.com/azmoon/civil'; AZQ='https://azmoon.dadrose.com/questions/civil'; AZN='https://azmoon.dadrose.com/notes/civil'
J=('حقوق-مدنی-1-تا-8','جامع حقوق مدنی ۱ تا ۸')
E=('دوره-امهات-حقوق-مدنی','امهات حقوق مدنی (جمع‌بندی)')
NT=('نکته-و-تست-حقوق-مدنی','نکته و تست حقوق مدنی')
FREE=('تحلیل-سوالات-5-سال-اخیر-حقوق-مدنی','تحلیل سوالات ۵ سال اخیر حقوق مدنی (رایگان)')
BK={'2':('civil-law-book-2-property-ownership','حقوق مدنی ۲ اموال و مالکیت'),
'3':('civil-law-book-3-general-rules-contracts','حقوق مدنی ۳ قواعد عمومی قراردادها'),
'4':('civil-law-book-4-non-contractual-obligations','حقوق مدنی ۴ الزامات خارج از قرارداد'),
'5':('civil-law-book-5-family-law','حقوق مدنی ۵ حقوق خانواده'),
'6':('civil-law-book-6-nominate-contracts','حقوق مدنی ۶ عقود معین ۱'),
'7':('civil-law-book-7-nominate-contracts','حقوق مدنی ۷ عقود معین ۲'),
'8':('civil-law-book-8-preemption-will-inheritance','حقوق مدنی ۸ شفعه، وصیت و ارث')}
INH=('modern-diagrammatic-course-inheritance','دوره نوین و نموداری ارث')
CP=('دوره-جامع-آیین-دادرسی-مدنی-2','جامع آیین دادرسی مدنی')
NOCARD='(کارت جدا ندارد)'
R=[
('ahliyat','اشخاص و اهلیت (محجورین، اقامتگاه، غایب مفقودالاثر)','مدنی ۱',['man-missing'],[J,E],'اشخاص و اهلیت','A-جزئی','فقط «غایب مفقودالاثر» پوشش دارد؛ مقاله‌ی اهلیت/حجر/اقامتگاه نیست. تقاضای «مدنی ۱» در سطح کتاب بالاست و کل آن را صفحه‌ی دوره می‌گیرد.',''),
('amval','اموال و مالکیت (حق انتفاع، ارتفاق، همسایگی)','مدنی ۲',['eliminative-method-for-civil-law-2'],[BK['2'],J,E],'اموال و مالکیت / حق انتفاع / حقوق ارتفاقی / حقوق همسایگی','A','مقاله‌ی مفهومی مالکیت و اموال نیست؛ تنها مقاله‌ی «روش حذفی مدنی ۲» (راهبرد تست، ۰ نمایش در ۹۰ روز).',''),
('mavat','احیای موات و حیازت مباحات','مدنی ۲',[],[BK['2'],J],'حیازت مباحات و شکار','A','مقاله ندارد و در GSC نمایشی ثبت نشده.',''),
('waqf','وقف، حبس، عمری و رقبی','مدنی ۲',[],[E,J],'وقف و قبض / صحت و بطلان جزئی وقف / قبول و رد تولیت','A','مقاله ندارد؛ در GSC نمایشی ثبت نشده.',''),
('qavaed','قواعد عمومی قراردادها (شرایط اساسی، شروط، معامله فضولی)','مدنی ۳',['the-importance-of-civil-law-3-in-the-attorney-exam','types-of-stipulations-within-a-contract','unauthorized-transaction-and-discharge-of-obligations','disposing-of-anothers-property-without-authorization'],[BK['3'],J,E],'اعمال حقوقی و قراردادها / قواعد عمومی قراردادها','C-جزئی','سرفصل مدنی ۳ خوب پوشش داده شده (رتبه ۶٫۰)؛ مقاله‌های شروط ضمن عقد و معامله فضولی تقریباً نمایش ندارند. اکراه، اشتباه، تدلیس و خیارات مقاله‌ی جدا ندارند.',''),
('qasb','الزامات خارج از قرارداد و مسئولیت مدنی (غصب، اتلاف، تسبیب، استیفا، ایفای ناروا)','مدنی ۴',['special-civil-liability-law','civil-rights-study-4'],[BK['4'],J,E],'تعهدات و مسئولیت مدنی','B-جزئی','قانون مسئولیت مدنی خوب پوشش داده شده (رتبه ۴٫۷)؛ غصب/اتلاف/تسبیب/استیفا/ایفای ناروا مقاله ندارد.','ضمان قهری، مسئولیت مدنی (AC بالا، بدون نمایش در GSC)'),
('nikah','نکاح، مهریه و نفقه','مدنی ۵',['types-of-dowry','what-does-a-wifes-maintenance-cover','mahr-al-sunnah-or-the-dowry-of-lady-fatimah-al-zahra','how-to-seize-assets-for-dowry','return-of-engagement-gifts','laws-regarding-the-promise-of-marriage','who-does-the-dowry-belong-to'],[BK['5'],J,E],'خانواده','B-جزئی','مقاله‌ها مصرف‌کننده‌محورند؛ شرایط صحت نکاح، موانع و نکاح موقت مقاله ندارد. حدود نیمی از نمایش‌ها مهرالسنه‌ی ۱۴۰۵ است.',''),
('talaq','طلاق (انواع، رجوع، عده، خلع و مبارات)','مدنی ۵',['stages-of-consensual-divorce'],[BK['5'],J,E],'خانواده','B','تنها مقاله «مراحل طلاق توافقی» است و رتبه‌ی میانگین آن ۴۹٫۲؛ سرفصل‌های آزمونی طلاق مقاله ندارد.',''),
('olad','اولاد، نسب و حضانت','مدنی ۵',['termination-of-custody','family-court'],[BK['5'],J,E],'خانواده','B','دو مقاله هست ولی نمایش تقریباً صفر و رتبه ۵۰ به بعد؛ نسب و ولایت قهری مقاله ندارد.',''),
('bay','بیع و خیارات','مدنی ۶',['laws-on-pre-sale-of-buildings','pre-sale-contract-document'],[BK['6'],J,E],'عقد بیع','A','فقط پیش‌فروش ساختمان؛ مقاله‌ی «بیع و خیارات» نیست. هر دو مقاله‌ی پیش‌فروش نمایش ندارند.',''),
('ejare','اجاره','مدنی ۶',['if-the-tenant-does-not-vacate','key-points-of-the-lease-agreement'],[BK['6'],J,E],'اجاره و عاریه','B','مقاله هست ولی رتبه‌ی میانگین ۸٫۱ و نشانی ?p=22450 هم در گوگل نمایش می‌گیرد. دوره‌ی جامع قانون موجر و مستأجر ۵۶ و ۷۶ را هم تدریس می‌کند.','فسخ قرارداد اجاره (AC متوسط)'),
('qarz','قرض','مدنی ۶',[],[BK['6'],J],NOCARD,'A','مقاله ندارد.',''),
('sherkat','شرکت (عقد شرکت و مشاع)','مدنی ۶',['where-are-the-common-areas-of-the-building'],[BK['6'],J],'رهن، صلح و شرکت','A','مقاله‌ی «مشاعات ساختمان» به مشاع آپارتمان می‌پردازد، نه عقد شرکت مدنی.',''),
('jaale','جعاله','مدنی ۶',[],[BK['6'],J],NOCARD,'A','مقاله ندارد.',''),
('sulh','صلح','مدنی ۶',['what-is-a-peace-contract','writing-a-peace-agreement'],[BK['6'],J,E],'رهن، صلح و شرکت','C','دو مقاله‌ی قوی (رتبه ۶٫۰ و ۶٫۴). پرنمایش‌ترین موضوع مدنی در GSC؛ فرصت بهینه‌سازی CTR روی پرسش تک‌کلمه‌ی «صلح».',''),
('ariye','عاریه','مدنی ۷',[],[BK['7'],J],'اجاره و عاریه','A','مقاله ندارد.',''),
('vadia','ودیعه','مدنی ۷',[],[BK['7'],J],NOCARD,'A','مقاله ندارد.',''),
('mozarebe','مضاربه','مدنی ۷',[],[BK['7'],J],NOCARD,'A','مقاله ندارد.',''),
('mozarea','مزارعه و مساقات','مدنی ۷',[],[BK['7'],J],NOCARD,'A','مقاله ندارد.',''),
('vekalat','وکالت (عقد وکالت)','مدنی ۷',[],[BK['7'],J],'وکالت، ضمان و حواله','A','مقاله‌ی عقد وکالت نیست (مقاله‌های «وکالت» سایت درباره‌ی آزمون و حرفه‌ی وکالت‌اند).',''),
('zaman','ضمان (ضمان عقدی)','مدنی ۷',[],[BK['7'],J],'وکالت، ضمان و حواله','A','تنها مقاله‌ی «ضمانت در حقوق تجارت» است و ناظر به قانون تجارت؛ برای مدنی لینک نشود.',''),
('hawale','حواله','مدنی ۷',[],[BK['7'],J],'وکالت، ضمان و حواله','A','مقاله ندارد.',''),
('kafalat','کفالت','مدنی ۷',[],[BK['7'],J],NOCARD,'A','مقاله ندارد.',''),
('rahn','رهن','مدنی ۷',['what-is-a-mortgage-contract'],[BK['7'],J,E],'رهن، صلح و شرکت','B-نمایش‌ندارد','مقاله‌ی ۲٬۲۰۴ کلمه‌ای هست ولی در ۹۰ روز فقط ۴ نمایش گرفته؛ بررسی ایندکس و نشانی لازم است.',''),
('hebe','هبه','مدنی ۷',[],[BK['7'],J],NOCARD,'A','مقاله ندارد.',''),
('ers','ارث (طبقات، سهم‌الارث، موانع)','مدنی ۸',['inheritance-laws'],[BK['8'],INH,J,E],'ارث و وصیت','B','تنها مقاله خبرمحور است («ارث دختر و پسر مساوی شد؟»؛ بیشتر نمایش‌ها همین یک پرسش)؛ مقاله‌ی آموزشی طبقات ارث و سهم نیست. CTR فقط ۰٫۷٪.',''),
('vasiat','وصیت','مدنی ۸',['types-of-wills'],[BK['8'],J,E],'ارث و وصیت','B-نمایش‌ندارد','مقاله هست ولی ۵ نمایش در ۹۰ روز.',''),
('shufa','شفعه و اخذ به شفعه','مدنی ۸',[],[BK['8'],J],NOCARD,'A','مقاله ندارد.',''),
('adele','ادله اثبات دعوا (اقرار، سند، شهادت، امارات، قسم)','ادله (مدنی/آ.د.م)',['means-of-proof-in-legal-proceedings','oath-in-law'],[CP,J,E],'(در کارت‌های مدنی نیست)','C','دو مقاله‌ی قوی؛ CTR ٪۲٫۱ و بخشی از پرسش‌ها کیفری است. دوره‌ی جامع آیین دادرسی مدنی «ادله اثبات دعوا» دارد.',''),
('mostasna','مستثنیات دین','ادله/اجرا',['what-are-the-exceptions-to-debt'],[CP,J],NOCARD,'B','رتبه ۹٫۴ و ۵ کلیک؛ پوشش مستثنیات دین در دوره‌ها تأیید نشد (باید مدرس تأیید کند).',''),
]
def pstat(s):
    v=PS.get(s)
    return v if v else (0,0,None)
out=[]
for key,name,book,arts,courses,card,flag,note,ac in R:
    t=T.get(key,[0,0,0.0]); imps,clk=t[0],t[1]; pos=round(t[2]/t[0],1) if t[0] else None
    out.append(dict(key=key,name=name,book=book,arts=arts,courses=courses,card=card,flag=flag,note=note,ac=ac,imps=imps,clk=clk,pos=pos))
json.dump(dict(rows=out,B=B,G=G),open('rows.json','w',encoding='utf8'),ensure_ascii=False)
with open('../map.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f)
    w.writerow(['row_type','topic_fa','syllabus_book','gsc_topic_impressions_90d','gsc_topic_clicks_90d','gsc_topic_avg_position','best_article_url','best_article_title','best_article_impressions_90d','best_article_clicks_90d','best_article_avg_position','other_articles','open_courses_verified_2026_10_15','azmoon_public_pages','azmoon_topic_card_on_page','gap_flag','note','autocomplete_signal'])
    for r in out:
        a0=r['arts'][0] if r['arts'] else ''
        st=pstat(a0) if a0 else (0,0,None)
        title=AM.get(a0,{}).get('title','') if a0 else ''
        w.writerow(['topic',r['name'],r['book'],r['imps'],r['clk'],r['pos'] or '',(A+a0+'/') if a0 else '',title,st[0] if a0 else '',st[1] if a0 else '',st[2] if (a0 and st[2]) else '',' | '.join(A+x+'/' for x in r['arts'][1:]),' | '.join(C+c[0]+'/' for c in r['courses']),' | '.join([AZ,AZQ,AZN]),r['card'],r['flag'],r['note'],r['ac']])
    for n in '12345678':
        bi=B.get(n,[0,0])
        w.writerow(['book_level_queries','پرسش‌های سطح کتاب «مدنی %s»'%n,'مدنی '+n,bi[0],bi[1],'','','','','','','','','','','','جمع پرسش‌هایی مثل «مدنی %s» و «سرفصل مدنی %s»؛ بین مبحث‌ها تقسیم نشده'%(n,n),''])
    w.writerow(['general_queries','پرسش‌های عمومی «حقوق مدنی» (جزوه، تست، تدریس، آموزش)','همه',G[0],G[1],'','','','','','','','','','','','بدون مقاله‌ی هاب؛ بیشترش را صفحه‌ی دوره می‌گیرد',''])
print('ok',len(out),sum(r['imps'] for r in out),dict(B),G)
