import os
from PIL import Image
import zpl

l = zpl.Label(width=100,height=50)
l.set_darkness(22)
height = 0
l.origin(4.59, 4.59)
l.write_text("1023934 - EVEREST MAXSKIN 9OZ 65%AL 35%LIO LP177", char_height=3.75, char_width=3.75)
l.endorigin()

l.origin(8.4, 1.25)
l.write_text("KAZZO CONFECCOES - 06.209.148/0002-06", char_height=4.17, char_width=3.4)
l.endorigin()

l.origin(4.17, 7.5)
l.write_text("NOTA FISCAL", char_height=3.75, char_width=3.75)
l.endorigin()
    
l.origin(4.17, 10.42)
l.write_text("NF 1013736", char_height=3.75, char_width=3.75)
l.endorigin()
    
l.origin(29.17, 7.5)
l.write_text("LARGURA", char_height=3.75, char_width=3.75)
l.endorigin()
    
l.origin(31.25, 10.42)
l.write_text("m", char_height=3.75, char_width=3.75)
l.endorigin()
    
l.origin(54.17, 7.5)
l.write_text("NUANCE", char_height=3.75, char_width=3.75)
l.endorigin()
    
l.origin(56.25, 10.42)
l.write_text("", char_height=3.75, char_width=3.75)
l.endorigin()
    
l.origin(0, 13.92)
l.write_text("Lote 1386 / 1 - 9,000 Metros", char_height=4.17, char_width=6.67)
l.endorigin()
l.origin(0, 13.92)
l.write_text("", char_height=4.17, char_width=6.67,line_width=100)
l.endorigin()
    
#l.origin(50, 215)
#l.write_barcode('00110000013860001', barcode_type='BC', height=150, width_ratio=3, bar_type='N')
  

#print(l.dumpZPL())
l1 = l.dumpZPL()

l1 = l1.replace("^A0N", "^AR")

with open('etiqueta.zpl', 'w') as file:
    file.write(l1)
#l.preview()