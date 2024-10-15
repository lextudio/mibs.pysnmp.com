# SNMP MIB module (KERNEL-READER-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KERNEL-READER-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:41 2024
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

kernelReader = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12)
)
kernelReader.setRevisions(
        ("1999-07-20 15:05",
         "1900-09-18 14:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_KrConsoleUser_Type = DisplayString
_KrConsoleUser_Object = MibScalar
krConsoleUser = _KrConsoleUser_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 1, 1),
    _KrConsoleUser_Type()
)
krConsoleUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krConsoleUser.setStatus("current")
_KrTotNumOfUsers_Type = Integer32
_KrTotNumOfUsers_Object = MibScalar
krTotNumOfUsers = _KrTotNumOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 1, 2),
    _KrTotNumOfUsers_Type()
)
krTotNumOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotNumOfUsers.setStatus("current")
_KrTotNumOfSessions_Type = Integer32
_KrTotNumOfSessions_Object = MibScalar
krTotNumOfSessions = _KrTotNumOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 1, 3),
    _KrTotNumOfSessions_Type()
)
krTotNumOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotNumOfSessions.setStatus("current")
_KrPrimaryUser_Type = DisplayString
_KrPrimaryUser_Object = MibScalar
krPrimaryUser = _KrPrimaryUser_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 1, 4),
    _KrPrimaryUser_Type()
)
krPrimaryUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krPrimaryUser.setStatus("current")
_KrSystemLoadAvg1min_Type = DisplayString
_KrSystemLoadAvg1min_Object = MibScalar
krSystemLoadAvg1min = _KrSystemLoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 2, 1),
    _KrSystemLoadAvg1min_Type()
)
krSystemLoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSystemLoadAvg1min.setStatus("current")
if mibBuilder.loadTexts:
    krSystemLoadAvg1min.setUnits("Jobs")
_KrSystemLoadAvg5min_Type = DisplayString
_KrSystemLoadAvg5min_Object = MibScalar
krSystemLoadAvg5min = _KrSystemLoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 2, 2),
    _KrSystemLoadAvg5min_Type()
)
krSystemLoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSystemLoadAvg5min.setStatus("current")
if mibBuilder.loadTexts:
    krSystemLoadAvg5min.setUnits("Jobs")
_KrSystemLoadAvg15min_Type = DisplayString
_KrSystemLoadAvg15min_Object = MibScalar
krSystemLoadAvg15min = _KrSystemLoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 2, 3),
    _KrSystemLoadAvg15min_Type()
)
krSystemLoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSystemLoadAvg15min.setStatus("current")
if mibBuilder.loadTexts:
    krSystemLoadAvg15min.setUnits("Jobs")
_KrSystemUpTime_Type = DisplayString
_KrSystemUpTime_Object = MibScalar
krSystemUpTime = _KrSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 2, 4),
    _KrSystemUpTime_Type()
)
krSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSystemUpTime.setStatus("current")
_KrDisk_ObjectIdentity = ObjectIdentity
krDisk = _KrDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3)
)
_KrDiskDetailTable_Object = MibTable
krDiskDetailTable = _KrDiskDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    krDiskDetailTable.setStatus("current")
_KrDiskDetailEntry_Object = MibTableRow
krDiskDetailEntry = _KrDiskDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1)
)
krDiskDetailEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDDDiskName"),
)
if mibBuilder.loadTexts:
    krDiskDetailEntry.setStatus("current")
_KrDDDiskName_Type = DisplayString
_KrDDDiskName_Object = MibTableColumn
krDDDiskName = _KrDDDiskName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 1),
    _KrDDDiskName_Type()
)
krDDDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDDDiskName.setStatus("current")
_KrDiskAliasName_Type = DisplayString
_KrDiskAliasName_Object = MibTableColumn
krDiskAliasName = _KrDiskAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 2),
    _KrDiskAliasName_Type()
)
krDiskAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskAliasName.setStatus("current")
_KrDiskReadOpRate_Type = DisplayString
_KrDiskReadOpRate_Object = MibTableColumn
krDiskReadOpRate = _KrDiskReadOpRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 3),
    _KrDiskReadOpRate_Type()
)
krDiskReadOpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskReadOpRate.setStatus("current")
if mibBuilder.loadTexts:
    krDiskReadOpRate.setUnits("op/sec")
_KrDiskWriteOpRate_Type = DisplayString
_KrDiskWriteOpRate_Object = MibTableColumn
krDiskWriteOpRate = _KrDiskWriteOpRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 4),
    _KrDiskWriteOpRate_Type()
)
krDiskWriteOpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskWriteOpRate.setStatus("current")
if mibBuilder.loadTexts:
    krDiskWriteOpRate.setUnits("op/sec")
_KrDiskOperationRate_Type = DisplayString
_KrDiskOperationRate_Object = MibTableColumn
krDiskOperationRate = _KrDiskOperationRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 5),
    _KrDiskOperationRate_Type()
)
krDiskOperationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskOperationRate.setStatus("current")
if mibBuilder.loadTexts:
    krDiskOperationRate.setUnits("op/sec")
_KrDiskDataReadRate_Type = DisplayString
_KrDiskDataReadRate_Object = MibTableColumn
krDiskDataReadRate = _KrDiskDataReadRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 6),
    _KrDiskDataReadRate_Type()
)
krDiskDataReadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskDataReadRate.setStatus("current")
if mibBuilder.loadTexts:
    krDiskDataReadRate.setUnits("KB/sec")
_KrDiskDataWriteRate_Type = DisplayString
_KrDiskDataWriteRate_Object = MibTableColumn
krDiskDataWriteRate = _KrDiskDataWriteRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 7),
    _KrDiskDataWriteRate_Type()
)
krDiskDataWriteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskDataWriteRate.setStatus("current")
if mibBuilder.loadTexts:
    krDiskDataWriteRate.setUnits("KB/secops")
_KrDiskDataTransferRate_Type = DisplayString
_KrDiskDataTransferRate_Object = MibTableColumn
krDiskDataTransferRate = _KrDiskDataTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 8),
    _KrDiskDataTransferRate_Type()
)
krDiskDataTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskDataTransferRate.setStatus("current")
if mibBuilder.loadTexts:
    krDiskDataTransferRate.setUnits("KB/sec")
_KrDiskAvgWaitTrans_Type = DisplayString
_KrDiskAvgWaitTrans_Object = MibTableColumn
krDiskAvgWaitTrans = _KrDiskAvgWaitTrans_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 9),
    _KrDiskAvgWaitTrans_Type()
)
krDiskAvgWaitTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskAvgWaitTrans.setStatus("current")
_KrDiskAvgRunTrans_Type = DisplayString
_KrDiskAvgRunTrans_Object = MibTableColumn
krDiskAvgRunTrans = _KrDiskAvgRunTrans_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1, 1, 1, 10),
    _KrDiskAvgRunTrans_Type()
)
krDiskAvgRunTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskAvgRunTrans.setStatus("current")
_KrDiskSrvTable_Object = MibTable
krDiskSrvTable = _KrDiskSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    krDiskSrvTable.setStatus("current")
_KrDiskSrvEntry_Object = MibTableRow
krDiskSrvEntry = _KrDiskSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1, 1)
)
krDiskSrvEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDSDiskName"),
)
if mibBuilder.loadTexts:
    krDiskSrvEntry.setStatus("current")
_KrDSDiskName_Type = DisplayString
_KrDSDiskName_Object = MibTableColumn
krDSDiskName = _KrDSDiskName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1, 1, 1),
    _KrDSDiskName_Type()
)
krDSDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDSDiskName.setStatus("current")
_KrDiskSrvcWaitPctTime_Type = DisplayString
_KrDiskSrvcWaitPctTime_Object = MibTableColumn
krDiskSrvcWaitPctTime = _KrDiskSrvcWaitPctTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1, 1, 2),
    _KrDiskSrvcWaitPctTime_Type()
)
krDiskSrvcWaitPctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskSrvcWaitPctTime.setStatus("current")
if mibBuilder.loadTexts:
    krDiskSrvcWaitPctTime.setUnits("%")
_KrDiskBusyPctTime_Type = DisplayString
_KrDiskBusyPctTime_Object = MibTableColumn
krDiskBusyPctTime = _KrDiskBusyPctTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1, 1, 3),
    _KrDiskBusyPctTime_Type()
)
krDiskBusyPctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskBusyPctTime.setStatus("current")
if mibBuilder.loadTexts:
    krDiskBusyPctTime.setUnits("%")
_KrDiskSrvcAvgWaitTime_Type = DisplayString
_KrDiskSrvcAvgWaitTime_Object = MibTableColumn
krDiskSrvcAvgWaitTime = _KrDiskSrvcAvgWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1, 1, 4),
    _KrDiskSrvcAvgWaitTime_Type()
)
krDiskSrvcAvgWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskSrvcAvgWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    krDiskSrvcAvgWaitTime.setUnits("msec")
_KrDiskSrvcAvgTransRunTime_Type = DisplayString
_KrDiskSrvcAvgTransRunTime_Object = MibTableColumn
krDiskSrvcAvgTransRunTime = _KrDiskSrvcAvgTransRunTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1, 1, 5),
    _KrDiskSrvcAvgTransRunTime_Type()
)
krDiskSrvcAvgTransRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskSrvcAvgTransRunTime.setStatus("current")
if mibBuilder.loadTexts:
    krDiskSrvcAvgTransRunTime.setUnits("msec")
_KrDiskSrvcAvgTransTime_Type = DisplayString
_KrDiskSrvcAvgTransTime_Object = MibTableColumn
krDiskSrvcAvgTransTime = _KrDiskSrvcAvgTransTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2, 1, 1, 6),
    _KrDiskSrvcAvgTransTime_Type()
)
krDiskSrvcAvgTransTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDiskSrvcAvgTransTime.setStatus("current")
if mibBuilder.loadTexts:
    krDiskSrvcAvgTransTime.setUnits("msec")
_KrFileSystem_ObjectIdentity = ObjectIdentity
krFileSystem = _KrFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4)
)
_KrUFSFileTable_Object = MibTable
krUFSFileTable = _KrUFSFileTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1)
)
if mibBuilder.loadTexts:
    krUFSFileTable.setStatus("current")
_KrUFSFileEntry_Object = MibTableRow
krUFSFileEntry = _KrUFSFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1)
)
krUFSFileEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemIndex"),
)
if mibBuilder.loadTexts:
    krUFSFileEntry.setStatus("current")
_KrUFSFileSystemIndex_Type = DisplayString
_KrUFSFileSystemIndex_Object = MibTableColumn
krUFSFileSystemIndex = _KrUFSFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 1),
    _KrUFSFileSystemIndex_Type()
)
krUFSFileSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemIndex.setStatus("current")
_KrUFSFileSystemMountPoint_Type = DisplayString
_KrUFSFileSystemMountPoint_Object = MibTableColumn
krUFSFileSystemMountPoint = _KrUFSFileSystemMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 2),
    _KrUFSFileSystemMountPoint_Type()
)
krUFSFileSystemMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemMountPoint.setStatus("current")
_KrUFSFileSystemDiskName_Type = DisplayString
_KrUFSFileSystemDiskName_Object = MibTableColumn
krUFSFileSystemDiskName = _KrUFSFileSystemDiskName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 3),
    _KrUFSFileSystemDiskName_Type()
)
krUFSFileSystemDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemDiskName.setStatus("current")
_KrUFSFileSystemSize_Type = Integer32
_KrUFSFileSystemSize_Object = MibTableColumn
krUFSFileSystemSize = _KrUFSFileSystemSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 4),
    _KrUFSFileSystemSize_Type()
)
krUFSFileSystemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemSize.setStatus("current")
if mibBuilder.loadTexts:
    krUFSFileSystemSize.setUnits("KB")
_KrUFSFileSystemFreeSpace_Type = Integer32
_KrUFSFileSystemFreeSpace_Object = MibTableColumn
krUFSFileSystemFreeSpace = _KrUFSFileSystemFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 5),
    _KrUFSFileSystemFreeSpace_Type()
)
krUFSFileSystemFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    krUFSFileSystemFreeSpace.setUnits("KB")
_KrUFSFreeSpaceForNonSU_Type = Integer32
_KrUFSFreeSpaceForNonSU_Object = MibTableColumn
krUFSFreeSpaceForNonSU = _KrUFSFreeSpaceForNonSU_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 6),
    _KrUFSFreeSpaceForNonSU_Type()
)
krUFSFreeSpaceForNonSU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFreeSpaceForNonSU.setStatus("current")
if mibBuilder.loadTexts:
    krUFSFreeSpaceForNonSU.setUnits("KB")
_KrUFSFileSystemPctUsedSpace_Type = DisplayString
_KrUFSFileSystemPctUsedSpace_Object = MibTableColumn
krUFSFileSystemPctUsedSpace = _KrUFSFileSystemPctUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 7),
    _KrUFSFileSystemPctUsedSpace_Type()
)
krUFSFileSystemPctUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemPctUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    krUFSFileSystemPctUsedSpace.setUnits("%")
_KrUFSTotNumOfInodes_Type = Integer32
_KrUFSTotNumOfInodes_Object = MibTableColumn
krUFSTotNumOfInodes = _KrUFSTotNumOfInodes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 8),
    _KrUFSTotNumOfInodes_Type()
)
krUFSTotNumOfInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSTotNumOfInodes.setStatus("current")
if mibBuilder.loadTexts:
    krUFSTotNumOfInodes.setUnits("inodes")
_KrUFSTotNumOfInodesAvail_Type = Integer32
_KrUFSTotNumOfInodesAvail_Object = MibTableColumn
krUFSTotNumOfInodesAvail = _KrUFSTotNumOfInodesAvail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 9),
    _KrUFSTotNumOfInodesAvail_Type()
)
krUFSTotNumOfInodesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSTotNumOfInodesAvail.setStatus("current")
if mibBuilder.loadTexts:
    krUFSTotNumOfInodesAvail.setUnits("inodes")
_KrUFSPctInodesUsed_Type = DisplayString
_KrUFSPctInodesUsed_Object = MibTableColumn
krUFSPctInodesUsed = _KrUFSPctInodesUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 10),
    _KrUFSPctInodesUsed_Type()
)
krUFSPctInodesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSPctInodesUsed.setStatus("current")
if mibBuilder.loadTexts:
    krUFSPctInodesUsed.setUnits("%")
_KrUFSFileSystemSize64_Type = Counter64
_KrUFSFileSystemSize64_Object = MibTableColumn
krUFSFileSystemSize64 = _KrUFSFileSystemSize64_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 11),
    _KrUFSFileSystemSize64_Type()
)
krUFSFileSystemSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemSize64.setStatus("current")
if mibBuilder.loadTexts:
    krUFSFileSystemSize64.setUnits("KB")
_KrUFSFileSystemFreeSpace64_Type = Counter64
_KrUFSFileSystemFreeSpace64_Object = MibTableColumn
krUFSFileSystemFreeSpace64 = _KrUFSFileSystemFreeSpace64_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 12),
    _KrUFSFileSystemFreeSpace64_Type()
)
krUFSFileSystemFreeSpace64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFileSystemFreeSpace64.setStatus("current")
if mibBuilder.loadTexts:
    krUFSFileSystemFreeSpace64.setUnits("KB")
_KrUFSFreeSpaceForNonSU64_Type = Counter64
_KrUFSFreeSpaceForNonSU64_Object = MibTableColumn
krUFSFreeSpaceForNonSU64 = _KrUFSFreeSpaceForNonSU64_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1, 1, 1, 13),
    _KrUFSFreeSpaceForNonSU64_Type()
)
krUFSFreeSpaceForNonSU64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krUFSFreeSpaceForNonSU64.setStatus("current")
if mibBuilder.loadTexts:
    krUFSFreeSpaceForNonSU64.setUnits("KB")
_KrVXFSFileTable_Object = MibTable
krVXFSFileTable = _KrVXFSFileTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1)
)
if mibBuilder.loadTexts:
    krVXFSFileTable.setStatus("current")
_KrVXFSFileEntry_Object = MibTableRow
krVXFSFileEntry = _KrVXFSFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1)
)
krVXFSFileEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemIndex"),
)
if mibBuilder.loadTexts:
    krVXFSFileEntry.setStatus("current")
_KrVXFSFileSystemIndex_Type = DisplayString
_KrVXFSFileSystemIndex_Object = MibTableColumn
krVXFSFileSystemIndex = _KrVXFSFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 1),
    _KrVXFSFileSystemIndex_Type()
)
krVXFSFileSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemIndex.setStatus("current")
_KrVXFSFileSystemMountPoint_Type = DisplayString
_KrVXFSFileSystemMountPoint_Object = MibTableColumn
krVXFSFileSystemMountPoint = _KrVXFSFileSystemMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 2),
    _KrVXFSFileSystemMountPoint_Type()
)
krVXFSFileSystemMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemMountPoint.setStatus("current")
_KrVXFSFileSystemDiskName_Type = DisplayString
_KrVXFSFileSystemDiskName_Object = MibTableColumn
krVXFSFileSystemDiskName = _KrVXFSFileSystemDiskName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 3),
    _KrVXFSFileSystemDiskName_Type()
)
krVXFSFileSystemDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemDiskName.setStatus("current")
_KrVXFSFileSystemSize_Type = Integer32
_KrVXFSFileSystemSize_Object = MibTableColumn
krVXFSFileSystemSize = _KrVXFSFileSystemSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 4),
    _KrVXFSFileSystemSize_Type()
)
krVXFSFileSystemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemSize.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSFileSystemSize.setUnits("KB")
_KrVXFSFileSystemFreeSpace_Type = Integer32
_KrVXFSFileSystemFreeSpace_Object = MibTableColumn
krVXFSFileSystemFreeSpace = _KrVXFSFileSystemFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 5),
    _KrVXFSFileSystemFreeSpace_Type()
)
krVXFSFileSystemFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSFileSystemFreeSpace.setUnits("KB")
_KrVXFSFreeSpaceForNonSU_Type = Integer32
_KrVXFSFreeSpaceForNonSU_Object = MibTableColumn
krVXFSFreeSpaceForNonSU = _KrVXFSFreeSpaceForNonSU_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 6),
    _KrVXFSFreeSpaceForNonSU_Type()
)
krVXFSFreeSpaceForNonSU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFreeSpaceForNonSU.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSFreeSpaceForNonSU.setUnits("KB")
_KrVXFSFileSystemPctUsedSpace_Type = DisplayString
_KrVXFSFileSystemPctUsedSpace_Object = MibTableColumn
krVXFSFileSystemPctUsedSpace = _KrVXFSFileSystemPctUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 7),
    _KrVXFSFileSystemPctUsedSpace_Type()
)
krVXFSFileSystemPctUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemPctUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSFileSystemPctUsedSpace.setUnits("%")
_KrVXFSTotNumOfInodes_Type = Integer32
_KrVXFSTotNumOfInodes_Object = MibTableColumn
krVXFSTotNumOfInodes = _KrVXFSTotNumOfInodes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 8),
    _KrVXFSTotNumOfInodes_Type()
)
krVXFSTotNumOfInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSTotNumOfInodes.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSTotNumOfInodes.setUnits("inodes")
_KrVXFSTotNumOfInodesAvail_Type = Integer32
_KrVXFSTotNumOfInodesAvail_Object = MibTableColumn
krVXFSTotNumOfInodesAvail = _KrVXFSTotNumOfInodesAvail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 9),
    _KrVXFSTotNumOfInodesAvail_Type()
)
krVXFSTotNumOfInodesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSTotNumOfInodesAvail.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSTotNumOfInodesAvail.setUnits("inodes")
_KrVXFSPctInodesUsed_Type = DisplayString
_KrVXFSPctInodesUsed_Object = MibTableColumn
krVXFSPctInodesUsed = _KrVXFSPctInodesUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 10),
    _KrVXFSPctInodesUsed_Type()
)
krVXFSPctInodesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSPctInodesUsed.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSPctInodesUsed.setUnits("%")
_KrVXFSFileSystemSize64_Type = Counter64
_KrVXFSFileSystemSize64_Object = MibTableColumn
krVXFSFileSystemSize64 = _KrVXFSFileSystemSize64_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 11),
    _KrVXFSFileSystemSize64_Type()
)
krVXFSFileSystemSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemSize64.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSFileSystemSize64.setUnits("KB")
_KrVXFSFileSystemFreeSpace64_Type = Counter64
_KrVXFSFileSystemFreeSpace64_Object = MibTableColumn
krVXFSFileSystemFreeSpace64 = _KrVXFSFileSystemFreeSpace64_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 12),
    _KrVXFSFileSystemFreeSpace64_Type()
)
krVXFSFileSystemFreeSpace64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFileSystemFreeSpace64.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSFileSystemFreeSpace64.setUnits("KB")
_KrVXFSFreeSpaceForNonSU64_Type = Counter64
_KrVXFSFreeSpaceForNonSU64_Object = MibTableColumn
krVXFSFreeSpaceForNonSU64 = _KrVXFSFreeSpaceForNonSU64_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2, 1, 1, 13),
    _KrVXFSFreeSpaceForNonSU64_Type()
)
krVXFSFreeSpaceForNonSU64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krVXFSFreeSpaceForNonSU64.setStatus("current")
if mibBuilder.loadTexts:
    krVXFSFreeSpaceForNonSU64.setUnits("KB")
_KrCPUDetail_ObjectIdentity = ObjectIdentity
krCPUDetail = _KrCPUDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5)
)
_KrCPUUtilTable_Object = MibTable
krCPUUtilTable = _KrCPUUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1)
)
if mibBuilder.loadTexts:
    krCPUUtilTable.setStatus("current")
_KrCPUUtilEntry_Object = MibTableRow
krCPUUtilEntry = _KrCPUUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1)
)
krCPUUtilEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPUUtilEntry.setStatus("current")


class _KrCPUInstance_Type(Integer32):
    """Custom type krCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrCPUInstance_Type.__name__ = "Integer32"
_KrCPUInstance_Object = MibTableColumn
krCPUInstance = _KrCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 1),
    _KrCPUInstance_Type()
)
krCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUInstance.setStatus("current")
_KrCPUDelta_Type = DisplayString
_KrCPUDelta_Object = MibTableColumn
krCPUDelta = _KrCPUDelta_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 2),
    _KrCPUDelta_Type()
)
krCPUDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUDelta.setStatus("current")
_KrCPUIdleTime_Type = DisplayString
_KrCPUIdleTime_Object = MibTableColumn
krCPUIdleTime = _KrCPUIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 3),
    _KrCPUIdleTime_Type()
)
krCPUIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUIdleTime.setStatus("current")
_KrCPUUserModeTime_Type = DisplayString
_KrCPUUserModeTime_Object = MibTableColumn
krCPUUserModeTime = _KrCPUUserModeTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 4),
    _KrCPUUserModeTime_Type()
)
krCPUUserModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUUserModeTime.setStatus("current")
_KrCPUKernelModeTime_Type = DisplayString
_KrCPUKernelModeTime_Object = MibTableColumn
krCPUKernelModeTime = _KrCPUKernelModeTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 5),
    _KrCPUKernelModeTime_Type()
)
krCPUKernelModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUKernelModeTime.setStatus("current")
_KrCPUTotWaitTime_Type = DisplayString
_KrCPUTotWaitTime_Object = MibTableColumn
krCPUTotWaitTime = _KrCPUTotWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 6),
    _KrCPUTotWaitTime_Type()
)
krCPUTotWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUTotWaitTime.setStatus("current")
_KrCPUTotIOWaitTime_Type = DisplayString
_KrCPUTotIOWaitTime_Object = MibTableColumn
krCPUTotIOWaitTime = _KrCPUTotIOWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 7),
    _KrCPUTotIOWaitTime_Type()
)
krCPUTotIOWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUTotIOWaitTime.setStatus("current")
_KrCPUTotSwapWaitTime_Type = DisplayString
_KrCPUTotSwapWaitTime_Object = MibTableColumn
krCPUTotSwapWaitTime = _KrCPUTotSwapWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 8),
    _KrCPUTotSwapWaitTime_Type()
)
krCPUTotSwapWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUTotSwapWaitTime.setStatus("current")
_KrCPUTotPIOWaitTime_Type = DisplayString
_KrCPUTotPIOWaitTime_Object = MibTableColumn
krCPUTotPIOWaitTime = _KrCPUTotPIOWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 9),
    _KrCPUTotPIOWaitTime_Type()
)
krCPUTotPIOWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUTotPIOWaitTime.setStatus("current")
_KrCPUNumOfIdleThreadSched_Type = Counter64
_KrCPUNumOfIdleThreadSched_Object = MibTableColumn
krCPUNumOfIdleThreadSched = _KrCPUNumOfIdleThreadSched_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1, 1, 1, 10),
    _KrCPUNumOfIdleThreadSched_Type()
)
krCPUNumOfIdleThreadSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krCPUNumOfIdleThreadSched.setStatus("current")
_KrCPUProcess_ObjectIdentity = ObjectIdentity
krCPUProcess = _KrCPUProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 2)
)
_KrTotProcInRunQueue_Type = Integer32
_KrTotProcInRunQueue_Object = MibScalar
krTotProcInRunQueue = _KrTotProcInRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 2, 1, 1),
    _KrTotProcInRunQueue_Type()
)
krTotProcInRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotProcInRunQueue.setStatus("current")
_KrTotProcBlocked_Type = Integer32
_KrTotProcBlocked_Object = MibScalar
krTotProcBlocked = _KrTotProcBlocked_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 2, 1, 2),
    _KrTotProcBlocked_Type()
)
krTotProcBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotProcBlocked.setStatus("current")
_KrTotProcReadyInSwap_Type = Integer32
_KrTotProcReadyInSwap_Object = MibScalar
krTotProcReadyInSwap = _KrTotProcReadyInSwap_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 2, 1, 3),
    _KrTotProcReadyInSwap_Type()
)
krTotProcReadyInSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotProcReadyInSwap.setStatus("current")
_KrTotNumberOfCPUs_Type = Integer32
_KrTotNumberOfCPUs_Object = MibScalar
krTotNumberOfCPUs = _KrTotNumberOfCPUs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 2, 1, 4),
    _KrTotNumberOfCPUs_Type()
)
krTotNumberOfCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotNumberOfCPUs.setStatus("current")
_KrCPUIOTable_Object = MibTable
krCPUIOTable = _KrCPUIOTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1)
)
if mibBuilder.loadTexts:
    krCPUIOTable.setStatus("current")
_KrCPUIOEntry_Object = MibTableRow
krCPUIOEntry = _KrCPUIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1)
)
krCPUIOEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krIOCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPUIOEntry.setStatus("current")


class _KrIOCPUInstance_Type(Integer32):
    """Custom type krIOCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrIOCPUInstance_Type.__name__ = "Integer32"
_KrIOCPUInstance_Object = MibTableColumn
krIOCPUInstance = _KrIOCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 1),
    _KrIOCPUInstance_Type()
)
krIOCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krIOCPUInstance.setStatus("current")
_KrNumPhyBlocksRead_Type = Counter64
_KrNumPhyBlocksRead_Object = MibTableColumn
krNumPhyBlocksRead = _KrNumPhyBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 2),
    _KrNumPhyBlocksRead_Type()
)
krNumPhyBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumPhyBlocksRead.setStatus("current")
_KrNumPhyBlocksWrite_Type = Counter64
_KrNumPhyBlocksWrite_Object = MibTableColumn
krNumPhyBlocksWrite = _KrNumPhyBlocksWrite_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 3),
    _KrNumPhyBlocksWrite_Type()
)
krNumPhyBlocksWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumPhyBlocksWrite.setStatus("current")
_KrNumLogBlocksRead_Type = Counter64
_KrNumLogBlocksRead_Object = MibTableColumn
krNumLogBlocksRead = _KrNumLogBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 4),
    _KrNumLogBlocksRead_Type()
)
krNumLogBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumLogBlocksRead.setStatus("current")
_KrNumLogBlocksWrite_Type = Counter64
_KrNumLogBlocksWrite_Object = MibTableColumn
krNumLogBlocksWrite = _KrNumLogBlocksWrite_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 5),
    _KrNumLogBlocksWrite_Type()
)
krNumLogBlocksWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumLogBlocksWrite.setStatus("current")
_KrNumRawIOReads_Type = Counter64
_KrNumRawIOReads_Object = MibTableColumn
krNumRawIOReads = _KrNumRawIOReads_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 6),
    _KrNumRawIOReads_Type()
)
krNumRawIOReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumRawIOReads.setStatus("current")
_KrNumRawIOWrites_Type = Counter64
_KrNumRawIOWrites_Object = MibTableColumn
krNumRawIOWrites = _KrNumRawIOWrites_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 7),
    _KrNumRawIOWrites_Type()
)
krNumRawIOWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumRawIOWrites.setStatus("current")
_KrNumBytesRead_Type = Counter64
_KrNumBytesRead_Object = MibTableColumn
krNumBytesRead = _KrNumBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 8),
    _KrNumBytesRead_Type()
)
krNumBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumBytesRead.setStatus("current")
_KrNumBytesWritten_Type = Counter64
_KrNumBytesWritten_Object = MibTableColumn
krNumBytesWritten = _KrNumBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 9),
    _KrNumBytesWritten_Type()
)
krNumBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumBytesWritten.setStatus("current")
_Krrcvint_Type = Counter64
_Krrcvint_Object = MibTableColumn
krrcvint = _Krrcvint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 10),
    _Krrcvint_Type()
)
krrcvint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krrcvint.setStatus("current")
_Krxmtint_Type = Counter64
_Krxmtint_Object = MibTableColumn
krxmtint = _Krxmtint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 11),
    _Krxmtint_Type()
)
krxmtint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krxmtint.setStatus("current")
_Krmdmint_Type = Counter64
_Krmdmint_Object = MibTableColumn
krmdmint = _Krmdmint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 12),
    _Krmdmint_Type()
)
krmdmint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krmdmint.setStatus("current")
_KrNumTermInputChars_Type = Counter64
_KrNumTermInputChars_Object = MibTableColumn
krNumTermInputChars = _KrNumTermInputChars_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 13),
    _KrNumTermInputChars_Type()
)
krNumTermInputChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumTermInputChars.setStatus("current")
_KrNumCanModeCharsHandled_Type = Counter64
_KrNumCanModeCharsHandled_Object = MibTableColumn
krNumCanModeCharsHandled = _KrNumCanModeCharsHandled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 14),
    _KrNumCanModeCharsHandled_Type()
)
krNumCanModeCharsHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumCanModeCharsHandled.setStatus("current")
_KrNumTermOutChars_Type = Counter64
_KrNumTermOutChars_Object = MibTableColumn
krNumTermOutChars = _KrNumTermOutChars_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 15),
    _KrNumTermOutChars_Type()
)
krNumTermOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumTermOutChars.setStatus("current")
_KrNumPhyBlocksAsyncWrite_Type = Counter64
_KrNumPhyBlocksAsyncWrite_Object = MibTableColumn
krNumPhyBlocksAsyncWrite = _KrNumPhyBlocksAsyncWrite_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 16),
    _KrNumPhyBlocksAsyncWrite_Type()
)
krNumPhyBlocksAsyncWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumPhyBlocksAsyncWrite.setStatus("current")
_Krphysio_Type = Counter64
_Krphysio_Object = MibTableColumn
krphysio = _Krphysio_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3, 1, 1, 17),
    _Krphysio_Type()
)
krphysio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krphysio.setStatus("current")
_KrCPUIntrTable_Object = MibTable
krCPUIntrTable = _KrCPUIntrTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1)
)
if mibBuilder.loadTexts:
    krCPUIntrTable.setStatus("current")
_KrCPUIntrEntry_Object = MibTableRow
krCPUIntrEntry = _KrCPUIntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1, 1)
)
krCPUIntrEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krIntrCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPUIntrEntry.setStatus("current")


class _KrIntrCPUInstance_Type(Integer32):
    """Custom type krIntrCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrIntrCPUInstance_Type.__name__ = "Integer32"
_KrIntrCPUInstance_Object = MibTableColumn
krIntrCPUInstance = _KrIntrCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1, 1, 1),
    _KrIntrCPUInstance_Type()
)
krIntrCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krIntrCPUInstance.setStatus("current")
_KrNumOfContextSwitches_Type = Counter64
_KrNumOfContextSwitches_Object = MibTableColumn
krNumOfContextSwitches = _KrNumOfContextSwitches_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1, 1, 2),
    _KrNumOfContextSwitches_Type()
)
krNumOfContextSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfContextSwitches.setStatus("current")
_KrNumberOfTraps_Type = Counter64
_KrNumberOfTraps_Object = MibTableColumn
krNumberOfTraps = _KrNumberOfTraps_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1, 1, 3),
    _KrNumberOfTraps_Type()
)
krNumberOfTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumberOfTraps.setStatus("current")
_KrNumberOfDevInterrupts_Type = Counter64
_KrNumberOfDevInterrupts_Object = MibTableColumn
krNumberOfDevInterrupts = _KrNumberOfDevInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1, 1, 4),
    _KrNumberOfDevInterrupts_Type()
)
krNumberOfDevInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumberOfDevInterrupts.setStatus("current")
_KrNumOfIntrThreads_Type = Counter64
_KrNumOfIntrThreads_Object = MibTableColumn
krNumOfIntrThreads = _KrNumOfIntrThreads_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1, 1, 5),
    _KrNumOfIntrThreads_Type()
)
krNumOfIntrThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfIntrThreads.setStatus("current")
_KrNumOfInterrupts_Type = Counter64
_KrNumOfInterrupts_Object = MibTableColumn
krNumOfInterrupts = _KrNumOfInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4, 1, 1, 6),
    _KrNumOfInterrupts_Type()
)
krNumOfInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfInterrupts.setStatus("current")
_KrCPUSysTable_Object = MibTable
krCPUSysTable = _KrCPUSysTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1)
)
if mibBuilder.loadTexts:
    krCPUSysTable.setStatus("current")
_KrCPUSysEntry_Object = MibTableRow
krCPUSysEntry = _KrCPUSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1)
)
krCPUSysEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSyscCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPUSysEntry.setStatus("current")


class _KrSyscCPUInstance_Type(Integer32):
    """Custom type krSyscCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrSyscCPUInstance_Type.__name__ = "Integer32"
_KrSyscCPUInstance_Object = MibTableColumn
krSyscCPUInstance = _KrSyscCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 1),
    _KrSyscCPUInstance_Type()
)
krSyscCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSyscCPUInstance.setStatus("current")
_KrNumOfSysCallsMade_Type = Counter64
_KrNumOfSysCallsMade_Object = MibTableColumn
krNumOfSysCallsMade = _KrNumOfSysCallsMade_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 2),
    _KrNumOfSysCallsMade_Type()
)
krNumOfSysCallsMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfSysCallsMade.setStatus("current")
_KrNumOfSysReads_Type = Counter64
_KrNumOfSysReads_Object = MibTableColumn
krNumOfSysReads = _KrNumOfSysReads_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 3),
    _KrNumOfSysReads_Type()
)
krNumOfSysReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfSysReads.setStatus("current")
_KrNumOfSysWrites_Type = Counter64
_KrNumOfSysWrites_Object = MibTableColumn
krNumOfSysWrites = _KrNumOfSysWrites_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 4),
    _KrNumOfSysWrites_Type()
)
krNumOfSysWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfSysWrites.setStatus("current")
_KrNumOfForksCalled_Type = Counter64
_KrNumOfForksCalled_Object = MibTableColumn
krNumOfForksCalled = _KrNumOfForksCalled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 5),
    _KrNumOfForksCalled_Type()
)
krNumOfForksCalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfForksCalled.setStatus("current")
_KrNumOfVForksCalled_Type = Counter64
_KrNumOfVForksCalled_Object = MibTableColumn
krNumOfVForksCalled = _KrNumOfVForksCalled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 6),
    _KrNumOfVForksCalled_Type()
)
krNumOfVForksCalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfVForksCalled.setStatus("current")
_KrNumOfExecsCalled_Type = Counter64
_KrNumOfExecsCalled_Object = MibTableColumn
krNumOfExecsCalled = _KrNumOfExecsCalled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 7),
    _KrNumOfExecsCalled_Type()
)
krNumOfExecsCalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfExecsCalled.setStatus("current")
_KrTotNumOfMessages_Type = Counter64
_KrTotNumOfMessages_Object = MibTableColumn
krTotNumOfMessages = _KrTotNumOfMessages_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 8),
    _KrTotNumOfMessages_Type()
)
krTotNumOfMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotNumOfMessages.setStatus("current")
_KrTotNumOfSemops_Type = Counter64
_KrTotNumOfSemops_Object = MibTableColumn
krTotNumOfSemops = _KrTotNumOfSemops_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 9),
    _KrTotNumOfSemops_Type()
)
krTotNumOfSemops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotNumOfSemops.setStatus("current")
_KrNumOfPnameLookup_Type = Counter64
_KrNumOfPnameLookup_Object = MibTableColumn
krNumOfPnameLookup = _KrNumOfPnameLookup_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 10),
    _KrNumOfPnameLookup_Type()
)
krNumOfPnameLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPnameLookup.setStatus("current")
_KrNumOfUfsigetcalls_Type = Counter64
_KrNumOfUfsigetcalls_Object = MibTableColumn
krNumOfUfsigetcalls = _KrNumOfUfsigetcalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 11),
    _KrNumOfUfsigetcalls_Type()
)
krNumOfUfsigetcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfUfsigetcalls.setStatus("current")
_KrNumOfDirBlocksRead_Type = Counter64
_KrNumOfDirBlocksRead_Object = MibTableColumn
krNumOfDirBlocksRead = _KrNumOfDirBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 12),
    _KrNumOfDirBlocksRead_Type()
)
krNumOfDirBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfDirBlocksRead.setStatus("current")
_KrNumOfInodesTakenWAP_Type = Counter64
_KrNumOfInodesTakenWAP_Object = MibTableColumn
krNumOfInodesTakenWAP = _KrNumOfInodesTakenWAP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 13),
    _KrNumOfInodesTakenWAP_Type()
)
krNumOfInodesTakenWAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfInodesTakenWAP.setStatus("current")
_KrNumOfInodesTakenWNAP_Type = Counter64
_KrNumOfInodesTakenWNAP_Object = MibTableColumn
krNumOfInodesTakenWNAP = _KrNumOfInodesTakenWNAP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 14),
    _KrNumOfInodesTakenWNAP_Type()
)
krNumOfInodesTakenWNAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfInodesTakenWNAP.setStatus("current")
_KrNumOfInodeTblOvrFlow_Type = Counter64
_KrNumOfInodeTblOvrFlow_Object = MibTableColumn
krNumOfInodeTblOvrFlow = _KrNumOfInodeTblOvrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 15),
    _KrNumOfInodeTblOvrFlow_Type()
)
krNumOfInodeTblOvrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfInodeTblOvrFlow.setStatus("current")
_KrNumOfFileTblOvrFlow_Type = Counter64
_KrNumOfFileTblOvrFlow_Object = MibTableColumn
krNumOfFileTblOvrFlow = _KrNumOfFileTblOvrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 16),
    _KrNumOfFileTblOvrFlow_Type()
)
krNumOfFileTblOvrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfFileTblOvrFlow.setStatus("current")
_KrNumOfProcTblOvrFlow_Type = Counter64
_KrNumOfProcTblOvrFlow_Object = MibTableColumn
krNumOfProcTblOvrFlow = _KrNumOfProcTblOvrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5, 1, 1, 17),
    _KrNumOfProcTblOvrFlow_Type()
)
krNumOfProcTblOvrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfProcTblOvrFlow.setStatus("current")
_KrCPUMiscTable_Object = MibTable
krCPUMiscTable = _KrCPUMiscTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1)
)
if mibBuilder.loadTexts:
    krCPUMiscTable.setStatus("current")
_KrCPUMiscEntry_Object = MibTableRow
krCPUMiscEntry = _KrCPUMiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1)
)
krCPUMiscEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krMiscCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPUMiscEntry.setStatus("current")


class _KrMiscCPUInstance_Type(Integer32):
    """Custom type krMiscCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrMiscCPUInstance_Type.__name__ = "Integer32"
_KrMiscCPUInstance_Object = MibTableColumn
krMiscCPUInstance = _KrMiscCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 1),
    _KrMiscCPUInstance_Type()
)
krMiscCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krMiscCPUInstance.setStatus("current")
_KrNumOfIvolCSwitches_Type = Counter64
_KrNumOfIvolCSwitches_Object = MibTableColumn
krNumOfIvolCSwitches = _KrNumOfIvolCSwitches_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 2),
    _KrNumOfIvolCSwitches_Type()
)
krNumOfIvolCSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfIvolCSwitches.setStatus("current")
_KrNumOfThrCreateCalls_Type = Counter64
_KrNumOfThrCreateCalls_Object = MibTableColumn
krNumOfThrCreateCalls = _KrNumOfThrCreateCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 3),
    _KrNumOfThrCreateCalls_Type()
)
krNumOfThrCreateCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfThrCreateCalls.setStatus("current")
_KrNumOfCPUMig_Type = Counter64
_KrNumOfCPUMig_Object = MibTableColumn
krNumOfCPUMig = _KrNumOfCPUMig_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 4),
    _KrNumOfCPUMig_Type()
)
krNumOfCPUMig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfCPUMig.setStatus("current")
_KrNumOfxcalls_Type = Counter64
_KrNumOfxcalls_Object = MibTableColumn
krNumOfxcalls = _KrNumOfxcalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 5),
    _KrNumOfxcalls_Type()
)
krNumOfxcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfxcalls.setStatus("current")
_KrNumOfFldMutxEntrs_Type = Counter64
_KrNumOfFldMutxEntrs_Object = MibTableColumn
krNumOfFldMutxEntrs = _KrNumOfFldMutxEntrs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 6),
    _KrNumOfFldMutxEntrs_Type()
)
krNumOfFldMutxEntrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfFldMutxEntrs.setStatus("current")
_KrNumOfRWReaderFails_Type = Counter64
_KrNumOfRWReaderFails_Object = MibTableColumn
krNumOfRWReaderFails = _KrNumOfRWReaderFails_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 7),
    _KrNumOfRWReaderFails_Type()
)
krNumOfRWReaderFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRWReaderFails.setStatus("current")
_KrNumOfRWWriterFails_Type = Counter64
_KrNumOfRWWriterFails_Object = MibTableColumn
krNumOfRWWriterFails = _KrNumOfRWWriterFails_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 8),
    _KrNumOfRWWriterFails_Type()
)
krNumOfRWWriterFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRWWriterFails.setStatus("current")
_KrNumOfModuleLoads_Type = Counter64
_KrNumOfModuleLoads_Object = MibTableColumn
krNumOfModuleLoads = _KrNumOfModuleLoads_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 9),
    _KrNumOfModuleLoads_Type()
)
krNumOfModuleLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfModuleLoads.setStatus("current")
_KrNumOfModuleUnloads_Type = Counter64
_KrNumOfModuleUnloads_Object = MibTableColumn
krNumOfModuleUnloads = _KrNumOfModuleUnloads_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 10),
    _KrNumOfModuleUnloads_Type()
)
krNumOfModuleUnloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfModuleUnloads.setStatus("current")
_KrNumOfRWLockTry_Type = Counter64
_KrNumOfRWLockTry_Object = MibTableColumn
krNumOfRWLockTry = _KrNumOfRWLockTry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6, 1, 1, 11),
    _KrNumOfRWLockTry_Type()
)
krNumOfRWLockTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRWLockTry.setStatus("current")
_KrCPURegTable_Object = MibTable
krCPURegTable = _KrCPURegTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1)
)
if mibBuilder.loadTexts:
    krCPURegTable.setStatus("current")
_KrCPURegEntry_Object = MibTableRow
krCPURegEntry = _KrCPURegEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1, 1)
)
krCPURegEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krRWCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPURegEntry.setStatus("current")


class _KrRWCPUInstance_Type(Integer32):
    """Custom type krRWCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrRWCPUInstance_Type.__name__ = "Integer32"
_KrRWCPUInstance_Object = MibTableColumn
krRWCPUInstance = _KrRWCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1, 1, 1),
    _KrRWCPUInstance_Type()
)
krRWCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krRWCPUInstance.setStatus("current")
_KrNumOfRegWinUsrOvrFlow_Type = Counter64
_KrNumOfRegWinUsrOvrFlow_Object = MibTableColumn
krNumOfRegWinUsrOvrFlow = _KrNumOfRegWinUsrOvrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1, 1, 2),
    _KrNumOfRegWinUsrOvrFlow_Type()
)
krNumOfRegWinUsrOvrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRegWinUsrOvrFlow.setStatus("current")
_KrNumOfRegWinUsrUndrFlow_Type = Counter64
_KrNumOfRegWinUsrUndrFlow_Object = MibTableColumn
krNumOfRegWinUsrUndrFlow = _KrNumOfRegWinUsrUndrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1, 1, 3),
    _KrNumOfRegWinUsrUndrFlow_Type()
)
krNumOfRegWinUsrUndrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRegWinUsrUndrFlow.setStatus("current")
_KrNumOfRegWinSysOvrFlow_Type = Counter64
_KrNumOfRegWinSysOvrFlow_Object = MibTableColumn
krNumOfRegWinSysOvrFlow = _KrNumOfRegWinSysOvrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1, 1, 4),
    _KrNumOfRegWinSysOvrFlow_Type()
)
krNumOfRegWinSysOvrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRegWinSysOvrFlow.setStatus("current")
_KrNumOfRegWinSysUndrFlow_Type = Counter64
_KrNumOfRegWinSysUndrFlow_Object = MibTableColumn
krNumOfRegWinSysUndrFlow = _KrNumOfRegWinSysUndrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1, 1, 5),
    _KrNumOfRegWinSysUndrFlow_Type()
)
krNumOfRegWinSysUndrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRegWinSysUndrFlow.setStatus("current")
_KrNumOfRegWinSysUsrOvrFlow_Type = Counter64
_KrNumOfRegWinSysUsrOvrFlow_Object = MibTableColumn
krNumOfRegWinSysUsrOvrFlow = _KrNumOfRegWinSysUsrOvrFlow_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7, 1, 1, 6),
    _KrNumOfRegWinSysUsrOvrFlow_Type()
)
krNumOfRegWinSysUsrOvrFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfRegWinSysUsrOvrFlow.setStatus("current")
_KrCPUPgTable_Object = MibTable
krCPUPgTable = _KrCPUPgTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1)
)
if mibBuilder.loadTexts:
    krCPUPgTable.setStatus("current")
_KrCPUPgEntry_Object = MibTableRow
krCPUPgEntry = _KrCPUPgEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1)
)
krCPUPgEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krPgCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPUPgEntry.setStatus("current")


class _KrPgCPUInstance_Type(Integer32):
    """Custom type krPgCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrPgCPUInstance_Type.__name__ = "Integer32"
_KrPgCPUInstance_Object = MibTableColumn
krPgCPUInstance = _KrPgCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 1),
    _KrPgCPUInstance_Type()
)
krPgCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krPgCPUInstance.setStatus("current")
_KrNumOfPageReclaims_Type = Counter64
_KrNumOfPageReclaims_Object = MibTableColumn
krNumOfPageReclaims = _KrNumOfPageReclaims_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 2),
    _KrNumOfPageReclaims_Type()
)
krNumOfPageReclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPageReclaims.setStatus("current")
_KrNumOfFreeListPgReclaims_Type = Counter64
_KrNumOfFreeListPgReclaims_Object = MibTableColumn
krNumOfFreeListPgReclaims = _KrNumOfFreeListPgReclaims_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 3),
    _KrNumOfFreeListPgReclaims_Type()
)
krNumOfFreeListPgReclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfFreeListPgReclaims.setStatus("current")
_KrNumOfPageIns_Type = Counter64
_KrNumOfPageIns_Object = MibTableColumn
krNumOfPageIns = _KrNumOfPageIns_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 4),
    _KrNumOfPageIns_Type()
)
krNumOfPageIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPageIns.setStatus("current")
_KrNumOfPgsPagedIn_Type = Counter64
_KrNumOfPgsPagedIn_Object = MibTableColumn
krNumOfPgsPagedIn = _KrNumOfPgsPagedIn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 5),
    _KrNumOfPgsPagedIn_Type()
)
krNumOfPgsPagedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPgsPagedIn.setStatus("current")
_KrNumOfPageOuts_Type = Counter64
_KrNumOfPageOuts_Object = MibTableColumn
krNumOfPageOuts = _KrNumOfPageOuts_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 6),
    _KrNumOfPageOuts_Type()
)
krNumOfPageOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPageOuts.setStatus("current")
_KrkrNumOfPgsPagedOut_Type = Counter64
_KrkrNumOfPgsPagedOut_Object = MibTableColumn
krkrNumOfPgsPagedOut = _KrkrNumOfPgsPagedOut_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 7),
    _KrkrNumOfPgsPagedOut_Type()
)
krkrNumOfPgsPagedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krkrNumOfPgsPagedOut.setStatus("current")
_KrNumOfSwapIns_Type = Counter64
_KrNumOfSwapIns_Object = MibTableColumn
krNumOfSwapIns = _KrNumOfSwapIns_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 8),
    _KrNumOfSwapIns_Type()
)
krNumOfSwapIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfSwapIns.setStatus("current")
_KrNumOfPgsSwappedIn_Type = Counter64
_KrNumOfPgsSwappedIn_Object = MibTableColumn
krNumOfPgsSwappedIn = _KrNumOfPgsSwappedIn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 9),
    _KrNumOfPgsSwappedIn_Type()
)
krNumOfPgsSwappedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPgsSwappedIn.setStatus("current")
_KrNumOfSwapOuts_Type = Counter64
_KrNumOfSwapOuts_Object = MibTableColumn
krNumOfSwapOuts = _KrNumOfSwapOuts_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 10),
    _KrNumOfSwapOuts_Type()
)
krNumOfSwapOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfSwapOuts.setStatus("current")
_KrNumOfPgsSwappedOut_Type = Counter64
_KrNumOfPgsSwappedOut_Object = MibTableColumn
krNumOfPgsSwappedOut = _KrNumOfPgsSwappedOut_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 11),
    _KrNumOfPgsSwappedOut_Type()
)
krNumOfPgsSwappedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPgsSwappedOut.setStatus("current")
_KrNumOfZeroFilledPages_Type = Counter64
_KrNumOfZeroFilledPages_Object = MibTableColumn
krNumOfZeroFilledPages = _KrNumOfZeroFilledPages_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 12),
    _KrNumOfZeroFilledPages_Type()
)
krNumOfZeroFilledPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfZeroFilledPages.setStatus("current")
_KrNumOfAutoFreedPages_Type = Counter64
_KrNumOfAutoFreedPages_Object = MibTableColumn
krNumOfAutoFreedPages = _KrNumOfAutoFreedPages_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 13),
    _KrNumOfAutoFreedPages_Type()
)
krNumOfAutoFreedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfAutoFreedPages.setStatus("current")
_KrNumberOfScanedPages_Type = Counter64
_KrNumberOfScanedPages_Object = MibTableColumn
krNumberOfScanedPages = _KrNumberOfScanedPages_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 14),
    _KrNumberOfScanedPages_Type()
)
krNumberOfScanedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumberOfScanedPages.setStatus("current")
_KrNumOfPDHandsRvln_Type = Counter64
_KrNumOfPDHandsRvln_Object = MibTableColumn
krNumOfPDHandsRvln = _KrNumOfPDHandsRvln_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 15),
    _KrNumOfPDHandsRvln_Type()
)
krNumOfPDHandsRvln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPDHandsRvln.setStatus("current")
_KrNumOfPagerRun_Type = Counter64
_KrNumOfPagerRun_Object = MibTableColumn
krNumOfPagerRun = _KrNumOfPagerRun_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8, 1, 1, 16),
    _KrNumOfPagerRun_Type()
)
krNumOfPagerRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfPagerRun.setStatus("current")
_KrCPUFaultTable_Object = MibTable
krCPUFaultTable = _KrCPUFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1)
)
if mibBuilder.loadTexts:
    krCPUFaultTable.setStatus("current")
_KrCPUFaultEntry_Object = MibTableRow
krCPUFaultEntry = _KrCPUFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1)
)
krCPUFaultEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krFaultCPUInstance"),
)
if mibBuilder.loadTexts:
    krCPUFaultEntry.setStatus("current")


class _KrFaultCPUInstance_Type(Integer32):
    """Custom type krFaultCPUInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_KrFaultCPUInstance_Type.__name__ = "Integer32"
_KrFaultCPUInstance_Object = MibTableColumn
krFaultCPUInstance = _KrFaultCPUInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 1),
    _KrFaultCPUInstance_Type()
)
krFaultCPUInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krFaultCPUInstance.setStatus("current")
_KrNumOfMinorHatPageFaults_Type = Counter64
_KrNumOfMinorHatPageFaults_Object = MibTableColumn
krNumOfMinorHatPageFaults = _KrNumOfMinorHatPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 2),
    _KrNumOfMinorHatPageFaults_Type()
)
krNumOfMinorHatPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfMinorHatPageFaults.setStatus("current")
_KrNumOfMinorAsPageFaults_Type = Counter64
_KrNumOfMinorAsPageFaults_Object = MibTableColumn
krNumOfMinorAsPageFaults = _KrNumOfMinorAsPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 3),
    _KrNumOfMinorAsPageFaults_Type()
)
krNumOfMinorAsPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfMinorAsPageFaults.setStatus("current")
_KrNumOfMajorPageFaults_Type = Counter64
_KrNumOfMajorPageFaults_Object = MibTableColumn
krNumOfMajorPageFaults = _KrNumOfMajorPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 4),
    _KrNumOfMajorPageFaults_Type()
)
krNumOfMajorPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfMajorPageFaults.setStatus("current")
_KrNumOfCopyOnWriteFaults_Type = Counter64
_KrNumOfCopyOnWriteFaults_Object = MibTableColumn
krNumOfCopyOnWriteFaults = _KrNumOfCopyOnWriteFaults_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 5),
    _KrNumOfCopyOnWriteFaults_Type()
)
krNumOfCopyOnWriteFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfCopyOnWriteFaults.setStatus("current")
_KrNumOfProtectionFaults_Type = Counter64
_KrNumOfProtectionFaults_Object = MibTableColumn
krNumOfProtectionFaults = _KrNumOfProtectionFaults_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 6),
    _KrNumOfProtectionFaults_Type()
)
krNumOfProtectionFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfProtectionFaults.setStatus("current")
_KrNumOfSWLockFaults_Type = Counter64
_KrNumOfSWLockFaults_Object = MibTableColumn
krNumOfSWLockFaults = _KrNumOfSWLockFaults_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 7),
    _KrNumOfSWLockFaults_Type()
)
krNumOfSWLockFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfSWLockFaults.setStatus("current")
_KrNumOfAsFaultsInKSpace_Type = Counter64
_KrNumOfAsFaultsInKSpace_Object = MibTableColumn
krNumOfAsFaultsInKSpace = _KrNumOfAsFaultsInKSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9, 1, 1, 8),
    _KrNumOfAsFaultsInKSpace_Type()
)
krNumOfAsFaultsInKSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krNumOfAsFaultsInKSpace.setStatus("current")
_KrOverAllCpuStatsUtil_Type = DisplayString
_KrOverAllCpuStatsUtil_Object = MibScalar
krOverAllCpuStatsUtil = _KrOverAllCpuStatsUtil_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 10, 1),
    _KrOverAllCpuStatsUtil_Type()
)
krOverAllCpuStatsUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krOverAllCpuStatsUtil.setStatus("current")
if mibBuilder.loadTexts:
    krOverAllCpuStatsUtil.setUnits("%")
_KrOverAllCpuStatsIdle_Type = DisplayString
_KrOverAllCpuStatsIdle_Object = MibScalar
krOverAllCpuStatsIdle = _KrOverAllCpuStatsIdle_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 10, 2),
    _KrOverAllCpuStatsIdle_Type()
)
krOverAllCpuStatsIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krOverAllCpuStatsIdle.setStatus("current")
if mibBuilder.loadTexts:
    krOverAllCpuStatsIdle.setUnits("%")
_KrTotPhyMemAvail_Type = Integer32
_KrTotPhyMemAvail_Object = MibScalar
krTotPhyMemAvail = _KrTotPhyMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 6, 1),
    _KrTotPhyMemAvail_Type()
)
krTotPhyMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotPhyMemAvail.setStatus("current")
if mibBuilder.loadTexts:
    krTotPhyMemAvail.setUnits("MB")
_KrPhyMemInUse_Type = Integer32
_KrPhyMemInUse_Object = MibScalar
krPhyMemInUse = _KrPhyMemInUse_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 6, 2),
    _KrPhyMemInUse_Type()
)
krPhyMemInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krPhyMemInUse.setStatus("current")
if mibBuilder.loadTexts:
    krPhyMemInUse.setUnits("MB")
_KrPctOfPhyMemInUse_Type = DisplayString
_KrPctOfPhyMemInUse_Object = MibScalar
krPctOfPhyMemInUse = _KrPctOfPhyMemInUse_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 6, 3),
    _KrPctOfPhyMemInUse_Type()
)
krPctOfPhyMemInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krPctOfPhyMemInUse.setStatus("current")
_KrFreePhyMem_Type = Integer32
_KrFreePhyMem_Object = MibScalar
krFreePhyMem = _KrFreePhyMem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 6, 4),
    _KrFreePhyMem_Type()
)
krFreePhyMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krFreePhyMem.setStatus("current")
if mibBuilder.loadTexts:
    krFreePhyMem.setUnits("MB")
_KrPctOfPhyMemFree_Type = DisplayString
_KrPctOfPhyMemFree_Object = MibScalar
krPctOfPhyMemFree = _KrPctOfPhyMemFree_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 6, 5),
    _KrPctOfPhyMemFree_Type()
)
krPctOfPhyMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krPctOfPhyMemFree.setStatus("current")
_KrTotSwapSpaceAvail_Type = Integer32
_KrTotSwapSpaceAvail_Object = MibScalar
krTotSwapSpaceAvail = _KrTotSwapSpaceAvail_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 7, 1),
    _KrTotSwapSpaceAvail_Type()
)
krTotSwapSpaceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSwapSpaceAvail.setStatus("current")
if mibBuilder.loadTexts:
    krTotSwapSpaceAvail.setUnits("Kilo Bytes")
_KrTotReservedSwapSpace_Type = Integer32
_KrTotReservedSwapSpace_Object = MibScalar
krTotReservedSwapSpace = _KrTotReservedSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 7, 2),
    _KrTotReservedSwapSpace_Type()
)
krTotReservedSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotReservedSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    krTotReservedSwapSpace.setUnits("Kilo Bytes")
_KrTotAllocatedSwapSpace_Type = Integer32
_KrTotAllocatedSwapSpace_Object = MibScalar
krTotAllocatedSwapSpace = _KrTotAllocatedSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 7, 3),
    _KrTotAllocatedSwapSpace_Type()
)
krTotAllocatedSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotAllocatedSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    krTotAllocatedSwapSpace.setUnits("Kilo Bytes")
_KrTotUsedSwapSpace_Type = Unsigned32
_KrTotUsedSwapSpace_Object = MibScalar
krTotUsedSwapSpace = _KrTotUsedSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 7, 4),
    _KrTotUsedSwapSpace_Type()
)
krTotUsedSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotUsedSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    krTotUsedSwapSpace.setUnits("Kilo Bytes")
_KrTotSwapSpace_Type = Integer32
_KrTotSwapSpace_Object = MibScalar
krTotSwapSpace = _KrTotSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 7, 5),
    _KrTotSwapSpace_Type()
)
krTotSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    krTotSwapSpace.setUnits("Kilo Bytes")
_KrTotPctOfSwapSpaceUsed_Type = DisplayString
_KrTotPctOfSwapSpaceUsed_Object = MibScalar
krTotPctOfSwapSpaceUsed = _KrTotPctOfSwapSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 7, 6),
    _KrTotPctOfSwapSpaceUsed_Type()
)
krTotPctOfSwapSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotPctOfSwapSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    krTotPctOfSwapSpaceUsed.setUnits("%")
_KrStreamsDetail_ObjectIdentity = ObjectIdentity
krStreamsDetail = _KrStreamsDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8)
)
_KrStrHeadCacheName_Type = DisplayString
_KrStrHeadCacheName_Object = MibScalar
krStrHeadCacheName = _KrStrHeadCacheName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 1, 1),
    _KrStrHeadCacheName_Type()
)
krStrHeadCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrHeadCacheName.setStatus("current")
_KrStrHeadCacheCurrUsage_Type = Integer32
_KrStrHeadCacheCurrUsage_Object = MibScalar
krStrHeadCacheCurrUsage = _KrStrHeadCacheCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 1, 2),
    _KrStrHeadCacheCurrUsage_Type()
)
krStrHeadCacheCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrHeadCacheCurrUsage.setStatus("current")
_KrStrHeadCacheSize_Type = Integer32
_KrStrHeadCacheSize_Object = MibScalar
krStrHeadCacheSize = _KrStrHeadCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 1, 3),
    _KrStrHeadCacheSize_Type()
)
krStrHeadCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrHeadCacheSize.setStatus("current")
_KrTotSHCacheAllocation_Type = Integer32
_KrTotSHCacheAllocation_Object = MibScalar
krTotSHCacheAllocation = _KrTotSHCacheAllocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 1, 4),
    _KrTotSHCacheAllocation_Type()
)
krTotSHCacheAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSHCacheAllocation.setStatus("current")
_KrTotSHAllocFailures_Type = Integer32
_KrTotSHAllocFailures_Object = MibScalar
krTotSHAllocFailures = _KrTotSHAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 1, 5),
    _KrTotSHAllocFailures_Type()
)
krTotSHAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSHAllocFailures.setStatus("current")
_KrStrHeadCachePctUsed_Type = DisplayString
_KrStrHeadCachePctUsed_Object = MibScalar
krStrHeadCachePctUsed = _KrStrHeadCachePctUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 1, 6),
    _KrStrHeadCachePctUsed_Type()
)
krStrHeadCachePctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrHeadCachePctUsed.setStatus("current")
_KrQueueCacheName_Type = DisplayString
_KrQueueCacheName_Object = MibScalar
krQueueCacheName = _KrQueueCacheName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 2, 1),
    _KrQueueCacheName_Type()
)
krQueueCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQueueCacheName.setStatus("current")
_KrQueueCacheCurrUsage_Type = Integer32
_KrQueueCacheCurrUsage_Object = MibScalar
krQueueCacheCurrUsage = _KrQueueCacheCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 2, 2),
    _KrQueueCacheCurrUsage_Type()
)
krQueueCacheCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQueueCacheCurrUsage.setStatus("current")
_KrQueueCacheSize_Type = Integer32
_KrQueueCacheSize_Object = MibScalar
krQueueCacheSize = _KrQueueCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 2, 3),
    _KrQueueCacheSize_Type()
)
krQueueCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQueueCacheSize.setStatus("current")
_KrTotQCacheAllocation_Type = Integer32
_KrTotQCacheAllocation_Object = MibScalar
krTotQCacheAllocation = _KrTotQCacheAllocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 2, 4),
    _KrTotQCacheAllocation_Type()
)
krTotQCacheAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotQCacheAllocation.setStatus("current")
_KrTotQAllocFailures_Type = Integer32
_KrTotQAllocFailures_Object = MibScalar
krTotQAllocFailures = _KrTotQAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 2, 5),
    _KrTotQAllocFailures_Type()
)
krTotQAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotQAllocFailures.setStatus("current")
_KrQueueCachePctUsed_Type = DisplayString
_KrQueueCachePctUsed_Object = MibScalar
krQueueCachePctUsed = _KrQueueCachePctUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 2, 6),
    _KrQueueCachePctUsed_Type()
)
krQueueCachePctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQueueCachePctUsed.setStatus("current")
_KrStrMsgCacheName_Type = DisplayString
_KrStrMsgCacheName_Object = MibScalar
krStrMsgCacheName = _KrStrMsgCacheName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 3, 1),
    _KrStrMsgCacheName_Type()
)
krStrMsgCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrMsgCacheName.setStatus("current")
_KrStrMsgCacheCurrUsage_Type = Integer32
_KrStrMsgCacheCurrUsage_Object = MibScalar
krStrMsgCacheCurrUsage = _KrStrMsgCacheCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 3, 2),
    _KrStrMsgCacheCurrUsage_Type()
)
krStrMsgCacheCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrMsgCacheCurrUsage.setStatus("current")
_KrStrMsgCacheSize_Type = Integer32
_KrStrMsgCacheSize_Object = MibScalar
krStrMsgCacheSize = _KrStrMsgCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 3, 3),
    _KrStrMsgCacheSize_Type()
)
krStrMsgCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrMsgCacheSize.setStatus("current")
_KrTotSMCacheAllocation_Type = Integer32
_KrTotSMCacheAllocation_Object = MibScalar
krTotSMCacheAllocation = _KrTotSMCacheAllocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 3, 4),
    _KrTotSMCacheAllocation_Type()
)
krTotSMCacheAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSMCacheAllocation.setStatus("current")
_KrTotSMAllocFailures_Type = Integer32
_KrTotSMAllocFailures_Object = MibScalar
krTotSMAllocFailures = _KrTotSMAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 3, 5),
    _KrTotSMAllocFailures_Type()
)
krTotSMAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSMAllocFailures.setStatus("current")
_KrStrMsgCachePctUsed_Type = DisplayString
_KrStrMsgCachePctUsed_Object = MibScalar
krStrMsgCachePctUsed = _KrStrMsgCachePctUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 3, 6),
    _KrStrMsgCachePctUsed_Type()
)
krStrMsgCachePctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrMsgCachePctUsed.setStatus("current")
_KrLinkinfoCacheName_Type = DisplayString
_KrLinkinfoCacheName_Object = MibScalar
krLinkinfoCacheName = _KrLinkinfoCacheName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 4, 1),
    _KrLinkinfoCacheName_Type()
)
krLinkinfoCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krLinkinfoCacheName.setStatus("current")
_KrLinkinfoCacheCurrUsage_Type = Integer32
_KrLinkinfoCacheCurrUsage_Object = MibScalar
krLinkinfoCacheCurrUsage = _KrLinkinfoCacheCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 4, 2),
    _KrLinkinfoCacheCurrUsage_Type()
)
krLinkinfoCacheCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krLinkinfoCacheCurrUsage.setStatus("current")
_KrLinkinfoCacheSize_Type = Integer32
_KrLinkinfoCacheSize_Object = MibScalar
krLinkinfoCacheSize = _KrLinkinfoCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 4, 3),
    _KrLinkinfoCacheSize_Type()
)
krLinkinfoCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krLinkinfoCacheSize.setStatus("current")
_KrTotLICacheAllocation_Type = Integer32
_KrTotLICacheAllocation_Object = MibScalar
krTotLICacheAllocation = _KrTotLICacheAllocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 4, 4),
    _KrTotLICacheAllocation_Type()
)
krTotLICacheAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotLICacheAllocation.setStatus("current")
_KrTotLIAllocFailures_Type = Integer32
_KrTotLIAllocFailures_Object = MibScalar
krTotLIAllocFailures = _KrTotLIAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 4, 5),
    _KrTotLIAllocFailures_Type()
)
krTotLIAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotLIAllocFailures.setStatus("current")
_KrLinkinfoCachePctUsed_Type = DisplayString
_KrLinkinfoCachePctUsed_Object = MibScalar
krLinkinfoCachePctUsed = _KrLinkinfoCachePctUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 4, 6),
    _KrLinkinfoCachePctUsed_Type()
)
krLinkinfoCachePctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krLinkinfoCachePctUsed.setStatus("current")
_KrStrEventCacheName_Type = DisplayString
_KrStrEventCacheName_Object = MibScalar
krStrEventCacheName = _KrStrEventCacheName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 5, 1),
    _KrStrEventCacheName_Type()
)
krStrEventCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrEventCacheName.setStatus("current")
_KrStrEventCacheCurrUsage_Type = Integer32
_KrStrEventCacheCurrUsage_Object = MibScalar
krStrEventCacheCurrUsage = _KrStrEventCacheCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 5, 2),
    _KrStrEventCacheCurrUsage_Type()
)
krStrEventCacheCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrEventCacheCurrUsage.setStatus("current")
_KrStrEventCacheSize_Type = Integer32
_KrStrEventCacheSize_Object = MibScalar
krStrEventCacheSize = _KrStrEventCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 5, 3),
    _KrStrEventCacheSize_Type()
)
krStrEventCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrEventCacheSize.setStatus("current")
_KrTotSECacheAllocation_Type = Integer32
_KrTotSECacheAllocation_Object = MibScalar
krTotSECacheAllocation = _KrTotSECacheAllocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 5, 4),
    _KrTotSECacheAllocation_Type()
)
krTotSECacheAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSECacheAllocation.setStatus("current")
_KrTotSEAllocFailures_Type = Integer32
_KrTotSEAllocFailures_Object = MibScalar
krTotSEAllocFailures = _KrTotSEAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 5, 5),
    _KrTotSEAllocFailures_Type()
)
krTotSEAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSEAllocFailures.setStatus("current")
_KrStrEventCachePctUsed_Type = DisplayString
_KrStrEventCachePctUsed_Object = MibScalar
krStrEventCachePctUsed = _KrStrEventCachePctUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 5, 6),
    _KrStrEventCachePctUsed_Type()
)
krStrEventCachePctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStrEventCachePctUsed.setStatus("current")
_KrSyncCacheName_Type = DisplayString
_KrSyncCacheName_Object = MibScalar
krSyncCacheName = _KrSyncCacheName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 6, 1),
    _KrSyncCacheName_Type()
)
krSyncCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSyncCacheName.setStatus("current")
_KrSyncCacheCurrUsage_Type = Integer32
_KrSyncCacheCurrUsage_Object = MibScalar
krSyncCacheCurrUsage = _KrSyncCacheCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 6, 2),
    _KrSyncCacheCurrUsage_Type()
)
krSyncCacheCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSyncCacheCurrUsage.setStatus("current")
_KrSyncCacheSize_Type = Integer32
_KrSyncCacheSize_Object = MibScalar
krSyncCacheSize = _KrSyncCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 6, 3),
    _KrSyncCacheSize_Type()
)
krSyncCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSyncCacheSize.setStatus("current")
_KrTotSyCacheAllocation_Type = Integer32
_KrTotSyCacheAllocation_Object = MibScalar
krTotSyCacheAllocation = _KrTotSyCacheAllocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 6, 4),
    _KrTotSyCacheAllocation_Type()
)
krTotSyCacheAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSyCacheAllocation.setStatus("current")
_KrTotSyAllocFailures_Type = Integer32
_KrTotSyAllocFailures_Object = MibScalar
krTotSyAllocFailures = _KrTotSyAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 6, 5),
    _KrTotSyAllocFailures_Type()
)
krTotSyAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotSyAllocFailures.setStatus("current")
_KrSyncCachePctUsed_Type = DisplayString
_KrSyncCachePctUsed_Object = MibScalar
krSyncCachePctUsed = _KrSyncCachePctUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 6, 6),
    _KrSyncCachePctUsed_Type()
)
krSyncCachePctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSyncCachePctUsed.setStatus("current")
_KrQbandCacheName_Type = DisplayString
_KrQbandCacheName_Object = MibScalar
krQbandCacheName = _KrQbandCacheName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 7, 1),
    _KrQbandCacheName_Type()
)
krQbandCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQbandCacheName.setStatus("current")
_KrQbandCacheCurrUsage_Type = Integer32
_KrQbandCacheCurrUsage_Object = MibScalar
krQbandCacheCurrUsage = _KrQbandCacheCurrUsage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 7, 2),
    _KrQbandCacheCurrUsage_Type()
)
krQbandCacheCurrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQbandCacheCurrUsage.setStatus("current")
_KrQbandCacheSize_Type = Integer32
_KrQbandCacheSize_Object = MibScalar
krQbandCacheSize = _KrQbandCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 7, 3),
    _KrQbandCacheSize_Type()
)
krQbandCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQbandCacheSize.setStatus("current")
_KrTotQBCacheAllocation_Type = Integer32
_KrTotQBCacheAllocation_Object = MibScalar
krTotQBCacheAllocation = _KrTotQBCacheAllocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 7, 4),
    _KrTotQBCacheAllocation_Type()
)
krTotQBCacheAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotQBCacheAllocation.setStatus("current")
_KrTotQBAllocFailures_Type = Integer32
_KrTotQBAllocFailures_Object = MibScalar
krTotQBAllocFailures = _KrTotQBAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 7, 5),
    _KrTotQBAllocFailures_Type()
)
krTotQBAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTotQBAllocFailures.setStatus("current")
_KrQbandCachePctUsed_Type = DisplayString
_KrQbandCachePctUsed_Object = MibScalar
krQbandCachePctUsed = _KrQbandCachePctUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 7, 6),
    _KrQbandCachePctUsed_Type()
)
krQbandCachePctUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krQbandCachePctUsed.setStatus("current")
_KrDeviceErrorTable_Object = MibTable
krDeviceErrorTable = _KrDeviceErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 1)
)
if mibBuilder.loadTexts:
    krDeviceErrorTable.setStatus("current")
_KrDeviceErrorEntry_Object = MibTableRow
krDeviceErrorEntry = _KrDeviceErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 1, 1)
)
krDeviceErrorEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDevDevice"),
)
if mibBuilder.loadTexts:
    krDeviceErrorEntry.setStatus("current")
_KrDevDevice_Type = DisplayString
_KrDevDevice_Object = MibTableColumn
krDevDevice = _KrDevDevice_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 1, 1, 1),
    _KrDevDevice_Type()
)
krDevDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDevDevice.setStatus("current")
_KrDevSoftwareErrors_Type = Integer32
_KrDevSoftwareErrors_Object = MibTableColumn
krDevSoftwareErrors = _KrDevSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 1, 1, 2),
    _KrDevSoftwareErrors_Type()
)
krDevSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDevSoftwareErrors.setStatus("current")
_KrDevHardwareErrors_Type = Integer32
_KrDevHardwareErrors_Object = MibTableColumn
krDevHardwareErrors = _KrDevHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 1, 1, 3),
    _KrDevHardwareErrors_Type()
)
krDevHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDevHardwareErrors.setStatus("current")
_KrDevTransportErrors_Type = Integer32
_KrDevTransportErrors_Object = MibTableColumn
krDevTransportErrors = _KrDevTransportErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 1, 1, 4),
    _KrDevTransportErrors_Type()
)
krDevTransportErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDevTransportErrors.setStatus("current")
_KrDevTotalErrors_Type = Integer32
_KrDevTotalErrors_Object = MibTableColumn
krDevTotalErrors = _KrDevTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 1, 1, 5),
    _KrDevTotalErrors_Type()
)
krDevTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krDevTotalErrors.setStatus("current")
_KrTapeErrorTable_Object = MibTable
krTapeErrorTable = _KrTapeErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 2)
)
if mibBuilder.loadTexts:
    krTapeErrorTable.setStatus("current")
_KrTapeErrorEntry_Object = MibTableRow
krTapeErrorEntry = _KrTapeErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 2, 1)
)
krTapeErrorEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTapeDevice"),
)
if mibBuilder.loadTexts:
    krTapeErrorEntry.setStatus("current")
_KrTapeDevice_Type = DisplayString
_KrTapeDevice_Object = MibTableColumn
krTapeDevice = _KrTapeDevice_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 2, 1, 1),
    _KrTapeDevice_Type()
)
krTapeDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTapeDevice.setStatus("current")
_KrTapeSoftwareErrors_Type = Integer32
_KrTapeSoftwareErrors_Object = MibTableColumn
krTapeSoftwareErrors = _KrTapeSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 2, 1, 2),
    _KrTapeSoftwareErrors_Type()
)
krTapeSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTapeSoftwareErrors.setStatus("current")
_KrTapeHardwareErrors_Type = Integer32
_KrTapeHardwareErrors_Object = MibTableColumn
krTapeHardwareErrors = _KrTapeHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 2, 1, 3),
    _KrTapeHardwareErrors_Type()
)
krTapeHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTapeHardwareErrors.setStatus("current")
_KrTapeTransportErrors_Type = Integer32
_KrTapeTransportErrors_Object = MibTableColumn
krTapeTransportErrors = _KrTapeTransportErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 2, 1, 4),
    _KrTapeTransportErrors_Type()
)
krTapeTransportErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTapeTransportErrors.setStatus("current")
_KrTapeTotalErrors_Type = Integer32
_KrTapeTotalErrors_Object = MibTableColumn
krTapeTotalErrors = _KrTapeTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9, 2, 1, 5),
    _KrTapeTotalErrors_Type()
)
krTapeTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krTapeTotalErrors.setStatus("current")
_KrSmallPoolMem_Type = Integer32
_KrSmallPoolMem_Object = MibScalar
krSmallPoolMem = _KrSmallPoolMem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 1),
    _KrSmallPoolMem_Type()
)
krSmallPoolMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSmallPoolMem.setStatus("current")
_KrSmallPoolMemAllocated_Type = Integer32
_KrSmallPoolMemAllocated_Object = MibScalar
krSmallPoolMemAllocated = _KrSmallPoolMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 2),
    _KrSmallPoolMemAllocated_Type()
)
krSmallPoolMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSmallPoolMemAllocated.setStatus("current")
_KrSmallPoolMemFailed_Type = Integer32
_KrSmallPoolMemFailed_Object = MibScalar
krSmallPoolMemFailed = _KrSmallPoolMemFailed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 3),
    _KrSmallPoolMemFailed_Type()
)
krSmallPoolMemFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krSmallPoolMemFailed.setStatus("current")
_KrLargePoolMem_Type = Integer32
_KrLargePoolMem_Object = MibScalar
krLargePoolMem = _KrLargePoolMem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 4),
    _KrLargePoolMem_Type()
)
krLargePoolMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krLargePoolMem.setStatus("current")
_KrLargePoolMemAllocated_Type = Integer32
_KrLargePoolMemAllocated_Object = MibScalar
krLargePoolMemAllocated = _KrLargePoolMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 5),
    _KrLargePoolMemAllocated_Type()
)
krLargePoolMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krLargePoolMemAllocated.setStatus("current")
_KrLargePoolMemFailed_Type = Integer32
_KrLargePoolMemFailed_Object = MibScalar
krLargePoolMemFailed = _KrLargePoolMemFailed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 6),
    _KrLargePoolMemFailed_Type()
)
krLargePoolMemFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krLargePoolMemFailed.setStatus("current")
_KrOversizeMem_Type = Integer32
_KrOversizeMem_Object = MibScalar
krOversizeMem = _KrOversizeMem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 7),
    _KrOversizeMem_Type()
)
krOversizeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krOversizeMem.setStatus("current")
_KrOversizeMemFailed_Type = Integer32
_KrOversizeMemFailed_Object = MibScalar
krOversizeMemFailed = _KrOversizeMemFailed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10, 8),
    _KrOversizeMemFailed_Type()
)
krOversizeMemFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krOversizeMemFailed.setStatus("current")
_KrZoneListTable_Object = MibTable
krZoneListTable = _KrZoneListTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1)
)
if mibBuilder.loadTexts:
    krZoneListTable.setStatus("current")
_KrZoneListEntry_Object = MibTableRow
krZoneListEntry = _KrZoneListEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1, 1)
)
krZoneListEntry.setIndexNames(
    (0, "KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krZoneName"),
)
if mibBuilder.loadTexts:
    krZoneListEntry.setStatus("current")
_KrZoneId_Type = DisplayString
_KrZoneId_Object = MibTableColumn
krZoneId = _KrZoneId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1, 1, 1),
    _KrZoneId_Type()
)
krZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krZoneId.setStatus("current")
_KrZoneName_Type = DisplayString
_KrZoneName_Object = MibTableColumn
krZoneName = _KrZoneName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1, 1, 2),
    _KrZoneName_Type()
)
krZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krZoneName.setStatus("current")
_KrStatus_Type = DisplayString
_KrStatus_Object = MibTableColumn
krStatus = _KrStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1, 1, 3),
    _KrStatus_Type()
)
krStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krStatus.setStatus("current")
_KrPath_Type = DisplayString
_KrPath_Object = MibTableColumn
krPath = _KrPath_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1, 1, 4),
    _KrPath_Type()
)
krPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krPath.setStatus("current")
_KrIp_Type = DisplayString
_KrIp_Object = MibTableColumn
krIp = _KrIp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1, 1, 5),
    _KrIp_Type()
)
krIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krIp.setStatus("current")
_KrAutoboot_Type = DisplayString
_KrAutoboot_Object = MibTableColumn
krAutoboot = _KrAutoboot_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14, 1, 1, 6),
    _KrAutoboot_Type()
)
krAutoboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    krAutoboot.setStatus("current")

# Managed Objects groups

krUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 1)
)
krUserGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krConsoleUser"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotNumOfUsers"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotNumOfSessions"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krPrimaryUser"))
)
if mibBuilder.loadTexts:
    krUserGroup.setStatus("current")

krLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 2)
)
krLoadGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSystemLoadAvg1min"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSystemLoadAvg5min"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSystemLoadAvg15min"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSystemUpTime"))
)
if mibBuilder.loadTexts:
    krLoadGroup.setStatus("current")

krDiskDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 1)
)
krDiskDetailGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDDDiskName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskAliasName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskReadOpRate"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskWriteOpRate"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskOperationRate"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskDataReadRate"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskDataWriteRate"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskDataTransferRate"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskAvgWaitTrans"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskAvgRunTrans"))
)
if mibBuilder.loadTexts:
    krDiskDetailGroup.setStatus("current")

krDiskSrvcTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 3, 2)
)
krDiskSrvcTimeGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDSDiskName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskSrvcWaitPctTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskBusyPctTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskSrvcAvgWaitTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskSrvcAvgTransRunTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDiskSrvcAvgTransTime"))
)
if mibBuilder.loadTexts:
    krDiskSrvcTimeGroup.setStatus("current")

krUFSFileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 1)
)
krUFSFileSystemGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemIndex"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemMountPoint"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemDiskName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemFreeSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFreeSpaceForNonSU"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemPctUsedSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSTotNumOfInodes"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSTotNumOfInodesAvail"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSPctInodesUsed"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemSize64"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFileSystemFreeSpace64"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krUFSFreeSpaceForNonSU64"))
)
if mibBuilder.loadTexts:
    krUFSFileSystemGroup.setStatus("current")

krVXFSFileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 4, 2)
)
krVXFSFileSystemGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemIndex"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemMountPoint"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemDiskName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemFreeSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFreeSpaceForNonSU"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemPctUsedSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSTotNumOfInodes"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSTotNumOfInodesAvail"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSPctInodesUsed"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemSize64"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFileSystemFreeSpace64"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krVXFSFreeSpaceForNonSU64"))
)
if mibBuilder.loadTexts:
    krVXFSFileSystemGroup.setStatus("current")

krCPUUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 1)
)
krCPUUtilGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUDelta"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUIdleTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUUserModeTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUKernelModeTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUTotWaitTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUTotIOWaitTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUTotSwapWaitTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUTotPIOWaitTime"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krCPUNumOfIdleThreadSched"))
)
if mibBuilder.loadTexts:
    krCPUUtilGroup.setStatus("current")

krCPUProcInStatesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 2, 1)
)
krCPUProcInStatesGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotProcInRunQueue"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotProcBlocked"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotProcReadyInSwap"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotNumberOfCPUs"))
)
if mibBuilder.loadTexts:
    krCPUProcInStatesGroup.setStatus("current")

krCPUIOGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 3)
)
krCPUIOGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krIOCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumPhyBlocksRead"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumPhyBlocksWrite"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumLogBlocksRead"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumLogBlocksWrite"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumRawIOReads"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumRawIOWrites"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumBytesRead"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumBytesWritten"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krrcvint"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krxmtint"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krmdmint"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumTermInputChars"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumCanModeCharsHandled"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumTermOutChars"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumPhyBlocksAsyncWrite"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krphysio"))
)
if mibBuilder.loadTexts:
    krCPUIOGroup.setStatus("current")

krCPUInterruptsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 4)
)
krCPUInterruptsGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krIntrCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfContextSwitches"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumberOfTraps"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumberOfDevInterrupts"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfIntrThreads"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfInterrupts"))
)
if mibBuilder.loadTexts:
    krCPUInterruptsGroup.setStatus("current")

krCPUSyscallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 5)
)
krCPUSyscallGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSyscCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfSysCallsMade"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfSysReads"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfSysWrites"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfForksCalled"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfVForksCalled"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfExecsCalled"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotNumOfMessages"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotNumOfSemops"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPnameLookup"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfUfsigetcalls"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfDirBlocksRead"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfInodesTakenWAP"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfInodesTakenWNAP"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfInodeTblOvrFlow"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfFileTblOvrFlow"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfProcTblOvrFlow"))
)
if mibBuilder.loadTexts:
    krCPUSyscallGroup.setStatus("current")

krCPUMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 6)
)
krCPUMiscGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krMiscCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfIvolCSwitches"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfThrCreateCalls"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfCPUMig"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfxcalls"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfFldMutxEntrs"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRWReaderFails"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRWWriterFails"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfModuleLoads"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfModuleUnloads"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRWLockTry"))
)
if mibBuilder.loadTexts:
    krCPUMiscGroup.setStatus("current")

krCPURegWindowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 7)
)
krCPURegWindowGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krRWCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRegWinUsrOvrFlow"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRegWinUsrUndrFlow"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRegWinSysOvrFlow"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRegWinSysUndrFlow"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfRegWinSysUsrOvrFlow"))
)
if mibBuilder.loadTexts:
    krCPURegWindowGroup.setStatus("current")

krCPUPginfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 8)
)
krCPUPginfoGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krPgCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPageReclaims"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfFreeListPgReclaims"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPageIns"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPgsPagedIn"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPageOuts"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krkrNumOfPgsPagedOut"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfSwapIns"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPgsSwappedIn"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfSwapOuts"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPgsSwappedOut"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfZeroFilledPages"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfAutoFreedPages"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumberOfScanedPages"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPDHandsRvln"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfPagerRun"))
)
if mibBuilder.loadTexts:
    krCPUPginfoGroup.setStatus("current")

krCPUFaultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 9)
)
krCPUFaultsGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krFaultCPUInstance"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfMinorHatPageFaults"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfMinorAsPageFaults"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfMajorPageFaults"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfCopyOnWriteFaults"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfProtectionFaults"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfSWLockFaults"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krNumOfAsFaultsInKSpace"))
)
if mibBuilder.loadTexts:
    krCPUFaultsGroup.setStatus("current")

krOverAllCPUStatistics = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 5, 10)
)
krOverAllCPUStatistics.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krOverAllCpuStatsUtil"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krOverAllCpuStatsIdle"))
)
if mibBuilder.loadTexts:
    krOverAllCPUStatistics.setStatus("current")

krMemoryUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 6)
)
krMemoryUsageGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotPhyMemAvail"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krPhyMemInUse"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krPctOfPhyMemInUse"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krFreePhyMem"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krPctOfPhyMemFree"))
)
if mibBuilder.loadTexts:
    krMemoryUsageGroup.setStatus("current")

krSwapDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 7)
)
krSwapDetailGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSwapSpaceAvail"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotReservedSwapSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotAllocatedSwapSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotUsedSwapSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSwapSpace"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotPctOfSwapSpaceUsed"))
)
if mibBuilder.loadTexts:
    krSwapDetailGroup.setStatus("current")

krStreamHeadCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 1)
)
krStreamHeadCacheGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrHeadCacheName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrHeadCacheCurrUsage"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrHeadCacheSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSHCacheAllocation"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSHAllocFailures"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrHeadCachePctUsed"))
)
if mibBuilder.loadTexts:
    krStreamHeadCacheGroup.setStatus("current")

krQueueCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 2)
)
krQueueCacheGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQueueCacheName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQueueCacheCurrUsage"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQueueCacheSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotQCacheAllocation"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotQAllocFailures"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQueueCachePctUsed"))
)
if mibBuilder.loadTexts:
    krQueueCacheGroup.setStatus("current")

krStreamsMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 3)
)
krStreamsMsgGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrMsgCacheName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrMsgCacheCurrUsage"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrMsgCacheSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSMCacheAllocation"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSMAllocFailures"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrMsgCachePctUsed"))
)
if mibBuilder.loadTexts:
    krStreamsMsgGroup.setStatus("current")

krLinkinfoCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 4)
)
krLinkinfoCacheGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krLinkinfoCacheName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krLinkinfoCacheCurrUsage"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krLinkinfoCacheSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotLICacheAllocation"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotLIAllocFailures"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krLinkinfoCachePctUsed"))
)
if mibBuilder.loadTexts:
    krLinkinfoCacheGroup.setStatus("current")

krStreventCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 5)
)
krStreventCacheGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrEventCacheName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrEventCacheCurrUsage"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrEventCacheSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSECacheAllocation"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSEAllocFailures"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStrEventCachePctUsed"))
)
if mibBuilder.loadTexts:
    krStreventCacheGroup.setStatus("current")

krSyncqCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 6)
)
krSyncqCacheGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSyncCacheName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSyncCacheCurrUsage"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSyncCacheSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSyCacheAllocation"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotSyAllocFailures"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSyncCachePctUsed"))
)
if mibBuilder.loadTexts:
    krSyncqCacheGroup.setStatus("current")

krQbandCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 8, 7)
)
krQbandCacheGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQbandCacheName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQbandCacheCurrUsage"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQbandCacheSize"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotQBCacheAllocation"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTotQBAllocFailures"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krQbandCachePctUsed"))
)
if mibBuilder.loadTexts:
    krQbandCacheGroup.setStatus("current")

krIOErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 9)
)
krIOErrorStatsGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDevDevice"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDevSoftwareErrors"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDevHardwareErrors"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDevTransportErrors"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krDevTotalErrors"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTapeDevice"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTapeSoftwareErrors"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTapeHardwareErrors"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTapeTransportErrors"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krTapeTotalErrors"))
)
if mibBuilder.loadTexts:
    krIOErrorStatsGroup.setStatus("current")

krKernelMemAllocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 10)
)
krKernelMemAllocGroup.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSmallPoolMem"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSmallPoolMemAllocated"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krSmallPoolMemFailed"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krLargePoolMem"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krLargePoolMemAllocated"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krLargePoolMemFailed"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krOversizeMem"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krOversizeMemFailed"))
)
if mibBuilder.loadTexts:
    krKernelMemAllocGroup.setStatus("current")

krZoneList = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12, 14)
)
krZoneList.setObjects(
      *(("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krZoneId"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krZoneName"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krStatus"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krPath"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krIp"),
        ("KERNEL-READER-SUNMANAGEMENTCENTER-MIB", "krAutoboot"))
)
if mibBuilder.loadTexts:
    krZoneList.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KERNEL-READER-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "modules": modules,
       "kernelReader": kernelReader,
       "krUserGroup": krUserGroup,
       "krConsoleUser": krConsoleUser,
       "krTotNumOfUsers": krTotNumOfUsers,
       "krTotNumOfSessions": krTotNumOfSessions,
       "krPrimaryUser": krPrimaryUser,
       "krLoadGroup": krLoadGroup,
       "krSystemLoadAvg1min": krSystemLoadAvg1min,
       "krSystemLoadAvg5min": krSystemLoadAvg5min,
       "krSystemLoadAvg15min": krSystemLoadAvg15min,
       "krSystemUpTime": krSystemUpTime,
       "krDisk": krDisk,
       "krDiskDetailGroup": krDiskDetailGroup,
       "krDiskDetailTable": krDiskDetailTable,
       "krDiskDetailEntry": krDiskDetailEntry,
       "krDDDiskName": krDDDiskName,
       "krDiskAliasName": krDiskAliasName,
       "krDiskReadOpRate": krDiskReadOpRate,
       "krDiskWriteOpRate": krDiskWriteOpRate,
       "krDiskOperationRate": krDiskOperationRate,
       "krDiskDataReadRate": krDiskDataReadRate,
       "krDiskDataWriteRate": krDiskDataWriteRate,
       "krDiskDataTransferRate": krDiskDataTransferRate,
       "krDiskAvgWaitTrans": krDiskAvgWaitTrans,
       "krDiskAvgRunTrans": krDiskAvgRunTrans,
       "krDiskSrvcTimeGroup": krDiskSrvcTimeGroup,
       "krDiskSrvTable": krDiskSrvTable,
       "krDiskSrvEntry": krDiskSrvEntry,
       "krDSDiskName": krDSDiskName,
       "krDiskSrvcWaitPctTime": krDiskSrvcWaitPctTime,
       "krDiskBusyPctTime": krDiskBusyPctTime,
       "krDiskSrvcAvgWaitTime": krDiskSrvcAvgWaitTime,
       "krDiskSrvcAvgTransRunTime": krDiskSrvcAvgTransRunTime,
       "krDiskSrvcAvgTransTime": krDiskSrvcAvgTransTime,
       "krFileSystem": krFileSystem,
       "krUFSFileSystemGroup": krUFSFileSystemGroup,
       "krUFSFileTable": krUFSFileTable,
       "krUFSFileEntry": krUFSFileEntry,
       "krUFSFileSystemIndex": krUFSFileSystemIndex,
       "krUFSFileSystemMountPoint": krUFSFileSystemMountPoint,
       "krUFSFileSystemDiskName": krUFSFileSystemDiskName,
       "krUFSFileSystemSize": krUFSFileSystemSize,
       "krUFSFileSystemFreeSpace": krUFSFileSystemFreeSpace,
       "krUFSFreeSpaceForNonSU": krUFSFreeSpaceForNonSU,
       "krUFSFileSystemPctUsedSpace": krUFSFileSystemPctUsedSpace,
       "krUFSTotNumOfInodes": krUFSTotNumOfInodes,
       "krUFSTotNumOfInodesAvail": krUFSTotNumOfInodesAvail,
       "krUFSPctInodesUsed": krUFSPctInodesUsed,
       "krUFSFileSystemSize64": krUFSFileSystemSize64,
       "krUFSFileSystemFreeSpace64": krUFSFileSystemFreeSpace64,
       "krUFSFreeSpaceForNonSU64": krUFSFreeSpaceForNonSU64,
       "krVXFSFileSystemGroup": krVXFSFileSystemGroup,
       "krVXFSFileTable": krVXFSFileTable,
       "krVXFSFileEntry": krVXFSFileEntry,
       "krVXFSFileSystemIndex": krVXFSFileSystemIndex,
       "krVXFSFileSystemMountPoint": krVXFSFileSystemMountPoint,
       "krVXFSFileSystemDiskName": krVXFSFileSystemDiskName,
       "krVXFSFileSystemSize": krVXFSFileSystemSize,
       "krVXFSFileSystemFreeSpace": krVXFSFileSystemFreeSpace,
       "krVXFSFreeSpaceForNonSU": krVXFSFreeSpaceForNonSU,
       "krVXFSFileSystemPctUsedSpace": krVXFSFileSystemPctUsedSpace,
       "krVXFSTotNumOfInodes": krVXFSTotNumOfInodes,
       "krVXFSTotNumOfInodesAvail": krVXFSTotNumOfInodesAvail,
       "krVXFSPctInodesUsed": krVXFSPctInodesUsed,
       "krVXFSFileSystemSize64": krVXFSFileSystemSize64,
       "krVXFSFileSystemFreeSpace64": krVXFSFileSystemFreeSpace64,
       "krVXFSFreeSpaceForNonSU64": krVXFSFreeSpaceForNonSU64,
       "krCPUDetail": krCPUDetail,
       "krCPUUtilGroup": krCPUUtilGroup,
       "krCPUUtilTable": krCPUUtilTable,
       "krCPUUtilEntry": krCPUUtilEntry,
       "krCPUInstance": krCPUInstance,
       "krCPUDelta": krCPUDelta,
       "krCPUIdleTime": krCPUIdleTime,
       "krCPUUserModeTime": krCPUUserModeTime,
       "krCPUKernelModeTime": krCPUKernelModeTime,
       "krCPUTotWaitTime": krCPUTotWaitTime,
       "krCPUTotIOWaitTime": krCPUTotIOWaitTime,
       "krCPUTotSwapWaitTime": krCPUTotSwapWaitTime,
       "krCPUTotPIOWaitTime": krCPUTotPIOWaitTime,
       "krCPUNumOfIdleThreadSched": krCPUNumOfIdleThreadSched,
       "krCPUProcess": krCPUProcess,
       "krCPUProcInStatesGroup": krCPUProcInStatesGroup,
       "krTotProcInRunQueue": krTotProcInRunQueue,
       "krTotProcBlocked": krTotProcBlocked,
       "krTotProcReadyInSwap": krTotProcReadyInSwap,
       "krTotNumberOfCPUs": krTotNumberOfCPUs,
       "krCPUIOGroup": krCPUIOGroup,
       "krCPUIOTable": krCPUIOTable,
       "krCPUIOEntry": krCPUIOEntry,
       "krIOCPUInstance": krIOCPUInstance,
       "krNumPhyBlocksRead": krNumPhyBlocksRead,
       "krNumPhyBlocksWrite": krNumPhyBlocksWrite,
       "krNumLogBlocksRead": krNumLogBlocksRead,
       "krNumLogBlocksWrite": krNumLogBlocksWrite,
       "krNumRawIOReads": krNumRawIOReads,
       "krNumRawIOWrites": krNumRawIOWrites,
       "krNumBytesRead": krNumBytesRead,
       "krNumBytesWritten": krNumBytesWritten,
       "krrcvint": krrcvint,
       "krxmtint": krxmtint,
       "krmdmint": krmdmint,
       "krNumTermInputChars": krNumTermInputChars,
       "krNumCanModeCharsHandled": krNumCanModeCharsHandled,
       "krNumTermOutChars": krNumTermOutChars,
       "krNumPhyBlocksAsyncWrite": krNumPhyBlocksAsyncWrite,
       "krphysio": krphysio,
       "krCPUInterruptsGroup": krCPUInterruptsGroup,
       "krCPUIntrTable": krCPUIntrTable,
       "krCPUIntrEntry": krCPUIntrEntry,
       "krIntrCPUInstance": krIntrCPUInstance,
       "krNumOfContextSwitches": krNumOfContextSwitches,
       "krNumberOfTraps": krNumberOfTraps,
       "krNumberOfDevInterrupts": krNumberOfDevInterrupts,
       "krNumOfIntrThreads": krNumOfIntrThreads,
       "krNumOfInterrupts": krNumOfInterrupts,
       "krCPUSyscallGroup": krCPUSyscallGroup,
       "krCPUSysTable": krCPUSysTable,
       "krCPUSysEntry": krCPUSysEntry,
       "krSyscCPUInstance": krSyscCPUInstance,
       "krNumOfSysCallsMade": krNumOfSysCallsMade,
       "krNumOfSysReads": krNumOfSysReads,
       "krNumOfSysWrites": krNumOfSysWrites,
       "krNumOfForksCalled": krNumOfForksCalled,
       "krNumOfVForksCalled": krNumOfVForksCalled,
       "krNumOfExecsCalled": krNumOfExecsCalled,
       "krTotNumOfMessages": krTotNumOfMessages,
       "krTotNumOfSemops": krTotNumOfSemops,
       "krNumOfPnameLookup": krNumOfPnameLookup,
       "krNumOfUfsigetcalls": krNumOfUfsigetcalls,
       "krNumOfDirBlocksRead": krNumOfDirBlocksRead,
       "krNumOfInodesTakenWAP": krNumOfInodesTakenWAP,
       "krNumOfInodesTakenWNAP": krNumOfInodesTakenWNAP,
       "krNumOfInodeTblOvrFlow": krNumOfInodeTblOvrFlow,
       "krNumOfFileTblOvrFlow": krNumOfFileTblOvrFlow,
       "krNumOfProcTblOvrFlow": krNumOfProcTblOvrFlow,
       "krCPUMiscGroup": krCPUMiscGroup,
       "krCPUMiscTable": krCPUMiscTable,
       "krCPUMiscEntry": krCPUMiscEntry,
       "krMiscCPUInstance": krMiscCPUInstance,
       "krNumOfIvolCSwitches": krNumOfIvolCSwitches,
       "krNumOfThrCreateCalls": krNumOfThrCreateCalls,
       "krNumOfCPUMig": krNumOfCPUMig,
       "krNumOfxcalls": krNumOfxcalls,
       "krNumOfFldMutxEntrs": krNumOfFldMutxEntrs,
       "krNumOfRWReaderFails": krNumOfRWReaderFails,
       "krNumOfRWWriterFails": krNumOfRWWriterFails,
       "krNumOfModuleLoads": krNumOfModuleLoads,
       "krNumOfModuleUnloads": krNumOfModuleUnloads,
       "krNumOfRWLockTry": krNumOfRWLockTry,
       "krCPURegWindowGroup": krCPURegWindowGroup,
       "krCPURegTable": krCPURegTable,
       "krCPURegEntry": krCPURegEntry,
       "krRWCPUInstance": krRWCPUInstance,
       "krNumOfRegWinUsrOvrFlow": krNumOfRegWinUsrOvrFlow,
       "krNumOfRegWinUsrUndrFlow": krNumOfRegWinUsrUndrFlow,
       "krNumOfRegWinSysOvrFlow": krNumOfRegWinSysOvrFlow,
       "krNumOfRegWinSysUndrFlow": krNumOfRegWinSysUndrFlow,
       "krNumOfRegWinSysUsrOvrFlow": krNumOfRegWinSysUsrOvrFlow,
       "krCPUPginfoGroup": krCPUPginfoGroup,
       "krCPUPgTable": krCPUPgTable,
       "krCPUPgEntry": krCPUPgEntry,
       "krPgCPUInstance": krPgCPUInstance,
       "krNumOfPageReclaims": krNumOfPageReclaims,
       "krNumOfFreeListPgReclaims": krNumOfFreeListPgReclaims,
       "krNumOfPageIns": krNumOfPageIns,
       "krNumOfPgsPagedIn": krNumOfPgsPagedIn,
       "krNumOfPageOuts": krNumOfPageOuts,
       "krkrNumOfPgsPagedOut": krkrNumOfPgsPagedOut,
       "krNumOfSwapIns": krNumOfSwapIns,
       "krNumOfPgsSwappedIn": krNumOfPgsSwappedIn,
       "krNumOfSwapOuts": krNumOfSwapOuts,
       "krNumOfPgsSwappedOut": krNumOfPgsSwappedOut,
       "krNumOfZeroFilledPages": krNumOfZeroFilledPages,
       "krNumOfAutoFreedPages": krNumOfAutoFreedPages,
       "krNumberOfScanedPages": krNumberOfScanedPages,
       "krNumOfPDHandsRvln": krNumOfPDHandsRvln,
       "krNumOfPagerRun": krNumOfPagerRun,
       "krCPUFaultsGroup": krCPUFaultsGroup,
       "krCPUFaultTable": krCPUFaultTable,
       "krCPUFaultEntry": krCPUFaultEntry,
       "krFaultCPUInstance": krFaultCPUInstance,
       "krNumOfMinorHatPageFaults": krNumOfMinorHatPageFaults,
       "krNumOfMinorAsPageFaults": krNumOfMinorAsPageFaults,
       "krNumOfMajorPageFaults": krNumOfMajorPageFaults,
       "krNumOfCopyOnWriteFaults": krNumOfCopyOnWriteFaults,
       "krNumOfProtectionFaults": krNumOfProtectionFaults,
       "krNumOfSWLockFaults": krNumOfSWLockFaults,
       "krNumOfAsFaultsInKSpace": krNumOfAsFaultsInKSpace,
       "krOverAllCPUStatistics": krOverAllCPUStatistics,
       "krOverAllCpuStatsUtil": krOverAllCpuStatsUtil,
       "krOverAllCpuStatsIdle": krOverAllCpuStatsIdle,
       "krMemoryUsageGroup": krMemoryUsageGroup,
       "krTotPhyMemAvail": krTotPhyMemAvail,
       "krPhyMemInUse": krPhyMemInUse,
       "krPctOfPhyMemInUse": krPctOfPhyMemInUse,
       "krFreePhyMem": krFreePhyMem,
       "krPctOfPhyMemFree": krPctOfPhyMemFree,
       "krSwapDetailGroup": krSwapDetailGroup,
       "krTotSwapSpaceAvail": krTotSwapSpaceAvail,
       "krTotReservedSwapSpace": krTotReservedSwapSpace,
       "krTotAllocatedSwapSpace": krTotAllocatedSwapSpace,
       "krTotUsedSwapSpace": krTotUsedSwapSpace,
       "krTotSwapSpace": krTotSwapSpace,
       "krTotPctOfSwapSpaceUsed": krTotPctOfSwapSpaceUsed,
       "krStreamsDetail": krStreamsDetail,
       "krStreamHeadCacheGroup": krStreamHeadCacheGroup,
       "krStrHeadCacheName": krStrHeadCacheName,
       "krStrHeadCacheCurrUsage": krStrHeadCacheCurrUsage,
       "krStrHeadCacheSize": krStrHeadCacheSize,
       "krTotSHCacheAllocation": krTotSHCacheAllocation,
       "krTotSHAllocFailures": krTotSHAllocFailures,
       "krStrHeadCachePctUsed": krStrHeadCachePctUsed,
       "krQueueCacheGroup": krQueueCacheGroup,
       "krQueueCacheName": krQueueCacheName,
       "krQueueCacheCurrUsage": krQueueCacheCurrUsage,
       "krQueueCacheSize": krQueueCacheSize,
       "krTotQCacheAllocation": krTotQCacheAllocation,
       "krTotQAllocFailures": krTotQAllocFailures,
       "krQueueCachePctUsed": krQueueCachePctUsed,
       "krStreamsMsgGroup": krStreamsMsgGroup,
       "krStrMsgCacheName": krStrMsgCacheName,
       "krStrMsgCacheCurrUsage": krStrMsgCacheCurrUsage,
       "krStrMsgCacheSize": krStrMsgCacheSize,
       "krTotSMCacheAllocation": krTotSMCacheAllocation,
       "krTotSMAllocFailures": krTotSMAllocFailures,
       "krStrMsgCachePctUsed": krStrMsgCachePctUsed,
       "krLinkinfoCacheGroup": krLinkinfoCacheGroup,
       "krLinkinfoCacheName": krLinkinfoCacheName,
       "krLinkinfoCacheCurrUsage": krLinkinfoCacheCurrUsage,
       "krLinkinfoCacheSize": krLinkinfoCacheSize,
       "krTotLICacheAllocation": krTotLICacheAllocation,
       "krTotLIAllocFailures": krTotLIAllocFailures,
       "krLinkinfoCachePctUsed": krLinkinfoCachePctUsed,
       "krStreventCacheGroup": krStreventCacheGroup,
       "krStrEventCacheName": krStrEventCacheName,
       "krStrEventCacheCurrUsage": krStrEventCacheCurrUsage,
       "krStrEventCacheSize": krStrEventCacheSize,
       "krTotSECacheAllocation": krTotSECacheAllocation,
       "krTotSEAllocFailures": krTotSEAllocFailures,
       "krStrEventCachePctUsed": krStrEventCachePctUsed,
       "krSyncqCacheGroup": krSyncqCacheGroup,
       "krSyncCacheName": krSyncCacheName,
       "krSyncCacheCurrUsage": krSyncCacheCurrUsage,
       "krSyncCacheSize": krSyncCacheSize,
       "krTotSyCacheAllocation": krTotSyCacheAllocation,
       "krTotSyAllocFailures": krTotSyAllocFailures,
       "krSyncCachePctUsed": krSyncCachePctUsed,
       "krQbandCacheGroup": krQbandCacheGroup,
       "krQbandCacheName": krQbandCacheName,
       "krQbandCacheCurrUsage": krQbandCacheCurrUsage,
       "krQbandCacheSize": krQbandCacheSize,
       "krTotQBCacheAllocation": krTotQBCacheAllocation,
       "krTotQBAllocFailures": krTotQBAllocFailures,
       "krQbandCachePctUsed": krQbandCachePctUsed,
       "krIOErrorStatsGroup": krIOErrorStatsGroup,
       "krDeviceErrorTable": krDeviceErrorTable,
       "krDeviceErrorEntry": krDeviceErrorEntry,
       "krDevDevice": krDevDevice,
       "krDevSoftwareErrors": krDevSoftwareErrors,
       "krDevHardwareErrors": krDevHardwareErrors,
       "krDevTransportErrors": krDevTransportErrors,
       "krDevTotalErrors": krDevTotalErrors,
       "krTapeErrorTable": krTapeErrorTable,
       "krTapeErrorEntry": krTapeErrorEntry,
       "krTapeDevice": krTapeDevice,
       "krTapeSoftwareErrors": krTapeSoftwareErrors,
       "krTapeHardwareErrors": krTapeHardwareErrors,
       "krTapeTransportErrors": krTapeTransportErrors,
       "krTapeTotalErrors": krTapeTotalErrors,
       "krKernelMemAllocGroup": krKernelMemAllocGroup,
       "krSmallPoolMem": krSmallPoolMem,
       "krSmallPoolMemAllocated": krSmallPoolMemAllocated,
       "krSmallPoolMemFailed": krSmallPoolMemFailed,
       "krLargePoolMem": krLargePoolMem,
       "krLargePoolMemAllocated": krLargePoolMemAllocated,
       "krLargePoolMemFailed": krLargePoolMemFailed,
       "krOversizeMem": krOversizeMem,
       "krOversizeMemFailed": krOversizeMemFailed,
       "krZoneList": krZoneList,
       "krZoneListTable": krZoneListTable,
       "krZoneListEntry": krZoneListEntry,
       "krZoneId": krZoneId,
       "krZoneName": krZoneName,
       "krStatus": krStatus,
       "krPath": krPath,
       "krIp": krIp,
       "krAutoboot": krAutoboot}
)
