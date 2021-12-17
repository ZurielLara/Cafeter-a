create database CafeteriaIS;
use CafeteriaIS;
CREATE TABLE Empleados (
    idEmpleado INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(25) NOT NULL,
    apellidoP VARCHAR(25) NOT NULL,
    apellidoM VARCHAR(25) NOT NULL,
    numContacto VARCHAR(10) NOT NULL,
    numEmergencia VARCHAR(10) NOT NULL,
    cargo VARCHAR(25) NOT NULL,
    users VARCHAR(10) NOT NULL,
    Password VARCHAR(16) NOT NULL
);
 CREATE TABLE Pedidos (empleados
    idPedido INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    tipoBebida VARCHAR(25) NOT NULL,
    sabor VARCHAR(25) NOT NULL,
    tamaño VARCHAR(25) NOT NULL,
    tipoLeche VARCHAR(25),
    extra0 VARCHAR(15),
    extra1 VARCHAR(15),
    extra2 VARCHAR(15),
    extra3 VARCHAR(15),
    extra4 VARCHAR(15),
    cantidad INT NOT NULL,
    tipoConsumo VARCHAR(11),
    nombre VARCHAR(15) NOT NULL
    
);
 CREATE TABLE Pago (
    idPago INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    metodoPago VARCHAR(15) NOT NULL,
    idPedido INT NOT NULL
);
CREATE TABLE ReportesVentas (
    idVenta INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    producto VARCHAR(50) NOT NULL,
    cantTotalProducto INT NOT NULL,
    montoUnidad FLOAT NOT NULL,
    montoTotal FLOAT NOT NULL,
    fecha VARCHAR(15) NOT NULL,
    idPedido INT NOT NULL
);
CREATE TABLE MateriaPrima (
    idMatPrima INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nomMatPrima VARCHAR(25) NOT NULL,
    categoria VARCHAR(15) NOT NULL
);
CREATE TABLE Inventario (
    cantIngresada INT,
    cantSalida INT,
    cantRestante INT NOT NULL,
    fechaCaducidad VARCHAR(10) NOT NULL,
    fechaRegistro VARCHAR(10) NOT NULL,
    idMatPrima INT NOT NULL
);
CREATE TABLE Proveedores (
	idProveedor int primary key not null auto_increment,
    nomProveedor VARCHAR(25),
    numProveedor VARCHAR(10),
    idMatPrima INT NOT NULL
);
CREATE TABLE Alertas (
	idAlerta int primary key not null auto_increment,
    tipoAlerta VARCHAR(25) NOT NULL,
    idMatPrima INT NOT NULL
);