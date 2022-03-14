get_properties_sql = '''
SELECT * FROM  habi_db.property p INNER JOIN (SELECT * FROM habi_db.status_history sh WHERE sh.update_date IN 
(SELECT max(sh2.update_date) FROM habi_db.status_history sh2 WHERE sh2.property_id = sh.property_id)) sh 
ON p.id = sh.property_id INNER JOIN habi_db.status s 
on s.id = sh.status_id and (s.name = 'pre_venta' or s.name = 'en_venta' or s.name = 'vendido') 
AND p.address<>''
'''
