# SNMP MIB module (RM3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RM3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:03 2024
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
 ObjectName,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rm3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_SoftSwitch_ObjectIdentity = ObjectIdentity
softSwitch = _SoftSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)
_ResourceMonitor_ObjectIdentity = ObjectIdentity
resourceMonitor = _ResourceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4)
)
_RmSystem_ObjectIdentity = ObjectIdentity
rmSystem = _RmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 1)
)
_RmDescr_Type = DisplayString
_RmDescr_Object = MibScalar
rmDescr = _RmDescr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 1, 1),
    _RmDescr_Type()
)
rmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDescr.setStatus("current")
_RmObjectID_Type = ObjectIdentifier
_RmObjectID_Object = MibScalar
rmObjectID = _RmObjectID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 1, 2),
    _RmObjectID_Type()
)
rmObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmObjectID.setStatus("current")
_RmUpTime_Type = TimeTicks
_RmUpTime_Object = MibScalar
rmUpTime = _RmUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 1, 3),
    _RmUpTime_Type()
)
rmUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmUpTime.setStatus("current")
_RmNetAddress_Type = IpAddress
_RmNetAddress_Object = MibScalar
rmNetAddress = _RmNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 1, 4),
    _RmNetAddress_Type()
)
rmNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmNetAddress.setStatus("current")
_RmControl_Type = DisplayString
_RmControl_Object = MibScalar
rmControl = _RmControl_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 1, 5),
    _RmControl_Type()
)
rmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmControl.setStatus("current")
_RmDiskGrp_ObjectIdentity = ObjectIdentity
rmDiskGrp = _RmDiskGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2)
)


class _DiskPeriod_Type(Integer32):
    """Custom type diskPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DiskPeriod_Type.__name__ = "Integer32"
_DiskPeriod_Object = MibScalar
diskPeriod = _DiskPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 1),
    _DiskPeriod_Type()
)
diskPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskPeriod.setStatus("current")


class _DiskUsageWarningPct_Type(Integer32):
    """Custom type diskUsageWarningPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_DiskUsageWarningPct_Type.__name__ = "Integer32"
_DiskUsageWarningPct_Object = MibScalar
diskUsageWarningPct = _DiskUsageWarningPct_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 2),
    _DiskUsageWarningPct_Type()
)
diskUsageWarningPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskUsageWarningPct.setStatus("current")


class _DiskUsageAlarmPct_Type(Integer32):
    """Custom type diskUsageAlarmPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_DiskUsageAlarmPct_Type.__name__ = "Integer32"
_DiskUsageAlarmPct_Object = MibScalar
diskUsageAlarmPct = _DiskUsageAlarmPct_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 3),
    _DiskUsageAlarmPct_Type()
)
diskUsageAlarmPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskUsageAlarmPct.setStatus("current")


class _DuNumber_Type(Integer32):
    """Custom type duNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_DuNumber_Type.__name__ = "Integer32"
_DuNumber_Object = MibScalar
duNumber = _DuNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 4),
    _DuNumber_Type()
)
duNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duNumber.setStatus("current")
_DiskUsageTable_Object = MibTable
diskUsageTable = _DiskUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 5)
)
if mibBuilder.loadTexts:
    diskUsageTable.setStatus("current")
_DiskUsageEntry_Object = MibTableRow
diskUsageEntry = _DiskUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 5, 1)
)
diskUsageEntry.setIndexNames(
    (0, "RM3-MIB", "duIndex"),
)
if mibBuilder.loadTexts:
    diskUsageEntry.setStatus("current")


class _DuIndex_Type(Integer32):
    """Custom type duIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_DuIndex_Type.__name__ = "Integer32"
_DuIndex_Object = MibTableColumn
duIndex = _DuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 5, 1, 1),
    _DuIndex_Type()
)
duIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duIndex.setStatus("current")
_DuFSName_Type = DisplayString
_DuFSName_Object = MibTableColumn
duFSName = _DuFSName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 5, 1, 2),
    _DuFSName_Type()
)
duFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duFSName.setStatus("current")


class _DuSize_Type(Integer32):
    """Custom type duSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_DuSize_Type.__name__ = "Integer32"
_DuSize_Object = MibTableColumn
duSize = _DuSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 5, 1, 3),
    _DuSize_Type()
)
duSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duSize.setStatus("current")


class _DuPctUsed_Type(Integer32):
    """Custom type duPctUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DuPctUsed_Type.__name__ = "Integer32"
_DuPctUsed_Object = MibTableColumn
duPctUsed = _DuPctUsed_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 2, 5, 1, 4),
    _DuPctUsed_Type()
)
duPctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duPctUsed.setStatus("current")
_RmCpuGrp_ObjectIdentity = ObjectIdentity
rmCpuGrp = _RmCpuGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3)
)


class _CpuPeriod_Type(Integer32):
    """Custom type cpuPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CpuPeriod_Type.__name__ = "Integer32"
_CpuPeriod_Object = MibScalar
cpuPeriod = _CpuPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3, 1),
    _CpuPeriod_Type()
)
cpuPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuPeriod.setStatus("current")


class _CpuUtilization_Type(Integer32):
    """Custom type cpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CpuUtilization_Type.__name__ = "Integer32"
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3, 2),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("current")


class _CpuUtilWarningPct_Type(Integer32):
    """Custom type cpuUtilWarningPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CpuUtilWarningPct_Type.__name__ = "Integer32"
_CpuUtilWarningPct_Object = MibScalar
cpuUtilWarningPct = _CpuUtilWarningPct_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3, 3),
    _CpuUtilWarningPct_Type()
)
cpuUtilWarningPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuUtilWarningPct.setStatus("current")


class _CpuUtilAlarmPct_Type(Integer32):
    """Custom type cpuUtilAlarmPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CpuUtilAlarmPct_Type.__name__ = "Integer32"
_CpuUtilAlarmPct_Object = MibScalar
cpuUtilAlarmPct = _CpuUtilAlarmPct_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3, 4),
    _CpuUtilAlarmPct_Type()
)
cpuUtilAlarmPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuUtilAlarmPct.setStatus("current")
_CpuLoad_Type = DisplayString
_CpuLoad_Object = MibScalar
cpuLoad = _CpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3, 5),
    _CpuLoad_Type()
)
cpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad.setStatus("current")
_CpuLoadWarningThreshold_Type = DisplayString
_CpuLoadWarningThreshold_Object = MibScalar
cpuLoadWarningThreshold = _CpuLoadWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3, 6),
    _CpuLoadWarningThreshold_Type()
)
cpuLoadWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuLoadWarningThreshold.setStatus("current")
_CpuLoadAlarmThreshold_Type = DisplayString
_CpuLoadAlarmThreshold_Object = MibScalar
cpuLoadAlarmThreshold = _CpuLoadAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 3, 7),
    _CpuLoadAlarmThreshold_Type()
)
cpuLoadAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuLoadAlarmThreshold.setStatus("current")
_RmFileGrp_ObjectIdentity = ObjectIdentity
rmFileGrp = _RmFileGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4)
)


class _FilePeriod_Type(Integer32):
    """Custom type filePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FilePeriod_Type.__name__ = "Integer32"
_FilePeriod_Object = MibScalar
filePeriod = _FilePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 1),
    _FilePeriod_Type()
)
filePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filePeriod.setStatus("current")


class _FmNumber_Type(Integer32):
    """Custom type fmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_FmNumber_Type.__name__ = "Integer32"
_FmNumber_Object = MibScalar
fmNumber = _FmNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 2),
    _FmNumber_Type()
)
fmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmNumber.setStatus("current")
_FmTable_Object = MibTable
fmTable = _FmTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 3)
)
if mibBuilder.loadTexts:
    fmTable.setStatus("current")
_FmEntry_Object = MibTableRow
fmEntry = _FmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 3, 1)
)
fmEntry.setIndexNames(
    (0, "RM3-MIB", "fmIndex"),
)
if mibBuilder.loadTexts:
    fmEntry.setStatus("current")


class _FmIndex_Type(Integer32):
    """Custom type fmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_FmIndex_Type.__name__ = "Integer32"
_FmIndex_Object = MibTableColumn
fmIndex = _FmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 3, 1, 1),
    _FmIndex_Type()
)
fmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmIndex.setStatus("current")


class _FmName_Type(DisplayString):
    """Custom type fmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmName_Type.__name__ = "DisplayString"
_FmName_Object = MibTableColumn
fmName = _FmName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 3, 1, 2),
    _FmName_Type()
)
fmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmName.setStatus("current")


class _FmCurSize_Type(Integer32):
    """Custom type fmCurSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_FmCurSize_Type.__name__ = "Integer32"
_FmCurSize_Object = MibTableColumn
fmCurSize = _FmCurSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 3, 1, 3),
    _FmCurSize_Type()
)
fmCurSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmCurSize.setStatus("current")


class _FmThreshold_Type(Integer32):
    """Custom type fmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_FmThreshold_Type.__name__ = "Integer32"
_FmThreshold_Object = MibTableColumn
fmThreshold = _FmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 3, 1, 4),
    _FmThreshold_Type()
)
fmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmThreshold.setStatus("current")
_ArchiveDir_Type = DisplayString
_ArchiveDir_Object = MibScalar
archiveDir = _ArchiveDir_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 4, 4),
    _ArchiveDir_Type()
)
archiveDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    archiveDir.setStatus("current")
_RmProcessGrp_ObjectIdentity = ObjectIdentity
rmProcessGrp = _RmProcessGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5)
)


class _ProcessPeriod_Type(Integer32):
    """Custom type processPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ProcessPeriod_Type.__name__ = "Integer32"
_ProcessPeriod_Object = MibScalar
processPeriod = _ProcessPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 1),
    _ProcessPeriod_Type()
)
processPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processPeriod.setStatus("current")


class _ProcessNumber_Type(Integer32):
    """Custom type processNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_ProcessNumber_Type.__name__ = "Integer32"
_ProcessNumber_Object = MibScalar
processNumber = _ProcessNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 2),
    _ProcessNumber_Type()
)
processNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processNumber.setStatus("current")
_ProcessTable_Object = MibTable
processTable = _ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3)
)
if mibBuilder.loadTexts:
    processTable.setStatus("current")
_ProcessEntry_Object = MibTableRow
processEntry = _ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1)
)
processEntry.setIndexNames(
    (0, "RM3-MIB", "processIndex"),
)
if mibBuilder.loadTexts:
    processEntry.setStatus("current")


class _ProcessIndex_Type(Integer32):
    """Custom type processIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_ProcessIndex_Type.__name__ = "Integer32"
_ProcessIndex_Object = MibTableColumn
processIndex = _ProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 1),
    _ProcessIndex_Type()
)
processIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processIndex.setStatus("current")


class _ProcessID_Type(Integer32):
    """Custom type processID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProcessID_Type.__name__ = "Integer32"
_ProcessID_Object = MibTableColumn
processID = _ProcessID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 2),
    _ProcessID_Type()
)
processID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processID.setStatus("current")
_ProcessName_Type = DisplayString
_ProcessName_Object = MibTableColumn
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 3),
    _ProcessName_Type()
)
processName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processName.setStatus("current")


class _ProcessUpTime_Type(Integer32):
    """Custom type processUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProcessUpTime_Type.__name__ = "Integer32"
_ProcessUpTime_Object = MibTableColumn
processUpTime = _ProcessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 4),
    _ProcessUpTime_Type()
)
processUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processUpTime.setStatus("current")


class _ProcessCPUUsageWarnMark_Type(Integer32):
    """Custom type processCPUUsageWarnMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ProcessCPUUsageWarnMark_Type.__name__ = "Integer32"
_ProcessCPUUsageWarnMark_Object = MibTableColumn
processCPUUsageWarnMark = _ProcessCPUUsageWarnMark_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 5),
    _ProcessCPUUsageWarnMark_Type()
)
processCPUUsageWarnMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCPUUsageWarnMark.setStatus("current")


class _ProcessCPUUsageAlarmMark_Type(Integer32):
    """Custom type processCPUUsageAlarmMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ProcessCPUUsageAlarmMark_Type.__name__ = "Integer32"
_ProcessCPUUsageAlarmMark_Object = MibTableColumn
processCPUUsageAlarmMark = _ProcessCPUUsageAlarmMark_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 6),
    _ProcessCPUUsageAlarmMark_Type()
)
processCPUUsageAlarmMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCPUUsageAlarmMark.setStatus("current")


class _ProcessCPUUsageCurrent_Type(Integer32):
    """Custom type processCPUUsageCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ProcessCPUUsageCurrent_Type.__name__ = "Integer32"
_ProcessCPUUsageCurrent_Object = MibTableColumn
processCPUUsageCurrent = _ProcessCPUUsageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 7),
    _ProcessCPUUsageCurrent_Type()
)
processCPUUsageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCPUUsageCurrent.setStatus("current")


class _ProcessMemUsageAlarmMark_Type(Integer32):
    """Custom type processMemUsageAlarmMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ProcessMemUsageAlarmMark_Type.__name__ = "Integer32"
_ProcessMemUsageAlarmMark_Object = MibTableColumn
processMemUsageAlarmMark = _ProcessMemUsageAlarmMark_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 8),
    _ProcessMemUsageAlarmMark_Type()
)
processMemUsageAlarmMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMemUsageAlarmMark.setStatus("current")


class _ProcessMemUsageCurrent_Type(Integer32):
    """Custom type processMemUsageCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_ProcessMemUsageCurrent_Type.__name__ = "Integer32"
_ProcessMemUsageCurrent_Object = MibTableColumn
processMemUsageCurrent = _ProcessMemUsageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 3, 5, 3, 1, 9),
    _ProcessMemUsageCurrent_Type()
)
processMemUsageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMemUsageCurrent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RM3-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "resourceMonitor": resourceMonitor,
       "rm3": rm3,
       "rmSystem": rmSystem,
       "rmDescr": rmDescr,
       "rmObjectID": rmObjectID,
       "rmUpTime": rmUpTime,
       "rmNetAddress": rmNetAddress,
       "rmControl": rmControl,
       "rmDiskGrp": rmDiskGrp,
       "diskPeriod": diskPeriod,
       "diskUsageWarningPct": diskUsageWarningPct,
       "diskUsageAlarmPct": diskUsageAlarmPct,
       "duNumber": duNumber,
       "diskUsageTable": diskUsageTable,
       "diskUsageEntry": diskUsageEntry,
       "duIndex": duIndex,
       "duFSName": duFSName,
       "duSize": duSize,
       "duPctUsed": duPctUsed,
       "rmCpuGrp": rmCpuGrp,
       "cpuPeriod": cpuPeriod,
       "cpuUtilization": cpuUtilization,
       "cpuUtilWarningPct": cpuUtilWarningPct,
       "cpuUtilAlarmPct": cpuUtilAlarmPct,
       "cpuLoad": cpuLoad,
       "cpuLoadWarningThreshold": cpuLoadWarningThreshold,
       "cpuLoadAlarmThreshold": cpuLoadAlarmThreshold,
       "rmFileGrp": rmFileGrp,
       "filePeriod": filePeriod,
       "fmNumber": fmNumber,
       "fmTable": fmTable,
       "fmEntry": fmEntry,
       "fmIndex": fmIndex,
       "fmName": fmName,
       "fmCurSize": fmCurSize,
       "fmThreshold": fmThreshold,
       "archiveDir": archiveDir,
       "rmProcessGrp": rmProcessGrp,
       "processPeriod": processPeriod,
       "processNumber": processNumber,
       "processTable": processTable,
       "processEntry": processEntry,
       "processIndex": processIndex,
       "processID": processID,
       "processName": processName,
       "processUpTime": processUpTime,
       "processCPUUsageWarnMark": processCPUUsageWarnMark,
       "processCPUUsageAlarmMark": processCPUUsageAlarmMark,
       "processCPUUsageCurrent": processCPUUsageCurrent,
       "processMemUsageAlarmMark": processMemUsageAlarmMark,
       "processMemUsageCurrent": processMemUsageCurrent}
)
