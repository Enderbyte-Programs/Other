a
    e?#aq  ?                   @   s?  d Z ddlZddlZddlmZ ddlT ddlZe?? Zdd? Zdd? Z	zed	? W n   e	d
? e?
?  Y n0 ej?d?Zedkr?ed? z$edd?Ze?ed?? e??  W n,   ed? e	d? ed? e?
?  Y n0 dd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd? Zd d!? Ze? Ze?d"? e?d#? zed?ZW n,   ed$? e	d%? ed&? e?
?  Y nP0 zee? ? ?a!W n,   ed'? e	d(? ed)? e?
?  Y n0 e??  ed*? e"ed+et!? d, d-d.?a#t#?$?  e%ed/ej&d0d1?Z'e'j$e(d2? e%ed3d4ed5?Z)e)j$e*d2? e%ed6d4ed5?Z+e+j$e*d2? e%ed7d4ed5?Z,e,j$e*d2? e%ed8d9ed5?Z-e-j$e.d2? e%ed:d9ed5?Z/e/j$e.d2? e%ed;d9ed5?Z0e0j$e.d2? e%ed<d0ed5?Z1e1j$e2d2? e%ed=d0ed5?Z3e3j$e2d2? e?4?  ed>? e?
?  dS )?z?
list of exit codes:
0: Proper stop via closing window or using exit button
1: Failed to write data
2: Could not open data file
3: Could not read data file
?    N)?
messagebox)?*c                 C   s>   t dd?}|?dttj?? ? d t| ? d ? |??  d S )N?credits.logza+?[z] ?
)?open?write?str?datetimeZnow?close)Zstuff_to_log?f? r   ?IC:\Users\jorda\AppData\Local\Programs\Python\Python39\Scripts\credits.pyw?log   s    
(r   c                 C   s   t ? ??  t?d| ? d S )N?Credits)?TkZwithdrawr   Z	showerror)?errorr   r   r   r      s    
r   zProgram startedzCould not write log file?credata.datFz+could not find data file, will make new one?w+zCould not write data filezCould not write dataz Process crashed with exit code 1c                  C   sp   t d7 a z$tdd?} | ?tt ?? | ??  W n   td? td? Y n$0 tjdtt ? d dd	? td
? d S )N?   r   r   ?$Could not write credits to data file?could not write data file?	You have ?	 Credits.?Z	HelveticaZ18Zbold??textZfontzAdded 1 credit?	?datar   r   r	   r   r   r   ?lbl?	configure?r   r   r   r   ?addOne(   s    
r"   c                  C   sp   t d7 a z$tdd?} | ?tt ?? | ??  W n   td? td? Y n$0 tjdtt ? d dd	? td
? d S )N?
   r   r   r   r   r   r   r   r   zAdded 10 creditsr   r!   r   r   r   ?addTen6   s    
r$   c                  C   sp   t d7 a z$tdd?} | ?tt ?? | ??  W n   td? td? Y n$0 tjdtt ? d dd	? td
? d S )N?d   r   r   r   r   r   r   r   r   zAdded 100 creditsr   r!   r   r   r   ?
addHundredD   s    
r&   c                  C   sp   t d8 a z$tdd?} | ?tt ?? | ??  W n   td? td? Y n$0 tjdtt ? d dd	? td
? d S )Nr   r   r   r   r   r   r   r   r   zRemoved 1 creditr   r!   r   r   r   ?remOneR   s    
r'   c                  C   sp   t d8 a z$tdd?} | ?tt ?? | ??  W n   td? td? Y n$0 tjdtt ? d dd	? td
? d S )Nr#   r   r   r   r   r   r   r   r   zRemoved 10 creditsr   r!   r   r   r   ?remTena   s    
r(   c                  C   sp   t d8 a z$tdd?} | ?tt ?? | ??  W n   td? td? Y n$0 tjdtt ? d dd	? td
? d S )Nr%   r   r   r   r   r   r   r   r   zRemoved 100 creditsr   r!   r   r   r   ?
remHundredp   s    
r)   c                  C   s?   t ?dd?} | dkr|daz$tdd?}|?tt?? |??  W n   td? td? Y n$0 t	j
d	tt? d
 dd? td? d S )Nr   z,Are you sure you want to remove all credits?Tr   r   r   r   r   r   r   r   r   zRemoved all credits)r   ?askyesnor   r   r   r	   r   r   r   r   r    )?mr   r   r   r   ?clrall   s    
r,   c                  C   s^   t ?dd?} | dkrZzt?d? t?d? W n   d}Y n0 td? t ?dd? t??  d S )	Nr   z(Are you sure you want to clear all data?Tr   r   r   zCleared all dataz%Data clear complete. Will now restart)r   r*   ?os?remover   Zshowinfo?sys?exit)r+   ?ar   r   r   ?clrdat?   s    

r2   r   Z700x150zCould not open data filezCould not read dataz Process crashed with exit code 2z)Error: Data file contains unreadable datazError when reading data filez Process crashed with exit code 3zData file read sucessfullyr   r   r   r   ZExitZred)r   ?command?bg)ZsidezAdd 1 Creditz
lime green)r   r4   r3   zAdd 10 CreditszAdd 100 CreditszRemove 1 CreditZyellowzRemove 10 CreditszRemove 100 Creditsz
Remove AllzClear All DatazProcess ended with exit code 0)5?__doc__r-   r/   Ztkinterr   r
   ?getcwd?cwdr   r   r0   ?path?isfileZadsr   r   r   r	   r   r"   r$   r&   r'   r(   r)   r,   r2   r   ?root?titleZgeometry?int?readr   ZLabelr   ZpackZButtonZdestroyZbtnZTOPZbtn2ZLEFTZbtn3Zbtn4Zbtn5ZRIGHTZbtn6Zbtn7Zbtn8ZBOTTOMZbtn9Zmainloopr   r   r   r   ?<module>   s?   


