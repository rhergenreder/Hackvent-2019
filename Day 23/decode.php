#!/usr/bin/php
<?php

if(count($argv) < 4) {
  die("Wrong Usage: " . $argv[0] . " <proc num> <start> <end>");
}

$PROC_NUM = $argv[1];

if(!is_numeric($argv[2])) {
  die("NaN: start");
}

if(!is_numeric($argv[3])) {
  die("NaN: end");
}

$start = intval($argv[2]);
$end   = intval($argv[3]);

if($end < $start) {
  die("Invalid interval: end < start");
}

$charset = 'abcdefghijkmpqrstuvwxyzABCDEFGHJKLMPQRSTUVWXYZ23456789';
$zip = new ZipArchive();
$zip_status = $zip->open("Santa-data.zip");
if ($zip_status !== true) {
  die("Could not open zip file");
}

for($t = $start; $t <= $end; $t++) {

  srand($t);
  $rand_str = "";

  // if(($t-$start) % 10000000 == 0) {
  //   $progress = (($t-$start) / ($end - $start)) * 100;
  //   print("[$PROC_NUM] Progress: $progress%\n");
  // }

  for($j = 0; $j < 12; $j++) {
    $rand_key = rand(0, 54 - 1);
    $rand_str .= $charset[$rand_key];
  }

  // stdout for john
  // if(strcmp($rand_str, "Kwmq3Sqmc5sA") == 0) {
  //   die("Done: $t\n");
  // }

  // 4160000
  // print("$rand_str\n");
  //
  if ($zip->setPassword($rand_str)) {
    if ($zip->extractTo(__DIR__)) {
      die("PASSWORD: $rand_str");
    }
  }
}

?>
