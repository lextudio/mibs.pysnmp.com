# SNMP MIB module (RFC1284-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1284-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:18 2024
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

_Dot3_ObjectIdentity = ObjectIdentity
dot3 = _Dot3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7)
)
_Dot3Table_Object = MibTable
dot3Table = _Dot3Table_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1)
)
if mibBuilder.loadTexts:
    dot3Table.setStatus("mandatory")
_Dot3Entry_Object = MibTableRow
dot3Entry = _Dot3Entry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1)
)
dot3Entry.setIndexNames(
    (0, "RFC1284-MIB", "dot3Index"),
)
if mibBuilder.loadTexts:
    dot3Entry.setStatus("mandatory")
_Dot3Index_Type = Integer32
_Dot3Index_Object = MibTableColumn
dot3Index = _Dot3Index_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 1),
    _Dot3Index_Type()
)
dot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3Index.setStatus("mandatory")


class _Dot3InitializeMac_Type(Integer32):
    """Custom type dot3InitializeMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 1),
          ("uninitialized", 2))
    )


_Dot3InitializeMac_Type.__name__ = "Integer32"
_Dot3InitializeMac_Object = MibTableColumn
dot3InitializeMac = _Dot3InitializeMac_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 2),
    _Dot3InitializeMac_Type()
)
dot3InitializeMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3InitializeMac.setStatus("mandatory")


class _Dot3MacSubLayerStatus_Type(Integer32):
    """Custom type dot3MacSubLayerStatus based on Integer32"""
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


_Dot3MacSubLayerStatus_Type.__name__ = "Integer32"
_Dot3MacSubLayerStatus_Object = MibTableColumn
dot3MacSubLayerStatus = _Dot3MacSubLayerStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 3),
    _Dot3MacSubLayerStatus_Type()
)
dot3MacSubLayerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3MacSubLayerStatus.setStatus("mandatory")


class _Dot3MulticastReceiveStatus_Type(Integer32):
    """Custom type dot3MulticastReceiveStatus based on Integer32"""
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


_Dot3MulticastReceiveStatus_Type.__name__ = "Integer32"
_Dot3MulticastReceiveStatus_Object = MibTableColumn
dot3MulticastReceiveStatus = _Dot3MulticastReceiveStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 4),
    _Dot3MulticastReceiveStatus_Type()
)
dot3MulticastReceiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3MulticastReceiveStatus.setStatus("mandatory")


class _Dot3TxEnabled_Type(Integer32):
    """Custom type dot3TxEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Dot3TxEnabled_Type.__name__ = "Integer32"
_Dot3TxEnabled_Object = MibTableColumn
dot3TxEnabled = _Dot3TxEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 5),
    _Dot3TxEnabled_Type()
)
dot3TxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3TxEnabled.setStatus("mandatory")
_Dot3TestTdrValue_Type = Gauge32
_Dot3TestTdrValue_Object = MibTableColumn
dot3TestTdrValue = _Dot3TestTdrValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 1, 1, 6),
    _Dot3TestTdrValue_Type()
)
dot3TestTdrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TestTdrValue.setStatus("mandatory")
_Dot3StatsTable_Object = MibTable
dot3StatsTable = _Dot3StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    dot3StatsTable.setStatus("mandatory")
_Dot3StatsEntry_Object = MibTableRow
dot3StatsEntry = _Dot3StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1)
)
dot3StatsEntry.setIndexNames(
    (0, "RFC1284-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    dot3StatsEntry.setStatus("mandatory")
_Dot3StatsIndex_Type = Integer32
_Dot3StatsIndex_Object = MibTableColumn
dot3StatsIndex = _Dot3StatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1),
    _Dot3StatsIndex_Type()
)
dot3StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsIndex.setStatus("mandatory")
_Dot3StatsAlignmentErrors_Type = Counter32
_Dot3StatsAlignmentErrors_Object = MibTableColumn
dot3StatsAlignmentErrors = _Dot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2),
    _Dot3StatsAlignmentErrors_Type()
)
dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsAlignmentErrors.setStatus("mandatory")
_Dot3StatsFCSErrors_Type = Counter32
_Dot3StatsFCSErrors_Object = MibTableColumn
dot3StatsFCSErrors = _Dot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3),
    _Dot3StatsFCSErrors_Type()
)
dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFCSErrors.setStatus("mandatory")
_Dot3StatsSingleCollisionFrames_Type = Counter32
_Dot3StatsSingleCollisionFrames_Object = MibTableColumn
dot3StatsSingleCollisionFrames = _Dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4),
    _Dot3StatsSingleCollisionFrames_Type()
)
dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSingleCollisionFrames.setStatus("mandatory")
_Dot3StatsMultipleCollisionFrames_Type = Counter32
_Dot3StatsMultipleCollisionFrames_Object = MibTableColumn
dot3StatsMultipleCollisionFrames = _Dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5),
    _Dot3StatsMultipleCollisionFrames_Type()
)
dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsMultipleCollisionFrames.setStatus("mandatory")
_Dot3StatsSQETestErrors_Type = Counter32
_Dot3StatsSQETestErrors_Object = MibTableColumn
dot3StatsSQETestErrors = _Dot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6),
    _Dot3StatsSQETestErrors_Type()
)
dot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsSQETestErrors.setStatus("mandatory")
_Dot3StatsDeferredTransmissions_Type = Counter32
_Dot3StatsDeferredTransmissions_Object = MibTableColumn
dot3StatsDeferredTransmissions = _Dot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7),
    _Dot3StatsDeferredTransmissions_Type()
)
dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsDeferredTransmissions.setStatus("mandatory")
_Dot3StatsLateCollisions_Type = Counter32
_Dot3StatsLateCollisions_Object = MibTableColumn
dot3StatsLateCollisions = _Dot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8),
    _Dot3StatsLateCollisions_Type()
)
dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsLateCollisions.setStatus("mandatory")
_Dot3StatsExcessiveCollisions_Type = Counter32
_Dot3StatsExcessiveCollisions_Object = MibTableColumn
dot3StatsExcessiveCollisions = _Dot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9),
    _Dot3StatsExcessiveCollisions_Type()
)
dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveCollisions.setStatus("mandatory")
_Dot3StatsInternalMacTransmitErrors_Type = Counter32
_Dot3StatsInternalMacTransmitErrors_Object = MibTableColumn
dot3StatsInternalMacTransmitErrors = _Dot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10),
    _Dot3StatsInternalMacTransmitErrors_Type()
)
dot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacTransmitErrors.setStatus("mandatory")
_Dot3StatsCarrierSenseErrors_Type = Counter32
_Dot3StatsCarrierSenseErrors_Object = MibTableColumn
dot3StatsCarrierSenseErrors = _Dot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11),
    _Dot3StatsCarrierSenseErrors_Type()
)
dot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsCarrierSenseErrors.setStatus("mandatory")
_Dot3StatsExcessiveDeferrals_Type = Counter32
_Dot3StatsExcessiveDeferrals_Object = MibTableColumn
dot3StatsExcessiveDeferrals = _Dot3StatsExcessiveDeferrals_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 12),
    _Dot3StatsExcessiveDeferrals_Type()
)
dot3StatsExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsExcessiveDeferrals.setStatus("mandatory")
_Dot3StatsFrameTooLongs_Type = Counter32
_Dot3StatsFrameTooLongs_Object = MibTableColumn
dot3StatsFrameTooLongs = _Dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13),
    _Dot3StatsFrameTooLongs_Type()
)
dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsFrameTooLongs.setStatus("mandatory")
_Dot3StatsInRangeLengthErrors_Type = Counter32
_Dot3StatsInRangeLengthErrors_Object = MibTableColumn
dot3StatsInRangeLengthErrors = _Dot3StatsInRangeLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 14),
    _Dot3StatsInRangeLengthErrors_Type()
)
dot3StatsInRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInRangeLengthErrors.setStatus("mandatory")
_Dot3StatsOutOfRangeLengthFields_Type = Counter32
_Dot3StatsOutOfRangeLengthFields_Object = MibTableColumn
dot3StatsOutOfRangeLengthFields = _Dot3StatsOutOfRangeLengthFields_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 15),
    _Dot3StatsOutOfRangeLengthFields_Type()
)
dot3StatsOutOfRangeLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsOutOfRangeLengthFields.setStatus("mandatory")
_Dot3StatsInternalMacReceiveErrors_Type = Counter32
_Dot3StatsInternalMacReceiveErrors_Object = MibTableColumn
dot3StatsInternalMacReceiveErrors = _Dot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16),
    _Dot3StatsInternalMacReceiveErrors_Type()
)
dot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3StatsInternalMacReceiveErrors.setStatus("mandatory")
_Dot3CollTable_Object = MibTable
dot3CollTable = _Dot3CollTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5)
)
if mibBuilder.loadTexts:
    dot3CollTable.setStatus("mandatory")
_Dot3CollEntry_Object = MibTableRow
dot3CollEntry = _Dot3CollEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1)
)
dot3CollEntry.setIndexNames(
    (0, "RFC1284-MIB", "dot3CollIndex"),
    (0, "RFC1284-MIB", "dot3CollCount"),
)
if mibBuilder.loadTexts:
    dot3CollEntry.setStatus("mandatory")
_Dot3CollIndex_Type = Integer32
_Dot3CollIndex_Object = MibTableColumn
dot3CollIndex = _Dot3CollIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 1),
    _Dot3CollIndex_Type()
)
dot3CollIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollIndex.setStatus("mandatory")


class _Dot3CollCount_Type(Integer32):
    """Custom type dot3CollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot3CollCount_Type.__name__ = "Integer32"
_Dot3CollCount_Object = MibTableColumn
dot3CollCount = _Dot3CollCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 2),
    _Dot3CollCount_Type()
)
dot3CollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollCount.setStatus("mandatory")
_Dot3CollFrequencies_Type = Counter32
_Dot3CollFrequencies_Object = MibTableColumn
dot3CollFrequencies = _Dot3CollFrequencies_Object(
    (1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 3),
    _Dot3CollFrequencies_Type()
)
dot3CollFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollFrequencies.setStatus("mandatory")
_Dot3Tests_ObjectIdentity = ObjectIdentity
dot3Tests = _Dot3Tests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6)
)
_Dot3TestTdr_ObjectIdentity = ObjectIdentity
dot3TestTdr = _Dot3TestTdr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 6, 1)
)
_Dot3Errors_ObjectIdentity = ObjectIdentity
dot3Errors = _Dot3Errors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7)
)
_Dot3ErrorInitError_ObjectIdentity = ObjectIdentity
dot3ErrorInitError = _Dot3ErrorInitError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 1)
)
_Dot3ErrorLoopbackError_ObjectIdentity = ObjectIdentity
dot3ErrorLoopbackError = _Dot3ErrorLoopbackError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 7, 2)
)
_Dot3ChipSets_ObjectIdentity = ObjectIdentity
dot3ChipSets = _Dot3ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8)
)
_Dot3ChipSetAMD_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD = _Dot3ChipSetAMD_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1)
)
_Dot3ChipSetAMD7990_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD7990 = _Dot3ChipSetAMD7990_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 1)
)
_Dot3ChipSetAMD79900_ObjectIdentity = ObjectIdentity
dot3ChipSetAMD79900 = _Dot3ChipSetAMD79900_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 1, 2)
)
_Dot3ChipSetIntel_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel = _Dot3ChipSetIntel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2)
)
_Dot3ChipSetIntel82586_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel82586 = _Dot3ChipSetIntel82586_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 1)
)
_Dot3ChipSetIntel82596_ObjectIdentity = ObjectIdentity
dot3ChipSetIntel82596 = _Dot3ChipSetIntel82596_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 2, 2)
)
_Dot3ChipSetSeeq_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq = _Dot3ChipSetSeeq_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3)
)
_Dot3ChipSetSeeq8003_ObjectIdentity = ObjectIdentity
dot3ChipSetSeeq8003 = _Dot3ChipSetSeeq8003_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 3, 1)
)
_Dot3ChipSetNational_ObjectIdentity = ObjectIdentity
dot3ChipSetNational = _Dot3ChipSetNational_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4)
)
_Dot3ChipSetNational8390_ObjectIdentity = ObjectIdentity
dot3ChipSetNational8390 = _Dot3ChipSetNational8390_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 1)
)
_Dot3ChipSetNationalSonic_ObjectIdentity = ObjectIdentity
dot3ChipSetNationalSonic = _Dot3ChipSetNationalSonic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 4, 2)
)
_Dot3ChipSetFujitsu_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu = _Dot3ChipSetFujitsu_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5)
)
_Dot3ChipSetFujitsu86950_ObjectIdentity = ObjectIdentity
dot3ChipSetFujitsu86950 = _Dot3ChipSetFujitsu86950_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 7, 8, 5, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1284-MIB",
    **{"dot3": dot3,
       "dot3Table": dot3Table,
       "dot3Entry": dot3Entry,
       "dot3Index": dot3Index,
       "dot3InitializeMac": dot3InitializeMac,
       "dot3MacSubLayerStatus": dot3MacSubLayerStatus,
       "dot3MulticastReceiveStatus": dot3MulticastReceiveStatus,
       "dot3TxEnabled": dot3TxEnabled,
       "dot3TestTdrValue": dot3TestTdrValue,
       "dot3StatsTable": dot3StatsTable,
       "dot3StatsEntry": dot3StatsEntry,
       "dot3StatsIndex": dot3StatsIndex,
       "dot3StatsAlignmentErrors": dot3StatsAlignmentErrors,
       "dot3StatsFCSErrors": dot3StatsFCSErrors,
       "dot3StatsSingleCollisionFrames": dot3StatsSingleCollisionFrames,
       "dot3StatsMultipleCollisionFrames": dot3StatsMultipleCollisionFrames,
       "dot3StatsSQETestErrors": dot3StatsSQETestErrors,
       "dot3StatsDeferredTransmissions": dot3StatsDeferredTransmissions,
       "dot3StatsLateCollisions": dot3StatsLateCollisions,
       "dot3StatsExcessiveCollisions": dot3StatsExcessiveCollisions,
       "dot3StatsInternalMacTransmitErrors": dot3StatsInternalMacTransmitErrors,
       "dot3StatsCarrierSenseErrors": dot3StatsCarrierSenseErrors,
       "dot3StatsExcessiveDeferrals": dot3StatsExcessiveDeferrals,
       "dot3StatsFrameTooLongs": dot3StatsFrameTooLongs,
       "dot3StatsInRangeLengthErrors": dot3StatsInRangeLengthErrors,
       "dot3StatsOutOfRangeLengthFields": dot3StatsOutOfRangeLengthFields,
       "dot3StatsInternalMacReceiveErrors": dot3StatsInternalMacReceiveErrors,
       "dot3CollTable": dot3CollTable,
       "dot3CollEntry": dot3CollEntry,
       "dot3CollIndex": dot3CollIndex,
       "dot3CollCount": dot3CollCount,
       "dot3CollFrequencies": dot3CollFrequencies,
       "dot3Tests": dot3Tests,
       "dot3TestTdr": dot3TestTdr,
       "dot3Errors": dot3Errors,
       "dot3ErrorInitError": dot3ErrorInitError,
       "dot3ErrorLoopbackError": dot3ErrorLoopbackError,
       "dot3ChipSets": dot3ChipSets,
       "dot3ChipSetAMD": dot3ChipSetAMD,
       "dot3ChipSetAMD7990": dot3ChipSetAMD7990,
       "dot3ChipSetAMD79900": dot3ChipSetAMD79900,
       "dot3ChipSetIntel": dot3ChipSetIntel,
       "dot3ChipSetIntel82586": dot3ChipSetIntel82586,
       "dot3ChipSetIntel82596": dot3ChipSetIntel82596,
       "dot3ChipSetSeeq": dot3ChipSetSeeq,
       "dot3ChipSetSeeq8003": dot3ChipSetSeeq8003,
       "dot3ChipSetNational": dot3ChipSetNational,
       "dot3ChipSetNational8390": dot3ChipSetNational8390,
       "dot3ChipSetNationalSonic": dot3ChipSetNationalSonic,
       "dot3ChipSetFujitsu": dot3ChipSetFujitsu,
       "dot3ChipSetFujitsu86950": dot3ChipSetFujitsu86950}
)
