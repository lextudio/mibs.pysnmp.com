# SNMP MIB module (ALTIGA-MULTILINK-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-MULTILINK-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:17 2024
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

(alMultiLinkMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alMultiLinkMibModule")

(alMultiLinkGroup,
 alStatsMultiLink) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alMultiLinkGroup",
    "alStatsMultiLink")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

altigaMultiLinkStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 39, 2)
)
altigaMultiLinkStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaMultiLinkStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaMultiLinkStatsMibConformance = _AltigaMultiLinkStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 39, 2, 1)
)
_AltigaMultiLinkStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaMultiLinkStatsMibCompliances = _AltigaMultiLinkStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 39, 2, 1, 1)
)
_AlStatsMultiLinkGlobal_ObjectIdentity = ObjectIdentity
alStatsMultiLinkGlobal = _AlStatsMultiLinkGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 1)
)
_AlMultiLinkStatsTable_Object = MibTable
alMultiLinkStatsTable = _AlMultiLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2)
)
if mibBuilder.loadTexts:
    alMultiLinkStatsTable.setStatus("current")
_AlMultiLinkStatsEntry_Object = MibTableRow
alMultiLinkStatsEntry = _AlMultiLinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1)
)
alMultiLinkStatsEntry.setIndexNames(
    (0, "ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsIndex"),
)
if mibBuilder.loadTexts:
    alMultiLinkStatsEntry.setStatus("current")
_AlMultiLinkStatsRowStatus_Type = RowStatus
_AlMultiLinkStatsRowStatus_Object = MibTableColumn
alMultiLinkStatsRowStatus = _AlMultiLinkStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 1),
    _AlMultiLinkStatsRowStatus_Type()
)
alMultiLinkStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alMultiLinkStatsRowStatus.setStatus("current")


class _AlMultiLinkStatsIndex_Type(Integer32):
    """Custom type alMultiLinkStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlMultiLinkStatsIndex_Type.__name__ = "Integer32"
_AlMultiLinkStatsIndex_Object = MibTableColumn
alMultiLinkStatsIndex = _AlMultiLinkStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 2),
    _AlMultiLinkStatsIndex_Type()
)
alMultiLinkStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsIndex.setStatus("current")
_AlMultiLinkStatsTxOctets_Type = Unsigned32
_AlMultiLinkStatsTxOctets_Object = MibTableColumn
alMultiLinkStatsTxOctets = _AlMultiLinkStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 3),
    _AlMultiLinkStatsTxOctets_Type()
)
alMultiLinkStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsTxOctets.setStatus("current")
_AlMultiLinkStatsTxPackets_Type = Unsigned32
_AlMultiLinkStatsTxPackets_Object = MibTableColumn
alMultiLinkStatsTxPackets = _AlMultiLinkStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 4),
    _AlMultiLinkStatsTxPackets_Type()
)
alMultiLinkStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsTxPackets.setStatus("current")
_AlMultiLinkStatsTxMlpFragments_Type = Unsigned32
_AlMultiLinkStatsTxMlpFragments_Object = MibTableColumn
alMultiLinkStatsTxMlpFragments = _AlMultiLinkStatsTxMlpFragments_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 5),
    _AlMultiLinkStatsTxMlpFragments_Type()
)
alMultiLinkStatsTxMlpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsTxMlpFragments.setStatus("current")
_AlMultiLinkStatsTxMlpPackets_Type = Unsigned32
_AlMultiLinkStatsTxMlpPackets_Object = MibTableColumn
alMultiLinkStatsTxMlpPackets = _AlMultiLinkStatsTxMlpPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 6),
    _AlMultiLinkStatsTxMlpPackets_Type()
)
alMultiLinkStatsTxMlpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsTxMlpPackets.setStatus("current")
_AlMultiLinkStatsTxNonMlpPackets_Type = Unsigned32
_AlMultiLinkStatsTxNonMlpPackets_Object = MibTableColumn
alMultiLinkStatsTxNonMlpPackets = _AlMultiLinkStatsTxNonMlpPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 7),
    _AlMultiLinkStatsTxNonMlpPackets_Type()
)
alMultiLinkStatsTxNonMlpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsTxNonMlpPackets.setStatus("current")
_AlMultiLinkStatsTxThroughput_Type = Gauge32
_AlMultiLinkStatsTxThroughput_Object = MibTableColumn
alMultiLinkStatsTxThroughput = _AlMultiLinkStatsTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 8),
    _AlMultiLinkStatsTxThroughput_Type()
)
alMultiLinkStatsTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsTxThroughput.setStatus("current")
_AlMultiLinkStatsRxOctets_Type = Unsigned32
_AlMultiLinkStatsRxOctets_Object = MibTableColumn
alMultiLinkStatsRxOctets = _AlMultiLinkStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 9),
    _AlMultiLinkStatsRxOctets_Type()
)
alMultiLinkStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxOctets.setStatus("current")
_AlMultiLinkStatsRxPackets_Type = Unsigned32
_AlMultiLinkStatsRxPackets_Object = MibTableColumn
alMultiLinkStatsRxPackets = _AlMultiLinkStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 10),
    _AlMultiLinkStatsRxPackets_Type()
)
alMultiLinkStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxPackets.setStatus("current")
_AlMultiLinkStatsRxMlpFragments_Type = Unsigned32
_AlMultiLinkStatsRxMlpFragments_Object = MibTableColumn
alMultiLinkStatsRxMlpFragments = _AlMultiLinkStatsRxMlpFragments_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 11),
    _AlMultiLinkStatsRxMlpFragments_Type()
)
alMultiLinkStatsRxMlpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxMlpFragments.setStatus("current")
_AlMultiLinkStatsRxMlpPackets_Type = Unsigned32
_AlMultiLinkStatsRxMlpPackets_Object = MibTableColumn
alMultiLinkStatsRxMlpPackets = _AlMultiLinkStatsRxMlpPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 12),
    _AlMultiLinkStatsRxMlpPackets_Type()
)
alMultiLinkStatsRxMlpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxMlpPackets.setStatus("current")
_AlMultiLinkStatsRxNonMlpPackets_Type = Unsigned32
_AlMultiLinkStatsRxNonMlpPackets_Object = MibTableColumn
alMultiLinkStatsRxNonMlpPackets = _AlMultiLinkStatsRxNonMlpPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 13),
    _AlMultiLinkStatsRxNonMlpPackets_Type()
)
alMultiLinkStatsRxNonMlpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxNonMlpPackets.setStatus("current")
_AlMultiLinkStatsRxThroughput_Type = Gauge32
_AlMultiLinkStatsRxThroughput_Object = MibTableColumn
alMultiLinkStatsRxThroughput = _AlMultiLinkStatsRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 14),
    _AlMultiLinkStatsRxThroughput_Type()
)
alMultiLinkStatsRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxThroughput.setStatus("current")
_AlMultiLinkStatsRxLostEnd_Type = Unsigned32
_AlMultiLinkStatsRxLostEnd_Object = MibTableColumn
alMultiLinkStatsRxLostEnd = _AlMultiLinkStatsRxLostEnd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 15),
    _AlMultiLinkStatsRxLostEnd_Type()
)
alMultiLinkStatsRxLostEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxLostEnd.setStatus("current")
_AlMultiLinkStatsRxStalePackets_Type = Unsigned32
_AlMultiLinkStatsRxStalePackets_Object = MibTableColumn
alMultiLinkStatsRxStalePackets = _AlMultiLinkStatsRxStalePackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 16),
    _AlMultiLinkStatsRxStalePackets_Type()
)
alMultiLinkStatsRxStalePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxStalePackets.setStatus("current")
_AlMultiLinkStatsRxStaleFragments_Type = Unsigned32
_AlMultiLinkStatsRxStaleFragments_Object = MibTableColumn
alMultiLinkStatsRxStaleFragments = _AlMultiLinkStatsRxStaleFragments_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 17),
    _AlMultiLinkStatsRxStaleFragments_Type()
)
alMultiLinkStatsRxStaleFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxStaleFragments.setStatus("current")
_AlMultiLinkStatsRxDroppedFragments_Type = Unsigned32
_AlMultiLinkStatsRxDroppedFragments_Object = MibTableColumn
alMultiLinkStatsRxDroppedFragments = _AlMultiLinkStatsRxDroppedFragments_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 18),
    _AlMultiLinkStatsRxDroppedFragments_Type()
)
alMultiLinkStatsRxDroppedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxDroppedFragments.setStatus("current")
_AlMultiLinkStatsRxOOSFragments_Type = Unsigned32
_AlMultiLinkStatsRxOOSFragments_Object = MibTableColumn
alMultiLinkStatsRxOOSFragments = _AlMultiLinkStatsRxOOSFragments_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 19),
    _AlMultiLinkStatsRxOOSFragments_Type()
)
alMultiLinkStatsRxOOSFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsRxOOSFragments.setStatus("current")
_AlMultiLinkStatsIdleTmrCleanup_Type = Unsigned32
_AlMultiLinkStatsIdleTmrCleanup_Object = MibTableColumn
alMultiLinkStatsIdleTmrCleanup = _AlMultiLinkStatsIdleTmrCleanup_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 34, 2, 1, 20),
    _AlMultiLinkStatsIdleTmrCleanup_Type()
)
alMultiLinkStatsIdleTmrCleanup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMultiLinkStatsIdleTmrCleanup.setStatus("current")

# Managed Objects groups

altigaMultiLinkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 34, 2)
)
altigaMultiLinkStatsGroup.setObjects(
      *(("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRowStatus"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsIndex"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsTxOctets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsTxPackets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsTxMlpFragments"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsTxMlpPackets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsTxNonMlpPackets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsTxThroughput"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxOctets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxPackets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxMlpFragments"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxMlpPackets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxNonMlpPackets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxThroughput"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxLostEnd"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxStalePackets"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxStaleFragments"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxDroppedFragments"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsRxOOSFragments"),
        ("ALTIGA-MULTILINK-STATS-MIB", "alMultiLinkStatsIdleTmrCleanup"))
)
if mibBuilder.loadTexts:
    altigaMultiLinkStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaMultiLinkStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 39, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaMultiLinkStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-MULTILINK-STATS-MIB",
    **{"altigaMultiLinkStatsMibModule": altigaMultiLinkStatsMibModule,
       "altigaMultiLinkStatsMibConformance": altigaMultiLinkStatsMibConformance,
       "altigaMultiLinkStatsMibCompliances": altigaMultiLinkStatsMibCompliances,
       "altigaMultiLinkStatsMibCompliance": altigaMultiLinkStatsMibCompliance,
       "altigaMultiLinkStatsGroup": altigaMultiLinkStatsGroup,
       "alStatsMultiLinkGlobal": alStatsMultiLinkGlobal,
       "alMultiLinkStatsTable": alMultiLinkStatsTable,
       "alMultiLinkStatsEntry": alMultiLinkStatsEntry,
       "alMultiLinkStatsRowStatus": alMultiLinkStatsRowStatus,
       "alMultiLinkStatsIndex": alMultiLinkStatsIndex,
       "alMultiLinkStatsTxOctets": alMultiLinkStatsTxOctets,
       "alMultiLinkStatsTxPackets": alMultiLinkStatsTxPackets,
       "alMultiLinkStatsTxMlpFragments": alMultiLinkStatsTxMlpFragments,
       "alMultiLinkStatsTxMlpPackets": alMultiLinkStatsTxMlpPackets,
       "alMultiLinkStatsTxNonMlpPackets": alMultiLinkStatsTxNonMlpPackets,
       "alMultiLinkStatsTxThroughput": alMultiLinkStatsTxThroughput,
       "alMultiLinkStatsRxOctets": alMultiLinkStatsRxOctets,
       "alMultiLinkStatsRxPackets": alMultiLinkStatsRxPackets,
       "alMultiLinkStatsRxMlpFragments": alMultiLinkStatsRxMlpFragments,
       "alMultiLinkStatsRxMlpPackets": alMultiLinkStatsRxMlpPackets,
       "alMultiLinkStatsRxNonMlpPackets": alMultiLinkStatsRxNonMlpPackets,
       "alMultiLinkStatsRxThroughput": alMultiLinkStatsRxThroughput,
       "alMultiLinkStatsRxLostEnd": alMultiLinkStatsRxLostEnd,
       "alMultiLinkStatsRxStalePackets": alMultiLinkStatsRxStalePackets,
       "alMultiLinkStatsRxStaleFragments": alMultiLinkStatsRxStaleFragments,
       "alMultiLinkStatsRxDroppedFragments": alMultiLinkStatsRxDroppedFragments,
       "alMultiLinkStatsRxOOSFragments": alMultiLinkStatsRxOOSFragments,
       "alMultiLinkStatsIdleTmrCleanup": alMultiLinkStatsIdleTmrCleanup}
)
