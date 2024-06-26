IF NOT EXISTS(SELECT * FROM sys.databases WHERE [name]='CarRentalSystem')
	BEGIN
		CREATE DATABASE [CarRentalSystem]
	END
	GO
USE	[CarRentalSystem]
GO

IF OBJECT_ID(N'vehicle') IS NULL
CREATE TABLE [vehicle] (
  [vehicleID] int NOT NULL IDENTITY(1,1),
  [make] varchar(255),
  [model] varchar(255),
  [year] varchar(4),
  [dailyrate] float,
  [status] varchar(255) NOT NULL CHECK ([status] IN ('Available','Unavailable')),
  [passengercapacity] int,
  [enginecapacity] int,
  CONSTRAINT vehicle_pk PRIMARY KEY ([vehicleID])
);




IF OBJECT_ID(N'customer') IS NULL
CREATE TABLE [customer] (
  [customerID] int NOT NULL IDENTITY(1,1),
  [firstname] varchar(255),
  [lastname] varchar(255),
  [email] varchar(255),
  [phoneNumber] varchar(255),
  CONSTRAINT customer_uk UNIQUE([email],[phoneNumber]),
  CONSTRAINT customer_pk PRIMARY KEY ([customerID])
);


IF OBJECT_ID(N'lease') IS NULL
CREATE TABLE [lease] (
  [leaseID] int NOT NULL IDENTITY(1,1),
  [vehicleID] int,
  [customerID] int,
  [startDate] date,
  [endDate] date,
  [type] varchar(255) NOT NULL CHECK ([type] IN ('Daily','Monthly')),
  CONSTRAINT lease_pk PRIMARY KEY ([leaseID]),
  CONSTRAINT lease_vehicle_fk FOREIGN KEY([vehicleID]) REFERENCES vehicle([vehicleID]) ON DELETE CASCADE,
  CONSTRAINT lease_customer_fk FOREIGN KEY([customerID]) REFERENCES customer([customerID]) ON DELETE CASCADE
);

IF OBJECT_ID(N'payment') IS NULL
CREATE TABLE [payment] (
  [paymentID] int NOT NULL IDENTITY(1,1),
  [leaseID] int,
  [paymentDate] date,
  [amount] float,
  CONSTRAINT payment_pk PRIMARY KEY ([paymentID]),
  CONSTRAINT payment_lease_fk FOREIGN KEY([leaseID]) REFERENCES lease([leaseID]) ON DELETE SET NULL

);
