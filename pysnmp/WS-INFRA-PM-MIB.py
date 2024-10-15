# SNMP MIB module (WS-INFRA-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:28 2024
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
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wsInfraPM,) = mibBuilder.importSymbols(
    "WS-INFRA-SMI-MIB",
    "wsInfraPM")

(DoActionNow,) = mibBuilder.importSymbols(
    "WS-TYPE-MIB",
    "DoActionNow")


# MODULE-IDENTITY

wsInfraProcessMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1)
)
wsInfraProcessMonitor.setRevisions(
        ("2006-05-24 15:32",
         "2006-05-12 14:26",
         "2005-10-27 18:30",
         "2005-09-02 16:22",
         "2005-05-19 15:36",
         "2005-05-18 17:11")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraProcMonSystemRestart_Type = TruthValue
_WsInfraProcMonSystemRestart_Object = MibScalar
wsInfraProcMonSystemRestart = _WsInfraProcMonSystemRestart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 1),
    _WsInfraProcMonSystemRestart_Type()
)
wsInfraProcMonSystemRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraProcMonSystemRestart.setStatus("current")


class _WsInfraProcMonMaxSystemRestarts_Type(Unsigned32):
    """Custom type wsInfraProcMonMaxSystemRestarts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WsInfraProcMonMaxSystemRestarts_Type.__name__ = "Unsigned32"
_WsInfraProcMonMaxSystemRestarts_Object = MibScalar
wsInfraProcMonMaxSystemRestarts = _WsInfraProcMonMaxSystemRestarts_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 2),
    _WsInfraProcMonMaxSystemRestarts_Type()
)
wsInfraProcMonMaxSystemRestarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraProcMonMaxSystemRestarts.setStatus("current")
_WsInfraProcMonSystemRestartCnt_Type = Integer32
_WsInfraProcMonSystemRestartCnt_Object = MibScalar
wsInfraProcMonSystemRestartCnt = _WsInfraProcMonSystemRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 3),
    _WsInfraProcMonSystemRestartCnt_Type()
)
wsInfraProcMonSystemRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonSystemRestartCnt.setStatus("current")
_WsInfraProcMonSystemRestartCntClear_Type = DoActionNow
_WsInfraProcMonSystemRestartCntClear_Object = MibScalar
wsInfraProcMonSystemRestartCntClear = _WsInfraProcMonSystemRestartCntClear_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 4),
    _WsInfraProcMonSystemRestartCntClear_Type()
)
wsInfraProcMonSystemRestartCntClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraProcMonSystemRestartCntClear.setStatus("current")
_WsInfraProcMonProcessTable_Object = MibTable
wsInfraProcMonProcessTable = _WsInfraProcMonProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    wsInfraProcMonProcessTable.setStatus("current")
_WsInfraProcMonProcessEntry_Object = MibTableRow
wsInfraProcMonProcessEntry = _WsInfraProcMonProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1)
)
wsInfraProcMonProcessEntry.setIndexNames(
    (0, "WS-INFRA-PM-MIB", "wsInfraProcMonProcessIndex"),
)
if mibBuilder.loadTexts:
    wsInfraProcMonProcessEntry.setStatus("current")


class _WsInfraProcMonProcessIndex_Type(Integer32):
    """Custom type wsInfraProcMonProcessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsInfraProcMonProcessIndex_Type.__name__ = "Integer32"
_WsInfraProcMonProcessIndex_Object = MibTableColumn
wsInfraProcMonProcessIndex = _WsInfraProcMonProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1, 1),
    _WsInfraProcMonProcessIndex_Type()
)
wsInfraProcMonProcessIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraProcMonProcessIndex.setStatus("current")


class _WsInfraProcMonProcessName_Type(DisplayString):
    """Custom type wsInfraProcMonProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WsInfraProcMonProcessName_Type.__name__ = "DisplayString"
_WsInfraProcMonProcessName_Object = MibTableColumn
wsInfraProcMonProcessName = _WsInfraProcMonProcessName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1, 2),
    _WsInfraProcMonProcessName_Type()
)
wsInfraProcMonProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonProcessName.setStatus("current")
_WsInfraProcMonProcessPid_Type = Integer32
_WsInfraProcMonProcessPid_Object = MibTableColumn
wsInfraProcMonProcessPid = _WsInfraProcMonProcessPid_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1, 3),
    _WsInfraProcMonProcessPid_Type()
)
wsInfraProcMonProcessPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonProcessPid.setStatus("current")


class _WsInfraProcMonProcessMaxRestart_Type(Integer32):
    """Custom type wsInfraProcMonProcessMaxRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WsInfraProcMonProcessMaxRestart_Type.__name__ = "Integer32"
_WsInfraProcMonProcessMaxRestart_Object = MibTableColumn
wsInfraProcMonProcessMaxRestart = _WsInfraProcMonProcessMaxRestart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1, 4),
    _WsInfraProcMonProcessMaxRestart_Type()
)
wsInfraProcMonProcessMaxRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonProcessMaxRestart.setStatus("current")
_WsInfraProcMonProcessStartCount_Type = Integer32
_WsInfraProcMonProcessStartCount_Object = MibTableColumn
wsInfraProcMonProcessStartCount = _WsInfraProcMonProcessStartCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1, 5),
    _WsInfraProcMonProcessStartCount_Type()
)
wsInfraProcMonProcessStartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonProcessStartCount.setStatus("current")
_WsInfraProcMonProcessLastHeard_Type = DateAndTime
_WsInfraProcMonProcessLastHeard_Object = MibTableColumn
wsInfraProcMonProcessLastHeard = _WsInfraProcMonProcessLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1, 6),
    _WsInfraProcMonProcessLastHeard_Type()
)
wsInfraProcMonProcessLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonProcessLastHeard.setStatus("current")
_WsInfraProcMonProcessLastStarted_Type = DateAndTime
_WsInfraProcMonProcessLastStarted_Object = MibTableColumn
wsInfraProcMonProcessLastStarted = _WsInfraProcMonProcessLastStarted_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 5, 1, 7),
    _WsInfraProcMonProcessLastStarted_Type()
)
wsInfraProcMonProcessLastStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonProcessLastStarted.setStatus("current")
_WsInfraProcMonHistTable_Object = MibTable
wsInfraProcMonHistTable = _WsInfraProcMonHistTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    wsInfraProcMonHistTable.setStatus("current")
_WsInfraProcMonHistEntry_Object = MibTableRow
wsInfraProcMonHistEntry = _WsInfraProcMonHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 6, 1)
)
wsInfraProcMonHistEntry.setIndexNames(
    (0, "WS-INFRA-PM-MIB", "wsInfraProcMonProcessIndex"),
    (0, "WS-INFRA-PM-MIB", "wsInfraProcMonHistIndex"),
)
if mibBuilder.loadTexts:
    wsInfraProcMonHistEntry.setStatus("current")


class _WsInfraProcMonHistIndex_Type(Integer32):
    """Custom type wsInfraProcMonHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WsInfraProcMonHistIndex_Type.__name__ = "Integer32"
_WsInfraProcMonHistIndex_Object = MibTableColumn
wsInfraProcMonHistIndex = _WsInfraProcMonHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 6, 1, 1),
    _WsInfraProcMonHistIndex_Type()
)
wsInfraProcMonHistIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraProcMonHistIndex.setStatus("current")
_WsInfraProcMonHistTimestamp_Type = DateAndTime
_WsInfraProcMonHistTimestamp_Object = MibTableColumn
wsInfraProcMonHistTimestamp = _WsInfraProcMonHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 6, 1, 2),
    _WsInfraProcMonHistTimestamp_Type()
)
wsInfraProcMonHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonHistTimestamp.setStatus("current")


class _WsInfraProcMonHistEvent_Type(Integer32):
    """Custom type wsInfraProcMonHistEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("failed", 4),
          ("heartbeat", 5),
          ("init", 1),
          ("resumeMonitoring", 8),
          ("shutdown", 6),
          ("stopMonitoring", 7),
          ("up", 2))
    )


_WsInfraProcMonHistEvent_Type.__name__ = "Integer32"
_WsInfraProcMonHistEvent_Object = MibTableColumn
wsInfraProcMonHistEvent = _WsInfraProcMonHistEvent_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 6, 1, 3),
    _WsInfraProcMonHistEvent_Type()
)
wsInfraProcMonHistEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonHistEvent.setStatus("current")


class _WsInfraProcMonHistState_Type(Integer32):
    """Custom type wsInfraProcMonHistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("down", 6),
          ("kill", 5),
          ("notMonitoring", 8),
          ("notResponding", 4),
          ("notRunning", 3),
          ("resumeMonitoring", 9),
          ("running", 2),
          ("shutdown", 7),
          ("unknown", 1))
    )


_WsInfraProcMonHistState_Type.__name__ = "Integer32"
_WsInfraProcMonHistState_Object = MibTableColumn
wsInfraProcMonHistState = _WsInfraProcMonHistState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 6, 1, 4),
    _WsInfraProcMonHistState_Type()
)
wsInfraProcMonHistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraProcMonHistState.setStatus("current")
_WsInfraPMMIBConformance_ObjectIdentity = ObjectIdentity
wsInfraPMMIBConformance = _WsInfraPMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 100)
)
_WsInfraPMMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfraPMMIBCompliances = _WsInfraPMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 100, 1)
)
_WsInfraPMMIBGroups_ObjectIdentity = ObjectIdentity
wsInfraPMMIBGroups = _WsInfraPMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 100, 2)
)

# Managed Objects groups

wsInfraMIBProcMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 100, 2, 1)
)
wsInfraMIBProcMonGroup.setObjects(
      *(("WS-INFRA-PM-MIB", "wsInfraProcMonProcessStartCount"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonSystemRestartCntClear"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonSystemRestartCnt"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonProcessLastStarted"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonSystemRestart"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonMaxSystemRestarts"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonProcessIndex"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonProcessName"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonProcessPid"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonProcessMaxRestart"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonProcessLastHeard"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonHistIndex"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonHistTimestamp"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonHistEvent"),
        ("WS-INFRA-PM-MIB", "wsInfraProcMonHistState"))
)
if mibBuilder.loadTexts:
    wsInfraMIBProcMonGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfraPMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    wsInfraPMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-PM-MIB",
    **{"wsInfraProcessMonitor": wsInfraProcessMonitor,
       "wsInfraProcMonSystemRestart": wsInfraProcMonSystemRestart,
       "wsInfraProcMonMaxSystemRestarts": wsInfraProcMonMaxSystemRestarts,
       "wsInfraProcMonSystemRestartCnt": wsInfraProcMonSystemRestartCnt,
       "wsInfraProcMonSystemRestartCntClear": wsInfraProcMonSystemRestartCntClear,
       "wsInfraProcMonProcessTable": wsInfraProcMonProcessTable,
       "wsInfraProcMonProcessEntry": wsInfraProcMonProcessEntry,
       "wsInfraProcMonProcessIndex": wsInfraProcMonProcessIndex,
       "wsInfraProcMonProcessName": wsInfraProcMonProcessName,
       "wsInfraProcMonProcessPid": wsInfraProcMonProcessPid,
       "wsInfraProcMonProcessMaxRestart": wsInfraProcMonProcessMaxRestart,
       "wsInfraProcMonProcessStartCount": wsInfraProcMonProcessStartCount,
       "wsInfraProcMonProcessLastHeard": wsInfraProcMonProcessLastHeard,
       "wsInfraProcMonProcessLastStarted": wsInfraProcMonProcessLastStarted,
       "wsInfraProcMonHistTable": wsInfraProcMonHistTable,
       "wsInfraProcMonHistEntry": wsInfraProcMonHistEntry,
       "wsInfraProcMonHistIndex": wsInfraProcMonHistIndex,
       "wsInfraProcMonHistTimestamp": wsInfraProcMonHistTimestamp,
       "wsInfraProcMonHistEvent": wsInfraProcMonHistEvent,
       "wsInfraProcMonHistState": wsInfraProcMonHistState,
       "wsInfraPMMIBConformance": wsInfraPMMIBConformance,
       "wsInfraPMMIBCompliances": wsInfraPMMIBCompliances,
       "wsInfraPMMIBCompliance": wsInfraPMMIBCompliance,
       "wsInfraPMMIBGroups": wsInfraPMMIBGroups,
       "wsInfraMIBProcMonGroup": wsInfraMIBProcMonGroup}
)
