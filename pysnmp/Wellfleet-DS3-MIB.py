# SNMP MIB module (Wellfleet-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:05 2024
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

(wfDs3Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDs3Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDs3Config_Object = MibTable
wfDs3Config = _WfDs3Config_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1)
)
if mibBuilder.loadTexts:
    wfDs3Config.setStatus("mandatory")
_WfDs3ConfigEntry_Object = MibTableRow
wfDs3ConfigEntry = _WfDs3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1)
)
wfDs3ConfigEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3LineIndex"),
)
if mibBuilder.loadTexts:
    wfDs3ConfigEntry.setStatus("mandatory")


class _WfDs3LineIndex_Type(Integer32):
    """Custom type wfDs3LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3LineIndex_Type.__name__ = "Integer32"
_WfDs3LineIndex_Object = MibTableColumn
wfDs3LineIndex = _WfDs3LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 1),
    _WfDs3LineIndex_Type()
)
wfDs3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LineIndex.setStatus("mandatory")
_WfDs3TimeElapsed_Type = Integer32
_WfDs3TimeElapsed_Object = MibTableColumn
wfDs3TimeElapsed = _WfDs3TimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 2),
    _WfDs3TimeElapsed_Type()
)
wfDs3TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TimeElapsed.setStatus("mandatory")
_WfDs3ValidIntervals_Type = Integer32
_WfDs3ValidIntervals_Object = MibTableColumn
wfDs3ValidIntervals = _WfDs3ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 3),
    _WfDs3ValidIntervals_Type()
)
wfDs3ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3ValidIntervals.setStatus("mandatory")


class _WfDs3LineType_Type(Integer32):
    """Custom type wfDs3LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ds3cbitparity", 4),
          ("ds3clearchannel", 5),
          ("other", 1))
    )


_WfDs3LineType_Type.__name__ = "Integer32"
_WfDs3LineType_Object = MibTableColumn
wfDs3LineType = _WfDs3LineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 4),
    _WfDs3LineType_Type()
)
wfDs3LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LineType.setStatus("mandatory")


class _WfDs3ZeroCoding_Type(Integer32):
    """Custom type wfDs3ZeroCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ds3b3zs", 2)
    )


_WfDs3ZeroCoding_Type.__name__ = "Integer32"
_WfDs3ZeroCoding_Object = MibTableColumn
wfDs3ZeroCoding = _WfDs3ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 5),
    _WfDs3ZeroCoding_Type()
)
wfDs3ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3ZeroCoding.setStatus("mandatory")


class _WfDs3SendCode_Type(Integer32):
    """Custom type wfDs3SendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ds3sendnocode", 2)
    )


_WfDs3SendCode_Type.__name__ = "Integer32"
_WfDs3SendCode_Object = MibTableColumn
wfDs3SendCode = _WfDs3SendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 6),
    _WfDs3SendCode_Type()
)
wfDs3SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3SendCode.setStatus("mandatory")
_WfDs3CircuitIdentifier_Type = DisplayString
_WfDs3CircuitIdentifier_Object = MibTableColumn
wfDs3CircuitIdentifier = _WfDs3CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 7),
    _WfDs3CircuitIdentifier_Type()
)
wfDs3CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CircuitIdentifier.setStatus("mandatory")


class _WfDs3LoopbackConfig_Type(Integer32):
    """Custom type wfDs3LoopbackConfig based on Integer32"""
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
        *(("ds3mgrlineloop", 3),
          ("ds3mgrpayloadloop", 2),
          ("ds3netreqlineloop", 5),
          ("ds3netreqpayloadloop", 4),
          ("ds3noloop", 1),
          ("ds3otherloop", 6))
    )


_WfDs3LoopbackConfig_Type.__name__ = "Integer32"
_WfDs3LoopbackConfig_Object = MibTableColumn
wfDs3LoopbackConfig = _WfDs3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 8),
    _WfDs3LoopbackConfig_Type()
)
wfDs3LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LoopbackConfig.setStatus("mandatory")


class _WfDs3LineStatus_Type(Integer32):
    """Custom type wfDs3LineStatus based on Integer32"""
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
        *(("ds3alarmindicationsignal", 4),
          ("ds3farendalarm", 2),
          ("ds3loopbackstate", 32),
          ("ds3lossofframe", 8),
          ("ds3lossofsignal", 16),
          ("ds3noalarm", 1))
    )


_WfDs3LineStatus_Type.__name__ = "Integer32"
_WfDs3LineStatus_Object = MibTableColumn
wfDs3LineStatus = _WfDs3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 1, 1, 9),
    _WfDs3LineStatus_Type()
)
wfDs3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3LineStatus.setStatus("mandatory")
_WfDs3Current_Object = MibTable
wfDs3Current = _WfDs3Current_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2)
)
if mibBuilder.loadTexts:
    wfDs3Current.setStatus("mandatory")
_WfDs3CurrentEntry_Object = MibTableRow
wfDs3CurrentEntry = _WfDs3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1)
)
wfDs3CurrentEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3CurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs3CurrentEntry.setStatus("mandatory")


class _WfDs3CurrentIndex_Type(Integer32):
    """Custom type wfDs3CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3CurrentIndex_Type.__name__ = "Integer32"
_WfDs3CurrentIndex_Object = MibTableColumn
wfDs3CurrentIndex = _WfDs3CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 1),
    _WfDs3CurrentIndex_Type()
)
wfDs3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentIndex.setStatus("mandatory")
_WfDs3CurrentESs_Type = Counter32
_WfDs3CurrentESs_Object = MibTableColumn
wfDs3CurrentESs = _WfDs3CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 2),
    _WfDs3CurrentESs_Type()
)
wfDs3CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentESs.setStatus("mandatory")
_WfDs3CurrentSESs_Type = Counter32
_WfDs3CurrentSESs_Object = MibTableColumn
wfDs3CurrentSESs = _WfDs3CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 3),
    _WfDs3CurrentSESs_Type()
)
wfDs3CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentSESs.setStatus("mandatory")
_WfDs3CurrentSEFs_Type = Counter32
_WfDs3CurrentSEFs_Object = MibTableColumn
wfDs3CurrentSEFs = _WfDs3CurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 4),
    _WfDs3CurrentSEFs_Type()
)
wfDs3CurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentSEFs.setStatus("mandatory")
_WfDs3CurrentUASs_Type = Counter32
_WfDs3CurrentUASs_Object = MibTableColumn
wfDs3CurrentUASs = _WfDs3CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 5),
    _WfDs3CurrentUASs_Type()
)
wfDs3CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentUASs.setStatus("mandatory")
_WfDs3CurrentBPVs_Type = Counter32
_WfDs3CurrentBPVs_Object = MibTableColumn
wfDs3CurrentBPVs = _WfDs3CurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 6),
    _WfDs3CurrentBPVs_Type()
)
wfDs3CurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentBPVs.setStatus("mandatory")
_WfDs3CurrentCVs_Type = Counter32
_WfDs3CurrentCVs_Object = MibTableColumn
wfDs3CurrentCVs = _WfDs3CurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 2, 1, 7),
    _WfDs3CurrentCVs_Type()
)
wfDs3CurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3CurrentCVs.setStatus("mandatory")
_WfDs3Interval_Object = MibTable
wfDs3Interval = _WfDs3Interval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3)
)
if mibBuilder.loadTexts:
    wfDs3Interval.setStatus("mandatory")
_WfDs3IntervalEntry_Object = MibTableRow
wfDs3IntervalEntry = _WfDs3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1)
)
wfDs3IntervalEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3IntervalIndex"),
    (0, "Wellfleet-DS3-MIB", "wfDs3IntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs3IntervalEntry.setStatus("mandatory")


class _WfDs3IntervalIndex_Type(Integer32):
    """Custom type wfDs3IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3IntervalIndex_Type.__name__ = "Integer32"
_WfDs3IntervalIndex_Object = MibTableColumn
wfDs3IntervalIndex = _WfDs3IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 1),
    _WfDs3IntervalIndex_Type()
)
wfDs3IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalIndex.setStatus("mandatory")


class _WfDs3IntervalNumber_Type(Integer32):
    """Custom type wfDs3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDs3IntervalNumber_Type.__name__ = "Integer32"
_WfDs3IntervalNumber_Object = MibTableColumn
wfDs3IntervalNumber = _WfDs3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 2),
    _WfDs3IntervalNumber_Type()
)
wfDs3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalNumber.setStatus("mandatory")
_WfDs3IntervalESs_Type = Gauge32
_WfDs3IntervalESs_Object = MibTableColumn
wfDs3IntervalESs = _WfDs3IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 3),
    _WfDs3IntervalESs_Type()
)
wfDs3IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalESs.setStatus("mandatory")
_WfDs3IntervalSESs_Type = Gauge32
_WfDs3IntervalSESs_Object = MibTableColumn
wfDs3IntervalSESs = _WfDs3IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 4),
    _WfDs3IntervalSESs_Type()
)
wfDs3IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalSESs.setStatus("mandatory")
_WfDs3IntervalSEFs_Type = Gauge32
_WfDs3IntervalSEFs_Object = MibTableColumn
wfDs3IntervalSEFs = _WfDs3IntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 5),
    _WfDs3IntervalSEFs_Type()
)
wfDs3IntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalSEFs.setStatus("mandatory")
_WfDs3IntervalUASs_Type = Gauge32
_WfDs3IntervalUASs_Object = MibTableColumn
wfDs3IntervalUASs = _WfDs3IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 6),
    _WfDs3IntervalUASs_Type()
)
wfDs3IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalUASs.setStatus("mandatory")
_WfDs3IntervalBPVs_Type = Gauge32
_WfDs3IntervalBPVs_Object = MibTableColumn
wfDs3IntervalBPVs = _WfDs3IntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 7),
    _WfDs3IntervalBPVs_Type()
)
wfDs3IntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalBPVs.setStatus("mandatory")
_WfDs3IntervalCVs_Type = Gauge32
_WfDs3IntervalCVs_Object = MibTableColumn
wfDs3IntervalCVs = _WfDs3IntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 3, 1, 8),
    _WfDs3IntervalCVs_Type()
)
wfDs3IntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3IntervalCVs.setStatus("mandatory")
_WfDs3Total_Object = MibTable
wfDs3Total = _WfDs3Total_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4)
)
if mibBuilder.loadTexts:
    wfDs3Total.setStatus("mandatory")
_WfDs3TotalEntry_Object = MibTableRow
wfDs3TotalEntry = _WfDs3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1)
)
wfDs3TotalEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3TotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs3TotalEntry.setStatus("mandatory")


class _WfDs3TotalIndex_Type(Integer32):
    """Custom type wfDs3TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3TotalIndex_Type.__name__ = "Integer32"
_WfDs3TotalIndex_Object = MibTableColumn
wfDs3TotalIndex = _WfDs3TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 1),
    _WfDs3TotalIndex_Type()
)
wfDs3TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalIndex.setStatus("mandatory")
_WfDs3TotalESs_Type = Gauge32
_WfDs3TotalESs_Object = MibTableColumn
wfDs3TotalESs = _WfDs3TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 2),
    _WfDs3TotalESs_Type()
)
wfDs3TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalESs.setStatus("mandatory")
_WfDs3TotalSESs_Type = Gauge32
_WfDs3TotalSESs_Object = MibTableColumn
wfDs3TotalSESs = _WfDs3TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 3),
    _WfDs3TotalSESs_Type()
)
wfDs3TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalSESs.setStatus("mandatory")
_WfDs3TotalSEFs_Type = Gauge32
_WfDs3TotalSEFs_Object = MibTableColumn
wfDs3TotalSEFs = _WfDs3TotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 4),
    _WfDs3TotalSEFs_Type()
)
wfDs3TotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalSEFs.setStatus("mandatory")
_WfDs3TotalUASs_Type = Gauge32
_WfDs3TotalUASs_Object = MibTableColumn
wfDs3TotalUASs = _WfDs3TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 5),
    _WfDs3TotalUASs_Type()
)
wfDs3TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalUASs.setStatus("mandatory")
_WfDs3TotalBPVs_Type = Gauge32
_WfDs3TotalBPVs_Object = MibTableColumn
wfDs3TotalBPVs = _WfDs3TotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 6),
    _WfDs3TotalBPVs_Type()
)
wfDs3TotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalBPVs.setStatus("mandatory")
_WfDs3TotalCVs_Type = Gauge32
_WfDs3TotalCVs_Object = MibTableColumn
wfDs3TotalCVs = _WfDs3TotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 4, 1, 7),
    _WfDs3TotalCVs_Type()
)
wfDs3TotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3TotalCVs.setStatus("mandatory")
_WfDs3FeConfig_Object = MibTable
wfDs3FeConfig = _WfDs3FeConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5)
)
if mibBuilder.loadTexts:
    wfDs3FeConfig.setStatus("mandatory")
_WfDs3FeConfigEntry_Object = MibTableRow
wfDs3FeConfigEntry = _WfDs3FeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1)
)
wfDs3FeConfigEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3FeConfigIndex"),
)
if mibBuilder.loadTexts:
    wfDs3FeConfigEntry.setStatus("mandatory")


class _WfDs3FeConfigIndex_Type(Integer32):
    """Custom type wfDs3FeConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3FeConfigIndex_Type.__name__ = "Integer32"
_WfDs3FeConfigIndex_Object = MibTableColumn
wfDs3FeConfigIndex = _WfDs3FeConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 1),
    _WfDs3FeConfigIndex_Type()
)
wfDs3FeConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeConfigIndex.setStatus("mandatory")
_WfDs3FarEndEquipCode_Type = DisplayString
_WfDs3FarEndEquipCode_Object = MibTableColumn
wfDs3FarEndEquipCode = _WfDs3FarEndEquipCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 2),
    _WfDs3FarEndEquipCode_Type()
)
wfDs3FarEndEquipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndEquipCode.setStatus("mandatory")
_WfDs3FarEndLocationIDCode_Type = DisplayString
_WfDs3FarEndLocationIDCode_Object = MibTableColumn
wfDs3FarEndLocationIDCode = _WfDs3FarEndLocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 3),
    _WfDs3FarEndLocationIDCode_Type()
)
wfDs3FarEndLocationIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndLocationIDCode.setStatus("mandatory")
_WfDs3FarEndFrameIDCode_Type = DisplayString
_WfDs3FarEndFrameIDCode_Object = MibTableColumn
wfDs3FarEndFrameIDCode = _WfDs3FarEndFrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 4),
    _WfDs3FarEndFrameIDCode_Type()
)
wfDs3FarEndFrameIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndFrameIDCode.setStatus("mandatory")
_WfDs3FarEndUnitCode_Type = DisplayString
_WfDs3FarEndUnitCode_Object = MibTableColumn
wfDs3FarEndUnitCode = _WfDs3FarEndUnitCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 5),
    _WfDs3FarEndUnitCode_Type()
)
wfDs3FarEndUnitCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndUnitCode.setStatus("mandatory")
_WfDs3FarEndFacilityIDCode_Type = DisplayString
_WfDs3FarEndFacilityIDCode_Object = MibTableColumn
wfDs3FarEndFacilityIDCode = _WfDs3FarEndFacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 5, 1, 6),
    _WfDs3FarEndFacilityIDCode_Type()
)
wfDs3FarEndFacilityIDCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3FarEndFacilityIDCode.setStatus("mandatory")
_WfDs3FeCurrent_Object = MibTable
wfDs3FeCurrent = _WfDs3FeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6)
)
if mibBuilder.loadTexts:
    wfDs3FeCurrent.setStatus("mandatory")
_WfDs3FeCurrentEntry_Object = MibTableRow
wfDs3FeCurrentEntry = _WfDs3FeCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1)
)
wfDs3FeCurrentEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3FeCurrentIndex"),
)
if mibBuilder.loadTexts:
    wfDs3FeCurrentEntry.setStatus("mandatory")


class _WfDs3FeCurrentIndex_Type(Integer32):
    """Custom type wfDs3FeCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3FeCurrentIndex_Type.__name__ = "Integer32"
_WfDs3FeCurrentIndex_Object = MibTableColumn
wfDs3FeCurrentIndex = _WfDs3FeCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 1),
    _WfDs3FeCurrentIndex_Type()
)
wfDs3FeCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentIndex.setStatus("mandatory")
_WfDs3FeCurrentESs_Type = Counter32
_WfDs3FeCurrentESs_Object = MibTableColumn
wfDs3FeCurrentESs = _WfDs3FeCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 2),
    _WfDs3FeCurrentESs_Type()
)
wfDs3FeCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentESs.setStatus("mandatory")
_WfDs3FeCurrentSESs_Type = Counter32
_WfDs3FeCurrentSESs_Object = MibTableColumn
wfDs3FeCurrentSESs = _WfDs3FeCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 3),
    _WfDs3FeCurrentSESs_Type()
)
wfDs3FeCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentSESs.setStatus("mandatory")
_WfDs3FeCurrentCVs_Type = Counter32
_WfDs3FeCurrentCVs_Object = MibTableColumn
wfDs3FeCurrentCVs = _WfDs3FeCurrentCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 6, 1, 4),
    _WfDs3FeCurrentCVs_Type()
)
wfDs3FeCurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeCurrentCVs.setStatus("mandatory")
_WfDs3FeInterval_Object = MibTable
wfDs3FeInterval = _WfDs3FeInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7)
)
if mibBuilder.loadTexts:
    wfDs3FeInterval.setStatus("mandatory")
_WfDs3FeIntervalEntry_Object = MibTableRow
wfDs3FeIntervalEntry = _WfDs3FeIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1)
)
wfDs3FeIntervalEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3FeIntervalIndex"),
    (0, "Wellfleet-DS3-MIB", "wfDs3FeIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs3FeIntervalEntry.setStatus("mandatory")


class _WfDs3FeIntervalIndex_Type(Integer32):
    """Custom type wfDs3FeIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3FeIntervalIndex_Type.__name__ = "Integer32"
_WfDs3FeIntervalIndex_Object = MibTableColumn
wfDs3FeIntervalIndex = _WfDs3FeIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 1),
    _WfDs3FeIntervalIndex_Type()
)
wfDs3FeIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalIndex.setStatus("mandatory")


class _WfDs3FeIntervalNumber_Type(Integer32):
    """Custom type wfDs3FeIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfDs3FeIntervalNumber_Type.__name__ = "Integer32"
_WfDs3FeIntervalNumber_Object = MibTableColumn
wfDs3FeIntervalNumber = _WfDs3FeIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 2),
    _WfDs3FeIntervalNumber_Type()
)
wfDs3FeIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalNumber.setStatus("mandatory")
_WfDs3FeIntervalESs_Type = Gauge32
_WfDs3FeIntervalESs_Object = MibTableColumn
wfDs3FeIntervalESs = _WfDs3FeIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 3),
    _WfDs3FeIntervalESs_Type()
)
wfDs3FeIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalESs.setStatus("mandatory")
_WfDs3FeIntervalSESs_Type = Gauge32
_WfDs3FeIntervalSESs_Object = MibTableColumn
wfDs3FeIntervalSESs = _WfDs3FeIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 4),
    _WfDs3FeIntervalSESs_Type()
)
wfDs3FeIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalSESs.setStatus("mandatory")
_WfDs3FeIntervalCVs_Type = Gauge32
_WfDs3FeIntervalCVs_Object = MibTableColumn
wfDs3FeIntervalCVs = _WfDs3FeIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 7, 1, 5),
    _WfDs3FeIntervalCVs_Type()
)
wfDs3FeIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeIntervalCVs.setStatus("mandatory")
_WfDs3FeTotal_Object = MibTable
wfDs3FeTotal = _WfDs3FeTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8)
)
if mibBuilder.loadTexts:
    wfDs3FeTotal.setStatus("mandatory")
_WfDs3FeTotalEntry_Object = MibTableRow
wfDs3FeTotalEntry = _WfDs3FeTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1)
)
wfDs3FeTotalEntry.setIndexNames(
    (0, "Wellfleet-DS3-MIB", "wfDs3FeTotalIndex"),
)
if mibBuilder.loadTexts:
    wfDs3FeTotalEntry.setStatus("mandatory")


class _WfDs3FeTotalIndex_Type(Integer32):
    """Custom type wfDs3FeTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfDs3FeTotalIndex_Type.__name__ = "Integer32"
_WfDs3FeTotalIndex_Object = MibTableColumn
wfDs3FeTotalIndex = _WfDs3FeTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 1),
    _WfDs3FeTotalIndex_Type()
)
wfDs3FeTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalIndex.setStatus("mandatory")
_WfDs3FeTotalESs_Type = Gauge32
_WfDs3FeTotalESs_Object = MibTableColumn
wfDs3FeTotalESs = _WfDs3FeTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 2),
    _WfDs3FeTotalESs_Type()
)
wfDs3FeTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalESs.setStatus("mandatory")
_WfDs3FeTotalSESs_Type = Gauge32
_WfDs3FeTotalSESs_Object = MibTableColumn
wfDs3FeTotalSESs = _WfDs3FeTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 3),
    _WfDs3FeTotalSESs_Type()
)
wfDs3FeTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalSESs.setStatus("mandatory")
_WfDs3FeTotalCVs_Type = Gauge32
_WfDs3FeTotalCVs_Object = MibTableColumn
wfDs3FeTotalCVs = _WfDs3FeTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13, 8, 1, 4),
    _WfDs3FeTotalCVs_Type()
)
wfDs3FeTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3FeTotalCVs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DS3-MIB",
    **{"wfDs3Config": wfDs3Config,
       "wfDs3ConfigEntry": wfDs3ConfigEntry,
       "wfDs3LineIndex": wfDs3LineIndex,
       "wfDs3TimeElapsed": wfDs3TimeElapsed,
       "wfDs3ValidIntervals": wfDs3ValidIntervals,
       "wfDs3LineType": wfDs3LineType,
       "wfDs3ZeroCoding": wfDs3ZeroCoding,
       "wfDs3SendCode": wfDs3SendCode,
       "wfDs3CircuitIdentifier": wfDs3CircuitIdentifier,
       "wfDs3LoopbackConfig": wfDs3LoopbackConfig,
       "wfDs3LineStatus": wfDs3LineStatus,
       "wfDs3Current": wfDs3Current,
       "wfDs3CurrentEntry": wfDs3CurrentEntry,
       "wfDs3CurrentIndex": wfDs3CurrentIndex,
       "wfDs3CurrentESs": wfDs3CurrentESs,
       "wfDs3CurrentSESs": wfDs3CurrentSESs,
       "wfDs3CurrentSEFs": wfDs3CurrentSEFs,
       "wfDs3CurrentUASs": wfDs3CurrentUASs,
       "wfDs3CurrentBPVs": wfDs3CurrentBPVs,
       "wfDs3CurrentCVs": wfDs3CurrentCVs,
       "wfDs3Interval": wfDs3Interval,
       "wfDs3IntervalEntry": wfDs3IntervalEntry,
       "wfDs3IntervalIndex": wfDs3IntervalIndex,
       "wfDs3IntervalNumber": wfDs3IntervalNumber,
       "wfDs3IntervalESs": wfDs3IntervalESs,
       "wfDs3IntervalSESs": wfDs3IntervalSESs,
       "wfDs3IntervalSEFs": wfDs3IntervalSEFs,
       "wfDs3IntervalUASs": wfDs3IntervalUASs,
       "wfDs3IntervalBPVs": wfDs3IntervalBPVs,
       "wfDs3IntervalCVs": wfDs3IntervalCVs,
       "wfDs3Total": wfDs3Total,
       "wfDs3TotalEntry": wfDs3TotalEntry,
       "wfDs3TotalIndex": wfDs3TotalIndex,
       "wfDs3TotalESs": wfDs3TotalESs,
       "wfDs3TotalSESs": wfDs3TotalSESs,
       "wfDs3TotalSEFs": wfDs3TotalSEFs,
       "wfDs3TotalUASs": wfDs3TotalUASs,
       "wfDs3TotalBPVs": wfDs3TotalBPVs,
       "wfDs3TotalCVs": wfDs3TotalCVs,
       "wfDs3FeConfig": wfDs3FeConfig,
       "wfDs3FeConfigEntry": wfDs3FeConfigEntry,
       "wfDs3FeConfigIndex": wfDs3FeConfigIndex,
       "wfDs3FarEndEquipCode": wfDs3FarEndEquipCode,
       "wfDs3FarEndLocationIDCode": wfDs3FarEndLocationIDCode,
       "wfDs3FarEndFrameIDCode": wfDs3FarEndFrameIDCode,
       "wfDs3FarEndUnitCode": wfDs3FarEndUnitCode,
       "wfDs3FarEndFacilityIDCode": wfDs3FarEndFacilityIDCode,
       "wfDs3FeCurrent": wfDs3FeCurrent,
       "wfDs3FeCurrentEntry": wfDs3FeCurrentEntry,
       "wfDs3FeCurrentIndex": wfDs3FeCurrentIndex,
       "wfDs3FeCurrentESs": wfDs3FeCurrentESs,
       "wfDs3FeCurrentSESs": wfDs3FeCurrentSESs,
       "wfDs3FeCurrentCVs": wfDs3FeCurrentCVs,
       "wfDs3FeInterval": wfDs3FeInterval,
       "wfDs3FeIntervalEntry": wfDs3FeIntervalEntry,
       "wfDs3FeIntervalIndex": wfDs3FeIntervalIndex,
       "wfDs3FeIntervalNumber": wfDs3FeIntervalNumber,
       "wfDs3FeIntervalESs": wfDs3FeIntervalESs,
       "wfDs3FeIntervalSESs": wfDs3FeIntervalSESs,
       "wfDs3FeIntervalCVs": wfDs3FeIntervalCVs,
       "wfDs3FeTotal": wfDs3FeTotal,
       "wfDs3FeTotalEntry": wfDs3FeTotalEntry,
       "wfDs3FeTotalIndex": wfDs3FeTotalIndex,
       "wfDs3FeTotalESs": wfDs3FeTotalESs,
       "wfDs3FeTotalSESs": wfDs3FeTotalSESs,
       "wfDs3FeTotalCVs": wfDs3FeTotalCVs}
)
