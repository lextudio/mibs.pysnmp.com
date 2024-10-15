# SNMP MIB module (NETRANGER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETRANGER
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:40 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wheelgroup_ObjectIdentity = ObjectIdentity
wheelgroup = _Wheelgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252)
)
_SecurityMgmt_ObjectIdentity = ObjectIdentity
securityMgmt = _SecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1)
)
_Netranger_ObjectIdentity = ObjectIdentity
netranger = _Netranger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1)
)
_NrTrapVars_ObjectIdentity = ObjectIdentity
nrTrapVars = _NrTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1)
)
_CommonVars_ObjectIdentity = ObjectIdentity
commonVars = _CommonVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0)
)
_MessageType_Type = Integer32
_MessageType_Object = MibScalar
messageType = _MessageType_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 1),
    _MessageType_Type()
)
messageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageType.setStatus("mandatory")
_RecordId_Type = Integer32
_RecordId_Object = MibScalar
recordId = _RecordId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 2),
    _RecordId_Type()
)
recordId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordId.setStatus("mandatory")
_GlobalTime_Type = Integer32
_GlobalTime_Object = MibScalar
globalTime = _GlobalTime_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 3),
    _GlobalTime_Type()
)
globalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTime.setStatus("mandatory")
_LocalTime_Type = Integer32
_LocalTime_Object = MibScalar
localTime = _LocalTime_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 4),
    _LocalTime_Type()
)
localTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localTime.setStatus("mandatory")
_DateString_Type = DisplayString
_DateString_Object = MibScalar
dateString = _DateString_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 5),
    _DateString_Type()
)
dateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateString.setStatus("mandatory")
_TimeString_Type = DisplayString
_TimeString_Object = MibScalar
timeString = _TimeString_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 6),
    _TimeString_Type()
)
timeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeString.setStatus("mandatory")
_AppId_Type = Integer32
_AppId_Object = MibScalar
appId = _AppId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 7),
    _AppId_Type()
)
appId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appId.setStatus("mandatory")
_HostId_Type = Integer32
_HostId_Object = MibScalar
hostId = _HostId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 8),
    _HostId_Type()
)
hostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostId.setStatus("mandatory")
_OrgId_Type = Integer32
_OrgId_Object = MibScalar
orgId = _OrgId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 9),
    _OrgId_Type()
)
orgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orgId.setStatus("mandatory")
_Command_ObjectIdentity = ObjectIdentity
command = _Command_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 1)
)
_Error_ObjectIdentity = ObjectIdentity
error = _Error_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 2)
)
_ErrorMessage_Type = DisplayString
_ErrorMessage_Object = MibScalar
errorMessage = _ErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 2, 1),
    _ErrorMessage_Type()
)
errorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMessage.setStatus("mandatory")
_CommandLog_ObjectIdentity = ObjectIdentity
commandLog = _CommandLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3)
)
_SourceAppId_Type = Integer32
_SourceAppId_Object = MibScalar
sourceAppId = _SourceAppId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 1),
    _SourceAppId_Type()
)
sourceAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceAppId.setStatus("mandatory")
_SourceHostId_Type = Integer32
_SourceHostId_Object = MibScalar
sourceHostId = _SourceHostId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 2),
    _SourceHostId_Type()
)
sourceHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceHostId.setStatus("mandatory")
_SourceOrgId_Type = Integer32
_SourceOrgId_Object = MibScalar
sourceOrgId = _SourceOrgId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 3),
    _SourceOrgId_Type()
)
sourceOrgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceOrgId.setStatus("mandatory")
_CommandMessage_Type = DisplayString
_CommandMessage_Object = MibScalar
commandMessage = _CommandMessage_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 4),
    _CommandMessage_Type()
)
commandMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandMessage.setStatus("mandatory")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4)
)
_Addressing_ObjectIdentity = ObjectIdentity
addressing = _Addressing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1)
)
_Tcpip_ObjectIdentity = ObjectIdentity
tcpip = _Tcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1)
)
_SrcIpAddr_Type = DisplayString
_SrcIpAddr_Object = MibScalar
srcIpAddr = _SrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 1),
    _SrcIpAddr_Type()
)
srcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcIpAddr.setStatus("mandatory")
_DstIpAddr_Type = DisplayString
_DstIpAddr_Object = MibScalar
dstIpAddr = _DstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 3),
    _DstIpAddr_Type()
)
dstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstIpAddr.setStatus("mandatory")
_SrcIpPort_Type = Integer32
_SrcIpPort_Object = MibScalar
srcIpPort = _SrcIpPort_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 5),
    _SrcIpPort_Type()
)
srcIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcIpPort.setStatus("mandatory")
_DstIpPort_Type = Integer32
_DstIpPort_Object = MibScalar
dstIpPort = _DstIpPort_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 7),
    _DstIpPort_Type()
)
dstIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstIpPort.setStatus("mandatory")
_RtrIpAddr_Type = DisplayString
_RtrIpAddr_Object = MibScalar
rtrIpAddr = _RtrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 9),
    _RtrIpAddr_Type()
)
rtrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIpAddr.setStatus("mandatory")
_SrcDirection_Type = DisplayString
_SrcDirection_Object = MibScalar
srcDirection = _SrcDirection_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 3),
    _SrcDirection_Type()
)
srcDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcDirection.setStatus("mandatory")
_DstDirection_Type = DisplayString
_DstDirection_Object = MibScalar
dstDirection = _DstDirection_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 5),
    _DstDirection_Type()
)
dstDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstDirection.setStatus("mandatory")
_EventLevel_Type = Integer32
_EventLevel_Object = MibScalar
eventLevel = _EventLevel_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 7),
    _EventLevel_Type()
)
eventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLevel.setStatus("mandatory")
_SigId_Type = Integer32
_SigId_Object = MibScalar
sigId = _SigId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 9),
    _SigId_Type()
)
sigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigId.setStatus("mandatory")
_SubSigId_Type = Integer32
_SubSigId_Object = MibScalar
subSigId = _SubSigId_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 11),
    _SubSigId_Type()
)
subSigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSigId.setStatus("mandatory")
_Protocol_Type = DisplayString
_Protocol_Object = MibScalar
protocol = _Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 13),
    _Protocol_Type()
)
protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocol.setStatus("mandatory")
_AlarmMessage_Type = DisplayString
_AlarmMessage_Object = MibScalar
alarmMessage = _AlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 15),
    _AlarmMessage_Type()
)
alarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMessage.setStatus("mandatory")
_IpLog_ObjectIdentity = ObjectIdentity
ipLog = _IpLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 5)
)
_Redirect_ObjectIdentity = ObjectIdentity
redirect = _Redirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 6)
)
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3)
)
_Postoffice_ObjectIdentity = ObjectIdentity
postoffice = _Postoffice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 0)
)
_Sensor_ObjectIdentity = ObjectIdentity
sensor = _Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 1)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 2)
)
_Manage_ObjectIdentity = ObjectIdentity
manage = _Manage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 3)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 4)
)
_Logger_ObjectIdentity = ObjectIdentity
logger = _Logger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 5)
)
_Smi_ObjectIdentity = ObjectIdentity
smi = _Smi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 6)
)
_Sap_ObjectIdentity = ObjectIdentity
sap = _Sap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 7)
)
_Packet_ObjectIdentity = ObjectIdentity
packet = _Packet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 8)
)
_CommonServices_ObjectIdentity = ObjectIdentity
commonServices = _CommonServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 9)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 1, 5)
)
_Autospa_ObjectIdentity = ObjectIdentity
autospa = _Autospa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 1, 3)
)
_NetworkMgmt_ObjectIdentity = ObjectIdentity
networkMgmt = _NetworkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 3)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 3, 1)
)
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 3, 3)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2252, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETRANGER",
    **{"wheelgroup": wheelgroup,
       "securityMgmt": securityMgmt,
       "netranger": netranger,
       "nrTrapVars": nrTrapVars,
       "commonVars": commonVars,
       "messageType": messageType,
       "recordId": recordId,
       "globalTime": globalTime,
       "localTime": localTime,
       "dateString": dateString,
       "timeString": timeString,
       "appId": appId,
       "hostId": hostId,
       "orgId": orgId,
       "command": command,
       "error": error,
       "errorMessage": errorMessage,
       "commandLog": commandLog,
       "sourceAppId": sourceAppId,
       "sourceHostId": sourceHostId,
       "sourceOrgId": sourceOrgId,
       "commandMessage": commandMessage,
       "alarm": alarm,
       "addressing": addressing,
       "tcpip": tcpip,
       "srcIpAddr": srcIpAddr,
       "dstIpAddr": dstIpAddr,
       "srcIpPort": srcIpPort,
       "dstIpPort": dstIpPort,
       "rtrIpAddr": rtrIpAddr,
       "srcDirection": srcDirection,
       "dstDirection": dstDirection,
       "eventLevel": eventLevel,
       "sigId": sigId,
       "subSigId": subSigId,
       "protocol": protocol,
       "alarmMessage": alarmMessage,
       "ipLog": ipLog,
       "redirect": redirect,
       "services": services,
       "postoffice": postoffice,
       "sensor": sensor,
       "config": config,
       "manage": manage,
       "event": event,
       "logger": logger,
       "smi": smi,
       "sap": sap,
       "packet": packet,
       "commonServices": commonServices,
       "general": general,
       "autospa": autospa,
       "networkMgmt": networkMgmt,
       "system": system,
       "ip": ip,
       "snmp": snmp}
)
