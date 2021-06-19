INSERT INTO users ( first_name, last_name, email, created_at, uploaded_at )
VALUES ( "cool", "guy", "c@c", NOW(), NOW() );
SELECT * FROM flask_schema.users;
