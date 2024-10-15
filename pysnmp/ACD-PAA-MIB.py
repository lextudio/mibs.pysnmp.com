# SNMP MIB module (ACD-PAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-PAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:21 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdPaa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5)
)
acdPaa.setRevisions(
        ("2012-11-06 01:00",
         "2010-11-10 01:00",
         "2009-02-23 01:00",
         "2008-02-06 01:00",
         "2007-10-12 01:00",
         "2006-12-18 01:00",
         "2006-11-11 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdPaaResultTable_Object = MibTable
acdPaaResultTable = _AcdPaaResultTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1)
)
if mibBuilder.loadTexts:
    acdPaaResultTable.setStatus("current")
_AcdPaaResultEntry_Object = MibTableRow
acdPaaResultEntry = _AcdPaaResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1)
)
acdPaaResultEntry.setIndexNames(
    (0, "ACD-PAA-MIB", "acdPaaResultID"),
)
if mibBuilder.loadTexts:
    acdPaaResultEntry.setStatus("current")
_AcdPaaResultID_Type = Unsigned32
_AcdPaaResultID_Object = MibTableColumn
acdPaaResultID = _AcdPaaResultID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 1),
    _AcdPaaResultID_Type()
)
acdPaaResultID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPaaResultID.setStatus("current")


class _AcdPaaResultState_Type(Integer32):
    """Custom type acdPaaResultState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("associated", 2),
          ("associating", 1),
          ("disabled", 0),
          ("idle", 4),
          ("lockedIS", 5),
          ("lockedOOS", 6),
          ("running", 3))
    )


_AcdPaaResultState_Type.__name__ = "Integer32"
_AcdPaaResultState_Object = MibTableColumn
acdPaaResultState = _AcdPaaResultState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 2),
    _AcdPaaResultState_Type()
)
acdPaaResultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultState.setStatus("current")
_AcdPaaResultPktLossNeCurrValid_Type = TruthValue
_AcdPaaResultPktLossNeCurrValid_Object = MibTableColumn
acdPaaResultPktLossNeCurrValid = _AcdPaaResultPktLossNeCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 3),
    _AcdPaaResultPktLossNeCurrValid_Type()
)
acdPaaResultPktLossNeCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNeCurrValid.setStatus("current")


class _AcdPaaResultPktLossNeCurrValue_Type(Unsigned32):
    """Custom type acdPaaResultPktLossNeCurrValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AcdPaaResultPktLossNeCurrValue_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossNeCurrValue_Object = MibTableColumn
acdPaaResultPktLossNeCurrValue = _AcdPaaResultPktLossNeCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 4),
    _AcdPaaResultPktLossNeCurrValue_Type()
)
acdPaaResultPktLossNeCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNeCurrValue.setStatus("current")
_AcdPaaResultPktLossNePrevValid_Type = TruthValue
_AcdPaaResultPktLossNePrevValid_Object = MibTableColumn
acdPaaResultPktLossNePrevValid = _AcdPaaResultPktLossNePrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 5),
    _AcdPaaResultPktLossNePrevValid_Type()
)
acdPaaResultPktLossNePrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNePrevValid.setStatus("current")


class _AcdPaaResultPktLossNePrevValue_Type(Unsigned32):
    """Custom type acdPaaResultPktLossNePrevValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AcdPaaResultPktLossNePrevValue_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossNePrevValue_Object = MibTableColumn
acdPaaResultPktLossNePrevValue = _AcdPaaResultPktLossNePrevValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 6),
    _AcdPaaResultPktLossNePrevValue_Type()
)
acdPaaResultPktLossNePrevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNePrevValue.setStatus("current")
_AcdPaaResultPktLossFeCurrValid_Type = TruthValue
_AcdPaaResultPktLossFeCurrValid_Object = MibTableColumn
acdPaaResultPktLossFeCurrValid = _AcdPaaResultPktLossFeCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 7),
    _AcdPaaResultPktLossFeCurrValid_Type()
)
acdPaaResultPktLossFeCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFeCurrValid.setStatus("current")


class _AcdPaaResultPktLossFeCurrValue_Type(Unsigned32):
    """Custom type acdPaaResultPktLossFeCurrValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AcdPaaResultPktLossFeCurrValue_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossFeCurrValue_Object = MibTableColumn
acdPaaResultPktLossFeCurrValue = _AcdPaaResultPktLossFeCurrValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 8),
    _AcdPaaResultPktLossFeCurrValue_Type()
)
acdPaaResultPktLossFeCurrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFeCurrValue.setStatus("current")
_AcdPaaResultPktLossFePrevValid_Type = TruthValue
_AcdPaaResultPktLossFePrevValid_Object = MibTableColumn
acdPaaResultPktLossFePrevValid = _AcdPaaResultPktLossFePrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 9),
    _AcdPaaResultPktLossFePrevValid_Type()
)
acdPaaResultPktLossFePrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFePrevValid.setStatus("current")


class _AcdPaaResultPktLossFePrevValue_Type(Unsigned32):
    """Custom type acdPaaResultPktLossFePrevValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AcdPaaResultPktLossFePrevValue_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossFePrevValue_Object = MibTableColumn
acdPaaResultPktLossFePrevValue = _AcdPaaResultPktLossFePrevValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 10),
    _AcdPaaResultPktLossFePrevValue_Type()
)
acdPaaResultPktLossFePrevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFePrevValue.setStatus("current")
_AcdPaaResultOneWayDvInstValue_Type = Integer32
_AcdPaaResultOneWayDvInstValue_Object = MibTableColumn
acdPaaResultOneWayDvInstValue = _AcdPaaResultOneWayDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 11),
    _AcdPaaResultOneWayDvInstValue_Type()
)
acdPaaResultOneWayDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvInstValue.setStatus("current")
_AcdPaaResultOneWayDvCurrValid_Type = TruthValue
_AcdPaaResultOneWayDvCurrValid_Object = MibTableColumn
acdPaaResultOneWayDvCurrValid = _AcdPaaResultOneWayDvCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 12),
    _AcdPaaResultOneWayDvCurrValid_Type()
)
acdPaaResultOneWayDvCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvCurrValid.setStatus("current")
_AcdPaaResultOneWayDvCurrMinValue_Type = Integer32
_AcdPaaResultOneWayDvCurrMinValue_Object = MibTableColumn
acdPaaResultOneWayDvCurrMinValue = _AcdPaaResultOneWayDvCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 13),
    _AcdPaaResultOneWayDvCurrMinValue_Type()
)
acdPaaResultOneWayDvCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvCurrMinValue.setStatus("current")
_AcdPaaResultOneWayDvCurrMaxValue_Type = Integer32
_AcdPaaResultOneWayDvCurrMaxValue_Object = MibTableColumn
acdPaaResultOneWayDvCurrMaxValue = _AcdPaaResultOneWayDvCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 14),
    _AcdPaaResultOneWayDvCurrMaxValue_Type()
)
acdPaaResultOneWayDvCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvCurrMaxValue.setStatus("current")
_AcdPaaResultOneWayDvCurrAvgValue_Type = Integer32
_AcdPaaResultOneWayDvCurrAvgValue_Object = MibTableColumn
acdPaaResultOneWayDvCurrAvgValue = _AcdPaaResultOneWayDvCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 15),
    _AcdPaaResultOneWayDvCurrAvgValue_Type()
)
acdPaaResultOneWayDvCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvCurrAvgValue.setStatus("current")
_AcdPaaResultOneWayDvCurrThreshExc_Type = Unsigned32
_AcdPaaResultOneWayDvCurrThreshExc_Object = MibTableColumn
acdPaaResultOneWayDvCurrThreshExc = _AcdPaaResultOneWayDvCurrThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 16),
    _AcdPaaResultOneWayDvCurrThreshExc_Type()
)
acdPaaResultOneWayDvCurrThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvCurrThreshExc.setStatus("current")
_AcdPaaResultOneWayDvPrevValid_Type = TruthValue
_AcdPaaResultOneWayDvPrevValid_Object = MibTableColumn
acdPaaResultOneWayDvPrevValid = _AcdPaaResultOneWayDvPrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 17),
    _AcdPaaResultOneWayDvPrevValid_Type()
)
acdPaaResultOneWayDvPrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvPrevValid.setStatus("current")
_AcdPaaResultOneWayDvPrevMinValue_Type = Integer32
_AcdPaaResultOneWayDvPrevMinValue_Object = MibTableColumn
acdPaaResultOneWayDvPrevMinValue = _AcdPaaResultOneWayDvPrevMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 18),
    _AcdPaaResultOneWayDvPrevMinValue_Type()
)
acdPaaResultOneWayDvPrevMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvPrevMinValue.setStatus("current")
_AcdPaaResultOneWayDvPrevMaxValue_Type = Integer32
_AcdPaaResultOneWayDvPrevMaxValue_Object = MibTableColumn
acdPaaResultOneWayDvPrevMaxValue = _AcdPaaResultOneWayDvPrevMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 19),
    _AcdPaaResultOneWayDvPrevMaxValue_Type()
)
acdPaaResultOneWayDvPrevMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvPrevMaxValue.setStatus("current")
_AcdPaaResultOneWayDvPrevAvgValue_Type = Integer32
_AcdPaaResultOneWayDvPrevAvgValue_Object = MibTableColumn
acdPaaResultOneWayDvPrevAvgValue = _AcdPaaResultOneWayDvPrevAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 20),
    _AcdPaaResultOneWayDvPrevAvgValue_Type()
)
acdPaaResultOneWayDvPrevAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvPrevAvgValue.setStatus("current")
_AcdPaaResultOneWayDvPrevThreshEx_Type = Unsigned32
_AcdPaaResultOneWayDvPrevThreshEx_Object = MibTableColumn
acdPaaResultOneWayDvPrevThreshEx = _AcdPaaResultOneWayDvPrevThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 21),
    _AcdPaaResultOneWayDvPrevThreshEx_Type()
)
acdPaaResultOneWayDvPrevThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvPrevThreshEx.setStatus("current")
_AcdPaaResultTwoWayDelayInstValue_Type = Integer32
_AcdPaaResultTwoWayDelayInstValue_Object = MibTableColumn
acdPaaResultTwoWayDelayInstValue = _AcdPaaResultTwoWayDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 22),
    _AcdPaaResultTwoWayDelayInstValue_Type()
)
acdPaaResultTwoWayDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayInstValue.setStatus("current")
_AcdPaaResultTwoWayDelayCurrValid_Type = TruthValue
_AcdPaaResultTwoWayDelayCurrValid_Object = MibTableColumn
acdPaaResultTwoWayDelayCurrValid = _AcdPaaResultTwoWayDelayCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 23),
    _AcdPaaResultTwoWayDelayCurrValid_Type()
)
acdPaaResultTwoWayDelayCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayCurrValid.setStatus("current")
_AcdPaaResultTwoWayDelayCurrMinValue_Type = Integer32
_AcdPaaResultTwoWayDelayCurrMinValue_Object = MibTableColumn
acdPaaResultTwoWayDelayCurrMinValue = _AcdPaaResultTwoWayDelayCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 24),
    _AcdPaaResultTwoWayDelayCurrMinValue_Type()
)
acdPaaResultTwoWayDelayCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayCurrMinValue.setStatus("current")
_AcdPaaResultTwoWayDelayCurrMaxValue_Type = Integer32
_AcdPaaResultTwoWayDelayCurrMaxValue_Object = MibTableColumn
acdPaaResultTwoWayDelayCurrMaxValue = _AcdPaaResultTwoWayDelayCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 25),
    _AcdPaaResultTwoWayDelayCurrMaxValue_Type()
)
acdPaaResultTwoWayDelayCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayCurrMaxValue.setStatus("current")
_AcdPaaResultTwoWayDelayCurrAvgValue_Type = Integer32
_AcdPaaResultTwoWayDelayCurrAvgValue_Object = MibTableColumn
acdPaaResultTwoWayDelayCurrAvgValue = _AcdPaaResultTwoWayDelayCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 26),
    _AcdPaaResultTwoWayDelayCurrAvgValue_Type()
)
acdPaaResultTwoWayDelayCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayCurrAvgValue.setStatus("current")
_AcdPaaResultTwoWayDelayCurrThreshEx_Type = Unsigned32
_AcdPaaResultTwoWayDelayCurrThreshEx_Object = MibTableColumn
acdPaaResultTwoWayDelayCurrThreshEx = _AcdPaaResultTwoWayDelayCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 27),
    _AcdPaaResultTwoWayDelayCurrThreshEx_Type()
)
acdPaaResultTwoWayDelayCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayCurrThreshEx.setStatus("current")
_AcdPaaResultTwoWayDelayPrevValid_Type = TruthValue
_AcdPaaResultTwoWayDelayPrevValid_Object = MibTableColumn
acdPaaResultTwoWayDelayPrevValid = _AcdPaaResultTwoWayDelayPrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 28),
    _AcdPaaResultTwoWayDelayPrevValid_Type()
)
acdPaaResultTwoWayDelayPrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayPrevValid.setStatus("current")
_AcdPaaResultTwoWayDelayPrevMinValue_Type = Integer32
_AcdPaaResultTwoWayDelayPrevMinValue_Object = MibTableColumn
acdPaaResultTwoWayDelayPrevMinValue = _AcdPaaResultTwoWayDelayPrevMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 29),
    _AcdPaaResultTwoWayDelayPrevMinValue_Type()
)
acdPaaResultTwoWayDelayPrevMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayPrevMinValue.setStatus("current")
_AcdPaaResultTwoWayDelayPrevMaxValue_Type = Integer32
_AcdPaaResultTwoWayDelayPrevMaxValue_Object = MibTableColumn
acdPaaResultTwoWayDelayPrevMaxValue = _AcdPaaResultTwoWayDelayPrevMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 30),
    _AcdPaaResultTwoWayDelayPrevMaxValue_Type()
)
acdPaaResultTwoWayDelayPrevMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayPrevMaxValue.setStatus("current")
_AcdPaaResultTwoWayDelayPrevAvgValue_Type = Integer32
_AcdPaaResultTwoWayDelayPrevAvgValue_Object = MibTableColumn
acdPaaResultTwoWayDelayPrevAvgValue = _AcdPaaResultTwoWayDelayPrevAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 31),
    _AcdPaaResultTwoWayDelayPrevAvgValue_Type()
)
acdPaaResultTwoWayDelayPrevAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayPrevAvgValue.setStatus("current")
_AcdPaaResultTwoWayDelayPrevThreshEx_Type = Unsigned32
_AcdPaaResultTwoWayDelayPrevThreshEx_Object = MibTableColumn
acdPaaResultTwoWayDelayPrevThreshEx = _AcdPaaResultTwoWayDelayPrevThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 32),
    _AcdPaaResultTwoWayDelayPrevThreshEx_Type()
)
acdPaaResultTwoWayDelayPrevThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayPrevThreshEx.setStatus("current")
_AcdPaaResultTwoWayDvInstValue_Type = Integer32
_AcdPaaResultTwoWayDvInstValue_Object = MibTableColumn
acdPaaResultTwoWayDvInstValue = _AcdPaaResultTwoWayDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 33),
    _AcdPaaResultTwoWayDvInstValue_Type()
)
acdPaaResultTwoWayDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvInstValue.setStatus("current")
_AcdPaaResultTwoWayDvCurrValid_Type = TruthValue
_AcdPaaResultTwoWayDvCurrValid_Object = MibTableColumn
acdPaaResultTwoWayDvCurrValid = _AcdPaaResultTwoWayDvCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 34),
    _AcdPaaResultTwoWayDvCurrValid_Type()
)
acdPaaResultTwoWayDvCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvCurrValid.setStatus("current")
_AcdPaaResultTwoWayDvCurrMinValue_Type = Integer32
_AcdPaaResultTwoWayDvCurrMinValue_Object = MibTableColumn
acdPaaResultTwoWayDvCurrMinValue = _AcdPaaResultTwoWayDvCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 35),
    _AcdPaaResultTwoWayDvCurrMinValue_Type()
)
acdPaaResultTwoWayDvCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvCurrMinValue.setStatus("current")
_AcdPaaResultTwoWayDvCurrMaxValue_Type = Integer32
_AcdPaaResultTwoWayDvCurrMaxValue_Object = MibTableColumn
acdPaaResultTwoWayDvCurrMaxValue = _AcdPaaResultTwoWayDvCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 36),
    _AcdPaaResultTwoWayDvCurrMaxValue_Type()
)
acdPaaResultTwoWayDvCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvCurrMaxValue.setStatus("current")
_AcdPaaResultTwoWayDvCurrAvgValue_Type = Integer32
_AcdPaaResultTwoWayDvCurrAvgValue_Object = MibTableColumn
acdPaaResultTwoWayDvCurrAvgValue = _AcdPaaResultTwoWayDvCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 37),
    _AcdPaaResultTwoWayDvCurrAvgValue_Type()
)
acdPaaResultTwoWayDvCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvCurrAvgValue.setStatus("current")
_AcdPaaResultTwoWayDvCurrThreshEx_Type = Unsigned32
_AcdPaaResultTwoWayDvCurrThreshEx_Object = MibTableColumn
acdPaaResultTwoWayDvCurrThreshEx = _AcdPaaResultTwoWayDvCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 38),
    _AcdPaaResultTwoWayDvCurrThreshEx_Type()
)
acdPaaResultTwoWayDvCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvCurrThreshEx.setStatus("current")
_AcdPaaResultTwoWayDvPrevValid_Type = TruthValue
_AcdPaaResultTwoWayDvPrevValid_Object = MibTableColumn
acdPaaResultTwoWayDvPrevValid = _AcdPaaResultTwoWayDvPrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 39),
    _AcdPaaResultTwoWayDvPrevValid_Type()
)
acdPaaResultTwoWayDvPrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvPrevValid.setStatus("current")
_AcdPaaResultTwoWayDvPrevMinValue_Type = Integer32
_AcdPaaResultTwoWayDvPrevMinValue_Object = MibTableColumn
acdPaaResultTwoWayDvPrevMinValue = _AcdPaaResultTwoWayDvPrevMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 40),
    _AcdPaaResultTwoWayDvPrevMinValue_Type()
)
acdPaaResultTwoWayDvPrevMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvPrevMinValue.setStatus("current")
_AcdPaaResultTwoWayDvPrevMaxValue_Type = Integer32
_AcdPaaResultTwoWayDvPrevMaxValue_Object = MibTableColumn
acdPaaResultTwoWayDvPrevMaxValue = _AcdPaaResultTwoWayDvPrevMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 41),
    _AcdPaaResultTwoWayDvPrevMaxValue_Type()
)
acdPaaResultTwoWayDvPrevMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvPrevMaxValue.setStatus("current")
_AcdPaaResultTwoWayDvPrevAvgValue_Type = Integer32
_AcdPaaResultTwoWayDvPrevAvgValue_Object = MibTableColumn
acdPaaResultTwoWayDvPrevAvgValue = _AcdPaaResultTwoWayDvPrevAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 42),
    _AcdPaaResultTwoWayDvPrevAvgValue_Type()
)
acdPaaResultTwoWayDvPrevAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvPrevAvgValue.setStatus("current")
_AcdPaaResultTwoWayDvPrevThreshEx_Type = Unsigned32
_AcdPaaResultTwoWayDvPrevThreshEx_Object = MibTableColumn
acdPaaResultTwoWayDvPrevThreshEx = _AcdPaaResultTwoWayDvPrevThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 43),
    _AcdPaaResultTwoWayDvPrevThreshEx_Type()
)
acdPaaResultTwoWayDvPrevThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvPrevThreshEx.setStatus("current")
_AcdPaaResultOneWayDelayInstValue_Type = Integer32
_AcdPaaResultOneWayDelayInstValue_Object = MibTableColumn
acdPaaResultOneWayDelayInstValue = _AcdPaaResultOneWayDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 44),
    _AcdPaaResultOneWayDelayInstValue_Type()
)
acdPaaResultOneWayDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayInstValue.setStatus("current")
_AcdPaaResultOneWayDelayCurrValid_Type = TruthValue
_AcdPaaResultOneWayDelayCurrValid_Object = MibTableColumn
acdPaaResultOneWayDelayCurrValid = _AcdPaaResultOneWayDelayCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 45),
    _AcdPaaResultOneWayDelayCurrValid_Type()
)
acdPaaResultOneWayDelayCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayCurrValid.setStatus("current")
_AcdPaaResultOneWayDelayCurrMinValue_Type = Integer32
_AcdPaaResultOneWayDelayCurrMinValue_Object = MibTableColumn
acdPaaResultOneWayDelayCurrMinValue = _AcdPaaResultOneWayDelayCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 46),
    _AcdPaaResultOneWayDelayCurrMinValue_Type()
)
acdPaaResultOneWayDelayCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayCurrMinValue.setStatus("current")
_AcdPaaResultOneWayDelayCurrMaxValue_Type = Integer32
_AcdPaaResultOneWayDelayCurrMaxValue_Object = MibTableColumn
acdPaaResultOneWayDelayCurrMaxValue = _AcdPaaResultOneWayDelayCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 47),
    _AcdPaaResultOneWayDelayCurrMaxValue_Type()
)
acdPaaResultOneWayDelayCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayCurrMaxValue.setStatus("current")
_AcdPaaResultOneWayDelayCurrAvgValue_Type = Integer32
_AcdPaaResultOneWayDelayCurrAvgValue_Object = MibTableColumn
acdPaaResultOneWayDelayCurrAvgValue = _AcdPaaResultOneWayDelayCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 48),
    _AcdPaaResultOneWayDelayCurrAvgValue_Type()
)
acdPaaResultOneWayDelayCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayCurrAvgValue.setStatus("current")
_AcdPaaResultOneWayDelayCurrThreshEx_Type = Unsigned32
_AcdPaaResultOneWayDelayCurrThreshEx_Object = MibTableColumn
acdPaaResultOneWayDelayCurrThreshEx = _AcdPaaResultOneWayDelayCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 49),
    _AcdPaaResultOneWayDelayCurrThreshEx_Type()
)
acdPaaResultOneWayDelayCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayCurrThreshEx.setStatus("current")
_AcdPaaResultOneWayDelayPrevValid_Type = TruthValue
_AcdPaaResultOneWayDelayPrevValid_Object = MibTableColumn
acdPaaResultOneWayDelayPrevValid = _AcdPaaResultOneWayDelayPrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 50),
    _AcdPaaResultOneWayDelayPrevValid_Type()
)
acdPaaResultOneWayDelayPrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayPrevValid.setStatus("current")
_AcdPaaResultOneWayDelayPrevMinValue_Type = Integer32
_AcdPaaResultOneWayDelayPrevMinValue_Object = MibTableColumn
acdPaaResultOneWayDelayPrevMinValue = _AcdPaaResultOneWayDelayPrevMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 51),
    _AcdPaaResultOneWayDelayPrevMinValue_Type()
)
acdPaaResultOneWayDelayPrevMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayPrevMinValue.setStatus("current")
_AcdPaaResultOneWayDelayPrevMaxValue_Type = Integer32
_AcdPaaResultOneWayDelayPrevMaxValue_Object = MibTableColumn
acdPaaResultOneWayDelayPrevMaxValue = _AcdPaaResultOneWayDelayPrevMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 52),
    _AcdPaaResultOneWayDelayPrevMaxValue_Type()
)
acdPaaResultOneWayDelayPrevMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayPrevMaxValue.setStatus("current")
_AcdPaaResultOneWayDelayPrevAvgValue_Type = Integer32
_AcdPaaResultOneWayDelayPrevAvgValue_Object = MibTableColumn
acdPaaResultOneWayDelayPrevAvgValue = _AcdPaaResultOneWayDelayPrevAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 53),
    _AcdPaaResultOneWayDelayPrevAvgValue_Type()
)
acdPaaResultOneWayDelayPrevAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayPrevAvgValue.setStatus("current")
_AcdPaaResultOneWayDelayPrevThreshEx_Type = Unsigned32
_AcdPaaResultOneWayDelayPrevThreshEx_Object = MibTableColumn
acdPaaResultOneWayDelayPrevThreshEx = _AcdPaaResultOneWayDelayPrevThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 54),
    _AcdPaaResultOneWayDelayPrevThreshEx_Type()
)
acdPaaResultOneWayDelayPrevThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayPrevThreshEx.setStatus("current")
_AcdPaaResultPktLossTime_Type = DateAndTime
_AcdPaaResultPktLossTime_Object = MibTableColumn
acdPaaResultPktLossTime = _AcdPaaResultPktLossTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 55),
    _AcdPaaResultPktLossTime_Type()
)
acdPaaResultPktLossTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossTime.setStatus("current")
_AcdPaaResultOneWayTime_Type = DateAndTime
_AcdPaaResultOneWayTime_Object = MibTableColumn
acdPaaResultOneWayTime = _AcdPaaResultOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 56),
    _AcdPaaResultOneWayTime_Type()
)
acdPaaResultOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayTime.setStatus("current")
_AcdPaaResultTwoWayTime_Type = DateAndTime
_AcdPaaResultTwoWayTime_Object = MibTableColumn
acdPaaResultTwoWayTime = _AcdPaaResultTwoWayTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 57),
    _AcdPaaResultTwoWayTime_Type()
)
acdPaaResultTwoWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayTime.setStatus("current")
_AcdPaaResultPktLossNeCurrSamples_Type = Unsigned32
_AcdPaaResultPktLossNeCurrSamples_Object = MibTableColumn
acdPaaResultPktLossNeCurrSamples = _AcdPaaResultPktLossNeCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 58),
    _AcdPaaResultPktLossNeCurrSamples_Type()
)
acdPaaResultPktLossNeCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNeCurrSamples.setStatus("current")
_AcdPaaResultPktLossNePrevSamples_Type = Unsigned32
_AcdPaaResultPktLossNePrevSamples_Object = MibTableColumn
acdPaaResultPktLossNePrevSamples = _AcdPaaResultPktLossNePrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 59),
    _AcdPaaResultPktLossNePrevSamples_Type()
)
acdPaaResultPktLossNePrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNePrevSamples.setStatus("current")
_AcdPaaResultPktLossFeCurrSamples_Type = Unsigned32
_AcdPaaResultPktLossFeCurrSamples_Object = MibTableColumn
acdPaaResultPktLossFeCurrSamples = _AcdPaaResultPktLossFeCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 60),
    _AcdPaaResultPktLossFeCurrSamples_Type()
)
acdPaaResultPktLossFeCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFeCurrSamples.setStatus("current")
_AcdPaaResultPktLossFePrevSamples_Type = Unsigned32
_AcdPaaResultPktLossFePrevSamples_Object = MibTableColumn
acdPaaResultPktLossFePrevSamples = _AcdPaaResultPktLossFePrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 61),
    _AcdPaaResultPktLossFePrevSamples_Type()
)
acdPaaResultPktLossFePrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFePrevSamples.setStatus("current")
_AcdPaaResultOneWayDelayCurrSamples_Type = Unsigned32
_AcdPaaResultOneWayDelayCurrSamples_Object = MibTableColumn
acdPaaResultOneWayDelayCurrSamples = _AcdPaaResultOneWayDelayCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 62),
    _AcdPaaResultOneWayDelayCurrSamples_Type()
)
acdPaaResultOneWayDelayCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayCurrSamples.setStatus("current")
_AcdPaaResultOneWayDelayPrevSamples_Type = Unsigned32
_AcdPaaResultOneWayDelayPrevSamples_Object = MibTableColumn
acdPaaResultOneWayDelayPrevSamples = _AcdPaaResultOneWayDelayPrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 63),
    _AcdPaaResultOneWayDelayPrevSamples_Type()
)
acdPaaResultOneWayDelayPrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDelayPrevSamples.setStatus("current")
_AcdPaaResultOneWayDvCurrSamples_Type = Unsigned32
_AcdPaaResultOneWayDvCurrSamples_Object = MibTableColumn
acdPaaResultOneWayDvCurrSamples = _AcdPaaResultOneWayDvCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 64),
    _AcdPaaResultOneWayDvCurrSamples_Type()
)
acdPaaResultOneWayDvCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvCurrSamples.setStatus("current")
_AcdPaaResultOneWayDvPrevSamples_Type = Unsigned32
_AcdPaaResultOneWayDvPrevSamples_Object = MibTableColumn
acdPaaResultOneWayDvPrevSamples = _AcdPaaResultOneWayDvPrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 65),
    _AcdPaaResultOneWayDvPrevSamples_Type()
)
acdPaaResultOneWayDvPrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultOneWayDvPrevSamples.setStatus("current")
_AcdPaaResultTwoWayDelayCurrSamples_Type = Unsigned32
_AcdPaaResultTwoWayDelayCurrSamples_Object = MibTableColumn
acdPaaResultTwoWayDelayCurrSamples = _AcdPaaResultTwoWayDelayCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 66),
    _AcdPaaResultTwoWayDelayCurrSamples_Type()
)
acdPaaResultTwoWayDelayCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayCurrSamples.setStatus("current")
_AcdPaaResultTwoWayDelayPrevSamples_Type = Unsigned32
_AcdPaaResultTwoWayDelayPrevSamples_Object = MibTableColumn
acdPaaResultTwoWayDelayPrevSamples = _AcdPaaResultTwoWayDelayPrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 67),
    _AcdPaaResultTwoWayDelayPrevSamples_Type()
)
acdPaaResultTwoWayDelayPrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDelayPrevSamples.setStatus("current")
_AcdPaaResultTwoWayDvCurrSamples_Type = Unsigned32
_AcdPaaResultTwoWayDvCurrSamples_Object = MibTableColumn
acdPaaResultTwoWayDvCurrSamples = _AcdPaaResultTwoWayDvCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 68),
    _AcdPaaResultTwoWayDvCurrSamples_Type()
)
acdPaaResultTwoWayDvCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvCurrSamples.setStatus("current")
_AcdPaaResultTwoWayDvPrevSamples_Type = Unsigned32
_AcdPaaResultTwoWayDvPrevSamples_Object = MibTableColumn
acdPaaResultTwoWayDvPrevSamples = _AcdPaaResultTwoWayDvPrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 69),
    _AcdPaaResultTwoWayDvPrevSamples_Type()
)
acdPaaResultTwoWayDvPrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultTwoWayDvPrevSamples.setStatus("current")
_AcdPaaResultIgmpJoinDelayInstValue_Type = Integer32
_AcdPaaResultIgmpJoinDelayInstValue_Object = MibTableColumn
acdPaaResultIgmpJoinDelayInstValue = _AcdPaaResultIgmpJoinDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 70),
    _AcdPaaResultIgmpJoinDelayInstValue_Type()
)
acdPaaResultIgmpJoinDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayInstValue.setStatus("current")
_AcdPaaResultIgmpJoinDelayCurrValid_Type = TruthValue
_AcdPaaResultIgmpJoinDelayCurrValid_Object = MibTableColumn
acdPaaResultIgmpJoinDelayCurrValid = _AcdPaaResultIgmpJoinDelayCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 71),
    _AcdPaaResultIgmpJoinDelayCurrValid_Type()
)
acdPaaResultIgmpJoinDelayCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayCurrValid.setStatus("current")
_AcdPaaResultIgmpJoinDelayCurrMinValue_Type = Integer32
_AcdPaaResultIgmpJoinDelayCurrMinValue_Object = MibTableColumn
acdPaaResultIgmpJoinDelayCurrMinValue = _AcdPaaResultIgmpJoinDelayCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 72),
    _AcdPaaResultIgmpJoinDelayCurrMinValue_Type()
)
acdPaaResultIgmpJoinDelayCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayCurrMinValue.setStatus("current")
_AcdPaaResultIgmpJoinDelayCurrMaxValue_Type = Integer32
_AcdPaaResultIgmpJoinDelayCurrMaxValue_Object = MibTableColumn
acdPaaResultIgmpJoinDelayCurrMaxValue = _AcdPaaResultIgmpJoinDelayCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 73),
    _AcdPaaResultIgmpJoinDelayCurrMaxValue_Type()
)
acdPaaResultIgmpJoinDelayCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayCurrMaxValue.setStatus("current")
_AcdPaaResultIgmpJoinDelayCurrAvgValue_Type = Integer32
_AcdPaaResultIgmpJoinDelayCurrAvgValue_Object = MibTableColumn
acdPaaResultIgmpJoinDelayCurrAvgValue = _AcdPaaResultIgmpJoinDelayCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 74),
    _AcdPaaResultIgmpJoinDelayCurrAvgValue_Type()
)
acdPaaResultIgmpJoinDelayCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayCurrAvgValue.setStatus("current")
_AcdPaaResultIgmpJoinDelayCurrThreshEx_Type = Unsigned32
_AcdPaaResultIgmpJoinDelayCurrThreshEx_Object = MibTableColumn
acdPaaResultIgmpJoinDelayCurrThreshEx = _AcdPaaResultIgmpJoinDelayCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 75),
    _AcdPaaResultIgmpJoinDelayCurrThreshEx_Type()
)
acdPaaResultIgmpJoinDelayCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayCurrThreshEx.setStatus("current")
_AcdPaaResultIgmpJoinDelayPrevValid_Type = TruthValue
_AcdPaaResultIgmpJoinDelayPrevValid_Object = MibTableColumn
acdPaaResultIgmpJoinDelayPrevValid = _AcdPaaResultIgmpJoinDelayPrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 76),
    _AcdPaaResultIgmpJoinDelayPrevValid_Type()
)
acdPaaResultIgmpJoinDelayPrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayPrevValid.setStatus("current")
_AcdPaaResultIgmpJoinDelayPrevMinValue_Type = Integer32
_AcdPaaResultIgmpJoinDelayPrevMinValue_Object = MibTableColumn
acdPaaResultIgmpJoinDelayPrevMinValue = _AcdPaaResultIgmpJoinDelayPrevMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 77),
    _AcdPaaResultIgmpJoinDelayPrevMinValue_Type()
)
acdPaaResultIgmpJoinDelayPrevMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayPrevMinValue.setStatus("current")
_AcdPaaResultIgmpJoinDelayPrevMaxValue_Type = Integer32
_AcdPaaResultIgmpJoinDelayPrevMaxValue_Object = MibTableColumn
acdPaaResultIgmpJoinDelayPrevMaxValue = _AcdPaaResultIgmpJoinDelayPrevMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 78),
    _AcdPaaResultIgmpJoinDelayPrevMaxValue_Type()
)
acdPaaResultIgmpJoinDelayPrevMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayPrevMaxValue.setStatus("current")
_AcdPaaResultIgmpJoinDelayPrevAvgValue_Type = Integer32
_AcdPaaResultIgmpJoinDelayPrevAvgValue_Object = MibTableColumn
acdPaaResultIgmpJoinDelayPrevAvgValue = _AcdPaaResultIgmpJoinDelayPrevAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 79),
    _AcdPaaResultIgmpJoinDelayPrevAvgValue_Type()
)
acdPaaResultIgmpJoinDelayPrevAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayPrevAvgValue.setStatus("current")
_AcdPaaResultIgmpJoinDelayPrevThreshEx_Type = Unsigned32
_AcdPaaResultIgmpJoinDelayPrevThreshEx_Object = MibTableColumn
acdPaaResultIgmpJoinDelayPrevThreshEx = _AcdPaaResultIgmpJoinDelayPrevThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 80),
    _AcdPaaResultIgmpJoinDelayPrevThreshEx_Type()
)
acdPaaResultIgmpJoinDelayPrevThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayPrevThreshEx.setStatus("current")
_AcdPaaResultIgmpLeaveDelayInstValue_Type = Integer32
_AcdPaaResultIgmpLeaveDelayInstValue_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayInstValue = _AcdPaaResultIgmpLeaveDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 81),
    _AcdPaaResultIgmpLeaveDelayInstValue_Type()
)
acdPaaResultIgmpLeaveDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayInstValue.setStatus("current")
_AcdPaaResultIgmpLeaveDelayCurrValid_Type = TruthValue
_AcdPaaResultIgmpLeaveDelayCurrValid_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayCurrValid = _AcdPaaResultIgmpLeaveDelayCurrValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 82),
    _AcdPaaResultIgmpLeaveDelayCurrValid_Type()
)
acdPaaResultIgmpLeaveDelayCurrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayCurrValid.setStatus("current")
_AcdPaaResultIgmpLeaveDelayCurrMinValue_Type = Integer32
_AcdPaaResultIgmpLeaveDelayCurrMinValue_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayCurrMinValue = _AcdPaaResultIgmpLeaveDelayCurrMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 83),
    _AcdPaaResultIgmpLeaveDelayCurrMinValue_Type()
)
acdPaaResultIgmpLeaveDelayCurrMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayCurrMinValue.setStatus("current")
_AcdPaaResultIgmpLeaveDelayCurrMaxValue_Type = Integer32
_AcdPaaResultIgmpLeaveDelayCurrMaxValue_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayCurrMaxValue = _AcdPaaResultIgmpLeaveDelayCurrMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 84),
    _AcdPaaResultIgmpLeaveDelayCurrMaxValue_Type()
)
acdPaaResultIgmpLeaveDelayCurrMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayCurrMaxValue.setStatus("current")
_AcdPaaResultIgmpLeaveDelayCurrAvgValue_Type = Integer32
_AcdPaaResultIgmpLeaveDelayCurrAvgValue_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayCurrAvgValue = _AcdPaaResultIgmpLeaveDelayCurrAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 85),
    _AcdPaaResultIgmpLeaveDelayCurrAvgValue_Type()
)
acdPaaResultIgmpLeaveDelayCurrAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayCurrAvgValue.setStatus("current")
_AcdPaaResultIgmpLeaveDelayCurrThreshEx_Type = Unsigned32
_AcdPaaResultIgmpLeaveDelayCurrThreshEx_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayCurrThreshEx = _AcdPaaResultIgmpLeaveDelayCurrThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 86),
    _AcdPaaResultIgmpLeaveDelayCurrThreshEx_Type()
)
acdPaaResultIgmpLeaveDelayCurrThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayCurrThreshEx.setStatus("current")
_AcdPaaResultIgmpLeaveDelayPrevValid_Type = TruthValue
_AcdPaaResultIgmpLeaveDelayPrevValid_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayPrevValid = _AcdPaaResultIgmpLeaveDelayPrevValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 87),
    _AcdPaaResultIgmpLeaveDelayPrevValid_Type()
)
acdPaaResultIgmpLeaveDelayPrevValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayPrevValid.setStatus("current")
_AcdPaaResultIgmpLeaveDelayPrevMinValue_Type = Integer32
_AcdPaaResultIgmpLeaveDelayPrevMinValue_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayPrevMinValue = _AcdPaaResultIgmpLeaveDelayPrevMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 88),
    _AcdPaaResultIgmpLeaveDelayPrevMinValue_Type()
)
acdPaaResultIgmpLeaveDelayPrevMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayPrevMinValue.setStatus("current")
_AcdPaaResultIgmpLeaveDelayPrevMaxValue_Type = Integer32
_AcdPaaResultIgmpLeaveDelayPrevMaxValue_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayPrevMaxValue = _AcdPaaResultIgmpLeaveDelayPrevMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 89),
    _AcdPaaResultIgmpLeaveDelayPrevMaxValue_Type()
)
acdPaaResultIgmpLeaveDelayPrevMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayPrevMaxValue.setStatus("current")
_AcdPaaResultIgmpLeaveDelayPrevAvgValue_Type = Integer32
_AcdPaaResultIgmpLeaveDelayPrevAvgValue_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayPrevAvgValue = _AcdPaaResultIgmpLeaveDelayPrevAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 90),
    _AcdPaaResultIgmpLeaveDelayPrevAvgValue_Type()
)
acdPaaResultIgmpLeaveDelayPrevAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayPrevAvgValue.setStatus("current")
_AcdPaaResultIgmpLeaveDelayPrevThreshEx_Type = Unsigned32
_AcdPaaResultIgmpLeaveDelayPrevThreshEx_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayPrevThreshEx = _AcdPaaResultIgmpLeaveDelayPrevThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 91),
    _AcdPaaResultIgmpLeaveDelayPrevThreshEx_Type()
)
acdPaaResultIgmpLeaveDelayPrevThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayPrevThreshEx.setStatus("current")
_AcdPaaResultIgmpJoinDelayTime_Type = DateAndTime
_AcdPaaResultIgmpJoinDelayTime_Object = MibTableColumn
acdPaaResultIgmpJoinDelayTime = _AcdPaaResultIgmpJoinDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 92),
    _AcdPaaResultIgmpJoinDelayTime_Type()
)
acdPaaResultIgmpJoinDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayTime.setStatus("current")
_AcdPaaResultIgmpLeaveDelayTime_Type = DateAndTime
_AcdPaaResultIgmpLeaveDelayTime_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayTime = _AcdPaaResultIgmpLeaveDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 93),
    _AcdPaaResultIgmpLeaveDelayTime_Type()
)
acdPaaResultIgmpLeaveDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayTime.setStatus("current")
_AcdPaaResultIgmpJoinDelayCurrSamples_Type = Unsigned32
_AcdPaaResultIgmpJoinDelayCurrSamples_Object = MibTableColumn
acdPaaResultIgmpJoinDelayCurrSamples = _AcdPaaResultIgmpJoinDelayCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 94),
    _AcdPaaResultIgmpJoinDelayCurrSamples_Type()
)
acdPaaResultIgmpJoinDelayCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayCurrSamples.setStatus("current")
_AcdPaaResultIgmpJoinDelayPrevSamples_Type = Unsigned32
_AcdPaaResultIgmpJoinDelayPrevSamples_Object = MibTableColumn
acdPaaResultIgmpJoinDelayPrevSamples = _AcdPaaResultIgmpJoinDelayPrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 95),
    _AcdPaaResultIgmpJoinDelayPrevSamples_Type()
)
acdPaaResultIgmpJoinDelayPrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpJoinDelayPrevSamples.setStatus("current")
_AcdPaaResultIgmpLeaveDelayCurrSamples_Type = Unsigned32
_AcdPaaResultIgmpLeaveDelayCurrSamples_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayCurrSamples = _AcdPaaResultIgmpLeaveDelayCurrSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 96),
    _AcdPaaResultIgmpLeaveDelayCurrSamples_Type()
)
acdPaaResultIgmpLeaveDelayCurrSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayCurrSamples.setStatus("current")
_AcdPaaResultIgmpLeaveDelayPrevSamples_Type = Unsigned32
_AcdPaaResultIgmpLeaveDelayPrevSamples_Object = MibTableColumn
acdPaaResultIgmpLeaveDelayPrevSamples = _AcdPaaResultIgmpLeaveDelayPrevSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 97),
    _AcdPaaResultIgmpLeaveDelayPrevSamples_Type()
)
acdPaaResultIgmpLeaveDelayPrevSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultIgmpLeaveDelayPrevSamples.setStatus("current")
_AcdPaaResultPktLossCurrGaps_Type = Unsigned32
_AcdPaaResultPktLossCurrGaps_Object = MibTableColumn
acdPaaResultPktLossCurrGaps = _AcdPaaResultPktLossCurrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 98),
    _AcdPaaResultPktLossCurrGaps_Type()
)
acdPaaResultPktLossCurrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossCurrGaps.setStatus("current")
_AcdPaaResultPktLossPrevGaps_Type = Unsigned32
_AcdPaaResultPktLossPrevGaps_Object = MibTableColumn
acdPaaResultPktLossPrevGaps = _AcdPaaResultPktLossPrevGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 99),
    _AcdPaaResultPktLossPrevGaps_Type()
)
acdPaaResultPktLossPrevGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossPrevGaps.setStatus("current")
_AcdPaaResultPktLossCurrLargestGap_Type = Unsigned32
_AcdPaaResultPktLossCurrLargestGap_Object = MibTableColumn
acdPaaResultPktLossCurrLargestGap = _AcdPaaResultPktLossCurrLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 100),
    _AcdPaaResultPktLossCurrLargestGap_Type()
)
acdPaaResultPktLossCurrLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossCurrLargestGap.setStatus("current")
_AcdPaaResultPktLossPrevLargestGap_Type = Unsigned32
_AcdPaaResultPktLossPrevLargestGap_Object = MibTableColumn
acdPaaResultPktLossPrevLargestGap = _AcdPaaResultPktLossPrevLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 101),
    _AcdPaaResultPktLossPrevLargestGap_Type()
)
acdPaaResultPktLossPrevLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossPrevLargestGap.setStatus("current")


class _AcdPaaResultPktLossNeCurrValueExt_Type(Unsigned32):
    """Custom type acdPaaResultPktLossNeCurrValueExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaResultPktLossNeCurrValueExt_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossNeCurrValueExt_Object = MibTableColumn
acdPaaResultPktLossNeCurrValueExt = _AcdPaaResultPktLossNeCurrValueExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 102),
    _AcdPaaResultPktLossNeCurrValueExt_Type()
)
acdPaaResultPktLossNeCurrValueExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNeCurrValueExt.setStatus("current")


class _AcdPaaResultPktLossNePrevValueExt_Type(Unsigned32):
    """Custom type acdPaaResultPktLossNePrevValueExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaResultPktLossNePrevValueExt_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossNePrevValueExt_Object = MibTableColumn
acdPaaResultPktLossNePrevValueExt = _AcdPaaResultPktLossNePrevValueExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 103),
    _AcdPaaResultPktLossNePrevValueExt_Type()
)
acdPaaResultPktLossNePrevValueExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNePrevValueExt.setStatus("current")


class _AcdPaaResultPktLossFeCurrValueExt_Type(Unsigned32):
    """Custom type acdPaaResultPktLossFeCurrValueExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaResultPktLossFeCurrValueExt_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossFeCurrValueExt_Object = MibTableColumn
acdPaaResultPktLossFeCurrValueExt = _AcdPaaResultPktLossFeCurrValueExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 104),
    _AcdPaaResultPktLossFeCurrValueExt_Type()
)
acdPaaResultPktLossFeCurrValueExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFeCurrValueExt.setStatus("current")


class _AcdPaaResultPktLossFePrevValueExt_Type(Unsigned32):
    """Custom type acdPaaResultPktLossFePrevValueExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaResultPktLossFePrevValueExt_Type.__name__ = "Unsigned32"
_AcdPaaResultPktLossFePrevValueExt_Object = MibTableColumn
acdPaaResultPktLossFePrevValueExt = _AcdPaaResultPktLossFePrevValueExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 105),
    _AcdPaaResultPktLossFePrevValueExt_Type()
)
acdPaaResultPktLossFePrevValueExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFePrevValueExt.setStatus("current")
_AcdPaaResultPktLossNeCurrNbrLoss_Type = Unsigned32
_AcdPaaResultPktLossNeCurrNbrLoss_Object = MibTableColumn
acdPaaResultPktLossNeCurrNbrLoss = _AcdPaaResultPktLossNeCurrNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 106),
    _AcdPaaResultPktLossNeCurrNbrLoss_Type()
)
acdPaaResultPktLossNeCurrNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNeCurrNbrLoss.setStatus("current")
_AcdPaaResultPktLossNePrevNbrLoss_Type = Unsigned32
_AcdPaaResultPktLossNePrevNbrLoss_Object = MibTableColumn
acdPaaResultPktLossNePrevNbrLoss = _AcdPaaResultPktLossNePrevNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 107),
    _AcdPaaResultPktLossNePrevNbrLoss_Type()
)
acdPaaResultPktLossNePrevNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossNePrevNbrLoss.setStatus("current")
_AcdPaaResultPktLossFeCurrNbrLoss_Type = Unsigned32
_AcdPaaResultPktLossFeCurrNbrLoss_Object = MibTableColumn
acdPaaResultPktLossFeCurrNbrLoss = _AcdPaaResultPktLossFeCurrNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 108),
    _AcdPaaResultPktLossFeCurrNbrLoss_Type()
)
acdPaaResultPktLossFeCurrNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFeCurrNbrLoss.setStatus("current")
_AcdPaaResultPktLossFePrevNbrLoss_Type = Unsigned32
_AcdPaaResultPktLossFePrevNbrLoss_Object = MibTableColumn
acdPaaResultPktLossFePrevNbrLoss = _AcdPaaResultPktLossFePrevNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 109),
    _AcdPaaResultPktLossFePrevNbrLoss_Type()
)
acdPaaResultPktLossFePrevNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultPktLossFePrevNbrLoss.setStatus("current")
_AcdPaaResultVlan1IdMismatch_Type = Unsigned32
_AcdPaaResultVlan1IdMismatch_Object = MibTableColumn
acdPaaResultVlan1IdMismatch = _AcdPaaResultVlan1IdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 110),
    _AcdPaaResultVlan1IdMismatch_Type()
)
acdPaaResultVlan1IdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan1IdMismatch.setStatus("current")
_AcdPaaResultVlan1IdExpected_Type = Unsigned32
_AcdPaaResultVlan1IdExpected_Object = MibTableColumn
acdPaaResultVlan1IdExpected = _AcdPaaResultVlan1IdExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 111),
    _AcdPaaResultVlan1IdExpected_Type()
)
acdPaaResultVlan1IdExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan1IdExpected.setStatus("current")
_AcdPaaResultVlan1IdReceived_Type = Unsigned32
_AcdPaaResultVlan1IdReceived_Object = MibTableColumn
acdPaaResultVlan1IdReceived = _AcdPaaResultVlan1IdReceived_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 112),
    _AcdPaaResultVlan1IdReceived_Type()
)
acdPaaResultVlan1IdReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan1IdReceived.setStatus("current")
_AcdPaaResultVlan2IdMismatch_Type = Unsigned32
_AcdPaaResultVlan2IdMismatch_Object = MibTableColumn
acdPaaResultVlan2IdMismatch = _AcdPaaResultVlan2IdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 113),
    _AcdPaaResultVlan2IdMismatch_Type()
)
acdPaaResultVlan2IdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan2IdMismatch.setStatus("current")
_AcdPaaResultVlan2IdExpected_Type = Unsigned32
_AcdPaaResultVlan2IdExpected_Object = MibTableColumn
acdPaaResultVlan2IdExpected = _AcdPaaResultVlan2IdExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 114),
    _AcdPaaResultVlan2IdExpected_Type()
)
acdPaaResultVlan2IdExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan2IdExpected.setStatus("current")
_AcdPaaResultVlan2IdReceived_Type = Unsigned32
_AcdPaaResultVlan2IdReceived_Object = MibTableColumn
acdPaaResultVlan2IdReceived = _AcdPaaResultVlan2IdReceived_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 115),
    _AcdPaaResultVlan2IdReceived_Type()
)
acdPaaResultVlan2IdReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan2IdReceived.setStatus("current")
_AcdPaaResultVlan1PriorityMismatch_Type = Unsigned32
_AcdPaaResultVlan1PriorityMismatch_Object = MibTableColumn
acdPaaResultVlan1PriorityMismatch = _AcdPaaResultVlan1PriorityMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 116),
    _AcdPaaResultVlan1PriorityMismatch_Type()
)
acdPaaResultVlan1PriorityMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan1PriorityMismatch.setStatus("current")
_AcdPaaResultVlan1PriorityExpected_Type = Unsigned32
_AcdPaaResultVlan1PriorityExpected_Object = MibTableColumn
acdPaaResultVlan1PriorityExpected = _AcdPaaResultVlan1PriorityExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 117),
    _AcdPaaResultVlan1PriorityExpected_Type()
)
acdPaaResultVlan1PriorityExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan1PriorityExpected.setStatus("current")
_AcdPaaResultVlan1PriorityReceived_Type = Unsigned32
_AcdPaaResultVlan1PriorityReceived_Object = MibTableColumn
acdPaaResultVlan1PriorityReceived = _AcdPaaResultVlan1PriorityReceived_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 118),
    _AcdPaaResultVlan1PriorityReceived_Type()
)
acdPaaResultVlan1PriorityReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan1PriorityReceived.setStatus("current")
_AcdPaaResultVlan2PriorityMismatch_Type = Unsigned32
_AcdPaaResultVlan2PriorityMismatch_Object = MibTableColumn
acdPaaResultVlan2PriorityMismatch = _AcdPaaResultVlan2PriorityMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 119),
    _AcdPaaResultVlan2PriorityMismatch_Type()
)
acdPaaResultVlan2PriorityMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan2PriorityMismatch.setStatus("current")
_AcdPaaResultVlan2PriorityExpected_Type = Unsigned32
_AcdPaaResultVlan2PriorityExpected_Object = MibTableColumn
acdPaaResultVlan2PriorityExpected = _AcdPaaResultVlan2PriorityExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 120),
    _AcdPaaResultVlan2PriorityExpected_Type()
)
acdPaaResultVlan2PriorityExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan2PriorityExpected.setStatus("current")
_AcdPaaResultVlan2PriorityReceived_Type = Unsigned32
_AcdPaaResultVlan2PriorityReceived_Object = MibTableColumn
acdPaaResultVlan2PriorityReceived = _AcdPaaResultVlan2PriorityReceived_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 121),
    _AcdPaaResultVlan2PriorityReceived_Type()
)
acdPaaResultVlan2PriorityReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultVlan2PriorityReceived.setStatus("current")
_AcdPaaResultDscpMismatch_Type = Unsigned32
_AcdPaaResultDscpMismatch_Object = MibTableColumn
acdPaaResultDscpMismatch = _AcdPaaResultDscpMismatch_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 122),
    _AcdPaaResultDscpMismatch_Type()
)
acdPaaResultDscpMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultDscpMismatch.setStatus("current")
_AcdPaaResultDscpExpected_Type = Unsigned32
_AcdPaaResultDscpExpected_Object = MibTableColumn
acdPaaResultDscpExpected = _AcdPaaResultDscpExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 123),
    _AcdPaaResultDscpExpected_Type()
)
acdPaaResultDscpExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultDscpExpected.setStatus("current")
_AcdPaaResultDscpReceived_Type = Unsigned32
_AcdPaaResultDscpReceived_Object = MibTableColumn
acdPaaResultDscpReceived = _AcdPaaResultDscpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 1, 1, 124),
    _AcdPaaResultDscpReceived_Type()
)
acdPaaResultDscpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaResultDscpReceived.setStatus("current")
_AcdPaaStatusTable_Object = MibTable
acdPaaStatusTable = _AcdPaaStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2)
)
if mibBuilder.loadTexts:
    acdPaaStatusTable.setStatus("current")
_AcdPaaStatusEntry_Object = MibTableRow
acdPaaStatusEntry = _AcdPaaStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1)
)
acdPaaStatusEntry.setIndexNames(
    (0, "ACD-PAA-MIB", "acdPaaStatusID"),
)
if mibBuilder.loadTexts:
    acdPaaStatusEntry.setStatus("current")
_AcdPaaStatusID_Type = Unsigned32
_AcdPaaStatusID_Object = MibTableColumn
acdPaaStatusID = _AcdPaaStatusID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 1),
    _AcdPaaStatusID_Type()
)
acdPaaStatusID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPaaStatusID.setStatus("current")
_AcdPaaStatusCcAlert_Type = TruthValue
_AcdPaaStatusCcAlert_Object = MibTableColumn
acdPaaStatusCcAlert = _AcdPaaStatusCcAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 2),
    _AcdPaaStatusCcAlert_Type()
)
acdPaaStatusCcAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusCcAlert.setStatus("current")
_AcdPaaStatusPktLossAlert_Type = TruthValue
_AcdPaaStatusPktLossAlert_Object = MibTableColumn
acdPaaStatusPktLossAlert = _AcdPaaStatusPktLossAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 3),
    _AcdPaaStatusPktLossAlert_Type()
)
acdPaaStatusPktLossAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusPktLossAlert.setStatus("current")
_AcdPaaStatusOneWayDvAlert_Type = TruthValue
_AcdPaaStatusOneWayDvAlert_Object = MibTableColumn
acdPaaStatusOneWayDvAlert = _AcdPaaStatusOneWayDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 4),
    _AcdPaaStatusOneWayDvAlert_Type()
)
acdPaaStatusOneWayDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusOneWayDvAlert.setStatus("current")
_AcdPaaStatusOneWayAvgDvAlert_Type = TruthValue
_AcdPaaStatusOneWayAvgDvAlert_Object = MibTableColumn
acdPaaStatusOneWayAvgDvAlert = _AcdPaaStatusOneWayAvgDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 5),
    _AcdPaaStatusOneWayAvgDvAlert_Type()
)
acdPaaStatusOneWayAvgDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusOneWayAvgDvAlert.setStatus("current")
_AcdPaaStatusTwoWayDelayAlert_Type = TruthValue
_AcdPaaStatusTwoWayDelayAlert_Object = MibTableColumn
acdPaaStatusTwoWayDelayAlert = _AcdPaaStatusTwoWayDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 6),
    _AcdPaaStatusTwoWayDelayAlert_Type()
)
acdPaaStatusTwoWayDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusTwoWayDelayAlert.setStatus("current")
_AcdPaaStatusTwoWayAvgDelayAlert_Type = TruthValue
_AcdPaaStatusTwoWayAvgDelayAlert_Object = MibTableColumn
acdPaaStatusTwoWayAvgDelayAlert = _AcdPaaStatusTwoWayAvgDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 7),
    _AcdPaaStatusTwoWayAvgDelayAlert_Type()
)
acdPaaStatusTwoWayAvgDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusTwoWayAvgDelayAlert.setStatus("current")
_AcdPaaStatusTwoWayDvAlert_Type = TruthValue
_AcdPaaStatusTwoWayDvAlert_Object = MibTableColumn
acdPaaStatusTwoWayDvAlert = _AcdPaaStatusTwoWayDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 8),
    _AcdPaaStatusTwoWayDvAlert_Type()
)
acdPaaStatusTwoWayDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusTwoWayDvAlert.setStatus("current")
_AcdPaaStatusTwoWayAvgDvAlert_Type = TruthValue
_AcdPaaStatusTwoWayAvgDvAlert_Object = MibTableColumn
acdPaaStatusTwoWayAvgDvAlert = _AcdPaaStatusTwoWayAvgDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 9),
    _AcdPaaStatusTwoWayAvgDvAlert_Type()
)
acdPaaStatusTwoWayAvgDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusTwoWayAvgDvAlert.setStatus("current")
_AcdPaaStatusOneWayDelayAlert_Type = TruthValue
_AcdPaaStatusOneWayDelayAlert_Object = MibTableColumn
acdPaaStatusOneWayDelayAlert = _AcdPaaStatusOneWayDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 10),
    _AcdPaaStatusOneWayDelayAlert_Type()
)
acdPaaStatusOneWayDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusOneWayDelayAlert.setStatus("current")
_AcdPaaStatusOneWayAvgDelayAlert_Type = TruthValue
_AcdPaaStatusOneWayAvgDelayAlert_Object = MibTableColumn
acdPaaStatusOneWayAvgDelayAlert = _AcdPaaStatusOneWayAvgDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 11),
    _AcdPaaStatusOneWayAvgDelayAlert_Type()
)
acdPaaStatusOneWayAvgDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusOneWayAvgDelayAlert.setStatus("current")


class _AcdPaaStatusState_Type(Integer32):
    """Custom type acdPaaStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("associated", 2),
          ("associating", 1),
          ("disabled", 0),
          ("idle", 4),
          ("lockedIS", 5),
          ("lockedOOS", 6),
          ("running", 3))
    )


_AcdPaaStatusState_Type.__name__ = "Integer32"
_AcdPaaStatusState_Object = MibTableColumn
acdPaaStatusState = _AcdPaaStatusState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 12),
    _AcdPaaStatusState_Type()
)
acdPaaStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusState.setStatus("current")


class _AcdPaaStatusPeerAddress_Type(DisplayString):
    """Custom type acdPaaStatusPeerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdPaaStatusPeerAddress_Type.__name__ = "DisplayString"
_AcdPaaStatusPeerAddress_Object = MibTableColumn
acdPaaStatusPeerAddress = _AcdPaaStatusPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 2, 1, 13),
    _AcdPaaStatusPeerAddress_Type()
)
acdPaaStatusPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaStatusPeerAddress.setStatus("current")
_AcdPaaUdpCfgTable_Object = MibTable
acdPaaUdpCfgTable = _AcdPaaUdpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3)
)
if mibBuilder.loadTexts:
    acdPaaUdpCfgTable.setStatus("current")
_AcdPaaUdpCfgEntry_Object = MibTableRow
acdPaaUdpCfgEntry = _AcdPaaUdpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1)
)
acdPaaUdpCfgEntry.setIndexNames(
    (0, "ACD-PAA-MIB", "acdPaaUdpCfgID"),
)
if mibBuilder.loadTexts:
    acdPaaUdpCfgEntry.setStatus("current")
_AcdPaaUdpCfgID_Type = Unsigned32
_AcdPaaUdpCfgID_Object = MibTableColumn
acdPaaUdpCfgID = _AcdPaaUdpCfgID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 1),
    _AcdPaaUdpCfgID_Type()
)
acdPaaUdpCfgID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPaaUdpCfgID.setStatus("current")


class _AcdPaaUdpCfgName_Type(DisplayString):
    """Custom type acdPaaUdpCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdPaaUdpCfgName_Type.__name__ = "DisplayString"
_AcdPaaUdpCfgName_Object = MibTableColumn
acdPaaUdpCfgName = _AcdPaaUdpCfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 2),
    _AcdPaaUdpCfgName_Type()
)
acdPaaUdpCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgName.setStatus("current")


class _AcdPaaUdpCfgState_Type(Integer32):
    """Custom type acdPaaUdpCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_AcdPaaUdpCfgState_Type.__name__ = "Integer32"
_AcdPaaUdpCfgState_Object = MibTableColumn
acdPaaUdpCfgState = _AcdPaaUdpCfgState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 3),
    _AcdPaaUdpCfgState_Type()
)
acdPaaUdpCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgState.setStatus("current")
_AcdPaaUdpCfgPktSize_Type = Unsigned32
_AcdPaaUdpCfgPktSize_Object = MibTableColumn
acdPaaUdpCfgPktSize = _AcdPaaUdpCfgPktSize_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 4),
    _AcdPaaUdpCfgPktSize_Type()
)
acdPaaUdpCfgPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgPktSize.setStatus("current")
_AcdPaaUdpCfgSamplingPeriod_Type = Unsigned32
_AcdPaaUdpCfgSamplingPeriod_Object = MibTableColumn
acdPaaUdpCfgSamplingPeriod = _AcdPaaUdpCfgSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 5),
    _AcdPaaUdpCfgSamplingPeriod_Type()
)
acdPaaUdpCfgSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgSamplingPeriod.setStatus("current")
_AcdPaaUdpCfgCcLossThresh_Type = Unsigned32
_AcdPaaUdpCfgCcLossThresh_Object = MibTableColumn
acdPaaUdpCfgCcLossThresh = _AcdPaaUdpCfgCcLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 6),
    _AcdPaaUdpCfgCcLossThresh_Type()
)
acdPaaUdpCfgCcLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgCcLossThresh.setStatus("current")
_AcdPaaUdpCfgPktLossRefPeriod_Type = Unsigned32
_AcdPaaUdpCfgPktLossRefPeriod_Object = MibTableColumn
acdPaaUdpCfgPktLossRefPeriod = _AcdPaaUdpCfgPktLossRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 7),
    _AcdPaaUdpCfgPktLossRefPeriod_Type()
)
acdPaaUdpCfgPktLossRefPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgPktLossRefPeriod.setStatus("current")
_AcdPaaUdpCfgPktLossThresh_Type = Unsigned32
_AcdPaaUdpCfgPktLossThresh_Object = MibTableColumn
acdPaaUdpCfgPktLossThresh = _AcdPaaUdpCfgPktLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 8),
    _AcdPaaUdpCfgPktLossThresh_Type()
)
acdPaaUdpCfgPktLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgPktLossThresh.setStatus("current")
_AcdPaaUdpCfgOneWayRefPeriod_Type = Unsigned32
_AcdPaaUdpCfgOneWayRefPeriod_Object = MibTableColumn
acdPaaUdpCfgOneWayRefPeriod = _AcdPaaUdpCfgOneWayRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 9),
    _AcdPaaUdpCfgOneWayRefPeriod_Type()
)
acdPaaUdpCfgOneWayRefPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOneWayRefPeriod.setStatus("current")
_AcdPaaUdpCfgOneWayDvMax_Type = Unsigned32
_AcdPaaUdpCfgOneWayDvMax_Object = MibTableColumn
acdPaaUdpCfgOneWayDvMax = _AcdPaaUdpCfgOneWayDvMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 10),
    _AcdPaaUdpCfgOneWayDvMax_Type()
)
acdPaaUdpCfgOneWayDvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOneWayDvMax.setStatus("current")
_AcdPaaUdpCfgOneWayDvThresh_Type = Unsigned32
_AcdPaaUdpCfgOneWayDvThresh_Object = MibTableColumn
acdPaaUdpCfgOneWayDvThresh = _AcdPaaUdpCfgOneWayDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 11),
    _AcdPaaUdpCfgOneWayDvThresh_Type()
)
acdPaaUdpCfgOneWayDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOneWayDvThresh.setStatus("current")
_AcdPaaUdpCfgOneWayAvgDvThresh_Type = Unsigned32
_AcdPaaUdpCfgOneWayAvgDvThresh_Object = MibTableColumn
acdPaaUdpCfgOneWayAvgDvThresh = _AcdPaaUdpCfgOneWayAvgDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 12),
    _AcdPaaUdpCfgOneWayAvgDvThresh_Type()
)
acdPaaUdpCfgOneWayAvgDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOneWayAvgDvThresh.setStatus("current")
_AcdPaaUdpCfgTwoWayRefPeriod_Type = Unsigned32
_AcdPaaUdpCfgTwoWayRefPeriod_Object = MibTableColumn
acdPaaUdpCfgTwoWayRefPeriod = _AcdPaaUdpCfgTwoWayRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 13),
    _AcdPaaUdpCfgTwoWayRefPeriod_Type()
)
acdPaaUdpCfgTwoWayRefPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgTwoWayRefPeriod.setStatus("current")
_AcdPaaUdpCfgTwoWayDelayMax_Type = Unsigned32
_AcdPaaUdpCfgTwoWayDelayMax_Object = MibTableColumn
acdPaaUdpCfgTwoWayDelayMax = _AcdPaaUdpCfgTwoWayDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 14),
    _AcdPaaUdpCfgTwoWayDelayMax_Type()
)
acdPaaUdpCfgTwoWayDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgTwoWayDelayMax.setStatus("current")
_AcdPaaUdpCfgTwoWayDelayThresh_Type = Unsigned32
_AcdPaaUdpCfgTwoWayDelayThresh_Object = MibTableColumn
acdPaaUdpCfgTwoWayDelayThresh = _AcdPaaUdpCfgTwoWayDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 15),
    _AcdPaaUdpCfgTwoWayDelayThresh_Type()
)
acdPaaUdpCfgTwoWayDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgTwoWayDelayThresh.setStatus("current")
_AcdPaaUdpCfgTwoWayAvgDelayThresh_Type = Unsigned32
_AcdPaaUdpCfgTwoWayAvgDelayThresh_Object = MibTableColumn
acdPaaUdpCfgTwoWayAvgDelayThresh = _AcdPaaUdpCfgTwoWayAvgDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 16),
    _AcdPaaUdpCfgTwoWayAvgDelayThresh_Type()
)
acdPaaUdpCfgTwoWayAvgDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgTwoWayAvgDelayThresh.setStatus("current")
_AcdPaaUdpCfgTwoWayDvMax_Type = Unsigned32
_AcdPaaUdpCfgTwoWayDvMax_Object = MibTableColumn
acdPaaUdpCfgTwoWayDvMax = _AcdPaaUdpCfgTwoWayDvMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 17),
    _AcdPaaUdpCfgTwoWayDvMax_Type()
)
acdPaaUdpCfgTwoWayDvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgTwoWayDvMax.setStatus("current")
_AcdPaaUdpCfgTwoWayDvThresh_Type = Unsigned32
_AcdPaaUdpCfgTwoWayDvThresh_Object = MibTableColumn
acdPaaUdpCfgTwoWayDvThresh = _AcdPaaUdpCfgTwoWayDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 18),
    _AcdPaaUdpCfgTwoWayDvThresh_Type()
)
acdPaaUdpCfgTwoWayDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgTwoWayDvThresh.setStatus("current")
_AcdPaaUdpCfgTwoWayAvgDvThresh_Type = Unsigned32
_AcdPaaUdpCfgTwoWayAvgDvThresh_Object = MibTableColumn
acdPaaUdpCfgTwoWayAvgDvThresh = _AcdPaaUdpCfgTwoWayAvgDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 19),
    _AcdPaaUdpCfgTwoWayAvgDvThresh_Type()
)
acdPaaUdpCfgTwoWayAvgDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgTwoWayAvgDvThresh.setStatus("current")
_AcdPaaUdpCfgIPv4DstAddr_Type = IpAddress
_AcdPaaUdpCfgIPv4DstAddr_Object = MibTableColumn
acdPaaUdpCfgIPv4DstAddr = _AcdPaaUdpCfgIPv4DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 20),
    _AcdPaaUdpCfgIPv4DstAddr_Type()
)
acdPaaUdpCfgIPv4DstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIPv4DstAddr.setStatus("current")
_AcdPaaUdpCfgPortNumber_Type = Unsigned32
_AcdPaaUdpCfgPortNumber_Object = MibTableColumn
acdPaaUdpCfgPortNumber = _AcdPaaUdpCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 21),
    _AcdPaaUdpCfgPortNumber_Type()
)
acdPaaUdpCfgPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgPortNumber.setStatus("current")
_AcdPaaUdpCfgDscpValue_Type = Unsigned32
_AcdPaaUdpCfgDscpValue_Object = MibTableColumn
acdPaaUdpCfgDscpValue = _AcdPaaUdpCfgDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 22),
    _AcdPaaUdpCfgDscpValue_Type()
)
acdPaaUdpCfgDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgDscpValue.setStatus("current")
_AcdPaaUdpCfgVlan1PbitsValue_Type = Unsigned32
_AcdPaaUdpCfgVlan1PbitsValue_Object = MibTableColumn
acdPaaUdpCfgVlan1PbitsValue = _AcdPaaUdpCfgVlan1PbitsValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 23),
    _AcdPaaUdpCfgVlan1PbitsValue_Type()
)
acdPaaUdpCfgVlan1PbitsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgVlan1PbitsValue.setStatus("current")
_AcdPaaUdpCfgVlan2PbitsValue_Type = Unsigned32
_AcdPaaUdpCfgVlan2PbitsValue_Object = MibTableColumn
acdPaaUdpCfgVlan2PbitsValue = _AcdPaaUdpCfgVlan2PbitsValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 24),
    _AcdPaaUdpCfgVlan2PbitsValue_Type()
)
acdPaaUdpCfgVlan2PbitsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgVlan2PbitsValue.setStatus("current")
_AcdPaaUdpCfgOneWayDelayMax_Type = Unsigned32
_AcdPaaUdpCfgOneWayDelayMax_Object = MibTableColumn
acdPaaUdpCfgOneWayDelayMax = _AcdPaaUdpCfgOneWayDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 25),
    _AcdPaaUdpCfgOneWayDelayMax_Type()
)
acdPaaUdpCfgOneWayDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOneWayDelayMax.setStatus("current")
_AcdPaaUdpCfgOneWayDelayThresh_Type = Unsigned32
_AcdPaaUdpCfgOneWayDelayThresh_Object = MibTableColumn
acdPaaUdpCfgOneWayDelayThresh = _AcdPaaUdpCfgOneWayDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 26),
    _AcdPaaUdpCfgOneWayDelayThresh_Type()
)
acdPaaUdpCfgOneWayDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOneWayDelayThresh.setStatus("current")
_AcdPaaUdpCfgOneWayAvgDelayThresh_Type = Unsigned32
_AcdPaaUdpCfgOneWayAvgDelayThresh_Object = MibTableColumn
acdPaaUdpCfgOneWayAvgDelayThresh = _AcdPaaUdpCfgOneWayAvgDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 27),
    _AcdPaaUdpCfgOneWayAvgDelayThresh_Type()
)
acdPaaUdpCfgOneWayAvgDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOneWayAvgDelayThresh.setStatus("current")
_AcdPaaUdpCfgDestinationPortNumber_Type = Unsigned32
_AcdPaaUdpCfgDestinationPortNumber_Object = MibTableColumn
acdPaaUdpCfgDestinationPortNumber = _AcdPaaUdpCfgDestinationPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 28),
    _AcdPaaUdpCfgDestinationPortNumber_Type()
)
acdPaaUdpCfgDestinationPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgDestinationPortNumber.setStatus("current")
_AcdPaaUdpCfgPeerID_Type = Unsigned32
_AcdPaaUdpCfgPeerID_Object = MibTableColumn
acdPaaUdpCfgPeerID = _AcdPaaUdpCfgPeerID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 29),
    _AcdPaaUdpCfgPeerID_Type()
)
acdPaaUdpCfgPeerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgPeerID.setStatus("current")
_AcdPaaUdpCfgOperationMode_Type = Unsigned32
_AcdPaaUdpCfgOperationMode_Object = MibTableColumn
acdPaaUdpCfgOperationMode = _AcdPaaUdpCfgOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 30),
    _AcdPaaUdpCfgOperationMode_Type()
)
acdPaaUdpCfgOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgOperationMode.setStatus("current")
_AcdPaaUdpCfgIgmpOneWayJoinPeriod_Type = Unsigned32
_AcdPaaUdpCfgIgmpOneWayJoinPeriod_Object = MibTableColumn
acdPaaUdpCfgIgmpOneWayJoinPeriod = _AcdPaaUdpCfgIgmpOneWayJoinPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 31),
    _AcdPaaUdpCfgIgmpOneWayJoinPeriod_Type()
)
acdPaaUdpCfgIgmpOneWayJoinPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpOneWayJoinPeriod.setStatus("current")
_AcdPaaUdpCfgIgmpRefPeriod_Type = Unsigned32
_AcdPaaUdpCfgIgmpRefPeriod_Object = MibTableColumn
acdPaaUdpCfgIgmpRefPeriod = _AcdPaaUdpCfgIgmpRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 32),
    _AcdPaaUdpCfgIgmpRefPeriod_Type()
)
acdPaaUdpCfgIgmpRefPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpRefPeriod.setStatus("current")
_AcdPaaUdpCfgIgmpMaxJoinDly_Type = Unsigned32
_AcdPaaUdpCfgIgmpMaxJoinDly_Object = MibTableColumn
acdPaaUdpCfgIgmpMaxJoinDly = _AcdPaaUdpCfgIgmpMaxJoinDly_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 33),
    _AcdPaaUdpCfgIgmpMaxJoinDly_Type()
)
acdPaaUdpCfgIgmpMaxJoinDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpMaxJoinDly.setStatus("current")
_AcdPaaUdpCfgIgmpJoinDlyThres_Type = Unsigned32
_AcdPaaUdpCfgIgmpJoinDlyThres_Object = MibTableColumn
acdPaaUdpCfgIgmpJoinDlyThres = _AcdPaaUdpCfgIgmpJoinDlyThres_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 34),
    _AcdPaaUdpCfgIgmpJoinDlyThres_Type()
)
acdPaaUdpCfgIgmpJoinDlyThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpJoinDlyThres.setStatus("current")
_AcdPaaUdpCfgIgmpJoinAvgDlyThres_Type = Unsigned32
_AcdPaaUdpCfgIgmpJoinAvgDlyThres_Object = MibTableColumn
acdPaaUdpCfgIgmpJoinAvgDlyThres = _AcdPaaUdpCfgIgmpJoinAvgDlyThres_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 35),
    _AcdPaaUdpCfgIgmpJoinAvgDlyThres_Type()
)
acdPaaUdpCfgIgmpJoinAvgDlyThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpJoinAvgDlyThres.setStatus("current")
_AcdPaaUdpCfgIgmpMaxLvDly_Type = Unsigned32
_AcdPaaUdpCfgIgmpMaxLvDly_Object = MibTableColumn
acdPaaUdpCfgIgmpMaxLvDly = _AcdPaaUdpCfgIgmpMaxLvDly_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 36),
    _AcdPaaUdpCfgIgmpMaxLvDly_Type()
)
acdPaaUdpCfgIgmpMaxLvDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpMaxLvDly.setStatus("current")
_AcdPaaUdpCfgIgmpLvDlyThresh_Type = Unsigned32
_AcdPaaUdpCfgIgmpLvDlyThresh_Object = MibTableColumn
acdPaaUdpCfgIgmpLvDlyThresh = _AcdPaaUdpCfgIgmpLvDlyThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 37),
    _AcdPaaUdpCfgIgmpLvDlyThresh_Type()
)
acdPaaUdpCfgIgmpLvDlyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpLvDlyThresh.setStatus("current")
_AcdPaaUdpCfgIgmpLvAvgDlyThresh_Type = Unsigned32
_AcdPaaUdpCfgIgmpLvAvgDlyThresh_Object = MibTableColumn
acdPaaUdpCfgIgmpLvAvgDlyThresh = _AcdPaaUdpCfgIgmpLvAvgDlyThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 38),
    _AcdPaaUdpCfgIgmpLvAvgDlyThresh_Type()
)
acdPaaUdpCfgIgmpLvAvgDlyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgIgmpLvAvgDlyThresh.setStatus("current")


class _AcdPaaUdpCfgPktLossThreshExt_Type(Unsigned32):
    """Custom type acdPaaUdpCfgPktLossThreshExt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaUdpCfgPktLossThreshExt_Type.__name__ = "Unsigned32"
_AcdPaaUdpCfgPktLossThreshExt_Object = MibTableColumn
acdPaaUdpCfgPktLossThreshExt = _AcdPaaUdpCfgPktLossThreshExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 39),
    _AcdPaaUdpCfgPktLossThreshExt_Type()
)
acdPaaUdpCfgPktLossThreshExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgPktLossThreshExt.setStatus("current")
_AcdPaaUdpCfgVlan1PriorityValidation_Type = TruthValue
_AcdPaaUdpCfgVlan1PriorityValidation_Object = MibTableColumn
acdPaaUdpCfgVlan1PriorityValidation = _AcdPaaUdpCfgVlan1PriorityValidation_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 40),
    _AcdPaaUdpCfgVlan1PriorityValidation_Type()
)
acdPaaUdpCfgVlan1PriorityValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgVlan1PriorityValidation.setStatus("current")
_AcdPaaUdpCfgVlan1PriorityTxRxCoupling_Type = TruthValue
_AcdPaaUdpCfgVlan1PriorityTxRxCoupling_Object = MibTableColumn
acdPaaUdpCfgVlan1PriorityTxRxCoupling = _AcdPaaUdpCfgVlan1PriorityTxRxCoupling_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 41),
    _AcdPaaUdpCfgVlan1PriorityTxRxCoupling_Type()
)
acdPaaUdpCfgVlan1PriorityTxRxCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgVlan1PriorityTxRxCoupling.setStatus("current")


class _AcdPaaUdpCfgVlan1PriorityExpected_Type(Unsigned32):
    """Custom type acdPaaUdpCfgVlan1PriorityExpected based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdPaaUdpCfgVlan1PriorityExpected_Type.__name__ = "Unsigned32"
_AcdPaaUdpCfgVlan1PriorityExpected_Object = MibTableColumn
acdPaaUdpCfgVlan1PriorityExpected = _AcdPaaUdpCfgVlan1PriorityExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 42),
    _AcdPaaUdpCfgVlan1PriorityExpected_Type()
)
acdPaaUdpCfgVlan1PriorityExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgVlan1PriorityExpected.setStatus("current")
_AcdPaaUdpCfgDscpValidation_Type = TruthValue
_AcdPaaUdpCfgDscpValidation_Object = MibTableColumn
acdPaaUdpCfgDscpValidation = _AcdPaaUdpCfgDscpValidation_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 43),
    _AcdPaaUdpCfgDscpValidation_Type()
)
acdPaaUdpCfgDscpValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgDscpValidation.setStatus("current")
_AcdPaaUdpCfgDscpTxRxCoupling_Type = TruthValue
_AcdPaaUdpCfgDscpTxRxCoupling_Object = MibTableColumn
acdPaaUdpCfgDscpTxRxCoupling = _AcdPaaUdpCfgDscpTxRxCoupling_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 44),
    _AcdPaaUdpCfgDscpTxRxCoupling_Type()
)
acdPaaUdpCfgDscpTxRxCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgDscpTxRxCoupling.setStatus("current")


class _AcdPaaUdpCfgDscpExpected_Type(Unsigned32):
    """Custom type acdPaaUdpCfgDscpExpected based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdPaaUdpCfgDscpExpected_Type.__name__ = "Unsigned32"
_AcdPaaUdpCfgDscpExpected_Object = MibTableColumn
acdPaaUdpCfgDscpExpected = _AcdPaaUdpCfgDscpExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 3, 1, 45),
    _AcdPaaUdpCfgDscpExpected_Type()
)
acdPaaUdpCfgDscpExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaUdpCfgDscpExpected.setStatus("current")
_AcdPaaL2CfgTable_Object = MibTable
acdPaaL2CfgTable = _AcdPaaL2CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4)
)
if mibBuilder.loadTexts:
    acdPaaL2CfgTable.setStatus("current")
_AcdPaaL2CfgEntry_Object = MibTableRow
acdPaaL2CfgEntry = _AcdPaaL2CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1)
)
acdPaaL2CfgEntry.setIndexNames(
    (0, "ACD-PAA-MIB", "acdPaaL2CfgID"),
)
if mibBuilder.loadTexts:
    acdPaaL2CfgEntry.setStatus("current")
_AcdPaaL2CfgID_Type = Unsigned32
_AcdPaaL2CfgID_Object = MibTableColumn
acdPaaL2CfgID = _AcdPaaL2CfgID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 1),
    _AcdPaaL2CfgID_Type()
)
acdPaaL2CfgID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPaaL2CfgID.setStatus("current")


class _AcdPaaL2CfgName_Type(DisplayString):
    """Custom type acdPaaL2CfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdPaaL2CfgName_Type.__name__ = "DisplayString"
_AcdPaaL2CfgName_Object = MibTableColumn
acdPaaL2CfgName = _AcdPaaL2CfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 2),
    _AcdPaaL2CfgName_Type()
)
acdPaaL2CfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgName.setStatus("current")


class _AcdPaaL2CfgState_Type(Integer32):
    """Custom type acdPaaL2CfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_AcdPaaL2CfgState_Type.__name__ = "Integer32"
_AcdPaaL2CfgState_Object = MibTableColumn
acdPaaL2CfgState = _AcdPaaL2CfgState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 3),
    _AcdPaaL2CfgState_Type()
)
acdPaaL2CfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgState.setStatus("current")
_AcdPaaL2CfgPktSize_Type = Unsigned32
_AcdPaaL2CfgPktSize_Object = MibTableColumn
acdPaaL2CfgPktSize = _AcdPaaL2CfgPktSize_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 4),
    _AcdPaaL2CfgPktSize_Type()
)
acdPaaL2CfgPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgPktSize.setStatus("current")
_AcdPaaL2CfgSamplingPeriod_Type = Unsigned32
_AcdPaaL2CfgSamplingPeriod_Object = MibTableColumn
acdPaaL2CfgSamplingPeriod = _AcdPaaL2CfgSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 5),
    _AcdPaaL2CfgSamplingPeriod_Type()
)
acdPaaL2CfgSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgSamplingPeriod.setStatus("current")
_AcdPaaL2CfgCcLossThresh_Type = Unsigned32
_AcdPaaL2CfgCcLossThresh_Object = MibTableColumn
acdPaaL2CfgCcLossThresh = _AcdPaaL2CfgCcLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 6),
    _AcdPaaL2CfgCcLossThresh_Type()
)
acdPaaL2CfgCcLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgCcLossThresh.setStatus("current")
_AcdPaaL2CfgPktLossRefPeriod_Type = Unsigned32
_AcdPaaL2CfgPktLossRefPeriod_Object = MibTableColumn
acdPaaL2CfgPktLossRefPeriod = _AcdPaaL2CfgPktLossRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 7),
    _AcdPaaL2CfgPktLossRefPeriod_Type()
)
acdPaaL2CfgPktLossRefPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgPktLossRefPeriod.setStatus("current")
_AcdPaaL2CfgPktLossThresh_Type = Unsigned32
_AcdPaaL2CfgPktLossThresh_Object = MibTableColumn
acdPaaL2CfgPktLossThresh = _AcdPaaL2CfgPktLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 8),
    _AcdPaaL2CfgPktLossThresh_Type()
)
acdPaaL2CfgPktLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgPktLossThresh.setStatus("current")
_AcdPaaL2CfgOneWayRefPeriod_Type = Unsigned32
_AcdPaaL2CfgOneWayRefPeriod_Object = MibTableColumn
acdPaaL2CfgOneWayRefPeriod = _AcdPaaL2CfgOneWayRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 9),
    _AcdPaaL2CfgOneWayRefPeriod_Type()
)
acdPaaL2CfgOneWayRefPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOneWayRefPeriod.setStatus("current")
_AcdPaaL2CfgOneWayDvMax_Type = Unsigned32
_AcdPaaL2CfgOneWayDvMax_Object = MibTableColumn
acdPaaL2CfgOneWayDvMax = _AcdPaaL2CfgOneWayDvMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 10),
    _AcdPaaL2CfgOneWayDvMax_Type()
)
acdPaaL2CfgOneWayDvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOneWayDvMax.setStatus("current")
_AcdPaaL2CfgOneWayDvThresh_Type = Unsigned32
_AcdPaaL2CfgOneWayDvThresh_Object = MibTableColumn
acdPaaL2CfgOneWayDvThresh = _AcdPaaL2CfgOneWayDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 11),
    _AcdPaaL2CfgOneWayDvThresh_Type()
)
acdPaaL2CfgOneWayDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOneWayDvThresh.setStatus("current")
_AcdPaaL2CfgOneWayAvgDvThresh_Type = Unsigned32
_AcdPaaL2CfgOneWayAvgDvThresh_Object = MibTableColumn
acdPaaL2CfgOneWayAvgDvThresh = _AcdPaaL2CfgOneWayAvgDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 12),
    _AcdPaaL2CfgOneWayAvgDvThresh_Type()
)
acdPaaL2CfgOneWayAvgDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOneWayAvgDvThresh.setStatus("current")
_AcdPaaL2CfgTwoWayRefPeriod_Type = Unsigned32
_AcdPaaL2CfgTwoWayRefPeriod_Object = MibTableColumn
acdPaaL2CfgTwoWayRefPeriod = _AcdPaaL2CfgTwoWayRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 13),
    _AcdPaaL2CfgTwoWayRefPeriod_Type()
)
acdPaaL2CfgTwoWayRefPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgTwoWayRefPeriod.setStatus("current")
_AcdPaaL2CfgTwoWayDelayMax_Type = Unsigned32
_AcdPaaL2CfgTwoWayDelayMax_Object = MibTableColumn
acdPaaL2CfgTwoWayDelayMax = _AcdPaaL2CfgTwoWayDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 14),
    _AcdPaaL2CfgTwoWayDelayMax_Type()
)
acdPaaL2CfgTwoWayDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgTwoWayDelayMax.setStatus("current")
_AcdPaaL2CfgTwoWayDelayThresh_Type = Unsigned32
_AcdPaaL2CfgTwoWayDelayThresh_Object = MibTableColumn
acdPaaL2CfgTwoWayDelayThresh = _AcdPaaL2CfgTwoWayDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 15),
    _AcdPaaL2CfgTwoWayDelayThresh_Type()
)
acdPaaL2CfgTwoWayDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgTwoWayDelayThresh.setStatus("current")
_AcdPaaL2CfgTwoWayAvgDelayThresh_Type = Unsigned32
_AcdPaaL2CfgTwoWayAvgDelayThresh_Object = MibTableColumn
acdPaaL2CfgTwoWayAvgDelayThresh = _AcdPaaL2CfgTwoWayAvgDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 16),
    _AcdPaaL2CfgTwoWayAvgDelayThresh_Type()
)
acdPaaL2CfgTwoWayAvgDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgTwoWayAvgDelayThresh.setStatus("current")
_AcdPaaL2CfgTwoWayDvMax_Type = Unsigned32
_AcdPaaL2CfgTwoWayDvMax_Object = MibTableColumn
acdPaaL2CfgTwoWayDvMax = _AcdPaaL2CfgTwoWayDvMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 17),
    _AcdPaaL2CfgTwoWayDvMax_Type()
)
acdPaaL2CfgTwoWayDvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgTwoWayDvMax.setStatus("current")
_AcdPaaL2CfgTwoWayDvThresh_Type = Unsigned32
_AcdPaaL2CfgTwoWayDvThresh_Object = MibTableColumn
acdPaaL2CfgTwoWayDvThresh = _AcdPaaL2CfgTwoWayDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 18),
    _AcdPaaL2CfgTwoWayDvThresh_Type()
)
acdPaaL2CfgTwoWayDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgTwoWayDvThresh.setStatus("current")
_AcdPaaL2CfgTwoWayAvgDvThresh_Type = Unsigned32
_AcdPaaL2CfgTwoWayAvgDvThresh_Object = MibTableColumn
acdPaaL2CfgTwoWayAvgDvThresh = _AcdPaaL2CfgTwoWayAvgDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 19),
    _AcdPaaL2CfgTwoWayAvgDvThresh_Type()
)
acdPaaL2CfgTwoWayAvgDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgTwoWayAvgDvThresh.setStatus("current")


class _AcdPaaL2CfgPortName_Type(DisplayString):
    """Custom type acdPaaL2CfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdPaaL2CfgPortName_Type.__name__ = "DisplayString"
_AcdPaaL2CfgPortName_Object = MibTableColumn
acdPaaL2CfgPortName = _AcdPaaL2CfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 20),
    _AcdPaaL2CfgPortName_Type()
)
acdPaaL2CfgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgPortName.setStatus("current")
_AcdPaaL2CfgMacDst_Type = MacAddress
_AcdPaaL2CfgMacDst_Object = MibTableColumn
acdPaaL2CfgMacDst = _AcdPaaL2CfgMacDst_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 21),
    _AcdPaaL2CfgMacDst_Type()
)
acdPaaL2CfgMacDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgMacDst.setStatus("current")
_AcdPaaL2CfgEtype_Type = Unsigned32
_AcdPaaL2CfgEtype_Object = MibTableColumn
acdPaaL2CfgEtype = _AcdPaaL2CfgEtype_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 22),
    _AcdPaaL2CfgEtype_Type()
)
acdPaaL2CfgEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgEtype.setStatus("current")
_AcdPaaL2CfgVlan1IdEn_Type = TruthValue
_AcdPaaL2CfgVlan1IdEn_Object = MibTableColumn
acdPaaL2CfgVlan1IdEn = _AcdPaaL2CfgVlan1IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 23),
    _AcdPaaL2CfgVlan1IdEn_Type()
)
acdPaaL2CfgVlan1IdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1IdEn.setStatus("current")
_AcdPaaL2CfgVlan1Id_Type = Unsigned32
_AcdPaaL2CfgVlan1Id_Object = MibTableColumn
acdPaaL2CfgVlan1Id = _AcdPaaL2CfgVlan1Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 24),
    _AcdPaaL2CfgVlan1Id_Type()
)
acdPaaL2CfgVlan1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1Id.setStatus("current")
_AcdPaaL2CfgVlan2IdEn_Type = TruthValue
_AcdPaaL2CfgVlan2IdEn_Object = MibTableColumn
acdPaaL2CfgVlan2IdEn = _AcdPaaL2CfgVlan2IdEn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 25),
    _AcdPaaL2CfgVlan2IdEn_Type()
)
acdPaaL2CfgVlan2IdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2IdEn.setStatus("current")
_AcdPaaL2CfgVlan2Id_Type = Unsigned32
_AcdPaaL2CfgVlan2Id_Object = MibTableColumn
acdPaaL2CfgVlan2Id = _AcdPaaL2CfgVlan2Id_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 26),
    _AcdPaaL2CfgVlan2Id_Type()
)
acdPaaL2CfgVlan2Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2Id.setStatus("current")
_AcdPaaL2CfgVlan1PbitsValue_Type = Unsigned32
_AcdPaaL2CfgVlan1PbitsValue_Object = MibTableColumn
acdPaaL2CfgVlan1PbitsValue = _AcdPaaL2CfgVlan1PbitsValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 27),
    _AcdPaaL2CfgVlan1PbitsValue_Type()
)
acdPaaL2CfgVlan1PbitsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1PbitsValue.setStatus("current")
_AcdPaaL2CfgVlan2PbitsValue_Type = Unsigned32
_AcdPaaL2CfgVlan2PbitsValue_Object = MibTableColumn
acdPaaL2CfgVlan2PbitsValue = _AcdPaaL2CfgVlan2PbitsValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 28),
    _AcdPaaL2CfgVlan2PbitsValue_Type()
)
acdPaaL2CfgVlan2PbitsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2PbitsValue.setStatus("current")
_AcdPaaL2CfgOneWayDelayMax_Type = Unsigned32
_AcdPaaL2CfgOneWayDelayMax_Object = MibTableColumn
acdPaaL2CfgOneWayDelayMax = _AcdPaaL2CfgOneWayDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 29),
    _AcdPaaL2CfgOneWayDelayMax_Type()
)
acdPaaL2CfgOneWayDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOneWayDelayMax.setStatus("current")
_AcdPaaL2CfgOneWayDelayThresh_Type = Unsigned32
_AcdPaaL2CfgOneWayDelayThresh_Object = MibTableColumn
acdPaaL2CfgOneWayDelayThresh = _AcdPaaL2CfgOneWayDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 30),
    _AcdPaaL2CfgOneWayDelayThresh_Type()
)
acdPaaL2CfgOneWayDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOneWayDelayThresh.setStatus("current")
_AcdPaaL2CfgOneWayAvgDelayThresh_Type = Unsigned32
_AcdPaaL2CfgOneWayAvgDelayThresh_Object = MibTableColumn
acdPaaL2CfgOneWayAvgDelayThresh = _AcdPaaL2CfgOneWayAvgDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 31),
    _AcdPaaL2CfgOneWayAvgDelayThresh_Type()
)
acdPaaL2CfgOneWayAvgDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOneWayAvgDelayThresh.setStatus("current")
_AcdPaaL2CfgPeerID_Type = Unsigned32
_AcdPaaL2CfgPeerID_Object = MibTableColumn
acdPaaL2CfgPeerID = _AcdPaaL2CfgPeerID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 32),
    _AcdPaaL2CfgPeerID_Type()
)
acdPaaL2CfgPeerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgPeerID.setStatus("current")
_AcdPaaL2CfgOperationMode_Type = Unsigned32
_AcdPaaL2CfgOperationMode_Object = MibTableColumn
acdPaaL2CfgOperationMode = _AcdPaaL2CfgOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 33),
    _AcdPaaL2CfgOperationMode_Type()
)
acdPaaL2CfgOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgOperationMode.setStatus("current")


class _AcdPaaL2CfgPktLossThreshExt_Type(Unsigned32):
    """Custom type acdPaaL2CfgPktLossThreshExt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaL2CfgPktLossThreshExt_Type.__name__ = "Unsigned32"
_AcdPaaL2CfgPktLossThreshExt_Object = MibTableColumn
acdPaaL2CfgPktLossThreshExt = _AcdPaaL2CfgPktLossThreshExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 34),
    _AcdPaaL2CfgPktLossThreshExt_Type()
)
acdPaaL2CfgPktLossThreshExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgPktLossThreshExt.setStatus("current")
_AcdPaaL2CfgVlan1IdValidation_Type = TruthValue
_AcdPaaL2CfgVlan1IdValidation_Object = MibTableColumn
acdPaaL2CfgVlan1IdValidation = _AcdPaaL2CfgVlan1IdValidation_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 35),
    _AcdPaaL2CfgVlan1IdValidation_Type()
)
acdPaaL2CfgVlan1IdValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1IdValidation.setStatus("current")
_AcdPaaL2CfgVlan1IdTxRxCoupling_Type = TruthValue
_AcdPaaL2CfgVlan1IdTxRxCoupling_Object = MibTableColumn
acdPaaL2CfgVlan1IdTxRxCoupling = _AcdPaaL2CfgVlan1IdTxRxCoupling_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 36),
    _AcdPaaL2CfgVlan1IdTxRxCoupling_Type()
)
acdPaaL2CfgVlan1IdTxRxCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1IdTxRxCoupling.setStatus("current")


class _AcdPaaL2CfgVlan1IdExpected_Type(Unsigned32):
    """Custom type acdPaaL2CfgVlan1IdExpected based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdPaaL2CfgVlan1IdExpected_Type.__name__ = "Unsigned32"
_AcdPaaL2CfgVlan1IdExpected_Object = MibTableColumn
acdPaaL2CfgVlan1IdExpected = _AcdPaaL2CfgVlan1IdExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 37),
    _AcdPaaL2CfgVlan1IdExpected_Type()
)
acdPaaL2CfgVlan1IdExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1IdExpected.setStatus("current")
_AcdPaaL2CfgVlan2IdValidation_Type = TruthValue
_AcdPaaL2CfgVlan2IdValidation_Object = MibTableColumn
acdPaaL2CfgVlan2IdValidation = _AcdPaaL2CfgVlan2IdValidation_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 38),
    _AcdPaaL2CfgVlan2IdValidation_Type()
)
acdPaaL2CfgVlan2IdValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2IdValidation.setStatus("current")
_AcdPaaL2CfgVlan2IdTxRxCoupling_Type = TruthValue
_AcdPaaL2CfgVlan2IdTxRxCoupling_Object = MibTableColumn
acdPaaL2CfgVlan2IdTxRxCoupling = _AcdPaaL2CfgVlan2IdTxRxCoupling_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 39),
    _AcdPaaL2CfgVlan2IdTxRxCoupling_Type()
)
acdPaaL2CfgVlan2IdTxRxCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2IdTxRxCoupling.setStatus("current")


class _AcdPaaL2CfgVlan2IdExpected_Type(Unsigned32):
    """Custom type acdPaaL2CfgVlan2IdExpected based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdPaaL2CfgVlan2IdExpected_Type.__name__ = "Unsigned32"
_AcdPaaL2CfgVlan2IdExpected_Object = MibTableColumn
acdPaaL2CfgVlan2IdExpected = _AcdPaaL2CfgVlan2IdExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 40),
    _AcdPaaL2CfgVlan2IdExpected_Type()
)
acdPaaL2CfgVlan2IdExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2IdExpected.setStatus("current")
_AcdPaaL2CfgVlan1PriorityValidation_Type = TruthValue
_AcdPaaL2CfgVlan1PriorityValidation_Object = MibTableColumn
acdPaaL2CfgVlan1PriorityValidation = _AcdPaaL2CfgVlan1PriorityValidation_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 41),
    _AcdPaaL2CfgVlan1PriorityValidation_Type()
)
acdPaaL2CfgVlan1PriorityValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1PriorityValidation.setStatus("current")
_AcdPaaL2CfgVlan1PriorityTxRxCoupling_Type = TruthValue
_AcdPaaL2CfgVlan1PriorityTxRxCoupling_Object = MibTableColumn
acdPaaL2CfgVlan1PriorityTxRxCoupling = _AcdPaaL2CfgVlan1PriorityTxRxCoupling_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 42),
    _AcdPaaL2CfgVlan1PriorityTxRxCoupling_Type()
)
acdPaaL2CfgVlan1PriorityTxRxCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1PriorityTxRxCoupling.setStatus("current")


class _AcdPaaL2CfgVlan1PriorityExpected_Type(Unsigned32):
    """Custom type acdPaaL2CfgVlan1PriorityExpected based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdPaaL2CfgVlan1PriorityExpected_Type.__name__ = "Unsigned32"
_AcdPaaL2CfgVlan1PriorityExpected_Object = MibTableColumn
acdPaaL2CfgVlan1PriorityExpected = _AcdPaaL2CfgVlan1PriorityExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 43),
    _AcdPaaL2CfgVlan1PriorityExpected_Type()
)
acdPaaL2CfgVlan1PriorityExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan1PriorityExpected.setStatus("current")
_AcdPaaL2CfgVlan2PriorityValidation_Type = TruthValue
_AcdPaaL2CfgVlan2PriorityValidation_Object = MibTableColumn
acdPaaL2CfgVlan2PriorityValidation = _AcdPaaL2CfgVlan2PriorityValidation_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 44),
    _AcdPaaL2CfgVlan2PriorityValidation_Type()
)
acdPaaL2CfgVlan2PriorityValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2PriorityValidation.setStatus("current")
_AcdPaaL2CfgVlan2PriorityTxRxCoupling_Type = TruthValue
_AcdPaaL2CfgVlan2PriorityTxRxCoupling_Object = MibTableColumn
acdPaaL2CfgVlan2PriorityTxRxCoupling = _AcdPaaL2CfgVlan2PriorityTxRxCoupling_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 45),
    _AcdPaaL2CfgVlan2PriorityTxRxCoupling_Type()
)
acdPaaL2CfgVlan2PriorityTxRxCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2PriorityTxRxCoupling.setStatus("current")


class _AcdPaaL2CfgVlan2PriorityExpected_Type(Unsigned32):
    """Custom type acdPaaL2CfgVlan2PriorityExpected based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdPaaL2CfgVlan2PriorityExpected_Type.__name__ = "Unsigned32"
_AcdPaaL2CfgVlan2PriorityExpected_Object = MibTableColumn
acdPaaL2CfgVlan2PriorityExpected = _AcdPaaL2CfgVlan2PriorityExpected_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 4, 1, 46),
    _AcdPaaL2CfgVlan2PriorityExpected_Type()
)
acdPaaL2CfgVlan2PriorityExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPaaL2CfgVlan2PriorityExpected.setStatus("current")
_AcdPaaHistResultTable_Object = MibTable
acdPaaHistResultTable = _AcdPaaHistResultTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5)
)
if mibBuilder.loadTexts:
    acdPaaHistResultTable.setStatus("current")
_AcdPaaHistResultEntry_Object = MibTableRow
acdPaaHistResultEntry = _AcdPaaHistResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1)
)
acdPaaHistResultEntry.setIndexNames(
    (0, "ACD-PAA-MIB", "acdPaaHistResultID"),
    (0, "ACD-PAA-MIB", "acdPaaHistResultSampleIndex"),
)
if mibBuilder.loadTexts:
    acdPaaHistResultEntry.setStatus("current")
_AcdPaaHistResultID_Type = Unsigned32
_AcdPaaHistResultID_Object = MibTableColumn
acdPaaHistResultID = _AcdPaaHistResultID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 1),
    _AcdPaaHistResultID_Type()
)
acdPaaHistResultID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPaaHistResultID.setStatus("current")
_AcdPaaHistResultSampleIndex_Type = Unsigned32
_AcdPaaHistResultSampleIndex_Object = MibTableColumn
acdPaaHistResultSampleIndex = _AcdPaaHistResultSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 2),
    _AcdPaaHistResultSampleIndex_Type()
)
acdPaaHistResultSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPaaHistResultSampleIndex.setStatus("current")


class _AcdPaaHistResultStatus_Type(Integer32):
    """Custom type acdPaaHistResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AcdPaaHistResultStatus_Type.__name__ = "Integer32"
_AcdPaaHistResultStatus_Object = MibTableColumn
acdPaaHistResultStatus = _AcdPaaHistResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 3),
    _AcdPaaHistResultStatus_Type()
)
acdPaaHistResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultStatus.setStatus("current")
_AcdPaaHistResultDuration_Type = Unsigned32
_AcdPaaHistResultDuration_Object = MibTableColumn
acdPaaHistResultDuration = _AcdPaaHistResultDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 4),
    _AcdPaaHistResultDuration_Type()
)
acdPaaHistResultDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultDuration.setStatus("current")
_AcdPaaHistResultIntervalEnd_Type = DateAndTime
_AcdPaaHistResultIntervalEnd_Object = MibTableColumn
acdPaaHistResultIntervalEnd = _AcdPaaHistResultIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 5),
    _AcdPaaHistResultIntervalEnd_Type()
)
acdPaaHistResultIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIntervalEnd.setStatus("current")
_AcdPaaHistResultPktLossNeValid_Type = TruthValue
_AcdPaaHistResultPktLossNeValid_Object = MibTableColumn
acdPaaHistResultPktLossNeValid = _AcdPaaHistResultPktLossNeValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 6),
    _AcdPaaHistResultPktLossNeValid_Type()
)
acdPaaHistResultPktLossNeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossNeValid.setStatus("current")
_AcdPaaHistResultPktLossNeSamples_Type = Unsigned32
_AcdPaaHistResultPktLossNeSamples_Object = MibTableColumn
acdPaaHistResultPktLossNeSamples = _AcdPaaHistResultPktLossNeSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 7),
    _AcdPaaHistResultPktLossNeSamples_Type()
)
acdPaaHistResultPktLossNeSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossNeSamples.setStatus("current")


class _AcdPaaHistResultPktLossNeValue_Type(Unsigned32):
    """Custom type acdPaaHistResultPktLossNeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AcdPaaHistResultPktLossNeValue_Type.__name__ = "Unsigned32"
_AcdPaaHistResultPktLossNeValue_Object = MibTableColumn
acdPaaHistResultPktLossNeValue = _AcdPaaHistResultPktLossNeValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 8),
    _AcdPaaHistResultPktLossNeValue_Type()
)
acdPaaHistResultPktLossNeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossNeValue.setStatus("current")
_AcdPaaHistResultPktLossFeValid_Type = TruthValue
_AcdPaaHistResultPktLossFeValid_Object = MibTableColumn
acdPaaHistResultPktLossFeValid = _AcdPaaHistResultPktLossFeValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 9),
    _AcdPaaHistResultPktLossFeValid_Type()
)
acdPaaHistResultPktLossFeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossFeValid.setStatus("current")
_AcdPaaHistResultPktLossFeSamples_Type = Unsigned32
_AcdPaaHistResultPktLossFeSamples_Object = MibTableColumn
acdPaaHistResultPktLossFeSamples = _AcdPaaHistResultPktLossFeSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 10),
    _AcdPaaHistResultPktLossFeSamples_Type()
)
acdPaaHistResultPktLossFeSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossFeSamples.setStatus("current")


class _AcdPaaHistResultPktLossFeValue_Type(Unsigned32):
    """Custom type acdPaaHistResultPktLossFeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AcdPaaHistResultPktLossFeValue_Type.__name__ = "Unsigned32"
_AcdPaaHistResultPktLossFeValue_Object = MibTableColumn
acdPaaHistResultPktLossFeValue = _AcdPaaHistResultPktLossFeValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 11),
    _AcdPaaHistResultPktLossFeValue_Type()
)
acdPaaHistResultPktLossFeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossFeValue.setStatus("current")
_AcdPaaHistResultOneWayDelayValid_Type = TruthValue
_AcdPaaHistResultOneWayDelayValid_Object = MibTableColumn
acdPaaHistResultOneWayDelayValid = _AcdPaaHistResultOneWayDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 12),
    _AcdPaaHistResultOneWayDelayValid_Type()
)
acdPaaHistResultOneWayDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDelayValid.setStatus("current")
_AcdPaaHistResultOneWayDelaySamples_Type = Unsigned32
_AcdPaaHistResultOneWayDelaySamples_Object = MibTableColumn
acdPaaHistResultOneWayDelaySamples = _AcdPaaHistResultOneWayDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 13),
    _AcdPaaHistResultOneWayDelaySamples_Type()
)
acdPaaHistResultOneWayDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDelaySamples.setStatus("current")
_AcdPaaHistResultOneWayDelayMinValue_Type = Integer32
_AcdPaaHistResultOneWayDelayMinValue_Object = MibTableColumn
acdPaaHistResultOneWayDelayMinValue = _AcdPaaHistResultOneWayDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 14),
    _AcdPaaHistResultOneWayDelayMinValue_Type()
)
acdPaaHistResultOneWayDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDelayMinValue.setStatus("current")
_AcdPaaHistResultOneWayDelayMaxValue_Type = Integer32
_AcdPaaHistResultOneWayDelayMaxValue_Object = MibTableColumn
acdPaaHistResultOneWayDelayMaxValue = _AcdPaaHistResultOneWayDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 15),
    _AcdPaaHistResultOneWayDelayMaxValue_Type()
)
acdPaaHistResultOneWayDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDelayMaxValue.setStatus("current")
_AcdPaaHistResultOneWayDelayAvgValue_Type = Integer32
_AcdPaaHistResultOneWayDelayAvgValue_Object = MibTableColumn
acdPaaHistResultOneWayDelayAvgValue = _AcdPaaHistResultOneWayDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 16),
    _AcdPaaHistResultOneWayDelayAvgValue_Type()
)
acdPaaHistResultOneWayDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDelayAvgValue.setStatus("current")
_AcdPaaHistResultOneWayDelayThreshEx_Type = Unsigned32
_AcdPaaHistResultOneWayDelayThreshEx_Object = MibTableColumn
acdPaaHistResultOneWayDelayThreshEx = _AcdPaaHistResultOneWayDelayThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 17),
    _AcdPaaHistResultOneWayDelayThreshEx_Type()
)
acdPaaHistResultOneWayDelayThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDelayThreshEx.setStatus("current")
_AcdPaaHistResultOneWayDvValid_Type = TruthValue
_AcdPaaHistResultOneWayDvValid_Object = MibTableColumn
acdPaaHistResultOneWayDvValid = _AcdPaaHistResultOneWayDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 18),
    _AcdPaaHistResultOneWayDvValid_Type()
)
acdPaaHistResultOneWayDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDvValid.setStatus("current")
_AcdPaaHistResultOneWayDvSamples_Type = Unsigned32
_AcdPaaHistResultOneWayDvSamples_Object = MibTableColumn
acdPaaHistResultOneWayDvSamples = _AcdPaaHistResultOneWayDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 19),
    _AcdPaaHistResultOneWayDvSamples_Type()
)
acdPaaHistResultOneWayDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDvSamples.setStatus("current")
_AcdPaaHistResultOneWayDvMinValue_Type = Integer32
_AcdPaaHistResultOneWayDvMinValue_Object = MibTableColumn
acdPaaHistResultOneWayDvMinValue = _AcdPaaHistResultOneWayDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 20),
    _AcdPaaHistResultOneWayDvMinValue_Type()
)
acdPaaHistResultOneWayDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDvMinValue.setStatus("current")
_AcdPaaHistResultOneWayDvMaxValue_Type = Integer32
_AcdPaaHistResultOneWayDvMaxValue_Object = MibTableColumn
acdPaaHistResultOneWayDvMaxValue = _AcdPaaHistResultOneWayDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 21),
    _AcdPaaHistResultOneWayDvMaxValue_Type()
)
acdPaaHistResultOneWayDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDvMaxValue.setStatus("current")
_AcdPaaHistResultOneWayDvAvgValue_Type = Integer32
_AcdPaaHistResultOneWayDvAvgValue_Object = MibTableColumn
acdPaaHistResultOneWayDvAvgValue = _AcdPaaHistResultOneWayDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 22),
    _AcdPaaHistResultOneWayDvAvgValue_Type()
)
acdPaaHistResultOneWayDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDvAvgValue.setStatus("current")
_AcdPaaHistResultOneWayDvThreshEx_Type = Unsigned32
_AcdPaaHistResultOneWayDvThreshEx_Object = MibTableColumn
acdPaaHistResultOneWayDvThreshEx = _AcdPaaHistResultOneWayDvThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 23),
    _AcdPaaHistResultOneWayDvThreshEx_Type()
)
acdPaaHistResultOneWayDvThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultOneWayDvThreshEx.setStatus("current")
_AcdPaaHistResultTwoWayDelayValid_Type = TruthValue
_AcdPaaHistResultTwoWayDelayValid_Object = MibTableColumn
acdPaaHistResultTwoWayDelayValid = _AcdPaaHistResultTwoWayDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 24),
    _AcdPaaHistResultTwoWayDelayValid_Type()
)
acdPaaHistResultTwoWayDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDelayValid.setStatus("current")
_AcdPaaHistResultTwoWayDelaySamples_Type = Unsigned32
_AcdPaaHistResultTwoWayDelaySamples_Object = MibTableColumn
acdPaaHistResultTwoWayDelaySamples = _AcdPaaHistResultTwoWayDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 25),
    _AcdPaaHistResultTwoWayDelaySamples_Type()
)
acdPaaHistResultTwoWayDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDelaySamples.setStatus("current")
_AcdPaaHistResultTwoWayDelayMinValue_Type = Integer32
_AcdPaaHistResultTwoWayDelayMinValue_Object = MibTableColumn
acdPaaHistResultTwoWayDelayMinValue = _AcdPaaHistResultTwoWayDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 26),
    _AcdPaaHistResultTwoWayDelayMinValue_Type()
)
acdPaaHistResultTwoWayDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDelayMinValue.setStatus("current")
_AcdPaaHistResultTwoWayDelayMaxValue_Type = Integer32
_AcdPaaHistResultTwoWayDelayMaxValue_Object = MibTableColumn
acdPaaHistResultTwoWayDelayMaxValue = _AcdPaaHistResultTwoWayDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 27),
    _AcdPaaHistResultTwoWayDelayMaxValue_Type()
)
acdPaaHistResultTwoWayDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDelayMaxValue.setStatus("current")
_AcdPaaHistResultTwoWayDelayAvgValue_Type = Integer32
_AcdPaaHistResultTwoWayDelayAvgValue_Object = MibTableColumn
acdPaaHistResultTwoWayDelayAvgValue = _AcdPaaHistResultTwoWayDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 28),
    _AcdPaaHistResultTwoWayDelayAvgValue_Type()
)
acdPaaHistResultTwoWayDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDelayAvgValue.setStatus("current")
_AcdPaaHistResultTwoWayDelayThreshEx_Type = Unsigned32
_AcdPaaHistResultTwoWayDelayThreshEx_Object = MibTableColumn
acdPaaHistResultTwoWayDelayThreshEx = _AcdPaaHistResultTwoWayDelayThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 29),
    _AcdPaaHistResultTwoWayDelayThreshEx_Type()
)
acdPaaHistResultTwoWayDelayThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDelayThreshEx.setStatus("current")
_AcdPaaHistResultTwoWayDvValid_Type = TruthValue
_AcdPaaHistResultTwoWayDvValid_Object = MibTableColumn
acdPaaHistResultTwoWayDvValid = _AcdPaaHistResultTwoWayDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 30),
    _AcdPaaHistResultTwoWayDvValid_Type()
)
acdPaaHistResultTwoWayDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDvValid.setStatus("current")
_AcdPaaHistResultTwoWayDvSamples_Type = Unsigned32
_AcdPaaHistResultTwoWayDvSamples_Object = MibTableColumn
acdPaaHistResultTwoWayDvSamples = _AcdPaaHistResultTwoWayDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 31),
    _AcdPaaHistResultTwoWayDvSamples_Type()
)
acdPaaHistResultTwoWayDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDvSamples.setStatus("current")
_AcdPaaHistResultTwoWayDvMinValue_Type = Integer32
_AcdPaaHistResultTwoWayDvMinValue_Object = MibTableColumn
acdPaaHistResultTwoWayDvMinValue = _AcdPaaHistResultTwoWayDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 32),
    _AcdPaaHistResultTwoWayDvMinValue_Type()
)
acdPaaHistResultTwoWayDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDvMinValue.setStatus("current")
_AcdPaaHistResultTwoWayDvMaxValue_Type = Integer32
_AcdPaaHistResultTwoWayDvMaxValue_Object = MibTableColumn
acdPaaHistResultTwoWayDvMaxValue = _AcdPaaHistResultTwoWayDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 33),
    _AcdPaaHistResultTwoWayDvMaxValue_Type()
)
acdPaaHistResultTwoWayDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDvMaxValue.setStatus("current")
_AcdPaaHistResultTwoWayDvAvgValue_Type = Integer32
_AcdPaaHistResultTwoWayDvAvgValue_Object = MibTableColumn
acdPaaHistResultTwoWayDvAvgValue = _AcdPaaHistResultTwoWayDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 34),
    _AcdPaaHistResultTwoWayDvAvgValue_Type()
)
acdPaaHistResultTwoWayDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDvAvgValue.setStatus("current")
_AcdPaaHistResultTwoWayDvThreshEx_Type = Unsigned32
_AcdPaaHistResultTwoWayDvThreshEx_Object = MibTableColumn
acdPaaHistResultTwoWayDvThreshEx = _AcdPaaHistResultTwoWayDvThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 35),
    _AcdPaaHistResultTwoWayDvThreshEx_Type()
)
acdPaaHistResultTwoWayDvThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultTwoWayDvThreshEx.setStatus("current")
_AcdPaaHistResultIgmpJoinDelayValid_Type = TruthValue
_AcdPaaHistResultIgmpJoinDelayValid_Object = MibTableColumn
acdPaaHistResultIgmpJoinDelayValid = _AcdPaaHistResultIgmpJoinDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 36),
    _AcdPaaHistResultIgmpJoinDelayValid_Type()
)
acdPaaHistResultIgmpJoinDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpJoinDelayValid.setStatus("current")
_AcdPaaHistResultIgmpJoinDelaySamples_Type = Unsigned32
_AcdPaaHistResultIgmpJoinDelaySamples_Object = MibTableColumn
acdPaaHistResultIgmpJoinDelaySamples = _AcdPaaHistResultIgmpJoinDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 37),
    _AcdPaaHistResultIgmpJoinDelaySamples_Type()
)
acdPaaHistResultIgmpJoinDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpJoinDelaySamples.setStatus("current")
_AcdPaaHistResultIgmpJoinDelayMinValue_Type = Integer32
_AcdPaaHistResultIgmpJoinDelayMinValue_Object = MibTableColumn
acdPaaHistResultIgmpJoinDelayMinValue = _AcdPaaHistResultIgmpJoinDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 38),
    _AcdPaaHistResultIgmpJoinDelayMinValue_Type()
)
acdPaaHistResultIgmpJoinDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpJoinDelayMinValue.setStatus("current")
_AcdPaaHistResultIgmpJoinDelayMaxValue_Type = Integer32
_AcdPaaHistResultIgmpJoinDelayMaxValue_Object = MibTableColumn
acdPaaHistResultIgmpJoinDelayMaxValue = _AcdPaaHistResultIgmpJoinDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 39),
    _AcdPaaHistResultIgmpJoinDelayMaxValue_Type()
)
acdPaaHistResultIgmpJoinDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpJoinDelayMaxValue.setStatus("current")
_AcdPaaHistResultIgmpJoinDelayAvgValue_Type = Integer32
_AcdPaaHistResultIgmpJoinDelayAvgValue_Object = MibTableColumn
acdPaaHistResultIgmpJoinDelayAvgValue = _AcdPaaHistResultIgmpJoinDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 40),
    _AcdPaaHistResultIgmpJoinDelayAvgValue_Type()
)
acdPaaHistResultIgmpJoinDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpJoinDelayAvgValue.setStatus("current")
_AcdPaaHistResultIgmpJoinDelayThreshEx_Type = Unsigned32
_AcdPaaHistResultIgmpJoinDelayThreshEx_Object = MibTableColumn
acdPaaHistResultIgmpJoinDelayThreshEx = _AcdPaaHistResultIgmpJoinDelayThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 41),
    _AcdPaaHistResultIgmpJoinDelayThreshEx_Type()
)
acdPaaHistResultIgmpJoinDelayThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpJoinDelayThreshEx.setStatus("current")
_AcdPaaHistResultIgmpLeaveDelayValid_Type = TruthValue
_AcdPaaHistResultIgmpLeaveDelayValid_Object = MibTableColumn
acdPaaHistResultIgmpLeaveDelayValid = _AcdPaaHistResultIgmpLeaveDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 42),
    _AcdPaaHistResultIgmpLeaveDelayValid_Type()
)
acdPaaHistResultIgmpLeaveDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpLeaveDelayValid.setStatus("current")
_AcdPaaHistResultIgmpLeaveDelaySamples_Type = Unsigned32
_AcdPaaHistResultIgmpLeaveDelaySamples_Object = MibTableColumn
acdPaaHistResultIgmpLeaveDelaySamples = _AcdPaaHistResultIgmpLeaveDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 43),
    _AcdPaaHistResultIgmpLeaveDelaySamples_Type()
)
acdPaaHistResultIgmpLeaveDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpLeaveDelaySamples.setStatus("current")
_AcdPaaHistResultIgmpLeaveDelayMinValue_Type = Integer32
_AcdPaaHistResultIgmpLeaveDelayMinValue_Object = MibTableColumn
acdPaaHistResultIgmpLeaveDelayMinValue = _AcdPaaHistResultIgmpLeaveDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 44),
    _AcdPaaHistResultIgmpLeaveDelayMinValue_Type()
)
acdPaaHistResultIgmpLeaveDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpLeaveDelayMinValue.setStatus("current")
_AcdPaaHistResultIgmpLeaveDelayMaxValue_Type = Integer32
_AcdPaaHistResultIgmpLeaveDelayMaxValue_Object = MibTableColumn
acdPaaHistResultIgmpLeaveDelayMaxValue = _AcdPaaHistResultIgmpLeaveDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 45),
    _AcdPaaHistResultIgmpLeaveDelayMaxValue_Type()
)
acdPaaHistResultIgmpLeaveDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpLeaveDelayMaxValue.setStatus("current")
_AcdPaaHistResultIgmpLeaveDelayAvgValue_Type = Integer32
_AcdPaaHistResultIgmpLeaveDelayAvgValue_Object = MibTableColumn
acdPaaHistResultIgmpLeaveDelayAvgValue = _AcdPaaHistResultIgmpLeaveDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 46),
    _AcdPaaHistResultIgmpLeaveDelayAvgValue_Type()
)
acdPaaHistResultIgmpLeaveDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpLeaveDelayAvgValue.setStatus("current")
_AcdPaaHistResultIgmpLeaveDelayThreshEx_Type = Unsigned32
_AcdPaaHistResultIgmpLeaveDelayThreshEx_Object = MibTableColumn
acdPaaHistResultIgmpLeaveDelayThreshEx = _AcdPaaHistResultIgmpLeaveDelayThreshEx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 47),
    _AcdPaaHistResultIgmpLeaveDelayThreshEx_Type()
)
acdPaaHistResultIgmpLeaveDelayThreshEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultIgmpLeaveDelayThreshEx.setStatus("current")


class _AcdPaaHistResultPktLossNeValueExt_Type(Unsigned32):
    """Custom type acdPaaHistResultPktLossNeValueExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaHistResultPktLossNeValueExt_Type.__name__ = "Unsigned32"
_AcdPaaHistResultPktLossNeValueExt_Object = MibTableColumn
acdPaaHistResultPktLossNeValueExt = _AcdPaaHistResultPktLossNeValueExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 48),
    _AcdPaaHistResultPktLossNeValueExt_Type()
)
acdPaaHistResultPktLossNeValueExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossNeValueExt.setStatus("current")


class _AcdPaaHistResultPktLossFeValueExt_Type(Unsigned32):
    """Custom type acdPaaHistResultPktLossFeValueExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdPaaHistResultPktLossFeValueExt_Type.__name__ = "Unsigned32"
_AcdPaaHistResultPktLossFeValueExt_Object = MibTableColumn
acdPaaHistResultPktLossFeValueExt = _AcdPaaHistResultPktLossFeValueExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 49),
    _AcdPaaHistResultPktLossFeValueExt_Type()
)
acdPaaHistResultPktLossFeValueExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossFeValueExt.setStatus("current")
_AcdPaaHistResultPktLossNeNbrLoss_Type = Unsigned32
_AcdPaaHistResultPktLossNeNbrLoss_Object = MibTableColumn
acdPaaHistResultPktLossNeNbrLoss = _AcdPaaHistResultPktLossNeNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 50),
    _AcdPaaHistResultPktLossNeNbrLoss_Type()
)
acdPaaHistResultPktLossNeNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossNeNbrLoss.setStatus("current")
_AcdPaaHistResultPktLossFeNbrLoss_Type = Unsigned32
_AcdPaaHistResultPktLossFeNbrLoss_Object = MibTableColumn
acdPaaHistResultPktLossFeNbrLoss = _AcdPaaHistResultPktLossFeNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 5, 1, 51),
    _AcdPaaHistResultPktLossFeNbrLoss_Type()
)
acdPaaHistResultPktLossFeNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPaaHistResultPktLossFeNbrLoss.setStatus("current")
_AcdPaaNotifications_ObjectIdentity = ObjectIdentity
acdPaaNotifications = _AcdPaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 7)
)
_AcdPaaMIBObjects_ObjectIdentity = ObjectIdentity
acdPaaMIBObjects = _AcdPaaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 8)
)
_AcdPaaConformance_ObjectIdentity = ObjectIdentity
acdPaaConformance = _AcdPaaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9)
)
_AcdPaaCompliances_ObjectIdentity = ObjectIdentity
acdPaaCompliances = _AcdPaaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 1)
)
_AcdPaaGroups_ObjectIdentity = ObjectIdentity
acdPaaGroups = _AcdPaaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 2)
)

# Managed Objects groups

acdPaaResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 2, 1)
)
acdPaaResultGroup.setObjects(
      *(("ACD-PAA-MIB", "acdPaaResultState"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNeCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNeCurrValue"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNePrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNePrevValue"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFeCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFeCurrValue"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFePrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFePrevValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvInstValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvCurrMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvCurrMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvCurrAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvCurrThreshExc"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvPrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvPrevMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvPrevMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvPrevAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvPrevThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayInstValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayCurrMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayCurrMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayCurrAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayCurrThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayPrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayPrevMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayPrevMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayPrevAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayPrevThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvInstValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvCurrMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvCurrMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvCurrAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvCurrThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvPrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvPrevMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvPrevMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvPrevAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvPrevThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayInstValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayCurrMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayCurrMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayCurrAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayCurrThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayPrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayPrevMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayPrevMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayPrevAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayPrevThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossTime"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayTime"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayTime"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNeCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNePrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFeCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFePrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDelayPrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultOneWayDvPrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDelayPrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultTwoWayDvPrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayInstValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayCurrMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayCurrMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayCurrAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayCurrThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayPrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayPrevMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayPrevMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayPrevAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayPrevThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayInstValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayCurrValid"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayCurrMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayCurrMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayCurrAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayCurrThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayPrevValid"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayPrevMinValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayPrevMaxValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayPrevAvgValue"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayPrevThreshEx"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayTime"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayTime"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpJoinDelayPrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayCurrSamples"),
        ("ACD-PAA-MIB", "acdPaaResultIgmpLeaveDelayPrevSamples"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossCurrGaps"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossPrevGaps"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossCurrLargestGap"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossPrevLargestGap"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNeCurrValueExt"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNePrevValueExt"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFeCurrValueExt"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFePrevValueExt"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNeCurrNbrLoss"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossNePrevNbrLoss"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFeCurrNbrLoss"),
        ("ACD-PAA-MIB", "acdPaaResultPktLossFePrevNbrLoss"),
        ("ACD-PAA-MIB", "acdPaaResultVlan1IdMismatch"),
        ("ACD-PAA-MIB", "acdPaaResultVlan1IdExpected"),
        ("ACD-PAA-MIB", "acdPaaResultVlan1IdReceived"),
        ("ACD-PAA-MIB", "acdPaaResultVlan2IdMismatch"),
        ("ACD-PAA-MIB", "acdPaaResultVlan2IdExpected"),
        ("ACD-PAA-MIB", "acdPaaResultVlan2IdReceived"),
        ("ACD-PAA-MIB", "acdPaaResultVlan1PriorityMismatch"),
        ("ACD-PAA-MIB", "acdPaaResultVlan1PriorityExpected"),
        ("ACD-PAA-MIB", "acdPaaResultVlan1PriorityReceived"),
        ("ACD-PAA-MIB", "acdPaaResultVlan2PriorityMismatch"),
        ("ACD-PAA-MIB", "acdPaaResultVlan2PriorityExpected"),
        ("ACD-PAA-MIB", "acdPaaResultVlan2PriorityReceived"),
        ("ACD-PAA-MIB", "acdPaaResultDscpMismatch"),
        ("ACD-PAA-MIB", "acdPaaResultDscpExpected"),
        ("ACD-PAA-MIB", "acdPaaResultDscpReceived"))
)
if mibBuilder.loadTexts:
    acdPaaResultGroup.setStatus("current")

acdPaaStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 2, 2)
)
acdPaaStatusGroup.setObjects(
      *(("ACD-PAA-MIB", "acdPaaStatusCcAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusPktLossAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusOneWayDelayAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusOneWayAvgDelayAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusOneWayDvAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusOneWayAvgDvAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusTwoWayDelayAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusTwoWayAvgDelayAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusTwoWayDvAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusTwoWayAvgDvAlert"),
        ("ACD-PAA-MIB", "acdPaaStatusState"),
        ("ACD-PAA-MIB", "acdPaaStatusPeerAddress"))
)
if mibBuilder.loadTexts:
    acdPaaStatusGroup.setStatus("current")

acdPaaUdpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 2, 3)
)
acdPaaUdpCfgGroup.setObjects(
      *(("ACD-PAA-MIB", "acdPaaUdpCfgName"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgState"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgPktSize"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgSamplingPeriod"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgCcLossThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgPktLossRefPeriod"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgPktLossThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOneWayRefPeriod"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOneWayDvMax"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOneWayDvThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOneWayAvgDvThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgTwoWayRefPeriod"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgTwoWayDelayMax"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgTwoWayDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgTwoWayAvgDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgTwoWayDvMax"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgTwoWayDvThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgTwoWayAvgDvThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIPv4DstAddr"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgPortNumber"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgDscpValue"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgVlan1PbitsValue"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgVlan2PbitsValue"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOneWayDelayMax"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOneWayDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOneWayAvgDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgDestinationPortNumber"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgPeerID"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgOperationMode"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpOneWayJoinPeriod"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpRefPeriod"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpMaxJoinDly"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpJoinDlyThres"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpJoinAvgDlyThres"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpMaxLvDly"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpLvDlyThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgIgmpLvAvgDlyThresh"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgPktLossThreshExt"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgVlan1PriorityValidation"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgVlan1PriorityTxRxCoupling"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgVlan1PriorityExpected"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgDscpValidation"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgDscpTxRxCoupling"),
        ("ACD-PAA-MIB", "acdPaaUdpCfgDscpExpected"))
)
if mibBuilder.loadTexts:
    acdPaaUdpCfgGroup.setStatus("current")

acdPaaL2CfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 2, 4)
)
acdPaaL2CfgGroup.setObjects(
      *(("ACD-PAA-MIB", "acdPaaL2CfgName"),
        ("ACD-PAA-MIB", "acdPaaL2CfgState"),
        ("ACD-PAA-MIB", "acdPaaL2CfgPktSize"),
        ("ACD-PAA-MIB", "acdPaaL2CfgSamplingPeriod"),
        ("ACD-PAA-MIB", "acdPaaL2CfgCcLossThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgPktLossRefPeriod"),
        ("ACD-PAA-MIB", "acdPaaL2CfgPktLossThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOneWayRefPeriod"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOneWayDvMax"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOneWayDvThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOneWayAvgDvThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgTwoWayRefPeriod"),
        ("ACD-PAA-MIB", "acdPaaL2CfgTwoWayDelayMax"),
        ("ACD-PAA-MIB", "acdPaaL2CfgTwoWayDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgTwoWayAvgDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgTwoWayDvMax"),
        ("ACD-PAA-MIB", "acdPaaL2CfgTwoWayDvThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgTwoWayAvgDvThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgPortName"),
        ("ACD-PAA-MIB", "acdPaaL2CfgMacDst"),
        ("ACD-PAA-MIB", "acdPaaL2CfgEtype"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1IdEn"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1Id"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2IdEn"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2Id"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1PbitsValue"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2PbitsValue"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOneWayDelayMax"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOneWayDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOneWayAvgDelayThresh"),
        ("ACD-PAA-MIB", "acdPaaL2CfgPeerID"),
        ("ACD-PAA-MIB", "acdPaaL2CfgOperationMode"),
        ("ACD-PAA-MIB", "acdPaaL2CfgPktLossThreshExt"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1IdValidation"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1IdTxRxCoupling"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1IdExpected"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2IdValidation"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2IdTxRxCoupling"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2IdExpected"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1PriorityValidation"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1PriorityTxRxCoupling"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan1PriorityExpected"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2PriorityValidation"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2PriorityTxRxCoupling"),
        ("ACD-PAA-MIB", "acdPaaL2CfgVlan2PriorityExpected"))
)
if mibBuilder.loadTexts:
    acdPaaL2CfgGroup.setStatus("current")

acdPaaHistResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 2, 5)
)
acdPaaHistResultGroup.setObjects(
      *(("ACD-PAA-MIB", "acdPaaHistResultStatus"),
        ("ACD-PAA-MIB", "acdPaaHistResultDuration"),
        ("ACD-PAA-MIB", "acdPaaHistResultIntervalEnd"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossNeValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossNeSamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossNeValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossFeValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossFeSamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossFeValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDelayValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDelaySamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDelayMinValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDelayMaxValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDelayAvgValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDelayThreshEx"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDvValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDvSamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDvMinValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDvMaxValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDvAvgValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultOneWayDvThreshEx"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDelayValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDelaySamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDelayMinValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDelayMaxValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDelayAvgValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDelayThreshEx"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDvValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDvSamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDvMinValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDvMaxValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDvAvgValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultTwoWayDvThreshEx"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpJoinDelayValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpJoinDelaySamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpJoinDelayMinValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpJoinDelayMaxValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpJoinDelayAvgValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpJoinDelayThreshEx"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpLeaveDelayValid"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpLeaveDelaySamples"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpLeaveDelayMinValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpLeaveDelayMaxValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpLeaveDelayAvgValue"),
        ("ACD-PAA-MIB", "acdPaaHistResultIgmpLeaveDelayThreshEx"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossNeValueExt"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossFeValueExt"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossNeNbrLoss"),
        ("ACD-PAA-MIB", "acdPaaHistResultPktLossFeNbrLoss"))
)
if mibBuilder.loadTexts:
    acdPaaHistResultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdPaaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 5, 9, 1, 1)
)
if mibBuilder.loadTexts:
    acdPaaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-PAA-MIB",
    **{"acdPaa": acdPaa,
       "acdPaaResultTable": acdPaaResultTable,
       "acdPaaResultEntry": acdPaaResultEntry,
       "acdPaaResultID": acdPaaResultID,
       "acdPaaResultState": acdPaaResultState,
       "acdPaaResultPktLossNeCurrValid": acdPaaResultPktLossNeCurrValid,
       "acdPaaResultPktLossNeCurrValue": acdPaaResultPktLossNeCurrValue,
       "acdPaaResultPktLossNePrevValid": acdPaaResultPktLossNePrevValid,
       "acdPaaResultPktLossNePrevValue": acdPaaResultPktLossNePrevValue,
       "acdPaaResultPktLossFeCurrValid": acdPaaResultPktLossFeCurrValid,
       "acdPaaResultPktLossFeCurrValue": acdPaaResultPktLossFeCurrValue,
       "acdPaaResultPktLossFePrevValid": acdPaaResultPktLossFePrevValid,
       "acdPaaResultPktLossFePrevValue": acdPaaResultPktLossFePrevValue,
       "acdPaaResultOneWayDvInstValue": acdPaaResultOneWayDvInstValue,
       "acdPaaResultOneWayDvCurrValid": acdPaaResultOneWayDvCurrValid,
       "acdPaaResultOneWayDvCurrMinValue": acdPaaResultOneWayDvCurrMinValue,
       "acdPaaResultOneWayDvCurrMaxValue": acdPaaResultOneWayDvCurrMaxValue,
       "acdPaaResultOneWayDvCurrAvgValue": acdPaaResultOneWayDvCurrAvgValue,
       "acdPaaResultOneWayDvCurrThreshExc": acdPaaResultOneWayDvCurrThreshExc,
       "acdPaaResultOneWayDvPrevValid": acdPaaResultOneWayDvPrevValid,
       "acdPaaResultOneWayDvPrevMinValue": acdPaaResultOneWayDvPrevMinValue,
       "acdPaaResultOneWayDvPrevMaxValue": acdPaaResultOneWayDvPrevMaxValue,
       "acdPaaResultOneWayDvPrevAvgValue": acdPaaResultOneWayDvPrevAvgValue,
       "acdPaaResultOneWayDvPrevThreshEx": acdPaaResultOneWayDvPrevThreshEx,
       "acdPaaResultTwoWayDelayInstValue": acdPaaResultTwoWayDelayInstValue,
       "acdPaaResultTwoWayDelayCurrValid": acdPaaResultTwoWayDelayCurrValid,
       "acdPaaResultTwoWayDelayCurrMinValue": acdPaaResultTwoWayDelayCurrMinValue,
       "acdPaaResultTwoWayDelayCurrMaxValue": acdPaaResultTwoWayDelayCurrMaxValue,
       "acdPaaResultTwoWayDelayCurrAvgValue": acdPaaResultTwoWayDelayCurrAvgValue,
       "acdPaaResultTwoWayDelayCurrThreshEx": acdPaaResultTwoWayDelayCurrThreshEx,
       "acdPaaResultTwoWayDelayPrevValid": acdPaaResultTwoWayDelayPrevValid,
       "acdPaaResultTwoWayDelayPrevMinValue": acdPaaResultTwoWayDelayPrevMinValue,
       "acdPaaResultTwoWayDelayPrevMaxValue": acdPaaResultTwoWayDelayPrevMaxValue,
       "acdPaaResultTwoWayDelayPrevAvgValue": acdPaaResultTwoWayDelayPrevAvgValue,
       "acdPaaResultTwoWayDelayPrevThreshEx": acdPaaResultTwoWayDelayPrevThreshEx,
       "acdPaaResultTwoWayDvInstValue": acdPaaResultTwoWayDvInstValue,
       "acdPaaResultTwoWayDvCurrValid": acdPaaResultTwoWayDvCurrValid,
       "acdPaaResultTwoWayDvCurrMinValue": acdPaaResultTwoWayDvCurrMinValue,
       "acdPaaResultTwoWayDvCurrMaxValue": acdPaaResultTwoWayDvCurrMaxValue,
       "acdPaaResultTwoWayDvCurrAvgValue": acdPaaResultTwoWayDvCurrAvgValue,
       "acdPaaResultTwoWayDvCurrThreshEx": acdPaaResultTwoWayDvCurrThreshEx,
       "acdPaaResultTwoWayDvPrevValid": acdPaaResultTwoWayDvPrevValid,
       "acdPaaResultTwoWayDvPrevMinValue": acdPaaResultTwoWayDvPrevMinValue,
       "acdPaaResultTwoWayDvPrevMaxValue": acdPaaResultTwoWayDvPrevMaxValue,
       "acdPaaResultTwoWayDvPrevAvgValue": acdPaaResultTwoWayDvPrevAvgValue,
       "acdPaaResultTwoWayDvPrevThreshEx": acdPaaResultTwoWayDvPrevThreshEx,
       "acdPaaResultOneWayDelayInstValue": acdPaaResultOneWayDelayInstValue,
       "acdPaaResultOneWayDelayCurrValid": acdPaaResultOneWayDelayCurrValid,
       "acdPaaResultOneWayDelayCurrMinValue": acdPaaResultOneWayDelayCurrMinValue,
       "acdPaaResultOneWayDelayCurrMaxValue": acdPaaResultOneWayDelayCurrMaxValue,
       "acdPaaResultOneWayDelayCurrAvgValue": acdPaaResultOneWayDelayCurrAvgValue,
       "acdPaaResultOneWayDelayCurrThreshEx": acdPaaResultOneWayDelayCurrThreshEx,
       "acdPaaResultOneWayDelayPrevValid": acdPaaResultOneWayDelayPrevValid,
       "acdPaaResultOneWayDelayPrevMinValue": acdPaaResultOneWayDelayPrevMinValue,
       "acdPaaResultOneWayDelayPrevMaxValue": acdPaaResultOneWayDelayPrevMaxValue,
       "acdPaaResultOneWayDelayPrevAvgValue": acdPaaResultOneWayDelayPrevAvgValue,
       "acdPaaResultOneWayDelayPrevThreshEx": acdPaaResultOneWayDelayPrevThreshEx,
       "acdPaaResultPktLossTime": acdPaaResultPktLossTime,
       "acdPaaResultOneWayTime": acdPaaResultOneWayTime,
       "acdPaaResultTwoWayTime": acdPaaResultTwoWayTime,
       "acdPaaResultPktLossNeCurrSamples": acdPaaResultPktLossNeCurrSamples,
       "acdPaaResultPktLossNePrevSamples": acdPaaResultPktLossNePrevSamples,
       "acdPaaResultPktLossFeCurrSamples": acdPaaResultPktLossFeCurrSamples,
       "acdPaaResultPktLossFePrevSamples": acdPaaResultPktLossFePrevSamples,
       "acdPaaResultOneWayDelayCurrSamples": acdPaaResultOneWayDelayCurrSamples,
       "acdPaaResultOneWayDelayPrevSamples": acdPaaResultOneWayDelayPrevSamples,
       "acdPaaResultOneWayDvCurrSamples": acdPaaResultOneWayDvCurrSamples,
       "acdPaaResultOneWayDvPrevSamples": acdPaaResultOneWayDvPrevSamples,
       "acdPaaResultTwoWayDelayCurrSamples": acdPaaResultTwoWayDelayCurrSamples,
       "acdPaaResultTwoWayDelayPrevSamples": acdPaaResultTwoWayDelayPrevSamples,
       "acdPaaResultTwoWayDvCurrSamples": acdPaaResultTwoWayDvCurrSamples,
       "acdPaaResultTwoWayDvPrevSamples": acdPaaResultTwoWayDvPrevSamples,
       "acdPaaResultIgmpJoinDelayInstValue": acdPaaResultIgmpJoinDelayInstValue,
       "acdPaaResultIgmpJoinDelayCurrValid": acdPaaResultIgmpJoinDelayCurrValid,
       "acdPaaResultIgmpJoinDelayCurrMinValue": acdPaaResultIgmpJoinDelayCurrMinValue,
       "acdPaaResultIgmpJoinDelayCurrMaxValue": acdPaaResultIgmpJoinDelayCurrMaxValue,
       "acdPaaResultIgmpJoinDelayCurrAvgValue": acdPaaResultIgmpJoinDelayCurrAvgValue,
       "acdPaaResultIgmpJoinDelayCurrThreshEx": acdPaaResultIgmpJoinDelayCurrThreshEx,
       "acdPaaResultIgmpJoinDelayPrevValid": acdPaaResultIgmpJoinDelayPrevValid,
       "acdPaaResultIgmpJoinDelayPrevMinValue": acdPaaResultIgmpJoinDelayPrevMinValue,
       "acdPaaResultIgmpJoinDelayPrevMaxValue": acdPaaResultIgmpJoinDelayPrevMaxValue,
       "acdPaaResultIgmpJoinDelayPrevAvgValue": acdPaaResultIgmpJoinDelayPrevAvgValue,
       "acdPaaResultIgmpJoinDelayPrevThreshEx": acdPaaResultIgmpJoinDelayPrevThreshEx,
       "acdPaaResultIgmpLeaveDelayInstValue": acdPaaResultIgmpLeaveDelayInstValue,
       "acdPaaResultIgmpLeaveDelayCurrValid": acdPaaResultIgmpLeaveDelayCurrValid,
       "acdPaaResultIgmpLeaveDelayCurrMinValue": acdPaaResultIgmpLeaveDelayCurrMinValue,
       "acdPaaResultIgmpLeaveDelayCurrMaxValue": acdPaaResultIgmpLeaveDelayCurrMaxValue,
       "acdPaaResultIgmpLeaveDelayCurrAvgValue": acdPaaResultIgmpLeaveDelayCurrAvgValue,
       "acdPaaResultIgmpLeaveDelayCurrThreshEx": acdPaaResultIgmpLeaveDelayCurrThreshEx,
       "acdPaaResultIgmpLeaveDelayPrevValid": acdPaaResultIgmpLeaveDelayPrevValid,
       "acdPaaResultIgmpLeaveDelayPrevMinValue": acdPaaResultIgmpLeaveDelayPrevMinValue,
       "acdPaaResultIgmpLeaveDelayPrevMaxValue": acdPaaResultIgmpLeaveDelayPrevMaxValue,
       "acdPaaResultIgmpLeaveDelayPrevAvgValue": acdPaaResultIgmpLeaveDelayPrevAvgValue,
       "acdPaaResultIgmpLeaveDelayPrevThreshEx": acdPaaResultIgmpLeaveDelayPrevThreshEx,
       "acdPaaResultIgmpJoinDelayTime": acdPaaResultIgmpJoinDelayTime,
       "acdPaaResultIgmpLeaveDelayTime": acdPaaResultIgmpLeaveDelayTime,
       "acdPaaResultIgmpJoinDelayCurrSamples": acdPaaResultIgmpJoinDelayCurrSamples,
       "acdPaaResultIgmpJoinDelayPrevSamples": acdPaaResultIgmpJoinDelayPrevSamples,
       "acdPaaResultIgmpLeaveDelayCurrSamples": acdPaaResultIgmpLeaveDelayCurrSamples,
       "acdPaaResultIgmpLeaveDelayPrevSamples": acdPaaResultIgmpLeaveDelayPrevSamples,
       "acdPaaResultPktLossCurrGaps": acdPaaResultPktLossCurrGaps,
       "acdPaaResultPktLossPrevGaps": acdPaaResultPktLossPrevGaps,
       "acdPaaResultPktLossCurrLargestGap": acdPaaResultPktLossCurrLargestGap,
       "acdPaaResultPktLossPrevLargestGap": acdPaaResultPktLossPrevLargestGap,
       "acdPaaResultPktLossNeCurrValueExt": acdPaaResultPktLossNeCurrValueExt,
       "acdPaaResultPktLossNePrevValueExt": acdPaaResultPktLossNePrevValueExt,
       "acdPaaResultPktLossFeCurrValueExt": acdPaaResultPktLossFeCurrValueExt,
       "acdPaaResultPktLossFePrevValueExt": acdPaaResultPktLossFePrevValueExt,
       "acdPaaResultPktLossNeCurrNbrLoss": acdPaaResultPktLossNeCurrNbrLoss,
       "acdPaaResultPktLossNePrevNbrLoss": acdPaaResultPktLossNePrevNbrLoss,
       "acdPaaResultPktLossFeCurrNbrLoss": acdPaaResultPktLossFeCurrNbrLoss,
       "acdPaaResultPktLossFePrevNbrLoss": acdPaaResultPktLossFePrevNbrLoss,
       "acdPaaResultVlan1IdMismatch": acdPaaResultVlan1IdMismatch,
       "acdPaaResultVlan1IdExpected": acdPaaResultVlan1IdExpected,
       "acdPaaResultVlan1IdReceived": acdPaaResultVlan1IdReceived,
       "acdPaaResultVlan2IdMismatch": acdPaaResultVlan2IdMismatch,
       "acdPaaResultVlan2IdExpected": acdPaaResultVlan2IdExpected,
       "acdPaaResultVlan2IdReceived": acdPaaResultVlan2IdReceived,
       "acdPaaResultVlan1PriorityMismatch": acdPaaResultVlan1PriorityMismatch,
       "acdPaaResultVlan1PriorityExpected": acdPaaResultVlan1PriorityExpected,
       "acdPaaResultVlan1PriorityReceived": acdPaaResultVlan1PriorityReceived,
       "acdPaaResultVlan2PriorityMismatch": acdPaaResultVlan2PriorityMismatch,
       "acdPaaResultVlan2PriorityExpected": acdPaaResultVlan2PriorityExpected,
       "acdPaaResultVlan2PriorityReceived": acdPaaResultVlan2PriorityReceived,
       "acdPaaResultDscpMismatch": acdPaaResultDscpMismatch,
       "acdPaaResultDscpExpected": acdPaaResultDscpExpected,
       "acdPaaResultDscpReceived": acdPaaResultDscpReceived,
       "acdPaaStatusTable": acdPaaStatusTable,
       "acdPaaStatusEntry": acdPaaStatusEntry,
       "acdPaaStatusID": acdPaaStatusID,
       "acdPaaStatusCcAlert": acdPaaStatusCcAlert,
       "acdPaaStatusPktLossAlert": acdPaaStatusPktLossAlert,
       "acdPaaStatusOneWayDvAlert": acdPaaStatusOneWayDvAlert,
       "acdPaaStatusOneWayAvgDvAlert": acdPaaStatusOneWayAvgDvAlert,
       "acdPaaStatusTwoWayDelayAlert": acdPaaStatusTwoWayDelayAlert,
       "acdPaaStatusTwoWayAvgDelayAlert": acdPaaStatusTwoWayAvgDelayAlert,
       "acdPaaStatusTwoWayDvAlert": acdPaaStatusTwoWayDvAlert,
       "acdPaaStatusTwoWayAvgDvAlert": acdPaaStatusTwoWayAvgDvAlert,
       "acdPaaStatusOneWayDelayAlert": acdPaaStatusOneWayDelayAlert,
       "acdPaaStatusOneWayAvgDelayAlert": acdPaaStatusOneWayAvgDelayAlert,
       "acdPaaStatusState": acdPaaStatusState,
       "acdPaaStatusPeerAddress": acdPaaStatusPeerAddress,
       "acdPaaUdpCfgTable": acdPaaUdpCfgTable,
       "acdPaaUdpCfgEntry": acdPaaUdpCfgEntry,
       "acdPaaUdpCfgID": acdPaaUdpCfgID,
       "acdPaaUdpCfgName": acdPaaUdpCfgName,
       "acdPaaUdpCfgState": acdPaaUdpCfgState,
       "acdPaaUdpCfgPktSize": acdPaaUdpCfgPktSize,
       "acdPaaUdpCfgSamplingPeriod": acdPaaUdpCfgSamplingPeriod,
       "acdPaaUdpCfgCcLossThresh": acdPaaUdpCfgCcLossThresh,
       "acdPaaUdpCfgPktLossRefPeriod": acdPaaUdpCfgPktLossRefPeriod,
       "acdPaaUdpCfgPktLossThresh": acdPaaUdpCfgPktLossThresh,
       "acdPaaUdpCfgOneWayRefPeriod": acdPaaUdpCfgOneWayRefPeriod,
       "acdPaaUdpCfgOneWayDvMax": acdPaaUdpCfgOneWayDvMax,
       "acdPaaUdpCfgOneWayDvThresh": acdPaaUdpCfgOneWayDvThresh,
       "acdPaaUdpCfgOneWayAvgDvThresh": acdPaaUdpCfgOneWayAvgDvThresh,
       "acdPaaUdpCfgTwoWayRefPeriod": acdPaaUdpCfgTwoWayRefPeriod,
       "acdPaaUdpCfgTwoWayDelayMax": acdPaaUdpCfgTwoWayDelayMax,
       "acdPaaUdpCfgTwoWayDelayThresh": acdPaaUdpCfgTwoWayDelayThresh,
       "acdPaaUdpCfgTwoWayAvgDelayThresh": acdPaaUdpCfgTwoWayAvgDelayThresh,
       "acdPaaUdpCfgTwoWayDvMax": acdPaaUdpCfgTwoWayDvMax,
       "acdPaaUdpCfgTwoWayDvThresh": acdPaaUdpCfgTwoWayDvThresh,
       "acdPaaUdpCfgTwoWayAvgDvThresh": acdPaaUdpCfgTwoWayAvgDvThresh,
       "acdPaaUdpCfgIPv4DstAddr": acdPaaUdpCfgIPv4DstAddr,
       "acdPaaUdpCfgPortNumber": acdPaaUdpCfgPortNumber,
       "acdPaaUdpCfgDscpValue": acdPaaUdpCfgDscpValue,
       "acdPaaUdpCfgVlan1PbitsValue": acdPaaUdpCfgVlan1PbitsValue,
       "acdPaaUdpCfgVlan2PbitsValue": acdPaaUdpCfgVlan2PbitsValue,
       "acdPaaUdpCfgOneWayDelayMax": acdPaaUdpCfgOneWayDelayMax,
       "acdPaaUdpCfgOneWayDelayThresh": acdPaaUdpCfgOneWayDelayThresh,
       "acdPaaUdpCfgOneWayAvgDelayThresh": acdPaaUdpCfgOneWayAvgDelayThresh,
       "acdPaaUdpCfgDestinationPortNumber": acdPaaUdpCfgDestinationPortNumber,
       "acdPaaUdpCfgPeerID": acdPaaUdpCfgPeerID,
       "acdPaaUdpCfgOperationMode": acdPaaUdpCfgOperationMode,
       "acdPaaUdpCfgIgmpOneWayJoinPeriod": acdPaaUdpCfgIgmpOneWayJoinPeriod,
       "acdPaaUdpCfgIgmpRefPeriod": acdPaaUdpCfgIgmpRefPeriod,
       "acdPaaUdpCfgIgmpMaxJoinDly": acdPaaUdpCfgIgmpMaxJoinDly,
       "acdPaaUdpCfgIgmpJoinDlyThres": acdPaaUdpCfgIgmpJoinDlyThres,
       "acdPaaUdpCfgIgmpJoinAvgDlyThres": acdPaaUdpCfgIgmpJoinAvgDlyThres,
       "acdPaaUdpCfgIgmpMaxLvDly": acdPaaUdpCfgIgmpMaxLvDly,
       "acdPaaUdpCfgIgmpLvDlyThresh": acdPaaUdpCfgIgmpLvDlyThresh,
       "acdPaaUdpCfgIgmpLvAvgDlyThresh": acdPaaUdpCfgIgmpLvAvgDlyThresh,
       "acdPaaUdpCfgPktLossThreshExt": acdPaaUdpCfgPktLossThreshExt,
       "acdPaaUdpCfgVlan1PriorityValidation": acdPaaUdpCfgVlan1PriorityValidation,
       "acdPaaUdpCfgVlan1PriorityTxRxCoupling": acdPaaUdpCfgVlan1PriorityTxRxCoupling,
       "acdPaaUdpCfgVlan1PriorityExpected": acdPaaUdpCfgVlan1PriorityExpected,
       "acdPaaUdpCfgDscpValidation": acdPaaUdpCfgDscpValidation,
       "acdPaaUdpCfgDscpTxRxCoupling": acdPaaUdpCfgDscpTxRxCoupling,
       "acdPaaUdpCfgDscpExpected": acdPaaUdpCfgDscpExpected,
       "acdPaaL2CfgTable": acdPaaL2CfgTable,
       "acdPaaL2CfgEntry": acdPaaL2CfgEntry,
       "acdPaaL2CfgID": acdPaaL2CfgID,
       "acdPaaL2CfgName": acdPaaL2CfgName,
       "acdPaaL2CfgState": acdPaaL2CfgState,
       "acdPaaL2CfgPktSize": acdPaaL2CfgPktSize,
       "acdPaaL2CfgSamplingPeriod": acdPaaL2CfgSamplingPeriod,
       "acdPaaL2CfgCcLossThresh": acdPaaL2CfgCcLossThresh,
       "acdPaaL2CfgPktLossRefPeriod": acdPaaL2CfgPktLossRefPeriod,
       "acdPaaL2CfgPktLossThresh": acdPaaL2CfgPktLossThresh,
       "acdPaaL2CfgOneWayRefPeriod": acdPaaL2CfgOneWayRefPeriod,
       "acdPaaL2CfgOneWayDvMax": acdPaaL2CfgOneWayDvMax,
       "acdPaaL2CfgOneWayDvThresh": acdPaaL2CfgOneWayDvThresh,
       "acdPaaL2CfgOneWayAvgDvThresh": acdPaaL2CfgOneWayAvgDvThresh,
       "acdPaaL2CfgTwoWayRefPeriod": acdPaaL2CfgTwoWayRefPeriod,
       "acdPaaL2CfgTwoWayDelayMax": acdPaaL2CfgTwoWayDelayMax,
       "acdPaaL2CfgTwoWayDelayThresh": acdPaaL2CfgTwoWayDelayThresh,
       "acdPaaL2CfgTwoWayAvgDelayThresh": acdPaaL2CfgTwoWayAvgDelayThresh,
       "acdPaaL2CfgTwoWayDvMax": acdPaaL2CfgTwoWayDvMax,
       "acdPaaL2CfgTwoWayDvThresh": acdPaaL2CfgTwoWayDvThresh,
       "acdPaaL2CfgTwoWayAvgDvThresh": acdPaaL2CfgTwoWayAvgDvThresh,
       "acdPaaL2CfgPortName": acdPaaL2CfgPortName,
       "acdPaaL2CfgMacDst": acdPaaL2CfgMacDst,
       "acdPaaL2CfgEtype": acdPaaL2CfgEtype,
       "acdPaaL2CfgVlan1IdEn": acdPaaL2CfgVlan1IdEn,
       "acdPaaL2CfgVlan1Id": acdPaaL2CfgVlan1Id,
       "acdPaaL2CfgVlan2IdEn": acdPaaL2CfgVlan2IdEn,
       "acdPaaL2CfgVlan2Id": acdPaaL2CfgVlan2Id,
       "acdPaaL2CfgVlan1PbitsValue": acdPaaL2CfgVlan1PbitsValue,
       "acdPaaL2CfgVlan2PbitsValue": acdPaaL2CfgVlan2PbitsValue,
       "acdPaaL2CfgOneWayDelayMax": acdPaaL2CfgOneWayDelayMax,
       "acdPaaL2CfgOneWayDelayThresh": acdPaaL2CfgOneWayDelayThresh,
       "acdPaaL2CfgOneWayAvgDelayThresh": acdPaaL2CfgOneWayAvgDelayThresh,
       "acdPaaL2CfgPeerID": acdPaaL2CfgPeerID,
       "acdPaaL2CfgOperationMode": acdPaaL2CfgOperationMode,
       "acdPaaL2CfgPktLossThreshExt": acdPaaL2CfgPktLossThreshExt,
       "acdPaaL2CfgVlan1IdValidation": acdPaaL2CfgVlan1IdValidation,
       "acdPaaL2CfgVlan1IdTxRxCoupling": acdPaaL2CfgVlan1IdTxRxCoupling,
       "acdPaaL2CfgVlan1IdExpected": acdPaaL2CfgVlan1IdExpected,
       "acdPaaL2CfgVlan2IdValidation": acdPaaL2CfgVlan2IdValidation,
       "acdPaaL2CfgVlan2IdTxRxCoupling": acdPaaL2CfgVlan2IdTxRxCoupling,
       "acdPaaL2CfgVlan2IdExpected": acdPaaL2CfgVlan2IdExpected,
       "acdPaaL2CfgVlan1PriorityValidation": acdPaaL2CfgVlan1PriorityValidation,
       "acdPaaL2CfgVlan1PriorityTxRxCoupling": acdPaaL2CfgVlan1PriorityTxRxCoupling,
       "acdPaaL2CfgVlan1PriorityExpected": acdPaaL2CfgVlan1PriorityExpected,
       "acdPaaL2CfgVlan2PriorityValidation": acdPaaL2CfgVlan2PriorityValidation,
       "acdPaaL2CfgVlan2PriorityTxRxCoupling": acdPaaL2CfgVlan2PriorityTxRxCoupling,
       "acdPaaL2CfgVlan2PriorityExpected": acdPaaL2CfgVlan2PriorityExpected,
       "acdPaaHistResultTable": acdPaaHistResultTable,
       "acdPaaHistResultEntry": acdPaaHistResultEntry,
       "acdPaaHistResultID": acdPaaHistResultID,
       "acdPaaHistResultSampleIndex": acdPaaHistResultSampleIndex,
       "acdPaaHistResultStatus": acdPaaHistResultStatus,
       "acdPaaHistResultDuration": acdPaaHistResultDuration,
       "acdPaaHistResultIntervalEnd": acdPaaHistResultIntervalEnd,
       "acdPaaHistResultPktLossNeValid": acdPaaHistResultPktLossNeValid,
       "acdPaaHistResultPktLossNeSamples": acdPaaHistResultPktLossNeSamples,
       "acdPaaHistResultPktLossNeValue": acdPaaHistResultPktLossNeValue,
       "acdPaaHistResultPktLossFeValid": acdPaaHistResultPktLossFeValid,
       "acdPaaHistResultPktLossFeSamples": acdPaaHistResultPktLossFeSamples,
       "acdPaaHistResultPktLossFeValue": acdPaaHistResultPktLossFeValue,
       "acdPaaHistResultOneWayDelayValid": acdPaaHistResultOneWayDelayValid,
       "acdPaaHistResultOneWayDelaySamples": acdPaaHistResultOneWayDelaySamples,
       "acdPaaHistResultOneWayDelayMinValue": acdPaaHistResultOneWayDelayMinValue,
       "acdPaaHistResultOneWayDelayMaxValue": acdPaaHistResultOneWayDelayMaxValue,
       "acdPaaHistResultOneWayDelayAvgValue": acdPaaHistResultOneWayDelayAvgValue,
       "acdPaaHistResultOneWayDelayThreshEx": acdPaaHistResultOneWayDelayThreshEx,
       "acdPaaHistResultOneWayDvValid": acdPaaHistResultOneWayDvValid,
       "acdPaaHistResultOneWayDvSamples": acdPaaHistResultOneWayDvSamples,
       "acdPaaHistResultOneWayDvMinValue": acdPaaHistResultOneWayDvMinValue,
       "acdPaaHistResultOneWayDvMaxValue": acdPaaHistResultOneWayDvMaxValue,
       "acdPaaHistResultOneWayDvAvgValue": acdPaaHistResultOneWayDvAvgValue,
       "acdPaaHistResultOneWayDvThreshEx": acdPaaHistResultOneWayDvThreshEx,
       "acdPaaHistResultTwoWayDelayValid": acdPaaHistResultTwoWayDelayValid,
       "acdPaaHistResultTwoWayDelaySamples": acdPaaHistResultTwoWayDelaySamples,
       "acdPaaHistResultTwoWayDelayMinValue": acdPaaHistResultTwoWayDelayMinValue,
       "acdPaaHistResultTwoWayDelayMaxValue": acdPaaHistResultTwoWayDelayMaxValue,
       "acdPaaHistResultTwoWayDelayAvgValue": acdPaaHistResultTwoWayDelayAvgValue,
       "acdPaaHistResultTwoWayDelayThreshEx": acdPaaHistResultTwoWayDelayThreshEx,
       "acdPaaHistResultTwoWayDvValid": acdPaaHistResultTwoWayDvValid,
       "acdPaaHistResultTwoWayDvSamples": acdPaaHistResultTwoWayDvSamples,
       "acdPaaHistResultTwoWayDvMinValue": acdPaaHistResultTwoWayDvMinValue,
       "acdPaaHistResultTwoWayDvMaxValue": acdPaaHistResultTwoWayDvMaxValue,
       "acdPaaHistResultTwoWayDvAvgValue": acdPaaHistResultTwoWayDvAvgValue,
       "acdPaaHistResultTwoWayDvThreshEx": acdPaaHistResultTwoWayDvThreshEx,
       "acdPaaHistResultIgmpJoinDelayValid": acdPaaHistResultIgmpJoinDelayValid,
       "acdPaaHistResultIgmpJoinDelaySamples": acdPaaHistResultIgmpJoinDelaySamples,
       "acdPaaHistResultIgmpJoinDelayMinValue": acdPaaHistResultIgmpJoinDelayMinValue,
       "acdPaaHistResultIgmpJoinDelayMaxValue": acdPaaHistResultIgmpJoinDelayMaxValue,
       "acdPaaHistResultIgmpJoinDelayAvgValue": acdPaaHistResultIgmpJoinDelayAvgValue,
       "acdPaaHistResultIgmpJoinDelayThreshEx": acdPaaHistResultIgmpJoinDelayThreshEx,
       "acdPaaHistResultIgmpLeaveDelayValid": acdPaaHistResultIgmpLeaveDelayValid,
       "acdPaaHistResultIgmpLeaveDelaySamples": acdPaaHistResultIgmpLeaveDelaySamples,
       "acdPaaHistResultIgmpLeaveDelayMinValue": acdPaaHistResultIgmpLeaveDelayMinValue,
       "acdPaaHistResultIgmpLeaveDelayMaxValue": acdPaaHistResultIgmpLeaveDelayMaxValue,
       "acdPaaHistResultIgmpLeaveDelayAvgValue": acdPaaHistResultIgmpLeaveDelayAvgValue,
       "acdPaaHistResultIgmpLeaveDelayThreshEx": acdPaaHistResultIgmpLeaveDelayThreshEx,
       "acdPaaHistResultPktLossNeValueExt": acdPaaHistResultPktLossNeValueExt,
       "acdPaaHistResultPktLossFeValueExt": acdPaaHistResultPktLossFeValueExt,
       "acdPaaHistResultPktLossNeNbrLoss": acdPaaHistResultPktLossNeNbrLoss,
       "acdPaaHistResultPktLossFeNbrLoss": acdPaaHistResultPktLossFeNbrLoss,
       "acdPaaNotifications": acdPaaNotifications,
       "acdPaaMIBObjects": acdPaaMIBObjects,
       "acdPaaConformance": acdPaaConformance,
       "acdPaaCompliances": acdPaaCompliances,
       "acdPaaCompliance": acdPaaCompliance,
       "acdPaaGroups": acdPaaGroups,
       "acdPaaResultGroup": acdPaaResultGroup,
       "acdPaaStatusGroup": acdPaaStatusGroup,
       "acdPaaUdpCfgGroup": acdPaaUdpCfgGroup,
       "acdPaaL2CfgGroup": acdPaaL2CfgGroup,
       "acdPaaHistResultGroup": acdPaaHistResultGroup}
)
