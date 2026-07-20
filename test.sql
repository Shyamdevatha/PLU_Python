-- views, index, storage procedure 


create procedure sp_get_all_users(table_name varchar(10),price varchar(10))
begin
    select * from table_name 
    where price = price;
end;

-- function call 
call sp_get_all_users('users', '100');