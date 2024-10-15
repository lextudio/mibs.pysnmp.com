# SNMP MIB module (AP553LIU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP553LIU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:07 2024
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

(liuGroup,) = mibBuilder.importSymbols(
    "INNOVX-CORE-MIB",
    "liuGroup")

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

_LiuAdmin_ObjectIdentity = ObjectIdentity
liuAdmin = _LiuAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 1)
)


class _Ap553MIBversion_Type(DisplayString):
    """Custom type ap553MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Ap553MIBversion_Type.__name__ = "DisplayString"
_Ap553MIBversion_Object = MibScalar
ap553MIBversion = _Ap553MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 1, 1),
    _Ap553MIBversion_Type()
)
ap553MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553MIBversion.setStatus("mandatory")
_LiuCsuNetCfg_ObjectIdentity = ObjectIdentity
liuCsuNetCfg = _LiuCsuNetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 2)
)


class _Ap553NetSetFrameType_Type(Integer32):
    """Custom type ap553NetSetFrameType based on Integer32"""
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


_Ap553NetSetFrameType_Type.__name__ = "Integer32"
_Ap553NetSetFrameType_Object = MibScalar
ap553NetSetFrameType = _Ap553NetSetFrameType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 2, 1),
    _Ap553NetSetFrameType_Type()
)
ap553NetSetFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetSetFrameType.setStatus("mandatory")


class _Ap553NetOperFrameType_Type(Integer32):
    """Custom type ap553NetOperFrameType based on Integer32"""
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


_Ap553NetOperFrameType_Type.__name__ = "Integer32"
_Ap553NetOperFrameType_Object = MibScalar
ap553NetOperFrameType = _Ap553NetOperFrameType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 2, 2),
    _Ap553NetOperFrameType_Type()
)
ap553NetOperFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553NetOperFrameType.setStatus("mandatory")


class _Ap553NetEsfMode_Type(Integer32):
    """Custom type ap553NetEsfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi-T1-403", 1),
          ("tr-54016", 2))
    )


_Ap553NetEsfMode_Type.__name__ = "Integer32"
_Ap553NetEsfMode_Object = MibScalar
ap553NetEsfMode = _Ap553NetEsfMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 2, 3),
    _Ap553NetEsfMode_Type()
)
ap553NetEsfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetEsfMode.setStatus("mandatory")


class _Ap553NetLineCoding_Type(Integer32):
    """Custom type ap553NetLineCoding based on Integer32"""
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


_Ap553NetLineCoding_Type.__name__ = "Integer32"
_Ap553NetLineCoding_Object = MibScalar
ap553NetLineCoding = _Ap553NetLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 2, 4),
    _Ap553NetLineCoding_Type()
)
ap553NetLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetLineCoding.setStatus("mandatory")


class _Ap553NetIntfType_Type(Integer32):
    """Custom type ap553NetIntfType based on Integer32"""
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
          ("dsx1-preeq133-ft", 6),
          ("dsx1-preeq266-ft", 7),
          ("dsx1-preeq399-ft", 8),
          ("dsx1-preeq533-ft", 9),
          ("dsx1-preeq655-ft", 10))
    )


_Ap553NetIntfType_Type.__name__ = "Integer32"
_Ap553NetIntfType_Object = MibScalar
ap553NetIntfType = _Ap553NetIntfType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 2, 5),
    _Ap553NetIntfType_Type()
)
ap553NetIntfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetIntfType.setStatus("mandatory")


class _Ap553NetDS1IntfRcvLevel_Type(Integer32):
    """Custom type ap553NetDS1IntfRcvLevel based on Integer32"""
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


_Ap553NetDS1IntfRcvLevel_Type.__name__ = "Integer32"
_Ap553NetDS1IntfRcvLevel_Object = MibScalar
ap553NetDS1IntfRcvLevel = _Ap553NetDS1IntfRcvLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 2, 6),
    _Ap553NetDS1IntfRcvLevel_Type()
)
ap553NetDS1IntfRcvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553NetDS1IntfRcvLevel.setStatus("mandatory")
_LiuDsuCfg_ObjectIdentity = ObjectIdentity
liuDsuCfg = _LiuDsuCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3)
)


class _Ap553DS0AllocationScheme_Type(Integer32):
    """Custom type ap553DS0AllocationScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("consecutive", 1))
    )


_Ap553DS0AllocationScheme_Type.__name__ = "Integer32"
_Ap553DS0AllocationScheme_Object = MibScalar
ap553DS0AllocationScheme = _Ap553DS0AllocationScheme_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 1),
    _Ap553DS0AllocationScheme_Type()
)
ap553DS0AllocationScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553DS0AllocationScheme.setStatus("mandatory")


class _Ap553DS0Fmt_Type(Integer32):
    """Custom type ap553DS0Fmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nx56k", 1),
          ("nx64k", 2))
    )


_Ap553DS0Fmt_Type.__name__ = "Integer32"
_Ap553DS0Fmt_Object = MibScalar
ap553DS0Fmt = _Ap553DS0Fmt_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 2),
    _Ap553DS0Fmt_Type()
)
ap553DS0Fmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553DS0Fmt.setStatus("mandatory")


class _Ap553StartingDS0_Type(Integer32):
    """Custom type ap553StartingDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Ap553StartingDS0_Type.__name__ = "Integer32"
_Ap553StartingDS0_Object = MibScalar
ap553StartingDS0 = _Ap553StartingDS0_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 3),
    _Ap553StartingDS0_Type()
)
ap553StartingDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553StartingDS0.setStatus("mandatory")


class _Ap553NumDS0s_Type(Integer32):
    """Custom type ap553NumDS0s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Ap553NumDS0s_Type.__name__ = "Integer32"
_Ap553NumDS0s_Object = MibScalar
ap553NumDS0s = _Ap553NumDS0s_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 4),
    _Ap553NumDS0s_Type()
)
ap553NumDS0s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NumDS0s.setStatus("mandatory")


class _Ap553LIUAggregateRate_Type(DisplayString):
    """Custom type ap553LIUAggregateRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Ap553LIUAggregateRate_Type.__name__ = "DisplayString"
_Ap553LIUAggregateRate_Object = MibScalar
ap553LIUAggregateRate = _Ap553LIUAggregateRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 5),
    _Ap553LIUAggregateRate_Type()
)
ap553LIUAggregateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553LIUAggregateRate.setStatus("mandatory")


class _Ap553SystemStatus_Type(Integer32):
    """Custom type ap553SystemStatus based on Integer32"""
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


_Ap553SystemStatus_Type.__name__ = "Integer32"
_Ap553SystemStatus_Object = MibScalar
ap553SystemStatus = _Ap553SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 6),
    _Ap553SystemStatus_Type()
)
ap553SystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553SystemStatus.setStatus("mandatory")


class _Ap553CircuitAssurance_Type(Integer32):
    """Custom type ap553CircuitAssurance based on Integer32"""
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


_Ap553CircuitAssurance_Type.__name__ = "Integer32"
_Ap553CircuitAssurance_Object = MibScalar
ap553CircuitAssurance = _Ap553CircuitAssurance_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 7),
    _Ap553CircuitAssurance_Type()
)
ap553CircuitAssurance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553CircuitAssurance.setStatus("mandatory")


class _Ap553InbandLoop_Type(Integer32):
    """Custom type ap553InbandLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("lineloop", 3),
          ("payloadloop", 2))
    )


_Ap553InbandLoop_Type.__name__ = "Integer32"
_Ap553InbandLoop_Object = MibScalar
ap553InbandLoop = _Ap553InbandLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 3, 8),
    _Ap553InbandLoop_Type()
)
ap553InbandLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553InbandLoop.setStatus("mandatory")
_LiuNetAlarmCfg_ObjectIdentity = ObjectIdentity
liuNetAlarmCfg = _LiuNetAlarmCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4)
)


class _Ap553NetBpvTrapSeverity_Type(Integer32):
    """Custom type ap553NetBpvTrapSeverity based on Integer32"""
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


_Ap553NetBpvTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetBpvTrapSeverity_Object = MibScalar
ap553NetBpvTrapSeverity = _Ap553NetBpvTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 1),
    _Ap553NetBpvTrapSeverity_Type()
)
ap553NetBpvTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetBpvTrapSeverity.setStatus("mandatory")


class _Ap553NetBpvWindow_Type(Integer32):
    """Custom type ap553NetBpvWindow based on Integer32"""
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


_Ap553NetBpvWindow_Type.__name__ = "Integer32"
_Ap553NetBpvWindow_Object = MibScalar
ap553NetBpvWindow = _Ap553NetBpvWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 2),
    _Ap553NetBpvWindow_Type()
)
ap553NetBpvWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetBpvWindow.setStatus("mandatory")


class _Ap553NetBpvThresh_Type(Integer32):
    """Custom type ap553NetBpvThresh based on Integer32"""
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


_Ap553NetBpvThresh_Type.__name__ = "Integer32"
_Ap553NetBpvThresh_Object = MibScalar
ap553NetBpvThresh = _Ap553NetBpvThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 3),
    _Ap553NetBpvThresh_Type()
)
ap553NetBpvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetBpvThresh.setStatus("mandatory")


class _Ap553NetCrcTrapSeverity_Type(Integer32):
    """Custom type ap553NetCrcTrapSeverity based on Integer32"""
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


_Ap553NetCrcTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetCrcTrapSeverity_Object = MibScalar
ap553NetCrcTrapSeverity = _Ap553NetCrcTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 4),
    _Ap553NetCrcTrapSeverity_Type()
)
ap553NetCrcTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetCrcTrapSeverity.setStatus("mandatory")


class _Ap553NetCrcWindow_Type(Integer32):
    """Custom type ap553NetCrcWindow based on Integer32"""
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


_Ap553NetCrcWindow_Type.__name__ = "Integer32"
_Ap553NetCrcWindow_Object = MibScalar
ap553NetCrcWindow = _Ap553NetCrcWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 5),
    _Ap553NetCrcWindow_Type()
)
ap553NetCrcWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetCrcWindow.setStatus("mandatory")


class _Ap553NetCrcThresh_Type(Integer32):
    """Custom type ap553NetCrcThresh based on Integer32"""
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


_Ap553NetCrcThresh_Type.__name__ = "Integer32"
_Ap553NetCrcThresh_Object = MibScalar
ap553NetCrcThresh = _Ap553NetCrcThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 6),
    _Ap553NetCrcThresh_Type()
)
ap553NetCrcThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetCrcThresh.setStatus("mandatory")


class _Ap553NetLadTrapSeverity_Type(Integer32):
    """Custom type ap553NetLadTrapSeverity based on Integer32"""
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


_Ap553NetLadTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetLadTrapSeverity_Object = MibScalar
ap553NetLadTrapSeverity = _Ap553NetLadTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 7),
    _Ap553NetLadTrapSeverity_Type()
)
ap553NetLadTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetLadTrapSeverity.setStatus("mandatory")


class _Ap553NetLadWindow_Type(Integer32):
    """Custom type ap553NetLadWindow based on Integer32"""
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


_Ap553NetLadWindow_Type.__name__ = "Integer32"
_Ap553NetLadWindow_Object = MibScalar
ap553NetLadWindow = _Ap553NetLadWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 8),
    _Ap553NetLadWindow_Type()
)
ap553NetLadWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetLadWindow.setStatus("mandatory")


class _Ap553NetLadThresh_Type(Integer32):
    """Custom type ap553NetLadThresh based on Integer32"""
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


_Ap553NetLadThresh_Type.__name__ = "Integer32"
_Ap553NetLadThresh_Object = MibScalar
ap553NetLadThresh = _Ap553NetLadThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 9),
    _Ap553NetLadThresh_Type()
)
ap553NetLadThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetLadThresh.setStatus("mandatory")


class _Ap553NetAisTrapSeverity_Type(Integer32):
    """Custom type ap553NetAisTrapSeverity based on Integer32"""
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


_Ap553NetAisTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetAisTrapSeverity_Object = MibScalar
ap553NetAisTrapSeverity = _Ap553NetAisTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 10),
    _Ap553NetAisTrapSeverity_Type()
)
ap553NetAisTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetAisTrapSeverity.setStatus("mandatory")


class _Ap553NetLosTrapSeverity_Type(Integer32):
    """Custom type ap553NetLosTrapSeverity based on Integer32"""
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


_Ap553NetLosTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetLosTrapSeverity_Object = MibScalar
ap553NetLosTrapSeverity = _Ap553NetLosTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 11),
    _Ap553NetLosTrapSeverity_Type()
)
ap553NetLosTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetLosTrapSeverity.setStatus("mandatory")


class _Ap553NetOofTrapSeverity_Type(Integer32):
    """Custom type ap553NetOofTrapSeverity based on Integer32"""
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


_Ap553NetOofTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetOofTrapSeverity_Object = MibScalar
ap553NetOofTrapSeverity = _Ap553NetOofTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 12),
    _Ap553NetOofTrapSeverity_Type()
)
ap553NetOofTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetOofTrapSeverity.setStatus("mandatory")


class _Ap553NetRcdYelTrapSeverity_Type(Integer32):
    """Custom type ap553NetRcdYelTrapSeverity based on Integer32"""
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


_Ap553NetRcdYelTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetRcdYelTrapSeverity_Object = MibScalar
ap553NetRcdYelTrapSeverity = _Ap553NetRcdYelTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 13),
    _Ap553NetRcdYelTrapSeverity_Type()
)
ap553NetRcdYelTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetRcdYelTrapSeverity.setStatus("mandatory")


class _Ap553NetUssTrapSeverity_Type(Integer32):
    """Custom type ap553NetUssTrapSeverity based on Integer32"""
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


_Ap553NetUssTrapSeverity_Type.__name__ = "Integer32"
_Ap553NetUssTrapSeverity_Object = MibScalar
ap553NetUssTrapSeverity = _Ap553NetUssTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 4, 14),
    _Ap553NetUssTrapSeverity_Type()
)
ap553NetUssTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553NetUssTrapSeverity.setStatus("mandatory")
_LiuDiagnostics_ObjectIdentity = ObjectIdentity
liuDiagnostics = _LiuDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 5)
)


class _Ap553DiagT1Test_Type(Integer32):
    """Custom type ap553DiagT1Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t1LineLoopback", 1),
          ("t1PayLoadLoopback", 2),
          ("t1StopTest", 3))
    )


_Ap553DiagT1Test_Type.__name__ = "Integer32"
_Ap553DiagT1Test_Object = MibScalar
ap553DiagT1Test = _Ap553DiagT1Test_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 5, 1),
    _Ap553DiagT1Test_Type()
)
ap553DiagT1Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553DiagT1Test.setStatus("mandatory")


class _Ap553DiagTestDuration_Type(Integer32):
    """Custom type ap553DiagTestDuration based on Integer32"""
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


_Ap553DiagTestDuration_Type.__name__ = "Integer32"
_Ap553DiagTestDuration_Object = MibScalar
ap553DiagTestDuration = _Ap553DiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 5, 2),
    _Ap553DiagTestDuration_Type()
)
ap553DiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap553DiagTestDuration.setStatus("mandatory")


class _Ap553DiagTestStatus_Type(Integer32):
    """Custom type ap553DiagTestStatus based on Integer32"""
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
          ("statT1LineLoopback", 1),
          ("statT1PayLoadLoopback", 2))
    )


_Ap553DiagTestStatus_Type.__name__ = "Integer32"
_Ap553DiagTestStatus_Object = MibScalar
ap553DiagTestStatus = _Ap553DiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 5, 3),
    _Ap553DiagTestStatus_Type()
)
ap553DiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553DiagTestStatus.setStatus("mandatory")
_LiuStatus_ObjectIdentity = ObjectIdentity
liuStatus = _LiuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 6)
)


class _Ap553LedStatus_Type(OctetString):
    """Custom type ap553LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ap553LedStatus_Type.__name__ = "OctetString"
_Ap553LedStatus_Object = MibScalar
ap553LedStatus = _Ap553LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 6, 1),
    _Ap553LedStatus_Type()
)
ap553LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553LedStatus.setStatus("mandatory")


class _Ap553PortStatus_Type(OctetString):
    """Custom type ap553PortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ap553PortStatus_Type.__name__ = "OctetString"
_Ap553PortStatus_Object = MibScalar
ap553PortStatus = _Ap553PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 6, 2),
    _Ap553PortStatus_Type()
)
ap553PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553PortStatus.setStatus("mandatory")


class _Ap553PortFrameCounts_Type(OctetString):
    """Custom type ap553PortFrameCounts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Ap553PortFrameCounts_Type.__name__ = "OctetString"
_Ap553PortFrameCounts_Object = MibScalar
ap553PortFrameCounts = _Ap553PortFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 6, 3),
    _Ap553PortFrameCounts_Type()
)
ap553PortFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553PortFrameCounts.setStatus("mandatory")
_LiuCurrentStats_ObjectIdentity = ObjectIdentity
liuCurrentStats = _LiuCurrentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7)
)


class _Ap553CurrentIntervalCompletion_Type(Integer32):
    """Custom type ap553CurrentIntervalCompletion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ap553CurrentIntervalCompletion_Type.__name__ = "Integer32"
_Ap553CurrentIntervalCompletion_Object = MibScalar
ap553CurrentIntervalCompletion = _Ap553CurrentIntervalCompletion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 1),
    _Ap553CurrentIntervalCompletion_Type()
)
ap553CurrentIntervalCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentIntervalCompletion.setStatus("mandatory")
_Ap553CurrentErroredSeconds_Type = Gauge32
_Ap553CurrentErroredSeconds_Object = MibScalar
ap553CurrentErroredSeconds = _Ap553CurrentErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 2),
    _Ap553CurrentErroredSeconds_Type()
)
ap553CurrentErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentErroredSeconds.setStatus("mandatory")
_Ap553CurrentSeverelyErroredSeconds_Type = Gauge32
_Ap553CurrentSeverelyErroredSeconds_Object = MibScalar
ap553CurrentSeverelyErroredSeconds = _Ap553CurrentSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 3),
    _Ap553CurrentSeverelyErroredSeconds_Type()
)
ap553CurrentSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentSeverelyErroredSeconds.setStatus("mandatory")
_Ap553CurrentBurstyErroredSeconds_Type = Gauge32
_Ap553CurrentBurstyErroredSeconds_Object = MibScalar
ap553CurrentBurstyErroredSeconds = _Ap553CurrentBurstyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 4),
    _Ap553CurrentBurstyErroredSeconds_Type()
)
ap553CurrentBurstyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentBurstyErroredSeconds.setStatus("mandatory")
_Ap553CurrentCrcErrors_Type = Gauge32
_Ap553CurrentCrcErrors_Object = MibScalar
ap553CurrentCrcErrors = _Ap553CurrentCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 5),
    _Ap553CurrentCrcErrors_Type()
)
ap553CurrentCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentCrcErrors.setStatus("mandatory")
_Ap553CurrentUnavailableSeconds_Type = Gauge32
_Ap553CurrentUnavailableSeconds_Object = MibScalar
ap553CurrentUnavailableSeconds = _Ap553CurrentUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 6),
    _Ap553CurrentUnavailableSeconds_Type()
)
ap553CurrentUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentUnavailableSeconds.setStatus("mandatory")
_Ap553CurrentLossOfFrameErrors_Type = Gauge32
_Ap553CurrentLossOfFrameErrors_Object = MibScalar
ap553CurrentLossOfFrameErrors = _Ap553CurrentLossOfFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 7),
    _Ap553CurrentLossOfFrameErrors_Type()
)
ap553CurrentLossOfFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentLossOfFrameErrors.setStatus("mandatory")
_Ap553CurrentBipolarViolationsErrors_Type = Gauge32
_Ap553CurrentBipolarViolationsErrors_Object = MibScalar
ap553CurrentBipolarViolationsErrors = _Ap553CurrentBipolarViolationsErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 8),
    _Ap553CurrentBipolarViolationsErrors_Type()
)
ap553CurrentBipolarViolationsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentBipolarViolationsErrors.setStatus("mandatory")
_Ap553CurrentLossOfSignalErrors_Type = Gauge32
_Ap553CurrentLossOfSignalErrors_Object = MibScalar
ap553CurrentLossOfSignalErrors = _Ap553CurrentLossOfSignalErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 7, 9),
    _Ap553CurrentLossOfSignalErrors_Type()
)
ap553CurrentLossOfSignalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CurrentLossOfSignalErrors.setStatus("mandatory")
_LiuTotalStats_ObjectIdentity = ObjectIdentity
liuTotalStats = _LiuTotalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8)
)
_Ap553TotalErroredSeconds_Type = Gauge32
_Ap553TotalErroredSeconds_Object = MibScalar
ap553TotalErroredSeconds = _Ap553TotalErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 1),
    _Ap553TotalErroredSeconds_Type()
)
ap553TotalErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalErroredSeconds.setStatus("mandatory")
_Ap553TotalSeverelyErroredSeconds_Type = Gauge32
_Ap553TotalSeverelyErroredSeconds_Object = MibScalar
ap553TotalSeverelyErroredSeconds = _Ap553TotalSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 2),
    _Ap553TotalSeverelyErroredSeconds_Type()
)
ap553TotalSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalSeverelyErroredSeconds.setStatus("mandatory")
_Ap553TotalBurstyErroredSeconds_Type = Gauge32
_Ap553TotalBurstyErroredSeconds_Object = MibScalar
ap553TotalBurstyErroredSeconds = _Ap553TotalBurstyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 3),
    _Ap553TotalBurstyErroredSeconds_Type()
)
ap553TotalBurstyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalBurstyErroredSeconds.setStatus("mandatory")
_Ap553TotalCrcErrors_Type = Gauge32
_Ap553TotalCrcErrors_Object = MibScalar
ap553TotalCrcErrors = _Ap553TotalCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 4),
    _Ap553TotalCrcErrors_Type()
)
ap553TotalCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalCrcErrors.setStatus("mandatory")
_Ap553TotalUnavailableSeconds_Type = Gauge32
_Ap553TotalUnavailableSeconds_Object = MibScalar
ap553TotalUnavailableSeconds = _Ap553TotalUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 5),
    _Ap553TotalUnavailableSeconds_Type()
)
ap553TotalUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalUnavailableSeconds.setStatus("mandatory")
_Ap553TotalLossOfFrameErrors_Type = Gauge32
_Ap553TotalLossOfFrameErrors_Object = MibScalar
ap553TotalLossOfFrameErrors = _Ap553TotalLossOfFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 6),
    _Ap553TotalLossOfFrameErrors_Type()
)
ap553TotalLossOfFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalLossOfFrameErrors.setStatus("mandatory")
_Ap553TotalBipolarViolationsErrors_Type = Gauge32
_Ap553TotalBipolarViolationsErrors_Object = MibScalar
ap553TotalBipolarViolationsErrors = _Ap553TotalBipolarViolationsErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 7),
    _Ap553TotalBipolarViolationsErrors_Type()
)
ap553TotalBipolarViolationsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalBipolarViolationsErrors.setStatus("mandatory")
_Ap553TotalLossOfSignalErrors_Type = Gauge32
_Ap553TotalLossOfSignalErrors_Object = MibScalar
ap553TotalLossOfSignalErrors = _Ap553TotalLossOfSignalErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 8, 8),
    _Ap553TotalLossOfSignalErrors_Type()
)
ap553TotalLossOfSignalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553TotalLossOfSignalErrors.setStatus("mandatory")
_LiuHistoryStats_ObjectIdentity = ObjectIdentity
liuHistoryStats = _LiuHistoryStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9)
)


class _Ap553ValidHistoryIntervals_Type(Integer32):
    """Custom type ap553ValidHistoryIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Ap553ValidHistoryIntervals_Type.__name__ = "Integer32"
_Ap553ValidHistoryIntervals_Object = MibScalar
ap553ValidHistoryIntervals = _Ap553ValidHistoryIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 1),
    _Ap553ValidHistoryIntervals_Type()
)
ap553ValidHistoryIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553ValidHistoryIntervals.setStatus("mandatory")
_Ap553LineStats24hrHistoryTable_Object = MibTable
ap553LineStats24hrHistoryTable = _Ap553LineStats24hrHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    ap553LineStats24hrHistoryTable.setStatus("mandatory")
_Ap553HistoryEntry_Object = MibTableRow
ap553HistoryEntry = _Ap553HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1)
)
ap553HistoryEntry.setIndexNames(
    (0, "AP553LIU-MIB", "ap553HistoryInterval"),
)
if mibBuilder.loadTexts:
    ap553HistoryEntry.setStatus("mandatory")


class _Ap553HistoryInterval_Type(Integer32):
    """Custom type ap553HistoryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Ap553HistoryInterval_Type.__name__ = "Integer32"
_Ap553HistoryInterval_Object = MibTableColumn
ap553HistoryInterval = _Ap553HistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 1),
    _Ap553HistoryInterval_Type()
)
ap553HistoryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553HistoryInterval.setStatus("mandatory")
_Ap553ErroredSecondsData_Type = Gauge32
_Ap553ErroredSecondsData_Object = MibTableColumn
ap553ErroredSecondsData = _Ap553ErroredSecondsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 2),
    _Ap553ErroredSecondsData_Type()
)
ap553ErroredSecondsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553ErroredSecondsData.setStatus("mandatory")
_Ap553SeverelyErroredSecondsData_Type = Gauge32
_Ap553SeverelyErroredSecondsData_Object = MibTableColumn
ap553SeverelyErroredSecondsData = _Ap553SeverelyErroredSecondsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 3),
    _Ap553SeverelyErroredSecondsData_Type()
)
ap553SeverelyErroredSecondsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553SeverelyErroredSecondsData.setStatus("mandatory")
_Ap553BurstyErroredSecondsData_Type = Gauge32
_Ap553BurstyErroredSecondsData_Object = MibTableColumn
ap553BurstyErroredSecondsData = _Ap553BurstyErroredSecondsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 4),
    _Ap553BurstyErroredSecondsData_Type()
)
ap553BurstyErroredSecondsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553BurstyErroredSecondsData.setStatus("mandatory")
_Ap553CrcErrorsData_Type = Gauge32
_Ap553CrcErrorsData_Object = MibTableColumn
ap553CrcErrorsData = _Ap553CrcErrorsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 5),
    _Ap553CrcErrorsData_Type()
)
ap553CrcErrorsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553CrcErrorsData.setStatus("mandatory")
_Ap553UnavailableSecondsData_Type = Gauge32
_Ap553UnavailableSecondsData_Object = MibTableColumn
ap553UnavailableSecondsData = _Ap553UnavailableSecondsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 6),
    _Ap553UnavailableSecondsData_Type()
)
ap553UnavailableSecondsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553UnavailableSecondsData.setStatus("mandatory")
_Ap553LossOfFrameErrorsData_Type = Gauge32
_Ap553LossOfFrameErrorsData_Object = MibTableColumn
ap553LossOfFrameErrorsData = _Ap553LossOfFrameErrorsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 7),
    _Ap553LossOfFrameErrorsData_Type()
)
ap553LossOfFrameErrorsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553LossOfFrameErrorsData.setStatus("mandatory")
_Ap553BipolarViolationsErrorsData_Type = Gauge32
_Ap553BipolarViolationsErrorsData_Object = MibTableColumn
ap553BipolarViolationsErrorsData = _Ap553BipolarViolationsErrorsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 8),
    _Ap553BipolarViolationsErrorsData_Type()
)
ap553BipolarViolationsErrorsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553BipolarViolationsErrorsData.setStatus("mandatory")
_Ap553LossOfSignalErrorsData_Type = Gauge32
_Ap553LossOfSignalErrorsData_Object = MibTableColumn
ap553LossOfSignalErrorsData = _Ap553LossOfSignalErrorsData_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3, 9, 2, 1, 9),
    _Ap553LossOfSignalErrorsData_Type()
)
ap553LossOfSignalErrorsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553LossOfSignalErrorsData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AP553LIU-MIB",
    **{"liuAdmin": liuAdmin,
       "ap553MIBversion": ap553MIBversion,
       "liuCsuNetCfg": liuCsuNetCfg,
       "ap553NetSetFrameType": ap553NetSetFrameType,
       "ap553NetOperFrameType": ap553NetOperFrameType,
       "ap553NetEsfMode": ap553NetEsfMode,
       "ap553NetLineCoding": ap553NetLineCoding,
       "ap553NetIntfType": ap553NetIntfType,
       "ap553NetDS1IntfRcvLevel": ap553NetDS1IntfRcvLevel,
       "liuDsuCfg": liuDsuCfg,
       "ap553DS0AllocationScheme": ap553DS0AllocationScheme,
       "ap553DS0Fmt": ap553DS0Fmt,
       "ap553StartingDS0": ap553StartingDS0,
       "ap553NumDS0s": ap553NumDS0s,
       "ap553LIUAggregateRate": ap553LIUAggregateRate,
       "ap553SystemStatus": ap553SystemStatus,
       "ap553CircuitAssurance": ap553CircuitAssurance,
       "ap553InbandLoop": ap553InbandLoop,
       "liuNetAlarmCfg": liuNetAlarmCfg,
       "ap553NetBpvTrapSeverity": ap553NetBpvTrapSeverity,
       "ap553NetBpvWindow": ap553NetBpvWindow,
       "ap553NetBpvThresh": ap553NetBpvThresh,
       "ap553NetCrcTrapSeverity": ap553NetCrcTrapSeverity,
       "ap553NetCrcWindow": ap553NetCrcWindow,
       "ap553NetCrcThresh": ap553NetCrcThresh,
       "ap553NetLadTrapSeverity": ap553NetLadTrapSeverity,
       "ap553NetLadWindow": ap553NetLadWindow,
       "ap553NetLadThresh": ap553NetLadThresh,
       "ap553NetAisTrapSeverity": ap553NetAisTrapSeverity,
       "ap553NetLosTrapSeverity": ap553NetLosTrapSeverity,
       "ap553NetOofTrapSeverity": ap553NetOofTrapSeverity,
       "ap553NetRcdYelTrapSeverity": ap553NetRcdYelTrapSeverity,
       "ap553NetUssTrapSeverity": ap553NetUssTrapSeverity,
       "liuDiagnostics": liuDiagnostics,
       "ap553DiagT1Test": ap553DiagT1Test,
       "ap553DiagTestDuration": ap553DiagTestDuration,
       "ap553DiagTestStatus": ap553DiagTestStatus,
       "liuStatus": liuStatus,
       "ap553LedStatus": ap553LedStatus,
       "ap553PortStatus": ap553PortStatus,
       "ap553PortFrameCounts": ap553PortFrameCounts,
       "liuCurrentStats": liuCurrentStats,
       "ap553CurrentIntervalCompletion": ap553CurrentIntervalCompletion,
       "ap553CurrentErroredSeconds": ap553CurrentErroredSeconds,
       "ap553CurrentSeverelyErroredSeconds": ap553CurrentSeverelyErroredSeconds,
       "ap553CurrentBurstyErroredSeconds": ap553CurrentBurstyErroredSeconds,
       "ap553CurrentCrcErrors": ap553CurrentCrcErrors,
       "ap553CurrentUnavailableSeconds": ap553CurrentUnavailableSeconds,
       "ap553CurrentLossOfFrameErrors": ap553CurrentLossOfFrameErrors,
       "ap553CurrentBipolarViolationsErrors": ap553CurrentBipolarViolationsErrors,
       "ap553CurrentLossOfSignalErrors": ap553CurrentLossOfSignalErrors,
       "liuTotalStats": liuTotalStats,
       "ap553TotalErroredSeconds": ap553TotalErroredSeconds,
       "ap553TotalSeverelyErroredSeconds": ap553TotalSeverelyErroredSeconds,
       "ap553TotalBurstyErroredSeconds": ap553TotalBurstyErroredSeconds,
       "ap553TotalCrcErrors": ap553TotalCrcErrors,
       "ap553TotalUnavailableSeconds": ap553TotalUnavailableSeconds,
       "ap553TotalLossOfFrameErrors": ap553TotalLossOfFrameErrors,
       "ap553TotalBipolarViolationsErrors": ap553TotalBipolarViolationsErrors,
       "ap553TotalLossOfSignalErrors": ap553TotalLossOfSignalErrors,
       "liuHistoryStats": liuHistoryStats,
       "ap553ValidHistoryIntervals": ap553ValidHistoryIntervals,
       "ap553LineStats24hrHistoryTable": ap553LineStats24hrHistoryTable,
       "ap553HistoryEntry": ap553HistoryEntry,
       "ap553HistoryInterval": ap553HistoryInterval,
       "ap553ErroredSecondsData": ap553ErroredSecondsData,
       "ap553SeverelyErroredSecondsData": ap553SeverelyErroredSecondsData,
       "ap553BurstyErroredSecondsData": ap553BurstyErroredSecondsData,
       "ap553CrcErrorsData": ap553CrcErrorsData,
       "ap553UnavailableSecondsData": ap553UnavailableSecondsData,
       "ap553LossOfFrameErrorsData": ap553LossOfFrameErrorsData,
       "ap553BipolarViolationsErrorsData": ap553BipolarViolationsErrorsData,
       "ap553LossOfSignalErrorsData": ap553LossOfSignalErrorsData}
)
