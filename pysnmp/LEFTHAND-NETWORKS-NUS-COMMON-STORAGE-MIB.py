# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-STORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:47 2024
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

(lhnModules,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules")

(lhnNusCommonStorage,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonStorage")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNusCommonStorageModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StorageDeviceCount_Type = Integer32
_StorageDeviceCount_Object = MibScalar
storageDeviceCount = _StorageDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 1),
    _StorageDeviceCount_Type()
)
storageDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceCount.setStatus("current")
_StorageDeviceTable_Object = MibTable
storageDeviceTable = _StorageDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    storageDeviceTable.setStatus("current")
_StorageDeviceEntry_Object = MibTableRow
storageDeviceEntry = _StorageDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1)
)
storageDeviceEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-STORAGE-MIB", "storageDeviceIndex"),
)
if mibBuilder.loadTexts:
    storageDeviceEntry.setStatus("current")
_StorageDeviceIndex_Type = Integer32
_StorageDeviceIndex_Object = MibTableColumn
storageDeviceIndex = _StorageDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 1),
    _StorageDeviceIndex_Type()
)
storageDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceIndex.setStatus("current")
_StorageDeviceModel_Type = OctetString
_StorageDeviceModel_Object = MibTableColumn
storageDeviceModel = _StorageDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 2),
    _StorageDeviceModel_Type()
)
storageDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceModel.setStatus("current")
_StorageDeviceClass_Type = OctetString
_StorageDeviceClass_Object = MibTableColumn
storageDeviceClass = _StorageDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 3),
    _StorageDeviceClass_Type()
)
storageDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceClass.setStatus("current")
_StorageDeviceCapacity_Type = Counter64
_StorageDeviceCapacity_Object = MibTableColumn
storageDeviceCapacity = _StorageDeviceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 4),
    _StorageDeviceCapacity_Type()
)
storageDeviceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceCapacity.setStatus("current")
if mibBuilder.loadTexts:
    storageDeviceCapacity.setUnits("Blocks (512 bytes)")
_StorageDeviceStatus_Type = OctetString
_StorageDeviceStatus_Object = MibTableColumn
storageDeviceStatus = _StorageDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 5),
    _StorageDeviceStatus_Type()
)
storageDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceStatus.setStatus("current")
_StorageDeviceChain_Type = OctetString
_StorageDeviceChain_Object = MibTableColumn
storageDeviceChain = _StorageDeviceChain_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 6),
    _StorageDeviceChain_Type()
)
storageDeviceChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceChain.setStatus("current")
_StorageDeviceSerialNo_Type = OctetString
_StorageDeviceSerialNo_Object = MibTableColumn
storageDeviceSerialNo = _StorageDeviceSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 7),
    _StorageDeviceSerialNo_Type()
)
storageDeviceSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceSerialNo.setStatus("current")
_StorageDeviceBayStatus_Type = OctetString
_StorageDeviceBayStatus_Object = MibTableColumn
storageDeviceBayStatus = _StorageDeviceBayStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 8),
    _StorageDeviceBayStatus_Type()
)
storageDeviceBayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceBayStatus.setStatus("current")
_StorageDeviceTemperature_Type = Integer32
_StorageDeviceTemperature_Object = MibTableColumn
storageDeviceTemperature = _StorageDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 9),
    _StorageDeviceTemperature_Type()
)
storageDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceTemperature.setStatus("current")
_StorageRaidCount_Type = Integer32
_StorageRaidCount_Object = MibScalar
storageRaidCount = _StorageRaidCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 3),
    _StorageRaidCount_Type()
)
storageRaidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidCount.setStatus("current")
_StorageRaidTable_Object = MibTable
storageRaidTable = _StorageRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    storageRaidTable.setStatus("current")
_StorageRaidEntry_Object = MibTableRow
storageRaidEntry = _StorageRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1)
)
storageRaidEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-STORAGE-MIB", "storageRaidIndex"),
)
if mibBuilder.loadTexts:
    storageRaidEntry.setStatus("current")
_StorageRaidIndex_Type = Integer32
_StorageRaidIndex_Object = MibTableColumn
storageRaidIndex = _StorageRaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 1),
    _StorageRaidIndex_Type()
)
storageRaidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidIndex.setStatus("current")
_StorageRaidDeviceName_Type = OctetString
_StorageRaidDeviceName_Object = MibTableColumn
storageRaidDeviceName = _StorageRaidDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 2),
    _StorageRaidDeviceName_Type()
)
storageRaidDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDeviceName.setStatus("current")
_StorageRaidLevel_Type = Integer32
_StorageRaidLevel_Object = MibTableColumn
storageRaidLevel = _StorageRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 3),
    _StorageRaidLevel_Type()
)
storageRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidLevel.setStatus("current")
_StorageRaidDiskCount_Type = Integer32
_StorageRaidDiskCount_Object = MibTableColumn
storageRaidDiskCount = _StorageRaidDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 4),
    _StorageRaidDiskCount_Type()
)
storageRaidDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDiskCount.setStatus("current")
_StorageRaidSpareDiskCount_Type = Integer32
_StorageRaidSpareDiskCount_Object = MibTableColumn
storageRaidSpareDiskCount = _StorageRaidSpareDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 5),
    _StorageRaidSpareDiskCount_Type()
)
storageRaidSpareDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidSpareDiskCount.setStatus("current")
_StorageRaidSuperBlock_Type = TruthValue
_StorageRaidSuperBlock_Object = MibTableColumn
storageRaidSuperBlock = _StorageRaidSuperBlock_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 6),
    _StorageRaidSuperBlock_Type()
)
storageRaidSuperBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidSuperBlock.setStatus("current")
_StorageRaidChunkSize_Type = Integer32
_StorageRaidChunkSize_Object = MibTableColumn
storageRaidChunkSize = _StorageRaidChunkSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 7),
    _StorageRaidChunkSize_Type()
)
storageRaidChunkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidChunkSize.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidChunkSize.setUnits("Kbytes")
_StorageRaidDisks_Type = OctetString
_StorageRaidDisks_Object = MibTableColumn
storageRaidDisks = _StorageRaidDisks_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 8),
    _StorageRaidDisks_Type()
)
storageRaidDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDisks.setStatus("current")


class _StorageRaidConfiguration_Type(Integer32):
    """Custom type storageRaidConfiguration based on Integer32"""
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
        *(("mirror", 3),
          ("mirrorAndStripe", 4),
          ("noRaid", 1),
          ("stripe", 2))
    )


_StorageRaidConfiguration_Type.__name__ = "Integer32"
_StorageRaidConfiguration_Object = MibScalar
storageRaidConfiguration = _StorageRaidConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 5),
    _StorageRaidConfiguration_Type()
)
storageRaidConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storageRaidConfiguration.setStatus("current")


class _StorageRaidStatus_Type(Integer32):
    """Custom type storageRaidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("normal", 1),
          ("notRebuilding", 4),
          ("off", 5),
          ("rebuilding", 2))
    )


_StorageRaidStatus_Type.__name__ = "Integer32"
_StorageRaidStatus_Object = MibScalar
storageRaidStatus = _StorageRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 7),
    _StorageRaidStatus_Type()
)
storageRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatus.setStatus("current")
_StorageRaidMinimumSpeed_Type = Integer32
_StorageRaidMinimumSpeed_Object = MibScalar
storageRaidMinimumSpeed = _StorageRaidMinimumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 8),
    _StorageRaidMinimumSpeed_Type()
)
storageRaidMinimumSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storageRaidMinimumSpeed.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidMinimumSpeed.setUnits("Kbytes / sec")
_StorageRaidMaximumSpeed_Type = Integer32
_StorageRaidMaximumSpeed_Object = MibScalar
storageRaidMaximumSpeed = _StorageRaidMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 9),
    _StorageRaidMaximumSpeed_Type()
)
storageRaidMaximumSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    storageRaidMaximumSpeed.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidMaximumSpeed.setUnits("Kbytes / sec")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-STORAGE-MIB",
    **{"lhnNusCommonStorageModule": lhnNusCommonStorageModule,
       "storageDeviceCount": storageDeviceCount,
       "storageDeviceTable": storageDeviceTable,
       "storageDeviceEntry": storageDeviceEntry,
       "storageDeviceIndex": storageDeviceIndex,
       "storageDeviceModel": storageDeviceModel,
       "storageDeviceClass": storageDeviceClass,
       "storageDeviceCapacity": storageDeviceCapacity,
       "storageDeviceStatus": storageDeviceStatus,
       "storageDeviceChain": storageDeviceChain,
       "storageDeviceSerialNo": storageDeviceSerialNo,
       "storageDeviceBayStatus": storageDeviceBayStatus,
       "storageDeviceTemperature": storageDeviceTemperature,
       "storageRaidCount": storageRaidCount,
       "storageRaidTable": storageRaidTable,
       "storageRaidEntry": storageRaidEntry,
       "storageRaidIndex": storageRaidIndex,
       "storageRaidDeviceName": storageRaidDeviceName,
       "storageRaidLevel": storageRaidLevel,
       "storageRaidDiskCount": storageRaidDiskCount,
       "storageRaidSpareDiskCount": storageRaidSpareDiskCount,
       "storageRaidSuperBlock": storageRaidSuperBlock,
       "storageRaidChunkSize": storageRaidChunkSize,
       "storageRaidDisks": storageRaidDisks,
       "storageRaidConfiguration": storageRaidConfiguration,
       "storageRaidStatus": storageRaidStatus,
       "storageRaidMinimumSpeed": storageRaidMinimumSpeed,
       "storageRaidMaximumSpeed": storageRaidMaximumSpeed}
)
