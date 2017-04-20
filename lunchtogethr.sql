CREATE DATABASE  IF NOT EXISTS `lunchtogethr` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `lunchtogethr`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: lunchtogethr
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `arrangements`
--

DROP TABLE IF EXISTS `arrangements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arrangements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) NOT NULL,
  `linkedin_user_id` int(11) NOT NULL,
  `created_at` date DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `buddy` int(11) DEFAULT NULL,
  `location_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_arrangements_topics_idx` (`topic_id`),
  KEY `fk_arrangements_linkedin_users1_idx` (`linkedin_user_id`),
  KEY `fk_arrangements_locations1_idx` (`location_id`),
  CONSTRAINT `fk_arrangements_linkedin_users1` FOREIGN KEY (`linkedin_user_id`) REFERENCES `linkedin_users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_arrangements_locations1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_arrangements_topics` FOREIGN KEY (`topic_id`) REFERENCES `topics` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrangements`
--

LOCK TABLES `arrangements` WRITE;
/*!40000 ALTER TABLE `arrangements` DISABLE KEYS */;
INSERT INTO `arrangements` VALUES (129,9,23,'2016-04-01','2016-04-01 11:28:26',17,2),(130,16,24,'2016-04-01','2016-04-01 11:29:57',17,7),(131,11,25,'2016-04-01','2016-04-01 11:35:31',17,5),(132,14,22,'2016-04-01','2016-04-01 11:36:51',17,1),(136,12,27,'2016-04-01','2016-04-01 18:00:01',18,1),(137,12,18,'2016-04-01','2016-04-01 18:04:02',27,1),(143,9,18,'2016-05-28','2016-05-28 00:32:22',17,1),(144,9,17,'2016-05-28','2016-05-28 00:33:11',18,1);
/*!40000 ALTER TABLE `arrangements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `linkedin_users`
--

DROP TABLE IF EXISTS `linkedin_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linkedin_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `access_token` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `headline` varchar(500) DEFAULT NULL,
  `industry` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `image_link` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linkedin_users`
--

LOCK TABLES `linkedin_users` WRITE;
/*!40000 ALTER TABLE `linkedin_users` DISABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'San Jose','2016-03-31 18:12:24','2016-03-31 18:12:24'),(2,'Palo Alto','2016-03-31 18:13:10','2016-03-31 18:13:10'),(3,'Seattle','2016-03-31 18:13:19','2016-03-31 18:13:19'),(4,'Menlo Park','2016-03-31 18:13:28','2016-03-31 18:13:28'),(5,'Mountain View','2016-03-31 18:13:35','2016-03-31 18:13:35'),(6,'Home','2016-03-31 18:30:12','2016-03-31 18:30:12'),(7,'Los Angeles','2016-04-01 11:29:57','2016-04-01 11:29:57'),(8,'mountain view','2016-04-01 11:35:31','2016-04-01 11:35:31'),(12,'Coding Dojo','2016-04-01 13:43:12','2016-04-01 13:43:12'),(15,'dawd','2016-05-28 01:53:03','2016-05-28 01:53:03');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topics`
--

DROP TABLE IF EXISTS `topics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topics`
--

LOCK TABLES `topics` WRITE;
/*!40000 ALTER TABLE `topics` DISABLE KEYS */;
INSERT INTO `topics` VALUES (9,'IoT','2016-03-31 18:16:34','2016-03-31 18:16:34'),(10,'Wearables','2016-03-31 18:16:39','2016-03-31 18:16:39'),(11,'Finance','2016-03-31 18:16:43','2016-03-31 18:16:43'),(12,'Marketing','2016-03-31 18:16:47','2016-03-31 18:16:47'),(13,'','2016-03-31 18:16:53','2016-03-31 18:16:53'),(14,'Machine Learning','2016-03-31 18:16:59','2016-03-31 18:16:59'),(15,'Entrepreneurship','2016-03-31 18:18:13','2016-03-31 18:18:13'),(16,'Event Management','2016-04-01 11:29:57','2016-04-01 11:29:57'),(17,'Coding Dojo','2016-04-01 11:38:02','2016-04-01 11:38:02'),(22,'awdawd','2016-05-28 01:53:03','2016-05-28 01:53:03');
/*!40000 ALTER TABLE `topics` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-31 12:23:10
