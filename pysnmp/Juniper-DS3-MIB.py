# SNMP MIB module (Juniper-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:05 2024
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

(dsx3FarEndConfigEntry,
 dsx3FarEndCurrentEntry,
 dsx3FarEndIntervalEntry,
 dsx3FarEndTotalEntry) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3FarEndConfigEntry",
    "dsx3FarEndCurrentEntry",
    "dsx3FarEndIntervalEntry",
    "dsx3FarEndTotalEntry")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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

juniDs3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4)
)
juniDs3MIB.setRevisions(
        ("2004-10-12 06:51",
         "2003-09-30 12:11",
         "2002-09-16 21:44",
         "2002-09-12 16:59",
         "2002-04-04 14:07",
         "2002-02-22 21:21",
         "2001-04-27 19:49",
         "2001-02-05 00:00",
         "1999-07-27 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniDs3Objects_ObjectIdentity = ObjectIdentity
juniDs3Objects = _JuniDs3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1)
)
_JuniDsx3ConfigTable_Object = MibTable
juniDsx3ConfigTable = _JuniDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniDsx3ConfigTable.setStatus("current")
_JuniDsx3ConfigEntry_Object = MibTableRow
juniDsx3ConfigEntry = _JuniDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1)
)
juniDsx3ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniDsx3ConfigEntry.setStatus("current")


class _JuniDsx3LineLength_Type(Integer32):
    """Custom type juniDsx3LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 137),
    )


_JuniDsx3LineLength_Type.__name__ = "Integer32"
_JuniDsx3LineLength_Object = MibTableColumn
juniDsx3LineLength = _JuniDsx3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 1),
    _JuniDsx3LineLength_Type()
)
juniDsx3LineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3LineLength.setStatus("current")
if mibBuilder.loadTexts:
    juniDsx3LineLength.setUnits("meters")


class _JuniDsx3LineType_Type(Integer32):
    """Custom type juniDsx3LineType based on Integer32"""
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
        *(("juniDsx3CbitParity", 4),
          ("juniDsx3CbitParityPlcp", 20),
          ("juniDsx3ClearChannel", 5),
          ("juniDsx3M23", 2),
          ("juniDsx3M23Plcp", 18),
          ("juniDsx3SYNTRAN", 3),
          ("juniDsx3other", 1),
          ("juniE3Framed", 7),
          ("juniE3G832", 6),
          ("juniE3Plcp", 8))
    )


_JuniDsx3LineType_Type.__name__ = "Integer32"
_JuniDsx3LineType_Object = MibTableColumn
juniDsx3LineType = _JuniDsx3LineType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 2),
    _JuniDsx3LineType_Type()
)
juniDsx3LineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3LineType.setStatus("current")


class _JuniDsx3CellScramblerConfig_Type(Integer32):
    """Custom type juniDsx3CellScramblerConfig based on Integer32"""
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


_JuniDsx3CellScramblerConfig_Type.__name__ = "Integer32"
_JuniDsx3CellScramblerConfig_Object = MibTableColumn
juniDsx3CellScramblerConfig = _JuniDsx3CellScramblerConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 3),
    _JuniDsx3CellScramblerConfig_Type()
)
juniDsx3CellScramblerConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3CellScramblerConfig.setStatus("current")
_JuniDsx3Channelization_Type = TruthValue
_JuniDsx3Channelization_Object = MibTableColumn
juniDsx3Channelization = _JuniDsx3Channelization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 4),
    _JuniDsx3Channelization_Type()
)
juniDsx3Channelization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3Channelization.setStatus("current")


class _JuniDsx3InterfaceType_Type(Integer32):
    """Custom type juniDsx3InterfaceType based on Integer32"""
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


_JuniDsx3InterfaceType_Type.__name__ = "Integer32"
_JuniDsx3InterfaceType_Object = MibTableColumn
juniDsx3InterfaceType = _JuniDsx3InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 5),
    _JuniDsx3InterfaceType_Type()
)
juniDsx3InterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3InterfaceType.setStatus("current")


class _JuniDsx3Application_Type(Integer32):
    """Custom type juniDsx3Application based on Integer32"""
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


_JuniDsx3Application_Type.__name__ = "Integer32"
_JuniDsx3Application_Object = MibTableColumn
juniDsx3Application = _JuniDsx3Application_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 6),
    _JuniDsx3Application_Type()
)
juniDsx3Application.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3Application.setStatus("current")


class _JuniDsx3Ds3Channel_Type(Integer32):
    """Custom type juniDsx3Ds3Channel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_JuniDsx3Ds3Channel_Type.__name__ = "Integer32"
_JuniDsx3Ds3Channel_Object = MibTableColumn
juniDsx3Ds3Channel = _JuniDsx3Ds3Channel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 7),
    _JuniDsx3Ds3Channel_Type()
)
juniDsx3Ds3Channel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3Ds3Channel.setStatus("current")
_JuniDsx3LowerIfIndex_Type = InterfaceIndexOrZero
_JuniDsx3LowerIfIndex_Object = MibTableColumn
juniDsx3LowerIfIndex = _JuniDsx3LowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 8),
    _JuniDsx3LowerIfIndex_Type()
)
juniDsx3LowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3LowerIfIndex.setStatus("current")
_JuniDsx3RowStatus_Type = RowStatus
_JuniDsx3RowStatus_Object = MibTableColumn
juniDsx3RowStatus = _JuniDsx3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 9),
    _JuniDsx3RowStatus_Type()
)
juniDsx3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3RowStatus.setStatus("current")


class _JuniDsx3Ds3DsuMode_Type(Integer32):
    """Custom type juniDsx3Ds3DsuMode based on Integer32"""
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


_JuniDsx3Ds3DsuMode_Type.__name__ = "Integer32"
_JuniDsx3Ds3DsuMode_Object = MibTableColumn
juniDsx3Ds3DsuMode = _JuniDsx3Ds3DsuMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 10),
    _JuniDsx3Ds3DsuMode_Type()
)
juniDsx3Ds3DsuMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3Ds3DsuMode.setStatus("current")


class _JuniDsx3Ds3BandwidthLimit_Type(Integer32):
    """Custom type juniDsx3Ds3BandwidthLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44210),
    )


_JuniDsx3Ds3BandwidthLimit_Type.__name__ = "Integer32"
_JuniDsx3Ds3BandwidthLimit_Object = MibTableColumn
juniDsx3Ds3BandwidthLimit = _JuniDsx3Ds3BandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 11),
    _JuniDsx3Ds3BandwidthLimit_Type()
)
juniDsx3Ds3BandwidthLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3Ds3BandwidthLimit.setStatus("current")


class _JuniDsx3Ds3DsuScrambleMode_Type(Integer32):
    """Custom type juniDsx3Ds3DsuScrambleMode based on Integer32"""
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


_JuniDsx3Ds3DsuScrambleMode_Type.__name__ = "Integer32"
_JuniDsx3Ds3DsuScrambleMode_Object = MibTableColumn
juniDsx3Ds3DsuScrambleMode = _JuniDsx3Ds3DsuScrambleMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 12),
    _JuniDsx3Ds3DsuScrambleMode_Type()
)
juniDsx3Ds3DsuScrambleMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3Ds3DsuScrambleMode.setStatus("current")


class _JuniDsx3MdlCarrier_Type(Integer32):
    """Custom type juniDsx3MdlCarrier based on Integer32"""
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


_JuniDsx3MdlCarrier_Type.__name__ = "Integer32"
_JuniDsx3MdlCarrier_Object = MibTableColumn
juniDsx3MdlCarrier = _JuniDsx3MdlCarrier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 13),
    _JuniDsx3MdlCarrier_Type()
)
juniDsx3MdlCarrier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlCarrier.setStatus("current")


class _JuniDsx3MdlTransmit_Type(Integer32):
    """Custom type juniDsx3MdlTransmit based on Integer32"""
    defaultValue = 8

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
        *(("idlesignal", 2),
          ("idlesignalTestsignal", 6),
          ("none", 8),
          ("path", 1),
          ("pathIdlesignal", 3),
          ("pathIdlesignalTestsignal", 7),
          ("pathTestsignal", 5),
          ("testsignal", 4))
    )


_JuniDsx3MdlTransmit_Type.__name__ = "Integer32"
_JuniDsx3MdlTransmit_Object = MibTableColumn
juniDsx3MdlTransmit = _JuniDsx3MdlTransmit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 14),
    _JuniDsx3MdlTransmit_Type()
)
juniDsx3MdlTransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlTransmit.setStatus("current")


class _JuniDsx3MdlEic_Type(DisplayString):
    """Custom type juniDsx3MdlEic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniDsx3MdlEic_Type.__name__ = "DisplayString"
_JuniDsx3MdlEic_Object = MibTableColumn
juniDsx3MdlEic = _JuniDsx3MdlEic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 15),
    _JuniDsx3MdlEic_Type()
)
juniDsx3MdlEic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlEic.setStatus("current")


class _JuniDsx3MdlLic_Type(DisplayString):
    """Custom type juniDsx3MdlLic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_JuniDsx3MdlLic_Type.__name__ = "DisplayString"
_JuniDsx3MdlLic_Object = MibTableColumn
juniDsx3MdlLic = _JuniDsx3MdlLic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 16),
    _JuniDsx3MdlLic_Type()
)
juniDsx3MdlLic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlLic.setStatus("current")


class _JuniDsx3MdlFic_Type(DisplayString):
    """Custom type juniDsx3MdlFic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniDsx3MdlFic_Type.__name__ = "DisplayString"
_JuniDsx3MdlFic_Object = MibTableColumn
juniDsx3MdlFic = _JuniDsx3MdlFic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 17),
    _JuniDsx3MdlFic_Type()
)
juniDsx3MdlFic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlFic.setStatus("current")


class _JuniDsx3MdlUnit_Type(DisplayString):
    """Custom type juniDsx3MdlUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_JuniDsx3MdlUnit_Type.__name__ = "DisplayString"
_JuniDsx3MdlUnit_Object = MibTableColumn
juniDsx3MdlUnit = _JuniDsx3MdlUnit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 18),
    _JuniDsx3MdlUnit_Type()
)
juniDsx3MdlUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlUnit.setStatus("current")


class _JuniDsx3MdlPfi_Type(DisplayString):
    """Custom type juniDsx3MdlPfi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx3MdlPfi_Type.__name__ = "DisplayString"
_JuniDsx3MdlPfi_Object = MibTableColumn
juniDsx3MdlPfi = _JuniDsx3MdlPfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 19),
    _JuniDsx3MdlPfi_Type()
)
juniDsx3MdlPfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlPfi.setStatus("current")


class _JuniDsx3MdlPort_Type(DisplayString):
    """Custom type juniDsx3MdlPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx3MdlPort_Type.__name__ = "DisplayString"
_JuniDsx3MdlPort_Object = MibTableColumn
juniDsx3MdlPort = _JuniDsx3MdlPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 20),
    _JuniDsx3MdlPort_Type()
)
juniDsx3MdlPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlPort.setStatus("current")


class _JuniDsx3MdlGenerator_Type(DisplayString):
    """Custom type juniDsx3MdlGenerator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx3MdlGenerator_Type.__name__ = "DisplayString"
_JuniDsx3MdlGenerator_Object = MibTableColumn
juniDsx3MdlGenerator = _JuniDsx3MdlGenerator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 21),
    _JuniDsx3MdlGenerator_Type()
)
juniDsx3MdlGenerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDsx3MdlGenerator.setStatus("current")
_JuniDs3NextIfIndex_Type = JuniNextIfIndex
_JuniDs3NextIfIndex_Object = MibScalar
juniDs3NextIfIndex = _JuniDs3NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 2),
    _JuniDs3NextIfIndex_Type()
)
juniDs3NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDs3NextIfIndex.setStatus("current")
_JuniDsx3FarEndCurrentTable_Object = MibTable
juniDsx3FarEndCurrentTable = _JuniDsx3FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndCurrentTable.setStatus("current")
_JuniDsx3FarEndCurrentEntry_Object = MibTableRow
juniDsx3FarEndCurrentEntry = _JuniDsx3FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndCurrentEntry.setStatus("current")
_JuniDsx3FarEndCurrentInvalidSeconds_Type = PerfCurrentCount
_JuniDsx3FarEndCurrentInvalidSeconds_Object = MibTableColumn
juniDsx3FarEndCurrentInvalidSeconds = _JuniDsx3FarEndCurrentInvalidSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3, 1, 1),
    _JuniDsx3FarEndCurrentInvalidSeconds_Type()
)
juniDsx3FarEndCurrentInvalidSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx3FarEndCurrentInvalidSeconds.setStatus("current")
_JuniDsx3FarEndIntervalTable_Object = MibTable
juniDsx3FarEndIntervalTable = _JuniDsx3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndIntervalTable.setStatus("current")
_JuniDsx3FarEndIntervalEntry_Object = MibTableRow
juniDsx3FarEndIntervalEntry = _JuniDsx3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndIntervalEntry.setStatus("current")
_JuniDsx3FarEndIntervalInvalidSeconds_Type = PerfIntervalCount
_JuniDsx3FarEndIntervalInvalidSeconds_Object = MibTableColumn
juniDsx3FarEndIntervalInvalidSeconds = _JuniDsx3FarEndIntervalInvalidSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4, 1, 1),
    _JuniDsx3FarEndIntervalInvalidSeconds_Type()
)
juniDsx3FarEndIntervalInvalidSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx3FarEndIntervalInvalidSeconds.setStatus("current")
_JuniDsx3FarEndTotalTable_Object = MibTable
juniDsx3FarEndTotalTable = _JuniDsx3FarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndTotalTable.setStatus("current")
_JuniDsx3FarEndTotalEntry_Object = MibTableRow
juniDsx3FarEndTotalEntry = _JuniDsx3FarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndTotalEntry.setStatus("current")
_JuniDsx3FarEndTotalInvalidSeconds_Type = PerfTotalCount
_JuniDsx3FarEndTotalInvalidSeconds_Object = MibTableColumn
juniDsx3FarEndTotalInvalidSeconds = _JuniDsx3FarEndTotalInvalidSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5, 1, 1),
    _JuniDsx3FarEndTotalInvalidSeconds_Type()
)
juniDsx3FarEndTotalInvalidSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDsx3FarEndTotalInvalidSeconds.setStatus("current")
_JuniDsx3FarEndConfigTable_Object = MibTable
juniDsx3FarEndConfigTable = _JuniDsx3FarEndConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndConfigTable.setStatus("current")
_JuniDsx3FarEndConfigEntry_Object = MibTableRow
juniDsx3FarEndConfigEntry = _JuniDsx3FarEndConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    juniDsx3FarEndConfigEntry.setStatus("current")


class _JuniDsx3FarEndPortNumber_Type(DisplayString):
    """Custom type juniDsx3FarEndPortNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx3FarEndPortNumber_Type.__name__ = "DisplayString"
_JuniDsx3FarEndPortNumber_Object = MibTableColumn
juniDsx3FarEndPortNumber = _JuniDsx3FarEndPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 6, 1, 1),
    _JuniDsx3FarEndPortNumber_Type()
)
juniDsx3FarEndPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDsx3FarEndPortNumber.setStatus("current")


class _JuniDsx3FarEndGeneratorNumber_Type(DisplayString):
    """Custom type juniDsx3FarEndGeneratorNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_JuniDsx3FarEndGeneratorNumber_Type.__name__ = "DisplayString"
_JuniDsx3FarEndGeneratorNumber_Object = MibTableColumn
juniDsx3FarEndGeneratorNumber = _JuniDsx3FarEndGeneratorNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 6, 1, 2),
    _JuniDsx3FarEndGeneratorNumber_Type()
)
juniDsx3FarEndGeneratorNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDsx3FarEndGeneratorNumber.setStatus("current")


class _JuniDsx3FarEndCarrier_Type(Integer32):
    """Custom type juniDsx3FarEndCarrier based on Integer32"""
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


_JuniDsx3FarEndCarrier_Type.__name__ = "Integer32"
_JuniDsx3FarEndCarrier_Object = MibTableColumn
juniDsx3FarEndCarrier = _JuniDsx3FarEndCarrier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 6, 1, 3),
    _JuniDsx3FarEndCarrier_Type()
)
juniDsx3FarEndCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDsx3FarEndCarrier.setStatus("current")
_JuniDs3Conformance_ObjectIdentity = ObjectIdentity
juniDs3Conformance = _JuniDs3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4)
)
_JuniDs3Compliances_ObjectIdentity = ObjectIdentity
juniDs3Compliances = _JuniDs3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1)
)
_JuniDs3Groups_ObjectIdentity = ObjectIdentity
juniDs3Groups = _JuniDs3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2)
)
dsx3FarEndCurrentEntry.registerAugmentions(
    ("Juniper-DS3-MIB",
     "juniDsx3FarEndCurrentEntry")
)
juniDsx3FarEndCurrentEntry.setIndexNames(*dsx3FarEndCurrentEntry.getIndexNames())
dsx3FarEndIntervalEntry.registerAugmentions(
    ("Juniper-DS3-MIB",
     "juniDsx3FarEndIntervalEntry")
)
juniDsx3FarEndIntervalEntry.setIndexNames(*dsx3FarEndIntervalEntry.getIndexNames())
dsx3FarEndTotalEntry.registerAugmentions(
    ("Juniper-DS3-MIB",
     "juniDsx3FarEndTotalEntry")
)
juniDsx3FarEndTotalEntry.setIndexNames(*dsx3FarEndTotalEntry.getIndexNames())
dsx3FarEndConfigEntry.registerAugmentions(
    ("Juniper-DS3-MIB",
     "juniDsx3FarEndConfigEntry")
)
juniDsx3FarEndConfigEntry.setIndexNames(*dsx3FarEndConfigEntry.getIndexNames())

# Managed Objects groups

juniDs3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 1)
)
juniDs3Group.setObjects(
    ("Juniper-DS3-MIB", "juniDsx3LineLength")
)
if mibBuilder.loadTexts:
    juniDs3Group.setStatus("obsolete")

juniDs3Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 2)
)
juniDs3Group2.setObjects(
      *(("Juniper-DS3-MIB", "juniDsx3LineLength"),
        ("Juniper-DS3-MIB", "juniDsx3LineType"),
        ("Juniper-DS3-MIB", "juniDsx3CellScramblerConfig"))
)
if mibBuilder.loadTexts:
    juniDs3Group2.setStatus("obsolete")

juniDs3Group3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 3)
)
juniDs3Group3.setObjects(
      *(("Juniper-DS3-MIB", "juniDsx3LineLength"),
        ("Juniper-DS3-MIB", "juniDsx3LineType"),
        ("Juniper-DS3-MIB", "juniDsx3CellScramblerConfig"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3DsuMode"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3BandwidthLimit"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3DsuScrambleMode"))
)
if mibBuilder.loadTexts:
    juniDs3Group3.setStatus("obsolete")

juniDs3Group4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 4)
)
juniDs3Group4.setObjects(
      *(("Juniper-DS3-MIB", "juniDsx3LineLength"),
        ("Juniper-DS3-MIB", "juniDsx3LineType"),
        ("Juniper-DS3-MIB", "juniDsx3CellScramblerConfig"),
        ("Juniper-DS3-MIB", "juniDsx3Channelization"),
        ("Juniper-DS3-MIB", "juniDsx3InterfaceType"),
        ("Juniper-DS3-MIB", "juniDsx3Application"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3Channel"),
        ("Juniper-DS3-MIB", "juniDsx3LowerIfIndex"),
        ("Juniper-DS3-MIB", "juniDsx3RowStatus"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3DsuMode"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3BandwidthLimit"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3DsuScrambleMode"),
        ("Juniper-DS3-MIB", "juniDs3NextIfIndex"))
)
if mibBuilder.loadTexts:
    juniDs3Group4.setStatus("obsolete")

juniDs3Group5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 5)
)
juniDs3Group5.setObjects(
      *(("Juniper-DS3-MIB", "juniDsx3LineLength"),
        ("Juniper-DS3-MIB", "juniDsx3LineType"),
        ("Juniper-DS3-MIB", "juniDsx3CellScramblerConfig"),
        ("Juniper-DS3-MIB", "juniDsx3Channelization"),
        ("Juniper-DS3-MIB", "juniDsx3InterfaceType"),
        ("Juniper-DS3-MIB", "juniDsx3Application"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3Channel"),
        ("Juniper-DS3-MIB", "juniDsx3LowerIfIndex"),
        ("Juniper-DS3-MIB", "juniDsx3RowStatus"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3DsuMode"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3BandwidthLimit"),
        ("Juniper-DS3-MIB", "juniDsx3Ds3DsuScrambleMode"),
        ("Juniper-DS3-MIB", "juniDsx3MdlCarrier"),
        ("Juniper-DS3-MIB", "juniDsx3MdlTransmit"),
        ("Juniper-DS3-MIB", "juniDsx3MdlEic"),
        ("Juniper-DS3-MIB", "juniDsx3MdlLic"),
        ("Juniper-DS3-MIB", "juniDsx3MdlFic"),
        ("Juniper-DS3-MIB", "juniDsx3MdlUnit"),
        ("Juniper-DS3-MIB", "juniDsx3MdlPfi"),
        ("Juniper-DS3-MIB", "juniDsx3MdlPort"),
        ("Juniper-DS3-MIB", "juniDsx3MdlGenerator"),
        ("Juniper-DS3-MIB", "juniDs3NextIfIndex"))
)
if mibBuilder.loadTexts:
    juniDs3Group5.setStatus("current")

juniDs3FarEndGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 6)
)
juniDs3FarEndGroup.setObjects(
      *(("Juniper-DS3-MIB", "juniDsx3FarEndCurrentInvalidSeconds"),
        ("Juniper-DS3-MIB", "juniDsx3FarEndIntervalInvalidSeconds"),
        ("Juniper-DS3-MIB", "juniDsx3FarEndTotalInvalidSeconds"))
)
if mibBuilder.loadTexts:
    juniDs3FarEndGroup.setStatus("obsolete")

juniDs3FarEndGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 7)
)
juniDs3FarEndGroup2.setObjects(
      *(("Juniper-DS3-MIB", "juniDsx3FarEndCurrentInvalidSeconds"),
        ("Juniper-DS3-MIB", "juniDsx3FarEndIntervalInvalidSeconds"),
        ("Juniper-DS3-MIB", "juniDsx3FarEndTotalInvalidSeconds"),
        ("Juniper-DS3-MIB", "juniDsx3FarEndPortNumber"),
        ("Juniper-DS3-MIB", "juniDsx3FarEndGeneratorNumber"),
        ("Juniper-DS3-MIB", "juniDsx3FarEndCarrier"))
)
if mibBuilder.loadTexts:
    juniDs3FarEndGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniDs3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniDs3Compliance.setStatus(
        "obsolete"
    )

juniDs3Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniDs3Compliance2.setStatus(
        "obsolete"
    )

juniDs3Compliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniDs3Compliance3.setStatus(
        "obsolete"
    )

juniDs3Compliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniDs3Compliance4.setStatus(
        "obsolete"
    )

juniDs3Compliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniDs3Compliance5.setStatus(
        "obsolete"
    )

juniDs3Compliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniDs3Compliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DS3-MIB",
    **{"juniDs3MIB": juniDs3MIB,
       "juniDs3Objects": juniDs3Objects,
       "juniDsx3ConfigTable": juniDsx3ConfigTable,
       "juniDsx3ConfigEntry": juniDsx3ConfigEntry,
       "juniDsx3LineLength": juniDsx3LineLength,
       "juniDsx3LineType": juniDsx3LineType,
       "juniDsx3CellScramblerConfig": juniDsx3CellScramblerConfig,
       "juniDsx3Channelization": juniDsx3Channelization,
       "juniDsx3InterfaceType": juniDsx3InterfaceType,
       "juniDsx3Application": juniDsx3Application,
       "juniDsx3Ds3Channel": juniDsx3Ds3Channel,
       "juniDsx3LowerIfIndex": juniDsx3LowerIfIndex,
       "juniDsx3RowStatus": juniDsx3RowStatus,
       "juniDsx3Ds3DsuMode": juniDsx3Ds3DsuMode,
       "juniDsx3Ds3BandwidthLimit": juniDsx3Ds3BandwidthLimit,
       "juniDsx3Ds3DsuScrambleMode": juniDsx3Ds3DsuScrambleMode,
       "juniDsx3MdlCarrier": juniDsx3MdlCarrier,
       "juniDsx3MdlTransmit": juniDsx3MdlTransmit,
       "juniDsx3MdlEic": juniDsx3MdlEic,
       "juniDsx3MdlLic": juniDsx3MdlLic,
       "juniDsx3MdlFic": juniDsx3MdlFic,
       "juniDsx3MdlUnit": juniDsx3MdlUnit,
       "juniDsx3MdlPfi": juniDsx3MdlPfi,
       "juniDsx3MdlPort": juniDsx3MdlPort,
       "juniDsx3MdlGenerator": juniDsx3MdlGenerator,
       "juniDs3NextIfIndex": juniDs3NextIfIndex,
       "juniDsx3FarEndCurrentTable": juniDsx3FarEndCurrentTable,
       "juniDsx3FarEndCurrentEntry": juniDsx3FarEndCurrentEntry,
       "juniDsx3FarEndCurrentInvalidSeconds": juniDsx3FarEndCurrentInvalidSeconds,
       "juniDsx3FarEndIntervalTable": juniDsx3FarEndIntervalTable,
       "juniDsx3FarEndIntervalEntry": juniDsx3FarEndIntervalEntry,
       "juniDsx3FarEndIntervalInvalidSeconds": juniDsx3FarEndIntervalInvalidSeconds,
       "juniDsx3FarEndTotalTable": juniDsx3FarEndTotalTable,
       "juniDsx3FarEndTotalEntry": juniDsx3FarEndTotalEntry,
       "juniDsx3FarEndTotalInvalidSeconds": juniDsx3FarEndTotalInvalidSeconds,
       "juniDsx3FarEndConfigTable": juniDsx3FarEndConfigTable,
       "juniDsx3FarEndConfigEntry": juniDsx3FarEndConfigEntry,
       "juniDsx3FarEndPortNumber": juniDsx3FarEndPortNumber,
       "juniDsx3FarEndGeneratorNumber": juniDsx3FarEndGeneratorNumber,
       "juniDsx3FarEndCarrier": juniDsx3FarEndCarrier,
       "juniDs3Conformance": juniDs3Conformance,
       "juniDs3Compliances": juniDs3Compliances,
       "juniDs3Compliance": juniDs3Compliance,
       "juniDs3Compliance2": juniDs3Compliance2,
       "juniDs3Compliance3": juniDs3Compliance3,
       "juniDs3Compliance4": juniDs3Compliance4,
       "juniDs3Compliance5": juniDs3Compliance5,
       "juniDs3Compliance6": juniDs3Compliance6,
       "juniDs3Groups": juniDs3Groups,
       "juniDs3Group": juniDs3Group,
       "juniDs3Group2": juniDs3Group2,
       "juniDs3Group3": juniDs3Group3,
       "juniDs3Group4": juniDs3Group4,
       "juniDs3Group5": juniDs3Group5,
       "juniDs3FarEndGroup": juniDs3FarEndGroup,
       "juniDs3FarEndGroup2": juniDs3FarEndGroup2}
)
