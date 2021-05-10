
CREATE DATABASE `homegreen` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `Users` (`email` varchar(100) NOT NULL, `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP, `notify` tinyint(1) DEFAULT '0', `news` tinyint(1) DEFAULT '0', PRIMARY KEY (`email`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci