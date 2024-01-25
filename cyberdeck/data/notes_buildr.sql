/* notes_buildr.sql		written by Duncan Murray 25/1/2024

Notes on testing the buildr database 


*/


select * from p_menu op where op.menu_id in (select ip.parent_id from p_menu ip);

select parent_id, menu_id from p_menu where menu_id != 'ROOT'
 order by  sort_order;

