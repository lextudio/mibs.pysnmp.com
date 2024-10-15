# SNMP MIB module (RFC1232-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1232-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:12 2024
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
_Ds1ConfigTable_Object = MibTable
ds1ConfigTable = _Ds1ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1)
)
if mibBuilder.loadTexts:
    ds1ConfigTable.setStatus("mandatory")
_Ds1ConfigEntry_Object = MibTableRow
ds1ConfigEntry = _Ds1ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1)
)
ds1ConfigEntry.setIndexNames(
    (0, "RFC1232-MIB", "ds1CSUIndex"),
)
if mibBuilder.loadTexts:
    ds1ConfigEntry.setStatus("mandatory")
_Ds1CSUIndex_Type = Integer32
_Ds1CSUIndex_Object = MibTableColumn
ds1CSUIndex = _Ds1CSUIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 1),
    _Ds1CSUIndex_Type()
)
ds1CSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CSUIndex.setStatus("mandatory")
_Ds1Index_Type = Integer32
_Ds1Index_Object = MibTableColumn
ds1Index = _Ds1Index_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 2),
    _Ds1Index_Type()
)
ds1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1Index.setStatus("mandatory")


class _Ds1TimeElapsed_Type(Integer32):
    """Custom type ds1TimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_Ds1TimeElapsed_Type.__name__ = "Integer32"
_Ds1TimeElapsed_Object = MibTableColumn
ds1TimeElapsed = _Ds1TimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 3),
    _Ds1TimeElapsed_Type()
)
ds1TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TimeElapsed.setStatus("mandatory")


class _Ds1ValidIntervals_Type(Integer32):
    """Custom type ds1ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Ds1ValidIntervals_Type.__name__ = "Integer32"
_Ds1ValidIntervals_Object = MibTableColumn
ds1ValidIntervals = _Ds1ValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 4),
    _Ds1ValidIntervals_Type()
)
ds1ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ValidIntervals.setStatus("mandatory")


class _Ds1LineType_Type(Integer32):
    """Custom type ds1LineType based on Integer32"""
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
        *(("ds1ANSI-ESF", 4),
          ("ds1D4", 3),
          ("ds1ESF", 2),
          ("ds1G704", 5),
          ("ds1G704-CRC", 6),
          ("other", 1))
    )


_Ds1LineType_Type.__name__ = "Integer32"
_Ds1LineType_Object = MibTableColumn
ds1LineType = _Ds1LineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 5),
    _Ds1LineType_Type()
)
ds1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineType.setStatus("mandatory")


class _Ds1ZeroCoding_Type(Integer32):
    """Custom type ds1ZeroCoding based on Integer32"""
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
        *(("ds1B8ZS", 2),
          ("ds1HDB3", 4),
          ("ds1InvertedHDLC", 3),
          ("ds1JammedBit", 1),
          ("ds1ZBTSI", 5))
    )


_Ds1ZeroCoding_Type.__name__ = "Integer32"
_Ds1ZeroCoding_Object = MibTableColumn
ds1ZeroCoding = _Ds1ZeroCoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 6),
    _Ds1ZeroCoding_Type()
)
ds1ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ZeroCoding.setStatus("mandatory")


class _Ds1Loopback_Type(Integer32):
    """Custom type ds1Loopback based on Integer32"""
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
        *(("ds1LocalLoopbackLocalSide", 2),
          ("ds1LocalLoopbackRemoteSide", 3),
          ("ds1NoLoop", 1),
          ("ds1RemoteLoopbackLocalSide", 4),
          ("ds1RemoteLoopbackRemoteSide", 5))
    )


_Ds1Loopback_Type.__name__ = "Integer32"
_Ds1Loopback_Object = MibTableColumn
ds1Loopback = _Ds1Loopback_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 7),
    _Ds1Loopback_Type()
)
ds1Loopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1Loopback.setStatus("mandatory")


class _Ds1SendCode_Type(Integer32):
    """Custom type ds1SendCode based on Integer32"""
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
        *(("ds1OtherTest", 1),
          ("ds1SendNoCode", 2),
          ("ds1SendQRSS", 5),
          ("ds1SendResetCode", 4),
          ("ds1SendSetCode", 3))
    )


_Ds1SendCode_Type.__name__ = "Integer32"
_Ds1SendCode_Object = MibTableColumn
ds1SendCode = _Ds1SendCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 8),
    _Ds1SendCode_Type()
)
ds1SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1SendCode.setStatus("mandatory")


class _Ds1YellowAlarm_Type(Integer32):
    """Custom type ds1YellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1NoYellowAlarm", 1),
          ("ds1YellowAlarm", 2))
    )


_Ds1YellowAlarm_Type.__name__ = "Integer32"
_Ds1YellowAlarm_Object = MibTableColumn
ds1YellowAlarm = _Ds1YellowAlarm_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 9),
    _Ds1YellowAlarm_Type()
)
ds1YellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1YellowAlarm.setStatus("mandatory")


class _Ds1RedAlarm_Type(Integer32):
    """Custom type ds1RedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1NoRedAlarm", 1),
          ("ds1RedAlarm", 2))
    )


_Ds1RedAlarm_Type.__name__ = "Integer32"
_Ds1RedAlarm_Object = MibTableColumn
ds1RedAlarm = _Ds1RedAlarm_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 10),
    _Ds1RedAlarm_Type()
)
ds1RedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1RedAlarm.setStatus("mandatory")


class _Ds1CircuitIdentifier_Type(DisplayString):
    """Custom type ds1CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ds1CircuitIdentifier_Type.__name__ = "DisplayString"
_Ds1CircuitIdentifier_Object = MibTableColumn
ds1CircuitIdentifier = _Ds1CircuitIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 1, 1, 11),
    _Ds1CircuitIdentifier_Type()
)
ds1CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CircuitIdentifier.setStatus("mandatory")
_Ds1IntervalTable_Object = MibTable
ds1IntervalTable = _Ds1IntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2)
)
if mibBuilder.loadTexts:
    ds1IntervalTable.setStatus("mandatory")
_Ds1IntervalEntry_Object = MibTableRow
ds1IntervalEntry = _Ds1IntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1)
)
ds1IntervalEntry.setIndexNames(
    (0, "RFC1232-MIB", "ds1IntervalIndex"),
    (0, "RFC1232-MIB", "ds1IntervalNumber"),
)
if mibBuilder.loadTexts:
    ds1IntervalEntry.setStatus("mandatory")
_Ds1IntervalIndex_Type = Integer32
_Ds1IntervalIndex_Object = MibTableColumn
ds1IntervalIndex = _Ds1IntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 1),
    _Ds1IntervalIndex_Type()
)
ds1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalIndex.setStatus("mandatory")


class _Ds1IntervalNumber_Type(Integer32):
    """Custom type ds1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Ds1IntervalNumber_Type.__name__ = "Integer32"
_Ds1IntervalNumber_Object = MibTableColumn
ds1IntervalNumber = _Ds1IntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 2),
    _Ds1IntervalNumber_Type()
)
ds1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalNumber.setStatus("mandatory")
_Ds1IntervalESs_Type = Counter32
_Ds1IntervalESs_Object = MibTableColumn
ds1IntervalESs = _Ds1IntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 3),
    _Ds1IntervalESs_Type()
)
ds1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalESs.setStatus("mandatory")
_Ds1IntervalSESs_Type = Counter32
_Ds1IntervalSESs_Object = MibTableColumn
ds1IntervalSESs = _Ds1IntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 4),
    _Ds1IntervalSESs_Type()
)
ds1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalSESs.setStatus("mandatory")
_Ds1IntervalSEFSs_Type = Counter32
_Ds1IntervalSEFSs_Object = MibTableColumn
ds1IntervalSEFSs = _Ds1IntervalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 5),
    _Ds1IntervalSEFSs_Type()
)
ds1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalSEFSs.setStatus("mandatory")
_Ds1IntervalUASs_Type = Counter32
_Ds1IntervalUASs_Object = MibTableColumn
ds1IntervalUASs = _Ds1IntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 6),
    _Ds1IntervalUASs_Type()
)
ds1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalUASs.setStatus("mandatory")
_Ds1IntervalCSSs_Type = Counter32
_Ds1IntervalCSSs_Object = MibTableColumn
ds1IntervalCSSs = _Ds1IntervalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 7),
    _Ds1IntervalCSSs_Type()
)
ds1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalCSSs.setStatus("mandatory")
_Ds1IntervalBPVs_Type = Counter32
_Ds1IntervalBPVs_Object = MibTableColumn
ds1IntervalBPVs = _Ds1IntervalBPVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 8),
    _Ds1IntervalBPVs_Type()
)
ds1IntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalBPVs.setStatus("mandatory")
_Ds1IntervalCVs_Type = Counter32
_Ds1IntervalCVs_Object = MibTableColumn
ds1IntervalCVs = _Ds1IntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 2, 1, 9),
    _Ds1IntervalCVs_Type()
)
ds1IntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1IntervalCVs.setStatus("mandatory")
_Ds1CurrentTable_Object = MibTable
ds1CurrentTable = _Ds1CurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3)
)
if mibBuilder.loadTexts:
    ds1CurrentTable.setStatus("mandatory")
_Ds1CurrentEntry_Object = MibTableRow
ds1CurrentEntry = _Ds1CurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1)
)
ds1CurrentEntry.setIndexNames(
    (0, "RFC1232-MIB", "ds1CurrentIndex"),
)
if mibBuilder.loadTexts:
    ds1CurrentEntry.setStatus("mandatory")
_Ds1CurrentIndex_Type = Integer32
_Ds1CurrentIndex_Object = MibTableColumn
ds1CurrentIndex = _Ds1CurrentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 1),
    _Ds1CurrentIndex_Type()
)
ds1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentIndex.setStatus("mandatory")
_Ds1CurrentESs_Type = Counter32
_Ds1CurrentESs_Object = MibTableColumn
ds1CurrentESs = _Ds1CurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 2),
    _Ds1CurrentESs_Type()
)
ds1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentESs.setStatus("mandatory")
_Ds1CurrentSESs_Type = Counter32
_Ds1CurrentSESs_Object = MibTableColumn
ds1CurrentSESs = _Ds1CurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 3),
    _Ds1CurrentSESs_Type()
)
ds1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentSESs.setStatus("mandatory")
_Ds1CurrentSEFSs_Type = Counter32
_Ds1CurrentSEFSs_Object = MibTableColumn
ds1CurrentSEFSs = _Ds1CurrentSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 4),
    _Ds1CurrentSEFSs_Type()
)
ds1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentSEFSs.setStatus("mandatory")
_Ds1CurrentUASs_Type = Counter32
_Ds1CurrentUASs_Object = MibTableColumn
ds1CurrentUASs = _Ds1CurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 5),
    _Ds1CurrentUASs_Type()
)
ds1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentUASs.setStatus("mandatory")
_Ds1CurrentCSSs_Type = Counter32
_Ds1CurrentCSSs_Object = MibTableColumn
ds1CurrentCSSs = _Ds1CurrentCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 6),
    _Ds1CurrentCSSs_Type()
)
ds1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentCSSs.setStatus("mandatory")
_Ds1CurrentBPVs_Type = Counter32
_Ds1CurrentBPVs_Object = MibTableColumn
ds1CurrentBPVs = _Ds1CurrentBPVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 7),
    _Ds1CurrentBPVs_Type()
)
ds1CurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentBPVs.setStatus("mandatory")
_Ds1CurrentCVs_Type = Counter32
_Ds1CurrentCVs_Object = MibTableColumn
ds1CurrentCVs = _Ds1CurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 3, 1, 8),
    _Ds1CurrentCVs_Type()
)
ds1CurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentCVs.setStatus("mandatory")
_Ds1TotalTable_Object = MibTable
ds1TotalTable = _Ds1TotalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4)
)
if mibBuilder.loadTexts:
    ds1TotalTable.setStatus("mandatory")
_Ds1TotalEntry_Object = MibTableRow
ds1TotalEntry = _Ds1TotalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1)
)
ds1TotalEntry.setIndexNames(
    (0, "RFC1232-MIB", "ds1TotalIndex"),
)
if mibBuilder.loadTexts:
    ds1TotalEntry.setStatus("mandatory")
_Ds1TotalIndex_Type = Integer32
_Ds1TotalIndex_Object = MibTableColumn
ds1TotalIndex = _Ds1TotalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 1),
    _Ds1TotalIndex_Type()
)
ds1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalIndex.setStatus("mandatory")
_Ds1TotalESs_Type = Counter32
_Ds1TotalESs_Object = MibTableColumn
ds1TotalESs = _Ds1TotalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 2),
    _Ds1TotalESs_Type()
)
ds1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalESs.setStatus("mandatory")
_Ds1TotalSESs_Type = Counter32
_Ds1TotalSESs_Object = MibTableColumn
ds1TotalSESs = _Ds1TotalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 3),
    _Ds1TotalSESs_Type()
)
ds1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalSESs.setStatus("mandatory")
_Ds1TotalSEFSs_Type = Counter32
_Ds1TotalSEFSs_Object = MibTableColumn
ds1TotalSEFSs = _Ds1TotalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 4),
    _Ds1TotalSEFSs_Type()
)
ds1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalSEFSs.setStatus("mandatory")
_Ds1TotalUASs_Type = Counter32
_Ds1TotalUASs_Object = MibTableColumn
ds1TotalUASs = _Ds1TotalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 5),
    _Ds1TotalUASs_Type()
)
ds1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalUASs.setStatus("mandatory")
_Ds1TotalCSSs_Type = Counter32
_Ds1TotalCSSs_Object = MibTableColumn
ds1TotalCSSs = _Ds1TotalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 6),
    _Ds1TotalCSSs_Type()
)
ds1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalCSSs.setStatus("mandatory")
_Ds1TotalBPVs_Type = Counter32
_Ds1TotalBPVs_Object = MibTableColumn
ds1TotalBPVs = _Ds1TotalBPVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 7),
    _Ds1TotalBPVs_Type()
)
ds1TotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalBPVs.setStatus("mandatory")
_Ds1TotalCVs_Type = Counter32
_Ds1TotalCVs_Object = MibTableColumn
ds1TotalCVs = _Ds1TotalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 4, 1, 8),
    _Ds1TotalCVs_Type()
)
ds1TotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1TotalCVs.setStatus("mandatory")
_Ds1FracTable_Object = MibTable
ds1FracTable = _Ds1FracTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 5)
)
if mibBuilder.loadTexts:
    ds1FracTable.setStatus("mandatory")
_Ds1FracEntry_Object = MibTableRow
ds1FracEntry = _Ds1FracEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 5, 1)
)
ds1FracEntry.setIndexNames(
    (0, "RFC1232-MIB", "ds1FracIndex"),
    (0, "RFC1232-MIB", "ds1FracNumber"),
)
if mibBuilder.loadTexts:
    ds1FracEntry.setStatus("mandatory")
_Ds1FracIndex_Type = Integer32
_Ds1FracIndex_Object = MibTableColumn
ds1FracIndex = _Ds1FracIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 5, 1, 1),
    _Ds1FracIndex_Type()
)
ds1FracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FracIndex.setStatus("mandatory")


class _Ds1FracNumber_Type(Integer32):
    """Custom type ds1FracNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Ds1FracNumber_Type.__name__ = "Integer32"
_Ds1FracNumber_Object = MibTableColumn
ds1FracNumber = _Ds1FracNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 5, 1, 2),
    _Ds1FracNumber_Type()
)
ds1FracNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FracNumber.setStatus("mandatory")
_Ds1FracIfIndex_Type = Integer32
_Ds1FracIfIndex_Object = MibTableColumn
ds1FracIfIndex = _Ds1FracIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 18, 5, 1, 3),
    _Ds1FracIfIndex_Type()
)
ds1FracIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FracIfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1232-MIB",
    **{"ds1": ds1,
       "ds1ConfigTable": ds1ConfigTable,
       "ds1ConfigEntry": ds1ConfigEntry,
       "ds1CSUIndex": ds1CSUIndex,
       "ds1Index": ds1Index,
       "ds1TimeElapsed": ds1TimeElapsed,
       "ds1ValidIntervals": ds1ValidIntervals,
       "ds1LineType": ds1LineType,
       "ds1ZeroCoding": ds1ZeroCoding,
       "ds1Loopback": ds1Loopback,
       "ds1SendCode": ds1SendCode,
       "ds1YellowAlarm": ds1YellowAlarm,
       "ds1RedAlarm": ds1RedAlarm,
       "ds1CircuitIdentifier": ds1CircuitIdentifier,
       "ds1IntervalTable": ds1IntervalTable,
       "ds1IntervalEntry": ds1IntervalEntry,
       "ds1IntervalIndex": ds1IntervalIndex,
       "ds1IntervalNumber": ds1IntervalNumber,
       "ds1IntervalESs": ds1IntervalESs,
       "ds1IntervalSESs": ds1IntervalSESs,
       "ds1IntervalSEFSs": ds1IntervalSEFSs,
       "ds1IntervalUASs": ds1IntervalUASs,
       "ds1IntervalCSSs": ds1IntervalCSSs,
       "ds1IntervalBPVs": ds1IntervalBPVs,
       "ds1IntervalCVs": ds1IntervalCVs,
       "ds1CurrentTable": ds1CurrentTable,
       "ds1CurrentEntry": ds1CurrentEntry,
       "ds1CurrentIndex": ds1CurrentIndex,
       "ds1CurrentESs": ds1CurrentESs,
       "ds1CurrentSESs": ds1CurrentSESs,
       "ds1CurrentSEFSs": ds1CurrentSEFSs,
       "ds1CurrentUASs": ds1CurrentUASs,
       "ds1CurrentCSSs": ds1CurrentCSSs,
       "ds1CurrentBPVs": ds1CurrentBPVs,
       "ds1CurrentCVs": ds1CurrentCVs,
       "ds1TotalTable": ds1TotalTable,
       "ds1TotalEntry": ds1TotalEntry,
       "ds1TotalIndex": ds1TotalIndex,
       "ds1TotalESs": ds1TotalESs,
       "ds1TotalSESs": ds1TotalSESs,
       "ds1TotalSEFSs": ds1TotalSEFSs,
       "ds1TotalUASs": ds1TotalUASs,
       "ds1TotalCSSs": ds1TotalCSSs,
       "ds1TotalBPVs": ds1TotalBPVs,
       "ds1TotalCVs": ds1TotalCVs,
       "ds1FracTable": ds1FracTable,
       "ds1FracEntry": ds1FracEntry,
       "ds1FracIndex": ds1FracIndex,
       "ds1FracNumber": ds1FracNumber,
       "ds1FracIfIndex": ds1FracIfIndex}
)
