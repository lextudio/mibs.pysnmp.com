# SNMP MIB module (IEEE8021-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-MSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:26 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(IEEE8021BridgePortNumber,
 IEEE8021MstIdentifier,
 IEEE8021PbbComponentIdentifier,
 IEEE8021VlanIndex,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021MstIdentifier",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021VlanIndex",
    "ieee802dot1mibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021MstpMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 6)
)
ieee8021MstpMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2012-08-10 00:00",
         "2011-12-12 00:00",
         "2011-03-23 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021MstpNotifications_ObjectIdentity = ObjectIdentity
ieee8021MstpNotifications = _Ieee8021MstpNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 6, 0)
)
_Ieee8021MstpObjects_ObjectIdentity = ObjectIdentity
ieee8021MstpObjects = _Ieee8021MstpObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 6, 1)
)
_Ieee8021MstpCistTable_Object = MibTable
ieee8021MstpCistTable = _Ieee8021MstpCistTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021MstpCistTable.setStatus("current")
_Ieee8021MstpCistEntry_Object = MibTableRow
ieee8021MstpCistEntry = _Ieee8021MstpCistEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1)
)
ieee8021MstpCistEntry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpCistComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021MstpCistEntry.setStatus("current")
_Ieee8021MstpCistComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpCistComponentId_Object = MibTableColumn
ieee8021MstpCistComponentId = _Ieee8021MstpCistComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 1),
    _Ieee8021MstpCistComponentId_Type()
)
ieee8021MstpCistComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpCistComponentId.setStatus("current")
_Ieee8021MstpCistBridgeIdentifier_Type = BridgeId
_Ieee8021MstpCistBridgeIdentifier_Object = MibTableColumn
ieee8021MstpCistBridgeIdentifier = _Ieee8021MstpCistBridgeIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 2),
    _Ieee8021MstpCistBridgeIdentifier_Type()
)
ieee8021MstpCistBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistBridgeIdentifier.setStatus("current")
_Ieee8021MstpCistTopologyChange_Type = TruthValue
_Ieee8021MstpCistTopologyChange_Object = MibTableColumn
ieee8021MstpCistTopologyChange = _Ieee8021MstpCistTopologyChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 3),
    _Ieee8021MstpCistTopologyChange_Type()
)
ieee8021MstpCistTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistTopologyChange.setStatus("current")
_Ieee8021MstpCistRegionalRootIdentifier_Type = BridgeId
_Ieee8021MstpCistRegionalRootIdentifier_Object = MibTableColumn
ieee8021MstpCistRegionalRootIdentifier = _Ieee8021MstpCistRegionalRootIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 4),
    _Ieee8021MstpCistRegionalRootIdentifier_Type()
)
ieee8021MstpCistRegionalRootIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistRegionalRootIdentifier.setStatus("current")


class _Ieee8021MstpCistPathCost_Type(Unsigned32):
    """Custom type ieee8021MstpCistPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ieee8021MstpCistPathCost_Type.__name__ = "Unsigned32"
_Ieee8021MstpCistPathCost_Object = MibTableColumn
ieee8021MstpCistPathCost = _Ieee8021MstpCistPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 5),
    _Ieee8021MstpCistPathCost_Type()
)
ieee8021MstpCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPathCost.setStatus("current")


class _Ieee8021MstpCistMaxHops_Type(Integer32):
    """Custom type ieee8021MstpCistMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Ieee8021MstpCistMaxHops_Type.__name__ = "Integer32"
_Ieee8021MstpCistMaxHops_Object = MibTableColumn
ieee8021MstpCistMaxHops = _Ieee8021MstpCistMaxHops_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 1, 1, 6),
    _Ieee8021MstpCistMaxHops_Type()
)
ieee8021MstpCistMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistMaxHops.setStatus("current")
_Ieee8021MstpTable_Object = MibTable
ieee8021MstpTable = _Ieee8021MstpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021MstpTable.setStatus("current")
_Ieee8021MstpEntry_Object = MibTableRow
ieee8021MstpEntry = _Ieee8021MstpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1)
)
ieee8021MstpEntry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpComponentId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpId"),
)
if mibBuilder.loadTexts:
    ieee8021MstpEntry.setStatus("current")
_Ieee8021MstpComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpComponentId_Object = MibTableColumn
ieee8021MstpComponentId = _Ieee8021MstpComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 1),
    _Ieee8021MstpComponentId_Type()
)
ieee8021MstpComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpComponentId.setStatus("current")
_Ieee8021MstpId_Type = IEEE8021MstIdentifier
_Ieee8021MstpId_Object = MibTableColumn
ieee8021MstpId = _Ieee8021MstpId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 2),
    _Ieee8021MstpId_Type()
)
ieee8021MstpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpId.setStatus("current")
_Ieee8021MstpBridgeId_Type = BridgeId
_Ieee8021MstpBridgeId_Object = MibTableColumn
ieee8021MstpBridgeId = _Ieee8021MstpBridgeId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 3),
    _Ieee8021MstpBridgeId_Type()
)
ieee8021MstpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpBridgeId.setStatus("current")
_Ieee8021MstpTimeSinceTopologyChange_Type = TimeTicks
_Ieee8021MstpTimeSinceTopologyChange_Object = MibTableColumn
ieee8021MstpTimeSinceTopologyChange = _Ieee8021MstpTimeSinceTopologyChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 4),
    _Ieee8021MstpTimeSinceTopologyChange_Type()
)
ieee8021MstpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021MstpTimeSinceTopologyChange.setUnits("centi-seconds")
_Ieee8021MstpTopologyChanges_Type = Counter64
_Ieee8021MstpTopologyChanges_Object = MibTableColumn
ieee8021MstpTopologyChanges = _Ieee8021MstpTopologyChanges_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 5),
    _Ieee8021MstpTopologyChanges_Type()
)
ieee8021MstpTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpTopologyChanges.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021MstpTopologyChanges.setUnits("topology changes")
_Ieee8021MstpTopologyChange_Type = TruthValue
_Ieee8021MstpTopologyChange_Object = MibTableColumn
ieee8021MstpTopologyChange = _Ieee8021MstpTopologyChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 6),
    _Ieee8021MstpTopologyChange_Type()
)
ieee8021MstpTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpTopologyChange.setStatus("current")
_Ieee8021MstpDesignatedRoot_Type = BridgeId
_Ieee8021MstpDesignatedRoot_Object = MibTableColumn
ieee8021MstpDesignatedRoot = _Ieee8021MstpDesignatedRoot_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 7),
    _Ieee8021MstpDesignatedRoot_Type()
)
ieee8021MstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpDesignatedRoot.setStatus("current")
_Ieee8021MstpRootPathCost_Type = Integer32
_Ieee8021MstpRootPathCost_Object = MibTableColumn
ieee8021MstpRootPathCost = _Ieee8021MstpRootPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 8),
    _Ieee8021MstpRootPathCost_Type()
)
ieee8021MstpRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpRootPathCost.setStatus("current")
_Ieee8021MstpRootPort_Type = IEEE8021BridgePortNumber
_Ieee8021MstpRootPort_Object = MibTableColumn
ieee8021MstpRootPort = _Ieee8021MstpRootPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 9),
    _Ieee8021MstpRootPort_Type()
)
ieee8021MstpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpRootPort.setStatus("current")


class _Ieee8021MstpBridgePriority_Type(Integer32):
    """Custom type ieee8021MstpBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Ieee8021MstpBridgePriority_Type.__name__ = "Integer32"
_Ieee8021MstpBridgePriority_Object = MibTableColumn
ieee8021MstpBridgePriority = _Ieee8021MstpBridgePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 10),
    _Ieee8021MstpBridgePriority_Type()
)
ieee8021MstpBridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MstpBridgePriority.setStatus("current")


class _Ieee8021MstpVids0_Type(OctetString):
    """Custom type ieee8021MstpVids0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_Ieee8021MstpVids0_Type.__name__ = "OctetString"
_Ieee8021MstpVids0_Object = MibTableColumn
ieee8021MstpVids0 = _Ieee8021MstpVids0_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 11),
    _Ieee8021MstpVids0_Type()
)
ieee8021MstpVids0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpVids0.setStatus("current")


class _Ieee8021MstpVids1_Type(OctetString):
    """Custom type ieee8021MstpVids1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_Ieee8021MstpVids1_Type.__name__ = "OctetString"
_Ieee8021MstpVids1_Object = MibTableColumn
ieee8021MstpVids1 = _Ieee8021MstpVids1_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 12),
    _Ieee8021MstpVids1_Type()
)
ieee8021MstpVids1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpVids1.setStatus("current")


class _Ieee8021MstpVids2_Type(OctetString):
    """Custom type ieee8021MstpVids2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_Ieee8021MstpVids2_Type.__name__ = "OctetString"
_Ieee8021MstpVids2_Object = MibTableColumn
ieee8021MstpVids2 = _Ieee8021MstpVids2_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 13),
    _Ieee8021MstpVids2_Type()
)
ieee8021MstpVids2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpVids2.setStatus("current")


class _Ieee8021MstpVids3_Type(OctetString):
    """Custom type ieee8021MstpVids3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_Ieee8021MstpVids3_Type.__name__ = "OctetString"
_Ieee8021MstpVids3_Object = MibTableColumn
ieee8021MstpVids3 = _Ieee8021MstpVids3_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 14),
    _Ieee8021MstpVids3_Type()
)
ieee8021MstpVids3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpVids3.setStatus("current")
_Ieee8021MstpRowStatus_Type = RowStatus
_Ieee8021MstpRowStatus_Object = MibTableColumn
ieee8021MstpRowStatus = _Ieee8021MstpRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 2, 1, 15),
    _Ieee8021MstpRowStatus_Type()
)
ieee8021MstpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021MstpRowStatus.setStatus("current")
_Ieee8021MstpCistPortTable_Object = MibTable
ieee8021MstpCistPortTable = _Ieee8021MstpCistPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021MstpCistPortTable.setStatus("current")
_Ieee8021MstpCistPortEntry_Object = MibTableRow
ieee8021MstpCistPortEntry = _Ieee8021MstpCistPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1)
)
ieee8021MstpCistPortEntry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpCistPortComponentId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpCistPortNum"),
)
if mibBuilder.loadTexts:
    ieee8021MstpCistPortEntry.setStatus("current")
_Ieee8021MstpCistPortComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpCistPortComponentId_Object = MibTableColumn
ieee8021MstpCistPortComponentId = _Ieee8021MstpCistPortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 1),
    _Ieee8021MstpCistPortComponentId_Type()
)
ieee8021MstpCistPortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortComponentId.setStatus("current")
_Ieee8021MstpCistPortNum_Type = IEEE8021BridgePortNumber
_Ieee8021MstpCistPortNum_Object = MibTableColumn
ieee8021MstpCistPortNum = _Ieee8021MstpCistPortNum_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 2),
    _Ieee8021MstpCistPortNum_Type()
)
ieee8021MstpCistPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortNum.setStatus("current")
_Ieee8021MstpCistPortUptime_Type = TimeTicks
_Ieee8021MstpCistPortUptime_Object = MibTableColumn
ieee8021MstpCistPortUptime = _Ieee8021MstpCistPortUptime_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 3),
    _Ieee8021MstpCistPortUptime_Type()
)
ieee8021MstpCistPortUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortUptime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortUptime.setUnits("centi-seconds")


class _Ieee8021MstpCistPortAdminPathCost_Type(Integer32):
    """Custom type ieee8021MstpCistPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Ieee8021MstpCistPortAdminPathCost_Type.__name__ = "Integer32"
_Ieee8021MstpCistPortAdminPathCost_Object = MibTableColumn
ieee8021MstpCistPortAdminPathCost = _Ieee8021MstpCistPortAdminPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 4),
    _Ieee8021MstpCistPortAdminPathCost_Type()
)
ieee8021MstpCistPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortAdminPathCost.setStatus("current")
_Ieee8021MstpCistPortDesignatedRoot_Type = BridgeId
_Ieee8021MstpCistPortDesignatedRoot_Object = MibTableColumn
ieee8021MstpCistPortDesignatedRoot = _Ieee8021MstpCistPortDesignatedRoot_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 5),
    _Ieee8021MstpCistPortDesignatedRoot_Type()
)
ieee8021MstpCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortDesignatedRoot.setStatus("current")
_Ieee8021MstpCistPortTopologyChangeAck_Type = TruthValue
_Ieee8021MstpCistPortTopologyChangeAck_Object = MibTableColumn
ieee8021MstpCistPortTopologyChangeAck = _Ieee8021MstpCistPortTopologyChangeAck_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 6),
    _Ieee8021MstpCistPortTopologyChangeAck_Type()
)
ieee8021MstpCistPortTopologyChangeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortTopologyChangeAck.setStatus("current")


class _Ieee8021MstpCistPortHelloTime_Type(Integer32):
    """Custom type ieee8021MstpCistPortHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Ieee8021MstpCistPortHelloTime_Type.__name__ = "Integer32"
_Ieee8021MstpCistPortHelloTime_Object = MibTableColumn
ieee8021MstpCistPortHelloTime = _Ieee8021MstpCistPortHelloTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 7),
    _Ieee8021MstpCistPortHelloTime_Type()
)
ieee8021MstpCistPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortHelloTime.setUnits("centi-seconds")


class _Ieee8021MstpCistPortAdminEdgePort_Type(TruthValue):
    """Custom type ieee8021MstpCistPortAdminEdgePort based on TruthValue"""


_Ieee8021MstpCistPortAdminEdgePort_Object = MibTableColumn
ieee8021MstpCistPortAdminEdgePort = _Ieee8021MstpCistPortAdminEdgePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 8),
    _Ieee8021MstpCistPortAdminEdgePort_Type()
)
ieee8021MstpCistPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortAdminEdgePort.setStatus("current")
_Ieee8021MstpCistPortOperEdgePort_Type = TruthValue
_Ieee8021MstpCistPortOperEdgePort_Object = MibTableColumn
ieee8021MstpCistPortOperEdgePort = _Ieee8021MstpCistPortOperEdgePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 9),
    _Ieee8021MstpCistPortOperEdgePort_Type()
)
ieee8021MstpCistPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortOperEdgePort.setStatus("current")
_Ieee8021MstpCistPortMacEnabled_Type = TruthValue
_Ieee8021MstpCistPortMacEnabled_Object = MibTableColumn
ieee8021MstpCistPortMacEnabled = _Ieee8021MstpCistPortMacEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 10),
    _Ieee8021MstpCistPortMacEnabled_Type()
)
ieee8021MstpCistPortMacEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortMacEnabled.setStatus("current")
_Ieee8021MstpCistPortMacOperational_Type = TruthValue
_Ieee8021MstpCistPortMacOperational_Object = MibTableColumn
ieee8021MstpCistPortMacOperational = _Ieee8021MstpCistPortMacOperational_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 11),
    _Ieee8021MstpCistPortMacOperational_Type()
)
ieee8021MstpCistPortMacOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortMacOperational.setStatus("current")
_Ieee8021MstpCistPortRestrictedRole_Type = TruthValue
_Ieee8021MstpCistPortRestrictedRole_Object = MibTableColumn
ieee8021MstpCistPortRestrictedRole = _Ieee8021MstpCistPortRestrictedRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 12),
    _Ieee8021MstpCistPortRestrictedRole_Type()
)
ieee8021MstpCistPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortRestrictedRole.setStatus("current")
_Ieee8021MstpCistPortRestrictedTcn_Type = TruthValue
_Ieee8021MstpCistPortRestrictedTcn_Object = MibTableColumn
ieee8021MstpCistPortRestrictedTcn = _Ieee8021MstpCistPortRestrictedTcn_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 13),
    _Ieee8021MstpCistPortRestrictedTcn_Type()
)
ieee8021MstpCistPortRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortRestrictedTcn.setStatus("current")


class _Ieee8021MstpCistPortRole_Type(Integer32):
    """Custom type ieee8021MstpCistPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("backup", 4),
          ("designated", 3),
          ("root", 1))
    )


_Ieee8021MstpCistPortRole_Type.__name__ = "Integer32"
_Ieee8021MstpCistPortRole_Object = MibTableColumn
ieee8021MstpCistPortRole = _Ieee8021MstpCistPortRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 14),
    _Ieee8021MstpCistPortRole_Type()
)
ieee8021MstpCistPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortRole.setStatus("current")
_Ieee8021MstpCistPortDisputed_Type = TruthValue
_Ieee8021MstpCistPortDisputed_Object = MibTableColumn
ieee8021MstpCistPortDisputed = _Ieee8021MstpCistPortDisputed_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 15),
    _Ieee8021MstpCistPortDisputed_Type()
)
ieee8021MstpCistPortDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortDisputed.setStatus("current")
_Ieee8021MstpCistPortCistRegionalRootId_Type = BridgeId
_Ieee8021MstpCistPortCistRegionalRootId_Object = MibTableColumn
ieee8021MstpCistPortCistRegionalRootId = _Ieee8021MstpCistPortCistRegionalRootId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 16),
    _Ieee8021MstpCistPortCistRegionalRootId_Type()
)
ieee8021MstpCistPortCistRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortCistRegionalRootId.setStatus("current")


class _Ieee8021MstpCistPortCistPathCost_Type(Unsigned32):
    """Custom type ieee8021MstpCistPortCistPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ieee8021MstpCistPortCistPathCost_Type.__name__ = "Unsigned32"
_Ieee8021MstpCistPortCistPathCost_Object = MibTableColumn
ieee8021MstpCistPortCistPathCost = _Ieee8021MstpCistPortCistPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 17),
    _Ieee8021MstpCistPortCistPathCost_Type()
)
ieee8021MstpCistPortCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortCistPathCost.setStatus("current")
_Ieee8021MstpCistPortProtocolMigration_Type = TruthValue
_Ieee8021MstpCistPortProtocolMigration_Object = MibTableColumn
ieee8021MstpCistPortProtocolMigration = _Ieee8021MstpCistPortProtocolMigration_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 18),
    _Ieee8021MstpCistPortProtocolMigration_Type()
)
ieee8021MstpCistPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortProtocolMigration.setStatus("current")


class _Ieee8021MstpCistPortEnableBPDURx_Type(TruthValue):
    """Custom type ieee8021MstpCistPortEnableBPDURx based on TruthValue"""


_Ieee8021MstpCistPortEnableBPDURx_Object = MibTableColumn
ieee8021MstpCistPortEnableBPDURx = _Ieee8021MstpCistPortEnableBPDURx_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 19),
    _Ieee8021MstpCistPortEnableBPDURx_Type()
)
ieee8021MstpCistPortEnableBPDURx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortEnableBPDURx.setStatus("current")


class _Ieee8021MstpCistPortEnableBPDUTx_Type(TruthValue):
    """Custom type ieee8021MstpCistPortEnableBPDUTx based on TruthValue"""


_Ieee8021MstpCistPortEnableBPDUTx_Object = MibTableColumn
ieee8021MstpCistPortEnableBPDUTx = _Ieee8021MstpCistPortEnableBPDUTx_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 20),
    _Ieee8021MstpCistPortEnableBPDUTx_Type()
)
ieee8021MstpCistPortEnableBPDUTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortEnableBPDUTx.setStatus("current")
_Ieee8021MstpCistPortPseudoRootId_Type = BridgeId
_Ieee8021MstpCistPortPseudoRootId_Object = MibTableColumn
ieee8021MstpCistPortPseudoRootId = _Ieee8021MstpCistPortPseudoRootId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 21),
    _Ieee8021MstpCistPortPseudoRootId_Type()
)
ieee8021MstpCistPortPseudoRootId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortPseudoRootId.setStatus("current")


class _Ieee8021MstpCistPortIsL2Gp_Type(TruthValue):
    """Custom type ieee8021MstpCistPortIsL2Gp based on TruthValue"""


_Ieee8021MstpCistPortIsL2Gp_Object = MibTableColumn
ieee8021MstpCistPortIsL2Gp = _Ieee8021MstpCistPortIsL2Gp_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 3, 1, 22),
    _Ieee8021MstpCistPortIsL2Gp_Type()
)
ieee8021MstpCistPortIsL2Gp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortIsL2Gp.setStatus("current")
_Ieee8021MstpPortTable_Object = MibTable
ieee8021MstpPortTable = _Ieee8021MstpPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021MstpPortTable.setStatus("current")
_Ieee8021MstpPortEntry_Object = MibTableRow
ieee8021MstpPortEntry = _Ieee8021MstpPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1)
)
ieee8021MstpPortEntry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpPortComponentId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpPortMstId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpPortNum"),
)
if mibBuilder.loadTexts:
    ieee8021MstpPortEntry.setStatus("current")
_Ieee8021MstpPortComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpPortComponentId_Object = MibTableColumn
ieee8021MstpPortComponentId = _Ieee8021MstpPortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 1),
    _Ieee8021MstpPortComponentId_Type()
)
ieee8021MstpPortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpPortComponentId.setStatus("current")
_Ieee8021MstpPortMstId_Type = IEEE8021MstIdentifier
_Ieee8021MstpPortMstId_Object = MibTableColumn
ieee8021MstpPortMstId = _Ieee8021MstpPortMstId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 2),
    _Ieee8021MstpPortMstId_Type()
)
ieee8021MstpPortMstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpPortMstId.setStatus("current")
_Ieee8021MstpPortNum_Type = IEEE8021BridgePortNumber
_Ieee8021MstpPortNum_Object = MibTableColumn
ieee8021MstpPortNum = _Ieee8021MstpPortNum_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 3),
    _Ieee8021MstpPortNum_Type()
)
ieee8021MstpPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpPortNum.setStatus("current")
_Ieee8021MstpPortUptime_Type = TimeTicks
_Ieee8021MstpPortUptime_Object = MibTableColumn
ieee8021MstpPortUptime = _Ieee8021MstpPortUptime_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 4),
    _Ieee8021MstpPortUptime_Type()
)
ieee8021MstpPortUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortUptime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021MstpPortUptime.setUnits("centi-seconds")


class _Ieee8021MstpPortState_Type(Integer32):
    """Custom type ieee8021MstpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 5),
          ("disabled", 1),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )


_Ieee8021MstpPortState_Type.__name__ = "Integer32"
_Ieee8021MstpPortState_Object = MibTableColumn
ieee8021MstpPortState = _Ieee8021MstpPortState_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 5),
    _Ieee8021MstpPortState_Type()
)
ieee8021MstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortState.setStatus("current")


class _Ieee8021MstpPortPriority_Type(Integer32):
    """Custom type ieee8021MstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Ieee8021MstpPortPriority_Type.__name__ = "Integer32"
_Ieee8021MstpPortPriority_Object = MibTableColumn
ieee8021MstpPortPriority = _Ieee8021MstpPortPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 6),
    _Ieee8021MstpPortPriority_Type()
)
ieee8021MstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpPortPriority.setStatus("current")


class _Ieee8021MstpPortPathCost_Type(Integer32):
    """Custom type ieee8021MstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Ieee8021MstpPortPathCost_Type.__name__ = "Integer32"
_Ieee8021MstpPortPathCost_Object = MibTableColumn
ieee8021MstpPortPathCost = _Ieee8021MstpPortPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 7),
    _Ieee8021MstpPortPathCost_Type()
)
ieee8021MstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpPortPathCost.setStatus("current")
_Ieee8021MstpPortDesignatedRoot_Type = BridgeId
_Ieee8021MstpPortDesignatedRoot_Object = MibTableColumn
ieee8021MstpPortDesignatedRoot = _Ieee8021MstpPortDesignatedRoot_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 8),
    _Ieee8021MstpPortDesignatedRoot_Type()
)
ieee8021MstpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortDesignatedRoot.setStatus("current")
_Ieee8021MstpPortDesignatedCost_Type = Integer32
_Ieee8021MstpPortDesignatedCost_Object = MibTableColumn
ieee8021MstpPortDesignatedCost = _Ieee8021MstpPortDesignatedCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 9),
    _Ieee8021MstpPortDesignatedCost_Type()
)
ieee8021MstpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortDesignatedCost.setStatus("current")
_Ieee8021MstpPortDesignatedBridge_Type = BridgeId
_Ieee8021MstpPortDesignatedBridge_Object = MibTableColumn
ieee8021MstpPortDesignatedBridge = _Ieee8021MstpPortDesignatedBridge_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 10),
    _Ieee8021MstpPortDesignatedBridge_Type()
)
ieee8021MstpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortDesignatedBridge.setStatus("current")
_Ieee8021MstpPortDesignatedPort_Type = IEEE8021BridgePortNumber
_Ieee8021MstpPortDesignatedPort_Object = MibTableColumn
ieee8021MstpPortDesignatedPort = _Ieee8021MstpPortDesignatedPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 11),
    _Ieee8021MstpPortDesignatedPort_Type()
)
ieee8021MstpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortDesignatedPort.setStatus("current")


class _Ieee8021MstpPortRole_Type(Integer32):
    """Custom type ieee8021MstpPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("backup", 4),
          ("designated", 3),
          ("root", 1))
    )


_Ieee8021MstpPortRole_Type.__name__ = "Integer32"
_Ieee8021MstpPortRole_Object = MibTableColumn
ieee8021MstpPortRole = _Ieee8021MstpPortRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 12),
    _Ieee8021MstpPortRole_Type()
)
ieee8021MstpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortRole.setStatus("current")
_Ieee8021MstpPortDisputed_Type = TruthValue
_Ieee8021MstpPortDisputed_Object = MibTableColumn
ieee8021MstpPortDisputed = _Ieee8021MstpPortDisputed_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 13),
    _Ieee8021MstpPortDisputed_Type()
)
ieee8021MstpPortDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpPortDisputed.setStatus("current")


class _Ieee8021MstpPortAdminPathCost_Type(Integer32):
    """Custom type ieee8021MstpPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Ieee8021MstpPortAdminPathCost_Type.__name__ = "Integer32"
_Ieee8021MstpPortAdminPathCost_Object = MibTableColumn
ieee8021MstpPortAdminPathCost = _Ieee8021MstpPortAdminPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 4, 1, 14),
    _Ieee8021MstpPortAdminPathCost_Type()
)
ieee8021MstpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpPortAdminPathCost.setStatus("current")
_Ieee8021MstpFidToMstiTable_Object = MibTable
ieee8021MstpFidToMstiTable = _Ieee8021MstpFidToMstiTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiTable.setStatus("deprecated")
_Ieee8021MstpFidToMstiEntry_Object = MibTableRow
ieee8021MstpFidToMstiEntry = _Ieee8021MstpFidToMstiEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1)
)
ieee8021MstpFidToMstiEntry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiComponentId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiFid"),
)
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiEntry.setStatus("deprecated")
_Ieee8021MstpFidToMstiComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpFidToMstiComponentId_Object = MibTableColumn
ieee8021MstpFidToMstiComponentId = _Ieee8021MstpFidToMstiComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1, 1),
    _Ieee8021MstpFidToMstiComponentId_Type()
)
ieee8021MstpFidToMstiComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiComponentId.setStatus("deprecated")


class _Ieee8021MstpFidToMstiFid_Type(Unsigned32):
    """Custom type ieee8021MstpFidToMstiFid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ieee8021MstpFidToMstiFid_Type.__name__ = "Unsigned32"
_Ieee8021MstpFidToMstiFid_Object = MibTableColumn
ieee8021MstpFidToMstiFid = _Ieee8021MstpFidToMstiFid_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1, 2),
    _Ieee8021MstpFidToMstiFid_Type()
)
ieee8021MstpFidToMstiFid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiFid.setStatus("deprecated")
_Ieee8021MstpFidToMstiMstId_Type = IEEE8021MstIdentifier
_Ieee8021MstpFidToMstiMstId_Object = MibTableColumn
ieee8021MstpFidToMstiMstId = _Ieee8021MstpFidToMstiMstId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 5, 1, 3),
    _Ieee8021MstpFidToMstiMstId_Type()
)
ieee8021MstpFidToMstiMstId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiMstId.setStatus("deprecated")
_Ieee8021MstpVlanTable_Object = MibTable
ieee8021MstpVlanTable = _Ieee8021MstpVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021MstpVlanTable.setStatus("deprecated")
_Ieee8021MstpVlanEntry_Object = MibTableRow
ieee8021MstpVlanEntry = _Ieee8021MstpVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1)
)
ieee8021MstpVlanEntry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanComponentId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanId"),
)
if mibBuilder.loadTexts:
    ieee8021MstpVlanEntry.setStatus("deprecated")
_Ieee8021MstpVlanComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpVlanComponentId_Object = MibTableColumn
ieee8021MstpVlanComponentId = _Ieee8021MstpVlanComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1, 1),
    _Ieee8021MstpVlanComponentId_Type()
)
ieee8021MstpVlanComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpVlanComponentId.setStatus("deprecated")
_Ieee8021MstpVlanId_Type = IEEE8021VlanIndex
_Ieee8021MstpVlanId_Object = MibTableColumn
ieee8021MstpVlanId = _Ieee8021MstpVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1, 2),
    _Ieee8021MstpVlanId_Type()
)
ieee8021MstpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpVlanId.setStatus("deprecated")
_Ieee8021MstpVlanMstId_Type = IEEE8021MstIdentifier
_Ieee8021MstpVlanMstId_Object = MibTableColumn
ieee8021MstpVlanMstId = _Ieee8021MstpVlanMstId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 6, 1, 3),
    _Ieee8021MstpVlanMstId_Type()
)
ieee8021MstpVlanMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpVlanMstId.setStatus("deprecated")
_Ieee8021MstpConfigIdTable_Object = MibTable
ieee8021MstpConfigIdTable = _Ieee8021MstpConfigIdTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021MstpConfigIdTable.setStatus("current")
_Ieee8021MstpConfigIdEntry_Object = MibTableRow
ieee8021MstpConfigIdEntry = _Ieee8021MstpConfigIdEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1)
)
ieee8021MstpConfigIdEntry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpConfigIdComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021MstpConfigIdEntry.setStatus("current")
_Ieee8021MstpConfigIdComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpConfigIdComponentId_Object = MibTableColumn
ieee8021MstpConfigIdComponentId = _Ieee8021MstpConfigIdComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 1),
    _Ieee8021MstpConfigIdComponentId_Type()
)
ieee8021MstpConfigIdComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpConfigIdComponentId.setStatus("current")


class _Ieee8021MstpConfigIdFormatSelector_Type(Integer32):
    """Custom type ieee8021MstpConfigIdFormatSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Ieee8021MstpConfigIdFormatSelector_Type.__name__ = "Integer32"
_Ieee8021MstpConfigIdFormatSelector_Object = MibTableColumn
ieee8021MstpConfigIdFormatSelector = _Ieee8021MstpConfigIdFormatSelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 2),
    _Ieee8021MstpConfigIdFormatSelector_Type()
)
ieee8021MstpConfigIdFormatSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpConfigIdFormatSelector.setStatus("current")


class _Ieee8021MstpConfigurationName_Type(SnmpAdminString):
    """Custom type ieee8021MstpConfigurationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Ieee8021MstpConfigurationName_Type.__name__ = "SnmpAdminString"
_Ieee8021MstpConfigurationName_Object = MibTableColumn
ieee8021MstpConfigurationName = _Ieee8021MstpConfigurationName_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 3),
    _Ieee8021MstpConfigurationName_Type()
)
ieee8021MstpConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpConfigurationName.setStatus("current")


class _Ieee8021MstpRevisionLevel_Type(Unsigned32):
    """Custom type ieee8021MstpRevisionLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021MstpRevisionLevel_Type.__name__ = "Unsigned32"
_Ieee8021MstpRevisionLevel_Object = MibTableColumn
ieee8021MstpRevisionLevel = _Ieee8021MstpRevisionLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 4),
    _Ieee8021MstpRevisionLevel_Type()
)
ieee8021MstpRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpRevisionLevel.setStatus("current")


class _Ieee8021MstpConfigurationDigest_Type(OctetString):
    """Custom type ieee8021MstpConfigurationDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Ieee8021MstpConfigurationDigest_Type.__name__ = "OctetString"
_Ieee8021MstpConfigurationDigest_Object = MibTableColumn
ieee8021MstpConfigurationDigest = _Ieee8021MstpConfigurationDigest_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 7, 1, 5),
    _Ieee8021MstpConfigurationDigest_Type()
)
ieee8021MstpConfigurationDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpConfigurationDigest.setStatus("current")
_Ieee8021MstpCistPortExtensionTable_Object = MibTable
ieee8021MstpCistPortExtensionTable = _Ieee8021MstpCistPortExtensionTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 8)
)
if mibBuilder.loadTexts:
    ieee8021MstpCistPortExtensionTable.setStatus("current")
_Ieee8021MstpCistPortExtensionEntry_Object = MibTableRow
ieee8021MstpCistPortExtensionEntry = _Ieee8021MstpCistPortExtensionEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ieee8021MstpCistPortExtensionEntry.setStatus("current")
_Ieee8021MstpCistPortAutoEdgePort_Type = TruthValue
_Ieee8021MstpCistPortAutoEdgePort_Object = MibTableColumn
ieee8021MstpCistPortAutoEdgePort = _Ieee8021MstpCistPortAutoEdgePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 8, 1, 1),
    _Ieee8021MstpCistPortAutoEdgePort_Type()
)
ieee8021MstpCistPortAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortAutoEdgePort.setStatus("current")
_Ieee8021MstpCistPortAutoIsolatePort_Type = TruthValue
_Ieee8021MstpCistPortAutoIsolatePort_Object = MibTableColumn
ieee8021MstpCistPortAutoIsolatePort = _Ieee8021MstpCistPortAutoIsolatePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 8, 1, 2),
    _Ieee8021MstpCistPortAutoIsolatePort_Type()
)
ieee8021MstpCistPortAutoIsolatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpCistPortAutoIsolatePort.setStatus("current")
_Ieee8021MstpFidToMstiV2Table_Object = MibTable
ieee8021MstpFidToMstiV2Table = _Ieee8021MstpFidToMstiV2Table_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 9)
)
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiV2Table.setStatus("current")
_Ieee8021MstpFidToMstiV2Entry_Object = MibTableRow
ieee8021MstpFidToMstiV2Entry = _Ieee8021MstpFidToMstiV2Entry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1)
)
ieee8021MstpFidToMstiV2Entry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiV2ComponentId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiV2Fid"),
)
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiV2Entry.setStatus("current")
_Ieee8021MstpFidToMstiV2ComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpFidToMstiV2ComponentId_Object = MibTableColumn
ieee8021MstpFidToMstiV2ComponentId = _Ieee8021MstpFidToMstiV2ComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1, 1),
    _Ieee8021MstpFidToMstiV2ComponentId_Type()
)
ieee8021MstpFidToMstiV2ComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiV2ComponentId.setStatus("current")


class _Ieee8021MstpFidToMstiV2Fid_Type(Unsigned32):
    """Custom type ieee8021MstpFidToMstiV2Fid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Ieee8021MstpFidToMstiV2Fid_Type.__name__ = "Unsigned32"
_Ieee8021MstpFidToMstiV2Fid_Object = MibTableColumn
ieee8021MstpFidToMstiV2Fid = _Ieee8021MstpFidToMstiV2Fid_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1, 2),
    _Ieee8021MstpFidToMstiV2Fid_Type()
)
ieee8021MstpFidToMstiV2Fid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiV2Fid.setStatus("current")


class _Ieee8021MstpFidToMstiV2MstId_Type(Unsigned32):
    """Custom type ieee8021MstpFidToMstiV2MstId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ieee8021MstpFidToMstiV2MstId_Type.__name__ = "Unsigned32"
_Ieee8021MstpFidToMstiV2MstId_Object = MibTableColumn
ieee8021MstpFidToMstiV2MstId = _Ieee8021MstpFidToMstiV2MstId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 9, 1, 3),
    _Ieee8021MstpFidToMstiV2MstId_Type()
)
ieee8021MstpFidToMstiV2MstId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiV2MstId.setStatus("current")
_Ieee8021MstpVlanV2Table_Object = MibTable
ieee8021MstpVlanV2Table = _Ieee8021MstpVlanV2Table_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 10)
)
if mibBuilder.loadTexts:
    ieee8021MstpVlanV2Table.setStatus("current")
_Ieee8021MstpVlanV2Entry_Object = MibTableRow
ieee8021MstpVlanV2Entry = _Ieee8021MstpVlanV2Entry_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1)
)
ieee8021MstpVlanV2Entry.setIndexNames(
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanV2ComponentId"),
    (0, "IEEE8021-MSTP-MIB", "ieee8021MstpVlanV2Id"),
)
if mibBuilder.loadTexts:
    ieee8021MstpVlanV2Entry.setStatus("current")
_Ieee8021MstpVlanV2ComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021MstpVlanV2ComponentId_Object = MibTableColumn
ieee8021MstpVlanV2ComponentId = _Ieee8021MstpVlanV2ComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1, 1),
    _Ieee8021MstpVlanV2ComponentId_Type()
)
ieee8021MstpVlanV2ComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpVlanV2ComponentId.setStatus("current")
_Ieee8021MstpVlanV2Id_Type = IEEE8021VlanIndex
_Ieee8021MstpVlanV2Id_Object = MibTableColumn
ieee8021MstpVlanV2Id = _Ieee8021MstpVlanV2Id_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1, 2),
    _Ieee8021MstpVlanV2Id_Type()
)
ieee8021MstpVlanV2Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021MstpVlanV2Id.setStatus("current")


class _Ieee8021MstpVlanV2MstId_Type(Unsigned32):
    """Custom type ieee8021MstpVlanV2MstId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Ieee8021MstpVlanV2MstId_Type.__name__ = "Unsigned32"
_Ieee8021MstpVlanV2MstId_Object = MibTableColumn
ieee8021MstpVlanV2MstId = _Ieee8021MstpVlanV2MstId_Object(
    (1, 3, 111, 2, 802, 1, 1, 6, 1, 10, 1, 3),
    _Ieee8021MstpVlanV2MstId_Type()
)
ieee8021MstpVlanV2MstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021MstpVlanV2MstId.setStatus("current")
_Ieee8021MstpConformance_ObjectIdentity = ObjectIdentity
ieee8021MstpConformance = _Ieee8021MstpConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 6, 2)
)
_Ieee8021MstpGroups_ObjectIdentity = ObjectIdentity
ieee8021MstpGroups = _Ieee8021MstpGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1)
)
_Ieee8021MstpCompliances_ObjectIdentity = ObjectIdentity
ieee8021MstpCompliances = _Ieee8021MstpCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 2)
)
ieee8021MstpCistPortEntry.registerAugmentions(
    ("IEEE8021-MSTP-MIB",
     "ieee8021MstpCistPortExtensionEntry")
)
ieee8021MstpCistPortExtensionEntry.setIndexNames(*ieee8021MstpCistPortEntry.getIndexNames())

# Managed Objects groups

ieee8021MstpCistGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 1)
)
ieee8021MstpCistGroup.setObjects(
      *(("IEEE8021-MSTP-MIB", "ieee8021MstpCistBridgeIdentifier"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistTopologyChange"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistRegionalRootIdentifier"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPathCost"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistMaxHops"))
)
if mibBuilder.loadTexts:
    ieee8021MstpCistGroup.setStatus("current")

ieee8021MstpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 2)
)
ieee8021MstpGroup.setObjects(
      *(("IEEE8021-MSTP-MIB", "ieee8021MstpBridgeId"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpTimeSinceTopologyChange"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpTopologyChanges"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpTopologyChange"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpDesignatedRoot"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpRootPathCost"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpRootPort"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpBridgePriority"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpVids0"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpVids1"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpVids2"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpVids3"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021MstpGroup.setStatus("current")

ieee8021MstpCistPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 3)
)
ieee8021MstpCistPortGroup.setObjects(
      *(("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortUptime"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAdminPathCost"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortDesignatedRoot"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortTopologyChangeAck"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortHelloTime"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAdminEdgePort"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortOperEdgePort"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortMacEnabled"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortMacOperational"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortRestrictedRole"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortRestrictedTcn"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortRole"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortDisputed"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortCistRegionalRootId"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortCistPathCost"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortProtocolMigration"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortEnableBPDURx"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortEnableBPDUTx"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortPseudoRootId"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortIsL2Gp"))
)
if mibBuilder.loadTexts:
    ieee8021MstpCistPortGroup.setStatus("current")

ieee8021MstpPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 4)
)
ieee8021MstpPortGroup.setObjects(
      *(("IEEE8021-MSTP-MIB", "ieee8021MstpPortUptime"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortState"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortPriority"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortPathCost"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedRoot"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedCost"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedBridge"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDesignatedPort"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortRole"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortDisputed"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpPortAdminPathCost"))
)
if mibBuilder.loadTexts:
    ieee8021MstpPortGroup.setStatus("current")

ieee8021MstpFidToMstiGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 5)
)
ieee8021MstpFidToMstiGroup.setObjects(
    ("IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiMstId")
)
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiGroup.setStatus("deprecated")

ieee8021MstpVlanGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 6)
)
ieee8021MstpVlanGroup.setObjects(
    ("IEEE8021-MSTP-MIB", "ieee8021MstpVlanMstId")
)
if mibBuilder.loadTexts:
    ieee8021MstpVlanGroup.setStatus("deprecated")

ieee8021MstpConfigIdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 7)
)
ieee8021MstpConfigIdGroup.setObjects(
      *(("IEEE8021-MSTP-MIB", "ieee8021MstpConfigIdFormatSelector"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpConfigurationName"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpRevisionLevel"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpConfigurationDigest"))
)
if mibBuilder.loadTexts:
    ieee8021MstpConfigIdGroup.setStatus("current")

ieee8021MstpCistPortExtensionGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 8)
)
ieee8021MstpCistPortExtensionGroup.setObjects(
      *(("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAutoEdgePort"),
        ("IEEE8021-MSTP-MIB", "ieee8021MstpCistPortAutoIsolatePort"))
)
if mibBuilder.loadTexts:
    ieee8021MstpCistPortExtensionGroup.setStatus("current")

ieee8021MstpFidToMstiV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 9)
)
ieee8021MstpFidToMstiV2Group.setObjects(
    ("IEEE8021-MSTP-MIB", "ieee8021MstpFidToMstiV2MstId")
)
if mibBuilder.loadTexts:
    ieee8021MstpFidToMstiV2Group.setStatus("current")

ieee8021MstpVlanV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 1, 10)
)
ieee8021MstpVlanV2Group.setObjects(
    ("IEEE8021-MSTP-MIB", "ieee8021MstpVlanV2MstId")
)
if mibBuilder.loadTexts:
    ieee8021MstpVlanV2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021MstpCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021MstpCompliance.setStatus(
        "deprecated"
    )

ieee8021MstpComplianceV2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021MstpComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-MSTP-MIB",
    **{"ieee8021MstpMib": ieee8021MstpMib,
       "ieee8021MstpNotifications": ieee8021MstpNotifications,
       "ieee8021MstpObjects": ieee8021MstpObjects,
       "ieee8021MstpCistTable": ieee8021MstpCistTable,
       "ieee8021MstpCistEntry": ieee8021MstpCistEntry,
       "ieee8021MstpCistComponentId": ieee8021MstpCistComponentId,
       "ieee8021MstpCistBridgeIdentifier": ieee8021MstpCistBridgeIdentifier,
       "ieee8021MstpCistTopologyChange": ieee8021MstpCistTopologyChange,
       "ieee8021MstpCistRegionalRootIdentifier": ieee8021MstpCistRegionalRootIdentifier,
       "ieee8021MstpCistPathCost": ieee8021MstpCistPathCost,
       "ieee8021MstpCistMaxHops": ieee8021MstpCistMaxHops,
       "ieee8021MstpTable": ieee8021MstpTable,
       "ieee8021MstpEntry": ieee8021MstpEntry,
       "ieee8021MstpComponentId": ieee8021MstpComponentId,
       "ieee8021MstpId": ieee8021MstpId,
       "ieee8021MstpBridgeId": ieee8021MstpBridgeId,
       "ieee8021MstpTimeSinceTopologyChange": ieee8021MstpTimeSinceTopologyChange,
       "ieee8021MstpTopologyChanges": ieee8021MstpTopologyChanges,
       "ieee8021MstpTopologyChange": ieee8021MstpTopologyChange,
       "ieee8021MstpDesignatedRoot": ieee8021MstpDesignatedRoot,
       "ieee8021MstpRootPathCost": ieee8021MstpRootPathCost,
       "ieee8021MstpRootPort": ieee8021MstpRootPort,
       "ieee8021MstpBridgePriority": ieee8021MstpBridgePriority,
       "ieee8021MstpVids0": ieee8021MstpVids0,
       "ieee8021MstpVids1": ieee8021MstpVids1,
       "ieee8021MstpVids2": ieee8021MstpVids2,
       "ieee8021MstpVids3": ieee8021MstpVids3,
       "ieee8021MstpRowStatus": ieee8021MstpRowStatus,
       "ieee8021MstpCistPortTable": ieee8021MstpCistPortTable,
       "ieee8021MstpCistPortEntry": ieee8021MstpCistPortEntry,
       "ieee8021MstpCistPortComponentId": ieee8021MstpCistPortComponentId,
       "ieee8021MstpCistPortNum": ieee8021MstpCistPortNum,
       "ieee8021MstpCistPortUptime": ieee8021MstpCistPortUptime,
       "ieee8021MstpCistPortAdminPathCost": ieee8021MstpCistPortAdminPathCost,
       "ieee8021MstpCistPortDesignatedRoot": ieee8021MstpCistPortDesignatedRoot,
       "ieee8021MstpCistPortTopologyChangeAck": ieee8021MstpCistPortTopologyChangeAck,
       "ieee8021MstpCistPortHelloTime": ieee8021MstpCistPortHelloTime,
       "ieee8021MstpCistPortAdminEdgePort": ieee8021MstpCistPortAdminEdgePort,
       "ieee8021MstpCistPortOperEdgePort": ieee8021MstpCistPortOperEdgePort,
       "ieee8021MstpCistPortMacEnabled": ieee8021MstpCistPortMacEnabled,
       "ieee8021MstpCistPortMacOperational": ieee8021MstpCistPortMacOperational,
       "ieee8021MstpCistPortRestrictedRole": ieee8021MstpCistPortRestrictedRole,
       "ieee8021MstpCistPortRestrictedTcn": ieee8021MstpCistPortRestrictedTcn,
       "ieee8021MstpCistPortRole": ieee8021MstpCistPortRole,
       "ieee8021MstpCistPortDisputed": ieee8021MstpCistPortDisputed,
       "ieee8021MstpCistPortCistRegionalRootId": ieee8021MstpCistPortCistRegionalRootId,
       "ieee8021MstpCistPortCistPathCost": ieee8021MstpCistPortCistPathCost,
       "ieee8021MstpCistPortProtocolMigration": ieee8021MstpCistPortProtocolMigration,
       "ieee8021MstpCistPortEnableBPDURx": ieee8021MstpCistPortEnableBPDURx,
       "ieee8021MstpCistPortEnableBPDUTx": ieee8021MstpCistPortEnableBPDUTx,
       "ieee8021MstpCistPortPseudoRootId": ieee8021MstpCistPortPseudoRootId,
       "ieee8021MstpCistPortIsL2Gp": ieee8021MstpCistPortIsL2Gp,
       "ieee8021MstpPortTable": ieee8021MstpPortTable,
       "ieee8021MstpPortEntry": ieee8021MstpPortEntry,
       "ieee8021MstpPortComponentId": ieee8021MstpPortComponentId,
       "ieee8021MstpPortMstId": ieee8021MstpPortMstId,
       "ieee8021MstpPortNum": ieee8021MstpPortNum,
       "ieee8021MstpPortUptime": ieee8021MstpPortUptime,
       "ieee8021MstpPortState": ieee8021MstpPortState,
       "ieee8021MstpPortPriority": ieee8021MstpPortPriority,
       "ieee8021MstpPortPathCost": ieee8021MstpPortPathCost,
       "ieee8021MstpPortDesignatedRoot": ieee8021MstpPortDesignatedRoot,
       "ieee8021MstpPortDesignatedCost": ieee8021MstpPortDesignatedCost,
       "ieee8021MstpPortDesignatedBridge": ieee8021MstpPortDesignatedBridge,
       "ieee8021MstpPortDesignatedPort": ieee8021MstpPortDesignatedPort,
       "ieee8021MstpPortRole": ieee8021MstpPortRole,
       "ieee8021MstpPortDisputed": ieee8021MstpPortDisputed,
       "ieee8021MstpPortAdminPathCost": ieee8021MstpPortAdminPathCost,
       "ieee8021MstpFidToMstiTable": ieee8021MstpFidToMstiTable,
       "ieee8021MstpFidToMstiEntry": ieee8021MstpFidToMstiEntry,
       "ieee8021MstpFidToMstiComponentId": ieee8021MstpFidToMstiComponentId,
       "ieee8021MstpFidToMstiFid": ieee8021MstpFidToMstiFid,
       "ieee8021MstpFidToMstiMstId": ieee8021MstpFidToMstiMstId,
       "ieee8021MstpVlanTable": ieee8021MstpVlanTable,
       "ieee8021MstpVlanEntry": ieee8021MstpVlanEntry,
       "ieee8021MstpVlanComponentId": ieee8021MstpVlanComponentId,
       "ieee8021MstpVlanId": ieee8021MstpVlanId,
       "ieee8021MstpVlanMstId": ieee8021MstpVlanMstId,
       "ieee8021MstpConfigIdTable": ieee8021MstpConfigIdTable,
       "ieee8021MstpConfigIdEntry": ieee8021MstpConfigIdEntry,
       "ieee8021MstpConfigIdComponentId": ieee8021MstpConfigIdComponentId,
       "ieee8021MstpConfigIdFormatSelector": ieee8021MstpConfigIdFormatSelector,
       "ieee8021MstpConfigurationName": ieee8021MstpConfigurationName,
       "ieee8021MstpRevisionLevel": ieee8021MstpRevisionLevel,
       "ieee8021MstpConfigurationDigest": ieee8021MstpConfigurationDigest,
       "ieee8021MstpCistPortExtensionTable": ieee8021MstpCistPortExtensionTable,
       "ieee8021MstpCistPortExtensionEntry": ieee8021MstpCistPortExtensionEntry,
       "ieee8021MstpCistPortAutoEdgePort": ieee8021MstpCistPortAutoEdgePort,
       "ieee8021MstpCistPortAutoIsolatePort": ieee8021MstpCistPortAutoIsolatePort,
       "ieee8021MstpFidToMstiV2Table": ieee8021MstpFidToMstiV2Table,
       "ieee8021MstpFidToMstiV2Entry": ieee8021MstpFidToMstiV2Entry,
       "ieee8021MstpFidToMstiV2ComponentId": ieee8021MstpFidToMstiV2ComponentId,
       "ieee8021MstpFidToMstiV2Fid": ieee8021MstpFidToMstiV2Fid,
       "ieee8021MstpFidToMstiV2MstId": ieee8021MstpFidToMstiV2MstId,
       "ieee8021MstpVlanV2Table": ieee8021MstpVlanV2Table,
       "ieee8021MstpVlanV2Entry": ieee8021MstpVlanV2Entry,
       "ieee8021MstpVlanV2ComponentId": ieee8021MstpVlanV2ComponentId,
       "ieee8021MstpVlanV2Id": ieee8021MstpVlanV2Id,
       "ieee8021MstpVlanV2MstId": ieee8021MstpVlanV2MstId,
       "ieee8021MstpConformance": ieee8021MstpConformance,
       "ieee8021MstpGroups": ieee8021MstpGroups,
       "ieee8021MstpCistGroup": ieee8021MstpCistGroup,
       "ieee8021MstpGroup": ieee8021MstpGroup,
       "ieee8021MstpCistPortGroup": ieee8021MstpCistPortGroup,
       "ieee8021MstpPortGroup": ieee8021MstpPortGroup,
       "ieee8021MstpFidToMstiGroup": ieee8021MstpFidToMstiGroup,
       "ieee8021MstpVlanGroup": ieee8021MstpVlanGroup,
       "ieee8021MstpConfigIdGroup": ieee8021MstpConfigIdGroup,
       "ieee8021MstpCistPortExtensionGroup": ieee8021MstpCistPortExtensionGroup,
       "ieee8021MstpFidToMstiV2Group": ieee8021MstpFidToMstiV2Group,
       "ieee8021MstpVlanV2Group": ieee8021MstpVlanV2Group,
       "ieee8021MstpCompliances": ieee8021MstpCompliances,
       "ieee8021MstpCompliance": ieee8021MstpCompliance,
       "ieee8021MstpComplianceV2": ieee8021MstpComplianceV2}
)
