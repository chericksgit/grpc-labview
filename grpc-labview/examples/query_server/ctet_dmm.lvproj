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
		<Item Name="ctet_dmm User" Type="Folder">
			<Item Name="ctet_dmm User Library.lvlib" Type="Library" URL="../User/ctet_dmm User Library.lvlib"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="instr.lib" Type="Folder">
				<Item Name="niDMM Close.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Close.vi"/>
				<Item Name="niDMM Initialize.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Initialize.vi"/>
				<Item Name="niDMM IVI Error Converter.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM IVI Error Converter.vi"/>
				<Item Name="niDMM Reset.vi" Type="VI" URL="/&lt;instrlib&gt;/niDMM/nidmm.llb/niDMM Reset.vi"/>
			</Item>
			<Item Name="Create Server.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/Server API/Create Server.vi"/>
			<Item Name="ctet_dmm.ctl" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/ctet_dmm.lvclass/ctet_dmm.ctl"/>
			<Item Name="Get measurementservice_DMMCloseSessionRequest.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMCloseSessionRequest/Get measurementservice_DMMCloseSessionRequest.vi"/>
			<Item Name="Get measurementservice_DMMOpenSessionRequest.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMOpenSessionRequest/Get measurementservice_DMMOpenSessionRequest.vi"/>
			<Item Name="Get measurementservice_DMMResetRequest.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMResetRequest/Get measurementservice_DMMResetRequest.vi"/>
			<Item Name="Get measurementservice_QueryRequest.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_QueryRequest/Get measurementservice_QueryRequest.vi"/>
			<Item Name="Get Server gRPC UEs.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/Accessors/Server gRPC UEs/Get Server gRPC UEs.vi"/>
			<Item Name="Get Server Stop UE.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/Accessors/Server Stop UE/Get Server Stop UE.vi"/>
			<Item Name="grpcId.ctl" Type="VI" URL="../Servers/ctet_dmm/gRPC lvSupport/Server API/typeDefs/grpcId.ctl"/>
			<Item Name="Initialize Server State.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/Server API/Initialize Server State.vi"/>
			<Item Name="measurementservice_DMMCloseSessionResponse_Data.ctl" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMCloseSessionResponse/measurementservice_DMMCloseSessionResponse_Data.ctl"/>
			<Item Name="measurementservice_DMMOpenSessionResponse_Data.ctl" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMOpenSessionResponse/measurementservice_DMMOpenSessionResponse_Data.ctl"/>
			<Item Name="measurementservice_DMMResetResponse_Data.ctl" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMResetResponse/measurementservice_DMMResetResponse_Data.ctl"/>
			<Item Name="measurementservice_ErrorOut_Data.ctl" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_ErrorOut/measurementservice_ErrorOut_Data.ctl"/>
			<Item Name="measurementservice_QueryResponse_Data.ctl" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_QueryResponse/measurementservice_QueryResponse_Data.ctl"/>
			<Item Name="nidmm_32.dll" Type="Document" URL="nidmm_32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Server State Data.ctl" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/typeDefs/Server State Data.ctl"/>
			<Item Name="Set measurementservice_DMMCloseSessionResponse.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMCloseSessionResponse/Set measurementservice_DMMCloseSessionResponse.vi"/>
			<Item Name="Set measurementservice_DMMOpenSessionResponse.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMOpenSessionResponse/Set measurementservice_DMMOpenSessionResponse.vi"/>
			<Item Name="Set measurementservice_DMMResetResponse.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_DMMResetResponse/Set measurementservice_DMMResetResponse.vi"/>
			<Item Name="Set measurementservice_QueryResponse.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/RPC Messages/measurementservice_QueryResponse/Set measurementservice_QueryResponse.vi"/>
			<Item Name="Start Server.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/Server API/Start Server.vi"/>
			<Item Name="Stop Server.vi" Type="VI" URL="../Servers/ctet_dmm/ctet_dmm Class/Server API/Stop Server.vi"/>
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
		<Property Name="target.RTTarget.LaunchAppAtBoot" Type="Bool">false</Property>
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
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
