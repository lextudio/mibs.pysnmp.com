# SNMP MIB module (CTRON-SSR-CAPACITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SSR-CAPACITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:38 2024
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

(ssrMibs,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

capacityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270)
)
capacityMIB.setRevisions(
        ("2000-07-15 00:00",
         "1998-11-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SSRMemoryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 1),
          ("intFlash", 2),
          ("l2Hardware", 5),
          ("l3Hardware", 6),
          ("pcmcia", 3),
          ("rmon", 4))
    )



class SSRCapabilityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("disabled", 4),
          ("enabled", 3),
          ("noSupport", 1))
    )



class SSRStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("finished", 11),
          ("ready", 0),
          ("suspDrvr", 10),
          ("suspEvent", 7),
          ("suspMbox", 3),
          ("suspMem", 9),
          ("suspPart", 8),
          ("suspPipe", 5),
          ("suspPure", 1),
          ("suspQue", 4),
          ("suspSema4", 6),
          ("suspSleep", 2),
          ("terminated", 12))
    )



# MIB Managed Objects in the order of their OIDs

_ChassisCap_ObjectIdentity = ObjectIdentity
chassisCap = _ChassisCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1)
)


class _CapChassisSlotCount_Type(Integer32):
    """Custom type capChassisSlotCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_CapChassisSlotCount_Type.__name__ = "Integer32"
_CapChassisSlotCount_Object = MibScalar
capChassisSlotCount = _CapChassisSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 1),
    _CapChassisSlotCount_Type()
)
capChassisSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChassisSlotCount.setStatus("current")


class _CapChassisSlotsUsed_Type(Integer32):
    """Custom type capChassisSlotsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CapChassisSlotsUsed_Type.__name__ = "Integer32"
_CapChassisSlotsUsed_Object = MibScalar
capChassisSlotsUsed = _CapChassisSlotsUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 2),
    _CapChassisSlotsUsed_Type()
)
capChassisSlotsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChassisSlotsUsed.setStatus("current")


class _CapChassisSlotsFree_Type(Integer32):
    """Custom type capChassisSlotsFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CapChassisSlotsFree_Type.__name__ = "Integer32"
_CapChassisSlotsFree_Object = MibScalar
capChassisSlotsFree = _CapChassisSlotsFree_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 3),
    _CapChassisSlotsFree_Type()
)
capChassisSlotsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChassisSlotsFree.setStatus("current")
_CapChassisCPURedundancy_Type = SSRCapabilityType
_CapChassisCPURedundancy_Object = MibScalar
capChassisCPURedundancy = _CapChassisCPURedundancy_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 4),
    _CapChassisCPURedundancy_Type()
)
capChassisCPURedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChassisCPURedundancy.setStatus("current")
_CapChassisPSRedundancy_Type = SSRCapabilityType
_CapChassisPSRedundancy_Object = MibScalar
capChassisPSRedundancy = _CapChassisPSRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 5),
    _CapChassisPSRedundancy_Type()
)
capChassisPSRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChassisPSRedundancy.setStatus("current")
_CapChassisSFRedundancy_Type = SSRCapabilityType
_CapChassisSFRedundancy_Object = MibScalar
capChassisSFRedundancy = _CapChassisSFRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 6),
    _CapChassisSFRedundancy_Type()
)
capChassisSFRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChassisSFRedundancy.setStatus("current")
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2)
)
_CapCPUTable_Object = MibTable
capCPUTable = _CapCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1)
)
if mibBuilder.loadTexts:
    capCPUTable.setStatus("current")
_CapCPUEntry_Object = MibTableRow
capCPUEntry = _CapCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1)
)
capCPUEntry.setIndexNames(
    (0, "CTRON-SSR-CAPACITY-MIB", "capCPUModuleIndex"),
)
if mibBuilder.loadTexts:
    capCPUEntry.setStatus("current")


class _CapCPUModuleIndex_Type(Integer32):
    """Custom type capCPUModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CapCPUModuleIndex_Type.__name__ = "Integer32"
_CapCPUModuleIndex_Object = MibTableColumn
capCPUModuleIndex = _CapCPUModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 1),
    _CapCPUModuleIndex_Type()
)
capCPUModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capCPUModuleIndex.setStatus("current")


class _CapCPUCurrentUtilization_Type(Integer32):
    """Custom type capCPUCurrentUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CapCPUCurrentUtilization_Type.__name__ = "Integer32"
_CapCPUCurrentUtilization_Object = MibTableColumn
capCPUCurrentUtilization = _CapCPUCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 2),
    _CapCPUCurrentUtilization_Type()
)
capCPUCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capCPUCurrentUtilization.setStatus("current")
_CapCPUL3Learned_Type = Counter32
_CapCPUL3Learned_Object = MibTableColumn
capCPUL3Learned = _CapCPUL3Learned_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 3),
    _CapCPUL3Learned_Type()
)
capCPUL3Learned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capCPUL3Learned.setStatus("current")
_CapCPUL3Aged_Type = Counter32
_CapCPUL3Aged_Object = MibTableColumn
capCPUL3Aged = _CapCPUL3Aged_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 4),
    _CapCPUL3Aged_Type()
)
capCPUL3Aged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capCPUL3Aged.setStatus("current")
_CapCPUL2Learned_Type = Counter32
_CapCPUL2Learned_Object = MibTableColumn
capCPUL2Learned = _CapCPUL2Learned_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 5),
    _CapCPUL2Learned_Type()
)
capCPUL2Learned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capCPUL2Learned.setStatus("current")
_CapCPUL2Aged_Type = Counter32
_CapCPUL2Aged_Object = MibTableColumn
capCPUL2Aged = _CapCPUL2Aged_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 6),
    _CapCPUL2Aged_Type()
)
capCPUL2Aged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capCPUL2Aged.setStatus("current")
_CapCPUNIAReceived_Type = Counter32
_CapCPUNIAReceived_Object = MibTableColumn
capCPUNIAReceived = _CapCPUNIAReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 7),
    _CapCPUNIAReceived_Type()
)
capCPUNIAReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capCPUNIAReceived.setStatus("current")
_CapCPUNIATransmitted_Type = Counter32
_CapCPUNIATransmitted_Object = MibTableColumn
capCPUNIATransmitted = _CapCPUNIATransmitted_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 8),
    _CapCPUNIATransmitted_Type()
)
capCPUNIATransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capCPUNIATransmitted.setStatus("current")


class _CapCPUMinThreshold_Type(Integer32):
    """Custom type capCPUMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CapCPUMinThreshold_Type.__name__ = "Integer32"
_CapCPUMinThreshold_Object = MibTableColumn
capCPUMinThreshold = _CapCPUMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 9),
    _CapCPUMinThreshold_Type()
)
capCPUMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capCPUMinThreshold.setStatus("current")


class _CapCPUMaxThreshold_Type(Integer32):
    """Custom type capCPUMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CapCPUMaxThreshold_Type.__name__ = "Integer32"
_CapCPUMaxThreshold_Object = MibTableColumn
capCPUMaxThreshold = _CapCPUMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 10),
    _CapCPUMaxThreshold_Type()
)
capCPUMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capCPUMaxThreshold.setStatus("current")
_Tasks_ObjectIdentity = ObjectIdentity
tasks = _Tasks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3)
)
_CapTaskTable_Object = MibTable
capTaskTable = _CapTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1)
)
if mibBuilder.loadTexts:
    capTaskTable.setStatus("current")
_CapTaskEntry_Object = MibTableRow
capTaskEntry = _CapTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1)
)
capTaskEntry.setIndexNames(
    (0, "CTRON-SSR-CAPACITY-MIB", "capTaskModuleIndex"),
    (0, "CTRON-SSR-CAPACITY-MIB", "capTaskIndex"),
)
if mibBuilder.loadTexts:
    capTaskEntry.setStatus("current")


class _CapTaskModuleIndex_Type(Integer32):
    """Custom type capTaskModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CapTaskModuleIndex_Type.__name__ = "Integer32"
_CapTaskModuleIndex_Object = MibTableColumn
capTaskModuleIndex = _CapTaskModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 1),
    _CapTaskModuleIndex_Type()
)
capTaskModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capTaskModuleIndex.setStatus("current")


class _CapTaskIndex_Type(Integer32):
    """Custom type capTaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CapTaskIndex_Type.__name__ = "Integer32"
_CapTaskIndex_Object = MibTableColumn
capTaskIndex = _CapTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 2),
    _CapTaskIndex_Type()
)
capTaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capTaskIndex.setStatus("current")


class _CapTaskName_Type(OctetString):
    """Custom type capTaskName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CapTaskName_Type.__name__ = "OctetString"
_CapTaskName_Object = MibTableColumn
capTaskName = _CapTaskName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 3),
    _CapTaskName_Type()
)
capTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capTaskName.setStatus("current")
_CapTaskShed_Type = Counter32
_CapTaskShed_Object = MibTableColumn
capTaskShed = _CapTaskShed_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 4),
    _CapTaskShed_Type()
)
capTaskShed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capTaskShed.setStatus("current")
_CapTaskStatus_Type = SSRStatusType
_CapTaskStatus_Object = MibTableColumn
capTaskStatus = _CapTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 5),
    _CapTaskStatus_Type()
)
capTaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capTaskStatus.setStatus("current")


class _CapTaskUsed_Type(Integer32):
    """Custom type capTaskUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CapTaskUsed_Type.__name__ = "Integer32"
_CapTaskUsed_Object = MibTableColumn
capTaskUsed = _CapTaskUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 6),
    _CapTaskUsed_Type()
)
capTaskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capTaskUsed.setStatus("current")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4)
)
_CapMemoryTable_Object = MibTable
capMemoryTable = _CapMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1)
)
if mibBuilder.loadTexts:
    capMemoryTable.setStatus("current")
_CapMemoryEntry_Object = MibTableRow
capMemoryEntry = _CapMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1)
)
capMemoryEntry.setIndexNames(
    (0, "CTRON-SSR-CAPACITY-MIB", "capMemoryType"),
    (0, "CTRON-SSR-CAPACITY-MIB", "capMemoryIndex"),
)
if mibBuilder.loadTexts:
    capMemoryEntry.setStatus("current")
_CapMemoryType_Type = SSRMemoryType
_CapMemoryType_Object = MibTableColumn
capMemoryType = _CapMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 1),
    _CapMemoryType_Type()
)
capMemoryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capMemoryType.setStatus("current")


class _CapMemoryIndex_Type(Integer32):
    """Custom type capMemoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CapMemoryIndex_Type.__name__ = "Integer32"
_CapMemoryIndex_Object = MibTableColumn
capMemoryIndex = _CapMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 2),
    _CapMemoryIndex_Type()
)
capMemoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capMemoryIndex.setStatus("current")


class _CapMemoryDescr_Type(OctetString):
    """Custom type capMemoryDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CapMemoryDescr_Type.__name__ = "OctetString"
_CapMemoryDescr_Object = MibTableColumn
capMemoryDescr = _CapMemoryDescr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 3),
    _CapMemoryDescr_Type()
)
capMemoryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capMemoryDescr.setStatus("current")


class _CapMemorySize_Type(Integer32):
    """Custom type capMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CapMemorySize_Type.__name__ = "Integer32"
_CapMemorySize_Object = MibTableColumn
capMemorySize = _CapMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 4),
    _CapMemorySize_Type()
)
capMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capMemorySize.setStatus("current")


class _CapMemoryFree_Type(Integer32):
    """Custom type capMemoryFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CapMemoryFree_Type.__name__ = "Integer32"
_CapMemoryFree_Object = MibTableColumn
capMemoryFree = _CapMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 5),
    _CapMemoryFree_Type()
)
capMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capMemoryFree.setStatus("current")


class _CapMemoryUsed_Type(Integer32):
    """Custom type capMemoryUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CapMemoryUsed_Type.__name__ = "Integer32"
_CapMemoryUsed_Object = MibTableColumn
capMemoryUsed = _CapMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 6),
    _CapMemoryUsed_Type()
)
capMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capMemoryUsed.setStatus("current")


class _CapMemoryBlockSize_Type(Integer32):
    """Custom type capMemoryBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CapMemoryBlockSize_Type.__name__ = "Integer32"
_CapMemoryBlockSize_Object = MibTableColumn
capMemoryBlockSize = _CapMemoryBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 7),
    _CapMemoryBlockSize_Type()
)
capMemoryBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capMemoryBlockSize.setStatus("current")
_CapMemoryFailures_Type = Counter32
_CapMemoryFailures_Object = MibTableColumn
capMemoryFailures = _CapMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 8),
    _CapMemoryFailures_Type()
)
capMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capMemoryFailures.setStatus("current")
_CapMemoryRemovable_Type = TruthValue
_CapMemoryRemovable_Object = MibTableColumn
capMemoryRemovable = _CapMemoryRemovable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 9),
    _CapMemoryRemovable_Type()
)
capMemoryRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capMemoryRemovable.setStatus("current")
_CapConformance_ObjectIdentity = ObjectIdentity
capConformance = _CapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6)
)
_CapCompliances_ObjectIdentity = ObjectIdentity
capCompliances = _CapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 1)
)
_CapGroups_ObjectIdentity = ObjectIdentity
capGroups = _CapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2)
)

# Managed Objects groups

capConfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 1)
)
capConfGroupV10.setObjects(
      *(("CTRON-SSR-CAPACITY-MIB", "capChassisSlotCount"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsUsed"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsFree"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisCPURedundancy"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisPSRedundancy"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisSFRedundancy"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Learned"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Aged"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Learned"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Aged"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUNIAReceived"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUNIATransmitted"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskName"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskShed"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskStatus"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskUsed"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryDescr"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemorySize"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryFree"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryUsed"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryBlockSize"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryFailures"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryRemovable"))
)
if mibBuilder.loadTexts:
    capConfGroupV10.setStatus("deprecated")

capConfGroupV20 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 2)
)
capConfGroupV20.setObjects(
      *(("CTRON-SSR-CAPACITY-MIB", "capChassisSlotCount"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsUsed"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsFree"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisCPURedundancy"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisPSRedundancy"),
        ("CTRON-SSR-CAPACITY-MIB", "capChassisSFRedundancy"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Learned"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Aged"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Learned"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Aged"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUNIAReceived"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUNIATransmitted"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUMinThreshold"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUMaxThreshold"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskName"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskShed"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskStatus"),
        ("CTRON-SSR-CAPACITY-MIB", "capTaskUsed"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryDescr"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemorySize"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryFree"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryUsed"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryBlockSize"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryFailures"),
        ("CTRON-SSR-CAPACITY-MIB", "capMemoryRemovable"))
)
if mibBuilder.loadTexts:
    capConfGroupV20.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

capComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    capComplianceV10.setStatus(
        "deprecated"
    )

capComplianceV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    capComplianceV20.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-CAPACITY-MIB",
    **{"SSRMemoryType": SSRMemoryType,
       "SSRCapabilityType": SSRCapabilityType,
       "SSRStatusType": SSRStatusType,
       "capacityMIB": capacityMIB,
       "chassisCap": chassisCap,
       "capChassisSlotCount": capChassisSlotCount,
       "capChassisSlotsUsed": capChassisSlotsUsed,
       "capChassisSlotsFree": capChassisSlotsFree,
       "capChassisCPURedundancy": capChassisCPURedundancy,
       "capChassisPSRedundancy": capChassisPSRedundancy,
       "capChassisSFRedundancy": capChassisSFRedundancy,
       "cpu": cpu,
       "capCPUTable": capCPUTable,
       "capCPUEntry": capCPUEntry,
       "capCPUModuleIndex": capCPUModuleIndex,
       "capCPUCurrentUtilization": capCPUCurrentUtilization,
       "capCPUL3Learned": capCPUL3Learned,
       "capCPUL3Aged": capCPUL3Aged,
       "capCPUL2Learned": capCPUL2Learned,
       "capCPUL2Aged": capCPUL2Aged,
       "capCPUNIAReceived": capCPUNIAReceived,
       "capCPUNIATransmitted": capCPUNIATransmitted,
       "capCPUMinThreshold": capCPUMinThreshold,
       "capCPUMaxThreshold": capCPUMaxThreshold,
       "tasks": tasks,
       "capTaskTable": capTaskTable,
       "capTaskEntry": capTaskEntry,
       "capTaskModuleIndex": capTaskModuleIndex,
       "capTaskIndex": capTaskIndex,
       "capTaskName": capTaskName,
       "capTaskShed": capTaskShed,
       "capTaskStatus": capTaskStatus,
       "capTaskUsed": capTaskUsed,
       "memory": memory,
       "capMemoryTable": capMemoryTable,
       "capMemoryEntry": capMemoryEntry,
       "capMemoryType": capMemoryType,
       "capMemoryIndex": capMemoryIndex,
       "capMemoryDescr": capMemoryDescr,
       "capMemorySize": capMemorySize,
       "capMemoryFree": capMemoryFree,
       "capMemoryUsed": capMemoryUsed,
       "capMemoryBlockSize": capMemoryBlockSize,
       "capMemoryFailures": capMemoryFailures,
       "capMemoryRemovable": capMemoryRemovable,
       "capConformance": capConformance,
       "capCompliances": capCompliances,
       "capGroups": capGroups,
       "capConfGroupV10": capConfGroupV10,
       "capComplianceV10": capComplianceV10,
       "capConfGroupV20": capConfGroupV20,
       "capComplianceV20": capComplianceV20}
)
