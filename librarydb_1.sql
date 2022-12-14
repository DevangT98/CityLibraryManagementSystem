-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2022 at 05:25 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `librarydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

CREATE TABLE `authors` (
  `PID` int(11) NOT NULL,
  `DOCID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `DOCID` int(11) NOT NULL,
  `ISBN` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`DOCID`, `ISBN`) VALUES
(30, '0-9844-1105-4'),
(31, '0-4705-8745-8'),
(32, '0-4696-3320-4'),
(33, '0-6315-7219-8'),
(34, '0-9000-7501-5'),
(35, '0-4924-7316-1'),
(36, '0-7440-7830-7'),
(37, '0-9040-9230-5'),
(38, '0-9000-2479-8');

-- --------------------------------------------------------

--
-- Table structure for table `borrowing`
--

CREATE TABLE `borrowing` (
  `BOR_NO` int(11) NOT NULL,
  `BDTIME` datetime NOT NULL,
  `RDTIME` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrowing`
--

INSERT INTO `borrowing` (`BOR_NO`, `BDTIME`, `RDTIME`) VALUES
(92816, '2022-11-09 18:59:31', '2022-12-15 08:16:39'),
(113312, '2022-11-13 22:43:39', '2022-12-06 22:25:23'),
(176684, '2022-11-30 17:11:57', '2022-12-02 00:01:20'),
(256004, '2022-11-19 06:37:48', '2022-12-14 05:23:20'),
(269448, '2022-12-05 14:19:33', '2022-12-06 00:06:58'),
(271228, '2022-11-20 17:00:45', '2022-12-03 21:10:23'),
(495512, '2022-11-18 05:34:22', '2022-11-23 00:24:45'),
(522059, '2022-11-19 13:05:02', '2022-12-06 07:03:17'),
(529590, '2022-11-18 22:29:21', '2022-12-03 06:33:51'),
(537926, '2022-11-19 17:45:18', '2022-11-29 02:55:04'),
(614564, '2022-11-14 14:23:51', '2022-12-10 12:33:53'),
(619350, '2022-12-03 00:58:13', '2022-12-06 19:26:03'),
(652987, '2022-11-23 03:13:04', '2022-11-25 04:30:27'),
(690304, '2022-11-19 13:05:02', '2022-11-26 16:14:09'),
(693111, '2022-11-23 01:55:49', '2022-11-30 15:18:43'),
(708213, '2022-11-19 20:55:20', '2022-11-20 11:11:59'),
(791208, '2022-11-21 09:25:42', '2022-12-18 09:25:42'),
(805138, '2022-11-15 12:48:03', '2022-12-08 15:28:31'),
(834517, '2022-11-18 07:42:31', '2022-12-14 08:20:40'),
(845915, '2022-11-20 05:21:42', '2022-12-07 01:35:29'),
(996402, '2022-11-21 07:25:55', '2022-11-23 09:18:19');

-- --------------------------------------------------------

--
-- Table structure for table `borrowing_backup`
--

CREATE TABLE `borrowing_backup` (
  `BOR_NO` int(11) NOT NULL,
  `BDTIME` datetime NOT NULL,
  `RDTIME` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrowing_backup`
--

INSERT INTO `borrowing_backup` (`BOR_NO`, `BDTIME`, `RDTIME`) VALUES
(92816, '2022-11-09 18:59:31', '2022-12-15 08:16:39'),
(113312, '2022-11-13 22:43:39', '2022-12-06 22:25:23'),
(176684, '2022-11-30 17:11:57', '2022-12-02 00:01:20'),
(256004, '2022-11-19 06:37:48', '2022-12-14 05:23:20'),
(269448, '2022-12-05 14:19:33', '2022-12-06 00:06:58'),
(271228, '2022-11-20 17:00:45', '2022-12-03 21:10:23'),
(495512, '2022-11-18 05:34:22', '2022-11-23 00:24:45'),
(522059, '2022-11-19 13:05:02', '2022-12-06 07:03:17'),
(529590, '2022-11-18 22:29:21', '2022-12-03 06:33:51'),
(537926, '2022-11-19 17:45:18', '2022-11-29 02:55:04'),
(614564, '2022-11-14 14:23:51', '2022-12-10 12:33:53'),
(619350, '2022-12-03 00:58:13', '2022-12-06 19:26:03'),
(652987, '2022-11-23 03:13:04', '2022-11-25 04:30:27'),
(690304, '2022-11-19 13:05:02', '2022-11-26 16:14:09'),
(693111, '2022-11-23 01:55:49', '2022-11-30 15:18:43'),
(708213, '2022-11-19 20:55:20', '2022-11-20 11:11:59'),
(791208, '2022-11-21 09:25:42', '2022-12-18 09:25:42'),
(805138, '2022-11-15 12:48:03', '2022-12-08 15:28:31'),
(834517, '2022-11-18 07:42:31', '2022-12-14 08:20:40'),
(845915, '2022-11-20 05:21:42', '2022-12-07 01:35:29'),
(996402, '2022-11-21 07:25:55', '2022-11-23 09:18:19');

-- --------------------------------------------------------

--
-- Table structure for table `borrows`
--

CREATE TABLE `borrows` (
  `BOR_NO` int(11) NOT NULL,
  `DOCID` int(11) NOT NULL,
  `COPYNO` int(11) NOT NULL,
  `BID` int(11) NOT NULL,
  `RID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrows`
--

INSERT INTO `borrows` (`BOR_NO`, `DOCID`, `COPYNO`, `BID`, `RID`) VALUES
(92816, 30, 100, 5, 320),
(92816, 32, 75, 20, 320),
(92816, 35, 10, 18, 320),
(92816, 38, 28, 6, 320),
(113312, 31, 5, 2, 320),
(113312, 33, 50, 13, 320),
(113312, 36, 150, 12, 320),
(113312, 39, 7, 9, 320),
(176684, 31, 150, 11, 320),
(176684, 34, 25, 8, 320),
(176684, 37, 120, 17, 320),
(176684, 39, 7, 9, 320),
(256004, 34, 25, 8, 311),
(271228, 40, 9, 1, 325),
(495512, 41, 46, 7, 326);

--
-- Triggers `borrows`
--
DELIMITER $$
CREATE TRIGGER `chk_docs` BEFORE INSERT ON `borrows` FOR EACH ROW BEGIN
DELETE FROM borrows_backup 
WHERE RID=(SELECT RID
           FROM borrows
           WHERE RID=new.RID
           GROUP BY(RID)
           HAVING COUNT(DOCID)>10);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `borrows_backup`
--

CREATE TABLE `borrows_backup` (
  `BOR_NO` int(11) NOT NULL,
  `DOCID` int(11) NOT NULL,
  `COPYNO` int(11) NOT NULL,
  `BID` int(11) NOT NULL,
  `RID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrows_backup`
--

INSERT INTO `borrows_backup` (`BOR_NO`, `DOCID`, `COPYNO`, `BID`, `RID`) VALUES
(271228, 40, 9, 1, 325),
(495512, 41, 46, 7, 326);

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE `branch` (
  `BID` int(11) NOT NULL,
  `LNAME` varchar(50) NOT NULL,
  `LOCATION` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`BID`, `LNAME`, `LOCATION`) VALUES
(1, 'Sacred Knowledge', 'New York City'),
(2, 'Osprey library', 'Newark'),
(3, 'Maximus Knowledge', 'Boston'),
(4, 'Techno library', 'Houston'),
(5, 'Acumen library', 'New York City'),
(6, 'Empress Knowledge', 'Newark'),
(7, 'Amadeus library', 'New York City'),
(8, 'Bella library', 'Los Angeles'),
(9, 'Mainline Knowledge', 'Los Angeles'),
(10, 'Grand library', 'Newark'),
(11, 'Cognitive library', 'Boston'),
(12, 'Formosa Knowledge', 'Seattle'),
(13, 'Blossom library', 'Chicago'),
(14, 'City Library', 'Seattle'),
(15, 'Red river Library', 'Dallas'),
(16, 'Supreme Knowledge', 'Newark'),
(17, 'Rule Knowledge', 'Boston'),
(18, 'Clear Knowledge', 'Chicago'),
(19, 'Book velvet', 'New York City'),
(20, 'Book motion', 'Chicago'),
(21, 'Book buddy', 'Boston');

-- --------------------------------------------------------

--
-- Table structure for table `chairs`
--

CREATE TABLE `chairs` (
  `PID` int(11) NOT NULL,
  `DOCID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `copy`
--

CREATE TABLE `copy` (
  `DOCID` int(11) NOT NULL,
  `COPYNO` int(11) NOT NULL,
  `BID` int(11) NOT NULL,
  `CPY_POSITION` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `copy`
--

INSERT INTO `copy` (`DOCID`, `COPYNO`, `BID`, `CPY_POSITION`) VALUES
(30, 100, 5, '001A10'),
(31, 5, 2, '001A06'),
(31, 100, 3, '008A03'),
(31, 150, 11, '006A02'),
(32, 75, 20, '004A01'),
(33, 50, 13, '001A03'),
(34, 25, 8, '001A02'),
(35, 10, 18, '007A05'),
(36, 150, 12, '001B10'),
(37, 120, 17, '003A02'),
(38, 28, 6, '001C06'),
(39, 7, 9, '001B03'),
(39, 51, 14, NULL),
(39, 54, 3, NULL),
(40, 9, 1, '001C06'),
(40, 76, 12, NULL),
(41, 46, 7, '004C07'),
(42, 55, 14, NULL),
(43, 57, 10, NULL),
(44, 31, 4, '004C09'),
(44, 50, 8, NULL),
(44, 100, 6, NULL),
(45, 22, 10, '001C00'),
(45, 50, 14, NULL),
(46, 100, 20, '0'),
(47, 150, 19, '002C03'),
(48, 17, 14, '010B02'),
(48, 50, 2, NULL),
(48, 50, 18, NULL),
(48, 120, 16, '001A09'),
(49, 100, 15, '004A06'),
(50, 100, 12, NULL),
(50, 100, 20, '001B03');

--
-- Triggers `copy`
--
DELIMITER $$
CREATE TRIGGER `CHK_ALPHANUMERIC` BEFORE INSERT ON `copy` FOR EACH ROW BEGIN
IF(new.CPY_POSITION = CONCAT( '%[0-9]%' + '%[0-9]%' + '%[0-9]%' +'%[A-Z]%' + '%[0-9]%' + '%[0-9]%')) THEN
INSERT INTO copy VALUES('DOCID',new.DOCID,'COPYNO', new.COPYNO,'BID', new.BID, 'CPY_POSITION', new.CPY_POSITION);
ELSE
SET new.CPY_POSITION=Null;
END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `copy_backup`
--

CREATE TABLE `copy_backup` (
  `DOCID` int(11) NOT NULL,
  `COPYNO` int(11) NOT NULL,
  `BID` int(11) NOT NULL,
  `POSITION` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `copy_backup`
--

INSERT INTO `copy_backup` (`DOCID`, `COPYNO`, `BID`, `POSITION`) VALUES
(30, 100, 5, '001A10'),
(31, 5, 2, '001A06'),
(31, 100, 3, '008A03'),
(31, 150, 11, '006A02'),
(32, 75, 20, '004A01'),
(33, 50, 13, '001A03'),
(34, 25, 8, '001A02'),
(35, 10, 18, '007A05'),
(36, 150, 12, '001B10'),
(37, 120, 17, '003A02'),
(38, 28, 6, '001C06'),
(39, 7, 9, '001B03'),
(40, 9, 1, '001C06'),
(41, 46, 7, '004C07'),
(44, 31, 4, '004C09'),
(45, 22, 10, '001C00'),
(47, 150, 19, '002C03'),
(48, 17, 14, '010B02'),
(48, 120, 16, '001A09'),
(49, 100, 15, '004A06'),
(50, 100, 20, '001B03');

-- --------------------------------------------------------

--
-- Table structure for table `document`
--

CREATE TABLE `document` (
  `DOCID` int(11) NOT NULL,
  `TITLE` varchar(120) NOT NULL,
  `PDATE` datetime NOT NULL,
  `PUBLISHERID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `document`
--

INSERT INTO `document` (`DOCID`, `TITLE`, `PDATE`, `PUBLISHERID`) VALUES
(30, 'Hamlet', '2007-03-26 13:27:29', 203),
(31, 'War and Peace', '2009-09-10 12:18:33', 204),
(32, 'The Odyssey ', '2002-05-11 03:52:58', 201),
(33, 'The Divine Comedy', '2000-03-01 10:25:45', 210),
(34, 'Crime and Punishment', '2001-01-30 00:08:36', 212),
(35, 'Collected Fiction', '2004-02-15 08:46:24', 201),
(36, 'The Magic Mountain', '2011-08-04 16:12:45', 217),
(37, 'The Adventures of Huckleberry Finn', '2003-07-21 07:00:35', 213),
(38, 'Gullivers Travels', '2000-03-01 23:48:39', 201),
(39, 'Theory of cryptography', '2011-12-05 00:27:17', 211),
(40, 'Generic competencies required by engineers graduating in Australia	', '2004-10-22 10:29:06', 210),
(41, 'Sensitizing engineers: A brief study of the role of ethics in engineering education', '2002-06-13 09:47:37', 215),
(42, 'Drone tourism: a study of the current and potential use of drones in hospitality and tourism', '2015-01-24 03:29:34', 207),
(43, 'Pacemaker leads 1997', '2008-11-19 18:11:34', 206),
(44, 'Latest trends on engineering education', '2003-07-23 14:47:47', 205),
(45, 'Journal of Media Communication', '2009-11-15 01:29:37', 208),
(46, 'Journal of the American Medical Association', '2015-08-26 05:33:27', 209),
(47, 'Journal of Applied Developmental Psychology', '2007-07-08 02:23:17', 202),
(48, 'Journal of Literature', '2001-10-09 19:30:07', 214),
(49, 'Journal of Computer Science', '2001-05-27 06:47:19', 216),
(50, 'The Wall Street Journal', '2006-12-30 05:23:59', 218);

-- --------------------------------------------------------

--
-- Table structure for table `gedits`
--

CREATE TABLE `gedits` (
  `DOCID` int(11) NOT NULL,
  `ISSUE_NO` int(11) NOT NULL,
  `PID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `journal_issue`
--

CREATE TABLE `journal_issue` (
  `DOCID` int(11) NOT NULL,
  `ISSUE_NO` int(11) NOT NULL,
  `SCOPE` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `journal_volume`
--

CREATE TABLE `journal_volume` (
  `DOCID` int(11) NOT NULL,
  `VOLUME_NO` int(11) NOT NULL,
  `EDITOR` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `person`
--

CREATE TABLE `person` (
  `PID` int(11) NOT NULL,
  `PNAME` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`PID`, `PNAME`) VALUES
(100, 'Anne'),
(101, 'Oliver'),
(102, 'Noah'),
(103, 'Amelia'),
(104, 'Ava'),
(105, 'Charlotte'),
(106, 'Emma'),
(107, 'Sophia'),
(108, 'Liam'),
(109, 'Lucas'),
(110, 'James'),
(111, 'Amy'),
(112, 'Camila'),
(113, 'Daniel'),
(114, 'Penelope'),
(115, 'Mason'),
(116, 'Naomi'),
(117, 'Asher'),
(118, 'Savannah'),
(119, 'Dylan'),
(120, 'Jade');

-- --------------------------------------------------------

--
-- Table structure for table `proceedings`
--

CREATE TABLE `proceedings` (
  `DOCID` int(11) NOT NULL,
  `CDATE` datetime NOT NULL,
  `CLOCATION` varchar(50) NOT NULL,
  `CEDITOR` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `PUBLISHERID` int(11) NOT NULL,
  `PUBNAME` varchar(50) NOT NULL,
  `ADDRESS` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`PUBLISHERID`, `PUBNAME`, `ADDRESS`) VALUES
(200, 'Royal Books', '180 Berry Street'),
(201, 'Smart Publishing', '181 Apple Street'),
(202, 'Urban Fiction Publishers', '182 Banana Street'),
(203, 'Adventure Time Narratives', '183 Cherry Street'),
(204, 'Collomotiva Book Publishing', '184 Cranberry Street'),
(205, 'Taste Edge Publishing', '185 Avocado Street'),
(206, 'Arkham House', '186 Tomato Street'),
(207, 'Balboa Press', '187 Coconut Street'),
(208, 'Penguin Books', '189 Hazelnut Street'),
(209, 'Olympia Publishers', '190 Guava Street'),
(210, 'Dover Publication', '191 Pear Street'),
(211, 'Blue Bird Publishers', '192 Watermelon Street'),
(212, 'Pen2Paper Press', '193 Mango Street'),
(213, 'Ileria Publishing', '195 Orange Street'),
(214, 'Book Publishing Of New York', '196 Lime Street'),
(215, 'Edittoria Book Publishing', '197 Olive Street'),
(216, 'Ideas Shaper Publishing', '198 Strawberry Street'),
(217, 'Ink N Paper Press', '199 Kiwi Street'),
(218, 'Echo Publishing', '200 Melon Street'),
(219, 'Everykind Books Publishing', '201 Pomegranate Street'),
(220, 'Mattermind Publishers', '202 Blueberry Street');

-- --------------------------------------------------------

--
-- Table structure for table `reader`
--

CREATE TABLE `reader` (
  `RID` int(11) NOT NULL,
  `RTYPE` varchar(40) NOT NULL,
  `RNAME` varchar(50) NOT NULL,
  `RADDRESS` varchar(70) NOT NULL,
  `PHONE_NO` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reader`
--

INSERT INTO `reader` (`RID`, `RTYPE`, `RNAME`, `RADDRESS`, `PHONE_NO`) VALUES
(300, 'Student', 'Robert', 'Newark', 1234567890),
(301, 'Senior Citizen', 'Rayan', 'Jersey City', 2147483647),
(302, 'Staff', 'Ariana', 'New York City', 2147483647),
(303, 'Student', 'Justin', 'Boston', 447780545),
(304, 'Student', 'Ava', 'Dallas', 832760561),
(305, 'Staff', 'Misha', 'Seattle', 2147483647),
(306, 'Senior Citizen', 'Ben', 'Seattle', 2147483647),
(307, 'Staff', 'David', 'Newark', 2147483647),
(308, 'Senior Citizen', 'Sia', 'New York City', 2147483647),
(309, 'Student', 'Hannah', 'Dallas', 2147483647),
(310, 'Staff', 'Frank', 'Dallas', 2147483647),
(311, 'Senior Citizen', 'Robert', 'Seattle', 2147483647),
(312, 'Student', 'Ben', 'Boston', 2147483647),
(313, 'Staff', 'John', 'Chicago', 2147483647),
(314, 'Student', 'Mark', 'Los Angeles', 2147483647),
(315, 'Senior Citizen', 'Amy', 'Boston', 930949723),
(316, 'Student', 'Sarah', 'Los Angeles', 2147483647),
(317, 'Student', 'Mark', 'Chicago', 2147483647),
(318, 'Senior Citizen', 'Jim', 'Boston', 2147483647),
(319, 'Staff', 'Sienna', 'Chicago', 2147483647),
(320, 'Student', 'Chris', 'Boston', 2147483647),
(397, 'Staff', 'Test Reader', 'Mumbai', 2147483647),
(398, 'Senior Citizen', 'Test Reader2', 'Mumbai', 5513448086),
(399, 'Student', 'Test Reader3', 'Delhi', 5789765652);

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `RES_NO` int(11) NOT NULL,
  `DTIME` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservation`
--

INSERT INTO `reservation` (`RES_NO`, `DTIME`) VALUES
(60, '2022-11-16 22:04:51'),
(61, '2022-06-08 15:40:57'),
(62, '2022-10-07 09:22:14'),
(63, '2022-06-15 03:04:32'),
(64, '2022-06-22 01:10:46'),
(65, '2022-11-11 09:53:17'),
(66, '2022-01-14 16:18:00'),
(67, '2022-02-17 01:26:59'),
(68, '2022-06-05 17:55:48'),
(69, '2021-12-11 16:36:11'),
(70, '2022-02-17 01:26:59'),
(71, '2022-06-05 17:55:48'),
(72, '2021-12-11 16:36:11'),
(73, '2022-09-22 06:19:21'),
(74, '2022-08-20 04:16:29'),
(75, '2022-02-17 01:26:59'),
(76, '2022-01-26 00:05:58'),
(77, '2022-10-29 15:17:42'),
(78, '2022-05-19 18:24:08'),
(79, '2022-07-29 01:00:27'),
(80, '2022-11-17 22:08:50'),
(82, '2022-12-11 00:25:32'),
(84, '2022-12-11 17:59:59'),
(88, '2022-12-11 20:27:24'),
(90, '2022-12-11 20:31:50'),
(91, '2022-12-11 21:39:52'),
(92, '2022-12-11 11:40:19'),
(94, '2022-12-11 20:44:56'),
(97, '2022-12-11 20:47:58'),
(98, '2022-12-11 21:42:30'),
(99, '2022-12-11 20:47:58'),
(101, '2022-12-11 20:56:01'),
(102, '2022-12-11 12:56:30'),
(104, '2022-12-11 21:00:34'),
(112, '2022-12-11 20:10:08'),
(115, '2022-12-11 20:13:22'),
(116, '2022-12-11 19:28:12'),
(117, '2022-12-11 20:30:43'),
(119, '2022-12-11 14:32:11'),
(120, '2022-12-11 21:33:33'),
(124, '2022-12-11 20:44:02');

--
-- Triggers `reservation`
--
DELIMITER $$
CREATE TRIGGER `CHK_RESERVATION_TIME` AFTER INSERT ON `reservation` FOR EACH ROW BEGIN
UPDATE reservation_backup
SET reservation_backup.RES_NO=Null
WHERE TIME(reservation_backup.DTIME)>'18:00:00';
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `reservation_backup`
--

CREATE TABLE `reservation_backup` (
  `RES_NO` int(11) NOT NULL,
  `DTIME` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservation_backup`
--

INSERT INTO `reservation_backup` (`RES_NO`, `DTIME`) VALUES
(61, '2022-06-08 15:40:57'),
(62, '2022-10-07 09:22:14'),
(63, '2022-06-15 03:04:32'),
(64, '2022-06-22 01:10:46'),
(65, '2022-11-11 09:53:17'),
(66, '2022-01-14 16:18:00'),
(67, '2022-02-17 01:26:59'),
(68, '2022-06-05 17:55:48'),
(69, '2021-12-11 16:36:11'),
(70, '2022-02-17 01:26:59'),
(71, '2022-06-05 17:55:48'),
(72, '2021-12-11 16:36:11'),
(73, '2022-09-22 06:19:21'),
(74, '2022-08-20 04:16:29'),
(75, '2022-02-17 01:26:59'),
(76, '2022-01-26 00:05:58'),
(77, '2022-10-29 15:17:42'),
(79, '2022-07-29 01:00:27');

-- --------------------------------------------------------

--
-- Table structure for table `reserves`
--

CREATE TABLE `reserves` (
  `RID` int(11) NOT NULL,
  `RESERVATION_NO` int(11) NOT NULL,
  `DOCID` int(11) NOT NULL,
  `COPYNO` int(11) NOT NULL,
  `BID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reserves`
--

INSERT INTO `reserves` (`RID`, `RESERVATION_NO`, `DOCID`, `COPYNO`, `BID`) VALUES
(310, 62, 34, 50, 11),
(309, 62, 44, 31, 4),
(305, 65, 34, 25, 8),
(117, 66, 34, 25, 8),
(311, 66, 41, 46, 7),
(305, 66, 45, 22, 10),
(315, 68, 37, 120, 17),
(307, 70, 38, 28, 6),
(315, 71, 45, 22, 10),
(318, 72, 35, 10, 18),
(318, 115, 41, 46, 7),
(316, 119, 34, 25, 8),
(314, 120, 45, 22, 10);

--
-- Triggers `reserves`
--
DELIMITER $$
CREATE TRIGGER `CHK_RES_DOCS` BEFORE INSERT ON `reserves` FOR EACH ROW BEGIN
DELETE FROM reserves_backup 
WHERE RID=(SELECT RID
           FROM reserves
           WHERE RID=new.RID
           GROUP BY(RID)
           HAVING COUNT(DOCID)>10);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `reserves_backup`
--

CREATE TABLE `reserves_backup` (
  `RID` int(11) NOT NULL,
  `RESERVATION_NO` int(11) NOT NULL,
  `DOCID` int(11) NOT NULL,
  `COPYNO` int(11) NOT NULL,
  `BID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`PID`,`DOCID`),
  ADD KEY `FK_ATHR_DOCID` (`DOCID`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`DOCID`);

--
-- Indexes for table `borrowing`
--
ALTER TABLE `borrowing`
  ADD PRIMARY KEY (`BOR_NO`);

--
-- Indexes for table `borrowing_backup`
--
ALTER TABLE `borrowing_backup`
  ADD PRIMARY KEY (`BOR_NO`);

--
-- Indexes for table `borrows`
--
ALTER TABLE `borrows`
  ADD PRIMARY KEY (`BOR_NO`,`DOCID`,`COPYNO`,`BID`),
  ADD KEY `DOCID_BOR_FK` (`DOCID`),
  ADD KEY `COPYNO_BOR_FK` (`COPYNO`),
  ADD KEY `BID_BOR_FK` (`BID`);

--
-- Indexes for table `borrows_backup`
--
ALTER TABLE `borrows_backup`
  ADD PRIMARY KEY (`BOR_NO`,`DOCID`,`COPYNO`,`BID`),
  ADD KEY `DOCID_BOR_FK` (`DOCID`),
  ADD KEY `COPYNO_BOR_FK` (`COPYNO`),
  ADD KEY `BID_BOR_FK` (`BID`);

--
-- Indexes for table `branch`
--
ALTER TABLE `branch`
  ADD PRIMARY KEY (`BID`);

--
-- Indexes for table `chairs`
--
ALTER TABLE `chairs`
  ADD PRIMARY KEY (`PID`,`DOCID`),
  ADD KEY `FK_CHAIRS_DOCID` (`DOCID`);

--
-- Indexes for table `copy`
--
ALTER TABLE `copy`
  ADD PRIMARY KEY (`DOCID`,`COPYNO`,`BID`),
  ADD KEY `FK_BID` (`BID`),
  ADD KEY `COPYNO` (`COPYNO`);

--
-- Indexes for table `copy_backup`
--
ALTER TABLE `copy_backup`
  ADD PRIMARY KEY (`DOCID`,`COPYNO`,`BID`),
  ADD KEY `FK_BID` (`BID`),
  ADD KEY `COPYNO` (`COPYNO`);

--
-- Indexes for table `document`
--
ALTER TABLE `document`
  ADD PRIMARY KEY (`DOCID`),
  ADD KEY `FK_PUBLISHERID` (`PUBLISHERID`);

--
-- Indexes for table `gedits`
--
ALTER TABLE `gedits`
  ADD PRIMARY KEY (`DOCID`,`ISSUE_NO`,`PID`),
  ADD KEY `FK_GEDT_ISSUE_NO` (`ISSUE_NO`),
  ADD KEY `FK_GEDT_PID` (`PID`);

--
-- Indexes for table `journal_issue`
--
ALTER TABLE `journal_issue`
  ADD PRIMARY KEY (`DOCID`,`ISSUE_NO`),
  ADD KEY `ISSUE_NO` (`ISSUE_NO`);

--
-- Indexes for table `journal_volume`
--
ALTER TABLE `journal_volume`
  ADD PRIMARY KEY (`DOCID`),
  ADD KEY `EDITOR` (`EDITOR`);

--
-- Indexes for table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`PID`),
  ADD KEY `PID` (`PID`);

--
-- Indexes for table `proceedings`
--
ALTER TABLE `proceedings`
  ADD PRIMARY KEY (`DOCID`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`PUBLISHERID`);

--
-- Indexes for table `reader`
--
ALTER TABLE `reader`
  ADD PRIMARY KEY (`RID`);

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`RES_NO`);

--
-- Indexes for table `reservation_backup`
--
ALTER TABLE `reservation_backup`
  ADD PRIMARY KEY (`RES_NO`);

--
-- Indexes for table `reserves`
--
ALTER TABLE `reserves`
  ADD PRIMARY KEY (`RESERVATION_NO`,`DOCID`,`COPYNO`,`BID`),
  ADD KEY `RESERVATION_NO` (`RESERVATION_NO`,`DOCID`,`COPYNO`,`BID`),
  ADD KEY `DOCID_FOREIGN_KEY` (`DOCID`),
  ADD KEY `FK_COPYNO` (`COPYNO`),
  ADD KEY `BID_FOREIGN_KEY` (`BID`);

--
-- Indexes for table `reserves_backup`
--
ALTER TABLE `reserves_backup`
  ADD PRIMARY KEY (`RESERVATION_NO`,`DOCID`,`COPYNO`,`BID`),
  ADD KEY `RESERVATION_NO` (`RESERVATION_NO`,`DOCID`,`COPYNO`,`BID`),
  ADD KEY `DOCID_FOREIGN_KEY` (`DOCID`),
  ADD KEY `FK_COPYNO` (`COPYNO`),
  ADD KEY `BID_FOREIGN_KEY` (`BID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authors`
--
ALTER TABLE `authors`
  ADD CONSTRAINT `FK_ATHR_DOCID` FOREIGN KEY (`DOCID`) REFERENCES `book` (`DOCID`),
  ADD CONSTRAINT `FK_ATHR_PID` FOREIGN KEY (`PID`) REFERENCES `person` (`PID`);

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `FK_book_docid` FOREIGN KEY (`DOCID`) REFERENCES `document` (`DOCID`);

--
-- Constraints for table `borrows`
--
ALTER TABLE `borrows`
  ADD CONSTRAINT `BID_BOR_FK` FOREIGN KEY (`BID`) REFERENCES `copy` (`BID`),
  ADD CONSTRAINT `BOR_NO_FK` FOREIGN KEY (`BOR_NO`) REFERENCES `borrowing` (`BOR_NO`),
  ADD CONSTRAINT `COPYNO_BOR_FK` FOREIGN KEY (`COPYNO`) REFERENCES `copy` (`COPYNO`),
  ADD CONSTRAINT `DOCID_BOR_FK` FOREIGN KEY (`DOCID`) REFERENCES `copy` (`DOCID`);

--
-- Constraints for table `chairs`
--
ALTER TABLE `chairs`
  ADD CONSTRAINT `FK_CHAIRS_DOCID` FOREIGN KEY (`DOCID`) REFERENCES `proceedings` (`DOCID`),
  ADD CONSTRAINT `FK_CHAIRS_PID` FOREIGN KEY (`PID`) REFERENCES `person` (`PID`);

--
-- Constraints for table `copy`
--
ALTER TABLE `copy`
  ADD CONSTRAINT `FK_BID` FOREIGN KEY (`BID`) REFERENCES `branch` (`BID`),
  ADD CONSTRAINT `FK_DOCID` FOREIGN KEY (`DOCID`) REFERENCES `document` (`DOCID`);

--
-- Constraints for table `document`
--
ALTER TABLE `document`
  ADD CONSTRAINT `FK_PUBLISHERID` FOREIGN KEY (`PUBLISHERID`) REFERENCES `publisher` (`PUBLISHERID`);

--
-- Constraints for table `gedits`
--
ALTER TABLE `gedits`
  ADD CONSTRAINT `FK_GEDT_DOCID` FOREIGN KEY (`DOCID`) REFERENCES `journal_issue` (`DOCID`),
  ADD CONSTRAINT `FK_GEDT_ISSUE_NO` FOREIGN KEY (`ISSUE_NO`) REFERENCES `journal_issue` (`ISSUE_NO`),
  ADD CONSTRAINT `FK_GEDT_PID` FOREIGN KEY (`PID`) REFERENCES `person` (`PID`);

--
-- Constraints for table `journal_issue`
--
ALTER TABLE `journal_issue`
  ADD CONSTRAINT `FK_JRNL_ISSUE_DOCID` FOREIGN KEY (`DOCID`) REFERENCES `journal_volume` (`DOCID`);

--
-- Constraints for table `journal_volume`
--
ALTER TABLE `journal_volume`
  ADD CONSTRAINT `FK_JRNL_VLM_DOCID` FOREIGN KEY (`DOCID`) REFERENCES `document` (`DOCID`),
  ADD CONSTRAINT `FK_JRNL_VLM_EDITOR` FOREIGN KEY (`EDITOR`) REFERENCES `person` (`PID`);

--
-- Constraints for table `proceedings`
--
ALTER TABLE `proceedings`
  ADD CONSTRAINT `FK_PRCDNG_DOCID` FOREIGN KEY (`DOCID`) REFERENCES `document` (`DOCID`);

--
-- Constraints for table `reserves`
--
ALTER TABLE `reserves`
  ADD CONSTRAINT `BID_FOREIGN_KEY` FOREIGN KEY (`BID`) REFERENCES `copy` (`BID`),
  ADD CONSTRAINT `DOCID_FOREIGN_KEY` FOREIGN KEY (`DOCID`) REFERENCES `copy` (`DOCID`),
  ADD CONSTRAINT `FK_COPYNO` FOREIGN KEY (`COPYNO`) REFERENCES `copy` (`COPYNO`),
  ADD CONSTRAINT `RES_NO_FK` FOREIGN KEY (`RESERVATION_NO`) REFERENCES `reservation` (`RES_NO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
