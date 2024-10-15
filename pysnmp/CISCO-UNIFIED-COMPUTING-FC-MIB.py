# SNMP MIB module (CISCO-UNIFIED-COMPUTING-FC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-FC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:30 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsConditionRemoteInvRslt,
 CucsEquipmentXcvrType,
 CucsFabricAdminState,
 CucsFcErrStatsHistThresholded,
 CucsFcErrStatsThresholded,
 CucsFcPIoFsmCurrentFsm,
 CucsFcPIoFsmStageName,
 CucsFcStatsHistThresholded,
 CucsFcStatsThresholded,
 CucsFsmFsmStageStatus,
 CucsFsmLifecycle,
 CucsLicenseState,
 CucsNetworkConnectionType,
 CucsNetworkLocale,
 CucsNetworkPhysEpIfType,
 CucsNetworkPortOperState,
 CucsNetworkPortRole,
 CucsNetworkSwitchId,
 CucsNetworkTransport,
 CucsPortEncap,
 CucsPortMode,
 CucsPortSpeed) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsEquipmentXcvrType",
    "CucsFabricAdminState",
    "CucsFcErrStatsHistThresholded",
    "CucsFcErrStatsThresholded",
    "CucsFcPIoFsmCurrentFsm",
    "CucsFcPIoFsmStageName",
    "CucsFcStatsHistThresholded",
    "CucsFcStatsThresholded",
    "CucsFsmFsmStageStatus",
    "CucsFsmLifecycle",
    "CucsLicenseState",
    "CucsNetworkConnectionType",
    "CucsNetworkLocale",
    "CucsNetworkPhysEpIfType",
    "CucsNetworkPortOperState",
    "CucsNetworkPortRole",
    "CucsNetworkSwitchId",
    "CucsNetworkTransport",
    "CucsPortEncap",
    "CucsPortMode",
    "CucsPortSpeed")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsFcObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFcErrStatsTable_Object = MibTable
cucsFcErrStatsTable = _CucsFcErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1)
)
if mibBuilder.loadTexts:
    cucsFcErrStatsTable.setStatus("current")
_CucsFcErrStatsEntry_Object = MibTableRow
cucsFcErrStatsEntry = _CucsFcErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1)
)
cucsFcErrStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcErrStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcErrStatsEntry.setStatus("current")
_CucsFcErrStatsInstanceId_Type = CucsManagedObjectId
_CucsFcErrStatsInstanceId_Object = MibTableColumn
cucsFcErrStatsInstanceId = _CucsFcErrStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 1),
    _CucsFcErrStatsInstanceId_Type()
)
cucsFcErrStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcErrStatsInstanceId.setStatus("current")
_CucsFcErrStatsDn_Type = CucsManagedObjectDn
_CucsFcErrStatsDn_Object = MibTableColumn
cucsFcErrStatsDn = _CucsFcErrStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 2),
    _CucsFcErrStatsDn_Type()
)
cucsFcErrStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDn.setStatus("current")
_CucsFcErrStatsRn_Type = SnmpAdminString
_CucsFcErrStatsRn_Object = MibTableColumn
cucsFcErrStatsRn = _CucsFcErrStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 3),
    _CucsFcErrStatsRn_Type()
)
cucsFcErrStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsRn.setStatus("current")
_CucsFcErrStatsCrcRx_Type = Unsigned64
_CucsFcErrStatsCrcRx_Object = MibTableColumn
cucsFcErrStatsCrcRx = _CucsFcErrStatsCrcRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 4),
    _CucsFcErrStatsCrcRx_Type()
)
cucsFcErrStatsCrcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsCrcRx.setStatus("current")
_CucsFcErrStatsCrcRxDelta_Type = Counter64
_CucsFcErrStatsCrcRxDelta_Object = MibTableColumn
cucsFcErrStatsCrcRxDelta = _CucsFcErrStatsCrcRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 5),
    _CucsFcErrStatsCrcRxDelta_Type()
)
cucsFcErrStatsCrcRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsCrcRxDelta.setStatus("current")
_CucsFcErrStatsCrcRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsCrcRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsCrcRxDeltaAvg = _CucsFcErrStatsCrcRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 6),
    _CucsFcErrStatsCrcRxDeltaAvg_Type()
)
cucsFcErrStatsCrcRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsCrcRxDeltaAvg.setStatus("current")
_CucsFcErrStatsCrcRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsCrcRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsCrcRxDeltaMax = _CucsFcErrStatsCrcRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 7),
    _CucsFcErrStatsCrcRxDeltaMax_Type()
)
cucsFcErrStatsCrcRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsCrcRxDeltaMax.setStatus("current")
_CucsFcErrStatsCrcRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsCrcRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsCrcRxDeltaMin = _CucsFcErrStatsCrcRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 8),
    _CucsFcErrStatsCrcRxDeltaMin_Type()
)
cucsFcErrStatsCrcRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsCrcRxDeltaMin.setStatus("current")
_CucsFcErrStatsDiscardRx_Type = Unsigned64
_CucsFcErrStatsDiscardRx_Object = MibTableColumn
cucsFcErrStatsDiscardRx = _CucsFcErrStatsDiscardRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 9),
    _CucsFcErrStatsDiscardRx_Type()
)
cucsFcErrStatsDiscardRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardRx.setStatus("current")
_CucsFcErrStatsDiscardRxDelta_Type = Counter64
_CucsFcErrStatsDiscardRxDelta_Object = MibTableColumn
cucsFcErrStatsDiscardRxDelta = _CucsFcErrStatsDiscardRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 10),
    _CucsFcErrStatsDiscardRxDelta_Type()
)
cucsFcErrStatsDiscardRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardRxDelta.setStatus("current")
_CucsFcErrStatsDiscardRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsDiscardRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsDiscardRxDeltaAvg = _CucsFcErrStatsDiscardRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 11),
    _CucsFcErrStatsDiscardRxDeltaAvg_Type()
)
cucsFcErrStatsDiscardRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardRxDeltaAvg.setStatus("current")
_CucsFcErrStatsDiscardRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsDiscardRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsDiscardRxDeltaMax = _CucsFcErrStatsDiscardRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 12),
    _CucsFcErrStatsDiscardRxDeltaMax_Type()
)
cucsFcErrStatsDiscardRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardRxDeltaMax.setStatus("current")
_CucsFcErrStatsDiscardRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsDiscardRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsDiscardRxDeltaMin = _CucsFcErrStatsDiscardRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 13),
    _CucsFcErrStatsDiscardRxDeltaMin_Type()
)
cucsFcErrStatsDiscardRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardRxDeltaMin.setStatus("current")
_CucsFcErrStatsDiscardTx_Type = Unsigned64
_CucsFcErrStatsDiscardTx_Object = MibTableColumn
cucsFcErrStatsDiscardTx = _CucsFcErrStatsDiscardTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 14),
    _CucsFcErrStatsDiscardTx_Type()
)
cucsFcErrStatsDiscardTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardTx.setStatus("current")
_CucsFcErrStatsDiscardTxDelta_Type = Counter64
_CucsFcErrStatsDiscardTxDelta_Object = MibTableColumn
cucsFcErrStatsDiscardTxDelta = _CucsFcErrStatsDiscardTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 15),
    _CucsFcErrStatsDiscardTxDelta_Type()
)
cucsFcErrStatsDiscardTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardTxDelta.setStatus("current")
_CucsFcErrStatsDiscardTxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsDiscardTxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsDiscardTxDeltaAvg = _CucsFcErrStatsDiscardTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 16),
    _CucsFcErrStatsDiscardTxDeltaAvg_Type()
)
cucsFcErrStatsDiscardTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardTxDeltaAvg.setStatus("current")
_CucsFcErrStatsDiscardTxDeltaMax_Type = Unsigned64
_CucsFcErrStatsDiscardTxDeltaMax_Object = MibTableColumn
cucsFcErrStatsDiscardTxDeltaMax = _CucsFcErrStatsDiscardTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 17),
    _CucsFcErrStatsDiscardTxDeltaMax_Type()
)
cucsFcErrStatsDiscardTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardTxDeltaMax.setStatus("current")
_CucsFcErrStatsDiscardTxDeltaMin_Type = Unsigned64
_CucsFcErrStatsDiscardTxDeltaMin_Object = MibTableColumn
cucsFcErrStatsDiscardTxDeltaMin = _CucsFcErrStatsDiscardTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 18),
    _CucsFcErrStatsDiscardTxDeltaMin_Type()
)
cucsFcErrStatsDiscardTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsDiscardTxDeltaMin.setStatus("current")
_CucsFcErrStatsIntervals_Type = Gauge32
_CucsFcErrStatsIntervals_Object = MibTableColumn
cucsFcErrStatsIntervals = _CucsFcErrStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 19),
    _CucsFcErrStatsIntervals_Type()
)
cucsFcErrStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsIntervals.setStatus("current")
_CucsFcErrStatsLinkFailures_Type = Unsigned64
_CucsFcErrStatsLinkFailures_Object = MibTableColumn
cucsFcErrStatsLinkFailures = _CucsFcErrStatsLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 20),
    _CucsFcErrStatsLinkFailures_Type()
)
cucsFcErrStatsLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsLinkFailures.setStatus("current")
_CucsFcErrStatsLinkFailuresDelta_Type = Counter64
_CucsFcErrStatsLinkFailuresDelta_Object = MibTableColumn
cucsFcErrStatsLinkFailuresDelta = _CucsFcErrStatsLinkFailuresDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 21),
    _CucsFcErrStatsLinkFailuresDelta_Type()
)
cucsFcErrStatsLinkFailuresDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsLinkFailuresDelta.setStatus("current")
_CucsFcErrStatsLinkFailuresDeltaAvg_Type = Unsigned64
_CucsFcErrStatsLinkFailuresDeltaAvg_Object = MibTableColumn
cucsFcErrStatsLinkFailuresDeltaAvg = _CucsFcErrStatsLinkFailuresDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 22),
    _CucsFcErrStatsLinkFailuresDeltaAvg_Type()
)
cucsFcErrStatsLinkFailuresDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsLinkFailuresDeltaAvg.setStatus("current")
_CucsFcErrStatsLinkFailuresDeltaMax_Type = Unsigned64
_CucsFcErrStatsLinkFailuresDeltaMax_Object = MibTableColumn
cucsFcErrStatsLinkFailuresDeltaMax = _CucsFcErrStatsLinkFailuresDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 23),
    _CucsFcErrStatsLinkFailuresDeltaMax_Type()
)
cucsFcErrStatsLinkFailuresDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsLinkFailuresDeltaMax.setStatus("current")
_CucsFcErrStatsLinkFailuresDeltaMin_Type = Unsigned64
_CucsFcErrStatsLinkFailuresDeltaMin_Object = MibTableColumn
cucsFcErrStatsLinkFailuresDeltaMin = _CucsFcErrStatsLinkFailuresDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 24),
    _CucsFcErrStatsLinkFailuresDeltaMin_Type()
)
cucsFcErrStatsLinkFailuresDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsLinkFailuresDeltaMin.setStatus("current")
_CucsFcErrStatsRx_Type = Unsigned64
_CucsFcErrStatsRx_Object = MibTableColumn
cucsFcErrStatsRx = _CucsFcErrStatsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 25),
    _CucsFcErrStatsRx_Type()
)
cucsFcErrStatsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsRx.setStatus("current")
_CucsFcErrStatsRxDelta_Type = Counter64
_CucsFcErrStatsRxDelta_Object = MibTableColumn
cucsFcErrStatsRxDelta = _CucsFcErrStatsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 26),
    _CucsFcErrStatsRxDelta_Type()
)
cucsFcErrStatsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsRxDelta.setStatus("current")
_CucsFcErrStatsRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsRxDeltaAvg = _CucsFcErrStatsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 27),
    _CucsFcErrStatsRxDeltaAvg_Type()
)
cucsFcErrStatsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsRxDeltaAvg.setStatus("current")
_CucsFcErrStatsRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsRxDeltaMax = _CucsFcErrStatsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 28),
    _CucsFcErrStatsRxDeltaMax_Type()
)
cucsFcErrStatsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsRxDeltaMax.setStatus("current")
_CucsFcErrStatsRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsRxDeltaMin = _CucsFcErrStatsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 29),
    _CucsFcErrStatsRxDeltaMin_Type()
)
cucsFcErrStatsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsRxDeltaMin.setStatus("current")
_CucsFcErrStatsSignalLosses_Type = Unsigned64
_CucsFcErrStatsSignalLosses_Object = MibTableColumn
cucsFcErrStatsSignalLosses = _CucsFcErrStatsSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 30),
    _CucsFcErrStatsSignalLosses_Type()
)
cucsFcErrStatsSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSignalLosses.setStatus("current")
_CucsFcErrStatsSignalLossesDelta_Type = Counter64
_CucsFcErrStatsSignalLossesDelta_Object = MibTableColumn
cucsFcErrStatsSignalLossesDelta = _CucsFcErrStatsSignalLossesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 31),
    _CucsFcErrStatsSignalLossesDelta_Type()
)
cucsFcErrStatsSignalLossesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSignalLossesDelta.setStatus("current")
_CucsFcErrStatsSignalLossesDeltaAvg_Type = Unsigned64
_CucsFcErrStatsSignalLossesDeltaAvg_Object = MibTableColumn
cucsFcErrStatsSignalLossesDeltaAvg = _CucsFcErrStatsSignalLossesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 32),
    _CucsFcErrStatsSignalLossesDeltaAvg_Type()
)
cucsFcErrStatsSignalLossesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSignalLossesDeltaAvg.setStatus("current")
_CucsFcErrStatsSignalLossesDeltaMax_Type = Unsigned64
_CucsFcErrStatsSignalLossesDeltaMax_Object = MibTableColumn
cucsFcErrStatsSignalLossesDeltaMax = _CucsFcErrStatsSignalLossesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 33),
    _CucsFcErrStatsSignalLossesDeltaMax_Type()
)
cucsFcErrStatsSignalLossesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSignalLossesDeltaMax.setStatus("current")
_CucsFcErrStatsSignalLossesDeltaMin_Type = Unsigned64
_CucsFcErrStatsSignalLossesDeltaMin_Object = MibTableColumn
cucsFcErrStatsSignalLossesDeltaMin = _CucsFcErrStatsSignalLossesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 34),
    _CucsFcErrStatsSignalLossesDeltaMin_Type()
)
cucsFcErrStatsSignalLossesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSignalLossesDeltaMin.setStatus("current")
_CucsFcErrStatsSuspect_Type = TruthValue
_CucsFcErrStatsSuspect_Object = MibTableColumn
cucsFcErrStatsSuspect = _CucsFcErrStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 35),
    _CucsFcErrStatsSuspect_Type()
)
cucsFcErrStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSuspect.setStatus("current")
_CucsFcErrStatsSyncLosses_Type = Unsigned64
_CucsFcErrStatsSyncLosses_Object = MibTableColumn
cucsFcErrStatsSyncLosses = _CucsFcErrStatsSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 36),
    _CucsFcErrStatsSyncLosses_Type()
)
cucsFcErrStatsSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSyncLosses.setStatus("current")
_CucsFcErrStatsSyncLossesDelta_Type = Counter64
_CucsFcErrStatsSyncLossesDelta_Object = MibTableColumn
cucsFcErrStatsSyncLossesDelta = _CucsFcErrStatsSyncLossesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 37),
    _CucsFcErrStatsSyncLossesDelta_Type()
)
cucsFcErrStatsSyncLossesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSyncLossesDelta.setStatus("current")
_CucsFcErrStatsSyncLossesDeltaAvg_Type = Unsigned64
_CucsFcErrStatsSyncLossesDeltaAvg_Object = MibTableColumn
cucsFcErrStatsSyncLossesDeltaAvg = _CucsFcErrStatsSyncLossesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 38),
    _CucsFcErrStatsSyncLossesDeltaAvg_Type()
)
cucsFcErrStatsSyncLossesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSyncLossesDeltaAvg.setStatus("current")
_CucsFcErrStatsSyncLossesDeltaMax_Type = Unsigned64
_CucsFcErrStatsSyncLossesDeltaMax_Object = MibTableColumn
cucsFcErrStatsSyncLossesDeltaMax = _CucsFcErrStatsSyncLossesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 39),
    _CucsFcErrStatsSyncLossesDeltaMax_Type()
)
cucsFcErrStatsSyncLossesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSyncLossesDeltaMax.setStatus("current")
_CucsFcErrStatsSyncLossesDeltaMin_Type = Unsigned64
_CucsFcErrStatsSyncLossesDeltaMin_Object = MibTableColumn
cucsFcErrStatsSyncLossesDeltaMin = _CucsFcErrStatsSyncLossesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 40),
    _CucsFcErrStatsSyncLossesDeltaMin_Type()
)
cucsFcErrStatsSyncLossesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsSyncLossesDeltaMin.setStatus("current")
_CucsFcErrStatsThresholded_Type = CucsFcErrStatsThresholded
_CucsFcErrStatsThresholded_Object = MibTableColumn
cucsFcErrStatsThresholded = _CucsFcErrStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 41),
    _CucsFcErrStatsThresholded_Type()
)
cucsFcErrStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsThresholded.setStatus("current")
_CucsFcErrStatsTimeCollected_Type = DateAndTime
_CucsFcErrStatsTimeCollected_Object = MibTableColumn
cucsFcErrStatsTimeCollected = _CucsFcErrStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 42),
    _CucsFcErrStatsTimeCollected_Type()
)
cucsFcErrStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTimeCollected.setStatus("current")
_CucsFcErrStatsTooLongRx_Type = Unsigned64
_CucsFcErrStatsTooLongRx_Object = MibTableColumn
cucsFcErrStatsTooLongRx = _CucsFcErrStatsTooLongRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 43),
    _CucsFcErrStatsTooLongRx_Type()
)
cucsFcErrStatsTooLongRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooLongRx.setStatus("current")
_CucsFcErrStatsTooLongRxDelta_Type = Counter64
_CucsFcErrStatsTooLongRxDelta_Object = MibTableColumn
cucsFcErrStatsTooLongRxDelta = _CucsFcErrStatsTooLongRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 44),
    _CucsFcErrStatsTooLongRxDelta_Type()
)
cucsFcErrStatsTooLongRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooLongRxDelta.setStatus("current")
_CucsFcErrStatsTooLongRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsTooLongRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsTooLongRxDeltaAvg = _CucsFcErrStatsTooLongRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 45),
    _CucsFcErrStatsTooLongRxDeltaAvg_Type()
)
cucsFcErrStatsTooLongRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooLongRxDeltaAvg.setStatus("current")
_CucsFcErrStatsTooLongRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsTooLongRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsTooLongRxDeltaMax = _CucsFcErrStatsTooLongRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 46),
    _CucsFcErrStatsTooLongRxDeltaMax_Type()
)
cucsFcErrStatsTooLongRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooLongRxDeltaMax.setStatus("current")
_CucsFcErrStatsTooLongRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsTooLongRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsTooLongRxDeltaMin = _CucsFcErrStatsTooLongRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 47),
    _CucsFcErrStatsTooLongRxDeltaMin_Type()
)
cucsFcErrStatsTooLongRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooLongRxDeltaMin.setStatus("current")
_CucsFcErrStatsTooShortRx_Type = Unsigned64
_CucsFcErrStatsTooShortRx_Object = MibTableColumn
cucsFcErrStatsTooShortRx = _CucsFcErrStatsTooShortRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 48),
    _CucsFcErrStatsTooShortRx_Type()
)
cucsFcErrStatsTooShortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooShortRx.setStatus("current")
_CucsFcErrStatsTooShortRxDelta_Type = Counter64
_CucsFcErrStatsTooShortRxDelta_Object = MibTableColumn
cucsFcErrStatsTooShortRxDelta = _CucsFcErrStatsTooShortRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 49),
    _CucsFcErrStatsTooShortRxDelta_Type()
)
cucsFcErrStatsTooShortRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooShortRxDelta.setStatus("current")
_CucsFcErrStatsTooShortRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsTooShortRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsTooShortRxDeltaAvg = _CucsFcErrStatsTooShortRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 50),
    _CucsFcErrStatsTooShortRxDeltaAvg_Type()
)
cucsFcErrStatsTooShortRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooShortRxDeltaAvg.setStatus("current")
_CucsFcErrStatsTooShortRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsTooShortRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsTooShortRxDeltaMax = _CucsFcErrStatsTooShortRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 51),
    _CucsFcErrStatsTooShortRxDeltaMax_Type()
)
cucsFcErrStatsTooShortRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooShortRxDeltaMax.setStatus("current")
_CucsFcErrStatsTooShortRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsTooShortRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsTooShortRxDeltaMin = _CucsFcErrStatsTooShortRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 52),
    _CucsFcErrStatsTooShortRxDeltaMin_Type()
)
cucsFcErrStatsTooShortRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTooShortRxDeltaMin.setStatus("current")
_CucsFcErrStatsTx_Type = Unsigned64
_CucsFcErrStatsTx_Object = MibTableColumn
cucsFcErrStatsTx = _CucsFcErrStatsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 53),
    _CucsFcErrStatsTx_Type()
)
cucsFcErrStatsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTx.setStatus("current")
_CucsFcErrStatsTxDelta_Type = Counter64
_CucsFcErrStatsTxDelta_Object = MibTableColumn
cucsFcErrStatsTxDelta = _CucsFcErrStatsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 54),
    _CucsFcErrStatsTxDelta_Type()
)
cucsFcErrStatsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTxDelta.setStatus("current")
_CucsFcErrStatsTxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsTxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsTxDeltaAvg = _CucsFcErrStatsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 55),
    _CucsFcErrStatsTxDeltaAvg_Type()
)
cucsFcErrStatsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTxDeltaAvg.setStatus("current")
_CucsFcErrStatsTxDeltaMax_Type = Unsigned64
_CucsFcErrStatsTxDeltaMax_Object = MibTableColumn
cucsFcErrStatsTxDeltaMax = _CucsFcErrStatsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 56),
    _CucsFcErrStatsTxDeltaMax_Type()
)
cucsFcErrStatsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTxDeltaMax.setStatus("current")
_CucsFcErrStatsTxDeltaMin_Type = Unsigned64
_CucsFcErrStatsTxDeltaMin_Object = MibTableColumn
cucsFcErrStatsTxDeltaMin = _CucsFcErrStatsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 57),
    _CucsFcErrStatsTxDeltaMin_Type()
)
cucsFcErrStatsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsTxDeltaMin.setStatus("current")
_CucsFcErrStatsUpdate_Type = Gauge32
_CucsFcErrStatsUpdate_Object = MibTableColumn
cucsFcErrStatsUpdate = _CucsFcErrStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 1, 1, 58),
    _CucsFcErrStatsUpdate_Type()
)
cucsFcErrStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsUpdate.setStatus("current")
_CucsFcErrStatsHistTable_Object = MibTable
cucsFcErrStatsHistTable = _CucsFcErrStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2)
)
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTable.setStatus("current")
_CucsFcErrStatsHistEntry_Object = MibTableRow
cucsFcErrStatsHistEntry = _CucsFcErrStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1)
)
cucsFcErrStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcErrStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcErrStatsHistEntry.setStatus("current")
_CucsFcErrStatsHistInstanceId_Type = CucsManagedObjectId
_CucsFcErrStatsHistInstanceId_Object = MibTableColumn
cucsFcErrStatsHistInstanceId = _CucsFcErrStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 1),
    _CucsFcErrStatsHistInstanceId_Type()
)
cucsFcErrStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistInstanceId.setStatus("current")
_CucsFcErrStatsHistDn_Type = CucsManagedObjectDn
_CucsFcErrStatsHistDn_Object = MibTableColumn
cucsFcErrStatsHistDn = _CucsFcErrStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 2),
    _CucsFcErrStatsHistDn_Type()
)
cucsFcErrStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDn.setStatus("current")
_CucsFcErrStatsHistRn_Type = SnmpAdminString
_CucsFcErrStatsHistRn_Object = MibTableColumn
cucsFcErrStatsHistRn = _CucsFcErrStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 3),
    _CucsFcErrStatsHistRn_Type()
)
cucsFcErrStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistRn.setStatus("current")
_CucsFcErrStatsHistCrcRx_Type = Unsigned64
_CucsFcErrStatsHistCrcRx_Object = MibTableColumn
cucsFcErrStatsHistCrcRx = _CucsFcErrStatsHistCrcRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 4),
    _CucsFcErrStatsHistCrcRx_Type()
)
cucsFcErrStatsHistCrcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistCrcRx.setStatus("current")
_CucsFcErrStatsHistCrcRxDelta_Type = Unsigned64
_CucsFcErrStatsHistCrcRxDelta_Object = MibTableColumn
cucsFcErrStatsHistCrcRxDelta = _CucsFcErrStatsHistCrcRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 5),
    _CucsFcErrStatsHistCrcRxDelta_Type()
)
cucsFcErrStatsHistCrcRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistCrcRxDelta.setStatus("current")
_CucsFcErrStatsHistCrcRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistCrcRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistCrcRxDeltaAvg = _CucsFcErrStatsHistCrcRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 6),
    _CucsFcErrStatsHistCrcRxDeltaAvg_Type()
)
cucsFcErrStatsHistCrcRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistCrcRxDeltaAvg.setStatus("current")
_CucsFcErrStatsHistCrcRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistCrcRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistCrcRxDeltaMax = _CucsFcErrStatsHistCrcRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 7),
    _CucsFcErrStatsHistCrcRxDeltaMax_Type()
)
cucsFcErrStatsHistCrcRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistCrcRxDeltaMax.setStatus("current")
_CucsFcErrStatsHistCrcRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistCrcRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistCrcRxDeltaMin = _CucsFcErrStatsHistCrcRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 8),
    _CucsFcErrStatsHistCrcRxDeltaMin_Type()
)
cucsFcErrStatsHistCrcRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistCrcRxDeltaMin.setStatus("current")
_CucsFcErrStatsHistDiscardRx_Type = Unsigned64
_CucsFcErrStatsHistDiscardRx_Object = MibTableColumn
cucsFcErrStatsHistDiscardRx = _CucsFcErrStatsHistDiscardRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 9),
    _CucsFcErrStatsHistDiscardRx_Type()
)
cucsFcErrStatsHistDiscardRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardRx.setStatus("current")
_CucsFcErrStatsHistDiscardRxDelta_Type = Unsigned64
_CucsFcErrStatsHistDiscardRxDelta_Object = MibTableColumn
cucsFcErrStatsHistDiscardRxDelta = _CucsFcErrStatsHistDiscardRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 10),
    _CucsFcErrStatsHistDiscardRxDelta_Type()
)
cucsFcErrStatsHistDiscardRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardRxDelta.setStatus("current")
_CucsFcErrStatsHistDiscardRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistDiscardRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistDiscardRxDeltaAvg = _CucsFcErrStatsHistDiscardRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 11),
    _CucsFcErrStatsHistDiscardRxDeltaAvg_Type()
)
cucsFcErrStatsHistDiscardRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardRxDeltaAvg.setStatus("current")
_CucsFcErrStatsHistDiscardRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistDiscardRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistDiscardRxDeltaMax = _CucsFcErrStatsHistDiscardRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 12),
    _CucsFcErrStatsHistDiscardRxDeltaMax_Type()
)
cucsFcErrStatsHistDiscardRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardRxDeltaMax.setStatus("current")
_CucsFcErrStatsHistDiscardRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistDiscardRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistDiscardRxDeltaMin = _CucsFcErrStatsHistDiscardRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 13),
    _CucsFcErrStatsHistDiscardRxDeltaMin_Type()
)
cucsFcErrStatsHistDiscardRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardRxDeltaMin.setStatus("current")
_CucsFcErrStatsHistDiscardTx_Type = Unsigned64
_CucsFcErrStatsHistDiscardTx_Object = MibTableColumn
cucsFcErrStatsHistDiscardTx = _CucsFcErrStatsHistDiscardTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 14),
    _CucsFcErrStatsHistDiscardTx_Type()
)
cucsFcErrStatsHistDiscardTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardTx.setStatus("current")
_CucsFcErrStatsHistDiscardTxDelta_Type = Unsigned64
_CucsFcErrStatsHistDiscardTxDelta_Object = MibTableColumn
cucsFcErrStatsHistDiscardTxDelta = _CucsFcErrStatsHistDiscardTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 15),
    _CucsFcErrStatsHistDiscardTxDelta_Type()
)
cucsFcErrStatsHistDiscardTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardTxDelta.setStatus("current")
_CucsFcErrStatsHistDiscardTxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistDiscardTxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistDiscardTxDeltaAvg = _CucsFcErrStatsHistDiscardTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 16),
    _CucsFcErrStatsHistDiscardTxDeltaAvg_Type()
)
cucsFcErrStatsHistDiscardTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardTxDeltaAvg.setStatus("current")
_CucsFcErrStatsHistDiscardTxDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistDiscardTxDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistDiscardTxDeltaMax = _CucsFcErrStatsHistDiscardTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 17),
    _CucsFcErrStatsHistDiscardTxDeltaMax_Type()
)
cucsFcErrStatsHistDiscardTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardTxDeltaMax.setStatus("current")
_CucsFcErrStatsHistDiscardTxDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistDiscardTxDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistDiscardTxDeltaMin = _CucsFcErrStatsHistDiscardTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 18),
    _CucsFcErrStatsHistDiscardTxDeltaMin_Type()
)
cucsFcErrStatsHistDiscardTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistDiscardTxDeltaMin.setStatus("current")
_CucsFcErrStatsHistId_Type = Unsigned64
_CucsFcErrStatsHistId_Object = MibTableColumn
cucsFcErrStatsHistId = _CucsFcErrStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 19),
    _CucsFcErrStatsHistId_Type()
)
cucsFcErrStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistId.setStatus("current")
_CucsFcErrStatsHistLinkFailures_Type = Unsigned64
_CucsFcErrStatsHistLinkFailures_Object = MibTableColumn
cucsFcErrStatsHistLinkFailures = _CucsFcErrStatsHistLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 20),
    _CucsFcErrStatsHistLinkFailures_Type()
)
cucsFcErrStatsHistLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistLinkFailures.setStatus("current")
_CucsFcErrStatsHistLinkFailuresDelta_Type = Unsigned64
_CucsFcErrStatsHistLinkFailuresDelta_Object = MibTableColumn
cucsFcErrStatsHistLinkFailuresDelta = _CucsFcErrStatsHistLinkFailuresDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 21),
    _CucsFcErrStatsHistLinkFailuresDelta_Type()
)
cucsFcErrStatsHistLinkFailuresDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistLinkFailuresDelta.setStatus("current")
_CucsFcErrStatsHistLinkFailuresDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistLinkFailuresDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistLinkFailuresDeltaAvg = _CucsFcErrStatsHistLinkFailuresDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 22),
    _CucsFcErrStatsHistLinkFailuresDeltaAvg_Type()
)
cucsFcErrStatsHistLinkFailuresDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistLinkFailuresDeltaAvg.setStatus("current")
_CucsFcErrStatsHistLinkFailuresDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistLinkFailuresDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistLinkFailuresDeltaMax = _CucsFcErrStatsHistLinkFailuresDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 23),
    _CucsFcErrStatsHistLinkFailuresDeltaMax_Type()
)
cucsFcErrStatsHistLinkFailuresDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistLinkFailuresDeltaMax.setStatus("current")
_CucsFcErrStatsHistLinkFailuresDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistLinkFailuresDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistLinkFailuresDeltaMin = _CucsFcErrStatsHistLinkFailuresDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 24),
    _CucsFcErrStatsHistLinkFailuresDeltaMin_Type()
)
cucsFcErrStatsHistLinkFailuresDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistLinkFailuresDeltaMin.setStatus("current")
_CucsFcErrStatsHistMostRecent_Type = TruthValue
_CucsFcErrStatsHistMostRecent_Object = MibTableColumn
cucsFcErrStatsHistMostRecent = _CucsFcErrStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 25),
    _CucsFcErrStatsHistMostRecent_Type()
)
cucsFcErrStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistMostRecent.setStatus("current")
_CucsFcErrStatsHistRx_Type = Unsigned64
_CucsFcErrStatsHistRx_Object = MibTableColumn
cucsFcErrStatsHistRx = _CucsFcErrStatsHistRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 26),
    _CucsFcErrStatsHistRx_Type()
)
cucsFcErrStatsHistRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistRx.setStatus("current")
_CucsFcErrStatsHistRxDelta_Type = Unsigned64
_CucsFcErrStatsHistRxDelta_Object = MibTableColumn
cucsFcErrStatsHistRxDelta = _CucsFcErrStatsHistRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 27),
    _CucsFcErrStatsHistRxDelta_Type()
)
cucsFcErrStatsHistRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistRxDelta.setStatus("current")
_CucsFcErrStatsHistRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistRxDeltaAvg = _CucsFcErrStatsHistRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 28),
    _CucsFcErrStatsHistRxDeltaAvg_Type()
)
cucsFcErrStatsHistRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistRxDeltaAvg.setStatus("current")
_CucsFcErrStatsHistRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistRxDeltaMax = _CucsFcErrStatsHistRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 29),
    _CucsFcErrStatsHistRxDeltaMax_Type()
)
cucsFcErrStatsHistRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistRxDeltaMax.setStatus("current")
_CucsFcErrStatsHistRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistRxDeltaMin = _CucsFcErrStatsHistRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 30),
    _CucsFcErrStatsHistRxDeltaMin_Type()
)
cucsFcErrStatsHistRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistRxDeltaMin.setStatus("current")
_CucsFcErrStatsHistSignalLosses_Type = Unsigned64
_CucsFcErrStatsHistSignalLosses_Object = MibTableColumn
cucsFcErrStatsHistSignalLosses = _CucsFcErrStatsHistSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 31),
    _CucsFcErrStatsHistSignalLosses_Type()
)
cucsFcErrStatsHistSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSignalLosses.setStatus("current")
_CucsFcErrStatsHistSignalLossesDelta_Type = Unsigned64
_CucsFcErrStatsHistSignalLossesDelta_Object = MibTableColumn
cucsFcErrStatsHistSignalLossesDelta = _CucsFcErrStatsHistSignalLossesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 32),
    _CucsFcErrStatsHistSignalLossesDelta_Type()
)
cucsFcErrStatsHistSignalLossesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSignalLossesDelta.setStatus("current")
_CucsFcErrStatsHistSignalLossesDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistSignalLossesDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistSignalLossesDeltaAvg = _CucsFcErrStatsHistSignalLossesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 33),
    _CucsFcErrStatsHistSignalLossesDeltaAvg_Type()
)
cucsFcErrStatsHistSignalLossesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSignalLossesDeltaAvg.setStatus("current")
_CucsFcErrStatsHistSignalLossesDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistSignalLossesDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistSignalLossesDeltaMax = _CucsFcErrStatsHistSignalLossesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 34),
    _CucsFcErrStatsHistSignalLossesDeltaMax_Type()
)
cucsFcErrStatsHistSignalLossesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSignalLossesDeltaMax.setStatus("current")
_CucsFcErrStatsHistSignalLossesDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistSignalLossesDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistSignalLossesDeltaMin = _CucsFcErrStatsHistSignalLossesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 35),
    _CucsFcErrStatsHistSignalLossesDeltaMin_Type()
)
cucsFcErrStatsHistSignalLossesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSignalLossesDeltaMin.setStatus("current")
_CucsFcErrStatsHistSuspect_Type = TruthValue
_CucsFcErrStatsHistSuspect_Object = MibTableColumn
cucsFcErrStatsHistSuspect = _CucsFcErrStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 36),
    _CucsFcErrStatsHistSuspect_Type()
)
cucsFcErrStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSuspect.setStatus("current")
_CucsFcErrStatsHistSyncLosses_Type = Unsigned64
_CucsFcErrStatsHistSyncLosses_Object = MibTableColumn
cucsFcErrStatsHistSyncLosses = _CucsFcErrStatsHistSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 37),
    _CucsFcErrStatsHistSyncLosses_Type()
)
cucsFcErrStatsHistSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSyncLosses.setStatus("current")
_CucsFcErrStatsHistSyncLossesDelta_Type = Unsigned64
_CucsFcErrStatsHistSyncLossesDelta_Object = MibTableColumn
cucsFcErrStatsHistSyncLossesDelta = _CucsFcErrStatsHistSyncLossesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 38),
    _CucsFcErrStatsHistSyncLossesDelta_Type()
)
cucsFcErrStatsHistSyncLossesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSyncLossesDelta.setStatus("current")
_CucsFcErrStatsHistSyncLossesDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistSyncLossesDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistSyncLossesDeltaAvg = _CucsFcErrStatsHistSyncLossesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 39),
    _CucsFcErrStatsHistSyncLossesDeltaAvg_Type()
)
cucsFcErrStatsHistSyncLossesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSyncLossesDeltaAvg.setStatus("current")
_CucsFcErrStatsHistSyncLossesDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistSyncLossesDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistSyncLossesDeltaMax = _CucsFcErrStatsHistSyncLossesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 40),
    _CucsFcErrStatsHistSyncLossesDeltaMax_Type()
)
cucsFcErrStatsHistSyncLossesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSyncLossesDeltaMax.setStatus("current")
_CucsFcErrStatsHistSyncLossesDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistSyncLossesDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistSyncLossesDeltaMin = _CucsFcErrStatsHistSyncLossesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 41),
    _CucsFcErrStatsHistSyncLossesDeltaMin_Type()
)
cucsFcErrStatsHistSyncLossesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistSyncLossesDeltaMin.setStatus("current")
_CucsFcErrStatsHistThresholded_Type = CucsFcErrStatsHistThresholded
_CucsFcErrStatsHistThresholded_Object = MibTableColumn
cucsFcErrStatsHistThresholded = _CucsFcErrStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 42),
    _CucsFcErrStatsHistThresholded_Type()
)
cucsFcErrStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistThresholded.setStatus("current")
_CucsFcErrStatsHistTimeCollected_Type = DateAndTime
_CucsFcErrStatsHistTimeCollected_Object = MibTableColumn
cucsFcErrStatsHistTimeCollected = _CucsFcErrStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 43),
    _CucsFcErrStatsHistTimeCollected_Type()
)
cucsFcErrStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTimeCollected.setStatus("current")
_CucsFcErrStatsHistTooLongRx_Type = Unsigned64
_CucsFcErrStatsHistTooLongRx_Object = MibTableColumn
cucsFcErrStatsHistTooLongRx = _CucsFcErrStatsHistTooLongRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 44),
    _CucsFcErrStatsHistTooLongRx_Type()
)
cucsFcErrStatsHistTooLongRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooLongRx.setStatus("current")
_CucsFcErrStatsHistTooLongRxDelta_Type = Unsigned64
_CucsFcErrStatsHistTooLongRxDelta_Object = MibTableColumn
cucsFcErrStatsHistTooLongRxDelta = _CucsFcErrStatsHistTooLongRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 45),
    _CucsFcErrStatsHistTooLongRxDelta_Type()
)
cucsFcErrStatsHistTooLongRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooLongRxDelta.setStatus("current")
_CucsFcErrStatsHistTooLongRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistTooLongRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistTooLongRxDeltaAvg = _CucsFcErrStatsHistTooLongRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 46),
    _CucsFcErrStatsHistTooLongRxDeltaAvg_Type()
)
cucsFcErrStatsHistTooLongRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooLongRxDeltaAvg.setStatus("current")
_CucsFcErrStatsHistTooLongRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistTooLongRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistTooLongRxDeltaMax = _CucsFcErrStatsHistTooLongRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 47),
    _CucsFcErrStatsHistTooLongRxDeltaMax_Type()
)
cucsFcErrStatsHistTooLongRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooLongRxDeltaMax.setStatus("current")
_CucsFcErrStatsHistTooLongRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistTooLongRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistTooLongRxDeltaMin = _CucsFcErrStatsHistTooLongRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 48),
    _CucsFcErrStatsHistTooLongRxDeltaMin_Type()
)
cucsFcErrStatsHistTooLongRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooLongRxDeltaMin.setStatus("current")
_CucsFcErrStatsHistTooShortRx_Type = Unsigned64
_CucsFcErrStatsHistTooShortRx_Object = MibTableColumn
cucsFcErrStatsHistTooShortRx = _CucsFcErrStatsHistTooShortRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 49),
    _CucsFcErrStatsHistTooShortRx_Type()
)
cucsFcErrStatsHistTooShortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooShortRx.setStatus("current")
_CucsFcErrStatsHistTooShortRxDelta_Type = Unsigned64
_CucsFcErrStatsHistTooShortRxDelta_Object = MibTableColumn
cucsFcErrStatsHistTooShortRxDelta = _CucsFcErrStatsHistTooShortRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 50),
    _CucsFcErrStatsHistTooShortRxDelta_Type()
)
cucsFcErrStatsHistTooShortRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooShortRxDelta.setStatus("current")
_CucsFcErrStatsHistTooShortRxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistTooShortRxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistTooShortRxDeltaAvg = _CucsFcErrStatsHistTooShortRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 51),
    _CucsFcErrStatsHistTooShortRxDeltaAvg_Type()
)
cucsFcErrStatsHistTooShortRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooShortRxDeltaAvg.setStatus("current")
_CucsFcErrStatsHistTooShortRxDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistTooShortRxDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistTooShortRxDeltaMax = _CucsFcErrStatsHistTooShortRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 52),
    _CucsFcErrStatsHistTooShortRxDeltaMax_Type()
)
cucsFcErrStatsHistTooShortRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooShortRxDeltaMax.setStatus("current")
_CucsFcErrStatsHistTooShortRxDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistTooShortRxDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistTooShortRxDeltaMin = _CucsFcErrStatsHistTooShortRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 53),
    _CucsFcErrStatsHistTooShortRxDeltaMin_Type()
)
cucsFcErrStatsHistTooShortRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTooShortRxDeltaMin.setStatus("current")
_CucsFcErrStatsHistTx_Type = Unsigned64
_CucsFcErrStatsHistTx_Object = MibTableColumn
cucsFcErrStatsHistTx = _CucsFcErrStatsHistTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 54),
    _CucsFcErrStatsHistTx_Type()
)
cucsFcErrStatsHistTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTx.setStatus("current")
_CucsFcErrStatsHistTxDelta_Type = Unsigned64
_CucsFcErrStatsHistTxDelta_Object = MibTableColumn
cucsFcErrStatsHistTxDelta = _CucsFcErrStatsHistTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 55),
    _CucsFcErrStatsHistTxDelta_Type()
)
cucsFcErrStatsHistTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTxDelta.setStatus("current")
_CucsFcErrStatsHistTxDeltaAvg_Type = Unsigned64
_CucsFcErrStatsHistTxDeltaAvg_Object = MibTableColumn
cucsFcErrStatsHistTxDeltaAvg = _CucsFcErrStatsHistTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 56),
    _CucsFcErrStatsHistTxDeltaAvg_Type()
)
cucsFcErrStatsHistTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTxDeltaAvg.setStatus("current")
_CucsFcErrStatsHistTxDeltaMax_Type = Unsigned64
_CucsFcErrStatsHistTxDeltaMax_Object = MibTableColumn
cucsFcErrStatsHistTxDeltaMax = _CucsFcErrStatsHistTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 57),
    _CucsFcErrStatsHistTxDeltaMax_Type()
)
cucsFcErrStatsHistTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTxDeltaMax.setStatus("current")
_CucsFcErrStatsHistTxDeltaMin_Type = Unsigned64
_CucsFcErrStatsHistTxDeltaMin_Object = MibTableColumn
cucsFcErrStatsHistTxDeltaMin = _CucsFcErrStatsHistTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 2, 1, 58),
    _CucsFcErrStatsHistTxDeltaMin_Type()
)
cucsFcErrStatsHistTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcErrStatsHistTxDeltaMin.setStatus("current")
_CucsFcNicIfConfigTable_Object = MibTable
cucsFcNicIfConfigTable = _CucsFcNicIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 3)
)
if mibBuilder.loadTexts:
    cucsFcNicIfConfigTable.setStatus("current")
_CucsFcNicIfConfigEntry_Object = MibTableRow
cucsFcNicIfConfigEntry = _CucsFcNicIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 3, 1)
)
cucsFcNicIfConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcNicIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcNicIfConfigEntry.setStatus("current")
_CucsFcNicIfConfigInstanceId_Type = CucsManagedObjectId
_CucsFcNicIfConfigInstanceId_Object = MibTableColumn
cucsFcNicIfConfigInstanceId = _CucsFcNicIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 3, 1, 1),
    _CucsFcNicIfConfigInstanceId_Type()
)
cucsFcNicIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcNicIfConfigInstanceId.setStatus("current")
_CucsFcNicIfConfigDn_Type = CucsManagedObjectDn
_CucsFcNicIfConfigDn_Object = MibTableColumn
cucsFcNicIfConfigDn = _CucsFcNicIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 3, 1, 2),
    _CucsFcNicIfConfigDn_Type()
)
cucsFcNicIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcNicIfConfigDn.setStatus("current")
_CucsFcNicIfConfigRn_Type = SnmpAdminString
_CucsFcNicIfConfigRn_Object = MibTableColumn
cucsFcNicIfConfigRn = _CucsFcNicIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 3, 1, 3),
    _CucsFcNicIfConfigRn_Type()
)
cucsFcNicIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcNicIfConfigRn.setStatus("current")
_CucsFcPIoTable_Object = MibTable
cucsFcPIoTable = _CucsFcPIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4)
)
if mibBuilder.loadTexts:
    cucsFcPIoTable.setStatus("current")
_CucsFcPIoEntry_Object = MibTableRow
cucsFcPIoEntry = _CucsFcPIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1)
)
cucsFcPIoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcPIoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcPIoEntry.setStatus("current")
_CucsFcPIoInstanceId_Type = CucsManagedObjectId
_CucsFcPIoInstanceId_Object = MibTableColumn
cucsFcPIoInstanceId = _CucsFcPIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 1),
    _CucsFcPIoInstanceId_Type()
)
cucsFcPIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcPIoInstanceId.setStatus("current")
_CucsFcPIoDn_Type = CucsManagedObjectDn
_CucsFcPIoDn_Object = MibTableColumn
cucsFcPIoDn = _CucsFcPIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 2),
    _CucsFcPIoDn_Type()
)
cucsFcPIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoDn.setStatus("current")
_CucsFcPIoRn_Type = SnmpAdminString
_CucsFcPIoRn_Object = MibTableColumn
cucsFcPIoRn = _CucsFcPIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 3),
    _CucsFcPIoRn_Type()
)
cucsFcPIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoRn.setStatus("current")
_CucsFcPIoAdminState_Type = CucsFabricAdminState
_CucsFcPIoAdminState_Object = MibTableColumn
cucsFcPIoAdminState = _CucsFcPIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 4),
    _CucsFcPIoAdminState_Type()
)
cucsFcPIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoAdminState.setStatus("current")
_CucsFcPIoChassisId_Type = Gauge32
_CucsFcPIoChassisId_Object = MibTableColumn
cucsFcPIoChassisId = _CucsFcPIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 5),
    _CucsFcPIoChassisId_Type()
)
cucsFcPIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoChassisId.setStatus("current")
_CucsFcPIoEncap_Type = CucsPortEncap
_CucsFcPIoEncap_Object = MibTableColumn
cucsFcPIoEncap = _CucsFcPIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 6),
    _CucsFcPIoEncap_Type()
)
cucsFcPIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoEncap.setStatus("current")
_CucsFcPIoEpDn_Type = SnmpAdminString
_CucsFcPIoEpDn_Object = MibTableColumn
cucsFcPIoEpDn = _CucsFcPIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 7),
    _CucsFcPIoEpDn_Type()
)
cucsFcPIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoEpDn.setStatus("current")
_CucsFcPIoFltAggr_Type = Unsigned64
_CucsFcPIoFltAggr_Object = MibTableColumn
cucsFcPIoFltAggr = _CucsFcPIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 8),
    _CucsFcPIoFltAggr_Type()
)
cucsFcPIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFltAggr.setStatus("current")
_CucsFcPIoIfRole_Type = CucsNetworkPortRole
_CucsFcPIoIfRole_Object = MibTableColumn
cucsFcPIoIfRole = _CucsFcPIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 9),
    _CucsFcPIoIfRole_Type()
)
cucsFcPIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoIfRole.setStatus("current")
_CucsFcPIoIfType_Type = CucsNetworkPhysEpIfType
_CucsFcPIoIfType_Object = MibTableColumn
cucsFcPIoIfType = _CucsFcPIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 10),
    _CucsFcPIoIfType_Type()
)
cucsFcPIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoIfType.setStatus("current")
_CucsFcPIoLocale_Type = CucsNetworkLocale
_CucsFcPIoLocale_Object = MibTableColumn
cucsFcPIoLocale = _CucsFcPIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 11),
    _CucsFcPIoLocale_Type()
)
cucsFcPIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoLocale.setStatus("current")
_CucsFcPIoMode_Type = CucsPortMode
_CucsFcPIoMode_Object = MibTableColumn
cucsFcPIoMode = _CucsFcPIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 12),
    _CucsFcPIoMode_Type()
)
cucsFcPIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoMode.setStatus("current")
_CucsFcPIoModel_Type = SnmpAdminString
_CucsFcPIoModel_Object = MibTableColumn
cucsFcPIoModel = _CucsFcPIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 13),
    _CucsFcPIoModel_Type()
)
cucsFcPIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoModel.setStatus("current")
_CucsFcPIoName_Type = SnmpAdminString
_CucsFcPIoName_Object = MibTableColumn
cucsFcPIoName = _CucsFcPIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 14),
    _CucsFcPIoName_Type()
)
cucsFcPIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoName.setStatus("current")
_CucsFcPIoOperSpeed_Type = CucsPortSpeed
_CucsFcPIoOperSpeed_Object = MibTableColumn
cucsFcPIoOperSpeed = _CucsFcPIoOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 15),
    _CucsFcPIoOperSpeed_Type()
)
cucsFcPIoOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoOperSpeed.setStatus("current")
_CucsFcPIoOperState_Type = CucsNetworkPortOperState
_CucsFcPIoOperState_Object = MibTableColumn
cucsFcPIoOperState = _CucsFcPIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 16),
    _CucsFcPIoOperState_Type()
)
cucsFcPIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoOperState.setStatus("current")
_CucsFcPIoPeerDn_Type = SnmpAdminString
_CucsFcPIoPeerDn_Object = MibTableColumn
cucsFcPIoPeerDn = _CucsFcPIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 17),
    _CucsFcPIoPeerDn_Type()
)
cucsFcPIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoPeerDn.setStatus("current")
_CucsFcPIoPeerPortId_Type = Gauge32
_CucsFcPIoPeerPortId_Object = MibTableColumn
cucsFcPIoPeerPortId = _CucsFcPIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 18),
    _CucsFcPIoPeerPortId_Type()
)
cucsFcPIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoPeerPortId.setStatus("current")
_CucsFcPIoPeerSlotId_Type = Gauge32
_CucsFcPIoPeerSlotId_Object = MibTableColumn
cucsFcPIoPeerSlotId = _CucsFcPIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 19),
    _CucsFcPIoPeerSlotId_Type()
)
cucsFcPIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoPeerSlotId.setStatus("current")
_CucsFcPIoPortId_Type = Gauge32
_CucsFcPIoPortId_Object = MibTableColumn
cucsFcPIoPortId = _CucsFcPIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 20),
    _CucsFcPIoPortId_Type()
)
cucsFcPIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoPortId.setStatus("current")
_CucsFcPIoRevision_Type = SnmpAdminString
_CucsFcPIoRevision_Object = MibTableColumn
cucsFcPIoRevision = _CucsFcPIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 21),
    _CucsFcPIoRevision_Type()
)
cucsFcPIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoRevision.setStatus("current")
_CucsFcPIoSerial_Type = SnmpAdminString
_CucsFcPIoSerial_Object = MibTableColumn
cucsFcPIoSerial = _CucsFcPIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 22),
    _CucsFcPIoSerial_Type()
)
cucsFcPIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoSerial.setStatus("current")
_CucsFcPIoSlotId_Type = Gauge32
_CucsFcPIoSlotId_Object = MibTableColumn
cucsFcPIoSlotId = _CucsFcPIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 23),
    _CucsFcPIoSlotId_Type()
)
cucsFcPIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoSlotId.setStatus("current")
_CucsFcPIoStateQual_Type = SnmpAdminString
_CucsFcPIoStateQual_Object = MibTableColumn
cucsFcPIoStateQual = _CucsFcPIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 24),
    _CucsFcPIoStateQual_Type()
)
cucsFcPIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoStateQual.setStatus("current")
_CucsFcPIoSwitchId_Type = CucsNetworkSwitchId
_CucsFcPIoSwitchId_Object = MibTableColumn
cucsFcPIoSwitchId = _CucsFcPIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 25),
    _CucsFcPIoSwitchId_Type()
)
cucsFcPIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoSwitchId.setStatus("current")
_CucsFcPIoTransport_Type = CucsNetworkTransport
_CucsFcPIoTransport_Object = MibTableColumn
cucsFcPIoTransport = _CucsFcPIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 26),
    _CucsFcPIoTransport_Type()
)
cucsFcPIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoTransport.setStatus("current")
_CucsFcPIoTs_Type = DateAndTime
_CucsFcPIoTs_Object = MibTableColumn
cucsFcPIoTs = _CucsFcPIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 27),
    _CucsFcPIoTs_Type()
)
cucsFcPIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoTs.setStatus("current")
_CucsFcPIoType_Type = CucsNetworkConnectionType
_CucsFcPIoType_Object = MibTableColumn
cucsFcPIoType = _CucsFcPIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 28),
    _CucsFcPIoType_Type()
)
cucsFcPIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoType.setStatus("current")
_CucsFcPIoUsrLbl_Type = SnmpAdminString
_CucsFcPIoUsrLbl_Object = MibTableColumn
cucsFcPIoUsrLbl = _CucsFcPIoUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 29),
    _CucsFcPIoUsrLbl_Type()
)
cucsFcPIoUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoUsrLbl.setStatus("current")
_CucsFcPIoVendor_Type = SnmpAdminString
_CucsFcPIoVendor_Object = MibTableColumn
cucsFcPIoVendor = _CucsFcPIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 30),
    _CucsFcPIoVendor_Type()
)
cucsFcPIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoVendor.setStatus("current")
_CucsFcPIoWwn_Type = Unsigned64
_CucsFcPIoWwn_Object = MibTableColumn
cucsFcPIoWwn = _CucsFcPIoWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 31),
    _CucsFcPIoWwn_Type()
)
cucsFcPIoWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoWwn.setStatus("current")
_CucsFcPIoFsmDescr_Type = SnmpAdminString
_CucsFcPIoFsmDescr_Object = MibTableColumn
cucsFcPIoFsmDescr = _CucsFcPIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 32),
    _CucsFcPIoFsmDescr_Type()
)
cucsFcPIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmDescr.setStatus("current")
_CucsFcPIoFsmPrev_Type = SnmpAdminString
_CucsFcPIoFsmPrev_Object = MibTableColumn
cucsFcPIoFsmPrev = _CucsFcPIoFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 33),
    _CucsFcPIoFsmPrev_Type()
)
cucsFcPIoFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmPrev.setStatus("current")
_CucsFcPIoFsmProgr_Type = Gauge32
_CucsFcPIoFsmProgr_Object = MibTableColumn
cucsFcPIoFsmProgr = _CucsFcPIoFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 34),
    _CucsFcPIoFsmProgr_Type()
)
cucsFcPIoFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmProgr.setStatus("current")
_CucsFcPIoFsmRmtInvErrCode_Type = Gauge32
_CucsFcPIoFsmRmtInvErrCode_Object = MibTableColumn
cucsFcPIoFsmRmtInvErrCode = _CucsFcPIoFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 35),
    _CucsFcPIoFsmRmtInvErrCode_Type()
)
cucsFcPIoFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmRmtInvErrCode.setStatus("current")
_CucsFcPIoFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsFcPIoFsmRmtInvErrDescr_Object = MibTableColumn
cucsFcPIoFsmRmtInvErrDescr = _CucsFcPIoFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 36),
    _CucsFcPIoFsmRmtInvErrDescr_Type()
)
cucsFcPIoFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmRmtInvErrDescr.setStatus("current")
_CucsFcPIoFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsFcPIoFsmRmtInvRslt_Object = MibTableColumn
cucsFcPIoFsmRmtInvRslt = _CucsFcPIoFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 37),
    _CucsFcPIoFsmRmtInvRslt_Type()
)
cucsFcPIoFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmRmtInvRslt.setStatus("current")
_CucsFcPIoFsmStageDescr_Type = SnmpAdminString
_CucsFcPIoFsmStageDescr_Object = MibTableColumn
cucsFcPIoFsmStageDescr = _CucsFcPIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 38),
    _CucsFcPIoFsmStageDescr_Type()
)
cucsFcPIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageDescr.setStatus("current")
_CucsFcPIoFsmStamp_Type = DateAndTime
_CucsFcPIoFsmStamp_Object = MibTableColumn
cucsFcPIoFsmStamp = _CucsFcPIoFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 39),
    _CucsFcPIoFsmStamp_Type()
)
cucsFcPIoFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStamp.setStatus("current")
_CucsFcPIoFsmStatus_Type = SnmpAdminString
_CucsFcPIoFsmStatus_Object = MibTableColumn
cucsFcPIoFsmStatus = _CucsFcPIoFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 40),
    _CucsFcPIoFsmStatus_Type()
)
cucsFcPIoFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStatus.setStatus("current")
_CucsFcPIoFsmTry_Type = Gauge32
_CucsFcPIoFsmTry_Object = MibTableColumn
cucsFcPIoFsmTry = _CucsFcPIoFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 41),
    _CucsFcPIoFsmTry_Type()
)
cucsFcPIoFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmTry.setStatus("current")
_CucsFcPIoLicGP_Type = Unsigned64
_CucsFcPIoLicGP_Object = MibTableColumn
cucsFcPIoLicGP = _CucsFcPIoLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 42),
    _CucsFcPIoLicGP_Type()
)
cucsFcPIoLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoLicGP.setStatus("current")
_CucsFcPIoLicState_Type = CucsLicenseState
_CucsFcPIoLicState_Object = MibTableColumn
cucsFcPIoLicState = _CucsFcPIoLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 43),
    _CucsFcPIoLicState_Type()
)
cucsFcPIoLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoLicState.setStatus("current")
_CucsFcPIoXcvrType_Type = CucsEquipmentXcvrType
_CucsFcPIoXcvrType_Object = MibTableColumn
cucsFcPIoXcvrType = _CucsFcPIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 44),
    _CucsFcPIoXcvrType_Type()
)
cucsFcPIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoXcvrType.setStatus("current")
_CucsFcPIoPeerChassisId_Type = Gauge32
_CucsFcPIoPeerChassisId_Object = MibTableColumn
cucsFcPIoPeerChassisId = _CucsFcPIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 45),
    _CucsFcPIoPeerChassisId_Type()
)
cucsFcPIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoPeerChassisId.setStatus("current")
_CucsFcPIoAdminTransport_Type = CucsNetworkTransport
_CucsFcPIoAdminTransport_Object = MibTableColumn
cucsFcPIoAdminTransport = _CucsFcPIoAdminTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 46),
    _CucsFcPIoAdminTransport_Type()
)
cucsFcPIoAdminTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoAdminTransport.setStatus("current")
_CucsFcPIoLc_Type = CucsFsmLifecycle
_CucsFcPIoLc_Object = MibTableColumn
cucsFcPIoLc = _CucsFcPIoLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 47),
    _CucsFcPIoLc_Type()
)
cucsFcPIoLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoLc.setStatus("current")
_CucsFcPIoUnifiedPort_Type = TruthValue
_CucsFcPIoUnifiedPort_Object = MibTableColumn
cucsFcPIoUnifiedPort = _CucsFcPIoUnifiedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 48),
    _CucsFcPIoUnifiedPort_Type()
)
cucsFcPIoUnifiedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoUnifiedPort.setStatus("current")
_CucsFcPIoMaxSpeed_Type = CucsPortSpeed
_CucsFcPIoMaxSpeed_Object = MibTableColumn
cucsFcPIoMaxSpeed = _CucsFcPIoMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 49),
    _CucsFcPIoMaxSpeed_Type()
)
cucsFcPIoMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoMaxSpeed.setStatus("current")
_CucsFcPIoIsPortChannelMember_Type = TruthValue
_CucsFcPIoIsPortChannelMember_Object = MibTableColumn
cucsFcPIoIsPortChannelMember = _CucsFcPIoIsPortChannelMember_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 50),
    _CucsFcPIoIsPortChannelMember_Type()
)
cucsFcPIoIsPortChannelMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoIsPortChannelMember.setStatus("current")
_CucsFcPIoAggrPortId_Type = Gauge32
_CucsFcPIoAggrPortId_Object = MibTableColumn
cucsFcPIoAggrPortId = _CucsFcPIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 51),
    _CucsFcPIoAggrPortId_Type()
)
cucsFcPIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoAggrPortId.setStatus("current")
_CucsFcPIoPeerAggrPortId_Type = Gauge32
_CucsFcPIoPeerAggrPortId_Object = MibTableColumn
cucsFcPIoPeerAggrPortId = _CucsFcPIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 4, 1, 52),
    _CucsFcPIoPeerAggrPortId_Type()
)
cucsFcPIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoPeerAggrPortId.setStatus("current")
_CucsFcStatsTable_Object = MibTable
cucsFcStatsTable = _CucsFcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5)
)
if mibBuilder.loadTexts:
    cucsFcStatsTable.setStatus("current")
_CucsFcStatsEntry_Object = MibTableRow
cucsFcStatsEntry = _CucsFcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1)
)
cucsFcStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcStatsEntry.setStatus("current")
_CucsFcStatsInstanceId_Type = CucsManagedObjectId
_CucsFcStatsInstanceId_Object = MibTableColumn
cucsFcStatsInstanceId = _CucsFcStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 1),
    _CucsFcStatsInstanceId_Type()
)
cucsFcStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcStatsInstanceId.setStatus("current")
_CucsFcStatsDn_Type = CucsManagedObjectDn
_CucsFcStatsDn_Object = MibTableColumn
cucsFcStatsDn = _CucsFcStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 2),
    _CucsFcStatsDn_Type()
)
cucsFcStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsDn.setStatus("current")
_CucsFcStatsRn_Type = SnmpAdminString
_CucsFcStatsRn_Object = MibTableColumn
cucsFcStatsRn = _CucsFcStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 3),
    _CucsFcStatsRn_Type()
)
cucsFcStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsRn.setStatus("current")
_CucsFcStatsBytesRx_Type = Unsigned64
_CucsFcStatsBytesRx_Object = MibTableColumn
cucsFcStatsBytesRx = _CucsFcStatsBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 4),
    _CucsFcStatsBytesRx_Type()
)
cucsFcStatsBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesRx.setStatus("current")
_CucsFcStatsBytesRxDelta_Type = Counter64
_CucsFcStatsBytesRxDelta_Object = MibTableColumn
cucsFcStatsBytesRxDelta = _CucsFcStatsBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 5),
    _CucsFcStatsBytesRxDelta_Type()
)
cucsFcStatsBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesRxDelta.setStatus("current")
_CucsFcStatsBytesRxDeltaAvg_Type = Unsigned64
_CucsFcStatsBytesRxDeltaAvg_Object = MibTableColumn
cucsFcStatsBytesRxDeltaAvg = _CucsFcStatsBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 6),
    _CucsFcStatsBytesRxDeltaAvg_Type()
)
cucsFcStatsBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesRxDeltaAvg.setStatus("current")
_CucsFcStatsBytesRxDeltaMax_Type = Unsigned64
_CucsFcStatsBytesRxDeltaMax_Object = MibTableColumn
cucsFcStatsBytesRxDeltaMax = _CucsFcStatsBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 7),
    _CucsFcStatsBytesRxDeltaMax_Type()
)
cucsFcStatsBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesRxDeltaMax.setStatus("current")
_CucsFcStatsBytesRxDeltaMin_Type = Unsigned64
_CucsFcStatsBytesRxDeltaMin_Object = MibTableColumn
cucsFcStatsBytesRxDeltaMin = _CucsFcStatsBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 8),
    _CucsFcStatsBytesRxDeltaMin_Type()
)
cucsFcStatsBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesRxDeltaMin.setStatus("current")
_CucsFcStatsBytesTx_Type = Unsigned64
_CucsFcStatsBytesTx_Object = MibTableColumn
cucsFcStatsBytesTx = _CucsFcStatsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 9),
    _CucsFcStatsBytesTx_Type()
)
cucsFcStatsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesTx.setStatus("current")
_CucsFcStatsBytesTxDelta_Type = Counter64
_CucsFcStatsBytesTxDelta_Object = MibTableColumn
cucsFcStatsBytesTxDelta = _CucsFcStatsBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 10),
    _CucsFcStatsBytesTxDelta_Type()
)
cucsFcStatsBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesTxDelta.setStatus("current")
_CucsFcStatsBytesTxDeltaAvg_Type = Unsigned64
_CucsFcStatsBytesTxDeltaAvg_Object = MibTableColumn
cucsFcStatsBytesTxDeltaAvg = _CucsFcStatsBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 11),
    _CucsFcStatsBytesTxDeltaAvg_Type()
)
cucsFcStatsBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesTxDeltaAvg.setStatus("current")
_CucsFcStatsBytesTxDeltaMax_Type = Unsigned64
_CucsFcStatsBytesTxDeltaMax_Object = MibTableColumn
cucsFcStatsBytesTxDeltaMax = _CucsFcStatsBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 12),
    _CucsFcStatsBytesTxDeltaMax_Type()
)
cucsFcStatsBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesTxDeltaMax.setStatus("current")
_CucsFcStatsBytesTxDeltaMin_Type = Unsigned64
_CucsFcStatsBytesTxDeltaMin_Object = MibTableColumn
cucsFcStatsBytesTxDeltaMin = _CucsFcStatsBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 13),
    _CucsFcStatsBytesTxDeltaMin_Type()
)
cucsFcStatsBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsBytesTxDeltaMin.setStatus("current")
_CucsFcStatsIntervals_Type = Gauge32
_CucsFcStatsIntervals_Object = MibTableColumn
cucsFcStatsIntervals = _CucsFcStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 14),
    _CucsFcStatsIntervals_Type()
)
cucsFcStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsIntervals.setStatus("current")
_CucsFcStatsPacketsRx_Type = Unsigned64
_CucsFcStatsPacketsRx_Object = MibTableColumn
cucsFcStatsPacketsRx = _CucsFcStatsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 15),
    _CucsFcStatsPacketsRx_Type()
)
cucsFcStatsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsRx.setStatus("current")
_CucsFcStatsPacketsRxDelta_Type = Counter64
_CucsFcStatsPacketsRxDelta_Object = MibTableColumn
cucsFcStatsPacketsRxDelta = _CucsFcStatsPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 16),
    _CucsFcStatsPacketsRxDelta_Type()
)
cucsFcStatsPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsRxDelta.setStatus("current")
_CucsFcStatsPacketsRxDeltaAvg_Type = Unsigned64
_CucsFcStatsPacketsRxDeltaAvg_Object = MibTableColumn
cucsFcStatsPacketsRxDeltaAvg = _CucsFcStatsPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 17),
    _CucsFcStatsPacketsRxDeltaAvg_Type()
)
cucsFcStatsPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsRxDeltaAvg.setStatus("current")
_CucsFcStatsPacketsRxDeltaMax_Type = Unsigned64
_CucsFcStatsPacketsRxDeltaMax_Object = MibTableColumn
cucsFcStatsPacketsRxDeltaMax = _CucsFcStatsPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 18),
    _CucsFcStatsPacketsRxDeltaMax_Type()
)
cucsFcStatsPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsRxDeltaMax.setStatus("current")
_CucsFcStatsPacketsRxDeltaMin_Type = Unsigned64
_CucsFcStatsPacketsRxDeltaMin_Object = MibTableColumn
cucsFcStatsPacketsRxDeltaMin = _CucsFcStatsPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 19),
    _CucsFcStatsPacketsRxDeltaMin_Type()
)
cucsFcStatsPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsRxDeltaMin.setStatus("current")
_CucsFcStatsPacketsTx_Type = Unsigned64
_CucsFcStatsPacketsTx_Object = MibTableColumn
cucsFcStatsPacketsTx = _CucsFcStatsPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 20),
    _CucsFcStatsPacketsTx_Type()
)
cucsFcStatsPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsTx.setStatus("current")
_CucsFcStatsPacketsTxDelta_Type = Counter64
_CucsFcStatsPacketsTxDelta_Object = MibTableColumn
cucsFcStatsPacketsTxDelta = _CucsFcStatsPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 21),
    _CucsFcStatsPacketsTxDelta_Type()
)
cucsFcStatsPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsTxDelta.setStatus("current")
_CucsFcStatsPacketsTxDeltaAvg_Type = Unsigned64
_CucsFcStatsPacketsTxDeltaAvg_Object = MibTableColumn
cucsFcStatsPacketsTxDeltaAvg = _CucsFcStatsPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 22),
    _CucsFcStatsPacketsTxDeltaAvg_Type()
)
cucsFcStatsPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsTxDeltaAvg.setStatus("current")
_CucsFcStatsPacketsTxDeltaMax_Type = Unsigned64
_CucsFcStatsPacketsTxDeltaMax_Object = MibTableColumn
cucsFcStatsPacketsTxDeltaMax = _CucsFcStatsPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 23),
    _CucsFcStatsPacketsTxDeltaMax_Type()
)
cucsFcStatsPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsTxDeltaMax.setStatus("current")
_CucsFcStatsPacketsTxDeltaMin_Type = Unsigned64
_CucsFcStatsPacketsTxDeltaMin_Object = MibTableColumn
cucsFcStatsPacketsTxDeltaMin = _CucsFcStatsPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 24),
    _CucsFcStatsPacketsTxDeltaMin_Type()
)
cucsFcStatsPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsPacketsTxDeltaMin.setStatus("current")
_CucsFcStatsSuspect_Type = TruthValue
_CucsFcStatsSuspect_Object = MibTableColumn
cucsFcStatsSuspect = _CucsFcStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 25),
    _CucsFcStatsSuspect_Type()
)
cucsFcStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsSuspect.setStatus("current")
_CucsFcStatsThresholded_Type = CucsFcStatsThresholded
_CucsFcStatsThresholded_Object = MibTableColumn
cucsFcStatsThresholded = _CucsFcStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 26),
    _CucsFcStatsThresholded_Type()
)
cucsFcStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsThresholded.setStatus("current")
_CucsFcStatsTimeCollected_Type = DateAndTime
_CucsFcStatsTimeCollected_Object = MibTableColumn
cucsFcStatsTimeCollected = _CucsFcStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 27),
    _CucsFcStatsTimeCollected_Type()
)
cucsFcStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsTimeCollected.setStatus("current")
_CucsFcStatsUpdate_Type = Gauge32
_CucsFcStatsUpdate_Object = MibTableColumn
cucsFcStatsUpdate = _CucsFcStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 5, 1, 28),
    _CucsFcStatsUpdate_Type()
)
cucsFcStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsUpdate.setStatus("current")
_CucsFcStatsHistTable_Object = MibTable
cucsFcStatsHistTable = _CucsFcStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6)
)
if mibBuilder.loadTexts:
    cucsFcStatsHistTable.setStatus("current")
_CucsFcStatsHistEntry_Object = MibTableRow
cucsFcStatsHistEntry = _CucsFcStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1)
)
cucsFcStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcStatsHistEntry.setStatus("current")
_CucsFcStatsHistInstanceId_Type = CucsManagedObjectId
_CucsFcStatsHistInstanceId_Object = MibTableColumn
cucsFcStatsHistInstanceId = _CucsFcStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 1),
    _CucsFcStatsHistInstanceId_Type()
)
cucsFcStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcStatsHistInstanceId.setStatus("current")
_CucsFcStatsHistDn_Type = CucsManagedObjectDn
_CucsFcStatsHistDn_Object = MibTableColumn
cucsFcStatsHistDn = _CucsFcStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 2),
    _CucsFcStatsHistDn_Type()
)
cucsFcStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistDn.setStatus("current")
_CucsFcStatsHistRn_Type = SnmpAdminString
_CucsFcStatsHistRn_Object = MibTableColumn
cucsFcStatsHistRn = _CucsFcStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 3),
    _CucsFcStatsHistRn_Type()
)
cucsFcStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistRn.setStatus("current")
_CucsFcStatsHistBytesRx_Type = Unsigned64
_CucsFcStatsHistBytesRx_Object = MibTableColumn
cucsFcStatsHistBytesRx = _CucsFcStatsHistBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 4),
    _CucsFcStatsHistBytesRx_Type()
)
cucsFcStatsHistBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesRx.setStatus("current")
_CucsFcStatsHistBytesRxDelta_Type = Unsigned64
_CucsFcStatsHistBytesRxDelta_Object = MibTableColumn
cucsFcStatsHistBytesRxDelta = _CucsFcStatsHistBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 5),
    _CucsFcStatsHistBytesRxDelta_Type()
)
cucsFcStatsHistBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesRxDelta.setStatus("current")
_CucsFcStatsHistBytesRxDeltaAvg_Type = Unsigned64
_CucsFcStatsHistBytesRxDeltaAvg_Object = MibTableColumn
cucsFcStatsHistBytesRxDeltaAvg = _CucsFcStatsHistBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 6),
    _CucsFcStatsHistBytesRxDeltaAvg_Type()
)
cucsFcStatsHistBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesRxDeltaAvg.setStatus("current")
_CucsFcStatsHistBytesRxDeltaMax_Type = Unsigned64
_CucsFcStatsHistBytesRxDeltaMax_Object = MibTableColumn
cucsFcStatsHistBytesRxDeltaMax = _CucsFcStatsHistBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 7),
    _CucsFcStatsHistBytesRxDeltaMax_Type()
)
cucsFcStatsHistBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesRxDeltaMax.setStatus("current")
_CucsFcStatsHistBytesRxDeltaMin_Type = Unsigned64
_CucsFcStatsHistBytesRxDeltaMin_Object = MibTableColumn
cucsFcStatsHistBytesRxDeltaMin = _CucsFcStatsHistBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 8),
    _CucsFcStatsHistBytesRxDeltaMin_Type()
)
cucsFcStatsHistBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesRxDeltaMin.setStatus("current")
_CucsFcStatsHistBytesTx_Type = Unsigned64
_CucsFcStatsHistBytesTx_Object = MibTableColumn
cucsFcStatsHistBytesTx = _CucsFcStatsHistBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 9),
    _CucsFcStatsHistBytesTx_Type()
)
cucsFcStatsHistBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesTx.setStatus("current")
_CucsFcStatsHistBytesTxDelta_Type = Unsigned64
_CucsFcStatsHistBytesTxDelta_Object = MibTableColumn
cucsFcStatsHistBytesTxDelta = _CucsFcStatsHistBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 10),
    _CucsFcStatsHistBytesTxDelta_Type()
)
cucsFcStatsHistBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesTxDelta.setStatus("current")
_CucsFcStatsHistBytesTxDeltaAvg_Type = Unsigned64
_CucsFcStatsHistBytesTxDeltaAvg_Object = MibTableColumn
cucsFcStatsHistBytesTxDeltaAvg = _CucsFcStatsHistBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 11),
    _CucsFcStatsHistBytesTxDeltaAvg_Type()
)
cucsFcStatsHistBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesTxDeltaAvg.setStatus("current")
_CucsFcStatsHistBytesTxDeltaMax_Type = Unsigned64
_CucsFcStatsHistBytesTxDeltaMax_Object = MibTableColumn
cucsFcStatsHistBytesTxDeltaMax = _CucsFcStatsHistBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 12),
    _CucsFcStatsHistBytesTxDeltaMax_Type()
)
cucsFcStatsHistBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesTxDeltaMax.setStatus("current")
_CucsFcStatsHistBytesTxDeltaMin_Type = Unsigned64
_CucsFcStatsHistBytesTxDeltaMin_Object = MibTableColumn
cucsFcStatsHistBytesTxDeltaMin = _CucsFcStatsHistBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 13),
    _CucsFcStatsHistBytesTxDeltaMin_Type()
)
cucsFcStatsHistBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistBytesTxDeltaMin.setStatus("current")
_CucsFcStatsHistId_Type = Unsigned64
_CucsFcStatsHistId_Object = MibTableColumn
cucsFcStatsHistId = _CucsFcStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 14),
    _CucsFcStatsHistId_Type()
)
cucsFcStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistId.setStatus("current")
_CucsFcStatsHistMostRecent_Type = TruthValue
_CucsFcStatsHistMostRecent_Object = MibTableColumn
cucsFcStatsHistMostRecent = _CucsFcStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 15),
    _CucsFcStatsHistMostRecent_Type()
)
cucsFcStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistMostRecent.setStatus("current")
_CucsFcStatsHistPacketsRx_Type = Unsigned64
_CucsFcStatsHistPacketsRx_Object = MibTableColumn
cucsFcStatsHistPacketsRx = _CucsFcStatsHistPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 16),
    _CucsFcStatsHistPacketsRx_Type()
)
cucsFcStatsHistPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsRx.setStatus("current")
_CucsFcStatsHistPacketsRxDelta_Type = Unsigned64
_CucsFcStatsHistPacketsRxDelta_Object = MibTableColumn
cucsFcStatsHistPacketsRxDelta = _CucsFcStatsHistPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 17),
    _CucsFcStatsHistPacketsRxDelta_Type()
)
cucsFcStatsHistPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsRxDelta.setStatus("current")
_CucsFcStatsHistPacketsRxDeltaAvg_Type = Unsigned64
_CucsFcStatsHistPacketsRxDeltaAvg_Object = MibTableColumn
cucsFcStatsHistPacketsRxDeltaAvg = _CucsFcStatsHistPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 18),
    _CucsFcStatsHistPacketsRxDeltaAvg_Type()
)
cucsFcStatsHistPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsRxDeltaAvg.setStatus("current")
_CucsFcStatsHistPacketsRxDeltaMax_Type = Unsigned64
_CucsFcStatsHistPacketsRxDeltaMax_Object = MibTableColumn
cucsFcStatsHistPacketsRxDeltaMax = _CucsFcStatsHistPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 19),
    _CucsFcStatsHistPacketsRxDeltaMax_Type()
)
cucsFcStatsHistPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsRxDeltaMax.setStatus("current")
_CucsFcStatsHistPacketsRxDeltaMin_Type = Unsigned64
_CucsFcStatsHistPacketsRxDeltaMin_Object = MibTableColumn
cucsFcStatsHistPacketsRxDeltaMin = _CucsFcStatsHistPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 20),
    _CucsFcStatsHistPacketsRxDeltaMin_Type()
)
cucsFcStatsHistPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsRxDeltaMin.setStatus("current")
_CucsFcStatsHistPacketsTx_Type = Unsigned64
_CucsFcStatsHistPacketsTx_Object = MibTableColumn
cucsFcStatsHistPacketsTx = _CucsFcStatsHistPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 21),
    _CucsFcStatsHistPacketsTx_Type()
)
cucsFcStatsHistPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsTx.setStatus("current")
_CucsFcStatsHistPacketsTxDelta_Type = Unsigned64
_CucsFcStatsHistPacketsTxDelta_Object = MibTableColumn
cucsFcStatsHistPacketsTxDelta = _CucsFcStatsHistPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 22),
    _CucsFcStatsHistPacketsTxDelta_Type()
)
cucsFcStatsHistPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsTxDelta.setStatus("current")
_CucsFcStatsHistPacketsTxDeltaAvg_Type = Unsigned64
_CucsFcStatsHistPacketsTxDeltaAvg_Object = MibTableColumn
cucsFcStatsHistPacketsTxDeltaAvg = _CucsFcStatsHistPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 23),
    _CucsFcStatsHistPacketsTxDeltaAvg_Type()
)
cucsFcStatsHistPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsTxDeltaAvg.setStatus("current")
_CucsFcStatsHistPacketsTxDeltaMax_Type = Unsigned64
_CucsFcStatsHistPacketsTxDeltaMax_Object = MibTableColumn
cucsFcStatsHistPacketsTxDeltaMax = _CucsFcStatsHistPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 24),
    _CucsFcStatsHistPacketsTxDeltaMax_Type()
)
cucsFcStatsHistPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsTxDeltaMax.setStatus("current")
_CucsFcStatsHistPacketsTxDeltaMin_Type = Unsigned64
_CucsFcStatsHistPacketsTxDeltaMin_Object = MibTableColumn
cucsFcStatsHistPacketsTxDeltaMin = _CucsFcStatsHistPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 25),
    _CucsFcStatsHistPacketsTxDeltaMin_Type()
)
cucsFcStatsHistPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistPacketsTxDeltaMin.setStatus("current")
_CucsFcStatsHistSuspect_Type = TruthValue
_CucsFcStatsHistSuspect_Object = MibTableColumn
cucsFcStatsHistSuspect = _CucsFcStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 26),
    _CucsFcStatsHistSuspect_Type()
)
cucsFcStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistSuspect.setStatus("current")
_CucsFcStatsHistThresholded_Type = CucsFcStatsHistThresholded
_CucsFcStatsHistThresholded_Object = MibTableColumn
cucsFcStatsHistThresholded = _CucsFcStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 27),
    _CucsFcStatsHistThresholded_Type()
)
cucsFcStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistThresholded.setStatus("current")
_CucsFcStatsHistTimeCollected_Type = DateAndTime
_CucsFcStatsHistTimeCollected_Object = MibTableColumn
cucsFcStatsHistTimeCollected = _CucsFcStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 6, 1, 28),
    _CucsFcStatsHistTimeCollected_Type()
)
cucsFcStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcStatsHistTimeCollected.setStatus("current")
_CucsFcSwIfConfigTable_Object = MibTable
cucsFcSwIfConfigTable = _CucsFcSwIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 7)
)
if mibBuilder.loadTexts:
    cucsFcSwIfConfigTable.setStatus("current")
_CucsFcSwIfConfigEntry_Object = MibTableRow
cucsFcSwIfConfigEntry = _CucsFcSwIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 7, 1)
)
cucsFcSwIfConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcSwIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcSwIfConfigEntry.setStatus("current")
_CucsFcSwIfConfigInstanceId_Type = CucsManagedObjectId
_CucsFcSwIfConfigInstanceId_Object = MibTableColumn
cucsFcSwIfConfigInstanceId = _CucsFcSwIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 7, 1, 1),
    _CucsFcSwIfConfigInstanceId_Type()
)
cucsFcSwIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcSwIfConfigInstanceId.setStatus("current")
_CucsFcSwIfConfigDn_Type = CucsManagedObjectDn
_CucsFcSwIfConfigDn_Object = MibTableColumn
cucsFcSwIfConfigDn = _CucsFcSwIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 7, 1, 2),
    _CucsFcSwIfConfigDn_Type()
)
cucsFcSwIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcSwIfConfigDn.setStatus("current")
_CucsFcSwIfConfigRn_Type = SnmpAdminString
_CucsFcSwIfConfigRn_Object = MibTableColumn
cucsFcSwIfConfigRn = _CucsFcSwIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 7, 1, 3),
    _CucsFcSwIfConfigRn_Type()
)
cucsFcSwIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcSwIfConfigRn.setStatus("current")
_CucsFcPIoFsmTable_Object = MibTable
cucsFcPIoFsmTable = _CucsFcPIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8)
)
if mibBuilder.loadTexts:
    cucsFcPIoFsmTable.setStatus("current")
_CucsFcPIoFsmEntry_Object = MibTableRow
cucsFcPIoFsmEntry = _CucsFcPIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1)
)
cucsFcPIoFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcPIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcPIoFsmEntry.setStatus("current")
_CucsFcPIoFsmInstanceId_Type = CucsManagedObjectId
_CucsFcPIoFsmInstanceId_Object = MibTableColumn
cucsFcPIoFsmInstanceId = _CucsFcPIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 1),
    _CucsFcPIoFsmInstanceId_Type()
)
cucsFcPIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcPIoFsmInstanceId.setStatus("current")
_CucsFcPIoFsmDn_Type = CucsManagedObjectDn
_CucsFcPIoFsmDn_Object = MibTableColumn
cucsFcPIoFsmDn = _CucsFcPIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 2),
    _CucsFcPIoFsmDn_Type()
)
cucsFcPIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmDn.setStatus("current")
_CucsFcPIoFsmRn_Type = SnmpAdminString
_CucsFcPIoFsmRn_Object = MibTableColumn
cucsFcPIoFsmRn = _CucsFcPIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 3),
    _CucsFcPIoFsmRn_Type()
)
cucsFcPIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmRn.setStatus("current")
_CucsFcPIoFsmCompletionTime_Type = DateAndTime
_CucsFcPIoFsmCompletionTime_Object = MibTableColumn
cucsFcPIoFsmCompletionTime = _CucsFcPIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 4),
    _CucsFcPIoFsmCompletionTime_Type()
)
cucsFcPIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmCompletionTime.setStatus("current")
_CucsFcPIoFsmCurrentFsm_Type = CucsFcPIoFsmCurrentFsm
_CucsFcPIoFsmCurrentFsm_Object = MibTableColumn
cucsFcPIoFsmCurrentFsm = _CucsFcPIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 5),
    _CucsFcPIoFsmCurrentFsm_Type()
)
cucsFcPIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmCurrentFsm.setStatus("current")
_CucsFcPIoFsmDescrData_Type = SnmpAdminString
_CucsFcPIoFsmDescrData_Object = MibTableColumn
cucsFcPIoFsmDescrData = _CucsFcPIoFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 6),
    _CucsFcPIoFsmDescrData_Type()
)
cucsFcPIoFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmDescrData.setStatus("current")
_CucsFcPIoFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsFcPIoFsmFsmStatus_Object = MibTableColumn
cucsFcPIoFsmFsmStatus = _CucsFcPIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 7),
    _CucsFcPIoFsmFsmStatus_Type()
)
cucsFcPIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmFsmStatus.setStatus("current")
_CucsFcPIoFsmProgress_Type = Gauge32
_CucsFcPIoFsmProgress_Object = MibTableColumn
cucsFcPIoFsmProgress = _CucsFcPIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 8),
    _CucsFcPIoFsmProgress_Type()
)
cucsFcPIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmProgress.setStatus("current")
_CucsFcPIoFsmRmtErrCode_Type = Gauge32
_CucsFcPIoFsmRmtErrCode_Object = MibTableColumn
cucsFcPIoFsmRmtErrCode = _CucsFcPIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 9),
    _CucsFcPIoFsmRmtErrCode_Type()
)
cucsFcPIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmRmtErrCode.setStatus("current")
_CucsFcPIoFsmRmtErrDescr_Type = SnmpAdminString
_CucsFcPIoFsmRmtErrDescr_Object = MibTableColumn
cucsFcPIoFsmRmtErrDescr = _CucsFcPIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 10),
    _CucsFcPIoFsmRmtErrDescr_Type()
)
cucsFcPIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmRmtErrDescr.setStatus("current")
_CucsFcPIoFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsFcPIoFsmRmtRslt_Object = MibTableColumn
cucsFcPIoFsmRmtRslt = _CucsFcPIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 8, 1, 11),
    _CucsFcPIoFsmRmtRslt_Type()
)
cucsFcPIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmRmtRslt.setStatus("current")
_CucsFcPIoFsmStageTable_Object = MibTable
cucsFcPIoFsmStageTable = _CucsFcPIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9)
)
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageTable.setStatus("current")
_CucsFcPIoFsmStageEntry_Object = MibTableRow
cucsFcPIoFsmStageEntry = _CucsFcPIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1)
)
cucsFcPIoFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FC-MIB", "cucsFcPIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageEntry.setStatus("current")
_CucsFcPIoFsmStageInstanceId_Type = CucsManagedObjectId
_CucsFcPIoFsmStageInstanceId_Object = MibTableColumn
cucsFcPIoFsmStageInstanceId = _CucsFcPIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 1),
    _CucsFcPIoFsmStageInstanceId_Type()
)
cucsFcPIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageInstanceId.setStatus("current")
_CucsFcPIoFsmStageDn_Type = CucsManagedObjectDn
_CucsFcPIoFsmStageDn_Object = MibTableColumn
cucsFcPIoFsmStageDn = _CucsFcPIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 2),
    _CucsFcPIoFsmStageDn_Type()
)
cucsFcPIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageDn.setStatus("current")
_CucsFcPIoFsmStageRn_Type = SnmpAdminString
_CucsFcPIoFsmStageRn_Object = MibTableColumn
cucsFcPIoFsmStageRn = _CucsFcPIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 3),
    _CucsFcPIoFsmStageRn_Type()
)
cucsFcPIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageRn.setStatus("current")
_CucsFcPIoFsmStageDescrData_Type = SnmpAdminString
_CucsFcPIoFsmStageDescrData_Object = MibTableColumn
cucsFcPIoFsmStageDescrData = _CucsFcPIoFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 4),
    _CucsFcPIoFsmStageDescrData_Type()
)
cucsFcPIoFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageDescrData.setStatus("current")
_CucsFcPIoFsmStageLastUpdateTime_Type = DateAndTime
_CucsFcPIoFsmStageLastUpdateTime_Object = MibTableColumn
cucsFcPIoFsmStageLastUpdateTime = _CucsFcPIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 5),
    _CucsFcPIoFsmStageLastUpdateTime_Type()
)
cucsFcPIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageLastUpdateTime.setStatus("current")
_CucsFcPIoFsmStageName_Type = CucsFcPIoFsmStageName
_CucsFcPIoFsmStageName_Object = MibTableColumn
cucsFcPIoFsmStageName = _CucsFcPIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 6),
    _CucsFcPIoFsmStageName_Type()
)
cucsFcPIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageName.setStatus("current")
_CucsFcPIoFsmStageOrder_Type = Gauge32
_CucsFcPIoFsmStageOrder_Object = MibTableColumn
cucsFcPIoFsmStageOrder = _CucsFcPIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 7),
    _CucsFcPIoFsmStageOrder_Type()
)
cucsFcPIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageOrder.setStatus("current")
_CucsFcPIoFsmStageRetry_Type = Gauge32
_CucsFcPIoFsmStageRetry_Object = MibTableColumn
cucsFcPIoFsmStageRetry = _CucsFcPIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 8),
    _CucsFcPIoFsmStageRetry_Type()
)
cucsFcPIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageRetry.setStatus("current")
_CucsFcPIoFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsFcPIoFsmStageStageStatus_Object = MibTableColumn
cucsFcPIoFsmStageStageStatus = _CucsFcPIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 20, 9, 1, 9),
    _CucsFcPIoFsmStageStageStatus_Type()
)
cucsFcPIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcPIoFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-FC-MIB",
    **{"cucsFcObjects": cucsFcObjects,
       "cucsFcErrStatsTable": cucsFcErrStatsTable,
       "cucsFcErrStatsEntry": cucsFcErrStatsEntry,
       "cucsFcErrStatsInstanceId": cucsFcErrStatsInstanceId,
       "cucsFcErrStatsDn": cucsFcErrStatsDn,
       "cucsFcErrStatsRn": cucsFcErrStatsRn,
       "cucsFcErrStatsCrcRx": cucsFcErrStatsCrcRx,
       "cucsFcErrStatsCrcRxDelta": cucsFcErrStatsCrcRxDelta,
       "cucsFcErrStatsCrcRxDeltaAvg": cucsFcErrStatsCrcRxDeltaAvg,
       "cucsFcErrStatsCrcRxDeltaMax": cucsFcErrStatsCrcRxDeltaMax,
       "cucsFcErrStatsCrcRxDeltaMin": cucsFcErrStatsCrcRxDeltaMin,
       "cucsFcErrStatsDiscardRx": cucsFcErrStatsDiscardRx,
       "cucsFcErrStatsDiscardRxDelta": cucsFcErrStatsDiscardRxDelta,
       "cucsFcErrStatsDiscardRxDeltaAvg": cucsFcErrStatsDiscardRxDeltaAvg,
       "cucsFcErrStatsDiscardRxDeltaMax": cucsFcErrStatsDiscardRxDeltaMax,
       "cucsFcErrStatsDiscardRxDeltaMin": cucsFcErrStatsDiscardRxDeltaMin,
       "cucsFcErrStatsDiscardTx": cucsFcErrStatsDiscardTx,
       "cucsFcErrStatsDiscardTxDelta": cucsFcErrStatsDiscardTxDelta,
       "cucsFcErrStatsDiscardTxDeltaAvg": cucsFcErrStatsDiscardTxDeltaAvg,
       "cucsFcErrStatsDiscardTxDeltaMax": cucsFcErrStatsDiscardTxDeltaMax,
       "cucsFcErrStatsDiscardTxDeltaMin": cucsFcErrStatsDiscardTxDeltaMin,
       "cucsFcErrStatsIntervals": cucsFcErrStatsIntervals,
       "cucsFcErrStatsLinkFailures": cucsFcErrStatsLinkFailures,
       "cucsFcErrStatsLinkFailuresDelta": cucsFcErrStatsLinkFailuresDelta,
       "cucsFcErrStatsLinkFailuresDeltaAvg": cucsFcErrStatsLinkFailuresDeltaAvg,
       "cucsFcErrStatsLinkFailuresDeltaMax": cucsFcErrStatsLinkFailuresDeltaMax,
       "cucsFcErrStatsLinkFailuresDeltaMin": cucsFcErrStatsLinkFailuresDeltaMin,
       "cucsFcErrStatsRx": cucsFcErrStatsRx,
       "cucsFcErrStatsRxDelta": cucsFcErrStatsRxDelta,
       "cucsFcErrStatsRxDeltaAvg": cucsFcErrStatsRxDeltaAvg,
       "cucsFcErrStatsRxDeltaMax": cucsFcErrStatsRxDeltaMax,
       "cucsFcErrStatsRxDeltaMin": cucsFcErrStatsRxDeltaMin,
       "cucsFcErrStatsSignalLosses": cucsFcErrStatsSignalLosses,
       "cucsFcErrStatsSignalLossesDelta": cucsFcErrStatsSignalLossesDelta,
       "cucsFcErrStatsSignalLossesDeltaAvg": cucsFcErrStatsSignalLossesDeltaAvg,
       "cucsFcErrStatsSignalLossesDeltaMax": cucsFcErrStatsSignalLossesDeltaMax,
       "cucsFcErrStatsSignalLossesDeltaMin": cucsFcErrStatsSignalLossesDeltaMin,
       "cucsFcErrStatsSuspect": cucsFcErrStatsSuspect,
       "cucsFcErrStatsSyncLosses": cucsFcErrStatsSyncLosses,
       "cucsFcErrStatsSyncLossesDelta": cucsFcErrStatsSyncLossesDelta,
       "cucsFcErrStatsSyncLossesDeltaAvg": cucsFcErrStatsSyncLossesDeltaAvg,
       "cucsFcErrStatsSyncLossesDeltaMax": cucsFcErrStatsSyncLossesDeltaMax,
       "cucsFcErrStatsSyncLossesDeltaMin": cucsFcErrStatsSyncLossesDeltaMin,
       "cucsFcErrStatsThresholded": cucsFcErrStatsThresholded,
       "cucsFcErrStatsTimeCollected": cucsFcErrStatsTimeCollected,
       "cucsFcErrStatsTooLongRx": cucsFcErrStatsTooLongRx,
       "cucsFcErrStatsTooLongRxDelta": cucsFcErrStatsTooLongRxDelta,
       "cucsFcErrStatsTooLongRxDeltaAvg": cucsFcErrStatsTooLongRxDeltaAvg,
       "cucsFcErrStatsTooLongRxDeltaMax": cucsFcErrStatsTooLongRxDeltaMax,
       "cucsFcErrStatsTooLongRxDeltaMin": cucsFcErrStatsTooLongRxDeltaMin,
       "cucsFcErrStatsTooShortRx": cucsFcErrStatsTooShortRx,
       "cucsFcErrStatsTooShortRxDelta": cucsFcErrStatsTooShortRxDelta,
       "cucsFcErrStatsTooShortRxDeltaAvg": cucsFcErrStatsTooShortRxDeltaAvg,
       "cucsFcErrStatsTooShortRxDeltaMax": cucsFcErrStatsTooShortRxDeltaMax,
       "cucsFcErrStatsTooShortRxDeltaMin": cucsFcErrStatsTooShortRxDeltaMin,
       "cucsFcErrStatsTx": cucsFcErrStatsTx,
       "cucsFcErrStatsTxDelta": cucsFcErrStatsTxDelta,
       "cucsFcErrStatsTxDeltaAvg": cucsFcErrStatsTxDeltaAvg,
       "cucsFcErrStatsTxDeltaMax": cucsFcErrStatsTxDeltaMax,
       "cucsFcErrStatsTxDeltaMin": cucsFcErrStatsTxDeltaMin,
       "cucsFcErrStatsUpdate": cucsFcErrStatsUpdate,
       "cucsFcErrStatsHistTable": cucsFcErrStatsHistTable,
       "cucsFcErrStatsHistEntry": cucsFcErrStatsHistEntry,
       "cucsFcErrStatsHistInstanceId": cucsFcErrStatsHistInstanceId,
       "cucsFcErrStatsHistDn": cucsFcErrStatsHistDn,
       "cucsFcErrStatsHistRn": cucsFcErrStatsHistRn,
       "cucsFcErrStatsHistCrcRx": cucsFcErrStatsHistCrcRx,
       "cucsFcErrStatsHistCrcRxDelta": cucsFcErrStatsHistCrcRxDelta,
       "cucsFcErrStatsHistCrcRxDeltaAvg": cucsFcErrStatsHistCrcRxDeltaAvg,
       "cucsFcErrStatsHistCrcRxDeltaMax": cucsFcErrStatsHistCrcRxDeltaMax,
       "cucsFcErrStatsHistCrcRxDeltaMin": cucsFcErrStatsHistCrcRxDeltaMin,
       "cucsFcErrStatsHistDiscardRx": cucsFcErrStatsHistDiscardRx,
       "cucsFcErrStatsHistDiscardRxDelta": cucsFcErrStatsHistDiscardRxDelta,
       "cucsFcErrStatsHistDiscardRxDeltaAvg": cucsFcErrStatsHistDiscardRxDeltaAvg,
       "cucsFcErrStatsHistDiscardRxDeltaMax": cucsFcErrStatsHistDiscardRxDeltaMax,
       "cucsFcErrStatsHistDiscardRxDeltaMin": cucsFcErrStatsHistDiscardRxDeltaMin,
       "cucsFcErrStatsHistDiscardTx": cucsFcErrStatsHistDiscardTx,
       "cucsFcErrStatsHistDiscardTxDelta": cucsFcErrStatsHistDiscardTxDelta,
       "cucsFcErrStatsHistDiscardTxDeltaAvg": cucsFcErrStatsHistDiscardTxDeltaAvg,
       "cucsFcErrStatsHistDiscardTxDeltaMax": cucsFcErrStatsHistDiscardTxDeltaMax,
       "cucsFcErrStatsHistDiscardTxDeltaMin": cucsFcErrStatsHistDiscardTxDeltaMin,
       "cucsFcErrStatsHistId": cucsFcErrStatsHistId,
       "cucsFcErrStatsHistLinkFailures": cucsFcErrStatsHistLinkFailures,
       "cucsFcErrStatsHistLinkFailuresDelta": cucsFcErrStatsHistLinkFailuresDelta,
       "cucsFcErrStatsHistLinkFailuresDeltaAvg": cucsFcErrStatsHistLinkFailuresDeltaAvg,
       "cucsFcErrStatsHistLinkFailuresDeltaMax": cucsFcErrStatsHistLinkFailuresDeltaMax,
       "cucsFcErrStatsHistLinkFailuresDeltaMin": cucsFcErrStatsHistLinkFailuresDeltaMin,
       "cucsFcErrStatsHistMostRecent": cucsFcErrStatsHistMostRecent,
       "cucsFcErrStatsHistRx": cucsFcErrStatsHistRx,
       "cucsFcErrStatsHistRxDelta": cucsFcErrStatsHistRxDelta,
       "cucsFcErrStatsHistRxDeltaAvg": cucsFcErrStatsHistRxDeltaAvg,
       "cucsFcErrStatsHistRxDeltaMax": cucsFcErrStatsHistRxDeltaMax,
       "cucsFcErrStatsHistRxDeltaMin": cucsFcErrStatsHistRxDeltaMin,
       "cucsFcErrStatsHistSignalLosses": cucsFcErrStatsHistSignalLosses,
       "cucsFcErrStatsHistSignalLossesDelta": cucsFcErrStatsHistSignalLossesDelta,
       "cucsFcErrStatsHistSignalLossesDeltaAvg": cucsFcErrStatsHistSignalLossesDeltaAvg,
       "cucsFcErrStatsHistSignalLossesDeltaMax": cucsFcErrStatsHistSignalLossesDeltaMax,
       "cucsFcErrStatsHistSignalLossesDeltaMin": cucsFcErrStatsHistSignalLossesDeltaMin,
       "cucsFcErrStatsHistSuspect": cucsFcErrStatsHistSuspect,
       "cucsFcErrStatsHistSyncLosses": cucsFcErrStatsHistSyncLosses,
       "cucsFcErrStatsHistSyncLossesDelta": cucsFcErrStatsHistSyncLossesDelta,
       "cucsFcErrStatsHistSyncLossesDeltaAvg": cucsFcErrStatsHistSyncLossesDeltaAvg,
       "cucsFcErrStatsHistSyncLossesDeltaMax": cucsFcErrStatsHistSyncLossesDeltaMax,
       "cucsFcErrStatsHistSyncLossesDeltaMin": cucsFcErrStatsHistSyncLossesDeltaMin,
       "cucsFcErrStatsHistThresholded": cucsFcErrStatsHistThresholded,
       "cucsFcErrStatsHistTimeCollected": cucsFcErrStatsHistTimeCollected,
       "cucsFcErrStatsHistTooLongRx": cucsFcErrStatsHistTooLongRx,
       "cucsFcErrStatsHistTooLongRxDelta": cucsFcErrStatsHistTooLongRxDelta,
       "cucsFcErrStatsHistTooLongRxDeltaAvg": cucsFcErrStatsHistTooLongRxDeltaAvg,
       "cucsFcErrStatsHistTooLongRxDeltaMax": cucsFcErrStatsHistTooLongRxDeltaMax,
       "cucsFcErrStatsHistTooLongRxDeltaMin": cucsFcErrStatsHistTooLongRxDeltaMin,
       "cucsFcErrStatsHistTooShortRx": cucsFcErrStatsHistTooShortRx,
       "cucsFcErrStatsHistTooShortRxDelta": cucsFcErrStatsHistTooShortRxDelta,
       "cucsFcErrStatsHistTooShortRxDeltaAvg": cucsFcErrStatsHistTooShortRxDeltaAvg,
       "cucsFcErrStatsHistTooShortRxDeltaMax": cucsFcErrStatsHistTooShortRxDeltaMax,
       "cucsFcErrStatsHistTooShortRxDeltaMin": cucsFcErrStatsHistTooShortRxDeltaMin,
       "cucsFcErrStatsHistTx": cucsFcErrStatsHistTx,
       "cucsFcErrStatsHistTxDelta": cucsFcErrStatsHistTxDelta,
       "cucsFcErrStatsHistTxDeltaAvg": cucsFcErrStatsHistTxDeltaAvg,
       "cucsFcErrStatsHistTxDeltaMax": cucsFcErrStatsHistTxDeltaMax,
       "cucsFcErrStatsHistTxDeltaMin": cucsFcErrStatsHistTxDeltaMin,
       "cucsFcNicIfConfigTable": cucsFcNicIfConfigTable,
       "cucsFcNicIfConfigEntry": cucsFcNicIfConfigEntry,
       "cucsFcNicIfConfigInstanceId": cucsFcNicIfConfigInstanceId,
       "cucsFcNicIfConfigDn": cucsFcNicIfConfigDn,
       "cucsFcNicIfConfigRn": cucsFcNicIfConfigRn,
       "cucsFcPIoTable": cucsFcPIoTable,
       "cucsFcPIoEntry": cucsFcPIoEntry,
       "cucsFcPIoInstanceId": cucsFcPIoInstanceId,
       "cucsFcPIoDn": cucsFcPIoDn,
       "cucsFcPIoRn": cucsFcPIoRn,
       "cucsFcPIoAdminState": cucsFcPIoAdminState,
       "cucsFcPIoChassisId": cucsFcPIoChassisId,
       "cucsFcPIoEncap": cucsFcPIoEncap,
       "cucsFcPIoEpDn": cucsFcPIoEpDn,
       "cucsFcPIoFltAggr": cucsFcPIoFltAggr,
       "cucsFcPIoIfRole": cucsFcPIoIfRole,
       "cucsFcPIoIfType": cucsFcPIoIfType,
       "cucsFcPIoLocale": cucsFcPIoLocale,
       "cucsFcPIoMode": cucsFcPIoMode,
       "cucsFcPIoModel": cucsFcPIoModel,
       "cucsFcPIoName": cucsFcPIoName,
       "cucsFcPIoOperSpeed": cucsFcPIoOperSpeed,
       "cucsFcPIoOperState": cucsFcPIoOperState,
       "cucsFcPIoPeerDn": cucsFcPIoPeerDn,
       "cucsFcPIoPeerPortId": cucsFcPIoPeerPortId,
       "cucsFcPIoPeerSlotId": cucsFcPIoPeerSlotId,
       "cucsFcPIoPortId": cucsFcPIoPortId,
       "cucsFcPIoRevision": cucsFcPIoRevision,
       "cucsFcPIoSerial": cucsFcPIoSerial,
       "cucsFcPIoSlotId": cucsFcPIoSlotId,
       "cucsFcPIoStateQual": cucsFcPIoStateQual,
       "cucsFcPIoSwitchId": cucsFcPIoSwitchId,
       "cucsFcPIoTransport": cucsFcPIoTransport,
       "cucsFcPIoTs": cucsFcPIoTs,
       "cucsFcPIoType": cucsFcPIoType,
       "cucsFcPIoUsrLbl": cucsFcPIoUsrLbl,
       "cucsFcPIoVendor": cucsFcPIoVendor,
       "cucsFcPIoWwn": cucsFcPIoWwn,
       "cucsFcPIoFsmDescr": cucsFcPIoFsmDescr,
       "cucsFcPIoFsmPrev": cucsFcPIoFsmPrev,
       "cucsFcPIoFsmProgr": cucsFcPIoFsmProgr,
       "cucsFcPIoFsmRmtInvErrCode": cucsFcPIoFsmRmtInvErrCode,
       "cucsFcPIoFsmRmtInvErrDescr": cucsFcPIoFsmRmtInvErrDescr,
       "cucsFcPIoFsmRmtInvRslt": cucsFcPIoFsmRmtInvRslt,
       "cucsFcPIoFsmStageDescr": cucsFcPIoFsmStageDescr,
       "cucsFcPIoFsmStamp": cucsFcPIoFsmStamp,
       "cucsFcPIoFsmStatus": cucsFcPIoFsmStatus,
       "cucsFcPIoFsmTry": cucsFcPIoFsmTry,
       "cucsFcPIoLicGP": cucsFcPIoLicGP,
       "cucsFcPIoLicState": cucsFcPIoLicState,
       "cucsFcPIoXcvrType": cucsFcPIoXcvrType,
       "cucsFcPIoPeerChassisId": cucsFcPIoPeerChassisId,
       "cucsFcPIoAdminTransport": cucsFcPIoAdminTransport,
       "cucsFcPIoLc": cucsFcPIoLc,
       "cucsFcPIoUnifiedPort": cucsFcPIoUnifiedPort,
       "cucsFcPIoMaxSpeed": cucsFcPIoMaxSpeed,
       "cucsFcPIoIsPortChannelMember": cucsFcPIoIsPortChannelMember,
       "cucsFcPIoAggrPortId": cucsFcPIoAggrPortId,
       "cucsFcPIoPeerAggrPortId": cucsFcPIoPeerAggrPortId,
       "cucsFcStatsTable": cucsFcStatsTable,
       "cucsFcStatsEntry": cucsFcStatsEntry,
       "cucsFcStatsInstanceId": cucsFcStatsInstanceId,
       "cucsFcStatsDn": cucsFcStatsDn,
       "cucsFcStatsRn": cucsFcStatsRn,
       "cucsFcStatsBytesRx": cucsFcStatsBytesRx,
       "cucsFcStatsBytesRxDelta": cucsFcStatsBytesRxDelta,
       "cucsFcStatsBytesRxDeltaAvg": cucsFcStatsBytesRxDeltaAvg,
       "cucsFcStatsBytesRxDeltaMax": cucsFcStatsBytesRxDeltaMax,
       "cucsFcStatsBytesRxDeltaMin": cucsFcStatsBytesRxDeltaMin,
       "cucsFcStatsBytesTx": cucsFcStatsBytesTx,
       "cucsFcStatsBytesTxDelta": cucsFcStatsBytesTxDelta,
       "cucsFcStatsBytesTxDeltaAvg": cucsFcStatsBytesTxDeltaAvg,
       "cucsFcStatsBytesTxDeltaMax": cucsFcStatsBytesTxDeltaMax,
       "cucsFcStatsBytesTxDeltaMin": cucsFcStatsBytesTxDeltaMin,
       "cucsFcStatsIntervals": cucsFcStatsIntervals,
       "cucsFcStatsPacketsRx": cucsFcStatsPacketsRx,
       "cucsFcStatsPacketsRxDelta": cucsFcStatsPacketsRxDelta,
       "cucsFcStatsPacketsRxDeltaAvg": cucsFcStatsPacketsRxDeltaAvg,
       "cucsFcStatsPacketsRxDeltaMax": cucsFcStatsPacketsRxDeltaMax,
       "cucsFcStatsPacketsRxDeltaMin": cucsFcStatsPacketsRxDeltaMin,
       "cucsFcStatsPacketsTx": cucsFcStatsPacketsTx,
       "cucsFcStatsPacketsTxDelta": cucsFcStatsPacketsTxDelta,
       "cucsFcStatsPacketsTxDeltaAvg": cucsFcStatsPacketsTxDeltaAvg,
       "cucsFcStatsPacketsTxDeltaMax": cucsFcStatsPacketsTxDeltaMax,
       "cucsFcStatsPacketsTxDeltaMin": cucsFcStatsPacketsTxDeltaMin,
       "cucsFcStatsSuspect": cucsFcStatsSuspect,
       "cucsFcStatsThresholded": cucsFcStatsThresholded,
       "cucsFcStatsTimeCollected": cucsFcStatsTimeCollected,
       "cucsFcStatsUpdate": cucsFcStatsUpdate,
       "cucsFcStatsHistTable": cucsFcStatsHistTable,
       "cucsFcStatsHistEntry": cucsFcStatsHistEntry,
       "cucsFcStatsHistInstanceId": cucsFcStatsHistInstanceId,
       "cucsFcStatsHistDn": cucsFcStatsHistDn,
       "cucsFcStatsHistRn": cucsFcStatsHistRn,
       "cucsFcStatsHistBytesRx": cucsFcStatsHistBytesRx,
       "cucsFcStatsHistBytesRxDelta": cucsFcStatsHistBytesRxDelta,
       "cucsFcStatsHistBytesRxDeltaAvg": cucsFcStatsHistBytesRxDeltaAvg,
       "cucsFcStatsHistBytesRxDeltaMax": cucsFcStatsHistBytesRxDeltaMax,
       "cucsFcStatsHistBytesRxDeltaMin": cucsFcStatsHistBytesRxDeltaMin,
       "cucsFcStatsHistBytesTx": cucsFcStatsHistBytesTx,
       "cucsFcStatsHistBytesTxDelta": cucsFcStatsHistBytesTxDelta,
       "cucsFcStatsHistBytesTxDeltaAvg": cucsFcStatsHistBytesTxDeltaAvg,
       "cucsFcStatsHistBytesTxDeltaMax": cucsFcStatsHistBytesTxDeltaMax,
       "cucsFcStatsHistBytesTxDeltaMin": cucsFcStatsHistBytesTxDeltaMin,
       "cucsFcStatsHistId": cucsFcStatsHistId,
       "cucsFcStatsHistMostRecent": cucsFcStatsHistMostRecent,
       "cucsFcStatsHistPacketsRx": cucsFcStatsHistPacketsRx,
       "cucsFcStatsHistPacketsRxDelta": cucsFcStatsHistPacketsRxDelta,
       "cucsFcStatsHistPacketsRxDeltaAvg": cucsFcStatsHistPacketsRxDeltaAvg,
       "cucsFcStatsHistPacketsRxDeltaMax": cucsFcStatsHistPacketsRxDeltaMax,
       "cucsFcStatsHistPacketsRxDeltaMin": cucsFcStatsHistPacketsRxDeltaMin,
       "cucsFcStatsHistPacketsTx": cucsFcStatsHistPacketsTx,
       "cucsFcStatsHistPacketsTxDelta": cucsFcStatsHistPacketsTxDelta,
       "cucsFcStatsHistPacketsTxDeltaAvg": cucsFcStatsHistPacketsTxDeltaAvg,
       "cucsFcStatsHistPacketsTxDeltaMax": cucsFcStatsHistPacketsTxDeltaMax,
       "cucsFcStatsHistPacketsTxDeltaMin": cucsFcStatsHistPacketsTxDeltaMin,
       "cucsFcStatsHistSuspect": cucsFcStatsHistSuspect,
       "cucsFcStatsHistThresholded": cucsFcStatsHistThresholded,
       "cucsFcStatsHistTimeCollected": cucsFcStatsHistTimeCollected,
       "cucsFcSwIfConfigTable": cucsFcSwIfConfigTable,
       "cucsFcSwIfConfigEntry": cucsFcSwIfConfigEntry,
       "cucsFcSwIfConfigInstanceId": cucsFcSwIfConfigInstanceId,
       "cucsFcSwIfConfigDn": cucsFcSwIfConfigDn,
       "cucsFcSwIfConfigRn": cucsFcSwIfConfigRn,
       "cucsFcPIoFsmTable": cucsFcPIoFsmTable,
       "cucsFcPIoFsmEntry": cucsFcPIoFsmEntry,
       "cucsFcPIoFsmInstanceId": cucsFcPIoFsmInstanceId,
       "cucsFcPIoFsmDn": cucsFcPIoFsmDn,
       "cucsFcPIoFsmRn": cucsFcPIoFsmRn,
       "cucsFcPIoFsmCompletionTime": cucsFcPIoFsmCompletionTime,
       "cucsFcPIoFsmCurrentFsm": cucsFcPIoFsmCurrentFsm,
       "cucsFcPIoFsmDescrData": cucsFcPIoFsmDescrData,
       "cucsFcPIoFsmFsmStatus": cucsFcPIoFsmFsmStatus,
       "cucsFcPIoFsmProgress": cucsFcPIoFsmProgress,
       "cucsFcPIoFsmRmtErrCode": cucsFcPIoFsmRmtErrCode,
       "cucsFcPIoFsmRmtErrDescr": cucsFcPIoFsmRmtErrDescr,
       "cucsFcPIoFsmRmtRslt": cucsFcPIoFsmRmtRslt,
       "cucsFcPIoFsmStageTable": cucsFcPIoFsmStageTable,
       "cucsFcPIoFsmStageEntry": cucsFcPIoFsmStageEntry,
       "cucsFcPIoFsmStageInstanceId": cucsFcPIoFsmStageInstanceId,
       "cucsFcPIoFsmStageDn": cucsFcPIoFsmStageDn,
       "cucsFcPIoFsmStageRn": cucsFcPIoFsmStageRn,
       "cucsFcPIoFsmStageDescrData": cucsFcPIoFsmStageDescrData,
       "cucsFcPIoFsmStageLastUpdateTime": cucsFcPIoFsmStageLastUpdateTime,
       "cucsFcPIoFsmStageName": cucsFcPIoFsmStageName,
       "cucsFcPIoFsmStageOrder": cucsFcPIoFsmStageOrder,
       "cucsFcPIoFsmStageRetry": cucsFcPIoFsmStageRetry,
       "cucsFcPIoFsmStageStageStatus": cucsFcPIoFsmStageStageStatus}
)
