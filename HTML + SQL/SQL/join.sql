use dstest;

select username,alamat,usia,nama_produk as nama, harga from cart
join product on cart.id_produk = product.id
join user on cart.id_user = user.id;

select * from product where id not in
(select id_produk from cart);

select * from user where id not in
(select id_user from cart);
