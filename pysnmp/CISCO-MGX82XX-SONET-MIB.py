# SNMP MIB module (CISCO-MGX82XX-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:37 2024
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

(cwsonetObjects,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cwsonetObjects")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetConfig_ObjectIdentity = ObjectIdentity
sonetConfig = _SonetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1)
)
_SonetConfigTable_Object = MibTable
sonetConfigTable = _SonetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonetConfigTable.setStatus("mandatory")
_SonetConfigEntry_Object = MibTableRow
sonetConfigEntry = _SonetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1)
)
sonetConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetLineNum"),
)
if mibBuilder.loadTexts:
    sonetConfigEntry.setStatus("mandatory")


class _SonetLineNum_Type(Integer32):
    """Custom type sonetLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SonetLineNum_Type.__name__ = "Integer32"
_SonetLineNum_Object = MibTableColumn
sonetLineNum = _SonetLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 1),
    _SonetLineNum_Type()
)
sonetLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineNum.setStatus("mandatory")


class _SonetLineType_Type(Integer32):
    """Custom type sonetLineType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("sonetStm1", 2),
          ("sonetStm16", 6),
          ("sonetStm4", 4),
          ("sonetStm64", 8),
          ("sonetSts12c", 3),
          ("sonetSts192c", 7),
          ("sonetSts3", 9),
          ("sonetSts3c", 1),
          ("sonetSts48c", 5))
    )


_SonetLineType_Type.__name__ = "Integer32"
_SonetLineType_Object = MibTableColumn
sonetLineType = _SonetLineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 2),
    _SonetLineType_Type()
)
sonetLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineType.setStatus("mandatory")


class _SonetLineLoopbackCommand_Type(Integer32):
    """Custom type sonetLineLoopbackCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonetLocalLineLoop", 3),
          ("sonetNoLoop", 1),
          ("sonetRemoteLineLoop", 2))
    )


_SonetLineLoopbackCommand_Type.__name__ = "Integer32"
_SonetLineLoopbackCommand_Object = MibTableColumn
sonetLineLoopbackCommand = _SonetLineLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 3),
    _SonetLineLoopbackCommand_Type()
)
sonetLineLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineLoopbackCommand.setStatus("mandatory")


class _SonetHCSmasking_Type(Integer32):
    """Custom type sonetHCSmasking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SonetHCSmasking_Type.__name__ = "Integer32"
_SonetHCSmasking_Object = MibTableColumn
sonetHCSmasking = _SonetHCSmasking_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 4),
    _SonetHCSmasking_Type()
)
sonetHCSmasking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetHCSmasking.setStatus("mandatory")


class _SonetPayloadScrambling_Type(Integer32):
    """Custom type sonetPayloadScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SonetPayloadScrambling_Type.__name__ = "Integer32"
_SonetPayloadScrambling_Object = MibTableColumn
sonetPayloadScrambling = _SonetPayloadScrambling_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 5),
    _SonetPayloadScrambling_Type()
)
sonetPayloadScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPayloadScrambling.setStatus("mandatory")


class _SonetFrameScrambling_Type(Integer32):
    """Custom type sonetFrameScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SonetFrameScrambling_Type.__name__ = "Integer32"
_SonetFrameScrambling_Object = MibTableColumn
sonetFrameScrambling = _SonetFrameScrambling_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 6),
    _SonetFrameScrambling_Type()
)
sonetFrameScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFrameScrambling.setStatus("mandatory")


class _SonetLineEnable_Type(Integer32):
    """Custom type sonetLineEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SonetLineEnable_Type.__name__ = "Integer32"
_SonetLineEnable_Object = MibTableColumn
sonetLineEnable = _SonetLineEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 7),
    _SonetLineEnable_Type()
)
sonetLineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineEnable.setStatus("mandatory")


class _SonetLineXmtClkSrc_Type(Integer32):
    """Custom type sonetLineXmtClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backplaneClk", 1),
          ("localClk", 3),
          ("recoverClk", 2))
    )


_SonetLineXmtClkSrc_Type.__name__ = "Integer32"
_SonetLineXmtClkSrc_Object = MibTableColumn
sonetLineXmtClkSrc = _SonetLineXmtClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 8),
    _SonetLineXmtClkSrc_Type()
)
sonetLineXmtClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineXmtClkSrc.setStatus("mandatory")


class _SonetRDIVType_Type(Integer32):
    """Custom type sonetRDIVType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onebit", 1),
          ("threebit", 3))
    )


_SonetRDIVType_Type.__name__ = "Integer32"
_SonetRDIVType_Object = MibTableColumn
sonetRDIVType = _SonetRDIVType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 9),
    _SonetRDIVType_Type()
)
sonetRDIVType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetRDIVType.setStatus("mandatory")


class _SonetRDIPType_Type(Integer32):
    """Custom type sonetRDIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onebit", 1),
          ("threebit", 3))
    )


_SonetRDIPType_Type.__name__ = "Integer32"
_SonetRDIPType_Object = MibTableColumn
sonetRDIPType = _SonetRDIPType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 10),
    _SonetRDIPType_Type()
)
sonetRDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetRDIPType.setStatus("mandatory")


class _SonetTributaryType_Type(Integer32):
    """Custom type sonetTributaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vt15vc11", 1),
          ("vt2vc12", 2))
    )


_SonetTributaryType_Type.__name__ = "Integer32"
_SonetTributaryType_Object = MibTableColumn
sonetTributaryType = _SonetTributaryType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 11),
    _SonetTributaryType_Type()
)
sonetTributaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetTributaryType.setStatus("mandatory")


class _SonetTributaryMappingType_Type(Integer32):
    """Custom type sonetTributaryMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("byteSynchronous", 2))
    )


_SonetTributaryMappingType_Type.__name__ = "Integer32"
_SonetTributaryMappingType_Object = MibTableColumn
sonetTributaryMappingType = _SonetTributaryMappingType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 12),
    _SonetTributaryMappingType_Type()
)
sonetTributaryMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetTributaryMappingType.setStatus("mandatory")


class _SonetTributaryFramingFormat_Type(Integer32):
    """Custom type sonetTributaryFramingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("esf", 3),
          ("notApplicable", 1),
          ("sf", 2))
    )


_SonetTributaryFramingFormat_Type.__name__ = "Integer32"
_SonetTributaryFramingFormat_Object = MibTableColumn
sonetTributaryFramingFormat = _SonetTributaryFramingFormat_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 13),
    _SonetTributaryFramingFormat_Type()
)
sonetTributaryFramingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetTributaryFramingFormat.setStatus("mandatory")


class _SonetSignallingTransportMode_Type(Integer32):
    """Custom type sonetSignallingTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearMode", 3),
          ("notApplicable", 1),
          ("signallingTransferMode", 2))
    )


_SonetSignallingTransportMode_Type.__name__ = "Integer32"
_SonetSignallingTransportMode_Object = MibTableColumn
sonetSignallingTransportMode = _SonetSignallingTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 14),
    _SonetSignallingTransportMode_Type()
)
sonetSignallingTransportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSignallingTransportMode.setStatus("mandatory")


class _SonetTributaryGroupingType_Type(Integer32):
    """Custom type sonetTributaryGroupingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("au3Grouping", 2),
          ("au4Grouping", 3),
          ("notApplicable", 1))
    )


_SonetTributaryGroupingType_Type.__name__ = "Integer32"
_SonetTributaryGroupingType_Object = MibTableColumn
sonetTributaryGroupingType = _SonetTributaryGroupingType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 1, 1, 15),
    _SonetTributaryGroupingType_Type()
)
sonetTributaryGroupingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetTributaryGroupingType.setStatus("mandatory")
_SonetConfigNumOfValidEntries_Type = Integer32
_SonetConfigNumOfValidEntries_Object = MibScalar
sonetConfigNumOfValidEntries = _SonetConfigNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 1, 2),
    _SonetConfigNumOfValidEntries_Type()
)
sonetConfigNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetConfigNumOfValidEntries.setStatus("mandatory")
_CwsonetMedium_ObjectIdentity = ObjectIdentity
cwsonetMedium = _CwsonetMedium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2)
)
_CwSonetMediumTable_Object = MibTable
cwSonetMediumTable = _CwSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwSonetMediumTable.setStatus("mandatory")
_CwSonetMediumEntry_Object = MibTableRow
cwSonetMediumEntry = _CwSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1, 1)
)
cwSonetMediumEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetLineNum"),
)
if mibBuilder.loadTexts:
    cwSonetMediumEntry.setStatus("mandatory")


class _CwSonetMediumType_Type(Integer32):
    """Custom type cwSonetMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_CwSonetMediumType_Type.__name__ = "Integer32"
_CwSonetMediumType_Object = MibTableColumn
cwSonetMediumType = _CwSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1, 1, 1),
    _CwSonetMediumType_Type()
)
cwSonetMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetMediumType.setStatus("mandatory")


class _CwSonetMediumTimeElapsed_Type(Integer32):
    """Custom type cwSonetMediumTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CwSonetMediumTimeElapsed_Type.__name__ = "Integer32"
_CwSonetMediumTimeElapsed_Object = MibTableColumn
cwSonetMediumTimeElapsed = _CwSonetMediumTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1, 1, 2),
    _CwSonetMediumTimeElapsed_Type()
)
cwSonetMediumTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetMediumTimeElapsed.setStatus("mandatory")


class _CwSonetMediumValidIntervals_Type(Integer32):
    """Custom type cwSonetMediumValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CwSonetMediumValidIntervals_Type.__name__ = "Integer32"
_CwSonetMediumValidIntervals_Object = MibTableColumn
cwSonetMediumValidIntervals = _CwSonetMediumValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1, 1, 3),
    _CwSonetMediumValidIntervals_Type()
)
cwSonetMediumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetMediumValidIntervals.setStatus("mandatory")


class _CwSonetMediumLineCoding_Type(Integer32):
    """Custom type cwSonetMediumLineCoding based on Integer32"""
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
        *(("sonetMediumB3ZS", 2),
          ("sonetMediumCMI", 3),
          ("sonetMediumNRZ", 4),
          ("sonetMediumOther", 1),
          ("sonetMediumRZ", 5))
    )


_CwSonetMediumLineCoding_Type.__name__ = "Integer32"
_CwSonetMediumLineCoding_Object = MibTableColumn
cwSonetMediumLineCoding = _CwSonetMediumLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1, 1, 4),
    _CwSonetMediumLineCoding_Type()
)
cwSonetMediumLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetMediumLineCoding.setStatus("mandatory")


class _CwSonetMediumLineType_Type(Integer32):
    """Custom type cwSonetMediumLineType based on Integer32"""
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
        *(("sonetCoax", 5),
          ("sonetLongSingleMode", 3),
          ("sonetMultiMode", 4),
          ("sonetOther", 1),
          ("sonetShortSingleMode", 2),
          ("sonetUTP", 6))
    )


_CwSonetMediumLineType_Type.__name__ = "Integer32"
_CwSonetMediumLineType_Object = MibTableColumn
cwSonetMediumLineType = _CwSonetMediumLineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1, 1, 5),
    _CwSonetMediumLineType_Type()
)
cwSonetMediumLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetMediumLineType.setStatus("mandatory")


class _CwSonetMediumCircuitIdentifier_Type(DisplayString):
    """Custom type cwSonetMediumCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CwSonetMediumCircuitIdentifier_Type.__name__ = "DisplayString"
_CwSonetMediumCircuitIdentifier_Object = MibTableColumn
cwSonetMediumCircuitIdentifier = _CwSonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 2, 1, 1, 6),
    _CwSonetMediumCircuitIdentifier_Type()
)
cwSonetMediumCircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetMediumCircuitIdentifier.setStatus("mandatory")
_CwsonetSection_ObjectIdentity = ObjectIdentity
cwsonetSection = _CwsonetSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3)
)
_CwSonetSectionCurrentTable_Object = MibTable
cwSonetSectionCurrentTable = _CwSonetSectionCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwSonetSectionCurrentTable.setStatus("mandatory")
_CwSonetSectionCurrentEntry_Object = MibTableRow
cwSonetSectionCurrentEntry = _CwSonetSectionCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1)
)
cwSonetSectionCurrentEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetSectionCurrentLineNum"),
)
if mibBuilder.loadTexts:
    cwSonetSectionCurrentEntry.setStatus("mandatory")


class _CwSonetSectionCurrentLineNum_Type(Integer32):
    """Custom type cwSonetSectionCurrentLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetSectionCurrentLineNum_Type.__name__ = "Integer32"
_CwSonetSectionCurrentLineNum_Object = MibTableColumn
cwSonetSectionCurrentLineNum = _CwSonetSectionCurrentLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 1),
    _CwSonetSectionCurrentLineNum_Type()
)
cwSonetSectionCurrentLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentLineNum.setStatus("mandatory")


class _CwSonetSectionCurrentStatus_Type(Integer32):
    """Custom type cwSonetSectionCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CwSonetSectionCurrentStatus_Type.__name__ = "Integer32"
_CwSonetSectionCurrentStatus_Object = MibTableColumn
cwSonetSectionCurrentStatus = _CwSonetSectionCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 2),
    _CwSonetSectionCurrentStatus_Type()
)
cwSonetSectionCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentStatus.setStatus("mandatory")


class _CwSonetSectionCurrentValidFlag_Type(Integer32):
    """Custom type cwSonetSectionCurrentValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetSectionCurrentValidFlag_Type.__name__ = "Integer32"
_CwSonetSectionCurrentValidFlag_Object = MibTableColumn
cwSonetSectionCurrentValidFlag = _CwSonetSectionCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 3),
    _CwSonetSectionCurrentValidFlag_Type()
)
cwSonetSectionCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentValidFlag.setStatus("mandatory")


class _CwSonetSectionCurrent15minTimeElapsed_Type(Integer32):
    """Custom type cwSonetSectionCurrent15minTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CwSonetSectionCurrent15minTimeElapsed_Type.__name__ = "Integer32"
_CwSonetSectionCurrent15minTimeElapsed_Object = MibTableColumn
cwSonetSectionCurrent15minTimeElapsed = _CwSonetSectionCurrent15minTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 4),
    _CwSonetSectionCurrent15minTimeElapsed_Type()
)
cwSonetSectionCurrent15minTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrent15minTimeElapsed.setStatus("mandatory")
_CwSonetSectionCurrentESs_Type = Counter32
_CwSonetSectionCurrentESs_Object = MibTableColumn
cwSonetSectionCurrentESs = _CwSonetSectionCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 5),
    _CwSonetSectionCurrentESs_Type()
)
cwSonetSectionCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentESs.setStatus("mandatory")
_CwSonetSectionCurrentSESs_Type = Counter32
_CwSonetSectionCurrentSESs_Object = MibTableColumn
cwSonetSectionCurrentSESs = _CwSonetSectionCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 6),
    _CwSonetSectionCurrentSESs_Type()
)
cwSonetSectionCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentSESs.setStatus("mandatory")
_CwSonetSectionCurrentSEFSs_Type = Counter32
_CwSonetSectionCurrentSEFSs_Object = MibTableColumn
cwSonetSectionCurrentSEFSs = _CwSonetSectionCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 7),
    _CwSonetSectionCurrentSEFSs_Type()
)
cwSonetSectionCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentSEFSs.setStatus("mandatory")
_CwSonetSectionCurrentCVs_Type = Counter32
_CwSonetSectionCurrentCVs_Object = MibTableColumn
cwSonetSectionCurrentCVs = _CwSonetSectionCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 8),
    _CwSonetSectionCurrentCVs_Type()
)
cwSonetSectionCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentCVs.setStatus("mandatory")


class _CwSonetSectionCurrentClrButton_Type(Integer32):
    """Custom type cwSonetSectionCurrentClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_CwSonetSectionCurrentClrButton_Type.__name__ = "Integer32"
_CwSonetSectionCurrentClrButton_Object = MibTableColumn
cwSonetSectionCurrentClrButton = _CwSonetSectionCurrentClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 1, 1, 9),
    _CwSonetSectionCurrentClrButton_Type()
)
cwSonetSectionCurrentClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwSonetSectionCurrentClrButton.setStatus("mandatory")
_SonetSectionCurrentDayTable_Object = MibTable
sonetSectionCurrentDayTable = _SonetSectionCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonetSectionCurrentDayTable.setStatus("mandatory")
_SonetSectionCurrentDayEntry_Object = MibTableRow
sonetSectionCurrentDayEntry = _SonetSectionCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1)
)
sonetSectionCurrentDayEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetSectionCurrentDayLineNum"),
)
if mibBuilder.loadTexts:
    sonetSectionCurrentDayEntry.setStatus("mandatory")


class _SonetSectionCurrentDayLineNum_Type(Integer32):
    """Custom type sonetSectionCurrentDayLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetSectionCurrentDayLineNum_Type.__name__ = "Integer32"
_SonetSectionCurrentDayLineNum_Object = MibTableColumn
sonetSectionCurrentDayLineNum = _SonetSectionCurrentDayLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1, 1),
    _SonetSectionCurrentDayLineNum_Type()
)
sonetSectionCurrentDayLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentDayLineNum.setStatus("mandatory")


class _SonetSectionCurrentDayValidFlag_Type(Integer32):
    """Custom type sonetSectionCurrentDayValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_SonetSectionCurrentDayValidFlag_Type.__name__ = "Integer32"
_SonetSectionCurrentDayValidFlag_Object = MibTableColumn
sonetSectionCurrentDayValidFlag = _SonetSectionCurrentDayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1, 2),
    _SonetSectionCurrentDayValidFlag_Type()
)
sonetSectionCurrentDayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentDayValidFlag.setStatus("mandatory")
_SonetSectionCurrentDayESs_Type = Counter32
_SonetSectionCurrentDayESs_Object = MibTableColumn
sonetSectionCurrentDayESs = _SonetSectionCurrentDayESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1, 3),
    _SonetSectionCurrentDayESs_Type()
)
sonetSectionCurrentDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentDayESs.setStatus("mandatory")
_SonetSectionCurrentDaySESs_Type = Counter32
_SonetSectionCurrentDaySESs_Object = MibTableColumn
sonetSectionCurrentDaySESs = _SonetSectionCurrentDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1, 4),
    _SonetSectionCurrentDaySESs_Type()
)
sonetSectionCurrentDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentDaySESs.setStatus("mandatory")
_SonetSectionCurrentDaySEFSs_Type = Counter32
_SonetSectionCurrentDaySEFSs_Object = MibTableColumn
sonetSectionCurrentDaySEFSs = _SonetSectionCurrentDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1, 5),
    _SonetSectionCurrentDaySEFSs_Type()
)
sonetSectionCurrentDaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentDaySEFSs.setStatus("mandatory")
_SonetSectionCurrentDayCVs_Type = Counter32
_SonetSectionCurrentDayCVs_Object = MibTableColumn
sonetSectionCurrentDayCVs = _SonetSectionCurrentDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1, 6),
    _SonetSectionCurrentDayCVs_Type()
)
sonetSectionCurrentDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCurrentDayCVs.setStatus("mandatory")


class _SonetSectionCurrentDayClrButton_Type(Integer32):
    """Custom type sonetSectionCurrentDayClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetSectionCurrentDayClrButton_Type.__name__ = "Integer32"
_SonetSectionCurrentDayClrButton_Object = MibTableColumn
sonetSectionCurrentDayClrButton = _SonetSectionCurrentDayClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 2, 1, 7),
    _SonetSectionCurrentDayClrButton_Type()
)
sonetSectionCurrentDayClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentDayClrButton.setStatus("mandatory")
_CwSonetSectionIntervalTable_Object = MibTable
cwSonetSectionIntervalTable = _CwSonetSectionIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cwSonetSectionIntervalTable.setStatus("mandatory")
_CwSonetSectionIntervalEntry_Object = MibTableRow
cwSonetSectionIntervalEntry = _CwSonetSectionIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1)
)
cwSonetSectionIntervalEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetSectionIntervalLineNum"),
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetSectionIntervalNumber"),
)
if mibBuilder.loadTexts:
    cwSonetSectionIntervalEntry.setStatus("mandatory")


class _CwSonetSectionIntervalLineNum_Type(Integer32):
    """Custom type cwSonetSectionIntervalLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetSectionIntervalLineNum_Type.__name__ = "Integer32"
_CwSonetSectionIntervalLineNum_Object = MibTableColumn
cwSonetSectionIntervalLineNum = _CwSonetSectionIntervalLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1, 1),
    _CwSonetSectionIntervalLineNum_Type()
)
cwSonetSectionIntervalLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionIntervalLineNum.setStatus("mandatory")


class _CwSonetSectionIntervalNumber_Type(Integer32):
    """Custom type cwSonetSectionIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CwSonetSectionIntervalNumber_Type.__name__ = "Integer32"
_CwSonetSectionIntervalNumber_Object = MibTableColumn
cwSonetSectionIntervalNumber = _CwSonetSectionIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1, 2),
    _CwSonetSectionIntervalNumber_Type()
)
cwSonetSectionIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionIntervalNumber.setStatus("mandatory")


class _CwSonetSectionIntervalValidFlag_Type(Integer32):
    """Custom type cwSonetSectionIntervalValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetSectionIntervalValidFlag_Type.__name__ = "Integer32"
_CwSonetSectionIntervalValidFlag_Object = MibTableColumn
cwSonetSectionIntervalValidFlag = _CwSonetSectionIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1, 3),
    _CwSonetSectionIntervalValidFlag_Type()
)
cwSonetSectionIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionIntervalValidFlag.setStatus("mandatory")
_CwSonetSectionIntervalESs_Type = Counter32
_CwSonetSectionIntervalESs_Object = MibTableColumn
cwSonetSectionIntervalESs = _CwSonetSectionIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1, 4),
    _CwSonetSectionIntervalESs_Type()
)
cwSonetSectionIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionIntervalESs.setStatus("mandatory")
_CwSonetSectionIntervalSESs_Type = Counter32
_CwSonetSectionIntervalSESs_Object = MibTableColumn
cwSonetSectionIntervalSESs = _CwSonetSectionIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1, 5),
    _CwSonetSectionIntervalSESs_Type()
)
cwSonetSectionIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionIntervalSESs.setStatus("mandatory")
_CwSonetSectionIntervalSEFss_Type = Counter32
_CwSonetSectionIntervalSEFss_Object = MibTableColumn
cwSonetSectionIntervalSEFss = _CwSonetSectionIntervalSEFss_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1, 6),
    _CwSonetSectionIntervalSEFss_Type()
)
cwSonetSectionIntervalSEFss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionIntervalSEFss.setStatus("mandatory")
_CwSonetSectionIntervalCVs_Type = Counter32
_CwSonetSectionIntervalCVs_Object = MibTableColumn
cwSonetSectionIntervalCVs = _CwSonetSectionIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 3, 1, 7),
    _CwSonetSectionIntervalCVs_Type()
)
cwSonetSectionIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetSectionIntervalCVs.setStatus("mandatory")
_SonetSectionAlarmTable_Object = MibTable
sonetSectionAlarmTable = _SonetSectionAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4)
)
if mibBuilder.loadTexts:
    sonetSectionAlarmTable.setStatus("mandatory")
_SonetSectionAlarmEntry_Object = MibTableRow
sonetSectionAlarmEntry = _SonetSectionAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1)
)
sonetSectionAlarmEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sectionAlarmLineNum"),
)
if mibBuilder.loadTexts:
    sonetSectionAlarmEntry.setStatus("mandatory")


class _SectionAlarmLineNum_Type(Integer32):
    """Custom type sectionAlarmLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SectionAlarmLineNum_Type.__name__ = "Integer32"
_SectionAlarmLineNum_Object = MibTableColumn
sectionAlarmLineNum = _SectionAlarmLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 1),
    _SectionAlarmLineNum_Type()
)
sectionAlarmLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectionAlarmLineNum.setStatus("mandatory")


class _SonetSectionStatisticalAlarmSeverity_Type(Integer32):
    """Custom type sonetSectionStatisticalAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_SonetSectionStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_SonetSectionStatisticalAlarmSeverity_Object = MibTableColumn
sonetSectionStatisticalAlarmSeverity = _SonetSectionStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 2),
    _SonetSectionStatisticalAlarmSeverity_Type()
)
sonetSectionStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionStatisticalAlarmSeverity.setStatus("mandatory")


class _SonetSectionCurrent15minESsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrent15minESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrent15minESsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrent15minESsThreshold_Object = MibTableColumn
sonetSectionCurrent15minESsThreshold = _SonetSectionCurrent15minESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 3),
    _SonetSectionCurrent15minESsThreshold_Type()
)
sonetSectionCurrent15minESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minESsThreshold.setStatus("mandatory")


class _SonetSectionCurrentDayESsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentDayESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrentDayESsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentDayESsThreshold_Object = MibTableColumn
sonetSectionCurrentDayESsThreshold = _SonetSectionCurrentDayESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 4),
    _SonetSectionCurrentDayESsThreshold_Type()
)
sonetSectionCurrentDayESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentDayESsThreshold.setStatus("mandatory")


class _SonetSectionCurrent15minSESsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrent15minSESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrent15minSESsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrent15minSESsThreshold_Object = MibTableColumn
sonetSectionCurrent15minSESsThreshold = _SonetSectionCurrent15minSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 5),
    _SonetSectionCurrent15minSESsThreshold_Type()
)
sonetSectionCurrent15minSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minSESsThreshold.setStatus("mandatory")


class _SonetSectionCurrentDaySESsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentDaySESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrentDaySESsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentDaySESsThreshold_Object = MibTableColumn
sonetSectionCurrentDaySESsThreshold = _SonetSectionCurrentDaySESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 6),
    _SonetSectionCurrentDaySESsThreshold_Type()
)
sonetSectionCurrentDaySESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentDaySESsThreshold.setStatus("mandatory")


class _SonetSectionCurrent15minSEFSsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrent15minSEFSsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrent15minSEFSsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrent15minSEFSsThreshold_Object = MibTableColumn
sonetSectionCurrent15minSEFSsThreshold = _SonetSectionCurrent15minSEFSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 7),
    _SonetSectionCurrent15minSEFSsThreshold_Type()
)
sonetSectionCurrent15minSEFSsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minSEFSsThreshold.setStatus("mandatory")


class _SonetSectionCurrentDaySEFSsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentDaySEFSsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrentDaySEFSsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentDaySEFSsThreshold_Object = MibTableColumn
sonetSectionCurrentDaySEFSsThreshold = _SonetSectionCurrentDaySEFSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 8),
    _SonetSectionCurrentDaySEFSsThreshold_Type()
)
sonetSectionCurrentDaySEFSsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentDaySEFSsThreshold.setStatus("mandatory")


class _SonetSectionCurrent15minCVsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrent15minCVsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrent15minCVsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrent15minCVsThreshold_Object = MibTableColumn
sonetSectionCurrent15minCVsThreshold = _SonetSectionCurrent15minCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 9),
    _SonetSectionCurrent15minCVsThreshold_Type()
)
sonetSectionCurrent15minCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrent15minCVsThreshold.setStatus("mandatory")


class _SonetSectionCurrentDayCVsThreshold_Type(Integer32):
    """Custom type sonetSectionCurrentDayCVsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetSectionCurrentDayCVsThreshold_Type.__name__ = "Integer32"
_SonetSectionCurrentDayCVsThreshold_Object = MibTableColumn
sonetSectionCurrentDayCVsThreshold = _SonetSectionCurrentDayCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 10),
    _SonetSectionCurrentDayCVsThreshold_Type()
)
sonetSectionCurrentDayCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCurrentDayCVsThreshold.setStatus("mandatory")


class _SonetSectionTraceSelection_Type(Integer32):
    """Custom type sonetSectionTraceSelection based on Integer32"""
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
          ("sixteenBytes", 4),
          ("sixteenBytesCrc7", 5),
          ("sixteenBytesMsb1", 6),
          ("sixtyFourBytes", 2),
          ("sixtyFourBytesCrlf", 3))
    )


_SonetSectionTraceSelection_Type.__name__ = "Integer32"
_SonetSectionTraceSelection_Object = MibTableColumn
sonetSectionTraceSelection = _SonetSectionTraceSelection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 11),
    _SonetSectionTraceSelection_Type()
)
sonetSectionTraceSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionTraceSelection.setStatus("mandatory")


class _SonetSectionTraceToTransmit_Type(OctetString):
    """Custom type sonetSectionTraceToTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SonetSectionTraceToTransmit_Type.__name__ = "OctetString"
_SonetSectionTraceToTransmit_Object = MibTableColumn
sonetSectionTraceToTransmit = _SonetSectionTraceToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 12),
    _SonetSectionTraceToTransmit_Type()
)
sonetSectionTraceToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionTraceToTransmit.setStatus("mandatory")


class _SonetSectionTraceToExpect_Type(OctetString):
    """Custom type sonetSectionTraceToExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SonetSectionTraceToExpect_Type.__name__ = "OctetString"
_SonetSectionTraceToExpect_Object = MibTableColumn
sonetSectionTraceToExpect = _SonetSectionTraceToExpect_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 13),
    _SonetSectionTraceToExpect_Type()
)
sonetSectionTraceToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionTraceToExpect.setStatus("mandatory")


class _SonetSectionTraceReceived_Type(OctetString):
    """Custom type sonetSectionTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SonetSectionTraceReceived_Type.__name__ = "OctetString"
_SonetSectionTraceReceived_Object = MibTableColumn
sonetSectionTraceReceived = _SonetSectionTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 14),
    _SonetSectionTraceReceived_Type()
)
sonetSectionTraceReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionTraceReceived.setStatus("mandatory")


class _SonetSectionStatAlarmStatus_Type(Integer32):
    """Custom type sonetSectionStatAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_SonetSectionStatAlarmStatus_Type.__name__ = "Integer32"
_SonetSectionStatAlarmStatus_Object = MibTableColumn
sonetSectionStatAlarmStatus = _SonetSectionStatAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 4, 1, 15),
    _SonetSectionStatAlarmStatus_Type()
)
sonetSectionStatAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionStatAlarmStatus.setStatus("mandatory")
_SonetSectionCounterTable_Object = MibTable
sonetSectionCounterTable = _SonetSectionCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 5)
)
if mibBuilder.loadTexts:
    sonetSectionCounterTable.setStatus("mandatory")
_SonetSectionCounterEntry_Object = MibTableRow
sonetSectionCounterEntry = _SonetSectionCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 5, 1)
)
sonetSectionCounterEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sectionCounterLineNum"),
)
if mibBuilder.loadTexts:
    sonetSectionCounterEntry.setStatus("mandatory")


class _SectionCounterLineNum_Type(Integer32):
    """Custom type sectionCounterLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SectionCounterLineNum_Type.__name__ = "Integer32"
_SectionCounterLineNum_Object = MibTableColumn
sectionCounterLineNum = _SectionCounterLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 5, 1, 1),
    _SectionCounterLineNum_Type()
)
sectionCounterLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectionCounterLineNum.setStatus("mandatory")
_SonetSectionCounterLOSs_Type = Gauge32
_SonetSectionCounterLOSs_Object = MibTableColumn
sonetSectionCounterLOSs = _SonetSectionCounterLOSs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 5, 1, 2),
    _SonetSectionCounterLOSs_Type()
)
sonetSectionCounterLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCounterLOSs.setStatus("mandatory")
_SonetSectionCounterLOFs_Type = Gauge32
_SonetSectionCounterLOFs_Object = MibTableColumn
sonetSectionCounterLOFs = _SonetSectionCounterLOFs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 5, 1, 3),
    _SonetSectionCounterLOFs_Type()
)
sonetSectionCounterLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionCounterLOFs.setStatus("mandatory")


class _SonetSectionCounterClrButton_Type(Integer32):
    """Custom type sonetSectionCounterClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetSectionCounterClrButton_Type.__name__ = "Integer32"
_SonetSectionCounterClrButton_Object = MibTableColumn
sonetSectionCounterClrButton = _SonetSectionCounterClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 3, 5, 1, 4),
    _SonetSectionCounterClrButton_Type()
)
sonetSectionCounterClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionCounterClrButton.setStatus("mandatory")
_CwsonetLine_ObjectIdentity = ObjectIdentity
cwsonetLine = _CwsonetLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4)
)
_CwSonetLineCurrentTable_Object = MibTable
cwSonetLineCurrentTable = _CwSonetLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwSonetLineCurrentTable.setStatus("mandatory")
_CwSonetLineCurrentEntry_Object = MibTableRow
cwSonetLineCurrentEntry = _CwSonetLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1)
)
cwSonetLineCurrentEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetLineCurrentLineNum"),
)
if mibBuilder.loadTexts:
    cwSonetLineCurrentEntry.setStatus("mandatory")


class _CwSonetLineCurrentLineNum_Type(Integer32):
    """Custom type cwSonetLineCurrentLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetLineCurrentLineNum_Type.__name__ = "Integer32"
_CwSonetLineCurrentLineNum_Object = MibTableColumn
cwSonetLineCurrentLineNum = _CwSonetLineCurrentLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 1),
    _CwSonetLineCurrentLineNum_Type()
)
cwSonetLineCurrentLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrentLineNum.setStatus("mandatory")


class _CwSonetLineCurrentStatus_Type(Integer32):
    """Custom type cwSonetLineCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CwSonetLineCurrentStatus_Type.__name__ = "Integer32"
_CwSonetLineCurrentStatus_Object = MibTableColumn
cwSonetLineCurrentStatus = _CwSonetLineCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 2),
    _CwSonetLineCurrentStatus_Type()
)
cwSonetLineCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrentStatus.setStatus("mandatory")


class _CwSonetLineCurrentValidFlag_Type(Integer32):
    """Custom type cwSonetLineCurrentValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetLineCurrentValidFlag_Type.__name__ = "Integer32"
_CwSonetLineCurrentValidFlag_Object = MibTableColumn
cwSonetLineCurrentValidFlag = _CwSonetLineCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 3),
    _CwSonetLineCurrentValidFlag_Type()
)
cwSonetLineCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrentValidFlag.setStatus("mandatory")


class _CwSonetLineCurrent15minTimeElapsed_Type(Integer32):
    """Custom type cwSonetLineCurrent15minTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CwSonetLineCurrent15minTimeElapsed_Type.__name__ = "Integer32"
_CwSonetLineCurrent15minTimeElapsed_Object = MibTableColumn
cwSonetLineCurrent15minTimeElapsed = _CwSonetLineCurrent15minTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 4),
    _CwSonetLineCurrent15minTimeElapsed_Type()
)
cwSonetLineCurrent15minTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrent15minTimeElapsed.setStatus("mandatory")
_CwSonetLineCurrentESs_Type = Gauge32
_CwSonetLineCurrentESs_Object = MibTableColumn
cwSonetLineCurrentESs = _CwSonetLineCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 5),
    _CwSonetLineCurrentESs_Type()
)
cwSonetLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrentESs.setStatus("mandatory")
_CwSonetLineCurrentSESs_Type = Gauge32
_CwSonetLineCurrentSESs_Object = MibTableColumn
cwSonetLineCurrentSESs = _CwSonetLineCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 6),
    _CwSonetLineCurrentSESs_Type()
)
cwSonetLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrentSESs.setStatus("mandatory")
_CwSonetLineCurrentCVs_Type = Gauge32
_CwSonetLineCurrentCVs_Object = MibTableColumn
cwSonetLineCurrentCVs = _CwSonetLineCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 7),
    _CwSonetLineCurrentCVs_Type()
)
cwSonetLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrentCVs.setStatus("mandatory")
_CwSonetLineCurrentUASs_Type = Gauge32
_CwSonetLineCurrentUASs_Object = MibTableColumn
cwSonetLineCurrentUASs = _CwSonetLineCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 8),
    _CwSonetLineCurrentUASs_Type()
)
cwSonetLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineCurrentUASs.setStatus("mandatory")


class _CwSonetLineCurrentClrButton_Type(Integer32):
    """Custom type cwSonetLineCurrentClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_CwSonetLineCurrentClrButton_Type.__name__ = "Integer32"
_CwSonetLineCurrentClrButton_Object = MibTableColumn
cwSonetLineCurrentClrButton = _CwSonetLineCurrentClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 1, 1, 9),
    _CwSonetLineCurrentClrButton_Type()
)
cwSonetLineCurrentClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwSonetLineCurrentClrButton.setStatus("mandatory")
_SonetLineCurrentDayTable_Object = MibTable
sonetLineCurrentDayTable = _SonetLineCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sonetLineCurrentDayTable.setStatus("mandatory")
_SonetLineCurrentDayEntry_Object = MibTableRow
sonetLineCurrentDayEntry = _SonetLineCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1)
)
sonetLineCurrentDayEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "lineCurrentDayLineNum"),
)
if mibBuilder.loadTexts:
    sonetLineCurrentDayEntry.setStatus("mandatory")


class _LineCurrentDayLineNum_Type(Integer32):
    """Custom type lineCurrentDayLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_LineCurrentDayLineNum_Type.__name__ = "Integer32"
_LineCurrentDayLineNum_Object = MibTableColumn
lineCurrentDayLineNum = _LineCurrentDayLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 1),
    _LineCurrentDayLineNum_Type()
)
lineCurrentDayLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCurrentDayLineNum.setStatus("mandatory")


class _SonetLineCurrentDayValidFlag_Type(Integer32):
    """Custom type sonetLineCurrentDayValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_SonetLineCurrentDayValidFlag_Type.__name__ = "Integer32"
_SonetLineCurrentDayValidFlag_Object = MibTableColumn
sonetLineCurrentDayValidFlag = _SonetLineCurrentDayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 2),
    _SonetLineCurrentDayValidFlag_Type()
)
sonetLineCurrentDayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentDayValidFlag.setStatus("mandatory")
_SonetLineCurrentDayESs_Type = Gauge32
_SonetLineCurrentDayESs_Object = MibTableColumn
sonetLineCurrentDayESs = _SonetLineCurrentDayESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 3),
    _SonetLineCurrentDayESs_Type()
)
sonetLineCurrentDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentDayESs.setStatus("mandatory")
_SonetLineCurrentDaySESs_Type = Gauge32
_SonetLineCurrentDaySESs_Object = MibTableColumn
sonetLineCurrentDaySESs = _SonetLineCurrentDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 4),
    _SonetLineCurrentDaySESs_Type()
)
sonetLineCurrentDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentDaySESs.setStatus("mandatory")
_SonetLineCurrentDayCVs_Type = Gauge32
_SonetLineCurrentDayCVs_Object = MibTableColumn
sonetLineCurrentDayCVs = _SonetLineCurrentDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 5),
    _SonetLineCurrentDayCVs_Type()
)
sonetLineCurrentDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentDayCVs.setStatus("mandatory")
_SonetLineCurrentDayFCs_Type = Gauge32
_SonetLineCurrentDayFCs_Object = MibTableColumn
sonetLineCurrentDayFCs = _SonetLineCurrentDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 6),
    _SonetLineCurrentDayFCs_Type()
)
sonetLineCurrentDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentDayFCs.setStatus("mandatory")
_SonetLineCurrentDayUASs_Type = Gauge32
_SonetLineCurrentDayUASs_Object = MibTableColumn
sonetLineCurrentDayUASs = _SonetLineCurrentDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 7),
    _SonetLineCurrentDayUASs_Type()
)
sonetLineCurrentDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCurrentDayUASs.setStatus("mandatory")


class _SonetLineCurrentDayClrButton_Type(Integer32):
    """Custom type sonetLineCurrentDayClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetLineCurrentDayClrButton_Type.__name__ = "Integer32"
_SonetLineCurrentDayClrButton_Object = MibTableColumn
sonetLineCurrentDayClrButton = _SonetLineCurrentDayClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 2, 1, 8),
    _SonetLineCurrentDayClrButton_Type()
)
sonetLineCurrentDayClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentDayClrButton.setStatus("mandatory")
_CwSonetLineIntervalTable_Object = MibTable
cwSonetLineIntervalTable = _CwSonetLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cwSonetLineIntervalTable.setStatus("mandatory")
_CwSonetLineIntervalEntry_Object = MibTableRow
cwSonetLineIntervalEntry = _CwSonetLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1)
)
cwSonetLineIntervalEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetLineIntervalLineNum"),
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    cwSonetLineIntervalEntry.setStatus("mandatory")


class _CwSonetLineIntervalLineNum_Type(Integer32):
    """Custom type cwSonetLineIntervalLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetLineIntervalLineNum_Type.__name__ = "Integer32"
_CwSonetLineIntervalLineNum_Object = MibTableColumn
cwSonetLineIntervalLineNum = _CwSonetLineIntervalLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 1),
    _CwSonetLineIntervalLineNum_Type()
)
cwSonetLineIntervalLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalLineNum.setStatus("mandatory")


class _CwSonetLineIntervalNumber_Type(Integer32):
    """Custom type cwSonetLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CwSonetLineIntervalNumber_Type.__name__ = "Integer32"
_CwSonetLineIntervalNumber_Object = MibTableColumn
cwSonetLineIntervalNumber = _CwSonetLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 2),
    _CwSonetLineIntervalNumber_Type()
)
cwSonetLineIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalNumber.setStatus("mandatory")


class _CwSonetLineIntervalValidFlag_Type(Integer32):
    """Custom type cwSonetLineIntervalValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetLineIntervalValidFlag_Type.__name__ = "Integer32"
_CwSonetLineIntervalValidFlag_Object = MibTableColumn
cwSonetLineIntervalValidFlag = _CwSonetLineIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 3),
    _CwSonetLineIntervalValidFlag_Type()
)
cwSonetLineIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalValidFlag.setStatus("mandatory")
_CwSonetLineIntervalESs_Type = Gauge32
_CwSonetLineIntervalESs_Object = MibTableColumn
cwSonetLineIntervalESs = _CwSonetLineIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 4),
    _CwSonetLineIntervalESs_Type()
)
cwSonetLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalESs.setStatus("mandatory")
_CwSonetLineIntervalSESs_Type = Gauge32
_CwSonetLineIntervalSESs_Object = MibTableColumn
cwSonetLineIntervalSESs = _CwSonetLineIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 5),
    _CwSonetLineIntervalSESs_Type()
)
cwSonetLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalSESs.setStatus("mandatory")
_CwSonetLineIntervalCVs_Type = Gauge32
_CwSonetLineIntervalCVs_Object = MibTableColumn
cwSonetLineIntervalCVs = _CwSonetLineIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 6),
    _CwSonetLineIntervalCVs_Type()
)
cwSonetLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalCVs.setStatus("mandatory")
_CwSonetLineIntervalFCs_Type = Gauge32
_CwSonetLineIntervalFCs_Object = MibTableColumn
cwSonetLineIntervalFCs = _CwSonetLineIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 7),
    _CwSonetLineIntervalFCs_Type()
)
cwSonetLineIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalFCs.setStatus("mandatory")
_CwSonetLineIntervalUASs_Type = Gauge32
_CwSonetLineIntervalUASs_Object = MibTableColumn
cwSonetLineIntervalUASs = _CwSonetLineIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 3, 1, 8),
    _CwSonetLineIntervalUASs_Type()
)
cwSonetLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetLineIntervalUASs.setStatus("mandatory")
_CwSonetFarEndLineCurrentTable_Object = MibTable
cwSonetFarEndLineCurrentTable = _CwSonetFarEndLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentTable.setStatus("mandatory")
_CwSonetFarEndLineCurrentEntry_Object = MibTableRow
cwSonetFarEndLineCurrentEntry = _CwSonetFarEndLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1)
)
cwSonetFarEndLineCurrentEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetFELineCurrentLineNum"),
)
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentEntry.setStatus("mandatory")


class _CwSonetFELineCurrentLineNum_Type(Integer32):
    """Custom type cwSonetFELineCurrentLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetFELineCurrentLineNum_Type.__name__ = "Integer32"
_CwSonetFELineCurrentLineNum_Object = MibTableColumn
cwSonetFELineCurrentLineNum = _CwSonetFELineCurrentLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 1),
    _CwSonetFELineCurrentLineNum_Type()
)
cwSonetFELineCurrentLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFELineCurrentLineNum.setStatus("mandatory")


class _CwSonetFarEndLineCurrentValidFlag_Type(Integer32):
    """Custom type cwSonetFarEndLineCurrentValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetFarEndLineCurrentValidFlag_Type.__name__ = "Integer32"
_CwSonetFarEndLineCurrentValidFlag_Object = MibTableColumn
cwSonetFarEndLineCurrentValidFlag = _CwSonetFarEndLineCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 2),
    _CwSonetFarEndLineCurrentValidFlag_Type()
)
cwSonetFarEndLineCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentValidFlag.setStatus("mandatory")


class _CwSonetFarEndLineCurrentTimeElapsed_Type(Integer32):
    """Custom type cwSonetFarEndLineCurrentTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CwSonetFarEndLineCurrentTimeElapsed_Type.__name__ = "Integer32"
_CwSonetFarEndLineCurrentTimeElapsed_Object = MibTableColumn
cwSonetFarEndLineCurrentTimeElapsed = _CwSonetFarEndLineCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 3),
    _CwSonetFarEndLineCurrentTimeElapsed_Type()
)
cwSonetFarEndLineCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentTimeElapsed.setStatus("mandatory")
_CwSonetFarEndLineCurrentESs_Type = Gauge32
_CwSonetFarEndLineCurrentESs_Object = MibTableColumn
cwSonetFarEndLineCurrentESs = _CwSonetFarEndLineCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 4),
    _CwSonetFarEndLineCurrentESs_Type()
)
cwSonetFarEndLineCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentESs.setStatus("mandatory")
_CwSonetFarEndLineCurrentSESs_Type = Gauge32
_CwSonetFarEndLineCurrentSESs_Object = MibTableColumn
cwSonetFarEndLineCurrentSESs = _CwSonetFarEndLineCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 5),
    _CwSonetFarEndLineCurrentSESs_Type()
)
cwSonetFarEndLineCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentSESs.setStatus("mandatory")
_CwSonetFarEndLineCurrentCVs_Type = Gauge32
_CwSonetFarEndLineCurrentCVs_Object = MibTableColumn
cwSonetFarEndLineCurrentCVs = _CwSonetFarEndLineCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 6),
    _CwSonetFarEndLineCurrentCVs_Type()
)
cwSonetFarEndLineCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentCVs.setStatus("mandatory")
_CwSonetFarEndLineCurrentFCs_Type = Gauge32
_CwSonetFarEndLineCurrentFCs_Object = MibTableColumn
cwSonetFarEndLineCurrentFCs = _CwSonetFarEndLineCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 7),
    _CwSonetFarEndLineCurrentFCs_Type()
)
cwSonetFarEndLineCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentFCs.setStatus("mandatory")
_CwSonetFarEndLineCurrentUASs_Type = Gauge32
_CwSonetFarEndLineCurrentUASs_Object = MibTableColumn
cwSonetFarEndLineCurrentUASs = _CwSonetFarEndLineCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 8),
    _CwSonetFarEndLineCurrentUASs_Type()
)
cwSonetFarEndLineCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentUASs.setStatus("mandatory")


class _CwSonetFarEndLineCurrentClrButton_Type(Integer32):
    """Custom type cwSonetFarEndLineCurrentClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_CwSonetFarEndLineCurrentClrButton_Type.__name__ = "Integer32"
_CwSonetFarEndLineCurrentClrButton_Object = MibTableColumn
cwSonetFarEndLineCurrentClrButton = _CwSonetFarEndLineCurrentClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 4, 1, 9),
    _CwSonetFarEndLineCurrentClrButton_Type()
)
cwSonetFarEndLineCurrentClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwSonetFarEndLineCurrentClrButton.setStatus("mandatory")
_SonetFarEndLineCurrentDayTable_Object = MibTable
sonetFarEndLineCurrentDayTable = _SonetFarEndLineCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5)
)
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayTable.setStatus("mandatory")
_SonetFarEndLineCurrentDayEntry_Object = MibTableRow
sonetFarEndLineCurrentDayEntry = _SonetFarEndLineCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1)
)
sonetFarEndLineCurrentDayEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetFELineCurrentDayLineNum"),
)
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayEntry.setStatus("mandatory")


class _SonetFELineCurrentDayLineNum_Type(Integer32):
    """Custom type sonetFELineCurrentDayLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetFELineCurrentDayLineNum_Type.__name__ = "Integer32"
_SonetFELineCurrentDayLineNum_Object = MibTableColumn
sonetFELineCurrentDayLineNum = _SonetFELineCurrentDayLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 1),
    _SonetFELineCurrentDayLineNum_Type()
)
sonetFELineCurrentDayLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFELineCurrentDayLineNum.setStatus("mandatory")


class _SonetFarEndLineCurrentDayValidFlag_Type(Integer32):
    """Custom type sonetFarEndLineCurrentDayValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_SonetFarEndLineCurrentDayValidFlag_Type.__name__ = "Integer32"
_SonetFarEndLineCurrentDayValidFlag_Object = MibTableColumn
sonetFarEndLineCurrentDayValidFlag = _SonetFarEndLineCurrentDayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 2),
    _SonetFarEndLineCurrentDayValidFlag_Type()
)
sonetFarEndLineCurrentDayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayValidFlag.setStatus("mandatory")
_SonetFarEndLineCurrentDayESs_Type = Gauge32
_SonetFarEndLineCurrentDayESs_Object = MibTableColumn
sonetFarEndLineCurrentDayESs = _SonetFarEndLineCurrentDayESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 3),
    _SonetFarEndLineCurrentDayESs_Type()
)
sonetFarEndLineCurrentDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayESs.setStatus("mandatory")
_SonetFarEndLineCurrentDaySESs_Type = Gauge32
_SonetFarEndLineCurrentDaySESs_Object = MibTableColumn
sonetFarEndLineCurrentDaySESs = _SonetFarEndLineCurrentDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 4),
    _SonetFarEndLineCurrentDaySESs_Type()
)
sonetFarEndLineCurrentDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDaySESs.setStatus("mandatory")
_SonetFarEndLineCurrentDayCVs_Type = Gauge32
_SonetFarEndLineCurrentDayCVs_Object = MibTableColumn
sonetFarEndLineCurrentDayCVs = _SonetFarEndLineCurrentDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 5),
    _SonetFarEndLineCurrentDayCVs_Type()
)
sonetFarEndLineCurrentDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayCVs.setStatus("mandatory")
_SonetFarEndLineCurrentDayFCs_Type = Gauge32
_SonetFarEndLineCurrentDayFCs_Object = MibTableColumn
sonetFarEndLineCurrentDayFCs = _SonetFarEndLineCurrentDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 6),
    _SonetFarEndLineCurrentDayFCs_Type()
)
sonetFarEndLineCurrentDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayFCs.setStatus("mandatory")
_SonetFarEndLineCurrentDayUASs_Type = Gauge32
_SonetFarEndLineCurrentDayUASs_Object = MibTableColumn
sonetFarEndLineCurrentDayUASs = _SonetFarEndLineCurrentDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 7),
    _SonetFarEndLineCurrentDayUASs_Type()
)
sonetFarEndLineCurrentDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayUASs.setStatus("mandatory")


class _SonetFarEndLineCurrentDayClrButton_Type(Integer32):
    """Custom type sonetFarEndLineCurrentDayClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetFarEndLineCurrentDayClrButton_Type.__name__ = "Integer32"
_SonetFarEndLineCurrentDayClrButton_Object = MibTableColumn
sonetFarEndLineCurrentDayClrButton = _SonetFarEndLineCurrentDayClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 5, 1, 8),
    _SonetFarEndLineCurrentDayClrButton_Type()
)
sonetFarEndLineCurrentDayClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFarEndLineCurrentDayClrButton.setStatus("mandatory")
_CwSonetFarEndLineIntervalTable_Object = MibTable
cwSonetFarEndLineIntervalTable = _CwSonetFarEndLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalTable.setStatus("mandatory")
_CwSonetFarEndLineIntervalEntry_Object = MibTableRow
cwSonetFarEndLineIntervalEntry = _CwSonetFarEndLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1)
)
cwSonetFarEndLineIntervalEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetFELineIntervalLineNum"),
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetFarEndLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalEntry.setStatus("mandatory")


class _CwSonetFELineIntervalLineNum_Type(Integer32):
    """Custom type cwSonetFELineIntervalLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetFELineIntervalLineNum_Type.__name__ = "Integer32"
_CwSonetFELineIntervalLineNum_Object = MibTableColumn
cwSonetFELineIntervalLineNum = _CwSonetFELineIntervalLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 1),
    _CwSonetFELineIntervalLineNum_Type()
)
cwSonetFELineIntervalLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFELineIntervalLineNum.setStatus("mandatory")


class _CwSonetFarEndLineIntervalNumber_Type(Integer32):
    """Custom type cwSonetFarEndLineIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CwSonetFarEndLineIntervalNumber_Type.__name__ = "Integer32"
_CwSonetFarEndLineIntervalNumber_Object = MibTableColumn
cwSonetFarEndLineIntervalNumber = _CwSonetFarEndLineIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 2),
    _CwSonetFarEndLineIntervalNumber_Type()
)
cwSonetFarEndLineIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalNumber.setStatus("mandatory")


class _CwSonetFarEndLineIntervalValidFlag_Type(Integer32):
    """Custom type cwSonetFarEndLineIntervalValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetFarEndLineIntervalValidFlag_Type.__name__ = "Integer32"
_CwSonetFarEndLineIntervalValidFlag_Object = MibTableColumn
cwSonetFarEndLineIntervalValidFlag = _CwSonetFarEndLineIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 3),
    _CwSonetFarEndLineIntervalValidFlag_Type()
)
cwSonetFarEndLineIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalValidFlag.setStatus("mandatory")
_CwSonetFarEndLineIntervalESs_Type = Gauge32
_CwSonetFarEndLineIntervalESs_Object = MibTableColumn
cwSonetFarEndLineIntervalESs = _CwSonetFarEndLineIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 4),
    _CwSonetFarEndLineIntervalESs_Type()
)
cwSonetFarEndLineIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalESs.setStatus("mandatory")
_CwSonetFarEndLineIntervalSESs_Type = Gauge32
_CwSonetFarEndLineIntervalSESs_Object = MibTableColumn
cwSonetFarEndLineIntervalSESs = _CwSonetFarEndLineIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 5),
    _CwSonetFarEndLineIntervalSESs_Type()
)
cwSonetFarEndLineIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalSESs.setStatus("mandatory")
_CwSonetFarEndLineIntervalCVs_Type = Gauge32
_CwSonetFarEndLineIntervalCVs_Object = MibTableColumn
cwSonetFarEndLineIntervalCVs = _CwSonetFarEndLineIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 6),
    _CwSonetFarEndLineIntervalCVs_Type()
)
cwSonetFarEndLineIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalCVs.setStatus("mandatory")
_CwSonetFarEndLineIntervalFCs_Type = Gauge32
_CwSonetFarEndLineIntervalFCs_Object = MibTableColumn
cwSonetFarEndLineIntervalFCs = _CwSonetFarEndLineIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 7),
    _CwSonetFarEndLineIntervalFCs_Type()
)
cwSonetFarEndLineIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalFCs.setStatus("mandatory")
_CwSonetFarEndLineIntervalUASs_Type = Gauge32
_CwSonetFarEndLineIntervalUASs_Object = MibTableColumn
cwSonetFarEndLineIntervalUASs = _CwSonetFarEndLineIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 6, 1, 8),
    _CwSonetFarEndLineIntervalUASs_Type()
)
cwSonetFarEndLineIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndLineIntervalUASs.setStatus("mandatory")
_SonetLineAlarmTable_Object = MibTable
sonetLineAlarmTable = _SonetLineAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7)
)
if mibBuilder.loadTexts:
    sonetLineAlarmTable.setStatus("mandatory")
_SonetLineAlarmEntry_Object = MibTableRow
sonetLineAlarmEntry = _SonetLineAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1)
)
sonetLineAlarmEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetLineAlarmLineNum"),
)
if mibBuilder.loadTexts:
    sonetLineAlarmEntry.setStatus("mandatory")


class _SonetLineAlarmLineNum_Type(Integer32):
    """Custom type sonetLineAlarmLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetLineAlarmLineNum_Type.__name__ = "Integer32"
_SonetLineAlarmLineNum_Object = MibTableColumn
sonetLineAlarmLineNum = _SonetLineAlarmLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 1),
    _SonetLineAlarmLineNum_Type()
)
sonetLineAlarmLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineAlarmLineNum.setStatus("mandatory")


class _SonetLineStatisticalAlarmSeverity_Type(Integer32):
    """Custom type sonetLineStatisticalAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_SonetLineStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_SonetLineStatisticalAlarmSeverity_Object = MibTableColumn
sonetLineStatisticalAlarmSeverity = _SonetLineStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 2),
    _SonetLineStatisticalAlarmSeverity_Type()
)
sonetLineStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineStatisticalAlarmSeverity.setStatus("mandatory")


class _SonetLineCurrent15minESsThreshold_Type(Integer32):
    """Custom type sonetLineCurrent15minESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrent15minESsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrent15minESsThreshold_Object = MibTableColumn
sonetLineCurrent15minESsThreshold = _SonetLineCurrent15minESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 3),
    _SonetLineCurrent15minESsThreshold_Type()
)
sonetLineCurrent15minESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrent15minESsThreshold.setStatus("mandatory")


class _SonetLineCurrentDayESsThreshold_Type(Integer32):
    """Custom type sonetLineCurrentDayESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrentDayESsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentDayESsThreshold_Object = MibTableColumn
sonetLineCurrentDayESsThreshold = _SonetLineCurrentDayESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 4),
    _SonetLineCurrentDayESsThreshold_Type()
)
sonetLineCurrentDayESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentDayESsThreshold.setStatus("mandatory")


class _SonetLineCurrent15minSESsThreshold_Type(Integer32):
    """Custom type sonetLineCurrent15minSESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrent15minSESsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrent15minSESsThreshold_Object = MibTableColumn
sonetLineCurrent15minSESsThreshold = _SonetLineCurrent15minSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 5),
    _SonetLineCurrent15minSESsThreshold_Type()
)
sonetLineCurrent15minSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrent15minSESsThreshold.setStatus("mandatory")


class _SonetLineCurrentDaySESsThreshold_Type(Integer32):
    """Custom type sonetLineCurrentDaySESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrentDaySESsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentDaySESsThreshold_Object = MibTableColumn
sonetLineCurrentDaySESsThreshold = _SonetLineCurrentDaySESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 6),
    _SonetLineCurrentDaySESsThreshold_Type()
)
sonetLineCurrentDaySESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentDaySESsThreshold.setStatus("mandatory")


class _SonetLineCurrent15minCVsThreshold_Type(Integer32):
    """Custom type sonetLineCurrent15minCVsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrent15minCVsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrent15minCVsThreshold_Object = MibTableColumn
sonetLineCurrent15minCVsThreshold = _SonetLineCurrent15minCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 7),
    _SonetLineCurrent15minCVsThreshold_Type()
)
sonetLineCurrent15minCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrent15minCVsThreshold.setStatus("mandatory")


class _SonetLineCurrentDayCVsThreshold_Type(Integer32):
    """Custom type sonetLineCurrentDayCVsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrentDayCVsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentDayCVsThreshold_Object = MibTableColumn
sonetLineCurrentDayCVsThreshold = _SonetLineCurrentDayCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 8),
    _SonetLineCurrentDayCVsThreshold_Type()
)
sonetLineCurrentDayCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentDayCVsThreshold.setStatus("mandatory")


class _SonetLineCurrent15minUASsThreshold_Type(Integer32):
    """Custom type sonetLineCurrent15minUASsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrent15minUASsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrent15minUASsThreshold_Object = MibTableColumn
sonetLineCurrent15minUASsThreshold = _SonetLineCurrent15minUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 9),
    _SonetLineCurrent15minUASsThreshold_Type()
)
sonetLineCurrent15minUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrent15minUASsThreshold.setStatus("mandatory")


class _SonetLineCurrentDayUASsThreshold_Type(Integer32):
    """Custom type sonetLineCurrentDayUASsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetLineCurrentDayUASsThreshold_Type.__name__ = "Integer32"
_SonetLineCurrentDayUASsThreshold_Object = MibTableColumn
sonetLineCurrentDayUASsThreshold = _SonetLineCurrentDayUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 10),
    _SonetLineCurrentDayUASsThreshold_Type()
)
sonetLineCurrentDayUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCurrentDayUASsThreshold.setStatus("mandatory")


class _SonetLineStatAlarmStatus_Type(Integer32):
    """Custom type sonetLineStatAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131071),
    )


_SonetLineStatAlarmStatus_Type.__name__ = "Integer32"
_SonetLineStatAlarmStatus_Object = MibTableColumn
sonetLineStatAlarmStatus = _SonetLineStatAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 7, 1, 11),
    _SonetLineStatAlarmStatus_Type()
)
sonetLineStatAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineStatAlarmStatus.setStatus("mandatory")
_SonetLineCounterTable_Object = MibTable
sonetLineCounterTable = _SonetLineCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 8)
)
if mibBuilder.loadTexts:
    sonetLineCounterTable.setStatus("mandatory")
_SonetLineCounterEntry_Object = MibTableRow
sonetLineCounterEntry = _SonetLineCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 8, 1)
)
sonetLineCounterEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetLineCounterLineNum"),
)
if mibBuilder.loadTexts:
    sonetLineCounterEntry.setStatus("mandatory")


class _SonetLineCounterLineNum_Type(Integer32):
    """Custom type sonetLineCounterLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetLineCounterLineNum_Type.__name__ = "Integer32"
_SonetLineCounterLineNum_Object = MibTableColumn
sonetLineCounterLineNum = _SonetLineCounterLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 8, 1, 1),
    _SonetLineCounterLineNum_Type()
)
sonetLineCounterLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCounterLineNum.setStatus("mandatory")
_SonetLineCounterAISs_Type = Gauge32
_SonetLineCounterAISs_Object = MibTableColumn
sonetLineCounterAISs = _SonetLineCounterAISs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 8, 1, 2),
    _SonetLineCounterAISs_Type()
)
sonetLineCounterAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCounterAISs.setStatus("mandatory")
_SonetLineCounterRFIs_Type = Gauge32
_SonetLineCounterRFIs_Object = MibTableColumn
sonetLineCounterRFIs = _SonetLineCounterRFIs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 8, 1, 3),
    _SonetLineCounterRFIs_Type()
)
sonetLineCounterRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCounterRFIs.setStatus("mandatory")


class _SonetLineCounterClrButton_Type(Integer32):
    """Custom type sonetLineCounterClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetLineCounterClrButton_Type.__name__ = "Integer32"
_SonetLineCounterClrButton_Object = MibTableColumn
sonetLineCounterClrButton = _SonetLineCounterClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 4, 8, 1, 4),
    _SonetLineCounterClrButton_Type()
)
sonetLineCounterClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineCounterClrButton.setStatus("mandatory")
_CwsonetPath_ObjectIdentity = ObjectIdentity
cwsonetPath = _CwsonetPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5)
)
_CwSonetPathCurrentTable_Object = MibTable
cwSonetPathCurrentTable = _CwSonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cwSonetPathCurrentTable.setStatus("mandatory")
_CwSonetPathCurrentEntry_Object = MibTableRow
cwSonetPathCurrentEntry = _CwSonetPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1)
)
cwSonetPathCurrentEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetPathCurrentLineNum"),
)
if mibBuilder.loadTexts:
    cwSonetPathCurrentEntry.setStatus("mandatory")


class _CwSonetPathCurrentLineNum_Type(Integer32):
    """Custom type cwSonetPathCurrentLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetPathCurrentLineNum_Type.__name__ = "Integer32"
_CwSonetPathCurrentLineNum_Object = MibTableColumn
cwSonetPathCurrentLineNum = _CwSonetPathCurrentLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 1),
    _CwSonetPathCurrentLineNum_Type()
)
cwSonetPathCurrentLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentLineNum.setStatus("mandatory")


class _CwSonetPathCurrentStatus_Type(Integer32):
    """Custom type cwSonetPathCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_CwSonetPathCurrentStatus_Type.__name__ = "Integer32"
_CwSonetPathCurrentStatus_Object = MibTableColumn
cwSonetPathCurrentStatus = _CwSonetPathCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 2),
    _CwSonetPathCurrentStatus_Type()
)
cwSonetPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentStatus.setStatus("mandatory")


class _CwSonetPathCurrentValidFlag_Type(Integer32):
    """Custom type cwSonetPathCurrentValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetPathCurrentValidFlag_Type.__name__ = "Integer32"
_CwSonetPathCurrentValidFlag_Object = MibTableColumn
cwSonetPathCurrentValidFlag = _CwSonetPathCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 3),
    _CwSonetPathCurrentValidFlag_Type()
)
cwSonetPathCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentValidFlag.setStatus("mandatory")


class _CwSonetPathCurrentTimeElapsed_Type(Integer32):
    """Custom type cwSonetPathCurrentTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CwSonetPathCurrentTimeElapsed_Type.__name__ = "Integer32"
_CwSonetPathCurrentTimeElapsed_Object = MibTableColumn
cwSonetPathCurrentTimeElapsed = _CwSonetPathCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 4),
    _CwSonetPathCurrentTimeElapsed_Type()
)
cwSonetPathCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentTimeElapsed.setStatus("mandatory")
_CwSonetPathCurrentESs_Type = Gauge32
_CwSonetPathCurrentESs_Object = MibTableColumn
cwSonetPathCurrentESs = _CwSonetPathCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 5),
    _CwSonetPathCurrentESs_Type()
)
cwSonetPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentESs.setStatus("mandatory")
_CwSonetPathCurrentSESs_Type = Gauge32
_CwSonetPathCurrentSESs_Object = MibTableColumn
cwSonetPathCurrentSESs = _CwSonetPathCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 6),
    _CwSonetPathCurrentSESs_Type()
)
cwSonetPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentSESs.setStatus("mandatory")
_CwSonetPathCurrentCVs_Type = Gauge32
_CwSonetPathCurrentCVs_Object = MibTableColumn
cwSonetPathCurrentCVs = _CwSonetPathCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 7),
    _CwSonetPathCurrentCVs_Type()
)
cwSonetPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentCVs.setStatus("mandatory")
_CwSonetPathCurrentFCs_Type = Gauge32
_CwSonetPathCurrentFCs_Object = MibTableColumn
cwSonetPathCurrentFCs = _CwSonetPathCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 8),
    _CwSonetPathCurrentFCs_Type()
)
cwSonetPathCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentFCs.setStatus("mandatory")
_CwSonetPathCurrentUASs_Type = Gauge32
_CwSonetPathCurrentUASs_Object = MibTableColumn
cwSonetPathCurrentUASs = _CwSonetPathCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 9),
    _CwSonetPathCurrentUASs_Type()
)
cwSonetPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathCurrentUASs.setStatus("mandatory")


class _CwSonetPathCurrentClrButton_Type(Integer32):
    """Custom type cwSonetPathCurrentClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_CwSonetPathCurrentClrButton_Type.__name__ = "Integer32"
_CwSonetPathCurrentClrButton_Object = MibTableColumn
cwSonetPathCurrentClrButton = _CwSonetPathCurrentClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 1, 1, 10),
    _CwSonetPathCurrentClrButton_Type()
)
cwSonetPathCurrentClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwSonetPathCurrentClrButton.setStatus("mandatory")
_SonetPathCurrentDayTable_Object = MibTable
sonetPathCurrentDayTable = _SonetPathCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2)
)
if mibBuilder.loadTexts:
    sonetPathCurrentDayTable.setStatus("mandatory")
_SonetPathCurrentDayEntry_Object = MibTableRow
sonetPathCurrentDayEntry = _SonetPathCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1)
)
sonetPathCurrentDayEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetPathCurrentDayLineNum"),
)
if mibBuilder.loadTexts:
    sonetPathCurrentDayEntry.setStatus("mandatory")


class _SonetPathCurrentDayLineNum_Type(Integer32):
    """Custom type sonetPathCurrentDayLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetPathCurrentDayLineNum_Type.__name__ = "Integer32"
_SonetPathCurrentDayLineNum_Object = MibTableColumn
sonetPathCurrentDayLineNum = _SonetPathCurrentDayLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 1),
    _SonetPathCurrentDayLineNum_Type()
)
sonetPathCurrentDayLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentDayLineNum.setStatus("mandatory")


class _SonetPathCurrentDayValidFlag_Type(Integer32):
    """Custom type sonetPathCurrentDayValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_SonetPathCurrentDayValidFlag_Type.__name__ = "Integer32"
_SonetPathCurrentDayValidFlag_Object = MibTableColumn
sonetPathCurrentDayValidFlag = _SonetPathCurrentDayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 2),
    _SonetPathCurrentDayValidFlag_Type()
)
sonetPathCurrentDayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentDayValidFlag.setStatus("mandatory")
_SonetPathCurrentDayESs_Type = Gauge32
_SonetPathCurrentDayESs_Object = MibTableColumn
sonetPathCurrentDayESs = _SonetPathCurrentDayESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 3),
    _SonetPathCurrentDayESs_Type()
)
sonetPathCurrentDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentDayESs.setStatus("mandatory")
_SonetPathCurrentDaySESs_Type = Gauge32
_SonetPathCurrentDaySESs_Object = MibTableColumn
sonetPathCurrentDaySESs = _SonetPathCurrentDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 4),
    _SonetPathCurrentDaySESs_Type()
)
sonetPathCurrentDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentDaySESs.setStatus("mandatory")
_SonetPathCurrentDayCVs_Type = Gauge32
_SonetPathCurrentDayCVs_Object = MibTableColumn
sonetPathCurrentDayCVs = _SonetPathCurrentDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 5),
    _SonetPathCurrentDayCVs_Type()
)
sonetPathCurrentDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentDayCVs.setStatus("mandatory")
_SonetPathCurrentDayFCs_Type = Gauge32
_SonetPathCurrentDayFCs_Object = MibTableColumn
sonetPathCurrentDayFCs = _SonetPathCurrentDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 6),
    _SonetPathCurrentDayFCs_Type()
)
sonetPathCurrentDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentDayFCs.setStatus("mandatory")
_SonetPathCurrentDayUASs_Type = Gauge32
_SonetPathCurrentDayUASs_Object = MibTableColumn
sonetPathCurrentDayUASs = _SonetPathCurrentDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 7),
    _SonetPathCurrentDayUASs_Type()
)
sonetPathCurrentDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCurrentDayUASs.setStatus("mandatory")


class _SonetPathCurrentDayClrButton_Type(Integer32):
    """Custom type sonetPathCurrentDayClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetPathCurrentDayClrButton_Type.__name__ = "Integer32"
_SonetPathCurrentDayClrButton_Object = MibTableColumn
sonetPathCurrentDayClrButton = _SonetPathCurrentDayClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 2, 1, 8),
    _SonetPathCurrentDayClrButton_Type()
)
sonetPathCurrentDayClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentDayClrButton.setStatus("mandatory")
_CwSonetPathIntervalTable_Object = MibTable
cwSonetPathIntervalTable = _CwSonetPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cwSonetPathIntervalTable.setStatus("mandatory")
_CwSonetPathIntervalEntry_Object = MibTableRow
cwSonetPathIntervalEntry = _CwSonetPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1)
)
cwSonetPathIntervalEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetPathIntervalLineNum"),
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    cwSonetPathIntervalEntry.setStatus("mandatory")


class _CwSonetPathIntervalLineNum_Type(Integer32):
    """Custom type cwSonetPathIntervalLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetPathIntervalLineNum_Type.__name__ = "Integer32"
_CwSonetPathIntervalLineNum_Object = MibTableColumn
cwSonetPathIntervalLineNum = _CwSonetPathIntervalLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 1),
    _CwSonetPathIntervalLineNum_Type()
)
cwSonetPathIntervalLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalLineNum.setStatus("mandatory")


class _CwSonetPathIntervalNumber_Type(Integer32):
    """Custom type cwSonetPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CwSonetPathIntervalNumber_Type.__name__ = "Integer32"
_CwSonetPathIntervalNumber_Object = MibTableColumn
cwSonetPathIntervalNumber = _CwSonetPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 2),
    _CwSonetPathIntervalNumber_Type()
)
cwSonetPathIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalNumber.setStatus("mandatory")


class _CwSonetPathIntervalValidFlag_Type(Integer32):
    """Custom type cwSonetPathIntervalValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetPathIntervalValidFlag_Type.__name__ = "Integer32"
_CwSonetPathIntervalValidFlag_Object = MibTableColumn
cwSonetPathIntervalValidFlag = _CwSonetPathIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 3),
    _CwSonetPathIntervalValidFlag_Type()
)
cwSonetPathIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalValidFlag.setStatus("mandatory")
_CwSonetPathIntervalESs_Type = Gauge32
_CwSonetPathIntervalESs_Object = MibTableColumn
cwSonetPathIntervalESs = _CwSonetPathIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 4),
    _CwSonetPathIntervalESs_Type()
)
cwSonetPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalESs.setStatus("mandatory")
_CwSonetPathIntervalSESs_Type = Gauge32
_CwSonetPathIntervalSESs_Object = MibTableColumn
cwSonetPathIntervalSESs = _CwSonetPathIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 5),
    _CwSonetPathIntervalSESs_Type()
)
cwSonetPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalSESs.setStatus("mandatory")
_CwSonetPathIntervalCVs_Type = Gauge32
_CwSonetPathIntervalCVs_Object = MibTableColumn
cwSonetPathIntervalCVs = _CwSonetPathIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 6),
    _CwSonetPathIntervalCVs_Type()
)
cwSonetPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalCVs.setStatus("mandatory")
_CwSonetPathIntervalFCs_Type = Gauge32
_CwSonetPathIntervalFCs_Object = MibTableColumn
cwSonetPathIntervalFCs = _CwSonetPathIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 7),
    _CwSonetPathIntervalFCs_Type()
)
cwSonetPathIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalFCs.setStatus("mandatory")
_CwSonetPathIntervalUASs_Type = Gauge32
_CwSonetPathIntervalUASs_Object = MibTableColumn
cwSonetPathIntervalUASs = _CwSonetPathIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 3, 1, 8),
    _CwSonetPathIntervalUASs_Type()
)
cwSonetPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetPathIntervalUASs.setStatus("mandatory")
_CwSonetFarEndPathCurrentTable_Object = MibTable
cwSonetFarEndPathCurrentTable = _CwSonetFarEndPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentTable.setStatus("mandatory")
_CwSonetFarEndPathCurrentEntry_Object = MibTableRow
cwSonetFarEndPathCurrentEntry = _CwSonetFarEndPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1)
)
cwSonetFarEndPathCurrentEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetFEPathCurrentLineNum"),
)
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentEntry.setStatus("mandatory")


class _CwSonetFEPathCurrentLineNum_Type(Integer32):
    """Custom type cwSonetFEPathCurrentLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetFEPathCurrentLineNum_Type.__name__ = "Integer32"
_CwSonetFEPathCurrentLineNum_Object = MibTableColumn
cwSonetFEPathCurrentLineNum = _CwSonetFEPathCurrentLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 1),
    _CwSonetFEPathCurrentLineNum_Type()
)
cwSonetFEPathCurrentLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFEPathCurrentLineNum.setStatus("mandatory")


class _CwSonetFarEndPathCurrentValidFlag_Type(Integer32):
    """Custom type cwSonetFarEndPathCurrentValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetFarEndPathCurrentValidFlag_Type.__name__ = "Integer32"
_CwSonetFarEndPathCurrentValidFlag_Object = MibTableColumn
cwSonetFarEndPathCurrentValidFlag = _CwSonetFarEndPathCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 2),
    _CwSonetFarEndPathCurrentValidFlag_Type()
)
cwSonetFarEndPathCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentValidFlag.setStatus("mandatory")


class _CwSonetFarEndPathCurrentTimeElapsed_Type(Integer32):
    """Custom type cwSonetFarEndPathCurrentTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CwSonetFarEndPathCurrentTimeElapsed_Type.__name__ = "Integer32"
_CwSonetFarEndPathCurrentTimeElapsed_Object = MibTableColumn
cwSonetFarEndPathCurrentTimeElapsed = _CwSonetFarEndPathCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 3),
    _CwSonetFarEndPathCurrentTimeElapsed_Type()
)
cwSonetFarEndPathCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentTimeElapsed.setStatus("mandatory")
_CwSonetFarEndPathCurrentESs_Type = Gauge32
_CwSonetFarEndPathCurrentESs_Object = MibTableColumn
cwSonetFarEndPathCurrentESs = _CwSonetFarEndPathCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 4),
    _CwSonetFarEndPathCurrentESs_Type()
)
cwSonetFarEndPathCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentESs.setStatus("mandatory")
_CwSonetFarEndPathCurrentSESs_Type = Gauge32
_CwSonetFarEndPathCurrentSESs_Object = MibTableColumn
cwSonetFarEndPathCurrentSESs = _CwSonetFarEndPathCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 5),
    _CwSonetFarEndPathCurrentSESs_Type()
)
cwSonetFarEndPathCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentSESs.setStatus("mandatory")
_CwSonetFarEndPathCurrentCVs_Type = Gauge32
_CwSonetFarEndPathCurrentCVs_Object = MibTableColumn
cwSonetFarEndPathCurrentCVs = _CwSonetFarEndPathCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 6),
    _CwSonetFarEndPathCurrentCVs_Type()
)
cwSonetFarEndPathCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentCVs.setStatus("mandatory")
_CwSonetFarEndPathCurrentFCs_Type = Gauge32
_CwSonetFarEndPathCurrentFCs_Object = MibTableColumn
cwSonetFarEndPathCurrentFCs = _CwSonetFarEndPathCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 7),
    _CwSonetFarEndPathCurrentFCs_Type()
)
cwSonetFarEndPathCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentFCs.setStatus("mandatory")
_CwSonetFarEndPathCurrentUASs_Type = Gauge32
_CwSonetFarEndPathCurrentUASs_Object = MibTableColumn
cwSonetFarEndPathCurrentUASs = _CwSonetFarEndPathCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 8),
    _CwSonetFarEndPathCurrentUASs_Type()
)
cwSonetFarEndPathCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentUASs.setStatus("mandatory")


class _CwSonetFarEndPathCurrentClrButton_Type(Integer32):
    """Custom type cwSonetFarEndPathCurrentClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_CwSonetFarEndPathCurrentClrButton_Type.__name__ = "Integer32"
_CwSonetFarEndPathCurrentClrButton_Object = MibTableColumn
cwSonetFarEndPathCurrentClrButton = _CwSonetFarEndPathCurrentClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 4, 1, 9),
    _CwSonetFarEndPathCurrentClrButton_Type()
)
cwSonetFarEndPathCurrentClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwSonetFarEndPathCurrentClrButton.setStatus("mandatory")
_SonetFarEndPathCurrentDayTable_Object = MibTable
sonetFarEndPathCurrentDayTable = _SonetFarEndPathCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5)
)
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayTable.setStatus("mandatory")
_SonetFarEndPathCurrentDayEntry_Object = MibTableRow
sonetFarEndPathCurrentDayEntry = _SonetFarEndPathCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1)
)
sonetFarEndPathCurrentDayEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetFEPathCurrentDayLineNum"),
)
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayEntry.setStatus("mandatory")


class _SonetFEPathCurrentDayLineNum_Type(Integer32):
    """Custom type sonetFEPathCurrentDayLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetFEPathCurrentDayLineNum_Type.__name__ = "Integer32"
_SonetFEPathCurrentDayLineNum_Object = MibTableColumn
sonetFEPathCurrentDayLineNum = _SonetFEPathCurrentDayLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 1),
    _SonetFEPathCurrentDayLineNum_Type()
)
sonetFEPathCurrentDayLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFEPathCurrentDayLineNum.setStatus("mandatory")


class _SonetFarEndPathCurrentDayValidFlag_Type(Integer32):
    """Custom type sonetFarEndPathCurrentDayValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_SonetFarEndPathCurrentDayValidFlag_Type.__name__ = "Integer32"
_SonetFarEndPathCurrentDayValidFlag_Object = MibTableColumn
sonetFarEndPathCurrentDayValidFlag = _SonetFarEndPathCurrentDayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 2),
    _SonetFarEndPathCurrentDayValidFlag_Type()
)
sonetFarEndPathCurrentDayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayValidFlag.setStatus("mandatory")
_SonetFarEndPathCurrentDayESs_Type = Gauge32
_SonetFarEndPathCurrentDayESs_Object = MibTableColumn
sonetFarEndPathCurrentDayESs = _SonetFarEndPathCurrentDayESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 3),
    _SonetFarEndPathCurrentDayESs_Type()
)
sonetFarEndPathCurrentDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayESs.setStatus("mandatory")
_SonetFarEndPathCurrentDaySESs_Type = Gauge32
_SonetFarEndPathCurrentDaySESs_Object = MibTableColumn
sonetFarEndPathCurrentDaySESs = _SonetFarEndPathCurrentDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 4),
    _SonetFarEndPathCurrentDaySESs_Type()
)
sonetFarEndPathCurrentDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDaySESs.setStatus("mandatory")
_SonetFarEndPathCurrentDayCVs_Type = Gauge32
_SonetFarEndPathCurrentDayCVs_Object = MibTableColumn
sonetFarEndPathCurrentDayCVs = _SonetFarEndPathCurrentDayCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 5),
    _SonetFarEndPathCurrentDayCVs_Type()
)
sonetFarEndPathCurrentDayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayCVs.setStatus("mandatory")
_SonetFarEndPathCurrentDayFCs_Type = Gauge32
_SonetFarEndPathCurrentDayFCs_Object = MibTableColumn
sonetFarEndPathCurrentDayFCs = _SonetFarEndPathCurrentDayFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 6),
    _SonetFarEndPathCurrentDayFCs_Type()
)
sonetFarEndPathCurrentDayFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayFCs.setStatus("mandatory")
_SonetFarEndPathCurrentDayUASs_Type = Gauge32
_SonetFarEndPathCurrentDayUASs_Object = MibTableColumn
sonetFarEndPathCurrentDayUASs = _SonetFarEndPathCurrentDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 7),
    _SonetFarEndPathCurrentDayUASs_Type()
)
sonetFarEndPathCurrentDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayUASs.setStatus("mandatory")


class _SonetFarEndPathCurrentDayClrButton_Type(Integer32):
    """Custom type sonetFarEndPathCurrentDayClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetFarEndPathCurrentDayClrButton_Type.__name__ = "Integer32"
_SonetFarEndPathCurrentDayClrButton_Object = MibTableColumn
sonetFarEndPathCurrentDayClrButton = _SonetFarEndPathCurrentDayClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 5, 1, 8),
    _SonetFarEndPathCurrentDayClrButton_Type()
)
sonetFarEndPathCurrentDayClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFarEndPathCurrentDayClrButton.setStatus("mandatory")
_CwSonetFarEndPathIntervalTable_Object = MibTable
cwSonetFarEndPathIntervalTable = _CwSonetFarEndPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6)
)
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalTable.setStatus("mandatory")
_CwSonetFarEndPathIntervalEntry_Object = MibTableRow
cwSonetFarEndPathIntervalEntry = _CwSonetFarEndPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1)
)
cwSonetFarEndPathIntervalEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetFEPathIntervalLineNum"),
    (0, "CISCO-MGX82XX-SONET-MIB", "cwSonetFarEndPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalEntry.setStatus("mandatory")


class _CwSonetFEPathIntervalLineNum_Type(Integer32):
    """Custom type cwSonetFEPathIntervalLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CwSonetFEPathIntervalLineNum_Type.__name__ = "Integer32"
_CwSonetFEPathIntervalLineNum_Object = MibTableColumn
cwSonetFEPathIntervalLineNum = _CwSonetFEPathIntervalLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 1),
    _CwSonetFEPathIntervalLineNum_Type()
)
cwSonetFEPathIntervalLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFEPathIntervalLineNum.setStatus("mandatory")


class _CwSonetFarEndPathIntervalNumber_Type(Integer32):
    """Custom type cwSonetFarEndPathIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CwSonetFarEndPathIntervalNumber_Type.__name__ = "Integer32"
_CwSonetFarEndPathIntervalNumber_Object = MibTableColumn
cwSonetFarEndPathIntervalNumber = _CwSonetFarEndPathIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 2),
    _CwSonetFarEndPathIntervalNumber_Type()
)
cwSonetFarEndPathIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalNumber.setStatus("mandatory")


class _CwSonetFarEndPathIntervalValidFlag_Type(Integer32):
    """Custom type cwSonetFarEndPathIntervalValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 1),
          ("valid", 2))
    )


_CwSonetFarEndPathIntervalValidFlag_Type.__name__ = "Integer32"
_CwSonetFarEndPathIntervalValidFlag_Object = MibTableColumn
cwSonetFarEndPathIntervalValidFlag = _CwSonetFarEndPathIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 3),
    _CwSonetFarEndPathIntervalValidFlag_Type()
)
cwSonetFarEndPathIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalValidFlag.setStatus("mandatory")
_CwSonetFarEndPathIntervalESs_Type = Gauge32
_CwSonetFarEndPathIntervalESs_Object = MibTableColumn
cwSonetFarEndPathIntervalESs = _CwSonetFarEndPathIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 4),
    _CwSonetFarEndPathIntervalESs_Type()
)
cwSonetFarEndPathIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalESs.setStatus("mandatory")
_CwSonetFarEndPathIntervalSESs_Type = Gauge32
_CwSonetFarEndPathIntervalSESs_Object = MibTableColumn
cwSonetFarEndPathIntervalSESs = _CwSonetFarEndPathIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 5),
    _CwSonetFarEndPathIntervalSESs_Type()
)
cwSonetFarEndPathIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalSESs.setStatus("mandatory")
_CwSonetFarEndPathIntervalCVs_Type = Gauge32
_CwSonetFarEndPathIntervalCVs_Object = MibTableColumn
cwSonetFarEndPathIntervalCVs = _CwSonetFarEndPathIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 6),
    _CwSonetFarEndPathIntervalCVs_Type()
)
cwSonetFarEndPathIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalCVs.setStatus("mandatory")
_CwSonetFarEndPathIntervalFCs_Type = Gauge32
_CwSonetFarEndPathIntervalFCs_Object = MibTableColumn
cwSonetFarEndPathIntervalFCs = _CwSonetFarEndPathIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 7),
    _CwSonetFarEndPathIntervalFCs_Type()
)
cwSonetFarEndPathIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalFCs.setStatus("mandatory")
_CwSonetFarEndPathIntervalUASs_Type = Gauge32
_CwSonetFarEndPathIntervalUASs_Object = MibTableColumn
cwSonetFarEndPathIntervalUASs = _CwSonetFarEndPathIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 6, 1, 8),
    _CwSonetFarEndPathIntervalUASs_Type()
)
cwSonetFarEndPathIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwSonetFarEndPathIntervalUASs.setStatus("mandatory")
_SonetPathAlarmTable_Object = MibTable
sonetPathAlarmTable = _SonetPathAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7)
)
if mibBuilder.loadTexts:
    sonetPathAlarmTable.setStatus("mandatory")
_SonetPathAlarmEntry_Object = MibTableRow
sonetPathAlarmEntry = _SonetPathAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1)
)
sonetPathAlarmEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetPathAlarmLineNum"),
)
if mibBuilder.loadTexts:
    sonetPathAlarmEntry.setStatus("mandatory")


class _SonetPathAlarmLineNum_Type(Integer32):
    """Custom type sonetPathAlarmLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetPathAlarmLineNum_Type.__name__ = "Integer32"
_SonetPathAlarmLineNum_Object = MibTableColumn
sonetPathAlarmLineNum = _SonetPathAlarmLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 1),
    _SonetPathAlarmLineNum_Type()
)
sonetPathAlarmLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathAlarmLineNum.setStatus("mandatory")


class _SonetPathStatisticalAlarmSeverity_Type(Integer32):
    """Custom type sonetPathStatisticalAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_SonetPathStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_SonetPathStatisticalAlarmSeverity_Object = MibTableColumn
sonetPathStatisticalAlarmSeverity = _SonetPathStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 2),
    _SonetPathStatisticalAlarmSeverity_Type()
)
sonetPathStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathStatisticalAlarmSeverity.setStatus("mandatory")


class _SonetPathCurrent15minESsThreshold_Type(Integer32):
    """Custom type sonetPathCurrent15minESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrent15minESsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrent15minESsThreshold_Object = MibTableColumn
sonetPathCurrent15minESsThreshold = _SonetPathCurrent15minESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 3),
    _SonetPathCurrent15minESsThreshold_Type()
)
sonetPathCurrent15minESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrent15minESsThreshold.setStatus("mandatory")


class _SonetPathCurrentDayESsThreshold_Type(Integer32):
    """Custom type sonetPathCurrentDayESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrentDayESsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentDayESsThreshold_Object = MibTableColumn
sonetPathCurrentDayESsThreshold = _SonetPathCurrentDayESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 4),
    _SonetPathCurrentDayESsThreshold_Type()
)
sonetPathCurrentDayESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentDayESsThreshold.setStatus("mandatory")


class _SonetPathCurrent15minSESsThreshold_Type(Integer32):
    """Custom type sonetPathCurrent15minSESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrent15minSESsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrent15minSESsThreshold_Object = MibTableColumn
sonetPathCurrent15minSESsThreshold = _SonetPathCurrent15minSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 5),
    _SonetPathCurrent15minSESsThreshold_Type()
)
sonetPathCurrent15minSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrent15minSESsThreshold.setStatus("mandatory")


class _SonetPathCurrentDaySESsThreshold_Type(Integer32):
    """Custom type sonetPathCurrentDaySESsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrentDaySESsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentDaySESsThreshold_Object = MibTableColumn
sonetPathCurrentDaySESsThreshold = _SonetPathCurrentDaySESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 6),
    _SonetPathCurrentDaySESsThreshold_Type()
)
sonetPathCurrentDaySESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentDaySESsThreshold.setStatus("mandatory")


class _SonetPathCurrent15minCVsThreshold_Type(Integer32):
    """Custom type sonetPathCurrent15minCVsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrent15minCVsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrent15minCVsThreshold_Object = MibTableColumn
sonetPathCurrent15minCVsThreshold = _SonetPathCurrent15minCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 7),
    _SonetPathCurrent15minCVsThreshold_Type()
)
sonetPathCurrent15minCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrent15minCVsThreshold.setStatus("mandatory")


class _SonetPathCurrentDayCVsThreshold_Type(Integer32):
    """Custom type sonetPathCurrentDayCVsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrentDayCVsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentDayCVsThreshold_Object = MibTableColumn
sonetPathCurrentDayCVsThreshold = _SonetPathCurrentDayCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 8),
    _SonetPathCurrentDayCVsThreshold_Type()
)
sonetPathCurrentDayCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentDayCVsThreshold.setStatus("mandatory")


class _SonetPathCurrent15minUASsThreshold_Type(Integer32):
    """Custom type sonetPathCurrent15minUASsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrent15minUASsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrent15minUASsThreshold_Object = MibTableColumn
sonetPathCurrent15minUASsThreshold = _SonetPathCurrent15minUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 9),
    _SonetPathCurrent15minUASsThreshold_Type()
)
sonetPathCurrent15minUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrent15minUASsThreshold.setStatus("mandatory")


class _SonetPathCurrentDayUASsThreshold_Type(Integer32):
    """Custom type sonetPathCurrentDayUASsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetPathCurrentDayUASsThreshold_Type.__name__ = "Integer32"
_SonetPathCurrentDayUASsThreshold_Object = MibTableColumn
sonetPathCurrentDayUASsThreshold = _SonetPathCurrentDayUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 10),
    _SonetPathCurrentDayUASsThreshold_Type()
)
sonetPathCurrentDayUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCurrentDayUASsThreshold.setStatus("mandatory")


class _SonetPathTraceSelection_Type(Integer32):
    """Custom type sonetPathTraceSelection based on Integer32"""
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
          ("sixteenBytes", 4),
          ("sixteenBytesCrc7", 5),
          ("sixteenBytesMsb1", 6),
          ("sixtyFourBytes", 2),
          ("sixtyFourBytesCrlf", 3))
    )


_SonetPathTraceSelection_Type.__name__ = "Integer32"
_SonetPathTraceSelection_Object = MibTableColumn
sonetPathTraceSelection = _SonetPathTraceSelection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 11),
    _SonetPathTraceSelection_Type()
)
sonetPathTraceSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathTraceSelection.setStatus("mandatory")


class _SonetPathTraceToTransmit_Type(OctetString):
    """Custom type sonetPathTraceToTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SonetPathTraceToTransmit_Type.__name__ = "OctetString"
_SonetPathTraceToTransmit_Object = MibTableColumn
sonetPathTraceToTransmit = _SonetPathTraceToTransmit_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 12),
    _SonetPathTraceToTransmit_Type()
)
sonetPathTraceToTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathTraceToTransmit.setStatus("mandatory")


class _SonetPathTraceToExpect_Type(OctetString):
    """Custom type sonetPathTraceToExpect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SonetPathTraceToExpect_Type.__name__ = "OctetString"
_SonetPathTraceToExpect_Object = MibTableColumn
sonetPathTraceToExpect = _SonetPathTraceToExpect_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 13),
    _SonetPathTraceToExpect_Type()
)
sonetPathTraceToExpect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathTraceToExpect.setStatus("mandatory")


class _SonetPathTraceReceived_Type(OctetString):
    """Custom type sonetPathTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SonetPathTraceReceived_Type.__name__ = "OctetString"
_SonetPathTraceReceived_Object = MibTableColumn
sonetPathTraceReceived = _SonetPathTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 14),
    _SonetPathTraceReceived_Type()
)
sonetPathTraceReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathTraceReceived.setStatus("mandatory")


class _SonetPathStatAlarmStatus_Type(Integer32):
    """Custom type sonetPathStatAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131071),
    )


_SonetPathStatAlarmStatus_Type.__name__ = "Integer32"
_SonetPathStatAlarmStatus_Object = MibTableColumn
sonetPathStatAlarmStatus = _SonetPathStatAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 7, 1, 15),
    _SonetPathStatAlarmStatus_Type()
)
sonetPathStatAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathStatAlarmStatus.setStatus("mandatory")
_SonetPathCounterTable_Object = MibTable
sonetPathCounterTable = _SonetPathCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 8)
)
if mibBuilder.loadTexts:
    sonetPathCounterTable.setStatus("mandatory")
_SonetPathCounterEntry_Object = MibTableRow
sonetPathCounterEntry = _SonetPathCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 8, 1)
)
sonetPathCounterEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "sonetPathCounterLineNum"),
)
if mibBuilder.loadTexts:
    sonetPathCounterEntry.setStatus("mandatory")


class _SonetPathCounterLineNum_Type(Integer32):
    """Custom type sonetPathCounterLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SonetPathCounterLineNum_Type.__name__ = "Integer32"
_SonetPathCounterLineNum_Object = MibTableColumn
sonetPathCounterLineNum = _SonetPathCounterLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 8, 1, 1),
    _SonetPathCounterLineNum_Type()
)
sonetPathCounterLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCounterLineNum.setStatus("mandatory")
_SonetPathCounterAISs_Type = Gauge32
_SonetPathCounterAISs_Object = MibTableColumn
sonetPathCounterAISs = _SonetPathCounterAISs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 8, 1, 2),
    _SonetPathCounterAISs_Type()
)
sonetPathCounterAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCounterAISs.setStatus("mandatory")
_SonetPathCounterRFIs_Type = Gauge32
_SonetPathCounterRFIs_Object = MibTableColumn
sonetPathCounterRFIs = _SonetPathCounterRFIs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 8, 1, 3),
    _SonetPathCounterRFIs_Type()
)
sonetPathCounterRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathCounterRFIs.setStatus("mandatory")


class _SonetPathCounterClrButton_Type(Integer32):
    """Custom type sonetPathCounterClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_SonetPathCounterClrButton_Type.__name__ = "Integer32"
_SonetPathCounterClrButton_Object = MibTableColumn
sonetPathCounterClrButton = _SonetPathCounterClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 5, 8, 1, 4),
    _SonetPathCounterClrButton_Type()
)
sonetPathCounterClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathCounterClrButton.setStatus("mandatory")
_SonetApsConfig_ObjectIdentity = ObjectIdentity
sonetApsConfig = _SonetApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6)
)
_SonetApsConfigTable_Object = MibTable
sonetApsConfigTable = _SonetApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sonetApsConfigTable.setStatus("mandatory")
_SonetApsConfigEntry_Object = MibTableRow
sonetApsConfigEntry = _SonetApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1)
)
sonetApsConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-SONET-MIB", "apsWorkingLine"),
)
if mibBuilder.loadTexts:
    sonetApsConfigEntry.setStatus("mandatory")


class _ApsWorkingSlot_Type(Integer32):
    """Custom type apsWorkingSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApsWorkingSlot_Type.__name__ = "Integer32"
_ApsWorkingSlot_Object = MibTableColumn
apsWorkingSlot = _ApsWorkingSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 1),
    _ApsWorkingSlot_Type()
)
apsWorkingSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsWorkingSlot.setStatus("mandatory")


class _ApsWorkingLine_Type(Integer32):
    """Custom type apsWorkingLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApsWorkingLine_Type.__name__ = "Integer32"
_ApsWorkingLine_Object = MibTableColumn
apsWorkingLine = _ApsWorkingLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 2),
    _ApsWorkingLine_Type()
)
apsWorkingLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsWorkingLine.setStatus("mandatory")


class _ApsProtectionSlot_Type(Integer32):
    """Custom type apsProtectionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApsProtectionSlot_Type.__name__ = "Integer32"
_ApsProtectionSlot_Object = MibTableColumn
apsProtectionSlot = _ApsProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 3),
    _ApsProtectionSlot_Type()
)
apsProtectionSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsProtectionSlot.setStatus("mandatory")


class _ApsProtectionLine_Type(Integer32):
    """Custom type apsProtectionLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApsProtectionLine_Type.__name__ = "Integer32"
_ApsProtectionLine_Object = MibTableColumn
apsProtectionLine = _ApsProtectionLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 4),
    _ApsProtectionLine_Type()
)
apsProtectionLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsProtectionLine.setStatus("mandatory")


class _ApsEnable_Type(Integer32):
    """Custom type apsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apsFeatDisable", 1),
          ("apsFeatEnable", 2))
    )


_ApsEnable_Type.__name__ = "Integer32"
_ApsEnable_Object = MibTableColumn
apsEnable = _ApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 5),
    _ApsEnable_Type()
)
apsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsEnable.setStatus("mandatory")


class _ApsArchMode_Type(Integer32):
    """Custom type apsArchMode based on Integer32"""
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
        *(("anexAOnePlusOne", 5),
          ("anexBOnePlusOne", 4),
          ("dualCardonePlusOne", 2),
          ("singleCardOneToOne", 3),
          ("singleCardonePlusOne", 1))
    )


_ApsArchMode_Type.__name__ = "Integer32"
_ApsArchMode_Object = MibTableColumn
apsArchMode = _ApsArchMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 6),
    _ApsArchMode_Type()
)
apsArchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsArchMode.setStatus("mandatory")


class _ApsActiveLine_Type(Integer32):
    """Custom type apsActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apsProtectionLine", 2),
          ("apsWorkingLine", 1))
    )


_ApsActiveLine_Type.__name__ = "Integer32"
_ApsActiveLine_Object = MibTableColumn
apsActiveLine = _ApsActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 7),
    _ApsActiveLine_Type()
)
apsActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsActiveLine.setStatus("mandatory")


class _ApsSFBER_Type(Integer32):
    """Custom type apsSFBER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 13),
    )


_ApsSFBER_Type.__name__ = "Integer32"
_ApsSFBER_Object = MibTableColumn
apsSFBER = _ApsSFBER_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 8),
    _ApsSFBER_Type()
)
apsSFBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsSFBER.setStatus("mandatory")


class _ApsSDBER_Type(Integer32):
    """Custom type apsSDBER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 13),
    )


_ApsSDBER_Type.__name__ = "Integer32"
_ApsSDBER_Object = MibTableColumn
apsSDBER = _ApsSDBER_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 9),
    _ApsSDBER_Type()
)
apsSDBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsSDBER.setStatus("mandatory")


class _ApsWtr_Type(Integer32):
    """Custom type apsWtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ApsWtr_Type.__name__ = "Integer32"
_ApsWtr_Object = MibTableColumn
apsWtr = _ApsWtr_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 10),
    _ApsWtr_Type()
)
apsWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsWtr.setStatus("mandatory")


class _Apsdirection_Type(Integer32):
    """Custom type apsdirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 1))
    )


_Apsdirection_Type.__name__ = "Integer32"
_Apsdirection_Object = MibTableColumn
apsdirection = _Apsdirection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 11),
    _Apsdirection_Type()
)
apsdirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsdirection.setStatus("mandatory")


class _ApsRevertive_Type(Integer32):
    """Custom type apsRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_ApsRevertive_Type.__name__ = "Integer32"
_ApsRevertive_Object = MibTableColumn
apsRevertive = _ApsRevertive_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 12),
    _ApsRevertive_Type()
)
apsRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsRevertive.setStatus("mandatory")


class _ApsK1K2Disable_Type(Integer32):
    """Custom type apsK1K2Disable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbandDisable", 2),
          ("kbandEnable", 1))
    )


_ApsK1K2Disable_Type.__name__ = "Integer32"
_ApsK1K2Disable_Object = MibTableColumn
apsK1K2Disable = _ApsK1K2Disable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 1, 1, 13),
    _ApsK1K2Disable_Type()
)
apsK1K2Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsK1K2Disable.setStatus("mandatory")


class _ApsCardFailureCode_Type(Integer32):
    """Custom type apsCardFailureCode based on Integer32"""
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
        *(("apsProtectBCMissing", 1),
          ("apsProtectCdMismatch", 6),
          ("apsProtectDCMissing", 2),
          ("apsWorkingBCMissing", 3),
          ("apsWorkingCdMismatch", 5),
          ("apsWorkingDCMissing", 4))
    )


_ApsCardFailureCode_Type.__name__ = "Integer32"
_ApsCardFailureCode_Object = MibScalar
apsCardFailureCode = _ApsCardFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 2),
    _ApsCardFailureCode_Type()
)
apsCardFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsCardFailureCode.setStatus("mandatory")


class _ApsLineFailureCode_Type(Integer32):
    """Custom type apsLineFailureCode based on Integer32"""
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
        *(("apsLineAlarm", 3),
          ("apsLineLoopBack", 4),
          ("apsSignalDegrade", 1),
          ("apsSignalFailure", 2))
    )


_ApsLineFailureCode_Type.__name__ = "Integer32"
_ApsLineFailureCode_Object = MibScalar
apsLineFailureCode = _ApsLineFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 3),
    _ApsLineFailureCode_Type()
)
apsLineFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsLineFailureCode.setStatus("mandatory")


class _ApsLineSwReason_Type(Integer32):
    """Custom type apsLineSwReason based on Integer32"""
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
        *(("apsForceSwitch", 7),
          ("apsLockOut", 8),
          ("apsManual", 2),
          ("apsRevertive", 1),
          ("apsSignalDefectHigh", 4),
          ("apsSignalDefectLow", 3),
          ("apsSignalFailureHigh", 6),
          ("apsSignalFailureLow", 5))
    )


_ApsLineSwReason_Type.__name__ = "Integer32"
_ApsLineSwReason_Object = MibScalar
apsLineSwReason = _ApsLineSwReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 4),
    _ApsLineSwReason_Type()
)
apsLineSwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsLineSwReason.setStatus("mandatory")


class _ApsLineSwFailureCode_Type(Integer32):
    """Custom type apsLineSwFailureCode based on Integer32"""
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
        *(("apsForceSwitchFail", 7),
          ("apsLockOutSwitchFail", 8),
          ("apsManualSwitchFail", 2),
          ("apsRevertiveSwitchFail", 1),
          ("apsSDHighSwitchFail", 4),
          ("apsSDLowSwitchFail", 3),
          ("apsSFHighSwitchFail", 6),
          ("apsSFLowSwitchFail", 5))
    )


_ApsLineSwFailureCode_Type.__name__ = "Integer32"
_ApsLineSwFailureCode_Object = MibScalar
apsLineSwFailureCode = _ApsLineSwFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 5),
    _ApsLineSwFailureCode_Type()
)
apsLineSwFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsLineSwFailureCode.setStatus("mandatory")


class _ApsStandbyLineFailureCode_Type(Integer32):
    """Custom type apsStandbyLineFailureCode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("apsArchitectureMismatch", 6),
          ("apsChannelMismatch", 7),
          ("apsDirectionMismatch", 8),
          ("apsLineAlarm", 3),
          ("apsLineLoopBack", 4),
          ("apsProtectionByteFail", 5),
          ("apsSignalDegrade", 1),
          ("apsSignalFailure", 2),
          ("apsWrongRequest", 9))
    )


_ApsStandbyLineFailureCode_Type.__name__ = "Integer32"
_ApsStandbyLineFailureCode_Object = MibScalar
apsStandbyLineFailureCode = _ApsStandbyLineFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1, 6, 6),
    _ApsStandbyLineFailureCode_Type()
)
apsStandbyLineFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStandbyLineFailureCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-SONET-MIB",
    **{"sonetConfig": sonetConfig,
       "sonetConfigTable": sonetConfigTable,
       "sonetConfigEntry": sonetConfigEntry,
       "sonetLineNum": sonetLineNum,
       "sonetLineType": sonetLineType,
       "sonetLineLoopbackCommand": sonetLineLoopbackCommand,
       "sonetHCSmasking": sonetHCSmasking,
       "sonetPayloadScrambling": sonetPayloadScrambling,
       "sonetFrameScrambling": sonetFrameScrambling,
       "sonetLineEnable": sonetLineEnable,
       "sonetLineXmtClkSrc": sonetLineXmtClkSrc,
       "sonetRDIVType": sonetRDIVType,
       "sonetRDIPType": sonetRDIPType,
       "sonetTributaryType": sonetTributaryType,
       "sonetTributaryMappingType": sonetTributaryMappingType,
       "sonetTributaryFramingFormat": sonetTributaryFramingFormat,
       "sonetSignallingTransportMode": sonetSignallingTransportMode,
       "sonetTributaryGroupingType": sonetTributaryGroupingType,
       "sonetConfigNumOfValidEntries": sonetConfigNumOfValidEntries,
       "cwsonetMedium": cwsonetMedium,
       "cwSonetMediumTable": cwSonetMediumTable,
       "cwSonetMediumEntry": cwSonetMediumEntry,
       "cwSonetMediumType": cwSonetMediumType,
       "cwSonetMediumTimeElapsed": cwSonetMediumTimeElapsed,
       "cwSonetMediumValidIntervals": cwSonetMediumValidIntervals,
       "cwSonetMediumLineCoding": cwSonetMediumLineCoding,
       "cwSonetMediumLineType": cwSonetMediumLineType,
       "cwSonetMediumCircuitIdentifier": cwSonetMediumCircuitIdentifier,
       "cwsonetSection": cwsonetSection,
       "cwSonetSectionCurrentTable": cwSonetSectionCurrentTable,
       "cwSonetSectionCurrentEntry": cwSonetSectionCurrentEntry,
       "cwSonetSectionCurrentLineNum": cwSonetSectionCurrentLineNum,
       "cwSonetSectionCurrentStatus": cwSonetSectionCurrentStatus,
       "cwSonetSectionCurrentValidFlag": cwSonetSectionCurrentValidFlag,
       "cwSonetSectionCurrent15minTimeElapsed": cwSonetSectionCurrent15minTimeElapsed,
       "cwSonetSectionCurrentESs": cwSonetSectionCurrentESs,
       "cwSonetSectionCurrentSESs": cwSonetSectionCurrentSESs,
       "cwSonetSectionCurrentSEFSs": cwSonetSectionCurrentSEFSs,
       "cwSonetSectionCurrentCVs": cwSonetSectionCurrentCVs,
       "cwSonetSectionCurrentClrButton": cwSonetSectionCurrentClrButton,
       "sonetSectionCurrentDayTable": sonetSectionCurrentDayTable,
       "sonetSectionCurrentDayEntry": sonetSectionCurrentDayEntry,
       "sonetSectionCurrentDayLineNum": sonetSectionCurrentDayLineNum,
       "sonetSectionCurrentDayValidFlag": sonetSectionCurrentDayValidFlag,
       "sonetSectionCurrentDayESs": sonetSectionCurrentDayESs,
       "sonetSectionCurrentDaySESs": sonetSectionCurrentDaySESs,
       "sonetSectionCurrentDaySEFSs": sonetSectionCurrentDaySEFSs,
       "sonetSectionCurrentDayCVs": sonetSectionCurrentDayCVs,
       "sonetSectionCurrentDayClrButton": sonetSectionCurrentDayClrButton,
       "cwSonetSectionIntervalTable": cwSonetSectionIntervalTable,
       "cwSonetSectionIntervalEntry": cwSonetSectionIntervalEntry,
       "cwSonetSectionIntervalLineNum": cwSonetSectionIntervalLineNum,
       "cwSonetSectionIntervalNumber": cwSonetSectionIntervalNumber,
       "cwSonetSectionIntervalValidFlag": cwSonetSectionIntervalValidFlag,
       "cwSonetSectionIntervalESs": cwSonetSectionIntervalESs,
       "cwSonetSectionIntervalSESs": cwSonetSectionIntervalSESs,
       "cwSonetSectionIntervalSEFss": cwSonetSectionIntervalSEFss,
       "cwSonetSectionIntervalCVs": cwSonetSectionIntervalCVs,
       "sonetSectionAlarmTable": sonetSectionAlarmTable,
       "sonetSectionAlarmEntry": sonetSectionAlarmEntry,
       "sectionAlarmLineNum": sectionAlarmLineNum,
       "sonetSectionStatisticalAlarmSeverity": sonetSectionStatisticalAlarmSeverity,
       "sonetSectionCurrent15minESsThreshold": sonetSectionCurrent15minESsThreshold,
       "sonetSectionCurrentDayESsThreshold": sonetSectionCurrentDayESsThreshold,
       "sonetSectionCurrent15minSESsThreshold": sonetSectionCurrent15minSESsThreshold,
       "sonetSectionCurrentDaySESsThreshold": sonetSectionCurrentDaySESsThreshold,
       "sonetSectionCurrent15minSEFSsThreshold": sonetSectionCurrent15minSEFSsThreshold,
       "sonetSectionCurrentDaySEFSsThreshold": sonetSectionCurrentDaySEFSsThreshold,
       "sonetSectionCurrent15minCVsThreshold": sonetSectionCurrent15minCVsThreshold,
       "sonetSectionCurrentDayCVsThreshold": sonetSectionCurrentDayCVsThreshold,
       "sonetSectionTraceSelection": sonetSectionTraceSelection,
       "sonetSectionTraceToTransmit": sonetSectionTraceToTransmit,
       "sonetSectionTraceToExpect": sonetSectionTraceToExpect,
       "sonetSectionTraceReceived": sonetSectionTraceReceived,
       "sonetSectionStatAlarmStatus": sonetSectionStatAlarmStatus,
       "sonetSectionCounterTable": sonetSectionCounterTable,
       "sonetSectionCounterEntry": sonetSectionCounterEntry,
       "sectionCounterLineNum": sectionCounterLineNum,
       "sonetSectionCounterLOSs": sonetSectionCounterLOSs,
       "sonetSectionCounterLOFs": sonetSectionCounterLOFs,
       "sonetSectionCounterClrButton": sonetSectionCounterClrButton,
       "cwsonetLine": cwsonetLine,
       "cwSonetLineCurrentTable": cwSonetLineCurrentTable,
       "cwSonetLineCurrentEntry": cwSonetLineCurrentEntry,
       "cwSonetLineCurrentLineNum": cwSonetLineCurrentLineNum,
       "cwSonetLineCurrentStatus": cwSonetLineCurrentStatus,
       "cwSonetLineCurrentValidFlag": cwSonetLineCurrentValidFlag,
       "cwSonetLineCurrent15minTimeElapsed": cwSonetLineCurrent15minTimeElapsed,
       "cwSonetLineCurrentESs": cwSonetLineCurrentESs,
       "cwSonetLineCurrentSESs": cwSonetLineCurrentSESs,
       "cwSonetLineCurrentCVs": cwSonetLineCurrentCVs,
       "cwSonetLineCurrentUASs": cwSonetLineCurrentUASs,
       "cwSonetLineCurrentClrButton": cwSonetLineCurrentClrButton,
       "sonetLineCurrentDayTable": sonetLineCurrentDayTable,
       "sonetLineCurrentDayEntry": sonetLineCurrentDayEntry,
       "lineCurrentDayLineNum": lineCurrentDayLineNum,
       "sonetLineCurrentDayValidFlag": sonetLineCurrentDayValidFlag,
       "sonetLineCurrentDayESs": sonetLineCurrentDayESs,
       "sonetLineCurrentDaySESs": sonetLineCurrentDaySESs,
       "sonetLineCurrentDayCVs": sonetLineCurrentDayCVs,
       "sonetLineCurrentDayFCs": sonetLineCurrentDayFCs,
       "sonetLineCurrentDayUASs": sonetLineCurrentDayUASs,
       "sonetLineCurrentDayClrButton": sonetLineCurrentDayClrButton,
       "cwSonetLineIntervalTable": cwSonetLineIntervalTable,
       "cwSonetLineIntervalEntry": cwSonetLineIntervalEntry,
       "cwSonetLineIntervalLineNum": cwSonetLineIntervalLineNum,
       "cwSonetLineIntervalNumber": cwSonetLineIntervalNumber,
       "cwSonetLineIntervalValidFlag": cwSonetLineIntervalValidFlag,
       "cwSonetLineIntervalESs": cwSonetLineIntervalESs,
       "cwSonetLineIntervalSESs": cwSonetLineIntervalSESs,
       "cwSonetLineIntervalCVs": cwSonetLineIntervalCVs,
       "cwSonetLineIntervalFCs": cwSonetLineIntervalFCs,
       "cwSonetLineIntervalUASs": cwSonetLineIntervalUASs,
       "cwSonetFarEndLineCurrentTable": cwSonetFarEndLineCurrentTable,
       "cwSonetFarEndLineCurrentEntry": cwSonetFarEndLineCurrentEntry,
       "cwSonetFELineCurrentLineNum": cwSonetFELineCurrentLineNum,
       "cwSonetFarEndLineCurrentValidFlag": cwSonetFarEndLineCurrentValidFlag,
       "cwSonetFarEndLineCurrentTimeElapsed": cwSonetFarEndLineCurrentTimeElapsed,
       "cwSonetFarEndLineCurrentESs": cwSonetFarEndLineCurrentESs,
       "cwSonetFarEndLineCurrentSESs": cwSonetFarEndLineCurrentSESs,
       "cwSonetFarEndLineCurrentCVs": cwSonetFarEndLineCurrentCVs,
       "cwSonetFarEndLineCurrentFCs": cwSonetFarEndLineCurrentFCs,
       "cwSonetFarEndLineCurrentUASs": cwSonetFarEndLineCurrentUASs,
       "cwSonetFarEndLineCurrentClrButton": cwSonetFarEndLineCurrentClrButton,
       "sonetFarEndLineCurrentDayTable": sonetFarEndLineCurrentDayTable,
       "sonetFarEndLineCurrentDayEntry": sonetFarEndLineCurrentDayEntry,
       "sonetFELineCurrentDayLineNum": sonetFELineCurrentDayLineNum,
       "sonetFarEndLineCurrentDayValidFlag": sonetFarEndLineCurrentDayValidFlag,
       "sonetFarEndLineCurrentDayESs": sonetFarEndLineCurrentDayESs,
       "sonetFarEndLineCurrentDaySESs": sonetFarEndLineCurrentDaySESs,
       "sonetFarEndLineCurrentDayCVs": sonetFarEndLineCurrentDayCVs,
       "sonetFarEndLineCurrentDayFCs": sonetFarEndLineCurrentDayFCs,
       "sonetFarEndLineCurrentDayUASs": sonetFarEndLineCurrentDayUASs,
       "sonetFarEndLineCurrentDayClrButton": sonetFarEndLineCurrentDayClrButton,
       "cwSonetFarEndLineIntervalTable": cwSonetFarEndLineIntervalTable,
       "cwSonetFarEndLineIntervalEntry": cwSonetFarEndLineIntervalEntry,
       "cwSonetFELineIntervalLineNum": cwSonetFELineIntervalLineNum,
       "cwSonetFarEndLineIntervalNumber": cwSonetFarEndLineIntervalNumber,
       "cwSonetFarEndLineIntervalValidFlag": cwSonetFarEndLineIntervalValidFlag,
       "cwSonetFarEndLineIntervalESs": cwSonetFarEndLineIntervalESs,
       "cwSonetFarEndLineIntervalSESs": cwSonetFarEndLineIntervalSESs,
       "cwSonetFarEndLineIntervalCVs": cwSonetFarEndLineIntervalCVs,
       "cwSonetFarEndLineIntervalFCs": cwSonetFarEndLineIntervalFCs,
       "cwSonetFarEndLineIntervalUASs": cwSonetFarEndLineIntervalUASs,
       "sonetLineAlarmTable": sonetLineAlarmTable,
       "sonetLineAlarmEntry": sonetLineAlarmEntry,
       "sonetLineAlarmLineNum": sonetLineAlarmLineNum,
       "sonetLineStatisticalAlarmSeverity": sonetLineStatisticalAlarmSeverity,
       "sonetLineCurrent15minESsThreshold": sonetLineCurrent15minESsThreshold,
       "sonetLineCurrentDayESsThreshold": sonetLineCurrentDayESsThreshold,
       "sonetLineCurrent15minSESsThreshold": sonetLineCurrent15minSESsThreshold,
       "sonetLineCurrentDaySESsThreshold": sonetLineCurrentDaySESsThreshold,
       "sonetLineCurrent15minCVsThreshold": sonetLineCurrent15minCVsThreshold,
       "sonetLineCurrentDayCVsThreshold": sonetLineCurrentDayCVsThreshold,
       "sonetLineCurrent15minUASsThreshold": sonetLineCurrent15minUASsThreshold,
       "sonetLineCurrentDayUASsThreshold": sonetLineCurrentDayUASsThreshold,
       "sonetLineStatAlarmStatus": sonetLineStatAlarmStatus,
       "sonetLineCounterTable": sonetLineCounterTable,
       "sonetLineCounterEntry": sonetLineCounterEntry,
       "sonetLineCounterLineNum": sonetLineCounterLineNum,
       "sonetLineCounterAISs": sonetLineCounterAISs,
       "sonetLineCounterRFIs": sonetLineCounterRFIs,
       "sonetLineCounterClrButton": sonetLineCounterClrButton,
       "cwsonetPath": cwsonetPath,
       "cwSonetPathCurrentTable": cwSonetPathCurrentTable,
       "cwSonetPathCurrentEntry": cwSonetPathCurrentEntry,
       "cwSonetPathCurrentLineNum": cwSonetPathCurrentLineNum,
       "cwSonetPathCurrentStatus": cwSonetPathCurrentStatus,
       "cwSonetPathCurrentValidFlag": cwSonetPathCurrentValidFlag,
       "cwSonetPathCurrentTimeElapsed": cwSonetPathCurrentTimeElapsed,
       "cwSonetPathCurrentESs": cwSonetPathCurrentESs,
       "cwSonetPathCurrentSESs": cwSonetPathCurrentSESs,
       "cwSonetPathCurrentCVs": cwSonetPathCurrentCVs,
       "cwSonetPathCurrentFCs": cwSonetPathCurrentFCs,
       "cwSonetPathCurrentUASs": cwSonetPathCurrentUASs,
       "cwSonetPathCurrentClrButton": cwSonetPathCurrentClrButton,
       "sonetPathCurrentDayTable": sonetPathCurrentDayTable,
       "sonetPathCurrentDayEntry": sonetPathCurrentDayEntry,
       "sonetPathCurrentDayLineNum": sonetPathCurrentDayLineNum,
       "sonetPathCurrentDayValidFlag": sonetPathCurrentDayValidFlag,
       "sonetPathCurrentDayESs": sonetPathCurrentDayESs,
       "sonetPathCurrentDaySESs": sonetPathCurrentDaySESs,
       "sonetPathCurrentDayCVs": sonetPathCurrentDayCVs,
       "sonetPathCurrentDayFCs": sonetPathCurrentDayFCs,
       "sonetPathCurrentDayUASs": sonetPathCurrentDayUASs,
       "sonetPathCurrentDayClrButton": sonetPathCurrentDayClrButton,
       "cwSonetPathIntervalTable": cwSonetPathIntervalTable,
       "cwSonetPathIntervalEntry": cwSonetPathIntervalEntry,
       "cwSonetPathIntervalLineNum": cwSonetPathIntervalLineNum,
       "cwSonetPathIntervalNumber": cwSonetPathIntervalNumber,
       "cwSonetPathIntervalValidFlag": cwSonetPathIntervalValidFlag,
       "cwSonetPathIntervalESs": cwSonetPathIntervalESs,
       "cwSonetPathIntervalSESs": cwSonetPathIntervalSESs,
       "cwSonetPathIntervalCVs": cwSonetPathIntervalCVs,
       "cwSonetPathIntervalFCs": cwSonetPathIntervalFCs,
       "cwSonetPathIntervalUASs": cwSonetPathIntervalUASs,
       "cwSonetFarEndPathCurrentTable": cwSonetFarEndPathCurrentTable,
       "cwSonetFarEndPathCurrentEntry": cwSonetFarEndPathCurrentEntry,
       "cwSonetFEPathCurrentLineNum": cwSonetFEPathCurrentLineNum,
       "cwSonetFarEndPathCurrentValidFlag": cwSonetFarEndPathCurrentValidFlag,
       "cwSonetFarEndPathCurrentTimeElapsed": cwSonetFarEndPathCurrentTimeElapsed,
       "cwSonetFarEndPathCurrentESs": cwSonetFarEndPathCurrentESs,
       "cwSonetFarEndPathCurrentSESs": cwSonetFarEndPathCurrentSESs,
       "cwSonetFarEndPathCurrentCVs": cwSonetFarEndPathCurrentCVs,
       "cwSonetFarEndPathCurrentFCs": cwSonetFarEndPathCurrentFCs,
       "cwSonetFarEndPathCurrentUASs": cwSonetFarEndPathCurrentUASs,
       "cwSonetFarEndPathCurrentClrButton": cwSonetFarEndPathCurrentClrButton,
       "sonetFarEndPathCurrentDayTable": sonetFarEndPathCurrentDayTable,
       "sonetFarEndPathCurrentDayEntry": sonetFarEndPathCurrentDayEntry,
       "sonetFEPathCurrentDayLineNum": sonetFEPathCurrentDayLineNum,
       "sonetFarEndPathCurrentDayValidFlag": sonetFarEndPathCurrentDayValidFlag,
       "sonetFarEndPathCurrentDayESs": sonetFarEndPathCurrentDayESs,
       "sonetFarEndPathCurrentDaySESs": sonetFarEndPathCurrentDaySESs,
       "sonetFarEndPathCurrentDayCVs": sonetFarEndPathCurrentDayCVs,
       "sonetFarEndPathCurrentDayFCs": sonetFarEndPathCurrentDayFCs,
       "sonetFarEndPathCurrentDayUASs": sonetFarEndPathCurrentDayUASs,
       "sonetFarEndPathCurrentDayClrButton": sonetFarEndPathCurrentDayClrButton,
       "cwSonetFarEndPathIntervalTable": cwSonetFarEndPathIntervalTable,
       "cwSonetFarEndPathIntervalEntry": cwSonetFarEndPathIntervalEntry,
       "cwSonetFEPathIntervalLineNum": cwSonetFEPathIntervalLineNum,
       "cwSonetFarEndPathIntervalNumber": cwSonetFarEndPathIntervalNumber,
       "cwSonetFarEndPathIntervalValidFlag": cwSonetFarEndPathIntervalValidFlag,
       "cwSonetFarEndPathIntervalESs": cwSonetFarEndPathIntervalESs,
       "cwSonetFarEndPathIntervalSESs": cwSonetFarEndPathIntervalSESs,
       "cwSonetFarEndPathIntervalCVs": cwSonetFarEndPathIntervalCVs,
       "cwSonetFarEndPathIntervalFCs": cwSonetFarEndPathIntervalFCs,
       "cwSonetFarEndPathIntervalUASs": cwSonetFarEndPathIntervalUASs,
       "sonetPathAlarmTable": sonetPathAlarmTable,
       "sonetPathAlarmEntry": sonetPathAlarmEntry,
       "sonetPathAlarmLineNum": sonetPathAlarmLineNum,
       "sonetPathStatisticalAlarmSeverity": sonetPathStatisticalAlarmSeverity,
       "sonetPathCurrent15minESsThreshold": sonetPathCurrent15minESsThreshold,
       "sonetPathCurrentDayESsThreshold": sonetPathCurrentDayESsThreshold,
       "sonetPathCurrent15minSESsThreshold": sonetPathCurrent15minSESsThreshold,
       "sonetPathCurrentDaySESsThreshold": sonetPathCurrentDaySESsThreshold,
       "sonetPathCurrent15minCVsThreshold": sonetPathCurrent15minCVsThreshold,
       "sonetPathCurrentDayCVsThreshold": sonetPathCurrentDayCVsThreshold,
       "sonetPathCurrent15minUASsThreshold": sonetPathCurrent15minUASsThreshold,
       "sonetPathCurrentDayUASsThreshold": sonetPathCurrentDayUASsThreshold,
       "sonetPathTraceSelection": sonetPathTraceSelection,
       "sonetPathTraceToTransmit": sonetPathTraceToTransmit,
       "sonetPathTraceToExpect": sonetPathTraceToExpect,
       "sonetPathTraceReceived": sonetPathTraceReceived,
       "sonetPathStatAlarmStatus": sonetPathStatAlarmStatus,
       "sonetPathCounterTable": sonetPathCounterTable,
       "sonetPathCounterEntry": sonetPathCounterEntry,
       "sonetPathCounterLineNum": sonetPathCounterLineNum,
       "sonetPathCounterAISs": sonetPathCounterAISs,
       "sonetPathCounterRFIs": sonetPathCounterRFIs,
       "sonetPathCounterClrButton": sonetPathCounterClrButton,
       "sonetApsConfig": sonetApsConfig,
       "sonetApsConfigTable": sonetApsConfigTable,
       "sonetApsConfigEntry": sonetApsConfigEntry,
       "apsWorkingSlot": apsWorkingSlot,
       "apsWorkingLine": apsWorkingLine,
       "apsProtectionSlot": apsProtectionSlot,
       "apsProtectionLine": apsProtectionLine,
       "apsEnable": apsEnable,
       "apsArchMode": apsArchMode,
       "apsActiveLine": apsActiveLine,
       "apsSFBER": apsSFBER,
       "apsSDBER": apsSDBER,
       "apsWtr": apsWtr,
       "apsdirection": apsdirection,
       "apsRevertive": apsRevertive,
       "apsK1K2Disable": apsK1K2Disable,
       "apsCardFailureCode": apsCardFailureCode,
       "apsLineFailureCode": apsLineFailureCode,
       "apsLineSwReason": apsLineSwReason,
       "apsLineSwFailureCode": apsLineSwFailureCode,
       "apsStandbyLineFailureCode": apsStandbyLineFailureCode}
)
