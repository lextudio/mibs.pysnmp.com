# SNMP MIB module (HPN-ICF-EVI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-EVI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:14 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfEvi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132)
)
hpnicfEvi.setRevisions(
        ("2013-04-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfEviMacType(Integer32, TextualConvention):
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



class HpnicfEviNeighborStatus(Integer32, TextualConvention):
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

_HpnicfEviNotifications_ObjectIdentity = ObjectIdentity
hpnicfEviNotifications = _HpnicfEviNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0)
)
_HpnicfEviObjects_ObjectIdentity = ObjectIdentity
hpnicfEviObjects = _HpnicfEviObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1)
)
_HpnicfEviBase_ObjectIdentity = ObjectIdentity
hpnicfEviBase = _HpnicfEviBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 1)
)


class _HpnicfEviDesignatedVlan_Type(VlanId):
    """Custom type hpnicfEviDesignatedVlan based on VlanId"""
    defaultValue = 1


_HpnicfEviDesignatedVlan_Object = MibScalar
hpnicfEviDesignatedVlan = _HpnicfEviDesignatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 1, 1),
    _HpnicfEviDesignatedVlan_Type()
)
hpnicfEviDesignatedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviDesignatedVlan.setStatus("current")


class _HpnicfEviSiteID_Type(Integer32):
    """Custom type hpnicfEviSiteID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfEviSiteID_Type.__name__ = "Integer32"
_HpnicfEviSiteID_Object = MibScalar
hpnicfEviSiteID = _HpnicfEviSiteID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 1, 2),
    _HpnicfEviSiteID_Type()
)
hpnicfEviSiteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviSiteID.setStatus("current")
_HpnicfEviIf_ObjectIdentity = ObjectIdentity
hpnicfEviIf = _HpnicfEviIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2)
)
_HpnicfEviIfExtendVlanTable_Object = MibTable
hpnicfEviIfExtendVlanTable = _HpnicfEviIfExtendVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfEviIfExtendVlanTable.setStatus("current")
_HpnicfEviIfExtendVlanEntry_Object = MibTableRow
hpnicfEviIfExtendVlanEntry = _HpnicfEviIfExtendVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1)
)
hpnicfEviIfExtendVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfExtendVlanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEviIfExtendVlanEntry.setStatus("current")
_HpnicfEviIfExtendVlanIndex_Type = VlanId
_HpnicfEviIfExtendVlanIndex_Object = MibTableColumn
hpnicfEviIfExtendVlanIndex = _HpnicfEviIfExtendVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1, 1),
    _HpnicfEviIfExtendVlanIndex_Type()
)
hpnicfEviIfExtendVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviIfExtendVlanIndex.setStatus("current")


class _HpnicfEviIfExtendVlanLAV_Type(TruthValue):
    """Custom type hpnicfEviIfExtendVlanLAV based on TruthValue"""


_HpnicfEviIfExtendVlanLAV_Object = MibTableColumn
hpnicfEviIfExtendVlanLAV = _HpnicfEviIfExtendVlanLAV_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1, 2),
    _HpnicfEviIfExtendVlanLAV_Type()
)
hpnicfEviIfExtendVlanLAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviIfExtendVlanLAV.setStatus("current")
_HpnicfEviIfExtendVlanRowStatus_Type = RowStatus
_HpnicfEviIfExtendVlanRowStatus_Object = MibTableColumn
hpnicfEviIfExtendVlanRowStatus = _HpnicfEviIfExtendVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1, 3),
    _HpnicfEviIfExtendVlanRowStatus_Type()
)
hpnicfEviIfExtendVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEviIfExtendVlanRowStatus.setStatus("current")
_HpnicfEviIfVlanMappingTable_Object = MibTable
hpnicfEviIfVlanMappingTable = _HpnicfEviIfVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfEviIfVlanMappingTable.setStatus("current")
_HpnicfEviIfVlanMappingEntry_Object = MibTableRow
hpnicfEviIfVlanMappingEntry = _HpnicfEviIfVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1)
)
hpnicfEviIfVlanMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfVlanMappingSiteId"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfVlanMappingSrc"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfVlanMappingDst"),
)
if mibBuilder.loadTexts:
    hpnicfEviIfVlanMappingEntry.setStatus("current")


class _HpnicfEviIfVlanMappingSiteId_Type(Integer32):
    """Custom type hpnicfEviIfVlanMappingSiteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfEviIfVlanMappingSiteId_Type.__name__ = "Integer32"
_HpnicfEviIfVlanMappingSiteId_Object = MibTableColumn
hpnicfEviIfVlanMappingSiteId = _HpnicfEviIfVlanMappingSiteId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 1),
    _HpnicfEviIfVlanMappingSiteId_Type()
)
hpnicfEviIfVlanMappingSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviIfVlanMappingSiteId.setStatus("current")
_HpnicfEviIfVlanMappingSrc_Type = VlanId
_HpnicfEviIfVlanMappingSrc_Object = MibTableColumn
hpnicfEviIfVlanMappingSrc = _HpnicfEviIfVlanMappingSrc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 2),
    _HpnicfEviIfVlanMappingSrc_Type()
)
hpnicfEviIfVlanMappingSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviIfVlanMappingSrc.setStatus("current")
_HpnicfEviIfVlanMappingDst_Type = VlanId
_HpnicfEviIfVlanMappingDst_Object = MibTableColumn
hpnicfEviIfVlanMappingDst = _HpnicfEviIfVlanMappingDst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 3),
    _HpnicfEviIfVlanMappingDst_Type()
)
hpnicfEviIfVlanMappingDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviIfVlanMappingDst.setStatus("current")
_HpnicfEviIfVlanMappingRowStatus_Type = RowStatus
_HpnicfEviIfVlanMappingRowStatus_Object = MibTableColumn
hpnicfEviIfVlanMappingRowStatus = _HpnicfEviIfVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 4),
    _HpnicfEviIfVlanMappingRowStatus_Type()
)
hpnicfEviIfVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEviIfVlanMappingRowStatus.setStatus("current")
_HpnicfEviIfAttributeTable_Object = MibTable
hpnicfEviIfAttributeTable = _HpnicfEviIfAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfEviIfAttributeTable.setStatus("current")
_HpnicfEviIfAttributeEntry_Object = MibTableRow
hpnicfEviIfAttributeEntry = _HpnicfEviIfAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3, 1)
)
hpnicfEviIfAttributeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEviIfAttributeEntry.setStatus("current")


class _HpnicfEviIfFloodingMode_Type(TruthValue):
    """Custom type hpnicfEviIfFloodingMode based on TruthValue"""


_HpnicfEviIfFloodingMode_Object = MibTableColumn
hpnicfEviIfFloodingMode = _HpnicfEviIfFloodingMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3, 1, 1),
    _HpnicfEviIfFloodingMode_Type()
)
hpnicfEviIfFloodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviIfFloodingMode.setStatus("current")


class _HpnicfEviIfARPSuppression_Type(TruthValue):
    """Custom type hpnicfEviIfARPSuppression based on TruthValue"""


_HpnicfEviIfARPSuppression_Object = MibTableColumn
hpnicfEviIfARPSuppression = _HpnicfEviIfARPSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3, 1, 2),
    _HpnicfEviIfARPSuppression_Type()
)
hpnicfEviIfARPSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviIfARPSuppression.setStatus("current")
_HpnicfEviIfFloodingMacTable_Object = MibTable
hpnicfEviIfFloodingMacTable = _HpnicfEviIfFloodingMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfEviIfFloodingMacTable.setStatus("current")
_HpnicfEviIfFloodingMacEntry_Object = MibTableRow
hpnicfEviIfFloodingMacEntry = _HpnicfEviIfFloodingMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1)
)
hpnicfEviIfFloodingMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfFloodingMacAddress"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfFloodMacVlanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEviIfFloodingMacEntry.setStatus("current")
_HpnicfEviIfFloodingMacAddress_Type = MacAddress
_HpnicfEviIfFloodingMacAddress_Object = MibTableColumn
hpnicfEviIfFloodingMacAddress = _HpnicfEviIfFloodingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1, 1),
    _HpnicfEviIfFloodingMacAddress_Type()
)
hpnicfEviIfFloodingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviIfFloodingMacAddress.setStatus("current")
_HpnicfEviIfFloodMacVlanIndex_Type = VlanId
_HpnicfEviIfFloodMacVlanIndex_Object = MibTableColumn
hpnicfEviIfFloodMacVlanIndex = _HpnicfEviIfFloodMacVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1, 2),
    _HpnicfEviIfFloodMacVlanIndex_Type()
)
hpnicfEviIfFloodMacVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviIfFloodMacVlanIndex.setStatus("current")
_HpnicfEviIfFloodingMacRowStatus_Type = RowStatus
_HpnicfEviIfFloodingMacRowStatus_Object = MibTableColumn
hpnicfEviIfFloodingMacRowStatus = _HpnicfEviIfFloodingMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1, 3),
    _HpnicfEviIfFloodingMacRowStatus_Type()
)
hpnicfEviIfFloodingMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEviIfFloodingMacRowStatus.setStatus("current")
_HpnicfEviMac_ObjectIdentity = ObjectIdentity
hpnicfEviMac = _HpnicfEviMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3)
)
_HpnicfEviMacCountTable_Object = MibTable
hpnicfEviMacCountTable = _HpnicfEviMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfEviMacCountTable.setStatus("current")
_HpnicfEviMacCountEntry_Object = MibTableRow
hpnicfEviMacCountEntry = _HpnicfEviMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1)
)
hpnicfEviMacCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEviMacCountEntry.setStatus("current")
_HpnicfEviMacLocalMacs_Type = Counter32
_HpnicfEviMacLocalMacs_Object = MibTableColumn
hpnicfEviMacLocalMacs = _HpnicfEviMacLocalMacs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 1),
    _HpnicfEviMacLocalMacs_Type()
)
hpnicfEviMacLocalMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacLocalMacs.setStatus("current")
_HpnicfEviMacLocalConflicts_Type = Counter32
_HpnicfEviMacLocalConflicts_Object = MibTableColumn
hpnicfEviMacLocalConflicts = _HpnicfEviMacLocalConflicts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 2),
    _HpnicfEviMacLocalConflicts_Type()
)
hpnicfEviMacLocalConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacLocalConflicts.setStatus("current")
_HpnicfEviMacRemoteMacs_Type = Counter32
_HpnicfEviMacRemoteMacs_Object = MibTableColumn
hpnicfEviMacRemoteMacs = _HpnicfEviMacRemoteMacs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 3),
    _HpnicfEviMacRemoteMacs_Type()
)
hpnicfEviMacRemoteMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteMacs.setStatus("current")
_HpnicfEviMacRemoteConflicts_Type = Counter32
_HpnicfEviMacRemoteConflicts_Object = MibTableColumn
hpnicfEviMacRemoteConflicts = _HpnicfEviMacRemoteConflicts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 4),
    _HpnicfEviMacRemoteConflicts_Type()
)
hpnicfEviMacRemoteConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteConflicts.setStatus("current")
_HpnicfEviMacLocalTable_Object = MibTable
hpnicfEviMacLocalTable = _HpnicfEviMacLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfEviMacLocalTable.setStatus("current")
_HpnicfEviMacLocalEntry_Object = MibTableRow
hpnicfEviMacLocalEntry = _HpnicfEviMacLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1)
)
hpnicfEviMacLocalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacLocalVlan"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacLocalMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfEviMacLocalEntry.setStatus("current")
_HpnicfEviMacLocalVlan_Type = VlanId
_HpnicfEviMacLocalVlan_Object = MibTableColumn
hpnicfEviMacLocalVlan = _HpnicfEviMacLocalVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 1),
    _HpnicfEviMacLocalVlan_Type()
)
hpnicfEviMacLocalVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviMacLocalVlan.setStatus("current")
_HpnicfEviMacLocalMacAddr_Type = MacAddress
_HpnicfEviMacLocalMacAddr_Object = MibTableColumn
hpnicfEviMacLocalMacAddr = _HpnicfEviMacLocalMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 2),
    _HpnicfEviMacLocalMacAddr_Type()
)
hpnicfEviMacLocalMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviMacLocalMacAddr.setStatus("current")
_HpnicfEviMacLocalMacType_Type = HpnicfEviMacType
_HpnicfEviMacLocalMacType_Object = MibTableColumn
hpnicfEviMacLocalMacType = _HpnicfEviMacLocalMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 3),
    _HpnicfEviMacLocalMacType_Type()
)
hpnicfEviMacLocalMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacLocalMacType.setStatus("current")
_HpnicfEviMacLocalConflict_Type = TruthValue
_HpnicfEviMacLocalConflict_Object = MibTableColumn
hpnicfEviMacLocalConflict = _HpnicfEviMacLocalConflict_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 4),
    _HpnicfEviMacLocalConflict_Type()
)
hpnicfEviMacLocalConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacLocalConflict.setStatus("current")
_HpnicfEviMacLocalFiltered_Type = TruthValue
_HpnicfEviMacLocalFiltered_Object = MibTableColumn
hpnicfEviMacLocalFiltered = _HpnicfEviMacLocalFiltered_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 5),
    _HpnicfEviMacLocalFiltered_Type()
)
hpnicfEviMacLocalFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacLocalFiltered.setStatus("current")
_HpnicfEviMacRemoteTable_Object = MibTable
hpnicfEviMacRemoteTable = _HpnicfEviMacRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteTable.setStatus("current")
_HpnicfEviMacRemoteEntry_Object = MibTableRow
hpnicfEviMacRemoteEntry = _HpnicfEviMacRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1)
)
hpnicfEviMacRemoteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacRemoteVlan"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacRemoteMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteEntry.setStatus("current")
_HpnicfEviMacRemoteVlan_Type = VlanId
_HpnicfEviMacRemoteVlan_Object = MibTableColumn
hpnicfEviMacRemoteVlan = _HpnicfEviMacRemoteVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 1),
    _HpnicfEviMacRemoteVlan_Type()
)
hpnicfEviMacRemoteVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteVlan.setStatus("current")
_HpnicfEviMacRemoteMacAddr_Type = MacAddress
_HpnicfEviMacRemoteMacAddr_Object = MibTableColumn
hpnicfEviMacRemoteMacAddr = _HpnicfEviMacRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 2),
    _HpnicfEviMacRemoteMacAddr_Type()
)
hpnicfEviMacRemoteMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteMacAddr.setStatus("current")
_HpnicfEviMacRemoteMacEffect_Type = TruthValue
_HpnicfEviMacRemoteMacEffect_Object = MibTableColumn
hpnicfEviMacRemoteMacEffect = _HpnicfEviMacRemoteMacEffect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 3),
    _HpnicfEviMacRemoteMacEffect_Type()
)
hpnicfEviMacRemoteMacEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteMacEffect.setStatus("current")
_HpnicfEviMacRemoteConflict_Type = TruthValue
_HpnicfEviMacRemoteConflict_Object = MibTableColumn
hpnicfEviMacRemoteConflict = _HpnicfEviMacRemoteConflict_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 4),
    _HpnicfEviMacRemoteConflict_Type()
)
hpnicfEviMacRemoteConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviMacRemoteConflict.setStatus("current")
_HpnicfEviProcess_ObjectIdentity = ObjectIdentity
hpnicfEviProcess = _HpnicfEviProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4)
)
_HpnicfEviProcessPolicyTable_Object = MibTable
hpnicfEviProcessPolicyTable = _HpnicfEviProcessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfEviProcessPolicyTable.setStatus("current")
_HpnicfEviProcessPolicyEntry_Object = MibTableRow
hpnicfEviProcessPolicyEntry = _HpnicfEviProcessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1, 1)
)
hpnicfEviProcessPolicyEntry.setIndexNames(
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"),
)
if mibBuilder.loadTexts:
    hpnicfEviProcessPolicyEntry.setStatus("current")


class _HpnicfEviProcessId_Type(Unsigned32):
    """Custom type hpnicfEviProcessId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HpnicfEviProcessId_Type.__name__ = "Unsigned32"
_HpnicfEviProcessId_Object = MibTableColumn
hpnicfEviProcessId = _HpnicfEviProcessId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1, 1, 1),
    _HpnicfEviProcessId_Type()
)
hpnicfEviProcessId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEviProcessId.setStatus("current")
_HpnicfEviProcessPolicy_Type = DisplayString
_HpnicfEviProcessPolicy_Object = MibTableColumn
hpnicfEviProcessPolicy = _HpnicfEviProcessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1, 1, 2),
    _HpnicfEviProcessPolicy_Type()
)
hpnicfEviProcessPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviProcessPolicy.setStatus("current")
_HpnicfEviProcessGrTable_Object = MibTable
hpnicfEviProcessGrTable = _HpnicfEviProcessGrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfEviProcessGrTable.setStatus("current")
_HpnicfEviProcessGrEntry_Object = MibTableRow
hpnicfEviProcessGrEntry = _HpnicfEviProcessGrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2, 1)
)
hpnicfEviProcessGrEntry.setIndexNames(
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"),
)
if mibBuilder.loadTexts:
    hpnicfEviProcessGrEntry.setStatus("current")


class _HpnicfEviProcessGrEnable_Type(TruthValue):
    """Custom type hpnicfEviProcessGrEnable based on TruthValue"""


_HpnicfEviProcessGrEnable_Object = MibTableColumn
hpnicfEviProcessGrEnable = _HpnicfEviProcessGrEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2, 1, 1),
    _HpnicfEviProcessGrEnable_Type()
)
hpnicfEviProcessGrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviProcessGrEnable.setStatus("current")


class _HpnicfEviProcessGrInterval_Type(Unsigned32):
    """Custom type hpnicfEviProcessGrInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1800),
    )


_HpnicfEviProcessGrInterval_Type.__name__ = "Unsigned32"
_HpnicfEviProcessGrInterval_Object = MibTableColumn
hpnicfEviProcessGrInterval = _HpnicfEviProcessGrInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2, 1, 2),
    _HpnicfEviProcessGrInterval_Type()
)
hpnicfEviProcessGrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviProcessGrInterval.setStatus("current")
_HpnicfEviProcessVSysTable_Object = MibTable
hpnicfEviProcessVSysTable = _HpnicfEviProcessVSysTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hpnicfEviProcessVSysTable.setStatus("current")
_HpnicfEviProcessVSysEntry_Object = MibTableRow
hpnicfEviProcessVSysEntry = _HpnicfEviProcessVSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3, 1)
)
hpnicfEviProcessVSysEntry.setIndexNames(
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviVirtualSysId"),
)
if mibBuilder.loadTexts:
    hpnicfEviProcessVSysEntry.setStatus("current")
_HpnicfEviVirtualSysId_Type = IsisSystemID
_HpnicfEviVirtualSysId_Object = MibTableColumn
hpnicfEviVirtualSysId = _HpnicfEviVirtualSysId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3, 1, 1),
    _HpnicfEviVirtualSysId_Type()
)
hpnicfEviVirtualSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviVirtualSysId.setStatus("current")
_HpnicfEviVirtualSysRowStatus_Type = RowStatus
_HpnicfEviVirtualSysRowStatus_Object = MibTableColumn
hpnicfEviVirtualSysRowStatus = _HpnicfEviVirtualSysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3, 1, 2),
    _HpnicfEviVirtualSysRowStatus_Type()
)
hpnicfEviVirtualSysRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEviVirtualSysRowStatus.setStatus("current")
_HpnicfEviISIS_ObjectIdentity = ObjectIdentity
hpnicfEviISIS = _HpnicfEviISIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5)
)
_HpnicfEviISISNbrSummaryTable_Object = MibTable
hpnicfEviISISNbrSummaryTable = _HpnicfEviISISNbrSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfEviISISNbrSummaryTable.setStatus("current")
_HpnicfEviISISNbrSummaryEntry_Object = MibTableRow
hpnicfEviISISNbrSummaryEntry = _HpnicfEviISISNbrSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1)
)
hpnicfEviISISNbrSummaryEntry.setIndexNames(
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"),
)
if mibBuilder.loadTexts:
    hpnicfEviISISNbrSummaryEntry.setStatus("current")
_HpnicfEviISISNbrMaxMultiHomes_Type = Unsigned32
_HpnicfEviISISNbrMaxMultiHomes_Object = MibTableColumn
hpnicfEviISISNbrMaxMultiHomes = _HpnicfEviISISNbrMaxMultiHomes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1, 1),
    _HpnicfEviISISNbrMaxMultiHomes_Type()
)
hpnicfEviISISNbrMaxMultiHomes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviISISNbrMaxMultiHomes.setStatus("current")
_HpnicfEviISISNbrSiteNbrs_Type = Unsigned32
_HpnicfEviISISNbrSiteNbrs_Object = MibTableColumn
hpnicfEviISISNbrSiteNbrs = _HpnicfEviISISNbrSiteNbrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1, 2),
    _HpnicfEviISISNbrSiteNbrs_Type()
)
hpnicfEviISISNbrSiteNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviISISNbrSiteNbrs.setStatus("current")
_HpnicfEviISISNbrLinkNbrs_Type = Unsigned32
_HpnicfEviISISNbrLinkNbrs_Object = MibTableColumn
hpnicfEviISISNbrLinkNbrs = _HpnicfEviISISNbrLinkNbrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1, 3),
    _HpnicfEviISISNbrLinkNbrs_Type()
)
hpnicfEviISISNbrLinkNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviISISNbrLinkNbrs.setStatus("current")
_HpnicfEviISISNbrTable_Object = MibTable
hpnicfEviISISNbrTable = _HpnicfEviISISNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfEviISISNbrTable.setStatus("current")
_HpnicfEviISISNbrEntry_Object = MibTableRow
hpnicfEviISISNbrEntry = _HpnicfEviISISNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1)
)
hpnicfEviISISNbrEntry.setIndexNames(
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviISISNbrSysId"),
)
if mibBuilder.loadTexts:
    hpnicfEviISISNbrEntry.setStatus("current")
_HpnicfEviISISNbrSysId_Type = IsisSystemID
_HpnicfEviISISNbrSysId_Object = MibTableColumn
hpnicfEviISISNbrSysId = _HpnicfEviISISNbrSysId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 1),
    _HpnicfEviISISNbrSysId_Type()
)
hpnicfEviISISNbrSysId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEviISISNbrSysId.setStatus("current")
_HpnicfEviISISNbrMacAddr_Type = MacAddress
_HpnicfEviISISNbrMacAddr_Object = MibTableColumn
hpnicfEviISISNbrMacAddr = _HpnicfEviISISNbrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 2),
    _HpnicfEviISISNbrMacAddr_Type()
)
hpnicfEviISISNbrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviISISNbrMacAddr.setStatus("current")


class _HpnicfEviISISNbrSiteId_Type(Integer32):
    """Custom type hpnicfEviISISNbrSiteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfEviISISNbrSiteId_Type.__name__ = "Integer32"
_HpnicfEviISISNbrSiteId_Object = MibTableColumn
hpnicfEviISISNbrSiteId = _HpnicfEviISISNbrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 3),
    _HpnicfEviISISNbrSiteId_Type()
)
hpnicfEviISISNbrSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviISISNbrSiteId.setStatus("current")
_HpnicfEviISISNbrTransStatus_Type = TruthValue
_HpnicfEviISISNbrTransStatus_Object = MibTableColumn
hpnicfEviISISNbrTransStatus = _HpnicfEviISISNbrTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 4),
    _HpnicfEviISISNbrTransStatus_Type()
)
hpnicfEviISISNbrTransStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviISISNbrTransStatus.setStatus("current")
_HpnicfEviEnable_ObjectIdentity = ObjectIdentity
hpnicfEviEnable = _HpnicfEviEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6)
)
_HpnicfEviEnableTable_Object = MibTable
hpnicfEviEnableTable = _HpnicfEviEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfEviEnableTable.setStatus("current")
_HpnicfEviEnableEntry_Object = MibTableRow
hpnicfEviEnableEntry = _HpnicfEviEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6, 1, 1)
)
hpnicfEviEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEviEnableEntry.setStatus("current")


class _HpnicfEviEnableStatus_Type(TruthValue):
    """Custom type hpnicfEviEnableStatus based on TruthValue"""


_HpnicfEviEnableStatus_Object = MibTableColumn
hpnicfEviEnableStatus = _HpnicfEviEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6, 1, 1, 1),
    _HpnicfEviEnableStatus_Type()
)
hpnicfEviEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviEnableStatus.setStatus("current")
_HpnicfEviNbr_ObjectIdentity = ObjectIdentity
hpnicfEviNbr = _HpnicfEviNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7)
)
_HpnicfEviNbrBaseTable_Object = MibTable
hpnicfEviNbrBaseTable = _HpnicfEviNbrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpnicfEviNbrBaseTable.setStatus("current")
_HpnicfEviNbrBaseEntry_Object = MibTableRow
hpnicfEviNbrBaseEntry = _HpnicfEviNbrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1)
)
hpnicfEviNbrBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEviNbrBaseEntry.setStatus("current")


class _HpnicfEviNbrSelfServerStatus_Type(TruthValue):
    """Custom type hpnicfEviNbrSelfServerStatus based on TruthValue"""


_HpnicfEviNbrSelfServerStatus_Object = MibTableColumn
hpnicfEviNbrSelfServerStatus = _HpnicfEviNbrSelfServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1, 1),
    _HpnicfEviNbrSelfServerStatus_Type()
)
hpnicfEviNbrSelfServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviNbrSelfServerStatus.setStatus("current")


class _HpnicfEviNbrAuthPassword_Type(OctetString):
    """Custom type hpnicfEviNbrAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HpnicfEviNbrAuthPassword_Type.__name__ = "OctetString"
_HpnicfEviNbrAuthPassword_Object = MibTableColumn
hpnicfEviNbrAuthPassword = _HpnicfEviNbrAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1, 2),
    _HpnicfEviNbrAuthPassword_Type()
)
hpnicfEviNbrAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviNbrAuthPassword.setStatus("current")


class _HpnicfEviNbrClientRegisterInterval_Type(Integer32):
    """Custom type hpnicfEviNbrClientRegisterInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_HpnicfEviNbrClientRegisterInterval_Type.__name__ = "Integer32"
_HpnicfEviNbrClientRegisterInterval_Object = MibTableColumn
hpnicfEviNbrClientRegisterInterval = _HpnicfEviNbrClientRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1, 3),
    _HpnicfEviNbrClientRegisterInterval_Type()
)
hpnicfEviNbrClientRegisterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEviNbrClientRegisterInterval.setStatus("current")
_HpnicfEviNbrRemoteServerTable_Object = MibTable
hpnicfEviNbrRemoteServerTable = _HpnicfEviNbrRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hpnicfEviNbrRemoteServerTable.setStatus("current")
_HpnicfEviNbrRemoteServerEntry_Object = MibTableRow
hpnicfEviNbrRemoteServerEntry = _HpnicfEviNbrRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1)
)
hpnicfEviNbrRemoteServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrRemoteServerType"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrRemoteServer"),
)
if mibBuilder.loadTexts:
    hpnicfEviNbrRemoteServerEntry.setStatus("current")
_HpnicfEviNbrRemoteServerType_Type = InetAddressType
_HpnicfEviNbrRemoteServerType_Object = MibTableColumn
hpnicfEviNbrRemoteServerType = _HpnicfEviNbrRemoteServerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1, 1),
    _HpnicfEviNbrRemoteServerType_Type()
)
hpnicfEviNbrRemoteServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviNbrRemoteServerType.setStatus("current")
_HpnicfEviNbrRemoteServer_Type = InetAddress
_HpnicfEviNbrRemoteServer_Object = MibTableColumn
hpnicfEviNbrRemoteServer = _HpnicfEviNbrRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1, 2),
    _HpnicfEviNbrRemoteServer_Type()
)
hpnicfEviNbrRemoteServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviNbrRemoteServer.setStatus("current")
_HpnicfEviNbrRemoteServerRowStatus_Type = RowStatus
_HpnicfEviNbrRemoteServerRowStatus_Object = MibTableColumn
hpnicfEviNbrRemoteServerRowStatus = _HpnicfEviNbrRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1, 3),
    _HpnicfEviNbrRemoteServerRowStatus_Type()
)
hpnicfEviNbrRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEviNbrRemoteServerRowStatus.setStatus("current")
_HpnicfEviNbrTable_Object = MibTable
hpnicfEviNbrTable = _HpnicfEviNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hpnicfEviNbrTable.setStatus("current")
_HpnicfEviNbrEntry_Object = MibTableRow
hpnicfEviNbrEntry = _HpnicfEviNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1)
)
hpnicfEviNbrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrAddressType"),
    (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrAddress"),
)
if mibBuilder.loadTexts:
    hpnicfEviNbrEntry.setStatus("current")
_HpnicfEviNbrAddressType_Type = InetAddressType
_HpnicfEviNbrAddressType_Object = MibTableColumn
hpnicfEviNbrAddressType = _HpnicfEviNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 1),
    _HpnicfEviNbrAddressType_Type()
)
hpnicfEviNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviNbrAddressType.setStatus("current")
_HpnicfEviNbrAddress_Type = InetAddress
_HpnicfEviNbrAddress_Object = MibTableColumn
hpnicfEviNbrAddress = _HpnicfEviNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 2),
    _HpnicfEviNbrAddress_Type()
)
hpnicfEviNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEviNbrAddress.setStatus("current")
_HpnicfEviNbrSystemID_Type = MacAddress
_HpnicfEviNbrSystemID_Object = MibTableColumn
hpnicfEviNbrSystemID = _HpnicfEviNbrSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 3),
    _HpnicfEviNbrSystemID_Type()
)
hpnicfEviNbrSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviNbrSystemID.setStatus("current")
_HpnicfEviNbrExpireTime_Type = Integer32
_HpnicfEviNbrExpireTime_Object = MibTableColumn
hpnicfEviNbrExpireTime = _HpnicfEviNbrExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 4),
    _HpnicfEviNbrExpireTime_Type()
)
hpnicfEviNbrExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviNbrExpireTime.setStatus("current")
_HpnicfEviNbrStatus_Type = HpnicfEviNeighborStatus
_HpnicfEviNbrStatus_Object = MibTableColumn
hpnicfEviNbrStatus = _HpnicfEviNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 5),
    _HpnicfEviNbrStatus_Type()
)
hpnicfEviNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEviNbrStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfEviNewDed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0, 1)
)
hpnicfEviNewDed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-EVI-MIB", "hpnicfEviProcessId"),
        ("HPN-ICF-EVI-MIB", "hpnicfEviISISNbrSysId"))
)
if mibBuilder.loadTexts:
    hpnicfEviNewDed.setStatus(
        "current"
    )

hpnicfEviSiteEDTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0, 2)
)
hpnicfEviSiteEDTopoChange.setObjects(
      *(("HPN-ICF-EVI-MIB", "hpnicfEviProcessId"),
        ("HPN-ICF-EVI-MIB", "hpnicfEviISISNbrSiteNbrs"))
)
if mibBuilder.loadTexts:
    hpnicfEviSiteEDTopoChange.setStatus(
        "current"
    )

hpnicfEviEDLinkDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0, 3)
)
hpnicfEviEDLinkDisconnect.setObjects(
    ("HPN-ICF-EVI-MIB", "hpnicfEviProcessId")
)
if mibBuilder.loadTexts:
    hpnicfEviEDLinkDisconnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EVI-MIB",
    **{"HpnicfEviMacType": HpnicfEviMacType,
       "HpnicfEviNeighborStatus": HpnicfEviNeighborStatus,
       "hpnicfEvi": hpnicfEvi,
       "hpnicfEviNotifications": hpnicfEviNotifications,
       "hpnicfEviNewDed": hpnicfEviNewDed,
       "hpnicfEviSiteEDTopoChange": hpnicfEviSiteEDTopoChange,
       "hpnicfEviEDLinkDisconnect": hpnicfEviEDLinkDisconnect,
       "hpnicfEviObjects": hpnicfEviObjects,
       "hpnicfEviBase": hpnicfEviBase,
       "hpnicfEviDesignatedVlan": hpnicfEviDesignatedVlan,
       "hpnicfEviSiteID": hpnicfEviSiteID,
       "hpnicfEviIf": hpnicfEviIf,
       "hpnicfEviIfExtendVlanTable": hpnicfEviIfExtendVlanTable,
       "hpnicfEviIfExtendVlanEntry": hpnicfEviIfExtendVlanEntry,
       "hpnicfEviIfExtendVlanIndex": hpnicfEviIfExtendVlanIndex,
       "hpnicfEviIfExtendVlanLAV": hpnicfEviIfExtendVlanLAV,
       "hpnicfEviIfExtendVlanRowStatus": hpnicfEviIfExtendVlanRowStatus,
       "hpnicfEviIfVlanMappingTable": hpnicfEviIfVlanMappingTable,
       "hpnicfEviIfVlanMappingEntry": hpnicfEviIfVlanMappingEntry,
       "hpnicfEviIfVlanMappingSiteId": hpnicfEviIfVlanMappingSiteId,
       "hpnicfEviIfVlanMappingSrc": hpnicfEviIfVlanMappingSrc,
       "hpnicfEviIfVlanMappingDst": hpnicfEviIfVlanMappingDst,
       "hpnicfEviIfVlanMappingRowStatus": hpnicfEviIfVlanMappingRowStatus,
       "hpnicfEviIfAttributeTable": hpnicfEviIfAttributeTable,
       "hpnicfEviIfAttributeEntry": hpnicfEviIfAttributeEntry,
       "hpnicfEviIfFloodingMode": hpnicfEviIfFloodingMode,
       "hpnicfEviIfARPSuppression": hpnicfEviIfARPSuppression,
       "hpnicfEviIfFloodingMacTable": hpnicfEviIfFloodingMacTable,
       "hpnicfEviIfFloodingMacEntry": hpnicfEviIfFloodingMacEntry,
       "hpnicfEviIfFloodingMacAddress": hpnicfEviIfFloodingMacAddress,
       "hpnicfEviIfFloodMacVlanIndex": hpnicfEviIfFloodMacVlanIndex,
       "hpnicfEviIfFloodingMacRowStatus": hpnicfEviIfFloodingMacRowStatus,
       "hpnicfEviMac": hpnicfEviMac,
       "hpnicfEviMacCountTable": hpnicfEviMacCountTable,
       "hpnicfEviMacCountEntry": hpnicfEviMacCountEntry,
       "hpnicfEviMacLocalMacs": hpnicfEviMacLocalMacs,
       "hpnicfEviMacLocalConflicts": hpnicfEviMacLocalConflicts,
       "hpnicfEviMacRemoteMacs": hpnicfEviMacRemoteMacs,
       "hpnicfEviMacRemoteConflicts": hpnicfEviMacRemoteConflicts,
       "hpnicfEviMacLocalTable": hpnicfEviMacLocalTable,
       "hpnicfEviMacLocalEntry": hpnicfEviMacLocalEntry,
       "hpnicfEviMacLocalVlan": hpnicfEviMacLocalVlan,
       "hpnicfEviMacLocalMacAddr": hpnicfEviMacLocalMacAddr,
       "hpnicfEviMacLocalMacType": hpnicfEviMacLocalMacType,
       "hpnicfEviMacLocalConflict": hpnicfEviMacLocalConflict,
       "hpnicfEviMacLocalFiltered": hpnicfEviMacLocalFiltered,
       "hpnicfEviMacRemoteTable": hpnicfEviMacRemoteTable,
       "hpnicfEviMacRemoteEntry": hpnicfEviMacRemoteEntry,
       "hpnicfEviMacRemoteVlan": hpnicfEviMacRemoteVlan,
       "hpnicfEviMacRemoteMacAddr": hpnicfEviMacRemoteMacAddr,
       "hpnicfEviMacRemoteMacEffect": hpnicfEviMacRemoteMacEffect,
       "hpnicfEviMacRemoteConflict": hpnicfEviMacRemoteConflict,
       "hpnicfEviProcess": hpnicfEviProcess,
       "hpnicfEviProcessPolicyTable": hpnicfEviProcessPolicyTable,
       "hpnicfEviProcessPolicyEntry": hpnicfEviProcessPolicyEntry,
       "hpnicfEviProcessId": hpnicfEviProcessId,
       "hpnicfEviProcessPolicy": hpnicfEviProcessPolicy,
       "hpnicfEviProcessGrTable": hpnicfEviProcessGrTable,
       "hpnicfEviProcessGrEntry": hpnicfEviProcessGrEntry,
       "hpnicfEviProcessGrEnable": hpnicfEviProcessGrEnable,
       "hpnicfEviProcessGrInterval": hpnicfEviProcessGrInterval,
       "hpnicfEviProcessVSysTable": hpnicfEviProcessVSysTable,
       "hpnicfEviProcessVSysEntry": hpnicfEviProcessVSysEntry,
       "hpnicfEviVirtualSysId": hpnicfEviVirtualSysId,
       "hpnicfEviVirtualSysRowStatus": hpnicfEviVirtualSysRowStatus,
       "hpnicfEviISIS": hpnicfEviISIS,
       "hpnicfEviISISNbrSummaryTable": hpnicfEviISISNbrSummaryTable,
       "hpnicfEviISISNbrSummaryEntry": hpnicfEviISISNbrSummaryEntry,
       "hpnicfEviISISNbrMaxMultiHomes": hpnicfEviISISNbrMaxMultiHomes,
       "hpnicfEviISISNbrSiteNbrs": hpnicfEviISISNbrSiteNbrs,
       "hpnicfEviISISNbrLinkNbrs": hpnicfEviISISNbrLinkNbrs,
       "hpnicfEviISISNbrTable": hpnicfEviISISNbrTable,
       "hpnicfEviISISNbrEntry": hpnicfEviISISNbrEntry,
       "hpnicfEviISISNbrSysId": hpnicfEviISISNbrSysId,
       "hpnicfEviISISNbrMacAddr": hpnicfEviISISNbrMacAddr,
       "hpnicfEviISISNbrSiteId": hpnicfEviISISNbrSiteId,
       "hpnicfEviISISNbrTransStatus": hpnicfEviISISNbrTransStatus,
       "hpnicfEviEnable": hpnicfEviEnable,
       "hpnicfEviEnableTable": hpnicfEviEnableTable,
       "hpnicfEviEnableEntry": hpnicfEviEnableEntry,
       "hpnicfEviEnableStatus": hpnicfEviEnableStatus,
       "hpnicfEviNbr": hpnicfEviNbr,
       "hpnicfEviNbrBaseTable": hpnicfEviNbrBaseTable,
       "hpnicfEviNbrBaseEntry": hpnicfEviNbrBaseEntry,
       "hpnicfEviNbrSelfServerStatus": hpnicfEviNbrSelfServerStatus,
       "hpnicfEviNbrAuthPassword": hpnicfEviNbrAuthPassword,
       "hpnicfEviNbrClientRegisterInterval": hpnicfEviNbrClientRegisterInterval,
       "hpnicfEviNbrRemoteServerTable": hpnicfEviNbrRemoteServerTable,
       "hpnicfEviNbrRemoteServerEntry": hpnicfEviNbrRemoteServerEntry,
       "hpnicfEviNbrRemoteServerType": hpnicfEviNbrRemoteServerType,
       "hpnicfEviNbrRemoteServer": hpnicfEviNbrRemoteServer,
       "hpnicfEviNbrRemoteServerRowStatus": hpnicfEviNbrRemoteServerRowStatus,
       "hpnicfEviNbrTable": hpnicfEviNbrTable,
       "hpnicfEviNbrEntry": hpnicfEviNbrEntry,
       "hpnicfEviNbrAddressType": hpnicfEviNbrAddressType,
       "hpnicfEviNbrAddress": hpnicfEviNbrAddress,
       "hpnicfEviNbrSystemID": hpnicfEviNbrSystemID,
       "hpnicfEviNbrExpireTime": hpnicfEviNbrExpireTime,
       "hpnicfEviNbrStatus": hpnicfEviNbrStatus}
)
