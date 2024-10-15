# SNMP MIB module (EMPIRE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMPIRE
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:26 2024
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
 NotificationType,
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
    "NotificationType",
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

_Empire_ObjectIdentity = ObjectIdentity
empire = _Empire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546)
)
_Unix_ObjectIdentity = ObjectIdentity
unix = _Unix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1)
)
_Sysmgmt_ObjectIdentity = ObjectIdentity
sysmgmt = _Sysmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1)
)
_Nodename_Type = DisplayString
_Nodename_Object = MibScalar
nodename = _Nodename_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 1),
    _Nodename_Type()
)
nodename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodename.setStatus("mandatory")
_Cpu_Type = DisplayString
_Cpu_Object = MibScalar
cpu = _Cpu_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 2),
    _Cpu_Type()
)
cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu.setStatus("mandatory")
_Memory_Type = Integer32
_Memory_Object = MibScalar
memory = _Memory_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 3),
    _Memory_Type()
)
memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memory.setStatus("mandatory")
_Hostid_Type = DisplayString
_Hostid_Object = MibScalar
hostid = _Hostid_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 4),
    _Hostid_Type()
)
hostid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostid.setStatus("mandatory")
_Osver_Type = DisplayString
_Osver_Object = MibScalar
osver = _Osver_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 5),
    _Osver_Type()
)
osver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osver.setStatus("mandatory")
_Osrel_Type = DisplayString
_Osrel_Object = MibScalar
osrel = _Osrel_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 6),
    _Osrel_Type()
)
osrel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrel.setStatus("mandatory")
_DevTable_Object = MibTable
devTable = _DevTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    devTable.setStatus("mandatory")
_DevTableEntry_Object = MibTableRow
devTableEntry = _DevTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1)
)
devTableEntry.setIndexNames(
    (0, "EMPIRE", "devIndex"),
)
if mibBuilder.loadTexts:
    devTableEntry.setStatus("mandatory")
_DevIndex_Type = Integer32
_DevIndex_Object = MibTableColumn
devIndex = _DevIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 1),
    _DevIndex_Type()
)
devIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIndex.setStatus("mandatory")
_DevDevice_Type = DisplayString
_DevDevice_Object = MibTableColumn
devDevice = _DevDevice_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 2),
    _DevDevice_Type()
)
devDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDevice.setStatus("mandatory")
_DevMntPt_Type = DisplayString
_DevMntPt_Object = MibTableColumn
devMntPt = _DevMntPt_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 3),
    _DevMntPt_Type()
)
devMntPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devMntPt.setStatus("mandatory")
_DevBsize_Type = Integer32
_DevBsize_Object = MibTableColumn
devBsize = _DevBsize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 4),
    _DevBsize_Type()
)
devBsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devBsize.setStatus("mandatory")
_DevTblks_Type = Integer32
_DevTblks_Object = MibTableColumn
devTblks = _DevTblks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 5),
    _DevTblks_Type()
)
devTblks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTblks.setStatus("mandatory")
_DevFblks_Type = Gauge32
_DevFblks_Object = MibTableColumn
devFblks = _DevFblks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 6),
    _DevFblks_Type()
)
devFblks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFblks.setStatus("mandatory")
_DevTfiles_Type = Integer32
_DevTfiles_Object = MibTableColumn
devTfiles = _DevTfiles_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 7),
    _DevTfiles_Type()
)
devTfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTfiles.setStatus("mandatory")
_DevFfiles_Type = Gauge32
_DevFfiles_Object = MibTableColumn
devFfiles = _DevFfiles_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 8),
    _DevFfiles_Type()
)
devFfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFfiles.setStatus("mandatory")
_DevMaxNameLen_Type = Integer32
_DevMaxNameLen_Object = MibTableColumn
devMaxNameLen = _DevMaxNameLen_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 9),
    _DevMaxNameLen_Type()
)
devMaxNameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devMaxNameLen.setStatus("mandatory")
_DevType_Type = DisplayString
_DevType_Object = MibTableColumn
devType = _DevType_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 10),
    _DevType_Type()
)
devType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devType.setStatus("mandatory")
_DevFsid_Type = Integer32
_DevFsid_Object = MibTableColumn
devFsid = _DevFsid_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 11),
    _DevFsid_Type()
)
devFsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFsid.setStatus("mandatory")
_DevFstr_Type = DisplayString
_DevFstr_Object = MibTableColumn
devFstr = _DevFstr_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 12),
    _DevFstr_Type()
)
devFstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFstr.setStatus("mandatory")


class _DevUnmount_Type(Integer32):
    """Custom type devUnmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("valid", 2))
    )


_DevUnmount_Type.__name__ = "Integer32"
_DevUnmount_Object = MibTableColumn
devUnmount = _DevUnmount_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 13),
    _DevUnmount_Type()
)
devUnmount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devUnmount.setStatus("mandatory")


class _DevCapacity_Type(Integer32):
    """Custom type devCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DevCapacity_Type.__name__ = "Integer32"
_DevCapacity_Object = MibTableColumn
devCapacity = _DevCapacity_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 14),
    _DevCapacity_Type()
)
devCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCapacity.setStatus("mandatory")


class _DevInodeCapacity_Type(Integer32):
    """Custom type devInodeCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DevInodeCapacity_Type.__name__ = "Integer32"
_DevInodeCapacity_Object = MibTableColumn
devInodeCapacity = _DevInodeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 7, 1, 15),
    _DevInodeCapacity_Type()
)
devInodeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devInodeCapacity.setStatus("mandatory")
_AgentVersion_Type = DisplayString
_AgentVersion_Object = MibScalar
agentVersion = _AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 8),
    _AgentVersion_Type()
)
agentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVersion.setStatus("mandatory")
_KernelConfig_ObjectIdentity = ObjectIdentity
kernelConfig = _KernelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9)
)
_MaxProcs_Type = Integer32
_MaxProcs_Object = MibScalar
maxProcs = _MaxProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 1),
    _MaxProcs_Type()
)
maxProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxProcs.setStatus("mandatory")
_SerialNumber_Type = Integer32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_RomVersion_Type = DisplayString
_RomVersion_Object = MibScalar
romVersion = _RomVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 3),
    _RomVersion_Type()
)
romVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    romVersion.setStatus("mandatory")
_NumCPU_Type = Gauge32
_NumCPU_Object = MibScalar
numCPU = _NumCPU_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 4),
    _NumCPU_Type()
)
numCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCPU.setStatus("mandatory")
_ClockHZ_Type = Integer32
_ClockHZ_Object = MibScalar
clockHZ = _ClockHZ_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 5),
    _ClockHZ_Type()
)
clockHZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockHZ.setStatus("mandatory")
_KernelVers_Type = DisplayString
_KernelVers_Object = MibScalar
kernelVers = _KernelVers_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 6),
    _KernelVers_Type()
)
kernelVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kernelVers.setStatus("mandatory")
_VirtualMem_Type = Gauge32
_VirtualMem_Object = MibScalar
virtualMem = _VirtualMem_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 7),
    _VirtualMem_Type()
)
virtualMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualMem.setStatus("mandatory")
_MaxInode_Type = Gauge32
_MaxInode_Object = MibScalar
maxInode = _MaxInode_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 8),
    _MaxInode_Type()
)
maxInode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxInode.setStatus("mandatory")
_MaxFiles_Type = Gauge32
_MaxFiles_Object = MibScalar
maxFiles = _MaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 9),
    _MaxFiles_Type()
)
maxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFiles.setStatus("mandatory")
_MaxClist_Type = Gauge32
_MaxClist_Object = MibScalar
maxClist = _MaxClist_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 10),
    _MaxClist_Type()
)
maxClist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxClist.setStatus("mandatory")
_MaxMemPerProc_Type = Gauge32
_MaxMemPerProc_Object = MibScalar
maxMemPerProc = _MaxMemPerProc_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 11),
    _MaxMemPerProc_Type()
)
maxMemPerProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxMemPerProc.setStatus("mandatory")
_TotalSwap_Type = Integer32
_TotalSwap_Object = MibScalar
totalSwap = _TotalSwap_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 12),
    _TotalSwap_Type()
)
totalSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSwap.setStatus("mandatory")
_OpenMaxPerProc_Type = Integer32
_OpenMaxPerProc_Object = MibScalar
openMaxPerProc = _OpenMaxPerProc_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 13),
    _OpenMaxPerProc_Type()
)
openMaxPerProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openMaxPerProc.setStatus("mandatory")


class _PosixJobCtrl_Type(Integer32):
    """Custom type posixJobCtrl based on Integer32"""
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


_PosixJobCtrl_Type.__name__ = "Integer32"
_PosixJobCtrl_Object = MibScalar
posixJobCtrl = _PosixJobCtrl_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 14),
    _PosixJobCtrl_Type()
)
posixJobCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posixJobCtrl.setStatus("mandatory")
_PosixVersion_Type = Integer32
_PosixVersion_Object = MibScalar
posixVersion = _PosixVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 15),
    _PosixVersion_Type()
)
posixVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posixVersion.setStatus("mandatory")
_PageSize_Type = Integer32
_PageSize_Object = MibScalar
pageSize = _PageSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 16),
    _PageSize_Type()
)
pageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pageSize.setStatus("mandatory")
_WordSize_Type = Integer32
_WordSize_Object = MibScalar
wordSize = _WordSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 9, 17),
    _WordSize_Type()
)
wordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wordSize.setStatus("mandatory")
_Bootconf_ObjectIdentity = ObjectIdentity
bootconf = _Bootconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10)
)
_RootName_Type = DisplayString
_RootName_Object = MibScalar
rootName = _RootName_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 1),
    _RootName_Type()
)
rootName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootName.setStatus("mandatory")
_RootFSType_Type = DisplayString
_RootFSType_Object = MibScalar
rootFSType = _RootFSType_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 2),
    _RootFSType_Type()
)
rootFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootFSType.setStatus("mandatory")
_RootBlocks_Type = Integer32
_RootBlocks_Object = MibScalar
rootBlocks = _RootBlocks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 3),
    _RootBlocks_Type()
)
rootBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rootBlocks.setStatus("mandatory")
_DumpName_Type = DisplayString
_DumpName_Object = MibScalar
dumpName = _DumpName_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 4),
    _DumpName_Type()
)
dumpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpName.setStatus("mandatory")
_DumpFSType_Type = DisplayString
_DumpFSType_Object = MibScalar
dumpFSType = _DumpFSType_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 5),
    _DumpFSType_Type()
)
dumpFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFSType.setStatus("mandatory")
_DumpBlocks_Type = Integer32
_DumpBlocks_Object = MibScalar
dumpBlocks = _DumpBlocks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 6),
    _DumpBlocks_Type()
)
dumpBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpBlocks.setStatus("mandatory")
_SwapName_Type = DisplayString
_SwapName_Object = MibScalar
swapName = _SwapName_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 7),
    _SwapName_Type()
)
swapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapName.setStatus("mandatory")
_SwapFSType_Type = DisplayString
_SwapFSType_Object = MibScalar
swapFSType = _SwapFSType_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 8),
    _SwapFSType_Type()
)
swapFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapFSType.setStatus("mandatory")
_SwapSize_Type = Integer32
_SwapSize_Object = MibScalar
swapSize = _SwapSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 10, 9),
    _SwapSize_Type()
)
swapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapSize.setStatus("mandatory")
_Streams_ObjectIdentity = ObjectIdentity
streams = _Streams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11)
)
_MaxmsgSize_Type = Integer32
_MaxmsgSize_Object = MibScalar
maxmsgSize = _MaxmsgSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 1),
    _MaxmsgSize_Type()
)
maxmsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxmsgSize.setStatus("mandatory")
_MaxNumPush_Type = Integer32
_MaxNumPush_Object = MibScalar
maxNumPush = _MaxNumPush_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 2),
    _MaxNumPush_Type()
)
maxNumPush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumPush.setStatus("mandatory")
_NumMuxLinks_Type = Gauge32
_NumMuxLinks_Object = MibScalar
numMuxLinks = _NumMuxLinks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 3),
    _NumMuxLinks_Type()
)
numMuxLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numMuxLinks.setStatus("mandatory")
_StreamUse_Type = Gauge32
_StreamUse_Object = MibScalar
streamUse = _StreamUse_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 4),
    _StreamUse_Type()
)
streamUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamUse.setStatus("mandatory")
_StreamMaxs_Type = Integer32
_StreamMaxs_Object = MibScalar
streamMaxs = _StreamMaxs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 5),
    _StreamMaxs_Type()
)
streamMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamMaxs.setStatus("mandatory")
_StreamFails_Type = Counter32
_StreamFails_Object = MibScalar
streamFails = _StreamFails_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 6),
    _StreamFails_Type()
)
streamFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamFails.setStatus("mandatory")
_QueueUse_Type = Gauge32
_QueueUse_Object = MibScalar
queueUse = _QueueUse_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 7),
    _QueueUse_Type()
)
queueUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueUse.setStatus("mandatory")
_QueueMaxs_Type = Integer32
_QueueMaxs_Object = MibScalar
queueMaxs = _QueueMaxs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 8),
    _QueueMaxs_Type()
)
queueMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueMaxs.setStatus("mandatory")
_QueueFails_Type = Counter32
_QueueFails_Object = MibScalar
queueFails = _QueueFails_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 9),
    _QueueFails_Type()
)
queueFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueFails.setStatus("mandatory")
_MblockUse_Type = Gauge32
_MblockUse_Object = MibScalar
mblockUse = _MblockUse_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 10),
    _MblockUse_Type()
)
mblockUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mblockUse.setStatus("mandatory")
_MblockMaxs_Type = Integer32
_MblockMaxs_Object = MibScalar
mblockMaxs = _MblockMaxs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 11),
    _MblockMaxs_Type()
)
mblockMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mblockMaxs.setStatus("mandatory")
_MblockFails_Type = Counter32
_MblockFails_Object = MibScalar
mblockFails = _MblockFails_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 12),
    _MblockFails_Type()
)
mblockFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mblockFails.setStatus("mandatory")
_DblockUse_Type = Gauge32
_DblockUse_Object = MibScalar
dblockUse = _DblockUse_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 13),
    _DblockUse_Type()
)
dblockUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dblockUse.setStatus("mandatory")
_DblockMaxs_Type = Integer32
_DblockMaxs_Object = MibScalar
dblockMaxs = _DblockMaxs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 14),
    _DblockMaxs_Type()
)
dblockMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dblockMaxs.setStatus("mandatory")
_DblockFails_Type = Counter32
_DblockFails_Object = MibScalar
dblockFails = _DblockFails_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 11, 15),
    _DblockFails_Type()
)
dblockFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dblockFails.setStatus("mandatory")


class _SystemType_Type(Integer32):
    """Custom type systemType based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("aix41RS6000", 15),
          ("aix42RS6000", 16),
          ("aix43RS6000", 17),
          ("aix5RS6000", 25),
          ("digitalUNIX", 19),
          ("hpux10Parisc", 7),
          ("hpux11IA64", 28),
          ("hpux11Parisc", 21),
          ("hpux9Parisc", 6),
          ("irix62Mips", 12),
          ("irix63Mips", 13),
          ("irix64Mips", 14),
          ("irix65Mips", 18),
          ("linuxIA64", 27),
          ("linuxIntel", 20),
          ("nt351Alpha", 9),
          ("nt351Intel", 8),
          ("nt40Alpha", 11),
          ("nt40Intel", 10),
          ("nt50Alpha", 23),
          ("nt50Intel", 22),
          ("nt51Intel", 24),
          ("nt52Intel", 26),
          ("solarisIntel", 3),
          ("solarisPPC", 4),
          ("solarisSparc", 2),
          ("sunosSparc", 5),
          ("unknown", 1))
    )


_SystemType_Type.__name__ = "Integer32"
_SystemType_Object = MibScalar
systemType = _SystemType_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 12),
    _SystemType_Type()
)
systemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemType.setStatus("mandatory")
_SystemEdgeUptime_Type = TimeTicks
_SystemEdgeUptime_Object = MibScalar
systemEdgeUptime = _SystemEdgeUptime_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 13),
    _SystemEdgeUptime_Type()
)
systemEdgeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEdgeUptime.setStatus("mandatory")
_SysedgeLicenseString_Type = DisplayString
_SysedgeLicenseString_Object = MibScalar
sysedgeLicenseString = _SysedgeLicenseString_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 14),
    _SysedgeLicenseString_Type()
)
sysedgeLicenseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysedgeLicenseString.setStatus("mandatory")
_SysedgeLicenseKey_Type = DisplayString
_SysedgeLicenseKey_Object = MibScalar
sysedgeLicenseKey = _SysedgeLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 16),
    _SysedgeLicenseKey_Type()
)
sysedgeLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysedgeLicenseKey.setStatus("mandatory")


class _SysedgeMode_Type(Integer32):
    """Custom type sysedgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullMode", 1),
          ("restrictedMode", 2))
    )


_SysedgeMode_Type.__name__ = "Integer32"
_SysedgeMode_Object = MibScalar
sysedgeMode = _SysedgeMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 17),
    _SysedgeMode_Type()
)
sysedgeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysedgeMode.setStatus("mandatory")
_SystemTimeZone_Type = DisplayString
_SystemTimeZone_Object = MibScalar
systemTimeZone = _SystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 18),
    _SystemTimeZone_Type()
)
systemTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeZone.setStatus("mandatory")
_SysedgeAddressList_Type = DisplayString
_SysedgeAddressList_Object = MibScalar
sysedgeAddressList = _SysedgeAddressList_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 19),
    _SysedgeAddressList_Type()
)
sysedgeAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysedgeAddressList.setStatus("mandatory")
_SysedgeFQDN_Type = DisplayString
_SysedgeFQDN_Object = MibScalar
sysedgeFQDN = _SysedgeFQDN_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 20),
    _SysedgeFQDN_Type()
)
sysedgeFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysedgeFQDN.setStatus("mandatory")


class _SysedgeConfProfile_Type(DisplayString):
    """Custom type sysedgeConfProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SysedgeConfProfile_Type.__name__ = "DisplayString"
_SysedgeConfProfile_Object = MibScalar
sysedgeConfProfile = _SysedgeConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 21),
    _SysedgeConfProfile_Type()
)
sysedgeConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysedgeConfProfile.setStatus("mandatory")
_SysedgeInstallDir_Type = DisplayString
_SysedgeInstallDir_Object = MibScalar
sysedgeInstallDir = _SysedgeInstallDir_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 22),
    _SysedgeInstallDir_Type()
)
sysedgeInstallDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysedgeInstallDir.setStatus("mandatory")
_SysedgePluginList_Type = DisplayString
_SysedgePluginList_Object = MibScalar
sysedgePluginList = _SysedgePluginList_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 1, 23),
    _SysedgePluginList_Type()
)
sysedgePluginList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysedgePluginList.setStatus("mandatory")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2)
)
if mibBuilder.loadTexts:
    userTable.setStatus("mandatory")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1)
)
userEntry.setIndexNames(
    (0, "EMPIRE", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("mandatory")
_UserIndex_Type = Integer32
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userIndex.setStatus("mandatory")
_UserLoginID_Type = DisplayString
_UserLoginID_Object = MibTableColumn
userLoginID = _UserLoginID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 2),
    _UserLoginID_Type()
)
userLoginID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLoginID.setStatus("mandatory")
_UserPasswd_Type = DisplayString
_UserPasswd_Object = MibTableColumn
userPasswd = _UserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 3),
    _UserPasswd_Type()
)
userPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPasswd.setStatus("mandatory")
_UserUID_Type = Integer32
_UserUID_Object = MibTableColumn
userUID = _UserUID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 4),
    _UserUID_Type()
)
userUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userUID.setStatus("mandatory")
_UserGID_Type = Integer32
_UserGID_Object = MibTableColumn
userGID = _UserGID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 5),
    _UserGID_Type()
)
userGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGID.setStatus("mandatory")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 6),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")
_UserHomeDir_Type = DisplayString
_UserHomeDir_Object = MibTableColumn
userHomeDir = _UserHomeDir_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 7),
    _UserHomeDir_Type()
)
userHomeDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userHomeDir.setStatus("mandatory")
_UserShell_Type = DisplayString
_UserShell_Object = MibTableColumn
userShell = _UserShell_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 2, 1, 8),
    _UserShell_Type()
)
userShell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userShell.setStatus("mandatory")
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 3)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("mandatory")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 3, 1)
)
groupEntry.setIndexNames(
    (0, "EMPIRE", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("mandatory")
_GroupIndex_Type = Integer32
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 3, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupIndex.setStatus("mandatory")
_GroupName_Type = DisplayString
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 3, 1, 2),
    _GroupName_Type()
)
groupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupName.setStatus("mandatory")
_GroupPasswd_Type = DisplayString
_GroupPasswd_Object = MibTableColumn
groupPasswd = _GroupPasswd_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 3, 1, 3),
    _GroupPasswd_Type()
)
groupPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPasswd.setStatus("mandatory")
_GroupGID_Type = Integer32
_GroupGID_Object = MibTableColumn
groupGID = _GroupGID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 3, 1, 4),
    _GroupGID_Type()
)
groupGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupGID.setStatus("mandatory")
_ProcessTable_Object = MibTable
processTable = _ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4)
)
if mibBuilder.loadTexts:
    processTable.setStatus("mandatory")
_ProcessEntry_Object = MibTableRow
processEntry = _ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1)
)
processEntry.setIndexNames(
    (0, "EMPIRE", "processID"),
)
if mibBuilder.loadTexts:
    processEntry.setStatus("mandatory")
_ProcessID_Type = Integer32
_ProcessID_Object = MibTableColumn
processID = _ProcessID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 1),
    _ProcessID_Type()
)
processID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processID.setStatus("mandatory")
_ProcessName_Type = DisplayString
_ProcessName_Object = MibTableColumn
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 2),
    _ProcessName_Type()
)
processName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processName.setStatus("mandatory")
_ProcessState_Type = Integer32
_ProcessState_Object = MibTableColumn
processState = _ProcessState_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 3),
    _ProcessState_Type()
)
processState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processState.setStatus("deprecated")
_ProcessNice_Type = Integer32
_ProcessNice_Object = MibTableColumn
processNice = _ProcessNice_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 4),
    _ProcessNice_Type()
)
processNice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processNice.setStatus("mandatory")
_ProcessFlags_Type = Integer32
_ProcessFlags_Object = MibTableColumn
processFlags = _ProcessFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 5),
    _ProcessFlags_Type()
)
processFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processFlags.setStatus("mandatory")
_ProcessUID_Type = Integer32
_ProcessUID_Object = MibTableColumn
processUID = _ProcessUID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 6),
    _ProcessUID_Type()
)
processUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processUID.setStatus("mandatory")
_ProcessGID_Type = Integer32
_ProcessGID_Object = MibTableColumn
processGID = _ProcessGID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 7),
    _ProcessGID_Type()
)
processGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processGID.setStatus("mandatory")
_ProcessKill_Type = Integer32
_ProcessKill_Object = MibTableColumn
processKill = _ProcessKill_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 8),
    _ProcessKill_Type()
)
processKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processKill.setStatus("mandatory")
_ProcessMEM_Type = Gauge32
_ProcessMEM_Object = MibTableColumn
processMEM = _ProcessMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 9),
    _ProcessMEM_Type()
)
processMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMEM.setStatus("mandatory")
_ProcessSize_Type = Gauge32
_ProcessSize_Object = MibTableColumn
processSize = _ProcessSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 10),
    _ProcessSize_Type()
)
processSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processSize.setStatus("mandatory")
_ProcessRSS_Type = Gauge32
_ProcessRSS_Object = MibTableColumn
processRSS = _ProcessRSS_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 11),
    _ProcessRSS_Type()
)
processRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processRSS.setStatus("mandatory")
_ProcessTime_Type = Integer32
_ProcessTime_Object = MibTableColumn
processTime = _ProcessTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 12),
    _ProcessTime_Type()
)
processTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processTime.setStatus("mandatory")
_ProcessParentPID_Type = Integer32
_ProcessParentPID_Object = MibTableColumn
processParentPID = _ProcessParentPID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 13),
    _ProcessParentPID_Type()
)
processParentPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processParentPID.setStatus("mandatory")
_ProcessNumThreads_Type = Integer32
_ProcessNumThreads_Object = MibTableColumn
processNumThreads = _ProcessNumThreads_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 14),
    _ProcessNumThreads_Type()
)
processNumThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processNumThreads.setStatus("mandatory")
_ProcessInBlks_Type = Counter32
_ProcessInBlks_Object = MibTableColumn
processInBlks = _ProcessInBlks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 15),
    _ProcessInBlks_Type()
)
processInBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processInBlks.setStatus("mandatory")
_ProcessOutBlks_Type = Counter32
_ProcessOutBlks_Object = MibTableColumn
processOutBlks = _ProcessOutBlks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 16),
    _ProcessOutBlks_Type()
)
processOutBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processOutBlks.setStatus("mandatory")
_ProcessMsgsSent_Type = Counter32
_ProcessMsgsSent_Object = MibTableColumn
processMsgsSent = _ProcessMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 17),
    _ProcessMsgsSent_Type()
)
processMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMsgsSent.setStatus("mandatory")
_ProcessMsgsRecv_Type = Counter32
_ProcessMsgsRecv_Object = MibTableColumn
processMsgsRecv = _ProcessMsgsRecv_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 18),
    _ProcessMsgsRecv_Type()
)
processMsgsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMsgsRecv.setStatus("mandatory")
_ProcessSysCalls_Type = Counter32
_ProcessSysCalls_Object = MibTableColumn
processSysCalls = _ProcessSysCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 19),
    _ProcessSysCalls_Type()
)
processSysCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processSysCalls.setStatus("mandatory")
_ProcessMinorPgFlts_Type = Counter32
_ProcessMinorPgFlts_Object = MibTableColumn
processMinorPgFlts = _ProcessMinorPgFlts_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 20),
    _ProcessMinorPgFlts_Type()
)
processMinorPgFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMinorPgFlts.setStatus("mandatory")
_ProcessMajorPgFlts_Type = Counter32
_ProcessMajorPgFlts_Object = MibTableColumn
processMajorPgFlts = _ProcessMajorPgFlts_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 21),
    _ProcessMajorPgFlts_Type()
)
processMajorPgFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMajorPgFlts.setStatus("mandatory")
_ProcessNumSwaps_Type = Counter32
_ProcessNumSwaps_Object = MibTableColumn
processNumSwaps = _ProcessNumSwaps_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 22),
    _ProcessNumSwaps_Type()
)
processNumSwaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processNumSwaps.setStatus("mandatory")
_ProcessVolCtx_Type = Counter32
_ProcessVolCtx_Object = MibTableColumn
processVolCtx = _ProcessVolCtx_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 23),
    _ProcessVolCtx_Type()
)
processVolCtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processVolCtx.setStatus("mandatory")
_ProcessInvolCtx_Type = Counter32
_ProcessInvolCtx_Object = MibTableColumn
processInvolCtx = _ProcessInvolCtx_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 24),
    _ProcessInvolCtx_Type()
)
processInvolCtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processInvolCtx.setStatus("mandatory")
_ProcessArgs_Type = DisplayString
_ProcessArgs_Object = MibTableColumn
processArgs = _ProcessArgs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 25),
    _ProcessArgs_Type()
)
processArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processArgs.setStatus("mandatory")
_ProcessStartTime_Type = DisplayString
_ProcessStartTime_Object = MibTableColumn
processStartTime = _ProcessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 26),
    _ProcessStartTime_Type()
)
processStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processStartTime.setStatus("mandatory")
_ProcessStateStr_Type = DisplayString
_ProcessStateStr_Object = MibTableColumn
processStateStr = _ProcessStateStr_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 27),
    _ProcessStateStr_Type()
)
processStateStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processStateStr.setStatus("mandatory")


class _ProcessStateInt_Type(Integer32):
    """Custom type processStateInt based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("procStateActive", 3),
          ("procStateOther", 9),
          ("procStateRunnable", 2),
          ("procStateSleep", 7),
          ("procStateSleeping", 5),
          ("procStateStarting", 1),
          ("procStateStop", 8),
          ("procStateSwapped", 6),
          ("procStateWait", 4),
          ("procStateZombie", 10))
    )


_ProcessStateInt_Type.__name__ = "Integer32"
_ProcessStateInt_Object = MibTableColumn
processStateInt = _ProcessStateInt_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 4, 1, 28),
    _ProcessStateInt_Type()
)
processStateInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processStateInt.setStatus("mandatory")
_WhoTable_Object = MibTable
whoTable = _WhoTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5)
)
if mibBuilder.loadTexts:
    whoTable.setStatus("mandatory")
_WhoEntry_Object = MibTableRow
whoEntry = _WhoEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5, 1)
)
whoEntry.setIndexNames(
    (0, "EMPIRE", "whoIndex"),
)
if mibBuilder.loadTexts:
    whoEntry.setStatus("mandatory")
_WhoIndex_Type = Integer32
_WhoIndex_Object = MibTableColumn
whoIndex = _WhoIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5, 1, 1),
    _WhoIndex_Type()
)
whoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoIndex.setStatus("mandatory")
_WhoName_Type = DisplayString
_WhoName_Object = MibTableColumn
whoName = _WhoName_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5, 1, 2),
    _WhoName_Type()
)
whoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoName.setStatus("mandatory")
_WhoDevice_Type = DisplayString
_WhoDevice_Object = MibTableColumn
whoDevice = _WhoDevice_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5, 1, 3),
    _WhoDevice_Type()
)
whoDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoDevice.setStatus("mandatory")
_WhoPID_Type = Integer32
_WhoPID_Object = MibTableColumn
whoPID = _WhoPID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5, 1, 4),
    _WhoPID_Type()
)
whoPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoPID.setStatus("mandatory")
_WhoTime_Type = TimeTicks
_WhoTime_Object = MibTableColumn
whoTime = _WhoTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5, 1, 5),
    _WhoTime_Type()
)
whoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoTime.setStatus("mandatory")
_WhoWhere_Type = DisplayString
_WhoWhere_Object = MibTableColumn
whoWhere = _WhoWhere_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 5, 1, 6),
    _WhoWhere_Type()
)
whoWhere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoWhere.setStatus("mandatory")
_RemoteShell_ObjectIdentity = ObjectIdentity
remoteShell = _RemoteShell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 6)
)
_ShellOutput_Type = DisplayString
_ShellOutput_Object = MibScalar
shellOutput = _ShellOutput_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 6, 1),
    _ShellOutput_Type()
)
shellOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shellOutput.setStatus("mandatory")
_ShellCmd_Type = DisplayString
_ShellCmd_Object = MibScalar
shellCmd = _ShellCmd_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 6, 2),
    _ShellCmd_Type()
)
shellCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shellCmd.setStatus("mandatory")
_ShellExitStat_Type = Integer32
_ShellExitStat_Object = MibScalar
shellExitStat = _ShellExitStat_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 6, 3),
    _ShellExitStat_Type()
)
shellExitStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shellExitStat.setStatus("mandatory")


class _ShellOutputContents_Type(DisplayString):
    """Custom type shellOutputContents based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ShellOutputContents_Type.__name__ = "DisplayString"
_ShellOutputContents_Object = MibScalar
shellOutputContents = _ShellOutputContents_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 6, 4),
    _ShellOutputContents_Type()
)
shellOutputContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shellOutputContents.setStatus("mandatory")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7)
)
_Kernelperf_ObjectIdentity = ObjectIdentity
kernelperf = _Kernelperf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8)
)
_RunQLen_Type = Gauge32
_RunQLen_Object = MibScalar
runQLen = _RunQLen_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 4),
    _RunQLen_Type()
)
runQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runQLen.setStatus("mandatory")
_DiskWaitNum_Type = Gauge32
_DiskWaitNum_Object = MibScalar
diskWaitNum = _DiskWaitNum_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 5),
    _DiskWaitNum_Type()
)
diskWaitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWaitNum.setStatus("mandatory")
_PageWaitNum_Type = Gauge32
_PageWaitNum_Object = MibScalar
pageWaitNum = _PageWaitNum_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 6),
    _PageWaitNum_Type()
)
pageWaitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pageWaitNum.setStatus("mandatory")
_SwapActive_Type = Gauge32
_SwapActive_Object = MibScalar
swapActive = _SwapActive_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 7),
    _SwapActive_Type()
)
swapActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapActive.setStatus("mandatory")
_SleepActive_Type = Gauge32
_SleepActive_Object = MibScalar
sleepActive = _SleepActive_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 8),
    _SleepActive_Type()
)
sleepActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleepActive.setStatus("mandatory")
_MemInUse_Type = Gauge32
_MemInUse_Object = MibScalar
memInUse = _MemInUse_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 9),
    _MemInUse_Type()
)
memInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memInUse.setStatus("mandatory")
_ActiveMem_Type = Gauge32
_ActiveMem_Object = MibScalar
activeMem = _ActiveMem_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 10),
    _ActiveMem_Type()
)
activeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeMem.setStatus("mandatory")
_NumProcs_Type = Gauge32
_NumProcs_Object = MibScalar
numProcs = _NumProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 11),
    _NumProcs_Type()
)
numProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numProcs.setStatus("mandatory")
_NumOpenFiles_Type = Gauge32
_NumOpenFiles_Object = MibScalar
numOpenFiles = _NumOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 12),
    _NumOpenFiles_Type()
)
numOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOpenFiles.setStatus("mandatory")
_SwapInUse_Type = Gauge32
_SwapInUse_Object = MibScalar
swapInUse = _SwapInUse_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 13),
    _SwapInUse_Type()
)
swapInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapInUse.setStatus("mandatory")
_NumSwitches_Type = Counter32
_NumSwitches_Object = MibScalar
numSwitches = _NumSwitches_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 14),
    _NumSwitches_Type()
)
numSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numSwitches.setStatus("mandatory")
_NumTraps_Type = Counter32
_NumTraps_Object = MibScalar
numTraps = _NumTraps_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 15),
    _NumTraps_Type()
)
numTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numTraps.setStatus("mandatory")
_NumSyscalls_Type = Counter32
_NumSyscalls_Object = MibScalar
numSyscalls = _NumSyscalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 16),
    _NumSyscalls_Type()
)
numSyscalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numSyscalls.setStatus("mandatory")
_NumInterrupts_Type = Counter32
_NumInterrupts_Object = MibScalar
numInterrupts = _NumInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 17),
    _NumInterrupts_Type()
)
numInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numInterrupts.setStatus("mandatory")
_NumPageSwapIns_Type = Counter32
_NumPageSwapIns_Object = MibScalar
numPageSwapIns = _NumPageSwapIns_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 18),
    _NumPageSwapIns_Type()
)
numPageSwapIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPageSwapIns.setStatus("mandatory")
_NumPageSwapOuts_Type = Counter32
_NumPageSwapOuts_Object = MibScalar
numPageSwapOuts = _NumPageSwapOuts_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 19),
    _NumPageSwapOuts_Type()
)
numPageSwapOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPageSwapOuts.setStatus("mandatory")
_NumSwapIns_Type = Counter32
_NumSwapIns_Object = MibScalar
numSwapIns = _NumSwapIns_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 20),
    _NumSwapIns_Type()
)
numSwapIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numSwapIns.setStatus("mandatory")
_NumSwapOuts_Type = Counter32
_NumSwapOuts_Object = MibScalar
numSwapOuts = _NumSwapOuts_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 21),
    _NumSwapOuts_Type()
)
numSwapOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numSwapOuts.setStatus("mandatory")
_NumPageIns_Type = Counter32
_NumPageIns_Object = MibScalar
numPageIns = _NumPageIns_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 22),
    _NumPageIns_Type()
)
numPageIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPageIns.setStatus("mandatory")
_NumPageOuts_Type = Counter32
_NumPageOuts_Object = MibScalar
numPageOuts = _NumPageOuts_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 23),
    _NumPageOuts_Type()
)
numPageOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPageOuts.setStatus("mandatory")
_NumPageReclaims_Type = Counter32
_NumPageReclaims_Object = MibScalar
numPageReclaims = _NumPageReclaims_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 24),
    _NumPageReclaims_Type()
)
numPageReclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPageReclaims.setStatus("mandatory")
_NumPageFaults_Type = Counter32
_NumPageFaults_Object = MibScalar
numPageFaults = _NumPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 25),
    _NumPageFaults_Type()
)
numPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPageFaults.setStatus("mandatory")
_LoadAverage1Min_Type = Integer32
_LoadAverage1Min_Object = MibScalar
loadAverage1Min = _LoadAverage1Min_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 26),
    _LoadAverage1Min_Type()
)
loadAverage1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadAverage1Min.setStatus("mandatory")
_LoadAverage5Min_Type = Integer32
_LoadAverage5Min_Object = MibScalar
loadAverage5Min = _LoadAverage5Min_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 27),
    _LoadAverage5Min_Type()
)
loadAverage5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadAverage5Min.setStatus("mandatory")
_LoadAverage15Min_Type = Integer32
_LoadAverage15Min_Object = MibScalar
loadAverage15Min = _LoadAverage15Min_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 28),
    _LoadAverage15Min_Type()
)
loadAverage15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadAverage15Min.setStatus("mandatory")
_TotalSwapSpace_Type = Integer32
_TotalSwapSpace_Object = MibScalar
totalSwapSpace = _TotalSwapSpace_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 29),
    _TotalSwapSpace_Type()
)
totalSwapSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSwapSpace.setStatus("mandatory")


class _SwapCapacity_Type(Integer32):
    """Custom type swapCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwapCapacity_Type.__name__ = "Integer32"
_SwapCapacity_Object = MibScalar
swapCapacity = _SwapCapacity_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 30),
    _SwapCapacity_Type()
)
swapCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapCapacity.setStatus("mandatory")


class _MemCapacity_Type(Integer32):
    """Custom type memCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MemCapacity_Type.__name__ = "Integer32"
_MemCapacity_Object = MibScalar
memCapacity = _MemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 31),
    _MemCapacity_Type()
)
memCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCapacity.setStatus("mandatory")


class _MemInUseCapacity_Type(Integer32):
    """Custom type memInUseCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MemInUseCapacity_Type.__name__ = "Integer32"
_MemInUseCapacity_Object = MibScalar
memInUseCapacity = _MemInUseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 32),
    _MemInUseCapacity_Type()
)
memInUseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memInUseCapacity.setStatus("mandatory")
_PageScans_Type = Counter32
_PageScans_Object = MibScalar
pageScans = _PageScans_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 33),
    _PageScans_Type()
)
pageScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pageScans.setStatus("mandatory")
_NumZombieProcs_Type = Gauge32
_NumZombieProcs_Object = MibScalar
numZombieProcs = _NumZombieProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 7, 8, 34),
    _NumZombieProcs_Type()
)
numZombieProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numZombieProcs.setStatus("mandatory")
_ErrorTable_Object = MibTable
errorTable = _ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8)
)
if mibBuilder.loadTexts:
    errorTable.setStatus("deprecated")
_ErrorEntry_Object = MibTableRow
errorEntry = _ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1)
)
errorEntry.setIndexNames(
    (0, "EMPIRE", "seqNum"),
)
if mibBuilder.loadTexts:
    errorEntry.setStatus("deprecated")
_SeqNum_Type = Integer32
_SeqNum_Object = MibTableColumn
seqNum = _SeqNum_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 1),
    _SeqNum_Type()
)
seqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seqNum.setStatus("deprecated")
_Mid_Type = Integer32
_Mid_Object = MibTableColumn
mid = _Mid_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 2),
    _Mid_Type()
)
mid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mid.setStatus("deprecated")
_Sid_Type = Integer32
_Sid_Object = MibTableColumn
sid = _Sid_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 3),
    _Sid_Type()
)
sid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sid.setStatus("deprecated")
_Time_Type = TimeTicks
_Time_Object = MibTableColumn
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 4),
    _Time_Type()
)
time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    time.setStatus("deprecated")
_Tag_Type = Integer32
_Tag_Object = MibTableColumn
tag = _Tag_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 5),
    _Tag_Type()
)
tag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tag.setStatus("deprecated")
_Type_Type = DisplayString
_Type_Object = MibTableColumn
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 6),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("deprecated")
_Cause_Type = DisplayString
_Cause_Object = MibTableColumn
cause = _Cause_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 7),
    _Cause_Type()
)
cause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cause.setStatus("deprecated")
_Severity_Type = DisplayString
_Severity_Object = MibTableColumn
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 8),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("deprecated")
_Level_Type = DisplayString
_Level_Object = MibTableColumn
level = _Level_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 9),
    _Level_Type()
)
level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    level.setStatus("deprecated")
_Module_Type = DisplayString
_Module_Object = MibTableColumn
module = _Module_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 10),
    _Module_Type()
)
module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    module.setStatus("deprecated")
_SubSysmsg_Type = DisplayString
_SubSysmsg_Object = MibTableColumn
subSysmsg = _SubSysmsg_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 11),
    _SubSysmsg_Type()
)
subSysmsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSysmsg.setStatus("deprecated")


class _ErrDelete_Type(Integer32):
    """Custom type errDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("valid", 2))
    )


_ErrDelete_Type.__name__ = "Integer32"
_ErrDelete_Object = MibTableColumn
errDelete = _ErrDelete_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 8, 1, 12),
    _ErrDelete_Type()
)
errDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errDelete.setStatus("deprecated")
_Ipc_ObjectIdentity = ObjectIdentity
ipc = _Ipc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9)
)
_MsgqueTable_Object = MibTable
msgqueTable = _MsgqueTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    msgqueTable.setStatus("mandatory")
_MsgqueEntry_Object = MibTableRow
msgqueEntry = _MsgqueEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1)
)
msgqueEntry.setIndexNames(
    (0, "EMPIRE", "queID"),
)
if mibBuilder.loadTexts:
    msgqueEntry.setStatus("mandatory")
_QueID_Type = Integer32
_QueID_Object = MibTableColumn
queID = _QueID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 1),
    _QueID_Type()
)
queID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queID.setStatus("mandatory")
_QueKey_Type = DisplayString
_QueKey_Object = MibTableColumn
queKey = _QueKey_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 2),
    _QueKey_Type()
)
queKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queKey.setStatus("mandatory")
_QueMode_Type = DisplayString
_QueMode_Object = MibTableColumn
queMode = _QueMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 3),
    _QueMode_Type()
)
queMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queMode.setStatus("mandatory")
_QueOwner_Type = DisplayString
_QueOwner_Object = MibTableColumn
queOwner = _QueOwner_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 4),
    _QueOwner_Type()
)
queOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOwner.setStatus("mandatory")
_QueGroup_Type = DisplayString
_QueGroup_Object = MibTableColumn
queGroup = _QueGroup_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 5),
    _QueGroup_Type()
)
queGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queGroup.setStatus("mandatory")
_QueNBytes_Type = Gauge32
_QueNBytes_Object = MibTableColumn
queNBytes = _QueNBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 6),
    _QueNBytes_Type()
)
queNBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queNBytes.setStatus("mandatory")
_QueNMesg_Type = Gauge32
_QueNMesg_Object = MibTableColumn
queNMesg = _QueNMesg_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 7),
    _QueNMesg_Type()
)
queNMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queNMesg.setStatus("mandatory")


class _QueDel_Type(Integer32):
    """Custom type queDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("valid", 2))
    )


_QueDel_Type.__name__ = "Integer32"
_QueDel_Object = MibTableColumn
queDel = _QueDel_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 1, 1, 8),
    _QueDel_Type()
)
queDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queDel.setStatus("mandatory")
_ShmemTable_Object = MibTable
shmemTable = _ShmemTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    shmemTable.setStatus("mandatory")
_ShmemEntry_Object = MibTableRow
shmemEntry = _ShmemEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1)
)
shmemEntry.setIndexNames(
    (0, "EMPIRE", "shmemID"),
)
if mibBuilder.loadTexts:
    shmemEntry.setStatus("mandatory")
_ShmemID_Type = Integer32
_ShmemID_Object = MibTableColumn
shmemID = _ShmemID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 1),
    _ShmemID_Type()
)
shmemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemID.setStatus("mandatory")
_ShmemKey_Type = DisplayString
_ShmemKey_Object = MibTableColumn
shmemKey = _ShmemKey_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 2),
    _ShmemKey_Type()
)
shmemKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemKey.setStatus("mandatory")
_ShmemMode_Type = DisplayString
_ShmemMode_Object = MibTableColumn
shmemMode = _ShmemMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 3),
    _ShmemMode_Type()
)
shmemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemMode.setStatus("mandatory")
_ShmemOwner_Type = DisplayString
_ShmemOwner_Object = MibTableColumn
shmemOwner = _ShmemOwner_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 4),
    _ShmemOwner_Type()
)
shmemOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemOwner.setStatus("mandatory")
_ShmemGroup_Type = DisplayString
_ShmemGroup_Object = MibTableColumn
shmemGroup = _ShmemGroup_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 5),
    _ShmemGroup_Type()
)
shmemGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemGroup.setStatus("mandatory")
_ShmemSegSz_Type = Integer32
_ShmemSegSz_Object = MibTableColumn
shmemSegSz = _ShmemSegSz_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 6),
    _ShmemSegSz_Type()
)
shmemSegSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemSegSz.setStatus("mandatory")
_ShmemNLcks_Type = Integer32
_ShmemNLcks_Object = MibTableColumn
shmemNLcks = _ShmemNLcks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 7),
    _ShmemNLcks_Type()
)
shmemNLcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shmemNLcks.setStatus("mandatory")


class _ShmemDel_Type(Integer32):
    """Custom type shmemDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("valid", 2))
    )


_ShmemDel_Type.__name__ = "Integer32"
_ShmemDel_Object = MibTableColumn
shmemDel = _ShmemDel_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 2, 1, 8),
    _ShmemDel_Type()
)
shmemDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shmemDel.setStatus("mandatory")
_SemTable_Object = MibTable
semTable = _SemTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3)
)
if mibBuilder.loadTexts:
    semTable.setStatus("mandatory")
_SemEntry_Object = MibTableRow
semEntry = _SemEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1)
)
semEntry.setIndexNames(
    (0, "EMPIRE", "semID"),
)
if mibBuilder.loadTexts:
    semEntry.setStatus("mandatory")
_SemID_Type = Integer32
_SemID_Object = MibTableColumn
semID = _SemID_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1, 1),
    _SemID_Type()
)
semID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semID.setStatus("mandatory")
_SemKey_Type = DisplayString
_SemKey_Object = MibTableColumn
semKey = _SemKey_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1, 2),
    _SemKey_Type()
)
semKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semKey.setStatus("mandatory")
_SemMode_Type = DisplayString
_SemMode_Object = MibTableColumn
semMode = _SemMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1, 3),
    _SemMode_Type()
)
semMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semMode.setStatus("mandatory")
_SemOwner_Type = DisplayString
_SemOwner_Object = MibTableColumn
semOwner = _SemOwner_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1, 4),
    _SemOwner_Type()
)
semOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semOwner.setStatus("mandatory")
_SemGroup_Type = DisplayString
_SemGroup_Object = MibTableColumn
semGroup = _SemGroup_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1, 5),
    _SemGroup_Type()
)
semGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semGroup.setStatus("mandatory")
_SemNsems_Type = Integer32
_SemNsems_Object = MibTableColumn
semNsems = _SemNsems_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1, 6),
    _SemNsems_Type()
)
semNsems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    semNsems.setStatus("mandatory")


class _SemDel_Type(Integer32):
    """Custom type semDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("valid", 2))
    )


_SemDel_Type.__name__ = "Integer32"
_SemDel_Object = MibTableColumn
semDel = _SemDel_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 9, 3, 1, 7),
    _SemDel_Type()
)
semDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    semDel.setStatus("mandatory")
_Buffers_ObjectIdentity = ObjectIdentity
buffers = _Buffers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10)
)
_Mbufs_ObjectIdentity = ObjectIdentity
mbufs = _Mbufs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1)
)
_NumMbufs_Type = Gauge32
_NumMbufs_Object = MibScalar
numMbufs = _NumMbufs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 1),
    _NumMbufs_Type()
)
numMbufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numMbufs.setStatus("mandatory")
_NumClusters_Type = Gauge32
_NumClusters_Object = MibScalar
numClusters = _NumClusters_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 2),
    _NumClusters_Type()
)
numClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numClusters.setStatus("mandatory")
_FreeClusters_Type = Gauge32
_FreeClusters_Object = MibScalar
freeClusters = _FreeClusters_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 3),
    _FreeClusters_Type()
)
freeClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeClusters.setStatus("mandatory")
_NumDrops_Type = Counter32
_NumDrops_Object = MibScalar
numDrops = _NumDrops_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 4),
    _NumDrops_Type()
)
numDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDrops.setStatus("mandatory")
_NumWaits_Type = Counter32
_NumWaits_Object = MibScalar
numWaits = _NumWaits_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 5),
    _NumWaits_Type()
)
numWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numWaits.setStatus("mandatory")
_NumDrains_Type = Counter32
_NumDrains_Object = MibScalar
numDrains = _NumDrains_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 6),
    _NumDrains_Type()
)
numDrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDrains.setStatus("mandatory")
_MbufAllocTable_Object = MibTable
mbufAllocTable = _MbufAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 7)
)
if mibBuilder.loadTexts:
    mbufAllocTable.setStatus("mandatory")
_MbufAllocEntry_Object = MibTableRow
mbufAllocEntry = _MbufAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 7, 1)
)
mbufAllocEntry.setIndexNames(
    (0, "EMPIRE", "mbufType"),
)
if mibBuilder.loadTexts:
    mbufAllocEntry.setStatus("mandatory")
_MbufType_Type = Integer32
_MbufType_Object = MibTableColumn
mbufType = _MbufType_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 7, 1, 1),
    _MbufType_Type()
)
mbufType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufType.setStatus("mandatory")
_MbufDesc_Type = DisplayString
_MbufDesc_Object = MibTableColumn
mbufDesc = _MbufDesc_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 7, 1, 2),
    _MbufDesc_Type()
)
mbufDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufDesc.setStatus("mandatory")
_MbufAlloc_Type = Gauge32
_MbufAlloc_Object = MibTableColumn
mbufAlloc = _MbufAlloc_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 1, 7, 1, 3),
    _MbufAlloc_Type()
)
mbufAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbufAlloc.setStatus("mandatory")
_Strbufs_ObjectIdentity = ObjectIdentity
strbufs = _Strbufs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2)
)
_StrbufAllocTable_Object = MibTable
strbufAllocTable = _StrbufAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    strbufAllocTable.setStatus("mandatory")
_StrbufAllocEntry_Object = MibTableRow
strbufAllocEntry = _StrbufAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1, 1)
)
strbufAllocEntry.setIndexNames(
    (0, "EMPIRE", "strbufAllocIndex"),
)
if mibBuilder.loadTexts:
    strbufAllocEntry.setStatus("mandatory")
_StrbufAllocIndex_Type = Integer32
_StrbufAllocIndex_Object = MibTableColumn
strbufAllocIndex = _StrbufAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1, 1, 1),
    _StrbufAllocIndex_Type()
)
strbufAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strbufAllocIndex.setStatus("mandatory")
_StrbufAllocSize_Type = Integer32
_StrbufAllocSize_Object = MibTableColumn
strbufAllocSize = _StrbufAllocSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1, 1, 2),
    _StrbufAllocSize_Type()
)
strbufAllocSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strbufAllocSize.setStatus("mandatory")
_StrbufAllocCurrent_Type = Gauge32
_StrbufAllocCurrent_Object = MibTableColumn
strbufAllocCurrent = _StrbufAllocCurrent_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1, 1, 3),
    _StrbufAllocCurrent_Type()
)
strbufAllocCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strbufAllocCurrent.setStatus("mandatory")
_StrbufAllocMaxs_Type = Integer32
_StrbufAllocMaxs_Object = MibTableColumn
strbufAllocMaxs = _StrbufAllocMaxs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1, 1, 4),
    _StrbufAllocMaxs_Type()
)
strbufAllocMaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strbufAllocMaxs.setStatus("mandatory")
_StrbufAllocTotals_Type = Counter32
_StrbufAllocTotals_Object = MibTableColumn
strbufAllocTotals = _StrbufAllocTotals_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1, 1, 5),
    _StrbufAllocTotals_Type()
)
strbufAllocTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strbufAllocTotals.setStatus("mandatory")
_StrbufAllocFails_Type = Counter32
_StrbufAllocFails_Object = MibTableColumn
strbufAllocFails = _StrbufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 2, 1, 1, 6),
    _StrbufAllocFails_Type()
)
strbufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strbufAllocFails.setStatus("mandatory")
_IoBufferCache_ObjectIdentity = ObjectIdentity
ioBufferCache = _IoBufferCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3)
)
_NumBreadRequests_Type = Counter32
_NumBreadRequests_Object = MibScalar
numBreadRequests = _NumBreadRequests_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 1),
    _NumBreadRequests_Type()
)
numBreadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBreadRequests.setStatus("mandatory")
_NumBreadHits_Type = Counter32
_NumBreadHits_Object = MibScalar
numBreadHits = _NumBreadHits_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 2),
    _NumBreadHits_Type()
)
numBreadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBreadHits.setStatus("mandatory")
_NumBufSleeps_Type = Counter32
_NumBufSleeps_Object = MibScalar
numBufSleeps = _NumBufSleeps_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 3),
    _NumBufSleeps_Type()
)
numBufSleeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBufSleeps.setStatus("mandatory")
_NumAgeAllocs_Type = Counter32
_NumAgeAllocs_Object = MibScalar
numAgeAllocs = _NumAgeAllocs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 4),
    _NumAgeAllocs_Type()
)
numAgeAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numAgeAllocs.setStatus("mandatory")
_NumLRUAllocs_Type = Counter32
_NumLRUAllocs_Object = MibScalar
numLRUAllocs = _NumLRUAllocs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 5),
    _NumLRUAllocs_Type()
)
numLRUAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numLRUAllocs.setStatus("mandatory")
_MinNumBufHdrs_Type = Gauge32
_MinNumBufHdrs_Object = MibScalar
minNumBufHdrs = _MinNumBufHdrs_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 6),
    _MinNumBufHdrs_Type()
)
minNumBufHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minNumBufHdrs.setStatus("mandatory")
_NumAllocBuf_Type = Gauge32
_NumAllocBuf_Object = MibScalar
numAllocBuf = _NumAllocBuf_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 7),
    _NumAllocBuf_Type()
)
numAllocBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numAllocBuf.setStatus("mandatory")


class _IoBufferHitRate_Type(Integer32):
    """Custom type ioBufferHitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoBufferHitRate_Type.__name__ = "Integer32"
_IoBufferHitRate_Object = MibScalar
ioBufferHitRate = _IoBufferHitRate_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 10, 3, 8),
    _IoBufferHitRate_Type()
)
ioBufferHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioBufferHitRate.setStatus("mandatory")
_Dnlc_ObjectIdentity = ObjectIdentity
dnlc = _Dnlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11)
)
_DnlcHits_Type = Counter32
_DnlcHits_Object = MibScalar
dnlcHits = _DnlcHits_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 1),
    _DnlcHits_Type()
)
dnlcHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcHits.setStatus("mandatory")
_DnlcMisses_Type = Counter32
_DnlcMisses_Object = MibScalar
dnlcMisses = _DnlcMisses_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 2),
    _DnlcMisses_Type()
)
dnlcMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcMisses.setStatus("mandatory")
_DnlcEnters_Type = Counter32
_DnlcEnters_Object = MibScalar
dnlcEnters = _DnlcEnters_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 3),
    _DnlcEnters_Type()
)
dnlcEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcEnters.setStatus("mandatory")
_DnlcDblEnters_Type = Counter32
_DnlcDblEnters_Object = MibScalar
dnlcDblEnters = _DnlcDblEnters_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 4),
    _DnlcDblEnters_Type()
)
dnlcDblEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcDblEnters.setStatus("mandatory")
_DnlcLongEnters_Type = Counter32
_DnlcLongEnters_Object = MibScalar
dnlcLongEnters = _DnlcLongEnters_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 5),
    _DnlcLongEnters_Type()
)
dnlcLongEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcLongEnters.setStatus("mandatory")
_DnlcLongLooks_Type = Counter32
_DnlcLongLooks_Object = MibScalar
dnlcLongLooks = _DnlcLongLooks_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 6),
    _DnlcLongLooks_Type()
)
dnlcLongLooks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcLongLooks.setStatus("mandatory")
_DnlcLruEmpty_Type = Counter32
_DnlcLruEmpty_Object = MibScalar
dnlcLruEmpty = _DnlcLruEmpty_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 7),
    _DnlcLruEmpty_Type()
)
dnlcLruEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcLruEmpty.setStatus("mandatory")
_DnlcPurges_Type = Counter32
_DnlcPurges_Object = MibScalar
dnlcPurges = _DnlcPurges_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 8),
    _DnlcPurges_Type()
)
dnlcPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcPurges.setStatus("mandatory")


class _DnlcHitRate_Type(Integer32):
    """Custom type dnlcHitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DnlcHitRate_Type.__name__ = "Integer32"
_DnlcHitRate_Object = MibScalar
dnlcHitRate = _DnlcHitRate_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 9),
    _DnlcHitRate_Type()
)
dnlcHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcHitRate.setStatus("mandatory")
_DnlcCacheSize_Type = Integer32
_DnlcCacheSize_Object = MibScalar
dnlcCacheSize = _DnlcCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 11, 10),
    _DnlcCacheSize_Type()
)
dnlcCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnlcCacheSize.setStatus("mandatory")
_Dos_ObjectIdentity = ObjectIdentity
dos = _Dos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 2)
)
_Os2_ObjectIdentity = ObjectIdentity
os2 = _Os2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 3)
)
_Windows_ObjectIdentity = ObjectIdentity
windows = _Windows_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 4)
)
_Nt_ObjectIdentity = ObjectIdentity
nt = _Nt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5)
)
_NtSystem_ObjectIdentity = ObjectIdentity
ntSystem = _NtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 1)
)
_NtSystemVersion_Type = DisplayString
_NtSystemVersion_Object = MibScalar
ntSystemVersion = _NtSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 1),
    _NtSystemVersion_Type()
)
ntSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSystemVersion.setStatus("mandatory")
_NtBuildNumber_Type = Integer32
_NtBuildNumber_Object = MibScalar
ntBuildNumber = _NtBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 2),
    _NtBuildNumber_Type()
)
ntBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntBuildNumber.setStatus("mandatory")
_NtServicePackNumber_Type = Integer32
_NtServicePackNumber_Object = MibScalar
ntServicePackNumber = _NtServicePackNumber_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 3),
    _NtServicePackNumber_Type()
)
ntServicePackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServicePackNumber.setStatus("mandatory")


class _NtWorkstationOrServer_Type(Integer32):
    """Custom type ntWorkstationOrServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("unknown", 3),
          ("workstation", 2))
    )


_NtWorkstationOrServer_Type.__name__ = "Integer32"
_NtWorkstationOrServer_Object = MibScalar
ntWorkstationOrServer = _NtWorkstationOrServer_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 4),
    _NtWorkstationOrServer_Type()
)
ntWorkstationOrServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWorkstationOrServer.setStatus("mandatory")


class _NtfsDisable8dot3NameCreation_Type(Integer32):
    """Custom type ntfsDisable8dot3NameCreation based on Integer32"""
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


_NtfsDisable8dot3NameCreation_Type.__name__ = "Integer32"
_NtfsDisable8dot3NameCreation_Object = MibScalar
ntfsDisable8dot3NameCreation = _NtfsDisable8dot3NameCreation_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 5),
    _NtfsDisable8dot3NameCreation_Type()
)
ntfsDisable8dot3NameCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntfsDisable8dot3NameCreation.setStatus("mandatory")


class _NtWin31FileSystem_Type(Integer32):
    """Custom type ntWin31FileSystem based on Integer32"""
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


_NtWin31FileSystem_Type.__name__ = "Integer32"
_NtWin31FileSystem_Object = MibScalar
ntWin31FileSystem = _NtWin31FileSystem_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 6),
    _NtWin31FileSystem_Type()
)
ntWin31FileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWin31FileSystem.setStatus("mandatory")
_NtCriticalSectTimeout_Type = Integer32
_NtCriticalSectTimeout_Object = MibScalar
ntCriticalSectTimeout = _NtCriticalSectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 7),
    _NtCriticalSectTimeout_Type()
)
ntCriticalSectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCriticalSectTimeout.setStatus("mandatory")
_NtGlobalFlag_Type = Integer32
_NtGlobalFlag_Object = MibScalar
ntGlobalFlag = _NtGlobalFlag_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 8),
    _NtGlobalFlag_Type()
)
ntGlobalFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntGlobalFlag.setStatus("mandatory")
_NtIoPageLockLimit_Type = Integer32
_NtIoPageLockLimit_Object = MibScalar
ntIoPageLockLimit = _NtIoPageLockLimit_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 9),
    _NtIoPageLockLimit_Type()
)
ntIoPageLockLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntIoPageLockLimit.setStatus("mandatory")
_NtLargeSystemCache_Type = Integer32
_NtLargeSystemCache_Object = MibScalar
ntLargeSystemCache = _NtLargeSystemCache_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 10),
    _NtLargeSystemCache_Type()
)
ntLargeSystemCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLargeSystemCache.setStatus("mandatory")
_NtPagedPoolSize_Type = Integer32
_NtPagedPoolSize_Object = MibScalar
ntPagedPoolSize = _NtPagedPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 11),
    _NtPagedPoolSize_Type()
)
ntPagedPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPagedPoolSize.setStatus("mandatory")
_NtNonPagedPoolSize_Type = Integer32
_NtNonPagedPoolSize_Object = MibScalar
ntNonPagedPoolSize = _NtNonPagedPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 12),
    _NtNonPagedPoolSize_Type()
)
ntNonPagedPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntNonPagedPoolSize.setStatus("mandatory")
_NtPagingFiles_Type = DisplayString
_NtPagingFiles_Object = MibScalar
ntPagingFiles = _NtPagingFiles_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 13),
    _NtPagingFiles_Type()
)
ntPagingFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPagingFiles.setStatus("mandatory")
_NtSystemPages_Type = Integer32
_NtSystemPages_Object = MibScalar
ntSystemPages = _NtSystemPages_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 14),
    _NtSystemPages_Type()
)
ntSystemPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSystemPages.setStatus("mandatory")
_NtOptionalSubsystem_Type = DisplayString
_NtOptionalSubsystem_Object = MibScalar
ntOptionalSubsystem = _NtOptionalSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 15),
    _NtOptionalSubsystem_Type()
)
ntOptionalSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntOptionalSubsystem.setStatus("mandatory")
_NtCmdlineOptions_Type = DisplayString
_NtCmdlineOptions_Object = MibScalar
ntCmdlineOptions = _NtCmdlineOptions_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 16),
    _NtCmdlineOptions_Type()
)
ntCmdlineOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCmdlineOptions.setStatus("mandatory")
_NtLPTTimeout_Type = Integer32
_NtLPTTimeout_Object = MibScalar
ntLPTTimeout = _NtLPTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 17),
    _NtLPTTimeout_Type()
)
ntLPTTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLPTTimeout.setStatus("mandatory")
_NtDosMemSize_Type = Integer32
_NtDosMemSize_Object = MibScalar
ntDosMemSize = _NtDosMemSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 18),
    _NtDosMemSize_Type()
)
ntDosMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntDosMemSize.setStatus("mandatory")
_NtWowCmdline_Type = DisplayString
_NtWowCmdline_Object = MibScalar
ntWowCmdline = _NtWowCmdline_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 19),
    _NtWowCmdline_Type()
)
ntWowCmdline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWowCmdline.setStatus("mandatory")
_NtWowSize_Type = Integer32
_NtWowSize_Object = MibScalar
ntWowSize = _NtWowSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 20),
    _NtWowSize_Type()
)
ntWowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWowSize.setStatus("mandatory")


class _NtUserFullScreen_Type(Integer32):
    """Custom type ntUserFullScreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fullscreen", 1),
          ("windowed", 0))
    )


_NtUserFullScreen_Type.__name__ = "Integer32"
_NtUserFullScreen_Object = MibScalar
ntUserFullScreen = _NtUserFullScreen_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 21),
    _NtUserFullScreen_Type()
)
ntUserFullScreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntUserFullScreen.setStatus("mandatory")
_NtHistoryBufferSize_Type = Integer32
_NtHistoryBufferSize_Object = MibScalar
ntHistoryBufferSize = _NtHistoryBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 22),
    _NtHistoryBufferSize_Type()
)
ntHistoryBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntHistoryBufferSize.setStatus("mandatory")
_NtNumberHistoryBuffers_Type = Integer32
_NtNumberHistoryBuffers_Object = MibScalar
ntNumberHistoryBuffers = _NtNumberHistoryBuffers_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 23),
    _NtNumberHistoryBuffers_Type()
)
ntNumberHistoryBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntNumberHistoryBuffers.setStatus("mandatory")


class _NtQuickEdit_Type(Integer32):
    """Custom type ntQuickEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtQuickEdit_Type.__name__ = "Integer32"
_NtQuickEdit_Object = MibScalar
ntQuickEdit = _NtQuickEdit_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 24),
    _NtQuickEdit_Type()
)
ntQuickEdit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntQuickEdit.setStatus("mandatory")
_NtScreenBufferSize_Type = DisplayString
_NtScreenBufferSize_Object = MibScalar
ntScreenBufferSize = _NtScreenBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 25),
    _NtScreenBufferSize_Type()
)
ntScreenBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntScreenBufferSize.setStatus("mandatory")
_NtWindowSize_Type = DisplayString
_NtWindowSize_Object = MibScalar
ntWindowSize = _NtWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 26),
    _NtWindowSize_Type()
)
ntWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWindowSize.setStatus("mandatory")
_NtWindowsAppInitDLLs_Type = DisplayString
_NtWindowsAppInitDLLs_Object = MibScalar
ntWindowsAppInitDLLs = _NtWindowsAppInitDLLs_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 27),
    _NtWindowsAppInitDLLs_Type()
)
ntWindowsAppInitDLLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWindowsAppInitDLLs.setStatus("mandatory")
_NtWindowsDeviceNotSelectedTimeout_Type = Integer32
_NtWindowsDeviceNotSelectedTimeout_Object = MibScalar
ntWindowsDeviceNotSelectedTimeout = _NtWindowsDeviceNotSelectedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 28),
    _NtWindowsDeviceNotSelectedTimeout_Type()
)
ntWindowsDeviceNotSelectedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWindowsDeviceNotSelectedTimeout.setStatus("mandatory")


class _NtWindowsSpooler_Type(Integer32):
    """Custom type ntWindowsSpooler based on Integer32"""
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


_NtWindowsSpooler_Type.__name__ = "Integer32"
_NtWindowsSpooler_Object = MibScalar
ntWindowsSpooler = _NtWindowsSpooler_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 29),
    _NtWindowsSpooler_Type()
)
ntWindowsSpooler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWindowsSpooler.setStatus("mandatory")
_NtWindowsSwapDisk_Type = DisplayString
_NtWindowsSwapDisk_Object = MibScalar
ntWindowsSwapDisk = _NtWindowsSwapDisk_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 30),
    _NtWindowsSwapDisk_Type()
)
ntWindowsSwapDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWindowsSwapDisk.setStatus("mandatory")
_NtWindowsXmitRetryTimeout_Type = Integer32
_NtWindowsXmitRetryTimeout_Object = MibScalar
ntWindowsXmitRetryTimeout = _NtWindowsXmitRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 31),
    _NtWindowsXmitRetryTimeout_Type()
)
ntWindowsXmitRetryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWindowsXmitRetryTimeout.setStatus("mandatory")
_NtSystemRoot_Type = DisplayString
_NtSystemRoot_Object = MibScalar
ntSystemRoot = _NtSystemRoot_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 32),
    _NtSystemRoot_Type()
)
ntSystemRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSystemRoot.setStatus("mandatory")


class _NtBuildType_Type(Integer32):
    """Custom type ntBuildType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiprocessor", 2),
          ("uniprocessor", 1),
          ("unknown", 3))
    )


_NtBuildType_Type.__name__ = "Integer32"
_NtBuildType_Object = MibScalar
ntBuildType = _NtBuildType_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 33),
    _NtBuildType_Type()
)
ntBuildType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntBuildType.setStatus("mandatory")
_NtSysStartOptions_Type = DisplayString
_NtSysStartOptions_Object = MibScalar
ntSysStartOptions = _NtSysStartOptions_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 34),
    _NtSysStartOptions_Type()
)
ntSysStartOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysStartOptions.setStatus("mandatory")
_NtSysBiosDate_Type = DisplayString
_NtSysBiosDate_Object = MibScalar
ntSysBiosDate = _NtSysBiosDate_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 35),
    _NtSysBiosDate_Type()
)
ntSysBiosDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysBiosDate.setStatus("mandatory")
_NtSysBiosVersion_Type = DisplayString
_NtSysBiosVersion_Object = MibScalar
ntSysBiosVersion = _NtSysBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 36),
    _NtSysBiosVersion_Type()
)
ntSysBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysBiosVersion.setStatus("mandatory")
_NtVideoResolution_Type = DisplayString
_NtVideoResolution_Object = MibScalar
ntVideoResolution = _NtVideoResolution_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 37),
    _NtVideoResolution_Type()
)
ntVideoResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntVideoResolution.setStatus("mandatory")


class _NtCrashDumpEnabled_Type(Integer32):
    """Custom type ntCrashDumpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", 2))
    )


_NtCrashDumpEnabled_Type.__name__ = "Integer32"
_NtCrashDumpEnabled_Object = MibScalar
ntCrashDumpEnabled = _NtCrashDumpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 38),
    _NtCrashDumpEnabled_Type()
)
ntCrashDumpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCrashDumpEnabled.setStatus("mandatory")


class _NtLogEvent_Type(Integer32):
    """Custom type ntLogEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", 2))
    )


_NtLogEvent_Type.__name__ = "Integer32"
_NtLogEvent_Object = MibScalar
ntLogEvent = _NtLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 39),
    _NtLogEvent_Type()
)
ntLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLogEvent.setStatus("mandatory")


class _NtOverwrite_Type(Integer32):
    """Custom type ntOverwrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", 2))
    )


_NtOverwrite_Type.__name__ = "Integer32"
_NtOverwrite_Object = MibScalar
ntOverwrite = _NtOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 40),
    _NtOverwrite_Type()
)
ntOverwrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntOverwrite.setStatus("mandatory")


class _NtSendAlert_Type(Integer32):
    """Custom type ntSendAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("unknown", 2))
    )


_NtSendAlert_Type.__name__ = "Integer32"
_NtSendAlert_Object = MibScalar
ntSendAlert = _NtSendAlert_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 41),
    _NtSendAlert_Type()
)
ntSendAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSendAlert.setStatus("mandatory")


class _NtIsClustered_Type(Integer32):
    """Custom type ntIsClustered based on Integer32"""
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


_NtIsClustered_Type.__name__ = "Integer32"
_NtIsClustered_Object = MibScalar
ntIsClustered = _NtIsClustered_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 42),
    _NtIsClustered_Type()
)
ntIsClustered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntIsClustered.setStatus("mandatory")
_NtClusterName_Type = DisplayString
_NtClusterName_Object = MibScalar
ntClusterName = _NtClusterName_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 43),
    _NtClusterName_Type()
)
ntClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntClusterName.setStatus("mandatory")
_NtClusterMembers_Type = DisplayString
_NtClusterMembers_Object = MibScalar
ntClusterMembers = _NtClusterMembers_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 44),
    _NtClusterMembers_Type()
)
ntClusterMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntClusterMembers.setStatus("mandatory")


class _NtClusterIsActive_Type(Integer32):
    """Custom type ntClusterIsActive based on Integer32"""
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


_NtClusterIsActive_Type.__name__ = "Integer32"
_NtClusterIsActive_Object = MibScalar
ntClusterIsActive = _NtClusterIsActive_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 45),
    _NtClusterIsActive_Type()
)
ntClusterIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntClusterIsActive.setStatus("mandatory")
_NtClusterActiveNode_Type = DisplayString
_NtClusterActiveNode_Object = MibScalar
ntClusterActiveNode = _NtClusterActiveNode_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 1, 46),
    _NtClusterActiveNode_Type()
)
ntClusterActiveNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntClusterActiveNode.setStatus("mandatory")
_NtThreads_ObjectIdentity = ObjectIdentity
ntThreads = _NtThreads_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 2)
)
_NtThreadTable_Object = MibTable
ntThreadTable = _NtThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ntThreadTable.setStatus("mandatory")
_NtThreadEntry_Object = MibTableRow
ntThreadEntry = _NtThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1)
)
ntThreadEntry.setIndexNames(
    (0, "EMPIRE", "ntThreadPID"),
    (0, "EMPIRE", "ntThreadNumber"),
)
if mibBuilder.loadTexts:
    ntThreadEntry.setStatus("mandatory")
_NtThreadPID_Type = Integer32
_NtThreadPID_Object = MibTableColumn
ntThreadPID = _NtThreadPID_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 1),
    _NtThreadPID_Type()
)
ntThreadPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadPID.setStatus("mandatory")
_NtThreadNumber_Type = Integer32
_NtThreadNumber_Object = MibTableColumn
ntThreadNumber = _NtThreadNumber_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 2),
    _NtThreadNumber_Type()
)
ntThreadNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadNumber.setStatus("mandatory")
_NtThreadPrivTime_Type = Counter32
_NtThreadPrivTime_Object = MibTableColumn
ntThreadPrivTime = _NtThreadPrivTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 3),
    _NtThreadPrivTime_Type()
)
ntThreadPrivTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadPrivTime.setStatus("mandatory")
_NtThreadProcTime_Type = Counter32
_NtThreadProcTime_Object = MibTableColumn
ntThreadProcTime = _NtThreadProcTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 4),
    _NtThreadProcTime_Type()
)
ntThreadProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadProcTime.setStatus("mandatory")
_NtThreadUserTime_Type = Counter32
_NtThreadUserTime_Object = MibTableColumn
ntThreadUserTime = _NtThreadUserTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 5),
    _NtThreadUserTime_Type()
)
ntThreadUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadUserTime.setStatus("mandatory")
_NtThreadContextSwitches_Type = Counter32
_NtThreadContextSwitches_Object = MibTableColumn
ntThreadContextSwitches = _NtThreadContextSwitches_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 6),
    _NtThreadContextSwitches_Type()
)
ntThreadContextSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadContextSwitches.setStatus("mandatory")
_NtThreadElapsedTime_Type = Integer32
_NtThreadElapsedTime_Object = MibTableColumn
ntThreadElapsedTime = _NtThreadElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 7),
    _NtThreadElapsedTime_Type()
)
ntThreadElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadElapsedTime.setStatus("mandatory")
_NtThreadPriorityBase_Type = Gauge32
_NtThreadPriorityBase_Object = MibTableColumn
ntThreadPriorityBase = _NtThreadPriorityBase_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 8),
    _NtThreadPriorityBase_Type()
)
ntThreadPriorityBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadPriorityBase.setStatus("mandatory")
_NtThreadPriority_Type = Gauge32
_NtThreadPriority_Object = MibTableColumn
ntThreadPriority = _NtThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 9),
    _NtThreadPriority_Type()
)
ntThreadPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadPriority.setStatus("mandatory")


class _NtThreadWaitReason_Type(Integer32):
    """Custom type ntThreadWaitReason based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("executionDelay", 4),
          ("executionDelay1", 11),
          ("suspended", 5),
          ("suspended1", 12),
          ("waitForEventPairHigh", 14),
          ("waitForEventPairLow", 15),
          ("waitForExecutive", 0),
          ("waitForExecutive1", 7),
          ("waitForFreePage", 1),
          ("waitForFreePage1", 8),
          ("waitForLPCRecv", 16),
          ("waitForLPCReply", 17),
          ("waitForPageIn", 2),
          ("waitForPageIn1", 9),
          ("waitForPageOut", 19),
          ("waitForPoolAlloc", 3),
          ("waitForPoolAlloc1", 10),
          ("waitForUserRequest", 6),
          ("waitForUserRequest1", 13),
          ("waitForVmem", 18))
    )


_NtThreadWaitReason_Type.__name__ = "Integer32"
_NtThreadWaitReason_Object = MibTableColumn
ntThreadWaitReason = _NtThreadWaitReason_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 10),
    _NtThreadWaitReason_Type()
)
ntThreadWaitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadWaitReason.setStatus("mandatory")
_NtThreadStartAddr_Type = Integer32
_NtThreadStartAddr_Object = MibTableColumn
ntThreadStartAddr = _NtThreadStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 11),
    _NtThreadStartAddr_Type()
)
ntThreadStartAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadStartAddr.setStatus("mandatory")


class _NtThreadState_Type(Integer32):
    """Custom type ntThreadState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 0),
          ("ready", 1),
          ("running", 2),
          ("standby", 3),
          ("terminated", 4),
          ("transition", 6),
          ("unknown", 7),
          ("wait", 5))
    )


_NtThreadState_Type.__name__ = "Integer32"
_NtThreadState_Object = MibTableColumn
ntThreadState = _NtThreadState_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 12),
    _NtThreadState_Type()
)
ntThreadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadState.setStatus("mandatory")
_NtThreadID_Type = Integer32
_NtThreadID_Object = MibTableColumn
ntThreadID = _NtThreadID_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 2, 1, 1, 13),
    _NtThreadID_Type()
)
ntThreadID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntThreadID.setStatus("mandatory")
_NtRegistry_ObjectIdentity = ObjectIdentity
ntRegistry = _NtRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 3)
)
_NtRegistryCurrentSize_Type = Integer32
_NtRegistryCurrentSize_Object = MibScalar
ntRegistryCurrentSize = _NtRegistryCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 3, 1),
    _NtRegistryCurrentSize_Type()
)
ntRegistryCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegistryCurrentSize.setStatus("mandatory")
_NtRegistrySizeLimit_Type = Integer32
_NtRegistrySizeLimit_Object = MibScalar
ntRegistrySizeLimit = _NtRegistrySizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 3, 2),
    _NtRegistrySizeLimit_Type()
)
ntRegistrySizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegistrySizeLimit.setStatus("mandatory")
_NtServices_ObjectIdentity = ObjectIdentity
ntServices = _NtServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 4)
)
_NtServiceTable_Object = MibTable
ntServiceTable = _NtServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1)
)
if mibBuilder.loadTexts:
    ntServiceTable.setStatus("mandatory")
_NtServiceEntry_Object = MibTableRow
ntServiceEntry = _NtServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1)
)
ntServiceEntry.setIndexNames(
    (0, "EMPIRE", "ntServiceIndex"),
)
if mibBuilder.loadTexts:
    ntServiceEntry.setStatus("mandatory")
_NtServiceIndex_Type = Integer32
_NtServiceIndex_Object = MibTableColumn
ntServiceIndex = _NtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1, 1),
    _NtServiceIndex_Type()
)
ntServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServiceIndex.setStatus("mandatory")
_NtServiceName_Type = DisplayString
_NtServiceName_Object = MibTableColumn
ntServiceName = _NtServiceName_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1, 2),
    _NtServiceName_Type()
)
ntServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServiceName.setStatus("mandatory")
_NtServicePathName_Type = DisplayString
_NtServicePathName_Object = MibTableColumn
ntServicePathName = _NtServicePathName_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1, 3),
    _NtServicePathName_Type()
)
ntServicePathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServicePathName.setStatus("mandatory")


class _NtServiceStartType_Type(Integer32):
    """Custom type ntServiceStartType based on Integer32"""
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
        *(("automatic", 1),
          ("disabled", 3),
          ("manual", 2),
          ("other", 4))
    )


_NtServiceStartType_Type.__name__ = "Integer32"
_NtServiceStartType_Object = MibTableColumn
ntServiceStartType = _NtServiceStartType_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1, 4),
    _NtServiceStartType_Type()
)
ntServiceStartType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntServiceStartType.setStatus("mandatory")
_NtServiceParameters_Type = DisplayString
_NtServiceParameters_Object = MibTableColumn
ntServiceParameters = _NtServiceParameters_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1, 5),
    _NtServiceParameters_Type()
)
ntServiceParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServiceParameters.setStatus("mandatory")


class _NtServiceState_Type(Integer32):
    """Custom type ntServiceState based on Integer32"""
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
        *(("notRunning", 2),
          ("other", 4),
          ("paused", 3),
          ("running", 1))
    )


_NtServiceState_Type.__name__ = "Integer32"
_NtServiceState_Object = MibTableColumn
ntServiceState = _NtServiceState_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1, 6),
    _NtServiceState_Type()
)
ntServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntServiceState.setStatus("mandatory")
_NtServiceObjectName_Type = DisplayString
_NtServiceObjectName_Object = MibTableColumn
ntServiceObjectName = _NtServiceObjectName_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 4, 1, 1, 7),
    _NtServiceObjectName_Type()
)
ntServiceObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntServiceObjectName.setStatus("mandatory")
_NtPerformance_ObjectIdentity = ObjectIdentity
ntPerformance = _NtPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 5)
)
_NtSystemPerf_ObjectIdentity = ObjectIdentity
ntSystemPerf = _NtSystemPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1)
)
_NtTotalPrivTime_Type = Counter32
_NtTotalPrivTime_Object = MibScalar
ntTotalPrivTime = _NtTotalPrivTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 1),
    _NtTotalPrivTime_Type()
)
ntTotalPrivTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTotalPrivTime.setStatus("mandatory")
_NtTotalProcessorTime_Type = Counter32
_NtTotalProcessorTime_Object = MibScalar
ntTotalProcessorTime = _NtTotalProcessorTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 2),
    _NtTotalProcessorTime_Type()
)
ntTotalProcessorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTotalProcessorTime.setStatus("mandatory")
_NtTotalUserTime_Type = Counter32
_NtTotalUserTime_Object = MibScalar
ntTotalUserTime = _NtTotalUserTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 3),
    _NtTotalUserTime_Type()
)
ntTotalUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTotalUserTime.setStatus("mandatory")
_NtAlignFixups_Type = Counter32
_NtAlignFixups_Object = MibScalar
ntAlignFixups = _NtAlignFixups_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 4),
    _NtAlignFixups_Type()
)
ntAlignFixups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAlignFixups.setStatus("mandatory")
_NtContextSwitches_Type = Counter32
_NtContextSwitches_Object = MibScalar
ntContextSwitches = _NtContextSwitches_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 5),
    _NtContextSwitches_Type()
)
ntContextSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntContextSwitches.setStatus("mandatory")
_NtExceptionDispatches_Type = Counter32
_NtExceptionDispatches_Object = MibScalar
ntExceptionDispatches = _NtExceptionDispatches_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 6),
    _NtExceptionDispatches_Type()
)
ntExceptionDispatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntExceptionDispatches.setStatus("mandatory")
_NtFileCtrlKBytes_Type = Counter32
_NtFileCtrlKBytes_Object = MibScalar
ntFileCtrlKBytes = _NtFileCtrlKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 7),
    _NtFileCtrlKBytes_Type()
)
ntFileCtrlKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileCtrlKBytes.setStatus("mandatory")
_NtFileCtrlOps_Type = Counter32
_NtFileCtrlOps_Object = MibScalar
ntFileCtrlOps = _NtFileCtrlOps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 8),
    _NtFileCtrlOps_Type()
)
ntFileCtrlOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileCtrlOps.setStatus("mandatory")
_NtFileDataOps_Type = Counter32
_NtFileDataOps_Object = MibScalar
ntFileDataOps = _NtFileDataOps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 9),
    _NtFileDataOps_Type()
)
ntFileDataOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFileDataOps.setStatus("mandatory")
_NtReadKBytes_Type = Counter32
_NtReadKBytes_Object = MibScalar
ntReadKBytes = _NtReadKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 10),
    _NtReadKBytes_Type()
)
ntReadKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntReadKBytes.setStatus("mandatory")
_NtReadOps_Type = Counter32
_NtReadOps_Object = MibScalar
ntReadOps = _NtReadOps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 11),
    _NtReadOps_Type()
)
ntReadOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntReadOps.setStatus("mandatory")
_NtWriteKBytes_Type = Counter32
_NtWriteKBytes_Object = MibScalar
ntWriteKBytes = _NtWriteKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 12),
    _NtWriteKBytes_Type()
)
ntWriteKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWriteKBytes.setStatus("mandatory")
_NtWriteOps_Type = Counter32
_NtWriteOps_Object = MibScalar
ntWriteOps = _NtWriteOps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 13),
    _NtWriteOps_Type()
)
ntWriteOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWriteOps.setStatus("mandatory")
_NtFloatEmuls_Type = Counter32
_NtFloatEmuls_Object = MibScalar
ntFloatEmuls = _NtFloatEmuls_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 14),
    _NtFloatEmuls_Type()
)
ntFloatEmuls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFloatEmuls.setStatus("mandatory")
_NtRunQLen_Type = Gauge32
_NtRunQLen_Object = MibScalar
ntRunQLen = _NtRunQLen_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 15),
    _NtRunQLen_Type()
)
ntRunQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRunQLen.setStatus("mandatory")
_NtSystemCalls_Type = Counter32
_NtSystemCalls_Object = MibScalar
ntSystemCalls = _NtSystemCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 16),
    _NtSystemCalls_Type()
)
ntSystemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSystemCalls.setStatus("mandatory")
_NtInterrupts_Type = Counter32
_NtInterrupts_Object = MibScalar
ntInterrupts = _NtInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 1, 17),
    _NtInterrupts_Type()
)
ntInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntInterrupts.setStatus("mandatory")
_NtCachePerf_ObjectIdentity = ObjectIdentity
ntCachePerf = _NtCachePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2)
)
_NtAsyncCopyReads_Type = Counter32
_NtAsyncCopyReads_Object = MibScalar
ntAsyncCopyReads = _NtAsyncCopyReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 1),
    _NtAsyncCopyReads_Type()
)
ntAsyncCopyReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAsyncCopyReads.setStatus("mandatory")
_NtAsyncDataMaps_Type = Counter32
_NtAsyncDataMaps_Object = MibScalar
ntAsyncDataMaps = _NtAsyncDataMaps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 2),
    _NtAsyncDataMaps_Type()
)
ntAsyncDataMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAsyncDataMaps.setStatus("mandatory")
_NtAsyncFastReads_Type = Counter32
_NtAsyncFastReads_Object = MibScalar
ntAsyncFastReads = _NtAsyncFastReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 3),
    _NtAsyncFastReads_Type()
)
ntAsyncFastReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAsyncFastReads.setStatus("mandatory")
_NtAsyncMDLReads_Type = Counter32
_NtAsyncMDLReads_Object = MibScalar
ntAsyncMDLReads = _NtAsyncMDLReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 4),
    _NtAsyncMDLReads_Type()
)
ntAsyncMDLReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAsyncMDLReads.setStatus("mandatory")
_NtAsyncPinReads_Type = Counter32
_NtAsyncPinReads_Object = MibScalar
ntAsyncPinReads = _NtAsyncPinReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 5),
    _NtAsyncPinReads_Type()
)
ntAsyncPinReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAsyncPinReads.setStatus("mandatory")
_NtCopyReadHits_Type = Counter32
_NtCopyReadHits_Object = MibScalar
ntCopyReadHits = _NtCopyReadHits_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 6),
    _NtCopyReadHits_Type()
)
ntCopyReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCopyReadHits.setStatus("mandatory")
_NtCopyReads_Type = Counter32
_NtCopyReads_Object = MibScalar
ntCopyReads = _NtCopyReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 7),
    _NtCopyReads_Type()
)
ntCopyReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCopyReads.setStatus("mandatory")
_NtDataFlushPages_Type = Counter32
_NtDataFlushPages_Object = MibScalar
ntDataFlushPages = _NtDataFlushPages_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 8),
    _NtDataFlushPages_Type()
)
ntDataFlushPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntDataFlushPages.setStatus("mandatory")
_NtDataFlushes_Type = Counter32
_NtDataFlushes_Object = MibScalar
ntDataFlushes = _NtDataFlushes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 9),
    _NtDataFlushes_Type()
)
ntDataFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntDataFlushes.setStatus("mandatory")
_NtDataMapHits_Type = Counter32
_NtDataMapHits_Object = MibScalar
ntDataMapHits = _NtDataMapHits_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 10),
    _NtDataMapHits_Type()
)
ntDataMapHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntDataMapHits.setStatus("mandatory")
_NtDataMapPins_Type = Counter32
_NtDataMapPins_Object = MibScalar
ntDataMapPins = _NtDataMapPins_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 11),
    _NtDataMapPins_Type()
)
ntDataMapPins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntDataMapPins.setStatus("mandatory")
_NtDataMaps_Type = Counter32
_NtDataMaps_Object = MibScalar
ntDataMaps = _NtDataMaps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 12),
    _NtDataMaps_Type()
)
ntDataMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntDataMaps.setStatus("mandatory")
_NtFastReadNotPossible_Type = Counter32
_NtFastReadNotPossible_Object = MibScalar
ntFastReadNotPossible = _NtFastReadNotPossible_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 13),
    _NtFastReadNotPossible_Type()
)
ntFastReadNotPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFastReadNotPossible.setStatus("mandatory")
_NtFastReadResourceMisses_Type = Counter32
_NtFastReadResourceMisses_Object = MibScalar
ntFastReadResourceMisses = _NtFastReadResourceMisses_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 14),
    _NtFastReadResourceMisses_Type()
)
ntFastReadResourceMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFastReadResourceMisses.setStatus("mandatory")
_NtFastReads_Type = Counter32
_NtFastReads_Object = MibScalar
ntFastReads = _NtFastReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 15),
    _NtFastReads_Type()
)
ntFastReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFastReads.setStatus("mandatory")
_NtLazyWriteFlushes_Type = Counter32
_NtLazyWriteFlushes_Object = MibScalar
ntLazyWriteFlushes = _NtLazyWriteFlushes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 16),
    _NtLazyWriteFlushes_Type()
)
ntLazyWriteFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLazyWriteFlushes.setStatus("mandatory")
_NtLazyWritePages_Type = Counter32
_NtLazyWritePages_Object = MibScalar
ntLazyWritePages = _NtLazyWritePages_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 17),
    _NtLazyWritePages_Type()
)
ntLazyWritePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLazyWritePages.setStatus("mandatory")
_NtMDLReadHits_Type = Counter32
_NtMDLReadHits_Object = MibScalar
ntMDLReadHits = _NtMDLReadHits_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 18),
    _NtMDLReadHits_Type()
)
ntMDLReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntMDLReadHits.setStatus("mandatory")
_NtMDLReads_Type = Counter32
_NtMDLReads_Object = MibScalar
ntMDLReads = _NtMDLReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 19),
    _NtMDLReads_Type()
)
ntMDLReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntMDLReads.setStatus("mandatory")
_NtPinReadHits_Type = Counter32
_NtPinReadHits_Object = MibScalar
ntPinReadHits = _NtPinReadHits_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 20),
    _NtPinReadHits_Type()
)
ntPinReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPinReadHits.setStatus("mandatory")
_NtPinReads_Type = Counter32
_NtPinReads_Object = MibScalar
ntPinReads = _NtPinReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 21),
    _NtPinReads_Type()
)
ntPinReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPinReads.setStatus("mandatory")
_NtSyncCopyReads_Type = Counter32
_NtSyncCopyReads_Object = MibScalar
ntSyncCopyReads = _NtSyncCopyReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 22),
    _NtSyncCopyReads_Type()
)
ntSyncCopyReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSyncCopyReads.setStatus("mandatory")
_NtSyncDataMaps_Type = Counter32
_NtSyncDataMaps_Object = MibScalar
ntSyncDataMaps = _NtSyncDataMaps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 23),
    _NtSyncDataMaps_Type()
)
ntSyncDataMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSyncDataMaps.setStatus("mandatory")
_NtSyncFastReads_Type = Counter32
_NtSyncFastReads_Object = MibScalar
ntSyncFastReads = _NtSyncFastReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 24),
    _NtSyncFastReads_Type()
)
ntSyncFastReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSyncFastReads.setStatus("mandatory")
_NtSyncMDLReads_Type = Counter32
_NtSyncMDLReads_Object = MibScalar
ntSyncMDLReads = _NtSyncMDLReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 25),
    _NtSyncMDLReads_Type()
)
ntSyncMDLReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSyncMDLReads.setStatus("mandatory")
_NtSyncPinReads_Type = Counter32
_NtSyncPinReads_Object = MibScalar
ntSyncPinReads = _NtSyncPinReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 2, 26),
    _NtSyncPinReads_Type()
)
ntSyncPinReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSyncPinReads.setStatus("mandatory")
_NtMemoryPerf_ObjectIdentity = ObjectIdentity
ntMemoryPerf = _NtMemoryPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3)
)
_NtAvailKBytes_Type = Gauge32
_NtAvailKBytes_Object = MibScalar
ntAvailKBytes = _NtAvailKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 1),
    _NtAvailKBytes_Type()
)
ntAvailKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntAvailKBytes.setStatus("mandatory")
_NtCacheKBytes_Type = Gauge32
_NtCacheKBytes_Object = MibScalar
ntCacheKBytes = _NtCacheKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 2),
    _NtCacheKBytes_Type()
)
ntCacheKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCacheKBytes.setStatus("mandatory")
_NtCacheKBytesPeak_Type = Integer32
_NtCacheKBytesPeak_Object = MibScalar
ntCacheKBytesPeak = _NtCacheKBytesPeak_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 3),
    _NtCacheKBytesPeak_Type()
)
ntCacheKBytesPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCacheKBytesPeak.setStatus("mandatory")
_NtCacheFaults_Type = Counter32
_NtCacheFaults_Object = MibScalar
ntCacheFaults = _NtCacheFaults_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 4),
    _NtCacheFaults_Type()
)
ntCacheFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCacheFaults.setStatus("mandatory")
_NtCommitLimit_Type = Integer32
_NtCommitLimit_Object = MibScalar
ntCommitLimit = _NtCommitLimit_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 5),
    _NtCommitLimit_Type()
)
ntCommitLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCommitLimit.setStatus("mandatory")
_NtCommittedKBytes_Type = Gauge32
_NtCommittedKBytes_Object = MibScalar
ntCommittedKBytes = _NtCommittedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 6),
    _NtCommittedKBytes_Type()
)
ntCommittedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntCommittedKBytes.setStatus("mandatory")
_NtDemandZeroFaults_Type = Counter32
_NtDemandZeroFaults_Object = MibScalar
ntDemandZeroFaults = _NtDemandZeroFaults_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 7),
    _NtDemandZeroFaults_Type()
)
ntDemandZeroFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntDemandZeroFaults.setStatus("mandatory")
_NtFreeSysPageTableEntries_Type = Gauge32
_NtFreeSysPageTableEntries_Object = MibScalar
ntFreeSysPageTableEntries = _NtFreeSysPageTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 8),
    _NtFreeSysPageTableEntries_Type()
)
ntFreeSysPageTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntFreeSysPageTableEntries.setStatus("mandatory")
_NtPageFaults_Type = Counter32
_NtPageFaults_Object = MibScalar
ntPageFaults = _NtPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 9),
    _NtPageFaults_Type()
)
ntPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPageFaults.setStatus("mandatory")
_NtPageReads_Type = Counter32
_NtPageReads_Object = MibScalar
ntPageReads = _NtPageReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 10),
    _NtPageReads_Type()
)
ntPageReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPageReads.setStatus("mandatory")
_NtPageWrites_Type = Counter32
_NtPageWrites_Object = MibScalar
ntPageWrites = _NtPageWrites_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 11),
    _NtPageWrites_Type()
)
ntPageWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPageWrites.setStatus("mandatory")
_NtPagesInput_Type = Counter32
_NtPagesInput_Object = MibScalar
ntPagesInput = _NtPagesInput_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 12),
    _NtPagesInput_Type()
)
ntPagesInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPagesInput.setStatus("mandatory")
_NtPagesOutput_Type = Counter32
_NtPagesOutput_Object = MibScalar
ntPagesOutput = _NtPagesOutput_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 13),
    _NtPagesOutput_Type()
)
ntPagesOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPagesOutput.setStatus("mandatory")
_NtPages_Type = Counter32
_NtPages_Object = MibScalar
ntPages = _NtPages_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 14),
    _NtPages_Type()
)
ntPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPages.setStatus("mandatory")
_NtPoolNonPagedAllocs_Type = Gauge32
_NtPoolNonPagedAllocs_Object = MibScalar
ntPoolNonPagedAllocs = _NtPoolNonPagedAllocs_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 15),
    _NtPoolNonPagedAllocs_Type()
)
ntPoolNonPagedAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPoolNonPagedAllocs.setStatus("mandatory")
_NtPoolNonPagedKBytes_Type = Gauge32
_NtPoolNonPagedKBytes_Object = MibScalar
ntPoolNonPagedKBytes = _NtPoolNonPagedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 16),
    _NtPoolNonPagedKBytes_Type()
)
ntPoolNonPagedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPoolNonPagedKBytes.setStatus("mandatory")
_NtPoolPagedAllocs_Type = Gauge32
_NtPoolPagedAllocs_Object = MibScalar
ntPoolPagedAllocs = _NtPoolPagedAllocs_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 17),
    _NtPoolPagedAllocs_Type()
)
ntPoolPagedAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPoolPagedAllocs.setStatus("mandatory")
_NtPoolPagedKBytes_Type = Gauge32
_NtPoolPagedKBytes_Object = MibScalar
ntPoolPagedKBytes = _NtPoolPagedKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 18),
    _NtPoolPagedKBytes_Type()
)
ntPoolPagedKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPoolPagedKBytes.setStatus("mandatory")
_NtPagedResidentKBytes_Type = Gauge32
_NtPagedResidentKBytes_Object = MibScalar
ntPagedResidentKBytes = _NtPagedResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 19),
    _NtPagedResidentKBytes_Type()
)
ntPagedResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPagedResidentKBytes.setStatus("mandatory")
_NtSysCacheResidentKBytes_Type = Gauge32
_NtSysCacheResidentKBytes_Object = MibScalar
ntSysCacheResidentKBytes = _NtSysCacheResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 20),
    _NtSysCacheResidentKBytes_Type()
)
ntSysCacheResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysCacheResidentKBytes.setStatus("mandatory")
_NtSysCodeResidentKBytes_Type = Gauge32
_NtSysCodeResidentKBytes_Object = MibScalar
ntSysCodeResidentKBytes = _NtSysCodeResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 21),
    _NtSysCodeResidentKBytes_Type()
)
ntSysCodeResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysCodeResidentKBytes.setStatus("mandatory")
_NtSysCodeTotalKBytes_Type = Gauge32
_NtSysCodeTotalKBytes_Object = MibScalar
ntSysCodeTotalKBytes = _NtSysCodeTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 22),
    _NtSysCodeTotalKBytes_Type()
)
ntSysCodeTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysCodeTotalKBytes.setStatus("mandatory")
_NtSysDriverResidentKBytes_Type = Gauge32
_NtSysDriverResidentKBytes_Object = MibScalar
ntSysDriverResidentKBytes = _NtSysDriverResidentKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 23),
    _NtSysDriverResidentKBytes_Type()
)
ntSysDriverResidentKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysDriverResidentKBytes.setStatus("mandatory")
_NtSysDriverTotalKBytes_Type = Gauge32
_NtSysDriverTotalKBytes_Object = MibScalar
ntSysDriverTotalKBytes = _NtSysDriverTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 24),
    _NtSysDriverTotalKBytes_Type()
)
ntSysDriverTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntSysDriverTotalKBytes.setStatus("mandatory")
_NtTransitionFaults_Type = Counter32
_NtTransitionFaults_Object = MibScalar
ntTransitionFaults = _NtTransitionFaults_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 25),
    _NtTransitionFaults_Type()
)
ntTransitionFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTransitionFaults.setStatus("mandatory")
_NtWriteCopies_Type = Counter32
_NtWriteCopies_Object = MibScalar
ntWriteCopies = _NtWriteCopies_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 3, 26),
    _NtWriteCopies_Type()
)
ntWriteCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWriteCopies.setStatus("mandatory")
_NtPageFilePerf_ObjectIdentity = ObjectIdentity
ntPageFilePerf = _NtPageFilePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 4)
)


class _NtPageFileUsage_Type(Integer32):
    """Custom type ntPageFileUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtPageFileUsage_Type.__name__ = "Integer32"
_NtPageFileUsage_Object = MibScalar
ntPageFileUsage = _NtPageFileUsage_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 4, 1),
    _NtPageFileUsage_Type()
)
ntPageFileUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPageFileUsage.setStatus("mandatory")


class _NtPageFilePeakUsage_Type(Integer32):
    """Custom type ntPageFilePeakUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtPageFilePeakUsage_Type.__name__ = "Integer32"
_NtPageFilePeakUsage_Object = MibScalar
ntPageFilePeakUsage = _NtPageFilePeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 5, 4, 2),
    _NtPageFilePeakUsage_Type()
)
ntPageFilePeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntPageFilePeakUsage.setStatus("mandatory")
_NtEvents_ObjectIdentity = ObjectIdentity
ntEvents = _NtEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 6)
)
_NtEventApplicationCount_Type = Counter32
_NtEventApplicationCount_Object = MibScalar
ntEventApplicationCount = _NtEventApplicationCount_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 1),
    _NtEventApplicationCount_Type()
)
ntEventApplicationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventApplicationCount.setStatus("mandatory")
_NtEventSecurityCount_Type = Counter32
_NtEventSecurityCount_Object = MibScalar
ntEventSecurityCount = _NtEventSecurityCount_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 2),
    _NtEventSecurityCount_Type()
)
ntEventSecurityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventSecurityCount.setStatus("mandatory")
_NtEventSystemCount_Type = Counter32
_NtEventSystemCount_Object = MibScalar
ntEventSystemCount = _NtEventSystemCount_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 3),
    _NtEventSystemCount_Type()
)
ntEventSystemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventSystemCount.setStatus("mandatory")
_NtEventMonTable_Object = MibTable
ntEventMonTable = _NtEventMonTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4)
)
if mibBuilder.loadTexts:
    ntEventMonTable.setStatus("mandatory")
_NtEventMonEntry_Object = MibTableRow
ntEventMonEntry = _NtEventMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1)
)
ntEventMonEntry.setIndexNames(
    (0, "EMPIRE", "ntEventMonIndex"),
)
if mibBuilder.loadTexts:
    ntEventMonEntry.setStatus("mandatory")


class _NtEventMonIndex_Type(Integer32):
    """Custom type ntEventMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtEventMonIndex_Type.__name__ = "Integer32"
_NtEventMonIndex_Object = MibTableColumn
ntEventMonIndex = _NtEventMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 1),
    _NtEventMonIndex_Type()
)
ntEventMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMonIndex.setStatus("mandatory")


class _NtEventMonLog_Type(Integer32):
    """Custom type ntEventMonLog based on Integer32"""
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
        *(("application", 1),
          ("dirService", 5),
          ("dnsServer", 4),
          ("fileRepService", 6),
          ("security", 2),
          ("system", 3))
    )


_NtEventMonLog_Type.__name__ = "Integer32"
_NtEventMonLog_Object = MibTableColumn
ntEventMonLog = _NtEventMonLog_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 2),
    _NtEventMonLog_Type()
)
ntEventMonLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonLog.setStatus("mandatory")
_NtEventMonTime_Type = TimeTicks
_NtEventMonTime_Object = MibTableColumn
ntEventMonTime = _NtEventMonTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 3),
    _NtEventMonTime_Type()
)
ntEventMonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMonTime.setStatus("mandatory")
_NtEventMonTraps_Type = Integer32
_NtEventMonTraps_Object = MibTableColumn
ntEventMonTraps = _NtEventMonTraps_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 4),
    _NtEventMonTraps_Type()
)
ntEventMonTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMonTraps.setStatus("mandatory")


class _NtEventMonTypeLastMatch_Type(Integer32):
    """Custom type ntEventMonTypeLastMatch based on Integer32"""
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
        *(("error", 1),
          ("failure", 5),
          ("information", 3),
          ("noMatch", 6),
          ("success", 4),
          ("warning", 2))
    )


_NtEventMonTypeLastMatch_Type.__name__ = "Integer32"
_NtEventMonTypeLastMatch_Object = MibTableColumn
ntEventMonTypeLastMatch = _NtEventMonTypeLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 5),
    _NtEventMonTypeLastMatch_Type()
)
ntEventMonTypeLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMonTypeLastMatch.setStatus("mandatory")


class _NtEventMonTypeFilter_Type(Integer32):
    """Custom type ntEventMonTypeFilter based on Integer32"""
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
        *(("all", 6),
          ("error", 1),
          ("failure", 5),
          ("information", 3),
          ("success", 4),
          ("warning", 2))
    )


_NtEventMonTypeFilter_Type.__name__ = "Integer32"
_NtEventMonTypeFilter_Object = MibTableColumn
ntEventMonTypeFilter = _NtEventMonTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 6),
    _NtEventMonTypeFilter_Type()
)
ntEventMonTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonTypeFilter.setStatus("mandatory")


class _NtEventMonSrcLastMatch_Type(DisplayString):
    """Custom type ntEventMonSrcLastMatch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtEventMonSrcLastMatch_Type.__name__ = "DisplayString"
_NtEventMonSrcLastMatch_Object = MibTableColumn
ntEventMonSrcLastMatch = _NtEventMonSrcLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 7),
    _NtEventMonSrcLastMatch_Type()
)
ntEventMonSrcLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMonSrcLastMatch.setStatus("mandatory")


class _NtEventMonSrcFilter_Type(DisplayString):
    """Custom type ntEventMonSrcFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtEventMonSrcFilter_Type.__name__ = "DisplayString"
_NtEventMonSrcFilter_Object = MibTableColumn
ntEventMonSrcFilter = _NtEventMonSrcFilter_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 8),
    _NtEventMonSrcFilter_Type()
)
ntEventMonSrcFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonSrcFilter.setStatus("mandatory")


class _NtEventMonDescLastMatch_Type(DisplayString):
    """Custom type ntEventMonDescLastMatch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_NtEventMonDescLastMatch_Type.__name__ = "DisplayString"
_NtEventMonDescLastMatch_Object = MibTableColumn
ntEventMonDescLastMatch = _NtEventMonDescLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 9),
    _NtEventMonDescLastMatch_Type()
)
ntEventMonDescLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMonDescLastMatch.setStatus("mandatory")


class _NtEventMonDescFilter_Type(DisplayString):
    """Custom type ntEventMonDescFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtEventMonDescFilter_Type.__name__ = "DisplayString"
_NtEventMonDescFilter_Object = MibTableColumn
ntEventMonDescFilter = _NtEventMonDescFilter_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 10),
    _NtEventMonDescFilter_Type()
)
ntEventMonDescFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonDescFilter.setStatus("mandatory")


class _NtEventMonStatus_Type(Integer32):
    """Custom type ntEventMonStatus based on Integer32"""
    defaultValue = 5

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_NtEventMonStatus_Type.__name__ = "Integer32"
_NtEventMonStatus_Object = MibTableColumn
ntEventMonStatus = _NtEventMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 11),
    _NtEventMonStatus_Type()
)
ntEventMonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonStatus.setStatus("mandatory")


class _NtEventMonDescr_Type(DisplayString):
    """Custom type ntEventMonDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NtEventMonDescr_Type.__name__ = "DisplayString"
_NtEventMonDescr_Object = MibTableColumn
ntEventMonDescr = _NtEventMonDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 12),
    _NtEventMonDescr_Type()
)
ntEventMonDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonDescr.setStatus("mandatory")


class _NtEventMonAction_Type(DisplayString):
    """Custom type ntEventMonAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NtEventMonAction_Type.__name__ = "DisplayString"
_NtEventMonAction_Object = MibTableColumn
ntEventMonAction = _NtEventMonAction_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 13),
    _NtEventMonAction_Type()
)
ntEventMonAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonAction.setStatus("mandatory")
_NtEventMonFlags_Type = Integer32
_NtEventMonFlags_Object = MibTableColumn
ntEventMonFlags = _NtEventMonFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 14),
    _NtEventMonFlags_Type()
)
ntEventMonFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMonFlags.setStatus("mandatory")
_NtEventMonMatches_Type = Counter32
_NtEventMonMatches_Object = MibTableColumn
ntEventMonMatches = _NtEventMonMatches_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 4, 1, 15),
    _NtEventMonMatches_Type()
)
ntEventMonMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMonMatches.setStatus("mandatory")
_NtEventApplicationMaxSize_Type = Gauge32
_NtEventApplicationMaxSize_Object = MibScalar
ntEventApplicationMaxSize = _NtEventApplicationMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 5),
    _NtEventApplicationMaxSize_Type()
)
ntEventApplicationMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventApplicationMaxSize.setStatus("mandatory")
_NtEventApplicationRetention_Type = Gauge32
_NtEventApplicationRetention_Object = MibScalar
ntEventApplicationRetention = _NtEventApplicationRetention_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 6),
    _NtEventApplicationRetention_Type()
)
ntEventApplicationRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventApplicationRetention.setStatus("mandatory")
_NtEventSecurityMaxSize_Type = Gauge32
_NtEventSecurityMaxSize_Object = MibScalar
ntEventSecurityMaxSize = _NtEventSecurityMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 7),
    _NtEventSecurityMaxSize_Type()
)
ntEventSecurityMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventSecurityMaxSize.setStatus("mandatory")
_NtEventSecurityRetention_Type = Gauge32
_NtEventSecurityRetention_Object = MibScalar
ntEventSecurityRetention = _NtEventSecurityRetention_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 8),
    _NtEventSecurityRetention_Type()
)
ntEventSecurityRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventSecurityRetention.setStatus("mandatory")
_NtEventSystemMaxSize_Type = Gauge32
_NtEventSystemMaxSize_Object = MibScalar
ntEventSystemMaxSize = _NtEventSystemMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 9),
    _NtEventSystemMaxSize_Type()
)
ntEventSystemMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventSystemMaxSize.setStatus("mandatory")
_NtEventSystemRetention_Type = Gauge32
_NtEventSystemRetention_Object = MibScalar
ntEventSystemRetention = _NtEventSystemRetention_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 10),
    _NtEventSystemRetention_Type()
)
ntEventSystemRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventSystemRetention.setStatus("mandatory")


class _NtEventUnusedIndex_Type(Integer32):
    """Custom type ntEventUnusedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtEventUnusedIndex_Type.__name__ = "Integer32"
_NtEventUnusedIndex_Object = MibScalar
ntEventUnusedIndex = _NtEventUnusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 11),
    _NtEventUnusedIndex_Type()
)
ntEventUnusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventUnusedIndex.setStatus("mandatory")
_NtEventMatchDescr_Type = DisplayString
_NtEventMatchDescr_Object = MibScalar
ntEventMatchDescr = _NtEventMatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 12),
    _NtEventMatchDescr_Type()
)
ntEventMatchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntEventMatchDescr.setStatus("mandatory")


class _NtEventMatchIndex_Type(Integer32):
    """Custom type ntEventMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtEventMatchIndex_Type.__name__ = "Integer32"
_NtEventMatchIndex_Object = MibScalar
ntEventMatchIndex = _NtEventMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 6, 13),
    _NtEventMatchIndex_Type()
)
ntEventMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntEventMatchIndex.setStatus("mandatory")
_NtRegPerf_ObjectIdentity = ObjectIdentity
ntRegPerf = _NtRegPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 5, 7)
)


class _NtRegPerfDumpFile_Type(DisplayString):
    """Custom type ntRegPerfDumpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NtRegPerfDumpFile_Type.__name__ = "DisplayString"
_NtRegPerfDumpFile_Object = MibScalar
ntRegPerfDumpFile = _NtRegPerfDumpFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 7, 1),
    _NtRegPerfDumpFile_Type()
)
ntRegPerfDumpFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegPerfDumpFile.setStatus("mandatory")
_NtRegNumberOfThreads_Type = Gauge32
_NtRegNumberOfThreads_Object = MibScalar
ntRegNumberOfThreads = _NtRegNumberOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 546, 5, 7, 2),
    _NtRegNumberOfThreads_Type()
)
ntRegNumberOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntRegNumberOfThreads.setStatus("mandatory")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 6)
)
_MonitorTable_Object = MibTable
monitorTable = _MonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1)
)
if mibBuilder.loadTexts:
    monitorTable.setStatus("mandatory")
_MonitorEntry_Object = MibTableRow
monitorEntry = _MonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1)
)
monitorEntry.setIndexNames(
    (0, "EMPIRE", "monIndex"),
)
if mibBuilder.loadTexts:
    monitorEntry.setStatus("mandatory")


class _MonIndex_Type(Integer32):
    """Custom type monIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MonIndex_Type.__name__ = "Integer32"
_MonIndex_Object = MibTableColumn
monIndex = _MonIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 1),
    _MonIndex_Type()
)
monIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monIndex.setStatus("mandatory")


class _MonDescr_Type(DisplayString):
    """Custom type monDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MonDescr_Type.__name__ = "DisplayString"
_MonDescr_Object = MibTableColumn
monDescr = _MonDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 2),
    _MonDescr_Type()
)
monDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monDescr.setStatus("mandatory")


class _MonInterval_Type(Integer32):
    """Custom type monInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MonInterval_Type.__name__ = "Integer32"
_MonInterval_Object = MibTableColumn
monInterval = _MonInterval_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 3),
    _MonInterval_Type()
)
monInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monInterval.setStatus("mandatory")


class _MonSampleType_Type(Integer32):
    """Custom type monSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_MonSampleType_Type.__name__ = "Integer32"
_MonSampleType_Object = MibTableColumn
monSampleType = _MonSampleType_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 4),
    _MonSampleType_Type()
)
monSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monSampleType.setStatus("mandatory")
_MonOID_Type = ObjectIdentifier
_MonOID_Object = MibTableColumn
monOID = _MonOID_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 5),
    _MonOID_Type()
)
monOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monOID.setStatus("mandatory")
_MonCurrVal_Type = Integer32
_MonCurrVal_Object = MibTableColumn
monCurrVal = _MonCurrVal_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 6),
    _MonCurrVal_Type()
)
monCurrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monCurrVal.setStatus("mandatory")


class _MonOperator_Type(Integer32):
    """Custom type monOperator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 6),
          ("ge", 4),
          ("gt", 2),
          ("le", 5),
          ("lt", 3),
          ("ne", 7),
          ("nop", 1))
    )


_MonOperator_Type.__name__ = "Integer32"
_MonOperator_Object = MibTableColumn
monOperator = _MonOperator_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 7),
    _MonOperator_Type()
)
monOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monOperator.setStatus("mandatory")
_MonValue_Type = Integer32
_MonValue_Object = MibTableColumn
monValue = _MonValue_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 8),
    _MonValue_Type()
)
monValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monValue.setStatus("mandatory")
_MonLastCall_Type = TimeTicks
_MonLastCall_Object = MibTableColumn
monLastCall = _MonLastCall_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 9),
    _MonLastCall_Type()
)
monLastCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLastCall.setStatus("mandatory")
_MonNumTraps_Type = Integer32
_MonNumTraps_Object = MibTableColumn
monNumTraps = _MonNumTraps_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 10),
    _MonNumTraps_Type()
)
monNumTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monNumTraps.setStatus("mandatory")
_MonLastTrap_Type = TimeTicks
_MonLastTrap_Object = MibTableColumn
monLastTrap = _MonLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 11),
    _MonLastTrap_Type()
)
monLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLastTrap.setStatus("mandatory")


class _MonRowStatus_Type(Integer32):
    """Custom type monRowStatus based on Integer32"""
    defaultValue = 5

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_MonRowStatus_Type.__name__ = "Integer32"
_MonRowStatus_Object = MibTableColumn
monRowStatus = _MonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 12),
    _MonRowStatus_Type()
)
monRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monRowStatus.setStatus("mandatory")
_MonMinValue_Type = Integer32
_MonMinValue_Object = MibTableColumn
monMinValue = _MonMinValue_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 13),
    _MonMinValue_Type()
)
monMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monMinValue.setStatus("mandatory")
_MonMaxValue_Type = Integer32
_MonMaxValue_Object = MibTableColumn
monMaxValue = _MonMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 14),
    _MonMaxValue_Type()
)
monMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monMaxValue.setStatus("mandatory")


class _MonAction_Type(DisplayString):
    """Custom type monAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MonAction_Type.__name__ = "DisplayString"
_MonAction_Object = MibTableColumn
monAction = _MonAction_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 15),
    _MonAction_Type()
)
monAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monAction.setStatus("mandatory")
_MonFlags_Type = Integer32
_MonFlags_Object = MibTableColumn
monFlags = _MonFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 1, 1, 16),
    _MonFlags_Type()
)
monFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monFlags.setStatus("mandatory")


class _MonUnusedIndex_Type(Integer32):
    """Custom type monUnusedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MonUnusedIndex_Type.__name__ = "Integer32"
_MonUnusedIndex_Object = MibScalar
monUnusedIndex = _MonUnusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 2),
    _MonUnusedIndex_Type()
)
monUnusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monUnusedIndex.setStatus("mandatory")
_MonMatchDescr_Type = DisplayString
_MonMatchDescr_Object = MibScalar
monMatchDescr = _MonMatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 3),
    _MonMatchDescr_Type()
)
monMatchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monMatchDescr.setStatus("mandatory")


class _MonMatchIndex_Type(Integer32):
    """Custom type monMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MonMatchIndex_Type.__name__ = "Integer32"
_MonMatchIndex_Object = MibScalar
monMatchIndex = _MonMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 6, 4),
    _MonMatchIndex_Type()
)
monMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monMatchIndex.setStatus("mandatory")
_Empireexp_ObjectIdentity = ObjectIdentity
empireexp = _Empireexp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 7)
)
_Distribsys_ObjectIdentity = ObjectIdentity
distribsys = _Distribsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 8)
)
_Rpc_ObjectIdentity = ObjectIdentity
rpc = _Rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 8, 1)
)
_ClientRPCCalls_Type = Counter32
_ClientRPCCalls_Object = MibScalar
clientRPCCalls = _ClientRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 1),
    _ClientRPCCalls_Type()
)
clientRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCCalls.setStatus("mandatory")
_ClientRPCBadcalls_Type = Counter32
_ClientRPCBadcalls_Object = MibScalar
clientRPCBadcalls = _ClientRPCBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 2),
    _ClientRPCBadcalls_Type()
)
clientRPCBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCBadcalls.setStatus("mandatory")
_ClientRPCRetrans_Type = Counter32
_ClientRPCRetrans_Object = MibScalar
clientRPCRetrans = _ClientRPCRetrans_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 3),
    _ClientRPCRetrans_Type()
)
clientRPCRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCRetrans.setStatus("mandatory")
_ClientRPCBadxids_Type = Counter32
_ClientRPCBadxids_Object = MibScalar
clientRPCBadxids = _ClientRPCBadxids_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 4),
    _ClientRPCBadxids_Type()
)
clientRPCBadxids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCBadxids.setStatus("mandatory")
_ClientRPCTimeouts_Type = Counter32
_ClientRPCTimeouts_Object = MibScalar
clientRPCTimeouts = _ClientRPCTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 5),
    _ClientRPCTimeouts_Type()
)
clientRPCTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCTimeouts.setStatus("mandatory")
_ClientRPCWaits_Type = Counter32
_ClientRPCWaits_Object = MibScalar
clientRPCWaits = _ClientRPCWaits_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 6),
    _ClientRPCWaits_Type()
)
clientRPCWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCWaits.setStatus("mandatory")
_ClientRPCNewcreds_Type = Counter32
_ClientRPCNewcreds_Object = MibScalar
clientRPCNewcreds = _ClientRPCNewcreds_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 7),
    _ClientRPCNewcreds_Type()
)
clientRPCNewcreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCNewcreds.setStatus("mandatory")
_ClientRPCTimers_Type = Counter32
_ClientRPCTimers_Object = MibScalar
clientRPCTimers = _ClientRPCTimers_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 8),
    _ClientRPCTimers_Type()
)
clientRPCTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientRPCTimers.setStatus("mandatory")
_ServerRPCCalls_Type = Counter32
_ServerRPCCalls_Object = MibScalar
serverRPCCalls = _ServerRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 9),
    _ServerRPCCalls_Type()
)
serverRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverRPCCalls.setStatus("mandatory")
_ServerRPCBadcalls_Type = Counter32
_ServerRPCBadcalls_Object = MibScalar
serverRPCBadcalls = _ServerRPCBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 10),
    _ServerRPCBadcalls_Type()
)
serverRPCBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverRPCBadcalls.setStatus("mandatory")
_ServerRPCNullrecvs_Type = Counter32
_ServerRPCNullrecvs_Object = MibScalar
serverRPCNullrecvs = _ServerRPCNullrecvs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 11),
    _ServerRPCNullrecvs_Type()
)
serverRPCNullrecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverRPCNullrecvs.setStatus("mandatory")
_ServerRPCBadlens_Type = Counter32
_ServerRPCBadlens_Object = MibScalar
serverRPCBadlens = _ServerRPCBadlens_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 12),
    _ServerRPCBadlens_Type()
)
serverRPCBadlens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverRPCBadlens.setStatus("mandatory")
_ServerRPCXdrcalls_Type = Counter32
_ServerRPCXdrcalls_Object = MibScalar
serverRPCXdrcalls = _ServerRPCXdrcalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 1, 13),
    _ServerRPCXdrcalls_Type()
)
serverRPCXdrcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverRPCXdrcalls.setStatus("mandatory")
_Nfs_ObjectIdentity = ObjectIdentity
nfs = _Nfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 8, 2)
)
_ClientNFSCalls_Type = Counter32
_ClientNFSCalls_Object = MibScalar
clientNFSCalls = _ClientNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 1),
    _ClientNFSCalls_Type()
)
clientNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSCalls.setStatus("mandatory")
_ClientNFSBadcalls_Type = Counter32
_ClientNFSBadcalls_Object = MibScalar
clientNFSBadcalls = _ClientNFSBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 2),
    _ClientNFSBadcalls_Type()
)
clientNFSBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSBadcalls.setStatus("mandatory")
_ClientNFSNclgets_Type = Counter32
_ClientNFSNclgets_Object = MibScalar
clientNFSNclgets = _ClientNFSNclgets_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 3),
    _ClientNFSNclgets_Type()
)
clientNFSNclgets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSNclgets.setStatus("mandatory")
_ClientNFSNclsleeps_Type = Counter32
_ClientNFSNclsleeps_Object = MibScalar
clientNFSNclsleeps = _ClientNFSNclsleeps_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 4),
    _ClientNFSNclsleeps_Type()
)
clientNFSNclsleeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSNclsleeps.setStatus("mandatory")
_ClientNFSNulls_Type = Counter32
_ClientNFSNulls_Object = MibScalar
clientNFSNulls = _ClientNFSNulls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 5),
    _ClientNFSNulls_Type()
)
clientNFSNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSNulls.setStatus("mandatory")
_ClientNFSGetattrs_Type = Counter32
_ClientNFSGetattrs_Object = MibScalar
clientNFSGetattrs = _ClientNFSGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 6),
    _ClientNFSGetattrs_Type()
)
clientNFSGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSGetattrs.setStatus("mandatory")
_ClientNFSSetattrs_Type = Counter32
_ClientNFSSetattrs_Object = MibScalar
clientNFSSetattrs = _ClientNFSSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 7),
    _ClientNFSSetattrs_Type()
)
clientNFSSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSSetattrs.setStatus("mandatory")
_ClientNFSRoots_Type = Counter32
_ClientNFSRoots_Object = MibScalar
clientNFSRoots = _ClientNFSRoots_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 8),
    _ClientNFSRoots_Type()
)
clientNFSRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSRoots.setStatus("mandatory")
_ClientNFSLookups_Type = Counter32
_ClientNFSLookups_Object = MibScalar
clientNFSLookups = _ClientNFSLookups_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 9),
    _ClientNFSLookups_Type()
)
clientNFSLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSLookups.setStatus("mandatory")
_ClientNFSReadlinks_Type = Counter32
_ClientNFSReadlinks_Object = MibScalar
clientNFSReadlinks = _ClientNFSReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 10),
    _ClientNFSReadlinks_Type()
)
clientNFSReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSReadlinks.setStatus("mandatory")
_ClientNFSReads_Type = Counter32
_ClientNFSReads_Object = MibScalar
clientNFSReads = _ClientNFSReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 11),
    _ClientNFSReads_Type()
)
clientNFSReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSReads.setStatus("mandatory")
_ClientNFSWrcaches_Type = Counter32
_ClientNFSWrcaches_Object = MibScalar
clientNFSWrcaches = _ClientNFSWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 12),
    _ClientNFSWrcaches_Type()
)
clientNFSWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSWrcaches.setStatus("mandatory")
_ClientNFSWrites_Type = Counter32
_ClientNFSWrites_Object = MibScalar
clientNFSWrites = _ClientNFSWrites_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 13),
    _ClientNFSWrites_Type()
)
clientNFSWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSWrites.setStatus("mandatory")
_ClientNFSCreates_Type = Counter32
_ClientNFSCreates_Object = MibScalar
clientNFSCreates = _ClientNFSCreates_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 14),
    _ClientNFSCreates_Type()
)
clientNFSCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSCreates.setStatus("mandatory")
_ClientNFSRemoves_Type = Counter32
_ClientNFSRemoves_Object = MibScalar
clientNFSRemoves = _ClientNFSRemoves_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 15),
    _ClientNFSRemoves_Type()
)
clientNFSRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSRemoves.setStatus("mandatory")
_ClientNFSRenames_Type = Counter32
_ClientNFSRenames_Object = MibScalar
clientNFSRenames = _ClientNFSRenames_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 16),
    _ClientNFSRenames_Type()
)
clientNFSRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSRenames.setStatus("mandatory")
_ClientNFSLinks_Type = Counter32
_ClientNFSLinks_Object = MibScalar
clientNFSLinks = _ClientNFSLinks_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 17),
    _ClientNFSLinks_Type()
)
clientNFSLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSLinks.setStatus("mandatory")
_ClientNFSSymlinks_Type = Counter32
_ClientNFSSymlinks_Object = MibScalar
clientNFSSymlinks = _ClientNFSSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 18),
    _ClientNFSSymlinks_Type()
)
clientNFSSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSSymlinks.setStatus("mandatory")
_ClientNFSMkdirs_Type = Counter32
_ClientNFSMkdirs_Object = MibScalar
clientNFSMkdirs = _ClientNFSMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 19),
    _ClientNFSMkdirs_Type()
)
clientNFSMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSMkdirs.setStatus("mandatory")
_ClientNFSRmdirs_Type = Counter32
_ClientNFSRmdirs_Object = MibScalar
clientNFSRmdirs = _ClientNFSRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 20),
    _ClientNFSRmdirs_Type()
)
clientNFSRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSRmdirs.setStatus("mandatory")
_ClientNFSReaddirs_Type = Counter32
_ClientNFSReaddirs_Object = MibScalar
clientNFSReaddirs = _ClientNFSReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 21),
    _ClientNFSReaddirs_Type()
)
clientNFSReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSReaddirs.setStatus("mandatory")
_ClientNFSFsstats_Type = Counter32
_ClientNFSFsstats_Object = MibScalar
clientNFSFsstats = _ClientNFSFsstats_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 22),
    _ClientNFSFsstats_Type()
)
clientNFSFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientNFSFsstats.setStatus("mandatory")
_ServerNFSCalls_Type = Counter32
_ServerNFSCalls_Object = MibScalar
serverNFSCalls = _ServerNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 23),
    _ServerNFSCalls_Type()
)
serverNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSCalls.setStatus("mandatory")
_ServerNFSBadcalls_Type = Counter32
_ServerNFSBadcalls_Object = MibScalar
serverNFSBadcalls = _ServerNFSBadcalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 24),
    _ServerNFSBadcalls_Type()
)
serverNFSBadcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSBadcalls.setStatus("mandatory")
_ServerNFSNulls_Type = Counter32
_ServerNFSNulls_Object = MibScalar
serverNFSNulls = _ServerNFSNulls_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 25),
    _ServerNFSNulls_Type()
)
serverNFSNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSNulls.setStatus("mandatory")
_ServerNFSGetattrs_Type = Counter32
_ServerNFSGetattrs_Object = MibScalar
serverNFSGetattrs = _ServerNFSGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 26),
    _ServerNFSGetattrs_Type()
)
serverNFSGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSGetattrs.setStatus("mandatory")
_ServerNFSSetattrs_Type = Counter32
_ServerNFSSetattrs_Object = MibScalar
serverNFSSetattrs = _ServerNFSSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 27),
    _ServerNFSSetattrs_Type()
)
serverNFSSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSSetattrs.setStatus("mandatory")
_ServerNFSRoots_Type = Counter32
_ServerNFSRoots_Object = MibScalar
serverNFSRoots = _ServerNFSRoots_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 28),
    _ServerNFSRoots_Type()
)
serverNFSRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSRoots.setStatus("mandatory")
_ServerNFSLookups_Type = Counter32
_ServerNFSLookups_Object = MibScalar
serverNFSLookups = _ServerNFSLookups_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 29),
    _ServerNFSLookups_Type()
)
serverNFSLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSLookups.setStatus("mandatory")
_ServerNFSReadlinks_Type = Counter32
_ServerNFSReadlinks_Object = MibScalar
serverNFSReadlinks = _ServerNFSReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 30),
    _ServerNFSReadlinks_Type()
)
serverNFSReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSReadlinks.setStatus("mandatory")
_ServerNFSReads_Type = Counter32
_ServerNFSReads_Object = MibScalar
serverNFSReads = _ServerNFSReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 31),
    _ServerNFSReads_Type()
)
serverNFSReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSReads.setStatus("mandatory")
_ServerNFSWrcaches_Type = Counter32
_ServerNFSWrcaches_Object = MibScalar
serverNFSWrcaches = _ServerNFSWrcaches_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 32),
    _ServerNFSWrcaches_Type()
)
serverNFSWrcaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSWrcaches.setStatus("mandatory")
_ServerNFSWrites_Type = Counter32
_ServerNFSWrites_Object = MibScalar
serverNFSWrites = _ServerNFSWrites_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 33),
    _ServerNFSWrites_Type()
)
serverNFSWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSWrites.setStatus("mandatory")
_ServerNFSCreates_Type = Counter32
_ServerNFSCreates_Object = MibScalar
serverNFSCreates = _ServerNFSCreates_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 34),
    _ServerNFSCreates_Type()
)
serverNFSCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSCreates.setStatus("mandatory")
_ServerNFSRemoves_Type = Counter32
_ServerNFSRemoves_Object = MibScalar
serverNFSRemoves = _ServerNFSRemoves_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 35),
    _ServerNFSRemoves_Type()
)
serverNFSRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSRemoves.setStatus("mandatory")
_ServerNFSRenames_Type = Counter32
_ServerNFSRenames_Object = MibScalar
serverNFSRenames = _ServerNFSRenames_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 36),
    _ServerNFSRenames_Type()
)
serverNFSRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSRenames.setStatus("mandatory")
_ServerNFSLinks_Type = Counter32
_ServerNFSLinks_Object = MibScalar
serverNFSLinks = _ServerNFSLinks_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 37),
    _ServerNFSLinks_Type()
)
serverNFSLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSLinks.setStatus("mandatory")
_ServerNFSSymlinks_Type = Counter32
_ServerNFSSymlinks_Object = MibScalar
serverNFSSymlinks = _ServerNFSSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 38),
    _ServerNFSSymlinks_Type()
)
serverNFSSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSSymlinks.setStatus("mandatory")
_ServerNFSMkdirs_Type = Counter32
_ServerNFSMkdirs_Object = MibScalar
serverNFSMkdirs = _ServerNFSMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 39),
    _ServerNFSMkdirs_Type()
)
serverNFSMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSMkdirs.setStatus("mandatory")
_ServerNFSRmdirs_Type = Counter32
_ServerNFSRmdirs_Object = MibScalar
serverNFSRmdirs = _ServerNFSRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 40),
    _ServerNFSRmdirs_Type()
)
serverNFSRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSRmdirs.setStatus("mandatory")
_ServerNFSReaddirs_Type = Counter32
_ServerNFSReaddirs_Object = MibScalar
serverNFSReaddirs = _ServerNFSReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 41),
    _ServerNFSReaddirs_Type()
)
serverNFSReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSReaddirs.setStatus("mandatory")
_ServerNFSFsstats_Type = Counter32
_ServerNFSFsstats_Object = MibScalar
serverNFSFsstats = _ServerNFSFsstats_Object(
    (1, 3, 6, 1, 4, 1, 546, 8, 2, 42),
    _ServerNFSFsstats_Type()
)
serverNFSFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNFSFsstats.setStatus("mandatory")
_Nis_ObjectIdentity = ObjectIdentity
nis = _Nis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 8, 3)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9)
)
_MonitorEvent_ObjectIdentity = ObjectIdentity
monitorEvent = _MonitorEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 1)
)
_KernelErrorEvent_ObjectIdentity = ObjectIdentity
kernelErrorEvent = _KernelErrorEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 2)
)
_MonitorEntryNotReadyEvent_ObjectIdentity = ObjectIdentity
monitorEntryNotReadyEvent = _MonitorEntryNotReadyEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 3)
)
_LogMonMatchEvent_ObjectIdentity = ObjectIdentity
logMonMatchEvent = _LogMonMatchEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 4)
)
_LogMonNotReadyEvent_ObjectIdentity = ObjectIdentity
logMonNotReadyEvent = _LogMonNotReadyEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 5)
)
_SendTrapEvent_ObjectIdentity = ObjectIdentity
sendTrapEvent = _SendTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 6)
)
_NtEventMonMatchEvent_ObjectIdentity = ObjectIdentity
ntEventMonMatchEvent = _NtEventMonMatchEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 7)
)
_NtEventMonNotReadyEvent_ObjectIdentity = ObjectIdentity
ntEventMonNotReadyEvent = _NtEventMonNotReadyEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 8)
)
_MonitorClearEvent_ObjectIdentity = ObjectIdentity
monitorClearEvent = _MonitorClearEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 9)
)
_ProcessStopEvent_ObjectIdentity = ObjectIdentity
processStopEvent = _ProcessStopEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 10)
)
_ProcessStartEvent_ObjectIdentity = ObjectIdentity
processStartEvent = _ProcessStartEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 11)
)
_ProcessThresholdEvent_ObjectIdentity = ObjectIdentity
processThresholdEvent = _ProcessThresholdEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 12)
)
_ProcessClearEvent_ObjectIdentity = ObjectIdentity
processClearEvent = _ProcessClearEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 13)
)
_LicenseEvent_ObjectIdentity = ObjectIdentity
licenseEvent = _LicenseEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 16)
)
_FwLogmonEvent_ObjectIdentity = ObjectIdentity
fwLogmonEvent = _FwLogmonEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 17)
)
_AddrChangeEvent_ObjectIdentity = ObjectIdentity
addrChangeEvent = _AddrChangeEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 18)
)
_ProcGroupChangeEvent_ObjectIdentity = ObjectIdentity
procGroupChangeEvent = _ProcGroupChangeEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 9, 19)
)
_EmpireHistory_ObjectIdentity = ObjectIdentity
empireHistory = _EmpireHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 10)
)
_EmpireHistoryCtrlTable_Object = MibTable
empireHistoryCtrlTable = _EmpireHistoryCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1)
)
if mibBuilder.loadTexts:
    empireHistoryCtrlTable.setStatus("mandatory")
_EmpireHistoryCtrlEntry_Object = MibTableRow
empireHistoryCtrlEntry = _EmpireHistoryCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1)
)
empireHistoryCtrlEntry.setIndexNames(
    (0, "EMPIRE", "empireHistoryCtrlIndex"),
)
if mibBuilder.loadTexts:
    empireHistoryCtrlEntry.setStatus("mandatory")


class _EmpireHistoryCtrlIndex_Type(Integer32):
    """Custom type empireHistoryCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EmpireHistoryCtrlIndex_Type.__name__ = "Integer32"
_EmpireHistoryCtrlIndex_Object = MibTableColumn
empireHistoryCtrlIndex = _EmpireHistoryCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 1),
    _EmpireHistoryCtrlIndex_Type()
)
empireHistoryCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryCtrlIndex.setStatus("mandatory")


class _EmpireHistoryCtrlDescr_Type(DisplayString):
    """Custom type empireHistoryCtrlDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EmpireHistoryCtrlDescr_Type.__name__ = "DisplayString"
_EmpireHistoryCtrlDescr_Object = MibTableColumn
empireHistoryCtrlDescr = _EmpireHistoryCtrlDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 2),
    _EmpireHistoryCtrlDescr_Type()
)
empireHistoryCtrlDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    empireHistoryCtrlDescr.setStatus("mandatory")
_EmpireHistoryCtrlInterval_Type = Integer32
_EmpireHistoryCtrlInterval_Object = MibTableColumn
empireHistoryCtrlInterval = _EmpireHistoryCtrlInterval_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 3),
    _EmpireHistoryCtrlInterval_Type()
)
empireHistoryCtrlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    empireHistoryCtrlInterval.setStatus("mandatory")
_EmpireHistoryCtrlObjID_Type = ObjectIdentifier
_EmpireHistoryCtrlObjID_Object = MibTableColumn
empireHistoryCtrlObjID = _EmpireHistoryCtrlObjID_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 4),
    _EmpireHistoryCtrlObjID_Type()
)
empireHistoryCtrlObjID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    empireHistoryCtrlObjID.setStatus("mandatory")
_EmpireHistoryCtrlObjType_Type = Integer32
_EmpireHistoryCtrlObjType_Object = MibTableColumn
empireHistoryCtrlObjType = _EmpireHistoryCtrlObjType_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 5),
    _EmpireHistoryCtrlObjType_Type()
)
empireHistoryCtrlObjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryCtrlObjType.setStatus("mandatory")
_EmpireHistoryCtrlBucketsReq_Type = Integer32
_EmpireHistoryCtrlBucketsReq_Object = MibTableColumn
empireHistoryCtrlBucketsReq = _EmpireHistoryCtrlBucketsReq_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 6),
    _EmpireHistoryCtrlBucketsReq_Type()
)
empireHistoryCtrlBucketsReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    empireHistoryCtrlBucketsReq.setStatus("mandatory")
_EmpireHistoryCtrlBucketsGrant_Type = Integer32
_EmpireHistoryCtrlBucketsGrant_Object = MibTableColumn
empireHistoryCtrlBucketsGrant = _EmpireHistoryCtrlBucketsGrant_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 7),
    _EmpireHistoryCtrlBucketsGrant_Type()
)
empireHistoryCtrlBucketsGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryCtrlBucketsGrant.setStatus("mandatory")
_EmpireHistoryCtrlLastCall_Type = TimeTicks
_EmpireHistoryCtrlLastCall_Object = MibTableColumn
empireHistoryCtrlLastCall = _EmpireHistoryCtrlLastCall_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 8),
    _EmpireHistoryCtrlLastCall_Type()
)
empireHistoryCtrlLastCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryCtrlLastCall.setStatus("mandatory")
_EmpireHistoryCtrlCreateTime_Type = TimeTicks
_EmpireHistoryCtrlCreateTime_Object = MibTableColumn
empireHistoryCtrlCreateTime = _EmpireHistoryCtrlCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 9),
    _EmpireHistoryCtrlCreateTime_Type()
)
empireHistoryCtrlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryCtrlCreateTime.setStatus("mandatory")


class _EmpireHistoryCtrlStatus_Type(Integer32):
    """Custom type empireHistoryCtrlStatus based on Integer32"""
    defaultValue = 5

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_EmpireHistoryCtrlStatus_Type.__name__ = "Integer32"
_EmpireHistoryCtrlStatus_Object = MibTableColumn
empireHistoryCtrlStatus = _EmpireHistoryCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 1, 1, 10),
    _EmpireHistoryCtrlStatus_Type()
)
empireHistoryCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    empireHistoryCtrlStatus.setStatus("mandatory")
_EmpireHistoryTable_Object = MibTable
empireHistoryTable = _EmpireHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 2)
)
if mibBuilder.loadTexts:
    empireHistoryTable.setStatus("mandatory")
_EmpireHistoryEntry_Object = MibTableRow
empireHistoryEntry = _EmpireHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 2, 1)
)
empireHistoryEntry.setIndexNames(
    (0, "EMPIRE", "empireHistoryIndex"),
    (0, "EMPIRE", "empireHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    empireHistoryEntry.setStatus("mandatory")
_EmpireHistoryIndex_Type = Integer32
_EmpireHistoryIndex_Object = MibTableColumn
empireHistoryIndex = _EmpireHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 2, 1, 1),
    _EmpireHistoryIndex_Type()
)
empireHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryIndex.setStatus("mandatory")
_EmpireHistorySampleIndex_Type = Integer32
_EmpireHistorySampleIndex_Object = MibTableColumn
empireHistorySampleIndex = _EmpireHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 2, 1, 2),
    _EmpireHistorySampleIndex_Type()
)
empireHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistorySampleIndex.setStatus("mandatory")
_EmpireHistoryStartTime_Type = TimeTicks
_EmpireHistoryStartTime_Object = MibTableColumn
empireHistoryStartTime = _EmpireHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 2, 1, 3),
    _EmpireHistoryStartTime_Type()
)
empireHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryStartTime.setStatus("mandatory")
_EmpireHistorySampleTime_Type = TimeTicks
_EmpireHistorySampleTime_Object = MibTableColumn
empireHistorySampleTime = _EmpireHistorySampleTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 2, 1, 4),
    _EmpireHistorySampleTime_Type()
)
empireHistorySampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistorySampleTime.setStatus("mandatory")
_EmpireHistoryValue_Type = Integer32
_EmpireHistoryValue_Object = MibTableColumn
empireHistoryValue = _EmpireHistoryValue_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 2, 1, 5),
    _EmpireHistoryValue_Type()
)
empireHistoryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    empireHistoryValue.setStatus("mandatory")


class _HistCtrlUnusedIndex_Type(Integer32):
    """Custom type histCtrlUnusedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HistCtrlUnusedIndex_Type.__name__ = "Integer32"
_HistCtrlUnusedIndex_Object = MibScalar
histCtrlUnusedIndex = _HistCtrlUnusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 3),
    _HistCtrlUnusedIndex_Type()
)
histCtrlUnusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histCtrlUnusedIndex.setStatus("mandatory")
_HistCtrlMatchDescr_Type = DisplayString
_HistCtrlMatchDescr_Object = MibScalar
histCtrlMatchDescr = _HistCtrlMatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 4),
    _HistCtrlMatchDescr_Type()
)
histCtrlMatchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    histCtrlMatchDescr.setStatus("mandatory")


class _HistCtrlMatchIndex_Type(Integer32):
    """Custom type histCtrlMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HistCtrlMatchIndex_Type.__name__ = "Integer32"
_HistCtrlMatchIndex_Object = MibScalar
histCtrlMatchIndex = _HistCtrlMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 10, 5),
    _HistCtrlMatchIndex_Type()
)
histCtrlMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histCtrlMatchIndex.setStatus("mandatory")
_LogMonitor_ObjectIdentity = ObjectIdentity
logMonitor = _LogMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 11)
)
_LogMonitorTable_Object = MibTable
logMonitorTable = _LogMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1)
)
if mibBuilder.loadTexts:
    logMonitorTable.setStatus("mandatory")
_LogMonitorEntry_Object = MibTableRow
logMonitorEntry = _LogMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1)
)
logMonitorEntry.setIndexNames(
    (0, "EMPIRE", "logMonitorIndex"),
)
if mibBuilder.loadTexts:
    logMonitorEntry.setStatus("mandatory")


class _LogMonitorIndex_Type(Integer32):
    """Custom type logMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LogMonitorIndex_Type.__name__ = "Integer32"
_LogMonitorIndex_Object = MibTableColumn
logMonitorIndex = _LogMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 1),
    _LogMonitorIndex_Type()
)
logMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMonitorIndex.setStatus("mandatory")


class _LogMonitorLogFile_Type(DisplayString):
    """Custom type logMonitorLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LogMonitorLogFile_Type.__name__ = "DisplayString"
_LogMonitorLogFile_Object = MibTableColumn
logMonitorLogFile = _LogMonitorLogFile_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 2),
    _LogMonitorLogFile_Type()
)
logMonitorLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMonitorLogFile.setStatus("mandatory")


class _LogMonitorRegularExpression_Type(DisplayString):
    """Custom type logMonitorRegularExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LogMonitorRegularExpression_Type.__name__ = "DisplayString"
_LogMonitorRegularExpression_Object = MibTableColumn
logMonitorRegularExpression = _LogMonitorRegularExpression_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 3),
    _LogMonitorRegularExpression_Type()
)
logMonitorRegularExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMonitorRegularExpression.setStatus("mandatory")
_LogMonitorNumberTraps_Type = Integer32
_LogMonitorNumberTraps_Object = MibTableColumn
logMonitorNumberTraps = _LogMonitorNumberTraps_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 4),
    _LogMonitorNumberTraps_Type()
)
logMonitorNumberTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMonitorNumberTraps.setStatus("mandatory")
_LogMonitorLastTrap_Type = TimeTicks
_LogMonitorLastTrap_Object = MibTableColumn
logMonitorLastTrap = _LogMonitorLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 5),
    _LogMonitorLastTrap_Type()
)
logMonitorLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMonitorLastTrap.setStatus("mandatory")


class _LogMonitorLastMatch_Type(DisplayString):
    """Custom type logMonitorLastMatch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LogMonitorLastMatch_Type.__name__ = "DisplayString"
_LogMonitorLastMatch_Object = MibTableColumn
logMonitorLastMatch = _LogMonitorLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 6),
    _LogMonitorLastMatch_Type()
)
logMonitorLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMonitorLastMatch.setStatus("mandatory")


class _LogMonitorStatus_Type(Integer32):
    """Custom type logMonitorStatus based on Integer32"""
    defaultValue = 5

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_LogMonitorStatus_Type.__name__ = "Integer32"
_LogMonitorStatus_Object = MibTableColumn
logMonitorStatus = _LogMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 7),
    _LogMonitorStatus_Type()
)
logMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMonitorStatus.setStatus("mandatory")
_LogMonitorLogFileSize_Type = Integer32
_LogMonitorLogFileSize_Object = MibTableColumn
logMonitorLogFileSize = _LogMonitorLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 8),
    _LogMonitorLogFileSize_Type()
)
logMonitorLogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMonitorLogFileSize.setStatus("mandatory")
_LogMonitorLogFileLastUpdate_Type = TimeTicks
_LogMonitorLogFileLastUpdate_Object = MibTableColumn
logMonitorLogFileLastUpdate = _LogMonitorLogFileLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 9),
    _LogMonitorLogFileLastUpdate_Type()
)
logMonitorLogFileLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMonitorLogFileLastUpdate.setStatus("mandatory")


class _LogMonitorDescr_Type(DisplayString):
    """Custom type logMonitorDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LogMonitorDescr_Type.__name__ = "DisplayString"
_LogMonitorDescr_Object = MibTableColumn
logMonitorDescr = _LogMonitorDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 10),
    _LogMonitorDescr_Type()
)
logMonitorDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMonitorDescr.setStatus("mandatory")


class _LogMonitorAction_Type(DisplayString):
    """Custom type logMonitorAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LogMonitorAction_Type.__name__ = "DisplayString"
_LogMonitorAction_Object = MibTableColumn
logMonitorAction = _LogMonitorAction_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 11),
    _LogMonitorAction_Type()
)
logMonitorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMonitorAction.setStatus("mandatory")
_LogMonitorFlags_Type = Integer32
_LogMonitorFlags_Object = MibTableColumn
logMonitorFlags = _LogMonitorFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 12),
    _LogMonitorFlags_Type()
)
logMonitorFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMonitorFlags.setStatus("mandatory")
_LogMonitorMatches_Type = Counter32
_LogMonitorMatches_Object = MibTableColumn
logMonitorMatches = _LogMonitorMatches_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 1, 1, 13),
    _LogMonitorMatches_Type()
)
logMonitorMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMonitorMatches.setStatus("mandatory")


class _LogmonUnusedIndex_Type(Integer32):
    """Custom type logmonUnusedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LogmonUnusedIndex_Type.__name__ = "Integer32"
_LogmonUnusedIndex_Object = MibScalar
logmonUnusedIndex = _LogmonUnusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 2),
    _LogmonUnusedIndex_Type()
)
logmonUnusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logmonUnusedIndex.setStatus("mandatory")
_LogmonMatchDescr_Type = DisplayString
_LogmonMatchDescr_Object = MibScalar
logmonMatchDescr = _LogmonMatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 3),
    _LogmonMatchDescr_Type()
)
logmonMatchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logmonMatchDescr.setStatus("mandatory")


class _LogmonMatchIndex_Type(Integer32):
    """Custom type logmonMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LogmonMatchIndex_Type.__name__ = "Integer32"
_LogmonMatchIndex_Object = MibScalar
logmonMatchIndex = _LogmonMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 11, 4),
    _LogmonMatchIndex_Type()
)
logmonMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logmonMatchIndex.setStatus("mandatory")
_DiskGroup_ObjectIdentity = ObjectIdentity
diskGroup = _DiskGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 12)
)
_DiskStatsTable_Object = MibTable
diskStatsTable = _DiskStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1)
)
if mibBuilder.loadTexts:
    diskStatsTable.setStatus("mandatory")
_DiskStatsEntry_Object = MibTableRow
diskStatsEntry = _DiskStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1)
)
diskStatsEntry.setIndexNames(
    (0, "EMPIRE", "diskStatsIndex"),
)
if mibBuilder.loadTexts:
    diskStatsEntry.setStatus("mandatory")


class _DiskStatsIndex_Type(Integer32):
    """Custom type diskStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiskStatsIndex_Type.__name__ = "Integer32"
_DiskStatsIndex_Object = MibTableColumn
diskStatsIndex = _DiskStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 1),
    _DiskStatsIndex_Type()
)
diskStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsIndex.setStatus("mandatory")
_DiskStatsQueueLength_Type = Gauge32
_DiskStatsQueueLength_Object = MibTableColumn
diskStatsQueueLength = _DiskStatsQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 2),
    _DiskStatsQueueLength_Type()
)
diskStatsQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsQueueLength.setStatus("mandatory")
_DiskStatsServiceTime_Type = Gauge32
_DiskStatsServiceTime_Object = MibTableColumn
diskStatsServiceTime = _DiskStatsServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 3),
    _DiskStatsServiceTime_Type()
)
diskStatsServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsServiceTime.setStatus("mandatory")


class _DiskStatsUtilization_Type(Integer32):
    """Custom type diskStatsUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskStatsUtilization_Type.__name__ = "Integer32"
_DiskStatsUtilization_Object = MibTableColumn
diskStatsUtilization = _DiskStatsUtilization_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 4),
    _DiskStatsUtilization_Type()
)
diskStatsUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsUtilization.setStatus("mandatory")
_DiskStatsKBytesTransferred_Type = Counter32
_DiskStatsKBytesTransferred_Object = MibTableColumn
diskStatsKBytesTransferred = _DiskStatsKBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 5),
    _DiskStatsKBytesTransferred_Type()
)
diskStatsKBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsKBytesTransferred.setStatus("mandatory")
_DiskStatsTransfers_Type = Counter32
_DiskStatsTransfers_Object = MibTableColumn
diskStatsTransfers = _DiskStatsTransfers_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 6),
    _DiskStatsTransfers_Type()
)
diskStatsTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsTransfers.setStatus("mandatory")
_DiskStatsReads_Type = Counter32
_DiskStatsReads_Object = MibTableColumn
diskStatsReads = _DiskStatsReads_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 7),
    _DiskStatsReads_Type()
)
diskStatsReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsReads.setStatus("mandatory")
_DiskStatsWrites_Type = Counter32
_DiskStatsWrites_Object = MibTableColumn
diskStatsWrites = _DiskStatsWrites_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 8),
    _DiskStatsWrites_Type()
)
diskStatsWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsWrites.setStatus("mandatory")


class _DiskStatsHostmibDevTableIndex_Type(Integer32):
    """Custom type diskStatsHostmibDevTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiskStatsHostmibDevTableIndex_Type.__name__ = "Integer32"
_DiskStatsHostmibDevTableIndex_Object = MibTableColumn
diskStatsHostmibDevTableIndex = _DiskStatsHostmibDevTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 9),
    _DiskStatsHostmibDevTableIndex_Type()
)
diskStatsHostmibDevTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsHostmibDevTableIndex.setStatus("mandatory")
_DiskStatsLastUpdate_Type = TimeTicks
_DiskStatsLastUpdate_Object = MibTableColumn
diskStatsLastUpdate = _DiskStatsLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 10),
    _DiskStatsLastUpdate_Type()
)
diskStatsLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsLastUpdate.setStatus("mandatory")
_DiskStatsKBytesXferStr_Type = DisplayString
_DiskStatsKBytesXferStr_Object = MibTableColumn
diskStatsKBytesXferStr = _DiskStatsKBytesXferStr_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 11),
    _DiskStatsKBytesXferStr_Type()
)
diskStatsKBytesXferStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsKBytesXferStr.setStatus("mandatory")
_DiskStatsTransfersStr_Type = DisplayString
_DiskStatsTransfersStr_Object = MibTableColumn
diskStatsTransfersStr = _DiskStatsTransfersStr_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 12),
    _DiskStatsTransfersStr_Type()
)
diskStatsTransfersStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsTransfersStr.setStatus("mandatory")
_DiskStatsReadsStr_Type = DisplayString
_DiskStatsReadsStr_Object = MibTableColumn
diskStatsReadsStr = _DiskStatsReadsStr_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 13),
    _DiskStatsReadsStr_Type()
)
diskStatsReadsStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsReadsStr.setStatus("mandatory")
_DiskStatsWritesStr_Type = DisplayString
_DiskStatsWritesStr_Object = MibTableColumn
diskStatsWritesStr = _DiskStatsWritesStr_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 14),
    _DiskStatsWritesStr_Type()
)
diskStatsWritesStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsWritesStr.setStatus("mandatory")
_DiskStatsKBytesXferHi_Type = Counter32
_DiskStatsKBytesXferHi_Object = MibTableColumn
diskStatsKBytesXferHi = _DiskStatsKBytesXferHi_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 15),
    _DiskStatsKBytesXferHi_Type()
)
diskStatsKBytesXferHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsKBytesXferHi.setStatus("mandatory")
_DiskStatsXferOpsHi_Type = Counter32
_DiskStatsXferOpsHi_Object = MibTableColumn
diskStatsXferOpsHi = _DiskStatsXferOpsHi_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 16),
    _DiskStatsXferOpsHi_Type()
)
diskStatsXferOpsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsXferOpsHi.setStatus("mandatory")
_DiskStatsReadsHi_Type = Counter32
_DiskStatsReadsHi_Object = MibTableColumn
diskStatsReadsHi = _DiskStatsReadsHi_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 17),
    _DiskStatsReadsHi_Type()
)
diskStatsReadsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsReadsHi.setStatus("mandatory")
_DiskStatsWritesHi_Type = Counter32
_DiskStatsWritesHi_Object = MibTableColumn
diskStatsWritesHi = _DiskStatsWritesHi_Object(
    (1, 3, 6, 1, 4, 1, 546, 12, 1, 1, 18),
    _DiskStatsWritesHi_Type()
)
diskStatsWritesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatsWritesHi.setStatus("mandatory")
_CpuGroup_ObjectIdentity = ObjectIdentity
cpuGroup = _CpuGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 13)
)
_CpuStatsTable_Object = MibTable
cpuStatsTable = _CpuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1)
)
if mibBuilder.loadTexts:
    cpuStatsTable.setStatus("mandatory")
_CpuStatsEntry_Object = MibTableRow
cpuStatsEntry = _CpuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1)
)
cpuStatsEntry.setIndexNames(
    (0, "EMPIRE", "cpuStatsIndex"),
)
if mibBuilder.loadTexts:
    cpuStatsEntry.setStatus("mandatory")


class _CpuStatsIndex_Type(Integer32):
    """Custom type cpuStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpuStatsIndex_Type.__name__ = "Integer32"
_CpuStatsIndex_Object = MibTableColumn
cpuStatsIndex = _CpuStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 1),
    _CpuStatsIndex_Type()
)
cpuStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsIndex.setStatus("mandatory")


class _CpuStatsDescr_Type(DisplayString):
    """Custom type cpuStatsDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpuStatsDescr_Type.__name__ = "DisplayString"
_CpuStatsDescr_Object = MibTableColumn
cpuStatsDescr = _CpuStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 2),
    _CpuStatsDescr_Type()
)
cpuStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsDescr.setStatus("mandatory")
_CpuStatsIdle_Type = Counter32
_CpuStatsIdle_Object = MibTableColumn
cpuStatsIdle = _CpuStatsIdle_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 3),
    _CpuStatsIdle_Type()
)
cpuStatsIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsIdle.setStatus("mandatory")
_CpuStatsUser_Type = Counter32
_CpuStatsUser_Object = MibTableColumn
cpuStatsUser = _CpuStatsUser_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 4),
    _CpuStatsUser_Type()
)
cpuStatsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsUser.setStatus("mandatory")
_CpuStatsSys_Type = Counter32
_CpuStatsSys_Object = MibTableColumn
cpuStatsSys = _CpuStatsSys_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 5),
    _CpuStatsSys_Type()
)
cpuStatsSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsSys.setStatus("mandatory")
_CpuStatsWait_Type = Counter32
_CpuStatsWait_Object = MibTableColumn
cpuStatsWait = _CpuStatsWait_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 6),
    _CpuStatsWait_Type()
)
cpuStatsWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsWait.setStatus("mandatory")
_CpuStatsLastUpdate_Type = TimeTicks
_CpuStatsLastUpdate_Object = MibTableColumn
cpuStatsLastUpdate = _CpuStatsLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 7),
    _CpuStatsLastUpdate_Type()
)
cpuStatsLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsLastUpdate.setStatus("mandatory")


class _CpuStatsIdlePercent_Type(Integer32):
    """Custom type cpuStatsIdlePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuStatsIdlePercent_Type.__name__ = "Integer32"
_CpuStatsIdlePercent_Object = MibTableColumn
cpuStatsIdlePercent = _CpuStatsIdlePercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 8),
    _CpuStatsIdlePercent_Type()
)
cpuStatsIdlePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsIdlePercent.setStatus("mandatory")


class _CpuStatsUserPercent_Type(Integer32):
    """Custom type cpuStatsUserPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuStatsUserPercent_Type.__name__ = "Integer32"
_CpuStatsUserPercent_Object = MibTableColumn
cpuStatsUserPercent = _CpuStatsUserPercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 9),
    _CpuStatsUserPercent_Type()
)
cpuStatsUserPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsUserPercent.setStatus("mandatory")


class _CpuStatsSysPercent_Type(Integer32):
    """Custom type cpuStatsSysPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuStatsSysPercent_Type.__name__ = "Integer32"
_CpuStatsSysPercent_Object = MibTableColumn
cpuStatsSysPercent = _CpuStatsSysPercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 10),
    _CpuStatsSysPercent_Type()
)
cpuStatsSysPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsSysPercent.setStatus("mandatory")


class _CpuStatsWaitPercent_Type(Integer32):
    """Custom type cpuStatsWaitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuStatsWaitPercent_Type.__name__ = "Integer32"
_CpuStatsWaitPercent_Object = MibTableColumn
cpuStatsWaitPercent = _CpuStatsWaitPercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 1, 1, 11),
    _CpuStatsWaitPercent_Type()
)
cpuStatsWaitPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatsWaitPercent.setStatus("mandatory")
_CpuTotalIdle_Type = Counter32
_CpuTotalIdle_Object = MibScalar
cpuTotalIdle = _CpuTotalIdle_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 2),
    _CpuTotalIdle_Type()
)
cpuTotalIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalIdle.setStatus("mandatory")
_CpuTotalUser_Type = Counter32
_CpuTotalUser_Object = MibScalar
cpuTotalUser = _CpuTotalUser_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 3),
    _CpuTotalUser_Type()
)
cpuTotalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalUser.setStatus("mandatory")
_CpuTotalSys_Type = Counter32
_CpuTotalSys_Object = MibScalar
cpuTotalSys = _CpuTotalSys_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 4),
    _CpuTotalSys_Type()
)
cpuTotalSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalSys.setStatus("mandatory")
_CpuTotalWait_Type = Counter32
_CpuTotalWait_Object = MibScalar
cpuTotalWait = _CpuTotalWait_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 5),
    _CpuTotalWait_Type()
)
cpuTotalWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalWait.setStatus("mandatory")
_CpuTotalLastUpdate_Type = TimeTicks
_CpuTotalLastUpdate_Object = MibScalar
cpuTotalLastUpdate = _CpuTotalLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 6),
    _CpuTotalLastUpdate_Type()
)
cpuTotalLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalLastUpdate.setStatus("mandatory")


class _CpuTotalIdlePercent_Type(Integer32):
    """Custom type cpuTotalIdlePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuTotalIdlePercent_Type.__name__ = "Integer32"
_CpuTotalIdlePercent_Object = MibScalar
cpuTotalIdlePercent = _CpuTotalIdlePercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 7),
    _CpuTotalIdlePercent_Type()
)
cpuTotalIdlePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalIdlePercent.setStatus("mandatory")


class _CpuTotalUserPercent_Type(Integer32):
    """Custom type cpuTotalUserPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuTotalUserPercent_Type.__name__ = "Integer32"
_CpuTotalUserPercent_Object = MibScalar
cpuTotalUserPercent = _CpuTotalUserPercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 8),
    _CpuTotalUserPercent_Type()
)
cpuTotalUserPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalUserPercent.setStatus("mandatory")


class _CpuTotalSysPercent_Type(Integer32):
    """Custom type cpuTotalSysPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuTotalSysPercent_Type.__name__ = "Integer32"
_CpuTotalSysPercent_Object = MibScalar
cpuTotalSysPercent = _CpuTotalSysPercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 9),
    _CpuTotalSysPercent_Type()
)
cpuTotalSysPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalSysPercent.setStatus("mandatory")


class _CpuTotalWaitPercent_Type(Integer32):
    """Custom type cpuTotalWaitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuTotalWaitPercent_Type.__name__ = "Integer32"
_CpuTotalWaitPercent_Object = MibScalar
cpuTotalWaitPercent = _CpuTotalWaitPercent_Object(
    (1, 3, 6, 1, 4, 1, 546, 13, 10),
    _CpuTotalWaitPercent_Type()
)
cpuTotalWaitPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTotalWaitPercent.setStatus("mandatory")
_ExtensionGroup_ObjectIdentity = ObjectIdentity
extensionGroup = _ExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 14)
)


class _ExtensionDomainName_Type(DisplayString):
    """Custom type extensionDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtensionDomainName_Type.__name__ = "DisplayString"
_ExtensionDomainName_Object = MibScalar
extensionDomainName = _ExtensionDomainName_Object(
    (1, 3, 6, 1, 4, 1, 546, 14, 1),
    _ExtensionDomainName_Type()
)
extensionDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionDomainName.setStatus("mandatory")


class _ExtensionNisServer_Type(DisplayString):
    """Custom type extensionNisServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtensionNisServer_Type.__name__ = "DisplayString"
_ExtensionNisServer_Object = MibScalar
extensionNisServer = _ExtensionNisServer_Object(
    (1, 3, 6, 1, 4, 1, 546, 14, 2),
    _ExtensionNisServer_Type()
)
extensionNisServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionNisServer.setStatus("mandatory")


class _ExtensionMotd_Type(DisplayString):
    """Custom type extensionMotd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtensionMotd_Type.__name__ = "DisplayString"
_ExtensionMotd_Object = MibScalar
extensionMotd = _ExtensionMotd_Object(
    (1, 3, 6, 1, 4, 1, 546, 14, 3),
    _ExtensionMotd_Type()
)
extensionMotd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionMotd.setStatus("mandatory")


class _ExtensionPing_Type(DisplayString):
    """Custom type extensionPing based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtensionPing_Type.__name__ = "DisplayString"
_ExtensionPing_Object = MibScalar
extensionPing = _ExtensionPing_Object(
    (1, 3, 6, 1, 4, 1, 546, 14, 31),
    _ExtensionPing_Type()
)
extensionPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extensionPing.setStatus("mandatory")
_ProcessMonitor_ObjectIdentity = ObjectIdentity
processMonitor = _ProcessMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 15)
)
_ProcessMonTable_Object = MibTable
processMonTable = _ProcessMonTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1)
)
if mibBuilder.loadTexts:
    processMonTable.setStatus("mandatory")
_ProcessMonEntry_Object = MibTableRow
processMonEntry = _ProcessMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1)
)
processMonEntry.setIndexNames(
    (0, "EMPIRE", "pmonIndex"),
)
if mibBuilder.loadTexts:
    processMonEntry.setStatus("mandatory")


class _PmonIndex_Type(Integer32):
    """Custom type pmonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmonIndex_Type.__name__ = "Integer32"
_PmonIndex_Object = MibTableColumn
pmonIndex = _PmonIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 1),
    _PmonIndex_Type()
)
pmonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonIndex.setStatus("mandatory")


class _PmonDescr_Type(DisplayString):
    """Custom type pmonDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PmonDescr_Type.__name__ = "DisplayString"
_PmonDescr_Object = MibTableColumn
pmonDescr = _PmonDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 2),
    _PmonDescr_Type()
)
pmonDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonDescr.setStatus("mandatory")


class _PmonInterval_Type(Integer32):
    """Custom type pmonInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmonInterval_Type.__name__ = "Integer32"
_PmonInterval_Object = MibTableColumn
pmonInterval = _PmonInterval_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 3),
    _PmonInterval_Type()
)
pmonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonInterval.setStatus("mandatory")


class _PmonSampleType_Type(Integer32):
    """Custom type pmonSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_PmonSampleType_Type.__name__ = "Integer32"
_PmonSampleType_Object = MibTableColumn
pmonSampleType = _PmonSampleType_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 4),
    _PmonSampleType_Type()
)
pmonSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonSampleType.setStatus("mandatory")


class _PmonAttribute_Type(Integer32):
    """Custom type pmonAttribute based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("procAlive", 1),
          ("procInBlks", 6),
          ("procInvolCtx", 17),
          ("procMajorPgFlts", 15),
          ("procMemory", 2),
          ("procMinorPgFlts", 14),
          ("procMsgsRecv", 9),
          ("procMsgsSent", 8),
          ("procNice", 10),
          ("procNumSwaps", 12),
          ("procNumThreads", 11),
          ("procOutBlks", 7),
          ("procRSS", 4),
          ("procSize", 3),
          ("procSysCalls", 13),
          ("procTime", 5),
          ("procVolCtx", 16))
    )


_PmonAttribute_Type.__name__ = "Integer32"
_PmonAttribute_Object = MibTableColumn
pmonAttribute = _PmonAttribute_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 5),
    _PmonAttribute_Type()
)
pmonAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonAttribute.setStatus("mandatory")
_PmonCurrVal_Type = Integer32
_PmonCurrVal_Object = MibTableColumn
pmonCurrVal = _PmonCurrVal_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 6),
    _PmonCurrVal_Type()
)
pmonCurrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonCurrVal.setStatus("mandatory")


class _PmonOperator_Type(Integer32):
    """Custom type pmonOperator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eq", 6),
          ("ge", 4),
          ("gt", 2),
          ("le", 5),
          ("lt", 3),
          ("ne", 7),
          ("nop", 1))
    )


_PmonOperator_Type.__name__ = "Integer32"
_PmonOperator_Object = MibTableColumn
pmonOperator = _PmonOperator_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 7),
    _PmonOperator_Type()
)
pmonOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonOperator.setStatus("mandatory")
_PmonValue_Type = Integer32
_PmonValue_Object = MibTableColumn
pmonValue = _PmonValue_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 8),
    _PmonValue_Type()
)
pmonValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonValue.setStatus("mandatory")
_PmonLastCall_Type = TimeTicks
_PmonLastCall_Object = MibTableColumn
pmonLastCall = _PmonLastCall_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 9),
    _PmonLastCall_Type()
)
pmonLastCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonLastCall.setStatus("mandatory")
_PmonNumTraps_Type = Integer32
_PmonNumTraps_Object = MibTableColumn
pmonNumTraps = _PmonNumTraps_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 10),
    _PmonNumTraps_Type()
)
pmonNumTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonNumTraps.setStatus("mandatory")
_PmonLastTrap_Type = TimeTicks
_PmonLastTrap_Object = MibTableColumn
pmonLastTrap = _PmonLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 11),
    _PmonLastTrap_Type()
)
pmonLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonLastTrap.setStatus("mandatory")
_PmonFlags_Type = Integer32
_PmonFlags_Object = MibTableColumn
pmonFlags = _PmonFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 12),
    _PmonFlags_Type()
)
pmonFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonFlags.setStatus("mandatory")


class _PmonAction_Type(DisplayString):
    """Custom type pmonAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PmonAction_Type.__name__ = "DisplayString"
_PmonAction_Object = MibTableColumn
pmonAction = _PmonAction_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 13),
    _PmonAction_Type()
)
pmonAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonAction.setStatus("mandatory")


class _PmonRegExpr_Type(DisplayString):
    """Custom type pmonRegExpr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PmonRegExpr_Type.__name__ = "DisplayString"
_PmonRegExpr_Object = MibTableColumn
pmonRegExpr = _PmonRegExpr_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 14),
    _PmonRegExpr_Type()
)
pmonRegExpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonRegExpr.setStatus("mandatory")
_PmonMinValue_Type = Integer32
_PmonMinValue_Object = MibTableColumn
pmonMinValue = _PmonMinValue_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 15),
    _PmonMinValue_Type()
)
pmonMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonMinValue.setStatus("mandatory")
_PmonMaxValue_Type = Integer32
_PmonMaxValue_Object = MibTableColumn
pmonMaxValue = _PmonMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 16),
    _PmonMaxValue_Type()
)
pmonMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonMaxValue.setStatus("mandatory")
_PmonCurrentPID_Type = Integer32
_PmonCurrentPID_Object = MibTableColumn
pmonCurrentPID = _PmonCurrentPID_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 17),
    _PmonCurrentPID_Type()
)
pmonCurrentPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonCurrentPID.setStatus("mandatory")


class _PmonRowStatus_Type(Integer32):
    """Custom type pmonRowStatus based on Integer32"""
    defaultValue = 5

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_PmonRowStatus_Type.__name__ = "Integer32"
_PmonRowStatus_Object = MibTableColumn
pmonRowStatus = _PmonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 18),
    _PmonRowStatus_Type()
)
pmonRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonRowStatus.setStatus("mandatory")
_PmonNumEvents_Type = Counter32
_PmonNumEvents_Object = MibTableColumn
pmonNumEvents = _PmonNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 1, 1, 19),
    _PmonNumEvents_Type()
)
pmonNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonNumEvents.setStatus("mandatory")


class _PmonUnusedIndex_Type(Integer32):
    """Custom type pmonUnusedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmonUnusedIndex_Type.__name__ = "Integer32"
_PmonUnusedIndex_Object = MibScalar
pmonUnusedIndex = _PmonUnusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 2),
    _PmonUnusedIndex_Type()
)
pmonUnusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonUnusedIndex.setStatus("mandatory")
_PmonMatchDescr_Type = DisplayString
_PmonMatchDescr_Object = MibScalar
pmonMatchDescr = _PmonMatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 3),
    _PmonMatchDescr_Type()
)
pmonMatchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmonMatchDescr.setStatus("mandatory")


class _PmonMatchIndex_Type(Integer32):
    """Custom type pmonMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmonMatchIndex_Type.__name__ = "Integer32"
_PmonMatchIndex_Object = MibScalar
pmonMatchIndex = _PmonMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 4),
    _PmonMatchIndex_Type()
)
pmonMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmonMatchIndex.setStatus("mandatory")
_ProcessGroupMonTable_Object = MibTable
processGroupMonTable = _ProcessGroupMonTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10)
)
if mibBuilder.loadTexts:
    processGroupMonTable.setStatus("mandatory")
_ProcessGroupMonEntry_Object = MibTableRow
processGroupMonEntry = _ProcessGroupMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1)
)
processGroupMonEntry.setIndexNames(
    (0, "EMPIRE", "pgmonIndex"),
)
if mibBuilder.loadTexts:
    processGroupMonEntry.setStatus("mandatory")


class _PgmonIndex_Type(Integer32):
    """Custom type pgmonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PgmonIndex_Type.__name__ = "Integer32"
_PgmonIndex_Object = MibTableColumn
pgmonIndex = _PgmonIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 1),
    _PgmonIndex_Type()
)
pgmonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonIndex.setStatus("mandatory")


class _PgmonDescr_Type(DisplayString):
    """Custom type pgmonDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PgmonDescr_Type.__name__ = "DisplayString"
_PgmonDescr_Object = MibTableColumn
pgmonDescr = _PgmonDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 2),
    _PgmonDescr_Type()
)
pgmonDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonDescr.setStatus("mandatory")


class _PgmonInterval_Type(Integer32):
    """Custom type pgmonInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PgmonInterval_Type.__name__ = "Integer32"
_PgmonInterval_Object = MibTableColumn
pgmonInterval = _PgmonInterval_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 3),
    _PgmonInterval_Type()
)
pgmonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonInterval.setStatus("mandatory")


class _PgmonProcRegExpr_Type(DisplayString):
    """Custom type pgmonProcRegExpr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PgmonProcRegExpr_Type.__name__ = "DisplayString"
_PgmonProcRegExpr_Object = MibTableColumn
pgmonProcRegExpr = _PgmonProcRegExpr_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 4),
    _PgmonProcRegExpr_Type()
)
pgmonProcRegExpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonProcRegExpr.setStatus("mandatory")
_PgmonFlags_Type = Integer32
_PgmonFlags_Object = MibTableColumn
pgmonFlags = _PgmonFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 5),
    _PgmonFlags_Type()
)
pgmonFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonFlags.setStatus("mandatory")
_PgmonNumProcs_Type = Gauge32
_PgmonNumProcs_Object = MibTableColumn
pgmonNumProcs = _PgmonNumProcs_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 6),
    _PgmonNumProcs_Type()
)
pgmonNumProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonNumProcs.setStatus("mandatory")
_PgmonPIDList_Type = DisplayString
_PgmonPIDList_Object = MibTableColumn
pgmonPIDList = _PgmonPIDList_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 7),
    _PgmonPIDList_Type()
)
pgmonPIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonPIDList.setStatus("mandatory")
_PgmonStatusList_Type = DisplayString
_PgmonStatusList_Object = MibTableColumn
pgmonStatusList = _PgmonStatusList_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 8),
    _PgmonStatusList_Type()
)
pgmonStatusList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonStatusList.setStatus("mandatory")


class _PgmonAction_Type(DisplayString):
    """Custom type pgmonAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PgmonAction_Type.__name__ = "DisplayString"
_PgmonAction_Object = MibTableColumn
pgmonAction = _PgmonAction_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 9),
    _PgmonAction_Type()
)
pgmonAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonAction.setStatus("mandatory")
_PgmonNumEvents_Type = Counter32
_PgmonNumEvents_Object = MibTableColumn
pgmonNumEvents = _PgmonNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 10),
    _PgmonNumEvents_Type()
)
pgmonNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonNumEvents.setStatus("mandatory")
_PgmonNumTraps_Type = Counter32
_PgmonNumTraps_Object = MibTableColumn
pgmonNumTraps = _PgmonNumTraps_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 11),
    _PgmonNumTraps_Type()
)
pgmonNumTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonNumTraps.setStatus("mandatory")
_PgmonLastTrap_Type = TimeTicks
_PgmonLastTrap_Object = MibTableColumn
pgmonLastTrap = _PgmonLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 12),
    _PgmonLastTrap_Type()
)
pgmonLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonLastTrap.setStatus("mandatory")


class _PgmonRowStatus_Type(Integer32):
    """Custom type pgmonRowStatus based on Integer32"""
    defaultValue = 5

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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_PgmonRowStatus_Type.__name__ = "Integer32"
_PgmonRowStatus_Object = MibTableColumn
pgmonRowStatus = _PgmonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 13),
    _PgmonRowStatus_Type()
)
pgmonRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonRowStatus.setStatus("mandatory")
_PgmonRSS_Type = Gauge32
_PgmonRSS_Object = MibTableColumn
pgmonRSS = _PgmonRSS_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 14),
    _PgmonRSS_Type()
)
pgmonRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonRSS.setStatus("mandatory")
_PgmonSize_Type = Gauge32
_PgmonSize_Object = MibTableColumn
pgmonSize = _PgmonSize_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 15),
    _PgmonSize_Type()
)
pgmonSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonSize.setStatus("mandatory")
_PgmonThreadCount_Type = Gauge32
_PgmonThreadCount_Object = MibTableColumn
pgmonThreadCount = _PgmonThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 16),
    _PgmonThreadCount_Type()
)
pgmonThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonThreadCount.setStatus("mandatory")
_PgmonMEM_Type = Gauge32
_PgmonMEM_Object = MibTableColumn
pgmonMEM = _PgmonMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 17),
    _PgmonMEM_Type()
)
pgmonMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonMEM.setStatus("mandatory")
_PgmonInBlks_Type = Counter32
_PgmonInBlks_Object = MibTableColumn
pgmonInBlks = _PgmonInBlks_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 18),
    _PgmonInBlks_Type()
)
pgmonInBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonInBlks.setStatus("mandatory")
_PgmonOutBlks_Type = Counter32
_PgmonOutBlks_Object = MibTableColumn
pgmonOutBlks = _PgmonOutBlks_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 19),
    _PgmonOutBlks_Type()
)
pgmonOutBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonOutBlks.setStatus("mandatory")
_PgmonMsgsSent_Type = Counter32
_PgmonMsgsSent_Object = MibTableColumn
pgmonMsgsSent = _PgmonMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 20),
    _PgmonMsgsSent_Type()
)
pgmonMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonMsgsSent.setStatus("mandatory")
_PgmonMsgsRecv_Type = Counter32
_PgmonMsgsRecv_Object = MibTableColumn
pgmonMsgsRecv = _PgmonMsgsRecv_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 21),
    _PgmonMsgsRecv_Type()
)
pgmonMsgsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonMsgsRecv.setStatus("mandatory")
_PgmonSysCalls_Type = Counter32
_PgmonSysCalls_Object = MibTableColumn
pgmonSysCalls = _PgmonSysCalls_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 22),
    _PgmonSysCalls_Type()
)
pgmonSysCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonSysCalls.setStatus("mandatory")
_PgmonMinorPgFlts_Type = Counter32
_PgmonMinorPgFlts_Object = MibTableColumn
pgmonMinorPgFlts = _PgmonMinorPgFlts_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 23),
    _PgmonMinorPgFlts_Type()
)
pgmonMinorPgFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonMinorPgFlts.setStatus("mandatory")
_PgmonMajorPgFlts_Type = Counter32
_PgmonMajorPgFlts_Object = MibTableColumn
pgmonMajorPgFlts = _PgmonMajorPgFlts_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 24),
    _PgmonMajorPgFlts_Type()
)
pgmonMajorPgFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonMajorPgFlts.setStatus("mandatory")
_PgmonNumSwaps_Type = Counter32
_PgmonNumSwaps_Object = MibTableColumn
pgmonNumSwaps = _PgmonNumSwaps_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 25),
    _PgmonNumSwaps_Type()
)
pgmonNumSwaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonNumSwaps.setStatus("mandatory")
_PgmonVolCtx_Type = Counter32
_PgmonVolCtx_Object = MibTableColumn
pgmonVolCtx = _PgmonVolCtx_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 26),
    _PgmonVolCtx_Type()
)
pgmonVolCtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonVolCtx.setStatus("mandatory")
_PgmonInvolCtx_Type = Counter32
_PgmonInvolCtx_Object = MibTableColumn
pgmonInvolCtx = _PgmonInvolCtx_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 27),
    _PgmonInvolCtx_Type()
)
pgmonInvolCtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonInvolCtx.setStatus("mandatory")
_PgmonCPUSecs_Type = Counter32
_PgmonCPUSecs_Object = MibTableColumn
pgmonCPUSecs = _PgmonCPUSecs_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 28),
    _PgmonCPUSecs_Type()
)
pgmonCPUSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonCPUSecs.setStatus("mandatory")


class _PgmonMatchUser_Type(DisplayString):
    """Custom type pgmonMatchUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PgmonMatchUser_Type.__name__ = "DisplayString"
_PgmonMatchUser_Object = MibTableColumn
pgmonMatchUser = _PgmonMatchUser_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 29),
    _PgmonMatchUser_Type()
)
pgmonMatchUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonMatchUser.setStatus("mandatory")


class _PgmonMatchGroup_Type(DisplayString):
    """Custom type pgmonMatchGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PgmonMatchGroup_Type.__name__ = "DisplayString"
_PgmonMatchGroup_Object = MibTableColumn
pgmonMatchGroup = _PgmonMatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 10, 1, 30),
    _PgmonMatchGroup_Type()
)
pgmonMatchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonMatchGroup.setStatus("mandatory")


class _PgmonUnusedIndex_Type(Integer32):
    """Custom type pgmonUnusedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PgmonUnusedIndex_Type.__name__ = "Integer32"
_PgmonUnusedIndex_Object = MibScalar
pgmonUnusedIndex = _PgmonUnusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 11),
    _PgmonUnusedIndex_Type()
)
pgmonUnusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonUnusedIndex.setStatus("mandatory")
_PgmonMatchDescr_Type = DisplayString
_PgmonMatchDescr_Object = MibScalar
pgmonMatchDescr = _PgmonMatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 12),
    _PgmonMatchDescr_Type()
)
pgmonMatchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgmonMatchDescr.setStatus("mandatory")


class _PgmonMatchIndex_Type(Integer32):
    """Custom type pgmonMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PgmonMatchIndex_Type.__name__ = "Integer32"
_PgmonMatchIndex_Object = MibScalar
pgmonMatchIndex = _PgmonMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 15, 13),
    _PgmonMatchIndex_Type()
)
pgmonMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgmonMatchIndex.setStatus("mandatory")
_Applications_ObjectIdentity = ObjectIdentity
applications = _Applications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16)
)
_MsExchange_ObjectIdentity = ObjectIdentity
msExchange = _MsExchange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 1)
)
_MsIIS_ObjectIdentity = ObjectIdentity
msIIS = _MsIIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 2)
)
_ApacheSrv_ObjectIdentity = ObjectIdentity
apacheSrv = _ApacheSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 3)
)
_Oracledb_ObjectIdentity = ObjectIdentity
oracledb = _Oracledb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4)
)
_Sybase_ObjectIdentity = ObjectIdentity
sybase = _Sybase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 5)
)
_SvcRsp_ObjectIdentity = ObjectIdentity
svcRsp = _SvcRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 6)
)
_TopProcs_ObjectIdentity = ObjectIdentity
topProcs = _TopProcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 7)
)
_SqlServer_ObjectIdentity = ObjectIdentity
sqlServer = _SqlServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 8)
)
_Domino_ObjectIdentity = ObjectIdentity
domino = _Domino_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 10)
)
_Surveyor_ObjectIdentity = ObjectIdentity
surveyor = _Surveyor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 11)
)
_MosMod_ObjectIdentity = ObjectIdentity
mosMod = _MosMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 12)
)
_Ccmmod_ObjectIdentity = ObjectIdentity
ccmmod = _Ccmmod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 13)
)
_Siebelmod_ObjectIdentity = ObjectIdentity
siebelmod = _Siebelmod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 14)
)
_Testplugin_ObjectIdentity = ObjectIdentity
testplugin = _Testplugin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 16)
)
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 17)
)
_Dirmwp_ObjectIdentity = ObjectIdentity
dirmwp = _Dirmwp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 18)
)
_Custom_ObjectIdentity = ObjectIdentity
custom = _Custom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 100)
)

# Managed Objects groups


# Notification objects

monitorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 1)
)
monitorTrap.setObjects(
      *(("EMPIRE", "monDescr"),
        ("EMPIRE", "monOID"),
        ("EMPIRE", "monCurrVal"),
        ("EMPIRE", "monValue"),
        ("EMPIRE", "monRowStatus"),
        ("EMPIRE", "monOperator"),
        ("EMPIRE", "monIndex"),
        ("EMPIRE", "monFlags"))
)
if mibBuilder.loadTexts:
    monitorTrap.setStatus(
        ""
    )

kernelErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 2)
)
kernelErrorTrap.setObjects(
      *(("EMPIRE", "seqNum"),
        ("EMPIRE", "type"),
        ("EMPIRE", "cause"),
        ("EMPIRE", "severity"))
)
if mibBuilder.loadTexts:
    kernelErrorTrap.setStatus(
        ""
    )

monitorEntryNotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 3)
)
monitorEntryNotReadyTrap.setObjects(
      *(("EMPIRE", "monDescr"),
        ("EMPIRE", "monOID"),
        ("EMPIRE", "monCurrVal"),
        ("EMPIRE", "monValue"),
        ("EMPIRE", "monRowStatus"),
        ("EMPIRE", "monOperator"),
        ("EMPIRE", "monIndex"),
        ("EMPIRE", "monFlags"))
)
if mibBuilder.loadTexts:
    monitorEntryNotReadyTrap.setStatus(
        ""
    )

logMonMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 4)
)
logMonMatchTrap.setObjects(
      *(("EMPIRE", "logMonitorLogFile"),
        ("EMPIRE", "logMonitorRegularExpression"),
        ("EMPIRE", "logMonitorLastTrap"),
        ("EMPIRE", "logMonitorLastMatch"),
        ("EMPIRE", "logMonitorDescr"),
        ("EMPIRE", "logMonitorIndex"),
        ("EMPIRE", "logMonitorFlags"))
)
if mibBuilder.loadTexts:
    logMonMatchTrap.setStatus(
        ""
    )

logMonNotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 5)
)
logMonNotReadyTrap.setObjects(
      *(("EMPIRE", "logMonitorLogFile"),
        ("EMPIRE", "logMonitorRegularExpression"),
        ("EMPIRE", "logMonitorLastTrap"),
        ("EMPIRE", "logMonitorLastMatch"),
        ("EMPIRE", "logMonitorDescr"),
        ("EMPIRE", "logMonitorIndex"),
        ("EMPIRE", "logMonitorFlags"))
)
if mibBuilder.loadTexts:
    logMonNotReadyTrap.setStatus(
        ""
    )

ntEventMonMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 7)
)
ntEventMonMatchTrap.setObjects(
      *(("EMPIRE", "ntEventMonLog"),
        ("EMPIRE", "ntEventMonTypeLastMatch"),
        ("EMPIRE", "ntEventMonTime"),
        ("EMPIRE", "ntEventMonSrcLastMatch"),
        ("EMPIRE", "ntEventMonDescLastMatch"),
        ("EMPIRE", "ntEventMonDescr"),
        ("EMPIRE", "ntEventMonIndex"),
        ("EMPIRE", "ntEventMonFlags"))
)
if mibBuilder.loadTexts:
    ntEventMonMatchTrap.setStatus(
        ""
    )

ntEventMonNotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 8)
)
ntEventMonNotReadyTrap.setObjects(
      *(("EMPIRE", "ntEventMonLog"),
        ("EMPIRE", "ntEventMonTypeFilter"),
        ("EMPIRE", "ntEventMonSrcFilter"),
        ("EMPIRE", "ntEventMonDescFilter"),
        ("EMPIRE", "ntEventMonDescr"),
        ("EMPIRE", "ntEventMonIndex"),
        ("EMPIRE", "ntEventMonFlags"))
)
if mibBuilder.loadTexts:
    ntEventMonNotReadyTrap.setStatus(
        ""
    )

monitorClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 9)
)
monitorClearTrap.setObjects(
      *(("EMPIRE", "monDescr"),
        ("EMPIRE", "monOID"),
        ("EMPIRE", "monCurrVal"),
        ("EMPIRE", "monValue"),
        ("EMPIRE", "monRowStatus"),
        ("EMPIRE", "monOperator"),
        ("EMPIRE", "monIndex"),
        ("EMPIRE", "monFlags"))
)
if mibBuilder.loadTexts:
    monitorClearTrap.setStatus(
        ""
    )

processStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 10)
)
processStopTrap.setObjects(
      *(("EMPIRE", "pmonIndex"),
        ("EMPIRE", "pmonDescr"),
        ("EMPIRE", "pmonAttribute"),
        ("EMPIRE", "pmonCurrVal"),
        ("EMPIRE", "pmonOperator"),
        ("EMPIRE", "pmonValue"),
        ("EMPIRE", "pmonFlags"),
        ("EMPIRE", "pmonRegExpr"),
        ("EMPIRE", "pmonCurrentPID"))
)
if mibBuilder.loadTexts:
    processStopTrap.setStatus(
        ""
    )

processStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 11)
)
processStartTrap.setObjects(
      *(("EMPIRE", "pmonIndex"),
        ("EMPIRE", "pmonDescr"),
        ("EMPIRE", "pmonAttribute"),
        ("EMPIRE", "pmonCurrVal"),
        ("EMPIRE", "pmonOperator"),
        ("EMPIRE", "pmonValue"),
        ("EMPIRE", "pmonFlags"),
        ("EMPIRE", "pmonRegExpr"),
        ("EMPIRE", "pmonCurrentPID"))
)
if mibBuilder.loadTexts:
    processStartTrap.setStatus(
        ""
    )

processThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 12)
)
processThresholdTrap.setObjects(
      *(("EMPIRE", "pmonIndex"),
        ("EMPIRE", "pmonDescr"),
        ("EMPIRE", "pmonAttribute"),
        ("EMPIRE", "pmonCurrVal"),
        ("EMPIRE", "pmonOperator"),
        ("EMPIRE", "pmonValue"),
        ("EMPIRE", "pmonFlags"),
        ("EMPIRE", "pmonRegExpr"),
        ("EMPIRE", "pmonCurrentPID"))
)
if mibBuilder.loadTexts:
    processThresholdTrap.setStatus(
        ""
    )

processClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 13)
)
processClearTrap.setObjects(
      *(("EMPIRE", "pmonIndex"),
        ("EMPIRE", "pmonDescr"),
        ("EMPIRE", "pmonAttribute"),
        ("EMPIRE", "pmonCurrVal"),
        ("EMPIRE", "pmonOperator"),
        ("EMPIRE", "pmonValue"),
        ("EMPIRE", "pmonFlags"),
        ("EMPIRE", "pmonRegExpr"),
        ("EMPIRE", "pmonCurrentPID"))
)
if mibBuilder.loadTexts:
    processClearTrap.setStatus(
        ""
    )

licenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 16)
)
licenseTrap.setObjects(
    ("EMPIRE", "sysedgeLicenseString")
)
if mibBuilder.loadTexts:
    licenseTrap.setStatus(
        ""
    )

addrChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 18)
)
addrChangeTrap.setObjects(
      *(("EMPIRE", "nodename"),
        ("EMPIRE", "sysedgeAddressList"))
)
if mibBuilder.loadTexts:
    addrChangeTrap.setStatus(
        ""
    )

procGroupChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 546, 1, 1, 0, 19)
)
procGroupChangeTrap.setObjects(
      *(("EMPIRE", "pgmonIndex"),
        ("EMPIRE", "pgmonDescr"),
        ("EMPIRE", "pgmonFlags"),
        ("EMPIRE", "pgmonNumProcs"),
        ("EMPIRE", "pgmonProcRegExpr"),
        ("EMPIRE", "pgmonRowStatus"),
        ("EMPIRE", "pgmonPIDList"),
        ("EMPIRE", "pgmonStatusList"))
)
if mibBuilder.loadTexts:
    procGroupChangeTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMPIRE",
    **{"empire": empire,
       "unix": unix,
       "sysmgmt": sysmgmt,
       "monitorTrap": monitorTrap,
       "kernelErrorTrap": kernelErrorTrap,
       "monitorEntryNotReadyTrap": monitorEntryNotReadyTrap,
       "logMonMatchTrap": logMonMatchTrap,
       "logMonNotReadyTrap": logMonNotReadyTrap,
       "ntEventMonMatchTrap": ntEventMonMatchTrap,
       "ntEventMonNotReadyTrap": ntEventMonNotReadyTrap,
       "monitorClearTrap": monitorClearTrap,
       "processStopTrap": processStopTrap,
       "processStartTrap": processStartTrap,
       "processThresholdTrap": processThresholdTrap,
       "processClearTrap": processClearTrap,
       "licenseTrap": licenseTrap,
       "addrChangeTrap": addrChangeTrap,
       "procGroupChangeTrap": procGroupChangeTrap,
       "system": system,
       "nodename": nodename,
       "cpu": cpu,
       "memory": memory,
       "hostid": hostid,
       "osver": osver,
       "osrel": osrel,
       "devTable": devTable,
       "devTableEntry": devTableEntry,
       "devIndex": devIndex,
       "devDevice": devDevice,
       "devMntPt": devMntPt,
       "devBsize": devBsize,
       "devTblks": devTblks,
       "devFblks": devFblks,
       "devTfiles": devTfiles,
       "devFfiles": devFfiles,
       "devMaxNameLen": devMaxNameLen,
       "devType": devType,
       "devFsid": devFsid,
       "devFstr": devFstr,
       "devUnmount": devUnmount,
       "devCapacity": devCapacity,
       "devInodeCapacity": devInodeCapacity,
       "agentVersion": agentVersion,
       "kernelConfig": kernelConfig,
       "maxProcs": maxProcs,
       "serialNumber": serialNumber,
       "romVersion": romVersion,
       "numCPU": numCPU,
       "clockHZ": clockHZ,
       "kernelVers": kernelVers,
       "virtualMem": virtualMem,
       "maxInode": maxInode,
       "maxFiles": maxFiles,
       "maxClist": maxClist,
       "maxMemPerProc": maxMemPerProc,
       "totalSwap": totalSwap,
       "openMaxPerProc": openMaxPerProc,
       "posixJobCtrl": posixJobCtrl,
       "posixVersion": posixVersion,
       "pageSize": pageSize,
       "wordSize": wordSize,
       "bootconf": bootconf,
       "rootName": rootName,
       "rootFSType": rootFSType,
       "rootBlocks": rootBlocks,
       "dumpName": dumpName,
       "dumpFSType": dumpFSType,
       "dumpBlocks": dumpBlocks,
       "swapName": swapName,
       "swapFSType": swapFSType,
       "swapSize": swapSize,
       "streams": streams,
       "maxmsgSize": maxmsgSize,
       "maxNumPush": maxNumPush,
       "numMuxLinks": numMuxLinks,
       "streamUse": streamUse,
       "streamMaxs": streamMaxs,
       "streamFails": streamFails,
       "queueUse": queueUse,
       "queueMaxs": queueMaxs,
       "queueFails": queueFails,
       "mblockUse": mblockUse,
       "mblockMaxs": mblockMaxs,
       "mblockFails": mblockFails,
       "dblockUse": dblockUse,
       "dblockMaxs": dblockMaxs,
       "dblockFails": dblockFails,
       "systemType": systemType,
       "systemEdgeUptime": systemEdgeUptime,
       "sysedgeLicenseString": sysedgeLicenseString,
       "sysedgeLicenseKey": sysedgeLicenseKey,
       "sysedgeMode": sysedgeMode,
       "systemTimeZone": systemTimeZone,
       "sysedgeAddressList": sysedgeAddressList,
       "sysedgeFQDN": sysedgeFQDN,
       "sysedgeConfProfile": sysedgeConfProfile,
       "sysedgeInstallDir": sysedgeInstallDir,
       "sysedgePluginList": sysedgePluginList,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "userLoginID": userLoginID,
       "userPasswd": userPasswd,
       "userUID": userUID,
       "userGID": userGID,
       "userName": userName,
       "userHomeDir": userHomeDir,
       "userShell": userShell,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupIndex": groupIndex,
       "groupName": groupName,
       "groupPasswd": groupPasswd,
       "groupGID": groupGID,
       "processTable": processTable,
       "processEntry": processEntry,
       "processID": processID,
       "processName": processName,
       "processState": processState,
       "processNice": processNice,
       "processFlags": processFlags,
       "processUID": processUID,
       "processGID": processGID,
       "processKill": processKill,
       "processMEM": processMEM,
       "processSize": processSize,
       "processRSS": processRSS,
       "processTime": processTime,
       "processParentPID": processParentPID,
       "processNumThreads": processNumThreads,
       "processInBlks": processInBlks,
       "processOutBlks": processOutBlks,
       "processMsgsSent": processMsgsSent,
       "processMsgsRecv": processMsgsRecv,
       "processSysCalls": processSysCalls,
       "processMinorPgFlts": processMinorPgFlts,
       "processMajorPgFlts": processMajorPgFlts,
       "processNumSwaps": processNumSwaps,
       "processVolCtx": processVolCtx,
       "processInvolCtx": processInvolCtx,
       "processArgs": processArgs,
       "processStartTime": processStartTime,
       "processStateStr": processStateStr,
       "processStateInt": processStateInt,
       "whoTable": whoTable,
       "whoEntry": whoEntry,
       "whoIndex": whoIndex,
       "whoName": whoName,
       "whoDevice": whoDevice,
       "whoPID": whoPID,
       "whoTime": whoTime,
       "whoWhere": whoWhere,
       "remoteShell": remoteShell,
       "shellOutput": shellOutput,
       "shellCmd": shellCmd,
       "shellExitStat": shellExitStat,
       "shellOutputContents": shellOutputContents,
       "performance": performance,
       "kernelperf": kernelperf,
       "runQLen": runQLen,
       "diskWaitNum": diskWaitNum,
       "pageWaitNum": pageWaitNum,
       "swapActive": swapActive,
       "sleepActive": sleepActive,
       "memInUse": memInUse,
       "activeMem": activeMem,
       "numProcs": numProcs,
       "numOpenFiles": numOpenFiles,
       "swapInUse": swapInUse,
       "numSwitches": numSwitches,
       "numTraps": numTraps,
       "numSyscalls": numSyscalls,
       "numInterrupts": numInterrupts,
       "numPageSwapIns": numPageSwapIns,
       "numPageSwapOuts": numPageSwapOuts,
       "numSwapIns": numSwapIns,
       "numSwapOuts": numSwapOuts,
       "numPageIns": numPageIns,
       "numPageOuts": numPageOuts,
       "numPageReclaims": numPageReclaims,
       "numPageFaults": numPageFaults,
       "loadAverage1Min": loadAverage1Min,
       "loadAverage5Min": loadAverage5Min,
       "loadAverage15Min": loadAverage15Min,
       "totalSwapSpace": totalSwapSpace,
       "swapCapacity": swapCapacity,
       "memCapacity": memCapacity,
       "memInUseCapacity": memInUseCapacity,
       "pageScans": pageScans,
       "numZombieProcs": numZombieProcs,
       "errorTable": errorTable,
       "errorEntry": errorEntry,
       "seqNum": seqNum,
       "mid": mid,
       "sid": sid,
       "time": time,
       "tag": tag,
       "type": type,
       "cause": cause,
       "severity": severity,
       "level": level,
       "module": module,
       "subSysmsg": subSysmsg,
       "errDelete": errDelete,
       "ipc": ipc,
       "msgqueTable": msgqueTable,
       "msgqueEntry": msgqueEntry,
       "queID": queID,
       "queKey": queKey,
       "queMode": queMode,
       "queOwner": queOwner,
       "queGroup": queGroup,
       "queNBytes": queNBytes,
       "queNMesg": queNMesg,
       "queDel": queDel,
       "shmemTable": shmemTable,
       "shmemEntry": shmemEntry,
       "shmemID": shmemID,
       "shmemKey": shmemKey,
       "shmemMode": shmemMode,
       "shmemOwner": shmemOwner,
       "shmemGroup": shmemGroup,
       "shmemSegSz": shmemSegSz,
       "shmemNLcks": shmemNLcks,
       "shmemDel": shmemDel,
       "semTable": semTable,
       "semEntry": semEntry,
       "semID": semID,
       "semKey": semKey,
       "semMode": semMode,
       "semOwner": semOwner,
       "semGroup": semGroup,
       "semNsems": semNsems,
       "semDel": semDel,
       "buffers": buffers,
       "mbufs": mbufs,
       "numMbufs": numMbufs,
       "numClusters": numClusters,
       "freeClusters": freeClusters,
       "numDrops": numDrops,
       "numWaits": numWaits,
       "numDrains": numDrains,
       "mbufAllocTable": mbufAllocTable,
       "mbufAllocEntry": mbufAllocEntry,
       "mbufType": mbufType,
       "mbufDesc": mbufDesc,
       "mbufAlloc": mbufAlloc,
       "strbufs": strbufs,
       "strbufAllocTable": strbufAllocTable,
       "strbufAllocEntry": strbufAllocEntry,
       "strbufAllocIndex": strbufAllocIndex,
       "strbufAllocSize": strbufAllocSize,
       "strbufAllocCurrent": strbufAllocCurrent,
       "strbufAllocMaxs": strbufAllocMaxs,
       "strbufAllocTotals": strbufAllocTotals,
       "strbufAllocFails": strbufAllocFails,
       "ioBufferCache": ioBufferCache,
       "numBreadRequests": numBreadRequests,
       "numBreadHits": numBreadHits,
       "numBufSleeps": numBufSleeps,
       "numAgeAllocs": numAgeAllocs,
       "numLRUAllocs": numLRUAllocs,
       "minNumBufHdrs": minNumBufHdrs,
       "numAllocBuf": numAllocBuf,
       "ioBufferHitRate": ioBufferHitRate,
       "dnlc": dnlc,
       "dnlcHits": dnlcHits,
       "dnlcMisses": dnlcMisses,
       "dnlcEnters": dnlcEnters,
       "dnlcDblEnters": dnlcDblEnters,
       "dnlcLongEnters": dnlcLongEnters,
       "dnlcLongLooks": dnlcLongLooks,
       "dnlcLruEmpty": dnlcLruEmpty,
       "dnlcPurges": dnlcPurges,
       "dnlcHitRate": dnlcHitRate,
       "dnlcCacheSize": dnlcCacheSize,
       "dos": dos,
       "os2": os2,
       "windows": windows,
       "nt": nt,
       "ntSystem": ntSystem,
       "ntSystemVersion": ntSystemVersion,
       "ntBuildNumber": ntBuildNumber,
       "ntServicePackNumber": ntServicePackNumber,
       "ntWorkstationOrServer": ntWorkstationOrServer,
       "ntfsDisable8dot3NameCreation": ntfsDisable8dot3NameCreation,
       "ntWin31FileSystem": ntWin31FileSystem,
       "ntCriticalSectTimeout": ntCriticalSectTimeout,
       "ntGlobalFlag": ntGlobalFlag,
       "ntIoPageLockLimit": ntIoPageLockLimit,
       "ntLargeSystemCache": ntLargeSystemCache,
       "ntPagedPoolSize": ntPagedPoolSize,
       "ntNonPagedPoolSize": ntNonPagedPoolSize,
       "ntPagingFiles": ntPagingFiles,
       "ntSystemPages": ntSystemPages,
       "ntOptionalSubsystem": ntOptionalSubsystem,
       "ntCmdlineOptions": ntCmdlineOptions,
       "ntLPTTimeout": ntLPTTimeout,
       "ntDosMemSize": ntDosMemSize,
       "ntWowCmdline": ntWowCmdline,
       "ntWowSize": ntWowSize,
       "ntUserFullScreen": ntUserFullScreen,
       "ntHistoryBufferSize": ntHistoryBufferSize,
       "ntNumberHistoryBuffers": ntNumberHistoryBuffers,
       "ntQuickEdit": ntQuickEdit,
       "ntScreenBufferSize": ntScreenBufferSize,
       "ntWindowSize": ntWindowSize,
       "ntWindowsAppInitDLLs": ntWindowsAppInitDLLs,
       "ntWindowsDeviceNotSelectedTimeout": ntWindowsDeviceNotSelectedTimeout,
       "ntWindowsSpooler": ntWindowsSpooler,
       "ntWindowsSwapDisk": ntWindowsSwapDisk,
       "ntWindowsXmitRetryTimeout": ntWindowsXmitRetryTimeout,
       "ntSystemRoot": ntSystemRoot,
       "ntBuildType": ntBuildType,
       "ntSysStartOptions": ntSysStartOptions,
       "ntSysBiosDate": ntSysBiosDate,
       "ntSysBiosVersion": ntSysBiosVersion,
       "ntVideoResolution": ntVideoResolution,
       "ntCrashDumpEnabled": ntCrashDumpEnabled,
       "ntLogEvent": ntLogEvent,
       "ntOverwrite": ntOverwrite,
       "ntSendAlert": ntSendAlert,
       "ntIsClustered": ntIsClustered,
       "ntClusterName": ntClusterName,
       "ntClusterMembers": ntClusterMembers,
       "ntClusterIsActive": ntClusterIsActive,
       "ntClusterActiveNode": ntClusterActiveNode,
       "ntThreads": ntThreads,
       "ntThreadTable": ntThreadTable,
       "ntThreadEntry": ntThreadEntry,
       "ntThreadPID": ntThreadPID,
       "ntThreadNumber": ntThreadNumber,
       "ntThreadPrivTime": ntThreadPrivTime,
       "ntThreadProcTime": ntThreadProcTime,
       "ntThreadUserTime": ntThreadUserTime,
       "ntThreadContextSwitches": ntThreadContextSwitches,
       "ntThreadElapsedTime": ntThreadElapsedTime,
       "ntThreadPriorityBase": ntThreadPriorityBase,
       "ntThreadPriority": ntThreadPriority,
       "ntThreadWaitReason": ntThreadWaitReason,
       "ntThreadStartAddr": ntThreadStartAddr,
       "ntThreadState": ntThreadState,
       "ntThreadID": ntThreadID,
       "ntRegistry": ntRegistry,
       "ntRegistryCurrentSize": ntRegistryCurrentSize,
       "ntRegistrySizeLimit": ntRegistrySizeLimit,
       "ntServices": ntServices,
       "ntServiceTable": ntServiceTable,
       "ntServiceEntry": ntServiceEntry,
       "ntServiceIndex": ntServiceIndex,
       "ntServiceName": ntServiceName,
       "ntServicePathName": ntServicePathName,
       "ntServiceStartType": ntServiceStartType,
       "ntServiceParameters": ntServiceParameters,
       "ntServiceState": ntServiceState,
       "ntServiceObjectName": ntServiceObjectName,
       "ntPerformance": ntPerformance,
       "ntSystemPerf": ntSystemPerf,
       "ntTotalPrivTime": ntTotalPrivTime,
       "ntTotalProcessorTime": ntTotalProcessorTime,
       "ntTotalUserTime": ntTotalUserTime,
       "ntAlignFixups": ntAlignFixups,
       "ntContextSwitches": ntContextSwitches,
       "ntExceptionDispatches": ntExceptionDispatches,
       "ntFileCtrlKBytes": ntFileCtrlKBytes,
       "ntFileCtrlOps": ntFileCtrlOps,
       "ntFileDataOps": ntFileDataOps,
       "ntReadKBytes": ntReadKBytes,
       "ntReadOps": ntReadOps,
       "ntWriteKBytes": ntWriteKBytes,
       "ntWriteOps": ntWriteOps,
       "ntFloatEmuls": ntFloatEmuls,
       "ntRunQLen": ntRunQLen,
       "ntSystemCalls": ntSystemCalls,
       "ntInterrupts": ntInterrupts,
       "ntCachePerf": ntCachePerf,
       "ntAsyncCopyReads": ntAsyncCopyReads,
       "ntAsyncDataMaps": ntAsyncDataMaps,
       "ntAsyncFastReads": ntAsyncFastReads,
       "ntAsyncMDLReads": ntAsyncMDLReads,
       "ntAsyncPinReads": ntAsyncPinReads,
       "ntCopyReadHits": ntCopyReadHits,
       "ntCopyReads": ntCopyReads,
       "ntDataFlushPages": ntDataFlushPages,
       "ntDataFlushes": ntDataFlushes,
       "ntDataMapHits": ntDataMapHits,
       "ntDataMapPins": ntDataMapPins,
       "ntDataMaps": ntDataMaps,
       "ntFastReadNotPossible": ntFastReadNotPossible,
       "ntFastReadResourceMisses": ntFastReadResourceMisses,
       "ntFastReads": ntFastReads,
       "ntLazyWriteFlushes": ntLazyWriteFlushes,
       "ntLazyWritePages": ntLazyWritePages,
       "ntMDLReadHits": ntMDLReadHits,
       "ntMDLReads": ntMDLReads,
       "ntPinReadHits": ntPinReadHits,
       "ntPinReads": ntPinReads,
       "ntSyncCopyReads": ntSyncCopyReads,
       "ntSyncDataMaps": ntSyncDataMaps,
       "ntSyncFastReads": ntSyncFastReads,
       "ntSyncMDLReads": ntSyncMDLReads,
       "ntSyncPinReads": ntSyncPinReads,
       "ntMemoryPerf": ntMemoryPerf,
       "ntAvailKBytes": ntAvailKBytes,
       "ntCacheKBytes": ntCacheKBytes,
       "ntCacheKBytesPeak": ntCacheKBytesPeak,
       "ntCacheFaults": ntCacheFaults,
       "ntCommitLimit": ntCommitLimit,
       "ntCommittedKBytes": ntCommittedKBytes,
       "ntDemandZeroFaults": ntDemandZeroFaults,
       "ntFreeSysPageTableEntries": ntFreeSysPageTableEntries,
       "ntPageFaults": ntPageFaults,
       "ntPageReads": ntPageReads,
       "ntPageWrites": ntPageWrites,
       "ntPagesInput": ntPagesInput,
       "ntPagesOutput": ntPagesOutput,
       "ntPages": ntPages,
       "ntPoolNonPagedAllocs": ntPoolNonPagedAllocs,
       "ntPoolNonPagedKBytes": ntPoolNonPagedKBytes,
       "ntPoolPagedAllocs": ntPoolPagedAllocs,
       "ntPoolPagedKBytes": ntPoolPagedKBytes,
       "ntPagedResidentKBytes": ntPagedResidentKBytes,
       "ntSysCacheResidentKBytes": ntSysCacheResidentKBytes,
       "ntSysCodeResidentKBytes": ntSysCodeResidentKBytes,
       "ntSysCodeTotalKBytes": ntSysCodeTotalKBytes,
       "ntSysDriverResidentKBytes": ntSysDriverResidentKBytes,
       "ntSysDriverTotalKBytes": ntSysDriverTotalKBytes,
       "ntTransitionFaults": ntTransitionFaults,
       "ntWriteCopies": ntWriteCopies,
       "ntPageFilePerf": ntPageFilePerf,
       "ntPageFileUsage": ntPageFileUsage,
       "ntPageFilePeakUsage": ntPageFilePeakUsage,
       "ntEvents": ntEvents,
       "ntEventApplicationCount": ntEventApplicationCount,
       "ntEventSecurityCount": ntEventSecurityCount,
       "ntEventSystemCount": ntEventSystemCount,
       "ntEventMonTable": ntEventMonTable,
       "ntEventMonEntry": ntEventMonEntry,
       "ntEventMonIndex": ntEventMonIndex,
       "ntEventMonLog": ntEventMonLog,
       "ntEventMonTime": ntEventMonTime,
       "ntEventMonTraps": ntEventMonTraps,
       "ntEventMonTypeLastMatch": ntEventMonTypeLastMatch,
       "ntEventMonTypeFilter": ntEventMonTypeFilter,
       "ntEventMonSrcLastMatch": ntEventMonSrcLastMatch,
       "ntEventMonSrcFilter": ntEventMonSrcFilter,
       "ntEventMonDescLastMatch": ntEventMonDescLastMatch,
       "ntEventMonDescFilter": ntEventMonDescFilter,
       "ntEventMonStatus": ntEventMonStatus,
       "ntEventMonDescr": ntEventMonDescr,
       "ntEventMonAction": ntEventMonAction,
       "ntEventMonFlags": ntEventMonFlags,
       "ntEventMonMatches": ntEventMonMatches,
       "ntEventApplicationMaxSize": ntEventApplicationMaxSize,
       "ntEventApplicationRetention": ntEventApplicationRetention,
       "ntEventSecurityMaxSize": ntEventSecurityMaxSize,
       "ntEventSecurityRetention": ntEventSecurityRetention,
       "ntEventSystemMaxSize": ntEventSystemMaxSize,
       "ntEventSystemRetention": ntEventSystemRetention,
       "ntEventUnusedIndex": ntEventUnusedIndex,
       "ntEventMatchDescr": ntEventMatchDescr,
       "ntEventMatchIndex": ntEventMatchIndex,
       "ntRegPerf": ntRegPerf,
       "ntRegPerfDumpFile": ntRegPerfDumpFile,
       "ntRegNumberOfThreads": ntRegNumberOfThreads,
       "monitor": monitor,
       "monitorTable": monitorTable,
       "monitorEntry": monitorEntry,
       "monIndex": monIndex,
       "monDescr": monDescr,
       "monInterval": monInterval,
       "monSampleType": monSampleType,
       "monOID": monOID,
       "monCurrVal": monCurrVal,
       "monOperator": monOperator,
       "monValue": monValue,
       "monLastCall": monLastCall,
       "monNumTraps": monNumTraps,
       "monLastTrap": monLastTrap,
       "monRowStatus": monRowStatus,
       "monMinValue": monMinValue,
       "monMaxValue": monMaxValue,
       "monAction": monAction,
       "monFlags": monFlags,
       "monUnusedIndex": monUnusedIndex,
       "monMatchDescr": monMatchDescr,
       "monMatchIndex": monMatchIndex,
       "empireexp": empireexp,
       "distribsys": distribsys,
       "rpc": rpc,
       "clientRPCCalls": clientRPCCalls,
       "clientRPCBadcalls": clientRPCBadcalls,
       "clientRPCRetrans": clientRPCRetrans,
       "clientRPCBadxids": clientRPCBadxids,
       "clientRPCTimeouts": clientRPCTimeouts,
       "clientRPCWaits": clientRPCWaits,
       "clientRPCNewcreds": clientRPCNewcreds,
       "clientRPCTimers": clientRPCTimers,
       "serverRPCCalls": serverRPCCalls,
       "serverRPCBadcalls": serverRPCBadcalls,
       "serverRPCNullrecvs": serverRPCNullrecvs,
       "serverRPCBadlens": serverRPCBadlens,
       "serverRPCXdrcalls": serverRPCXdrcalls,
       "nfs": nfs,
       "clientNFSCalls": clientNFSCalls,
       "clientNFSBadcalls": clientNFSBadcalls,
       "clientNFSNclgets": clientNFSNclgets,
       "clientNFSNclsleeps": clientNFSNclsleeps,
       "clientNFSNulls": clientNFSNulls,
       "clientNFSGetattrs": clientNFSGetattrs,
       "clientNFSSetattrs": clientNFSSetattrs,
       "clientNFSRoots": clientNFSRoots,
       "clientNFSLookups": clientNFSLookups,
       "clientNFSReadlinks": clientNFSReadlinks,
       "clientNFSReads": clientNFSReads,
       "clientNFSWrcaches": clientNFSWrcaches,
       "clientNFSWrites": clientNFSWrites,
       "clientNFSCreates": clientNFSCreates,
       "clientNFSRemoves": clientNFSRemoves,
       "clientNFSRenames": clientNFSRenames,
       "clientNFSLinks": clientNFSLinks,
       "clientNFSSymlinks": clientNFSSymlinks,
       "clientNFSMkdirs": clientNFSMkdirs,
       "clientNFSRmdirs": clientNFSRmdirs,
       "clientNFSReaddirs": clientNFSReaddirs,
       "clientNFSFsstats": clientNFSFsstats,
       "serverNFSCalls": serverNFSCalls,
       "serverNFSBadcalls": serverNFSBadcalls,
       "serverNFSNulls": serverNFSNulls,
       "serverNFSGetattrs": serverNFSGetattrs,
       "serverNFSSetattrs": serverNFSSetattrs,
       "serverNFSRoots": serverNFSRoots,
       "serverNFSLookups": serverNFSLookups,
       "serverNFSReadlinks": serverNFSReadlinks,
       "serverNFSReads": serverNFSReads,
       "serverNFSWrcaches": serverNFSWrcaches,
       "serverNFSWrites": serverNFSWrites,
       "serverNFSCreates": serverNFSCreates,
       "serverNFSRemoves": serverNFSRemoves,
       "serverNFSRenames": serverNFSRenames,
       "serverNFSLinks": serverNFSLinks,
       "serverNFSSymlinks": serverNFSSymlinks,
       "serverNFSMkdirs": serverNFSMkdirs,
       "serverNFSRmdirs": serverNFSRmdirs,
       "serverNFSReaddirs": serverNFSReaddirs,
       "serverNFSFsstats": serverNFSFsstats,
       "nis": nis,
       "traps": traps,
       "monitorEvent": monitorEvent,
       "kernelErrorEvent": kernelErrorEvent,
       "monitorEntryNotReadyEvent": monitorEntryNotReadyEvent,
       "logMonMatchEvent": logMonMatchEvent,
       "logMonNotReadyEvent": logMonNotReadyEvent,
       "sendTrapEvent": sendTrapEvent,
       "ntEventMonMatchEvent": ntEventMonMatchEvent,
       "ntEventMonNotReadyEvent": ntEventMonNotReadyEvent,
       "monitorClearEvent": monitorClearEvent,
       "processStopEvent": processStopEvent,
       "processStartEvent": processStartEvent,
       "processThresholdEvent": processThresholdEvent,
       "processClearEvent": processClearEvent,
       "licenseEvent": licenseEvent,
       "fwLogmonEvent": fwLogmonEvent,
       "addrChangeEvent": addrChangeEvent,
       "procGroupChangeEvent": procGroupChangeEvent,
       "empireHistory": empireHistory,
       "empireHistoryCtrlTable": empireHistoryCtrlTable,
       "empireHistoryCtrlEntry": empireHistoryCtrlEntry,
       "empireHistoryCtrlIndex": empireHistoryCtrlIndex,
       "empireHistoryCtrlDescr": empireHistoryCtrlDescr,
       "empireHistoryCtrlInterval": empireHistoryCtrlInterval,
       "empireHistoryCtrlObjID": empireHistoryCtrlObjID,
       "empireHistoryCtrlObjType": empireHistoryCtrlObjType,
       "empireHistoryCtrlBucketsReq": empireHistoryCtrlBucketsReq,
       "empireHistoryCtrlBucketsGrant": empireHistoryCtrlBucketsGrant,
       "empireHistoryCtrlLastCall": empireHistoryCtrlLastCall,
       "empireHistoryCtrlCreateTime": empireHistoryCtrlCreateTime,
       "empireHistoryCtrlStatus": empireHistoryCtrlStatus,
       "empireHistoryTable": empireHistoryTable,
       "empireHistoryEntry": empireHistoryEntry,
       "empireHistoryIndex": empireHistoryIndex,
       "empireHistorySampleIndex": empireHistorySampleIndex,
       "empireHistoryStartTime": empireHistoryStartTime,
       "empireHistorySampleTime": empireHistorySampleTime,
       "empireHistoryValue": empireHistoryValue,
       "histCtrlUnusedIndex": histCtrlUnusedIndex,
       "histCtrlMatchDescr": histCtrlMatchDescr,
       "histCtrlMatchIndex": histCtrlMatchIndex,
       "logMonitor": logMonitor,
       "logMonitorTable": logMonitorTable,
       "logMonitorEntry": logMonitorEntry,
       "logMonitorIndex": logMonitorIndex,
       "logMonitorLogFile": logMonitorLogFile,
       "logMonitorRegularExpression": logMonitorRegularExpression,
       "logMonitorNumberTraps": logMonitorNumberTraps,
       "logMonitorLastTrap": logMonitorLastTrap,
       "logMonitorLastMatch": logMonitorLastMatch,
       "logMonitorStatus": logMonitorStatus,
       "logMonitorLogFileSize": logMonitorLogFileSize,
       "logMonitorLogFileLastUpdate": logMonitorLogFileLastUpdate,
       "logMonitorDescr": logMonitorDescr,
       "logMonitorAction": logMonitorAction,
       "logMonitorFlags": logMonitorFlags,
       "logMonitorMatches": logMonitorMatches,
       "logmonUnusedIndex": logmonUnusedIndex,
       "logmonMatchDescr": logmonMatchDescr,
       "logmonMatchIndex": logmonMatchIndex,
       "diskGroup": diskGroup,
       "diskStatsTable": diskStatsTable,
       "diskStatsEntry": diskStatsEntry,
       "diskStatsIndex": diskStatsIndex,
       "diskStatsQueueLength": diskStatsQueueLength,
       "diskStatsServiceTime": diskStatsServiceTime,
       "diskStatsUtilization": diskStatsUtilization,
       "diskStatsKBytesTransferred": diskStatsKBytesTransferred,
       "diskStatsTransfers": diskStatsTransfers,
       "diskStatsReads": diskStatsReads,
       "diskStatsWrites": diskStatsWrites,
       "diskStatsHostmibDevTableIndex": diskStatsHostmibDevTableIndex,
       "diskStatsLastUpdate": diskStatsLastUpdate,
       "diskStatsKBytesXferStr": diskStatsKBytesXferStr,
       "diskStatsTransfersStr": diskStatsTransfersStr,
       "diskStatsReadsStr": diskStatsReadsStr,
       "diskStatsWritesStr": diskStatsWritesStr,
       "diskStatsKBytesXferHi": diskStatsKBytesXferHi,
       "diskStatsXferOpsHi": diskStatsXferOpsHi,
       "diskStatsReadsHi": diskStatsReadsHi,
       "diskStatsWritesHi": diskStatsWritesHi,
       "cpuGroup": cpuGroup,
       "cpuStatsTable": cpuStatsTable,
       "cpuStatsEntry": cpuStatsEntry,
       "cpuStatsIndex": cpuStatsIndex,
       "cpuStatsDescr": cpuStatsDescr,
       "cpuStatsIdle": cpuStatsIdle,
       "cpuStatsUser": cpuStatsUser,
       "cpuStatsSys": cpuStatsSys,
       "cpuStatsWait": cpuStatsWait,
       "cpuStatsLastUpdate": cpuStatsLastUpdate,
       "cpuStatsIdlePercent": cpuStatsIdlePercent,
       "cpuStatsUserPercent": cpuStatsUserPercent,
       "cpuStatsSysPercent": cpuStatsSysPercent,
       "cpuStatsWaitPercent": cpuStatsWaitPercent,
       "cpuTotalIdle": cpuTotalIdle,
       "cpuTotalUser": cpuTotalUser,
       "cpuTotalSys": cpuTotalSys,
       "cpuTotalWait": cpuTotalWait,
       "cpuTotalLastUpdate": cpuTotalLastUpdate,
       "cpuTotalIdlePercent": cpuTotalIdlePercent,
       "cpuTotalUserPercent": cpuTotalUserPercent,
       "cpuTotalSysPercent": cpuTotalSysPercent,
       "cpuTotalWaitPercent": cpuTotalWaitPercent,
       "extensionGroup": extensionGroup,
       "extensionDomainName": extensionDomainName,
       "extensionNisServer": extensionNisServer,
       "extensionMotd": extensionMotd,
       "extensionPing": extensionPing,
       "processMonitor": processMonitor,
       "processMonTable": processMonTable,
       "processMonEntry": processMonEntry,
       "pmonIndex": pmonIndex,
       "pmonDescr": pmonDescr,
       "pmonInterval": pmonInterval,
       "pmonSampleType": pmonSampleType,
       "pmonAttribute": pmonAttribute,
       "pmonCurrVal": pmonCurrVal,
       "pmonOperator": pmonOperator,
       "pmonValue": pmonValue,
       "pmonLastCall": pmonLastCall,
       "pmonNumTraps": pmonNumTraps,
       "pmonLastTrap": pmonLastTrap,
       "pmonFlags": pmonFlags,
       "pmonAction": pmonAction,
       "pmonRegExpr": pmonRegExpr,
       "pmonMinValue": pmonMinValue,
       "pmonMaxValue": pmonMaxValue,
       "pmonCurrentPID": pmonCurrentPID,
       "pmonRowStatus": pmonRowStatus,
       "pmonNumEvents": pmonNumEvents,
       "pmonUnusedIndex": pmonUnusedIndex,
       "pmonMatchDescr": pmonMatchDescr,
       "pmonMatchIndex": pmonMatchIndex,
       "processGroupMonTable": processGroupMonTable,
       "processGroupMonEntry": processGroupMonEntry,
       "pgmonIndex": pgmonIndex,
       "pgmonDescr": pgmonDescr,
       "pgmonInterval": pgmonInterval,
       "pgmonProcRegExpr": pgmonProcRegExpr,
       "pgmonFlags": pgmonFlags,
       "pgmonNumProcs": pgmonNumProcs,
       "pgmonPIDList": pgmonPIDList,
       "pgmonStatusList": pgmonStatusList,
       "pgmonAction": pgmonAction,
       "pgmonNumEvents": pgmonNumEvents,
       "pgmonNumTraps": pgmonNumTraps,
       "pgmonLastTrap": pgmonLastTrap,
       "pgmonRowStatus": pgmonRowStatus,
       "pgmonRSS": pgmonRSS,
       "pgmonSize": pgmonSize,
       "pgmonThreadCount": pgmonThreadCount,
       "pgmonMEM": pgmonMEM,
       "pgmonInBlks": pgmonInBlks,
       "pgmonOutBlks": pgmonOutBlks,
       "pgmonMsgsSent": pgmonMsgsSent,
       "pgmonMsgsRecv": pgmonMsgsRecv,
       "pgmonSysCalls": pgmonSysCalls,
       "pgmonMinorPgFlts": pgmonMinorPgFlts,
       "pgmonMajorPgFlts": pgmonMajorPgFlts,
       "pgmonNumSwaps": pgmonNumSwaps,
       "pgmonVolCtx": pgmonVolCtx,
       "pgmonInvolCtx": pgmonInvolCtx,
       "pgmonCPUSecs": pgmonCPUSecs,
       "pgmonMatchUser": pgmonMatchUser,
       "pgmonMatchGroup": pgmonMatchGroup,
       "pgmonUnusedIndex": pgmonUnusedIndex,
       "pgmonMatchDescr": pgmonMatchDescr,
       "pgmonMatchIndex": pgmonMatchIndex,
       "applications": applications,
       "msExchange": msExchange,
       "msIIS": msIIS,
       "apacheSrv": apacheSrv,
       "oracledb": oracledb,
       "sybase": sybase,
       "svcRsp": svcRsp,
       "topProcs": topProcs,
       "sqlServer": sqlServer,
       "domino": domino,
       "surveyor": surveyor,
       "mosMod": mosMod,
       "ccmmod": ccmmod,
       "siebelmod": siebelmod,
       "testplugin": testplugin,
       "firewall": firewall,
       "dirmwp": dirmwp,
       "custom": custom}
)
