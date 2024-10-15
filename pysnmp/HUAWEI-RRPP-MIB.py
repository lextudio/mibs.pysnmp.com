# SNMP MIB module (HUAWEI-RRPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-RRPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:48 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifName")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwRrpp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113)
)
hwRrpp.setRevisions(
        ("2015-03-23 00:00",
         "2013-09-07 00:00",
         "2013-06-17 00:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_HwRrppScalarGroup_ObjectIdentity = ObjectIdentity
hwRrppScalarGroup = _HwRrppScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 1)
)
_HwRrppEnableStatus_Type = EnabledStatus
_HwRrppEnableStatus_Object = MibScalar
hwRrppEnableStatus = _HwRrppEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 1, 1),
    _HwRrppEnableStatus_Type()
)
hwRrppEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRrppEnableStatus.setStatus("current")
_HwRrppLinkupDelayTime_Type = Integer32
_HwRrppLinkupDelayTime_Object = MibScalar
hwRrppLinkupDelayTime = _HwRrppLinkupDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 1, 2),
    _HwRrppLinkupDelayTime_Type()
)
hwRrppLinkupDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRrppLinkupDelayTime.setStatus("current")
_HwRrppTable_ObjectIdentity = ObjectIdentity
hwRrppTable = _HwRrppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2)
)
_HwRrppDomainTable_Object = MibTable
hwRrppDomainTable = _HwRrppDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1)
)
if mibBuilder.loadTexts:
    hwRrppDomainTable.setStatus("current")
_HwRrppDomainEntry_Object = MibTableRow
hwRrppDomainEntry = _HwRrppDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1)
)
hwRrppDomainEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppDomainID"),
)
if mibBuilder.loadTexts:
    hwRrppDomainEntry.setStatus("current")
_HwRrppDomainID_Type = Integer32
_HwRrppDomainID_Object = MibTableColumn
hwRrppDomainID = _HwRrppDomainID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 1),
    _HwRrppDomainID_Type()
)
hwRrppDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppDomainID.setStatus("current")


class _HwRrppDomainControlVlanID_Type(Integer32):
    """Custom type hwRrppDomainControlVlanID based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
        ValueRangeConstraint(65535, 65535),
    )


_HwRrppDomainControlVlanID_Type.__name__ = "Integer32"
_HwRrppDomainControlVlanID_Object = MibTableColumn
hwRrppDomainControlVlanID = _HwRrppDomainControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 2),
    _HwRrppDomainControlVlanID_Type()
)
hwRrppDomainControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppDomainControlVlanID.setStatus("current")


class _HwRrppDomainHelloTime_Type(Integer32):
    """Custom type hwRrppDomainHelloTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwRrppDomainHelloTime_Type.__name__ = "Integer32"
_HwRrppDomainHelloTime_Object = MibTableColumn
hwRrppDomainHelloTime = _HwRrppDomainHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 3),
    _HwRrppDomainHelloTime_Type()
)
hwRrppDomainHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppDomainHelloTime.setStatus("current")
_HwRrppDomainFailTime_Type = Integer32
_HwRrppDomainFailTime_Object = MibTableColumn
hwRrppDomainFailTime = _HwRrppDomainFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 4),
    _HwRrppDomainFailTime_Type()
)
hwRrppDomainFailTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppDomainFailTime.setStatus("current")
_HwRrppDomainRowStatus_Type = RowStatus
_HwRrppDomainRowStatus_Object = MibTableColumn
hwRrppDomainRowStatus = _HwRrppDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 5),
    _HwRrppDomainRowStatus_Type()
)
hwRrppDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppDomainRowStatus.setStatus("current")


class _HwRrppDomainResetStatistics_Type(Integer32):
    """Custom type hwRrppDomainResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("unused", 2))
    )


_HwRrppDomainResetStatistics_Type.__name__ = "Integer32"
_HwRrppDomainResetStatistics_Object = MibTableColumn
hwRrppDomainResetStatistics = _HwRrppDomainResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 6),
    _HwRrppDomainResetStatistics_Type()
)
hwRrppDomainResetStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppDomainResetStatistics.setStatus("current")
_HwRrppMulSubRingProtection_Type = EnabledStatus
_HwRrppMulSubRingProtection_Object = MibTableColumn
hwRrppMulSubRingProtection = _HwRrppMulSubRingProtection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 7),
    _HwRrppMulSubRingProtection_Type()
)
hwRrppMulSubRingProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppMulSubRingProtection.setStatus("current")


class _HwRrppDomainProtectedVlan_Type(OctetString):
    """Custom type hwRrppDomainProtectedVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_HwRrppDomainProtectedVlan_Type.__name__ = "OctetString"
_HwRrppDomainProtectedVlan_Object = MibTableColumn
hwRrppDomainProtectedVlan = _HwRrppDomainProtectedVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 8),
    _HwRrppDomainProtectedVlan_Type()
)
hwRrppDomainProtectedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppDomainProtectedVlan.setStatus("current")


class _HwRrppDomainDescription_Type(OctetString):
    """Custom type hwRrppDomainDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwRrppDomainDescription_Type.__name__ = "OctetString"
_HwRrppDomainDescription_Object = MibTableColumn
hwRrppDomainDescription = _HwRrppDomainDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 1, 1, 9),
    _HwRrppDomainDescription_Type()
)
hwRrppDomainDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppDomainDescription.setStatus("current")
_HwRrppRingTable_Object = MibTable
hwRrppRingTable = _HwRrppRingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2)
)
if mibBuilder.loadTexts:
    hwRrppRingTable.setStatus("current")
_HwRrppRingEntry_Object = MibTableRow
hwRrppRingEntry = _HwRrppRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1)
)
hwRrppRingEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppDomainID"),
    (0, "HUAWEI-RRPP-MIB", "hwRrppRingID"),
)
if mibBuilder.loadTexts:
    hwRrppRingEntry.setStatus("current")
_HwRrppRingID_Type = Integer32
_HwRrppRingID_Object = MibTableColumn
hwRrppRingID = _HwRrppRingID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 1),
    _HwRrppRingID_Type()
)
hwRrppRingID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppRingID.setStatus("current")
_HwRrppRingEnableStatus_Type = EnabledStatus
_HwRrppRingEnableStatus_Object = MibTableColumn
hwRrppRingEnableStatus = _HwRrppRingEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 2),
    _HwRrppRingEnableStatus_Type()
)
hwRrppRingEnableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingEnableStatus.setStatus("current")


class _HwRrppRingActive_Type(Integer32):
    """Custom type hwRrppRingActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HwRrppRingActive_Type.__name__ = "Integer32"
_HwRrppRingActive_Object = MibTableColumn
hwRrppRingActive = _HwRrppRingActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 3),
    _HwRrppRingActive_Type()
)
hwRrppRingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppRingActive.setStatus("current")


class _HwRrppRingState_Type(Integer32):
    """Custom type hwRrppRingState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("complete", 4),
          ("failed", 5),
          ("fault", 3),
          ("health", 2),
          ("linkdown", 7),
          ("linkdownnotify", 10),
          ("linkup", 6),
          ("linkupnotify", 9),
          ("preforwarding", 8),
          ("preforwardnotify", 11),
          ("unknown", 1))
    )


_HwRrppRingState_Type.__name__ = "Integer32"
_HwRrppRingState_Object = MibTableColumn
hwRrppRingState = _HwRrppRingState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 4),
    _HwRrppRingState_Type()
)
hwRrppRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppRingState.setStatus("current")


class _HwRrppRingNodeMode_Type(Integer32):
    """Custom type hwRrppRingNodeMode based on Integer32"""
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
        *(("assistantEdge", 4),
          ("edge", 3),
          ("master", 1),
          ("transit", 2))
    )


_HwRrppRingNodeMode_Type.__name__ = "Integer32"
_HwRrppRingNodeMode_Object = MibTableColumn
hwRrppRingNodeMode = _HwRrppRingNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 5),
    _HwRrppRingNodeMode_Type()
)
hwRrppRingNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingNodeMode.setStatus("current")
_HwRrppRingPrimaryPort_Type = InterfaceIndex
_HwRrppRingPrimaryPort_Object = MibTableColumn
hwRrppRingPrimaryPort = _HwRrppRingPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 6),
    _HwRrppRingPrimaryPort_Type()
)
hwRrppRingPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingPrimaryPort.setStatus("current")
_HwRrppRingSecondaryPort_Type = InterfaceIndex
_HwRrppRingSecondaryPort_Object = MibTableColumn
hwRrppRingSecondaryPort = _HwRrppRingSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 7),
    _HwRrppRingSecondaryPort_Type()
)
hwRrppRingSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingSecondaryPort.setStatus("current")


class _HwRrppRingLevel_Type(Integer32):
    """Custom type hwRrppRingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("majorRing", 0),
          ("subRing", 1))
    )


_HwRrppRingLevel_Type.__name__ = "Integer32"
_HwRrppRingLevel_Object = MibTableColumn
hwRrppRingLevel = _HwRrppRingLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 8),
    _HwRrppRingLevel_Type()
)
hwRrppRingLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingLevel.setStatus("current")
_HwRrppRingRowStatus_Type = RowStatus
_HwRrppRingRowStatus_Object = MibTableColumn
hwRrppRingRowStatus = _HwRrppRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 9),
    _HwRrppRingRowStatus_Type()
)
hwRrppRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingRowStatus.setStatus("current")


class _HwRrppRingResetStatistics_Type(Integer32):
    """Custom type hwRrppRingResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("unused", 2))
    )


_HwRrppRingResetStatistics_Type.__name__ = "Integer32"
_HwRrppRingResetStatistics_Object = MibTableColumn
hwRrppRingResetStatistics = _HwRrppRingResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 2, 1, 10),
    _HwRrppRingResetStatistics_Type()
)
hwRrppRingResetStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingResetStatistics.setStatus("current")
_HwRrppPortTable_Object = MibTable
hwRrppPortTable = _HwRrppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3)
)
if mibBuilder.loadTexts:
    hwRrppPortTable.setStatus("current")
_HwRrppPortEntry_Object = MibTableRow
hwRrppPortEntry = _HwRrppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1)
)
hwRrppPortEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppDomainID"),
    (0, "HUAWEI-RRPP-MIB", "hwRrppRingID"),
    (0, "HUAWEI-RRPP-MIB", "hwRrppPortID"),
)
if mibBuilder.loadTexts:
    hwRrppPortEntry.setStatus("current")
_HwRrppPortID_Type = InterfaceIndex
_HwRrppPortID_Object = MibTableColumn
hwRrppPortID = _HwRrppPortID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 1),
    _HwRrppPortID_Type()
)
hwRrppPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppPortID.setStatus("current")


class _HwRrppPortType_Type(Integer32):
    """Custom type hwRrppPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ethtrunk", 4),
          ("fe", 1),
          ("ge", 2),
          ("ve", 3),
          ("x100ge", 7),
          ("x40ge", 6),
          ("xge", 5))
    )


_HwRrppPortType_Type.__name__ = "Integer32"
_HwRrppPortType_Object = MibTableColumn
hwRrppPortType = _HwRrppPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 2),
    _HwRrppPortType_Type()
)
hwRrppPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortType.setStatus("current")


class _HwRrppPortRole_Type(Integer32):
    """Custom type hwRrppPortRole based on Integer32"""
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
        *(("common", 3),
          ("edge", 4),
          ("primary", 1),
          ("secondary", 2))
    )


_HwRrppPortRole_Type.__name__ = "Integer32"
_HwRrppPortRole_Object = MibTableColumn
hwRrppPortRole = _HwRrppPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 3),
    _HwRrppPortRole_Type()
)
hwRrppPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRole.setStatus("current")


class _HwRrppPortState_Type(Integer32):
    """Custom type hwRrppPortState based on Integer32"""
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
        *(("blocked", 3),
          ("down", 4),
          ("unblocked", 2),
          ("unknown", 1))
    )


_HwRrppPortState_Type.__name__ = "Integer32"
_HwRrppPortState_Object = MibTableColumn
hwRrppPortState = _HwRrppPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 4),
    _HwRrppPortState_Type()
)
hwRrppPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortState.setStatus("current")
_HwRrppPortRXError_Type = Counter32
_HwRrppPortRXError_Object = MibTableColumn
hwRrppPortRXError = _HwRrppPortRXError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 5),
    _HwRrppPortRXError_Type()
)
hwRrppPortRXError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXError.setStatus("current")
_HwRrppPortRXHello_Type = Counter32
_HwRrppPortRXHello_Object = MibTableColumn
hwRrppPortRXHello = _HwRrppPortRXHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 6),
    _HwRrppPortRXHello_Type()
)
hwRrppPortRXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXHello.setStatus("current")
_HwRrppPortRXLinkUp_Type = Counter32
_HwRrppPortRXLinkUp_Object = MibTableColumn
hwRrppPortRXLinkUp = _HwRrppPortRXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 7),
    _HwRrppPortRXLinkUp_Type()
)
hwRrppPortRXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXLinkUp.setStatus("current")
_HwRrppPortRXLinkDown_Type = Counter32
_HwRrppPortRXLinkDown_Object = MibTableColumn
hwRrppPortRXLinkDown = _HwRrppPortRXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 8),
    _HwRrppPortRXLinkDown_Type()
)
hwRrppPortRXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXLinkDown.setStatus("current")
_HwRrppPortRXCommonFlush_Type = Counter32
_HwRrppPortRXCommonFlush_Object = MibTableColumn
hwRrppPortRXCommonFlush = _HwRrppPortRXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 9),
    _HwRrppPortRXCommonFlush_Type()
)
hwRrppPortRXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXCommonFlush.setStatus("current")
_HwRrppPortRXCompleteFlush_Type = Counter32
_HwRrppPortRXCompleteFlush_Object = MibTableColumn
hwRrppPortRXCompleteFlush = _HwRrppPortRXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 10),
    _HwRrppPortRXCompleteFlush_Type()
)
hwRrppPortRXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXCompleteFlush.setStatus("current")
_HwRrppPortRXEdgeHello_Type = Counter32
_HwRrppPortRXEdgeHello_Object = MibTableColumn
hwRrppPortRXEdgeHello = _HwRrppPortRXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 11),
    _HwRrppPortRXEdgeHello_Type()
)
hwRrppPortRXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXEdgeHello.setStatus("current")
_HwRrppPortRXMajorFault_Type = Counter32
_HwRrppPortRXMajorFault_Object = MibTableColumn
hwRrppPortRXMajorFault = _HwRrppPortRXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 12),
    _HwRrppPortRXMajorFault_Type()
)
hwRrppPortRXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortRXMajorFault.setStatus("current")
_HwRrppPortTXError_Type = Counter32
_HwRrppPortTXError_Object = MibTableColumn
hwRrppPortTXError = _HwRrppPortTXError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 13),
    _HwRrppPortTXError_Type()
)
hwRrppPortTXError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXError.setStatus("current")
_HwRrppPortTXHello_Type = Counter32
_HwRrppPortTXHello_Object = MibTableColumn
hwRrppPortTXHello = _HwRrppPortTXHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 14),
    _HwRrppPortTXHello_Type()
)
hwRrppPortTXHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXHello.setStatus("current")
_HwRrppPortTXLinkUp_Type = Counter32
_HwRrppPortTXLinkUp_Object = MibTableColumn
hwRrppPortTXLinkUp = _HwRrppPortTXLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 15),
    _HwRrppPortTXLinkUp_Type()
)
hwRrppPortTXLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXLinkUp.setStatus("current")
_HwRrppPortTXLinkDown_Type = Counter32
_HwRrppPortTXLinkDown_Object = MibTableColumn
hwRrppPortTXLinkDown = _HwRrppPortTXLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 16),
    _HwRrppPortTXLinkDown_Type()
)
hwRrppPortTXLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXLinkDown.setStatus("current")
_HwRrppPortTXCommonFlush_Type = Counter32
_HwRrppPortTXCommonFlush_Object = MibTableColumn
hwRrppPortTXCommonFlush = _HwRrppPortTXCommonFlush_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 17),
    _HwRrppPortTXCommonFlush_Type()
)
hwRrppPortTXCommonFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXCommonFlush.setStatus("current")
_HwRrppPortTXCompleteFlush_Type = Counter32
_HwRrppPortTXCompleteFlush_Object = MibTableColumn
hwRrppPortTXCompleteFlush = _HwRrppPortTXCompleteFlush_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 18),
    _HwRrppPortTXCompleteFlush_Type()
)
hwRrppPortTXCompleteFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXCompleteFlush.setStatus("current")
_HwRrppPortTXEdgeHello_Type = Counter32
_HwRrppPortTXEdgeHello_Object = MibTableColumn
hwRrppPortTXEdgeHello = _HwRrppPortTXEdgeHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 19),
    _HwRrppPortTXEdgeHello_Type()
)
hwRrppPortTXEdgeHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXEdgeHello.setStatus("current")
_HwRrppPortTXMajorFault_Type = Counter32
_HwRrppPortTXMajorFault_Object = MibTableColumn
hwRrppPortTXMajorFault = _HwRrppPortTXMajorFault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 3, 1, 20),
    _HwRrppPortTXMajorFault_Type()
)
hwRrppPortTXMajorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppPortTXMajorFault.setStatus("current")
_HwRrppTrackInterfaceTable_Object = MibTable
hwRrppTrackInterfaceTable = _HwRrppTrackInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 4)
)
if mibBuilder.loadTexts:
    hwRrppTrackInterfaceTable.setStatus("current")
_HwRrppTrackInterfaceEntry_Object = MibTableRow
hwRrppTrackInterfaceEntry = _HwRrppTrackInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 4, 1)
)
hwRrppTrackInterfaceEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppDomainID"),
    (0, "HUAWEI-RRPP-MIB", "hwRrppRingID"),
    (0, "HUAWEI-RRPP-MIB", "hwRrppTrackInterfaceID"),
)
if mibBuilder.loadTexts:
    hwRrppTrackInterfaceEntry.setStatus("current")
_HwRrppTrackInterfaceID_Type = InterfaceIndex
_HwRrppTrackInterfaceID_Object = MibTableColumn
hwRrppTrackInterfaceID = _HwRrppTrackInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 4, 1, 1),
    _HwRrppTrackInterfaceID_Type()
)
hwRrppTrackInterfaceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppTrackInterfaceID.setStatus("current")
_HwRrppTrackRowStatus_Type = RowStatus
_HwRrppTrackRowStatus_Object = MibTableColumn
hwRrppTrackRowStatus = _HwRrppTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 4, 1, 2),
    _HwRrppTrackRowStatus_Type()
)
hwRrppTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppTrackRowStatus.setStatus("current")
_HwRrppRingGroupTable_Object = MibTable
hwRrppRingGroupTable = _HwRrppRingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 5)
)
if mibBuilder.loadTexts:
    hwRrppRingGroupTable.setStatus("current")
_HwRrppRingGroupEntry_Object = MibTableRow
hwRrppRingGroupEntry = _HwRrppRingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 5, 1)
)
hwRrppRingGroupEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppRingGroupID"),
)
if mibBuilder.loadTexts:
    hwRrppRingGroupEntry.setStatus("current")
_HwRrppRingGroupID_Type = Integer32
_HwRrppRingGroupID_Object = MibTableColumn
hwRrppRingGroupID = _HwRrppRingGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 5, 1, 1),
    _HwRrppRingGroupID_Type()
)
hwRrppRingGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppRingGroupID.setStatus("current")
_HwRrppRingGroupRowStatus_Type = RowStatus
_HwRrppRingGroupRowStatus_Object = MibTableColumn
hwRrppRingGroupRowStatus = _HwRrppRingGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 5, 1, 2),
    _HwRrppRingGroupRowStatus_Type()
)
hwRrppRingGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingGroupRowStatus.setStatus("current")
_HwRrppRingGroupMemberTable_Object = MibTable
hwRrppRingGroupMemberTable = _HwRrppRingGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 6)
)
if mibBuilder.loadTexts:
    hwRrppRingGroupMemberTable.setStatus("current")
_HwRrppRingGroupMemberEntry_Object = MibTableRow
hwRrppRingGroupMemberEntry = _HwRrppRingGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 6, 1)
)
hwRrppRingGroupMemberEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppRingGroupID"),
    (0, "HUAWEI-RRPP-MIB", "hwRrppRingGroupMemberDomainID"),
    (0, "HUAWEI-RRPP-MIB", "hwRrppRingGroupMemberRingID"),
)
if mibBuilder.loadTexts:
    hwRrppRingGroupMemberEntry.setStatus("current")
_HwRrppRingGroupMemberDomainID_Type = Integer32
_HwRrppRingGroupMemberDomainID_Object = MibTableColumn
hwRrppRingGroupMemberDomainID = _HwRrppRingGroupMemberDomainID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 6, 1, 1),
    _HwRrppRingGroupMemberDomainID_Type()
)
hwRrppRingGroupMemberDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppRingGroupMemberDomainID.setStatus("current")
_HwRrppRingGroupMemberRingID_Type = Integer32
_HwRrppRingGroupMemberRingID_Object = MibTableColumn
hwRrppRingGroupMemberRingID = _HwRrppRingGroupMemberRingID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 6, 1, 2),
    _HwRrppRingGroupMemberRingID_Type()
)
hwRrppRingGroupMemberRingID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppRingGroupMemberRingID.setStatus("current")
_HwRrppRingGroupIsEdgeHelloProcess_Type = EnabledStatus
_HwRrppRingGroupIsEdgeHelloProcess_Object = MibTableColumn
hwRrppRingGroupIsEdgeHelloProcess = _HwRrppRingGroupIsEdgeHelloProcess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 6, 1, 3),
    _HwRrppRingGroupIsEdgeHelloProcess_Type()
)
hwRrppRingGroupIsEdgeHelloProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppRingGroupIsEdgeHelloProcess.setStatus("current")
_HwRrppRingGroupMemberRowStatus_Type = RowStatus
_HwRrppRingGroupMemberRowStatus_Object = MibTableColumn
hwRrppRingGroupMemberRowStatus = _HwRrppRingGroupMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 2, 6, 1, 4),
    _HwRrppRingGroupMemberRowStatus_Type()
)
hwRrppRingGroupMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppRingGroupMemberRowStatus.setStatus("current")
_HwRrppSnoopingTable_ObjectIdentity = ObjectIdentity
hwRrppSnoopingTable = _HwRrppSnoopingTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3)
)
_HwRrppSnoopingInterfaceTable_Object = MibTable
hwRrppSnoopingInterfaceTable = _HwRrppSnoopingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1)
)
if mibBuilder.loadTexts:
    hwRrppSnoopingInterfaceTable.setStatus("current")
_HwRrppSnoopingInterfaceEntry_Object = MibTableRow
hwRrppSnoopingInterfaceEntry = _HwRrppSnoopingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1, 1)
)
hwRrppSnoopingInterfaceEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppSnoopingInterfaceId"),
)
if mibBuilder.loadTexts:
    hwRrppSnoopingInterfaceEntry.setStatus("current")
_HwRrppSnoopingInterfaceId_Type = InterfaceIndex
_HwRrppSnoopingInterfaceId_Object = MibTableColumn
hwRrppSnoopingInterfaceId = _HwRrppSnoopingInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1, 1, 1),
    _HwRrppSnoopingInterfaceId_Type()
)
hwRrppSnoopingInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppSnoopingInterfaceId.setStatus("current")
_HwRrppSnoopingVsiName_Type = OctetString
_HwRrppSnoopingVsiName_Object = MibTableColumn
hwRrppSnoopingVsiName = _HwRrppSnoopingVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1, 1, 2),
    _HwRrppSnoopingVsiName_Type()
)
hwRrppSnoopingVsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppSnoopingVsiName.setStatus("current")
_HwRrppSnoopingVlanId_Type = VlanId
_HwRrppSnoopingVlanId_Object = MibTableColumn
hwRrppSnoopingVlanId = _HwRrppSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1, 1, 3),
    _HwRrppSnoopingVlanId_Type()
)
hwRrppSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRrppSnoopingVlanId.setStatus("current")
_HwRrppSnoopingEnableStatus_Type = EnabledStatus
_HwRrppSnoopingEnableStatus_Object = MibTableColumn
hwRrppSnoopingEnableStatus = _HwRrppSnoopingEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1, 1, 4),
    _HwRrppSnoopingEnableStatus_Type()
)
hwRrppSnoopingEnableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppSnoopingEnableStatus.setStatus("current")
_HwRrppSnoopingRowStatus_Type = RowStatus
_HwRrppSnoopingRowStatus_Object = MibTableColumn
hwRrppSnoopingRowStatus = _HwRrppSnoopingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1, 1, 5),
    _HwRrppSnoopingRowStatus_Type()
)
hwRrppSnoopingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppSnoopingRowStatus.setStatus("current")
_HwRrppSnoopingAllVsiStatus_Type = EnabledStatus
_HwRrppSnoopingAllVsiStatus_Object = MibTableColumn
hwRrppSnoopingAllVsiStatus = _HwRrppSnoopingAllVsiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 1, 1, 6),
    _HwRrppSnoopingAllVsiStatus_Type()
)
hwRrppSnoopingAllVsiStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppSnoopingAllVsiStatus.setStatus("current")
_HwRrppSnoopingVsiTable_Object = MibTable
hwRrppSnoopingVsiTable = _HwRrppSnoopingVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 2)
)
if mibBuilder.loadTexts:
    hwRrppSnoopingVsiTable.setStatus("current")
_HwRrppSnoopingVsiEntry_Object = MibTableRow
hwRrppSnoopingVsiEntry = _HwRrppSnoopingVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 2, 1)
)
hwRrppSnoopingVsiEntry.setIndexNames(
    (0, "HUAWEI-RRPP-MIB", "hwRrppSnoopingVsiInterfaceId"),
    (0, "HUAWEI-RRPP-MIB", "hwVsiName"),
)
if mibBuilder.loadTexts:
    hwRrppSnoopingVsiEntry.setStatus("current")
_HwRrppSnoopingVsiInterfaceId_Type = InterfaceIndex
_HwRrppSnoopingVsiInterfaceId_Object = MibTableColumn
hwRrppSnoopingVsiInterfaceId = _HwRrppSnoopingVsiInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 2, 1, 1),
    _HwRrppSnoopingVsiInterfaceId_Type()
)
hwRrppSnoopingVsiInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRrppSnoopingVsiInterfaceId.setStatus("current")


class _HwVsiName_Type(OctetString):
    """Custom type hwVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVsiName_Type.__name__ = "OctetString"
_HwVsiName_Object = MibTableColumn
hwVsiName = _HwVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 2, 1, 2),
    _HwVsiName_Type()
)
hwVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVsiName.setStatus("current")
_HwRrppSnoopingVsiRowStatus_Type = RowStatus
_HwRrppSnoopingVsiRowStatus_Object = MibTableColumn
hwRrppSnoopingVsiRowStatus = _HwRrppSnoopingVsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 3, 2, 1, 3),
    _HwRrppSnoopingVsiRowStatus_Type()
)
hwRrppSnoopingVsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRrppSnoopingVsiRowStatus.setStatus("current")
_HwRrppNotifications_ObjectIdentity = ObjectIdentity
hwRrppNotifications = _HwRrppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 4)
)
_HwRrppMibGroup_ObjectIdentity = ObjectIdentity
hwRrppMibGroup = _HwRrppMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5)
)
_HwRrppConformance_ObjectIdentity = ObjectIdentity
hwRrppConformance = _HwRrppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 6)
)
_HwRrppCompliances_ObjectIdentity = ObjectIdentity
hwRrppCompliances = _HwRrppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 6, 1)
)

# Managed Objects groups

hwRrppGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 1)
)
hwRrppGlobalGroup.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppEnableStatus"),
        ("HUAWEI-RRPP-MIB", "hwRrppLinkupDelayTime"))
)
if mibBuilder.loadTexts:
    hwRrppGlobalGroup.setStatus("current")

hwRrppDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 2)
)
hwRrppDomainGroup.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppDomainControlVlanID"),
        ("HUAWEI-RRPP-MIB", "hwRrppDomainHelloTime"),
        ("HUAWEI-RRPP-MIB", "hwRrppDomainFailTime"),
        ("HUAWEI-RRPP-MIB", "hwRrppDomainRowStatus"),
        ("HUAWEI-RRPP-MIB", "hwRrppDomainResetStatistics"),
        ("HUAWEI-RRPP-MIB", "hwRrppMulSubRingProtection"),
        ("HUAWEI-RRPP-MIB", "hwRrppDomainProtectedVlan"),
        ("HUAWEI-RRPP-MIB", "hwRrppDomainDescription"))
)
if mibBuilder.loadTexts:
    hwRrppDomainGroup.setStatus("current")

hwRrppRingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 3)
)
hwRrppRingGroup.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppRingEnableStatus"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingActive"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingState"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingNodeMode"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingPrimaryPort"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingSecondaryPort"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingLevel"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingRowStatus"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingResetStatistics"))
)
if mibBuilder.loadTexts:
    hwRrppRingGroup.setStatus("current")

hwRrppPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 4)
)
hwRrppPortGroup.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppPortType"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRole"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortState"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXError"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXHello"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXLinkUp"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXLinkDown"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXCommonFlush"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXCompleteFlush"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXEdgeHello"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortRXMajorFault"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXError"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXHello"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXLinkUp"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXLinkDown"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXCommonFlush"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXCompleteFlush"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXEdgeHello"),
        ("HUAWEI-RRPP-MIB", "hwRrppPortTXMajorFault"))
)
if mibBuilder.loadTexts:
    hwRrppPortGroup.setStatus("current")

hwRrppTrackInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 5)
)
hwRrppTrackInterfaceGroup.setObjects(
    ("HUAWEI-RRPP-MIB", "hwRrppTrackRowStatus")
)
if mibBuilder.loadTexts:
    hwRrppTrackInterfaceGroup.setStatus("current")

hwRrppRingGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 6)
)
hwRrppRingGroupGroup.setObjects(
    ("HUAWEI-RRPP-MIB", "hwRrppRingGroupRowStatus")
)
if mibBuilder.loadTexts:
    hwRrppRingGroupGroup.setStatus("current")

hwRrppRingGroupMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 7)
)
hwRrppRingGroupMemberGroup.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppRingGroupIsEdgeHelloProcess"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingGroupMemberRowStatus"))
)
if mibBuilder.loadTexts:
    hwRrppRingGroupMemberGroup.setStatus("current")

hwRrppSnoopingInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 8)
)
hwRrppSnoopingInterfaceGroup.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppSnoopingVsiName"),
        ("HUAWEI-RRPP-MIB", "hwRrppSnoopingVlanId"),
        ("HUAWEI-RRPP-MIB", "hwRrppSnoopingEnableStatus"),
        ("HUAWEI-RRPP-MIB", "hwRrppSnoopingRowStatus"),
        ("HUAWEI-RRPP-MIB", "hwRrppSnoopingAllVsiStatus"))
)
if mibBuilder.loadTexts:
    hwRrppSnoopingInterfaceGroup.setStatus("current")

hwRrppSnoopingVsiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 9)
)
hwRrppSnoopingVsiGroup.setObjects(
    ("HUAWEI-RRPP-MIB", "hwRrppSnoopingVsiRowStatus")
)
if mibBuilder.loadTexts:
    hwRrppSnoopingVsiGroup.setStatus("current")


# Notification objects

hwRrppRingRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 4, 1)
)
hwRrppRingRecover.setObjects(
    ("HUAWEI-RRPP-MIB", "hwRrppRingState")
)
if mibBuilder.loadTexts:
    hwRrppRingRecover.setStatus(
        "current"
    )

hwRrppRingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 4, 2)
)
hwRrppRingFail.setObjects(
    ("HUAWEI-RRPP-MIB", "hwRrppRingState")
)
if mibBuilder.loadTexts:
    hwRrppRingFail.setStatus(
        "current"
    )

hwRrppMultiMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 4, 3)
)
hwRrppMultiMaster.setObjects(
    ("HUAWEI-RRPP-MIB", "hwRrppRingNodeMode")
)
if mibBuilder.loadTexts:
    hwRrppMultiMaster.setStatus(
        "current"
    )

hwRrppTrackInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 4, 4)
)
hwRrppTrackInterfaceDown.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppTrackRowStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwRrppTrackInterfaceDown.setStatus(
        "current"
    )

hwRrppTrackInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 4, 5)
)
hwRrppTrackInterfaceUp.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppTrackRowStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwRrppTrackInterfaceUp.setStatus(
        "current"
    )

hwRrppRingSingleDirectionFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 4, 6)
)
hwRrppRingSingleDirectionFail.setObjects(
    ("HUAWEI-RRPP-MIB", "hwRrppRingState")
)
if mibBuilder.loadTexts:
    hwRrppRingSingleDirectionFail.setStatus(
        "current"
    )


# Notifications groups

hwRrppNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 5, 10)
)
hwRrppNotificationGroup.setObjects(
      *(("HUAWEI-RRPP-MIB", "hwRrppRingRecover"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingFail"),
        ("HUAWEI-RRPP-MIB", "hwRrppMultiMaster"),
        ("HUAWEI-RRPP-MIB", "hwRrppTrackInterfaceDown"),
        ("HUAWEI-RRPP-MIB", "hwRrppTrackInterfaceUp"),
        ("HUAWEI-RRPP-MIB", "hwRrppRingSingleDirectionFail"))
)
if mibBuilder.loadTexts:
    hwRrppNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwRrppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 113, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwRrppCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-RRPP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hwRrpp": hwRrpp,
       "hwRrppScalarGroup": hwRrppScalarGroup,
       "hwRrppEnableStatus": hwRrppEnableStatus,
       "hwRrppLinkupDelayTime": hwRrppLinkupDelayTime,
       "hwRrppTable": hwRrppTable,
       "hwRrppDomainTable": hwRrppDomainTable,
       "hwRrppDomainEntry": hwRrppDomainEntry,
       "hwRrppDomainID": hwRrppDomainID,
       "hwRrppDomainControlVlanID": hwRrppDomainControlVlanID,
       "hwRrppDomainHelloTime": hwRrppDomainHelloTime,
       "hwRrppDomainFailTime": hwRrppDomainFailTime,
       "hwRrppDomainRowStatus": hwRrppDomainRowStatus,
       "hwRrppDomainResetStatistics": hwRrppDomainResetStatistics,
       "hwRrppMulSubRingProtection": hwRrppMulSubRingProtection,
       "hwRrppDomainProtectedVlan": hwRrppDomainProtectedVlan,
       "hwRrppDomainDescription": hwRrppDomainDescription,
       "hwRrppRingTable": hwRrppRingTable,
       "hwRrppRingEntry": hwRrppRingEntry,
       "hwRrppRingID": hwRrppRingID,
       "hwRrppRingEnableStatus": hwRrppRingEnableStatus,
       "hwRrppRingActive": hwRrppRingActive,
       "hwRrppRingState": hwRrppRingState,
       "hwRrppRingNodeMode": hwRrppRingNodeMode,
       "hwRrppRingPrimaryPort": hwRrppRingPrimaryPort,
       "hwRrppRingSecondaryPort": hwRrppRingSecondaryPort,
       "hwRrppRingLevel": hwRrppRingLevel,
       "hwRrppRingRowStatus": hwRrppRingRowStatus,
       "hwRrppRingResetStatistics": hwRrppRingResetStatistics,
       "hwRrppPortTable": hwRrppPortTable,
       "hwRrppPortEntry": hwRrppPortEntry,
       "hwRrppPortID": hwRrppPortID,
       "hwRrppPortType": hwRrppPortType,
       "hwRrppPortRole": hwRrppPortRole,
       "hwRrppPortState": hwRrppPortState,
       "hwRrppPortRXError": hwRrppPortRXError,
       "hwRrppPortRXHello": hwRrppPortRXHello,
       "hwRrppPortRXLinkUp": hwRrppPortRXLinkUp,
       "hwRrppPortRXLinkDown": hwRrppPortRXLinkDown,
       "hwRrppPortRXCommonFlush": hwRrppPortRXCommonFlush,
       "hwRrppPortRXCompleteFlush": hwRrppPortRXCompleteFlush,
       "hwRrppPortRXEdgeHello": hwRrppPortRXEdgeHello,
       "hwRrppPortRXMajorFault": hwRrppPortRXMajorFault,
       "hwRrppPortTXError": hwRrppPortTXError,
       "hwRrppPortTXHello": hwRrppPortTXHello,
       "hwRrppPortTXLinkUp": hwRrppPortTXLinkUp,
       "hwRrppPortTXLinkDown": hwRrppPortTXLinkDown,
       "hwRrppPortTXCommonFlush": hwRrppPortTXCommonFlush,
       "hwRrppPortTXCompleteFlush": hwRrppPortTXCompleteFlush,
       "hwRrppPortTXEdgeHello": hwRrppPortTXEdgeHello,
       "hwRrppPortTXMajorFault": hwRrppPortTXMajorFault,
       "hwRrppTrackInterfaceTable": hwRrppTrackInterfaceTable,
       "hwRrppTrackInterfaceEntry": hwRrppTrackInterfaceEntry,
       "hwRrppTrackInterfaceID": hwRrppTrackInterfaceID,
       "hwRrppTrackRowStatus": hwRrppTrackRowStatus,
       "hwRrppRingGroupTable": hwRrppRingGroupTable,
       "hwRrppRingGroupEntry": hwRrppRingGroupEntry,
       "hwRrppRingGroupID": hwRrppRingGroupID,
       "hwRrppRingGroupRowStatus": hwRrppRingGroupRowStatus,
       "hwRrppRingGroupMemberTable": hwRrppRingGroupMemberTable,
       "hwRrppRingGroupMemberEntry": hwRrppRingGroupMemberEntry,
       "hwRrppRingGroupMemberDomainID": hwRrppRingGroupMemberDomainID,
       "hwRrppRingGroupMemberRingID": hwRrppRingGroupMemberRingID,
       "hwRrppRingGroupIsEdgeHelloProcess": hwRrppRingGroupIsEdgeHelloProcess,
       "hwRrppRingGroupMemberRowStatus": hwRrppRingGroupMemberRowStatus,
       "hwRrppSnoopingTable": hwRrppSnoopingTable,
       "hwRrppSnoopingInterfaceTable": hwRrppSnoopingInterfaceTable,
       "hwRrppSnoopingInterfaceEntry": hwRrppSnoopingInterfaceEntry,
       "hwRrppSnoopingInterfaceId": hwRrppSnoopingInterfaceId,
       "hwRrppSnoopingVsiName": hwRrppSnoopingVsiName,
       "hwRrppSnoopingVlanId": hwRrppSnoopingVlanId,
       "hwRrppSnoopingEnableStatus": hwRrppSnoopingEnableStatus,
       "hwRrppSnoopingRowStatus": hwRrppSnoopingRowStatus,
       "hwRrppSnoopingAllVsiStatus": hwRrppSnoopingAllVsiStatus,
       "hwRrppSnoopingVsiTable": hwRrppSnoopingVsiTable,
       "hwRrppSnoopingVsiEntry": hwRrppSnoopingVsiEntry,
       "hwRrppSnoopingVsiInterfaceId": hwRrppSnoopingVsiInterfaceId,
       "hwVsiName": hwVsiName,
       "hwRrppSnoopingVsiRowStatus": hwRrppSnoopingVsiRowStatus,
       "hwRrppNotifications": hwRrppNotifications,
       "hwRrppRingRecover": hwRrppRingRecover,
       "hwRrppRingFail": hwRrppRingFail,
       "hwRrppMultiMaster": hwRrppMultiMaster,
       "hwRrppTrackInterfaceDown": hwRrppTrackInterfaceDown,
       "hwRrppTrackInterfaceUp": hwRrppTrackInterfaceUp,
       "hwRrppRingSingleDirectionFail": hwRrppRingSingleDirectionFail,
       "hwRrppMibGroup": hwRrppMibGroup,
       "hwRrppGlobalGroup": hwRrppGlobalGroup,
       "hwRrppDomainGroup": hwRrppDomainGroup,
       "hwRrppRingGroup": hwRrppRingGroup,
       "hwRrppPortGroup": hwRrppPortGroup,
       "hwRrppTrackInterfaceGroup": hwRrppTrackInterfaceGroup,
       "hwRrppRingGroupGroup": hwRrppRingGroupGroup,
       "hwRrppRingGroupMemberGroup": hwRrppRingGroupMemberGroup,
       "hwRrppSnoopingInterfaceGroup": hwRrppSnoopingInterfaceGroup,
       "hwRrppSnoopingVsiGroup": hwRrppSnoopingVsiGroup,
       "hwRrppNotificationGroup": hwRrppNotificationGroup,
       "hwRrppConformance": hwRrppConformance,
       "hwRrppCompliances": hwRrppCompliances,
       "hwRrppCompliance": hwRrppCompliance}
)
