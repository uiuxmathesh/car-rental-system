
INSERT INTO vehicle (make, model, year, dailyrate, status, passengercapacity, enginecapacity)
VALUES
('Honda', 'Civic', '2022', 50.00, 'available', 5, 2000),
('Toyota', 'Corolla', '2020', 60.00, 'available', 5, 1800),
('Ford', 'Fusion', '2019', 55.00, 'available', 5, 2200),
('Chevrolet', 'Malibu', '2018', 55.00, 'available', 5, 2000),
('Nissan', 'Altima', '2017', 55.00, 'available', 5, 2500),
('Hyundai', 'Elantra', '2016', 45.00, 'available', 5, 1600),
('Volkswagen', 'Jetta', '2015', 50.00, 'available', 5, 1800),
('Kia', 'Optima', '2014', 50.00, 'available', 5, 2000);

-- Seed data for the customer table
INSERT INTO customer (firstname, lastname, email, phoneNumber)
VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '986543210'),
('Michael', 'Johnson', 'michael.johnson@example.com', '4567890123'),
('Emily', 'Brown', 'emily.brown@example.com', '7890123456'),
('David', 'Lee', 'david.lee@example.com', '2345678901');

-- Seed data for the lease table
INSERT INTO lease (vehicleID, customerID, startDate, endDate, type)
VALUES
(1, 1, '2024-05-01', '2024-05-02', 'Daily'),
(2, 2, '2024-05-01', '2024-05-31', 'Monthly'),
(3, 3, '2024-05-03', '2024-05-04', 'Daily'),
(4, 4, '2024-05-05', '2024-05-06', 'Daily'),
(5, 5, '2024-05-06', '2024-05-08', 'Daily');

-- Seed data for the payment table
INSERT INTO payment (leaseID, paymentDate, amount)
VALUES
(1, '2024-05-02', 50.00),
(2, '2024-05-31', 1800.00),
(3, '2024-05-04', 55.00),
(4, '2024-05-06', 55.00),
(5, '2024-05-08', 110.00);