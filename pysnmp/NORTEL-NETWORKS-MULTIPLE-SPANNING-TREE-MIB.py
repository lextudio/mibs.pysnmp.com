# SNMP MIB module (NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:50 2024
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

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

nnMultipleSpanningTreeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 5)
)
nnMultipleSpanningTreeMib.setRevisions(
        ("2014-06-24 00:00",
         "2009-03-25 00:00",
         "2008-11-05 00:00",
         "2006-04-10 00:00",
         "2004-02-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnMstNotifications_ObjectIdentity = ObjectIdentity
nnMstNotifications = _NnMstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 0)
)
_NnMstObjects_ObjectIdentity = ObjectIdentity
nnMstObjects = _NnMstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1)
)
_NnMstScalars_ObjectIdentity = ObjectIdentity
nnMstScalars = _NnMstScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1)
)
_NnMstNoOfInstancesSupported_Type = Integer32
_NnMstNoOfInstancesSupported_Object = MibScalar
nnMstNoOfInstancesSupported = _NnMstNoOfInstancesSupported_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 1),
    _NnMstNoOfInstancesSupported_Type()
)
nnMstNoOfInstancesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstNoOfInstancesSupported.setStatus("current")


class _NnMstMaxHopCount_Type(Integer32):
    """Custom type nnMstMaxHopCount based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4000),
    )


_NnMstMaxHopCount_Type.__name__ = "Integer32"
_NnMstMaxHopCount_Object = MibScalar
nnMstMaxHopCount = _NnMstMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 2),
    _NnMstMaxHopCount_Type()
)
nnMstMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstMaxHopCount.setStatus("current")
_NnMstBrgAddress_Type = MacAddress
_NnMstBrgAddress_Object = MibScalar
nnMstBrgAddress = _NnMstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 3),
    _NnMstBrgAddress_Type()
)
nnMstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBrgAddress.setStatus("current")
_NnMstCistRoot_Type = BridgeId
_NnMstCistRoot_Object = MibScalar
nnMstCistRoot = _NnMstCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 4),
    _NnMstCistRoot_Type()
)
nnMstCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistRoot.setStatus("current")
_NnMstCistRegionalRoot_Type = BridgeId
_NnMstCistRegionalRoot_Object = MibScalar
nnMstCistRegionalRoot = _NnMstCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 5),
    _NnMstCistRegionalRoot_Type()
)
nnMstCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistRegionalRoot.setStatus("current")
_NnMstCistRootCost_Type = Integer32
_NnMstCistRootCost_Object = MibScalar
nnMstCistRootCost = _NnMstCistRootCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 6),
    _NnMstCistRootCost_Type()
)
nnMstCistRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistRootCost.setStatus("current")
_NnMstCistRegionalRootCost_Type = Integer32
_NnMstCistRegionalRootCost_Object = MibScalar
nnMstCistRegionalRootCost = _NnMstCistRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 7),
    _NnMstCistRegionalRootCost_Type()
)
nnMstCistRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistRegionalRootCost.setStatus("current")
_NnMstCistRootPort_Type = Integer32
_NnMstCistRootPort_Object = MibScalar
nnMstCistRootPort = _NnMstCistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 8),
    _NnMstCistRootPort_Type()
)
nnMstCistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistRootPort.setStatus("current")


class _NnMstCistBridgePriority_Type(Integer32):
    """Custom type nnMstCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_NnMstCistBridgePriority_Type.__name__ = "Integer32"
_NnMstCistBridgePriority_Object = MibScalar
nnMstCistBridgePriority = _NnMstCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 9),
    _NnMstCistBridgePriority_Type()
)
nnMstCistBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistBridgePriority.setStatus("current")


class _NnMstCistBridgeMaxAge_Type(Timeout):
    """Custom type nnMstCistBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_NnMstCistBridgeMaxAge_Type.__name__ = "Timeout"
_NnMstCistBridgeMaxAge_Object = MibScalar
nnMstCistBridgeMaxAge = _NnMstCistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 10),
    _NnMstCistBridgeMaxAge_Type()
)
nnMstCistBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistBridgeMaxAge.setStatus("current")


class _NnMstCistBridgeForwardDelay_Type(Timeout):
    """Custom type nnMstCistBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_NnMstCistBridgeForwardDelay_Type.__name__ = "Timeout"
_NnMstCistBridgeForwardDelay_Object = MibScalar
nnMstCistBridgeForwardDelay = _NnMstCistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 11),
    _NnMstCistBridgeForwardDelay_Type()
)
nnMstCistBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistBridgeForwardDelay.setStatus("current")
_NnMstCistHoldTime_Type = Integer32
_NnMstCistHoldTime_Object = MibScalar
nnMstCistHoldTime = _NnMstCistHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 12),
    _NnMstCistHoldTime_Type()
)
nnMstCistHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistHoldTime.setStatus("current")
_NnMstCistMaxAge_Type = Timeout
_NnMstCistMaxAge_Object = MibScalar
nnMstCistMaxAge = _NnMstCistMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 13),
    _NnMstCistMaxAge_Type()
)
nnMstCistMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistMaxAge.setStatus("current")
_NnMstCistForwardDelay_Type = Timeout
_NnMstCistForwardDelay_Object = MibScalar
nnMstCistForwardDelay = _NnMstCistForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 14),
    _NnMstCistForwardDelay_Type()
)
nnMstCistForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistForwardDelay.setStatus("current")
_NnMstMstpUpCount_Type = Counter32
_NnMstMstpUpCount_Object = MibScalar
nnMstMstpUpCount = _NnMstMstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 15),
    _NnMstMstpUpCount_Type()
)
nnMstMstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstMstpUpCount.setStatus("current")
_NnMstMstpDownCount_Type = Counter32
_NnMstMstpDownCount_Object = MibScalar
nnMstMstpDownCount = _NnMstMstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 16),
    _NnMstMstpDownCount_Type()
)
nnMstMstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstMstpDownCount.setStatus("current")


class _NnMstPathCostDefaultType_Type(Integer32):
    """Custom type nnMstPathCostDefaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_NnMstPathCostDefaultType_Type.__name__ = "Integer32"
_NnMstPathCostDefaultType_Object = MibScalar
nnMstPathCostDefaultType = _NnMstPathCostDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 17),
    _NnMstPathCostDefaultType_Type()
)
nnMstPathCostDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstPathCostDefaultType.setStatus("current")


class _NnMstForceProtocolVersion_Type(Integer32):
    """Custom type nnMstForceProtocolVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_NnMstForceProtocolVersion_Type.__name__ = "Integer32"
_NnMstForceProtocolVersion_Object = MibScalar
nnMstForceProtocolVersion = _NnMstForceProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 18),
    _NnMstForceProtocolVersion_Type()
)
nnMstForceProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstForceProtocolVersion.setStatus("current")


class _NnMstTxHoldCount_Type(Integer32):
    """Custom type nnMstTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NnMstTxHoldCount_Type.__name__ = "Integer32"
_NnMstTxHoldCount_Object = MibScalar
nnMstTxHoldCount = _NnMstTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 19),
    _NnMstTxHoldCount_Type()
)
nnMstTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstTxHoldCount.setStatus("current")


class _NnMstConfigIdSel_Type(Integer32):
    """Custom type nnMstConfigIdSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NnMstConfigIdSel_Type.__name__ = "Integer32"
_NnMstConfigIdSel_Object = MibScalar
nnMstConfigIdSel = _NnMstConfigIdSel_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 20),
    _NnMstConfigIdSel_Type()
)
nnMstConfigIdSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstConfigIdSel.setStatus("current")


class _NnMstRegionName_Type(OctetString):
    """Custom type nnMstRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NnMstRegionName_Type.__name__ = "OctetString"
_NnMstRegionName_Object = MibScalar
nnMstRegionName = _NnMstRegionName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 21),
    _NnMstRegionName_Type()
)
nnMstRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstRegionName.setStatus("current")


class _NnMstRegionVersion_Type(Integer32):
    """Custom type nnMstRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NnMstRegionVersion_Type.__name__ = "Integer32"
_NnMstRegionVersion_Object = MibScalar
nnMstRegionVersion = _NnMstRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 22),
    _NnMstRegionVersion_Type()
)
nnMstRegionVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstRegionVersion.setStatus("current")


class _NnMstConfigDigest_Type(OctetString):
    """Custom type nnMstConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_NnMstConfigDigest_Type.__name__ = "OctetString"
_NnMstConfigDigest_Object = MibScalar
nnMstConfigDigest = _NnMstConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 23),
    _NnMstConfigDigest_Type()
)
nnMstConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstConfigDigest.setStatus("current")
_NnMstRegionConfigChangeCount_Type = Counter32
_NnMstRegionConfigChangeCount_Object = MibScalar
nnMstRegionConfigChangeCount = _NnMstRegionConfigChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 24),
    _NnMstRegionConfigChangeCount_Type()
)
nnMstRegionConfigChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstRegionConfigChangeCount.setStatus("current")


class _NnMstCistBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type nnMstCistBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_NnMstCistBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_NnMstCistBridgeRoleSelectionSemState_Object = MibScalar
nnMstCistBridgeRoleSelectionSemState = _NnMstCistBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 25),
    _NnMstCistBridgeRoleSelectionSemState_Type()
)
nnMstCistBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistBridgeRoleSelectionSemState.setStatus("current")
_NnMstCistTimeSinceTopologyChange_Type = TimeTicks
_NnMstCistTimeSinceTopologyChange_Object = MibScalar
nnMstCistTimeSinceTopologyChange = _NnMstCistTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 26),
    _NnMstCistTimeSinceTopologyChange_Type()
)
nnMstCistTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistTimeSinceTopologyChange.setStatus("current")
_NnMstCistTopChanges_Type = Counter32
_NnMstCistTopChanges_Object = MibScalar
nnMstCistTopChanges = _NnMstCistTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 27),
    _NnMstCistTopChanges_Type()
)
nnMstCistTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistTopChanges.setStatus("current")
_NnMstCistNewRootBridgeCount_Type = Counter32
_NnMstCistNewRootBridgeCount_Object = MibScalar
nnMstCistNewRootBridgeCount = _NnMstCistNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 1, 28),
    _NnMstCistNewRootBridgeCount_Type()
)
nnMstCistNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistNewRootBridgeCount.setStatus("current")
_NnMstBridgeTable_Object = MibTable
nnMstBridgeTable = _NnMstBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2)
)
if mibBuilder.loadTexts:
    nnMstBridgeTable.setStatus("current")
_NnMstBridgeEntry_Object = MibTableRow
nnMstBridgeEntry = _NnMstBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1)
)
nnMstBridgeEntry.setIndexNames(
    (0, "NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBridgeInstance"),
)
if mibBuilder.loadTexts:
    nnMstBridgeEntry.setStatus("current")


class _NnMstBridgeInstance_Type(Integer32):
    """Custom type nnMstBridgeInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_NnMstBridgeInstance_Type.__name__ = "Integer32"
_NnMstBridgeInstance_Object = MibTableColumn
nnMstBridgeInstance = _NnMstBridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 1),
    _NnMstBridgeInstance_Type()
)
nnMstBridgeInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnMstBridgeInstance.setStatus("current")
_NnMstBridgeRegionalRoot_Type = BridgeId
_NnMstBridgeRegionalRoot_Object = MibTableColumn
nnMstBridgeRegionalRoot = _NnMstBridgeRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 2),
    _NnMstBridgeRegionalRoot_Type()
)
nnMstBridgeRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeRegionalRoot.setStatus("current")


class _NnMstBridgePriority_Type(Integer32):
    """Custom type nnMstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_NnMstBridgePriority_Type.__name__ = "Integer32"
_NnMstBridgePriority_Object = MibTableColumn
nnMstBridgePriority = _NnMstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 3),
    _NnMstBridgePriority_Type()
)
nnMstBridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnMstBridgePriority.setStatus("current")
_NnMstBridgeRootCost_Type = Integer32
_NnMstBridgeRootCost_Object = MibTableColumn
nnMstBridgeRootCost = _NnMstBridgeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 4),
    _NnMstBridgeRootCost_Type()
)
nnMstBridgeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeRootCost.setStatus("current")
_NnMstBridgeRootPort_Type = Integer32
_NnMstBridgeRootPort_Object = MibTableColumn
nnMstBridgeRootPort = _NnMstBridgeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 5),
    _NnMstBridgeRootPort_Type()
)
nnMstBridgeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeRootPort.setStatus("current")
_NnMstBridgeTimeSinceTopologyChange_Type = TimeTicks
_NnMstBridgeTimeSinceTopologyChange_Object = MibTableColumn
nnMstBridgeTimeSinceTopologyChange = _NnMstBridgeTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 6),
    _NnMstBridgeTimeSinceTopologyChange_Type()
)
nnMstBridgeTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeTimeSinceTopologyChange.setStatus("current")
_NnMstBridgeTopChanges_Type = Counter32
_NnMstBridgeTopChanges_Object = MibTableColumn
nnMstBridgeTopChanges = _NnMstBridgeTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 7),
    _NnMstBridgeTopChanges_Type()
)
nnMstBridgeTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeTopChanges.setStatus("current")
_NnMstBridgeNewRootCount_Type = Counter32
_NnMstBridgeNewRootCount_Object = MibTableColumn
nnMstBridgeNewRootCount = _NnMstBridgeNewRootCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 8),
    _NnMstBridgeNewRootCount_Type()
)
nnMstBridgeNewRootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeNewRootCount.setStatus("current")


class _NnMstBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type nnMstBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_NnMstBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_NnMstBridgeRoleSelectionSemState_Object = MibTableColumn
nnMstBridgeRoleSelectionSemState = _NnMstBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 9),
    _NnMstBridgeRoleSelectionSemState_Type()
)
nnMstBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeRoleSelectionSemState.setStatus("current")
_NnMstBridgeInstanceUpCount_Type = Counter32
_NnMstBridgeInstanceUpCount_Object = MibTableColumn
nnMstBridgeInstanceUpCount = _NnMstBridgeInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 10),
    _NnMstBridgeInstanceUpCount_Type()
)
nnMstBridgeInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeInstanceUpCount.setStatus("current")
_NnMstBridgeInstanceDownCount_Type = Counter32
_NnMstBridgeInstanceDownCount_Object = MibTableColumn
nnMstBridgeInstanceDownCount = _NnMstBridgeInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 11),
    _NnMstBridgeInstanceDownCount_Type()
)
nnMstBridgeInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeInstanceDownCount.setStatus("current")
_NnMstBridgeOldDesignatedRoot_Type = BridgeId
_NnMstBridgeOldDesignatedRoot_Object = MibTableColumn
nnMstBridgeOldDesignatedRoot = _NnMstBridgeOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 12),
    _NnMstBridgeOldDesignatedRoot_Type()
)
nnMstBridgeOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstBridgeOldDesignatedRoot.setStatus("current")
_NnMstBridgeEnabled_Type = TruthValue
_NnMstBridgeEnabled_Object = MibTableColumn
nnMstBridgeEnabled = _NnMstBridgeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 13),
    _NnMstBridgeEnabled_Type()
)
nnMstBridgeEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnMstBridgeEnabled.setStatus("current")
_NnMstBridgeRowStatus_Type = RowStatus
_NnMstBridgeRowStatus_Object = MibTableColumn
nnMstBridgeRowStatus = _NnMstBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 2, 1, 14),
    _NnMstBridgeRowStatus_Type()
)
nnMstBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnMstBridgeRowStatus.setStatus("current")
_NnMstCistPortTable_Object = MibTable
nnMstCistPortTable = _NnMstCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    nnMstCistPortTable.setStatus("current")
_NnMstCistPortEntry_Object = MibTableRow
nnMstCistPortEntry = _NnMstCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1)
)
nnMstCistPortEntry.setIndexNames(
    (0, "NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstCistPort"),
)
if mibBuilder.loadTexts:
    nnMstCistPortEntry.setStatus("current")


class _NnMstCistPort_Type(Integer32):
    """Custom type nnMstCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NnMstCistPort_Type.__name__ = "Integer32"
_NnMstCistPort_Object = MibTableColumn
nnMstCistPort = _NnMstCistPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 1),
    _NnMstCistPort_Type()
)
nnMstCistPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnMstCistPort.setStatus("current")


class _NnMstCistPortPathCost_Type(Integer32):
    """Custom type nnMstCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_NnMstCistPortPathCost_Type.__name__ = "Integer32"
_NnMstCistPortPathCost_Object = MibTableColumn
nnMstCistPortPathCost = _NnMstCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 2),
    _NnMstCistPortPathCost_Type()
)
nnMstCistPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistPortPathCost.setStatus("current")


class _NnMstCistPortPriority_Type(Integer32):
    """Custom type nnMstCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_NnMstCistPortPriority_Type.__name__ = "Integer32"
_NnMstCistPortPriority_Object = MibTableColumn
nnMstCistPortPriority = _NnMstCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 3),
    _NnMstCistPortPriority_Type()
)
nnMstCistPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistPortPriority.setStatus("current")
_NnMstCistPortDesignatedRoot_Type = BridgeId
_NnMstCistPortDesignatedRoot_Object = MibTableColumn
nnMstCistPortDesignatedRoot = _NnMstCistPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 4),
    _NnMstCistPortDesignatedRoot_Type()
)
nnMstCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortDesignatedRoot.setStatus("current")
_NnMstCistPortDesignatedBridge_Type = BridgeId
_NnMstCistPortDesignatedBridge_Object = MibTableColumn
nnMstCistPortDesignatedBridge = _NnMstCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 5),
    _NnMstCistPortDesignatedBridge_Type()
)
nnMstCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortDesignatedBridge.setStatus("current")


class _NnMstCistPortDesignatedPort_Type(OctetString):
    """Custom type nnMstCistPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NnMstCistPortDesignatedPort_Type.__name__ = "OctetString"
_NnMstCistPortDesignatedPort_Object = MibTableColumn
nnMstCistPortDesignatedPort = _NnMstCistPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 6),
    _NnMstCistPortDesignatedPort_Type()
)
nnMstCistPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortDesignatedPort.setStatus("current")


class _NnMstCistPortAdminP2P_Type(Integer32):
    """Custom type nnMstCistPortAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_NnMstCistPortAdminP2P_Type.__name__ = "Integer32"
_NnMstCistPortAdminP2P_Object = MibTableColumn
nnMstCistPortAdminP2P = _NnMstCistPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 7),
    _NnMstCistPortAdminP2P_Type()
)
nnMstCistPortAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistPortAdminP2P.setStatus("current")
_NnMstCistPortOperP2P_Type = TruthValue
_NnMstCistPortOperP2P_Object = MibTableColumn
nnMstCistPortOperP2P = _NnMstCistPortOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 8),
    _NnMstCistPortOperP2P_Type()
)
nnMstCistPortOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortOperP2P.setStatus("current")
_NnMstCistPortAdminEdgeStatus_Type = TruthValue
_NnMstCistPortAdminEdgeStatus_Object = MibTableColumn
nnMstCistPortAdminEdgeStatus = _NnMstCistPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 9),
    _NnMstCistPortAdminEdgeStatus_Type()
)
nnMstCistPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistPortAdminEdgeStatus.setStatus("current")
_NnMstCistPortOperEdgeStatus_Type = TruthValue
_NnMstCistPortOperEdgeStatus_Object = MibTableColumn
nnMstCistPortOperEdgeStatus = _NnMstCistPortOperEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 10),
    _NnMstCistPortOperEdgeStatus_Type()
)
nnMstCistPortOperEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortOperEdgeStatus.setStatus("current")
_NnMstCistPortProtocolMigration_Type = TruthValue
_NnMstCistPortProtocolMigration_Object = MibTableColumn
nnMstCistPortProtocolMigration = _NnMstCistPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 11),
    _NnMstCistPortProtocolMigration_Type()
)
nnMstCistPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistPortProtocolMigration.setStatus("current")


class _NnMstCistPortState_Type(Integer32):
    """Custom type nnMstCistPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_NnMstCistPortState_Type.__name__ = "Integer32"
_NnMstCistPortState_Object = MibTableColumn
nnMstCistPortState = _NnMstCistPortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 12),
    _NnMstCistPortState_Type()
)
nnMstCistPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortState.setStatus("current")


class _NnMstCistForcePortState_Type(Integer32):
    """Custom type nnMstCistForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NnMstCistForcePortState_Type.__name__ = "Integer32"
_NnMstCistForcePortState_Object = MibTableColumn
nnMstCistForcePortState = _NnMstCistForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 13),
    _NnMstCistForcePortState_Type()
)
nnMstCistForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistForcePortState.setStatus("current")
_NnMstCistPortForwardTransitions_Type = Counter32
_NnMstCistPortForwardTransitions_Object = MibTableColumn
nnMstCistPortForwardTransitions = _NnMstCistPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 14),
    _NnMstCistPortForwardTransitions_Type()
)
nnMstCistPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortForwardTransitions.setStatus("current")
_NnMstCistPortRxMstBpduCount_Type = Counter32
_NnMstCistPortRxMstBpduCount_Object = MibTableColumn
nnMstCistPortRxMstBpduCount = _NnMstCistPortRxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 15),
    _NnMstCistPortRxMstBpduCount_Type()
)
nnMstCistPortRxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortRxMstBpduCount.setStatus("current")
_NnMstCistPortRxRstBpduCount_Type = Counter32
_NnMstCistPortRxRstBpduCount_Object = MibTableColumn
nnMstCistPortRxRstBpduCount = _NnMstCistPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 16),
    _NnMstCistPortRxRstBpduCount_Type()
)
nnMstCistPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortRxRstBpduCount.setStatus("current")
_NnMstCistPortRxConfigBpduCount_Type = Counter32
_NnMstCistPortRxConfigBpduCount_Object = MibTableColumn
nnMstCistPortRxConfigBpduCount = _NnMstCistPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 17),
    _NnMstCistPortRxConfigBpduCount_Type()
)
nnMstCistPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortRxConfigBpduCount.setStatus("current")
_NnMstCistPortRxTcnBpduCount_Type = Counter32
_NnMstCistPortRxTcnBpduCount_Object = MibTableColumn
nnMstCistPortRxTcnBpduCount = _NnMstCistPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 18),
    _NnMstCistPortRxTcnBpduCount_Type()
)
nnMstCistPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortRxTcnBpduCount.setStatus("current")
_NnMstCistPortTxMstBpduCount_Type = Counter32
_NnMstCistPortTxMstBpduCount_Object = MibTableColumn
nnMstCistPortTxMstBpduCount = _NnMstCistPortTxMstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 19),
    _NnMstCistPortTxMstBpduCount_Type()
)
nnMstCistPortTxMstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortTxMstBpduCount.setStatus("current")
_NnMstCistPortTxRstBpduCount_Type = Counter32
_NnMstCistPortTxRstBpduCount_Object = MibTableColumn
nnMstCistPortTxRstBpduCount = _NnMstCistPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 20),
    _NnMstCistPortTxRstBpduCount_Type()
)
nnMstCistPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortTxRstBpduCount.setStatus("current")
_NnMstCistPortTxConfigBpduCount_Type = Counter32
_NnMstCistPortTxConfigBpduCount_Object = MibTableColumn
nnMstCistPortTxConfigBpduCount = _NnMstCistPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 21),
    _NnMstCistPortTxConfigBpduCount_Type()
)
nnMstCistPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortTxConfigBpduCount.setStatus("current")
_NnMstCistPortTxTcnBpduCount_Type = Counter32
_NnMstCistPortTxTcnBpduCount_Object = MibTableColumn
nnMstCistPortTxTcnBpduCount = _NnMstCistPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 22),
    _NnMstCistPortTxTcnBpduCount_Type()
)
nnMstCistPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortTxTcnBpduCount.setStatus("current")
_NnMstCistPortInvalidMstBpduRxCount_Type = Counter32
_NnMstCistPortInvalidMstBpduRxCount_Object = MibTableColumn
nnMstCistPortInvalidMstBpduRxCount = _NnMstCistPortInvalidMstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 23),
    _NnMstCistPortInvalidMstBpduRxCount_Type()
)
nnMstCistPortInvalidMstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortInvalidMstBpduRxCount.setStatus("current")
_NnMstCistPortInvalidRstBpduRxCount_Type = Counter32
_NnMstCistPortInvalidRstBpduRxCount_Object = MibTableColumn
nnMstCistPortInvalidRstBpduRxCount = _NnMstCistPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 24),
    _NnMstCistPortInvalidRstBpduRxCount_Type()
)
nnMstCistPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortInvalidRstBpduRxCount.setStatus("current")
_NnMstCistPortInvalidConfigBpduRxCount_Type = Counter32
_NnMstCistPortInvalidConfigBpduRxCount_Object = MibTableColumn
nnMstCistPortInvalidConfigBpduRxCount = _NnMstCistPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 25),
    _NnMstCistPortInvalidConfigBpduRxCount_Type()
)
nnMstCistPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortInvalidConfigBpduRxCount.setStatus("current")
_NnMstCistPortInvalidTcnBpduRxCount_Type = Counter32
_NnMstCistPortInvalidTcnBpduRxCount_Object = MibTableColumn
nnMstCistPortInvalidTcnBpduRxCount = _NnMstCistPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 26),
    _NnMstCistPortInvalidTcnBpduRxCount_Type()
)
nnMstCistPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortInvalidTcnBpduRxCount.setStatus("current")


class _NnMstCistPortTransmitSemState_Type(Integer32):
    """Custom type nnMstCistPortTransmitSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 5),
          ("transmitconfig", 2),
          ("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitrstp", 4),
          ("transmittcn", 3))
    )


_NnMstCistPortTransmitSemState_Type.__name__ = "Integer32"
_NnMstCistPortTransmitSemState_Object = MibTableColumn
nnMstCistPortTransmitSemState = _NnMstCistPortTransmitSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 27),
    _NnMstCistPortTransmitSemState_Type()
)
nnMstCistPortTransmitSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortTransmitSemState.setStatus("current")


class _NnMstCistPortReceiveSemState_Type(Integer32):
    """Custom type nnMstCistPortReceiveSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("receive", 1))
    )


_NnMstCistPortReceiveSemState_Type.__name__ = "Integer32"
_NnMstCistPortReceiveSemState_Object = MibTableColumn
nnMstCistPortReceiveSemState = _NnMstCistPortReceiveSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 28),
    _NnMstCistPortReceiveSemState_Type()
)
nnMstCistPortReceiveSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortReceiveSemState.setStatus("current")


class _NnMstCistPortProtMigrationSemState_Type(Integer32):
    """Custom type nnMstCistPortProtMigrationSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("sendingrstp", 2),
          ("sendingstp", 4),
          ("sendrstp", 1),
          ("sendstp", 3))
    )


_NnMstCistPortProtMigrationSemState_Type.__name__ = "Integer32"
_NnMstCistPortProtMigrationSemState_Object = MibTableColumn
nnMstCistPortProtMigrationSemState = _NnMstCistPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 29),
    _NnMstCistPortProtMigrationSemState_Type()
)
nnMstCistPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortProtMigrationSemState.setStatus("current")
_NnMstCistProtocolMigrationCount_Type = Counter32
_NnMstCistProtocolMigrationCount_Object = MibTableColumn
nnMstCistProtocolMigrationCount = _NnMstCistProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 30),
    _NnMstCistProtocolMigrationCount_Type()
)
nnMstCistProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistProtocolMigrationCount.setStatus("current")
_NnMstCistPortDesignatedCost_Type = Integer32
_NnMstCistPortDesignatedCost_Object = MibTableColumn
nnMstCistPortDesignatedCost = _NnMstCistPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 31),
    _NnMstCistPortDesignatedCost_Type()
)
nnMstCistPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortDesignatedCost.setStatus("current")
_NnMstCistPortRegionalRoot_Type = BridgeId
_NnMstCistPortRegionalRoot_Object = MibTableColumn
nnMstCistPortRegionalRoot = _NnMstCistPortRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 32),
    _NnMstCistPortRegionalRoot_Type()
)
nnMstCistPortRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortRegionalRoot.setStatus("current")
_NnMstCistPortRegionalPathCost_Type = Integer32
_NnMstCistPortRegionalPathCost_Object = MibTableColumn
nnMstCistPortRegionalPathCost = _NnMstCistPortRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 33),
    _NnMstCistPortRegionalPathCost_Type()
)
nnMstCistPortRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortRegionalPathCost.setStatus("current")


class _NnMstCistSelectedPortRole_Type(Integer32):
    """Custom type nnMstCistSelectedPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("root", 3))
    )


_NnMstCistSelectedPortRole_Type.__name__ = "Integer32"
_NnMstCistSelectedPortRole_Object = MibTableColumn
nnMstCistSelectedPortRole = _NnMstCistSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 34),
    _NnMstCistSelectedPortRole_Type()
)
nnMstCistSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistSelectedPortRole.setStatus("current")


class _NnMstCistCurrentPortRole_Type(Integer32):
    """Custom type nnMstCistCurrentPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("root", 3))
    )


_NnMstCistCurrentPortRole_Type.__name__ = "Integer32"
_NnMstCistCurrentPortRole_Object = MibTableColumn
nnMstCistCurrentPortRole = _NnMstCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 35),
    _NnMstCistCurrentPortRole_Type()
)
nnMstCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistCurrentPortRole.setStatus("current")


class _NnMstCistPortInfoSemState_Type(Integer32):
    """Custom type nnMstCistPortInfoSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("aged", 2),
          ("disabled", 0),
          ("enabled", 1),
          ("other", 7),
          ("present", 8),
          ("receive", 9),
          ("repeatdesg", 5),
          ("root", 6),
          ("superiordesg", 4),
          ("update", 3))
    )


_NnMstCistPortInfoSemState_Type.__name__ = "Integer32"
_NnMstCistPortInfoSemState_Object = MibTableColumn
nnMstCistPortInfoSemState = _NnMstCistPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 36),
    _NnMstCistPortInfoSemState_Type()
)
nnMstCistPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortInfoSemState.setStatus("current")


class _NnMstCistPortRoleTransitionSemState_Type(Integer32):
    """Custom type nnMstCistPortRoleTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeport", 3),
          ("blockedport", 2),
          ("blockport", 1),
          ("init", 0))
    )


_NnMstCistPortRoleTransitionSemState_Type.__name__ = "Integer32"
_NnMstCistPortRoleTransitionSemState_Object = MibTableColumn
nnMstCistPortRoleTransitionSemState = _NnMstCistPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 37),
    _NnMstCistPortRoleTransitionSemState_Type()
)
nnMstCistPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortRoleTransitionSemState.setStatus("current")


class _NnMstCistPortStateTransitionSemState_Type(Integer32):
    """Custom type nnMstCistPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_NnMstCistPortStateTransitionSemState_Type.__name__ = "Integer32"
_NnMstCistPortStateTransitionSemState_Object = MibTableColumn
nnMstCistPortStateTransitionSemState = _NnMstCistPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 38),
    _NnMstCistPortStateTransitionSemState_Type()
)
nnMstCistPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortStateTransitionSemState.setStatus("current")


class _NnMstCistPortTopologyChangeSemState_Type(Integer32):
    """Custom type nnMstCistPortTopologyChangeSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 7),
          ("active", 2),
          ("detected", 3),
          ("inactive", 1),
          ("init", 0),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_NnMstCistPortTopologyChangeSemState_Type.__name__ = "Integer32"
_NnMstCistPortTopologyChangeSemState_Object = MibTableColumn
nnMstCistPortTopologyChangeSemState = _NnMstCistPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 39),
    _NnMstCistPortTopologyChangeSemState_Type()
)
nnMstCistPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortTopologyChangeSemState.setStatus("current")


class _NnMstCistPortHelloTime_Type(Timeout):
    """Custom type nnMstCistPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_NnMstCistPortHelloTime_Type.__name__ = "Timeout"
_NnMstCistPortHelloTime_Object = MibTableColumn
nnMstCistPortHelloTime = _NnMstCistPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 40),
    _NnMstCistPortHelloTime_Type()
)
nnMstCistPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstCistPortHelloTime.setStatus("current")


class _NnMstCistPortOperVersion_Type(Integer32):
    """Custom type nnMstCistPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_NnMstCistPortOperVersion_Type.__name__ = "Integer32"
_NnMstCistPortOperVersion_Object = MibTableColumn
nnMstCistPortOperVersion = _NnMstCistPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 41),
    _NnMstCistPortOperVersion_Type()
)
nnMstCistPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortOperVersion.setStatus("current")
_NnMstCistPortEffectivePortState_Type = TruthValue
_NnMstCistPortEffectivePortState_Object = MibTableColumn
nnMstCistPortEffectivePortState = _NnMstCistPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 3, 1, 42),
    _NnMstCistPortEffectivePortState_Type()
)
nnMstCistPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstCistPortEffectivePortState.setStatus("current")
_NnMstPortTable_Object = MibTable
nnMstPortTable = _NnMstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4)
)
if mibBuilder.loadTexts:
    nnMstPortTable.setStatus("current")
_NnMstPortEntry_Object = MibTableRow
nnMstPortEntry = _NnMstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1)
)
nnMstPortEntry.setIndexNames(
    (0, "NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstPort"),
    (0, "NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBridgeInstance"),
)
if mibBuilder.loadTexts:
    nnMstPortEntry.setStatus("current")


class _NnMstPort_Type(Integer32):
    """Custom type nnMstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NnMstPort_Type.__name__ = "Integer32"
_NnMstPort_Object = MibTableColumn
nnMstPort = _NnMstPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 1),
    _NnMstPort_Type()
)
nnMstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnMstPort.setStatus("current")


class _NnMstPortPathCost_Type(Integer32):
    """Custom type nnMstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_NnMstPortPathCost_Type.__name__ = "Integer32"
_NnMstPortPathCost_Object = MibTableColumn
nnMstPortPathCost = _NnMstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 2),
    _NnMstPortPathCost_Type()
)
nnMstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstPortPathCost.setStatus("current")


class _NnMstPortPriority_Type(Integer32):
    """Custom type nnMstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_NnMstPortPriority_Type.__name__ = "Integer32"
_NnMstPortPriority_Object = MibTableColumn
nnMstPortPriority = _NnMstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 3),
    _NnMstPortPriority_Type()
)
nnMstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstPortPriority.setStatus("current")
_NnMstPortDesignatedRoot_Type = BridgeId
_NnMstPortDesignatedRoot_Object = MibTableColumn
nnMstPortDesignatedRoot = _NnMstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 4),
    _NnMstPortDesignatedRoot_Type()
)
nnMstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortDesignatedRoot.setStatus("current")
_NnMstPortDesignatedBridge_Type = BridgeId
_NnMstPortDesignatedBridge_Object = MibTableColumn
nnMstPortDesignatedBridge = _NnMstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 5),
    _NnMstPortDesignatedBridge_Type()
)
nnMstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortDesignatedBridge.setStatus("current")


class _NnMstPortDesignatedPort_Type(OctetString):
    """Custom type nnMstPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NnMstPortDesignatedPort_Type.__name__ = "OctetString"
_NnMstPortDesignatedPort_Object = MibTableColumn
nnMstPortDesignatedPort = _NnMstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 6),
    _NnMstPortDesignatedPort_Type()
)
nnMstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortDesignatedPort.setStatus("current")


class _NnMstPortState_Type(Integer32):
    """Custom type nnMstPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_NnMstPortState_Type.__name__ = "Integer32"
_NnMstPortState_Object = MibTableColumn
nnMstPortState = _NnMstPortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 7),
    _NnMstPortState_Type()
)
nnMstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortState.setStatus("current")


class _NnMstPortForcePortState_Type(Integer32):
    """Custom type nnMstPortForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NnMstPortForcePortState_Type.__name__ = "Integer32"
_NnMstPortForcePortState_Object = MibTableColumn
nnMstPortForcePortState = _NnMstPortForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 8),
    _NnMstPortForcePortState_Type()
)
nnMstPortForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstPortForcePortState.setStatus("current")
_NnMstPortForwardTransitions_Type = Counter32
_NnMstPortForwardTransitions_Object = MibTableColumn
nnMstPortForwardTransitions = _NnMstPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 9),
    _NnMstPortForwardTransitions_Type()
)
nnMstPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortForwardTransitions.setStatus("current")
_NnMstPortReceivedBPDUs_Type = Counter32
_NnMstPortReceivedBPDUs_Object = MibTableColumn
nnMstPortReceivedBPDUs = _NnMstPortReceivedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 10),
    _NnMstPortReceivedBPDUs_Type()
)
nnMstPortReceivedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortReceivedBPDUs.setStatus("current")
_NnMstPortTransmittedBPDUs_Type = Counter32
_NnMstPortTransmittedBPDUs_Object = MibTableColumn
nnMstPortTransmittedBPDUs = _NnMstPortTransmittedBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 11),
    _NnMstPortTransmittedBPDUs_Type()
)
nnMstPortTransmittedBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortTransmittedBPDUs.setStatus("current")
_NnMstPortInvalidBPDUsRcvd_Type = Counter32
_NnMstPortInvalidBPDUsRcvd_Object = MibTableColumn
nnMstPortInvalidBPDUsRcvd = _NnMstPortInvalidBPDUsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 12),
    _NnMstPortInvalidBPDUsRcvd_Type()
)
nnMstPortInvalidBPDUsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortInvalidBPDUsRcvd.setStatus("current")
_NnMstPortDesignatedCost_Type = Integer32
_NnMstPortDesignatedCost_Object = MibTableColumn
nnMstPortDesignatedCost = _NnMstPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 13),
    _NnMstPortDesignatedCost_Type()
)
nnMstPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortDesignatedCost.setStatus("current")


class _NnMstPortSelectedPortRole_Type(Integer32):
    """Custom type nnMstPortSelectedPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_NnMstPortSelectedPortRole_Type.__name__ = "Integer32"
_NnMstPortSelectedPortRole_Object = MibTableColumn
nnMstPortSelectedPortRole = _NnMstPortSelectedPortRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 14),
    _NnMstPortSelectedPortRole_Type()
)
nnMstPortSelectedPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortSelectedPortRole.setStatus("current")


class _NnMstPortCurrentPortRole_Type(Integer32):
    """Custom type nnMstPortCurrentPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disabled", 0),
          ("master", 5),
          ("root", 3))
    )


_NnMstPortCurrentPortRole_Type.__name__ = "Integer32"
_NnMstPortCurrentPortRole_Object = MibTableColumn
nnMstPortCurrentPortRole = _NnMstPortCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 15),
    _NnMstPortCurrentPortRole_Type()
)
nnMstPortCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortCurrentPortRole.setStatus("current")


class _NnMstPortInfoSemState_Type(Integer32):
    """Custom type nnMstPortInfoSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("aged", 2),
          ("disabled", 0),
          ("enabled", 1),
          ("other", 7),
          ("present", 8),
          ("receive", 9),
          ("repeatdesg", 5),
          ("root", 6),
          ("superiordesg", 4),
          ("update", 3))
    )


_NnMstPortInfoSemState_Type.__name__ = "Integer32"
_NnMstPortInfoSemState_Object = MibTableColumn
nnMstPortInfoSemState = _NnMstPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 16),
    _NnMstPortInfoSemState_Type()
)
nnMstPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortInfoSemState.setStatus("current")


class _NnMstPortRoleTransitionSemState_Type(Integer32):
    """Custom type nnMstPortRoleTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeport", 3),
          ("blockedport", 2),
          ("blockport", 1),
          ("init", 0))
    )


_NnMstPortRoleTransitionSemState_Type.__name__ = "Integer32"
_NnMstPortRoleTransitionSemState_Object = MibTableColumn
nnMstPortRoleTransitionSemState = _NnMstPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 17),
    _NnMstPortRoleTransitionSemState_Type()
)
nnMstPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortRoleTransitionSemState.setStatus("current")


class _NnMstPortStateTransitionSemState_Type(Integer32):
    """Custom type nnMstPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("forwarding", 2),
          ("learning", 1))
    )


_NnMstPortStateTransitionSemState_Type.__name__ = "Integer32"
_NnMstPortStateTransitionSemState_Object = MibTableColumn
nnMstPortStateTransitionSemState = _NnMstPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 18),
    _NnMstPortStateTransitionSemState_Type()
)
nnMstPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortStateTransitionSemState.setStatus("current")


class _NnMstPortTopologyChangeSemState_Type(Integer32):
    """Custom type nnMstPortTopologyChangeSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 7),
          ("active", 2),
          ("detected", 3),
          ("inactive", 1),
          ("init", 0),
          ("notifiedtc", 5),
          ("notifiedtcn", 4),
          ("propagating", 6))
    )


_NnMstPortTopologyChangeSemState_Type.__name__ = "Integer32"
_NnMstPortTopologyChangeSemState_Object = MibTableColumn
nnMstPortTopologyChangeSemState = _NnMstPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 19),
    _NnMstPortTopologyChangeSemState_Type()
)
nnMstPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortTopologyChangeSemState.setStatus("current")
_NnMstPortEffectivePortState_Type = TruthValue
_NnMstPortEffectivePortState_Object = MibTableColumn
nnMstPortEffectivePortState = _NnMstPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 4, 1, 20),
    _NnMstPortEffectivePortState_Type()
)
nnMstPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortEffectivePortState.setStatus("current")
_NnMstNotificationControl_ObjectIdentity = ObjectIdentity
nnMstNotificationControl = _NnMstNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5)
)
_NnMstNotificationControlScalars_ObjectIdentity = ObjectIdentity
nnMstNotificationControlScalars = _NnMstNotificationControlScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 1)
)


class _NnMstSetNotifications_Type(Integer32):
    """Custom type nnMstSetNotifications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NnMstSetNotifications_Type.__name__ = "Integer32"
_NnMstSetNotifications_Object = MibScalar
nnMstSetNotifications = _NnMstSetNotifications_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 1, 1),
    _NnMstSetNotifications_Type()
)
nnMstSetNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstSetNotifications.setStatus("current")


class _NnMstGenNotificationType_Type(Integer32):
    """Custom type nnMstGenNotificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("instanceDown", 4),
          ("instanceUp", 3),
          ("none", 0),
          ("up", 1))
    )


_NnMstGenNotificationType_Type.__name__ = "Integer32"
_NnMstGenNotificationType_Object = MibScalar
nnMstGenNotificationType = _NnMstGenNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 1, 2),
    _NnMstGenNotificationType_Type()
)
nnMstGenNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstGenNotificationType.setStatus("current")


class _NnMstErrNotificationType_Type(Integer32):
    """Custom type nnMstErrNotificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufffail", 2),
          ("memfail", 1),
          ("none", 0))
    )


_NnMstErrNotificationType_Type.__name__ = "Integer32"
_NnMstErrNotificationType_Object = MibScalar
nnMstErrNotificationType = _NnMstErrNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 1, 3),
    _NnMstErrNotificationType_Type()
)
nnMstErrNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstErrNotificationType.setStatus("current")
_NnMstPortNotificationTable_Object = MibTable
nnMstPortNotificationTable = _NnMstPortNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    nnMstPortNotificationTable.setStatus("current")
_NnMstPortNotificationEntry_Object = MibTableRow
nnMstPortNotificationEntry = _NnMstPortNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 2, 1)
)
nnMstPortNotificationEntry.setIndexNames(
    (0, "NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstPortNotificationIndex"),
)
if mibBuilder.loadTexts:
    nnMstPortNotificationEntry.setStatus("current")


class _NnMstPortNotificationIndex_Type(Integer32):
    """Custom type nnMstPortNotificationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_NnMstPortNotificationIndex_Type.__name__ = "Integer32"
_NnMstPortNotificationIndex_Object = MibTableColumn
nnMstPortNotificationIndex = _NnMstPortNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 2, 1, 1),
    _NnMstPortNotificationIndex_Type()
)
nnMstPortNotificationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnMstPortNotificationIndex.setStatus("current")


class _NnMstPortNotificationMigrationType_Type(Integer32):
    """Custom type nnMstPortNotificationMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendrstp", 1),
          ("sendstp", 0))
    )


_NnMstPortNotificationMigrationType_Type.__name__ = "Integer32"
_NnMstPortNotificationMigrationType_Object = MibTableColumn
nnMstPortNotificationMigrationType = _NnMstPortNotificationMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 2, 1, 2),
    _NnMstPortNotificationMigrationType_Type()
)
nnMstPortNotificationMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortNotificationMigrationType.setStatus("current")


class _NnMstPortNotificationPktErrType_Type(Integer32):
    """Custom type nnMstPortNotificationPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("configLengthErr", 2),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("invalidBpdu", 1),
          ("maxAgeErr", 5),
          ("mstpLengthErr", 8),
          ("protocolIdErr", 0),
          ("rstpLengthErr", 4),
          ("tcnLengthErr", 3))
    )


_NnMstPortNotificationPktErrType_Type.__name__ = "Integer32"
_NnMstPortNotificationPktErrType_Object = MibTableColumn
nnMstPortNotificationPktErrType = _NnMstPortNotificationPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 2, 1, 3),
    _NnMstPortNotificationPktErrType_Type()
)
nnMstPortNotificationPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortNotificationPktErrType.setStatus("current")
_NnMstPortNotificationPktErrVal_Type = Integer32
_NnMstPortNotificationPktErrVal_Object = MibTableColumn
nnMstPortNotificationPktErrVal = _NnMstPortNotificationPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 5, 2, 1, 4),
    _NnMstPortNotificationPktErrVal_Type()
)
nnMstPortNotificationPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnMstPortNotificationPktErrVal.setStatus("current")
_NnMstBridgeVlanMapTable_Object = MibTable
nnMstBridgeVlanMapTable = _NnMstBridgeVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 6)
)
if mibBuilder.loadTexts:
    nnMstBridgeVlanMapTable.setStatus("current")
_NnMstBridgeVlanMapEntry_Object = MibTableRow
nnMstBridgeVlanMapEntry = _NnMstBridgeVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 6, 1)
)
nnMstBridgeVlanMapEntry.setIndexNames(
    (0, "NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBridgeInstId"),
)
if mibBuilder.loadTexts:
    nnMstBridgeVlanMapEntry.setStatus("current")


class _NnMstBridgeInstId_Type(Integer32):
    """Custom type nnMstBridgeInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_NnMstBridgeInstId_Type.__name__ = "Integer32"
_NnMstBridgeInstId_Object = MibTableColumn
nnMstBridgeInstId = _NnMstBridgeInstId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 6, 1, 1),
    _NnMstBridgeInstId_Type()
)
nnMstBridgeInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnMstBridgeInstId.setStatus("current")


class _NnMstBridgeVlanMap_Type(OctetString):
    """Custom type nnMstBridgeVlanMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_NnMstBridgeVlanMap_Type.__name__ = "OctetString"
_NnMstBridgeVlanMap_Object = MibTableColumn
nnMstBridgeVlanMap = _NnMstBridgeVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 1, 6, 1, 2),
    _NnMstBridgeVlanMap_Type()
)
nnMstBridgeVlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnMstBridgeVlanMap.setStatus("current")

# Managed Objects groups


# Notification objects

nnMstGeneralEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 0, 1)
)
nnMstGeneralEvent.setObjects(
      *(("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBrgAddress"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstGenNotificationType"))
)
if mibBuilder.loadTexts:
    nnMstGeneralEvent.setStatus(
        "current"
    )

nnMstErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 0, 2)
)
nnMstErrorEvent.setObjects(
      *(("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBrgAddress"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstErrNotificationType"))
)
if mibBuilder.loadTexts:
    nnMstErrorEvent.setStatus(
        "current"
    )

nnMstNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 0, 3)
)
nnMstNewRoot.setObjects(
      *(("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBrgAddress"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBridgeOldDesignatedRoot"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBridgeRegionalRoot"))
)
if mibBuilder.loadTexts:
    nnMstNewRoot.setStatus(
        "current"
    )

nnMstTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 0, 4)
)
nnMstTopologyChange.setObjects(
    ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBrgAddress")
)
if mibBuilder.loadTexts:
    nnMstTopologyChange.setStatus(
        "current"
    )

nnMstProtocolMigration = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 0, 5)
)
nnMstProtocolMigration.setObjects(
      *(("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBrgAddress"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstForceProtocolVersion"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstPortNotificationMigrationType"))
)
if mibBuilder.loadTexts:
    nnMstProtocolMigration.setStatus(
        "current"
    )

nnMstRegionConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 5, 0, 6)
)
nnMstRegionConfigChange.setObjects(
      *(("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstBrgAddress"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstConfigIdSel"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstRegionName"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstRegionVersion"),
        ("NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB", "nnMstConfigDigest"))
)
if mibBuilder.loadTexts:
    nnMstRegionConfigChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB",
    **{"nnMultipleSpanningTreeMib": nnMultipleSpanningTreeMib,
       "nnMstNotifications": nnMstNotifications,
       "nnMstGeneralEvent": nnMstGeneralEvent,
       "nnMstErrorEvent": nnMstErrorEvent,
       "nnMstNewRoot": nnMstNewRoot,
       "nnMstTopologyChange": nnMstTopologyChange,
       "nnMstProtocolMigration": nnMstProtocolMigration,
       "nnMstRegionConfigChange": nnMstRegionConfigChange,
       "nnMstObjects": nnMstObjects,
       "nnMstScalars": nnMstScalars,
       "nnMstNoOfInstancesSupported": nnMstNoOfInstancesSupported,
       "nnMstMaxHopCount": nnMstMaxHopCount,
       "nnMstBrgAddress": nnMstBrgAddress,
       "nnMstCistRoot": nnMstCistRoot,
       "nnMstCistRegionalRoot": nnMstCistRegionalRoot,
       "nnMstCistRootCost": nnMstCistRootCost,
       "nnMstCistRegionalRootCost": nnMstCistRegionalRootCost,
       "nnMstCistRootPort": nnMstCistRootPort,
       "nnMstCistBridgePriority": nnMstCistBridgePriority,
       "nnMstCistBridgeMaxAge": nnMstCistBridgeMaxAge,
       "nnMstCistBridgeForwardDelay": nnMstCistBridgeForwardDelay,
       "nnMstCistHoldTime": nnMstCistHoldTime,
       "nnMstCistMaxAge": nnMstCistMaxAge,
       "nnMstCistForwardDelay": nnMstCistForwardDelay,
       "nnMstMstpUpCount": nnMstMstpUpCount,
       "nnMstMstpDownCount": nnMstMstpDownCount,
       "nnMstPathCostDefaultType": nnMstPathCostDefaultType,
       "nnMstForceProtocolVersion": nnMstForceProtocolVersion,
       "nnMstTxHoldCount": nnMstTxHoldCount,
       "nnMstConfigIdSel": nnMstConfigIdSel,
       "nnMstRegionName": nnMstRegionName,
       "nnMstRegionVersion": nnMstRegionVersion,
       "nnMstConfigDigest": nnMstConfigDigest,
       "nnMstRegionConfigChangeCount": nnMstRegionConfigChangeCount,
       "nnMstCistBridgeRoleSelectionSemState": nnMstCistBridgeRoleSelectionSemState,
       "nnMstCistTimeSinceTopologyChange": nnMstCistTimeSinceTopologyChange,
       "nnMstCistTopChanges": nnMstCistTopChanges,
       "nnMstCistNewRootBridgeCount": nnMstCistNewRootBridgeCount,
       "nnMstBridgeTable": nnMstBridgeTable,
       "nnMstBridgeEntry": nnMstBridgeEntry,
       "nnMstBridgeInstance": nnMstBridgeInstance,
       "nnMstBridgeRegionalRoot": nnMstBridgeRegionalRoot,
       "nnMstBridgePriority": nnMstBridgePriority,
       "nnMstBridgeRootCost": nnMstBridgeRootCost,
       "nnMstBridgeRootPort": nnMstBridgeRootPort,
       "nnMstBridgeTimeSinceTopologyChange": nnMstBridgeTimeSinceTopologyChange,
       "nnMstBridgeTopChanges": nnMstBridgeTopChanges,
       "nnMstBridgeNewRootCount": nnMstBridgeNewRootCount,
       "nnMstBridgeRoleSelectionSemState": nnMstBridgeRoleSelectionSemState,
       "nnMstBridgeInstanceUpCount": nnMstBridgeInstanceUpCount,
       "nnMstBridgeInstanceDownCount": nnMstBridgeInstanceDownCount,
       "nnMstBridgeOldDesignatedRoot": nnMstBridgeOldDesignatedRoot,
       "nnMstBridgeEnabled": nnMstBridgeEnabled,
       "nnMstBridgeRowStatus": nnMstBridgeRowStatus,
       "nnMstCistPortTable": nnMstCistPortTable,
       "nnMstCistPortEntry": nnMstCistPortEntry,
       "nnMstCistPort": nnMstCistPort,
       "nnMstCistPortPathCost": nnMstCistPortPathCost,
       "nnMstCistPortPriority": nnMstCistPortPriority,
       "nnMstCistPortDesignatedRoot": nnMstCistPortDesignatedRoot,
       "nnMstCistPortDesignatedBridge": nnMstCistPortDesignatedBridge,
       "nnMstCistPortDesignatedPort": nnMstCistPortDesignatedPort,
       "nnMstCistPortAdminP2P": nnMstCistPortAdminP2P,
       "nnMstCistPortOperP2P": nnMstCistPortOperP2P,
       "nnMstCistPortAdminEdgeStatus": nnMstCistPortAdminEdgeStatus,
       "nnMstCistPortOperEdgeStatus": nnMstCistPortOperEdgeStatus,
       "nnMstCistPortProtocolMigration": nnMstCistPortProtocolMigration,
       "nnMstCistPortState": nnMstCistPortState,
       "nnMstCistForcePortState": nnMstCistForcePortState,
       "nnMstCistPortForwardTransitions": nnMstCistPortForwardTransitions,
       "nnMstCistPortRxMstBpduCount": nnMstCistPortRxMstBpduCount,
       "nnMstCistPortRxRstBpduCount": nnMstCistPortRxRstBpduCount,
       "nnMstCistPortRxConfigBpduCount": nnMstCistPortRxConfigBpduCount,
       "nnMstCistPortRxTcnBpduCount": nnMstCistPortRxTcnBpduCount,
       "nnMstCistPortTxMstBpduCount": nnMstCistPortTxMstBpduCount,
       "nnMstCistPortTxRstBpduCount": nnMstCistPortTxRstBpduCount,
       "nnMstCistPortTxConfigBpduCount": nnMstCistPortTxConfigBpduCount,
       "nnMstCistPortTxTcnBpduCount": nnMstCistPortTxTcnBpduCount,
       "nnMstCistPortInvalidMstBpduRxCount": nnMstCistPortInvalidMstBpduRxCount,
       "nnMstCistPortInvalidRstBpduRxCount": nnMstCistPortInvalidRstBpduRxCount,
       "nnMstCistPortInvalidConfigBpduRxCount": nnMstCistPortInvalidConfigBpduRxCount,
       "nnMstCistPortInvalidTcnBpduRxCount": nnMstCistPortInvalidTcnBpduRxCount,
       "nnMstCistPortTransmitSemState": nnMstCistPortTransmitSemState,
       "nnMstCistPortReceiveSemState": nnMstCistPortReceiveSemState,
       "nnMstCistPortProtMigrationSemState": nnMstCistPortProtMigrationSemState,
       "nnMstCistProtocolMigrationCount": nnMstCistProtocolMigrationCount,
       "nnMstCistPortDesignatedCost": nnMstCistPortDesignatedCost,
       "nnMstCistPortRegionalRoot": nnMstCistPortRegionalRoot,
       "nnMstCistPortRegionalPathCost": nnMstCistPortRegionalPathCost,
       "nnMstCistSelectedPortRole": nnMstCistSelectedPortRole,
       "nnMstCistCurrentPortRole": nnMstCistCurrentPortRole,
       "nnMstCistPortInfoSemState": nnMstCistPortInfoSemState,
       "nnMstCistPortRoleTransitionSemState": nnMstCistPortRoleTransitionSemState,
       "nnMstCistPortStateTransitionSemState": nnMstCistPortStateTransitionSemState,
       "nnMstCistPortTopologyChangeSemState": nnMstCistPortTopologyChangeSemState,
       "nnMstCistPortHelloTime": nnMstCistPortHelloTime,
       "nnMstCistPortOperVersion": nnMstCistPortOperVersion,
       "nnMstCistPortEffectivePortState": nnMstCistPortEffectivePortState,
       "nnMstPortTable": nnMstPortTable,
       "nnMstPortEntry": nnMstPortEntry,
       "nnMstPort": nnMstPort,
       "nnMstPortPathCost": nnMstPortPathCost,
       "nnMstPortPriority": nnMstPortPriority,
       "nnMstPortDesignatedRoot": nnMstPortDesignatedRoot,
       "nnMstPortDesignatedBridge": nnMstPortDesignatedBridge,
       "nnMstPortDesignatedPort": nnMstPortDesignatedPort,
       "nnMstPortState": nnMstPortState,
       "nnMstPortForcePortState": nnMstPortForcePortState,
       "nnMstPortForwardTransitions": nnMstPortForwardTransitions,
       "nnMstPortReceivedBPDUs": nnMstPortReceivedBPDUs,
       "nnMstPortTransmittedBPDUs": nnMstPortTransmittedBPDUs,
       "nnMstPortInvalidBPDUsRcvd": nnMstPortInvalidBPDUsRcvd,
       "nnMstPortDesignatedCost": nnMstPortDesignatedCost,
       "nnMstPortSelectedPortRole": nnMstPortSelectedPortRole,
       "nnMstPortCurrentPortRole": nnMstPortCurrentPortRole,
       "nnMstPortInfoSemState": nnMstPortInfoSemState,
       "nnMstPortRoleTransitionSemState": nnMstPortRoleTransitionSemState,
       "nnMstPortStateTransitionSemState": nnMstPortStateTransitionSemState,
       "nnMstPortTopologyChangeSemState": nnMstPortTopologyChangeSemState,
       "nnMstPortEffectivePortState": nnMstPortEffectivePortState,
       "nnMstNotificationControl": nnMstNotificationControl,
       "nnMstNotificationControlScalars": nnMstNotificationControlScalars,
       "nnMstSetNotifications": nnMstSetNotifications,
       "nnMstGenNotificationType": nnMstGenNotificationType,
       "nnMstErrNotificationType": nnMstErrNotificationType,
       "nnMstPortNotificationTable": nnMstPortNotificationTable,
       "nnMstPortNotificationEntry": nnMstPortNotificationEntry,
       "nnMstPortNotificationIndex": nnMstPortNotificationIndex,
       "nnMstPortNotificationMigrationType": nnMstPortNotificationMigrationType,
       "nnMstPortNotificationPktErrType": nnMstPortNotificationPktErrType,
       "nnMstPortNotificationPktErrVal": nnMstPortNotificationPktErrVal,
       "nnMstBridgeVlanMapTable": nnMstBridgeVlanMapTable,
       "nnMstBridgeVlanMapEntry": nnMstBridgeVlanMapEntry,
       "nnMstBridgeInstId": nnMstBridgeInstId,
       "nnMstBridgeVlanMap": nnMstBridgeVlanMap}
)
