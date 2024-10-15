# SNMP MIB module (HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:22 2024
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

healthMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11)
)
healthMonitor.setRevisions(
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
_HmSwap_ObjectIdentity = ObjectIdentity
hmSwap = _HmSwap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 1)
)
_HmAvailableSwapSpace_Type = Integer32
_HmAvailableSwapSpace_Object = MibScalar
hmAvailableSwapSpace = _HmAvailableSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 1, 1, 1),
    _HmAvailableSwapSpace_Type()
)
hmAvailableSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAvailableSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    hmAvailableSwapSpace.setUnits("kB")
_HmReservedSwapSpace_Type = Integer32
_HmReservedSwapSpace_Object = MibScalar
hmReservedSwapSpace = _HmReservedSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 1, 1, 2),
    _HmReservedSwapSpace_Type()
)
hmReservedSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmReservedSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    hmReservedSwapSpace.setUnits("kB")
_HmAllocatedSwapSpace_Type = Integer32
_HmAllocatedSwapSpace_Object = MibScalar
hmAllocatedSwapSpace = _HmAllocatedSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 1, 1, 3),
    _HmAllocatedSwapSpace_Type()
)
hmAllocatedSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAllocatedSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    hmAllocatedSwapSpace.setUnits("kB")
_HmUsedSwapSpace_Type = Integer32
_HmUsedSwapSpace_Object = MibScalar
hmUsedSwapSpace = _HmUsedSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 1, 1, 4),
    _HmUsedSwapSpace_Type()
)
hmUsedSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmUsedSwapSpace.setStatus("current")
if mibBuilder.loadTexts:
    hmUsedSwapSpace.setUnits("kB")
_HmKernelcontention_ObjectIdentity = ObjectIdentity
hmKernelcontention = _HmKernelcontention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 2)
)
_HmSpinsOnMutexes_Type = Integer32
_HmSpinsOnMutexes_Object = MibScalar
hmSpinsOnMutexes = _HmSpinsOnMutexes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 2, 1, 1),
    _HmSpinsOnMutexes_Type()
)
hmSpinsOnMutexes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSpinsOnMutexes.setStatus("current")
_HmTotNumOfCPUs_Type = Integer32
_HmTotNumOfCPUs_Object = MibScalar
hmTotNumOfCPUs = _HmTotNumOfCPUs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 2, 1, 2),
    _HmTotNumOfCPUs_Type()
)
hmTotNumOfCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotNumOfCPUs.setStatus("current")
_HmNFS_ObjectIdentity = ObjectIdentity
hmNFS = _HmNFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3)
)
_HmTotRPCCalls_Type = DisplayString
_HmTotRPCCalls_Object = MibScalar
hmTotRPCCalls = _HmTotRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 1),
    _HmTotRPCCalls_Type()
)
hmTotRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotRPCCalls.setStatus("current")
_HmTotBadRPCCalls_Type = Integer32
_HmTotBadRPCCalls_Object = MibScalar
hmTotBadRPCCalls = _HmTotBadRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 2),
    _HmTotBadRPCCalls_Type()
)
hmTotBadRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotBadRPCCalls.setStatus("current")
_HmTotRPCRetransmissions_Type = Integer32
_HmTotRPCRetransmissions_Object = MibScalar
hmTotRPCRetransmissions = _HmTotRPCRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 3),
    _HmTotRPCRetransmissions_Type()
)
hmTotRPCRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotRPCRetransmissions.setStatus("current")
_HmTotBadRPCReplies_Type = Integer32
_HmTotBadRPCReplies_Object = MibScalar
hmTotBadRPCReplies = _HmTotBadRPCReplies_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 4),
    _HmTotBadRPCReplies_Type()
)
hmTotBadRPCReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotBadRPCReplies.setStatus("current")
_HmTotRPCCallsTimedOut_Type = Integer32
_HmTotRPCCallsTimedOut_Object = MibScalar
hmTotRPCCallsTimedOut = _HmTotRPCCallsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 5),
    _HmTotRPCCallsTimedOut_Type()
)
hmTotRPCCallsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotRPCCallsTimedOut.setStatus("current")
_HmTotNumOfAuthRefresh_Type = Integer32
_HmTotNumOfAuthRefresh_Object = MibScalar
hmTotNumOfAuthRefresh = _HmTotNumOfAuthRefresh_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 6),
    _HmTotNumOfAuthRefresh_Type()
)
hmTotNumOfAuthRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotNumOfAuthRefresh.setStatus("current")
_HmTotFailedCallsBV_Type = Integer32
_HmTotFailedCallsBV_Object = MibScalar
hmTotFailedCallsBV = _HmTotFailedCallsBV_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 7),
    _HmTotFailedCallsBV_Type()
)
hmTotFailedCallsBV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotFailedCallsBV.setStatus("current")
_HmTimers_Type = Integer32
_HmTimers_Object = MibScalar
hmTimers = _HmTimers_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 8),
    _HmTimers_Type()
)
hmTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTimers.setStatus("current")
_HmTotMemAllocFails_Type = Integer32
_HmTotMemAllocFails_Object = MibScalar
hmTotMemAllocFails = _HmTotMemAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 9),
    _HmTotMemAllocFails_Type()
)
hmTotMemAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotMemAllocFails.setStatus("current")
_HmTotSendFails_Type = Integer32
_HmTotSendFails_Object = MibScalar
hmTotSendFails = _HmTotSendFails_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1, 10),
    _HmTotSendFails_Type()
)
hmTotSendFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotSendFails.setStatus("current")
_HmCPU_ObjectIdentity = ObjectIdentity
hmCPU = _HmCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 4)
)
_HmTotProcInRunQueue_Type = Integer32
_HmTotProcInRunQueue_Object = MibScalar
hmTotProcInRunQueue = _HmTotProcInRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 4, 1, 1),
    _HmTotProcInRunQueue_Type()
)
hmTotProcInRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotProcInRunQueue.setStatus("current")
_HmTotProcBlocked_Type = Integer32
_HmTotProcBlocked_Object = MibScalar
hmTotProcBlocked = _HmTotProcBlocked_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 4, 1, 2),
    _HmTotProcBlocked_Type()
)
hmTotProcBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotProcBlocked.setStatus("current")
_HmTotProcReadyInSwap_Type = Integer32
_HmTotProcReadyInSwap_Object = MibScalar
hmTotProcReadyInSwap = _HmTotProcReadyInSwap_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 4, 1, 3),
    _HmTotProcReadyInSwap_Type()
)
hmTotProcReadyInSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTotProcReadyInSwap.setStatus("current")
_HmDiskTable_Object = MibTable
hmDiskTable = _HmDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5, 1)
)
if mibBuilder.loadTexts:
    hmDiskTable.setStatus("current")
_HmDiskEntry_Object = MibTableRow
hmDiskEntry = _HmDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5, 1, 1)
)
hmDiskEntry.setIndexNames(
    (0, "HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDiskName"),
)
if mibBuilder.loadTexts:
    hmDiskEntry.setStatus("current")
_HmDiskName_Type = DisplayString
_HmDiskName_Object = MibTableColumn
hmDiskName = _HmDiskName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5, 1, 1, 1),
    _HmDiskName_Type()
)
hmDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDiskName.setStatus("current")
_HmDiskAliasName_Type = DisplayString
_HmDiskAliasName_Object = MibTableColumn
hmDiskAliasName = _HmDiskAliasName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5, 1, 1, 2),
    _HmDiskAliasName_Type()
)
hmDiskAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDiskAliasName.setStatus("current")
_HmAvgWaitTransactions_Type = DisplayString
_HmAvgWaitTransactions_Object = MibTableColumn
hmAvgWaitTransactions = _HmAvgWaitTransactions_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5, 1, 1, 3),
    _HmAvgWaitTransactions_Type()
)
hmAvgWaitTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAvgWaitTransactions.setStatus("current")
_HmDiskBusyPcnt_Type = DisplayString
_HmDiskBusyPcnt_Object = MibTableColumn
hmDiskBusyPcnt = _HmDiskBusyPcnt_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5, 1, 1, 4),
    _HmDiskBusyPcnt_Type()
)
hmDiskBusyPcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDiskBusyPcnt.setStatus("current")
if mibBuilder.loadTexts:
    hmDiskBusyPcnt.setUnits("%")
_HmAvgDiskSvcTime_Type = DisplayString
_HmAvgDiskSvcTime_Object = MibTableColumn
hmAvgDiskSvcTime = _HmAvgDiskSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5, 1, 1, 5),
    _HmAvgDiskSvcTime_Type()
)
hmAvgDiskSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAvgDiskSvcTime.setStatus("current")
if mibBuilder.loadTexts:
    hmAvgDiskSvcTime.setUnits("msec")
_HmRAM_ObjectIdentity = ObjectIdentity
hmRAM = _HmRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 6)
)
_HmHandspread_Type = Integer32
_HmHandspread_Object = MibScalar
hmHandspread = _HmHandspread_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 6, 1, 1),
    _HmHandspread_Type()
)
hmHandspread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmHandspread.setStatus("current")
if mibBuilder.loadTexts:
    hmHandspread.setUnits("MB")
_HmPageScanRate_Type = Integer32
_HmPageScanRate_Object = MibScalar
hmPageScanRate = _HmPageScanRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 6, 1, 2),
    _HmPageScanRate_Type()
)
hmPageScanRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPageScanRate.setStatus("current")
_HmKMEM_ObjectIdentity = ObjectIdentity
hmKMEM = _HmKMEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 7)
)
_HmKmemErrors_Type = Integer32
_HmKmemErrors_Object = MibScalar
hmKmemErrors = _HmKmemErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 7, 1, 1),
    _HmKmemErrors_Type()
)
hmKmemErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmKmemErrors.setStatus("current")
_HmKmemFreeMem_Type = Integer32
_HmKmemFreeMem_Object = MibScalar
hmKmemFreeMem = _HmKmemFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 7, 1, 2),
    _HmKmemFreeMem_Type()
)
hmKmemFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmKmemFreeMem.setStatus("current")
if mibBuilder.loadTexts:
    hmKmemFreeMem.setUnits("MB")
_HmDNLC_ObjectIdentity = ObjectIdentity
hmDNLC = _HmDNLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 8)
)
_HmDNLCHits_Type = Unsigned32
_HmDNLCHits_Object = MibScalar
hmDNLCHits = _HmDNLCHits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 8, 1, 1),
    _HmDNLCHits_Type()
)
hmDNLCHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDNLCHits.setStatus("current")
_HmDNLCMisses_Type = Unsigned32
_HmDNLCMisses_Object = MibScalar
hmDNLCMisses = _HmDNLCMisses_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 8, 1, 2),
    _HmDNLCMisses_Type()
)
hmDNLCMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDNLCMisses.setStatus("current")
_HmDNLCHitRate_Type = Unsigned32
_HmDNLCHitRate_Object = MibScalar
hmDNLCHitRate = _HmDNLCHitRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 8, 1, 3),
    _HmDNLCHitRate_Type()
)
hmDNLCHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDNLCHitRate.setStatus("current")
_HmDNLCRefRate_Type = Unsigned32
_HmDNLCRefRate_Object = MibScalar
hmDNLCRefRate = _HmDNLCRefRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 8, 1, 4),
    _HmDNLCRefRate_Type()
)
hmDNLCRefRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDNLCRefRate.setStatus("current")

# Managed Objects groups

hmSwapSpaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 1, 1)
)
hmSwapSpaceGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmAvailableSwapSpace"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmReservedSwapSpace"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmAllocatedSwapSpace"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmUsedSwapSpace"))
)
if mibBuilder.loadTexts:
    hmSwapSpaceGroup.setStatus("current")

hmMutexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 2, 1)
)
hmMutexGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmSpinsOnMutexes"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotNumOfCPUs"))
)
if mibBuilder.loadTexts:
    hmMutexGroup.setStatus("current")

hmNFSClientRPCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 3, 1)
)
hmNFSClientRPCGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotRPCCalls"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotBadRPCCalls"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotRPCRetransmissions"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotBadRPCReplies"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotRPCCallsTimedOut"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotNumOfAuthRefresh"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotFailedCallsBV"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTimers"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotMemAllocFails"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotSendFails"))
)
if mibBuilder.loadTexts:
    hmNFSClientRPCGroup.setStatus("current")

hmCPUProcInStatesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 4, 1)
)
hmCPUProcInStatesGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotProcInRunQueue"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotProcBlocked"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmTotProcReadyInSwap"))
)
if mibBuilder.loadTexts:
    hmCPUProcInStatesGroup.setStatus("current")

hmDiskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 5)
)
hmDiskGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDiskName"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDiskAliasName"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmAvgWaitTransactions"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDiskBusyPcnt"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmAvgDiskSvcTime"))
)
if mibBuilder.loadTexts:
    hmDiskGroup.setStatus("current")

hmRamMemoryPagingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 6, 1)
)
hmRamMemoryPagingGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmHandspread"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmPageScanRate"))
)
if mibBuilder.loadTexts:
    hmRamMemoryPagingGroup.setStatus("current")

hmKmemStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 7, 1)
)
hmKmemStatisticsGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmKmemErrors"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmKmemFreeMem"))
)
if mibBuilder.loadTexts:
    hmKmemStatisticsGroup.setStatus("current")

hmDNLCStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11, 8, 1)
)
hmDNLCStatGroup.setObjects(
      *(("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDNLCHits"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDNLCMisses"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDNLCHitRate"),
        ("HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB", "hmDNLCRefRate"))
)
if mibBuilder.loadTexts:
    hmDNLCStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HEALTH-MONITOR-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "modules": modules,
       "healthMonitor": healthMonitor,
       "hmSwap": hmSwap,
       "hmSwapSpaceGroup": hmSwapSpaceGroup,
       "hmAvailableSwapSpace": hmAvailableSwapSpace,
       "hmReservedSwapSpace": hmReservedSwapSpace,
       "hmAllocatedSwapSpace": hmAllocatedSwapSpace,
       "hmUsedSwapSpace": hmUsedSwapSpace,
       "hmKernelcontention": hmKernelcontention,
       "hmMutexGroup": hmMutexGroup,
       "hmSpinsOnMutexes": hmSpinsOnMutexes,
       "hmTotNumOfCPUs": hmTotNumOfCPUs,
       "hmNFS": hmNFS,
       "hmNFSClientRPCGroup": hmNFSClientRPCGroup,
       "hmTotRPCCalls": hmTotRPCCalls,
       "hmTotBadRPCCalls": hmTotBadRPCCalls,
       "hmTotRPCRetransmissions": hmTotRPCRetransmissions,
       "hmTotBadRPCReplies": hmTotBadRPCReplies,
       "hmTotRPCCallsTimedOut": hmTotRPCCallsTimedOut,
       "hmTotNumOfAuthRefresh": hmTotNumOfAuthRefresh,
       "hmTotFailedCallsBV": hmTotFailedCallsBV,
       "hmTimers": hmTimers,
       "hmTotMemAllocFails": hmTotMemAllocFails,
       "hmTotSendFails": hmTotSendFails,
       "hmCPU": hmCPU,
       "hmCPUProcInStatesGroup": hmCPUProcInStatesGroup,
       "hmTotProcInRunQueue": hmTotProcInRunQueue,
       "hmTotProcBlocked": hmTotProcBlocked,
       "hmTotProcReadyInSwap": hmTotProcReadyInSwap,
       "hmDiskGroup": hmDiskGroup,
       "hmDiskTable": hmDiskTable,
       "hmDiskEntry": hmDiskEntry,
       "hmDiskName": hmDiskName,
       "hmDiskAliasName": hmDiskAliasName,
       "hmAvgWaitTransactions": hmAvgWaitTransactions,
       "hmDiskBusyPcnt": hmDiskBusyPcnt,
       "hmAvgDiskSvcTime": hmAvgDiskSvcTime,
       "hmRAM": hmRAM,
       "hmRamMemoryPagingGroup": hmRamMemoryPagingGroup,
       "hmHandspread": hmHandspread,
       "hmPageScanRate": hmPageScanRate,
       "hmKMEM": hmKMEM,
       "hmKmemStatisticsGroup": hmKmemStatisticsGroup,
       "hmKmemErrors": hmKmemErrors,
       "hmKmemFreeMem": hmKmemFreeMem,
       "hmDNLC": hmDNLC,
       "hmDNLCStatGroup": hmDNLCStatGroup,
       "hmDNLCHits": hmDNLCHits,
       "hmDNLCMisses": hmDNLCMisses,
       "hmDNLCHitRate": hmDNLCHitRate,
       "hmDNLCRefRate": hmDNLCRefRate}
)
