# SNMP MIB module (EXTREME-RTSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

extremeRtStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeRtStatsTable_Object = MibTable
extremeRtStatsTable = _ExtremeRtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1)
)
if mibBuilder.loadTexts:
    extremeRtStatsTable.setStatus("current")
_ExtremeRtStatsEntry_Object = MibTableRow
extremeRtStatsEntry = _ExtremeRtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1)
)
extremeRtStatsEntry.setIndexNames(
    (0, "EXTREME-RTSTATS-MIB", "extremeRtStatsIndex"),
)
if mibBuilder.loadTexts:
    extremeRtStatsEntry.setStatus("current")


class _ExtremeRtStatsIndex_Type(Integer32):
    """Custom type extremeRtStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeRtStatsIndex_Type.__name__ = "Integer32"
_ExtremeRtStatsIndex_Object = MibTableColumn
extremeRtStatsIndex = _ExtremeRtStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 1),
    _ExtremeRtStatsIndex_Type()
)
extremeRtStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsIndex.setStatus("current")
_ExtremeRtStatsIntervalStart_Type = TimeTicks
_ExtremeRtStatsIntervalStart_Object = MibTableColumn
extremeRtStatsIntervalStart = _ExtremeRtStatsIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 2),
    _ExtremeRtStatsIntervalStart_Type()
)
extremeRtStatsIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsIntervalStart.setStatus("current")
_ExtremeRtStatsCRCAlignErrors_Type = Counter32
_ExtremeRtStatsCRCAlignErrors_Object = MibTableColumn
extremeRtStatsCRCAlignErrors = _ExtremeRtStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 3),
    _ExtremeRtStatsCRCAlignErrors_Type()
)
extremeRtStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsCRCAlignErrors.setStatus("current")
_ExtremeRtStatsUndersizePkts_Type = Counter32
_ExtremeRtStatsUndersizePkts_Object = MibTableColumn
extremeRtStatsUndersizePkts = _ExtremeRtStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 4),
    _ExtremeRtStatsUndersizePkts_Type()
)
extremeRtStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsUndersizePkts.setStatus("current")
_ExtremeRtStatsOversizePkts_Type = Counter32
_ExtremeRtStatsOversizePkts_Object = MibTableColumn
extremeRtStatsOversizePkts = _ExtremeRtStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 5),
    _ExtremeRtStatsOversizePkts_Type()
)
extremeRtStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsOversizePkts.setStatus("current")
_ExtremeRtStatsFragments_Type = Counter32
_ExtremeRtStatsFragments_Object = MibTableColumn
extremeRtStatsFragments = _ExtremeRtStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 6),
    _ExtremeRtStatsFragments_Type()
)
extremeRtStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsFragments.setStatus("current")
_ExtremeRtStatsJabbers_Type = Counter32
_ExtremeRtStatsJabbers_Object = MibTableColumn
extremeRtStatsJabbers = _ExtremeRtStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 7),
    _ExtremeRtStatsJabbers_Type()
)
extremeRtStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsJabbers.setStatus("current")
_ExtremeRtStatsCollisions_Type = Counter32
_ExtremeRtStatsCollisions_Object = MibTableColumn
extremeRtStatsCollisions = _ExtremeRtStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 8),
    _ExtremeRtStatsCollisions_Type()
)
extremeRtStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsCollisions.setStatus("current")
_ExtremeRtStatsTotalErrors_Type = Counter32
_ExtremeRtStatsTotalErrors_Object = MibTableColumn
extremeRtStatsTotalErrors = _ExtremeRtStatsTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 9),
    _ExtremeRtStatsTotalErrors_Type()
)
extremeRtStatsTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsTotalErrors.setStatus("current")


class _ExtremeRtStatsUtilization_Type(Integer32):
    """Custom type extremeRtStatsUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ExtremeRtStatsUtilization_Type.__name__ = "Integer32"
_ExtremeRtStatsUtilization_Object = MibTableColumn
extremeRtStatsUtilization = _ExtremeRtStatsUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 10),
    _ExtremeRtStatsUtilization_Type()
)
extremeRtStatsUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRtStatsUtilization.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-RTSTATS-MIB",
    **{"extremeRtStats": extremeRtStats,
       "extremeRtStatsTable": extremeRtStatsTable,
       "extremeRtStatsEntry": extremeRtStatsEntry,
       "extremeRtStatsIndex": extremeRtStatsIndex,
       "extremeRtStatsIntervalStart": extremeRtStatsIntervalStart,
       "extremeRtStatsCRCAlignErrors": extremeRtStatsCRCAlignErrors,
       "extremeRtStatsUndersizePkts": extremeRtStatsUndersizePkts,
       "extremeRtStatsOversizePkts": extremeRtStatsOversizePkts,
       "extremeRtStatsFragments": extremeRtStatsFragments,
       "extremeRtStatsJabbers": extremeRtStatsJabbers,
       "extremeRtStatsCollisions": extremeRtStatsCollisions,
       "extremeRtStatsTotalErrors": extremeRtStatsTotalErrors,
       "extremeRtStatsUtilization": extremeRtStatsUtilization}
)
