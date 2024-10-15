# SNMP MIB module (ALCATEL-IND1-PCAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PCAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:42 2024
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

(hardentIND1Pcam,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardentIND1Pcam")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1PCAMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1)
)
alcatelIND1PCAMMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoroL3HashFunction(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PCAMMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PCAMMIBObjects = _AlcatelIND1PCAMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PCAMMIBObjects.setStatus("current")
_AlaCoroL3HrePerModeTable_Object = MibTable
alaCoroL3HrePerModeTable = _AlaCoroL3HrePerModeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaCoroL3HrePerModeTable.setStatus("current")
_AlaCoroL3HrePerModeTableEntry_Object = MibTableRow
alaCoroL3HrePerModeTableEntry = _AlaCoroL3HrePerModeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1)
)
alaCoroL3HrePerModeTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HrePerModeSlotNumber"),
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HrePerModeSliceNumber"),
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HrePerModeModeNumber"),
)
if mibBuilder.loadTexts:
    alaCoroL3HrePerModeTableEntry.setStatus("current")
_AlaCoroL3HrePerModeSlotNumber_Type = Unsigned32
_AlaCoroL3HrePerModeSlotNumber_Object = MibTableColumn
alaCoroL3HrePerModeSlotNumber = _AlaCoroL3HrePerModeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 1),
    _AlaCoroL3HrePerModeSlotNumber_Type()
)
alaCoroL3HrePerModeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HrePerModeSlotNumber.setStatus("current")
_AlaCoroL3HrePerModeSliceNumber_Type = Unsigned32
_AlaCoroL3HrePerModeSliceNumber_Object = MibTableColumn
alaCoroL3HrePerModeSliceNumber = _AlaCoroL3HrePerModeSliceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 2),
    _AlaCoroL3HrePerModeSliceNumber_Type()
)
alaCoroL3HrePerModeSliceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HrePerModeSliceNumber.setStatus("current")


class _AlaCoroL3HrePerModeModeNumber_Type(Integer32):
    """Custom type alaCoroL3HrePerModeModeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaCoroL3HrePerModeModeNumber_Type.__name__ = "Integer32"
_AlaCoroL3HrePerModeModeNumber_Object = MibTableColumn
alaCoroL3HrePerModeModeNumber = _AlaCoroL3HrePerModeModeNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 3),
    _AlaCoroL3HrePerModeModeNumber_Type()
)
alaCoroL3HrePerModeModeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HrePerModeModeNumber.setStatus("current")
_AlaCoroL3HreModeHashTableSize_Type = Unsigned32
_AlaCoroL3HreModeHashTableSize_Object = MibTableColumn
alaCoroL3HreModeHashTableSize = _AlaCoroL3HreModeHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 4),
    _AlaCoroL3HreModeHashTableSize_Type()
)
alaCoroL3HreModeHashTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreModeHashTableSize.setStatus("current")
_AlaCoroL3HreModeHashEntriesInUse_Type = Unsigned32
_AlaCoroL3HreModeHashEntriesInUse_Object = MibTableColumn
alaCoroL3HreModeHashEntriesInUse = _AlaCoroL3HreModeHashEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 5),
    _AlaCoroL3HreModeHashEntriesInUse_Type()
)
alaCoroL3HreModeHashEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreModeHashEntriesInUse.setStatus("current")
_AlaCoroL3HreModeCollEntriesInUse_Type = Unsigned32
_AlaCoroL3HreModeCollEntriesInUse_Object = MibTableColumn
alaCoroL3HreModeCollEntriesInUse = _AlaCoroL3HreModeCollEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 6),
    _AlaCoroL3HreModeCollEntriesInUse_Type()
)
alaCoroL3HreModeCollEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreModeCollEntriesInUse.setStatus("current")
_AlaCoroL3HreModeCurrentHashFunction_Type = CoroL3HashFunction
_AlaCoroL3HreModeCurrentHashFunction_Object = MibTableColumn
alaCoroL3HreModeCurrentHashFunction = _AlaCoroL3HreModeCurrentHashFunction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 7),
    _AlaCoroL3HreModeCurrentHashFunction_Type()
)
alaCoroL3HreModeCurrentHashFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreModeCurrentHashFunction.setStatus("current")
_AlaCoroL3HreMaxCollChainLen_Type = Unsigned32
_AlaCoroL3HreMaxCollChainLen_Object = MibTableColumn
alaCoroL3HreMaxCollChainLen = _AlaCoroL3HreMaxCollChainLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 8),
    _AlaCoroL3HreMaxCollChainLen_Type()
)
alaCoroL3HreMaxCollChainLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreMaxCollChainLen.setStatus("current")
_AlaCoroL3HreAvgCollChainLen_Type = Unsigned32
_AlaCoroL3HreAvgCollChainLen_Object = MibTableColumn
alaCoroL3HreAvgCollChainLen = _AlaCoroL3HreAvgCollChainLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 1, 1, 9),
    _AlaCoroL3HreAvgCollChainLen_Type()
)
alaCoroL3HreAvgCollChainLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreAvgCollChainLen.setStatus("current")
_AlaCoroL3HrePerCoronadoStatsTable_Object = MibTable
alaCoroL3HrePerCoronadoStatsTable = _AlaCoroL3HrePerCoronadoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaCoroL3HrePerCoronadoStatsTable.setStatus("current")
_AlaCoroL3HrePerCoronadoStatsTableEntry_Object = MibTableRow
alaCoroL3HrePerCoronadoStatsTableEntry = _AlaCoroL3HrePerCoronadoStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1)
)
alaCoroL3HrePerCoronadoStatsTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreSlotNumber"),
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreSliceNumber"),
)
if mibBuilder.loadTexts:
    alaCoroL3HrePerCoronadoStatsTableEntry.setStatus("current")
_AlaCoroL3HreSlotNumber_Type = Unsigned32
_AlaCoroL3HreSlotNumber_Object = MibTableColumn
alaCoroL3HreSlotNumber = _AlaCoroL3HreSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 1),
    _AlaCoroL3HreSlotNumber_Type()
)
alaCoroL3HreSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreSlotNumber.setStatus("current")
_AlaCoroL3HreSliceNumber_Type = Unsigned32
_AlaCoroL3HreSliceNumber_Object = MibTableColumn
alaCoroL3HreSliceNumber = _AlaCoroL3HreSliceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 2),
    _AlaCoroL3HreSliceNumber_Type()
)
alaCoroL3HreSliceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreSliceNumber.setStatus("current")
_AlaCoroL3HreRouteCacheEntriesTotal_Type = Unsigned32
_AlaCoroL3HreRouteCacheEntriesTotal_Object = MibTableColumn
alaCoroL3HreRouteCacheEntriesTotal = _AlaCoroL3HreRouteCacheEntriesTotal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 3),
    _AlaCoroL3HreRouteCacheEntriesTotal_Type()
)
alaCoroL3HreRouteCacheEntriesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreRouteCacheEntriesTotal.setStatus("current")
_AlaCoroL3HreRouteCacheEntriesInUse_Type = Unsigned32
_AlaCoroL3HreRouteCacheEntriesInUse_Object = MibTableColumn
alaCoroL3HreRouteCacheEntriesInUse = _AlaCoroL3HreRouteCacheEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 4),
    _AlaCoroL3HreRouteCacheEntriesInUse_Type()
)
alaCoroL3HreRouteCacheEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreRouteCacheEntriesInUse.setStatus("current")
_AlaCoroL3HreIpPacketsReceived_Type = Counter64
_AlaCoroL3HreIpPacketsReceived_Object = MibTableColumn
alaCoroL3HreIpPacketsReceived = _AlaCoroL3HreIpPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 5),
    _AlaCoroL3HreIpPacketsReceived_Type()
)
alaCoroL3HreIpPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpPacketsReceived.setStatus("current")
_AlaCoroL3HreIpBytesReceived_Type = Counter64
_AlaCoroL3HreIpBytesReceived_Object = MibTableColumn
alaCoroL3HreIpBytesReceived = _AlaCoroL3HreIpBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 6),
    _AlaCoroL3HreIpBytesReceived_Type()
)
alaCoroL3HreIpBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpBytesReceived.setStatus("current")
_AlaCoroL3HreIpPacketsForwarded_Type = Counter64
_AlaCoroL3HreIpPacketsForwarded_Object = MibTableColumn
alaCoroL3HreIpPacketsForwarded = _AlaCoroL3HreIpPacketsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 7),
    _AlaCoroL3HreIpPacketsForwarded_Type()
)
alaCoroL3HreIpPacketsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpPacketsForwarded.setStatus("current")
_AlaCoroL3HreIpBytesForwarded_Type = Counter64
_AlaCoroL3HreIpBytesForwarded_Object = MibTableColumn
alaCoroL3HreIpBytesForwarded = _AlaCoroL3HreIpBytesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 8),
    _AlaCoroL3HreIpBytesForwarded_Type()
)
alaCoroL3HreIpBytesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpBytesForwarded.setStatus("current")
_AlaCoroL3HreIpPacketsDiscarded_Type = Counter64
_AlaCoroL3HreIpPacketsDiscarded_Object = MibTableColumn
alaCoroL3HreIpPacketsDiscarded = _AlaCoroL3HreIpPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 9),
    _AlaCoroL3HreIpPacketsDiscarded_Type()
)
alaCoroL3HreIpPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpPacketsDiscarded.setStatus("current")
_AlaCoroL3HreIpBytesDiscarded_Type = Counter64
_AlaCoroL3HreIpBytesDiscarded_Object = MibTableColumn
alaCoroL3HreIpBytesDiscarded = _AlaCoroL3HreIpBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 10),
    _AlaCoroL3HreIpBytesDiscarded_Type()
)
alaCoroL3HreIpBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpBytesDiscarded.setStatus("current")
_AlaCoroL3HreIpPacketsFragmented_Type = Counter64
_AlaCoroL3HreIpPacketsFragmented_Object = MibTableColumn
alaCoroL3HreIpPacketsFragmented = _AlaCoroL3HreIpPacketsFragmented_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 11),
    _AlaCoroL3HreIpPacketsFragmented_Type()
)
alaCoroL3HreIpPacketsFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpPacketsFragmented.setStatus("current")
_AlaCoroL3HreIpPacketsFragsGenerated_Type = Counter64
_AlaCoroL3HreIpPacketsFragsGenerated_Object = MibTableColumn
alaCoroL3HreIpPacketsFragsGenerated = _AlaCoroL3HreIpPacketsFragsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 12),
    _AlaCoroL3HreIpPacketsFragsGenerated_Type()
)
alaCoroL3HreIpPacketsFragsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpPacketsFragsGenerated.setStatus("current")
_AlaCoroL3HreIpPacketsFailedToFrag_Type = Counter64
_AlaCoroL3HreIpPacketsFailedToFrag_Object = MibTableColumn
alaCoroL3HreIpPacketsFailedToFrag = _AlaCoroL3HreIpPacketsFailedToFrag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 13),
    _AlaCoroL3HreIpPacketsFailedToFrag_Type()
)
alaCoroL3HreIpPacketsFailedToFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpPacketsFailedToFrag.setStatus("current")
_AlaCoroL3HreIpxPacketsReceived_Type = Counter64
_AlaCoroL3HreIpxPacketsReceived_Object = MibTableColumn
alaCoroL3HreIpxPacketsReceived = _AlaCoroL3HreIpxPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 14),
    _AlaCoroL3HreIpxPacketsReceived_Type()
)
alaCoroL3HreIpxPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpxPacketsReceived.setStatus("current")
_AlaCoroL3HreIpxBytesReceived_Type = Counter64
_AlaCoroL3HreIpxBytesReceived_Object = MibTableColumn
alaCoroL3HreIpxBytesReceived = _AlaCoroL3HreIpxBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 15),
    _AlaCoroL3HreIpxBytesReceived_Type()
)
alaCoroL3HreIpxBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpxBytesReceived.setStatus("current")
_AlaCoroL3HreIpxPacketsForwarded_Type = Counter64
_AlaCoroL3HreIpxPacketsForwarded_Object = MibTableColumn
alaCoroL3HreIpxPacketsForwarded = _AlaCoroL3HreIpxPacketsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 16),
    _AlaCoroL3HreIpxPacketsForwarded_Type()
)
alaCoroL3HreIpxPacketsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpxPacketsForwarded.setStatus("current")
_AlaCoroL3HreIpxBytesForwarded_Type = Counter64
_AlaCoroL3HreIpxBytesForwarded_Object = MibTableColumn
alaCoroL3HreIpxBytesForwarded = _AlaCoroL3HreIpxBytesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 17),
    _AlaCoroL3HreIpxBytesForwarded_Type()
)
alaCoroL3HreIpxBytesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpxBytesForwarded.setStatus("current")
_AlaCoroL3HreIpxPacketsDiscarded_Type = Counter64
_AlaCoroL3HreIpxPacketsDiscarded_Object = MibTableColumn
alaCoroL3HreIpxPacketsDiscarded = _AlaCoroL3HreIpxPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 18),
    _AlaCoroL3HreIpxPacketsDiscarded_Type()
)
alaCoroL3HreIpxPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpxPacketsDiscarded.setStatus("current")
_AlaCoroL3HreIpxBytesDiscarded_Type = Counter64
_AlaCoroL3HreIpxBytesDiscarded_Object = MibTableColumn
alaCoroL3HreIpxBytesDiscarded = _AlaCoroL3HreIpxBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 2, 1, 19),
    _AlaCoroL3HreIpxBytesDiscarded_Type()
)
alaCoroL3HreIpxBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreIpxBytesDiscarded.setStatus("current")


class _AlaCoroL3HreUpdateChanges_Type(Integer32):
    """Custom type alaCoroL3HreUpdateChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 0),
          ("clear", 1))
    )


_AlaCoroL3HreUpdateChanges_Type.__name__ = "Integer32"
_AlaCoroL3HreUpdateChanges_Object = MibScalar
alaCoroL3HreUpdateChanges = _AlaCoroL3HreUpdateChanges_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 3),
    _AlaCoroL3HreUpdateChanges_Type()
)
alaCoroL3HreUpdateChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCoroL3HreUpdateChanges.setStatus("current")
_AlaCoroL3HreChangeTable_Object = MibTable
alaCoroL3HreChangeTable = _AlaCoroL3HreChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaCoroL3HreChangeTable.setStatus("current")
_AlaCoroL3HreChangeTableEntry_Object = MibTableRow
alaCoroL3HreChangeTableEntry = _AlaCoroL3HreChangeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4, 1)
)
alaCoroL3HreChangeTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeSlotNumber"),
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeSliceNumber"),
    (0, "ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeModeNumber"),
)
if mibBuilder.loadTexts:
    alaCoroL3HreChangeTableEntry.setStatus("current")
_AlaCoroL3HreChangeSlotNumber_Type = Unsigned32
_AlaCoroL3HreChangeSlotNumber_Object = MibTableColumn
alaCoroL3HreChangeSlotNumber = _AlaCoroL3HreChangeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4, 1, 1),
    _AlaCoroL3HreChangeSlotNumber_Type()
)
alaCoroL3HreChangeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreChangeSlotNumber.setStatus("current")
_AlaCoroL3HreChangeSliceNumber_Type = Unsigned32
_AlaCoroL3HreChangeSliceNumber_Object = MibTableColumn
alaCoroL3HreChangeSliceNumber = _AlaCoroL3HreChangeSliceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4, 1, 2),
    _AlaCoroL3HreChangeSliceNumber_Type()
)
alaCoroL3HreChangeSliceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreChangeSliceNumber.setStatus("current")


class _AlaCoroL3HreChangeModeNumber_Type(Integer32):
    """Custom type alaCoroL3HreChangeModeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaCoroL3HreChangeModeNumber_Type.__name__ = "Integer32"
_AlaCoroL3HreChangeModeNumber_Object = MibTableColumn
alaCoroL3HreChangeModeNumber = _AlaCoroL3HreChangeModeNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4, 1, 3),
    _AlaCoroL3HreChangeModeNumber_Type()
)
alaCoroL3HreChangeModeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCoroL3HreChangeModeNumber.setStatus("current")
_AlaCoroL3HreChangeHashTableSize_Type = Unsigned32
_AlaCoroL3HreChangeHashTableSize_Object = MibTableColumn
alaCoroL3HreChangeHashTableSize = _AlaCoroL3HreChangeHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4, 1, 4),
    _AlaCoroL3HreChangeHashTableSize_Type()
)
alaCoroL3HreChangeHashTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCoroL3HreChangeHashTableSize.setStatus("current")
_AlaCoroL3HreChangeHashFunction_Type = CoroL3HashFunction
_AlaCoroL3HreChangeHashFunction_Object = MibTableColumn
alaCoroL3HreChangeHashFunction = _AlaCoroL3HreChangeHashFunction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4, 1, 5),
    _AlaCoroL3HreChangeHashFunction_Type()
)
alaCoroL3HreChangeHashFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCoroL3HreChangeHashFunction.setStatus("current")


class _AlaCoroL3HreChangeClear_Type(Integer32):
    """Custom type alaCoroL3HreChangeClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("clear", 0)
    )


_AlaCoroL3HreChangeClear_Type.__name__ = "Integer32"
_AlaCoroL3HreChangeClear_Object = MibTableColumn
alaCoroL3HreChangeClear = _AlaCoroL3HreChangeClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 1, 4, 1, 6),
    _AlaCoroL3HreChangeClear_Type()
)
alaCoroL3HreChangeClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCoroL3HreChangeClear.setStatus("current")
_AlcatelIND1PCAMMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PCAMMIBConformance = _AlcatelIND1PCAMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PCAMMIBConformance.setStatus("current")
_AlcatelIND1PCAMMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PCAMMIBGroups = _AlcatelIND1PCAMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PCAMMIBGroups.setStatus("current")
_AlcatelIND1PCAMMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PCAMMIBCompliances = _AlcatelIND1PCAMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PCAMMIBCompliances.setStatus("current")

# Managed Objects groups

alaCoroL3HrePerModeObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 2, 1, 1)
)
alaCoroL3HrePerModeObjects.setObjects(
      *(("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HrePerModeSlotNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HrePerModeSliceNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HrePerModeModeNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreModeHashTableSize"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreModeHashEntriesInUse"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreModeCollEntriesInUse"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreModeCurrentHashFunction"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreMaxCollChainLen"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreAvgCollChainLen"))
)
if mibBuilder.loadTexts:
    alaCoroL3HrePerModeObjects.setStatus("current")

alaCoroL3HrePerCoronadoObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 2, 1, 2)
)
alaCoroL3HrePerCoronadoObjects.setObjects(
      *(("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreSlotNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreSliceNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreRouteCacheEntriesTotal"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreRouteCacheEntriesInUse"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpPacketsReceived"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpBytesReceived"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpPacketsForwarded"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpBytesForwarded"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpPacketsDiscarded"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpBytesDiscarded"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpPacketsFragmented"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpPacketsFragsGenerated"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpPacketsFailedToFrag"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpxPacketsReceived"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpxBytesReceived"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpxPacketsForwarded"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpxBytesForwarded"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpxPacketsDiscarded"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreIpxBytesDiscarded"))
)
if mibBuilder.loadTexts:
    alaCoroL3HrePerCoronadoObjects.setStatus("current")

alaCoroL3HreChangeObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 2, 1, 3)
)
alaCoroL3HreChangeObjects.setObjects(
      *(("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreUpdateChanges"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeSlotNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeSliceNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeModeNumber"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeHashTableSize"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeHashFunction"),
        ("ALCATEL-IND1-PCAM-MIB", "alaCoroL3HreChangeClear"))
)
if mibBuilder.loadTexts:
    alaCoroL3HreChangeObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelInd1PCAMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelInd1PCAMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PCAM-MIB",
    **{"CoroL3HashFunction": CoroL3HashFunction,
       "alcatelIND1PCAMMIB": alcatelIND1PCAMMIB,
       "alcatelIND1PCAMMIBObjects": alcatelIND1PCAMMIBObjects,
       "alaCoroL3HrePerModeTable": alaCoroL3HrePerModeTable,
       "alaCoroL3HrePerModeTableEntry": alaCoroL3HrePerModeTableEntry,
       "alaCoroL3HrePerModeSlotNumber": alaCoroL3HrePerModeSlotNumber,
       "alaCoroL3HrePerModeSliceNumber": alaCoroL3HrePerModeSliceNumber,
       "alaCoroL3HrePerModeModeNumber": alaCoroL3HrePerModeModeNumber,
       "alaCoroL3HreModeHashTableSize": alaCoroL3HreModeHashTableSize,
       "alaCoroL3HreModeHashEntriesInUse": alaCoroL3HreModeHashEntriesInUse,
       "alaCoroL3HreModeCollEntriesInUse": alaCoroL3HreModeCollEntriesInUse,
       "alaCoroL3HreModeCurrentHashFunction": alaCoroL3HreModeCurrentHashFunction,
       "alaCoroL3HreMaxCollChainLen": alaCoroL3HreMaxCollChainLen,
       "alaCoroL3HreAvgCollChainLen": alaCoroL3HreAvgCollChainLen,
       "alaCoroL3HrePerCoronadoStatsTable": alaCoroL3HrePerCoronadoStatsTable,
       "alaCoroL3HrePerCoronadoStatsTableEntry": alaCoroL3HrePerCoronadoStatsTableEntry,
       "alaCoroL3HreSlotNumber": alaCoroL3HreSlotNumber,
       "alaCoroL3HreSliceNumber": alaCoroL3HreSliceNumber,
       "alaCoroL3HreRouteCacheEntriesTotal": alaCoroL3HreRouteCacheEntriesTotal,
       "alaCoroL3HreRouteCacheEntriesInUse": alaCoroL3HreRouteCacheEntriesInUse,
       "alaCoroL3HreIpPacketsReceived": alaCoroL3HreIpPacketsReceived,
       "alaCoroL3HreIpBytesReceived": alaCoroL3HreIpBytesReceived,
       "alaCoroL3HreIpPacketsForwarded": alaCoroL3HreIpPacketsForwarded,
       "alaCoroL3HreIpBytesForwarded": alaCoroL3HreIpBytesForwarded,
       "alaCoroL3HreIpPacketsDiscarded": alaCoroL3HreIpPacketsDiscarded,
       "alaCoroL3HreIpBytesDiscarded": alaCoroL3HreIpBytesDiscarded,
       "alaCoroL3HreIpPacketsFragmented": alaCoroL3HreIpPacketsFragmented,
       "alaCoroL3HreIpPacketsFragsGenerated": alaCoroL3HreIpPacketsFragsGenerated,
       "alaCoroL3HreIpPacketsFailedToFrag": alaCoroL3HreIpPacketsFailedToFrag,
       "alaCoroL3HreIpxPacketsReceived": alaCoroL3HreIpxPacketsReceived,
       "alaCoroL3HreIpxBytesReceived": alaCoroL3HreIpxBytesReceived,
       "alaCoroL3HreIpxPacketsForwarded": alaCoroL3HreIpxPacketsForwarded,
       "alaCoroL3HreIpxBytesForwarded": alaCoroL3HreIpxBytesForwarded,
       "alaCoroL3HreIpxPacketsDiscarded": alaCoroL3HreIpxPacketsDiscarded,
       "alaCoroL3HreIpxBytesDiscarded": alaCoroL3HreIpxBytesDiscarded,
       "alaCoroL3HreUpdateChanges": alaCoroL3HreUpdateChanges,
       "alaCoroL3HreChangeTable": alaCoroL3HreChangeTable,
       "alaCoroL3HreChangeTableEntry": alaCoroL3HreChangeTableEntry,
       "alaCoroL3HreChangeSlotNumber": alaCoroL3HreChangeSlotNumber,
       "alaCoroL3HreChangeSliceNumber": alaCoroL3HreChangeSliceNumber,
       "alaCoroL3HreChangeModeNumber": alaCoroL3HreChangeModeNumber,
       "alaCoroL3HreChangeHashTableSize": alaCoroL3HreChangeHashTableSize,
       "alaCoroL3HreChangeHashFunction": alaCoroL3HreChangeHashFunction,
       "alaCoroL3HreChangeClear": alaCoroL3HreChangeClear,
       "alcatelIND1PCAMMIBConformance": alcatelIND1PCAMMIBConformance,
       "alcatelIND1PCAMMIBGroups": alcatelIND1PCAMMIBGroups,
       "alaCoroL3HrePerModeObjects": alaCoroL3HrePerModeObjects,
       "alaCoroL3HrePerCoronadoObjects": alaCoroL3HrePerCoronadoObjects,
       "alaCoroL3HreChangeObjects": alaCoroL3HreChangeObjects,
       "alcatelIND1PCAMMIBCompliances": alcatelIND1PCAMMIBCompliances,
       "alcatelInd1PCAMMIBCompliance": alcatelInd1PCAMMIBCompliance}
)
