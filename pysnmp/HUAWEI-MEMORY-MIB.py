# SNMP MIB module (HUAWEI-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MEMORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:54 2024
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

(hwFrameIndex,
 hwSlotIndex) = mibBuilder.importSymbols(
    "HUAWEI-DEVICE-MIB",
    "hwFrameIndex",
    "hwSlotIndex")

(hwDev,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDev")

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

hwMemoryDev = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMemoryDevTable_Object = MibTable
hwMemoryDevTable = _HwMemoryDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1)
)
if mibBuilder.loadTexts:
    hwMemoryDevTable.setStatus("current")
_HwMemoryDevEntry_Object = MibTableRow
hwMemoryDevEntry = _HwMemoryDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1)
)
hwMemoryDevEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-MEMORY-MIB", "hwMemoryDevModuleIndex"),
)
if mibBuilder.loadTexts:
    hwMemoryDevEntry.setStatus("current")


class _HwMemoryDevModuleIndex_Type(Integer32):
    """Custom type hwMemoryDevModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMemoryDevModuleIndex_Type.__name__ = "Integer32"
_HwMemoryDevModuleIndex_Object = MibTableColumn
hwMemoryDevModuleIndex = _HwMemoryDevModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 1),
    _HwMemoryDevModuleIndex_Type()
)
hwMemoryDevModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMemoryDevModuleIndex.setStatus("current")
_HwMemoryDevSize_Type = Unsigned32
_HwMemoryDevSize_Object = MibTableColumn
hwMemoryDevSize = _HwMemoryDevSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 2),
    _HwMemoryDevSize_Type()
)
hwMemoryDevSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevSize.setStatus("current")
_HwMemoryDevFree_Type = Unsigned32
_HwMemoryDevFree_Object = MibTableColumn
hwMemoryDevFree = _HwMemoryDevFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 3),
    _HwMemoryDevFree_Type()
)
hwMemoryDevFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevFree.setStatus("current")
_HwMemoryDevRawSliceUsed_Type = Unsigned32
_HwMemoryDevRawSliceUsed_Object = MibTableColumn
hwMemoryDevRawSliceUsed = _HwMemoryDevRawSliceUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 4),
    _HwMemoryDevRawSliceUsed_Type()
)
hwMemoryDevRawSliceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevRawSliceUsed.setStatus("current")
_HwMemoryDevLargestFree_Type = Unsigned32
_HwMemoryDevLargestFree_Object = MibTableColumn
hwMemoryDevLargestFree = _HwMemoryDevLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 5),
    _HwMemoryDevLargestFree_Type()
)
hwMemoryDevLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevLargestFree.setStatus("current")
_HwMemoryDevFail_Type = Integer32
_HwMemoryDevFail_Object = MibTableColumn
hwMemoryDevFail = _HwMemoryDevFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 6),
    _HwMemoryDevFail_Type()
)
hwMemoryDevFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevFail.setStatus("current")
_HwMemoryDevFailNoMem_Type = Integer32
_HwMemoryDevFailNoMem_Object = MibTableColumn
hwMemoryDevFailNoMem = _HwMemoryDevFailNoMem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 7),
    _HwMemoryDevFailNoMem_Type()
)
hwMemoryDevFailNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevFailNoMem.setStatus("current")
_HwBufferTable_Object = MibTable
hwBufferTable = _HwBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2)
)
if mibBuilder.loadTexts:
    hwBufferTable.setStatus("current")
_HwBufferEntry_Object = MibTableRow
hwBufferEntry = _HwBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1)
)
hwBufferEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-MEMORY-MIB", "hwBufferModuleIndex"),
    (0, "HUAWEI-MEMORY-MIB", "hwBufferSize"),
)
if mibBuilder.loadTexts:
    hwBufferEntry.setStatus("current")


class _HwBufferModuleIndex_Type(Integer32):
    """Custom type hwBufferModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwBufferModuleIndex_Type.__name__ = "Integer32"
_HwBufferModuleIndex_Object = MibTableColumn
hwBufferModuleIndex = _HwBufferModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 1),
    _HwBufferModuleIndex_Type()
)
hwBufferModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBufferModuleIndex.setStatus("current")


class _HwBufferSize_Type(Integer32):
    """Custom type hwBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBufferSize_Type.__name__ = "Integer32"
_HwBufferSize_Object = MibTableColumn
hwBufferSize = _HwBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 2),
    _HwBufferSize_Type()
)
hwBufferSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBufferSize.setStatus("current")
_HwBufferCurrentTotal_Type = Integer32
_HwBufferCurrentTotal_Object = MibTableColumn
hwBufferCurrentTotal = _HwBufferCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 3),
    _HwBufferCurrentTotal_Type()
)
hwBufferCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBufferCurrentTotal.setStatus("current")
_HwBufferCurrentUsed_Type = Integer32
_HwBufferCurrentUsed_Object = MibTableColumn
hwBufferCurrentUsed = _HwBufferCurrentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 4),
    _HwBufferCurrentUsed_Type()
)
hwBufferCurrentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBufferCurrentUsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MEMORY-MIB",
    **{"hwMemoryDev": hwMemoryDev,
       "hwMemoryDevTable": hwMemoryDevTable,
       "hwMemoryDevEntry": hwMemoryDevEntry,
       "hwMemoryDevModuleIndex": hwMemoryDevModuleIndex,
       "hwMemoryDevSize": hwMemoryDevSize,
       "hwMemoryDevFree": hwMemoryDevFree,
       "hwMemoryDevRawSliceUsed": hwMemoryDevRawSliceUsed,
       "hwMemoryDevLargestFree": hwMemoryDevLargestFree,
       "hwMemoryDevFail": hwMemoryDevFail,
       "hwMemoryDevFailNoMem": hwMemoryDevFailNoMem,
       "hwBufferTable": hwBufferTable,
       "hwBufferEntry": hwBufferEntry,
       "hwBufferModuleIndex": hwBufferModuleIndex,
       "hwBufferSize": hwBufferSize,
       "hwBufferCurrentTotal": hwBufferCurrentTotal,
       "hwBufferCurrentUsed": hwBufferCurrentUsed}
)
