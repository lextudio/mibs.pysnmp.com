# SNMP MIB module (RBN-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-CES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:01 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(RbnAlarmId,) = mibBuilder.importSymbols(
    "RBN-ALARM-TC",
    "RbnAlarmId")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPercentage,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPercentage")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rbnCesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56)
)
rbnCesMIB.setRevisions(
        ("2010-12-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnCesMIBObjects_ObjectIdentity = ObjectIdentity
rbnCesMIBObjects = _RbnCesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1)
)


class _RbnCesSlaInfoResetAll_Type(TruthValue):
    """Custom type rbnCesSlaInfoResetAll based on TruthValue"""


_RbnCesSlaInfoResetAll_Object = MibScalar
rbnCesSlaInfoResetAll = _RbnCesSlaInfoResetAll_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 1),
    _RbnCesSlaInfoResetAll_Type()
)
rbnCesSlaInfoResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnCesSlaInfoResetAll.setStatus("current")
_RbnCesCfgTable_Object = MibTable
rbnCesCfgTable = _RbnCesCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2)
)
if mibBuilder.loadTexts:
    rbnCesCfgTable.setStatus("current")
_RbnCesCfgEntry_Object = MibTableRow
rbnCesCfgEntry = _RbnCesCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1)
)
rbnCesCfgEntry.setIndexNames(
    (0, "RBN-CES-MIB", "rbnCesCfgIndex"),
)
if mibBuilder.loadTexts:
    rbnCesCfgEntry.setStatus("current")
_RbnCesCfgIndex_Type = InterfaceIndex
_RbnCesCfgIndex_Object = MibTableColumn
rbnCesCfgIndex = _RbnCesCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 1),
    _RbnCesCfgIndex_Type()
)
rbnCesCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCesCfgIndex.setStatus("current")


class _RbnCesCfgPktLatency_Type(Unsigned32):
    """Custom type rbnCesCfgPktLatency based on Unsigned32"""
    defaultValue = 1000


_RbnCesCfgPktLatency_Object = MibTableColumn
rbnCesCfgPktLatency = _RbnCesCfgPktLatency_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 2),
    _RbnCesCfgPktLatency_Type()
)
rbnCesCfgPktLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgPktLatency.setStatus("current")
if mibBuilder.loadTexts:
    rbnCesCfgPktLatency.setUnits("microseconds")


class _RbnCesCfgJtrBfrDepth_Type(Unsigned32):
    """Custom type rbnCesCfgJtrBfrDepth based on Unsigned32"""
    defaultValue = 5000


_RbnCesCfgJtrBfrDepth_Object = MibTableColumn
rbnCesCfgJtrBfrDepth = _RbnCesCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 3),
    _RbnCesCfgJtrBfrDepth_Type()
)
rbnCesCfgJtrBfrDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    rbnCesCfgJtrBfrDepth.setUnits("microseconds")


class _RbnCesCfgConsecPktsInSync_Type(Unsigned32):
    """Custom type rbnCesCfgConsecPktsInSync based on Unsigned32"""
    defaultValue = 10


_RbnCesCfgConsecPktsInSync_Object = MibTableColumn
rbnCesCfgConsecPktsInSync = _RbnCesCfgConsecPktsInSync_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 4),
    _RbnCesCfgConsecPktsInSync_Type()
)
rbnCesCfgConsecPktsInSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgConsecPktsInSync.setStatus("current")


class _RbnCesCfgConsecMissPktsOutSync_Type(Unsigned32):
    """Custom type rbnCesCfgConsecMissPktsOutSync based on Unsigned32"""
    defaultValue = 1


_RbnCesCfgConsecMissPktsOutSync_Object = MibTableColumn
rbnCesCfgConsecMissPktsOutSync = _RbnCesCfgConsecMissPktsOutSync_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 5),
    _RbnCesCfgConsecMissPktsOutSync_Type()
)
rbnCesCfgConsecMissPktsOutSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgConsecMissPktsOutSync.setStatus("current")


class _RbnCesCfgIdlePattern_Type(OctetString):
    """Custom type rbnCesCfgIdlePattern based on OctetString"""
    defaultHexValue = "3F"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RbnCesCfgIdlePattern_Type.__name__ = "OctetString"
_RbnCesCfgIdlePattern_Object = MibTableColumn
rbnCesCfgIdlePattern = _RbnCesCfgIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 6),
    _RbnCesCfgIdlePattern_Type()
)
rbnCesCfgIdlePattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgIdlePattern.setStatus("current")


class _RbnCesCfgTrunkCtl_Type(TruthValue):
    """Custom type rbnCesCfgTrunkCtl based on TruthValue"""


_RbnCesCfgTrunkCtl_Object = MibTableColumn
rbnCesCfgTrunkCtl = _RbnCesCfgTrunkCtl_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 7),
    _RbnCesCfgTrunkCtl_Type()
)
rbnCesCfgTrunkCtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgTrunkCtl.setStatus("current")


class _RbnCesCfgAdminStatus_Type(Integer32):
    """Custom type rbnCesCfgAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RbnCesCfgAdminStatus_Type.__name__ = "Integer32"
_RbnCesCfgAdminStatus_Object = MibTableColumn
rbnCesCfgAdminStatus = _RbnCesCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 8),
    _RbnCesCfgAdminStatus_Type()
)
rbnCesCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgAdminStatus.setStatus("current")
_RbnCesCfgRowStatus_Type = RowStatus
_RbnCesCfgRowStatus_Object = MibTableColumn
rbnCesCfgRowStatus = _RbnCesCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 2, 1, 9),
    _RbnCesCfgRowStatus_Type()
)
rbnCesCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesCfgRowStatus.setStatus("current")
_RbnCesStatsTable_Object = MibTable
rbnCesStatsTable = _RbnCesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3)
)
if mibBuilder.loadTexts:
    rbnCesStatsTable.setStatus("current")
_RbnCesStatsEntry_Object = MibTableRow
rbnCesStatsEntry = _RbnCesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbnCesStatsEntry.setStatus("current")
_RbnCesStatsEgressOutOfBfrDroppedPkts_Type = Counter64
_RbnCesStatsEgressOutOfBfrDroppedPkts_Object = MibTableColumn
rbnCesStatsEgressOutOfBfrDroppedPkts = _RbnCesStatsEgressOutOfBfrDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 1),
    _RbnCesStatsEgressOutOfBfrDroppedPkts_Type()
)
rbnCesStatsEgressOutOfBfrDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressOutOfBfrDroppedPkts.setStatus("current")
_RbnCesStatsEgressMissingPkts_Type = Counter64
_RbnCesStatsEgressMissingPkts_Object = MibTableColumn
rbnCesStatsEgressMissingPkts = _RbnCesStatsEgressMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 2),
    _RbnCesStatsEgressMissingPkts_Type()
)
rbnCesStatsEgressMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressMissingPkts.setStatus("current")
_RbnCesStatsEgressMalformedPkts_Type = Counter64
_RbnCesStatsEgressMalformedPkts_Object = MibTableColumn
rbnCesStatsEgressMalformedPkts = _RbnCesStatsEgressMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 3),
    _RbnCesStatsEgressMalformedPkts_Type()
)
rbnCesStatsEgressMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressMalformedPkts.setStatus("current")
_RbnCesStatsEgressJtrBfrOverrunPkts_Type = Counter64
_RbnCesStatsEgressJtrBfrOverrunPkts_Object = MibTableColumn
rbnCesStatsEgressJtrBfrOverrunPkts = _RbnCesStatsEgressJtrBfrOverrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 4),
    _RbnCesStatsEgressJtrBfrOverrunPkts_Type()
)
rbnCesStatsEgressJtrBfrOverrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressJtrBfrOverrunPkts.setStatus("current")
_RbnCesStatsEgressJtrBfrUnderruns_Type = Counter64
_RbnCesStatsEgressJtrBfrUnderruns_Object = MibTableColumn
rbnCesStatsEgressJtrBfrUnderruns = _RbnCesStatsEgressJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 5),
    _RbnCesStatsEgressJtrBfrUnderruns_Type()
)
rbnCesStatsEgressJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressJtrBfrUnderruns.setStatus("current")
_RbnCesStatsEgressMisOrderPkts_Type = Counter64
_RbnCesStatsEgressMisOrderPkts_Object = MibTableColumn
rbnCesStatsEgressMisOrderPkts = _RbnCesStatsEgressMisOrderPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 6),
    _RbnCesStatsEgressMisOrderPkts_Type()
)
rbnCesStatsEgressMisOrderPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressMisOrderPkts.setStatus("current")
_RbnCesStatsEgressRemoteLossPkts_Type = Counter64
_RbnCesStatsEgressRemoteLossPkts_Object = MibTableColumn
rbnCesStatsEgressRemoteLossPkts = _RbnCesStatsEgressRemoteLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 7),
    _RbnCesStatsEgressRemoteLossPkts_Type()
)
rbnCesStatsEgressRemoteLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressRemoteLossPkts.setStatus("current")
_RbnCesStatsEgressWindowSwitchovers_Type = Counter64
_RbnCesStatsEgressWindowSwitchovers_Object = MibTableColumn
rbnCesStatsEgressWindowSwitchovers = _RbnCesStatsEgressWindowSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 8),
    _RbnCesStatsEgressWindowSwitchovers_Type()
)
rbnCesStatsEgressWindowSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressWindowSwitchovers.setStatus("current")
_RbnCesStatsEgressRemoteAcDownPkts_Type = Counter64
_RbnCesStatsEgressRemoteAcDownPkts_Object = MibTableColumn
rbnCesStatsEgressRemoteAcDownPkts = _RbnCesStatsEgressRemoteAcDownPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 9),
    _RbnCesStatsEgressRemoteAcDownPkts_Type()
)
rbnCesStatsEgressRemoteAcDownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressRemoteAcDownPkts.setStatus("current")
_RbnCesStatsEgressDuplicatePkts_Type = Counter64
_RbnCesStatsEgressDuplicatePkts_Object = MibTableColumn
rbnCesStatsEgressDuplicatePkts = _RbnCesStatsEgressDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 10),
    _RbnCesStatsEgressDuplicatePkts_Type()
)
rbnCesStatsEgressDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressDuplicatePkts.setStatus("current")
_RbnCesStatsEgressDeniedPkts_Type = Counter64
_RbnCesStatsEgressDeniedPkts_Object = MibTableColumn
rbnCesStatsEgressDeniedPkts = _RbnCesStatsEgressDeniedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 11),
    _RbnCesStatsEgressDeniedPkts_Type()
)
rbnCesStatsEgressDeniedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressDeniedPkts.setStatus("current")
_RbnCesStatsEgressErrorEvents_Type = Counter64
_RbnCesStatsEgressErrorEvents_Object = MibTableColumn
rbnCesStatsEgressErrorEvents = _RbnCesStatsEgressErrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 12),
    _RbnCesStatsEgressErrorEvents_Type()
)
rbnCesStatsEgressErrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressErrorEvents.setStatus("current")
_RbnCesStatsEgressErrorDataBlocks_Type = Counter64
_RbnCesStatsEgressErrorDataBlocks_Object = MibTableColumn
rbnCesStatsEgressErrorDataBlocks = _RbnCesStatsEgressErrorDataBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 13),
    _RbnCesStatsEgressErrorDataBlocks_Type()
)
rbnCesStatsEgressErrorDataBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsEgressErrorDataBlocks.setStatus("current")
_RbnCesStatsIngressOutOfBfrDroppedPkts_Type = Counter64
_RbnCesStatsIngressOutOfBfrDroppedPkts_Object = MibTableColumn
rbnCesStatsIngressOutOfBfrDroppedPkts = _RbnCesStatsIngressOutOfBfrDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 14),
    _RbnCesStatsIngressOutOfBfrDroppedPkts_Type()
)
rbnCesStatsIngressOutOfBfrDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsIngressOutOfBfrDroppedPkts.setStatus("current")
_RbnCesStatsIngressSizeViolationDroppedPkts_Type = Counter64
_RbnCesStatsIngressSizeViolationDroppedPkts_Object = MibTableColumn
rbnCesStatsIngressSizeViolationDroppedPkts = _RbnCesStatsIngressSizeViolationDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 15),
    _RbnCesStatsIngressSizeViolationDroppedPkts_Type()
)
rbnCesStatsIngressSizeViolationDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsIngressSizeViolationDroppedPkts.setStatus("current")
_RbnCesStatsIngressTransmitDroppedPkts_Type = Counter64
_RbnCesStatsIngressTransmitDroppedPkts_Object = MibTableColumn
rbnCesStatsIngressTransmitDroppedPkts = _RbnCesStatsIngressTransmitDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 3, 1, 16),
    _RbnCesStatsIngressTransmitDroppedPkts_Type()
)
rbnCesStatsIngressTransmitDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesStatsIngressTransmitDroppedPkts.setStatus("current")
_RbnCesEplCfgTable_Object = MibTable
rbnCesEplCfgTable = _RbnCesEplCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4)
)
if mibBuilder.loadTexts:
    rbnCesEplCfgTable.setStatus("current")
_RbnCesEplCfgEntry_Object = MibTableRow
rbnCesEplCfgEntry = _RbnCesEplCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1)
)
rbnCesEplCfgEntry.setIndexNames(
    (0, "RBN-CES-MIB", "rbnCesEplCfgIndex"),
)
if mibBuilder.loadTexts:
    rbnCesEplCfgEntry.setStatus("current")


class _RbnCesEplCfgIndex_Type(Integer32):
    """Custom type rbnCesEplCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnCesEplCfgIndex_Type.__name__ = "Integer32"
_RbnCesEplCfgIndex_Object = MibTableColumn
rbnCesEplCfgIndex = _RbnCesEplCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1, 1),
    _RbnCesEplCfgIndex_Type()
)
rbnCesEplCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCesEplCfgIndex.setStatus("current")
_RbnCesEplCfgThreshold_Type = RbnPercentage
_RbnCesEplCfgThreshold_Object = MibTableColumn
rbnCesEplCfgThreshold = _RbnCesEplCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1, 2),
    _RbnCesEplCfgThreshold_Type()
)
rbnCesEplCfgThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesEplCfgThreshold.setStatus("current")


class _RbnCesEplCfgFaultDeclarationTime_Type(Unsigned32):
    """Custom type rbnCesEplCfgFaultDeclarationTime based on Unsigned32"""
    defaultValue = 2500


_RbnCesEplCfgFaultDeclarationTime_Object = MibTableColumn
rbnCesEplCfgFaultDeclarationTime = _RbnCesEplCfgFaultDeclarationTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1, 3),
    _RbnCesEplCfgFaultDeclarationTime_Type()
)
rbnCesEplCfgFaultDeclarationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesEplCfgFaultDeclarationTime.setStatus("current")
if mibBuilder.loadTexts:
    rbnCesEplCfgFaultDeclarationTime.setUnits("milliseconds")


class _RbnCesEplCfgClearingTime_Type(Unsigned32):
    """Custom type rbnCesEplCfgClearingTime based on Unsigned32"""
    defaultValue = 10000


_RbnCesEplCfgClearingTime_Object = MibTableColumn
rbnCesEplCfgClearingTime = _RbnCesEplCfgClearingTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1, 4),
    _RbnCesEplCfgClearingTime_Type()
)
rbnCesEplCfgClearingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesEplCfgClearingTime.setStatus("current")
if mibBuilder.loadTexts:
    rbnCesEplCfgClearingTime.setUnits("milliseconds")


class _RbnCesEplCfgStatsResetAll_Type(TruthValue):
    """Custom type rbnCesEplCfgStatsResetAll based on TruthValue"""


_RbnCesEplCfgStatsResetAll_Object = MibTableColumn
rbnCesEplCfgStatsResetAll = _RbnCesEplCfgStatsResetAll_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1, 5),
    _RbnCesEplCfgStatsResetAll_Type()
)
rbnCesEplCfgStatsResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnCesEplCfgStatsResetAll.setStatus("current")


class _RbnCesEplCfgAdminStatus_Type(Integer32):
    """Custom type rbnCesEplCfgAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RbnCesEplCfgAdminStatus_Type.__name__ = "Integer32"
_RbnCesEplCfgAdminStatus_Object = MibTableColumn
rbnCesEplCfgAdminStatus = _RbnCesEplCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1, 6),
    _RbnCesEplCfgAdminStatus_Type()
)
rbnCesEplCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesEplCfgAdminStatus.setStatus("current")
_RbnCesEplCfgRowStatus_Type = RowStatus
_RbnCesEplCfgRowStatus_Object = MibTableColumn
rbnCesEplCfgRowStatus = _RbnCesEplCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 4, 1, 7),
    _RbnCesEplCfgRowStatus_Type()
)
rbnCesEplCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnCesEplCfgRowStatus.setStatus("current")
_RbnCesEplStatsTable_Object = MibTable
rbnCesEplStatsTable = _RbnCesEplStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5)
)
if mibBuilder.loadTexts:
    rbnCesEplStatsTable.setStatus("current")
_RbnCesEplStatsEntry_Object = MibTableRow
rbnCesEplStatsEntry = _RbnCesEplStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1)
)
rbnCesEplStatsEntry.setIndexNames(
    (0, "RBN-CES-MIB", "rbnCesEplStatsIndex"),
)
if mibBuilder.loadTexts:
    rbnCesEplStatsEntry.setStatus("current")
_RbnCesEplStatsIndex_Type = InterfaceIndex
_RbnCesEplStatsIndex_Object = MibTableColumn
rbnCesEplStatsIndex = _RbnCesEplStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 1),
    _RbnCesEplStatsIndex_Type()
)
rbnCesEplStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCesEplStatsIndex.setStatus("current")
_RbnCesEplStatsEntryTime_Type = DateAndTime
_RbnCesEplStatsEntryTime_Object = MibTableColumn
rbnCesEplStatsEntryTime = _RbnCesEplStatsEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 2),
    _RbnCesEplStatsEntryTime_Type()
)
rbnCesEplStatsEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesEplStatsEntryTime.setStatus("current")
_RbnCesEplStatsEntryTotalPktLossTime_Type = TimeInterval
_RbnCesEplStatsEntryTotalPktLossTime_Object = MibTableColumn
rbnCesEplStatsEntryTotalPktLossTime = _RbnCesEplStatsEntryTotalPktLossTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 3),
    _RbnCesEplStatsEntryTotalPktLossTime_Type()
)
rbnCesEplStatsEntryTotalPktLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesEplStatsEntryTotalPktLossTime.setStatus("current")
_RbnCesEplStatsExitTime_Type = TimeInterval
_RbnCesEplStatsExitTime_Object = MibTableColumn
rbnCesEplStatsExitTime = _RbnCesEplStatsExitTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 4),
    _RbnCesEplStatsExitTime_Type()
)
rbnCesEplStatsExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesEplStatsExitTime.setStatus("current")
_RbnCesEplStatsExitTotalPktLossTime_Type = TimeInterval
_RbnCesEplStatsExitTotalPktLossTime_Object = MibTableColumn
rbnCesEplStatsExitTotalPktLossTime = _RbnCesEplStatsExitTotalPktLossTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 5),
    _RbnCesEplStatsExitTotalPktLossTime_Type()
)
rbnCesEplStatsExitTotalPktLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesEplStatsExitTotalPktLossTime.setStatus("current")
_RbnCesEplStatsCount_Type = Gauge32
_RbnCesEplStatsCount_Object = MibTableColumn
rbnCesEplStatsCount = _RbnCesEplStatsCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 6),
    _RbnCesEplStatsCount_Type()
)
rbnCesEplStatsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesEplStatsCount.setStatus("current")
_RbnCesEplStatsTotalCircuitTime_Type = TimeInterval
_RbnCesEplStatsTotalCircuitTime_Object = MibTableColumn
rbnCesEplStatsTotalCircuitTime = _RbnCesEplStatsTotalCircuitTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 7),
    _RbnCesEplStatsTotalCircuitTime_Type()
)
rbnCesEplStatsTotalCircuitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesEplStatsTotalCircuitTime.setStatus("current")
_RbnCesEplStatsTotalFailureRate_Type = RbnPercentage
_RbnCesEplStatsTotalFailureRate_Object = MibTableColumn
rbnCesEplStatsTotalFailureRate = _RbnCesEplStatsTotalFailureRate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 8),
    _RbnCesEplStatsTotalFailureRate_Type()
)
rbnCesEplStatsTotalFailureRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesEplStatsTotalFailureRate.setStatus("current")


class _RbnCesEplStatsReset_Type(TruthValue):
    """Custom type rbnCesEplStatsReset based on TruthValue"""


_RbnCesEplStatsReset_Object = MibTableColumn
rbnCesEplStatsReset = _RbnCesEplStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 5, 1, 9),
    _RbnCesEplStatsReset_Type()
)
rbnCesEplStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnCesEplStatsReset.setStatus("current")
_RbnCesSlaInfoTable_Object = MibTable
rbnCesSlaInfoTable = _RbnCesSlaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6)
)
if mibBuilder.loadTexts:
    rbnCesSlaInfoTable.setStatus("current")
_RbnCesSlaInfoEntry_Object = MibTableRow
rbnCesSlaInfoEntry = _RbnCesSlaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1)
)
rbnCesSlaInfoEntry.setIndexNames(
    (0, "RBN-CES-MIB", "rbnCesSlaInfoIndex"),
)
if mibBuilder.loadTexts:
    rbnCesSlaInfoEntry.setStatus("current")
_RbnCesSlaInfoIndex_Type = InterfaceIndex
_RbnCesSlaInfoIndex_Object = MibTableColumn
rbnCesSlaInfoIndex = _RbnCesSlaInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 1),
    _RbnCesSlaInfoIndex_Type()
)
rbnCesSlaInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCesSlaInfoIndex.setStatus("current")
_RbnCesSlaInfoLatestOutageTime_Type = TimeInterval
_RbnCesSlaInfoLatestOutageTime_Object = MibTableColumn
rbnCesSlaInfoLatestOutageTime = _RbnCesSlaInfoLatestOutageTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 2),
    _RbnCesSlaInfoLatestOutageTime_Type()
)
rbnCesSlaInfoLatestOutageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoLatestOutageTime.setStatus("current")
_RbnCesSlaInfoEntryLatestOutage_Type = DateAndTime
_RbnCesSlaInfoEntryLatestOutage_Object = MibTableColumn
rbnCesSlaInfoEntryLatestOutage = _RbnCesSlaInfoEntryLatestOutage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 3),
    _RbnCesSlaInfoEntryLatestOutage_Type()
)
rbnCesSlaInfoEntryLatestOutage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoEntryLatestOutage.setStatus("current")
_RbnCesSlaInfoExitLatestOutage_Type = DateAndTime
_RbnCesSlaInfoExitLatestOutage_Object = MibTableColumn
rbnCesSlaInfoExitLatestOutage = _RbnCesSlaInfoExitLatestOutage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 4),
    _RbnCesSlaInfoExitLatestOutage_Type()
)
rbnCesSlaInfoExitLatestOutage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoExitLatestOutage.setStatus("current")
_RbnCesSlaInfoLastOutageTime_Type = TimeInterval
_RbnCesSlaInfoLastOutageTime_Object = MibTableColumn
rbnCesSlaInfoLastOutageTime = _RbnCesSlaInfoLastOutageTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 5),
    _RbnCesSlaInfoLastOutageTime_Type()
)
rbnCesSlaInfoLastOutageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoLastOutageTime.setStatus("current")
_RbnCesSlaInfoLastUpTime_Type = TimeInterval
_RbnCesSlaInfoLastUpTime_Object = MibTableColumn
rbnCesSlaInfoLastUpTime = _RbnCesSlaInfoLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 6),
    _RbnCesSlaInfoLastUpTime_Type()
)
rbnCesSlaInfoLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoLastUpTime.setStatus("current")
_RbnCesSlaInfoTotalOutageTime_Type = TimeInterval
_RbnCesSlaInfoTotalOutageTime_Object = MibTableColumn
rbnCesSlaInfoTotalOutageTime = _RbnCesSlaInfoTotalOutageTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 7),
    _RbnCesSlaInfoTotalOutageTime_Type()
)
rbnCesSlaInfoTotalOutageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoTotalOutageTime.setStatus("current")
_RbnCesSlaInfoTotalUpTime_Type = TimeInterval
_RbnCesSlaInfoTotalUpTime_Object = MibTableColumn
rbnCesSlaInfoTotalUpTime = _RbnCesSlaInfoTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 8),
    _RbnCesSlaInfoTotalUpTime_Type()
)
rbnCesSlaInfoTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoTotalUpTime.setStatus("current")
_RbnCesSlaInfoOutageCount_Type = Gauge32
_RbnCesSlaInfoOutageCount_Object = MibTableColumn
rbnCesSlaInfoOutageCount = _RbnCesSlaInfoOutageCount_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 9),
    _RbnCesSlaInfoOutageCount_Type()
)
rbnCesSlaInfoOutageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCesSlaInfoOutageCount.setStatus("current")


class _RbnCesSlaInfoReset_Type(TruthValue):
    """Custom type rbnCesSlaInfoReset based on TruthValue"""


_RbnCesSlaInfoReset_Object = MibTableColumn
rbnCesSlaInfoReset = _RbnCesSlaInfoReset_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 6, 1, 10),
    _RbnCesSlaInfoReset_Type()
)
rbnCesSlaInfoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnCesSlaInfoReset.setStatus("current")
_RbnCesCardAlarmTable_Object = MibTable
rbnCesCardAlarmTable = _RbnCesCardAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 7)
)
if mibBuilder.loadTexts:
    rbnCesCardAlarmTable.setStatus("current")
_RbnCesCardAlarmEntry_Object = MibTableRow
rbnCesCardAlarmEntry = _RbnCesCardAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 7, 1)
)
rbnCesCardAlarmEntry.setIndexNames(
    (0, "RBN-CES-MIB", "rbnCesCardAlarmId"),
)
if mibBuilder.loadTexts:
    rbnCesCardAlarmEntry.setStatus("current")
_RbnCesCardAlarmId_Type = RbnAlarmId
_RbnCesCardAlarmId_Object = MibTableColumn
rbnCesCardAlarmId = _RbnCesCardAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 7, 1, 1),
    _RbnCesCardAlarmId_Type()
)
rbnCesCardAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCesCardAlarmId.setStatus("current")


class _RbnCesCardAlarmNotificationEnable_Type(TruthValue):
    """Custom type rbnCesCardAlarmNotificationEnable based on TruthValue"""


_RbnCesCardAlarmNotificationEnable_Object = MibTableColumn
rbnCesCardAlarmNotificationEnable = _RbnCesCardAlarmNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 1, 7, 1, 2),
    _RbnCesCardAlarmNotificationEnable_Type()
)
rbnCesCardAlarmNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnCesCardAlarmNotificationEnable.setStatus("current")
_RbnCesMIBConformance_ObjectIdentity = ObjectIdentity
rbnCesMIBConformance = _RbnCesMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2)
)
_RbnCesMIBCompliances_ObjectIdentity = ObjectIdentity
rbnCesMIBCompliances = _RbnCesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 1)
)
_RbnCesMIBGroups_ObjectIdentity = ObjectIdentity
rbnCesMIBGroups = _RbnCesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 2)
)
rbnCesCfgEntry.registerAugmentions(
    ("RBN-CES-MIB",
     "rbnCesStatsEntry")
)
rbnCesStatsEntry.setIndexNames(*rbnCesCfgEntry.getIndexNames())

# Managed Objects groups

rbnCesCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 2, 1)
)
rbnCesCfgGroup.setObjects(
      *(("RBN-CES-MIB", "rbnCesSlaInfoResetAll"),
        ("RBN-CES-MIB", "rbnCesCfgPktLatency"),
        ("RBN-CES-MIB", "rbnCesCfgJtrBfrDepth"),
        ("RBN-CES-MIB", "rbnCesCfgConsecPktsInSync"),
        ("RBN-CES-MIB", "rbnCesCfgConsecMissPktsOutSync"),
        ("RBN-CES-MIB", "rbnCesCfgIdlePattern"),
        ("RBN-CES-MIB", "rbnCesCfgTrunkCtl"),
        ("RBN-CES-MIB", "rbnCesCfgAdminStatus"),
        ("RBN-CES-MIB", "rbnCesCfgRowStatus"))
)
if mibBuilder.loadTexts:
    rbnCesCfgGroup.setStatus("current")

rbnCesStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 2, 2)
)
rbnCesStatsGroup.setObjects(
      *(("RBN-CES-MIB", "rbnCesStatsEgressOutOfBfrDroppedPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressMissingPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressMalformedPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressJtrBfrOverrunPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressJtrBfrUnderruns"),
        ("RBN-CES-MIB", "rbnCesStatsEgressMisOrderPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressRemoteLossPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressWindowSwitchovers"),
        ("RBN-CES-MIB", "rbnCesStatsEgressRemoteAcDownPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressDuplicatePkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressDeniedPkts"),
        ("RBN-CES-MIB", "rbnCesStatsEgressErrorEvents"),
        ("RBN-CES-MIB", "rbnCesStatsEgressErrorDataBlocks"),
        ("RBN-CES-MIB", "rbnCesStatsIngressOutOfBfrDroppedPkts"),
        ("RBN-CES-MIB", "rbnCesStatsIngressSizeViolationDroppedPkts"),
        ("RBN-CES-MIB", "rbnCesStatsIngressTransmitDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnCesStatsGroup.setStatus("current")

rbnCesEplCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 2, 3)
)
rbnCesEplCfgGroup.setObjects(
      *(("RBN-CES-MIB", "rbnCesEplCfgThreshold"),
        ("RBN-CES-MIB", "rbnCesEplCfgFaultDeclarationTime"),
        ("RBN-CES-MIB", "rbnCesEplCfgClearingTime"),
        ("RBN-CES-MIB", "rbnCesEplCfgStatsResetAll"),
        ("RBN-CES-MIB", "rbnCesEplCfgAdminStatus"),
        ("RBN-CES-MIB", "rbnCesEplCfgRowStatus"))
)
if mibBuilder.loadTexts:
    rbnCesEplCfgGroup.setStatus("current")

rbnCesEplStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 2, 4)
)
rbnCesEplStatsGroup.setObjects(
      *(("RBN-CES-MIB", "rbnCesEplStatsEntryTime"),
        ("RBN-CES-MIB", "rbnCesEplStatsEntryTotalPktLossTime"),
        ("RBN-CES-MIB", "rbnCesEplStatsExitTime"),
        ("RBN-CES-MIB", "rbnCesEplStatsExitTotalPktLossTime"),
        ("RBN-CES-MIB", "rbnCesEplStatsCount"),
        ("RBN-CES-MIB", "rbnCesEplStatsTotalCircuitTime"),
        ("RBN-CES-MIB", "rbnCesEplStatsTotalFailureRate"),
        ("RBN-CES-MIB", "rbnCesEplStatsReset"))
)
if mibBuilder.loadTexts:
    rbnCesEplStatsGroup.setStatus("current")

rbnCesSlaInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 2, 5)
)
rbnCesSlaInfoGroup.setObjects(
      *(("RBN-CES-MIB", "rbnCesSlaInfoLatestOutageTime"),
        ("RBN-CES-MIB", "rbnCesSlaInfoEntryLatestOutage"),
        ("RBN-CES-MIB", "rbnCesSlaInfoExitLatestOutage"),
        ("RBN-CES-MIB", "rbnCesSlaInfoLastOutageTime"),
        ("RBN-CES-MIB", "rbnCesSlaInfoLastUpTime"),
        ("RBN-CES-MIB", "rbnCesSlaInfoTotalOutageTime"),
        ("RBN-CES-MIB", "rbnCesSlaInfoTotalUpTime"),
        ("RBN-CES-MIB", "rbnCesSlaInfoOutageCount"),
        ("RBN-CES-MIB", "rbnCesSlaInfoReset"))
)
if mibBuilder.loadTexts:
    rbnCesSlaInfoGroup.setStatus("current")

rbnCesCardAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 2, 6)
)
rbnCesCardAlarmGroup.setObjects(
    ("RBN-CES-MIB", "rbnCesCardAlarmNotificationEnable")
)
if mibBuilder.loadTexts:
    rbnCesCardAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnCesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 56, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnCesMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-CES-MIB",
    **{"rbnCesMIB": rbnCesMIB,
       "rbnCesMIBObjects": rbnCesMIBObjects,
       "rbnCesSlaInfoResetAll": rbnCesSlaInfoResetAll,
       "rbnCesCfgTable": rbnCesCfgTable,
       "rbnCesCfgEntry": rbnCesCfgEntry,
       "rbnCesCfgIndex": rbnCesCfgIndex,
       "rbnCesCfgPktLatency": rbnCesCfgPktLatency,
       "rbnCesCfgJtrBfrDepth": rbnCesCfgJtrBfrDepth,
       "rbnCesCfgConsecPktsInSync": rbnCesCfgConsecPktsInSync,
       "rbnCesCfgConsecMissPktsOutSync": rbnCesCfgConsecMissPktsOutSync,
       "rbnCesCfgIdlePattern": rbnCesCfgIdlePattern,
       "rbnCesCfgTrunkCtl": rbnCesCfgTrunkCtl,
       "rbnCesCfgAdminStatus": rbnCesCfgAdminStatus,
       "rbnCesCfgRowStatus": rbnCesCfgRowStatus,
       "rbnCesStatsTable": rbnCesStatsTable,
       "rbnCesStatsEntry": rbnCesStatsEntry,
       "rbnCesStatsEgressOutOfBfrDroppedPkts": rbnCesStatsEgressOutOfBfrDroppedPkts,
       "rbnCesStatsEgressMissingPkts": rbnCesStatsEgressMissingPkts,
       "rbnCesStatsEgressMalformedPkts": rbnCesStatsEgressMalformedPkts,
       "rbnCesStatsEgressJtrBfrOverrunPkts": rbnCesStatsEgressJtrBfrOverrunPkts,
       "rbnCesStatsEgressJtrBfrUnderruns": rbnCesStatsEgressJtrBfrUnderruns,
       "rbnCesStatsEgressMisOrderPkts": rbnCesStatsEgressMisOrderPkts,
       "rbnCesStatsEgressRemoteLossPkts": rbnCesStatsEgressRemoteLossPkts,
       "rbnCesStatsEgressWindowSwitchovers": rbnCesStatsEgressWindowSwitchovers,
       "rbnCesStatsEgressRemoteAcDownPkts": rbnCesStatsEgressRemoteAcDownPkts,
       "rbnCesStatsEgressDuplicatePkts": rbnCesStatsEgressDuplicatePkts,
       "rbnCesStatsEgressDeniedPkts": rbnCesStatsEgressDeniedPkts,
       "rbnCesStatsEgressErrorEvents": rbnCesStatsEgressErrorEvents,
       "rbnCesStatsEgressErrorDataBlocks": rbnCesStatsEgressErrorDataBlocks,
       "rbnCesStatsIngressOutOfBfrDroppedPkts": rbnCesStatsIngressOutOfBfrDroppedPkts,
       "rbnCesStatsIngressSizeViolationDroppedPkts": rbnCesStatsIngressSizeViolationDroppedPkts,
       "rbnCesStatsIngressTransmitDroppedPkts": rbnCesStatsIngressTransmitDroppedPkts,
       "rbnCesEplCfgTable": rbnCesEplCfgTable,
       "rbnCesEplCfgEntry": rbnCesEplCfgEntry,
       "rbnCesEplCfgIndex": rbnCesEplCfgIndex,
       "rbnCesEplCfgThreshold": rbnCesEplCfgThreshold,
       "rbnCesEplCfgFaultDeclarationTime": rbnCesEplCfgFaultDeclarationTime,
       "rbnCesEplCfgClearingTime": rbnCesEplCfgClearingTime,
       "rbnCesEplCfgStatsResetAll": rbnCesEplCfgStatsResetAll,
       "rbnCesEplCfgAdminStatus": rbnCesEplCfgAdminStatus,
       "rbnCesEplCfgRowStatus": rbnCesEplCfgRowStatus,
       "rbnCesEplStatsTable": rbnCesEplStatsTable,
       "rbnCesEplStatsEntry": rbnCesEplStatsEntry,
       "rbnCesEplStatsIndex": rbnCesEplStatsIndex,
       "rbnCesEplStatsEntryTime": rbnCesEplStatsEntryTime,
       "rbnCesEplStatsEntryTotalPktLossTime": rbnCesEplStatsEntryTotalPktLossTime,
       "rbnCesEplStatsExitTime": rbnCesEplStatsExitTime,
       "rbnCesEplStatsExitTotalPktLossTime": rbnCesEplStatsExitTotalPktLossTime,
       "rbnCesEplStatsCount": rbnCesEplStatsCount,
       "rbnCesEplStatsTotalCircuitTime": rbnCesEplStatsTotalCircuitTime,
       "rbnCesEplStatsTotalFailureRate": rbnCesEplStatsTotalFailureRate,
       "rbnCesEplStatsReset": rbnCesEplStatsReset,
       "rbnCesSlaInfoTable": rbnCesSlaInfoTable,
       "rbnCesSlaInfoEntry": rbnCesSlaInfoEntry,
       "rbnCesSlaInfoIndex": rbnCesSlaInfoIndex,
       "rbnCesSlaInfoLatestOutageTime": rbnCesSlaInfoLatestOutageTime,
       "rbnCesSlaInfoEntryLatestOutage": rbnCesSlaInfoEntryLatestOutage,
       "rbnCesSlaInfoExitLatestOutage": rbnCesSlaInfoExitLatestOutage,
       "rbnCesSlaInfoLastOutageTime": rbnCesSlaInfoLastOutageTime,
       "rbnCesSlaInfoLastUpTime": rbnCesSlaInfoLastUpTime,
       "rbnCesSlaInfoTotalOutageTime": rbnCesSlaInfoTotalOutageTime,
       "rbnCesSlaInfoTotalUpTime": rbnCesSlaInfoTotalUpTime,
       "rbnCesSlaInfoOutageCount": rbnCesSlaInfoOutageCount,
       "rbnCesSlaInfoReset": rbnCesSlaInfoReset,
       "rbnCesCardAlarmTable": rbnCesCardAlarmTable,
       "rbnCesCardAlarmEntry": rbnCesCardAlarmEntry,
       "rbnCesCardAlarmId": rbnCesCardAlarmId,
       "rbnCesCardAlarmNotificationEnable": rbnCesCardAlarmNotificationEnable,
       "rbnCesMIBConformance": rbnCesMIBConformance,
       "rbnCesMIBCompliances": rbnCesMIBCompliances,
       "rbnCesMIBCompliance": rbnCesMIBCompliance,
       "rbnCesMIBGroups": rbnCesMIBGroups,
       "rbnCesCfgGroup": rbnCesCfgGroup,
       "rbnCesStatsGroup": rbnCesStatsGroup,
       "rbnCesEplCfgGroup": rbnCesEplCfgGroup,
       "rbnCesEplStatsGroup": rbnCesEplStatsGroup,
       "rbnCesSlaInfoGroup": rbnCesSlaInfoGroup,
       "rbnCesCardAlarmGroup": rbnCesCardAlarmGroup}
)
