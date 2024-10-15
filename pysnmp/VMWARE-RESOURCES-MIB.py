# SNMP MIB module (VMWARE-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:53 2024
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

(vmwResources,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwResources")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwCPU_ObjectIdentity = ObjectIdentity
vmwCPU = _VmwCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1)
)
_NumCPUs_Type = Gauge32
_NumCPUs_Object = MibScalar
numCPUs = _NumCPUs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 1),
    _NumCPUs_Type()
)
numCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCPUs.setStatus("mandatory")
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("mandatory")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1)
)
cpuEntry.setIndexNames(
    (0, "VMWARE-RESOURCES-MIB", "cpuVMID"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("mandatory")


class _CpuVMID_Type(Integer32):
    """Custom type cpuVMID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CpuVMID_Type.__name__ = "Integer32"
_CpuVMID_Object = MibTableColumn
cpuVMID = _CpuVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 1),
    _CpuVMID_Type()
)
cpuVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVMID.setStatus("mandatory")
_CpuShares_Type = Gauge32
_CpuShares_Object = MibTableColumn
cpuShares = _CpuShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 2),
    _CpuShares_Type()
)
cpuShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuShares.setStatus("mandatory")
_CpuUtil_Type = Gauge32
_CpuUtil_Object = MibTableColumn
cpuUtil = _CpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 1, 2, 1, 3),
    _CpuUtil_Type()
)
cpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtil.setStatus("mandatory")
_VmwMemory_ObjectIdentity = ObjectIdentity
vmwMemory = _VmwMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2)
)
_MemSize_Type = Gauge32
_MemSize_Object = MibScalar
memSize = _MemSize_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 1),
    _MemSize_Type()
)
memSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSize.setStatus("mandatory")
_MemCOS_Type = Gauge32
_MemCOS_Object = MibScalar
memCOS = _MemCOS_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 2),
    _MemCOS_Type()
)
memCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCOS.setStatus("mandatory")
_MemAvail_Type = Gauge32
_MemAvail_Object = MibScalar
memAvail = _MemAvail_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 3),
    _MemAvail_Type()
)
memAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvail.setStatus("mandatory")
_MemTable_Object = MibTable
memTable = _MemTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4)
)
if mibBuilder.loadTexts:
    memTable.setStatus("mandatory")
_MemEntry_Object = MibTableRow
memEntry = _MemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1)
)
memEntry.setIndexNames(
    (0, "VMWARE-RESOURCES-MIB", "memVMID"),
)
if mibBuilder.loadTexts:
    memEntry.setStatus("mandatory")


class _MemVMID_Type(Integer32):
    """Custom type memVMID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MemVMID_Type.__name__ = "Integer32"
_MemVMID_Object = MibTableColumn
memVMID = _MemVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 1),
    _MemVMID_Type()
)
memVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memVMID.setStatus("mandatory")
_MemShares_Type = Gauge32
_MemShares_Object = MibTableColumn
memShares = _MemShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 2),
    _MemShares_Type()
)
memShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memShares.setStatus("mandatory")
_MemConfigured_Type = Gauge32
_MemConfigured_Object = MibTableColumn
memConfigured = _MemConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 3),
    _MemConfigured_Type()
)
memConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memConfigured.setStatus("mandatory")
_MemUtil_Type = Gauge32
_MemUtil_Object = MibTableColumn
memUtil = _MemUtil_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 2, 4, 1, 4),
    _MemUtil_Type()
)
memUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUtil.setStatus("mandatory")
_VmwHBATable_Object = MibTable
vmwHBATable = _VmwHBATable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3)
)
if mibBuilder.loadTexts:
    vmwHBATable.setStatus("mandatory")
_HbaEntry_Object = MibTableRow
hbaEntry = _HbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1)
)
hbaEntry.setIndexNames(
    (0, "VMWARE-RESOURCES-MIB", "hbaIdx"),
)
if mibBuilder.loadTexts:
    hbaEntry.setStatus("mandatory")


class _HbaIdx_Type(Integer32):
    """Custom type hbaIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HbaIdx_Type.__name__ = "Integer32"
_HbaIdx_Object = MibTableColumn
hbaIdx = _HbaIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 1),
    _HbaIdx_Type()
)
hbaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaIdx.setStatus("mandatory")
_HbaName_Type = DisplayString
_HbaName_Object = MibTableColumn
hbaName = _HbaName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 2),
    _HbaName_Type()
)
hbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaName.setStatus("mandatory")
_HbaVMID_Type = Integer32
_HbaVMID_Object = MibTableColumn
hbaVMID = _HbaVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 3),
    _HbaVMID_Type()
)
hbaVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaVMID.setStatus("mandatory")
_DiskShares_Type = Gauge32
_DiskShares_Object = MibTableColumn
diskShares = _DiskShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 4),
    _DiskShares_Type()
)
diskShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskShares.setStatus("mandatory")
_NumReads_Type = Counter32
_NumReads_Object = MibTableColumn
numReads = _NumReads_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 5),
    _NumReads_Type()
)
numReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numReads.setStatus("mandatory")
_KbRead_Type = Counter32
_KbRead_Object = MibTableColumn
kbRead = _KbRead_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 6),
    _KbRead_Type()
)
kbRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbRead.setStatus("mandatory")
_NumWrites_Type = Counter32
_NumWrites_Object = MibTableColumn
numWrites = _NumWrites_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 7),
    _NumWrites_Type()
)
numWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numWrites.setStatus("mandatory")
_KbWritten_Type = Counter32
_KbWritten_Object = MibTableColumn
kbWritten = _KbWritten_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 3, 1, 8),
    _KbWritten_Type()
)
kbWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbWritten.setStatus("mandatory")
_VmwNetTable_Object = MibTable
vmwNetTable = _VmwNetTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4)
)
if mibBuilder.loadTexts:
    vmwNetTable.setStatus("mandatory")
_NetEntry_Object = MibTableRow
netEntry = _NetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1)
)
netEntry.setIndexNames(
    (0, "VMWARE-RESOURCES-MIB", "netIdx"),
)
if mibBuilder.loadTexts:
    netEntry.setStatus("mandatory")


class _NetIdx_Type(Integer32):
    """Custom type netIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetIdx_Type.__name__ = "Integer32"
_NetIdx_Object = MibTableColumn
netIdx = _NetIdx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 1),
    _NetIdx_Type()
)
netIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIdx.setStatus("mandatory")
_NetName_Type = DisplayString
_NetName_Object = MibTableColumn
netName = _NetName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 2),
    _NetName_Type()
)
netName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netName.setStatus("mandatory")
_NetVMID_Type = Integer32
_NetVMID_Object = MibTableColumn
netVMID = _NetVMID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 3),
    _NetVMID_Type()
)
netVMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netVMID.setStatus("mandatory")
_IfAddr_Type = DisplayString
_IfAddr_Object = MibTableColumn
ifAddr = _IfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 4),
    _IfAddr_Type()
)
ifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAddr.setStatus("mandatory")
_NetShares_Type = Gauge32
_NetShares_Object = MibTableColumn
netShares = _NetShares_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 5),
    _NetShares_Type()
)
netShares.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netShares.setStatus("mandatory")
_PktsTx_Type = Counter32
_PktsTx_Object = MibTableColumn
pktsTx = _PktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 6),
    _PktsTx_Type()
)
pktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsTx.setStatus("mandatory")
_KbTx_Type = Counter32
_KbTx_Object = MibTableColumn
kbTx = _KbTx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 7),
    _KbTx_Type()
)
kbTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbTx.setStatus("mandatory")
_PktsRx_Type = Counter32
_PktsRx_Object = MibTableColumn
pktsRx = _PktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 8),
    _PktsRx_Type()
)
pktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsRx.setStatus("mandatory")
_KbRx_Type = Counter32
_KbRx_Object = MibTableColumn
kbRx = _KbRx_Object(
    (1, 3, 6, 1, 4, 1, 6876, 3, 4, 1, 9),
    _KbRx_Type()
)
kbRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kbRx.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-RESOURCES-MIB",
    **{"vmwCPU": vmwCPU,
       "numCPUs": numCPUs,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuVMID": cpuVMID,
       "cpuShares": cpuShares,
       "cpuUtil": cpuUtil,
       "vmwMemory": vmwMemory,
       "memSize": memSize,
       "memCOS": memCOS,
       "memAvail": memAvail,
       "memTable": memTable,
       "memEntry": memEntry,
       "memVMID": memVMID,
       "memShares": memShares,
       "memConfigured": memConfigured,
       "memUtil": memUtil,
       "vmwHBATable": vmwHBATable,
       "hbaEntry": hbaEntry,
       "hbaIdx": hbaIdx,
       "hbaName": hbaName,
       "hbaVMID": hbaVMID,
       "diskShares": diskShares,
       "numReads": numReads,
       "kbRead": kbRead,
       "numWrites": numWrites,
       "kbWritten": kbWritten,
       "vmwNetTable": vmwNetTable,
       "netEntry": netEntry,
       "netIdx": netIdx,
       "netName": netName,
       "netVMID": netVMID,
       "ifAddr": ifAddr,
       "netShares": netShares,
       "pktsTx": pktsTx,
       "kbTx": kbTx,
       "pktsRx": pktsRx,
       "kbRx": kbRx}
)
