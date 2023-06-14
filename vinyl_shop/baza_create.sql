-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-06-14 06:37:44.841

-- tables
-- Table: Customers
CREATE TABLE Customers (
    CustomerID int NOT NULL CONSTRAINT Customers_pk PRIMARY KEY,
    Name varchar(30) NOT NULL,
    Surname varchar(50) NOT NULL,
    Address varchar(100) NOT NULL
);

-- Table: Deliveries
CREATE TABLE "Deliveries" (
	"DeliveryID"	INTEGER NOT NULL,
	"DateOfDelivery"	datetime NOT NULL,
	"VinylID"	int NOT NULL,
	"UnitsDelivered"	int NOT NULL,
	CONSTRAINT "Deliveries_Vinyls" FOREIGN KEY("VinylID") REFERENCES "Vinyls"("VinylID"),
	PRIMARY KEY("DeliveryID" AUTOINCREMENT)
);

-- Table: Sales
CREATE TABLE Sales (
    SaleID int NOT NULL CONSTRAINT Sales_pk PRIMARY KEY,
    CustomerID int NOT NULL,
    VinylID int NOT NULL,
    DateOfTransaction datetime NOT NULL,
    Quantity int NOT NULL,
    Price int NOT NULL,
    CONSTRAINT Sales_Vinyls FOREIGN KEY (VinylID)
    REFERENCES Vinyls (VinylID),
    CONSTRAINT Sales_Customers FOREIGN KEY (CustomerID)
    REFERENCES Customers (CustomerID)
);

-- Table: Vinyls
CREATE TABLE Vinyls (
    VinylID int NOT NULL CONSTRAINT Vinyls_pk PRIMARY KEY,
    Title varchar(130) NOT NULL,
    Artist varchar(100) NOT NULL,
    Genre varchar(30) NOT NULL,
    Description varchar(200) NOT NULL,
    URL varchar(200) NOT NULL,
    Price int NOT NULL
);

-- End of file.

