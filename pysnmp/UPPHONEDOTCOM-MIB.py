# SNMP MIB module (UPPHONEDOTCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UPPHONEDOTCOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:36 2024
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
 NotificationType,
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
    "NotificationType",
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

_PhoneDotCom_ObjectIdentity = ObjectIdentity
phoneDotCom = _PhoneDotCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4)
)
_UpiInit_ObjectIdentity = ObjectIdentity
upiInit = _UpiInit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1)
)
_UpiInitDescriptionTable_Object = MibTable
upiInitDescriptionTable = _UpiInitDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1)
)
if mibBuilder.loadTexts:
    upiInitDescriptionTable.setStatus("mandatory")
_UpiInitDescriptionEntry_Object = MibTableRow
upiInitDescriptionEntry = _UpiInitDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1, 1)
)
upiInitDescriptionEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "upidInitIpAddr"),
    (0, "UPPHONEDOTCOM-MIB", "upidInitProcessId"),
)
if mibBuilder.loadTexts:
    upiInitDescriptionEntry.setStatus("mandatory")
_UpidInitIpAddr_Type = IpAddress
_UpidInitIpAddr_Object = MibTableColumn
upidInitIpAddr = _UpidInitIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1, 1, 1),
    _UpidInitIpAddr_Type()
)
upidInitIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upidInitIpAddr.setStatus("mandatory")
_UpidInitProcessId_Type = Integer32
_UpidInitProcessId_Object = MibTableColumn
upidInitProcessId = _UpidInitProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1, 1, 2),
    _UpidInitProcessId_Type()
)
upidInitProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upidInitProcessId.setStatus("mandatory")
_UpidInitVersion_Type = DisplayString
_UpidInitVersion_Object = MibTableColumn
upidInitVersion = _UpidInitVersion_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1, 1, 3),
    _UpidInitVersion_Type()
)
upidInitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upidInitVersion.setStatus("mandatory")
_UpidInitProcessType_Type = DisplayString
_UpidInitProcessType_Object = MibTableColumn
upidInitProcessType = _UpidInitProcessType_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1, 1, 4),
    _UpidInitProcessType_Type()
)
upidInitProcessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upidInitProcessType.setStatus("mandatory")
_UpidInitHostName_Type = DisplayString
_UpidInitHostName_Object = MibTableColumn
upidInitHostName = _UpidInitHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1, 1, 5),
    _UpidInitHostName_Type()
)
upidInitHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upidInitHostName.setStatus("mandatory")
_UpidInitStartupTime_Type = DisplayString
_UpidInitStartupTime_Object = MibTableColumn
upidInitStartupTime = _UpidInitStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 1, 1, 6),
    _UpidInitStartupTime_Type()
)
upidInitStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upidInitStartupTime.setStatus("mandatory")
_UpiInitStats_ObjectIdentity = ObjectIdentity
upiInitStats = _UpiInitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2)
)
_UpiInitChildProcessTable_Object = MibTable
upiInitChildProcessTable = _UpiInitChildProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    upiInitChildProcessTable.setStatus("mandatory")
_UpiInitChildProcessEntry_Object = MibTableRow
upiInitChildProcessEntry = _UpiInitChildProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1)
)
upiInitChildProcessEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "upipInitIpAddr"),
    (0, "UPPHONEDOTCOM-MIB", "upipInitProcessId"),
    (0, "UPPHONEDOTCOM-MIB", "upipChildProcessId"),
)
if mibBuilder.loadTexts:
    upiInitChildProcessEntry.setStatus("mandatory")
_UpipInitIpAddr_Type = IpAddress
_UpipInitIpAddr_Object = MibTableColumn
upipInitIpAddr = _UpipInitIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 1),
    _UpipInitIpAddr_Type()
)
upipInitIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipInitIpAddr.setStatus("mandatory")
_UpipInitProcessType_Type = DisplayString
_UpipInitProcessType_Object = MibTableColumn
upipInitProcessType = _UpipInitProcessType_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 2),
    _UpipInitProcessType_Type()
)
upipInitProcessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipInitProcessType.setStatus("mandatory")
_UpipInitProcessId_Type = Integer32
_UpipInitProcessId_Object = MibTableColumn
upipInitProcessId = _UpipInitProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 3),
    _UpipInitProcessId_Type()
)
upipInitProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipInitProcessId.setStatus("mandatory")
_UpipChildProcessId_Type = Integer32
_UpipChildProcessId_Object = MibTableColumn
upipChildProcessId = _UpipChildProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 4),
    _UpipChildProcessId_Type()
)
upipChildProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessId.setStatus("mandatory")
_UpipChildProcessType_Type = DisplayString
_UpipChildProcessType_Object = MibTableColumn
upipChildProcessType = _UpipChildProcessType_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 5),
    _UpipChildProcessType_Type()
)
upipChildProcessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessType.setStatus("mandatory")
_UpipChildProcessIpAddr_Type = IpAddress
_UpipChildProcessIpAddr_Object = MibTableColumn
upipChildProcessIpAddr = _UpipChildProcessIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 6),
    _UpipChildProcessIpAddr_Type()
)
upipChildProcessIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessIpAddr.setStatus("mandatory")
_UpipChildProcessHostName_Type = DisplayString
_UpipChildProcessHostName_Object = MibTableColumn
upipChildProcessHostName = _UpipChildProcessHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 7),
    _UpipChildProcessHostName_Type()
)
upipChildProcessHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessHostName.setStatus("mandatory")
_UpipChildProcessExePath_Type = DisplayString
_UpipChildProcessExePath_Object = MibTableColumn
upipChildProcessExePath = _UpipChildProcessExePath_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 8),
    _UpipChildProcessExePath_Type()
)
upipChildProcessExePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessExePath.setStatus("mandatory")
_UpipChildProcessExeArgs_Type = DisplayString
_UpipChildProcessExeArgs_Object = MibTableColumn
upipChildProcessExeArgs = _UpipChildProcessExeArgs_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 9),
    _UpipChildProcessExeArgs_Type()
)
upipChildProcessExeArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessExeArgs.setStatus("mandatory")
_UpipChildProcessState_Type = DisplayString
_UpipChildProcessState_Object = MibTableColumn
upipChildProcessState = _UpipChildProcessState_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 10),
    _UpipChildProcessState_Type()
)
upipChildProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessState.setStatus("mandatory")
_UpipChildProcessStatus_Type = DisplayString
_UpipChildProcessStatus_Object = MibTableColumn
upipChildProcessStatus = _UpipChildProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 11),
    _UpipChildProcessStatus_Type()
)
upipChildProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessStatus.setStatus("mandatory")
_UpipChildProcessStartTime_Type = DisplayString
_UpipChildProcessStartTime_Object = MibTableColumn
upipChildProcessStartTime = _UpipChildProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 12),
    _UpipChildProcessStartTime_Type()
)
upipChildProcessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessStartTime.setStatus("mandatory")
_UpipChildProcessStopTime_Type = DisplayString
_UpipChildProcessStopTime_Object = MibTableColumn
upipChildProcessStopTime = _UpipChildProcessStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 1, 1, 13),
    _UpipChildProcessStopTime_Type()
)
upipChildProcessStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipChildProcessStopTime.setStatus("mandatory")
_UpiInitChildProcessStatsTable_Object = MibTable
upiInitChildProcessStatsTable = _UpiInitChildProcessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    upiInitChildProcessStatsTable.setStatus("mandatory")
_UpiInitChildProcessStatsEntry_Object = MibTableRow
upiInitChildProcessStatsEntry = _UpiInitChildProcessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1)
)
upiInitChildProcessStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "upipsInitIpAddr"),
    (0, "UPPHONEDOTCOM-MIB", "upipsInitProcessId"),
    (0, "UPPHONEDOTCOM-MIB", "upipsChildProcessType"),
)
if mibBuilder.loadTexts:
    upiInitChildProcessStatsEntry.setStatus("mandatory")
_UpipsInitIpAddr_Type = IpAddress
_UpipsInitIpAddr_Object = MibTableColumn
upipsInitIpAddr = _UpipsInitIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1, 1),
    _UpipsInitIpAddr_Type()
)
upipsInitIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipsInitIpAddr.setStatus("mandatory")
_UpipsInitProcessId_Type = Integer32
_UpipsInitProcessId_Object = MibTableColumn
upipsInitProcessId = _UpipsInitProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1, 2),
    _UpipsInitProcessId_Type()
)
upipsInitProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipsInitProcessId.setStatus("mandatory")
_UpipsChildProcessType_Type = DisplayString
_UpipsChildProcessType_Object = MibTableColumn
upipsChildProcessType = _UpipsChildProcessType_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1, 3),
    _UpipsChildProcessType_Type()
)
upipsChildProcessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipsChildProcessType.setStatus("mandatory")
_UpipsInitProcessType_Type = DisplayString
_UpipsInitProcessType_Object = MibTableColumn
upipsInitProcessType = _UpipsInitProcessType_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1, 4),
    _UpipsInitProcessType_Type()
)
upipsInitProcessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipsInitProcessType.setStatus("mandatory")
_UpipsChildProcessesStarted_Type = Counter32
_UpipsChildProcessesStarted_Object = MibTableColumn
upipsChildProcessesStarted = _UpipsChildProcessesStarted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1, 5),
    _UpipsChildProcessesStarted_Type()
)
upipsChildProcessesStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipsChildProcessesStarted.setStatus("mandatory")
_UpipsChildProcessesDied_Type = Counter32
_UpipsChildProcessesDied_Object = MibTableColumn
upipsChildProcessesDied = _UpipsChildProcessesDied_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1, 6),
    _UpipsChildProcessesDied_Type()
)
upipsChildProcessesDied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipsChildProcessesDied.setStatus("mandatory")
_UpipsChildProcessesRunning_Type = Gauge32
_UpipsChildProcessesRunning_Object = MibTableColumn
upipsChildProcessesRunning = _UpipsChildProcessesRunning_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 2, 2, 1, 7),
    _UpipsChildProcessesRunning_Type()
)
upipsChildProcessesRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upipsChildProcessesRunning.setStatus("mandatory")
_UpiInitTrapInfo_ObjectIdentity = ObjectIdentity
upiInitTrapInfo = _UpiInitTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 20)
)
_UpitTrapInfo_Type = DisplayString
_UpitTrapInfo_Object = MibScalar
upitTrapInfo = _UpitTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 20, 1),
    _UpitTrapInfo_Type()
)
upitTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upitTrapInfo.setStatus("optional")
_UpitChildProcessHostName_Type = DisplayString
_UpitChildProcessHostName_Object = MibScalar
upitChildProcessHostName = _UpitChildProcessHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 20, 2),
    _UpitChildProcessHostName_Type()
)
upitChildProcessHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upitChildProcessHostName.setStatus("mandatory")
_UpitChildProcessType_Type = DisplayString
_UpitChildProcessType_Object = MibScalar
upitChildProcessType = _UpitChildProcessType_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 20, 3),
    _UpitChildProcessType_Type()
)
upitChildProcessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upitChildProcessType.setStatus("mandatory")
_UpitChildProcessId_Type = Integer32
_UpitChildProcessId_Object = MibScalar
upitChildProcessId = _UpitChildProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 20, 4),
    _UpitChildProcessId_Type()
)
upitChildProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upitChildProcessId.setStatus("mandatory")
_UpLink_ObjectIdentity = ObjectIdentity
upLink = _UpLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2)
)
_UpLinkProcesses_ObjectIdentity = ObjectIdentity
upLinkProcesses = _UpLinkProcesses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1)
)
_UplDispatcher_ObjectIdentity = ObjectIdentity
uplDispatcher = _UplDispatcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1)
)
_UplDispatcherDescription_ObjectIdentity = ObjectIdentity
uplDispatcherDescription = _UplDispatcherDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 1)
)
_UpldHostName_Type = DisplayString
_UpldHostName_Object = MibScalar
upldHostName = _UpldHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 1, 1),
    _UpldHostName_Type()
)
upldHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldHostName.setStatus("mandatory")
_UpldProcessId_Type = Integer32
_UpldProcessId_Object = MibScalar
upldProcessId = _UpldProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 1, 2),
    _UpldProcessId_Type()
)
upldProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldProcessId.setStatus("mandatory")
_UpldPortNumber_Type = Integer32
_UpldPortNumber_Object = MibScalar
upldPortNumber = _UpldPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 1, 3),
    _UpldPortNumber_Type()
)
upldPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldPortNumber.setStatus("mandatory")
_UpldStartUpTime_Type = DisplayString
_UpldStartUpTime_Object = MibScalar
upldStartUpTime = _UpldStartUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 1, 4),
    _UpldStartUpTime_Type()
)
upldStartUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldStartUpTime.setStatus("mandatory")


class _UpldState_Type(Integer32):
    """Custom type upldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redirect", 2),
          ("regular", 1))
    )


_UpldState_Type.__name__ = "Integer32"
_UpldState_Object = MibScalar
upldState = _UpldState_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 1, 5),
    _UpldState_Type()
)
upldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldState.setStatus("mandatory")
_UplDispatcherStats_ObjectIdentity = ObjectIdentity
uplDispatcherStats = _UplDispatcherStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 2)
)
_UpldRequestsReceived_Type = Counter32
_UpldRequestsReceived_Object = MibScalar
upldRequestsReceived = _UpldRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 2, 1),
    _UpldRequestsReceived_Type()
)
upldRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldRequestsReceived.setStatus("mandatory")
_UpldRequestsDropped_Type = Counter32
_UpldRequestsDropped_Object = MibScalar
upldRequestsDropped = _UpldRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 2, 2),
    _UpldRequestsDropped_Type()
)
upldRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldRequestsDropped.setStatus("mandatory")
_UpldUplAgentsLoaded_Type = Gauge32
_UpldUplAgentsLoaded_Object = MibScalar
upldUplAgentsLoaded = _UpldUplAgentsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 2, 3),
    _UpldUplAgentsLoaded_Type()
)
upldUplAgentsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldUplAgentsLoaded.setStatus("mandatory")
_UpldUplAgentsDisconnected_Type = Gauge32
_UpldUplAgentsDisconnected_Object = MibScalar
upldUplAgentsDisconnected = _UpldUplAgentsDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 2, 4),
    _UpldUplAgentsDisconnected_Type()
)
upldUplAgentsDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldUplAgentsDisconnected.setStatus("mandatory")
_UpldSubscribersLoaded_Type = Gauge32
_UpldSubscribersLoaded_Object = MibScalar
upldSubscribersLoaded = _UpldSubscribersLoaded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 2, 5),
    _UpldSubscribersLoaded_Type()
)
upldSubscribersLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldSubscribersLoaded.setStatus("mandatory")
_UpldKeyExchanges_Type = Counter32
_UpldKeyExchanges_Object = MibScalar
upldKeyExchanges = _UpldKeyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 2, 6),
    _UpldKeyExchanges_Type()
)
upldKeyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldKeyExchanges.setStatus("mandatory")
_UplDispatcherTrapInfo_ObjectIdentity = ObjectIdentity
uplDispatcherTrapInfo = _UplDispatcherTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 20)
)
_UpldTrapInfo_Type = DisplayString
_UpldTrapInfo_Object = MibScalar
upldTrapInfo = _UpldTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 20, 1),
    _UpldTrapInfo_Type()
)
upldTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upldTrapInfo.setStatus("optional")
_UpldUplAgentId_Type = Integer32
_UpldUplAgentId_Object = MibScalar
upldUplAgentId = _UpldUplAgentId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 20, 2),
    _UpldUplAgentId_Type()
)
upldUplAgentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upldUplAgentId.setStatus("optional")
_UplAgent_ObjectIdentity = ObjectIdentity
uplAgent = _UplAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2)
)
_UplAgentDescriptionTable_Object = MibTable
uplAgentDescriptionTable = _UplAgentDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    uplAgentDescriptionTable.setStatus("mandatory")
_UplAgentDescriptionEntry_Object = MibTableRow
uplAgentDescriptionEntry = _UplAgentDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 1, 1)
)
uplAgentDescriptionEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentDescriptionEntry.setStatus("mandatory")
_UplaAgentIdentifier_Type = Integer32
_UplaAgentIdentifier_Object = MibTableColumn
uplaAgentIdentifier = _UplaAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 1, 1, 1),
    _UplaAgentIdentifier_Type()
)
uplaAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaAgentIdentifier.setStatus("mandatory")
_UplaHostName_Type = DisplayString
_UplaHostName_Object = MibTableColumn
uplaHostName = _UplaHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 1, 1, 2),
    _UplaHostName_Type()
)
uplaHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHostName.setStatus("mandatory")
_UplaProcessId_Type = Integer32
_UplaProcessId_Object = MibTableColumn
uplaProcessId = _UplaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 1, 1, 3),
    _UplaProcessId_Type()
)
uplaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaProcessId.setStatus("mandatory")
_UplaStartUpTime_Type = DisplayString
_UplaStartUpTime_Object = MibTableColumn
uplaStartUpTime = _UplaStartUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 1, 1, 5),
    _UplaStartUpTime_Type()
)
uplaStartUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaStartUpTime.setStatus("mandatory")
_UplAgentProxyStats_ObjectIdentity = ObjectIdentity
uplAgentProxyStats = _UplAgentProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2)
)
_UplAgentWebAccessStatsTable_Object = MibTable
uplAgentWebAccessStatsTable = _UplAgentWebAccessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    uplAgentWebAccessStatsTable.setStatus("mandatory")
_UplAgentWebAccessStatsEntry_Object = MibTableRow
uplAgentWebAccessStatsEntry = _UplAgentWebAccessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1)
)
uplAgentWebAccessStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplawsAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentWebAccessStatsEntry.setStatus("mandatory")
_UplawsAgentIdentifier_Type = Integer32
_UplawsAgentIdentifier_Object = MibTableColumn
uplawsAgentIdentifier = _UplawsAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 1),
    _UplawsAgentIdentifier_Type()
)
uplawsAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplawsAgentIdentifier.setStatus("mandatory")
_UplaHttpRequestsStarted_Type = Counter32
_UplaHttpRequestsStarted_Object = MibTableColumn
uplaHttpRequestsStarted = _UplaHttpRequestsStarted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 2),
    _UplaHttpRequestsStarted_Type()
)
uplaHttpRequestsStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpRequestsStarted.setStatus("mandatory")
_UplaHttpRequestsSucceeded_Type = Counter32
_UplaHttpRequestsSucceeded_Object = MibTableColumn
uplaHttpRequestsSucceeded = _UplaHttpRequestsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 3),
    _UplaHttpRequestsSucceeded_Type()
)
uplaHttpRequestsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpRequestsSucceeded.setStatus("mandatory")
_UplaHttpMeanResponseTime_Type = Integer32
_UplaHttpMeanResponseTime_Object = MibTableColumn
uplaHttpMeanResponseTime = _UplaHttpMeanResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 4),
    _UplaHttpMeanResponseTime_Type()
)
uplaHttpMeanResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpMeanResponseTime.setStatus("mandatory")
_UplaHttpDeviationOfResponseTime_Type = Integer32
_UplaHttpDeviationOfResponseTime_Object = MibTableColumn
uplaHttpDeviationOfResponseTime = _UplaHttpDeviationOfResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 5),
    _UplaHttpDeviationOfResponseTime_Type()
)
uplaHttpDeviationOfResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpDeviationOfResponseTime.setStatus("mandatory")
_UplaHttpsRequestsStarted_Type = Counter32
_UplaHttpsRequestsStarted_Object = MibTableColumn
uplaHttpsRequestsStarted = _UplaHttpsRequestsStarted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 6),
    _UplaHttpsRequestsStarted_Type()
)
uplaHttpsRequestsStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpsRequestsStarted.setStatus("mandatory")
_UplaHttpsRequestsSucceeded_Type = Counter32
_UplaHttpsRequestsSucceeded_Object = MibTableColumn
uplaHttpsRequestsSucceeded = _UplaHttpsRequestsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 7),
    _UplaHttpsRequestsSucceeded_Type()
)
uplaHttpsRequestsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpsRequestsSucceeded.setStatus("mandatory")
_UplaHttpsMeanResponseTime_Type = Integer32
_UplaHttpsMeanResponseTime_Object = MibTableColumn
uplaHttpsMeanResponseTime = _UplaHttpsMeanResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 8),
    _UplaHttpsMeanResponseTime_Type()
)
uplaHttpsMeanResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpsMeanResponseTime.setStatus("mandatory")
_UplaHttpsDeviationOfResponseTime_Type = Integer32
_UplaHttpsDeviationOfResponseTime_Object = MibTableColumn
uplaHttpsDeviationOfResponseTime = _UplaHttpsDeviationOfResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 1, 1, 9),
    _UplaHttpsDeviationOfResponseTime_Type()
)
uplaHttpsDeviationOfResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaHttpsDeviationOfResponseTime.setStatus("mandatory")
_UplAgentErrorStatsSummaryTable_Object = MibTable
uplAgentErrorStatsSummaryTable = _UplAgentErrorStatsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    uplAgentErrorStatsSummaryTable.setStatus("mandatory")
_UplAgentErrorStatsSummaryEntry_Object = MibTableRow
uplAgentErrorStatsSummaryEntry = _UplAgentErrorStatsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1)
)
uplAgentErrorStatsSummaryEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplaesAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentErrorStatsSummaryEntry.setStatus("mandatory")
_UplaesAgentIdentifier_Type = Integer32
_UplaesAgentIdentifier_Object = MibTableColumn
uplaesAgentIdentifier = _UplaesAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 1),
    _UplaesAgentIdentifier_Type()
)
uplaesAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaesAgentIdentifier.setStatus("mandatory")
_UplaTotalErrors_Type = Counter32
_UplaTotalErrors_Object = MibTableColumn
uplaTotalErrors = _UplaTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 2),
    _UplaTotalErrors_Type()
)
uplaTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTotalErrors.setStatus("mandatory")
_UplaSilentErrors_Type = Counter32
_UplaSilentErrors_Object = MibTableColumn
uplaSilentErrors = _UplaSilentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 3),
    _UplaSilentErrors_Type()
)
uplaSilentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaSilentErrors.setStatus("mandatory")
_UplaDeviceErrors_Type = Counter32
_UplaDeviceErrors_Object = MibTableColumn
uplaDeviceErrors = _UplaDeviceErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 4),
    _UplaDeviceErrors_Type()
)
uplaDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaDeviceErrors.setStatus("mandatory")
_UplaKeyErrors_Type = Counter32
_UplaKeyErrors_Object = MibTableColumn
uplaKeyErrors = _UplaKeyErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 5),
    _UplaKeyErrors_Type()
)
uplaKeyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaKeyErrors.setStatus("mandatory")
_UplaSessionErrors_Type = Counter32
_UplaSessionErrors_Object = MibTableColumn
uplaSessionErrors = _UplaSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 6),
    _UplaSessionErrors_Type()
)
uplaSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaSessionErrors.setStatus("mandatory")
_UplaTransactionErrors_Type = Counter32
_UplaTransactionErrors_Object = MibTableColumn
uplaTransactionErrors = _UplaTransactionErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 7),
    _UplaTransactionErrors_Type()
)
uplaTransactionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTransactionErrors.setStatus("mandatory")
_UplaOtherErrors_Type = Counter32
_UplaOtherErrors_Object = MibTableColumn
uplaOtherErrors = _UplaOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 2, 1, 8),
    _UplaOtherErrors_Type()
)
uplaOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaOtherErrors.setStatus("mandatory")
_UplAgentErrorStatsDetailTable_Object = MibTable
uplAgentErrorStatsDetailTable = _UplAgentErrorStatsDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    uplAgentErrorStatsDetailTable.setStatus("mandatory")
_UplAgentErrorStatsDetailEntry_Object = MibTableRow
uplAgentErrorStatsDetailEntry = _UplAgentErrorStatsDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3, 1)
)
uplAgentErrorStatsDetailEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplaedAgentIdentifier"),
    (0, "UPPHONEDOTCOM-MIB", "uplaErrorCode"),
)
if mibBuilder.loadTexts:
    uplAgentErrorStatsDetailEntry.setStatus("mandatory")
_UplaedAgentIdentifier_Type = Integer32
_UplaedAgentIdentifier_Object = MibTableColumn
uplaedAgentIdentifier = _UplaedAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3, 1, 1),
    _UplaedAgentIdentifier_Type()
)
uplaedAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaedAgentIdentifier.setStatus("mandatory")
_UplaErrorCode_Type = Integer32
_UplaErrorCode_Object = MibTableColumn
uplaErrorCode = _UplaErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3, 1, 2),
    _UplaErrorCode_Type()
)
uplaErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaErrorCode.setStatus("mandatory")
_UplaErrorName_Type = DisplayString
_UplaErrorName_Object = MibTableColumn
uplaErrorName = _UplaErrorName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3, 1, 3),
    _UplaErrorName_Type()
)
uplaErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaErrorName.setStatus("mandatory")
_UplaErrorSeverity_Type = Integer32
_UplaErrorSeverity_Object = MibTableColumn
uplaErrorSeverity = _UplaErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3, 1, 4),
    _UplaErrorSeverity_Type()
)
uplaErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaErrorSeverity.setStatus("optional")


class _UplaErrorClass_Type(Integer32):
    """Custom type uplaErrorClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("device", 2),
          ("key", 3),
          ("other", 6),
          ("session", 4),
          ("silent", 1),
          ("transaction", 5))
    )


_UplaErrorClass_Type.__name__ = "Integer32"
_UplaErrorClass_Object = MibTableColumn
uplaErrorClass = _UplaErrorClass_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3, 1, 5),
    _UplaErrorClass_Type()
)
uplaErrorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaErrorClass.setStatus("mandatory")
_UplaErrorCount_Type = Counter32
_UplaErrorCount_Object = MibTableColumn
uplaErrorCount = _UplaErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 2, 3, 1, 6),
    _UplaErrorCount_Type()
)
uplaErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaErrorCount.setStatus("mandatory")
_UplHdtpStats_ObjectIdentity = ObjectIdentity
uplHdtpStats = _UplHdtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3)
)
_UplAgentSessionStatsTable_Object = MibTable
uplAgentSessionStatsTable = _UplAgentSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    uplAgentSessionStatsTable.setStatus("mandatory")
_UplAgentSessionStatsEntry_Object = MibTableRow
uplAgentSessionStatsEntry = _UplAgentSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1)
)
uplAgentSessionStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplassAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentSessionStatsEntry.setStatus("mandatory")
_UplassAgentIdentifier_Type = Integer32
_UplassAgentIdentifier_Object = MibTableColumn
uplassAgentIdentifier = _UplassAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1, 1),
    _UplassAgentIdentifier_Type()
)
uplassAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplassAgentIdentifier.setStatus("mandatory")
_UplaActiveSessions_Type = Gauge32
_UplaActiveSessions_Object = MibTableColumn
uplaActiveSessions = _UplaActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1, 2),
    _UplaActiveSessions_Type()
)
uplaActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaActiveSessions.setStatus("mandatory")
_UplaEncryptedSessions_Type = Gauge32
_UplaEncryptedSessions_Object = MibTableColumn
uplaEncryptedSessions = _UplaEncryptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1, 3),
    _UplaEncryptedSessions_Type()
)
uplaEncryptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaEncryptedSessions.setStatus("mandatory")
_UplaProtoSessions_Type = Gauge32
_UplaProtoSessions_Object = MibTableColumn
uplaProtoSessions = _UplaProtoSessions_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1, 4),
    _UplaProtoSessions_Type()
)
uplaProtoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaProtoSessions.setStatus("mandatory")
_UplaSessionsStarted_Type = Counter32
_UplaSessionsStarted_Object = MibTableColumn
uplaSessionsStarted = _UplaSessionsStarted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1, 5),
    _UplaSessionsStarted_Type()
)
uplaSessionsStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaSessionsStarted.setStatus("mandatory")
_UplaSessionsSucceeded_Type = Counter32
_UplaSessionsSucceeded_Object = MibTableColumn
uplaSessionsSucceeded = _UplaSessionsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1, 6),
    _UplaSessionsSucceeded_Type()
)
uplaSessionsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaSessionsSucceeded.setStatus("mandatory")
_UplaKeyExchanges_Type = Counter32
_UplaKeyExchanges_Object = MibTableColumn
uplaKeyExchanges = _UplaKeyExchanges_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 1, 1, 7),
    _UplaKeyExchanges_Type()
)
uplaKeyExchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaKeyExchanges.setStatus("mandatory")
_UplAgentAirLinkStatsTable_Object = MibTable
uplAgentAirLinkStatsTable = _UplAgentAirLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    uplAgentAirLinkStatsTable.setStatus("deprecated")
_UplAgentAirLinkStatsEntry_Object = MibTableRow
uplAgentAirLinkStatsEntry = _UplAgentAirLinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1)
)
uplAgentAirLinkStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplaasAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentAirLinkStatsEntry.setStatus("deprecated")
_UplaasAgentIdentifier_Type = Integer32
_UplaasAgentIdentifier_Object = MibTableColumn
uplaasAgentIdentifier = _UplaasAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1, 1),
    _UplaasAgentIdentifier_Type()
)
uplaasAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaasAgentIdentifier.setStatus("deprecated")
_UplaRequestsReceived_Type = Counter32
_UplaRequestsReceived_Object = MibTableColumn
uplaRequestsReceived = _UplaRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1, 2),
    _UplaRequestsReceived_Type()
)
uplaRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaRequestsReceived.setStatus("deprecated")
_UplaRequestsDropped_Type = Counter32
_UplaRequestsDropped_Object = MibTableColumn
uplaRequestsDropped = _UplaRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1, 3),
    _UplaRequestsDropped_Type()
)
uplaRequestsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaRequestsDropped.setStatus("deprecated")
_UplaRequestsDuplicated_Type = Counter32
_UplaRequestsDuplicated_Object = MibTableColumn
uplaRequestsDuplicated = _UplaRequestsDuplicated_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1, 4),
    _UplaRequestsDuplicated_Type()
)
uplaRequestsDuplicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaRequestsDuplicated.setStatus("deprecated")
_UplaRequestsNotValid_Type = Counter32
_UplaRequestsNotValid_Object = MibTableColumn
uplaRequestsNotValid = _UplaRequestsNotValid_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1, 5),
    _UplaRequestsNotValid_Type()
)
uplaRequestsNotValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaRequestsNotValid.setStatus("deprecated")
_UplaRepliesDelivered_Type = Counter32
_UplaRepliesDelivered_Object = MibTableColumn
uplaRepliesDelivered = _UplaRepliesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1, 6),
    _UplaRepliesDelivered_Type()
)
uplaRepliesDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaRepliesDelivered.setStatus("deprecated")
_UplaRepliesTimedOut_Type = Counter32
_UplaRepliesTimedOut_Object = MibTableColumn
uplaRepliesTimedOut = _UplaRepliesTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 2, 1, 7),
    _UplaRepliesTimedOut_Type()
)
uplaRepliesTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaRepliesTimedOut.setStatus("deprecated")
_UplAgentTransactionStatsTable_Object = MibTable
uplAgentTransactionStatsTable = _UplAgentTransactionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    uplAgentTransactionStatsTable.setStatus("mandatory")
_UplAgentTransactionStatsEntry_Object = MibTableRow
uplAgentTransactionStatsEntry = _UplAgentTransactionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1)
)
uplAgentTransactionStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplatsAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentTransactionStatsEntry.setStatus("mandatory")
_UplatsAgentIdentifier_Type = Integer32
_UplatsAgentIdentifier_Object = MibTableColumn
uplatsAgentIdentifier = _UplatsAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 1),
    _UplatsAgentIdentifier_Type()
)
uplatsAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplatsAgentIdentifier.setStatus("mandatory")
_UplaTransactionsActive_Type = Gauge32
_UplaTransactionsActive_Object = MibTableColumn
uplaTransactionsActive = _UplaTransactionsActive_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 2),
    _UplaTransactionsActive_Type()
)
uplaTransactionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTransactionsActive.setStatus("mandatory")
_UplaTransactionsStarted_Type = Counter32
_UplaTransactionsStarted_Object = MibTableColumn
uplaTransactionsStarted = _UplaTransactionsStarted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 3),
    _UplaTransactionsStarted_Type()
)
uplaTransactionsStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTransactionsStarted.setStatus("mandatory")
_UplaTransactionsSucceeded_Type = Counter32
_UplaTransactionsSucceeded_Object = MibTableColumn
uplaTransactionsSucceeded = _UplaTransactionsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 4),
    _UplaTransactionsSucceeded_Type()
)
uplaTransactionsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTransactionsSucceeded.setStatus("mandatory")
_UplaMeanTransactionLife_Type = Integer32
_UplaMeanTransactionLife_Object = MibTableColumn
uplaMeanTransactionLife = _UplaMeanTransactionLife_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 5),
    _UplaMeanTransactionLife_Type()
)
uplaMeanTransactionLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaMeanTransactionLife.setStatus("mandatory")
_UplaDeviationOfTransactionLife_Type = Integer32
_UplaDeviationOfTransactionLife_Object = MibTableColumn
uplaDeviationOfTransactionLife = _UplaDeviationOfTransactionLife_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 6),
    _UplaDeviationOfTransactionLife_Type()
)
uplaDeviationOfTransactionLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaDeviationOfTransactionLife.setStatus("mandatory")
_UplaMeanResponseTime_Type = Integer32
_UplaMeanResponseTime_Object = MibTableColumn
uplaMeanResponseTime = _UplaMeanResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 7),
    _UplaMeanResponseTime_Type()
)
uplaMeanResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaMeanResponseTime.setStatus("mandatory")
_UplaDeviationOfResponseTime_Type = Integer32
_UplaDeviationOfResponseTime_Object = MibTableColumn
uplaDeviationOfResponseTime = _UplaDeviationOfResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 8),
    _UplaDeviationOfResponseTime_Type()
)
uplaDeviationOfResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaDeviationOfResponseTime.setStatus("mandatory")
_UplaMeanRetriesPerThousandTxn_Type = Integer32
_UplaMeanRetriesPerThousandTxn_Object = MibTableColumn
uplaMeanRetriesPerThousandTxn = _UplaMeanRetriesPerThousandTxn_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 9),
    _UplaMeanRetriesPerThousandTxn_Type()
)
uplaMeanRetriesPerThousandTxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaMeanRetriesPerThousandTxn.setStatus("mandatory")
_UplaDeviationOfRetriesPTTxn_Type = Integer32
_UplaDeviationOfRetriesPTTxn_Object = MibTableColumn
uplaDeviationOfRetriesPTTxn = _UplaDeviationOfRetriesPTTxn_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 3, 1, 10),
    _UplaDeviationOfRetriesPTTxn_Type()
)
uplaDeviationOfRetriesPTTxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaDeviationOfRetriesPTTxn.setStatus("mandatory")
_UplAgentLimitedResourceTable_Object = MibTable
uplAgentLimitedResourceTable = _UplAgentLimitedResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    uplAgentLimitedResourceTable.setStatus("deprecated")
_UplAgentLimitedResourceEntry_Object = MibTableRow
uplAgentLimitedResourceEntry = _UplAgentLimitedResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    uplAgentLimitedResourceEntry.setStatus("deprecated")
_UplaWapStats_ObjectIdentity = ObjectIdentity
uplaWapStats = _UplaWapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4)
)
_UplAgentWapWSPSessionStatsTable_Object = MibTable
uplAgentWapWSPSessionStatsTable = _UplAgentWapWSPSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    uplAgentWapWSPSessionStatsTable.setStatus("mandatory")
_UplAgentWapSessionStatsEntry_Object = MibTableRow
uplAgentWapSessionStatsEntry = _UplAgentWapSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 1, 1)
)
uplAgentWapSessionStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplawssAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentWapSessionStatsEntry.setStatus("mandatory")
_UplawssAgentIdentifier_Type = Integer32
_UplawssAgentIdentifier_Object = MibTableColumn
uplawssAgentIdentifier = _UplawssAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 1, 1, 1),
    _UplawssAgentIdentifier_Type()
)
uplawssAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplawssAgentIdentifier.setStatus("mandatory")
_UplaActiveWapSessions_Type = Gauge32
_UplaActiveWapSessions_Object = MibTableColumn
uplaActiveWapSessions = _UplaActiveWapSessions_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 1, 1, 2),
    _UplaActiveWapSessions_Type()
)
uplaActiveWapSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaActiveWapSessions.setStatus("mandatory")
_UplaWapSessionsStarted_Type = Counter32
_UplaWapSessionsStarted_Object = MibTableColumn
uplaWapSessionsStarted = _UplaWapSessionsStarted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 1, 1, 3),
    _UplaWapSessionsStarted_Type()
)
uplaWapSessionsStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapSessionsStarted.setStatus("mandatory")
_UplAgentWapWTPTransactionStatsTable_Object = MibTable
uplAgentWapWTPTransactionStatsTable = _UplAgentWapWTPTransactionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    uplAgentWapWTPTransactionStatsTable.setStatus("mandatory")
_UplAgentWapTransactionStatsEntry_Object = MibTableRow
uplAgentWapTransactionStatsEntry = _UplAgentWapTransactionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 2, 1)
)
uplAgentWapTransactionStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplawtsAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentWapTransactionStatsEntry.setStatus("mandatory")
_UplawtsAgentIdentifier_Type = Integer32
_UplawtsAgentIdentifier_Object = MibTableColumn
uplawtsAgentIdentifier = _UplawtsAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 2, 1, 1),
    _UplawtsAgentIdentifier_Type()
)
uplawtsAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplawtsAgentIdentifier.setStatus("mandatory")
_UplaWapInvokeTpdus_Type = Gauge32
_UplaWapInvokeTpdus_Object = MibTableColumn
uplaWapInvokeTpdus = _UplaWapInvokeTpdus_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 2, 1, 2),
    _UplaWapInvokeTpdus_Type()
)
uplaWapInvokeTpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapInvokeTpdus.setStatus("mandatory")
_UplaWapResultTpdus_Type = Counter32
_UplaWapResultTpdus_Object = MibTableColumn
uplaWapResultTpdus = _UplaWapResultTpdus_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 2, 1, 3),
    _UplaWapResultTpdus_Type()
)
uplaWapResultTpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapResultTpdus.setStatus("mandatory")
_UplaWapAbortTransaction_Type = Counter32
_UplaWapAbortTransaction_Object = MibTableColumn
uplaWapAbortTransaction = _UplaWapAbortTransaction_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 2, 1, 4),
    _UplaWapAbortTransaction_Type()
)
uplaWapAbortTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapAbortTransaction.setStatus("mandatory")
_UplAgentWapErrorStatsSummaryTable_Object = MibTable
uplAgentWapErrorStatsSummaryTable = _UplAgentWapErrorStatsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    uplAgentWapErrorStatsSummaryTable.setStatus("mandatory")
_UplAgentWapErrorStatsSummaryEntry_Object = MibTableRow
uplAgentWapErrorStatsSummaryEntry = _UplAgentWapErrorStatsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 3, 1)
)
uplAgentWapErrorStatsSummaryEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplawesAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentWapErrorStatsSummaryEntry.setStatus("mandatory")
_UplawesAgentIdentifier_Type = Integer32
_UplawesAgentIdentifier_Object = MibTableColumn
uplawesAgentIdentifier = _UplawesAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 3, 1, 1),
    _UplawesAgentIdentifier_Type()
)
uplawesAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplawesAgentIdentifier.setStatus("mandatory")
_UplaTotalWapErrors_Type = Counter32
_UplaTotalWapErrors_Object = MibTableColumn
uplaTotalWapErrors = _UplaTotalWapErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 3, 1, 2),
    _UplaTotalWapErrors_Type()
)
uplaTotalWapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTotalWapErrors.setStatus("mandatory")
_UplaOtherWapErrors_Type = Counter32
_UplaOtherWapErrors_Object = MibTableColumn
uplaOtherWapErrors = _UplaOtherWapErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 3, 1, 3),
    _UplaOtherWapErrors_Type()
)
uplaOtherWapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaOtherWapErrors.setStatus("mandatory")
_UplaSessionWapErrors_Type = Counter32
_UplaSessionWapErrors_Object = MibTableColumn
uplaSessionWapErrors = _UplaSessionWapErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 3, 1, 4),
    _UplaSessionWapErrors_Type()
)
uplaSessionWapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaSessionWapErrors.setStatus("mandatory")
_UplaTransactionWapErrors_Type = Counter32
_UplaTransactionWapErrors_Object = MibTableColumn
uplaTransactionWapErrors = _UplaTransactionWapErrors_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 3, 1, 5),
    _UplaTransactionWapErrors_Type()
)
uplaTransactionWapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTransactionWapErrors.setStatus("mandatory")
_UplAgentWapErrorStatsDetailTable_Object = MibTable
uplAgentWapErrorStatsDetailTable = _UplAgentWapErrorStatsDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    uplAgentWapErrorStatsDetailTable.setStatus("mandatory")
_UplAgentWapErrorStatsDetailEntry_Object = MibTableRow
uplAgentWapErrorStatsDetailEntry = _UplAgentWapErrorStatsDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4, 1)
)
uplAgentWapErrorStatsDetailEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplaweAgentIdentifier"),
    (0, "UPPHONEDOTCOM-MIB", "uplaWapErrorCode"),
)
if mibBuilder.loadTexts:
    uplAgentWapErrorStatsDetailEntry.setStatus("mandatory")
_UplaweAgentIdentifier_Type = Integer32
_UplaweAgentIdentifier_Object = MibTableColumn
uplaweAgentIdentifier = _UplaweAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4, 1, 1),
    _UplaweAgentIdentifier_Type()
)
uplaweAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaweAgentIdentifier.setStatus("mandatory")
_UplaWapErrorCode_Type = Integer32
_UplaWapErrorCode_Object = MibTableColumn
uplaWapErrorCode = _UplaWapErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4, 1, 2),
    _UplaWapErrorCode_Type()
)
uplaWapErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapErrorCode.setStatus("mandatory")
_UplaWapErrorName_Type = DisplayString
_UplaWapErrorName_Object = MibTableColumn
uplaWapErrorName = _UplaWapErrorName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4, 1, 3),
    _UplaWapErrorName_Type()
)
uplaWapErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapErrorName.setStatus("mandatory")
_UplaWapErrorSeverity_Type = Integer32
_UplaWapErrorSeverity_Object = MibTableColumn
uplaWapErrorSeverity = _UplaWapErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4, 1, 4),
    _UplaWapErrorSeverity_Type()
)
uplaWapErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapErrorSeverity.setStatus("optional")


class _UplaWapErrorClass_Type(Integer32):
    """Custom type uplaWapErrorClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("session", 2),
          ("txn", 3))
    )


_UplaWapErrorClass_Type.__name__ = "Integer32"
_UplaWapErrorClass_Object = MibTableColumn
uplaWapErrorClass = _UplaWapErrorClass_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4, 1, 5),
    _UplaWapErrorClass_Type()
)
uplaWapErrorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapErrorClass.setStatus("mandatory")
_UplaWapErrorCount_Type = Counter32
_UplaWapErrorCount_Object = MibTableColumn
uplaWapErrorCount = _UplaWapErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 4, 4, 1, 6),
    _UplaWapErrorCount_Type()
)
uplaWapErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaWapErrorCount.setStatus("mandatory")
_UplaStackServiceStats_ObjectIdentity = ObjectIdentity
uplaStackServiceStats = _UplaStackServiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5)
)
_UplAgentStackServiceTable_Object = MibTable
uplAgentStackServiceTable = _UplAgentStackServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    uplAgentStackServiceTable.setStatus("mandatory")
_UplAgentStackServiceEntry_Object = MibTableRow
uplAgentStackServiceEntry = _UplAgentStackServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1)
)
uplAgentStackServiceEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplasstAgentIdentifier"),
    (0, "UPPHONEDOTCOM-MIB", "uplAgentStackServiceIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentStackServiceEntry.setStatus("mandatory")
_UplasstAgentIdentifier_Type = Integer32
_UplasstAgentIdentifier_Object = MibTableColumn
uplasstAgentIdentifier = _UplasstAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 1),
    _UplasstAgentIdentifier_Type()
)
uplasstAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplasstAgentIdentifier.setStatus("mandatory")
_UplAgentStackServiceIdentifier_Type = Integer32
_UplAgentStackServiceIdentifier_Object = MibTableColumn
uplAgentStackServiceIdentifier = _UplAgentStackServiceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 2),
    _UplAgentStackServiceIdentifier_Type()
)
uplAgentStackServiceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceIdentifier.setStatus("mandatory")
_UplAgentStackServiceAppProtoName_Type = DisplayString
_UplAgentStackServiceAppProtoName_Object = MibTableColumn
uplAgentStackServiceAppProtoName = _UplAgentStackServiceAppProtoName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 3),
    _UplAgentStackServiceAppProtoName_Type()
)
uplAgentStackServiceAppProtoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceAppProtoName.setStatus("mandatory")
_UplAgentStackServiceName_Type = DisplayString
_UplAgentStackServiceName_Object = MibTableColumn
uplAgentStackServiceName = _UplAgentStackServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 4),
    _UplAgentStackServiceName_Type()
)
uplAgentStackServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceName.setStatus("mandatory")


class _UplAgentStackServiceLoaded_Type(Integer32):
    """Custom type uplAgentStackServiceLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 2),
          ("notloaded", 1))
    )


_UplAgentStackServiceLoaded_Type.__name__ = "Integer32"
_UplAgentStackServiceLoaded_Object = MibTableColumn
uplAgentStackServiceLoaded = _UplAgentStackServiceLoaded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 5),
    _UplAgentStackServiceLoaded_Type()
)
uplAgentStackServiceLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceLoaded.setStatus("mandatory")
_UplAgentStackServiceAdaptorThreads_Type = Integer32
_UplAgentStackServiceAdaptorThreads_Object = MibTableColumn
uplAgentStackServiceAdaptorThreads = _UplAgentStackServiceAdaptorThreads_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 6),
    _UplAgentStackServiceAdaptorThreads_Type()
)
uplAgentStackServiceAdaptorThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceAdaptorThreads.setStatus("mandatory")
_UplAgentStackServiceWDPPortNumber_Type = Integer32
_UplAgentStackServiceWDPPortNumber_Object = MibTableColumn
uplAgentStackServiceWDPPortNumber = _UplAgentStackServiceWDPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 7),
    _UplAgentStackServiceWDPPortNumber_Type()
)
uplAgentStackServiceWDPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceWDPPortNumber.setStatus("mandatory")
_UplAgentTrapInfo_ObjectIdentity = ObjectIdentity
uplAgentTrapInfo = _UplAgentTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 20)
)
_UplaTrapInfo_Type = DisplayString
_UplaTrapInfo_Object = MibScalar
uplaTrapInfo = _UplaTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 20, 1),
    _UplaTrapInfo_Type()
)
uplaTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplaTrapInfo.setStatus("optional")
_UplNbRouter_ObjectIdentity = ObjectIdentity
uplNbRouter = _UplNbRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3)
)
_UplNbRouterDescriptionTable_Object = MibTable
uplNbRouterDescriptionTable = _UplNbRouterDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    uplNbRouterDescriptionTable.setStatus("mandatory")
_UplNbRouterDescriptionEntry_Object = MibTableRow
uplNbRouterDescriptionEntry = _UplNbRouterDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 1, 1)
)
uplNbRouterDescriptionEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplrdIpAddress"),
    (0, "UPPHONEDOTCOM-MIB", "uplrdProcessId"),
)
if mibBuilder.loadTexts:
    uplNbRouterDescriptionEntry.setStatus("mandatory")
_UplrdIpAddress_Type = IpAddress
_UplrdIpAddress_Object = MibTableColumn
uplrdIpAddress = _UplrdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 1, 1, 1),
    _UplrdIpAddress_Type()
)
uplrdIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrdIpAddress.setStatus("mandatory")
_UplrdProcessId_Type = Integer32
_UplrdProcessId_Object = MibTableColumn
uplrdProcessId = _UplrdProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 1, 1, 2),
    _UplrdProcessId_Type()
)
uplrdProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrdProcessId.setStatus("mandatory")
_UplrdHostName_Type = DisplayString
_UplrdHostName_Object = MibTableColumn
uplrdHostName = _UplrdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 1, 1, 3),
    _UplrdHostName_Type()
)
uplrdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrdHostName.setStatus("mandatory")
_UplrdPortNumber_Type = Integer32
_UplrdPortNumber_Object = MibTableColumn
uplrdPortNumber = _UplrdPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 1, 1, 4),
    _UplrdPortNumber_Type()
)
uplrdPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrdPortNumber.setStatus("mandatory")
_UplrdStartUpTime_Type = DisplayString
_UplrdStartUpTime_Object = MibTableColumn
uplrdStartUpTime = _UplrdStartUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 1, 1, 5),
    _UplrdStartUpTime_Type()
)
uplrdStartUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrdStartUpTime.setStatus("mandatory")
_UplrHdtpStats_ObjectIdentity = ObjectIdentity
uplrHdtpStats = _UplrHdtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 2)
)
_UplNbRouterAirlinkTable_Object = MibTable
uplNbRouterAirlinkTable = _UplNbRouterAirlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    uplNbRouterAirlinkTable.setStatus("deprecated")
_UplNbRouterAirlinkEntry_Object = MibTableRow
uplNbRouterAirlinkEntry = _UplNbRouterAirlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    uplNbRouterAirlinkEntry.setStatus("deprecated")
_UplNbRouterAirlinkStatsTable_Object = MibTable
uplNbRouterAirlinkStatsTable = _UplNbRouterAirlinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    uplNbRouterAirlinkStatsTable.setStatus("deprecated")
_UplNbRouterAirlinkStatsEntry_Object = MibTableRow
uplNbRouterAirlinkStatsEntry = _UplNbRouterAirlinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    uplNbRouterAirlinkStatsEntry.setStatus("deprecated")
_UplrStackServiceStats_ObjectIdentity = ObjectIdentity
uplrStackServiceStats = _UplrStackServiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 3)
)
_UplNbRouterTrapInfo_ObjectIdentity = ObjectIdentity
uplNbRouterTrapInfo = _UplNbRouterTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 20)
)
_UplrTrapInfo_Type = DisplayString
_UplrTrapInfo_Object = MibScalar
uplrTrapInfo = _UplrTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 20, 1),
    _UplrTrapInfo_Type()
)
uplrTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplrTrapInfo.setStatus("optional")
_UplrClientIpAddress_Type = IpAddress
_UplrClientIpAddress_Object = MibScalar
uplrClientIpAddress = _UplrClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 20, 2),
    _UplrClientIpAddress_Type()
)
uplrClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrClientIpAddress.setStatus("mandatory")
_UplrClientHostName_Type = DisplayString
_UplrClientHostName_Object = MibScalar
uplrClientHostName = _UplrClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 20, 3),
    _UplrClientHostName_Type()
)
uplrClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrClientHostName.setStatus("mandatory")
_UplrClientProcessId_Type = Integer32
_UplrClientProcessId_Object = MibScalar
uplrClientProcessId = _UplrClientProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 20, 4),
    _UplrClientProcessId_Type()
)
uplrClientProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrClientProcessId.setStatus("mandatory")
_UplMessenger_ObjectIdentity = ObjectIdentity
uplMessenger = _UplMessenger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4)
)
_UplMessengerDescriptionTable_Object = MibTable
uplMessengerDescriptionTable = _UplMessengerDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    uplMessengerDescriptionTable.setStatus("mandatory")
_UplMessengerDescriptionEntry_Object = MibTableRow
uplMessengerDescriptionEntry = _UplMessengerDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1)
)
uplMessengerDescriptionEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
    (0, "UPPHONEDOTCOM-MIB", "uplmdProcessId"),
)
if mibBuilder.loadTexts:
    uplMessengerDescriptionEntry.setStatus("mandatory")
_UplmdIpAddress_Type = IpAddress
_UplmdIpAddress_Object = MibTableColumn
uplmdIpAddress = _UplmdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 1),
    _UplmdIpAddress_Type()
)
uplmdIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdIpAddress.setStatus("mandatory")
_UplmdProcessId_Type = Integer32
_UplmdProcessId_Object = MibTableColumn
uplmdProcessId = _UplmdProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 2),
    _UplmdProcessId_Type()
)
uplmdProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdProcessId.setStatus("mandatory")
_UplmdHostName_Type = DisplayString
_UplmdHostName_Object = MibTableColumn
uplmdHostName = _UplmdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 3),
    _UplmdHostName_Type()
)
uplmdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdHostName.setStatus("mandatory")
_UplmdMsgServerPortNumber_Type = Integer32
_UplmdMsgServerPortNumber_Object = MibTableColumn
uplmdMsgServerPortNumber = _UplmdMsgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 4),
    _UplmdMsgServerPortNumber_Type()
)
uplmdMsgServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdMsgServerPortNumber.setStatus("mandatory")
_UplmdPublicHTTPPortNumber_Type = Integer32
_UplmdPublicHTTPPortNumber_Object = MibTableColumn
uplmdPublicHTTPPortNumber = _UplmdPublicHTTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 5),
    _UplmdPublicHTTPPortNumber_Type()
)
uplmdPublicHTTPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdPublicHTTPPortNumber.setStatus("mandatory")
_UplmdPublicHTTPSPortNumber_Type = Integer32
_UplmdPublicHTTPSPortNumber_Object = MibTableColumn
uplmdPublicHTTPSPortNumber = _UplmdPublicHTTPSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 6),
    _UplmdPublicHTTPSPortNumber_Type()
)
uplmdPublicHTTPSPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdPublicHTTPSPortNumber.setStatus("mandatory")
_UplmdPrivateHTTPPortNumber_Type = Integer32
_UplmdPrivateHTTPPortNumber_Object = MibTableColumn
uplmdPrivateHTTPPortNumber = _UplmdPrivateHTTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 7),
    _UplmdPrivateHTTPPortNumber_Type()
)
uplmdPrivateHTTPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdPrivateHTTPPortNumber.setStatus("mandatory")
_UplmdStartupTime_Type = DisplayString
_UplmdStartupTime_Object = MibTableColumn
uplmdStartupTime = _UplmdStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 8),
    _UplmdStartupTime_Type()
)
uplmdStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdStartupTime.setStatus("mandatory")
_UplmHdtpStats_ObjectIdentity = ObjectIdentity
uplmHdtpStats = _UplmHdtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2)
)
_UplMessengerAirlinkTable_Object = MibTable
uplMessengerAirlinkTable = _UplMessengerAirlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    uplMessengerAirlinkTable.setStatus("deprecated")
_UplMessengerAirlinkEntry_Object = MibTableRow
uplMessengerAirlinkEntry = _UplMessengerAirlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    uplMessengerAirlinkEntry.setStatus("deprecated")
_UplMessengerAirlinkStatsTable_Object = MibTable
uplMessengerAirlinkStatsTable = _UplMessengerAirlinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    uplMessengerAirlinkStatsTable.setStatus("deprecated")
_UplMessengerAirlinkStatsEntry_Object = MibTableRow
uplMessengerAirlinkStatsEntry = _UplMessengerAirlinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    uplMessengerAirlinkStatsEntry.setStatus("deprecated")
_UplmStackServiceStats_ObjectIdentity = ObjectIdentity
uplmStackServiceStats = _UplmStackServiceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 3)
)
_UplMessengerNtfnStatsTable_Object = MibTable
uplMessengerNtfnStatsTable = _UplMessengerNtfnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    uplMessengerNtfnStatsTable.setStatus("mandatory")
_UplMessengerNtfnStatsEntry_Object = MibTableRow
uplMessengerNtfnStatsEntry = _UplMessengerNtfnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1)
)
uplMessengerNtfnStatsEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplmnsIpAddress"),
    (0, "UPPHONEDOTCOM-MIB", "uplmnsProcessId"),
)
if mibBuilder.loadTexts:
    uplMessengerNtfnStatsEntry.setStatus("mandatory")
_UplmnsIpAddress_Type = IpAddress
_UplmnsIpAddress_Object = MibTableColumn
uplmnsIpAddress = _UplmnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 1),
    _UplmnsIpAddress_Type()
)
uplmnsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsIpAddress.setStatus("mandatory")
_UplmnsProcessId_Type = Integer32
_UplmnsProcessId_Object = MibTableColumn
uplmnsProcessId = _UplmnsProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 2),
    _UplmnsProcessId_Type()
)
uplmnsProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsProcessId.setStatus("mandatory")
_UplmnsPublicHTTPReqReceived_Type = Counter32
_UplmnsPublicHTTPReqReceived_Object = MibTableColumn
uplmnsPublicHTTPReqReceived = _UplmnsPublicHTTPReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 3),
    _UplmnsPublicHTTPReqReceived_Type()
)
uplmnsPublicHTTPReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsPublicHTTPReqReceived.setStatus("mandatory")
_UplmnsPrivateHTTPReqReceived_Type = Counter32
_UplmnsPrivateHTTPReqReceived_Object = MibTableColumn
uplmnsPrivateHTTPReqReceived = _UplmnsPrivateHTTPReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 4),
    _UplmnsPrivateHTTPReqReceived_Type()
)
uplmnsPrivateHTTPReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsPrivateHTTPReqReceived.setStatus("mandatory")
_UplmnsPublicHTTPSReqReceived_Type = Counter32
_UplmnsPublicHTTPSReqReceived_Object = MibTableColumn
uplmnsPublicHTTPSReqReceived = _UplmnsPublicHTTPSReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 5),
    _UplmnsPublicHTTPSReqReceived_Type()
)
uplmnsPublicHTTPSReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsPublicHTTPSReqReceived.setStatus("mandatory")
_UplmnsPublicHTTPReqProcessed_Type = Counter32
_UplmnsPublicHTTPReqProcessed_Object = MibTableColumn
uplmnsPublicHTTPReqProcessed = _UplmnsPublicHTTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 6),
    _UplmnsPublicHTTPReqProcessed_Type()
)
uplmnsPublicHTTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsPublicHTTPReqProcessed.setStatus("mandatory")
_UplmnsPrivateHTTPReqProcessed_Type = Counter32
_UplmnsPrivateHTTPReqProcessed_Object = MibTableColumn
uplmnsPrivateHTTPReqProcessed = _UplmnsPrivateHTTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 7),
    _UplmnsPrivateHTTPReqProcessed_Type()
)
uplmnsPrivateHTTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsPrivateHTTPReqProcessed.setStatus("mandatory")
_UplmnsPublicHTTPSReqProcessed_Type = Counter32
_UplmnsPublicHTTPSReqProcessed_Object = MibTableColumn
uplmnsPublicHTTPSReqProcessed = _UplmnsPublicHTTPSReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 8),
    _UplmnsPublicHTTPSReqProcessed_Type()
)
uplmnsPublicHTTPSReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsPublicHTTPSReqProcessed.setStatus("mandatory")
_UplmnsAvgNtfnsAddedPerSec_Type = Integer32
_UplmnsAvgNtfnsAddedPerSec_Object = MibTableColumn
uplmnsAvgNtfnsAddedPerSec = _UplmnsAvgNtfnsAddedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 9),
    _UplmnsAvgNtfnsAddedPerSec_Type()
)
uplmnsAvgNtfnsAddedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsAvgNtfnsAddedPerSec.setStatus("mandatory")
_UplmnsAvgNtfnsDeliveredPerSec_Type = Integer32
_UplmnsAvgNtfnsDeliveredPerSec_Object = MibTableColumn
uplmnsAvgNtfnsDeliveredPerSec = _UplmnsAvgNtfnsDeliveredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 10),
    _UplmnsAvgNtfnsDeliveredPerSec_Type()
)
uplmnsAvgNtfnsDeliveredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsAvgNtfnsDeliveredPerSec.setStatus("mandatory")
_UplmnsAvgNtfnsExpiredPerSec_Type = Integer32
_UplmnsAvgNtfnsExpiredPerSec_Object = MibTableColumn
uplmnsAvgNtfnsExpiredPerSec = _UplmnsAvgNtfnsExpiredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 11),
    _UplmnsAvgNtfnsExpiredPerSec_Type()
)
uplmnsAvgNtfnsExpiredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsAvgNtfnsExpiredPerSec.setStatus("mandatory")
_UplmnsAvgNtfnsMarkedUnDelvrPerSec_Type = Integer32
_UplmnsAvgNtfnsMarkedUnDelvrPerSec_Object = MibTableColumn
uplmnsAvgNtfnsMarkedUnDelvrPerSec = _UplmnsAvgNtfnsMarkedUnDelvrPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 12),
    _UplmnsAvgNtfnsMarkedUnDelvrPerSec_Type()
)
uplmnsAvgNtfnsMarkedUnDelvrPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsAvgNtfnsMarkedUnDelvrPerSec.setStatus("mandatory")
_UplMessengerNtfnCacheTable_Object = MibTable
uplMessengerNtfnCacheTable = _UplMessengerNtfnCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    uplMessengerNtfnCacheTable.setStatus("mandatory")
_UplMessengerNtfnCacheEntry_Object = MibTableRow
uplMessengerNtfnCacheEntry = _UplMessengerNtfnCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 5, 1)
)
uplMessengerNtfnCacheEntry.setIndexNames(
    (0, "UPPHONEDOTCOM-MIB", "uplmncIpAddress"),
    (0, "UPPHONEDOTCOM-MIB", "uplmncProcessId"),
)
if mibBuilder.loadTexts:
    uplMessengerNtfnCacheEntry.setStatus("mandatory")
_UplmncIpAddress_Type = IpAddress
_UplmncIpAddress_Object = MibTableColumn
uplmncIpAddress = _UplmncIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 5, 1, 1),
    _UplmncIpAddress_Type()
)
uplmncIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmncIpAddress.setStatus("mandatory")
_UplmncProcessId_Type = Integer32
_UplmncProcessId_Object = MibTableColumn
uplmncProcessId = _UplmncProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 5, 1, 2),
    _UplmncProcessId_Type()
)
uplmncProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmncProcessId.setStatus("mandatory")
_UplmncTotalNumOfPendingNtfns_Type = Counter32
_UplmncTotalNumOfPendingNtfns_Object = MibTableColumn
uplmncTotalNumOfPendingNtfns = _UplmncTotalNumOfPendingNtfns_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 5, 1, 3),
    _UplmncTotalNumOfPendingNtfns_Type()
)
uplmncTotalNumOfPendingNtfns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmncTotalNumOfPendingNtfns.setStatus("mandatory")
_UplmncAvgNumOfPendingNtfnsPerSub_Type = Integer32
_UplmncAvgNumOfPendingNtfnsPerSub_Object = MibTableColumn
uplmncAvgNumOfPendingNtfnsPerSub = _UplmncAvgNumOfPendingNtfnsPerSub_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 5, 1, 4),
    _UplmncAvgNumOfPendingNtfnsPerSub_Type()
)
uplmncAvgNumOfPendingNtfnsPerSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmncAvgNumOfPendingNtfnsPerSub.setStatus("mandatory")
_UplMessengerTrapInfo_ObjectIdentity = ObjectIdentity
uplMessengerTrapInfo = _UplMessengerTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 20)
)
_UplmTrapInfo_Type = DisplayString
_UplmTrapInfo_Object = MibScalar
uplmTrapInfo = _UplmTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 20, 1),
    _UplmTrapInfo_Type()
)
uplmTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplmTrapInfo.setStatus("optional")
_UpLinkConfig_ObjectIdentity = ObjectIdentity
upLinkConfig = _UpLinkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 2)
)
_UpLinkStaticInfo_ObjectIdentity = ObjectIdentity
upLinkStaticInfo = _UpLinkStaticInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 2, 1)
)
_UpAdmin_ObjectIdentity = ObjectIdentity
upAdmin = _UpAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3)
)
_UpAdminTrapInfo_ObjectIdentity = ObjectIdentity
upAdminTrapInfo = _UpAdminTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 20)
)
_UpsTrapInfo_Type = DisplayString
_UpsTrapInfo_Object = MibScalar
upsTrapInfo = _UpsTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 20, 1),
    _UpsTrapInfo_Type()
)
upsTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsTrapInfo.setStatus("optional")
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 5)
)
_UpMail_ObjectIdentity = ObjectIdentity
upMail = _UpMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 5, 1)
)

# Managed Objects groups


# Notification objects

upiChildProcessStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 300)
)
upiChildProcessStart.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessHostName"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessType"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessStart.setStatus(
        ""
    )

upiChildProcessShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 301)
)
upiChildProcessShutdown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessHostName"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessType"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessShutdown.setStatus(
        ""
    )

upiInitFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 302)
)
upiInitFailToStart.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiInitFailToStart.setStatus(
        ""
    )

upiInitShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 303)
)
upiInitShutdown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiInitShutdown.setStatus(
        ""
    )

upiAllChildProcessesStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 304)
)
upiAllChildProcessesStop.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiAllChildProcessesStop.setStatus(
        ""
    )

upiAllChildProcessesRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 305)
)
upiAllChildProcessesRestart.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiAllChildProcessesRestart.setStatus(
        ""
    )

upiDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 306)
)
upiDatabaseConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiDatabaseConnectionDown.setStatus(
        ""
    )

upiDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 307)
)
upiDatabaseConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiDatabaseConnectionUp.setStatus(
        ""
    )

upiChildProcessFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 308)
)
upiChildProcessFailToStart.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessType"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessFailToStart.setStatus(
        ""
    )

upiNoChildProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 309)
)
upiNoChildProcess.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiNoChildProcess.setStatus(
        ""
    )

upiChildProcessesBelowMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 310)
)
upiChildProcessesBelowMinimum.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upidInitHostName"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessType"),
        ("UPPHONEDOTCOM-MIB", "upidInitProcessId"),
        ("UPPHONEDOTCOM-MIB", "upitChildProcessType"),
        ("UPPHONEDOTCOM-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessesBelowMinimum.setStatus(
        ""
    )

upldStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 100)
)
upldStartup.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldStartup.setStatus(
        ""
    )

upldShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 101)
)
upldShutdown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldShutdown.setStatus(
        ""
    )

upldInvalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 102)
)
upldInvalidConfig.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldInvalidConfig.setStatus(
        ""
    )

upldUplAgentConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 103)
)
upldUplAgentConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldUplAgentId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldUplAgentConnectionDown.setStatus(
        ""
    )

upldDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 104)
)
upldDatabaseConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldDatabaseConnectionDown.setStatus(
        ""
    )

upldOutOfResouce = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 105)
)
upldOutOfResouce.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldOutOfResouce.setStatus(
        ""
    )

upldUplAgentConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 106)
)
upldUplAgentConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldUplAgentId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldUplAgentConnectionUp.setStatus(
        ""
    )

upldDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 107)
)
upldDatabaseConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "upldHostName"),
        ("UPPHONEDOTCOM-MIB", "upldProcessId"),
        ("UPPHONEDOTCOM-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldDatabaseConnectionUp.setStatus(
        ""
    )

uplaStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 200)
)
uplaStartup.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaStartup.setStatus(
        ""
    )

uplaShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 201)
)
uplaShutdown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaShutdown.setStatus(
        ""
    )

uplaDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 202)
)
uplaDatabaseConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaDatabaseConnectionDown.setStatus(
        ""
    )

uplaFaxMgrConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 203)
)
uplaFaxMgrConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaFaxMgrConnectionDown.setStatus(
        ""
    )

uplaMessengerConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 204)
)
uplaMessengerConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaMessengerConnectionDown.setStatus(
        ""
    )

uplaInvalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 205)
)
uplaInvalidConfig.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaInvalidConfig.setStatus(
        ""
    )

uplaInternalFatalErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 206)
)
uplaInternalFatalErrors.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaInternalFatalErrors.setStatus(
        ""
    )

uplaOutOfResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 207)
)
uplaOutOfResource.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaOutOfResource.setStatus(
        ""
    )

uplaDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 208)
)
uplaDatabaseConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplaAgentIdentifier"),
        ("UPPHONEDOTCOM-MIB", "uplaHostName"),
        ("UPPHONEDOTCOM-MIB", "uplaProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaDatabaseConnectionUp.setStatus(
        ""
    )

uplrStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 500)
)
uplrStartup.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrStartup.setStatus(
        ""
    )

uplrShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 501)
)
uplrShutdown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrShutdown.setStatus(
        ""
    )

uplrDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 502)
)
uplrDatabaseConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrDatabaseConnectionDown.setStatus(
        ""
    )

uplrDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 503)
)
uplrDatabaseConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrDatabaseConnectionUp.setStatus(
        ""
    )

uplrInvalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 504)
)
uplrInvalidConfig.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrInvalidConfig.setStatus(
        ""
    )

uplrInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 505)
)
uplrInternalError.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrInternalError.setStatus(
        ""
    )

uplrSMSCConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 506)
)
uplrSMSCConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrSMSCConnectionDown.setStatus(
        ""
    )

uplrSMSCConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 507)
)
uplrSMSCConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrSMSCConnectionUp.setStatus(
        ""
    )

uplrClientConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 508)
)
uplrClientConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrClientConnectionDown.setStatus(
        ""
    )

uplrClientConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 509)
)
uplrClientConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrClientConnectionUp.setStatus(
        ""
    )

uplrNbRouterConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 510)
)
uplrNbRouterConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrClientIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplrClientHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrClientProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrNbRouterConnectionDown.setStatus(
        ""
    )

uplrNbRouterConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 511)
)
uplrNbRouterConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrClientIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplrClientHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrClientProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrNbRouterConnectionUp.setStatus(
        ""
    )

uplrProtocolError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 512)
)
uplrProtocolError.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplrClientIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplrClientHostName"),
        ("UPPHONEDOTCOM-MIB", "uplrClientProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrProtocolError.setStatus(
        ""
    )

uplmStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 600)
)
uplmStartup.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmStartup.setStatus(
        ""
    )

uplmShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 601)
)
uplmShutdown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmShutdown.setStatus(
        ""
    )

uplmDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 602)
)
uplmDatabaseConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmDatabaseConnectionDown.setStatus(
        ""
    )

uplmDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 603)
)
uplmDatabaseConnectionUp.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmDatabaseConnectionUp.setStatus(
        ""
    )

uplmInvalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 604)
)
uplmInvalidConfig.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmInvalidConfig.setStatus(
        ""
    )

uplmInternalErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 605)
)
uplmInternalErrors.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmInternalErrors.setStatus(
        ""
    )

uplmAgentConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 606)
)
uplmAgentConnectionDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmAgentConnectionDown.setStatus(
        ""
    )

uplmPublicHTTPServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 607)
)
uplmPublicHTTPServiceStarted.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPublicHTTPServiceStarted.setStatus(
        ""
    )

uplmPublicHTTPServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 608)
)
uplmPublicHTTPServiceDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPublicHTTPServiceDown.setStatus(
        ""
    )

uplmPrivateHTTPServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 609)
)
uplmPrivateHTTPServiceDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPrivateHTTPServiceDown.setStatus(
        ""
    )

uplmPublicHTTPSServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 610)
)
uplmPublicHTTPSServiceDown.setObjects(
      *(("UPPHONEDOTCOM-MIB", "uplmdIpAddress"),
        ("UPPHONEDOTCOM-MIB", "uplmdHostName"),
        ("UPPHONEDOTCOM-MIB", "uplmdProcessId"),
        ("UPPHONEDOTCOM-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPublicHTTPSServiceDown.setStatus(
        ""
    )

upsProxyServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 400)
)
upsProxyServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceDown.setStatus(
        ""
    )

upsProxyServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 401)
)
upsProxyServiceSlow.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceSlow.setStatus(
        ""
    )

upsPushServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 402)
)
upsPushServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsPushServiceDown.setStatus(
        ""
    )

upsBookmarksServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 403)
)
upsBookmarksServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceDown.setStatus(
        ""
    )

upsBookmarksServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 404)
)
upsBookmarksServiceSlow.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceSlow.setStatus(
        ""
    )

upsHomePageServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 405)
)
upsHomePageServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsHomePageServiceDown.setStatus(
        ""
    )

upsUPWebServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 406)
)
upsUPWebServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceDown.setStatus(
        ""
    )

upsUPWebServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 407)
)
upsUPWebServiceSlow.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceSlow.setStatus(
        ""
    )

upsUPAdminServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 408)
)
upsUPAdminServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPAdminServiceDown.setStatus(
        ""
    )

upsUPMailServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 409)
)
upsUPMailServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceDown.setStatus(
        ""
    )

upsUPMailServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 410)
)
upsUPMailServiceSlow.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceSlow.setStatus(
        ""
    )

upsUPPimServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 411)
)
upsUPPimServiceDown.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceDown.setStatus(
        ""
    )

upsUPPimServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 412)
)
upsUPPimServiceSlow.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceSlow.setStatus(
        ""
    )

upsHomePageServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 413)
)
upsHomePageServiceSlow.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsHomePageServiceSlow.setStatus(
        ""
    )

upsProxyServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 414)
)
upsProxyServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceUp.setStatus(
        ""
    )

upsProxyServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 415)
)
upsProxyServiceNormal.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceNormal.setStatus(
        ""
    )

upsPushServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 416)
)
upsPushServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsPushServiceUp.setStatus(
        ""
    )

upsBookmarksServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 417)
)
upsBookmarksServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceUp.setStatus(
        ""
    )

upsBookmarksServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 418)
)
upsBookmarksServiceNormal.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceNormal.setStatus(
        ""
    )

upsHomePageServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 419)
)
upsHomePageServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsHomePageServiceUp.setStatus(
        ""
    )

upsUPWebServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 420)
)
upsUPWebServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceUp.setStatus(
        ""
    )

upsUPWebServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 421)
)
upsUPWebServiceNormal.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceNormal.setStatus(
        ""
    )

upsUPAdminServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 422)
)
upsUPAdminServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPAdminServiceUp.setStatus(
        ""
    )

upsUPMailServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 423)
)
upsUPMailServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceUp.setStatus(
        ""
    )

upsUPMailServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 424)
)
upsUPMailServiceNormal.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceNormal.setStatus(
        ""
    )

upsUPPimServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 425)
)
upsUPPimServiceUp.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceUp.setStatus(
        ""
    )

upsUPPimServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 426)
)
upsUPPimServiceNormal.setObjects(
    ("UPPHONEDOTCOM-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceNormal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UPPHONEDOTCOM-MIB",
    **{"phoneDotCom": phoneDotCom,
       "systems": systems,
       "upiInit": upiInit,
       "upiChildProcessStart": upiChildProcessStart,
       "upiChildProcessShutdown": upiChildProcessShutdown,
       "upiInitFailToStart": upiInitFailToStart,
       "upiInitShutdown": upiInitShutdown,
       "upiAllChildProcessesStop": upiAllChildProcessesStop,
       "upiAllChildProcessesRestart": upiAllChildProcessesRestart,
       "upiDatabaseConnectionDown": upiDatabaseConnectionDown,
       "upiDatabaseConnectionUp": upiDatabaseConnectionUp,
       "upiChildProcessFailToStart": upiChildProcessFailToStart,
       "upiNoChildProcess": upiNoChildProcess,
       "upiChildProcessesBelowMinimum": upiChildProcessesBelowMinimum,
       "upiInitDescriptionTable": upiInitDescriptionTable,
       "upiInitDescriptionEntry": upiInitDescriptionEntry,
       "upidInitIpAddr": upidInitIpAddr,
       "upidInitProcessId": upidInitProcessId,
       "upidInitVersion": upidInitVersion,
       "upidInitProcessType": upidInitProcessType,
       "upidInitHostName": upidInitHostName,
       "upidInitStartupTime": upidInitStartupTime,
       "upiInitStats": upiInitStats,
       "upiInitChildProcessTable": upiInitChildProcessTable,
       "upiInitChildProcessEntry": upiInitChildProcessEntry,
       "upipInitIpAddr": upipInitIpAddr,
       "upipInitProcessType": upipInitProcessType,
       "upipInitProcessId": upipInitProcessId,
       "upipChildProcessId": upipChildProcessId,
       "upipChildProcessType": upipChildProcessType,
       "upipChildProcessIpAddr": upipChildProcessIpAddr,
       "upipChildProcessHostName": upipChildProcessHostName,
       "upipChildProcessExePath": upipChildProcessExePath,
       "upipChildProcessExeArgs": upipChildProcessExeArgs,
       "upipChildProcessState": upipChildProcessState,
       "upipChildProcessStatus": upipChildProcessStatus,
       "upipChildProcessStartTime": upipChildProcessStartTime,
       "upipChildProcessStopTime": upipChildProcessStopTime,
       "upiInitChildProcessStatsTable": upiInitChildProcessStatsTable,
       "upiInitChildProcessStatsEntry": upiInitChildProcessStatsEntry,
       "upipsInitIpAddr": upipsInitIpAddr,
       "upipsInitProcessId": upipsInitProcessId,
       "upipsChildProcessType": upipsChildProcessType,
       "upipsInitProcessType": upipsInitProcessType,
       "upipsChildProcessesStarted": upipsChildProcessesStarted,
       "upipsChildProcessesDied": upipsChildProcessesDied,
       "upipsChildProcessesRunning": upipsChildProcessesRunning,
       "upiInitTrapInfo": upiInitTrapInfo,
       "upitTrapInfo": upitTrapInfo,
       "upitChildProcessHostName": upitChildProcessHostName,
       "upitChildProcessType": upitChildProcessType,
       "upitChildProcessId": upitChildProcessId,
       "upLink": upLink,
       "upldStartup": upldStartup,
       "upldShutdown": upldShutdown,
       "upldInvalidConfig": upldInvalidConfig,
       "upldUplAgentConnectionDown": upldUplAgentConnectionDown,
       "upldDatabaseConnectionDown": upldDatabaseConnectionDown,
       "upldOutOfResouce": upldOutOfResouce,
       "upldUplAgentConnectionUp": upldUplAgentConnectionUp,
       "upldDatabaseConnectionUp": upldDatabaseConnectionUp,
       "uplaStartup": uplaStartup,
       "uplaShutdown": uplaShutdown,
       "uplaDatabaseConnectionDown": uplaDatabaseConnectionDown,
       "uplaFaxMgrConnectionDown": uplaFaxMgrConnectionDown,
       "uplaMessengerConnectionDown": uplaMessengerConnectionDown,
       "uplaInvalidConfig": uplaInvalidConfig,
       "uplaInternalFatalErrors": uplaInternalFatalErrors,
       "uplaOutOfResource": uplaOutOfResource,
       "uplaDatabaseConnectionUp": uplaDatabaseConnectionUp,
       "uplrStartup": uplrStartup,
       "uplrShutdown": uplrShutdown,
       "uplrDatabaseConnectionDown": uplrDatabaseConnectionDown,
       "uplrDatabaseConnectionUp": uplrDatabaseConnectionUp,
       "uplrInvalidConfig": uplrInvalidConfig,
       "uplrInternalError": uplrInternalError,
       "uplrSMSCConnectionDown": uplrSMSCConnectionDown,
       "uplrSMSCConnectionUp": uplrSMSCConnectionUp,
       "uplrClientConnectionDown": uplrClientConnectionDown,
       "uplrClientConnectionUp": uplrClientConnectionUp,
       "uplrNbRouterConnectionDown": uplrNbRouterConnectionDown,
       "uplrNbRouterConnectionUp": uplrNbRouterConnectionUp,
       "uplrProtocolError": uplrProtocolError,
       "uplmStartup": uplmStartup,
       "uplmShutdown": uplmShutdown,
       "uplmDatabaseConnectionDown": uplmDatabaseConnectionDown,
       "uplmDatabaseConnectionUp": uplmDatabaseConnectionUp,
       "uplmInvalidConfig": uplmInvalidConfig,
       "uplmInternalErrors": uplmInternalErrors,
       "uplmAgentConnectionDown": uplmAgentConnectionDown,
       "uplmPublicHTTPServiceStarted": uplmPublicHTTPServiceStarted,
       "uplmPublicHTTPServiceDown": uplmPublicHTTPServiceDown,
       "uplmPrivateHTTPServiceDown": uplmPrivateHTTPServiceDown,
       "uplmPublicHTTPSServiceDown": uplmPublicHTTPSServiceDown,
       "upLinkProcesses": upLinkProcesses,
       "uplDispatcher": uplDispatcher,
       "uplDispatcherDescription": uplDispatcherDescription,
       "upldHostName": upldHostName,
       "upldProcessId": upldProcessId,
       "upldPortNumber": upldPortNumber,
       "upldStartUpTime": upldStartUpTime,
       "upldState": upldState,
       "uplDispatcherStats": uplDispatcherStats,
       "upldRequestsReceived": upldRequestsReceived,
       "upldRequestsDropped": upldRequestsDropped,
       "upldUplAgentsLoaded": upldUplAgentsLoaded,
       "upldUplAgentsDisconnected": upldUplAgentsDisconnected,
       "upldSubscribersLoaded": upldSubscribersLoaded,
       "upldKeyExchanges": upldKeyExchanges,
       "uplDispatcherTrapInfo": uplDispatcherTrapInfo,
       "upldTrapInfo": upldTrapInfo,
       "upldUplAgentId": upldUplAgentId,
       "uplAgent": uplAgent,
       "uplAgentDescriptionTable": uplAgentDescriptionTable,
       "uplAgentDescriptionEntry": uplAgentDescriptionEntry,
       "uplaAgentIdentifier": uplaAgentIdentifier,
       "uplaHostName": uplaHostName,
       "uplaProcessId": uplaProcessId,
       "uplaStartUpTime": uplaStartUpTime,
       "uplAgentProxyStats": uplAgentProxyStats,
       "uplAgentWebAccessStatsTable": uplAgentWebAccessStatsTable,
       "uplAgentWebAccessStatsEntry": uplAgentWebAccessStatsEntry,
       "uplawsAgentIdentifier": uplawsAgentIdentifier,
       "uplaHttpRequestsStarted": uplaHttpRequestsStarted,
       "uplaHttpRequestsSucceeded": uplaHttpRequestsSucceeded,
       "uplaHttpMeanResponseTime": uplaHttpMeanResponseTime,
       "uplaHttpDeviationOfResponseTime": uplaHttpDeviationOfResponseTime,
       "uplaHttpsRequestsStarted": uplaHttpsRequestsStarted,
       "uplaHttpsRequestsSucceeded": uplaHttpsRequestsSucceeded,
       "uplaHttpsMeanResponseTime": uplaHttpsMeanResponseTime,
       "uplaHttpsDeviationOfResponseTime": uplaHttpsDeviationOfResponseTime,
       "uplAgentErrorStatsSummaryTable": uplAgentErrorStatsSummaryTable,
       "uplAgentErrorStatsSummaryEntry": uplAgentErrorStatsSummaryEntry,
       "uplaesAgentIdentifier": uplaesAgentIdentifier,
       "uplaTotalErrors": uplaTotalErrors,
       "uplaSilentErrors": uplaSilentErrors,
       "uplaDeviceErrors": uplaDeviceErrors,
       "uplaKeyErrors": uplaKeyErrors,
       "uplaSessionErrors": uplaSessionErrors,
       "uplaTransactionErrors": uplaTransactionErrors,
       "uplaOtherErrors": uplaOtherErrors,
       "uplAgentErrorStatsDetailTable": uplAgentErrorStatsDetailTable,
       "uplAgentErrorStatsDetailEntry": uplAgentErrorStatsDetailEntry,
       "uplaedAgentIdentifier": uplaedAgentIdentifier,
       "uplaErrorCode": uplaErrorCode,
       "uplaErrorName": uplaErrorName,
       "uplaErrorSeverity": uplaErrorSeverity,
       "uplaErrorClass": uplaErrorClass,
       "uplaErrorCount": uplaErrorCount,
       "uplHdtpStats": uplHdtpStats,
       "uplAgentSessionStatsTable": uplAgentSessionStatsTable,
       "uplAgentSessionStatsEntry": uplAgentSessionStatsEntry,
       "uplassAgentIdentifier": uplassAgentIdentifier,
       "uplaActiveSessions": uplaActiveSessions,
       "uplaEncryptedSessions": uplaEncryptedSessions,
       "uplaProtoSessions": uplaProtoSessions,
       "uplaSessionsStarted": uplaSessionsStarted,
       "uplaSessionsSucceeded": uplaSessionsSucceeded,
       "uplaKeyExchanges": uplaKeyExchanges,
       "uplAgentAirLinkStatsTable": uplAgentAirLinkStatsTable,
       "uplAgentAirLinkStatsEntry": uplAgentAirLinkStatsEntry,
       "uplaasAgentIdentifier": uplaasAgentIdentifier,
       "uplaRequestsReceived": uplaRequestsReceived,
       "uplaRequestsDropped": uplaRequestsDropped,
       "uplaRequestsDuplicated": uplaRequestsDuplicated,
       "uplaRequestsNotValid": uplaRequestsNotValid,
       "uplaRepliesDelivered": uplaRepliesDelivered,
       "uplaRepliesTimedOut": uplaRepliesTimedOut,
       "uplAgentTransactionStatsTable": uplAgentTransactionStatsTable,
       "uplAgentTransactionStatsEntry": uplAgentTransactionStatsEntry,
       "uplatsAgentIdentifier": uplatsAgentIdentifier,
       "uplaTransactionsActive": uplaTransactionsActive,
       "uplaTransactionsStarted": uplaTransactionsStarted,
       "uplaTransactionsSucceeded": uplaTransactionsSucceeded,
       "uplaMeanTransactionLife": uplaMeanTransactionLife,
       "uplaDeviationOfTransactionLife": uplaDeviationOfTransactionLife,
       "uplaMeanResponseTime": uplaMeanResponseTime,
       "uplaDeviationOfResponseTime": uplaDeviationOfResponseTime,
       "uplaMeanRetriesPerThousandTxn": uplaMeanRetriesPerThousandTxn,
       "uplaDeviationOfRetriesPTTxn": uplaDeviationOfRetriesPTTxn,
       "uplAgentLimitedResourceTable": uplAgentLimitedResourceTable,
       "uplAgentLimitedResourceEntry": uplAgentLimitedResourceEntry,
       "uplaWapStats": uplaWapStats,
       "uplAgentWapWSPSessionStatsTable": uplAgentWapWSPSessionStatsTable,
       "uplAgentWapSessionStatsEntry": uplAgentWapSessionStatsEntry,
       "uplawssAgentIdentifier": uplawssAgentIdentifier,
       "uplaActiveWapSessions": uplaActiveWapSessions,
       "uplaWapSessionsStarted": uplaWapSessionsStarted,
       "uplAgentWapWTPTransactionStatsTable": uplAgentWapWTPTransactionStatsTable,
       "uplAgentWapTransactionStatsEntry": uplAgentWapTransactionStatsEntry,
       "uplawtsAgentIdentifier": uplawtsAgentIdentifier,
       "uplaWapInvokeTpdus": uplaWapInvokeTpdus,
       "uplaWapResultTpdus": uplaWapResultTpdus,
       "uplaWapAbortTransaction": uplaWapAbortTransaction,
       "uplAgentWapErrorStatsSummaryTable": uplAgentWapErrorStatsSummaryTable,
       "uplAgentWapErrorStatsSummaryEntry": uplAgentWapErrorStatsSummaryEntry,
       "uplawesAgentIdentifier": uplawesAgentIdentifier,
       "uplaTotalWapErrors": uplaTotalWapErrors,
       "uplaOtherWapErrors": uplaOtherWapErrors,
       "uplaSessionWapErrors": uplaSessionWapErrors,
       "uplaTransactionWapErrors": uplaTransactionWapErrors,
       "uplAgentWapErrorStatsDetailTable": uplAgentWapErrorStatsDetailTable,
       "uplAgentWapErrorStatsDetailEntry": uplAgentWapErrorStatsDetailEntry,
       "uplaweAgentIdentifier": uplaweAgentIdentifier,
       "uplaWapErrorCode": uplaWapErrorCode,
       "uplaWapErrorName": uplaWapErrorName,
       "uplaWapErrorSeverity": uplaWapErrorSeverity,
       "uplaWapErrorClass": uplaWapErrorClass,
       "uplaWapErrorCount": uplaWapErrorCount,
       "uplaStackServiceStats": uplaStackServiceStats,
       "uplAgentStackServiceTable": uplAgentStackServiceTable,
       "uplAgentStackServiceEntry": uplAgentStackServiceEntry,
       "uplasstAgentIdentifier": uplasstAgentIdentifier,
       "uplAgentStackServiceIdentifier": uplAgentStackServiceIdentifier,
       "uplAgentStackServiceAppProtoName": uplAgentStackServiceAppProtoName,
       "uplAgentStackServiceName": uplAgentStackServiceName,
       "uplAgentStackServiceLoaded": uplAgentStackServiceLoaded,
       "uplAgentStackServiceAdaptorThreads": uplAgentStackServiceAdaptorThreads,
       "uplAgentStackServiceWDPPortNumber": uplAgentStackServiceWDPPortNumber,
       "uplAgentTrapInfo": uplAgentTrapInfo,
       "uplaTrapInfo": uplaTrapInfo,
       "uplNbRouter": uplNbRouter,
       "uplNbRouterDescriptionTable": uplNbRouterDescriptionTable,
       "uplNbRouterDescriptionEntry": uplNbRouterDescriptionEntry,
       "uplrdIpAddress": uplrdIpAddress,
       "uplrdProcessId": uplrdProcessId,
       "uplrdHostName": uplrdHostName,
       "uplrdPortNumber": uplrdPortNumber,
       "uplrdStartUpTime": uplrdStartUpTime,
       "uplrHdtpStats": uplrHdtpStats,
       "uplNbRouterAirlinkTable": uplNbRouterAirlinkTable,
       "uplNbRouterAirlinkEntry": uplNbRouterAirlinkEntry,
       "uplNbRouterAirlinkStatsTable": uplNbRouterAirlinkStatsTable,
       "uplNbRouterAirlinkStatsEntry": uplNbRouterAirlinkStatsEntry,
       "uplrStackServiceStats": uplrStackServiceStats,
       "uplNbRouterTrapInfo": uplNbRouterTrapInfo,
       "uplrTrapInfo": uplrTrapInfo,
       "uplrClientIpAddress": uplrClientIpAddress,
       "uplrClientHostName": uplrClientHostName,
       "uplrClientProcessId": uplrClientProcessId,
       "uplMessenger": uplMessenger,
       "uplMessengerDescriptionTable": uplMessengerDescriptionTable,
       "uplMessengerDescriptionEntry": uplMessengerDescriptionEntry,
       "uplmdIpAddress": uplmdIpAddress,
       "uplmdProcessId": uplmdProcessId,
       "uplmdHostName": uplmdHostName,
       "uplmdMsgServerPortNumber": uplmdMsgServerPortNumber,
       "uplmdPublicHTTPPortNumber": uplmdPublicHTTPPortNumber,
       "uplmdPublicHTTPSPortNumber": uplmdPublicHTTPSPortNumber,
       "uplmdPrivateHTTPPortNumber": uplmdPrivateHTTPPortNumber,
       "uplmdStartupTime": uplmdStartupTime,
       "uplmHdtpStats": uplmHdtpStats,
       "uplMessengerAirlinkTable": uplMessengerAirlinkTable,
       "uplMessengerAirlinkEntry": uplMessengerAirlinkEntry,
       "uplMessengerAirlinkStatsTable": uplMessengerAirlinkStatsTable,
       "uplMessengerAirlinkStatsEntry": uplMessengerAirlinkStatsEntry,
       "uplmStackServiceStats": uplmStackServiceStats,
       "uplMessengerNtfnStatsTable": uplMessengerNtfnStatsTable,
       "uplMessengerNtfnStatsEntry": uplMessengerNtfnStatsEntry,
       "uplmnsIpAddress": uplmnsIpAddress,
       "uplmnsProcessId": uplmnsProcessId,
       "uplmnsPublicHTTPReqReceived": uplmnsPublicHTTPReqReceived,
       "uplmnsPrivateHTTPReqReceived": uplmnsPrivateHTTPReqReceived,
       "uplmnsPublicHTTPSReqReceived": uplmnsPublicHTTPSReqReceived,
       "uplmnsPublicHTTPReqProcessed": uplmnsPublicHTTPReqProcessed,
       "uplmnsPrivateHTTPReqProcessed": uplmnsPrivateHTTPReqProcessed,
       "uplmnsPublicHTTPSReqProcessed": uplmnsPublicHTTPSReqProcessed,
       "uplmnsAvgNtfnsAddedPerSec": uplmnsAvgNtfnsAddedPerSec,
       "uplmnsAvgNtfnsDeliveredPerSec": uplmnsAvgNtfnsDeliveredPerSec,
       "uplmnsAvgNtfnsExpiredPerSec": uplmnsAvgNtfnsExpiredPerSec,
       "uplmnsAvgNtfnsMarkedUnDelvrPerSec": uplmnsAvgNtfnsMarkedUnDelvrPerSec,
       "uplMessengerNtfnCacheTable": uplMessengerNtfnCacheTable,
       "uplMessengerNtfnCacheEntry": uplMessengerNtfnCacheEntry,
       "uplmncIpAddress": uplmncIpAddress,
       "uplmncProcessId": uplmncProcessId,
       "uplmncTotalNumOfPendingNtfns": uplmncTotalNumOfPendingNtfns,
       "uplmncAvgNumOfPendingNtfnsPerSub": uplmncAvgNumOfPendingNtfnsPerSub,
       "uplMessengerTrapInfo": uplMessengerTrapInfo,
       "uplmTrapInfo": uplmTrapInfo,
       "upLinkConfig": upLinkConfig,
       "upLinkStaticInfo": upLinkStaticInfo,
       "upAdmin": upAdmin,
       "upsProxyServiceDown": upsProxyServiceDown,
       "upsProxyServiceSlow": upsProxyServiceSlow,
       "upsPushServiceDown": upsPushServiceDown,
       "upsBookmarksServiceDown": upsBookmarksServiceDown,
       "upsBookmarksServiceSlow": upsBookmarksServiceSlow,
       "upsHomePageServiceDown": upsHomePageServiceDown,
       "upsUPWebServiceDown": upsUPWebServiceDown,
       "upsUPWebServiceSlow": upsUPWebServiceSlow,
       "upsUPAdminServiceDown": upsUPAdminServiceDown,
       "upsUPMailServiceDown": upsUPMailServiceDown,
       "upsUPMailServiceSlow": upsUPMailServiceSlow,
       "upsUPPimServiceDown": upsUPPimServiceDown,
       "upsUPPimServiceSlow": upsUPPimServiceSlow,
       "upsHomePageServiceSlow": upsHomePageServiceSlow,
       "upsProxyServiceUp": upsProxyServiceUp,
       "upsProxyServiceNormal": upsProxyServiceNormal,
       "upsPushServiceUp": upsPushServiceUp,
       "upsBookmarksServiceUp": upsBookmarksServiceUp,
       "upsBookmarksServiceNormal": upsBookmarksServiceNormal,
       "upsHomePageServiceUp": upsHomePageServiceUp,
       "upsUPWebServiceUp": upsUPWebServiceUp,
       "upsUPWebServiceNormal": upsUPWebServiceNormal,
       "upsUPAdminServiceUp": upsUPAdminServiceUp,
       "upsUPMailServiceUp": upsUPMailServiceUp,
       "upsUPMailServiceNormal": upsUPMailServiceNormal,
       "upsUPPimServiceUp": upsUPPimServiceUp,
       "upsUPPimServiceNormal": upsUPPimServiceNormal,
       "upAdminTrapInfo": upAdminTrapInfo,
       "upsTrapInfo": upsTrapInfo,
       "services": services,
       "upMail": upMail}
)
