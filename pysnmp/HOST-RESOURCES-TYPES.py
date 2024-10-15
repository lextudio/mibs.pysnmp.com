# SNMP MIB module (HOST-RESOURCES-TYPES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HOST-RESOURCES-TYPES
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:48 2024
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

(hrDevice,
 hrMIBAdminInfo,
 hrStorage) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDevice",
    "hrMIBAdminInfo",
    "hrStorage")

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

hostResourcesTypesModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7, 4)
)
hostResourcesTypesModule.setRevisions(
        ("2000-03-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HrStorageTypes_ObjectIdentity = ObjectIdentity
hrStorageTypes = _HrStorageTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1)
)
_HrStorageOther_ObjectIdentity = ObjectIdentity
hrStorageOther = _HrStorageOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hrStorageOther.setStatus("current")
_HrStorageRam_ObjectIdentity = ObjectIdentity
hrStorageRam = _HrStorageRam_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hrStorageRam.setStatus("current")
_HrStorageVirtualMemory_ObjectIdentity = ObjectIdentity
hrStorageVirtualMemory = _HrStorageVirtualMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hrStorageVirtualMemory.setStatus("current")
_HrStorageFixedDisk_ObjectIdentity = ObjectIdentity
hrStorageFixedDisk = _HrStorageFixedDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hrStorageFixedDisk.setStatus("current")
_HrStorageRemovableDisk_ObjectIdentity = ObjectIdentity
hrStorageRemovableDisk = _HrStorageRemovableDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hrStorageRemovableDisk.setStatus("current")
_HrStorageFloppyDisk_ObjectIdentity = ObjectIdentity
hrStorageFloppyDisk = _HrStorageFloppyDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hrStorageFloppyDisk.setStatus("current")
_HrStorageCompactDisc_ObjectIdentity = ObjectIdentity
hrStorageCompactDisc = _HrStorageCompactDisc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hrStorageCompactDisc.setStatus("current")
_HrStorageRamDisk_ObjectIdentity = ObjectIdentity
hrStorageRamDisk = _HrStorageRamDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hrStorageRamDisk.setStatus("current")
_HrStorageFlashMemory_ObjectIdentity = ObjectIdentity
hrStorageFlashMemory = _HrStorageFlashMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hrStorageFlashMemory.setStatus("current")
_HrStorageNetworkDisk_ObjectIdentity = ObjectIdentity
hrStorageNetworkDisk = _HrStorageNetworkDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hrStorageNetworkDisk.setStatus("current")
_HrDeviceTypes_ObjectIdentity = ObjectIdentity
hrDeviceTypes = _HrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1)
)
_HrDeviceOther_ObjectIdentity = ObjectIdentity
hrDeviceOther = _HrDeviceOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hrDeviceOther.setStatus("current")
_HrDeviceUnknown_ObjectIdentity = ObjectIdentity
hrDeviceUnknown = _HrDeviceUnknown_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hrDeviceUnknown.setStatus("current")
_HrDeviceProcessor_ObjectIdentity = ObjectIdentity
hrDeviceProcessor = _HrDeviceProcessor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hrDeviceProcessor.setStatus("current")
_HrDeviceNetwork_ObjectIdentity = ObjectIdentity
hrDeviceNetwork = _HrDeviceNetwork_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hrDeviceNetwork.setStatus("current")
_HrDevicePrinter_ObjectIdentity = ObjectIdentity
hrDevicePrinter = _HrDevicePrinter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hrDevicePrinter.setStatus("current")
_HrDeviceDiskStorage_ObjectIdentity = ObjectIdentity
hrDeviceDiskStorage = _HrDeviceDiskStorage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hrDeviceDiskStorage.setStatus("current")
_HrDeviceVideo_ObjectIdentity = ObjectIdentity
hrDeviceVideo = _HrDeviceVideo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hrDeviceVideo.setStatus("current")
_HrDeviceAudio_ObjectIdentity = ObjectIdentity
hrDeviceAudio = _HrDeviceAudio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 11)
)
if mibBuilder.loadTexts:
    hrDeviceAudio.setStatus("current")
_HrDeviceCoprocessor_ObjectIdentity = ObjectIdentity
hrDeviceCoprocessor = _HrDeviceCoprocessor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 12)
)
if mibBuilder.loadTexts:
    hrDeviceCoprocessor.setStatus("current")
_HrDeviceKeyboard_ObjectIdentity = ObjectIdentity
hrDeviceKeyboard = _HrDeviceKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 13)
)
if mibBuilder.loadTexts:
    hrDeviceKeyboard.setStatus("current")
_HrDeviceModem_ObjectIdentity = ObjectIdentity
hrDeviceModem = _HrDeviceModem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 14)
)
if mibBuilder.loadTexts:
    hrDeviceModem.setStatus("current")
_HrDeviceParallelPort_ObjectIdentity = ObjectIdentity
hrDeviceParallelPort = _HrDeviceParallelPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 15)
)
if mibBuilder.loadTexts:
    hrDeviceParallelPort.setStatus("current")
_HrDevicePointing_ObjectIdentity = ObjectIdentity
hrDevicePointing = _HrDevicePointing_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 16)
)
if mibBuilder.loadTexts:
    hrDevicePointing.setStatus("current")
_HrDeviceSerialPort_ObjectIdentity = ObjectIdentity
hrDeviceSerialPort = _HrDeviceSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 17)
)
if mibBuilder.loadTexts:
    hrDeviceSerialPort.setStatus("current")
_HrDeviceTape_ObjectIdentity = ObjectIdentity
hrDeviceTape = _HrDeviceTape_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 18)
)
if mibBuilder.loadTexts:
    hrDeviceTape.setStatus("current")
_HrDeviceClock_ObjectIdentity = ObjectIdentity
hrDeviceClock = _HrDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 19)
)
if mibBuilder.loadTexts:
    hrDeviceClock.setStatus("current")
_HrDeviceVolatileMemory_ObjectIdentity = ObjectIdentity
hrDeviceVolatileMemory = _HrDeviceVolatileMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 20)
)
if mibBuilder.loadTexts:
    hrDeviceVolatileMemory.setStatus("current")
_HrDeviceNonVolatileMemory_ObjectIdentity = ObjectIdentity
hrDeviceNonVolatileMemory = _HrDeviceNonVolatileMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 21)
)
if mibBuilder.loadTexts:
    hrDeviceNonVolatileMemory.setStatus("current")
_HrFSTypes_ObjectIdentity = ObjectIdentity
hrFSTypes = _HrFSTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9)
)
_HrFSOther_ObjectIdentity = ObjectIdentity
hrFSOther = _HrFSOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 1)
)
if mibBuilder.loadTexts:
    hrFSOther.setStatus("current")
_HrFSUnknown_ObjectIdentity = ObjectIdentity
hrFSUnknown = _HrFSUnknown_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 2)
)
if mibBuilder.loadTexts:
    hrFSUnknown.setStatus("current")
_HrFSBerkeleyFFS_ObjectIdentity = ObjectIdentity
hrFSBerkeleyFFS = _HrFSBerkeleyFFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 3)
)
if mibBuilder.loadTexts:
    hrFSBerkeleyFFS.setStatus("current")
_HrFSSys5FS_ObjectIdentity = ObjectIdentity
hrFSSys5FS = _HrFSSys5FS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 4)
)
if mibBuilder.loadTexts:
    hrFSSys5FS.setStatus("current")
_HrFSFat_ObjectIdentity = ObjectIdentity
hrFSFat = _HrFSFat_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 5)
)
if mibBuilder.loadTexts:
    hrFSFat.setStatus("current")
_HrFSHPFS_ObjectIdentity = ObjectIdentity
hrFSHPFS = _HrFSHPFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 6)
)
if mibBuilder.loadTexts:
    hrFSHPFS.setStatus("current")
_HrFSHFS_ObjectIdentity = ObjectIdentity
hrFSHFS = _HrFSHFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 7)
)
if mibBuilder.loadTexts:
    hrFSHFS.setStatus("current")
_HrFSMFS_ObjectIdentity = ObjectIdentity
hrFSMFS = _HrFSMFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 8)
)
if mibBuilder.loadTexts:
    hrFSMFS.setStatus("current")
_HrFSNTFS_ObjectIdentity = ObjectIdentity
hrFSNTFS = _HrFSNTFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 9)
)
if mibBuilder.loadTexts:
    hrFSNTFS.setStatus("current")
_HrFSVNode_ObjectIdentity = ObjectIdentity
hrFSVNode = _HrFSVNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 10)
)
if mibBuilder.loadTexts:
    hrFSVNode.setStatus("current")
_HrFSJournaled_ObjectIdentity = ObjectIdentity
hrFSJournaled = _HrFSJournaled_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 11)
)
if mibBuilder.loadTexts:
    hrFSJournaled.setStatus("current")
_HrFSiso9660_ObjectIdentity = ObjectIdentity
hrFSiso9660 = _HrFSiso9660_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 12)
)
if mibBuilder.loadTexts:
    hrFSiso9660.setStatus("current")
_HrFSRockRidge_ObjectIdentity = ObjectIdentity
hrFSRockRidge = _HrFSRockRidge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 13)
)
if mibBuilder.loadTexts:
    hrFSRockRidge.setStatus("current")
_HrFSNFS_ObjectIdentity = ObjectIdentity
hrFSNFS = _HrFSNFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 14)
)
if mibBuilder.loadTexts:
    hrFSNFS.setStatus("current")
_HrFSNetware_ObjectIdentity = ObjectIdentity
hrFSNetware = _HrFSNetware_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 15)
)
if mibBuilder.loadTexts:
    hrFSNetware.setStatus("current")
_HrFSAFS_ObjectIdentity = ObjectIdentity
hrFSAFS = _HrFSAFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 16)
)
if mibBuilder.loadTexts:
    hrFSAFS.setStatus("current")
_HrFSDFS_ObjectIdentity = ObjectIdentity
hrFSDFS = _HrFSDFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 17)
)
if mibBuilder.loadTexts:
    hrFSDFS.setStatus("current")
_HrFSAppleshare_ObjectIdentity = ObjectIdentity
hrFSAppleshare = _HrFSAppleshare_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 18)
)
if mibBuilder.loadTexts:
    hrFSAppleshare.setStatus("current")
_HrFSRFS_ObjectIdentity = ObjectIdentity
hrFSRFS = _HrFSRFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 19)
)
if mibBuilder.loadTexts:
    hrFSRFS.setStatus("current")
_HrFSDGCFS_ObjectIdentity = ObjectIdentity
hrFSDGCFS = _HrFSDGCFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 20)
)
if mibBuilder.loadTexts:
    hrFSDGCFS.setStatus("current")
_HrFSBFS_ObjectIdentity = ObjectIdentity
hrFSBFS = _HrFSBFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 21)
)
if mibBuilder.loadTexts:
    hrFSBFS.setStatus("current")
_HrFSFAT32_ObjectIdentity = ObjectIdentity
hrFSFAT32 = _HrFSFAT32_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 22)
)
if mibBuilder.loadTexts:
    hrFSFAT32.setStatus("current")
_HrFSLinuxExt2_ObjectIdentity = ObjectIdentity
hrFSLinuxExt2 = _HrFSLinuxExt2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 23)
)
if mibBuilder.loadTexts:
    hrFSLinuxExt2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HOST-RESOURCES-TYPES",
    **{"hrStorageTypes": hrStorageTypes,
       "hrStorageOther": hrStorageOther,
       "hrStorageRam": hrStorageRam,
       "hrStorageVirtualMemory": hrStorageVirtualMemory,
       "hrStorageFixedDisk": hrStorageFixedDisk,
       "hrStorageRemovableDisk": hrStorageRemovableDisk,
       "hrStorageFloppyDisk": hrStorageFloppyDisk,
       "hrStorageCompactDisc": hrStorageCompactDisc,
       "hrStorageRamDisk": hrStorageRamDisk,
       "hrStorageFlashMemory": hrStorageFlashMemory,
       "hrStorageNetworkDisk": hrStorageNetworkDisk,
       "hrDeviceTypes": hrDeviceTypes,
       "hrDeviceOther": hrDeviceOther,
       "hrDeviceUnknown": hrDeviceUnknown,
       "hrDeviceProcessor": hrDeviceProcessor,
       "hrDeviceNetwork": hrDeviceNetwork,
       "hrDevicePrinter": hrDevicePrinter,
       "hrDeviceDiskStorage": hrDeviceDiskStorage,
       "hrDeviceVideo": hrDeviceVideo,
       "hrDeviceAudio": hrDeviceAudio,
       "hrDeviceCoprocessor": hrDeviceCoprocessor,
       "hrDeviceKeyboard": hrDeviceKeyboard,
       "hrDeviceModem": hrDeviceModem,
       "hrDeviceParallelPort": hrDeviceParallelPort,
       "hrDevicePointing": hrDevicePointing,
       "hrDeviceSerialPort": hrDeviceSerialPort,
       "hrDeviceTape": hrDeviceTape,
       "hrDeviceClock": hrDeviceClock,
       "hrDeviceVolatileMemory": hrDeviceVolatileMemory,
       "hrDeviceNonVolatileMemory": hrDeviceNonVolatileMemory,
       "hrFSTypes": hrFSTypes,
       "hrFSOther": hrFSOther,
       "hrFSUnknown": hrFSUnknown,
       "hrFSBerkeleyFFS": hrFSBerkeleyFFS,
       "hrFSSys5FS": hrFSSys5FS,
       "hrFSFat": hrFSFat,
       "hrFSHPFS": hrFSHPFS,
       "hrFSHFS": hrFSHFS,
       "hrFSMFS": hrFSMFS,
       "hrFSNTFS": hrFSNTFS,
       "hrFSVNode": hrFSVNode,
       "hrFSJournaled": hrFSJournaled,
       "hrFSiso9660": hrFSiso9660,
       "hrFSRockRidge": hrFSRockRidge,
       "hrFSNFS": hrFSNFS,
       "hrFSNetware": hrFSNetware,
       "hrFSAFS": hrFSAFS,
       "hrFSDFS": hrFSDFS,
       "hrFSAppleshare": hrFSAppleshare,
       "hrFSRFS": hrFSRFS,
       "hrFSDGCFS": hrFSDGCFS,
       "hrFSBFS": hrFSBFS,
       "hrFSFAT32": hrFSFAT32,
       "hrFSLinuxExt2": hrFSLinuxExt2,
       "hostResourcesTypesModule": hostResourcesTypesModule}
)
