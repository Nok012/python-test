##### Solution:
    ตัวแปร highest_number_of_vehicles เก็บค่าจำนวนรถยานพหนะในแต่ละ intersections.
    โดยการ loop ค่าจาก data ที่เป็น type dictionary แล้วเอาเฉพาะ value เก็บใส่ตัวแปร highest_number_of_vehicles.
    ตัวแปร max_value คือค่าจำนวนรถยานพหนะสูงสุดที่หามาจากตัวแปร highest_number_of_vehicles.
    หลังจากนั้นนำมา loop อีกรอบจาก data โดยมีเงื่อนไขว่า ถ้า value มีค่าเท่ากับ ตัวแปร max_value.
    ให้เพิ่มไปไหนตัวแปร results โดยค่าที่เก็บจะเป็น key ของ value นั้น.

##### Time Complexity 
   - ความซับซ้อนของเวลา คือ O(n) โดยที่ n คือจำนวนข้อมูลของ data
