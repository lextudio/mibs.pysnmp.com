# SNMP MIB module (WLSX-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-MESH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:07 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaEncryptionMethods,
 ArubaMeshRole,
 ArubaPhyType) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaEncryptionMethods",
    "ArubaMeshRole",
    "ArubaPhyType")

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
 snmpModules) = mibBuilder.importSymbols(
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
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")

(wlanAPMacAddress,) = mibBuilder.importSymbols(
    "WLSX-WLAN-MIB",
    "wlanAPMacAddress")


# MODULE-IDENTITY

wlsxMeshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13)
)
wlsxMeshMIB.setRevisions(
        ("1907-08-06 05:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxMeshInfoGroup_ObjectIdentity = ObjectIdentity
wlsxMeshInfoGroup = _WlsxMeshInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1)
)
_WlsxMeshNodeGroup_ObjectIdentity = ObjectIdentity
wlsxMeshNodeGroup = _WlsxMeshNodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1)
)
_WlsxMeshNodeTotal_Type = Unsigned32
_WlsxMeshNodeTotal_Object = MibScalar
wlsxMeshNodeTotal = _WlsxMeshNodeTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 1),
    _WlsxMeshNodeTotal_Type()
)
wlsxMeshNodeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeTotal.setStatus("current")
_WlsxMeshNodeTable_Object = MibTable
wlsxMeshNodeTable = _WlsxMeshNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxMeshNodeTable.setStatus("current")
_WlsxMeshNodeEntry_Object = MibTableRow
wlsxMeshNodeEntry = _WlsxMeshNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1)
)
wlsxMeshNodeEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
)
if mibBuilder.loadTexts:
    wlsxMeshNodeEntry.setStatus("current")
_WlsxMeshRole_Type = ArubaMeshRole
_WlsxMeshRole_Object = MibTableColumn
wlsxMeshRole = _WlsxMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 1),
    _WlsxMeshRole_Type()
)
wlsxMeshRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxMeshRole.setStatus("current")
_WlsxMeshNodeParent_Type = MacAddress
_WlsxMeshNodeParent_Object = MibTableColumn
wlsxMeshNodeParent = _WlsxMeshNodeParent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 2),
    _WlsxMeshNodeParent_Type()
)
wlsxMeshNodeParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeParent.setStatus("current")
_WlsxMeshNodeChildrenCount_Type = Unsigned32
_WlsxMeshNodeChildrenCount_Object = MibTableColumn
wlsxMeshNodeChildrenCount = _WlsxMeshNodeChildrenCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 3),
    _WlsxMeshNodeChildrenCount_Type()
)
wlsxMeshNodeChildrenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeChildrenCount.setStatus("current")


class _WlsxMeshNodeCluster_Type(DisplayString):
    """Custom type wlsxMeshNodeCluster based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxMeshNodeCluster_Type.__name__ = "DisplayString"
_WlsxMeshNodeCluster_Object = MibTableColumn
wlsxMeshNodeCluster = _WlsxMeshNodeCluster_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 4),
    _WlsxMeshNodeCluster_Type()
)
wlsxMeshNodeCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeCluster.setStatus("current")
_WlsxMeshNodeRfBand_Type = ArubaPhyType
_WlsxMeshNodeRfBand_Object = MibTableColumn
wlsxMeshNodeRfBand = _WlsxMeshNodeRfBand_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 5),
    _WlsxMeshNodeRfBand_Type()
)
wlsxMeshNodeRfBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeRfBand.setStatus("current")
_WlsxMeshNodePathCost_Type = Integer32
_WlsxMeshNodePathCost_Object = MibTableColumn
wlsxMeshNodePathCost = _WlsxMeshNodePathCost_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 6),
    _WlsxMeshNodePathCost_Type()
)
wlsxMeshNodePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodePathCost.setStatus("current")
_WlsxMeshNodeNodeCost_Type = Integer32
_WlsxMeshNodeNodeCost_Object = MibTableColumn
wlsxMeshNodeNodeCost = _WlsxMeshNodeNodeCost_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 7),
    _WlsxMeshNodeNodeCost_Type()
)
wlsxMeshNodeNodeCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeNodeCost.setStatus("current")
_WlsxMeshNodeLinkCost_Type = Integer32
_WlsxMeshNodeLinkCost_Object = MibTableColumn
wlsxMeshNodeLinkCost = _WlsxMeshNodeLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 8),
    _WlsxMeshNodeLinkCost_Type()
)
wlsxMeshNodeLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeLinkCost.setStatus("current")
_WlsxMeshNodeHopCount_Type = Integer32
_WlsxMeshNodeHopCount_Object = MibTableColumn
wlsxMeshNodeHopCount = _WlsxMeshNodeHopCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 9),
    _WlsxMeshNodeHopCount_Type()
)
wlsxMeshNodeHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNodeHopCount.setStatus("current")
_WlsxMeshSNR_Type = Unsigned32
_WlsxMeshSNR_Object = MibTableColumn
wlsxMeshSNR = _WlsxMeshSNR_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 10),
    _WlsxMeshSNR_Type()
)
wlsxMeshSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshSNR.setStatus("current")
_WlsxMeshTxRate_Type = Unsigned32
_WlsxMeshTxRate_Object = MibTableColumn
wlsxMeshTxRate = _WlsxMeshTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 11),
    _WlsxMeshTxRate_Type()
)
wlsxMeshTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshTxRate.setStatus("current")
_WlsxMeshRxRate_Type = Unsigned32
_WlsxMeshRxRate_Object = MibTableColumn
wlsxMeshRxRate = _WlsxMeshRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 12),
    _WlsxMeshRxRate_Type()
)
wlsxMeshRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshRxRate.setStatus("current")
_WlsxMeshUplinkAge_Type = TimeTicks
_WlsxMeshUplinkAge_Object = MibTableColumn
wlsxMeshUplinkAge = _WlsxMeshUplinkAge_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 13),
    _WlsxMeshUplinkAge_Type()
)
wlsxMeshUplinkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshUplinkAge.setStatus("current")
_WlsxMeshNumRecoveryChildren_Type = Unsigned32
_WlsxMeshNumRecoveryChildren_Object = MibTableColumn
wlsxMeshNumRecoveryChildren = _WlsxMeshNumRecoveryChildren_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 14),
    _WlsxMeshNumRecoveryChildren_Type()
)
wlsxMeshNumRecoveryChildren.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshNumRecoveryChildren.setStatus("current")
_WlsxMeshTopologyUpdateAge_Type = TimeTicks
_WlsxMeshTopologyUpdateAge_Object = MibTableColumn
wlsxMeshTopologyUpdateAge = _WlsxMeshTopologyUpdateAge_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 15),
    _WlsxMeshTopologyUpdateAge_Type()
)
wlsxMeshTopologyUpdateAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshTopologyUpdateAge.setStatus("current")
_WlsxMeshIsRecovery_Type = TruthValue
_WlsxMeshIsRecovery_Object = MibTableColumn
wlsxMeshIsRecovery = _WlsxMeshIsRecovery_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 16),
    _WlsxMeshIsRecovery_Type()
)
wlsxMeshIsRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshIsRecovery.setStatus("current")
_WlsxMeshIs11n_Type = TruthValue
_WlsxMeshIs11n_Object = MibTableColumn
wlsxMeshIs11n = _WlsxMeshIs11n_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 13, 1, 1, 2, 1, 17),
    _WlsxMeshIs11n_Type()
)
wlsxMeshIs11n.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxMeshIs11n.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-MESH-MIB",
    **{"wlsxMeshMIB": wlsxMeshMIB,
       "wlsxMeshInfoGroup": wlsxMeshInfoGroup,
       "wlsxMeshNodeGroup": wlsxMeshNodeGroup,
       "wlsxMeshNodeTotal": wlsxMeshNodeTotal,
       "wlsxMeshNodeTable": wlsxMeshNodeTable,
       "wlsxMeshNodeEntry": wlsxMeshNodeEntry,
       "wlsxMeshRole": wlsxMeshRole,
       "wlsxMeshNodeParent": wlsxMeshNodeParent,
       "wlsxMeshNodeChildrenCount": wlsxMeshNodeChildrenCount,
       "wlsxMeshNodeCluster": wlsxMeshNodeCluster,
       "wlsxMeshNodeRfBand": wlsxMeshNodeRfBand,
       "wlsxMeshNodePathCost": wlsxMeshNodePathCost,
       "wlsxMeshNodeNodeCost": wlsxMeshNodeNodeCost,
       "wlsxMeshNodeLinkCost": wlsxMeshNodeLinkCost,
       "wlsxMeshNodeHopCount": wlsxMeshNodeHopCount,
       "wlsxMeshSNR": wlsxMeshSNR,
       "wlsxMeshTxRate": wlsxMeshTxRate,
       "wlsxMeshRxRate": wlsxMeshRxRate,
       "wlsxMeshUplinkAge": wlsxMeshUplinkAge,
       "wlsxMeshNumRecoveryChildren": wlsxMeshNumRecoveryChildren,
       "wlsxMeshTopologyUpdateAge": wlsxMeshTopologyUpdateAge,
       "wlsxMeshIsRecovery": wlsxMeshIsRecovery,
       "wlsxMeshIs11n": wlsxMeshIs11n}
)
