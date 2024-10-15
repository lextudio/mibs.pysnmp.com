# SNMP MIB module (INNOVX-CASCADE-LIU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INNOVX-CASCADE-LIU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:26 2024
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

(casGroup,) = mibBuilder.importSymbols(
    "INNOVX-CORE-MIB",
    "casGroup")

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

_AdminGroup_ObjectIdentity = ObjectIdentity
adminGroup = _AdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 1)
)


class _CascadeMIBversion_Type(DisplayString):
    """Custom type cascadeMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_CascadeMIBversion_Type.__name__ = "DisplayString"
_CascadeMIBversion_Object = MibScalar
cascadeMIBversion = _CascadeMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 1, 1),
    _CascadeMIBversion_Type()
)
cascadeMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cascadeMIBversion.setStatus("mandatory")
_ConfigGroup_ObjectIdentity = ObjectIdentity
configGroup = _ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2)
)


class _CascadeInService_Type(Integer32):
    """Custom type cascadeInService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_CascadeInService_Type.__name__ = "Integer32"
_CascadeInService_Object = MibScalar
cascadeInService = _CascadeInService_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 1),
    _CascadeInService_Type()
)
cascadeInService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeInService.setStatus("mandatory")


class _CascadeSetFrameType_Type(Integer32):
    """Custom type cascadeSetFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("d4", 2),
          ("esf", 1))
    )


_CascadeSetFrameType_Type.__name__ = "Integer32"
_CascadeSetFrameType_Object = MibScalar
cascadeSetFrameType = _CascadeSetFrameType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 2),
    _CascadeSetFrameType_Type()
)
cascadeSetFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeSetFrameType.setStatus("mandatory")


class _CascadeOperFrameType_Type(Integer32):
    """Custom type cascadeOperFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("d4", 2),
          ("esf", 1))
    )


_CascadeOperFrameType_Type.__name__ = "Integer32"
_CascadeOperFrameType_Object = MibScalar
cascadeOperFrameType = _CascadeOperFrameType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 3),
    _CascadeOperFrameType_Type()
)
cascadeOperFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cascadeOperFrameType.setStatus("mandatory")


class _CascadeLineCoding_Type(Integer32):
    """Custom type cascadeLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )


_CascadeLineCoding_Type.__name__ = "Integer32"
_CascadeLineCoding_Object = MibScalar
cascadeLineCoding = _CascadeLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 4),
    _CascadeLineCoding_Type()
)
cascadeLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeLineCoding.setStatus("mandatory")


class _CascadeIntfType_Type(Integer32):
    """Custom type cascadeIntfType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ds1-auto-lbo", 1),
          ("ds1-neg15pt0-dB", 4),
          ("ds1-neg22pt5-dB", 5),
          ("ds1-neg7pt5-dB", 3),
          ("ds1-zero-dB", 2),
          ("dsx1-preeq130-ft", 6),
          ("dsx1-preeq260-ft", 7),
          ("dsx1-preeq390-ft", 8),
          ("dsx1-preeq530-ft", 9),
          ("dsx1-preeq655-ft", 10))
    )


_CascadeIntfType_Type.__name__ = "Integer32"
_CascadeIntfType_Object = MibScalar
cascadeIntfType = _CascadeIntfType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 5),
    _CascadeIntfType_Type()
)
cascadeIntfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeIntfType.setStatus("mandatory")


class _CascadeDS1IntfRcvLevel_Type(Integer32):
    """Custom type cascadeDS1IntfRcvLevel based on Integer32"""
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
        *(("invalidDSX1intf", 6),
          ("lessThanNeg22pt5-dB", 5),
          ("neg15toNeg22pt5-dB", 4),
          ("neg7pt5toNeg15-dB", 3),
          ("noSignal", 1),
          ("pos2toNeg7pt5-dB", 2))
    )


_CascadeDS1IntfRcvLevel_Type.__name__ = "Integer32"
_CascadeDS1IntfRcvLevel_Object = MibScalar
cascadeDS1IntfRcvLevel = _CascadeDS1IntfRcvLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 6),
    _CascadeDS1IntfRcvLevel_Type()
)
cascadeDS1IntfRcvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cascadeDS1IntfRcvLevel.setStatus("mandatory")
_CascadeDropAndInsertTable_Object = MibTable
cascadeDropAndInsertTable = _CascadeDropAndInsertTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7)
)
if mibBuilder.loadTexts:
    cascadeDropAndInsertTable.setStatus("mandatory")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1)
)
channelEntry.setIndexNames(
    (0, "INNOVX-CASCADE-LIU-MIB", "channelIndex"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("mandatory")


class _ChannelIndex_Type(Integer32):
    """Custom type channelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChannelIndex_Type.__name__ = "Integer32"
_ChannelIndex_Object = MibTableColumn
channelIndex = _ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1, 1),
    _ChannelIndex_Type()
)
channelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelIndex.setStatus("mandatory")


class _CascadeDropAndInsert_Type(Integer32):
    """Custom type cascadeDropAndInsert based on Integer32"""
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
        *(("casChannel", 4),
          ("clearChannel", 2),
          ("none", 1),
          ("signallingChannel", 3),
          ("tsNotAvailable", 5))
    )


_CascadeDropAndInsert_Type.__name__ = "Integer32"
_CascadeDropAndInsert_Object = MibTableColumn
cascadeDropAndInsert = _CascadeDropAndInsert_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1, 2),
    _CascadeDropAndInsert_Type()
)
cascadeDropAndInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeDropAndInsert.setStatus("mandatory")
_AlarmCfgGroup_ObjectIdentity = ObjectIdentity
alarmCfgGroup = _AlarmCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3)
)


class _CascadeBpvTrapSeverity_Type(Integer32):
    """Custom type cascadeBpvTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeBpvTrapSeverity_Type.__name__ = "Integer32"
_CascadeBpvTrapSeverity_Object = MibScalar
cascadeBpvTrapSeverity = _CascadeBpvTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 1),
    _CascadeBpvTrapSeverity_Type()
)
cascadeBpvTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeBpvTrapSeverity.setStatus("mandatory")


class _CascadeBpvWindow_Type(Integer32):
    """Custom type cascadeBpvWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 2),
          ("oneHour", 3),
          ("oneMinute", 1))
    )


_CascadeBpvWindow_Type.__name__ = "Integer32"
_CascadeBpvWindow_Object = MibScalar
cascadeBpvWindow = _CascadeBpvWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 2),
    _CascadeBpvWindow_Type()
)
cascadeBpvWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeBpvWindow.setStatus("mandatory")


class _CascadeBpvThresh_Type(Integer32):
    """Custom type cascadeBpvThresh based on Integer32"""
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
        *(("thr1", 1),
          ("thr10", 2),
          ("thr100", 3),
          ("thr1000", 4),
          ("thr10000", 5))
    )


_CascadeBpvThresh_Type.__name__ = "Integer32"
_CascadeBpvThresh_Object = MibScalar
cascadeBpvThresh = _CascadeBpvThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 3),
    _CascadeBpvThresh_Type()
)
cascadeBpvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeBpvThresh.setStatus("mandatory")


class _CascadeCrcTrapSeverity_Type(Integer32):
    """Custom type cascadeCrcTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeCrcTrapSeverity_Type.__name__ = "Integer32"
_CascadeCrcTrapSeverity_Object = MibScalar
cascadeCrcTrapSeverity = _CascadeCrcTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 4),
    _CascadeCrcTrapSeverity_Type()
)
cascadeCrcTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeCrcTrapSeverity.setStatus("mandatory")


class _CascadeCrcWindow_Type(Integer32):
    """Custom type cascadeCrcWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 2),
          ("oneHour", 3),
          ("oneMinute", 1))
    )


_CascadeCrcWindow_Type.__name__ = "Integer32"
_CascadeCrcWindow_Object = MibScalar
cascadeCrcWindow = _CascadeCrcWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 5),
    _CascadeCrcWindow_Type()
)
cascadeCrcWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeCrcWindow.setStatus("mandatory")


class _CascadeCrcThresh_Type(Integer32):
    """Custom type cascadeCrcThresh based on Integer32"""
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
        *(("thr1", 1),
          ("thr10", 2),
          ("thr100", 3),
          ("thr1000", 4),
          ("thr10000", 5))
    )


_CascadeCrcThresh_Type.__name__ = "Integer32"
_CascadeCrcThresh_Object = MibScalar
cascadeCrcThresh = _CascadeCrcThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 6),
    _CascadeCrcThresh_Type()
)
cascadeCrcThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeCrcThresh.setStatus("mandatory")


class _CascadeLadTrapSeverity_Type(Integer32):
    """Custom type cascadeLadTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeLadTrapSeverity_Type.__name__ = "Integer32"
_CascadeLadTrapSeverity_Object = MibScalar
cascadeLadTrapSeverity = _CascadeLadTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 7),
    _CascadeLadTrapSeverity_Type()
)
cascadeLadTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeLadTrapSeverity.setStatus("mandatory")


class _CascadeLadWindow_Type(Integer32):
    """Custom type cascadeLadWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 2),
          ("oneHour", 3),
          ("oneMinute", 1))
    )


_CascadeLadWindow_Type.__name__ = "Integer32"
_CascadeLadWindow_Object = MibScalar
cascadeLadWindow = _CascadeLadWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 8),
    _CascadeLadWindow_Type()
)
cascadeLadWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeLadWindow.setStatus("mandatory")


class _CascadeLadThresh_Type(Integer32):
    """Custom type cascadeLadThresh based on Integer32"""
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
        *(("thr1", 1),
          ("thr10", 2),
          ("thr100", 3),
          ("thr1000", 4),
          ("thr10000", 5))
    )


_CascadeLadThresh_Type.__name__ = "Integer32"
_CascadeLadThresh_Object = MibScalar
cascadeLadThresh = _CascadeLadThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 9),
    _CascadeLadThresh_Type()
)
cascadeLadThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeLadThresh.setStatus("mandatory")


class _CascadeAisTrapSeverity_Type(Integer32):
    """Custom type cascadeAisTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeAisTrapSeverity_Type.__name__ = "Integer32"
_CascadeAisTrapSeverity_Object = MibScalar
cascadeAisTrapSeverity = _CascadeAisTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 10),
    _CascadeAisTrapSeverity_Type()
)
cascadeAisTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeAisTrapSeverity.setStatus("mandatory")


class _CascadeLosTrapSeverity_Type(Integer32):
    """Custom type cascadeLosTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeLosTrapSeverity_Type.__name__ = "Integer32"
_CascadeLosTrapSeverity_Object = MibScalar
cascadeLosTrapSeverity = _CascadeLosTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 11),
    _CascadeLosTrapSeverity_Type()
)
cascadeLosTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeLosTrapSeverity.setStatus("mandatory")


class _CascadeOofTrapSeverity_Type(Integer32):
    """Custom type cascadeOofTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeOofTrapSeverity_Type.__name__ = "Integer32"
_CascadeOofTrapSeverity_Object = MibScalar
cascadeOofTrapSeverity = _CascadeOofTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 12),
    _CascadeOofTrapSeverity_Type()
)
cascadeOofTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeOofTrapSeverity.setStatus("mandatory")


class _CascadeRcdYelTrapSeverity_Type(Integer32):
    """Custom type cascadeRcdYelTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeRcdYelTrapSeverity_Type.__name__ = "Integer32"
_CascadeRcdYelTrapSeverity_Object = MibScalar
cascadeRcdYelTrapSeverity = _CascadeRcdYelTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 13),
    _CascadeRcdYelTrapSeverity_Type()
)
cascadeRcdYelTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeRcdYelTrapSeverity.setStatus("mandatory")


class _CascadeUssTrapSeverity_Type(Integer32):
    """Custom type cascadeUssTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_CascadeUssTrapSeverity_Type.__name__ = "Integer32"
_CascadeUssTrapSeverity_Object = MibScalar
cascadeUssTrapSeverity = _CascadeUssTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 14),
    _CascadeUssTrapSeverity_Type()
)
cascadeUssTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeUssTrapSeverity.setStatus("mandatory")
_Diagnostics_ObjectIdentity = ObjectIdentity
diagnostics = _Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4)
)


class _CascadeDiagTest_Type(Integer32):
    """Custom type cascadeDiagTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cascadeLineLoopback", 1),
          ("cascadePayLoadLoopback", 2),
          ("cascadeStopTest", 3))
    )


_CascadeDiagTest_Type.__name__ = "Integer32"
_CascadeDiagTest_Object = MibScalar
cascadeDiagTest = _CascadeDiagTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 1),
    _CascadeDiagTest_Type()
)
cascadeDiagTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeDiagTest.setStatus("mandatory")


class _CascadeDiagTestDuration_Type(Integer32):
    """Custom type cascadeDiagTestDuration based on Integer32"""
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
        *(("testTime10Mins", 3),
          ("testTime1Min", 1),
          ("testTime20Mins", 4),
          ("testTime5Mins", 2))
    )


_CascadeDiagTestDuration_Type.__name__ = "Integer32"
_CascadeDiagTestDuration_Object = MibScalar
cascadeDiagTestDuration = _CascadeDiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 2),
    _CascadeDiagTestDuration_Type()
)
cascadeDiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cascadeDiagTestDuration.setStatus("mandatory")


class _CascadeDiagTestStatus_Type(Integer32):
    """Custom type cascadeDiagTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("statNoTestinProgress", 3),
          ("statcascadeLineLoopback", 1),
          ("statcascadePayLoadLoopback", 2))
    )


_CascadeDiagTestStatus_Type.__name__ = "Integer32"
_CascadeDiagTestStatus_Object = MibScalar
cascadeDiagTestStatus = _CascadeDiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 3),
    _CascadeDiagTestStatus_Type()
)
cascadeDiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cascadeDiagTestStatus.setStatus("mandatory")
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 5)
)


class _CascadePortStatus_Type(OctetString):
    """Custom type cascadePortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CascadePortStatus_Type.__name__ = "OctetString"
_CascadePortStatus_Object = MibScalar
cascadePortStatus = _CascadePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 5, 1),
    _CascadePortStatus_Type()
)
cascadePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cascadePortStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INNOVX-CASCADE-LIU-MIB",
    **{"adminGroup": adminGroup,
       "cascadeMIBversion": cascadeMIBversion,
       "configGroup": configGroup,
       "cascadeInService": cascadeInService,
       "cascadeSetFrameType": cascadeSetFrameType,
       "cascadeOperFrameType": cascadeOperFrameType,
       "cascadeLineCoding": cascadeLineCoding,
       "cascadeIntfType": cascadeIntfType,
       "cascadeDS1IntfRcvLevel": cascadeDS1IntfRcvLevel,
       "cascadeDropAndInsertTable": cascadeDropAndInsertTable,
       "channelEntry": channelEntry,
       "channelIndex": channelIndex,
       "cascadeDropAndInsert": cascadeDropAndInsert,
       "alarmCfgGroup": alarmCfgGroup,
       "cascadeBpvTrapSeverity": cascadeBpvTrapSeverity,
       "cascadeBpvWindow": cascadeBpvWindow,
       "cascadeBpvThresh": cascadeBpvThresh,
       "cascadeCrcTrapSeverity": cascadeCrcTrapSeverity,
       "cascadeCrcWindow": cascadeCrcWindow,
       "cascadeCrcThresh": cascadeCrcThresh,
       "cascadeLadTrapSeverity": cascadeLadTrapSeverity,
       "cascadeLadWindow": cascadeLadWindow,
       "cascadeLadThresh": cascadeLadThresh,
       "cascadeAisTrapSeverity": cascadeAisTrapSeverity,
       "cascadeLosTrapSeverity": cascadeLosTrapSeverity,
       "cascadeOofTrapSeverity": cascadeOofTrapSeverity,
       "cascadeRcdYelTrapSeverity": cascadeRcdYelTrapSeverity,
       "cascadeUssTrapSeverity": cascadeUssTrapSeverity,
       "diagnostics": diagnostics,
       "cascadeDiagTest": cascadeDiagTest,
       "cascadeDiagTestDuration": cascadeDiagTestDuration,
       "cascadeDiagTestStatus": cascadeDiagTestStatus,
       "statusGroup": statusGroup,
       "cascadePortStatus": cascadePortStatus}
)
