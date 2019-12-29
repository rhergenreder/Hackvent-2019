<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"></head><body><code><span style="color: #000000">
<span style="color: #0000BB">&lt;?php<br><br></span><span style="color: #007700">if&nbsp;(isset(</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">'show'</span><span style="color: #007700">]))&nbsp;</span><span style="color: #0000BB">highlight_file</span><span style="color: #007700">(</span><span style="color: #0000BB">__FILE__</span><span style="color: #007700">);<br><br></span><span style="color: #FF8000">/**<br>&nbsp;*&nbsp;Verifies&nbsp;user&nbsp;credentials.<br>&nbsp;*/<br></span><span style="color: #007700">function&nbsp;</span><span style="color: #0000BB">verifyCreds</span><span style="color: #007700">(</span><span style="color: #0000BB">$conn</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$username</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$password</span><span style="color: #007700">)&nbsp;{<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$usr&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">real_escape_string</span><span style="color: #007700">(</span><span style="color: #0000BB">$username</span><span style="color: #007700">);<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$res&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">query</span><span style="color: #007700">(</span><span style="color: #DD0000">"SELECT&nbsp;password&nbsp;FROM&nbsp;users&nbsp;WHERE&nbsp;username='"</span><span style="color: #007700">.</span><span style="color: #0000BB">$usr</span><span style="color: #007700">.</span><span style="color: #DD0000">"'"</span><span style="color: #007700">);<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$row&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$res</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">fetch_assoc</span><span style="color: #007700">();<br>&nbsp;&nbsp;if&nbsp;(</span><span style="color: #0000BB">$row</span><span style="color: #007700">)&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(</span><span style="color: #0000BB">password_verify</span><span style="color: #007700">(</span><span style="color: #0000BB">$password</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$row</span><span style="color: #007700">[</span><span style="color: #DD0000">'password'</span><span style="color: #007700">]))&nbsp;return&nbsp;</span><span style="color: #0000BB">true</span><span style="color: #007700">;<br>&nbsp;&nbsp;&nbsp;&nbsp;else&nbsp;</span><span style="color: #0000BB">addFailedLoginAttempt</span><span style="color: #007700">(</span><span style="color: #0000BB">$conn</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$_SERVER</span><span style="color: #007700">[</span><span style="color: #DD0000">'REMOTE_ADDR'</span><span style="color: #007700">]);<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;return&nbsp;</span><span style="color: #0000BB">false</span><span style="color: #007700">;<br>}<br><br></span><span style="color: #FF8000">/**<br>&nbsp;*&nbsp;Determines&nbsp;if&nbsp;the&nbsp;given&nbsp;user&nbsp;is&nbsp;admin.<br>&nbsp;*/<br></span><span style="color: #007700">function&nbsp;</span><span style="color: #0000BB">isAdmin</span><span style="color: #007700">(</span><span style="color: #0000BB">$username</span><span style="color: #007700">)&nbsp;{<br>&nbsp;&nbsp;return&nbsp;(</span><span style="color: #0000BB">$username&nbsp;</span><span style="color: #007700">===&nbsp;</span><span style="color: #DD0000">'santa'</span><span style="color: #007700">);<br>}<br><br></span><span style="color: #FF8000">/**<br>&nbsp;*&nbsp;Determines&nbsp;if&nbsp;the&nbsp;given&nbsp;username&nbsp;is&nbsp;already&nbsp;taken.<br>&nbsp;*/<br></span><span style="color: #007700">function&nbsp;</span><span style="color: #0000BB">isUsernameAvailable</span><span style="color: #007700">(</span><span style="color: #0000BB">$conn</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$username</span><span style="color: #007700">)&nbsp;{<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$usr&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">real_escape_string</span><span style="color: #007700">(</span><span style="color: #0000BB">$username</span><span style="color: #007700">);<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$res&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">query</span><span style="color: #007700">(</span><span style="color: #DD0000">"SELECT&nbsp;COUNT(*)&nbsp;AS&nbsp;cnt&nbsp;FROM&nbsp;users&nbsp;WHERE&nbsp;LOWER(username)&nbsp;=&nbsp;BINARY&nbsp;LOWER('"</span><span style="color: #007700">.</span><span style="color: #0000BB">$usr</span><span style="color: #007700">.</span><span style="color: #DD0000">"')"</span><span style="color: #007700">);<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$row&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$res</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">fetch_assoc</span><span style="color: #007700">();<br>&nbsp;&nbsp;return&nbsp;(int)</span><span style="color: #0000BB">$row</span><span style="color: #007700">[</span><span style="color: #DD0000">'cnt'</span><span style="color: #007700">]&nbsp;===&nbsp;</span><span style="color: #0000BB">0</span><span style="color: #007700">;<br>}<br><br></span><span style="color: #FF8000">/**<br>&nbsp;*&nbsp;Registers&nbsp;a&nbsp;new&nbsp;user.<br>&nbsp;*/<br></span><span style="color: #007700">function&nbsp;</span><span style="color: #0000BB">registerUser</span><span style="color: #007700">(</span><span style="color: #0000BB">$conn</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$username</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$password</span><span style="color: #007700">)&nbsp;{<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$usr&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">real_escape_string</span><span style="color: #007700">(</span><span style="color: #0000BB">$username</span><span style="color: #007700">);<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$pwd&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">password_hash</span><span style="color: #007700">(</span><span style="color: #0000BB">$password</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">PASSWORD_DEFAULT</span><span style="color: #007700">);<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">query</span><span style="color: #007700">(</span><span style="color: #DD0000">"INSERT&nbsp;INTO&nbsp;users&nbsp;(username,&nbsp;password)&nbsp;VALUES&nbsp;(UPPER('"</span><span style="color: #007700">.</span><span style="color: #0000BB">$usr</span><span style="color: #007700">.</span><span style="color: #DD0000">"'),'"</span><span style="color: #007700">.</span><span style="color: #0000BB">$pwd</span><span style="color: #007700">.</span><span style="color: #DD0000">"')&nbsp;ON&nbsp;DUPLICATE&nbsp;KEY&nbsp;UPDATE&nbsp;password='"</span><span style="color: #007700">.</span><span style="color: #0000BB">$pwd</span><span style="color: #007700">.</span><span style="color: #DD0000">"'"</span><span style="color: #007700">);<br>}<br><br></span><span style="color: #FF8000">/**<br>&nbsp;*&nbsp;Adds&nbsp;a&nbsp;failed&nbsp;login&nbsp;attempt&nbsp;for&nbsp;the&nbsp;given&nbsp;ip&nbsp;address.&nbsp;An&nbsp;ip&nbsp;address&nbsp;gets&nbsp;blacklisted&nbsp;for&nbsp;15&nbsp;minutes&nbsp;if&nbsp;there&nbsp;are&nbsp;more&nbsp;than&nbsp;3&nbsp;failed&nbsp;login&nbsp;attempts.<br>&nbsp;*/<br></span><span style="color: #007700">function&nbsp;</span><span style="color: #0000BB">addFailedLoginAttempt</span><span style="color: #007700">(</span><span style="color: #0000BB">$conn</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$ip</span><span style="color: #007700">)&nbsp;{<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$ip&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">real_escape_string</span><span style="color: #007700">(</span><span style="color: #0000BB">$ip</span><span style="color: #007700">);<br>&nbsp;&nbsp;</span><span style="color: #0000BB">$conn</span><span style="color: #007700">-&gt;</span><span style="color: #0000BB">query</span><span style="color: #007700">(</span><span style="color: #DD0000">"INSERT&nbsp;INTO&nbsp;fails&nbsp;(ip)&nbsp;VALUES&nbsp;('"</span><span style="color: #007700">.</span><span style="color: #0000BB">$ip</span><span style="color: #007700">.</span><span style="color: #DD0000">"')"</span><span style="color: #007700">);<br>}<br><br></span><span style="color: #0000BB">?&gt;<br></span>
</span>
</code></body></html>