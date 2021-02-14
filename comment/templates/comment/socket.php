<?php

	//$key_ = $_POST['customer_did'];
	$key_ = 1;
	$mySocket = socket_create(AF_INET, SOCK_STREAM, 0) or die("could not create socket");
	$Socket = socket_connect($mySocket, '', '9000' ) or die("could not connect socket");
	socket_write($mySocket, $key) or die("could not write");
	$data_list = socket_read($mySocket, 1024 ) or die("could not read the input");
	echo ($data_list);
?>