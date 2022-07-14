-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: cse_calculator
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `specialties`
--

DROP TABLE IF EXISTS `specialties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialties` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `naming` varchar(100) DEFAULT NULL,
  `institution_id` varchar(10) DEFAULT NULL,
  `description` text,
  `picture_name` varchar(30) DEFAULT NULL,
  `institute` varchar(60) DEFAULT NULL,
  `degree` varchar(40) DEFAULT NULL,
  `average_score` double DEFAULT NULL,
  `members_bachelor` int DEFAULT NULL,
  `members_commerce` int DEFAULT NULL,
  `period_of_study` varchar(40) DEFAULT NULL,
  `necessary_subjects` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialties`
--

LOCK TABLES `specialties` WRITE;
/*!40000 ALTER TABLE `specialties` DISABLE KEYS */;
INSERT INTO `specialties` VALUES (1,'Лечебное дело','imedcol','Научитесь помогать людям профессионально','imedcol_ld.jpg','Медицинский колледж','Медицинский колледж',NULL,NULL,NULL,'3 года 10 месяцев',NULL),(2,'Акушерское дело','imedcol','Научитесь помогать людям профессионально','imedcol_ad.jpg','Медицинский колледж','Медицинский колледж',NULL,NULL,NULL,'2 года 10 месяцев',NULL),(3,'Сестринское дело','imedcol','Научитесь помогать людям профессионально','imedcol_sd.jpg','Медицинский колледж','Медицинский колледж',NULL,NULL,NULL,'2 года 10 месяцев',NULL),(4,'Лабораторная диагностика','imedcol','Научитесь помогать людям профессионально','imedcol_ldi.jpg','Медицинский колледж','Медицинский колледж',NULL,NULL,NULL,'2 года 10 месяцев',NULL);
/*!40000 ALTER TABLE `specialties` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-14  7:46:39
