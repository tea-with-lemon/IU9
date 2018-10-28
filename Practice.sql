CREATE DATABASE PracticeBase;
USE PracticeBase;

-- ***************************************************;

DROP TABLE `Practice`;

DROP TABLE `Manager`;

DROP TABLE `Group`;

DROP TABLE `Company`;

DROP TABLE `Student`;

-- ************************************** `Student`

create table Student
(
 `StudentID`  int not null auto_increment,
 `FirstName`  nvarchar(50) not null,
 `LastName`   nvarchar(50) not null,
 `FName`	    nvarchar(50),
 `BirthDate`  date not null,
 `Phone`      varchar(20),
 `Email`      varchar(40),
 `Course`     tinyint,
 `Group`      tinyint,
 `Entrance`   year not null,

primary key (`StudentID`),
unique key `AK_Phone` (`Phone`),
unique key `AK_Mail` (`Email`),
unique key `AK_Student` (`LastName`, `FirstName`, `BirthDate`)
)
;

-- **************************************  `Company`
create table Company
(
  `CompanyName` varchar(225)  not null
    primary key,
  `Description` varchar(1000),
  `Addres`      varchar(1000),
  `Email`       varchar(30)
);

-- ************************************** `Manager`

create table `Manager`
(
 `ManagerID`      int not null auto_increment primary key,
 `Phone`          varchar(20) not null,
 `Email`          varchar(40) not null,
 `CompanyName`    varchar(255) not null,
 `FirstName`      nvarchar(50) not null,
 `LastName`       nvarchar(50) not null,
 `FName`	        nvarchar(50),
 `Head`           bool,

 unique key `AK_ManagerPhone` (`Phone`),
 unique key  `AK_ManagerMail` (`Email`),
 foreign key (`CompanyName`) references Company (`CompanyName`)
  on update cascade
  on delete restrict
);

-- ************************************** `Group`

CREATE TABLE `Group`
(
  `Student`          int not null,
  `PracticeYear`     date not null,
  `CompanyName`      varchar(225)  not null,

 primary key (`Student`, `PracticeYear`),
 foreign key (`Student`) references Student (`StudentID`)
   on update cascade on delete restrict,
 foreign key (`CompanyName`) references Company (`CompanyName`)
   on update cascade on delete restrict
);

-- ************************************** `Practice`

create table Practice
(
 `TreatmentNumber` 			   varchar(30) not null
   primary key,
 `TreatmentNumberCompany`	 varchar(30),
 `StartDate`               date,
 `EndDate`                 date,
 `Mark`						         tinyint,
 `Task`						         text,
 `Report`					         bool,
 `Student`				         int not null,
 `Head`					           int not null,
 `ManagerCompany`          int not null,
 `ManagerBMSTU`            int not null,

foreign key (`Student`) references Student (`StudentID`)
  on update cascade on delete restrict,
foreign key (`Head`) references Student (`StudentID`)
  on update cascade on delete restrict,
foreign key (`ManagerCompany`) references Manager (`ManagerID`)
  on update cascade on delete restrict,
foreign key (`ManagerBMSTU`) references Manager (`ManagerID`)
  on update cascade on delete restrict,
unique key  `AK_Practice` (`TreatmentNumberCompany`)
);

-- **************************************

insert into Student (`FirstName`, `LastName`, `BirthDate`, `Entrance`) values ('Давид', 'Зухбая', date(now()), '2015');
insert into Student (`FirstName`, `LastName`, `BirthDate`, `Entrance`) values ('Иванов', 'Павел', date("1998-09-15"), '2019');
insert into Practice (`TreatmentNumber`, `Student`, `Head`) values ('02.08-05/18', 4, 1);
SELECT * FROM Student;



select BirthDate from Student;
