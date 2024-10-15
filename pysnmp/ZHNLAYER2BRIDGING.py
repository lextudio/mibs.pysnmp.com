# SNMP MIB module (ZHNLAYER2BRIDGING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNLAYER2BRIDGING
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:58 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhnLayer2Bridging = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42)
)
zhnLayer2Bridging.setRevisions(
        ("2012-07-11 12:00",
         "2012-06-21 12:00",
         "2012-06-05 12:00",
         "2012-05-16 12:00",
         "2012-01-26 12:00",
         "2011-01-11 00:00",
         "2010-08-10 00:00",
         "2010-04-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeEntryStatusValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class VlanTypeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class VlanSecureType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class VlanIDType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class BridgingIntfTypeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VlanTLSMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("sTag", 1),
          ("unknown", 2))
    )



class VlanTLSServiceTags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sTag8100", 2),
          ("sTag88A8", 3),
          ("sTag9100", 4),
          ("sTag9200", 5),
          ("sTag9300", 6))
    )



class VlanQOSMethods(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Layer2BridgingObjects_ObjectIdentity = ObjectIdentity
layer2BridgingObjects = _Layer2BridgingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1)
)
_MaxBridgeEntries_Type = Unsigned32
_MaxBridgeEntries_Object = MibScalar
maxBridgeEntries = _MaxBridgeEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 1),
    _MaxBridgeEntries_Type()
)
maxBridgeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBridgeEntries.setStatus("current")
_MaxFilterEntries_Type = Unsigned32
_MaxFilterEntries_Object = MibScalar
maxFilterEntries = _MaxFilterEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 2),
    _MaxFilterEntries_Type()
)
maxFilterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFilterEntries.setStatus("current")
_MaxMarkingEntries_Type = Unsigned32
_MaxMarkingEntries_Object = MibScalar
maxMarkingEntries = _MaxMarkingEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 3),
    _MaxMarkingEntries_Type()
)
maxMarkingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxMarkingEntries.setStatus("current")
_BridgeNumberOfEntries_Type = Unsigned32
_BridgeNumberOfEntries_Object = MibScalar
bridgeNumberOfEntries = _BridgeNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 4),
    _BridgeNumberOfEntries_Type()
)
bridgeNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNumberOfEntries.setStatus("current")
_FilterNumberOfEntries_Type = Unsigned32
_FilterNumberOfEntries_Object = MibScalar
filterNumberOfEntries = _FilterNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 5),
    _FilterNumberOfEntries_Type()
)
filterNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterNumberOfEntries.setStatus("current")
_MarkingNumberOfEntries_Type = Unsigned32
_MarkingNumberOfEntries_Object = MibScalar
markingNumberOfEntries = _MarkingNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 6),
    _MarkingNumberOfEntries_Type()
)
markingNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markingNumberOfEntries.setStatus("current")
_AvailableInterfaceNumberOfEntries_Type = Unsigned32
_AvailableInterfaceNumberOfEntries_Object = MibScalar
availableInterfaceNumberOfEntries = _AvailableInterfaceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 7),
    _AvailableInterfaceNumberOfEntries_Type()
)
availableInterfaceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableInterfaceNumberOfEntries.setStatus("current")
_BridgeTable_Object = MibTable
bridgeTable = _BridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8)
)
if mibBuilder.loadTexts:
    bridgeTable.setStatus("current")
_BridgeEntry_Object = MibTableRow
bridgeEntry = _BridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1)
)
bridgeEntry.setIndexNames(
    (0, "ZHNLAYER2BRIDGING", "bridgeKey"),
)
if mibBuilder.loadTexts:
    bridgeEntry.setStatus("current")


class _BridgeKey_Type(Unsigned32):
    """Custom type bridgeKey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_BridgeKey_Type.__name__ = "Unsigned32"
_BridgeKey_Object = MibTableColumn
bridgeKey = _BridgeKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 1),
    _BridgeKey_Type()
)
bridgeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeKey.setStatus("current")
_BridgeEnable_Type = TruthValue
_BridgeEnable_Object = MibTableColumn
bridgeEnable = _BridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 2),
    _BridgeEnable_Type()
)
bridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEnable.setStatus("current")
_BridgeStatus_Type = BridgeEntryStatusValues
_BridgeStatus_Object = MibTableColumn
bridgeStatus = _BridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 3),
    _BridgeStatus_Type()
)
bridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatus.setStatus("current")
_BridgeName_Type = OctetString
_BridgeName_Object = MibTableColumn
bridgeName = _BridgeName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 4),
    _BridgeName_Type()
)
bridgeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeName.setStatus("current")


class _VlanID_Type(Unsigned32):
    """Custom type vlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VlanID_Type.__name__ = "Unsigned32"
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 5),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")
_VlanType_Type = VlanTypeValues
_VlanType_Object = MibTableColumn
vlanType = _VlanType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 6),
    _VlanType_Type()
)
vlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanType.setStatus("current")
_SecureVlan_Type = VlanSecureType
_SecureVlan_Object = MibTableColumn
secureVlan = _SecureVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 7),
    _SecureVlan_Type()
)
secureVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureVlan.setStatus("current")
_BridgeTableRowStatus_Type = ZhoneRowStatus
_BridgeTableRowStatus_Object = MibTableColumn
bridgeTableRowStatus = _BridgeTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 8, 1, 8),
    _BridgeTableRowStatus_Type()
)
bridgeTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTableRowStatus.setStatus("current")
_FilterBridgeTable_Object = MibTable
filterBridgeTable = _FilterBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9)
)
if mibBuilder.loadTexts:
    filterBridgeTable.setStatus("current")
_FilterBridgeEntry_Object = MibTableRow
filterBridgeEntry = _FilterBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1)
)
filterBridgeEntry.setIndexNames(
    (0, "ZHNLAYER2BRIDGING", "filterKey"),
    (0, "ZHNLAYER2BRIDGING", "filterBridgeReference"),
)
if mibBuilder.loadTexts:
    filterBridgeEntry.setStatus("current")


class _FilterKey_Type(Unsigned32):
    """Custom type filterKey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FilterKey_Type.__name__ = "Unsigned32"
_FilterKey_Object = MibTableColumn
filterKey = _FilterKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 1),
    _FilterKey_Type()
)
filterKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterKey.setStatus("current")
_FilterEnable_Type = TruthValue
_FilterEnable_Object = MibTableColumn
filterEnable = _FilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 2),
    _FilterEnable_Type()
)
filterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterEnable.setStatus("current")
_ZhnFilterStatus_Type = BridgeEntryStatusValues
_ZhnFilterStatus_Object = MibTableColumn
zhnFilterStatus = _ZhnFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 3),
    _ZhnFilterStatus_Type()
)
zhnFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnFilterStatus.setStatus("current")
_FilterBridgeReference_Type = Unsigned32
_FilterBridgeReference_Object = MibTableColumn
filterBridgeReference = _FilterBridgeReference_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 4),
    _FilterBridgeReference_Type()
)
filterBridgeReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterBridgeReference.setStatus("current")
_FilterInterface_Type = OctetString
_FilterInterface_Object = MibTableColumn
filterInterface = _FilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 5),
    _FilterInterface_Type()
)
filterInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterInterface.setStatus("current")
_SourceMACFromVendorClassIDFilter_Type = OctetString
_SourceMACFromVendorClassIDFilter_Object = MibTableColumn
sourceMACFromVendorClassIDFilter = _SourceMACFromVendorClassIDFilter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 6),
    _SourceMACFromVendorClassIDFilter_Type()
)
sourceMACFromVendorClassIDFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceMACFromVendorClassIDFilter.setStatus("current")
_SourceMACFromVendorClassIDFilterExclude_Type = TruthValue
_SourceMACFromVendorClassIDFilterExclude_Object = MibTableColumn
sourceMACFromVendorClassIDFilterExclude = _SourceMACFromVendorClassIDFilterExclude_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 7),
    _SourceMACFromVendorClassIDFilterExclude_Type()
)
sourceMACFromVendorClassIDFilterExclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceMACFromVendorClassIDFilterExclude.setStatus("current")
_BridgeFilterRowStatus_Type = ZhoneRowStatus
_BridgeFilterRowStatus_Object = MibTableColumn
bridgeFilterRowStatus = _BridgeFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 9, 1, 8),
    _BridgeFilterRowStatus_Type()
)
bridgeFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeFilterRowStatus.setStatus("current")
_MarkingTable_Object = MibTable
markingTable = _MarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10)
)
if mibBuilder.loadTexts:
    markingTable.setStatus("current")
_MarkingEntry_Object = MibTableRow
markingEntry = _MarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1)
)
markingEntry.setIndexNames(
    (0, "ZHNLAYER2BRIDGING", "markingKey"),
    (0, "ZHNLAYER2BRIDGING", "markingBridgeReference"),
)
if mibBuilder.loadTexts:
    markingEntry.setStatus("current")


class _MarkingKey_Type(Unsigned32):
    """Custom type markingKey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MarkingKey_Type.__name__ = "Unsigned32"
_MarkingKey_Object = MibTableColumn
markingKey = _MarkingKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 1),
    _MarkingKey_Type()
)
markingKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markingKey.setStatus("current")
_MarkingEnable_Type = TruthValue
_MarkingEnable_Object = MibTableColumn
markingEnable = _MarkingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 2),
    _MarkingEnable_Type()
)
markingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    markingEnable.setStatus("current")
_MarkingStatus_Type = BridgeEntryStatusValues
_MarkingStatus_Object = MibTableColumn
markingStatus = _MarkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 3),
    _MarkingStatus_Type()
)
markingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markingStatus.setStatus("current")
_MarkingBridgeReference_Type = Unsigned32
_MarkingBridgeReference_Object = MibTableColumn
markingBridgeReference = _MarkingBridgeReference_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 4),
    _MarkingBridgeReference_Type()
)
markingBridgeReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markingBridgeReference.setStatus("current")
_MarkingInterface_Type = OctetString
_MarkingInterface_Object = MibTableColumn
markingInterface = _MarkingInterface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 5),
    _MarkingInterface_Type()
)
markingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    markingInterface.setStatus("current")
_VlanIDUntag_Type = TruthValue
_VlanIDUntag_Object = MibTableColumn
vlanIDUntag = _VlanIDUntag_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 6),
    _VlanIDUntag_Type()
)
vlanIDUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIDUntag.setStatus("current")


class _VlanIDMark_Type(Integer32):
    """Custom type vlanIDMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_VlanIDMark_Type.__name__ = "Integer32"
_VlanIDMark_Object = MibTableColumn
vlanIDMark = _VlanIDMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 7),
    _VlanIDMark_Type()
)
vlanIDMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIDMark.setStatus("current")


class _EthernetPriorityMark_Type(Integer32):
    """Custom type ethernetPriorityMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_EthernetPriorityMark_Type.__name__ = "Integer32"
_EthernetPriorityMark_Object = MibTableColumn
ethernetPriorityMark = _EthernetPriorityMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 8),
    _EthernetPriorityMark_Type()
)
ethernetPriorityMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPriorityMark.setStatus("current")
_EthernetPriorityOverride_Type = TruthValue
_EthernetPriorityOverride_Object = MibTableColumn
ethernetPriorityOverride = _EthernetPriorityOverride_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 9),
    _EthernetPriorityOverride_Type()
)
ethernetPriorityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPriorityOverride.setStatus("current")
_VlanIDType_Type = VlanIDType
_VlanIDType_Object = MibTableColumn
vlanIDType = _VlanIDType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 10),
    _VlanIDType_Type()
)
vlanIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIDType.setStatus("current")
_BridgeMarkingRowStatus_Type = ZhoneRowStatus
_BridgeMarkingRowStatus_Object = MibTableColumn
bridgeMarkingRowStatus = _BridgeMarkingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 10, 1, 11),
    _BridgeMarkingRowStatus_Type()
)
bridgeMarkingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMarkingRowStatus.setStatus("current")
_AvailableInterfaceTable_Object = MibTable
availableInterfaceTable = _AvailableInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 11)
)
if mibBuilder.loadTexts:
    availableInterfaceTable.setStatus("current")
_AvailableInterfaceEntry_Object = MibTableRow
availableInterfaceEntry = _AvailableInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 11, 1)
)
availableInterfaceEntry.setIndexNames(
    (0, "ZHNLAYER2BRIDGING", "availableInterfaceKey"),
)
if mibBuilder.loadTexts:
    availableInterfaceEntry.setStatus("current")


class _AvailableInterfaceKey_Type(Unsigned32):
    """Custom type availableInterfaceKey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AvailableInterfaceKey_Type.__name__ = "Unsigned32"
_AvailableInterfaceKey_Object = MibTableColumn
availableInterfaceKey = _AvailableInterfaceKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 11, 1, 1),
    _AvailableInterfaceKey_Type()
)
availableInterfaceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availableInterfaceKey.setStatus("current")
_InterfaceType_Type = BridgingIntfTypeValues
_InterfaceType_Object = MibTableColumn
interfaceType = _InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 11, 1, 2),
    _InterfaceType_Type()
)
interfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceType.setStatus("current")
_InterfaceReference_Type = OctetString
_InterfaceReference_Object = MibTableColumn
interfaceReference = _InterfaceReference_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 11, 1, 3),
    _InterfaceReference_Type()
)
interfaceReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceReference.setStatus("current")
_AvailableInterfaceRowStatus_Type = ZhoneRowStatus
_AvailableInterfaceRowStatus_Object = MibTableColumn
availableInterfaceRowStatus = _AvailableInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 11, 1, 4),
    _AvailableInterfaceRowStatus_Type()
)
availableInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    availableInterfaceRowStatus.setStatus("current")
_VlanPortMembershipTable_Object = MibTable
vlanPortMembershipTable = _VlanPortMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 12)
)
if mibBuilder.loadTexts:
    vlanPortMembershipTable.setStatus("current")
_VlanPortMembershipEntry_Object = MibTableRow
vlanPortMembershipEntry = _VlanPortMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 12, 1)
)
vlanPortMembershipEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHNLAYER2BRIDGING", "vlanPortVlanID"),
)
if mibBuilder.loadTexts:
    vlanPortMembershipEntry.setStatus("current")
_VlanPort_Type = OctetString
_VlanPort_Object = MibTableColumn
vlanPort = _VlanPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 12, 1, 1),
    _VlanPort_Type()
)
vlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPort.setStatus("current")
_VlanPortVlanID_Type = Unsigned32
_VlanPortVlanID_Object = MibTableColumn
vlanPortVlanID = _VlanPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 12, 1, 2),
    _VlanPortVlanID_Type()
)
vlanPortVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortVlanID.setStatus("current")
_VlanPortMembershipType_Type = VlanIDType
_VlanPortMembershipType_Object = MibTableColumn
vlanPortMembershipType = _VlanPortMembershipType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 12, 1, 3),
    _VlanPortMembershipType_Type()
)
vlanPortMembershipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMembershipType.setStatus("current")
_VlanPortMembershipAction_Type = ZhoneRowStatus
_VlanPortMembershipAction_Object = MibTableColumn
vlanPortMembershipAction = _VlanPortMembershipAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 12, 1, 4),
    _VlanPortMembershipAction_Type()
)
vlanPortMembershipAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMembershipAction.setStatus("current")
_Layer2BridgingGlobalObjects_ObjectIdentity = ObjectIdentity
layer2BridgingGlobalObjects = _Layer2BridgingGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 13)
)
_VlanTLSMode_Type = VlanTLSMode
_VlanTLSMode_Object = MibScalar
vlanTLSMode = _VlanTLSMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 13, 1),
    _VlanTLSMode_Type()
)
vlanTLSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTLSMode.setStatus("current")
_VlanServiceTagTPID_Type = VlanTLSServiceTags
_VlanServiceTagTPID_Object = MibScalar
vlanServiceTagTPID = _VlanServiceTagTPID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 13, 2),
    _VlanServiceTagTPID_Type()
)
vlanServiceTagTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanServiceTagTPID.setStatus("current")
_VlanRouteAcrossVlans_Type = TruthValue
_VlanRouteAcrossVlans_Object = MibScalar
vlanRouteAcrossVlans = _VlanRouteAcrossVlans_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 13, 3),
    _VlanRouteAcrossVlans_Type()
)
vlanRouteAcrossVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanRouteAcrossVlans.setStatus("current")
_VlanQOSMethod_Type = VlanQOSMethods
_VlanQOSMethod_Object = MibScalar
vlanQOSMethod = _VlanQOSMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 1, 13, 4),
    _VlanQOSMethod_Type()
)
vlanQOSMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanQOSMethod.setStatus("current")
_ZhnLayer2BridgeConformance_ObjectIdentity = ObjectIdentity
zhnLayer2BridgeConformance = _ZhnLayer2BridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2)
)
_ZhnLayer2BridgeGroups_ObjectIdentity = ObjectIdentity
zhnLayer2BridgeGroups = _ZhnLayer2BridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1)
)
_ZhnLayer2BridgeCompliances_ObjectIdentity = ObjectIdentity
zhnLayer2BridgeCompliances = _ZhnLayer2BridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 2)
)

# Managed Objects groups

zhnBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1, 1)
)
zhnBridgeGroup.setObjects(
      *(("ZHNLAYER2BRIDGING", "maxBridgeEntries"),
        ("ZHNLAYER2BRIDGING", "maxFilterEntries"),
        ("ZHNLAYER2BRIDGING", "maxMarkingEntries"),
        ("ZHNLAYER2BRIDGING", "bridgeNumberOfEntries"),
        ("ZHNLAYER2BRIDGING", "filterNumberOfEntries"),
        ("ZHNLAYER2BRIDGING", "markingNumberOfEntries"),
        ("ZHNLAYER2BRIDGING", "availableInterfaceNumberOfEntries"))
)
if mibBuilder.loadTexts:
    zhnBridgeGroup.setStatus("current")

zhnBridgeTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1, 2)
)
zhnBridgeTableGroup.setObjects(
      *(("ZHNLAYER2BRIDGING", "bridgeKey"),
        ("ZHNLAYER2BRIDGING", "bridgeEnable"),
        ("ZHNLAYER2BRIDGING", "bridgeStatus"),
        ("ZHNLAYER2BRIDGING", "bridgeName"),
        ("ZHNLAYER2BRIDGING", "vlanID"),
        ("ZHNLAYER2BRIDGING", "vlanType"),
        ("ZHNLAYER2BRIDGING", "secureVlan"),
        ("ZHNLAYER2BRIDGING", "bridgeTableRowStatus"))
)
if mibBuilder.loadTexts:
    zhnBridgeTableGroup.setStatus("current")

zhnFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1, 3)
)
zhnFilterGroup.setObjects(
      *(("ZHNLAYER2BRIDGING", "filterKey"),
        ("ZHNLAYER2BRIDGING", "filterEnable"),
        ("ZHNLAYER2BRIDGING", "zhnFilterStatus"),
        ("ZHNLAYER2BRIDGING", "filterBridgeReference"),
        ("ZHNLAYER2BRIDGING", "filterInterface"),
        ("ZHNLAYER2BRIDGING", "sourceMACFromVendorClassIDFilter"),
        ("ZHNLAYER2BRIDGING", "sourceMACFromVendorClassIDFilterExclude"),
        ("ZHNLAYER2BRIDGING", "bridgeFilterRowStatus"))
)
if mibBuilder.loadTexts:
    zhnFilterGroup.setStatus("current")

zhnBridgeMarkingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1, 4)
)
zhnBridgeMarkingTableGroup.setObjects(
      *(("ZHNLAYER2BRIDGING", "markingKey"),
        ("ZHNLAYER2BRIDGING", "markingEnable"),
        ("ZHNLAYER2BRIDGING", "markingStatus"),
        ("ZHNLAYER2BRIDGING", "markingBridgeReference"),
        ("ZHNLAYER2BRIDGING", "markingInterface"),
        ("ZHNLAYER2BRIDGING", "vlanIDUntag"),
        ("ZHNLAYER2BRIDGING", "vlanIDMark"),
        ("ZHNLAYER2BRIDGING", "ethernetPriorityMark"),
        ("ZHNLAYER2BRIDGING", "ethernetPriorityOverride"),
        ("ZHNLAYER2BRIDGING", "vlanIDType"),
        ("ZHNLAYER2BRIDGING", "bridgeMarkingRowStatus"))
)
if mibBuilder.loadTexts:
    zhnBridgeMarkingTableGroup.setStatus("current")

zhnBridgeAvailableInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1, 5)
)
zhnBridgeAvailableInterfaceGroup.setObjects(
      *(("ZHNLAYER2BRIDGING", "availableInterfaceKey"),
        ("ZHNLAYER2BRIDGING", "interfaceType"),
        ("ZHNLAYER2BRIDGING", "interfaceReference"),
        ("ZHNLAYER2BRIDGING", "availableInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    zhnBridgeAvailableInterfaceGroup.setStatus("current")

zhnPortMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1, 6)
)
zhnPortMembershipGroup.setObjects(
      *(("ZHNLAYER2BRIDGING", "vlanPort"),
        ("ZHNLAYER2BRIDGING", "vlanPortVlanID"),
        ("ZHNLAYER2BRIDGING", "vlanPortMembershipType"),
        ("ZHNLAYER2BRIDGING", "vlanPortMembershipAction"))
)
if mibBuilder.loadTexts:
    zhnPortMembershipGroup.setStatus("current")

zhnVlanGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 1, 7)
)
zhnVlanGlobalGroup.setObjects(
      *(("ZHNLAYER2BRIDGING", "vlanTLSMode"),
        ("ZHNLAYER2BRIDGING", "vlanServiceTagTPID"),
        ("ZHNLAYER2BRIDGING", "vlanRouteAcrossVlans"),
        ("ZHNLAYER2BRIDGING", "vlanQOSMethod"))
)
if mibBuilder.loadTexts:
    zhnVlanGlobalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnLayer2BridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnLayer2BridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNLAYER2BRIDGING",
    **{"BridgeEntryStatusValues": BridgeEntryStatusValues,
       "VlanTypeValues": VlanTypeValues,
       "VlanSecureType": VlanSecureType,
       "VlanIDType": VlanIDType,
       "BridgingIntfTypeValues": BridgingIntfTypeValues,
       "VlanTLSMode": VlanTLSMode,
       "VlanTLSServiceTags": VlanTLSServiceTags,
       "VlanQOSMethods": VlanQOSMethods,
       "zhnLayer2Bridging": zhnLayer2Bridging,
       "layer2BridgingObjects": layer2BridgingObjects,
       "maxBridgeEntries": maxBridgeEntries,
       "maxFilterEntries": maxFilterEntries,
       "maxMarkingEntries": maxMarkingEntries,
       "bridgeNumberOfEntries": bridgeNumberOfEntries,
       "filterNumberOfEntries": filterNumberOfEntries,
       "markingNumberOfEntries": markingNumberOfEntries,
       "availableInterfaceNumberOfEntries": availableInterfaceNumberOfEntries,
       "bridgeTable": bridgeTable,
       "bridgeEntry": bridgeEntry,
       "bridgeKey": bridgeKey,
       "bridgeEnable": bridgeEnable,
       "bridgeStatus": bridgeStatus,
       "bridgeName": bridgeName,
       "vlanID": vlanID,
       "vlanType": vlanType,
       "secureVlan": secureVlan,
       "bridgeTableRowStatus": bridgeTableRowStatus,
       "filterBridgeTable": filterBridgeTable,
       "filterBridgeEntry": filterBridgeEntry,
       "filterKey": filterKey,
       "filterEnable": filterEnable,
       "zhnFilterStatus": zhnFilterStatus,
       "filterBridgeReference": filterBridgeReference,
       "filterInterface": filterInterface,
       "sourceMACFromVendorClassIDFilter": sourceMACFromVendorClassIDFilter,
       "sourceMACFromVendorClassIDFilterExclude": sourceMACFromVendorClassIDFilterExclude,
       "bridgeFilterRowStatus": bridgeFilterRowStatus,
       "markingTable": markingTable,
       "markingEntry": markingEntry,
       "markingKey": markingKey,
       "markingEnable": markingEnable,
       "markingStatus": markingStatus,
       "markingBridgeReference": markingBridgeReference,
       "markingInterface": markingInterface,
       "vlanIDUntag": vlanIDUntag,
       "vlanIDMark": vlanIDMark,
       "ethernetPriorityMark": ethernetPriorityMark,
       "ethernetPriorityOverride": ethernetPriorityOverride,
       "vlanIDType": vlanIDType,
       "bridgeMarkingRowStatus": bridgeMarkingRowStatus,
       "availableInterfaceTable": availableInterfaceTable,
       "availableInterfaceEntry": availableInterfaceEntry,
       "availableInterfaceKey": availableInterfaceKey,
       "interfaceType": interfaceType,
       "interfaceReference": interfaceReference,
       "availableInterfaceRowStatus": availableInterfaceRowStatus,
       "vlanPortMembershipTable": vlanPortMembershipTable,
       "vlanPortMembershipEntry": vlanPortMembershipEntry,
       "vlanPort": vlanPort,
       "vlanPortVlanID": vlanPortVlanID,
       "vlanPortMembershipType": vlanPortMembershipType,
       "vlanPortMembershipAction": vlanPortMembershipAction,
       "layer2BridgingGlobalObjects": layer2BridgingGlobalObjects,
       "vlanTLSMode": vlanTLSMode,
       "vlanServiceTagTPID": vlanServiceTagTPID,
       "vlanRouteAcrossVlans": vlanRouteAcrossVlans,
       "vlanQOSMethod": vlanQOSMethod,
       "zhnLayer2BridgeConformance": zhnLayer2BridgeConformance,
       "zhnLayer2BridgeGroups": zhnLayer2BridgeGroups,
       "zhnBridgeGroup": zhnBridgeGroup,
       "zhnBridgeTableGroup": zhnBridgeTableGroup,
       "zhnFilterGroup": zhnFilterGroup,
       "zhnBridgeMarkingTableGroup": zhnBridgeMarkingTableGroup,
       "zhnBridgeAvailableInterfaceGroup": zhnBridgeAvailableInterfaceGroup,
       "zhnPortMembershipGroup": zhnPortMembershipGroup,
       "zhnVlanGlobalGroup": zhnVlanGlobalGroup,
       "zhnLayer2BridgeCompliances": zhnLayer2BridgeCompliances,
       "zhnLayer2BridgeCompliance": zhnLayer2BridgeCompliance}
)
