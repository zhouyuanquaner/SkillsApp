# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.10)
# Database: SkillsApp
# Generation Time: 2016-09-10 19:44:53 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table Categories
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Categories`;

CREATE TABLE `Categories` (
  `CategoryName` varchar(45) NOT NULL DEFAULT '',
  `CateDescription` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`CategoryName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Categories` WRITE;
/*!40000 ALTER TABLE `Categories` DISABLE KEYS */;

INSERT INTO `Categories` (`CategoryName`, `CateDescription`)
VALUES
	('CAREER&POST-GRAD','Explore career pathways and gain valuable skills for life beyond college.'),
	('CIVIC RESPONSIBILITY','Grow into a thoughtful citizen of your local and global communities.'),
	('COMMUNICATION&CONNECTION','Learn how to effectively convey messages, express yourself, and connect with others.'),
	('EMPATHY','Deepen a sense of connection, curiosity, and understanding of others.'),
	('INNOVATION&ENTREPRENEURSHIP','Approach the world with a solutions-oriented lens and hone your sense of creativity.'),
	('LEADERSHIP&FOLLOWERSHIP','Master the components of ethical, inclusive leadership.'),
	('SUCCESS SKILLS','Master skills to succeed academically, financially, and in life.'),
	('WELLNESS','Understand and practice how to take excellent care of yourself, inside and out. ');

/*!40000 ALTER TABLE `Categories` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
