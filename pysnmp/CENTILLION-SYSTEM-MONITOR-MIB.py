# SNMP MIB module (CENTILLION-SYSTEM-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-SYSTEM-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:16 2024
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

(sysMonitor,) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "sysMonitor")

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

_CardMonitorTable_Object = MibTable
cardMonitorTable = _CardMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cardMonitorTable.setStatus("mandatory")
_CardMonEntry_Object = MibTableRow
cardMonEntry = _CardMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1)
)
cardMonEntry.setIndexNames(
    (0, "CENTILLION-SYSTEM-MONITOR-MIB", "cardMonIndex"),
)
if mibBuilder.loadTexts:
    cardMonEntry.setStatus("mandatory")
_CardMonIndex_Type = Integer32
_CardMonIndex_Object = MibTableColumn
cardMonIndex = _CardMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 1),
    _CardMonIndex_Type()
)
cardMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonIndex.setStatus("mandatory")
_CardMonCellsReceived_Type = Counter32
_CardMonCellsReceived_Object = MibTableColumn
cardMonCellsReceived = _CardMonCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 2),
    _CardMonCellsReceived_Type()
)
cardMonCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonCellsReceived.setStatus("mandatory")
_CardMonCellsTransmitted_Type = Counter32
_CardMonCellsTransmitted_Object = MibTableColumn
cardMonCellsTransmitted = _CardMonCellsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 3),
    _CardMonCellsTransmitted_Type()
)
cardMonCellsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonCellsTransmitted.setStatus("mandatory")
_CardMonCellsDropped_Type = Counter32
_CardMonCellsDropped_Object = MibTableColumn
cardMonCellsDropped = _CardMonCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 4),
    _CardMonCellsDropped_Type()
)
cardMonCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonCellsDropped.setStatus("mandatory")
_CardMonSARReceived_Type = Counter32
_CardMonSARReceived_Object = MibTableColumn
cardMonSARReceived = _CardMonSARReceived_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 5),
    _CardMonSARReceived_Type()
)
cardMonSARReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonSARReceived.setStatus("mandatory")
_CardMonSARTransmitted_Type = Counter32
_CardMonSARTransmitted_Object = MibTableColumn
cardMonSARTransmitted = _CardMonSARTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 6),
    _CardMonSARTransmitted_Type()
)
cardMonSARTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonSARTransmitted.setStatus("mandatory")
_CardMonSARDropped_Type = Counter32
_CardMonSARDropped_Object = MibTableColumn
cardMonSARDropped = _CardMonSARDropped_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 7),
    _CardMonSARDropped_Type()
)
cardMonSARDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonSARDropped.setStatus("mandatory")
_CardMonMSIMsgs_Type = Counter32
_CardMonMSIMsgs_Object = MibTableColumn
cardMonMSIMsgs = _CardMonMSIMsgs_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 8),
    _CardMonMSIMsgs_Type()
)
cardMonMSIMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonMSIMsgs.setStatus("mandatory")
_CardMonCardInsertions_Type = Counter32
_CardMonCardInsertions_Object = MibTableColumn
cardMonCardInsertions = _CardMonCardInsertions_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 9),
    _CardMonCardInsertions_Type()
)
cardMonCardInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonCardInsertions.setStatus("mandatory")
_CardMonCardRemovals_Type = Counter32
_CardMonCardRemovals_Object = MibTableColumn
cardMonCardRemovals = _CardMonCardRemovals_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 1, 1, 10),
    _CardMonCardRemovals_Type()
)
cardMonCardRemovals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMonCardRemovals.setStatus("mandatory")
_CpuPctUse_Type = Integer32
_CpuPctUse_Object = MibScalar
cpuPctUse = _CpuPctUse_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 4),
    _CpuPctUse_Type()
)
cpuPctUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPctUse.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-SYSTEM-MONITOR-MIB",
    **{"cardMonitorTable": cardMonitorTable,
       "cardMonEntry": cardMonEntry,
       "cardMonIndex": cardMonIndex,
       "cardMonCellsReceived": cardMonCellsReceived,
       "cardMonCellsTransmitted": cardMonCellsTransmitted,
       "cardMonCellsDropped": cardMonCellsDropped,
       "cardMonSARReceived": cardMonSARReceived,
       "cardMonSARTransmitted": cardMonSARTransmitted,
       "cardMonSARDropped": cardMonSARDropped,
       "cardMonMSIMsgs": cardMonMSIMsgs,
       "cardMonCardInsertions": cardMonCardInsertions,
       "cardMonCardRemovals": cardMonCardRemovals,
       "cpuPctUse": cpuPctUse}
)
