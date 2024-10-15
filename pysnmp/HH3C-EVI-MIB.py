# SNMP MIB module (HH3C-EVI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EVI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:14 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IsisSystemID,) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "IsisSystemID")

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


# MODULE-IDENTITY

hh3cEvi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132)
)
hh3cEvi.setRevisions(
        ("2013-04-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cEviMacType(Integer32, TextualConvention):
    status = "current"
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
        *(("dynamic", 2),
          ("flood", 4),
          ("other", 1),
          ("static", 3))
    )



class Hh3cEviNeighborStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_Hh3cEviNotifications_ObjectIdentity = ObjectIdentity
hh3cEviNotifications = _Hh3cEviNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 0)
)
_Hh3cEviObjects_ObjectIdentity = ObjectIdentity
hh3cEviObjects = _Hh3cEviObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1)
)
_Hh3cEviBase_ObjectIdentity = ObjectIdentity
hh3cEviBase = _Hh3cEviBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 1)
)


class _Hh3cEviDesignatedVlan_Type(VlanId):
    """Custom type hh3cEviDesignatedVlan based on VlanId"""
    defaultValue = 1


_Hh3cEviDesignatedVlan_Object = MibScalar
hh3cEviDesignatedVlan = _Hh3cEviDesignatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 1, 1),
    _Hh3cEviDesignatedVlan_Type()
)
hh3cEviDesignatedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviDesignatedVlan.setStatus("current")


class _Hh3cEviSiteID_Type(Integer32):
    """Custom type hh3cEviSiteID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cEviSiteID_Type.__name__ = "Integer32"
_Hh3cEviSiteID_Object = MibScalar
hh3cEviSiteID = _Hh3cEviSiteID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 1, 2),
    _Hh3cEviSiteID_Type()
)
hh3cEviSiteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviSiteID.setStatus("current")
_Hh3cEviIf_ObjectIdentity = ObjectIdentity
hh3cEviIf = _Hh3cEviIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2)
)
_Hh3cEviIfExtendVlanTable_Object = MibTable
hh3cEviIfExtendVlanTable = _Hh3cEviIfExtendVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cEviIfExtendVlanTable.setStatus("current")
_Hh3cEviIfExtendVlanEntry_Object = MibTableRow
hh3cEviIfExtendVlanEntry = _Hh3cEviIfExtendVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 1, 1)
)
hh3cEviIfExtendVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviIfExtendVlanIndex"),
)
if mibBuilder.loadTexts:
    hh3cEviIfExtendVlanEntry.setStatus("current")
_Hh3cEviIfExtendVlanIndex_Type = VlanId
_Hh3cEviIfExtendVlanIndex_Object = MibTableColumn
hh3cEviIfExtendVlanIndex = _Hh3cEviIfExtendVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 1, 1, 1),
    _Hh3cEviIfExtendVlanIndex_Type()
)
hh3cEviIfExtendVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviIfExtendVlanIndex.setStatus("current")


class _Hh3cEviIfExtendVlanLAV_Type(TruthValue):
    """Custom type hh3cEviIfExtendVlanLAV based on TruthValue"""


_Hh3cEviIfExtendVlanLAV_Object = MibTableColumn
hh3cEviIfExtendVlanLAV = _Hh3cEviIfExtendVlanLAV_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 1, 1, 2),
    _Hh3cEviIfExtendVlanLAV_Type()
)
hh3cEviIfExtendVlanLAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviIfExtendVlanLAV.setStatus("current")
_Hh3cEviIfExtendVlanRowStatus_Type = RowStatus
_Hh3cEviIfExtendVlanRowStatus_Object = MibTableColumn
hh3cEviIfExtendVlanRowStatus = _Hh3cEviIfExtendVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 1, 1, 3),
    _Hh3cEviIfExtendVlanRowStatus_Type()
)
hh3cEviIfExtendVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEviIfExtendVlanRowStatus.setStatus("current")
_Hh3cEviIfVlanMappingTable_Object = MibTable
hh3cEviIfVlanMappingTable = _Hh3cEviIfVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cEviIfVlanMappingTable.setStatus("current")
_Hh3cEviIfVlanMappingEntry_Object = MibTableRow
hh3cEviIfVlanMappingEntry = _Hh3cEviIfVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 2, 1)
)
hh3cEviIfVlanMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviIfVlanMappingSiteId"),
    (0, "HH3C-EVI-MIB", "hh3cEviIfVlanMappingSrc"),
    (0, "HH3C-EVI-MIB", "hh3cEviIfVlanMappingDst"),
)
if mibBuilder.loadTexts:
    hh3cEviIfVlanMappingEntry.setStatus("current")


class _Hh3cEviIfVlanMappingSiteId_Type(Integer32):
    """Custom type hh3cEviIfVlanMappingSiteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cEviIfVlanMappingSiteId_Type.__name__ = "Integer32"
_Hh3cEviIfVlanMappingSiteId_Object = MibTableColumn
hh3cEviIfVlanMappingSiteId = _Hh3cEviIfVlanMappingSiteId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 2, 1, 1),
    _Hh3cEviIfVlanMappingSiteId_Type()
)
hh3cEviIfVlanMappingSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviIfVlanMappingSiteId.setStatus("current")
_Hh3cEviIfVlanMappingSrc_Type = VlanId
_Hh3cEviIfVlanMappingSrc_Object = MibTableColumn
hh3cEviIfVlanMappingSrc = _Hh3cEviIfVlanMappingSrc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 2, 1, 2),
    _Hh3cEviIfVlanMappingSrc_Type()
)
hh3cEviIfVlanMappingSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviIfVlanMappingSrc.setStatus("current")
_Hh3cEviIfVlanMappingDst_Type = VlanId
_Hh3cEviIfVlanMappingDst_Object = MibTableColumn
hh3cEviIfVlanMappingDst = _Hh3cEviIfVlanMappingDst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 2, 1, 3),
    _Hh3cEviIfVlanMappingDst_Type()
)
hh3cEviIfVlanMappingDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviIfVlanMappingDst.setStatus("current")
_Hh3cEviIfVlanMappingRowStatus_Type = RowStatus
_Hh3cEviIfVlanMappingRowStatus_Object = MibTableColumn
hh3cEviIfVlanMappingRowStatus = _Hh3cEviIfVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 2, 1, 4),
    _Hh3cEviIfVlanMappingRowStatus_Type()
)
hh3cEviIfVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEviIfVlanMappingRowStatus.setStatus("current")
_Hh3cEviIfAttributeTable_Object = MibTable
hh3cEviIfAttributeTable = _Hh3cEviIfAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cEviIfAttributeTable.setStatus("current")
_Hh3cEviIfAttributeEntry_Object = MibTableRow
hh3cEviIfAttributeEntry = _Hh3cEviIfAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 3, 1)
)
hh3cEviIfAttributeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEviIfAttributeEntry.setStatus("current")


class _Hh3cEviIfFloodingMode_Type(TruthValue):
    """Custom type hh3cEviIfFloodingMode based on TruthValue"""


_Hh3cEviIfFloodingMode_Object = MibTableColumn
hh3cEviIfFloodingMode = _Hh3cEviIfFloodingMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 3, 1, 1),
    _Hh3cEviIfFloodingMode_Type()
)
hh3cEviIfFloodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviIfFloodingMode.setStatus("current")


class _Hh3cEviIfARPSuppression_Type(TruthValue):
    """Custom type hh3cEviIfARPSuppression based on TruthValue"""


_Hh3cEviIfARPSuppression_Object = MibTableColumn
hh3cEviIfARPSuppression = _Hh3cEviIfARPSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 3, 1, 2),
    _Hh3cEviIfARPSuppression_Type()
)
hh3cEviIfARPSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviIfARPSuppression.setStatus("current")
_Hh3cEviIfFloodingMacTable_Object = MibTable
hh3cEviIfFloodingMacTable = _Hh3cEviIfFloodingMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cEviIfFloodingMacTable.setStatus("current")
_Hh3cEviIfFloodingMacEntry_Object = MibTableRow
hh3cEviIfFloodingMacEntry = _Hh3cEviIfFloodingMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 4, 1)
)
hh3cEviIfFloodingMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviIfFloodingMacAddress"),
    (0, "HH3C-EVI-MIB", "hh3cEviIfFloodMacVlanIndex"),
)
if mibBuilder.loadTexts:
    hh3cEviIfFloodingMacEntry.setStatus("current")
_Hh3cEviIfFloodingMacAddress_Type = MacAddress
_Hh3cEviIfFloodingMacAddress_Object = MibTableColumn
hh3cEviIfFloodingMacAddress = _Hh3cEviIfFloodingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 4, 1, 1),
    _Hh3cEviIfFloodingMacAddress_Type()
)
hh3cEviIfFloodingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviIfFloodingMacAddress.setStatus("current")
_Hh3cEviIfFloodMacVlanIndex_Type = VlanId
_Hh3cEviIfFloodMacVlanIndex_Object = MibTableColumn
hh3cEviIfFloodMacVlanIndex = _Hh3cEviIfFloodMacVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 4, 1, 2),
    _Hh3cEviIfFloodMacVlanIndex_Type()
)
hh3cEviIfFloodMacVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviIfFloodMacVlanIndex.setStatus("current")
_Hh3cEviIfFloodingMacRowStatus_Type = RowStatus
_Hh3cEviIfFloodingMacRowStatus_Object = MibTableColumn
hh3cEviIfFloodingMacRowStatus = _Hh3cEviIfFloodingMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 2, 4, 1, 3),
    _Hh3cEviIfFloodingMacRowStatus_Type()
)
hh3cEviIfFloodingMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEviIfFloodingMacRowStatus.setStatus("current")
_Hh3cEviMac_ObjectIdentity = ObjectIdentity
hh3cEviMac = _Hh3cEviMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3)
)
_Hh3cEviMacCountTable_Object = MibTable
hh3cEviMacCountTable = _Hh3cEviMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cEviMacCountTable.setStatus("current")
_Hh3cEviMacCountEntry_Object = MibTableRow
hh3cEviMacCountEntry = _Hh3cEviMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 1, 1)
)
hh3cEviMacCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEviMacCountEntry.setStatus("current")
_Hh3cEviMacLocalMacs_Type = Counter32
_Hh3cEviMacLocalMacs_Object = MibTableColumn
hh3cEviMacLocalMacs = _Hh3cEviMacLocalMacs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 1, 1, 1),
    _Hh3cEviMacLocalMacs_Type()
)
hh3cEviMacLocalMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacLocalMacs.setStatus("current")
_Hh3cEviMacLocalConflicts_Type = Counter32
_Hh3cEviMacLocalConflicts_Object = MibTableColumn
hh3cEviMacLocalConflicts = _Hh3cEviMacLocalConflicts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 1, 1, 2),
    _Hh3cEviMacLocalConflicts_Type()
)
hh3cEviMacLocalConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacLocalConflicts.setStatus("current")
_Hh3cEviMacRemoteMacs_Type = Counter32
_Hh3cEviMacRemoteMacs_Object = MibTableColumn
hh3cEviMacRemoteMacs = _Hh3cEviMacRemoteMacs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 1, 1, 3),
    _Hh3cEviMacRemoteMacs_Type()
)
hh3cEviMacRemoteMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacRemoteMacs.setStatus("current")
_Hh3cEviMacRemoteConflicts_Type = Counter32
_Hh3cEviMacRemoteConflicts_Object = MibTableColumn
hh3cEviMacRemoteConflicts = _Hh3cEviMacRemoteConflicts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 1, 1, 4),
    _Hh3cEviMacRemoteConflicts_Type()
)
hh3cEviMacRemoteConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacRemoteConflicts.setStatus("current")
_Hh3cEviMacLocalTable_Object = MibTable
hh3cEviMacLocalTable = _Hh3cEviMacLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cEviMacLocalTable.setStatus("current")
_Hh3cEviMacLocalEntry_Object = MibTableRow
hh3cEviMacLocalEntry = _Hh3cEviMacLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 2, 1)
)
hh3cEviMacLocalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviMacLocalVlan"),
    (0, "HH3C-EVI-MIB", "hh3cEviMacLocalMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cEviMacLocalEntry.setStatus("current")
_Hh3cEviMacLocalVlan_Type = VlanId
_Hh3cEviMacLocalVlan_Object = MibTableColumn
hh3cEviMacLocalVlan = _Hh3cEviMacLocalVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 2, 1, 1),
    _Hh3cEviMacLocalVlan_Type()
)
hh3cEviMacLocalVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviMacLocalVlan.setStatus("current")
_Hh3cEviMacLocalMacAddr_Type = MacAddress
_Hh3cEviMacLocalMacAddr_Object = MibTableColumn
hh3cEviMacLocalMacAddr = _Hh3cEviMacLocalMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 2, 1, 2),
    _Hh3cEviMacLocalMacAddr_Type()
)
hh3cEviMacLocalMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviMacLocalMacAddr.setStatus("current")
_Hh3cEviMacLocalMacType_Type = Hh3cEviMacType
_Hh3cEviMacLocalMacType_Object = MibTableColumn
hh3cEviMacLocalMacType = _Hh3cEviMacLocalMacType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 2, 1, 3),
    _Hh3cEviMacLocalMacType_Type()
)
hh3cEviMacLocalMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacLocalMacType.setStatus("current")
_Hh3cEviMacLocalConflict_Type = TruthValue
_Hh3cEviMacLocalConflict_Object = MibTableColumn
hh3cEviMacLocalConflict = _Hh3cEviMacLocalConflict_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 2, 1, 4),
    _Hh3cEviMacLocalConflict_Type()
)
hh3cEviMacLocalConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacLocalConflict.setStatus("current")
_Hh3cEviMacLocalFiltered_Type = TruthValue
_Hh3cEviMacLocalFiltered_Object = MibTableColumn
hh3cEviMacLocalFiltered = _Hh3cEviMacLocalFiltered_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 2, 1, 5),
    _Hh3cEviMacLocalFiltered_Type()
)
hh3cEviMacLocalFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacLocalFiltered.setStatus("current")
_Hh3cEviMacRemoteTable_Object = MibTable
hh3cEviMacRemoteTable = _Hh3cEviMacRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cEviMacRemoteTable.setStatus("current")
_Hh3cEviMacRemoteEntry_Object = MibTableRow
hh3cEviMacRemoteEntry = _Hh3cEviMacRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 3, 1)
)
hh3cEviMacRemoteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviMacRemoteVlan"),
    (0, "HH3C-EVI-MIB", "hh3cEviMacRemoteMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cEviMacRemoteEntry.setStatus("current")
_Hh3cEviMacRemoteVlan_Type = VlanId
_Hh3cEviMacRemoteVlan_Object = MibTableColumn
hh3cEviMacRemoteVlan = _Hh3cEviMacRemoteVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 3, 1, 1),
    _Hh3cEviMacRemoteVlan_Type()
)
hh3cEviMacRemoteVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviMacRemoteVlan.setStatus("current")
_Hh3cEviMacRemoteMacAddr_Type = MacAddress
_Hh3cEviMacRemoteMacAddr_Object = MibTableColumn
hh3cEviMacRemoteMacAddr = _Hh3cEviMacRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 3, 1, 2),
    _Hh3cEviMacRemoteMacAddr_Type()
)
hh3cEviMacRemoteMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviMacRemoteMacAddr.setStatus("current")
_Hh3cEviMacRemoteMacEffect_Type = TruthValue
_Hh3cEviMacRemoteMacEffect_Object = MibTableColumn
hh3cEviMacRemoteMacEffect = _Hh3cEviMacRemoteMacEffect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 3, 1, 3),
    _Hh3cEviMacRemoteMacEffect_Type()
)
hh3cEviMacRemoteMacEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacRemoteMacEffect.setStatus("current")
_Hh3cEviMacRemoteConflict_Type = TruthValue
_Hh3cEviMacRemoteConflict_Object = MibTableColumn
hh3cEviMacRemoteConflict = _Hh3cEviMacRemoteConflict_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 3, 3, 1, 4),
    _Hh3cEviMacRemoteConflict_Type()
)
hh3cEviMacRemoteConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviMacRemoteConflict.setStatus("current")
_Hh3cEviProcess_ObjectIdentity = ObjectIdentity
hh3cEviProcess = _Hh3cEviProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4)
)
_Hh3cEviProcessPolicyTable_Object = MibTable
hh3cEviProcessPolicyTable = _Hh3cEviProcessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cEviProcessPolicyTable.setStatus("current")
_Hh3cEviProcessPolicyEntry_Object = MibTableRow
hh3cEviProcessPolicyEntry = _Hh3cEviProcessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 1, 1)
)
hh3cEviProcessPolicyEntry.setIndexNames(
    (0, "HH3C-EVI-MIB", "hh3cEviProcessId"),
)
if mibBuilder.loadTexts:
    hh3cEviProcessPolicyEntry.setStatus("current")


class _Hh3cEviProcessId_Type(Unsigned32):
    """Custom type hh3cEviProcessId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_Hh3cEviProcessId_Type.__name__ = "Unsigned32"
_Hh3cEviProcessId_Object = MibTableColumn
hh3cEviProcessId = _Hh3cEviProcessId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 1, 1, 1),
    _Hh3cEviProcessId_Type()
)
hh3cEviProcessId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEviProcessId.setStatus("current")
_Hh3cEviProcessPolicy_Type = DisplayString
_Hh3cEviProcessPolicy_Object = MibTableColumn
hh3cEviProcessPolicy = _Hh3cEviProcessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 1, 1, 2),
    _Hh3cEviProcessPolicy_Type()
)
hh3cEviProcessPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviProcessPolicy.setStatus("current")
_Hh3cEviProcessGrTable_Object = MibTable
hh3cEviProcessGrTable = _Hh3cEviProcessGrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cEviProcessGrTable.setStatus("current")
_Hh3cEviProcessGrEntry_Object = MibTableRow
hh3cEviProcessGrEntry = _Hh3cEviProcessGrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 2, 1)
)
hh3cEviProcessGrEntry.setIndexNames(
    (0, "HH3C-EVI-MIB", "hh3cEviProcessId"),
)
if mibBuilder.loadTexts:
    hh3cEviProcessGrEntry.setStatus("current")


class _Hh3cEviProcessGrEnable_Type(TruthValue):
    """Custom type hh3cEviProcessGrEnable based on TruthValue"""


_Hh3cEviProcessGrEnable_Object = MibTableColumn
hh3cEviProcessGrEnable = _Hh3cEviProcessGrEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 2, 1, 1),
    _Hh3cEviProcessGrEnable_Type()
)
hh3cEviProcessGrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviProcessGrEnable.setStatus("current")


class _Hh3cEviProcessGrInterval_Type(Unsigned32):
    """Custom type hh3cEviProcessGrInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1800),
    )


_Hh3cEviProcessGrInterval_Type.__name__ = "Unsigned32"
_Hh3cEviProcessGrInterval_Object = MibTableColumn
hh3cEviProcessGrInterval = _Hh3cEviProcessGrInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 2, 1, 2),
    _Hh3cEviProcessGrInterval_Type()
)
hh3cEviProcessGrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviProcessGrInterval.setStatus("current")
_Hh3cEviProcessVSysTable_Object = MibTable
hh3cEviProcessVSysTable = _Hh3cEviProcessVSysTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cEviProcessVSysTable.setStatus("current")
_Hh3cEviProcessVSysEntry_Object = MibTableRow
hh3cEviProcessVSysEntry = _Hh3cEviProcessVSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 3, 1)
)
hh3cEviProcessVSysEntry.setIndexNames(
    (0, "HH3C-EVI-MIB", "hh3cEviProcessId"),
    (0, "HH3C-EVI-MIB", "hh3cEviVirtualSysId"),
)
if mibBuilder.loadTexts:
    hh3cEviProcessVSysEntry.setStatus("current")
_Hh3cEviVirtualSysId_Type = IsisSystemID
_Hh3cEviVirtualSysId_Object = MibTableColumn
hh3cEviVirtualSysId = _Hh3cEviVirtualSysId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 3, 1, 1),
    _Hh3cEviVirtualSysId_Type()
)
hh3cEviVirtualSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviVirtualSysId.setStatus("current")
_Hh3cEviVirtualSysRowStatus_Type = RowStatus
_Hh3cEviVirtualSysRowStatus_Object = MibTableColumn
hh3cEviVirtualSysRowStatus = _Hh3cEviVirtualSysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 4, 3, 1, 2),
    _Hh3cEviVirtualSysRowStatus_Type()
)
hh3cEviVirtualSysRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEviVirtualSysRowStatus.setStatus("current")
_Hh3cEviISIS_ObjectIdentity = ObjectIdentity
hh3cEviISIS = _Hh3cEviISIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5)
)
_Hh3cEviISISNbrSummaryTable_Object = MibTable
hh3cEviISISNbrSummaryTable = _Hh3cEviISISNbrSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cEviISISNbrSummaryTable.setStatus("current")
_Hh3cEviISISNbrSummaryEntry_Object = MibTableRow
hh3cEviISISNbrSummaryEntry = _Hh3cEviISISNbrSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 1, 1)
)
hh3cEviISISNbrSummaryEntry.setIndexNames(
    (0, "HH3C-EVI-MIB", "hh3cEviProcessId"),
)
if mibBuilder.loadTexts:
    hh3cEviISISNbrSummaryEntry.setStatus("current")
_Hh3cEviISISNbrMaxMultiHomes_Type = Unsigned32
_Hh3cEviISISNbrMaxMultiHomes_Object = MibTableColumn
hh3cEviISISNbrMaxMultiHomes = _Hh3cEviISISNbrMaxMultiHomes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 1, 1, 1),
    _Hh3cEviISISNbrMaxMultiHomes_Type()
)
hh3cEviISISNbrMaxMultiHomes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviISISNbrMaxMultiHomes.setStatus("current")
_Hh3cEviISISNbrSiteNbrs_Type = Unsigned32
_Hh3cEviISISNbrSiteNbrs_Object = MibTableColumn
hh3cEviISISNbrSiteNbrs = _Hh3cEviISISNbrSiteNbrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 1, 1, 2),
    _Hh3cEviISISNbrSiteNbrs_Type()
)
hh3cEviISISNbrSiteNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviISISNbrSiteNbrs.setStatus("current")
_Hh3cEviISISNbrLinkNbrs_Type = Unsigned32
_Hh3cEviISISNbrLinkNbrs_Object = MibTableColumn
hh3cEviISISNbrLinkNbrs = _Hh3cEviISISNbrLinkNbrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 1, 1, 3),
    _Hh3cEviISISNbrLinkNbrs_Type()
)
hh3cEviISISNbrLinkNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviISISNbrLinkNbrs.setStatus("current")
_Hh3cEviISISNbrTable_Object = MibTable
hh3cEviISISNbrTable = _Hh3cEviISISNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cEviISISNbrTable.setStatus("current")
_Hh3cEviISISNbrEntry_Object = MibTableRow
hh3cEviISISNbrEntry = _Hh3cEviISISNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 2, 1)
)
hh3cEviISISNbrEntry.setIndexNames(
    (0, "HH3C-EVI-MIB", "hh3cEviProcessId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviISISNbrSysId"),
)
if mibBuilder.loadTexts:
    hh3cEviISISNbrEntry.setStatus("current")
_Hh3cEviISISNbrSysId_Type = IsisSystemID
_Hh3cEviISISNbrSysId_Object = MibTableColumn
hh3cEviISISNbrSysId = _Hh3cEviISISNbrSysId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 2, 1, 1),
    _Hh3cEviISISNbrSysId_Type()
)
hh3cEviISISNbrSysId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEviISISNbrSysId.setStatus("current")
_Hh3cEviISISNbrMacAddr_Type = MacAddress
_Hh3cEviISISNbrMacAddr_Object = MibTableColumn
hh3cEviISISNbrMacAddr = _Hh3cEviISISNbrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 2, 1, 2),
    _Hh3cEviISISNbrMacAddr_Type()
)
hh3cEviISISNbrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviISISNbrMacAddr.setStatus("current")


class _Hh3cEviISISNbrSiteId_Type(Integer32):
    """Custom type hh3cEviISISNbrSiteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cEviISISNbrSiteId_Type.__name__ = "Integer32"
_Hh3cEviISISNbrSiteId_Object = MibTableColumn
hh3cEviISISNbrSiteId = _Hh3cEviISISNbrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 2, 1, 3),
    _Hh3cEviISISNbrSiteId_Type()
)
hh3cEviISISNbrSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviISISNbrSiteId.setStatus("current")
_Hh3cEviISISNbrTransStatus_Type = TruthValue
_Hh3cEviISISNbrTransStatus_Object = MibTableColumn
hh3cEviISISNbrTransStatus = _Hh3cEviISISNbrTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 5, 2, 1, 4),
    _Hh3cEviISISNbrTransStatus_Type()
)
hh3cEviISISNbrTransStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviISISNbrTransStatus.setStatus("current")
_Hh3cEviEnable_ObjectIdentity = ObjectIdentity
hh3cEviEnable = _Hh3cEviEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 6)
)
_Hh3cEviEnableTable_Object = MibTable
hh3cEviEnableTable = _Hh3cEviEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cEviEnableTable.setStatus("current")
_Hh3cEviEnableEntry_Object = MibTableRow
hh3cEviEnableEntry = _Hh3cEviEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 6, 1, 1)
)
hh3cEviEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEviEnableEntry.setStatus("current")


class _Hh3cEviEnableStatus_Type(TruthValue):
    """Custom type hh3cEviEnableStatus based on TruthValue"""


_Hh3cEviEnableStatus_Object = MibTableColumn
hh3cEviEnableStatus = _Hh3cEviEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 6, 1, 1, 1),
    _Hh3cEviEnableStatus_Type()
)
hh3cEviEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviEnableStatus.setStatus("current")
_Hh3cEviNbr_ObjectIdentity = ObjectIdentity
hh3cEviNbr = _Hh3cEviNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7)
)
_Hh3cEviNbrBaseTable_Object = MibTable
hh3cEviNbrBaseTable = _Hh3cEviNbrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cEviNbrBaseTable.setStatus("current")
_Hh3cEviNbrBaseEntry_Object = MibTableRow
hh3cEviNbrBaseEntry = _Hh3cEviNbrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 1, 1)
)
hh3cEviNbrBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEviNbrBaseEntry.setStatus("current")


class _Hh3cEviNbrSelfServerStatus_Type(TruthValue):
    """Custom type hh3cEviNbrSelfServerStatus based on TruthValue"""


_Hh3cEviNbrSelfServerStatus_Object = MibTableColumn
hh3cEviNbrSelfServerStatus = _Hh3cEviNbrSelfServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 1, 1, 1),
    _Hh3cEviNbrSelfServerStatus_Type()
)
hh3cEviNbrSelfServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviNbrSelfServerStatus.setStatus("current")


class _Hh3cEviNbrAuthPassword_Type(OctetString):
    """Custom type hh3cEviNbrAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Hh3cEviNbrAuthPassword_Type.__name__ = "OctetString"
_Hh3cEviNbrAuthPassword_Object = MibTableColumn
hh3cEviNbrAuthPassword = _Hh3cEviNbrAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 1, 1, 2),
    _Hh3cEviNbrAuthPassword_Type()
)
hh3cEviNbrAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviNbrAuthPassword.setStatus("current")


class _Hh3cEviNbrClientRegisterInterval_Type(Integer32):
    """Custom type hh3cEviNbrClientRegisterInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_Hh3cEviNbrClientRegisterInterval_Type.__name__ = "Integer32"
_Hh3cEviNbrClientRegisterInterval_Object = MibTableColumn
hh3cEviNbrClientRegisterInterval = _Hh3cEviNbrClientRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 1, 1, 3),
    _Hh3cEviNbrClientRegisterInterval_Type()
)
hh3cEviNbrClientRegisterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEviNbrClientRegisterInterval.setStatus("current")
_Hh3cEviNbrRemoteServerTable_Object = MibTable
hh3cEviNbrRemoteServerTable = _Hh3cEviNbrRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hh3cEviNbrRemoteServerTable.setStatus("current")
_Hh3cEviNbrRemoteServerEntry_Object = MibTableRow
hh3cEviNbrRemoteServerEntry = _Hh3cEviNbrRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 2, 1)
)
hh3cEviNbrRemoteServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviNbrRemoteServerType"),
    (0, "HH3C-EVI-MIB", "hh3cEviNbrRemoteServer"),
)
if mibBuilder.loadTexts:
    hh3cEviNbrRemoteServerEntry.setStatus("current")
_Hh3cEviNbrRemoteServerType_Type = InetAddressType
_Hh3cEviNbrRemoteServerType_Object = MibTableColumn
hh3cEviNbrRemoteServerType = _Hh3cEviNbrRemoteServerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 2, 1, 1),
    _Hh3cEviNbrRemoteServerType_Type()
)
hh3cEviNbrRemoteServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviNbrRemoteServerType.setStatus("current")
_Hh3cEviNbrRemoteServer_Type = InetAddress
_Hh3cEviNbrRemoteServer_Object = MibTableColumn
hh3cEviNbrRemoteServer = _Hh3cEviNbrRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 2, 1, 2),
    _Hh3cEviNbrRemoteServer_Type()
)
hh3cEviNbrRemoteServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviNbrRemoteServer.setStatus("current")
_Hh3cEviNbrRemoteServerRowStatus_Type = RowStatus
_Hh3cEviNbrRemoteServerRowStatus_Object = MibTableColumn
hh3cEviNbrRemoteServerRowStatus = _Hh3cEviNbrRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 2, 1, 3),
    _Hh3cEviNbrRemoteServerRowStatus_Type()
)
hh3cEviNbrRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEviNbrRemoteServerRowStatus.setStatus("current")
_Hh3cEviNbrTable_Object = MibTable
hh3cEviNbrTable = _Hh3cEviNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hh3cEviNbrTable.setStatus("current")
_Hh3cEviNbrEntry_Object = MibTableRow
hh3cEviNbrEntry = _Hh3cEviNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 3, 1)
)
hh3cEviNbrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVI-MIB", "hh3cEviNbrAddressType"),
    (0, "HH3C-EVI-MIB", "hh3cEviNbrAddress"),
)
if mibBuilder.loadTexts:
    hh3cEviNbrEntry.setStatus("current")
_Hh3cEviNbrAddressType_Type = InetAddressType
_Hh3cEviNbrAddressType_Object = MibTableColumn
hh3cEviNbrAddressType = _Hh3cEviNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 3, 1, 1),
    _Hh3cEviNbrAddressType_Type()
)
hh3cEviNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviNbrAddressType.setStatus("current")
_Hh3cEviNbrAddress_Type = InetAddress
_Hh3cEviNbrAddress_Object = MibTableColumn
hh3cEviNbrAddress = _Hh3cEviNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 3, 1, 2),
    _Hh3cEviNbrAddress_Type()
)
hh3cEviNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEviNbrAddress.setStatus("current")
_Hh3cEviNbrSystemID_Type = MacAddress
_Hh3cEviNbrSystemID_Object = MibTableColumn
hh3cEviNbrSystemID = _Hh3cEviNbrSystemID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 3, 1, 3),
    _Hh3cEviNbrSystemID_Type()
)
hh3cEviNbrSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviNbrSystemID.setStatus("current")
_Hh3cEviNbrExpireTime_Type = Integer32
_Hh3cEviNbrExpireTime_Object = MibTableColumn
hh3cEviNbrExpireTime = _Hh3cEviNbrExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 3, 1, 4),
    _Hh3cEviNbrExpireTime_Type()
)
hh3cEviNbrExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviNbrExpireTime.setStatus("current")
_Hh3cEviNbrStatus_Type = Hh3cEviNeighborStatus
_Hh3cEviNbrStatus_Object = MibTableColumn
hh3cEviNbrStatus = _Hh3cEviNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 1, 7, 3, 1, 5),
    _Hh3cEviNbrStatus_Type()
)
hh3cEviNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEviNbrStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cEviNewDed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 0, 1)
)
hh3cEviNewDed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-EVI-MIB", "hh3cEviProcessId"),
        ("HH3C-EVI-MIB", "hh3cEviISISNbrSysId"))
)
if mibBuilder.loadTexts:
    hh3cEviNewDed.setStatus(
        "current"
    )

hh3cEviSiteEDTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 0, 2)
)
hh3cEviSiteEDTopoChange.setObjects(
      *(("HH3C-EVI-MIB", "hh3cEviProcessId"),
        ("HH3C-EVI-MIB", "hh3cEviISISNbrSiteNbrs"))
)
if mibBuilder.loadTexts:
    hh3cEviSiteEDTopoChange.setStatus(
        "current"
    )

hh3cEviEDLinkDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132, 0, 3)
)
hh3cEviEDLinkDisconnect.setObjects(
    ("HH3C-EVI-MIB", "hh3cEviProcessId")
)
if mibBuilder.loadTexts:
    hh3cEviEDLinkDisconnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EVI-MIB",
    **{"Hh3cEviMacType": Hh3cEviMacType,
       "Hh3cEviNeighborStatus": Hh3cEviNeighborStatus,
       "hh3cEvi": hh3cEvi,
       "hh3cEviNotifications": hh3cEviNotifications,
       "hh3cEviNewDed": hh3cEviNewDed,
       "hh3cEviSiteEDTopoChange": hh3cEviSiteEDTopoChange,
       "hh3cEviEDLinkDisconnect": hh3cEviEDLinkDisconnect,
       "hh3cEviObjects": hh3cEviObjects,
       "hh3cEviBase": hh3cEviBase,
       "hh3cEviDesignatedVlan": hh3cEviDesignatedVlan,
       "hh3cEviSiteID": hh3cEviSiteID,
       "hh3cEviIf": hh3cEviIf,
       "hh3cEviIfExtendVlanTable": hh3cEviIfExtendVlanTable,
       "hh3cEviIfExtendVlanEntry": hh3cEviIfExtendVlanEntry,
       "hh3cEviIfExtendVlanIndex": hh3cEviIfExtendVlanIndex,
       "hh3cEviIfExtendVlanLAV": hh3cEviIfExtendVlanLAV,
       "hh3cEviIfExtendVlanRowStatus": hh3cEviIfExtendVlanRowStatus,
       "hh3cEviIfVlanMappingTable": hh3cEviIfVlanMappingTable,
       "hh3cEviIfVlanMappingEntry": hh3cEviIfVlanMappingEntry,
       "hh3cEviIfVlanMappingSiteId": hh3cEviIfVlanMappingSiteId,
       "hh3cEviIfVlanMappingSrc": hh3cEviIfVlanMappingSrc,
       "hh3cEviIfVlanMappingDst": hh3cEviIfVlanMappingDst,
       "hh3cEviIfVlanMappingRowStatus": hh3cEviIfVlanMappingRowStatus,
       "hh3cEviIfAttributeTable": hh3cEviIfAttributeTable,
       "hh3cEviIfAttributeEntry": hh3cEviIfAttributeEntry,
       "hh3cEviIfFloodingMode": hh3cEviIfFloodingMode,
       "hh3cEviIfARPSuppression": hh3cEviIfARPSuppression,
       "hh3cEviIfFloodingMacTable": hh3cEviIfFloodingMacTable,
       "hh3cEviIfFloodingMacEntry": hh3cEviIfFloodingMacEntry,
       "hh3cEviIfFloodingMacAddress": hh3cEviIfFloodingMacAddress,
       "hh3cEviIfFloodMacVlanIndex": hh3cEviIfFloodMacVlanIndex,
       "hh3cEviIfFloodingMacRowStatus": hh3cEviIfFloodingMacRowStatus,
       "hh3cEviMac": hh3cEviMac,
       "hh3cEviMacCountTable": hh3cEviMacCountTable,
       "hh3cEviMacCountEntry": hh3cEviMacCountEntry,
       "hh3cEviMacLocalMacs": hh3cEviMacLocalMacs,
       "hh3cEviMacLocalConflicts": hh3cEviMacLocalConflicts,
       "hh3cEviMacRemoteMacs": hh3cEviMacRemoteMacs,
       "hh3cEviMacRemoteConflicts": hh3cEviMacRemoteConflicts,
       "hh3cEviMacLocalTable": hh3cEviMacLocalTable,
       "hh3cEviMacLocalEntry": hh3cEviMacLocalEntry,
       "hh3cEviMacLocalVlan": hh3cEviMacLocalVlan,
       "hh3cEviMacLocalMacAddr": hh3cEviMacLocalMacAddr,
       "hh3cEviMacLocalMacType": hh3cEviMacLocalMacType,
       "hh3cEviMacLocalConflict": hh3cEviMacLocalConflict,
       "hh3cEviMacLocalFiltered": hh3cEviMacLocalFiltered,
       "hh3cEviMacRemoteTable": hh3cEviMacRemoteTable,
       "hh3cEviMacRemoteEntry": hh3cEviMacRemoteEntry,
       "hh3cEviMacRemoteVlan": hh3cEviMacRemoteVlan,
       "hh3cEviMacRemoteMacAddr": hh3cEviMacRemoteMacAddr,
       "hh3cEviMacRemoteMacEffect": hh3cEviMacRemoteMacEffect,
       "hh3cEviMacRemoteConflict": hh3cEviMacRemoteConflict,
       "hh3cEviProcess": hh3cEviProcess,
       "hh3cEviProcessPolicyTable": hh3cEviProcessPolicyTable,
       "hh3cEviProcessPolicyEntry": hh3cEviProcessPolicyEntry,
       "hh3cEviProcessId": hh3cEviProcessId,
       "hh3cEviProcessPolicy": hh3cEviProcessPolicy,
       "hh3cEviProcessGrTable": hh3cEviProcessGrTable,
       "hh3cEviProcessGrEntry": hh3cEviProcessGrEntry,
       "hh3cEviProcessGrEnable": hh3cEviProcessGrEnable,
       "hh3cEviProcessGrInterval": hh3cEviProcessGrInterval,
       "hh3cEviProcessVSysTable": hh3cEviProcessVSysTable,
       "hh3cEviProcessVSysEntry": hh3cEviProcessVSysEntry,
       "hh3cEviVirtualSysId": hh3cEviVirtualSysId,
       "hh3cEviVirtualSysRowStatus": hh3cEviVirtualSysRowStatus,
       "hh3cEviISIS": hh3cEviISIS,
       "hh3cEviISISNbrSummaryTable": hh3cEviISISNbrSummaryTable,
       "hh3cEviISISNbrSummaryEntry": hh3cEviISISNbrSummaryEntry,
       "hh3cEviISISNbrMaxMultiHomes": hh3cEviISISNbrMaxMultiHomes,
       "hh3cEviISISNbrSiteNbrs": hh3cEviISISNbrSiteNbrs,
       "hh3cEviISISNbrLinkNbrs": hh3cEviISISNbrLinkNbrs,
       "hh3cEviISISNbrTable": hh3cEviISISNbrTable,
       "hh3cEviISISNbrEntry": hh3cEviISISNbrEntry,
       "hh3cEviISISNbrSysId": hh3cEviISISNbrSysId,
       "hh3cEviISISNbrMacAddr": hh3cEviISISNbrMacAddr,
       "hh3cEviISISNbrSiteId": hh3cEviISISNbrSiteId,
       "hh3cEviISISNbrTransStatus": hh3cEviISISNbrTransStatus,
       "hh3cEviEnable": hh3cEviEnable,
       "hh3cEviEnableTable": hh3cEviEnableTable,
       "hh3cEviEnableEntry": hh3cEviEnableEntry,
       "hh3cEviEnableStatus": hh3cEviEnableStatus,
       "hh3cEviNbr": hh3cEviNbr,
       "hh3cEviNbrBaseTable": hh3cEviNbrBaseTable,
       "hh3cEviNbrBaseEntry": hh3cEviNbrBaseEntry,
       "hh3cEviNbrSelfServerStatus": hh3cEviNbrSelfServerStatus,
       "hh3cEviNbrAuthPassword": hh3cEviNbrAuthPassword,
       "hh3cEviNbrClientRegisterInterval": hh3cEviNbrClientRegisterInterval,
       "hh3cEviNbrRemoteServerTable": hh3cEviNbrRemoteServerTable,
       "hh3cEviNbrRemoteServerEntry": hh3cEviNbrRemoteServerEntry,
       "hh3cEviNbrRemoteServerType": hh3cEviNbrRemoteServerType,
       "hh3cEviNbrRemoteServer": hh3cEviNbrRemoteServer,
       "hh3cEviNbrRemoteServerRowStatus": hh3cEviNbrRemoteServerRowStatus,
       "hh3cEviNbrTable": hh3cEviNbrTable,
       "hh3cEviNbrEntry": hh3cEviNbrEntry,
       "hh3cEviNbrAddressType": hh3cEviNbrAddressType,
       "hh3cEviNbrAddress": hh3cEviNbrAddress,
       "hh3cEviNbrSystemID": hh3cEviNbrSystemID,
       "hh3cEviNbrExpireTime": hh3cEviNbrExpireTime,
       "hh3cEviNbrStatus": hh3cEviNbrStatus}
)
