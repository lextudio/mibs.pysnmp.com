# SNMP MIB module (IEEE8021-Q-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-Q-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:20 2024
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

(ieee8021BridgeBasePort,
 ieee8021BridgeBasePortComponentId,
 ieee8021BridgeBasePortEntry) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortComponentId",
    "ieee8021BridgeBasePortEntry")

(IEEE8021BridgePortNumber,
 IEEE8021BridgePortNumberOrZero,
 IEEE8021PbbComponentIdentifier,
 IEEE8021PortAcceptableFrameTypes,
 IEEE8021VlanIndex,
 IEEE8021VlanIndexOrWildcard,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021BridgePortNumberOrZero",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021PortAcceptableFrameTypes",
    "IEEE8021VlanIndex",
    "IEEE8021VlanIndexOrWildcard",
    "ieee802dot1mibs")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021QBridgeMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4)
)
ieee8021QBridgeMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-12-12 00:00",
         "2011-02-27 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021QBridgeMibObjects_ObjectIdentity = ObjectIdentity
ieee8021QBridgeMibObjects = _Ieee8021QBridgeMibObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 1)
)
_Ieee8021QBridgeBase_ObjectIdentity = ObjectIdentity
ieee8021QBridgeBase = _Ieee8021QBridgeBase_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1)
)
_Ieee8021QBridgeTable_Object = MibTable
ieee8021QBridgeTable = _Ieee8021QBridgeTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeTable.setStatus("current")
_Ieee8021QBridgeEntry_Object = MibTableRow
ieee8021QBridgeEntry = _Ieee8021QBridgeEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1, 1)
)
ieee8021QBridgeEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEntry.setStatus("current")
_Ieee8021QBridgeComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeComponentId_Object = MibTableColumn
ieee8021QBridgeComponentId = _Ieee8021QBridgeComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1, 1, 1),
    _Ieee8021QBridgeComponentId_Type()
)
ieee8021QBridgeComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeComponentId.setStatus("current")


class _Ieee8021QBridgeVlanVersionNumber_Type(Integer32):
    """Custom type ieee8021QBridgeVlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_Ieee8021QBridgeVlanVersionNumber_Type.__name__ = "Integer32"
_Ieee8021QBridgeVlanVersionNumber_Object = MibTableColumn
ieee8021QBridgeVlanVersionNumber = _Ieee8021QBridgeVlanVersionNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1, 1, 2),
    _Ieee8021QBridgeVlanVersionNumber_Type()
)
ieee8021QBridgeVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanVersionNumber.setStatus("current")
_Ieee8021QBridgeMaxVlanId_Type = VlanId
_Ieee8021QBridgeMaxVlanId_Object = MibTableColumn
ieee8021QBridgeMaxVlanId = _Ieee8021QBridgeMaxVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1, 1, 3),
    _Ieee8021QBridgeMaxVlanId_Type()
)
ieee8021QBridgeMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeMaxVlanId.setStatus("current")
_Ieee8021QBridgeMaxSupportedVlans_Type = Unsigned32
_Ieee8021QBridgeMaxSupportedVlans_Object = MibTableColumn
ieee8021QBridgeMaxSupportedVlans = _Ieee8021QBridgeMaxSupportedVlans_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1, 1, 4),
    _Ieee8021QBridgeMaxSupportedVlans_Type()
)
ieee8021QBridgeMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeMaxSupportedVlans.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeMaxSupportedVlans.setUnits("vlans")
_Ieee8021QBridgeNumVlans_Type = Gauge32
_Ieee8021QBridgeNumVlans_Object = MibTableColumn
ieee8021QBridgeNumVlans = _Ieee8021QBridgeNumVlans_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1, 1, 5),
    _Ieee8021QBridgeNumVlans_Type()
)
ieee8021QBridgeNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeNumVlans.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeNumVlans.setUnits("vlans")


class _Ieee8021QBridgeMvrpEnabledStatus_Type(TruthValue):
    """Custom type ieee8021QBridgeMvrpEnabledStatus based on TruthValue"""


_Ieee8021QBridgeMvrpEnabledStatus_Object = MibTableColumn
ieee8021QBridgeMvrpEnabledStatus = _Ieee8021QBridgeMvrpEnabledStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 1, 1, 6),
    _Ieee8021QBridgeMvrpEnabledStatus_Type()
)
ieee8021QBridgeMvrpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeMvrpEnabledStatus.setStatus("current")
_Ieee8021QBridgeCVlanPortTable_Object = MibTable
ieee8021QBridgeCVlanPortTable = _Ieee8021QBridgeCVlanPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeCVlanPortTable.setStatus("current")
_Ieee8021QBridgeCVlanPortEntry_Object = MibTableRow
ieee8021QBridgeCVlanPortEntry = _Ieee8021QBridgeCVlanPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 2, 1)
)
ieee8021QBridgeCVlanPortEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeCVlanPortComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeCVlanPortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeCVlanPortEntry.setStatus("current")
_Ieee8021QBridgeCVlanPortComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeCVlanPortComponentId_Object = MibTableColumn
ieee8021QBridgeCVlanPortComponentId = _Ieee8021QBridgeCVlanPortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 2, 1, 1),
    _Ieee8021QBridgeCVlanPortComponentId_Type()
)
ieee8021QBridgeCVlanPortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeCVlanPortComponentId.setStatus("current")
_Ieee8021QBridgeCVlanPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021QBridgeCVlanPortNumber_Object = MibTableColumn
ieee8021QBridgeCVlanPortNumber = _Ieee8021QBridgeCVlanPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 2, 1, 2),
    _Ieee8021QBridgeCVlanPortNumber_Type()
)
ieee8021QBridgeCVlanPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeCVlanPortNumber.setStatus("current")
_Ieee8021QBridgeCVlanPortRowStatus_Type = RowStatus
_Ieee8021QBridgeCVlanPortRowStatus_Object = MibTableColumn
ieee8021QBridgeCVlanPortRowStatus = _Ieee8021QBridgeCVlanPortRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 1, 2, 1, 3),
    _Ieee8021QBridgeCVlanPortRowStatus_Type()
)
ieee8021QBridgeCVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeCVlanPortRowStatus.setStatus("current")
_Ieee8021QBridgeTp_ObjectIdentity = ObjectIdentity
ieee8021QBridgeTp = _Ieee8021QBridgeTp_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2)
)
_Ieee8021QBridgeFdbTable_Object = MibTable
ieee8021QBridgeFdbTable = _Ieee8021QBridgeFdbTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbTable.setStatus("current")
_Ieee8021QBridgeFdbEntry_Object = MibTableRow
ieee8021QBridgeFdbEntry = _Ieee8021QBridgeFdbEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 1, 1)
)
ieee8021QBridgeFdbEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeFdbComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeFdbId"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbEntry.setStatus("current")
_Ieee8021QBridgeFdbComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeFdbComponentId_Object = MibTableColumn
ieee8021QBridgeFdbComponentId = _Ieee8021QBridgeFdbComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 1, 1, 1),
    _Ieee8021QBridgeFdbComponentId_Type()
)
ieee8021QBridgeFdbComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbComponentId.setStatus("current")


class _Ieee8021QBridgeFdbId_Type(Unsigned32):
    """Custom type ieee8021QBridgeFdbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ieee8021QBridgeFdbId_Type.__name__ = "Unsigned32"
_Ieee8021QBridgeFdbId_Object = MibTableColumn
ieee8021QBridgeFdbId = _Ieee8021QBridgeFdbId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 1, 1, 2),
    _Ieee8021QBridgeFdbId_Type()
)
ieee8021QBridgeFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbId.setStatus("current")
_Ieee8021QBridgeFdbDynamicCount_Type = Gauge32
_Ieee8021QBridgeFdbDynamicCount_Object = MibTableColumn
ieee8021QBridgeFdbDynamicCount = _Ieee8021QBridgeFdbDynamicCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 1, 1, 3),
    _Ieee8021QBridgeFdbDynamicCount_Type()
)
ieee8021QBridgeFdbDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbDynamicCount.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbDynamicCount.setUnits("database entries")
_Ieee8021QBridgeFdbLearnedEntryDiscards_Type = Counter64
_Ieee8021QBridgeFdbLearnedEntryDiscards_Object = MibTableColumn
ieee8021QBridgeFdbLearnedEntryDiscards = _Ieee8021QBridgeFdbLearnedEntryDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 1, 1, 4),
    _Ieee8021QBridgeFdbLearnedEntryDiscards_Type()
)
ieee8021QBridgeFdbLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbLearnedEntryDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbLearnedEntryDiscards.setUnits("database entries")


class _Ieee8021QBridgeFdbAgingTime_Type(Integer32):
    """Custom type ieee8021QBridgeFdbAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Ieee8021QBridgeFdbAgingTime_Type.__name__ = "Integer32"
_Ieee8021QBridgeFdbAgingTime_Object = MibTableColumn
ieee8021QBridgeFdbAgingTime = _Ieee8021QBridgeFdbAgingTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 1, 1, 5),
    _Ieee8021QBridgeFdbAgingTime_Type()
)
ieee8021QBridgeFdbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbAgingTime.setUnits("seconds")
_Ieee8021QBridgeTpFdbTable_Object = MibTable
ieee8021QBridgeTpFdbTable = _Ieee8021QBridgeTpFdbTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeTpFdbTable.setStatus("current")
_Ieee8021QBridgeTpFdbEntry_Object = MibTableRow
ieee8021QBridgeTpFdbEntry = _Ieee8021QBridgeTpFdbEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 2, 1)
)
ieee8021QBridgeTpFdbEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeFdbComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeFdbId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpFdbAddress"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeTpFdbEntry.setStatus("current")
_Ieee8021QBridgeTpFdbAddress_Type = MacAddress
_Ieee8021QBridgeTpFdbAddress_Object = MibTableColumn
ieee8021QBridgeTpFdbAddress = _Ieee8021QBridgeTpFdbAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 2, 1, 1),
    _Ieee8021QBridgeTpFdbAddress_Type()
)
ieee8021QBridgeTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpFdbAddress.setStatus("current")
_Ieee8021QBridgeTpFdbPort_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021QBridgeTpFdbPort_Object = MibTableColumn
ieee8021QBridgeTpFdbPort = _Ieee8021QBridgeTpFdbPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 2, 1, 2),
    _Ieee8021QBridgeTpFdbPort_Type()
)
ieee8021QBridgeTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpFdbPort.setStatus("current")


class _Ieee8021QBridgeTpFdbStatus_Type(Integer32):
    """Custom type ieee8021QBridgeTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_Ieee8021QBridgeTpFdbStatus_Type.__name__ = "Integer32"
_Ieee8021QBridgeTpFdbStatus_Object = MibTableColumn
ieee8021QBridgeTpFdbStatus = _Ieee8021QBridgeTpFdbStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 2, 1, 3),
    _Ieee8021QBridgeTpFdbStatus_Type()
)
ieee8021QBridgeTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpFdbStatus.setStatus("current")
_Ieee8021QBridgeTpGroupTable_Object = MibTable
ieee8021QBridgeTpGroupTable = _Ieee8021QBridgeTpGroupTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeTpGroupTable.setStatus("current")
_Ieee8021QBridgeTpGroupEntry_Object = MibTableRow
ieee8021QBridgeTpGroupEntry = _Ieee8021QBridgeTpGroupEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 3, 1)
)
ieee8021QBridgeTpGroupEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanIndex"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpGroupAddress"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeTpGroupEntry.setStatus("current")
_Ieee8021QBridgeTpGroupAddress_Type = MacAddress
_Ieee8021QBridgeTpGroupAddress_Object = MibTableColumn
ieee8021QBridgeTpGroupAddress = _Ieee8021QBridgeTpGroupAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 3, 1, 1),
    _Ieee8021QBridgeTpGroupAddress_Type()
)
ieee8021QBridgeTpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpGroupAddress.setStatus("current")
_Ieee8021QBridgeTpGroupEgressPorts_Type = PortList
_Ieee8021QBridgeTpGroupEgressPorts_Object = MibTableColumn
ieee8021QBridgeTpGroupEgressPorts = _Ieee8021QBridgeTpGroupEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 3, 1, 2),
    _Ieee8021QBridgeTpGroupEgressPorts_Type()
)
ieee8021QBridgeTpGroupEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpGroupEgressPorts.setStatus("current")
_Ieee8021QBridgeTpGroupLearnt_Type = PortList
_Ieee8021QBridgeTpGroupLearnt_Object = MibTableColumn
ieee8021QBridgeTpGroupLearnt = _Ieee8021QBridgeTpGroupLearnt_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 3, 1, 3),
    _Ieee8021QBridgeTpGroupLearnt_Type()
)
ieee8021QBridgeTpGroupLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpGroupLearnt.setStatus("current")
_Ieee8021QBridgeForwardAllTable_Object = MibTable
ieee8021QBridgeForwardAllTable = _Ieee8021QBridgeForwardAllTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardAllTable.setStatus("current")
_Ieee8021QBridgeForwardAllEntry_Object = MibTableRow
ieee8021QBridgeForwardAllEntry = _Ieee8021QBridgeForwardAllEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 4, 1)
)
ieee8021QBridgeForwardAllEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardAllVlanIndex"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardAllEntry.setStatus("current")
_Ieee8021QBridgeForwardAllVlanIndex_Type = IEEE8021VlanIndexOrWildcard
_Ieee8021QBridgeForwardAllVlanIndex_Object = MibTableColumn
ieee8021QBridgeForwardAllVlanIndex = _Ieee8021QBridgeForwardAllVlanIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 4, 1, 1),
    _Ieee8021QBridgeForwardAllVlanIndex_Type()
)
ieee8021QBridgeForwardAllVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardAllVlanIndex.setStatus("current")
_Ieee8021QBridgeForwardAllPorts_Type = PortList
_Ieee8021QBridgeForwardAllPorts_Object = MibTableColumn
ieee8021QBridgeForwardAllPorts = _Ieee8021QBridgeForwardAllPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 4, 1, 2),
    _Ieee8021QBridgeForwardAllPorts_Type()
)
ieee8021QBridgeForwardAllPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardAllPorts.setStatus("current")
_Ieee8021QBridgeForwardAllStaticPorts_Type = PortList
_Ieee8021QBridgeForwardAllStaticPorts_Object = MibTableColumn
ieee8021QBridgeForwardAllStaticPorts = _Ieee8021QBridgeForwardAllStaticPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 4, 1, 3),
    _Ieee8021QBridgeForwardAllStaticPorts_Type()
)
ieee8021QBridgeForwardAllStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardAllStaticPorts.setStatus("current")
_Ieee8021QBridgeForwardAllForbiddenPorts_Type = PortList
_Ieee8021QBridgeForwardAllForbiddenPorts_Object = MibTableColumn
ieee8021QBridgeForwardAllForbiddenPorts = _Ieee8021QBridgeForwardAllForbiddenPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 4, 1, 4),
    _Ieee8021QBridgeForwardAllForbiddenPorts_Type()
)
ieee8021QBridgeForwardAllForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardAllForbiddenPorts.setStatus("current")
_Ieee8021QBridgeForwardUnregisteredTable_Object = MibTable
ieee8021QBridgeForwardUnregisteredTable = _Ieee8021QBridgeForwardUnregisteredTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardUnregisteredTable.setStatus("current")
_Ieee8021QBridgeForwardUnregisteredEntry_Object = MibTableRow
ieee8021QBridgeForwardUnregisteredEntry = _Ieee8021QBridgeForwardUnregisteredEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 5, 1)
)
ieee8021QBridgeForwardUnregisteredEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardUnregisteredVlanIndex"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardUnregisteredEntry.setStatus("current")
_Ieee8021QBridgeForwardUnregisteredVlanIndex_Type = IEEE8021VlanIndexOrWildcard
_Ieee8021QBridgeForwardUnregisteredVlanIndex_Object = MibTableColumn
ieee8021QBridgeForwardUnregisteredVlanIndex = _Ieee8021QBridgeForwardUnregisteredVlanIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 5, 1, 1),
    _Ieee8021QBridgeForwardUnregisteredVlanIndex_Type()
)
ieee8021QBridgeForwardUnregisteredVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardUnregisteredVlanIndex.setStatus("current")
_Ieee8021QBridgeForwardUnregisteredPorts_Type = PortList
_Ieee8021QBridgeForwardUnregisteredPorts_Object = MibTableColumn
ieee8021QBridgeForwardUnregisteredPorts = _Ieee8021QBridgeForwardUnregisteredPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 5, 1, 2),
    _Ieee8021QBridgeForwardUnregisteredPorts_Type()
)
ieee8021QBridgeForwardUnregisteredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardUnregisteredPorts.setStatus("current")
_Ieee8021QBridgeForwardUnregisteredStaticPorts_Type = PortList
_Ieee8021QBridgeForwardUnregisteredStaticPorts_Object = MibTableColumn
ieee8021QBridgeForwardUnregisteredStaticPorts = _Ieee8021QBridgeForwardUnregisteredStaticPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 5, 1, 3),
    _Ieee8021QBridgeForwardUnregisteredStaticPorts_Type()
)
ieee8021QBridgeForwardUnregisteredStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardUnregisteredStaticPorts.setStatus("current")
_Ieee8021QBridgeForwardUnregisteredForbiddenPorts_Type = PortList
_Ieee8021QBridgeForwardUnregisteredForbiddenPorts_Object = MibTableColumn
ieee8021QBridgeForwardUnregisteredForbiddenPorts = _Ieee8021QBridgeForwardUnregisteredForbiddenPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 2, 5, 1, 4),
    _Ieee8021QBridgeForwardUnregisteredForbiddenPorts_Type()
)
ieee8021QBridgeForwardUnregisteredForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeForwardUnregisteredForbiddenPorts.setStatus("current")
_Ieee8021QBridgeStatic_ObjectIdentity = ObjectIdentity
ieee8021QBridgeStatic = _Ieee8021QBridgeStatic_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3)
)
_Ieee8021QBridgeStaticUnicastTable_Object = MibTable
ieee8021QBridgeStaticUnicastTable = _Ieee8021QBridgeStaticUnicastTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastTable.setStatus("current")
_Ieee8021QBridgeStaticUnicastEntry_Object = MibTableRow
ieee8021QBridgeStaticUnicastEntry = _Ieee8021QBridgeStaticUnicastEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1)
)
ieee8021QBridgeStaticUnicastEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastVlanIndex"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastAddress"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastReceivePort"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastEntry.setStatus("current")
_Ieee8021QBridgeStaticUnicastComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeStaticUnicastComponentId_Object = MibTableColumn
ieee8021QBridgeStaticUnicastComponentId = _Ieee8021QBridgeStaticUnicastComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 1),
    _Ieee8021QBridgeStaticUnicastComponentId_Type()
)
ieee8021QBridgeStaticUnicastComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastComponentId.setStatus("current")
_Ieee8021QBridgeStaticUnicastVlanIndex_Type = IEEE8021VlanIndexOrWildcard
_Ieee8021QBridgeStaticUnicastVlanIndex_Object = MibTableColumn
ieee8021QBridgeStaticUnicastVlanIndex = _Ieee8021QBridgeStaticUnicastVlanIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 2),
    _Ieee8021QBridgeStaticUnicastVlanIndex_Type()
)
ieee8021QBridgeStaticUnicastVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastVlanIndex.setStatus("current")
_Ieee8021QBridgeStaticUnicastAddress_Type = MacAddress
_Ieee8021QBridgeStaticUnicastAddress_Object = MibTableColumn
ieee8021QBridgeStaticUnicastAddress = _Ieee8021QBridgeStaticUnicastAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 3),
    _Ieee8021QBridgeStaticUnicastAddress_Type()
)
ieee8021QBridgeStaticUnicastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastAddress.setStatus("current")
_Ieee8021QBridgeStaticUnicastReceivePort_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021QBridgeStaticUnicastReceivePort_Object = MibTableColumn
ieee8021QBridgeStaticUnicastReceivePort = _Ieee8021QBridgeStaticUnicastReceivePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 4),
    _Ieee8021QBridgeStaticUnicastReceivePort_Type()
)
ieee8021QBridgeStaticUnicastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastReceivePort.setStatus("current")


class _Ieee8021QBridgeStaticUnicastStaticEgressPorts_Type(PortList):
    """Custom type ieee8021QBridgeStaticUnicastStaticEgressPorts based on PortList"""
    defaultHexValue = ""


_Ieee8021QBridgeStaticUnicastStaticEgressPorts_Object = MibTableColumn
ieee8021QBridgeStaticUnicastStaticEgressPorts = _Ieee8021QBridgeStaticUnicastStaticEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 5),
    _Ieee8021QBridgeStaticUnicastStaticEgressPorts_Type()
)
ieee8021QBridgeStaticUnicastStaticEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastStaticEgressPorts.setStatus("current")


class _Ieee8021QBridgeStaticUnicastForbiddenEgressPorts_Type(PortList):
    """Custom type ieee8021QBridgeStaticUnicastForbiddenEgressPorts based on PortList"""
    defaultHexValue = ""


_Ieee8021QBridgeStaticUnicastForbiddenEgressPorts_Object = MibTableColumn
ieee8021QBridgeStaticUnicastForbiddenEgressPorts = _Ieee8021QBridgeStaticUnicastForbiddenEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 6),
    _Ieee8021QBridgeStaticUnicastForbiddenEgressPorts_Type()
)
ieee8021QBridgeStaticUnicastForbiddenEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastForbiddenEgressPorts.setStatus("current")


class _Ieee8021QBridgeStaticUnicastStorageType_Type(StorageType):
    """Custom type ieee8021QBridgeStaticUnicastStorageType based on StorageType"""


_Ieee8021QBridgeStaticUnicastStorageType_Object = MibTableColumn
ieee8021QBridgeStaticUnicastStorageType = _Ieee8021QBridgeStaticUnicastStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 7),
    _Ieee8021QBridgeStaticUnicastStorageType_Type()
)
ieee8021QBridgeStaticUnicastStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastStorageType.setStatus("current")
_Ieee8021QBridgeStaticUnicastRowStatus_Type = RowStatus
_Ieee8021QBridgeStaticUnicastRowStatus_Object = MibTableColumn
ieee8021QBridgeStaticUnicastRowStatus = _Ieee8021QBridgeStaticUnicastRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 1, 1, 8),
    _Ieee8021QBridgeStaticUnicastRowStatus_Type()
)
ieee8021QBridgeStaticUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticUnicastRowStatus.setStatus("current")
_Ieee8021QBridgeStaticMulticastTable_Object = MibTable
ieee8021QBridgeStaticMulticastTable = _Ieee8021QBridgeStaticMulticastTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastTable.setStatus("current")
_Ieee8021QBridgeStaticMulticastEntry_Object = MibTableRow
ieee8021QBridgeStaticMulticastEntry = _Ieee8021QBridgeStaticMulticastEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2, 1)
)
ieee8021QBridgeStaticMulticastEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanIndex"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticMulticastAddress"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticMulticastReceivePort"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastEntry.setStatus("current")
_Ieee8021QBridgeStaticMulticastAddress_Type = MacAddress
_Ieee8021QBridgeStaticMulticastAddress_Object = MibTableColumn
ieee8021QBridgeStaticMulticastAddress = _Ieee8021QBridgeStaticMulticastAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2, 1, 1),
    _Ieee8021QBridgeStaticMulticastAddress_Type()
)
ieee8021QBridgeStaticMulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastAddress.setStatus("current")
_Ieee8021QBridgeStaticMulticastReceivePort_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021QBridgeStaticMulticastReceivePort_Object = MibTableColumn
ieee8021QBridgeStaticMulticastReceivePort = _Ieee8021QBridgeStaticMulticastReceivePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2, 1, 2),
    _Ieee8021QBridgeStaticMulticastReceivePort_Type()
)
ieee8021QBridgeStaticMulticastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastReceivePort.setStatus("current")


class _Ieee8021QBridgeStaticMulticastStaticEgressPorts_Type(PortList):
    """Custom type ieee8021QBridgeStaticMulticastStaticEgressPorts based on PortList"""
    defaultHexValue = ""


_Ieee8021QBridgeStaticMulticastStaticEgressPorts_Object = MibTableColumn
ieee8021QBridgeStaticMulticastStaticEgressPorts = _Ieee8021QBridgeStaticMulticastStaticEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2, 1, 3),
    _Ieee8021QBridgeStaticMulticastStaticEgressPorts_Type()
)
ieee8021QBridgeStaticMulticastStaticEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastStaticEgressPorts.setStatus("current")


class _Ieee8021QBridgeStaticMulticastForbiddenEgressPorts_Type(PortList):
    """Custom type ieee8021QBridgeStaticMulticastForbiddenEgressPorts based on PortList"""
    defaultHexValue = ""


_Ieee8021QBridgeStaticMulticastForbiddenEgressPorts_Object = MibTableColumn
ieee8021QBridgeStaticMulticastForbiddenEgressPorts = _Ieee8021QBridgeStaticMulticastForbiddenEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2, 1, 4),
    _Ieee8021QBridgeStaticMulticastForbiddenEgressPorts_Type()
)
ieee8021QBridgeStaticMulticastForbiddenEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastForbiddenEgressPorts.setStatus("current")


class _Ieee8021QBridgeStaticMulticastStorageType_Type(StorageType):
    """Custom type ieee8021QBridgeStaticMulticastStorageType based on StorageType"""


_Ieee8021QBridgeStaticMulticastStorageType_Object = MibTableColumn
ieee8021QBridgeStaticMulticastStorageType = _Ieee8021QBridgeStaticMulticastStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2, 1, 5),
    _Ieee8021QBridgeStaticMulticastStorageType_Type()
)
ieee8021QBridgeStaticMulticastStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastStorageType.setStatus("current")
_Ieee8021QBridgeStaticMulticastRowStatus_Type = RowStatus
_Ieee8021QBridgeStaticMulticastRowStatus_Object = MibTableColumn
ieee8021QBridgeStaticMulticastRowStatus = _Ieee8021QBridgeStaticMulticastRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 3, 2, 1, 6),
    _Ieee8021QBridgeStaticMulticastRowStatus_Type()
)
ieee8021QBridgeStaticMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeStaticMulticastRowStatus.setStatus("current")
_Ieee8021QBridgeVlan_ObjectIdentity = ObjectIdentity
ieee8021QBridgeVlan = _Ieee8021QBridgeVlan_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4)
)
_Ieee8021QBridgeVlanNumDeletes_Type = Counter64
_Ieee8021QBridgeVlanNumDeletes_Object = MibScalar
ieee8021QBridgeVlanNumDeletes = _Ieee8021QBridgeVlanNumDeletes_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 1),
    _Ieee8021QBridgeVlanNumDeletes_Type()
)
ieee8021QBridgeVlanNumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanNumDeletes.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanNumDeletes.setUnits("vlan deletions")
_Ieee8021QBridgeVlanCurrentTable_Object = MibTable
ieee8021QBridgeVlanCurrentTable = _Ieee8021QBridgeVlanCurrentTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanCurrentTable.setStatus("current")
_Ieee8021QBridgeVlanCurrentEntry_Object = MibTableRow
ieee8021QBridgeVlanCurrentEntry = _Ieee8021QBridgeVlanCurrentEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1)
)
ieee8021QBridgeVlanCurrentEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanTimeMark"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanIndex"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanCurrentEntry.setStatus("current")
_Ieee8021QBridgeVlanTimeMark_Type = TimeFilter
_Ieee8021QBridgeVlanTimeMark_Object = MibTableColumn
ieee8021QBridgeVlanTimeMark = _Ieee8021QBridgeVlanTimeMark_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 1),
    _Ieee8021QBridgeVlanTimeMark_Type()
)
ieee8021QBridgeVlanTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanTimeMark.setStatus("current")
_Ieee8021QBridgeVlanCurrentComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeVlanCurrentComponentId_Object = MibTableColumn
ieee8021QBridgeVlanCurrentComponentId = _Ieee8021QBridgeVlanCurrentComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 2),
    _Ieee8021QBridgeVlanCurrentComponentId_Type()
)
ieee8021QBridgeVlanCurrentComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanCurrentComponentId.setStatus("current")
_Ieee8021QBridgeVlanIndex_Type = IEEE8021VlanIndex
_Ieee8021QBridgeVlanIndex_Object = MibTableColumn
ieee8021QBridgeVlanIndex = _Ieee8021QBridgeVlanIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 3),
    _Ieee8021QBridgeVlanIndex_Type()
)
ieee8021QBridgeVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanIndex.setStatus("current")
_Ieee8021QBridgeVlanFdbId_Type = Unsigned32
_Ieee8021QBridgeVlanFdbId_Object = MibTableColumn
ieee8021QBridgeVlanFdbId = _Ieee8021QBridgeVlanFdbId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 4),
    _Ieee8021QBridgeVlanFdbId_Type()
)
ieee8021QBridgeVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanFdbId.setStatus("current")
_Ieee8021QBridgeVlanCurrentEgressPorts_Type = PortList
_Ieee8021QBridgeVlanCurrentEgressPorts_Object = MibTableColumn
ieee8021QBridgeVlanCurrentEgressPorts = _Ieee8021QBridgeVlanCurrentEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 5),
    _Ieee8021QBridgeVlanCurrentEgressPorts_Type()
)
ieee8021QBridgeVlanCurrentEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanCurrentEgressPorts.setStatus("current")
_Ieee8021QBridgeVlanCurrentUntaggedPorts_Type = PortList
_Ieee8021QBridgeVlanCurrentUntaggedPorts_Object = MibTableColumn
ieee8021QBridgeVlanCurrentUntaggedPorts = _Ieee8021QBridgeVlanCurrentUntaggedPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 6),
    _Ieee8021QBridgeVlanCurrentUntaggedPorts_Type()
)
ieee8021QBridgeVlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanCurrentUntaggedPorts.setStatus("current")


class _Ieee8021QBridgeVlanStatus_Type(Integer32):
    """Custom type ieee8021QBridgeVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicMvrp", 3),
          ("other", 1),
          ("permanent", 2))
    )


_Ieee8021QBridgeVlanStatus_Type.__name__ = "Integer32"
_Ieee8021QBridgeVlanStatus_Object = MibTableColumn
ieee8021QBridgeVlanStatus = _Ieee8021QBridgeVlanStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 7),
    _Ieee8021QBridgeVlanStatus_Type()
)
ieee8021QBridgeVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStatus.setStatus("current")
_Ieee8021QBridgeVlanCreationTime_Type = TimeTicks
_Ieee8021QBridgeVlanCreationTime_Object = MibTableColumn
ieee8021QBridgeVlanCreationTime = _Ieee8021QBridgeVlanCreationTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 2, 1, 8),
    _Ieee8021QBridgeVlanCreationTime_Type()
)
ieee8021QBridgeVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanCreationTime.setStatus("current")
_Ieee8021QBridgeVlanStaticTable_Object = MibTable
ieee8021QBridgeVlanStaticTable = _Ieee8021QBridgeVlanStaticTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticTable.setStatus("current")
_Ieee8021QBridgeVlanStaticEntry_Object = MibTableRow
ieee8021QBridgeVlanStaticEntry = _Ieee8021QBridgeVlanStaticEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1)
)
ieee8021QBridgeVlanStaticEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanStaticComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticEntry.setStatus("current")
_Ieee8021QBridgeVlanStaticComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeVlanStaticComponentId_Object = MibTableColumn
ieee8021QBridgeVlanStaticComponentId = _Ieee8021QBridgeVlanStaticComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1, 1),
    _Ieee8021QBridgeVlanStaticComponentId_Type()
)
ieee8021QBridgeVlanStaticComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticComponentId.setStatus("current")
_Ieee8021QBridgeVlanStaticVlanIndex_Type = IEEE8021VlanIndex
_Ieee8021QBridgeVlanStaticVlanIndex_Object = MibTableColumn
ieee8021QBridgeVlanStaticVlanIndex = _Ieee8021QBridgeVlanStaticVlanIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1, 2),
    _Ieee8021QBridgeVlanStaticVlanIndex_Type()
)
ieee8021QBridgeVlanStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticVlanIndex.setStatus("current")


class _Ieee8021QBridgeVlanStaticName_Type(SnmpAdminString):
    """Custom type ieee8021QBridgeVlanStaticName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ieee8021QBridgeVlanStaticName_Type.__name__ = "SnmpAdminString"
_Ieee8021QBridgeVlanStaticName_Object = MibTableColumn
ieee8021QBridgeVlanStaticName = _Ieee8021QBridgeVlanStaticName_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1, 3),
    _Ieee8021QBridgeVlanStaticName_Type()
)
ieee8021QBridgeVlanStaticName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticName.setStatus("current")
_Ieee8021QBridgeVlanStaticEgressPorts_Type = PortList
_Ieee8021QBridgeVlanStaticEgressPorts_Object = MibTableColumn
ieee8021QBridgeVlanStaticEgressPorts = _Ieee8021QBridgeVlanStaticEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1, 4),
    _Ieee8021QBridgeVlanStaticEgressPorts_Type()
)
ieee8021QBridgeVlanStaticEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticEgressPorts.setStatus("current")
_Ieee8021QBridgeVlanForbiddenEgressPorts_Type = PortList
_Ieee8021QBridgeVlanForbiddenEgressPorts_Object = MibTableColumn
ieee8021QBridgeVlanForbiddenEgressPorts = _Ieee8021QBridgeVlanForbiddenEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1, 5),
    _Ieee8021QBridgeVlanForbiddenEgressPorts_Type()
)
ieee8021QBridgeVlanForbiddenEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanForbiddenEgressPorts.setStatus("current")
_Ieee8021QBridgeVlanStaticUntaggedPorts_Type = PortList
_Ieee8021QBridgeVlanStaticUntaggedPorts_Object = MibTableColumn
ieee8021QBridgeVlanStaticUntaggedPorts = _Ieee8021QBridgeVlanStaticUntaggedPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1, 6),
    _Ieee8021QBridgeVlanStaticUntaggedPorts_Type()
)
ieee8021QBridgeVlanStaticUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticUntaggedPorts.setStatus("current")
_Ieee8021QBridgeVlanStaticRowStatus_Type = RowStatus
_Ieee8021QBridgeVlanStaticRowStatus_Object = MibTableColumn
ieee8021QBridgeVlanStaticRowStatus = _Ieee8021QBridgeVlanStaticRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 3, 1, 7),
    _Ieee8021QBridgeVlanStaticRowStatus_Type()
)
ieee8021QBridgeVlanStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticRowStatus.setStatus("current")
_Ieee8021QBridgeNextFreeLocalVlanTable_Object = MibTable
ieee8021QBridgeNextFreeLocalVlanTable = _Ieee8021QBridgeNextFreeLocalVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeNextFreeLocalVlanTable.setStatus("current")
_Ieee8021QBridgeNextFreeLocalVlanEntry_Object = MibTableRow
ieee8021QBridgeNextFreeLocalVlanEntry = _Ieee8021QBridgeNextFreeLocalVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 4, 1)
)
ieee8021QBridgeNextFreeLocalVlanEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeNextFreeLocalVlanComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeNextFreeLocalVlanEntry.setStatus("current")
_Ieee8021QBridgeNextFreeLocalVlanComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeNextFreeLocalVlanComponentId_Object = MibTableColumn
ieee8021QBridgeNextFreeLocalVlanComponentId = _Ieee8021QBridgeNextFreeLocalVlanComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 4, 1, 1),
    _Ieee8021QBridgeNextFreeLocalVlanComponentId_Type()
)
ieee8021QBridgeNextFreeLocalVlanComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeNextFreeLocalVlanComponentId.setStatus("current")


class _Ieee8021QBridgeNextFreeLocalVlanIndex_Type(Unsigned32):
    """Custom type ieee8021QBridgeNextFreeLocalVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4096, 4294967295),
    )


_Ieee8021QBridgeNextFreeLocalVlanIndex_Type.__name__ = "Unsigned32"
_Ieee8021QBridgeNextFreeLocalVlanIndex_Object = MibTableColumn
ieee8021QBridgeNextFreeLocalVlanIndex = _Ieee8021QBridgeNextFreeLocalVlanIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 4, 1, 2),
    _Ieee8021QBridgeNextFreeLocalVlanIndex_Type()
)
ieee8021QBridgeNextFreeLocalVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeNextFreeLocalVlanIndex.setStatus("current")
_Ieee8021QBridgePortVlanTable_Object = MibTable
ieee8021QBridgePortVlanTable = _Ieee8021QBridgePortVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortVlanTable.setStatus("current")
_Ieee8021QBridgePortVlanEntry_Object = MibTableRow
ieee8021QBridgePortVlanEntry = _Ieee8021QBridgePortVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortVlanEntry.setStatus("current")


class _Ieee8021QBridgePvid_Type(IEEE8021VlanIndex):
    """Custom type ieee8021QBridgePvid based on IEEE8021VlanIndex"""
    defaultValue = 1


_Ieee8021QBridgePvid_Object = MibTableColumn
ieee8021QBridgePvid = _Ieee8021QBridgePvid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1, 1),
    _Ieee8021QBridgePvid_Type()
)
ieee8021QBridgePvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgePvid.setStatus("current")


class _Ieee8021QBridgePortAcceptableFrameTypes_Type(IEEE8021PortAcceptableFrameTypes):
    """Custom type ieee8021QBridgePortAcceptableFrameTypes based on IEEE8021PortAcceptableFrameTypes"""


_Ieee8021QBridgePortAcceptableFrameTypes_Object = MibTableColumn
ieee8021QBridgePortAcceptableFrameTypes = _Ieee8021QBridgePortAcceptableFrameTypes_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1, 2),
    _Ieee8021QBridgePortAcceptableFrameTypes_Type()
)
ieee8021QBridgePortAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgePortAcceptableFrameTypes.setStatus("current")


class _Ieee8021QBridgePortIngressFiltering_Type(TruthValue):
    """Custom type ieee8021QBridgePortIngressFiltering based on TruthValue"""


_Ieee8021QBridgePortIngressFiltering_Object = MibTableColumn
ieee8021QBridgePortIngressFiltering = _Ieee8021QBridgePortIngressFiltering_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1, 3),
    _Ieee8021QBridgePortIngressFiltering_Type()
)
ieee8021QBridgePortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgePortIngressFiltering.setStatus("current")


class _Ieee8021QBridgePortMvrpEnabledStatus_Type(TruthValue):
    """Custom type ieee8021QBridgePortMvrpEnabledStatus based on TruthValue"""


_Ieee8021QBridgePortMvrpEnabledStatus_Object = MibTableColumn
ieee8021QBridgePortMvrpEnabledStatus = _Ieee8021QBridgePortMvrpEnabledStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1, 4),
    _Ieee8021QBridgePortMvrpEnabledStatus_Type()
)
ieee8021QBridgePortMvrpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgePortMvrpEnabledStatus.setStatus("current")
_Ieee8021QBridgePortMvrpFailedRegistrations_Type = Counter64
_Ieee8021QBridgePortMvrpFailedRegistrations_Object = MibTableColumn
ieee8021QBridgePortMvrpFailedRegistrations = _Ieee8021QBridgePortMvrpFailedRegistrations_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1, 5),
    _Ieee8021QBridgePortMvrpFailedRegistrations_Type()
)
ieee8021QBridgePortMvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgePortMvrpFailedRegistrations.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgePortMvrpFailedRegistrations.setUnits("failed MVRP registrations")
_Ieee8021QBridgePortMvrpLastPduOrigin_Type = MacAddress
_Ieee8021QBridgePortMvrpLastPduOrigin_Object = MibTableColumn
ieee8021QBridgePortMvrpLastPduOrigin = _Ieee8021QBridgePortMvrpLastPduOrigin_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1, 6),
    _Ieee8021QBridgePortMvrpLastPduOrigin_Type()
)
ieee8021QBridgePortMvrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgePortMvrpLastPduOrigin.setStatus("current")


class _Ieee8021QBridgePortRestrictedVlanRegistration_Type(TruthValue):
    """Custom type ieee8021QBridgePortRestrictedVlanRegistration based on TruthValue"""


_Ieee8021QBridgePortRestrictedVlanRegistration_Object = MibTableColumn
ieee8021QBridgePortRestrictedVlanRegistration = _Ieee8021QBridgePortRestrictedVlanRegistration_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 5, 1, 7),
    _Ieee8021QBridgePortRestrictedVlanRegistration_Type()
)
ieee8021QBridgePortRestrictedVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgePortRestrictedVlanRegistration.setStatus("current")
_Ieee8021QBridgePortVlanStatisticsTable_Object = MibTable
ieee8021QBridgePortVlanStatisticsTable = _Ieee8021QBridgePortVlanStatisticsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortVlanStatisticsTable.setStatus("current")
_Ieee8021QBridgePortVlanStatisticsEntry_Object = MibTableRow
ieee8021QBridgePortVlanStatisticsEntry = _Ieee8021QBridgePortVlanStatisticsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 6, 1)
)
ieee8021QBridgePortVlanStatisticsEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanIndex"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortVlanStatisticsEntry.setStatus("current")
_Ieee8021QBridgeTpVlanPortInFrames_Type = Counter64
_Ieee8021QBridgeTpVlanPortInFrames_Object = MibTableColumn
ieee8021QBridgeTpVlanPortInFrames = _Ieee8021QBridgeTpVlanPortInFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 6, 1, 1),
    _Ieee8021QBridgeTpVlanPortInFrames_Type()
)
ieee8021QBridgeTpVlanPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortInFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortInFrames.setUnits("frames")
_Ieee8021QBridgeTpVlanPortOutFrames_Type = Counter64
_Ieee8021QBridgeTpVlanPortOutFrames_Object = MibTableColumn
ieee8021QBridgeTpVlanPortOutFrames = _Ieee8021QBridgeTpVlanPortOutFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 6, 1, 2),
    _Ieee8021QBridgeTpVlanPortOutFrames_Type()
)
ieee8021QBridgeTpVlanPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortOutFrames.setUnits("frames")
_Ieee8021QBridgeTpVlanPortInDiscards_Type = Counter64
_Ieee8021QBridgeTpVlanPortInDiscards_Object = MibTableColumn
ieee8021QBridgeTpVlanPortInDiscards = _Ieee8021QBridgeTpVlanPortInDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 6, 1, 3),
    _Ieee8021QBridgeTpVlanPortInDiscards_Type()
)
ieee8021QBridgeTpVlanPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021QBridgeTpVlanPortInDiscards.setUnits("frames")
_Ieee8021QBridgeLearningConstraintsTable_Object = MibTable
ieee8021QBridgeLearningConstraintsTable = _Ieee8021QBridgeLearningConstraintsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 8)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsTable.setStatus("deprecated")
_Ieee8021QBridgeLearningConstraintsEntry_Object = MibTableRow
ieee8021QBridgeLearningConstraintsEntry = _Ieee8021QBridgeLearningConstraintsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 8, 1)
)
ieee8021QBridgeLearningConstraintsEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintsComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintsVlan"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintsSet"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsEntry.setStatus("deprecated")
_Ieee8021QBridgeLearningConstraintsComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeLearningConstraintsComponentId_Object = MibTableColumn
ieee8021QBridgeLearningConstraintsComponentId = _Ieee8021QBridgeLearningConstraintsComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 8, 1, 1),
    _Ieee8021QBridgeLearningConstraintsComponentId_Type()
)
ieee8021QBridgeLearningConstraintsComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsComponentId.setStatus("deprecated")
_Ieee8021QBridgeLearningConstraintsVlan_Type = IEEE8021VlanIndex
_Ieee8021QBridgeLearningConstraintsVlan_Object = MibTableColumn
ieee8021QBridgeLearningConstraintsVlan = _Ieee8021QBridgeLearningConstraintsVlan_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 8, 1, 2),
    _Ieee8021QBridgeLearningConstraintsVlan_Type()
)
ieee8021QBridgeLearningConstraintsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsVlan.setStatus("deprecated")


class _Ieee8021QBridgeLearningConstraintsSet_Type(Integer32):
    """Custom type ieee8021QBridgeLearningConstraintsSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021QBridgeLearningConstraintsSet_Type.__name__ = "Integer32"
_Ieee8021QBridgeLearningConstraintsSet_Object = MibTableColumn
ieee8021QBridgeLearningConstraintsSet = _Ieee8021QBridgeLearningConstraintsSet_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 8, 1, 3),
    _Ieee8021QBridgeLearningConstraintsSet_Type()
)
ieee8021QBridgeLearningConstraintsSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsSet.setStatus("deprecated")


class _Ieee8021QBridgeLearningConstraintsType_Type(Integer32):
    """Custom type ieee8021QBridgeLearningConstraintsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("shared", 2))
    )


_Ieee8021QBridgeLearningConstraintsType_Type.__name__ = "Integer32"
_Ieee8021QBridgeLearningConstraintsType_Object = MibTableColumn
ieee8021QBridgeLearningConstraintsType = _Ieee8021QBridgeLearningConstraintsType_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 8, 1, 4),
    _Ieee8021QBridgeLearningConstraintsType_Type()
)
ieee8021QBridgeLearningConstraintsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsType.setStatus("deprecated")
_Ieee8021QBridgeLearningConstraintsStatus_Type = RowStatus
_Ieee8021QBridgeLearningConstraintsStatus_Object = MibTableColumn
ieee8021QBridgeLearningConstraintsStatus = _Ieee8021QBridgeLearningConstraintsStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 8, 1, 5),
    _Ieee8021QBridgeLearningConstraintsStatus_Type()
)
ieee8021QBridgeLearningConstraintsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsStatus.setStatus("deprecated")
_Ieee8021QBridgeLearningConstraintDefaultsTable_Object = MibTable
ieee8021QBridgeLearningConstraintDefaultsTable = _Ieee8021QBridgeLearningConstraintDefaultsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 9)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintDefaultsTable.setStatus("deprecated")
_Ieee8021QBridgeLearningConstraintDefaultsEntry_Object = MibTableRow
ieee8021QBridgeLearningConstraintDefaultsEntry = _Ieee8021QBridgeLearningConstraintDefaultsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 9, 1)
)
ieee8021QBridgeLearningConstraintDefaultsEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintDefaultsComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintDefaultsEntry.setStatus("deprecated")
_Ieee8021QBridgeLearningConstraintDefaultsComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeLearningConstraintDefaultsComponentId_Object = MibTableColumn
ieee8021QBridgeLearningConstraintDefaultsComponentId = _Ieee8021QBridgeLearningConstraintDefaultsComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 9, 1, 1),
    _Ieee8021QBridgeLearningConstraintDefaultsComponentId_Type()
)
ieee8021QBridgeLearningConstraintDefaultsComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintDefaultsComponentId.setStatus("deprecated")


class _Ieee8021QBridgeLearningConstraintDefaultsSet_Type(Integer32):
    """Custom type ieee8021QBridgeLearningConstraintDefaultsSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021QBridgeLearningConstraintDefaultsSet_Type.__name__ = "Integer32"
_Ieee8021QBridgeLearningConstraintDefaultsSet_Object = MibTableColumn
ieee8021QBridgeLearningConstraintDefaultsSet = _Ieee8021QBridgeLearningConstraintDefaultsSet_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 9, 1, 2),
    _Ieee8021QBridgeLearningConstraintDefaultsSet_Type()
)
ieee8021QBridgeLearningConstraintDefaultsSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintDefaultsSet.setStatus("deprecated")


class _Ieee8021QBridgeLearningConstraintDefaultsType_Type(Integer32):
    """Custom type ieee8021QBridgeLearningConstraintDefaultsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("shared", 2))
    )


_Ieee8021QBridgeLearningConstraintDefaultsType_Type.__name__ = "Integer32"
_Ieee8021QBridgeLearningConstraintDefaultsType_Object = MibTableColumn
ieee8021QBridgeLearningConstraintDefaultsType = _Ieee8021QBridgeLearningConstraintDefaultsType_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 4, 9, 1, 3),
    _Ieee8021QBridgeLearningConstraintDefaultsType_Type()
)
ieee8021QBridgeLearningConstraintDefaultsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintDefaultsType.setStatus("deprecated")
_Ieee8021QBridgeProtocol_ObjectIdentity = ObjectIdentity
ieee8021QBridgeProtocol = _Ieee8021QBridgeProtocol_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5)
)
_Ieee8021QBridgeProtocolGroupTable_Object = MibTable
ieee8021QBridgeProtocolGroupTable = _Ieee8021QBridgeProtocolGroupTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolGroupTable.setStatus("current")
_Ieee8021QBridgeProtocolGroupEntry_Object = MibTableRow
ieee8021QBridgeProtocolGroupEntry = _Ieee8021QBridgeProtocolGroupEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 1, 1)
)
ieee8021QBridgeProtocolGroupEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolGroupComponentId"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolTemplateFrameType"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolTemplateProtocolValue"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolGroupEntry.setStatus("current")
_Ieee8021QBridgeProtocolGroupComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021QBridgeProtocolGroupComponentId_Object = MibTableColumn
ieee8021QBridgeProtocolGroupComponentId = _Ieee8021QBridgeProtocolGroupComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 1, 1, 1),
    _Ieee8021QBridgeProtocolGroupComponentId_Type()
)
ieee8021QBridgeProtocolGroupComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolGroupComponentId.setStatus("current")


class _Ieee8021QBridgeProtocolTemplateFrameType_Type(Integer32):
    """Custom type ieee8021QBridgeProtocolTemplateFrameType based on Integer32"""
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
        *(("ethernet", 1),
          ("llcOther", 5),
          ("rfc1042", 2),
          ("snap8021H", 3),
          ("snapOther", 4))
    )


_Ieee8021QBridgeProtocolTemplateFrameType_Type.__name__ = "Integer32"
_Ieee8021QBridgeProtocolTemplateFrameType_Object = MibTableColumn
ieee8021QBridgeProtocolTemplateFrameType = _Ieee8021QBridgeProtocolTemplateFrameType_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 1, 1, 2),
    _Ieee8021QBridgeProtocolTemplateFrameType_Type()
)
ieee8021QBridgeProtocolTemplateFrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolTemplateFrameType.setStatus("current")


class _Ieee8021QBridgeProtocolTemplateProtocolValue_Type(OctetString):
    """Custom type ieee8021QBridgeProtocolTemplateProtocolValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(5, 5),
    )


_Ieee8021QBridgeProtocolTemplateProtocolValue_Type.__name__ = "OctetString"
_Ieee8021QBridgeProtocolTemplateProtocolValue_Object = MibTableColumn
ieee8021QBridgeProtocolTemplateProtocolValue = _Ieee8021QBridgeProtocolTemplateProtocolValue_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 1, 1, 3),
    _Ieee8021QBridgeProtocolTemplateProtocolValue_Type()
)
ieee8021QBridgeProtocolTemplateProtocolValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolTemplateProtocolValue.setStatus("current")


class _Ieee8021QBridgeProtocolGroupId_Type(Integer32):
    """Custom type ieee8021QBridgeProtocolGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ieee8021QBridgeProtocolGroupId_Type.__name__ = "Integer32"
_Ieee8021QBridgeProtocolGroupId_Object = MibTableColumn
ieee8021QBridgeProtocolGroupId = _Ieee8021QBridgeProtocolGroupId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 1, 1, 4),
    _Ieee8021QBridgeProtocolGroupId_Type()
)
ieee8021QBridgeProtocolGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolGroupId.setStatus("current")
_Ieee8021QBridgeProtocolGroupRowStatus_Type = RowStatus
_Ieee8021QBridgeProtocolGroupRowStatus_Object = MibTableColumn
ieee8021QBridgeProtocolGroupRowStatus = _Ieee8021QBridgeProtocolGroupRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 1, 1, 5),
    _Ieee8021QBridgeProtocolGroupRowStatus_Type()
)
ieee8021QBridgeProtocolGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolGroupRowStatus.setStatus("current")
_Ieee8021QBridgeProtocolPortTable_Object = MibTable
ieee8021QBridgeProtocolPortTable = _Ieee8021QBridgeProtocolPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolPortTable.setStatus("current")
_Ieee8021QBridgeProtocolPortEntry_Object = MibTableRow
ieee8021QBridgeProtocolPortEntry = _Ieee8021QBridgeProtocolPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 2, 1)
)
ieee8021QBridgeProtocolPortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolPortGroupId"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolPortEntry.setStatus("current")


class _Ieee8021QBridgeProtocolPortGroupId_Type(Integer32):
    """Custom type ieee8021QBridgeProtocolPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ieee8021QBridgeProtocolPortGroupId_Type.__name__ = "Integer32"
_Ieee8021QBridgeProtocolPortGroupId_Object = MibTableColumn
ieee8021QBridgeProtocolPortGroupId = _Ieee8021QBridgeProtocolPortGroupId_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 2, 1, 1),
    _Ieee8021QBridgeProtocolPortGroupId_Type()
)
ieee8021QBridgeProtocolPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolPortGroupId.setStatus("current")
_Ieee8021QBridgeProtocolPortGroupVid_Type = VlanId
_Ieee8021QBridgeProtocolPortGroupVid_Object = MibTableColumn
ieee8021QBridgeProtocolPortGroupVid = _Ieee8021QBridgeProtocolPortGroupVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 2, 1, 2),
    _Ieee8021QBridgeProtocolPortGroupVid_Type()
)
ieee8021QBridgeProtocolPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolPortGroupVid.setStatus("current")
_Ieee8021QBridgeProtocolPortRowStatus_Type = RowStatus
_Ieee8021QBridgeProtocolPortRowStatus_Object = MibTableColumn
ieee8021QBridgeProtocolPortRowStatus = _Ieee8021QBridgeProtocolPortRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 5, 2, 1, 3),
    _Ieee8021QBridgeProtocolPortRowStatus_Type()
)
ieee8021QBridgeProtocolPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeProtocolPortRowStatus.setStatus("current")
_Ieee8021QBridgeVIDX_ObjectIdentity = ObjectIdentity
ieee8021QBridgeVIDX = _Ieee8021QBridgeVIDX_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6)
)
_Ieee8021QBridgeVIDXTable_Object = MibTable
ieee8021QBridgeVIDXTable = _Ieee8021QBridgeVIDXTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVIDXTable.setStatus("current")
_Ieee8021QBridgeVIDXEntry_Object = MibTableRow
ieee8021QBridgeVIDXEntry = _Ieee8021QBridgeVIDXEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 1, 1)
)
ieee8021QBridgeVIDXEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVIDXLocalVid"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVIDXEntry.setStatus("current")
_Ieee8021QBridgeVIDXLocalVid_Type = VlanId
_Ieee8021QBridgeVIDXLocalVid_Object = MibTableColumn
ieee8021QBridgeVIDXLocalVid = _Ieee8021QBridgeVIDXLocalVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 1, 1, 1),
    _Ieee8021QBridgeVIDXLocalVid_Type()
)
ieee8021QBridgeVIDXLocalVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeVIDXLocalVid.setStatus("current")
_Ieee8021QBridgeVIDXRelayVid_Type = VlanId
_Ieee8021QBridgeVIDXRelayVid_Object = MibTableColumn
ieee8021QBridgeVIDXRelayVid = _Ieee8021QBridgeVIDXRelayVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 1, 1, 2),
    _Ieee8021QBridgeVIDXRelayVid_Type()
)
ieee8021QBridgeVIDXRelayVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVIDXRelayVid.setStatus("current")
_Ieee8021QBridgeVIDXRowStatus_Type = RowStatus
_Ieee8021QBridgeVIDXRowStatus_Object = MibTableColumn
ieee8021QBridgeVIDXRowStatus = _Ieee8021QBridgeVIDXRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 1, 1, 3),
    _Ieee8021QBridgeVIDXRowStatus_Type()
)
ieee8021QBridgeVIDXRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeVIDXRowStatus.setStatus("current")
_Ieee8021QBridgeEgressVidXTable_Object = MibTable
ieee8021QBridgeEgressVidXTable = _Ieee8021QBridgeEgressVidXTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXTable.setStatus("deprecated")
_Ieee8021QBridgeEgressVidXEntry_Object = MibTableRow
ieee8021QBridgeEgressVidXEntry = _Ieee8021QBridgeEgressVidXEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 2, 1)
)
ieee8021QBridgeEgressVidXEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeEgressVidXRelayVid"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXEntry.setStatus("deprecated")
_Ieee8021QBridgeEgressVidXRelayVid_Type = VlanId
_Ieee8021QBridgeEgressVidXRelayVid_Object = MibTableColumn
ieee8021QBridgeEgressVidXRelayVid = _Ieee8021QBridgeEgressVidXRelayVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 2, 1, 1),
    _Ieee8021QBridgeEgressVidXRelayVid_Type()
)
ieee8021QBridgeEgressVidXRelayVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXRelayVid.setStatus("deprecated")
_Ieee8021QBridgeEgressVidXLocalVid_Type = VlanId
_Ieee8021QBridgeEgressVidXLocalVid_Object = MibTableColumn
ieee8021QBridgeEgressVidXLocalVid = _Ieee8021QBridgeEgressVidXLocalVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 2, 1, 2),
    _Ieee8021QBridgeEgressVidXLocalVid_Type()
)
ieee8021QBridgeEgressVidXLocalVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXLocalVid.setStatus("deprecated")
_Ieee8021QBridgeEgressVidXRowStatus_Type = RowStatus
_Ieee8021QBridgeEgressVidXRowStatus_Object = MibTableColumn
ieee8021QBridgeEgressVidXRowStatus = _Ieee8021QBridgeEgressVidXRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 2, 1, 3),
    _Ieee8021QBridgeEgressVidXRowStatus_Type()
)
ieee8021QBridgeEgressVidXRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXRowStatus.setStatus("deprecated")
_Ieee8021QBridgeEgressVidXV2Table_Object = MibTable
ieee8021QBridgeEgressVidXV2Table = _Ieee8021QBridgeEgressVidXV2Table_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXV2Table.setStatus("current")
_Ieee8021QBridgeEgressVidXV2Entry_Object = MibTableRow
ieee8021QBridgeEgressVidXV2Entry = _Ieee8021QBridgeEgressVidXV2Entry_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 3, 1)
)
ieee8021QBridgeEgressVidXV2Entry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeEgressVidXV2RelayVid"),
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXV2Entry.setStatus("current")
_Ieee8021QBridgeEgressVidXV2RelayVid_Type = VlanId
_Ieee8021QBridgeEgressVidXV2RelayVid_Object = MibTableColumn
ieee8021QBridgeEgressVidXV2RelayVid = _Ieee8021QBridgeEgressVidXV2RelayVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 3, 1, 1),
    _Ieee8021QBridgeEgressVidXV2RelayVid_Type()
)
ieee8021QBridgeEgressVidXV2RelayVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXV2RelayVid.setStatus("current")
_Ieee8021QBridgeEgressVidXV2LocalVid_Type = VlanId
_Ieee8021QBridgeEgressVidXV2LocalVid_Object = MibTableColumn
ieee8021QBridgeEgressVidXV2LocalVid = _Ieee8021QBridgeEgressVidXV2LocalVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 3, 1, 2),
    _Ieee8021QBridgeEgressVidXV2LocalVid_Type()
)
ieee8021QBridgeEgressVidXV2LocalVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXV2LocalVid.setStatus("current")
_Ieee8021QBridgeEgressVidXV2RowStatus_Type = RowStatus
_Ieee8021QBridgeEgressVidXV2RowStatus_Object = MibTableColumn
ieee8021QBridgeEgressVidXV2RowStatus = _Ieee8021QBridgeEgressVidXV2RowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 4, 1, 6, 3, 1, 3),
    _Ieee8021QBridgeEgressVidXV2RowStatus_Type()
)
ieee8021QBridgeEgressVidXV2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVidXV2RowStatus.setStatus("current")
_Ieee8021QBridgeConformance_ObjectIdentity = ObjectIdentity
ieee8021QBridgeConformance = _Ieee8021QBridgeConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 2)
)
_Ieee8021QBridgeGroups_ObjectIdentity = ObjectIdentity
ieee8021QBridgeGroups = _Ieee8021QBridgeGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1)
)
_Ieee8021QBridgeCompliances_ObjectIdentity = ObjectIdentity
ieee8021QBridgeCompliances = _Ieee8021QBridgeCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 2)
)
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("IEEE8021-Q-BRIDGE-MIB",
     "ieee8021QBridgePortVlanEntry")
)
ieee8021QBridgePortVlanEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())

# Managed Objects groups

ieee8021QBridgeBaseGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 1)
)
ieee8021QBridgeBaseGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanVersionNumber"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeMaxVlanId"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeMaxSupportedVlans"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeNumVlans"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeMvrpEnabledStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeBaseGroup.setStatus("current")

ieee8021QBridgeFdbUnicastGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 2)
)
ieee8021QBridgeFdbUnicastGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeFdbDynamicCount"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeFdbLearnedEntryDiscards"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeFdbAgingTime"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpFdbPort"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpFdbStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbUnicastGroup.setStatus("current")

ieee8021QBridgeFdbMulticastGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 3)
)
ieee8021QBridgeFdbMulticastGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpGroupEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpGroupLearnt"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbMulticastGroup.setStatus("current")

ieee8021QBridgeServiceRequirementsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 4)
)
ieee8021QBridgeServiceRequirementsGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardAllPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardAllStaticPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardAllForbiddenPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardUnregisteredPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardUnregisteredStaticPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeForwardUnregisteredForbiddenPorts"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeServiceRequirementsGroup.setStatus("current")

ieee8021QBridgeFdbStaticGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 5)
)
ieee8021QBridgeFdbStaticGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastStaticEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastForbiddenEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastStorageType"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticUnicastRowStatus"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticMulticastStaticEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticMulticastForbiddenEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticMulticastStorageType"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeStaticMulticastRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeFdbStaticGroup.setStatus("current")

ieee8021QBridgeVlanGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 6)
)
ieee8021QBridgeVlanGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanNumDeletes"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanFdbId"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentUntaggedPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanStatus"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCreationTime"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanGroup.setStatus("current")

ieee8021QBridgeVlanStaticGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 7)
)
ieee8021QBridgeVlanStaticGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanStaticName"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanStaticEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanForbiddenEgressPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanStaticUntaggedPorts"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanStaticRowStatus"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeNextFreeLocalVlanIndex"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStaticGroup.setStatus("current")

ieee8021QBridgeVlanStatisticsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 8)
)
ieee8021QBridgeVlanStatisticsGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpVlanPortInFrames"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpVlanPortOutFrames"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpVlanPortInDiscards"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVlanStatisticsGroup.setStatus("current")

ieee8021QBridgeLearningConstraintsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 9)
)
ieee8021QBridgeLearningConstraintsGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintsType"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintsStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintsGroup.setStatus("deprecated")

ieee8021QBridgeLearningConstraintDefaultGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 10)
)
ieee8021QBridgeLearningConstraintDefaultGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintDefaultsSet"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeLearningConstraintDefaultsType"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeLearningConstraintDefaultGroup.setStatus("deprecated")

ieee8021QBridgeClassificationDeviceGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 11)
)
ieee8021QBridgeClassificationDeviceGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolGroupId"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeClassificationDeviceGroup.setStatus("current")

ieee8021QBridgeClassificationPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 12)
)
ieee8021QBridgeClassificationPortGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolPortGroupVid"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeProtocolPortRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeClassificationPortGroup.setStatus("current")

ieee8021QBridgePortGroup2 = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 13)
)
ieee8021QBridgePortGroup2.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePvid"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePortAcceptableFrameTypes"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePortIngressFiltering"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePortMvrpEnabledStatus"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePortMvrpFailedRegistrations"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePortMvrpLastPduOrigin"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePortRestrictedVlanRegistration"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgePortGroup2.setStatus("current")

ieee8021QBridgeCVlanPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 14)
)
ieee8021QBridgeCVlanPortGroup.setObjects(
    ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeCVlanPortRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021QBridgeCVlanPortGroup.setStatus("current")

ieee8021QBridgeVIDXGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 15)
)
ieee8021QBridgeVIDXGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVIDXRelayVid"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVIDXRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeVIDXGroup.setStatus("current")

ieee8021QBridgeEgressVIDXGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 16)
)
ieee8021QBridgeEgressVIDXGroup.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeEgressVidXLocalVid"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeEgressVidXRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVIDXGroup.setStatus("deprecated")

ieee8021QBridgeEgressVIDXV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 1, 17)
)
ieee8021QBridgeEgressVIDXV2Group.setObjects(
      *(("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeEgressVidXV2LocalVid"),
        ("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeEgressVidXV2RowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021QBridgeEgressVIDXV2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021QBridgeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeCompliance.setStatus(
        "deprecated"
    )

ieee8021QBridgeComplianceV2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021QBridgeComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-Q-BRIDGE-MIB",
    **{"ieee8021QBridgeMib": ieee8021QBridgeMib,
       "ieee8021QBridgeMibObjects": ieee8021QBridgeMibObjects,
       "ieee8021QBridgeBase": ieee8021QBridgeBase,
       "ieee8021QBridgeTable": ieee8021QBridgeTable,
       "ieee8021QBridgeEntry": ieee8021QBridgeEntry,
       "ieee8021QBridgeComponentId": ieee8021QBridgeComponentId,
       "ieee8021QBridgeVlanVersionNumber": ieee8021QBridgeVlanVersionNumber,
       "ieee8021QBridgeMaxVlanId": ieee8021QBridgeMaxVlanId,
       "ieee8021QBridgeMaxSupportedVlans": ieee8021QBridgeMaxSupportedVlans,
       "ieee8021QBridgeNumVlans": ieee8021QBridgeNumVlans,
       "ieee8021QBridgeMvrpEnabledStatus": ieee8021QBridgeMvrpEnabledStatus,
       "ieee8021QBridgeCVlanPortTable": ieee8021QBridgeCVlanPortTable,
       "ieee8021QBridgeCVlanPortEntry": ieee8021QBridgeCVlanPortEntry,
       "ieee8021QBridgeCVlanPortComponentId": ieee8021QBridgeCVlanPortComponentId,
       "ieee8021QBridgeCVlanPortNumber": ieee8021QBridgeCVlanPortNumber,
       "ieee8021QBridgeCVlanPortRowStatus": ieee8021QBridgeCVlanPortRowStatus,
       "ieee8021QBridgeTp": ieee8021QBridgeTp,
       "ieee8021QBridgeFdbTable": ieee8021QBridgeFdbTable,
       "ieee8021QBridgeFdbEntry": ieee8021QBridgeFdbEntry,
       "ieee8021QBridgeFdbComponentId": ieee8021QBridgeFdbComponentId,
       "ieee8021QBridgeFdbId": ieee8021QBridgeFdbId,
       "ieee8021QBridgeFdbDynamicCount": ieee8021QBridgeFdbDynamicCount,
       "ieee8021QBridgeFdbLearnedEntryDiscards": ieee8021QBridgeFdbLearnedEntryDiscards,
       "ieee8021QBridgeFdbAgingTime": ieee8021QBridgeFdbAgingTime,
       "ieee8021QBridgeTpFdbTable": ieee8021QBridgeTpFdbTable,
       "ieee8021QBridgeTpFdbEntry": ieee8021QBridgeTpFdbEntry,
       "ieee8021QBridgeTpFdbAddress": ieee8021QBridgeTpFdbAddress,
       "ieee8021QBridgeTpFdbPort": ieee8021QBridgeTpFdbPort,
       "ieee8021QBridgeTpFdbStatus": ieee8021QBridgeTpFdbStatus,
       "ieee8021QBridgeTpGroupTable": ieee8021QBridgeTpGroupTable,
       "ieee8021QBridgeTpGroupEntry": ieee8021QBridgeTpGroupEntry,
       "ieee8021QBridgeTpGroupAddress": ieee8021QBridgeTpGroupAddress,
       "ieee8021QBridgeTpGroupEgressPorts": ieee8021QBridgeTpGroupEgressPorts,
       "ieee8021QBridgeTpGroupLearnt": ieee8021QBridgeTpGroupLearnt,
       "ieee8021QBridgeForwardAllTable": ieee8021QBridgeForwardAllTable,
       "ieee8021QBridgeForwardAllEntry": ieee8021QBridgeForwardAllEntry,
       "ieee8021QBridgeForwardAllVlanIndex": ieee8021QBridgeForwardAllVlanIndex,
       "ieee8021QBridgeForwardAllPorts": ieee8021QBridgeForwardAllPorts,
       "ieee8021QBridgeForwardAllStaticPorts": ieee8021QBridgeForwardAllStaticPorts,
       "ieee8021QBridgeForwardAllForbiddenPorts": ieee8021QBridgeForwardAllForbiddenPorts,
       "ieee8021QBridgeForwardUnregisteredTable": ieee8021QBridgeForwardUnregisteredTable,
       "ieee8021QBridgeForwardUnregisteredEntry": ieee8021QBridgeForwardUnregisteredEntry,
       "ieee8021QBridgeForwardUnregisteredVlanIndex": ieee8021QBridgeForwardUnregisteredVlanIndex,
       "ieee8021QBridgeForwardUnregisteredPorts": ieee8021QBridgeForwardUnregisteredPorts,
       "ieee8021QBridgeForwardUnregisteredStaticPorts": ieee8021QBridgeForwardUnregisteredStaticPorts,
       "ieee8021QBridgeForwardUnregisteredForbiddenPorts": ieee8021QBridgeForwardUnregisteredForbiddenPorts,
       "ieee8021QBridgeStatic": ieee8021QBridgeStatic,
       "ieee8021QBridgeStaticUnicastTable": ieee8021QBridgeStaticUnicastTable,
       "ieee8021QBridgeStaticUnicastEntry": ieee8021QBridgeStaticUnicastEntry,
       "ieee8021QBridgeStaticUnicastComponentId": ieee8021QBridgeStaticUnicastComponentId,
       "ieee8021QBridgeStaticUnicastVlanIndex": ieee8021QBridgeStaticUnicastVlanIndex,
       "ieee8021QBridgeStaticUnicastAddress": ieee8021QBridgeStaticUnicastAddress,
       "ieee8021QBridgeStaticUnicastReceivePort": ieee8021QBridgeStaticUnicastReceivePort,
       "ieee8021QBridgeStaticUnicastStaticEgressPorts": ieee8021QBridgeStaticUnicastStaticEgressPorts,
       "ieee8021QBridgeStaticUnicastForbiddenEgressPorts": ieee8021QBridgeStaticUnicastForbiddenEgressPorts,
       "ieee8021QBridgeStaticUnicastStorageType": ieee8021QBridgeStaticUnicastStorageType,
       "ieee8021QBridgeStaticUnicastRowStatus": ieee8021QBridgeStaticUnicastRowStatus,
       "ieee8021QBridgeStaticMulticastTable": ieee8021QBridgeStaticMulticastTable,
       "ieee8021QBridgeStaticMulticastEntry": ieee8021QBridgeStaticMulticastEntry,
       "ieee8021QBridgeStaticMulticastAddress": ieee8021QBridgeStaticMulticastAddress,
       "ieee8021QBridgeStaticMulticastReceivePort": ieee8021QBridgeStaticMulticastReceivePort,
       "ieee8021QBridgeStaticMulticastStaticEgressPorts": ieee8021QBridgeStaticMulticastStaticEgressPorts,
       "ieee8021QBridgeStaticMulticastForbiddenEgressPorts": ieee8021QBridgeStaticMulticastForbiddenEgressPorts,
       "ieee8021QBridgeStaticMulticastStorageType": ieee8021QBridgeStaticMulticastStorageType,
       "ieee8021QBridgeStaticMulticastRowStatus": ieee8021QBridgeStaticMulticastRowStatus,
       "ieee8021QBridgeVlan": ieee8021QBridgeVlan,
       "ieee8021QBridgeVlanNumDeletes": ieee8021QBridgeVlanNumDeletes,
       "ieee8021QBridgeVlanCurrentTable": ieee8021QBridgeVlanCurrentTable,
       "ieee8021QBridgeVlanCurrentEntry": ieee8021QBridgeVlanCurrentEntry,
       "ieee8021QBridgeVlanTimeMark": ieee8021QBridgeVlanTimeMark,
       "ieee8021QBridgeVlanCurrentComponentId": ieee8021QBridgeVlanCurrentComponentId,
       "ieee8021QBridgeVlanIndex": ieee8021QBridgeVlanIndex,
       "ieee8021QBridgeVlanFdbId": ieee8021QBridgeVlanFdbId,
       "ieee8021QBridgeVlanCurrentEgressPorts": ieee8021QBridgeVlanCurrentEgressPorts,
       "ieee8021QBridgeVlanCurrentUntaggedPorts": ieee8021QBridgeVlanCurrentUntaggedPorts,
       "ieee8021QBridgeVlanStatus": ieee8021QBridgeVlanStatus,
       "ieee8021QBridgeVlanCreationTime": ieee8021QBridgeVlanCreationTime,
       "ieee8021QBridgeVlanStaticTable": ieee8021QBridgeVlanStaticTable,
       "ieee8021QBridgeVlanStaticEntry": ieee8021QBridgeVlanStaticEntry,
       "ieee8021QBridgeVlanStaticComponentId": ieee8021QBridgeVlanStaticComponentId,
       "ieee8021QBridgeVlanStaticVlanIndex": ieee8021QBridgeVlanStaticVlanIndex,
       "ieee8021QBridgeVlanStaticName": ieee8021QBridgeVlanStaticName,
       "ieee8021QBridgeVlanStaticEgressPorts": ieee8021QBridgeVlanStaticEgressPorts,
       "ieee8021QBridgeVlanForbiddenEgressPorts": ieee8021QBridgeVlanForbiddenEgressPorts,
       "ieee8021QBridgeVlanStaticUntaggedPorts": ieee8021QBridgeVlanStaticUntaggedPorts,
       "ieee8021QBridgeVlanStaticRowStatus": ieee8021QBridgeVlanStaticRowStatus,
       "ieee8021QBridgeNextFreeLocalVlanTable": ieee8021QBridgeNextFreeLocalVlanTable,
       "ieee8021QBridgeNextFreeLocalVlanEntry": ieee8021QBridgeNextFreeLocalVlanEntry,
       "ieee8021QBridgeNextFreeLocalVlanComponentId": ieee8021QBridgeNextFreeLocalVlanComponentId,
       "ieee8021QBridgeNextFreeLocalVlanIndex": ieee8021QBridgeNextFreeLocalVlanIndex,
       "ieee8021QBridgePortVlanTable": ieee8021QBridgePortVlanTable,
       "ieee8021QBridgePortVlanEntry": ieee8021QBridgePortVlanEntry,
       "ieee8021QBridgePvid": ieee8021QBridgePvid,
       "ieee8021QBridgePortAcceptableFrameTypes": ieee8021QBridgePortAcceptableFrameTypes,
       "ieee8021QBridgePortIngressFiltering": ieee8021QBridgePortIngressFiltering,
       "ieee8021QBridgePortMvrpEnabledStatus": ieee8021QBridgePortMvrpEnabledStatus,
       "ieee8021QBridgePortMvrpFailedRegistrations": ieee8021QBridgePortMvrpFailedRegistrations,
       "ieee8021QBridgePortMvrpLastPduOrigin": ieee8021QBridgePortMvrpLastPduOrigin,
       "ieee8021QBridgePortRestrictedVlanRegistration": ieee8021QBridgePortRestrictedVlanRegistration,
       "ieee8021QBridgePortVlanStatisticsTable": ieee8021QBridgePortVlanStatisticsTable,
       "ieee8021QBridgePortVlanStatisticsEntry": ieee8021QBridgePortVlanStatisticsEntry,
       "ieee8021QBridgeTpVlanPortInFrames": ieee8021QBridgeTpVlanPortInFrames,
       "ieee8021QBridgeTpVlanPortOutFrames": ieee8021QBridgeTpVlanPortOutFrames,
       "ieee8021QBridgeTpVlanPortInDiscards": ieee8021QBridgeTpVlanPortInDiscards,
       "ieee8021QBridgeLearningConstraintsTable": ieee8021QBridgeLearningConstraintsTable,
       "ieee8021QBridgeLearningConstraintsEntry": ieee8021QBridgeLearningConstraintsEntry,
       "ieee8021QBridgeLearningConstraintsComponentId": ieee8021QBridgeLearningConstraintsComponentId,
       "ieee8021QBridgeLearningConstraintsVlan": ieee8021QBridgeLearningConstraintsVlan,
       "ieee8021QBridgeLearningConstraintsSet": ieee8021QBridgeLearningConstraintsSet,
       "ieee8021QBridgeLearningConstraintsType": ieee8021QBridgeLearningConstraintsType,
       "ieee8021QBridgeLearningConstraintsStatus": ieee8021QBridgeLearningConstraintsStatus,
       "ieee8021QBridgeLearningConstraintDefaultsTable": ieee8021QBridgeLearningConstraintDefaultsTable,
       "ieee8021QBridgeLearningConstraintDefaultsEntry": ieee8021QBridgeLearningConstraintDefaultsEntry,
       "ieee8021QBridgeLearningConstraintDefaultsComponentId": ieee8021QBridgeLearningConstraintDefaultsComponentId,
       "ieee8021QBridgeLearningConstraintDefaultsSet": ieee8021QBridgeLearningConstraintDefaultsSet,
       "ieee8021QBridgeLearningConstraintDefaultsType": ieee8021QBridgeLearningConstraintDefaultsType,
       "ieee8021QBridgeProtocol": ieee8021QBridgeProtocol,
       "ieee8021QBridgeProtocolGroupTable": ieee8021QBridgeProtocolGroupTable,
       "ieee8021QBridgeProtocolGroupEntry": ieee8021QBridgeProtocolGroupEntry,
       "ieee8021QBridgeProtocolGroupComponentId": ieee8021QBridgeProtocolGroupComponentId,
       "ieee8021QBridgeProtocolTemplateFrameType": ieee8021QBridgeProtocolTemplateFrameType,
       "ieee8021QBridgeProtocolTemplateProtocolValue": ieee8021QBridgeProtocolTemplateProtocolValue,
       "ieee8021QBridgeProtocolGroupId": ieee8021QBridgeProtocolGroupId,
       "ieee8021QBridgeProtocolGroupRowStatus": ieee8021QBridgeProtocolGroupRowStatus,
       "ieee8021QBridgeProtocolPortTable": ieee8021QBridgeProtocolPortTable,
       "ieee8021QBridgeProtocolPortEntry": ieee8021QBridgeProtocolPortEntry,
       "ieee8021QBridgeProtocolPortGroupId": ieee8021QBridgeProtocolPortGroupId,
       "ieee8021QBridgeProtocolPortGroupVid": ieee8021QBridgeProtocolPortGroupVid,
       "ieee8021QBridgeProtocolPortRowStatus": ieee8021QBridgeProtocolPortRowStatus,
       "ieee8021QBridgeVIDX": ieee8021QBridgeVIDX,
       "ieee8021QBridgeVIDXTable": ieee8021QBridgeVIDXTable,
       "ieee8021QBridgeVIDXEntry": ieee8021QBridgeVIDXEntry,
       "ieee8021QBridgeVIDXLocalVid": ieee8021QBridgeVIDXLocalVid,
       "ieee8021QBridgeVIDXRelayVid": ieee8021QBridgeVIDXRelayVid,
       "ieee8021QBridgeVIDXRowStatus": ieee8021QBridgeVIDXRowStatus,
       "ieee8021QBridgeEgressVidXTable": ieee8021QBridgeEgressVidXTable,
       "ieee8021QBridgeEgressVidXEntry": ieee8021QBridgeEgressVidXEntry,
       "ieee8021QBridgeEgressVidXRelayVid": ieee8021QBridgeEgressVidXRelayVid,
       "ieee8021QBridgeEgressVidXLocalVid": ieee8021QBridgeEgressVidXLocalVid,
       "ieee8021QBridgeEgressVidXRowStatus": ieee8021QBridgeEgressVidXRowStatus,
       "ieee8021QBridgeEgressVidXV2Table": ieee8021QBridgeEgressVidXV2Table,
       "ieee8021QBridgeEgressVidXV2Entry": ieee8021QBridgeEgressVidXV2Entry,
       "ieee8021QBridgeEgressVidXV2RelayVid": ieee8021QBridgeEgressVidXV2RelayVid,
       "ieee8021QBridgeEgressVidXV2LocalVid": ieee8021QBridgeEgressVidXV2LocalVid,
       "ieee8021QBridgeEgressVidXV2RowStatus": ieee8021QBridgeEgressVidXV2RowStatus,
       "ieee8021QBridgeConformance": ieee8021QBridgeConformance,
       "ieee8021QBridgeGroups": ieee8021QBridgeGroups,
       "ieee8021QBridgeBaseGroup": ieee8021QBridgeBaseGroup,
       "ieee8021QBridgeFdbUnicastGroup": ieee8021QBridgeFdbUnicastGroup,
       "ieee8021QBridgeFdbMulticastGroup": ieee8021QBridgeFdbMulticastGroup,
       "ieee8021QBridgeServiceRequirementsGroup": ieee8021QBridgeServiceRequirementsGroup,
       "ieee8021QBridgeFdbStaticGroup": ieee8021QBridgeFdbStaticGroup,
       "ieee8021QBridgeVlanGroup": ieee8021QBridgeVlanGroup,
       "ieee8021QBridgeVlanStaticGroup": ieee8021QBridgeVlanStaticGroup,
       "ieee8021QBridgeVlanStatisticsGroup": ieee8021QBridgeVlanStatisticsGroup,
       "ieee8021QBridgeLearningConstraintsGroup": ieee8021QBridgeLearningConstraintsGroup,
       "ieee8021QBridgeLearningConstraintDefaultGroup": ieee8021QBridgeLearningConstraintDefaultGroup,
       "ieee8021QBridgeClassificationDeviceGroup": ieee8021QBridgeClassificationDeviceGroup,
       "ieee8021QBridgeClassificationPortGroup": ieee8021QBridgeClassificationPortGroup,
       "ieee8021QBridgePortGroup2": ieee8021QBridgePortGroup2,
       "ieee8021QBridgeCVlanPortGroup": ieee8021QBridgeCVlanPortGroup,
       "ieee8021QBridgeVIDXGroup": ieee8021QBridgeVIDXGroup,
       "ieee8021QBridgeEgressVIDXGroup": ieee8021QBridgeEgressVIDXGroup,
       "ieee8021QBridgeEgressVIDXV2Group": ieee8021QBridgeEgressVIDXV2Group,
       "ieee8021QBridgeCompliances": ieee8021QBridgeCompliances,
       "ieee8021QBridgeCompliance": ieee8021QBridgeCompliance,
       "ieee8021QBridgeComplianceV2": ieee8021QBridgeComplianceV2}
)
