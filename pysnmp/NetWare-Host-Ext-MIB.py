# SNMP MIB module (NetWare-Host-Ext-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NetWare-Host-Ext-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:06 2024
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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



class TransportDomain(Integer32):
    """Custom type TransportDomain based on Integer32"""
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
        *(("appleTalkDDP", 4),
          ("ip", 3),
          ("ipx", 2),
          ("noAddress", 1))
    )





class TransportAddress(OctetString):
    """Custom type TransportAddress based on OctetString"""




class KBytes(Integer32):
    """Custom type KBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class InternationalDisplayString(OctetString):
    """Custom type InternationalDisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_NwHostExtensions_ObjectIdentity = ObjectIdentity
nwHostExtensions = _NwHostExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27)
)
_NwhrStorage_ObjectIdentity = ObjectIdentity
nwhrStorage = _NwhrStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2)
)
_NwhrStorageTypes_ObjectIdentity = ObjectIdentity
nwhrStorageTypes = _NwhrStorageTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1)
)
_NwhrStorageVolume_ObjectIdentity = ObjectIdentity
nwhrStorageVolume = _NwhrStorageVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 1)
)
_NwhrStorageMemoryPermanent_ObjectIdentity = ObjectIdentity
nwhrStorageMemoryPermanent = _NwhrStorageMemoryPermanent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 2)
)
_NwhrStorageMemoryAlloc_ObjectIdentity = ObjectIdentity
nwhrStorageMemoryAlloc = _NwhrStorageMemoryAlloc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 3)
)
_NwhrStorageCacheBuffers_ObjectIdentity = ObjectIdentity
nwhrStorageCacheBuffers = _NwhrStorageCacheBuffers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 4)
)
_NwhrStorageCacheMovable_ObjectIdentity = ObjectIdentity
nwhrStorageCacheMovable = _NwhrStorageCacheMovable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 5)
)
_NwhrStorageCacheNonMovable_ObjectIdentity = ObjectIdentity
nwhrStorageCacheNonMovable = _NwhrStorageCacheNonMovable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 6)
)
_NwhrStorageCodeAndDataMemory_ObjectIdentity = ObjectIdentity
nwhrStorageCodeAndDataMemory = _NwhrStorageCodeAndDataMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 7)
)
_NwhrStorageDOSMemory_ObjectIdentity = ObjectIdentity
nwhrStorageDOSMemory = _NwhrStorageDOSMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 8)
)
_NwhrStorageIOEngineMemory_ObjectIdentity = ObjectIdentity
nwhrStorageIOEngineMemory = _NwhrStorageIOEngineMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 9)
)
_NwhrStorageMSEngineMemory_ObjectIdentity = ObjectIdentity
nwhrStorageMSEngineMemory = _NwhrStorageMSEngineMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 10)
)
_NwhrStorageUnclaimedMemory_ObjectIdentity = ObjectIdentity
nwhrStorageUnclaimedMemory = _NwhrStorageUnclaimedMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 11)
)
_NwhrDevice_ObjectIdentity = ObjectIdentity
nwhrDevice = _NwhrDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3)
)
_NwhrDeviceTypes_ObjectIdentity = ObjectIdentity
nwhrDeviceTypes = _NwhrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 1)
)
_NwhrDeviceMirroredServerLink_ObjectIdentity = ObjectIdentity
nwhrDeviceMirroredServerLink = _NwhrDeviceMirroredServerLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 1, 1)
)
_NwhrDeviceTable_Object = MibTable
nwhrDeviceTable = _NwhrDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2)
)
if mibBuilder.loadTexts:
    nwhrDeviceTable.setStatus("mandatory")
_NwhrDeviceEntry_Object = MibTableRow
nwhrDeviceEntry = _NwhrDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1)
)
nwhrDeviceEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    nwhrDeviceEntry.setStatus("mandatory")
_NwhrDeviceAdapterIndex_Type = Integer32
_NwhrDeviceAdapterIndex_Object = MibTableColumn
nwhrDeviceAdapterIndex = _NwhrDeviceAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1, 1),
    _NwhrDeviceAdapterIndex_Type()
)
nwhrDeviceAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDeviceAdapterIndex.setStatus("mandatory")
_NwhrDeviceControllerNumber_Type = Integer32
_NwhrDeviceControllerNumber_Object = MibTableColumn
nwhrDeviceControllerNumber = _NwhrDeviceControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1, 2),
    _NwhrDeviceControllerNumber_Type()
)
nwhrDeviceControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDeviceControllerNumber.setStatus("mandatory")
_NwhrDeviceNumber_Type = Integer32
_NwhrDeviceNumber_Object = MibTableColumn
nwhrDeviceNumber = _NwhrDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1, 3),
    _NwhrDeviceNumber_Type()
)
nwhrDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDeviceNumber.setStatus("mandatory")
_NwhrProcessorCount_Type = Integer32
_NwhrProcessorCount_Object = MibScalar
nwhrProcessorCount = _NwhrProcessorCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 3),
    _NwhrProcessorCount_Type()
)
nwhrProcessorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProcessorCount.setStatus("mandatory")
_NwhrPrinterCount_Type = Integer32
_NwhrPrinterCount_Object = MibScalar
nwhrPrinterCount = _NwhrPrinterCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 4),
    _NwhrPrinterCount_Type()
)
nwhrPrinterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterCount.setStatus("mandatory")
_NwhrDiskStorageCount_Type = Integer32
_NwhrDiskStorageCount_Object = MibScalar
nwhrDiskStorageCount = _NwhrDiskStorageCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 5),
    _NwhrDiskStorageCount_Type()
)
nwhrDiskStorageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDiskStorageCount.setStatus("mandatory")
_NwhrDiskStorageTable_Object = MibTable
nwhrDiskStorageTable = _NwhrDiskStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6)
)
if mibBuilder.loadTexts:
    nwhrDiskStorageTable.setStatus("mandatory")
_NwhrDiskStorageEntry_Object = MibTableRow
nwhrDiskStorageEntry = _NwhrDiskStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1)
)
nwhrDiskStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    nwhrDiskStorageEntry.setStatus("mandatory")
_NwhrDiskStorageHeads_Type = Integer32
_NwhrDiskStorageHeads_Object = MibTableColumn
nwhrDiskStorageHeads = _NwhrDiskStorageHeads_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 1),
    _NwhrDiskStorageHeads_Type()
)
nwhrDiskStorageHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDiskStorageHeads.setStatus("mandatory")
_NwhrDiskStorageCylinders_Type = Integer32
_NwhrDiskStorageCylinders_Object = MibTableColumn
nwhrDiskStorageCylinders = _NwhrDiskStorageCylinders_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 2),
    _NwhrDiskStorageCylinders_Type()
)
nwhrDiskStorageCylinders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDiskStorageCylinders.setStatus("mandatory")
_NwhrDiskStorageSectorsPerTrack_Type = Integer32
_NwhrDiskStorageSectorsPerTrack_Object = MibTableColumn
nwhrDiskStorageSectorsPerTrack = _NwhrDiskStorageSectorsPerTrack_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 3),
    _NwhrDiskStorageSectorsPerTrack_Type()
)
nwhrDiskStorageSectorsPerTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDiskStorageSectorsPerTrack.setStatus("mandatory")
_NwhrDiskStorageSectorSize_Type = Integer32
_NwhrDiskStorageSectorSize_Object = MibTableColumn
nwhrDiskStorageSectorSize = _NwhrDiskStorageSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 4),
    _NwhrDiskStorageSectorSize_Type()
)
nwhrDiskStorageSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDiskStorageSectorSize.setStatus("mandatory")
_NwhrDiskStorageBlockSize_Type = Integer32
_NwhrDiskStorageBlockSize_Object = MibTableColumn
nwhrDiskStorageBlockSize = _NwhrDiskStorageBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 5),
    _NwhrDiskStorageBlockSize_Type()
)
nwhrDiskStorageBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrDiskStorageBlockSize.setStatus("mandatory")
_NwhrPhysicalPartitionTable_Object = MibTable
nwhrPhysicalPartitionTable = _NwhrPhysicalPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7)
)
if mibBuilder.loadTexts:
    nwhrPhysicalPartitionTable.setStatus("mandatory")
_NwhrPhysicalPartitionEntry_Object = MibTableRow
nwhrPhysicalPartitionEntry = _NwhrPhysicalPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1)
)
nwhrPhysicalPartitionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "NetWare-Host-Ext-MIB", "nwhrPhysicalPartitionIndex"),
)
if mibBuilder.loadTexts:
    nwhrPhysicalPartitionEntry.setStatus("mandatory")


class _NwhrPhysicalPartitionIndex_Type(Integer32):
    """Custom type nwhrPhysicalPartitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NwhrPhysicalPartitionIndex_Type.__name__ = "Integer32"
_NwhrPhysicalPartitionIndex_Object = MibTableColumn
nwhrPhysicalPartitionIndex = _NwhrPhysicalPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 1),
    _NwhrPhysicalPartitionIndex_Type()
)
nwhrPhysicalPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPhysicalPartitionIndex.setStatus("mandatory")


class _NwhrPhysicalPartitionType_Type(Integer32):
    """Custom type nwhrPhysicalPartitionType based on Integer32"""
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
        *(("dos", 3),
          ("inwDos", 4),
          ("netWare", 2),
          ("other", 1))
    )


_NwhrPhysicalPartitionType_Type.__name__ = "Integer32"
_NwhrPhysicalPartitionType_Object = MibTableColumn
nwhrPhysicalPartitionType = _NwhrPhysicalPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 2),
    _NwhrPhysicalPartitionType_Type()
)
nwhrPhysicalPartitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPhysicalPartitionType.setStatus("mandatory")


class _NwhrPhysicalPartitionDescr_Type(InternationalDisplayString):
    """Custom type nwhrPhysicalPartitionDescr based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NwhrPhysicalPartitionDescr_Type.__name__ = "InternationalDisplayString"
_NwhrPhysicalPartitionDescr_Object = MibTableColumn
nwhrPhysicalPartitionDescr = _NwhrPhysicalPartitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 3),
    _NwhrPhysicalPartitionDescr_Type()
)
nwhrPhysicalPartitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPhysicalPartitionDescr.setStatus("mandatory")
_NwhrPhysicalPartitionSize_Type = KBytes
_NwhrPhysicalPartitionSize_Object = MibTableColumn
nwhrPhysicalPartitionSize = _NwhrPhysicalPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 4),
    _NwhrPhysicalPartitionSize_Type()
)
nwhrPhysicalPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPhysicalPartitionSize.setStatus("mandatory")
_NwhrHotfixTable_Object = MibTable
nwhrHotfixTable = _NwhrHotfixTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8)
)
if mibBuilder.loadTexts:
    nwhrHotfixTable.setStatus("mandatory")
_NwhrHotfixEntry_Object = MibTableRow
nwhrHotfixEntry = _NwhrHotfixEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1)
)
nwhrHotfixEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "NetWare-Host-Ext-MIB", "nwhrPhysicalPartitionIndex"),
)
if mibBuilder.loadTexts:
    nwhrHotfixEntry.setStatus("mandatory")
_NwhrHotfixUnits_Type = Integer32
_NwhrHotfixUnits_Object = MibTableColumn
nwhrHotfixUnits = _NwhrHotfixUnits_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 1),
    _NwhrHotfixUnits_Type()
)
nwhrHotfixUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrHotfixUnits.setStatus("mandatory")
_NwhrHotfixTotal_Type = Integer32
_NwhrHotfixTotal_Object = MibTableColumn
nwhrHotfixTotal = _NwhrHotfixTotal_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 2),
    _NwhrHotfixTotal_Type()
)
nwhrHotfixTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrHotfixTotal.setStatus("mandatory")
_NwhrHotfixUsed_Type = Integer32
_NwhrHotfixUsed_Object = MibTableColumn
nwhrHotfixUsed = _NwhrHotfixUsed_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 3),
    _NwhrHotfixUsed_Type()
)
nwhrHotfixUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrHotfixUsed.setStatus("mandatory")
_NwhrHotfixReserved_Type = Integer32
_NwhrHotfixReserved_Object = MibTableColumn
nwhrHotfixReserved = _NwhrHotfixReserved_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 4),
    _NwhrHotfixReserved_Type()
)
nwhrHotfixReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrHotfixReserved.setStatus("mandatory")
_NwhrAdapterCount_Type = Integer32
_NwhrAdapterCount_Object = MibScalar
nwhrAdapterCount = _NwhrAdapterCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 9),
    _NwhrAdapterCount_Type()
)
nwhrAdapterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterCount.setStatus("mandatory")
_NwhrAdapterTable_Object = MibTable
nwhrAdapterTable = _NwhrAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10)
)
if mibBuilder.loadTexts:
    nwhrAdapterTable.setStatus("mandatory")
_NwhrAdapterEntry_Object = MibTableRow
nwhrAdapterEntry = _NwhrAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1)
)
nwhrAdapterEntry.setIndexNames(
    (0, "NetWare-Host-Ext-MIB", "nwhrAdapterIndex"),
)
if mibBuilder.loadTexts:
    nwhrAdapterEntry.setStatus("mandatory")
_NwhrAdapterIndex_Type = Integer32
_NwhrAdapterIndex_Object = MibTableColumn
nwhrAdapterIndex = _NwhrAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 1),
    _NwhrAdapterIndex_Type()
)
nwhrAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterIndex.setStatus("mandatory")
_NwhrAdapterType_Type = ObjectIdentifier
_NwhrAdapterType_Object = MibTableColumn
nwhrAdapterType = _NwhrAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 2),
    _NwhrAdapterType_Type()
)
nwhrAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterType.setStatus("mandatory")


class _NwhrAdapterDescr_Type(InternationalDisplayString):
    """Custom type nwhrAdapterDescr based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NwhrAdapterDescr_Type.__name__ = "InternationalDisplayString"
_NwhrAdapterDescr_Object = MibTableColumn
nwhrAdapterDescr = _NwhrAdapterDescr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 3),
    _NwhrAdapterDescr_Type()
)
nwhrAdapterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterDescr.setStatus("mandatory")


class _NwhrAdapterDriverDescr_Type(InternationalDisplayString):
    """Custom type nwhrAdapterDriverDescr based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NwhrAdapterDriverDescr_Type.__name__ = "InternationalDisplayString"
_NwhrAdapterDriverDescr_Object = MibTableColumn
nwhrAdapterDriverDescr = _NwhrAdapterDriverDescr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 4),
    _NwhrAdapterDriverDescr_Type()
)
nwhrAdapterDriverDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterDriverDescr.setStatus("mandatory")
_NwhrAdapterDriverMajorVer_Type = Integer32
_NwhrAdapterDriverMajorVer_Object = MibTableColumn
nwhrAdapterDriverMajorVer = _NwhrAdapterDriverMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 5),
    _NwhrAdapterDriverMajorVer_Type()
)
nwhrAdapterDriverMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterDriverMajorVer.setStatus("mandatory")
_NwhrAdapterDriverMinorVer_Type = Integer32
_NwhrAdapterDriverMinorVer_Object = MibTableColumn
nwhrAdapterDriverMinorVer = _NwhrAdapterDriverMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 6),
    _NwhrAdapterDriverMinorVer_Type()
)
nwhrAdapterDriverMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterDriverMinorVer.setStatus("mandatory")
_NwhrAdapterPort1_Type = Integer32
_NwhrAdapterPort1_Object = MibTableColumn
nwhrAdapterPort1 = _NwhrAdapterPort1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 7),
    _NwhrAdapterPort1_Type()
)
nwhrAdapterPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterPort1.setStatus("mandatory")
_NwhrAdapterPort1Len_Type = Integer32
_NwhrAdapterPort1Len_Object = MibTableColumn
nwhrAdapterPort1Len = _NwhrAdapterPort1Len_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 8),
    _NwhrAdapterPort1Len_Type()
)
nwhrAdapterPort1Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterPort1Len.setStatus("mandatory")
_NwhrAdapterPort2_Type = Integer32
_NwhrAdapterPort2_Object = MibTableColumn
nwhrAdapterPort2 = _NwhrAdapterPort2_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 9),
    _NwhrAdapterPort2_Type()
)
nwhrAdapterPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterPort2.setStatus("mandatory")
_NwhrAdapterPort2Len_Type = Integer32
_NwhrAdapterPort2Len_Object = MibTableColumn
nwhrAdapterPort2Len = _NwhrAdapterPort2Len_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 10),
    _NwhrAdapterPort2Len_Type()
)
nwhrAdapterPort2Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterPort2Len.setStatus("mandatory")
_NwhrAdapterMem1_Type = Integer32
_NwhrAdapterMem1_Object = MibTableColumn
nwhrAdapterMem1 = _NwhrAdapterMem1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 11),
    _NwhrAdapterMem1_Type()
)
nwhrAdapterMem1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterMem1.setStatus("mandatory")
_NwhrAdapterMem1Len_Type = Integer32
_NwhrAdapterMem1Len_Object = MibTableColumn
nwhrAdapterMem1Len = _NwhrAdapterMem1Len_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 12),
    _NwhrAdapterMem1Len_Type()
)
nwhrAdapterMem1Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterMem1Len.setStatus("mandatory")
_NwhrAdapterMem2_Type = Integer32
_NwhrAdapterMem2_Object = MibTableColumn
nwhrAdapterMem2 = _NwhrAdapterMem2_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 13),
    _NwhrAdapterMem2_Type()
)
nwhrAdapterMem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterMem2.setStatus("mandatory")
_NwhrAdapterMem2Len_Type = Integer32
_NwhrAdapterMem2Len_Object = MibTableColumn
nwhrAdapterMem2Len = _NwhrAdapterMem2Len_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 14),
    _NwhrAdapterMem2Len_Type()
)
nwhrAdapterMem2Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterMem2Len.setStatus("mandatory")


class _NwhrAdapterDMA1_Type(Integer32):
    """Custom type nwhrAdapterDMA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwhrAdapterDMA1_Type.__name__ = "Integer32"
_NwhrAdapterDMA1_Object = MibTableColumn
nwhrAdapterDMA1 = _NwhrAdapterDMA1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 15),
    _NwhrAdapterDMA1_Type()
)
nwhrAdapterDMA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterDMA1.setStatus("mandatory")


class _NwhrAdapterDMA2_Type(Integer32):
    """Custom type nwhrAdapterDMA2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwhrAdapterDMA2_Type.__name__ = "Integer32"
_NwhrAdapterDMA2_Object = MibTableColumn
nwhrAdapterDMA2 = _NwhrAdapterDMA2_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 16),
    _NwhrAdapterDMA2_Type()
)
nwhrAdapterDMA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterDMA2.setStatus("mandatory")


class _NwhrAdapterInterrupt1_Type(Integer32):
    """Custom type nwhrAdapterInterrupt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwhrAdapterInterrupt1_Type.__name__ = "Integer32"
_NwhrAdapterInterrupt1_Object = MibTableColumn
nwhrAdapterInterrupt1 = _NwhrAdapterInterrupt1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 17),
    _NwhrAdapterInterrupt1_Type()
)
nwhrAdapterInterrupt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterInterrupt1.setStatus("mandatory")


class _NwhrAdapterInterrupt2_Type(Integer32):
    """Custom type nwhrAdapterInterrupt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwhrAdapterInterrupt2_Type.__name__ = "Integer32"
_NwhrAdapterInterrupt2_Object = MibTableColumn
nwhrAdapterInterrupt2 = _NwhrAdapterInterrupt2_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 18),
    _NwhrAdapterInterrupt2_Type()
)
nwhrAdapterInterrupt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterInterrupt2.setStatus("mandatory")


class _NwhrAdapterSlot_Type(Integer32):
    """Custom type nwhrAdapterSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NwhrAdapterSlot_Type.__name__ = "Integer32"
_NwhrAdapterSlot_Object = MibTableColumn
nwhrAdapterSlot = _NwhrAdapterSlot_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 19),
    _NwhrAdapterSlot_Type()
)
nwhrAdapterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterSlot.setStatus("mandatory")
_NwhrAdapterDevices_Type = Integer32
_NwhrAdapterDevices_Object = MibTableColumn
nwhrAdapterDevices = _NwhrAdapterDevices_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 20),
    _NwhrAdapterDevices_Type()
)
nwhrAdapterDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrAdapterDevices.setStatus("mandatory")
_NwhrMslCount_Type = Integer32
_NwhrMslCount_Object = MibScalar
nwhrMslCount = _NwhrMslCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 11),
    _NwhrMslCount_Type()
)
nwhrMslCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrMslCount.setStatus("mandatory")
_NwhrMslTable_Object = MibTable
nwhrMslTable = _NwhrMslTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12)
)
if mibBuilder.loadTexts:
    nwhrMslTable.setStatus("mandatory")
_NwhrMslEntry_Object = MibTableRow
nwhrMslEntry = _NwhrMslEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1)
)
nwhrMslEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    nwhrMslEntry.setStatus("mandatory")


class _NwhrMslState_Type(Integer32):
    """Custom type nwhrMslState based on Integer32"""
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
        *(("active", 4),
          ("offline", 1),
          ("standby", 3),
          ("startup", 2))
    )


_NwhrMslState_Type.__name__ = "Integer32"
_NwhrMslState_Object = MibTableColumn
nwhrMslState = _NwhrMslState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 1),
    _NwhrMslState_Type()
)
nwhrMslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrMslState.setStatus("mandatory")
_NwhrMslSpeed_Type = Integer32
_NwhrMslSpeed_Object = MibTableColumn
nwhrMslSpeed = _NwhrMslSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 2),
    _NwhrMslSpeed_Type()
)
nwhrMslSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrMslSpeed.setStatus("mandatory")
_NwhrMslSends_Type = Counter32
_NwhrMslSends_Object = MibTableColumn
nwhrMslSends = _NwhrMslSends_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 3),
    _NwhrMslSends_Type()
)
nwhrMslSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrMslSends.setStatus("mandatory")
_NwhrMslReceives_Type = Counter32
_NwhrMslReceives_Object = MibTableColumn
nwhrMslReceives = _NwhrMslReceives_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 4),
    _NwhrMslReceives_Type()
)
nwhrMslReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrMslReceives.setStatus("mandatory")
_NwhrMslInErrors_Type = Counter32
_NwhrMslInErrors_Object = MibTableColumn
nwhrMslInErrors = _NwhrMslInErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 5),
    _NwhrMslInErrors_Type()
)
nwhrMslInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrMslInErrors.setStatus("mandatory")
_NwhrMslOutErrors_Type = Counter32
_NwhrMslOutErrors_Object = MibTableColumn
nwhrMslOutErrors = _NwhrMslOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 6),
    _NwhrMslOutErrors_Type()
)
nwhrMslOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrMslOutErrors.setStatus("mandatory")
_NwhrPrinterTable_Object = MibTable
nwhrPrinterTable = _NwhrPrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13)
)
if mibBuilder.loadTexts:
    nwhrPrinterTable.setStatus("mandatory")
_NwhrPrinterEntry_Object = MibTableRow
nwhrPrinterEntry = _NwhrPrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1)
)
nwhrPrinterEntry.setIndexNames(
    (0, "NetWare-Host-Ext-MIB", "nwhrPrinterID"),
)
if mibBuilder.loadTexts:
    nwhrPrinterEntry.setStatus("mandatory")
_NwhrPrinterID_Type = Integer32
_NwhrPrinterID_Object = MibTableColumn
nwhrPrinterID = _NwhrPrinterID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 1),
    _NwhrPrinterID_Type()
)
nwhrPrinterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterID.setStatus("mandatory")


class _NwhrPrinterType_Type(Integer32):
    """Custom type nwhrPrinterType based on Integer32"""
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
        *(("local", 2),
          ("netware", 3),
          ("other", 1),
          ("unixware", 4))
    )


_NwhrPrinterType_Type.__name__ = "Integer32"
_NwhrPrinterType_Object = MibTableColumn
nwhrPrinterType = _NwhrPrinterType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 2),
    _NwhrPrinterType_Type()
)
nwhrPrinterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterType.setStatus("mandatory")
_NwhrPrinterLocalName_Type = InternationalDisplayString
_NwhrPrinterLocalName_Object = MibTableColumn
nwhrPrinterLocalName = _NwhrPrinterLocalName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 3),
    _NwhrPrinterLocalName_Type()
)
nwhrPrinterLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterLocalName.setStatus("mandatory")
_NwhrPrinterQueueName_Type = InternationalDisplayString
_NwhrPrinterQueueName_Object = MibTableColumn
nwhrPrinterQueueName = _NwhrPrinterQueueName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 4),
    _NwhrPrinterQueueName_Type()
)
nwhrPrinterQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterQueueName.setStatus("mandatory")
_NwhrPrinterServerName_Type = InternationalDisplayString
_NwhrPrinterServerName_Object = MibTableColumn
nwhrPrinterServerName = _NwhrPrinterServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 5),
    _NwhrPrinterServerName_Type()
)
nwhrPrinterServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterServerName.setStatus("mandatory")
_NwhrPrinterTransportDomain_Type = TransportDomain
_NwhrPrinterTransportDomain_Object = MibTableColumn
nwhrPrinterTransportDomain = _NwhrPrinterTransportDomain_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 6),
    _NwhrPrinterTransportDomain_Type()
)
nwhrPrinterTransportDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterTransportDomain.setStatus("mandatory")
_NwhrPrinterTransportAddress_Type = TransportAddress
_NwhrPrinterTransportAddress_Object = MibTableColumn
nwhrPrinterTransportAddress = _NwhrPrinterTransportAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 7),
    _NwhrPrinterTransportAddress_Type()
)
nwhrPrinterTransportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterTransportAddress.setStatus("mandatory")


class _NwhrPrinterDeviceIndex_Type(Integer32):
    """Custom type nwhrPrinterDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NwhrPrinterDeviceIndex_Type.__name__ = "Integer32"
_NwhrPrinterDeviceIndex_Object = MibTableColumn
nwhrPrinterDeviceIndex = _NwhrPrinterDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 8),
    _NwhrPrinterDeviceIndex_Type()
)
nwhrPrinterDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrPrinterDeviceIndex.setStatus("mandatory")
_NwhrOdi_ObjectIdentity = ObjectIdentity
nwhrOdi = _NwhrOdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10)
)
_NwhrLslOutPkts_Type = Counter32
_NwhrLslOutPkts_Object = MibScalar
nwhrLslOutPkts = _NwhrLslOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 1),
    _NwhrLslOutPkts_Type()
)
nwhrLslOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrLslOutPkts.setStatus("mandatory")
_NwhrLslInPkts_Type = Counter32
_NwhrLslInPkts_Object = MibScalar
nwhrLslInPkts = _NwhrLslInPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 2),
    _NwhrLslInPkts_Type()
)
nwhrLslInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrLslInPkts.setStatus("mandatory")
_NwhrLslUnclaimedPkts_Type = Counter32
_NwhrLslUnclaimedPkts_Object = MibScalar
nwhrLslUnclaimedPkts = _NwhrLslUnclaimedPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 3),
    _NwhrLslUnclaimedPkts_Type()
)
nwhrLslUnclaimedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrLslUnclaimedPkts.setStatus("mandatory")
_NwhrProtocolTable_Object = MibTable
nwhrProtocolTable = _NwhrProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4)
)
if mibBuilder.loadTexts:
    nwhrProtocolTable.setStatus("mandatory")
_NwhrProtocolEntry_Object = MibTableRow
nwhrProtocolEntry = _NwhrProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1)
)
nwhrProtocolEntry.setIndexNames(
    (0, "NetWare-Host-Ext-MIB", "pysmiFakeCol1"),
    (0, "NetWare-Host-Ext-MIB", "nwhrProtocolName"),
)
if mibBuilder.loadTexts:
    nwhrProtocolEntry.setStatus("mandatory")


class _NwhrProtocolName_Type(InternationalDisplayString):
    """Custom type nwhrProtocolName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NwhrProtocolName_Type.__name__ = "InternationalDisplayString"
_NwhrProtocolName_Object = MibTableColumn
nwhrProtocolName = _NwhrProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 1),
    _NwhrProtocolName_Type()
)
nwhrProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProtocolName.setStatus("mandatory")


class _NwhrProtocolID_Type(OctetString):
    """Custom type nwhrProtocolID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_NwhrProtocolID_Type.__name__ = "OctetString"
_NwhrProtocolID_Object = MibTableColumn
nwhrProtocolID = _NwhrProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 2),
    _NwhrProtocolID_Type()
)
nwhrProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProtocolID.setStatus("mandatory")
_NwhrProtocolAddress_Type = InternationalDisplayString
_NwhrProtocolAddress_Object = MibTableColumn
nwhrProtocolAddress = _NwhrProtocolAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 3),
    _NwhrProtocolAddress_Type()
)
nwhrProtocolAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProtocolAddress.setStatus("mandatory")
_NwhrProtocolOutPkts_Type = Counter32
_NwhrProtocolOutPkts_Object = MibTableColumn
nwhrProtocolOutPkts = _NwhrProtocolOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 4),
    _NwhrProtocolOutPkts_Type()
)
nwhrProtocolOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProtocolOutPkts.setStatus("mandatory")
_NwhrProtocolInPkts_Type = Counter32
_NwhrProtocolInPkts_Object = MibTableColumn
nwhrProtocolInPkts = _NwhrProtocolInPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 5),
    _NwhrProtocolInPkts_Type()
)
nwhrProtocolInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProtocolInPkts.setStatus("mandatory")
_NwhrProtocolIgnoredPkts_Type = Counter32
_NwhrProtocolIgnoredPkts_Object = MibTableColumn
nwhrProtocolIgnoredPkts = _NwhrProtocolIgnoredPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 6),
    _NwhrProtocolIgnoredPkts_Type()
)
nwhrProtocolIgnoredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProtocolIgnoredPkts.setStatus("mandatory")
_NwhrProtocolFullName_Type = InternationalDisplayString
_NwhrProtocolFullName_Object = MibTableColumn
nwhrProtocolFullName = _NwhrProtocolFullName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 7),
    _NwhrProtocolFullName_Type()
)
nwhrProtocolFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrProtocolFullName.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_NwhrIfTable_Object = MibTable
nwhrIfTable = _NwhrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5)
)
if mibBuilder.loadTexts:
    nwhrIfTable.setStatus("mandatory")
_NwhrIfEntry_Object = MibTableRow
nwhrIfEntry = _NwhrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1)
)
nwhrIfEntry.setIndexNames(
    (0, "NetWare-Host-Ext-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    nwhrIfEntry.setStatus("mandatory")
_NwhrIfLogicalBoardNumber_Type = Integer32
_NwhrIfLogicalBoardNumber_Object = MibTableColumn
nwhrIfLogicalBoardNumber = _NwhrIfLogicalBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1, 1),
    _NwhrIfLogicalBoardNumber_Type()
)
nwhrIfLogicalBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrIfLogicalBoardNumber.setStatus("mandatory")
_NwhrIfFrameType_Type = InternationalDisplayString
_NwhrIfFrameType_Object = MibTableColumn
nwhrIfFrameType = _NwhrIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1, 2),
    _NwhrIfFrameType_Type()
)
nwhrIfFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrIfFrameType.setStatus("mandatory")


class _NwhrIfLogicalBoardName_Type(InternationalDisplayString):
    """Custom type nwhrIfLogicalBoardName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_NwhrIfLogicalBoardName_Type.__name__ = "InternationalDisplayString"
_NwhrIfLogicalBoardName_Object = MibTableColumn
nwhrIfLogicalBoardName = _NwhrIfLogicalBoardName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1, 3),
    _NwhrIfLogicalBoardName_Type()
)
nwhrIfLogicalBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwhrIfLogicalBoardName.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NetWare-Host-Ext-MIB",
    **{"TransportDomain": TransportDomain,
       "TransportAddress": TransportAddress,
       "KBytes": KBytes,
       "InternationalDisplayString": InternationalDisplayString,
       "novell": novell,
       "mibDoc": mibDoc,
       "nwHostExtensions": nwHostExtensions,
       "nwhrStorage": nwhrStorage,
       "nwhrStorageTypes": nwhrStorageTypes,
       "nwhrStorageVolume": nwhrStorageVolume,
       "nwhrStorageMemoryPermanent": nwhrStorageMemoryPermanent,
       "nwhrStorageMemoryAlloc": nwhrStorageMemoryAlloc,
       "nwhrStorageCacheBuffers": nwhrStorageCacheBuffers,
       "nwhrStorageCacheMovable": nwhrStorageCacheMovable,
       "nwhrStorageCacheNonMovable": nwhrStorageCacheNonMovable,
       "nwhrStorageCodeAndDataMemory": nwhrStorageCodeAndDataMemory,
       "nwhrStorageDOSMemory": nwhrStorageDOSMemory,
       "nwhrStorageIOEngineMemory": nwhrStorageIOEngineMemory,
       "nwhrStorageMSEngineMemory": nwhrStorageMSEngineMemory,
       "nwhrStorageUnclaimedMemory": nwhrStorageUnclaimedMemory,
       "nwhrDevice": nwhrDevice,
       "nwhrDeviceTypes": nwhrDeviceTypes,
       "nwhrDeviceMirroredServerLink": nwhrDeviceMirroredServerLink,
       "nwhrDeviceTable": nwhrDeviceTable,
       "nwhrDeviceEntry": nwhrDeviceEntry,
       "nwhrDeviceAdapterIndex": nwhrDeviceAdapterIndex,
       "nwhrDeviceControllerNumber": nwhrDeviceControllerNumber,
       "nwhrDeviceNumber": nwhrDeviceNumber,
       "nwhrProcessorCount": nwhrProcessorCount,
       "nwhrPrinterCount": nwhrPrinterCount,
       "nwhrDiskStorageCount": nwhrDiskStorageCount,
       "nwhrDiskStorageTable": nwhrDiskStorageTable,
       "nwhrDiskStorageEntry": nwhrDiskStorageEntry,
       "nwhrDiskStorageHeads": nwhrDiskStorageHeads,
       "nwhrDiskStorageCylinders": nwhrDiskStorageCylinders,
       "nwhrDiskStorageSectorsPerTrack": nwhrDiskStorageSectorsPerTrack,
       "nwhrDiskStorageSectorSize": nwhrDiskStorageSectorSize,
       "nwhrDiskStorageBlockSize": nwhrDiskStorageBlockSize,
       "nwhrPhysicalPartitionTable": nwhrPhysicalPartitionTable,
       "nwhrPhysicalPartitionEntry": nwhrPhysicalPartitionEntry,
       "nwhrPhysicalPartitionIndex": nwhrPhysicalPartitionIndex,
       "nwhrPhysicalPartitionType": nwhrPhysicalPartitionType,
       "nwhrPhysicalPartitionDescr": nwhrPhysicalPartitionDescr,
       "nwhrPhysicalPartitionSize": nwhrPhysicalPartitionSize,
       "nwhrHotfixTable": nwhrHotfixTable,
       "nwhrHotfixEntry": nwhrHotfixEntry,
       "nwhrHotfixUnits": nwhrHotfixUnits,
       "nwhrHotfixTotal": nwhrHotfixTotal,
       "nwhrHotfixUsed": nwhrHotfixUsed,
       "nwhrHotfixReserved": nwhrHotfixReserved,
       "nwhrAdapterCount": nwhrAdapterCount,
       "nwhrAdapterTable": nwhrAdapterTable,
       "nwhrAdapterEntry": nwhrAdapterEntry,
       "nwhrAdapterIndex": nwhrAdapterIndex,
       "nwhrAdapterType": nwhrAdapterType,
       "nwhrAdapterDescr": nwhrAdapterDescr,
       "nwhrAdapterDriverDescr": nwhrAdapterDriverDescr,
       "nwhrAdapterDriverMajorVer": nwhrAdapterDriverMajorVer,
       "nwhrAdapterDriverMinorVer": nwhrAdapterDriverMinorVer,
       "nwhrAdapterPort1": nwhrAdapterPort1,
       "nwhrAdapterPort1Len": nwhrAdapterPort1Len,
       "nwhrAdapterPort2": nwhrAdapterPort2,
       "nwhrAdapterPort2Len": nwhrAdapterPort2Len,
       "nwhrAdapterMem1": nwhrAdapterMem1,
       "nwhrAdapterMem1Len": nwhrAdapterMem1Len,
       "nwhrAdapterMem2": nwhrAdapterMem2,
       "nwhrAdapterMem2Len": nwhrAdapterMem2Len,
       "nwhrAdapterDMA1": nwhrAdapterDMA1,
       "nwhrAdapterDMA2": nwhrAdapterDMA2,
       "nwhrAdapterInterrupt1": nwhrAdapterInterrupt1,
       "nwhrAdapterInterrupt2": nwhrAdapterInterrupt2,
       "nwhrAdapterSlot": nwhrAdapterSlot,
       "nwhrAdapterDevices": nwhrAdapterDevices,
       "nwhrMslCount": nwhrMslCount,
       "nwhrMslTable": nwhrMslTable,
       "nwhrMslEntry": nwhrMslEntry,
       "nwhrMslState": nwhrMslState,
       "nwhrMslSpeed": nwhrMslSpeed,
       "nwhrMslSends": nwhrMslSends,
       "nwhrMslReceives": nwhrMslReceives,
       "nwhrMslInErrors": nwhrMslInErrors,
       "nwhrMslOutErrors": nwhrMslOutErrors,
       "nwhrPrinterTable": nwhrPrinterTable,
       "nwhrPrinterEntry": nwhrPrinterEntry,
       "nwhrPrinterID": nwhrPrinterID,
       "nwhrPrinterType": nwhrPrinterType,
       "nwhrPrinterLocalName": nwhrPrinterLocalName,
       "nwhrPrinterQueueName": nwhrPrinterQueueName,
       "nwhrPrinterServerName": nwhrPrinterServerName,
       "nwhrPrinterTransportDomain": nwhrPrinterTransportDomain,
       "nwhrPrinterTransportAddress": nwhrPrinterTransportAddress,
       "nwhrPrinterDeviceIndex": nwhrPrinterDeviceIndex,
       "nwhrOdi": nwhrOdi,
       "nwhrLslOutPkts": nwhrLslOutPkts,
       "nwhrLslInPkts": nwhrLslInPkts,
       "nwhrLslUnclaimedPkts": nwhrLslUnclaimedPkts,
       "nwhrProtocolTable": nwhrProtocolTable,
       "nwhrProtocolEntry": nwhrProtocolEntry,
       "nwhrProtocolName": nwhrProtocolName,
       "nwhrProtocolID": nwhrProtocolID,
       "nwhrProtocolAddress": nwhrProtocolAddress,
       "nwhrProtocolOutPkts": nwhrProtocolOutPkts,
       "nwhrProtocolInPkts": nwhrProtocolInPkts,
       "nwhrProtocolIgnoredPkts": nwhrProtocolIgnoredPkts,
       "nwhrProtocolFullName": nwhrProtocolFullName,
       "pysmiFakeCol1": pysmiFakeCol1,
       "nwhrIfTable": nwhrIfTable,
       "nwhrIfEntry": nwhrIfEntry,
       "nwhrIfLogicalBoardNumber": nwhrIfLogicalBoardNumber,
       "nwhrIfFrameType": nwhrIfFrameType,
       "nwhrIfLogicalBoardName": nwhrIfLogicalBoardName,
       "pysmiFakeCol2": pysmiFakeCol2}
)
