# SNMP MIB module (RFC1406-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1406-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:25 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ds1_ObjectIdentity = ObjectIdentity
ds1 = _Ds1_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 18)
)
_Dsx1ConfigTable_Object = MibTable
dsx1ConfigTable = _Dsx1ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6)
)
if mibBuilder.loadTexts:
    dsx1ConfigTable.setStatus("mandatory")
_Dsx1ConfigEntry_Object = MibTableRow
dsx1ConfigEntry = _Dsx1ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1)
)
dsx1ConfigEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    dsx1ConfigEntry.setStatus("mandatory")


class _Dsx1LineIndex_Type(Integer32):
    """Custom type dsx1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1LineIndex_Type.__name__ = "Integer32"
_Dsx1LineIndex_Object = MibTableColumn
dsx1LineIndex = _Dsx1LineIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 1),
    _Dsx1LineIndex_Type()
)
dsx1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1LineIndex.setStatus("mandatory")


class _Dsx1IfIndex_Type(Integer32):
    """Custom type dsx1IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1IfIndex_Type.__name__ = "Integer32"
_Dsx1IfIndex_Object = MibTableColumn
dsx1IfIndex = _Dsx1IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 2),
    _Dsx1IfIndex_Type()
)
dsx1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IfIndex.setStatus("mandatory")


class _Dsx1TimeElapsed_Type(Integer32):
    """Custom type dsx1TimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_Dsx1TimeElapsed_Type.__name__ = "Integer32"
_Dsx1TimeElapsed_Object = MibTableColumn
dsx1TimeElapsed = _Dsx1TimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 3),
    _Dsx1TimeElapsed_Type()
)
dsx1TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TimeElapsed.setStatus("mandatory")


class _Dsx1ValidIntervals_Type(Integer32):
    """Custom type dsx1ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Dsx1ValidIntervals_Type.__name__ = "Integer32"
_Dsx1ValidIntervals_Object = MibTableColumn
dsx1ValidIntervals = _Dsx1ValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 4),
    _Dsx1ValidIntervals_Type()
)
dsx1ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ValidIntervals.setStatus("mandatory")


class _Dsx1LineType_Type(Integer32):
    """Custom type dsx1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsx1D4", 3),
          ("dsx1E1", 4),
          ("dsx1E1-CRC", 5),
          ("dsx1E1-CRC-MF", 7),
          ("dsx1E1-MF", 6),
          ("dsx1ESF", 2),
          ("other", 1))
    )


_Dsx1LineType_Type.__name__ = "Integer32"
_Dsx1LineType_Object = MibTableColumn
dsx1LineType = _Dsx1LineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 5),
    _Dsx1LineType_Type()
)
dsx1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineType.setStatus("mandatory")


class _Dsx1LineCoding_Type(Integer32):
    """Custom type dsx1LineCoding based on Integer32"""
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
        *(("dsx1AMI", 5),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1JBZS", 1),
          ("dsx1ZBTSI", 4),
          ("other", 6))
    )


_Dsx1LineCoding_Type.__name__ = "Integer32"
_Dsx1LineCoding_Object = MibTableColumn
dsx1LineCoding = _Dsx1LineCoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 6),
    _Dsx1LineCoding_Type()
)
dsx1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineCoding.setStatus("mandatory")


class _Dsx1SendCode_Type(Integer32):
    """Custom type dsx1SendCode based on Integer32"""
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
        *(("dsx1Send3in24Pattern", 7),
          ("dsx1Send511Pattern", 6),
          ("dsx1SendLineCode", 2),
          ("dsx1SendNoCode", 1),
          ("dsx1SendOtherTestPattern", 8),
          ("dsx1SendPayloadCode", 3),
          ("dsx1SendQRS", 5),
          ("dsx1SendResetCode", 4))
    )


_Dsx1SendCode_Type.__name__ = "Integer32"
_Dsx1SendCode_Object = MibTableColumn
dsx1SendCode = _Dsx1SendCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 7),
    _Dsx1SendCode_Type()
)
dsx1SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1SendCode.setStatus("mandatory")


class _Dsx1CircuitIdentifier_Type(DisplayString):
    """Custom type dsx1CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dsx1CircuitIdentifier_Type.__name__ = "DisplayString"
_Dsx1CircuitIdentifier_Object = MibTableColumn
dsx1CircuitIdentifier = _Dsx1CircuitIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 8),
    _Dsx1CircuitIdentifier_Type()
)
dsx1CircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1CircuitIdentifier.setStatus("mandatory")


class _Dsx1LoopbackConfig_Type(Integer32):
    """Custom type dsx1LoopbackConfig based on Integer32"""
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
        *(("dsx1LineLoop", 3),
          ("dsx1NoLoop", 1),
          ("dsx1OtherLoop", 4),
          ("dsx1PayloadLoop", 2))
    )


_Dsx1LoopbackConfig_Type.__name__ = "Integer32"
_Dsx1LoopbackConfig_Object = MibTableColumn
dsx1LoopbackConfig = _Dsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 9),
    _Dsx1LoopbackConfig_Type()
)
dsx1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LoopbackConfig.setStatus("mandatory")


class _Dsx1LineStatus_Type(Integer32):
    """Custom type dsx1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_Dsx1LineStatus_Type.__name__ = "Integer32"
_Dsx1LineStatus_Object = MibTableColumn
dsx1LineStatus = _Dsx1LineStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 10),
    _Dsx1LineStatus_Type()
)
dsx1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1LineStatus.setStatus("mandatory")


class _Dsx1SignalMode_Type(Integer32):
    """Custom type dsx1SignalMode based on Integer32"""
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
        *(("bitOriented", 3),
          ("messageOriented", 4),
          ("none", 1),
          ("robbedBit", 2))
    )


_Dsx1SignalMode_Type.__name__ = "Integer32"
_Dsx1SignalMode_Object = MibTableColumn
dsx1SignalMode = _Dsx1SignalMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 11),
    _Dsx1SignalMode_Type()
)
dsx1SignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1SignalMode.setStatus("mandatory")


class _Dsx1TransmitClockSource_Type(Integer32):
    """Custom type dsx1TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1),
          ("throughTiming", 3))
    )


_Dsx1TransmitClockSource_Type.__name__ = "Integer32"
_Dsx1TransmitClockSource_Object = MibTableColumn
dsx1TransmitClockSource = _Dsx1TransmitClockSource_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 12),
    _Dsx1TransmitClockSource_Type()
)
dsx1TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TransmitClockSource.setStatus("mandatory")


class _Dsx1Fdl_Type(Integer32):
    """Custom type dsx1Fdl based on Integer32"""
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
        *(("dsx1Ansi-T1-403", 2),
          ("dsx1Att-54016", 4),
          ("dsx1Fdl-none", 8),
          ("other", 1))
    )


_Dsx1Fdl_Type.__name__ = "Integer32"
_Dsx1Fdl_Object = MibTableColumn
dsx1Fdl = _Dsx1Fdl_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 13),
    _Dsx1Fdl_Type()
)
dsx1Fdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1Fdl.setStatus("mandatory")
_Dsx1CurrentTable_Object = MibTable
dsx1CurrentTable = _Dsx1CurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7)
)
if mibBuilder.loadTexts:
    dsx1CurrentTable.setStatus("mandatory")
_Dsx1CurrentEntry_Object = MibTableRow
dsx1CurrentEntry = _Dsx1CurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1)
)
dsx1CurrentEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1CurrentIndex"),
)
if mibBuilder.loadTexts:
    dsx1CurrentEntry.setStatus("mandatory")


class _Dsx1CurrentIndex_Type(Integer32):
    """Custom type dsx1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1CurrentIndex_Type.__name__ = "Integer32"
_Dsx1CurrentIndex_Object = MibTableColumn
dsx1CurrentIndex = _Dsx1CurrentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 1),
    _Dsx1CurrentIndex_Type()
)
dsx1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentIndex.setStatus("mandatory")
_Dsx1CurrentESs_Type = Gauge32
_Dsx1CurrentESs_Object = MibTableColumn
dsx1CurrentESs = _Dsx1CurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 2),
    _Dsx1CurrentESs_Type()
)
dsx1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentESs.setStatus("mandatory")
_Dsx1CurrentSESs_Type = Gauge32
_Dsx1CurrentSESs_Object = MibTableColumn
dsx1CurrentSESs = _Dsx1CurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 3),
    _Dsx1CurrentSESs_Type()
)
dsx1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentSESs.setStatus("mandatory")
_Dsx1CurrentSEFSs_Type = Gauge32
_Dsx1CurrentSEFSs_Object = MibTableColumn
dsx1CurrentSEFSs = _Dsx1CurrentSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 4),
    _Dsx1CurrentSEFSs_Type()
)
dsx1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentSEFSs.setStatus("mandatory")
_Dsx1CurrentUASs_Type = Gauge32
_Dsx1CurrentUASs_Object = MibTableColumn
dsx1CurrentUASs = _Dsx1CurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 5),
    _Dsx1CurrentUASs_Type()
)
dsx1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentUASs.setStatus("mandatory")
_Dsx1CurrentCSSs_Type = Gauge32
_Dsx1CurrentCSSs_Object = MibTableColumn
dsx1CurrentCSSs = _Dsx1CurrentCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 6),
    _Dsx1CurrentCSSs_Type()
)
dsx1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentCSSs.setStatus("mandatory")
_Dsx1CurrentPCVs_Type = Gauge32
_Dsx1CurrentPCVs_Object = MibTableColumn
dsx1CurrentPCVs = _Dsx1CurrentPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 7),
    _Dsx1CurrentPCVs_Type()
)
dsx1CurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentPCVs.setStatus("mandatory")
_Dsx1CurrentLESs_Type = Gauge32
_Dsx1CurrentLESs_Object = MibTableColumn
dsx1CurrentLESs = _Dsx1CurrentLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 8),
    _Dsx1CurrentLESs_Type()
)
dsx1CurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLESs.setStatus("mandatory")
_Dsx1CurrentBESs_Type = Gauge32
_Dsx1CurrentBESs_Object = MibTableColumn
dsx1CurrentBESs = _Dsx1CurrentBESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 9),
    _Dsx1CurrentBESs_Type()
)
dsx1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentBESs.setStatus("mandatory")
_Dsx1CurrentDMs_Type = Gauge32
_Dsx1CurrentDMs_Object = MibTableColumn
dsx1CurrentDMs = _Dsx1CurrentDMs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 10),
    _Dsx1CurrentDMs_Type()
)
dsx1CurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentDMs.setStatus("mandatory")
_Dsx1CurrentLCVs_Type = Gauge32
_Dsx1CurrentLCVs_Object = MibTableColumn
dsx1CurrentLCVs = _Dsx1CurrentLCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 11),
    _Dsx1CurrentLCVs_Type()
)
dsx1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLCVs.setStatus("mandatory")
_Dsx1IntervalTable_Object = MibTable
dsx1IntervalTable = _Dsx1IntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8)
)
if mibBuilder.loadTexts:
    dsx1IntervalTable.setStatus("mandatory")
_Dsx1IntervalEntry_Object = MibTableRow
dsx1IntervalEntry = _Dsx1IntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1)
)
dsx1IntervalEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1IntervalIndex"),
    (0, "RFC1406-MIB", "dsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx1IntervalEntry.setStatus("mandatory")


class _Dsx1IntervalIndex_Type(Integer32):
    """Custom type dsx1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1IntervalIndex_Type.__name__ = "Integer32"
_Dsx1IntervalIndex_Object = MibTableColumn
dsx1IntervalIndex = _Dsx1IntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 1),
    _Dsx1IntervalIndex_Type()
)
dsx1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalIndex.setStatus("mandatory")


class _Dsx1IntervalNumber_Type(Integer32):
    """Custom type dsx1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Dsx1IntervalNumber_Type.__name__ = "Integer32"
_Dsx1IntervalNumber_Object = MibTableColumn
dsx1IntervalNumber = _Dsx1IntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 2),
    _Dsx1IntervalNumber_Type()
)
dsx1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalNumber.setStatus("mandatory")
_Dsx1IntervalESs_Type = Gauge32
_Dsx1IntervalESs_Object = MibTableColumn
dsx1IntervalESs = _Dsx1IntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 3),
    _Dsx1IntervalESs_Type()
)
dsx1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalESs.setStatus("mandatory")
_Dsx1IntervalSESs_Type = Gauge32
_Dsx1IntervalSESs_Object = MibTableColumn
dsx1IntervalSESs = _Dsx1IntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 4),
    _Dsx1IntervalSESs_Type()
)
dsx1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalSESs.setStatus("mandatory")
_Dsx1IntervalSEFSs_Type = Gauge32
_Dsx1IntervalSEFSs_Object = MibTableColumn
dsx1IntervalSEFSs = _Dsx1IntervalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 5),
    _Dsx1IntervalSEFSs_Type()
)
dsx1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalSEFSs.setStatus("mandatory")
_Dsx1IntervalUASs_Type = Gauge32
_Dsx1IntervalUASs_Object = MibTableColumn
dsx1IntervalUASs = _Dsx1IntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 6),
    _Dsx1IntervalUASs_Type()
)
dsx1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalUASs.setStatus("mandatory")
_Dsx1IntervalCSSs_Type = Gauge32
_Dsx1IntervalCSSs_Object = MibTableColumn
dsx1IntervalCSSs = _Dsx1IntervalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 7),
    _Dsx1IntervalCSSs_Type()
)
dsx1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalCSSs.setStatus("mandatory")
_Dsx1IntervalPCVs_Type = Gauge32
_Dsx1IntervalPCVs_Object = MibTableColumn
dsx1IntervalPCVs = _Dsx1IntervalPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 8),
    _Dsx1IntervalPCVs_Type()
)
dsx1IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalPCVs.setStatus("mandatory")
_Dsx1IntervalLESs_Type = Gauge32
_Dsx1IntervalLESs_Object = MibTableColumn
dsx1IntervalLESs = _Dsx1IntervalLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 9),
    _Dsx1IntervalLESs_Type()
)
dsx1IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLESs.setStatus("mandatory")
_Dsx1IntervalBESs_Type = Gauge32
_Dsx1IntervalBESs_Object = MibTableColumn
dsx1IntervalBESs = _Dsx1IntervalBESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 10),
    _Dsx1IntervalBESs_Type()
)
dsx1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalBESs.setStatus("mandatory")
_Dsx1IntervalDMs_Type = Gauge32
_Dsx1IntervalDMs_Object = MibTableColumn
dsx1IntervalDMs = _Dsx1IntervalDMs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 11),
    _Dsx1IntervalDMs_Type()
)
dsx1IntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalDMs.setStatus("mandatory")
_Dsx1IntervalLCVs_Type = Gauge32
_Dsx1IntervalLCVs_Object = MibTableColumn
dsx1IntervalLCVs = _Dsx1IntervalLCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 12),
    _Dsx1IntervalLCVs_Type()
)
dsx1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLCVs.setStatus("mandatory")
_Dsx1TotalTable_Object = MibTable
dsx1TotalTable = _Dsx1TotalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9)
)
if mibBuilder.loadTexts:
    dsx1TotalTable.setStatus("mandatory")
_Dsx1TotalEntry_Object = MibTableRow
dsx1TotalEntry = _Dsx1TotalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1)
)
dsx1TotalEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1TotalIndex"),
)
if mibBuilder.loadTexts:
    dsx1TotalEntry.setStatus("mandatory")


class _Dsx1TotalIndex_Type(Integer32):
    """Custom type dsx1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1TotalIndex_Type.__name__ = "Integer32"
_Dsx1TotalIndex_Object = MibTableColumn
dsx1TotalIndex = _Dsx1TotalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 1),
    _Dsx1TotalIndex_Type()
)
dsx1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalIndex.setStatus("mandatory")
_Dsx1TotalESs_Type = Gauge32
_Dsx1TotalESs_Object = MibTableColumn
dsx1TotalESs = _Dsx1TotalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 2),
    _Dsx1TotalESs_Type()
)
dsx1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalESs.setStatus("mandatory")
_Dsx1TotalSESs_Type = Gauge32
_Dsx1TotalSESs_Object = MibTableColumn
dsx1TotalSESs = _Dsx1TotalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 3),
    _Dsx1TotalSESs_Type()
)
dsx1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalSESs.setStatus("mandatory")
_Dsx1TotalSEFSs_Type = Gauge32
_Dsx1TotalSEFSs_Object = MibTableColumn
dsx1TotalSEFSs = _Dsx1TotalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 4),
    _Dsx1TotalSEFSs_Type()
)
dsx1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalSEFSs.setStatus("mandatory")
_Dsx1TotalUASs_Type = Gauge32
_Dsx1TotalUASs_Object = MibTableColumn
dsx1TotalUASs = _Dsx1TotalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 5),
    _Dsx1TotalUASs_Type()
)
dsx1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalUASs.setStatus("mandatory")
_Dsx1TotalCSSs_Type = Gauge32
_Dsx1TotalCSSs_Object = MibTableColumn
dsx1TotalCSSs = _Dsx1TotalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 6),
    _Dsx1TotalCSSs_Type()
)
dsx1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalCSSs.setStatus("mandatory")
_Dsx1TotalPCVs_Type = Gauge32
_Dsx1TotalPCVs_Object = MibTableColumn
dsx1TotalPCVs = _Dsx1TotalPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 7),
    _Dsx1TotalPCVs_Type()
)
dsx1TotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalPCVs.setStatus("mandatory")
_Dsx1TotalLESs_Type = Gauge32
_Dsx1TotalLESs_Object = MibTableColumn
dsx1TotalLESs = _Dsx1TotalLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 8),
    _Dsx1TotalLESs_Type()
)
dsx1TotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLESs.setStatus("mandatory")
_Dsx1TotalBESs_Type = Gauge32
_Dsx1TotalBESs_Object = MibTableColumn
dsx1TotalBESs = _Dsx1TotalBESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 9),
    _Dsx1TotalBESs_Type()
)
dsx1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalBESs.setStatus("mandatory")
_Dsx1TotalDMs_Type = Gauge32
_Dsx1TotalDMs_Object = MibTableColumn
dsx1TotalDMs = _Dsx1TotalDMs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 10),
    _Dsx1TotalDMs_Type()
)
dsx1TotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalDMs.setStatus("mandatory")
_Dsx1TotalLCVs_Type = Gauge32
_Dsx1TotalLCVs_Object = MibTableColumn
dsx1TotalLCVs = _Dsx1TotalLCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 11),
    _Dsx1TotalLCVs_Type()
)
dsx1TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLCVs.setStatus("mandatory")
_Dsx1FarEndCurrentTable_Object = MibTable
dsx1FarEndCurrentTable = _Dsx1FarEndCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10)
)
if mibBuilder.loadTexts:
    dsx1FarEndCurrentTable.setStatus("mandatory")
_Dsx1FarEndCurrentEntry_Object = MibTableRow
dsx1FarEndCurrentEntry = _Dsx1FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1)
)
dsx1FarEndCurrentEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1FarEndCurrentIndex"),
)
if mibBuilder.loadTexts:
    dsx1FarEndCurrentEntry.setStatus("mandatory")


class _Dsx1FarEndCurrentIndex_Type(Integer32):
    """Custom type dsx1FarEndCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1FarEndCurrentIndex_Type.__name__ = "Integer32"
_Dsx1FarEndCurrentIndex_Object = MibTableColumn
dsx1FarEndCurrentIndex = _Dsx1FarEndCurrentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 1),
    _Dsx1FarEndCurrentIndex_Type()
)
dsx1FarEndCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentIndex.setStatus("mandatory")


class _Dsx1FarEndTimeElapsed_Type(Integer32):
    """Custom type dsx1FarEndTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_Dsx1FarEndTimeElapsed_Type.__name__ = "Integer32"
_Dsx1FarEndTimeElapsed_Object = MibTableColumn
dsx1FarEndTimeElapsed = _Dsx1FarEndTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 2),
    _Dsx1FarEndTimeElapsed_Type()
)
dsx1FarEndTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTimeElapsed.setStatus("mandatory")


class _Dsx1FarEndValidIntervals_Type(Integer32):
    """Custom type dsx1FarEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Dsx1FarEndValidIntervals_Type.__name__ = "Integer32"
_Dsx1FarEndValidIntervals_Object = MibTableColumn
dsx1FarEndValidIntervals = _Dsx1FarEndValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 3),
    _Dsx1FarEndValidIntervals_Type()
)
dsx1FarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndValidIntervals.setStatus("mandatory")
_Dsx1FarEndCurrentESs_Type = Gauge32
_Dsx1FarEndCurrentESs_Object = MibTableColumn
dsx1FarEndCurrentESs = _Dsx1FarEndCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 4),
    _Dsx1FarEndCurrentESs_Type()
)
dsx1FarEndCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentESs.setStatus("mandatory")
_Dsx1FarEndCurrentSESs_Type = Gauge32
_Dsx1FarEndCurrentSESs_Object = MibTableColumn
dsx1FarEndCurrentSESs = _Dsx1FarEndCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 5),
    _Dsx1FarEndCurrentSESs_Type()
)
dsx1FarEndCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentSESs.setStatus("mandatory")
_Dsx1FarEndCurrentSEFSs_Type = Gauge32
_Dsx1FarEndCurrentSEFSs_Object = MibTableColumn
dsx1FarEndCurrentSEFSs = _Dsx1FarEndCurrentSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 6),
    _Dsx1FarEndCurrentSEFSs_Type()
)
dsx1FarEndCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentSEFSs.setStatus("mandatory")
_Dsx1FarEndCurrentUASs_Type = Gauge32
_Dsx1FarEndCurrentUASs_Object = MibTableColumn
dsx1FarEndCurrentUASs = _Dsx1FarEndCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 7),
    _Dsx1FarEndCurrentUASs_Type()
)
dsx1FarEndCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentUASs.setStatus("mandatory")
_Dsx1FarEndCurrentCSSs_Type = Gauge32
_Dsx1FarEndCurrentCSSs_Object = MibTableColumn
dsx1FarEndCurrentCSSs = _Dsx1FarEndCurrentCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 8),
    _Dsx1FarEndCurrentCSSs_Type()
)
dsx1FarEndCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentCSSs.setStatus("mandatory")
_Dsx1FarEndCurrentLESs_Type = Gauge32
_Dsx1FarEndCurrentLESs_Object = MibTableColumn
dsx1FarEndCurrentLESs = _Dsx1FarEndCurrentLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 9),
    _Dsx1FarEndCurrentLESs_Type()
)
dsx1FarEndCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentLESs.setStatus("mandatory")
_Dsx1FarEndCurrentPCVs_Type = Gauge32
_Dsx1FarEndCurrentPCVs_Object = MibTableColumn
dsx1FarEndCurrentPCVs = _Dsx1FarEndCurrentPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 10),
    _Dsx1FarEndCurrentPCVs_Type()
)
dsx1FarEndCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentPCVs.setStatus("mandatory")
_Dsx1FarEndCurrentBESs_Type = Gauge32
_Dsx1FarEndCurrentBESs_Object = MibTableColumn
dsx1FarEndCurrentBESs = _Dsx1FarEndCurrentBESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 11),
    _Dsx1FarEndCurrentBESs_Type()
)
dsx1FarEndCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentBESs.setStatus("mandatory")
_Dsx1FarEndCurrentDMs_Type = Gauge32
_Dsx1FarEndCurrentDMs_Object = MibTableColumn
dsx1FarEndCurrentDMs = _Dsx1FarEndCurrentDMs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 12),
    _Dsx1FarEndCurrentDMs_Type()
)
dsx1FarEndCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndCurrentDMs.setStatus("mandatory")
_Dsx1FarEndIntervalTable_Object = MibTable
dsx1FarEndIntervalTable = _Dsx1FarEndIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11)
)
if mibBuilder.loadTexts:
    dsx1FarEndIntervalTable.setStatus("mandatory")
_Dsx1FarEndIntervalEntry_Object = MibTableRow
dsx1FarEndIntervalEntry = _Dsx1FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1)
)
dsx1FarEndIntervalEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1FarEndIntervalIndex"),
    (0, "RFC1406-MIB", "dsx1FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx1FarEndIntervalEntry.setStatus("mandatory")


class _Dsx1FarEndIntervalIndex_Type(Integer32):
    """Custom type dsx1FarEndIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1FarEndIntervalIndex_Type.__name__ = "Integer32"
_Dsx1FarEndIntervalIndex_Object = MibTableColumn
dsx1FarEndIntervalIndex = _Dsx1FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 1),
    _Dsx1FarEndIntervalIndex_Type()
)
dsx1FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalIndex.setStatus("mandatory")


class _Dsx1FarEndIntervalNumber_Type(Integer32):
    """Custom type dsx1FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Dsx1FarEndIntervalNumber_Type.__name__ = "Integer32"
_Dsx1FarEndIntervalNumber_Object = MibTableColumn
dsx1FarEndIntervalNumber = _Dsx1FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 2),
    _Dsx1FarEndIntervalNumber_Type()
)
dsx1FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalNumber.setStatus("mandatory")
_Dsx1FarEndIntervalESs_Type = Gauge32
_Dsx1FarEndIntervalESs_Object = MibTableColumn
dsx1FarEndIntervalESs = _Dsx1FarEndIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 3),
    _Dsx1FarEndIntervalESs_Type()
)
dsx1FarEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalESs.setStatus("mandatory")
_Dsx1FarEndIntervalSESs_Type = Gauge32
_Dsx1FarEndIntervalSESs_Object = MibTableColumn
dsx1FarEndIntervalSESs = _Dsx1FarEndIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 4),
    _Dsx1FarEndIntervalSESs_Type()
)
dsx1FarEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalSESs.setStatus("mandatory")
_Dsx1FarEndIntervalSEFSs_Type = Gauge32
_Dsx1FarEndIntervalSEFSs_Object = MibTableColumn
dsx1FarEndIntervalSEFSs = _Dsx1FarEndIntervalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 5),
    _Dsx1FarEndIntervalSEFSs_Type()
)
dsx1FarEndIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalSEFSs.setStatus("mandatory")
_Dsx1FarEndIntervalUASs_Type = Gauge32
_Dsx1FarEndIntervalUASs_Object = MibTableColumn
dsx1FarEndIntervalUASs = _Dsx1FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 6),
    _Dsx1FarEndIntervalUASs_Type()
)
dsx1FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalUASs.setStatus("mandatory")
_Dsx1FarEndIntervalCSSs_Type = Gauge32
_Dsx1FarEndIntervalCSSs_Object = MibTableColumn
dsx1FarEndIntervalCSSs = _Dsx1FarEndIntervalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 7),
    _Dsx1FarEndIntervalCSSs_Type()
)
dsx1FarEndIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalCSSs.setStatus("mandatory")
_Dsx1FarEndIntervalLESs_Type = Gauge32
_Dsx1FarEndIntervalLESs_Object = MibTableColumn
dsx1FarEndIntervalLESs = _Dsx1FarEndIntervalLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 8),
    _Dsx1FarEndIntervalLESs_Type()
)
dsx1FarEndIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalLESs.setStatus("mandatory")
_Dsx1FarEndIntervalPCVs_Type = Gauge32
_Dsx1FarEndIntervalPCVs_Object = MibTableColumn
dsx1FarEndIntervalPCVs = _Dsx1FarEndIntervalPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 9),
    _Dsx1FarEndIntervalPCVs_Type()
)
dsx1FarEndIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalPCVs.setStatus("mandatory")
_Dsx1FarEndIntervalBESs_Type = Gauge32
_Dsx1FarEndIntervalBESs_Object = MibTableColumn
dsx1FarEndIntervalBESs = _Dsx1FarEndIntervalBESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 10),
    _Dsx1FarEndIntervalBESs_Type()
)
dsx1FarEndIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalBESs.setStatus("mandatory")
_Dsx1FarEndIntervalDMs_Type = Gauge32
_Dsx1FarEndIntervalDMs_Object = MibTableColumn
dsx1FarEndIntervalDMs = _Dsx1FarEndIntervalDMs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 11),
    _Dsx1FarEndIntervalDMs_Type()
)
dsx1FarEndIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndIntervalDMs.setStatus("mandatory")
_Dsx1FarEndTotalTable_Object = MibTable
dsx1FarEndTotalTable = _Dsx1FarEndTotalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12)
)
if mibBuilder.loadTexts:
    dsx1FarEndTotalTable.setStatus("mandatory")
_Dsx1FarEndTotalEntry_Object = MibTableRow
dsx1FarEndTotalEntry = _Dsx1FarEndTotalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1)
)
dsx1FarEndTotalEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1FarEndTotalIndex"),
)
if mibBuilder.loadTexts:
    dsx1FarEndTotalEntry.setStatus("mandatory")


class _Dsx1FarEndTotalIndex_Type(Integer32):
    """Custom type dsx1FarEndTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1FarEndTotalIndex_Type.__name__ = "Integer32"
_Dsx1FarEndTotalIndex_Object = MibTableColumn
dsx1FarEndTotalIndex = _Dsx1FarEndTotalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 1),
    _Dsx1FarEndTotalIndex_Type()
)
dsx1FarEndTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalIndex.setStatus("mandatory")
_Dsx1FarEndTotalESs_Type = Gauge32
_Dsx1FarEndTotalESs_Object = MibTableColumn
dsx1FarEndTotalESs = _Dsx1FarEndTotalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 2),
    _Dsx1FarEndTotalESs_Type()
)
dsx1FarEndTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalESs.setStatus("mandatory")
_Dsx1FarEndTotalSESs_Type = Gauge32
_Dsx1FarEndTotalSESs_Object = MibTableColumn
dsx1FarEndTotalSESs = _Dsx1FarEndTotalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 3),
    _Dsx1FarEndTotalSESs_Type()
)
dsx1FarEndTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalSESs.setStatus("mandatory")
_Dsx1FarEndTotalSEFSs_Type = Gauge32
_Dsx1FarEndTotalSEFSs_Object = MibTableColumn
dsx1FarEndTotalSEFSs = _Dsx1FarEndTotalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 4),
    _Dsx1FarEndTotalSEFSs_Type()
)
dsx1FarEndTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalSEFSs.setStatus("mandatory")
_Dsx1FarEndTotalUASs_Type = Gauge32
_Dsx1FarEndTotalUASs_Object = MibTableColumn
dsx1FarEndTotalUASs = _Dsx1FarEndTotalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 5),
    _Dsx1FarEndTotalUASs_Type()
)
dsx1FarEndTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalUASs.setStatus("mandatory")
_Dsx1FarEndTotalCSSs_Type = Gauge32
_Dsx1FarEndTotalCSSs_Object = MibTableColumn
dsx1FarEndTotalCSSs = _Dsx1FarEndTotalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 6),
    _Dsx1FarEndTotalCSSs_Type()
)
dsx1FarEndTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalCSSs.setStatus("mandatory")
_Dsx1FarEndTotalLESs_Type = Gauge32
_Dsx1FarEndTotalLESs_Object = MibTableColumn
dsx1FarEndTotalLESs = _Dsx1FarEndTotalLESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 7),
    _Dsx1FarEndTotalLESs_Type()
)
dsx1FarEndTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalLESs.setStatus("mandatory")
_Dsx1FarEndTotalPCVs_Type = Gauge32
_Dsx1FarEndTotalPCVs_Object = MibTableColumn
dsx1FarEndTotalPCVs = _Dsx1FarEndTotalPCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 8),
    _Dsx1FarEndTotalPCVs_Type()
)
dsx1FarEndTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalPCVs.setStatus("mandatory")
_Dsx1FarEndTotalBESs_Type = Gauge32
_Dsx1FarEndTotalBESs_Object = MibTableColumn
dsx1FarEndTotalBESs = _Dsx1FarEndTotalBESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 9),
    _Dsx1FarEndTotalBESs_Type()
)
dsx1FarEndTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalBESs.setStatus("mandatory")
_Dsx1FarEndTotalDMs_Type = Gauge32
_Dsx1FarEndTotalDMs_Object = MibTableColumn
dsx1FarEndTotalDMs = _Dsx1FarEndTotalDMs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 10),
    _Dsx1FarEndTotalDMs_Type()
)
dsx1FarEndTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FarEndTotalDMs.setStatus("mandatory")
_Dsx1FracTable_Object = MibTable
dsx1FracTable = _Dsx1FracTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 13)
)
if mibBuilder.loadTexts:
    dsx1FracTable.setStatus("mandatory")
_Dsx1FracEntry_Object = MibTableRow
dsx1FracEntry = _Dsx1FracEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 13, 1)
)
dsx1FracEntry.setIndexNames(
    (0, "RFC1406-MIB", "dsx1FracIndex"),
    (0, "RFC1406-MIB", "dsx1FracNumber"),
)
if mibBuilder.loadTexts:
    dsx1FracEntry.setStatus("mandatory")


class _Dsx1FracIndex_Type(Integer32):
    """Custom type dsx1FracIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1FracIndex_Type.__name__ = "Integer32"
_Dsx1FracIndex_Object = MibTableColumn
dsx1FracIndex = _Dsx1FracIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 1),
    _Dsx1FracIndex_Type()
)
dsx1FracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FracIndex.setStatus("mandatory")


class _Dsx1FracNumber_Type(Integer32):
    """Custom type dsx1FracNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Dsx1FracNumber_Type.__name__ = "Integer32"
_Dsx1FracNumber_Object = MibTableColumn
dsx1FracNumber = _Dsx1FracNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 2),
    _Dsx1FracNumber_Type()
)
dsx1FracNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1FracNumber.setStatus("mandatory")


class _Dsx1FracIfIndex_Type(Integer32):
    """Custom type dsx1FracIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1FracIfIndex_Type.__name__ = "Integer32"
_Dsx1FracIfIndex_Object = MibTableColumn
dsx1FracIfIndex = _Dsx1FracIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 3),
    _Dsx1FracIfIndex_Type()
)
dsx1FracIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1FracIfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1406-MIB",
    **{"ds1": ds1,
       "dsx1ConfigTable": dsx1ConfigTable,
       "dsx1ConfigEntry": dsx1ConfigEntry,
       "dsx1LineIndex": dsx1LineIndex,
       "dsx1IfIndex": dsx1IfIndex,
       "dsx1TimeElapsed": dsx1TimeElapsed,
       "dsx1ValidIntervals": dsx1ValidIntervals,
       "dsx1LineType": dsx1LineType,
       "dsx1LineCoding": dsx1LineCoding,
       "dsx1SendCode": dsx1SendCode,
       "dsx1CircuitIdentifier": dsx1CircuitIdentifier,
       "dsx1LoopbackConfig": dsx1LoopbackConfig,
       "dsx1LineStatus": dsx1LineStatus,
       "dsx1SignalMode": dsx1SignalMode,
       "dsx1TransmitClockSource": dsx1TransmitClockSource,
       "dsx1Fdl": dsx1Fdl,
       "dsx1CurrentTable": dsx1CurrentTable,
       "dsx1CurrentEntry": dsx1CurrentEntry,
       "dsx1CurrentIndex": dsx1CurrentIndex,
       "dsx1CurrentESs": dsx1CurrentESs,
       "dsx1CurrentSESs": dsx1CurrentSESs,
       "dsx1CurrentSEFSs": dsx1CurrentSEFSs,
       "dsx1CurrentUASs": dsx1CurrentUASs,
       "dsx1CurrentCSSs": dsx1CurrentCSSs,
       "dsx1CurrentPCVs": dsx1CurrentPCVs,
       "dsx1CurrentLESs": dsx1CurrentLESs,
       "dsx1CurrentBESs": dsx1CurrentBESs,
       "dsx1CurrentDMs": dsx1CurrentDMs,
       "dsx1CurrentLCVs": dsx1CurrentLCVs,
       "dsx1IntervalTable": dsx1IntervalTable,
       "dsx1IntervalEntry": dsx1IntervalEntry,
       "dsx1IntervalIndex": dsx1IntervalIndex,
       "dsx1IntervalNumber": dsx1IntervalNumber,
       "dsx1IntervalESs": dsx1IntervalESs,
       "dsx1IntervalSESs": dsx1IntervalSESs,
       "dsx1IntervalSEFSs": dsx1IntervalSEFSs,
       "dsx1IntervalUASs": dsx1IntervalUASs,
       "dsx1IntervalCSSs": dsx1IntervalCSSs,
       "dsx1IntervalPCVs": dsx1IntervalPCVs,
       "dsx1IntervalLESs": dsx1IntervalLESs,
       "dsx1IntervalBESs": dsx1IntervalBESs,
       "dsx1IntervalDMs": dsx1IntervalDMs,
       "dsx1IntervalLCVs": dsx1IntervalLCVs,
       "dsx1TotalTable": dsx1TotalTable,
       "dsx1TotalEntry": dsx1TotalEntry,
       "dsx1TotalIndex": dsx1TotalIndex,
       "dsx1TotalESs": dsx1TotalESs,
       "dsx1TotalSESs": dsx1TotalSESs,
       "dsx1TotalSEFSs": dsx1TotalSEFSs,
       "dsx1TotalUASs": dsx1TotalUASs,
       "dsx1TotalCSSs": dsx1TotalCSSs,
       "dsx1TotalPCVs": dsx1TotalPCVs,
       "dsx1TotalLESs": dsx1TotalLESs,
       "dsx1TotalBESs": dsx1TotalBESs,
       "dsx1TotalDMs": dsx1TotalDMs,
       "dsx1TotalLCVs": dsx1TotalLCVs,
       "dsx1FarEndCurrentTable": dsx1FarEndCurrentTable,
       "dsx1FarEndCurrentEntry": dsx1FarEndCurrentEntry,
       "dsx1FarEndCurrentIndex": dsx1FarEndCurrentIndex,
       "dsx1FarEndTimeElapsed": dsx1FarEndTimeElapsed,
       "dsx1FarEndValidIntervals": dsx1FarEndValidIntervals,
       "dsx1FarEndCurrentESs": dsx1FarEndCurrentESs,
       "dsx1FarEndCurrentSESs": dsx1FarEndCurrentSESs,
       "dsx1FarEndCurrentSEFSs": dsx1FarEndCurrentSEFSs,
       "dsx1FarEndCurrentUASs": dsx1FarEndCurrentUASs,
       "dsx1FarEndCurrentCSSs": dsx1FarEndCurrentCSSs,
       "dsx1FarEndCurrentLESs": dsx1FarEndCurrentLESs,
       "dsx1FarEndCurrentPCVs": dsx1FarEndCurrentPCVs,
       "dsx1FarEndCurrentBESs": dsx1FarEndCurrentBESs,
       "dsx1FarEndCurrentDMs": dsx1FarEndCurrentDMs,
       "dsx1FarEndIntervalTable": dsx1FarEndIntervalTable,
       "dsx1FarEndIntervalEntry": dsx1FarEndIntervalEntry,
       "dsx1FarEndIntervalIndex": dsx1FarEndIntervalIndex,
       "dsx1FarEndIntervalNumber": dsx1FarEndIntervalNumber,
       "dsx1FarEndIntervalESs": dsx1FarEndIntervalESs,
       "dsx1FarEndIntervalSESs": dsx1FarEndIntervalSESs,
       "dsx1FarEndIntervalSEFSs": dsx1FarEndIntervalSEFSs,
       "dsx1FarEndIntervalUASs": dsx1FarEndIntervalUASs,
       "dsx1FarEndIntervalCSSs": dsx1FarEndIntervalCSSs,
       "dsx1FarEndIntervalLESs": dsx1FarEndIntervalLESs,
       "dsx1FarEndIntervalPCVs": dsx1FarEndIntervalPCVs,
       "dsx1FarEndIntervalBESs": dsx1FarEndIntervalBESs,
       "dsx1FarEndIntervalDMs": dsx1FarEndIntervalDMs,
       "dsx1FarEndTotalTable": dsx1FarEndTotalTable,
       "dsx1FarEndTotalEntry": dsx1FarEndTotalEntry,
       "dsx1FarEndTotalIndex": dsx1FarEndTotalIndex,
       "dsx1FarEndTotalESs": dsx1FarEndTotalESs,
       "dsx1FarEndTotalSESs": dsx1FarEndTotalSESs,
       "dsx1FarEndTotalSEFSs": dsx1FarEndTotalSEFSs,
       "dsx1FarEndTotalUASs": dsx1FarEndTotalUASs,
       "dsx1FarEndTotalCSSs": dsx1FarEndTotalCSSs,
       "dsx1FarEndTotalLESs": dsx1FarEndTotalLESs,
       "dsx1FarEndTotalPCVs": dsx1FarEndTotalPCVs,
       "dsx1FarEndTotalBESs": dsx1FarEndTotalBESs,
       "dsx1FarEndTotalDMs": dsx1FarEndTotalDMs,
       "dsx1FracTable": dsx1FracTable,
       "dsx1FracEntry": dsx1FracEntry,
       "dsx1FracIndex": dsx1FracIndex,
       "dsx1FracNumber": dsx1FracNumber,
       "dsx1FracIfIndex": dsx1FracIfIndex}
)
