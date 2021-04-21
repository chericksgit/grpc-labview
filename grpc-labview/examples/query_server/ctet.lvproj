<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="19008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="ctet_dio" Type="Folder">
			<Item Name="ctet_dio.lvlib" Type="Library" URL="../Servers/ctet_dio/ctet_dio.lvlib"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Get LV Class Path.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/LVClass/Get LV Class Path.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
	<Item Name="NI-PXIe-8821-0320C16A" Type="RT PXI Chassis">
		<Property Name="alias.name" Type="Str">NI-PXIe-8821-0320C16A</Property>
		<Property Name="alias.value" Type="Str">192.168.1.20</Property>
		<Property Name="CCSymbols" Type="Str">TARGET_TYPE,RT;OS,Linux;CPU,x64;</Property>
		<Property Name="host.ResponsivenessCheckEnabled" Type="Bool">true</Property>
		<Property Name="host.ResponsivenessCheckPingDelay" Type="UInt">5000</Property>
		<Property Name="host.ResponsivenessCheckPingTimeout" Type="UInt">1000</Property>
		<Property Name="host.TargetCPUID" Type="UInt">9</Property>
		<Property Name="host.TargetOSID" Type="UInt">19</Property>
		<Property Name="target.cleanupVisa" Type="Bool">false</Property>
		<Property Name="target.FPProtocolGlobals_ControlTimeLimit" Type="Int">300</Property>
		<Property Name="target.getDefault-&gt;WebServer.Port" Type="Int">80</Property>
		<Property Name="target.getDefault-&gt;WebServer.Timeout" Type="Int">60</Property>
		<Property Name="target.IOScan.Faults" Type="Str"></Property>
		<Property Name="target.IOScan.NetVarPeriod" Type="UInt">100</Property>
		<Property Name="target.IOScan.NetWatchdogEnabled" Type="Bool">false</Property>
		<Property Name="target.IOScan.Period" Type="UInt">10000</Property>
		<Property Name="target.IOScan.PowerupMode" Type="UInt">0</Property>
		<Property Name="target.IOScan.Priority" Type="UInt">0</Property>
		<Property Name="target.IOScan.ReportModeConflict" Type="Bool">true</Property>
		<Property Name="target.IsRemotePanelSupported" Type="Bool">true</Property>
		<Property Name="target.RTCPULoadMonitoringEnabled" Type="Bool">true</Property>
		<Property Name="target.RTDebugWebServerHTTPPort" Type="Int">8001</Property>
		<Property Name="target.RTTarget.ApplicationPath" Type="Path">/home/lvuser/natinst/bin/startup.rtexe</Property>
		<Property Name="target.RTTarget.EnableFileSharing" Type="Bool">true</Property>
		<Property Name="target.RTTarget.IPAccess" Type="Str">+*</Property>
		<Property Name="target.RTTarget.LaunchAppAtBoot" Type="Bool">true</Property>
		<Property Name="target.RTTarget.VIPath" Type="Path">/home/lvuser/natinst/bin</Property>
		<Property Name="target.server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="target.server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="target.server.tcp.access" Type="Str">+*</Property>
		<Property Name="target.server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="target.server.tcp.paranoid" Type="Bool">true</Property>
		<Property Name="target.server.tcp.port" Type="Int">3363</Property>
		<Property Name="target.server.tcp.serviceName" Type="Str">Main Application Instance/VI Server</Property>
		<Property Name="target.server.tcp.serviceName.default" Type="Str">Main Application Instance/VI Server</Property>
		<Property Name="target.server.vi.access" Type="Str">+*</Property>
		<Property Name="target.server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="target.server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="target.WebServer.Config" Type="Str">Listen 8000

NI.ServerName default
DocumentRoot "$LVSERVER_DOCROOT"
TypesConfig "$LVSERVER_CONFIGROOT/mime.types"
DirectoryIndex index.htm
WorkerLimit 10
InactivityTimeout 60

LoadModulePath "$LVSERVER_MODULEPATHS"
LoadModule LVAuth lvauthmodule
LoadModule LVRFP lvrfpmodule

#
# Pipeline Definition
#

SetConnector netConnector

AddHandler LVAuth
AddHandler LVRFP

AddHandler fileHandler ""

AddOutputFilter chunkFilter


</Property>
		<Property Name="target.WebServer.Enabled" Type="Bool">false</Property>
		<Property Name="target.WebServer.LogEnabled" Type="Bool">false</Property>
		<Property Name="target.WebServer.LogPath" Type="Path">/c/ni-rt/system/www/www.log</Property>
		<Property Name="target.WebServer.Port" Type="Int">80</Property>
		<Property Name="target.WebServer.RootPath" Type="Path">/c/ni-rt/system/www</Property>
		<Property Name="target.WebServer.TcpAccess" Type="Str">c+*</Property>
		<Property Name="target.WebServer.Timeout" Type="Int">60</Property>
		<Property Name="target.WebServer.ViAccess" Type="Str">+*</Property>
		<Property Name="target.webservices.SecurityAPIKey" Type="Str">PqVr/ifkAQh+lVrdPIykXlFvg12GhhQFR8H9cUhphgg=:pTe9HRlQuMfJxAG6QCGq7UvoUpJzAzWGKy5SbZ+roSU=</Property>
		<Property Name="target.webservices.ValidTimestampWindow" Type="Int">15</Property>
		<Item Name="ctet_dmm" Type="Folder">
			<Item Name="ctet_dmm.lvlib" Type="Library" URL="../Servers/ctet_dmm/ctet_dmm.lvlib"/>
		</Item>
		<Item Name="ctet_dmm User" Type="Folder">
			<Item Name="ctet_dmm User Library.lvlib" Type="Library" URL="../User/dmm/ctet_dmm User Library.lvlib"/>
		</Item>
		<Item Name="ctet_smu" Type="Folder">
			<Item Name="ctet_smu.lvlib" Type="Library" URL="../Servers/ctet_smu/ctet_smu.lvlib"/>
		</Item>
		<Item Name="ctet_smu User" Type="Folder">
			<Item Name="ctet_smu User Library.lvlib" Type="Library" URL="../User/smu/ctet_smu User Library.lvlib"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="instr.lib" Type="Folder">
				<Item Name="niDCPower Abort.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Abort.vi"/>
				<Item Name="niDCPower Cal Self Calibrate.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Cal Self Calibrate.vi"/>
				<Item Name="niDCPower Close.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Close.vi"/>
				<Item Name="niDCPower Commit.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Commit.vi"/>
				<Item Name="niDCPower Configure Current Level Range.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Configure Current Level Range.vi"/>
				<Item Name="niDCPower Configure Current Level.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Configure Current Level.vi"/>
				<Item Name="niDCPower Configure Output Enabled.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Configure Output Enabled.vi"/>
				<Item Name="niDCPower Configure Output Function.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Configure Output Function.vi"/>
				<Item Name="niDCPower Configure Source Mode.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Configure Source Mode.vi"/>
				<Item Name="niDCPower Configure Voltage Limit Range.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Configure Voltage Limit Range.vi"/>
				<Item Name="niDCPower Configure Voltage Limit.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Configure Voltage Limit.vi"/>
				<Item Name="niDCPower Initialize With Channels.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Initialize With Channels.vi"/>
				<Item Name="niDCPower Initiate.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Initiate.vi"/>
				<Item Name="niDCPower IVI Error Converter.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower IVI Error Converter.vi"/>
				<Item Name="niDCPower Measure Multiple.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Measure Multiple.vi"/>
				<Item Name="niDCPower Output Function.ctl" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Output Function.ctl"/>
				<Item Name="niDCPower Query In Compliance.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Query In Compliance.vi"/>
				<Item Name="niDCPower Reset Device.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Reset Device.vi"/>
				<Item Name="niDCPower Source Mode.ctl" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Source Mode.ctl"/>
				<Item Name="niDCPower Wait For Event - Event.ctl" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Wait For Event - Event.ctl"/>
				<Item Name="niDCPower Wait For Event.vi" Type="VI" URL="/&lt;instrlib&gt;/niDCPower/nidcpower.llb/niDCPower Wait For Event.vi"/>
				<Item Name="niDMM Close.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Close.vi"/>
				<Item Name="niDMM Config Measurement.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Config Measurement.vi"/>
				<Item Name="niDMM Configure Measurement Absolute.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Configure Measurement Absolute.vi"/>
				<Item Name="niDMM Configure Measurement Digits.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Configure Measurement Digits.vi"/>
				<Item Name="niDMM Control Actions.ctl" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Control Actions.ctl"/>
				<Item Name="niDMM Control.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Control.vi"/>
				<Item Name="niDMM Function To IVI Constant.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Function To IVI Constant.vi"/>
				<Item Name="niDMM Function.ctl" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Function.ctl"/>
				<Item Name="niDMM Initialize.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Initialize.vi"/>
				<Item Name="niDMM IVI Error Converter.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM IVI Error Converter.vi"/>
				<Item Name="niDMM Read.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Read.vi"/>
				<Item Name="niDMM Reset.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Reset.vi"/>
				<Item Name="niDMM Resolution in Digits.ctl" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Resolution in Digits.ctl"/>
				<Item Name="niDMM Self Cal.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Self Cal.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Get LV Class Path.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/LVClass/Get LV Class Path.vi"/>
			</Item>
			<Item Name="nidcpower_32.dll" Type="Document" URL="nidcpower_32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nidmm_32.dll" Type="Document" URL="nidmm_32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="DMM" Type="{69A947D5-514E-4E75-818E-69657C0547D8}">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{0475A22B-6EB6-4724-839F-E1907635A17C}</Property>
				<Property Name="App_INI_GUID" Type="Str">{F83F4D0D-6A25-4A3E-BA7D-0526A870EAD8}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{C4FB8DE6-87F8-455A-A73D-08D5350E9091}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">DMM</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/NI_AB_TARGETNAME/DMM</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{CC19CB12-CBDF-436C-B5D2-1A9BC6FB8ECE}</Property>
				<Property Name="Bld_targetDestDir" Type="Path">/home/lvuser/natinst/bin</Property>
				<Property Name="Bld_version.build" Type="Int">6</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">startup.rtexe</Property>
				<Property Name="Destination[0].path" Type="Path">/home/lvuser/natinst/bin/startup.rtexe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">/home/lvuser/natinst/bin</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{D0A9A405-FB8A-4380-8ABE-FF9636433629}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/NI-PXIe-8821-0320C16A/ctet_dmm/ctet_dmm.lvlib/gprc-lvsupport.lvlib/Libraries/LinuxRT/liblabview_grpc_server.so</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/NI-PXIe-8821-0320C16A/ctet_dmm User/ctet_dmm User Library.lvlib/ctet_dmm_User Main.vi</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[2].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">3</Property>
				<Property Name="TgtF_companyName" Type="Str">National Instruments</Property>
				<Property Name="TgtF_fileDescription" Type="Str">DMM</Property>
				<Property Name="TgtF_internalName" Type="Str">DMM</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2021 National Instruments</Property>
				<Property Name="TgtF_productName" Type="Str">DMM</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{19FDEA70-81F7-472C-A60C-852E8A1FC093}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">startup.rtexe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="SMU" Type="{69A947D5-514E-4E75-818E-69657C0547D8}">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{99E71308-1D32-483E-8924-4BD195E85056}</Property>
				<Property Name="App_INI_GUID" Type="Str">{4FDD842F-36E7-4F6E-BF75-922443159353}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{B03D998B-EC35-40D8-B6A8-0C9AA34E2A2C}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">SMU</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/NI_AB_TARGETNAME/SMU</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{9F7C43BC-74C4-455B-9E89-BD6FE40ACF93}</Property>
				<Property Name="Bld_targetDestDir" Type="Path">/home/lvuser/natinst/bin</Property>
				<Property Name="Bld_version.build" Type="Int">3</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">startup.rtexe</Property>
				<Property Name="Destination[0].path" Type="Path">/home/lvuser/natinst/bin/startup.rtexe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">/home/lvuser/natinst/bin</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{D0A9A405-FB8A-4380-8ABE-FF9636433629}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/NI-PXIe-8821-0320C16A/ctet_smu/ctet_smu.lvlib/gprc-lvsupport.lvlib/Libraries/LinuxRT/liblabview_grpc_server.so</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/NI-PXIe-8821-0320C16A/ctet_smu User/ctet_smu User Library.lvlib/ctet_smu_User Main.vi</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[2].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">3</Property>
				<Property Name="TgtF_companyName" Type="Str">National Instruments</Property>
				<Property Name="TgtF_fileDescription" Type="Str">SMU</Property>
				<Property Name="TgtF_internalName" Type="Str">SMU</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2021 National Instruments</Property>
				<Property Name="TgtF_productName" Type="Str">SMU</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{D4036B87-3704-407A-9543-E5878B35D45C}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">startup.rtexe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
