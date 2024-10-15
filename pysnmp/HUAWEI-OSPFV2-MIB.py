# SNMP MIB module (HUAWEI-OSPFV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-OSPFV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:25 2024
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

(ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfNbrAddressLessIndex,
 ospfNbrIpAddr,
 ospfNbrRtrId,
 ospfNbrState,
 ospfRouterId) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfNbrAddressLessIndex",
    "ospfNbrIpAddr",
    "ospfNbrRtrId",
    "ospfNbrState",
    "ospfRouterId")

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

hwOspfv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwOspfv2MIBObjects_ObjectIdentity = ObjectIdentity
hwOspfv2MIBObjects = _HwOspfv2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 1)
)


class _HwOspfv2MIBBinding_Type(Integer32):
    """Custom type hwOspfv2MIBBinding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwOspfv2MIBBinding_Type.__name__ = "Integer32"
_HwOspfv2MIBBinding_Object = MibScalar
hwOspfv2MIBBinding = _HwOspfv2MIBBinding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 1, 1),
    _HwOspfv2MIBBinding_Type()
)
hwOspfv2MIBBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv2MIBBinding.setStatus("current")
_HwOspfv2ChangeTable_ObjectIdentity = ObjectIdentity
hwOspfv2ChangeTable = _HwOspfv2ChangeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 2)
)
_HwOspfv2MIBObjectsChange_Type = TimeTicks
_HwOspfv2MIBObjectsChange_Object = MibScalar
hwOspfv2MIBObjectsChange = _HwOspfv2MIBObjectsChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 2, 1),
    _HwOspfv2MIBObjectsChange_Type()
)
hwOspfv2MIBObjectsChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2MIBObjectsChange.setStatus("current")
_HwOspfv2ProcessChange_Type = TimeTicks
_HwOspfv2ProcessChange_Object = MibScalar
hwOspfv2ProcessChange = _HwOspfv2ProcessChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 2, 2),
    _HwOspfv2ProcessChange_Type()
)
hwOspfv2ProcessChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2ProcessChange.setStatus("current")
_HwOspfv2AreaChange_Type = TimeTicks
_HwOspfv2AreaChange_Object = MibScalar
hwOspfv2AreaChange = _HwOspfv2AreaChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 2, 3),
    _HwOspfv2AreaChange_Type()
)
hwOspfv2AreaChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2AreaChange.setStatus("current")
_HwOspfv2NetworkChange_Type = TimeTicks
_HwOspfv2NetworkChange_Object = MibScalar
hwOspfv2NetworkChange = _HwOspfv2NetworkChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 2, 4),
    _HwOspfv2NetworkChange_Type()
)
hwOspfv2NetworkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NetworkChange.setStatus("current")
_HwOspfv2ProcessTable_Object = MibTable
hwOspfv2ProcessTable = _HwOspfv2ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3)
)
if mibBuilder.loadTexts:
    hwOspfv2ProcessTable.setStatus("current")
_HwOspfv2ProcessEntry_Object = MibTableRow
hwOspfv2ProcessEntry = _HwOspfv2ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1)
)
hwOspfv2ProcessEntry.setIndexNames(
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2ProcessIdIndex"),
)
if mibBuilder.loadTexts:
    hwOspfv2ProcessEntry.setStatus("current")


class _HwOspfv2ProcessIdIndex_Type(Integer32):
    """Custom type hwOspfv2ProcessIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwOspfv2ProcessIdIndex_Type.__name__ = "Integer32"
_HwOspfv2ProcessIdIndex_Object = MibTableColumn
hwOspfv2ProcessIdIndex = _HwOspfv2ProcessIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 1),
    _HwOspfv2ProcessIdIndex_Type()
)
hwOspfv2ProcessIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv2ProcessIdIndex.setStatus("current")


class _HwOspfv2VpnName_Type(DisplayString):
    """Custom type hwOspfv2VpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwOspfv2VpnName_Type.__name__ = "DisplayString"
_HwOspfv2VpnName_Object = MibTableColumn
hwOspfv2VpnName = _HwOspfv2VpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 2),
    _HwOspfv2VpnName_Type()
)
hwOspfv2VpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2VpnName.setStatus("current")


class _HwOspfv2ConfigRouterId_Type(IpAddress):
    """Custom type hwOspfv2ConfigRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_HwOspfv2ConfigRouterId_Object = MibTableColumn
hwOspfv2ConfigRouterId = _HwOspfv2ConfigRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 3),
    _HwOspfv2ConfigRouterId_Type()
)
hwOspfv2ConfigRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2ConfigRouterId.setStatus("current")
_HwOspfv2ActualRouterId_Type = IpAddress
_HwOspfv2ActualRouterId_Object = MibTableColumn
hwOspfv2ActualRouterId = _HwOspfv2ActualRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 4),
    _HwOspfv2ActualRouterId_Type()
)
hwOspfv2ActualRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2ActualRouterId.setStatus("current")


class _HwOspfv2BandwidthReference_Type(Unsigned32):
    """Custom type hwOspfv2BandwidthReference based on Unsigned32"""
    defaultValue = 100


_HwOspfv2BandwidthReference_Object = MibTableColumn
hwOspfv2BandwidthReference = _HwOspfv2BandwidthReference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 5),
    _HwOspfv2BandwidthReference_Type()
)
hwOspfv2BandwidthReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2BandwidthReference.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2BandwidthReference.setUnits("Mbit/s")


class _HwOspfv2Description_Type(DisplayString):
    """Custom type hwOspfv2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwOspfv2Description_Type.__name__ = "DisplayString"
_HwOspfv2Description_Object = MibTableColumn
hwOspfv2Description = _HwOspfv2Description_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 6),
    _HwOspfv2Description_Type()
)
hwOspfv2Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2Description.setStatus("current")


class _HwOspfv2LsaArriveIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaArriveIntvl based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10000),
    )


_HwOspfv2LsaArriveIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaArriveIntvl_Object = MibTableColumn
hwOspfv2LsaArriveIntvl = _HwOspfv2LsaArriveIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 7),
    _HwOspfv2LsaArriveIntvl_Type()
)
hwOspfv2LsaArriveIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveIntvl.setUnits("millionSecond")


class _HwOspfv2LsaArriveMaxIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaArriveMaxIntvl based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )


_HwOspfv2LsaArriveMaxIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaArriveMaxIntvl_Object = MibTableColumn
hwOspfv2LsaArriveMaxIntvl = _HwOspfv2LsaArriveMaxIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 8),
    _HwOspfv2LsaArriveMaxIntvl_Type()
)
hwOspfv2LsaArriveMaxIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveMaxIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveMaxIntvl.setUnits("millionSecond")


class _HwOspfv2LsaArriveStartIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaArriveStartIntvl based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000),
    )


_HwOspfv2LsaArriveStartIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaArriveStartIntvl_Object = MibTableColumn
hwOspfv2LsaArriveStartIntvl = _HwOspfv2LsaArriveStartIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 9),
    _HwOspfv2LsaArriveStartIntvl_Type()
)
hwOspfv2LsaArriveStartIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveStartIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveStartIntvl.setUnits("millionSecond")


class _HwOspfv2LsaArriveHoldIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaArriveHoldIntvl based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 5000),
    )


_HwOspfv2LsaArriveHoldIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaArriveHoldIntvl_Object = MibTableColumn
hwOspfv2LsaArriveHoldIntvl = _HwOspfv2LsaArriveHoldIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 10),
    _HwOspfv2LsaArriveHoldIntvl_Type()
)
hwOspfv2LsaArriveHoldIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveHoldIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaArriveHoldIntvl.setUnits("millionSecond")


class _HwOspfv2LsaOrigIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaOrigIntvl based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
    )


_HwOspfv2LsaOrigIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaOrigIntvl_Object = MibTableColumn
hwOspfv2LsaOrigIntvl = _HwOspfv2LsaOrigIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 11),
    _HwOspfv2LsaOrigIntvl_Type()
)
hwOspfv2LsaOrigIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigIntvl.setUnits("millionSecond")


class _HwOspfv2LsaOrigMaxIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaOrigMaxIntvl based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )


_HwOspfv2LsaOrigMaxIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaOrigMaxIntvl_Object = MibTableColumn
hwOspfv2LsaOrigMaxIntvl = _HwOspfv2LsaOrigMaxIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 12),
    _HwOspfv2LsaOrigMaxIntvl_Type()
)
hwOspfv2LsaOrigMaxIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigMaxIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigMaxIntvl.setUnits("millionSecond")


class _HwOspfv2LsaOrigStartIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaOrigStartIntvl based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1000),
    )


_HwOspfv2LsaOrigStartIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaOrigStartIntvl_Object = MibTableColumn
hwOspfv2LsaOrigStartIntvl = _HwOspfv2LsaOrigStartIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 13),
    _HwOspfv2LsaOrigStartIntvl_Type()
)
hwOspfv2LsaOrigStartIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigStartIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigStartIntvl.setUnits("millionSecond")


class _HwOspfv2LsaOrigHoldIntvl_Type(Integer32):
    """Custom type hwOspfv2LsaOrigHoldIntvl based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 5000),
    )


_HwOspfv2LsaOrigHoldIntvl_Type.__name__ = "Integer32"
_HwOspfv2LsaOrigHoldIntvl_Object = MibTableColumn
hwOspfv2LsaOrigHoldIntvl = _HwOspfv2LsaOrigHoldIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 14),
    _HwOspfv2LsaOrigHoldIntvl_Type()
)
hwOspfv2LsaOrigHoldIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigHoldIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigHoldIntvl.setUnits("millionSecond")


class _HwOspfv2LsaOrigIntvlOtherType_Type(Integer32):
    """Custom type hwOspfv2LsaOrigIntvlOtherType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 10),
    )


_HwOspfv2LsaOrigIntvlOtherType_Type.__name__ = "Integer32"
_HwOspfv2LsaOrigIntvlOtherType_Object = MibTableColumn
hwOspfv2LsaOrigIntvlOtherType = _HwOspfv2LsaOrigIntvlOtherType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 15),
    _HwOspfv2LsaOrigIntvlOtherType_Type()
)
hwOspfv2LsaOrigIntvlOtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigIntvlOtherType.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2LsaOrigIntvlOtherType.setUnits("second")


class _HwOspfv2LsdbOverflowLimit_Type(Integer32):
    """Custom type hwOspfv2LsdbOverflowLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwOspfv2LsdbOverflowLimit_Type.__name__ = "Integer32"
_HwOspfv2LsdbOverflowLimit_Object = MibTableColumn
hwOspfv2LsdbOverflowLimit = _HwOspfv2LsdbOverflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 16),
    _HwOspfv2LsdbOverflowLimit_Type()
)
hwOspfv2LsdbOverflowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2LsdbOverflowLimit.setStatus("current")


class _HwOspfv2MaxLoadBalaNumber_Type(Integer32):
    """Custom type hwOspfv2MaxLoadBalaNumber based on Integer32"""
    defaultBinValue = 0


_HwOspfv2MaxLoadBalaNumber_Object = MibTableColumn
hwOspfv2MaxLoadBalaNumber = _HwOspfv2MaxLoadBalaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 17),
    _HwOspfv2MaxLoadBalaNumber_Type()
)
hwOspfv2MaxLoadBalaNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2MaxLoadBalaNumber.setStatus("current")


class _HwOspfv2AseRouteMaxNumber_Type(Integer32):
    """Custom type hwOspfv2AseRouteMaxNumber based on Integer32"""
    defaultValue = 5000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000000),
    )


_HwOspfv2AseRouteMaxNumber_Type.__name__ = "Integer32"
_HwOspfv2AseRouteMaxNumber_Object = MibTableColumn
hwOspfv2AseRouteMaxNumber = _HwOspfv2AseRouteMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 18),
    _HwOspfv2AseRouteMaxNumber_Type()
)
hwOspfv2AseRouteMaxNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AseRouteMaxNumber.setStatus("current")


class _HwOspfv2InterRouteMaxNumber_Type(Integer32):
    """Custom type hwOspfv2InterRouteMaxNumber based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_HwOspfv2InterRouteMaxNumber_Type.__name__ = "Integer32"
_HwOspfv2InterRouteMaxNumber_Object = MibTableColumn
hwOspfv2InterRouteMaxNumber = _HwOspfv2InterRouteMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 19),
    _HwOspfv2InterRouteMaxNumber_Type()
)
hwOspfv2InterRouteMaxNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2InterRouteMaxNumber.setStatus("current")


class _HwOspfv2IntraRouteMaxNumber_Type(Integer32):
    """Custom type hwOspfv2IntraRouteMaxNumber based on Integer32"""
    defaultValue = 100000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_HwOspfv2IntraRouteMaxNumber_Type.__name__ = "Integer32"
_HwOspfv2IntraRouteMaxNumber_Object = MibTableColumn
hwOspfv2IntraRouteMaxNumber = _HwOspfv2IntraRouteMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 20),
    _HwOspfv2IntraRouteMaxNumber_Type()
)
hwOspfv2IntraRouteMaxNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2IntraRouteMaxNumber.setStatus("current")


class _HwOspfv2RetransLimitMaxNumber_Type(Integer32):
    """Custom type hwOspfv2RetransLimitMaxNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 255),
    )


_HwOspfv2RetransLimitMaxNumber_Type.__name__ = "Integer32"
_HwOspfv2RetransLimitMaxNumber_Object = MibTableColumn
hwOspfv2RetransLimitMaxNumber = _HwOspfv2RetransLimitMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 21),
    _HwOspfv2RetransLimitMaxNumber_Type()
)
hwOspfv2RetransLimitMaxNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2RetransLimitMaxNumber.setStatus("current")


class _HwOspfv2Rfc1583Compatibility_Type(TruthValue):
    """Custom type hwOspfv2Rfc1583Compatibility based on TruthValue"""


_HwOspfv2Rfc1583Compatibility_Object = MibTableColumn
hwOspfv2Rfc1583Compatibility = _HwOspfv2Rfc1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 22),
    _HwOspfv2Rfc1583Compatibility_Type()
)
hwOspfv2Rfc1583Compatibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2Rfc1583Compatibility.setStatus("current")


class _HwOspfv2ShamHello_Type(TruthValue):
    """Custom type hwOspfv2ShamHello based on TruthValue"""


_HwOspfv2ShamHello_Object = MibTableColumn
hwOspfv2ShamHello = _HwOspfv2ShamHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 23),
    _HwOspfv2ShamHello_Type()
)
hwOspfv2ShamHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2ShamHello.setStatus("current")


class _HwOspfv2SpfSchIntvlUnit_Type(Integer32):
    """Custom type hwOspfv2SpfSchIntvlUnit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("millionSecond", 2),
          ("none", 3),
          ("second", 1))
    )


_HwOspfv2SpfSchIntvlUnit_Type.__name__ = "Integer32"
_HwOspfv2SpfSchIntvlUnit_Object = MibTableColumn
hwOspfv2SpfSchIntvlUnit = _HwOspfv2SpfSchIntvlUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 24),
    _HwOspfv2SpfSchIntvlUnit_Type()
)
hwOspfv2SpfSchIntvlUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchIntvlUnit.setStatus("current")


class _HwOspfv2SpfSchIntvlNumber_Type(Integer32):
    """Custom type hwOspfv2SpfSchIntvlNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000),
    )


_HwOspfv2SpfSchIntvlNumber_Type.__name__ = "Integer32"
_HwOspfv2SpfSchIntvlNumber_Object = MibTableColumn
hwOspfv2SpfSchIntvlNumber = _HwOspfv2SpfSchIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 25),
    _HwOspfv2SpfSchIntvlNumber_Type()
)
hwOspfv2SpfSchIntvlNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchIntvlNumber.setStatus("current")


class _HwOspfv2SpfSchMaxIntvl_Type(Integer32):
    """Custom type hwOspfv2SpfSchMaxIntvl based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 20000),
    )


_HwOspfv2SpfSchMaxIntvl_Type.__name__ = "Integer32"
_HwOspfv2SpfSchMaxIntvl_Object = MibTableColumn
hwOspfv2SpfSchMaxIntvl = _HwOspfv2SpfSchMaxIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 26),
    _HwOspfv2SpfSchMaxIntvl_Type()
)
hwOspfv2SpfSchMaxIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchMaxIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchMaxIntvl.setUnits("millionSecond")


class _HwOspfv2SpfSchStartIntvl_Type(Integer32):
    """Custom type hwOspfv2SpfSchStartIntvl based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1000),
    )


_HwOspfv2SpfSchStartIntvl_Type.__name__ = "Integer32"
_HwOspfv2SpfSchStartIntvl_Object = MibTableColumn
hwOspfv2SpfSchStartIntvl = _HwOspfv2SpfSchStartIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 27),
    _HwOspfv2SpfSchStartIntvl_Type()
)
hwOspfv2SpfSchStartIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchStartIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchStartIntvl.setUnits("millionSecond")


class _HwOspfv2SpfSchHoldIntvl_Type(Integer32):
    """Custom type hwOspfv2SpfSchHoldIntvl based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 5000),
    )


_HwOspfv2SpfSchHoldIntvl_Type.__name__ = "Integer32"
_HwOspfv2SpfSchHoldIntvl_Object = MibTableColumn
hwOspfv2SpfSchHoldIntvl = _HwOspfv2SpfSchHoldIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 28),
    _HwOspfv2SpfSchHoldIntvl_Type()
)
hwOspfv2SpfSchHoldIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchHoldIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv2SpfSchHoldIntvl.setUnits("millionSecond")


class _HwOspfv2OpaqueCapability_Type(TruthValue):
    """Custom type hwOspfv2OpaqueCapability based on TruthValue"""


_HwOspfv2OpaqueCapability_Object = MibTableColumn
hwOspfv2OpaqueCapability = _HwOspfv2OpaqueCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 29),
    _HwOspfv2OpaqueCapability_Type()
)
hwOspfv2OpaqueCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2OpaqueCapability.setStatus("current")


class _HwOspfv2TrafficAdjustment_Type(TruthValue):
    """Custom type hwOspfv2TrafficAdjustment based on TruthValue"""


_HwOspfv2TrafficAdjustment_Object = MibTableColumn
hwOspfv2TrafficAdjustment = _HwOspfv2TrafficAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 30),
    _HwOspfv2TrafficAdjustment_Type()
)
hwOspfv2TrafficAdjustment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2TrafficAdjustment.setStatus("current")


class _HwOspfv2TrafficAdvertise_Type(TruthValue):
    """Custom type hwOspfv2TrafficAdvertise based on TruthValue"""


_HwOspfv2TrafficAdvertise_Object = MibTableColumn
hwOspfv2TrafficAdvertise = _HwOspfv2TrafficAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 31),
    _HwOspfv2TrafficAdvertise_Type()
)
hwOspfv2TrafficAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2TrafficAdvertise.setStatus("current")


class _HwOspfv2FlushTimer_Type(Integer32):
    """Custom type hwOspfv2FlushTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_HwOspfv2FlushTimer_Type.__name__ = "Integer32"
_HwOspfv2FlushTimer_Object = MibTableColumn
hwOspfv2FlushTimer = _HwOspfv2FlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 32),
    _HwOspfv2FlushTimer_Type()
)
hwOspfv2FlushTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2FlushTimer.setStatus("current")
_HwOspfv2ProcessRowStatus_Type = RowStatus
_HwOspfv2ProcessRowStatus_Object = MibTableColumn
hwOspfv2ProcessRowStatus = _HwOspfv2ProcessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 3, 1, 33),
    _HwOspfv2ProcessRowStatus_Type()
)
hwOspfv2ProcessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2ProcessRowStatus.setStatus("current")
_HwOspfv2AreaTable_Object = MibTable
hwOspfv2AreaTable = _HwOspfv2AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4)
)
if mibBuilder.loadTexts:
    hwOspfv2AreaTable.setStatus("current")
_HwOspfv2AreaEntry_Object = MibTableRow
hwOspfv2AreaEntry = _HwOspfv2AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1)
)
hwOspfv2AreaEntry.setIndexNames(
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2ProcessIdIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2AreaIdIndex"),
)
if mibBuilder.loadTexts:
    hwOspfv2AreaEntry.setStatus("current")
_HwOspfv2AreaIdIndex_Type = IpAddress
_HwOspfv2AreaIdIndex_Object = MibTableColumn
hwOspfv2AreaIdIndex = _HwOspfv2AreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 1),
    _HwOspfv2AreaIdIndex_Type()
)
hwOspfv2AreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv2AreaIdIndex.setStatus("current")


class _HwOspfv2AreaType_Type(Integer32):
    """Custom type hwOspfv2AreaType based on Integer32"""
    defaultValue = 3

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
          ("nssa", 1),
          ("stub", 2))
    )


_HwOspfv2AreaType_Type.__name__ = "Integer32"
_HwOspfv2AreaType_Object = MibTableColumn
hwOspfv2AreaType = _HwOspfv2AreaType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 2),
    _HwOspfv2AreaType_Type()
)
hwOspfv2AreaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaType.setStatus("current")


class _HwOspfv2AreaNoSummary_Type(TruthValue):
    """Custom type hwOspfv2AreaNoSummary based on TruthValue"""


_HwOspfv2AreaNoSummary_Object = MibTableColumn
hwOspfv2AreaNoSummary = _HwOspfv2AreaNoSummary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 3),
    _HwOspfv2AreaNoSummary_Type()
)
hwOspfv2AreaNoSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNoSummary.setStatus("current")


class _HwOspfv2AreaNssaFlushTimer_Type(Integer32):
    """Custom type hwOspfv2AreaNssaFlushTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_HwOspfv2AreaNssaFlushTimer_Type.__name__ = "Integer32"
_HwOspfv2AreaNssaFlushTimer_Object = MibTableColumn
hwOspfv2AreaNssaFlushTimer = _HwOspfv2AreaNssaFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 4),
    _HwOspfv2AreaNssaFlushTimer_Type()
)
hwOspfv2AreaNssaFlushTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaFlushTimer.setStatus("current")


class _HwOspfv2AreaNssaDefAdvertise_Type(TruthValue):
    """Custom type hwOspfv2AreaNssaDefAdvertise based on TruthValue"""


_HwOspfv2AreaNssaDefAdvertise_Object = MibTableColumn
hwOspfv2AreaNssaDefAdvertise = _HwOspfv2AreaNssaDefAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 5),
    _HwOspfv2AreaNssaDefAdvertise_Type()
)
hwOspfv2AreaNssaDefAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaDefAdvertise.setStatus("current")


class _HwOspfv2AreaNssaNoImportRoute_Type(TruthValue):
    """Custom type hwOspfv2AreaNssaNoImportRoute based on TruthValue"""


_HwOspfv2AreaNssaNoImportRoute_Object = MibTableColumn
hwOspfv2AreaNssaNoImportRoute = _HwOspfv2AreaNssaNoImportRoute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 6),
    _HwOspfv2AreaNssaNoImportRoute_Type()
)
hwOspfv2AreaNssaNoImportRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaNoImportRoute.setStatus("current")


class _HwOspfv2AreaNssaTransAlways_Type(TruthValue):
    """Custom type hwOspfv2AreaNssaTransAlways based on TruthValue"""


_HwOspfv2AreaNssaTransAlways_Object = MibTableColumn
hwOspfv2AreaNssaTransAlways = _HwOspfv2AreaNssaTransAlways_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 7),
    _HwOspfv2AreaNssaTransAlways_Type()
)
hwOspfv2AreaNssaTransAlways.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaTransAlways.setStatus("current")


class _HwOspfv2AreaNssaTransTimer_Type(Integer32):
    """Custom type hwOspfv2AreaNssaTransTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwOspfv2AreaNssaTransTimer_Type.__name__ = "Integer32"
_HwOspfv2AreaNssaTransTimer_Object = MibTableColumn
hwOspfv2AreaNssaTransTimer = _HwOspfv2AreaNssaTransTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 8),
    _HwOspfv2AreaNssaTransTimer_Type()
)
hwOspfv2AreaNssaTransTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaTransTimer.setStatus("current")


class _HwOspfv2AreaNssaAllowFaZero_Type(TruthValue):
    """Custom type hwOspfv2AreaNssaAllowFaZero based on TruthValue"""


_HwOspfv2AreaNssaAllowFaZero_Object = MibTableColumn
hwOspfv2AreaNssaAllowFaZero = _HwOspfv2AreaNssaAllowFaZero_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 9),
    _HwOspfv2AreaNssaAllowFaZero_Type()
)
hwOspfv2AreaNssaAllowFaZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaAllowFaZero.setStatus("current")


class _HwOspfv2AreaNssaSuppressFa_Type(TruthValue):
    """Custom type hwOspfv2AreaNssaSuppressFa based on TruthValue"""


_HwOspfv2AreaNssaSuppressFa_Object = MibTableColumn
hwOspfv2AreaNssaSuppressFa = _HwOspfv2AreaNssaSuppressFa_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 10),
    _HwOspfv2AreaNssaSuppressFa_Type()
)
hwOspfv2AreaNssaSuppressFa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaSuppressFa.setStatus("current")


class _HwOspfv2AreaNssaSetNBit_Type(TruthValue):
    """Custom type hwOspfv2AreaNssaSetNBit based on TruthValue"""


_HwOspfv2AreaNssaSetNBit_Object = MibTableColumn
hwOspfv2AreaNssaSetNBit = _HwOspfv2AreaNssaSetNBit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 11),
    _HwOspfv2AreaNssaSetNBit_Type()
)
hwOspfv2AreaNssaSetNBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaNssaSetNBit.setStatus("current")


class _HwOspfv2AreaDefCost_Type(Integer32):
    """Custom type hwOspfv2AreaDefCost based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777214),
    )


_HwOspfv2AreaDefCost_Type.__name__ = "Integer32"
_HwOspfv2AreaDefCost_Object = MibTableColumn
hwOspfv2AreaDefCost = _HwOspfv2AreaDefCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 12),
    _HwOspfv2AreaDefCost_Type()
)
hwOspfv2AreaDefCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaDefCost.setStatus("current")


class _HwOspfv2AreaDescription_Type(DisplayString):
    """Custom type hwOspfv2AreaDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwOspfv2AreaDescription_Type.__name__ = "DisplayString"
_HwOspfv2AreaDescription_Object = MibTableColumn
hwOspfv2AreaDescription = _HwOspfv2AreaDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 13),
    _HwOspfv2AreaDescription_Type()
)
hwOspfv2AreaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaDescription.setStatus("current")


class _HwOspfv2AreaFilterExpAcl_Type(Integer32):
    """Custom type hwOspfv2AreaFilterExpAcl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwOspfv2AreaFilterExpAcl_Type.__name__ = "Integer32"
_HwOspfv2AreaFilterExpAcl_Object = MibTableColumn
hwOspfv2AreaFilterExpAcl = _HwOspfv2AreaFilterExpAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 14),
    _HwOspfv2AreaFilterExpAcl_Type()
)
hwOspfv2AreaFilterExpAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterExpAcl.setStatus("current")


class _HwOspfv2AreaFilterExpPrefix_Type(DisplayString):
    """Custom type hwOspfv2AreaFilterExpPrefix based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 169),
    )


_HwOspfv2AreaFilterExpPrefix_Type.__name__ = "DisplayString"
_HwOspfv2AreaFilterExpPrefix_Object = MibTableColumn
hwOspfv2AreaFilterExpPrefix = _HwOspfv2AreaFilterExpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 15),
    _HwOspfv2AreaFilterExpPrefix_Type()
)
hwOspfv2AreaFilterExpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterExpPrefix.setStatus("current")


class _HwOspfv2AreaFilterExpPolicy_Type(DisplayString):
    """Custom type hwOspfv2AreaFilterExpPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwOspfv2AreaFilterExpPolicy_Type.__name__ = "DisplayString"
_HwOspfv2AreaFilterExpPolicy_Object = MibTableColumn
hwOspfv2AreaFilterExpPolicy = _HwOspfv2AreaFilterExpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 16),
    _HwOspfv2AreaFilterExpPolicy_Type()
)
hwOspfv2AreaFilterExpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterExpPolicy.setStatus("current")


class _HwOspfv2AreaFilterImpAcl_Type(Integer32):
    """Custom type hwOspfv2AreaFilterImpAcl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwOspfv2AreaFilterImpAcl_Type.__name__ = "Integer32"
_HwOspfv2AreaFilterImpAcl_Object = MibTableColumn
hwOspfv2AreaFilterImpAcl = _HwOspfv2AreaFilterImpAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 17),
    _HwOspfv2AreaFilterImpAcl_Type()
)
hwOspfv2AreaFilterImpAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterImpAcl.setStatus("current")


class _HwOspfv2AreaFilterImpPrefix_Type(DisplayString):
    """Custom type hwOspfv2AreaFilterImpPrefix based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 169),
    )


_HwOspfv2AreaFilterImpPrefix_Type.__name__ = "DisplayString"
_HwOspfv2AreaFilterImpPrefix_Object = MibTableColumn
hwOspfv2AreaFilterImpPrefix = _HwOspfv2AreaFilterImpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 18),
    _HwOspfv2AreaFilterImpPrefix_Type()
)
hwOspfv2AreaFilterImpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterImpPrefix.setStatus("current")


class _HwOspfv2AreaFilterImpPolicy_Type(DisplayString):
    """Custom type hwOspfv2AreaFilterImpPolicy based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwOspfv2AreaFilterImpPolicy_Type.__name__ = "DisplayString"
_HwOspfv2AreaFilterImpPolicy_Object = MibTableColumn
hwOspfv2AreaFilterImpPolicy = _HwOspfv2AreaFilterImpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 19),
    _HwOspfv2AreaFilterImpPolicy_Type()
)
hwOspfv2AreaFilterImpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterImpPolicy.setStatus("current")


class _HwOspfv2AreaAuthModeType_Type(Integer32):
    """Custom type hwOspfv2AreaAuthModeType based on Integer32"""
    defaultValue = 1

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
        *(("hmd5", 4),
          ("keychain", 5),
          ("md5", 3),
          ("none", 1),
          ("simple", 2))
    )


_HwOspfv2AreaAuthModeType_Type.__name__ = "Integer32"
_HwOspfv2AreaAuthModeType_Object = MibTableColumn
hwOspfv2AreaAuthModeType = _HwOspfv2AreaAuthModeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 20),
    _HwOspfv2AreaAuthModeType_Type()
)
hwOspfv2AreaAuthModeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaAuthModeType.setStatus("current")


class _HwOspfv2AreaAuthPasswordType_Type(Integer32):
    """Custom type hwOspfv2AreaAuthPasswordType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cipherText", 3),
          ("none", 1),
          ("plainText", 2))
    )


_HwOspfv2AreaAuthPasswordType_Type.__name__ = "Integer32"
_HwOspfv2AreaAuthPasswordType_Object = MibTableColumn
hwOspfv2AreaAuthPasswordType = _HwOspfv2AreaAuthPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 21),
    _HwOspfv2AreaAuthPasswordType_Type()
)
hwOspfv2AreaAuthPasswordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaAuthPasswordType.setStatus("current")


class _HwOspfv2AreaAuthKeyId_Type(Integer32):
    """Custom type hwOspfv2AreaAuthKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwOspfv2AreaAuthKeyId_Type.__name__ = "Integer32"
_HwOspfv2AreaAuthKeyId_Object = MibTableColumn
hwOspfv2AreaAuthKeyId = _HwOspfv2AreaAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 22),
    _HwOspfv2AreaAuthKeyId_Type()
)
hwOspfv2AreaAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaAuthKeyId.setStatus("current")


class _HwOspfv2AreaAuthText_Type(DisplayString):
    """Custom type hwOspfv2AreaAuthText based on DisplayString"""
    defaultHexValue = ""


_HwOspfv2AreaAuthText_Object = MibTableColumn
hwOspfv2AreaAuthText = _HwOspfv2AreaAuthText_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 23),
    _HwOspfv2AreaAuthText_Type()
)
hwOspfv2AreaAuthText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaAuthText.setStatus("current")


class _HwOspfv2AreaMplsTe_Type(Integer32):
    """Custom type hwOspfv2AreaMplsTe based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("stdDisable", 3),
          ("stdEnable", 2))
    )


_HwOspfv2AreaMplsTe_Type.__name__ = "Integer32"
_HwOspfv2AreaMplsTe_Object = MibTableColumn
hwOspfv2AreaMplsTe = _HwOspfv2AreaMplsTe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 24),
    _HwOspfv2AreaMplsTe_Type()
)
hwOspfv2AreaMplsTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaMplsTe.setStatus("current")
_HwOspfv2AreaAreaRowStatus_Type = RowStatus
_HwOspfv2AreaAreaRowStatus_Object = MibTableColumn
hwOspfv2AreaAreaRowStatus = _HwOspfv2AreaAreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 25),
    _HwOspfv2AreaAreaRowStatus_Type()
)
hwOspfv2AreaAreaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaAreaRowStatus.setStatus("current")


class _HwOspfv2AreaFilterExpAclName_Type(DisplayString):
    """Custom type hwOspfv2AreaFilterExpAclName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwOspfv2AreaFilterExpAclName_Type.__name__ = "DisplayString"
_HwOspfv2AreaFilterExpAclName_Object = MibTableColumn
hwOspfv2AreaFilterExpAclName = _HwOspfv2AreaFilterExpAclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 26),
    _HwOspfv2AreaFilterExpAclName_Type()
)
hwOspfv2AreaFilterExpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterExpAclName.setStatus("current")


class _HwOspfv2AreaFilterImpAclName_Type(DisplayString):
    """Custom type hwOspfv2AreaFilterImpAclName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwOspfv2AreaFilterImpAclName_Type.__name__ = "DisplayString"
_HwOspfv2AreaFilterImpAclName_Object = MibTableColumn
hwOspfv2AreaFilterImpAclName = _HwOspfv2AreaFilterImpAclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 4, 1, 27),
    _HwOspfv2AreaFilterImpAclName_Type()
)
hwOspfv2AreaFilterImpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2AreaFilterImpAclName.setStatus("current")
_HwOspfv2NetworkTable_Object = MibTable
hwOspfv2NetworkTable = _HwOspfv2NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 5)
)
if mibBuilder.loadTexts:
    hwOspfv2NetworkTable.setStatus("current")
_HwOspfv2NetworkEntry_Object = MibTableRow
hwOspfv2NetworkEntry = _HwOspfv2NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 5, 1)
)
hwOspfv2NetworkEntry.setIndexNames(
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2ProcessIdIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2AreaIdIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2NetworkIpAddrIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2NetworkIpMaskIndex"),
)
if mibBuilder.loadTexts:
    hwOspfv2NetworkEntry.setStatus("current")
_HwOspfv2NetworkIpAddrIndex_Type = IpAddress
_HwOspfv2NetworkIpAddrIndex_Object = MibTableColumn
hwOspfv2NetworkIpAddrIndex = _HwOspfv2NetworkIpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 5, 1, 1),
    _HwOspfv2NetworkIpAddrIndex_Type()
)
hwOspfv2NetworkIpAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv2NetworkIpAddrIndex.setStatus("current")
_HwOspfv2NetworkIpMaskIndex_Type = IpAddress
_HwOspfv2NetworkIpMaskIndex_Object = MibTableColumn
hwOspfv2NetworkIpMaskIndex = _HwOspfv2NetworkIpMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 5, 1, 2),
    _HwOspfv2NetworkIpMaskIndex_Type()
)
hwOspfv2NetworkIpMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv2NetworkIpMaskIndex.setStatus("current")
_HwOspfv2NetworkRowStatus_Type = RowStatus
_HwOspfv2NetworkRowStatus_Object = MibTableColumn
hwOspfv2NetworkRowStatus = _HwOspfv2NetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 5, 1, 3),
    _HwOspfv2NetworkRowStatus_Type()
)
hwOspfv2NetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv2NetworkRowStatus.setStatus("current")
_HwOspfv2NeighborTable_Object = MibTable
hwOspfv2NeighborTable = _HwOspfv2NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6)
)
if mibBuilder.loadTexts:
    hwOspfv2NeighborTable.setStatus("current")
_HwOspfv2NeighborEntry_Object = MibTableRow
hwOspfv2NeighborEntry = _HwOspfv2NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1)
)
hwOspfv2NeighborEntry.setIndexNames(
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2ProcessIdIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2AreaIdIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2SelfIfnetIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2NbrIpAddrIndex"),
)
if mibBuilder.loadTexts:
    hwOspfv2NeighborEntry.setStatus("current")


class _HwOspfv2SelfIfnetIndex_Type(Integer32):
    """Custom type hwOspfv2SelfIfnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwOspfv2SelfIfnetIndex_Type.__name__ = "Integer32"
_HwOspfv2SelfIfnetIndex_Object = MibTableColumn
hwOspfv2SelfIfnetIndex = _HwOspfv2SelfIfnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 1),
    _HwOspfv2SelfIfnetIndex_Type()
)
hwOspfv2SelfIfnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv2SelfIfnetIndex.setStatus("current")
_HwOspfv2NbrIpAddrIndex_Type = IpAddress
_HwOspfv2NbrIpAddrIndex_Object = MibTableColumn
hwOspfv2NbrIpAddrIndex = _HwOspfv2NbrIpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 2),
    _HwOspfv2NbrIpAddrIndex_Type()
)
hwOspfv2NbrIpAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv2NbrIpAddrIndex.setStatus("current")
_HwOspfv2SelfRouterId_Type = IpAddress
_HwOspfv2SelfRouterId_Object = MibTableColumn
hwOspfv2SelfRouterId = _HwOspfv2SelfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 3),
    _HwOspfv2SelfRouterId_Type()
)
hwOspfv2SelfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2SelfRouterId.setStatus("current")
_HwOspfv2SelfIfIpAddress_Type = IpAddress
_HwOspfv2SelfIfIpAddress_Object = MibTableColumn
hwOspfv2SelfIfIpAddress = _HwOspfv2SelfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 4),
    _HwOspfv2SelfIfIpAddress_Type()
)
hwOspfv2SelfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2SelfIfIpAddress.setStatus("current")


class _HwOspfv2SelfIfName_Type(DisplayString):
    """Custom type hwOspfv2SelfIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwOspfv2SelfIfName_Type.__name__ = "DisplayString"
_HwOspfv2SelfIfName_Object = MibTableColumn
hwOspfv2SelfIfName = _HwOspfv2SelfIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 5),
    _HwOspfv2SelfIfName_Type()
)
hwOspfv2SelfIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2SelfIfName.setStatus("current")
_HwOspfv2NbrIfDesignatedRouter_Type = IpAddress
_HwOspfv2NbrIfDesignatedRouter_Object = MibTableColumn
hwOspfv2NbrIfDesignatedRouter = _HwOspfv2NbrIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 6),
    _HwOspfv2NbrIfDesignatedRouter_Type()
)
hwOspfv2NbrIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrIfDesignatedRouter.setStatus("current")
_HwOspfv2NbrIfBackupDesignatedRouter_Type = IpAddress
_HwOspfv2NbrIfBackupDesignatedRouter_Object = MibTableColumn
hwOspfv2NbrIfBackupDesignatedRouter = _HwOspfv2NbrIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 7),
    _HwOspfv2NbrIfBackupDesignatedRouter_Type()
)
hwOspfv2NbrIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrIfBackupDesignatedRouter.setStatus("current")
_HwOspfv2NbrIfMtu_Type = Integer32
_HwOspfv2NbrIfMtu_Object = MibTableColumn
hwOspfv2NbrIfMtu = _HwOspfv2NbrIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 8),
    _HwOspfv2NbrIfMtu_Type()
)
hwOspfv2NbrIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrIfMtu.setStatus("current")
_HwOspfv2NbrRouterId_Type = IpAddress
_HwOspfv2NbrRouterId_Object = MibTableColumn
hwOspfv2NbrRouterId = _HwOspfv2NbrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 9),
    _HwOspfv2NbrRouterId_Type()
)
hwOspfv2NbrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrRouterId.setStatus("current")


class _HwOspfv2NbrState_Type(Integer32):
    """Custom type hwOspfv2NbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_HwOspfv2NbrState_Type.__name__ = "Integer32"
_HwOspfv2NbrState_Object = MibTableColumn
hwOspfv2NbrState = _HwOspfv2NbrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 10),
    _HwOspfv2NbrState_Type()
)
hwOspfv2NbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrState.setStatus("current")


class _HwOspfv2NbrMode_Type(Integer32):
    """Custom type hwOspfv2NbrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwOspfv2NbrMode_Type.__name__ = "Integer32"
_HwOspfv2NbrMode_Object = MibTableColumn
hwOspfv2NbrMode = _HwOspfv2NbrMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 11),
    _HwOspfv2NbrMode_Type()
)
hwOspfv2NbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrMode.setStatus("current")


class _HwOspfv2NbrPriority_Type(Integer32):
    """Custom type hwOspfv2NbrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwOspfv2NbrPriority_Type.__name__ = "Integer32"
_HwOspfv2NbrPriority_Object = MibTableColumn
hwOspfv2NbrPriority = _HwOspfv2NbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 12),
    _HwOspfv2NbrPriority_Type()
)
hwOspfv2NbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrPriority.setStatus("current")
_HwOspfv2NbrUpTime_Type = Unsigned32
_HwOspfv2NbrUpTime_Object = MibTableColumn
hwOspfv2NbrUpTime = _HwOspfv2NbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 13),
    _HwOspfv2NbrUpTime_Type()
)
hwOspfv2NbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrUpTime.setStatus("current")
_HwOspfv2NbrAuthSequence_Type = Unsigned32
_HwOspfv2NbrAuthSequence_Object = MibTableColumn
hwOspfv2NbrAuthSequence = _HwOspfv2NbrAuthSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 14),
    _HwOspfv2NbrAuthSequence_Type()
)
hwOspfv2NbrAuthSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrAuthSequence.setStatus("current")


class _HwOspfv2NbrDeadTimeLeft_Type(Gauge32):
    """Custom type hwOspfv2NbrDeadTimeLeft based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 235926000),
    )


_HwOspfv2NbrDeadTimeLeft_Type.__name__ = "Gauge32"
_HwOspfv2NbrDeadTimeLeft_Object = MibTableColumn
hwOspfv2NbrDeadTimeLeft = _HwOspfv2NbrDeadTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 15),
    _HwOspfv2NbrDeadTimeLeft_Type()
)
hwOspfv2NbrDeadTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrDeadTimeLeft.setStatus("current")


class _HwOspfv2NbrGrStatus_Type(Integer32):
    """Custom type hwOspfv2NbrGrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doingGR", 2),
          ("helper", 3),
          ("normal", 1))
    )


_HwOspfv2NbrGrStatus_Type.__name__ = "Integer32"
_HwOspfv2NbrGrStatus_Object = MibTableColumn
hwOspfv2NbrGrStatus = _HwOspfv2NbrGrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 6, 1, 16),
    _HwOspfv2NbrGrStatus_Type()
)
hwOspfv2NbrGrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2NbrGrStatus.setStatus("current")
_HwOspfv2InterfaceTable_Object = MibTable
hwOspfv2InterfaceTable = _HwOspfv2InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 7)
)
if mibBuilder.loadTexts:
    hwOspfv2InterfaceTable.setStatus("current")
_HwOspfv2InterfaceEntry_Object = MibTableRow
hwOspfv2InterfaceEntry = _HwOspfv2InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 7, 1)
)
hwOspfv2InterfaceEntry.setIndexNames(
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2ProcessIdIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2AreaIdIndex"),
    (0, "HUAWEI-OSPFV2-MIB", "hwOspfv2InterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwOspfv2InterfaceEntry.setStatus("current")
_HwOspfv2InterfaceIndex_Type = Integer32
_HwOspfv2InterfaceIndex_Object = MibTableColumn
hwOspfv2InterfaceIndex = _HwOspfv2InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 7, 1, 1),
    _HwOspfv2InterfaceIndex_Type()
)
hwOspfv2InterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv2InterfaceIndex.setStatus("current")


class _HwOspfv2InterfaceName_Type(DisplayString):
    """Custom type hwOspfv2InterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwOspfv2InterfaceName_Type.__name__ = "DisplayString"
_HwOspfv2InterfaceName_Object = MibTableColumn
hwOspfv2InterfaceName = _HwOspfv2InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 7, 1, 2),
    _HwOspfv2InterfaceName_Type()
)
hwOspfv2InterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv2InterfaceName.setStatus("current")
_HwOspfv2TrapsObjects_ObjectIdentity = ObjectIdentity
hwOspfv2TrapsObjects = _HwOspfv2TrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 30)
)


class _HwOspfv2NbrChgReason_Type(Integer32):
    """Custom type hwOspfv2NbrChgReason based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("adjacencyHoldTimerExpired", 1),
          ("alarmCleared", 100),
          ("bfdSessionStateChange", 4),
          ("configureChange", 5),
          ("ospfProtocolReason", 3),
          ("peerRouterReason", 6),
          ("physicalInterfaceChange", 2),
          ("waitingForEstablishingNeighbor", 7))
    )


_HwOspfv2NbrChgReason_Type.__name__ = "Integer32"
_HwOspfv2NbrChgReason_Object = MibScalar
hwOspfv2NbrChgReason = _HwOspfv2NbrChgReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 30, 1),
    _HwOspfv2NbrChgReason_Type()
)
hwOspfv2NbrChgReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv2NbrChgReason.setStatus("current")


class _HwOspfv2IfChgReason_Type(Integer32):
    """Custom type hwOspfv2IfChgReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("alarmCleared", 100),
          ("configureChange", 1),
          ("physicalInterfaceChange", 2))
    )


_HwOspfv2IfChgReason_Type.__name__ = "Integer32"
_HwOspfv2IfChgReason_Object = MibScalar
hwOspfv2IfChgReason = _HwOspfv2IfChgReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 30, 2),
    _HwOspfv2IfChgReason_Type()
)
hwOspfv2IfChgReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv2IfChgReason.setStatus("current")
_HwOspfv2Traps_ObjectIdentity = ObjectIdentity
hwOspfv2Traps = _HwOspfv2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 31)
)
_HwOspfv2Conformance_ObjectIdentity = ObjectIdentity
hwOspfv2Conformance = _HwOspfv2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32)
)
_HwOspfv2Compliances_ObjectIdentity = ObjectIdentity
hwOspfv2Compliances = _HwOspfv2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 1)
)
_HwOspfv2Groups_ObjectIdentity = ObjectIdentity
hwOspfv2Groups = _HwOspfv2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2)
)

# Managed Objects groups

hwOspfv2MIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 1)
)
hwOspfv2MIBObjectsGroup.setObjects(
    ("HUAWEI-OSPFV2-MIB", "hwOspfv2MIBBinding")
)
if mibBuilder.loadTexts:
    hwOspfv2MIBObjectsGroup.setStatus("current")

hwOspfv2ProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 2)
)
hwOspfv2ProcessGroup.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfv2VpnName"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2ConfigRouterId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2ActualRouterId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2BandwidthReference"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2Description"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsdbOverflowLimit"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2MaxLoadBalaNumber"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AseRouteMaxNumber"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2InterRouteMaxNumber"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2IntraRouteMaxNumber"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2RetransLimitMaxNumber"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2Rfc1583Compatibility"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2ShamHello"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2OpaqueCapability"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2TrafficAdjustment"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2TrafficAdvertise"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2FlushTimer"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SpfSchHoldIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SpfSchStartIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SpfSchMaxIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaOrigIntvlOtherType"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaOrigHoldIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaOrigStartIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaOrigMaxIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaArriveHoldIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaArriveStartIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaArriveMaxIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaArriveIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SpfSchIntvlUnit"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SpfSchIntvlNumber"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2LsaOrigIntvl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2ProcessRowStatus"))
)
if mibBuilder.loadTexts:
    hwOspfv2ProcessGroup.setStatus("current")

hwOspfv2AreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 4)
)
hwOspfv2AreaGroup.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaType"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNoSummary"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaFlushTimer"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaDefAdvertise"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaNoImportRoute"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaTransAlways"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaTransTimer"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaAllowFaZero"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaSuppressFa"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaNssaSetNBit"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaDefCost"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaDescription"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterExpAcl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterExpPrefix"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterExpPolicy"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterImpAcl"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterImpPrefix"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterImpPolicy"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaAuthModeType"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaAuthPasswordType"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaAuthKeyId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaAuthText"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaMplsTe"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaAreaRowStatus"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterExpAclName"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaFilterImpAclName"))
)
if mibBuilder.loadTexts:
    hwOspfv2AreaGroup.setStatus("current")

hwOspfv2NetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 5)
)
hwOspfv2NetworkGroup.setObjects(
    ("HUAWEI-OSPFV2-MIB", "hwOspfv2NetworkRowStatus")
)
if mibBuilder.loadTexts:
    hwOspfv2NetworkGroup.setStatus("current")

hwOspfv2NeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 6)
)
hwOspfv2NeighborGroup.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfRouterId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfIfIpAddress"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfIfName"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrIfDesignatedRouter"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrIfBackupDesignatedRouter"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrIfMtu"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrRouterId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrState"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrMode"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrPriority"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrUpTime"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrAuthSequence"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrDeadTimeLeft"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrGrStatus"))
)
if mibBuilder.loadTexts:
    hwOspfv2NeighborGroup.setStatus("current")

hwOspfv2ChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 7)
)
hwOspfv2ChangeGroup.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfv2MIBObjectsChange"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2ProcessChange"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2AreaChange"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NetworkChange"))
)
if mibBuilder.loadTexts:
    hwOspfv2ChangeGroup.setStatus("current")

hwOspfv2TrapsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 9)
)
hwOspfv2TrapsObjectsGroup.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrChgReason"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2IfChgReason"))
)
if mibBuilder.loadTexts:
    hwOspfv2TrapsObjectsGroup.setStatus("current")

hwOspfv2InterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 10)
)
hwOspfv2InterfaceGroup.setObjects(
    ("HUAWEI-OSPFV2-MIB", "hwOspfv2InterfaceName")
)
if mibBuilder.loadTexts:
    hwOspfv2InterfaceGroup.setStatus("current")


# Notification objects

hwOspfV2NeighborUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 31, 1)
)
hwOspfV2NeighborUnavailable.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfNbrIpAddr"),
        ("OSPF-MIB", "ospfNbrAddressLessIndex"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfIfName"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2VpnName"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrChgReason"))
)
if mibBuilder.loadTexts:
    hwOspfV2NeighborUnavailable.setStatus(
        "current"
    )

hwOspfV2NeighborUnavailableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 31, 2)
)
hwOspfV2NeighborUnavailableClear.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfNbrIpAddr"),
        ("OSPF-MIB", "ospfNbrAddressLessIndex"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfIfName"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2VpnName"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrChgReason"))
)
if mibBuilder.loadTexts:
    hwOspfV2NeighborUnavailableClear.setStatus(
        "current"
    )

hwOspfv2IntraAreaRouteridConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 31, 3)
)
hwOspfv2IntraAreaRouteridConflict.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfRouterId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2NbrRouterId"))
)
if mibBuilder.loadTexts:
    hwOspfv2IntraAreaRouteridConflict.setStatus(
        "current"
    )

hwOspfv2IntraAreaDRIpAddressConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 31, 4)
)
hwOspfv2IntraAreaDRIpAddressConflict.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfRouterId"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfIfIpAddress"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2SelfIfName"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    hwOspfv2IntraAreaDRIpAddressConflict.setStatus(
        "current"
    )


# Notifications groups

hwOspfTrapEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 2, 8)
)
hwOspfTrapEventGroup.setObjects(
      *(("HUAWEI-OSPFV2-MIB", "hwOspfV2NeighborUnavailable"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfV2NeighborUnavailableClear"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2IntraAreaRouteridConflict"),
        ("HUAWEI-OSPFV2-MIB", "hwOspfv2IntraAreaDRIpAddressConflict"))
)
if mibBuilder.loadTexts:
    hwOspfTrapEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwOspfv2ModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 155, 32, 1, 1)
)
if mibBuilder.loadTexts:
    hwOspfv2ModuleFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-OSPFV2-MIB",
    **{"hwOspfv2MIB": hwOspfv2MIB,
       "hwOspfv2MIBObjects": hwOspfv2MIBObjects,
       "hwOspfv2MIBBinding": hwOspfv2MIBBinding,
       "hwOspfv2ChangeTable": hwOspfv2ChangeTable,
       "hwOspfv2MIBObjectsChange": hwOspfv2MIBObjectsChange,
       "hwOspfv2ProcessChange": hwOspfv2ProcessChange,
       "hwOspfv2AreaChange": hwOspfv2AreaChange,
       "hwOspfv2NetworkChange": hwOspfv2NetworkChange,
       "hwOspfv2ProcessTable": hwOspfv2ProcessTable,
       "hwOspfv2ProcessEntry": hwOspfv2ProcessEntry,
       "hwOspfv2ProcessIdIndex": hwOspfv2ProcessIdIndex,
       "hwOspfv2VpnName": hwOspfv2VpnName,
       "hwOspfv2ConfigRouterId": hwOspfv2ConfigRouterId,
       "hwOspfv2ActualRouterId": hwOspfv2ActualRouterId,
       "hwOspfv2BandwidthReference": hwOspfv2BandwidthReference,
       "hwOspfv2Description": hwOspfv2Description,
       "hwOspfv2LsaArriveIntvl": hwOspfv2LsaArriveIntvl,
       "hwOspfv2LsaArriveMaxIntvl": hwOspfv2LsaArriveMaxIntvl,
       "hwOspfv2LsaArriveStartIntvl": hwOspfv2LsaArriveStartIntvl,
       "hwOspfv2LsaArriveHoldIntvl": hwOspfv2LsaArriveHoldIntvl,
       "hwOspfv2LsaOrigIntvl": hwOspfv2LsaOrigIntvl,
       "hwOspfv2LsaOrigMaxIntvl": hwOspfv2LsaOrigMaxIntvl,
       "hwOspfv2LsaOrigStartIntvl": hwOspfv2LsaOrigStartIntvl,
       "hwOspfv2LsaOrigHoldIntvl": hwOspfv2LsaOrigHoldIntvl,
       "hwOspfv2LsaOrigIntvlOtherType": hwOspfv2LsaOrigIntvlOtherType,
       "hwOspfv2LsdbOverflowLimit": hwOspfv2LsdbOverflowLimit,
       "hwOspfv2MaxLoadBalaNumber": hwOspfv2MaxLoadBalaNumber,
       "hwOspfv2AseRouteMaxNumber": hwOspfv2AseRouteMaxNumber,
       "hwOspfv2InterRouteMaxNumber": hwOspfv2InterRouteMaxNumber,
       "hwOspfv2IntraRouteMaxNumber": hwOspfv2IntraRouteMaxNumber,
       "hwOspfv2RetransLimitMaxNumber": hwOspfv2RetransLimitMaxNumber,
       "hwOspfv2Rfc1583Compatibility": hwOspfv2Rfc1583Compatibility,
       "hwOspfv2ShamHello": hwOspfv2ShamHello,
       "hwOspfv2SpfSchIntvlUnit": hwOspfv2SpfSchIntvlUnit,
       "hwOspfv2SpfSchIntvlNumber": hwOspfv2SpfSchIntvlNumber,
       "hwOspfv2SpfSchMaxIntvl": hwOspfv2SpfSchMaxIntvl,
       "hwOspfv2SpfSchStartIntvl": hwOspfv2SpfSchStartIntvl,
       "hwOspfv2SpfSchHoldIntvl": hwOspfv2SpfSchHoldIntvl,
       "hwOspfv2OpaqueCapability": hwOspfv2OpaqueCapability,
       "hwOspfv2TrafficAdjustment": hwOspfv2TrafficAdjustment,
       "hwOspfv2TrafficAdvertise": hwOspfv2TrafficAdvertise,
       "hwOspfv2FlushTimer": hwOspfv2FlushTimer,
       "hwOspfv2ProcessRowStatus": hwOspfv2ProcessRowStatus,
       "hwOspfv2AreaTable": hwOspfv2AreaTable,
       "hwOspfv2AreaEntry": hwOspfv2AreaEntry,
       "hwOspfv2AreaIdIndex": hwOspfv2AreaIdIndex,
       "hwOspfv2AreaType": hwOspfv2AreaType,
       "hwOspfv2AreaNoSummary": hwOspfv2AreaNoSummary,
       "hwOspfv2AreaNssaFlushTimer": hwOspfv2AreaNssaFlushTimer,
       "hwOspfv2AreaNssaDefAdvertise": hwOspfv2AreaNssaDefAdvertise,
       "hwOspfv2AreaNssaNoImportRoute": hwOspfv2AreaNssaNoImportRoute,
       "hwOspfv2AreaNssaTransAlways": hwOspfv2AreaNssaTransAlways,
       "hwOspfv2AreaNssaTransTimer": hwOspfv2AreaNssaTransTimer,
       "hwOspfv2AreaNssaAllowFaZero": hwOspfv2AreaNssaAllowFaZero,
       "hwOspfv2AreaNssaSuppressFa": hwOspfv2AreaNssaSuppressFa,
       "hwOspfv2AreaNssaSetNBit": hwOspfv2AreaNssaSetNBit,
       "hwOspfv2AreaDefCost": hwOspfv2AreaDefCost,
       "hwOspfv2AreaDescription": hwOspfv2AreaDescription,
       "hwOspfv2AreaFilterExpAcl": hwOspfv2AreaFilterExpAcl,
       "hwOspfv2AreaFilterExpPrefix": hwOspfv2AreaFilterExpPrefix,
       "hwOspfv2AreaFilterExpPolicy": hwOspfv2AreaFilterExpPolicy,
       "hwOspfv2AreaFilterImpAcl": hwOspfv2AreaFilterImpAcl,
       "hwOspfv2AreaFilterImpPrefix": hwOspfv2AreaFilterImpPrefix,
       "hwOspfv2AreaFilterImpPolicy": hwOspfv2AreaFilterImpPolicy,
       "hwOspfv2AreaAuthModeType": hwOspfv2AreaAuthModeType,
       "hwOspfv2AreaAuthPasswordType": hwOspfv2AreaAuthPasswordType,
       "hwOspfv2AreaAuthKeyId": hwOspfv2AreaAuthKeyId,
       "hwOspfv2AreaAuthText": hwOspfv2AreaAuthText,
       "hwOspfv2AreaMplsTe": hwOspfv2AreaMplsTe,
       "hwOspfv2AreaAreaRowStatus": hwOspfv2AreaAreaRowStatus,
       "hwOspfv2AreaFilterExpAclName": hwOspfv2AreaFilterExpAclName,
       "hwOspfv2AreaFilterImpAclName": hwOspfv2AreaFilterImpAclName,
       "hwOspfv2NetworkTable": hwOspfv2NetworkTable,
       "hwOspfv2NetworkEntry": hwOspfv2NetworkEntry,
       "hwOspfv2NetworkIpAddrIndex": hwOspfv2NetworkIpAddrIndex,
       "hwOspfv2NetworkIpMaskIndex": hwOspfv2NetworkIpMaskIndex,
       "hwOspfv2NetworkRowStatus": hwOspfv2NetworkRowStatus,
       "hwOspfv2NeighborTable": hwOspfv2NeighborTable,
       "hwOspfv2NeighborEntry": hwOspfv2NeighborEntry,
       "hwOspfv2SelfIfnetIndex": hwOspfv2SelfIfnetIndex,
       "hwOspfv2NbrIpAddrIndex": hwOspfv2NbrIpAddrIndex,
       "hwOspfv2SelfRouterId": hwOspfv2SelfRouterId,
       "hwOspfv2SelfIfIpAddress": hwOspfv2SelfIfIpAddress,
       "hwOspfv2SelfIfName": hwOspfv2SelfIfName,
       "hwOspfv2NbrIfDesignatedRouter": hwOspfv2NbrIfDesignatedRouter,
       "hwOspfv2NbrIfBackupDesignatedRouter": hwOspfv2NbrIfBackupDesignatedRouter,
       "hwOspfv2NbrIfMtu": hwOspfv2NbrIfMtu,
       "hwOspfv2NbrRouterId": hwOspfv2NbrRouterId,
       "hwOspfv2NbrState": hwOspfv2NbrState,
       "hwOspfv2NbrMode": hwOspfv2NbrMode,
       "hwOspfv2NbrPriority": hwOspfv2NbrPriority,
       "hwOspfv2NbrUpTime": hwOspfv2NbrUpTime,
       "hwOspfv2NbrAuthSequence": hwOspfv2NbrAuthSequence,
       "hwOspfv2NbrDeadTimeLeft": hwOspfv2NbrDeadTimeLeft,
       "hwOspfv2NbrGrStatus": hwOspfv2NbrGrStatus,
       "hwOspfv2InterfaceTable": hwOspfv2InterfaceTable,
       "hwOspfv2InterfaceEntry": hwOspfv2InterfaceEntry,
       "hwOspfv2InterfaceIndex": hwOspfv2InterfaceIndex,
       "hwOspfv2InterfaceName": hwOspfv2InterfaceName,
       "hwOspfv2TrapsObjects": hwOspfv2TrapsObjects,
       "hwOspfv2NbrChgReason": hwOspfv2NbrChgReason,
       "hwOspfv2IfChgReason": hwOspfv2IfChgReason,
       "hwOspfv2Traps": hwOspfv2Traps,
       "hwOspfV2NeighborUnavailable": hwOspfV2NeighborUnavailable,
       "hwOspfV2NeighborUnavailableClear": hwOspfV2NeighborUnavailableClear,
       "hwOspfv2IntraAreaRouteridConflict": hwOspfv2IntraAreaRouteridConflict,
       "hwOspfv2IntraAreaDRIpAddressConflict": hwOspfv2IntraAreaDRIpAddressConflict,
       "hwOspfv2Conformance": hwOspfv2Conformance,
       "hwOspfv2Compliances": hwOspfv2Compliances,
       "hwOspfv2ModuleFullCompliance": hwOspfv2ModuleFullCompliance,
       "hwOspfv2Groups": hwOspfv2Groups,
       "hwOspfv2MIBObjectsGroup": hwOspfv2MIBObjectsGroup,
       "hwOspfv2ProcessGroup": hwOspfv2ProcessGroup,
       "hwOspfv2AreaGroup": hwOspfv2AreaGroup,
       "hwOspfv2NetworkGroup": hwOspfv2NetworkGroup,
       "hwOspfv2NeighborGroup": hwOspfv2NeighborGroup,
       "hwOspfv2ChangeGroup": hwOspfv2ChangeGroup,
       "hwOspfTrapEventGroup": hwOspfTrapEventGroup,
       "hwOspfv2TrapsObjectsGroup": hwOspfv2TrapsObjectsGroup,
       "hwOspfv2InterfaceGroup": hwOspfv2InterfaceGroup}
)
