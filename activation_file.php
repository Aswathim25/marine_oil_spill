<html>
<head>
<script type="text/javascript">
  window.onclick = function(){
   window.location.href = 'final.php';
  };
</script>
</head>
<body>
    <img src="monkey-1.gif" style="width:  100%;height: 600px;">    
    
    
<?php
$lat=$_GET['lat'];
$lng=$_GET['lng'];
$ot=$_GET['otype'];
$seed=$_GET['seed'];

file_put_contents("file.txt", $lat."\n".$lng."\n".$ot."\n".$seed."\n");
execInBackground('start cmd.exe @cmd /k "C:\ProgramData\Anaconda3e\Scripts\activate.bat C:\ProgramData\Anaconda3e && python E:\xampp\htdocs\FYP\run.py"');
function execInBackground($cmd) { 
    if (substr(php_uname(), 0, 7) == "Windows"){ 
        pclose(popen("start /B ". $cmd, "r"));  
    } 
    else { 
        exec($cmd . " > /dev/null &");   
    } 
}
?>
</body>
</html>
