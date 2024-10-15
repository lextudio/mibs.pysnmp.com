# SNMP MIB module (CTRON-FDDI-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-FDDI-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:52 2024
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

(ctFDDIStats,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFDDIStats")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtFDDIStatsUtil_ObjectIdentity = ObjectIdentity
ctFDDIStatsUtil = _CtFDDIStatsUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1)
)
_CtFDDIStatsCtlTable_Object = MibTable
ctFDDIStatsCtlTable = _CtFDDIStatsCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ctFDDIStatsCtlTable.setStatus("mandatory")
_CtFDDIStatsCtlEntry_Object = MibTableRow
ctFDDIStatsCtlEntry = _CtFDDIStatsCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1)
)
ctFDDIStatsCtlEntry.setIndexNames(
    (0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"),
    (0, "CTRON-FDDI-STAT-MIB", "ctFDDISMT"),
    (0, "CTRON-FDDI-STAT-MIB", "ctFDDIPath"),
)
if mibBuilder.loadTexts:
    ctFDDIStatsCtlEntry.setStatus("mandatory")
_CtFDDISlot_Type = Integer32
_CtFDDISlot_Object = MibTableColumn
ctFDDISlot = _CtFDDISlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 1),
    _CtFDDISlot_Type()
)
ctFDDISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDISlot.setStatus("mandatory")
_CtFDDISMT_Type = Integer32
_CtFDDISMT_Object = MibTableColumn
ctFDDISMT = _CtFDDISMT_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 2),
    _CtFDDISMT_Type()
)
ctFDDISMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDISMT.setStatus("mandatory")
_CtFDDIPath_Type = Integer32
_CtFDDIPath_Object = MibTableColumn
ctFDDIPath = _CtFDDIPath_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 3),
    _CtFDDIPath_Type()
)
ctFDDIPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIPath.setStatus("mandatory")
_CtFDDINextEntry_Type = Integer32
_CtFDDINextEntry_Object = MibTableColumn
ctFDDINextEntry = _CtFDDINextEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 4),
    _CtFDDINextEntry_Type()
)
ctFDDINextEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDINextEntry.setStatus("mandatory")


class _CtFDDIResetPeak_Type(Integer32):
    """Custom type ctFDDIResetPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_CtFDDIResetPeak_Type.__name__ = "Integer32"
_CtFDDIResetPeak_Object = MibTableColumn
ctFDDIResetPeak = _CtFDDIResetPeak_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 5),
    _CtFDDIResetPeak_Type()
)
ctFDDIResetPeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFDDIResetPeak.setStatus("mandatory")
_CtFDDIStatsHistoryTable_Object = MibTable
ctFDDIStatsHistoryTable = _CtFDDIStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ctFDDIStatsHistoryTable.setStatus("mandatory")
_CtFDDIStatsHistoryEntry_Object = MibTableRow
ctFDDIStatsHistoryEntry = _CtFDDIStatsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1)
)
ctFDDIStatsHistoryEntry.setIndexNames(
    (0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"),
    (0, "CTRON-FDDI-STAT-MIB", "ctFDDIStatsIndex"),
)
if mibBuilder.loadTexts:
    ctFDDIStatsHistoryEntry.setStatus("mandatory")
_CtFDDIStatsIndex_Type = Integer32
_CtFDDIStatsIndex_Object = MibTableColumn
ctFDDIStatsIndex = _CtFDDIStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 1),
    _CtFDDIStatsIndex_Type()
)
ctFDDIStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIStatsIndex.setStatus("mandatory")
_CtFDDIStatsTimeStamp_Type = TimeTicks
_CtFDDIStatsTimeStamp_Object = MibTableColumn
ctFDDIStatsTimeStamp = _CtFDDIStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 2),
    _CtFDDIStatsTimeStamp_Type()
)
ctFDDIStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIStatsTimeStamp.setStatus("mandatory")
_CtFDDIFrames_Type = Integer32
_CtFDDIFrames_Object = MibTableColumn
ctFDDIFrames = _CtFDDIFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 3),
    _CtFDDIFrames_Type()
)
ctFDDIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIFrames.setStatus("mandatory")
_CtFDDIBytes_Type = Integer32
_CtFDDIBytes_Object = MibTableColumn
ctFDDIBytes = _CtFDDIBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 4),
    _CtFDDIBytes_Type()
)
ctFDDIBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIBytes.setStatus("mandatory")
_CtFDDIPeakBytes_Type = Integer32
_CtFDDIPeakBytes_Object = MibTableColumn
ctFDDIPeakBytes = _CtFDDIPeakBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 5),
    _CtFDDIPeakBytes_Type()
)
ctFDDIPeakBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIPeakBytes.setStatus("mandatory")
_CtFDDIPeakTime_Type = Integer32
_CtFDDIPeakTime_Object = MibTableColumn
ctFDDIPeakTime = _CtFDDIPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 6),
    _CtFDDIPeakTime_Type()
)
ctFDDIPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIPeakTime.setStatus("mandatory")
_CtFDDIStatsSMT_Type = Integer32
_CtFDDIStatsSMT_Object = MibTableColumn
ctFDDIStatsSMT = _CtFDDIStatsSMT_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 7),
    _CtFDDIStatsSMT_Type()
)
ctFDDIStatsSMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIStatsSMT.setStatus("mandatory")
_CtFDDIStatsPath_Type = Integer32
_CtFDDIStatsPath_Object = MibTableColumn
ctFDDIStatsPath = _CtFDDIStatsPath_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 8),
    _CtFDDIStatsPath_Type()
)
ctFDDIStatsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFDDIStatsPath.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-FDDI-STAT-MIB",
    **{"ctFDDIStatsUtil": ctFDDIStatsUtil,
       "ctFDDIStatsCtlTable": ctFDDIStatsCtlTable,
       "ctFDDIStatsCtlEntry": ctFDDIStatsCtlEntry,
       "ctFDDISlot": ctFDDISlot,
       "ctFDDISMT": ctFDDISMT,
       "ctFDDIPath": ctFDDIPath,
       "ctFDDINextEntry": ctFDDINextEntry,
       "ctFDDIResetPeak": ctFDDIResetPeak,
       "ctFDDIStatsHistoryTable": ctFDDIStatsHistoryTable,
       "ctFDDIStatsHistoryEntry": ctFDDIStatsHistoryEntry,
       "ctFDDIStatsIndex": ctFDDIStatsIndex,
       "ctFDDIStatsTimeStamp": ctFDDIStatsTimeStamp,
       "ctFDDIFrames": ctFDDIFrames,
       "ctFDDIBytes": ctFDDIBytes,
       "ctFDDIPeakBytes": ctFDDIPeakBytes,
       "ctFDDIPeakTime": ctFDDIPeakTime,
       "ctFDDIStatsSMT": ctFDDIStatsSMT,
       "ctFDDIStatsPath": ctFDDIStatsPath}
)
