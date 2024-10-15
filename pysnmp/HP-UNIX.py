# SNMP MIB module (HP-UNIX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-UNIX
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:09 2024
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
 enterprises,
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
    "enterprises",
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1)
)
_ComputerSystem_ObjectIdentity = ObjectIdentity
computerSystem = _ComputerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1)
)
_ComputerSystemUpTime_Type = TimeTicks
_ComputerSystemUpTime_Object = MibScalar
computerSystemUpTime = _ComputerSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 1),
    _ComputerSystemUpTime_Type()
)
computerSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemUpTime.setStatus("mandatory")
_ComputerSystemUsers_Type = Gauge32
_ComputerSystemUsers_Object = MibScalar
computerSystemUsers = _ComputerSystemUsers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 2),
    _ComputerSystemUsers_Type()
)
computerSystemUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemUsers.setStatus("mandatory")
_ComputerSystemAvgJobs1_Type = Gauge32
_ComputerSystemAvgJobs1_Object = MibScalar
computerSystemAvgJobs1 = _ComputerSystemAvgJobs1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 3),
    _ComputerSystemAvgJobs1_Type()
)
computerSystemAvgJobs1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemAvgJobs1.setStatus("mandatory")
_ComputerSystemAvgJobs5_Type = Gauge32
_ComputerSystemAvgJobs5_Object = MibScalar
computerSystemAvgJobs5 = _ComputerSystemAvgJobs5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 4),
    _ComputerSystemAvgJobs5_Type()
)
computerSystemAvgJobs5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemAvgJobs5.setStatus("mandatory")
_ComputerSystemAvgJobs15_Type = Gauge32
_ComputerSystemAvgJobs15_Object = MibScalar
computerSystemAvgJobs15 = _ComputerSystemAvgJobs15_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 5),
    _ComputerSystemAvgJobs15_Type()
)
computerSystemAvgJobs15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemAvgJobs15.setStatus("mandatory")
_ComputerSystemMaxProc_Type = Integer32
_ComputerSystemMaxProc_Object = MibScalar
computerSystemMaxProc = _ComputerSystemMaxProc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 6),
    _ComputerSystemMaxProc_Type()
)
computerSystemMaxProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemMaxProc.setStatus("mandatory")
_ComputerSystemFreeMemory_Type = Gauge32
_ComputerSystemFreeMemory_Object = MibScalar
computerSystemFreeMemory = _ComputerSystemFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 7),
    _ComputerSystemFreeMemory_Type()
)
computerSystemFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemFreeMemory.setStatus("mandatory")
_ComputerSystemPhysMemory_Type = Integer32
_ComputerSystemPhysMemory_Object = MibScalar
computerSystemPhysMemory = _ComputerSystemPhysMemory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 8),
    _ComputerSystemPhysMemory_Type()
)
computerSystemPhysMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemPhysMemory.setStatus("mandatory")
_ComputerSystemMaxUserMem_Type = Gauge32
_ComputerSystemMaxUserMem_Object = MibScalar
computerSystemMaxUserMem = _ComputerSystemMaxUserMem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 9),
    _ComputerSystemMaxUserMem_Type()
)
computerSystemMaxUserMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemMaxUserMem.setStatus("mandatory")
_ComputerSystemSwapConfig_Type = Integer32
_ComputerSystemSwapConfig_Object = MibScalar
computerSystemSwapConfig = _ComputerSystemSwapConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 10),
    _ComputerSystemSwapConfig_Type()
)
computerSystemSwapConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemSwapConfig.setStatus("mandatory")
_ComputerSystemEnabledSwap_Type = Gauge32
_ComputerSystemEnabledSwap_Object = MibScalar
computerSystemEnabledSwap = _ComputerSystemEnabledSwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 11),
    _ComputerSystemEnabledSwap_Type()
)
computerSystemEnabledSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemEnabledSwap.setStatus("mandatory")
_ComputerSystemFreeSwap_Type = Gauge32
_ComputerSystemFreeSwap_Object = MibScalar
computerSystemFreeSwap = _ComputerSystemFreeSwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 12),
    _ComputerSystemFreeSwap_Type()
)
computerSystemFreeSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemFreeSwap.setStatus("mandatory")
_ComputerSystemUserCPU_Type = Counter32
_ComputerSystemUserCPU_Object = MibScalar
computerSystemUserCPU = _ComputerSystemUserCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 13),
    _ComputerSystemUserCPU_Type()
)
computerSystemUserCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemUserCPU.setStatus("mandatory")
_ComputerSystemSysCPU_Type = Counter32
_ComputerSystemSysCPU_Object = MibScalar
computerSystemSysCPU = _ComputerSystemSysCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 14),
    _ComputerSystemSysCPU_Type()
)
computerSystemSysCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemSysCPU.setStatus("mandatory")
_ComputerSystemIdleCPU_Type = Counter32
_ComputerSystemIdleCPU_Object = MibScalar
computerSystemIdleCPU = _ComputerSystemIdleCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 15),
    _ComputerSystemIdleCPU_Type()
)
computerSystemIdleCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemIdleCPU.setStatus("mandatory")
_ComputerSystemNiceCPU_Type = Counter32
_ComputerSystemNiceCPU_Object = MibScalar
computerSystemNiceCPU = _ComputerSystemNiceCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 1, 16),
    _ComputerSystemNiceCPU_Type()
)
computerSystemNiceCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computerSystemNiceCPU.setStatus("mandatory")
_FileSystem_ObjectIdentity = ObjectIdentity
fileSystem = _FileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2)
)
_FileSystemMounted_Type = Gauge32
_FileSystemMounted_Object = MibScalar
fileSystemMounted = _FileSystemMounted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 1),
    _FileSystemMounted_Type()
)
fileSystemMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemMounted.setStatus("mandatory")
_FileSystemTable_Object = MibTable
fileSystemTable = _FileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fileSystemTable.setStatus("mandatory")
_FileSystemEntry_Object = MibTableRow
fileSystemEntry = _FileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1)
)
fileSystemEntry.setIndexNames(
    (0, "HP-UNIX", "fileSystemID1"),
    (0, "HP-UNIX", "fileSystemID2"),
)
if mibBuilder.loadTexts:
    fileSystemEntry.setStatus("mandatory")


class _FileSystemID1_Type(Integer32):
    """Custom type fileSystemID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FileSystemID1_Type.__name__ = "Integer32"
_FileSystemID1_Object = MibTableColumn
fileSystemID1 = _FileSystemID1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 1),
    _FileSystemID1_Type()
)
fileSystemID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemID1.setStatus("mandatory")


class _FileSystemID2_Type(Integer32):
    """Custom type fileSystemID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FileSystemID2_Type.__name__ = "Integer32"
_FileSystemID2_Object = MibTableColumn
fileSystemID2 = _FileSystemID2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 2),
    _FileSystemID2_Type()
)
fileSystemID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemID2.setStatus("mandatory")
_FileSystemName_Type = DisplayString
_FileSystemName_Object = MibTableColumn
fileSystemName = _FileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 3),
    _FileSystemName_Type()
)
fileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemName.setStatus("mandatory")
_FileSystemBlock_Type = Integer32
_FileSystemBlock_Object = MibTableColumn
fileSystemBlock = _FileSystemBlock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 4),
    _FileSystemBlock_Type()
)
fileSystemBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemBlock.setStatus("mandatory")
_FileSystemBfree_Type = Integer32
_FileSystemBfree_Object = MibTableColumn
fileSystemBfree = _FileSystemBfree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 5),
    _FileSystemBfree_Type()
)
fileSystemBfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemBfree.setStatus("mandatory")
_FileSystemBavail_Type = Integer32
_FileSystemBavail_Object = MibTableColumn
fileSystemBavail = _FileSystemBavail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 6),
    _FileSystemBavail_Type()
)
fileSystemBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemBavail.setStatus("mandatory")
_FileSystemBsize_Type = Integer32
_FileSystemBsize_Object = MibTableColumn
fileSystemBsize = _FileSystemBsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 7),
    _FileSystemBsize_Type()
)
fileSystemBsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemBsize.setStatus("mandatory")
_FileSystemFiles_Type = Integer32
_FileSystemFiles_Object = MibTableColumn
fileSystemFiles = _FileSystemFiles_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 8),
    _FileSystemFiles_Type()
)
fileSystemFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemFiles.setStatus("mandatory")
_FileSystemFfree_Type = Integer32
_FileSystemFfree_Object = MibTableColumn
fileSystemFfree = _FileSystemFfree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 9),
    _FileSystemFfree_Type()
)
fileSystemFfree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemFfree.setStatus("mandatory")
_FileSystemDir_Type = DisplayString
_FileSystemDir_Object = MibTableColumn
fileSystemDir = _FileSystemDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 2, 2, 1, 10),
    _FileSystemDir_Type()
)
fileSystemDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemDir.setStatus("mandatory")
_Processes_ObjectIdentity = ObjectIdentity
processes = _Processes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4)
)
_ProcessNum_Type = Gauge32
_ProcessNum_Object = MibScalar
processNum = _ProcessNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 1),
    _ProcessNum_Type()
)
processNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processNum.setStatus("mandatory")
_ProcessTable_Object = MibTable
processTable = _ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    processTable.setStatus("mandatory")
_ProcessEntry_Object = MibTableRow
processEntry = _ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1)
)
processEntry.setIndexNames(
    (0, "HP-UNIX", "processPID"),
)
if mibBuilder.loadTexts:
    processEntry.setStatus("mandatory")
_ProcessPID_Type = Integer32
_ProcessPID_Object = MibTableColumn
processPID = _ProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 1),
    _ProcessPID_Type()
)
processPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPID.setStatus("mandatory")
_ProcessIdx_Type = Integer32
_ProcessIdx_Object = MibTableColumn
processIdx = _ProcessIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 2),
    _ProcessIdx_Type()
)
processIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processIdx.setStatus("mandatory")
_ProcessUID_Type = Integer32
_ProcessUID_Object = MibTableColumn
processUID = _ProcessUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 3),
    _ProcessUID_Type()
)
processUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processUID.setStatus("mandatory")
_ProcessPPID_Type = Integer32
_ProcessPPID_Object = MibTableColumn
processPPID = _ProcessPPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 4),
    _ProcessPPID_Type()
)
processPPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPPID.setStatus("mandatory")
_ProcessDsize_Type = Gauge32
_ProcessDsize_Object = MibTableColumn
processDsize = _ProcessDsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 5),
    _ProcessDsize_Type()
)
processDsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processDsize.setStatus("mandatory")
_ProcessTsize_Type = Gauge32
_ProcessTsize_Object = MibTableColumn
processTsize = _ProcessTsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 6),
    _ProcessTsize_Type()
)
processTsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processTsize.setStatus("mandatory")
_ProcessSsize_Type = Gauge32
_ProcessSsize_Object = MibTableColumn
processSsize = _ProcessSsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 7),
    _ProcessSsize_Type()
)
processSsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processSsize.setStatus("mandatory")
_ProcessNice_Type = Gauge32
_ProcessNice_Object = MibTableColumn
processNice = _ProcessNice_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 8),
    _ProcessNice_Type()
)
processNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processNice.setStatus("mandatory")
_ProcessMajor_Type = Integer32
_ProcessMajor_Object = MibTableColumn
processMajor = _ProcessMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 9),
    _ProcessMajor_Type()
)
processMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMajor.setStatus("mandatory")
_ProcessMinor_Type = Integer32
_ProcessMinor_Object = MibTableColumn
processMinor = _ProcessMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 10),
    _ProcessMinor_Type()
)
processMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMinor.setStatus("mandatory")
_ProcessPgrp_Type = Integer32
_ProcessPgrp_Object = MibTableColumn
processPgrp = _ProcessPgrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 11),
    _ProcessPgrp_Type()
)
processPgrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPgrp.setStatus("mandatory")
_ProcessPrio_Type = Integer32
_ProcessPrio_Object = MibTableColumn
processPrio = _ProcessPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 12),
    _ProcessPrio_Type()
)
processPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPrio.setStatus("mandatory")
_ProcessAddr_Type = Integer32
_ProcessAddr_Object = MibTableColumn
processAddr = _ProcessAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 13),
    _ProcessAddr_Type()
)
processAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processAddr.setStatus("mandatory")
_ProcessCPU_Type = Gauge32
_ProcessCPU_Object = MibTableColumn
processCPU = _ProcessCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 14),
    _ProcessCPU_Type()
)
processCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCPU.setStatus("mandatory")
_ProcessUtime_Type = TimeTicks
_ProcessUtime_Object = MibTableColumn
processUtime = _ProcessUtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 15),
    _ProcessUtime_Type()
)
processUtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processUtime.setStatus("mandatory")
_ProcessStime_Type = TimeTicks
_ProcessStime_Object = MibTableColumn
processStime = _ProcessStime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 16),
    _ProcessStime_Type()
)
processStime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processStime.setStatus("mandatory")
_ProcessStart_Type = TimeTicks
_ProcessStart_Object = MibTableColumn
processStart = _ProcessStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 17),
    _ProcessStart_Type()
)
processStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processStart.setStatus("mandatory")


class _ProcessFlags_Type(Integer32):
    """Custom type processFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("incore", 1),
          ("locked", 4),
          ("sys", 2),
          ("trace", 8),
          ("trace2", 16))
    )


_ProcessFlags_Type.__name__ = "Integer32"
_ProcessFlags_Object = MibTableColumn
processFlags = _ProcessFlags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 18),
    _ProcessFlags_Type()
)
processFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processFlags.setStatus("mandatory")


class _ProcessStatus_Type(Integer32):
    """Custom type processStatus based on Integer32"""
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
        *(("idle", 6),
          ("other", 5),
          ("run", 2),
          ("sleep", 1),
          ("stop", 3),
          ("zombie", 4))
    )


_ProcessStatus_Type.__name__ = "Integer32"
_ProcessStatus_Object = MibTableColumn
processStatus = _ProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 19),
    _ProcessStatus_Type()
)
processStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processStatus.setStatus("mandatory")
_ProcessWchan_Type = Integer32
_ProcessWchan_Object = MibTableColumn
processWchan = _ProcessWchan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 20),
    _ProcessWchan_Type()
)
processWchan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processWchan.setStatus("mandatory")
_ProcessProcNum_Type = Integer32
_ProcessProcNum_Object = MibTableColumn
processProcNum = _ProcessProcNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 21),
    _ProcessProcNum_Type()
)
processProcNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processProcNum.setStatus("mandatory")
_ProcessCmd_Type = DisplayString
_ProcessCmd_Object = MibTableColumn
processCmd = _ProcessCmd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 22),
    _ProcessCmd_Type()
)
processCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCmd.setStatus("mandatory")
_ProcessTime_Type = Integer32
_ProcessTime_Object = MibTableColumn
processTime = _ProcessTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 23),
    _ProcessTime_Type()
)
processTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processTime.setStatus("mandatory")
_ProcessCPUticks_Type = Counter32
_ProcessCPUticks_Object = MibTableColumn
processCPUticks = _ProcessCPUticks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 24),
    _ProcessCPUticks_Type()
)
processCPUticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCPUticks.setStatus("mandatory")
_ProcessCPUticksTotal_Type = Counter32
_ProcessCPUticksTotal_Object = MibTableColumn
processCPUticksTotal = _ProcessCPUticksTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 25),
    _ProcessCPUticksTotal_Type()
)
processCPUticksTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCPUticksTotal.setStatus("mandatory")
_ProcessFss_Type = Integer32
_ProcessFss_Object = MibTableColumn
processFss = _ProcessFss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 26),
    _ProcessFss_Type()
)
processFss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processFss.setStatus("mandatory")
_ProcessPctCPU_Type = Gauge32
_ProcessPctCPU_Object = MibTableColumn
processPctCPU = _ProcessPctCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 27),
    _ProcessPctCPU_Type()
)
processPctCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processPctCPU.setStatus("mandatory")
_ProcessRssize_Type = Gauge32
_ProcessRssize_Object = MibTableColumn
processRssize = _ProcessRssize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 28),
    _ProcessRssize_Type()
)
processRssize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processRssize.setStatus("mandatory")
_ProcessSUID_Type = Integer32
_ProcessSUID_Object = MibTableColumn
processSUID = _ProcessSUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 29),
    _ProcessSUID_Type()
)
processSUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processSUID.setStatus("mandatory")
_ProcessUname_Type = DisplayString
_ProcessUname_Object = MibTableColumn
processUname = _ProcessUname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 30),
    _ProcessUname_Type()
)
processUname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processUname.setStatus("mandatory")
_ProcessTTY_Type = DisplayString
_ProcessTTY_Object = MibTableColumn
processTTY = _ProcessTTY_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 4, 2, 1, 31),
    _ProcessTTY_Type()
)
processTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processTTY.setStatus("mandatory")
_Cluster_ObjectIdentity = ObjectIdentity
cluster = _Cluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5)
)


class _IsClustered_Type(Integer32):
    """Custom type isClustered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cnode", 3),
          ("rootserver", 2),
          ("standalone", 1))
    )


_IsClustered_Type.__name__ = "Integer32"
_IsClustered_Object = MibScalar
isClustered = _IsClustered_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 1),
    _IsClustered_Type()
)
isClustered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isClustered.setStatus("mandatory")
_ClusterTable_Object = MibTable
clusterTable = _ClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    clusterTable.setStatus("mandatory")
_ClusterEntry_Object = MibTableRow
clusterEntry = _ClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1)
)
clusterEntry.setIndexNames(
    (0, "HP-UNIX", "clusterID"),
)
if mibBuilder.loadTexts:
    clusterEntry.setStatus("mandatory")
_ClusterID_Type = Integer32
_ClusterID_Object = MibTableColumn
clusterID = _ClusterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1, 1),
    _ClusterID_Type()
)
clusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterID.setStatus("mandatory")
_ClusterMachineID_Type = OctetString
_ClusterMachineID_Object = MibTableColumn
clusterMachineID = _ClusterMachineID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1, 2),
    _ClusterMachineID_Type()
)
clusterMachineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMachineID.setStatus("mandatory")
_ClusterType_Type = DisplayString
_ClusterType_Object = MibTableColumn
clusterType = _ClusterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1, 3),
    _ClusterType_Type()
)
clusterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterType.setStatus("mandatory")
_ClusterCnodeName_Type = DisplayString
_ClusterCnodeName_Object = MibTableColumn
clusterCnodeName = _ClusterCnodeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1, 4),
    _ClusterCnodeName_Type()
)
clusterCnodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCnodeName.setStatus("mandatory")
_ClusterSwapServingCnode_Type = Integer32
_ClusterSwapServingCnode_Object = MibTableColumn
clusterSwapServingCnode = _ClusterSwapServingCnode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1, 5),
    _ClusterSwapServingCnode_Type()
)
clusterSwapServingCnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterSwapServingCnode.setStatus("mandatory")
_ClusterKcsp_Type = Integer32
_ClusterKcsp_Object = MibTableColumn
clusterKcsp = _ClusterKcsp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1, 6),
    _ClusterKcsp_Type()
)
clusterKcsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterKcsp.setStatus("mandatory")
_ClusterCnodeAddress_Type = IpAddress
_ClusterCnodeAddress_Object = MibTableColumn
clusterCnodeAddress = _ClusterCnodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 2, 1, 7),
    _ClusterCnodeAddress_Type()
)
clusterCnodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCnodeAddress.setStatus("mandatory")
_ClusterCnodeID_Type = Integer32
_ClusterCnodeID_Object = MibScalar
clusterCnodeID = _ClusterCnodeID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 5, 3),
    _ClusterCnodeID_Type()
)
clusterCnodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCnodeID.setStatus("mandatory")
_Hpux_ObjectIdentity = ObjectIdentity
hpux = _Hpux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 2)
)
_Hp9000s300_ObjectIdentity = ObjectIdentity
hp9000s300 = _Hp9000s300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 2, 2)
)
_Hp9000s800_ObjectIdentity = ObjectIdentity
hp9000s800 = _Hp9000s800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 2, 3)
)
_Hp9000s700_ObjectIdentity = ObjectIdentity
hp9000s700 = _Hp9000s700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 2, 5)
)
_Hp386_ObjectIdentity = ObjectIdentity
hp386 = _Hp386_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 8)
)
_Hpsun_ObjectIdentity = ObjectIdentity
hpsun = _Hpsun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 10)
)
_Sparc_ObjectIdentity = ObjectIdentity
sparc = _Sparc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 10, 1)
)
_Sun4_ObjectIdentity = ObjectIdentity
sun4 = _Sun4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 10, 1, 1)
)
_Sun5_ObjectIdentity = ObjectIdentity
sun5 = _Sun5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 10, 1, 2)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4)
)
_Ieee8023Mac_ObjectIdentity = ObjectIdentity
ieee8023Mac = _Ieee8023Mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1)
)
_Ieee8023MacTable_Object = MibTable
ieee8023MacTable = _Ieee8023MacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8023MacTable.setStatus("mandatory")
_Ieee8023MacEntry_Object = MibTableRow
ieee8023MacEntry = _Ieee8023MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1)
)
ieee8023MacEntry.setIndexNames(
    (0, "HP-UNIX", "ieee8023MacIndex"),
)
if mibBuilder.loadTexts:
    ieee8023MacEntry.setStatus("mandatory")
_Ieee8023MacIndex_Type = Integer32
_Ieee8023MacIndex_Object = MibTableColumn
ieee8023MacIndex = _Ieee8023MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 1),
    _Ieee8023MacIndex_Type()
)
ieee8023MacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacIndex.setStatus("mandatory")
_Ieee8023MacTransmitted_Type = Counter32
_Ieee8023MacTransmitted_Object = MibTableColumn
ieee8023MacTransmitted = _Ieee8023MacTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 2),
    _Ieee8023MacTransmitted_Type()
)
ieee8023MacTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacTransmitted.setStatus("mandatory")
_Ieee8023MacNotTransmitted_Type = Counter32
_Ieee8023MacNotTransmitted_Object = MibTableColumn
ieee8023MacNotTransmitted = _Ieee8023MacNotTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 3),
    _Ieee8023MacNotTransmitted_Type()
)
ieee8023MacNotTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacNotTransmitted.setStatus("mandatory")
_Ieee8023MacDeferred_Type = Counter32
_Ieee8023MacDeferred_Object = MibTableColumn
ieee8023MacDeferred = _Ieee8023MacDeferred_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 4),
    _Ieee8023MacDeferred_Type()
)
ieee8023MacDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacDeferred.setStatus("mandatory")
_Ieee8023MacCollisions_Type = Counter32
_Ieee8023MacCollisions_Object = MibTableColumn
ieee8023MacCollisions = _Ieee8023MacCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 5),
    _Ieee8023MacCollisions_Type()
)
ieee8023MacCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacCollisions.setStatus("mandatory")
_Ieee8023MacSingleCollisions_Type = Counter32
_Ieee8023MacSingleCollisions_Object = MibTableColumn
ieee8023MacSingleCollisions = _Ieee8023MacSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 6),
    _Ieee8023MacSingleCollisions_Type()
)
ieee8023MacSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacSingleCollisions.setStatus("mandatory")
_Ieee8023MacMultipleCollisions_Type = Counter32
_Ieee8023MacMultipleCollisions_Object = MibTableColumn
ieee8023MacMultipleCollisions = _Ieee8023MacMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 7),
    _Ieee8023MacMultipleCollisions_Type()
)
ieee8023MacMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacMultipleCollisions.setStatus("mandatory")
_Ieee8023MacExcessCollisions_Type = Counter32
_Ieee8023MacExcessCollisions_Object = MibTableColumn
ieee8023MacExcessCollisions = _Ieee8023MacExcessCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 8),
    _Ieee8023MacExcessCollisions_Type()
)
ieee8023MacExcessCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacExcessCollisions.setStatus("mandatory")
_Ieee8023MacLateCollisions_Type = Counter32
_Ieee8023MacLateCollisions_Object = MibTableColumn
ieee8023MacLateCollisions = _Ieee8023MacLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 9),
    _Ieee8023MacLateCollisions_Type()
)
ieee8023MacLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacLateCollisions.setStatus("mandatory")
_Ieee8023MacCarrierLostErrors_Type = Counter32
_Ieee8023MacCarrierLostErrors_Object = MibTableColumn
ieee8023MacCarrierLostErrors = _Ieee8023MacCarrierLostErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 10),
    _Ieee8023MacCarrierLostErrors_Type()
)
ieee8023MacCarrierLostErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacCarrierLostErrors.setStatus("mandatory")
_Ieee8023MacNoHeartBeatErrors_Type = Counter32
_Ieee8023MacNoHeartBeatErrors_Object = MibTableColumn
ieee8023MacNoHeartBeatErrors = _Ieee8023MacNoHeartBeatErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 11),
    _Ieee8023MacNoHeartBeatErrors_Type()
)
ieee8023MacNoHeartBeatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacNoHeartBeatErrors.setStatus("mandatory")
_Ieee8023MacFramesReceived_Type = Counter32
_Ieee8023MacFramesReceived_Object = MibTableColumn
ieee8023MacFramesReceived = _Ieee8023MacFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 12),
    _Ieee8023MacFramesReceived_Type()
)
ieee8023MacFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacFramesReceived.setStatus("mandatory")
_Ieee8023MacUndeliverableFramesReceived_Type = Counter32
_Ieee8023MacUndeliverableFramesReceived_Object = MibTableColumn
ieee8023MacUndeliverableFramesReceived = _Ieee8023MacUndeliverableFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 13),
    _Ieee8023MacUndeliverableFramesReceived_Type()
)
ieee8023MacUndeliverableFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacUndeliverableFramesReceived.setStatus("mandatory")
_Ieee8023MacCRCErrors_Type = Counter32
_Ieee8023MacCRCErrors_Object = MibTableColumn
ieee8023MacCRCErrors = _Ieee8023MacCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 14),
    _Ieee8023MacCRCErrors_Type()
)
ieee8023MacCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacCRCErrors.setStatus("mandatory")
_Ieee8023MacAlignmentErrors_Type = Counter32
_Ieee8023MacAlignmentErrors_Object = MibTableColumn
ieee8023MacAlignmentErrors = _Ieee8023MacAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 15),
    _Ieee8023MacAlignmentErrors_Type()
)
ieee8023MacAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacAlignmentErrors.setStatus("mandatory")
_Ieee8023MacResourceErrors_Type = Counter32
_Ieee8023MacResourceErrors_Object = MibTableColumn
ieee8023MacResourceErrors = _Ieee8023MacResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 16),
    _Ieee8023MacResourceErrors_Type()
)
ieee8023MacResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacResourceErrors.setStatus("mandatory")
_Ieee8023MacControlFieldErrors_Type = Counter32
_Ieee8023MacControlFieldErrors_Object = MibTableColumn
ieee8023MacControlFieldErrors = _Ieee8023MacControlFieldErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 17),
    _Ieee8023MacControlFieldErrors_Type()
)
ieee8023MacControlFieldErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacControlFieldErrors.setStatus("mandatory")
_Ieee8023MacUnknownProtocolErrors_Type = Counter32
_Ieee8023MacUnknownProtocolErrors_Object = MibTableColumn
ieee8023MacUnknownProtocolErrors = _Ieee8023MacUnknownProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 18),
    _Ieee8023MacUnknownProtocolErrors_Type()
)
ieee8023MacUnknownProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacUnknownProtocolErrors.setStatus("mandatory")
_Ieee8023MacMulticastsAccepted_Type = Counter32
_Ieee8023MacMulticastsAccepted_Object = MibTableColumn
ieee8023MacMulticastsAccepted = _Ieee8023MacMulticastsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 1, 1, 1, 19),
    _Ieee8023MacMulticastsAccepted_Type()
)
ieee8023MacMulticastsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MacMulticastsAccepted.setStatus("mandatory")
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 7)
)
_IcmpEchoReq_Type = Integer32
_IcmpEchoReq_Object = MibScalar
icmpEchoReq = _IcmpEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 7, 1),
    _IcmpEchoReq_Type()
)
icmpEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpEchoReq.setStatus("mandatory")
_IcmpEchoReqTable_Object = MibTable
icmpEchoReqTable = _IcmpEchoReqTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 7, 2)
)
if mibBuilder.loadTexts:
    icmpEchoReqTable.setStatus("mandatory")
_IcmpEchoReqEntry_Object = MibTableRow
icmpEchoReqEntry = _IcmpEchoReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 7, 2, 1)
)
icmpEchoReqEntry.setIndexNames(
    (0, "HP-UNIX", "icmpEchoReqPktSize"),
    (0, "HP-UNIX", "icmpEchoReqTimeOut"),
    (0, "HP-UNIX", "icmpEchoReqHost"),
)
if mibBuilder.loadTexts:
    icmpEchoReqEntry.setStatus("mandatory")
_IcmpEchoReqTime_Type = Integer32
_IcmpEchoReqTime_Object = MibTableColumn
icmpEchoReqTime = _IcmpEchoReqTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 7, 2, 1, 1),
    _IcmpEchoReqTime_Type()
)
icmpEchoReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpEchoReqTime.setStatus("mandatory")
_IcmpEchoReqPktSize_Type = Integer32
_IcmpEchoReqPktSize_Object = MibTableColumn
icmpEchoReqPktSize = _IcmpEchoReqPktSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 7, 2, 1, 2),
    _IcmpEchoReqPktSize_Type()
)
icmpEchoReqPktSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icmpEchoReqPktSize.setStatus("mandatory")
_IcmpEchoReqTimeOut_Type = Integer32
_IcmpEchoReqTimeOut_Object = MibTableColumn
icmpEchoReqTimeOut = _IcmpEchoReqTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 7, 2, 1, 3),
    _IcmpEchoReqTimeOut_Type()
)
icmpEchoReqTimeOut.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icmpEchoReqTimeOut.setStatus("mandatory")
_IcmpEchoReqHost_Type = IpAddress
_IcmpEchoReqHost_Object = MibTableColumn
icmpEchoReqHost = _IcmpEchoReqHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 7, 2, 1, 4),
    _IcmpEchoReqHost_Type()
)
icmpEchoReqHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icmpEchoReqHost.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1)
)
_TrapDestinationNum_Type = Gauge32
_TrapDestinationNum_Object = MibScalar
trapDestinationNum = _TrapDestinationNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 1),
    _TrapDestinationNum_Type()
)
trapDestinationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestinationNum.setStatus("mandatory")
_TrapDestinationTable_Object = MibTable
trapDestinationTable = _TrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 2)
)
if mibBuilder.loadTexts:
    trapDestinationTable.setStatus("mandatory")
_TrapDestinationEntry_Object = MibTableRow
trapDestinationEntry = _TrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 2, 1)
)
trapDestinationEntry.setIndexNames(
    (0, "HP-UNIX", "trapDestination"),
)
if mibBuilder.loadTexts:
    trapDestinationEntry.setStatus("mandatory")
_TrapDestination_Type = IpAddress
_TrapDestination_Object = MibTableColumn
trapDestination = _TrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1, 2, 1, 1),
    _TrapDestination_Type()
)
trapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestination.setStatus("mandatory")
_SnmpdConf_ObjectIdentity = ObjectIdentity
snmpdConf = _SnmpdConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2)
)


class _SnmpdConfRespond_Type(Integer32):
    """Custom type snmpdConfRespond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SnmpdConfRespond_Type.__name__ = "Integer32"
_SnmpdConfRespond_Object = MibScalar
snmpdConfRespond = _SnmpdConfRespond_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 1),
    _SnmpdConfRespond_Type()
)
snmpdConfRespond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdConfRespond.setStatus("mandatory")


class _SnmpdReConfigure_Type(Integer32):
    """Custom type snmpdReConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_SnmpdReConfigure_Type.__name__ = "Integer32"
_SnmpdReConfigure_Object = MibScalar
snmpdReConfigure = _SnmpdReConfigure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 2),
    _SnmpdReConfigure_Type()
)
snmpdReConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdReConfigure.setStatus("mandatory")


class _SnmpdFlag_Type(Integer32):
    """Custom type snmpdFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netwareproxy", 2),
          ("removetrap", 1))
    )


_SnmpdFlag_Type.__name__ = "Integer32"
_SnmpdFlag_Object = MibScalar
snmpdFlag = _SnmpdFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 3),
    _SnmpdFlag_Type()
)
snmpdFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpdFlag.setStatus("mandatory")
_SnmpdLogMask_Type = Integer32
_SnmpdLogMask_Object = MibScalar
snmpdLogMask = _SnmpdLogMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 4),
    _SnmpdLogMask_Type()
)
snmpdLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdLogMask.setStatus("mandatory")
_SnmpdVersion_Type = Integer32
_SnmpdVersion_Object = MibScalar
snmpdVersion = _SnmpdVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 5),
    _SnmpdVersion_Type()
)
snmpdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpdVersion.setStatus("mandatory")


class _SnmpdStatus_Type(Integer32):
    """Custom type snmpdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SnmpdStatus_Type.__name__ = "Integer32"
_SnmpdStatus_Object = MibScalar
snmpdStatus = _SnmpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 6),
    _SnmpdStatus_Type()
)
snmpdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdStatus.setStatus("mandatory")
_SnmpdSize_Type = Integer32
_SnmpdSize_Object = MibScalar
snmpdSize = _SnmpdSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 7),
    _SnmpdSize_Type()
)
snmpdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpdSize.setStatus("mandatory")
_SnmpdWhatString_Type = DisplayString
_SnmpdWhatString_Object = MibScalar
snmpdWhatString = _SnmpdWhatString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2, 9),
    _SnmpdWhatString_Type()
)
snmpdWhatString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpdWhatString.setStatus("mandatory")
_Authfail_ObjectIdentity = ObjectIdentity
authfail = _Authfail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 4)
)
_AuthFailTable_Object = MibTable
authFailTable = _AuthFailTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 4, 1)
)
if mibBuilder.loadTexts:
    authFailTable.setStatus("mandatory")
_AuthFailEntry_Object = MibTableRow
authFailEntry = _AuthFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 4, 1, 1)
)
authFailEntry.setIndexNames(
    (0, "HP-UNIX", "authIpAddress"),
)
if mibBuilder.loadTexts:
    authFailEntry.setStatus("mandatory")
_AuthIpAddress_Type = IpAddress
_AuthIpAddress_Object = MibTableColumn
authIpAddress = _AuthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 4, 1, 1, 1),
    _AuthIpAddress_Type()
)
authIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authIpAddress.setStatus("mandatory")
_AuthTime_Type = TimeTicks
_AuthTime_Object = MibTableColumn
authTime = _AuthTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 4, 1, 1, 2),
    _AuthTime_Type()
)
authTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authTime.setStatus("mandatory")
_AuthCommunityName_Type = OctetString
_AuthCommunityName_Object = MibTableColumn
authCommunityName = _AuthCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 4, 1, 1, 3),
    _AuthCommunityName_Type()
)
authCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authCommunityName.setStatus("mandatory")
_OpenView_ObjectIdentity = ObjectIdentity
openView = _OpenView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17)
)
_HpOpenView_ObjectIdentity = ObjectIdentity
hpOpenView = _HpOpenView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 1)
)
_OpenViewTrapVars_ObjectIdentity = ObjectIdentity
openViewTrapVars = _OpenViewTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2)
)
_OpenViewSourceId_Type = Integer32
_OpenViewSourceId_Object = MibScalar
openViewSourceId = _OpenViewSourceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 1),
    _OpenViewSourceId_Type()
)
openViewSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewSourceId.setStatus("mandatory")
_OpenViewSourceName_Type = OctetString
_OpenViewSourceName_Object = MibScalar
openViewSourceName = _OpenViewSourceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 2),
    _OpenViewSourceName_Type()
)
openViewSourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewSourceName.setStatus("mandatory")
_OpenViewObjectId_Type = OctetString
_OpenViewObjectId_Object = MibScalar
openViewObjectId = _OpenViewObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 3),
    _OpenViewObjectId_Type()
)
openViewObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewObjectId.setStatus("mandatory")
_OpenViewData_Type = OctetString
_OpenViewData_Object = MibScalar
openViewData = _OpenViewData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 4),
    _OpenViewData_Type()
)
openViewData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewData.setStatus("mandatory")
_OpenViewSeverity_Type = OctetString
_OpenViewSeverity_Object = MibScalar
openViewSeverity = _OpenViewSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 5),
    _OpenViewSeverity_Type()
)
openViewSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewSeverity.setStatus("mandatory")
_OpenViewCategory_Type = OctetString
_OpenViewCategory_Object = MibScalar
openViewCategory = _OpenViewCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 6),
    _OpenViewCategory_Type()
)
openViewCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewCategory.setStatus("mandatory")
_OpenViewFilter_Type = OctetString
_OpenViewFilter_Object = MibScalar
openViewFilter = _OpenViewFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 7),
    _OpenViewFilter_Type()
)
openViewFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewFilter.setStatus("mandatory")
_OpenViewEntity_Type = OctetString
_OpenViewEntity_Object = MibScalar
openViewEntity = _OpenViewEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 8),
    _OpenViewEntity_Type()
)
openViewEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewEntity.setStatus("mandatory")
_OpenViewAddress_Type = OctetString
_OpenViewAddress_Object = MibScalar
openViewAddress = _OpenViewAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 9),
    _OpenViewAddress_Type()
)
openViewAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewAddress.setStatus("mandatory")
_OpenViewPid_Type = OctetString
_OpenViewPid_Object = MibScalar
openViewPid = _OpenViewPid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 10),
    _OpenViewPid_Type()
)
openViewPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    openViewPid.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-UNIX",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "general": general,
       "computerSystem": computerSystem,
       "computerSystemUpTime": computerSystemUpTime,
       "computerSystemUsers": computerSystemUsers,
       "computerSystemAvgJobs1": computerSystemAvgJobs1,
       "computerSystemAvgJobs5": computerSystemAvgJobs5,
       "computerSystemAvgJobs15": computerSystemAvgJobs15,
       "computerSystemMaxProc": computerSystemMaxProc,
       "computerSystemFreeMemory": computerSystemFreeMemory,
       "computerSystemPhysMemory": computerSystemPhysMemory,
       "computerSystemMaxUserMem": computerSystemMaxUserMem,
       "computerSystemSwapConfig": computerSystemSwapConfig,
       "computerSystemEnabledSwap": computerSystemEnabledSwap,
       "computerSystemFreeSwap": computerSystemFreeSwap,
       "computerSystemUserCPU": computerSystemUserCPU,
       "computerSystemSysCPU": computerSystemSysCPU,
       "computerSystemIdleCPU": computerSystemIdleCPU,
       "computerSystemNiceCPU": computerSystemNiceCPU,
       "fileSystem": fileSystem,
       "fileSystemMounted": fileSystemMounted,
       "fileSystemTable": fileSystemTable,
       "fileSystemEntry": fileSystemEntry,
       "fileSystemID1": fileSystemID1,
       "fileSystemID2": fileSystemID2,
       "fileSystemName": fileSystemName,
       "fileSystemBlock": fileSystemBlock,
       "fileSystemBfree": fileSystemBfree,
       "fileSystemBavail": fileSystemBavail,
       "fileSystemBsize": fileSystemBsize,
       "fileSystemFiles": fileSystemFiles,
       "fileSystemFfree": fileSystemFfree,
       "fileSystemDir": fileSystemDir,
       "processes": processes,
       "processNum": processNum,
       "processTable": processTable,
       "processEntry": processEntry,
       "processPID": processPID,
       "processIdx": processIdx,
       "processUID": processUID,
       "processPPID": processPPID,
       "processDsize": processDsize,
       "processTsize": processTsize,
       "processSsize": processSsize,
       "processNice": processNice,
       "processMajor": processMajor,
       "processMinor": processMinor,
       "processPgrp": processPgrp,
       "processPrio": processPrio,
       "processAddr": processAddr,
       "processCPU": processCPU,
       "processUtime": processUtime,
       "processStime": processStime,
       "processStart": processStart,
       "processFlags": processFlags,
       "processStatus": processStatus,
       "processWchan": processWchan,
       "processProcNum": processProcNum,
       "processCmd": processCmd,
       "processTime": processTime,
       "processCPUticks": processCPUticks,
       "processCPUticksTotal": processCPUticksTotal,
       "processFss": processFss,
       "processPctCPU": processPctCPU,
       "processRssize": processRssize,
       "processSUID": processSUID,
       "processUname": processUname,
       "processTTY": processTTY,
       "cluster": cluster,
       "isClustered": isClustered,
       "clusterTable": clusterTable,
       "clusterEntry": clusterEntry,
       "clusterID": clusterID,
       "clusterMachineID": clusterMachineID,
       "clusterType": clusterType,
       "clusterCnodeName": clusterCnodeName,
       "clusterSwapServingCnode": clusterSwapServingCnode,
       "clusterKcsp": clusterKcsp,
       "clusterCnodeAddress": clusterCnodeAddress,
       "clusterCnodeID": clusterCnodeID,
       "hpux": hpux,
       "hp9000s300": hp9000s300,
       "hp9000s800": hp9000s800,
       "hp9000s700": hp9000s700,
       "hp386": hp386,
       "hpsun": hpsun,
       "sparc": sparc,
       "sun4": sun4,
       "sun5": sun5,
       "interface": interface,
       "ieee8023Mac": ieee8023Mac,
       "ieee8023MacTable": ieee8023MacTable,
       "ieee8023MacEntry": ieee8023MacEntry,
       "ieee8023MacIndex": ieee8023MacIndex,
       "ieee8023MacTransmitted": ieee8023MacTransmitted,
       "ieee8023MacNotTransmitted": ieee8023MacNotTransmitted,
       "ieee8023MacDeferred": ieee8023MacDeferred,
       "ieee8023MacCollisions": ieee8023MacCollisions,
       "ieee8023MacSingleCollisions": ieee8023MacSingleCollisions,
       "ieee8023MacMultipleCollisions": ieee8023MacMultipleCollisions,
       "ieee8023MacExcessCollisions": ieee8023MacExcessCollisions,
       "ieee8023MacLateCollisions": ieee8023MacLateCollisions,
       "ieee8023MacCarrierLostErrors": ieee8023MacCarrierLostErrors,
       "ieee8023MacNoHeartBeatErrors": ieee8023MacNoHeartBeatErrors,
       "ieee8023MacFramesReceived": ieee8023MacFramesReceived,
       "ieee8023MacUndeliverableFramesReceived": ieee8023MacUndeliverableFramesReceived,
       "ieee8023MacCRCErrors": ieee8023MacCRCErrors,
       "ieee8023MacAlignmentErrors": ieee8023MacAlignmentErrors,
       "ieee8023MacResourceErrors": ieee8023MacResourceErrors,
       "ieee8023MacControlFieldErrors": ieee8023MacControlFieldErrors,
       "ieee8023MacUnknownProtocolErrors": ieee8023MacUnknownProtocolErrors,
       "ieee8023MacMulticastsAccepted": ieee8023MacMulticastsAccepted,
       "icmp": icmp,
       "icmpEchoReq": icmpEchoReq,
       "icmpEchoReqTable": icmpEchoReqTable,
       "icmpEchoReqEntry": icmpEchoReqEntry,
       "icmpEchoReqTime": icmpEchoReqTime,
       "icmpEchoReqPktSize": icmpEchoReqPktSize,
       "icmpEchoReqTimeOut": icmpEchoReqTimeOut,
       "icmpEchoReqHost": icmpEchoReqHost,
       "snmp": snmp,
       "trap": trap,
       "trapDestinationNum": trapDestinationNum,
       "trapDestinationTable": trapDestinationTable,
       "trapDestinationEntry": trapDestinationEntry,
       "trapDestination": trapDestination,
       "snmpdConf": snmpdConf,
       "snmpdConfRespond": snmpdConfRespond,
       "snmpdReConfigure": snmpdReConfigure,
       "snmpdFlag": snmpdFlag,
       "snmpdLogMask": snmpdLogMask,
       "snmpdVersion": snmpdVersion,
       "snmpdStatus": snmpdStatus,
       "snmpdSize": snmpdSize,
       "snmpdWhatString": snmpdWhatString,
       "authfail": authfail,
       "authFailTable": authFailTable,
       "authFailEntry": authFailEntry,
       "authIpAddress": authIpAddress,
       "authTime": authTime,
       "authCommunityName": authCommunityName,
       "openView": openView,
       "hpOpenView": hpOpenView,
       "openViewTrapVars": openViewTrapVars,
       "openViewSourceId": openViewSourceId,
       "openViewSourceName": openViewSourceName,
       "openViewObjectId": openViewObjectId,
       "openViewData": openViewData,
       "openViewSeverity": openViewSeverity,
       "openViewCategory": openViewCategory,
       "openViewFilter": openViewFilter,
       "openViewEntity": openViewEntity,
       "openViewAddress": openViewAddress,
       "openViewPid": openViewPid}
)
