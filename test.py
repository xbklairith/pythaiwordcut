# -*- coding: utf-8 -*-

import pythaiwordcut as ptw
import time

# print ptw.search(u'ทดสอบตัดคำ')[1]
import time
start_time = time.time()
pt = ptw.wordcut()
print "|".join(pt.segment(u'ดิฉันมีโอกาสพูดคุยกับ ผอ.องค์การสะพานปลา ในรายการ คิดลึกคิดไกลไปกับหอการค้า เกี่ยวกับเรื่องการประมงผิดกฎหมาย หรือ IUU Fishing ที่ไทยได้ใบเหลืองจาก สหภาพยุโรปมาเมื่อปีที่แล้ว และต้องพัฒนามาตรฐานต่างๆ เพื่อให้ อียูปลดล็อกใบเหลืองออก มิฉะนั้นแล้ว ประเทศไทยอาจมีปัญหาเรื่องการส่งออกสัตว์น้ำไปยังสหภาพยุโรป'))

print("--- %s seconds ---" % (time.time() - start_time))
