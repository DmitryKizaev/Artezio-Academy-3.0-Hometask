# Задание 1

CREATE DATABASE IF NOT EXISTS my_office;

USE my_office;

CREATE TABLE IF NOT EXISTS personal_info (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	position_id VARCHAR(30) NOT NULL
    );

CREATE TABLE IF NOT EXISTS positions (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	position VARCHAR(30) NOT NULL,
    	salary INT NOT NULL
);

INSERT INTO positions (id, position, salary) VALUES (null, 'Boss', 100000);
INSERT INTO positions (id, position, salary) VALUES (null, 'Secretary', 34000);
INSERT INTO positions (id, position, salary) VALUES (null, 'Courier', 15000);
INSERT INTO positions (id, position, salary) VALUES (null, 'Designer', 75000);
INSERT INTO positions (id, position, salary) VALUES (null, 'Cleaning manager', 12000);

SELECT * FROM positions;

INSERT INTO personal_info (id, first_name, last_name, position_id) VALUES (null, 'Angela', 'Ivanova', 2);
INSERT INTO personal_info (id, first_name, last_name, position_id) VALUES (null, 'Stepan', 'Petrovichsky', 1); 
INSERT INTO personal_info (id, first_name, last_name, position_id) VALUES (null, 'Vitya', 'Zabegailo', 3);
INSERT INTO personal_info (id, first_name, last_name, position_id) VALUES (null, 'Petya', 'Zabegailo', 3);
INSERT INTO personal_info (id, first_name, last_name, position_id) VALUES (null, 'Feoktist', 'Przhevalsky', 4);

SELECT personal_info.first_name, personal_info.last_name, positions.position, positions.salary
FROM personal_info INNER JOIN positions ON personal_info.position_id=positions.id;

# Задание 2

# показать всех сотрудников с зарплатой меньше 30 000 рублей

SELECT personal_info.first_name, personal_info.last_name, positions.salary
FROM personal_info INNER JOIN positions ON personal_info.position_id=positions.id
WHERE positions.salary < 30000;

# показать всех сотрудников, занимающих определённую должность, и с зарплатой меньше 30 000 рублей

# курьеры: выдаст 2 ребят

SELECT personal_info.first_name, personal_info.last_name, positions.salary
FROM personal_info INNER JOIN positions ON personal_info.position_id=positions.id
WHERE positions.salary < 30000 AND positions.position = "Courier";

# дизайнеры: не выдаст ничего, зарплаты больше 30к

SELECT personal_info.first_name, personal_info.last_name, positions.salary
FROM personal_info INNER JOIN positions ON personal_info.position_id=positions.id
WHERE positions.salary < 30000 AND positions.position = "Designer";

# проверим, все ли работает как надо
# устроим коммунизм и уравняем ЗП курьеров и дизайнеров

UPDATE positions SET salary=25000 WHERE id IN (3,4);

# снова тот же самый вывод информации, для тех и для других

SELECT personal_info.first_name, personal_info.last_name, positions.salary
FROM personal_info INNER JOIN positions ON personal_info.position_id=positions.id
WHERE positions.salary < 30000 AND positions.position = "Courier";

SELECT personal_info.first_name, personal_info.last_name, positions.salary
FROM personal_info INNER JOIN positions ON personal_info.position_id=positions.id
WHERE positions.salary < 30000 AND positions.position = "Designer";

# всё работает, мы восхитительны

# Задание 3

CREATE TABLE submission (
id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
boss_id INT,
peon_id INT
);

# линейный персонал подчиняется боссу, его id 2
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 2, 1);
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 2, 3);
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 2, 4);
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 2, 5);

# покажем подчиненных босса через его id
SELECT peon_table.first_name, peon_table.last_name
FROM submission
JOIN personal_info AS boss_table ON submission.boss_id = boss_table.id
JOIN personal_info AS peon_table ON submission.peon_id = peon_table.id
WHERE boss_table.id = 2;

# курьеры подчиняются линейному персоналу
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 1, 3);
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 5, 3);
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 1, 4);
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 5, 4);

# а сам босс пусть будет подкаблучник и подчиняется секретарше
INSERT INTO submission (id, boss_id, peon_id) VALUES (null, 1, 2);

# покажем начальников курьера по имени Петя
SELECT boss_table.first_name, boss_table.last_name
FROM submission
JOIN personal_info AS boss_table ON submission.boss_id = boss_table.id
JOIN personal_info AS peon_table ON submission.peon_id = peon_table.id
JOIN positions ON positions.id = peon_table.position_id
WHERE peon_table.first_name = "Petya";

# проверим себя и покажем все отношения в виде "босс -> подчиненный"
SELECT boss_id, boss_table.first_name, boss_table.last_name,
peon_id, peon_table.first_name, peon_table.last_name 
FROM submission
JOIN personal_info AS boss_table ON submission.boss_id = boss_table.id
JOIN personal_info AS peon_table ON submission.peon_id = peon_table.id
JOIN positions ON positions.id = peon_table.position_id;