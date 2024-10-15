# SNMP MIB module (Unisphere-Data-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:33 2024
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,
 UsdTimeSlotMap) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex",
    "UsdTimeSlotMap")


# MODULE-IDENTITY

usdDs1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5)
)
usdDs1MIB.setRevisions(
        ("2002-05-13 16:01",
         "2001-07-31 18:25",
         "2001-04-04 18:05",
         "1999-06-17 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdDs1Objects_ObjectIdentity = ObjectIdentity
usdDs1Objects = _UsdDs1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1)
)
_UsdDsx1ConfigTable_Object = MibTable
usdDsx1ConfigTable = _UsdDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    usdDsx1ConfigTable.setStatus("current")
_UsdDsx1ConfigEntry_Object = MibTableRow
usdDsx1ConfigEntry = _UsdDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1)
)
usdDsx1ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdDsx1ConfigEntry.setStatus("current")
_UsdDsx1TimeSlotMap_Type = UsdTimeSlotMap
_UsdDsx1TimeSlotMap_Object = MibTableColumn
usdDsx1TimeSlotMap = _UsdDsx1TimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 1),
    _UsdDsx1TimeSlotMap_Type()
)
usdDsx1TimeSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDsx1TimeSlotMap.setStatus("current")


class _UsdDsx1Ds1ChannelNumber_Type(Integer32):
    """Custom type usdDsx1Ds1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_UsdDsx1Ds1ChannelNumber_Type.__name__ = "Integer32"
_UsdDsx1Ds1ChannelNumber_Object = MibTableColumn
usdDsx1Ds1ChannelNumber = _UsdDsx1Ds1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 2),
    _UsdDsx1Ds1ChannelNumber_Type()
)
usdDsx1Ds1ChannelNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1Ds1ChannelNumber.setStatus("current")


class _UsdDsx1Capabilities_Type(Integer32):
    """Custom type usdDsx1Capabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UsdDsx1Capabilities_Type.__name__ = "Integer32"
_UsdDsx1Capabilities_Object = MibTableColumn
usdDsx1Capabilities = _UsdDsx1Capabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 3),
    _UsdDsx1Capabilities_Type()
)
usdDsx1Capabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDsx1Capabilities.setStatus("current")


class _UsdDsx1Mode_Type(Integer32):
    """Custom type usdDsx1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("j1", 3),
          ("t1", 1))
    )


_UsdDsx1Mode_Type.__name__ = "Integer32"
_UsdDsx1Mode_Object = MibTableColumn
usdDsx1Mode = _UsdDsx1Mode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 4),
    _UsdDsx1Mode_Type()
)
usdDsx1Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1Mode.setStatus("current")


class _UsdDsx1LineBuildOutCapabilities_Type(Integer32):
    """Custom type usdDsx1LineBuildOutCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_UsdDsx1LineBuildOutCapabilities_Type.__name__ = "Integer32"
_UsdDsx1LineBuildOutCapabilities_Object = MibTableColumn
usdDsx1LineBuildOutCapabilities = _UsdDsx1LineBuildOutCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 5),
    _UsdDsx1LineBuildOutCapabilities_Type()
)
usdDsx1LineBuildOutCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDsx1LineBuildOutCapabilities.setStatus("current")


class _UsdDsx1LineBuildOutType_Type(Integer32):
    """Custom type usdDsx1LineBuildOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("longHaul", 2),
          ("notSupported", 3),
          ("shortHaul", 1))
    )


_UsdDsx1LineBuildOutType_Type.__name__ = "Integer32"
_UsdDsx1LineBuildOutType_Object = MibTableColumn
usdDsx1LineBuildOutType = _UsdDsx1LineBuildOutType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 6),
    _UsdDsx1LineBuildOutType_Type()
)
usdDsx1LineBuildOutType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1LineBuildOutType.setStatus("current")


class _UsdDsx1LineAttenuation_Type(Integer32):
    """Custom type usdDsx1LineAttenuation based on Integer32"""
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
        *(("db0", 1),
          ("dbMinus15", 3),
          ("dbMinus22Point5", 4),
          ("dbMinus7Point5", 2),
          ("notSupported", 5))
    )


_UsdDsx1LineAttenuation_Type.__name__ = "Integer32"
_UsdDsx1LineAttenuation_Object = MibTableColumn
usdDsx1LineAttenuation = _UsdDsx1LineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 7),
    _UsdDsx1LineAttenuation_Type()
)
usdDsx1LineAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1LineAttenuation.setStatus("current")


class _UsdDsx1LineLength_Type(Integer32):
    """Custom type usdDsx1LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_UsdDsx1LineLength_Type.__name__ = "Integer32"
_UsdDsx1LineLength_Object = MibTableColumn
usdDsx1LineLength = _UsdDsx1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 8),
    _UsdDsx1LineLength_Type()
)
usdDsx1LineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1LineLength.setStatus("current")
if mibBuilder.loadTexts:
    usdDsx1LineLength.setUnits("meters")
_UsdDsx1LowerIfIndex_Type = InterfaceIndexOrZero
_UsdDsx1LowerIfIndex_Object = MibTableColumn
usdDsx1LowerIfIndex = _UsdDsx1LowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 9),
    _UsdDsx1LowerIfIndex_Type()
)
usdDsx1LowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1LowerIfIndex.setStatus("current")
_UsdDsx1RowStatus_Type = RowStatus
_UsdDsx1RowStatus_Object = MibTableColumn
usdDsx1RowStatus = _UsdDsx1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 10),
    _UsdDsx1RowStatus_Type()
)
usdDsx1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1RowStatus.setStatus("current")


class _UsdDsx1SendCode_Type(Integer32):
    """Custom type usdDsx1SendCode based on Integer32"""
    defaultValue = 20

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
              20)
        )
    )
    namedValues = NamedValues(
        *(("otherPattern", 20),
          ("sendAllOnesPattern", 6),
          ("sendAllZerosPattern", 5),
          ("sendAltZeroOnePattern", 7),
          ("sendBellcoreInbandLineCode", 3),
          ("sendBellcoreLineCode", 2),
          ("sendInbandLineCode", 1),
          ("sendQRSPattern", 4),
          ("sendTwo11Pattern", 8),
          ("sendTwo15Pattern", 9),
          ("sendTwo20Pattern", 10),
          ("sendTwo23Pattern", 11),
          ("sendUnfrAllOnesPattern", 14),
          ("sendUnfrAllZerosPattern", 13),
          ("sendUnfrAltZeroOnePattern", 15),
          ("sendUnfrQRSPattern", 12),
          ("sendUnfrTwo11Pattern", 16),
          ("sendUnfrTwo15Pattern", 17),
          ("sendUnfrTwo20Pattern", 18),
          ("sendUnfrTwo23Pattern", 19))
    )


_UsdDsx1SendCode_Type.__name__ = "Integer32"
_UsdDsx1SendCode_Object = MibTableColumn
usdDsx1SendCode = _UsdDsx1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 11),
    _UsdDsx1SendCode_Type()
)
usdDsx1SendCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1SendCode.setStatus("current")


class _UsdDsx1YellowAlarm_Type(Integer32):
    """Custom type usdDsx1YellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("detect", 2),
          ("generate", 1),
          ("none", 4))
    )


_UsdDsx1YellowAlarm_Type.__name__ = "Integer32"
_UsdDsx1YellowAlarm_Object = MibTableColumn
usdDsx1YellowAlarm = _UsdDsx1YellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 12),
    _UsdDsx1YellowAlarm_Type()
)
usdDsx1YellowAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1YellowAlarm.setStatus("current")


class _UsdDsx1RemoteLoopback_Type(Integer32):
    """Custom type usdDsx1RemoteLoopback based on Integer32"""
    defaultValue = 0

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


_UsdDsx1RemoteLoopback_Type.__name__ = "Integer32"
_UsdDsx1RemoteLoopback_Object = MibTableColumn
usdDsx1RemoteLoopback = _UsdDsx1RemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 13),
    _UsdDsx1RemoteLoopback_Type()
)
usdDsx1RemoteLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1RemoteLoopback.setStatus("current")


class _UsdDsx1FdlCarrier_Type(Integer32):
    """Custom type usdDsx1FdlCarrier based on Integer32"""
    defaultValue = 0

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


_UsdDsx1FdlCarrier_Type.__name__ = "Integer32"
_UsdDsx1FdlCarrier_Object = MibTableColumn
usdDsx1FdlCarrier = _UsdDsx1FdlCarrier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 14),
    _UsdDsx1FdlCarrier_Type()
)
usdDsx1FdlCarrier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlCarrier.setStatus("current")


class _UsdDsx1FdlEic_Type(DisplayString):
    """Custom type usdDsx1FdlEic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdDsx1FdlEic_Type.__name__ = "DisplayString"
_UsdDsx1FdlEic_Object = MibTableColumn
usdDsx1FdlEic = _UsdDsx1FdlEic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 15),
    _UsdDsx1FdlEic_Type()
)
usdDsx1FdlEic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlEic.setStatus("current")


class _UsdDsx1FdlLic_Type(DisplayString):
    """Custom type usdDsx1FdlLic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_UsdDsx1FdlLic_Type.__name__ = "DisplayString"
_UsdDsx1FdlLic_Object = MibTableColumn
usdDsx1FdlLic = _UsdDsx1FdlLic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 16),
    _UsdDsx1FdlLic_Type()
)
usdDsx1FdlLic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlLic.setStatus("current")


class _UsdDsx1FdlFic_Type(DisplayString):
    """Custom type usdDsx1FdlFic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdDsx1FdlFic_Type.__name__ = "DisplayString"
_UsdDsx1FdlFic_Object = MibTableColumn
usdDsx1FdlFic = _UsdDsx1FdlFic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 17),
    _UsdDsx1FdlFic_Type()
)
usdDsx1FdlFic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlFic.setStatus("current")


class _UsdDsx1FdlUnit_Type(DisplayString):
    """Custom type usdDsx1FdlUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_UsdDsx1FdlUnit_Type.__name__ = "DisplayString"
_UsdDsx1FdlUnit_Object = MibTableColumn
usdDsx1FdlUnit = _UsdDsx1FdlUnit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 18),
    _UsdDsx1FdlUnit_Type()
)
usdDsx1FdlUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlUnit.setStatus("current")


class _UsdDsx1FdlPfi_Type(DisplayString):
    """Custom type usdDsx1FdlPfi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_UsdDsx1FdlPfi_Type.__name__ = "DisplayString"
_UsdDsx1FdlPfi_Object = MibTableColumn
usdDsx1FdlPfi = _UsdDsx1FdlPfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 19),
    _UsdDsx1FdlPfi_Type()
)
usdDsx1FdlPfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlPfi.setStatus("current")


class _UsdDsx1FdlPort_Type(DisplayString):
    """Custom type usdDsx1FdlPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UsdDsx1FdlPort_Type.__name__ = "DisplayString"
_UsdDsx1FdlPort_Object = MibTableColumn
usdDsx1FdlPort = _UsdDsx1FdlPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 20),
    _UsdDsx1FdlPort_Type()
)
usdDsx1FdlPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlPort.setStatus("current")


class _UsdDsx1FdlGenerator_Type(DisplayString):
    """Custom type usdDsx1FdlGenerator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_UsdDsx1FdlGenerator_Type.__name__ = "DisplayString"
_UsdDsx1FdlGenerator_Object = MibTableColumn
usdDsx1FdlGenerator = _UsdDsx1FdlGenerator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 21),
    _UsdDsx1FdlGenerator_Type()
)
usdDsx1FdlGenerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx1FdlGenerator.setStatus("current")
_UsdDs1NextIfIndex_Type = UsdNextIfIndex
_UsdDs1NextIfIndex_Object = MibScalar
usdDs1NextIfIndex = _UsdDs1NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 2),
    _UsdDs1NextIfIndex_Type()
)
usdDs1NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDs1NextIfIndex.setStatus("current")
_UsdDs1Conformance_ObjectIdentity = ObjectIdentity
usdDs1Conformance = _UsdDs1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4)
)
_UsdDs1Compliances_ObjectIdentity = ObjectIdentity
usdDs1Compliances = _UsdDs1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1)
)
_UsdDs1Groups_ObjectIdentity = ObjectIdentity
usdDs1Groups = _UsdDs1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2)
)

# Managed Objects groups

usdDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 1)
)
usdDs1Group.setObjects(
      *(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"))
)
if mibBuilder.loadTexts:
    usdDs1Group.setStatus("obsolete")

usdDs1Group1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 2)
)
usdDs1Group1.setObjects(
      *(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Capabilities"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Mode"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutCapabilities"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutType"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineAttenuation"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineLength"))
)
if mibBuilder.loadTexts:
    usdDs1Group1.setStatus("obsolete")

usdDs1Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 3)
)
usdDs1Group2.setObjects(
      *(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Capabilities"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Mode"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutCapabilities"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutType"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineAttenuation"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineLength"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LowerIfIndex"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1RowStatus"),
        ("Unisphere-Data-DS1-MIB", "usdDs1NextIfIndex"))
)
if mibBuilder.loadTexts:
    usdDs1Group2.setStatus("obsolete")

usdDs1Group3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 4)
)
usdDs1Group3.setObjects(
      *(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Capabilities"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1Mode"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutCapabilities"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutType"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineAttenuation"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LineLength"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1LowerIfIndex"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1RowStatus"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1SendCode"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1YellowAlarm"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1RemoteLoopback"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlCarrier"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlEic"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlLic"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlFic"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlUnit"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlPfi"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlPort"),
        ("Unisphere-Data-DS1-MIB", "usdDsx1FdlGenerator"),
        ("Unisphere-Data-DS1-MIB", "usdDs1NextIfIndex"))
)
if mibBuilder.loadTexts:
    usdDs1Group3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdDs1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdDs1Compliance.setStatus(
        "obsolete"
    )

usdDs1Compliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdDs1Compliance1.setStatus(
        "obsolete"
    )

usdDs1Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdDs1Compliance2.setStatus(
        "obsolete"
    )

usdDs1Compliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdDs1Compliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DS1-MIB",
    **{"usdDs1MIB": usdDs1MIB,
       "usdDs1Objects": usdDs1Objects,
       "usdDsx1ConfigTable": usdDsx1ConfigTable,
       "usdDsx1ConfigEntry": usdDsx1ConfigEntry,
       "usdDsx1TimeSlotMap": usdDsx1TimeSlotMap,
       "usdDsx1Ds1ChannelNumber": usdDsx1Ds1ChannelNumber,
       "usdDsx1Capabilities": usdDsx1Capabilities,
       "usdDsx1Mode": usdDsx1Mode,
       "usdDsx1LineBuildOutCapabilities": usdDsx1LineBuildOutCapabilities,
       "usdDsx1LineBuildOutType": usdDsx1LineBuildOutType,
       "usdDsx1LineAttenuation": usdDsx1LineAttenuation,
       "usdDsx1LineLength": usdDsx1LineLength,
       "usdDsx1LowerIfIndex": usdDsx1LowerIfIndex,
       "usdDsx1RowStatus": usdDsx1RowStatus,
       "usdDsx1SendCode": usdDsx1SendCode,
       "usdDsx1YellowAlarm": usdDsx1YellowAlarm,
       "usdDsx1RemoteLoopback": usdDsx1RemoteLoopback,
       "usdDsx1FdlCarrier": usdDsx1FdlCarrier,
       "usdDsx1FdlEic": usdDsx1FdlEic,
       "usdDsx1FdlLic": usdDsx1FdlLic,
       "usdDsx1FdlFic": usdDsx1FdlFic,
       "usdDsx1FdlUnit": usdDsx1FdlUnit,
       "usdDsx1FdlPfi": usdDsx1FdlPfi,
       "usdDsx1FdlPort": usdDsx1FdlPort,
       "usdDsx1FdlGenerator": usdDsx1FdlGenerator,
       "usdDs1NextIfIndex": usdDs1NextIfIndex,
       "usdDs1Conformance": usdDs1Conformance,
       "usdDs1Compliances": usdDs1Compliances,
       "usdDs1Compliance": usdDs1Compliance,
       "usdDs1Compliance1": usdDs1Compliance1,
       "usdDs1Compliance2": usdDs1Compliance2,
       "usdDs1Compliance3": usdDs1Compliance3,
       "usdDs1Groups": usdDs1Groups,
       "usdDs1Group": usdDs1Group,
       "usdDs1Group1": usdDs1Group1,
       "usdDs1Group2": usdDs1Group2,
       "usdDs1Group3": usdDs1Group3}
)
