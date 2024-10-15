# SNMP MIB module (Unisphere-Data-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:34 2024
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

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(dsx3FarEndCurrentEntry,
 dsx3FarEndIntervalEntry,
 dsx3FarEndTotalEntry) = mibBuilder.importSymbols(
    "RFC1407-MIB",
    "dsx3FarEndCurrentEntry",
    "dsx3FarEndIntervalEntry",
    "dsx3FarEndTotalEntry")

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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdDs3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4)
)
usdDs3MIB.setRevisions(
        ("2002-04-04 14:07",
         "2002-02-22 21:21",
         "2001-04-27 19:49",
         "2001-02-05 00:00",
         "1999-07-27 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdDs3Objects_ObjectIdentity = ObjectIdentity
usdDs3Objects = _UsdDs3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1)
)
_UsdDsx3ConfigTable_Object = MibTable
usdDsx3ConfigTable = _UsdDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdDsx3ConfigTable.setStatus("current")
_UsdDsx3ConfigEntry_Object = MibTableRow
usdDsx3ConfigEntry = _UsdDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1)
)
usdDsx3ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdDsx3ConfigEntry.setStatus("current")


class _UsdDsx3LineLength_Type(Integer32):
    """Custom type usdDsx3LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_UsdDsx3LineLength_Type.__name__ = "Integer32"
_UsdDsx3LineLength_Object = MibTableColumn
usdDsx3LineLength = _UsdDsx3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 1),
    _UsdDsx3LineLength_Type()
)
usdDsx3LineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3LineLength.setStatus("current")
if mibBuilder.loadTexts:
    usdDsx3LineLength.setUnits("meters")


class _UsdDsx3LineType_Type(Integer32):
    """Custom type usdDsx3LineType based on Integer32"""
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
              18,
              20)
        )
    )
    namedValues = NamedValues(
        *(("usdDsx3CbitParity", 4),
          ("usdDsx3CbitParityPlcp", 20),
          ("usdDsx3ClearChannel", 5),
          ("usdDsx3M23", 2),
          ("usdDsx3M23Plcp", 18),
          ("usdDsx3SYNTRAN", 3),
          ("usdDsx3other", 1),
          ("usdE3Framed", 7),
          ("usdE3G832", 6),
          ("usdE3Plcp", 8))
    )


_UsdDsx3LineType_Type.__name__ = "Integer32"
_UsdDsx3LineType_Object = MibTableColumn
usdDsx3LineType = _UsdDsx3LineType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 2),
    _UsdDsx3LineType_Type()
)
usdDsx3LineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3LineType.setStatus("current")


class _UsdDsx3CellScramblerConfig_Type(Integer32):
    """Custom type usdDsx3CellScramblerConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("scramblerOff", 2),
          ("scramblerOn", 1))
    )


_UsdDsx3CellScramblerConfig_Type.__name__ = "Integer32"
_UsdDsx3CellScramblerConfig_Object = MibTableColumn
usdDsx3CellScramblerConfig = _UsdDsx3CellScramblerConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 3),
    _UsdDsx3CellScramblerConfig_Type()
)
usdDsx3CellScramblerConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3CellScramblerConfig.setStatus("current")
_UsdDsx3Channelization_Type = TruthValue
_UsdDsx3Channelization_Object = MibTableColumn
usdDsx3Channelization = _UsdDsx3Channelization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 4),
    _UsdDsx3Channelization_Type()
)
usdDsx3Channelization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3Channelization.setStatus("current")


class _UsdDsx3InterfaceType_Type(Integer32):
    """Custom type usdDsx3InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds3E3", 1),
          ("ds3T3", 0))
    )


_UsdDsx3InterfaceType_Type.__name__ = "Integer32"
_UsdDsx3InterfaceType_Object = MibTableColumn
usdDsx3InterfaceType = _UsdDsx3InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 5),
    _UsdDsx3InterfaceType_Type()
)
usdDsx3InterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3InterfaceType.setStatus("current")


class _UsdDsx3Application_Type(Integer32):
    """Custom type usdDsx3Application based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds3AtmOverDs3", 1),
          ("ds3FrameOverDs3", 0))
    )


_UsdDsx3Application_Type.__name__ = "Integer32"
_UsdDsx3Application_Object = MibTableColumn
usdDsx3Application = _UsdDsx3Application_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 6),
    _UsdDsx3Application_Type()
)
usdDsx3Application.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3Application.setStatus("current")


class _UsdDsx3Ds3Channel_Type(Integer32):
    """Custom type usdDsx3Ds3Channel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_UsdDsx3Ds3Channel_Type.__name__ = "Integer32"
_UsdDsx3Ds3Channel_Object = MibTableColumn
usdDsx3Ds3Channel = _UsdDsx3Ds3Channel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 7),
    _UsdDsx3Ds3Channel_Type()
)
usdDsx3Ds3Channel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3Ds3Channel.setStatus("current")
_UsdDsx3LowerIfIndex_Type = InterfaceIndexOrZero
_UsdDsx3LowerIfIndex_Object = MibTableColumn
usdDsx3LowerIfIndex = _UsdDsx3LowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 8),
    _UsdDsx3LowerIfIndex_Type()
)
usdDsx3LowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3LowerIfIndex.setStatus("current")
_UsdDsx3RowStatus_Type = RowStatus
_UsdDsx3RowStatus_Object = MibTableColumn
usdDsx3RowStatus = _UsdDsx3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 9),
    _UsdDsx3RowStatus_Type()
)
usdDsx3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3RowStatus.setStatus("current")


class _UsdDsx3Ds3DsuMode_Type(Integer32):
    """Custom type usdDsx3Ds3DsuMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ds3DsuDigitalLink", 4),
          ("ds3DsuLarsCom", 2),
          ("ds3DsuModeNone", 0))
    )


_UsdDsx3Ds3DsuMode_Type.__name__ = "Integer32"
_UsdDsx3Ds3DsuMode_Object = MibTableColumn
usdDsx3Ds3DsuMode = _UsdDsx3Ds3DsuMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 10),
    _UsdDsx3Ds3DsuMode_Type()
)
usdDsx3Ds3DsuMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3Ds3DsuMode.setStatus("current")


class _UsdDsx3Ds3BandwidthLimit_Type(Integer32):
    """Custom type usdDsx3Ds3BandwidthLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_UsdDsx3Ds3BandwidthLimit_Type.__name__ = "Integer32"
_UsdDsx3Ds3BandwidthLimit_Object = MibTableColumn
usdDsx3Ds3BandwidthLimit = _UsdDsx3Ds3BandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 11),
    _UsdDsx3Ds3BandwidthLimit_Type()
)
usdDsx3Ds3BandwidthLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3Ds3BandwidthLimit.setStatus("current")


class _UsdDsx3Ds3DsuScrambleMode_Type(Integer32):
    """Custom type usdDsx3Ds3DsuScrambleMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds3DsuScrambleDisabled", 0),
          ("ds3DsuScrambleEnable", 1))
    )


_UsdDsx3Ds3DsuScrambleMode_Type.__name__ = "Integer32"
_UsdDsx3Ds3DsuScrambleMode_Object = MibTableColumn
usdDsx3Ds3DsuScrambleMode = _UsdDsx3Ds3DsuScrambleMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 12),
    _UsdDsx3Ds3DsuScrambleMode_Type()
)
usdDsx3Ds3DsuScrambleMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3Ds3DsuScrambleMode.setStatus("current")


class _UsdDsx3MdlCarrier_Type(Integer32):
    """Custom type usdDsx3MdlCarrier based on Integer32"""
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


_UsdDsx3MdlCarrier_Type.__name__ = "Integer32"
_UsdDsx3MdlCarrier_Object = MibTableColumn
usdDsx3MdlCarrier = _UsdDsx3MdlCarrier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 13),
    _UsdDsx3MdlCarrier_Type()
)
usdDsx3MdlCarrier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlCarrier.setStatus("current")


class _UsdDsx3MdlTransmit_Type(Integer32):
    """Custom type usdDsx3MdlTransmit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idlesignal", 2),
          ("none", 8),
          ("path", 1),
          ("testsignal", 4))
    )


_UsdDsx3MdlTransmit_Type.__name__ = "Integer32"
_UsdDsx3MdlTransmit_Object = MibTableColumn
usdDsx3MdlTransmit = _UsdDsx3MdlTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 14),
    _UsdDsx3MdlTransmit_Type()
)
usdDsx3MdlTransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlTransmit.setStatus("current")


class _UsdDsx3MdlEic_Type(DisplayString):
    """Custom type usdDsx3MdlEic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdDsx3MdlEic_Type.__name__ = "DisplayString"
_UsdDsx3MdlEic_Object = MibTableColumn
usdDsx3MdlEic = _UsdDsx3MdlEic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 15),
    _UsdDsx3MdlEic_Type()
)
usdDsx3MdlEic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlEic.setStatus("current")


class _UsdDsx3MdlLic_Type(DisplayString):
    """Custom type usdDsx3MdlLic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_UsdDsx3MdlLic_Type.__name__ = "DisplayString"
_UsdDsx3MdlLic_Object = MibTableColumn
usdDsx3MdlLic = _UsdDsx3MdlLic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 16),
    _UsdDsx3MdlLic_Type()
)
usdDsx3MdlLic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlLic.setStatus("current")


class _UsdDsx3MdlFic_Type(DisplayString):
    """Custom type usdDsx3MdlFic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdDsx3MdlFic_Type.__name__ = "DisplayString"
_UsdDsx3MdlFic_Object = MibTableColumn
usdDsx3MdlFic = _UsdDsx3MdlFic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 17),
    _UsdDsx3MdlFic_Type()
)
usdDsx3MdlFic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlFic.setStatus("current")


class _UsdDsx3MdlUnit_Type(DisplayString):
    """Custom type usdDsx3MdlUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_UsdDsx3MdlUnit_Type.__name__ = "DisplayString"
_UsdDsx3MdlUnit_Object = MibTableColumn
usdDsx3MdlUnit = _UsdDsx3MdlUnit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 18),
    _UsdDsx3MdlUnit_Type()
)
usdDsx3MdlUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlUnit.setStatus("current")


class _UsdDsx3MdlPfi_Type(DisplayString):
    """Custom type usdDsx3MdlPfi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_UsdDsx3MdlPfi_Type.__name__ = "DisplayString"
_UsdDsx3MdlPfi_Object = MibTableColumn
usdDsx3MdlPfi = _UsdDsx3MdlPfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 19),
    _UsdDsx3MdlPfi_Type()
)
usdDsx3MdlPfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlPfi.setStatus("current")


class _UsdDsx3MdlPort_Type(DisplayString):
    """Custom type usdDsx3MdlPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_UsdDsx3MdlPort_Type.__name__ = "DisplayString"
_UsdDsx3MdlPort_Object = MibTableColumn
usdDsx3MdlPort = _UsdDsx3MdlPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 20),
    _UsdDsx3MdlPort_Type()
)
usdDsx3MdlPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlPort.setStatus("current")


class _UsdDsx3MdlGenerator_Type(DisplayString):
    """Custom type usdDsx3MdlGenerator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_UsdDsx3MdlGenerator_Type.__name__ = "DisplayString"
_UsdDsx3MdlGenerator_Object = MibTableColumn
usdDsx3MdlGenerator = _UsdDsx3MdlGenerator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 21),
    _UsdDsx3MdlGenerator_Type()
)
usdDsx3MdlGenerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDsx3MdlGenerator.setStatus("current")
_UsdDs3NextIfIndex_Type = UsdNextIfIndex
_UsdDs3NextIfIndex_Object = MibScalar
usdDs3NextIfIndex = _UsdDs3NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 2),
    _UsdDs3NextIfIndex_Type()
)
usdDs3NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDs3NextIfIndex.setStatus("current")
_UsdDsx3FarEndCurrentTable_Object = MibTable
usdDsx3FarEndCurrentTable = _UsdDsx3FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdDsx3FarEndCurrentTable.setStatus("current")
_UsdDsx3FarEndCurrentEntry_Object = MibTableRow
usdDsx3FarEndCurrentEntry = _UsdDsx3FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    usdDsx3FarEndCurrentEntry.setStatus("current")
_UsdDsx3FarEndCurrentInvalidSeconds_Type = PerfCurrentCount
_UsdDsx3FarEndCurrentInvalidSeconds_Object = MibTableColumn
usdDsx3FarEndCurrentInvalidSeconds = _UsdDsx3FarEndCurrentInvalidSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3, 1, 1),
    _UsdDsx3FarEndCurrentInvalidSeconds_Type()
)
usdDsx3FarEndCurrentInvalidSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDsx3FarEndCurrentInvalidSeconds.setStatus("current")
_UsdDsx3FarEndIntervalTable_Object = MibTable
usdDsx3FarEndIntervalTable = _UsdDsx3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdDsx3FarEndIntervalTable.setStatus("current")
_UsdDsx3FarEndIntervalEntry_Object = MibTableRow
usdDsx3FarEndIntervalEntry = _UsdDsx3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    usdDsx3FarEndIntervalEntry.setStatus("current")
_UsdDsx3FarEndIntervalInvalidSeconds_Type = PerfIntervalCount
_UsdDsx3FarEndIntervalInvalidSeconds_Object = MibTableColumn
usdDsx3FarEndIntervalInvalidSeconds = _UsdDsx3FarEndIntervalInvalidSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4, 1, 1),
    _UsdDsx3FarEndIntervalInvalidSeconds_Type()
)
usdDsx3FarEndIntervalInvalidSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDsx3FarEndIntervalInvalidSeconds.setStatus("current")
_UsdDsx3FarEndTotalTable_Object = MibTable
usdDsx3FarEndTotalTable = _UsdDsx3FarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    usdDsx3FarEndTotalTable.setStatus("current")
_UsdDsx3FarEndTotalEntry_Object = MibTableRow
usdDsx3FarEndTotalEntry = _UsdDsx3FarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    usdDsx3FarEndTotalEntry.setStatus("current")
_UsdDsx3FarEndTotalInvalidSeconds_Type = PerfTotalCount
_UsdDsx3FarEndTotalInvalidSeconds_Object = MibTableColumn
usdDsx3FarEndTotalInvalidSeconds = _UsdDsx3FarEndTotalInvalidSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5, 1, 1),
    _UsdDsx3FarEndTotalInvalidSeconds_Type()
)
usdDsx3FarEndTotalInvalidSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDsx3FarEndTotalInvalidSeconds.setStatus("current")
_UsdDs3Conformance_ObjectIdentity = ObjectIdentity
usdDs3Conformance = _UsdDs3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4)
)
_UsdDs3Compliances_ObjectIdentity = ObjectIdentity
usdDs3Compliances = _UsdDs3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1)
)
_UsdDs3Groups_ObjectIdentity = ObjectIdentity
usdDs3Groups = _UsdDs3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2)
)
dsx3FarEndCurrentEntry.registerAugmentions(
    ("Unisphere-Data-DS3-MIB",
     "usdDsx3FarEndCurrentEntry")
)
usdDsx3FarEndCurrentEntry.setIndexNames(*dsx3FarEndCurrentEntry.getIndexNames())
dsx3FarEndIntervalEntry.registerAugmentions(
    ("Unisphere-Data-DS3-MIB",
     "usdDsx3FarEndIntervalEntry")
)
usdDsx3FarEndIntervalEntry.setIndexNames(*dsx3FarEndIntervalEntry.getIndexNames())
dsx3FarEndTotalEntry.registerAugmentions(
    ("Unisphere-Data-DS3-MIB",
     "usdDsx3FarEndTotalEntry")
)
usdDsx3FarEndTotalEntry.setIndexNames(*dsx3FarEndTotalEntry.getIndexNames())

# Managed Objects groups

usdDs3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 1)
)
usdDs3Group.setObjects(
    ("Unisphere-Data-DS3-MIB", "usdDsx3LineLength")
)
if mibBuilder.loadTexts:
    usdDs3Group.setStatus("obsolete")

usdDs3Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 2)
)
usdDs3Group2.setObjects(
      *(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"))
)
if mibBuilder.loadTexts:
    usdDs3Group2.setStatus("obsolete")

usdDs3Group3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 3)
)
usdDs3Group3.setObjects(
      *(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuMode"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3BandwidthLimit"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuScrambleMode"))
)
if mibBuilder.loadTexts:
    usdDs3Group3.setStatus("obsolete")

usdDs3Group4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 4)
)
usdDs3Group4.setObjects(
      *(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Channelization"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3InterfaceType"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Application"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3Channel"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3LowerIfIndex"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3RowStatus"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuMode"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3BandwidthLimit"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuScrambleMode"),
        ("Unisphere-Data-DS3-MIB", "usdDs3NextIfIndex"))
)
if mibBuilder.loadTexts:
    usdDs3Group4.setStatus("obsolete")

usdDs3Group5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 5)
)
usdDs3Group5.setObjects(
      *(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Channelization"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3InterfaceType"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Application"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3Channel"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3LowerIfIndex"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3RowStatus"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuMode"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3BandwidthLimit"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuScrambleMode"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlCarrier"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlTransmit"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlEic"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlLic"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlFic"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlUnit"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlPfi"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlPort"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3MdlGenerator"),
        ("Unisphere-Data-DS3-MIB", "usdDs3NextIfIndex"))
)
if mibBuilder.loadTexts:
    usdDs3Group5.setStatus("current")

usdDs3FarEndGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 6)
)
usdDs3FarEndGroup.setObjects(
      *(("Unisphere-Data-DS3-MIB", "usdDsx3FarEndCurrentInvalidSeconds"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3FarEndIntervalInvalidSeconds"),
        ("Unisphere-Data-DS3-MIB", "usdDsx3FarEndTotalInvalidSeconds"))
)
if mibBuilder.loadTexts:
    usdDs3FarEndGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdDs3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdDs3Compliance.setStatus(
        "obsolete"
    )

usdDs3Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdDs3Compliance2.setStatus(
        "obsolete"
    )

usdDs3Compliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdDs3Compliance3.setStatus(
        "obsolete"
    )

usdDs3Compliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdDs3Compliance4.setStatus(
        "obsolete"
    )

usdDs3Compliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 5)
)
if mibBuilder.loadTexts:
    usdDs3Compliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DS3-MIB",
    **{"usdDs3MIB": usdDs3MIB,
       "usdDs3Objects": usdDs3Objects,
       "usdDsx3ConfigTable": usdDsx3ConfigTable,
       "usdDsx3ConfigEntry": usdDsx3ConfigEntry,
       "usdDsx3LineLength": usdDsx3LineLength,
       "usdDsx3LineType": usdDsx3LineType,
       "usdDsx3CellScramblerConfig": usdDsx3CellScramblerConfig,
       "usdDsx3Channelization": usdDsx3Channelization,
       "usdDsx3InterfaceType": usdDsx3InterfaceType,
       "usdDsx3Application": usdDsx3Application,
       "usdDsx3Ds3Channel": usdDsx3Ds3Channel,
       "usdDsx3LowerIfIndex": usdDsx3LowerIfIndex,
       "usdDsx3RowStatus": usdDsx3RowStatus,
       "usdDsx3Ds3DsuMode": usdDsx3Ds3DsuMode,
       "usdDsx3Ds3BandwidthLimit": usdDsx3Ds3BandwidthLimit,
       "usdDsx3Ds3DsuScrambleMode": usdDsx3Ds3DsuScrambleMode,
       "usdDsx3MdlCarrier": usdDsx3MdlCarrier,
       "usdDsx3MdlTransmit": usdDsx3MdlTransmit,
       "usdDsx3MdlEic": usdDsx3MdlEic,
       "usdDsx3MdlLic": usdDsx3MdlLic,
       "usdDsx3MdlFic": usdDsx3MdlFic,
       "usdDsx3MdlUnit": usdDsx3MdlUnit,
       "usdDsx3MdlPfi": usdDsx3MdlPfi,
       "usdDsx3MdlPort": usdDsx3MdlPort,
       "usdDsx3MdlGenerator": usdDsx3MdlGenerator,
       "usdDs3NextIfIndex": usdDs3NextIfIndex,
       "usdDsx3FarEndCurrentTable": usdDsx3FarEndCurrentTable,
       "usdDsx3FarEndCurrentEntry": usdDsx3FarEndCurrentEntry,
       "usdDsx3FarEndCurrentInvalidSeconds": usdDsx3FarEndCurrentInvalidSeconds,
       "usdDsx3FarEndIntervalTable": usdDsx3FarEndIntervalTable,
       "usdDsx3FarEndIntervalEntry": usdDsx3FarEndIntervalEntry,
       "usdDsx3FarEndIntervalInvalidSeconds": usdDsx3FarEndIntervalInvalidSeconds,
       "usdDsx3FarEndTotalTable": usdDsx3FarEndTotalTable,
       "usdDsx3FarEndTotalEntry": usdDsx3FarEndTotalEntry,
       "usdDsx3FarEndTotalInvalidSeconds": usdDsx3FarEndTotalInvalidSeconds,
       "usdDs3Conformance": usdDs3Conformance,
       "usdDs3Compliances": usdDs3Compliances,
       "usdDs3Compliance": usdDs3Compliance,
       "usdDs3Compliance2": usdDs3Compliance2,
       "usdDs3Compliance3": usdDs3Compliance3,
       "usdDs3Compliance4": usdDs3Compliance4,
       "usdDs3Compliance5": usdDs3Compliance5,
       "usdDs3Groups": usdDs3Groups,
       "usdDs3Group": usdDs3Group,
       "usdDs3Group2": usdDs3Group2,
       "usdDs3Group3": usdDs3Group3,
       "usdDs3Group4": usdDs3Group4,
       "usdDs3Group5": usdDs3Group5,
       "usdDs3FarEndGroup": usdDs3FarEndGroup}
)
