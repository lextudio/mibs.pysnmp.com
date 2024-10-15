# SNMP MIB module (Juniper-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:03 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,
 JuniTimeSlotMap) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex",
    "JuniTimeSlotMap")

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

juniDs1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5)
)
juniDs1MIB.setRevisions(
        ("2003-02-10 15:07",
         "2002-09-12 16:59",
         "2002-05-13 16:01",
         "2001-07-31 18:25",
         "2001-04-04 18:05",
         "1999-06-17 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniDs1Objects_ObjectIdentity = ObjectIdentity
juniDs1Objects = _JuniDs1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1)
)
_JuniDsx1ConfigTable_Object = MibTable
juniDsx1ConfigTable = _JuniDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    juniDsx1ConfigTable.setStatus("current")
_JuniDsx1ConfigEntry_Object = MibTableRow
juniDsx1ConfigEntry = _JuniDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1)
)
juniDsx1ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniDsx1ConfigEntry.setStatus("current")
_JuniDsx1TimeSlotMap_Type = JuniTimeSlotMap
_JuniDsx1TimeSlotMap_Object = MibTableColumn
juniDsx1TimeSlotMap = _JuniDsx1TimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 1),
    _JuniDsx1TimeSlotMap_Type()
)
juniDsx1TimeSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1TimeSlotMap.setStatus("current")


class _JuniDsx1Ds1ChannelNumber_Type(Integer32):
    """Custom type juniDsx1Ds1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_JuniDsx1Ds1ChannelNumber_Type.__name__ = "Integer32"
_JuniDsx1Ds1ChannelNumber_Object = MibTableColumn
juniDsx1Ds1ChannelNumber = _JuniDsx1Ds1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 2),
    _JuniDsx1Ds1ChannelNumber_Type()
)
juniDsx1Ds1ChannelNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1Ds1ChannelNumber.setStatus("current")


class _JuniDsx1Capabilities_Type(Integer32):
    """Custom type juniDsx1Capabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JuniDsx1Capabilities_Type.__name__ = "Integer32"
_JuniDsx1Capabilities_Object = MibTableColumn
juniDsx1Capabilities = _JuniDsx1Capabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 3),
    _JuniDsx1Capabilities_Type()
)
juniDsx1Capabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1Capabilities.setStatus("current")


class _JuniDsx1Mode_Type(Integer32):
    """Custom type juniDsx1Mode based on Integer32"""
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


_JuniDsx1Mode_Type.__name__ = "Integer32"
_JuniDsx1Mode_Object = MibTableColumn
juniDsx1Mode = _JuniDsx1Mode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 4),
    _JuniDsx1Mode_Type()
)
juniDsx1Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1Mode.setStatus("current")


class _JuniDsx1LineBuildOutCapabilities_Type(Integer32):
    """Custom type juniDsx1LineBuildOutCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_JuniDsx1LineBuildOutCapabilities_Type.__name__ = "Integer32"
_JuniDsx1LineBuildOutCapabilities_Object = MibTableColumn
juniDsx1LineBuildOutCapabilities = _JuniDsx1LineBuildOutCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 5),
    _JuniDsx1LineBuildOutCapabilities_Type()
)
juniDsx1LineBuildOutCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1LineBuildOutCapabilities.setStatus("current")


class _JuniDsx1LineBuildOutType_Type(Integer32):
    """Custom type juniDsx1LineBuildOutType based on Integer32"""
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


_JuniDsx1LineBuildOutType_Type.__name__ = "Integer32"
_JuniDsx1LineBuildOutType_Object = MibTableColumn
juniDsx1LineBuildOutType = _JuniDsx1LineBuildOutType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 6),
    _JuniDsx1LineBuildOutType_Type()
)
juniDsx1LineBuildOutType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1LineBuildOutType.setStatus("current")


class _JuniDsx1LineAttenuation_Type(Integer32):
    """Custom type juniDsx1LineAttenuation based on Integer32"""
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


_JuniDsx1LineAttenuation_Type.__name__ = "Integer32"
_JuniDsx1LineAttenuation_Object = MibTableColumn
juniDsx1LineAttenuation = _JuniDsx1LineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 7),
    _JuniDsx1LineAttenuation_Type()
)
juniDsx1LineAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1LineAttenuation.setStatus("current")


class _JuniDsx1LineLength_Type(Integer32):
    """Custom type juniDsx1LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_JuniDsx1LineLength_Type.__name__ = "Integer32"
_JuniDsx1LineLength_Object = MibTableColumn
juniDsx1LineLength = _JuniDsx1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 8),
    _JuniDsx1LineLength_Type()
)
juniDsx1LineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1LineLength.setStatus("current")
if mibBuilder.loadTexts:
    juniDsx1LineLength.setUnits("meters")
_JuniDsx1LowerIfIndex_Type = InterfaceIndexOrZero
_JuniDsx1LowerIfIndex_Object = MibTableColumn
juniDsx1LowerIfIndex = _JuniDsx1LowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 9),
    _JuniDsx1LowerIfIndex_Type()
)
juniDsx1LowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1LowerIfIndex.setStatus("current")
_JuniDsx1RowStatus_Type = RowStatus
_JuniDsx1RowStatus_Object = MibTableColumn
juniDsx1RowStatus = _JuniDsx1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 10),
    _JuniDsx1RowStatus_Type()
)
juniDsx1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1RowStatus.setStatus("current")


class _JuniDsx1SendCode_Type(Integer32):
    """Custom type juniDsx1SendCode based on Integer32"""
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


_JuniDsx1SendCode_Type.__name__ = "Integer32"
_JuniDsx1SendCode_Object = MibTableColumn
juniDsx1SendCode = _JuniDsx1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 11),
    _JuniDsx1SendCode_Type()
)
juniDsx1SendCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1SendCode.setStatus("current")


class _JuniDsx1YellowAlarm_Type(Integer32):
    """Custom type juniDsx1YellowAlarm based on Integer32"""
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
        *(("detect", 2),
          ("generate", 1),
          ("generateAndDetect", 3),
          ("none", 4))
    )


_JuniDsx1YellowAlarm_Type.__name__ = "Integer32"
_JuniDsx1YellowAlarm_Object = MibTableColumn
juniDsx1YellowAlarm = _JuniDsx1YellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 12),
    _JuniDsx1YellowAlarm_Type()
)
juniDsx1YellowAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1YellowAlarm.setStatus("current")


class _JuniDsx1RemoteLoopback_Type(Integer32):
    """Custom type juniDsx1RemoteLoopback based on Integer32"""
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


_JuniDsx1RemoteLoopback_Type.__name__ = "Integer32"
_JuniDsx1RemoteLoopback_Object = MibTableColumn
juniDsx1RemoteLoopback = _JuniDsx1RemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 13),
    _JuniDsx1RemoteLoopback_Type()
)
juniDsx1RemoteLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1RemoteLoopback.setStatus("current")


class _JuniDsx1FdlCarrier_Type(Integer32):
    """Custom type juniDsx1FdlCarrier based on Integer32"""
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


_JuniDsx1FdlCarrier_Type.__name__ = "Integer32"
_JuniDsx1FdlCarrier_Object = MibTableColumn
juniDsx1FdlCarrier = _JuniDsx1FdlCarrier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 14),
    _JuniDsx1FdlCarrier_Type()
)
juniDsx1FdlCarrier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlCarrier.setStatus("current")


class _JuniDsx1FdlEic_Type(DisplayString):
    """Custom type juniDsx1FdlEic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniDsx1FdlEic_Type.__name__ = "DisplayString"
_JuniDsx1FdlEic_Object = MibTableColumn
juniDsx1FdlEic = _JuniDsx1FdlEic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 15),
    _JuniDsx1FdlEic_Type()
)
juniDsx1FdlEic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlEic.setStatus("current")


class _JuniDsx1FdlLic_Type(DisplayString):
    """Custom type juniDsx1FdlLic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_JuniDsx1FdlLic_Type.__name__ = "DisplayString"
_JuniDsx1FdlLic_Object = MibTableColumn
juniDsx1FdlLic = _JuniDsx1FdlLic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 16),
    _JuniDsx1FdlLic_Type()
)
juniDsx1FdlLic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlLic.setStatus("current")


class _JuniDsx1FdlFic_Type(DisplayString):
    """Custom type juniDsx1FdlFic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniDsx1FdlFic_Type.__name__ = "DisplayString"
_JuniDsx1FdlFic_Object = MibTableColumn
juniDsx1FdlFic = _JuniDsx1FdlFic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 17),
    _JuniDsx1FdlFic_Type()
)
juniDsx1FdlFic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlFic.setStatus("current")


class _JuniDsx1FdlUnit_Type(DisplayString):
    """Custom type juniDsx1FdlUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_JuniDsx1FdlUnit_Type.__name__ = "DisplayString"
_JuniDsx1FdlUnit_Object = MibTableColumn
juniDsx1FdlUnit = _JuniDsx1FdlUnit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 18),
    _JuniDsx1FdlUnit_Type()
)
juniDsx1FdlUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlUnit.setStatus("current")


class _JuniDsx1FdlPfi_Type(DisplayString):
    """Custom type juniDsx1FdlPfi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx1FdlPfi_Type.__name__ = "DisplayString"
_JuniDsx1FdlPfi_Object = MibTableColumn
juniDsx1FdlPfi = _JuniDsx1FdlPfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 19),
    _JuniDsx1FdlPfi_Type()
)
juniDsx1FdlPfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlPfi.setStatus("current")


class _JuniDsx1FdlPort_Type(DisplayString):
    """Custom type juniDsx1FdlPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_JuniDsx1FdlPort_Type.__name__ = "DisplayString"
_JuniDsx1FdlPort_Object = MibTableColumn
juniDsx1FdlPort = _JuniDsx1FdlPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 20),
    _JuniDsx1FdlPort_Type()
)
juniDsx1FdlPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlPort.setStatus("current")


class _JuniDsx1FdlGenerator_Type(DisplayString):
    """Custom type juniDsx1FdlGenerator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx1FdlGenerator_Type.__name__ = "DisplayString"
_JuniDsx1FdlGenerator_Object = MibTableColumn
juniDsx1FdlGenerator = _JuniDsx1FdlGenerator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 21),
    _JuniDsx1FdlGenerator_Type()
)
juniDsx1FdlGenerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlGenerator.setStatus("current")


class _JuniDsx1FdlTransmit_Type(Bits):
    """Custom type juniDsx1FdlTransmit based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("idlesignal", 1),
          ("path", 0),
          ("testsignal", 2))
    )

_JuniDsx1FdlTransmit_Type.__name__ = "Bits"
_JuniDsx1FdlTransmit_Object = MibTableColumn
juniDsx1FdlTransmit = _JuniDsx1FdlTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 22),
    _JuniDsx1FdlTransmit_Type()
)
juniDsx1FdlTransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx1FdlTransmit.setStatus("current")
_JuniDs1NextIfIndex_Type = JuniNextIfIndex
_JuniDs1NextIfIndex_Object = MibScalar
juniDs1NextIfIndex = _JuniDs1NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 2),
    _JuniDs1NextIfIndex_Type()
)
juniDs1NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDs1NextIfIndex.setStatus("current")
_JuniDsx1FarEndConfigTable_Object = MibTable
juniDsx1FarEndConfigTable = _JuniDsx1FarEndConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    juniDsx1FarEndConfigTable.setStatus("current")
_JuniDsx1FarEndConfigEntry_Object = MibTableRow
juniDsx1FarEndConfigEntry = _JuniDsx1FarEndConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1)
)
juniDsx1FarEndConfigEntry.setIndexNames(
    (0, "Juniper-DS1-MIB", "juniDsx1FarEndLineIndex"),
)
if mibBuilder.loadTexts:
    juniDsx1FarEndConfigEntry.setStatus("current")


class _JuniDsx1FarEndLineIndex_Type(Integer32):
    """Custom type juniDsx1FarEndLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniDsx1FarEndLineIndex_Type.__name__ = "Integer32"
_JuniDsx1FarEndLineIndex_Object = MibTableColumn
juniDsx1FarEndLineIndex = _JuniDsx1FarEndLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 1),
    _JuniDsx1FarEndLineIndex_Type()
)
juniDsx1FarEndLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDsx1FarEndLineIndex.setStatus("current")


class _JuniDsx1FarEndEquipCode_Type(DisplayString):
    """Custom type juniDsx1FarEndEquipCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniDsx1FarEndEquipCode_Type.__name__ = "DisplayString"
_JuniDsx1FarEndEquipCode_Object = MibTableColumn
juniDsx1FarEndEquipCode = _JuniDsx1FarEndEquipCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 2),
    _JuniDsx1FarEndEquipCode_Type()
)
juniDsx1FarEndEquipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndEquipCode.setStatus("current")


class _JuniDsx1FarEndLocationIDCode_Type(DisplayString):
    """Custom type juniDsx1FarEndLocationIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_JuniDsx1FarEndLocationIDCode_Type.__name__ = "DisplayString"
_JuniDsx1FarEndLocationIDCode_Object = MibTableColumn
juniDsx1FarEndLocationIDCode = _JuniDsx1FarEndLocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 3),
    _JuniDsx1FarEndLocationIDCode_Type()
)
juniDsx1FarEndLocationIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndLocationIDCode.setStatus("current")


class _JuniDsx1FarEndFrameIDCode_Type(DisplayString):
    """Custom type juniDsx1FarEndFrameIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniDsx1FarEndFrameIDCode_Type.__name__ = "DisplayString"
_JuniDsx1FarEndFrameIDCode_Object = MibTableColumn
juniDsx1FarEndFrameIDCode = _JuniDsx1FarEndFrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 4),
    _JuniDsx1FarEndFrameIDCode_Type()
)
juniDsx1FarEndFrameIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndFrameIDCode.setStatus("current")


class _JuniDsx1FarEndUnitCode_Type(DisplayString):
    """Custom type juniDsx1FarEndUnitCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_JuniDsx1FarEndUnitCode_Type.__name__ = "DisplayString"
_JuniDsx1FarEndUnitCode_Object = MibTableColumn
juniDsx1FarEndUnitCode = _JuniDsx1FarEndUnitCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 5),
    _JuniDsx1FarEndUnitCode_Type()
)
juniDsx1FarEndUnitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndUnitCode.setStatus("current")


class _JuniDsx1FarEndFacilityIDCode_Type(DisplayString):
    """Custom type juniDsx1FarEndFacilityIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx1FarEndFacilityIDCode_Type.__name__ = "DisplayString"
_JuniDsx1FarEndFacilityIDCode_Object = MibTableColumn
juniDsx1FarEndFacilityIDCode = _JuniDsx1FarEndFacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 6),
    _JuniDsx1FarEndFacilityIDCode_Type()
)
juniDsx1FarEndFacilityIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndFacilityIDCode.setStatus("current")


class _JuniDsx1FarEndPortNumber_Type(DisplayString):
    """Custom type juniDsx1FarEndPortNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_JuniDsx1FarEndPortNumber_Type.__name__ = "DisplayString"
_JuniDsx1FarEndPortNumber_Object = MibTableColumn
juniDsx1FarEndPortNumber = _JuniDsx1FarEndPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 7),
    _JuniDsx1FarEndPortNumber_Type()
)
juniDsx1FarEndPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndPortNumber.setStatus("current")


class _JuniDsx1FarEndGeneratorNumber_Type(DisplayString):
    """Custom type juniDsx1FarEndGeneratorNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx1FarEndGeneratorNumber_Type.__name__ = "DisplayString"
_JuniDsx1FarEndGeneratorNumber_Object = MibTableColumn
juniDsx1FarEndGeneratorNumber = _JuniDsx1FarEndGeneratorNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 8),
    _JuniDsx1FarEndGeneratorNumber_Type()
)
juniDsx1FarEndGeneratorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndGeneratorNumber.setStatus("current")


class _JuniDsx1FarEndCarrier_Type(Integer32):
    """Custom type juniDsx1FarEndCarrier based on Integer32"""
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


_JuniDsx1FarEndCarrier_Type.__name__ = "Integer32"
_JuniDsx1FarEndCarrier_Object = MibTableColumn
juniDsx1FarEndCarrier = _JuniDsx1FarEndCarrier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 3, 1, 9),
    _JuniDsx1FarEndCarrier_Type()
)
juniDsx1FarEndCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx1FarEndCarrier.setStatus("current")
_JuniDs1Conformance_ObjectIdentity = ObjectIdentity
juniDs1Conformance = _JuniDs1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4)
)
_JuniDs1Compliances_ObjectIdentity = ObjectIdentity
juniDs1Compliances = _JuniDs1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1)
)
_JuniDs1Groups_ObjectIdentity = ObjectIdentity
juniDs1Groups = _JuniDs1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2)
)

# Managed Objects groups

juniDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 1)
)
juniDs1Group.setObjects(
      *(("Juniper-DS1-MIB", "juniDsx1TimeSlotMap"),
        ("Juniper-DS1-MIB", "juniDsx1Ds1ChannelNumber"))
)
if mibBuilder.loadTexts:
    juniDs1Group.setStatus("obsolete")

juniDs1Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 2)
)
juniDs1Group2.setObjects(
      *(("Juniper-DS1-MIB", "juniDsx1TimeSlotMap"),
        ("Juniper-DS1-MIB", "juniDsx1Ds1ChannelNumber"),
        ("Juniper-DS1-MIB", "juniDsx1Capabilities"),
        ("Juniper-DS1-MIB", "juniDsx1Mode"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutCapabilities"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutType"),
        ("Juniper-DS1-MIB", "juniDsx1LineAttenuation"),
        ("Juniper-DS1-MIB", "juniDsx1LineLength"))
)
if mibBuilder.loadTexts:
    juniDs1Group2.setStatus("obsolete")

juniDs1Group3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 3)
)
juniDs1Group3.setObjects(
      *(("Juniper-DS1-MIB", "juniDsx1TimeSlotMap"),
        ("Juniper-DS1-MIB", "juniDsx1Ds1ChannelNumber"),
        ("Juniper-DS1-MIB", "juniDsx1Capabilities"),
        ("Juniper-DS1-MIB", "juniDsx1Mode"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutCapabilities"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutType"),
        ("Juniper-DS1-MIB", "juniDsx1LineAttenuation"),
        ("Juniper-DS1-MIB", "juniDsx1LineLength"),
        ("Juniper-DS1-MIB", "juniDsx1LowerIfIndex"),
        ("Juniper-DS1-MIB", "juniDsx1RowStatus"),
        ("Juniper-DS1-MIB", "juniDs1NextIfIndex"))
)
if mibBuilder.loadTexts:
    juniDs1Group3.setStatus("obsolete")

juniDs1Group4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 4)
)
juniDs1Group4.setObjects(
      *(("Juniper-DS1-MIB", "juniDsx1TimeSlotMap"),
        ("Juniper-DS1-MIB", "juniDsx1Ds1ChannelNumber"),
        ("Juniper-DS1-MIB", "juniDsx1Capabilities"),
        ("Juniper-DS1-MIB", "juniDsx1Mode"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutCapabilities"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutType"),
        ("Juniper-DS1-MIB", "juniDsx1LineAttenuation"),
        ("Juniper-DS1-MIB", "juniDsx1LineLength"),
        ("Juniper-DS1-MIB", "juniDsx1LowerIfIndex"),
        ("Juniper-DS1-MIB", "juniDsx1RowStatus"),
        ("Juniper-DS1-MIB", "juniDsx1SendCode"),
        ("Juniper-DS1-MIB", "juniDsx1YellowAlarm"),
        ("Juniper-DS1-MIB", "juniDsx1RemoteLoopback"),
        ("Juniper-DS1-MIB", "juniDsx1FdlCarrier"),
        ("Juniper-DS1-MIB", "juniDsx1FdlEic"),
        ("Juniper-DS1-MIB", "juniDsx1FdlLic"),
        ("Juniper-DS1-MIB", "juniDsx1FdlFic"),
        ("Juniper-DS1-MIB", "juniDsx1FdlUnit"),
        ("Juniper-DS1-MIB", "juniDsx1FdlPfi"),
        ("Juniper-DS1-MIB", "juniDsx1FdlPort"),
        ("Juniper-DS1-MIB", "juniDsx1FdlGenerator"),
        ("Juniper-DS1-MIB", "juniDs1NextIfIndex"))
)
if mibBuilder.loadTexts:
    juniDs1Group4.setStatus("obsolete")

juniDs1Group5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 5)
)
juniDs1Group5.setObjects(
      *(("Juniper-DS1-MIB", "juniDsx1TimeSlotMap"),
        ("Juniper-DS1-MIB", "juniDsx1Ds1ChannelNumber"),
        ("Juniper-DS1-MIB", "juniDsx1Capabilities"),
        ("Juniper-DS1-MIB", "juniDsx1Mode"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutCapabilities"),
        ("Juniper-DS1-MIB", "juniDsx1LineBuildOutType"),
        ("Juniper-DS1-MIB", "juniDsx1LineAttenuation"),
        ("Juniper-DS1-MIB", "juniDsx1LineLength"),
        ("Juniper-DS1-MIB", "juniDsx1LowerIfIndex"),
        ("Juniper-DS1-MIB", "juniDsx1RowStatus"),
        ("Juniper-DS1-MIB", "juniDsx1SendCode"),
        ("Juniper-DS1-MIB", "juniDsx1YellowAlarm"),
        ("Juniper-DS1-MIB", "juniDsx1RemoteLoopback"),
        ("Juniper-DS1-MIB", "juniDsx1FdlCarrier"),
        ("Juniper-DS1-MIB", "juniDsx1FdlEic"),
        ("Juniper-DS1-MIB", "juniDsx1FdlLic"),
        ("Juniper-DS1-MIB", "juniDsx1FdlFic"),
        ("Juniper-DS1-MIB", "juniDsx1FdlUnit"),
        ("Juniper-DS1-MIB", "juniDsx1FdlPfi"),
        ("Juniper-DS1-MIB", "juniDsx1FdlPort"),
        ("Juniper-DS1-MIB", "juniDsx1FdlGenerator"),
        ("Juniper-DS1-MIB", "juniDsx1FdlTransmit"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndEquipCode"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndLocationIDCode"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndFrameIDCode"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndUnitCode"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndFacilityIDCode"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndPortNumber"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndGeneratorNumber"),
        ("Juniper-DS1-MIB", "juniDsx1FarEndCarrier"),
        ("Juniper-DS1-MIB", "juniDs1NextIfIndex"))
)
if mibBuilder.loadTexts:
    juniDs1Group5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniDs1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniDs1Compliance.setStatus(
        "obsolete"
    )

juniDs1Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniDs1Compliance2.setStatus(
        "obsolete"
    )

juniDs1Compliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniDs1Compliance3.setStatus(
        "obsolete"
    )

juniDs1Compliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniDs1Compliance4.setStatus(
        "obsolete"
    )

juniDs1Compliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniDs1Compliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DS1-MIB",
    **{"juniDs1MIB": juniDs1MIB,
       "juniDs1Objects": juniDs1Objects,
       "juniDsx1ConfigTable": juniDsx1ConfigTable,
       "juniDsx1ConfigEntry": juniDsx1ConfigEntry,
       "juniDsx1TimeSlotMap": juniDsx1TimeSlotMap,
       "juniDsx1Ds1ChannelNumber": juniDsx1Ds1ChannelNumber,
       "juniDsx1Capabilities": juniDsx1Capabilities,
       "juniDsx1Mode": juniDsx1Mode,
       "juniDsx1LineBuildOutCapabilities": juniDsx1LineBuildOutCapabilities,
       "juniDsx1LineBuildOutType": juniDsx1LineBuildOutType,
       "juniDsx1LineAttenuation": juniDsx1LineAttenuation,
       "juniDsx1LineLength": juniDsx1LineLength,
       "juniDsx1LowerIfIndex": juniDsx1LowerIfIndex,
       "juniDsx1RowStatus": juniDsx1RowStatus,
       "juniDsx1SendCode": juniDsx1SendCode,
       "juniDsx1YellowAlarm": juniDsx1YellowAlarm,
       "juniDsx1RemoteLoopback": juniDsx1RemoteLoopback,
       "juniDsx1FdlCarrier": juniDsx1FdlCarrier,
       "juniDsx1FdlEic": juniDsx1FdlEic,
       "juniDsx1FdlLic": juniDsx1FdlLic,
       "juniDsx1FdlFic": juniDsx1FdlFic,
       "juniDsx1FdlUnit": juniDsx1FdlUnit,
       "juniDsx1FdlPfi": juniDsx1FdlPfi,
       "juniDsx1FdlPort": juniDsx1FdlPort,
       "juniDsx1FdlGenerator": juniDsx1FdlGenerator,
       "juniDsx1FdlTransmit": juniDsx1FdlTransmit,
       "juniDs1NextIfIndex": juniDs1NextIfIndex,
       "juniDsx1FarEndConfigTable": juniDsx1FarEndConfigTable,
       "juniDsx1FarEndConfigEntry": juniDsx1FarEndConfigEntry,
       "juniDsx1FarEndLineIndex": juniDsx1FarEndLineIndex,
       "juniDsx1FarEndEquipCode": juniDsx1FarEndEquipCode,
       "juniDsx1FarEndLocationIDCode": juniDsx1FarEndLocationIDCode,
       "juniDsx1FarEndFrameIDCode": juniDsx1FarEndFrameIDCode,
       "juniDsx1FarEndUnitCode": juniDsx1FarEndUnitCode,
       "juniDsx1FarEndFacilityIDCode": juniDsx1FarEndFacilityIDCode,
       "juniDsx1FarEndPortNumber": juniDsx1FarEndPortNumber,
       "juniDsx1FarEndGeneratorNumber": juniDsx1FarEndGeneratorNumber,
       "juniDsx1FarEndCarrier": juniDsx1FarEndCarrier,
       "juniDs1Conformance": juniDs1Conformance,
       "juniDs1Compliances": juniDs1Compliances,
       "juniDs1Compliance": juniDs1Compliance,
       "juniDs1Compliance2": juniDs1Compliance2,
       "juniDs1Compliance3": juniDs1Compliance3,
       "juniDs1Compliance4": juniDs1Compliance4,
       "juniDs1Compliance5": juniDs1Compliance5,
       "juniDs1Groups": juniDs1Groups,
       "juniDs1Group": juniDs1Group,
       "juniDs1Group2": juniDs1Group2,
       "juniDs1Group3": juniDs1Group3,
       "juniDs1Group4": juniDs1Group4,
       "juniDs1Group5": juniDs1Group5}
)
