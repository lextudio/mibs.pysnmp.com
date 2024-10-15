# SNMP MIB module (AISLCANALOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISLCANALOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:20 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSLCAnalog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 28)
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLCAnalogInputTable_Object = MibTable
aiSLCAnalogInputTable = _AiSLCAnalogInputTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1)
)
if mibBuilder.loadTexts:
    aiSLCAnalogInputTable.setStatus("current")
_AiSLCAnalogInputEntry_Object = MibTableRow
aiSLCAnalogInputEntry = _AiSLCAnalogInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1)
)
aiSLCAnalogInputEntry.setIndexNames(
    (0, "AISLCANALOG-MIB", "aislcainPointNumber"),
)
if mibBuilder.loadTexts:
    aiSLCAnalogInputEntry.setStatus("current")
_AislcainPointNumber_Type = PositiveInteger
_AislcainPointNumber_Object = MibTableColumn
aislcainPointNumber = _AislcainPointNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 1),
    _AislcainPointNumber_Type()
)
aislcainPointNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcainPointNumber.setStatus("current")


class _AislcainScanningEnabled_Type(Integer32):
    """Custom type aislcainScanningEnabled based on Integer32"""
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


_AislcainScanningEnabled_Type.__name__ = "Integer32"
_AislcainScanningEnabled_Object = MibTableColumn
aislcainScanningEnabled = _AislcainScanningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 2),
    _AislcainScanningEnabled_Type()
)
aislcainScanningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainScanningEnabled.setStatus("current")


class _AislcainDescription_Type(DisplayString):
    """Custom type aislcainDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcainDescription_Type.__name__ = "DisplayString"
_AislcainDescription_Object = MibTableColumn
aislcainDescription = _AislcainDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 3),
    _AislcainDescription_Type()
)
aislcainDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainDescription.setStatus("current")


class _AislcainTrapEnable_Type(Integer32):
    """Custom type aislcainTrapEnable based on Integer32"""
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


_AislcainTrapEnable_Type.__name__ = "Integer32"
_AislcainTrapEnable_Object = MibTableColumn
aislcainTrapEnable = _AislcainTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 4),
    _AislcainTrapEnable_Type()
)
aislcainTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainTrapEnable.setStatus("current")


class _AislcainNormalStateTrap_Type(Integer32):
    """Custom type aislcainNormalStateTrap based on Integer32"""
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


_AislcainNormalStateTrap_Type.__name__ = "Integer32"
_AislcainNormalStateTrap_Object = MibTableColumn
aislcainNormalStateTrap = _AislcainNormalStateTrap_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 5),
    _AislcainNormalStateTrap_Type()
)
aislcainNormalStateTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainNormalStateTrap.setStatus("current")


class _AislcainHighAlarmSeverity_Type(Integer32):
    """Custom type aislcainHighAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("notReported", 5))
    )


_AislcainHighAlarmSeverity_Type.__name__ = "Integer32"
_AislcainHighAlarmSeverity_Object = MibTableColumn
aislcainHighAlarmSeverity = _AislcainHighAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 6),
    _AislcainHighAlarmSeverity_Type()
)
aislcainHighAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainHighAlarmSeverity.setStatus("current")


class _AislcainHighAlarmStateText_Type(DisplayString):
    """Custom type aislcainHighAlarmStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcainHighAlarmStateText_Type.__name__ = "DisplayString"
_AislcainHighAlarmStateText_Object = MibTableColumn
aislcainHighAlarmStateText = _AislcainHighAlarmStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 7),
    _AislcainHighAlarmStateText_Type()
)
aislcainHighAlarmStateText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainHighAlarmStateText.setStatus("current")


class _AislcainLowAlarmSeverity_Type(Integer32):
    """Custom type aislcainLowAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("notReported", 5))
    )


_AislcainLowAlarmSeverity_Type.__name__ = "Integer32"
_AislcainLowAlarmSeverity_Object = MibTableColumn
aislcainLowAlarmSeverity = _AislcainLowAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 8),
    _AislcainLowAlarmSeverity_Type()
)
aislcainLowAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainLowAlarmSeverity.setStatus("current")


class _AislcainLowAlarmStateText_Type(DisplayString):
    """Custom type aislcainLowAlarmStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcainLowAlarmStateText_Type.__name__ = "DisplayString"
_AislcainLowAlarmStateText_Object = MibTableColumn
aislcainLowAlarmStateText = _AislcainLowAlarmStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 9),
    _AislcainLowAlarmStateText_Type()
)
aislcainLowAlarmStateText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainLowAlarmStateText.setStatus("current")


class _AislcainNormalStateText_Type(DisplayString):
    """Custom type aislcainNormalStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcainNormalStateText_Type.__name__ = "DisplayString"
_AislcainNormalStateText_Object = MibTableColumn
aislcainNormalStateText = _AislcainNormalStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 10),
    _AislcainNormalStateText_Type()
)
aislcainNormalStateText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainNormalStateText.setStatus("current")


class _AislcainUserUnits_Type(DisplayString):
    """Custom type aislcainUserUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AislcainUserUnits_Type.__name__ = "DisplayString"
_AislcainUserUnits_Object = MibTableColumn
aislcainUserUnits = _AislcainUserUnits_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 11),
    _AislcainUserUnits_Type()
)
aislcainUserUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainUserUnits.setStatus("current")


class _AislcainMinInputmA_Type(DisplayString):
    """Custom type aislcainMinInputmA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainMinInputmA_Type.__name__ = "DisplayString"
_AislcainMinInputmA_Object = MibTableColumn
aislcainMinInputmA = _AislcainMinInputmA_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 12),
    _AislcainMinInputmA_Type()
)
aislcainMinInputmA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainMinInputmA.setStatus("current")


class _AislcainMinInputuu_Type(DisplayString):
    """Custom type aislcainMinInputuu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainMinInputuu_Type.__name__ = "DisplayString"
_AislcainMinInputuu_Object = MibTableColumn
aislcainMinInputuu = _AislcainMinInputuu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 13),
    _AislcainMinInputuu_Type()
)
aislcainMinInputuu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainMinInputuu.setStatus("current")


class _AislcainMaxInputmA_Type(DisplayString):
    """Custom type aislcainMaxInputmA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainMaxInputmA_Type.__name__ = "DisplayString"
_AislcainMaxInputmA_Object = MibTableColumn
aislcainMaxInputmA = _AislcainMaxInputmA_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 14),
    _AislcainMaxInputmA_Type()
)
aislcainMaxInputmA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainMaxInputmA.setStatus("current")


class _AislcainMaxInputuu_Type(DisplayString):
    """Custom type aislcainMaxInputuu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainMaxInputuu_Type.__name__ = "DisplayString"
_AislcainMaxInputuu_Object = MibTableColumn
aislcainMaxInputuu = _AislcainMaxInputuu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 15),
    _AislcainMaxInputuu_Type()
)
aislcainMaxInputuu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainMaxInputuu.setStatus("current")


class _AislcainHighLimitScan_Type(Integer32):
    """Custom type aislcainHighLimitScan based on Integer32"""
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


_AislcainHighLimitScan_Type.__name__ = "Integer32"
_AislcainHighLimitScan_Object = MibTableColumn
aislcainHighLimitScan = _AislcainHighLimitScan_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 16),
    _AislcainHighLimitScan_Type()
)
aislcainHighLimitScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainHighLimitScan.setStatus("current")


class _AislcainHighAlarmThresholduu_Type(DisplayString):
    """Custom type aislcainHighAlarmThresholduu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainHighAlarmThresholduu_Type.__name__ = "DisplayString"
_AislcainHighAlarmThresholduu_Object = MibTableColumn
aislcainHighAlarmThresholduu = _AislcainHighAlarmThresholduu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 17),
    _AislcainHighAlarmThresholduu_Type()
)
aislcainHighAlarmThresholduu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainHighAlarmThresholduu.setStatus("current")


class _AislcainHighAlarmThresholdIntervaluu_Type(DisplayString):
    """Custom type aislcainHighAlarmThresholdIntervaluu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainHighAlarmThresholdIntervaluu_Type.__name__ = "DisplayString"
_AislcainHighAlarmThresholdIntervaluu_Object = MibTableColumn
aislcainHighAlarmThresholdIntervaluu = _AislcainHighAlarmThresholdIntervaluu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 18),
    _AislcainHighAlarmThresholdIntervaluu_Type()
)
aislcainHighAlarmThresholdIntervaluu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainHighAlarmThresholdIntervaluu.setStatus("current")


class _AislcainHighAlarmMinPeriod_Type(Integer32):
    """Custom type aislcainHighAlarmMinPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AislcainHighAlarmMinPeriod_Type.__name__ = "Integer32"
_AislcainHighAlarmMinPeriod_Object = MibTableColumn
aislcainHighAlarmMinPeriod = _AislcainHighAlarmMinPeriod_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 19),
    _AislcainHighAlarmMinPeriod_Type()
)
aislcainHighAlarmMinPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainHighAlarmMinPeriod.setStatus("current")


class _AislcainHighAlarmHysteresisuu_Type(DisplayString):
    """Custom type aislcainHighAlarmHysteresisuu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainHighAlarmHysteresisuu_Type.__name__ = "DisplayString"
_AislcainHighAlarmHysteresisuu_Object = MibTableColumn
aislcainHighAlarmHysteresisuu = _AislcainHighAlarmHysteresisuu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 20),
    _AislcainHighAlarmHysteresisuu_Type()
)
aislcainHighAlarmHysteresisuu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainHighAlarmHysteresisuu.setStatus("current")


class _AislcainLowLimitScan_Type(Integer32):
    """Custom type aislcainLowLimitScan based on Integer32"""
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


_AislcainLowLimitScan_Type.__name__ = "Integer32"
_AislcainLowLimitScan_Object = MibTableColumn
aislcainLowLimitScan = _AislcainLowLimitScan_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 21),
    _AislcainLowLimitScan_Type()
)
aislcainLowLimitScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainLowLimitScan.setStatus("current")


class _AislcainLowAlarmThresholduu_Type(DisplayString):
    """Custom type aislcainLowAlarmThresholduu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainLowAlarmThresholduu_Type.__name__ = "DisplayString"
_AislcainLowAlarmThresholduu_Object = MibTableColumn
aislcainLowAlarmThresholduu = _AislcainLowAlarmThresholduu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 22),
    _AislcainLowAlarmThresholduu_Type()
)
aislcainLowAlarmThresholduu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainLowAlarmThresholduu.setStatus("current")


class _AislcainLowAlarmThresholdIntervaluu_Type(DisplayString):
    """Custom type aislcainLowAlarmThresholdIntervaluu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainLowAlarmThresholdIntervaluu_Type.__name__ = "DisplayString"
_AislcainLowAlarmThresholdIntervaluu_Object = MibTableColumn
aislcainLowAlarmThresholdIntervaluu = _AislcainLowAlarmThresholdIntervaluu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 23),
    _AislcainLowAlarmThresholdIntervaluu_Type()
)
aislcainLowAlarmThresholdIntervaluu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainLowAlarmThresholdIntervaluu.setStatus("current")


class _AislcainLowAlarmMinPeriod_Type(Integer32):
    """Custom type aislcainLowAlarmMinPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AislcainLowAlarmMinPeriod_Type.__name__ = "Integer32"
_AislcainLowAlarmMinPeriod_Object = MibTableColumn
aislcainLowAlarmMinPeriod = _AislcainLowAlarmMinPeriod_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 24),
    _AislcainLowAlarmMinPeriod_Type()
)
aislcainLowAlarmMinPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainLowAlarmMinPeriod.setStatus("current")


class _AislcainLowAlarmHysteresisuu_Type(DisplayString):
    """Custom type aislcainLowAlarmHysteresisuu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainLowAlarmHysteresisuu_Type.__name__ = "DisplayString"
_AislcainLowAlarmHysteresisuu_Object = MibTableColumn
aislcainLowAlarmHysteresisuu = _AislcainLowAlarmHysteresisuu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 25),
    _AislcainLowAlarmHysteresisuu_Type()
)
aislcainLowAlarmHysteresisuu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcainLowAlarmHysteresisuu.setStatus("current")


class _AislcainCurrentValueuu_Type(DisplayString):
    """Custom type aislcainCurrentValueuu based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AislcainCurrentValueuu_Type.__name__ = "DisplayString"
_AislcainCurrentValueuu_Object = MibTableColumn
aislcainCurrentValueuu = _AislcainCurrentValueuu_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 26),
    _AislcainCurrentValueuu_Type()
)
aislcainCurrentValueuu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcainCurrentValueuu.setStatus("current")


class _AislcainCurrentValuemA_Type(DisplayString):
    """Custom type aislcainCurrentValuemA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AislcainCurrentValuemA_Type.__name__ = "DisplayString"
_AislcainCurrentValuemA_Object = MibTableColumn
aislcainCurrentValuemA = _AislcainCurrentValuemA_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 27),
    _AislcainCurrentValuemA_Type()
)
aislcainCurrentValuemA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcainCurrentValuemA.setStatus("current")


class _AislcainLastChangeTime_Type(DisplayString):
    """Custom type aislcainLastChangeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 23),
    )


_AislcainLastChangeTime_Type.__name__ = "DisplayString"
_AislcainLastChangeTime_Object = MibTableColumn
aislcainLastChangeTime = _AislcainLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 28),
    _AislcainLastChangeTime_Type()
)
aislcainLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcainLastChangeTime.setStatus("current")


class _Aislcaintl1AccessID_Type(DisplayString):
    """Custom type aislcaintl1AccessID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Aislcaintl1AccessID_Type.__name__ = "DisplayString"
_Aislcaintl1AccessID_Object = MibTableColumn
aislcaintl1AccessID = _Aislcaintl1AccessID_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 29),
    _Aislcaintl1AccessID_Type()
)
aislcaintl1AccessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1AccessID.setStatus("current")
_Aislcaintl1Provisioned_Type = TruthValue
_Aislcaintl1Provisioned_Object = MibTableColumn
aislcaintl1Provisioned = _Aislcaintl1Provisioned_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 30),
    _Aislcaintl1Provisioned_Type()
)
aislcaintl1Provisioned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1Provisioned.setStatus("current")


class _Aislcaintl1AccessIDType_Type(Integer32):
    """Custom type aislcaintl1AccessIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("environmental", 2),
          ("equipment", 1))
    )


_Aislcaintl1AccessIDType_Type.__name__ = "Integer32"
_Aislcaintl1AccessIDType_Object = MibTableColumn
aislcaintl1AccessIDType = _Aislcaintl1AccessIDType_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 31),
    _Aislcaintl1AccessIDType_Type()
)
aislcaintl1AccessIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1AccessIDType.setStatus("current")


class _Aislcaintl1HighAlarmType_Type(DisplayString):
    """Custom type aislcaintl1HighAlarmType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Aislcaintl1HighAlarmType_Type.__name__ = "DisplayString"
_Aislcaintl1HighAlarmType_Object = MibTableColumn
aislcaintl1HighAlarmType = _Aislcaintl1HighAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 32),
    _Aislcaintl1HighAlarmType_Type()
)
aislcaintl1HighAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1HighAlarmType.setStatus("current")


class _Aislcaintl1HighAlarmMessage_Type(DisplayString):
    """Custom type aislcaintl1HighAlarmMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Aislcaintl1HighAlarmMessage_Type.__name__ = "DisplayString"
_Aislcaintl1HighAlarmMessage_Object = MibTableColumn
aislcaintl1HighAlarmMessage = _Aislcaintl1HighAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 33),
    _Aislcaintl1HighAlarmMessage_Type()
)
aislcaintl1HighAlarmMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1HighAlarmMessage.setStatus("current")


class _Aislcaintl1LowAlarmType_Type(DisplayString):
    """Custom type aislcaintl1LowAlarmType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Aislcaintl1LowAlarmType_Type.__name__ = "DisplayString"
_Aislcaintl1LowAlarmType_Object = MibTableColumn
aislcaintl1LowAlarmType = _Aislcaintl1LowAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 34),
    _Aislcaintl1LowAlarmType_Type()
)
aislcaintl1LowAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1LowAlarmType.setStatus("current")


class _Aislcaintl1LowAlarmMessage_Type(DisplayString):
    """Custom type aislcaintl1LowAlarmMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Aislcaintl1LowAlarmMessage_Type.__name__ = "DisplayString"
_Aislcaintl1LowAlarmMessage_Object = MibTableColumn
aislcaintl1LowAlarmMessage = _Aislcaintl1LowAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 35),
    _Aislcaintl1LowAlarmMessage_Type()
)
aislcaintl1LowAlarmMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1LowAlarmMessage.setStatus("current")


class _Aislcaintl1HighAlarmNotificationCode_Type(Integer32):
    """Custom type aislcaintl1HighAlarmNotificationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_Aislcaintl1HighAlarmNotificationCode_Type.__name__ = "Integer32"
_Aislcaintl1HighAlarmNotificationCode_Object = MibTableColumn
aislcaintl1HighAlarmNotificationCode = _Aislcaintl1HighAlarmNotificationCode_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 36),
    _Aislcaintl1HighAlarmNotificationCode_Type()
)
aislcaintl1HighAlarmNotificationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1HighAlarmNotificationCode.setStatus("current")


class _Aislcaintl1HighAlarmServiceAffecting_Type(Integer32):
    """Custom type aislcaintl1HighAlarmServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notServiceAffecting", 2),
          ("serviceAffecting", 1))
    )


_Aislcaintl1HighAlarmServiceAffecting_Type.__name__ = "Integer32"
_Aislcaintl1HighAlarmServiceAffecting_Object = MibTableColumn
aislcaintl1HighAlarmServiceAffecting = _Aislcaintl1HighAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 37),
    _Aislcaintl1HighAlarmServiceAffecting_Type()
)
aislcaintl1HighAlarmServiceAffecting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1HighAlarmServiceAffecting.setStatus("current")


class _Aislcaintl1HighAlarmConditionType_Type(DisplayString):
    """Custom type aislcaintl1HighAlarmConditionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Aislcaintl1HighAlarmConditionType_Type.__name__ = "DisplayString"
_Aislcaintl1HighAlarmConditionType_Object = MibTableColumn
aislcaintl1HighAlarmConditionType = _Aislcaintl1HighAlarmConditionType_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 38),
    _Aislcaintl1HighAlarmConditionType_Type()
)
aislcaintl1HighAlarmConditionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1HighAlarmConditionType.setStatus("current")


class _Aislcaintl1HighAlarmConditionDesc_Type(DisplayString):
    """Custom type aislcaintl1HighAlarmConditionDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Aislcaintl1HighAlarmConditionDesc_Type.__name__ = "DisplayString"
_Aislcaintl1HighAlarmConditionDesc_Object = MibTableColumn
aislcaintl1HighAlarmConditionDesc = _Aislcaintl1HighAlarmConditionDesc_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 39),
    _Aislcaintl1HighAlarmConditionDesc_Type()
)
aislcaintl1HighAlarmConditionDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1HighAlarmConditionDesc.setStatus("current")


class _Aislcaintl1LowAlarmNotificationCode_Type(Integer32):
    """Custom type aislcaintl1LowAlarmNotificationCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_Aislcaintl1LowAlarmNotificationCode_Type.__name__ = "Integer32"
_Aislcaintl1LowAlarmNotificationCode_Object = MibTableColumn
aislcaintl1LowAlarmNotificationCode = _Aislcaintl1LowAlarmNotificationCode_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 40),
    _Aislcaintl1LowAlarmNotificationCode_Type()
)
aislcaintl1LowAlarmNotificationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1LowAlarmNotificationCode.setStatus("current")


class _Aislcaintl1LowAlarmServiceAffecting_Type(Integer32):
    """Custom type aislcaintl1LowAlarmServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notServiceAffecting", 2),
          ("serviceAffecting", 1))
    )


_Aislcaintl1LowAlarmServiceAffecting_Type.__name__ = "Integer32"
_Aislcaintl1LowAlarmServiceAffecting_Object = MibTableColumn
aislcaintl1LowAlarmServiceAffecting = _Aislcaintl1LowAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 41),
    _Aislcaintl1LowAlarmServiceAffecting_Type()
)
aislcaintl1LowAlarmServiceAffecting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1LowAlarmServiceAffecting.setStatus("current")


class _Aislcaintl1LowAlarmConditionType_Type(DisplayString):
    """Custom type aislcaintl1LowAlarmConditionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Aislcaintl1LowAlarmConditionType_Type.__name__ = "DisplayString"
_Aislcaintl1LowAlarmConditionType_Object = MibTableColumn
aislcaintl1LowAlarmConditionType = _Aislcaintl1LowAlarmConditionType_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 42),
    _Aislcaintl1LowAlarmConditionType_Type()
)
aislcaintl1LowAlarmConditionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1LowAlarmConditionType.setStatus("current")


class _Aislcaintl1LowAlarmConditionDesc_Type(DisplayString):
    """Custom type aislcaintl1LowAlarmConditionDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Aislcaintl1LowAlarmConditionDesc_Type.__name__ = "DisplayString"
_Aislcaintl1LowAlarmConditionDesc_Object = MibTableColumn
aislcaintl1LowAlarmConditionDesc = _Aislcaintl1LowAlarmConditionDesc_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 43),
    _Aislcaintl1LowAlarmConditionDesc_Type()
)
aislcaintl1LowAlarmConditionDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcaintl1LowAlarmConditionDesc.setStatus("current")


class _AislcainAnalogStatus_Type(Integer32):
    """Custom type aislcainAnalogStatus based on Integer32"""
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
        *(("highLimitExceeded", 2),
          ("lossOfSignal", 4),
          ("lowLimitExceeded", 3),
          ("normal", 1),
          ("saturated", 5))
    )


_AislcainAnalogStatus_Type.__name__ = "Integer32"
_AislcainAnalogStatus_Object = MibTableColumn
aislcainAnalogStatus = _AislcainAnalogStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 44),
    _AislcainAnalogStatus_Type()
)
aislcainAnalogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcainAnalogStatus.setStatus("current")


class _AislcainCurrentStateText_Type(DisplayString):
    """Custom type aislcainCurrentStateText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcainCurrentStateText_Type.__name__ = "DisplayString"
_AislcainCurrentStateText_Object = MibTableColumn
aislcainCurrentStateText = _AislcainCurrentStateText_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 45),
    _AislcainCurrentStateText_Type()
)
aislcainCurrentStateText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcainCurrentStateText.setStatus("current")


class _AislcainAnalogAlarmState_Type(Integer32):
    """Custom type aislcainAnalogAlarmState based on Integer32"""
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3),
          ("normal", 5))
    )


_AislcainAnalogAlarmState_Type.__name__ = "Integer32"
_AislcainAnalogAlarmState_Object = MibTableColumn
aislcainAnalogAlarmState = _AislcainAnalogAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 539, 28, 1, 1, 46),
    _AislcainAnalogAlarmState_Type()
)
aislcainAnalogAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcainAnalogAlarmState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISLCANALOG-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "aii": aii,
       "aiSLCAnalog": aiSLCAnalog,
       "aiSLCAnalogInputTable": aiSLCAnalogInputTable,
       "aiSLCAnalogInputEntry": aiSLCAnalogInputEntry,
       "aislcainPointNumber": aislcainPointNumber,
       "aislcainScanningEnabled": aislcainScanningEnabled,
       "aislcainDescription": aislcainDescription,
       "aislcainTrapEnable": aislcainTrapEnable,
       "aislcainNormalStateTrap": aislcainNormalStateTrap,
       "aislcainHighAlarmSeverity": aislcainHighAlarmSeverity,
       "aislcainHighAlarmStateText": aislcainHighAlarmStateText,
       "aislcainLowAlarmSeverity": aislcainLowAlarmSeverity,
       "aislcainLowAlarmStateText": aislcainLowAlarmStateText,
       "aislcainNormalStateText": aislcainNormalStateText,
       "aislcainUserUnits": aislcainUserUnits,
       "aislcainMinInputmA": aislcainMinInputmA,
       "aislcainMinInputuu": aislcainMinInputuu,
       "aislcainMaxInputmA": aislcainMaxInputmA,
       "aislcainMaxInputuu": aislcainMaxInputuu,
       "aislcainHighLimitScan": aislcainHighLimitScan,
       "aislcainHighAlarmThresholduu": aislcainHighAlarmThresholduu,
       "aislcainHighAlarmThresholdIntervaluu": aislcainHighAlarmThresholdIntervaluu,
       "aislcainHighAlarmMinPeriod": aislcainHighAlarmMinPeriod,
       "aislcainHighAlarmHysteresisuu": aislcainHighAlarmHysteresisuu,
       "aislcainLowLimitScan": aislcainLowLimitScan,
       "aislcainLowAlarmThresholduu": aislcainLowAlarmThresholduu,
       "aislcainLowAlarmThresholdIntervaluu": aislcainLowAlarmThresholdIntervaluu,
       "aislcainLowAlarmMinPeriod": aislcainLowAlarmMinPeriod,
       "aislcainLowAlarmHysteresisuu": aislcainLowAlarmHysteresisuu,
       "aislcainCurrentValueuu": aislcainCurrentValueuu,
       "aislcainCurrentValuemA": aislcainCurrentValuemA,
       "aislcainLastChangeTime": aislcainLastChangeTime,
       "aislcaintl1AccessID": aislcaintl1AccessID,
       "aislcaintl1Provisioned": aislcaintl1Provisioned,
       "aislcaintl1AccessIDType": aislcaintl1AccessIDType,
       "aislcaintl1HighAlarmType": aislcaintl1HighAlarmType,
       "aislcaintl1HighAlarmMessage": aislcaintl1HighAlarmMessage,
       "aislcaintl1LowAlarmType": aislcaintl1LowAlarmType,
       "aislcaintl1LowAlarmMessage": aislcaintl1LowAlarmMessage,
       "aislcaintl1HighAlarmNotificationCode": aislcaintl1HighAlarmNotificationCode,
       "aislcaintl1HighAlarmServiceAffecting": aislcaintl1HighAlarmServiceAffecting,
       "aislcaintl1HighAlarmConditionType": aislcaintl1HighAlarmConditionType,
       "aislcaintl1HighAlarmConditionDesc": aislcaintl1HighAlarmConditionDesc,
       "aislcaintl1LowAlarmNotificationCode": aislcaintl1LowAlarmNotificationCode,
       "aislcaintl1LowAlarmServiceAffecting": aislcaintl1LowAlarmServiceAffecting,
       "aislcaintl1LowAlarmConditionType": aislcaintl1LowAlarmConditionType,
       "aislcaintl1LowAlarmConditionDesc": aislcaintl1LowAlarmConditionDesc,
       "aislcainAnalogStatus": aislcainAnalogStatus,
       "aislcainCurrentStateText": aislcainCurrentStateText,
       "aislcainAnalogAlarmState": aislcainAnalogAlarmState}
)
