# SNMP MIB module (SYSTEM-RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYSTEM-RESOURCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:16 2024
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

(ctResource,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctResource")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysResourceInstalled_ObjectIdentity = ObjectIdentity
sysResourceInstalled = _SysResourceInstalled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1)
)
_SysResourceCpuTable_Object = MibTable
sysResourceCpuTable = _SysResourceCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    sysResourceCpuTable.setStatus("mandatory")
_SysResourceCpuEntry_Object = MibTableRow
sysResourceCpuEntry = _SysResourceCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1)
)
sysResourceCpuEntry.setIndexNames(
    (0, "SYSTEM-RESOURCE-MIB", "sysResSlotID"),
    (0, "SYSTEM-RESOURCE-MIB", "sysResCpuIndex"),
)
if mibBuilder.loadTexts:
    sysResourceCpuEntry.setStatus("mandatory")
_SysResSlotID_Type = Integer32
_SysResSlotID_Object = MibTableColumn
sysResSlotID = _SysResSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1, 1),
    _SysResSlotID_Type()
)
sysResSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResSlotID.setStatus("mandatory")
_SysResCpuIndex_Type = Integer32
_SysResCpuIndex_Object = MibTableColumn
sysResCpuIndex = _SysResCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1, 2),
    _SysResCpuIndex_Type()
)
sysResCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResCpuIndex.setStatus("mandatory")
_SysResCpuType_Type = ObjectIdentifier
_SysResCpuType_Object = MibTableColumn
sysResCpuType = _SysResCpuType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1, 3),
    _SysResCpuType_Type()
)
sysResCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResCpuType.setStatus("mandatory")
_SysResCpuSpeed_Type = Integer32
_SysResCpuSpeed_Object = MibTableColumn
sysResCpuSpeed = _SysResCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1, 4),
    _SysResCpuSpeed_Type()
)
sysResCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResCpuSpeed.setStatus("mandatory")
_SysResCpuID_Type = Integer32
_SysResCpuID_Object = MibTableColumn
sysResCpuID = _SysResCpuID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1, 5),
    _SysResCpuID_Type()
)
sysResCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResCpuID.setStatus("mandatory")
_SysResInstalledLocalMemory_Type = Integer32
_SysResInstalledLocalMemory_Object = MibTableColumn
sysResInstalledLocalMemory = _SysResInstalledLocalMemory_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1, 6),
    _SysResInstalledLocalMemory_Type()
)
sysResInstalledLocalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResInstalledLocalMemory.setStatus("mandatory")
_SysResUsedLocalMemory_Type = Integer32
_SysResUsedLocalMemory_Object = MibTableColumn
sysResUsedLocalMemory = _SysResUsedLocalMemory_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 1, 1, 7),
    _SysResUsedLocalMemory_Type()
)
sysResUsedLocalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResUsedLocalMemory.setStatus("mandatory")
_SysResourceTable_Object = MibTable
sysResourceTable = _SysResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    sysResourceTable.setStatus("mandatory")
_SysResourceEntry_Object = MibTableRow
sysResourceEntry = _SysResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2, 1)
)
sysResourceEntry.setIndexNames(
    (0, "SYSTEM-RESOURCE-MIB", "sysResSlotID"),
    (0, "SYSTEM-RESOURCE-MIB", "sysResCpuIndex"),
)
if mibBuilder.loadTexts:
    sysResourceEntry.setStatus("mandatory")
_SysResInstalledNvram_Type = Integer32
_SysResInstalledNvram_Object = MibTableColumn
sysResInstalledNvram = _SysResInstalledNvram_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2, 1, 1),
    _SysResInstalledNvram_Type()
)
sysResInstalledNvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResInstalledNvram.setStatus("mandatory")
_SysResInstalledFlash_Type = Integer32
_SysResInstalledFlash_Object = MibTableColumn
sysResInstalledFlash = _SysResInstalledFlash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2, 1, 2),
    _SysResInstalledFlash_Type()
)
sysResInstalledFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResInstalledFlash.setStatus("mandatory")
_SysResInstalledSharedMemory_Type = Integer32
_SysResInstalledSharedMemory_Object = MibTableColumn
sysResInstalledSharedMemory = _SysResInstalledSharedMemory_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2, 1, 3),
    _SysResInstalledSharedMemory_Type()
)
sysResInstalledSharedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResInstalledSharedMemory.setStatus("mandatory")
_SysResUsedNvram_Type = Integer32
_SysResUsedNvram_Object = MibTableColumn
sysResUsedNvram = _SysResUsedNvram_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2, 1, 4),
    _SysResUsedNvram_Type()
)
sysResUsedNvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResUsedNvram.setStatus("mandatory")
_SysResUsedFlash_Type = Integer32
_SysResUsedFlash_Object = MibTableColumn
sysResUsedFlash = _SysResUsedFlash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2, 1, 5),
    _SysResUsedFlash_Type()
)
sysResUsedFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResUsedFlash.setStatus("mandatory")
_SysResUsedSharedMemory_Type = Integer32
_SysResUsedSharedMemory_Object = MibTableColumn
sysResUsedSharedMemory = _SysResUsedSharedMemory_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 1, 2, 1, 6),
    _SysResUsedSharedMemory_Type()
)
sysResUsedSharedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResUsedSharedMemory.setStatus("mandatory")
_SysResourceSwitch_ObjectIdentity = ObjectIdentity
sysResourceSwitch = _SysResourceSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 2)
)


class _SysResManagementCpuResource_Type(Integer32):
    """Custom type sysResManagementCpuResource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("limited", 2),
          ("none", 1))
    )


_SysResManagementCpuResource_Type.__name__ = "Integer32"
_SysResManagementCpuResource_Object = MibScalar
sysResManagementCpuResource = _SysResManagementCpuResource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 2, 1),
    _SysResManagementCpuResource_Type()
)
sysResManagementCpuResource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResManagementCpuResource.setStatus("mandatory")
_SwitchLoad_Type = Integer32
_SwitchLoad_Object = MibScalar
switchLoad = _SwitchLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 2, 2),
    _SwitchLoad_Type()
)
switchLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchLoad.setStatus("mandatory")
_PeakSwitchload_Type = Integer32
_PeakSwitchload_Object = MibScalar
peakSwitchload = _PeakSwitchload_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 2, 3),
    _PeakSwitchload_Type()
)
peakSwitchload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakSwitchload.setStatus("mandatory")
_PeakSwitchLoadTime_Type = TimeTicks
_PeakSwitchLoadTime_Object = MibScalar
peakSwitchLoadTime = _PeakSwitchLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 2, 4),
    _PeakSwitchLoadTime_Type()
)
peakSwitchLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakSwitchLoadTime.setStatus("mandatory")


class _PeakSwitchClear_Type(Integer32):
    """Custom type peakSwitchClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noClear", 2))
    )


_PeakSwitchClear_Type.__name__ = "Integer32"
_PeakSwitchClear_Object = MibScalar
peakSwitchClear = _PeakSwitchClear_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 2, 5),
    _PeakSwitchClear_Type()
)
peakSwitchClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakSwitchClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSTEM-RESOURCE-MIB",
    **{"sysResourceInstalled": sysResourceInstalled,
       "sysResourceCpuTable": sysResourceCpuTable,
       "sysResourceCpuEntry": sysResourceCpuEntry,
       "sysResSlotID": sysResSlotID,
       "sysResCpuIndex": sysResCpuIndex,
       "sysResCpuType": sysResCpuType,
       "sysResCpuSpeed": sysResCpuSpeed,
       "sysResCpuID": sysResCpuID,
       "sysResInstalledLocalMemory": sysResInstalledLocalMemory,
       "sysResUsedLocalMemory": sysResUsedLocalMemory,
       "sysResourceTable": sysResourceTable,
       "sysResourceEntry": sysResourceEntry,
       "sysResInstalledNvram": sysResInstalledNvram,
       "sysResInstalledFlash": sysResInstalledFlash,
       "sysResInstalledSharedMemory": sysResInstalledSharedMemory,
       "sysResUsedNvram": sysResUsedNvram,
       "sysResUsedFlash": sysResUsedFlash,
       "sysResUsedSharedMemory": sysResUsedSharedMemory,
       "sysResourceSwitch": sysResourceSwitch,
       "sysResManagementCpuResource": sysResManagementCpuResource,
       "switchLoad": switchLoad,
       "peakSwitchload": peakSwitchload,
       "peakSwitchLoadTime": peakSwitchLoadTime,
       "peakSwitchClear": peakSwitchClear}
)
