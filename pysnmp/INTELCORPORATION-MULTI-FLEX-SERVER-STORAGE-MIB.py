# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:11 2024
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

(bladeSlotId,) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB",
    "bladeSlotId")

(chassis,) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-MIB",
    "chassis")

(groups,
 regModule) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    "groups",
    "regModule")

(FaultLedStates,
 IdromBinary16,
 Index,
 Power,
 PowerLedStates,
 PresenceLedStates) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    "FaultLedStates",
    "IdromBinary16",
    "Index",
    "Power",
    "PowerLedStates",
    "PresenceLedStates")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

multiFlexServerStorageMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 18)
)
multiFlexServerStorageMibModule.setRevisions(
        ("2007-09-12 11:10",
         "2007-08-16 13:30",
         "2007-07-20 16:30",
         "2007-07-09 12:00",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-04-18 19:05",
         "2007-04-18 19:05",
         "2007-04-09 15:45",
         "2007-04-09 10:30",
         "2007-03-15 18:30",
         "2007-03-10 16:00",
         "2007-02-22 17:00",
         "2007-01-08 09:50",
         "2006-12-28 17:30",
         "2006-12-05 10:30",
         "2006-12-04 16:30",
         "2006-11-07 07:01",
         "2006-10-02 06:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208)
)
if mibBuilder.loadTexts:
    storage.setStatus("current")
_Interposer_ObjectIdentity = ObjectIdentity
interposer = _Interposer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1)
)
if mibBuilder.loadTexts:
    interposer.setStatus("current")
_InterposerVendor_Type = DisplayString
_InterposerVendor_Object = MibScalar
interposerVendor = _InterposerVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 1),
    _InterposerVendor_Type()
)
interposerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerVendor.setStatus("current")
_InterposerMfgDate_Type = DisplayString
_InterposerMfgDate_Object = MibScalar
interposerMfgDate = _InterposerMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 2),
    _InterposerMfgDate_Type()
)
interposerMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerMfgDate.setStatus("current")
_InterposerDeviceName_Type = DisplayString
_InterposerDeviceName_Object = MibScalar
interposerDeviceName = _InterposerDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 3),
    _InterposerDeviceName_Type()
)
interposerDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerDeviceName.setStatus("current")
_InterposerPart_Type = IdromBinary16
_InterposerPart_Object = MibScalar
interposerPart = _InterposerPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 4),
    _InterposerPart_Type()
)
interposerPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerPart.setStatus("current")
_InterposerSerialNo_Type = IdromBinary16
_InterposerSerialNo_Object = MibScalar
interposerSerialNo = _InterposerSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 5),
    _InterposerSerialNo_Type()
)
interposerSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerSerialNo.setStatus("current")
_InterposerMaximumPower_Type = Power
_InterposerMaximumPower_Object = MibScalar
interposerMaximumPower = _InterposerMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 6),
    _InterposerMaximumPower_Type()
)
interposerMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerMaximumPower.setStatus("current")
_InterposerNominalPower_Type = Power
_InterposerNominalPower_Object = MibScalar
interposerNominalPower = _InterposerNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 7),
    _InterposerNominalPower_Type()
)
interposerNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerNominalPower.setStatus("current")
_InterposerAssetTag_Type = IdromBinary16
_InterposerAssetTag_Object = MibScalar
interposerAssetTag = _InterposerAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 8),
    _InterposerAssetTag_Type()
)
interposerAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interposerAssetTag.setStatus("current")


class _StorageWWN_Type(DisplayString):
    """Custom type storageWWN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_StorageWWN_Type.__name__ = "DisplayString"
_StorageWWN_Object = MibScalar
storageWWN = _StorageWWN_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 3),
    _StorageWWN_Type()
)
storageWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageWWN.setStatus("current")


class _StorageInterConnectionType_Type(Integer32):
    """Custom type storageInterConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sas", 1),
          ("unsupported", 0))
    )


_StorageInterConnectionType_Type.__name__ = "Integer32"
_StorageInterConnectionType_Object = MibScalar
storageInterConnectionType = _StorageInterConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 4),
    _StorageInterConnectionType_Type()
)
storageInterConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageInterConnectionType.setStatus("current")
_StoragePoolTable_Object = MibTable
storagePoolTable = _StoragePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5)
)
if mibBuilder.loadTexts:
    storagePoolTable.setStatus("current")
_StoragePoolEntry_Object = MibTableRow
storagePoolEntry = _StoragePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1)
)
storagePoolEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolIndex"),
)
if mibBuilder.loadTexts:
    storagePoolEntry.setStatus("current")
_PoolIndex_Type = Index
_PoolIndex_Object = MibTableColumn
poolIndex = _PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 1),
    _PoolIndex_Type()
)
poolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolIndex.setStatus("current")


class _PoolAlias_Type(DisplayString):
    """Custom type poolAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PoolAlias_Type.__name__ = "DisplayString"
_PoolAlias_Object = MibTableColumn
poolAlias = _PoolAlias_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 2),
    _PoolAlias_Type()
)
poolAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolAlias.setStatus("current")
_PoolOperationalStatus_Type = DisplayString
_PoolOperationalStatus_Object = MibTableColumn
poolOperationalStatus = _PoolOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 3),
    _PoolOperationalStatus_Type()
)
poolOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolOperationalStatus.setStatus("current")
_PoolCondition_Type = DisplayString
_PoolCondition_Object = MibTableColumn
poolCondition = _PoolCondition_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 4),
    _PoolCondition_Type()
)
poolCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCondition.setStatus("current")
_PoolOperation_Type = DisplayString
_PoolOperation_Object = MibTableColumn
poolOperation = _PoolOperation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 5),
    _PoolOperation_Type()
)
poolOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolOperation.setStatus("current")
_PoolPhysicalCapacity_Type = Counter64
_PoolPhysicalCapacity_Object = MibTableColumn
poolPhysicalCapacity = _PoolPhysicalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 6),
    _PoolPhysicalCapacity_Type()
)
poolPhysicalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPhysicalCapacity.setStatus("current")
_PoolConfigurableCapacity_Type = Counter64
_PoolConfigurableCapacity_Object = MibTableColumn
poolConfigurableCapacity = _PoolConfigurableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 7),
    _PoolConfigurableCapacity_Type()
)
poolConfigurableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolConfigurableCapacity.setStatus("current")
_PoolFreeCapacity_Type = Counter64
_PoolFreeCapacity_Object = MibTableColumn
poolFreeCapacity = _PoolFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 8),
    _PoolFreeCapacity_Type()
)
poolFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolFreeCapacity.setStatus("current")
_PoolMaxContiguousCapacity_Type = Counter64
_PoolMaxContiguousCapacity_Object = MibTableColumn
poolMaxContiguousCapacity = _PoolMaxContiguousCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 9),
    _PoolMaxContiguousCapacity_Type()
)
poolMaxContiguousCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMaxContiguousCapacity.setStatus("current")
_PoolMediaPatrolEnabled_Type = TruthValue
_PoolMediaPatrolEnabled_Object = MibTableColumn
poolMediaPatrolEnabled = _PoolMediaPatrolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 10),
    _PoolMediaPatrolEnabled_Type()
)
poolMediaPatrolEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMediaPatrolEnabled.setStatus("current")
_PoolPDMEnabled_Type = TruthValue
_PoolPDMEnabled_Object = MibTableColumn
poolPDMEnabled = _PoolPDMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 11),
    _PoolPDMEnabled_Type()
)
poolPDMEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPDMEnabled.setStatus("current")
_PoolNumOfPhysicalDrives_Type = Integer32
_PoolNumOfPhysicalDrives_Object = MibTableColumn
poolNumOfPhysicalDrives = _PoolNumOfPhysicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 12),
    _PoolNumOfPhysicalDrives_Type()
)
poolNumOfPhysicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumOfPhysicalDrives.setStatus("current")
_PoolNumOfVirtualDrives_Type = Integer32
_PoolNumOfVirtualDrives_Object = MibTableColumn
poolNumOfVirtualDrives = _PoolNumOfVirtualDrives_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 13),
    _PoolNumOfVirtualDrives_Type()
)
poolNumOfVirtualDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumOfVirtualDrives.setStatus("current")
_PoolNumOfDedicatedSpares_Type = Integer32
_PoolNumOfDedicatedSpares_Object = MibTableColumn
poolNumOfDedicatedSpares = _PoolNumOfDedicatedSpares_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 14),
    _PoolNumOfDedicatedSpares_Type()
)
poolNumOfDedicatedSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumOfDedicatedSpares.setStatus("current")
_PoolPhysicalDriveIDs_Type = DisplayString
_PoolPhysicalDriveIDs_Object = MibTableColumn
poolPhysicalDriveIDs = _PoolPhysicalDriveIDs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 15),
    _PoolPhysicalDriveIDs_Type()
)
poolPhysicalDriveIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPhysicalDriveIDs.setStatus("current")
_PoolVirtualDriveIDs_Type = DisplayString
_PoolVirtualDriveIDs_Object = MibTableColumn
poolVirtualDriveIDs = _PoolVirtualDriveIDs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 16),
    _PoolVirtualDriveIDs_Type()
)
poolVirtualDriveIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolVirtualDriveIDs.setStatus("current")
_PoolDedicatedSpareIDs_Type = DisplayString
_PoolDedicatedSpareIDs_Object = MibTableColumn
poolDedicatedSpareIDs = _PoolDedicatedSpareIDs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 17),
    _PoolDedicatedSpareIDs_Type()
)
poolDedicatedSpareIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDedicatedSpareIDs.setStatus("current")
_PoolWWN_Type = DisplayString
_PoolWWN_Object = MibTableColumn
poolWWN = _PoolWWN_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 18),
    _PoolWWN_Type()
)
poolWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolWWN.setStatus("current")
_VirtualDriveTable_Object = MibTable
virtualDriveTable = _VirtualDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6)
)
if mibBuilder.loadTexts:
    virtualDriveTable.setStatus("current")
_VirtualDriveEntry_Object = MibTableRow
virtualDriveEntry = _VirtualDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1)
)
virtualDriveEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveId"),
)
if mibBuilder.loadTexts:
    virtualDriveEntry.setStatus("current")
_VirtDriveId_Type = Index
_VirtDriveId_Object = MibTableColumn
virtDriveId = _VirtDriveId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 1),
    _VirtDriveId_Type()
)
virtDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveId.setStatus("current")


class _VirtDriveAlias_Type(DisplayString):
    """Custom type virtDriveAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VirtDriveAlias_Type.__name__ = "DisplayString"
_VirtDriveAlias_Object = MibTableColumn
virtDriveAlias = _VirtDriveAlias_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 2),
    _VirtDriveAlias_Type()
)
virtDriveAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveAlias.setStatus("current")
_VirtDriveSerialNo_Type = DisplayString
_VirtDriveSerialNo_Object = MibTableColumn
virtDriveSerialNo = _VirtDriveSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 3),
    _VirtDriveSerialNo_Type()
)
virtDriveSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveSerialNo.setStatus("current")


class _VirtDriveWWN_Type(DisplayString):
    """Custom type virtDriveWWN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_VirtDriveWWN_Type.__name__ = "DisplayString"
_VirtDriveWWN_Object = MibTableColumn
virtDriveWWN = _VirtDriveWWN_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 4),
    _VirtDriveWWN_Type()
)
virtDriveWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveWWN.setStatus("current")
_VirtDriveOperationalStatus_Type = DisplayString
_VirtDriveOperationalStatus_Object = MibTableColumn
virtDriveOperationalStatus = _VirtDriveOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 5),
    _VirtDriveOperationalStatus_Type()
)
virtDriveOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveOperationalStatus.setStatus("current")
_VirtDriveCondition_Type = DisplayString
_VirtDriveCondition_Object = MibTableColumn
virtDriveCondition = _VirtDriveCondition_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 6),
    _VirtDriveCondition_Type()
)
virtDriveCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveCondition.setStatus("current")
_VirtDriveOperation_Type = DisplayString
_VirtDriveOperation_Object = MibTableColumn
virtDriveOperation = _VirtDriveOperation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 7),
    _VirtDriveOperation_Type()
)
virtDriveOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveOperation.setStatus("current")
_VirtDriveSynchronized_Type = TruthValue
_VirtDriveSynchronized_Object = MibTableColumn
virtDriveSynchronized = _VirtDriveSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 8),
    _VirtDriveSynchronized_Type()
)
virtDriveSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveSynchronized.setStatus("current")


class _VirtDriveRAIDLevel_Type(Integer32):
    """Custom type virtDriveRAIDLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              3,
              5,
              6,
              10,
              16,
              80,
              81,
              85,
              95,
              96)
        )
    )
    namedValues = NamedValues(
        *(("jbod", 10),
          ("raid0", 0),
          ("raid1", 1),
          ("raid10", 16),
          ("raid1e", 95),
          ("raid3", 3),
          ("raid5", 5),
          ("raid50", 80),
          ("raid51", 81),
          ("raid55", 85),
          ("raid6", 6),
          ("raid60", 96),
          ("unknown", -1))
    )


_VirtDriveRAIDLevel_Type.__name__ = "Integer32"
_VirtDriveRAIDLevel_Object = MibTableColumn
virtDriveRAIDLevel = _VirtDriveRAIDLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 9),
    _VirtDriveRAIDLevel_Type()
)
virtDriveRAIDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveRAIDLevel.setStatus("current")
_VirtDriveCapacity_Type = Counter64
_VirtDriveCapacity_Object = MibTableColumn
virtDriveCapacity = _VirtDriveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 10),
    _VirtDriveCapacity_Type()
)
virtDriveCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveCapacity.setStatus("current")
_VirtDrivePhysicalCapacity_Type = Counter64
_VirtDrivePhysicalCapacity_Object = MibTableColumn
virtDrivePhysicalCapacity = _VirtDrivePhysicalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 11),
    _VirtDrivePhysicalCapacity_Type()
)
virtDrivePhysicalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDrivePhysicalCapacity.setStatus("current")
_VirtDriveStoragePoolId_Type = Integer32
_VirtDriveStoragePoolId_Object = MibTableColumn
virtDriveStoragePoolId = _VirtDriveStoragePoolId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 12),
    _VirtDriveStoragePoolId_Type()
)
virtDriveStoragePoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStoragePoolId.setStatus("current")
_VirtDriveNumOfAxels_Type = Integer32
_VirtDriveNumOfAxels_Object = MibTableColumn
virtDriveNumOfAxels = _VirtDriveNumOfAxels_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 13),
    _VirtDriveNumOfAxels_Type()
)
virtDriveNumOfAxels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveNumOfAxels.setStatus("current")
_VirtDriveNumOfUsedPD_Type = Integer32
_VirtDriveNumOfUsedPD_Object = MibTableColumn
virtDriveNumOfUsedPD = _VirtDriveNumOfUsedPD_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 14),
    _VirtDriveNumOfUsedPD_Type()
)
virtDriveNumOfUsedPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveNumOfUsedPD.setStatus("current")
_VirtDriveSectorSize_Type = Integer32
_VirtDriveSectorSize_Object = MibTableColumn
virtDriveSectorSize = _VirtDriveSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 15),
    _VirtDriveSectorSize_Type()
)
virtDriveSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveSectorSize.setStatus("current")


class _VirtDrivePreferredScmId_Type(Integer32):
    """Custom type virtDrivePreferredScmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("unavailable", -1)
    )


_VirtDrivePreferredScmId_Type.__name__ = "Integer32"
_VirtDrivePreferredScmId_Object = MibTableColumn
virtDrivePreferredScmId = _VirtDrivePreferredScmId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 16),
    _VirtDrivePreferredScmId_Type()
)
virtDrivePreferredScmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDrivePreferredScmId.setStatus("current")
_VirtualDriveStatsTable_Object = MibTable
virtualDriveStatsTable = _VirtualDriveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7)
)
if mibBuilder.loadTexts:
    virtualDriveStatsTable.setStatus("current")
_VirtualDriveStatsEntry_Object = MibTableRow
virtualDriveStatsEntry = _VirtualDriveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1)
)
if mibBuilder.loadTexts:
    virtualDriveStatsEntry.setStatus("current")
_VirtDriveStatsDataTransferred_Type = Counter64
_VirtDriveStatsDataTransferred_Object = MibTableColumn
virtDriveStatsDataTransferred = _VirtDriveStatsDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 1),
    _VirtDriveStatsDataTransferred_Type()
)
virtDriveStatsDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsDataTransferred.setStatus("current")
_VirtDriveStatsReadDataTransferred_Type = Counter64
_VirtDriveStatsReadDataTransferred_Object = MibTableColumn
virtDriveStatsReadDataTransferred = _VirtDriveStatsReadDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 2),
    _VirtDriveStatsReadDataTransferred_Type()
)
virtDriveStatsReadDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsReadDataTransferred.setStatus("current")
_VirtDriveStatsWriteDataTransferred_Type = Counter64
_VirtDriveStatsWriteDataTransferred_Object = MibTableColumn
virtDriveStatsWriteDataTransferred = _VirtDriveStatsWriteDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 3),
    _VirtDriveStatsWriteDataTransferred_Type()
)
virtDriveStatsWriteDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsWriteDataTransferred.setStatus("current")
_VirtDriveStatsNumOfErrors_Type = Integer32
_VirtDriveStatsNumOfErrors_Object = MibTableColumn
virtDriveStatsNumOfErrors = _VirtDriveStatsNumOfErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 4),
    _VirtDriveStatsNumOfErrors_Type()
)
virtDriveStatsNumOfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfErrors.setStatus("current")
_VirtDriveStatsNumOfNonRWErrors_Type = Integer32
_VirtDriveStatsNumOfNonRWErrors_Object = MibTableColumn
virtDriveStatsNumOfNonRWErrors = _VirtDriveStatsNumOfNonRWErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 5),
    _VirtDriveStatsNumOfNonRWErrors_Type()
)
virtDriveStatsNumOfNonRWErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfNonRWErrors.setStatus("current")
_VirtDriveStatsNumOfReadErrors_Type = Integer32
_VirtDriveStatsNumOfReadErrors_Object = MibTableColumn
virtDriveStatsNumOfReadErrors = _VirtDriveStatsNumOfReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 6),
    _VirtDriveStatsNumOfReadErrors_Type()
)
virtDriveStatsNumOfReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfReadErrors.setStatus("current")
_VirtDriveStatsNumOfWriteErrors_Type = Integer32
_VirtDriveStatsNumOfWriteErrors_Object = MibTableColumn
virtDriveStatsNumOfWriteErrors = _VirtDriveStatsNumOfWriteErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 7),
    _VirtDriveStatsNumOfWriteErrors_Type()
)
virtDriveStatsNumOfWriteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfWriteErrors.setStatus("current")
_VirtDriveStatsNumOfIORequests_Type = Counter64
_VirtDriveStatsNumOfIORequests_Object = MibTableColumn
virtDriveStatsNumOfIORequests = _VirtDriveStatsNumOfIORequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 8),
    _VirtDriveStatsNumOfIORequests_Type()
)
virtDriveStatsNumOfIORequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfIORequests.setStatus("current")
_VirtDriveStatsNumOfNonRWRequests_Type = Counter64
_VirtDriveStatsNumOfNonRWRequests_Object = MibTableColumn
virtDriveStatsNumOfNonRWRequests = _VirtDriveStatsNumOfNonRWRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 9),
    _VirtDriveStatsNumOfNonRWRequests_Type()
)
virtDriveStatsNumOfNonRWRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfNonRWRequests.setStatus("current")
_VirtDriveStatsNumOfReadRequests_Type = Counter64
_VirtDriveStatsNumOfReadRequests_Object = MibTableColumn
virtDriveStatsNumOfReadRequests = _VirtDriveStatsNumOfReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 10),
    _VirtDriveStatsNumOfReadRequests_Type()
)
virtDriveStatsNumOfReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfReadRequests.setStatus("current")
_VirtDriveStatsNumOfWriteRequests_Type = Counter64
_VirtDriveStatsNumOfWriteRequests_Object = MibTableColumn
virtDriveStatsNumOfWriteRequests = _VirtDriveStatsNumOfWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 11),
    _VirtDriveStatsNumOfWriteRequests_Type()
)
virtDriveStatsNumOfWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsNumOfWriteRequests.setStatus("current")
_VirtDriveStatsStartTime_Type = Counter64
_VirtDriveStatsStartTime_Object = MibTableColumn
virtDriveStatsStartTime = _VirtDriveStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 12),
    _VirtDriveStatsStartTime_Type()
)
virtDriveStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsStartTime.setStatus("current")
_VirtDriveStatsCollectionTime_Type = Counter64
_VirtDriveStatsCollectionTime_Object = MibTableColumn
virtDriveStatsCollectionTime = _VirtDriveStatsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 13),
    _VirtDriveStatsCollectionTime_Type()
)
virtDriveStatsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtDriveStatsCollectionTime.setStatus("current")
_SpareDriveTable_Object = MibTable
spareDriveTable = _SpareDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8)
)
if mibBuilder.loadTexts:
    spareDriveTable.setStatus("current")
_SpareDriveEntry_Object = MibTableRow
spareDriveEntry = _SpareDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1)
)
spareDriveEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareIndex"),
)
if mibBuilder.loadTexts:
    spareDriveEntry.setStatus("current")
_SpareIndex_Type = Index
_SpareIndex_Object = MibTableColumn
spareIndex = _SpareIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 1),
    _SpareIndex_Type()
)
spareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareIndex.setStatus("current")
_SpareOperationalStatus_Type = DisplayString
_SpareOperationalStatus_Object = MibTableColumn
spareOperationalStatus = _SpareOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 2),
    _SpareOperationalStatus_Type()
)
spareOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareOperationalStatus.setStatus("current")
_SparePhysicalDriveId_Type = Integer32
_SparePhysicalDriveId_Object = MibTableColumn
sparePhysicalDriveId = _SparePhysicalDriveId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 3),
    _SparePhysicalDriveId_Type()
)
sparePhysicalDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparePhysicalDriveId.setStatus("current")
_SparePhysicalCapacity_Type = Counter64
_SparePhysicalCapacity_Object = MibTableColumn
sparePhysicalCapacity = _SparePhysicalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 4),
    _SparePhysicalCapacity_Type()
)
sparePhysicalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sparePhysicalCapacity.setStatus("current")
_SpareConfigurableCapacity_Type = Counter64
_SpareConfigurableCapacity_Object = MibTableColumn
spareConfigurableCapacity = _SpareConfigurableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 5),
    _SpareConfigurableCapacity_Type()
)
spareConfigurableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareConfigurableCapacity.setStatus("current")
_SpareRevertible_Type = TruthValue
_SpareRevertible_Object = MibTableColumn
spareRevertible = _SpareRevertible_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 6),
    _SpareRevertible_Type()
)
spareRevertible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareRevertible.setStatus("current")


class _SpareType_Type(Integer32):
    """Custom type spareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("global", 3),
          ("unknown", 0))
    )


_SpareType_Type.__name__ = "Integer32"
_SpareType_Object = MibTableColumn
spareType = _SpareType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 7),
    _SpareType_Type()
)
spareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareType.setStatus("current")
_SpareNumOfAssociatedStoragePools_Type = Integer32
_SpareNumOfAssociatedStoragePools_Object = MibTableColumn
spareNumOfAssociatedStoragePools = _SpareNumOfAssociatedStoragePools_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 8),
    _SpareNumOfAssociatedStoragePools_Type()
)
spareNumOfAssociatedStoragePools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareNumOfAssociatedStoragePools.setStatus("current")
_SpareAssociatedStoragePoolIDs_Type = DisplayString
_SpareAssociatedStoragePoolIDs_Object = MibTableColumn
spareAssociatedStoragePoolIDs = _SpareAssociatedStoragePoolIDs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 9),
    _SpareAssociatedStoragePoolIDs_Type()
)
spareAssociatedStoragePoolIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareAssociatedStoragePoolIDs.setStatus("current")
_SpareDriveWWN_Type = DisplayString
_SpareDriveWWN_Object = MibTableColumn
spareDriveWWN = _SpareDriveWWN_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 10),
    _SpareDriveWWN_Type()
)
spareDriveWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spareDriveWWN.setStatus("current")
_Vdb2lTable_Object = MibTable
vdb2lTable = _Vdb2lTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 9)
)
if mibBuilder.loadTexts:
    vdb2lTable.setStatus("current")
_Vdb2lEntry_Object = MibTableRow
vdb2lEntry = _Vdb2lEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 9, 1)
)
vdb2lEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveId"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
)
if mibBuilder.loadTexts:
    vdb2lEntry.setStatus("current")
_Vdb2Lun_Type = Unsigned32
_Vdb2Lun_Object = MibTableColumn
vdb2Lun = _Vdb2Lun_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 9, 1, 1),
    _Vdb2Lun_Type()
)
vdb2Lun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdb2Lun.setStatus("current")
_Bl2vdTable_Object = MibTable
bl2vdTable = _Bl2vdTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 10)
)
if mibBuilder.loadTexts:
    bl2vdTable.setStatus("current")
_Bl2vdEntry_Object = MibTableRow
bl2vdEntry = _Bl2vdEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 10, 1)
)
bl2vdEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "vdb2Lun"),
)
if mibBuilder.loadTexts:
    bl2vdEntry.setStatus("current")
_Bl2vdVirtualDriveId_Type = Index
_Bl2vdVirtualDriveId_Object = MibTableColumn
bl2vdVirtualDriveId = _Bl2vdVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 10, 1, 1),
    _Bl2vdVirtualDriveId_Type()
)
bl2vdVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bl2vdVirtualDriveId.setStatus("current")
virtualDriveEntry.registerAugmentions(
    ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB",
     "virtualDriveStatsEntry")
)
virtualDriveStatsEntry.setIndexNames(*virtualDriveEntry.getIndexNames())

# Managed Objects groups

storageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 18)
)
storageGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "storageWWN"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "storageInterConnectionType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolAlias"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolOperationalStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolCondition"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolOperation"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolPhysicalCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolConfigurableCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolFreeCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolMaxContiguousCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolMediaPatrolEnabled"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolPDMEnabled"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolNumOfPhysicalDrives"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolNumOfVirtualDrives"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolNumOfDedicatedSpares"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolPhysicalDriveIDs"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolVirtualDriveIDs"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolDedicatedSpareIDs"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolWWN"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveAlias"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveWWN"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveOperationalStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveCondition"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveOperation"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveSynchronized"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveRAIDLevel"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDrivePhysicalCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStoragePoolId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveNumOfAxels"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveNumOfUsedPD"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveSectorSize"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDrivePreferredScmId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsReadDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsWriteDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfNonRWErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfReadErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfWriteErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfIORequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfNonRWRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfReadRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfWriteRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsStartTime"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsCollectionTime"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareOperationalStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "sparePhysicalDriveId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "sparePhysicalCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareConfigurableCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareRevertible"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareNumOfAssociatedStoragePools"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareAssociatedStoragePoolIDs"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareDriveWWN"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "vdb2Lun"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "bl2vdVirtualDriveId"))
)
if mibBuilder.loadTexts:
    storageGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB",
    **{"multiFlexServerStorageMibModule": multiFlexServerStorageMibModule,
       "storageGroup": storageGroup,
       "storage": storage,
       "interposer": interposer,
       "interposerVendor": interposerVendor,
       "interposerMfgDate": interposerMfgDate,
       "interposerDeviceName": interposerDeviceName,
       "interposerPart": interposerPart,
       "interposerSerialNo": interposerSerialNo,
       "interposerMaximumPower": interposerMaximumPower,
       "interposerNominalPower": interposerNominalPower,
       "interposerAssetTag": interposerAssetTag,
       "storageWWN": storageWWN,
       "storageInterConnectionType": storageInterConnectionType,
       "storagePoolTable": storagePoolTable,
       "storagePoolEntry": storagePoolEntry,
       "poolIndex": poolIndex,
       "poolAlias": poolAlias,
       "poolOperationalStatus": poolOperationalStatus,
       "poolCondition": poolCondition,
       "poolOperation": poolOperation,
       "poolPhysicalCapacity": poolPhysicalCapacity,
       "poolConfigurableCapacity": poolConfigurableCapacity,
       "poolFreeCapacity": poolFreeCapacity,
       "poolMaxContiguousCapacity": poolMaxContiguousCapacity,
       "poolMediaPatrolEnabled": poolMediaPatrolEnabled,
       "poolPDMEnabled": poolPDMEnabled,
       "poolNumOfPhysicalDrives": poolNumOfPhysicalDrives,
       "poolNumOfVirtualDrives": poolNumOfVirtualDrives,
       "poolNumOfDedicatedSpares": poolNumOfDedicatedSpares,
       "poolPhysicalDriveIDs": poolPhysicalDriveIDs,
       "poolVirtualDriveIDs": poolVirtualDriveIDs,
       "poolDedicatedSpareIDs": poolDedicatedSpareIDs,
       "poolWWN": poolWWN,
       "virtualDriveTable": virtualDriveTable,
       "virtualDriveEntry": virtualDriveEntry,
       "virtDriveId": virtDriveId,
       "virtDriveAlias": virtDriveAlias,
       "virtDriveSerialNo": virtDriveSerialNo,
       "virtDriveWWN": virtDriveWWN,
       "virtDriveOperationalStatus": virtDriveOperationalStatus,
       "virtDriveCondition": virtDriveCondition,
       "virtDriveOperation": virtDriveOperation,
       "virtDriveSynchronized": virtDriveSynchronized,
       "virtDriveRAIDLevel": virtDriveRAIDLevel,
       "virtDriveCapacity": virtDriveCapacity,
       "virtDrivePhysicalCapacity": virtDrivePhysicalCapacity,
       "virtDriveStoragePoolId": virtDriveStoragePoolId,
       "virtDriveNumOfAxels": virtDriveNumOfAxels,
       "virtDriveNumOfUsedPD": virtDriveNumOfUsedPD,
       "virtDriveSectorSize": virtDriveSectorSize,
       "virtDrivePreferredScmId": virtDrivePreferredScmId,
       "virtualDriveStatsTable": virtualDriveStatsTable,
       "virtualDriveStatsEntry": virtualDriveStatsEntry,
       "virtDriveStatsDataTransferred": virtDriveStatsDataTransferred,
       "virtDriveStatsReadDataTransferred": virtDriveStatsReadDataTransferred,
       "virtDriveStatsWriteDataTransferred": virtDriveStatsWriteDataTransferred,
       "virtDriveStatsNumOfErrors": virtDriveStatsNumOfErrors,
       "virtDriveStatsNumOfNonRWErrors": virtDriveStatsNumOfNonRWErrors,
       "virtDriveStatsNumOfReadErrors": virtDriveStatsNumOfReadErrors,
       "virtDriveStatsNumOfWriteErrors": virtDriveStatsNumOfWriteErrors,
       "virtDriveStatsNumOfIORequests": virtDriveStatsNumOfIORequests,
       "virtDriveStatsNumOfNonRWRequests": virtDriveStatsNumOfNonRWRequests,
       "virtDriveStatsNumOfReadRequests": virtDriveStatsNumOfReadRequests,
       "virtDriveStatsNumOfWriteRequests": virtDriveStatsNumOfWriteRequests,
       "virtDriveStatsStartTime": virtDriveStatsStartTime,
       "virtDriveStatsCollectionTime": virtDriveStatsCollectionTime,
       "spareDriveTable": spareDriveTable,
       "spareDriveEntry": spareDriveEntry,
       "spareIndex": spareIndex,
       "spareOperationalStatus": spareOperationalStatus,
       "sparePhysicalDriveId": sparePhysicalDriveId,
       "sparePhysicalCapacity": sparePhysicalCapacity,
       "spareConfigurableCapacity": spareConfigurableCapacity,
       "spareRevertible": spareRevertible,
       "spareType": spareType,
       "spareNumOfAssociatedStoragePools": spareNumOfAssociatedStoragePools,
       "spareAssociatedStoragePoolIDs": spareAssociatedStoragePoolIDs,
       "spareDriveWWN": spareDriveWWN,
       "vdb2lTable": vdb2lTable,
       "vdb2lEntry": vdb2lEntry,
       "vdb2Lun": vdb2Lun,
       "bl2vdTable": bl2vdTable,
       "bl2vdEntry": bl2vdEntry,
       "bl2vdVirtualDriveId": bl2vdVirtualDriveId}
)
