-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-12-2023 a las 19:33:09
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `qicdatabase`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `archivo_servicios`
--

CREATE TABLE `archivo_servicios` (
  `id_servicio` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `id_mesa` int(11) NOT NULL,
  `tipo_servicio` varchar(45) NOT NULL,
  `tamano_grupo` int(11) NOT NULL,
  `senia` int(45) DEFAULT NULL,
  `hora_inicio` int(45) NOT NULL,
  `hora_fin` int(45) NOT NULL,
  `fecha` date NOT NULL,
  `monto_final` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `archivo_servicios`
--

INSERT INTO `archivo_servicios` (`id_servicio`, `id_cliente`, `id_mesa`, `tipo_servicio`, `tamano_grupo`, `senia`, `hora_inicio`, `hora_fin`, `fecha`, `monto_final`) VALUES
(1, 41, 1, 'mesa', 1, 0, 1408, 1411, '2023-11-26', 5000),
(2, 41, 4, 'mesa', 2, 1000, 1, 11, '2023-11-27', 4000),
(3, 38, 1, 'mesa', 3, 0, 1136, 1137, '2023-12-01', 2800);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) NOT NULL,
  `email` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `nombre`, `apellido`, `telefono`, `email`) VALUES
(33, 'Maria', 'Claudia', '1130099405', 'mariaclaudia@gmail.com'),
(34, 'Maria', 'Fernanda', '1130000400', 'mariaclaudia@gmail.com'),
(36, 'Maria', 'Claudia', '1130000400', 'mariaclaudia@gmail.com'),
(37, 'Maria', 'Claudia', '1130000404', 'mariaclaudia@gmail.com'),
(38, 'Josefina', 'Estrosis', '0303030303', 'josefinaestrosis@gmail.com'),
(39, 'Mario', 'Claudio', '1130000403', 'marioclaudio@gmail.com'),
(40, 'Juan', 'Martinez', '1190478362', 'juanmartinez38@gmail.com'),
(41, 'Melina', 'Pereyra Balaguer', '1141438332', 'melunisan@hotmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id_empleado` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `direccion` varchar(200) NOT NULL,
  `cuit` varchar(45) DEFAULT NULL,
  `cuil` varchar(45) DEFAULT NULL,
  `username` varchar(25) NOT NULL,
  `password` char(110) NOT NULL,
  `is_admin` varchar(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id_empleado`, `nombre`, `apellido`, `telefono`, `email`, `direccion`, `cuit`, `cuil`, `username`, `password`, `is_admin`) VALUES
(1, 'Juansote', 'Martinez', '1130485930', 'juanmartinez38@gmail.com', 'Av. Suarez 3371', '302049120', '120392103', 'jmartinez', 'pbkdf2:sha256:260000$P2e3hJT2DfB2dYes$2765655e3533e69ddbc3240cf88523813da77b123e686b56bd711ad007834eda', 'User'),
(2, 'Maria', 'Claudia', '1130000403', 'mariaclaudia@gmail.com', 'Av. Suarez 3371', '302013033', '', '', '', 'User'),
(3, 'Lucas', 'Boniardi', '1139232416', 'lboniardi@gmail.com', 'callefalsa123', '20382681852', '', 'lboniardi', 'pbkdf2:sha256:260000$P2e3hJT2DfB2dYes$2765655e3533e69ddbc3240cf88523813da77b123e686b56bd711ad007834eda', 'Admin'),
(4, 'Taiel', 'Cleiman', '1000000000', 'cleimantaiel@gmail.com', 'Calle Falsa 123', '202020202', '202020202', 'tcleiman', 'pbkdf2:sha256:260000$P2e3hJT2DfB2dYes$2765655e3533e69ddbc3240cf88523813da77b123e686b56bd711ad007834eda', 'Admin'),
(5, 'Paul', 'Longoni', '1122334455', 'paul@test.com', 'Calle Falsa 123', '112233445566', '112233445566', 'paul', 'sha256$4DHpzwOajhKYJYB0$4457389255e91440c5bf7262f2069b855eb1dcb03e11ac66e39db430ab8bdc09', 'Admin'),
(6, 'Melina', 'Pereyra', '1141438332', 'naa.mii.1996@gmail.com', 'Tandil', '27395225652', '', 'NaaMii', 'sha256$wBmBPsOrliJRaAW3$365a7306e626ad6b0643efa8b3ddc22f86e15a12afc6656d4593a03cea90b4cf', 'Usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mesas`
--

CREATE TABLE `mesas` (
  `id_mesa` int(11) NOT NULL,
  `estado` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `mesas`
--

INSERT INTO `mesas` (`id_mesa`, `estado`) VALUES
(1, 'disponible'),
(2, 'disponible'),
(3, 'no disponible'),
(4, 'disponible'),
(5, 'disponible'),
(6, 'disponible'),
(7, 'disponible'),
(8, 'disponible'),
(9, 'disponible'),
(10, 'disponible'),
(11, 'disponible'),
(12, 'disponible'),
(13, 'disponible'),
(14, 'disponible'),
(15, 'disponible'),
(16, 'disponible'),
(17, 'disponible'),
(18, 'disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `precio` int(11) NOT NULL,
  `disponible` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre`, `precio`, `disponible`) VALUES
(1, 'Pollo Frito para 2', 2200, 'si'),
(2, 'Fideos a la Bolognesa', 1300, 'si'),
(3, 'Suprema de pollo', 4000, 'si'),
(4, 'Guarnición de papas', 700, 'no'),
(5, 'Helado', 200, 'Sí'),
(6, 'Hamburguesa con papitas', 5800, 'Sí'),
(7, 'Hamburguesa con papitas', 5800, 'Sí');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_mesa`
--

CREATE TABLE `productos_mesa` (
  `id_producto` int(11) NOT NULL,
  `id_mesa` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `id_mesa_producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `id_servicio` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `id_mesa` int(11) NOT NULL,
  `tipo_servicio` varchar(45) NOT NULL,
  `tamano_grupo` int(11) NOT NULL,
  `senia` int(11) DEFAULT NULL,
  `hora_inicio` int(11) NOT NULL,
  `hora_fin` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id_empleado`);

--
-- Indices de la tabla `mesas`
--
ALTER TABLE `mesas`
  ADD PRIMARY KEY (`id_mesa`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `productos_mesa`
--
ALTER TABLE `productos_mesa`
  ADD PRIMARY KEY (`id_mesa_producto`),
  ADD KEY `id_mesa_idx` (`id_mesa`),
  ADD KEY `id_producto_idx` (`id_producto`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id_servicio`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_mesa` (`id_mesa`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `productos_mesa`
--
ALTER TABLE `productos_mesa`
  MODIFY `id_mesa_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `productos_mesa`
--
ALTER TABLE `productos_mesa`
  ADD CONSTRAINT `id_mesa` FOREIGN KEY (`id_mesa`) REFERENCES `mesas` (`id_mesa`),
  ADD CONSTRAINT `id_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`);

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `servicios_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  ADD CONSTRAINT `servicios_ibfk_2` FOREIGN KEY (`id_mesa`) REFERENCES `mesas` (`id_mesa`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
