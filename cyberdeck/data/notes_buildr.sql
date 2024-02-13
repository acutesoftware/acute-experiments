/* notes_buildr.sql		written by Duncan Murray 25/1/2024

Notes on testing the buildr database 


*/


select * from p_menu op where op.menu_id in (select ip.parent_id from p_menu ip);

select parent_id, menu_id from p_menu where menu_id != 'ROOT'
 order by  sort_order;

 ---------------------------------------------------------------
 -- Parts 
 
 select * from o_parts;

select * from o_part_types;
 
select tp.part_type_desc, prt.nme, prt.dsc, prt.quant 
from o_parts prt, o_part_types tp
where prt.part_type_id = tp.id
order by 1,2;


-------------------------------------------------------------------
-- Menu 

select id, menu_id, parent_id, sort_order, menu_text, help_text,
'fn_' || menu_id || '.py' as script_name,
'from ' || lower(parent_id) || ' import fn_' || menu_id || ' as mod_' || lower(menu_id) as script_import,
'C:\C_DATA\dev\src\acute_experiment\cyberdeck\src\' || lower(menu_id) || '\' as script_folder
 from p_menu;
