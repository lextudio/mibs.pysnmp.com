# SNMP MIB module (EXTREME-SOFTWARE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-SOFTWARE-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:15 2024
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

(PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "PortList",
    "extremeAgent")

(extremeImageDescription,) = mibBuilder.importSymbols(
    "EXTREME-SYSTEM-MIB",
    "extremeImageDescription")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeSwMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeSwMonitorCpu_ObjectIdentity = ObjectIdentity
extremeSwMonitorCpu = _ExtremeSwMonitorCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1)
)


class _ExtremeCpuMonitorInterval_Type(Integer32):
    """Custom type extremeCpuMonitorInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_ExtremeCpuMonitorInterval_Type.__name__ = "Integer32"
_ExtremeCpuMonitorInterval_Object = MibScalar
extremeCpuMonitorInterval = _ExtremeCpuMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 1),
    _ExtremeCpuMonitorInterval_Type()
)
extremeCpuMonitorInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorInterval.setStatus("current")


class _ExtremeCpuMonitorTotalUtilization_Type(Integer32):
    """Custom type extremeCpuMonitorTotalUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExtremeCpuMonitorTotalUtilization_Type.__name__ = "Integer32"
_ExtremeCpuMonitorTotalUtilization_Object = MibScalar
extremeCpuMonitorTotalUtilization = _ExtremeCpuMonitorTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 2),
    _ExtremeCpuMonitorTotalUtilization_Type()
)
extremeCpuMonitorTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorTotalUtilization.setStatus("current")
_ExtremeCpuMonitorTable_Object = MibTable
extremeCpuMonitorTable = _ExtremeCpuMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3)
)
if mibBuilder.loadTexts:
    extremeCpuMonitorTable.setStatus("current")
_ExtremeCpuMonitorEntry_Object = MibTableRow
extremeCpuMonitorEntry = _ExtremeCpuMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1)
)
extremeCpuMonitorEntry.setIndexNames(
    (0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorSlotId"),
    (1, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorProcessName"),
)
if mibBuilder.loadTexts:
    extremeCpuMonitorEntry.setStatus("current")
_ExtremeCpuMonitorSlotId_Type = Unsigned32
_ExtremeCpuMonitorSlotId_Object = MibTableColumn
extremeCpuMonitorSlotId = _ExtremeCpuMonitorSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 1),
    _ExtremeCpuMonitorSlotId_Type()
)
extremeCpuMonitorSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSlotId.setStatus("current")


class _ExtremeCpuMonitorProcessName_Type(DisplayString):
    """Custom type extremeCpuMonitorProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtremeCpuMonitorProcessName_Type.__name__ = "DisplayString"
_ExtremeCpuMonitorProcessName_Object = MibTableColumn
extremeCpuMonitorProcessName = _ExtremeCpuMonitorProcessName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 2),
    _ExtremeCpuMonitorProcessName_Type()
)
extremeCpuMonitorProcessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeCpuMonitorProcessName.setStatus("current")
_ExtremeCpuMonitorProcessId_Type = Unsigned32
_ExtremeCpuMonitorProcessId_Object = MibTableColumn
extremeCpuMonitorProcessId = _ExtremeCpuMonitorProcessId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 3),
    _ExtremeCpuMonitorProcessId_Type()
)
extremeCpuMonitorProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorProcessId.setStatus("current")
_ExtremeCpuMonitorProcessState_Type = DisplayString
_ExtremeCpuMonitorProcessState_Object = MibTableColumn
extremeCpuMonitorProcessState = _ExtremeCpuMonitorProcessState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 4),
    _ExtremeCpuMonitorProcessState_Type()
)
extremeCpuMonitorProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorProcessState.setStatus("current")
_ExtremeCpuMonitorUtilization5secs_Type = DisplayString
_ExtremeCpuMonitorUtilization5secs_Object = MibTableColumn
extremeCpuMonitorUtilization5secs = _ExtremeCpuMonitorUtilization5secs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 5),
    _ExtremeCpuMonitorUtilization5secs_Type()
)
extremeCpuMonitorUtilization5secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUtilization5secs.setStatus("current")
_ExtremeCpuMonitorUtilization10secs_Type = DisplayString
_ExtremeCpuMonitorUtilization10secs_Object = MibTableColumn
extremeCpuMonitorUtilization10secs = _ExtremeCpuMonitorUtilization10secs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 6),
    _ExtremeCpuMonitorUtilization10secs_Type()
)
extremeCpuMonitorUtilization10secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUtilization10secs.setStatus("current")
_ExtremeCpuMonitorUtilization30secs_Type = DisplayString
_ExtremeCpuMonitorUtilization30secs_Object = MibTableColumn
extremeCpuMonitorUtilization30secs = _ExtremeCpuMonitorUtilization30secs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 7),
    _ExtremeCpuMonitorUtilization30secs_Type()
)
extremeCpuMonitorUtilization30secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUtilization30secs.setStatus("current")
_ExtremeCpuMonitorUtilization1min_Type = DisplayString
_ExtremeCpuMonitorUtilization1min_Object = MibTableColumn
extremeCpuMonitorUtilization1min = _ExtremeCpuMonitorUtilization1min_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 8),
    _ExtremeCpuMonitorUtilization1min_Type()
)
extremeCpuMonitorUtilization1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUtilization1min.setStatus("current")
_ExtremeCpuMonitorUtilization5mins_Type = DisplayString
_ExtremeCpuMonitorUtilization5mins_Object = MibTableColumn
extremeCpuMonitorUtilization5mins = _ExtremeCpuMonitorUtilization5mins_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 9),
    _ExtremeCpuMonitorUtilization5mins_Type()
)
extremeCpuMonitorUtilization5mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUtilization5mins.setStatus("current")
_ExtremeCpuMonitorUtilization30mins_Type = DisplayString
_ExtremeCpuMonitorUtilization30mins_Object = MibTableColumn
extremeCpuMonitorUtilization30mins = _ExtremeCpuMonitorUtilization30mins_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 10),
    _ExtremeCpuMonitorUtilization30mins_Type()
)
extremeCpuMonitorUtilization30mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUtilization30mins.setStatus("current")
_ExtremeCpuMonitorUtilization1hour_Type = DisplayString
_ExtremeCpuMonitorUtilization1hour_Object = MibTableColumn
extremeCpuMonitorUtilization1hour = _ExtremeCpuMonitorUtilization1hour_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 11),
    _ExtremeCpuMonitorUtilization1hour_Type()
)
extremeCpuMonitorUtilization1hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUtilization1hour.setStatus("current")
_ExtremeCpuMonitorMaxUtilization_Type = DisplayString
_ExtremeCpuMonitorMaxUtilization_Object = MibTableColumn
extremeCpuMonitorMaxUtilization = _ExtremeCpuMonitorMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 12),
    _ExtremeCpuMonitorMaxUtilization_Type()
)
extremeCpuMonitorMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorMaxUtilization.setStatus("current")
_ExtremeCpuMonitorUserTime_Type = DisplayString
_ExtremeCpuMonitorUserTime_Object = MibTableColumn
extremeCpuMonitorUserTime = _ExtremeCpuMonitorUserTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 13),
    _ExtremeCpuMonitorUserTime_Type()
)
extremeCpuMonitorUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorUserTime.setStatus("current")
_ExtremeCpuMonitorSystemTime_Type = DisplayString
_ExtremeCpuMonitorSystemTime_Object = MibTableColumn
extremeCpuMonitorSystemTime = _ExtremeCpuMonitorSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 3, 1, 14),
    _ExtremeCpuMonitorSystemTime_Type()
)
extremeCpuMonitorSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemTime.setStatus("current")
_ExtremeCpuMonitorSystemTable_Object = MibTable
extremeCpuMonitorSystemTable = _ExtremeCpuMonitorSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4)
)
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemTable.setStatus("current")
_ExtremeCpuMonitorSystemEntry_Object = MibTableRow
extremeCpuMonitorSystemEntry = _ExtremeCpuMonitorSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1)
)
extremeCpuMonitorSystemEntry.setIndexNames(
    (0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorSystemSlotId"),
)
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemEntry.setStatus("current")
_ExtremeCpuMonitorSystemSlotId_Type = Unsigned32
_ExtremeCpuMonitorSystemSlotId_Object = MibTableColumn
extremeCpuMonitorSystemSlotId = _ExtremeCpuMonitorSystemSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 1),
    _ExtremeCpuMonitorSystemSlotId_Type()
)
extremeCpuMonitorSystemSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemSlotId.setStatus("current")
_ExtremeCpuMonitorSystemUtilization5secs_Type = DisplayString
_ExtremeCpuMonitorSystemUtilization5secs_Object = MibTableColumn
extremeCpuMonitorSystemUtilization5secs = _ExtremeCpuMonitorSystemUtilization5secs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 5),
    _ExtremeCpuMonitorSystemUtilization5secs_Type()
)
extremeCpuMonitorSystemUtilization5secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemUtilization5secs.setStatus("current")
_ExtremeCpuMonitorSystemUtilization10secs_Type = DisplayString
_ExtremeCpuMonitorSystemUtilization10secs_Object = MibTableColumn
extremeCpuMonitorSystemUtilization10secs = _ExtremeCpuMonitorSystemUtilization10secs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 6),
    _ExtremeCpuMonitorSystemUtilization10secs_Type()
)
extremeCpuMonitorSystemUtilization10secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemUtilization10secs.setStatus("current")
_ExtremeCpuMonitorSystemUtilization30secs_Type = DisplayString
_ExtremeCpuMonitorSystemUtilization30secs_Object = MibTableColumn
extremeCpuMonitorSystemUtilization30secs = _ExtremeCpuMonitorSystemUtilization30secs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 7),
    _ExtremeCpuMonitorSystemUtilization30secs_Type()
)
extremeCpuMonitorSystemUtilization30secs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemUtilization30secs.setStatus("current")
_ExtremeCpuMonitorSystemUtilization1min_Type = DisplayString
_ExtremeCpuMonitorSystemUtilization1min_Object = MibTableColumn
extremeCpuMonitorSystemUtilization1min = _ExtremeCpuMonitorSystemUtilization1min_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 8),
    _ExtremeCpuMonitorSystemUtilization1min_Type()
)
extremeCpuMonitorSystemUtilization1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemUtilization1min.setStatus("current")
_ExtremeCpuMonitorSystemUtilization5mins_Type = DisplayString
_ExtremeCpuMonitorSystemUtilization5mins_Object = MibTableColumn
extremeCpuMonitorSystemUtilization5mins = _ExtremeCpuMonitorSystemUtilization5mins_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 9),
    _ExtremeCpuMonitorSystemUtilization5mins_Type()
)
extremeCpuMonitorSystemUtilization5mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemUtilization5mins.setStatus("current")
_ExtremeCpuMonitorSystemUtilization30mins_Type = DisplayString
_ExtremeCpuMonitorSystemUtilization30mins_Object = MibTableColumn
extremeCpuMonitorSystemUtilization30mins = _ExtremeCpuMonitorSystemUtilization30mins_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 10),
    _ExtremeCpuMonitorSystemUtilization30mins_Type()
)
extremeCpuMonitorSystemUtilization30mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemUtilization30mins.setStatus("current")
_ExtremeCpuMonitorSystemUtilization1hour_Type = DisplayString
_ExtremeCpuMonitorSystemUtilization1hour_Object = MibTableColumn
extremeCpuMonitorSystemUtilization1hour = _ExtremeCpuMonitorSystemUtilization1hour_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 11),
    _ExtremeCpuMonitorSystemUtilization1hour_Type()
)
extremeCpuMonitorSystemUtilization1hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemUtilization1hour.setStatus("current")
_ExtremeCpuMonitorSystemMaxUtilization_Type = DisplayString
_ExtremeCpuMonitorSystemMaxUtilization_Object = MibTableColumn
extremeCpuMonitorSystemMaxUtilization = _ExtremeCpuMonitorSystemMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 4, 1, 12),
    _ExtremeCpuMonitorSystemMaxUtilization_Type()
)
extremeCpuMonitorSystemMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuMonitorSystemMaxUtilization.setStatus("current")


class _ExtremeCpuMonitorThreshold_Type(Integer32):
    """Custom type extremeCpuMonitorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExtremeCpuMonitorThreshold_Type.__name__ = "Integer32"
_ExtremeCpuMonitorThreshold_Object = MibScalar
extremeCpuMonitorThreshold = _ExtremeCpuMonitorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 5),
    _ExtremeCpuMonitorThreshold_Type()
)
extremeCpuMonitorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeCpuMonitorThreshold.setStatus("current")
_ExtremeCpuMonitorCurrentUtilization_Type = DisplayString
_ExtremeCpuMonitorCurrentUtilization_Object = MibScalar
extremeCpuMonitorCurrentUtilization = _ExtremeCpuMonitorCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 1, 6),
    _ExtremeCpuMonitorCurrentUtilization_Type()
)
extremeCpuMonitorCurrentUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeCpuMonitorCurrentUtilization.setStatus("current")
_ExtremeSwMonitorMemory_ObjectIdentity = ObjectIdentity
extremeSwMonitorMemory = _ExtremeSwMonitorMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2)
)
_ExtremeMemoryMonitorSystemTable_Object = MibTable
extremeMemoryMonitorSystemTable = _ExtremeMemoryMonitorSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2)
)
if mibBuilder.loadTexts:
    extremeMemoryMonitorSystemTable.setStatus("current")
_ExtremeMemoryMonitorSystemEntry_Object = MibTableRow
extremeMemoryMonitorSystemEntry = _ExtremeMemoryMonitorSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1)
)
extremeMemoryMonitorSystemEntry.setIndexNames(
    (0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeMemoryMonitorSystemSlotId"),
)
if mibBuilder.loadTexts:
    extremeMemoryMonitorSystemEntry.setStatus("current")
_ExtremeMemoryMonitorSystemSlotId_Type = Unsigned32
_ExtremeMemoryMonitorSystemSlotId_Object = MibTableColumn
extremeMemoryMonitorSystemSlotId = _ExtremeMemoryMonitorSystemSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 1),
    _ExtremeMemoryMonitorSystemSlotId_Type()
)
extremeMemoryMonitorSystemSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorSystemSlotId.setStatus("current")


class _ExtremeMemoryMonitorSystemTotal_Type(DisplayString):
    """Custom type extremeMemoryMonitorSystemTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExtremeMemoryMonitorSystemTotal_Type.__name__ = "DisplayString"
_ExtremeMemoryMonitorSystemTotal_Object = MibTableColumn
extremeMemoryMonitorSystemTotal = _ExtremeMemoryMonitorSystemTotal_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 2),
    _ExtremeMemoryMonitorSystemTotal_Type()
)
extremeMemoryMonitorSystemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorSystemTotal.setStatus("current")


class _ExtremeMemoryMonitorSystemFree_Type(DisplayString):
    """Custom type extremeMemoryMonitorSystemFree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExtremeMemoryMonitorSystemFree_Type.__name__ = "DisplayString"
_ExtremeMemoryMonitorSystemFree_Object = MibTableColumn
extremeMemoryMonitorSystemFree = _ExtremeMemoryMonitorSystemFree_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 3),
    _ExtremeMemoryMonitorSystemFree_Type()
)
extremeMemoryMonitorSystemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorSystemFree.setStatus("current")


class _ExtremeMemoryMonitorSystemUsage_Type(DisplayString):
    """Custom type extremeMemoryMonitorSystemUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExtremeMemoryMonitorSystemUsage_Type.__name__ = "DisplayString"
_ExtremeMemoryMonitorSystemUsage_Object = MibTableColumn
extremeMemoryMonitorSystemUsage = _ExtremeMemoryMonitorSystemUsage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 4),
    _ExtremeMemoryMonitorSystemUsage_Type()
)
extremeMemoryMonitorSystemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorSystemUsage.setStatus("current")


class _ExtremeMemoryMonitorUserUsage_Type(DisplayString):
    """Custom type extremeMemoryMonitorUserUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExtremeMemoryMonitorUserUsage_Type.__name__ = "DisplayString"
_ExtremeMemoryMonitorUserUsage_Object = MibTableColumn
extremeMemoryMonitorUserUsage = _ExtremeMemoryMonitorUserUsage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 2, 1, 5),
    _ExtremeMemoryMonitorUserUsage_Type()
)
extremeMemoryMonitorUserUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorUserUsage.setStatus("current")
_ExtremeMemoryMonitorTable_Object = MibTable
extremeMemoryMonitorTable = _ExtremeMemoryMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3)
)
if mibBuilder.loadTexts:
    extremeMemoryMonitorTable.setStatus("current")
_ExtremeMemoryMonitorEntry_Object = MibTableRow
extremeMemoryMonitorEntry = _ExtremeMemoryMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1)
)
extremeMemoryMonitorEntry.setIndexNames(
    (0, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeMemoryMonitorSlotId"),
    (1, "EXTREME-SOFTWARE-MONITOR-MIB", "extremeMemoryMonitorProcessName"),
)
if mibBuilder.loadTexts:
    extremeMemoryMonitorEntry.setStatus("current")
_ExtremeMemoryMonitorSlotId_Type = Unsigned32
_ExtremeMemoryMonitorSlotId_Object = MibTableColumn
extremeMemoryMonitorSlotId = _ExtremeMemoryMonitorSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 1),
    _ExtremeMemoryMonitorSlotId_Type()
)
extremeMemoryMonitorSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorSlotId.setStatus("current")


class _ExtremeMemoryMonitorProcessName_Type(DisplayString):
    """Custom type extremeMemoryMonitorProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtremeMemoryMonitorProcessName_Type.__name__ = "DisplayString"
_ExtremeMemoryMonitorProcessName_Object = MibTableColumn
extremeMemoryMonitorProcessName = _ExtremeMemoryMonitorProcessName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 2),
    _ExtremeMemoryMonitorProcessName_Type()
)
extremeMemoryMonitorProcessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeMemoryMonitorProcessName.setStatus("current")
_ExtremeMemoryMonitorUsage_Type = Unsigned32
_ExtremeMemoryMonitorUsage_Object = MibTableColumn
extremeMemoryMonitorUsage = _ExtremeMemoryMonitorUsage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 3),
    _ExtremeMemoryMonitorUsage_Type()
)
extremeMemoryMonitorUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorUsage.setStatus("current")
_ExtremeMemoryMonitorLimit_Type = Unsigned32
_ExtremeMemoryMonitorLimit_Object = MibTableColumn
extremeMemoryMonitorLimit = _ExtremeMemoryMonitorLimit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 4),
    _ExtremeMemoryMonitorLimit_Type()
)
extremeMemoryMonitorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorLimit.setStatus("current")


class _ExtremeMemoryMonitorZone_Type(DisplayString):
    """Custom type extremeMemoryMonitorZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExtremeMemoryMonitorZone_Type.__name__ = "DisplayString"
_ExtremeMemoryMonitorZone_Object = MibTableColumn
extremeMemoryMonitorZone = _ExtremeMemoryMonitorZone_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 5),
    _ExtremeMemoryMonitorZone_Type()
)
extremeMemoryMonitorZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorZone.setStatus("current")
_ExtremeMemoryMonitorGreenZoneCount_Type = Unsigned32
_ExtremeMemoryMonitorGreenZoneCount_Object = MibTableColumn
extremeMemoryMonitorGreenZoneCount = _ExtremeMemoryMonitorGreenZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 6),
    _ExtremeMemoryMonitorGreenZoneCount_Type()
)
extremeMemoryMonitorGreenZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorGreenZoneCount.setStatus("current")
_ExtremeMemoryMonitorYellowZoneCount_Type = Unsigned32
_ExtremeMemoryMonitorYellowZoneCount_Object = MibTableColumn
extremeMemoryMonitorYellowZoneCount = _ExtremeMemoryMonitorYellowZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 7),
    _ExtremeMemoryMonitorYellowZoneCount_Type()
)
extremeMemoryMonitorYellowZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorYellowZoneCount.setStatus("current")
_ExtremeMemoryMonitorOrangeZoneCount_Type = Unsigned32
_ExtremeMemoryMonitorOrangeZoneCount_Object = MibTableColumn
extremeMemoryMonitorOrangeZoneCount = _ExtremeMemoryMonitorOrangeZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 8),
    _ExtremeMemoryMonitorOrangeZoneCount_Type()
)
extremeMemoryMonitorOrangeZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorOrangeZoneCount.setStatus("current")
_ExtremeMemoryMonitorRedZoneCount_Type = Unsigned32
_ExtremeMemoryMonitorRedZoneCount_Object = MibTableColumn
extremeMemoryMonitorRedZoneCount = _ExtremeMemoryMonitorRedZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 9),
    _ExtremeMemoryMonitorRedZoneCount_Type()
)
extremeMemoryMonitorRedZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorRedZoneCount.setStatus("current")
_ExtremeMemoryMonitorGreenZoneThreshold_Type = Unsigned32
_ExtremeMemoryMonitorGreenZoneThreshold_Object = MibTableColumn
extremeMemoryMonitorGreenZoneThreshold = _ExtremeMemoryMonitorGreenZoneThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 10),
    _ExtremeMemoryMonitorGreenZoneThreshold_Type()
)
extremeMemoryMonitorGreenZoneThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorGreenZoneThreshold.setStatus("current")
_ExtremeMemoryMonitorYellowZoneThreshold_Type = Unsigned32
_ExtremeMemoryMonitorYellowZoneThreshold_Object = MibTableColumn
extremeMemoryMonitorYellowZoneThreshold = _ExtremeMemoryMonitorYellowZoneThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 11),
    _ExtremeMemoryMonitorYellowZoneThreshold_Type()
)
extremeMemoryMonitorYellowZoneThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorYellowZoneThreshold.setStatus("current")
_ExtremeMemoryMonitorOrangeZoneThreshold_Type = Unsigned32
_ExtremeMemoryMonitorOrangeZoneThreshold_Object = MibTableColumn
extremeMemoryMonitorOrangeZoneThreshold = _ExtremeMemoryMonitorOrangeZoneThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 12),
    _ExtremeMemoryMonitorOrangeZoneThreshold_Type()
)
extremeMemoryMonitorOrangeZoneThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorOrangeZoneThreshold.setStatus("current")
_ExtremeMemoryMonitorRedZoneThreshold_Type = Unsigned32
_ExtremeMemoryMonitorRedZoneThreshold_Object = MibTableColumn
extremeMemoryMonitorRedZoneThreshold = _ExtremeMemoryMonitorRedZoneThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 2, 3, 1, 13),
    _ExtremeMemoryMonitorRedZoneThreshold_Type()
)
extremeMemoryMonitorRedZoneThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMemoryMonitorRedZoneThreshold.setStatus("current")
_ExtremeSwMonitorNotifications_ObjectIdentity = ObjectIdentity
extremeSwMonitorNotifications = _ExtremeSwMonitorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 3)
)
_ExtremeSwMonitorNotificationsPrefix_ObjectIdentity = ObjectIdentity
extremeSwMonitorNotificationsPrefix = _ExtremeSwMonitorNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0)
)
_ExtremeServiceLicense_ObjectIdentity = ObjectIdentity
extremeServiceLicense = _ExtremeServiceLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 4)
)
_ExtremeServiceLicenseExpiryDate_Type = DisplayString
_ExtremeServiceLicenseExpiryDate_Object = MibScalar
extremeServiceLicenseExpiryDate = _ExtremeServiceLicenseExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 1),
    _ExtremeServiceLicenseExpiryDate_Type()
)
extremeServiceLicenseExpiryDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeServiceLicenseExpiryDate.setStatus("current")
_ExtremeServiceLicenseType_Type = DisplayString
_ExtremeServiceLicenseType_Object = MibScalar
extremeServiceLicenseType = _ExtremeServiceLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 2),
    _ExtremeServiceLicenseType_Type()
)
extremeServiceLicenseType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeServiceLicenseType.setStatus("current")
_ImageDescription_Type = DisplayString
_ImageDescription_Object = MibScalar
imageDescription = _ImageDescription_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 3),
    _ImageDescription_Type()
)
imageDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imageDescription.setStatus("current")


class _NoOfDaysLeft_Type(Integer32):
    """Custom type noOfDaysLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_NoOfDaysLeft_Type.__name__ = "Integer32"
_NoOfDaysLeft_Object = MibScalar
noOfDaysLeft = _NoOfDaysLeft_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 4, 4),
    _NoOfDaysLeft_Type()
)
noOfDaysLeft.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    noOfDaysLeft.setStatus("current")
_ExtremeTrialLicense_ObjectIdentity = ObjectIdentity
extremeTrialLicense = _ExtremeTrialLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 5)
)


class _TrialPeriod_Type(Integer32):
    """Custom type trialPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_TrialPeriod_Type.__name__ = "Integer32"
_TrialPeriod_Object = MibScalar
trialPeriod = _TrialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 5, 1),
    _TrialPeriod_Type()
)
trialPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trialPeriod.setStatus("current")

# Managed Objects groups


# Notification objects

extremeSwMonitorCpuUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0, 1)
)
extremeSwMonitorCpuUtilization.setObjects(
      *(("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorSlotId"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorProcessName"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorCurrentUtilization"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeCpuMonitorThreshold"))
)
if mibBuilder.loadTexts:
    extremeSwMonitorCpuUtilization.setStatus(
        "current"
    )

extremeServiceLicenseExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0, 2)
)
extremeServiceLicenseExpiration.setObjects(
      *(("EXTREME-SOFTWARE-MONITOR-MIB", "extremeServiceLicenseExpiryDate"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "extremeServiceLicenseType"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "imageDescription"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "noOfDaysLeft"))
)
if mibBuilder.loadTexts:
    extremeServiceLicenseExpiration.setStatus(
        "current"
    )

extremeTrialLicenseExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32, 3, 0, 3)
)
extremeTrialLicenseExpiration.setObjects(
      *(("EXTREME-SOFTWARE-MONITOR-MIB", "trialPeriod"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "imageDescription"),
        ("EXTREME-SOFTWARE-MONITOR-MIB", "noOfDaysLeft"))
)
if mibBuilder.loadTexts:
    extremeTrialLicenseExpiration.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-SOFTWARE-MONITOR-MIB",
    **{"extremeSwMonitor": extremeSwMonitor,
       "extremeSwMonitorCpu": extremeSwMonitorCpu,
       "extremeCpuMonitorInterval": extremeCpuMonitorInterval,
       "extremeCpuMonitorTotalUtilization": extremeCpuMonitorTotalUtilization,
       "extremeCpuMonitorTable": extremeCpuMonitorTable,
       "extremeCpuMonitorEntry": extremeCpuMonitorEntry,
       "extremeCpuMonitorSlotId": extremeCpuMonitorSlotId,
       "extremeCpuMonitorProcessName": extremeCpuMonitorProcessName,
       "extremeCpuMonitorProcessId": extremeCpuMonitorProcessId,
       "extremeCpuMonitorProcessState": extremeCpuMonitorProcessState,
       "extremeCpuMonitorUtilization5secs": extremeCpuMonitorUtilization5secs,
       "extremeCpuMonitorUtilization10secs": extremeCpuMonitorUtilization10secs,
       "extremeCpuMonitorUtilization30secs": extremeCpuMonitorUtilization30secs,
       "extremeCpuMonitorUtilization1min": extremeCpuMonitorUtilization1min,
       "extremeCpuMonitorUtilization5mins": extremeCpuMonitorUtilization5mins,
       "extremeCpuMonitorUtilization30mins": extremeCpuMonitorUtilization30mins,
       "extremeCpuMonitorUtilization1hour": extremeCpuMonitorUtilization1hour,
       "extremeCpuMonitorMaxUtilization": extremeCpuMonitorMaxUtilization,
       "extremeCpuMonitorUserTime": extremeCpuMonitorUserTime,
       "extremeCpuMonitorSystemTime": extremeCpuMonitorSystemTime,
       "extremeCpuMonitorSystemTable": extremeCpuMonitorSystemTable,
       "extremeCpuMonitorSystemEntry": extremeCpuMonitorSystemEntry,
       "extremeCpuMonitorSystemSlotId": extremeCpuMonitorSystemSlotId,
       "extremeCpuMonitorSystemUtilization5secs": extremeCpuMonitorSystemUtilization5secs,
       "extremeCpuMonitorSystemUtilization10secs": extremeCpuMonitorSystemUtilization10secs,
       "extremeCpuMonitorSystemUtilization30secs": extremeCpuMonitorSystemUtilization30secs,
       "extremeCpuMonitorSystemUtilization1min": extremeCpuMonitorSystemUtilization1min,
       "extremeCpuMonitorSystemUtilization5mins": extremeCpuMonitorSystemUtilization5mins,
       "extremeCpuMonitorSystemUtilization30mins": extremeCpuMonitorSystemUtilization30mins,
       "extremeCpuMonitorSystemUtilization1hour": extremeCpuMonitorSystemUtilization1hour,
       "extremeCpuMonitorSystemMaxUtilization": extremeCpuMonitorSystemMaxUtilization,
       "extremeCpuMonitorThreshold": extremeCpuMonitorThreshold,
       "extremeCpuMonitorCurrentUtilization": extremeCpuMonitorCurrentUtilization,
       "extremeSwMonitorMemory": extremeSwMonitorMemory,
       "extremeMemoryMonitorSystemTable": extremeMemoryMonitorSystemTable,
       "extremeMemoryMonitorSystemEntry": extremeMemoryMonitorSystemEntry,
       "extremeMemoryMonitorSystemSlotId": extremeMemoryMonitorSystemSlotId,
       "extremeMemoryMonitorSystemTotal": extremeMemoryMonitorSystemTotal,
       "extremeMemoryMonitorSystemFree": extremeMemoryMonitorSystemFree,
       "extremeMemoryMonitorSystemUsage": extremeMemoryMonitorSystemUsage,
       "extremeMemoryMonitorUserUsage": extremeMemoryMonitorUserUsage,
       "extremeMemoryMonitorTable": extremeMemoryMonitorTable,
       "extremeMemoryMonitorEntry": extremeMemoryMonitorEntry,
       "extremeMemoryMonitorSlotId": extremeMemoryMonitorSlotId,
       "extremeMemoryMonitorProcessName": extremeMemoryMonitorProcessName,
       "extremeMemoryMonitorUsage": extremeMemoryMonitorUsage,
       "extremeMemoryMonitorLimit": extremeMemoryMonitorLimit,
       "extremeMemoryMonitorZone": extremeMemoryMonitorZone,
       "extremeMemoryMonitorGreenZoneCount": extremeMemoryMonitorGreenZoneCount,
       "extremeMemoryMonitorYellowZoneCount": extremeMemoryMonitorYellowZoneCount,
       "extremeMemoryMonitorOrangeZoneCount": extremeMemoryMonitorOrangeZoneCount,
       "extremeMemoryMonitorRedZoneCount": extremeMemoryMonitorRedZoneCount,
       "extremeMemoryMonitorGreenZoneThreshold": extremeMemoryMonitorGreenZoneThreshold,
       "extremeMemoryMonitorYellowZoneThreshold": extremeMemoryMonitorYellowZoneThreshold,
       "extremeMemoryMonitorOrangeZoneThreshold": extremeMemoryMonitorOrangeZoneThreshold,
       "extremeMemoryMonitorRedZoneThreshold": extremeMemoryMonitorRedZoneThreshold,
       "extremeSwMonitorNotifications": extremeSwMonitorNotifications,
       "extremeSwMonitorNotificationsPrefix": extremeSwMonitorNotificationsPrefix,
       "extremeSwMonitorCpuUtilization": extremeSwMonitorCpuUtilization,
       "extremeServiceLicenseExpiration": extremeServiceLicenseExpiration,
       "extremeTrialLicenseExpiration": extremeTrialLicenseExpiration,
       "extremeServiceLicense": extremeServiceLicense,
       "extremeServiceLicenseExpiryDate": extremeServiceLicenseExpiryDate,
       "extremeServiceLicenseType": extremeServiceLicenseType,
       "imageDescription": imageDescription,
       "noOfDaysLeft": noOfDaysLeft,
       "extremeTrialLicense": extremeTrialLicense,
       "trialPeriod": trialPeriod}
)
