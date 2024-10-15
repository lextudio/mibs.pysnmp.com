# SNMP MIB module (HUAWEI-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-QINQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:41 2024
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

(VlanList,) = mibBuilder.importSymbols(
    "HUAWEI-L2IF-MIB",
    "VlanList")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwQinQ = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BpduIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("cdp", 50),
          ("gmrp", 33),
          ("gvrp", 34),
          ("hgmp", 11),
          ("isisLevel01", 21),
          ("isisLevel02", 22),
          ("lacp", 49),
          ("pagp", 51),
          ("pauseFrame", 2),
          ("reserved02", 3),
          ("reserved03", 4),
          ("reserved04", 5),
          ("reserved05", 6),
          ("reserved06", 7),
          ("reserved07", 8),
          ("reserved08", 10),
          ("reserved09", 12),
          ("reserved10", 13),
          ("reserved11", 14),
          ("reserved12", 15),
          ("reserved13", 16),
          ("reserved14", 17),
          ("reserved15", 18),
          ("reserved16", 19),
          ("reserved17", 20),
          ("reserved18", 23),
          ("reserved19", 24),
          ("reserved20", 25),
          ("reserved21", 26),
          ("reserved22", 27),
          ("reserved23", 28),
          ("reserved24", 29),
          ("reserved25", 30),
          ("reserved26", 31),
          ("reserved27", 32),
          ("reserved28", 35),
          ("reserved29", 36),
          ("reserved30", 37),
          ("reserved31", 38),
          ("reserved32", 39),
          ("reserved33", 40),
          ("reserved34", 41),
          ("reserved35", 42),
          ("reserved36", 43),
          ("reserved37", 44),
          ("reserved38", 45),
          ("reserved39", 46),
          ("reserved40", 47),
          ("reserved41", 48),
          ("stp01", 1),
          ("stp02", 9),
          ("udld", 52),
          ("vtp", 53))
    )



# MIB Managed Objects in the order of their OIDs

_HwQinQSystemBase_ObjectIdentity = ObjectIdentity
hwQinQSystemBase = _HwQinQSystemBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 1)
)
_HwQinQSystemWellKnowMac_Type = MacAddress
_HwQinQSystemWellKnowMac_Object = MibScalar
hwQinQSystemWellKnowMac = _HwQinQSystemWellKnowMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 1, 1),
    _HwQinQSystemWellKnowMac_Type()
)
hwQinQSystemWellKnowMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQSystemWellKnowMac.setStatus("current")


class _HwQinQSystemBridgeRole_Type(Integer32):
    """Custom type hwQinQSystemBridgeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customer", 1),
          ("provider", 2))
    )


_HwQinQSystemBridgeRole_Type.__name__ = "Integer32"
_HwQinQSystemBridgeRole_Object = MibScalar
hwQinQSystemBridgeRole = _HwQinQSystemBridgeRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 1, 2),
    _HwQinQSystemBridgeRole_Type()
)
hwQinQSystemBridgeRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQSystemBridgeRole.setStatus("current")


class _HwBpduSystemDropPacketSta_Type(Integer32):
    """Custom type hwBpduSystemDropPacketSta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwBpduSystemDropPacketSta_Type.__name__ = "Integer32"
_HwBpduSystemDropPacketSta_Object = MibScalar
hwBpduSystemDropPacketSta = _HwBpduSystemDropPacketSta_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 1, 3),
    _HwBpduSystemDropPacketSta_Type()
)
hwBpduSystemDropPacketSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBpduSystemDropPacketSta.setStatus("current")


class _HwQinQSystemEtherType_Type(Unsigned32):
    """Custom type hwQinQSystemEtherType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwQinQSystemEtherType_Type.__name__ = "Unsigned32"
_HwQinQSystemEtherType_Object = MibScalar
hwQinQSystemEtherType = _HwQinQSystemEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 1, 4),
    _HwQinQSystemEtherType_Type()
)
hwQinQSystemEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQSystemEtherType.setStatus("current")
_HwQinQMngObjects_ObjectIdentity = ObjectIdentity
hwQinQMngObjects = _HwQinQMngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2)
)
_HwQinQBpduTunnelTable_Object = MibTable
hwQinQBpduTunnelTable = _HwQinQBpduTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1)
)
if mibBuilder.loadTexts:
    hwQinQBpduTunnelTable.setStatus("current")
_HwQinQBpduTunnelEntry_Object = MibTableRow
hwQinQBpduTunnelEntry = _HwQinQBpduTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1)
)
hwQinQBpduTunnelEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQBpduTunnelIndex"),
)
if mibBuilder.loadTexts:
    hwQinQBpduTunnelEntry.setStatus("current")
_HwQinQBpduTunnelIndex_Type = Integer32
_HwQinQBpduTunnelIndex_Object = MibTableColumn
hwQinQBpduTunnelIndex = _HwQinQBpduTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 1),
    _HwQinQBpduTunnelIndex_Type()
)
hwQinQBpduTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelIndex.setStatus("current")


class _HwQinQEtherEncpsType_Type(OctetString):
    """Custom type hwQinQEtherEncpsType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwQinQEtherEncpsType_Type.__name__ = "OctetString"
_HwQinQEtherEncpsType_Object = MibTableColumn
hwQinQEtherEncpsType = _HwQinQEtherEncpsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 2),
    _HwQinQEtherEncpsType_Type()
)
hwQinQEtherEncpsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQEtherEncpsType.setStatus("current")


class _HwQinQBpduTunnelEnableOneQBpduTunnel_Type(EnabledStatus):
    """Custom type hwQinQBpduTunnelEnableOneQBpduTunnel based on EnabledStatus"""


_HwQinQBpduTunnelEnableOneQBpduTunnel_Object = MibTableColumn
hwQinQBpduTunnelEnableOneQBpduTunnel = _HwQinQBpduTunnelEnableOneQBpduTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 3),
    _HwQinQBpduTunnelEnableOneQBpduTunnel_Type()
)
hwQinQBpduTunnelEnableOneQBpduTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelEnableOneQBpduTunnel.setStatus("current")
_HwQinQBpduTunnelEnableBpduTag_Type = EnabledStatus
_HwQinQBpduTunnelEnableBpduTag_Object = MibTableColumn
hwQinQBpduTunnelEnableBpduTag = _HwQinQBpduTunnelEnableBpduTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 4),
    _HwQinQBpduTunnelEnableBpduTag_Type()
)
hwQinQBpduTunnelEnableBpduTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelEnableBpduTag.setStatus("current")
_HwQinQBpduTunnelEnableTwoQBpduTunnel_Type = EnabledStatus
_HwQinQBpduTunnelEnableTwoQBpduTunnel_Object = MibTableColumn
hwQinQBpduTunnelEnableTwoQBpduTunnel = _HwQinQBpduTunnelEnableTwoQBpduTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 5),
    _HwQinQBpduTunnelEnableTwoQBpduTunnel_Type()
)
hwQinQBpduTunnelEnableTwoQBpduTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelEnableTwoQBpduTunnel.setStatus("current")


class _HwQinQBpduTunnelCustomerBpduTag_Type(Integer32):
    """Custom type hwQinQBpduTunnelCustomerBpduTag based on Integer32"""
    defaultValue = 0


_HwQinQBpduTunnelCustomerBpduTag_Object = MibTableColumn
hwQinQBpduTunnelCustomerBpduTag = _HwQinQBpduTunnelCustomerBpduTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 6),
    _HwQinQBpduTunnelCustomerBpduTag_Type()
)
hwQinQBpduTunnelCustomerBpduTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelCustomerBpduTag.setStatus("current")


class _HwQinQBpduTunnelCustomerBpduTagListLow_Type(OctetString):
    """Custom type hwQinQBpduTunnelCustomerBpduTagListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwQinQBpduTunnelCustomerBpduTagListLow_Type.__name__ = "OctetString"
_HwQinQBpduTunnelCustomerBpduTagListLow_Object = MibTableColumn
hwQinQBpduTunnelCustomerBpduTagListLow = _HwQinQBpduTunnelCustomerBpduTagListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 7),
    _HwQinQBpduTunnelCustomerBpduTagListLow_Type()
)
hwQinQBpduTunnelCustomerBpduTagListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelCustomerBpduTagListLow.setStatus("current")


class _HwQinQBpduTunnelCustomerBpduTagListHigh_Type(OctetString):
    """Custom type hwQinQBpduTunnelCustomerBpduTagListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwQinQBpduTunnelCustomerBpduTagListHigh_Type.__name__ = "OctetString"
_HwQinQBpduTunnelCustomerBpduTagListHigh_Object = MibTableColumn
hwQinQBpduTunnelCustomerBpduTagListHigh = _HwQinQBpduTunnelCustomerBpduTagListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 8),
    _HwQinQBpduTunnelCustomerBpduTagListHigh_Type()
)
hwQinQBpduTunnelCustomerBpduTagListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelCustomerBpduTagListHigh.setStatus("current")


class _HwQinQRemarkOuterTpid_Type(Integer32):
    """Custom type hwQinQRemarkOuterTpid based on Integer32"""
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
        *(("hex8100", 4),
          ("hex88a8", 2),
          ("hex9100", 3),
          ("hexffff", 1))
    )


_HwQinQRemarkOuterTpid_Type.__name__ = "Integer32"
_HwQinQRemarkOuterTpid_Object = MibTableColumn
hwQinQRemarkOuterTpid = _HwQinQRemarkOuterTpid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 9),
    _HwQinQRemarkOuterTpid_Type()
)
hwQinQRemarkOuterTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQRemarkOuterTpid.setStatus("current")


class _HwQinQBpduTunnelEnableBpduFilter_Type(EnabledStatus):
    """Custom type hwQinQBpduTunnelEnableBpduFilter based on EnabledStatus"""


_HwQinQBpduTunnelEnableBpduFilter_Object = MibTableColumn
hwQinQBpduTunnelEnableBpduFilter = _HwQinQBpduTunnelEnableBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 1, 1, 10),
    _HwQinQBpduTunnelEnableBpduFilter_Type()
)
hwQinQBpduTunnelEnableBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQBpduTunnelEnableBpduFilter.setStatus("current")
_HwQinQSubIfVlanStackingTable_Object = MibTable
hwQinQSubIfVlanStackingTable = _HwQinQSubIfVlanStackingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2)
)
if mibBuilder.loadTexts:
    hwQinQSubIfVlanStackingTable.setStatus("current")
_HwQinQSubIfVlanStackingEntry_Object = MibTableRow
hwQinQSubIfVlanStackingEntry = _HwQinQSubIfVlanStackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2, 1)
)
hwQinQSubIfVlanStackingEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfStackingIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfStackingCEVlanStart"),
)
if mibBuilder.loadTexts:
    hwQinQSubIfVlanStackingEntry.setStatus("current")
_HwQinQSubIfStackingIfIndex_Type = InterfaceIndex
_HwQinQSubIfStackingIfIndex_Object = MibTableColumn
hwQinQSubIfStackingIfIndex = _HwQinQSubIfStackingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2, 1, 1),
    _HwQinQSubIfStackingIfIndex_Type()
)
hwQinQSubIfStackingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingIfIndex.setStatus("current")
_HwQinQSubIfStackingCEVlanStart_Type = VlanId
_HwQinQSubIfStackingCEVlanStart_Object = MibTableColumn
hwQinQSubIfStackingCEVlanStart = _HwQinQSubIfStackingCEVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2, 1, 2),
    _HwQinQSubIfStackingCEVlanStart_Type()
)
hwQinQSubIfStackingCEVlanStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingCEVlanStart.setStatus("current")
_HwQinQSubIfStackingCEVlanEnd_Type = VlanId
_HwQinQSubIfStackingCEVlanEnd_Object = MibTableColumn
hwQinQSubIfStackingCEVlanEnd = _HwQinQSubIfStackingCEVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2, 1, 3),
    _HwQinQSubIfStackingCEVlanEnd_Type()
)
hwQinQSubIfStackingCEVlanEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingCEVlanEnd.setStatus("current")


class _HwQinQSubIfStackGroupId_Type(Integer32):
    """Custom type hwQinQSubIfStackGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwQinQSubIfStackGroupId_Type.__name__ = "Integer32"
_HwQinQSubIfStackGroupId_Object = MibTableColumn
hwQinQSubIfStackGroupId = _HwQinQSubIfStackGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2, 1, 4),
    _HwQinQSubIfStackGroupId_Type()
)
hwQinQSubIfStackGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfStackGroupId.setStatus("current")
_HwQinQSubIfStackingRowStatus_Type = RowStatus
_HwQinQSubIfStackingRowStatus_Object = MibTableColumn
hwQinQSubIfStackingRowStatus = _HwQinQSubIfStackingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2, 1, 5),
    _HwQinQSubIfStackingRowStatus_Type()
)
hwQinQSubIfStackingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingRowStatus.setStatus("current")


class _HwQinQSubIfStackingPEVlan_Type(Integer32):
    """Custom type hwQinQSubIfStackingPEVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwQinQSubIfStackingPEVlan_Type.__name__ = "Integer32"
_HwQinQSubIfStackingPEVlan_Object = MibTableColumn
hwQinQSubIfStackingPEVlan = _HwQinQSubIfStackingPEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 2, 1, 6),
    _HwQinQSubIfStackingPEVlan_Type()
)
hwQinQSubIfStackingPEVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingPEVlan.setStatus("current")
_HwQinQSubIfStackingStatTable_Object = MibTable
hwQinQSubIfStackingStatTable = _HwQinQSubIfStackingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3)
)
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatTable.setStatus("current")
_HwQinQSubIfStackingStatEntry_Object = MibTableRow
hwQinQSubIfStackingStatEntry = _HwQinQSubIfStackingStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1)
)
hwQinQSubIfStackingStatEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfStackingStatIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfStackingStatCEVlan"),
)
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatEntry.setStatus("current")
_HwQinQSubIfStackingStatIfIndex_Type = InterfaceIndex
_HwQinQSubIfStackingStatIfIndex_Object = MibTableColumn
hwQinQSubIfStackingStatIfIndex = _HwQinQSubIfStackingStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 1),
    _HwQinQSubIfStackingStatIfIndex_Type()
)
hwQinQSubIfStackingStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatIfIndex.setStatus("current")
_HwQinQSubIfStackingStatCEVlan_Type = VlanId
_HwQinQSubIfStackingStatCEVlan_Object = MibTableColumn
hwQinQSubIfStackingStatCEVlan = _HwQinQSubIfStackingStatCEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 2),
    _HwQinQSubIfStackingStatCEVlan_Type()
)
hwQinQSubIfStackingStatCEVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatCEVlan.setStatus("current")


class _HwQinQSubIfStackStatGroupId_Type(Integer32):
    """Custom type hwQinQSubIfStackStatGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwQinQSubIfStackStatGroupId_Type.__name__ = "Integer32"
_HwQinQSubIfStackStatGroupId_Object = MibTableColumn
hwQinQSubIfStackStatGroupId = _HwQinQSubIfStackStatGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 3),
    _HwQinQSubIfStackStatGroupId_Type()
)
hwQinQSubIfStackStatGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackStatGroupId.setStatus("current")
_HwQinQSubIfStackingStatOutPackets_Type = Counter64
_HwQinQSubIfStackingStatOutPackets_Object = MibTableColumn
hwQinQSubIfStackingStatOutPackets = _HwQinQSubIfStackingStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 4),
    _HwQinQSubIfStackingStatOutPackets_Type()
)
hwQinQSubIfStackingStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatOutPackets.setStatus("current")
_HwQinQSubIfStackingStatOutBytes_Type = Counter64
_HwQinQSubIfStackingStatOutBytes_Object = MibTableColumn
hwQinQSubIfStackingStatOutBytes = _HwQinQSubIfStackingStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 5),
    _HwQinQSubIfStackingStatOutBytes_Type()
)
hwQinQSubIfStackingStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatOutBytes.setStatus("current")
_HwQinQSubIfStackingStatInPackets_Type = Counter64
_HwQinQSubIfStackingStatInPackets_Object = MibTableColumn
hwQinQSubIfStackingStatInPackets = _HwQinQSubIfStackingStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 6),
    _HwQinQSubIfStackingStatInPackets_Type()
)
hwQinQSubIfStackingStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatInPackets.setStatus("current")
_HwQinQSubIfStackingStatInBytes_Type = Counter64
_HwQinQSubIfStackingStatInBytes_Object = MibTableColumn
hwQinQSubIfStackingStatInBytes = _HwQinQSubIfStackingStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 7),
    _HwQinQSubIfStackingStatInBytes_Type()
)
hwQinQSubIfStackingStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatInBytes.setStatus("current")
_HwQinQSubIfStackStatOutBdPackets_Type = Counter64
_HwQinQSubIfStackStatOutBdPackets_Object = MibTableColumn
hwQinQSubIfStackStatOutBdPackets = _HwQinQSubIfStackStatOutBdPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 8),
    _HwQinQSubIfStackStatOutBdPackets_Type()
)
hwQinQSubIfStackStatOutBdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackStatOutBdPackets.setStatus("current")
_HwQinQSubIfStackStatInBdPackets_Type = Counter64
_HwQinQSubIfStackStatInBdPackets_Object = MibTableColumn
hwQinQSubIfStackStatInBdPackets = _HwQinQSubIfStackStatInBdPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 9),
    _HwQinQSubIfStackStatInBdPackets_Type()
)
hwQinQSubIfStackStatInBdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackStatInBdPackets.setStatus("current")
_HwQinQSubIfStackStatOutMuPackets_Type = Counter64
_HwQinQSubIfStackStatOutMuPackets_Object = MibTableColumn
hwQinQSubIfStackStatOutMuPackets = _HwQinQSubIfStackStatOutMuPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 10),
    _HwQinQSubIfStackStatOutMuPackets_Type()
)
hwQinQSubIfStackStatOutMuPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackStatOutMuPackets.setStatus("current")
_HwQinQSubIfStackStatInMuPackets_Type = Counter64
_HwQinQSubIfStackStatInMuPackets_Object = MibTableColumn
hwQinQSubIfStackStatInMuPackets = _HwQinQSubIfStackStatInMuPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 11),
    _HwQinQSubIfStackStatInMuPackets_Type()
)
hwQinQSubIfStackStatInMuPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackStatInMuPackets.setStatus("current")
_HwQinQSubIfStackStatOutUniPackets_Type = Counter64
_HwQinQSubIfStackStatOutUniPackets_Object = MibTableColumn
hwQinQSubIfStackStatOutUniPackets = _HwQinQSubIfStackStatOutUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 12),
    _HwQinQSubIfStackStatOutUniPackets_Type()
)
hwQinQSubIfStackStatOutUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackStatOutUniPackets.setStatus("current")
_HwQinQSubIfStackStatInUniPackets_Type = Counter64
_HwQinQSubIfStackStatInUniPackets_Object = MibTableColumn
hwQinQSubIfStackStatInUniPackets = _HwQinQSubIfStackStatInUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 3, 1, 13),
    _HwQinQSubIfStackStatInUniPackets_Type()
)
hwQinQSubIfStackStatInUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfStackStatInUniPackets.setStatus("current")
_HwQinQSubIfTermTable_Object = MibTable
hwQinQSubIfTermTable = _HwQinQSubIfTermTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4)
)
if mibBuilder.loadTexts:
    hwQinQSubIfTermTable.setStatus("current")
_HwQinQSubIfTermEntry_Object = MibTableRow
hwQinQSubIfTermEntry = _HwQinQSubIfTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4, 1)
)
hwQinQSubIfTermEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfTermIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfTermPEVlan"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfTermCEVlanStart"),
)
if mibBuilder.loadTexts:
    hwQinQSubIfTermEntry.setStatus("current")
_HwQinQSubIfTermIfIndex_Type = InterfaceIndex
_HwQinQSubIfTermIfIndex_Object = MibTableColumn
hwQinQSubIfTermIfIndex = _HwQinQSubIfTermIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4, 1, 1),
    _HwQinQSubIfTermIfIndex_Type()
)
hwQinQSubIfTermIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfTermIfIndex.setStatus("current")
_HwQinQSubIfTermPEVlan_Type = VlanId
_HwQinQSubIfTermPEVlan_Object = MibTableColumn
hwQinQSubIfTermPEVlan = _HwQinQSubIfTermPEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4, 1, 2),
    _HwQinQSubIfTermPEVlan_Type()
)
hwQinQSubIfTermPEVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfTermPEVlan.setStatus("current")
_HwQinQSubIfTermCEVlanStart_Type = VlanId
_HwQinQSubIfTermCEVlanStart_Object = MibTableColumn
hwQinQSubIfTermCEVlanStart = _HwQinQSubIfTermCEVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4, 1, 3),
    _HwQinQSubIfTermCEVlanStart_Type()
)
hwQinQSubIfTermCEVlanStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfTermCEVlanStart.setStatus("current")
_HwQinQSubIfTermCEVlanEnd_Type = VlanId
_HwQinQSubIfTermCEVlanEnd_Object = MibTableColumn
hwQinQSubIfTermCEVlanEnd = _HwQinQSubIfTermCEVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4, 1, 4),
    _HwQinQSubIfTermCEVlanEnd_Type()
)
hwQinQSubIfTermCEVlanEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfTermCEVlanEnd.setStatus("current")


class _HwQinQSubIfTermGroupId_Type(Integer32):
    """Custom type hwQinQSubIfTermGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwQinQSubIfTermGroupId_Type.__name__ = "Integer32"
_HwQinQSubIfTermGroupId_Object = MibTableColumn
hwQinQSubIfTermGroupId = _HwQinQSubIfTermGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4, 1, 5),
    _HwQinQSubIfTermGroupId_Type()
)
hwQinQSubIfTermGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfTermGroupId.setStatus("current")
_HwQinQSubIfTermRowStatus_Type = RowStatus
_HwQinQSubIfTermRowStatus_Object = MibTableColumn
hwQinQSubIfTermRowStatus = _HwQinQSubIfTermRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 4, 1, 6),
    _HwQinQSubIfTermRowStatus_Type()
)
hwQinQSubIfTermRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfTermRowStatus.setStatus("current")
_HwQinQSubIfTermStatTable_Object = MibTable
hwQinQSubIfTermStatTable = _HwQinQSubIfTermStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5)
)
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatTable.setStatus("current")
_HwQinQSubIfTermStatEntry_Object = MibTableRow
hwQinQSubIfTermStatEntry = _HwQinQSubIfTermStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1)
)
hwQinQSubIfTermStatEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatPEVlan"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatCEVlan"),
)
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatEntry.setStatus("current")
_HwQinQSubIfTermStatIfIndex_Type = InterfaceIndex
_HwQinQSubIfTermStatIfIndex_Object = MibTableColumn
hwQinQSubIfTermStatIfIndex = _HwQinQSubIfTermStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 1),
    _HwQinQSubIfTermStatIfIndex_Type()
)
hwQinQSubIfTermStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatIfIndex.setStatus("current")
_HwQinQSubIfTermStatPEVlan_Type = VlanId
_HwQinQSubIfTermStatPEVlan_Object = MibTableColumn
hwQinQSubIfTermStatPEVlan = _HwQinQSubIfTermStatPEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 2),
    _HwQinQSubIfTermStatPEVlan_Type()
)
hwQinQSubIfTermStatPEVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatPEVlan.setStatus("current")
_HwQinQSubIfTermStatCEVlan_Type = VlanId
_HwQinQSubIfTermStatCEVlan_Object = MibTableColumn
hwQinQSubIfTermStatCEVlan = _HwQinQSubIfTermStatCEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 3),
    _HwQinQSubIfTermStatCEVlan_Type()
)
hwQinQSubIfTermStatCEVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatCEVlan.setStatus("current")


class _HwQinQSubIfTermStatGroupId_Type(Integer32):
    """Custom type hwQinQSubIfTermStatGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwQinQSubIfTermStatGroupId_Type.__name__ = "Integer32"
_HwQinQSubIfTermStatGroupId_Object = MibTableColumn
hwQinQSubIfTermStatGroupId = _HwQinQSubIfTermStatGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 4),
    _HwQinQSubIfTermStatGroupId_Type()
)
hwQinQSubIfTermStatGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatGroupId.setStatus("current")
_HwQinQSubIfTermStatOutPackets_Type = Counter64
_HwQinQSubIfTermStatOutPackets_Object = MibTableColumn
hwQinQSubIfTermStatOutPackets = _HwQinQSubIfTermStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 5),
    _HwQinQSubIfTermStatOutPackets_Type()
)
hwQinQSubIfTermStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatOutPackets.setStatus("current")
_HwQinQSubIfTermStatOutBytes_Type = Counter64
_HwQinQSubIfTermStatOutBytes_Object = MibTableColumn
hwQinQSubIfTermStatOutBytes = _HwQinQSubIfTermStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 6),
    _HwQinQSubIfTermStatOutBytes_Type()
)
hwQinQSubIfTermStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatOutBytes.setStatus("current")
_HwQinQSubIfTermStatInPackets_Type = Counter64
_HwQinQSubIfTermStatInPackets_Object = MibTableColumn
hwQinQSubIfTermStatInPackets = _HwQinQSubIfTermStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 7),
    _HwQinQSubIfTermStatInPackets_Type()
)
hwQinQSubIfTermStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatInPackets.setStatus("current")
_HwQinQSubIfTermStatInBytes_Type = Counter64
_HwQinQSubIfTermStatInBytes_Object = MibTableColumn
hwQinQSubIfTermStatInBytes = _HwQinQSubIfTermStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 8),
    _HwQinQSubIfTermStatInBytes_Type()
)
hwQinQSubIfTermStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatInBytes.setStatus("current")
_HwQinQSubIfTermStatOutBdPackets_Type = Counter64
_HwQinQSubIfTermStatOutBdPackets_Object = MibTableColumn
hwQinQSubIfTermStatOutBdPackets = _HwQinQSubIfTermStatOutBdPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 9),
    _HwQinQSubIfTermStatOutBdPackets_Type()
)
hwQinQSubIfTermStatOutBdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatOutBdPackets.setStatus("current")
_HwQinQSubIfTermStatInBdPackets_Type = Counter64
_HwQinQSubIfTermStatInBdPackets_Object = MibTableColumn
hwQinQSubIfTermStatInBdPackets = _HwQinQSubIfTermStatInBdPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 10),
    _HwQinQSubIfTermStatInBdPackets_Type()
)
hwQinQSubIfTermStatInBdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatInBdPackets.setStatus("current")
_HwQinQSubIfTermStatOutMuPackets_Type = Counter64
_HwQinQSubIfTermStatOutMuPackets_Object = MibTableColumn
hwQinQSubIfTermStatOutMuPackets = _HwQinQSubIfTermStatOutMuPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 11),
    _HwQinQSubIfTermStatOutMuPackets_Type()
)
hwQinQSubIfTermStatOutMuPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatOutMuPackets.setStatus("current")
_HwQinQSubIfTermStatInMuPackets_Type = Counter64
_HwQinQSubIfTermStatInMuPackets_Object = MibTableColumn
hwQinQSubIfTermStatInMuPackets = _HwQinQSubIfTermStatInMuPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 12),
    _HwQinQSubIfTermStatInMuPackets_Type()
)
hwQinQSubIfTermStatInMuPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatInMuPackets.setStatus("current")
_HwQinQSubIfTermStatOutUniPackets_Type = Counter64
_HwQinQSubIfTermStatOutUniPackets_Object = MibTableColumn
hwQinQSubIfTermStatOutUniPackets = _HwQinQSubIfTermStatOutUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 13),
    _HwQinQSubIfTermStatOutUniPackets_Type()
)
hwQinQSubIfTermStatOutUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatOutUniPackets.setStatus("current")
_HwQinQSubIfTermStatInUniPackets_Type = Counter64
_HwQinQSubIfTermStatInUniPackets_Object = MibTableColumn
hwQinQSubIfTermStatInUniPackets = _HwQinQSubIfTermStatInUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 5, 1, 14),
    _HwQinQSubIfTermStatInUniPackets_Type()
)
hwQinQSubIfTermStatInUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatInUniPackets.setStatus("current")
_HwQinQStaticARPCfgTable_Object = MibTable
hwQinQStaticARPCfgTable = _HwQinQStaticARPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6)
)
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgTable.setStatus("current")
_HwQinQStaticARPCfgEntry_Object = MibTableRow
hwQinQStaticARPCfgEntry = _HwQinQStaticARPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6, 1)
)
hwQinQStaticARPCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQStaticARPCfgIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQStaticARPCfgIp"),
)
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgEntry.setStatus("current")
_HwQinQStaticARPCfgIfIndex_Type = InterfaceIndex
_HwQinQStaticARPCfgIfIndex_Object = MibTableColumn
hwQinQStaticARPCfgIfIndex = _HwQinQStaticARPCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6, 1, 1),
    _HwQinQStaticARPCfgIfIndex_Type()
)
hwQinQStaticARPCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgIfIndex.setStatus("current")
_HwQinQStaticARPCfgIp_Type = IpAddress
_HwQinQStaticARPCfgIp_Object = MibTableColumn
hwQinQStaticARPCfgIp = _HwQinQStaticARPCfgIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6, 1, 2),
    _HwQinQStaticARPCfgIp_Type()
)
hwQinQStaticARPCfgIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgIp.setStatus("current")
_HwQinQStaticARPCfgMac_Type = MacAddress
_HwQinQStaticARPCfgMac_Object = MibTableColumn
hwQinQStaticARPCfgMac = _HwQinQStaticARPCfgMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6, 1, 3),
    _HwQinQStaticARPCfgMac_Type()
)
hwQinQStaticARPCfgMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgMac.setStatus("current")
_HwQinQStaticARPCfgVlan_Type = VlanId
_HwQinQStaticARPCfgVlan_Object = MibTableColumn
hwQinQStaticARPCfgVlan = _HwQinQStaticARPCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6, 1, 4),
    _HwQinQStaticARPCfgVlan_Type()
)
hwQinQStaticARPCfgVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgVlan.setStatus("current")


class _HwQinQStaticARPCfgCEVlan_Type(Integer32):
    """Custom type hwQinQStaticARPCfgCEVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwQinQStaticARPCfgCEVlan_Type.__name__ = "Integer32"
_HwQinQStaticARPCfgCEVlan_Object = MibTableColumn
hwQinQStaticARPCfgCEVlan = _HwQinQStaticARPCfgCEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6, 1, 5),
    _HwQinQStaticARPCfgCEVlan_Type()
)
hwQinQStaticARPCfgCEVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgCEVlan.setStatus("current")
_HwQinQStaticARPCfgRowStatus_Type = RowStatus
_HwQinQStaticARPCfgRowStatus_Object = MibTableColumn
hwQinQStaticARPCfgRowStatus = _HwQinQStaticARPCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 6, 1, 6),
    _HwQinQStaticARPCfgRowStatus_Type()
)
hwQinQStaticARPCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgRowStatus.setStatus("current")
_HwQinQStaticMACCfgTable_Object = MibTable
hwQinQStaticMACCfgTable = _HwQinQStaticMACCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7)
)
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgTable.setStatus("current")
_HwQinQStaticMACCfgEntry_Object = MibTableRow
hwQinQStaticMACCfgEntry = _HwQinQStaticMACCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1)
)
hwQinQStaticMACCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgMac"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgVsiName"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgVlan"),
)
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgEntry.setStatus("current")
_HwQinQStaticMACCfgMac_Type = MacAddress
_HwQinQStaticMACCfgMac_Object = MibTableColumn
hwQinQStaticMACCfgMac = _HwQinQStaticMACCfgMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 1),
    _HwQinQStaticMACCfgMac_Type()
)
hwQinQStaticMACCfgMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgMac.setStatus("current")
_HwQinQStaticMACCfgVlan_Type = VlanId
_HwQinQStaticMACCfgVlan_Object = MibTableColumn
hwQinQStaticMACCfgVlan = _HwQinQStaticMACCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 2),
    _HwQinQStaticMACCfgVlan_Type()
)
hwQinQStaticMACCfgVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgVlan.setStatus("current")


class _HwQinQStaticMACCfgVsiName_Type(OctetString):
    """Custom type hwQinQStaticMACCfgVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwQinQStaticMACCfgVsiName_Type.__name__ = "OctetString"
_HwQinQStaticMACCfgVsiName_Object = MibTableColumn
hwQinQStaticMACCfgVsiName = _HwQinQStaticMACCfgVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 3),
    _HwQinQStaticMACCfgVsiName_Type()
)
hwQinQStaticMACCfgVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgVsiName.setStatus("current")
_HwQinQStaticMACCfgPEVlan_Type = VlanId
_HwQinQStaticMACCfgPEVlan_Object = MibTableColumn
hwQinQStaticMACCfgPEVlan = _HwQinQStaticMACCfgPEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 4),
    _HwQinQStaticMACCfgPEVlan_Type()
)
hwQinQStaticMACCfgPEVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgPEVlan.setStatus("current")


class _HwQinQStaticMACCfgCEVlan_Type(Integer32):
    """Custom type hwQinQStaticMACCfgCEVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwQinQStaticMACCfgCEVlan_Type.__name__ = "Integer32"
_HwQinQStaticMACCfgCEVlan_Object = MibTableColumn
hwQinQStaticMACCfgCEVlan = _HwQinQStaticMACCfgCEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 5),
    _HwQinQStaticMACCfgCEVlan_Type()
)
hwQinQStaticMACCfgCEVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgCEVlan.setStatus("current")


class _HwQinQStaticMACCfgType_Type(Integer32):
    """Custom type hwQinQStaticMACCfgType based on Integer32"""
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
        *(("blackhole", 3),
          ("dynamid", 1),
          ("invalid", 0),
          ("static", 2),
          ("toobig", 4))
    )


_HwQinQStaticMACCfgType_Type.__name__ = "Integer32"
_HwQinQStaticMACCfgType_Object = MibTableColumn
hwQinQStaticMACCfgType = _HwQinQStaticMACCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 6),
    _HwQinQStaticMACCfgType_Type()
)
hwQinQStaticMACCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgType.setStatus("current")
_HwQinQStaticMACCfgIfIndex_Type = InterfaceIndex
_HwQinQStaticMACCfgIfIndex_Object = MibTableColumn
hwQinQStaticMACCfgIfIndex = _HwQinQStaticMACCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 7),
    _HwQinQStaticMACCfgIfIndex_Type()
)
hwQinQStaticMACCfgIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgIfIndex.setStatus("current")


class _HwQinQStaticMACCfgFlag_Type(Integer32):
    """Custom type hwQinQStaticMACCfgFlag based on Integer32"""
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
        *(("dot1qtermination", 5),
          ("mapping", 3),
          ("qinqtermination", 4),
          ("vlan", 1),
          ("vsi", 2))
    )


_HwQinQStaticMACCfgFlag_Type.__name__ = "Integer32"
_HwQinQStaticMACCfgFlag_Object = MibTableColumn
hwQinQStaticMACCfgFlag = _HwQinQStaticMACCfgFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 8),
    _HwQinQStaticMACCfgFlag_Type()
)
hwQinQStaticMACCfgFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgFlag.setStatus("current")
_HwQinQStaticMACCfgRowStatus_Type = RowStatus
_HwQinQStaticMACCfgRowStatus_Object = MibTableColumn
hwQinQStaticMACCfgRowStatus = _HwQinQStaticMACCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 7, 1, 9),
    _HwQinQStaticMACCfgRowStatus_Type()
)
hwQinQStaticMACCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgRowStatus.setStatus("current")
_HwQinQSubIfDot1qTermTable_Object = MibTable
hwQinQSubIfDot1qTermTable = _HwQinQSubIfDot1qTermTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 8)
)
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermTable.setStatus("current")
_HwQinQSubIfDot1qTermEntry_Object = MibTableRow
hwQinQSubIfDot1qTermEntry = _HwQinQSubIfDot1qTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 8, 1)
)
hwQinQSubIfDot1qTermEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermVidStart"),
)
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermEntry.setStatus("current")
_HwQinQSubIfDot1qTermIfIndex_Type = InterfaceIndex
_HwQinQSubIfDot1qTermIfIndex_Object = MibTableColumn
hwQinQSubIfDot1qTermIfIndex = _HwQinQSubIfDot1qTermIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 8, 1, 1),
    _HwQinQSubIfDot1qTermIfIndex_Type()
)
hwQinQSubIfDot1qTermIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermIfIndex.setStatus("current")
_HwQinQSubIfDot1qTermVidStart_Type = VlanId
_HwQinQSubIfDot1qTermVidStart_Object = MibTableColumn
hwQinQSubIfDot1qTermVidStart = _HwQinQSubIfDot1qTermVidStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 8, 1, 2),
    _HwQinQSubIfDot1qTermVidStart_Type()
)
hwQinQSubIfDot1qTermVidStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermVidStart.setStatus("current")
_HwQinQSubIfDot1qTermVidEnd_Type = VlanId
_HwQinQSubIfDot1qTermVidEnd_Object = MibTableColumn
hwQinQSubIfDot1qTermVidEnd = _HwQinQSubIfDot1qTermVidEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 8, 1, 3),
    _HwQinQSubIfDot1qTermVidEnd_Type()
)
hwQinQSubIfDot1qTermVidEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermVidEnd.setStatus("current")


class _HwQinQSubIfDot1qTermGroupId_Type(Integer32):
    """Custom type hwQinQSubIfDot1qTermGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwQinQSubIfDot1qTermGroupId_Type.__name__ = "Integer32"
_HwQinQSubIfDot1qTermGroupId_Object = MibTableColumn
hwQinQSubIfDot1qTermGroupId = _HwQinQSubIfDot1qTermGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 8, 1, 4),
    _HwQinQSubIfDot1qTermGroupId_Type()
)
hwQinQSubIfDot1qTermGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermGroupId.setStatus("current")
_HwQinQSubIfDot1qTermRowStatus_Type = RowStatus
_HwQinQSubIfDot1qTermRowStatus_Object = MibTableColumn
hwQinQSubIfDot1qTermRowStatus = _HwQinQSubIfDot1qTermRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 8, 1, 5),
    _HwQinQSubIfDot1qTermRowStatus_Type()
)
hwQinQSubIfDot1qTermRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermRowStatus.setStatus("current")
_HwQinQSubIfDot1qTermStatTable_Object = MibTable
hwQinQSubIfDot1qTermStatTable = _HwQinQSubIfDot1qTermStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9)
)
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatTable.setStatus("current")
_HwQinQSubIfDot1qTermStatEntry_Object = MibTableRow
hwQinQSubIfDot1qTermStatEntry = _HwQinQSubIfDot1qTermStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1)
)
hwQinQSubIfDot1qTermStatEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatCEVlan"),
)
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatEntry.setStatus("current")
_HwQinQSubIfDot1qTermStatIfIndex_Type = InterfaceIndex
_HwQinQSubIfDot1qTermStatIfIndex_Object = MibTableColumn
hwQinQSubIfDot1qTermStatIfIndex = _HwQinQSubIfDot1qTermStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 1),
    _HwQinQSubIfDot1qTermStatIfIndex_Type()
)
hwQinQSubIfDot1qTermStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatIfIndex.setStatus("current")
_HwQinQSubIfDot1qTermStatCEVlan_Type = VlanId
_HwQinQSubIfDot1qTermStatCEVlan_Object = MibTableColumn
hwQinQSubIfDot1qTermStatCEVlan = _HwQinQSubIfDot1qTermStatCEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 2),
    _HwQinQSubIfDot1qTermStatCEVlan_Type()
)
hwQinQSubIfDot1qTermStatCEVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatCEVlan.setStatus("current")


class _HwQinQSubIfDot1qTermStatGroupId_Type(Integer32):
    """Custom type hwQinQSubIfDot1qTermStatGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwQinQSubIfDot1qTermStatGroupId_Type.__name__ = "Integer32"
_HwQinQSubIfDot1qTermStatGroupId_Object = MibTableColumn
hwQinQSubIfDot1qTermStatGroupId = _HwQinQSubIfDot1qTermStatGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 3),
    _HwQinQSubIfDot1qTermStatGroupId_Type()
)
hwQinQSubIfDot1qTermStatGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatGroupId.setStatus("current")
_HwQinQSubIfDot1qTermStatOutPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatOutPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatOutPackets = _HwQinQSubIfDot1qTermStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 4),
    _HwQinQSubIfDot1qTermStatOutPackets_Type()
)
hwQinQSubIfDot1qTermStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatOutPackets.setStatus("current")
_HwQinQSubIfDot1qTermStatOutBytes_Type = Counter64
_HwQinQSubIfDot1qTermStatOutBytes_Object = MibTableColumn
hwQinQSubIfDot1qTermStatOutBytes = _HwQinQSubIfDot1qTermStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 5),
    _HwQinQSubIfDot1qTermStatOutBytes_Type()
)
hwQinQSubIfDot1qTermStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatOutBytes.setStatus("current")
_HwQinQSubIfDot1qTermStatInPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatInPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatInPackets = _HwQinQSubIfDot1qTermStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 6),
    _HwQinQSubIfDot1qTermStatInPackets_Type()
)
hwQinQSubIfDot1qTermStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatInPackets.setStatus("current")
_HwQinQSubIfDot1qTermStatInBytes_Type = Counter64
_HwQinQSubIfDot1qTermStatInBytes_Object = MibTableColumn
hwQinQSubIfDot1qTermStatInBytes = _HwQinQSubIfDot1qTermStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 7),
    _HwQinQSubIfDot1qTermStatInBytes_Type()
)
hwQinQSubIfDot1qTermStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatInBytes.setStatus("current")
_HwQinQSubIfDot1qTermStatOutBdPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatOutBdPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatOutBdPackets = _HwQinQSubIfDot1qTermStatOutBdPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 8),
    _HwQinQSubIfDot1qTermStatOutBdPackets_Type()
)
hwQinQSubIfDot1qTermStatOutBdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatOutBdPackets.setStatus("current")
_HwQinQSubIfDot1qTermStatInBdPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatInBdPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatInBdPackets = _HwQinQSubIfDot1qTermStatInBdPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 9),
    _HwQinQSubIfDot1qTermStatInBdPackets_Type()
)
hwQinQSubIfDot1qTermStatInBdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatInBdPackets.setStatus("current")
_HwQinQSubIfDot1qTermStatOutMuPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatOutMuPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatOutMuPackets = _HwQinQSubIfDot1qTermStatOutMuPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 10),
    _HwQinQSubIfDot1qTermStatOutMuPackets_Type()
)
hwQinQSubIfDot1qTermStatOutMuPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatOutMuPackets.setStatus("current")
_HwQinQSubIfDot1qTermStatInMuPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatInMuPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatInMuPackets = _HwQinQSubIfDot1qTermStatInMuPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 11),
    _HwQinQSubIfDot1qTermStatInMuPackets_Type()
)
hwQinQSubIfDot1qTermStatInMuPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatInMuPackets.setStatus("current")
_HwQinQSubIfDot1qTermStatOutUniPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatOutUniPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatOutUniPackets = _HwQinQSubIfDot1qTermStatOutUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 12),
    _HwQinQSubIfDot1qTermStatOutUniPackets_Type()
)
hwQinQSubIfDot1qTermStatOutUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatOutUniPackets.setStatus("current")
_HwQinQSubIfDot1qTermStatInUniPackets_Type = Counter64
_HwQinQSubIfDot1qTermStatInUniPackets_Object = MibTableColumn
hwQinQSubIfDot1qTermStatInUniPackets = _HwQinQSubIfDot1qTermStatInUniPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 9, 1, 13),
    _HwQinQSubIfDot1qTermStatInUniPackets_Type()
)
hwQinQSubIfDot1qTermStatInUniPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatInUniPackets.setStatus("current")
_HwQinQModeCfgTable_Object = MibTable
hwQinQModeCfgTable = _HwQinQModeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 10)
)
if mibBuilder.loadTexts:
    hwQinQModeCfgTable.setStatus("current")
_HwQinQModeCfgEntry_Object = MibTableRow
hwQinQModeCfgEntry = _HwQinQModeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 10, 1)
)
hwQinQModeCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQModeCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwQinQModeCfgEntry.setStatus("current")
_HwQinQModeCfgIfIndex_Type = InterfaceIndex
_HwQinQModeCfgIfIndex_Object = MibTableColumn
hwQinQModeCfgIfIndex = _HwQinQModeCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 10, 1, 1),
    _HwQinQModeCfgIfIndex_Type()
)
hwQinQModeCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQModeCfgIfIndex.setStatus("current")


class _HwQinQModeCfgMode_Type(Integer32):
    """Custom type hwQinQModeCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("qinq", 2))
    )


_HwQinQModeCfgMode_Type.__name__ = "Integer32"
_HwQinQModeCfgMode_Object = MibTableColumn
hwQinQModeCfgMode = _HwQinQModeCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 10, 1, 2),
    _HwQinQModeCfgMode_Type()
)
hwQinQModeCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQModeCfgMode.setStatus("current")


class _HwQinQEtherType_Type(Unsigned32):
    """Custom type hwQinQEtherType based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwQinQEtherType_Type.__name__ = "Unsigned32"
_HwQinQEtherType_Object = MibTableColumn
hwQinQEtherType = _HwQinQEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 10, 1, 3),
    _HwQinQEtherType_Type()
)
hwQinQEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQEtherType.setStatus("current")


class _HwQinQCeEtherType_Type(Unsigned32):
    """Custom type hwQinQCeEtherType based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwQinQCeEtherType_Type.__name__ = "Unsigned32"
_HwQinQCeEtherType_Object = MibTableColumn
hwQinQCeEtherType = _HwQinQCeEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 10, 1, 4),
    _HwQinQCeEtherType_Type()
)
hwQinQCeEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQCeEtherType.setStatus("current")
_HwQinQCtrlVlanCfgTable_Object = MibTable
hwQinQCtrlVlanCfgTable = _HwQinQCtrlVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11)
)
if mibBuilder.loadTexts:
    hwQinQCtrlVlanCfgTable.setStatus("current")
_HwQinQCtrlVlanCfgEntry_Object = MibTableRow
hwQinQCtrlVlanCfgEntry = _HwQinQCtrlVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11, 1)
)
hwQinQCtrlVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQCtrlVlanCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwQinQCtrlVlanCfgEntry.setStatus("current")
_HwQinQCtrlVlanCfgIfIndex_Type = InterfaceIndex
_HwQinQCtrlVlanCfgIfIndex_Object = MibTableColumn
hwQinQCtrlVlanCfgIfIndex = _HwQinQCtrlVlanCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11, 1, 1),
    _HwQinQCtrlVlanCfgIfIndex_Type()
)
hwQinQCtrlVlanCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQCtrlVlanCfgIfIndex.setStatus("current")
_HwQinQCtrlVlan_Type = VlanId
_HwQinQCtrlVlan_Object = MibTableColumn
hwQinQCtrlVlan = _HwQinQCtrlVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11, 1, 2),
    _HwQinQCtrlVlan_Type()
)
hwQinQCtrlVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQCtrlVlan.setStatus("current")


class _HwQinQSubIfType_Type(Integer32):
    """Custom type hwQinQSubIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1q", 2),
          ("qinq", 1))
    )


_HwQinQSubIfType_Type.__name__ = "Integer32"
_HwQinQSubIfType_Object = MibTableColumn
hwQinQSubIfType = _HwQinQSubIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11, 1, 3),
    _HwQinQSubIfType_Type()
)
hwQinQSubIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfType.setStatus("current")


class _HwQinQCtrlVlanFlag_Type(Integer32):
    """Custom type hwQinQCtrlVlanFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localswitch", 3),
          ("original", 2),
          ("rtprotocolenable", 1))
    )


_HwQinQCtrlVlanFlag_Type.__name__ = "Integer32"
_HwQinQCtrlVlanFlag_Object = MibTableColumn
hwQinQCtrlVlanFlag = _HwQinQCtrlVlanFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11, 1, 4),
    _HwQinQCtrlVlanFlag_Type()
)
hwQinQCtrlVlanFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQCtrlVlanFlag.setStatus("current")
_HwQinQCtrlVlanRowStatus_Type = RowStatus
_HwQinQCtrlVlanRowStatus_Object = MibTableColumn
hwQinQCtrlVlanRowStatus = _HwQinQCtrlVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11, 1, 5),
    _HwQinQCtrlVlanRowStatus_Type()
)
hwQinQCtrlVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQCtrlVlanRowStatus.setStatus("current")
_HwQinQFlexibleFlag_Type = EnabledStatus
_HwQinQFlexibleFlag_Object = MibTableColumn
hwQinQFlexibleFlag = _HwQinQFlexibleFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 11, 1, 6),
    _HwQinQFlexibleFlag_Type()
)
hwQinQFlexibleFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQFlexibleFlag.setStatus("current")
_HwQinQGroupCfgTable_Object = MibTable
hwQinQGroupCfgTable = _HwQinQGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 12)
)
if mibBuilder.loadTexts:
    hwQinQGroupCfgTable.setStatus("current")
_HwQinQGroupCfgEntry_Object = MibTableRow
hwQinQGroupCfgEntry = _HwQinQGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 12, 1)
)
hwQinQGroupCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQGroupCfgIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQGroupId"),
)
if mibBuilder.loadTexts:
    hwQinQGroupCfgEntry.setStatus("current")
_HwQinQGroupCfgIfIndex_Type = InterfaceIndex
_HwQinQGroupCfgIfIndex_Object = MibTableColumn
hwQinQGroupCfgIfIndex = _HwQinQGroupCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 12, 1, 1),
    _HwQinQGroupCfgIfIndex_Type()
)
hwQinQGroupCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQGroupCfgIfIndex.setStatus("current")


class _HwQinQGroupId_Type(Integer32):
    """Custom type hwQinQGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwQinQGroupId_Type.__name__ = "Integer32"
_HwQinQGroupId_Object = MibTableColumn
hwQinQGroupId = _HwQinQGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 12, 1, 2),
    _HwQinQGroupId_Type()
)
hwQinQGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQGroupId.setStatus("current")


class _HwQinQGroupType_Type(Integer32):
    """Custom type hwQinQGroupType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multi", 2),
          ("single", 1))
    )


_HwQinQGroupType_Type.__name__ = "Integer32"
_HwQinQGroupType_Object = MibTableColumn
hwQinQGroupType = _HwQinQGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 12, 1, 3),
    _HwQinQGroupType_Type()
)
hwQinQGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQGroupType.setStatus("current")


class _HwQinQGroupStat_Type(EnabledStatus):
    """Custom type hwQinQGroupStat based on EnabledStatus"""


_HwQinQGroupStat_Object = MibTableColumn
hwQinQGroupStat = _HwQinQGroupStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 12, 1, 4),
    _HwQinQGroupStat_Type()
)
hwQinQGroupStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQGroupStat.setStatus("current")
_HwQinQGroupRowStatus_Type = RowStatus
_HwQinQGroupRowStatus_Object = MibTableColumn
hwQinQGroupRowStatus = _HwQinQGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 12, 1, 5),
    _HwQinQGroupRowStatus_Type()
)
hwQinQGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQGroupRowStatus.setStatus("current")
_HwQinQAsymmetryCfgTable_Object = MibTable
hwQinQAsymmetryCfgTable = _HwQinQAsymmetryCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 13)
)
if mibBuilder.loadTexts:
    hwQinQAsymmetryCfgTable.setStatus("current")
_HwQinQAsymmetryCfgEntry_Object = MibTableRow
hwQinQAsymmetryCfgEntry = _HwQinQAsymmetryCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 13, 1)
)
hwQinQAsymmetryCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQAsymmetryCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwQinQAsymmetryCfgEntry.setStatus("current")
_HwQinQAsymmetryCfgIfIndex_Type = InterfaceIndex
_HwQinQAsymmetryCfgIfIndex_Object = MibTableColumn
hwQinQAsymmetryCfgIfIndex = _HwQinQAsymmetryCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 13, 1, 1),
    _HwQinQAsymmetryCfgIfIndex_Type()
)
hwQinQAsymmetryCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQAsymmetryCfgIfIndex.setStatus("current")


class _HwQinQSubIfAsymmetry_Type(Integer32):
    """Custom type hwQinQSubIfAsymmetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetry", 2),
          ("symmetry", 1),
          ("transparent", 3))
    )


_HwQinQSubIfAsymmetry_Type.__name__ = "Integer32"
_HwQinQSubIfAsymmetry_Object = MibTableColumn
hwQinQSubIfAsymmetry = _HwQinQSubIfAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 13, 1, 2),
    _HwQinQSubIfAsymmetry_Type()
)
hwQinQSubIfAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQSubIfAsymmetry.setStatus("current")


class _HwQinQAsymmetryUserMode_Type(EnabledStatus):
    """Custom type hwQinQAsymmetryUserMode based on EnabledStatus"""


_HwQinQAsymmetryUserMode_Object = MibTableColumn
hwQinQAsymmetryUserMode = _HwQinQAsymmetryUserMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 13, 1, 3),
    _HwQinQAsymmetryUserMode_Type()
)
hwQinQAsymmetryUserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQAsymmetryUserMode.setStatus("current")
_HwQinQRemarkCfgTable_Object = MibTable
hwQinQRemarkCfgTable = _HwQinQRemarkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 14)
)
if mibBuilder.loadTexts:
    hwQinQRemarkCfgTable.setStatus("current")
_HwQinQRemarkCfgEntry_Object = MibTableRow
hwQinQRemarkCfgEntry = _HwQinQRemarkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 14, 1)
)
hwQinQRemarkCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQRemarkCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwQinQRemarkCfgEntry.setStatus("current")
_HwQinQRemarkCfgIfIndex_Type = InterfaceIndex
_HwQinQRemarkCfgIfIndex_Object = MibTableColumn
hwQinQRemarkCfgIfIndex = _HwQinQRemarkCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 14, 1, 1),
    _HwQinQRemarkCfgIfIndex_Type()
)
hwQinQRemarkCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQRemarkCfgIfIndex.setStatus("current")


class _HwQinQPriorityRemark_Type(Integer32):
    """Custom type hwQinQPriorityRemark based on Integer32"""
    defaultValue = 9

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
        *(("cevid", 8),
          ("pevid", 9),
          ("specify0", 0),
          ("specify1", 1),
          ("specify2", 2),
          ("specify3", 3),
          ("specify4", 4),
          ("specify5", 5),
          ("specify6", 6),
          ("specify7", 7))
    )


_HwQinQPriorityRemark_Type.__name__ = "Integer32"
_HwQinQPriorityRemark_Object = MibTableColumn
hwQinQPriorityRemark = _HwQinQPriorityRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 14, 1, 2),
    _HwQinQPriorityRemark_Type()
)
hwQinQPriorityRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQPriorityRemark.setStatus("current")
_HwBpduTunnelIngressTable_Object = MibTable
hwBpduTunnelIngressTable = _HwBpduTunnelIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 15)
)
if mibBuilder.loadTexts:
    hwBpduTunnelIngressTable.setStatus("current")
_HwBpduTunnelIngressEntry_Object = MibTableRow
hwBpduTunnelIngressEntry = _HwBpduTunnelIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 15, 1)
)
hwBpduTunnelIngressEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwBpduTunnelIngressPortIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwBpduTunnelBpduIngressMacIndex"),
)
if mibBuilder.loadTexts:
    hwBpduTunnelIngressEntry.setStatus("current")


class _HwBpduTunnelIngressPortIndex_Type(Integer32):
    """Custom type hwBpduTunnelIngressPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBpduTunnelIngressPortIndex_Type.__name__ = "Integer32"
_HwBpduTunnelIngressPortIndex_Object = MibTableColumn
hwBpduTunnelIngressPortIndex = _HwBpduTunnelIngressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 15, 1, 1),
    _HwBpduTunnelIngressPortIndex_Type()
)
hwBpduTunnelIngressPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBpduTunnelIngressPortIndex.setStatus("current")
_HwBpduTunnelBpduIngressMacIndex_Type = BpduIndex
_HwBpduTunnelBpduIngressMacIndex_Object = MibTableColumn
hwBpduTunnelBpduIngressMacIndex = _HwBpduTunnelBpduIngressMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 15, 1, 2),
    _HwBpduTunnelBpduIngressMacIndex_Type()
)
hwBpduTunnelBpduIngressMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBpduTunnelBpduIngressMacIndex.setStatus("current")
_HwBpduTunnelIngressAddress_Type = MacAddress
_HwBpduTunnelIngressAddress_Object = MibTableColumn
hwBpduTunnelIngressAddress = _HwBpduTunnelIngressAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 15, 1, 3),
    _HwBpduTunnelIngressAddress_Type()
)
hwBpduTunnelIngressAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBpduTunnelIngressAddress.setStatus("current")
_HwBpduTunnelIngressRowStatus_Type = RowStatus
_HwBpduTunnelIngressRowStatus_Object = MibTableColumn
hwBpduTunnelIngressRowStatus = _HwBpduTunnelIngressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 15, 1, 4),
    _HwBpduTunnelIngressRowStatus_Type()
)
hwBpduTunnelIngressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBpduTunnelIngressRowStatus.setStatus("current")
_HwBpduTunnelEgressTable_Object = MibTable
hwBpduTunnelEgressTable = _HwBpduTunnelEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 16)
)
if mibBuilder.loadTexts:
    hwBpduTunnelEgressTable.setStatus("current")
_HwBpduTunnelEgressEntry_Object = MibTableRow
hwBpduTunnelEgressEntry = _HwBpduTunnelEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 16, 1)
)
hwBpduTunnelEgressEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwBpduTunnelEgressPortIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwBpduTunnelBpduEgressMacIndex"),
)
if mibBuilder.loadTexts:
    hwBpduTunnelEgressEntry.setStatus("current")


class _HwBpduTunnelEgressPortIndex_Type(Integer32):
    """Custom type hwBpduTunnelEgressPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBpduTunnelEgressPortIndex_Type.__name__ = "Integer32"
_HwBpduTunnelEgressPortIndex_Object = MibTableColumn
hwBpduTunnelEgressPortIndex = _HwBpduTunnelEgressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 16, 1, 1),
    _HwBpduTunnelEgressPortIndex_Type()
)
hwBpduTunnelEgressPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBpduTunnelEgressPortIndex.setStatus("current")
_HwBpduTunnelBpduEgressMacIndex_Type = BpduIndex
_HwBpduTunnelBpduEgressMacIndex_Object = MibTableColumn
hwBpduTunnelBpduEgressMacIndex = _HwBpduTunnelBpduEgressMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 16, 1, 2),
    _HwBpduTunnelBpduEgressMacIndex_Type()
)
hwBpduTunnelBpduEgressMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBpduTunnelBpduEgressMacIndex.setStatus("current")
_HwBpduTunnelEgressAddress_Type = MacAddress
_HwBpduTunnelEgressAddress_Object = MibTableColumn
hwBpduTunnelEgressAddress = _HwBpduTunnelEgressAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 16, 1, 3),
    _HwBpduTunnelEgressAddress_Type()
)
hwBpduTunnelEgressAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBpduTunnelEgressAddress.setStatus("current")
_HwBpduTunnelEgressRowStatus_Type = RowStatus
_HwBpduTunnelEgressRowStatus_Object = MibTableColumn
hwBpduTunnelEgressRowStatus = _HwBpduTunnelEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 16, 1, 4),
    _HwBpduTunnelEgressRowStatus_Type()
)
hwBpduTunnelEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBpduTunnelEgressRowStatus.setStatus("current")
_HwBpduTunnelVlanTable_Object = MibTable
hwBpduTunnelVlanTable = _HwBpduTunnelVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 17)
)
if mibBuilder.loadTexts:
    hwBpduTunnelVlanTable.setStatus("current")
_HwBpduTunnelVlanEntry_Object = MibTableRow
hwBpduTunnelVlanEntry = _HwBpduTunnelVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 17, 1)
)
hwBpduTunnelVlanEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwBpduTunnelPortIndex"),
)
if mibBuilder.loadTexts:
    hwBpduTunnelVlanEntry.setStatus("current")


class _HwBpduTunnelPortIndex_Type(Integer32):
    """Custom type hwBpduTunnelPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBpduTunnelPortIndex_Type.__name__ = "Integer32"
_HwBpduTunnelPortIndex_Object = MibTableColumn
hwBpduTunnelPortIndex = _HwBpduTunnelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 17, 1, 1),
    _HwBpduTunnelPortIndex_Type()
)
hwBpduTunnelPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBpduTunnelPortIndex.setStatus("current")


class _HwBpduTunnelEnable_Type(Integer32):
    """Custom type hwBpduTunnelEnable based on Integer32"""
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


_HwBpduTunnelEnable_Type.__name__ = "Integer32"
_HwBpduTunnelEnable_Object = MibTableColumn
hwBpduTunnelEnable = _HwBpduTunnelEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 17, 1, 2),
    _HwBpduTunnelEnable_Type()
)
hwBpduTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBpduTunnelEnable.setStatus("current")
_HwBpduTunnelVlanListLow_Type = VlanList
_HwBpduTunnelVlanListLow_Object = MibTableColumn
hwBpduTunnelVlanListLow = _HwBpduTunnelVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 17, 1, 3),
    _HwBpduTunnelVlanListLow_Type()
)
hwBpduTunnelVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBpduTunnelVlanListLow.setStatus("current")
_HwBpduTunnelVlanListHigh_Type = VlanList
_HwBpduTunnelVlanListHigh_Object = MibTableColumn
hwBpduTunnelVlanListHigh = _HwBpduTunnelVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 17, 1, 4),
    _HwBpduTunnelVlanListHigh_Type()
)
hwBpduTunnelVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBpduTunnelVlanListHigh.setStatus("current")
_HwBpduTunnelTable_Object = MibTable
hwBpduTunnelTable = _HwBpduTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 18)
)
if mibBuilder.loadTexts:
    hwBpduTunnelTable.setStatus("current")
_HwBpduTunnelEntry_Object = MibTableRow
hwBpduTunnelEntry = _HwBpduTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 18, 1)
)
hwBpduTunnelEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwBpduTunnelBpduIndex"),
)
if mibBuilder.loadTexts:
    hwBpduTunnelEntry.setStatus("current")
_HwBpduTunnelBpduIndex_Type = BpduIndex
_HwBpduTunnelBpduIndex_Object = MibTableColumn
hwBpduTunnelBpduIndex = _HwBpduTunnelBpduIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 18, 1, 1),
    _HwBpduTunnelBpduIndex_Type()
)
hwBpduTunnelBpduIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBpduTunnelBpduIndex.setStatus("current")


class _HwBpduTunnelBpduEnable_Type(Integer32):
    """Custom type hwBpduTunnelBpduEnable based on Integer32"""
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


_HwBpduTunnelBpduEnable_Type.__name__ = "Integer32"
_HwBpduTunnelBpduEnable_Object = MibTableColumn
hwBpduTunnelBpduEnable = _HwBpduTunnelBpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 18, 1, 2),
    _HwBpduTunnelBpduEnable_Type()
)
hwBpduTunnelBpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBpduTunnelBpduEnable.setStatus("current")
_HwBpduTunnelMultiAddress_Type = MacAddress
_HwBpduTunnelMultiAddress_Object = MibTableColumn
hwBpduTunnelMultiAddress = _HwBpduTunnelMultiAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 18, 1, 3),
    _HwBpduTunnelMultiAddress_Type()
)
hwBpduTunnelMultiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBpduTunnelMultiAddress.setStatus("current")
_HwBpduTunnelRowStatus_Type = RowStatus
_HwBpduTunnelRowStatus_Object = MibTableColumn
hwBpduTunnelRowStatus = _HwBpduTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 18, 1, 4),
    _HwBpduTunnelRowStatus_Type()
)
hwBpduTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBpduTunnelRowStatus.setStatus("current")
_HwQinQSwapCfgTable_Object = MibTable
hwQinQSwapCfgTable = _HwQinQSwapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 19)
)
if mibBuilder.loadTexts:
    hwQinQSwapCfgTable.setStatus("current")
_HwQinQSwapCfgEntry_Object = MibTableRow
hwQinQSwapCfgEntry = _HwQinQSwapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 19, 1)
)
hwQinQSwapCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSwapCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwQinQSwapCfgEntry.setStatus("current")
_HwQinQSwapCfgIfIndex_Type = InterfaceIndex
_HwQinQSwapCfgIfIndex_Object = MibTableColumn
hwQinQSwapCfgIfIndex = _HwQinQSwapCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 19, 1, 1),
    _HwQinQSwapCfgIfIndex_Type()
)
hwQinQSwapCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSwapCfgIfIndex.setStatus("current")


class _HwQinQSwapCfgFlag_Type(EnabledStatus):
    """Custom type hwQinQSwapCfgFlag based on EnabledStatus"""


_HwQinQSwapCfgFlag_Object = MibTableColumn
hwQinQSwapCfgFlag = _HwQinQSwapCfgFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 19, 1, 2),
    _HwQinQSwapCfgFlag_Type()
)
hwQinQSwapCfgFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQSwapCfgFlag.setStatus("current")
_HwQinQSubIfMapTable_Object = MibTable
hwQinQSubIfMapTable = _HwQinQSubIfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20)
)
if mibBuilder.loadTexts:
    hwQinQSubIfMapTable.setStatus("current")
_HwQinQSubIfMapEntry_Object = MibTableRow
hwQinQSubIfMapEntry = _HwQinQSubIfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1)
)
hwQinQSubIfMapEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfMapIfIndex"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfPEVlan"),
    (0, "HUAWEI-QINQ-MIB", "hwQinQSubIfCEVlanStart"),
)
if mibBuilder.loadTexts:
    hwQinQSubIfMapEntry.setStatus("current")
_HwQinQSubIfMapIfIndex_Type = InterfaceIndex
_HwQinQSubIfMapIfIndex_Object = MibTableColumn
hwQinQSubIfMapIfIndex = _HwQinQSubIfMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 1),
    _HwQinQSubIfMapIfIndex_Type()
)
hwQinQSubIfMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfMapIfIndex.setStatus("current")


class _HwQinQSubIfPEVlan_Type(Integer32):
    """Custom type hwQinQSubIfPEVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwQinQSubIfPEVlan_Type.__name__ = "Integer32"
_HwQinQSubIfPEVlan_Object = MibTableColumn
hwQinQSubIfPEVlan = _HwQinQSubIfPEVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 2),
    _HwQinQSubIfPEVlan_Type()
)
hwQinQSubIfPEVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfPEVlan.setStatus("current")


class _HwQinQSubIfCEVlanStart_Type(Integer32):
    """Custom type hwQinQSubIfCEVlanStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwQinQSubIfCEVlanStart_Type.__name__ = "Integer32"
_HwQinQSubIfCEVlanStart_Object = MibTableColumn
hwQinQSubIfCEVlanStart = _HwQinQSubIfCEVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 3),
    _HwQinQSubIfCEVlanStart_Type()
)
hwQinQSubIfCEVlanStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQSubIfCEVlanStart.setStatus("current")


class _HwQinQSubIfCEVlanEnd_Type(Integer32):
    """Custom type hwQinQSubIfCEVlanEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwQinQSubIfCEVlanEnd_Type.__name__ = "Integer32"
_HwQinQSubIfCEVlanEnd_Object = MibTableColumn
hwQinQSubIfCEVlanEnd = _HwQinQSubIfCEVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 4),
    _HwQinQSubIfCEVlanEnd_Type()
)
hwQinQSubIfCEVlanEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfCEVlanEnd.setStatus("current")


class _HwQinQSubIfPEVlanMap_Type(Integer32):
    """Custom type hwQinQSubIfPEVlanMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwQinQSubIfPEVlanMap_Type.__name__ = "Integer32"
_HwQinQSubIfPEVlanMap_Object = MibTableColumn
hwQinQSubIfPEVlanMap = _HwQinQSubIfPEVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 5),
    _HwQinQSubIfPEVlanMap_Type()
)
hwQinQSubIfPEVlanMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfPEVlanMap.setStatus("current")


class _HwQinQSubIfPEEtherType_Type(Unsigned32):
    """Custom type hwQinQSubIfPEEtherType based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwQinQSubIfPEEtherType_Type.__name__ = "Unsigned32"
_HwQinQSubIfPEEtherType_Object = MibTableColumn
hwQinQSubIfPEEtherType = _HwQinQSubIfPEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 6),
    _HwQinQSubIfPEEtherType_Type()
)
hwQinQSubIfPEEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfPEEtherType.setStatus("current")


class _HwQinQSubIfCEVlanMap_Type(Integer32):
    """Custom type hwQinQSubIfCEVlanMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwQinQSubIfCEVlanMap_Type.__name__ = "Integer32"
_HwQinQSubIfCEVlanMap_Object = MibTableColumn
hwQinQSubIfCEVlanMap = _HwQinQSubIfCEVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 7),
    _HwQinQSubIfCEVlanMap_Type()
)
hwQinQSubIfCEVlanMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfCEVlanMap.setStatus("current")


class _HwQinQSubIfCEEtherType_Type(Unsigned32):
    """Custom type hwQinQSubIfCEEtherType based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwQinQSubIfCEEtherType_Type.__name__ = "Unsigned32"
_HwQinQSubIfCEEtherType_Object = MibTableColumn
hwQinQSubIfCEEtherType = _HwQinQSubIfCEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 8),
    _HwQinQSubIfCEEtherType_Type()
)
hwQinQSubIfCEEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfCEEtherType.setStatus("current")


class _HwQinQSubIfMapGroupId_Type(Integer32):
    """Custom type hwQinQSubIfMapGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwQinQSubIfMapGroupId_Type.__name__ = "Integer32"
_HwQinQSubIfMapGroupId_Object = MibTableColumn
hwQinQSubIfMapGroupId = _HwQinQSubIfMapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 9),
    _HwQinQSubIfMapGroupId_Type()
)
hwQinQSubIfMapGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfMapGroupId.setStatus("current")


class _HwQinQSubIfMapPe8021p_Type(Integer32):
    """Custom type hwQinQSubIfMapPe8021p based on Integer32"""
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
        *(("specify0", 0),
          ("specify1", 1),
          ("specify2", 2),
          ("specify3", 3),
          ("specify4", 4),
          ("specify5", 5),
          ("specify6", 6),
          ("specify7", 7))
    )


_HwQinQSubIfMapPe8021p_Type.__name__ = "Integer32"
_HwQinQSubIfMapPe8021p_Object = MibTableColumn
hwQinQSubIfMapPe8021p = _HwQinQSubIfMapPe8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 10),
    _HwQinQSubIfMapPe8021p_Type()
)
hwQinQSubIfMapPe8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQSubIfMapPe8021p.setStatus("current")


class _HwQinQSubIfMapCe8021p_Type(Integer32):
    """Custom type hwQinQSubIfMapCe8021p based on Integer32"""
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
        *(("specify0", 0),
          ("specify1", 1),
          ("specify2", 2),
          ("specify3", 3),
          ("specify4", 4),
          ("specify5", 5),
          ("specify6", 6),
          ("specify7", 7))
    )


_HwQinQSubIfMapCe8021p_Type.__name__ = "Integer32"
_HwQinQSubIfMapCe8021p_Object = MibTableColumn
hwQinQSubIfMapCe8021p = _HwQinQSubIfMapCe8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 11),
    _HwQinQSubIfMapCe8021p_Type()
)
hwQinQSubIfMapCe8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQinQSubIfMapCe8021p.setStatus("current")
_HwQinQSubIfMapCetoPeFlag_Type = EnabledStatus
_HwQinQSubIfMapCetoPeFlag_Object = MibTableColumn
hwQinQSubIfMapCetoPeFlag = _HwQinQSubIfMapCetoPeFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 12),
    _HwQinQSubIfMapCetoPeFlag_Type()
)
hwQinQSubIfMapCetoPeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfMapCetoPeFlag.setStatus("current")
_HwQinQSubIfMapRowStatus_Type = RowStatus
_HwQinQSubIfMapRowStatus_Object = MibTableColumn
hwQinQSubIfMapRowStatus = _HwQinQSubIfMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 20, 1, 13),
    _HwQinQSubIfMapRowStatus_Type()
)
hwQinQSubIfMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQSubIfMapRowStatus.setStatus("current")
_HwQinQStackingVlanCfgTable_Object = MibTable
hwQinQStackingVlanCfgTable = _HwQinQStackingVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 21)
)
if mibBuilder.loadTexts:
    hwQinQStackingVlanCfgTable.setStatus("current")
_HwQinQStackingVlanCfgEntry_Object = MibTableRow
hwQinQStackingVlanCfgEntry = _HwQinQStackingVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 21, 1)
)
hwQinQStackingVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-QINQ-MIB", "hwQinQStackingVlanCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwQinQStackingVlanCfgEntry.setStatus("current")
_HwQinQStackingVlanCfgIfIndex_Type = InterfaceIndex
_HwQinQStackingVlanCfgIfIndex_Object = MibTableColumn
hwQinQStackingVlanCfgIfIndex = _HwQinQStackingVlanCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 21, 1, 1),
    _HwQinQStackingVlanCfgIfIndex_Type()
)
hwQinQStackingVlanCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwQinQStackingVlanCfgIfIndex.setStatus("current")
_HwQinQStackingVlanCfgVlanId_Type = VlanId
_HwQinQStackingVlanCfgVlanId_Object = MibTableColumn
hwQinQStackingVlanCfgVlanId = _HwQinQStackingVlanCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 21, 1, 2),
    _HwQinQStackingVlanCfgVlanId_Type()
)
hwQinQStackingVlanCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStackingVlanCfgVlanId.setStatus("current")
_HwQinQStackingVlanCfgRowStatus_Type = RowStatus
_HwQinQStackingVlanCfgRowStatus_Object = MibTableColumn
hwQinQStackingVlanCfgRowStatus = _HwQinQStackingVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 2, 21, 1, 50),
    _HwQinQStackingVlanCfgRowStatus_Type()
)
hwQinQStackingVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwQinQStackingVlanCfgRowStatus.setStatus("current")
_HwQinQConformance_ObjectIdentity = ObjectIdentity
hwQinQConformance = _HwQinQConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3)
)
_HwQinQGroups_ObjectIdentity = ObjectIdentity
hwQinQGroups = _HwQinQGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1)
)
_HwQinQCompliances_ObjectIdentity = ObjectIdentity
hwQinQCompliances = _HwQinQCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 2)
)

# Managed Objects groups

hwQinQSystemBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 1)
)
hwQinQSystemBaseGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSystemWellKnowMac"),
        ("HUAWEI-QINQ-MIB", "hwQinQSystemBridgeRole"),
        ("HUAWEI-QINQ-MIB", "hwBpduSystemDropPacketSta"),
        ("HUAWEI-QINQ-MIB", "hwQinQSystemEtherType"))
)
if mibBuilder.loadTexts:
    hwQinQSystemBaseGroup.setStatus("current")

hwQinQBpduTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 2)
)
hwQinQBpduTunnelGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQEtherEncpsType"),
        ("HUAWEI-QINQ-MIB", "hwQinQBpduTunnelEnableOneQBpduTunnel"),
        ("HUAWEI-QINQ-MIB", "hwQinQBpduTunnelEnableBpduTag"),
        ("HUAWEI-QINQ-MIB", "hwQinQBpduTunnelEnableTwoQBpduTunnel"),
        ("HUAWEI-QINQ-MIB", "hwQinQBpduTunnelCustomerBpduTag"),
        ("HUAWEI-QINQ-MIB", "hwQinQBpduTunnelCustomerBpduTagListLow"),
        ("HUAWEI-QINQ-MIB", "hwQinQBpduTunnelCustomerBpduTagListHigh"),
        ("HUAWEI-QINQ-MIB", "hwQinQRemarkOuterTpid"),
        ("HUAWEI-QINQ-MIB", "hwQinQBpduTunnelEnableBpduFilter"))
)
if mibBuilder.loadTexts:
    hwQinQBpduTunnelGroup.setStatus("current")

hwQinQSubIfVlanStackingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 3)
)
hwQinQSubIfVlanStackingGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfStackingCEVlanEnd"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackGroupId"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackingRowStatus"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackingPEVlan"))
)
if mibBuilder.loadTexts:
    hwQinQSubIfVlanStackingGroup.setStatus("current")

hwQinQSubIfStackingStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 4)
)
hwQinQSubIfStackingStatGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfStackStatGroupId"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackingStatOutPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackingStatOutBytes"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackingStatInPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackingStatInBytes"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackStatOutBdPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackStatInBdPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackStatOutMuPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackStatInMuPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackStatOutUniPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfStackStatInUniPackets"))
)
if mibBuilder.loadTexts:
    hwQinQSubIfStackingStatGroup.setStatus("current")

hwQinQSubIfTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 5)
)
hwQinQSubIfTermGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfTermCEVlanEnd"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermGroupId"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermRowStatus"))
)
if mibBuilder.loadTexts:
    hwQinQSubIfTermGroup.setStatus("current")

hwQinQSubIfTermStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 6)
)
hwQinQSubIfTermStatGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatGroupId"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatOutPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatOutBytes"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatInPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatInBytes"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatOutBdPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatInBdPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatOutMuPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatInMuPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatOutUniPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfTermStatInUniPackets"))
)
if mibBuilder.loadTexts:
    hwQinQSubIfTermStatGroup.setStatus("current")

hwQinQStaticARPCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 7)
)
hwQinQStaticARPCfgGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQStaticARPCfgMac"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticARPCfgVlan"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticARPCfgCEVlan"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticARPCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwQinQStaticARPCfgGroup.setStatus("current")

hwQinQStaticMACCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 8)
)
hwQinQStaticMACCfgGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgPEVlan"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgCEVlan"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgType"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgIfIndex"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgFlag"),
        ("HUAWEI-QINQ-MIB", "hwQinQStaticMACCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwQinQStaticMACCfgGroup.setStatus("current")

hwQinQSubIfDot1qTermGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 9)
)
hwQinQSubIfDot1qTermGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermVidEnd"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermGroupId"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermRowStatus"))
)
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermGroup.setStatus("current")

hwQinQSubIfDot1qTermStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 10)
)
hwQinQSubIfDot1qTermStatGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatGroupId"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatOutPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatOutBytes"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatInPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatInBytes"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatOutBdPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatInBdPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatOutMuPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatInMuPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatOutUniPackets"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfDot1qTermStatInUniPackets"))
)
if mibBuilder.loadTexts:
    hwQinQSubIfDot1qTermStatGroup.setStatus("current")

hwQinQModeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 11)
)
hwQinQModeCfgGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQModeCfgMode"),
        ("HUAWEI-QINQ-MIB", "hwQinQEtherType"))
)
if mibBuilder.loadTexts:
    hwQinQModeCfgGroup.setStatus("current")

hwQinQCtrlVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 12)
)
hwQinQCtrlVlanCfgGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQCtrlVlan"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfType"),
        ("HUAWEI-QINQ-MIB", "hwQinQCtrlVlanFlag"),
        ("HUAWEI-QINQ-MIB", "hwQinQCtrlVlanRowStatus"),
        ("HUAWEI-QINQ-MIB", "hwQinQFlexibleFlag"))
)
if mibBuilder.loadTexts:
    hwQinQCtrlVlanCfgGroup.setStatus("current")

hwQinQGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 13)
)
hwQinQGroupCfgGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQGroupType"),
        ("HUAWEI-QINQ-MIB", "hwQinQGroupStat"),
        ("HUAWEI-QINQ-MIB", "hwQinQGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwQinQGroupCfgGroup.setStatus("current")

hwQinQAsymmetryCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 14)
)
hwQinQAsymmetryCfgGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfAsymmetry"),
        ("HUAWEI-QINQ-MIB", "hwQinQAsymmetryUserMode"))
)
if mibBuilder.loadTexts:
    hwQinQAsymmetryCfgGroup.setStatus("current")

hwQinQRemarkCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 15)
)
hwQinQRemarkCfgGroup.setObjects(
    ("HUAWEI-QINQ-MIB", "hwQinQPriorityRemark")
)
if mibBuilder.loadTexts:
    hwQinQRemarkCfgGroup.setStatus("current")

hwBpduTunnelIngressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 16)
)
hwBpduTunnelIngressGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwBpduTunnelIngressAddress"),
        ("HUAWEI-QINQ-MIB", "hwBpduTunnelIngressRowStatus"))
)
if mibBuilder.loadTexts:
    hwBpduTunnelIngressGroup.setStatus("current")

hwBpduTunnelEgressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 17)
)
hwBpduTunnelEgressGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwBpduTunnelEgressAddress"),
        ("HUAWEI-QINQ-MIB", "hwBpduTunnelEgressRowStatus"))
)
if mibBuilder.loadTexts:
    hwBpduTunnelEgressGroup.setStatus("current")

hwBpduTunnelVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 18)
)
hwBpduTunnelVlanGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwBpduTunnelEnable"),
        ("HUAWEI-QINQ-MIB", "hwBpduTunnelVlanListLow"),
        ("HUAWEI-QINQ-MIB", "hwBpduTunnelVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwBpduTunnelVlanGroup.setStatus("current")

hwBpduTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 19)
)
hwBpduTunnelGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwBpduTunnelBpduEnable"),
        ("HUAWEI-QINQ-MIB", "hwBpduTunnelMultiAddress"),
        ("HUAWEI-QINQ-MIB", "hwBpduTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    hwBpduTunnelGroup.setStatus("current")

hwQinQSwapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 20)
)
hwQinQSwapCfgGroup.setObjects(
    ("HUAWEI-QINQ-MIB", "hwQinQSwapCfgFlag")
)
if mibBuilder.loadTexts:
    hwQinQSwapCfgGroup.setStatus("current")

hwQinQSubIfMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 21)
)
hwQinQSubIfMapGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQSubIfCEVlanEnd"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfPEVlanMap"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfPEEtherType"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfCEVlanMap"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfCEEtherType"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfMapGroupId"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfMapRowStatus"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfMapPe8021p"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfMapCe8021p"),
        ("HUAWEI-QINQ-MIB", "hwQinQSubIfMapCetoPeFlag"))
)
if mibBuilder.loadTexts:
    hwQinQSubIfMapGroup.setStatus("current")

hwQinQStackingVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 1, 22)
)
hwQinQStackingVlanCfgGroup.setObjects(
      *(("HUAWEI-QINQ-MIB", "hwQinQStackingVlanCfgVlanId"),
        ("HUAWEI-QINQ-MIB", "hwQinQStackingVlanCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwQinQStackingVlanCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwQinQCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 116, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwQinQCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-QINQ-MIB",
    **{"BpduIndex": BpduIndex,
       "hwQinQ": hwQinQ,
       "hwQinQSystemBase": hwQinQSystemBase,
       "hwQinQSystemWellKnowMac": hwQinQSystemWellKnowMac,
       "hwQinQSystemBridgeRole": hwQinQSystemBridgeRole,
       "hwBpduSystemDropPacketSta": hwBpduSystemDropPacketSta,
       "hwQinQSystemEtherType": hwQinQSystemEtherType,
       "hwQinQMngObjects": hwQinQMngObjects,
       "hwQinQBpduTunnelTable": hwQinQBpduTunnelTable,
       "hwQinQBpduTunnelEntry": hwQinQBpduTunnelEntry,
       "hwQinQBpduTunnelIndex": hwQinQBpduTunnelIndex,
       "hwQinQEtherEncpsType": hwQinQEtherEncpsType,
       "hwQinQBpduTunnelEnableOneQBpduTunnel": hwQinQBpduTunnelEnableOneQBpduTunnel,
       "hwQinQBpduTunnelEnableBpduTag": hwQinQBpduTunnelEnableBpduTag,
       "hwQinQBpduTunnelEnableTwoQBpduTunnel": hwQinQBpduTunnelEnableTwoQBpduTunnel,
       "hwQinQBpduTunnelCustomerBpduTag": hwQinQBpduTunnelCustomerBpduTag,
       "hwQinQBpduTunnelCustomerBpduTagListLow": hwQinQBpduTunnelCustomerBpduTagListLow,
       "hwQinQBpduTunnelCustomerBpduTagListHigh": hwQinQBpduTunnelCustomerBpduTagListHigh,
       "hwQinQRemarkOuterTpid": hwQinQRemarkOuterTpid,
       "hwQinQBpduTunnelEnableBpduFilter": hwQinQBpduTunnelEnableBpduFilter,
       "hwQinQSubIfVlanStackingTable": hwQinQSubIfVlanStackingTable,
       "hwQinQSubIfVlanStackingEntry": hwQinQSubIfVlanStackingEntry,
       "hwQinQSubIfStackingIfIndex": hwQinQSubIfStackingIfIndex,
       "hwQinQSubIfStackingCEVlanStart": hwQinQSubIfStackingCEVlanStart,
       "hwQinQSubIfStackingCEVlanEnd": hwQinQSubIfStackingCEVlanEnd,
       "hwQinQSubIfStackGroupId": hwQinQSubIfStackGroupId,
       "hwQinQSubIfStackingRowStatus": hwQinQSubIfStackingRowStatus,
       "hwQinQSubIfStackingPEVlan": hwQinQSubIfStackingPEVlan,
       "hwQinQSubIfStackingStatTable": hwQinQSubIfStackingStatTable,
       "hwQinQSubIfStackingStatEntry": hwQinQSubIfStackingStatEntry,
       "hwQinQSubIfStackingStatIfIndex": hwQinQSubIfStackingStatIfIndex,
       "hwQinQSubIfStackingStatCEVlan": hwQinQSubIfStackingStatCEVlan,
       "hwQinQSubIfStackStatGroupId": hwQinQSubIfStackStatGroupId,
       "hwQinQSubIfStackingStatOutPackets": hwQinQSubIfStackingStatOutPackets,
       "hwQinQSubIfStackingStatOutBytes": hwQinQSubIfStackingStatOutBytes,
       "hwQinQSubIfStackingStatInPackets": hwQinQSubIfStackingStatInPackets,
       "hwQinQSubIfStackingStatInBytes": hwQinQSubIfStackingStatInBytes,
       "hwQinQSubIfStackStatOutBdPackets": hwQinQSubIfStackStatOutBdPackets,
       "hwQinQSubIfStackStatInBdPackets": hwQinQSubIfStackStatInBdPackets,
       "hwQinQSubIfStackStatOutMuPackets": hwQinQSubIfStackStatOutMuPackets,
       "hwQinQSubIfStackStatInMuPackets": hwQinQSubIfStackStatInMuPackets,
       "hwQinQSubIfStackStatOutUniPackets": hwQinQSubIfStackStatOutUniPackets,
       "hwQinQSubIfStackStatInUniPackets": hwQinQSubIfStackStatInUniPackets,
       "hwQinQSubIfTermTable": hwQinQSubIfTermTable,
       "hwQinQSubIfTermEntry": hwQinQSubIfTermEntry,
       "hwQinQSubIfTermIfIndex": hwQinQSubIfTermIfIndex,
       "hwQinQSubIfTermPEVlan": hwQinQSubIfTermPEVlan,
       "hwQinQSubIfTermCEVlanStart": hwQinQSubIfTermCEVlanStart,
       "hwQinQSubIfTermCEVlanEnd": hwQinQSubIfTermCEVlanEnd,
       "hwQinQSubIfTermGroupId": hwQinQSubIfTermGroupId,
       "hwQinQSubIfTermRowStatus": hwQinQSubIfTermRowStatus,
       "hwQinQSubIfTermStatTable": hwQinQSubIfTermStatTable,
       "hwQinQSubIfTermStatEntry": hwQinQSubIfTermStatEntry,
       "hwQinQSubIfTermStatIfIndex": hwQinQSubIfTermStatIfIndex,
       "hwQinQSubIfTermStatPEVlan": hwQinQSubIfTermStatPEVlan,
       "hwQinQSubIfTermStatCEVlan": hwQinQSubIfTermStatCEVlan,
       "hwQinQSubIfTermStatGroupId": hwQinQSubIfTermStatGroupId,
       "hwQinQSubIfTermStatOutPackets": hwQinQSubIfTermStatOutPackets,
       "hwQinQSubIfTermStatOutBytes": hwQinQSubIfTermStatOutBytes,
       "hwQinQSubIfTermStatInPackets": hwQinQSubIfTermStatInPackets,
       "hwQinQSubIfTermStatInBytes": hwQinQSubIfTermStatInBytes,
       "hwQinQSubIfTermStatOutBdPackets": hwQinQSubIfTermStatOutBdPackets,
       "hwQinQSubIfTermStatInBdPackets": hwQinQSubIfTermStatInBdPackets,
       "hwQinQSubIfTermStatOutMuPackets": hwQinQSubIfTermStatOutMuPackets,
       "hwQinQSubIfTermStatInMuPackets": hwQinQSubIfTermStatInMuPackets,
       "hwQinQSubIfTermStatOutUniPackets": hwQinQSubIfTermStatOutUniPackets,
       "hwQinQSubIfTermStatInUniPackets": hwQinQSubIfTermStatInUniPackets,
       "hwQinQStaticARPCfgTable": hwQinQStaticARPCfgTable,
       "hwQinQStaticARPCfgEntry": hwQinQStaticARPCfgEntry,
       "hwQinQStaticARPCfgIfIndex": hwQinQStaticARPCfgIfIndex,
       "hwQinQStaticARPCfgIp": hwQinQStaticARPCfgIp,
       "hwQinQStaticARPCfgMac": hwQinQStaticARPCfgMac,
       "hwQinQStaticARPCfgVlan": hwQinQStaticARPCfgVlan,
       "hwQinQStaticARPCfgCEVlan": hwQinQStaticARPCfgCEVlan,
       "hwQinQStaticARPCfgRowStatus": hwQinQStaticARPCfgRowStatus,
       "hwQinQStaticMACCfgTable": hwQinQStaticMACCfgTable,
       "hwQinQStaticMACCfgEntry": hwQinQStaticMACCfgEntry,
       "hwQinQStaticMACCfgMac": hwQinQStaticMACCfgMac,
       "hwQinQStaticMACCfgVlan": hwQinQStaticMACCfgVlan,
       "hwQinQStaticMACCfgVsiName": hwQinQStaticMACCfgVsiName,
       "hwQinQStaticMACCfgPEVlan": hwQinQStaticMACCfgPEVlan,
       "hwQinQStaticMACCfgCEVlan": hwQinQStaticMACCfgCEVlan,
       "hwQinQStaticMACCfgType": hwQinQStaticMACCfgType,
       "hwQinQStaticMACCfgIfIndex": hwQinQStaticMACCfgIfIndex,
       "hwQinQStaticMACCfgFlag": hwQinQStaticMACCfgFlag,
       "hwQinQStaticMACCfgRowStatus": hwQinQStaticMACCfgRowStatus,
       "hwQinQSubIfDot1qTermTable": hwQinQSubIfDot1qTermTable,
       "hwQinQSubIfDot1qTermEntry": hwQinQSubIfDot1qTermEntry,
       "hwQinQSubIfDot1qTermIfIndex": hwQinQSubIfDot1qTermIfIndex,
       "hwQinQSubIfDot1qTermVidStart": hwQinQSubIfDot1qTermVidStart,
       "hwQinQSubIfDot1qTermVidEnd": hwQinQSubIfDot1qTermVidEnd,
       "hwQinQSubIfDot1qTermGroupId": hwQinQSubIfDot1qTermGroupId,
       "hwQinQSubIfDot1qTermRowStatus": hwQinQSubIfDot1qTermRowStatus,
       "hwQinQSubIfDot1qTermStatTable": hwQinQSubIfDot1qTermStatTable,
       "hwQinQSubIfDot1qTermStatEntry": hwQinQSubIfDot1qTermStatEntry,
       "hwQinQSubIfDot1qTermStatIfIndex": hwQinQSubIfDot1qTermStatIfIndex,
       "hwQinQSubIfDot1qTermStatCEVlan": hwQinQSubIfDot1qTermStatCEVlan,
       "hwQinQSubIfDot1qTermStatGroupId": hwQinQSubIfDot1qTermStatGroupId,
       "hwQinQSubIfDot1qTermStatOutPackets": hwQinQSubIfDot1qTermStatOutPackets,
       "hwQinQSubIfDot1qTermStatOutBytes": hwQinQSubIfDot1qTermStatOutBytes,
       "hwQinQSubIfDot1qTermStatInPackets": hwQinQSubIfDot1qTermStatInPackets,
       "hwQinQSubIfDot1qTermStatInBytes": hwQinQSubIfDot1qTermStatInBytes,
       "hwQinQSubIfDot1qTermStatOutBdPackets": hwQinQSubIfDot1qTermStatOutBdPackets,
       "hwQinQSubIfDot1qTermStatInBdPackets": hwQinQSubIfDot1qTermStatInBdPackets,
       "hwQinQSubIfDot1qTermStatOutMuPackets": hwQinQSubIfDot1qTermStatOutMuPackets,
       "hwQinQSubIfDot1qTermStatInMuPackets": hwQinQSubIfDot1qTermStatInMuPackets,
       "hwQinQSubIfDot1qTermStatOutUniPackets": hwQinQSubIfDot1qTermStatOutUniPackets,
       "hwQinQSubIfDot1qTermStatInUniPackets": hwQinQSubIfDot1qTermStatInUniPackets,
       "hwQinQModeCfgTable": hwQinQModeCfgTable,
       "hwQinQModeCfgEntry": hwQinQModeCfgEntry,
       "hwQinQModeCfgIfIndex": hwQinQModeCfgIfIndex,
       "hwQinQModeCfgMode": hwQinQModeCfgMode,
       "hwQinQEtherType": hwQinQEtherType,
       "hwQinQCeEtherType": hwQinQCeEtherType,
       "hwQinQCtrlVlanCfgTable": hwQinQCtrlVlanCfgTable,
       "hwQinQCtrlVlanCfgEntry": hwQinQCtrlVlanCfgEntry,
       "hwQinQCtrlVlanCfgIfIndex": hwQinQCtrlVlanCfgIfIndex,
       "hwQinQCtrlVlan": hwQinQCtrlVlan,
       "hwQinQSubIfType": hwQinQSubIfType,
       "hwQinQCtrlVlanFlag": hwQinQCtrlVlanFlag,
       "hwQinQCtrlVlanRowStatus": hwQinQCtrlVlanRowStatus,
       "hwQinQFlexibleFlag": hwQinQFlexibleFlag,
       "hwQinQGroupCfgTable": hwQinQGroupCfgTable,
       "hwQinQGroupCfgEntry": hwQinQGroupCfgEntry,
       "hwQinQGroupCfgIfIndex": hwQinQGroupCfgIfIndex,
       "hwQinQGroupId": hwQinQGroupId,
       "hwQinQGroupType": hwQinQGroupType,
       "hwQinQGroupStat": hwQinQGroupStat,
       "hwQinQGroupRowStatus": hwQinQGroupRowStatus,
       "hwQinQAsymmetryCfgTable": hwQinQAsymmetryCfgTable,
       "hwQinQAsymmetryCfgEntry": hwQinQAsymmetryCfgEntry,
       "hwQinQAsymmetryCfgIfIndex": hwQinQAsymmetryCfgIfIndex,
       "hwQinQSubIfAsymmetry": hwQinQSubIfAsymmetry,
       "hwQinQAsymmetryUserMode": hwQinQAsymmetryUserMode,
       "hwQinQRemarkCfgTable": hwQinQRemarkCfgTable,
       "hwQinQRemarkCfgEntry": hwQinQRemarkCfgEntry,
       "hwQinQRemarkCfgIfIndex": hwQinQRemarkCfgIfIndex,
       "hwQinQPriorityRemark": hwQinQPriorityRemark,
       "hwBpduTunnelIngressTable": hwBpduTunnelIngressTable,
       "hwBpduTunnelIngressEntry": hwBpduTunnelIngressEntry,
       "hwBpduTunnelIngressPortIndex": hwBpduTunnelIngressPortIndex,
       "hwBpduTunnelBpduIngressMacIndex": hwBpduTunnelBpduIngressMacIndex,
       "hwBpduTunnelIngressAddress": hwBpduTunnelIngressAddress,
       "hwBpduTunnelIngressRowStatus": hwBpduTunnelIngressRowStatus,
       "hwBpduTunnelEgressTable": hwBpduTunnelEgressTable,
       "hwBpduTunnelEgressEntry": hwBpduTunnelEgressEntry,
       "hwBpduTunnelEgressPortIndex": hwBpduTunnelEgressPortIndex,
       "hwBpduTunnelBpduEgressMacIndex": hwBpduTunnelBpduEgressMacIndex,
       "hwBpduTunnelEgressAddress": hwBpduTunnelEgressAddress,
       "hwBpduTunnelEgressRowStatus": hwBpduTunnelEgressRowStatus,
       "hwBpduTunnelVlanTable": hwBpduTunnelVlanTable,
       "hwBpduTunnelVlanEntry": hwBpduTunnelVlanEntry,
       "hwBpduTunnelPortIndex": hwBpduTunnelPortIndex,
       "hwBpduTunnelEnable": hwBpduTunnelEnable,
       "hwBpduTunnelVlanListLow": hwBpduTunnelVlanListLow,
       "hwBpduTunnelVlanListHigh": hwBpduTunnelVlanListHigh,
       "hwBpduTunnelTable": hwBpduTunnelTable,
       "hwBpduTunnelEntry": hwBpduTunnelEntry,
       "hwBpduTunnelBpduIndex": hwBpduTunnelBpduIndex,
       "hwBpduTunnelBpduEnable": hwBpduTunnelBpduEnable,
       "hwBpduTunnelMultiAddress": hwBpduTunnelMultiAddress,
       "hwBpduTunnelRowStatus": hwBpduTunnelRowStatus,
       "hwQinQSwapCfgTable": hwQinQSwapCfgTable,
       "hwQinQSwapCfgEntry": hwQinQSwapCfgEntry,
       "hwQinQSwapCfgIfIndex": hwQinQSwapCfgIfIndex,
       "hwQinQSwapCfgFlag": hwQinQSwapCfgFlag,
       "hwQinQSubIfMapTable": hwQinQSubIfMapTable,
       "hwQinQSubIfMapEntry": hwQinQSubIfMapEntry,
       "hwQinQSubIfMapIfIndex": hwQinQSubIfMapIfIndex,
       "hwQinQSubIfPEVlan": hwQinQSubIfPEVlan,
       "hwQinQSubIfCEVlanStart": hwQinQSubIfCEVlanStart,
       "hwQinQSubIfCEVlanEnd": hwQinQSubIfCEVlanEnd,
       "hwQinQSubIfPEVlanMap": hwQinQSubIfPEVlanMap,
       "hwQinQSubIfPEEtherType": hwQinQSubIfPEEtherType,
       "hwQinQSubIfCEVlanMap": hwQinQSubIfCEVlanMap,
       "hwQinQSubIfCEEtherType": hwQinQSubIfCEEtherType,
       "hwQinQSubIfMapGroupId": hwQinQSubIfMapGroupId,
       "hwQinQSubIfMapPe8021p": hwQinQSubIfMapPe8021p,
       "hwQinQSubIfMapCe8021p": hwQinQSubIfMapCe8021p,
       "hwQinQSubIfMapCetoPeFlag": hwQinQSubIfMapCetoPeFlag,
       "hwQinQSubIfMapRowStatus": hwQinQSubIfMapRowStatus,
       "hwQinQStackingVlanCfgTable": hwQinQStackingVlanCfgTable,
       "hwQinQStackingVlanCfgEntry": hwQinQStackingVlanCfgEntry,
       "hwQinQStackingVlanCfgIfIndex": hwQinQStackingVlanCfgIfIndex,
       "hwQinQStackingVlanCfgVlanId": hwQinQStackingVlanCfgVlanId,
       "hwQinQStackingVlanCfgRowStatus": hwQinQStackingVlanCfgRowStatus,
       "hwQinQConformance": hwQinQConformance,
       "hwQinQGroups": hwQinQGroups,
       "hwQinQSystemBaseGroup": hwQinQSystemBaseGroup,
       "hwQinQBpduTunnelGroup": hwQinQBpduTunnelGroup,
       "hwQinQSubIfVlanStackingGroup": hwQinQSubIfVlanStackingGroup,
       "hwQinQSubIfStackingStatGroup": hwQinQSubIfStackingStatGroup,
       "hwQinQSubIfTermGroup": hwQinQSubIfTermGroup,
       "hwQinQSubIfTermStatGroup": hwQinQSubIfTermStatGroup,
       "hwQinQStaticARPCfgGroup": hwQinQStaticARPCfgGroup,
       "hwQinQStaticMACCfgGroup": hwQinQStaticMACCfgGroup,
       "hwQinQSubIfDot1qTermGroup": hwQinQSubIfDot1qTermGroup,
       "hwQinQSubIfDot1qTermStatGroup": hwQinQSubIfDot1qTermStatGroup,
       "hwQinQModeCfgGroup": hwQinQModeCfgGroup,
       "hwQinQCtrlVlanCfgGroup": hwQinQCtrlVlanCfgGroup,
       "hwQinQGroupCfgGroup": hwQinQGroupCfgGroup,
       "hwQinQAsymmetryCfgGroup": hwQinQAsymmetryCfgGroup,
       "hwQinQRemarkCfgGroup": hwQinQRemarkCfgGroup,
       "hwBpduTunnelIngressGroup": hwBpduTunnelIngressGroup,
       "hwBpduTunnelEgressGroup": hwBpduTunnelEgressGroup,
       "hwBpduTunnelVlanGroup": hwBpduTunnelVlanGroup,
       "hwBpduTunnelGroup": hwBpduTunnelGroup,
       "hwQinQSwapCfgGroup": hwQinQSwapCfgGroup,
       "hwQinQSubIfMapGroup": hwQinQSubIfMapGroup,
       "hwQinQStackingVlanCfgGroup": hwQinQStackingVlanCfgGroup,
       "hwQinQCompliances": hwQinQCompliances,
       "hwQinQCompliance": hwQinQCompliance}
)
