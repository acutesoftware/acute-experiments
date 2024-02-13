/* notes_buildr.sql		written by Duncan Murray 25/1/2024

Notes on testing the buildr database 


*/


select * from p_menu op where op.menu_id in (select ip.parent_id from p_menu ip);

select parent_id, menu_id from p_menu where menu_id != 'ROOT'
 order by  sort_order;

 select * from o_parts;
 
select tp.part_type_desc, prt.nme, prt.dsc, prt.quant 
from o_parts prt, o_part_types tp
where prt.part_type_id = tp.id
order by 1,2;

select * from o_part_types;

