# SNMP MIB module (NTN-QOS-POLICY-AUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTN-QOS-POLICY-AUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:39 2024
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

(ntnQosIfParametersExt,) = mibBuilder.importSymbols(
    "NTN-QOS-POLICY-EXT-PIB",
    "ntnQosIfParametersExt")

(PolicyInstanceId,
 RoleCombination) = mibBuilder.importSymbols(
    "POLICY-FRAMEWORK-PIB",
    "PolicyInstanceId",
    "RoleCombination")

(qosTargetEntry,) = mibBuilder.importSymbols(
    "QOS-POLICY-IP-PIB",
    "qosTargetEntry")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(policy,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "policy")


# MODULE-IDENTITY

ntnQosPolicyAuxMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 5)
)
ntnQosPolicyAuxMib.setRevisions(
        ("2004-07-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtnQosInterfaceIdTable_Object = MibTable
ntnQosInterfaceIdTable = _NtnQosInterfaceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ntnQosInterfaceIdTable.setStatus("current")
_NtnQosInterfaceIdEntry_Object = MibTableRow
ntnQosInterfaceIdEntry = _NtnQosInterfaceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 4, 1)
)
ntnQosInterfaceIdEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-AUX-MIB", "ntnQosInterfaceIdIfIndex"),
)
if mibBuilder.loadTexts:
    ntnQosInterfaceIdEntry.setStatus("current")
_NtnQosInterfaceIdIfIndex_Type = InterfaceIndex
_NtnQosInterfaceIdIfIndex_Object = MibTableColumn
ntnQosInterfaceIdIfIndex = _NtnQosInterfaceIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 4, 1, 1),
    _NtnQosInterfaceIdIfIndex_Type()
)
ntnQosInterfaceIdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosInterfaceIdIfIndex.setStatus("current")
_NtnQosInterfaceIdRoleCombination_Type = RoleCombination
_NtnQosInterfaceIdRoleCombination_Object = MibTableColumn
ntnQosInterfaceIdRoleCombination = _NtnQosInterfaceIdRoleCombination_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 4, 1, 2),
    _NtnQosInterfaceIdRoleCombination_Type()
)
ntnQosInterfaceIdRoleCombination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceIdRoleCombination.setStatus("current")


class _NtnQosInterfaceIdStorageType_Type(StorageType):
    """Custom type ntnQosInterfaceIdStorageType based on StorageType"""


_NtnQosInterfaceIdStorageType_Object = MibTableColumn
ntnQosInterfaceIdStorageType = _NtnQosInterfaceIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 4, 1, 3),
    _NtnQosInterfaceIdStorageType_Type()
)
ntnQosInterfaceIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceIdStorageType.setStatus("current")
_NtnQosInterfaceIdStatus_Type = RowStatus
_NtnQosInterfaceIdStatus_Object = MibTableColumn
ntnQosInterfaceIdStatus = _NtnQosInterfaceIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 4, 1, 4),
    _NtnQosInterfaceIdStatus_Type()
)
ntnQosInterfaceIdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceIdStatus.setStatus("current")
_NtnQosInterfaceIdQueueSet_Type = PolicyInstanceId
_NtnQosInterfaceIdQueueSet_Object = MibTableColumn
ntnQosInterfaceIdQueueSet = _NtnQosInterfaceIdQueueSet_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 4, 1, 5),
    _NtnQosInterfaceIdQueueSet_Type()
)
ntnQosInterfaceIdQueueSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceIdQueueSet.setStatus("current")
_NtnQosPolicyAuxObjects_ObjectIdentity = ObjectIdentity
ntnQosPolicyAuxObjects = _NtnQosPolicyAuxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1)
)
_NtnQosConfig_ObjectIdentity = ObjectIdentity
ntnQosConfig = _NtnQosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1)
)


class _NtnQosConfigDynamicMgmt_Type(Integer32):
    """Custom type ntnQosConfigDynamicMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NtnQosConfigDynamicMgmt_Type.__name__ = "Integer32"
_NtnQosConfigDynamicMgmt_Object = MibScalar
ntnQosConfigDynamicMgmt = _NtnQosConfigDynamicMgmt_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 1),
    _NtnQosConfigDynamicMgmt_Type()
)
ntnQosConfigDynamicMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDynamicMgmt.setStatus("current")


class _NtnQosConfigQpaState_Type(Integer32):
    """Custom type ntnQosConfigQpaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 2),
          ("resetToDefault", 3),
          ("running", 1))
    )


_NtnQosConfigQpaState_Type.__name__ = "Integer32"
_NtnQosConfigQpaState_Object = MibScalar
ntnQosConfigQpaState = _NtnQosConfigQpaState_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 2),
    _NtnQosConfigQpaState_Type()
)
ntnQosConfigQpaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigQpaState.setStatus("current")


class _NtnQosConfigQpaRetryTimer_Type(Integer32):
    """Custom type ntnQosConfigQpaRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 86400),
    )


_NtnQosConfigQpaRetryTimer_Type.__name__ = "Integer32"
_NtnQosConfigQpaRetryTimer_Object = MibScalar
ntnQosConfigQpaRetryTimer = _NtnQosConfigQpaRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 3),
    _NtnQosConfigQpaRetryTimer_Type()
)
ntnQosConfigQpaRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigQpaRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosConfigQpaRetryTimer.setUnits("seconds")


class _NtnQosConfigAllowPacketReordering_Type(TruthValue):
    """Custom type ntnQosConfigAllowPacketReordering based on TruthValue"""


_NtnQosConfigAllowPacketReordering_Object = MibScalar
ntnQosConfigAllowPacketReordering = _NtnQosConfigAllowPacketReordering_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 4),
    _NtnQosConfigAllowPacketReordering_Type()
)
ntnQosConfigAllowPacketReordering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigAllowPacketReordering.setStatus("current")


class _NtnQosConfigMaintainPolicingStats_Type(TruthValue):
    """Custom type ntnQosConfigMaintainPolicingStats based on TruthValue"""


_NtnQosConfigMaintainPolicingStats_Object = MibScalar
ntnQosConfigMaintainPolicingStats = _NtnQosConfigMaintainPolicingStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 5),
    _NtnQosConfigMaintainPolicingStats_Type()
)
ntnQosConfigMaintainPolicingStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigMaintainPolicingStats.setStatus("current")


class _NtnQosConfigIfcClassRestrictions_Type(Integer32):
    """Custom type ntnQosConfigIfcClassRestrictions based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowAllIfcClasses", 3),
          ("unrestrictedAndTrusted", 2),
          ("unrestrictedOnly", 1))
    )


_NtnQosConfigIfcClassRestrictions_Type.__name__ = "Integer32"
_NtnQosConfigIfcClassRestrictions_Object = MibScalar
ntnQosConfigIfcClassRestrictions = _NtnQosConfigIfcClassRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 6),
    _NtnQosConfigIfcClassRestrictions_Type()
)
ntnQosConfigIfcClassRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigIfcClassRestrictions.setStatus("current")
_NtnQosConfigDefaultOutOfProfileAction_Type = PolicyInstanceId
_NtnQosConfigDefaultOutOfProfileAction_Object = MibScalar
ntnQosConfigDefaultOutOfProfileAction = _NtnQosConfigDefaultOutOfProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 7),
    _NtnQosConfigDefaultOutOfProfileAction_Type()
)
ntnQosConfigDefaultOutOfProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDefaultOutOfProfileAction.setStatus("current")


class _NtnQosConfigPolicyCfgRestrictionMode_Type(Integer32):
    """Custom type ntnQosConfigPolicyCfgRestrictionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l3PolicyRestrictions", 2),
          ("noPolicyRestrictions", 1))
    )


_NtnQosConfigPolicyCfgRestrictionMode_Type.__name__ = "Integer32"
_NtnQosConfigPolicyCfgRestrictionMode_Object = MibScalar
ntnQosConfigPolicyCfgRestrictionMode = _NtnQosConfigPolicyCfgRestrictionMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 1, 8),
    _NtnQosConfigPolicyCfgRestrictionMode_Type()
)
ntnQosConfigPolicyCfgRestrictionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigPolicyCfgRestrictionMode.setStatus("current")
_NtnQosStatistics_ObjectIdentity = ObjectIdentity
ntnQosStatistics = _NtnQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2)
)
_NtnQosTargetStatsTable_Object = MibTable
ntnQosTargetStatsTable = _NtnQosTargetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntnQosTargetStatsTable.setStatus("current")
_NtnQosTargetStatsEntry_Object = MibTableRow
ntnQosTargetStatsEntry = _NtnQosTargetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntnQosTargetStatsEntry.setStatus("current")
_NtnQosTargetStatsPktHits_Type = Counter32
_NtnQosTargetStatsPktHits_Object = MibTableColumn
ntnQosTargetStatsPktHits = _NtnQosTargetStatsPktHits_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 1),
    _NtnQosTargetStatsPktHits_Type()
)
ntnQosTargetStatsPktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsPktHits.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsPktHits.setUnits("packets")
_NtnQosTargetStatsOverflowPktHits_Type = Counter32
_NtnQosTargetStatsOverflowPktHits_Object = MibTableColumn
ntnQosTargetStatsOverflowPktHits = _NtnQosTargetStatsOverflowPktHits_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 2),
    _NtnQosTargetStatsOverflowPktHits_Type()
)
ntnQosTargetStatsOverflowPktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOverflowPktHits.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOverflowPktHits.setUnits("packets")
_NtnQosTargetStatsHCPktHits_Type = Counter64
_NtnQosTargetStatsHCPktHits_Object = MibTableColumn
ntnQosTargetStatsHCPktHits = _NtnQosTargetStatsHCPktHits_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 3),
    _NtnQosTargetStatsHCPktHits_Type()
)
ntnQosTargetStatsHCPktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsHCPktHits.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsHCPktHits.setUnits("packets")
_NtnQosTargetStatsTotalOctets_Type = Counter32
_NtnQosTargetStatsTotalOctets_Object = MibTableColumn
ntnQosTargetStatsTotalOctets = _NtnQosTargetStatsTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 4),
    _NtnQosTargetStatsTotalOctets_Type()
)
ntnQosTargetStatsTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsTotalOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsTotalOctets.setUnits("octets")
_NtnQosTargetStatsTotalOverflowOctets_Type = Counter32
_NtnQosTargetStatsTotalOverflowOctets_Object = MibTableColumn
ntnQosTargetStatsTotalOverflowOctets = _NtnQosTargetStatsTotalOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 5),
    _NtnQosTargetStatsTotalOverflowOctets_Type()
)
ntnQosTargetStatsTotalOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsTotalOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsTotalOverflowOctets.setUnits("octets")
_NtnQosTargetStatsTotalHCOctets_Type = Counter64
_NtnQosTargetStatsTotalHCOctets_Object = MibTableColumn
ntnQosTargetStatsTotalHCOctets = _NtnQosTargetStatsTotalHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 6),
    _NtnQosTargetStatsTotalHCOctets_Type()
)
ntnQosTargetStatsTotalHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsTotalHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsTotalHCOctets.setUnits("octets")
_NtnQosTargetStatsInProfOctets_Type = Counter32
_NtnQosTargetStatsInProfOctets_Object = MibTableColumn
ntnQosTargetStatsInProfOctets = _NtnQosTargetStatsInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 7),
    _NtnQosTargetStatsInProfOctets_Type()
)
ntnQosTargetStatsInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsInProfOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsInProfOctets.setUnits("octets")
_NtnQosTargetStatsInProfOverflowOctets_Type = Counter32
_NtnQosTargetStatsInProfOverflowOctets_Object = MibTableColumn
ntnQosTargetStatsInProfOverflowOctets = _NtnQosTargetStatsInProfOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 8),
    _NtnQosTargetStatsInProfOverflowOctets_Type()
)
ntnQosTargetStatsInProfOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsInProfOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsInProfOverflowOctets.setUnits("octets")
_NtnQosTargetStatsInProfHCOctets_Type = Counter64
_NtnQosTargetStatsInProfHCOctets_Object = MibTableColumn
ntnQosTargetStatsInProfHCOctets = _NtnQosTargetStatsInProfHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 9),
    _NtnQosTargetStatsInProfHCOctets_Type()
)
ntnQosTargetStatsInProfHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsInProfHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsInProfHCOctets.setUnits("octets")
_NtnQosTargetStatsOutProfOctets_Type = Counter32
_NtnQosTargetStatsOutProfOctets_Object = MibTableColumn
ntnQosTargetStatsOutProfOctets = _NtnQosTargetStatsOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 10),
    _NtnQosTargetStatsOutProfOctets_Type()
)
ntnQosTargetStatsOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOutProfOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOutProfOctets.setUnits("octets")
_NtnQosTargetStatsOutProfOverflowOctets_Type = Counter32
_NtnQosTargetStatsOutProfOverflowOctets_Object = MibTableColumn
ntnQosTargetStatsOutProfOverflowOctets = _NtnQosTargetStatsOutProfOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 11),
    _NtnQosTargetStatsOutProfOverflowOctets_Type()
)
ntnQosTargetStatsOutProfOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOutProfOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOutProfOverflowOctets.setUnits("octets")
_NtnQosTargetStatsOutProfHCOctets_Type = Counter64
_NtnQosTargetStatsOutProfHCOctets_Object = MibTableColumn
ntnQosTargetStatsOutProfHCOctets = _NtnQosTargetStatsOutProfHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 12),
    _NtnQosTargetStatsOutProfHCOctets_Type()
)
ntnQosTargetStatsOutProfHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOutProfHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOutProfHCOctets.setUnits("octets")
_NtnQosTargetStatsTrackStatistics_Type = TruthValue
_NtnQosTargetStatsTrackStatistics_Object = MibTableColumn
ntnQosTargetStatsTrackStatistics = _NtnQosTargetStatsTrackStatistics_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 13),
    _NtnQosTargetStatsTrackStatistics_Type()
)
ntnQosTargetStatsTrackStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosTargetStatsTrackStatistics.setStatus("current")
_NtnQosTargetStatsShapingQDrops_Type = Counter32
_NtnQosTargetStatsShapingQDrops_Object = MibTableColumn
ntnQosTargetStatsShapingQDrops = _NtnQosTargetStatsShapingQDrops_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 14),
    _NtnQosTargetStatsShapingQDrops_Type()
)
ntnQosTargetStatsShapingQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsShapingQDrops.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsShapingQDrops.setUnits("packets")
_NtnQosTargetStatsOverflowShapingQDrops_Type = Counter32
_NtnQosTargetStatsOverflowShapingQDrops_Object = MibTableColumn
ntnQosTargetStatsOverflowShapingQDrops = _NtnQosTargetStatsOverflowShapingQDrops_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 15),
    _NtnQosTargetStatsOverflowShapingQDrops_Type()
)
ntnQosTargetStatsOverflowShapingQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOverflowShapingQDrops.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsOverflowShapingQDrops.setUnits("packets")
_NtnQosTargetStatsHCShapingQDrops_Type = Counter64
_NtnQosTargetStatsHCShapingQDrops_Object = MibTableColumn
ntnQosTargetStatsHCShapingQDrops = _NtnQosTargetStatsHCShapingQDrops_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 1, 2, 1, 1, 16),
    _NtnQosTargetStatsHCShapingQDrops_Type()
)
ntnQosTargetStatsHCShapingQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTargetStatsHCShapingQDrops.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTargetStatsHCShapingQDrops.setUnits("packets")
_NtnQosPolicyAuxConformance_ObjectIdentity = ObjectIdentity
ntnQosPolicyAuxConformance = _NtnQosPolicyAuxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 2)
)
_NtnQosCompliances_ObjectIdentity = ObjectIdentity
ntnQosCompliances = _NtnQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 2, 1)
)
_NtnQosGroups_ObjectIdentity = ObjectIdentity
ntnQosGroups = _NtnQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 2, 2)
)
qosTargetEntry.registerAugmentions(
    ("NTN-QOS-POLICY-AUX-MIB",
     "ntnQosTargetStatsEntry")
)
ntnQosTargetStatsEntry.setIndexNames(*qosTargetEntry.getIndexNames())

# Managed Objects groups

ntnQosConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 2, 2, 1)
)
ntnQosConfigGroup.setObjects(
      *(("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigDynamicMgmt"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigQpaState"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigQpaRetryTimer"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigAllowPacketReordering"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigMaintainPolicingStats"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigIfcClassRestrictions"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigDefaultOutOfProfileAction"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosConfigPolicyCfgRestrictionMode"))
)
if mibBuilder.loadTexts:
    ntnQosConfigGroup.setStatus("current")

ntnQosInterfaceIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 2, 2, 2)
)
ntnQosInterfaceIdGroup.setObjects(
      *(("NTN-QOS-POLICY-AUX-MIB", "ntnQosInterfaceIdRoleCombination"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosInterfaceIdStorageType"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosInterfaceIdStatus"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosInterfaceIdQueueSet"))
)
if mibBuilder.loadTexts:
    ntnQosInterfaceIdGroup.setStatus("current")

ntnQosTargetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 2, 2, 3)
)
ntnQosTargetStatsGroup.setObjects(
      *(("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsPktHits"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsOverflowPktHits"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsHCPktHits"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsTotalOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsTotalOverflowOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsTotalHCOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsInProfOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsInProfOverflowOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsInProfHCOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsOutProfOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsOutProfOverflowOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsOutProfHCOctets"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsTrackStatistics"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsShapingQDrops"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsOverflowShapingQDrops"),
        ("NTN-QOS-POLICY-AUX-MIB", "ntnQosTargetStatsHCShapingQDrops"))
)
if mibBuilder.loadTexts:
    ntnQosTargetStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntnQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 4, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntnQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTN-QOS-POLICY-AUX-MIB",
    **{"ntnQosInterfaceIdTable": ntnQosInterfaceIdTable,
       "ntnQosInterfaceIdEntry": ntnQosInterfaceIdEntry,
       "ntnQosInterfaceIdIfIndex": ntnQosInterfaceIdIfIndex,
       "ntnQosInterfaceIdRoleCombination": ntnQosInterfaceIdRoleCombination,
       "ntnQosInterfaceIdStorageType": ntnQosInterfaceIdStorageType,
       "ntnQosInterfaceIdStatus": ntnQosInterfaceIdStatus,
       "ntnQosInterfaceIdQueueSet": ntnQosInterfaceIdQueueSet,
       "ntnQosPolicyAuxMib": ntnQosPolicyAuxMib,
       "ntnQosPolicyAuxObjects": ntnQosPolicyAuxObjects,
       "ntnQosConfig": ntnQosConfig,
       "ntnQosConfigDynamicMgmt": ntnQosConfigDynamicMgmt,
       "ntnQosConfigQpaState": ntnQosConfigQpaState,
       "ntnQosConfigQpaRetryTimer": ntnQosConfigQpaRetryTimer,
       "ntnQosConfigAllowPacketReordering": ntnQosConfigAllowPacketReordering,
       "ntnQosConfigMaintainPolicingStats": ntnQosConfigMaintainPolicingStats,
       "ntnQosConfigIfcClassRestrictions": ntnQosConfigIfcClassRestrictions,
       "ntnQosConfigDefaultOutOfProfileAction": ntnQosConfigDefaultOutOfProfileAction,
       "ntnQosConfigPolicyCfgRestrictionMode": ntnQosConfigPolicyCfgRestrictionMode,
       "ntnQosStatistics": ntnQosStatistics,
       "ntnQosTargetStatsTable": ntnQosTargetStatsTable,
       "ntnQosTargetStatsEntry": ntnQosTargetStatsEntry,
       "ntnQosTargetStatsPktHits": ntnQosTargetStatsPktHits,
       "ntnQosTargetStatsOverflowPktHits": ntnQosTargetStatsOverflowPktHits,
       "ntnQosTargetStatsHCPktHits": ntnQosTargetStatsHCPktHits,
       "ntnQosTargetStatsTotalOctets": ntnQosTargetStatsTotalOctets,
       "ntnQosTargetStatsTotalOverflowOctets": ntnQosTargetStatsTotalOverflowOctets,
       "ntnQosTargetStatsTotalHCOctets": ntnQosTargetStatsTotalHCOctets,
       "ntnQosTargetStatsInProfOctets": ntnQosTargetStatsInProfOctets,
       "ntnQosTargetStatsInProfOverflowOctets": ntnQosTargetStatsInProfOverflowOctets,
       "ntnQosTargetStatsInProfHCOctets": ntnQosTargetStatsInProfHCOctets,
       "ntnQosTargetStatsOutProfOctets": ntnQosTargetStatsOutProfOctets,
       "ntnQosTargetStatsOutProfOverflowOctets": ntnQosTargetStatsOutProfOverflowOctets,
       "ntnQosTargetStatsOutProfHCOctets": ntnQosTargetStatsOutProfHCOctets,
       "ntnQosTargetStatsTrackStatistics": ntnQosTargetStatsTrackStatistics,
       "ntnQosTargetStatsShapingQDrops": ntnQosTargetStatsShapingQDrops,
       "ntnQosTargetStatsOverflowShapingQDrops": ntnQosTargetStatsOverflowShapingQDrops,
       "ntnQosTargetStatsHCShapingQDrops": ntnQosTargetStatsHCShapingQDrops,
       "ntnQosPolicyAuxConformance": ntnQosPolicyAuxConformance,
       "ntnQosCompliances": ntnQosCompliances,
       "ntnQosCompliance": ntnQosCompliance,
       "ntnQosGroups": ntnQosGroups,
       "ntnQosConfigGroup": ntnQosConfigGroup,
       "ntnQosInterfaceIdGroup": ntnQosInterfaceIdGroup,
       "ntnQosTargetStatsGroup": ntnQosTargetStatsGroup}
)
