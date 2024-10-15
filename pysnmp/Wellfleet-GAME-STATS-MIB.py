# SNMP MIB module (Wellfleet-GAME-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-GAME-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:17 2024
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

(wfGameGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfGameGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfKernelTable_Object = MibTable
wfKernelTable = _WfKernelTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    wfKernelTable.setStatus("mandatory")
_WfKernelEntry_Object = MibTableRow
wfKernelEntry = _WfKernelEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1)
)
wfKernelEntry.setIndexNames(
    (0, "Wellfleet-GAME-STATS-MIB", "wfKernelSlot"),
)
if mibBuilder.loadTexts:
    wfKernelEntry.setStatus("mandatory")
_WfKernelSlot_Type = Integer32
_WfKernelSlot_Object = MibTableColumn
wfKernelSlot = _WfKernelSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 1),
    _WfKernelSlot_Type()
)
wfKernelSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelSlot.setStatus("mandatory")
_WfKernelMemorySize_Type = Integer32
_WfKernelMemorySize_Object = MibTableColumn
wfKernelMemorySize = _WfKernelMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 2),
    _WfKernelMemorySize_Type()
)
wfKernelMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemorySize.setStatus("mandatory")
_WfKernelMemoryFree_Type = Integer32
_WfKernelMemoryFree_Object = MibTableColumn
wfKernelMemoryFree = _WfKernelMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 3),
    _WfKernelMemoryFree_Type()
)
wfKernelMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemoryFree.setStatus("mandatory")
_WfKernelMemorySegsTotal_Type = Integer32
_WfKernelMemorySegsTotal_Object = MibTableColumn
wfKernelMemorySegsTotal = _WfKernelMemorySegsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 4),
    _WfKernelMemorySegsTotal_Type()
)
wfKernelMemorySegsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemorySegsTotal.setStatus("mandatory")
_WfKernelMemorySegsFree_Type = Integer32
_WfKernelMemorySegsFree_Object = MibTableColumn
wfKernelMemorySegsFree = _WfKernelMemorySegsFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 5),
    _WfKernelMemorySegsFree_Type()
)
wfKernelMemorySegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemorySegsFree.setStatus("mandatory")
_WfKernelMemoryMaxSegFree_Type = Integer32
_WfKernelMemoryMaxSegFree_Object = MibTableColumn
wfKernelMemoryMaxSegFree = _WfKernelMemoryMaxSegFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 6),
    _WfKernelMemoryMaxSegFree_Type()
)
wfKernelMemoryMaxSegFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemoryMaxSegFree.setStatus("mandatory")
_WfKernelBuffersTotal_Type = Integer32
_WfKernelBuffersTotal_Object = MibTableColumn
wfKernelBuffersTotal = _WfKernelBuffersTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 7),
    _WfKernelBuffersTotal_Type()
)
wfKernelBuffersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBuffersTotal.setStatus("mandatory")
_WfKernelBuffersFree_Type = Integer32
_WfKernelBuffersFree_Object = MibTableColumn
wfKernelBuffersFree = _WfKernelBuffersFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 8),
    _WfKernelBuffersFree_Type()
)
wfKernelBuffersFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBuffersFree.setStatus("mandatory")
_WfKernelTasksTotal_Type = Integer32
_WfKernelTasksTotal_Object = MibTableColumn
wfKernelTasksTotal = _WfKernelTasksTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 9),
    _WfKernelTasksTotal_Type()
)
wfKernelTasksTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTasksTotal.setStatus("mandatory")
_WfKernelTasksInQueue_Type = Integer32
_WfKernelTasksInQueue_Object = MibTableColumn
wfKernelTasksInQueue = _WfKernelTasksInQueue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 10),
    _WfKernelTasksInQueue_Type()
)
wfKernelTasksInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTasksInQueue.setStatus("mandatory")
_WfKernelTimersTotal_Type = Integer32
_WfKernelTimersTotal_Object = MibTableColumn
wfKernelTimersTotal = _WfKernelTimersTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 11),
    _WfKernelTimersTotal_Type()
)
wfKernelTimersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTimersTotal.setStatus("mandatory")
_WfKernelTimersActive_Type = Integer32
_WfKernelTimersActive_Object = MibTableColumn
wfKernelTimersActive = _WfKernelTimersActive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 12),
    _WfKernelTimersActive_Type()
)
wfKernelTimersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelTimersActive.setStatus("mandatory")
_WfKernelBufOwnerTask1_Type = DisplayString
_WfKernelBufOwnerTask1_Object = MibTableColumn
wfKernelBufOwnerTask1 = _WfKernelBufOwnerTask1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 13),
    _WfKernelBufOwnerTask1_Type()
)
wfKernelBufOwnerTask1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask1.setStatus("mandatory")
_WfKernelBufOwnerTask1Bufs_Type = Integer32
_WfKernelBufOwnerTask1Bufs_Object = MibTableColumn
wfKernelBufOwnerTask1Bufs = _WfKernelBufOwnerTask1Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 14),
    _WfKernelBufOwnerTask1Bufs_Type()
)
wfKernelBufOwnerTask1Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask1Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask2_Type = DisplayString
_WfKernelBufOwnerTask2_Object = MibTableColumn
wfKernelBufOwnerTask2 = _WfKernelBufOwnerTask2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 15),
    _WfKernelBufOwnerTask2_Type()
)
wfKernelBufOwnerTask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask2.setStatus("mandatory")
_WfKernelBufOwnerTask2Bufs_Type = Integer32
_WfKernelBufOwnerTask2Bufs_Object = MibTableColumn
wfKernelBufOwnerTask2Bufs = _WfKernelBufOwnerTask2Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 16),
    _WfKernelBufOwnerTask2Bufs_Type()
)
wfKernelBufOwnerTask2Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask2Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask3_Type = DisplayString
_WfKernelBufOwnerTask3_Object = MibTableColumn
wfKernelBufOwnerTask3 = _WfKernelBufOwnerTask3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 17),
    _WfKernelBufOwnerTask3_Type()
)
wfKernelBufOwnerTask3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask3.setStatus("mandatory")
_WfKernelBufOwnerTask3Bufs_Type = Integer32
_WfKernelBufOwnerTask3Bufs_Object = MibTableColumn
wfKernelBufOwnerTask3Bufs = _WfKernelBufOwnerTask3Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 18),
    _WfKernelBufOwnerTask3Bufs_Type()
)
wfKernelBufOwnerTask3Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask3Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask4_Type = DisplayString
_WfKernelBufOwnerTask4_Object = MibTableColumn
wfKernelBufOwnerTask4 = _WfKernelBufOwnerTask4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 19),
    _WfKernelBufOwnerTask4_Type()
)
wfKernelBufOwnerTask4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask4.setStatus("mandatory")
_WfKernelBufOwnerTask4Bufs_Type = Integer32
_WfKernelBufOwnerTask4Bufs_Object = MibTableColumn
wfKernelBufOwnerTask4Bufs = _WfKernelBufOwnerTask4Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 20),
    _WfKernelBufOwnerTask4Bufs_Type()
)
wfKernelBufOwnerTask4Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask4Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask5_Type = DisplayString
_WfKernelBufOwnerTask5_Object = MibTableColumn
wfKernelBufOwnerTask5 = _WfKernelBufOwnerTask5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 21),
    _WfKernelBufOwnerTask5_Type()
)
wfKernelBufOwnerTask5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask5.setStatus("mandatory")
_WfKernelBufOwnerTask5Bufs_Type = Integer32
_WfKernelBufOwnerTask5Bufs_Object = MibTableColumn
wfKernelBufOwnerTask5Bufs = _WfKernelBufOwnerTask5Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 22),
    _WfKernelBufOwnerTask5Bufs_Type()
)
wfKernelBufOwnerTask5Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask5Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask6_Type = DisplayString
_WfKernelBufOwnerTask6_Object = MibTableColumn
wfKernelBufOwnerTask6 = _WfKernelBufOwnerTask6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 23),
    _WfKernelBufOwnerTask6_Type()
)
wfKernelBufOwnerTask6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask6.setStatus("mandatory")
_WfKernelBufOwnerTask6Bufs_Type = Integer32
_WfKernelBufOwnerTask6Bufs_Object = MibTableColumn
wfKernelBufOwnerTask6Bufs = _WfKernelBufOwnerTask6Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 24),
    _WfKernelBufOwnerTask6Bufs_Type()
)
wfKernelBufOwnerTask6Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask6Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask7_Type = DisplayString
_WfKernelBufOwnerTask7_Object = MibTableColumn
wfKernelBufOwnerTask7 = _WfKernelBufOwnerTask7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 25),
    _WfKernelBufOwnerTask7_Type()
)
wfKernelBufOwnerTask7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask7.setStatus("mandatory")
_WfKernelBufOwnerTask7Bufs_Type = Integer32
_WfKernelBufOwnerTask7Bufs_Object = MibTableColumn
wfKernelBufOwnerTask7Bufs = _WfKernelBufOwnerTask7Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 26),
    _WfKernelBufOwnerTask7Bufs_Type()
)
wfKernelBufOwnerTask7Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask7Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask8_Type = DisplayString
_WfKernelBufOwnerTask8_Object = MibTableColumn
wfKernelBufOwnerTask8 = _WfKernelBufOwnerTask8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 27),
    _WfKernelBufOwnerTask8_Type()
)
wfKernelBufOwnerTask8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask8.setStatus("mandatory")
_WfKernelBufOwnerTask8Bufs_Type = Integer32
_WfKernelBufOwnerTask8Bufs_Object = MibTableColumn
wfKernelBufOwnerTask8Bufs = _WfKernelBufOwnerTask8Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 28),
    _WfKernelBufOwnerTask8Bufs_Type()
)
wfKernelBufOwnerTask8Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask8Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask9_Type = DisplayString
_WfKernelBufOwnerTask9_Object = MibTableColumn
wfKernelBufOwnerTask9 = _WfKernelBufOwnerTask9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 29),
    _WfKernelBufOwnerTask9_Type()
)
wfKernelBufOwnerTask9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask9.setStatus("mandatory")
_WfKernelBufOwnerTask9Bufs_Type = Integer32
_WfKernelBufOwnerTask9Bufs_Object = MibTableColumn
wfKernelBufOwnerTask9Bufs = _WfKernelBufOwnerTask9Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 30),
    _WfKernelBufOwnerTask9Bufs_Type()
)
wfKernelBufOwnerTask9Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask9Bufs.setStatus("mandatory")
_WfKernelBufOwnerTask10_Type = DisplayString
_WfKernelBufOwnerTask10_Object = MibTableColumn
wfKernelBufOwnerTask10 = _WfKernelBufOwnerTask10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 31),
    _WfKernelBufOwnerTask10_Type()
)
wfKernelBufOwnerTask10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask10.setStatus("mandatory")
_WfKernelBufOwnerTask10Bufs_Type = Integer32
_WfKernelBufOwnerTask10Bufs_Object = MibTableColumn
wfKernelBufOwnerTask10Bufs = _WfKernelBufOwnerTask10Bufs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 32),
    _WfKernelBufOwnerTask10Bufs_Type()
)
wfKernelBufOwnerTask10Bufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBufOwnerTask10Bufs.setStatus("mandatory")
_WfKernelMemOwnerTask1_Type = DisplayString
_WfKernelMemOwnerTask1_Object = MibTableColumn
wfKernelMemOwnerTask1 = _WfKernelMemOwnerTask1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 33),
    _WfKernelMemOwnerTask1_Type()
)
wfKernelMemOwnerTask1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask1.setStatus("mandatory")
_WfKernelMemOwnerTask1Size_Type = Integer32
_WfKernelMemOwnerTask1Size_Object = MibTableColumn
wfKernelMemOwnerTask1Size = _WfKernelMemOwnerTask1Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 34),
    _WfKernelMemOwnerTask1Size_Type()
)
wfKernelMemOwnerTask1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask1Size.setStatus("mandatory")
_WfKernelMemOwnerTask2_Type = DisplayString
_WfKernelMemOwnerTask2_Object = MibTableColumn
wfKernelMemOwnerTask2 = _WfKernelMemOwnerTask2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 35),
    _WfKernelMemOwnerTask2_Type()
)
wfKernelMemOwnerTask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask2.setStatus("mandatory")
_WfKernelMemOwnerTask2Size_Type = Integer32
_WfKernelMemOwnerTask2Size_Object = MibTableColumn
wfKernelMemOwnerTask2Size = _WfKernelMemOwnerTask2Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 36),
    _WfKernelMemOwnerTask2Size_Type()
)
wfKernelMemOwnerTask2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask2Size.setStatus("mandatory")
_WfKernelMemOwnerTask3_Type = DisplayString
_WfKernelMemOwnerTask3_Object = MibTableColumn
wfKernelMemOwnerTask3 = _WfKernelMemOwnerTask3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 37),
    _WfKernelMemOwnerTask3_Type()
)
wfKernelMemOwnerTask3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask3.setStatus("mandatory")
_WfKernelMemOwnerTask3Size_Type = Integer32
_WfKernelMemOwnerTask3Size_Object = MibTableColumn
wfKernelMemOwnerTask3Size = _WfKernelMemOwnerTask3Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 38),
    _WfKernelMemOwnerTask3Size_Type()
)
wfKernelMemOwnerTask3Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask3Size.setStatus("mandatory")
_WfKernelMemOwnerTask4_Type = DisplayString
_WfKernelMemOwnerTask4_Object = MibTableColumn
wfKernelMemOwnerTask4 = _WfKernelMemOwnerTask4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 39),
    _WfKernelMemOwnerTask4_Type()
)
wfKernelMemOwnerTask4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask4.setStatus("mandatory")
_WfKernelMemOwnerTask4Size_Type = Integer32
_WfKernelMemOwnerTask4Size_Object = MibTableColumn
wfKernelMemOwnerTask4Size = _WfKernelMemOwnerTask4Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 40),
    _WfKernelMemOwnerTask4Size_Type()
)
wfKernelMemOwnerTask4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask4Size.setStatus("mandatory")
_WfKernelMemOwnerTask5_Type = DisplayString
_WfKernelMemOwnerTask5_Object = MibTableColumn
wfKernelMemOwnerTask5 = _WfKernelMemOwnerTask5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 41),
    _WfKernelMemOwnerTask5_Type()
)
wfKernelMemOwnerTask5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask5.setStatus("mandatory")
_WfKernelMemOwnerTask5Size_Type = Integer32
_WfKernelMemOwnerTask5Size_Object = MibTableColumn
wfKernelMemOwnerTask5Size = _WfKernelMemOwnerTask5Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 42),
    _WfKernelMemOwnerTask5Size_Type()
)
wfKernelMemOwnerTask5Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask5Size.setStatus("mandatory")
_WfKernelMemOwnerTask6_Type = DisplayString
_WfKernelMemOwnerTask6_Object = MibTableColumn
wfKernelMemOwnerTask6 = _WfKernelMemOwnerTask6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 43),
    _WfKernelMemOwnerTask6_Type()
)
wfKernelMemOwnerTask6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask6.setStatus("mandatory")
_WfKernelMemOwnerTask6Size_Type = Integer32
_WfKernelMemOwnerTask6Size_Object = MibTableColumn
wfKernelMemOwnerTask6Size = _WfKernelMemOwnerTask6Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 44),
    _WfKernelMemOwnerTask6Size_Type()
)
wfKernelMemOwnerTask6Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask6Size.setStatus("mandatory")
_WfKernelMemOwnerTask7_Type = DisplayString
_WfKernelMemOwnerTask7_Object = MibTableColumn
wfKernelMemOwnerTask7 = _WfKernelMemOwnerTask7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 45),
    _WfKernelMemOwnerTask7_Type()
)
wfKernelMemOwnerTask7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask7.setStatus("mandatory")
_WfKernelMemOwnerTask7Size_Type = Integer32
_WfKernelMemOwnerTask7Size_Object = MibTableColumn
wfKernelMemOwnerTask7Size = _WfKernelMemOwnerTask7Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 46),
    _WfKernelMemOwnerTask7Size_Type()
)
wfKernelMemOwnerTask7Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask7Size.setStatus("mandatory")
_WfKernelMemOwnerTask8_Type = DisplayString
_WfKernelMemOwnerTask8_Object = MibTableColumn
wfKernelMemOwnerTask8 = _WfKernelMemOwnerTask8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 47),
    _WfKernelMemOwnerTask8_Type()
)
wfKernelMemOwnerTask8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask8.setStatus("mandatory")
_WfKernelMemOwnerTask8Size_Type = Integer32
_WfKernelMemOwnerTask8Size_Object = MibTableColumn
wfKernelMemOwnerTask8Size = _WfKernelMemOwnerTask8Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 48),
    _WfKernelMemOwnerTask8Size_Type()
)
wfKernelMemOwnerTask8Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask8Size.setStatus("mandatory")
_WfKernelMemOwnerTask9_Type = DisplayString
_WfKernelMemOwnerTask9_Object = MibTableColumn
wfKernelMemOwnerTask9 = _WfKernelMemOwnerTask9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 49),
    _WfKernelMemOwnerTask9_Type()
)
wfKernelMemOwnerTask9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask9.setStatus("mandatory")
_WfKernelMemOwnerTask9Size_Type = Integer32
_WfKernelMemOwnerTask9Size_Object = MibTableColumn
wfKernelMemOwnerTask9Size = _WfKernelMemOwnerTask9Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 50),
    _WfKernelMemOwnerTask9Size_Type()
)
wfKernelMemOwnerTask9Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask9Size.setStatus("mandatory")
_WfKernelMemOwnerTask10_Type = DisplayString
_WfKernelMemOwnerTask10_Object = MibTableColumn
wfKernelMemOwnerTask10 = _WfKernelMemOwnerTask10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 51),
    _WfKernelMemOwnerTask10_Type()
)
wfKernelMemOwnerTask10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask10.setStatus("mandatory")
_WfKernelMemOwnerTask10Size_Type = Integer32
_WfKernelMemOwnerTask10Size_Object = MibTableColumn
wfKernelMemOwnerTask10Size = _WfKernelMemOwnerTask10Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 52),
    _WfKernelMemOwnerTask10Size_Type()
)
wfKernelMemOwnerTask10Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemOwnerTask10Size.setStatus("mandatory")
_WfKernelAliasBuffsDropped_Type = Integer32
_WfKernelAliasBuffsDropped_Object = MibTableColumn
wfKernelAliasBuffsDropped = _WfKernelAliasBuffsDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 53),
    _WfKernelAliasBuffsDropped_Type()
)
wfKernelAliasBuffsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelAliasBuffsDropped.setStatus("mandatory")
_WfKernelBallocFail_Type = Integer32
_WfKernelBallocFail_Object = MibTableColumn
wfKernelBallocFail = _WfKernelBallocFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 54),
    _WfKernelBallocFail_Type()
)
wfKernelBallocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelBallocFail.setStatus("mandatory")
_WfKernelReplenEmpty_Type = Integer32
_WfKernelReplenEmpty_Object = MibTableColumn
wfKernelReplenEmpty = _WfKernelReplenEmpty_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 55),
    _WfKernelReplenEmpty_Type()
)
wfKernelReplenEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelReplenEmpty.setStatus("mandatory")
_WfKernelMemoryFreeLow_Type = Integer32
_WfKernelMemoryFreeLow_Object = MibTableColumn
wfKernelMemoryFreeLow = _WfKernelMemoryFreeLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 56),
    _WfKernelMemoryFreeLow_Type()
)
wfKernelMemoryFreeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelMemoryFreeLow.setStatus("mandatory")
_WfKernelAliasNoMembers_Type = Integer32
_WfKernelAliasNoMembers_Object = MibTableColumn
wfKernelAliasNoMembers = _WfKernelAliasNoMembers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 1, 1, 57),
    _WfKernelAliasNoMembers_Type()
)
wfKernelAliasNoMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelAliasNoMembers.setStatus("mandatory")
_WfKernParamTable_Object = MibTable
wfKernParamTable = _WfKernParamTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    wfKernParamTable.setStatus("mandatory")
_WfKernParamEntry_Object = MibTableRow
wfKernParamEntry = _WfKernParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1)
)
wfKernParamEntry.setIndexNames(
    (0, "Wellfleet-GAME-STATS-MIB", "wfKernParamSlot"),
)
if mibBuilder.loadTexts:
    wfKernParamEntry.setStatus("mandatory")
_WfKernParamSlot_Type = Integer32
_WfKernParamSlot_Object = MibTableColumn
wfKernParamSlot = _WfKernParamSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 1),
    _WfKernParamSlot_Type()
)
wfKernParamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernParamSlot.setStatus("mandatory")
_WfKernParamTotMem_Type = Integer32
_WfKernParamTotMem_Object = MibTableColumn
wfKernParamTotMem = _WfKernParamTotMem_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 2),
    _WfKernParamTotMem_Type()
)
wfKernParamTotMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernParamTotMem.setStatus("mandatory")
_WfKernParamLocMem_Type = Integer32
_WfKernParamLocMem_Object = MibTableColumn
wfKernParamLocMem = _WfKernParamLocMem_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 3),
    _WfKernParamLocMem_Type()
)
wfKernParamLocMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernParamLocMem.setStatus("mandatory")
_WfKernParamGlobMem_Type = Integer32
_WfKernParamGlobMem_Object = MibTableColumn
wfKernParamGlobMem = _WfKernParamGlobMem_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 2, 1, 4),
    _WfKernParamGlobMem_Type()
)
wfKernParamGlobMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernParamGlobMem.setStatus("mandatory")
_WfKernCfgParamTable_Object = MibTable
wfKernCfgParamTable = _WfKernCfgParamTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    wfKernCfgParamTable.setStatus("mandatory")
_WfKernCfgParamEntry_Object = MibTableRow
wfKernCfgParamEntry = _WfKernCfgParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1)
)
wfKernCfgParamEntry.setIndexNames(
    (0, "Wellfleet-GAME-STATS-MIB", "wfKernCfgParamSlot"),
)
if mibBuilder.loadTexts:
    wfKernCfgParamEntry.setStatus("mandatory")


class _WfKernCfgParamDelete_Type(Integer32):
    """Custom type wfKernCfgParamDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfKernCfgParamDelete_Type.__name__ = "Integer32"
_WfKernCfgParamDelete_Object = MibTableColumn
wfKernCfgParamDelete = _WfKernCfgParamDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 1),
    _WfKernCfgParamDelete_Type()
)
wfKernCfgParamDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfKernCfgParamDelete.setStatus("mandatory")
_WfKernCfgParamSlot_Type = Integer32
_WfKernCfgParamSlot_Object = MibTableColumn
wfKernCfgParamSlot = _WfKernCfgParamSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 2),
    _WfKernCfgParamSlot_Type()
)
wfKernCfgParamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernCfgParamSlot.setStatus("mandatory")
_WfKernCfgParamStatus_Type = Integer32
_WfKernCfgParamStatus_Object = MibTableColumn
wfKernCfgParamStatus = _WfKernCfgParamStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 3),
    _WfKernCfgParamStatus_Type()
)
wfKernCfgParamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernCfgParamStatus.setStatus("mandatory")
_WfKernCfgParamLocMem_Type = Integer32
_WfKernCfgParamLocMem_Object = MibTableColumn
wfKernCfgParamLocMem = _WfKernCfgParamLocMem_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 4),
    _WfKernCfgParamLocMem_Type()
)
wfKernCfgParamLocMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernCfgParamLocMem.setStatus("mandatory")
_WfKernCfgParamGlobMem_Type = Integer32
_WfKernCfgParamGlobMem_Object = MibTableColumn
wfKernCfgParamGlobMem = _WfKernCfgParamGlobMem_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 5),
    _WfKernCfgParamGlobMem_Type()
)
wfKernCfgParamGlobMem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfKernCfgParamGlobMem.setStatus("mandatory")


class _WfKernCfgParamGlobMemReset_Type(Integer32):
    """Custom type wfKernCfgParamGlobMemReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfKernCfgParamGlobMemReset_Type.__name__ = "Integer32"
_WfKernCfgParamGlobMemReset_Object = MibTableColumn
wfKernCfgParamGlobMemReset = _WfKernCfgParamGlobMemReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 6),
    _WfKernCfgParamGlobMemReset_Type()
)
wfKernCfgParamGlobMemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfKernCfgParamGlobMemReset.setStatus("mandatory")
_WfKernCfgParamBufSize_Type = Integer32
_WfKernCfgParamBufSize_Object = MibTableColumn
wfKernCfgParamBufSize = _WfKernCfgParamBufSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 7),
    _WfKernCfgParamBufSize_Type()
)
wfKernCfgParamBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfKernCfgParamBufSize.setStatus("mandatory")


class _WfKernCfgParamBufSizeReset_Type(Integer32):
    """Custom type wfKernCfgParamBufSizeReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfKernCfgParamBufSizeReset_Type.__name__ = "Integer32"
_WfKernCfgParamBufSizeReset_Object = MibTableColumn
wfKernCfgParamBufSizeReset = _WfKernCfgParamBufSizeReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 3, 1, 8),
    _WfKernCfgParamBufSizeReset_Type()
)
wfKernCfgParamBufSizeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfKernCfgParamBufSizeReset.setStatus("mandatory")
_WfKernelSysCfgTable_Object = MibTable
wfKernelSysCfgTable = _WfKernelSysCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5)
)
if mibBuilder.loadTexts:
    wfKernelSysCfgTable.setStatus("mandatory")
_WfKernelSysCfgEntry_Object = MibTableRow
wfKernelSysCfgEntry = _WfKernelSysCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1)
)
wfKernelSysCfgEntry.setIndexNames(
    (0, "Wellfleet-GAME-STATS-MIB", "wfKernelSysCfgSlot"),
)
if mibBuilder.loadTexts:
    wfKernelSysCfgEntry.setStatus("mandatory")


class _WfKernelSysCfgDelete_Type(Integer32):
    """Custom type wfKernelSysCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfKernelSysCfgDelete_Type.__name__ = "Integer32"
_WfKernelSysCfgDelete_Object = MibTableColumn
wfKernelSysCfgDelete = _WfKernelSysCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1, 1),
    _WfKernelSysCfgDelete_Type()
)
wfKernelSysCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfKernelSysCfgDelete.setStatus("mandatory")
_WfKernelSysCfgSlot_Type = Integer32
_WfKernelSysCfgSlot_Object = MibTableColumn
wfKernelSysCfgSlot = _WfKernelSysCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1, 2),
    _WfKernelSysCfgSlot_Type()
)
wfKernelSysCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfKernelSysCfgSlot.setStatus("mandatory")


class _WfKernelSysCfgLogging_Type(Integer32):
    """Custom type wfKernelSysCfgLogging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfKernelSysCfgLogging_Type.__name__ = "Integer32"
_WfKernelSysCfgLogging_Object = MibTableColumn
wfKernelSysCfgLogging = _WfKernelSysCfgLogging_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 5, 1, 3),
    _WfKernelSysCfgLogging_Type()
)
wfKernelSysCfgLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfKernelSysCfgLogging.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-GAME-STATS-MIB",
    **{"wfKernelTable": wfKernelTable,
       "wfKernelEntry": wfKernelEntry,
       "wfKernelSlot": wfKernelSlot,
       "wfKernelMemorySize": wfKernelMemorySize,
       "wfKernelMemoryFree": wfKernelMemoryFree,
       "wfKernelMemorySegsTotal": wfKernelMemorySegsTotal,
       "wfKernelMemorySegsFree": wfKernelMemorySegsFree,
       "wfKernelMemoryMaxSegFree": wfKernelMemoryMaxSegFree,
       "wfKernelBuffersTotal": wfKernelBuffersTotal,
       "wfKernelBuffersFree": wfKernelBuffersFree,
       "wfKernelTasksTotal": wfKernelTasksTotal,
       "wfKernelTasksInQueue": wfKernelTasksInQueue,
       "wfKernelTimersTotal": wfKernelTimersTotal,
       "wfKernelTimersActive": wfKernelTimersActive,
       "wfKernelBufOwnerTask1": wfKernelBufOwnerTask1,
       "wfKernelBufOwnerTask1Bufs": wfKernelBufOwnerTask1Bufs,
       "wfKernelBufOwnerTask2": wfKernelBufOwnerTask2,
       "wfKernelBufOwnerTask2Bufs": wfKernelBufOwnerTask2Bufs,
       "wfKernelBufOwnerTask3": wfKernelBufOwnerTask3,
       "wfKernelBufOwnerTask3Bufs": wfKernelBufOwnerTask3Bufs,
       "wfKernelBufOwnerTask4": wfKernelBufOwnerTask4,
       "wfKernelBufOwnerTask4Bufs": wfKernelBufOwnerTask4Bufs,
       "wfKernelBufOwnerTask5": wfKernelBufOwnerTask5,
       "wfKernelBufOwnerTask5Bufs": wfKernelBufOwnerTask5Bufs,
       "wfKernelBufOwnerTask6": wfKernelBufOwnerTask6,
       "wfKernelBufOwnerTask6Bufs": wfKernelBufOwnerTask6Bufs,
       "wfKernelBufOwnerTask7": wfKernelBufOwnerTask7,
       "wfKernelBufOwnerTask7Bufs": wfKernelBufOwnerTask7Bufs,
       "wfKernelBufOwnerTask8": wfKernelBufOwnerTask8,
       "wfKernelBufOwnerTask8Bufs": wfKernelBufOwnerTask8Bufs,
       "wfKernelBufOwnerTask9": wfKernelBufOwnerTask9,
       "wfKernelBufOwnerTask9Bufs": wfKernelBufOwnerTask9Bufs,
       "wfKernelBufOwnerTask10": wfKernelBufOwnerTask10,
       "wfKernelBufOwnerTask10Bufs": wfKernelBufOwnerTask10Bufs,
       "wfKernelMemOwnerTask1": wfKernelMemOwnerTask1,
       "wfKernelMemOwnerTask1Size": wfKernelMemOwnerTask1Size,
       "wfKernelMemOwnerTask2": wfKernelMemOwnerTask2,
       "wfKernelMemOwnerTask2Size": wfKernelMemOwnerTask2Size,
       "wfKernelMemOwnerTask3": wfKernelMemOwnerTask3,
       "wfKernelMemOwnerTask3Size": wfKernelMemOwnerTask3Size,
       "wfKernelMemOwnerTask4": wfKernelMemOwnerTask4,
       "wfKernelMemOwnerTask4Size": wfKernelMemOwnerTask4Size,
       "wfKernelMemOwnerTask5": wfKernelMemOwnerTask5,
       "wfKernelMemOwnerTask5Size": wfKernelMemOwnerTask5Size,
       "wfKernelMemOwnerTask6": wfKernelMemOwnerTask6,
       "wfKernelMemOwnerTask6Size": wfKernelMemOwnerTask6Size,
       "wfKernelMemOwnerTask7": wfKernelMemOwnerTask7,
       "wfKernelMemOwnerTask7Size": wfKernelMemOwnerTask7Size,
       "wfKernelMemOwnerTask8": wfKernelMemOwnerTask8,
       "wfKernelMemOwnerTask8Size": wfKernelMemOwnerTask8Size,
       "wfKernelMemOwnerTask9": wfKernelMemOwnerTask9,
       "wfKernelMemOwnerTask9Size": wfKernelMemOwnerTask9Size,
       "wfKernelMemOwnerTask10": wfKernelMemOwnerTask10,
       "wfKernelMemOwnerTask10Size": wfKernelMemOwnerTask10Size,
       "wfKernelAliasBuffsDropped": wfKernelAliasBuffsDropped,
       "wfKernelBallocFail": wfKernelBallocFail,
       "wfKernelReplenEmpty": wfKernelReplenEmpty,
       "wfKernelMemoryFreeLow": wfKernelMemoryFreeLow,
       "wfKernelAliasNoMembers": wfKernelAliasNoMembers,
       "wfKernParamTable": wfKernParamTable,
       "wfKernParamEntry": wfKernParamEntry,
       "wfKernParamSlot": wfKernParamSlot,
       "wfKernParamTotMem": wfKernParamTotMem,
       "wfKernParamLocMem": wfKernParamLocMem,
       "wfKernParamGlobMem": wfKernParamGlobMem,
       "wfKernCfgParamTable": wfKernCfgParamTable,
       "wfKernCfgParamEntry": wfKernCfgParamEntry,
       "wfKernCfgParamDelete": wfKernCfgParamDelete,
       "wfKernCfgParamSlot": wfKernCfgParamSlot,
       "wfKernCfgParamStatus": wfKernCfgParamStatus,
       "wfKernCfgParamLocMem": wfKernCfgParamLocMem,
       "wfKernCfgParamGlobMem": wfKernCfgParamGlobMem,
       "wfKernCfgParamGlobMemReset": wfKernCfgParamGlobMemReset,
       "wfKernCfgParamBufSize": wfKernCfgParamBufSize,
       "wfKernCfgParamBufSizeReset": wfKernCfgParamBufSizeReset,
       "wfKernelSysCfgTable": wfKernelSysCfgTable,
       "wfKernelSysCfgEntry": wfKernelSysCfgEntry,
       "wfKernelSysCfgDelete": wfKernelSysCfgDelete,
       "wfKernelSysCfgSlot": wfKernelSysCfgSlot,
       "wfKernelSysCfgLogging": wfKernelSysCfgLogging}
)
