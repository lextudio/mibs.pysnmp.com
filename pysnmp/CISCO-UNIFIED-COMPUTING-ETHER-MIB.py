# SNMP MIB module (CISCO-UNIFIED-COMPUTING-ETHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-ETHER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:22 2024
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
 CucsEquipmentChassisConfigState,
 CucsEquipmentXcvrType,
 CucsEtherCIoEpIfType,
 CucsEtherCloudType,
 CucsEtherErrStatsHistThresholded,
 CucsEtherErrStatsThresholded,
 CucsEtherExternalEpAdminState,
 CucsEtherExternalEpLocale,
 CucsEtherExternalPcAdminState,
 CucsEtherExternalPcLocale,
 CucsEtherFcoeInterfaceStatsHistThresholded,
 CucsEtherFcoeInterfaceStatsThresholded,
 CucsEtherIntFIoEpType,
 CucsEtherInternalPcLocale,
 CucsEtherLossStatsHistThresholded,
 CucsEtherLossStatsThresholded,
 CucsEtherNiErrStatsHistThresholded,
 CucsEtherNiErrStatsThresholded,
 CucsEtherPIoEpIfType,
 CucsEtherPIoFsmCurrentFsm,
 CucsEtherPIoFsmStageName,
 CucsEtherPauseStatsHistThresholded,
 CucsEtherPauseStatsThresholded,
 CucsEtherRxStatsHistThresholded,
 CucsEtherRxStatsThresholded,
 CucsEtherSatelliteConnectionDisc,
 CucsEtherServerIntFIoAdminState,
 CucsEtherServerIntFIoFsmCurrentFsm,
 CucsEtherServerIntFIoFsmStageName,
 CucsEtherServerIntFIoFsmTaskItem,
 CucsEtherServerIntFIoIfRole,
 CucsEtherServerIntFIoLocale,
 CucsEtherServerIntFIoPcEpIfRole,
 CucsEtherServerIntFIoPcEpPortId,
 CucsEtherServerIntFIoPcIfRole,
 CucsEtherServerIntFIoPcPortId,
 CucsEtherServerIntFIoPcTransport,
 CucsEtherServerIntFIoPcType,
 CucsEtherServerIntFIoTransport,
 CucsEtherServerIntFIoType,
 CucsEtherSwitchIntFIoAck,
 CucsEtherSwitchIntFIoIfRole,
 CucsEtherSwitchIntFIoLocale,
 CucsEtherSwitchIntFIoPcEpIfRole,
 CucsEtherSwitchIntFIoPcEpPortId,
 CucsEtherSwitchIntFIoPcIfRole,
 CucsEtherSwitchIntFIoPcMulticastHwHash,
 CucsEtherSwitchIntFIoPcPortId,
 CucsEtherSwitchIntFIoPcTransport,
 CucsEtherSwitchIntFIoPcType,
 CucsEtherSwitchIntFIoTransport,
 CucsEtherSwitchIntFIoType,
 CucsEtherTxStatsHistThresholded,
 CucsEtherTxStatsThresholded,
 CucsFabricAdminState,
 CucsFabricMembershipStatus,
 CucsFsmCompletion,
 CucsFsmFlags,
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
 CucsPortEthSpeed,
 CucsPortMode) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsEquipmentChassisConfigState",
    "CucsEquipmentXcvrType",
    "CucsEtherCIoEpIfType",
    "CucsEtherCloudType",
    "CucsEtherErrStatsHistThresholded",
    "CucsEtherErrStatsThresholded",
    "CucsEtherExternalEpAdminState",
    "CucsEtherExternalEpLocale",
    "CucsEtherExternalPcAdminState",
    "CucsEtherExternalPcLocale",
    "CucsEtherFcoeInterfaceStatsHistThresholded",
    "CucsEtherFcoeInterfaceStatsThresholded",
    "CucsEtherIntFIoEpType",
    "CucsEtherInternalPcLocale",
    "CucsEtherLossStatsHistThresholded",
    "CucsEtherLossStatsThresholded",
    "CucsEtherNiErrStatsHistThresholded",
    "CucsEtherNiErrStatsThresholded",
    "CucsEtherPIoEpIfType",
    "CucsEtherPIoFsmCurrentFsm",
    "CucsEtherPIoFsmStageName",
    "CucsEtherPauseStatsHistThresholded",
    "CucsEtherPauseStatsThresholded",
    "CucsEtherRxStatsHistThresholded",
    "CucsEtherRxStatsThresholded",
    "CucsEtherSatelliteConnectionDisc",
    "CucsEtherServerIntFIoAdminState",
    "CucsEtherServerIntFIoFsmCurrentFsm",
    "CucsEtherServerIntFIoFsmStageName",
    "CucsEtherServerIntFIoFsmTaskItem",
    "CucsEtherServerIntFIoIfRole",
    "CucsEtherServerIntFIoLocale",
    "CucsEtherServerIntFIoPcEpIfRole",
    "CucsEtherServerIntFIoPcEpPortId",
    "CucsEtherServerIntFIoPcIfRole",
    "CucsEtherServerIntFIoPcPortId",
    "CucsEtherServerIntFIoPcTransport",
    "CucsEtherServerIntFIoPcType",
    "CucsEtherServerIntFIoTransport",
    "CucsEtherServerIntFIoType",
    "CucsEtherSwitchIntFIoAck",
    "CucsEtherSwitchIntFIoIfRole",
    "CucsEtherSwitchIntFIoLocale",
    "CucsEtherSwitchIntFIoPcEpIfRole",
    "CucsEtherSwitchIntFIoPcEpPortId",
    "CucsEtherSwitchIntFIoPcIfRole",
    "CucsEtherSwitchIntFIoPcMulticastHwHash",
    "CucsEtherSwitchIntFIoPcPortId",
    "CucsEtherSwitchIntFIoPcTransport",
    "CucsEtherSwitchIntFIoPcType",
    "CucsEtherSwitchIntFIoTransport",
    "CucsEtherSwitchIntFIoType",
    "CucsEtherTxStatsHistThresholded",
    "CucsEtherTxStatsThresholded",
    "CucsFabricAdminState",
    "CucsFabricMembershipStatus",
    "CucsFsmCompletion",
    "CucsFsmFlags",
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
    "CucsPortEthSpeed",
    "CucsPortMode")

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

cucsEtherObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsEtherErrStatsTable_Object = MibTable
cucsEtherErrStatsTable = _CucsEtherErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cucsEtherErrStatsTable.setStatus("current")
_CucsEtherErrStatsEntry_Object = MibTableRow
cucsEtherErrStatsEntry = _CucsEtherErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1)
)
cucsEtherErrStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherErrStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherErrStatsEntry.setStatus("current")
_CucsEtherErrStatsInstanceId_Type = CucsManagedObjectId
_CucsEtherErrStatsInstanceId_Object = MibTableColumn
cucsEtherErrStatsInstanceId = _CucsEtherErrStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 1),
    _CucsEtherErrStatsInstanceId_Type()
)
cucsEtherErrStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherErrStatsInstanceId.setStatus("current")
_CucsEtherErrStatsDn_Type = CucsManagedObjectDn
_CucsEtherErrStatsDn_Object = MibTableColumn
cucsEtherErrStatsDn = _CucsEtherErrStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 2),
    _CucsEtherErrStatsDn_Type()
)
cucsEtherErrStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsDn.setStatus("current")
_CucsEtherErrStatsRn_Type = SnmpAdminString
_CucsEtherErrStatsRn_Object = MibTableColumn
cucsEtherErrStatsRn = _CucsEtherErrStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 3),
    _CucsEtherErrStatsRn_Type()
)
cucsEtherErrStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsRn.setStatus("current")
_CucsEtherErrStatsAlign_Type = Unsigned64
_CucsEtherErrStatsAlign_Object = MibTableColumn
cucsEtherErrStatsAlign = _CucsEtherErrStatsAlign_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 4),
    _CucsEtherErrStatsAlign_Type()
)
cucsEtherErrStatsAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsAlign.setStatus("current")
_CucsEtherErrStatsAlignDelta_Type = Counter64
_CucsEtherErrStatsAlignDelta_Object = MibTableColumn
cucsEtherErrStatsAlignDelta = _CucsEtherErrStatsAlignDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 5),
    _CucsEtherErrStatsAlignDelta_Type()
)
cucsEtherErrStatsAlignDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsAlignDelta.setStatus("current")
_CucsEtherErrStatsAlignDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsAlignDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsAlignDeltaAvg = _CucsEtherErrStatsAlignDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 6),
    _CucsEtherErrStatsAlignDeltaAvg_Type()
)
cucsEtherErrStatsAlignDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsAlignDeltaAvg.setStatus("current")
_CucsEtherErrStatsAlignDeltaMax_Type = Unsigned64
_CucsEtherErrStatsAlignDeltaMax_Object = MibTableColumn
cucsEtherErrStatsAlignDeltaMax = _CucsEtherErrStatsAlignDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 7),
    _CucsEtherErrStatsAlignDeltaMax_Type()
)
cucsEtherErrStatsAlignDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsAlignDeltaMax.setStatus("current")
_CucsEtherErrStatsAlignDeltaMin_Type = Unsigned64
_CucsEtherErrStatsAlignDeltaMin_Object = MibTableColumn
cucsEtherErrStatsAlignDeltaMin = _CucsEtherErrStatsAlignDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 8),
    _CucsEtherErrStatsAlignDeltaMin_Type()
)
cucsEtherErrStatsAlignDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsAlignDeltaMin.setStatus("current")
_CucsEtherErrStatsDeferredTx_Type = Unsigned64
_CucsEtherErrStatsDeferredTx_Object = MibTableColumn
cucsEtherErrStatsDeferredTx = _CucsEtherErrStatsDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 9),
    _CucsEtherErrStatsDeferredTx_Type()
)
cucsEtherErrStatsDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsDeferredTx.setStatus("current")
_CucsEtherErrStatsDeferredTxDelta_Type = Counter64
_CucsEtherErrStatsDeferredTxDelta_Object = MibTableColumn
cucsEtherErrStatsDeferredTxDelta = _CucsEtherErrStatsDeferredTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 10),
    _CucsEtherErrStatsDeferredTxDelta_Type()
)
cucsEtherErrStatsDeferredTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsDeferredTxDelta.setStatus("current")
_CucsEtherErrStatsDeferredTxDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsDeferredTxDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsDeferredTxDeltaAvg = _CucsEtherErrStatsDeferredTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 11),
    _CucsEtherErrStatsDeferredTxDeltaAvg_Type()
)
cucsEtherErrStatsDeferredTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsDeferredTxDeltaAvg.setStatus("current")
_CucsEtherErrStatsDeferredTxDeltaMax_Type = Unsigned64
_CucsEtherErrStatsDeferredTxDeltaMax_Object = MibTableColumn
cucsEtherErrStatsDeferredTxDeltaMax = _CucsEtherErrStatsDeferredTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 12),
    _CucsEtherErrStatsDeferredTxDeltaMax_Type()
)
cucsEtherErrStatsDeferredTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsDeferredTxDeltaMax.setStatus("current")
_CucsEtherErrStatsDeferredTxDeltaMin_Type = Unsigned64
_CucsEtherErrStatsDeferredTxDeltaMin_Object = MibTableColumn
cucsEtherErrStatsDeferredTxDeltaMin = _CucsEtherErrStatsDeferredTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 13),
    _CucsEtherErrStatsDeferredTxDeltaMin_Type()
)
cucsEtherErrStatsDeferredTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsDeferredTxDeltaMin.setStatus("current")
_CucsEtherErrStatsFcs_Type = Unsigned64
_CucsEtherErrStatsFcs_Object = MibTableColumn
cucsEtherErrStatsFcs = _CucsEtherErrStatsFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 14),
    _CucsEtherErrStatsFcs_Type()
)
cucsEtherErrStatsFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsFcs.setStatus("current")
_CucsEtherErrStatsFcsDelta_Type = Counter64
_CucsEtherErrStatsFcsDelta_Object = MibTableColumn
cucsEtherErrStatsFcsDelta = _CucsEtherErrStatsFcsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 15),
    _CucsEtherErrStatsFcsDelta_Type()
)
cucsEtherErrStatsFcsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsFcsDelta.setStatus("current")
_CucsEtherErrStatsFcsDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsFcsDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsFcsDeltaAvg = _CucsEtherErrStatsFcsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 16),
    _CucsEtherErrStatsFcsDeltaAvg_Type()
)
cucsEtherErrStatsFcsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsFcsDeltaAvg.setStatus("current")
_CucsEtherErrStatsFcsDeltaMax_Type = Unsigned64
_CucsEtherErrStatsFcsDeltaMax_Object = MibTableColumn
cucsEtherErrStatsFcsDeltaMax = _CucsEtherErrStatsFcsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 17),
    _CucsEtherErrStatsFcsDeltaMax_Type()
)
cucsEtherErrStatsFcsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsFcsDeltaMax.setStatus("current")
_CucsEtherErrStatsFcsDeltaMin_Type = Unsigned64
_CucsEtherErrStatsFcsDeltaMin_Object = MibTableColumn
cucsEtherErrStatsFcsDeltaMin = _CucsEtherErrStatsFcsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 18),
    _CucsEtherErrStatsFcsDeltaMin_Type()
)
cucsEtherErrStatsFcsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsFcsDeltaMin.setStatus("current")
_CucsEtherErrStatsIntMacRx_Type = Unsigned64
_CucsEtherErrStatsIntMacRx_Object = MibTableColumn
cucsEtherErrStatsIntMacRx = _CucsEtherErrStatsIntMacRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 19),
    _CucsEtherErrStatsIntMacRx_Type()
)
cucsEtherErrStatsIntMacRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacRx.setStatus("current")
_CucsEtherErrStatsIntMacRxDelta_Type = Counter64
_CucsEtherErrStatsIntMacRxDelta_Object = MibTableColumn
cucsEtherErrStatsIntMacRxDelta = _CucsEtherErrStatsIntMacRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 20),
    _CucsEtherErrStatsIntMacRxDelta_Type()
)
cucsEtherErrStatsIntMacRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacRxDelta.setStatus("current")
_CucsEtherErrStatsIntMacRxDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsIntMacRxDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsIntMacRxDeltaAvg = _CucsEtherErrStatsIntMacRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 21),
    _CucsEtherErrStatsIntMacRxDeltaAvg_Type()
)
cucsEtherErrStatsIntMacRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacRxDeltaAvg.setStatus("current")
_CucsEtherErrStatsIntMacRxDeltaMax_Type = Unsigned64
_CucsEtherErrStatsIntMacRxDeltaMax_Object = MibTableColumn
cucsEtherErrStatsIntMacRxDeltaMax = _CucsEtherErrStatsIntMacRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 22),
    _CucsEtherErrStatsIntMacRxDeltaMax_Type()
)
cucsEtherErrStatsIntMacRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacRxDeltaMax.setStatus("current")
_CucsEtherErrStatsIntMacRxDeltaMin_Type = Unsigned64
_CucsEtherErrStatsIntMacRxDeltaMin_Object = MibTableColumn
cucsEtherErrStatsIntMacRxDeltaMin = _CucsEtherErrStatsIntMacRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 23),
    _CucsEtherErrStatsIntMacRxDeltaMin_Type()
)
cucsEtherErrStatsIntMacRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacRxDeltaMin.setStatus("current")
_CucsEtherErrStatsIntMacTx_Type = Unsigned64
_CucsEtherErrStatsIntMacTx_Object = MibTableColumn
cucsEtherErrStatsIntMacTx = _CucsEtherErrStatsIntMacTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 24),
    _CucsEtherErrStatsIntMacTx_Type()
)
cucsEtherErrStatsIntMacTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacTx.setStatus("current")
_CucsEtherErrStatsIntMacTxDelta_Type = Counter64
_CucsEtherErrStatsIntMacTxDelta_Object = MibTableColumn
cucsEtherErrStatsIntMacTxDelta = _CucsEtherErrStatsIntMacTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 25),
    _CucsEtherErrStatsIntMacTxDelta_Type()
)
cucsEtherErrStatsIntMacTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacTxDelta.setStatus("current")
_CucsEtherErrStatsIntMacTxDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsIntMacTxDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsIntMacTxDeltaAvg = _CucsEtherErrStatsIntMacTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 26),
    _CucsEtherErrStatsIntMacTxDeltaAvg_Type()
)
cucsEtherErrStatsIntMacTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacTxDeltaAvg.setStatus("current")
_CucsEtherErrStatsIntMacTxDeltaMax_Type = Unsigned64
_CucsEtherErrStatsIntMacTxDeltaMax_Object = MibTableColumn
cucsEtherErrStatsIntMacTxDeltaMax = _CucsEtherErrStatsIntMacTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 27),
    _CucsEtherErrStatsIntMacTxDeltaMax_Type()
)
cucsEtherErrStatsIntMacTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacTxDeltaMax.setStatus("current")
_CucsEtherErrStatsIntMacTxDeltaMin_Type = Unsigned64
_CucsEtherErrStatsIntMacTxDeltaMin_Object = MibTableColumn
cucsEtherErrStatsIntMacTxDeltaMin = _CucsEtherErrStatsIntMacTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 28),
    _CucsEtherErrStatsIntMacTxDeltaMin_Type()
)
cucsEtherErrStatsIntMacTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntMacTxDeltaMin.setStatus("current")
_CucsEtherErrStatsIntervals_Type = Gauge32
_CucsEtherErrStatsIntervals_Object = MibTableColumn
cucsEtherErrStatsIntervals = _CucsEtherErrStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 29),
    _CucsEtherErrStatsIntervals_Type()
)
cucsEtherErrStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsIntervals.setStatus("current")
_CucsEtherErrStatsOutDiscard_Type = Unsigned64
_CucsEtherErrStatsOutDiscard_Object = MibTableColumn
cucsEtherErrStatsOutDiscard = _CucsEtherErrStatsOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 30),
    _CucsEtherErrStatsOutDiscard_Type()
)
cucsEtherErrStatsOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsOutDiscard.setStatus("current")
_CucsEtherErrStatsOutDiscardDelta_Type = Counter64
_CucsEtherErrStatsOutDiscardDelta_Object = MibTableColumn
cucsEtherErrStatsOutDiscardDelta = _CucsEtherErrStatsOutDiscardDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 31),
    _CucsEtherErrStatsOutDiscardDelta_Type()
)
cucsEtherErrStatsOutDiscardDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsOutDiscardDelta.setStatus("current")
_CucsEtherErrStatsOutDiscardDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsOutDiscardDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsOutDiscardDeltaAvg = _CucsEtherErrStatsOutDiscardDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 32),
    _CucsEtherErrStatsOutDiscardDeltaAvg_Type()
)
cucsEtherErrStatsOutDiscardDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsOutDiscardDeltaAvg.setStatus("current")
_CucsEtherErrStatsOutDiscardDeltaMax_Type = Unsigned64
_CucsEtherErrStatsOutDiscardDeltaMax_Object = MibTableColumn
cucsEtherErrStatsOutDiscardDeltaMax = _CucsEtherErrStatsOutDiscardDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 33),
    _CucsEtherErrStatsOutDiscardDeltaMax_Type()
)
cucsEtherErrStatsOutDiscardDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsOutDiscardDeltaMax.setStatus("current")
_CucsEtherErrStatsOutDiscardDeltaMin_Type = Unsigned64
_CucsEtherErrStatsOutDiscardDeltaMin_Object = MibTableColumn
cucsEtherErrStatsOutDiscardDeltaMin = _CucsEtherErrStatsOutDiscardDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 34),
    _CucsEtherErrStatsOutDiscardDeltaMin_Type()
)
cucsEtherErrStatsOutDiscardDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsOutDiscardDeltaMin.setStatus("current")
_CucsEtherErrStatsRcv_Type = Unsigned64
_CucsEtherErrStatsRcv_Object = MibTableColumn
cucsEtherErrStatsRcv = _CucsEtherErrStatsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 35),
    _CucsEtherErrStatsRcv_Type()
)
cucsEtherErrStatsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsRcv.setStatus("current")
_CucsEtherErrStatsRcvDelta_Type = Counter64
_CucsEtherErrStatsRcvDelta_Object = MibTableColumn
cucsEtherErrStatsRcvDelta = _CucsEtherErrStatsRcvDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 36),
    _CucsEtherErrStatsRcvDelta_Type()
)
cucsEtherErrStatsRcvDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsRcvDelta.setStatus("current")
_CucsEtherErrStatsRcvDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsRcvDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsRcvDeltaAvg = _CucsEtherErrStatsRcvDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 37),
    _CucsEtherErrStatsRcvDeltaAvg_Type()
)
cucsEtherErrStatsRcvDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsRcvDeltaAvg.setStatus("current")
_CucsEtherErrStatsRcvDeltaMax_Type = Unsigned64
_CucsEtherErrStatsRcvDeltaMax_Object = MibTableColumn
cucsEtherErrStatsRcvDeltaMax = _CucsEtherErrStatsRcvDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 38),
    _CucsEtherErrStatsRcvDeltaMax_Type()
)
cucsEtherErrStatsRcvDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsRcvDeltaMax.setStatus("current")
_CucsEtherErrStatsRcvDeltaMin_Type = Unsigned64
_CucsEtherErrStatsRcvDeltaMin_Object = MibTableColumn
cucsEtherErrStatsRcvDeltaMin = _CucsEtherErrStatsRcvDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 39),
    _CucsEtherErrStatsRcvDeltaMin_Type()
)
cucsEtherErrStatsRcvDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsRcvDeltaMin.setStatus("current")
_CucsEtherErrStatsSuspect_Type = TruthValue
_CucsEtherErrStatsSuspect_Object = MibTableColumn
cucsEtherErrStatsSuspect = _CucsEtherErrStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 40),
    _CucsEtherErrStatsSuspect_Type()
)
cucsEtherErrStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsSuspect.setStatus("current")
_CucsEtherErrStatsThresholded_Type = CucsEtherErrStatsThresholded
_CucsEtherErrStatsThresholded_Object = MibTableColumn
cucsEtherErrStatsThresholded = _CucsEtherErrStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 41),
    _CucsEtherErrStatsThresholded_Type()
)
cucsEtherErrStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsThresholded.setStatus("current")
_CucsEtherErrStatsTimeCollected_Type = DateAndTime
_CucsEtherErrStatsTimeCollected_Object = MibTableColumn
cucsEtherErrStatsTimeCollected = _CucsEtherErrStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 42),
    _CucsEtherErrStatsTimeCollected_Type()
)
cucsEtherErrStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsTimeCollected.setStatus("current")
_CucsEtherErrStatsUnderSize_Type = Unsigned64
_CucsEtherErrStatsUnderSize_Object = MibTableColumn
cucsEtherErrStatsUnderSize = _CucsEtherErrStatsUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 43),
    _CucsEtherErrStatsUnderSize_Type()
)
cucsEtherErrStatsUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsUnderSize.setStatus("current")
_CucsEtherErrStatsUnderSizeDelta_Type = Counter64
_CucsEtherErrStatsUnderSizeDelta_Object = MibTableColumn
cucsEtherErrStatsUnderSizeDelta = _CucsEtherErrStatsUnderSizeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 44),
    _CucsEtherErrStatsUnderSizeDelta_Type()
)
cucsEtherErrStatsUnderSizeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsUnderSizeDelta.setStatus("current")
_CucsEtherErrStatsUnderSizeDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsUnderSizeDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsUnderSizeDeltaAvg = _CucsEtherErrStatsUnderSizeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 45),
    _CucsEtherErrStatsUnderSizeDeltaAvg_Type()
)
cucsEtherErrStatsUnderSizeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsUnderSizeDeltaAvg.setStatus("current")
_CucsEtherErrStatsUnderSizeDeltaMax_Type = Unsigned64
_CucsEtherErrStatsUnderSizeDeltaMax_Object = MibTableColumn
cucsEtherErrStatsUnderSizeDeltaMax = _CucsEtherErrStatsUnderSizeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 46),
    _CucsEtherErrStatsUnderSizeDeltaMax_Type()
)
cucsEtherErrStatsUnderSizeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsUnderSizeDeltaMax.setStatus("current")
_CucsEtherErrStatsUnderSizeDeltaMin_Type = Unsigned64
_CucsEtherErrStatsUnderSizeDeltaMin_Object = MibTableColumn
cucsEtherErrStatsUnderSizeDeltaMin = _CucsEtherErrStatsUnderSizeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 47),
    _CucsEtherErrStatsUnderSizeDeltaMin_Type()
)
cucsEtherErrStatsUnderSizeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsUnderSizeDeltaMin.setStatus("current")
_CucsEtherErrStatsUpdate_Type = Gauge32
_CucsEtherErrStatsUpdate_Object = MibTableColumn
cucsEtherErrStatsUpdate = _CucsEtherErrStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 48),
    _CucsEtherErrStatsUpdate_Type()
)
cucsEtherErrStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsUpdate.setStatus("current")
_CucsEtherErrStatsXmit_Type = Unsigned64
_CucsEtherErrStatsXmit_Object = MibTableColumn
cucsEtherErrStatsXmit = _CucsEtherErrStatsXmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 49),
    _CucsEtherErrStatsXmit_Type()
)
cucsEtherErrStatsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsXmit.setStatus("current")
_CucsEtherErrStatsXmitDelta_Type = Counter64
_CucsEtherErrStatsXmitDelta_Object = MibTableColumn
cucsEtherErrStatsXmitDelta = _CucsEtherErrStatsXmitDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 50),
    _CucsEtherErrStatsXmitDelta_Type()
)
cucsEtherErrStatsXmitDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsXmitDelta.setStatus("current")
_CucsEtherErrStatsXmitDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsXmitDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsXmitDeltaAvg = _CucsEtherErrStatsXmitDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 51),
    _CucsEtherErrStatsXmitDeltaAvg_Type()
)
cucsEtherErrStatsXmitDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsXmitDeltaAvg.setStatus("current")
_CucsEtherErrStatsXmitDeltaMax_Type = Unsigned64
_CucsEtherErrStatsXmitDeltaMax_Object = MibTableColumn
cucsEtherErrStatsXmitDeltaMax = _CucsEtherErrStatsXmitDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 52),
    _CucsEtherErrStatsXmitDeltaMax_Type()
)
cucsEtherErrStatsXmitDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsXmitDeltaMax.setStatus("current")
_CucsEtherErrStatsXmitDeltaMin_Type = Unsigned64
_CucsEtherErrStatsXmitDeltaMin_Object = MibTableColumn
cucsEtherErrStatsXmitDeltaMin = _CucsEtherErrStatsXmitDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 1, 1, 53),
    _CucsEtherErrStatsXmitDeltaMin_Type()
)
cucsEtherErrStatsXmitDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsXmitDeltaMin.setStatus("current")
_CucsEtherErrStatsHistTable_Object = MibTable
cucsEtherErrStatsHistTable = _CucsEtherErrStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2)
)
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistTable.setStatus("current")
_CucsEtherErrStatsHistEntry_Object = MibTableRow
cucsEtherErrStatsHistEntry = _CucsEtherErrStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1)
)
cucsEtherErrStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherErrStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistEntry.setStatus("current")
_CucsEtherErrStatsHistInstanceId_Type = CucsManagedObjectId
_CucsEtherErrStatsHistInstanceId_Object = MibTableColumn
cucsEtherErrStatsHistInstanceId = _CucsEtherErrStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 1),
    _CucsEtherErrStatsHistInstanceId_Type()
)
cucsEtherErrStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistInstanceId.setStatus("current")
_CucsEtherErrStatsHistDn_Type = CucsManagedObjectDn
_CucsEtherErrStatsHistDn_Object = MibTableColumn
cucsEtherErrStatsHistDn = _CucsEtherErrStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 2),
    _CucsEtherErrStatsHistDn_Type()
)
cucsEtherErrStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistDn.setStatus("current")
_CucsEtherErrStatsHistRn_Type = SnmpAdminString
_CucsEtherErrStatsHistRn_Object = MibTableColumn
cucsEtherErrStatsHistRn = _CucsEtherErrStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 3),
    _CucsEtherErrStatsHistRn_Type()
)
cucsEtherErrStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistRn.setStatus("current")
_CucsEtherErrStatsHistAlign_Type = Unsigned64
_CucsEtherErrStatsHistAlign_Object = MibTableColumn
cucsEtherErrStatsHistAlign = _CucsEtherErrStatsHistAlign_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 4),
    _CucsEtherErrStatsHistAlign_Type()
)
cucsEtherErrStatsHistAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistAlign.setStatus("current")
_CucsEtherErrStatsHistAlignDelta_Type = Unsigned64
_CucsEtherErrStatsHistAlignDelta_Object = MibTableColumn
cucsEtherErrStatsHistAlignDelta = _CucsEtherErrStatsHistAlignDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 5),
    _CucsEtherErrStatsHistAlignDelta_Type()
)
cucsEtherErrStatsHistAlignDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistAlignDelta.setStatus("current")
_CucsEtherErrStatsHistAlignDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistAlignDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistAlignDeltaAvg = _CucsEtherErrStatsHistAlignDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 6),
    _CucsEtherErrStatsHistAlignDeltaAvg_Type()
)
cucsEtherErrStatsHistAlignDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistAlignDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistAlignDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistAlignDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistAlignDeltaMax = _CucsEtherErrStatsHistAlignDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 7),
    _CucsEtherErrStatsHistAlignDeltaMax_Type()
)
cucsEtherErrStatsHistAlignDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistAlignDeltaMax.setStatus("current")
_CucsEtherErrStatsHistAlignDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistAlignDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistAlignDeltaMin = _CucsEtherErrStatsHistAlignDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 8),
    _CucsEtherErrStatsHistAlignDeltaMin_Type()
)
cucsEtherErrStatsHistAlignDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistAlignDeltaMin.setStatus("current")
_CucsEtherErrStatsHistDeferredTx_Type = Unsigned64
_CucsEtherErrStatsHistDeferredTx_Object = MibTableColumn
cucsEtherErrStatsHistDeferredTx = _CucsEtherErrStatsHistDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 9),
    _CucsEtherErrStatsHistDeferredTx_Type()
)
cucsEtherErrStatsHistDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistDeferredTx.setStatus("current")
_CucsEtherErrStatsHistDeferredTxDelta_Type = Unsigned64
_CucsEtherErrStatsHistDeferredTxDelta_Object = MibTableColumn
cucsEtherErrStatsHistDeferredTxDelta = _CucsEtherErrStatsHistDeferredTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 10),
    _CucsEtherErrStatsHistDeferredTxDelta_Type()
)
cucsEtherErrStatsHistDeferredTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistDeferredTxDelta.setStatus("current")
_CucsEtherErrStatsHistDeferredTxDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistDeferredTxDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistDeferredTxDeltaAvg = _CucsEtherErrStatsHistDeferredTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 11),
    _CucsEtherErrStatsHistDeferredTxDeltaAvg_Type()
)
cucsEtherErrStatsHistDeferredTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistDeferredTxDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistDeferredTxDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistDeferredTxDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistDeferredTxDeltaMax = _CucsEtherErrStatsHistDeferredTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 12),
    _CucsEtherErrStatsHistDeferredTxDeltaMax_Type()
)
cucsEtherErrStatsHistDeferredTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistDeferredTxDeltaMax.setStatus("current")
_CucsEtherErrStatsHistDeferredTxDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistDeferredTxDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistDeferredTxDeltaMin = _CucsEtherErrStatsHistDeferredTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 13),
    _CucsEtherErrStatsHistDeferredTxDeltaMin_Type()
)
cucsEtherErrStatsHistDeferredTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistDeferredTxDeltaMin.setStatus("current")
_CucsEtherErrStatsHistFcs_Type = Unsigned64
_CucsEtherErrStatsHistFcs_Object = MibTableColumn
cucsEtherErrStatsHistFcs = _CucsEtherErrStatsHistFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 14),
    _CucsEtherErrStatsHistFcs_Type()
)
cucsEtherErrStatsHistFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistFcs.setStatus("current")
_CucsEtherErrStatsHistFcsDelta_Type = Unsigned64
_CucsEtherErrStatsHistFcsDelta_Object = MibTableColumn
cucsEtherErrStatsHistFcsDelta = _CucsEtherErrStatsHistFcsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 15),
    _CucsEtherErrStatsHistFcsDelta_Type()
)
cucsEtherErrStatsHistFcsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistFcsDelta.setStatus("current")
_CucsEtherErrStatsHistFcsDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistFcsDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistFcsDeltaAvg = _CucsEtherErrStatsHistFcsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 16),
    _CucsEtherErrStatsHistFcsDeltaAvg_Type()
)
cucsEtherErrStatsHistFcsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistFcsDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistFcsDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistFcsDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistFcsDeltaMax = _CucsEtherErrStatsHistFcsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 17),
    _CucsEtherErrStatsHistFcsDeltaMax_Type()
)
cucsEtherErrStatsHistFcsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistFcsDeltaMax.setStatus("current")
_CucsEtherErrStatsHistFcsDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistFcsDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistFcsDeltaMin = _CucsEtherErrStatsHistFcsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 18),
    _CucsEtherErrStatsHistFcsDeltaMin_Type()
)
cucsEtherErrStatsHistFcsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistFcsDeltaMin.setStatus("current")
_CucsEtherErrStatsHistId_Type = Unsigned64
_CucsEtherErrStatsHistId_Object = MibTableColumn
cucsEtherErrStatsHistId = _CucsEtherErrStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 19),
    _CucsEtherErrStatsHistId_Type()
)
cucsEtherErrStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistId.setStatus("current")
_CucsEtherErrStatsHistIntMacRx_Type = Unsigned64
_CucsEtherErrStatsHistIntMacRx_Object = MibTableColumn
cucsEtherErrStatsHistIntMacRx = _CucsEtherErrStatsHistIntMacRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 20),
    _CucsEtherErrStatsHistIntMacRx_Type()
)
cucsEtherErrStatsHistIntMacRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacRx.setStatus("current")
_CucsEtherErrStatsHistIntMacRxDelta_Type = Unsigned64
_CucsEtherErrStatsHistIntMacRxDelta_Object = MibTableColumn
cucsEtherErrStatsHistIntMacRxDelta = _CucsEtherErrStatsHistIntMacRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 21),
    _CucsEtherErrStatsHistIntMacRxDelta_Type()
)
cucsEtherErrStatsHistIntMacRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacRxDelta.setStatus("current")
_CucsEtherErrStatsHistIntMacRxDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistIntMacRxDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistIntMacRxDeltaAvg = _CucsEtherErrStatsHistIntMacRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 22),
    _CucsEtherErrStatsHistIntMacRxDeltaAvg_Type()
)
cucsEtherErrStatsHistIntMacRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacRxDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistIntMacRxDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistIntMacRxDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistIntMacRxDeltaMax = _CucsEtherErrStatsHistIntMacRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 23),
    _CucsEtherErrStatsHistIntMacRxDeltaMax_Type()
)
cucsEtherErrStatsHistIntMacRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacRxDeltaMax.setStatus("current")
_CucsEtherErrStatsHistIntMacRxDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistIntMacRxDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistIntMacRxDeltaMin = _CucsEtherErrStatsHistIntMacRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 24),
    _CucsEtherErrStatsHistIntMacRxDeltaMin_Type()
)
cucsEtherErrStatsHistIntMacRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacRxDeltaMin.setStatus("current")
_CucsEtherErrStatsHistIntMacTx_Type = Unsigned64
_CucsEtherErrStatsHistIntMacTx_Object = MibTableColumn
cucsEtherErrStatsHistIntMacTx = _CucsEtherErrStatsHistIntMacTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 25),
    _CucsEtherErrStatsHistIntMacTx_Type()
)
cucsEtherErrStatsHistIntMacTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacTx.setStatus("current")
_CucsEtherErrStatsHistIntMacTxDelta_Type = Unsigned64
_CucsEtherErrStatsHistIntMacTxDelta_Object = MibTableColumn
cucsEtherErrStatsHistIntMacTxDelta = _CucsEtherErrStatsHistIntMacTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 26),
    _CucsEtherErrStatsHistIntMacTxDelta_Type()
)
cucsEtherErrStatsHistIntMacTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacTxDelta.setStatus("current")
_CucsEtherErrStatsHistIntMacTxDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistIntMacTxDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistIntMacTxDeltaAvg = _CucsEtherErrStatsHistIntMacTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 27),
    _CucsEtherErrStatsHistIntMacTxDeltaAvg_Type()
)
cucsEtherErrStatsHistIntMacTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacTxDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistIntMacTxDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistIntMacTxDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistIntMacTxDeltaMax = _CucsEtherErrStatsHistIntMacTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 28),
    _CucsEtherErrStatsHistIntMacTxDeltaMax_Type()
)
cucsEtherErrStatsHistIntMacTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacTxDeltaMax.setStatus("current")
_CucsEtherErrStatsHistIntMacTxDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistIntMacTxDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistIntMacTxDeltaMin = _CucsEtherErrStatsHistIntMacTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 29),
    _CucsEtherErrStatsHistIntMacTxDeltaMin_Type()
)
cucsEtherErrStatsHistIntMacTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistIntMacTxDeltaMin.setStatus("current")
_CucsEtherErrStatsHistMostRecent_Type = TruthValue
_CucsEtherErrStatsHistMostRecent_Object = MibTableColumn
cucsEtherErrStatsHistMostRecent = _CucsEtherErrStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 30),
    _CucsEtherErrStatsHistMostRecent_Type()
)
cucsEtherErrStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistMostRecent.setStatus("current")
_CucsEtherErrStatsHistOutDiscard_Type = Unsigned64
_CucsEtherErrStatsHistOutDiscard_Object = MibTableColumn
cucsEtherErrStatsHistOutDiscard = _CucsEtherErrStatsHistOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 31),
    _CucsEtherErrStatsHistOutDiscard_Type()
)
cucsEtherErrStatsHistOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistOutDiscard.setStatus("current")
_CucsEtherErrStatsHistOutDiscardDelta_Type = Unsigned64
_CucsEtherErrStatsHistOutDiscardDelta_Object = MibTableColumn
cucsEtherErrStatsHistOutDiscardDelta = _CucsEtherErrStatsHistOutDiscardDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 32),
    _CucsEtherErrStatsHistOutDiscardDelta_Type()
)
cucsEtherErrStatsHistOutDiscardDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistOutDiscardDelta.setStatus("current")
_CucsEtherErrStatsHistOutDiscardDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistOutDiscardDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistOutDiscardDeltaAvg = _CucsEtherErrStatsHistOutDiscardDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 33),
    _CucsEtherErrStatsHistOutDiscardDeltaAvg_Type()
)
cucsEtherErrStatsHistOutDiscardDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistOutDiscardDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistOutDiscardDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistOutDiscardDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistOutDiscardDeltaMax = _CucsEtherErrStatsHistOutDiscardDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 34),
    _CucsEtherErrStatsHistOutDiscardDeltaMax_Type()
)
cucsEtherErrStatsHistOutDiscardDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistOutDiscardDeltaMax.setStatus("current")
_CucsEtherErrStatsHistOutDiscardDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistOutDiscardDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistOutDiscardDeltaMin = _CucsEtherErrStatsHistOutDiscardDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 35),
    _CucsEtherErrStatsHistOutDiscardDeltaMin_Type()
)
cucsEtherErrStatsHistOutDiscardDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistOutDiscardDeltaMin.setStatus("current")
_CucsEtherErrStatsHistRcv_Type = Unsigned64
_CucsEtherErrStatsHistRcv_Object = MibTableColumn
cucsEtherErrStatsHistRcv = _CucsEtherErrStatsHistRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 36),
    _CucsEtherErrStatsHistRcv_Type()
)
cucsEtherErrStatsHistRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistRcv.setStatus("current")
_CucsEtherErrStatsHistRcvDelta_Type = Unsigned64
_CucsEtherErrStatsHistRcvDelta_Object = MibTableColumn
cucsEtherErrStatsHistRcvDelta = _CucsEtherErrStatsHistRcvDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 37),
    _CucsEtherErrStatsHistRcvDelta_Type()
)
cucsEtherErrStatsHistRcvDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistRcvDelta.setStatus("current")
_CucsEtherErrStatsHistRcvDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistRcvDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistRcvDeltaAvg = _CucsEtherErrStatsHistRcvDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 38),
    _CucsEtherErrStatsHistRcvDeltaAvg_Type()
)
cucsEtherErrStatsHistRcvDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistRcvDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistRcvDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistRcvDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistRcvDeltaMax = _CucsEtherErrStatsHistRcvDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 39),
    _CucsEtherErrStatsHistRcvDeltaMax_Type()
)
cucsEtherErrStatsHistRcvDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistRcvDeltaMax.setStatus("current")
_CucsEtherErrStatsHistRcvDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistRcvDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistRcvDeltaMin = _CucsEtherErrStatsHistRcvDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 40),
    _CucsEtherErrStatsHistRcvDeltaMin_Type()
)
cucsEtherErrStatsHistRcvDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistRcvDeltaMin.setStatus("current")
_CucsEtherErrStatsHistSuspect_Type = TruthValue
_CucsEtherErrStatsHistSuspect_Object = MibTableColumn
cucsEtherErrStatsHistSuspect = _CucsEtherErrStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 41),
    _CucsEtherErrStatsHistSuspect_Type()
)
cucsEtherErrStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistSuspect.setStatus("current")
_CucsEtherErrStatsHistThresholded_Type = CucsEtherErrStatsHistThresholded
_CucsEtherErrStatsHistThresholded_Object = MibTableColumn
cucsEtherErrStatsHistThresholded = _CucsEtherErrStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 42),
    _CucsEtherErrStatsHistThresholded_Type()
)
cucsEtherErrStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistThresholded.setStatus("current")
_CucsEtherErrStatsHistTimeCollected_Type = DateAndTime
_CucsEtherErrStatsHistTimeCollected_Object = MibTableColumn
cucsEtherErrStatsHistTimeCollected = _CucsEtherErrStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 43),
    _CucsEtherErrStatsHistTimeCollected_Type()
)
cucsEtherErrStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistTimeCollected.setStatus("current")
_CucsEtherErrStatsHistUnderSize_Type = Unsigned64
_CucsEtherErrStatsHistUnderSize_Object = MibTableColumn
cucsEtherErrStatsHistUnderSize = _CucsEtherErrStatsHistUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 44),
    _CucsEtherErrStatsHistUnderSize_Type()
)
cucsEtherErrStatsHistUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistUnderSize.setStatus("current")
_CucsEtherErrStatsHistUnderSizeDelta_Type = Unsigned64
_CucsEtherErrStatsHistUnderSizeDelta_Object = MibTableColumn
cucsEtherErrStatsHistUnderSizeDelta = _CucsEtherErrStatsHistUnderSizeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 45),
    _CucsEtherErrStatsHistUnderSizeDelta_Type()
)
cucsEtherErrStatsHistUnderSizeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistUnderSizeDelta.setStatus("current")
_CucsEtherErrStatsHistUnderSizeDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistUnderSizeDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistUnderSizeDeltaAvg = _CucsEtherErrStatsHistUnderSizeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 46),
    _CucsEtherErrStatsHistUnderSizeDeltaAvg_Type()
)
cucsEtherErrStatsHistUnderSizeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistUnderSizeDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistUnderSizeDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistUnderSizeDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistUnderSizeDeltaMax = _CucsEtherErrStatsHistUnderSizeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 47),
    _CucsEtherErrStatsHistUnderSizeDeltaMax_Type()
)
cucsEtherErrStatsHistUnderSizeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistUnderSizeDeltaMax.setStatus("current")
_CucsEtherErrStatsHistUnderSizeDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistUnderSizeDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistUnderSizeDeltaMin = _CucsEtherErrStatsHistUnderSizeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 48),
    _CucsEtherErrStatsHistUnderSizeDeltaMin_Type()
)
cucsEtherErrStatsHistUnderSizeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistUnderSizeDeltaMin.setStatus("current")
_CucsEtherErrStatsHistXmit_Type = Unsigned64
_CucsEtherErrStatsHistXmit_Object = MibTableColumn
cucsEtherErrStatsHistXmit = _CucsEtherErrStatsHistXmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 49),
    _CucsEtherErrStatsHistXmit_Type()
)
cucsEtherErrStatsHistXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistXmit.setStatus("current")
_CucsEtherErrStatsHistXmitDelta_Type = Unsigned64
_CucsEtherErrStatsHistXmitDelta_Object = MibTableColumn
cucsEtherErrStatsHistXmitDelta = _CucsEtherErrStatsHistXmitDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 50),
    _CucsEtherErrStatsHistXmitDelta_Type()
)
cucsEtherErrStatsHistXmitDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistXmitDelta.setStatus("current")
_CucsEtherErrStatsHistXmitDeltaAvg_Type = Unsigned64
_CucsEtherErrStatsHistXmitDeltaAvg_Object = MibTableColumn
cucsEtherErrStatsHistXmitDeltaAvg = _CucsEtherErrStatsHistXmitDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 51),
    _CucsEtherErrStatsHistXmitDeltaAvg_Type()
)
cucsEtherErrStatsHistXmitDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistXmitDeltaAvg.setStatus("current")
_CucsEtherErrStatsHistXmitDeltaMax_Type = Unsigned64
_CucsEtherErrStatsHistXmitDeltaMax_Object = MibTableColumn
cucsEtherErrStatsHistXmitDeltaMax = _CucsEtherErrStatsHistXmitDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 52),
    _CucsEtherErrStatsHistXmitDeltaMax_Type()
)
cucsEtherErrStatsHistXmitDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistXmitDeltaMax.setStatus("current")
_CucsEtherErrStatsHistXmitDeltaMin_Type = Unsigned64
_CucsEtherErrStatsHistXmitDeltaMin_Object = MibTableColumn
cucsEtherErrStatsHistXmitDeltaMin = _CucsEtherErrStatsHistXmitDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 2, 1, 53),
    _CucsEtherErrStatsHistXmitDeltaMin_Type()
)
cucsEtherErrStatsHistXmitDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherErrStatsHistXmitDeltaMin.setStatus("current")
_CucsEtherLossStatsTable_Object = MibTable
cucsEtherLossStatsTable = _CucsEtherLossStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3)
)
if mibBuilder.loadTexts:
    cucsEtherLossStatsTable.setStatus("current")
_CucsEtherLossStatsEntry_Object = MibTableRow
cucsEtherLossStatsEntry = _CucsEtherLossStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1)
)
cucsEtherLossStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherLossStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherLossStatsEntry.setStatus("current")
_CucsEtherLossStatsInstanceId_Type = CucsManagedObjectId
_CucsEtherLossStatsInstanceId_Object = MibTableColumn
cucsEtherLossStatsInstanceId = _CucsEtherLossStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 1),
    _CucsEtherLossStatsInstanceId_Type()
)
cucsEtherLossStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherLossStatsInstanceId.setStatus("current")
_CucsEtherLossStatsDn_Type = CucsManagedObjectDn
_CucsEtherLossStatsDn_Object = MibTableColumn
cucsEtherLossStatsDn = _CucsEtherLossStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 2),
    _CucsEtherLossStatsDn_Type()
)
cucsEtherLossStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsDn.setStatus("current")
_CucsEtherLossStatsRn_Type = SnmpAdminString
_CucsEtherLossStatsRn_Object = MibTableColumn
cucsEtherLossStatsRn = _CucsEtherLossStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 3),
    _CucsEtherLossStatsRn_Type()
)
cucsEtherLossStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsRn.setStatus("current")
_CucsEtherLossStatsSQETest_Type = Unsigned64
_CucsEtherLossStatsSQETest_Object = MibTableColumn
cucsEtherLossStatsSQETest = _CucsEtherLossStatsSQETest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 4),
    _CucsEtherLossStatsSQETest_Type()
)
cucsEtherLossStatsSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSQETest.setStatus("current")
_CucsEtherLossStatsSQETestDelta_Type = Counter64
_CucsEtherLossStatsSQETestDelta_Object = MibTableColumn
cucsEtherLossStatsSQETestDelta = _CucsEtherLossStatsSQETestDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 5),
    _CucsEtherLossStatsSQETestDelta_Type()
)
cucsEtherLossStatsSQETestDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSQETestDelta.setStatus("current")
_CucsEtherLossStatsSQETestDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsSQETestDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsSQETestDeltaAvg = _CucsEtherLossStatsSQETestDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 6),
    _CucsEtherLossStatsSQETestDeltaAvg_Type()
)
cucsEtherLossStatsSQETestDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSQETestDeltaAvg.setStatus("current")
_CucsEtherLossStatsSQETestDeltaMax_Type = Unsigned64
_CucsEtherLossStatsSQETestDeltaMax_Object = MibTableColumn
cucsEtherLossStatsSQETestDeltaMax = _CucsEtherLossStatsSQETestDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 7),
    _CucsEtherLossStatsSQETestDeltaMax_Type()
)
cucsEtherLossStatsSQETestDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSQETestDeltaMax.setStatus("current")
_CucsEtherLossStatsSQETestDeltaMin_Type = Unsigned64
_CucsEtherLossStatsSQETestDeltaMin_Object = MibTableColumn
cucsEtherLossStatsSQETestDeltaMin = _CucsEtherLossStatsSQETestDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 8),
    _CucsEtherLossStatsSQETestDeltaMin_Type()
)
cucsEtherLossStatsSQETestDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSQETestDeltaMin.setStatus("current")
_CucsEtherLossStatsCarrierSense_Type = Unsigned64
_CucsEtherLossStatsCarrierSense_Object = MibTableColumn
cucsEtherLossStatsCarrierSense = _CucsEtherLossStatsCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 9),
    _CucsEtherLossStatsCarrierSense_Type()
)
cucsEtherLossStatsCarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsCarrierSense.setStatus("current")
_CucsEtherLossStatsCarrierSenseDelta_Type = Counter64
_CucsEtherLossStatsCarrierSenseDelta_Object = MibTableColumn
cucsEtherLossStatsCarrierSenseDelta = _CucsEtherLossStatsCarrierSenseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 10),
    _CucsEtherLossStatsCarrierSenseDelta_Type()
)
cucsEtherLossStatsCarrierSenseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsCarrierSenseDelta.setStatus("current")
_CucsEtherLossStatsCarrierSenseDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsCarrierSenseDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsCarrierSenseDeltaAvg = _CucsEtherLossStatsCarrierSenseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 11),
    _CucsEtherLossStatsCarrierSenseDeltaAvg_Type()
)
cucsEtherLossStatsCarrierSenseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsCarrierSenseDeltaAvg.setStatus("current")
_CucsEtherLossStatsCarrierSenseDeltaMax_Type = Unsigned64
_CucsEtherLossStatsCarrierSenseDeltaMax_Object = MibTableColumn
cucsEtherLossStatsCarrierSenseDeltaMax = _CucsEtherLossStatsCarrierSenseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 12),
    _CucsEtherLossStatsCarrierSenseDeltaMax_Type()
)
cucsEtherLossStatsCarrierSenseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsCarrierSenseDeltaMax.setStatus("current")
_CucsEtherLossStatsCarrierSenseDeltaMin_Type = Unsigned64
_CucsEtherLossStatsCarrierSenseDeltaMin_Object = MibTableColumn
cucsEtherLossStatsCarrierSenseDeltaMin = _CucsEtherLossStatsCarrierSenseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 13),
    _CucsEtherLossStatsCarrierSenseDeltaMin_Type()
)
cucsEtherLossStatsCarrierSenseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsCarrierSenseDeltaMin.setStatus("current")
_CucsEtherLossStatsExcessCollision_Type = Unsigned64
_CucsEtherLossStatsExcessCollision_Object = MibTableColumn
cucsEtherLossStatsExcessCollision = _CucsEtherLossStatsExcessCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 14),
    _CucsEtherLossStatsExcessCollision_Type()
)
cucsEtherLossStatsExcessCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsExcessCollision.setStatus("current")
_CucsEtherLossStatsExcessCollisionDelta_Type = Counter64
_CucsEtherLossStatsExcessCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsExcessCollisionDelta = _CucsEtherLossStatsExcessCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 15),
    _CucsEtherLossStatsExcessCollisionDelta_Type()
)
cucsEtherLossStatsExcessCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsExcessCollisionDelta.setStatus("current")
_CucsEtherLossStatsExcessCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsExcessCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsExcessCollisionDeltaAvg = _CucsEtherLossStatsExcessCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 16),
    _CucsEtherLossStatsExcessCollisionDeltaAvg_Type()
)
cucsEtherLossStatsExcessCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsExcessCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsExcessCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsExcessCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsExcessCollisionDeltaMax = _CucsEtherLossStatsExcessCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 17),
    _CucsEtherLossStatsExcessCollisionDeltaMax_Type()
)
cucsEtherLossStatsExcessCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsExcessCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsExcessCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsExcessCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsExcessCollisionDeltaMin = _CucsEtherLossStatsExcessCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 18),
    _CucsEtherLossStatsExcessCollisionDeltaMin_Type()
)
cucsEtherLossStatsExcessCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsExcessCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsGiants_Type = Unsigned64
_CucsEtherLossStatsGiants_Object = MibTableColumn
cucsEtherLossStatsGiants = _CucsEtherLossStatsGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 19),
    _CucsEtherLossStatsGiants_Type()
)
cucsEtherLossStatsGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsGiants.setStatus("current")
_CucsEtherLossStatsGiantsDelta_Type = Counter64
_CucsEtherLossStatsGiantsDelta_Object = MibTableColumn
cucsEtherLossStatsGiantsDelta = _CucsEtherLossStatsGiantsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 20),
    _CucsEtherLossStatsGiantsDelta_Type()
)
cucsEtherLossStatsGiantsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsGiantsDelta.setStatus("current")
_CucsEtherLossStatsGiantsDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsGiantsDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsGiantsDeltaAvg = _CucsEtherLossStatsGiantsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 21),
    _CucsEtherLossStatsGiantsDeltaAvg_Type()
)
cucsEtherLossStatsGiantsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsGiantsDeltaAvg.setStatus("current")
_CucsEtherLossStatsGiantsDeltaMax_Type = Unsigned64
_CucsEtherLossStatsGiantsDeltaMax_Object = MibTableColumn
cucsEtherLossStatsGiantsDeltaMax = _CucsEtherLossStatsGiantsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 22),
    _CucsEtherLossStatsGiantsDeltaMax_Type()
)
cucsEtherLossStatsGiantsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsGiantsDeltaMax.setStatus("current")
_CucsEtherLossStatsGiantsDeltaMin_Type = Unsigned64
_CucsEtherLossStatsGiantsDeltaMin_Object = MibTableColumn
cucsEtherLossStatsGiantsDeltaMin = _CucsEtherLossStatsGiantsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 23),
    _CucsEtherLossStatsGiantsDeltaMin_Type()
)
cucsEtherLossStatsGiantsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsGiantsDeltaMin.setStatus("current")
_CucsEtherLossStatsIntervals_Type = Gauge32
_CucsEtherLossStatsIntervals_Object = MibTableColumn
cucsEtherLossStatsIntervals = _CucsEtherLossStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 24),
    _CucsEtherLossStatsIntervals_Type()
)
cucsEtherLossStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsIntervals.setStatus("current")
_CucsEtherLossStatsLateCollision_Type = Unsigned64
_CucsEtherLossStatsLateCollision_Object = MibTableColumn
cucsEtherLossStatsLateCollision = _CucsEtherLossStatsLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 25),
    _CucsEtherLossStatsLateCollision_Type()
)
cucsEtherLossStatsLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsLateCollision.setStatus("current")
_CucsEtherLossStatsLateCollisionDelta_Type = Counter64
_CucsEtherLossStatsLateCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsLateCollisionDelta = _CucsEtherLossStatsLateCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 26),
    _CucsEtherLossStatsLateCollisionDelta_Type()
)
cucsEtherLossStatsLateCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsLateCollisionDelta.setStatus("current")
_CucsEtherLossStatsLateCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsLateCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsLateCollisionDeltaAvg = _CucsEtherLossStatsLateCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 27),
    _CucsEtherLossStatsLateCollisionDeltaAvg_Type()
)
cucsEtherLossStatsLateCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsLateCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsLateCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsLateCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsLateCollisionDeltaMax = _CucsEtherLossStatsLateCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 28),
    _CucsEtherLossStatsLateCollisionDeltaMax_Type()
)
cucsEtherLossStatsLateCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsLateCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsLateCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsLateCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsLateCollisionDeltaMin = _CucsEtherLossStatsLateCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 29),
    _CucsEtherLossStatsLateCollisionDeltaMin_Type()
)
cucsEtherLossStatsLateCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsLateCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsMultiCollision_Type = Unsigned64
_CucsEtherLossStatsMultiCollision_Object = MibTableColumn
cucsEtherLossStatsMultiCollision = _CucsEtherLossStatsMultiCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 30),
    _CucsEtherLossStatsMultiCollision_Type()
)
cucsEtherLossStatsMultiCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsMultiCollision.setStatus("current")
_CucsEtherLossStatsMultiCollisionDelta_Type = Counter64
_CucsEtherLossStatsMultiCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsMultiCollisionDelta = _CucsEtherLossStatsMultiCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 31),
    _CucsEtherLossStatsMultiCollisionDelta_Type()
)
cucsEtherLossStatsMultiCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsMultiCollisionDelta.setStatus("current")
_CucsEtherLossStatsMultiCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsMultiCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsMultiCollisionDeltaAvg = _CucsEtherLossStatsMultiCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 32),
    _CucsEtherLossStatsMultiCollisionDeltaAvg_Type()
)
cucsEtherLossStatsMultiCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsMultiCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsMultiCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsMultiCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsMultiCollisionDeltaMax = _CucsEtherLossStatsMultiCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 33),
    _CucsEtherLossStatsMultiCollisionDeltaMax_Type()
)
cucsEtherLossStatsMultiCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsMultiCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsMultiCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsMultiCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsMultiCollisionDeltaMin = _CucsEtherLossStatsMultiCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 34),
    _CucsEtherLossStatsMultiCollisionDeltaMin_Type()
)
cucsEtherLossStatsMultiCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsMultiCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsSingleCollision_Type = Unsigned64
_CucsEtherLossStatsSingleCollision_Object = MibTableColumn
cucsEtherLossStatsSingleCollision = _CucsEtherLossStatsSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 35),
    _CucsEtherLossStatsSingleCollision_Type()
)
cucsEtherLossStatsSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSingleCollision.setStatus("current")
_CucsEtherLossStatsSingleCollisionDelta_Type = Counter64
_CucsEtherLossStatsSingleCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsSingleCollisionDelta = _CucsEtherLossStatsSingleCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 36),
    _CucsEtherLossStatsSingleCollisionDelta_Type()
)
cucsEtherLossStatsSingleCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSingleCollisionDelta.setStatus("current")
_CucsEtherLossStatsSingleCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsSingleCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsSingleCollisionDeltaAvg = _CucsEtherLossStatsSingleCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 37),
    _CucsEtherLossStatsSingleCollisionDeltaAvg_Type()
)
cucsEtherLossStatsSingleCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSingleCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsSingleCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsSingleCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsSingleCollisionDeltaMax = _CucsEtherLossStatsSingleCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 38),
    _CucsEtherLossStatsSingleCollisionDeltaMax_Type()
)
cucsEtherLossStatsSingleCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSingleCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsSingleCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsSingleCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsSingleCollisionDeltaMin = _CucsEtherLossStatsSingleCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 39),
    _CucsEtherLossStatsSingleCollisionDeltaMin_Type()
)
cucsEtherLossStatsSingleCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSingleCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsSuspect_Type = TruthValue
_CucsEtherLossStatsSuspect_Object = MibTableColumn
cucsEtherLossStatsSuspect = _CucsEtherLossStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 40),
    _CucsEtherLossStatsSuspect_Type()
)
cucsEtherLossStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSuspect.setStatus("current")
_CucsEtherLossStatsSymbol_Type = Unsigned64
_CucsEtherLossStatsSymbol_Object = MibTableColumn
cucsEtherLossStatsSymbol = _CucsEtherLossStatsSymbol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 41),
    _CucsEtherLossStatsSymbol_Type()
)
cucsEtherLossStatsSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSymbol.setStatus("current")
_CucsEtherLossStatsSymbolDelta_Type = Counter64
_CucsEtherLossStatsSymbolDelta_Object = MibTableColumn
cucsEtherLossStatsSymbolDelta = _CucsEtherLossStatsSymbolDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 42),
    _CucsEtherLossStatsSymbolDelta_Type()
)
cucsEtherLossStatsSymbolDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSymbolDelta.setStatus("current")
_CucsEtherLossStatsSymbolDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsSymbolDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsSymbolDeltaAvg = _CucsEtherLossStatsSymbolDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 43),
    _CucsEtherLossStatsSymbolDeltaAvg_Type()
)
cucsEtherLossStatsSymbolDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSymbolDeltaAvg.setStatus("current")
_CucsEtherLossStatsSymbolDeltaMax_Type = Unsigned64
_CucsEtherLossStatsSymbolDeltaMax_Object = MibTableColumn
cucsEtherLossStatsSymbolDeltaMax = _CucsEtherLossStatsSymbolDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 44),
    _CucsEtherLossStatsSymbolDeltaMax_Type()
)
cucsEtherLossStatsSymbolDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSymbolDeltaMax.setStatus("current")
_CucsEtherLossStatsSymbolDeltaMin_Type = Unsigned64
_CucsEtherLossStatsSymbolDeltaMin_Object = MibTableColumn
cucsEtherLossStatsSymbolDeltaMin = _CucsEtherLossStatsSymbolDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 45),
    _CucsEtherLossStatsSymbolDeltaMin_Type()
)
cucsEtherLossStatsSymbolDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsSymbolDeltaMin.setStatus("current")
_CucsEtherLossStatsThresholded_Type = CucsEtherLossStatsThresholded
_CucsEtherLossStatsThresholded_Object = MibTableColumn
cucsEtherLossStatsThresholded = _CucsEtherLossStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 46),
    _CucsEtherLossStatsThresholded_Type()
)
cucsEtherLossStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsThresholded.setStatus("current")
_CucsEtherLossStatsTimeCollected_Type = DateAndTime
_CucsEtherLossStatsTimeCollected_Object = MibTableColumn
cucsEtherLossStatsTimeCollected = _CucsEtherLossStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 47),
    _CucsEtherLossStatsTimeCollected_Type()
)
cucsEtherLossStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsTimeCollected.setStatus("current")
_CucsEtherLossStatsUpdate_Type = Gauge32
_CucsEtherLossStatsUpdate_Object = MibTableColumn
cucsEtherLossStatsUpdate = _CucsEtherLossStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 3, 1, 48),
    _CucsEtherLossStatsUpdate_Type()
)
cucsEtherLossStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsUpdate.setStatus("current")
_CucsEtherLossStatsHistTable_Object = MibTable
cucsEtherLossStatsHistTable = _CucsEtherLossStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4)
)
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistTable.setStatus("current")
_CucsEtherLossStatsHistEntry_Object = MibTableRow
cucsEtherLossStatsHistEntry = _CucsEtherLossStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1)
)
cucsEtherLossStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherLossStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistEntry.setStatus("current")
_CucsEtherLossStatsHistInstanceId_Type = CucsManagedObjectId
_CucsEtherLossStatsHistInstanceId_Object = MibTableColumn
cucsEtherLossStatsHistInstanceId = _CucsEtherLossStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 1),
    _CucsEtherLossStatsHistInstanceId_Type()
)
cucsEtherLossStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistInstanceId.setStatus("current")
_CucsEtherLossStatsHistDn_Type = CucsManagedObjectDn
_CucsEtherLossStatsHistDn_Object = MibTableColumn
cucsEtherLossStatsHistDn = _CucsEtherLossStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 2),
    _CucsEtherLossStatsHistDn_Type()
)
cucsEtherLossStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistDn.setStatus("current")
_CucsEtherLossStatsHistRn_Type = SnmpAdminString
_CucsEtherLossStatsHistRn_Object = MibTableColumn
cucsEtherLossStatsHistRn = _CucsEtherLossStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 3),
    _CucsEtherLossStatsHistRn_Type()
)
cucsEtherLossStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistRn.setStatus("current")
_CucsEtherLossStatsHistSQETest_Type = Unsigned64
_CucsEtherLossStatsHistSQETest_Object = MibTableColumn
cucsEtherLossStatsHistSQETest = _CucsEtherLossStatsHistSQETest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 4),
    _CucsEtherLossStatsHistSQETest_Type()
)
cucsEtherLossStatsHistSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSQETest.setStatus("current")
_CucsEtherLossStatsHistSQETestDelta_Type = Unsigned64
_CucsEtherLossStatsHistSQETestDelta_Object = MibTableColumn
cucsEtherLossStatsHistSQETestDelta = _CucsEtherLossStatsHistSQETestDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 5),
    _CucsEtherLossStatsHistSQETestDelta_Type()
)
cucsEtherLossStatsHistSQETestDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSQETestDelta.setStatus("current")
_CucsEtherLossStatsHistSQETestDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistSQETestDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistSQETestDeltaAvg = _CucsEtherLossStatsHistSQETestDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 6),
    _CucsEtherLossStatsHistSQETestDeltaAvg_Type()
)
cucsEtherLossStatsHistSQETestDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSQETestDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistSQETestDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistSQETestDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistSQETestDeltaMax = _CucsEtherLossStatsHistSQETestDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 7),
    _CucsEtherLossStatsHistSQETestDeltaMax_Type()
)
cucsEtherLossStatsHistSQETestDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSQETestDeltaMax.setStatus("current")
_CucsEtherLossStatsHistSQETestDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistSQETestDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistSQETestDeltaMin = _CucsEtherLossStatsHistSQETestDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 8),
    _CucsEtherLossStatsHistSQETestDeltaMin_Type()
)
cucsEtherLossStatsHistSQETestDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSQETestDeltaMin.setStatus("current")
_CucsEtherLossStatsHistCarrierSense_Type = Unsigned64
_CucsEtherLossStatsHistCarrierSense_Object = MibTableColumn
cucsEtherLossStatsHistCarrierSense = _CucsEtherLossStatsHistCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 9),
    _CucsEtherLossStatsHistCarrierSense_Type()
)
cucsEtherLossStatsHistCarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistCarrierSense.setStatus("current")
_CucsEtherLossStatsHistCarrierSenseDelta_Type = Unsigned64
_CucsEtherLossStatsHistCarrierSenseDelta_Object = MibTableColumn
cucsEtherLossStatsHistCarrierSenseDelta = _CucsEtherLossStatsHistCarrierSenseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 10),
    _CucsEtherLossStatsHistCarrierSenseDelta_Type()
)
cucsEtherLossStatsHistCarrierSenseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistCarrierSenseDelta.setStatus("current")
_CucsEtherLossStatsHistCarrierSenseDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistCarrierSenseDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistCarrierSenseDeltaAvg = _CucsEtherLossStatsHistCarrierSenseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 11),
    _CucsEtherLossStatsHistCarrierSenseDeltaAvg_Type()
)
cucsEtherLossStatsHistCarrierSenseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistCarrierSenseDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistCarrierSenseDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistCarrierSenseDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistCarrierSenseDeltaMax = _CucsEtherLossStatsHistCarrierSenseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 12),
    _CucsEtherLossStatsHistCarrierSenseDeltaMax_Type()
)
cucsEtherLossStatsHistCarrierSenseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistCarrierSenseDeltaMax.setStatus("current")
_CucsEtherLossStatsHistCarrierSenseDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistCarrierSenseDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistCarrierSenseDeltaMin = _CucsEtherLossStatsHistCarrierSenseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 13),
    _CucsEtherLossStatsHistCarrierSenseDeltaMin_Type()
)
cucsEtherLossStatsHistCarrierSenseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistCarrierSenseDeltaMin.setStatus("current")
_CucsEtherLossStatsHistExcessCollision_Type = Unsigned64
_CucsEtherLossStatsHistExcessCollision_Object = MibTableColumn
cucsEtherLossStatsHistExcessCollision = _CucsEtherLossStatsHistExcessCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 14),
    _CucsEtherLossStatsHistExcessCollision_Type()
)
cucsEtherLossStatsHistExcessCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistExcessCollision.setStatus("current")
_CucsEtherLossStatsHistExcessCollisionDelta_Type = Unsigned64
_CucsEtherLossStatsHistExcessCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsHistExcessCollisionDelta = _CucsEtherLossStatsHistExcessCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 15),
    _CucsEtherLossStatsHistExcessCollisionDelta_Type()
)
cucsEtherLossStatsHistExcessCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistExcessCollisionDelta.setStatus("current")
_CucsEtherLossStatsHistExcessCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistExcessCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistExcessCollisionDeltaAvg = _CucsEtherLossStatsHistExcessCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 16),
    _CucsEtherLossStatsHistExcessCollisionDeltaAvg_Type()
)
cucsEtherLossStatsHistExcessCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistExcessCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistExcessCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistExcessCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistExcessCollisionDeltaMax = _CucsEtherLossStatsHistExcessCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 17),
    _CucsEtherLossStatsHistExcessCollisionDeltaMax_Type()
)
cucsEtherLossStatsHistExcessCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistExcessCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsHistExcessCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistExcessCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistExcessCollisionDeltaMin = _CucsEtherLossStatsHistExcessCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 18),
    _CucsEtherLossStatsHistExcessCollisionDeltaMin_Type()
)
cucsEtherLossStatsHistExcessCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistExcessCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsHistGiants_Type = Unsigned64
_CucsEtherLossStatsHistGiants_Object = MibTableColumn
cucsEtherLossStatsHistGiants = _CucsEtherLossStatsHistGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 19),
    _CucsEtherLossStatsHistGiants_Type()
)
cucsEtherLossStatsHistGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistGiants.setStatus("current")
_CucsEtherLossStatsHistGiantsDelta_Type = Unsigned64
_CucsEtherLossStatsHistGiantsDelta_Object = MibTableColumn
cucsEtherLossStatsHistGiantsDelta = _CucsEtherLossStatsHistGiantsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 20),
    _CucsEtherLossStatsHistGiantsDelta_Type()
)
cucsEtherLossStatsHistGiantsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistGiantsDelta.setStatus("current")
_CucsEtherLossStatsHistGiantsDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistGiantsDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistGiantsDeltaAvg = _CucsEtherLossStatsHistGiantsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 21),
    _CucsEtherLossStatsHistGiantsDeltaAvg_Type()
)
cucsEtherLossStatsHistGiantsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistGiantsDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistGiantsDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistGiantsDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistGiantsDeltaMax = _CucsEtherLossStatsHistGiantsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 22),
    _CucsEtherLossStatsHistGiantsDeltaMax_Type()
)
cucsEtherLossStatsHistGiantsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistGiantsDeltaMax.setStatus("current")
_CucsEtherLossStatsHistGiantsDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistGiantsDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistGiantsDeltaMin = _CucsEtherLossStatsHistGiantsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 23),
    _CucsEtherLossStatsHistGiantsDeltaMin_Type()
)
cucsEtherLossStatsHistGiantsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistGiantsDeltaMin.setStatus("current")
_CucsEtherLossStatsHistId_Type = Unsigned64
_CucsEtherLossStatsHistId_Object = MibTableColumn
cucsEtherLossStatsHistId = _CucsEtherLossStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 24),
    _CucsEtherLossStatsHistId_Type()
)
cucsEtherLossStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistId.setStatus("current")
_CucsEtherLossStatsHistLateCollision_Type = Unsigned64
_CucsEtherLossStatsHistLateCollision_Object = MibTableColumn
cucsEtherLossStatsHistLateCollision = _CucsEtherLossStatsHistLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 25),
    _CucsEtherLossStatsHistLateCollision_Type()
)
cucsEtherLossStatsHistLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistLateCollision.setStatus("current")
_CucsEtherLossStatsHistLateCollisionDelta_Type = Unsigned64
_CucsEtherLossStatsHistLateCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsHistLateCollisionDelta = _CucsEtherLossStatsHistLateCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 26),
    _CucsEtherLossStatsHistLateCollisionDelta_Type()
)
cucsEtherLossStatsHistLateCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistLateCollisionDelta.setStatus("current")
_CucsEtherLossStatsHistLateCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistLateCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistLateCollisionDeltaAvg = _CucsEtherLossStatsHistLateCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 27),
    _CucsEtherLossStatsHistLateCollisionDeltaAvg_Type()
)
cucsEtherLossStatsHistLateCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistLateCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistLateCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistLateCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistLateCollisionDeltaMax = _CucsEtherLossStatsHistLateCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 28),
    _CucsEtherLossStatsHistLateCollisionDeltaMax_Type()
)
cucsEtherLossStatsHistLateCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistLateCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsHistLateCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistLateCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistLateCollisionDeltaMin = _CucsEtherLossStatsHistLateCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 29),
    _CucsEtherLossStatsHistLateCollisionDeltaMin_Type()
)
cucsEtherLossStatsHistLateCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistLateCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsHistMostRecent_Type = TruthValue
_CucsEtherLossStatsHistMostRecent_Object = MibTableColumn
cucsEtherLossStatsHistMostRecent = _CucsEtherLossStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 30),
    _CucsEtherLossStatsHistMostRecent_Type()
)
cucsEtherLossStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistMostRecent.setStatus("current")
_CucsEtherLossStatsHistMultiCollision_Type = Unsigned64
_CucsEtherLossStatsHistMultiCollision_Object = MibTableColumn
cucsEtherLossStatsHistMultiCollision = _CucsEtherLossStatsHistMultiCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 31),
    _CucsEtherLossStatsHistMultiCollision_Type()
)
cucsEtherLossStatsHistMultiCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistMultiCollision.setStatus("current")
_CucsEtherLossStatsHistMultiCollisionDelta_Type = Unsigned64
_CucsEtherLossStatsHistMultiCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsHistMultiCollisionDelta = _CucsEtherLossStatsHistMultiCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 32),
    _CucsEtherLossStatsHistMultiCollisionDelta_Type()
)
cucsEtherLossStatsHistMultiCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistMultiCollisionDelta.setStatus("current")
_CucsEtherLossStatsHistMultiCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistMultiCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistMultiCollisionDeltaAvg = _CucsEtherLossStatsHistMultiCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 33),
    _CucsEtherLossStatsHistMultiCollisionDeltaAvg_Type()
)
cucsEtherLossStatsHistMultiCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistMultiCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistMultiCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistMultiCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistMultiCollisionDeltaMax = _CucsEtherLossStatsHistMultiCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 34),
    _CucsEtherLossStatsHistMultiCollisionDeltaMax_Type()
)
cucsEtherLossStatsHistMultiCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistMultiCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsHistMultiCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistMultiCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistMultiCollisionDeltaMin = _CucsEtherLossStatsHistMultiCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 35),
    _CucsEtherLossStatsHistMultiCollisionDeltaMin_Type()
)
cucsEtherLossStatsHistMultiCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistMultiCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsHistSingleCollision_Type = Unsigned64
_CucsEtherLossStatsHistSingleCollision_Object = MibTableColumn
cucsEtherLossStatsHistSingleCollision = _CucsEtherLossStatsHistSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 36),
    _CucsEtherLossStatsHistSingleCollision_Type()
)
cucsEtherLossStatsHistSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSingleCollision.setStatus("current")
_CucsEtherLossStatsHistSingleCollisionDelta_Type = Unsigned64
_CucsEtherLossStatsHistSingleCollisionDelta_Object = MibTableColumn
cucsEtherLossStatsHistSingleCollisionDelta = _CucsEtherLossStatsHistSingleCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 37),
    _CucsEtherLossStatsHistSingleCollisionDelta_Type()
)
cucsEtherLossStatsHistSingleCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSingleCollisionDelta.setStatus("current")
_CucsEtherLossStatsHistSingleCollisionDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistSingleCollisionDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistSingleCollisionDeltaAvg = _CucsEtherLossStatsHistSingleCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 38),
    _CucsEtherLossStatsHistSingleCollisionDeltaAvg_Type()
)
cucsEtherLossStatsHistSingleCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSingleCollisionDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistSingleCollisionDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistSingleCollisionDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistSingleCollisionDeltaMax = _CucsEtherLossStatsHistSingleCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 39),
    _CucsEtherLossStatsHistSingleCollisionDeltaMax_Type()
)
cucsEtherLossStatsHistSingleCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSingleCollisionDeltaMax.setStatus("current")
_CucsEtherLossStatsHistSingleCollisionDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistSingleCollisionDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistSingleCollisionDeltaMin = _CucsEtherLossStatsHistSingleCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 40),
    _CucsEtherLossStatsHistSingleCollisionDeltaMin_Type()
)
cucsEtherLossStatsHistSingleCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSingleCollisionDeltaMin.setStatus("current")
_CucsEtherLossStatsHistSuspect_Type = TruthValue
_CucsEtherLossStatsHistSuspect_Object = MibTableColumn
cucsEtherLossStatsHistSuspect = _CucsEtherLossStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 41),
    _CucsEtherLossStatsHistSuspect_Type()
)
cucsEtherLossStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSuspect.setStatus("current")
_CucsEtherLossStatsHistSymbol_Type = Unsigned64
_CucsEtherLossStatsHistSymbol_Object = MibTableColumn
cucsEtherLossStatsHistSymbol = _CucsEtherLossStatsHistSymbol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 42),
    _CucsEtherLossStatsHistSymbol_Type()
)
cucsEtherLossStatsHistSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSymbol.setStatus("current")
_CucsEtherLossStatsHistSymbolDelta_Type = Unsigned64
_CucsEtherLossStatsHistSymbolDelta_Object = MibTableColumn
cucsEtherLossStatsHistSymbolDelta = _CucsEtherLossStatsHistSymbolDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 43),
    _CucsEtherLossStatsHistSymbolDelta_Type()
)
cucsEtherLossStatsHistSymbolDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSymbolDelta.setStatus("current")
_CucsEtherLossStatsHistSymbolDeltaAvg_Type = Unsigned64
_CucsEtherLossStatsHistSymbolDeltaAvg_Object = MibTableColumn
cucsEtherLossStatsHistSymbolDeltaAvg = _CucsEtherLossStatsHistSymbolDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 44),
    _CucsEtherLossStatsHistSymbolDeltaAvg_Type()
)
cucsEtherLossStatsHistSymbolDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSymbolDeltaAvg.setStatus("current")
_CucsEtherLossStatsHistSymbolDeltaMax_Type = Unsigned64
_CucsEtherLossStatsHistSymbolDeltaMax_Object = MibTableColumn
cucsEtherLossStatsHistSymbolDeltaMax = _CucsEtherLossStatsHistSymbolDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 45),
    _CucsEtherLossStatsHistSymbolDeltaMax_Type()
)
cucsEtherLossStatsHistSymbolDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSymbolDeltaMax.setStatus("current")
_CucsEtherLossStatsHistSymbolDeltaMin_Type = Unsigned64
_CucsEtherLossStatsHistSymbolDeltaMin_Object = MibTableColumn
cucsEtherLossStatsHistSymbolDeltaMin = _CucsEtherLossStatsHistSymbolDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 46),
    _CucsEtherLossStatsHistSymbolDeltaMin_Type()
)
cucsEtherLossStatsHistSymbolDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistSymbolDeltaMin.setStatus("current")
_CucsEtherLossStatsHistThresholded_Type = CucsEtherLossStatsHistThresholded
_CucsEtherLossStatsHistThresholded_Object = MibTableColumn
cucsEtherLossStatsHistThresholded = _CucsEtherLossStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 47),
    _CucsEtherLossStatsHistThresholded_Type()
)
cucsEtherLossStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistThresholded.setStatus("current")
_CucsEtherLossStatsHistTimeCollected_Type = DateAndTime
_CucsEtherLossStatsHistTimeCollected_Object = MibTableColumn
cucsEtherLossStatsHistTimeCollected = _CucsEtherLossStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 4, 1, 48),
    _CucsEtherLossStatsHistTimeCollected_Type()
)
cucsEtherLossStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherLossStatsHistTimeCollected.setStatus("current")
_CucsEtherNicIfConfigTable_Object = MibTable
cucsEtherNicIfConfigTable = _CucsEtherNicIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 5)
)
if mibBuilder.loadTexts:
    cucsEtherNicIfConfigTable.setStatus("current")
_CucsEtherNicIfConfigEntry_Object = MibTableRow
cucsEtherNicIfConfigEntry = _CucsEtherNicIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 5, 1)
)
cucsEtherNicIfConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherNicIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherNicIfConfigEntry.setStatus("current")
_CucsEtherNicIfConfigInstanceId_Type = CucsManagedObjectId
_CucsEtherNicIfConfigInstanceId_Object = MibTableColumn
cucsEtherNicIfConfigInstanceId = _CucsEtherNicIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 5, 1, 1),
    _CucsEtherNicIfConfigInstanceId_Type()
)
cucsEtherNicIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherNicIfConfigInstanceId.setStatus("current")
_CucsEtherNicIfConfigDn_Type = CucsManagedObjectDn
_CucsEtherNicIfConfigDn_Object = MibTableColumn
cucsEtherNicIfConfigDn = _CucsEtherNicIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 5, 1, 2),
    _CucsEtherNicIfConfigDn_Type()
)
cucsEtherNicIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNicIfConfigDn.setStatus("current")
_CucsEtherNicIfConfigRn_Type = SnmpAdminString
_CucsEtherNicIfConfigRn_Object = MibTableColumn
cucsEtherNicIfConfigRn = _CucsEtherNicIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 5, 1, 3),
    _CucsEtherNicIfConfigRn_Type()
)
cucsEtherNicIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNicIfConfigRn.setStatus("current")
_CucsEtherPIoTable_Object = MibTable
cucsEtherPIoTable = _CucsEtherPIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6)
)
if mibBuilder.loadTexts:
    cucsEtherPIoTable.setStatus("current")
_CucsEtherPIoEntry_Object = MibTableRow
cucsEtherPIoEntry = _CucsEtherPIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1)
)
cucsEtherPIoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPIoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPIoEntry.setStatus("current")
_CucsEtherPIoInstanceId_Type = CucsManagedObjectId
_CucsEtherPIoInstanceId_Object = MibTableColumn
cucsEtherPIoInstanceId = _CucsEtherPIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 1),
    _CucsEtherPIoInstanceId_Type()
)
cucsEtherPIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPIoInstanceId.setStatus("current")
_CucsEtherPIoDn_Type = CucsManagedObjectDn
_CucsEtherPIoDn_Object = MibTableColumn
cucsEtherPIoDn = _CucsEtherPIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 2),
    _CucsEtherPIoDn_Type()
)
cucsEtherPIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoDn.setStatus("current")
_CucsEtherPIoRn_Type = SnmpAdminString
_CucsEtherPIoRn_Object = MibTableColumn
cucsEtherPIoRn = _CucsEtherPIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 3),
    _CucsEtherPIoRn_Type()
)
cucsEtherPIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoRn.setStatus("current")
_CucsEtherPIoAdminState_Type = CucsFabricAdminState
_CucsEtherPIoAdminState_Object = MibTableColumn
cucsEtherPIoAdminState = _CucsEtherPIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 4),
    _CucsEtherPIoAdminState_Type()
)
cucsEtherPIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoAdminState.setStatus("current")
_CucsEtherPIoChassisId_Type = Gauge32
_CucsEtherPIoChassisId_Object = MibTableColumn
cucsEtherPIoChassisId = _CucsEtherPIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 5),
    _CucsEtherPIoChassisId_Type()
)
cucsEtherPIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoChassisId.setStatus("current")
_CucsEtherPIoEncap_Type = CucsPortEncap
_CucsEtherPIoEncap_Object = MibTableColumn
cucsEtherPIoEncap = _CucsEtherPIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 6),
    _CucsEtherPIoEncap_Type()
)
cucsEtherPIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoEncap.setStatus("current")
_CucsEtherPIoEpDn_Type = SnmpAdminString
_CucsEtherPIoEpDn_Object = MibTableColumn
cucsEtherPIoEpDn = _CucsEtherPIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 7),
    _CucsEtherPIoEpDn_Type()
)
cucsEtherPIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoEpDn.setStatus("current")
_CucsEtherPIoFltAggr_Type = Unsigned64
_CucsEtherPIoFltAggr_Object = MibTableColumn
cucsEtherPIoFltAggr = _CucsEtherPIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 8),
    _CucsEtherPIoFltAggr_Type()
)
cucsEtherPIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFltAggr.setStatus("current")
_CucsEtherPIoIfRole_Type = CucsNetworkPortRole
_CucsEtherPIoIfRole_Object = MibTableColumn
cucsEtherPIoIfRole = _CucsEtherPIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 9),
    _CucsEtherPIoIfRole_Type()
)
cucsEtherPIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoIfRole.setStatus("current")
_CucsEtherPIoIfType_Type = CucsNetworkPhysEpIfType
_CucsEtherPIoIfType_Object = MibTableColumn
cucsEtherPIoIfType = _CucsEtherPIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 10),
    _CucsEtherPIoIfType_Type()
)
cucsEtherPIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoIfType.setStatus("current")
_CucsEtherPIoLocale_Type = CucsNetworkLocale
_CucsEtherPIoLocale_Object = MibTableColumn
cucsEtherPIoLocale = _CucsEtherPIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 11),
    _CucsEtherPIoLocale_Type()
)
cucsEtherPIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoLocale.setStatus("current")
_CucsEtherPIoMac_Type = MacAddress
_CucsEtherPIoMac_Object = MibTableColumn
cucsEtherPIoMac = _CucsEtherPIoMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 12),
    _CucsEtherPIoMac_Type()
)
cucsEtherPIoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoMac.setStatus("current")
_CucsEtherPIoMode_Type = CucsPortMode
_CucsEtherPIoMode_Object = MibTableColumn
cucsEtherPIoMode = _CucsEtherPIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 13),
    _CucsEtherPIoMode_Type()
)
cucsEtherPIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoMode.setStatus("current")
_CucsEtherPIoModel_Type = SnmpAdminString
_CucsEtherPIoModel_Object = MibTableColumn
cucsEtherPIoModel = _CucsEtherPIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 14),
    _CucsEtherPIoModel_Type()
)
cucsEtherPIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoModel.setStatus("current")
_CucsEtherPIoName_Type = SnmpAdminString
_CucsEtherPIoName_Object = MibTableColumn
cucsEtherPIoName = _CucsEtherPIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 15),
    _CucsEtherPIoName_Type()
)
cucsEtherPIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoName.setStatus("current")
_CucsEtherPIoOperSpeed_Type = CucsPortEthSpeed
_CucsEtherPIoOperSpeed_Object = MibTableColumn
cucsEtherPIoOperSpeed = _CucsEtherPIoOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 16),
    _CucsEtherPIoOperSpeed_Type()
)
cucsEtherPIoOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoOperSpeed.setStatus("current")
_CucsEtherPIoOperState_Type = CucsNetworkPortOperState
_CucsEtherPIoOperState_Object = MibTableColumn
cucsEtherPIoOperState = _CucsEtherPIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 17),
    _CucsEtherPIoOperState_Type()
)
cucsEtherPIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoOperState.setStatus("current")
_CucsEtherPIoPeerDn_Type = SnmpAdminString
_CucsEtherPIoPeerDn_Object = MibTableColumn
cucsEtherPIoPeerDn = _CucsEtherPIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 18),
    _CucsEtherPIoPeerDn_Type()
)
cucsEtherPIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoPeerDn.setStatus("current")
_CucsEtherPIoPeerPortId_Type = Gauge32
_CucsEtherPIoPeerPortId_Object = MibTableColumn
cucsEtherPIoPeerPortId = _CucsEtherPIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 19),
    _CucsEtherPIoPeerPortId_Type()
)
cucsEtherPIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoPeerPortId.setStatus("current")
_CucsEtherPIoPeerSlotId_Type = Gauge32
_CucsEtherPIoPeerSlotId_Object = MibTableColumn
cucsEtherPIoPeerSlotId = _CucsEtherPIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 20),
    _CucsEtherPIoPeerSlotId_Type()
)
cucsEtherPIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoPeerSlotId.setStatus("current")
_CucsEtherPIoPortId_Type = Gauge32
_CucsEtherPIoPortId_Object = MibTableColumn
cucsEtherPIoPortId = _CucsEtherPIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 21),
    _CucsEtherPIoPortId_Type()
)
cucsEtherPIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoPortId.setStatus("current")
_CucsEtherPIoRevision_Type = SnmpAdminString
_CucsEtherPIoRevision_Object = MibTableColumn
cucsEtherPIoRevision = _CucsEtherPIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 22),
    _CucsEtherPIoRevision_Type()
)
cucsEtherPIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoRevision.setStatus("current")
_CucsEtherPIoSerial_Type = SnmpAdminString
_CucsEtherPIoSerial_Object = MibTableColumn
cucsEtherPIoSerial = _CucsEtherPIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 23),
    _CucsEtherPIoSerial_Type()
)
cucsEtherPIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoSerial.setStatus("current")
_CucsEtherPIoSlotId_Type = Gauge32
_CucsEtherPIoSlotId_Object = MibTableColumn
cucsEtherPIoSlotId = _CucsEtherPIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 24),
    _CucsEtherPIoSlotId_Type()
)
cucsEtherPIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoSlotId.setStatus("current")
_CucsEtherPIoStateQual_Type = SnmpAdminString
_CucsEtherPIoStateQual_Object = MibTableColumn
cucsEtherPIoStateQual = _CucsEtherPIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 25),
    _CucsEtherPIoStateQual_Type()
)
cucsEtherPIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoStateQual.setStatus("current")
_CucsEtherPIoSwitchId_Type = CucsNetworkSwitchId
_CucsEtherPIoSwitchId_Object = MibTableColumn
cucsEtherPIoSwitchId = _CucsEtherPIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 26),
    _CucsEtherPIoSwitchId_Type()
)
cucsEtherPIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoSwitchId.setStatus("current")
_CucsEtherPIoTransport_Type = CucsNetworkTransport
_CucsEtherPIoTransport_Object = MibTableColumn
cucsEtherPIoTransport = _CucsEtherPIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 27),
    _CucsEtherPIoTransport_Type()
)
cucsEtherPIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoTransport.setStatus("current")
_CucsEtherPIoTs_Type = DateAndTime
_CucsEtherPIoTs_Object = MibTableColumn
cucsEtherPIoTs = _CucsEtherPIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 28),
    _CucsEtherPIoTs_Type()
)
cucsEtherPIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoTs.setStatus("current")
_CucsEtherPIoType_Type = CucsNetworkConnectionType
_CucsEtherPIoType_Object = MibTableColumn
cucsEtherPIoType = _CucsEtherPIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 29),
    _CucsEtherPIoType_Type()
)
cucsEtherPIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoType.setStatus("current")
_CucsEtherPIoUsrLbl_Type = SnmpAdminString
_CucsEtherPIoUsrLbl_Object = MibTableColumn
cucsEtherPIoUsrLbl = _CucsEtherPIoUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 30),
    _CucsEtherPIoUsrLbl_Type()
)
cucsEtherPIoUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoUsrLbl.setStatus("current")
_CucsEtherPIoVendor_Type = SnmpAdminString
_CucsEtherPIoVendor_Object = MibTableColumn
cucsEtherPIoVendor = _CucsEtherPIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 31),
    _CucsEtherPIoVendor_Type()
)
cucsEtherPIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoVendor.setStatus("current")
_CucsEtherPIoFsmDescr_Type = SnmpAdminString
_CucsEtherPIoFsmDescr_Object = MibTableColumn
cucsEtherPIoFsmDescr = _CucsEtherPIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 32),
    _CucsEtherPIoFsmDescr_Type()
)
cucsEtherPIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmDescr.setStatus("current")
_CucsEtherPIoFsmPrev_Type = SnmpAdminString
_CucsEtherPIoFsmPrev_Object = MibTableColumn
cucsEtherPIoFsmPrev = _CucsEtherPIoFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 33),
    _CucsEtherPIoFsmPrev_Type()
)
cucsEtherPIoFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmPrev.setStatus("current")
_CucsEtherPIoFsmProgr_Type = Gauge32
_CucsEtherPIoFsmProgr_Object = MibTableColumn
cucsEtherPIoFsmProgr = _CucsEtherPIoFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 34),
    _CucsEtherPIoFsmProgr_Type()
)
cucsEtherPIoFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmProgr.setStatus("current")
_CucsEtherPIoFsmRmtInvErrCode_Type = Gauge32
_CucsEtherPIoFsmRmtInvErrCode_Object = MibTableColumn
cucsEtherPIoFsmRmtInvErrCode = _CucsEtherPIoFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 35),
    _CucsEtherPIoFsmRmtInvErrCode_Type()
)
cucsEtherPIoFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmRmtInvErrCode.setStatus("current")
_CucsEtherPIoFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsEtherPIoFsmRmtInvErrDescr_Object = MibTableColumn
cucsEtherPIoFsmRmtInvErrDescr = _CucsEtherPIoFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 36),
    _CucsEtherPIoFsmRmtInvErrDescr_Type()
)
cucsEtherPIoFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmRmtInvErrDescr.setStatus("current")
_CucsEtherPIoFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsEtherPIoFsmRmtInvRslt_Object = MibTableColumn
cucsEtherPIoFsmRmtInvRslt = _CucsEtherPIoFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 37),
    _CucsEtherPIoFsmRmtInvRslt_Type()
)
cucsEtherPIoFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmRmtInvRslt.setStatus("current")
_CucsEtherPIoFsmStageDescr_Type = SnmpAdminString
_CucsEtherPIoFsmStageDescr_Object = MibTableColumn
cucsEtherPIoFsmStageDescr = _CucsEtherPIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 38),
    _CucsEtherPIoFsmStageDescr_Type()
)
cucsEtherPIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageDescr.setStatus("current")
_CucsEtherPIoFsmStamp_Type = DateAndTime
_CucsEtherPIoFsmStamp_Object = MibTableColumn
cucsEtherPIoFsmStamp = _CucsEtherPIoFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 39),
    _CucsEtherPIoFsmStamp_Type()
)
cucsEtherPIoFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStamp.setStatus("current")
_CucsEtherPIoFsmStatus_Type = SnmpAdminString
_CucsEtherPIoFsmStatus_Object = MibTableColumn
cucsEtherPIoFsmStatus = _CucsEtherPIoFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 40),
    _CucsEtherPIoFsmStatus_Type()
)
cucsEtherPIoFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStatus.setStatus("current")
_CucsEtherPIoFsmTry_Type = Gauge32
_CucsEtherPIoFsmTry_Object = MibTableColumn
cucsEtherPIoFsmTry = _CucsEtherPIoFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 41),
    _CucsEtherPIoFsmTry_Type()
)
cucsEtherPIoFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmTry.setStatus("current")
_CucsEtherPIoLicGP_Type = Unsigned64
_CucsEtherPIoLicGP_Object = MibTableColumn
cucsEtherPIoLicGP = _CucsEtherPIoLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 42),
    _CucsEtherPIoLicGP_Type()
)
cucsEtherPIoLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoLicGP.setStatus("current")
_CucsEtherPIoLicState_Type = CucsLicenseState
_CucsEtherPIoLicState_Object = MibTableColumn
cucsEtherPIoLicState = _CucsEtherPIoLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 43),
    _CucsEtherPIoLicState_Type()
)
cucsEtherPIoLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoLicState.setStatus("current")
_CucsEtherPIoXcvrType_Type = CucsEquipmentXcvrType
_CucsEtherPIoXcvrType_Object = MibTableColumn
cucsEtherPIoXcvrType = _CucsEtherPIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 44),
    _CucsEtherPIoXcvrType_Type()
)
cucsEtherPIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoXcvrType.setStatus("current")
_CucsEtherPIoPeerChassisId_Type = Gauge32
_CucsEtherPIoPeerChassisId_Object = MibTableColumn
cucsEtherPIoPeerChassisId = _CucsEtherPIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 45),
    _CucsEtherPIoPeerChassisId_Type()
)
cucsEtherPIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoPeerChassisId.setStatus("current")
_CucsEtherPIoAdminTransport_Type = CucsNetworkTransport
_CucsEtherPIoAdminTransport_Object = MibTableColumn
cucsEtherPIoAdminTransport = _CucsEtherPIoAdminTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 46),
    _CucsEtherPIoAdminTransport_Type()
)
cucsEtherPIoAdminTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoAdminTransport.setStatus("current")
_CucsEtherPIoLc_Type = CucsFsmLifecycle
_CucsEtherPIoLc_Object = MibTableColumn
cucsEtherPIoLc = _CucsEtherPIoLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 47),
    _CucsEtherPIoLc_Type()
)
cucsEtherPIoLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoLc.setStatus("current")
_CucsEtherPIoUnifiedPort_Type = TruthValue
_CucsEtherPIoUnifiedPort_Object = MibTableColumn
cucsEtherPIoUnifiedPort = _CucsEtherPIoUnifiedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 48),
    _CucsEtherPIoUnifiedPort_Type()
)
cucsEtherPIoUnifiedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoUnifiedPort.setStatus("current")
_CucsEtherPIoIsPortChannelMember_Type = TruthValue
_CucsEtherPIoIsPortChannelMember_Object = MibTableColumn
cucsEtherPIoIsPortChannelMember = _CucsEtherPIoIsPortChannelMember_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 49),
    _CucsEtherPIoIsPortChannelMember_Type()
)
cucsEtherPIoIsPortChannelMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoIsPortChannelMember.setStatus("current")
_CucsEtherPIoAggrPortId_Type = Gauge32
_CucsEtherPIoAggrPortId_Object = MibTableColumn
cucsEtherPIoAggrPortId = _CucsEtherPIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 50),
    _CucsEtherPIoAggrPortId_Type()
)
cucsEtherPIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoAggrPortId.setStatus("current")
_CucsEtherPIoPeerAggrPortId_Type = Gauge32
_CucsEtherPIoPeerAggrPortId_Object = MibTableColumn
cucsEtherPIoPeerAggrPortId = _CucsEtherPIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 51),
    _CucsEtherPIoPeerAggrPortId_Type()
)
cucsEtherPIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoPeerAggrPortId.setStatus("current")
_CucsEtherPIoNonCR4_Type = TruthValue
_CucsEtherPIoNonCR4_Object = MibTableColumn
cucsEtherPIoNonCR4 = _CucsEtherPIoNonCR4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 6, 1, 52),
    _CucsEtherPIoNonCR4_Type()
)
cucsEtherPIoNonCR4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoNonCR4.setStatus("current")
_CucsEtherPauseStatsTable_Object = MibTable
cucsEtherPauseStatsTable = _CucsEtherPauseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7)
)
if mibBuilder.loadTexts:
    cucsEtherPauseStatsTable.setStatus("current")
_CucsEtherPauseStatsEntry_Object = MibTableRow
cucsEtherPauseStatsEntry = _CucsEtherPauseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1)
)
cucsEtherPauseStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPauseStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPauseStatsEntry.setStatus("current")
_CucsEtherPauseStatsInstanceId_Type = CucsManagedObjectId
_CucsEtherPauseStatsInstanceId_Object = MibTableColumn
cucsEtherPauseStatsInstanceId = _CucsEtherPauseStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 1),
    _CucsEtherPauseStatsInstanceId_Type()
)
cucsEtherPauseStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsInstanceId.setStatus("current")
_CucsEtherPauseStatsDn_Type = CucsManagedObjectDn
_CucsEtherPauseStatsDn_Object = MibTableColumn
cucsEtherPauseStatsDn = _CucsEtherPauseStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 2),
    _CucsEtherPauseStatsDn_Type()
)
cucsEtherPauseStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsDn.setStatus("current")
_CucsEtherPauseStatsRn_Type = SnmpAdminString
_CucsEtherPauseStatsRn_Object = MibTableColumn
cucsEtherPauseStatsRn = _CucsEtherPauseStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 3),
    _CucsEtherPauseStatsRn_Type()
)
cucsEtherPauseStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsRn.setStatus("current")
_CucsEtherPauseStatsIntervals_Type = Gauge32
_CucsEtherPauseStatsIntervals_Object = MibTableColumn
cucsEtherPauseStatsIntervals = _CucsEtherPauseStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 4),
    _CucsEtherPauseStatsIntervals_Type()
)
cucsEtherPauseStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsIntervals.setStatus("current")
_CucsEtherPauseStatsRecvPause_Type = Unsigned64
_CucsEtherPauseStatsRecvPause_Object = MibTableColumn
cucsEtherPauseStatsRecvPause = _CucsEtherPauseStatsRecvPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 5),
    _CucsEtherPauseStatsRecvPause_Type()
)
cucsEtherPauseStatsRecvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsRecvPause.setStatus("current")
_CucsEtherPauseStatsRecvPauseDelta_Type = Counter64
_CucsEtherPauseStatsRecvPauseDelta_Object = MibTableColumn
cucsEtherPauseStatsRecvPauseDelta = _CucsEtherPauseStatsRecvPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 6),
    _CucsEtherPauseStatsRecvPauseDelta_Type()
)
cucsEtherPauseStatsRecvPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsRecvPauseDelta.setStatus("current")
_CucsEtherPauseStatsRecvPauseDeltaAvg_Type = Unsigned64
_CucsEtherPauseStatsRecvPauseDeltaAvg_Object = MibTableColumn
cucsEtherPauseStatsRecvPauseDeltaAvg = _CucsEtherPauseStatsRecvPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 7),
    _CucsEtherPauseStatsRecvPauseDeltaAvg_Type()
)
cucsEtherPauseStatsRecvPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsRecvPauseDeltaAvg.setStatus("current")
_CucsEtherPauseStatsRecvPauseDeltaMax_Type = Unsigned64
_CucsEtherPauseStatsRecvPauseDeltaMax_Object = MibTableColumn
cucsEtherPauseStatsRecvPauseDeltaMax = _CucsEtherPauseStatsRecvPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 8),
    _CucsEtherPauseStatsRecvPauseDeltaMax_Type()
)
cucsEtherPauseStatsRecvPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsRecvPauseDeltaMax.setStatus("current")
_CucsEtherPauseStatsRecvPauseDeltaMin_Type = Unsigned64
_CucsEtherPauseStatsRecvPauseDeltaMin_Object = MibTableColumn
cucsEtherPauseStatsRecvPauseDeltaMin = _CucsEtherPauseStatsRecvPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 9),
    _CucsEtherPauseStatsRecvPauseDeltaMin_Type()
)
cucsEtherPauseStatsRecvPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsRecvPauseDeltaMin.setStatus("current")
_CucsEtherPauseStatsResets_Type = Unsigned64
_CucsEtherPauseStatsResets_Object = MibTableColumn
cucsEtherPauseStatsResets = _CucsEtherPauseStatsResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 10),
    _CucsEtherPauseStatsResets_Type()
)
cucsEtherPauseStatsResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsResets.setStatus("current")
_CucsEtherPauseStatsResetsDelta_Type = Counter64
_CucsEtherPauseStatsResetsDelta_Object = MibTableColumn
cucsEtherPauseStatsResetsDelta = _CucsEtherPauseStatsResetsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 11),
    _CucsEtherPauseStatsResetsDelta_Type()
)
cucsEtherPauseStatsResetsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsResetsDelta.setStatus("current")
_CucsEtherPauseStatsResetsDeltaAvg_Type = Unsigned64
_CucsEtherPauseStatsResetsDeltaAvg_Object = MibTableColumn
cucsEtherPauseStatsResetsDeltaAvg = _CucsEtherPauseStatsResetsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 12),
    _CucsEtherPauseStatsResetsDeltaAvg_Type()
)
cucsEtherPauseStatsResetsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsResetsDeltaAvg.setStatus("current")
_CucsEtherPauseStatsResetsDeltaMax_Type = Unsigned64
_CucsEtherPauseStatsResetsDeltaMax_Object = MibTableColumn
cucsEtherPauseStatsResetsDeltaMax = _CucsEtherPauseStatsResetsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 13),
    _CucsEtherPauseStatsResetsDeltaMax_Type()
)
cucsEtherPauseStatsResetsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsResetsDeltaMax.setStatus("current")
_CucsEtherPauseStatsResetsDeltaMin_Type = Unsigned64
_CucsEtherPauseStatsResetsDeltaMin_Object = MibTableColumn
cucsEtherPauseStatsResetsDeltaMin = _CucsEtherPauseStatsResetsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 14),
    _CucsEtherPauseStatsResetsDeltaMin_Type()
)
cucsEtherPauseStatsResetsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsResetsDeltaMin.setStatus("current")
_CucsEtherPauseStatsSuspect_Type = TruthValue
_CucsEtherPauseStatsSuspect_Object = MibTableColumn
cucsEtherPauseStatsSuspect = _CucsEtherPauseStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 15),
    _CucsEtherPauseStatsSuspect_Type()
)
cucsEtherPauseStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsSuspect.setStatus("current")
_CucsEtherPauseStatsThresholded_Type = CucsEtherPauseStatsThresholded
_CucsEtherPauseStatsThresholded_Object = MibTableColumn
cucsEtherPauseStatsThresholded = _CucsEtherPauseStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 16),
    _CucsEtherPauseStatsThresholded_Type()
)
cucsEtherPauseStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsThresholded.setStatus("current")
_CucsEtherPauseStatsTimeCollected_Type = DateAndTime
_CucsEtherPauseStatsTimeCollected_Object = MibTableColumn
cucsEtherPauseStatsTimeCollected = _CucsEtherPauseStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 17),
    _CucsEtherPauseStatsTimeCollected_Type()
)
cucsEtherPauseStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsTimeCollected.setStatus("current")
_CucsEtherPauseStatsUpdate_Type = Gauge32
_CucsEtherPauseStatsUpdate_Object = MibTableColumn
cucsEtherPauseStatsUpdate = _CucsEtherPauseStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 18),
    _CucsEtherPauseStatsUpdate_Type()
)
cucsEtherPauseStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsUpdate.setStatus("current")
_CucsEtherPauseStatsXmitPause_Type = Unsigned64
_CucsEtherPauseStatsXmitPause_Object = MibTableColumn
cucsEtherPauseStatsXmitPause = _CucsEtherPauseStatsXmitPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 19),
    _CucsEtherPauseStatsXmitPause_Type()
)
cucsEtherPauseStatsXmitPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsXmitPause.setStatus("current")
_CucsEtherPauseStatsXmitPauseDelta_Type = Counter64
_CucsEtherPauseStatsXmitPauseDelta_Object = MibTableColumn
cucsEtherPauseStatsXmitPauseDelta = _CucsEtherPauseStatsXmitPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 20),
    _CucsEtherPauseStatsXmitPauseDelta_Type()
)
cucsEtherPauseStatsXmitPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsXmitPauseDelta.setStatus("current")
_CucsEtherPauseStatsXmitPauseDeltaAvg_Type = Unsigned64
_CucsEtherPauseStatsXmitPauseDeltaAvg_Object = MibTableColumn
cucsEtherPauseStatsXmitPauseDeltaAvg = _CucsEtherPauseStatsXmitPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 21),
    _CucsEtherPauseStatsXmitPauseDeltaAvg_Type()
)
cucsEtherPauseStatsXmitPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsXmitPauseDeltaAvg.setStatus("current")
_CucsEtherPauseStatsXmitPauseDeltaMax_Type = Unsigned64
_CucsEtherPauseStatsXmitPauseDeltaMax_Object = MibTableColumn
cucsEtherPauseStatsXmitPauseDeltaMax = _CucsEtherPauseStatsXmitPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 22),
    _CucsEtherPauseStatsXmitPauseDeltaMax_Type()
)
cucsEtherPauseStatsXmitPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsXmitPauseDeltaMax.setStatus("current")
_CucsEtherPauseStatsXmitPauseDeltaMin_Type = Unsigned64
_CucsEtherPauseStatsXmitPauseDeltaMin_Object = MibTableColumn
cucsEtherPauseStatsXmitPauseDeltaMin = _CucsEtherPauseStatsXmitPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 7, 1, 23),
    _CucsEtherPauseStatsXmitPauseDeltaMin_Type()
)
cucsEtherPauseStatsXmitPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsXmitPauseDeltaMin.setStatus("current")
_CucsEtherPauseStatsHistTable_Object = MibTable
cucsEtherPauseStatsHistTable = _CucsEtherPauseStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8)
)
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistTable.setStatus("current")
_CucsEtherPauseStatsHistEntry_Object = MibTableRow
cucsEtherPauseStatsHistEntry = _CucsEtherPauseStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1)
)
cucsEtherPauseStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPauseStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistEntry.setStatus("current")
_CucsEtherPauseStatsHistInstanceId_Type = CucsManagedObjectId
_CucsEtherPauseStatsHistInstanceId_Object = MibTableColumn
cucsEtherPauseStatsHistInstanceId = _CucsEtherPauseStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 1),
    _CucsEtherPauseStatsHistInstanceId_Type()
)
cucsEtherPauseStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistInstanceId.setStatus("current")
_CucsEtherPauseStatsHistDn_Type = CucsManagedObjectDn
_CucsEtherPauseStatsHistDn_Object = MibTableColumn
cucsEtherPauseStatsHistDn = _CucsEtherPauseStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 2),
    _CucsEtherPauseStatsHistDn_Type()
)
cucsEtherPauseStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistDn.setStatus("current")
_CucsEtherPauseStatsHistRn_Type = SnmpAdminString
_CucsEtherPauseStatsHistRn_Object = MibTableColumn
cucsEtherPauseStatsHistRn = _CucsEtherPauseStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 3),
    _CucsEtherPauseStatsHistRn_Type()
)
cucsEtherPauseStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistRn.setStatus("current")
_CucsEtherPauseStatsHistId_Type = Unsigned64
_CucsEtherPauseStatsHistId_Object = MibTableColumn
cucsEtherPauseStatsHistId = _CucsEtherPauseStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 4),
    _CucsEtherPauseStatsHistId_Type()
)
cucsEtherPauseStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistId.setStatus("current")
_CucsEtherPauseStatsHistMostRecent_Type = TruthValue
_CucsEtherPauseStatsHistMostRecent_Object = MibTableColumn
cucsEtherPauseStatsHistMostRecent = _CucsEtherPauseStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 5),
    _CucsEtherPauseStatsHistMostRecent_Type()
)
cucsEtherPauseStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistMostRecent.setStatus("current")
_CucsEtherPauseStatsHistRecvPause_Type = Unsigned64
_CucsEtherPauseStatsHistRecvPause_Object = MibTableColumn
cucsEtherPauseStatsHistRecvPause = _CucsEtherPauseStatsHistRecvPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 6),
    _CucsEtherPauseStatsHistRecvPause_Type()
)
cucsEtherPauseStatsHistRecvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistRecvPause.setStatus("current")
_CucsEtherPauseStatsHistRecvPauseDelta_Type = Unsigned64
_CucsEtherPauseStatsHistRecvPauseDelta_Object = MibTableColumn
cucsEtherPauseStatsHistRecvPauseDelta = _CucsEtherPauseStatsHistRecvPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 7),
    _CucsEtherPauseStatsHistRecvPauseDelta_Type()
)
cucsEtherPauseStatsHistRecvPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistRecvPauseDelta.setStatus("current")
_CucsEtherPauseStatsHistRecvPauseDeltaAvg_Type = Unsigned64
_CucsEtherPauseStatsHistRecvPauseDeltaAvg_Object = MibTableColumn
cucsEtherPauseStatsHistRecvPauseDeltaAvg = _CucsEtherPauseStatsHistRecvPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 8),
    _CucsEtherPauseStatsHistRecvPauseDeltaAvg_Type()
)
cucsEtherPauseStatsHistRecvPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistRecvPauseDeltaAvg.setStatus("current")
_CucsEtherPauseStatsHistRecvPauseDeltaMax_Type = Unsigned64
_CucsEtherPauseStatsHistRecvPauseDeltaMax_Object = MibTableColumn
cucsEtherPauseStatsHistRecvPauseDeltaMax = _CucsEtherPauseStatsHistRecvPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 9),
    _CucsEtherPauseStatsHistRecvPauseDeltaMax_Type()
)
cucsEtherPauseStatsHistRecvPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistRecvPauseDeltaMax.setStatus("current")
_CucsEtherPauseStatsHistRecvPauseDeltaMin_Type = Unsigned64
_CucsEtherPauseStatsHistRecvPauseDeltaMin_Object = MibTableColumn
cucsEtherPauseStatsHistRecvPauseDeltaMin = _CucsEtherPauseStatsHistRecvPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 10),
    _CucsEtherPauseStatsHistRecvPauseDeltaMin_Type()
)
cucsEtherPauseStatsHistRecvPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistRecvPauseDeltaMin.setStatus("current")
_CucsEtherPauseStatsHistResets_Type = Unsigned64
_CucsEtherPauseStatsHistResets_Object = MibTableColumn
cucsEtherPauseStatsHistResets = _CucsEtherPauseStatsHistResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 11),
    _CucsEtherPauseStatsHistResets_Type()
)
cucsEtherPauseStatsHistResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistResets.setStatus("current")
_CucsEtherPauseStatsHistResetsDelta_Type = Unsigned64
_CucsEtherPauseStatsHistResetsDelta_Object = MibTableColumn
cucsEtherPauseStatsHistResetsDelta = _CucsEtherPauseStatsHistResetsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 12),
    _CucsEtherPauseStatsHistResetsDelta_Type()
)
cucsEtherPauseStatsHistResetsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistResetsDelta.setStatus("current")
_CucsEtherPauseStatsHistResetsDeltaAvg_Type = Unsigned64
_CucsEtherPauseStatsHistResetsDeltaAvg_Object = MibTableColumn
cucsEtherPauseStatsHistResetsDeltaAvg = _CucsEtherPauseStatsHistResetsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 13),
    _CucsEtherPauseStatsHistResetsDeltaAvg_Type()
)
cucsEtherPauseStatsHistResetsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistResetsDeltaAvg.setStatus("current")
_CucsEtherPauseStatsHistResetsDeltaMax_Type = Unsigned64
_CucsEtherPauseStatsHistResetsDeltaMax_Object = MibTableColumn
cucsEtherPauseStatsHistResetsDeltaMax = _CucsEtherPauseStatsHistResetsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 14),
    _CucsEtherPauseStatsHistResetsDeltaMax_Type()
)
cucsEtherPauseStatsHistResetsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistResetsDeltaMax.setStatus("current")
_CucsEtherPauseStatsHistResetsDeltaMin_Type = Unsigned64
_CucsEtherPauseStatsHistResetsDeltaMin_Object = MibTableColumn
cucsEtherPauseStatsHistResetsDeltaMin = _CucsEtherPauseStatsHistResetsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 15),
    _CucsEtherPauseStatsHistResetsDeltaMin_Type()
)
cucsEtherPauseStatsHistResetsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistResetsDeltaMin.setStatus("current")
_CucsEtherPauseStatsHistSuspect_Type = TruthValue
_CucsEtherPauseStatsHistSuspect_Object = MibTableColumn
cucsEtherPauseStatsHistSuspect = _CucsEtherPauseStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 16),
    _CucsEtherPauseStatsHistSuspect_Type()
)
cucsEtherPauseStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistSuspect.setStatus("current")
_CucsEtherPauseStatsHistThresholded_Type = CucsEtherPauseStatsHistThresholded
_CucsEtherPauseStatsHistThresholded_Object = MibTableColumn
cucsEtherPauseStatsHistThresholded = _CucsEtherPauseStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 17),
    _CucsEtherPauseStatsHistThresholded_Type()
)
cucsEtherPauseStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistThresholded.setStatus("current")
_CucsEtherPauseStatsHistTimeCollected_Type = DateAndTime
_CucsEtherPauseStatsHistTimeCollected_Object = MibTableColumn
cucsEtherPauseStatsHistTimeCollected = _CucsEtherPauseStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 18),
    _CucsEtherPauseStatsHistTimeCollected_Type()
)
cucsEtherPauseStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistTimeCollected.setStatus("current")
_CucsEtherPauseStatsHistXmitPause_Type = Unsigned64
_CucsEtherPauseStatsHistXmitPause_Object = MibTableColumn
cucsEtherPauseStatsHistXmitPause = _CucsEtherPauseStatsHistXmitPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 19),
    _CucsEtherPauseStatsHistXmitPause_Type()
)
cucsEtherPauseStatsHistXmitPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistXmitPause.setStatus("current")
_CucsEtherPauseStatsHistXmitPauseDelta_Type = Unsigned64
_CucsEtherPauseStatsHistXmitPauseDelta_Object = MibTableColumn
cucsEtherPauseStatsHistXmitPauseDelta = _CucsEtherPauseStatsHistXmitPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 20),
    _CucsEtherPauseStatsHistXmitPauseDelta_Type()
)
cucsEtherPauseStatsHistXmitPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistXmitPauseDelta.setStatus("current")
_CucsEtherPauseStatsHistXmitPauseDeltaAvg_Type = Unsigned64
_CucsEtherPauseStatsHistXmitPauseDeltaAvg_Object = MibTableColumn
cucsEtherPauseStatsHistXmitPauseDeltaAvg = _CucsEtherPauseStatsHistXmitPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 21),
    _CucsEtherPauseStatsHistXmitPauseDeltaAvg_Type()
)
cucsEtherPauseStatsHistXmitPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistXmitPauseDeltaAvg.setStatus("current")
_CucsEtherPauseStatsHistXmitPauseDeltaMax_Type = Unsigned64
_CucsEtherPauseStatsHistXmitPauseDeltaMax_Object = MibTableColumn
cucsEtherPauseStatsHistXmitPauseDeltaMax = _CucsEtherPauseStatsHistXmitPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 22),
    _CucsEtherPauseStatsHistXmitPauseDeltaMax_Type()
)
cucsEtherPauseStatsHistXmitPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistXmitPauseDeltaMax.setStatus("current")
_CucsEtherPauseStatsHistXmitPauseDeltaMin_Type = Unsigned64
_CucsEtherPauseStatsHistXmitPauseDeltaMin_Object = MibTableColumn
cucsEtherPauseStatsHistXmitPauseDeltaMin = _CucsEtherPauseStatsHistXmitPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 8, 1, 23),
    _CucsEtherPauseStatsHistXmitPauseDeltaMin_Type()
)
cucsEtherPauseStatsHistXmitPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPauseStatsHistXmitPauseDeltaMin.setStatus("current")
_CucsEtherRxStatsTable_Object = MibTable
cucsEtherRxStatsTable = _CucsEtherRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9)
)
if mibBuilder.loadTexts:
    cucsEtherRxStatsTable.setStatus("current")
_CucsEtherRxStatsEntry_Object = MibTableRow
cucsEtherRxStatsEntry = _CucsEtherRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1)
)
cucsEtherRxStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherRxStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherRxStatsEntry.setStatus("current")
_CucsEtherRxStatsInstanceId_Type = CucsManagedObjectId
_CucsEtherRxStatsInstanceId_Object = MibTableColumn
cucsEtherRxStatsInstanceId = _CucsEtherRxStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 1),
    _CucsEtherRxStatsInstanceId_Type()
)
cucsEtherRxStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherRxStatsInstanceId.setStatus("current")
_CucsEtherRxStatsDn_Type = CucsManagedObjectDn
_CucsEtherRxStatsDn_Object = MibTableColumn
cucsEtherRxStatsDn = _CucsEtherRxStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 2),
    _CucsEtherRxStatsDn_Type()
)
cucsEtherRxStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsDn.setStatus("current")
_CucsEtherRxStatsRn_Type = SnmpAdminString
_CucsEtherRxStatsRn_Object = MibTableColumn
cucsEtherRxStatsRn = _CucsEtherRxStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 3),
    _CucsEtherRxStatsRn_Type()
)
cucsEtherRxStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsRn.setStatus("current")
_CucsEtherRxStatsBroadcastPackets_Type = Unsigned64
_CucsEtherRxStatsBroadcastPackets_Object = MibTableColumn
cucsEtherRxStatsBroadcastPackets = _CucsEtherRxStatsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 4),
    _CucsEtherRxStatsBroadcastPackets_Type()
)
cucsEtherRxStatsBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsBroadcastPackets.setStatus("current")
_CucsEtherRxStatsBroadcastPacketsDelta_Type = Counter64
_CucsEtherRxStatsBroadcastPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsBroadcastPacketsDelta = _CucsEtherRxStatsBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 5),
    _CucsEtherRxStatsBroadcastPacketsDelta_Type()
)
cucsEtherRxStatsBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsBroadcastPacketsDelta.setStatus("current")
_CucsEtherRxStatsBroadcastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsBroadcastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsBroadcastPacketsDeltaAvg = _CucsEtherRxStatsBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 6),
    _CucsEtherRxStatsBroadcastPacketsDeltaAvg_Type()
)
cucsEtherRxStatsBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsBroadcastPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsBroadcastPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsBroadcastPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsBroadcastPacketsDeltaMax = _CucsEtherRxStatsBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 7),
    _CucsEtherRxStatsBroadcastPacketsDeltaMax_Type()
)
cucsEtherRxStatsBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsBroadcastPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsBroadcastPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsBroadcastPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsBroadcastPacketsDeltaMin = _CucsEtherRxStatsBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 8),
    _CucsEtherRxStatsBroadcastPacketsDeltaMin_Type()
)
cucsEtherRxStatsBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsBroadcastPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsIntervals_Type = Gauge32
_CucsEtherRxStatsIntervals_Object = MibTableColumn
cucsEtherRxStatsIntervals = _CucsEtherRxStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 9),
    _CucsEtherRxStatsIntervals_Type()
)
cucsEtherRxStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsIntervals.setStatus("current")
_CucsEtherRxStatsJumboPackets_Type = Unsigned64
_CucsEtherRxStatsJumboPackets_Object = MibTableColumn
cucsEtherRxStatsJumboPackets = _CucsEtherRxStatsJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 10),
    _CucsEtherRxStatsJumboPackets_Type()
)
cucsEtherRxStatsJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsJumboPackets.setStatus("current")
_CucsEtherRxStatsJumboPacketsDelta_Type = Counter64
_CucsEtherRxStatsJumboPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsJumboPacketsDelta = _CucsEtherRxStatsJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 11),
    _CucsEtherRxStatsJumboPacketsDelta_Type()
)
cucsEtherRxStatsJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsJumboPacketsDelta.setStatus("current")
_CucsEtherRxStatsJumboPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsJumboPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsJumboPacketsDeltaAvg = _CucsEtherRxStatsJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 12),
    _CucsEtherRxStatsJumboPacketsDeltaAvg_Type()
)
cucsEtherRxStatsJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsJumboPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsJumboPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsJumboPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsJumboPacketsDeltaMax = _CucsEtherRxStatsJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 13),
    _CucsEtherRxStatsJumboPacketsDeltaMax_Type()
)
cucsEtherRxStatsJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsJumboPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsJumboPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsJumboPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsJumboPacketsDeltaMin = _CucsEtherRxStatsJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 14),
    _CucsEtherRxStatsJumboPacketsDeltaMin_Type()
)
cucsEtherRxStatsJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsJumboPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsMulticastPackets_Type = Unsigned64
_CucsEtherRxStatsMulticastPackets_Object = MibTableColumn
cucsEtherRxStatsMulticastPackets = _CucsEtherRxStatsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 15),
    _CucsEtherRxStatsMulticastPackets_Type()
)
cucsEtherRxStatsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsMulticastPackets.setStatus("current")
_CucsEtherRxStatsMulticastPacketsDelta_Type = Counter64
_CucsEtherRxStatsMulticastPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsMulticastPacketsDelta = _CucsEtherRxStatsMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 16),
    _CucsEtherRxStatsMulticastPacketsDelta_Type()
)
cucsEtherRxStatsMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsMulticastPacketsDelta.setStatus("current")
_CucsEtherRxStatsMulticastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsMulticastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsMulticastPacketsDeltaAvg = _CucsEtherRxStatsMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 17),
    _CucsEtherRxStatsMulticastPacketsDeltaAvg_Type()
)
cucsEtherRxStatsMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsMulticastPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsMulticastPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsMulticastPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsMulticastPacketsDeltaMax = _CucsEtherRxStatsMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 18),
    _CucsEtherRxStatsMulticastPacketsDeltaMax_Type()
)
cucsEtherRxStatsMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsMulticastPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsMulticastPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsMulticastPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsMulticastPacketsDeltaMin = _CucsEtherRxStatsMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 19),
    _CucsEtherRxStatsMulticastPacketsDeltaMin_Type()
)
cucsEtherRxStatsMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsMulticastPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsSuspect_Type = TruthValue
_CucsEtherRxStatsSuspect_Object = MibTableColumn
cucsEtherRxStatsSuspect = _CucsEtherRxStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 20),
    _CucsEtherRxStatsSuspect_Type()
)
cucsEtherRxStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsSuspect.setStatus("current")
_CucsEtherRxStatsThresholded_Type = CucsEtherRxStatsThresholded
_CucsEtherRxStatsThresholded_Object = MibTableColumn
cucsEtherRxStatsThresholded = _CucsEtherRxStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 21),
    _CucsEtherRxStatsThresholded_Type()
)
cucsEtherRxStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsThresholded.setStatus("current")
_CucsEtherRxStatsTimeCollected_Type = DateAndTime
_CucsEtherRxStatsTimeCollected_Object = MibTableColumn
cucsEtherRxStatsTimeCollected = _CucsEtherRxStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 22),
    _CucsEtherRxStatsTimeCollected_Type()
)
cucsEtherRxStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTimeCollected.setStatus("current")
_CucsEtherRxStatsTotalBytes_Type = Unsigned64
_CucsEtherRxStatsTotalBytes_Object = MibTableColumn
cucsEtherRxStatsTotalBytes = _CucsEtherRxStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 23),
    _CucsEtherRxStatsTotalBytes_Type()
)
cucsEtherRxStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalBytes.setStatus("current")
_CucsEtherRxStatsTotalBytesDelta_Type = Counter64
_CucsEtherRxStatsTotalBytesDelta_Object = MibTableColumn
cucsEtherRxStatsTotalBytesDelta = _CucsEtherRxStatsTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 24),
    _CucsEtherRxStatsTotalBytesDelta_Type()
)
cucsEtherRxStatsTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalBytesDelta.setStatus("current")
_CucsEtherRxStatsTotalBytesDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsTotalBytesDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsTotalBytesDeltaAvg = _CucsEtherRxStatsTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 25),
    _CucsEtherRxStatsTotalBytesDeltaAvg_Type()
)
cucsEtherRxStatsTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalBytesDeltaAvg.setStatus("current")
_CucsEtherRxStatsTotalBytesDeltaMax_Type = Unsigned64
_CucsEtherRxStatsTotalBytesDeltaMax_Object = MibTableColumn
cucsEtherRxStatsTotalBytesDeltaMax = _CucsEtherRxStatsTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 26),
    _CucsEtherRxStatsTotalBytesDeltaMax_Type()
)
cucsEtherRxStatsTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalBytesDeltaMax.setStatus("current")
_CucsEtherRxStatsTotalBytesDeltaMin_Type = Unsigned64
_CucsEtherRxStatsTotalBytesDeltaMin_Object = MibTableColumn
cucsEtherRxStatsTotalBytesDeltaMin = _CucsEtherRxStatsTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 27),
    _CucsEtherRxStatsTotalBytesDeltaMin_Type()
)
cucsEtherRxStatsTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalBytesDeltaMin.setStatus("current")
_CucsEtherRxStatsTotalPackets_Type = Unsigned64
_CucsEtherRxStatsTotalPackets_Object = MibTableColumn
cucsEtherRxStatsTotalPackets = _CucsEtherRxStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 28),
    _CucsEtherRxStatsTotalPackets_Type()
)
cucsEtherRxStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalPackets.setStatus("current")
_CucsEtherRxStatsTotalPacketsDelta_Type = Counter64
_CucsEtherRxStatsTotalPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsTotalPacketsDelta = _CucsEtherRxStatsTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 29),
    _CucsEtherRxStatsTotalPacketsDelta_Type()
)
cucsEtherRxStatsTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalPacketsDelta.setStatus("current")
_CucsEtherRxStatsTotalPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsTotalPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsTotalPacketsDeltaAvg = _CucsEtherRxStatsTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 30),
    _CucsEtherRxStatsTotalPacketsDeltaAvg_Type()
)
cucsEtherRxStatsTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsTotalPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsTotalPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsTotalPacketsDeltaMax = _CucsEtherRxStatsTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 31),
    _CucsEtherRxStatsTotalPacketsDeltaMax_Type()
)
cucsEtherRxStatsTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsTotalPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsTotalPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsTotalPacketsDeltaMin = _CucsEtherRxStatsTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 32),
    _CucsEtherRxStatsTotalPacketsDeltaMin_Type()
)
cucsEtherRxStatsTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsTotalPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsUnicastPackets_Type = Unsigned64
_CucsEtherRxStatsUnicastPackets_Object = MibTableColumn
cucsEtherRxStatsUnicastPackets = _CucsEtherRxStatsUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 33),
    _CucsEtherRxStatsUnicastPackets_Type()
)
cucsEtherRxStatsUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsUnicastPackets.setStatus("current")
_CucsEtherRxStatsUnicastPacketsDelta_Type = Counter64
_CucsEtherRxStatsUnicastPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsUnicastPacketsDelta = _CucsEtherRxStatsUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 34),
    _CucsEtherRxStatsUnicastPacketsDelta_Type()
)
cucsEtherRxStatsUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsUnicastPacketsDelta.setStatus("current")
_CucsEtherRxStatsUnicastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsUnicastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsUnicastPacketsDeltaAvg = _CucsEtherRxStatsUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 35),
    _CucsEtherRxStatsUnicastPacketsDeltaAvg_Type()
)
cucsEtherRxStatsUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsUnicastPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsUnicastPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsUnicastPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsUnicastPacketsDeltaMax = _CucsEtherRxStatsUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 36),
    _CucsEtherRxStatsUnicastPacketsDeltaMax_Type()
)
cucsEtherRxStatsUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsUnicastPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsUnicastPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsUnicastPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsUnicastPacketsDeltaMin = _CucsEtherRxStatsUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 37),
    _CucsEtherRxStatsUnicastPacketsDeltaMin_Type()
)
cucsEtherRxStatsUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsUnicastPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsUpdate_Type = Gauge32
_CucsEtherRxStatsUpdate_Object = MibTableColumn
cucsEtherRxStatsUpdate = _CucsEtherRxStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 9, 1, 38),
    _CucsEtherRxStatsUpdate_Type()
)
cucsEtherRxStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsUpdate.setStatus("current")
_CucsEtherRxStatsHistTable_Object = MibTable
cucsEtherRxStatsHistTable = _CucsEtherRxStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10)
)
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTable.setStatus("current")
_CucsEtherRxStatsHistEntry_Object = MibTableRow
cucsEtherRxStatsHistEntry = _CucsEtherRxStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1)
)
cucsEtherRxStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherRxStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistEntry.setStatus("current")
_CucsEtherRxStatsHistInstanceId_Type = CucsManagedObjectId
_CucsEtherRxStatsHistInstanceId_Object = MibTableColumn
cucsEtherRxStatsHistInstanceId = _CucsEtherRxStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 1),
    _CucsEtherRxStatsHistInstanceId_Type()
)
cucsEtherRxStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistInstanceId.setStatus("current")
_CucsEtherRxStatsHistDn_Type = CucsManagedObjectDn
_CucsEtherRxStatsHistDn_Object = MibTableColumn
cucsEtherRxStatsHistDn = _CucsEtherRxStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 2),
    _CucsEtherRxStatsHistDn_Type()
)
cucsEtherRxStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistDn.setStatus("current")
_CucsEtherRxStatsHistRn_Type = SnmpAdminString
_CucsEtherRxStatsHistRn_Object = MibTableColumn
cucsEtherRxStatsHistRn = _CucsEtherRxStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 3),
    _CucsEtherRxStatsHistRn_Type()
)
cucsEtherRxStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistRn.setStatus("current")
_CucsEtherRxStatsHistBroadcastPackets_Type = Unsigned64
_CucsEtherRxStatsHistBroadcastPackets_Object = MibTableColumn
cucsEtherRxStatsHistBroadcastPackets = _CucsEtherRxStatsHistBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 4),
    _CucsEtherRxStatsHistBroadcastPackets_Type()
)
cucsEtherRxStatsHistBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistBroadcastPackets.setStatus("current")
_CucsEtherRxStatsHistBroadcastPacketsDelta_Type = Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDelta = _CucsEtherRxStatsHistBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 5),
    _CucsEtherRxStatsHistBroadcastPacketsDelta_Type()
)
cucsEtherRxStatsHistBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistBroadcastPacketsDelta.setStatus("current")
_CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDeltaAvg = _CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 6),
    _CucsEtherRxStatsHistBroadcastPacketsDeltaAvg_Type()
)
cucsEtherRxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistBroadcastPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDeltaMax = _CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 7),
    _CucsEtherRxStatsHistBroadcastPacketsDeltaMax_Type()
)
cucsEtherRxStatsHistBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistBroadcastPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsHistBroadcastPacketsDeltaMin = _CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 8),
    _CucsEtherRxStatsHistBroadcastPacketsDeltaMin_Type()
)
cucsEtherRxStatsHistBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistBroadcastPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsHistId_Type = Unsigned64
_CucsEtherRxStatsHistId_Object = MibTableColumn
cucsEtherRxStatsHistId = _CucsEtherRxStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 9),
    _CucsEtherRxStatsHistId_Type()
)
cucsEtherRxStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistId.setStatus("current")
_CucsEtherRxStatsHistJumboPackets_Type = Unsigned64
_CucsEtherRxStatsHistJumboPackets_Object = MibTableColumn
cucsEtherRxStatsHistJumboPackets = _CucsEtherRxStatsHistJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 10),
    _CucsEtherRxStatsHistJumboPackets_Type()
)
cucsEtherRxStatsHistJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistJumboPackets.setStatus("current")
_CucsEtherRxStatsHistJumboPacketsDelta_Type = Unsigned64
_CucsEtherRxStatsHistJumboPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsHistJumboPacketsDelta = _CucsEtherRxStatsHistJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 11),
    _CucsEtherRxStatsHistJumboPacketsDelta_Type()
)
cucsEtherRxStatsHistJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistJumboPacketsDelta.setStatus("current")
_CucsEtherRxStatsHistJumboPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsHistJumboPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsHistJumboPacketsDeltaAvg = _CucsEtherRxStatsHistJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 12),
    _CucsEtherRxStatsHistJumboPacketsDeltaAvg_Type()
)
cucsEtherRxStatsHistJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistJumboPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsHistJumboPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsHistJumboPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsHistJumboPacketsDeltaMax = _CucsEtherRxStatsHistJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 13),
    _CucsEtherRxStatsHistJumboPacketsDeltaMax_Type()
)
cucsEtherRxStatsHistJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistJumboPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsHistJumboPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsHistJumboPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsHistJumboPacketsDeltaMin = _CucsEtherRxStatsHistJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 14),
    _CucsEtherRxStatsHistJumboPacketsDeltaMin_Type()
)
cucsEtherRxStatsHistJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistJumboPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsHistMostRecent_Type = TruthValue
_CucsEtherRxStatsHistMostRecent_Object = MibTableColumn
cucsEtherRxStatsHistMostRecent = _CucsEtherRxStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 15),
    _CucsEtherRxStatsHistMostRecent_Type()
)
cucsEtherRxStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistMostRecent.setStatus("current")
_CucsEtherRxStatsHistMulticastPackets_Type = Unsigned64
_CucsEtherRxStatsHistMulticastPackets_Object = MibTableColumn
cucsEtherRxStatsHistMulticastPackets = _CucsEtherRxStatsHistMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 16),
    _CucsEtherRxStatsHistMulticastPackets_Type()
)
cucsEtherRxStatsHistMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistMulticastPackets.setStatus("current")
_CucsEtherRxStatsHistMulticastPacketsDelta_Type = Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDelta = _CucsEtherRxStatsHistMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 17),
    _CucsEtherRxStatsHistMulticastPacketsDelta_Type()
)
cucsEtherRxStatsHistMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistMulticastPacketsDelta.setStatus("current")
_CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDeltaAvg = _CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 18),
    _CucsEtherRxStatsHistMulticastPacketsDeltaAvg_Type()
)
cucsEtherRxStatsHistMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistMulticastPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsHistMulticastPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDeltaMax = _CucsEtherRxStatsHistMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 19),
    _CucsEtherRxStatsHistMulticastPacketsDeltaMax_Type()
)
cucsEtherRxStatsHistMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistMulticastPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsHistMulticastPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsHistMulticastPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsHistMulticastPacketsDeltaMin = _CucsEtherRxStatsHistMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 20),
    _CucsEtherRxStatsHistMulticastPacketsDeltaMin_Type()
)
cucsEtherRxStatsHistMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistMulticastPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsHistSuspect_Type = TruthValue
_CucsEtherRxStatsHistSuspect_Object = MibTableColumn
cucsEtherRxStatsHistSuspect = _CucsEtherRxStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 21),
    _CucsEtherRxStatsHistSuspect_Type()
)
cucsEtherRxStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistSuspect.setStatus("current")
_CucsEtherRxStatsHistThresholded_Type = CucsEtherRxStatsHistThresholded
_CucsEtherRxStatsHistThresholded_Object = MibTableColumn
cucsEtherRxStatsHistThresholded = _CucsEtherRxStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 22),
    _CucsEtherRxStatsHistThresholded_Type()
)
cucsEtherRxStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistThresholded.setStatus("current")
_CucsEtherRxStatsHistTimeCollected_Type = DateAndTime
_CucsEtherRxStatsHistTimeCollected_Object = MibTableColumn
cucsEtherRxStatsHistTimeCollected = _CucsEtherRxStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 23),
    _CucsEtherRxStatsHistTimeCollected_Type()
)
cucsEtherRxStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTimeCollected.setStatus("current")
_CucsEtherRxStatsHistTotalBytes_Type = Unsigned64
_CucsEtherRxStatsHistTotalBytes_Object = MibTableColumn
cucsEtherRxStatsHistTotalBytes = _CucsEtherRxStatsHistTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 24),
    _CucsEtherRxStatsHistTotalBytes_Type()
)
cucsEtherRxStatsHistTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalBytes.setStatus("current")
_CucsEtherRxStatsHistTotalBytesDelta_Type = Unsigned64
_CucsEtherRxStatsHistTotalBytesDelta_Object = MibTableColumn
cucsEtherRxStatsHistTotalBytesDelta = _CucsEtherRxStatsHistTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 25),
    _CucsEtherRxStatsHistTotalBytesDelta_Type()
)
cucsEtherRxStatsHistTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalBytesDelta.setStatus("current")
_CucsEtherRxStatsHistTotalBytesDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsHistTotalBytesDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsHistTotalBytesDeltaAvg = _CucsEtherRxStatsHistTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 26),
    _CucsEtherRxStatsHistTotalBytesDeltaAvg_Type()
)
cucsEtherRxStatsHistTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalBytesDeltaAvg.setStatus("current")
_CucsEtherRxStatsHistTotalBytesDeltaMax_Type = Unsigned64
_CucsEtherRxStatsHistTotalBytesDeltaMax_Object = MibTableColumn
cucsEtherRxStatsHistTotalBytesDeltaMax = _CucsEtherRxStatsHistTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 27),
    _CucsEtherRxStatsHistTotalBytesDeltaMax_Type()
)
cucsEtherRxStatsHistTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalBytesDeltaMax.setStatus("current")
_CucsEtherRxStatsHistTotalBytesDeltaMin_Type = Unsigned64
_CucsEtherRxStatsHistTotalBytesDeltaMin_Object = MibTableColumn
cucsEtherRxStatsHistTotalBytesDeltaMin = _CucsEtherRxStatsHistTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 28),
    _CucsEtherRxStatsHistTotalBytesDeltaMin_Type()
)
cucsEtherRxStatsHistTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalBytesDeltaMin.setStatus("current")
_CucsEtherRxStatsHistTotalPackets_Type = Unsigned64
_CucsEtherRxStatsHistTotalPackets_Object = MibTableColumn
cucsEtherRxStatsHistTotalPackets = _CucsEtherRxStatsHistTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 29),
    _CucsEtherRxStatsHistTotalPackets_Type()
)
cucsEtherRxStatsHistTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalPackets.setStatus("current")
_CucsEtherRxStatsHistTotalPacketsDelta_Type = Unsigned64
_CucsEtherRxStatsHistTotalPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsHistTotalPacketsDelta = _CucsEtherRxStatsHistTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 30),
    _CucsEtherRxStatsHistTotalPacketsDelta_Type()
)
cucsEtherRxStatsHistTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalPacketsDelta.setStatus("current")
_CucsEtherRxStatsHistTotalPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsHistTotalPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsHistTotalPacketsDeltaAvg = _CucsEtherRxStatsHistTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 31),
    _CucsEtherRxStatsHistTotalPacketsDeltaAvg_Type()
)
cucsEtherRxStatsHistTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsHistTotalPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsHistTotalPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsHistTotalPacketsDeltaMax = _CucsEtherRxStatsHistTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 32),
    _CucsEtherRxStatsHistTotalPacketsDeltaMax_Type()
)
cucsEtherRxStatsHistTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsHistTotalPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsHistTotalPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsHistTotalPacketsDeltaMin = _CucsEtherRxStatsHistTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 33),
    _CucsEtherRxStatsHistTotalPacketsDeltaMin_Type()
)
cucsEtherRxStatsHistTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistTotalPacketsDeltaMin.setStatus("current")
_CucsEtherRxStatsHistUnicastPackets_Type = Unsigned64
_CucsEtherRxStatsHistUnicastPackets_Object = MibTableColumn
cucsEtherRxStatsHistUnicastPackets = _CucsEtherRxStatsHistUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 34),
    _CucsEtherRxStatsHistUnicastPackets_Type()
)
cucsEtherRxStatsHistUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistUnicastPackets.setStatus("current")
_CucsEtherRxStatsHistUnicastPacketsDelta_Type = Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDelta_Object = MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDelta = _CucsEtherRxStatsHistUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 35),
    _CucsEtherRxStatsHistUnicastPacketsDelta_Type()
)
cucsEtherRxStatsHistUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistUnicastPacketsDelta.setStatus("current")
_CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDeltaAvg = _CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 36),
    _CucsEtherRxStatsHistUnicastPacketsDeltaAvg_Type()
)
cucsEtherRxStatsHistUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistUnicastPacketsDeltaAvg.setStatus("current")
_CucsEtherRxStatsHistUnicastPacketsDeltaMax_Type = Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDeltaMax_Object = MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDeltaMax = _CucsEtherRxStatsHistUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 37),
    _CucsEtherRxStatsHistUnicastPacketsDeltaMax_Type()
)
cucsEtherRxStatsHistUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistUnicastPacketsDeltaMax.setStatus("current")
_CucsEtherRxStatsHistUnicastPacketsDeltaMin_Type = Unsigned64
_CucsEtherRxStatsHistUnicastPacketsDeltaMin_Object = MibTableColumn
cucsEtherRxStatsHistUnicastPacketsDeltaMin = _CucsEtherRxStatsHistUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 10, 1, 38),
    _CucsEtherRxStatsHistUnicastPacketsDeltaMin_Type()
)
cucsEtherRxStatsHistUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherRxStatsHistUnicastPacketsDeltaMin.setStatus("current")
_CucsEtherServerIntFIoTable_Object = MibTable
cucsEtherServerIntFIoTable = _CucsEtherServerIntFIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11)
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoTable.setStatus("current")
_CucsEtherServerIntFIoEntry_Object = MibTableRow
cucsEtherServerIntFIoEntry = _CucsEtherServerIntFIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1)
)
cucsEtherServerIntFIoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherServerIntFIoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoEntry.setStatus("current")
_CucsEtherServerIntFIoInstanceId_Type = CucsManagedObjectId
_CucsEtherServerIntFIoInstanceId_Object = MibTableColumn
cucsEtherServerIntFIoInstanceId = _CucsEtherServerIntFIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 1),
    _CucsEtherServerIntFIoInstanceId_Type()
)
cucsEtherServerIntFIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoInstanceId.setStatus("current")
_CucsEtherServerIntFIoDn_Type = CucsManagedObjectDn
_CucsEtherServerIntFIoDn_Object = MibTableColumn
cucsEtherServerIntFIoDn = _CucsEtherServerIntFIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 2),
    _CucsEtherServerIntFIoDn_Type()
)
cucsEtherServerIntFIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoDn.setStatus("current")
_CucsEtherServerIntFIoRn_Type = SnmpAdminString
_CucsEtherServerIntFIoRn_Object = MibTableColumn
cucsEtherServerIntFIoRn = _CucsEtherServerIntFIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 3),
    _CucsEtherServerIntFIoRn_Type()
)
cucsEtherServerIntFIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoRn.setStatus("current")
_CucsEtherServerIntFIoAdminState_Type = CucsEtherServerIntFIoAdminState
_CucsEtherServerIntFIoAdminState_Object = MibTableColumn
cucsEtherServerIntFIoAdminState = _CucsEtherServerIntFIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 4),
    _CucsEtherServerIntFIoAdminState_Type()
)
cucsEtherServerIntFIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoAdminState.setStatus("current")
_CucsEtherServerIntFIoChassisId_Type = Gauge32
_CucsEtherServerIntFIoChassisId_Object = MibTableColumn
cucsEtherServerIntFIoChassisId = _CucsEtherServerIntFIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 5),
    _CucsEtherServerIntFIoChassisId_Type()
)
cucsEtherServerIntFIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoChassisId.setStatus("current")
_CucsEtherServerIntFIoEncap_Type = CucsPortEncap
_CucsEtherServerIntFIoEncap_Object = MibTableColumn
cucsEtherServerIntFIoEncap = _CucsEtherServerIntFIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 6),
    _CucsEtherServerIntFIoEncap_Type()
)
cucsEtherServerIntFIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoEncap.setStatus("current")
_CucsEtherServerIntFIoEpDn_Type = SnmpAdminString
_CucsEtherServerIntFIoEpDn_Object = MibTableColumn
cucsEtherServerIntFIoEpDn = _CucsEtherServerIntFIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 7),
    _CucsEtherServerIntFIoEpDn_Type()
)
cucsEtherServerIntFIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoEpDn.setStatus("current")
_CucsEtherServerIntFIoFltAggr_Type = Unsigned64
_CucsEtherServerIntFIoFltAggr_Object = MibTableColumn
cucsEtherServerIntFIoFltAggr = _CucsEtherServerIntFIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 8),
    _CucsEtherServerIntFIoFltAggr_Type()
)
cucsEtherServerIntFIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFltAggr.setStatus("current")
_CucsEtherServerIntFIoIfRole_Type = CucsEtherServerIntFIoIfRole
_CucsEtherServerIntFIoIfRole_Object = MibTableColumn
cucsEtherServerIntFIoIfRole = _CucsEtherServerIntFIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 9),
    _CucsEtherServerIntFIoIfRole_Type()
)
cucsEtherServerIntFIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoIfRole.setStatus("current")
_CucsEtherServerIntFIoIfType_Type = CucsNetworkPhysEpIfType
_CucsEtherServerIntFIoIfType_Object = MibTableColumn
cucsEtherServerIntFIoIfType = _CucsEtherServerIntFIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 10),
    _CucsEtherServerIntFIoIfType_Type()
)
cucsEtherServerIntFIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoIfType.setStatus("current")
_CucsEtherServerIntFIoLocale_Type = CucsEtherServerIntFIoLocale
_CucsEtherServerIntFIoLocale_Object = MibTableColumn
cucsEtherServerIntFIoLocale = _CucsEtherServerIntFIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 11),
    _CucsEtherServerIntFIoLocale_Type()
)
cucsEtherServerIntFIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoLocale.setStatus("current")
_CucsEtherServerIntFIoMode_Type = CucsPortMode
_CucsEtherServerIntFIoMode_Object = MibTableColumn
cucsEtherServerIntFIoMode = _CucsEtherServerIntFIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 12),
    _CucsEtherServerIntFIoMode_Type()
)
cucsEtherServerIntFIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoMode.setStatus("current")
_CucsEtherServerIntFIoModel_Type = SnmpAdminString
_CucsEtherServerIntFIoModel_Object = MibTableColumn
cucsEtherServerIntFIoModel = _CucsEtherServerIntFIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 13),
    _CucsEtherServerIntFIoModel_Type()
)
cucsEtherServerIntFIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoModel.setStatus("current")
_CucsEtherServerIntFIoName_Type = SnmpAdminString
_CucsEtherServerIntFIoName_Object = MibTableColumn
cucsEtherServerIntFIoName = _CucsEtherServerIntFIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 14),
    _CucsEtherServerIntFIoName_Type()
)
cucsEtherServerIntFIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoName.setStatus("current")
_CucsEtherServerIntFIoOperBorderPortId_Type = Gauge32
_CucsEtherServerIntFIoOperBorderPortId_Object = MibTableColumn
cucsEtherServerIntFIoOperBorderPortId = _CucsEtherServerIntFIoOperBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 15),
    _CucsEtherServerIntFIoOperBorderPortId_Type()
)
cucsEtherServerIntFIoOperBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoOperBorderPortId.setStatus("current")
_CucsEtherServerIntFIoOperBorderSlotId_Type = Gauge32
_CucsEtherServerIntFIoOperBorderSlotId_Object = MibTableColumn
cucsEtherServerIntFIoOperBorderSlotId = _CucsEtherServerIntFIoOperBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 16),
    _CucsEtherServerIntFIoOperBorderSlotId_Type()
)
cucsEtherServerIntFIoOperBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoOperBorderSlotId.setStatus("current")
_CucsEtherServerIntFIoOperState_Type = CucsNetworkPortOperState
_CucsEtherServerIntFIoOperState_Object = MibTableColumn
cucsEtherServerIntFIoOperState = _CucsEtherServerIntFIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 17),
    _CucsEtherServerIntFIoOperState_Type()
)
cucsEtherServerIntFIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoOperState.setStatus("current")
_CucsEtherServerIntFIoPeerDn_Type = SnmpAdminString
_CucsEtherServerIntFIoPeerDn_Object = MibTableColumn
cucsEtherServerIntFIoPeerDn = _CucsEtherServerIntFIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 18),
    _CucsEtherServerIntFIoPeerDn_Type()
)
cucsEtherServerIntFIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPeerDn.setStatus("current")
_CucsEtherServerIntFIoPeerPortId_Type = Gauge32
_CucsEtherServerIntFIoPeerPortId_Object = MibTableColumn
cucsEtherServerIntFIoPeerPortId = _CucsEtherServerIntFIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 19),
    _CucsEtherServerIntFIoPeerPortId_Type()
)
cucsEtherServerIntFIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPeerPortId.setStatus("current")
_CucsEtherServerIntFIoPeerSlotId_Type = Gauge32
_CucsEtherServerIntFIoPeerSlotId_Object = MibTableColumn
cucsEtherServerIntFIoPeerSlotId = _CucsEtherServerIntFIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 20),
    _CucsEtherServerIntFIoPeerSlotId_Type()
)
cucsEtherServerIntFIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPeerSlotId.setStatus("current")
_CucsEtherServerIntFIoPortId_Type = Gauge32
_CucsEtherServerIntFIoPortId_Object = MibTableColumn
cucsEtherServerIntFIoPortId = _CucsEtherServerIntFIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 21),
    _CucsEtherServerIntFIoPortId_Type()
)
cucsEtherServerIntFIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPortId.setStatus("current")
_CucsEtherServerIntFIoRevision_Type = SnmpAdminString
_CucsEtherServerIntFIoRevision_Object = MibTableColumn
cucsEtherServerIntFIoRevision = _CucsEtherServerIntFIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 22),
    _CucsEtherServerIntFIoRevision_Type()
)
cucsEtherServerIntFIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoRevision.setStatus("current")
_CucsEtherServerIntFIoSerial_Type = SnmpAdminString
_CucsEtherServerIntFIoSerial_Object = MibTableColumn
cucsEtherServerIntFIoSerial = _CucsEtherServerIntFIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 23),
    _CucsEtherServerIntFIoSerial_Type()
)
cucsEtherServerIntFIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoSerial.setStatus("current")
_CucsEtherServerIntFIoSlotId_Type = Gauge32
_CucsEtherServerIntFIoSlotId_Object = MibTableColumn
cucsEtherServerIntFIoSlotId = _CucsEtherServerIntFIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 24),
    _CucsEtherServerIntFIoSlotId_Type()
)
cucsEtherServerIntFIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoSlotId.setStatus("current")
_CucsEtherServerIntFIoStateQual_Type = SnmpAdminString
_CucsEtherServerIntFIoStateQual_Object = MibTableColumn
cucsEtherServerIntFIoStateQual = _CucsEtherServerIntFIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 25),
    _CucsEtherServerIntFIoStateQual_Type()
)
cucsEtherServerIntFIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoStateQual.setStatus("current")
_CucsEtherServerIntFIoSwitchId_Type = CucsNetworkSwitchId
_CucsEtherServerIntFIoSwitchId_Object = MibTableColumn
cucsEtherServerIntFIoSwitchId = _CucsEtherServerIntFIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 26),
    _CucsEtherServerIntFIoSwitchId_Type()
)
cucsEtherServerIntFIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoSwitchId.setStatus("current")
_CucsEtherServerIntFIoTransport_Type = CucsEtherServerIntFIoTransport
_CucsEtherServerIntFIoTransport_Object = MibTableColumn
cucsEtherServerIntFIoTransport = _CucsEtherServerIntFIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 27),
    _CucsEtherServerIntFIoTransport_Type()
)
cucsEtherServerIntFIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoTransport.setStatus("current")
_CucsEtherServerIntFIoTs_Type = DateAndTime
_CucsEtherServerIntFIoTs_Object = MibTableColumn
cucsEtherServerIntFIoTs = _CucsEtherServerIntFIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 28),
    _CucsEtherServerIntFIoTs_Type()
)
cucsEtherServerIntFIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoTs.setStatus("current")
_CucsEtherServerIntFIoType_Type = CucsEtherServerIntFIoType
_CucsEtherServerIntFIoType_Object = MibTableColumn
cucsEtherServerIntFIoType = _CucsEtherServerIntFIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 29),
    _CucsEtherServerIntFIoType_Type()
)
cucsEtherServerIntFIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoType.setStatus("current")
_CucsEtherServerIntFIoVendor_Type = SnmpAdminString
_CucsEtherServerIntFIoVendor_Object = MibTableColumn
cucsEtherServerIntFIoVendor = _CucsEtherServerIntFIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 30),
    _CucsEtherServerIntFIoVendor_Type()
)
cucsEtherServerIntFIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoVendor.setStatus("current")
_CucsEtherServerIntFIoMac_Type = MacAddress
_CucsEtherServerIntFIoMac_Object = MibTableColumn
cucsEtherServerIntFIoMac = _CucsEtherServerIntFIoMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 31),
    _CucsEtherServerIntFIoMac_Type()
)
cucsEtherServerIntFIoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoMac.setStatus("current")
_CucsEtherServerIntFIoPeerChassisId_Type = Gauge32
_CucsEtherServerIntFIoPeerChassisId_Object = MibTableColumn
cucsEtherServerIntFIoPeerChassisId = _CucsEtherServerIntFIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 32),
    _CucsEtherServerIntFIoPeerChassisId_Type()
)
cucsEtherServerIntFIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPeerChassisId.setStatus("current")
_CucsEtherServerIntFIoXcvrType_Type = CucsEquipmentXcvrType
_CucsEtherServerIntFIoXcvrType_Object = MibTableColumn
cucsEtherServerIntFIoXcvrType = _CucsEtherServerIntFIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 33),
    _CucsEtherServerIntFIoXcvrType_Type()
)
cucsEtherServerIntFIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoXcvrType.setStatus("current")
_CucsEtherServerIntFIoAdminSpeed_Type = CucsPortEthSpeed
_CucsEtherServerIntFIoAdminSpeed_Object = MibTableColumn
cucsEtherServerIntFIoAdminSpeed = _CucsEtherServerIntFIoAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 34),
    _CucsEtherServerIntFIoAdminSpeed_Type()
)
cucsEtherServerIntFIoAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoAdminSpeed.setStatus("current")
_CucsEtherServerIntFIoFsmDescr_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmDescr_Object = MibTableColumn
cucsEtherServerIntFIoFsmDescr = _CucsEtherServerIntFIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 35),
    _CucsEtherServerIntFIoFsmDescr_Type()
)
cucsEtherServerIntFIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmDescr.setStatus("current")
_CucsEtherServerIntFIoFsmPrev_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmPrev_Object = MibTableColumn
cucsEtherServerIntFIoFsmPrev = _CucsEtherServerIntFIoFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 36),
    _CucsEtherServerIntFIoFsmPrev_Type()
)
cucsEtherServerIntFIoFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmPrev.setStatus("current")
_CucsEtherServerIntFIoFsmProgr_Type = Gauge32
_CucsEtherServerIntFIoFsmProgr_Object = MibTableColumn
cucsEtherServerIntFIoFsmProgr = _CucsEtherServerIntFIoFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 37),
    _CucsEtherServerIntFIoFsmProgr_Type()
)
cucsEtherServerIntFIoFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmProgr.setStatus("current")
_CucsEtherServerIntFIoFsmRmtInvErrCode_Type = Gauge32
_CucsEtherServerIntFIoFsmRmtInvErrCode_Object = MibTableColumn
cucsEtherServerIntFIoFsmRmtInvErrCode = _CucsEtherServerIntFIoFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 38),
    _CucsEtherServerIntFIoFsmRmtInvErrCode_Type()
)
cucsEtherServerIntFIoFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmRmtInvErrCode.setStatus("current")
_CucsEtherServerIntFIoFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmRmtInvErrDescr_Object = MibTableColumn
cucsEtherServerIntFIoFsmRmtInvErrDescr = _CucsEtherServerIntFIoFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 39),
    _CucsEtherServerIntFIoFsmRmtInvErrDescr_Type()
)
cucsEtherServerIntFIoFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmRmtInvErrDescr.setStatus("current")
_CucsEtherServerIntFIoFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsEtherServerIntFIoFsmRmtInvRslt_Object = MibTableColumn
cucsEtherServerIntFIoFsmRmtInvRslt = _CucsEtherServerIntFIoFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 40),
    _CucsEtherServerIntFIoFsmRmtInvRslt_Type()
)
cucsEtherServerIntFIoFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmRmtInvRslt.setStatus("current")
_CucsEtherServerIntFIoFsmStageDescr_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmStageDescr_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageDescr = _CucsEtherServerIntFIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 41),
    _CucsEtherServerIntFIoFsmStageDescr_Type()
)
cucsEtherServerIntFIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageDescr.setStatus("current")
_CucsEtherServerIntFIoFsmStamp_Type = DateAndTime
_CucsEtherServerIntFIoFsmStamp_Object = MibTableColumn
cucsEtherServerIntFIoFsmStamp = _CucsEtherServerIntFIoFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 42),
    _CucsEtherServerIntFIoFsmStamp_Type()
)
cucsEtherServerIntFIoFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStamp.setStatus("current")
_CucsEtherServerIntFIoFsmStatus_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmStatus_Object = MibTableColumn
cucsEtherServerIntFIoFsmStatus = _CucsEtherServerIntFIoFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 43),
    _CucsEtherServerIntFIoFsmStatus_Type()
)
cucsEtherServerIntFIoFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStatus.setStatus("current")
_CucsEtherServerIntFIoFsmTry_Type = Gauge32
_CucsEtherServerIntFIoFsmTry_Object = MibTableColumn
cucsEtherServerIntFIoFsmTry = _CucsEtherServerIntFIoFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 44),
    _CucsEtherServerIntFIoFsmTry_Type()
)
cucsEtherServerIntFIoFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTry.setStatus("current")
_CucsEtherServerIntFIoNsSize_Type = Gauge32
_CucsEtherServerIntFIoNsSize_Object = MibTableColumn
cucsEtherServerIntFIoNsSize = _CucsEtherServerIntFIoNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 45),
    _CucsEtherServerIntFIoNsSize_Type()
)
cucsEtherServerIntFIoNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoNsSize.setStatus("current")
_CucsEtherServerIntFIoPeerEncap_Type = Gauge32
_CucsEtherServerIntFIoPeerEncap_Object = MibTableColumn
cucsEtherServerIntFIoPeerEncap = _CucsEtherServerIntFIoPeerEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 46),
    _CucsEtherServerIntFIoPeerEncap_Type()
)
cucsEtherServerIntFIoPeerEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPeerEncap.setStatus("current")
_CucsEtherServerIntFIoAggrPortId_Type = Gauge32
_CucsEtherServerIntFIoAggrPortId_Object = MibTableColumn
cucsEtherServerIntFIoAggrPortId = _CucsEtherServerIntFIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 47),
    _CucsEtherServerIntFIoAggrPortId_Type()
)
cucsEtherServerIntFIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoAggrPortId.setStatus("current")
_CucsEtherServerIntFIoPeerAggrPortId_Type = Gauge32
_CucsEtherServerIntFIoPeerAggrPortId_Object = MibTableColumn
cucsEtherServerIntFIoPeerAggrPortId = _CucsEtherServerIntFIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 48),
    _CucsEtherServerIntFIoPeerAggrPortId_Type()
)
cucsEtherServerIntFIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPeerAggrPortId.setStatus("current")
_CucsEtherServerIntFIoMacAddr_Type = MacAddress
_CucsEtherServerIntFIoMacAddr_Object = MibTableColumn
cucsEtherServerIntFIoMacAddr = _CucsEtherServerIntFIoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 49),
    _CucsEtherServerIntFIoMacAddr_Type()
)
cucsEtherServerIntFIoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoMacAddr.setStatus("current")
_CucsEtherServerIntFIoOperBorderAggrPortId_Type = Gauge32
_CucsEtherServerIntFIoOperBorderAggrPortId_Object = MibTableColumn
cucsEtherServerIntFIoOperBorderAggrPortId = _CucsEtherServerIntFIoOperBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 11, 1, 50),
    _CucsEtherServerIntFIoOperBorderAggrPortId_Type()
)
cucsEtherServerIntFIoOperBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoOperBorderAggrPortId.setStatus("current")
_CucsEtherSwIfConfigTable_Object = MibTable
cucsEtherSwIfConfigTable = _CucsEtherSwIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 12)
)
if mibBuilder.loadTexts:
    cucsEtherSwIfConfigTable.setStatus("current")
_CucsEtherSwIfConfigEntry_Object = MibTableRow
cucsEtherSwIfConfigEntry = _CucsEtherSwIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 12, 1)
)
cucsEtherSwIfConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherSwIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherSwIfConfigEntry.setStatus("current")
_CucsEtherSwIfConfigInstanceId_Type = CucsManagedObjectId
_CucsEtherSwIfConfigInstanceId_Object = MibTableColumn
cucsEtherSwIfConfigInstanceId = _CucsEtherSwIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 12, 1, 1),
    _CucsEtherSwIfConfigInstanceId_Type()
)
cucsEtherSwIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherSwIfConfigInstanceId.setStatus("current")
_CucsEtherSwIfConfigDn_Type = CucsManagedObjectDn
_CucsEtherSwIfConfigDn_Object = MibTableColumn
cucsEtherSwIfConfigDn = _CucsEtherSwIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 12, 1, 2),
    _CucsEtherSwIfConfigDn_Type()
)
cucsEtherSwIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwIfConfigDn.setStatus("current")
_CucsEtherSwIfConfigRn_Type = SnmpAdminString
_CucsEtherSwIfConfigRn_Object = MibTableColumn
cucsEtherSwIfConfigRn = _CucsEtherSwIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 12, 1, 3),
    _CucsEtherSwIfConfigRn_Type()
)
cucsEtherSwIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwIfConfigRn.setStatus("current")
_CucsEtherSwitchIntFIoTable_Object = MibTable
cucsEtherSwitchIntFIoTable = _CucsEtherSwitchIntFIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13)
)
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoTable.setStatus("current")
_CucsEtherSwitchIntFIoEntry_Object = MibTableRow
cucsEtherSwitchIntFIoEntry = _CucsEtherSwitchIntFIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1)
)
cucsEtherSwitchIntFIoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherSwitchIntFIoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoEntry.setStatus("current")
_CucsEtherSwitchIntFIoInstanceId_Type = CucsManagedObjectId
_CucsEtherSwitchIntFIoInstanceId_Object = MibTableColumn
cucsEtherSwitchIntFIoInstanceId = _CucsEtherSwitchIntFIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 1),
    _CucsEtherSwitchIntFIoInstanceId_Type()
)
cucsEtherSwitchIntFIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoInstanceId.setStatus("current")
_CucsEtherSwitchIntFIoDn_Type = CucsManagedObjectDn
_CucsEtherSwitchIntFIoDn_Object = MibTableColumn
cucsEtherSwitchIntFIoDn = _CucsEtherSwitchIntFIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 2),
    _CucsEtherSwitchIntFIoDn_Type()
)
cucsEtherSwitchIntFIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoDn.setStatus("current")
_CucsEtherSwitchIntFIoRn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoRn_Object = MibTableColumn
cucsEtherSwitchIntFIoRn = _CucsEtherSwitchIntFIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 3),
    _CucsEtherSwitchIntFIoRn_Type()
)
cucsEtherSwitchIntFIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoRn.setStatus("current")
_CucsEtherSwitchIntFIoAck_Type = CucsEtherSwitchIntFIoAck
_CucsEtherSwitchIntFIoAck_Object = MibTableColumn
cucsEtherSwitchIntFIoAck = _CucsEtherSwitchIntFIoAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 4),
    _CucsEtherSwitchIntFIoAck_Type()
)
cucsEtherSwitchIntFIoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoAck.setStatus("current")
_CucsEtherSwitchIntFIoAdminState_Type = CucsFabricAdminState
_CucsEtherSwitchIntFIoAdminState_Object = MibTableColumn
cucsEtherSwitchIntFIoAdminState = _CucsEtherSwitchIntFIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 5),
    _CucsEtherSwitchIntFIoAdminState_Type()
)
cucsEtherSwitchIntFIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoAdminState.setStatus("current")
_CucsEtherSwitchIntFIoChassisId_Type = Gauge32
_CucsEtherSwitchIntFIoChassisId_Object = MibTableColumn
cucsEtherSwitchIntFIoChassisId = _CucsEtherSwitchIntFIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 6),
    _CucsEtherSwitchIntFIoChassisId_Type()
)
cucsEtherSwitchIntFIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoChassisId.setStatus("current")
_CucsEtherSwitchIntFIoDiscovery_Type = CucsEtherSatelliteConnectionDisc
_CucsEtherSwitchIntFIoDiscovery_Object = MibTableColumn
cucsEtherSwitchIntFIoDiscovery = _CucsEtherSwitchIntFIoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 7),
    _CucsEtherSwitchIntFIoDiscovery_Type()
)
cucsEtherSwitchIntFIoDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoDiscovery.setStatus("current")
_CucsEtherSwitchIntFIoEncap_Type = CucsPortEncap
_CucsEtherSwitchIntFIoEncap_Object = MibTableColumn
cucsEtherSwitchIntFIoEncap = _CucsEtherSwitchIntFIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 8),
    _CucsEtherSwitchIntFIoEncap_Type()
)
cucsEtherSwitchIntFIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoEncap.setStatus("current")
_CucsEtherSwitchIntFIoEpDn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoEpDn_Object = MibTableColumn
cucsEtherSwitchIntFIoEpDn = _CucsEtherSwitchIntFIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 9),
    _CucsEtherSwitchIntFIoEpDn_Type()
)
cucsEtherSwitchIntFIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoEpDn.setStatus("current")
_CucsEtherSwitchIntFIoFltAggr_Type = Unsigned64
_CucsEtherSwitchIntFIoFltAggr_Object = MibTableColumn
cucsEtherSwitchIntFIoFltAggr = _CucsEtherSwitchIntFIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 10),
    _CucsEtherSwitchIntFIoFltAggr_Type()
)
cucsEtherSwitchIntFIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoFltAggr.setStatus("current")
_CucsEtherSwitchIntFIoIfRole_Type = CucsEtherSwitchIntFIoIfRole
_CucsEtherSwitchIntFIoIfRole_Object = MibTableColumn
cucsEtherSwitchIntFIoIfRole = _CucsEtherSwitchIntFIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 11),
    _CucsEtherSwitchIntFIoIfRole_Type()
)
cucsEtherSwitchIntFIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoIfRole.setStatus("current")
_CucsEtherSwitchIntFIoIfType_Type = CucsNetworkPhysEpIfType
_CucsEtherSwitchIntFIoIfType_Object = MibTableColumn
cucsEtherSwitchIntFIoIfType = _CucsEtherSwitchIntFIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 12),
    _CucsEtherSwitchIntFIoIfType_Type()
)
cucsEtherSwitchIntFIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoIfType.setStatus("current")
_CucsEtherSwitchIntFIoLocale_Type = CucsEtherSwitchIntFIoLocale
_CucsEtherSwitchIntFIoLocale_Object = MibTableColumn
cucsEtherSwitchIntFIoLocale = _CucsEtherSwitchIntFIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 13),
    _CucsEtherSwitchIntFIoLocale_Type()
)
cucsEtherSwitchIntFIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoLocale.setStatus("current")
_CucsEtherSwitchIntFIoMode_Type = CucsPortMode
_CucsEtherSwitchIntFIoMode_Object = MibTableColumn
cucsEtherSwitchIntFIoMode = _CucsEtherSwitchIntFIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 14),
    _CucsEtherSwitchIntFIoMode_Type()
)
cucsEtherSwitchIntFIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoMode.setStatus("current")
_CucsEtherSwitchIntFIoModel_Type = SnmpAdminString
_CucsEtherSwitchIntFIoModel_Object = MibTableColumn
cucsEtherSwitchIntFIoModel = _CucsEtherSwitchIntFIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 15),
    _CucsEtherSwitchIntFIoModel_Type()
)
cucsEtherSwitchIntFIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoModel.setStatus("current")
_CucsEtherSwitchIntFIoName_Type = SnmpAdminString
_CucsEtherSwitchIntFIoName_Object = MibTableColumn
cucsEtherSwitchIntFIoName = _CucsEtherSwitchIntFIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 16),
    _CucsEtherSwitchIntFIoName_Type()
)
cucsEtherSwitchIntFIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoName.setStatus("current")
_CucsEtherSwitchIntFIoOperState_Type = CucsNetworkPortOperState
_CucsEtherSwitchIntFIoOperState_Object = MibTableColumn
cucsEtherSwitchIntFIoOperState = _CucsEtherSwitchIntFIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 17),
    _CucsEtherSwitchIntFIoOperState_Type()
)
cucsEtherSwitchIntFIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoOperState.setStatus("current")
_CucsEtherSwitchIntFIoPeerDn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPeerDn_Object = MibTableColumn
cucsEtherSwitchIntFIoPeerDn = _CucsEtherSwitchIntFIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 18),
    _CucsEtherSwitchIntFIoPeerDn_Type()
)
cucsEtherSwitchIntFIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPeerDn.setStatus("current")
_CucsEtherSwitchIntFIoPeerPortId_Type = Gauge32
_CucsEtherSwitchIntFIoPeerPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPeerPortId = _CucsEtherSwitchIntFIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 19),
    _CucsEtherSwitchIntFIoPeerPortId_Type()
)
cucsEtherSwitchIntFIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPeerPortId.setStatus("current")
_CucsEtherSwitchIntFIoPeerSlotId_Type = Gauge32
_CucsEtherSwitchIntFIoPeerSlotId_Object = MibTableColumn
cucsEtherSwitchIntFIoPeerSlotId = _CucsEtherSwitchIntFIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 20),
    _CucsEtherSwitchIntFIoPeerSlotId_Type()
)
cucsEtherSwitchIntFIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPeerSlotId.setStatus("current")
_CucsEtherSwitchIntFIoPortId_Type = Gauge32
_CucsEtherSwitchIntFIoPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPortId = _CucsEtherSwitchIntFIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 21),
    _CucsEtherSwitchIntFIoPortId_Type()
)
cucsEtherSwitchIntFIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPortId.setStatus("current")
_CucsEtherSwitchIntFIoRevision_Type = SnmpAdminString
_CucsEtherSwitchIntFIoRevision_Object = MibTableColumn
cucsEtherSwitchIntFIoRevision = _CucsEtherSwitchIntFIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 22),
    _CucsEtherSwitchIntFIoRevision_Type()
)
cucsEtherSwitchIntFIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoRevision.setStatus("current")
_CucsEtherSwitchIntFIoSerial_Type = SnmpAdminString
_CucsEtherSwitchIntFIoSerial_Object = MibTableColumn
cucsEtherSwitchIntFIoSerial = _CucsEtherSwitchIntFIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 23),
    _CucsEtherSwitchIntFIoSerial_Type()
)
cucsEtherSwitchIntFIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoSerial.setStatus("current")
_CucsEtherSwitchIntFIoSlotId_Type = Gauge32
_CucsEtherSwitchIntFIoSlotId_Object = MibTableColumn
cucsEtherSwitchIntFIoSlotId = _CucsEtherSwitchIntFIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 24),
    _CucsEtherSwitchIntFIoSlotId_Type()
)
cucsEtherSwitchIntFIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoSlotId.setStatus("current")
_CucsEtherSwitchIntFIoStateQual_Type = SnmpAdminString
_CucsEtherSwitchIntFIoStateQual_Object = MibTableColumn
cucsEtherSwitchIntFIoStateQual = _CucsEtherSwitchIntFIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 25),
    _CucsEtherSwitchIntFIoStateQual_Type()
)
cucsEtherSwitchIntFIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoStateQual.setStatus("current")
_CucsEtherSwitchIntFIoSwitchId_Type = CucsNetworkSwitchId
_CucsEtherSwitchIntFIoSwitchId_Object = MibTableColumn
cucsEtherSwitchIntFIoSwitchId = _CucsEtherSwitchIntFIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 26),
    _CucsEtherSwitchIntFIoSwitchId_Type()
)
cucsEtherSwitchIntFIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoSwitchId.setStatus("current")
_CucsEtherSwitchIntFIoTransport_Type = CucsEtherSwitchIntFIoTransport
_CucsEtherSwitchIntFIoTransport_Object = MibTableColumn
cucsEtherSwitchIntFIoTransport = _CucsEtherSwitchIntFIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 27),
    _CucsEtherSwitchIntFIoTransport_Type()
)
cucsEtherSwitchIntFIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoTransport.setStatus("current")
_CucsEtherSwitchIntFIoTs_Type = DateAndTime
_CucsEtherSwitchIntFIoTs_Object = MibTableColumn
cucsEtherSwitchIntFIoTs = _CucsEtherSwitchIntFIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 28),
    _CucsEtherSwitchIntFIoTs_Type()
)
cucsEtherSwitchIntFIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoTs.setStatus("current")
_CucsEtherSwitchIntFIoType_Type = CucsEtherSwitchIntFIoType
_CucsEtherSwitchIntFIoType_Object = MibTableColumn
cucsEtherSwitchIntFIoType = _CucsEtherSwitchIntFIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 29),
    _CucsEtherSwitchIntFIoType_Type()
)
cucsEtherSwitchIntFIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoType.setStatus("current")
_CucsEtherSwitchIntFIoVendor_Type = SnmpAdminString
_CucsEtherSwitchIntFIoVendor_Object = MibTableColumn
cucsEtherSwitchIntFIoVendor = _CucsEtherSwitchIntFIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 30),
    _CucsEtherSwitchIntFIoVendor_Type()
)
cucsEtherSwitchIntFIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoVendor.setStatus("current")
_CucsEtherSwitchIntFIoPeerChassisId_Type = Gauge32
_CucsEtherSwitchIntFIoPeerChassisId_Object = MibTableColumn
cucsEtherSwitchIntFIoPeerChassisId = _CucsEtherSwitchIntFIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 31),
    _CucsEtherSwitchIntFIoPeerChassisId_Type()
)
cucsEtherSwitchIntFIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPeerChassisId.setStatus("current")
_CucsEtherSwitchIntFIoXcvrType_Type = CucsEquipmentXcvrType
_CucsEtherSwitchIntFIoXcvrType_Object = MibTableColumn
cucsEtherSwitchIntFIoXcvrType = _CucsEtherSwitchIntFIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 32),
    _CucsEtherSwitchIntFIoXcvrType_Type()
)
cucsEtherSwitchIntFIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoXcvrType.setStatus("current")
_CucsEtherSwitchIntFIoDelFeTs_Type = Unsigned64
_CucsEtherSwitchIntFIoDelFeTs_Object = MibTableColumn
cucsEtherSwitchIntFIoDelFeTs = _CucsEtherSwitchIntFIoDelFeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 33),
    _CucsEtherSwitchIntFIoDelFeTs_Type()
)
cucsEtherSwitchIntFIoDelFeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoDelFeTs.setStatus("current")
_CucsEtherSwitchIntFIoNewFeTs_Type = Unsigned64
_CucsEtherSwitchIntFIoNewFeTs_Object = MibTableColumn
cucsEtherSwitchIntFIoNewFeTs = _CucsEtherSwitchIntFIoNewFeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 34),
    _CucsEtherSwitchIntFIoNewFeTs_Type()
)
cucsEtherSwitchIntFIoNewFeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoNewFeTs.setStatus("current")
_CucsEtherSwitchIntFIoAggrPortId_Type = Gauge32
_CucsEtherSwitchIntFIoAggrPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoAggrPortId = _CucsEtherSwitchIntFIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 35),
    _CucsEtherSwitchIntFIoAggrPortId_Type()
)
cucsEtherSwitchIntFIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoAggrPortId.setStatus("current")
_CucsEtherSwitchIntFIoPeerAggrPortId_Type = Gauge32
_CucsEtherSwitchIntFIoPeerAggrPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPeerAggrPortId = _CucsEtherSwitchIntFIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 36),
    _CucsEtherSwitchIntFIoPeerAggrPortId_Type()
)
cucsEtherSwitchIntFIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPeerAggrPortId.setStatus("current")
_CucsEtherSwitchIntFIoMacAddr_Type = MacAddress
_CucsEtherSwitchIntFIoMacAddr_Object = MibTableColumn
cucsEtherSwitchIntFIoMacAddr = _CucsEtherSwitchIntFIoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 13, 1, 37),
    _CucsEtherSwitchIntFIoMacAddr_Type()
)
cucsEtherSwitchIntFIoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoMacAddr.setStatus("current")
_CucsEtherTxStatsTable_Object = MibTable
cucsEtherTxStatsTable = _CucsEtherTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14)
)
if mibBuilder.loadTexts:
    cucsEtherTxStatsTable.setStatus("current")
_CucsEtherTxStatsEntry_Object = MibTableRow
cucsEtherTxStatsEntry = _CucsEtherTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1)
)
cucsEtherTxStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherTxStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherTxStatsEntry.setStatus("current")
_CucsEtherTxStatsInstanceId_Type = CucsManagedObjectId
_CucsEtherTxStatsInstanceId_Object = MibTableColumn
cucsEtherTxStatsInstanceId = _CucsEtherTxStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 1),
    _CucsEtherTxStatsInstanceId_Type()
)
cucsEtherTxStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherTxStatsInstanceId.setStatus("current")
_CucsEtherTxStatsDn_Type = CucsManagedObjectDn
_CucsEtherTxStatsDn_Object = MibTableColumn
cucsEtherTxStatsDn = _CucsEtherTxStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 2),
    _CucsEtherTxStatsDn_Type()
)
cucsEtherTxStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsDn.setStatus("current")
_CucsEtherTxStatsRn_Type = SnmpAdminString
_CucsEtherTxStatsRn_Object = MibTableColumn
cucsEtherTxStatsRn = _CucsEtherTxStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 3),
    _CucsEtherTxStatsRn_Type()
)
cucsEtherTxStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsRn.setStatus("current")
_CucsEtherTxStatsBroadcastPackets_Type = Unsigned64
_CucsEtherTxStatsBroadcastPackets_Object = MibTableColumn
cucsEtherTxStatsBroadcastPackets = _CucsEtherTxStatsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 4),
    _CucsEtherTxStatsBroadcastPackets_Type()
)
cucsEtherTxStatsBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsBroadcastPackets.setStatus("current")
_CucsEtherTxStatsBroadcastPacketsDelta_Type = Counter64
_CucsEtherTxStatsBroadcastPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsBroadcastPacketsDelta = _CucsEtherTxStatsBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 5),
    _CucsEtherTxStatsBroadcastPacketsDelta_Type()
)
cucsEtherTxStatsBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsBroadcastPacketsDelta.setStatus("current")
_CucsEtherTxStatsBroadcastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsBroadcastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsBroadcastPacketsDeltaAvg = _CucsEtherTxStatsBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 6),
    _CucsEtherTxStatsBroadcastPacketsDeltaAvg_Type()
)
cucsEtherTxStatsBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsBroadcastPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsBroadcastPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsBroadcastPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsBroadcastPacketsDeltaMax = _CucsEtherTxStatsBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 7),
    _CucsEtherTxStatsBroadcastPacketsDeltaMax_Type()
)
cucsEtherTxStatsBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsBroadcastPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsBroadcastPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsBroadcastPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsBroadcastPacketsDeltaMin = _CucsEtherTxStatsBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 8),
    _CucsEtherTxStatsBroadcastPacketsDeltaMin_Type()
)
cucsEtherTxStatsBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsBroadcastPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsIntervals_Type = Gauge32
_CucsEtherTxStatsIntervals_Object = MibTableColumn
cucsEtherTxStatsIntervals = _CucsEtherTxStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 9),
    _CucsEtherTxStatsIntervals_Type()
)
cucsEtherTxStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsIntervals.setStatus("current")
_CucsEtherTxStatsJumboPackets_Type = Unsigned64
_CucsEtherTxStatsJumboPackets_Object = MibTableColumn
cucsEtherTxStatsJumboPackets = _CucsEtherTxStatsJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 10),
    _CucsEtherTxStatsJumboPackets_Type()
)
cucsEtherTxStatsJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsJumboPackets.setStatus("current")
_CucsEtherTxStatsJumboPacketsDelta_Type = Counter64
_CucsEtherTxStatsJumboPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsJumboPacketsDelta = _CucsEtherTxStatsJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 11),
    _CucsEtherTxStatsJumboPacketsDelta_Type()
)
cucsEtherTxStatsJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsJumboPacketsDelta.setStatus("current")
_CucsEtherTxStatsJumboPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsJumboPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsJumboPacketsDeltaAvg = _CucsEtherTxStatsJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 12),
    _CucsEtherTxStatsJumboPacketsDeltaAvg_Type()
)
cucsEtherTxStatsJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsJumboPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsJumboPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsJumboPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsJumboPacketsDeltaMax = _CucsEtherTxStatsJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 13),
    _CucsEtherTxStatsJumboPacketsDeltaMax_Type()
)
cucsEtherTxStatsJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsJumboPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsJumboPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsJumboPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsJumboPacketsDeltaMin = _CucsEtherTxStatsJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 14),
    _CucsEtherTxStatsJumboPacketsDeltaMin_Type()
)
cucsEtherTxStatsJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsJumboPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsMulticastPackets_Type = Unsigned64
_CucsEtherTxStatsMulticastPackets_Object = MibTableColumn
cucsEtherTxStatsMulticastPackets = _CucsEtherTxStatsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 15),
    _CucsEtherTxStatsMulticastPackets_Type()
)
cucsEtherTxStatsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsMulticastPackets.setStatus("current")
_CucsEtherTxStatsMulticastPacketsDelta_Type = Counter64
_CucsEtherTxStatsMulticastPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsMulticastPacketsDelta = _CucsEtherTxStatsMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 16),
    _CucsEtherTxStatsMulticastPacketsDelta_Type()
)
cucsEtherTxStatsMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsMulticastPacketsDelta.setStatus("current")
_CucsEtherTxStatsMulticastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsMulticastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsMulticastPacketsDeltaAvg = _CucsEtherTxStatsMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 17),
    _CucsEtherTxStatsMulticastPacketsDeltaAvg_Type()
)
cucsEtherTxStatsMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsMulticastPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsMulticastPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsMulticastPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsMulticastPacketsDeltaMax = _CucsEtherTxStatsMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 18),
    _CucsEtherTxStatsMulticastPacketsDeltaMax_Type()
)
cucsEtherTxStatsMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsMulticastPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsMulticastPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsMulticastPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsMulticastPacketsDeltaMin = _CucsEtherTxStatsMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 19),
    _CucsEtherTxStatsMulticastPacketsDeltaMin_Type()
)
cucsEtherTxStatsMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsMulticastPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsSuspect_Type = TruthValue
_CucsEtherTxStatsSuspect_Object = MibTableColumn
cucsEtherTxStatsSuspect = _CucsEtherTxStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 20),
    _CucsEtherTxStatsSuspect_Type()
)
cucsEtherTxStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsSuspect.setStatus("current")
_CucsEtherTxStatsThresholded_Type = CucsEtherTxStatsThresholded
_CucsEtherTxStatsThresholded_Object = MibTableColumn
cucsEtherTxStatsThresholded = _CucsEtherTxStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 21),
    _CucsEtherTxStatsThresholded_Type()
)
cucsEtherTxStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsThresholded.setStatus("current")
_CucsEtherTxStatsTimeCollected_Type = DateAndTime
_CucsEtherTxStatsTimeCollected_Object = MibTableColumn
cucsEtherTxStatsTimeCollected = _CucsEtherTxStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 22),
    _CucsEtherTxStatsTimeCollected_Type()
)
cucsEtherTxStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTimeCollected.setStatus("current")
_CucsEtherTxStatsTotalBytes_Type = Unsigned64
_CucsEtherTxStatsTotalBytes_Object = MibTableColumn
cucsEtherTxStatsTotalBytes = _CucsEtherTxStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 23),
    _CucsEtherTxStatsTotalBytes_Type()
)
cucsEtherTxStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalBytes.setStatus("current")
_CucsEtherTxStatsTotalBytesDelta_Type = Counter64
_CucsEtherTxStatsTotalBytesDelta_Object = MibTableColumn
cucsEtherTxStatsTotalBytesDelta = _CucsEtherTxStatsTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 24),
    _CucsEtherTxStatsTotalBytesDelta_Type()
)
cucsEtherTxStatsTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalBytesDelta.setStatus("current")
_CucsEtherTxStatsTotalBytesDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsTotalBytesDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsTotalBytesDeltaAvg = _CucsEtherTxStatsTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 25),
    _CucsEtherTxStatsTotalBytesDeltaAvg_Type()
)
cucsEtherTxStatsTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalBytesDeltaAvg.setStatus("current")
_CucsEtherTxStatsTotalBytesDeltaMax_Type = Unsigned64
_CucsEtherTxStatsTotalBytesDeltaMax_Object = MibTableColumn
cucsEtherTxStatsTotalBytesDeltaMax = _CucsEtherTxStatsTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 26),
    _CucsEtherTxStatsTotalBytesDeltaMax_Type()
)
cucsEtherTxStatsTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalBytesDeltaMax.setStatus("current")
_CucsEtherTxStatsTotalBytesDeltaMin_Type = Unsigned64
_CucsEtherTxStatsTotalBytesDeltaMin_Object = MibTableColumn
cucsEtherTxStatsTotalBytesDeltaMin = _CucsEtherTxStatsTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 27),
    _CucsEtherTxStatsTotalBytesDeltaMin_Type()
)
cucsEtherTxStatsTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalBytesDeltaMin.setStatus("current")
_CucsEtherTxStatsTotalPackets_Type = Unsigned64
_CucsEtherTxStatsTotalPackets_Object = MibTableColumn
cucsEtherTxStatsTotalPackets = _CucsEtherTxStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 28),
    _CucsEtherTxStatsTotalPackets_Type()
)
cucsEtherTxStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalPackets.setStatus("current")
_CucsEtherTxStatsTotalPacketsDelta_Type = Counter64
_CucsEtherTxStatsTotalPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsTotalPacketsDelta = _CucsEtherTxStatsTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 29),
    _CucsEtherTxStatsTotalPacketsDelta_Type()
)
cucsEtherTxStatsTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalPacketsDelta.setStatus("current")
_CucsEtherTxStatsTotalPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsTotalPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsTotalPacketsDeltaAvg = _CucsEtherTxStatsTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 30),
    _CucsEtherTxStatsTotalPacketsDeltaAvg_Type()
)
cucsEtherTxStatsTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsTotalPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsTotalPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsTotalPacketsDeltaMax = _CucsEtherTxStatsTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 31),
    _CucsEtherTxStatsTotalPacketsDeltaMax_Type()
)
cucsEtherTxStatsTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsTotalPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsTotalPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsTotalPacketsDeltaMin = _CucsEtherTxStatsTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 32),
    _CucsEtherTxStatsTotalPacketsDeltaMin_Type()
)
cucsEtherTxStatsTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsTotalPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsUnicastPackets_Type = Unsigned64
_CucsEtherTxStatsUnicastPackets_Object = MibTableColumn
cucsEtherTxStatsUnicastPackets = _CucsEtherTxStatsUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 33),
    _CucsEtherTxStatsUnicastPackets_Type()
)
cucsEtherTxStatsUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsUnicastPackets.setStatus("current")
_CucsEtherTxStatsUnicastPacketsDelta_Type = Counter64
_CucsEtherTxStatsUnicastPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsUnicastPacketsDelta = _CucsEtherTxStatsUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 34),
    _CucsEtherTxStatsUnicastPacketsDelta_Type()
)
cucsEtherTxStatsUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsUnicastPacketsDelta.setStatus("current")
_CucsEtherTxStatsUnicastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsUnicastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsUnicastPacketsDeltaAvg = _CucsEtherTxStatsUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 35),
    _CucsEtherTxStatsUnicastPacketsDeltaAvg_Type()
)
cucsEtherTxStatsUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsUnicastPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsUnicastPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsUnicastPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsUnicastPacketsDeltaMax = _CucsEtherTxStatsUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 36),
    _CucsEtherTxStatsUnicastPacketsDeltaMax_Type()
)
cucsEtherTxStatsUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsUnicastPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsUnicastPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsUnicastPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsUnicastPacketsDeltaMin = _CucsEtherTxStatsUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 37),
    _CucsEtherTxStatsUnicastPacketsDeltaMin_Type()
)
cucsEtherTxStatsUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsUnicastPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsUpdate_Type = Gauge32
_CucsEtherTxStatsUpdate_Object = MibTableColumn
cucsEtherTxStatsUpdate = _CucsEtherTxStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 14, 1, 38),
    _CucsEtherTxStatsUpdate_Type()
)
cucsEtherTxStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsUpdate.setStatus("current")
_CucsEtherTxStatsHistTable_Object = MibTable
cucsEtherTxStatsHistTable = _CucsEtherTxStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15)
)
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTable.setStatus("current")
_CucsEtherTxStatsHistEntry_Object = MibTableRow
cucsEtherTxStatsHistEntry = _CucsEtherTxStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1)
)
cucsEtherTxStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherTxStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistEntry.setStatus("current")
_CucsEtherTxStatsHistInstanceId_Type = CucsManagedObjectId
_CucsEtherTxStatsHistInstanceId_Object = MibTableColumn
cucsEtherTxStatsHistInstanceId = _CucsEtherTxStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 1),
    _CucsEtherTxStatsHistInstanceId_Type()
)
cucsEtherTxStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistInstanceId.setStatus("current")
_CucsEtherTxStatsHistDn_Type = CucsManagedObjectDn
_CucsEtherTxStatsHistDn_Object = MibTableColumn
cucsEtherTxStatsHistDn = _CucsEtherTxStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 2),
    _CucsEtherTxStatsHistDn_Type()
)
cucsEtherTxStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistDn.setStatus("current")
_CucsEtherTxStatsHistRn_Type = SnmpAdminString
_CucsEtherTxStatsHistRn_Object = MibTableColumn
cucsEtherTxStatsHistRn = _CucsEtherTxStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 3),
    _CucsEtherTxStatsHistRn_Type()
)
cucsEtherTxStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistRn.setStatus("current")
_CucsEtherTxStatsHistBroadcastPackets_Type = Unsigned64
_CucsEtherTxStatsHistBroadcastPackets_Object = MibTableColumn
cucsEtherTxStatsHistBroadcastPackets = _CucsEtherTxStatsHistBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 4),
    _CucsEtherTxStatsHistBroadcastPackets_Type()
)
cucsEtherTxStatsHistBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistBroadcastPackets.setStatus("current")
_CucsEtherTxStatsHistBroadcastPacketsDelta_Type = Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDelta = _CucsEtherTxStatsHistBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 5),
    _CucsEtherTxStatsHistBroadcastPacketsDelta_Type()
)
cucsEtherTxStatsHistBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistBroadcastPacketsDelta.setStatus("current")
_CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDeltaAvg = _CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 6),
    _CucsEtherTxStatsHistBroadcastPacketsDeltaAvg_Type()
)
cucsEtherTxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistBroadcastPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDeltaMax = _CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 7),
    _CucsEtherTxStatsHistBroadcastPacketsDeltaMax_Type()
)
cucsEtherTxStatsHistBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistBroadcastPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsHistBroadcastPacketsDeltaMin = _CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 8),
    _CucsEtherTxStatsHistBroadcastPacketsDeltaMin_Type()
)
cucsEtherTxStatsHistBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistBroadcastPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsHistId_Type = Unsigned64
_CucsEtherTxStatsHistId_Object = MibTableColumn
cucsEtherTxStatsHistId = _CucsEtherTxStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 9),
    _CucsEtherTxStatsHistId_Type()
)
cucsEtherTxStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistId.setStatus("current")
_CucsEtherTxStatsHistJumboPackets_Type = Unsigned64
_CucsEtherTxStatsHistJumboPackets_Object = MibTableColumn
cucsEtherTxStatsHistJumboPackets = _CucsEtherTxStatsHistJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 10),
    _CucsEtherTxStatsHistJumboPackets_Type()
)
cucsEtherTxStatsHistJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistJumboPackets.setStatus("current")
_CucsEtherTxStatsHistJumboPacketsDelta_Type = Unsigned64
_CucsEtherTxStatsHistJumboPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsHistJumboPacketsDelta = _CucsEtherTxStatsHistJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 11),
    _CucsEtherTxStatsHistJumboPacketsDelta_Type()
)
cucsEtherTxStatsHistJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistJumboPacketsDelta.setStatus("current")
_CucsEtherTxStatsHistJumboPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsHistJumboPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsHistJumboPacketsDeltaAvg = _CucsEtherTxStatsHistJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 12),
    _CucsEtherTxStatsHistJumboPacketsDeltaAvg_Type()
)
cucsEtherTxStatsHistJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistJumboPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsHistJumboPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsHistJumboPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsHistJumboPacketsDeltaMax = _CucsEtherTxStatsHistJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 13),
    _CucsEtherTxStatsHistJumboPacketsDeltaMax_Type()
)
cucsEtherTxStatsHistJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistJumboPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsHistJumboPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsHistJumboPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsHistJumboPacketsDeltaMin = _CucsEtherTxStatsHistJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 14),
    _CucsEtherTxStatsHistJumboPacketsDeltaMin_Type()
)
cucsEtherTxStatsHistJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistJumboPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsHistMostRecent_Type = TruthValue
_CucsEtherTxStatsHistMostRecent_Object = MibTableColumn
cucsEtherTxStatsHistMostRecent = _CucsEtherTxStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 15),
    _CucsEtherTxStatsHistMostRecent_Type()
)
cucsEtherTxStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistMostRecent.setStatus("current")
_CucsEtherTxStatsHistMulticastPackets_Type = Unsigned64
_CucsEtherTxStatsHistMulticastPackets_Object = MibTableColumn
cucsEtherTxStatsHistMulticastPackets = _CucsEtherTxStatsHistMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 16),
    _CucsEtherTxStatsHistMulticastPackets_Type()
)
cucsEtherTxStatsHistMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistMulticastPackets.setStatus("current")
_CucsEtherTxStatsHistMulticastPacketsDelta_Type = Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDelta = _CucsEtherTxStatsHistMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 17),
    _CucsEtherTxStatsHistMulticastPacketsDelta_Type()
)
cucsEtherTxStatsHistMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistMulticastPacketsDelta.setStatus("current")
_CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDeltaAvg = _CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 18),
    _CucsEtherTxStatsHistMulticastPacketsDeltaAvg_Type()
)
cucsEtherTxStatsHistMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistMulticastPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsHistMulticastPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDeltaMax = _CucsEtherTxStatsHistMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 19),
    _CucsEtherTxStatsHistMulticastPacketsDeltaMax_Type()
)
cucsEtherTxStatsHistMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistMulticastPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsHistMulticastPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsHistMulticastPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsHistMulticastPacketsDeltaMin = _CucsEtherTxStatsHistMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 20),
    _CucsEtherTxStatsHistMulticastPacketsDeltaMin_Type()
)
cucsEtherTxStatsHistMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistMulticastPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsHistSuspect_Type = TruthValue
_CucsEtherTxStatsHistSuspect_Object = MibTableColumn
cucsEtherTxStatsHistSuspect = _CucsEtherTxStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 21),
    _CucsEtherTxStatsHistSuspect_Type()
)
cucsEtherTxStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistSuspect.setStatus("current")
_CucsEtherTxStatsHistThresholded_Type = CucsEtherTxStatsHistThresholded
_CucsEtherTxStatsHistThresholded_Object = MibTableColumn
cucsEtherTxStatsHistThresholded = _CucsEtherTxStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 22),
    _CucsEtherTxStatsHistThresholded_Type()
)
cucsEtherTxStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistThresholded.setStatus("current")
_CucsEtherTxStatsHistTimeCollected_Type = DateAndTime
_CucsEtherTxStatsHistTimeCollected_Object = MibTableColumn
cucsEtherTxStatsHistTimeCollected = _CucsEtherTxStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 23),
    _CucsEtherTxStatsHistTimeCollected_Type()
)
cucsEtherTxStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTimeCollected.setStatus("current")
_CucsEtherTxStatsHistTotalBytes_Type = Unsigned64
_CucsEtherTxStatsHistTotalBytes_Object = MibTableColumn
cucsEtherTxStatsHistTotalBytes = _CucsEtherTxStatsHistTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 24),
    _CucsEtherTxStatsHistTotalBytes_Type()
)
cucsEtherTxStatsHistTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalBytes.setStatus("current")
_CucsEtherTxStatsHistTotalBytesDelta_Type = Unsigned64
_CucsEtherTxStatsHistTotalBytesDelta_Object = MibTableColumn
cucsEtherTxStatsHistTotalBytesDelta = _CucsEtherTxStatsHistTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 25),
    _CucsEtherTxStatsHistTotalBytesDelta_Type()
)
cucsEtherTxStatsHistTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalBytesDelta.setStatus("current")
_CucsEtherTxStatsHistTotalBytesDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsHistTotalBytesDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsHistTotalBytesDeltaAvg = _CucsEtherTxStatsHistTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 26),
    _CucsEtherTxStatsHistTotalBytesDeltaAvg_Type()
)
cucsEtherTxStatsHistTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalBytesDeltaAvg.setStatus("current")
_CucsEtherTxStatsHistTotalBytesDeltaMax_Type = Unsigned64
_CucsEtherTxStatsHistTotalBytesDeltaMax_Object = MibTableColumn
cucsEtherTxStatsHistTotalBytesDeltaMax = _CucsEtherTxStatsHistTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 27),
    _CucsEtherTxStatsHistTotalBytesDeltaMax_Type()
)
cucsEtherTxStatsHistTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalBytesDeltaMax.setStatus("current")
_CucsEtherTxStatsHistTotalBytesDeltaMin_Type = Unsigned64
_CucsEtherTxStatsHistTotalBytesDeltaMin_Object = MibTableColumn
cucsEtherTxStatsHistTotalBytesDeltaMin = _CucsEtherTxStatsHistTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 28),
    _CucsEtherTxStatsHistTotalBytesDeltaMin_Type()
)
cucsEtherTxStatsHistTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalBytesDeltaMin.setStatus("current")
_CucsEtherTxStatsHistTotalPackets_Type = Unsigned64
_CucsEtherTxStatsHistTotalPackets_Object = MibTableColumn
cucsEtherTxStatsHistTotalPackets = _CucsEtherTxStatsHistTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 29),
    _CucsEtherTxStatsHistTotalPackets_Type()
)
cucsEtherTxStatsHistTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalPackets.setStatus("current")
_CucsEtherTxStatsHistTotalPacketsDelta_Type = Unsigned64
_CucsEtherTxStatsHistTotalPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsHistTotalPacketsDelta = _CucsEtherTxStatsHistTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 30),
    _CucsEtherTxStatsHistTotalPacketsDelta_Type()
)
cucsEtherTxStatsHistTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalPacketsDelta.setStatus("current")
_CucsEtherTxStatsHistTotalPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsHistTotalPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsHistTotalPacketsDeltaAvg = _CucsEtherTxStatsHistTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 31),
    _CucsEtherTxStatsHistTotalPacketsDeltaAvg_Type()
)
cucsEtherTxStatsHistTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsHistTotalPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsHistTotalPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsHistTotalPacketsDeltaMax = _CucsEtherTxStatsHistTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 32),
    _CucsEtherTxStatsHistTotalPacketsDeltaMax_Type()
)
cucsEtherTxStatsHistTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsHistTotalPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsHistTotalPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsHistTotalPacketsDeltaMin = _CucsEtherTxStatsHistTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 33),
    _CucsEtherTxStatsHistTotalPacketsDeltaMin_Type()
)
cucsEtherTxStatsHistTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistTotalPacketsDeltaMin.setStatus("current")
_CucsEtherTxStatsHistUnicastPackets_Type = Unsigned64
_CucsEtherTxStatsHistUnicastPackets_Object = MibTableColumn
cucsEtherTxStatsHistUnicastPackets = _CucsEtherTxStatsHistUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 34),
    _CucsEtherTxStatsHistUnicastPackets_Type()
)
cucsEtherTxStatsHistUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistUnicastPackets.setStatus("current")
_CucsEtherTxStatsHistUnicastPacketsDelta_Type = Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDelta_Object = MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDelta = _CucsEtherTxStatsHistUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 35),
    _CucsEtherTxStatsHistUnicastPacketsDelta_Type()
)
cucsEtherTxStatsHistUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistUnicastPacketsDelta.setStatus("current")
_CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Type = Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Object = MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDeltaAvg = _CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 36),
    _CucsEtherTxStatsHistUnicastPacketsDeltaAvg_Type()
)
cucsEtherTxStatsHistUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistUnicastPacketsDeltaAvg.setStatus("current")
_CucsEtherTxStatsHistUnicastPacketsDeltaMax_Type = Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDeltaMax_Object = MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDeltaMax = _CucsEtherTxStatsHistUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 37),
    _CucsEtherTxStatsHistUnicastPacketsDeltaMax_Type()
)
cucsEtherTxStatsHistUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistUnicastPacketsDeltaMax.setStatus("current")
_CucsEtherTxStatsHistUnicastPacketsDeltaMin_Type = Unsigned64
_CucsEtherTxStatsHistUnicastPacketsDeltaMin_Object = MibTableColumn
cucsEtherTxStatsHistUnicastPacketsDeltaMin = _CucsEtherTxStatsHistUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 15, 1, 38),
    _CucsEtherTxStatsHistUnicastPacketsDeltaMin_Type()
)
cucsEtherTxStatsHistUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherTxStatsHistUnicastPacketsDeltaMin.setStatus("current")
_CucsEtherPortChanIdElemTable_Object = MibTable
cucsEtherPortChanIdElemTable = _CucsEtherPortChanIdElemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16)
)
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemTable.setStatus("current")
_CucsEtherPortChanIdElemEntry_Object = MibTableRow
cucsEtherPortChanIdElemEntry = _CucsEtherPortChanIdElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16, 1)
)
cucsEtherPortChanIdElemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPortChanIdElemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemEntry.setStatus("current")
_CucsEtherPortChanIdElemInstanceId_Type = CucsManagedObjectId
_CucsEtherPortChanIdElemInstanceId_Object = MibTableColumn
cucsEtherPortChanIdElemInstanceId = _CucsEtherPortChanIdElemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16, 1, 1),
    _CucsEtherPortChanIdElemInstanceId_Type()
)
cucsEtherPortChanIdElemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemInstanceId.setStatus("current")
_CucsEtherPortChanIdElemDn_Type = CucsManagedObjectDn
_CucsEtherPortChanIdElemDn_Object = MibTableColumn
cucsEtherPortChanIdElemDn = _CucsEtherPortChanIdElemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16, 1, 2),
    _CucsEtherPortChanIdElemDn_Type()
)
cucsEtherPortChanIdElemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemDn.setStatus("current")
_CucsEtherPortChanIdElemRn_Type = SnmpAdminString
_CucsEtherPortChanIdElemRn_Object = MibTableColumn
cucsEtherPortChanIdElemRn = _CucsEtherPortChanIdElemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16, 1, 3),
    _CucsEtherPortChanIdElemRn_Type()
)
cucsEtherPortChanIdElemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemRn.setStatus("current")
_CucsEtherPortChanIdElemId_Type = Gauge32
_CucsEtherPortChanIdElemId_Object = MibTableColumn
cucsEtherPortChanIdElemId = _CucsEtherPortChanIdElemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16, 1, 4),
    _CucsEtherPortChanIdElemId_Type()
)
cucsEtherPortChanIdElemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemId.setStatus("current")
_CucsEtherPortChanIdElemAssignedToDn_Type = SnmpAdminString
_CucsEtherPortChanIdElemAssignedToDn_Object = MibTableColumn
cucsEtherPortChanIdElemAssignedToDn = _CucsEtherPortChanIdElemAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16, 1, 5),
    _CucsEtherPortChanIdElemAssignedToDn_Type()
)
cucsEtherPortChanIdElemAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemAssignedToDn.setStatus("current")
_CucsEtherPortChanIdElemPrevAssignedToDn_Type = SnmpAdminString
_CucsEtherPortChanIdElemPrevAssignedToDn_Object = MibTableColumn
cucsEtherPortChanIdElemPrevAssignedToDn = _CucsEtherPortChanIdElemPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 16, 1, 6),
    _CucsEtherPortChanIdElemPrevAssignedToDn_Type()
)
cucsEtherPortChanIdElemPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdElemPrevAssignedToDn.setStatus("current")
_CucsEtherPortChanIdUniverseTable_Object = MibTable
cucsEtherPortChanIdUniverseTable = _CucsEtherPortChanIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 17)
)
if mibBuilder.loadTexts:
    cucsEtherPortChanIdUniverseTable.setStatus("current")
_CucsEtherPortChanIdUniverseEntry_Object = MibTableRow
cucsEtherPortChanIdUniverseEntry = _CucsEtherPortChanIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 17, 1)
)
cucsEtherPortChanIdUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPortChanIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPortChanIdUniverseEntry.setStatus("current")
_CucsEtherPortChanIdUniverseInstanceId_Type = CucsManagedObjectId
_CucsEtherPortChanIdUniverseInstanceId_Object = MibTableColumn
cucsEtherPortChanIdUniverseInstanceId = _CucsEtherPortChanIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 17, 1, 1),
    _CucsEtherPortChanIdUniverseInstanceId_Type()
)
cucsEtherPortChanIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdUniverseInstanceId.setStatus("current")
_CucsEtherPortChanIdUniverseDn_Type = CucsManagedObjectDn
_CucsEtherPortChanIdUniverseDn_Object = MibTableColumn
cucsEtherPortChanIdUniverseDn = _CucsEtherPortChanIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 17, 1, 2),
    _CucsEtherPortChanIdUniverseDn_Type()
)
cucsEtherPortChanIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdUniverseDn.setStatus("current")
_CucsEtherPortChanIdUniverseRn_Type = SnmpAdminString
_CucsEtherPortChanIdUniverseRn_Object = MibTableColumn
cucsEtherPortChanIdUniverseRn = _CucsEtherPortChanIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 17, 1, 3),
    _CucsEtherPortChanIdUniverseRn_Type()
)
cucsEtherPortChanIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPortChanIdUniverseRn.setStatus("current")
_CucsEtherServerIntFIoPcTable_Object = MibTable
cucsEtherServerIntFIoPcTable = _CucsEtherServerIntFIoPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18)
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcTable.setStatus("current")
_CucsEtherServerIntFIoPcEntry_Object = MibTableRow
cucsEtherServerIntFIoPcEntry = _CucsEtherServerIntFIoPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1)
)
cucsEtherServerIntFIoPcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherServerIntFIoPcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEntry.setStatus("current")
_CucsEtherServerIntFIoPcInstanceId_Type = CucsManagedObjectId
_CucsEtherServerIntFIoPcInstanceId_Object = MibTableColumn
cucsEtherServerIntFIoPcInstanceId = _CucsEtherServerIntFIoPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 1),
    _CucsEtherServerIntFIoPcInstanceId_Type()
)
cucsEtherServerIntFIoPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcInstanceId.setStatus("current")
_CucsEtherServerIntFIoPcDn_Type = CucsManagedObjectDn
_CucsEtherServerIntFIoPcDn_Object = MibTableColumn
cucsEtherServerIntFIoPcDn = _CucsEtherServerIntFIoPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 2),
    _CucsEtherServerIntFIoPcDn_Type()
)
cucsEtherServerIntFIoPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcDn.setStatus("current")
_CucsEtherServerIntFIoPcRn_Type = SnmpAdminString
_CucsEtherServerIntFIoPcRn_Object = MibTableColumn
cucsEtherServerIntFIoPcRn = _CucsEtherServerIntFIoPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 3),
    _CucsEtherServerIntFIoPcRn_Type()
)
cucsEtherServerIntFIoPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcRn.setStatus("current")
_CucsEtherServerIntFIoPcChassisId_Type = Gauge32
_CucsEtherServerIntFIoPcChassisId_Object = MibTableColumn
cucsEtherServerIntFIoPcChassisId = _CucsEtherServerIntFIoPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 4),
    _CucsEtherServerIntFIoPcChassisId_Type()
)
cucsEtherServerIntFIoPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcChassisId.setStatus("current")
_CucsEtherServerIntFIoPcEpDn_Type = SnmpAdminString
_CucsEtherServerIntFIoPcEpDn_Object = MibTableColumn
cucsEtherServerIntFIoPcEpDn = _CucsEtherServerIntFIoPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 5),
    _CucsEtherServerIntFIoPcEpDn_Type()
)
cucsEtherServerIntFIoPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpDn.setStatus("current")
_CucsEtherServerIntFIoPcFltAggr_Type = Unsigned64
_CucsEtherServerIntFIoPcFltAggr_Object = MibTableColumn
cucsEtherServerIntFIoPcFltAggr = _CucsEtherServerIntFIoPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 6),
    _CucsEtherServerIntFIoPcFltAggr_Type()
)
cucsEtherServerIntFIoPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcFltAggr.setStatus("current")
_CucsEtherServerIntFIoPcIfRole_Type = CucsEtherServerIntFIoPcIfRole
_CucsEtherServerIntFIoPcIfRole_Object = MibTableColumn
cucsEtherServerIntFIoPcIfRole = _CucsEtherServerIntFIoPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 7),
    _CucsEtherServerIntFIoPcIfRole_Type()
)
cucsEtherServerIntFIoPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcIfRole.setStatus("current")
_CucsEtherServerIntFIoPcIfType_Type = CucsEtherCIoEpIfType
_CucsEtherServerIntFIoPcIfType_Object = MibTableColumn
cucsEtherServerIntFIoPcIfType = _CucsEtherServerIntFIoPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 8),
    _CucsEtherServerIntFIoPcIfType_Type()
)
cucsEtherServerIntFIoPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcIfType.setStatus("current")
_CucsEtherServerIntFIoPcLocale_Type = CucsEtherInternalPcLocale
_CucsEtherServerIntFIoPcLocale_Object = MibTableColumn
cucsEtherServerIntFIoPcLocale = _CucsEtherServerIntFIoPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 9),
    _CucsEtherServerIntFIoPcLocale_Type()
)
cucsEtherServerIntFIoPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcLocale.setStatus("current")
_CucsEtherServerIntFIoPcName_Type = SnmpAdminString
_CucsEtherServerIntFIoPcName_Object = MibTableColumn
cucsEtherServerIntFIoPcName = _CucsEtherServerIntFIoPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 10),
    _CucsEtherServerIntFIoPcName_Type()
)
cucsEtherServerIntFIoPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcName.setStatus("current")
_CucsEtherServerIntFIoPcOperSpeed_Type = CucsPortEthSpeed
_CucsEtherServerIntFIoPcOperSpeed_Object = MibTableColumn
cucsEtherServerIntFIoPcOperSpeed = _CucsEtherServerIntFIoPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 11),
    _CucsEtherServerIntFIoPcOperSpeed_Type()
)
cucsEtherServerIntFIoPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcOperSpeed.setStatus("current")
_CucsEtherServerIntFIoPcOperState_Type = CucsNetworkPortOperState
_CucsEtherServerIntFIoPcOperState_Object = MibTableColumn
cucsEtherServerIntFIoPcOperState = _CucsEtherServerIntFIoPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 12),
    _CucsEtherServerIntFIoPcOperState_Type()
)
cucsEtherServerIntFIoPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcOperState.setStatus("current")
_CucsEtherServerIntFIoPcPeerDn_Type = SnmpAdminString
_CucsEtherServerIntFIoPcPeerDn_Object = MibTableColumn
cucsEtherServerIntFIoPcPeerDn = _CucsEtherServerIntFIoPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 13),
    _CucsEtherServerIntFIoPcPeerDn_Type()
)
cucsEtherServerIntFIoPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcPeerDn.setStatus("current")
_CucsEtherServerIntFIoPcPortId_Type = CucsEtherServerIntFIoPcPortId
_CucsEtherServerIntFIoPcPortId_Object = MibTableColumn
cucsEtherServerIntFIoPcPortId = _CucsEtherServerIntFIoPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 14),
    _CucsEtherServerIntFIoPcPortId_Type()
)
cucsEtherServerIntFIoPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcPortId.setStatus("current")
_CucsEtherServerIntFIoPcStateQual_Type = SnmpAdminString
_CucsEtherServerIntFIoPcStateQual_Object = MibTableColumn
cucsEtherServerIntFIoPcStateQual = _CucsEtherServerIntFIoPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 15),
    _CucsEtherServerIntFIoPcStateQual_Type()
)
cucsEtherServerIntFIoPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcStateQual.setStatus("current")
_CucsEtherServerIntFIoPcSwitchId_Type = CucsNetworkSwitchId
_CucsEtherServerIntFIoPcSwitchId_Object = MibTableColumn
cucsEtherServerIntFIoPcSwitchId = _CucsEtherServerIntFIoPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 16),
    _CucsEtherServerIntFIoPcSwitchId_Type()
)
cucsEtherServerIntFIoPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcSwitchId.setStatus("current")
_CucsEtherServerIntFIoPcTransport_Type = CucsEtherServerIntFIoPcTransport
_CucsEtherServerIntFIoPcTransport_Object = MibTableColumn
cucsEtherServerIntFIoPcTransport = _CucsEtherServerIntFIoPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 17),
    _CucsEtherServerIntFIoPcTransport_Type()
)
cucsEtherServerIntFIoPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcTransport.setStatus("current")
_CucsEtherServerIntFIoPcType_Type = CucsEtherServerIntFIoPcType
_CucsEtherServerIntFIoPcType_Object = MibTableColumn
cucsEtherServerIntFIoPcType = _CucsEtherServerIntFIoPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 18, 1, 18),
    _CucsEtherServerIntFIoPcType_Type()
)
cucsEtherServerIntFIoPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcType.setStatus("current")
_CucsEtherServerIntFIoPcEpTable_Object = MibTable
cucsEtherServerIntFIoPcEpTable = _CucsEtherServerIntFIoPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19)
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpTable.setStatus("current")
_CucsEtherServerIntFIoPcEpEntry_Object = MibTableRow
cucsEtherServerIntFIoPcEpEntry = _CucsEtherServerIntFIoPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1)
)
cucsEtherServerIntFIoPcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherServerIntFIoPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpEntry.setStatus("current")
_CucsEtherServerIntFIoPcEpInstanceId_Type = CucsManagedObjectId
_CucsEtherServerIntFIoPcEpInstanceId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpInstanceId = _CucsEtherServerIntFIoPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 1),
    _CucsEtherServerIntFIoPcEpInstanceId_Type()
)
cucsEtherServerIntFIoPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpInstanceId.setStatus("current")
_CucsEtherServerIntFIoPcEpDnData_Type = CucsManagedObjectDn
_CucsEtherServerIntFIoPcEpDnData_Object = MibTableColumn
cucsEtherServerIntFIoPcEpDnData = _CucsEtherServerIntFIoPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 2),
    _CucsEtherServerIntFIoPcEpDnData_Type()
)
cucsEtherServerIntFIoPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpDnData.setStatus("current")
_CucsEtherServerIntFIoPcEpRn_Type = SnmpAdminString
_CucsEtherServerIntFIoPcEpRn_Object = MibTableColumn
cucsEtherServerIntFIoPcEpRn = _CucsEtherServerIntFIoPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 3),
    _CucsEtherServerIntFIoPcEpRn_Type()
)
cucsEtherServerIntFIoPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpRn.setStatus("current")
_CucsEtherServerIntFIoPcEpAdminState_Type = CucsEtherExternalEpAdminState
_CucsEtherServerIntFIoPcEpAdminState_Object = MibTableColumn
cucsEtherServerIntFIoPcEpAdminState = _CucsEtherServerIntFIoPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 4),
    _CucsEtherServerIntFIoPcEpAdminState_Type()
)
cucsEtherServerIntFIoPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpAdminState.setStatus("current")
_CucsEtherServerIntFIoPcEpChassisId_Type = Gauge32
_CucsEtherServerIntFIoPcEpChassisId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpChassisId = _CucsEtherServerIntFIoPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 5),
    _CucsEtherServerIntFIoPcEpChassisId_Type()
)
cucsEtherServerIntFIoPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpChassisId.setStatus("current")
_CucsEtherServerIntFIoPcEpEpDn_Type = SnmpAdminString
_CucsEtherServerIntFIoPcEpEpDn_Object = MibTableColumn
cucsEtherServerIntFIoPcEpEpDn = _CucsEtherServerIntFIoPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 6),
    _CucsEtherServerIntFIoPcEpEpDn_Type()
)
cucsEtherServerIntFIoPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpEpDn.setStatus("current")
_CucsEtherServerIntFIoPcEpIfRole_Type = CucsEtherServerIntFIoPcEpIfRole
_CucsEtherServerIntFIoPcEpIfRole_Object = MibTableColumn
cucsEtherServerIntFIoPcEpIfRole = _CucsEtherServerIntFIoPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 7),
    _CucsEtherServerIntFIoPcEpIfRole_Type()
)
cucsEtherServerIntFIoPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpIfRole.setStatus("current")
_CucsEtherServerIntFIoPcEpIfType_Type = CucsEtherPIoEpIfType
_CucsEtherServerIntFIoPcEpIfType_Object = MibTableColumn
cucsEtherServerIntFIoPcEpIfType = _CucsEtherServerIntFIoPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 8),
    _CucsEtherServerIntFIoPcEpIfType_Type()
)
cucsEtherServerIntFIoPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpIfType.setStatus("current")
_CucsEtherServerIntFIoPcEpLocale_Type = CucsEtherExternalEpLocale
_CucsEtherServerIntFIoPcEpLocale_Object = MibTableColumn
cucsEtherServerIntFIoPcEpLocale = _CucsEtherServerIntFIoPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 9),
    _CucsEtherServerIntFIoPcEpLocale_Type()
)
cucsEtherServerIntFIoPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpLocale.setStatus("current")
_CucsEtherServerIntFIoPcEpMembership_Type = CucsFabricMembershipStatus
_CucsEtherServerIntFIoPcEpMembership_Object = MibTableColumn
cucsEtherServerIntFIoPcEpMembership = _CucsEtherServerIntFIoPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 10),
    _CucsEtherServerIntFIoPcEpMembership_Type()
)
cucsEtherServerIntFIoPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpMembership.setStatus("current")
_CucsEtherServerIntFIoPcEpName_Type = SnmpAdminString
_CucsEtherServerIntFIoPcEpName_Object = MibTableColumn
cucsEtherServerIntFIoPcEpName = _CucsEtherServerIntFIoPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 11),
    _CucsEtherServerIntFIoPcEpName_Type()
)
cucsEtherServerIntFIoPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpName.setStatus("current")
_CucsEtherServerIntFIoPcEpPeerChassisId_Type = Gauge32
_CucsEtherServerIntFIoPcEpPeerChassisId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpPeerChassisId = _CucsEtherServerIntFIoPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 12),
    _CucsEtherServerIntFIoPcEpPeerChassisId_Type()
)
cucsEtherServerIntFIoPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpPeerChassisId.setStatus("current")
_CucsEtherServerIntFIoPcEpPeerDn_Type = SnmpAdminString
_CucsEtherServerIntFIoPcEpPeerDn_Object = MibTableColumn
cucsEtherServerIntFIoPcEpPeerDn = _CucsEtherServerIntFIoPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 13),
    _CucsEtherServerIntFIoPcEpPeerDn_Type()
)
cucsEtherServerIntFIoPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpPeerDn.setStatus("current")
_CucsEtherServerIntFIoPcEpPeerPortId_Type = Gauge32
_CucsEtherServerIntFIoPcEpPeerPortId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpPeerPortId = _CucsEtherServerIntFIoPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 14),
    _CucsEtherServerIntFIoPcEpPeerPortId_Type()
)
cucsEtherServerIntFIoPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpPeerPortId.setStatus("current")
_CucsEtherServerIntFIoPcEpPeerSlotId_Type = Gauge32
_CucsEtherServerIntFIoPcEpPeerSlotId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpPeerSlotId = _CucsEtherServerIntFIoPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 15),
    _CucsEtherServerIntFIoPcEpPeerSlotId_Type()
)
cucsEtherServerIntFIoPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpPeerSlotId.setStatus("current")
_CucsEtherServerIntFIoPcEpPortId_Type = CucsEtherServerIntFIoPcEpPortId
_CucsEtherServerIntFIoPcEpPortId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpPortId = _CucsEtherServerIntFIoPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 16),
    _CucsEtherServerIntFIoPcEpPortId_Type()
)
cucsEtherServerIntFIoPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpPortId.setStatus("current")
_CucsEtherServerIntFIoPcEpSlotId_Type = Gauge32
_CucsEtherServerIntFIoPcEpSlotId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpSlotId = _CucsEtherServerIntFIoPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 17),
    _CucsEtherServerIntFIoPcEpSlotId_Type()
)
cucsEtherServerIntFIoPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpSlotId.setStatus("current")
_CucsEtherServerIntFIoPcEpSwitchId_Type = CucsNetworkSwitchId
_CucsEtherServerIntFIoPcEpSwitchId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpSwitchId = _CucsEtherServerIntFIoPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 18),
    _CucsEtherServerIntFIoPcEpSwitchId_Type()
)
cucsEtherServerIntFIoPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpSwitchId.setStatus("current")
_CucsEtherServerIntFIoPcEpTransport_Type = CucsNetworkTransport
_CucsEtherServerIntFIoPcEpTransport_Object = MibTableColumn
cucsEtherServerIntFIoPcEpTransport = _CucsEtherServerIntFIoPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 19),
    _CucsEtherServerIntFIoPcEpTransport_Type()
)
cucsEtherServerIntFIoPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpTransport.setStatus("current")
_CucsEtherServerIntFIoPcEpType_Type = CucsEtherIntFIoEpType
_CucsEtherServerIntFIoPcEpType_Object = MibTableColumn
cucsEtherServerIntFIoPcEpType = _CucsEtherServerIntFIoPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 20),
    _CucsEtherServerIntFIoPcEpType_Type()
)
cucsEtherServerIntFIoPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpType.setStatus("current")
_CucsEtherServerIntFIoPcEpAggrPortId_Type = Gauge32
_CucsEtherServerIntFIoPcEpAggrPortId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpAggrPortId = _CucsEtherServerIntFIoPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 21),
    _CucsEtherServerIntFIoPcEpAggrPortId_Type()
)
cucsEtherServerIntFIoPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpAggrPortId.setStatus("current")
_CucsEtherServerIntFIoPcEpPeerAggrPortId_Type = Gauge32
_CucsEtherServerIntFIoPcEpPeerAggrPortId_Object = MibTableColumn
cucsEtherServerIntFIoPcEpPeerAggrPortId = _CucsEtherServerIntFIoPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 19, 1, 22),
    _CucsEtherServerIntFIoPcEpPeerAggrPortId_Type()
)
cucsEtherServerIntFIoPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoPcEpPeerAggrPortId.setStatus("current")
_CucsEtherSwitchIntFIoPcTable_Object = MibTable
cucsEtherSwitchIntFIoPcTable = _CucsEtherSwitchIntFIoPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20)
)
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcTable.setStatus("current")
_CucsEtherSwitchIntFIoPcEntry_Object = MibTableRow
cucsEtherSwitchIntFIoPcEntry = _CucsEtherSwitchIntFIoPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1)
)
cucsEtherSwitchIntFIoPcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherSwitchIntFIoPcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEntry.setStatus("current")
_CucsEtherSwitchIntFIoPcInstanceId_Type = CucsManagedObjectId
_CucsEtherSwitchIntFIoPcInstanceId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcInstanceId = _CucsEtherSwitchIntFIoPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 1),
    _CucsEtherSwitchIntFIoPcInstanceId_Type()
)
cucsEtherSwitchIntFIoPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcInstanceId.setStatus("current")
_CucsEtherSwitchIntFIoPcDn_Type = CucsManagedObjectDn
_CucsEtherSwitchIntFIoPcDn_Object = MibTableColumn
cucsEtherSwitchIntFIoPcDn = _CucsEtherSwitchIntFIoPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 2),
    _CucsEtherSwitchIntFIoPcDn_Type()
)
cucsEtherSwitchIntFIoPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcDn.setStatus("current")
_CucsEtherSwitchIntFIoPcRn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcRn_Object = MibTableColumn
cucsEtherSwitchIntFIoPcRn = _CucsEtherSwitchIntFIoPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 3),
    _CucsEtherSwitchIntFIoPcRn_Type()
)
cucsEtherSwitchIntFIoPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcRn.setStatus("current")
_CucsEtherSwitchIntFIoPcAdminState_Type = CucsEtherExternalPcAdminState
_CucsEtherSwitchIntFIoPcAdminState_Object = MibTableColumn
cucsEtherSwitchIntFIoPcAdminState = _CucsEtherSwitchIntFIoPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 4),
    _CucsEtherSwitchIntFIoPcAdminState_Type()
)
cucsEtherSwitchIntFIoPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcAdminState.setStatus("current")
_CucsEtherSwitchIntFIoPcChassisId_Type = Gauge32
_CucsEtherSwitchIntFIoPcChassisId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcChassisId = _CucsEtherSwitchIntFIoPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 5),
    _CucsEtherSwitchIntFIoPcChassisId_Type()
)
cucsEtherSwitchIntFIoPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcChassisId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpDn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcEpDn_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpDn = _CucsEtherSwitchIntFIoPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 6),
    _CucsEtherSwitchIntFIoPcEpDn_Type()
)
cucsEtherSwitchIntFIoPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpDn.setStatus("current")
_CucsEtherSwitchIntFIoPcFltAggr_Type = Unsigned64
_CucsEtherSwitchIntFIoPcFltAggr_Object = MibTableColumn
cucsEtherSwitchIntFIoPcFltAggr = _CucsEtherSwitchIntFIoPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 7),
    _CucsEtherSwitchIntFIoPcFltAggr_Type()
)
cucsEtherSwitchIntFIoPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcFltAggr.setStatus("current")
_CucsEtherSwitchIntFIoPcIfRole_Type = CucsEtherSwitchIntFIoPcIfRole
_CucsEtherSwitchIntFIoPcIfRole_Object = MibTableColumn
cucsEtherSwitchIntFIoPcIfRole = _CucsEtherSwitchIntFIoPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 8),
    _CucsEtherSwitchIntFIoPcIfRole_Type()
)
cucsEtherSwitchIntFIoPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcIfRole.setStatus("current")
_CucsEtherSwitchIntFIoPcIfType_Type = CucsEtherCIoEpIfType
_CucsEtherSwitchIntFIoPcIfType_Object = MibTableColumn
cucsEtherSwitchIntFIoPcIfType = _CucsEtherSwitchIntFIoPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 9),
    _CucsEtherSwitchIntFIoPcIfType_Type()
)
cucsEtherSwitchIntFIoPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcIfType.setStatus("current")
_CucsEtherSwitchIntFIoPcLocale_Type = CucsEtherExternalPcLocale
_CucsEtherSwitchIntFIoPcLocale_Object = MibTableColumn
cucsEtherSwitchIntFIoPcLocale = _CucsEtherSwitchIntFIoPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 10),
    _CucsEtherSwitchIntFIoPcLocale_Type()
)
cucsEtherSwitchIntFIoPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcLocale.setStatus("current")
_CucsEtherSwitchIntFIoPcName_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcName_Object = MibTableColumn
cucsEtherSwitchIntFIoPcName = _CucsEtherSwitchIntFIoPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 11),
    _CucsEtherSwitchIntFIoPcName_Type()
)
cucsEtherSwitchIntFIoPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcName.setStatus("current")
_CucsEtherSwitchIntFIoPcOperSpeed_Type = CucsPortEthSpeed
_CucsEtherSwitchIntFIoPcOperSpeed_Object = MibTableColumn
cucsEtherSwitchIntFIoPcOperSpeed = _CucsEtherSwitchIntFIoPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 12),
    _CucsEtherSwitchIntFIoPcOperSpeed_Type()
)
cucsEtherSwitchIntFIoPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcOperSpeed.setStatus("current")
_CucsEtherSwitchIntFIoPcOperState_Type = CucsNetworkPortOperState
_CucsEtherSwitchIntFIoPcOperState_Object = MibTableColumn
cucsEtherSwitchIntFIoPcOperState = _CucsEtherSwitchIntFIoPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 13),
    _CucsEtherSwitchIntFIoPcOperState_Type()
)
cucsEtherSwitchIntFIoPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcOperState.setStatus("current")
_CucsEtherSwitchIntFIoPcPeerDn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcPeerDn_Object = MibTableColumn
cucsEtherSwitchIntFIoPcPeerDn = _CucsEtherSwitchIntFIoPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 14),
    _CucsEtherSwitchIntFIoPcPeerDn_Type()
)
cucsEtherSwitchIntFIoPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcPeerDn.setStatus("current")
_CucsEtherSwitchIntFIoPcPortId_Type = CucsEtherSwitchIntFIoPcPortId
_CucsEtherSwitchIntFIoPcPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcPortId = _CucsEtherSwitchIntFIoPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 15),
    _CucsEtherSwitchIntFIoPcPortId_Type()
)
cucsEtherSwitchIntFIoPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcPortId.setStatus("current")
_CucsEtherSwitchIntFIoPcStateQual_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcStateQual_Object = MibTableColumn
cucsEtherSwitchIntFIoPcStateQual = _CucsEtherSwitchIntFIoPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 16),
    _CucsEtherSwitchIntFIoPcStateQual_Type()
)
cucsEtherSwitchIntFIoPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcStateQual.setStatus("current")
_CucsEtherSwitchIntFIoPcSwitchId_Type = CucsNetworkSwitchId
_CucsEtherSwitchIntFIoPcSwitchId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcSwitchId = _CucsEtherSwitchIntFIoPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 17),
    _CucsEtherSwitchIntFIoPcSwitchId_Type()
)
cucsEtherSwitchIntFIoPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcSwitchId.setStatus("current")
_CucsEtherSwitchIntFIoPcTransport_Type = CucsEtherSwitchIntFIoPcTransport
_CucsEtherSwitchIntFIoPcTransport_Object = MibTableColumn
cucsEtherSwitchIntFIoPcTransport = _CucsEtherSwitchIntFIoPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 18),
    _CucsEtherSwitchIntFIoPcTransport_Type()
)
cucsEtherSwitchIntFIoPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcTransport.setStatus("current")
_CucsEtherSwitchIntFIoPcType_Type = CucsEtherSwitchIntFIoPcType
_CucsEtherSwitchIntFIoPcType_Object = MibTableColumn
cucsEtherSwitchIntFIoPcType = _CucsEtherSwitchIntFIoPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 19),
    _CucsEtherSwitchIntFIoPcType_Type()
)
cucsEtherSwitchIntFIoPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcType.setStatus("current")
_CucsEtherSwitchIntFIoPcMulticastHwHash_Type = CucsEtherSwitchIntFIoPcMulticastHwHash
_CucsEtherSwitchIntFIoPcMulticastHwHash_Object = MibTableColumn
cucsEtherSwitchIntFIoPcMulticastHwHash = _CucsEtherSwitchIntFIoPcMulticastHwHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 20, 1, 20),
    _CucsEtherSwitchIntFIoPcMulticastHwHash_Type()
)
cucsEtherSwitchIntFIoPcMulticastHwHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcMulticastHwHash.setStatus("current")
_CucsEtherSwitchIntFIoPcEpTable_Object = MibTable
cucsEtherSwitchIntFIoPcEpTable = _CucsEtherSwitchIntFIoPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21)
)
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpTable.setStatus("current")
_CucsEtherSwitchIntFIoPcEpEntry_Object = MibTableRow
cucsEtherSwitchIntFIoPcEpEntry = _CucsEtherSwitchIntFIoPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1)
)
cucsEtherSwitchIntFIoPcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherSwitchIntFIoPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpEntry.setStatus("current")
_CucsEtherSwitchIntFIoPcEpInstanceId_Type = CucsManagedObjectId
_CucsEtherSwitchIntFIoPcEpInstanceId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpInstanceId = _CucsEtherSwitchIntFIoPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 1),
    _CucsEtherSwitchIntFIoPcEpInstanceId_Type()
)
cucsEtherSwitchIntFIoPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpInstanceId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpDnData_Type = CucsManagedObjectDn
_CucsEtherSwitchIntFIoPcEpDnData_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpDnData = _CucsEtherSwitchIntFIoPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 2),
    _CucsEtherSwitchIntFIoPcEpDnData_Type()
)
cucsEtherSwitchIntFIoPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpDnData.setStatus("current")
_CucsEtherSwitchIntFIoPcEpRn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcEpRn_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpRn = _CucsEtherSwitchIntFIoPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 3),
    _CucsEtherSwitchIntFIoPcEpRn_Type()
)
cucsEtherSwitchIntFIoPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpRn.setStatus("current")
_CucsEtherSwitchIntFIoPcEpAdminState_Type = CucsEtherExternalEpAdminState
_CucsEtherSwitchIntFIoPcEpAdminState_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpAdminState = _CucsEtherSwitchIntFIoPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 4),
    _CucsEtherSwitchIntFIoPcEpAdminState_Type()
)
cucsEtherSwitchIntFIoPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpAdminState.setStatus("current")
_CucsEtherSwitchIntFIoPcEpChassisId_Type = Gauge32
_CucsEtherSwitchIntFIoPcEpChassisId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpChassisId = _CucsEtherSwitchIntFIoPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 5),
    _CucsEtherSwitchIntFIoPcEpChassisId_Type()
)
cucsEtherSwitchIntFIoPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpChassisId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpEpDn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcEpEpDn_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpEpDn = _CucsEtherSwitchIntFIoPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 6),
    _CucsEtherSwitchIntFIoPcEpEpDn_Type()
)
cucsEtherSwitchIntFIoPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpEpDn.setStatus("current")
_CucsEtherSwitchIntFIoPcEpIfRole_Type = CucsEtherSwitchIntFIoPcEpIfRole
_CucsEtherSwitchIntFIoPcEpIfRole_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpIfRole = _CucsEtherSwitchIntFIoPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 7),
    _CucsEtherSwitchIntFIoPcEpIfRole_Type()
)
cucsEtherSwitchIntFIoPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpIfRole.setStatus("current")
_CucsEtherSwitchIntFIoPcEpIfType_Type = CucsEtherPIoEpIfType
_CucsEtherSwitchIntFIoPcEpIfType_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpIfType = _CucsEtherSwitchIntFIoPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 8),
    _CucsEtherSwitchIntFIoPcEpIfType_Type()
)
cucsEtherSwitchIntFIoPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpIfType.setStatus("current")
_CucsEtherSwitchIntFIoPcEpLocale_Type = CucsEtherExternalEpLocale
_CucsEtherSwitchIntFIoPcEpLocale_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpLocale = _CucsEtherSwitchIntFIoPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 9),
    _CucsEtherSwitchIntFIoPcEpLocale_Type()
)
cucsEtherSwitchIntFIoPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpLocale.setStatus("current")
_CucsEtherSwitchIntFIoPcEpMembership_Type = CucsFabricMembershipStatus
_CucsEtherSwitchIntFIoPcEpMembership_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpMembership = _CucsEtherSwitchIntFIoPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 10),
    _CucsEtherSwitchIntFIoPcEpMembership_Type()
)
cucsEtherSwitchIntFIoPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpMembership.setStatus("current")
_CucsEtherSwitchIntFIoPcEpName_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcEpName_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpName = _CucsEtherSwitchIntFIoPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 11),
    _CucsEtherSwitchIntFIoPcEpName_Type()
)
cucsEtherSwitchIntFIoPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpName.setStatus("current")
_CucsEtherSwitchIntFIoPcEpPeerChassisId_Type = Gauge32
_CucsEtherSwitchIntFIoPcEpPeerChassisId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerChassisId = _CucsEtherSwitchIntFIoPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 12),
    _CucsEtherSwitchIntFIoPcEpPeerChassisId_Type()
)
cucsEtherSwitchIntFIoPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpPeerChassisId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpPeerDn_Type = SnmpAdminString
_CucsEtherSwitchIntFIoPcEpPeerDn_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerDn = _CucsEtherSwitchIntFIoPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 13),
    _CucsEtherSwitchIntFIoPcEpPeerDn_Type()
)
cucsEtherSwitchIntFIoPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpPeerDn.setStatus("current")
_CucsEtherSwitchIntFIoPcEpPeerPortId_Type = Gauge32
_CucsEtherSwitchIntFIoPcEpPeerPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerPortId = _CucsEtherSwitchIntFIoPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 14),
    _CucsEtherSwitchIntFIoPcEpPeerPortId_Type()
)
cucsEtherSwitchIntFIoPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpPeerPortId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpPeerSlotId_Type = Gauge32
_CucsEtherSwitchIntFIoPcEpPeerSlotId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerSlotId = _CucsEtherSwitchIntFIoPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 15),
    _CucsEtherSwitchIntFIoPcEpPeerSlotId_Type()
)
cucsEtherSwitchIntFIoPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpPeerSlotId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpPortId_Type = CucsEtherSwitchIntFIoPcEpPortId
_CucsEtherSwitchIntFIoPcEpPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpPortId = _CucsEtherSwitchIntFIoPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 16),
    _CucsEtherSwitchIntFIoPcEpPortId_Type()
)
cucsEtherSwitchIntFIoPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpPortId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpSlotId_Type = Gauge32
_CucsEtherSwitchIntFIoPcEpSlotId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpSlotId = _CucsEtherSwitchIntFIoPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 17),
    _CucsEtherSwitchIntFIoPcEpSlotId_Type()
)
cucsEtherSwitchIntFIoPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpSlotId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpStatusChangeTs_Type = DateAndTime
_CucsEtherSwitchIntFIoPcEpStatusChangeTs_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpStatusChangeTs = _CucsEtherSwitchIntFIoPcEpStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 18),
    _CucsEtherSwitchIntFIoPcEpStatusChangeTs_Type()
)
cucsEtherSwitchIntFIoPcEpStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpStatusChangeTs.setStatus("current")
_CucsEtherSwitchIntFIoPcEpSwitchId_Type = CucsNetworkSwitchId
_CucsEtherSwitchIntFIoPcEpSwitchId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpSwitchId = _CucsEtherSwitchIntFIoPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 19),
    _CucsEtherSwitchIntFIoPcEpSwitchId_Type()
)
cucsEtherSwitchIntFIoPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpSwitchId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpTransport_Type = CucsNetworkTransport
_CucsEtherSwitchIntFIoPcEpTransport_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpTransport = _CucsEtherSwitchIntFIoPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 20),
    _CucsEtherSwitchIntFIoPcEpTransport_Type()
)
cucsEtherSwitchIntFIoPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpTransport.setStatus("current")
_CucsEtherSwitchIntFIoPcEpType_Type = CucsEtherIntFIoEpType
_CucsEtherSwitchIntFIoPcEpType_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpType = _CucsEtherSwitchIntFIoPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 21),
    _CucsEtherSwitchIntFIoPcEpType_Type()
)
cucsEtherSwitchIntFIoPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpType.setStatus("current")
_CucsEtherSwitchIntFIoPcEpAckState_Type = CucsEquipmentChassisConfigState
_CucsEtherSwitchIntFIoPcEpAckState_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpAckState = _CucsEtherSwitchIntFIoPcEpAckState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 22),
    _CucsEtherSwitchIntFIoPcEpAckState_Type()
)
cucsEtherSwitchIntFIoPcEpAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpAckState.setStatus("current")
_CucsEtherSwitchIntFIoPcEpAggrPortId_Type = Gauge32
_CucsEtherSwitchIntFIoPcEpAggrPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpAggrPortId = _CucsEtherSwitchIntFIoPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 23),
    _CucsEtherSwitchIntFIoPcEpAggrPortId_Type()
)
cucsEtherSwitchIntFIoPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpAggrPortId.setStatus("current")
_CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Type = Gauge32
_CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Object = MibTableColumn
cucsEtherSwitchIntFIoPcEpPeerAggrPortId = _CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 21, 1, 24),
    _CucsEtherSwitchIntFIoPcEpPeerAggrPortId_Type()
)
cucsEtherSwitchIntFIoPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherSwitchIntFIoPcEpPeerAggrPortId.setStatus("current")
_CucsEtherServerIntFIoFsmTaskTable_Object = MibTable
cucsEtherServerIntFIoFsmTaskTable = _CucsEtherServerIntFIoFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22)
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskTable.setStatus("current")
_CucsEtherServerIntFIoFsmTaskEntry_Object = MibTableRow
cucsEtherServerIntFIoFsmTaskEntry = _CucsEtherServerIntFIoFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1)
)
cucsEtherServerIntFIoFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherServerIntFIoFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskEntry.setStatus("current")
_CucsEtherServerIntFIoFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsEtherServerIntFIoFsmTaskInstanceId_Object = MibTableColumn
cucsEtherServerIntFIoFsmTaskInstanceId = _CucsEtherServerIntFIoFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1, 1),
    _CucsEtherServerIntFIoFsmTaskInstanceId_Type()
)
cucsEtherServerIntFIoFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskInstanceId.setStatus("current")
_CucsEtherServerIntFIoFsmTaskDn_Type = CucsManagedObjectDn
_CucsEtherServerIntFIoFsmTaskDn_Object = MibTableColumn
cucsEtherServerIntFIoFsmTaskDn = _CucsEtherServerIntFIoFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1, 2),
    _CucsEtherServerIntFIoFsmTaskDn_Type()
)
cucsEtherServerIntFIoFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskDn.setStatus("current")
_CucsEtherServerIntFIoFsmTaskRn_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmTaskRn_Object = MibTableColumn
cucsEtherServerIntFIoFsmTaskRn = _CucsEtherServerIntFIoFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1, 3),
    _CucsEtherServerIntFIoFsmTaskRn_Type()
)
cucsEtherServerIntFIoFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskRn.setStatus("current")
_CucsEtherServerIntFIoFsmTaskCompletion_Type = CucsFsmCompletion
_CucsEtherServerIntFIoFsmTaskCompletion_Object = MibTableColumn
cucsEtherServerIntFIoFsmTaskCompletion = _CucsEtherServerIntFIoFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1, 4),
    _CucsEtherServerIntFIoFsmTaskCompletion_Type()
)
cucsEtherServerIntFIoFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskCompletion.setStatus("current")
_CucsEtherServerIntFIoFsmTaskFlags_Type = CucsFsmFlags
_CucsEtherServerIntFIoFsmTaskFlags_Object = MibTableColumn
cucsEtherServerIntFIoFsmTaskFlags = _CucsEtherServerIntFIoFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1, 5),
    _CucsEtherServerIntFIoFsmTaskFlags_Type()
)
cucsEtherServerIntFIoFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskFlags.setStatus("current")
_CucsEtherServerIntFIoFsmTaskItem_Type = CucsEtherServerIntFIoFsmTaskItem
_CucsEtherServerIntFIoFsmTaskItem_Object = MibTableColumn
cucsEtherServerIntFIoFsmTaskItem = _CucsEtherServerIntFIoFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1, 6),
    _CucsEtherServerIntFIoFsmTaskItem_Type()
)
cucsEtherServerIntFIoFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskItem.setStatus("current")
_CucsEtherServerIntFIoFsmTaskSeqId_Type = Gauge32
_CucsEtherServerIntFIoFsmTaskSeqId_Object = MibTableColumn
cucsEtherServerIntFIoFsmTaskSeqId = _CucsEtherServerIntFIoFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 22, 1, 7),
    _CucsEtherServerIntFIoFsmTaskSeqId_Type()
)
cucsEtherServerIntFIoFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTaskSeqId.setStatus("current")
_CucsEtherFcoeInterfaceStatsTable_Object = MibTable
cucsEtherFcoeInterfaceStatsTable = _CucsEtherFcoeInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23)
)
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsTable.setStatus("current")
_CucsEtherFcoeInterfaceStatsEntry_Object = MibTableRow
cucsEtherFcoeInterfaceStatsEntry = _CucsEtherFcoeInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1)
)
cucsEtherFcoeInterfaceStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherFcoeInterfaceStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsEntry.setStatus("current")
_CucsEtherFcoeInterfaceStatsInstanceId_Type = CucsManagedObjectId
_CucsEtherFcoeInterfaceStatsInstanceId_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsInstanceId = _CucsEtherFcoeInterfaceStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 1),
    _CucsEtherFcoeInterfaceStatsInstanceId_Type()
)
cucsEtherFcoeInterfaceStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsInstanceId.setStatus("current")
_CucsEtherFcoeInterfaceStatsDn_Type = CucsManagedObjectDn
_CucsEtherFcoeInterfaceStatsDn_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDn = _CucsEtherFcoeInterfaceStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 2),
    _CucsEtherFcoeInterfaceStatsDn_Type()
)
cucsEtherFcoeInterfaceStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDn.setStatus("current")
_CucsEtherFcoeInterfaceStatsRn_Type = SnmpAdminString
_CucsEtherFcoeInterfaceStatsRn_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsRn = _CucsEtherFcoeInterfaceStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 3),
    _CucsEtherFcoeInterfaceStatsRn_Type()
)
cucsEtherFcoeInterfaceStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsRn.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRx = _CucsEtherFcoeInterfaceStatsBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 4),
    _CucsEtherFcoeInterfaceStatsBytesRx_Type()
)
cucsEtherFcoeInterfaceStatsBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesRxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsBytesRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDelta = _CucsEtherFcoeInterfaceStatsBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 5),
    _CucsEtherFcoeInterfaceStatsBytesRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg = _CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 6),
    _CucsEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDeltaMax = _CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 7),
    _CucsEtherFcoeInterfaceStatsBytesRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesRxDeltaMin = _CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 8),
    _CucsEtherFcoeInterfaceStatsBytesRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTx = _CucsEtherFcoeInterfaceStatsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 9),
    _CucsEtherFcoeInterfaceStatsBytesTx_Type()
)
cucsEtherFcoeInterfaceStatsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesTxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsBytesTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDelta = _CucsEtherFcoeInterfaceStatsBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 10),
    _CucsEtherFcoeInterfaceStatsBytesTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg = _CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 11),
    _CucsEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDeltaMax = _CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 12),
    _CucsEtherFcoeInterfaceStatsBytesTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsBytesTxDeltaMin = _CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 13),
    _CucsEtherFcoeInterfaceStatsBytesTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsBytesTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRx = _CucsEtherFcoeInterfaceStatsDroppedRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 14),
    _CucsEtherFcoeInterfaceStatsDroppedRx_Type()
)
cucsEtherFcoeInterfaceStatsDroppedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedRxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsDroppedRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDelta = _CucsEtherFcoeInterfaceStatsDroppedRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 15),
    _CucsEtherFcoeInterfaceStatsDroppedRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsDroppedRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg = _CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 16),
    _CucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax = _CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 17),
    _CucsEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin = _CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 18),
    _CucsEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTx = _CucsEtherFcoeInterfaceStatsDroppedTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 19),
    _CucsEtherFcoeInterfaceStatsDroppedTx_Type()
)
cucsEtherFcoeInterfaceStatsDroppedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedTxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsDroppedTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDelta = _CucsEtherFcoeInterfaceStatsDroppedTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 20),
    _CucsEtherFcoeInterfaceStatsDroppedTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsDroppedTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg = _CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 21),
    _CucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax = _CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 22),
    _CucsEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin = _CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 23),
    _CucsEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRx = _CucsEtherFcoeInterfaceStatsErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 24),
    _CucsEtherFcoeInterfaceStatsErrorsRx_Type()
)
cucsEtherFcoeInterfaceStatsErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsRxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsErrorsRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDelta = _CucsEtherFcoeInterfaceStatsErrorsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 25),
    _CucsEtherFcoeInterfaceStatsErrorsRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsErrorsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg = _CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 26),
    _CucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax = _CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 27),
    _CucsEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin = _CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 28),
    _CucsEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTx = _CucsEtherFcoeInterfaceStatsErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 29),
    _CucsEtherFcoeInterfaceStatsErrorsTx_Type()
)
cucsEtherFcoeInterfaceStatsErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsTxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsErrorsTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDelta = _CucsEtherFcoeInterfaceStatsErrorsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 30),
    _CucsEtherFcoeInterfaceStatsErrorsTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsErrorsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg = _CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 31),
    _CucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax = _CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 32),
    _CucsEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin = _CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 33),
    _CucsEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsIntervals_Type = Gauge32
_CucsEtherFcoeInterfaceStatsIntervals_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsIntervals = _CucsEtherFcoeInterfaceStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 34),
    _CucsEtherFcoeInterfaceStatsIntervals_Type()
)
cucsEtherFcoeInterfaceStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsIntervals.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRx = _CucsEtherFcoeInterfaceStatsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 35),
    _CucsEtherFcoeInterfaceStatsPacketsRx_Type()
)
cucsEtherFcoeInterfaceStatsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsRxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsPacketsRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDelta = _CucsEtherFcoeInterfaceStatsPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 36),
    _CucsEtherFcoeInterfaceStatsPacketsRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg = _CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 37),
    _CucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax = _CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 38),
    _CucsEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin = _CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 39),
    _CucsEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTx = _CucsEtherFcoeInterfaceStatsPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 40),
    _CucsEtherFcoeInterfaceStatsPacketsTx_Type()
)
cucsEtherFcoeInterfaceStatsPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsTxDelta_Type = Counter64
_CucsEtherFcoeInterfaceStatsPacketsTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDelta = _CucsEtherFcoeInterfaceStatsPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 41),
    _CucsEtherFcoeInterfaceStatsPacketsTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg = _CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 42),
    _CucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax = _CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 43),
    _CucsEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin = _CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 44),
    _CucsEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsSuspect_Type = TruthValue
_CucsEtherFcoeInterfaceStatsSuspect_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsSuspect = _CucsEtherFcoeInterfaceStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 45),
    _CucsEtherFcoeInterfaceStatsSuspect_Type()
)
cucsEtherFcoeInterfaceStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsSuspect.setStatus("current")
_CucsEtherFcoeInterfaceStatsThresholded_Type = CucsEtherFcoeInterfaceStatsThresholded
_CucsEtherFcoeInterfaceStatsThresholded_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsThresholded = _CucsEtherFcoeInterfaceStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 46),
    _CucsEtherFcoeInterfaceStatsThresholded_Type()
)
cucsEtherFcoeInterfaceStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsThresholded.setStatus("current")
_CucsEtherFcoeInterfaceStatsTimeCollected_Type = DateAndTime
_CucsEtherFcoeInterfaceStatsTimeCollected_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsTimeCollected = _CucsEtherFcoeInterfaceStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 47),
    _CucsEtherFcoeInterfaceStatsTimeCollected_Type()
)
cucsEtherFcoeInterfaceStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsTimeCollected.setStatus("current")
_CucsEtherFcoeInterfaceStatsUpdate_Type = Gauge32
_CucsEtherFcoeInterfaceStatsUpdate_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsUpdate = _CucsEtherFcoeInterfaceStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 23, 1, 48),
    _CucsEtherFcoeInterfaceStatsUpdate_Type()
)
cucsEtherFcoeInterfaceStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsUpdate.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistTable_Object = MibTable
cucsEtherFcoeInterfaceStatsHistTable = _CucsEtherFcoeInterfaceStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24)
)
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistTable.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistEntry_Object = MibTableRow
cucsEtherFcoeInterfaceStatsHistEntry = _CucsEtherFcoeInterfaceStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1)
)
cucsEtherFcoeInterfaceStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherFcoeInterfaceStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistEntry.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistInstanceId_Type = CucsManagedObjectId
_CucsEtherFcoeInterfaceStatsHistInstanceId_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistInstanceId = _CucsEtherFcoeInterfaceStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 1),
    _CucsEtherFcoeInterfaceStatsHistInstanceId_Type()
)
cucsEtherFcoeInterfaceStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistInstanceId.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDn_Type = CucsManagedObjectDn
_CucsEtherFcoeInterfaceStatsHistDn_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDn = _CucsEtherFcoeInterfaceStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 2),
    _CucsEtherFcoeInterfaceStatsHistDn_Type()
)
cucsEtherFcoeInterfaceStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDn.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistRn_Type = SnmpAdminString
_CucsEtherFcoeInterfaceStatsHistRn_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistRn = _CucsEtherFcoeInterfaceStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 3),
    _CucsEtherFcoeInterfaceStatsHistRn_Type()
)
cucsEtherFcoeInterfaceStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistRn.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRx = _CucsEtherFcoeInterfaceStatsHistBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 4),
    _CucsEtherFcoeInterfaceStatsHistBytesRx_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDelta = _CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 5),
    _CucsEtherFcoeInterfaceStatsHistBytesRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 6),
    _CucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax = _CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 7),
    _CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin = _CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 8),
    _CucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTx = _CucsEtherFcoeInterfaceStatsHistBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 9),
    _CucsEtherFcoeInterfaceStatsHistBytesTx_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDelta = _CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 10),
    _CucsEtherFcoeInterfaceStatsHistBytesTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 11),
    _CucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax = _CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 12),
    _CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin = _CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 13),
    _CucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRx = _CucsEtherFcoeInterfaceStatsHistDroppedRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 14),
    _CucsEtherFcoeInterfaceStatsHistDroppedRx_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDelta = _CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 15),
    _CucsEtherFcoeInterfaceStatsHistDroppedRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 16),
    _CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax = _CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 17),
    _CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin = _CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 18),
    _CucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTx = _CucsEtherFcoeInterfaceStatsHistDroppedTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 19),
    _CucsEtherFcoeInterfaceStatsHistDroppedTx_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDelta = _CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 20),
    _CucsEtherFcoeInterfaceStatsHistDroppedTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 21),
    _CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax = _CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 22),
    _CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin = _CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 23),
    _CucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRx = _CucsEtherFcoeInterfaceStatsHistErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 24),
    _CucsEtherFcoeInterfaceStatsHistErrorsRx_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDelta = _CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 25),
    _CucsEtherFcoeInterfaceStatsHistErrorsRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 26),
    _CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax = _CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 27),
    _CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin = _CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 28),
    _CucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTx = _CucsEtherFcoeInterfaceStatsHistErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 29),
    _CucsEtherFcoeInterfaceStatsHistErrorsTx_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDelta = _CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 30),
    _CucsEtherFcoeInterfaceStatsHistErrorsTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 31),
    _CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax = _CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 32),
    _CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin = _CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 33),
    _CucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistId_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistId_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistId = _CucsEtherFcoeInterfaceStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 34),
    _CucsEtherFcoeInterfaceStatsHistId_Type()
)
cucsEtherFcoeInterfaceStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistId.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistMostRecent_Type = TruthValue
_CucsEtherFcoeInterfaceStatsHistMostRecent_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistMostRecent = _CucsEtherFcoeInterfaceStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 35),
    _CucsEtherFcoeInterfaceStatsHistMostRecent_Type()
)
cucsEtherFcoeInterfaceStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistMostRecent.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsRx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRx = _CucsEtherFcoeInterfaceStatsHistPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 36),
    _CucsEtherFcoeInterfaceStatsHistPacketsRx_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsRx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDelta = _CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 37),
    _CucsEtherFcoeInterfaceStatsHistPacketsRxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsRxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 38),
    _CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax = _CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 39),
    _CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin = _CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 40),
    _CucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsTx_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTx_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTx = _CucsEtherFcoeInterfaceStatsHistPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 41),
    _CucsEtherFcoeInterfaceStatsHistPacketsTx_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsTx.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDelta = _CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 42),
    _CucsEtherFcoeInterfaceStatsHistPacketsTxDelta_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsTxDelta.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg = _CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 43),
    _CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax = _CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 44),
    _CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type = Unsigned64
_CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin = _CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 45),
    _CucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type()
)
cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistSuspect_Type = TruthValue
_CucsEtherFcoeInterfaceStatsHistSuspect_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistSuspect = _CucsEtherFcoeInterfaceStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 46),
    _CucsEtherFcoeInterfaceStatsHistSuspect_Type()
)
cucsEtherFcoeInterfaceStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistSuspect.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistThresholded_Type = CucsEtherFcoeInterfaceStatsHistThresholded
_CucsEtherFcoeInterfaceStatsHistThresholded_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistThresholded = _CucsEtherFcoeInterfaceStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 47),
    _CucsEtherFcoeInterfaceStatsHistThresholded_Type()
)
cucsEtherFcoeInterfaceStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistThresholded.setStatus("current")
_CucsEtherFcoeInterfaceStatsHistTimeCollected_Type = DateAndTime
_CucsEtherFcoeInterfaceStatsHistTimeCollected_Object = MibTableColumn
cucsEtherFcoeInterfaceStatsHistTimeCollected = _CucsEtherFcoeInterfaceStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 24, 1, 48),
    _CucsEtherFcoeInterfaceStatsHistTimeCollected_Type()
)
cucsEtherFcoeInterfaceStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherFcoeInterfaceStatsHistTimeCollected.setStatus("current")
_CucsEtherPIoEndPointTable_Object = MibTable
cucsEtherPIoEndPointTable = _CucsEtherPIoEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25)
)
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointTable.setStatus("current")
_CucsEtherPIoEndPointEntry_Object = MibTableRow
cucsEtherPIoEndPointEntry = _CucsEtherPIoEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25, 1)
)
cucsEtherPIoEndPointEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPIoEndPointInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointEntry.setStatus("current")
_CucsEtherPIoEndPointInstanceId_Type = CucsManagedObjectId
_CucsEtherPIoEndPointInstanceId_Object = MibTableColumn
cucsEtherPIoEndPointInstanceId = _CucsEtherPIoEndPointInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25, 1, 1),
    _CucsEtherPIoEndPointInstanceId_Type()
)
cucsEtherPIoEndPointInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointInstanceId.setStatus("current")
_CucsEtherPIoEndPointDn_Type = CucsManagedObjectDn
_CucsEtherPIoEndPointDn_Object = MibTableColumn
cucsEtherPIoEndPointDn = _CucsEtherPIoEndPointDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25, 1, 2),
    _CucsEtherPIoEndPointDn_Type()
)
cucsEtherPIoEndPointDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointDn.setStatus("current")
_CucsEtherPIoEndPointRn_Type = SnmpAdminString
_CucsEtherPIoEndPointRn_Object = MibTableColumn
cucsEtherPIoEndPointRn = _CucsEtherPIoEndPointRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25, 1, 3),
    _CucsEtherPIoEndPointRn_Type()
)
cucsEtherPIoEndPointRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointRn.setStatus("current")
_CucsEtherPIoEndPointEndPointDn_Type = SnmpAdminString
_CucsEtherPIoEndPointEndPointDn_Object = MibTableColumn
cucsEtherPIoEndPointEndPointDn = _CucsEtherPIoEndPointEndPointDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25, 1, 4),
    _CucsEtherPIoEndPointEndPointDn_Type()
)
cucsEtherPIoEndPointEndPointDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointEndPointDn.setStatus("current")
_CucsEtherPIoEndPointEpCloudType_Type = CucsEtherCloudType
_CucsEtherPIoEndPointEpCloudType_Object = MibTableColumn
cucsEtherPIoEndPointEpCloudType = _CucsEtherPIoEndPointEpCloudType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25, 1, 5),
    _CucsEtherPIoEndPointEpCloudType_Type()
)
cucsEtherPIoEndPointEpCloudType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointEpCloudType.setStatus("current")
_CucsEtherPIoEndPointUsrLbl_Type = SnmpAdminString
_CucsEtherPIoEndPointUsrLbl_Object = MibTableColumn
cucsEtherPIoEndPointUsrLbl = _CucsEtherPIoEndPointUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 25, 1, 6),
    _CucsEtherPIoEndPointUsrLbl_Type()
)
cucsEtherPIoEndPointUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoEndPointUsrLbl.setStatus("current")
_CucsEtherPIoFsmTable_Object = MibTable
cucsEtherPIoFsmTable = _CucsEtherPIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26)
)
if mibBuilder.loadTexts:
    cucsEtherPIoFsmTable.setStatus("current")
_CucsEtherPIoFsmEntry_Object = MibTableRow
cucsEtherPIoFsmEntry = _CucsEtherPIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1)
)
cucsEtherPIoFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPIoFsmEntry.setStatus("current")
_CucsEtherPIoFsmInstanceId_Type = CucsManagedObjectId
_CucsEtherPIoFsmInstanceId_Object = MibTableColumn
cucsEtherPIoFsmInstanceId = _CucsEtherPIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 1),
    _CucsEtherPIoFsmInstanceId_Type()
)
cucsEtherPIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmInstanceId.setStatus("current")
_CucsEtherPIoFsmDn_Type = CucsManagedObjectDn
_CucsEtherPIoFsmDn_Object = MibTableColumn
cucsEtherPIoFsmDn = _CucsEtherPIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 2),
    _CucsEtherPIoFsmDn_Type()
)
cucsEtherPIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmDn.setStatus("current")
_CucsEtherPIoFsmRn_Type = SnmpAdminString
_CucsEtherPIoFsmRn_Object = MibTableColumn
cucsEtherPIoFsmRn = _CucsEtherPIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 3),
    _CucsEtherPIoFsmRn_Type()
)
cucsEtherPIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmRn.setStatus("current")
_CucsEtherPIoFsmCompletionTime_Type = DateAndTime
_CucsEtherPIoFsmCompletionTime_Object = MibTableColumn
cucsEtherPIoFsmCompletionTime = _CucsEtherPIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 4),
    _CucsEtherPIoFsmCompletionTime_Type()
)
cucsEtherPIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmCompletionTime.setStatus("current")
_CucsEtherPIoFsmCurrentFsm_Type = CucsEtherPIoFsmCurrentFsm
_CucsEtherPIoFsmCurrentFsm_Object = MibTableColumn
cucsEtherPIoFsmCurrentFsm = _CucsEtherPIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 5),
    _CucsEtherPIoFsmCurrentFsm_Type()
)
cucsEtherPIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmCurrentFsm.setStatus("current")
_CucsEtherPIoFsmDescrData_Type = SnmpAdminString
_CucsEtherPIoFsmDescrData_Object = MibTableColumn
cucsEtherPIoFsmDescrData = _CucsEtherPIoFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 6),
    _CucsEtherPIoFsmDescrData_Type()
)
cucsEtherPIoFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmDescrData.setStatus("current")
_CucsEtherPIoFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsEtherPIoFsmFsmStatus_Object = MibTableColumn
cucsEtherPIoFsmFsmStatus = _CucsEtherPIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 7),
    _CucsEtherPIoFsmFsmStatus_Type()
)
cucsEtherPIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmFsmStatus.setStatus("current")
_CucsEtherPIoFsmProgress_Type = Gauge32
_CucsEtherPIoFsmProgress_Object = MibTableColumn
cucsEtherPIoFsmProgress = _CucsEtherPIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 8),
    _CucsEtherPIoFsmProgress_Type()
)
cucsEtherPIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmProgress.setStatus("current")
_CucsEtherPIoFsmRmtErrCode_Type = Gauge32
_CucsEtherPIoFsmRmtErrCode_Object = MibTableColumn
cucsEtherPIoFsmRmtErrCode = _CucsEtherPIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 9),
    _CucsEtherPIoFsmRmtErrCode_Type()
)
cucsEtherPIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmRmtErrCode.setStatus("current")
_CucsEtherPIoFsmRmtErrDescr_Type = SnmpAdminString
_CucsEtherPIoFsmRmtErrDescr_Object = MibTableColumn
cucsEtherPIoFsmRmtErrDescr = _CucsEtherPIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 10),
    _CucsEtherPIoFsmRmtErrDescr_Type()
)
cucsEtherPIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmRmtErrDescr.setStatus("current")
_CucsEtherPIoFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsEtherPIoFsmRmtRslt_Object = MibTableColumn
cucsEtherPIoFsmRmtRslt = _CucsEtherPIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 26, 1, 11),
    _CucsEtherPIoFsmRmtRslt_Type()
)
cucsEtherPIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmRmtRslt.setStatus("current")
_CucsEtherPIoFsmStageTable_Object = MibTable
cucsEtherPIoFsmStageTable = _CucsEtherPIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27)
)
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageTable.setStatus("current")
_CucsEtherPIoFsmStageEntry_Object = MibTableRow
cucsEtherPIoFsmStageEntry = _CucsEtherPIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1)
)
cucsEtherPIoFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherPIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageEntry.setStatus("current")
_CucsEtherPIoFsmStageInstanceId_Type = CucsManagedObjectId
_CucsEtherPIoFsmStageInstanceId_Object = MibTableColumn
cucsEtherPIoFsmStageInstanceId = _CucsEtherPIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 1),
    _CucsEtherPIoFsmStageInstanceId_Type()
)
cucsEtherPIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageInstanceId.setStatus("current")
_CucsEtherPIoFsmStageDn_Type = CucsManagedObjectDn
_CucsEtherPIoFsmStageDn_Object = MibTableColumn
cucsEtherPIoFsmStageDn = _CucsEtherPIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 2),
    _CucsEtherPIoFsmStageDn_Type()
)
cucsEtherPIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageDn.setStatus("current")
_CucsEtherPIoFsmStageRn_Type = SnmpAdminString
_CucsEtherPIoFsmStageRn_Object = MibTableColumn
cucsEtherPIoFsmStageRn = _CucsEtherPIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 3),
    _CucsEtherPIoFsmStageRn_Type()
)
cucsEtherPIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageRn.setStatus("current")
_CucsEtherPIoFsmStageDescrData_Type = SnmpAdminString
_CucsEtherPIoFsmStageDescrData_Object = MibTableColumn
cucsEtherPIoFsmStageDescrData = _CucsEtherPIoFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 4),
    _CucsEtherPIoFsmStageDescrData_Type()
)
cucsEtherPIoFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageDescrData.setStatus("current")
_CucsEtherPIoFsmStageLastUpdateTime_Type = DateAndTime
_CucsEtherPIoFsmStageLastUpdateTime_Object = MibTableColumn
cucsEtherPIoFsmStageLastUpdateTime = _CucsEtherPIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 5),
    _CucsEtherPIoFsmStageLastUpdateTime_Type()
)
cucsEtherPIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageLastUpdateTime.setStatus("current")
_CucsEtherPIoFsmStageName_Type = CucsEtherPIoFsmStageName
_CucsEtherPIoFsmStageName_Object = MibTableColumn
cucsEtherPIoFsmStageName = _CucsEtherPIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 6),
    _CucsEtherPIoFsmStageName_Type()
)
cucsEtherPIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageName.setStatus("current")
_CucsEtherPIoFsmStageOrder_Type = Gauge32
_CucsEtherPIoFsmStageOrder_Object = MibTableColumn
cucsEtherPIoFsmStageOrder = _CucsEtherPIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 7),
    _CucsEtherPIoFsmStageOrder_Type()
)
cucsEtherPIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageOrder.setStatus("current")
_CucsEtherPIoFsmStageRetry_Type = Gauge32
_CucsEtherPIoFsmStageRetry_Object = MibTableColumn
cucsEtherPIoFsmStageRetry = _CucsEtherPIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 8),
    _CucsEtherPIoFsmStageRetry_Type()
)
cucsEtherPIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageRetry.setStatus("current")
_CucsEtherPIoFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsEtherPIoFsmStageStageStatus_Object = MibTableColumn
cucsEtherPIoFsmStageStageStatus = _CucsEtherPIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 27, 1, 9),
    _CucsEtherPIoFsmStageStageStatus_Type()
)
cucsEtherPIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherPIoFsmStageStageStatus.setStatus("current")
_CucsEtherServerIntFIoFsmTable_Object = MibTable
cucsEtherServerIntFIoFsmTable = _CucsEtherServerIntFIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28)
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmTable.setStatus("current")
_CucsEtherServerIntFIoFsmEntry_Object = MibTableRow
cucsEtherServerIntFIoFsmEntry = _CucsEtherServerIntFIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1)
)
cucsEtherServerIntFIoFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherServerIntFIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmEntry.setStatus("current")
_CucsEtherServerIntFIoFsmInstanceId_Type = CucsManagedObjectId
_CucsEtherServerIntFIoFsmInstanceId_Object = MibTableColumn
cucsEtherServerIntFIoFsmInstanceId = _CucsEtherServerIntFIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 1),
    _CucsEtherServerIntFIoFsmInstanceId_Type()
)
cucsEtherServerIntFIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmInstanceId.setStatus("current")
_CucsEtherServerIntFIoFsmDn_Type = CucsManagedObjectDn
_CucsEtherServerIntFIoFsmDn_Object = MibTableColumn
cucsEtherServerIntFIoFsmDn = _CucsEtherServerIntFIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 2),
    _CucsEtherServerIntFIoFsmDn_Type()
)
cucsEtherServerIntFIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmDn.setStatus("current")
_CucsEtherServerIntFIoFsmRn_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmRn_Object = MibTableColumn
cucsEtherServerIntFIoFsmRn = _CucsEtherServerIntFIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 3),
    _CucsEtherServerIntFIoFsmRn_Type()
)
cucsEtherServerIntFIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmRn.setStatus("current")
_CucsEtherServerIntFIoFsmCompletionTime_Type = DateAndTime
_CucsEtherServerIntFIoFsmCompletionTime_Object = MibTableColumn
cucsEtherServerIntFIoFsmCompletionTime = _CucsEtherServerIntFIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 4),
    _CucsEtherServerIntFIoFsmCompletionTime_Type()
)
cucsEtherServerIntFIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmCompletionTime.setStatus("current")
_CucsEtherServerIntFIoFsmCurrentFsm_Type = CucsEtherServerIntFIoFsmCurrentFsm
_CucsEtherServerIntFIoFsmCurrentFsm_Object = MibTableColumn
cucsEtherServerIntFIoFsmCurrentFsm = _CucsEtherServerIntFIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 5),
    _CucsEtherServerIntFIoFsmCurrentFsm_Type()
)
cucsEtherServerIntFIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmCurrentFsm.setStatus("current")
_CucsEtherServerIntFIoFsmDescrData_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmDescrData_Object = MibTableColumn
cucsEtherServerIntFIoFsmDescrData = _CucsEtherServerIntFIoFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 6),
    _CucsEtherServerIntFIoFsmDescrData_Type()
)
cucsEtherServerIntFIoFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmDescrData.setStatus("current")
_CucsEtherServerIntFIoFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsEtherServerIntFIoFsmFsmStatus_Object = MibTableColumn
cucsEtherServerIntFIoFsmFsmStatus = _CucsEtherServerIntFIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 7),
    _CucsEtherServerIntFIoFsmFsmStatus_Type()
)
cucsEtherServerIntFIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmFsmStatus.setStatus("current")
_CucsEtherServerIntFIoFsmProgress_Type = Gauge32
_CucsEtherServerIntFIoFsmProgress_Object = MibTableColumn
cucsEtherServerIntFIoFsmProgress = _CucsEtherServerIntFIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 8),
    _CucsEtherServerIntFIoFsmProgress_Type()
)
cucsEtherServerIntFIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmProgress.setStatus("current")
_CucsEtherServerIntFIoFsmRmtErrCode_Type = Gauge32
_CucsEtherServerIntFIoFsmRmtErrCode_Object = MibTableColumn
cucsEtherServerIntFIoFsmRmtErrCode = _CucsEtherServerIntFIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 9),
    _CucsEtherServerIntFIoFsmRmtErrCode_Type()
)
cucsEtherServerIntFIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmRmtErrCode.setStatus("current")
_CucsEtherServerIntFIoFsmRmtErrDescr_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmRmtErrDescr_Object = MibTableColumn
cucsEtherServerIntFIoFsmRmtErrDescr = _CucsEtherServerIntFIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 10),
    _CucsEtherServerIntFIoFsmRmtErrDescr_Type()
)
cucsEtherServerIntFIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmRmtErrDescr.setStatus("current")
_CucsEtherServerIntFIoFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsEtherServerIntFIoFsmRmtRslt_Object = MibTableColumn
cucsEtherServerIntFIoFsmRmtRslt = _CucsEtherServerIntFIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 28, 1, 11),
    _CucsEtherServerIntFIoFsmRmtRslt_Type()
)
cucsEtherServerIntFIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmRmtRslt.setStatus("current")
_CucsEtherServerIntFIoFsmStageTable_Object = MibTable
cucsEtherServerIntFIoFsmStageTable = _CucsEtherServerIntFIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29)
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageTable.setStatus("current")
_CucsEtherServerIntFIoFsmStageEntry_Object = MibTableRow
cucsEtherServerIntFIoFsmStageEntry = _CucsEtherServerIntFIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1)
)
cucsEtherServerIntFIoFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherServerIntFIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageEntry.setStatus("current")
_CucsEtherServerIntFIoFsmStageInstanceId_Type = CucsManagedObjectId
_CucsEtherServerIntFIoFsmStageInstanceId_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageInstanceId = _CucsEtherServerIntFIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 1),
    _CucsEtherServerIntFIoFsmStageInstanceId_Type()
)
cucsEtherServerIntFIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageInstanceId.setStatus("current")
_CucsEtherServerIntFIoFsmStageDn_Type = CucsManagedObjectDn
_CucsEtherServerIntFIoFsmStageDn_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageDn = _CucsEtherServerIntFIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 2),
    _CucsEtherServerIntFIoFsmStageDn_Type()
)
cucsEtherServerIntFIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageDn.setStatus("current")
_CucsEtherServerIntFIoFsmStageRn_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmStageRn_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageRn = _CucsEtherServerIntFIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 3),
    _CucsEtherServerIntFIoFsmStageRn_Type()
)
cucsEtherServerIntFIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageRn.setStatus("current")
_CucsEtherServerIntFIoFsmStageDescrData_Type = SnmpAdminString
_CucsEtherServerIntFIoFsmStageDescrData_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageDescrData = _CucsEtherServerIntFIoFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 4),
    _CucsEtherServerIntFIoFsmStageDescrData_Type()
)
cucsEtherServerIntFIoFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageDescrData.setStatus("current")
_CucsEtherServerIntFIoFsmStageLastUpdateTime_Type = DateAndTime
_CucsEtherServerIntFIoFsmStageLastUpdateTime_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageLastUpdateTime = _CucsEtherServerIntFIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 5),
    _CucsEtherServerIntFIoFsmStageLastUpdateTime_Type()
)
cucsEtherServerIntFIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageLastUpdateTime.setStatus("current")
_CucsEtherServerIntFIoFsmStageName_Type = CucsEtherServerIntFIoFsmStageName
_CucsEtherServerIntFIoFsmStageName_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageName = _CucsEtherServerIntFIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 6),
    _CucsEtherServerIntFIoFsmStageName_Type()
)
cucsEtherServerIntFIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageName.setStatus("current")
_CucsEtherServerIntFIoFsmStageOrder_Type = Gauge32
_CucsEtherServerIntFIoFsmStageOrder_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageOrder = _CucsEtherServerIntFIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 7),
    _CucsEtherServerIntFIoFsmStageOrder_Type()
)
cucsEtherServerIntFIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageOrder.setStatus("current")
_CucsEtherServerIntFIoFsmStageRetry_Type = Gauge32
_CucsEtherServerIntFIoFsmStageRetry_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageRetry = _CucsEtherServerIntFIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 8),
    _CucsEtherServerIntFIoFsmStageRetry_Type()
)
cucsEtherServerIntFIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageRetry.setStatus("current")
_CucsEtherServerIntFIoFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsEtherServerIntFIoFsmStageStageStatus_Object = MibTableColumn
cucsEtherServerIntFIoFsmStageStageStatus = _CucsEtherServerIntFIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 29, 1, 9),
    _CucsEtherServerIntFIoFsmStageStageStatus_Type()
)
cucsEtherServerIntFIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherServerIntFIoFsmStageStageStatus.setStatus("current")
_CucsEtherNiErrStatsTable_Object = MibTable
cucsEtherNiErrStatsTable = _CucsEtherNiErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30)
)
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTable.setStatus("current")
_CucsEtherNiErrStatsEntry_Object = MibTableRow
cucsEtherNiErrStatsEntry = _CucsEtherNiErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1)
)
cucsEtherNiErrStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherNiErrStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsEntry.setStatus("current")
_CucsEtherNiErrStatsInstanceId_Type = CucsManagedObjectId
_CucsEtherNiErrStatsInstanceId_Object = MibTableColumn
cucsEtherNiErrStatsInstanceId = _CucsEtherNiErrStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 1),
    _CucsEtherNiErrStatsInstanceId_Type()
)
cucsEtherNiErrStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsInstanceId.setStatus("current")
_CucsEtherNiErrStatsDn_Type = CucsManagedObjectDn
_CucsEtherNiErrStatsDn_Object = MibTableColumn
cucsEtherNiErrStatsDn = _CucsEtherNiErrStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 2),
    _CucsEtherNiErrStatsDn_Type()
)
cucsEtherNiErrStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsDn.setStatus("current")
_CucsEtherNiErrStatsRn_Type = SnmpAdminString
_CucsEtherNiErrStatsRn_Object = MibTableColumn
cucsEtherNiErrStatsRn = _CucsEtherNiErrStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 3),
    _CucsEtherNiErrStatsRn_Type()
)
cucsEtherNiErrStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsRn.setStatus("current")
_CucsEtherNiErrStatsCrc_Type = Unsigned64
_CucsEtherNiErrStatsCrc_Object = MibTableColumn
cucsEtherNiErrStatsCrc = _CucsEtherNiErrStatsCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 4),
    _CucsEtherNiErrStatsCrc_Type()
)
cucsEtherNiErrStatsCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsCrc.setStatus("current")
_CucsEtherNiErrStatsCrcDelta_Type = Counter64
_CucsEtherNiErrStatsCrcDelta_Object = MibTableColumn
cucsEtherNiErrStatsCrcDelta = _CucsEtherNiErrStatsCrcDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 5),
    _CucsEtherNiErrStatsCrcDelta_Type()
)
cucsEtherNiErrStatsCrcDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsCrcDelta.setStatus("current")
_CucsEtherNiErrStatsCrcDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsCrcDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsCrcDeltaAvg = _CucsEtherNiErrStatsCrcDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 6),
    _CucsEtherNiErrStatsCrcDeltaAvg_Type()
)
cucsEtherNiErrStatsCrcDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsCrcDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsCrcDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsCrcDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsCrcDeltaMax = _CucsEtherNiErrStatsCrcDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 7),
    _CucsEtherNiErrStatsCrcDeltaMax_Type()
)
cucsEtherNiErrStatsCrcDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsCrcDeltaMax.setStatus("current")
_CucsEtherNiErrStatsCrcDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsCrcDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsCrcDeltaMin = _CucsEtherNiErrStatsCrcDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 8),
    _CucsEtherNiErrStatsCrcDeltaMin_Type()
)
cucsEtherNiErrStatsCrcDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsCrcDeltaMin.setStatus("current")
_CucsEtherNiErrStatsFrameTx_Type = Unsigned64
_CucsEtherNiErrStatsFrameTx_Object = MibTableColumn
cucsEtherNiErrStatsFrameTx = _CucsEtherNiErrStatsFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 9),
    _CucsEtherNiErrStatsFrameTx_Type()
)
cucsEtherNiErrStatsFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsFrameTx.setStatus("current")
_CucsEtherNiErrStatsFrameTxDelta_Type = Counter64
_CucsEtherNiErrStatsFrameTxDelta_Object = MibTableColumn
cucsEtherNiErrStatsFrameTxDelta = _CucsEtherNiErrStatsFrameTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 10),
    _CucsEtherNiErrStatsFrameTxDelta_Type()
)
cucsEtherNiErrStatsFrameTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsFrameTxDelta.setStatus("current")
_CucsEtherNiErrStatsFrameTxDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsFrameTxDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsFrameTxDeltaAvg = _CucsEtherNiErrStatsFrameTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 11),
    _CucsEtherNiErrStatsFrameTxDeltaAvg_Type()
)
cucsEtherNiErrStatsFrameTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsFrameTxDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsFrameTxDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsFrameTxDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsFrameTxDeltaMax = _CucsEtherNiErrStatsFrameTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 12),
    _CucsEtherNiErrStatsFrameTxDeltaMax_Type()
)
cucsEtherNiErrStatsFrameTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsFrameTxDeltaMax.setStatus("current")
_CucsEtherNiErrStatsFrameTxDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsFrameTxDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsFrameTxDeltaMin = _CucsEtherNiErrStatsFrameTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 13),
    _CucsEtherNiErrStatsFrameTxDeltaMin_Type()
)
cucsEtherNiErrStatsFrameTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsFrameTxDeltaMin.setStatus("current")
_CucsEtherNiErrStatsInRange_Type = Unsigned64
_CucsEtherNiErrStatsInRange_Object = MibTableColumn
cucsEtherNiErrStatsInRange = _CucsEtherNiErrStatsInRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 14),
    _CucsEtherNiErrStatsInRange_Type()
)
cucsEtherNiErrStatsInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsInRange.setStatus("current")
_CucsEtherNiErrStatsInRangeDelta_Type = Counter64
_CucsEtherNiErrStatsInRangeDelta_Object = MibTableColumn
cucsEtherNiErrStatsInRangeDelta = _CucsEtherNiErrStatsInRangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 15),
    _CucsEtherNiErrStatsInRangeDelta_Type()
)
cucsEtherNiErrStatsInRangeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsInRangeDelta.setStatus("current")
_CucsEtherNiErrStatsInRangeDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsInRangeDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsInRangeDeltaAvg = _CucsEtherNiErrStatsInRangeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 16),
    _CucsEtherNiErrStatsInRangeDeltaAvg_Type()
)
cucsEtherNiErrStatsInRangeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsInRangeDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsInRangeDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsInRangeDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsInRangeDeltaMax = _CucsEtherNiErrStatsInRangeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 17),
    _CucsEtherNiErrStatsInRangeDeltaMax_Type()
)
cucsEtherNiErrStatsInRangeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsInRangeDeltaMax.setStatus("current")
_CucsEtherNiErrStatsInRangeDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsInRangeDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsInRangeDeltaMin = _CucsEtherNiErrStatsInRangeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 18),
    _CucsEtherNiErrStatsInRangeDeltaMin_Type()
)
cucsEtherNiErrStatsInRangeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsInRangeDeltaMin.setStatus("current")
_CucsEtherNiErrStatsIntervals_Type = Gauge32
_CucsEtherNiErrStatsIntervals_Object = MibTableColumn
cucsEtherNiErrStatsIntervals = _CucsEtherNiErrStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 19),
    _CucsEtherNiErrStatsIntervals_Type()
)
cucsEtherNiErrStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsIntervals.setStatus("current")
_CucsEtherNiErrStatsSuspect_Type = TruthValue
_CucsEtherNiErrStatsSuspect_Object = MibTableColumn
cucsEtherNiErrStatsSuspect = _CucsEtherNiErrStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 20),
    _CucsEtherNiErrStatsSuspect_Type()
)
cucsEtherNiErrStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsSuspect.setStatus("current")
_CucsEtherNiErrStatsThresholded_Type = CucsEtherNiErrStatsThresholded
_CucsEtherNiErrStatsThresholded_Object = MibTableColumn
cucsEtherNiErrStatsThresholded = _CucsEtherNiErrStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 21),
    _CucsEtherNiErrStatsThresholded_Type()
)
cucsEtherNiErrStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsThresholded.setStatus("current")
_CucsEtherNiErrStatsTimeCollected_Type = DateAndTime
_CucsEtherNiErrStatsTimeCollected_Object = MibTableColumn
cucsEtherNiErrStatsTimeCollected = _CucsEtherNiErrStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 22),
    _CucsEtherNiErrStatsTimeCollected_Type()
)
cucsEtherNiErrStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTimeCollected.setStatus("current")
_CucsEtherNiErrStatsTooLong_Type = Unsigned64
_CucsEtherNiErrStatsTooLong_Object = MibTableColumn
cucsEtherNiErrStatsTooLong = _CucsEtherNiErrStatsTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 23),
    _CucsEtherNiErrStatsTooLong_Type()
)
cucsEtherNiErrStatsTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooLong.setStatus("current")
_CucsEtherNiErrStatsTooLongDelta_Type = Counter64
_CucsEtherNiErrStatsTooLongDelta_Object = MibTableColumn
cucsEtherNiErrStatsTooLongDelta = _CucsEtherNiErrStatsTooLongDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 24),
    _CucsEtherNiErrStatsTooLongDelta_Type()
)
cucsEtherNiErrStatsTooLongDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooLongDelta.setStatus("current")
_CucsEtherNiErrStatsTooLongDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsTooLongDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsTooLongDeltaAvg = _CucsEtherNiErrStatsTooLongDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 25),
    _CucsEtherNiErrStatsTooLongDeltaAvg_Type()
)
cucsEtherNiErrStatsTooLongDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooLongDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsTooLongDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsTooLongDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsTooLongDeltaMax = _CucsEtherNiErrStatsTooLongDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 26),
    _CucsEtherNiErrStatsTooLongDeltaMax_Type()
)
cucsEtherNiErrStatsTooLongDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooLongDeltaMax.setStatus("current")
_CucsEtherNiErrStatsTooLongDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsTooLongDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsTooLongDeltaMin = _CucsEtherNiErrStatsTooLongDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 27),
    _CucsEtherNiErrStatsTooLongDeltaMin_Type()
)
cucsEtherNiErrStatsTooLongDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooLongDeltaMin.setStatus("current")
_CucsEtherNiErrStatsTooShort_Type = Unsigned64
_CucsEtherNiErrStatsTooShort_Object = MibTableColumn
cucsEtherNiErrStatsTooShort = _CucsEtherNiErrStatsTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 28),
    _CucsEtherNiErrStatsTooShort_Type()
)
cucsEtherNiErrStatsTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooShort.setStatus("current")
_CucsEtherNiErrStatsTooShortDelta_Type = Counter64
_CucsEtherNiErrStatsTooShortDelta_Object = MibTableColumn
cucsEtherNiErrStatsTooShortDelta = _CucsEtherNiErrStatsTooShortDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 29),
    _CucsEtherNiErrStatsTooShortDelta_Type()
)
cucsEtherNiErrStatsTooShortDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooShortDelta.setStatus("current")
_CucsEtherNiErrStatsTooShortDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsTooShortDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsTooShortDeltaAvg = _CucsEtherNiErrStatsTooShortDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 30),
    _CucsEtherNiErrStatsTooShortDeltaAvg_Type()
)
cucsEtherNiErrStatsTooShortDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooShortDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsTooShortDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsTooShortDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsTooShortDeltaMax = _CucsEtherNiErrStatsTooShortDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 31),
    _CucsEtherNiErrStatsTooShortDeltaMax_Type()
)
cucsEtherNiErrStatsTooShortDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooShortDeltaMax.setStatus("current")
_CucsEtherNiErrStatsTooShortDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsTooShortDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsTooShortDeltaMin = _CucsEtherNiErrStatsTooShortDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 32),
    _CucsEtherNiErrStatsTooShortDeltaMin_Type()
)
cucsEtherNiErrStatsTooShortDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsTooShortDeltaMin.setStatus("current")
_CucsEtherNiErrStatsUpdate_Type = Gauge32
_CucsEtherNiErrStatsUpdate_Object = MibTableColumn
cucsEtherNiErrStatsUpdate = _CucsEtherNiErrStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 30, 1, 33),
    _CucsEtherNiErrStatsUpdate_Type()
)
cucsEtherNiErrStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsUpdate.setStatus("current")
_CucsEtherNiErrStatsHistTable_Object = MibTable
cucsEtherNiErrStatsHistTable = _CucsEtherNiErrStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31)
)
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTable.setStatus("current")
_CucsEtherNiErrStatsHistEntry_Object = MibTableRow
cucsEtherNiErrStatsHistEntry = _CucsEtherNiErrStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1)
)
cucsEtherNiErrStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ETHER-MIB", "cucsEtherNiErrStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistEntry.setStatus("current")
_CucsEtherNiErrStatsHistInstanceId_Type = CucsManagedObjectId
_CucsEtherNiErrStatsHistInstanceId_Object = MibTableColumn
cucsEtherNiErrStatsHistInstanceId = _CucsEtherNiErrStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 1),
    _CucsEtherNiErrStatsHistInstanceId_Type()
)
cucsEtherNiErrStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistInstanceId.setStatus("current")
_CucsEtherNiErrStatsHistDn_Type = CucsManagedObjectDn
_CucsEtherNiErrStatsHistDn_Object = MibTableColumn
cucsEtherNiErrStatsHistDn = _CucsEtherNiErrStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 2),
    _CucsEtherNiErrStatsHistDn_Type()
)
cucsEtherNiErrStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistDn.setStatus("current")
_CucsEtherNiErrStatsHistRn_Type = SnmpAdminString
_CucsEtherNiErrStatsHistRn_Object = MibTableColumn
cucsEtherNiErrStatsHistRn = _CucsEtherNiErrStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 3),
    _CucsEtherNiErrStatsHistRn_Type()
)
cucsEtherNiErrStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistRn.setStatus("current")
_CucsEtherNiErrStatsHistCrc_Type = Unsigned64
_CucsEtherNiErrStatsHistCrc_Object = MibTableColumn
cucsEtherNiErrStatsHistCrc = _CucsEtherNiErrStatsHistCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 4),
    _CucsEtherNiErrStatsHistCrc_Type()
)
cucsEtherNiErrStatsHistCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistCrc.setStatus("current")
_CucsEtherNiErrStatsHistCrcDelta_Type = Unsigned64
_CucsEtherNiErrStatsHistCrcDelta_Object = MibTableColumn
cucsEtherNiErrStatsHistCrcDelta = _CucsEtherNiErrStatsHistCrcDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 5),
    _CucsEtherNiErrStatsHistCrcDelta_Type()
)
cucsEtherNiErrStatsHistCrcDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistCrcDelta.setStatus("current")
_CucsEtherNiErrStatsHistCrcDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsHistCrcDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsHistCrcDeltaAvg = _CucsEtherNiErrStatsHistCrcDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 6),
    _CucsEtherNiErrStatsHistCrcDeltaAvg_Type()
)
cucsEtherNiErrStatsHistCrcDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistCrcDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsHistCrcDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsHistCrcDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsHistCrcDeltaMax = _CucsEtherNiErrStatsHistCrcDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 7),
    _CucsEtherNiErrStatsHistCrcDeltaMax_Type()
)
cucsEtherNiErrStatsHistCrcDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistCrcDeltaMax.setStatus("current")
_CucsEtherNiErrStatsHistCrcDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsHistCrcDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsHistCrcDeltaMin = _CucsEtherNiErrStatsHistCrcDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 8),
    _CucsEtherNiErrStatsHistCrcDeltaMin_Type()
)
cucsEtherNiErrStatsHistCrcDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistCrcDeltaMin.setStatus("current")
_CucsEtherNiErrStatsHistFrameTx_Type = Unsigned64
_CucsEtherNiErrStatsHistFrameTx_Object = MibTableColumn
cucsEtherNiErrStatsHistFrameTx = _CucsEtherNiErrStatsHistFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 9),
    _CucsEtherNiErrStatsHistFrameTx_Type()
)
cucsEtherNiErrStatsHistFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistFrameTx.setStatus("current")
_CucsEtherNiErrStatsHistFrameTxDelta_Type = Unsigned64
_CucsEtherNiErrStatsHistFrameTxDelta_Object = MibTableColumn
cucsEtherNiErrStatsHistFrameTxDelta = _CucsEtherNiErrStatsHistFrameTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 10),
    _CucsEtherNiErrStatsHistFrameTxDelta_Type()
)
cucsEtherNiErrStatsHistFrameTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistFrameTxDelta.setStatus("current")
_CucsEtherNiErrStatsHistFrameTxDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsHistFrameTxDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsHistFrameTxDeltaAvg = _CucsEtherNiErrStatsHistFrameTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 11),
    _CucsEtherNiErrStatsHistFrameTxDeltaAvg_Type()
)
cucsEtherNiErrStatsHistFrameTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistFrameTxDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsHistFrameTxDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsHistFrameTxDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsHistFrameTxDeltaMax = _CucsEtherNiErrStatsHistFrameTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 12),
    _CucsEtherNiErrStatsHistFrameTxDeltaMax_Type()
)
cucsEtherNiErrStatsHistFrameTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistFrameTxDeltaMax.setStatus("current")
_CucsEtherNiErrStatsHistFrameTxDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsHistFrameTxDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsHistFrameTxDeltaMin = _CucsEtherNiErrStatsHistFrameTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 13),
    _CucsEtherNiErrStatsHistFrameTxDeltaMin_Type()
)
cucsEtherNiErrStatsHistFrameTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistFrameTxDeltaMin.setStatus("current")
_CucsEtherNiErrStatsHistId_Type = Unsigned64
_CucsEtherNiErrStatsHistId_Object = MibTableColumn
cucsEtherNiErrStatsHistId = _CucsEtherNiErrStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 14),
    _CucsEtherNiErrStatsHistId_Type()
)
cucsEtherNiErrStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistId.setStatus("current")
_CucsEtherNiErrStatsHistInRange_Type = Unsigned64
_CucsEtherNiErrStatsHistInRange_Object = MibTableColumn
cucsEtherNiErrStatsHistInRange = _CucsEtherNiErrStatsHistInRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 15),
    _CucsEtherNiErrStatsHistInRange_Type()
)
cucsEtherNiErrStatsHistInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistInRange.setStatus("current")
_CucsEtherNiErrStatsHistInRangeDelta_Type = Unsigned64
_CucsEtherNiErrStatsHistInRangeDelta_Object = MibTableColumn
cucsEtherNiErrStatsHistInRangeDelta = _CucsEtherNiErrStatsHistInRangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 16),
    _CucsEtherNiErrStatsHistInRangeDelta_Type()
)
cucsEtherNiErrStatsHistInRangeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistInRangeDelta.setStatus("current")
_CucsEtherNiErrStatsHistInRangeDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsHistInRangeDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsHistInRangeDeltaAvg = _CucsEtherNiErrStatsHistInRangeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 17),
    _CucsEtherNiErrStatsHistInRangeDeltaAvg_Type()
)
cucsEtherNiErrStatsHistInRangeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistInRangeDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsHistInRangeDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsHistInRangeDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsHistInRangeDeltaMax = _CucsEtherNiErrStatsHistInRangeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 18),
    _CucsEtherNiErrStatsHistInRangeDeltaMax_Type()
)
cucsEtherNiErrStatsHistInRangeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistInRangeDeltaMax.setStatus("current")
_CucsEtherNiErrStatsHistInRangeDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsHistInRangeDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsHistInRangeDeltaMin = _CucsEtherNiErrStatsHistInRangeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 19),
    _CucsEtherNiErrStatsHistInRangeDeltaMin_Type()
)
cucsEtherNiErrStatsHistInRangeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistInRangeDeltaMin.setStatus("current")
_CucsEtherNiErrStatsHistMostRecent_Type = TruthValue
_CucsEtherNiErrStatsHistMostRecent_Object = MibTableColumn
cucsEtherNiErrStatsHistMostRecent = _CucsEtherNiErrStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 20),
    _CucsEtherNiErrStatsHistMostRecent_Type()
)
cucsEtherNiErrStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistMostRecent.setStatus("current")
_CucsEtherNiErrStatsHistSuspect_Type = TruthValue
_CucsEtherNiErrStatsHistSuspect_Object = MibTableColumn
cucsEtherNiErrStatsHistSuspect = _CucsEtherNiErrStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 21),
    _CucsEtherNiErrStatsHistSuspect_Type()
)
cucsEtherNiErrStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistSuspect.setStatus("current")
_CucsEtherNiErrStatsHistThresholded_Type = CucsEtherNiErrStatsHistThresholded
_CucsEtherNiErrStatsHistThresholded_Object = MibTableColumn
cucsEtherNiErrStatsHistThresholded = _CucsEtherNiErrStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 22),
    _CucsEtherNiErrStatsHistThresholded_Type()
)
cucsEtherNiErrStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistThresholded.setStatus("current")
_CucsEtherNiErrStatsHistTimeCollected_Type = DateAndTime
_CucsEtherNiErrStatsHistTimeCollected_Object = MibTableColumn
cucsEtherNiErrStatsHistTimeCollected = _CucsEtherNiErrStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 23),
    _CucsEtherNiErrStatsHistTimeCollected_Type()
)
cucsEtherNiErrStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTimeCollected.setStatus("current")
_CucsEtherNiErrStatsHistTooLong_Type = Unsigned64
_CucsEtherNiErrStatsHistTooLong_Object = MibTableColumn
cucsEtherNiErrStatsHistTooLong = _CucsEtherNiErrStatsHistTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 24),
    _CucsEtherNiErrStatsHistTooLong_Type()
)
cucsEtherNiErrStatsHistTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooLong.setStatus("current")
_CucsEtherNiErrStatsHistTooLongDelta_Type = Unsigned64
_CucsEtherNiErrStatsHistTooLongDelta_Object = MibTableColumn
cucsEtherNiErrStatsHistTooLongDelta = _CucsEtherNiErrStatsHistTooLongDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 25),
    _CucsEtherNiErrStatsHistTooLongDelta_Type()
)
cucsEtherNiErrStatsHistTooLongDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooLongDelta.setStatus("current")
_CucsEtherNiErrStatsHistTooLongDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsHistTooLongDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsHistTooLongDeltaAvg = _CucsEtherNiErrStatsHistTooLongDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 26),
    _CucsEtherNiErrStatsHistTooLongDeltaAvg_Type()
)
cucsEtherNiErrStatsHistTooLongDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooLongDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsHistTooLongDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsHistTooLongDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsHistTooLongDeltaMax = _CucsEtherNiErrStatsHistTooLongDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 27),
    _CucsEtherNiErrStatsHistTooLongDeltaMax_Type()
)
cucsEtherNiErrStatsHistTooLongDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooLongDeltaMax.setStatus("current")
_CucsEtherNiErrStatsHistTooLongDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsHistTooLongDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsHistTooLongDeltaMin = _CucsEtherNiErrStatsHistTooLongDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 28),
    _CucsEtherNiErrStatsHistTooLongDeltaMin_Type()
)
cucsEtherNiErrStatsHistTooLongDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooLongDeltaMin.setStatus("current")
_CucsEtherNiErrStatsHistTooShort_Type = Unsigned64
_CucsEtherNiErrStatsHistTooShort_Object = MibTableColumn
cucsEtherNiErrStatsHistTooShort = _CucsEtherNiErrStatsHistTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 29),
    _CucsEtherNiErrStatsHistTooShort_Type()
)
cucsEtherNiErrStatsHistTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooShort.setStatus("current")
_CucsEtherNiErrStatsHistTooShortDelta_Type = Unsigned64
_CucsEtherNiErrStatsHistTooShortDelta_Object = MibTableColumn
cucsEtherNiErrStatsHistTooShortDelta = _CucsEtherNiErrStatsHistTooShortDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 30),
    _CucsEtherNiErrStatsHistTooShortDelta_Type()
)
cucsEtherNiErrStatsHistTooShortDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooShortDelta.setStatus("current")
_CucsEtherNiErrStatsHistTooShortDeltaAvg_Type = Unsigned64
_CucsEtherNiErrStatsHistTooShortDeltaAvg_Object = MibTableColumn
cucsEtherNiErrStatsHistTooShortDeltaAvg = _CucsEtherNiErrStatsHistTooShortDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 31),
    _CucsEtherNiErrStatsHistTooShortDeltaAvg_Type()
)
cucsEtherNiErrStatsHistTooShortDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooShortDeltaAvg.setStatus("current")
_CucsEtherNiErrStatsHistTooShortDeltaMax_Type = Unsigned64
_CucsEtherNiErrStatsHistTooShortDeltaMax_Object = MibTableColumn
cucsEtherNiErrStatsHistTooShortDeltaMax = _CucsEtherNiErrStatsHistTooShortDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 32),
    _CucsEtherNiErrStatsHistTooShortDeltaMax_Type()
)
cucsEtherNiErrStatsHistTooShortDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooShortDeltaMax.setStatus("current")
_CucsEtherNiErrStatsHistTooShortDeltaMin_Type = Unsigned64
_CucsEtherNiErrStatsHistTooShortDeltaMin_Object = MibTableColumn
cucsEtherNiErrStatsHistTooShortDeltaMin = _CucsEtherNiErrStatsHistTooShortDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 16, 31, 1, 33),
    _CucsEtherNiErrStatsHistTooShortDeltaMin_Type()
)
cucsEtherNiErrStatsHistTooShortDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEtherNiErrStatsHistTooShortDeltaMin.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-ETHER-MIB",
    **{"cucsEtherObjects": cucsEtherObjects,
       "cucsEtherErrStatsTable": cucsEtherErrStatsTable,
       "cucsEtherErrStatsEntry": cucsEtherErrStatsEntry,
       "cucsEtherErrStatsInstanceId": cucsEtherErrStatsInstanceId,
       "cucsEtherErrStatsDn": cucsEtherErrStatsDn,
       "cucsEtherErrStatsRn": cucsEtherErrStatsRn,
       "cucsEtherErrStatsAlign": cucsEtherErrStatsAlign,
       "cucsEtherErrStatsAlignDelta": cucsEtherErrStatsAlignDelta,
       "cucsEtherErrStatsAlignDeltaAvg": cucsEtherErrStatsAlignDeltaAvg,
       "cucsEtherErrStatsAlignDeltaMax": cucsEtherErrStatsAlignDeltaMax,
       "cucsEtherErrStatsAlignDeltaMin": cucsEtherErrStatsAlignDeltaMin,
       "cucsEtherErrStatsDeferredTx": cucsEtherErrStatsDeferredTx,
       "cucsEtherErrStatsDeferredTxDelta": cucsEtherErrStatsDeferredTxDelta,
       "cucsEtherErrStatsDeferredTxDeltaAvg": cucsEtherErrStatsDeferredTxDeltaAvg,
       "cucsEtherErrStatsDeferredTxDeltaMax": cucsEtherErrStatsDeferredTxDeltaMax,
       "cucsEtherErrStatsDeferredTxDeltaMin": cucsEtherErrStatsDeferredTxDeltaMin,
       "cucsEtherErrStatsFcs": cucsEtherErrStatsFcs,
       "cucsEtherErrStatsFcsDelta": cucsEtherErrStatsFcsDelta,
       "cucsEtherErrStatsFcsDeltaAvg": cucsEtherErrStatsFcsDeltaAvg,
       "cucsEtherErrStatsFcsDeltaMax": cucsEtherErrStatsFcsDeltaMax,
       "cucsEtherErrStatsFcsDeltaMin": cucsEtherErrStatsFcsDeltaMin,
       "cucsEtherErrStatsIntMacRx": cucsEtherErrStatsIntMacRx,
       "cucsEtherErrStatsIntMacRxDelta": cucsEtherErrStatsIntMacRxDelta,
       "cucsEtherErrStatsIntMacRxDeltaAvg": cucsEtherErrStatsIntMacRxDeltaAvg,
       "cucsEtherErrStatsIntMacRxDeltaMax": cucsEtherErrStatsIntMacRxDeltaMax,
       "cucsEtherErrStatsIntMacRxDeltaMin": cucsEtherErrStatsIntMacRxDeltaMin,
       "cucsEtherErrStatsIntMacTx": cucsEtherErrStatsIntMacTx,
       "cucsEtherErrStatsIntMacTxDelta": cucsEtherErrStatsIntMacTxDelta,
       "cucsEtherErrStatsIntMacTxDeltaAvg": cucsEtherErrStatsIntMacTxDeltaAvg,
       "cucsEtherErrStatsIntMacTxDeltaMax": cucsEtherErrStatsIntMacTxDeltaMax,
       "cucsEtherErrStatsIntMacTxDeltaMin": cucsEtherErrStatsIntMacTxDeltaMin,
       "cucsEtherErrStatsIntervals": cucsEtherErrStatsIntervals,
       "cucsEtherErrStatsOutDiscard": cucsEtherErrStatsOutDiscard,
       "cucsEtherErrStatsOutDiscardDelta": cucsEtherErrStatsOutDiscardDelta,
       "cucsEtherErrStatsOutDiscardDeltaAvg": cucsEtherErrStatsOutDiscardDeltaAvg,
       "cucsEtherErrStatsOutDiscardDeltaMax": cucsEtherErrStatsOutDiscardDeltaMax,
       "cucsEtherErrStatsOutDiscardDeltaMin": cucsEtherErrStatsOutDiscardDeltaMin,
       "cucsEtherErrStatsRcv": cucsEtherErrStatsRcv,
       "cucsEtherErrStatsRcvDelta": cucsEtherErrStatsRcvDelta,
       "cucsEtherErrStatsRcvDeltaAvg": cucsEtherErrStatsRcvDeltaAvg,
       "cucsEtherErrStatsRcvDeltaMax": cucsEtherErrStatsRcvDeltaMax,
       "cucsEtherErrStatsRcvDeltaMin": cucsEtherErrStatsRcvDeltaMin,
       "cucsEtherErrStatsSuspect": cucsEtherErrStatsSuspect,
       "cucsEtherErrStatsThresholded": cucsEtherErrStatsThresholded,
       "cucsEtherErrStatsTimeCollected": cucsEtherErrStatsTimeCollected,
       "cucsEtherErrStatsUnderSize": cucsEtherErrStatsUnderSize,
       "cucsEtherErrStatsUnderSizeDelta": cucsEtherErrStatsUnderSizeDelta,
       "cucsEtherErrStatsUnderSizeDeltaAvg": cucsEtherErrStatsUnderSizeDeltaAvg,
       "cucsEtherErrStatsUnderSizeDeltaMax": cucsEtherErrStatsUnderSizeDeltaMax,
       "cucsEtherErrStatsUnderSizeDeltaMin": cucsEtherErrStatsUnderSizeDeltaMin,
       "cucsEtherErrStatsUpdate": cucsEtherErrStatsUpdate,
       "cucsEtherErrStatsXmit": cucsEtherErrStatsXmit,
       "cucsEtherErrStatsXmitDelta": cucsEtherErrStatsXmitDelta,
       "cucsEtherErrStatsXmitDeltaAvg": cucsEtherErrStatsXmitDeltaAvg,
       "cucsEtherErrStatsXmitDeltaMax": cucsEtherErrStatsXmitDeltaMax,
       "cucsEtherErrStatsXmitDeltaMin": cucsEtherErrStatsXmitDeltaMin,
       "cucsEtherErrStatsHistTable": cucsEtherErrStatsHistTable,
       "cucsEtherErrStatsHistEntry": cucsEtherErrStatsHistEntry,
       "cucsEtherErrStatsHistInstanceId": cucsEtherErrStatsHistInstanceId,
       "cucsEtherErrStatsHistDn": cucsEtherErrStatsHistDn,
       "cucsEtherErrStatsHistRn": cucsEtherErrStatsHistRn,
       "cucsEtherErrStatsHistAlign": cucsEtherErrStatsHistAlign,
       "cucsEtherErrStatsHistAlignDelta": cucsEtherErrStatsHistAlignDelta,
       "cucsEtherErrStatsHistAlignDeltaAvg": cucsEtherErrStatsHistAlignDeltaAvg,
       "cucsEtherErrStatsHistAlignDeltaMax": cucsEtherErrStatsHistAlignDeltaMax,
       "cucsEtherErrStatsHistAlignDeltaMin": cucsEtherErrStatsHistAlignDeltaMin,
       "cucsEtherErrStatsHistDeferredTx": cucsEtherErrStatsHistDeferredTx,
       "cucsEtherErrStatsHistDeferredTxDelta": cucsEtherErrStatsHistDeferredTxDelta,
       "cucsEtherErrStatsHistDeferredTxDeltaAvg": cucsEtherErrStatsHistDeferredTxDeltaAvg,
       "cucsEtherErrStatsHistDeferredTxDeltaMax": cucsEtherErrStatsHistDeferredTxDeltaMax,
       "cucsEtherErrStatsHistDeferredTxDeltaMin": cucsEtherErrStatsHistDeferredTxDeltaMin,
       "cucsEtherErrStatsHistFcs": cucsEtherErrStatsHistFcs,
       "cucsEtherErrStatsHistFcsDelta": cucsEtherErrStatsHistFcsDelta,
       "cucsEtherErrStatsHistFcsDeltaAvg": cucsEtherErrStatsHistFcsDeltaAvg,
       "cucsEtherErrStatsHistFcsDeltaMax": cucsEtherErrStatsHistFcsDeltaMax,
       "cucsEtherErrStatsHistFcsDeltaMin": cucsEtherErrStatsHistFcsDeltaMin,
       "cucsEtherErrStatsHistId": cucsEtherErrStatsHistId,
       "cucsEtherErrStatsHistIntMacRx": cucsEtherErrStatsHistIntMacRx,
       "cucsEtherErrStatsHistIntMacRxDelta": cucsEtherErrStatsHistIntMacRxDelta,
       "cucsEtherErrStatsHistIntMacRxDeltaAvg": cucsEtherErrStatsHistIntMacRxDeltaAvg,
       "cucsEtherErrStatsHistIntMacRxDeltaMax": cucsEtherErrStatsHistIntMacRxDeltaMax,
       "cucsEtherErrStatsHistIntMacRxDeltaMin": cucsEtherErrStatsHistIntMacRxDeltaMin,
       "cucsEtherErrStatsHistIntMacTx": cucsEtherErrStatsHistIntMacTx,
       "cucsEtherErrStatsHistIntMacTxDelta": cucsEtherErrStatsHistIntMacTxDelta,
       "cucsEtherErrStatsHistIntMacTxDeltaAvg": cucsEtherErrStatsHistIntMacTxDeltaAvg,
       "cucsEtherErrStatsHistIntMacTxDeltaMax": cucsEtherErrStatsHistIntMacTxDeltaMax,
       "cucsEtherErrStatsHistIntMacTxDeltaMin": cucsEtherErrStatsHistIntMacTxDeltaMin,
       "cucsEtherErrStatsHistMostRecent": cucsEtherErrStatsHistMostRecent,
       "cucsEtherErrStatsHistOutDiscard": cucsEtherErrStatsHistOutDiscard,
       "cucsEtherErrStatsHistOutDiscardDelta": cucsEtherErrStatsHistOutDiscardDelta,
       "cucsEtherErrStatsHistOutDiscardDeltaAvg": cucsEtherErrStatsHistOutDiscardDeltaAvg,
       "cucsEtherErrStatsHistOutDiscardDeltaMax": cucsEtherErrStatsHistOutDiscardDeltaMax,
       "cucsEtherErrStatsHistOutDiscardDeltaMin": cucsEtherErrStatsHistOutDiscardDeltaMin,
       "cucsEtherErrStatsHistRcv": cucsEtherErrStatsHistRcv,
       "cucsEtherErrStatsHistRcvDelta": cucsEtherErrStatsHistRcvDelta,
       "cucsEtherErrStatsHistRcvDeltaAvg": cucsEtherErrStatsHistRcvDeltaAvg,
       "cucsEtherErrStatsHistRcvDeltaMax": cucsEtherErrStatsHistRcvDeltaMax,
       "cucsEtherErrStatsHistRcvDeltaMin": cucsEtherErrStatsHistRcvDeltaMin,
       "cucsEtherErrStatsHistSuspect": cucsEtherErrStatsHistSuspect,
       "cucsEtherErrStatsHistThresholded": cucsEtherErrStatsHistThresholded,
       "cucsEtherErrStatsHistTimeCollected": cucsEtherErrStatsHistTimeCollected,
       "cucsEtherErrStatsHistUnderSize": cucsEtherErrStatsHistUnderSize,
       "cucsEtherErrStatsHistUnderSizeDelta": cucsEtherErrStatsHistUnderSizeDelta,
       "cucsEtherErrStatsHistUnderSizeDeltaAvg": cucsEtherErrStatsHistUnderSizeDeltaAvg,
       "cucsEtherErrStatsHistUnderSizeDeltaMax": cucsEtherErrStatsHistUnderSizeDeltaMax,
       "cucsEtherErrStatsHistUnderSizeDeltaMin": cucsEtherErrStatsHistUnderSizeDeltaMin,
       "cucsEtherErrStatsHistXmit": cucsEtherErrStatsHistXmit,
       "cucsEtherErrStatsHistXmitDelta": cucsEtherErrStatsHistXmitDelta,
       "cucsEtherErrStatsHistXmitDeltaAvg": cucsEtherErrStatsHistXmitDeltaAvg,
       "cucsEtherErrStatsHistXmitDeltaMax": cucsEtherErrStatsHistXmitDeltaMax,
       "cucsEtherErrStatsHistXmitDeltaMin": cucsEtherErrStatsHistXmitDeltaMin,
       "cucsEtherLossStatsTable": cucsEtherLossStatsTable,
       "cucsEtherLossStatsEntry": cucsEtherLossStatsEntry,
       "cucsEtherLossStatsInstanceId": cucsEtherLossStatsInstanceId,
       "cucsEtherLossStatsDn": cucsEtherLossStatsDn,
       "cucsEtherLossStatsRn": cucsEtherLossStatsRn,
       "cucsEtherLossStatsSQETest": cucsEtherLossStatsSQETest,
       "cucsEtherLossStatsSQETestDelta": cucsEtherLossStatsSQETestDelta,
       "cucsEtherLossStatsSQETestDeltaAvg": cucsEtherLossStatsSQETestDeltaAvg,
       "cucsEtherLossStatsSQETestDeltaMax": cucsEtherLossStatsSQETestDeltaMax,
       "cucsEtherLossStatsSQETestDeltaMin": cucsEtherLossStatsSQETestDeltaMin,
       "cucsEtherLossStatsCarrierSense": cucsEtherLossStatsCarrierSense,
       "cucsEtherLossStatsCarrierSenseDelta": cucsEtherLossStatsCarrierSenseDelta,
       "cucsEtherLossStatsCarrierSenseDeltaAvg": cucsEtherLossStatsCarrierSenseDeltaAvg,
       "cucsEtherLossStatsCarrierSenseDeltaMax": cucsEtherLossStatsCarrierSenseDeltaMax,
       "cucsEtherLossStatsCarrierSenseDeltaMin": cucsEtherLossStatsCarrierSenseDeltaMin,
       "cucsEtherLossStatsExcessCollision": cucsEtherLossStatsExcessCollision,
       "cucsEtherLossStatsExcessCollisionDelta": cucsEtherLossStatsExcessCollisionDelta,
       "cucsEtherLossStatsExcessCollisionDeltaAvg": cucsEtherLossStatsExcessCollisionDeltaAvg,
       "cucsEtherLossStatsExcessCollisionDeltaMax": cucsEtherLossStatsExcessCollisionDeltaMax,
       "cucsEtherLossStatsExcessCollisionDeltaMin": cucsEtherLossStatsExcessCollisionDeltaMin,
       "cucsEtherLossStatsGiants": cucsEtherLossStatsGiants,
       "cucsEtherLossStatsGiantsDelta": cucsEtherLossStatsGiantsDelta,
       "cucsEtherLossStatsGiantsDeltaAvg": cucsEtherLossStatsGiantsDeltaAvg,
       "cucsEtherLossStatsGiantsDeltaMax": cucsEtherLossStatsGiantsDeltaMax,
       "cucsEtherLossStatsGiantsDeltaMin": cucsEtherLossStatsGiantsDeltaMin,
       "cucsEtherLossStatsIntervals": cucsEtherLossStatsIntervals,
       "cucsEtherLossStatsLateCollision": cucsEtherLossStatsLateCollision,
       "cucsEtherLossStatsLateCollisionDelta": cucsEtherLossStatsLateCollisionDelta,
       "cucsEtherLossStatsLateCollisionDeltaAvg": cucsEtherLossStatsLateCollisionDeltaAvg,
       "cucsEtherLossStatsLateCollisionDeltaMax": cucsEtherLossStatsLateCollisionDeltaMax,
       "cucsEtherLossStatsLateCollisionDeltaMin": cucsEtherLossStatsLateCollisionDeltaMin,
       "cucsEtherLossStatsMultiCollision": cucsEtherLossStatsMultiCollision,
       "cucsEtherLossStatsMultiCollisionDelta": cucsEtherLossStatsMultiCollisionDelta,
       "cucsEtherLossStatsMultiCollisionDeltaAvg": cucsEtherLossStatsMultiCollisionDeltaAvg,
       "cucsEtherLossStatsMultiCollisionDeltaMax": cucsEtherLossStatsMultiCollisionDeltaMax,
       "cucsEtherLossStatsMultiCollisionDeltaMin": cucsEtherLossStatsMultiCollisionDeltaMin,
       "cucsEtherLossStatsSingleCollision": cucsEtherLossStatsSingleCollision,
       "cucsEtherLossStatsSingleCollisionDelta": cucsEtherLossStatsSingleCollisionDelta,
       "cucsEtherLossStatsSingleCollisionDeltaAvg": cucsEtherLossStatsSingleCollisionDeltaAvg,
       "cucsEtherLossStatsSingleCollisionDeltaMax": cucsEtherLossStatsSingleCollisionDeltaMax,
       "cucsEtherLossStatsSingleCollisionDeltaMin": cucsEtherLossStatsSingleCollisionDeltaMin,
       "cucsEtherLossStatsSuspect": cucsEtherLossStatsSuspect,
       "cucsEtherLossStatsSymbol": cucsEtherLossStatsSymbol,
       "cucsEtherLossStatsSymbolDelta": cucsEtherLossStatsSymbolDelta,
       "cucsEtherLossStatsSymbolDeltaAvg": cucsEtherLossStatsSymbolDeltaAvg,
       "cucsEtherLossStatsSymbolDeltaMax": cucsEtherLossStatsSymbolDeltaMax,
       "cucsEtherLossStatsSymbolDeltaMin": cucsEtherLossStatsSymbolDeltaMin,
       "cucsEtherLossStatsThresholded": cucsEtherLossStatsThresholded,
       "cucsEtherLossStatsTimeCollected": cucsEtherLossStatsTimeCollected,
       "cucsEtherLossStatsUpdate": cucsEtherLossStatsUpdate,
       "cucsEtherLossStatsHistTable": cucsEtherLossStatsHistTable,
       "cucsEtherLossStatsHistEntry": cucsEtherLossStatsHistEntry,
       "cucsEtherLossStatsHistInstanceId": cucsEtherLossStatsHistInstanceId,
       "cucsEtherLossStatsHistDn": cucsEtherLossStatsHistDn,
       "cucsEtherLossStatsHistRn": cucsEtherLossStatsHistRn,
       "cucsEtherLossStatsHistSQETest": cucsEtherLossStatsHistSQETest,
       "cucsEtherLossStatsHistSQETestDelta": cucsEtherLossStatsHistSQETestDelta,
       "cucsEtherLossStatsHistSQETestDeltaAvg": cucsEtherLossStatsHistSQETestDeltaAvg,
       "cucsEtherLossStatsHistSQETestDeltaMax": cucsEtherLossStatsHistSQETestDeltaMax,
       "cucsEtherLossStatsHistSQETestDeltaMin": cucsEtherLossStatsHistSQETestDeltaMin,
       "cucsEtherLossStatsHistCarrierSense": cucsEtherLossStatsHistCarrierSense,
       "cucsEtherLossStatsHistCarrierSenseDelta": cucsEtherLossStatsHistCarrierSenseDelta,
       "cucsEtherLossStatsHistCarrierSenseDeltaAvg": cucsEtherLossStatsHistCarrierSenseDeltaAvg,
       "cucsEtherLossStatsHistCarrierSenseDeltaMax": cucsEtherLossStatsHistCarrierSenseDeltaMax,
       "cucsEtherLossStatsHistCarrierSenseDeltaMin": cucsEtherLossStatsHistCarrierSenseDeltaMin,
       "cucsEtherLossStatsHistExcessCollision": cucsEtherLossStatsHistExcessCollision,
       "cucsEtherLossStatsHistExcessCollisionDelta": cucsEtherLossStatsHistExcessCollisionDelta,
       "cucsEtherLossStatsHistExcessCollisionDeltaAvg": cucsEtherLossStatsHistExcessCollisionDeltaAvg,
       "cucsEtherLossStatsHistExcessCollisionDeltaMax": cucsEtherLossStatsHistExcessCollisionDeltaMax,
       "cucsEtherLossStatsHistExcessCollisionDeltaMin": cucsEtherLossStatsHistExcessCollisionDeltaMin,
       "cucsEtherLossStatsHistGiants": cucsEtherLossStatsHistGiants,
       "cucsEtherLossStatsHistGiantsDelta": cucsEtherLossStatsHistGiantsDelta,
       "cucsEtherLossStatsHistGiantsDeltaAvg": cucsEtherLossStatsHistGiantsDeltaAvg,
       "cucsEtherLossStatsHistGiantsDeltaMax": cucsEtherLossStatsHistGiantsDeltaMax,
       "cucsEtherLossStatsHistGiantsDeltaMin": cucsEtherLossStatsHistGiantsDeltaMin,
       "cucsEtherLossStatsHistId": cucsEtherLossStatsHistId,
       "cucsEtherLossStatsHistLateCollision": cucsEtherLossStatsHistLateCollision,
       "cucsEtherLossStatsHistLateCollisionDelta": cucsEtherLossStatsHistLateCollisionDelta,
       "cucsEtherLossStatsHistLateCollisionDeltaAvg": cucsEtherLossStatsHistLateCollisionDeltaAvg,
       "cucsEtherLossStatsHistLateCollisionDeltaMax": cucsEtherLossStatsHistLateCollisionDeltaMax,
       "cucsEtherLossStatsHistLateCollisionDeltaMin": cucsEtherLossStatsHistLateCollisionDeltaMin,
       "cucsEtherLossStatsHistMostRecent": cucsEtherLossStatsHistMostRecent,
       "cucsEtherLossStatsHistMultiCollision": cucsEtherLossStatsHistMultiCollision,
       "cucsEtherLossStatsHistMultiCollisionDelta": cucsEtherLossStatsHistMultiCollisionDelta,
       "cucsEtherLossStatsHistMultiCollisionDeltaAvg": cucsEtherLossStatsHistMultiCollisionDeltaAvg,
       "cucsEtherLossStatsHistMultiCollisionDeltaMax": cucsEtherLossStatsHistMultiCollisionDeltaMax,
       "cucsEtherLossStatsHistMultiCollisionDeltaMin": cucsEtherLossStatsHistMultiCollisionDeltaMin,
       "cucsEtherLossStatsHistSingleCollision": cucsEtherLossStatsHistSingleCollision,
       "cucsEtherLossStatsHistSingleCollisionDelta": cucsEtherLossStatsHistSingleCollisionDelta,
       "cucsEtherLossStatsHistSingleCollisionDeltaAvg": cucsEtherLossStatsHistSingleCollisionDeltaAvg,
       "cucsEtherLossStatsHistSingleCollisionDeltaMax": cucsEtherLossStatsHistSingleCollisionDeltaMax,
       "cucsEtherLossStatsHistSingleCollisionDeltaMin": cucsEtherLossStatsHistSingleCollisionDeltaMin,
       "cucsEtherLossStatsHistSuspect": cucsEtherLossStatsHistSuspect,
       "cucsEtherLossStatsHistSymbol": cucsEtherLossStatsHistSymbol,
       "cucsEtherLossStatsHistSymbolDelta": cucsEtherLossStatsHistSymbolDelta,
       "cucsEtherLossStatsHistSymbolDeltaAvg": cucsEtherLossStatsHistSymbolDeltaAvg,
       "cucsEtherLossStatsHistSymbolDeltaMax": cucsEtherLossStatsHistSymbolDeltaMax,
       "cucsEtherLossStatsHistSymbolDeltaMin": cucsEtherLossStatsHistSymbolDeltaMin,
       "cucsEtherLossStatsHistThresholded": cucsEtherLossStatsHistThresholded,
       "cucsEtherLossStatsHistTimeCollected": cucsEtherLossStatsHistTimeCollected,
       "cucsEtherNicIfConfigTable": cucsEtherNicIfConfigTable,
       "cucsEtherNicIfConfigEntry": cucsEtherNicIfConfigEntry,
       "cucsEtherNicIfConfigInstanceId": cucsEtherNicIfConfigInstanceId,
       "cucsEtherNicIfConfigDn": cucsEtherNicIfConfigDn,
       "cucsEtherNicIfConfigRn": cucsEtherNicIfConfigRn,
       "cucsEtherPIoTable": cucsEtherPIoTable,
       "cucsEtherPIoEntry": cucsEtherPIoEntry,
       "cucsEtherPIoInstanceId": cucsEtherPIoInstanceId,
       "cucsEtherPIoDn": cucsEtherPIoDn,
       "cucsEtherPIoRn": cucsEtherPIoRn,
       "cucsEtherPIoAdminState": cucsEtherPIoAdminState,
       "cucsEtherPIoChassisId": cucsEtherPIoChassisId,
       "cucsEtherPIoEncap": cucsEtherPIoEncap,
       "cucsEtherPIoEpDn": cucsEtherPIoEpDn,
       "cucsEtherPIoFltAggr": cucsEtherPIoFltAggr,
       "cucsEtherPIoIfRole": cucsEtherPIoIfRole,
       "cucsEtherPIoIfType": cucsEtherPIoIfType,
       "cucsEtherPIoLocale": cucsEtherPIoLocale,
       "cucsEtherPIoMac": cucsEtherPIoMac,
       "cucsEtherPIoMode": cucsEtherPIoMode,
       "cucsEtherPIoModel": cucsEtherPIoModel,
       "cucsEtherPIoName": cucsEtherPIoName,
       "cucsEtherPIoOperSpeed": cucsEtherPIoOperSpeed,
       "cucsEtherPIoOperState": cucsEtherPIoOperState,
       "cucsEtherPIoPeerDn": cucsEtherPIoPeerDn,
       "cucsEtherPIoPeerPortId": cucsEtherPIoPeerPortId,
       "cucsEtherPIoPeerSlotId": cucsEtherPIoPeerSlotId,
       "cucsEtherPIoPortId": cucsEtherPIoPortId,
       "cucsEtherPIoRevision": cucsEtherPIoRevision,
       "cucsEtherPIoSerial": cucsEtherPIoSerial,
       "cucsEtherPIoSlotId": cucsEtherPIoSlotId,
       "cucsEtherPIoStateQual": cucsEtherPIoStateQual,
       "cucsEtherPIoSwitchId": cucsEtherPIoSwitchId,
       "cucsEtherPIoTransport": cucsEtherPIoTransport,
       "cucsEtherPIoTs": cucsEtherPIoTs,
       "cucsEtherPIoType": cucsEtherPIoType,
       "cucsEtherPIoUsrLbl": cucsEtherPIoUsrLbl,
       "cucsEtherPIoVendor": cucsEtherPIoVendor,
       "cucsEtherPIoFsmDescr": cucsEtherPIoFsmDescr,
       "cucsEtherPIoFsmPrev": cucsEtherPIoFsmPrev,
       "cucsEtherPIoFsmProgr": cucsEtherPIoFsmProgr,
       "cucsEtherPIoFsmRmtInvErrCode": cucsEtherPIoFsmRmtInvErrCode,
       "cucsEtherPIoFsmRmtInvErrDescr": cucsEtherPIoFsmRmtInvErrDescr,
       "cucsEtherPIoFsmRmtInvRslt": cucsEtherPIoFsmRmtInvRslt,
       "cucsEtherPIoFsmStageDescr": cucsEtherPIoFsmStageDescr,
       "cucsEtherPIoFsmStamp": cucsEtherPIoFsmStamp,
       "cucsEtherPIoFsmStatus": cucsEtherPIoFsmStatus,
       "cucsEtherPIoFsmTry": cucsEtherPIoFsmTry,
       "cucsEtherPIoLicGP": cucsEtherPIoLicGP,
       "cucsEtherPIoLicState": cucsEtherPIoLicState,
       "cucsEtherPIoXcvrType": cucsEtherPIoXcvrType,
       "cucsEtherPIoPeerChassisId": cucsEtherPIoPeerChassisId,
       "cucsEtherPIoAdminTransport": cucsEtherPIoAdminTransport,
       "cucsEtherPIoLc": cucsEtherPIoLc,
       "cucsEtherPIoUnifiedPort": cucsEtherPIoUnifiedPort,
       "cucsEtherPIoIsPortChannelMember": cucsEtherPIoIsPortChannelMember,
       "cucsEtherPIoAggrPortId": cucsEtherPIoAggrPortId,
       "cucsEtherPIoPeerAggrPortId": cucsEtherPIoPeerAggrPortId,
       "cucsEtherPIoNonCR4": cucsEtherPIoNonCR4,
       "cucsEtherPauseStatsTable": cucsEtherPauseStatsTable,
       "cucsEtherPauseStatsEntry": cucsEtherPauseStatsEntry,
       "cucsEtherPauseStatsInstanceId": cucsEtherPauseStatsInstanceId,
       "cucsEtherPauseStatsDn": cucsEtherPauseStatsDn,
       "cucsEtherPauseStatsRn": cucsEtherPauseStatsRn,
       "cucsEtherPauseStatsIntervals": cucsEtherPauseStatsIntervals,
       "cucsEtherPauseStatsRecvPause": cucsEtherPauseStatsRecvPause,
       "cucsEtherPauseStatsRecvPauseDelta": cucsEtherPauseStatsRecvPauseDelta,
       "cucsEtherPauseStatsRecvPauseDeltaAvg": cucsEtherPauseStatsRecvPauseDeltaAvg,
       "cucsEtherPauseStatsRecvPauseDeltaMax": cucsEtherPauseStatsRecvPauseDeltaMax,
       "cucsEtherPauseStatsRecvPauseDeltaMin": cucsEtherPauseStatsRecvPauseDeltaMin,
       "cucsEtherPauseStatsResets": cucsEtherPauseStatsResets,
       "cucsEtherPauseStatsResetsDelta": cucsEtherPauseStatsResetsDelta,
       "cucsEtherPauseStatsResetsDeltaAvg": cucsEtherPauseStatsResetsDeltaAvg,
       "cucsEtherPauseStatsResetsDeltaMax": cucsEtherPauseStatsResetsDeltaMax,
       "cucsEtherPauseStatsResetsDeltaMin": cucsEtherPauseStatsResetsDeltaMin,
       "cucsEtherPauseStatsSuspect": cucsEtherPauseStatsSuspect,
       "cucsEtherPauseStatsThresholded": cucsEtherPauseStatsThresholded,
       "cucsEtherPauseStatsTimeCollected": cucsEtherPauseStatsTimeCollected,
       "cucsEtherPauseStatsUpdate": cucsEtherPauseStatsUpdate,
       "cucsEtherPauseStatsXmitPause": cucsEtherPauseStatsXmitPause,
       "cucsEtherPauseStatsXmitPauseDelta": cucsEtherPauseStatsXmitPauseDelta,
       "cucsEtherPauseStatsXmitPauseDeltaAvg": cucsEtherPauseStatsXmitPauseDeltaAvg,
       "cucsEtherPauseStatsXmitPauseDeltaMax": cucsEtherPauseStatsXmitPauseDeltaMax,
       "cucsEtherPauseStatsXmitPauseDeltaMin": cucsEtherPauseStatsXmitPauseDeltaMin,
       "cucsEtherPauseStatsHistTable": cucsEtherPauseStatsHistTable,
       "cucsEtherPauseStatsHistEntry": cucsEtherPauseStatsHistEntry,
       "cucsEtherPauseStatsHistInstanceId": cucsEtherPauseStatsHistInstanceId,
       "cucsEtherPauseStatsHistDn": cucsEtherPauseStatsHistDn,
       "cucsEtherPauseStatsHistRn": cucsEtherPauseStatsHistRn,
       "cucsEtherPauseStatsHistId": cucsEtherPauseStatsHistId,
       "cucsEtherPauseStatsHistMostRecent": cucsEtherPauseStatsHistMostRecent,
       "cucsEtherPauseStatsHistRecvPause": cucsEtherPauseStatsHistRecvPause,
       "cucsEtherPauseStatsHistRecvPauseDelta": cucsEtherPauseStatsHistRecvPauseDelta,
       "cucsEtherPauseStatsHistRecvPauseDeltaAvg": cucsEtherPauseStatsHistRecvPauseDeltaAvg,
       "cucsEtherPauseStatsHistRecvPauseDeltaMax": cucsEtherPauseStatsHistRecvPauseDeltaMax,
       "cucsEtherPauseStatsHistRecvPauseDeltaMin": cucsEtherPauseStatsHistRecvPauseDeltaMin,
       "cucsEtherPauseStatsHistResets": cucsEtherPauseStatsHistResets,
       "cucsEtherPauseStatsHistResetsDelta": cucsEtherPauseStatsHistResetsDelta,
       "cucsEtherPauseStatsHistResetsDeltaAvg": cucsEtherPauseStatsHistResetsDeltaAvg,
       "cucsEtherPauseStatsHistResetsDeltaMax": cucsEtherPauseStatsHistResetsDeltaMax,
       "cucsEtherPauseStatsHistResetsDeltaMin": cucsEtherPauseStatsHistResetsDeltaMin,
       "cucsEtherPauseStatsHistSuspect": cucsEtherPauseStatsHistSuspect,
       "cucsEtherPauseStatsHistThresholded": cucsEtherPauseStatsHistThresholded,
       "cucsEtherPauseStatsHistTimeCollected": cucsEtherPauseStatsHistTimeCollected,
       "cucsEtherPauseStatsHistXmitPause": cucsEtherPauseStatsHistXmitPause,
       "cucsEtherPauseStatsHistXmitPauseDelta": cucsEtherPauseStatsHistXmitPauseDelta,
       "cucsEtherPauseStatsHistXmitPauseDeltaAvg": cucsEtherPauseStatsHistXmitPauseDeltaAvg,
       "cucsEtherPauseStatsHistXmitPauseDeltaMax": cucsEtherPauseStatsHistXmitPauseDeltaMax,
       "cucsEtherPauseStatsHistXmitPauseDeltaMin": cucsEtherPauseStatsHistXmitPauseDeltaMin,
       "cucsEtherRxStatsTable": cucsEtherRxStatsTable,
       "cucsEtherRxStatsEntry": cucsEtherRxStatsEntry,
       "cucsEtherRxStatsInstanceId": cucsEtherRxStatsInstanceId,
       "cucsEtherRxStatsDn": cucsEtherRxStatsDn,
       "cucsEtherRxStatsRn": cucsEtherRxStatsRn,
       "cucsEtherRxStatsBroadcastPackets": cucsEtherRxStatsBroadcastPackets,
       "cucsEtherRxStatsBroadcastPacketsDelta": cucsEtherRxStatsBroadcastPacketsDelta,
       "cucsEtherRxStatsBroadcastPacketsDeltaAvg": cucsEtherRxStatsBroadcastPacketsDeltaAvg,
       "cucsEtherRxStatsBroadcastPacketsDeltaMax": cucsEtherRxStatsBroadcastPacketsDeltaMax,
       "cucsEtherRxStatsBroadcastPacketsDeltaMin": cucsEtherRxStatsBroadcastPacketsDeltaMin,
       "cucsEtherRxStatsIntervals": cucsEtherRxStatsIntervals,
       "cucsEtherRxStatsJumboPackets": cucsEtherRxStatsJumboPackets,
       "cucsEtherRxStatsJumboPacketsDelta": cucsEtherRxStatsJumboPacketsDelta,
       "cucsEtherRxStatsJumboPacketsDeltaAvg": cucsEtherRxStatsJumboPacketsDeltaAvg,
       "cucsEtherRxStatsJumboPacketsDeltaMax": cucsEtherRxStatsJumboPacketsDeltaMax,
       "cucsEtherRxStatsJumboPacketsDeltaMin": cucsEtherRxStatsJumboPacketsDeltaMin,
       "cucsEtherRxStatsMulticastPackets": cucsEtherRxStatsMulticastPackets,
       "cucsEtherRxStatsMulticastPacketsDelta": cucsEtherRxStatsMulticastPacketsDelta,
       "cucsEtherRxStatsMulticastPacketsDeltaAvg": cucsEtherRxStatsMulticastPacketsDeltaAvg,
       "cucsEtherRxStatsMulticastPacketsDeltaMax": cucsEtherRxStatsMulticastPacketsDeltaMax,
       "cucsEtherRxStatsMulticastPacketsDeltaMin": cucsEtherRxStatsMulticastPacketsDeltaMin,
       "cucsEtherRxStatsSuspect": cucsEtherRxStatsSuspect,
       "cucsEtherRxStatsThresholded": cucsEtherRxStatsThresholded,
       "cucsEtherRxStatsTimeCollected": cucsEtherRxStatsTimeCollected,
       "cucsEtherRxStatsTotalBytes": cucsEtherRxStatsTotalBytes,
       "cucsEtherRxStatsTotalBytesDelta": cucsEtherRxStatsTotalBytesDelta,
       "cucsEtherRxStatsTotalBytesDeltaAvg": cucsEtherRxStatsTotalBytesDeltaAvg,
       "cucsEtherRxStatsTotalBytesDeltaMax": cucsEtherRxStatsTotalBytesDeltaMax,
       "cucsEtherRxStatsTotalBytesDeltaMin": cucsEtherRxStatsTotalBytesDeltaMin,
       "cucsEtherRxStatsTotalPackets": cucsEtherRxStatsTotalPackets,
       "cucsEtherRxStatsTotalPacketsDelta": cucsEtherRxStatsTotalPacketsDelta,
       "cucsEtherRxStatsTotalPacketsDeltaAvg": cucsEtherRxStatsTotalPacketsDeltaAvg,
       "cucsEtherRxStatsTotalPacketsDeltaMax": cucsEtherRxStatsTotalPacketsDeltaMax,
       "cucsEtherRxStatsTotalPacketsDeltaMin": cucsEtherRxStatsTotalPacketsDeltaMin,
       "cucsEtherRxStatsUnicastPackets": cucsEtherRxStatsUnicastPackets,
       "cucsEtherRxStatsUnicastPacketsDelta": cucsEtherRxStatsUnicastPacketsDelta,
       "cucsEtherRxStatsUnicastPacketsDeltaAvg": cucsEtherRxStatsUnicastPacketsDeltaAvg,
       "cucsEtherRxStatsUnicastPacketsDeltaMax": cucsEtherRxStatsUnicastPacketsDeltaMax,
       "cucsEtherRxStatsUnicastPacketsDeltaMin": cucsEtherRxStatsUnicastPacketsDeltaMin,
       "cucsEtherRxStatsUpdate": cucsEtherRxStatsUpdate,
       "cucsEtherRxStatsHistTable": cucsEtherRxStatsHistTable,
       "cucsEtherRxStatsHistEntry": cucsEtherRxStatsHistEntry,
       "cucsEtherRxStatsHistInstanceId": cucsEtherRxStatsHistInstanceId,
       "cucsEtherRxStatsHistDn": cucsEtherRxStatsHistDn,
       "cucsEtherRxStatsHistRn": cucsEtherRxStatsHistRn,
       "cucsEtherRxStatsHistBroadcastPackets": cucsEtherRxStatsHistBroadcastPackets,
       "cucsEtherRxStatsHistBroadcastPacketsDelta": cucsEtherRxStatsHistBroadcastPacketsDelta,
       "cucsEtherRxStatsHistBroadcastPacketsDeltaAvg": cucsEtherRxStatsHistBroadcastPacketsDeltaAvg,
       "cucsEtherRxStatsHistBroadcastPacketsDeltaMax": cucsEtherRxStatsHistBroadcastPacketsDeltaMax,
       "cucsEtherRxStatsHistBroadcastPacketsDeltaMin": cucsEtherRxStatsHistBroadcastPacketsDeltaMin,
       "cucsEtherRxStatsHistId": cucsEtherRxStatsHistId,
       "cucsEtherRxStatsHistJumboPackets": cucsEtherRxStatsHistJumboPackets,
       "cucsEtherRxStatsHistJumboPacketsDelta": cucsEtherRxStatsHistJumboPacketsDelta,
       "cucsEtherRxStatsHistJumboPacketsDeltaAvg": cucsEtherRxStatsHistJumboPacketsDeltaAvg,
       "cucsEtherRxStatsHistJumboPacketsDeltaMax": cucsEtherRxStatsHistJumboPacketsDeltaMax,
       "cucsEtherRxStatsHistJumboPacketsDeltaMin": cucsEtherRxStatsHistJumboPacketsDeltaMin,
       "cucsEtherRxStatsHistMostRecent": cucsEtherRxStatsHistMostRecent,
       "cucsEtherRxStatsHistMulticastPackets": cucsEtherRxStatsHistMulticastPackets,
       "cucsEtherRxStatsHistMulticastPacketsDelta": cucsEtherRxStatsHistMulticastPacketsDelta,
       "cucsEtherRxStatsHistMulticastPacketsDeltaAvg": cucsEtherRxStatsHistMulticastPacketsDeltaAvg,
       "cucsEtherRxStatsHistMulticastPacketsDeltaMax": cucsEtherRxStatsHistMulticastPacketsDeltaMax,
       "cucsEtherRxStatsHistMulticastPacketsDeltaMin": cucsEtherRxStatsHistMulticastPacketsDeltaMin,
       "cucsEtherRxStatsHistSuspect": cucsEtherRxStatsHistSuspect,
       "cucsEtherRxStatsHistThresholded": cucsEtherRxStatsHistThresholded,
       "cucsEtherRxStatsHistTimeCollected": cucsEtherRxStatsHistTimeCollected,
       "cucsEtherRxStatsHistTotalBytes": cucsEtherRxStatsHistTotalBytes,
       "cucsEtherRxStatsHistTotalBytesDelta": cucsEtherRxStatsHistTotalBytesDelta,
       "cucsEtherRxStatsHistTotalBytesDeltaAvg": cucsEtherRxStatsHistTotalBytesDeltaAvg,
       "cucsEtherRxStatsHistTotalBytesDeltaMax": cucsEtherRxStatsHistTotalBytesDeltaMax,
       "cucsEtherRxStatsHistTotalBytesDeltaMin": cucsEtherRxStatsHistTotalBytesDeltaMin,
       "cucsEtherRxStatsHistTotalPackets": cucsEtherRxStatsHistTotalPackets,
       "cucsEtherRxStatsHistTotalPacketsDelta": cucsEtherRxStatsHistTotalPacketsDelta,
       "cucsEtherRxStatsHistTotalPacketsDeltaAvg": cucsEtherRxStatsHistTotalPacketsDeltaAvg,
       "cucsEtherRxStatsHistTotalPacketsDeltaMax": cucsEtherRxStatsHistTotalPacketsDeltaMax,
       "cucsEtherRxStatsHistTotalPacketsDeltaMin": cucsEtherRxStatsHistTotalPacketsDeltaMin,
       "cucsEtherRxStatsHistUnicastPackets": cucsEtherRxStatsHistUnicastPackets,
       "cucsEtherRxStatsHistUnicastPacketsDelta": cucsEtherRxStatsHistUnicastPacketsDelta,
       "cucsEtherRxStatsHistUnicastPacketsDeltaAvg": cucsEtherRxStatsHistUnicastPacketsDeltaAvg,
       "cucsEtherRxStatsHistUnicastPacketsDeltaMax": cucsEtherRxStatsHistUnicastPacketsDeltaMax,
       "cucsEtherRxStatsHistUnicastPacketsDeltaMin": cucsEtherRxStatsHistUnicastPacketsDeltaMin,
       "cucsEtherServerIntFIoTable": cucsEtherServerIntFIoTable,
       "cucsEtherServerIntFIoEntry": cucsEtherServerIntFIoEntry,
       "cucsEtherServerIntFIoInstanceId": cucsEtherServerIntFIoInstanceId,
       "cucsEtherServerIntFIoDn": cucsEtherServerIntFIoDn,
       "cucsEtherServerIntFIoRn": cucsEtherServerIntFIoRn,
       "cucsEtherServerIntFIoAdminState": cucsEtherServerIntFIoAdminState,
       "cucsEtherServerIntFIoChassisId": cucsEtherServerIntFIoChassisId,
       "cucsEtherServerIntFIoEncap": cucsEtherServerIntFIoEncap,
       "cucsEtherServerIntFIoEpDn": cucsEtherServerIntFIoEpDn,
       "cucsEtherServerIntFIoFltAggr": cucsEtherServerIntFIoFltAggr,
       "cucsEtherServerIntFIoIfRole": cucsEtherServerIntFIoIfRole,
       "cucsEtherServerIntFIoIfType": cucsEtherServerIntFIoIfType,
       "cucsEtherServerIntFIoLocale": cucsEtherServerIntFIoLocale,
       "cucsEtherServerIntFIoMode": cucsEtherServerIntFIoMode,
       "cucsEtherServerIntFIoModel": cucsEtherServerIntFIoModel,
       "cucsEtherServerIntFIoName": cucsEtherServerIntFIoName,
       "cucsEtherServerIntFIoOperBorderPortId": cucsEtherServerIntFIoOperBorderPortId,
       "cucsEtherServerIntFIoOperBorderSlotId": cucsEtherServerIntFIoOperBorderSlotId,
       "cucsEtherServerIntFIoOperState": cucsEtherServerIntFIoOperState,
       "cucsEtherServerIntFIoPeerDn": cucsEtherServerIntFIoPeerDn,
       "cucsEtherServerIntFIoPeerPortId": cucsEtherServerIntFIoPeerPortId,
       "cucsEtherServerIntFIoPeerSlotId": cucsEtherServerIntFIoPeerSlotId,
       "cucsEtherServerIntFIoPortId": cucsEtherServerIntFIoPortId,
       "cucsEtherServerIntFIoRevision": cucsEtherServerIntFIoRevision,
       "cucsEtherServerIntFIoSerial": cucsEtherServerIntFIoSerial,
       "cucsEtherServerIntFIoSlotId": cucsEtherServerIntFIoSlotId,
       "cucsEtherServerIntFIoStateQual": cucsEtherServerIntFIoStateQual,
       "cucsEtherServerIntFIoSwitchId": cucsEtherServerIntFIoSwitchId,
       "cucsEtherServerIntFIoTransport": cucsEtherServerIntFIoTransport,
       "cucsEtherServerIntFIoTs": cucsEtherServerIntFIoTs,
       "cucsEtherServerIntFIoType": cucsEtherServerIntFIoType,
       "cucsEtherServerIntFIoVendor": cucsEtherServerIntFIoVendor,
       "cucsEtherServerIntFIoMac": cucsEtherServerIntFIoMac,
       "cucsEtherServerIntFIoPeerChassisId": cucsEtherServerIntFIoPeerChassisId,
       "cucsEtherServerIntFIoXcvrType": cucsEtherServerIntFIoXcvrType,
       "cucsEtherServerIntFIoAdminSpeed": cucsEtherServerIntFIoAdminSpeed,
       "cucsEtherServerIntFIoFsmDescr": cucsEtherServerIntFIoFsmDescr,
       "cucsEtherServerIntFIoFsmPrev": cucsEtherServerIntFIoFsmPrev,
       "cucsEtherServerIntFIoFsmProgr": cucsEtherServerIntFIoFsmProgr,
       "cucsEtherServerIntFIoFsmRmtInvErrCode": cucsEtherServerIntFIoFsmRmtInvErrCode,
       "cucsEtherServerIntFIoFsmRmtInvErrDescr": cucsEtherServerIntFIoFsmRmtInvErrDescr,
       "cucsEtherServerIntFIoFsmRmtInvRslt": cucsEtherServerIntFIoFsmRmtInvRslt,
       "cucsEtherServerIntFIoFsmStageDescr": cucsEtherServerIntFIoFsmStageDescr,
       "cucsEtherServerIntFIoFsmStamp": cucsEtherServerIntFIoFsmStamp,
       "cucsEtherServerIntFIoFsmStatus": cucsEtherServerIntFIoFsmStatus,
       "cucsEtherServerIntFIoFsmTry": cucsEtherServerIntFIoFsmTry,
       "cucsEtherServerIntFIoNsSize": cucsEtherServerIntFIoNsSize,
       "cucsEtherServerIntFIoPeerEncap": cucsEtherServerIntFIoPeerEncap,
       "cucsEtherServerIntFIoAggrPortId": cucsEtherServerIntFIoAggrPortId,
       "cucsEtherServerIntFIoPeerAggrPortId": cucsEtherServerIntFIoPeerAggrPortId,
       "cucsEtherServerIntFIoMacAddr": cucsEtherServerIntFIoMacAddr,
       "cucsEtherServerIntFIoOperBorderAggrPortId": cucsEtherServerIntFIoOperBorderAggrPortId,
       "cucsEtherSwIfConfigTable": cucsEtherSwIfConfigTable,
       "cucsEtherSwIfConfigEntry": cucsEtherSwIfConfigEntry,
       "cucsEtherSwIfConfigInstanceId": cucsEtherSwIfConfigInstanceId,
       "cucsEtherSwIfConfigDn": cucsEtherSwIfConfigDn,
       "cucsEtherSwIfConfigRn": cucsEtherSwIfConfigRn,
       "cucsEtherSwitchIntFIoTable": cucsEtherSwitchIntFIoTable,
       "cucsEtherSwitchIntFIoEntry": cucsEtherSwitchIntFIoEntry,
       "cucsEtherSwitchIntFIoInstanceId": cucsEtherSwitchIntFIoInstanceId,
       "cucsEtherSwitchIntFIoDn": cucsEtherSwitchIntFIoDn,
       "cucsEtherSwitchIntFIoRn": cucsEtherSwitchIntFIoRn,
       "cucsEtherSwitchIntFIoAck": cucsEtherSwitchIntFIoAck,
       "cucsEtherSwitchIntFIoAdminState": cucsEtherSwitchIntFIoAdminState,
       "cucsEtherSwitchIntFIoChassisId": cucsEtherSwitchIntFIoChassisId,
       "cucsEtherSwitchIntFIoDiscovery": cucsEtherSwitchIntFIoDiscovery,
       "cucsEtherSwitchIntFIoEncap": cucsEtherSwitchIntFIoEncap,
       "cucsEtherSwitchIntFIoEpDn": cucsEtherSwitchIntFIoEpDn,
       "cucsEtherSwitchIntFIoFltAggr": cucsEtherSwitchIntFIoFltAggr,
       "cucsEtherSwitchIntFIoIfRole": cucsEtherSwitchIntFIoIfRole,
       "cucsEtherSwitchIntFIoIfType": cucsEtherSwitchIntFIoIfType,
       "cucsEtherSwitchIntFIoLocale": cucsEtherSwitchIntFIoLocale,
       "cucsEtherSwitchIntFIoMode": cucsEtherSwitchIntFIoMode,
       "cucsEtherSwitchIntFIoModel": cucsEtherSwitchIntFIoModel,
       "cucsEtherSwitchIntFIoName": cucsEtherSwitchIntFIoName,
       "cucsEtherSwitchIntFIoOperState": cucsEtherSwitchIntFIoOperState,
       "cucsEtherSwitchIntFIoPeerDn": cucsEtherSwitchIntFIoPeerDn,
       "cucsEtherSwitchIntFIoPeerPortId": cucsEtherSwitchIntFIoPeerPortId,
       "cucsEtherSwitchIntFIoPeerSlotId": cucsEtherSwitchIntFIoPeerSlotId,
       "cucsEtherSwitchIntFIoPortId": cucsEtherSwitchIntFIoPortId,
       "cucsEtherSwitchIntFIoRevision": cucsEtherSwitchIntFIoRevision,
       "cucsEtherSwitchIntFIoSerial": cucsEtherSwitchIntFIoSerial,
       "cucsEtherSwitchIntFIoSlotId": cucsEtherSwitchIntFIoSlotId,
       "cucsEtherSwitchIntFIoStateQual": cucsEtherSwitchIntFIoStateQual,
       "cucsEtherSwitchIntFIoSwitchId": cucsEtherSwitchIntFIoSwitchId,
       "cucsEtherSwitchIntFIoTransport": cucsEtherSwitchIntFIoTransport,
       "cucsEtherSwitchIntFIoTs": cucsEtherSwitchIntFIoTs,
       "cucsEtherSwitchIntFIoType": cucsEtherSwitchIntFIoType,
       "cucsEtherSwitchIntFIoVendor": cucsEtherSwitchIntFIoVendor,
       "cucsEtherSwitchIntFIoPeerChassisId": cucsEtherSwitchIntFIoPeerChassisId,
       "cucsEtherSwitchIntFIoXcvrType": cucsEtherSwitchIntFIoXcvrType,
       "cucsEtherSwitchIntFIoDelFeTs": cucsEtherSwitchIntFIoDelFeTs,
       "cucsEtherSwitchIntFIoNewFeTs": cucsEtherSwitchIntFIoNewFeTs,
       "cucsEtherSwitchIntFIoAggrPortId": cucsEtherSwitchIntFIoAggrPortId,
       "cucsEtherSwitchIntFIoPeerAggrPortId": cucsEtherSwitchIntFIoPeerAggrPortId,
       "cucsEtherSwitchIntFIoMacAddr": cucsEtherSwitchIntFIoMacAddr,
       "cucsEtherTxStatsTable": cucsEtherTxStatsTable,
       "cucsEtherTxStatsEntry": cucsEtherTxStatsEntry,
       "cucsEtherTxStatsInstanceId": cucsEtherTxStatsInstanceId,
       "cucsEtherTxStatsDn": cucsEtherTxStatsDn,
       "cucsEtherTxStatsRn": cucsEtherTxStatsRn,
       "cucsEtherTxStatsBroadcastPackets": cucsEtherTxStatsBroadcastPackets,
       "cucsEtherTxStatsBroadcastPacketsDelta": cucsEtherTxStatsBroadcastPacketsDelta,
       "cucsEtherTxStatsBroadcastPacketsDeltaAvg": cucsEtherTxStatsBroadcastPacketsDeltaAvg,
       "cucsEtherTxStatsBroadcastPacketsDeltaMax": cucsEtherTxStatsBroadcastPacketsDeltaMax,
       "cucsEtherTxStatsBroadcastPacketsDeltaMin": cucsEtherTxStatsBroadcastPacketsDeltaMin,
       "cucsEtherTxStatsIntervals": cucsEtherTxStatsIntervals,
       "cucsEtherTxStatsJumboPackets": cucsEtherTxStatsJumboPackets,
       "cucsEtherTxStatsJumboPacketsDelta": cucsEtherTxStatsJumboPacketsDelta,
       "cucsEtherTxStatsJumboPacketsDeltaAvg": cucsEtherTxStatsJumboPacketsDeltaAvg,
       "cucsEtherTxStatsJumboPacketsDeltaMax": cucsEtherTxStatsJumboPacketsDeltaMax,
       "cucsEtherTxStatsJumboPacketsDeltaMin": cucsEtherTxStatsJumboPacketsDeltaMin,
       "cucsEtherTxStatsMulticastPackets": cucsEtherTxStatsMulticastPackets,
       "cucsEtherTxStatsMulticastPacketsDelta": cucsEtherTxStatsMulticastPacketsDelta,
       "cucsEtherTxStatsMulticastPacketsDeltaAvg": cucsEtherTxStatsMulticastPacketsDeltaAvg,
       "cucsEtherTxStatsMulticastPacketsDeltaMax": cucsEtherTxStatsMulticastPacketsDeltaMax,
       "cucsEtherTxStatsMulticastPacketsDeltaMin": cucsEtherTxStatsMulticastPacketsDeltaMin,
       "cucsEtherTxStatsSuspect": cucsEtherTxStatsSuspect,
       "cucsEtherTxStatsThresholded": cucsEtherTxStatsThresholded,
       "cucsEtherTxStatsTimeCollected": cucsEtherTxStatsTimeCollected,
       "cucsEtherTxStatsTotalBytes": cucsEtherTxStatsTotalBytes,
       "cucsEtherTxStatsTotalBytesDelta": cucsEtherTxStatsTotalBytesDelta,
       "cucsEtherTxStatsTotalBytesDeltaAvg": cucsEtherTxStatsTotalBytesDeltaAvg,
       "cucsEtherTxStatsTotalBytesDeltaMax": cucsEtherTxStatsTotalBytesDeltaMax,
       "cucsEtherTxStatsTotalBytesDeltaMin": cucsEtherTxStatsTotalBytesDeltaMin,
       "cucsEtherTxStatsTotalPackets": cucsEtherTxStatsTotalPackets,
       "cucsEtherTxStatsTotalPacketsDelta": cucsEtherTxStatsTotalPacketsDelta,
       "cucsEtherTxStatsTotalPacketsDeltaAvg": cucsEtherTxStatsTotalPacketsDeltaAvg,
       "cucsEtherTxStatsTotalPacketsDeltaMax": cucsEtherTxStatsTotalPacketsDeltaMax,
       "cucsEtherTxStatsTotalPacketsDeltaMin": cucsEtherTxStatsTotalPacketsDeltaMin,
       "cucsEtherTxStatsUnicastPackets": cucsEtherTxStatsUnicastPackets,
       "cucsEtherTxStatsUnicastPacketsDelta": cucsEtherTxStatsUnicastPacketsDelta,
       "cucsEtherTxStatsUnicastPacketsDeltaAvg": cucsEtherTxStatsUnicastPacketsDeltaAvg,
       "cucsEtherTxStatsUnicastPacketsDeltaMax": cucsEtherTxStatsUnicastPacketsDeltaMax,
       "cucsEtherTxStatsUnicastPacketsDeltaMin": cucsEtherTxStatsUnicastPacketsDeltaMin,
       "cucsEtherTxStatsUpdate": cucsEtherTxStatsUpdate,
       "cucsEtherTxStatsHistTable": cucsEtherTxStatsHistTable,
       "cucsEtherTxStatsHistEntry": cucsEtherTxStatsHistEntry,
       "cucsEtherTxStatsHistInstanceId": cucsEtherTxStatsHistInstanceId,
       "cucsEtherTxStatsHistDn": cucsEtherTxStatsHistDn,
       "cucsEtherTxStatsHistRn": cucsEtherTxStatsHistRn,
       "cucsEtherTxStatsHistBroadcastPackets": cucsEtherTxStatsHistBroadcastPackets,
       "cucsEtherTxStatsHistBroadcastPacketsDelta": cucsEtherTxStatsHistBroadcastPacketsDelta,
       "cucsEtherTxStatsHistBroadcastPacketsDeltaAvg": cucsEtherTxStatsHistBroadcastPacketsDeltaAvg,
       "cucsEtherTxStatsHistBroadcastPacketsDeltaMax": cucsEtherTxStatsHistBroadcastPacketsDeltaMax,
       "cucsEtherTxStatsHistBroadcastPacketsDeltaMin": cucsEtherTxStatsHistBroadcastPacketsDeltaMin,
       "cucsEtherTxStatsHistId": cucsEtherTxStatsHistId,
       "cucsEtherTxStatsHistJumboPackets": cucsEtherTxStatsHistJumboPackets,
       "cucsEtherTxStatsHistJumboPacketsDelta": cucsEtherTxStatsHistJumboPacketsDelta,
       "cucsEtherTxStatsHistJumboPacketsDeltaAvg": cucsEtherTxStatsHistJumboPacketsDeltaAvg,
       "cucsEtherTxStatsHistJumboPacketsDeltaMax": cucsEtherTxStatsHistJumboPacketsDeltaMax,
       "cucsEtherTxStatsHistJumboPacketsDeltaMin": cucsEtherTxStatsHistJumboPacketsDeltaMin,
       "cucsEtherTxStatsHistMostRecent": cucsEtherTxStatsHistMostRecent,
       "cucsEtherTxStatsHistMulticastPackets": cucsEtherTxStatsHistMulticastPackets,
       "cucsEtherTxStatsHistMulticastPacketsDelta": cucsEtherTxStatsHistMulticastPacketsDelta,
       "cucsEtherTxStatsHistMulticastPacketsDeltaAvg": cucsEtherTxStatsHistMulticastPacketsDeltaAvg,
       "cucsEtherTxStatsHistMulticastPacketsDeltaMax": cucsEtherTxStatsHistMulticastPacketsDeltaMax,
       "cucsEtherTxStatsHistMulticastPacketsDeltaMin": cucsEtherTxStatsHistMulticastPacketsDeltaMin,
       "cucsEtherTxStatsHistSuspect": cucsEtherTxStatsHistSuspect,
       "cucsEtherTxStatsHistThresholded": cucsEtherTxStatsHistThresholded,
       "cucsEtherTxStatsHistTimeCollected": cucsEtherTxStatsHistTimeCollected,
       "cucsEtherTxStatsHistTotalBytes": cucsEtherTxStatsHistTotalBytes,
       "cucsEtherTxStatsHistTotalBytesDelta": cucsEtherTxStatsHistTotalBytesDelta,
       "cucsEtherTxStatsHistTotalBytesDeltaAvg": cucsEtherTxStatsHistTotalBytesDeltaAvg,
       "cucsEtherTxStatsHistTotalBytesDeltaMax": cucsEtherTxStatsHistTotalBytesDeltaMax,
       "cucsEtherTxStatsHistTotalBytesDeltaMin": cucsEtherTxStatsHistTotalBytesDeltaMin,
       "cucsEtherTxStatsHistTotalPackets": cucsEtherTxStatsHistTotalPackets,
       "cucsEtherTxStatsHistTotalPacketsDelta": cucsEtherTxStatsHistTotalPacketsDelta,
       "cucsEtherTxStatsHistTotalPacketsDeltaAvg": cucsEtherTxStatsHistTotalPacketsDeltaAvg,
       "cucsEtherTxStatsHistTotalPacketsDeltaMax": cucsEtherTxStatsHistTotalPacketsDeltaMax,
       "cucsEtherTxStatsHistTotalPacketsDeltaMin": cucsEtherTxStatsHistTotalPacketsDeltaMin,
       "cucsEtherTxStatsHistUnicastPackets": cucsEtherTxStatsHistUnicastPackets,
       "cucsEtherTxStatsHistUnicastPacketsDelta": cucsEtherTxStatsHistUnicastPacketsDelta,
       "cucsEtherTxStatsHistUnicastPacketsDeltaAvg": cucsEtherTxStatsHistUnicastPacketsDeltaAvg,
       "cucsEtherTxStatsHistUnicastPacketsDeltaMax": cucsEtherTxStatsHistUnicastPacketsDeltaMax,
       "cucsEtherTxStatsHistUnicastPacketsDeltaMin": cucsEtherTxStatsHistUnicastPacketsDeltaMin,
       "cucsEtherPortChanIdElemTable": cucsEtherPortChanIdElemTable,
       "cucsEtherPortChanIdElemEntry": cucsEtherPortChanIdElemEntry,
       "cucsEtherPortChanIdElemInstanceId": cucsEtherPortChanIdElemInstanceId,
       "cucsEtherPortChanIdElemDn": cucsEtherPortChanIdElemDn,
       "cucsEtherPortChanIdElemRn": cucsEtherPortChanIdElemRn,
       "cucsEtherPortChanIdElemId": cucsEtherPortChanIdElemId,
       "cucsEtherPortChanIdElemAssignedToDn": cucsEtherPortChanIdElemAssignedToDn,
       "cucsEtherPortChanIdElemPrevAssignedToDn": cucsEtherPortChanIdElemPrevAssignedToDn,
       "cucsEtherPortChanIdUniverseTable": cucsEtherPortChanIdUniverseTable,
       "cucsEtherPortChanIdUniverseEntry": cucsEtherPortChanIdUniverseEntry,
       "cucsEtherPortChanIdUniverseInstanceId": cucsEtherPortChanIdUniverseInstanceId,
       "cucsEtherPortChanIdUniverseDn": cucsEtherPortChanIdUniverseDn,
       "cucsEtherPortChanIdUniverseRn": cucsEtherPortChanIdUniverseRn,
       "cucsEtherServerIntFIoPcTable": cucsEtherServerIntFIoPcTable,
       "cucsEtherServerIntFIoPcEntry": cucsEtherServerIntFIoPcEntry,
       "cucsEtherServerIntFIoPcInstanceId": cucsEtherServerIntFIoPcInstanceId,
       "cucsEtherServerIntFIoPcDn": cucsEtherServerIntFIoPcDn,
       "cucsEtherServerIntFIoPcRn": cucsEtherServerIntFIoPcRn,
       "cucsEtherServerIntFIoPcChassisId": cucsEtherServerIntFIoPcChassisId,
       "cucsEtherServerIntFIoPcEpDn": cucsEtherServerIntFIoPcEpDn,
       "cucsEtherServerIntFIoPcFltAggr": cucsEtherServerIntFIoPcFltAggr,
       "cucsEtherServerIntFIoPcIfRole": cucsEtherServerIntFIoPcIfRole,
       "cucsEtherServerIntFIoPcIfType": cucsEtherServerIntFIoPcIfType,
       "cucsEtherServerIntFIoPcLocale": cucsEtherServerIntFIoPcLocale,
       "cucsEtherServerIntFIoPcName": cucsEtherServerIntFIoPcName,
       "cucsEtherServerIntFIoPcOperSpeed": cucsEtherServerIntFIoPcOperSpeed,
       "cucsEtherServerIntFIoPcOperState": cucsEtherServerIntFIoPcOperState,
       "cucsEtherServerIntFIoPcPeerDn": cucsEtherServerIntFIoPcPeerDn,
       "cucsEtherServerIntFIoPcPortId": cucsEtherServerIntFIoPcPortId,
       "cucsEtherServerIntFIoPcStateQual": cucsEtherServerIntFIoPcStateQual,
       "cucsEtherServerIntFIoPcSwitchId": cucsEtherServerIntFIoPcSwitchId,
       "cucsEtherServerIntFIoPcTransport": cucsEtherServerIntFIoPcTransport,
       "cucsEtherServerIntFIoPcType": cucsEtherServerIntFIoPcType,
       "cucsEtherServerIntFIoPcEpTable": cucsEtherServerIntFIoPcEpTable,
       "cucsEtherServerIntFIoPcEpEntry": cucsEtherServerIntFIoPcEpEntry,
       "cucsEtherServerIntFIoPcEpInstanceId": cucsEtherServerIntFIoPcEpInstanceId,
       "cucsEtherServerIntFIoPcEpDnData": cucsEtherServerIntFIoPcEpDnData,
       "cucsEtherServerIntFIoPcEpRn": cucsEtherServerIntFIoPcEpRn,
       "cucsEtherServerIntFIoPcEpAdminState": cucsEtherServerIntFIoPcEpAdminState,
       "cucsEtherServerIntFIoPcEpChassisId": cucsEtherServerIntFIoPcEpChassisId,
       "cucsEtherServerIntFIoPcEpEpDn": cucsEtherServerIntFIoPcEpEpDn,
       "cucsEtherServerIntFIoPcEpIfRole": cucsEtherServerIntFIoPcEpIfRole,
       "cucsEtherServerIntFIoPcEpIfType": cucsEtherServerIntFIoPcEpIfType,
       "cucsEtherServerIntFIoPcEpLocale": cucsEtherServerIntFIoPcEpLocale,
       "cucsEtherServerIntFIoPcEpMembership": cucsEtherServerIntFIoPcEpMembership,
       "cucsEtherServerIntFIoPcEpName": cucsEtherServerIntFIoPcEpName,
       "cucsEtherServerIntFIoPcEpPeerChassisId": cucsEtherServerIntFIoPcEpPeerChassisId,
       "cucsEtherServerIntFIoPcEpPeerDn": cucsEtherServerIntFIoPcEpPeerDn,
       "cucsEtherServerIntFIoPcEpPeerPortId": cucsEtherServerIntFIoPcEpPeerPortId,
       "cucsEtherServerIntFIoPcEpPeerSlotId": cucsEtherServerIntFIoPcEpPeerSlotId,
       "cucsEtherServerIntFIoPcEpPortId": cucsEtherServerIntFIoPcEpPortId,
       "cucsEtherServerIntFIoPcEpSlotId": cucsEtherServerIntFIoPcEpSlotId,
       "cucsEtherServerIntFIoPcEpSwitchId": cucsEtherServerIntFIoPcEpSwitchId,
       "cucsEtherServerIntFIoPcEpTransport": cucsEtherServerIntFIoPcEpTransport,
       "cucsEtherServerIntFIoPcEpType": cucsEtherServerIntFIoPcEpType,
       "cucsEtherServerIntFIoPcEpAggrPortId": cucsEtherServerIntFIoPcEpAggrPortId,
       "cucsEtherServerIntFIoPcEpPeerAggrPortId": cucsEtherServerIntFIoPcEpPeerAggrPortId,
       "cucsEtherSwitchIntFIoPcTable": cucsEtherSwitchIntFIoPcTable,
       "cucsEtherSwitchIntFIoPcEntry": cucsEtherSwitchIntFIoPcEntry,
       "cucsEtherSwitchIntFIoPcInstanceId": cucsEtherSwitchIntFIoPcInstanceId,
       "cucsEtherSwitchIntFIoPcDn": cucsEtherSwitchIntFIoPcDn,
       "cucsEtherSwitchIntFIoPcRn": cucsEtherSwitchIntFIoPcRn,
       "cucsEtherSwitchIntFIoPcAdminState": cucsEtherSwitchIntFIoPcAdminState,
       "cucsEtherSwitchIntFIoPcChassisId": cucsEtherSwitchIntFIoPcChassisId,
       "cucsEtherSwitchIntFIoPcEpDn": cucsEtherSwitchIntFIoPcEpDn,
       "cucsEtherSwitchIntFIoPcFltAggr": cucsEtherSwitchIntFIoPcFltAggr,
       "cucsEtherSwitchIntFIoPcIfRole": cucsEtherSwitchIntFIoPcIfRole,
       "cucsEtherSwitchIntFIoPcIfType": cucsEtherSwitchIntFIoPcIfType,
       "cucsEtherSwitchIntFIoPcLocale": cucsEtherSwitchIntFIoPcLocale,
       "cucsEtherSwitchIntFIoPcName": cucsEtherSwitchIntFIoPcName,
       "cucsEtherSwitchIntFIoPcOperSpeed": cucsEtherSwitchIntFIoPcOperSpeed,
       "cucsEtherSwitchIntFIoPcOperState": cucsEtherSwitchIntFIoPcOperState,
       "cucsEtherSwitchIntFIoPcPeerDn": cucsEtherSwitchIntFIoPcPeerDn,
       "cucsEtherSwitchIntFIoPcPortId": cucsEtherSwitchIntFIoPcPortId,
       "cucsEtherSwitchIntFIoPcStateQual": cucsEtherSwitchIntFIoPcStateQual,
       "cucsEtherSwitchIntFIoPcSwitchId": cucsEtherSwitchIntFIoPcSwitchId,
       "cucsEtherSwitchIntFIoPcTransport": cucsEtherSwitchIntFIoPcTransport,
       "cucsEtherSwitchIntFIoPcType": cucsEtherSwitchIntFIoPcType,
       "cucsEtherSwitchIntFIoPcMulticastHwHash": cucsEtherSwitchIntFIoPcMulticastHwHash,
       "cucsEtherSwitchIntFIoPcEpTable": cucsEtherSwitchIntFIoPcEpTable,
       "cucsEtherSwitchIntFIoPcEpEntry": cucsEtherSwitchIntFIoPcEpEntry,
       "cucsEtherSwitchIntFIoPcEpInstanceId": cucsEtherSwitchIntFIoPcEpInstanceId,
       "cucsEtherSwitchIntFIoPcEpDnData": cucsEtherSwitchIntFIoPcEpDnData,
       "cucsEtherSwitchIntFIoPcEpRn": cucsEtherSwitchIntFIoPcEpRn,
       "cucsEtherSwitchIntFIoPcEpAdminState": cucsEtherSwitchIntFIoPcEpAdminState,
       "cucsEtherSwitchIntFIoPcEpChassisId": cucsEtherSwitchIntFIoPcEpChassisId,
       "cucsEtherSwitchIntFIoPcEpEpDn": cucsEtherSwitchIntFIoPcEpEpDn,
       "cucsEtherSwitchIntFIoPcEpIfRole": cucsEtherSwitchIntFIoPcEpIfRole,
       "cucsEtherSwitchIntFIoPcEpIfType": cucsEtherSwitchIntFIoPcEpIfType,
       "cucsEtherSwitchIntFIoPcEpLocale": cucsEtherSwitchIntFIoPcEpLocale,
       "cucsEtherSwitchIntFIoPcEpMembership": cucsEtherSwitchIntFIoPcEpMembership,
       "cucsEtherSwitchIntFIoPcEpName": cucsEtherSwitchIntFIoPcEpName,
       "cucsEtherSwitchIntFIoPcEpPeerChassisId": cucsEtherSwitchIntFIoPcEpPeerChassisId,
       "cucsEtherSwitchIntFIoPcEpPeerDn": cucsEtherSwitchIntFIoPcEpPeerDn,
       "cucsEtherSwitchIntFIoPcEpPeerPortId": cucsEtherSwitchIntFIoPcEpPeerPortId,
       "cucsEtherSwitchIntFIoPcEpPeerSlotId": cucsEtherSwitchIntFIoPcEpPeerSlotId,
       "cucsEtherSwitchIntFIoPcEpPortId": cucsEtherSwitchIntFIoPcEpPortId,
       "cucsEtherSwitchIntFIoPcEpSlotId": cucsEtherSwitchIntFIoPcEpSlotId,
       "cucsEtherSwitchIntFIoPcEpStatusChangeTs": cucsEtherSwitchIntFIoPcEpStatusChangeTs,
       "cucsEtherSwitchIntFIoPcEpSwitchId": cucsEtherSwitchIntFIoPcEpSwitchId,
       "cucsEtherSwitchIntFIoPcEpTransport": cucsEtherSwitchIntFIoPcEpTransport,
       "cucsEtherSwitchIntFIoPcEpType": cucsEtherSwitchIntFIoPcEpType,
       "cucsEtherSwitchIntFIoPcEpAckState": cucsEtherSwitchIntFIoPcEpAckState,
       "cucsEtherSwitchIntFIoPcEpAggrPortId": cucsEtherSwitchIntFIoPcEpAggrPortId,
       "cucsEtherSwitchIntFIoPcEpPeerAggrPortId": cucsEtherSwitchIntFIoPcEpPeerAggrPortId,
       "cucsEtherServerIntFIoFsmTaskTable": cucsEtherServerIntFIoFsmTaskTable,
       "cucsEtherServerIntFIoFsmTaskEntry": cucsEtherServerIntFIoFsmTaskEntry,
       "cucsEtherServerIntFIoFsmTaskInstanceId": cucsEtherServerIntFIoFsmTaskInstanceId,
       "cucsEtherServerIntFIoFsmTaskDn": cucsEtherServerIntFIoFsmTaskDn,
       "cucsEtherServerIntFIoFsmTaskRn": cucsEtherServerIntFIoFsmTaskRn,
       "cucsEtherServerIntFIoFsmTaskCompletion": cucsEtherServerIntFIoFsmTaskCompletion,
       "cucsEtherServerIntFIoFsmTaskFlags": cucsEtherServerIntFIoFsmTaskFlags,
       "cucsEtherServerIntFIoFsmTaskItem": cucsEtherServerIntFIoFsmTaskItem,
       "cucsEtherServerIntFIoFsmTaskSeqId": cucsEtherServerIntFIoFsmTaskSeqId,
       "cucsEtherFcoeInterfaceStatsTable": cucsEtherFcoeInterfaceStatsTable,
       "cucsEtherFcoeInterfaceStatsEntry": cucsEtherFcoeInterfaceStatsEntry,
       "cucsEtherFcoeInterfaceStatsInstanceId": cucsEtherFcoeInterfaceStatsInstanceId,
       "cucsEtherFcoeInterfaceStatsDn": cucsEtherFcoeInterfaceStatsDn,
       "cucsEtherFcoeInterfaceStatsRn": cucsEtherFcoeInterfaceStatsRn,
       "cucsEtherFcoeInterfaceStatsBytesRx": cucsEtherFcoeInterfaceStatsBytesRx,
       "cucsEtherFcoeInterfaceStatsBytesRxDelta": cucsEtherFcoeInterfaceStatsBytesRxDelta,
       "cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg": cucsEtherFcoeInterfaceStatsBytesRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsBytesRxDeltaMax": cucsEtherFcoeInterfaceStatsBytesRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsBytesRxDeltaMin": cucsEtherFcoeInterfaceStatsBytesRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsBytesTx": cucsEtherFcoeInterfaceStatsBytesTx,
       "cucsEtherFcoeInterfaceStatsBytesTxDelta": cucsEtherFcoeInterfaceStatsBytesTxDelta,
       "cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg": cucsEtherFcoeInterfaceStatsBytesTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsBytesTxDeltaMax": cucsEtherFcoeInterfaceStatsBytesTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsBytesTxDeltaMin": cucsEtherFcoeInterfaceStatsBytesTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsDroppedRx": cucsEtherFcoeInterfaceStatsDroppedRx,
       "cucsEtherFcoeInterfaceStatsDroppedRxDelta": cucsEtherFcoeInterfaceStatsDroppedRxDelta,
       "cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg": cucsEtherFcoeInterfaceStatsDroppedRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax": cucsEtherFcoeInterfaceStatsDroppedRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin": cucsEtherFcoeInterfaceStatsDroppedRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsDroppedTx": cucsEtherFcoeInterfaceStatsDroppedTx,
       "cucsEtherFcoeInterfaceStatsDroppedTxDelta": cucsEtherFcoeInterfaceStatsDroppedTxDelta,
       "cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg": cucsEtherFcoeInterfaceStatsDroppedTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax": cucsEtherFcoeInterfaceStatsDroppedTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin": cucsEtherFcoeInterfaceStatsDroppedTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsErrorsRx": cucsEtherFcoeInterfaceStatsErrorsRx,
       "cucsEtherFcoeInterfaceStatsErrorsRxDelta": cucsEtherFcoeInterfaceStatsErrorsRxDelta,
       "cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg": cucsEtherFcoeInterfaceStatsErrorsRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax": cucsEtherFcoeInterfaceStatsErrorsRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin": cucsEtherFcoeInterfaceStatsErrorsRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsErrorsTx": cucsEtherFcoeInterfaceStatsErrorsTx,
       "cucsEtherFcoeInterfaceStatsErrorsTxDelta": cucsEtherFcoeInterfaceStatsErrorsTxDelta,
       "cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg": cucsEtherFcoeInterfaceStatsErrorsTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax": cucsEtherFcoeInterfaceStatsErrorsTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin": cucsEtherFcoeInterfaceStatsErrorsTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsIntervals": cucsEtherFcoeInterfaceStatsIntervals,
       "cucsEtherFcoeInterfaceStatsPacketsRx": cucsEtherFcoeInterfaceStatsPacketsRx,
       "cucsEtherFcoeInterfaceStatsPacketsRxDelta": cucsEtherFcoeInterfaceStatsPacketsRxDelta,
       "cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg": cucsEtherFcoeInterfaceStatsPacketsRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax": cucsEtherFcoeInterfaceStatsPacketsRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin": cucsEtherFcoeInterfaceStatsPacketsRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsPacketsTx": cucsEtherFcoeInterfaceStatsPacketsTx,
       "cucsEtherFcoeInterfaceStatsPacketsTxDelta": cucsEtherFcoeInterfaceStatsPacketsTxDelta,
       "cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg": cucsEtherFcoeInterfaceStatsPacketsTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax": cucsEtherFcoeInterfaceStatsPacketsTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin": cucsEtherFcoeInterfaceStatsPacketsTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsSuspect": cucsEtherFcoeInterfaceStatsSuspect,
       "cucsEtherFcoeInterfaceStatsThresholded": cucsEtherFcoeInterfaceStatsThresholded,
       "cucsEtherFcoeInterfaceStatsTimeCollected": cucsEtherFcoeInterfaceStatsTimeCollected,
       "cucsEtherFcoeInterfaceStatsUpdate": cucsEtherFcoeInterfaceStatsUpdate,
       "cucsEtherFcoeInterfaceStatsHistTable": cucsEtherFcoeInterfaceStatsHistTable,
       "cucsEtherFcoeInterfaceStatsHistEntry": cucsEtherFcoeInterfaceStatsHistEntry,
       "cucsEtherFcoeInterfaceStatsHistInstanceId": cucsEtherFcoeInterfaceStatsHistInstanceId,
       "cucsEtherFcoeInterfaceStatsHistDn": cucsEtherFcoeInterfaceStatsHistDn,
       "cucsEtherFcoeInterfaceStatsHistRn": cucsEtherFcoeInterfaceStatsHistRn,
       "cucsEtherFcoeInterfaceStatsHistBytesRx": cucsEtherFcoeInterfaceStatsHistBytesRx,
       "cucsEtherFcoeInterfaceStatsHistBytesRxDelta": cucsEtherFcoeInterfaceStatsHistBytesRxDelta,
       "cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg": cucsEtherFcoeInterfaceStatsHistBytesRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax": cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin": cucsEtherFcoeInterfaceStatsHistBytesRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistBytesTx": cucsEtherFcoeInterfaceStatsHistBytesTx,
       "cucsEtherFcoeInterfaceStatsHistBytesTxDelta": cucsEtherFcoeInterfaceStatsHistBytesTxDelta,
       "cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg": cucsEtherFcoeInterfaceStatsHistBytesTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax": cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin": cucsEtherFcoeInterfaceStatsHistBytesTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistDroppedRx": cucsEtherFcoeInterfaceStatsHistDroppedRx,
       "cucsEtherFcoeInterfaceStatsHistDroppedRxDelta": cucsEtherFcoeInterfaceStatsHistDroppedRxDelta,
       "cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg": cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax": cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin": cucsEtherFcoeInterfaceStatsHistDroppedRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistDroppedTx": cucsEtherFcoeInterfaceStatsHistDroppedTx,
       "cucsEtherFcoeInterfaceStatsHistDroppedTxDelta": cucsEtherFcoeInterfaceStatsHistDroppedTxDelta,
       "cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg": cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax": cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin": cucsEtherFcoeInterfaceStatsHistDroppedTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistErrorsRx": cucsEtherFcoeInterfaceStatsHistErrorsRx,
       "cucsEtherFcoeInterfaceStatsHistErrorsRxDelta": cucsEtherFcoeInterfaceStatsHistErrorsRxDelta,
       "cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg": cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax": cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin": cucsEtherFcoeInterfaceStatsHistErrorsRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistErrorsTx": cucsEtherFcoeInterfaceStatsHistErrorsTx,
       "cucsEtherFcoeInterfaceStatsHistErrorsTxDelta": cucsEtherFcoeInterfaceStatsHistErrorsTxDelta,
       "cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg": cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax": cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin": cucsEtherFcoeInterfaceStatsHistErrorsTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistId": cucsEtherFcoeInterfaceStatsHistId,
       "cucsEtherFcoeInterfaceStatsHistMostRecent": cucsEtherFcoeInterfaceStatsHistMostRecent,
       "cucsEtherFcoeInterfaceStatsHistPacketsRx": cucsEtherFcoeInterfaceStatsHistPacketsRx,
       "cucsEtherFcoeInterfaceStatsHistPacketsRxDelta": cucsEtherFcoeInterfaceStatsHistPacketsRxDelta,
       "cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg": cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax": cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin": cucsEtherFcoeInterfaceStatsHistPacketsRxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistPacketsTx": cucsEtherFcoeInterfaceStatsHistPacketsTx,
       "cucsEtherFcoeInterfaceStatsHistPacketsTxDelta": cucsEtherFcoeInterfaceStatsHistPacketsTxDelta,
       "cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg": cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg,
       "cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax": cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMax,
       "cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin": cucsEtherFcoeInterfaceStatsHistPacketsTxDeltaMin,
       "cucsEtherFcoeInterfaceStatsHistSuspect": cucsEtherFcoeInterfaceStatsHistSuspect,
       "cucsEtherFcoeInterfaceStatsHistThresholded": cucsEtherFcoeInterfaceStatsHistThresholded,
       "cucsEtherFcoeInterfaceStatsHistTimeCollected": cucsEtherFcoeInterfaceStatsHistTimeCollected,
       "cucsEtherPIoEndPointTable": cucsEtherPIoEndPointTable,
       "cucsEtherPIoEndPointEntry": cucsEtherPIoEndPointEntry,
       "cucsEtherPIoEndPointInstanceId": cucsEtherPIoEndPointInstanceId,
       "cucsEtherPIoEndPointDn": cucsEtherPIoEndPointDn,
       "cucsEtherPIoEndPointRn": cucsEtherPIoEndPointRn,
       "cucsEtherPIoEndPointEndPointDn": cucsEtherPIoEndPointEndPointDn,
       "cucsEtherPIoEndPointEpCloudType": cucsEtherPIoEndPointEpCloudType,
       "cucsEtherPIoEndPointUsrLbl": cucsEtherPIoEndPointUsrLbl,
       "cucsEtherPIoFsmTable": cucsEtherPIoFsmTable,
       "cucsEtherPIoFsmEntry": cucsEtherPIoFsmEntry,
       "cucsEtherPIoFsmInstanceId": cucsEtherPIoFsmInstanceId,
       "cucsEtherPIoFsmDn": cucsEtherPIoFsmDn,
       "cucsEtherPIoFsmRn": cucsEtherPIoFsmRn,
       "cucsEtherPIoFsmCompletionTime": cucsEtherPIoFsmCompletionTime,
       "cucsEtherPIoFsmCurrentFsm": cucsEtherPIoFsmCurrentFsm,
       "cucsEtherPIoFsmDescrData": cucsEtherPIoFsmDescrData,
       "cucsEtherPIoFsmFsmStatus": cucsEtherPIoFsmFsmStatus,
       "cucsEtherPIoFsmProgress": cucsEtherPIoFsmProgress,
       "cucsEtherPIoFsmRmtErrCode": cucsEtherPIoFsmRmtErrCode,
       "cucsEtherPIoFsmRmtErrDescr": cucsEtherPIoFsmRmtErrDescr,
       "cucsEtherPIoFsmRmtRslt": cucsEtherPIoFsmRmtRslt,
       "cucsEtherPIoFsmStageTable": cucsEtherPIoFsmStageTable,
       "cucsEtherPIoFsmStageEntry": cucsEtherPIoFsmStageEntry,
       "cucsEtherPIoFsmStageInstanceId": cucsEtherPIoFsmStageInstanceId,
       "cucsEtherPIoFsmStageDn": cucsEtherPIoFsmStageDn,
       "cucsEtherPIoFsmStageRn": cucsEtherPIoFsmStageRn,
       "cucsEtherPIoFsmStageDescrData": cucsEtherPIoFsmStageDescrData,
       "cucsEtherPIoFsmStageLastUpdateTime": cucsEtherPIoFsmStageLastUpdateTime,
       "cucsEtherPIoFsmStageName": cucsEtherPIoFsmStageName,
       "cucsEtherPIoFsmStageOrder": cucsEtherPIoFsmStageOrder,
       "cucsEtherPIoFsmStageRetry": cucsEtherPIoFsmStageRetry,
       "cucsEtherPIoFsmStageStageStatus": cucsEtherPIoFsmStageStageStatus,
       "cucsEtherServerIntFIoFsmTable": cucsEtherServerIntFIoFsmTable,
       "cucsEtherServerIntFIoFsmEntry": cucsEtherServerIntFIoFsmEntry,
       "cucsEtherServerIntFIoFsmInstanceId": cucsEtherServerIntFIoFsmInstanceId,
       "cucsEtherServerIntFIoFsmDn": cucsEtherServerIntFIoFsmDn,
       "cucsEtherServerIntFIoFsmRn": cucsEtherServerIntFIoFsmRn,
       "cucsEtherServerIntFIoFsmCompletionTime": cucsEtherServerIntFIoFsmCompletionTime,
       "cucsEtherServerIntFIoFsmCurrentFsm": cucsEtherServerIntFIoFsmCurrentFsm,
       "cucsEtherServerIntFIoFsmDescrData": cucsEtherServerIntFIoFsmDescrData,
       "cucsEtherServerIntFIoFsmFsmStatus": cucsEtherServerIntFIoFsmFsmStatus,
       "cucsEtherServerIntFIoFsmProgress": cucsEtherServerIntFIoFsmProgress,
       "cucsEtherServerIntFIoFsmRmtErrCode": cucsEtherServerIntFIoFsmRmtErrCode,
       "cucsEtherServerIntFIoFsmRmtErrDescr": cucsEtherServerIntFIoFsmRmtErrDescr,
       "cucsEtherServerIntFIoFsmRmtRslt": cucsEtherServerIntFIoFsmRmtRslt,
       "cucsEtherServerIntFIoFsmStageTable": cucsEtherServerIntFIoFsmStageTable,
       "cucsEtherServerIntFIoFsmStageEntry": cucsEtherServerIntFIoFsmStageEntry,
       "cucsEtherServerIntFIoFsmStageInstanceId": cucsEtherServerIntFIoFsmStageInstanceId,
       "cucsEtherServerIntFIoFsmStageDn": cucsEtherServerIntFIoFsmStageDn,
       "cucsEtherServerIntFIoFsmStageRn": cucsEtherServerIntFIoFsmStageRn,
       "cucsEtherServerIntFIoFsmStageDescrData": cucsEtherServerIntFIoFsmStageDescrData,
       "cucsEtherServerIntFIoFsmStageLastUpdateTime": cucsEtherServerIntFIoFsmStageLastUpdateTime,
       "cucsEtherServerIntFIoFsmStageName": cucsEtherServerIntFIoFsmStageName,
       "cucsEtherServerIntFIoFsmStageOrder": cucsEtherServerIntFIoFsmStageOrder,
       "cucsEtherServerIntFIoFsmStageRetry": cucsEtherServerIntFIoFsmStageRetry,
       "cucsEtherServerIntFIoFsmStageStageStatus": cucsEtherServerIntFIoFsmStageStageStatus,
       "cucsEtherNiErrStatsTable": cucsEtherNiErrStatsTable,
       "cucsEtherNiErrStatsEntry": cucsEtherNiErrStatsEntry,
       "cucsEtherNiErrStatsInstanceId": cucsEtherNiErrStatsInstanceId,
       "cucsEtherNiErrStatsDn": cucsEtherNiErrStatsDn,
       "cucsEtherNiErrStatsRn": cucsEtherNiErrStatsRn,
       "cucsEtherNiErrStatsCrc": cucsEtherNiErrStatsCrc,
       "cucsEtherNiErrStatsCrcDelta": cucsEtherNiErrStatsCrcDelta,
       "cucsEtherNiErrStatsCrcDeltaAvg": cucsEtherNiErrStatsCrcDeltaAvg,
       "cucsEtherNiErrStatsCrcDeltaMax": cucsEtherNiErrStatsCrcDeltaMax,
       "cucsEtherNiErrStatsCrcDeltaMin": cucsEtherNiErrStatsCrcDeltaMin,
       "cucsEtherNiErrStatsFrameTx": cucsEtherNiErrStatsFrameTx,
       "cucsEtherNiErrStatsFrameTxDelta": cucsEtherNiErrStatsFrameTxDelta,
       "cucsEtherNiErrStatsFrameTxDeltaAvg": cucsEtherNiErrStatsFrameTxDeltaAvg,
       "cucsEtherNiErrStatsFrameTxDeltaMax": cucsEtherNiErrStatsFrameTxDeltaMax,
       "cucsEtherNiErrStatsFrameTxDeltaMin": cucsEtherNiErrStatsFrameTxDeltaMin,
       "cucsEtherNiErrStatsInRange": cucsEtherNiErrStatsInRange,
       "cucsEtherNiErrStatsInRangeDelta": cucsEtherNiErrStatsInRangeDelta,
       "cucsEtherNiErrStatsInRangeDeltaAvg": cucsEtherNiErrStatsInRangeDeltaAvg,
       "cucsEtherNiErrStatsInRangeDeltaMax": cucsEtherNiErrStatsInRangeDeltaMax,
       "cucsEtherNiErrStatsInRangeDeltaMin": cucsEtherNiErrStatsInRangeDeltaMin,
       "cucsEtherNiErrStatsIntervals": cucsEtherNiErrStatsIntervals,
       "cucsEtherNiErrStatsSuspect": cucsEtherNiErrStatsSuspect,
       "cucsEtherNiErrStatsThresholded": cucsEtherNiErrStatsThresholded,
       "cucsEtherNiErrStatsTimeCollected": cucsEtherNiErrStatsTimeCollected,
       "cucsEtherNiErrStatsTooLong": cucsEtherNiErrStatsTooLong,
       "cucsEtherNiErrStatsTooLongDelta": cucsEtherNiErrStatsTooLongDelta,
       "cucsEtherNiErrStatsTooLongDeltaAvg": cucsEtherNiErrStatsTooLongDeltaAvg,
       "cucsEtherNiErrStatsTooLongDeltaMax": cucsEtherNiErrStatsTooLongDeltaMax,
       "cucsEtherNiErrStatsTooLongDeltaMin": cucsEtherNiErrStatsTooLongDeltaMin,
       "cucsEtherNiErrStatsTooShort": cucsEtherNiErrStatsTooShort,
       "cucsEtherNiErrStatsTooShortDelta": cucsEtherNiErrStatsTooShortDelta,
       "cucsEtherNiErrStatsTooShortDeltaAvg": cucsEtherNiErrStatsTooShortDeltaAvg,
       "cucsEtherNiErrStatsTooShortDeltaMax": cucsEtherNiErrStatsTooShortDeltaMax,
       "cucsEtherNiErrStatsTooShortDeltaMin": cucsEtherNiErrStatsTooShortDeltaMin,
       "cucsEtherNiErrStatsUpdate": cucsEtherNiErrStatsUpdate,
       "cucsEtherNiErrStatsHistTable": cucsEtherNiErrStatsHistTable,
       "cucsEtherNiErrStatsHistEntry": cucsEtherNiErrStatsHistEntry,
       "cucsEtherNiErrStatsHistInstanceId": cucsEtherNiErrStatsHistInstanceId,
       "cucsEtherNiErrStatsHistDn": cucsEtherNiErrStatsHistDn,
       "cucsEtherNiErrStatsHistRn": cucsEtherNiErrStatsHistRn,
       "cucsEtherNiErrStatsHistCrc": cucsEtherNiErrStatsHistCrc,
       "cucsEtherNiErrStatsHistCrcDelta": cucsEtherNiErrStatsHistCrcDelta,
       "cucsEtherNiErrStatsHistCrcDeltaAvg": cucsEtherNiErrStatsHistCrcDeltaAvg,
       "cucsEtherNiErrStatsHistCrcDeltaMax": cucsEtherNiErrStatsHistCrcDeltaMax,
       "cucsEtherNiErrStatsHistCrcDeltaMin": cucsEtherNiErrStatsHistCrcDeltaMin,
       "cucsEtherNiErrStatsHistFrameTx": cucsEtherNiErrStatsHistFrameTx,
       "cucsEtherNiErrStatsHistFrameTxDelta": cucsEtherNiErrStatsHistFrameTxDelta,
       "cucsEtherNiErrStatsHistFrameTxDeltaAvg": cucsEtherNiErrStatsHistFrameTxDeltaAvg,
       "cucsEtherNiErrStatsHistFrameTxDeltaMax": cucsEtherNiErrStatsHistFrameTxDeltaMax,
       "cucsEtherNiErrStatsHistFrameTxDeltaMin": cucsEtherNiErrStatsHistFrameTxDeltaMin,
       "cucsEtherNiErrStatsHistId": cucsEtherNiErrStatsHistId,
       "cucsEtherNiErrStatsHistInRange": cucsEtherNiErrStatsHistInRange,
       "cucsEtherNiErrStatsHistInRangeDelta": cucsEtherNiErrStatsHistInRangeDelta,
       "cucsEtherNiErrStatsHistInRangeDeltaAvg": cucsEtherNiErrStatsHistInRangeDeltaAvg,
       "cucsEtherNiErrStatsHistInRangeDeltaMax": cucsEtherNiErrStatsHistInRangeDeltaMax,
       "cucsEtherNiErrStatsHistInRangeDeltaMin": cucsEtherNiErrStatsHistInRangeDeltaMin,
       "cucsEtherNiErrStatsHistMostRecent": cucsEtherNiErrStatsHistMostRecent,
       "cucsEtherNiErrStatsHistSuspect": cucsEtherNiErrStatsHistSuspect,
       "cucsEtherNiErrStatsHistThresholded": cucsEtherNiErrStatsHistThresholded,
       "cucsEtherNiErrStatsHistTimeCollected": cucsEtherNiErrStatsHistTimeCollected,
       "cucsEtherNiErrStatsHistTooLong": cucsEtherNiErrStatsHistTooLong,
       "cucsEtherNiErrStatsHistTooLongDelta": cucsEtherNiErrStatsHistTooLongDelta,
       "cucsEtherNiErrStatsHistTooLongDeltaAvg": cucsEtherNiErrStatsHistTooLongDeltaAvg,
       "cucsEtherNiErrStatsHistTooLongDeltaMax": cucsEtherNiErrStatsHistTooLongDeltaMax,
       "cucsEtherNiErrStatsHistTooLongDeltaMin": cucsEtherNiErrStatsHistTooLongDeltaMin,
       "cucsEtherNiErrStatsHistTooShort": cucsEtherNiErrStatsHistTooShort,
       "cucsEtherNiErrStatsHistTooShortDelta": cucsEtherNiErrStatsHistTooShortDelta,
       "cucsEtherNiErrStatsHistTooShortDeltaAvg": cucsEtherNiErrStatsHistTooShortDeltaAvg,
       "cucsEtherNiErrStatsHistTooShortDeltaMax": cucsEtherNiErrStatsHistTooShortDeltaMax,
       "cucsEtherNiErrStatsHistTooShortDeltaMin": cucsEtherNiErrStatsHistTooShortDeltaMin}
)
