#!/usr/bin/php
<?php

$charset = 'abcdefghijkmpqrstuvwxyzABCDEFGHJKLMPQRSTUVWXYZ23456789';

for($t = 0; ; $t++) {

  srand($t);
  $rand_str = "";

  for($j = 0; $j < 12; $j++) {
    $rand_key = rand(0, 54 - 1);
    $rand_str .= $charset[$rand_key];
  }

  echo "$rand_str\n";
}

?>
