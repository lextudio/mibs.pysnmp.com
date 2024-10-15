# SNMP MIB module (CISCOSB-RMON) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-RMON
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:44 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlRmonControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49)
)
rlRmonControl.setRevisions(
        ("2004-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlRmonControlMibVersion_Type = Integer32
_RlRmonControlMibVersion_Object = MibScalar
rlRmonControlMibVersion = _RlRmonControlMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 1),
    _RlRmonControlMibVersion_Type()
)
rlRmonControlMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRmonControlMibVersion.setStatus("current")


class _RlRmonControlHistoryControlQuotaBucket_Type(Integer32):
    """Custom type rlRmonControlHistoryControlQuotaBucket based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlRmonControlHistoryControlQuotaBucket_Type.__name__ = "Integer32"
_RlRmonControlHistoryControlQuotaBucket_Object = MibScalar
rlRmonControlHistoryControlQuotaBucket = _RlRmonControlHistoryControlQuotaBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 2),
    _RlRmonControlHistoryControlQuotaBucket_Type()
)
rlRmonControlHistoryControlQuotaBucket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRmonControlHistoryControlQuotaBucket.setStatus("current")


class _RlRmonControlHistoryControlMaxGlobalBuckets_Type(Integer32):
    """Custom type rlRmonControlHistoryControlMaxGlobalBuckets based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlRmonControlHistoryControlMaxGlobalBuckets_Type.__name__ = "Integer32"
_RlRmonControlHistoryControlMaxGlobalBuckets_Object = MibScalar
rlRmonControlHistoryControlMaxGlobalBuckets = _RlRmonControlHistoryControlMaxGlobalBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 3),
    _RlRmonControlHistoryControlMaxGlobalBuckets_Type()
)
rlRmonControlHistoryControlMaxGlobalBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRmonControlHistoryControlMaxGlobalBuckets.setStatus("current")
_RlHistoryControlTable_Object = MibTable
rlHistoryControlTable = _RlHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4)
)
if mibBuilder.loadTexts:
    rlHistoryControlTable.setStatus("current")
_RlHistoryControlEntry_Object = MibTableRow
rlHistoryControlEntry = _RlHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1)
)
rlHistoryControlEntry.setIndexNames(
    (0, "CISCOSB-RMON", "rlHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    rlHistoryControlEntry.setStatus("current")


class _RlHistoryControlIndex_Type(Integer32):
    """Custom type rlHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlHistoryControlIndex_Type.__name__ = "Integer32"
_RlHistoryControlIndex_Object = MibTableColumn
rlHistoryControlIndex = _RlHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1, 1),
    _RlHistoryControlIndex_Type()
)
rlHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHistoryControlIndex.setStatus("current")
_RlHistoryControlDataSource_Type = ObjectIdentifier
_RlHistoryControlDataSource_Object = MibTableColumn
rlHistoryControlDataSource = _RlHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1, 2),
    _RlHistoryControlDataSource_Type()
)
rlHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlHistoryControlDataSource.setStatus("current")


class _RlHistoryControlBucketsRequested_Type(Integer32):
    """Custom type rlHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_RlHistoryControlBucketsRequested_Object = MibTableColumn
rlHistoryControlBucketsRequested = _RlHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1, 3),
    _RlHistoryControlBucketsRequested_Type()
)
rlHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlHistoryControlBucketsRequested.setStatus("current")


class _RlHistoryControlBucketsGranted_Type(Integer32):
    """Custom type rlHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_RlHistoryControlBucketsGranted_Object = MibTableColumn
rlHistoryControlBucketsGranted = _RlHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1, 4),
    _RlHistoryControlBucketsGranted_Type()
)
rlHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHistoryControlBucketsGranted.setStatus("current")


class _RlHistoryControlInterval_Type(Integer32):
    """Custom type rlHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RlHistoryControlInterval_Type.__name__ = "Integer32"
_RlHistoryControlInterval_Object = MibTableColumn
rlHistoryControlInterval = _RlHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1, 5),
    _RlHistoryControlInterval_Type()
)
rlHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlHistoryControlInterval.setStatus("current")
_RlHistoryControlOwner_Type = OwnerString
_RlHistoryControlOwner_Object = MibTableColumn
rlHistoryControlOwner = _RlHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1, 6),
    _RlHistoryControlOwner_Type()
)
rlHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlHistoryControlOwner.setStatus("current")
_RlHistoryControlStatus_Type = EntryStatus
_RlHistoryControlStatus_Object = MibTableColumn
rlHistoryControlStatus = _RlHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 4, 1, 7),
    _RlHistoryControlStatus_Type()
)
rlHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlHistoryControlStatus.setStatus("current")
_RlHistoryTable_Object = MibTable
rlHistoryTable = _RlHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 5)
)
if mibBuilder.loadTexts:
    rlHistoryTable.setStatus("current")
_RlHistoryEntry_Object = MibTableRow
rlHistoryEntry = _RlHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 5, 1)
)
rlHistoryEntry.setIndexNames(
    (0, "CISCOSB-RMON", "rlHistoryIndex"),
    (0, "CISCOSB-RMON", "rlHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    rlHistoryEntry.setStatus("current")


class _RlHistoryIndex_Type(Integer32):
    """Custom type rlHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlHistoryIndex_Type.__name__ = "Integer32"
_RlHistoryIndex_Object = MibTableColumn
rlHistoryIndex = _RlHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 5, 1, 1),
    _RlHistoryIndex_Type()
)
rlHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHistoryIndex.setStatus("current")


class _RlHistorySampleIndex_Type(Integer32):
    """Custom type rlHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlHistorySampleIndex_Type.__name__ = "Integer32"
_RlHistorySampleIndex_Object = MibTableColumn
rlHistorySampleIndex = _RlHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 5, 1, 2),
    _RlHistorySampleIndex_Type()
)
rlHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHistorySampleIndex.setStatus("current")
_RlHistoryIntervalStart_Type = TimeTicks
_RlHistoryIntervalStart_Object = MibTableColumn
rlHistoryIntervalStart = _RlHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 5, 1, 3),
    _RlHistoryIntervalStart_Type()
)
rlHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHistoryIntervalStart.setStatus("current")
_RlHistoryValue_Type = Counter32
_RlHistoryValue_Object = MibTableColumn
rlHistoryValue = _RlHistoryValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 5, 1, 4),
    _RlHistoryValue_Type()
)
rlHistoryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlHistoryValue.setStatus("current")


class _RlControlHistoryControlQuotaBucket_Type(Integer32):
    """Custom type rlControlHistoryControlQuotaBucket based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlControlHistoryControlQuotaBucket_Type.__name__ = "Integer32"
_RlControlHistoryControlQuotaBucket_Object = MibScalar
rlControlHistoryControlQuotaBucket = _RlControlHistoryControlQuotaBucket_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 6),
    _RlControlHistoryControlQuotaBucket_Type()
)
rlControlHistoryControlQuotaBucket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlControlHistoryControlQuotaBucket.setStatus("current")


class _RlControlHistoryControlMaxGlobalBuckets_Type(Integer32):
    """Custom type rlControlHistoryControlMaxGlobalBuckets based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlControlHistoryControlMaxGlobalBuckets_Type.__name__ = "Integer32"
_RlControlHistoryControlMaxGlobalBuckets_Object = MibScalar
rlControlHistoryControlMaxGlobalBuckets = _RlControlHistoryControlMaxGlobalBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 7),
    _RlControlHistoryControlMaxGlobalBuckets_Type()
)
rlControlHistoryControlMaxGlobalBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlControlHistoryControlMaxGlobalBuckets.setStatus("current")


class _RlControlHistoryMaxEntries_Type(Integer32):
    """Custom type rlControlHistoryMaxEntries based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlControlHistoryMaxEntries_Type.__name__ = "Integer32"
_RlControlHistoryMaxEntries_Object = MibScalar
rlControlHistoryMaxEntries = _RlControlHistoryMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49, 8),
    _RlControlHistoryMaxEntries_Type()
)
rlControlHistoryMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlControlHistoryMaxEntries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-RMON",
    **{"rlRmonControl": rlRmonControl,
       "rlRmonControlMibVersion": rlRmonControlMibVersion,
       "rlRmonControlHistoryControlQuotaBucket": rlRmonControlHistoryControlQuotaBucket,
       "rlRmonControlHistoryControlMaxGlobalBuckets": rlRmonControlHistoryControlMaxGlobalBuckets,
       "rlHistoryControlTable": rlHistoryControlTable,
       "rlHistoryControlEntry": rlHistoryControlEntry,
       "rlHistoryControlIndex": rlHistoryControlIndex,
       "rlHistoryControlDataSource": rlHistoryControlDataSource,
       "rlHistoryControlBucketsRequested": rlHistoryControlBucketsRequested,
       "rlHistoryControlBucketsGranted": rlHistoryControlBucketsGranted,
       "rlHistoryControlInterval": rlHistoryControlInterval,
       "rlHistoryControlOwner": rlHistoryControlOwner,
       "rlHistoryControlStatus": rlHistoryControlStatus,
       "rlHistoryTable": rlHistoryTable,
       "rlHistoryEntry": rlHistoryEntry,
       "rlHistoryIndex": rlHistoryIndex,
       "rlHistorySampleIndex": rlHistorySampleIndex,
       "rlHistoryIntervalStart": rlHistoryIntervalStart,
       "rlHistoryValue": rlHistoryValue,
       "rlControlHistoryControlQuotaBucket": rlControlHistoryControlQuotaBucket,
       "rlControlHistoryControlMaxGlobalBuckets": rlControlHistoryControlMaxGlobalBuckets,
       "rlControlHistoryMaxEntries": rlControlHistoryMaxEntries}
)
