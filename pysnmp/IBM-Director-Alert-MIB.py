# SNMP MIB module (IBM-Director-Alert-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-Director-Alert-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:26 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

directorTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201)
)
directorTraps.setRevisions(
        ("2004-04-21 00:00",
         "2003-07-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Director_ObjectIdentity = ObjectIdentity
director = _Director_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159)
)
_DirectorFamily_ObjectIdentity = ObjectIdentity
directorFamily = _DirectorFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1)
)
_Topology_ObjectIdentity = ObjectIdentity
topology = _Topology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 1)
)
_DirectorAgent_ObjectIdentity = ObjectIdentity
directorAgent = _DirectorAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2)
)
_CpuMonitors_ObjectIdentity = ObjectIdentity
cpuMonitors = _CpuMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 2)
)
_DiskMonitors_ObjectIdentity = ObjectIdentity
diskMonitors = _DiskMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 3)
)
_MemoryMonitors_ObjectIdentity = ObjectIdentity
memoryMonitors = _MemoryMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 4)
)
_NicMonitors_ObjectIdentity = ObjectIdentity
nicMonitors = _NicMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 5)
)
_NtPerfMonitors_ObjectIdentity = ObjectIdentity
ntPerfMonitors = _NtPerfMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 6)
)
_TcpipMonitors_ObjectIdentity = ObjectIdentity
tcpipMonitors = _TcpipMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 7)
)
_MonitorEventDetails_ObjectIdentity = ObjectIdentity
monitorEventDetails = _MonitorEventDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 8)
)
_ActualValue_Type = SnmpAdminString
_ActualValue_Object = MibScalar
actualValue = _ActualValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 8, 1),
    _ActualValue_Type()
)
actualValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualValue.setStatus("current")
_Duration_Type = DisplayString
_Duration_Object = MibScalar
duration = _Duration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 8, 2),
    _Duration_Type()
)
duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duration.setStatus("current")
_MonitorResource_Type = SnmpAdminString
_MonitorResource_Object = MibScalar
monitorResource = _MonitorResource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 8, 3),
    _MonitorResource_Type()
)
monitorResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorResource.setStatus("current")
_ThresholdName_Type = SnmpAdminString
_ThresholdName_Object = MibScalar
thresholdName = _ThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 8, 4),
    _ThresholdName_Type()
)
thresholdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdName.setStatus("current")
_ThresholdValue_Type = SnmpAdminString
_ThresholdValue_Object = MibScalar
thresholdValue = _ThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 8, 5),
    _ThresholdValue_Type()
)
thresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdValue.setStatus("current")
_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 3)
)
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4)
)
_ConsoleEventDetails_ObjectIdentity = ObjectIdentity
consoleEventDetails = _ConsoleEventDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 1)
)
_UserID_Type = SnmpAdminString
_UserID_Object = MibScalar
userID = _UserID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 1, 1),
    _UserID_Type()
)
userID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userID.setStatus("current")
_Address_Type = SnmpAdminString
_Address_Object = MibScalar
address = _Address_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 1, 2),
    _Address_Type()
)
address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    address.setStatus("current")
_UserName_Type = SnmpAdminString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 1, 3),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserDescription_Type = SnmpAdminString
_UserDescription_Object = MibScalar
userDescription = _UserDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 1, 4),
    _UserDescription_Type()
)
userDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDescription.setStatus("current")
_UserLocale_Type = SnmpAdminString
_UserLocale_Object = MibScalar
userLocale = _UserLocale_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 1, 5),
    _UserLocale_Type()
)
userLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLocale.setStatus("current")
_LogonFailure_ObjectIdentity = ObjectIdentity
logonFailure = _LogonFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2)
)
_CimFamily_ObjectIdentity = ObjectIdentity
cimFamily = _CimFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3)
)
_WindowsNTEventLog_ObjectIdentity = ObjectIdentity
windowsNTEventLog = _WindowsNTEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1)
)
_WindowsNTEventLogEventDetails_ObjectIdentity = ObjectIdentity
windowsNTEventLogEventDetails = _WindowsNTEventLogEventDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1)
)
_Category_Type = Integer32
_Category_Object = MibScalar
category = _Category_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 1),
    _Category_Type()
)
category.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    category.setStatus("current")
_CategoryString_Type = SnmpAdminString
_CategoryString_Object = MibScalar
categoryString = _CategoryString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 2),
    _CategoryString_Type()
)
categoryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    categoryString.setStatus("current")
_ComputerName_Type = SnmpAdminString
_ComputerName_Object = MibScalar
computerName = _ComputerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 3),
    _ComputerName_Type()
)
computerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerName.setStatus("current")
_Data_Type = OctetString
_Data_Object = MibScalar
data = _Data_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 4),
    _Data_Type()
)
data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    data.setStatus("current")
_EventLogCode_Type = Integer32
_EventLogCode_Object = MibScalar
eventLogCode = _EventLogCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 5),
    _EventLogCode_Type()
)
eventLogCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogCode.setStatus("current")
_EventLogIdentifier_Type = DisplayString
_EventLogIdentifier_Object = MibScalar
eventLogIdentifier = _EventLogIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 6),
    _EventLogIdentifier_Type()
)
eventLogIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIdentifier.setStatus("current")
_EventLogType_Type = Integer32
_EventLogType_Object = MibScalar
eventLogType = _EventLogType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 7),
    _EventLogType_Type()
)
eventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogType.setStatus("current")
_InsertionStrings_Type = SnmpAdminString
_InsertionStrings_Object = MibScalar
insertionStrings = _InsertionStrings_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 8),
    _InsertionStrings_Type()
)
insertionStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insertionStrings.setStatus("current")
_LogFile_Type = SnmpAdminString
_LogFile_Object = MibScalar
logFile = _LogFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 9),
    _LogFile_Type()
)
logFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFile.setStatus("current")
_Message_Type = SnmpAdminString
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 10),
    _Message_Type()
)
message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    message.setStatus("current")
_RecordNumber_Type = DisplayString
_RecordNumber_Object = MibScalar
recordNumber = _RecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 11),
    _RecordNumber_Type()
)
recordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordNumber.setStatus("current")
_SourceName_Type = SnmpAdminString
_SourceName_Object = MibScalar
sourceName = _SourceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 12),
    _SourceName_Type()
)
sourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceName.setStatus("current")
_Type_Type = SnmpAdminString
_Type_Object = MibScalar
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 13),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("current")
_User_Type = SnmpAdminString
_User_Object = MibScalar
user = _User_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 1, 14),
    _User_Type()
)
user.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user.setStatus("current")
_WindowsNTService_ObjectIdentity = ObjectIdentity
windowsNTService = _WindowsNTService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2)
)
_WindowsNTServiceEventDetails_ObjectIdentity = ObjectIdentity
windowsNTServiceEventDetails = _WindowsNTServiceEventDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1)
)
_AcceptPause_Type = TruthValue
_AcceptPause_Object = MibScalar
acceptPause = _AcceptPause_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 1),
    _AcceptPause_Type()
)
acceptPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptPause.setStatus("current")
_AcceptStop_Type = TruthValue
_AcceptStop_Object = MibScalar
acceptStop = _AcceptStop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 2),
    _AcceptStop_Type()
)
acceptStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptStop.setStatus("current")
_Caption_Type = SnmpAdminString
_Caption_Object = MibScalar
caption = _Caption_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 3),
    _Caption_Type()
)
caption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caption.setStatus("current")
_CheckPoint_Type = DisplayString
_CheckPoint_Object = MibScalar
checkPoint = _CheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 4),
    _CheckPoint_Type()
)
checkPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkPoint.setStatus("current")
_CreationClassName_Type = SnmpAdminString
_CreationClassName_Object = MibScalar
creationClassName = _CreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 5),
    _CreationClassName_Type()
)
creationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creationClassName.setStatus("current")
_ServiceDescription_Type = SnmpAdminString
_ServiceDescription_Object = MibScalar
serviceDescription = _ServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 6),
    _ServiceDescription_Type()
)
serviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceDescription.setStatus("current")
_DesktopInteract_Type = TruthValue
_DesktopInteract_Object = MibScalar
desktopInteract = _DesktopInteract_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 7),
    _DesktopInteract_Type()
)
desktopInteract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    desktopInteract.setStatus("current")
_DisplayName_Type = SnmpAdminString
_DisplayName_Object = MibScalar
displayName = _DisplayName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 8),
    _DisplayName_Type()
)
displayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    displayName.setStatus("current")
_ErrorControl_Type = SnmpAdminString
_ErrorControl_Object = MibScalar
errorControl = _ErrorControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 9),
    _ErrorControl_Type()
)
errorControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorControl.setStatus("current")
_ExitCode_Type = DisplayString
_ExitCode_Object = MibScalar
exitCode = _ExitCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 10),
    _ExitCode_Type()
)
exitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exitCode.setStatus("current")
_Name_Type = SnmpAdminString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 11),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_PathName_Type = SnmpAdminString
_PathName_Object = MibScalar
pathName = _PathName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 12),
    _PathName_Type()
)
pathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathName.setStatus("current")
_ProcessId_Type = DisplayString
_ProcessId_Object = MibScalar
processId = _ProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 13),
    _ProcessId_Type()
)
processId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processId.setStatus("current")
_ServiceSpecificExitCode_Type = DisplayString
_ServiceSpecificExitCode_Object = MibScalar
serviceSpecificExitCode = _ServiceSpecificExitCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 14),
    _ServiceSpecificExitCode_Type()
)
serviceSpecificExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceSpecificExitCode.setStatus("current")
_ServiceType_Type = SnmpAdminString
_ServiceType_Object = MibScalar
serviceType = _ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 15),
    _ServiceType_Type()
)
serviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceType.setStatus("current")
_StartMode_Type = SnmpAdminString
_StartMode_Object = MibScalar
startMode = _StartMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 16),
    _StartMode_Type()
)
startMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startMode.setStatus("current")
_StartName_Type = SnmpAdminString
_StartName_Object = MibScalar
startName = _StartName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 17),
    _StartName_Type()
)
startName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startName.setStatus("current")
_Started_Type = TruthValue
_Started_Object = MibScalar
started = _Started_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 18),
    _Started_Type()
)
started.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    started.setStatus("current")
_ServiceState_Type = SnmpAdminString
_ServiceState_Object = MibScalar
serviceState = _ServiceState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 19),
    _ServiceState_Type()
)
serviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceState.setStatus("current")
_Status_Type = SnmpAdminString
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 20),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")
_SystemCreationClassName_Type = SnmpAdminString
_SystemCreationClassName_Object = MibScalar
systemCreationClassName = _SystemCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 21),
    _SystemCreationClassName_Type()
)
systemCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCreationClassName.setStatus("current")
_SystemName_Type = SnmpAdminString
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 22),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")
_TagId_Type = DisplayString
_TagId_Object = MibScalar
tagId = _TagId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 23),
    _TagId_Type()
)
tagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tagId.setStatus("current")
_WaitHint_Type = DisplayString
_WaitHint_Object = MibScalar
waitHint = _WaitHint_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 1, 24),
    _WaitHint_Type()
)
waitHint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waitHint.setStatus("current")
_WindowsRegistry_ObjectIdentity = ObjectIdentity
windowsRegistry = _WindowsRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3)
)
_WindowsRegistryEventDetails_ObjectIdentity = ObjectIdentity
windowsRegistryEventDetails = _WindowsRegistryEventDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3, 1)
)
_Hive_Type = SnmpAdminString
_Hive_Object = MibScalar
hive = _Hive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3, 1, 1),
    _Hive_Type()
)
hive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hive.setStatus("current")
_RootPath_Type = SnmpAdminString
_RootPath_Object = MibScalar
rootPath = _RootPath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3, 1, 2),
    _RootPath_Type()
)
rootPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootPath.setStatus("current")
_SecurityDescriptor_Type = OctetString
_SecurityDescriptor_Object = MibScalar
securityDescriptor = _SecurityDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3, 1, 3),
    _SecurityDescriptor_Type()
)
securityDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityDescriptor.setStatus("current")
_TimeCreated_Type = SnmpAdminString
_TimeCreated_Object = MibScalar
timeCreated = _TimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3, 1, 4),
    _TimeCreated_Type()
)
timeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeCreated.setStatus("current")
_MpaFamily_ObjectIdentity = ObjectIdentity
mpaFamily = _MpaFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4)
)
_MpaEventDetails_ObjectIdentity = ObjectIdentity
mpaEventDetails = _MpaEventDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1)
)
_AlertCode_Type = Integer32
_AlertCode_Object = MibScalar
alertCode = _AlertCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 1),
    _AlertCode_Type()
)
alertCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertCode.setStatus("current")
_BusId_Type = Integer32
_BusId_Object = MibScalar
busId = _BusId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 2),
    _BusId_Type()
)
busId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busId.setStatus("current")
_ComponentId_Type = SnmpAdminString
_ComponentId_Object = MibScalar
componentId = _ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 3),
    _ComponentId_Type()
)
componentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentId.setStatus("current")
_FirmwareCode_Type = OctetString
_FirmwareCode_Object = MibScalar
firmwareCode = _FirmwareCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 4),
    _FirmwareCode_Type()
)
firmwareCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareCode.setStatus("current")
_IpAddress1_Type = OctetString
_IpAddress1_Object = MibScalar
ipAddress1 = _IpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 5),
    _IpAddress1_Type()
)
ipAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress1.setStatus("current")
_IpAddress2_Type = OctetString
_IpAddress2_Object = MibScalar
ipAddress2 = _IpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 6),
    _IpAddress2_Type()
)
ipAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress2.setStatus("current")
_Issue_Type = SnmpAdminString
_Issue_Object = MibScalar
issue = _Issue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 7),
    _Issue_Type()
)
issue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issue.setStatus("current")
_PowerDomain_Type = Integer32
_PowerDomain_Object = MibScalar
powerDomain = _PowerDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 8),
    _PowerDomain_Type()
)
powerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDomain.setStatus("current")
_Reason_Type = SnmpAdminString
_Reason_Object = MibScalar
reason = _Reason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 9),
    _Reason_Type()
)
reason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reason.setStatus("current")
_ScsiId_Type = Integer32
_ScsiId_Object = MibScalar
scsiId = _ScsiId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 10),
    _ScsiId_Type()
)
scsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiId.setStatus("current")
_Side_Type = SnmpAdminString
_Side_Object = MibScalar
side = _Side_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 11),
    _Side_Type()
)
side.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    side.setStatus("current")
_NewState_Type = SnmpAdminString
_NewState_Object = MibScalar
newState = _NewState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 12),
    _NewState_Type()
)
newState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newState.setStatus("current")
_TemperatureSensor_Type = SnmpAdminString
_TemperatureSensor_Object = MibScalar
temperatureSensor = _TemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 13),
    _TemperatureSensor_Type()
)
temperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor.setStatus("current")
_Threshold_Type = SnmpAdminString
_Threshold_Object = MibScalar
threshold = _Threshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 14),
    _Threshold_Type()
)
threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threshold.setStatus("current")
_UniversalUniqueId_Type = OctetString
_UniversalUniqueId_Object = MibScalar
universalUniqueId = _UniversalUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 15),
    _UniversalUniqueId_Type()
)
universalUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalUniqueId.setStatus("current")
_SenderUniversalUniqueId_Type = OctetString
_SenderUniversalUniqueId_Object = MibScalar
senderUniversalUniqueId = _SenderUniversalUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 16),
    _SenderUniversalUniqueId_Type()
)
senderUniversalUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderUniversalUniqueId.setStatus("current")
_SourceUniversalUniqueId_Type = OctetString
_SourceUniversalUniqueId_Object = MibScalar
sourceUniversalUniqueId = _SourceUniversalUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 17),
    _SourceUniversalUniqueId_Type()
)
sourceUniversalUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceUniversalUniqueId.setStatus("current")
_UnitNumber_Type = Integer32
_UnitNumber_Object = MibScalar
unitNumber = _UnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 18),
    _UnitNumber_Type()
)
unitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNumber.setStatus("current")
_VoltageSensor_Type = SnmpAdminString
_VoltageSensor_Object = MibScalar
voltageSensor = _VoltageSensor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 1, 19),
    _VoltageSensor_Type()
)
voltageSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensor.setStatus("current")
_Component_ObjectIdentity = ObjectIdentity
component = _Component_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2)
)
_BladeServer_ObjectIdentity = ObjectIdentity
bladeServer = _BladeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 1)
)
_CoD_ObjectIdentity = ObjectIdentity
coD = _CoD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 1, 1)
)
_Bus_ObjectIdentity = ObjectIdentity
bus = _Bus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 2)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 3)
)
_Dasd_ObjectIdentity = ObjectIdentity
dasd = _Dasd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 4)
)
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 5)
)
_ComponentFan_ObjectIdentity = ObjectIdentity
componentFan = _ComponentFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 6)
)
_HardwareInformation_ObjectIdentity = ObjectIdentity
hardwareInformation = _HardwareInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 7)
)
_HardwareCrashDump_ObjectIdentity = ObjectIdentity
hardwareCrashDump = _HardwareCrashDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 7, 1)
)
_IoModule_ObjectIdentity = ObjectIdentity
ioModule = _IoModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8)
)
_IoModulePower_ObjectIdentity = ObjectIdentity
ioModulePower = _IoModulePower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 5)
)
_Kvm_ObjectIdentity = ObjectIdentity
kvm = _Kvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 9)
)
_OsImage_ObjectIdentity = ObjectIdentity
osImage = _OsImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 10)
)
_OsImageCrashDump_ObjectIdentity = ObjectIdentity
osImageCrashDump = _OsImageCrashDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 10, 1)
)
_PowerSubsystem_ObjectIdentity = ObjectIdentity
powerSubsystem = _PowerSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 12)
)
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 13)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 14)
)
_ServerPower_ObjectIdentity = ObjectIdentity
serverPower = _ServerPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 14, 1)
)
_ServiceProcessor_ObjectIdentity = ObjectIdentity
serviceProcessor = _ServiceProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15)
)
_SmpExpansionModule_ObjectIdentity = ObjectIdentity
smpExpansionModule = _SmpExpansionModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 16)
)
_Usb_ObjectIdentity = ObjectIdentity
usb = _Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 17)
)
_Vrm_ObjectIdentity = ObjectIdentity
vrm = _Vrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 18)
)
_Critical_ObjectIdentity = ObjectIdentity
critical = _Critical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3)
)
_PowerFailure_ObjectIdentity = ObjectIdentity
powerFailure = _PowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 3)
)
_CriticalTemperature_ObjectIdentity = ObjectIdentity
criticalTemperature = _CriticalTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 5)
)
_CriticalVoltage_ObjectIdentity = ObjectIdentity
criticalVoltage = _CriticalVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6)
)
_CriticalTwelveVolts_ObjectIdentity = ObjectIdentity
criticalTwelveVolts = _CriticalTwelveVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 1)
)
_CriticalOneVolt_ObjectIdentity = ObjectIdentity
criticalOneVolt = _CriticalOneVolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 6)
)
_CriticalTwoVolts_ObjectIdentity = ObjectIdentity
criticalTwoVolts = _CriticalTwoVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 7)
)
_CriticalThreeVolts_ObjectIdentity = ObjectIdentity
criticalThreeVolts = _CriticalThreeVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 8)
)
_CriticalThreeVoltsPci_ObjectIdentity = ObjectIdentity
criticalThreeVoltsPci = _CriticalThreeVoltsPci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 9)
)
_CriticalThreeVoltsStandby_ObjectIdentity = ObjectIdentity
criticalThreeVoltsStandby = _CriticalThreeVoltsStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 10)
)
_CriticalFiveVolts_ObjectIdentity = ObjectIdentity
criticalFiveVolts = _CriticalFiveVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 11)
)
_CriticalFiveVoltsFault_ObjectIdentity = ObjectIdentity
criticalFiveVoltsFault = _CriticalFiveVoltsFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 12)
)
_CriticalFiveVoltsPci_ObjectIdentity = ObjectIdentity
criticalFiveVoltsPci = _CriticalFiveVoltsPci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 13)
)
_CriticalFiveVoltsStandby_ObjectIdentity = ObjectIdentity
criticalFiveVoltsStandby = _CriticalFiveVoltsStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 14)
)
_CriticalNTwelveVolts_ObjectIdentity = ObjectIdentity
criticalNTwelveVolts = _CriticalNTwelveVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 15)
)
_Deployment_ObjectIdentity = ObjectIdentity
deployment = _Deployment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 4)
)
_Environmental_ObjectIdentity = ObjectIdentity
environmental = _Environmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 5)
)
_NonCritical_ObjectIdentity = ObjectIdentity
nonCritical = _NonCritical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6)
)
_NonCriticalFan_ObjectIdentity = ObjectIdentity
nonCriticalFan = _NonCriticalFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 1)
)
_NonCriticalTemperature_ObjectIdentity = ObjectIdentity
nonCriticalTemperature = _NonCriticalTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 4)
)
_NonCriticalVoltage_ObjectIdentity = ObjectIdentity
nonCriticalVoltage = _NonCriticalVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5)
)
_NonCriticalTwelveVolts_ObjectIdentity = ObjectIdentity
nonCriticalTwelveVolts = _NonCriticalTwelveVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 1)
)
_NonCriticalOneVolt_ObjectIdentity = ObjectIdentity
nonCriticalOneVolt = _NonCriticalOneVolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 2)
)
_NonCriticalTwoVolts_ObjectIdentity = ObjectIdentity
nonCriticalTwoVolts = _NonCriticalTwoVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 3)
)
_NonCriticalThreeVolts_ObjectIdentity = ObjectIdentity
nonCriticalThreeVolts = _NonCriticalThreeVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 4)
)
_NonCriticalThreeVoltsPci_ObjectIdentity = ObjectIdentity
nonCriticalThreeVoltsPci = _NonCriticalThreeVoltsPci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 5)
)
_NonCriticalThreeVoltsStandby_ObjectIdentity = ObjectIdentity
nonCriticalThreeVoltsStandby = _NonCriticalThreeVoltsStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 6)
)
_NonCriticalFiveVolts_ObjectIdentity = ObjectIdentity
nonCriticalFiveVolts = _NonCriticalFiveVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 7)
)
_NonCriticalFiveVoltsPci_ObjectIdentity = ObjectIdentity
nonCriticalFiveVoltsPci = _NonCriticalFiveVoltsPci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 8)
)
_NonCriticalFiveVoltsStandby_ObjectIdentity = ObjectIdentity
nonCriticalFiveVoltsStandby = _NonCriticalFiveVoltsStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 9)
)
_NonCriticalNTwelveVolts_ObjectIdentity = ObjectIdentity
nonCriticalNTwelveVolts = _NonCriticalNTwelveVolts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 10)
)
_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7)
)
_ScalableNode_ObjectIdentity = ObjectIdentity
scalableNode = _ScalableNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1)
)
_ScalableNodeMode_ObjectIdentity = ObjectIdentity
scalableNodeMode = _ScalableNodeMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 1)
)
_ScalableNodeStandalone_ObjectIdentity = ObjectIdentity
scalableNodeStandalone = _ScalableNodeStandalone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 2)
)
_StandaloneMode_ObjectIdentity = ObjectIdentity
standaloneMode = _StandaloneMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 2, 1)
)
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 2, 1, 2)
)
_ScalablePartition_ObjectIdentity = ObjectIdentity
scalablePartition = _ScalablePartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2)
)
_ScalablePartitionState_ObjectIdentity = ObjectIdentity
scalablePartitionState = _ScalablePartitionState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8)
)
_FuelGauge_ObjectIdentity = ObjectIdentity
fuelGauge = _FuelGauge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 2)
)
_SystemPfa_ObjectIdentity = ObjectIdentity
systemPfa = _SystemPfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 5)
)
_PetFamily_ObjectIdentity = ObjectIdentity
petFamily = _PetFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5)
)
_PetFamilyEventDetails_ObjectIdentity = ObjectIdentity
petFamilyEventDetails = _PetFamilyEventDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1)
)
_AllVariableBindings_Type = OctetString
_AllVariableBindings_Object = MibScalar
allVariableBindings = _AllVariableBindings_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 1),
    _AllVariableBindings_Type()
)
allVariableBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allVariableBindings.setStatus("current")
_Entity_Type = OctetString
_Entity_Object = MibScalar
entity = _Entity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 2),
    _Entity_Type()
)
entity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entity.setStatus("current")
_EntityInstance_Type = OctetString
_EntityInstance_Object = MibScalar
entityInstance = _EntityInstance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 3),
    _EntityInstance_Type()
)
entityInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityInstance.setStatus("current")
_PetEventData_Type = OctetString
_PetEventData_Object = MibScalar
petEventData = _PetEventData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 4),
    _PetEventData_Type()
)
petEventData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    petEventData.setStatus("current")
_PetEventSeverity_Type = OctetString
_PetEventSeverity_Object = MibScalar
petEventSeverity = _PetEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 5),
    _PetEventSeverity_Type()
)
petEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    petEventSeverity.setStatus("current")
_PetEventSourceType_Type = OctetString
_PetEventSourceType_Object = MibScalar
petEventSourceType = _PetEventSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 6),
    _PetEventSourceType_Type()
)
petEventSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    petEventSourceType.setStatus("current")
_PetEventType_Type = OctetString
_PetEventType_Object = MibScalar
petEventType = _PetEventType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 7),
    _PetEventType_Type()
)
petEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    petEventType.setStatus("current")
_Guid_Type = OctetString
_Guid_Object = MibScalar
guid = _Guid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 8),
    _Guid_Type()
)
guid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    guid.setStatus("current")
_LanguageCode_Type = OctetString
_LanguageCode_Object = MibScalar
languageCode = _LanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 9),
    _LanguageCode_Type()
)
languageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    languageCode.setStatus("current")
_LocalTimeStamp_Type = DisplayString
_LocalTimeStamp_Object = MibScalar
localTimeStamp = _LocalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 10),
    _LocalTimeStamp_Type()
)
localTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localTimeStamp.setStatus("current")
_ManufacturerId_Type = DisplayString
_ManufacturerId_Object = MibScalar
manufacturerId = _ManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 11),
    _ManufacturerId_Type()
)
manufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturerId.setStatus("current")
_OemCustomField_Type = OctetString
_OemCustomField_Object = MibScalar
oemCustomField = _OemCustomField_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 12),
    _OemCustomField_Type()
)
oemCustomField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oemCustomField.setStatus("current")
_Offset_Type = OctetString
_Offset_Object = MibScalar
offset = _Offset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 13),
    _Offset_Type()
)
offset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offset.setStatus("current")
_SensorDevice_Type = OctetString
_SensorDevice_Object = MibScalar
sensorDevice = _SensorDevice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 14),
    _SensorDevice_Type()
)
sensorDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDevice.setStatus("current")
_SensorNumber_Type = OctetString
_SensorNumber_Object = MibScalar
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 15),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("current")
_SensorType_Type = OctetString
_SensorType_Object = MibScalar
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 16),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_SequenceId_Type = Integer32
_SequenceId_Object = MibScalar
sequenceId = _SequenceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 17),
    _SequenceId_Type()
)
sequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceId.setStatus("current")
_SystemId_Type = Integer32
_SystemId_Object = MibScalar
systemId = _SystemId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 18),
    _SystemId_Type()
)
systemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemId.setStatus("current")
_TrapSourceType_Type = OctetString
_TrapSourceType_Object = MibScalar
trapSourceType = _TrapSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 19),
    _TrapSourceType_Type()
)
trapSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSourceType.setStatus("current")
_UtcOffset_Type = Integer32
_UtcOffset_Object = MibScalar
utcOffset = _UtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 1, 20),
    _UtcOffset_Type()
)
utcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utcOffset.setStatus("current")
_PetEnvironmental_ObjectIdentity = ObjectIdentity
petEnvironmental = _PetEnvironmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2)
)
_PetEnvironmentalSensor_ObjectIdentity = ObjectIdentity
petEnvironmentalSensor = _PetEnvironmentalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2, 1)
)
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 3)
)
_Bios_ObjectIdentity = ObjectIdentity
bios = _Bios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 3, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4)
)
_PetFamilySystem_ObjectIdentity = ObjectIdentity
petFamilySystem = _PetFamilySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 5)
)
_PetFamilySystemOs_ObjectIdentity = ObjectIdentity
petFamilySystemOs = _PetFamilySystemOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 5, 1)
)
_PetFamilySystemOsOperation_ObjectIdentity = ObjectIdentity
petFamilySystemOsOperation = _PetFamilySystemOsOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 5, 1, 2)
)
_StorageFamily_ObjectIdentity = ObjectIdentity
storageFamily = _StorageFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 6)
)
_ServeRaidController_ObjectIdentity = ObjectIdentity
serveRaidController = _ServeRaidController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 6, 1)
)
_PhysicalDrive_ObjectIdentity = ObjectIdentity
physicalDrive = _PhysicalDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 6, 1, 1)
)
_State_ObjectIdentity = ObjectIdentity
state = _State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 6, 1, 2)
)
_DirectorTrapsConformance_ObjectIdentity = ObjectIdentity
directorTrapsConformance = _DirectorTrapsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 100)
)
_DirectorTrapsGroups_ObjectIdentity = ObjectIdentity
directorTrapsGroups = _DirectorTrapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 100, 1)
)
_DirectorTrapsCompliances_ObjectIdentity = ObjectIdentity
directorTrapsCompliances = _DirectorTrapsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 100, 2)
)
_Description_ObjectIdentity = ObjectIdentity
description = _Description_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 202)
)
_TrapType_Type = SnmpAdminString
_TrapType_Object = MibScalar
trapType = _TrapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 202, 1),
    _TrapType_Type()
)
trapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapType.setStatus("current")
_TrapSeverity_Type = SnmpAdminString
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 202, 2),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_TrapSenderName_Type = SnmpAdminString
_TrapSenderName_Object = MibScalar
trapSenderName = _TrapSenderName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 202, 3),
    _TrapSenderName_Type()
)
trapSenderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderName.setStatus("current")
_TrapManagedObjectName_Type = SnmpAdminString
_TrapManagedObjectName_Object = MibScalar
trapManagedObjectName = _TrapManagedObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 202, 4),
    _TrapManagedObjectName_Type()
)
trapManagedObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapManagedObjectName.setStatus("current")
_TrapText_Type = SnmpAdminString
_TrapText_Object = MibScalar
trapText = _TrapText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 202, 5),
    _TrapText_Type()
)
trapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapText.setStatus("current")
_TrapCategory_Type = SnmpAdminString
_TrapCategory_Object = MibScalar
trapCategory = _TrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 202, 6),
    _TrapCategory_Type()
)
trapCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCategory.setStatus("current")
_Details_ObjectIdentity = ObjectIdentity
details = _Details_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696)
)
_Char_Type = OctetString
_Char_Object = MibScalar
char = _Char_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 1),
    _Char_Type()
)
char.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    char.setStatus("current")
_Short_Type = Integer32
_Short_Object = MibScalar
short = _Short_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 2),
    _Short_Type()
)
short.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    short.setStatus("current")
_Int_Type = Integer32
_Int_Object = MibScalar
int = _Int_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 3),
    _Int_Type()
)
int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    int.setStatus("current")
_Long_Type = DisplayString
_Long_Object = MibScalar
long = _Long_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 4),
    _Long_Type()
)
long.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    long.setStatus("current")
_Boolean_Type = TruthValue
_Boolean_Object = MibScalar
boolean = _Boolean_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 5),
    _Boolean_Type()
)
boolean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boolean.setStatus("current")
_Float_Type = DisplayString
_Float_Object = MibScalar
float = _Float_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 6),
    _Float_Type()
)
float.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    float.setStatus("current")
_Double_Type = DisplayString
_Double_Object = MibScalar
double = _Double_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 7),
    _Double_Type()
)
double.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    double.setStatus("current")
_Octet_Type = DisplayString
_Octet_Object = MibScalar
octet = _Octet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 8),
    _Octet_Type()
)
octet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octet.setStatus("current")
_String_Type = SnmpAdminString
_String_Object = MibScalar
string = _String_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 9),
    _String_Type()
)
string.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    string.setStatus("current")
_DateTime_Type = DisplayString
_DateTime_Object = MibScalar
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 10),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_UniChar_Type = DisplayString
_UniChar_Object = MibScalar
uniChar = _UniChar_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 11),
    _UniChar_Type()
)
uniChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniChar.setStatus("current")
_Byte_Type = DisplayString
_Byte_Object = MibScalar
byte = _Byte_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 9696, 12),
    _Byte_Type()
)
byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byte.setStatus("current")

# Managed Objects groups

directorTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 100, 1, 1)
)
directorTrapsGroup.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "char"),
        ("IBM-Director-Alert-MIB", "short"),
        ("IBM-Director-Alert-MIB", "int"),
        ("IBM-Director-Alert-MIB", "long"),
        ("IBM-Director-Alert-MIB", "boolean"),
        ("IBM-Director-Alert-MIB", "float"),
        ("IBM-Director-Alert-MIB", "octet"),
        ("IBM-Director-Alert-MIB", "double"),
        ("IBM-Director-Alert-MIB", "string"),
        ("IBM-Director-Alert-MIB", "dateTime"),
        ("IBM-Director-Alert-MIB", "uniChar"),
        ("IBM-Director-Alert-MIB", "byte"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"),
        ("IBM-Director-Alert-MIB", "userName"),
        ("IBM-Director-Alert-MIB", "userDescription"),
        ("IBM-Director-Alert-MIB", "userLocale"),
        ("IBM-Director-Alert-MIB", "category"),
        ("IBM-Director-Alert-MIB", "categoryString"),
        ("IBM-Director-Alert-MIB", "computerName"),
        ("IBM-Director-Alert-MIB", "data"),
        ("IBM-Director-Alert-MIB", "eventLogCode"),
        ("IBM-Director-Alert-MIB", "eventLogIdentifier"),
        ("IBM-Director-Alert-MIB", "eventLogType"),
        ("IBM-Director-Alert-MIB", "insertionStrings"),
        ("IBM-Director-Alert-MIB", "logFile"),
        ("IBM-Director-Alert-MIB", "message"),
        ("IBM-Director-Alert-MIB", "recordNumber"),
        ("IBM-Director-Alert-MIB", "sourceName"),
        ("IBM-Director-Alert-MIB", "type"),
        ("IBM-Director-Alert-MIB", "user"),
        ("IBM-Director-Alert-MIB", "acceptPause"),
        ("IBM-Director-Alert-MIB", "acceptStop"),
        ("IBM-Director-Alert-MIB", "caption"),
        ("IBM-Director-Alert-MIB", "checkPoint"),
        ("IBM-Director-Alert-MIB", "creationClassName"),
        ("IBM-Director-Alert-MIB", "serviceDescription"),
        ("IBM-Director-Alert-MIB", "desktopInteract"),
        ("IBM-Director-Alert-MIB", "displayName"),
        ("IBM-Director-Alert-MIB", "errorControl"),
        ("IBM-Director-Alert-MIB", "exitCode"),
        ("IBM-Director-Alert-MIB", "name"),
        ("IBM-Director-Alert-MIB", "pathName"),
        ("IBM-Director-Alert-MIB", "processId"),
        ("IBM-Director-Alert-MIB", "serviceSpecificExitCode"),
        ("IBM-Director-Alert-MIB", "serviceType"),
        ("IBM-Director-Alert-MIB", "startMode"),
        ("IBM-Director-Alert-MIB", "startName"),
        ("IBM-Director-Alert-MIB", "started"),
        ("IBM-Director-Alert-MIB", "serviceState"),
        ("IBM-Director-Alert-MIB", "status"),
        ("IBM-Director-Alert-MIB", "systemCreationClassName"),
        ("IBM-Director-Alert-MIB", "systemName"),
        ("IBM-Director-Alert-MIB", "tagId"),
        ("IBM-Director-Alert-MIB", "waitHint"),
        ("IBM-Director-Alert-MIB", "hive"),
        ("IBM-Director-Alert-MIB", "rootPath"),
        ("IBM-Director-Alert-MIB", "securityDescriptor"),
        ("IBM-Director-Alert-MIB", "timeCreated"),
        ("IBM-Director-Alert-MIB", "alertCode"),
        ("IBM-Director-Alert-MIB", "busId"),
        ("IBM-Director-Alert-MIB", "componentId"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "ipAddress1"),
        ("IBM-Director-Alert-MIB", "ipAddress2"),
        ("IBM-Director-Alert-MIB", "issue"),
        ("IBM-Director-Alert-MIB", "powerDomain"),
        ("IBM-Director-Alert-MIB", "reason"),
        ("IBM-Director-Alert-MIB", "scsiId"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "newState"),
        ("IBM-Director-Alert-MIB", "temperatureSensor"),
        ("IBM-Director-Alert-MIB", "threshold"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"),
        ("IBM-Director-Alert-MIB", "voltageSensor"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    directorTrapsGroup.setStatus("current")


# Notification objects

online = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 1, 1)
)
online.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    online.setStatus(
        "current"
    )

offline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 1, 2)
)
offline.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    offline.setStatus(
        "current"
    )

create = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 1, 3)
)
create.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    create.setStatus(
        "current"
    )

change = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 1, 4)
)
change.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    change.setStatus(
        "current"
    )

destroy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 1, 5)
)
destroy.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    destroy.setStatus(
        "current"
    )

processMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 1)
)
processMonitor.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    processMonitor.setStatus(
        "current"
    )

cpuUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 2, 1)
)
cpuUtilization.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    cpuUtilization.setStatus(
        "current"
    )

processCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 2, 2)
)
processCount.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    processCount.setStatus(
        "current"
    )

driveSpaceUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 3, 1)
)
driveSpaceUsed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    driveSpaceUsed.setStatus(
        "current"
    )

driveSpaceUsedPercent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 3, 2)
)
driveSpaceUsedPercent.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    driveSpaceUsedPercent.setStatus(
        "current"
    )

driveSpaceRemaining = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 3, 3)
)
driveSpaceRemaining.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    driveSpaceRemaining.setStatus(
        "current"
    )

driveWorkload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 3, 4)
)
driveWorkload.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    driveWorkload.setStatus(
        "current"
    )

lockedMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 4, 1)
)
lockedMemory.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    lockedMemory.setStatus(
        "current"
    )

memoryUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 4, 2)
)
memoryUsage.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    memoryUsage.setStatus(
        "current"
    )

totalPrivilegedTimePercent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 6, 1)
)
totalPrivilegedTimePercent.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    totalPrivilegedTimePercent.setStatus(
        "current"
    )

fileReadOperationsPerSec = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 6, 2)
)
fileReadOperationsPerSec.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    fileReadOperationsPerSec.setStatus(
        "current"
    )

udpPacketsSentPerSec = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 7, 1)
)
udpPacketsSentPerSec.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    udpPacketsSentPerSec.setStatus(
        "current"
    )

udpPacketsReceivedPerSec = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 7, 2)
)
udpPacketsReceivedPerSec.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    udpPacketsReceivedPerSec.setStatus(
        "current"
    )

ipPacketsSentPerSec = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 7, 3)
)
ipPacketsSentPerSec.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    ipPacketsSentPerSec.setStatus(
        "current"
    )

ipPacketsReceivedPerSec = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 7, 4)
)
ipPacketsReceivedPerSec.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    ipPacketsReceivedPerSec.setStatus(
        "current"
    )

ipErrorPacketsReceivedPerSec = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 7, 5)
)
ipErrorPacketsReceivedPerSec.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    ipErrorPacketsReceivedPerSec.setStatus(
        "current"
    )

tcpConnections = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 2, 7, 6)
)
tcpConnections.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "actualValue"),
        ("IBM-Director-Alert-MIB", "duration"),
        ("IBM-Director-Alert-MIB", "monitorResource"),
        ("IBM-Director-Alert-MIB", "thresholdName"),
        ("IBM-Director-Alert-MIB", "thresholdValue"))
)
if mibBuilder.loadTexts:
    tcpConnections.setStatus(
        "current"
    )

action = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 3, 1)
)
action.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    action.setStatus(
        "current"
    )

badPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 1)
)
badPassword.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    badPassword.setStatus(
        "current"
    )

badUserID = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 2)
)
badUserID.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    badUserID.setStatus(
        "current"
    )

disabledUserID = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 3)
)
disabledUserID.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    disabledUserID.setStatus(
        "current"
    )

downlevelConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 4)
)
downlevelConsole.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    downlevelConsole.setStatus(
        "current"
    )

expiredPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 5)
)
expiredPassword.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    expiredPassword.setStatus(
        "current"
    )

tooManyActiveIDs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 6)
)
tooManyActiveIDs.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    tooManyActiveIDs.setStatus(
        "current"
    )

tooManyActiveLogons = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 7)
)
tooManyActiveLogons.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    tooManyActiveLogons.setStatus(
        "current"
    )

uplevelConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 2, 8)
)
uplevelConsole.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"))
)
if mibBuilder.loadTexts:
    uplevelConsole.setStatus(
        "current"
    )

logoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 3)
)
logoff.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"),
        ("IBM-Director-Alert-MIB", "userName"),
        ("IBM-Director-Alert-MIB", "userDescription"),
        ("IBM-Director-Alert-MIB", "userLocale"))
)
if mibBuilder.loadTexts:
    logoff.setStatus(
        "current"
    )

logon = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 1, 4, 4)
)
logon.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "userID"),
        ("IBM-Director-Alert-MIB", "address"),
        ("IBM-Director-Alert-MIB", "userName"),
        ("IBM-Director-Alert-MIB", "userDescription"),
        ("IBM-Director-Alert-MIB", "userLocale"))
)
if mibBuilder.loadTexts:
    logon.setStatus(
        "current"
    )

generalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 2)
)
generalEvent.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    generalEvent.setStatus(
        "current"
    )

applicationLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 2)
)
applicationLog.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "category"),
        ("IBM-Director-Alert-MIB", "categoryString"),
        ("IBM-Director-Alert-MIB", "computerName"),
        ("IBM-Director-Alert-MIB", "data"),
        ("IBM-Director-Alert-MIB", "eventLogCode"),
        ("IBM-Director-Alert-MIB", "eventLogIdentifier"),
        ("IBM-Director-Alert-MIB", "eventLogType"),
        ("IBM-Director-Alert-MIB", "insertionStrings"),
        ("IBM-Director-Alert-MIB", "logFile"),
        ("IBM-Director-Alert-MIB", "message"),
        ("IBM-Director-Alert-MIB", "recordNumber"),
        ("IBM-Director-Alert-MIB", "sourceName"),
        ("IBM-Director-Alert-MIB", "type"),
        ("IBM-Director-Alert-MIB", "user"))
)
if mibBuilder.loadTexts:
    applicationLog.setStatus(
        "current"
    )

securityLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 3)
)
securityLog.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "category"),
        ("IBM-Director-Alert-MIB", "categoryString"),
        ("IBM-Director-Alert-MIB", "computerName"),
        ("IBM-Director-Alert-MIB", "data"),
        ("IBM-Director-Alert-MIB", "eventLogCode"),
        ("IBM-Director-Alert-MIB", "eventLogIdentifier"),
        ("IBM-Director-Alert-MIB", "eventLogType"),
        ("IBM-Director-Alert-MIB", "insertionStrings"),
        ("IBM-Director-Alert-MIB", "logFile"),
        ("IBM-Director-Alert-MIB", "message"),
        ("IBM-Director-Alert-MIB", "recordNumber"),
        ("IBM-Director-Alert-MIB", "sourceName"),
        ("IBM-Director-Alert-MIB", "type"),
        ("IBM-Director-Alert-MIB", "user"))
)
if mibBuilder.loadTexts:
    securityLog.setStatus(
        "current"
    )

systemLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 1, 4)
)
systemLog.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    systemLog.setStatus(
        "current"
    )

startedService = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 2)
)
startedService.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "acceptPause"),
        ("IBM-Director-Alert-MIB", "acceptStop"),
        ("IBM-Director-Alert-MIB", "caption"),
        ("IBM-Director-Alert-MIB", "checkPoint"),
        ("IBM-Director-Alert-MIB", "creationClassName"),
        ("IBM-Director-Alert-MIB", "serviceDescription"),
        ("IBM-Director-Alert-MIB", "desktopInteract"),
        ("IBM-Director-Alert-MIB", "displayName"),
        ("IBM-Director-Alert-MIB", "errorControl"),
        ("IBM-Director-Alert-MIB", "exitCode"),
        ("IBM-Director-Alert-MIB", "name"),
        ("IBM-Director-Alert-MIB", "pathName"),
        ("IBM-Director-Alert-MIB", "processId"),
        ("IBM-Director-Alert-MIB", "serviceSpecificExitCode"),
        ("IBM-Director-Alert-MIB", "serviceType"),
        ("IBM-Director-Alert-MIB", "startMode"),
        ("IBM-Director-Alert-MIB", "startName"),
        ("IBM-Director-Alert-MIB", "started"),
        ("IBM-Director-Alert-MIB", "serviceState"),
        ("IBM-Director-Alert-MIB", "status"),
        ("IBM-Director-Alert-MIB", "systemCreationClassName"),
        ("IBM-Director-Alert-MIB", "systemName"),
        ("IBM-Director-Alert-MIB", "tagId"),
        ("IBM-Director-Alert-MIB", "waitHint"))
)
if mibBuilder.loadTexts:
    startedService.setStatus(
        "current"
    )

stoppedService = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 2, 3)
)
stoppedService.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "acceptPause"),
        ("IBM-Director-Alert-MIB", "acceptStop"),
        ("IBM-Director-Alert-MIB", "caption"),
        ("IBM-Director-Alert-MIB", "checkPoint"),
        ("IBM-Director-Alert-MIB", "creationClassName"),
        ("IBM-Director-Alert-MIB", "serviceDescription"),
        ("IBM-Director-Alert-MIB", "desktopInteract"),
        ("IBM-Director-Alert-MIB", "displayName"),
        ("IBM-Director-Alert-MIB", "errorControl"),
        ("IBM-Director-Alert-MIB", "exitCode"),
        ("IBM-Director-Alert-MIB", "name"),
        ("IBM-Director-Alert-MIB", "pathName"),
        ("IBM-Director-Alert-MIB", "processId"),
        ("IBM-Director-Alert-MIB", "serviceSpecificExitCode"),
        ("IBM-Director-Alert-MIB", "serviceType"),
        ("IBM-Director-Alert-MIB", "startMode"),
        ("IBM-Director-Alert-MIB", "startName"),
        ("IBM-Director-Alert-MIB", "started"),
        ("IBM-Director-Alert-MIB", "serviceState"),
        ("IBM-Director-Alert-MIB", "status"),
        ("IBM-Director-Alert-MIB", "systemCreationClassName"),
        ("IBM-Director-Alert-MIB", "systemName"),
        ("IBM-Director-Alert-MIB", "tagId"),
        ("IBM-Director-Alert-MIB", "waitHint"))
)
if mibBuilder.loadTexts:
    stoppedService.setStatus(
        "current"
    )

softwareTreeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3, 2)
)
softwareTreeChanged.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "hive"),
        ("IBM-Director-Alert-MIB", "rootPath"),
        ("IBM-Director-Alert-MIB", "securityDescriptor"),
        ("IBM-Director-Alert-MIB", "timeCreated"))
)
if mibBuilder.loadTexts:
    softwareTreeChanged.setStatus(
        "current"
    )

systemTreeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 3, 3, 3)
)
systemTreeChanged.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "hive"),
        ("IBM-Director-Alert-MIB", "rootPath"),
        ("IBM-Director-Alert-MIB", "securityDescriptor"),
        ("IBM-Director-Alert-MIB", "timeCreated"))
)
if mibBuilder.loadTexts:
    systemTreeChanged.setStatus(
        "current"
    )

codEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 1, 1, 1)
)
codEnabled.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    codEnabled.setStatus(
        "current"
    )

bladeServerCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 1, 2)
)
bladeServerCommunication.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    bladeServerCommunication.setStatus(
        "current"
    )

bladeServerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 1, 3)
)
bladeServerInserted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    bladeServerInserted.setStatus(
        "current"
    )

bladeServerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 1, 4)
)
bladeServerRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    bladeServerRemoved.setStatus(
        "current"
    )

busCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 2, 1)
)
busCommunication.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "busId"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    busCommunication.setStatus(
        "current"
    )

chassisConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 3, 1)
)
chassisConfiguration.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "componentId"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "issue"),
        ("IBM-Director-Alert-MIB", "powerDomain"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    chassisConfiguration.setStatus(
        "current"
    )

chassisFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 3, 2)
)
chassisFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "issue"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    chassisFailed.setStatus(
        "current"
    )

dasdFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 4, 1)
)
dasdFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "scsiId"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    dasdFailed.setStatus(
        "current"
    )

dasdInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 4, 2)
)
dasdInserted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "scsiId"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    dasdInserted.setStatus(
        "current"
    )

dasdRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 4, 3)
)
dasdRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "scsiId"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    dasdRemoved.setStatus(
        "current"
    )

memoryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 5, 1)
)
memoryFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    memoryFailed.setStatus(
        "current"
    )

componentFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 6, 1)
)
componentFanFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    componentFanFailed.setStatus(
        "current"
    )

componentFanInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 6, 2)
)
componentFanInserted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    componentFanInserted.setStatus(
        "current"
    )

componentFanPfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 6, 3)
)
componentFanPfa.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    componentFanPfa.setStatus(
        "current"
    )

componentFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 6, 4)
)
componentFanRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    componentFanRemoved.setStatus(
        "current"
    )

hardwareCrashDumpAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 7, 1, 1)
)
hardwareCrashDumpAborted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    hardwareCrashDumpAborted.setStatus(
        "current"
    )

hardwareCrashDumpCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 7, 1, 2)
)
hardwareCrashDumpCompleted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    hardwareCrashDumpCompleted.setStatus(
        "current"
    )

hardwareCrashDumpInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 7, 1, 3)
)
hardwareCrashDumpInitiated.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    hardwareCrashDumpInitiated.setStatus(
        "current"
    )

ioModuleConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 1)
)
ioModuleConfiguration.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "ipAddress1"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModuleConfiguration.setStatus(
        "current"
    )

ioModuleFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 2)
)
ioModuleFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModuleFailed.setStatus(
        "current"
    )

ioModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 3)
)
ioModuleInserted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModuleInserted.setStatus(
        "current"
    )

ioModulePost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 4)
)
ioModulePost.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModulePost.setStatus(
        "current"
    )

ioModulePowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 5, 1)
)
ioModulePowerOn.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModulePowerOn.setStatus(
        "current"
    )

ioModulePowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 5, 2)
)
ioModulePowerOff.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModulePowerOff.setStatus(
        "current"
    )

ioModuleRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 6)
)
ioModuleRedundancy.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModuleRedundancy.setStatus(
        "current"
    )

ioModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 8, 7)
)
ioModuleRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    ioModuleRemoved.setStatus(
        "current"
    )

kvmOwner = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 9, 1)
)
kvmOwner.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    kvmOwner.setStatus(
        "current"
    )

osImageCrashDumpAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 10, 1, 1)
)
osImageCrashDumpAborted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    osImageCrashDumpAborted.setStatus(
        "current"
    )

osImageCrashDumpCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 10, 1, 2)
)
osImageCrashDumpCompleted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    osImageCrashDumpCompleted.setStatus(
        "current"
    )

osImageCrashDumpInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 10, 1, 3)
)
osImageCrashDumpInitiated.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    osImageCrashDumpInitiated.setStatus(
        "current"
    )

componentPfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 11)
)
componentPfa.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    componentPfa.setStatus(
        "current"
    )

powerSubsystemLowFuel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 12, 1)
)
powerSubsystemLowFuel.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    powerSubsystemLowFuel.setStatus(
        "current"
    )

powerSubsystemOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 12, 2)
)
powerSubsystemOverCurrent.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    powerSubsystemOverCurrent.setStatus(
        "current"
    )

powerSubsystemOverPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 12, 3)
)
powerSubsystemOverPower.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    powerSubsystemOverPower.setStatus(
        "current"
    )

powerSubsystemRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 12, 4)
)
powerSubsystemRedundancy.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    powerSubsystemRedundancy.setStatus(
        "current"
    )

powerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 13, 1)
)
powerSupplyFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "reason"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    powerSupplyFailed.setStatus(
        "current"
    )

powerSupplyInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 13, 2)
)
powerSupplyInserted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    powerSupplyInserted.setStatus(
        "current"
    )

powerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 13, 3)
)
powerSupplyRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    powerSupplyRemoved.setStatus(
        "current"
    )

serverPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 14, 1, 1)
)
serverPowerOff.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serverPowerOff.setStatus(
        "current"
    )

serverPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 14, 1, 2)
)
serverPowerOn.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serverPowerOn.setStatus(
        "current"
    )

serverPowerState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 14, 2)
)
serverPowerState.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "newState"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serverPowerState.setStatus(
        "current"
    )

serviceProcessorActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 1)
)
serviceProcessorActive.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    serviceProcessorActive.setStatus(
        "current"
    )

serviceProcessorConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 2)
)
serviceProcessorConfiguration.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serviceProcessorConfiguration.setStatus(
        "current"
    )

serviceProcessorInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 3)
)
serviceProcessorInserted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    serviceProcessorInserted.setStatus(
        "current"
    )

serviceProcessorLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 4)
)
serviceProcessorLog.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    serviceProcessorLog.setStatus(
        "current"
    )

serviceProcessorNetworkStack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 5)
)
serviceProcessorNetworkStack.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "ipAddress1"),
        ("IBM-Director-Alert-MIB", "ipAddress2"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serviceProcessorNetworkStack.setStatus(
        "current"
    )

serviceProcessorRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 6)
)
serviceProcessorRedundancy.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serviceProcessorRedundancy.setStatus(
        "current"
    )

serviceProcessorRemoteLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 7)
)
serviceProcessorRemoteLogin.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serviceProcessorRemoteLogin.setStatus(
        "current"
    )

serviceProcessorRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 8)
)
serviceProcessorRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    serviceProcessorRemoved.setStatus(
        "current"
    )

serviceProcessorRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 9)
)
serviceProcessorRestart.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serviceProcessorRestart.setStatus(
        "current"
    )

serviceProcessorTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 15, 10)
)
serviceProcessorTest.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    serviceProcessorTest.setStatus(
        "current"
    )

smpExpansionModuleDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 16, 1)
)
smpExpansionModuleDisabled.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    smpExpansionModuleDisabled.setStatus(
        "current"
    )

usbInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 17, 1)
)
usbInserted.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    usbInserted.setStatus(
        "current"
    )

usbOwner = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 17, 2)
)
usbOwner.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    usbOwner.setStatus(
        "current"
    )

usbRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 17, 3)
)
usbRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    usbRemoved.setStatus(
        "current"
    )

vrmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 2, 18, 1)
)
vrmFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    vrmFailed.setStatus(
        "current"
    )

hardDiskDrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 1)
)
hardDiskDrive.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    hardDiskDrive.setStatus(
        "current"
    )

multipleFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 2)
)
multipleFanFailure.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    multipleFanFailure.setStatus(
        "current"
    )

powerFailureEpow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 3, 1)
)
powerFailureEpow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "unitNumber"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    powerFailureEpow.setStatus(
        "current"
    )

powerFailureFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 3, 2)
)
powerFailureFailed.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "unitNumber"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    powerFailureFailed.setStatus(
        "current"
    )

powerFailureRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 3, 3)
)
powerFailureRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "unitNumber"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    powerFailureRemoved.setStatus(
        "current"
    )

criticalTamper = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 4)
)
criticalTamper.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTamper.setStatus(
        "current"
    )

criticalTemperatureAmbient = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 5, 1)
)
criticalTemperatureAmbient.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTemperatureAmbient.setStatus(
        "current"
    )

criticalTemperaturePci = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 5, 2)
)
criticalTemperaturePci.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTemperaturePci.setStatus(
        "current"
    )

criticalTemperaturePlanar = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 5, 3)
)
criticalTemperaturePlanar.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTemperaturePlanar.setStatus(
        "current"
    )

criticalTwelveVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 1, 1)
)
criticalTwelveVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwelveVoltsHigh.setStatus(
        "current"
    )

criticalTwelveVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 1, 2)
)
criticalTwelveVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwelveVoltsLow.setStatus(
        "current"
    )

criticalTwelveVoltsFaultA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 2)
)
criticalTwelveVoltsFaultA.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwelveVoltsFaultA.setStatus(
        "current"
    )

criticalTwelveVoltsFaultB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 3)
)
criticalTwelveVoltsFaultB.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwelveVoltsFaultB.setStatus(
        "current"
    )

criticalTwelveVoltsFaultC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 4)
)
criticalTwelveVoltsFaultC.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwelveVoltsFaultC.setStatus(
        "current"
    )

criticalTwelveVoltsFaultD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 5)
)
criticalTwelveVoltsFaultD.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwelveVoltsFaultD.setStatus(
        "current"
    )

criticalOneVoltHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 6, 1)
)
criticalOneVoltHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalOneVoltHigh.setStatus(
        "current"
    )

criticalOneVoltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 6, 2)
)
criticalOneVoltLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalOneVoltLow.setStatus(
        "current"
    )

criticalTwoVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 7, 1)
)
criticalTwoVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwoVoltsHigh.setStatus(
        "current"
    )

criticalTwoVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 7, 2)
)
criticalTwoVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalTwoVoltsLow.setStatus(
        "current"
    )

criticalThreeVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 8, 1)
)
criticalThreeVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalThreeVoltsHigh.setStatus(
        "current"
    )

criticalThreeVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 8, 2)
)
criticalThreeVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalThreeVoltsLow.setStatus(
        "current"
    )

criticalThreeVoltsPciHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 9, 1)
)
criticalThreeVoltsPciHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalThreeVoltsPciHigh.setStatus(
        "current"
    )

criticalThreeVoltsPciLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 9, 2)
)
criticalThreeVoltsPciLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalThreeVoltsPciLow.setStatus(
        "current"
    )

criticalThreeVoltsStandbyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 10, 1)
)
criticalThreeVoltsStandbyHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalThreeVoltsStandbyHigh.setStatus(
        "current"
    )

criticalThreeVoltsStandbyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 10, 2)
)
criticalThreeVoltsStandbyLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalThreeVoltsStandbyLow.setStatus(
        "current"
    )

criticalFiveVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 11, 1)
)
criticalFiveVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsHigh.setStatus(
        "current"
    )

criticalFiveVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 11, 2)
)
criticalFiveVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsLow.setStatus(
        "current"
    )

criticalFiveVoltsFaultHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 12, 1)
)
criticalFiveVoltsFaultHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsFaultHigh.setStatus(
        "current"
    )

criticalFiveVoltsFaultLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 12, 2)
)
criticalFiveVoltsFaultLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsFaultLow.setStatus(
        "current"
    )

criticalFiveVoltsPciHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 13, 1)
)
criticalFiveVoltsPciHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsPciHigh.setStatus(
        "current"
    )

criticalFiveVoltsPciLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 13, 2)
)
criticalFiveVoltsPciLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsPciLow.setStatus(
        "current"
    )

criticalFiveVoltsStandbyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 14, 1)
)
criticalFiveVoltsStandbyHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsStandbyHigh.setStatus(
        "current"
    )

criticalFiveVoltsStandbyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 14, 2)
)
criticalFiveVoltsStandbyLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalFiveVoltsStandbyLow.setStatus(
        "current"
    )

criticalNTwelveVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 15, 1)
)
criticalNTwelveVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalNTwelveVoltsHigh.setStatus(
        "current"
    )

criticalNTwelveVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 6, 15, 2)
)
criticalNTwelveVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    criticalNTwelveVoltsLow.setStatus(
        "current"
    )

voltageRegulatorModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 3, 7)
)
voltageRegulatorModuleFailure.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    voltageRegulatorModuleFailure.setStatus(
        "current"
    )

deploymentBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 4, 1)
)
deploymentBoot.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    deploymentBoot.setStatus(
        "current"
    )

deploymentLoader = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 4, 2)
)
deploymentLoader.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    deploymentLoader.setStatus(
        "current"
    )

deploymentOs = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 4, 3)
)
deploymentOs.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    deploymentOs.setStatus(
        "current"
    )

deploymentPost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 4, 4)
)
deploymentPost.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    deploymentPost.setStatus(
        "current"
    )

environmentalTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 5, 1)
)
environmentalTemperature.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "temperatureSensor"),
        ("IBM-Director-Alert-MIB", "unitNumber"))
)
if mibBuilder.loadTexts:
    environmentalTemperature.setStatus(
        "current"
    )

environmentalVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 5, 2)
)
environmentalVoltage.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "componentId"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "threshold"),
        ("IBM-Director-Alert-MIB", "voltageSensor"))
)
if mibBuilder.loadTexts:
    environmentalVoltage.setStatus(
        "current"
    )

nonCriticalFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 1, 1)
)
nonCriticalFanRemoved.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalFanRemoved.setStatus(
        "current"
    )

redundantPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 2)
)
redundantPower.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    redundantPower.setStatus(
        "current"
    )

singleFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 3)
)
singleFanFailure.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "unitNumber"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    singleFanFailure.setStatus(
        "current"
    )

nonCriticalTemperatureAmbient = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 4, 1)
)
nonCriticalTemperatureAmbient.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalTemperatureAmbient.setStatus(
        "current"
    )

nonCriticalTemperaturePci = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 4, 2)
)
nonCriticalTemperaturePci.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalTemperaturePci.setStatus(
        "current"
    )

nonCriticalTemperaturePlanar = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 4, 3)
)
nonCriticalTemperaturePlanar.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalTemperaturePlanar.setStatus(
        "current"
    )

nonCriticalTwelveVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 1, 1)
)
nonCriticalTwelveVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalTwelveVoltsHigh.setStatus(
        "current"
    )

nonCriticalTwelveVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 1, 2)
)
nonCriticalTwelveVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalTwelveVoltsLow.setStatus(
        "current"
    )

nonCriticalOneVoltHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 2, 1)
)
nonCriticalOneVoltHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalOneVoltHigh.setStatus(
        "current"
    )

nonCriticalOneVoltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 2, 2)
)
nonCriticalOneVoltLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalOneVoltLow.setStatus(
        "current"
    )

nonCriticalTwoVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 3, 1)
)
nonCriticalTwoVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalTwoVoltsHigh.setStatus(
        "current"
    )

nonCriticalTwoVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 3, 2)
)
nonCriticalTwoVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalTwoVoltsLow.setStatus(
        "current"
    )

nonCriticalThreeVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 4, 1)
)
nonCriticalThreeVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalThreeVoltsHigh.setStatus(
        "current"
    )

nonCriticalThreeVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 4, 2)
)
nonCriticalThreeVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalThreeVoltsLow.setStatus(
        "current"
    )

nonCriticalThreeVoltsPciHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 5, 1)
)
nonCriticalThreeVoltsPciHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalThreeVoltsPciHigh.setStatus(
        "current"
    )

nonCriticalThreeVoltsPciLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 5, 2)
)
nonCriticalThreeVoltsPciLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalThreeVoltsPciLow.setStatus(
        "current"
    )

nonCriticalThreeVoltsStandbyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 6, 1)
)
nonCriticalThreeVoltsStandbyHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalThreeVoltsStandbyHigh.setStatus(
        "current"
    )

nonCriticalThreeVoltsStandbyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 6, 2)
)
nonCriticalThreeVoltsStandbyLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalThreeVoltsStandbyLow.setStatus(
        "current"
    )

nonCriticalFiveVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 7, 1)
)
nonCriticalFiveVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalFiveVoltsHigh.setStatus(
        "current"
    )

nonCriticalFiveVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 7, 2)
)
nonCriticalFiveVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalFiveVoltsLow.setStatus(
        "current"
    )

nonCriticalFiveVoltsPciHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 8, 1)
)
nonCriticalFiveVoltsPciHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalFiveVoltsPciHigh.setStatus(
        "current"
    )

nonCriticalFiveVoltsPciLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 8, 2)
)
nonCriticalFiveVoltsPciLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalFiveVoltsPciLow.setStatus(
        "current"
    )

nonCriticalFiveVoltsStandbyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 9, 1)
)
nonCriticalFiveVoltsStandbyHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalFiveVoltsStandbyHigh.setStatus(
        "current"
    )

nonCriticalFiveVoltsStandbyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 9, 2)
)
nonCriticalFiveVoltsStandbyLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalFiveVoltsStandbyLow.setStatus(
        "current"
    )

nonCriticalNTwelveVoltsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 10, 1)
)
nonCriticalNTwelveVoltsHigh.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalNTwelveVoltsHigh.setStatus(
        "current"
    )

nonCriticalNTwelveVoltsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 6, 5, 10, 2)
)
nonCriticalNTwelveVoltsLow.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "side"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    nonCriticalNTwelveVoltsLow.setStatus(
        "current"
    )

scalableNodeModeNullOrUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 1, 1)
)
scalableNodeModeNullOrUnknown.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalableNodeModeNullOrUnknown.setStatus(
        "current"
    )

scalableNodeModePrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 1, 2)
)
scalableNodeModePrimary.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalableNodeModePrimary.setStatus(
        "current"
    )

scalableNodeModeSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 1, 3)
)
scalableNodeModeSecondary.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalableNodeModeSecondary.setStatus(
        "current"
    )

scalableNodeModeStandalone = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 1, 4)
)
scalableNodeModeStandalone.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalableNodeModeStandalone.setStatus(
        "current"
    )

primary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 2, 1, 1)
)
primary.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    primary.setStatus(
        "current"
    )

resetPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 2, 1, 2, 1)
)
resetPrimary.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    resetPrimary.setStatus(
        "current"
    )

resetSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 2, 1, 2, 2)
)
resetSecondary.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    resetSecondary.setStatus(
        "current"
    )

secondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 1, 2, 1, 3)
)
secondary.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    secondary.setStatus(
        "current"
    )

scalablePartitionAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2, 1)
)
scalablePartitionAlert.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "alertCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalablePartitionAlert.setStatus(
        "current"
    )

scalablePartitionNullOrUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2, 2, 1)
)
scalablePartitionNullOrUnknown.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalablePartitionNullOrUnknown.setStatus(
        "current"
    )

scalablePartitionPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2, 2, 2)
)
scalablePartitionPoweredOff.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalablePartitionPoweredOff.setStatus(
        "current"
    )

scalablePartitionPoweringOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2, 2, 3)
)
scalablePartitionPoweringOn.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalablePartitionPoweringOn.setStatus(
        "current"
    )

scalablePartitionResetting = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2, 2, 4)
)
scalablePartitionResetting.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalablePartitionResetting.setStatus(
        "current"
    )

scalablePartitionShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 7, 2, 2, 5)
)
scalablePartitionShuttingDown.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    scalablePartitionShuttingDown.setStatus(
        "current"
    )

bootFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 1)
)
bootFailure.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    bootFailure.setStatus(
        "current"
    )

fuelGaugeLowFuel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 2, 1)
)
fuelGaugeLowFuel.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    fuelGaugeLowFuel.setStatus(
        "current"
    )

fuelGaugeNotRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 2, 2)
)
fuelGaugeNotRedundant.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    fuelGaugeNotRedundant.setStatus(
        "current"
    )

fuelGaugeOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 2, 3)
)
fuelGaugeOverCurrent.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    fuelGaugeOverCurrent.setStatus(
        "current"
    )

systemLoaderTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 3)
)
systemLoaderTimeout.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    systemLoaderTimeout.setStatus(
        "current"
    )

systemOsTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 4)
)
systemOsTimeout.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    systemOsTimeout.setStatus(
        "current"
    )

fanSystemPfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 5, 1)
)
fanSystemPfa.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "unitNumber"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    fanSystemPfa.setStatus(
        "current"
    )

systemPostTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 6)
)
systemPostTimeout.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    systemPostTimeout.setStatus(
        "current"
    )

systemPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 7)
)
systemPowerOff.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    systemPowerOff.setStatus(
        "current"
    )

systemPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 8)
)
systemPowerOn.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    systemPowerOn.setStatus(
        "current"
    )

systemRedundantPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 9)
)
systemRedundantPower.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    systemRedundantPower.setStatus(
        "current"
    )

systemTamper = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 8, 10)
)
systemTamper.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "universalUniqueId"))
)
if mibBuilder.loadTexts:
    systemTamper.setStatus(
        "current"
    )

unknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 4, 9)
)
unknown.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "firmwareCode"),
        ("IBM-Director-Alert-MIB", "senderUniversalUniqueId"),
        ("IBM-Director-Alert-MIB", "sourceUniversalUniqueId"))
)
if mibBuilder.loadTexts:
    unknown.setStatus(
        "current"
    )

sensorCaseIntrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2, 1, 1)
)
sensorCaseIntrusion.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    sensorCaseIntrusion.setStatus(
        "current"
    )

sensorCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2, 1, 2)
)
sensorCurrent.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    sensorCurrent.setStatus(
        "current"
    )

sensorFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2, 1, 3)
)
sensorFan.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    sensorFan.setStatus(
        "current"
    )

sensorPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2, 1, 4)
)
sensorPowerSupply.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    sensorPowerSupply.setStatus(
        "current"
    )

sensorTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2, 1, 5)
)
sensorTemperature.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    sensorTemperature.setStatus(
        "current"
    )

sensorVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 2, 1, 6)
)
sensorVoltage.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    sensorVoltage.setStatus(
        "current"
    )

progress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 3, 1, 1)
)
progress.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    progress.setStatus(
        "current"
    )

cableInterconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4, 1)
)
cableInterconnect.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    cableInterconnect.setStatus(
        "current"
    )

drivebay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4, 2)
)
drivebay.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    drivebay.setStatus(
        "current"
    )

moduleBoard = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4, 3)
)
moduleBoard.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    moduleBoard.setStatus(
        "current"
    )

monitorAsicIc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4, 4)
)
monitorAsicIc.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    monitorAsicIc.setStatus(
        "current"
    )

network = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4, 5)
)
network.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    network.setStatus(
        "current"
    )

watchdog1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4, 6)
)
watchdog1.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    watchdog1.setStatus(
        "current"
    )

watchdog2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 4, 7)
)
watchdog2.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    watchdog2.setStatus(
        "current"
    )

petFamilySystemOsBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 5, 1, 1)
)
petFamilySystemOsBoot.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    petFamilySystemOsBoot.setStatus(
        "current"
    )

heartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 5, 5, 1, 2, 1)
)
heartbeat.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"),
        ("IBM-Director-Alert-MIB", "allVariableBindings"),
        ("IBM-Director-Alert-MIB", "entity"),
        ("IBM-Director-Alert-MIB", "entityInstance"),
        ("IBM-Director-Alert-MIB", "petEventData"),
        ("IBM-Director-Alert-MIB", "petEventSeverity"),
        ("IBM-Director-Alert-MIB", "petEventSourceType"),
        ("IBM-Director-Alert-MIB", "petEventType"),
        ("IBM-Director-Alert-MIB", "guid"),
        ("IBM-Director-Alert-MIB", "languageCode"),
        ("IBM-Director-Alert-MIB", "localTimeStamp"),
        ("IBM-Director-Alert-MIB", "manufacturerId"),
        ("IBM-Director-Alert-MIB", "oemCustomField"),
        ("IBM-Director-Alert-MIB", "offset"),
        ("IBM-Director-Alert-MIB", "sensorDevice"),
        ("IBM-Director-Alert-MIB", "sensorNumber"),
        ("IBM-Director-Alert-MIB", "sensorType"),
        ("IBM-Director-Alert-MIB", "sequenceId"),
        ("IBM-Director-Alert-MIB", "systemId"),
        ("IBM-Director-Alert-MIB", "trapSourceType"),
        ("IBM-Director-Alert-MIB", "utcOffset"))
)
if mibBuilder.loadTexts:
    heartbeat.setStatus(
        "current"
    )

vendorUnsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 6, 1, 1, 1)
)
vendorUnsupported.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    vendorUnsupported.setStatus(
        "current"
    )

notFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 6, 1, 2, 1)
)
notFound.setObjects(
      *(("IBM-Director-Alert-MIB", "trapType"),
        ("IBM-Director-Alert-MIB", "trapSeverity"),
        ("IBM-Director-Alert-MIB", "trapSenderName"),
        ("IBM-Director-Alert-MIB", "trapManagedObjectName"),
        ("IBM-Director-Alert-MIB", "trapText"),
        ("IBM-Director-Alert-MIB", "trapCategory"))
)
if mibBuilder.loadTexts:
    notFound.setStatus(
        "current"
    )


# Notifications groups

directorNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 100, 1, 2)
)
directorNotificationsGroup.setObjects(
      *(("IBM-Director-Alert-MIB", "generalEvent"),
        ("IBM-Director-Alert-MIB", "online"),
        ("IBM-Director-Alert-MIB", "offline"),
        ("IBM-Director-Alert-MIB", "create"),
        ("IBM-Director-Alert-MIB", "change"),
        ("IBM-Director-Alert-MIB", "destroy"),
        ("IBM-Director-Alert-MIB", "processMonitor"),
        ("IBM-Director-Alert-MIB", "cpuUtilization"),
        ("IBM-Director-Alert-MIB", "processCount"),
        ("IBM-Director-Alert-MIB", "driveSpaceUsed"),
        ("IBM-Director-Alert-MIB", "driveSpaceUsedPercent"),
        ("IBM-Director-Alert-MIB", "driveSpaceRemaining"),
        ("IBM-Director-Alert-MIB", "driveWorkload"),
        ("IBM-Director-Alert-MIB", "lockedMemory"),
        ("IBM-Director-Alert-MIB", "memoryUsage"),
        ("IBM-Director-Alert-MIB", "totalPrivilegedTimePercent"),
        ("IBM-Director-Alert-MIB", "fileReadOperationsPerSec"),
        ("IBM-Director-Alert-MIB", "udpPacketsSentPerSec"),
        ("IBM-Director-Alert-MIB", "udpPacketsReceivedPerSec"),
        ("IBM-Director-Alert-MIB", "ipPacketsSentPerSec"),
        ("IBM-Director-Alert-MIB", "ipPacketsReceivedPerSec"),
        ("IBM-Director-Alert-MIB", "ipErrorPacketsReceivedPerSec"),
        ("IBM-Director-Alert-MIB", "tcpConnections"),
        ("IBM-Director-Alert-MIB", "action"),
        ("IBM-Director-Alert-MIB", "badPassword"),
        ("IBM-Director-Alert-MIB", "badUserID"),
        ("IBM-Director-Alert-MIB", "disabledUserID"),
        ("IBM-Director-Alert-MIB", "downlevelConsole"),
        ("IBM-Director-Alert-MIB", "expiredPassword"),
        ("IBM-Director-Alert-MIB", "tooManyActiveIDs"),
        ("IBM-Director-Alert-MIB", "tooManyActiveLogons"),
        ("IBM-Director-Alert-MIB", "uplevelConsole"),
        ("IBM-Director-Alert-MIB", "logoff"),
        ("IBM-Director-Alert-MIB", "logon"),
        ("IBM-Director-Alert-MIB", "applicationLog"),
        ("IBM-Director-Alert-MIB", "securityLog"),
        ("IBM-Director-Alert-MIB", "systemLog"),
        ("IBM-Director-Alert-MIB", "startedService"),
        ("IBM-Director-Alert-MIB", "stoppedService"),
        ("IBM-Director-Alert-MIB", "softwareTreeChanged"),
        ("IBM-Director-Alert-MIB", "systemTreeChanged"),
        ("IBM-Director-Alert-MIB", "codEnabled"),
        ("IBM-Director-Alert-MIB", "bladeServerCommunication"),
        ("IBM-Director-Alert-MIB", "bladeServerInserted"),
        ("IBM-Director-Alert-MIB", "bladeServerRemoved"),
        ("IBM-Director-Alert-MIB", "busCommunication"),
        ("IBM-Director-Alert-MIB", "chassisConfiguration"),
        ("IBM-Director-Alert-MIB", "chassisFailed"),
        ("IBM-Director-Alert-MIB", "dasdFailed"),
        ("IBM-Director-Alert-MIB", "dasdInserted"),
        ("IBM-Director-Alert-MIB", "dasdRemoved"),
        ("IBM-Director-Alert-MIB", "memoryFailed"),
        ("IBM-Director-Alert-MIB", "componentFanFailed"),
        ("IBM-Director-Alert-MIB", "componentFanInserted"),
        ("IBM-Director-Alert-MIB", "componentFanPfa"),
        ("IBM-Director-Alert-MIB", "componentFanRemoved"),
        ("IBM-Director-Alert-MIB", "hardwareCrashDumpAborted"),
        ("IBM-Director-Alert-MIB", "hardwareCrashDumpCompleted"),
        ("IBM-Director-Alert-MIB", "hardwareCrashDumpInitiated"),
        ("IBM-Director-Alert-MIB", "ioModuleConfiguration"),
        ("IBM-Director-Alert-MIB", "ioModuleFailed"),
        ("IBM-Director-Alert-MIB", "ioModuleInserted"),
        ("IBM-Director-Alert-MIB", "ioModulePost"),
        ("IBM-Director-Alert-MIB", "ioModulePowerOn"),
        ("IBM-Director-Alert-MIB", "ioModulePowerOff"),
        ("IBM-Director-Alert-MIB", "ioModuleRedundancy"),
        ("IBM-Director-Alert-MIB", "ioModuleRemoved"),
        ("IBM-Director-Alert-MIB", "kvmOwner"),
        ("IBM-Director-Alert-MIB", "osImageCrashDumpAborted"),
        ("IBM-Director-Alert-MIB", "osImageCrashDumpCompleted"),
        ("IBM-Director-Alert-MIB", "osImageCrashDumpInitiated"),
        ("IBM-Director-Alert-MIB", "componentPfa"),
        ("IBM-Director-Alert-MIB", "powerSubsystemLowFuel"),
        ("IBM-Director-Alert-MIB", "powerSubsystemOverCurrent"),
        ("IBM-Director-Alert-MIB", "powerSubsystemOverPower"),
        ("IBM-Director-Alert-MIB", "powerSubsystemRedundancy"),
        ("IBM-Director-Alert-MIB", "powerSupplyFailed"),
        ("IBM-Director-Alert-MIB", "powerSupplyInserted"),
        ("IBM-Director-Alert-MIB", "powerSupplyRemoved"),
        ("IBM-Director-Alert-MIB", "serverPowerOff"),
        ("IBM-Director-Alert-MIB", "serverPowerOn"),
        ("IBM-Director-Alert-MIB", "serverPowerState"),
        ("IBM-Director-Alert-MIB", "serviceProcessorActive"),
        ("IBM-Director-Alert-MIB", "serviceProcessorConfiguration"),
        ("IBM-Director-Alert-MIB", "serviceProcessorInserted"),
        ("IBM-Director-Alert-MIB", "serviceProcessorLog"),
        ("IBM-Director-Alert-MIB", "serviceProcessorNetworkStack"),
        ("IBM-Director-Alert-MIB", "serviceProcessorRedundancy"),
        ("IBM-Director-Alert-MIB", "serviceProcessorRemoteLogin"),
        ("IBM-Director-Alert-MIB", "serviceProcessorRemoved"),
        ("IBM-Director-Alert-MIB", "serviceProcessorRestart"),
        ("IBM-Director-Alert-MIB", "serviceProcessorTest"),
        ("IBM-Director-Alert-MIB", "smpExpansionModuleDisabled"),
        ("IBM-Director-Alert-MIB", "usbInserted"),
        ("IBM-Director-Alert-MIB", "usbOwner"),
        ("IBM-Director-Alert-MIB", "usbRemoved"),
        ("IBM-Director-Alert-MIB", "vrmFailed"),
        ("IBM-Director-Alert-MIB", "hardDiskDrive"),
        ("IBM-Director-Alert-MIB", "multipleFanFailure"),
        ("IBM-Director-Alert-MIB", "powerFailureEpow"),
        ("IBM-Director-Alert-MIB", "powerFailureFailed"),
        ("IBM-Director-Alert-MIB", "powerFailureRemoved"),
        ("IBM-Director-Alert-MIB", "criticalTamper"),
        ("IBM-Director-Alert-MIB", "criticalTemperatureAmbient"),
        ("IBM-Director-Alert-MIB", "criticalTemperaturePci"),
        ("IBM-Director-Alert-MIB", "criticalTemperaturePlanar"),
        ("IBM-Director-Alert-MIB", "criticalTwelveVoltsHigh"),
        ("IBM-Director-Alert-MIB", "criticalTwelveVoltsLow"),
        ("IBM-Director-Alert-MIB", "criticalTwelveVoltsFaultA"),
        ("IBM-Director-Alert-MIB", "criticalTwelveVoltsFaultB"),
        ("IBM-Director-Alert-MIB", "criticalTwelveVoltsFaultC"),
        ("IBM-Director-Alert-MIB", "criticalTwelveVoltsFaultD"),
        ("IBM-Director-Alert-MIB", "criticalOneVoltHigh"),
        ("IBM-Director-Alert-MIB", "criticalOneVoltLow"),
        ("IBM-Director-Alert-MIB", "criticalTwoVoltsHigh"),
        ("IBM-Director-Alert-MIB", "criticalTwoVoltsLow"),
        ("IBM-Director-Alert-MIB", "criticalThreeVoltsHigh"),
        ("IBM-Director-Alert-MIB", "criticalThreeVoltsLow"),
        ("IBM-Director-Alert-MIB", "criticalThreeVoltsPciHigh"),
        ("IBM-Director-Alert-MIB", "criticalThreeVoltsPciLow"),
        ("IBM-Director-Alert-MIB", "criticalThreeVoltsStandbyHigh"),
        ("IBM-Director-Alert-MIB", "criticalThreeVoltsStandbyLow"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsHigh"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsLow"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsFaultHigh"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsFaultLow"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsPciHigh"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsPciLow"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsStandbyHigh"),
        ("IBM-Director-Alert-MIB", "criticalFiveVoltsStandbyLow"),
        ("IBM-Director-Alert-MIB", "criticalNTwelveVoltsHigh"),
        ("IBM-Director-Alert-MIB", "criticalNTwelveVoltsLow"),
        ("IBM-Director-Alert-MIB", "voltageRegulatorModuleFailure"),
        ("IBM-Director-Alert-MIB", "deploymentBoot"),
        ("IBM-Director-Alert-MIB", "deploymentLoader"),
        ("IBM-Director-Alert-MIB", "deploymentOs"),
        ("IBM-Director-Alert-MIB", "deploymentPost"),
        ("IBM-Director-Alert-MIB", "environmentalTemperature"),
        ("IBM-Director-Alert-MIB", "environmentalVoltage"),
        ("IBM-Director-Alert-MIB", "nonCriticalFanRemoved"),
        ("IBM-Director-Alert-MIB", "redundantPower"),
        ("IBM-Director-Alert-MIB", "singleFanFailure"),
        ("IBM-Director-Alert-MIB", "nonCriticalTemperatureAmbient"),
        ("IBM-Director-Alert-MIB", "nonCriticalTemperaturePci"),
        ("IBM-Director-Alert-MIB", "nonCriticalTemperaturePlanar"),
        ("IBM-Director-Alert-MIB", "nonCriticalTwelveVoltsHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalTwelveVoltsLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalOneVoltHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalOneVoltLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalTwoVoltsHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalTwoVoltsLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalThreeVoltsHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalThreeVoltsLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalThreeVoltsPciHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalThreeVoltsPciLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalThreeVoltsStandbyHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalThreeVoltsStandbyLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalFiveVoltsHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalFiveVoltsLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalFiveVoltsPciHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalFiveVoltsPciLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalFiveVoltsStandbyHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalFiveVoltsStandbyLow"),
        ("IBM-Director-Alert-MIB", "nonCriticalNTwelveVoltsHigh"),
        ("IBM-Director-Alert-MIB", "nonCriticalNTwelveVoltsLow"),
        ("IBM-Director-Alert-MIB", "scalableNodeModeNullOrUnknown"),
        ("IBM-Director-Alert-MIB", "scalableNodeModePrimary"),
        ("IBM-Director-Alert-MIB", "scalableNodeModeSecondary"),
        ("IBM-Director-Alert-MIB", "scalableNodeModeStandalone"),
        ("IBM-Director-Alert-MIB", "primary"),
        ("IBM-Director-Alert-MIB", "resetPrimary"),
        ("IBM-Director-Alert-MIB", "resetSecondary"),
        ("IBM-Director-Alert-MIB", "secondary"),
        ("IBM-Director-Alert-MIB", "scalablePartitionAlert"),
        ("IBM-Director-Alert-MIB", "scalablePartitionNullOrUnknown"),
        ("IBM-Director-Alert-MIB", "scalablePartitionPoweredOff"),
        ("IBM-Director-Alert-MIB", "scalablePartitionPoweringOn"),
        ("IBM-Director-Alert-MIB", "scalablePartitionResetting"),
        ("IBM-Director-Alert-MIB", "scalablePartitionShuttingDown"),
        ("IBM-Director-Alert-MIB", "bootFailure"),
        ("IBM-Director-Alert-MIB", "fuelGaugeLowFuel"),
        ("IBM-Director-Alert-MIB", "fuelGaugeNotRedundant"),
        ("IBM-Director-Alert-MIB", "fuelGaugeOverCurrent"),
        ("IBM-Director-Alert-MIB", "systemLoaderTimeout"),
        ("IBM-Director-Alert-MIB", "systemOsTimeout"),
        ("IBM-Director-Alert-MIB", "fanSystemPfa"),
        ("IBM-Director-Alert-MIB", "systemPostTimeout"),
        ("IBM-Director-Alert-MIB", "systemPowerOff"),
        ("IBM-Director-Alert-MIB", "systemPowerOn"),
        ("IBM-Director-Alert-MIB", "systemRedundantPower"),
        ("IBM-Director-Alert-MIB", "systemTamper"),
        ("IBM-Director-Alert-MIB", "unknown"),
        ("IBM-Director-Alert-MIB", "sensorCaseIntrusion"),
        ("IBM-Director-Alert-MIB", "sensorCurrent"),
        ("IBM-Director-Alert-MIB", "sensorFan"),
        ("IBM-Director-Alert-MIB", "sensorPowerSupply"),
        ("IBM-Director-Alert-MIB", "sensorTemperature"),
        ("IBM-Director-Alert-MIB", "sensorVoltage"),
        ("IBM-Director-Alert-MIB", "progress"),
        ("IBM-Director-Alert-MIB", "cableInterconnect"),
        ("IBM-Director-Alert-MIB", "drivebay"),
        ("IBM-Director-Alert-MIB", "moduleBoard"),
        ("IBM-Director-Alert-MIB", "monitorAsicIc"),
        ("IBM-Director-Alert-MIB", "network"),
        ("IBM-Director-Alert-MIB", "watchdog1"),
        ("IBM-Director-Alert-MIB", "watchdog2"),
        ("IBM-Director-Alert-MIB", "petFamilySystemOsBoot"),
        ("IBM-Director-Alert-MIB", "heartbeat"),
        ("IBM-Director-Alert-MIB", "vendorUnsupported"),
        ("IBM-Director-Alert-MIB", "notFound"))
)
if mibBuilder.loadTexts:
    directorNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

directorTrapsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 201, 100, 2, 1)
)
if mibBuilder.loadTexts:
    directorTrapsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-Director-Alert-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "director": director,
       "directorTraps": directorTraps,
       "directorFamily": directorFamily,
       "topology": topology,
       "online": online,
       "offline": offline,
       "create": create,
       "change": change,
       "destroy": destroy,
       "directorAgent": directorAgent,
       "processMonitor": processMonitor,
       "cpuMonitors": cpuMonitors,
       "cpuUtilization": cpuUtilization,
       "processCount": processCount,
       "diskMonitors": diskMonitors,
       "driveSpaceUsed": driveSpaceUsed,
       "driveSpaceUsedPercent": driveSpaceUsedPercent,
       "driveSpaceRemaining": driveSpaceRemaining,
       "driveWorkload": driveWorkload,
       "memoryMonitors": memoryMonitors,
       "lockedMemory": lockedMemory,
       "memoryUsage": memoryUsage,
       "nicMonitors": nicMonitors,
       "ntPerfMonitors": ntPerfMonitors,
       "totalPrivilegedTimePercent": totalPrivilegedTimePercent,
       "fileReadOperationsPerSec": fileReadOperationsPerSec,
       "tcpipMonitors": tcpipMonitors,
       "udpPacketsSentPerSec": udpPacketsSentPerSec,
       "udpPacketsReceivedPerSec": udpPacketsReceivedPerSec,
       "ipPacketsSentPerSec": ipPacketsSentPerSec,
       "ipPacketsReceivedPerSec": ipPacketsReceivedPerSec,
       "ipErrorPacketsReceivedPerSec": ipErrorPacketsReceivedPerSec,
       "tcpConnections": tcpConnections,
       "monitorEventDetails": monitorEventDetails,
       "actualValue": actualValue,
       "duration": duration,
       "monitorResource": monitorResource,
       "thresholdName": thresholdName,
       "thresholdValue": thresholdValue,
       "test": test,
       "action": action,
       "console": console,
       "consoleEventDetails": consoleEventDetails,
       "userID": userID,
       "address": address,
       "userName": userName,
       "userDescription": userDescription,
       "userLocale": userLocale,
       "logonFailure": logonFailure,
       "badPassword": badPassword,
       "badUserID": badUserID,
       "disabledUserID": disabledUserID,
       "downlevelConsole": downlevelConsole,
       "expiredPassword": expiredPassword,
       "tooManyActiveIDs": tooManyActiveIDs,
       "tooManyActiveLogons": tooManyActiveLogons,
       "uplevelConsole": uplevelConsole,
       "logoff": logoff,
       "logon": logon,
       "generalEvent": generalEvent,
       "cimFamily": cimFamily,
       "windowsNTEventLog": windowsNTEventLog,
       "windowsNTEventLogEventDetails": windowsNTEventLogEventDetails,
       "category": category,
       "categoryString": categoryString,
       "computerName": computerName,
       "data": data,
       "eventLogCode": eventLogCode,
       "eventLogIdentifier": eventLogIdentifier,
       "eventLogType": eventLogType,
       "insertionStrings": insertionStrings,
       "logFile": logFile,
       "message": message,
       "recordNumber": recordNumber,
       "sourceName": sourceName,
       "type": type,
       "user": user,
       "applicationLog": applicationLog,
       "securityLog": securityLog,
       "systemLog": systemLog,
       "windowsNTService": windowsNTService,
       "windowsNTServiceEventDetails": windowsNTServiceEventDetails,
       "acceptPause": acceptPause,
       "acceptStop": acceptStop,
       "caption": caption,
       "checkPoint": checkPoint,
       "creationClassName": creationClassName,
       "serviceDescription": serviceDescription,
       "desktopInteract": desktopInteract,
       "displayName": displayName,
       "errorControl": errorControl,
       "exitCode": exitCode,
       "name": name,
       "pathName": pathName,
       "processId": processId,
       "serviceSpecificExitCode": serviceSpecificExitCode,
       "serviceType": serviceType,
       "startMode": startMode,
       "startName": startName,
       "started": started,
       "serviceState": serviceState,
       "status": status,
       "systemCreationClassName": systemCreationClassName,
       "systemName": systemName,
       "tagId": tagId,
       "waitHint": waitHint,
       "startedService": startedService,
       "stoppedService": stoppedService,
       "windowsRegistry": windowsRegistry,
       "windowsRegistryEventDetails": windowsRegistryEventDetails,
       "hive": hive,
       "rootPath": rootPath,
       "securityDescriptor": securityDescriptor,
       "timeCreated": timeCreated,
       "softwareTreeChanged": softwareTreeChanged,
       "systemTreeChanged": systemTreeChanged,
       "mpaFamily": mpaFamily,
       "mpaEventDetails": mpaEventDetails,
       "alertCode": alertCode,
       "busId": busId,
       "componentId": componentId,
       "firmwareCode": firmwareCode,
       "ipAddress1": ipAddress1,
       "ipAddress2": ipAddress2,
       "issue": issue,
       "powerDomain": powerDomain,
       "reason": reason,
       "scsiId": scsiId,
       "side": side,
       "newState": newState,
       "temperatureSensor": temperatureSensor,
       "threshold": threshold,
       "universalUniqueId": universalUniqueId,
       "senderUniversalUniqueId": senderUniversalUniqueId,
       "sourceUniversalUniqueId": sourceUniversalUniqueId,
       "unitNumber": unitNumber,
       "voltageSensor": voltageSensor,
       "component": component,
       "bladeServer": bladeServer,
       "coD": coD,
       "codEnabled": codEnabled,
       "bladeServerCommunication": bladeServerCommunication,
       "bladeServerInserted": bladeServerInserted,
       "bladeServerRemoved": bladeServerRemoved,
       "bus": bus,
       "busCommunication": busCommunication,
       "chassis": chassis,
       "chassisConfiguration": chassisConfiguration,
       "chassisFailed": chassisFailed,
       "dasd": dasd,
       "dasdFailed": dasdFailed,
       "dasdInserted": dasdInserted,
       "dasdRemoved": dasdRemoved,
       "memory": memory,
       "memoryFailed": memoryFailed,
       "componentFan": componentFan,
       "componentFanFailed": componentFanFailed,
       "componentFanInserted": componentFanInserted,
       "componentFanPfa": componentFanPfa,
       "componentFanRemoved": componentFanRemoved,
       "hardwareInformation": hardwareInformation,
       "hardwareCrashDump": hardwareCrashDump,
       "hardwareCrashDumpAborted": hardwareCrashDumpAborted,
       "hardwareCrashDumpCompleted": hardwareCrashDumpCompleted,
       "hardwareCrashDumpInitiated": hardwareCrashDumpInitiated,
       "ioModule": ioModule,
       "ioModuleConfiguration": ioModuleConfiguration,
       "ioModuleFailed": ioModuleFailed,
       "ioModuleInserted": ioModuleInserted,
       "ioModulePost": ioModulePost,
       "ioModulePower": ioModulePower,
       "ioModulePowerOn": ioModulePowerOn,
       "ioModulePowerOff": ioModulePowerOff,
       "ioModuleRedundancy": ioModuleRedundancy,
       "ioModuleRemoved": ioModuleRemoved,
       "kvm": kvm,
       "kvmOwner": kvmOwner,
       "osImage": osImage,
       "osImageCrashDump": osImageCrashDump,
       "osImageCrashDumpAborted": osImageCrashDumpAborted,
       "osImageCrashDumpCompleted": osImageCrashDumpCompleted,
       "osImageCrashDumpInitiated": osImageCrashDumpInitiated,
       "componentPfa": componentPfa,
       "powerSubsystem": powerSubsystem,
       "powerSubsystemLowFuel": powerSubsystemLowFuel,
       "powerSubsystemOverCurrent": powerSubsystemOverCurrent,
       "powerSubsystemOverPower": powerSubsystemOverPower,
       "powerSubsystemRedundancy": powerSubsystemRedundancy,
       "powerSupply": powerSupply,
       "powerSupplyFailed": powerSupplyFailed,
       "powerSupplyInserted": powerSupplyInserted,
       "powerSupplyRemoved": powerSupplyRemoved,
       "server": server,
       "serverPower": serverPower,
       "serverPowerOff": serverPowerOff,
       "serverPowerOn": serverPowerOn,
       "serverPowerState": serverPowerState,
       "serviceProcessor": serviceProcessor,
       "serviceProcessorActive": serviceProcessorActive,
       "serviceProcessorConfiguration": serviceProcessorConfiguration,
       "serviceProcessorInserted": serviceProcessorInserted,
       "serviceProcessorLog": serviceProcessorLog,
       "serviceProcessorNetworkStack": serviceProcessorNetworkStack,
       "serviceProcessorRedundancy": serviceProcessorRedundancy,
       "serviceProcessorRemoteLogin": serviceProcessorRemoteLogin,
       "serviceProcessorRemoved": serviceProcessorRemoved,
       "serviceProcessorRestart": serviceProcessorRestart,
       "serviceProcessorTest": serviceProcessorTest,
       "smpExpansionModule": smpExpansionModule,
       "smpExpansionModuleDisabled": smpExpansionModuleDisabled,
       "usb": usb,
       "usbInserted": usbInserted,
       "usbOwner": usbOwner,
       "usbRemoved": usbRemoved,
       "vrm": vrm,
       "vrmFailed": vrmFailed,
       "critical": critical,
       "hardDiskDrive": hardDiskDrive,
       "multipleFanFailure": multipleFanFailure,
       "powerFailure": powerFailure,
       "powerFailureEpow": powerFailureEpow,
       "powerFailureFailed": powerFailureFailed,
       "powerFailureRemoved": powerFailureRemoved,
       "criticalTamper": criticalTamper,
       "criticalTemperature": criticalTemperature,
       "criticalTemperatureAmbient": criticalTemperatureAmbient,
       "criticalTemperaturePci": criticalTemperaturePci,
       "criticalTemperaturePlanar": criticalTemperaturePlanar,
       "criticalVoltage": criticalVoltage,
       "criticalTwelveVolts": criticalTwelveVolts,
       "criticalTwelveVoltsHigh": criticalTwelveVoltsHigh,
       "criticalTwelveVoltsLow": criticalTwelveVoltsLow,
       "criticalTwelveVoltsFaultA": criticalTwelveVoltsFaultA,
       "criticalTwelveVoltsFaultB": criticalTwelveVoltsFaultB,
       "criticalTwelveVoltsFaultC": criticalTwelveVoltsFaultC,
       "criticalTwelveVoltsFaultD": criticalTwelveVoltsFaultD,
       "criticalOneVolt": criticalOneVolt,
       "criticalOneVoltHigh": criticalOneVoltHigh,
       "criticalOneVoltLow": criticalOneVoltLow,
       "criticalTwoVolts": criticalTwoVolts,
       "criticalTwoVoltsHigh": criticalTwoVoltsHigh,
       "criticalTwoVoltsLow": criticalTwoVoltsLow,
       "criticalThreeVolts": criticalThreeVolts,
       "criticalThreeVoltsHigh": criticalThreeVoltsHigh,
       "criticalThreeVoltsLow": criticalThreeVoltsLow,
       "criticalThreeVoltsPci": criticalThreeVoltsPci,
       "criticalThreeVoltsPciHigh": criticalThreeVoltsPciHigh,
       "criticalThreeVoltsPciLow": criticalThreeVoltsPciLow,
       "criticalThreeVoltsStandby": criticalThreeVoltsStandby,
       "criticalThreeVoltsStandbyHigh": criticalThreeVoltsStandbyHigh,
       "criticalThreeVoltsStandbyLow": criticalThreeVoltsStandbyLow,
       "criticalFiveVolts": criticalFiveVolts,
       "criticalFiveVoltsHigh": criticalFiveVoltsHigh,
       "criticalFiveVoltsLow": criticalFiveVoltsLow,
       "criticalFiveVoltsFault": criticalFiveVoltsFault,
       "criticalFiveVoltsFaultHigh": criticalFiveVoltsFaultHigh,
       "criticalFiveVoltsFaultLow": criticalFiveVoltsFaultLow,
       "criticalFiveVoltsPci": criticalFiveVoltsPci,
       "criticalFiveVoltsPciHigh": criticalFiveVoltsPciHigh,
       "criticalFiveVoltsPciLow": criticalFiveVoltsPciLow,
       "criticalFiveVoltsStandby": criticalFiveVoltsStandby,
       "criticalFiveVoltsStandbyHigh": criticalFiveVoltsStandbyHigh,
       "criticalFiveVoltsStandbyLow": criticalFiveVoltsStandbyLow,
       "criticalNTwelveVolts": criticalNTwelveVolts,
       "criticalNTwelveVoltsHigh": criticalNTwelveVoltsHigh,
       "criticalNTwelveVoltsLow": criticalNTwelveVoltsLow,
       "voltageRegulatorModuleFailure": voltageRegulatorModuleFailure,
       "deployment": deployment,
       "deploymentBoot": deploymentBoot,
       "deploymentLoader": deploymentLoader,
       "deploymentOs": deploymentOs,
       "deploymentPost": deploymentPost,
       "environmental": environmental,
       "environmentalTemperature": environmentalTemperature,
       "environmentalVoltage": environmentalVoltage,
       "nonCritical": nonCritical,
       "nonCriticalFan": nonCriticalFan,
       "nonCriticalFanRemoved": nonCriticalFanRemoved,
       "redundantPower": redundantPower,
       "singleFanFailure": singleFanFailure,
       "nonCriticalTemperature": nonCriticalTemperature,
       "nonCriticalTemperatureAmbient": nonCriticalTemperatureAmbient,
       "nonCriticalTemperaturePci": nonCriticalTemperaturePci,
       "nonCriticalTemperaturePlanar": nonCriticalTemperaturePlanar,
       "nonCriticalVoltage": nonCriticalVoltage,
       "nonCriticalTwelveVolts": nonCriticalTwelveVolts,
       "nonCriticalTwelveVoltsHigh": nonCriticalTwelveVoltsHigh,
       "nonCriticalTwelveVoltsLow": nonCriticalTwelveVoltsLow,
       "nonCriticalOneVolt": nonCriticalOneVolt,
       "nonCriticalOneVoltHigh": nonCriticalOneVoltHigh,
       "nonCriticalOneVoltLow": nonCriticalOneVoltLow,
       "nonCriticalTwoVolts": nonCriticalTwoVolts,
       "nonCriticalTwoVoltsHigh": nonCriticalTwoVoltsHigh,
       "nonCriticalTwoVoltsLow": nonCriticalTwoVoltsLow,
       "nonCriticalThreeVolts": nonCriticalThreeVolts,
       "nonCriticalThreeVoltsHigh": nonCriticalThreeVoltsHigh,
       "nonCriticalThreeVoltsLow": nonCriticalThreeVoltsLow,
       "nonCriticalThreeVoltsPci": nonCriticalThreeVoltsPci,
       "nonCriticalThreeVoltsPciHigh": nonCriticalThreeVoltsPciHigh,
       "nonCriticalThreeVoltsPciLow": nonCriticalThreeVoltsPciLow,
       "nonCriticalThreeVoltsStandby": nonCriticalThreeVoltsStandby,
       "nonCriticalThreeVoltsStandbyHigh": nonCriticalThreeVoltsStandbyHigh,
       "nonCriticalThreeVoltsStandbyLow": nonCriticalThreeVoltsStandbyLow,
       "nonCriticalFiveVolts": nonCriticalFiveVolts,
       "nonCriticalFiveVoltsHigh": nonCriticalFiveVoltsHigh,
       "nonCriticalFiveVoltsLow": nonCriticalFiveVoltsLow,
       "nonCriticalFiveVoltsPci": nonCriticalFiveVoltsPci,
       "nonCriticalFiveVoltsPciHigh": nonCriticalFiveVoltsPciHigh,
       "nonCriticalFiveVoltsPciLow": nonCriticalFiveVoltsPciLow,
       "nonCriticalFiveVoltsStandby": nonCriticalFiveVoltsStandby,
       "nonCriticalFiveVoltsStandbyHigh": nonCriticalFiveVoltsStandbyHigh,
       "nonCriticalFiveVoltsStandbyLow": nonCriticalFiveVoltsStandbyLow,
       "nonCriticalNTwelveVolts": nonCriticalNTwelveVolts,
       "nonCriticalNTwelveVoltsHigh": nonCriticalNTwelveVoltsHigh,
       "nonCriticalNTwelveVoltsLow": nonCriticalNTwelveVoltsLow,
       "platform": platform,
       "scalableNode": scalableNode,
       "scalableNodeMode": scalableNodeMode,
       "scalableNodeModeNullOrUnknown": scalableNodeModeNullOrUnknown,
       "scalableNodeModePrimary": scalableNodeModePrimary,
       "scalableNodeModeSecondary": scalableNodeModeSecondary,
       "scalableNodeModeStandalone": scalableNodeModeStandalone,
       "scalableNodeStandalone": scalableNodeStandalone,
       "standaloneMode": standaloneMode,
       "primary": primary,
       "reset": reset,
       "resetPrimary": resetPrimary,
       "resetSecondary": resetSecondary,
       "secondary": secondary,
       "scalablePartition": scalablePartition,
       "scalablePartitionAlert": scalablePartitionAlert,
       "scalablePartitionState": scalablePartitionState,
       "scalablePartitionNullOrUnknown": scalablePartitionNullOrUnknown,
       "scalablePartitionPoweredOff": scalablePartitionPoweredOff,
       "scalablePartitionPoweringOn": scalablePartitionPoweringOn,
       "scalablePartitionResetting": scalablePartitionResetting,
       "scalablePartitionShuttingDown": scalablePartitionShuttingDown,
       "system": system,
       "bootFailure": bootFailure,
       "fuelGauge": fuelGauge,
       "fuelGaugeLowFuel": fuelGaugeLowFuel,
       "fuelGaugeNotRedundant": fuelGaugeNotRedundant,
       "fuelGaugeOverCurrent": fuelGaugeOverCurrent,
       "systemLoaderTimeout": systemLoaderTimeout,
       "systemOsTimeout": systemOsTimeout,
       "systemPfa": systemPfa,
       "fanSystemPfa": fanSystemPfa,
       "systemPostTimeout": systemPostTimeout,
       "systemPowerOff": systemPowerOff,
       "systemPowerOn": systemPowerOn,
       "systemRedundantPower": systemRedundantPower,
       "systemTamper": systemTamper,
       "unknown": unknown,
       "petFamily": petFamily,
       "petFamilyEventDetails": petFamilyEventDetails,
       "allVariableBindings": allVariableBindings,
       "entity": entity,
       "entityInstance": entityInstance,
       "petEventData": petEventData,
       "petEventSeverity": petEventSeverity,
       "petEventSourceType": petEventSourceType,
       "petEventType": petEventType,
       "guid": guid,
       "languageCode": languageCode,
       "localTimeStamp": localTimeStamp,
       "manufacturerId": manufacturerId,
       "oemCustomField": oemCustomField,
       "offset": offset,
       "sensorDevice": sensorDevice,
       "sensorNumber": sensorNumber,
       "sensorType": sensorType,
       "sequenceId": sequenceId,
       "systemId": systemId,
       "trapSourceType": trapSourceType,
       "utcOffset": utcOffset,
       "petEnvironmental": petEnvironmental,
       "petEnvironmentalSensor": petEnvironmentalSensor,
       "sensorCaseIntrusion": sensorCaseIntrusion,
       "sensorCurrent": sensorCurrent,
       "sensorFan": sensorFan,
       "sensorPowerSupply": sensorPowerSupply,
       "sensorTemperature": sensorTemperature,
       "sensorVoltage": sensorVoltage,
       "firmware": firmware,
       "bios": bios,
       "progress": progress,
       "hardware": hardware,
       "cableInterconnect": cableInterconnect,
       "drivebay": drivebay,
       "moduleBoard": moduleBoard,
       "monitorAsicIc": monitorAsicIc,
       "network": network,
       "watchdog1": watchdog1,
       "watchdog2": watchdog2,
       "petFamilySystem": petFamilySystem,
       "petFamilySystemOs": petFamilySystemOs,
       "petFamilySystemOsBoot": petFamilySystemOsBoot,
       "petFamilySystemOsOperation": petFamilySystemOsOperation,
       "heartbeat": heartbeat,
       "storageFamily": storageFamily,
       "serveRaidController": serveRaidController,
       "physicalDrive": physicalDrive,
       "vendorUnsupported": vendorUnsupported,
       "state": state,
       "notFound": notFound,
       "directorTrapsConformance": directorTrapsConformance,
       "directorTrapsGroups": directorTrapsGroups,
       "directorTrapsGroup": directorTrapsGroup,
       "directorNotificationsGroup": directorNotificationsGroup,
       "directorTrapsCompliances": directorTrapsCompliances,
       "directorTrapsCompliance": directorTrapsCompliance,
       "description": description,
       "trapType": trapType,
       "trapSeverity": trapSeverity,
       "trapSenderName": trapSenderName,
       "trapManagedObjectName": trapManagedObjectName,
       "trapText": trapText,
       "trapCategory": trapCategory,
       "details": details,
       "char": char,
       "short": short,
       "int": int,
       "long": long,
       "boolean": boolean,
       "float": float,
       "double": double,
       "octet": octet,
       "string": string,
       "dateTime": dateTime,
       "uniChar": uniChar,
       "byte": byte}
)
