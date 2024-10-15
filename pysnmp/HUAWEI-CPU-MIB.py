# SNMP MIB module (HUAWEI-CPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-CPU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:24 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

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

hwDev = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwCpuDevTable_Object = MibTable
hwCpuDevTable = _HwCpuDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4)
)
if mibBuilder.loadTexts:
    hwCpuDevTable.setStatus("current")
_HwCpuDevEntry_Object = MibTableRow
hwCpuDevEntry = _HwCpuDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1)
)
hwCpuDevEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-CPU-MIB", "hwCpuDevIndex"),
)
if mibBuilder.loadTexts:
    hwCpuDevEntry.setStatus("current")


class _HwCpuDevIndex_Type(Integer32):
    """Custom type hwCpuDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwCpuDevIndex_Type.__name__ = "Integer32"
_HwCpuDevIndex_Object = MibTableColumn
hwCpuDevIndex = _HwCpuDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 1),
    _HwCpuDevIndex_Type()
)
hwCpuDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCpuDevIndex.setStatus("current")


class _HwCpuDevDuty_Type(Integer32):
    """Custom type hwCpuDevDuty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwCpuDevDuty_Type.__name__ = "Integer32"
_HwCpuDevDuty_Object = MibTableColumn
hwCpuDevDuty = _HwCpuDevDuty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 2),
    _HwCpuDevDuty_Type()
)
hwCpuDevDuty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCpuDevDuty.setStatus("current")


class _HwAvgDuty1min_Type(Integer32):
    """Custom type hwAvgDuty1min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwAvgDuty1min_Type.__name__ = "Integer32"
_HwAvgDuty1min_Object = MibTableColumn
hwAvgDuty1min = _HwAvgDuty1min_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 3),
    _HwAvgDuty1min_Type()
)
hwAvgDuty1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAvgDuty1min.setStatus("current")


class _HwAvgDuty5min_Type(Integer32):
    """Custom type hwAvgDuty5min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwAvgDuty5min_Type.__name__ = "Integer32"
_HwAvgDuty5min_Object = MibTableColumn
hwAvgDuty5min = _HwAvgDuty5min_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 4),
    _HwAvgDuty5min_Type()
)
hwAvgDuty5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAvgDuty5min.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-CPU-MIB",
    **{"hwDev": hwDev,
       "hwCpuDevTable": hwCpuDevTable,
       "hwCpuDevEntry": hwCpuDevEntry,
       "hwCpuDevIndex": hwCpuDevIndex,
       "hwCpuDevDuty": hwCpuDevDuty,
       "hwAvgDuty1min": hwAvgDuty1min,
       "hwAvgDuty5min": hwAvgDuty5min}
)
