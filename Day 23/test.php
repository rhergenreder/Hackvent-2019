<?php

// for($i = 0; $i < 1000; $i++)
//   print(microtime(true) . "\n");

srand(1);
$alphabet = 'abcdefghijkmpqrstuvwxyzABCDEFGHJKLMPQRSTUVWXYZ23456789';
$out = "";

for($j = 0; $j < 12; $j++) {
  $rand_key = rand(0, 54 - 1);
  // var_dump($rand_key);
  $out .= $alphabet[$rand_key];
}

var_dump($out);

?>
