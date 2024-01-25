/*
buildr.db.sql written by Duncan Murray 24/1/2024
SQLite schema to manage building a PC - complete parts
maangement, requirements > design > parts > build steps

It will also manage the software functions via menu
driven selection, which maps to a software process that
gets kicked off from that menu

The output of this will allow auto production of
1. Checklist of requirements
2. mapping of requirements to parts
3. Shopping list needed to get remaining items
4. Build steps - and auto created build instructions
5. User steps for using the product
*/




------------------------------------------------------------------------
-- Menu

drop TABLE IF EXISTS p_menu;

create table p_menu (
id integer PRIMARY KEY,
menu_id TEXT,
parent_id TEXT, -- 0=root, 1=level 1, ....
sort_order INTEGER, -- how it appears on the list
menu_text TEXT,
help_text TEXT
);

insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('ROOT', NULL,0,'Root menu', 'hide this');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('AUDIO', 'ROOT',1,'Audio Tasks', 'Audio tasks');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('RADIO', 'ROOT',2,'Radio Tasks', 'Radio tasks');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('VIDEO', 'ROOT',3,'Video Tasks', 'Video tasks');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('ROBOT', 'ROOT',4,'Robot Tasks', 'Robot tasks');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('NETWORK','ROOT',5,'Network Tasks', 'Network tasks');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('DATA', 'ROOT',6,'Data Tasks', 'Data tasks');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('POWER', 'ROOT',7,'Power Tasks', 'Power tasks');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('MISC', 'ROOT',8,'Misc Tasks', 'Misc tasks');

insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text)  VALUES ('EXIT', 'ROOT',9,'Exit to system', 'Quit this menu and return to linux prompt (type menu to restart later)');

insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('AUDIO_PLAY', 'AUDIO',11,'MP3 Player', 'Play MP3s');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('AUDIO_SFX', 'AUDIO',12,'Sound Effects', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('RADIO_HF', 'RADIO',21,'Scan HF', 'Set SDR to scan HF channels');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('RADIO_VHF', 'RADIO',22,'Scan VHF', 'Set SDR to scan VHF channels');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('RADIO_UHF', 'RADIO',23,'Scan UHF', 'Set SDR to scan UHF channels');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('RADIO_TX', 'RADIO',24,'Transmit', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('VIDEO_PLAY', 'VIDEO',31,'Play video', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('VIDEO_CAM', 'VIDEO',32,'Camera', 'use camera to take photo');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('VIDEO_REC', 'VIDEO',33,'Record video', 'use camera');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('ROBOT_TEST', 'ROBOT',41,'Robot Self test', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('NETWORK_WIFI_LIST', 'NETWORK',51,'List Wifi devices', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('NETWORK_CONN', 'NETWORK',52,'Connect to device', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('NETWORK_DISC', 'NETWORK',53,'Disconnect a device', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('DATA_LIST', 'DATA',61,'List summary of attached storage', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('DATA_CP_A_C', 'DATA',62,'Copy USB-A to USB-C', 'Full disk copy');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('DATA_CP_C_A', 'DATA',63,'Copy USB-C to USB-A', 'Full disk copy');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('POWER_USAGE', 'POWER',71,'Show Power usage', 'Show usage');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('POWER_SAVE', 'POWER',72,'Enter Power save mode', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('POWER_FULL', 'POWER',73,'Full Power all devices', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('MISC_01', 'MISC',81,'Misc Task Group 1', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('MISC_01_a', 'MISC_01',81.1,'Misc Task 1a', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('MISC_01_b', 'MISC_01',81.1,'Misc Task 1b', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('MISC_01_c', 'MISC_01',81.1,'Misc Task 1c', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('MISC_02', 'MISC',82,'Misc Task 2', '');
insert into p_menu (menu_id, parent_id, sort_order, menu_text, help_text) VALUES ('MISC_03', 'MISC',83,'Misc Task 3', '');



------------------------------------------------------------------------
-- Parts and Types
drop TABLE IF EXISTS o_parts;
drop TABLE IF EXISTS o_part_types;

CREATE TABLE IF NOT EXISTS o_part_types (
id integer PRIMARY KEY,
part_type_desc TEXT
);

insert into o_part_types (part_type_desc) values ( 'Unknown');
insert into o_part_types (part_type_desc) values ( 'Electronic');
insert into o_part_types (part_type_desc) values ( 'Metal');
insert into o_part_types (part_type_desc) values ( 'Misc');
insert into o_part_types (part_type_desc) values ( 'Software');
insert into o_part_types (part_type_desc) values ( 'Service');



CREATE TABLE IF NOT EXISTS o_parts (
id integer PRIMARY KEY,
nme TEXT,
part_type_id INTEGER,
dsc TEXT,
quant INTEGER,
FOREIGN KEY(part_type_id) REFERENCES o_part_types(id)
);

insert into o_parts (nme, part_type_id, dsc, quant) values ( 'Rasb PI Zero', 1,  'Rasb PI Zero - main CPU', 2);
insert into o_parts (nme, part_type_id, dsc, quant) values ( 'SDR Radio V4', 1,  'SDR RAdio via USB', 1);
insert into o_parts (nme, part_type_id, dsc, quant) values ( 'Metal Case', 2,  '', 1);
insert into o_parts (nme, part_type_id, dsc, quant) values ( 'Audio Amp', 1,  '', 1);
insert into o_parts (nme, part_type_id, dsc, quant) values ( 'Antenna', 1,  '', 1);
insert into o_parts (nme, part_type_id, dsc, quant) values ( 'Resistors', 1,  '', 1);


------------------------------------------------------------------------
-- Requirements

drop TABLE IF EXISTS f_bus_requirement;
CREATE TABLE IF NOT EXISTS f_bus_requirement (
id integer PRIMARY KEY,
name TEXT,
details TEXT
);
insert into f_bus_requirement (name, details) VALUES ( '', '');
insert into f_bus_requirement (name, details) VALUES ( '', '');
insert into f_bus_requirement (name, details) VALUES ( '', '');
insert into f_bus_requirement (name, details) VALUES ( '', '');
insert into f_bus_requirement (name, details) VALUES ( '', '');


COMMIT;