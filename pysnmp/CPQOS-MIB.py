# SNMP MIB module (CPQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:34 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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

_CpqWinOsMgmt_ObjectIdentity = ObjectIdentity
cpqWinOsMgmt = _CpqWinOsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19)
)
_CpqOsMibRev_ObjectIdentity = ObjectIdentity
cpqOsMibRev = _CpqOsMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 1)
)


class _CpqOsMibRevMajor_Type(Integer32):
    """Custom type cpqOsMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqOsMibRevMajor_Type.__name__ = "Integer32"
_CpqOsMibRevMajor_Object = MibScalar
cpqOsMibRevMajor = _CpqOsMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 1, 1),
    _CpqOsMibRevMajor_Type()
)
cpqOsMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMibRevMajor.setStatus("mandatory")


class _CpqOsMibRevMinor_Type(Integer32):
    """Custom type cpqOsMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqOsMibRevMinor_Type.__name__ = "Integer32"
_CpqOsMibRevMinor_Object = MibScalar
cpqOsMibRevMinor = _CpqOsMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 1, 2),
    _CpqOsMibRevMinor_Type()
)
cpqOsMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMibRevMinor.setStatus("mandatory")


class _CpqOsMibCondition_Type(Integer32):
    """Custom type cpqOsMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsMibCondition_Type.__name__ = "Integer32"
_CpqOsMibCondition_Object = MibScalar
cpqOsMibCondition = _CpqOsMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 1, 3),
    _CpqOsMibCondition_Type()
)
cpqOsMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMibCondition.setStatus("mandatory")
_CpqOsComponent_ObjectIdentity = ObjectIdentity
cpqOsComponent = _CpqOsComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2)
)
_CpqOsInterface_ObjectIdentity = ObjectIdentity
cpqOsInterface = _CpqOsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 1)
)
_CpqOsCommon_ObjectIdentity = ObjectIdentity
cpqOsCommon = _CpqOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 1, 4)
)


class _CpqOsCommonPollFreq_Type(Integer32):
    """Custom type cpqOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqOsCommonPollFreq_Object = MibScalar
cpqOsCommonPollFreq = _CpqOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 1, 4, 1),
    _CpqOsCommonPollFreq_Type()
)
cpqOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsCommonPollFreq.setStatus("mandatory")
_CpqOsSystem_ObjectIdentity = ObjectIdentity
cpqOsSystem = _CpqOsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2)
)


class _CpqOsSystemStatus_Type(Integer32):
    """Custom type cpqOsSystemStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsSystemStatus_Type.__name__ = "Integer32"
_CpqOsSystemStatus_Object = MibScalar
cpqOsSystemStatus = _CpqOsSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2, 1),
    _CpqOsSystemStatus_Type()
)
cpqOsSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsSystemStatus.setStatus("mandatory")


class _CpqOsSystemUpTime_Type(DisplayString):
    """Custom type cpqOsSystemUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsSystemUpTime_Type.__name__ = "DisplayString"
_CpqOsSystemUpTime_Object = MibScalar
cpqOsSystemUpTime = _CpqOsSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2, 2),
    _CpqOsSystemUpTime_Type()
)
cpqOsSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsSystemUpTime.setStatus("mandatory")
_CpqOsSystemThreads_Type = Integer32
_CpqOsSystemThreads_Object = MibScalar
cpqOsSystemThreads = _CpqOsSystemThreads_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2, 3),
    _CpqOsSystemThreads_Type()
)
cpqOsSystemThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsSystemThreads.setStatus("mandatory")
_CpqOsSysContextSwitchesPersec_Type = Integer32
_CpqOsSysContextSwitchesPersec_Object = MibScalar
cpqOsSysContextSwitchesPersec = _CpqOsSysContextSwitchesPersec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2, 4),
    _CpqOsSysContextSwitchesPersec_Type()
)
cpqOsSysContextSwitchesPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsSysContextSwitchesPersec.setStatus("mandatory")
_CpqOsSysCpuQueueLength_Type = Integer32
_CpqOsSysCpuQueueLength_Object = MibScalar
cpqOsSysCpuQueueLength = _CpqOsSysCpuQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2, 5),
    _CpqOsSysCpuQueueLength_Type()
)
cpqOsSysCpuQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsSysCpuQueueLength.setStatus("mandatory")
_CpqOsSysProcesses_Type = Integer32
_CpqOsSysProcesses_Object = MibScalar
cpqOsSysProcesses = _CpqOsSysProcesses_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2, 6),
    _CpqOsSysProcesses_Type()
)
cpqOsSysProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsSysProcesses.setStatus("mandatory")
_CpqOsSysRegistryInUsePercent_Type = Integer32
_CpqOsSysRegistryInUsePercent_Object = MibScalar
cpqOsSysRegistryInUsePercent = _CpqOsSysRegistryInUsePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 2, 7),
    _CpqOsSysRegistryInUsePercent_Type()
)
cpqOsSysRegistryInUsePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsSysRegistryInUsePercent.setStatus("mandatory")
_CpqOsProcessor_ObjectIdentity = ObjectIdentity
cpqOsProcessor = _CpqOsProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3)
)


class _CpqOsProcessorStatus_Type(Integer32):
    """Custom type cpqOsProcessorStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsProcessorStatus_Type.__name__ = "Integer32"
_CpqOsProcessorStatus_Object = MibScalar
cpqOsProcessorStatus = _CpqOsProcessorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 1),
    _CpqOsProcessorStatus_Type()
)
cpqOsProcessorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessorStatus.setStatus("mandatory")
_CpqOsProcessorTable_Object = MibTable
cpqOsProcessorTable = _CpqOsProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cpqOsProcessorTable.setStatus("mandatory")
_CpqOsProcessorEntry_Object = MibTableRow
cpqOsProcessorEntry = _CpqOsProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1)
)
cpqOsProcessorEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsCpuIndex"),
)
if mibBuilder.loadTexts:
    cpqOsProcessorEntry.setStatus("mandatory")
_CpqOsCpuIndex_Type = Integer32
_CpqOsCpuIndex_Object = MibTableColumn
cpqOsCpuIndex = _CpqOsCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 1),
    _CpqOsCpuIndex_Type()
)
cpqOsCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuIndex.setStatus("mandatory")


class _CpqOsCpuInstance_Type(DisplayString):
    """Custom type cpqOsCpuInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsCpuInstance_Type.__name__ = "DisplayString"
_CpqOsCpuInstance_Object = MibTableColumn
cpqOsCpuInstance = _CpqOsCpuInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 2),
    _CpqOsCpuInstance_Type()
)
cpqOsCpuInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuInstance.setStatus("mandatory")
_CpqOsCpuInterruptsPerSec_Type = Integer32
_CpqOsCpuInterruptsPerSec_Object = MibTableColumn
cpqOsCpuInterruptsPerSec = _CpqOsCpuInterruptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 3),
    _CpqOsCpuInterruptsPerSec_Type()
)
cpqOsCpuInterruptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuInterruptsPerSec.setStatus("mandatory")
_CpqOsCpuTimePercent_Type = Integer32
_CpqOsCpuTimePercent_Object = MibTableColumn
cpqOsCpuTimePercent = _CpqOsCpuTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 4),
    _CpqOsCpuTimePercent_Type()
)
cpqOsCpuTimePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuTimePercent.setStatus("mandatory")
_CpqOsWarCpuTimePercent_Type = Integer32
_CpqOsWarCpuTimePercent_Object = MibTableColumn
cpqOsWarCpuTimePercent = _CpqOsWarCpuTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 5),
    _CpqOsWarCpuTimePercent_Type()
)
cpqOsWarCpuTimePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsWarCpuTimePercent.setStatus("mandatory")
_CpqOsCriCpuTimePercent_Type = Integer32
_CpqOsCriCpuTimePercent_Object = MibTableColumn
cpqOsCriCpuTimePercent = _CpqOsCriCpuTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 6),
    _CpqOsCriCpuTimePercent_Type()
)
cpqOsCriCpuTimePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsCriCpuTimePercent.setStatus("mandatory")
_CpqOsCpuUserTimePercent_Type = Integer32
_CpqOsCpuUserTimePercent_Object = MibTableColumn
cpqOsCpuUserTimePercent = _CpqOsCpuUserTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 7),
    _CpqOsCpuUserTimePercent_Type()
)
cpqOsCpuUserTimePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuUserTimePercent.setStatus("mandatory")
_CpqOsCpuPrivilegedTimePercent_Type = Integer32
_CpqOsCpuPrivilegedTimePercent_Object = MibTableColumn
cpqOsCpuPrivilegedTimePercent = _CpqOsCpuPrivilegedTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 8),
    _CpqOsCpuPrivilegedTimePercent_Type()
)
cpqOsCpuPrivilegedTimePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuPrivilegedTimePercent.setStatus("mandatory")


class _CpqOsCpuCondition_Type(Integer32):
    """Custom type cpqOsCpuCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsCpuCondition_Type.__name__ = "Integer32"
_CpqOsCpuCondition_Object = MibTableColumn
cpqOsCpuCondition = _CpqOsCpuCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 9),
    _CpqOsCpuCondition_Type()
)
cpqOsCpuCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuCondition.setStatus("mandatory")
_CpqOsCpuPercentDPCTime_Type = Integer32
_CpqOsCpuPercentDPCTime_Object = MibTableColumn
cpqOsCpuPercentDPCTime = _CpqOsCpuPercentDPCTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 10),
    _CpqOsCpuPercentDPCTime_Type()
)
cpqOsCpuPercentDPCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuPercentDPCTime.setStatus("mandatory")
_CpqOsCpuPercentInterruptTime_Type = Integer32
_CpqOsCpuPercentInterruptTime_Object = MibTableColumn
cpqOsCpuPercentInterruptTime = _CpqOsCpuPercentInterruptTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 3, 2, 1, 11),
    _CpqOsCpuPercentInterruptTime_Type()
)
cpqOsCpuPercentInterruptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCpuPercentInterruptTime.setStatus("mandatory")
_CpqOsMemory_ObjectIdentity = ObjectIdentity
cpqOsMemory = _CpqOsMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4)
)


class _CpqOsMemoryStatus_Type(Integer32):
    """Custom type cpqOsMemoryStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsMemoryStatus_Type.__name__ = "Integer32"
_CpqOsMemoryStatus_Object = MibScalar
cpqOsMemoryStatus = _CpqOsMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 1),
    _CpqOsMemoryStatus_Type()
)
cpqOsMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemoryStatus.setStatus("mandatory")
_CpqOsMemAvailableKBytes_Type = Integer32
_CpqOsMemAvailableKBytes_Object = MibScalar
cpqOsMemAvailableKBytes = _CpqOsMemAvailableKBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 2),
    _CpqOsMemAvailableKBytes_Type()
)
cpqOsMemAvailableKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemAvailableKBytes.setStatus("mandatory")
_CpqOsMemPagesPerSec_Type = Integer32
_CpqOsMemPagesPerSec_Object = MibScalar
cpqOsMemPagesPerSec = _CpqOsMemPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 3),
    _CpqOsMemPagesPerSec_Type()
)
cpqOsMemPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemPagesPerSec.setStatus("mandatory")
_CpqOsMemPagesInputPerSec_Type = Integer32
_CpqOsMemPagesInputPerSec_Object = MibScalar
cpqOsMemPagesInputPerSec = _CpqOsMemPagesInputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 4),
    _CpqOsMemPagesInputPerSec_Type()
)
cpqOsMemPagesInputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemPagesInputPerSec.setStatus("mandatory")
_CpqOsMemPagesOutputPerSec_Type = Integer32
_CpqOsMemPagesOutputPerSec_Object = MibScalar
cpqOsMemPagesOutputPerSec = _CpqOsMemPagesOutputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 5),
    _CpqOsMemPagesOutputPerSec_Type()
)
cpqOsMemPagesOutputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemPagesOutputPerSec.setStatus("mandatory")
_CpqOsMemPageFaultsPerSec_Type = Integer32
_CpqOsMemPageFaultsPerSec_Object = MibScalar
cpqOsMemPageFaultsPerSec = _CpqOsMemPageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 6),
    _CpqOsMemPageFaultsPerSec_Type()
)
cpqOsMemPageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemPageFaultsPerSec.setStatus("mandatory")
_CpqOsMemCacheFaultsPerSec_Type = Integer32
_CpqOsMemCacheFaultsPerSec_Object = MibScalar
cpqOsMemCacheFaultsPerSec = _CpqOsMemCacheFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 7),
    _CpqOsMemCacheFaultsPerSec_Type()
)
cpqOsMemCacheFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemCacheFaultsPerSec.setStatus("mandatory")
_CpqOsMemPageReadsPerSecx1000_Type = Integer32
_CpqOsMemPageReadsPerSecx1000_Object = MibScalar
cpqOsMemPageReadsPerSecx1000 = _CpqOsMemPageReadsPerSecx1000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 8),
    _CpqOsMemPageReadsPerSecx1000_Type()
)
cpqOsMemPageReadsPerSecx1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemPageReadsPerSecx1000.setStatus("mandatory")
_CpqOsMemPageWritesPerSecx1000_Type = Integer32
_CpqOsMemPageWritesPerSecx1000_Object = MibScalar
cpqOsMemPageWritesPerSecx1000 = _CpqOsMemPageWritesPerSecx1000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 9),
    _CpqOsMemPageWritesPerSecx1000_Type()
)
cpqOsMemPageWritesPerSecx1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemPageWritesPerSecx1000.setStatus("mandatory")
_CpqOsMemPoolNonpagedBytes_Type = Integer32
_CpqOsMemPoolNonpagedBytes_Object = MibScalar
cpqOsMemPoolNonpagedBytes = _CpqOsMemPoolNonpagedBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 10),
    _CpqOsMemPoolNonpagedBytes_Type()
)
cpqOsMemPoolNonpagedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemPoolNonpagedBytes.setStatus("mandatory")
_CpqOsMemCacheBytes_Type = Integer32
_CpqOsMemCacheBytes_Object = MibScalar
cpqOsMemCacheBytes = _CpqOsMemCacheBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 4, 11),
    _CpqOsMemCacheBytes_Type()
)
cpqOsMemCacheBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsMemCacheBytes.setStatus("mandatory")
_CpqOsCache_ObjectIdentity = ObjectIdentity
cpqOsCache = _CpqOsCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5)
)


class _CpqOsCacheStatus_Type(Integer32):
    """Custom type cpqOsCacheStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsCacheStatus_Type.__name__ = "Integer32"
_CpqOsCacheStatus_Object = MibScalar
cpqOsCacheStatus = _CpqOsCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 1),
    _CpqOsCacheStatus_Type()
)
cpqOsCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCacheStatus.setStatus("mandatory")
_CpqOsCacheTable_Object = MibTable
cpqOsCacheTable = _CpqOsCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cpqOsCacheTable.setStatus("mandatory")
_CpqOsCacheEntry_Object = MibTableRow
cpqOsCacheEntry = _CpqOsCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1)
)
cpqOsCacheEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsCacheIndex"),
)
if mibBuilder.loadTexts:
    cpqOsCacheEntry.setStatus("mandatory")
_CpqOsCacheIndex_Type = Integer32
_CpqOsCacheIndex_Object = MibTableColumn
cpqOsCacheIndex = _CpqOsCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1, 1),
    _CpqOsCacheIndex_Type()
)
cpqOsCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCacheIndex.setStatus("mandatory")


class _CpqOsCacheInstance_Type(DisplayString):
    """Custom type cpqOsCacheInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsCacheInstance_Type.__name__ = "DisplayString"
_CpqOsCacheInstance_Object = MibTableColumn
cpqOsCacheInstance = _CpqOsCacheInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1, 2),
    _CpqOsCacheInstance_Type()
)
cpqOsCacheInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCacheInstance.setStatus("mandatory")
_CpqOsCacheCopyReadHitsPercent_Type = Integer32
_CpqOsCacheCopyReadHitsPercent_Object = MibTableColumn
cpqOsCacheCopyReadHitsPercent = _CpqOsCacheCopyReadHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1, 3),
    _CpqOsCacheCopyReadHitsPercent_Type()
)
cpqOsCacheCopyReadHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCacheCopyReadHitsPercent.setStatus("mandatory")
_CpqOsWarCacheCopyReadHitsPercent_Type = Integer32
_CpqOsWarCacheCopyReadHitsPercent_Object = MibTableColumn
cpqOsWarCacheCopyReadHitsPercent = _CpqOsWarCacheCopyReadHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1, 4),
    _CpqOsWarCacheCopyReadHitsPercent_Type()
)
cpqOsWarCacheCopyReadHitsPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsWarCacheCopyReadHitsPercent.setStatus("mandatory")
_CpqOsCriCacheCopyReadHitsPercent_Type = Integer32
_CpqOsCriCacheCopyReadHitsPercent_Object = MibTableColumn
cpqOsCriCacheCopyReadHitsPercent = _CpqOsCriCacheCopyReadHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1, 5),
    _CpqOsCriCacheCopyReadHitsPercent_Type()
)
cpqOsCriCacheCopyReadHitsPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsCriCacheCopyReadHitsPercent.setStatus("mandatory")
_CpqOsCacheCopyReadsPerSec_Type = Integer32
_CpqOsCacheCopyReadsPerSec_Object = MibTableColumn
cpqOsCacheCopyReadsPerSec = _CpqOsCacheCopyReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1, 6),
    _CpqOsCacheCopyReadsPerSec_Type()
)
cpqOsCacheCopyReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCacheCopyReadsPerSec.setStatus("mandatory")


class _CpqOsCacheCondition_Type(Integer32):
    """Custom type cpqOsCacheCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsCacheCondition_Type.__name__ = "Integer32"
_CpqOsCacheCondition_Object = MibTableColumn
cpqOsCacheCondition = _CpqOsCacheCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 5, 2, 1, 7),
    _CpqOsCacheCondition_Type()
)
cpqOsCacheCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsCacheCondition.setStatus("mandatory")
_CpqOsPagingFile_ObjectIdentity = ObjectIdentity
cpqOsPagingFile = _CpqOsPagingFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6)
)


class _CpqOsPagingFileStatus_Type(Integer32):
    """Custom type cpqOsPagingFileStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsPagingFileStatus_Type.__name__ = "Integer32"
_CpqOsPagingFileStatus_Object = MibScalar
cpqOsPagingFileStatus = _CpqOsPagingFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 1),
    _CpqOsPagingFileStatus_Type()
)
cpqOsPagingFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPagingFileStatus.setStatus("mandatory")
_CpqOsPagingFileTable_Object = MibTable
cpqOsPagingFileTable = _CpqOsPagingFileTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2)
)
if mibBuilder.loadTexts:
    cpqOsPagingFileTable.setStatus("mandatory")
_CpqOsPagingFileEntry_Object = MibTableRow
cpqOsPagingFileEntry = _CpqOsPagingFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2, 1)
)
cpqOsPagingFileEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsPagingFileIndex"),
)
if mibBuilder.loadTexts:
    cpqOsPagingFileEntry.setStatus("mandatory")
_CpqOsPagingFileIndex_Type = Integer32
_CpqOsPagingFileIndex_Object = MibTableColumn
cpqOsPagingFileIndex = _CpqOsPagingFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2, 1, 1),
    _CpqOsPagingFileIndex_Type()
)
cpqOsPagingFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPagingFileIndex.setStatus("mandatory")


class _CpqOsPagingFileInstance_Type(DisplayString):
    """Custom type cpqOsPagingFileInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsPagingFileInstance_Type.__name__ = "DisplayString"
_CpqOsPagingFileInstance_Object = MibTableColumn
cpqOsPagingFileInstance = _CpqOsPagingFileInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2, 1, 2),
    _CpqOsPagingFileInstance_Type()
)
cpqOsPagingFileInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPagingFileInstance.setStatus("mandatory")
_CpqOsPageFileUsagePercent_Type = Integer32
_CpqOsPageFileUsagePercent_Object = MibTableColumn
cpqOsPageFileUsagePercent = _CpqOsPageFileUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2, 1, 3),
    _CpqOsPageFileUsagePercent_Type()
)
cpqOsPageFileUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPageFileUsagePercent.setStatus("mandatory")
_CpqOsWarPageFileUsagePercent_Type = Integer32
_CpqOsWarPageFileUsagePercent_Object = MibTableColumn
cpqOsWarPageFileUsagePercent = _CpqOsWarPageFileUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2, 1, 4),
    _CpqOsWarPageFileUsagePercent_Type()
)
cpqOsWarPageFileUsagePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsWarPageFileUsagePercent.setStatus("mandatory")
_CpqOsCriPageFileUsagePercent_Type = Integer32
_CpqOsCriPageFileUsagePercent_Object = MibTableColumn
cpqOsCriPageFileUsagePercent = _CpqOsCriPageFileUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2, 1, 5),
    _CpqOsCriPageFileUsagePercent_Type()
)
cpqOsCriPageFileUsagePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsCriPageFileUsagePercent.setStatus("mandatory")


class _CpqOsPagingFileCondition_Type(Integer32):
    """Custom type cpqOsPagingFileCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsPagingFileCondition_Type.__name__ = "Integer32"
_CpqOsPagingFileCondition_Object = MibTableColumn
cpqOsPagingFileCondition = _CpqOsPagingFileCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 6, 2, 1, 6),
    _CpqOsPagingFileCondition_Type()
)
cpqOsPagingFileCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPagingFileCondition.setStatus("mandatory")
_CpqOsPhysicalDisk_ObjectIdentity = ObjectIdentity
cpqOsPhysicalDisk = _CpqOsPhysicalDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7)
)


class _CpqOsPhysicalDiskStatus_Type(Integer32):
    """Custom type cpqOsPhysicalDiskStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsPhysicalDiskStatus_Type.__name__ = "Integer32"
_CpqOsPhysicalDiskStatus_Object = MibScalar
cpqOsPhysicalDiskStatus = _CpqOsPhysicalDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 1),
    _CpqOsPhysicalDiskStatus_Type()
)
cpqOsPhysicalDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskStatus.setStatus("mandatory")
_CpqOsPhysicalDiskTable_Object = MibTable
cpqOsPhysicalDiskTable = _CpqOsPhysicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2)
)
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskTable.setStatus("mandatory")
_CpqOsPhysicalDiskEntry_Object = MibTableRow
cpqOsPhysicalDiskEntry = _CpqOsPhysicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1)
)
cpqOsPhysicalDiskEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsPhysicalDiskIndex"),
)
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskEntry.setStatus("mandatory")
_CpqOsPhysicalDiskIndex_Type = Integer32
_CpqOsPhysicalDiskIndex_Object = MibTableColumn
cpqOsPhysicalDiskIndex = _CpqOsPhysicalDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 1),
    _CpqOsPhysicalDiskIndex_Type()
)
cpqOsPhysicalDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskIndex.setStatus("mandatory")


class _CpqOsPhysicalDiskInstance_Type(DisplayString):
    """Custom type cpqOsPhysicalDiskInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsPhysicalDiskInstance_Type.__name__ = "DisplayString"
_CpqOsPhysicalDiskInstance_Object = MibTableColumn
cpqOsPhysicalDiskInstance = _CpqOsPhysicalDiskInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 2),
    _CpqOsPhysicalDiskInstance_Type()
)
cpqOsPhysicalDiskInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskInstance.setStatus("mandatory")
_CpqOsPhysicalDiskQueueLength_Type = Integer32
_CpqOsPhysicalDiskQueueLength_Object = MibTableColumn
cpqOsPhysicalDiskQueueLength = _CpqOsPhysicalDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 3),
    _CpqOsPhysicalDiskQueueLength_Type()
)
cpqOsPhysicalDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskQueueLength.setStatus("mandatory")
_CpqOsPhysicalDiskBusyTimePercent_Type = Integer32
_CpqOsPhysicalDiskBusyTimePercent_Object = MibTableColumn
cpqOsPhysicalDiskBusyTimePercent = _CpqOsPhysicalDiskBusyTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 4),
    _CpqOsPhysicalDiskBusyTimePercent_Type()
)
cpqOsPhysicalDiskBusyTimePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskBusyTimePercent.setStatus("mandatory")


class _CpqOsPhysicalDiskCondition_Type(Integer32):
    """Custom type cpqOsPhysicalDiskCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsPhysicalDiskCondition_Type.__name__ = "Integer32"
_CpqOsPhysicalDiskCondition_Object = MibTableColumn
cpqOsPhysicalDiskCondition = _CpqOsPhysicalDiskCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 5),
    _CpqOsPhysicalDiskCondition_Type()
)
cpqOsPhysicalDiskCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskCondition.setStatus("mandatory")
_CpqOsPhysicalDiskBytesPersec_Type = Integer32
_CpqOsPhysicalDiskBytesPersec_Object = MibTableColumn
cpqOsPhysicalDiskBytesPersec = _CpqOsPhysicalDiskBytesPersec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 6),
    _CpqOsPhysicalDiskBytesPersec_Type()
)
cpqOsPhysicalDiskBytesPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskBytesPersec.setStatus("mandatory")
_CpqOsPhysicalDiskTransfersPersecx1000_Type = Integer32
_CpqOsPhysicalDiskTransfersPersecx1000_Object = MibTableColumn
cpqOsPhysicalDiskTransfersPersecx1000 = _CpqOsPhysicalDiskTransfersPersecx1000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 7),
    _CpqOsPhysicalDiskTransfersPersecx1000_Type()
)
cpqOsPhysicalDiskTransfersPersecx1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskTransfersPersecx1000.setStatus("mandatory")
_CpqOsPhysicalDiskReadsPersecx1000_Type = Integer32
_CpqOsPhysicalDiskReadsPersecx1000_Object = MibTableColumn
cpqOsPhysicalDiskReadsPersecx1000 = _CpqOsPhysicalDiskReadsPersecx1000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 8),
    _CpqOsPhysicalDiskReadsPersecx1000_Type()
)
cpqOsPhysicalDiskReadsPersecx1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskReadsPersecx1000.setStatus("mandatory")
_CpqOsPhysicalDiskWritesPersecx1000_Type = Integer32
_CpqOsPhysicalDiskWritesPersecx1000_Object = MibTableColumn
cpqOsPhysicalDiskWritesPersecx1000 = _CpqOsPhysicalDiskWritesPersecx1000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 9),
    _CpqOsPhysicalDiskWritesPersecx1000_Type()
)
cpqOsPhysicalDiskWritesPersecx1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskWritesPersecx1000.setStatus("mandatory")
_CpqOsPhysicalDiskReadBytesPersec_Type = Integer32
_CpqOsPhysicalDiskReadBytesPersec_Object = MibTableColumn
cpqOsPhysicalDiskReadBytesPersec = _CpqOsPhysicalDiskReadBytesPersec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 10),
    _CpqOsPhysicalDiskReadBytesPersec_Type()
)
cpqOsPhysicalDiskReadBytesPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskReadBytesPersec.setStatus("mandatory")
_CpqOsPhysicalDiskWriteBytesPersec_Type = Integer32
_CpqOsPhysicalDiskWriteBytesPersec_Object = MibTableColumn
cpqOsPhysicalDiskWriteBytesPersec = _CpqOsPhysicalDiskWriteBytesPersec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 11),
    _CpqOsPhysicalDiskWriteBytesPersec_Type()
)
cpqOsPhysicalDiskWriteBytesPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskWriteBytesPersec.setStatus("mandatory")
_CpqOsPhysicalDiskAvgDisksecPerReadx10000_Type = Integer32
_CpqOsPhysicalDiskAvgDisksecPerReadx10000_Object = MibTableColumn
cpqOsPhysicalDiskAvgDisksecPerReadx10000 = _CpqOsPhysicalDiskAvgDisksecPerReadx10000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 12),
    _CpqOsPhysicalDiskAvgDisksecPerReadx10000_Type()
)
cpqOsPhysicalDiskAvgDisksecPerReadx10000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskAvgDisksecPerReadx10000.setStatus("mandatory")
_CpqOsPhysicalDiskAvgDisksecPerWritex10000_Type = Integer32
_CpqOsPhysicalDiskAvgDisksecPerWritex10000_Object = MibTableColumn
cpqOsPhysicalDiskAvgDisksecPerWritex10000 = _CpqOsPhysicalDiskAvgDisksecPerWritex10000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 13),
    _CpqOsPhysicalDiskAvgDisksecPerWritex10000_Type()
)
cpqOsPhysicalDiskAvgDisksecPerWritex10000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskAvgDisksecPerWritex10000.setStatus("mandatory")
_CpqOsPhysicalDiskCurrentDiskQueueLength_Type = Integer32
_CpqOsPhysicalDiskCurrentDiskQueueLength_Object = MibTableColumn
cpqOsPhysicalDiskCurrentDiskQueueLength = _CpqOsPhysicalDiskCurrentDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 7, 2, 1, 14),
    _CpqOsPhysicalDiskCurrentDiskQueueLength_Type()
)
cpqOsPhysicalDiskCurrentDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsPhysicalDiskCurrentDiskQueueLength.setStatus("mandatory")
_CpqOsLogicalDisk_ObjectIdentity = ObjectIdentity
cpqOsLogicalDisk = _CpqOsLogicalDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8)
)


class _CpqOsLogicalDiskStatus_Type(Integer32):
    """Custom type cpqOsLogicalDiskStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsLogicalDiskStatus_Type.__name__ = "Integer32"
_CpqOsLogicalDiskStatus_Object = MibScalar
cpqOsLogicalDiskStatus = _CpqOsLogicalDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 1),
    _CpqOsLogicalDiskStatus_Type()
)
cpqOsLogicalDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskStatus.setStatus("mandatory")
_CpqOsLogicalDiskTable_Object = MibTable
cpqOsLogicalDiskTable = _CpqOsLogicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2)
)
if mibBuilder.loadTexts:
    cpqOsLogicalDiskTable.setStatus("mandatory")
_CpqOsLogicalDiskEntry_Object = MibTableRow
cpqOsLogicalDiskEntry = _CpqOsLogicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1)
)
cpqOsLogicalDiskEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsLogicalDiskIndex"),
)
if mibBuilder.loadTexts:
    cpqOsLogicalDiskEntry.setStatus("mandatory")
_CpqOsLogicalDiskIndex_Type = Integer32
_CpqOsLogicalDiskIndex_Object = MibTableColumn
cpqOsLogicalDiskIndex = _CpqOsLogicalDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 1),
    _CpqOsLogicalDiskIndex_Type()
)
cpqOsLogicalDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskIndex.setStatus("mandatory")


class _CpqOsLogicalDiskInstance_Type(DisplayString):
    """Custom type cpqOsLogicalDiskInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsLogicalDiskInstance_Type.__name__ = "DisplayString"
_CpqOsLogicalDiskInstance_Object = MibTableColumn
cpqOsLogicalDiskInstance = _CpqOsLogicalDiskInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 2),
    _CpqOsLogicalDiskInstance_Type()
)
cpqOsLogicalDiskInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskInstance.setStatus("mandatory")
_CpqOsLogicalDiskFreeSpaceMBytes_Type = Integer32
_CpqOsLogicalDiskFreeSpaceMBytes_Object = MibTableColumn
cpqOsLogicalDiskFreeSpaceMBytes = _CpqOsLogicalDiskFreeSpaceMBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 3),
    _CpqOsLogicalDiskFreeSpaceMBytes_Type()
)
cpqOsLogicalDiskFreeSpaceMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskFreeSpaceMBytes.setStatus("mandatory")
_CpqOsLogicalDiskFreeSpacePercent_Type = Integer32
_CpqOsLogicalDiskFreeSpacePercent_Object = MibTableColumn
cpqOsLogicalDiskFreeSpacePercent = _CpqOsLogicalDiskFreeSpacePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 4),
    _CpqOsLogicalDiskFreeSpacePercent_Type()
)
cpqOsLogicalDiskFreeSpacePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskFreeSpacePercent.setStatus("mandatory")
_CpqOsLogicalDiskQueueLength_Type = Integer32
_CpqOsLogicalDiskQueueLength_Object = MibTableColumn
cpqOsLogicalDiskQueueLength = _CpqOsLogicalDiskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 5),
    _CpqOsLogicalDiskQueueLength_Type()
)
cpqOsLogicalDiskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskQueueLength.setStatus("mandatory")
_CpqOsLogicalDiskBusyTimePercent_Type = Integer32
_CpqOsLogicalDiskBusyTimePercent_Object = MibTableColumn
cpqOsLogicalDiskBusyTimePercent = _CpqOsLogicalDiskBusyTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 6),
    _CpqOsLogicalDiskBusyTimePercent_Type()
)
cpqOsLogicalDiskBusyTimePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskBusyTimePercent.setStatus("mandatory")
_CpqOsWarLogicalDiskBusyTimePercent_Type = Integer32
_CpqOsWarLogicalDiskBusyTimePercent_Object = MibTableColumn
cpqOsWarLogicalDiskBusyTimePercent = _CpqOsWarLogicalDiskBusyTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 7),
    _CpqOsWarLogicalDiskBusyTimePercent_Type()
)
cpqOsWarLogicalDiskBusyTimePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsWarLogicalDiskBusyTimePercent.setStatus("mandatory")
_CpqOsCriLogicalDiskBusyTimePercent_Type = Integer32
_CpqOsCriLogicalDiskBusyTimePercent_Object = MibTableColumn
cpqOsCriLogicalDiskBusyTimePercent = _CpqOsCriLogicalDiskBusyTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 8),
    _CpqOsCriLogicalDiskBusyTimePercent_Type()
)
cpqOsCriLogicalDiskBusyTimePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqOsCriLogicalDiskBusyTimePercent.setStatus("mandatory")


class _CpqOsLogicalDiskCondition_Type(Integer32):
    """Custom type cpqOsLogicalDiskCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsLogicalDiskCondition_Type.__name__ = "Integer32"
_CpqOsLogicalDiskCondition_Object = MibTableColumn
cpqOsLogicalDiskCondition = _CpqOsLogicalDiskCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 8, 2, 1, 9),
    _CpqOsLogicalDiskCondition_Type()
)
cpqOsLogicalDiskCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsLogicalDiskCondition.setStatus("mandatory")
_CpqOsServer_ObjectIdentity = ObjectIdentity
cpqOsServer = _CpqOsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9)
)


class _CpqOsServerStatus_Type(Integer32):
    """Custom type cpqOsServerStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsServerStatus_Type.__name__ = "Integer32"
_CpqOsServerStatus_Object = MibScalar
cpqOsServerStatus = _CpqOsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 1),
    _CpqOsServerStatus_Type()
)
cpqOsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerStatus.setStatus("mandatory")
_CpqOsServerTotalNetworkUtilizationBytesPerSec_Type = Integer32
_CpqOsServerTotalNetworkUtilizationBytesPerSec_Object = MibScalar
cpqOsServerTotalNetworkUtilizationBytesPerSec = _CpqOsServerTotalNetworkUtilizationBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 2),
    _CpqOsServerTotalNetworkUtilizationBytesPerSec_Type()
)
cpqOsServerTotalNetworkUtilizationBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerTotalNetworkUtilizationBytesPerSec.setStatus("mandatory")
_CpqOsServerSessions_Type = Integer32
_CpqOsServerSessions_Object = MibScalar
cpqOsServerSessions = _CpqOsServerSessions_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 3),
    _CpqOsServerSessions_Type()
)
cpqOsServerSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerSessions.setStatus("mandatory")
_CpqOsServerAccessPermissionErrors_Type = Integer32
_CpqOsServerAccessPermissionErrors_Object = MibScalar
cpqOsServerAccessPermissionErrors = _CpqOsServerAccessPermissionErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 4),
    _CpqOsServerAccessPermissionErrors_Type()
)
cpqOsServerAccessPermissionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerAccessPermissionErrors.setStatus("mandatory")
_CpqOsServerAccessGrantedErrors_Type = Integer32
_CpqOsServerAccessGrantedErrors_Object = MibScalar
cpqOsServerAccessGrantedErrors = _CpqOsServerAccessGrantedErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 5),
    _CpqOsServerAccessGrantedErrors_Type()
)
cpqOsServerAccessGrantedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerAccessGrantedErrors.setStatus("mandatory")
_CpqOsServerLogonErrors_Type = Integer32
_CpqOsServerLogonErrors_Object = MibScalar
cpqOsServerLogonErrors = _CpqOsServerLogonErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 6),
    _CpqOsServerLogonErrors_Type()
)
cpqOsServerLogonErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerLogonErrors.setStatus("mandatory")
_CpqOsServerSessionsErroredOut_Type = Integer32
_CpqOsServerSessionsErroredOut_Object = MibScalar
cpqOsServerSessionsErroredOut = _CpqOsServerSessionsErroredOut_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 7),
    _CpqOsServerSessionsErroredOut_Type()
)
cpqOsServerSessionsErroredOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerSessionsErroredOut.setStatus("mandatory")
_CpqOsServerContextBlocksQueuePerSec_Type = Integer32
_CpqOsServerContextBlocksQueuePerSec_Object = MibScalar
cpqOsServerContextBlocksQueuePerSec = _CpqOsServerContextBlocksQueuePerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 9, 8),
    _CpqOsServerContextBlocksQueuePerSec_Type()
)
cpqOsServerContextBlocksQueuePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsServerContextBlocksQueuePerSec.setStatus("mandatory")
_CpqOsNetworkInterface_ObjectIdentity = ObjectIdentity
cpqOsNetworkInterface = _CpqOsNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10)
)


class _CpqOsNetworkInterfaceStatus_Type(Integer32):
    """Custom type cpqOsNetworkInterfaceStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsNetworkInterfaceStatus_Type.__name__ = "Integer32"
_CpqOsNetworkInterfaceStatus_Object = MibScalar
cpqOsNetworkInterfaceStatus = _CpqOsNetworkInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 1),
    _CpqOsNetworkInterfaceStatus_Type()
)
cpqOsNetworkInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkInterfaceStatus.setStatus("mandatory")
_CpqOsNetworkInterfaceTable_Object = MibTable
cpqOsNetworkInterfaceTable = _CpqOsNetworkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2)
)
if mibBuilder.loadTexts:
    cpqOsNetworkInterfaceTable.setStatus("mandatory")
_CpqOsNetworkInterfaceEntry_Object = MibTableRow
cpqOsNetworkInterfaceEntry = _CpqOsNetworkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1)
)
cpqOsNetworkInterfaceEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsNetworkInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cpqOsNetworkInterfaceEntry.setStatus("mandatory")
_CpqOsNetworkInterfaceIndex_Type = Integer32
_CpqOsNetworkInterfaceIndex_Object = MibTableColumn
cpqOsNetworkInterfaceIndex = _CpqOsNetworkInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 1),
    _CpqOsNetworkInterfaceIndex_Type()
)
cpqOsNetworkInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkInterfaceIndex.setStatus("mandatory")


class _CpqOsNetworkInterfaceInstance_Type(DisplayString):
    """Custom type cpqOsNetworkInterfaceInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsNetworkInterfaceInstance_Type.__name__ = "DisplayString"
_CpqOsNetworkInterfaceInstance_Object = MibTableColumn
cpqOsNetworkInterfaceInstance = _CpqOsNetworkInterfaceInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 2),
    _CpqOsNetworkInterfaceInstance_Type()
)
cpqOsNetworkInterfaceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkInterfaceInstance.setStatus("mandatory")
_CpqOsNetworkTotalBytesPerSec_Type = Integer32
_CpqOsNetworkTotalBytesPerSec_Object = MibTableColumn
cpqOsNetworkTotalBytesPerSec = _CpqOsNetworkTotalBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 3),
    _CpqOsNetworkTotalBytesPerSec_Type()
)
cpqOsNetworkTotalBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkTotalBytesPerSec.setStatus("mandatory")
_CpqOsNetworkPacketsPerSec_Type = Integer32
_CpqOsNetworkPacketsPerSec_Object = MibTableColumn
cpqOsNetworkPacketsPerSec = _CpqOsNetworkPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 4),
    _CpqOsNetworkPacketsPerSec_Type()
)
cpqOsNetworkPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkPacketsPerSec.setStatus("mandatory")
_CpqOsNetworkOutputQueueLength_Type = Integer32
_CpqOsNetworkOutputQueueLength_Object = MibTableColumn
cpqOsNetworkOutputQueueLength = _CpqOsNetworkOutputQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 5),
    _CpqOsNetworkOutputQueueLength_Type()
)
cpqOsNetworkOutputQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkOutputQueueLength.setStatus("mandatory")
_CpqOsNetworkPktOutboundErrors_Type = Integer32
_CpqOsNetworkPktOutboundErrors_Object = MibTableColumn
cpqOsNetworkPktOutboundErrors = _CpqOsNetworkPktOutboundErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 6),
    _CpqOsNetworkPktOutboundErrors_Type()
)
cpqOsNetworkPktOutboundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkPktOutboundErrors.setStatus("mandatory")
_CpqOsNetworkPktReceiveErrors_Type = Integer32
_CpqOsNetworkPktReceiveErrors_Object = MibTableColumn
cpqOsNetworkPktReceiveErrors = _CpqOsNetworkPktReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 7),
    _CpqOsNetworkPktReceiveErrors_Type()
)
cpqOsNetworkPktReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkPktReceiveErrors.setStatus("mandatory")
_CpqOsNetworkCurrentBandWidth_Type = Integer32
_CpqOsNetworkCurrentBandWidth_Object = MibTableColumn
cpqOsNetworkCurrentBandWidth = _CpqOsNetworkCurrentBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 8),
    _CpqOsNetworkCurrentBandWidth_Type()
)
cpqOsNetworkCurrentBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkCurrentBandWidth.setStatus("mandatory")


class _CpqOsNetworkInterfaceCondition_Type(Integer32):
    """Custom type cpqOsNetworkInterfaceCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsNetworkInterfaceCondition_Type.__name__ = "Integer32"
_CpqOsNetworkInterfaceCondition_Object = MibTableColumn
cpqOsNetworkInterfaceCondition = _CpqOsNetworkInterfaceCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 9),
    _CpqOsNetworkInterfaceCondition_Type()
)
cpqOsNetworkInterfaceCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkInterfaceCondition.setStatus("mandatory")
_CpqOsNetworkBytesSentPersec_Type = Integer32
_CpqOsNetworkBytesSentPersec_Object = MibTableColumn
cpqOsNetworkBytesSentPersec = _CpqOsNetworkBytesSentPersec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 10),
    _CpqOsNetworkBytesSentPersec_Type()
)
cpqOsNetworkBytesSentPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkBytesSentPersec.setStatus("mandatory")
_CpqOsNetworkBytesReceivedPersec_Type = Integer32
_CpqOsNetworkBytesReceivedPersec_Object = MibTableColumn
cpqOsNetworkBytesReceivedPersec = _CpqOsNetworkBytesReceivedPersec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 11),
    _CpqOsNetworkBytesReceivedPersec_Type()
)
cpqOsNetworkBytesReceivedPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkBytesReceivedPersec.setStatus("mandatory")
_CpqOsNetworkPacketsSentPersecx1000_Type = Integer32
_CpqOsNetworkPacketsSentPersecx1000_Object = MibTableColumn
cpqOsNetworkPacketsSentPersecx1000 = _CpqOsNetworkPacketsSentPersecx1000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 12),
    _CpqOsNetworkPacketsSentPersecx1000_Type()
)
cpqOsNetworkPacketsSentPersecx1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkPacketsSentPersecx1000.setStatus("mandatory")
_CpqOsNetworkPacketsReceivedPersecx1000_Type = Integer32
_CpqOsNetworkPacketsReceivedPersecx1000_Object = MibTableColumn
cpqOsNetworkPacketsReceivedPersecx1000 = _CpqOsNetworkPacketsReceivedPersecx1000_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 10, 2, 1, 13),
    _CpqOsNetworkPacketsReceivedPersecx1000_Type()
)
cpqOsNetworkPacketsReceivedPersecx1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsNetworkPacketsReceivedPersecx1000.setStatus("mandatory")
_CpqOsTcp_ObjectIdentity = ObjectIdentity
cpqOsTcp = _CpqOsTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11)
)


class _CpqOsTcpStatus_Type(Integer32):
    """Custom type cpqOsTcpStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsTcpStatus_Type.__name__ = "Integer32"
_CpqOsTcpStatus_Object = MibScalar
cpqOsTcpStatus = _CpqOsTcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 1),
    _CpqOsTcpStatus_Type()
)
cpqOsTcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpStatus.setStatus("mandatory")
_CpqOsTcpTable_Object = MibTable
cpqOsTcpTable = _CpqOsTcpTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2)
)
if mibBuilder.loadTexts:
    cpqOsTcpTable.setStatus("mandatory")
_CpqOsTcpEntry_Object = MibTableRow
cpqOsTcpEntry = _CpqOsTcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1)
)
cpqOsTcpEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsTcpIndex"),
)
if mibBuilder.loadTexts:
    cpqOsTcpEntry.setStatus("mandatory")
_CpqOsTcpIndex_Type = Integer32
_CpqOsTcpIndex_Object = MibTableColumn
cpqOsTcpIndex = _CpqOsTcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 1),
    _CpqOsTcpIndex_Type()
)
cpqOsTcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpIndex.setStatus("mandatory")


class _CpqOsTcpInstance_Type(DisplayString):
    """Custom type cpqOsTcpInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsTcpInstance_Type.__name__ = "DisplayString"
_CpqOsTcpInstance_Object = MibTableColumn
cpqOsTcpInstance = _CpqOsTcpInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 2),
    _CpqOsTcpInstance_Type()
)
cpqOsTcpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpInstance.setStatus("mandatory")
_CpqOsTcpActiveConnections_Type = Integer32
_CpqOsTcpActiveConnections_Object = MibTableColumn
cpqOsTcpActiveConnections = _CpqOsTcpActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 3),
    _CpqOsTcpActiveConnections_Type()
)
cpqOsTcpActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpActiveConnections.setStatus("mandatory")
_CpqOsTcpEstablishedConections_Type = Integer32
_CpqOsTcpEstablishedConections_Object = MibTableColumn
cpqOsTcpEstablishedConections = _CpqOsTcpEstablishedConections_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 4),
    _CpqOsTcpEstablishedConections_Type()
)
cpqOsTcpEstablishedConections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpEstablishedConections.setStatus("mandatory")
_CpqOsTcpSegmentsPerSec_Type = Integer32
_CpqOsTcpSegmentsPerSec_Object = MibTableColumn
cpqOsTcpSegmentsPerSec = _CpqOsTcpSegmentsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 5),
    _CpqOsTcpSegmentsPerSec_Type()
)
cpqOsTcpSegmentsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpSegmentsPerSec.setStatus("mandatory")
_CpqOsTcpRetransmittedSegmentsPerSec_Type = Integer32
_CpqOsTcpRetransmittedSegmentsPerSec_Object = MibTableColumn
cpqOsTcpRetransmittedSegmentsPerSec = _CpqOsTcpRetransmittedSegmentsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 6),
    _CpqOsTcpRetransmittedSegmentsPerSec_Type()
)
cpqOsTcpRetransmittedSegmentsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpRetransmittedSegmentsPerSec.setStatus("mandatory")
_CpqOsTcpConnectionFailures_Type = Integer32
_CpqOsTcpConnectionFailures_Object = MibTableColumn
cpqOsTcpConnectionFailures = _CpqOsTcpConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 7),
    _CpqOsTcpConnectionFailures_Type()
)
cpqOsTcpConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpConnectionFailures.setStatus("mandatory")


class _CpqOsTcpCondition_Type(Integer32):
    """Custom type cpqOsTcpCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsTcpCondition_Type.__name__ = "Integer32"
_CpqOsTcpCondition_Object = MibTableColumn
cpqOsTcpCondition = _CpqOsTcpCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 11, 2, 1, 8),
    _CpqOsTcpCondition_Type()
)
cpqOsTcpCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsTcpCondition.setStatus("mandatory")
_CpqOsProcess_ObjectIdentity = ObjectIdentity
cpqOsProcess = _CpqOsProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12)
)


class _CpqOsProcessStatus_Type(Integer32):
    """Custom type cpqOsProcessStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsProcessStatus_Type.__name__ = "Integer32"
_CpqOsProcessStatus_Object = MibScalar
cpqOsProcessStatus = _CpqOsProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 1),
    _CpqOsProcessStatus_Type()
)
cpqOsProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessStatus.setStatus("mandatory")
_CpqOsProcessTable_Object = MibTable
cpqOsProcessTable = _CpqOsProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2)
)
if mibBuilder.loadTexts:
    cpqOsProcessTable.setStatus("mandatory")
_CpqOsProcessEntry_Object = MibTableRow
cpqOsProcessEntry = _CpqOsProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1)
)
cpqOsProcessEntry.setIndexNames(
    (0, "CPQOS-MIB", "cpqOsProcessIndex"),
)
if mibBuilder.loadTexts:
    cpqOsProcessEntry.setStatus("mandatory")
_CpqOsProcessIndex_Type = Integer32
_CpqOsProcessIndex_Object = MibTableColumn
cpqOsProcessIndex = _CpqOsProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 1),
    _CpqOsProcessIndex_Type()
)
cpqOsProcessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessIndex.setStatus("mandatory")


class _CpqOsProcessInstance_Type(DisplayString):
    """Custom type cpqOsProcessInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqOsProcessInstance_Type.__name__ = "DisplayString"
_CpqOsProcessInstance_Object = MibTableColumn
cpqOsProcessInstance = _CpqOsProcessInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 2),
    _CpqOsProcessInstance_Type()
)
cpqOsProcessInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessInstance.setStatus("mandatory")
_CpqOsProcessThreadCount_Type = Integer32
_CpqOsProcessThreadCount_Object = MibTableColumn
cpqOsProcessThreadCount = _CpqOsProcessThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 3),
    _CpqOsProcessThreadCount_Type()
)
cpqOsProcessThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessThreadCount.setStatus("mandatory")
_CpqOsProcessPrivateBytes_Type = Integer32
_CpqOsProcessPrivateBytes_Object = MibTableColumn
cpqOsProcessPrivateBytes = _CpqOsProcessPrivateBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 4),
    _CpqOsProcessPrivateBytes_Type()
)
cpqOsProcessPrivateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessPrivateBytes.setStatus("mandatory")
_CpqOsProcessPageFileBytes_Type = Integer32
_CpqOsProcessPageFileBytes_Object = MibTableColumn
cpqOsProcessPageFileBytes = _CpqOsProcessPageFileBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 5),
    _CpqOsProcessPageFileBytes_Type()
)
cpqOsProcessPageFileBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessPageFileBytes.setStatus("mandatory")
_CpqOsProcessWorkingSet_Type = Integer32
_CpqOsProcessWorkingSet_Object = MibTableColumn
cpqOsProcessWorkingSet = _CpqOsProcessWorkingSet_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 6),
    _CpqOsProcessWorkingSet_Type()
)
cpqOsProcessWorkingSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessWorkingSet.setStatus("mandatory")
_CpqOsProcessCpuTimePercent_Type = Integer32
_CpqOsProcessCpuTimePercent_Object = MibTableColumn
cpqOsProcessCpuTimePercent = _CpqOsProcessCpuTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 7),
    _CpqOsProcessCpuTimePercent_Type()
)
cpqOsProcessCpuTimePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessCpuTimePercent.setStatus("mandatory")
_CpqOsProcessPrivilegedTimePercent_Type = Integer32
_CpqOsProcessPrivilegedTimePercent_Object = MibTableColumn
cpqOsProcessPrivilegedTimePercent = _CpqOsProcessPrivilegedTimePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 8),
    _CpqOsProcessPrivilegedTimePercent_Type()
)
cpqOsProcessPrivilegedTimePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessPrivilegedTimePercent.setStatus("mandatory")
_CpqOsProcessPageFaultsPerSec_Type = Integer32
_CpqOsProcessPageFaultsPerSec_Object = MibTableColumn
cpqOsProcessPageFaultsPerSec = _CpqOsProcessPageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 9),
    _CpqOsProcessPageFaultsPerSec_Type()
)
cpqOsProcessPageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessPageFaultsPerSec.setStatus("mandatory")


class _CpqOsProcessCondition_Type(Integer32):
    """Custom type cpqOsProcessCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqOsProcessCondition_Type.__name__ = "Integer32"
_CpqOsProcessCondition_Object = MibTableColumn
cpqOsProcessCondition = _CpqOsProcessCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 19, 2, 12, 2, 1, 10),
    _CpqOsProcessCondition_Type()
)
cpqOsProcessCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqOsProcessCondition.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqOsCpuTimeDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19001)
)
cpqOsCpuTimeDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsCpuIndex"),
        ("CPQOS-MIB", "cpqOsCpuInstance"),
        ("CPQOS-MIB", "cpqOsCpuTimePercent"))
)
if mibBuilder.loadTexts:
    cpqOsCpuTimeDegraded.setStatus(
        ""
    )

cpqOsCpuTimeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19002)
)
cpqOsCpuTimeFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsCpuIndex"),
        ("CPQOS-MIB", "cpqOsCpuInstance"),
        ("CPQOS-MIB", "cpqOsCpuTimePercent"))
)
if mibBuilder.loadTexts:
    cpqOsCpuTimeFailed.setStatus(
        ""
    )

cpqOsCacheCopyReadHitsDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19003)
)
cpqOsCacheCopyReadHitsDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsCacheIndex"),
        ("CPQOS-MIB", "cpqOsCacheInstance"),
        ("CPQOS-MIB", "cpqOsCacheCopyReadHitsPercent"))
)
if mibBuilder.loadTexts:
    cpqOsCacheCopyReadHitsDegraded.setStatus(
        ""
    )

cpqOsCacheCopyReadHitsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19004)
)
cpqOsCacheCopyReadHitsFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsCacheIndex"),
        ("CPQOS-MIB", "cpqOsCacheInstance"),
        ("CPQOS-MIB", "cpqOsCacheCopyReadHitsPercent"))
)
if mibBuilder.loadTexts:
    cpqOsCacheCopyReadHitsFailed.setStatus(
        ""
    )

cpqOsPageFileUsageDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19005)
)
cpqOsPageFileUsageDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsPagingFileIndex"),
        ("CPQOS-MIB", "cpqOsPagingFileInstance"),
        ("CPQOS-MIB", "cpqOsPageFileUsagePercent"))
)
if mibBuilder.loadTexts:
    cpqOsPageFileUsageDegraded.setStatus(
        ""
    )

cpqOsPageFileUsageFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19006)
)
cpqOsPageFileUsageFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsPagingFileIndex"),
        ("CPQOS-MIB", "cpqOsPagingFileInstance"),
        ("CPQOS-MIB", "cpqOsPageFileUsagePercent"))
)
if mibBuilder.loadTexts:
    cpqOsPageFileUsageFailed.setStatus(
        ""
    )

cpqOsLogicalDiskBusyTimeDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19007)
)
cpqOsLogicalDiskBusyTimeDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsLogicalDiskIndex"),
        ("CPQOS-MIB", "cpqOsLogicalDiskInstance"),
        ("CPQOS-MIB", "cpqOsLogicalDiskBusyTimePercent"))
)
if mibBuilder.loadTexts:
    cpqOsLogicalDiskBusyTimeDegraded.setStatus(
        ""
    )

cpqOsLogicalDiskBusyTimeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 19008)
)
cpqOsLogicalDiskBusyTimeFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQOS-MIB", "cpqOsLogicalDiskIndex"),
        ("CPQOS-MIB", "cpqOsLogicalDiskInstance"),
        ("CPQOS-MIB", "cpqOsLogicalDiskBusyTimePercent"))
)
if mibBuilder.loadTexts:
    cpqOsLogicalDiskBusyTimeFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQOS-MIB",
    **{"cpqOsCpuTimeDegraded": cpqOsCpuTimeDegraded,
       "cpqOsCpuTimeFailed": cpqOsCpuTimeFailed,
       "cpqOsCacheCopyReadHitsDegraded": cpqOsCacheCopyReadHitsDegraded,
       "cpqOsCacheCopyReadHitsFailed": cpqOsCacheCopyReadHitsFailed,
       "cpqOsPageFileUsageDegraded": cpqOsPageFileUsageDegraded,
       "cpqOsPageFileUsageFailed": cpqOsPageFileUsageFailed,
       "cpqOsLogicalDiskBusyTimeDegraded": cpqOsLogicalDiskBusyTimeDegraded,
       "cpqOsLogicalDiskBusyTimeFailed": cpqOsLogicalDiskBusyTimeFailed,
       "cpqWinOsMgmt": cpqWinOsMgmt,
       "cpqOsMibRev": cpqOsMibRev,
       "cpqOsMibRevMajor": cpqOsMibRevMajor,
       "cpqOsMibRevMinor": cpqOsMibRevMinor,
       "cpqOsMibCondition": cpqOsMibCondition,
       "cpqOsComponent": cpqOsComponent,
       "cpqOsInterface": cpqOsInterface,
       "cpqOsCommon": cpqOsCommon,
       "cpqOsCommonPollFreq": cpqOsCommonPollFreq,
       "cpqOsSystem": cpqOsSystem,
       "cpqOsSystemStatus": cpqOsSystemStatus,
       "cpqOsSystemUpTime": cpqOsSystemUpTime,
       "cpqOsSystemThreads": cpqOsSystemThreads,
       "cpqOsSysContextSwitchesPersec": cpqOsSysContextSwitchesPersec,
       "cpqOsSysCpuQueueLength": cpqOsSysCpuQueueLength,
       "cpqOsSysProcesses": cpqOsSysProcesses,
       "cpqOsSysRegistryInUsePercent": cpqOsSysRegistryInUsePercent,
       "cpqOsProcessor": cpqOsProcessor,
       "cpqOsProcessorStatus": cpqOsProcessorStatus,
       "cpqOsProcessorTable": cpqOsProcessorTable,
       "cpqOsProcessorEntry": cpqOsProcessorEntry,
       "cpqOsCpuIndex": cpqOsCpuIndex,
       "cpqOsCpuInstance": cpqOsCpuInstance,
       "cpqOsCpuInterruptsPerSec": cpqOsCpuInterruptsPerSec,
       "cpqOsCpuTimePercent": cpqOsCpuTimePercent,
       "cpqOsWarCpuTimePercent": cpqOsWarCpuTimePercent,
       "cpqOsCriCpuTimePercent": cpqOsCriCpuTimePercent,
       "cpqOsCpuUserTimePercent": cpqOsCpuUserTimePercent,
       "cpqOsCpuPrivilegedTimePercent": cpqOsCpuPrivilegedTimePercent,
       "cpqOsCpuCondition": cpqOsCpuCondition,
       "cpqOsCpuPercentDPCTime": cpqOsCpuPercentDPCTime,
       "cpqOsCpuPercentInterruptTime": cpqOsCpuPercentInterruptTime,
       "cpqOsMemory": cpqOsMemory,
       "cpqOsMemoryStatus": cpqOsMemoryStatus,
       "cpqOsMemAvailableKBytes": cpqOsMemAvailableKBytes,
       "cpqOsMemPagesPerSec": cpqOsMemPagesPerSec,
       "cpqOsMemPagesInputPerSec": cpqOsMemPagesInputPerSec,
       "cpqOsMemPagesOutputPerSec": cpqOsMemPagesOutputPerSec,
       "cpqOsMemPageFaultsPerSec": cpqOsMemPageFaultsPerSec,
       "cpqOsMemCacheFaultsPerSec": cpqOsMemCacheFaultsPerSec,
       "cpqOsMemPageReadsPerSecx1000": cpqOsMemPageReadsPerSecx1000,
       "cpqOsMemPageWritesPerSecx1000": cpqOsMemPageWritesPerSecx1000,
       "cpqOsMemPoolNonpagedBytes": cpqOsMemPoolNonpagedBytes,
       "cpqOsMemCacheBytes": cpqOsMemCacheBytes,
       "cpqOsCache": cpqOsCache,
       "cpqOsCacheStatus": cpqOsCacheStatus,
       "cpqOsCacheTable": cpqOsCacheTable,
       "cpqOsCacheEntry": cpqOsCacheEntry,
       "cpqOsCacheIndex": cpqOsCacheIndex,
       "cpqOsCacheInstance": cpqOsCacheInstance,
       "cpqOsCacheCopyReadHitsPercent": cpqOsCacheCopyReadHitsPercent,
       "cpqOsWarCacheCopyReadHitsPercent": cpqOsWarCacheCopyReadHitsPercent,
       "cpqOsCriCacheCopyReadHitsPercent": cpqOsCriCacheCopyReadHitsPercent,
       "cpqOsCacheCopyReadsPerSec": cpqOsCacheCopyReadsPerSec,
       "cpqOsCacheCondition": cpqOsCacheCondition,
       "cpqOsPagingFile": cpqOsPagingFile,
       "cpqOsPagingFileStatus": cpqOsPagingFileStatus,
       "cpqOsPagingFileTable": cpqOsPagingFileTable,
       "cpqOsPagingFileEntry": cpqOsPagingFileEntry,
       "cpqOsPagingFileIndex": cpqOsPagingFileIndex,
       "cpqOsPagingFileInstance": cpqOsPagingFileInstance,
       "cpqOsPageFileUsagePercent": cpqOsPageFileUsagePercent,
       "cpqOsWarPageFileUsagePercent": cpqOsWarPageFileUsagePercent,
       "cpqOsCriPageFileUsagePercent": cpqOsCriPageFileUsagePercent,
       "cpqOsPagingFileCondition": cpqOsPagingFileCondition,
       "cpqOsPhysicalDisk": cpqOsPhysicalDisk,
       "cpqOsPhysicalDiskStatus": cpqOsPhysicalDiskStatus,
       "cpqOsPhysicalDiskTable": cpqOsPhysicalDiskTable,
       "cpqOsPhysicalDiskEntry": cpqOsPhysicalDiskEntry,
       "cpqOsPhysicalDiskIndex": cpqOsPhysicalDiskIndex,
       "cpqOsPhysicalDiskInstance": cpqOsPhysicalDiskInstance,
       "cpqOsPhysicalDiskQueueLength": cpqOsPhysicalDiskQueueLength,
       "cpqOsPhysicalDiskBusyTimePercent": cpqOsPhysicalDiskBusyTimePercent,
       "cpqOsPhysicalDiskCondition": cpqOsPhysicalDiskCondition,
       "cpqOsPhysicalDiskBytesPersec": cpqOsPhysicalDiskBytesPersec,
       "cpqOsPhysicalDiskTransfersPersecx1000": cpqOsPhysicalDiskTransfersPersecx1000,
       "cpqOsPhysicalDiskReadsPersecx1000": cpqOsPhysicalDiskReadsPersecx1000,
       "cpqOsPhysicalDiskWritesPersecx1000": cpqOsPhysicalDiskWritesPersecx1000,
       "cpqOsPhysicalDiskReadBytesPersec": cpqOsPhysicalDiskReadBytesPersec,
       "cpqOsPhysicalDiskWriteBytesPersec": cpqOsPhysicalDiskWriteBytesPersec,
       "cpqOsPhysicalDiskAvgDisksecPerReadx10000": cpqOsPhysicalDiskAvgDisksecPerReadx10000,
       "cpqOsPhysicalDiskAvgDisksecPerWritex10000": cpqOsPhysicalDiskAvgDisksecPerWritex10000,
       "cpqOsPhysicalDiskCurrentDiskQueueLength": cpqOsPhysicalDiskCurrentDiskQueueLength,
       "cpqOsLogicalDisk": cpqOsLogicalDisk,
       "cpqOsLogicalDiskStatus": cpqOsLogicalDiskStatus,
       "cpqOsLogicalDiskTable": cpqOsLogicalDiskTable,
       "cpqOsLogicalDiskEntry": cpqOsLogicalDiskEntry,
       "cpqOsLogicalDiskIndex": cpqOsLogicalDiskIndex,
       "cpqOsLogicalDiskInstance": cpqOsLogicalDiskInstance,
       "cpqOsLogicalDiskFreeSpaceMBytes": cpqOsLogicalDiskFreeSpaceMBytes,
       "cpqOsLogicalDiskFreeSpacePercent": cpqOsLogicalDiskFreeSpacePercent,
       "cpqOsLogicalDiskQueueLength": cpqOsLogicalDiskQueueLength,
       "cpqOsLogicalDiskBusyTimePercent": cpqOsLogicalDiskBusyTimePercent,
       "cpqOsWarLogicalDiskBusyTimePercent": cpqOsWarLogicalDiskBusyTimePercent,
       "cpqOsCriLogicalDiskBusyTimePercent": cpqOsCriLogicalDiskBusyTimePercent,
       "cpqOsLogicalDiskCondition": cpqOsLogicalDiskCondition,
       "cpqOsServer": cpqOsServer,
       "cpqOsServerStatus": cpqOsServerStatus,
       "cpqOsServerTotalNetworkUtilizationBytesPerSec": cpqOsServerTotalNetworkUtilizationBytesPerSec,
       "cpqOsServerSessions": cpqOsServerSessions,
       "cpqOsServerAccessPermissionErrors": cpqOsServerAccessPermissionErrors,
       "cpqOsServerAccessGrantedErrors": cpqOsServerAccessGrantedErrors,
       "cpqOsServerLogonErrors": cpqOsServerLogonErrors,
       "cpqOsServerSessionsErroredOut": cpqOsServerSessionsErroredOut,
       "cpqOsServerContextBlocksQueuePerSec": cpqOsServerContextBlocksQueuePerSec,
       "cpqOsNetworkInterface": cpqOsNetworkInterface,
       "cpqOsNetworkInterfaceStatus": cpqOsNetworkInterfaceStatus,
       "cpqOsNetworkInterfaceTable": cpqOsNetworkInterfaceTable,
       "cpqOsNetworkInterfaceEntry": cpqOsNetworkInterfaceEntry,
       "cpqOsNetworkInterfaceIndex": cpqOsNetworkInterfaceIndex,
       "cpqOsNetworkInterfaceInstance": cpqOsNetworkInterfaceInstance,
       "cpqOsNetworkTotalBytesPerSec": cpqOsNetworkTotalBytesPerSec,
       "cpqOsNetworkPacketsPerSec": cpqOsNetworkPacketsPerSec,
       "cpqOsNetworkOutputQueueLength": cpqOsNetworkOutputQueueLength,
       "cpqOsNetworkPktOutboundErrors": cpqOsNetworkPktOutboundErrors,
       "cpqOsNetworkPktReceiveErrors": cpqOsNetworkPktReceiveErrors,
       "cpqOsNetworkCurrentBandWidth": cpqOsNetworkCurrentBandWidth,
       "cpqOsNetworkInterfaceCondition": cpqOsNetworkInterfaceCondition,
       "cpqOsNetworkBytesSentPersec": cpqOsNetworkBytesSentPersec,
       "cpqOsNetworkBytesReceivedPersec": cpqOsNetworkBytesReceivedPersec,
       "cpqOsNetworkPacketsSentPersecx1000": cpqOsNetworkPacketsSentPersecx1000,
       "cpqOsNetworkPacketsReceivedPersecx1000": cpqOsNetworkPacketsReceivedPersecx1000,
       "cpqOsTcp": cpqOsTcp,
       "cpqOsTcpStatus": cpqOsTcpStatus,
       "cpqOsTcpTable": cpqOsTcpTable,
       "cpqOsTcpEntry": cpqOsTcpEntry,
       "cpqOsTcpIndex": cpqOsTcpIndex,
       "cpqOsTcpInstance": cpqOsTcpInstance,
       "cpqOsTcpActiveConnections": cpqOsTcpActiveConnections,
       "cpqOsTcpEstablishedConections": cpqOsTcpEstablishedConections,
       "cpqOsTcpSegmentsPerSec": cpqOsTcpSegmentsPerSec,
       "cpqOsTcpRetransmittedSegmentsPerSec": cpqOsTcpRetransmittedSegmentsPerSec,
       "cpqOsTcpConnectionFailures": cpqOsTcpConnectionFailures,
       "cpqOsTcpCondition": cpqOsTcpCondition,
       "cpqOsProcess": cpqOsProcess,
       "cpqOsProcessStatus": cpqOsProcessStatus,
       "cpqOsProcessTable": cpqOsProcessTable,
       "cpqOsProcessEntry": cpqOsProcessEntry,
       "cpqOsProcessIndex": cpqOsProcessIndex,
       "cpqOsProcessInstance": cpqOsProcessInstance,
       "cpqOsProcessThreadCount": cpqOsProcessThreadCount,
       "cpqOsProcessPrivateBytes": cpqOsProcessPrivateBytes,
       "cpqOsProcessPageFileBytes": cpqOsProcessPageFileBytes,
       "cpqOsProcessWorkingSet": cpqOsProcessWorkingSet,
       "cpqOsProcessCpuTimePercent": cpqOsProcessCpuTimePercent,
       "cpqOsProcessPrivilegedTimePercent": cpqOsProcessPrivilegedTimePercent,
       "cpqOsProcessPageFaultsPerSec": cpqOsProcessPageFaultsPerSec,
       "cpqOsProcessCondition": cpqOsProcessCondition}
)
