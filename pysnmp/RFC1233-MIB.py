# SNMP MIB module (RFC1233-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1233-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:13 2024
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

_Ds3_ObjectIdentity = ObjectIdentity
ds3 = _Ds3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 30)
)
_Ds3ConfigTable_Object = MibTable
ds3ConfigTable = _Ds3ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1)
)
if mibBuilder.loadTexts:
    ds3ConfigTable.setStatus("mandatory")
_Ds3ConfigEntry_Object = MibTableRow
ds3ConfigEntry = _Ds3ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1)
)
ds3ConfigEntry.setIndexNames(
    (0, "RFC1233-MIB", "ds3CSUIndex"),
)
if mibBuilder.loadTexts:
    ds3ConfigEntry.setStatus("mandatory")
_Ds3CSUIndex_Type = Integer32
_Ds3CSUIndex_Object = MibTableColumn
ds3CSUIndex = _Ds3CSUIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 1),
    _Ds3CSUIndex_Type()
)
ds3CSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CSUIndex.setStatus("mandatory")
_Ds3Index_Type = Integer32
_Ds3Index_Object = MibTableColumn
ds3Index = _Ds3Index_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 2),
    _Ds3Index_Type()
)
ds3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3Index.setStatus("mandatory")


class _Ds3TimeElapsed_Type(Integer32):
    """Custom type ds3TimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_Ds3TimeElapsed_Type.__name__ = "Integer32"
_Ds3TimeElapsed_Object = MibTableColumn
ds3TimeElapsed = _Ds3TimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 3),
    _Ds3TimeElapsed_Type()
)
ds3TimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TimeElapsed.setStatus("mandatory")


class _Ds3ValidIntervals_Type(Integer32):
    """Custom type ds3ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Ds3ValidIntervals_Type.__name__ = "Integer32"
_Ds3ValidIntervals_Object = MibTableColumn
ds3ValidIntervals = _Ds3ValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 4),
    _Ds3ValidIntervals_Type()
)
ds3ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ValidIntervals.setStatus("mandatory")


class _Ds3LineType_Type(Integer32):
    """Custom type ds3LineType based on Integer32"""
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
        *(("ds3CbitParity", 4),
          ("ds3ClearChannel", 5),
          ("ds3M23", 2),
          ("ds3SYNTRAN", 3),
          ("other", 1))
    )


_Ds3LineType_Type.__name__ = "Integer32"
_Ds3LineType_Object = MibTableColumn
ds3LineType = _Ds3LineType_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 5),
    _Ds3LineType_Type()
)
ds3LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LineType.setStatus("mandatory")


class _Ds3ZeroCoding_Type(Integer32):
    """Custom type ds3ZeroCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3B3ZS", 2),
          ("ds3other", 1))
    )


_Ds3ZeroCoding_Type.__name__ = "Integer32"
_Ds3ZeroCoding_Object = MibTableColumn
ds3ZeroCoding = _Ds3ZeroCoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 6),
    _Ds3ZeroCoding_Type()
)
ds3ZeroCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ZeroCoding.setStatus("mandatory")


class _Ds3Loopback_Type(Integer32):
    """Custom type ds3Loopback based on Integer32"""
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
        *(("ds3LocalLoopbackLocalSide", 2),
          ("ds3LocalLoopbackRemoteSide", 3),
          ("ds3NoLoop", 1),
          ("ds3RemoteLoopbackLocalSide", 4),
          ("ds3RemoteLoopbackRemoteSide", 5))
    )


_Ds3Loopback_Type.__name__ = "Integer32"
_Ds3Loopback_Object = MibTableColumn
ds3Loopback = _Ds3Loopback_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 7),
    _Ds3Loopback_Type()
)
ds3Loopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3Loopback.setStatus("mandatory")


class _Ds3SendCode_Type(Integer32):
    """Custom type ds3SendCode based on Integer32"""
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
        *(("ds3SendLoopbackCode", 4),
          ("ds3SendNoCode", 2),
          ("ds3SendResetCode", 5),
          ("ds3SendSetCode", 3),
          ("ds3SendTestMessage", 1))
    )


_Ds3SendCode_Type.__name__ = "Integer32"
_Ds3SendCode_Object = MibTableColumn
ds3SendCode = _Ds3SendCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 8),
    _Ds3SendCode_Type()
)
ds3SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3SendCode.setStatus("mandatory")


class _Ds3YellowAlarm_Type(Integer32):
    """Custom type ds3YellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3NoYellowAlarm", 2),
          ("ds3YellowAlarm", 1))
    )


_Ds3YellowAlarm_Type.__name__ = "Integer32"
_Ds3YellowAlarm_Object = MibTableColumn
ds3YellowAlarm = _Ds3YellowAlarm_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 9),
    _Ds3YellowAlarm_Type()
)
ds3YellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3YellowAlarm.setStatus("mandatory")


class _Ds3RedAlarm_Type(Integer32):
    """Custom type ds3RedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3NoRedAlarm", 2),
          ("ds3RedAlarm", 1))
    )


_Ds3RedAlarm_Type.__name__ = "Integer32"
_Ds3RedAlarm_Object = MibTableColumn
ds3RedAlarm = _Ds3RedAlarm_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 10),
    _Ds3RedAlarm_Type()
)
ds3RedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3RedAlarm.setStatus("mandatory")


class _Ds3CircuitIdentifier_Type(DisplayString):
    """Custom type ds3CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ds3CircuitIdentifier_Type.__name__ = "DisplayString"
_Ds3CircuitIdentifier_Object = MibTableColumn
ds3CircuitIdentifier = _Ds3CircuitIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 11),
    _Ds3CircuitIdentifier_Type()
)
ds3CircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CircuitIdentifier.setStatus("mandatory")
_Ds3IntervalTable_Object = MibTable
ds3IntervalTable = _Ds3IntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2)
)
if mibBuilder.loadTexts:
    ds3IntervalTable.setStatus("mandatory")
_Ds3IntervalEntry_Object = MibTableRow
ds3IntervalEntry = _Ds3IntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1)
)
ds3IntervalEntry.setIndexNames(
    (0, "RFC1233-MIB", "ds3IntervalIndex"),
    (0, "RFC1233-MIB", "ds3IntervalNumber"),
)
if mibBuilder.loadTexts:
    ds3IntervalEntry.setStatus("mandatory")
_Ds3IntervalIndex_Type = Integer32
_Ds3IntervalIndex_Object = MibTableColumn
ds3IntervalIndex = _Ds3IntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 1),
    _Ds3IntervalIndex_Type()
)
ds3IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalIndex.setStatus("mandatory")


class _Ds3IntervalNumber_Type(Integer32):
    """Custom type ds3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Ds3IntervalNumber_Type.__name__ = "Integer32"
_Ds3IntervalNumber_Object = MibTableColumn
ds3IntervalNumber = _Ds3IntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 2),
    _Ds3IntervalNumber_Type()
)
ds3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalNumber.setStatus("mandatory")
_Ds3IntervalESs_Type = Counter32
_Ds3IntervalESs_Object = MibTableColumn
ds3IntervalESs = _Ds3IntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 3),
    _Ds3IntervalESs_Type()
)
ds3IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalESs.setStatus("mandatory")
_Ds3IntervalSESs_Type = Counter32
_Ds3IntervalSESs_Object = MibTableColumn
ds3IntervalSESs = _Ds3IntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 4),
    _Ds3IntervalSESs_Type()
)
ds3IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalSESs.setStatus("mandatory")
_Ds3IntervalSEFSs_Type = Counter32
_Ds3IntervalSEFSs_Object = MibTableColumn
ds3IntervalSEFSs = _Ds3IntervalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 5),
    _Ds3IntervalSEFSs_Type()
)
ds3IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalSEFSs.setStatus("mandatory")
_Ds3IntervalUASs_Type = Counter32
_Ds3IntervalUASs_Object = MibTableColumn
ds3IntervalUASs = _Ds3IntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 6),
    _Ds3IntervalUASs_Type()
)
ds3IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalUASs.setStatus("mandatory")
_Ds3IntervalCSSs_Type = Counter32
_Ds3IntervalCSSs_Object = MibTableColumn
ds3IntervalCSSs = _Ds3IntervalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 7),
    _Ds3IntervalCSSs_Type()
)
ds3IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalCSSs.setStatus("mandatory")
_Ds3IntervalBPVs_Type = Counter32
_Ds3IntervalBPVs_Object = MibTableColumn
ds3IntervalBPVs = _Ds3IntervalBPVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 8),
    _Ds3IntervalBPVs_Type()
)
ds3IntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalBPVs.setStatus("mandatory")
_Ds3IntervalCVs_Type = Counter32
_Ds3IntervalCVs_Object = MibTableColumn
ds3IntervalCVs = _Ds3IntervalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 9),
    _Ds3IntervalCVs_Type()
)
ds3IntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3IntervalCVs.setStatus("mandatory")
_Ds3CurrentTable_Object = MibTable
ds3CurrentTable = _Ds3CurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3)
)
if mibBuilder.loadTexts:
    ds3CurrentTable.setStatus("mandatory")
_Ds3CurrentEntry_Object = MibTableRow
ds3CurrentEntry = _Ds3CurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1)
)
ds3CurrentEntry.setIndexNames(
    (0, "RFC1233-MIB", "ds3CurrentIndex"),
)
if mibBuilder.loadTexts:
    ds3CurrentEntry.setStatus("mandatory")
_Ds3CurrentIndex_Type = Integer32
_Ds3CurrentIndex_Object = MibTableColumn
ds3CurrentIndex = _Ds3CurrentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 1),
    _Ds3CurrentIndex_Type()
)
ds3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentIndex.setStatus("mandatory")
_Ds3CurrentESs_Type = Counter32
_Ds3CurrentESs_Object = MibTableColumn
ds3CurrentESs = _Ds3CurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 2),
    _Ds3CurrentESs_Type()
)
ds3CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentESs.setStatus("mandatory")
_Ds3CurrentSESs_Type = Counter32
_Ds3CurrentSESs_Object = MibTableColumn
ds3CurrentSESs = _Ds3CurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 3),
    _Ds3CurrentSESs_Type()
)
ds3CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentSESs.setStatus("mandatory")
_Ds3CurrentSEFSs_Type = Counter32
_Ds3CurrentSEFSs_Object = MibTableColumn
ds3CurrentSEFSs = _Ds3CurrentSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 4),
    _Ds3CurrentSEFSs_Type()
)
ds3CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentSEFSs.setStatus("mandatory")
_Ds3CurrentUASs_Type = Counter32
_Ds3CurrentUASs_Object = MibTableColumn
ds3CurrentUASs = _Ds3CurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 5),
    _Ds3CurrentUASs_Type()
)
ds3CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentUASs.setStatus("mandatory")
_Ds3CurrentCSSs_Type = Counter32
_Ds3CurrentCSSs_Object = MibTableColumn
ds3CurrentCSSs = _Ds3CurrentCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 6),
    _Ds3CurrentCSSs_Type()
)
ds3CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentCSSs.setStatus("mandatory")
_Ds3CurrentBPVs_Type = Counter32
_Ds3CurrentBPVs_Object = MibTableColumn
ds3CurrentBPVs = _Ds3CurrentBPVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 7),
    _Ds3CurrentBPVs_Type()
)
ds3CurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentBPVs.setStatus("mandatory")
_Ds3CurrentCVs_Type = Counter32
_Ds3CurrentCVs_Object = MibTableColumn
ds3CurrentCVs = _Ds3CurrentCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 8),
    _Ds3CurrentCVs_Type()
)
ds3CurrentCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3CurrentCVs.setStatus("mandatory")
_Ds3TotalTable_Object = MibTable
ds3TotalTable = _Ds3TotalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4)
)
if mibBuilder.loadTexts:
    ds3TotalTable.setStatus("mandatory")
_Ds3TotalEntry_Object = MibTableRow
ds3TotalEntry = _Ds3TotalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1)
)
ds3TotalEntry.setIndexNames(
    (0, "RFC1233-MIB", "ds3TotalIndex"),
)
if mibBuilder.loadTexts:
    ds3TotalEntry.setStatus("mandatory")
_Ds3TotalIndex_Type = Integer32
_Ds3TotalIndex_Object = MibTableColumn
ds3TotalIndex = _Ds3TotalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 1),
    _Ds3TotalIndex_Type()
)
ds3TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalIndex.setStatus("mandatory")
_Ds3TotalESs_Type = Counter32
_Ds3TotalESs_Object = MibTableColumn
ds3TotalESs = _Ds3TotalESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 2),
    _Ds3TotalESs_Type()
)
ds3TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalESs.setStatus("mandatory")
_Ds3TotalSESs_Type = Counter32
_Ds3TotalSESs_Object = MibTableColumn
ds3TotalSESs = _Ds3TotalSESs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 3),
    _Ds3TotalSESs_Type()
)
ds3TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalSESs.setStatus("mandatory")
_Ds3TotalSEFSs_Type = Counter32
_Ds3TotalSEFSs_Object = MibTableColumn
ds3TotalSEFSs = _Ds3TotalSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 4),
    _Ds3TotalSEFSs_Type()
)
ds3TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalSEFSs.setStatus("mandatory")
_Ds3TotalUASs_Type = Counter32
_Ds3TotalUASs_Object = MibTableColumn
ds3TotalUASs = _Ds3TotalUASs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 5),
    _Ds3TotalUASs_Type()
)
ds3TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalUASs.setStatus("mandatory")
_Ds3TotalCSSs_Type = Counter32
_Ds3TotalCSSs_Object = MibTableColumn
ds3TotalCSSs = _Ds3TotalCSSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 6),
    _Ds3TotalCSSs_Type()
)
ds3TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalCSSs.setStatus("mandatory")
_Ds3TotalBPVs_Type = Counter32
_Ds3TotalBPVs_Object = MibTableColumn
ds3TotalBPVs = _Ds3TotalBPVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 7),
    _Ds3TotalBPVs_Type()
)
ds3TotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalBPVs.setStatus("mandatory")
_Ds3TotalCVs_Type = Counter32
_Ds3TotalCVs_Object = MibTableColumn
ds3TotalCVs = _Ds3TotalCVs_Object(
    (1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 8),
    _Ds3TotalCVs_Type()
)
ds3TotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TotalCVs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1233-MIB",
    **{"ds3": ds3,
       "ds3ConfigTable": ds3ConfigTable,
       "ds3ConfigEntry": ds3ConfigEntry,
       "ds3CSUIndex": ds3CSUIndex,
       "ds3Index": ds3Index,
       "ds3TimeElapsed": ds3TimeElapsed,
       "ds3ValidIntervals": ds3ValidIntervals,
       "ds3LineType": ds3LineType,
       "ds3ZeroCoding": ds3ZeroCoding,
       "ds3Loopback": ds3Loopback,
       "ds3SendCode": ds3SendCode,
       "ds3YellowAlarm": ds3YellowAlarm,
       "ds3RedAlarm": ds3RedAlarm,
       "ds3CircuitIdentifier": ds3CircuitIdentifier,
       "ds3IntervalTable": ds3IntervalTable,
       "ds3IntervalEntry": ds3IntervalEntry,
       "ds3IntervalIndex": ds3IntervalIndex,
       "ds3IntervalNumber": ds3IntervalNumber,
       "ds3IntervalESs": ds3IntervalESs,
       "ds3IntervalSESs": ds3IntervalSESs,
       "ds3IntervalSEFSs": ds3IntervalSEFSs,
       "ds3IntervalUASs": ds3IntervalUASs,
       "ds3IntervalCSSs": ds3IntervalCSSs,
       "ds3IntervalBPVs": ds3IntervalBPVs,
       "ds3IntervalCVs": ds3IntervalCVs,
       "ds3CurrentTable": ds3CurrentTable,
       "ds3CurrentEntry": ds3CurrentEntry,
       "ds3CurrentIndex": ds3CurrentIndex,
       "ds3CurrentESs": ds3CurrentESs,
       "ds3CurrentSESs": ds3CurrentSESs,
       "ds3CurrentSEFSs": ds3CurrentSEFSs,
       "ds3CurrentUASs": ds3CurrentUASs,
       "ds3CurrentCSSs": ds3CurrentCSSs,
       "ds3CurrentBPVs": ds3CurrentBPVs,
       "ds3CurrentCVs": ds3CurrentCVs,
       "ds3TotalTable": ds3TotalTable,
       "ds3TotalEntry": ds3TotalEntry,
       "ds3TotalIndex": ds3TotalIndex,
       "ds3TotalESs": ds3TotalESs,
       "ds3TotalSESs": ds3TotalSESs,
       "ds3TotalSEFSs": ds3TotalSEFSs,
       "ds3TotalUASs": ds3TotalUASs,
       "ds3TotalCSSs": ds3TotalCSSs,
       "ds3TotalBPVs": ds3TotalBPVs,
       "ds3TotalCVs": ds3TotalCVs}
)
