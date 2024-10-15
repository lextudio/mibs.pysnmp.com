# SNMP MIB module (INFORMANT-VS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-VS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:21 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(WtcsDisplayString,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "WtcsDisplayString",
    "informant")


# MODULE-IDENTITY

wmiVirtualServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24)
)
wmiVirtualServer.setRevisions(
        ("2007-05-10 21:35",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VsVirtualMachineTable_Object = MibTable
vsVirtualMachineTable = _VsVirtualMachineTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1)
)
if mibBuilder.loadTexts:
    vsVirtualMachineTable.setStatus("current")
_VsVirtualMachineEntry_Object = MibTableRow
vsVirtualMachineEntry = _VsVirtualMachineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1)
)
vsVirtualMachineEntry.setIndexNames(
    (0, "INFORMANT-VS", "vsvmIndex"),
)
if mibBuilder.loadTexts:
    vsVirtualMachineEntry.setStatus("current")


class _VsvmIndex_Type(Integer32):
    """Custom type vsvmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VsvmIndex_Type.__name__ = "Integer32"
_VsvmIndex_Object = MibTableColumn
vsvmIndex = _VsvmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 1),
    _VsvmIndex_Type()
)
vsvmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmIndex.setStatus("current")
_VsvmName_Type = WtcsDisplayString
_VsvmName_Object = MibTableColumn
vsvmName = _VsvmName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 2),
    _VsvmName_Type()
)
vsvmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmName.setStatus("current")
_VsvmCpuUtilization_Type = Gauge32
_VsvmCpuUtilization_Object = MibTableColumn
vsvmCpuUtilization = _VsvmCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 3),
    _VsvmCpuUtilization_Type()
)
vsvmCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmCpuUtilization.setStatus("current")
_VsvmDiskBytesRead_Type = Counter64
_VsvmDiskBytesRead_Object = MibTableColumn
vsvmDiskBytesRead = _VsvmDiskBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 4),
    _VsvmDiskBytesRead_Type()
)
vsvmDiskBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmDiskBytesRead.setStatus("current")
if mibBuilder.loadTexts:
    vsvmDiskBytesRead.setUnits("Bytes")
_VsvmDiskSpaceUsed_Type = Gauge32
_VsvmDiskSpaceUsed_Object = MibTableColumn
vsvmDiskSpaceUsed = _VsvmDiskSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 5),
    _VsvmDiskSpaceUsed_Type()
)
vsvmDiskSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmDiskSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    vsvmDiskSpaceUsed.setUnits("Bytes")
_VsvmDiskSpaceUsedK_Type = Gauge32
_VsvmDiskSpaceUsedK_Object = MibTableColumn
vsvmDiskSpaceUsedK = _VsvmDiskSpaceUsedK_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 6),
    _VsvmDiskSpaceUsedK_Type()
)
vsvmDiskSpaceUsedK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmDiskSpaceUsedK.setStatus("current")
if mibBuilder.loadTexts:
    vsvmDiskSpaceUsedK.setUnits("KiloBytes")
_VsvmDiskSpaceUsedM_Type = Gauge32
_VsvmDiskSpaceUsedM_Object = MibTableColumn
vsvmDiskSpaceUsedM = _VsvmDiskSpaceUsedM_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 7),
    _VsvmDiskSpaceUsedM_Type()
)
vsvmDiskSpaceUsedM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmDiskSpaceUsedM.setStatus("current")
if mibBuilder.loadTexts:
    vsvmDiskSpaceUsedM.setUnits("MegaBytes")
_VsvmDiskBytesWritten_Type = Counter64
_VsvmDiskBytesWritten_Object = MibTableColumn
vsvmDiskBytesWritten = _VsvmDiskBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 8),
    _VsvmDiskBytesWritten_Type()
)
vsvmDiskBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmDiskBytesWritten.setStatus("current")
if mibBuilder.loadTexts:
    vsvmDiskBytesWritten.setUnits("Bytes")
_VsvmHeartbeatCount_Type = Counter64
_VsvmHeartbeatCount_Object = MibTableColumn
vsvmHeartbeatCount = _VsvmHeartbeatCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 9),
    _VsvmHeartbeatCount_Type()
)
vsvmHeartbeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmHeartbeatCount.setStatus("current")
_VsvmHeartbeatInterval_Type = Gauge32
_VsvmHeartbeatInterval_Object = MibTableColumn
vsvmHeartbeatInterval = _VsvmHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 10),
    _VsvmHeartbeatInterval_Type()
)
vsvmHeartbeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmHeartbeatInterval.setStatus("current")
_VsvmHeartbeatPercentage_Type = Gauge32
_VsvmHeartbeatPercentage_Object = MibTableColumn
vsvmHeartbeatPercentage = _VsvmHeartbeatPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 11),
    _VsvmHeartbeatPercentage_Type()
)
vsvmHeartbeatPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmHeartbeatPercentage.setStatus("current")
_VsvmHeartbeatRate_Type = Gauge32
_VsvmHeartbeatRate_Object = MibTableColumn
vsvmHeartbeatRate = _VsvmHeartbeatRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 12),
    _VsvmHeartbeatRate_Type()
)
vsvmHeartbeatRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmHeartbeatRate.setStatus("current")
_VsvmNetworkBytesSent_Type = Counter64
_VsvmNetworkBytesSent_Object = MibTableColumn
vsvmNetworkBytesSent = _VsvmNetworkBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 13),
    _VsvmNetworkBytesSent_Type()
)
vsvmNetworkBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmNetworkBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    vsvmNetworkBytesSent.setUnits("Bytes")
_VsvmNetworkBytesReceived_Type = Counter64
_VsvmNetworkBytesReceived_Object = MibTableColumn
vsvmNetworkBytesReceived = _VsvmNetworkBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 14),
    _VsvmNetworkBytesReceived_Type()
)
vsvmNetworkBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmNetworkBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    vsvmNetworkBytesReceived.setUnits("Bytes")
_VsvmPhysicalMemoryAllocated_Type = Gauge32
_VsvmPhysicalMemoryAllocated_Object = MibTableColumn
vsvmPhysicalMemoryAllocated = _VsvmPhysicalMemoryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 15),
    _VsvmPhysicalMemoryAllocated_Type()
)
vsvmPhysicalMemoryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmPhysicalMemoryAllocated.setStatus("current")
if mibBuilder.loadTexts:
    vsvmPhysicalMemoryAllocated.setUnits("Bytes")
_VsvmPhysicalMemoryAllocatedK_Type = Gauge32
_VsvmPhysicalMemoryAllocatedK_Object = MibTableColumn
vsvmPhysicalMemoryAllocatedK = _VsvmPhysicalMemoryAllocatedK_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 16),
    _VsvmPhysicalMemoryAllocatedK_Type()
)
vsvmPhysicalMemoryAllocatedK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmPhysicalMemoryAllocatedK.setStatus("current")
if mibBuilder.loadTexts:
    vsvmPhysicalMemoryAllocatedK.setUnits("KiloBytes")
_VsvmPhysicalMemoryAllocatedM_Type = Gauge32
_VsvmPhysicalMemoryAllocatedM_Object = MibTableColumn
vsvmPhysicalMemoryAllocatedM = _VsvmPhysicalMemoryAllocatedM_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 17),
    _VsvmPhysicalMemoryAllocatedM_Type()
)
vsvmPhysicalMemoryAllocatedM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmPhysicalMemoryAllocatedM.setStatus("current")
if mibBuilder.loadTexts:
    vsvmPhysicalMemoryAllocatedM.setUnits("MegaBytes")
_VsvmUptime_Type = Gauge32
_VsvmUptime_Object = MibTableColumn
vsvmUptime = _VsvmUptime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 1, 1, 18),
    _VsvmUptime_Type()
)
vsvmUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvmUptime.setStatus("current")
if mibBuilder.loadTexts:
    vsvmUptime.setUnits("Seconds")
_VsVirtualNetworkTable_Object = MibTable
vsVirtualNetworkTable = _VsVirtualNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2)
)
if mibBuilder.loadTexts:
    vsVirtualNetworkTable.setStatus("current")
_VsVirtualNetworkEntry_Object = MibTableRow
vsVirtualNetworkEntry = _VsVirtualNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1)
)
vsVirtualNetworkEntry.setIndexNames(
    (0, "INFORMANT-VS", "vsvnIndex"),
)
if mibBuilder.loadTexts:
    vsVirtualNetworkEntry.setStatus("current")


class _VsvnIndex_Type(Integer32):
    """Custom type vsvnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VsvnIndex_Type.__name__ = "Integer32"
_VsvnIndex_Object = MibTableColumn
vsvnIndex = _VsvnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 1),
    _VsvnIndex_Type()
)
vsvnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnIndex.setStatus("current")
_VsvnName_Type = WtcsDisplayString
_VsvnName_Object = MibTableColumn
vsvnName = _VsvnName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 2),
    _VsvnName_Type()
)
vsvnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnName.setStatus("current")
_VsvnBytesDropped_Type = Counter64
_VsvnBytesDropped_Object = MibTableColumn
vsvnBytesDropped = _VsvnBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 3),
    _VsvnBytesDropped_Type()
)
vsvnBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnBytesDropped.setStatus("current")
if mibBuilder.loadTexts:
    vsvnBytesDropped.setUnits("Bytes")
_VsvnBytesReceived_Type = Counter64
_VsvnBytesReceived_Object = MibTableColumn
vsvnBytesReceived = _VsvnBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 4),
    _VsvnBytesReceived_Type()
)
vsvnBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    vsvnBytesReceived.setUnits("Bytes")
_VsvnBytesSent_Type = Counter64
_VsvnBytesSent_Object = MibTableColumn
vsvnBytesSent = _VsvnBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 5),
    _VsvnBytesSent_Type()
)
vsvnBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    vsvnBytesSent.setUnits("Bytes")
_VsvnPacketsDropped_Type = Counter64
_VsvnPacketsDropped_Object = MibTableColumn
vsvnPacketsDropped = _VsvnPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 6),
    _VsvnPacketsDropped_Type()
)
vsvnPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    vsvnPacketsDropped.setUnits("Packets")
_VsvnPacketsReceived_Type = Counter64
_VsvnPacketsReceived_Object = MibTableColumn
vsvnPacketsReceived = _VsvnPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 7),
    _VsvnPacketsReceived_Type()
)
vsvnPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    vsvnPacketsReceived.setUnits("Packets")
_VsvnPacketsSent_Type = Counter64
_VsvnPacketsSent_Object = MibTableColumn
vsvnPacketsSent = _VsvnPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 24, 2, 1, 8),
    _VsvnPacketsSent_Type()
)
vsvnPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsvnPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    vsvnPacketsSent.setUnits("Packets")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-VS",
    **{"wmiVirtualServer": wmiVirtualServer,
       "vsVirtualMachineTable": vsVirtualMachineTable,
       "vsVirtualMachineEntry": vsVirtualMachineEntry,
       "vsvmIndex": vsvmIndex,
       "vsvmName": vsvmName,
       "vsvmCpuUtilization": vsvmCpuUtilization,
       "vsvmDiskBytesRead": vsvmDiskBytesRead,
       "vsvmDiskSpaceUsed": vsvmDiskSpaceUsed,
       "vsvmDiskSpaceUsedK": vsvmDiskSpaceUsedK,
       "vsvmDiskSpaceUsedM": vsvmDiskSpaceUsedM,
       "vsvmDiskBytesWritten": vsvmDiskBytesWritten,
       "vsvmHeartbeatCount": vsvmHeartbeatCount,
       "vsvmHeartbeatInterval": vsvmHeartbeatInterval,
       "vsvmHeartbeatPercentage": vsvmHeartbeatPercentage,
       "vsvmHeartbeatRate": vsvmHeartbeatRate,
       "vsvmNetworkBytesSent": vsvmNetworkBytesSent,
       "vsvmNetworkBytesReceived": vsvmNetworkBytesReceived,
       "vsvmPhysicalMemoryAllocated": vsvmPhysicalMemoryAllocated,
       "vsvmPhysicalMemoryAllocatedK": vsvmPhysicalMemoryAllocatedK,
       "vsvmPhysicalMemoryAllocatedM": vsvmPhysicalMemoryAllocatedM,
       "vsvmUptime": vsvmUptime,
       "vsVirtualNetworkTable": vsVirtualNetworkTable,
       "vsVirtualNetworkEntry": vsVirtualNetworkEntry,
       "vsvnIndex": vsvnIndex,
       "vsvnName": vsvnName,
       "vsvnBytesDropped": vsvnBytesDropped,
       "vsvnBytesReceived": vsvnBytesReceived,
       "vsvnBytesSent": vsvnBytesSent,
       "vsvnPacketsDropped": vsvnPacketsDropped,
       "vsvnPacketsReceived": vsvnPacketsReceived,
       "vsvnPacketsSent": vsvnPacketsSent}
)
