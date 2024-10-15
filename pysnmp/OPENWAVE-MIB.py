# SNMP MIB module (OPENWAVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPENWAVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:23 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Openwave_ObjectIdentity = ObjectIdentity
openwave = _Openwave_ObjectIdentity(
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
    (0, "OPENWAVE-MIB", "upidInitIpAddr"),
    (0, "OPENWAVE-MIB", "upidInitProcessId"),
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
    (0, "OPENWAVE-MIB", "upipInitIpAddr"),
    (0, "OPENWAVE-MIB", "upipInitProcessId"),
    (0, "OPENWAVE-MIB", "upipChildProcessId"),
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
    (0, "OPENWAVE-MIB", "upipsInitIpAddr"),
    (0, "OPENWAVE-MIB", "upipsInitProcessId"),
    (0, "OPENWAVE-MIB", "upipsChildProcessType"),
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
_UplDispRadiusClientStats_ObjectIdentity = ObjectIdentity
uplDispRadiusClientStats = _UplDispRadiusClientStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 3)
)
_UpldTotalMappingTableHits_Type = Counter32
_UpldTotalMappingTableHits_Object = MibScalar
upldTotalMappingTableHits = _UpldTotalMappingTableHits_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 3, 1),
    _UpldTotalMappingTableHits_Type()
)
upldTotalMappingTableHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldTotalMappingTableHits.setStatus("mandatory")
_UpldSuccessfulMappingHits_Type = Counter32
_UpldSuccessfulMappingHits_Object = MibScalar
upldSuccessfulMappingHits = _UpldSuccessfulMappingHits_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 3, 2),
    _UpldSuccessfulMappingHits_Type()
)
upldSuccessfulMappingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldSuccessfulMappingHits.setStatus("mandatory")
_UpldFailedMappingHits_Type = Counter32
_UpldFailedMappingHits_Object = MibScalar
upldFailedMappingHits = _UpldFailedMappingHits_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 1, 3, 3),
    _UpldFailedMappingHits_Type()
)
upldFailedMappingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upldFailedMappingHits.setStatus("mandatory")
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
    (0, "OPENWAVE-MIB", "uplaAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplawsAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplaesAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplaedAgentIdentifier"),
    (0, "OPENWAVE-MIB", "uplaErrorCode"),
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
    (0, "OPENWAVE-MIB", "uplassAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplaasAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplatsAgentIdentifier"),
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
_UplAgentLimitedResourceTable_Type = Integer32
_UplAgentLimitedResourceTable_Object = MibScalar
uplAgentLimitedResourceTable = _UplAgentLimitedResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 3, 6),
    _UplAgentLimitedResourceTable_Type()
)
uplAgentLimitedResourceTable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplAgentLimitedResourceTable.setStatus("deprecated")
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
    (0, "OPENWAVE-MIB", "uplawssAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplawtsAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplawesAgentIdentifier"),
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
    (0, "OPENWAVE-MIB", "uplaweAgentIdentifier"),
    (0, "OPENWAVE-MIB", "uplaWapErrorCode"),
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
    (0, "OPENWAVE-MIB", "uplasstAgentIdentifier"),
    (0, "OPENWAVE-MIB", "uplAgentStackServiceIdentifier"),
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
_UplAgentStackServiceTableSize_Type = Integer32
_UplAgentStackServiceTableSize_Object = MibTableColumn
uplAgentStackServiceTableSize = _UplAgentStackServiceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 8),
    _UplAgentStackServiceTableSize_Type()
)
uplAgentStackServiceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceTableSize.setStatus("mandatory")
_UplAgentStackServiceMeanTableItems_Type = Integer32
_UplAgentStackServiceMeanTableItems_Object = MibTableColumn
uplAgentStackServiceMeanTableItems = _UplAgentStackServiceMeanTableItems_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 9),
    _UplAgentStackServiceMeanTableItems_Type()
)
uplAgentStackServiceMeanTableItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceMeanTableItems.setStatus("mandatory")
_UplAgentStackServiceMeanTableItemsDeviation_Type = Integer32
_UplAgentStackServiceMeanTableItemsDeviation_Object = MibTableColumn
uplAgentStackServiceMeanTableItemsDeviation = _UplAgentStackServiceMeanTableItemsDeviation_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 10),
    _UplAgentStackServiceMeanTableItemsDeviation_Type()
)
uplAgentStackServiceMeanTableItemsDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceMeanTableItemsDeviation.setStatus("mandatory")
_UplAgentStackServiceMeanBucketChainLength_Type = Integer32
_UplAgentStackServiceMeanBucketChainLength_Object = MibTableColumn
uplAgentStackServiceMeanBucketChainLength = _UplAgentStackServiceMeanBucketChainLength_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 11),
    _UplAgentStackServiceMeanBucketChainLength_Type()
)
uplAgentStackServiceMeanBucketChainLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceMeanBucketChainLength.setStatus("mandatory")
_UplAgentStackServiceMeanBucketChainLengthDeviation_Type = Integer32
_UplAgentStackServiceMeanBucketChainLengthDeviation_Object = MibTableColumn
uplAgentStackServiceMeanBucketChainLengthDeviation = _UplAgentStackServiceMeanBucketChainLengthDeviation_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 12),
    _UplAgentStackServiceMeanBucketChainLengthDeviation_Type()
)
uplAgentStackServiceMeanBucketChainLengthDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceMeanBucketChainLengthDeviation.setStatus("mandatory")
_UplAgentStackServiceTableMeanNumberItemsGarbageCollected_Type = Integer32
_UplAgentStackServiceTableMeanNumberItemsGarbageCollected_Object = MibTableColumn
uplAgentStackServiceTableMeanNumberItemsGarbageCollected = _UplAgentStackServiceTableMeanNumberItemsGarbageCollected_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 13),
    _UplAgentStackServiceTableMeanNumberItemsGarbageCollected_Type()
)
uplAgentStackServiceTableMeanNumberItemsGarbageCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceTableMeanNumberItemsGarbageCollected.setStatus("mandatory")
_UplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn_Type = Integer32
_UplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn_Object = MibTableColumn
uplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn = _UplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 14),
    _UplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn_Type()
)
uplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn.setStatus("mandatory")
_UplAgentStackServiceMeanGarbageCollectTime_Type = Integer32
_UplAgentStackServiceMeanGarbageCollectTime_Object = MibTableColumn
uplAgentStackServiceMeanGarbageCollectTime = _UplAgentStackServiceMeanGarbageCollectTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 15),
    _UplAgentStackServiceMeanGarbageCollectTime_Type()
)
uplAgentStackServiceMeanGarbageCollectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceMeanGarbageCollectTime.setStatus("mandatory")
_UplAgentStackServiceMeanGarbageCollectTimeDeviation_Type = Integer32
_UplAgentStackServiceMeanGarbageCollectTimeDeviation_Object = MibTableColumn
uplAgentStackServiceMeanGarbageCollectTimeDeviation = _UplAgentStackServiceMeanGarbageCollectTimeDeviation_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 5, 1, 1, 16),
    _UplAgentStackServiceMeanGarbageCollectTimeDeviation_Type()
)
uplAgentStackServiceMeanGarbageCollectTimeDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplAgentStackServiceMeanGarbageCollectTimeDeviation.setStatus("mandatory")
_UplaRadiusClientStats_ObjectIdentity = ObjectIdentity
uplaRadiusClientStats = _UplaRadiusClientStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 6)
)
_UplAgentRadiusClientStatsTable_Object = MibTable
uplAgentRadiusClientStatsTable = _UplAgentRadiusClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    uplAgentRadiusClientStatsTable.setStatus("mandatory")
_UplAgentRadiusClientStatsEntry_Object = MibTableRow
uplAgentRadiusClientStatsEntry = _UplAgentRadiusClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 6, 1, 1)
)
uplAgentRadiusClientStatsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplarcsAgentIdentifier"),
)
if mibBuilder.loadTexts:
    uplAgentRadiusClientStatsEntry.setStatus("mandatory")
_UplarcsAgentIdentifier_Type = Integer32
_UplarcsAgentIdentifier_Object = MibTableColumn
uplarcsAgentIdentifier = _UplarcsAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 6, 1, 1, 1),
    _UplarcsAgentIdentifier_Type()
)
uplarcsAgentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplarcsAgentIdentifier.setStatus("mandatory")
_UplaTotalMappingTableHits_Type = Counter32
_UplaTotalMappingTableHits_Object = MibTableColumn
uplaTotalMappingTableHits = _UplaTotalMappingTableHits_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 6, 1, 1, 2),
    _UplaTotalMappingTableHits_Type()
)
uplaTotalMappingTableHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaTotalMappingTableHits.setStatus("mandatory")
_UplaSuccessfulMappingHits_Type = Counter32
_UplaSuccessfulMappingHits_Object = MibTableColumn
uplaSuccessfulMappingHits = _UplaSuccessfulMappingHits_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 6, 1, 1, 3),
    _UplaSuccessfulMappingHits_Type()
)
uplaSuccessfulMappingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaSuccessfulMappingHits.setStatus("mandatory")
_UplaFailedMappingHits_Type = Counter32
_UplaFailedMappingHits_Object = MibTableColumn
uplaFailedMappingHits = _UplaFailedMappingHits_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 2, 6, 1, 1, 4),
    _UplaFailedMappingHits_Type()
)
uplaFailedMappingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplaFailedMappingHits.setStatus("mandatory")
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
    (0, "OPENWAVE-MIB", "uplrdIpAddress"),
    (0, "OPENWAVE-MIB", "uplrdProcessId"),
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
_UplNbRouterAirlinkTable_Type = Integer32
_UplNbRouterAirlinkTable_Object = MibScalar
uplNbRouterAirlinkTable = _UplNbRouterAirlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 2, 1),
    _UplNbRouterAirlinkTable_Type()
)
uplNbRouterAirlinkTable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplNbRouterAirlinkTable.setStatus("deprecated")
_UplNbRouterAirlinkStatsTable_Type = Integer32
_UplNbRouterAirlinkStatsTable_Object = MibScalar
uplNbRouterAirlinkStatsTable = _UplNbRouterAirlinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 3, 2, 2),
    _UplNbRouterAirlinkStatsTable_Type()
)
uplNbRouterAirlinkStatsTable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplNbRouterAirlinkStatsTable.setStatus("deprecated")
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
    (0, "OPENWAVE-MIB", "uplmdIpAddress"),
    (0, "OPENWAVE-MIB", "uplmdProcessId"),
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
_UplmDBMaxConnections_Type = Integer32
_UplmDBMaxConnections_Object = MibTableColumn
uplmDBMaxConnections = _UplmDBMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 9),
    _UplmDBMaxConnections_Type()
)
uplmDBMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmDBMaxConnections.setStatus("mandatory")
_UplmDBMinConnections_Type = Integer32
_UplmDBMinConnections_Object = MibTableColumn
uplmDBMinConnections = _UplmDBMinConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 10),
    _UplmDBMinConnections_Type()
)
uplmDBMinConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmDBMinConnections.setStatus("mandatory")
_UplmDBConnectionCacheThreadWaits_Type = Counter32
_UplmDBConnectionCacheThreadWaits_Object = MibTableColumn
uplmDBConnectionCacheThreadWaits = _UplmDBConnectionCacheThreadWaits_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 11),
    _UplmDBConnectionCacheThreadWaits_Type()
)
uplmDBConnectionCacheThreadWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmDBConnectionCacheThreadWaits.setStatus("mandatory")
_UplmDBConnectionCacheMeanWaitTime_Type = Integer32
_UplmDBConnectionCacheMeanWaitTime_Object = MibTableColumn
uplmDBConnectionCacheMeanWaitTime = _UplmDBConnectionCacheMeanWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 12),
    _UplmDBConnectionCacheMeanWaitTime_Type()
)
uplmDBConnectionCacheMeanWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmDBConnectionCacheMeanWaitTime.setStatus("mandatory")
_UplmDBConnectionCacheDeviationOfWaitTime_Type = Integer32
_UplmDBConnectionCacheDeviationOfWaitTime_Object = MibTableColumn
uplmDBConnectionCacheDeviationOfWaitTime = _UplmDBConnectionCacheDeviationOfWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 13),
    _UplmDBConnectionCacheDeviationOfWaitTime_Type()
)
uplmDBConnectionCacheDeviationOfWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmDBConnectionCacheDeviationOfWaitTime.setStatus("mandatory")
_UplmdMaxMsgClientStreams_Type = Integer32
_UplmdMaxMsgClientStreams_Object = MibTableColumn
uplmdMaxMsgClientStreams = _UplmdMaxMsgClientStreams_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 14),
    _UplmdMaxMsgClientStreams_Type()
)
uplmdMaxMsgClientStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdMaxMsgClientStreams.setStatus("mandatory")
_UplmdOpenAgentStreams_Type = Integer32
_UplmdOpenAgentStreams_Object = MibTableColumn
uplmdOpenAgentStreams = _UplmdOpenAgentStreams_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 15),
    _UplmdOpenAgentStreams_Type()
)
uplmdOpenAgentStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdOpenAgentStreams.setStatus("mandatory")
_UplmdNumTxnProcessed_Type = Integer32
_UplmdNumTxnProcessed_Object = MibTableColumn
uplmdNumTxnProcessed = _UplmdNumTxnProcessed_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 1, 1, 16),
    _UplmdNumTxnProcessed_Type()
)
uplmdNumTxnProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmdNumTxnProcessed.setStatus("mandatory")
_UplmHdtpStats_ObjectIdentity = ObjectIdentity
uplmHdtpStats = _UplmHdtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2)
)
_UplMessengerAirlinkTable_Type = Integer32
_UplMessengerAirlinkTable_Object = MibScalar
uplMessengerAirlinkTable = _UplMessengerAirlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2, 1),
    _UplMessengerAirlinkTable_Type()
)
uplMessengerAirlinkTable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplMessengerAirlinkTable.setStatus("deprecated")
_UplMessengerAirlinkStatsTable_Type = Integer32
_UplMessengerAirlinkStatsTable_Object = MibScalar
uplMessengerAirlinkStatsTable = _UplMessengerAirlinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 2, 2),
    _UplMessengerAirlinkStatsTable_Type()
)
uplMessengerAirlinkStatsTable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplMessengerAirlinkStatsTable.setStatus("deprecated")
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
    (0, "OPENWAVE-MIB", "uplmnsIpAddress"),
    (0, "OPENWAVE-MIB", "uplmnsProcessId"),
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
_UplmnsNumAddRequests_Type = Integer32
_UplmnsNumAddRequests_Object = MibTableColumn
uplmnsNumAddRequests = _UplmnsNumAddRequests_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 13),
    _UplmnsNumAddRequests_Type()
)
uplmnsNumAddRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsNumAddRequests.setStatus("mandatory")
_UplmnsNumStatusRequests_Type = Integer32
_UplmnsNumStatusRequests_Object = MibTableColumn
uplmnsNumStatusRequests = _UplmnsNumStatusRequests_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 14),
    _UplmnsNumStatusRequests_Type()
)
uplmnsNumStatusRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsNumStatusRequests.setStatus("mandatory")
_UplmnsNumDeleteRequests_Type = Integer32
_UplmnsNumDeleteRequests_Object = MibTableColumn
uplmnsNumDeleteRequests = _UplmnsNumDeleteRequests_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 15),
    _UplmnsNumDeleteRequests_Type()
)
uplmnsNumDeleteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsNumDeleteRequests.setStatus("mandatory")
_UplmnsNumAdded_Type = Integer32
_UplmnsNumAdded_Object = MibTableColumn
uplmnsNumAdded = _UplmnsNumAdded_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 16),
    _UplmnsNumAdded_Type()
)
uplmnsNumAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsNumAdded.setStatus("mandatory")
_UplmnsNumStatusFound_Type = Integer32
_UplmnsNumStatusFound_Object = MibTableColumn
uplmnsNumStatusFound = _UplmnsNumStatusFound_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 17),
    _UplmnsNumStatusFound_Type()
)
uplmnsNumStatusFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsNumStatusFound.setStatus("mandatory")
_UplmnsNumDeleted_Type = Integer32
_UplmnsNumDeleted_Object = MibTableColumn
uplmnsNumDeleted = _UplmnsNumDeleted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 18),
    _UplmnsNumDeleted_Type()
)
uplmnsNumDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsNumDeleted.setStatus("mandatory")
_UplmnsNumExpired_Type = Integer32
_UplmnsNumExpired_Object = MibTableColumn
uplmnsNumExpired = _UplmnsNumExpired_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 19),
    _UplmnsNumExpired_Type()
)
uplmnsNumExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsNumExpired.setStatus("mandatory")
_UplmnsCompletedNotifications_Type = Integer32
_UplmnsCompletedNotifications_Object = MibTableColumn
uplmnsCompletedNotifications = _UplmnsCompletedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 20),
    _UplmnsCompletedNotifications_Type()
)
uplmnsCompletedNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsCompletedNotifications.setStatus("mandatory")
_UplmnsSignalsSent_Type = Integer32
_UplmnsSignalsSent_Object = MibTableColumn
uplmnsSignalsSent = _UplmnsSignalsSent_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 4, 1, 21),
    _UplmnsSignalsSent_Type()
)
uplmnsSignalsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmnsSignalsSent.setStatus("mandatory")
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
    (0, "OPENWAVE-MIB", "uplmncIpAddress"),
    (0, "OPENWAVE-MIB", "uplmncProcessId"),
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
_UplMessengerHTTPStatsTable_Object = MibTable
uplMessengerHTTPStatsTable = _UplMessengerHTTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    uplMessengerHTTPStatsTable.setStatus("mandatory")
_UplMessengerHTTPStatsEntry_Object = MibTableRow
uplMessengerHTTPStatsEntry = _UplMessengerHTTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1)
)
uplMessengerHTTPStatsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplmhIpAddress"),
    (0, "OPENWAVE-MIB", "uplmhProcessId"),
)
if mibBuilder.loadTexts:
    uplMessengerHTTPStatsEntry.setStatus("mandatory")
_UplmhIpAddress_Type = IpAddress
_UplmhIpAddress_Object = MibTableColumn
uplmhIpAddress = _UplmhIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 1),
    _UplmhIpAddress_Type()
)
uplmhIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhIpAddress.setStatus("mandatory")
_UplmhProcessId_Type = Integer32
_UplmhProcessId_Object = MibTableColumn
uplmhProcessId = _UplmhProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 2),
    _UplmhProcessId_Type()
)
uplmhProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhProcessId.setStatus("mandatory")
_UplmhPublicHTTPMaxConnections_Type = Integer32
_UplmhPublicHTTPMaxConnections_Object = MibTableColumn
uplmhPublicHTTPMaxConnections = _UplmhPublicHTTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 3),
    _UplmhPublicHTTPMaxConnections_Type()
)
uplmhPublicHTTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPMaxConnections.setStatus("mandatory")
_UplmhPublicHTTPOpenConnections_Type = Integer32
_UplmhPublicHTTPOpenConnections_Object = MibTableColumn
uplmhPublicHTTPOpenConnections = _UplmhPublicHTTPOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 4),
    _UplmhPublicHTTPOpenConnections_Type()
)
uplmhPublicHTTPOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPOpenConnections.setStatus("mandatory")
_UplmhPublicHTTPMaxThreads_Type = Integer32
_UplmhPublicHTTPMaxThreads_Object = MibTableColumn
uplmhPublicHTTPMaxThreads = _UplmhPublicHTTPMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 5),
    _UplmhPublicHTTPMaxThreads_Type()
)
uplmhPublicHTTPMaxThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPMaxThreads.setStatus("mandatory")
_UplmhPublicHTTPBusyThreads_Type = Integer32
_UplmhPublicHTTPBusyThreads_Object = MibTableColumn
uplmhPublicHTTPBusyThreads = _UplmhPublicHTTPBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 6),
    _UplmhPublicHTTPBusyThreads_Type()
)
uplmhPublicHTTPBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPBusyThreads.setStatus("mandatory")
_UplmhPublicHTTPTimesAllThreadsBusy_Type = Integer32
_UplmhPublicHTTPTimesAllThreadsBusy_Object = MibTableColumn
uplmhPublicHTTPTimesAllThreadsBusy = _UplmhPublicHTTPTimesAllThreadsBusy_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 7),
    _UplmhPublicHTTPTimesAllThreadsBusy_Type()
)
uplmhPublicHTTPTimesAllThreadsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPTimesAllThreadsBusy.setStatus("mandatory")
_UplmhPublicHTTPMaxDispQueueLength_Type = Integer32
_UplmhPublicHTTPMaxDispQueueLength_Object = MibTableColumn
uplmhPublicHTTPMaxDispQueueLength = _UplmhPublicHTTPMaxDispQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 8),
    _UplmhPublicHTTPMaxDispQueueLength_Type()
)
uplmhPublicHTTPMaxDispQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPMaxDispQueueLength.setStatus("mandatory")
_UplmhPublicHTTPCurrentDispQueueLen_Type = Integer32
_UplmhPublicHTTPCurrentDispQueueLen_Object = MibTableColumn
uplmhPublicHTTPCurrentDispQueueLen = _UplmhPublicHTTPCurrentDispQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 9),
    _UplmhPublicHTTPCurrentDispQueueLen_Type()
)
uplmhPublicHTTPCurrentDispQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPCurrentDispQueueLen.setStatus("mandatory")
_UplmhPublicHTTPTimesDispQueueFull_Type = Integer32
_UplmhPublicHTTPTimesDispQueueFull_Object = MibTableColumn
uplmhPublicHTTPTimesDispQueueFull = _UplmhPublicHTTPTimesDispQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 10),
    _UplmhPublicHTTPTimesDispQueueFull_Type()
)
uplmhPublicHTTPTimesDispQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPTimesDispQueueFull.setStatus("mandatory")
_UplmhPrivateHTTPMaxConnections_Type = Integer32
_UplmhPrivateHTTPMaxConnections_Object = MibTableColumn
uplmhPrivateHTTPMaxConnections = _UplmhPrivateHTTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 11),
    _UplmhPrivateHTTPMaxConnections_Type()
)
uplmhPrivateHTTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPMaxConnections.setStatus("mandatory")
_UplmhPrivateHTTPOpenConnections_Type = Integer32
_UplmhPrivateHTTPOpenConnections_Object = MibTableColumn
uplmhPrivateHTTPOpenConnections = _UplmhPrivateHTTPOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 12),
    _UplmhPrivateHTTPOpenConnections_Type()
)
uplmhPrivateHTTPOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPOpenConnections.setStatus("mandatory")
_UplmhPrivateHTTPMaxThreads_Type = Integer32
_UplmhPrivateHTTPMaxThreads_Object = MibTableColumn
uplmhPrivateHTTPMaxThreads = _UplmhPrivateHTTPMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 13),
    _UplmhPrivateHTTPMaxThreads_Type()
)
uplmhPrivateHTTPMaxThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPMaxThreads.setStatus("mandatory")
_UplmhPrivateHTTPBusyThreads_Type = Integer32
_UplmhPrivateHTTPBusyThreads_Object = MibTableColumn
uplmhPrivateHTTPBusyThreads = _UplmhPrivateHTTPBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 14),
    _UplmhPrivateHTTPBusyThreads_Type()
)
uplmhPrivateHTTPBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPBusyThreads.setStatus("mandatory")
_UplmhPrivateHTTPTimesAllThreadsBusy_Type = Integer32
_UplmhPrivateHTTPTimesAllThreadsBusy_Object = MibTableColumn
uplmhPrivateHTTPTimesAllThreadsBusy = _UplmhPrivateHTTPTimesAllThreadsBusy_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 15),
    _UplmhPrivateHTTPTimesAllThreadsBusy_Type()
)
uplmhPrivateHTTPTimesAllThreadsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPTimesAllThreadsBusy.setStatus("mandatory")
_UplmhPrivateHTTPMaxDispQueueLength_Type = Integer32
_UplmhPrivateHTTPMaxDispQueueLength_Object = MibTableColumn
uplmhPrivateHTTPMaxDispQueueLength = _UplmhPrivateHTTPMaxDispQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 16),
    _UplmhPrivateHTTPMaxDispQueueLength_Type()
)
uplmhPrivateHTTPMaxDispQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPMaxDispQueueLength.setStatus("mandatory")
_UplmhPrivateHTTPCurrentDispQueueLen_Type = Integer32
_UplmhPrivateHTTPCurrentDispQueueLen_Object = MibTableColumn
uplmhPrivateHTTPCurrentDispQueueLen = _UplmhPrivateHTTPCurrentDispQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 17),
    _UplmhPrivateHTTPCurrentDispQueueLen_Type()
)
uplmhPrivateHTTPCurrentDispQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPCurrentDispQueueLen.setStatus("mandatory")
_UplmhPrivateHTTPTimesDispQueueFull_Type = Integer32
_UplmhPrivateHTTPTimesDispQueueFull_Object = MibTableColumn
uplmhPrivateHTTPTimesDispQueueFull = _UplmhPrivateHTTPTimesDispQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 18),
    _UplmhPrivateHTTPTimesDispQueueFull_Type()
)
uplmhPrivateHTTPTimesDispQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPrivateHTTPTimesDispQueueFull.setStatus("mandatory")
_UplmhPublicHTTPSMaxConnections_Type = Integer32
_UplmhPublicHTTPSMaxConnections_Object = MibTableColumn
uplmhPublicHTTPSMaxConnections = _UplmhPublicHTTPSMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 19),
    _UplmhPublicHTTPSMaxConnections_Type()
)
uplmhPublicHTTPSMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSMaxConnections.setStatus("mandatory")
_UplmhPublicHTTPSOpenConnections_Type = Integer32
_UplmhPublicHTTPSOpenConnections_Object = MibTableColumn
uplmhPublicHTTPSOpenConnections = _UplmhPublicHTTPSOpenConnections_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 20),
    _UplmhPublicHTTPSOpenConnections_Type()
)
uplmhPublicHTTPSOpenConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSOpenConnections.setStatus("mandatory")
_UplmhPublicHTTPSMaxThreads_Type = Integer32
_UplmhPublicHTTPSMaxThreads_Object = MibTableColumn
uplmhPublicHTTPSMaxThreads = _UplmhPublicHTTPSMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 21),
    _UplmhPublicHTTPSMaxThreads_Type()
)
uplmhPublicHTTPSMaxThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSMaxThreads.setStatus("mandatory")
_UplmhPublicHTTPSBusyThreads_Type = Integer32
_UplmhPublicHTTPSBusyThreads_Object = MibTableColumn
uplmhPublicHTTPSBusyThreads = _UplmhPublicHTTPSBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 22),
    _UplmhPublicHTTPSBusyThreads_Type()
)
uplmhPublicHTTPSBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSBusyThreads.setStatus("mandatory")
_UplmhPublicHTTPSTimesAllThreadsBusy_Type = Integer32
_UplmhPublicHTTPSTimesAllThreadsBusy_Object = MibTableColumn
uplmhPublicHTTPSTimesAllThreadsBusy = _UplmhPublicHTTPSTimesAllThreadsBusy_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 23),
    _UplmhPublicHTTPSTimesAllThreadsBusy_Type()
)
uplmhPublicHTTPSTimesAllThreadsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSTimesAllThreadsBusy.setStatus("mandatory")
_UplmhPublicHTTPSMaxDispQueueLength_Type = Integer32
_UplmhPublicHTTPSMaxDispQueueLength_Object = MibTableColumn
uplmhPublicHTTPSMaxDispQueueLength = _UplmhPublicHTTPSMaxDispQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 24),
    _UplmhPublicHTTPSMaxDispQueueLength_Type()
)
uplmhPublicHTTPSMaxDispQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSMaxDispQueueLength.setStatus("mandatory")
_UplmhPublicHTTPSCurrentDispQueueLen_Type = Integer32
_UplmhPublicHTTPSCurrentDispQueueLen_Object = MibTableColumn
uplmhPublicHTTPSCurrentDispQueueLen = _UplmhPublicHTTPSCurrentDispQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 25),
    _UplmhPublicHTTPSCurrentDispQueueLen_Type()
)
uplmhPublicHTTPSCurrentDispQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSCurrentDispQueueLen.setStatus("mandatory")
_UplmhPublicHTTPSTimesDispQueueFull_Type = Integer32
_UplmhPublicHTTPSTimesDispQueueFull_Object = MibTableColumn
uplmhPublicHTTPSTimesDispQueueFull = _UplmhPublicHTTPSTimesDispQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 4, 6, 1, 26),
    _UplmhPublicHTTPSTimesDispQueueFull_Type()
)
uplmhPublicHTTPSTimesDispQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplmhPublicHTTPSTimesDispQueueFull.setStatus("mandatory")
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
_UplWap_ObjectIdentity = ObjectIdentity
uplWap = _UplWap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 5)
)
_UplWapTrapInfo_ObjectIdentity = ObjectIdentity
uplWapTrapInfo = _UplWapTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 5, 20)
)
_UplwTrapInfo_Type = DisplayString
_UplwTrapInfo_Object = MibScalar
uplwTrapInfo = _UplwTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 5, 20, 1),
    _UplwTrapInfo_Type()
)
uplwTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplwTrapInfo.setStatus("optional")
_UplwHostName_Type = DisplayString
_UplwHostName_Object = MibScalar
uplwHostName = _UplwHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 5, 20, 2),
    _UplwHostName_Type()
)
uplwHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplwHostName.setStatus("optional")
_UplwProcessId_Type = Integer32
_UplwProcessId_Object = MibScalar
uplwProcessId = _UplwProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 5, 20, 3),
    _UplwProcessId_Type()
)
uplwProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplwProcessId.setStatus("optional")
_UplBillingMgr_ObjectIdentity = ObjectIdentity
uplBillingMgr = _UplBillingMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6)
)
_UplBillingMgrDescriptionTable_Object = MibTable
uplBillingMgrDescriptionTable = _UplBillingMgrDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    uplBillingMgrDescriptionTable.setStatus("mandatory")
_UplBillingMgrDescriptionEntry_Object = MibTableRow
uplBillingMgrDescriptionEntry = _UplBillingMgrDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 1, 1)
)
uplBillingMgrDescriptionEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplbdIpAddress"),
    (0, "OPENWAVE-MIB", "uplbdProcessId"),
)
if mibBuilder.loadTexts:
    uplBillingMgrDescriptionEntry.setStatus("mandatory")
_UplbdIpAddress_Type = IpAddress
_UplbdIpAddress_Object = MibTableColumn
uplbdIpAddress = _UplbdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 1, 1, 1),
    _UplbdIpAddress_Type()
)
uplbdIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbdIpAddress.setStatus("mandatory")
_UplbdProcessId_Type = Integer32
_UplbdProcessId_Object = MibTableColumn
uplbdProcessId = _UplbdProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 1, 1, 2),
    _UplbdProcessId_Type()
)
uplbdProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbdProcessId.setStatus("mandatory")
_UplbdHostName_Type = DisplayString
_UplbdHostName_Object = MibTableColumn
uplbdHostName = _UplbdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 1, 1, 3),
    _UplbdHostName_Type()
)
uplbdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbdHostName.setStatus("mandatory")
_UplbdPortNumber_Type = Integer32
_UplbdPortNumber_Object = MibTableColumn
uplbdPortNumber = _UplbdPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 1, 1, 4),
    _UplbdPortNumber_Type()
)
uplbdPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbdPortNumber.setStatus("mandatory")
_UplbdStartupTime_Type = DisplayString
_UplbdStartupTime_Object = MibTableColumn
uplbdStartupTime = _UplbdStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 1, 1, 5),
    _UplbdStartupTime_Type()
)
uplbdStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbdStartupTime.setStatus("mandatory")
_UplBillingMgrEventStatsTable_Object = MibTable
uplBillingMgrEventStatsTable = _UplBillingMgrEventStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    uplBillingMgrEventStatsTable.setStatus("mandatory")
_UplBillingMgrEventStatsEntry_Object = MibTableRow
uplBillingMgrEventStatsEntry = _UplBillingMgrEventStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 2, 1)
)
uplBillingMgrEventStatsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplbesIpAddress"),
    (0, "OPENWAVE-MIB", "uplbesProcessId"),
)
if mibBuilder.loadTexts:
    uplBillingMgrEventStatsEntry.setStatus("mandatory")
_UplbesIpAddress_Type = IpAddress
_UplbesIpAddress_Object = MibTableColumn
uplbesIpAddress = _UplbesIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 2, 1, 1),
    _UplbesIpAddress_Type()
)
uplbesIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbesIpAddress.setStatus("mandatory")
_UplbesProcessId_Type = Integer32
_UplbesProcessId_Object = MibTableColumn
uplbesProcessId = _UplbesProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 2, 1, 2),
    _UplbesProcessId_Type()
)
uplbesProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbesProcessId.setStatus("mandatory")
_UplbesEventsReceived_Type = Counter32
_UplbesEventsReceived_Object = MibTableColumn
uplbesEventsReceived = _UplbesEventsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 2, 1, 3),
    _UplbesEventsReceived_Type()
)
uplbesEventsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbesEventsReceived.setStatus("mandatory")
_UplbesEventLogFailures_Type = Counter32
_UplbesEventLogFailures_Object = MibTableColumn
uplbesEventLogFailures = _UplbesEventLogFailures_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 2, 1, 4),
    _UplbesEventLogFailures_Type()
)
uplbesEventLogFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbesEventLogFailures.setStatus("mandatory")
_UplbesDirectTransferFailures_Type = Counter32
_UplbesDirectTransferFailures_Object = MibTableColumn
uplbesDirectTransferFailures = _UplbesDirectTransferFailures_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 2, 1, 5),
    _UplbesDirectTransferFailures_Type()
)
uplbesDirectTransferFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbesDirectTransferFailures.setStatus("mandatory")
_UplBillingMgrFileStatsTable_Object = MibTable
uplBillingMgrFileStatsTable = _UplBillingMgrFileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    uplBillingMgrFileStatsTable.setStatus("mandatory")
_UplBillingMgrFileStatsEntry_Object = MibTableRow
uplBillingMgrFileStatsEntry = _UplBillingMgrFileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1)
)
uplBillingMgrFileStatsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplbfsIpAddress"),
    (0, "OPENWAVE-MIB", "uplbfsProcessId"),
)
if mibBuilder.loadTexts:
    uplBillingMgrFileStatsEntry.setStatus("mandatory")
_UplbfsIpAddress_Type = IpAddress
_UplbfsIpAddress_Object = MibTableColumn
uplbfsIpAddress = _UplbfsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 1),
    _UplbfsIpAddress_Type()
)
uplbfsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsIpAddress.setStatus("mandatory")
_UplbfsProcessId_Type = Integer32
_UplbfsProcessId_Object = MibTableColumn
uplbfsProcessId = _UplbfsProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 2),
    _UplbfsProcessId_Type()
)
uplbfsProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsProcessId.setStatus("mandatory")
_UplbfsMaxBillingFileSize_Type = Integer32
_UplbfsMaxBillingFileSize_Object = MibTableColumn
uplbfsMaxBillingFileSize = _UplbfsMaxBillingFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 3),
    _UplbfsMaxBillingFileSize_Type()
)
uplbfsMaxBillingFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsMaxBillingFileSize.setStatus("mandatory")
_UplbfsCompressorName_Type = DisplayString
_UplbfsCompressorName_Object = MibTableColumn
uplbfsCompressorName = _UplbfsCompressorName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 4),
    _UplbfsCompressorName_Type()
)
uplbfsCompressorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsCompressorName.setStatus("mandatory")
_UplbfsBillingFilePath_Type = DisplayString
_UplbfsBillingFilePath_Object = MibTableColumn
uplbfsBillingFilePath = _UplbfsBillingFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 5),
    _UplbfsBillingFilePath_Type()
)
uplbfsBillingFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsBillingFilePath.setStatus("mandatory")
_UplbfsArchiveFilePath_Type = DisplayString
_UplbfsArchiveFilePath_Object = MibTableColumn
uplbfsArchiveFilePath = _UplbfsArchiveFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 6),
    _UplbfsArchiveFilePath_Type()
)
uplbfsArchiveFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsArchiveFilePath.setStatus("mandatory")
_UplbfsFileDiskSpaceUsed_Type = Integer32
_UplbfsFileDiskSpaceUsed_Object = MibTableColumn
uplbfsFileDiskSpaceUsed = _UplbfsFileDiskSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 7),
    _UplbfsFileDiskSpaceUsed_Type()
)
uplbfsFileDiskSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsFileDiskSpaceUsed.setStatus("mandatory")
_UplbfsArchiveDiskSpaceUsed_Type = Integer32
_UplbfsArchiveDiskSpaceUsed_Object = MibTableColumn
uplbfsArchiveDiskSpaceUsed = _UplbfsArchiveDiskSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 3, 1, 8),
    _UplbfsArchiveDiskSpaceUsed_Type()
)
uplbfsArchiveDiskSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplbfsArchiveDiskSpaceUsed.setStatus("mandatory")
_UplBillingMgrTrapInfo_ObjectIdentity = ObjectIdentity
uplBillingMgrTrapInfo = _UplBillingMgrTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 20)
)
_UplbTrapInfo_Type = DisplayString
_UplbTrapInfo_Object = MibScalar
uplbTrapInfo = _UplbTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 6, 20, 1),
    _UplbTrapInfo_Type()
)
uplbTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplbTrapInfo.setStatus("optional")
_UplRadiusServer_ObjectIdentity = ObjectIdentity
uplRadiusServer = _UplRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7)
)
_UplRadiusServerDescriptionTable_Object = MibTable
uplRadiusServerDescriptionTable = _UplRadiusServerDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    uplRadiusServerDescriptionTable.setStatus("mandatory")
_UplRadiusServerDescriptionEntry_Object = MibTableRow
uplRadiusServerDescriptionEntry = _UplRadiusServerDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 1, 1)
)
uplRadiusServerDescriptionEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplrsdIpAddress"),
    (0, "OPENWAVE-MIB", "uplrsdProcessId"),
)
if mibBuilder.loadTexts:
    uplRadiusServerDescriptionEntry.setStatus("mandatory")
_UplrsdIpAddress_Type = IpAddress
_UplrsdIpAddress_Object = MibTableColumn
uplrsdIpAddress = _UplrsdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 1, 1, 1),
    _UplrsdIpAddress_Type()
)
uplrsdIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrsdIpAddress.setStatus("mandatory")
_UplrsdProcessId_Type = Integer32
_UplrsdProcessId_Object = MibTableColumn
uplrsdProcessId = _UplrsdProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 1, 1, 2),
    _UplrsdProcessId_Type()
)
uplrsdProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrsdProcessId.setStatus("mandatory")
_UplrsdHostName_Type = DisplayString
_UplrsdHostName_Object = MibTableColumn
uplrsdHostName = _UplrsdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 1, 1, 3),
    _UplrsdHostName_Type()
)
uplrsdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrsdHostName.setStatus("mandatory")
_UplrsdPortNumber_Type = Integer32
_UplrsdPortNumber_Object = MibTableColumn
uplrsdPortNumber = _UplrsdPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 1, 1, 4),
    _UplrsdPortNumber_Type()
)
uplrsdPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrsdPortNumber.setStatus("mandatory")
_UplrsdStartupTime_Type = DisplayString
_UplrsdStartupTime_Object = MibTableColumn
uplrsdStartupTime = _UplrsdStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 1, 1, 5),
    _UplrsdStartupTime_Type()
)
uplrsdStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrsdStartupTime.setStatus("mandatory")
_UplRadiusServerStatsTable_Object = MibTable
uplRadiusServerStatsTable = _UplRadiusServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    uplRadiusServerStatsTable.setStatus("mandatory")
_UplRadiusServerStatsEntry_Object = MibTableRow
uplRadiusServerStatsEntry = _UplRadiusServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1)
)
uplRadiusServerStatsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplrssIpAddress"),
    (0, "OPENWAVE-MIB", "uplrssProcessId"),
)
if mibBuilder.loadTexts:
    uplRadiusServerStatsEntry.setStatus("mandatory")
_UplrssIpAddress_Type = IpAddress
_UplrssIpAddress_Object = MibTableColumn
uplrssIpAddress = _UplrssIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 1),
    _UplrssIpAddress_Type()
)
uplrssIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssIpAddress.setStatus("mandatory")
_UplrssProcessId_Type = Integer32
_UplrssProcessId_Object = MibTableColumn
uplrssProcessId = _UplrssProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 2),
    _UplrssProcessId_Type()
)
uplrssProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssProcessId.setStatus("mandatory")
_UplrssRasServiceAddress_Type = DisplayString
_UplrssRasServiceAddress_Object = MibTableColumn
uplrssRasServiceAddress = _UplrssRasServiceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 3),
    _UplrssRasServiceAddress_Type()
)
uplrssRasServiceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssRasServiceAddress.setStatus("mandatory")
_UplrssAuthenticationStatus_Type = DisplayString
_UplrssAuthenticationStatus_Object = MibTableColumn
uplrssAuthenticationStatus = _UplrssAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 4),
    _UplrssAuthenticationStatus_Type()
)
uplrssAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssAuthenticationStatus.setStatus("mandatory")
_UplrssStartAccMsgReceived_Type = Counter32
_UplrssStartAccMsgReceived_Object = MibTableColumn
uplrssStartAccMsgReceived = _UplrssStartAccMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 5),
    _UplrssStartAccMsgReceived_Type()
)
uplrssStartAccMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssStartAccMsgReceived.setStatus("mandatory")
_UplrssInterimAccMsgReceived_Type = Counter32
_UplrssInterimAccMsgReceived_Object = MibTableColumn
uplrssInterimAccMsgReceived = _UplrssInterimAccMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 6),
    _UplrssInterimAccMsgReceived_Type()
)
uplrssInterimAccMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssInterimAccMsgReceived.setStatus("mandatory")
_UplrssStopAccMsgReceived_Type = Counter32
_UplrssStopAccMsgReceived_Object = MibTableColumn
uplrssStopAccMsgReceived = _UplrssStopAccMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 7),
    _UplrssStopAccMsgReceived_Type()
)
uplrssStopAccMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssStopAccMsgReceived.setStatus("mandatory")
_UplrssIpMsisdnPairsInserted_Type = Counter32
_UplrssIpMsisdnPairsInserted_Object = MibTableColumn
uplrssIpMsisdnPairsInserted = _UplrssIpMsisdnPairsInserted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 8),
    _UplrssIpMsisdnPairsInserted_Type()
)
uplrssIpMsisdnPairsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssIpMsisdnPairsInserted.setStatus("mandatory")
_UplrssIpMsisdnPairsUpdated_Type = Counter32
_UplrssIpMsisdnPairsUpdated_Object = MibTableColumn
uplrssIpMsisdnPairsUpdated = _UplrssIpMsisdnPairsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 9),
    _UplrssIpMsisdnPairsUpdated_Type()
)
uplrssIpMsisdnPairsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssIpMsisdnPairsUpdated.setStatus("mandatory")
_UplrssIpMsisdnPairsDeleted_Type = Counter32
_UplrssIpMsisdnPairsDeleted_Object = MibTableColumn
uplrssIpMsisdnPairsDeleted = _UplrssIpMsisdnPairsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 2, 1, 10),
    _UplrssIpMsisdnPairsDeleted_Type()
)
uplrssIpMsisdnPairsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplrssIpMsisdnPairsDeleted.setStatus("mandatory")
_UplRadiusServerTrapInfo_ObjectIdentity = ObjectIdentity
uplRadiusServerTrapInfo = _UplRadiusServerTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 20)
)
_UplrsTrapInfo_Type = DisplayString
_UplrsTrapInfo_Object = MibScalar
uplrsTrapInfo = _UplrsTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 7, 20, 1),
    _UplrsTrapInfo_Type()
)
uplrsTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplrsTrapInfo.setStatus("optional")
_UplCertRequester_ObjectIdentity = ObjectIdentity
uplCertRequester = _UplCertRequester_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8)
)
_UplCertRequesterDescriptionTable_Object = MibTable
uplCertRequesterDescriptionTable = _UplCertRequesterDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    uplCertRequesterDescriptionTable.setStatus("mandatory")
_UplCertRequesterDescriptionEntry_Object = MibTableRow
uplCertRequesterDescriptionEntry = _UplCertRequesterDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1, 1)
)
uplCertRequesterDescriptionEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uplcrdIpAddress"),
    (0, "OPENWAVE-MIB", "uplcrdProcessId"),
)
if mibBuilder.loadTexts:
    uplCertRequesterDescriptionEntry.setStatus("mandatory")
_UplcrdIpAddress_Type = IpAddress
_UplcrdIpAddress_Object = MibTableColumn
uplcrdIpAddress = _UplcrdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1, 1, 1),
    _UplcrdIpAddress_Type()
)
uplcrdIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplcrdIpAddress.setStatus("mandatory")
_UplcrdProcessId_Type = Integer32
_UplcrdProcessId_Object = MibTableColumn
uplcrdProcessId = _UplcrdProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1, 1, 2),
    _UplcrdProcessId_Type()
)
uplcrdProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplcrdProcessId.setStatus("mandatory")
_UplcrdHostName_Type = DisplayString
_UplcrdHostName_Object = MibTableColumn
uplcrdHostName = _UplcrdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1, 1, 3),
    _UplcrdHostName_Type()
)
uplcrdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplcrdHostName.setStatus("mandatory")
_UplcrdUpdateInterval_Type = Integer32
_UplcrdUpdateInterval_Object = MibTableColumn
uplcrdUpdateInterval = _UplcrdUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1, 1, 4),
    _UplcrdUpdateInterval_Type()
)
uplcrdUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplcrdUpdateInterval.setStatus("mandatory")
_UplcrdRequestAllowance_Type = Integer32
_UplcrdRequestAllowance_Object = MibTableColumn
uplcrdRequestAllowance = _UplcrdRequestAllowance_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1, 1, 5),
    _UplcrdRequestAllowance_Type()
)
uplcrdRequestAllowance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplcrdRequestAllowance.setStatus("mandatory")
_UplcrdStartupTime_Type = DisplayString
_UplcrdStartupTime_Object = MibTableColumn
uplcrdStartupTime = _UplcrdStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 1, 1, 6),
    _UplcrdStartupTime_Type()
)
uplcrdStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplcrdStartupTime.setStatus("mandatory")
_UplCertRequesterTrapInfo_ObjectIdentity = ObjectIdentity
uplCertRequesterTrapInfo = _UplCertRequesterTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 20)
)
_UplcrTrapInfo_Type = DisplayString
_UplcrTrapInfo_Object = MibScalar
uplcrTrapInfo = _UplcrTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 1, 8, 20, 1),
    _UplcrTrapInfo_Type()
)
uplcrTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uplcrTrapInfo.setStatus("optional")
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
_UpPushProxy_ObjectIdentity = ObjectIdentity
upPushProxy = _UpPushProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5)
)
_UpPushPap_ObjectIdentity = ObjectIdentity
upPushPap = _UpPushPap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1)
)
_UpPushPapDescriptionTable_Object = MibTable
upPushPapDescriptionTable = _UpPushPapDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    upPushPapDescriptionTable.setStatus("mandatory")
_UpPushPapDescriptionEntry_Object = MibTableRow
upPushPapDescriptionEntry = _UpPushPapDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1)
)
upPushPapDescriptionEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uppdPAPIndex"),
)
if mibBuilder.loadTexts:
    upPushPapDescriptionEntry.setStatus("mandatory")
_UppdPAPIndex_Type = Integer32
_UppdPAPIndex_Object = MibTableColumn
uppdPAPIndex = _UppdPAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 1),
    _UppdPAPIndex_Type()
)
uppdPAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdPAPIndex.setStatus("mandatory")
_UppdPAPIdentifier_Type = Integer32
_UppdPAPIdentifier_Object = MibTableColumn
uppdPAPIdentifier = _UppdPAPIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 2),
    _UppdPAPIdentifier_Type()
)
uppdPAPIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdPAPIdentifier.setStatus("mandatory")
_UppdProcessId_Type = Integer32
_UppdProcessId_Object = MibTableColumn
uppdProcessId = _UppdProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 3),
    _UppdProcessId_Type()
)
uppdProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdProcessId.setStatus("mandatory")
_UppdHostName_Type = DisplayString
_UppdHostName_Object = MibTableColumn
uppdHostName = _UppdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 4),
    _UppdHostName_Type()
)
uppdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdHostName.setStatus("mandatory")
_UppdPublicHTTPPortNumber_Type = Integer32
_UppdPublicHTTPPortNumber_Object = MibTableColumn
uppdPublicHTTPPortNumber = _UppdPublicHTTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 5),
    _UppdPublicHTTPPortNumber_Type()
)
uppdPublicHTTPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdPublicHTTPPortNumber.setStatus("mandatory")
_UppdPublicHTTPSPortNumber_Type = Integer32
_UppdPublicHTTPSPortNumber_Object = MibTableColumn
uppdPublicHTTPSPortNumber = _UppdPublicHTTPSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 6),
    _UppdPublicHTTPSPortNumber_Type()
)
uppdPublicHTTPSPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdPublicHTTPSPortNumber.setStatus("mandatory")
_UppdPrivateHTTPPortNumber_Type = Integer32
_UppdPrivateHTTPPortNumber_Object = MibTableColumn
uppdPrivateHTTPPortNumber = _UppdPrivateHTTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 7),
    _UppdPrivateHTTPPortNumber_Type()
)
uppdPrivateHTTPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdPrivateHTTPPortNumber.setStatus("mandatory")
_UppdStartupTime_Type = DisplayString
_UppdStartupTime_Object = MibTableColumn
uppdStartupTime = _UppdStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 1, 1, 8),
    _UppdStartupTime_Type()
)
uppdStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppdStartupTime.setStatus("mandatory")
_UpPushPapNtfnStatsTable_Object = MibTable
upPushPapNtfnStatsTable = _UpPushPapNtfnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    upPushPapNtfnStatsTable.setStatus("mandatory")
_UpPushPapNtfnStatsEntry_Object = MibTableRow
upPushPapNtfnStatsEntry = _UpPushPapNtfnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1)
)
upPushPapNtfnStatsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uppnsPAPIndex"),
)
if mibBuilder.loadTexts:
    upPushPapNtfnStatsEntry.setStatus("mandatory")
_UppnsPAPIndex_Type = Integer32
_UppnsPAPIndex_Object = MibTableColumn
uppnsPAPIndex = _UppnsPAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 1),
    _UppnsPAPIndex_Type()
)
uppnsPAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPAPIndex.setStatus("mandatory")
_UppnsPAPIdentifier_Type = Integer32
_UppnsPAPIdentifier_Object = MibTableColumn
uppnsPAPIdentifier = _UppnsPAPIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 2),
    _UppnsPAPIdentifier_Type()
)
uppnsPAPIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPAPIdentifier.setStatus("mandatory")
_UppnsPublicHTTPReqReceived_Type = Counter32
_UppnsPublicHTTPReqReceived_Object = MibTableColumn
uppnsPublicHTTPReqReceived = _UppnsPublicHTTPReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 3),
    _UppnsPublicHTTPReqReceived_Type()
)
uppnsPublicHTTPReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPublicHTTPReqReceived.setStatus("mandatory")
_UppnsPrivateHTTPReqReceived_Type = Counter32
_UppnsPrivateHTTPReqReceived_Object = MibTableColumn
uppnsPrivateHTTPReqReceived = _UppnsPrivateHTTPReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 4),
    _UppnsPrivateHTTPReqReceived_Type()
)
uppnsPrivateHTTPReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPrivateHTTPReqReceived.setStatus("mandatory")
_UppnsPublicHTTPSReqReceived_Type = Counter32
_UppnsPublicHTTPSReqReceived_Object = MibTableColumn
uppnsPublicHTTPSReqReceived = _UppnsPublicHTTPSReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 5),
    _UppnsPublicHTTPSReqReceived_Type()
)
uppnsPublicHTTPSReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPublicHTTPSReqReceived.setStatus("mandatory")
_UppnsPublicHTTPReqAccepted_Type = Counter32
_UppnsPublicHTTPReqAccepted_Object = MibTableColumn
uppnsPublicHTTPReqAccepted = _UppnsPublicHTTPReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 6),
    _UppnsPublicHTTPReqAccepted_Type()
)
uppnsPublicHTTPReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPublicHTTPReqAccepted.setStatus("mandatory")
_UppnsPrivateHTTPReqAccepted_Type = Counter32
_UppnsPrivateHTTPReqAccepted_Object = MibTableColumn
uppnsPrivateHTTPReqAccepted = _UppnsPrivateHTTPReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 7),
    _UppnsPrivateHTTPReqAccepted_Type()
)
uppnsPrivateHTTPReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPrivateHTTPReqAccepted.setStatus("mandatory")
_UppnsPublicHTTPSReqAccepted_Type = Counter32
_UppnsPublicHTTPSReqAccepted_Object = MibTableColumn
uppnsPublicHTTPSReqAccepted = _UppnsPublicHTTPSReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 8),
    _UppnsPublicHTTPSReqAccepted_Type()
)
uppnsPublicHTTPSReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsPublicHTTPSReqAccepted.setStatus("mandatory")
_UppnsAvgNtfnsReceivedPerSec_Type = Integer32
_UppnsAvgNtfnsReceivedPerSec_Object = MibTableColumn
uppnsAvgNtfnsReceivedPerSec = _UppnsAvgNtfnsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 9),
    _UppnsAvgNtfnsReceivedPerSec_Type()
)
uppnsAvgNtfnsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsAvgNtfnsReceivedPerSec.setStatus("mandatory")
_UppnsAvgNtfnsAcceptedPerSec_Type = Integer32
_UppnsAvgNtfnsAcceptedPerSec_Object = MibTableColumn
uppnsAvgNtfnsAcceptedPerSec = _UppnsAvgNtfnsAcceptedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 2, 1, 10),
    _UppnsAvgNtfnsAcceptedPerSec_Type()
)
uppnsAvgNtfnsAcceptedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppnsAvgNtfnsAcceptedPerSec.setStatus("mandatory")
_UpPushPapForwardedNtfnsTable_Object = MibTable
upPushPapForwardedNtfnsTable = _UpPushPapForwardedNtfnsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3)
)
if mibBuilder.loadTexts:
    upPushPapForwardedNtfnsTable.setStatus("mandatory")
_UpPushPapForwardedNtfnsEntry_Object = MibTableRow
upPushPapForwardedNtfnsEntry = _UpPushPapForwardedNtfnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3, 1)
)
upPushPapForwardedNtfnsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uppfnPAPIndex"),
)
if mibBuilder.loadTexts:
    upPushPapForwardedNtfnsEntry.setStatus("mandatory")
_UppfnPAPIndex_Type = Integer32
_UppfnPAPIndex_Object = MibTableColumn
uppfnPAPIndex = _UppfnPAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3, 1, 1),
    _UppfnPAPIndex_Type()
)
uppfnPAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppfnPAPIndex.setStatus("mandatory")
_UppfnPAPIdentifier_Type = Integer32
_UppfnPAPIdentifier_Object = MibTableColumn
uppfnPAPIdentifier = _UppfnPAPIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3, 1, 2),
    _UppfnPAPIdentifier_Type()
)
uppfnPAPIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppfnPAPIdentifier.setStatus("mandatory")
_UppfnPPGForwardedNtfns_Type = Counter32
_UppfnPPGForwardedNtfns_Object = MibTableColumn
uppfnPPGForwardedNtfns = _UppfnPPGForwardedNtfns_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3, 1, 3),
    _UppfnPPGForwardedNtfns_Type()
)
uppfnPPGForwardedNtfns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppfnPPGForwardedNtfns.setStatus("mandatory")
_UppfnPPGFailedNtfns_Type = Counter32
_UppfnPPGFailedNtfns_Object = MibTableColumn
uppfnPPGFailedNtfns = _UppfnPPGFailedNtfns_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3, 1, 4),
    _UppfnPPGFailedNtfns_Type()
)
uppfnPPGFailedNtfns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppfnPPGFailedNtfns.setStatus("mandatory")
_UppfnMessengerForwardedNtfns_Type = Counter32
_UppfnMessengerForwardedNtfns_Object = MibTableColumn
uppfnMessengerForwardedNtfns = _UppfnMessengerForwardedNtfns_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3, 1, 5),
    _UppfnMessengerForwardedNtfns_Type()
)
uppfnMessengerForwardedNtfns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppfnMessengerForwardedNtfns.setStatus("mandatory")
_UppfnMessengerFailedNtfns_Type = Counter32
_UppfnMessengerFailedNtfns_Object = MibTableColumn
uppfnMessengerFailedNtfns = _UppfnMessengerFailedNtfns_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 3, 1, 6),
    _UppfnMessengerFailedNtfns_Type()
)
uppfnMessengerFailedNtfns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppfnMessengerFailedNtfns.setStatus("mandatory")
_UpPushPapTrapInfo_ObjectIdentity = ObjectIdentity
upPushPapTrapInfo = _UpPushPapTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 20)
)
_UppTrapInfo_Type = DisplayString
_UppTrapInfo_Object = MibScalar
uppTrapInfo = _UppTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 1, 20, 1),
    _UppTrapInfo_Type()
)
uppTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uppTrapInfo.setStatus("optional")
_UpPushPpg_ObjectIdentity = ObjectIdentity
upPushPpg = _UpPushPpg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2)
)
_UpPushPpgDescriptionTable_Object = MibTable
upPushPpgDescriptionTable = _UpPushPpgDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    upPushPpgDescriptionTable.setStatus("mandatory")
_UpPushPpgDescriptionEntry_Object = MibTableRow
upPushPpgDescriptionEntry = _UpPushPpgDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1, 1)
)
upPushPpgDescriptionEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uppgdPPGIndex"),
)
if mibBuilder.loadTexts:
    upPushPpgDescriptionEntry.setStatus("mandatory")
_UppgdPPGIndex_Type = Integer32
_UppgdPPGIndex_Object = MibTableColumn
uppgdPPGIndex = _UppgdPPGIndex_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1, 1, 1),
    _UppgdPPGIndex_Type()
)
uppgdPPGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgdPPGIndex.setStatus("mandatory")
_UppgdPPGIdentifier_Type = Integer32
_UppgdPPGIdentifier_Object = MibTableColumn
uppgdPPGIdentifier = _UppgdPPGIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1, 1, 2),
    _UppgdPPGIdentifier_Type()
)
uppgdPPGIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgdPPGIdentifier.setStatus("mandatory")
_UppgdProcessId_Type = Integer32
_UppgdProcessId_Object = MibTableColumn
uppgdProcessId = _UppgdProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1, 1, 3),
    _UppgdProcessId_Type()
)
uppgdProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgdProcessId.setStatus("mandatory")
_UppgdHostName_Type = DisplayString
_UppgdHostName_Object = MibTableColumn
uppgdHostName = _UppgdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1, 1, 4),
    _UppgdHostName_Type()
)
uppgdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgdHostName.setStatus("mandatory")
_UppgdMsgServerPortNumber_Type = Integer32
_UppgdMsgServerPortNumber_Object = MibTableColumn
uppgdMsgServerPortNumber = _UppgdMsgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1, 1, 5),
    _UppgdMsgServerPortNumber_Type()
)
uppgdMsgServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgdMsgServerPortNumber.setStatus("mandatory")
_UppgdStartupTime_Type = DisplayString
_UppgdStartupTime_Object = MibTableColumn
uppgdStartupTime = _UppgdStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 1, 1, 6),
    _UppgdStartupTime_Type()
)
uppgdStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgdStartupTime.setStatus("mandatory")
_UpPushPpgNtfnStatsTable_Object = MibTable
upPushPpgNtfnStatsTable = _UpPushPpgNtfnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 2)
)
if mibBuilder.loadTexts:
    upPushPpgNtfnStatsTable.setStatus("mandatory")
_UpPushPpgNtfnStatsEntry_Object = MibTableRow
upPushPpgNtfnStatsEntry = _UpPushPpgNtfnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 2, 1)
)
upPushPpgNtfnStatsEntry.setIndexNames(
    (0, "OPENWAVE-MIB", "uppgnsPPGIndex"),
)
if mibBuilder.loadTexts:
    upPushPpgNtfnStatsEntry.setStatus("mandatory")
_UppgnsPPGIndex_Type = Integer32
_UppgnsPPGIndex_Object = MibTableColumn
uppgnsPPGIndex = _UppgnsPPGIndex_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 2, 1, 1),
    _UppgnsPPGIndex_Type()
)
uppgnsPPGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgnsPPGIndex.setStatus("mandatory")
_UppgnsPPGIdentifier_Type = Integer32
_UppgnsPPGIdentifier_Object = MibTableColumn
uppgnsPPGIdentifier = _UppgnsPPGIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 2, 1, 2),
    _UppgnsPPGIdentifier_Type()
)
uppgnsPPGIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgnsPPGIdentifier.setStatus("mandatory")
_UppgnsTotalNumOfPendingNtfns_Type = Counter32
_UppgnsTotalNumOfPendingNtfns_Object = MibTableColumn
uppgnsTotalNumOfPendingNtfns = _UppgnsTotalNumOfPendingNtfns_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 2, 1, 3),
    _UppgnsTotalNumOfPendingNtfns_Type()
)
uppgnsTotalNumOfPendingNtfns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgnsTotalNumOfPendingNtfns.setStatus("mandatory")
_UppgnsAvgNtfnsDeliveredPerSec_Type = Integer32
_UppgnsAvgNtfnsDeliveredPerSec_Object = MibTableColumn
uppgnsAvgNtfnsDeliveredPerSec = _UppgnsAvgNtfnsDeliveredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 2, 1, 4),
    _UppgnsAvgNtfnsDeliveredPerSec_Type()
)
uppgnsAvgNtfnsDeliveredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgnsAvgNtfnsDeliveredPerSec.setStatus("mandatory")
_UppgnsAvgNtfnsMarkedUnDelvrPerSec_Type = Integer32
_UppgnsAvgNtfnsMarkedUnDelvrPerSec_Object = MibTableColumn
uppgnsAvgNtfnsMarkedUnDelvrPerSec = _UppgnsAvgNtfnsMarkedUnDelvrPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 2, 1, 5),
    _UppgnsAvgNtfnsMarkedUnDelvrPerSec_Type()
)
uppgnsAvgNtfnsMarkedUnDelvrPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uppgnsAvgNtfnsMarkedUnDelvrPerSec.setStatus("mandatory")
_UpPushPpgTrapInfo_ObjectIdentity = ObjectIdentity
upPushPpgTrapInfo = _UpPushPpgTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 20)
)
_UppgTrapInfo_Type = DisplayString
_UppgTrapInfo_Object = MibScalar
uppgTrapInfo = _UppgTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 2, 20, 1),
    _UppgTrapInfo_Type()
)
uppgTrapInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uppgTrapInfo.setStatus("optional")
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
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitChildProcessHostName"),
        ("OPENWAVE-MIB", "upitChildProcessType"),
        ("OPENWAVE-MIB", "upitChildProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessStart.setStatus(
        ""
    )

upiChildProcessShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 301)
)
upiChildProcessShutdown.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitChildProcessHostName"),
        ("OPENWAVE-MIB", "upitChildProcessType"),
        ("OPENWAVE-MIB", "upitChildProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessShutdown.setStatus(
        ""
    )

upiInitFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 302)
)
upiInitFailToStart.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiInitFailToStart.setStatus(
        ""
    )

upiInitShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 303)
)
upiInitShutdown.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiInitShutdown.setStatus(
        ""
    )

upiAllChildProcessesStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 304)
)
upiAllChildProcessesStop.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiAllChildProcessesStop.setStatus(
        ""
    )

upiAllChildProcessesRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 305)
)
upiAllChildProcessesRestart.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiAllChildProcessesRestart.setStatus(
        ""
    )

upiDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 306)
)
upiDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiDatabaseConnectionDown.setStatus(
        ""
    )

upiDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 307)
)
upiDatabaseConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiDatabaseConnectionUp.setStatus(
        ""
    )

upiChildProcessFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 308)
)
upiChildProcessFailToStart.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitChildProcessType"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessFailToStart.setStatus(
        ""
    )

upiNoChildProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 309)
)
upiNoChildProcess.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiNoChildProcess.setStatus(
        ""
    )

upiChildProcessesBelowMinimum = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 1, 0, 310)
)
upiChildProcessesBelowMinimum.setObjects(
      *(("OPENWAVE-MIB", "upidInitHostName"),
        ("OPENWAVE-MIB", "upidInitProcessType"),
        ("OPENWAVE-MIB", "upidInitProcessId"),
        ("OPENWAVE-MIB", "upitChildProcessType"),
        ("OPENWAVE-MIB", "upitTrapInfo"))
)
if mibBuilder.loadTexts:
    upiChildProcessesBelowMinimum.setStatus(
        ""
    )

upldStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 100)
)
upldStartup.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldStartup.setStatus(
        ""
    )

upldShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 101)
)
upldShutdown.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldShutdown.setStatus(
        ""
    )

upldInvalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 102)
)
upldInvalidConfig.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldInvalidConfig.setStatus(
        ""
    )

upldUplAgentConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 103)
)
upldUplAgentConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldUplAgentId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldUplAgentConnectionDown.setStatus(
        ""
    )

upldDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 104)
)
upldDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldDatabaseConnectionDown.setStatus(
        ""
    )

upldOutOfResouce = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 105)
)
upldOutOfResouce.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldOutOfResouce.setStatus(
        ""
    )

upldUplAgentConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 106)
)
upldUplAgentConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldUplAgentId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldUplAgentConnectionUp.setStatus(
        ""
    )

upldDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 107)
)
upldDatabaseConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldDatabaseConnectionUp.setStatus(
        ""
    )

upldUplRadiusConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 108)
)
upldUplRadiusConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "upldHostName"),
        ("OPENWAVE-MIB", "upldProcessId"),
        ("OPENWAVE-MIB", "upldTrapInfo"))
)
if mibBuilder.loadTexts:
    upldUplRadiusConnectionDown.setStatus(
        ""
    )

uplaStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 200)
)
uplaStartup.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaStartup.setStatus(
        ""
    )

uplaShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 201)
)
uplaShutdown.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaShutdown.setStatus(
        ""
    )

uplaDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 202)
)
uplaDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaDatabaseConnectionDown.setStatus(
        ""
    )

uplaFaxMgrConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 203)
)
uplaFaxMgrConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaFaxMgrConnectionDown.setStatus(
        ""
    )

uplaMessengerConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 204)
)
uplaMessengerConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaMessengerConnectionDown.setStatus(
        ""
    )

uplaInvalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 205)
)
uplaInvalidConfig.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaInvalidConfig.setStatus(
        ""
    )

uplaInternalFatalErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 206)
)
uplaInternalFatalErrors.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaInternalFatalErrors.setStatus(
        ""
    )

uplaOutOfResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 207)
)
uplaOutOfResource.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaOutOfResource.setStatus(
        ""
    )

uplaDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 208)
)
uplaDatabaseConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaDatabaseConnectionUp.setStatus(
        ""
    )

uplaBillingInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 209)
)
uplaBillingInitError.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaBillingInitError.setStatus(
        ""
    )

uplaBillingLogError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 210)
)
uplaBillingLogError.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaBillingLogError.setStatus(
        ""
    )

uplaDynamicUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 211)
)
uplaDynamicUpdateStarted.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaDynamicUpdateStarted.setStatus(
        ""
    )

uplaDynamicUpdateStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 212)
)
uplaDynamicUpdateStopped.setObjects(
      *(("OPENWAVE-MIB", "uplaAgentIdentifier"),
        ("OPENWAVE-MIB", "uplaHostName"),
        ("OPENWAVE-MIB", "uplaProcessId"),
        ("OPENWAVE-MIB", "uplaTrapInfo"))
)
if mibBuilder.loadTexts:
    uplaDynamicUpdateStopped.setStatus(
        ""
    )

uplrStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 500)
)
uplrStartup.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrStartup.setStatus(
        ""
    )

uplrShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 501)
)
uplrShutdown.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrShutdown.setStatus(
        ""
    )

uplrDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 502)
)
uplrDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrDatabaseConnectionDown.setStatus(
        ""
    )

uplrDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 503)
)
uplrDatabaseConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrDatabaseConnectionUp.setStatus(
        ""
    )

uplrInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 505)
)
uplrInternalError.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrInternalError.setStatus(
        ""
    )

uplrSMSCConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 506)
)
uplrSMSCConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrSMSCConnectionDown.setStatus(
        ""
    )

uplrSMSCConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 507)
)
uplrSMSCConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrSMSCConnectionUp.setStatus(
        ""
    )

uplrClientConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 508)
)
uplrClientConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrClientConnectionDown.setStatus(
        ""
    )

uplrClientConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 509)
)
uplrClientConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrClientConnectionUp.setStatus(
        ""
    )

uplrNbRouterConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 510)
)
uplrNbRouterConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplrClientIpAddress"),
        ("OPENWAVE-MIB", "uplrClientHostName"),
        ("OPENWAVE-MIB", "uplrClientProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrNbRouterConnectionDown.setStatus(
        ""
    )

uplrNbRouterConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 511)
)
uplrNbRouterConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "uplrClientIpAddress"),
        ("OPENWAVE-MIB", "uplrClientHostName"),
        ("OPENWAVE-MIB", "uplrClientProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrNbRouterConnectionUp.setStatus(
        ""
    )

uplrProtocolError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 512)
)
uplrProtocolError.setObjects(
      *(("OPENWAVE-MIB", "uplrClientIpAddress"),
        ("OPENWAVE-MIB", "uplrClientHostName"),
        ("OPENWAVE-MIB", "uplrClientProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrProtocolError.setStatus(
        ""
    )

uplrBillingInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 513)
)
uplrBillingInitError.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrBillingInitError.setStatus(
        ""
    )

uplrBillingLogError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 514)
)
uplrBillingLogError.setObjects(
      *(("OPENWAVE-MIB", "uplrdHostName"),
        ("OPENWAVE-MIB", "uplrdProcessId"),
        ("OPENWAVE-MIB", "uplrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrBillingLogError.setStatus(
        ""
    )

uplmStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 600)
)
uplmStartup.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmStartup.setStatus(
        ""
    )

uplmShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 601)
)
uplmShutdown.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmShutdown.setStatus(
        ""
    )

uplmDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 602)
)
uplmDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmDatabaseConnectionDown.setStatus(
        ""
    )

uplmDatabaseConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 603)
)
uplmDatabaseConnectionUp.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmDatabaseConnectionUp.setStatus(
        ""
    )

uplmInvalidConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 604)
)
uplmInvalidConfig.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmInvalidConfig.setStatus(
        ""
    )

uplmInternalErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 605)
)
uplmInternalErrors.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmInternalErrors.setStatus(
        ""
    )

uplmAgentConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 606)
)
uplmAgentConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmAgentConnectionDown.setStatus(
        ""
    )

uplmPublicHTTPServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 607)
)
uplmPublicHTTPServiceStarted.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPublicHTTPServiceStarted.setStatus(
        ""
    )

uplmPublicHTTPServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 608)
)
uplmPublicHTTPServiceDown.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPublicHTTPServiceDown.setStatus(
        ""
    )

uplmPrivateHTTPServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 609)
)
uplmPrivateHTTPServiceDown.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPrivateHTTPServiceDown.setStatus(
        ""
    )

uplmPublicHTTPSServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 610)
)
uplmPublicHTTPSServiceDown.setObjects(
      *(("OPENWAVE-MIB", "uplmdIpAddress"),
        ("OPENWAVE-MIB", "uplmdHostName"),
        ("OPENWAVE-MIB", "uplmdProcessId"),
        ("OPENWAVE-MIB", "uplmTrapInfo"))
)
if mibBuilder.loadTexts:
    uplmPublicHTTPSServiceDown.setStatus(
        ""
    )

uplwCLIDMappingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 701)
)
uplwCLIDMappingError.setObjects(
      *(("OPENWAVE-MIB", "uplwHostName"),
        ("OPENWAVE-MIB", "uplwProcessId"),
        ("OPENWAVE-MIB", "uplwTrapInfo"))
)
if mibBuilder.loadTexts:
    uplwCLIDMappingError.setStatus(
        ""
    )

uplbStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 800)
)
uplbStartup.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbStartup.setStatus(
        ""
    )

uplbShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 801)
)
uplbShutdown.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbShutdown.setStatus(
        ""
    )

uplbDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 802)
)
uplbDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbDatabaseConnectionDown.setStatus(
        ""
    )

uplbBillingLogFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 803)
)
uplbBillingLogFileError.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbBillingLogFileError.setStatus(
        ""
    )

uplbBillingDirectTransferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 804)
)
uplbBillingDirectTransferError.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbBillingDirectTransferError.setStatus(
        ""
    )

uplbDiskSpaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 805)
)
uplbDiskSpaceError.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbDiskSpaceError.setStatus(
        ""
    )

uplbDiskSpaceLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 806)
)
uplbDiskSpaceLow.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbDiskSpaceLow.setStatus(
        ""
    )

uplbDiskSpaceCriticallyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 807)
)
uplbDiskSpaceCriticallyLow.setObjects(
      *(("OPENWAVE-MIB", "uplbdIpAddress"),
        ("OPENWAVE-MIB", "uplbdHostName"),
        ("OPENWAVE-MIB", "uplbdProcessId"),
        ("OPENWAVE-MIB", "uplbTrapInfo"))
)
if mibBuilder.loadTexts:
    uplbDiskSpaceCriticallyLow.setStatus(
        ""
    )

uplrsStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 900)
)
uplrsStartup.setObjects(
      *(("OPENWAVE-MIB", "uplrsdIpAddress"),
        ("OPENWAVE-MIB", "uplrsdHostName"),
        ("OPENWAVE-MIB", "uplrsdProcessId"),
        ("OPENWAVE-MIB", "uplrsTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrsStartup.setStatus(
        ""
    )

uplrsFailedToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 901)
)
uplrsFailedToStart.setObjects(
      *(("OPENWAVE-MIB", "uplrsdIpAddress"),
        ("OPENWAVE-MIB", "uplrsdHostName"),
        ("OPENWAVE-MIB", "uplrsdProcessId"),
        ("OPENWAVE-MIB", "uplrsTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrsFailedToStart.setStatus(
        ""
    )

uplrsDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 902)
)
uplrsDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uplrsdIpAddress"),
        ("OPENWAVE-MIB", "uplrsdHostName"),
        ("OPENWAVE-MIB", "uplrsdProcessId"),
        ("OPENWAVE-MIB", "uplrsTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrsDatabaseConnectionDown.setStatus(
        ""
    )

uplrsBillingInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 903)
)
uplrsBillingInitError.setObjects(
      *(("OPENWAVE-MIB", "uplrsdIpAddress"),
        ("OPENWAVE-MIB", "uplrsdHostName"),
        ("OPENWAVE-MIB", "uplrsdProcessId"),
        ("OPENWAVE-MIB", "uplrsTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrsBillingInitError.setStatus(
        ""
    )

uplrsBillingLogError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 904)
)
uplrsBillingLogError.setObjects(
      *(("OPENWAVE-MIB", "uplrsdIpAddress"),
        ("OPENWAVE-MIB", "uplrsdHostName"),
        ("OPENWAVE-MIB", "uplrsdProcessId"),
        ("OPENWAVE-MIB", "uplrsTrapInfo"))
)
if mibBuilder.loadTexts:
    uplrsBillingLogError.setStatus(
        ""
    )

uplcrStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 1200)
)
uplcrStartup.setObjects(
      *(("OPENWAVE-MIB", "uplcrdIpAddress"),
        ("OPENWAVE-MIB", "uplcrdHostName"),
        ("OPENWAVE-MIB", "uplcrdProcessId"),
        ("OPENWAVE-MIB", "uplcrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplcrStartup.setStatus(
        ""
    )

uplcrFatalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 1201)
)
uplcrFatalError.setObjects(
      *(("OPENWAVE-MIB", "uplcrdIpAddress"),
        ("OPENWAVE-MIB", "uplcrdHostName"),
        ("OPENWAVE-MIB", "uplcrdProcessId"),
        ("OPENWAVE-MIB", "uplcrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplcrFatalError.setStatus(
        ""
    )

uplcrCertificateUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 1202)
)
uplcrCertificateUpdateFailed.setObjects(
      *(("OPENWAVE-MIB", "uplcrdIpAddress"),
        ("OPENWAVE-MIB", "uplcrdHostName"),
        ("OPENWAVE-MIB", "uplcrdProcessId"),
        ("OPENWAVE-MIB", "uplcrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplcrCertificateUpdateFailed.setStatus(
        ""
    )

uplcrInvalidCertResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 2, 0, 1203)
)
uplcrInvalidCertResponse.setObjects(
      *(("OPENWAVE-MIB", "uplcrdIpAddress"),
        ("OPENWAVE-MIB", "uplcrdHostName"),
        ("OPENWAVE-MIB", "uplcrdProcessId"),
        ("OPENWAVE-MIB", "uplcrTrapInfo"))
)
if mibBuilder.loadTexts:
    uplcrInvalidCertResponse.setStatus(
        ""
    )

upsProxyServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 400)
)
upsProxyServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceDown.setStatus(
        ""
    )

upsProxyServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 401)
)
upsProxyServiceSlow.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceSlow.setStatus(
        ""
    )

upsPushServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 402)
)
upsPushServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsPushServiceDown.setStatus(
        ""
    )

upsBookmarksServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 403)
)
upsBookmarksServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceDown.setStatus(
        ""
    )

upsBookmarksServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 404)
)
upsBookmarksServiceSlow.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceSlow.setStatus(
        ""
    )

upsHomePageServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 405)
)
upsHomePageServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsHomePageServiceDown.setStatus(
        ""
    )

upsUPWebServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 406)
)
upsUPWebServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceDown.setStatus(
        ""
    )

upsUPWebServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 407)
)
upsUPWebServiceSlow.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceSlow.setStatus(
        ""
    )

upsUPAdminServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 408)
)
upsUPAdminServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPAdminServiceDown.setStatus(
        ""
    )

upsUPMailServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 409)
)
upsUPMailServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceDown.setStatus(
        ""
    )

upsUPMailServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 410)
)
upsUPMailServiceSlow.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceSlow.setStatus(
        ""
    )

upsUPPimServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 411)
)
upsUPPimServiceDown.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceDown.setStatus(
        ""
    )

upsUPPimServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 412)
)
upsUPPimServiceSlow.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceSlow.setStatus(
        ""
    )

upsHomePageServiceSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 413)
)
upsHomePageServiceSlow.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsHomePageServiceSlow.setStatus(
        ""
    )

upsProxyServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 414)
)
upsProxyServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceUp.setStatus(
        ""
    )

upsProxyServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 415)
)
upsProxyServiceNormal.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsProxyServiceNormal.setStatus(
        ""
    )

upsPushServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 416)
)
upsPushServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsPushServiceUp.setStatus(
        ""
    )

upsBookmarksServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 417)
)
upsBookmarksServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceUp.setStatus(
        ""
    )

upsBookmarksServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 418)
)
upsBookmarksServiceNormal.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsBookmarksServiceNormal.setStatus(
        ""
    )

upsHomePageServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 419)
)
upsHomePageServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsHomePageServiceUp.setStatus(
        ""
    )

upsUPWebServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 420)
)
upsUPWebServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceUp.setStatus(
        ""
    )

upsUPWebServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 421)
)
upsUPWebServiceNormal.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPWebServiceNormal.setStatus(
        ""
    )

upsUPAdminServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 422)
)
upsUPAdminServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPAdminServiceUp.setStatus(
        ""
    )

upsUPMailServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 423)
)
upsUPMailServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceUp.setStatus(
        ""
    )

upsUPMailServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 424)
)
upsUPMailServiceNormal.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPMailServiceNormal.setStatus(
        ""
    )

upsUPPimServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 425)
)
upsUPPimServiceUp.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceUp.setStatus(
        ""
    )

upsUPPimServiceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 3, 0, 426)
)
upsUPPimServiceNormal.setObjects(
    ("OPENWAVE-MIB", "upsTrapInfo")
)
if mibBuilder.loadTexts:
    upsUPPimServiceNormal.setStatus(
        ""
    )

uppStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1000)
)
uppStartup.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppStartup.setStatus(
        ""
    )

uppShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1001)
)
uppShutDown.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppShutDown.setStatus(
        ""
    )

uppFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1002)
)
uppFailToStart.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppFailToStart.setStatus(
        ""
    )

uppDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1003)
)
uppDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppDatabaseConnectionDown.setStatus(
        ""
    )

uppInternalErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1006)
)
uppInternalErrors.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppInternalErrors.setStatus(
        ""
    )

uppPublicHTTPServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1007)
)
uppPublicHTTPServiceStarted.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPublicHTTPServiceStarted.setStatus(
        ""
    )

uppPublicHTTPServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1008)
)
uppPublicHTTPServiceDown.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPublicHTTPServiceDown.setStatus(
        ""
    )

uppPrivateHTTPServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1009)
)
uppPrivateHTTPServiceDown.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPrivateHTTPServiceDown.setStatus(
        ""
    )

uppPublicHTTPSServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1010)
)
uppPublicHTTPSServiceDown.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPublicHTTPSServiceDown.setStatus(
        ""
    )

uppPPGInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1011)
)
uppPPGInterfaceDown.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPPGInterfaceDown.setStatus(
        ""
    )

uppPPGInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1012)
)
uppPPGInterfaceUp.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPPGInterfaceUp.setStatus(
        ""
    )

uppPAPSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1013)
)
uppPAPSuspended.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPAPSuspended.setStatus(
        ""
    )

uppPAPResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1014)
)
uppPAPResumed.setObjects(
      *(("OPENWAVE-MIB", "uppdPAPIdentifier"),
        ("OPENWAVE-MIB", "uppdHostName"),
        ("OPENWAVE-MIB", "uppdProcessId"),
        ("OPENWAVE-MIB", "uppTrapInfo"))
)
if mibBuilder.loadTexts:
    uppPAPResumed.setStatus(
        ""
    )

uppgStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1100)
)
uppgStartup.setObjects(
      *(("OPENWAVE-MIB", "uppgdPPGIdentifier"),
        ("OPENWAVE-MIB", "uppgdHostName"),
        ("OPENWAVE-MIB", "uppgdProcessId"),
        ("OPENWAVE-MIB", "uppgTrapInfo"))
)
if mibBuilder.loadTexts:
    uppgStartup.setStatus(
        ""
    )

upgFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1101)
)
upgFailToStart.setObjects(
      *(("OPENWAVE-MIB", "uppgdPPGIdentifier"),
        ("OPENWAVE-MIB", "uppgdHostName"),
        ("OPENWAVE-MIB", "uppgdProcessId"),
        ("OPENWAVE-MIB", "uppgTrapInfo"))
)
if mibBuilder.loadTexts:
    upgFailToStart.setStatus(
        ""
    )

uppgDatabaseConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1102)
)
uppgDatabaseConnectionDown.setObjects(
      *(("OPENWAVE-MIB", "uppgdPPGIdentifier"),
        ("OPENWAVE-MIB", "uppgdHostName"),
        ("OPENWAVE-MIB", "uppgdProcessId"),
        ("OPENWAVE-MIB", "uppgTrapInfo"))
)
if mibBuilder.loadTexts:
    uppgDatabaseConnectionDown.setStatus(
        ""
    )

uppgInternalErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 1900, 4, 5, 0, 1105)
)
uppgInternalErrors.setObjects(
      *(("OPENWAVE-MIB", "uppgdPPGIdentifier"),
        ("OPENWAVE-MIB", "uppgdHostName"),
        ("OPENWAVE-MIB", "uppgdProcessId"),
        ("OPENWAVE-MIB", "uppgTrapInfo"))
)
if mibBuilder.loadTexts:
    uppgInternalErrors.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENWAVE-MIB",
    **{"DisplayString": DisplayString,
       "openwave": openwave,
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
       "upldUplRadiusConnectionDown": upldUplRadiusConnectionDown,
       "uplaStartup": uplaStartup,
       "uplaShutdown": uplaShutdown,
       "uplaDatabaseConnectionDown": uplaDatabaseConnectionDown,
       "uplaFaxMgrConnectionDown": uplaFaxMgrConnectionDown,
       "uplaMessengerConnectionDown": uplaMessengerConnectionDown,
       "uplaInvalidConfig": uplaInvalidConfig,
       "uplaInternalFatalErrors": uplaInternalFatalErrors,
       "uplaOutOfResource": uplaOutOfResource,
       "uplaDatabaseConnectionUp": uplaDatabaseConnectionUp,
       "uplaBillingInitError": uplaBillingInitError,
       "uplaBillingLogError": uplaBillingLogError,
       "uplaDynamicUpdateStarted": uplaDynamicUpdateStarted,
       "uplaDynamicUpdateStopped": uplaDynamicUpdateStopped,
       "uplrStartup": uplrStartup,
       "uplrShutdown": uplrShutdown,
       "uplrDatabaseConnectionDown": uplrDatabaseConnectionDown,
       "uplrDatabaseConnectionUp": uplrDatabaseConnectionUp,
       "uplrInternalError": uplrInternalError,
       "uplrSMSCConnectionDown": uplrSMSCConnectionDown,
       "uplrSMSCConnectionUp": uplrSMSCConnectionUp,
       "uplrClientConnectionDown": uplrClientConnectionDown,
       "uplrClientConnectionUp": uplrClientConnectionUp,
       "uplrNbRouterConnectionDown": uplrNbRouterConnectionDown,
       "uplrNbRouterConnectionUp": uplrNbRouterConnectionUp,
       "uplrProtocolError": uplrProtocolError,
       "uplrBillingInitError": uplrBillingInitError,
       "uplrBillingLogError": uplrBillingLogError,
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
       "uplwCLIDMappingError": uplwCLIDMappingError,
       "uplbStartup": uplbStartup,
       "uplbShutdown": uplbShutdown,
       "uplbDatabaseConnectionDown": uplbDatabaseConnectionDown,
       "uplbBillingLogFileError": uplbBillingLogFileError,
       "uplbBillingDirectTransferError": uplbBillingDirectTransferError,
       "uplbDiskSpaceError": uplbDiskSpaceError,
       "uplbDiskSpaceLow": uplbDiskSpaceLow,
       "uplbDiskSpaceCriticallyLow": uplbDiskSpaceCriticallyLow,
       "uplrsStartup": uplrsStartup,
       "uplrsFailedToStart": uplrsFailedToStart,
       "uplrsDatabaseConnectionDown": uplrsDatabaseConnectionDown,
       "uplrsBillingInitError": uplrsBillingInitError,
       "uplrsBillingLogError": uplrsBillingLogError,
       "uplcrStartup": uplcrStartup,
       "uplcrFatalError": uplcrFatalError,
       "uplcrCertificateUpdateFailed": uplcrCertificateUpdateFailed,
       "uplcrInvalidCertResponse": uplcrInvalidCertResponse,
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
       "uplDispRadiusClientStats": uplDispRadiusClientStats,
       "upldTotalMappingTableHits": upldTotalMappingTableHits,
       "upldSuccessfulMappingHits": upldSuccessfulMappingHits,
       "upldFailedMappingHits": upldFailedMappingHits,
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
       "uplAgentStackServiceTableSize": uplAgentStackServiceTableSize,
       "uplAgentStackServiceMeanTableItems": uplAgentStackServiceMeanTableItems,
       "uplAgentStackServiceMeanTableItemsDeviation": uplAgentStackServiceMeanTableItemsDeviation,
       "uplAgentStackServiceMeanBucketChainLength": uplAgentStackServiceMeanBucketChainLength,
       "uplAgentStackServiceMeanBucketChainLengthDeviation": uplAgentStackServiceMeanBucketChainLengthDeviation,
       "uplAgentStackServiceTableMeanNumberItemsGarbageCollected": uplAgentStackServiceTableMeanNumberItemsGarbageCollected,
       "uplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn": uplAgentStackServiceTableMeanNumberItemsGarbageCollectedDeviatn,
       "uplAgentStackServiceMeanGarbageCollectTime": uplAgentStackServiceMeanGarbageCollectTime,
       "uplAgentStackServiceMeanGarbageCollectTimeDeviation": uplAgentStackServiceMeanGarbageCollectTimeDeviation,
       "uplaRadiusClientStats": uplaRadiusClientStats,
       "uplAgentRadiusClientStatsTable": uplAgentRadiusClientStatsTable,
       "uplAgentRadiusClientStatsEntry": uplAgentRadiusClientStatsEntry,
       "uplarcsAgentIdentifier": uplarcsAgentIdentifier,
       "uplaTotalMappingTableHits": uplaTotalMappingTableHits,
       "uplaSuccessfulMappingHits": uplaSuccessfulMappingHits,
       "uplaFailedMappingHits": uplaFailedMappingHits,
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
       "uplNbRouterAirlinkStatsTable": uplNbRouterAirlinkStatsTable,
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
       "uplmDBMaxConnections": uplmDBMaxConnections,
       "uplmDBMinConnections": uplmDBMinConnections,
       "uplmDBConnectionCacheThreadWaits": uplmDBConnectionCacheThreadWaits,
       "uplmDBConnectionCacheMeanWaitTime": uplmDBConnectionCacheMeanWaitTime,
       "uplmDBConnectionCacheDeviationOfWaitTime": uplmDBConnectionCacheDeviationOfWaitTime,
       "uplmdMaxMsgClientStreams": uplmdMaxMsgClientStreams,
       "uplmdOpenAgentStreams": uplmdOpenAgentStreams,
       "uplmdNumTxnProcessed": uplmdNumTxnProcessed,
       "uplmHdtpStats": uplmHdtpStats,
       "uplMessengerAirlinkTable": uplMessengerAirlinkTable,
       "uplMessengerAirlinkStatsTable": uplMessengerAirlinkStatsTable,
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
       "uplmnsNumAddRequests": uplmnsNumAddRequests,
       "uplmnsNumStatusRequests": uplmnsNumStatusRequests,
       "uplmnsNumDeleteRequests": uplmnsNumDeleteRequests,
       "uplmnsNumAdded": uplmnsNumAdded,
       "uplmnsNumStatusFound": uplmnsNumStatusFound,
       "uplmnsNumDeleted": uplmnsNumDeleted,
       "uplmnsNumExpired": uplmnsNumExpired,
       "uplmnsCompletedNotifications": uplmnsCompletedNotifications,
       "uplmnsSignalsSent": uplmnsSignalsSent,
       "uplMessengerNtfnCacheTable": uplMessengerNtfnCacheTable,
       "uplMessengerNtfnCacheEntry": uplMessengerNtfnCacheEntry,
       "uplmncIpAddress": uplmncIpAddress,
       "uplmncProcessId": uplmncProcessId,
       "uplmncTotalNumOfPendingNtfns": uplmncTotalNumOfPendingNtfns,
       "uplmncAvgNumOfPendingNtfnsPerSub": uplmncAvgNumOfPendingNtfnsPerSub,
       "uplMessengerHTTPStatsTable": uplMessengerHTTPStatsTable,
       "uplMessengerHTTPStatsEntry": uplMessengerHTTPStatsEntry,
       "uplmhIpAddress": uplmhIpAddress,
       "uplmhProcessId": uplmhProcessId,
       "uplmhPublicHTTPMaxConnections": uplmhPublicHTTPMaxConnections,
       "uplmhPublicHTTPOpenConnections": uplmhPublicHTTPOpenConnections,
       "uplmhPublicHTTPMaxThreads": uplmhPublicHTTPMaxThreads,
       "uplmhPublicHTTPBusyThreads": uplmhPublicHTTPBusyThreads,
       "uplmhPublicHTTPTimesAllThreadsBusy": uplmhPublicHTTPTimesAllThreadsBusy,
       "uplmhPublicHTTPMaxDispQueueLength": uplmhPublicHTTPMaxDispQueueLength,
       "uplmhPublicHTTPCurrentDispQueueLen": uplmhPublicHTTPCurrentDispQueueLen,
       "uplmhPublicHTTPTimesDispQueueFull": uplmhPublicHTTPTimesDispQueueFull,
       "uplmhPrivateHTTPMaxConnections": uplmhPrivateHTTPMaxConnections,
       "uplmhPrivateHTTPOpenConnections": uplmhPrivateHTTPOpenConnections,
       "uplmhPrivateHTTPMaxThreads": uplmhPrivateHTTPMaxThreads,
       "uplmhPrivateHTTPBusyThreads": uplmhPrivateHTTPBusyThreads,
       "uplmhPrivateHTTPTimesAllThreadsBusy": uplmhPrivateHTTPTimesAllThreadsBusy,
       "uplmhPrivateHTTPMaxDispQueueLength": uplmhPrivateHTTPMaxDispQueueLength,
       "uplmhPrivateHTTPCurrentDispQueueLen": uplmhPrivateHTTPCurrentDispQueueLen,
       "uplmhPrivateHTTPTimesDispQueueFull": uplmhPrivateHTTPTimesDispQueueFull,
       "uplmhPublicHTTPSMaxConnections": uplmhPublicHTTPSMaxConnections,
       "uplmhPublicHTTPSOpenConnections": uplmhPublicHTTPSOpenConnections,
       "uplmhPublicHTTPSMaxThreads": uplmhPublicHTTPSMaxThreads,
       "uplmhPublicHTTPSBusyThreads": uplmhPublicHTTPSBusyThreads,
       "uplmhPublicHTTPSTimesAllThreadsBusy": uplmhPublicHTTPSTimesAllThreadsBusy,
       "uplmhPublicHTTPSMaxDispQueueLength": uplmhPublicHTTPSMaxDispQueueLength,
       "uplmhPublicHTTPSCurrentDispQueueLen": uplmhPublicHTTPSCurrentDispQueueLen,
       "uplmhPublicHTTPSTimesDispQueueFull": uplmhPublicHTTPSTimesDispQueueFull,
       "uplMessengerTrapInfo": uplMessengerTrapInfo,
       "uplmTrapInfo": uplmTrapInfo,
       "uplWap": uplWap,
       "uplWapTrapInfo": uplWapTrapInfo,
       "uplwTrapInfo": uplwTrapInfo,
       "uplwHostName": uplwHostName,
       "uplwProcessId": uplwProcessId,
       "uplBillingMgr": uplBillingMgr,
       "uplBillingMgrDescriptionTable": uplBillingMgrDescriptionTable,
       "uplBillingMgrDescriptionEntry": uplBillingMgrDescriptionEntry,
       "uplbdIpAddress": uplbdIpAddress,
       "uplbdProcessId": uplbdProcessId,
       "uplbdHostName": uplbdHostName,
       "uplbdPortNumber": uplbdPortNumber,
       "uplbdStartupTime": uplbdStartupTime,
       "uplBillingMgrEventStatsTable": uplBillingMgrEventStatsTable,
       "uplBillingMgrEventStatsEntry": uplBillingMgrEventStatsEntry,
       "uplbesIpAddress": uplbesIpAddress,
       "uplbesProcessId": uplbesProcessId,
       "uplbesEventsReceived": uplbesEventsReceived,
       "uplbesEventLogFailures": uplbesEventLogFailures,
       "uplbesDirectTransferFailures": uplbesDirectTransferFailures,
       "uplBillingMgrFileStatsTable": uplBillingMgrFileStatsTable,
       "uplBillingMgrFileStatsEntry": uplBillingMgrFileStatsEntry,
       "uplbfsIpAddress": uplbfsIpAddress,
       "uplbfsProcessId": uplbfsProcessId,
       "uplbfsMaxBillingFileSize": uplbfsMaxBillingFileSize,
       "uplbfsCompressorName": uplbfsCompressorName,
       "uplbfsBillingFilePath": uplbfsBillingFilePath,
       "uplbfsArchiveFilePath": uplbfsArchiveFilePath,
       "uplbfsFileDiskSpaceUsed": uplbfsFileDiskSpaceUsed,
       "uplbfsArchiveDiskSpaceUsed": uplbfsArchiveDiskSpaceUsed,
       "uplBillingMgrTrapInfo": uplBillingMgrTrapInfo,
       "uplbTrapInfo": uplbTrapInfo,
       "uplRadiusServer": uplRadiusServer,
       "uplRadiusServerDescriptionTable": uplRadiusServerDescriptionTable,
       "uplRadiusServerDescriptionEntry": uplRadiusServerDescriptionEntry,
       "uplrsdIpAddress": uplrsdIpAddress,
       "uplrsdProcessId": uplrsdProcessId,
       "uplrsdHostName": uplrsdHostName,
       "uplrsdPortNumber": uplrsdPortNumber,
       "uplrsdStartupTime": uplrsdStartupTime,
       "uplRadiusServerStatsTable": uplRadiusServerStatsTable,
       "uplRadiusServerStatsEntry": uplRadiusServerStatsEntry,
       "uplrssIpAddress": uplrssIpAddress,
       "uplrssProcessId": uplrssProcessId,
       "uplrssRasServiceAddress": uplrssRasServiceAddress,
       "uplrssAuthenticationStatus": uplrssAuthenticationStatus,
       "uplrssStartAccMsgReceived": uplrssStartAccMsgReceived,
       "uplrssInterimAccMsgReceived": uplrssInterimAccMsgReceived,
       "uplrssStopAccMsgReceived": uplrssStopAccMsgReceived,
       "uplrssIpMsisdnPairsInserted": uplrssIpMsisdnPairsInserted,
       "uplrssIpMsisdnPairsUpdated": uplrssIpMsisdnPairsUpdated,
       "uplrssIpMsisdnPairsDeleted": uplrssIpMsisdnPairsDeleted,
       "uplRadiusServerTrapInfo": uplRadiusServerTrapInfo,
       "uplrsTrapInfo": uplrsTrapInfo,
       "uplCertRequester": uplCertRequester,
       "uplCertRequesterDescriptionTable": uplCertRequesterDescriptionTable,
       "uplCertRequesterDescriptionEntry": uplCertRequesterDescriptionEntry,
       "uplcrdIpAddress": uplcrdIpAddress,
       "uplcrdProcessId": uplcrdProcessId,
       "uplcrdHostName": uplcrdHostName,
       "uplcrdUpdateInterval": uplcrdUpdateInterval,
       "uplcrdRequestAllowance": uplcrdRequestAllowance,
       "uplcrdStartupTime": uplcrdStartupTime,
       "uplCertRequesterTrapInfo": uplCertRequesterTrapInfo,
       "uplcrTrapInfo": uplcrTrapInfo,
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
       "upPushProxy": upPushProxy,
       "uppStartup": uppStartup,
       "uppShutDown": uppShutDown,
       "uppFailToStart": uppFailToStart,
       "uppDatabaseConnectionDown": uppDatabaseConnectionDown,
       "uppInternalErrors": uppInternalErrors,
       "uppPublicHTTPServiceStarted": uppPublicHTTPServiceStarted,
       "uppPublicHTTPServiceDown": uppPublicHTTPServiceDown,
       "uppPrivateHTTPServiceDown": uppPrivateHTTPServiceDown,
       "uppPublicHTTPSServiceDown": uppPublicHTTPSServiceDown,
       "uppPPGInterfaceDown": uppPPGInterfaceDown,
       "uppPPGInterfaceUp": uppPPGInterfaceUp,
       "uppPAPSuspended": uppPAPSuspended,
       "uppPAPResumed": uppPAPResumed,
       "uppgStartup": uppgStartup,
       "upgFailToStart": upgFailToStart,
       "uppgDatabaseConnectionDown": uppgDatabaseConnectionDown,
       "uppgInternalErrors": uppgInternalErrors,
       "upPushPap": upPushPap,
       "upPushPapDescriptionTable": upPushPapDescriptionTable,
       "upPushPapDescriptionEntry": upPushPapDescriptionEntry,
       "uppdPAPIndex": uppdPAPIndex,
       "uppdPAPIdentifier": uppdPAPIdentifier,
       "uppdProcessId": uppdProcessId,
       "uppdHostName": uppdHostName,
       "uppdPublicHTTPPortNumber": uppdPublicHTTPPortNumber,
       "uppdPublicHTTPSPortNumber": uppdPublicHTTPSPortNumber,
       "uppdPrivateHTTPPortNumber": uppdPrivateHTTPPortNumber,
       "uppdStartupTime": uppdStartupTime,
       "upPushPapNtfnStatsTable": upPushPapNtfnStatsTable,
       "upPushPapNtfnStatsEntry": upPushPapNtfnStatsEntry,
       "uppnsPAPIndex": uppnsPAPIndex,
       "uppnsPAPIdentifier": uppnsPAPIdentifier,
       "uppnsPublicHTTPReqReceived": uppnsPublicHTTPReqReceived,
       "uppnsPrivateHTTPReqReceived": uppnsPrivateHTTPReqReceived,
       "uppnsPublicHTTPSReqReceived": uppnsPublicHTTPSReqReceived,
       "uppnsPublicHTTPReqAccepted": uppnsPublicHTTPReqAccepted,
       "uppnsPrivateHTTPReqAccepted": uppnsPrivateHTTPReqAccepted,
       "uppnsPublicHTTPSReqAccepted": uppnsPublicHTTPSReqAccepted,
       "uppnsAvgNtfnsReceivedPerSec": uppnsAvgNtfnsReceivedPerSec,
       "uppnsAvgNtfnsAcceptedPerSec": uppnsAvgNtfnsAcceptedPerSec,
       "upPushPapForwardedNtfnsTable": upPushPapForwardedNtfnsTable,
       "upPushPapForwardedNtfnsEntry": upPushPapForwardedNtfnsEntry,
       "uppfnPAPIndex": uppfnPAPIndex,
       "uppfnPAPIdentifier": uppfnPAPIdentifier,
       "uppfnPPGForwardedNtfns": uppfnPPGForwardedNtfns,
       "uppfnPPGFailedNtfns": uppfnPPGFailedNtfns,
       "uppfnMessengerForwardedNtfns": uppfnMessengerForwardedNtfns,
       "uppfnMessengerFailedNtfns": uppfnMessengerFailedNtfns,
       "upPushPapTrapInfo": upPushPapTrapInfo,
       "uppTrapInfo": uppTrapInfo,
       "upPushPpg": upPushPpg,
       "upPushPpgDescriptionTable": upPushPpgDescriptionTable,
       "upPushPpgDescriptionEntry": upPushPpgDescriptionEntry,
       "uppgdPPGIndex": uppgdPPGIndex,
       "uppgdPPGIdentifier": uppgdPPGIdentifier,
       "uppgdProcessId": uppgdProcessId,
       "uppgdHostName": uppgdHostName,
       "uppgdMsgServerPortNumber": uppgdMsgServerPortNumber,
       "uppgdStartupTime": uppgdStartupTime,
       "upPushPpgNtfnStatsTable": upPushPpgNtfnStatsTable,
       "upPushPpgNtfnStatsEntry": upPushPpgNtfnStatsEntry,
       "uppgnsPPGIndex": uppgnsPPGIndex,
       "uppgnsPPGIdentifier": uppgnsPPGIdentifier,
       "uppgnsTotalNumOfPendingNtfns": uppgnsTotalNumOfPendingNtfns,
       "uppgnsAvgNtfnsDeliveredPerSec": uppgnsAvgNtfnsDeliveredPerSec,
       "uppgnsAvgNtfnsMarkedUnDelvrPerSec": uppgnsAvgNtfnsMarkedUnDelvrPerSec,
       "upPushPpgTrapInfo": upPushPpgTrapInfo,
       "uppgTrapInfo": uppgTrapInfo,
       "services": services,
       "upMail": upMail}
)
