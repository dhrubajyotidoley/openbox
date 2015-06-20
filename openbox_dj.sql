CREATE TABLE IF NOT EXISTS `clients_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `desc` longtext NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `person` varchar(100) NOT NULL,
  `hashtag` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;


INSERT INTO `clients_client` (`id`, `name`, `desc`, `phone`, `email`, `address`, `person`, `hashtag`) VALUES
(1, 'Open Nirvana', 'This is Test to track and get the Hastag of CNN on the Screen', '8692999219', 'dhruba.doley@gmail.com', 'G--118, Ground Floor, Haware Fantasia Business Park,\r\nSector 30A, Near Inorbit Mall, Vashi', 'Dhruba', 'cnn');



CREATE TABLE IF NOT EXISTS `clients_facebook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `content` varchar(250) NOT NULL,
  `content_main` longtext NOT NULL,
  `profile_pic` varchar(300) NOT NULL,
  `content_pic` varchar(300) NOT NULL,
  `time` varchar(100) NOT NULL,
  `hashtag` varchar(100) NOT NULL,
  `client_id` int(11) NOT NULL,
  `read` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_pic` (`content_pic`),
  KEY `client_id` (`client_id`)
);


CREATE TABLE IF NOT EXISTS `clients_instagram` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `profile_pic` varchar(300) NOT NULL,
  `content_pic` varchar(250) NOT NULL,
  `time` varchar(100) NOT NULL,
  `hashtag` varchar(100) NOT NULL,
  `show` varchar(10) NOT NULL,
  `client_id` int(11) NOT NULL,
  `read` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_pic` (`content_pic`),
  KEY `client_id` (`client_id`)
);


CREATE TABLE IF NOT EXISTS `clients_twitter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `content` varchar(250) NOT NULL,
  `content_main` longtext NOT NULL,
  `profile_pic` varchar(300) NOT NULL,
  `content_pic` varchar(300) NOT NULL,
  `time` varchar(100) NOT NULL,
  `hashtag` varchar(100) NOT NULL,
  `client_id` int(11) NOT NULL,
  `read` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_pic` (`content_pic`),
  KEY `client_id` (`client_id`)
);

