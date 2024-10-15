# SNMP MIB module (Wellfleet-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:04 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfDs1Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDs1Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDs1Config_Object = MibTable
wfDs1Config = _WfDs1Config_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1)
)
if mibBuilder.loadTexts:
    wfDs1Config.setStatus("mandatory")
_WfDs1ConfigEntry_Object = MibTableRow
wfDs1ConfigEntry = _WfDs1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1)
)
wfDs1ConfigEntry.setIndexNames(
    (0, "Wellfleet-DS1-MIB", "wfDs1LineIndex"),
)
if mibBuilder.loadTexts:
    wfDs1ConfigEntry.setStatus("mandatory")


class _WfDs1LineIndex_Type(Integer32):
    """Custom type wfDs1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs1LineIndex_Type.__name__ = "Integer32"
_WfDs1LineIndex_Object = MibTableColumn
wfDs1LineIndex = _WfDs1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 1),
    _WfDs1LineIndex_Type()
)
wfDs1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LineIndex.setStatus("mandatory")
_WfDs1TimeElapsed_Type = Integer32
_WfDs1TimeElapsed_Object = MibTableColumn
wfDs1TimeElapsed = _WfDs1TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 2),
    _WfDs1TimeElapsed_Type()
)
wfDs1TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TimeElapsed.setStatus("mandatory")
_WfDs1ValidIntervals_Type = Integer32
_WfDs1ValidIntervals_Object = MibTableColumn
wfDs1ValidIntervals = _WfDs1ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 3),
    _WfDs1ValidIntervals_Type()
)
wfDs1ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1ValidIntervals.setStatus("mandatory")


class _WfDs1LineType_Type(Integer32):
    """Custom type wfDs1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("ds1ansi-esf", 4)
    )


_WfDs1LineType_Type.__name__ = "Integer32"
_WfDs1LineType_Object = MibTableColumn
wfDs1LineType = _WfDs1LineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 4),
    _WfDs1LineType_Type()
)
wfDs1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LineType.setStatus("mandatory")


class _WfDs1ZeroCoding_Type(Integer32):
    """Custom type wfDs1ZeroCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ds1b8zs", 2),
          ("ds1zbtsi", 5))
    )


_WfDs1ZeroCoding_Type.__name__ = "Integer32"
_WfDs1ZeroCoding_Object = MibTableColumn
wfDs1ZeroCoding = _WfDs1ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 5),
    _WfDs1ZeroCoding_Type()
)
wfDs1ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1ZeroCoding.setStatus("mandatory")


class _WfDs1SendCode_Type(Integer32):
    """Custom type wfDs1SendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ds1sendnocode", 2)
    )


_WfDs1SendCode_Type.__name__ = "Integer32"
_WfDs1SendCode_Object = MibTableColumn
wfDs1SendCode = _WfDs1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 6),
    _WfDs1SendCode_Type()
)
wfDs1SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1SendCode.setStatus("mandatory")
_WfDs1CircuitIdentifier_Type = DisplayString
_WfDs1CircuitIdentifier_Object = MibTableColumn
wfDs1CircuitIdentifier = _WfDs1CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 7),
    _WfDs1CircuitIdentifier_Type()
)
wfDs1CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CircuitIdentifier.setStatus("mandatory")


class _WfDs1LoopbackConfig_Type(Integer32):
    """Custom type wfDs1LoopbackConfig based on Integer32"""
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
        *(("ds1mgrlineloop", 3),
          ("ds1mgrpayloadloop", 2),
          ("ds1netreqlineloop", 5),
          ("ds1netreqpayloadloop", 4),
          ("ds1noloop", 1),
          ("ds1otherloop", 6))
    )


_WfDs1LoopbackConfig_Type.__name__ = "Integer32"
_WfDs1LoopbackConfig_Object = MibTableColumn
wfDs1LoopbackConfig = _WfDs1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 8),
    _WfDs1LoopbackConfig_Type()
)
wfDs1LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LoopbackConfig.setStatus("mandatory")


class _WfDs1LineStatus_Type(Integer32):
    """Custom type wfDs1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ds1alarmindicationsignal", 4),
          ("ds1farendalarm", 2),
          ("ds1loopbackstate", 32),
          ("ds1lossofframe", 8),
          ("ds1lossofsignal", 16),
          ("ds1noalarm", 1))
    )


_WfDs1LineStatus_Type.__name__ = "Integer32"
_WfDs1LineStatus_Object = MibTableColumn
wfDs1LineStatus = _WfDs1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 1, 1, 9),
    _WfDs1LineStatus_Type()
)
wfDs1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1LineStatus.setStatus("mandatory")
_WfDs1Current_Object = MibTable
wfDs1Current = _WfDs1Current_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2)
)
if mibBuilder.loadTexts:
    wfDs1Current.setStatus("mandatory")
_WfDs1CurrentEntry_Object = MibTableRow
wfDs1CurrentEntry = _WfDs1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1)
)
wfDs1CurrentEntry.setIndexNames(
    (0, "Wellfleet-DS1-MIB", "wfDs1CurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs1CurrentEntry.setStatus("mandatory")


class _WfDs1CurrentIndex_Type(Integer32):
    """Custom type wfDs1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs1CurrentIndex_Type.__name__ = "Integer32"
_WfDs1CurrentIndex_Object = MibTableColumn
wfDs1CurrentIndex = _WfDs1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 1),
    _WfDs1CurrentIndex_Type()
)
wfDs1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentIndex.setStatus("mandatory")
_WfDs1CurrentESs_Type = Counter32
_WfDs1CurrentESs_Object = MibTableColumn
wfDs1CurrentESs = _WfDs1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 2),
    _WfDs1CurrentESs_Type()
)
wfDs1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentESs.setStatus("mandatory")
_WfDs1CurrentSESs_Type = Counter32
_WfDs1CurrentSESs_Object = MibTableColumn
wfDs1CurrentSESs = _WfDs1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 3),
    _WfDs1CurrentSESs_Type()
)
wfDs1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentSESs.setStatus("mandatory")
_WfDs1CurrentSEFs_Type = Counter32
_WfDs1CurrentSEFs_Object = MibTableColumn
wfDs1CurrentSEFs = _WfDs1CurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 4),
    _WfDs1CurrentSEFs_Type()
)
wfDs1CurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentSEFs.setStatus("mandatory")
_WfDs1CurrentUASs_Type = Counter32
_WfDs1CurrentUASs_Object = MibTableColumn
wfDs1CurrentUASs = _WfDs1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 5),
    _WfDs1CurrentUASs_Type()
)
wfDs1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentUASs.setStatus("mandatory")
_WfDs1CurrentBPVs_Type = Counter32
_WfDs1CurrentBPVs_Object = MibTableColumn
wfDs1CurrentBPVs = _WfDs1CurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 6),
    _WfDs1CurrentBPVs_Type()
)
wfDs1CurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentBPVs.setStatus("mandatory")
_WfDs1CurrentCVs_Type = Counter32
_WfDs1CurrentCVs_Object = MibTableColumn
wfDs1CurrentCVs = _WfDs1CurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 2, 1, 7),
    _WfDs1CurrentCVs_Type()
)
wfDs1CurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1CurrentCVs.setStatus("mandatory")
_WfDs1Interval_Object = MibTable
wfDs1Interval = _WfDs1Interval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3)
)
if mibBuilder.loadTexts:
    wfDs1Interval.setStatus("mandatory")
_WfDs1IntervalEntry_Object = MibTableRow
wfDs1IntervalEntry = _WfDs1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1)
)
wfDs1IntervalEntry.setIndexNames(
    (0, "Wellfleet-DS1-MIB", "wfDs1IntervalIndex"),
    (0, "Wellfleet-DS1-MIB", "wfDs1IntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1IntervalEntry.setStatus("mandatory")


class _WfDs1IntervalIndex_Type(Integer32):
    """Custom type wfDs1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs1IntervalIndex_Type.__name__ = "Integer32"
_WfDs1IntervalIndex_Object = MibTableColumn
wfDs1IntervalIndex = _WfDs1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 1),
    _WfDs1IntervalIndex_Type()
)
wfDs1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalIndex.setStatus("mandatory")


class _WfDs1IntervalNumber_Type(Integer32):
    """Custom type wfDs1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDs1IntervalNumber_Type.__name__ = "Integer32"
_WfDs1IntervalNumber_Object = MibTableColumn
wfDs1IntervalNumber = _WfDs1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 2),
    _WfDs1IntervalNumber_Type()
)
wfDs1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalNumber.setStatus("mandatory")
_WfDs1IntervalESs_Type = Gauge32
_WfDs1IntervalESs_Object = MibTableColumn
wfDs1IntervalESs = _WfDs1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 3),
    _WfDs1IntervalESs_Type()
)
wfDs1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalESs.setStatus("mandatory")
_WfDs1IntervalSESs_Type = Gauge32
_WfDs1IntervalSESs_Object = MibTableColumn
wfDs1IntervalSESs = _WfDs1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 4),
    _WfDs1IntervalSESs_Type()
)
wfDs1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalSESs.setStatus("mandatory")
_WfDs1IntervalSEFs_Type = Gauge32
_WfDs1IntervalSEFs_Object = MibTableColumn
wfDs1IntervalSEFs = _WfDs1IntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 5),
    _WfDs1IntervalSEFs_Type()
)
wfDs1IntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalSEFs.setStatus("mandatory")
_WfDs1IntervalUASs_Type = Gauge32
_WfDs1IntervalUASs_Object = MibTableColumn
wfDs1IntervalUASs = _WfDs1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 6),
    _WfDs1IntervalUASs_Type()
)
wfDs1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalUASs.setStatus("mandatory")
_WfDs1IntervalBPVs_Type = Gauge32
_WfDs1IntervalBPVs_Object = MibTableColumn
wfDs1IntervalBPVs = _WfDs1IntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 7),
    _WfDs1IntervalBPVs_Type()
)
wfDs1IntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalBPVs.setStatus("mandatory")
_WfDs1IntervalCVs_Type = Gauge32
_WfDs1IntervalCVs_Object = MibTableColumn
wfDs1IntervalCVs = _WfDs1IntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 3, 1, 8),
    _WfDs1IntervalCVs_Type()
)
wfDs1IntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1IntervalCVs.setStatus("mandatory")
_WfDs1Total_Object = MibTable
wfDs1Total = _WfDs1Total_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4)
)
if mibBuilder.loadTexts:
    wfDs1Total.setStatus("mandatory")
_WfDs1TotalEntry_Object = MibTableRow
wfDs1TotalEntry = _WfDs1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1)
)
wfDs1TotalEntry.setIndexNames(
    (0, "Wellfleet-DS1-MIB", "wfDs1TotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs1TotalEntry.setStatus("mandatory")


class _WfDs1TotalIndex_Type(Integer32):
    """Custom type wfDs1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs1TotalIndex_Type.__name__ = "Integer32"
_WfDs1TotalIndex_Object = MibTableColumn
wfDs1TotalIndex = _WfDs1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 1),
    _WfDs1TotalIndex_Type()
)
wfDs1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalIndex.setStatus("mandatory")
_WfDs1TotalESs_Type = Gauge32
_WfDs1TotalESs_Object = MibTableColumn
wfDs1TotalESs = _WfDs1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 2),
    _WfDs1TotalESs_Type()
)
wfDs1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalESs.setStatus("mandatory")
_WfDs1TotalSESs_Type = Gauge32
_WfDs1TotalSESs_Object = MibTableColumn
wfDs1TotalSESs = _WfDs1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 3),
    _WfDs1TotalSESs_Type()
)
wfDs1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalSESs.setStatus("mandatory")
_WfDs1TotalSEFs_Type = Gauge32
_WfDs1TotalSEFs_Object = MibTableColumn
wfDs1TotalSEFs = _WfDs1TotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 4),
    _WfDs1TotalSEFs_Type()
)
wfDs1TotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalSEFs.setStatus("mandatory")
_WfDs1TotalUASs_Type = Gauge32
_WfDs1TotalUASs_Object = MibTableColumn
wfDs1TotalUASs = _WfDs1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 5),
    _WfDs1TotalUASs_Type()
)
wfDs1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalUASs.setStatus("mandatory")
_WfDs1TotalBPVs_Type = Gauge32
_WfDs1TotalBPVs_Object = MibTableColumn
wfDs1TotalBPVs = _WfDs1TotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 6),
    _WfDs1TotalBPVs_Type()
)
wfDs1TotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalBPVs.setStatus("mandatory")
_WfDs1TotalCVs_Type = Gauge32
_WfDs1TotalCVs_Object = MibTableColumn
wfDs1TotalCVs = _WfDs1TotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 4, 1, 7),
    _WfDs1TotalCVs_Type()
)
wfDs1TotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1TotalCVs.setStatus("mandatory")
_WfDs1FeCurrent_Object = MibTable
wfDs1FeCurrent = _WfDs1FeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5)
)
if mibBuilder.loadTexts:
    wfDs1FeCurrent.setStatus("mandatory")
_WfDs1FeCurrentEntry_Object = MibTableRow
wfDs1FeCurrentEntry = _WfDs1FeCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1)
)
wfDs1FeCurrentEntry.setIndexNames(
    (0, "Wellfleet-DS1-MIB", "wfDs1FeCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs1FeCurrentEntry.setStatus("mandatory")


class _WfDs1FeCurrentIndex_Type(Integer32):
    """Custom type wfDs1FeCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs1FeCurrentIndex_Type.__name__ = "Integer32"
_WfDs1FeCurrentIndex_Object = MibTableColumn
wfDs1FeCurrentIndex = _WfDs1FeCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 1),
    _WfDs1FeCurrentIndex_Type()
)
wfDs1FeCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentIndex.setStatus("mandatory")
_WfDs1FeCurrentESs_Type = Counter32
_WfDs1FeCurrentESs_Object = MibTableColumn
wfDs1FeCurrentESs = _WfDs1FeCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 2),
    _WfDs1FeCurrentESs_Type()
)
wfDs1FeCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentESs.setStatus("mandatory")
_WfDs1FeCurrentSESs_Type = Counter32
_WfDs1FeCurrentSESs_Object = MibTableColumn
wfDs1FeCurrentSESs = _WfDs1FeCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 3),
    _WfDs1FeCurrentSESs_Type()
)
wfDs1FeCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentSESs.setStatus("mandatory")
_WfDs1FeCurrentSEFs_Type = Counter32
_WfDs1FeCurrentSEFs_Object = MibTableColumn
wfDs1FeCurrentSEFs = _WfDs1FeCurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 4),
    _WfDs1FeCurrentSEFs_Type()
)
wfDs1FeCurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentSEFs.setStatus("mandatory")
_WfDs1FeCurrentBPVs_Type = Counter32
_WfDs1FeCurrentBPVs_Object = MibTableColumn
wfDs1FeCurrentBPVs = _WfDs1FeCurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 5),
    _WfDs1FeCurrentBPVs_Type()
)
wfDs1FeCurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentBPVs.setStatus("mandatory")
_WfDs1FeCurrentCVs_Type = Counter32
_WfDs1FeCurrentCVs_Object = MibTableColumn
wfDs1FeCurrentCVs = _WfDs1FeCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 5, 1, 6),
    _WfDs1FeCurrentCVs_Type()
)
wfDs1FeCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeCurrentCVs.setStatus("mandatory")
_WfDs1FeInterval_Object = MibTable
wfDs1FeInterval = _WfDs1FeInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6)
)
if mibBuilder.loadTexts:
    wfDs1FeInterval.setStatus("mandatory")
_WfDs1FeIntervalEntry_Object = MibTableRow
wfDs1FeIntervalEntry = _WfDs1FeIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1)
)
wfDs1FeIntervalEntry.setIndexNames(
    (0, "Wellfleet-DS1-MIB", "wfDs1FeIntervalIndex"),
    (0, "Wellfleet-DS1-MIB", "wfDs1FeIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1FeIntervalEntry.setStatus("mandatory")


class _WfDs1FeIntervalIndex_Type(Integer32):
    """Custom type wfDs1FeIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs1FeIntervalIndex_Type.__name__ = "Integer32"
_WfDs1FeIntervalIndex_Object = MibTableColumn
wfDs1FeIntervalIndex = _WfDs1FeIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 1),
    _WfDs1FeIntervalIndex_Type()
)
wfDs1FeIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalIndex.setStatus("mandatory")


class _WfDs1FeIntervalNumber_Type(Integer32):
    """Custom type wfDs1FeIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDs1FeIntervalNumber_Type.__name__ = "Integer32"
_WfDs1FeIntervalNumber_Object = MibTableColumn
wfDs1FeIntervalNumber = _WfDs1FeIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 2),
    _WfDs1FeIntervalNumber_Type()
)
wfDs1FeIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalNumber.setStatus("mandatory")
_WfDs1FeIntervalESs_Type = Gauge32
_WfDs1FeIntervalESs_Object = MibTableColumn
wfDs1FeIntervalESs = _WfDs1FeIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 3),
    _WfDs1FeIntervalESs_Type()
)
wfDs1FeIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalESs.setStatus("mandatory")
_WfDs1FeIntervalSESs_Type = Gauge32
_WfDs1FeIntervalSESs_Object = MibTableColumn
wfDs1FeIntervalSESs = _WfDs1FeIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 4),
    _WfDs1FeIntervalSESs_Type()
)
wfDs1FeIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalSESs.setStatus("mandatory")
_WfDs1FeIntervalSEFs_Type = Gauge32
_WfDs1FeIntervalSEFs_Object = MibTableColumn
wfDs1FeIntervalSEFs = _WfDs1FeIntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 5),
    _WfDs1FeIntervalSEFs_Type()
)
wfDs1FeIntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalSEFs.setStatus("mandatory")
_WfDs1FeIntervalBPVs_Type = Gauge32
_WfDs1FeIntervalBPVs_Object = MibTableColumn
wfDs1FeIntervalBPVs = _WfDs1FeIntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 6),
    _WfDs1FeIntervalBPVs_Type()
)
wfDs1FeIntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalBPVs.setStatus("mandatory")
_WfDs1FeIntervalCVs_Type = Gauge32
_WfDs1FeIntervalCVs_Object = MibTableColumn
wfDs1FeIntervalCVs = _WfDs1FeIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 6, 1, 7),
    _WfDs1FeIntervalCVs_Type()
)
wfDs1FeIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeIntervalCVs.setStatus("mandatory")
_WfDs1FeTotal_Object = MibTable
wfDs1FeTotal = _WfDs1FeTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7)
)
if mibBuilder.loadTexts:
    wfDs1FeTotal.setStatus("mandatory")
_WfDs1FeTotalEntry_Object = MibTableRow
wfDs1FeTotalEntry = _WfDs1FeTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1)
)
wfDs1FeTotalEntry.setIndexNames(
    (0, "Wellfleet-DS1-MIB", "wfDs1FeTotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs1FeTotalEntry.setStatus("mandatory")


class _WfDs1FeTotalIndex_Type(Integer32):
    """Custom type wfDs1FeTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs1FeTotalIndex_Type.__name__ = "Integer32"
_WfDs1FeTotalIndex_Object = MibTableColumn
wfDs1FeTotalIndex = _WfDs1FeTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 1),
    _WfDs1FeTotalIndex_Type()
)
wfDs1FeTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalIndex.setStatus("mandatory")
_WfDs1FeTotalESs_Type = Gauge32
_WfDs1FeTotalESs_Object = MibTableColumn
wfDs1FeTotalESs = _WfDs1FeTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 2),
    _WfDs1FeTotalESs_Type()
)
wfDs1FeTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalESs.setStatus("mandatory")
_WfDs1FeTotalSESs_Type = Gauge32
_WfDs1FeTotalSESs_Object = MibTableColumn
wfDs1FeTotalSESs = _WfDs1FeTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 3),
    _WfDs1FeTotalSESs_Type()
)
wfDs1FeTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalSESs.setStatus("mandatory")
_WfDs1FeTotalSEFs_Type = Gauge32
_WfDs1FeTotalSEFs_Object = MibTableColumn
wfDs1FeTotalSEFs = _WfDs1FeTotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 4),
    _WfDs1FeTotalSEFs_Type()
)
wfDs1FeTotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalSEFs.setStatus("mandatory")
_WfDs1FeTotalBPVs_Type = Gauge32
_WfDs1FeTotalBPVs_Object = MibTableColumn
wfDs1FeTotalBPVs = _WfDs1FeTotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 5),
    _WfDs1FeTotalBPVs_Type()
)
wfDs1FeTotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalBPVs.setStatus("mandatory")
_WfDs1FeTotalCVs_Type = Gauge32
_WfDs1FeTotalCVs_Object = MibTableColumn
wfDs1FeTotalCVs = _WfDs1FeTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12, 7, 1, 6),
    _WfDs1FeTotalCVs_Type()
)
wfDs1FeTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1FeTotalCVs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DS1-MIB",
    **{"wfDs1Config": wfDs1Config,
       "wfDs1ConfigEntry": wfDs1ConfigEntry,
       "wfDs1LineIndex": wfDs1LineIndex,
       "wfDs1TimeElapsed": wfDs1TimeElapsed,
       "wfDs1ValidIntervals": wfDs1ValidIntervals,
       "wfDs1LineType": wfDs1LineType,
       "wfDs1ZeroCoding": wfDs1ZeroCoding,
       "wfDs1SendCode": wfDs1SendCode,
       "wfDs1CircuitIdentifier": wfDs1CircuitIdentifier,
       "wfDs1LoopbackConfig": wfDs1LoopbackConfig,
       "wfDs1LineStatus": wfDs1LineStatus,
       "wfDs1Current": wfDs1Current,
       "wfDs1CurrentEntry": wfDs1CurrentEntry,
       "wfDs1CurrentIndex": wfDs1CurrentIndex,
       "wfDs1CurrentESs": wfDs1CurrentESs,
       "wfDs1CurrentSESs": wfDs1CurrentSESs,
       "wfDs1CurrentSEFs": wfDs1CurrentSEFs,
       "wfDs1CurrentUASs": wfDs1CurrentUASs,
       "wfDs1CurrentBPVs": wfDs1CurrentBPVs,
       "wfDs1CurrentCVs": wfDs1CurrentCVs,
       "wfDs1Interval": wfDs1Interval,
       "wfDs1IntervalEntry": wfDs1IntervalEntry,
       "wfDs1IntervalIndex": wfDs1IntervalIndex,
       "wfDs1IntervalNumber": wfDs1IntervalNumber,
       "wfDs1IntervalESs": wfDs1IntervalESs,
       "wfDs1IntervalSESs": wfDs1IntervalSESs,
       "wfDs1IntervalSEFs": wfDs1IntervalSEFs,
       "wfDs1IntervalUASs": wfDs1IntervalUASs,
       "wfDs1IntervalBPVs": wfDs1IntervalBPVs,
       "wfDs1IntervalCVs": wfDs1IntervalCVs,
       "wfDs1Total": wfDs1Total,
       "wfDs1TotalEntry": wfDs1TotalEntry,
       "wfDs1TotalIndex": wfDs1TotalIndex,
       "wfDs1TotalESs": wfDs1TotalESs,
       "wfDs1TotalSESs": wfDs1TotalSESs,
       "wfDs1TotalSEFs": wfDs1TotalSEFs,
       "wfDs1TotalUASs": wfDs1TotalUASs,
       "wfDs1TotalBPVs": wfDs1TotalBPVs,
       "wfDs1TotalCVs": wfDs1TotalCVs,
       "wfDs1FeCurrent": wfDs1FeCurrent,
       "wfDs1FeCurrentEntry": wfDs1FeCurrentEntry,
       "wfDs1FeCurrentIndex": wfDs1FeCurrentIndex,
       "wfDs1FeCurrentESs": wfDs1FeCurrentESs,
       "wfDs1FeCurrentSESs": wfDs1FeCurrentSESs,
       "wfDs1FeCurrentSEFs": wfDs1FeCurrentSEFs,
       "wfDs1FeCurrentBPVs": wfDs1FeCurrentBPVs,
       "wfDs1FeCurrentCVs": wfDs1FeCurrentCVs,
       "wfDs1FeInterval": wfDs1FeInterval,
       "wfDs1FeIntervalEntry": wfDs1FeIntervalEntry,
       "wfDs1FeIntervalIndex": wfDs1FeIntervalIndex,
       "wfDs1FeIntervalNumber": wfDs1FeIntervalNumber,
       "wfDs1FeIntervalESs": wfDs1FeIntervalESs,
       "wfDs1FeIntervalSESs": wfDs1FeIntervalSESs,
       "wfDs1FeIntervalSEFs": wfDs1FeIntervalSEFs,
       "wfDs1FeIntervalBPVs": wfDs1FeIntervalBPVs,
       "wfDs1FeIntervalCVs": wfDs1FeIntervalCVs,
       "wfDs1FeTotal": wfDs1FeTotal,
       "wfDs1FeTotalEntry": wfDs1FeTotalEntry,
       "wfDs1FeTotalIndex": wfDs1FeTotalIndex,
       "wfDs1FeTotalESs": wfDs1FeTotalESs,
       "wfDs1FeTotalSESs": wfDs1FeTotalSESs,
       "wfDs1FeTotalSEFs": wfDs1FeTotalSEFs,
       "wfDs1FeTotalBPVs": wfDs1FeTotalBPVs,
       "wfDs1FeTotalCVs": wfDs1FeTotalCVs}
)
