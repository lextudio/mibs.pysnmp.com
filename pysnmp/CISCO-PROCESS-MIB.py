# SNMP MIB module (CISCO-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PROCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:08 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero",
    "Unsigned64")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109)
)
ciscoProcessMIB.setRevisions(
        ("2011-06-23 00:00",
         "2010-05-06 00:00",
         "2009-10-12 00:00",
         "2009-01-23 00:00",
         "2007-03-23 00:00",
         "2003-01-22 00:00",
         "2001-05-18 00:00",
         "1998-04-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CPULoadAverage(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_CiscoProcessMIBObjects_ObjectIdentity = ObjectIdentity
ciscoProcessMIBObjects = _CiscoProcessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1)
)
_CpmCPU_ObjectIdentity = ObjectIdentity
cpmCPU = _CpmCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1)
)
_CpmCPUTotalTable_Object = MibTable
cpmCPUTotalTable = _CpmCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpmCPUTotalTable.setStatus("current")
_CpmCPUTotalEntry_Object = MibTableRow
cpmCPUTotalEntry = _CpmCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1)
)
cpmCPUTotalEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
)
if mibBuilder.loadTexts:
    cpmCPUTotalEntry.setStatus("current")


class _CpmCPUTotalIndex_Type(Unsigned32):
    """Custom type cpmCPUTotalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpmCPUTotalIndex_Type.__name__ = "Unsigned32"
_CpmCPUTotalIndex_Object = MibTableColumn
cpmCPUTotalIndex = _CpmCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 1),
    _CpmCPUTotalIndex_Type()
)
cpmCPUTotalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCPUTotalIndex.setStatus("current")
_CpmCPUTotalPhysicalIndex_Type = EntPhysicalIndexOrZero
_CpmCPUTotalPhysicalIndex_Object = MibTableColumn
cpmCPUTotalPhysicalIndex = _CpmCPUTotalPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 2),
    _CpmCPUTotalPhysicalIndex_Type()
)
cpmCPUTotalPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotalPhysicalIndex.setStatus("current")


class _CpmCPUTotal5sec_Type(Gauge32):
    """Custom type cpmCPUTotal5sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmCPUTotal5sec_Type.__name__ = "Gauge32"
_CpmCPUTotal5sec_Object = MibTableColumn
cpmCPUTotal5sec = _CpmCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 3),
    _CpmCPUTotal5sec_Type()
)
cpmCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotal5sec.setStatus("deprecated")


class _CpmCPUTotal1min_Type(Gauge32):
    """Custom type cpmCPUTotal1min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmCPUTotal1min_Type.__name__ = "Gauge32"
_CpmCPUTotal1min_Object = MibTableColumn
cpmCPUTotal1min = _CpmCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 4),
    _CpmCPUTotal1min_Type()
)
cpmCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotal1min.setStatus("deprecated")


class _CpmCPUTotal5min_Type(Gauge32):
    """Custom type cpmCPUTotal5min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmCPUTotal5min_Type.__name__ = "Gauge32"
_CpmCPUTotal5min_Object = MibTableColumn
cpmCPUTotal5min = _CpmCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 5),
    _CpmCPUTotal5min_Type()
)
cpmCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotal5min.setStatus("deprecated")


class _CpmCPUTotal5secRev_Type(Gauge32):
    """Custom type cpmCPUTotal5secRev based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUTotal5secRev_Type.__name__ = "Gauge32"
_CpmCPUTotal5secRev_Object = MibTableColumn
cpmCPUTotal5secRev = _CpmCPUTotal5secRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 6),
    _CpmCPUTotal5secRev_Type()
)
cpmCPUTotal5secRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotal5secRev.setStatus("deprecated")
if mibBuilder.loadTexts:
    cpmCPUTotal5secRev.setUnits("percent")


class _CpmCPUTotal1minRev_Type(Gauge32):
    """Custom type cpmCPUTotal1minRev based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUTotal1minRev_Type.__name__ = "Gauge32"
_CpmCPUTotal1minRev_Object = MibTableColumn
cpmCPUTotal1minRev = _CpmCPUTotal1minRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 7),
    _CpmCPUTotal1minRev_Type()
)
cpmCPUTotal1minRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotal1minRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUTotal1minRev.setUnits("percent")


class _CpmCPUTotal5minRev_Type(Gauge32):
    """Custom type cpmCPUTotal5minRev based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUTotal5minRev_Type.__name__ = "Gauge32"
_CpmCPUTotal5minRev_Object = MibTableColumn
cpmCPUTotal5minRev = _CpmCPUTotal5minRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 8),
    _CpmCPUTotal5minRev_Type()
)
cpmCPUTotal5minRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotal5minRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUTotal5minRev.setUnits("percent")
_CpmCPUMonInterval_Type = Unsigned32
_CpmCPUMonInterval_Object = MibTableColumn
cpmCPUMonInterval = _CpmCPUMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 9),
    _CpmCPUMonInterval_Type()
)
cpmCPUMonInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMonInterval.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMonInterval.setUnits("seconds")


class _CpmCPUTotalMonIntervalValue_Type(Gauge32):
    """Custom type cpmCPUTotalMonIntervalValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUTotalMonIntervalValue_Type.__name__ = "Gauge32"
_CpmCPUTotalMonIntervalValue_Object = MibTableColumn
cpmCPUTotalMonIntervalValue = _CpmCPUTotalMonIntervalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 10),
    _CpmCPUTotalMonIntervalValue_Type()
)
cpmCPUTotalMonIntervalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUTotalMonIntervalValue.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUTotalMonIntervalValue.setUnits("percent")


class _CpmCPUInterruptMonIntervalValue_Type(Gauge32):
    """Custom type cpmCPUInterruptMonIntervalValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUInterruptMonIntervalValue_Type.__name__ = "Gauge32"
_CpmCPUInterruptMonIntervalValue_Object = MibTableColumn
cpmCPUInterruptMonIntervalValue = _CpmCPUInterruptMonIntervalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 11),
    _CpmCPUInterruptMonIntervalValue_Type()
)
cpmCPUInterruptMonIntervalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUInterruptMonIntervalValue.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUInterruptMonIntervalValue.setUnits("percent")
_CpmCPUMemoryUsed_Type = Gauge32
_CpmCPUMemoryUsed_Object = MibTableColumn
cpmCPUMemoryUsed = _CpmCPUMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 12),
    _CpmCPUMemoryUsed_Type()
)
cpmCPUMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryUsed.setUnits("kilo-bytes")
_CpmCPUMemoryFree_Type = Gauge32
_CpmCPUMemoryFree_Object = MibTableColumn
cpmCPUMemoryFree = _CpmCPUMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 13),
    _CpmCPUMemoryFree_Type()
)
cpmCPUMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryFree.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryFree.setUnits("kilo-bytes")
_CpmCPUMemoryKernelReserved_Type = Gauge32
_CpmCPUMemoryKernelReserved_Object = MibTableColumn
cpmCPUMemoryKernelReserved = _CpmCPUMemoryKernelReserved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 14),
    _CpmCPUMemoryKernelReserved_Type()
)
cpmCPUMemoryKernelReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryKernelReserved.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryKernelReserved.setUnits("kilo-bytes")
_CpmCPUMemoryLowest_Type = Gauge32
_CpmCPUMemoryLowest_Object = MibTableColumn
cpmCPUMemoryLowest = _CpmCPUMemoryLowest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 15),
    _CpmCPUMemoryLowest_Type()
)
cpmCPUMemoryLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryLowest.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryLowest.setUnits("bytes")
_CpmCPUMemoryUsedOvrflw_Type = Gauge32
_CpmCPUMemoryUsedOvrflw_Object = MibTableColumn
cpmCPUMemoryUsedOvrflw = _CpmCPUMemoryUsedOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 16),
    _CpmCPUMemoryUsedOvrflw_Type()
)
cpmCPUMemoryUsedOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryUsedOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryUsedOvrflw.setUnits("kilo-bytes")
_CpmCPUMemoryHCUsed_Type = CounterBasedGauge64
_CpmCPUMemoryHCUsed_Object = MibTableColumn
cpmCPUMemoryHCUsed = _CpmCPUMemoryHCUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 17),
    _CpmCPUMemoryHCUsed_Type()
)
cpmCPUMemoryHCUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCUsed.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCUsed.setUnits("kilo-bytes")
_CpmCPUMemoryFreeOvrflw_Type = Gauge32
_CpmCPUMemoryFreeOvrflw_Object = MibTableColumn
cpmCPUMemoryFreeOvrflw = _CpmCPUMemoryFreeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 18),
    _CpmCPUMemoryFreeOvrflw_Type()
)
cpmCPUMemoryFreeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryFreeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryFreeOvrflw.setUnits("kilo-bytes")
_CpmCPUMemoryHCFree_Type = Counter64
_CpmCPUMemoryHCFree_Object = MibTableColumn
cpmCPUMemoryHCFree = _CpmCPUMemoryHCFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 19),
    _CpmCPUMemoryHCFree_Type()
)
cpmCPUMemoryHCFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCFree.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCFree.setUnits("kilo-bytes")
_CpmCPUMemoryKernelReservedOvrflw_Type = Gauge32
_CpmCPUMemoryKernelReservedOvrflw_Object = MibTableColumn
cpmCPUMemoryKernelReservedOvrflw = _CpmCPUMemoryKernelReservedOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 20),
    _CpmCPUMemoryKernelReservedOvrflw_Type()
)
cpmCPUMemoryKernelReservedOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryKernelReservedOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryKernelReservedOvrflw.setUnits("kilo-bytes")
_CpmCPUMemoryHCKernelReserved_Type = CounterBasedGauge64
_CpmCPUMemoryHCKernelReserved_Object = MibTableColumn
cpmCPUMemoryHCKernelReserved = _CpmCPUMemoryHCKernelReserved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 21),
    _CpmCPUMemoryHCKernelReserved_Type()
)
cpmCPUMemoryHCKernelReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCKernelReserved.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCKernelReserved.setUnits("kilo-bytes")
_CpmCPUMemoryLowestOvrflw_Type = Gauge32
_CpmCPUMemoryLowestOvrflw_Object = MibTableColumn
cpmCPUMemoryLowestOvrflw = _CpmCPUMemoryLowestOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 22),
    _CpmCPUMemoryLowestOvrflw_Type()
)
cpmCPUMemoryLowestOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryLowestOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryLowestOvrflw.setUnits("kilo-bytes")
_CpmCPUMemoryHCLowest_Type = CounterBasedGauge64
_CpmCPUMemoryHCLowest_Object = MibTableColumn
cpmCPUMemoryHCLowest = _CpmCPUMemoryHCLowest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 23),
    _CpmCPUMemoryHCLowest_Type()
)
cpmCPUMemoryHCLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCLowest.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCLowest.setUnits("kilo-bytes")
_CpmCPULoadAvg1min_Type = CPULoadAverage
_CpmCPULoadAvg1min_Object = MibTableColumn
cpmCPULoadAvg1min = _CpmCPULoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 24),
    _CpmCPULoadAvg1min_Type()
)
cpmCPULoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPULoadAvg1min.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPULoadAvg1min.setUnits("hundredths of processes")
_CpmCPULoadAvg5min_Type = CPULoadAverage
_CpmCPULoadAvg5min_Object = MibTableColumn
cpmCPULoadAvg5min = _CpmCPULoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 25),
    _CpmCPULoadAvg5min_Type()
)
cpmCPULoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPULoadAvg5min.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPULoadAvg5min.setUnits("hundredths of processes")
_CpmCPULoadAvg15min_Type = CPULoadAverage
_CpmCPULoadAvg15min_Object = MibTableColumn
cpmCPULoadAvg15min = _CpmCPULoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 26),
    _CpmCPULoadAvg15min_Type()
)
cpmCPULoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPULoadAvg15min.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPULoadAvg15min.setUnits("hundredths of processes")
_CpmCPUMemoryCommitted_Type = Gauge32
_CpmCPUMemoryCommitted_Object = MibTableColumn
cpmCPUMemoryCommitted = _CpmCPUMemoryCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 27),
    _CpmCPUMemoryCommitted_Type()
)
cpmCPUMemoryCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryCommitted.setStatus("current")
_CpmCPUMemoryCommittedOvrflw_Type = Gauge32
_CpmCPUMemoryCommittedOvrflw_Object = MibTableColumn
cpmCPUMemoryCommittedOvrflw = _CpmCPUMemoryCommittedOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 28),
    _CpmCPUMemoryCommittedOvrflw_Type()
)
cpmCPUMemoryCommittedOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryCommittedOvrflw.setStatus("current")
_CpmCPUMemoryHCCommitted_Type = CounterBasedGauge64
_CpmCPUMemoryHCCommitted_Object = MibTableColumn
cpmCPUMemoryHCCommitted = _CpmCPUMemoryHCCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 1, 1, 29),
    _CpmCPUMemoryHCCommitted_Type()
)
cpmCPUMemoryHCCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUMemoryHCCommitted.setStatus("current")
_CpmCoreTable_Object = MibTable
cpmCoreTable = _CpmCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpmCoreTable.setStatus("current")
_CpmCoreEntry_Object = MibTableRow
cpmCoreEntry = _CpmCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1)
)
cpmCoreEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmCoreIndex"),
)
if mibBuilder.loadTexts:
    cpmCoreEntry.setStatus("current")


class _CpmCoreIndex_Type(Unsigned32):
    """Custom type cpmCoreIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpmCoreIndex_Type.__name__ = "Unsigned32"
_CpmCoreIndex_Object = MibTableColumn
cpmCoreIndex = _CpmCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 1),
    _CpmCoreIndex_Type()
)
cpmCoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCoreIndex.setStatus("current")
_CpmCorePhysicalIndex_Type = EntPhysicalIndexOrZero
_CpmCorePhysicalIndex_Object = MibTableColumn
cpmCorePhysicalIndex = _CpmCorePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 2),
    _CpmCorePhysicalIndex_Type()
)
cpmCorePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCorePhysicalIndex.setStatus("current")


class _CpmCore5sec_Type(Gauge32):
    """Custom type cpmCore5sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCore5sec_Type.__name__ = "Gauge32"
_CpmCore5sec_Object = MibTableColumn
cpmCore5sec = _CpmCore5sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 3),
    _CpmCore5sec_Type()
)
cpmCore5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCore5sec.setStatus("current")


class _CpmCore1min_Type(Gauge32):
    """Custom type cpmCore1min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCore1min_Type.__name__ = "Gauge32"
_CpmCore1min_Object = MibTableColumn
cpmCore1min = _CpmCore1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 4),
    _CpmCore1min_Type()
)
cpmCore1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCore1min.setStatus("current")


class _CpmCore5min_Type(Gauge32):
    """Custom type cpmCore5min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCore5min_Type.__name__ = "Gauge32"
_CpmCore5min_Object = MibTableColumn
cpmCore5min = _CpmCore5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 5),
    _CpmCore5min_Type()
)
cpmCore5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCore5min.setStatus("current")
_CpmCoreLoadAvg1min_Type = CPULoadAverage
_CpmCoreLoadAvg1min_Object = MibTableColumn
cpmCoreLoadAvg1min = _CpmCoreLoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 6),
    _CpmCoreLoadAvg1min_Type()
)
cpmCoreLoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCoreLoadAvg1min.setStatus("current")
if mibBuilder.loadTexts:
    cpmCoreLoadAvg1min.setUnits("hundredths of processes")
_CpmCoreLoadAvg5min_Type = CPULoadAverage
_CpmCoreLoadAvg5min_Object = MibTableColumn
cpmCoreLoadAvg5min = _CpmCoreLoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 7),
    _CpmCoreLoadAvg5min_Type()
)
cpmCoreLoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCoreLoadAvg5min.setStatus("current")
if mibBuilder.loadTexts:
    cpmCoreLoadAvg5min.setUnits("hundredths of processes")
_CpmCoreLoadAvg15min_Type = CPULoadAverage
_CpmCoreLoadAvg15min_Object = MibTableColumn
cpmCoreLoadAvg15min = _CpmCoreLoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 1, 2, 1, 8),
    _CpmCoreLoadAvg15min_Type()
)
cpmCoreLoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCoreLoadAvg15min.setStatus("current")
if mibBuilder.loadTexts:
    cpmCoreLoadAvg15min.setUnits("hundredths of processes")
_CpmProcess_ObjectIdentity = ObjectIdentity
cpmProcess = _CpmProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2)
)
_CpmProcessTable_Object = MibTable
cpmProcessTable = _CpmProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpmProcessTable.setStatus("current")
_CpmProcessEntry_Object = MibTableRow
cpmProcessEntry = _CpmProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 1, 1)
)
cpmProcessEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmProcessPID"),
)
if mibBuilder.loadTexts:
    cpmProcessEntry.setStatus("current")
_CpmProcessPID_Type = Unsigned32
_CpmProcessPID_Object = MibTableColumn
cpmProcessPID = _CpmProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 1, 1, 1),
    _CpmProcessPID_Type()
)
cpmProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessPID.setStatus("current")


class _CpmProcessName_Type(DisplayString):
    """Custom type cpmProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CpmProcessName_Type.__name__ = "DisplayString"
_CpmProcessName_Object = MibTableColumn
cpmProcessName = _CpmProcessName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 1, 1, 2),
    _CpmProcessName_Type()
)
cpmProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessName.setStatus("current")
_CpmProcessuSecs_Type = Unsigned32
_CpmProcessuSecs_Object = MibTableColumn
cpmProcessuSecs = _CpmProcessuSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 1, 1, 4),
    _CpmProcessuSecs_Type()
)
cpmProcessuSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessuSecs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cpmProcessuSecs.setUnits("microseconds")
_CpmProcessTimeCreated_Type = TimeStamp
_CpmProcessTimeCreated_Object = MibTableColumn
cpmProcessTimeCreated = _CpmProcessTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 1, 1, 5),
    _CpmProcessTimeCreated_Type()
)
cpmProcessTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessTimeCreated.setStatus("current")
_CpmProcessAverageUSecs_Type = Unsigned32
_CpmProcessAverageUSecs_Object = MibTableColumn
cpmProcessAverageUSecs = _CpmProcessAverageUSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 1, 1, 6),
    _CpmProcessAverageUSecs_Type()
)
cpmProcessAverageUSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessAverageUSecs.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessAverageUSecs.setUnits("microseconds")
_CpmProcessExtTable_Object = MibTable
cpmProcessExtTable = _CpmProcessExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpmProcessExtTable.setStatus("deprecated")
_CpmProcessExtEntry_Object = MibTableRow
cpmProcessExtEntry = _CpmProcessExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpmProcessExtEntry.setStatus("deprecated")
_CpmProcExtMemAllocated_Type = Gauge32
_CpmProcExtMemAllocated_Object = MibTableColumn
cpmProcExtMemAllocated = _CpmProcExtMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 1),
    _CpmProcExtMemAllocated_Type()
)
cpmProcExtMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtMemAllocated.setStatus("deprecated")
if mibBuilder.loadTexts:
    cpmProcExtMemAllocated.setUnits("bytes")
_CpmProcExtMemFreed_Type = Gauge32
_CpmProcExtMemFreed_Object = MibTableColumn
cpmProcExtMemFreed = _CpmProcExtMemFreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 2),
    _CpmProcExtMemFreed_Type()
)
cpmProcExtMemFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtMemFreed.setStatus("deprecated")
if mibBuilder.loadTexts:
    cpmProcExtMemFreed.setUnits("bytes")
_CpmProcExtInvoked_Type = Counter32
_CpmProcExtInvoked_Object = MibTableColumn
cpmProcExtInvoked = _CpmProcExtInvoked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 3),
    _CpmProcExtInvoked_Type()
)
cpmProcExtInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtInvoked.setStatus("deprecated")
_CpmProcExtRuntime_Type = Counter32
_CpmProcExtRuntime_Object = MibTableColumn
cpmProcExtRuntime = _CpmProcExtRuntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 4),
    _CpmProcExtRuntime_Type()
)
cpmProcExtRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtRuntime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cpmProcExtRuntime.setUnits("microseconds")


class _CpmProcExtUtil5Sec_Type(Gauge32):
    """Custom type cpmProcExtUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmProcExtUtil5Sec_Type.__name__ = "Gauge32"
_CpmProcExtUtil5Sec_Object = MibTableColumn
cpmProcExtUtil5Sec = _CpmProcExtUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 5),
    _CpmProcExtUtil5Sec_Type()
)
cpmProcExtUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtUtil5Sec.setStatus("deprecated")


class _CpmProcExtUtil1Min_Type(Gauge32):
    """Custom type cpmProcExtUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmProcExtUtil1Min_Type.__name__ = "Gauge32"
_CpmProcExtUtil1Min_Object = MibTableColumn
cpmProcExtUtil1Min = _CpmProcExtUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 6),
    _CpmProcExtUtil1Min_Type()
)
cpmProcExtUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtUtil1Min.setStatus("deprecated")


class _CpmProcExtUtil5Min_Type(Gauge32):
    """Custom type cpmProcExtUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmProcExtUtil5Min_Type.__name__ = "Gauge32"
_CpmProcExtUtil5Min_Object = MibTableColumn
cpmProcExtUtil5Min = _CpmProcExtUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 7),
    _CpmProcExtUtil5Min_Type()
)
cpmProcExtUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtUtil5Min.setStatus("deprecated")


class _CpmProcExtPriority_Type(Integer32):
    """Custom type cpmProcExtPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 4),
          ("normal", 3),
          ("notAssigned", 5))
    )


_CpmProcExtPriority_Type.__name__ = "Integer32"
_CpmProcExtPriority_Object = MibTableColumn
cpmProcExtPriority = _CpmProcExtPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 2, 1, 8),
    _CpmProcExtPriority_Type()
)
cpmProcExtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmProcExtPriority.setStatus("deprecated")
_CpmProcessExtRevTable_Object = MibTable
cpmProcessExtRevTable = _CpmProcessExtRevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cpmProcessExtRevTable.setStatus("current")
_CpmProcessExtRevEntry_Object = MibTableRow
cpmProcessExtRevEntry = _CpmProcessExtRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1)
)
cpmProcessExtRevEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmProcessPID"),
)
if mibBuilder.loadTexts:
    cpmProcessExtRevEntry.setStatus("current")
_CpmProcExtMemAllocatedRev_Type = Gauge32
_CpmProcExtMemAllocatedRev_Object = MibTableColumn
cpmProcExtMemAllocatedRev = _CpmProcExtMemAllocatedRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 1),
    _CpmProcExtMemAllocatedRev_Type()
)
cpmProcExtMemAllocatedRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtMemAllocatedRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtMemAllocatedRev.setUnits("bytes")
_CpmProcExtMemFreedRev_Type = Gauge32
_CpmProcExtMemFreedRev_Object = MibTableColumn
cpmProcExtMemFreedRev = _CpmProcExtMemFreedRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 2),
    _CpmProcExtMemFreedRev_Type()
)
cpmProcExtMemFreedRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtMemFreedRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtMemFreedRev.setUnits("bytes")
_CpmProcExtInvokedRev_Type = Counter32
_CpmProcExtInvokedRev_Object = MibTableColumn
cpmProcExtInvokedRev = _CpmProcExtInvokedRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 3),
    _CpmProcExtInvokedRev_Type()
)
cpmProcExtInvokedRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtInvokedRev.setStatus("current")
_CpmProcExtRuntimeRev_Type = Counter32
_CpmProcExtRuntimeRev_Object = MibTableColumn
cpmProcExtRuntimeRev = _CpmProcExtRuntimeRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 4),
    _CpmProcExtRuntimeRev_Type()
)
cpmProcExtRuntimeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtRuntimeRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtRuntimeRev.setUnits("microseconds")


class _CpmProcExtUtil5SecRev_Type(Gauge32):
    """Custom type cpmProcExtUtil5SecRev based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmProcExtUtil5SecRev_Type.__name__ = "Gauge32"
_CpmProcExtUtil5SecRev_Object = MibTableColumn
cpmProcExtUtil5SecRev = _CpmProcExtUtil5SecRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 5),
    _CpmProcExtUtil5SecRev_Type()
)
cpmProcExtUtil5SecRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtUtil5SecRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtUtil5SecRev.setUnits("percent")


class _CpmProcExtUtil1MinRev_Type(Gauge32):
    """Custom type cpmProcExtUtil1MinRev based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmProcExtUtil1MinRev_Type.__name__ = "Gauge32"
_CpmProcExtUtil1MinRev_Object = MibTableColumn
cpmProcExtUtil1MinRev = _CpmProcExtUtil1MinRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 6),
    _CpmProcExtUtil1MinRev_Type()
)
cpmProcExtUtil1MinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtUtil1MinRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtUtil1MinRev.setUnits("percent")


class _CpmProcExtUtil5MinRev_Type(Gauge32):
    """Custom type cpmProcExtUtil5MinRev based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmProcExtUtil5MinRev_Type.__name__ = "Gauge32"
_CpmProcExtUtil5MinRev_Object = MibTableColumn
cpmProcExtUtil5MinRev = _CpmProcExtUtil5MinRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 7),
    _CpmProcExtUtil5MinRev_Type()
)
cpmProcExtUtil5MinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtUtil5MinRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtUtil5MinRev.setUnits("percent")


class _CpmProcExtPriorityRev_Type(Integer32):
    """Custom type cpmProcExtPriorityRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 4),
          ("normal", 3),
          ("notAssigned", 5))
    )


_CpmProcExtPriorityRev_Type.__name__ = "Integer32"
_CpmProcExtPriorityRev_Object = MibTableColumn
cpmProcExtPriorityRev = _CpmProcExtPriorityRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 8),
    _CpmProcExtPriorityRev_Type()
)
cpmProcExtPriorityRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtPriorityRev.setStatus("current")


class _CpmProcessType_Type(Integer32):
    """Custom type cpmProcessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ios", 3),
          ("other", 1),
          ("posix", 2))
    )


_CpmProcessType_Type.__name__ = "Integer32"
_CpmProcessType_Object = MibTableColumn
cpmProcessType = _CpmProcessType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 9),
    _CpmProcessType_Type()
)
cpmProcessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessType.setStatus("current")
_CpmProcessRespawn_Type = TruthValue
_CpmProcessRespawn_Object = MibTableColumn
cpmProcessRespawn = _CpmProcessRespawn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 10),
    _CpmProcessRespawn_Type()
)
cpmProcessRespawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessRespawn.setStatus("current")
_CpmProcessRespawnCount_Type = Counter32
_CpmProcessRespawnCount_Object = MibTableColumn
cpmProcessRespawnCount = _CpmProcessRespawnCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 11),
    _CpmProcessRespawnCount_Type()
)
cpmProcessRespawnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessRespawnCount.setStatus("current")
_CpmProcessRespawnAfterLastPatch_Type = Counter32
_CpmProcessRespawnAfterLastPatch_Object = MibTableColumn
cpmProcessRespawnAfterLastPatch = _CpmProcessRespawnAfterLastPatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 12),
    _CpmProcessRespawnAfterLastPatch_Type()
)
cpmProcessRespawnAfterLastPatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessRespawnAfterLastPatch.setStatus("current")


class _CpmProcessMemoryCore_Type(Integer32):
    """Custom type cpmProcessMemoryCore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("mainmem", 2),
          ("mainmemSharedmem", 3),
          ("mainmemText", 4),
          ("mainmemTextSharedmem", 5),
          ("off", 8),
          ("other", 1),
          ("sharedmem", 6),
          ("sparse", 7))
    )


_CpmProcessMemoryCore_Type.__name__ = "Integer32"
_CpmProcessMemoryCore_Object = MibTableColumn
cpmProcessMemoryCore = _CpmProcessMemoryCore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 13),
    _CpmProcessMemoryCore_Type()
)
cpmProcessMemoryCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessMemoryCore.setStatus("current")
_CpmProcessLastRestartUser_Type = SnmpAdminString
_CpmProcessLastRestartUser_Object = MibTableColumn
cpmProcessLastRestartUser = _CpmProcessLastRestartUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 14),
    _CpmProcessLastRestartUser_Type()
)
cpmProcessLastRestartUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessLastRestartUser.setStatus("current")
_CpmProcessTextSegmentSize_Type = Unsigned32
_CpmProcessTextSegmentSize_Object = MibTableColumn
cpmProcessTextSegmentSize = _CpmProcessTextSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 15),
    _CpmProcessTextSegmentSize_Type()
)
cpmProcessTextSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessTextSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessTextSegmentSize.setUnits("kilo-bytes")
_CpmProcessDataSegmentSize_Type = Gauge32
_CpmProcessDataSegmentSize_Object = MibTableColumn
cpmProcessDataSegmentSize = _CpmProcessDataSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 16),
    _CpmProcessDataSegmentSize_Type()
)
cpmProcessDataSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessDataSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessDataSegmentSize.setUnits("kilo-bytes")
_CpmProcessStackSize_Type = Gauge32
_CpmProcessStackSize_Object = MibTableColumn
cpmProcessStackSize = _CpmProcessStackSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 17),
    _CpmProcessStackSize_Type()
)
cpmProcessStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessStackSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessStackSize.setUnits("kilo-bytes")
_CpmProcessDynamicMemorySize_Type = Gauge32
_CpmProcessDynamicMemorySize_Object = MibTableColumn
cpmProcessDynamicMemorySize = _CpmProcessDynamicMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 18),
    _CpmProcessDynamicMemorySize_Type()
)
cpmProcessDynamicMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessDynamicMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessDynamicMemorySize.setUnits("kilo-bytes")
_CpmProcExtMemAllocatedRevOvrflw_Type = Gauge32
_CpmProcExtMemAllocatedRevOvrflw_Object = MibTableColumn
cpmProcExtMemAllocatedRevOvrflw = _CpmProcExtMemAllocatedRevOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 19),
    _CpmProcExtMemAllocatedRevOvrflw_Type()
)
cpmProcExtMemAllocatedRevOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtMemAllocatedRevOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtMemAllocatedRevOvrflw.setUnits("bytes")
_CpmProcExtHCMemAllocatedRev_Type = CounterBasedGauge64
_CpmProcExtHCMemAllocatedRev_Object = MibTableColumn
cpmProcExtHCMemAllocatedRev = _CpmProcExtHCMemAllocatedRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 20),
    _CpmProcExtHCMemAllocatedRev_Type()
)
cpmProcExtHCMemAllocatedRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtHCMemAllocatedRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtHCMemAllocatedRev.setUnits("bytes")
_CpmProcExtMemFreedRevOvrflw_Type = Gauge32
_CpmProcExtMemFreedRevOvrflw_Object = MibTableColumn
cpmProcExtMemFreedRevOvrflw = _CpmProcExtMemFreedRevOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 21),
    _CpmProcExtMemFreedRevOvrflw_Type()
)
cpmProcExtMemFreedRevOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtMemFreedRevOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtMemFreedRevOvrflw.setUnits("bytes")
_CpmProcExtHCMemFreedRev_Type = CounterBasedGauge64
_CpmProcExtHCMemFreedRev_Object = MibTableColumn
cpmProcExtHCMemFreedRev = _CpmProcExtHCMemFreedRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 22),
    _CpmProcExtHCMemFreedRev_Type()
)
cpmProcExtHCMemFreedRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcExtHCMemFreedRev.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcExtHCMemFreedRev.setUnits("bytes")
_CpmProcessTextSegmentSizeOvrflw_Type = Unsigned32
_CpmProcessTextSegmentSizeOvrflw_Object = MibTableColumn
cpmProcessTextSegmentSizeOvrflw = _CpmProcessTextSegmentSizeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 23),
    _CpmProcessTextSegmentSizeOvrflw_Type()
)
cpmProcessTextSegmentSizeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessTextSegmentSizeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessTextSegmentSizeOvrflw.setUnits("kilo-bytes")
_CpmProcessHCTextSegmentSize_Type = Unsigned64
_CpmProcessHCTextSegmentSize_Object = MibTableColumn
cpmProcessHCTextSegmentSize = _CpmProcessHCTextSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 24),
    _CpmProcessHCTextSegmentSize_Type()
)
cpmProcessHCTextSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessHCTextSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessHCTextSegmentSize.setUnits("kilo-bytes")
_CpmProcessDataSegmentSizeOvrflw_Type = Gauge32
_CpmProcessDataSegmentSizeOvrflw_Object = MibTableColumn
cpmProcessDataSegmentSizeOvrflw = _CpmProcessDataSegmentSizeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 25),
    _CpmProcessDataSegmentSizeOvrflw_Type()
)
cpmProcessDataSegmentSizeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessDataSegmentSizeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessDataSegmentSizeOvrflw.setUnits("kilo-bytes")
_CpmProcessHCDataSegmentSize_Type = CounterBasedGauge64
_CpmProcessHCDataSegmentSize_Object = MibTableColumn
cpmProcessHCDataSegmentSize = _CpmProcessHCDataSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 26),
    _CpmProcessHCDataSegmentSize_Type()
)
cpmProcessHCDataSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessHCDataSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessHCDataSegmentSize.setUnits("kilo-bytes")
_CpmProcessStackSizeOvrflw_Type = Gauge32
_CpmProcessStackSizeOvrflw_Object = MibTableColumn
cpmProcessStackSizeOvrflw = _CpmProcessStackSizeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 27),
    _CpmProcessStackSizeOvrflw_Type()
)
cpmProcessStackSizeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessStackSizeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessStackSizeOvrflw.setUnits("kilo-bytes")
_CpmProcessHCStackSize_Type = CounterBasedGauge64
_CpmProcessHCStackSize_Object = MibTableColumn
cpmProcessHCStackSize = _CpmProcessHCStackSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 28),
    _CpmProcessHCStackSize_Type()
)
cpmProcessHCStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessHCStackSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessHCStackSize.setUnits("kilo-bytes")
_CpmProcessDynamicMemorySizeOvrflw_Type = Gauge32
_CpmProcessDynamicMemorySizeOvrflw_Object = MibTableColumn
cpmProcessDynamicMemorySizeOvrflw = _CpmProcessDynamicMemorySizeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 29),
    _CpmProcessDynamicMemorySizeOvrflw_Type()
)
cpmProcessDynamicMemorySizeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessDynamicMemorySizeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessDynamicMemorySizeOvrflw.setUnits("kilo-bytes")
_CpmProcessHCDynamicMemorySize_Type = CounterBasedGauge64
_CpmProcessHCDynamicMemorySize_Object = MibTableColumn
cpmProcessHCDynamicMemorySize = _CpmProcessHCDynamicMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 3, 1, 30),
    _CpmProcessHCDynamicMemorySize_Type()
)
cpmProcessHCDynamicMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmProcessHCDynamicMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    cpmProcessHCDynamicMemorySize.setUnits("kilo-bytes")
_CpmCPUThresholdTable_Object = MibTable
cpmCPUThresholdTable = _CpmCPUThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cpmCPUThresholdTable.setStatus("current")
_CpmCPUThresholdEntry_Object = MibTableRow
cpmCPUThresholdEntry = _CpmCPUThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4, 1)
)
cpmCPUThresholdEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmCPUThresholdClass"),
)
if mibBuilder.loadTexts:
    cpmCPUThresholdEntry.setStatus("current")


class _CpmCPUThresholdClass_Type(Integer32):
    """Custom type cpmCPUThresholdClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interrupt", 2),
          ("process", 3),
          ("total", 1))
    )


_CpmCPUThresholdClass_Type.__name__ = "Integer32"
_CpmCPUThresholdClass_Object = MibTableColumn
cpmCPUThresholdClass = _CpmCPUThresholdClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4, 1, 1),
    _CpmCPUThresholdClass_Type()
)
cpmCPUThresholdClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCPUThresholdClass.setStatus("current")


class _CpmCPURisingThresholdValue_Type(Unsigned32):
    """Custom type cpmCPURisingThresholdValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmCPURisingThresholdValue_Type.__name__ = "Unsigned32"
_CpmCPURisingThresholdValue_Object = MibTableColumn
cpmCPURisingThresholdValue = _CpmCPURisingThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4, 1, 2),
    _CpmCPURisingThresholdValue_Type()
)
cpmCPURisingThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpmCPURisingThresholdValue.setStatus("current")


class _CpmCPURisingThresholdPeriod_Type(Unsigned32):
    """Custom type cpmCPURisingThresholdPeriod based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 4294967295),
    )


_CpmCPURisingThresholdPeriod_Type.__name__ = "Unsigned32"
_CpmCPURisingThresholdPeriod_Object = MibTableColumn
cpmCPURisingThresholdPeriod = _CpmCPURisingThresholdPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4, 1, 3),
    _CpmCPURisingThresholdPeriod_Type()
)
cpmCPURisingThresholdPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpmCPURisingThresholdPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPURisingThresholdPeriod.setUnits("seconds")


class _CpmCPUFallingThresholdValue_Type(Unsigned32):
    """Custom type cpmCPUFallingThresholdValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmCPUFallingThresholdValue_Type.__name__ = "Unsigned32"
_CpmCPUFallingThresholdValue_Object = MibTableColumn
cpmCPUFallingThresholdValue = _CpmCPUFallingThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4, 1, 4),
    _CpmCPUFallingThresholdValue_Type()
)
cpmCPUFallingThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpmCPUFallingThresholdValue.setStatus("current")


class _CpmCPUFallingThresholdPeriod_Type(Unsigned32):
    """Custom type cpmCPUFallingThresholdPeriod based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 4294967295),
    )


_CpmCPUFallingThresholdPeriod_Type.__name__ = "Unsigned32"
_CpmCPUFallingThresholdPeriod_Object = MibTableColumn
cpmCPUFallingThresholdPeriod = _CpmCPUFallingThresholdPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4, 1, 5),
    _CpmCPUFallingThresholdPeriod_Type()
)
cpmCPUFallingThresholdPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpmCPUFallingThresholdPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUFallingThresholdPeriod.setUnits("seconds")
_CpmCPUThresholdEntryStatus_Type = RowStatus
_CpmCPUThresholdEntryStatus_Object = MibTableColumn
cpmCPUThresholdEntryStatus = _CpmCPUThresholdEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 4, 1, 6),
    _CpmCPUThresholdEntryStatus_Type()
)
cpmCPUThresholdEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpmCPUThresholdEntryStatus.setStatus("current")
_CpmCPUHistory_ObjectIdentity = ObjectIdentity
cpmCPUHistory = _CpmCPUHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5)
)


class _CpmCPUHistoryThreshold_Type(Unsigned32):
    """Custom type cpmCPUHistoryThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmCPUHistoryThreshold_Type.__name__ = "Unsigned32"
_CpmCPUHistoryThreshold_Object = MibScalar
cpmCPUHistoryThreshold = _CpmCPUHistoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 1),
    _CpmCPUHistoryThreshold_Type()
)
cpmCPUHistoryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmCPUHistoryThreshold.setStatus("current")


class _CpmCPUHistorySize_Type(Unsigned32):
    """Custom type cpmCPUHistorySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpmCPUHistorySize_Type.__name__ = "Unsigned32"
_CpmCPUHistorySize_Object = MibScalar
cpmCPUHistorySize = _CpmCPUHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 2),
    _CpmCPUHistorySize_Type()
)
cpmCPUHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmCPUHistorySize.setStatus("current")
_CpmCPUHistoryTable_Object = MibTable
cpmCPUHistoryTable = _CpmCPUHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    cpmCPUHistoryTable.setStatus("current")
_CpmCPUHistoryEntry_Object = MibTableRow
cpmCPUHistoryEntry = _CpmCPUHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 3, 1)
)
cpmCPUHistoryEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmCPUHistoryReportId"),
)
if mibBuilder.loadTexts:
    cpmCPUHistoryEntry.setStatus("current")
_CpmCPUHistoryReportId_Type = Unsigned32
_CpmCPUHistoryReportId_Object = MibTableColumn
cpmCPUHistoryReportId = _CpmCPUHistoryReportId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 3, 1, 1),
    _CpmCPUHistoryReportId_Type()
)
cpmCPUHistoryReportId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCPUHistoryReportId.setStatus("current")


class _CpmCPUHistoryReportSize_Type(Unsigned32):
    """Custom type cpmCPUHistoryReportSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpmCPUHistoryReportSize_Type.__name__ = "Unsigned32"
_CpmCPUHistoryReportSize_Object = MibTableColumn
cpmCPUHistoryReportSize = _CpmCPUHistoryReportSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 3, 1, 2),
    _CpmCPUHistoryReportSize_Type()
)
cpmCPUHistoryReportSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryReportSize.setStatus("current")


class _CpmCPUHistoryTotalUtil_Type(Gauge32):
    """Custom type cpmCPUHistoryTotalUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUHistoryTotalUtil_Type.__name__ = "Gauge32"
_CpmCPUHistoryTotalUtil_Object = MibTableColumn
cpmCPUHistoryTotalUtil = _CpmCPUHistoryTotalUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 3, 1, 3),
    _CpmCPUHistoryTotalUtil_Type()
)
cpmCPUHistoryTotalUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryTotalUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUHistoryTotalUtil.setUnits("percent")


class _CpmCPUHistoryInterruptUtil_Type(Gauge32):
    """Custom type cpmCPUHistoryInterruptUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUHistoryInterruptUtil_Type.__name__ = "Gauge32"
_CpmCPUHistoryInterruptUtil_Object = MibTableColumn
cpmCPUHistoryInterruptUtil = _CpmCPUHistoryInterruptUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 3, 1, 4),
    _CpmCPUHistoryInterruptUtil_Type()
)
cpmCPUHistoryInterruptUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryInterruptUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUHistoryInterruptUtil.setUnits("percent")
_CpmCPUHistoryCreatedTime_Type = TimeStamp
_CpmCPUHistoryCreatedTime_Object = MibTableColumn
cpmCPUHistoryCreatedTime = _CpmCPUHistoryCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 3, 1, 5),
    _CpmCPUHistoryCreatedTime_Type()
)
cpmCPUHistoryCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryCreatedTime.setStatus("current")
_CpmCPUProcessHistoryTable_Object = MibTable
cpmCPUProcessHistoryTable = _CpmCPUProcessHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    cpmCPUProcessHistoryTable.setStatus("current")
_CpmCPUProcessHistoryEntry_Object = MibTableRow
cpmCPUProcessHistoryEntry = _CpmCPUProcessHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 4, 1)
)
cpmCPUProcessHistoryEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmCPUHistoryReportId"),
    (0, "CISCO-PROCESS-MIB", "cpmCPUProcessHistoryIndex"),
)
if mibBuilder.loadTexts:
    cpmCPUProcessHistoryEntry.setStatus("current")


class _CpmCPUProcessHistoryIndex_Type(Unsigned32):
    """Custom type cpmCPUProcessHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpmCPUProcessHistoryIndex_Type.__name__ = "Unsigned32"
_CpmCPUProcessHistoryIndex_Object = MibTableColumn
cpmCPUProcessHistoryIndex = _CpmCPUProcessHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 4, 1, 1),
    _CpmCPUProcessHistoryIndex_Type()
)
cpmCPUProcessHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCPUProcessHistoryIndex.setStatus("current")


class _CpmCPUHistoryProcId_Type(Unsigned32):
    """Custom type cpmCPUHistoryProcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpmCPUHistoryProcId_Type.__name__ = "Unsigned32"
_CpmCPUHistoryProcId_Object = MibTableColumn
cpmCPUHistoryProcId = _CpmCPUHistoryProcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 4, 1, 2),
    _CpmCPUHistoryProcId_Type()
)
cpmCPUHistoryProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryProcId.setStatus("current")
_CpmCPUHistoryProcName_Type = DisplayString
_CpmCPUHistoryProcName_Object = MibTableColumn
cpmCPUHistoryProcName = _CpmCPUHistoryProcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 4, 1, 3),
    _CpmCPUHistoryProcName_Type()
)
cpmCPUHistoryProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryProcName.setStatus("current")
_CpmCPUHistoryProcCreated_Type = TimeStamp
_CpmCPUHistoryProcCreated_Object = MibTableColumn
cpmCPUHistoryProcCreated = _CpmCPUHistoryProcCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 4, 1, 4),
    _CpmCPUHistoryProcCreated_Type()
)
cpmCPUHistoryProcCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryProcCreated.setStatus("current")


class _CpmCPUHistoryProcUtil_Type(Gauge32):
    """Custom type cpmCPUHistoryProcUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmCPUHistoryProcUtil_Type.__name__ = "Gauge32"
_CpmCPUHistoryProcUtil_Object = MibTableColumn
cpmCPUHistoryProcUtil = _CpmCPUHistoryProcUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 2, 5, 4, 1, 5),
    _CpmCPUHistoryProcUtil_Type()
)
cpmCPUHistoryProcUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCPUHistoryProcUtil.setStatus("current")
if mibBuilder.loadTexts:
    cpmCPUHistoryProcUtil.setUnits("percent")
_CpmThread_ObjectIdentity = ObjectIdentity
cpmThread = _CpmThread_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3)
)
_CpmThreadTable_Object = MibTable
cpmThreadTable = _CpmThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cpmThreadTable.setStatus("current")
_CpmThreadEntry_Object = MibTableRow
cpmThreadEntry = _CpmThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1)
)
cpmThreadEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmProcessPID"),
    (0, "CISCO-PROCESS-MIB", "cpmThreadID"),
)
if mibBuilder.loadTexts:
    cpmThreadEntry.setStatus("current")
_CpmThreadID_Type = Unsigned32
_CpmThreadID_Object = MibTableColumn
cpmThreadID = _CpmThreadID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 1),
    _CpmThreadID_Type()
)
cpmThreadID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmThreadID.setStatus("current")
_CpmThreadName_Type = SnmpAdminString
_CpmThreadName_Object = MibTableColumn
cpmThreadName = _CpmThreadName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 2),
    _CpmThreadName_Type()
)
cpmThreadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadName.setStatus("current")


class _CpmThreadPriority_Type(Unsigned32):
    """Custom type cpmThreadPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CpmThreadPriority_Type.__name__ = "Unsigned32"
_CpmThreadPriority_Object = MibTableColumn
cpmThreadPriority = _CpmThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 3),
    _CpmThreadPriority_Type()
)
cpmThreadPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadPriority.setStatus("current")


class _CpmThreadState_Type(Integer32):
    """Custom type cpmThreadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("condvar", 15),
          ("dead", 2),
          ("intr", 17),
          ("join", 16),
          ("mutex", 14),
          ("nanosleep", 13),
          ("other", 1),
          ("ready", 4),
          ("receive", 7),
          ("reply", 8),
          ("running", 3),
          ("sem", 18),
          ("send", 6),
          ("sigsuspend", 11),
          ("sigwaitinfo", 12),
          ("stack", 9),
          ("stopped", 5),
          ("waitpage", 10))
    )


_CpmThreadState_Type.__name__ = "Integer32"
_CpmThreadState_Object = MibTableColumn
cpmThreadState = _CpmThreadState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 4),
    _CpmThreadState_Type()
)
cpmThreadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadState.setStatus("current")
_CpmThreadBlockingProcess_Type = RowPointer
_CpmThreadBlockingProcess_Object = MibTableColumn
cpmThreadBlockingProcess = _CpmThreadBlockingProcess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 5),
    _CpmThreadBlockingProcess_Type()
)
cpmThreadBlockingProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadBlockingProcess.setStatus("current")
_CpmThreadCpuUtilization_Type = Gauge32
_CpmThreadCpuUtilization_Object = MibTableColumn
cpmThreadCpuUtilization = _CpmThreadCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 6),
    _CpmThreadCpuUtilization_Type()
)
cpmThreadCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cpmThreadCpuUtilization.setUnits("milliseconds")
_CpmThreadStackSize_Type = Gauge32
_CpmThreadStackSize_Object = MibTableColumn
cpmThreadStackSize = _CpmThreadStackSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 7),
    _CpmThreadStackSize_Type()
)
cpmThreadStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadStackSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmThreadStackSize.setUnits("bytes")
_CpmThreadStackSizeOvrflw_Type = Gauge32
_CpmThreadStackSizeOvrflw_Object = MibTableColumn
cpmThreadStackSizeOvrflw = _CpmThreadStackSizeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 8),
    _CpmThreadStackSizeOvrflw_Type()
)
cpmThreadStackSizeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadStackSizeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmThreadStackSizeOvrflw.setUnits("bytes")
_CpmThreadHCStackSize_Type = CounterBasedGauge64
_CpmThreadHCStackSize_Object = MibTableColumn
cpmThreadHCStackSize = _CpmThreadHCStackSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 3, 1, 1, 9),
    _CpmThreadHCStackSize_Type()
)
cpmThreadHCStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmThreadHCStackSize.setStatus("current")
if mibBuilder.loadTexts:
    cpmThreadHCStackSize.setUnits("bytes")
_CpmVirtualProcess_ObjectIdentity = ObjectIdentity
cpmVirtualProcess = _CpmVirtualProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4)
)
_CpmVirtualProcessTable_Object = MibTable
cpmVirtualProcessTable = _CpmVirtualProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cpmVirtualProcessTable.setStatus("current")
_CpmVirtualProcessEntry_Object = MibTableRow
cpmVirtualProcessEntry = _CpmVirtualProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1)
)
cpmVirtualProcessEntry.setIndexNames(
    (0, "CISCO-PROCESS-MIB", "cpmCPUTotalIndex"),
    (0, "CISCO-PROCESS-MIB", "cpmProcessPID"),
    (0, "CISCO-PROCESS-MIB", "cpmVirtualProcessID"),
)
if mibBuilder.loadTexts:
    cpmVirtualProcessEntry.setStatus("current")
_CpmVirtualProcessID_Type = Unsigned32
_CpmVirtualProcessID_Object = MibTableColumn
cpmVirtualProcessID = _CpmVirtualProcessID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 1),
    _CpmVirtualProcessID_Type()
)
cpmVirtualProcessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmVirtualProcessID.setStatus("current")


class _CpmVirtualProcessName_Type(SnmpAdminString):
    """Custom type cpmVirtualProcessName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CpmVirtualProcessName_Type.__name__ = "SnmpAdminString"
_CpmVirtualProcessName_Object = MibTableColumn
cpmVirtualProcessName = _CpmVirtualProcessName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 2),
    _CpmVirtualProcessName_Type()
)
cpmVirtualProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessName.setStatus("current")


class _CpmVirtualProcessUtil5Sec_Type(Gauge32):
    """Custom type cpmVirtualProcessUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmVirtualProcessUtil5Sec_Type.__name__ = "Gauge32"
_CpmVirtualProcessUtil5Sec_Object = MibTableColumn
cpmVirtualProcessUtil5Sec = _CpmVirtualProcessUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 3),
    _CpmVirtualProcessUtil5Sec_Type()
)
cpmVirtualProcessUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessUtil5Sec.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessUtil5Sec.setUnits("percent")


class _CpmVirtualProcessUtil1Min_Type(Gauge32):
    """Custom type cpmVirtualProcessUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmVirtualProcessUtil1Min_Type.__name__ = "Gauge32"
_CpmVirtualProcessUtil1Min_Object = MibTableColumn
cpmVirtualProcessUtil1Min = _CpmVirtualProcessUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 4),
    _CpmVirtualProcessUtil1Min_Type()
)
cpmVirtualProcessUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessUtil1Min.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessUtil1Min.setUnits("percent")


class _CpmVirtualProcessUtil5Min_Type(Gauge32):
    """Custom type cpmVirtualProcessUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmVirtualProcessUtil5Min_Type.__name__ = "Gauge32"
_CpmVirtualProcessUtil5Min_Object = MibTableColumn
cpmVirtualProcessUtil5Min = _CpmVirtualProcessUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 5),
    _CpmVirtualProcessUtil5Min_Type()
)
cpmVirtualProcessUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessUtil5Min.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessUtil5Min.setUnits("percent")
_CpmVirtualProcessMemAllocated_Type = Gauge32
_CpmVirtualProcessMemAllocated_Object = MibTableColumn
cpmVirtualProcessMemAllocated = _CpmVirtualProcessMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 6),
    _CpmVirtualProcessMemAllocated_Type()
)
cpmVirtualProcessMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemAllocated.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemAllocated.setUnits("bytes")
_CpmVirtualProcessMemFreed_Type = Gauge32
_CpmVirtualProcessMemFreed_Object = MibTableColumn
cpmVirtualProcessMemFreed = _CpmVirtualProcessMemFreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 7),
    _CpmVirtualProcessMemFreed_Type()
)
cpmVirtualProcessMemFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemFreed.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemFreed.setUnits("bytes")
_CpmVirtualProcessInvokeCount_Type = Counter32
_CpmVirtualProcessInvokeCount_Object = MibTableColumn
cpmVirtualProcessInvokeCount = _CpmVirtualProcessInvokeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 8),
    _CpmVirtualProcessInvokeCount_Type()
)
cpmVirtualProcessInvokeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessInvokeCount.setStatus("current")
_CpmVirtualProcessRuntime_Type = Counter32
_CpmVirtualProcessRuntime_Object = MibTableColumn
cpmVirtualProcessRuntime = _CpmVirtualProcessRuntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 9),
    _CpmVirtualProcessRuntime_Type()
)
cpmVirtualProcessRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessRuntime.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessRuntime.setUnits("microseconds")
_CpmVirtualProcessMemAllocatedOvrflw_Type = Gauge32
_CpmVirtualProcessMemAllocatedOvrflw_Object = MibTableColumn
cpmVirtualProcessMemAllocatedOvrflw = _CpmVirtualProcessMemAllocatedOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 10),
    _CpmVirtualProcessMemAllocatedOvrflw_Type()
)
cpmVirtualProcessMemAllocatedOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemAllocatedOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemAllocatedOvrflw.setUnits("bytes")
_CpmVirtualProcessHCMemAllocated_Type = CounterBasedGauge64
_CpmVirtualProcessHCMemAllocated_Object = MibTableColumn
cpmVirtualProcessHCMemAllocated = _CpmVirtualProcessHCMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 11),
    _CpmVirtualProcessHCMemAllocated_Type()
)
cpmVirtualProcessHCMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessHCMemAllocated.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessHCMemAllocated.setUnits("bytes")
_CpmVirtualProcessMemFreedOvrflw_Type = Gauge32
_CpmVirtualProcessMemFreedOvrflw_Object = MibTableColumn
cpmVirtualProcessMemFreedOvrflw = _CpmVirtualProcessMemFreedOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 12),
    _CpmVirtualProcessMemFreedOvrflw_Type()
)
cpmVirtualProcessMemFreedOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemFreedOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessMemFreedOvrflw.setUnits("bytes")
_CpmVirtualProcessHCMemFreed_Type = CounterBasedGauge64
_CpmVirtualProcessHCMemFreed_Object = MibTableColumn
cpmVirtualProcessHCMemFreed = _CpmVirtualProcessHCMemFreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 1, 4, 1, 1, 13),
    _CpmVirtualProcessHCMemFreed_Type()
)
cpmVirtualProcessHCMemFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVirtualProcessHCMemFreed.setStatus("current")
if mibBuilder.loadTexts:
    cpmVirtualProcessHCMemFreed.setUnits("bytes")
_CiscoProcessMIBNotifPrefix_ObjectIdentity = ObjectIdentity
ciscoProcessMIBNotifPrefix = _CiscoProcessMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 2)
)
_CiscoProcessMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoProcessMIBNotifs = _CiscoProcessMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 2, 0)
)
_CiscoProcessMIBConformance_ObjectIdentity = ObjectIdentity
ciscoProcessMIBConformance = _CiscoProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3)
)
_CpmCompliances_ObjectIdentity = ObjectIdentity
cpmCompliances = _CpmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1)
)
_CpmGroups_ObjectIdentity = ObjectIdentity
cpmGroups = _CpmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2)
)
cpmProcessEntry.registerAugmentions(
    ("CISCO-PROCESS-MIB",
     "cpmProcessExtEntry")
)
cpmProcessExtEntry.setIndexNames(*cpmProcessEntry.getIndexNames())

# Managed Objects groups

cpmCPUTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 1)
)
cpmCPUTotalGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUTotalPhysicalIndex"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal5sec"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal1min"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal5min"))
)
if mibBuilder.loadTexts:
    cpmCPUTotalGroup.setStatus("deprecated")

cpmProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 2)
)
cpmProcessGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmProcessPID"),
        ("CISCO-PROCESS-MIB", "cpmProcessName"),
        ("CISCO-PROCESS-MIB", "cpmProcessuSecs"),
        ("CISCO-PROCESS-MIB", "cpmProcessTimeCreated"))
)
if mibBuilder.loadTexts:
    cpmProcessGroup.setStatus("deprecated")

cpmProcessExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 3)
)
cpmProcessExtGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmProcExtMemAllocated"),
        ("CISCO-PROCESS-MIB", "cpmProcExtMemFreed"),
        ("CISCO-PROCESS-MIB", "cpmProcExtInvoked"),
        ("CISCO-PROCESS-MIB", "cpmProcExtRuntime"),
        ("CISCO-PROCESS-MIB", "cpmProcExtUtil5Sec"),
        ("CISCO-PROCESS-MIB", "cpmProcExtUtil1Min"),
        ("CISCO-PROCESS-MIB", "cpmProcExtUtil5Min"),
        ("CISCO-PROCESS-MIB", "cpmProcExtPriority"))
)
if mibBuilder.loadTexts:
    cpmProcessExtGroup.setStatus("deprecated")

cpmCPUTotalGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 4)
)
cpmCPUTotalGroupRev.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUTotalPhysicalIndex"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal5secRev"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal1minRev"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal5minRev"))
)
if mibBuilder.loadTexts:
    cpmCPUTotalGroupRev.setStatus("deprecated")

cpmProcessExtGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 5)
)
cpmProcessExtGroupRev.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmProcExtMemAllocatedRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtMemFreedRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtInvokedRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtRuntimeRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtUtil5SecRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtUtil1MinRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtUtil5MinRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtPriorityRev"))
)
if mibBuilder.loadTexts:
    cpmProcessExtGroupRev.setStatus("current")

cpmProcessGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 6)
)
cpmProcessGroupRev.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmProcessPID"),
        ("CISCO-PROCESS-MIB", "cpmProcessName"),
        ("CISCO-PROCESS-MIB", "cpmProcessAverageUSecs"),
        ("CISCO-PROCESS-MIB", "cpmProcessTimeCreated"))
)
if mibBuilder.loadTexts:
    cpmProcessGroupRev.setStatus("current")

cpmCPUTotalGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 7)
)
cpmCPUTotalGroupRev1.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUTotalPhysicalIndex"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal1minRev"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotal5minRev"),
        ("CISCO-PROCESS-MIB", "cpmCPUMonInterval"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotalMonIntervalValue"),
        ("CISCO-PROCESS-MIB", "cpmCPUInterruptMonIntervalValue"))
)
if mibBuilder.loadTexts:
    cpmCPUTotalGroupRev1.setStatus("current")

cpmCPUThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 8)
)
cpmCPUThresholdGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPURisingThresholdValue"),
        ("CISCO-PROCESS-MIB", "cpmCPURisingThresholdPeriod"),
        ("CISCO-PROCESS-MIB", "cpmCPUFallingThresholdValue"),
        ("CISCO-PROCESS-MIB", "cpmCPUFallingThresholdPeriod"),
        ("CISCO-PROCESS-MIB", "cpmCPUThresholdEntryStatus"))
)
if mibBuilder.loadTexts:
    cpmCPUThresholdGroup.setStatus("current")

cpmCPUHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 9)
)
cpmCPUHistoryGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUHistorySize"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryThreshold"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryTotalUtil"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryInterruptUtil"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryCreatedTime"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryReportSize"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryProcId"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryProcName"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryProcCreated"),
        ("CISCO-PROCESS-MIB", "cpmCPUHistoryProcUtil"))
)
if mibBuilder.loadTexts:
    cpmCPUHistoryGroup.setStatus("current")

cpmCPUPosixMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 11)
)
cpmCPUPosixMemoryGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUMemoryUsed"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryFree"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryKernelReserved"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryLowest"))
)
if mibBuilder.loadTexts:
    cpmCPUPosixMemoryGroup.setStatus("current")

cpmPosixProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 12)
)
cpmPosixProcessGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmProcessType"),
        ("CISCO-PROCESS-MIB", "cpmProcessRespawn"),
        ("CISCO-PROCESS-MIB", "cpmProcessRespawnCount"),
        ("CISCO-PROCESS-MIB", "cpmProcessRespawnAfterLastPatch"),
        ("CISCO-PROCESS-MIB", "cpmProcessMemoryCore"),
        ("CISCO-PROCESS-MIB", "cpmProcessLastRestartUser"),
        ("CISCO-PROCESS-MIB", "cpmProcessTextSegmentSize"),
        ("CISCO-PROCESS-MIB", "cpmProcessDataSegmentSize"),
        ("CISCO-PROCESS-MIB", "cpmProcessStackSize"),
        ("CISCO-PROCESS-MIB", "cpmProcessDynamicMemorySize"))
)
if mibBuilder.loadTexts:
    cpmPosixProcessGroup.setStatus("current")

cpmThreadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 13)
)
cpmThreadGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmThreadName"),
        ("CISCO-PROCESS-MIB", "cpmThreadPriority"),
        ("CISCO-PROCESS-MIB", "cpmThreadState"),
        ("CISCO-PROCESS-MIB", "cpmThreadBlockingProcess"),
        ("CISCO-PROCESS-MIB", "cpmThreadCpuUtilization"),
        ("CISCO-PROCESS-MIB", "cpmThreadStackSize"))
)
if mibBuilder.loadTexts:
    cpmThreadGroup.setStatus("current")

cpmVirtualProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 14)
)
cpmVirtualProcessGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmVirtualProcessName"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessUtil5Sec"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessUtil1Min"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessUtil5Min"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessMemAllocated"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessMemFreed"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessInvokeCount"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessRuntime"))
)
if mibBuilder.loadTexts:
    cpmVirtualProcessGroup.setStatus("current")

cpmCPUTotalOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 15)
)
cpmCPUTotalOverflowGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUMemoryUsedOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryFreeOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryKernelReservedOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryLowestOvrflw"))
)
if mibBuilder.loadTexts:
    cpmCPUTotalOverflowGroup.setStatus("current")

cpmCPUTotalHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 16)
)
cpmCPUTotalHCGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUMemoryHCUsed"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryHCFree"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryHCKernelReserved"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryHCLowest"))
)
if mibBuilder.loadTexts:
    cpmCPUTotalHCGroup.setStatus("current")

cpmProcessExtRevOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 17)
)
cpmProcessExtRevOverflowGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmProcExtMemAllocatedRevOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmProcExtMemFreedRevOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmProcessTextSegmentSizeOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmProcessDataSegmentSizeOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmProcessStackSizeOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmProcessDynamicMemorySizeOvrflw"))
)
if mibBuilder.loadTexts:
    cpmProcessExtRevOverflowGroup.setStatus("current")

cpmProcessExtRevHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 18)
)
cpmProcessExtRevHCGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmProcExtHCMemAllocatedRev"),
        ("CISCO-PROCESS-MIB", "cpmProcExtHCMemFreedRev"),
        ("CISCO-PROCESS-MIB", "cpmProcessHCTextSegmentSize"),
        ("CISCO-PROCESS-MIB", "cpmProcessHCDataSegmentSize"),
        ("CISCO-PROCESS-MIB", "cpmProcessHCStackSize"),
        ("CISCO-PROCESS-MIB", "cpmProcessHCDynamicMemorySize"))
)
if mibBuilder.loadTexts:
    cpmProcessExtRevHCGroup.setStatus("current")

cpmThreadOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 19)
)
cpmThreadOverflowGroup.setObjects(
    ("CISCO-PROCESS-MIB", "cpmThreadStackSizeOvrflw")
)
if mibBuilder.loadTexts:
    cpmThreadOverflowGroup.setStatus("current")

cpmThreadHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 20)
)
cpmThreadHCGroup.setObjects(
    ("CISCO-PROCESS-MIB", "cpmThreadHCStackSize")
)
if mibBuilder.loadTexts:
    cpmThreadHCGroup.setStatus("current")

cpmVirtualProcessOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 21)
)
cpmVirtualProcessOverflowGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmVirtualProcessMemAllocatedOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessMemFreedOvrflw"))
)
if mibBuilder.loadTexts:
    cpmVirtualProcessOverflowGroup.setStatus("current")

cpmVirtualProcessHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 22)
)
cpmVirtualProcessHCGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmVirtualProcessHCMemAllocated"),
        ("CISCO-PROCESS-MIB", "cpmVirtualProcessHCMemFreed"))
)
if mibBuilder.loadTexts:
    cpmVirtualProcessHCGroup.setStatus("current")

cpmCPULoadAvgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 23)
)
cpmCPULoadAvgGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPULoadAvg1min"),
        ("CISCO-PROCESS-MIB", "cpmCPULoadAvg5min"),
        ("CISCO-PROCESS-MIB", "cpmCPULoadAvg15min"))
)
if mibBuilder.loadTexts:
    cpmCPULoadAvgGroup.setStatus("current")

cpmCPUTotalMemoryCommitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 24)
)
cpmCPUTotalMemoryCommitGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUMemoryCommitted"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryCommittedOvrflw"),
        ("CISCO-PROCESS-MIB", "cpmCPUMemoryHCCommitted"))
)
if mibBuilder.loadTexts:
    cpmCPUTotalMemoryCommitGroup.setStatus("current")

cpmCoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 25)
)
cpmCoreGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCorePhysicalIndex"),
        ("CISCO-PROCESS-MIB", "cpmCore5sec"),
        ("CISCO-PROCESS-MIB", "cpmCore1min"),
        ("CISCO-PROCESS-MIB", "cpmCore5min"),
        ("CISCO-PROCESS-MIB", "cpmCoreLoadAvg1min"),
        ("CISCO-PROCESS-MIB", "cpmCoreLoadAvg5min"),
        ("CISCO-PROCESS-MIB", "cpmCoreLoadAvg15min"))
)
if mibBuilder.loadTexts:
    cpmCoreGroup.setStatus("current")


# Notification objects

cpmCPURisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 2, 0, 1)
)
cpmCPURisingThreshold.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPURisingThresholdValue"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotalMonIntervalValue"),
        ("CISCO-PROCESS-MIB", "cpmCPUInterruptMonIntervalValue"),
        ("CISCO-PROCESS-MIB", "cpmProcExtUtil5SecRev"),
        ("CISCO-PROCESS-MIB", "cpmProcessTimeCreated"))
)
if mibBuilder.loadTexts:
    cpmCPURisingThreshold.setStatus(
        "current"
    )

cpmCPUFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 2, 0, 2)
)
cpmCPUFallingThreshold.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPUFallingThresholdValue"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotalMonIntervalValue"),
        ("CISCO-PROCESS-MIB", "cpmCPUInterruptMonIntervalValue"))
)
if mibBuilder.loadTexts:
    cpmCPUFallingThreshold.setStatus(
        "current"
    )


# Notifications groups

cpmCPUThresholdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 2, 10)
)
cpmCPUThresholdNotificationGroup.setObjects(
      *(("CISCO-PROCESS-MIB", "cpmCPURisingThreshold"),
        ("CISCO-PROCESS-MIB", "cpmCPUFallingThreshold"))
)
if mibBuilder.loadTexts:
    cpmCPUThresholdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cProcessMIBCompliance.setStatus(
        "deprecated"
    )

cProcessMIBComplianceRev = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cProcessMIBComplianceRev.setStatus(
        "deprecated"
    )

cProcessMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cProcessMIBComplianceRev1.setStatus(
        "deprecated"
    )

cProcessMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cProcessMIBComplianceRev2.setStatus(
        "deprecated"
    )

cProcessMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cProcessMIBComplianceRev3.setStatus(
        "deprecated"
    )

cProcessMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cProcessMIBComplianceRev4.setStatus(
        "deprecated"
    )

cProcessMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 109, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cProcessMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PROCESS-MIB",
    **{"CPULoadAverage": CPULoadAverage,
       "ciscoProcessMIB": ciscoProcessMIB,
       "ciscoProcessMIBObjects": ciscoProcessMIBObjects,
       "cpmCPU": cpmCPU,
       "cpmCPUTotalTable": cpmCPUTotalTable,
       "cpmCPUTotalEntry": cpmCPUTotalEntry,
       "cpmCPUTotalIndex": cpmCPUTotalIndex,
       "cpmCPUTotalPhysicalIndex": cpmCPUTotalPhysicalIndex,
       "cpmCPUTotal5sec": cpmCPUTotal5sec,
       "cpmCPUTotal1min": cpmCPUTotal1min,
       "cpmCPUTotal5min": cpmCPUTotal5min,
       "cpmCPUTotal5secRev": cpmCPUTotal5secRev,
       "cpmCPUTotal1minRev": cpmCPUTotal1minRev,
       "cpmCPUTotal5minRev": cpmCPUTotal5minRev,
       "cpmCPUMonInterval": cpmCPUMonInterval,
       "cpmCPUTotalMonIntervalValue": cpmCPUTotalMonIntervalValue,
       "cpmCPUInterruptMonIntervalValue": cpmCPUInterruptMonIntervalValue,
       "cpmCPUMemoryUsed": cpmCPUMemoryUsed,
       "cpmCPUMemoryFree": cpmCPUMemoryFree,
       "cpmCPUMemoryKernelReserved": cpmCPUMemoryKernelReserved,
       "cpmCPUMemoryLowest": cpmCPUMemoryLowest,
       "cpmCPUMemoryUsedOvrflw": cpmCPUMemoryUsedOvrflw,
       "cpmCPUMemoryHCUsed": cpmCPUMemoryHCUsed,
       "cpmCPUMemoryFreeOvrflw": cpmCPUMemoryFreeOvrflw,
       "cpmCPUMemoryHCFree": cpmCPUMemoryHCFree,
       "cpmCPUMemoryKernelReservedOvrflw": cpmCPUMemoryKernelReservedOvrflw,
       "cpmCPUMemoryHCKernelReserved": cpmCPUMemoryHCKernelReserved,
       "cpmCPUMemoryLowestOvrflw": cpmCPUMemoryLowestOvrflw,
       "cpmCPUMemoryHCLowest": cpmCPUMemoryHCLowest,
       "cpmCPULoadAvg1min": cpmCPULoadAvg1min,
       "cpmCPULoadAvg5min": cpmCPULoadAvg5min,
       "cpmCPULoadAvg15min": cpmCPULoadAvg15min,
       "cpmCPUMemoryCommitted": cpmCPUMemoryCommitted,
       "cpmCPUMemoryCommittedOvrflw": cpmCPUMemoryCommittedOvrflw,
       "cpmCPUMemoryHCCommitted": cpmCPUMemoryHCCommitted,
       "cpmCoreTable": cpmCoreTable,
       "cpmCoreEntry": cpmCoreEntry,
       "cpmCoreIndex": cpmCoreIndex,
       "cpmCorePhysicalIndex": cpmCorePhysicalIndex,
       "cpmCore5sec": cpmCore5sec,
       "cpmCore1min": cpmCore1min,
       "cpmCore5min": cpmCore5min,
       "cpmCoreLoadAvg1min": cpmCoreLoadAvg1min,
       "cpmCoreLoadAvg5min": cpmCoreLoadAvg5min,
       "cpmCoreLoadAvg15min": cpmCoreLoadAvg15min,
       "cpmProcess": cpmProcess,
       "cpmProcessTable": cpmProcessTable,
       "cpmProcessEntry": cpmProcessEntry,
       "cpmProcessPID": cpmProcessPID,
       "cpmProcessName": cpmProcessName,
       "cpmProcessuSecs": cpmProcessuSecs,
       "cpmProcessTimeCreated": cpmProcessTimeCreated,
       "cpmProcessAverageUSecs": cpmProcessAverageUSecs,
       "cpmProcessExtTable": cpmProcessExtTable,
       "cpmProcessExtEntry": cpmProcessExtEntry,
       "cpmProcExtMemAllocated": cpmProcExtMemAllocated,
       "cpmProcExtMemFreed": cpmProcExtMemFreed,
       "cpmProcExtInvoked": cpmProcExtInvoked,
       "cpmProcExtRuntime": cpmProcExtRuntime,
       "cpmProcExtUtil5Sec": cpmProcExtUtil5Sec,
       "cpmProcExtUtil1Min": cpmProcExtUtil1Min,
       "cpmProcExtUtil5Min": cpmProcExtUtil5Min,
       "cpmProcExtPriority": cpmProcExtPriority,
       "cpmProcessExtRevTable": cpmProcessExtRevTable,
       "cpmProcessExtRevEntry": cpmProcessExtRevEntry,
       "cpmProcExtMemAllocatedRev": cpmProcExtMemAllocatedRev,
       "cpmProcExtMemFreedRev": cpmProcExtMemFreedRev,
       "cpmProcExtInvokedRev": cpmProcExtInvokedRev,
       "cpmProcExtRuntimeRev": cpmProcExtRuntimeRev,
       "cpmProcExtUtil5SecRev": cpmProcExtUtil5SecRev,
       "cpmProcExtUtil1MinRev": cpmProcExtUtil1MinRev,
       "cpmProcExtUtil5MinRev": cpmProcExtUtil5MinRev,
       "cpmProcExtPriorityRev": cpmProcExtPriorityRev,
       "cpmProcessType": cpmProcessType,
       "cpmProcessRespawn": cpmProcessRespawn,
       "cpmProcessRespawnCount": cpmProcessRespawnCount,
       "cpmProcessRespawnAfterLastPatch": cpmProcessRespawnAfterLastPatch,
       "cpmProcessMemoryCore": cpmProcessMemoryCore,
       "cpmProcessLastRestartUser": cpmProcessLastRestartUser,
       "cpmProcessTextSegmentSize": cpmProcessTextSegmentSize,
       "cpmProcessDataSegmentSize": cpmProcessDataSegmentSize,
       "cpmProcessStackSize": cpmProcessStackSize,
       "cpmProcessDynamicMemorySize": cpmProcessDynamicMemorySize,
       "cpmProcExtMemAllocatedRevOvrflw": cpmProcExtMemAllocatedRevOvrflw,
       "cpmProcExtHCMemAllocatedRev": cpmProcExtHCMemAllocatedRev,
       "cpmProcExtMemFreedRevOvrflw": cpmProcExtMemFreedRevOvrflw,
       "cpmProcExtHCMemFreedRev": cpmProcExtHCMemFreedRev,
       "cpmProcessTextSegmentSizeOvrflw": cpmProcessTextSegmentSizeOvrflw,
       "cpmProcessHCTextSegmentSize": cpmProcessHCTextSegmentSize,
       "cpmProcessDataSegmentSizeOvrflw": cpmProcessDataSegmentSizeOvrflw,
       "cpmProcessHCDataSegmentSize": cpmProcessHCDataSegmentSize,
       "cpmProcessStackSizeOvrflw": cpmProcessStackSizeOvrflw,
       "cpmProcessHCStackSize": cpmProcessHCStackSize,
       "cpmProcessDynamicMemorySizeOvrflw": cpmProcessDynamicMemorySizeOvrflw,
       "cpmProcessHCDynamicMemorySize": cpmProcessHCDynamicMemorySize,
       "cpmCPUThresholdTable": cpmCPUThresholdTable,
       "cpmCPUThresholdEntry": cpmCPUThresholdEntry,
       "cpmCPUThresholdClass": cpmCPUThresholdClass,
       "cpmCPURisingThresholdValue": cpmCPURisingThresholdValue,
       "cpmCPURisingThresholdPeriod": cpmCPURisingThresholdPeriod,
       "cpmCPUFallingThresholdValue": cpmCPUFallingThresholdValue,
       "cpmCPUFallingThresholdPeriod": cpmCPUFallingThresholdPeriod,
       "cpmCPUThresholdEntryStatus": cpmCPUThresholdEntryStatus,
       "cpmCPUHistory": cpmCPUHistory,
       "cpmCPUHistoryThreshold": cpmCPUHistoryThreshold,
       "cpmCPUHistorySize": cpmCPUHistorySize,
       "cpmCPUHistoryTable": cpmCPUHistoryTable,
       "cpmCPUHistoryEntry": cpmCPUHistoryEntry,
       "cpmCPUHistoryReportId": cpmCPUHistoryReportId,
       "cpmCPUHistoryReportSize": cpmCPUHistoryReportSize,
       "cpmCPUHistoryTotalUtil": cpmCPUHistoryTotalUtil,
       "cpmCPUHistoryInterruptUtil": cpmCPUHistoryInterruptUtil,
       "cpmCPUHistoryCreatedTime": cpmCPUHistoryCreatedTime,
       "cpmCPUProcessHistoryTable": cpmCPUProcessHistoryTable,
       "cpmCPUProcessHistoryEntry": cpmCPUProcessHistoryEntry,
       "cpmCPUProcessHistoryIndex": cpmCPUProcessHistoryIndex,
       "cpmCPUHistoryProcId": cpmCPUHistoryProcId,
       "cpmCPUHistoryProcName": cpmCPUHistoryProcName,
       "cpmCPUHistoryProcCreated": cpmCPUHistoryProcCreated,
       "cpmCPUHistoryProcUtil": cpmCPUHistoryProcUtil,
       "cpmThread": cpmThread,
       "cpmThreadTable": cpmThreadTable,
       "cpmThreadEntry": cpmThreadEntry,
       "cpmThreadID": cpmThreadID,
       "cpmThreadName": cpmThreadName,
       "cpmThreadPriority": cpmThreadPriority,
       "cpmThreadState": cpmThreadState,
       "cpmThreadBlockingProcess": cpmThreadBlockingProcess,
       "cpmThreadCpuUtilization": cpmThreadCpuUtilization,
       "cpmThreadStackSize": cpmThreadStackSize,
       "cpmThreadStackSizeOvrflw": cpmThreadStackSizeOvrflw,
       "cpmThreadHCStackSize": cpmThreadHCStackSize,
       "cpmVirtualProcess": cpmVirtualProcess,
       "cpmVirtualProcessTable": cpmVirtualProcessTable,
       "cpmVirtualProcessEntry": cpmVirtualProcessEntry,
       "cpmVirtualProcessID": cpmVirtualProcessID,
       "cpmVirtualProcessName": cpmVirtualProcessName,
       "cpmVirtualProcessUtil5Sec": cpmVirtualProcessUtil5Sec,
       "cpmVirtualProcessUtil1Min": cpmVirtualProcessUtil1Min,
       "cpmVirtualProcessUtil5Min": cpmVirtualProcessUtil5Min,
       "cpmVirtualProcessMemAllocated": cpmVirtualProcessMemAllocated,
       "cpmVirtualProcessMemFreed": cpmVirtualProcessMemFreed,
       "cpmVirtualProcessInvokeCount": cpmVirtualProcessInvokeCount,
       "cpmVirtualProcessRuntime": cpmVirtualProcessRuntime,
       "cpmVirtualProcessMemAllocatedOvrflw": cpmVirtualProcessMemAllocatedOvrflw,
       "cpmVirtualProcessHCMemAllocated": cpmVirtualProcessHCMemAllocated,
       "cpmVirtualProcessMemFreedOvrflw": cpmVirtualProcessMemFreedOvrflw,
       "cpmVirtualProcessHCMemFreed": cpmVirtualProcessHCMemFreed,
       "ciscoProcessMIBNotifPrefix": ciscoProcessMIBNotifPrefix,
       "ciscoProcessMIBNotifs": ciscoProcessMIBNotifs,
       "cpmCPURisingThreshold": cpmCPURisingThreshold,
       "cpmCPUFallingThreshold": cpmCPUFallingThreshold,
       "ciscoProcessMIBConformance": ciscoProcessMIBConformance,
       "cpmCompliances": cpmCompliances,
       "cProcessMIBCompliance": cProcessMIBCompliance,
       "cProcessMIBComplianceRev": cProcessMIBComplianceRev,
       "cProcessMIBComplianceRev1": cProcessMIBComplianceRev1,
       "cProcessMIBComplianceRev2": cProcessMIBComplianceRev2,
       "cProcessMIBComplianceRev3": cProcessMIBComplianceRev3,
       "cProcessMIBComplianceRev4": cProcessMIBComplianceRev4,
       "cProcessMIBComplianceRev5": cProcessMIBComplianceRev5,
       "cpmGroups": cpmGroups,
       "cpmCPUTotalGroup": cpmCPUTotalGroup,
       "cpmProcessGroup": cpmProcessGroup,
       "cpmProcessExtGroup": cpmProcessExtGroup,
       "cpmCPUTotalGroupRev": cpmCPUTotalGroupRev,
       "cpmProcessExtGroupRev": cpmProcessExtGroupRev,
       "cpmProcessGroupRev": cpmProcessGroupRev,
       "cpmCPUTotalGroupRev1": cpmCPUTotalGroupRev1,
       "cpmCPUThresholdGroup": cpmCPUThresholdGroup,
       "cpmCPUHistoryGroup": cpmCPUHistoryGroup,
       "cpmCPUThresholdNotificationGroup": cpmCPUThresholdNotificationGroup,
       "cpmCPUPosixMemoryGroup": cpmCPUPosixMemoryGroup,
       "cpmPosixProcessGroup": cpmPosixProcessGroup,
       "cpmThreadGroup": cpmThreadGroup,
       "cpmVirtualProcessGroup": cpmVirtualProcessGroup,
       "cpmCPUTotalOverflowGroup": cpmCPUTotalOverflowGroup,
       "cpmCPUTotalHCGroup": cpmCPUTotalHCGroup,
       "cpmProcessExtRevOverflowGroup": cpmProcessExtRevOverflowGroup,
       "cpmProcessExtRevHCGroup": cpmProcessExtRevHCGroup,
       "cpmThreadOverflowGroup": cpmThreadOverflowGroup,
       "cpmThreadHCGroup": cpmThreadHCGroup,
       "cpmVirtualProcessOverflowGroup": cpmVirtualProcessOverflowGroup,
       "cpmVirtualProcessHCGroup": cpmVirtualProcessHCGroup,
       "cpmCPULoadAvgGroup": cpmCPULoadAvgGroup,
       "cpmCPUTotalMemoryCommitGroup": cpmCPUTotalMemoryCommitGroup,
       "cpmCoreGroup": cpmCoreGroup}
)
