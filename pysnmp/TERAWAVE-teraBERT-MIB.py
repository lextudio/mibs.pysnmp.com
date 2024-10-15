# SNMP MIB module (TERAWAVE-teraBERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraBERT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:14 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraBERTGroup_ObjectIdentity = ObjectIdentity
teraBERTGroup = _TeraBERTGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 16)
)
_TeraBERTConfigureTable_Object = MibTable
teraBERTConfigureTable = _TeraBERTConfigureTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1)
)
if mibBuilder.loadTexts:
    teraBERTConfigureTable.setStatus("mandatory")
_TeraBERTConfigureTableEntry_Object = MibTableRow
teraBERTConfigureTableEntry = _TeraBERTConfigureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1)
)
teraBERTConfigureTableEntry.setIndexNames(
    (0, "TERAWAVE-teraBERT-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraBERTConfigureTableEntry.setStatus("mandatory")


class _TeraBERTCommand_Type(Integer32):
    """Custom type teraBERTCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("insert-err", 4),
          ("none", 0),
          ("start", 1),
          ("stop", 2),
          ("timer", 5))
    )


_TeraBERTCommand_Type.__name__ = "Integer32"
_TeraBERTCommand_Object = MibTableColumn
teraBERTCommand = _TeraBERTCommand_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 1),
    _TeraBERTCommand_Type()
)
teraBERTCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBERTCommand.setStatus("mandatory")


class _TeraBERTTestTime_Type(Integer32):
    """Custom type teraBERTTestTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TeraBERTTestTime_Type.__name__ = "Integer32"
_TeraBERTTestTime_Object = MibTableColumn
teraBERTTestTime = _TeraBERTTestTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 2),
    _TeraBERTTestTime_Type()
)
teraBERTTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBERTTestTime.setStatus("mandatory")


class _TeraBERTSynThreshold_Type(Integer32):
    """Custom type teraBERTSynThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraBERTSynThreshold_Type.__name__ = "Integer32"
_TeraBERTSynThreshold_Object = MibTableColumn
teraBERTSynThreshold = _TeraBERTSynThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 3),
    _TeraBERTSynThreshold_Type()
)
teraBERTSynThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBERTSynThreshold.setStatus("mandatory")


class _TeraBERTSESThresholdMantissa_Type(Integer32):
    """Custom type teraBERTSESThresholdMantissa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TeraBERTSESThresholdMantissa_Type.__name__ = "Integer32"
_TeraBERTSESThresholdMantissa_Object = MibTableColumn
teraBERTSESThresholdMantissa = _TeraBERTSESThresholdMantissa_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 4),
    _TeraBERTSESThresholdMantissa_Type()
)
teraBERTSESThresholdMantissa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBERTSESThresholdMantissa.setStatus("mandatory")


class _TeraBERTSESThresholdExponent_Type(Integer32):
    """Custom type teraBERTSESThresholdExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TeraBERTSESThresholdExponent_Type.__name__ = "Integer32"
_TeraBERTSESThresholdExponent_Object = MibTableColumn
teraBERTSESThresholdExponent = _TeraBERTSESThresholdExponent_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 5),
    _TeraBERTSESThresholdExponent_Type()
)
teraBERTSESThresholdExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBERTSESThresholdExponent.setStatus("mandatory")


class _TeraBERTSynStatus_Type(Integer32):
    """Custom type teraBERTSynStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_TeraBERTSynStatus_Type.__name__ = "Integer32"
_TeraBERTSynStatus_Object = MibTableColumn
teraBERTSynStatus = _TeraBERTSynStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 6),
    _TeraBERTSynStatus_Type()
)
teraBERTSynStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTSynStatus.setStatus("mandatory")
_TeraBERTElapsedTime_Type = Integer32
_TeraBERTElapsedTime_Object = MibTableColumn
teraBERTElapsedTime = _TeraBERTElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 7),
    _TeraBERTElapsedTime_Type()
)
teraBERTElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTElapsedTime.setStatus("mandatory")


class _TeraBERTPattern_Type(Integer32):
    """Custom type teraBERTPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 5),
          ("allZeroes", 6),
          ("alternatingOneZero", 7),
          ("none", 0),
          ("twoE11MinusOne", 1),
          ("twoE15MinusOne", 2),
          ("twoE20MinusOne", 3),
          ("twoE23MinusOne", 4))
    )


_TeraBERTPattern_Type.__name__ = "Integer32"
_TeraBERTPattern_Object = MibTableColumn
teraBERTPattern = _TeraBERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 1, 1, 8),
    _TeraBERTPattern_Type()
)
teraBERTPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBERTPattern.setStatus("mandatory")
_TeraBERTCurrentTable_Object = MibTable
teraBERTCurrentTable = _TeraBERTCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2)
)
if mibBuilder.loadTexts:
    teraBERTCurrentTable.setStatus("mandatory")
_TeraBERTCurrentTableEntry_Object = MibTableRow
teraBERTCurrentTableEntry = _TeraBERTCurrentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2, 1)
)
teraBERTCurrentTableEntry.setIndexNames(
    (0, "TERAWAVE-teraBERT-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraBERTCurrentTableEntry.setStatus("mandatory")
_TeraBERTCurrentCountInSync_Type = Gauge32
_TeraBERTCurrentCountInSync_Object = MibTableColumn
teraBERTCurrentCountInSync = _TeraBERTCurrentCountInSync_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 1),
    _TeraBERTCurrentCountInSync_Type()
)
teraBERTCurrentCountInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTCurrentCountInSync.setStatus("mandatory")
_TeraBERTCurrentRateInSync_Type = Gauge32
_TeraBERTCurrentRateInSync_Object = MibTableColumn
teraBERTCurrentRateInSync = _TeraBERTCurrentRateInSync_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 2),
    _TeraBERTCurrentRateInSync_Type()
)
teraBERTCurrentRateInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTCurrentRateInSync.setStatus("mandatory")
_TeraBERTCurrentESCount_Type = Gauge32
_TeraBERTCurrentESCount_Object = MibTableColumn
teraBERTCurrentESCount = _TeraBERTCurrentESCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 3),
    _TeraBERTCurrentESCount_Type()
)
teraBERTCurrentESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTCurrentESCount.setStatus("mandatory")
_TeraBERTCurrentSESCount_Type = Gauge32
_TeraBERTCurrentSESCount_Object = MibTableColumn
teraBERTCurrentSESCount = _TeraBERTCurrentSESCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 4),
    _TeraBERTCurrentSESCount_Type()
)
teraBERTCurrentSESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTCurrentSESCount.setStatus("mandatory")
_TeraBERTCurrentCSESCount_Type = Gauge32
_TeraBERTCurrentCSESCount_Object = MibTableColumn
teraBERTCurrentCSESCount = _TeraBERTCurrentCSESCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 5),
    _TeraBERTCurrentCSESCount_Type()
)
teraBERTCurrentCSESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTCurrentCSESCount.setStatus("mandatory")
_TeraBERTCurrentUASCount_Type = Gauge32
_TeraBERTCurrentUASCount_Object = MibTableColumn
teraBERTCurrentUASCount = _TeraBERTCurrentUASCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 16, 2, 1, 6),
    _TeraBERTCurrentUASCount_Type()
)
teraBERTCurrentUASCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraBERTCurrentUASCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraBERT-MIB",
    **{"terawave": terawave,
       "teraBERTGroup": teraBERTGroup,
       "teraBERTConfigureTable": teraBERTConfigureTable,
       "teraBERTConfigureTableEntry": teraBERTConfigureTableEntry,
       "teraBERTCommand": teraBERTCommand,
       "teraBERTTestTime": teraBERTTestTime,
       "teraBERTSynThreshold": teraBERTSynThreshold,
       "teraBERTSESThresholdMantissa": teraBERTSESThresholdMantissa,
       "teraBERTSESThresholdExponent": teraBERTSESThresholdExponent,
       "teraBERTSynStatus": teraBERTSynStatus,
       "teraBERTElapsedTime": teraBERTElapsedTime,
       "teraBERTPattern": teraBERTPattern,
       "teraBERTCurrentTable": teraBERTCurrentTable,
       "teraBERTCurrentTableEntry": teraBERTCurrentTableEntry,
       "teraBERTCurrentCountInSync": teraBERTCurrentCountInSync,
       "teraBERTCurrentRateInSync": teraBERTCurrentRateInSync,
       "teraBERTCurrentESCount": teraBERTCurrentESCount,
       "teraBERTCurrentSESCount": teraBERTCurrentSESCount,
       "teraBERTCurrentCSESCount": teraBERTCurrentCSESCount,
       "teraBERTCurrentUASCount": teraBERTCurrentUASCount}
)
