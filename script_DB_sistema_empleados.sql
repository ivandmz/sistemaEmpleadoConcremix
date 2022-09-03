create schema if not exists sistema_empleados;
use sistema_empleados;

create table if not exists empleados (
	id int not null auto_increment primary key,
    nombre_completo varchar(255),
    foto varchar(255),
    fecha_nac date,
    dni varchar(255),
    telefono varchar(255),
    correo varchar(255),
    direccion varchar(255),
    puesto varchar(255)
);
drop table if exists empleados;

SELECT * FROM `sistema_empleados`.`empleados`;
INSERT INTO `sistema_empleados`.`empleados` (`nombre_completo`, `fecha_nac`, `dni`, `telefono`, `correo`, `direccion`, `puesto`) VALUES ('Muñoz, Ivan', '2022/02/28', '32812421', '2612155911', 'ivandariomunioz@gmail.com', 'Juan Jose Paso 856', 'Encargado Laboratorio');
