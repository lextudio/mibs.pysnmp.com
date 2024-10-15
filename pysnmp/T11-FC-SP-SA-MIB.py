# SNMP MIB module (T11-FC-SP-SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-SP-SA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:37 2024
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

(FcAddressIdOrZero,
 fcmInstanceIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcAddressIdOrZero",
    "fcmInstanceIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(T11FcRoutingControl,
 T11FcSaDirection,
 T11FcSpLifetimeLeft,
 T11FcSpLifetimeLeftUnits,
 T11FcSpPrecedence,
 T11FcSpSecurityProtocolId,
 T11FcSpTransforms,
 T11FcSpType,
 T11FcSpiIndex) = mibBuilder.importSymbols(
    "T11-FC-SP-TC-MIB",
    "T11FcRoutingControl",
    "T11FcSaDirection",
    "T11FcSpLifetimeLeft",
    "T11FcSpLifetimeLeftUnits",
    "T11FcSpPrecedence",
    "T11FcSpSecurityProtocolId",
    "T11FcSpTransforms",
    "T11FcSpType",
    "T11FcSpiIndex")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcSpSaMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 179)
)
t11FcSpSaMIB.setRevisions(
        ("2008-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11FcSpSaMIBNotifications_ObjectIdentity = ObjectIdentity
t11FcSpSaMIBNotifications = _T11FcSpSaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 0)
)
_T11FcSpSaMIBObjects_ObjectIdentity = ObjectIdentity
t11FcSpSaMIBObjects = _T11FcSpSaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 1)
)
_T11FcSpSaBase_ObjectIdentity = ObjectIdentity
t11FcSpSaBase = _T11FcSpSaBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 1, 1)
)
_T11FcSpSaIfTable_Object = MibTable
t11FcSpSaIfTable = _T11FcSpSaIfTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpSaIfTable.setStatus("current")
_T11FcSpSaIfEntry_Object = MibTableRow
t11FcSpSaIfEntry = _T11FcSpSaIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1)
)
t11FcSpSaIfEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpSaIfEntry.setStatus("current")
_T11FcSpSaIfIndex_Type = InterfaceIndexOrZero
_T11FcSpSaIfIndex_Object = MibTableColumn
t11FcSpSaIfIndex = _T11FcSpSaIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 1),
    _T11FcSpSaIfIndex_Type()
)
t11FcSpSaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaIfIndex.setStatus("current")
_T11FcSpSaIfFabricIndex_Type = T11FabricIndex
_T11FcSpSaIfFabricIndex_Object = MibTableColumn
t11FcSpSaIfFabricIndex = _T11FcSpSaIfFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 2),
    _T11FcSpSaIfFabricIndex_Type()
)
t11FcSpSaIfFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaIfFabricIndex.setStatus("current")
_T11FcSpSaIfEspHeaderCapab_Type = T11FcSpTransforms
_T11FcSpSaIfEspHeaderCapab_Object = MibTableColumn
t11FcSpSaIfEspHeaderCapab = _T11FcSpSaIfEspHeaderCapab_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 3),
    _T11FcSpSaIfEspHeaderCapab_Type()
)
t11FcSpSaIfEspHeaderCapab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfEspHeaderCapab.setStatus("current")
_T11FcSpSaIfCTAuthCapab_Type = T11FcSpTransforms
_T11FcSpSaIfCTAuthCapab_Object = MibTableColumn
t11FcSpSaIfCTAuthCapab = _T11FcSpSaIfCTAuthCapab_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 4),
    _T11FcSpSaIfCTAuthCapab_Type()
)
t11FcSpSaIfCTAuthCapab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfCTAuthCapab.setStatus("current")
_T11FcSpSaIfIKEv2Capab_Type = T11FcSpTransforms
_T11FcSpSaIfIKEv2Capab_Object = MibTableColumn
t11FcSpSaIfIKEv2Capab = _T11FcSpSaIfIKEv2Capab_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 5),
    _T11FcSpSaIfIKEv2Capab_Type()
)
t11FcSpSaIfIKEv2Capab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfIKEv2Capab.setStatus("current")
_T11FcSpSaIfIkev2AuthCapab_Type = TruthValue
_T11FcSpSaIfIkev2AuthCapab_Object = MibTableColumn
t11FcSpSaIfIkev2AuthCapab = _T11FcSpSaIfIkev2AuthCapab_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 6),
    _T11FcSpSaIfIkev2AuthCapab_Type()
)
t11FcSpSaIfIkev2AuthCapab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfIkev2AuthCapab.setStatus("current")
_T11FcSpSaIfStorageType_Type = StorageType
_T11FcSpSaIfStorageType_Object = MibTableColumn
t11FcSpSaIfStorageType = _T11FcSpSaIfStorageType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 7),
    _T11FcSpSaIfStorageType_Type()
)
t11FcSpSaIfStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaIfStorageType.setStatus("current")
_T11FcSpSaIfReplayPrevention_Type = TruthValue
_T11FcSpSaIfReplayPrevention_Object = MibTableColumn
t11FcSpSaIfReplayPrevention = _T11FcSpSaIfReplayPrevention_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 8),
    _T11FcSpSaIfReplayPrevention_Type()
)
t11FcSpSaIfReplayPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaIfReplayPrevention.setStatus("current")
_T11FcSpSaIfReplayWindowSize_Type = Unsigned32
_T11FcSpSaIfReplayWindowSize_Object = MibTableColumn
t11FcSpSaIfReplayWindowSize = _T11FcSpSaIfReplayWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 9),
    _T11FcSpSaIfReplayWindowSize_Type()
)
t11FcSpSaIfReplayWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaIfReplayWindowSize.setStatus("current")
_T11FcSpSaIfDeadPeerDetections_Type = Counter32
_T11FcSpSaIfDeadPeerDetections_Object = MibTableColumn
t11FcSpSaIfDeadPeerDetections = _T11FcSpSaIfDeadPeerDetections_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 10),
    _T11FcSpSaIfDeadPeerDetections_Type()
)
t11FcSpSaIfDeadPeerDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfDeadPeerDetections.setStatus("current")


class _T11FcSpSaIfTerminateAllSas_Type(Integer32):
    """Custom type t11FcSpSaIfTerminateAllSas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("terminate", 2))
    )


_T11FcSpSaIfTerminateAllSas_Type.__name__ = "Integer32"
_T11FcSpSaIfTerminateAllSas_Object = MibTableColumn
t11FcSpSaIfTerminateAllSas = _T11FcSpSaIfTerminateAllSas_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 11),
    _T11FcSpSaIfTerminateAllSas_Type()
)
t11FcSpSaIfTerminateAllSas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaIfTerminateAllSas.setStatus("current")
_T11FcSpSaIfOutDrops_Type = Counter64
_T11FcSpSaIfOutDrops_Object = MibTableColumn
t11FcSpSaIfOutDrops = _T11FcSpSaIfOutDrops_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 12),
    _T11FcSpSaIfOutDrops_Type()
)
t11FcSpSaIfOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfOutDrops.setStatus("current")
_T11FcSpSaIfOutBypasses_Type = Counter64
_T11FcSpSaIfOutBypasses_Object = MibTableColumn
t11FcSpSaIfOutBypasses = _T11FcSpSaIfOutBypasses_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 13),
    _T11FcSpSaIfOutBypasses_Type()
)
t11FcSpSaIfOutBypasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfOutBypasses.setStatus("current")
_T11FcSpSaIfOutProcesses_Type = Counter64
_T11FcSpSaIfOutProcesses_Object = MibTableColumn
t11FcSpSaIfOutProcesses = _T11FcSpSaIfOutProcesses_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 14),
    _T11FcSpSaIfOutProcesses_Type()
)
t11FcSpSaIfOutProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfOutProcesses.setStatus("current")
_T11FcSpSaIfOutUnMatcheds_Type = Counter64
_T11FcSpSaIfOutUnMatcheds_Object = MibTableColumn
t11FcSpSaIfOutUnMatcheds = _T11FcSpSaIfOutUnMatcheds_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 15),
    _T11FcSpSaIfOutUnMatcheds_Type()
)
t11FcSpSaIfOutUnMatcheds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfOutUnMatcheds.setStatus("current")
_T11FcSpSaIfInUnprotUnmtchDrops_Type = Counter64
_T11FcSpSaIfInUnprotUnmtchDrops_Object = MibTableColumn
t11FcSpSaIfInUnprotUnmtchDrops = _T11FcSpSaIfInUnprotUnmtchDrops_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 16),
    _T11FcSpSaIfInUnprotUnmtchDrops_Type()
)
t11FcSpSaIfInUnprotUnmtchDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfInUnprotUnmtchDrops.setStatus("current")
_T11FcSpSaIfInDetReplays_Type = Counter64
_T11FcSpSaIfInDetReplays_Object = MibTableColumn
t11FcSpSaIfInDetReplays = _T11FcSpSaIfInDetReplays_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 17),
    _T11FcSpSaIfInDetReplays_Type()
)
t11FcSpSaIfInDetReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfInDetReplays.setStatus("current")
_T11FcSpSaIfInUnprotMtchDrops_Type = Counter64
_T11FcSpSaIfInUnprotMtchDrops_Object = MibTableColumn
t11FcSpSaIfInUnprotMtchDrops = _T11FcSpSaIfInUnprotMtchDrops_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 18),
    _T11FcSpSaIfInUnprotMtchDrops_Type()
)
t11FcSpSaIfInUnprotMtchDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfInUnprotMtchDrops.setStatus("current")
_T11FcSpSaIfInBadXforms_Type = Counter64
_T11FcSpSaIfInBadXforms_Object = MibTableColumn
t11FcSpSaIfInBadXforms = _T11FcSpSaIfInBadXforms_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 19),
    _T11FcSpSaIfInBadXforms_Type()
)
t11FcSpSaIfInBadXforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfInBadXforms.setStatus("current")
_T11FcSpSaIfInGoodXforms_Type = Counter64
_T11FcSpSaIfInGoodXforms_Object = MibTableColumn
t11FcSpSaIfInGoodXforms = _T11FcSpSaIfInGoodXforms_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 20),
    _T11FcSpSaIfInGoodXforms_Type()
)
t11FcSpSaIfInGoodXforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfInGoodXforms.setStatus("current")
_T11FcSpSaIfInProtUnmtchs_Type = Counter64
_T11FcSpSaIfInProtUnmtchs_Object = MibTableColumn
t11FcSpSaIfInProtUnmtchs = _T11FcSpSaIfInProtUnmtchs_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 1, 1, 1, 21),
    _T11FcSpSaIfInProtUnmtchs_Type()
)
t11FcSpSaIfInProtUnmtchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaIfInProtUnmtchs.setStatus("current")
_T11FcSpSaConfig_ObjectIdentity = ObjectIdentity
t11FcSpSaConfig = _T11FcSpSaConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 1, 2)
)
_T11FcSpSaPropTable_Object = MibTable
t11FcSpSaPropTable = _T11FcSpSaPropTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcSpSaPropTable.setStatus("current")
_T11FcSpSaPropEntry_Object = MibTableRow
t11FcSpSaPropEntry = _T11FcSpSaPropEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1)
)
t11FcSpSaPropEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaPropIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpSaPropEntry.setStatus("current")


class _T11FcSpSaPropIndex_Type(Unsigned32):
    """Custom type t11FcSpSaPropIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaPropIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaPropIndex_Object = MibTableColumn
t11FcSpSaPropIndex = _T11FcSpSaPropIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1, 1),
    _T11FcSpSaPropIndex_Type()
)
t11FcSpSaPropIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaPropIndex.setStatus("current")
_T11FcSpSaPropSecurityProt_Type = T11FcSpSecurityProtocolId
_T11FcSpSaPropSecurityProt_Object = MibTableColumn
t11FcSpSaPropSecurityProt = _T11FcSpSaPropSecurityProt_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1, 2),
    _T11FcSpSaPropSecurityProt_Type()
)
t11FcSpSaPropSecurityProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaPropSecurityProt.setStatus("current")
_T11FcSpSaPropTSelListIndex_Type = Unsigned32
_T11FcSpSaPropTSelListIndex_Object = MibTableColumn
t11FcSpSaPropTSelListIndex = _T11FcSpSaPropTSelListIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1, 3),
    _T11FcSpSaPropTSelListIndex_Type()
)
t11FcSpSaPropTSelListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaPropTSelListIndex.setStatus("current")
_T11FcSpSaPropTransListIndex_Type = Unsigned32
_T11FcSpSaPropTransListIndex_Object = MibTableColumn
t11FcSpSaPropTransListIndex = _T11FcSpSaPropTransListIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1, 4),
    _T11FcSpSaPropTransListIndex_Type()
)
t11FcSpSaPropTransListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaPropTransListIndex.setStatus("current")


class _T11FcSpSaPropAcceptAlgorithm_Type(Integer32):
    """Custom type t11FcSpSaPropAcceptAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intersection", 1),
          ("other", 3),
          ("union", 2))
    )


_T11FcSpSaPropAcceptAlgorithm_Type.__name__ = "Integer32"
_T11FcSpSaPropAcceptAlgorithm_Object = MibTableColumn
t11FcSpSaPropAcceptAlgorithm = _T11FcSpSaPropAcceptAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1, 5),
    _T11FcSpSaPropAcceptAlgorithm_Type()
)
t11FcSpSaPropAcceptAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaPropAcceptAlgorithm.setStatus("current")
_T11FcSpSaPropOutMatchSucceeds_Type = Counter64
_T11FcSpSaPropOutMatchSucceeds_Object = MibTableColumn
t11FcSpSaPropOutMatchSucceeds = _T11FcSpSaPropOutMatchSucceeds_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1, 6),
    _T11FcSpSaPropOutMatchSucceeds_Type()
)
t11FcSpSaPropOutMatchSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPropOutMatchSucceeds.setStatus("current")
_T11FcSpSaPropRowStatus_Type = RowStatus
_T11FcSpSaPropRowStatus_Object = MibTableColumn
t11FcSpSaPropRowStatus = _T11FcSpSaPropRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 1, 1, 7),
    _T11FcSpSaPropRowStatus_Type()
)
t11FcSpSaPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaPropRowStatus.setStatus("current")
_T11FcSpSaTSelPropTable_Object = MibTable
t11FcSpSaTSelPropTable = _T11FcSpSaTSelPropTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2)
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropTable.setStatus("current")
_T11FcSpSaTSelPropEntry_Object = MibTableRow
t11FcSpSaTSelPropEntry = _T11FcSpSaTSelPropEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1)
)
t11FcSpSaTSelPropEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropListIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropPrecedence"),
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropEntry.setStatus("current")


class _T11FcSpSaTSelPropListIndex_Type(Unsigned32):
    """Custom type t11FcSpSaTSelPropListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaTSelPropListIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaTSelPropListIndex_Object = MibTableColumn
t11FcSpSaTSelPropListIndex = _T11FcSpSaTSelPropListIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 1),
    _T11FcSpSaTSelPropListIndex_Type()
)
t11FcSpSaTSelPropListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropListIndex.setStatus("current")
_T11FcSpSaTSelPropPrecedence_Type = T11FcSpPrecedence
_T11FcSpSaTSelPropPrecedence_Object = MibTableColumn
t11FcSpSaTSelPropPrecedence = _T11FcSpSaTSelPropPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 2),
    _T11FcSpSaTSelPropPrecedence_Type()
)
t11FcSpSaTSelPropPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropPrecedence.setStatus("current")


class _T11FcSpSaTSelPropDirection_Type(T11FcSaDirection):
    """Custom type t11FcSpSaTSelPropDirection based on T11FcSaDirection"""


_T11FcSpSaTSelPropDirection_Object = MibTableColumn
t11FcSpSaTSelPropDirection = _T11FcSpSaTSelPropDirection_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 3),
    _T11FcSpSaTSelPropDirection_Type()
)
t11FcSpSaTSelPropDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropDirection.setStatus("current")


class _T11FcSpSaTSelPropStartSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelPropStartSrcAddr based on FcAddressIdOrZero"""
    defaultHexValue = "000000"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelPropStartSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelPropStartSrcAddr_Object = MibTableColumn
t11FcSpSaTSelPropStartSrcAddr = _T11FcSpSaTSelPropStartSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 4),
    _T11FcSpSaTSelPropStartSrcAddr_Type()
)
t11FcSpSaTSelPropStartSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropStartSrcAddr.setStatus("current")


class _T11FcSpSaTSelPropEndSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelPropEndSrcAddr based on FcAddressIdOrZero"""
    defaultHexValue = "FFFFFF"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelPropEndSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelPropEndSrcAddr_Object = MibTableColumn
t11FcSpSaTSelPropEndSrcAddr = _T11FcSpSaTSelPropEndSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 5),
    _T11FcSpSaTSelPropEndSrcAddr_Type()
)
t11FcSpSaTSelPropEndSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropEndSrcAddr.setStatus("current")


class _T11FcSpSaTSelPropStartDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelPropStartDstAddr based on FcAddressIdOrZero"""
    defaultHexValue = "000000"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelPropStartDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelPropStartDstAddr_Object = MibTableColumn
t11FcSpSaTSelPropStartDstAddr = _T11FcSpSaTSelPropStartDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 6),
    _T11FcSpSaTSelPropStartDstAddr_Type()
)
t11FcSpSaTSelPropStartDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropStartDstAddr.setStatus("current")


class _T11FcSpSaTSelPropEndDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelPropEndDstAddr based on FcAddressIdOrZero"""
    defaultHexValue = "FFFFFF"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelPropEndDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelPropEndDstAddr_Object = MibTableColumn
t11FcSpSaTSelPropEndDstAddr = _T11FcSpSaTSelPropEndDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 7),
    _T11FcSpSaTSelPropEndDstAddr_Type()
)
t11FcSpSaTSelPropEndDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropEndDstAddr.setStatus("current")


class _T11FcSpSaTSelPropStartRCtl_Type(T11FcRoutingControl):
    """Custom type t11FcSpSaTSelPropStartRCtl based on T11FcRoutingControl"""
    defaultHexValue = "00"


_T11FcSpSaTSelPropStartRCtl_Object = MibTableColumn
t11FcSpSaTSelPropStartRCtl = _T11FcSpSaTSelPropStartRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 8),
    _T11FcSpSaTSelPropStartRCtl_Type()
)
t11FcSpSaTSelPropStartRCtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropStartRCtl.setStatus("current")


class _T11FcSpSaTSelPropEndRCtl_Type(T11FcRoutingControl):
    """Custom type t11FcSpSaTSelPropEndRCtl based on T11FcRoutingControl"""
    defaultHexValue = "FF"


_T11FcSpSaTSelPropEndRCtl_Object = MibTableColumn
t11FcSpSaTSelPropEndRCtl = _T11FcSpSaTSelPropEndRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 9),
    _T11FcSpSaTSelPropEndRCtl_Type()
)
t11FcSpSaTSelPropEndRCtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropEndRCtl.setStatus("current")


class _T11FcSpSaTSelPropStartType_Type(T11FcSpType):
    """Custom type t11FcSpSaTSelPropStartType based on T11FcSpType"""
    defaultHexValue = "0000"


_T11FcSpSaTSelPropStartType_Object = MibTableColumn
t11FcSpSaTSelPropStartType = _T11FcSpSaTSelPropStartType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 10),
    _T11FcSpSaTSelPropStartType_Type()
)
t11FcSpSaTSelPropStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropStartType.setStatus("current")


class _T11FcSpSaTSelPropEndType_Type(T11FcSpType):
    """Custom type t11FcSpSaTSelPropEndType based on T11FcSpType"""
    defaultHexValue = "FFFF"


_T11FcSpSaTSelPropEndType_Object = MibTableColumn
t11FcSpSaTSelPropEndType = _T11FcSpSaTSelPropEndType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 11),
    _T11FcSpSaTSelPropEndType_Type()
)
t11FcSpSaTSelPropEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropEndType.setStatus("current")
_T11FcSpSaTSelPropStorageType_Type = StorageType
_T11FcSpSaTSelPropStorageType_Object = MibTableColumn
t11FcSpSaTSelPropStorageType = _T11FcSpSaTSelPropStorageType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 12),
    _T11FcSpSaTSelPropStorageType_Type()
)
t11FcSpSaTSelPropStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropStorageType.setStatus("current")
_T11FcSpSaTSelPropRowStatus_Type = RowStatus
_T11FcSpSaTSelPropRowStatus_Object = MibTableColumn
t11FcSpSaTSelPropRowStatus = _T11FcSpSaTSelPropRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 2, 1, 13),
    _T11FcSpSaTSelPropRowStatus_Type()
)
t11FcSpSaTSelPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelPropRowStatus.setStatus("current")
_T11FcSpSaTransTable_Object = MibTable
t11FcSpSaTransTable = _T11FcSpSaTransTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3)
)
if mibBuilder.loadTexts:
    t11FcSpSaTransTable.setStatus("current")
_T11FcSpSaTransEntry_Object = MibTableRow
t11FcSpSaTransEntry = _T11FcSpSaTransEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1)
)
t11FcSpSaTransEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTransListIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTransIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpSaTransEntry.setStatus("current")


class _T11FcSpSaTransListIndex_Type(Unsigned32):
    """Custom type t11FcSpSaTransListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaTransListIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaTransListIndex_Object = MibTableColumn
t11FcSpSaTransListIndex = _T11FcSpSaTransListIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 1),
    _T11FcSpSaTransListIndex_Type()
)
t11FcSpSaTransListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTransListIndex.setStatus("current")


class _T11FcSpSaTransIndex_Type(Unsigned32):
    """Custom type t11FcSpSaTransIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaTransIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaTransIndex_Object = MibTableColumn
t11FcSpSaTransIndex = _T11FcSpSaTransIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 2),
    _T11FcSpSaTransIndex_Type()
)
t11FcSpSaTransIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTransIndex.setStatus("current")
_T11FcSpSaTransSecurityProt_Type = T11FcSpSecurityProtocolId
_T11FcSpSaTransSecurityProt_Object = MibTableColumn
t11FcSpSaTransSecurityProt = _T11FcSpSaTransSecurityProt_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 3),
    _T11FcSpSaTransSecurityProt_Type()
)
t11FcSpSaTransSecurityProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTransSecurityProt.setStatus("current")
_T11FcSpSaTransEncryptAlg_Type = AutonomousType
_T11FcSpSaTransEncryptAlg_Object = MibTableColumn
t11FcSpSaTransEncryptAlg = _T11FcSpSaTransEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 4),
    _T11FcSpSaTransEncryptAlg_Type()
)
t11FcSpSaTransEncryptAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTransEncryptAlg.setStatus("current")
_T11FcSpSaTransEncryptKeyLen_Type = Unsigned32
_T11FcSpSaTransEncryptKeyLen_Object = MibTableColumn
t11FcSpSaTransEncryptKeyLen = _T11FcSpSaTransEncryptKeyLen_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 5),
    _T11FcSpSaTransEncryptKeyLen_Type()
)
t11FcSpSaTransEncryptKeyLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTransEncryptKeyLen.setStatus("current")
_T11FcSpSaTransIntegrityAlg_Type = AutonomousType
_T11FcSpSaTransIntegrityAlg_Object = MibTableColumn
t11FcSpSaTransIntegrityAlg = _T11FcSpSaTransIntegrityAlg_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 6),
    _T11FcSpSaTransIntegrityAlg_Type()
)
t11FcSpSaTransIntegrityAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTransIntegrityAlg.setStatus("current")
_T11FcSpSaTransStorageType_Type = StorageType
_T11FcSpSaTransStorageType_Object = MibTableColumn
t11FcSpSaTransStorageType = _T11FcSpSaTransStorageType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 7),
    _T11FcSpSaTransStorageType_Type()
)
t11FcSpSaTransStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTransStorageType.setStatus("current")
_T11FcSpSaTransRowStatus_Type = RowStatus
_T11FcSpSaTransRowStatus_Object = MibTableColumn
t11FcSpSaTransRowStatus = _T11FcSpSaTransRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 3, 1, 8),
    _T11FcSpSaTransRowStatus_Type()
)
t11FcSpSaTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTransRowStatus.setStatus("current")
_T11FcSpSaTSelDrByTable_Object = MibTable
t11FcSpSaTSelDrByTable = _T11FcSpSaTSelDrByTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4)
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByTable.setStatus("current")
_T11FcSpSaTSelDrByEntry_Object = MibTableRow
t11FcSpSaTSelDrByEntry = _T11FcSpSaTSelDrByEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1)
)
t11FcSpSaTSelDrByEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByDirection"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByPrecedence"),
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByEntry.setStatus("current")
_T11FcSpSaTSelDrByDirection_Type = T11FcSaDirection
_T11FcSpSaTSelDrByDirection_Object = MibTableColumn
t11FcSpSaTSelDrByDirection = _T11FcSpSaTSelDrByDirection_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 1),
    _T11FcSpSaTSelDrByDirection_Type()
)
t11FcSpSaTSelDrByDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByDirection.setStatus("current")
_T11FcSpSaTSelDrByPrecedence_Type = T11FcSpPrecedence
_T11FcSpSaTSelDrByPrecedence_Object = MibTableColumn
t11FcSpSaTSelDrByPrecedence = _T11FcSpSaTSelDrByPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 2),
    _T11FcSpSaTSelDrByPrecedence_Type()
)
t11FcSpSaTSelDrByPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByPrecedence.setStatus("current")


class _T11FcSpSaTSelDrByAction_Type(Integer32):
    """Custom type t11FcSpSaTSelDrByAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("drop", 1))
    )


_T11FcSpSaTSelDrByAction_Type.__name__ = "Integer32"
_T11FcSpSaTSelDrByAction_Object = MibTableColumn
t11FcSpSaTSelDrByAction = _T11FcSpSaTSelDrByAction_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 3),
    _T11FcSpSaTSelDrByAction_Type()
)
t11FcSpSaTSelDrByAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByAction.setStatus("current")


class _T11FcSpSaTSelDrByStartSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelDrByStartSrcAddr based on FcAddressIdOrZero"""
    defaultHexValue = "000000"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelDrByStartSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelDrByStartSrcAddr_Object = MibTableColumn
t11FcSpSaTSelDrByStartSrcAddr = _T11FcSpSaTSelDrByStartSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 4),
    _T11FcSpSaTSelDrByStartSrcAddr_Type()
)
t11FcSpSaTSelDrByStartSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByStartSrcAddr.setStatus("current")


class _T11FcSpSaTSelDrByEndSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelDrByEndSrcAddr based on FcAddressIdOrZero"""
    defaultHexValue = "FFFFFF"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelDrByEndSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelDrByEndSrcAddr_Object = MibTableColumn
t11FcSpSaTSelDrByEndSrcAddr = _T11FcSpSaTSelDrByEndSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 5),
    _T11FcSpSaTSelDrByEndSrcAddr_Type()
)
t11FcSpSaTSelDrByEndSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByEndSrcAddr.setStatus("current")


class _T11FcSpSaTSelDrByStartDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelDrByStartDstAddr based on FcAddressIdOrZero"""
    defaultHexValue = "000000"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelDrByStartDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelDrByStartDstAddr_Object = MibTableColumn
t11FcSpSaTSelDrByStartDstAddr = _T11FcSpSaTSelDrByStartDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 6),
    _T11FcSpSaTSelDrByStartDstAddr_Type()
)
t11FcSpSaTSelDrByStartDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByStartDstAddr.setStatus("current")


class _T11FcSpSaTSelDrByEndDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelDrByEndDstAddr based on FcAddressIdOrZero"""
    defaultHexValue = "FFFFFF"

    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelDrByEndDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelDrByEndDstAddr_Object = MibTableColumn
t11FcSpSaTSelDrByEndDstAddr = _T11FcSpSaTSelDrByEndDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 7),
    _T11FcSpSaTSelDrByEndDstAddr_Type()
)
t11FcSpSaTSelDrByEndDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByEndDstAddr.setStatus("current")


class _T11FcSpSaTSelDrByStartRCtl_Type(T11FcRoutingControl):
    """Custom type t11FcSpSaTSelDrByStartRCtl based on T11FcRoutingControl"""
    defaultHexValue = "00"


_T11FcSpSaTSelDrByStartRCtl_Object = MibTableColumn
t11FcSpSaTSelDrByStartRCtl = _T11FcSpSaTSelDrByStartRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 8),
    _T11FcSpSaTSelDrByStartRCtl_Type()
)
t11FcSpSaTSelDrByStartRCtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByStartRCtl.setStatus("current")


class _T11FcSpSaTSelDrByEndRCtl_Type(T11FcRoutingControl):
    """Custom type t11FcSpSaTSelDrByEndRCtl based on T11FcRoutingControl"""
    defaultHexValue = "FF"


_T11FcSpSaTSelDrByEndRCtl_Object = MibTableColumn
t11FcSpSaTSelDrByEndRCtl = _T11FcSpSaTSelDrByEndRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 9),
    _T11FcSpSaTSelDrByEndRCtl_Type()
)
t11FcSpSaTSelDrByEndRCtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByEndRCtl.setStatus("current")


class _T11FcSpSaTSelDrByStartType_Type(T11FcSpType):
    """Custom type t11FcSpSaTSelDrByStartType based on T11FcSpType"""
    defaultHexValue = "0000"


_T11FcSpSaTSelDrByStartType_Object = MibTableColumn
t11FcSpSaTSelDrByStartType = _T11FcSpSaTSelDrByStartType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 10),
    _T11FcSpSaTSelDrByStartType_Type()
)
t11FcSpSaTSelDrByStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByStartType.setStatus("current")


class _T11FcSpSaTSelDrByEndType_Type(T11FcSpType):
    """Custom type t11FcSpSaTSelDrByEndType based on T11FcSpType"""
    defaultHexValue = "FFFF"


_T11FcSpSaTSelDrByEndType_Object = MibTableColumn
t11FcSpSaTSelDrByEndType = _T11FcSpSaTSelDrByEndType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 11),
    _T11FcSpSaTSelDrByEndType_Type()
)
t11FcSpSaTSelDrByEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByEndType.setStatus("current")
_T11FcSpSaTSelDrByMatches_Type = Counter64
_T11FcSpSaTSelDrByMatches_Object = MibTableColumn
t11FcSpSaTSelDrByMatches = _T11FcSpSaTSelDrByMatches_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 12),
    _T11FcSpSaTSelDrByMatches_Type()
)
t11FcSpSaTSelDrByMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByMatches.setStatus("current")
_T11FcSpSaTSelDrByRowStatus_Type = RowStatus
_T11FcSpSaTSelDrByRowStatus_Object = MibTableColumn
t11FcSpSaTSelDrByRowStatus = _T11FcSpSaTSelDrByRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 2, 4, 1, 13),
    _T11FcSpSaTSelDrByRowStatus_Type()
)
t11FcSpSaTSelDrByRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpSaTSelDrByRowStatus.setStatus("current")
_T11FcSpSaActive_ObjectIdentity = ObjectIdentity
t11FcSpSaActive = _T11FcSpSaActive_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 1, 3)
)
_T11FcSpSaPairTable_Object = MibTable
t11FcSpSaPairTable = _T11FcSpSaPairTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1)
)
if mibBuilder.loadTexts:
    t11FcSpSaPairTable.setStatus("current")
_T11FcSpSaPairEntry_Object = MibTableRow
t11FcSpSaPairEntry = _T11FcSpSaPairEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1)
)
t11FcSpSaPairEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaPairIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaPairInboundSpi"),
)
if mibBuilder.loadTexts:
    t11FcSpSaPairEntry.setStatus("current")
_T11FcSpSaPairIfIndex_Type = InterfaceIndex
_T11FcSpSaPairIfIndex_Object = MibTableColumn
t11FcSpSaPairIfIndex = _T11FcSpSaPairIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 1),
    _T11FcSpSaPairIfIndex_Type()
)
t11FcSpSaPairIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaPairIfIndex.setStatus("current")
_T11FcSpSaPairInboundSpi_Type = T11FcSpiIndex
_T11FcSpSaPairInboundSpi_Object = MibTableColumn
t11FcSpSaPairInboundSpi = _T11FcSpSaPairInboundSpi_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 2),
    _T11FcSpSaPairInboundSpi_Type()
)
t11FcSpSaPairInboundSpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaPairInboundSpi.setStatus("current")
_T11FcSpSaPairSecurityProt_Type = T11FcSpSecurityProtocolId
_T11FcSpSaPairSecurityProt_Object = MibTableColumn
t11FcSpSaPairSecurityProt = _T11FcSpSaPairSecurityProt_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 3),
    _T11FcSpSaPairSecurityProt_Type()
)
t11FcSpSaPairSecurityProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairSecurityProt.setStatus("current")


class _T11FcSpSaPairTransListIndex_Type(Unsigned32):
    """Custom type t11FcSpSaPairTransListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaPairTransListIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaPairTransListIndex_Object = MibTableColumn
t11FcSpSaPairTransListIndex = _T11FcSpSaPairTransListIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 4),
    _T11FcSpSaPairTransListIndex_Type()
)
t11FcSpSaPairTransListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairTransListIndex.setStatus("current")


class _T11FcSpSaPairTransIndex_Type(Unsigned32):
    """Custom type t11FcSpSaPairTransIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaPairTransIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaPairTransIndex_Object = MibTableColumn
t11FcSpSaPairTransIndex = _T11FcSpSaPairTransIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 5),
    _T11FcSpSaPairTransIndex_Type()
)
t11FcSpSaPairTransIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairTransIndex.setStatus("current")
_T11FcSpSaPairLifetimeLeft_Type = T11FcSpLifetimeLeft
_T11FcSpSaPairLifetimeLeft_Object = MibTableColumn
t11FcSpSaPairLifetimeLeft = _T11FcSpSaPairLifetimeLeft_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 6),
    _T11FcSpSaPairLifetimeLeft_Type()
)
t11FcSpSaPairLifetimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairLifetimeLeft.setStatus("current")
_T11FcSpSaPairLifetimeLeftUnits_Type = T11FcSpLifetimeLeftUnits
_T11FcSpSaPairLifetimeLeftUnits_Object = MibTableColumn
t11FcSpSaPairLifetimeLeftUnits = _T11FcSpSaPairLifetimeLeftUnits_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 7),
    _T11FcSpSaPairLifetimeLeftUnits_Type()
)
t11FcSpSaPairLifetimeLeftUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairLifetimeLeftUnits.setStatus("current")


class _T11FcSpSaPairTerminate_Type(Integer32):
    """Custom type t11FcSpSaPairTerminate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("terminate", 2))
    )


_T11FcSpSaPairTerminate_Type.__name__ = "Integer32"
_T11FcSpSaPairTerminate_Object = MibTableColumn
t11FcSpSaPairTerminate = _T11FcSpSaPairTerminate_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 8),
    _T11FcSpSaPairTerminate_Type()
)
t11FcSpSaPairTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaPairTerminate.setStatus("current")
_T11FcSpSaPairInProtUnMatchs_Type = Counter64
_T11FcSpSaPairInProtUnMatchs_Object = MibTableColumn
t11FcSpSaPairInProtUnMatchs = _T11FcSpSaPairInProtUnMatchs_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 9),
    _T11FcSpSaPairInProtUnMatchs_Type()
)
t11FcSpSaPairInProtUnMatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairInProtUnMatchs.setStatus("current")
_T11FcSpSaPairInDetReplays_Type = Counter64
_T11FcSpSaPairInDetReplays_Object = MibTableColumn
t11FcSpSaPairInDetReplays = _T11FcSpSaPairInDetReplays_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 10),
    _T11FcSpSaPairInDetReplays_Type()
)
t11FcSpSaPairInDetReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairInDetReplays.setStatus("current")
_T11FcSpSaPairInBadXforms_Type = Counter64
_T11FcSpSaPairInBadXforms_Object = MibTableColumn
t11FcSpSaPairInBadXforms = _T11FcSpSaPairInBadXforms_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 11),
    _T11FcSpSaPairInBadXforms_Type()
)
t11FcSpSaPairInBadXforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairInBadXforms.setStatus("current")
_T11FcSpSaPairInGoodXforms_Type = Counter64
_T11FcSpSaPairInGoodXforms_Object = MibTableColumn
t11FcSpSaPairInGoodXforms = _T11FcSpSaPairInGoodXforms_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 1, 1, 12),
    _T11FcSpSaPairInGoodXforms_Type()
)
t11FcSpSaPairInGoodXforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaPairInGoodXforms.setStatus("current")
_T11FcSpSaTSelNegInTable_Object = MibTable
t11FcSpSaTSelNegInTable = _T11FcSpSaTSelNegInTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2)
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInTable.setStatus("current")
_T11FcSpSaTSelNegInEntry_Object = MibTableRow
t11FcSpSaTSelNegInEntry = _T11FcSpSaTSelNegInEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1)
)
t11FcSpSaTSelNegInEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaPairIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInEntry.setStatus("current")


class _T11FcSpSaTSelNegInIndex_Type(Unsigned32):
    """Custom type t11FcSpSaTSelNegInIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaTSelNegInIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaTSelNegInIndex_Object = MibTableColumn
t11FcSpSaTSelNegInIndex = _T11FcSpSaTSelNegInIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 1),
    _T11FcSpSaTSelNegInIndex_Type()
)
t11FcSpSaTSelNegInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInIndex.setStatus("current")
_T11FcSpSaTSelNegInInboundSpi_Type = T11FcSpiIndex
_T11FcSpSaTSelNegInInboundSpi_Object = MibTableColumn
t11FcSpSaTSelNegInInboundSpi = _T11FcSpSaTSelNegInInboundSpi_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 2),
    _T11FcSpSaTSelNegInInboundSpi_Type()
)
t11FcSpSaTSelNegInInboundSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInInboundSpi.setStatus("current")


class _T11FcSpSaTSelNegInStartSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegInStartSrcAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegInStartSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegInStartSrcAddr_Object = MibTableColumn
t11FcSpSaTSelNegInStartSrcAddr = _T11FcSpSaTSelNegInStartSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 3),
    _T11FcSpSaTSelNegInStartSrcAddr_Type()
)
t11FcSpSaTSelNegInStartSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInStartSrcAddr.setStatus("current")


class _T11FcSpSaTSelNegInEndSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegInEndSrcAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegInEndSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegInEndSrcAddr_Object = MibTableColumn
t11FcSpSaTSelNegInEndSrcAddr = _T11FcSpSaTSelNegInEndSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 4),
    _T11FcSpSaTSelNegInEndSrcAddr_Type()
)
t11FcSpSaTSelNegInEndSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInEndSrcAddr.setStatus("current")


class _T11FcSpSaTSelNegInStartDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegInStartDstAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegInStartDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegInStartDstAddr_Object = MibTableColumn
t11FcSpSaTSelNegInStartDstAddr = _T11FcSpSaTSelNegInStartDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 5),
    _T11FcSpSaTSelNegInStartDstAddr_Type()
)
t11FcSpSaTSelNegInStartDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInStartDstAddr.setStatus("current")


class _T11FcSpSaTSelNegInEndDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegInEndDstAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegInEndDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegInEndDstAddr_Object = MibTableColumn
t11FcSpSaTSelNegInEndDstAddr = _T11FcSpSaTSelNegInEndDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 6),
    _T11FcSpSaTSelNegInEndDstAddr_Type()
)
t11FcSpSaTSelNegInEndDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInEndDstAddr.setStatus("current")
_T11FcSpSaTSelNegInStartRCtl_Type = T11FcRoutingControl
_T11FcSpSaTSelNegInStartRCtl_Object = MibTableColumn
t11FcSpSaTSelNegInStartRCtl = _T11FcSpSaTSelNegInStartRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 7),
    _T11FcSpSaTSelNegInStartRCtl_Type()
)
t11FcSpSaTSelNegInStartRCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInStartRCtl.setStatus("current")
_T11FcSpSaTSelNegInEndRCtl_Type = T11FcRoutingControl
_T11FcSpSaTSelNegInEndRCtl_Object = MibTableColumn
t11FcSpSaTSelNegInEndRCtl = _T11FcSpSaTSelNegInEndRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 8),
    _T11FcSpSaTSelNegInEndRCtl_Type()
)
t11FcSpSaTSelNegInEndRCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInEndRCtl.setStatus("current")
_T11FcSpSaTSelNegInStartType_Type = T11FcSpType
_T11FcSpSaTSelNegInStartType_Object = MibTableColumn
t11FcSpSaTSelNegInStartType = _T11FcSpSaTSelNegInStartType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 9),
    _T11FcSpSaTSelNegInStartType_Type()
)
t11FcSpSaTSelNegInStartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInStartType.setStatus("current")
_T11FcSpSaTSelNegInEndType_Type = T11FcSpType
_T11FcSpSaTSelNegInEndType_Object = MibTableColumn
t11FcSpSaTSelNegInEndType = _T11FcSpSaTSelNegInEndType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 10),
    _T11FcSpSaTSelNegInEndType_Type()
)
t11FcSpSaTSelNegInEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInEndType.setStatus("current")
_T11FcSpSaTSelNegInUnpMtchDrops_Type = Counter64
_T11FcSpSaTSelNegInUnpMtchDrops_Object = MibTableColumn
t11FcSpSaTSelNegInUnpMtchDrops = _T11FcSpSaTSelNegInUnpMtchDrops_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 2, 1, 11),
    _T11FcSpSaTSelNegInUnpMtchDrops_Type()
)
t11FcSpSaTSelNegInUnpMtchDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegInUnpMtchDrops.setStatus("current")
_T11FcSpSaTSelNegOutTable_Object = MibTable
t11FcSpSaTSelNegOutTable = _T11FcSpSaTSelNegOutTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3)
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutTable.setStatus("current")
_T11FcSpSaTSelNegOutEntry_Object = MibTableRow
t11FcSpSaTSelNegOutEntry = _T11FcSpSaTSelNegOutEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1)
)
t11FcSpSaTSelNegOutEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaPairIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutPrecedence"),
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutEntry.setStatus("current")
_T11FcSpSaTSelNegOutPrecedence_Type = T11FcSpPrecedence
_T11FcSpSaTSelNegOutPrecedence_Object = MibTableColumn
t11FcSpSaTSelNegOutPrecedence = _T11FcSpSaTSelNegOutPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 1),
    _T11FcSpSaTSelNegOutPrecedence_Type()
)
t11FcSpSaTSelNegOutPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutPrecedence.setStatus("current")
_T11FcSpSaTSelNegOutInboundSpi_Type = T11FcSpiIndex
_T11FcSpSaTSelNegOutInboundSpi_Object = MibTableColumn
t11FcSpSaTSelNegOutInboundSpi = _T11FcSpSaTSelNegOutInboundSpi_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 2),
    _T11FcSpSaTSelNegOutInboundSpi_Type()
)
t11FcSpSaTSelNegOutInboundSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutInboundSpi.setStatus("current")


class _T11FcSpSaTSelNegOutStartSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegOutStartSrcAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegOutStartSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegOutStartSrcAddr_Object = MibTableColumn
t11FcSpSaTSelNegOutStartSrcAddr = _T11FcSpSaTSelNegOutStartSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 3),
    _T11FcSpSaTSelNegOutStartSrcAddr_Type()
)
t11FcSpSaTSelNegOutStartSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutStartSrcAddr.setStatus("current")


class _T11FcSpSaTSelNegOutEndSrcAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegOutEndSrcAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegOutEndSrcAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegOutEndSrcAddr_Object = MibTableColumn
t11FcSpSaTSelNegOutEndSrcAddr = _T11FcSpSaTSelNegOutEndSrcAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 4),
    _T11FcSpSaTSelNegOutEndSrcAddr_Type()
)
t11FcSpSaTSelNegOutEndSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutEndSrcAddr.setStatus("current")


class _T11FcSpSaTSelNegOutStartDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegOutStartDstAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegOutStartDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegOutStartDstAddr_Object = MibTableColumn
t11FcSpSaTSelNegOutStartDstAddr = _T11FcSpSaTSelNegOutStartDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 5),
    _T11FcSpSaTSelNegOutStartDstAddr_Type()
)
t11FcSpSaTSelNegOutStartDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutStartDstAddr.setStatus("current")


class _T11FcSpSaTSelNegOutEndDstAddr_Type(FcAddressIdOrZero):
    """Custom type t11FcSpSaTSelNegOutEndDstAddr based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcSpSaTSelNegOutEndDstAddr_Type.__name__ = "FcAddressIdOrZero"
_T11FcSpSaTSelNegOutEndDstAddr_Object = MibTableColumn
t11FcSpSaTSelNegOutEndDstAddr = _T11FcSpSaTSelNegOutEndDstAddr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 6),
    _T11FcSpSaTSelNegOutEndDstAddr_Type()
)
t11FcSpSaTSelNegOutEndDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutEndDstAddr.setStatus("current")
_T11FcSpSaTSelNegOutStartRCtl_Type = T11FcRoutingControl
_T11FcSpSaTSelNegOutStartRCtl_Object = MibTableColumn
t11FcSpSaTSelNegOutStartRCtl = _T11FcSpSaTSelNegOutStartRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 7),
    _T11FcSpSaTSelNegOutStartRCtl_Type()
)
t11FcSpSaTSelNegOutStartRCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutStartRCtl.setStatus("current")
_T11FcSpSaTSelNegOutEndRCtl_Type = T11FcRoutingControl
_T11FcSpSaTSelNegOutEndRCtl_Object = MibTableColumn
t11FcSpSaTSelNegOutEndRCtl = _T11FcSpSaTSelNegOutEndRCtl_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 8),
    _T11FcSpSaTSelNegOutEndRCtl_Type()
)
t11FcSpSaTSelNegOutEndRCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutEndRCtl.setStatus("current")
_T11FcSpSaTSelNegOutStartType_Type = T11FcSpType
_T11FcSpSaTSelNegOutStartType_Object = MibTableColumn
t11FcSpSaTSelNegOutStartType = _T11FcSpSaTSelNegOutStartType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 9),
    _T11FcSpSaTSelNegOutStartType_Type()
)
t11FcSpSaTSelNegOutStartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutStartType.setStatus("current")
_T11FcSpSaTSelNegOutEndType_Type = T11FcSpType
_T11FcSpSaTSelNegOutEndType_Object = MibTableColumn
t11FcSpSaTSelNegOutEndType = _T11FcSpSaTSelNegOutEndType_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 3, 1, 10),
    _T11FcSpSaTSelNegOutEndType_Type()
)
t11FcSpSaTSelNegOutEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelNegOutEndType.setStatus("current")
_T11FcSpSaTSelSpiTable_Object = MibTable
t11FcSpSaTSelSpiTable = _T11FcSpSaTSelSpiTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 4)
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelSpiTable.setStatus("current")
_T11FcSpSaTSelSpiEntry_Object = MibTableRow
t11FcSpSaTSelSpiEntry = _T11FcSpSaTSelSpiEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 4, 1)
)
t11FcSpSaTSelSpiEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaPairIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelSpiInboundSpi"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaTSelSpiTrafSelIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpSaTSelSpiEntry.setStatus("current")
_T11FcSpSaTSelSpiInboundSpi_Type = T11FcSpiIndex
_T11FcSpSaTSelSpiInboundSpi_Object = MibTableColumn
t11FcSpSaTSelSpiInboundSpi = _T11FcSpSaTSelSpiInboundSpi_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 4, 1, 1),
    _T11FcSpSaTSelSpiInboundSpi_Type()
)
t11FcSpSaTSelSpiInboundSpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelSpiInboundSpi.setStatus("current")


class _T11FcSpSaTSelSpiTrafSelIndex_Type(Unsigned32):
    """Custom type t11FcSpSaTSelSpiTrafSelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaTSelSpiTrafSelIndex_Type.__name__ = "Unsigned32"
_T11FcSpSaTSelSpiTrafSelIndex_Object = MibTableColumn
t11FcSpSaTSelSpiTrafSelIndex = _T11FcSpSaTSelSpiTrafSelIndex_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 4, 1, 2),
    _T11FcSpSaTSelSpiTrafSelIndex_Type()
)
t11FcSpSaTSelSpiTrafSelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpSaTSelSpiTrafSelIndex.setStatus("current")
_T11FcSpSaTSelSpiDirection_Type = T11FcSaDirection
_T11FcSpSaTSelSpiDirection_Object = MibTableColumn
t11FcSpSaTSelSpiDirection = _T11FcSpSaTSelSpiDirection_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 4, 1, 3),
    _T11FcSpSaTSelSpiDirection_Type()
)
t11FcSpSaTSelSpiDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelSpiDirection.setStatus("current")
_T11FcSpSaTSelSpiTrafSelPtr_Type = Unsigned32
_T11FcSpSaTSelSpiTrafSelPtr_Object = MibTableColumn
t11FcSpSaTSelSpiTrafSelPtr = _T11FcSpSaTSelSpiTrafSelPtr_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 3, 4, 1, 4),
    _T11FcSpSaTSelSpiTrafSelPtr_Type()
)
t11FcSpSaTSelSpiTrafSelPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaTSelSpiTrafSelPtr.setStatus("current")
_T11FcSpSaControl_ObjectIdentity = ObjectIdentity
t11FcSpSaControl = _T11FcSpSaControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 1, 4)
)
_T11FcSpSaControlTable_Object = MibTable
t11FcSpSaControlTable = _T11FcSpSaControlTable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1)
)
if mibBuilder.loadTexts:
    t11FcSpSaControlTable.setStatus("current")
_T11FcSpSaControlEntry_Object = MibTableRow
t11FcSpSaControlEntry = _T11FcSpSaControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1)
)
t11FcSpSaControlEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfIndex"),
    (0, "T11-FC-SP-SA-MIB", "t11FcSpSaIfFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpSaControlEntry.setStatus("current")
_T11FcSpSaControlAuthFailEnable_Type = TruthValue
_T11FcSpSaControlAuthFailEnable_Object = MibTableColumn
t11FcSpSaControlAuthFailEnable = _T11FcSpSaControlAuthFailEnable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 1),
    _T11FcSpSaControlAuthFailEnable_Type()
)
t11FcSpSaControlAuthFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaControlAuthFailEnable.setStatus("current")
_T11FcSpSaControlInboundSpi_Type = T11FcSpiIndex
_T11FcSpSaControlInboundSpi_Object = MibTableColumn
t11FcSpSaControlInboundSpi = _T11FcSpSaControlInboundSpi_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 2),
    _T11FcSpSaControlInboundSpi_Type()
)
t11FcSpSaControlInboundSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlInboundSpi.setStatus("current")
_T11FcSpSaControlSource_Type = FcAddressIdOrZero
_T11FcSpSaControlSource_Object = MibTableColumn
t11FcSpSaControlSource = _T11FcSpSaControlSource_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 3),
    _T11FcSpSaControlSource_Type()
)
t11FcSpSaControlSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlSource.setStatus("current")
_T11FcSpSaControlDestination_Type = FcAddressIdOrZero
_T11FcSpSaControlDestination_Object = MibTableColumn
t11FcSpSaControlDestination = _T11FcSpSaControlDestination_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 4),
    _T11FcSpSaControlDestination_Type()
)
t11FcSpSaControlDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlDestination.setStatus("current")


class _T11FcSpSaControlFrame_Type(OctetString):
    """Custom type t11FcSpSaControlFrame based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_T11FcSpSaControlFrame_Type.__name__ = "OctetString"
_T11FcSpSaControlFrame_Object = MibTableColumn
t11FcSpSaControlFrame = _T11FcSpSaControlFrame_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 5),
    _T11FcSpSaControlFrame_Type()
)
t11FcSpSaControlFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlFrame.setStatus("current")
_T11FcSpSaControlElapsed_Type = TimeTicks
_T11FcSpSaControlElapsed_Object = MibTableColumn
t11FcSpSaControlElapsed = _T11FcSpSaControlElapsed_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 6),
    _T11FcSpSaControlElapsed_Type()
)
t11FcSpSaControlElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlElapsed.setStatus("current")
_T11FcSpSaControlSuppressed_Type = Gauge32
_T11FcSpSaControlSuppressed_Object = MibTableColumn
t11FcSpSaControlSuppressed = _T11FcSpSaControlSuppressed_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 7),
    _T11FcSpSaControlSuppressed_Type()
)
t11FcSpSaControlSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlSuppressed.setStatus("current")


class _T11FcSpSaControlWindow_Type(Unsigned32):
    """Custom type t11FcSpSaControlWindow based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpSaControlWindow_Type.__name__ = "Unsigned32"
_T11FcSpSaControlWindow_Object = MibTableColumn
t11FcSpSaControlWindow = _T11FcSpSaControlWindow_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 8),
    _T11FcSpSaControlWindow_Type()
)
t11FcSpSaControlWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaControlWindow.setStatus("current")
if mibBuilder.loadTexts:
    t11FcSpSaControlWindow.setUnits("seconds")


class _T11FcSpSaControlMaxNotifs_Type(Unsigned32):
    """Custom type t11FcSpSaControlMaxNotifs based on Unsigned32"""
    defaultValue = 16


_T11FcSpSaControlMaxNotifs_Object = MibTableColumn
t11FcSpSaControlMaxNotifs = _T11FcSpSaControlMaxNotifs_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 9),
    _T11FcSpSaControlMaxNotifs_Type()
)
t11FcSpSaControlMaxNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaControlMaxNotifs.setStatus("current")


class _T11FcSpSaControlLifeExcdEnable_Type(TruthValue):
    """Custom type t11FcSpSaControlLifeExcdEnable based on TruthValue"""


_T11FcSpSaControlLifeExcdEnable_Object = MibTableColumn
t11FcSpSaControlLifeExcdEnable = _T11FcSpSaControlLifeExcdEnable_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 10),
    _T11FcSpSaControlLifeExcdEnable_Type()
)
t11FcSpSaControlLifeExcdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpSaControlLifeExcdEnable.setStatus("current")
_T11FcSpSaControlLifeExcdSpi_Type = T11FcSpiIndex
_T11FcSpSaControlLifeExcdSpi_Object = MibTableColumn
t11FcSpSaControlLifeExcdSpi = _T11FcSpSaControlLifeExcdSpi_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 11),
    _T11FcSpSaControlLifeExcdSpi_Type()
)
t11FcSpSaControlLifeExcdSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlLifeExcdSpi.setStatus("current")
_T11FcSpSaControlLifeExcdDir_Type = T11FcSaDirection
_T11FcSpSaControlLifeExcdDir_Object = MibTableColumn
t11FcSpSaControlLifeExcdDir = _T11FcSpSaControlLifeExcdDir_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 12),
    _T11FcSpSaControlLifeExcdDir_Type()
)
t11FcSpSaControlLifeExcdDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlLifeExcdDir.setStatus("current")
_T11FcSpSaControlLifeExcdTime_Type = TimeStamp
_T11FcSpSaControlLifeExcdTime_Object = MibTableColumn
t11FcSpSaControlLifeExcdTime = _T11FcSpSaControlLifeExcdTime_Object(
    (1, 3, 6, 1, 2, 1, 179, 1, 4, 1, 1, 13),
    _T11FcSpSaControlLifeExcdTime_Type()
)
t11FcSpSaControlLifeExcdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpSaControlLifeExcdTime.setStatus("current")
_T11FcSpSaMIBConformance_ObjectIdentity = ObjectIdentity
t11FcSpSaMIBConformance = _T11FcSpSaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 2)
)
_T11FcSpSaMIBCompliances_ObjectIdentity = ObjectIdentity
t11FcSpSaMIBCompliances = _T11FcSpSaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 2, 1)
)
_T11FcSpSaMIBGroups_ObjectIdentity = ObjectIdentity
t11FcSpSaMIBGroups = _T11FcSpSaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 179, 2, 2)
)

# Managed Objects groups

t11FcSpSaCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 1)
)
t11FcSpSaCapabilityGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaIfEspHeaderCapab"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfCTAuthCapab"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfIKEv2Capab"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfIkev2AuthCapab"))
)
if mibBuilder.loadTexts:
    t11FcSpSaCapabilityGroup.setStatus("current")

t11FcSpSaParamStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 2)
)
t11FcSpSaParamStatusGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaIfStorageType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfReplayPrevention"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfReplayWindowSize"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfDeadPeerDetections"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfTerminateAllSas"))
)
if mibBuilder.loadTexts:
    t11FcSpSaParamStatusGroup.setStatus("current")

t11FcSpSaSummaryCountGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 3)
)
t11FcSpSaSummaryCountGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaIfOutDrops"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfOutBypasses"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfOutProcesses"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfOutUnMatcheds"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfInUnprotUnmtchDrops"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfInDetReplays"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfInUnprotMtchDrops"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfInBadXforms"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfInGoodXforms"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaIfInProtUnmtchs"))
)
if mibBuilder.loadTexts:
    t11FcSpSaSummaryCountGroup.setStatus("current")

t11FcSpSaProposalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 4)
)
t11FcSpSaProposalGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaPropSecurityProt"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPropTSelListIndex"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPropTransListIndex"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPropAcceptAlgorithm"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPropOutMatchSucceeds"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPropRowStatus"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropDirection"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropStartSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropEndSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropStartDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropEndDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropStartRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropEndRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropStartType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropEndType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropStorageType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelPropRowStatus"))
)
if mibBuilder.loadTexts:
    t11FcSpSaProposalGroup.setStatus("current")

t11FcSpSaDropBypassGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 5)
)
t11FcSpSaDropBypassGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByAction"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByStartSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByEndSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByStartDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByEndDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByStartRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByEndRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByStartType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByEndType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByMatches"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelDrByRowStatus"))
)
if mibBuilder.loadTexts:
    t11FcSpSaDropBypassGroup.setStatus("current")

t11FcSpSaActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 6)
)
t11FcSpSaActiveGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaPairSecurityProt"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairTransListIndex"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairTransIndex"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairLifetimeLeft"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairLifetimeLeftUnits"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairTerminate"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairInProtUnMatchs"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairInDetReplays"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairInBadXforms"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaPairInGoodXforms"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTransSecurityProt"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTransEncryptAlg"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTransEncryptKeyLen"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTransIntegrityAlg"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTransStorageType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTransRowStatus"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInInboundSpi"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInStartSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInEndSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInStartDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInEndDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInStartRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInEndRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInStartType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInEndType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegInUnpMtchDrops"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutInboundSpi"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutStartSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutEndSrcAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutStartDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutEndDstAddr"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutStartRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutEndRCtl"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutStartType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelNegOutEndType"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelSpiDirection"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaTSelSpiTrafSelPtr"))
)
if mibBuilder.loadTexts:
    t11FcSpSaActiveGroup.setStatus("current")

t11FcSpSaNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 7)
)
t11FcSpSaNotifInfoGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaControlAuthFailEnable"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlInboundSpi"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlSource"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlDestination"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlFrame"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlElapsed"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlSuppressed"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlWindow"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlMaxNotifs"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlLifeExcdEnable"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlLifeExcdSpi"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlLifeExcdDir"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlLifeExcdTime"))
)
if mibBuilder.loadTexts:
    t11FcSpSaNotifInfoGroup.setStatus("current")


# Notification objects

t11FcSpSaNotifyAuthFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 179, 0, 1)
)
t11FcSpSaNotifyAuthFailure.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaControlInboundSpi"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlSource"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlDestination"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlFrame"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlElapsed"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlSuppressed"))
)
if mibBuilder.loadTexts:
    t11FcSpSaNotifyAuthFailure.setStatus(
        "current"
    )

t11FcSpSaNotifyLifeExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 179, 0, 2)
)
t11FcSpSaNotifyLifeExceeded.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaControlLifeExcdSpi"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaControlLifeExcdDir"))
)
if mibBuilder.loadTexts:
    t11FcSpSaNotifyLifeExceeded.setStatus(
        "current"
    )


# Notifications groups

t11FcSpSaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 179, 2, 2, 8)
)
t11FcSpSaNotificationGroup.setObjects(
      *(("T11-FC-SP-SA-MIB", "t11FcSpSaNotifyAuthFailure"),
        ("T11-FC-SP-SA-MIB", "t11FcSpSaNotifyLifeExceeded"))
)
if mibBuilder.loadTexts:
    t11FcSpSaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FcSpSaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 179, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpSaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-SP-SA-MIB",
    **{"t11FcSpSaMIB": t11FcSpSaMIB,
       "t11FcSpSaMIBNotifications": t11FcSpSaMIBNotifications,
       "t11FcSpSaNotifyAuthFailure": t11FcSpSaNotifyAuthFailure,
       "t11FcSpSaNotifyLifeExceeded": t11FcSpSaNotifyLifeExceeded,
       "t11FcSpSaMIBObjects": t11FcSpSaMIBObjects,
       "t11FcSpSaBase": t11FcSpSaBase,
       "t11FcSpSaIfTable": t11FcSpSaIfTable,
       "t11FcSpSaIfEntry": t11FcSpSaIfEntry,
       "t11FcSpSaIfIndex": t11FcSpSaIfIndex,
       "t11FcSpSaIfFabricIndex": t11FcSpSaIfFabricIndex,
       "t11FcSpSaIfEspHeaderCapab": t11FcSpSaIfEspHeaderCapab,
       "t11FcSpSaIfCTAuthCapab": t11FcSpSaIfCTAuthCapab,
       "t11FcSpSaIfIKEv2Capab": t11FcSpSaIfIKEv2Capab,
       "t11FcSpSaIfIkev2AuthCapab": t11FcSpSaIfIkev2AuthCapab,
       "t11FcSpSaIfStorageType": t11FcSpSaIfStorageType,
       "t11FcSpSaIfReplayPrevention": t11FcSpSaIfReplayPrevention,
       "t11FcSpSaIfReplayWindowSize": t11FcSpSaIfReplayWindowSize,
       "t11FcSpSaIfDeadPeerDetections": t11FcSpSaIfDeadPeerDetections,
       "t11FcSpSaIfTerminateAllSas": t11FcSpSaIfTerminateAllSas,
       "t11FcSpSaIfOutDrops": t11FcSpSaIfOutDrops,
       "t11FcSpSaIfOutBypasses": t11FcSpSaIfOutBypasses,
       "t11FcSpSaIfOutProcesses": t11FcSpSaIfOutProcesses,
       "t11FcSpSaIfOutUnMatcheds": t11FcSpSaIfOutUnMatcheds,
       "t11FcSpSaIfInUnprotUnmtchDrops": t11FcSpSaIfInUnprotUnmtchDrops,
       "t11FcSpSaIfInDetReplays": t11FcSpSaIfInDetReplays,
       "t11FcSpSaIfInUnprotMtchDrops": t11FcSpSaIfInUnprotMtchDrops,
       "t11FcSpSaIfInBadXforms": t11FcSpSaIfInBadXforms,
       "t11FcSpSaIfInGoodXforms": t11FcSpSaIfInGoodXforms,
       "t11FcSpSaIfInProtUnmtchs": t11FcSpSaIfInProtUnmtchs,
       "t11FcSpSaConfig": t11FcSpSaConfig,
       "t11FcSpSaPropTable": t11FcSpSaPropTable,
       "t11FcSpSaPropEntry": t11FcSpSaPropEntry,
       "t11FcSpSaPropIndex": t11FcSpSaPropIndex,
       "t11FcSpSaPropSecurityProt": t11FcSpSaPropSecurityProt,
       "t11FcSpSaPropTSelListIndex": t11FcSpSaPropTSelListIndex,
       "t11FcSpSaPropTransListIndex": t11FcSpSaPropTransListIndex,
       "t11FcSpSaPropAcceptAlgorithm": t11FcSpSaPropAcceptAlgorithm,
       "t11FcSpSaPropOutMatchSucceeds": t11FcSpSaPropOutMatchSucceeds,
       "t11FcSpSaPropRowStatus": t11FcSpSaPropRowStatus,
       "t11FcSpSaTSelPropTable": t11FcSpSaTSelPropTable,
       "t11FcSpSaTSelPropEntry": t11FcSpSaTSelPropEntry,
       "t11FcSpSaTSelPropListIndex": t11FcSpSaTSelPropListIndex,
       "t11FcSpSaTSelPropPrecedence": t11FcSpSaTSelPropPrecedence,
       "t11FcSpSaTSelPropDirection": t11FcSpSaTSelPropDirection,
       "t11FcSpSaTSelPropStartSrcAddr": t11FcSpSaTSelPropStartSrcAddr,
       "t11FcSpSaTSelPropEndSrcAddr": t11FcSpSaTSelPropEndSrcAddr,
       "t11FcSpSaTSelPropStartDstAddr": t11FcSpSaTSelPropStartDstAddr,
       "t11FcSpSaTSelPropEndDstAddr": t11FcSpSaTSelPropEndDstAddr,
       "t11FcSpSaTSelPropStartRCtl": t11FcSpSaTSelPropStartRCtl,
       "t11FcSpSaTSelPropEndRCtl": t11FcSpSaTSelPropEndRCtl,
       "t11FcSpSaTSelPropStartType": t11FcSpSaTSelPropStartType,
       "t11FcSpSaTSelPropEndType": t11FcSpSaTSelPropEndType,
       "t11FcSpSaTSelPropStorageType": t11FcSpSaTSelPropStorageType,
       "t11FcSpSaTSelPropRowStatus": t11FcSpSaTSelPropRowStatus,
       "t11FcSpSaTransTable": t11FcSpSaTransTable,
       "t11FcSpSaTransEntry": t11FcSpSaTransEntry,
       "t11FcSpSaTransListIndex": t11FcSpSaTransListIndex,
       "t11FcSpSaTransIndex": t11FcSpSaTransIndex,
       "t11FcSpSaTransSecurityProt": t11FcSpSaTransSecurityProt,
       "t11FcSpSaTransEncryptAlg": t11FcSpSaTransEncryptAlg,
       "t11FcSpSaTransEncryptKeyLen": t11FcSpSaTransEncryptKeyLen,
       "t11FcSpSaTransIntegrityAlg": t11FcSpSaTransIntegrityAlg,
       "t11FcSpSaTransStorageType": t11FcSpSaTransStorageType,
       "t11FcSpSaTransRowStatus": t11FcSpSaTransRowStatus,
       "t11FcSpSaTSelDrByTable": t11FcSpSaTSelDrByTable,
       "t11FcSpSaTSelDrByEntry": t11FcSpSaTSelDrByEntry,
       "t11FcSpSaTSelDrByDirection": t11FcSpSaTSelDrByDirection,
       "t11FcSpSaTSelDrByPrecedence": t11FcSpSaTSelDrByPrecedence,
       "t11FcSpSaTSelDrByAction": t11FcSpSaTSelDrByAction,
       "t11FcSpSaTSelDrByStartSrcAddr": t11FcSpSaTSelDrByStartSrcAddr,
       "t11FcSpSaTSelDrByEndSrcAddr": t11FcSpSaTSelDrByEndSrcAddr,
       "t11FcSpSaTSelDrByStartDstAddr": t11FcSpSaTSelDrByStartDstAddr,
       "t11FcSpSaTSelDrByEndDstAddr": t11FcSpSaTSelDrByEndDstAddr,
       "t11FcSpSaTSelDrByStartRCtl": t11FcSpSaTSelDrByStartRCtl,
       "t11FcSpSaTSelDrByEndRCtl": t11FcSpSaTSelDrByEndRCtl,
       "t11FcSpSaTSelDrByStartType": t11FcSpSaTSelDrByStartType,
       "t11FcSpSaTSelDrByEndType": t11FcSpSaTSelDrByEndType,
       "t11FcSpSaTSelDrByMatches": t11FcSpSaTSelDrByMatches,
       "t11FcSpSaTSelDrByRowStatus": t11FcSpSaTSelDrByRowStatus,
       "t11FcSpSaActive": t11FcSpSaActive,
       "t11FcSpSaPairTable": t11FcSpSaPairTable,
       "t11FcSpSaPairEntry": t11FcSpSaPairEntry,
       "t11FcSpSaPairIfIndex": t11FcSpSaPairIfIndex,
       "t11FcSpSaPairInboundSpi": t11FcSpSaPairInboundSpi,
       "t11FcSpSaPairSecurityProt": t11FcSpSaPairSecurityProt,
       "t11FcSpSaPairTransListIndex": t11FcSpSaPairTransListIndex,
       "t11FcSpSaPairTransIndex": t11FcSpSaPairTransIndex,
       "t11FcSpSaPairLifetimeLeft": t11FcSpSaPairLifetimeLeft,
       "t11FcSpSaPairLifetimeLeftUnits": t11FcSpSaPairLifetimeLeftUnits,
       "t11FcSpSaPairTerminate": t11FcSpSaPairTerminate,
       "t11FcSpSaPairInProtUnMatchs": t11FcSpSaPairInProtUnMatchs,
       "t11FcSpSaPairInDetReplays": t11FcSpSaPairInDetReplays,
       "t11FcSpSaPairInBadXforms": t11FcSpSaPairInBadXforms,
       "t11FcSpSaPairInGoodXforms": t11FcSpSaPairInGoodXforms,
       "t11FcSpSaTSelNegInTable": t11FcSpSaTSelNegInTable,
       "t11FcSpSaTSelNegInEntry": t11FcSpSaTSelNegInEntry,
       "t11FcSpSaTSelNegInIndex": t11FcSpSaTSelNegInIndex,
       "t11FcSpSaTSelNegInInboundSpi": t11FcSpSaTSelNegInInboundSpi,
       "t11FcSpSaTSelNegInStartSrcAddr": t11FcSpSaTSelNegInStartSrcAddr,
       "t11FcSpSaTSelNegInEndSrcAddr": t11FcSpSaTSelNegInEndSrcAddr,
       "t11FcSpSaTSelNegInStartDstAddr": t11FcSpSaTSelNegInStartDstAddr,
       "t11FcSpSaTSelNegInEndDstAddr": t11FcSpSaTSelNegInEndDstAddr,
       "t11FcSpSaTSelNegInStartRCtl": t11FcSpSaTSelNegInStartRCtl,
       "t11FcSpSaTSelNegInEndRCtl": t11FcSpSaTSelNegInEndRCtl,
       "t11FcSpSaTSelNegInStartType": t11FcSpSaTSelNegInStartType,
       "t11FcSpSaTSelNegInEndType": t11FcSpSaTSelNegInEndType,
       "t11FcSpSaTSelNegInUnpMtchDrops": t11FcSpSaTSelNegInUnpMtchDrops,
       "t11FcSpSaTSelNegOutTable": t11FcSpSaTSelNegOutTable,
       "t11FcSpSaTSelNegOutEntry": t11FcSpSaTSelNegOutEntry,
       "t11FcSpSaTSelNegOutPrecedence": t11FcSpSaTSelNegOutPrecedence,
       "t11FcSpSaTSelNegOutInboundSpi": t11FcSpSaTSelNegOutInboundSpi,
       "t11FcSpSaTSelNegOutStartSrcAddr": t11FcSpSaTSelNegOutStartSrcAddr,
       "t11FcSpSaTSelNegOutEndSrcAddr": t11FcSpSaTSelNegOutEndSrcAddr,
       "t11FcSpSaTSelNegOutStartDstAddr": t11FcSpSaTSelNegOutStartDstAddr,
       "t11FcSpSaTSelNegOutEndDstAddr": t11FcSpSaTSelNegOutEndDstAddr,
       "t11FcSpSaTSelNegOutStartRCtl": t11FcSpSaTSelNegOutStartRCtl,
       "t11FcSpSaTSelNegOutEndRCtl": t11FcSpSaTSelNegOutEndRCtl,
       "t11FcSpSaTSelNegOutStartType": t11FcSpSaTSelNegOutStartType,
       "t11FcSpSaTSelNegOutEndType": t11FcSpSaTSelNegOutEndType,
       "t11FcSpSaTSelSpiTable": t11FcSpSaTSelSpiTable,
       "t11FcSpSaTSelSpiEntry": t11FcSpSaTSelSpiEntry,
       "t11FcSpSaTSelSpiInboundSpi": t11FcSpSaTSelSpiInboundSpi,
       "t11FcSpSaTSelSpiTrafSelIndex": t11FcSpSaTSelSpiTrafSelIndex,
       "t11FcSpSaTSelSpiDirection": t11FcSpSaTSelSpiDirection,
       "t11FcSpSaTSelSpiTrafSelPtr": t11FcSpSaTSelSpiTrafSelPtr,
       "t11FcSpSaControl": t11FcSpSaControl,
       "t11FcSpSaControlTable": t11FcSpSaControlTable,
       "t11FcSpSaControlEntry": t11FcSpSaControlEntry,
       "t11FcSpSaControlAuthFailEnable": t11FcSpSaControlAuthFailEnable,
       "t11FcSpSaControlInboundSpi": t11FcSpSaControlInboundSpi,
       "t11FcSpSaControlSource": t11FcSpSaControlSource,
       "t11FcSpSaControlDestination": t11FcSpSaControlDestination,
       "t11FcSpSaControlFrame": t11FcSpSaControlFrame,
       "t11FcSpSaControlElapsed": t11FcSpSaControlElapsed,
       "t11FcSpSaControlSuppressed": t11FcSpSaControlSuppressed,
       "t11FcSpSaControlWindow": t11FcSpSaControlWindow,
       "t11FcSpSaControlMaxNotifs": t11FcSpSaControlMaxNotifs,
       "t11FcSpSaControlLifeExcdEnable": t11FcSpSaControlLifeExcdEnable,
       "t11FcSpSaControlLifeExcdSpi": t11FcSpSaControlLifeExcdSpi,
       "t11FcSpSaControlLifeExcdDir": t11FcSpSaControlLifeExcdDir,
       "t11FcSpSaControlLifeExcdTime": t11FcSpSaControlLifeExcdTime,
       "t11FcSpSaMIBConformance": t11FcSpSaMIBConformance,
       "t11FcSpSaMIBCompliances": t11FcSpSaMIBCompliances,
       "t11FcSpSaMIBCompliance": t11FcSpSaMIBCompliance,
       "t11FcSpSaMIBGroups": t11FcSpSaMIBGroups,
       "t11FcSpSaCapabilityGroup": t11FcSpSaCapabilityGroup,
       "t11FcSpSaParamStatusGroup": t11FcSpSaParamStatusGroup,
       "t11FcSpSaSummaryCountGroup": t11FcSpSaSummaryCountGroup,
       "t11FcSpSaProposalGroup": t11FcSpSaProposalGroup,
       "t11FcSpSaDropBypassGroup": t11FcSpSaDropBypassGroup,
       "t11FcSpSaActiveGroup": t11FcSpSaActiveGroup,
       "t11FcSpSaNotifInfoGroup": t11FcSpSaNotifInfoGroup,
       "t11FcSpSaNotificationGroup": t11FcSpSaNotificationGroup}
)
