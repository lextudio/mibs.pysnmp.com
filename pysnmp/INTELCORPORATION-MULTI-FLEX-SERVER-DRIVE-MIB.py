# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:07 2024
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

(chassis,) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-MIB",
    "chassis")

(groups,
 regModule) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    "groups",
    "regModule")

(FaultLedStates,
 FeatureSet,
 INT32withException,
 IdromBinary16,
 Index,
 Power,
 PowerLedStates,
 Presence,
 PresenceLedStates) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    "FaultLedStates",
    "FeatureSet",
    "INT32withException",
    "IdromBinary16",
    "Index",
    "Power",
    "PowerLedStates",
    "Presence",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

multiFlexServerDrivesMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 15)
)
multiFlexServerDrivesMibModule.setRevisions(
        ("2007-08-16 12:00",
         "2007-07-20 16:45",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-30 17:00",
         "2007-04-18 19:05",
         "2007-04-09 15:45",
         "2007-04-09 15:30",
         "2007-03-27 11:30",
         "2007-03-14 11:30",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2006-12-28 17:30",
         "2006-12-05 10:30",
         "2006-11-27 15:30",
         "2006-11-20 13:30",
         "2006-11-07 11:30",
         "2006-10-02 10:24")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MaxSharedDrives_Type = Unsigned32
_MaxSharedDrives_Object = MibScalar
maxSharedDrives = _MaxSharedDrives_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 15),
    _MaxSharedDrives_Type()
)
maxSharedDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSharedDrives.setStatus("current")
_NumOfSharedDrives_Type = Integer32
_NumOfSharedDrives_Object = MibScalar
numOfSharedDrives = _NumOfSharedDrives_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 25),
    _NumOfSharedDrives_Type()
)
numOfSharedDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfSharedDrives.setStatus("current")
_SDrivePresenceMask_Type = DisplayString
_SDrivePresenceMask_Object = MibScalar
sDrivePresenceMask = _SDrivePresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 35),
    _SDrivePresenceMask_Type()
)
sDrivePresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDrivePresenceMask.setStatus("current")
_SharedDrives_ObjectIdentity = ObjectIdentity
sharedDrives = _SharedDrives_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205)
)
if mibBuilder.loadTexts:
    sharedDrives.setStatus("current")
_DriveBackplane_ObjectIdentity = ObjectIdentity
driveBackplane = _DriveBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1)
)
if mibBuilder.loadTexts:
    driveBackplane.setStatus("current")
_DriveBackplaneVendor_Type = DisplayString
_DriveBackplaneVendor_Object = MibScalar
driveBackplaneVendor = _DriveBackplaneVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 1),
    _DriveBackplaneVendor_Type()
)
driveBackplaneVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplaneVendor.setStatus("current")
_DriveBackplaneMfgDate_Type = DisplayString
_DriveBackplaneMfgDate_Object = MibScalar
driveBackplaneMfgDate = _DriveBackplaneMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 2),
    _DriveBackplaneMfgDate_Type()
)
driveBackplaneMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplaneMfgDate.setStatus("current")
_DriveBackplaneDeviceName_Type = DisplayString
_DriveBackplaneDeviceName_Object = MibScalar
driveBackplaneDeviceName = _DriveBackplaneDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 3),
    _DriveBackplaneDeviceName_Type()
)
driveBackplaneDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplaneDeviceName.setStatus("current")
_DriveBackplanePart_Type = IdromBinary16
_DriveBackplanePart_Object = MibScalar
driveBackplanePart = _DriveBackplanePart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 4),
    _DriveBackplanePart_Type()
)
driveBackplanePart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplanePart.setStatus("current")
_DriveBackplaneSerialNo_Type = IdromBinary16
_DriveBackplaneSerialNo_Object = MibScalar
driveBackplaneSerialNo = _DriveBackplaneSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 5),
    _DriveBackplaneSerialNo_Type()
)
driveBackplaneSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplaneSerialNo.setStatus("current")
_DriveBackplaneMaximumPower_Type = Power
_DriveBackplaneMaximumPower_Object = MibScalar
driveBackplaneMaximumPower = _DriveBackplaneMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 6),
    _DriveBackplaneMaximumPower_Type()
)
driveBackplaneMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplaneMaximumPower.setStatus("current")
_DriveBackplaneNominalPower_Type = Power
_DriveBackplaneNominalPower_Object = MibScalar
driveBackplaneNominalPower = _DriveBackplaneNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 7),
    _DriveBackplaneNominalPower_Type()
)
driveBackplaneNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplaneNominalPower.setStatus("current")
_DriveBackplaneAssetTag_Type = IdromBinary16
_DriveBackplaneAssetTag_Object = MibScalar
driveBackplaneAssetTag = _DriveBackplaneAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 1, 8),
    _DriveBackplaneAssetTag_Type()
)
driveBackplaneAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveBackplaneAssetTag.setStatus("current")
_SharedDriveTable_Object = MibTable
sharedDriveTable = _SharedDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2)
)
if mibBuilder.loadTexts:
    sharedDriveTable.setStatus("current")
_SharedDriveEntry_Object = MibTableRow
sharedDriveEntry = _SharedDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1)
)
sharedDriveEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveSlotNumber"),
)
if mibBuilder.loadTexts:
    sharedDriveEntry.setStatus("current")
_SDriveSlotNumber_Type = Index
_SDriveSlotNumber_Object = MibTableColumn
sDriveSlotNumber = _SDriveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 1),
    _SDriveSlotNumber_Type()
)
sDriveSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveSlotNumber.setStatus("current")
_SDrivePresence_Type = Presence
_SDrivePresence_Object = MibTableColumn
sDrivePresence = _SDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 2),
    _SDrivePresence_Type()
)
sDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDrivePresence.setStatus("current")
_SDriveInterface_Type = DisplayString
_SDriveInterface_Object = MibTableColumn
sDriveInterface = _SDriveInterface_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 3),
    _SDriveInterface_Type()
)
sDriveInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveInterface.setStatus("current")
_SDriveModelNumber_Type = DisplayString
_SDriveModelNumber_Object = MibTableColumn
sDriveModelNumber = _SDriveModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 4),
    _SDriveModelNumber_Type()
)
sDriveModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveModelNumber.setStatus("current")
_SDriveSerialNumber_Type = DisplayString
_SDriveSerialNumber_Object = MibTableColumn
sDriveSerialNumber = _SDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 5),
    _SDriveSerialNumber_Type()
)
sDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveSerialNumber.setStatus("current")
_SDriveFirmwareVersion_Type = DisplayString
_SDriveFirmwareVersion_Object = MibTableColumn
sDriveFirmwareVersion = _SDriveFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 6),
    _SDriveFirmwareVersion_Type()
)
sDriveFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveFirmwareVersion.setStatus("current")
_SDriveProtocolVersion_Type = DisplayString
_SDriveProtocolVersion_Object = MibTableColumn
sDriveProtocolVersion = _SDriveProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 7),
    _SDriveProtocolVersion_Type()
)
sDriveProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveProtocolVersion.setStatus("current")
_SDriveOperationalStatus_Type = DisplayString
_SDriveOperationalStatus_Object = MibTableColumn
sDriveOperationalStatus = _SDriveOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 8),
    _SDriveOperationalStatus_Type()
)
sDriveOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveOperationalStatus.setStatus("current")
_SDriveCondition_Type = DisplayString
_SDriveCondition_Object = MibTableColumn
sDriveCondition = _SDriveCondition_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 9),
    _SDriveCondition_Type()
)
sDriveCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveCondition.setStatus("current")
_SDriveOperation_Type = DisplayString
_SDriveOperation_Object = MibTableColumn
sDriveOperation = _SDriveOperation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 10),
    _SDriveOperation_Type()
)
sDriveOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveOperation.setStatus("current")
_SDriveConfiguration_Type = DisplayString
_SDriveConfiguration_Object = MibTableColumn
sDriveConfiguration = _SDriveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 11),
    _SDriveConfiguration_Type()
)
sDriveConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveConfiguration.setStatus("current")


class _SDriveStoragePoolID_Type(Integer32):
    """Custom type sDriveStoragePoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("notavailable", 256),
          ("unavailable", -1),
          ("unknown", -16))
    )


_SDriveStoragePoolID_Type.__name__ = "Integer32"
_SDriveStoragePoolID_Object = MibTableColumn
sDriveStoragePoolID = _SDriveStoragePoolID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 12),
    _SDriveStoragePoolID_Type()
)
sDriveStoragePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStoragePoolID.setStatus("current")


class _SDriveSequenceNumber_Type(Integer32):
    """Custom type sDriveSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("unavailable", -1),
          ("unknown", -16))
    )


_SDriveSequenceNumber_Type.__name__ = "Integer32"
_SDriveSequenceNumber_Object = MibTableColumn
sDriveSequenceNumber = _SDriveSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 13),
    _SDriveSequenceNumber_Type()
)
sDriveSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveSequenceNumber.setStatus("current")
_SDriveEnclosureID_Type = INT32withException
_SDriveEnclosureID_Object = MibTableColumn
sDriveEnclosureID = _SDriveEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 14),
    _SDriveEnclosureID_Type()
)
sDriveEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveEnclosureID.setStatus("current")
_SDriveBlockSize_Type = INT32withException
_SDriveBlockSize_Object = MibTableColumn
sDriveBlockSize = _SDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 15),
    _SDriveBlockSize_Type()
)
sDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveBlockSize.setStatus("current")
_SDrivePhysicalCapacity_Type = Counter64
_SDrivePhysicalCapacity_Object = MibTableColumn
sDrivePhysicalCapacity = _SDrivePhysicalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 16),
    _SDrivePhysicalCapacity_Type()
)
sDrivePhysicalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDrivePhysicalCapacity.setStatus("current")
_SDriveConfigurableCapacity_Type = Counter64
_SDriveConfigurableCapacity_Object = MibTableColumn
sDriveConfigurableCapacity = _SDriveConfigurableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 17),
    _SDriveConfigurableCapacity_Type()
)
sDriveConfigurableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveConfigurableCapacity.setStatus("current")
_SDriveUsedCapacity_Type = Counter64
_SDriveUsedCapacity_Object = MibTableColumn
sDriveUsedCapacity = _SDriveUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 18),
    _SDriveUsedCapacity_Type()
)
sDriveUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveUsedCapacity.setStatus("current")


class _SDriveType_Type(Integer32):
    """Custom type sDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              -1,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("sas", 4),
          ("sata", 1),
          ("unavailable", -1),
          ("unknown", -16))
    )


_SDriveType_Type.__name__ = "Integer32"
_SDriveType_Object = MibTableColumn
sDriveType = _SDriveType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 2, 1, 19),
    _SDriveType_Type()
)
sDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveType.setStatus("current")
_SharedDriveStatsTable_Object = MibTable
sharedDriveStatsTable = _SharedDriveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3)
)
if mibBuilder.loadTexts:
    sharedDriveStatsTable.setStatus("current")
_SharedDriveStatsEntry_Object = MibTableRow
sharedDriveStatsEntry = _SharedDriveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1)
)
if mibBuilder.loadTexts:
    sharedDriveStatsEntry.setStatus("current")
_SDriveStatsDataTransferred_Type = Counter64
_SDriveStatsDataTransferred_Object = MibTableColumn
sDriveStatsDataTransferred = _SDriveStatsDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 1),
    _SDriveStatsDataTransferred_Type()
)
sDriveStatsDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsDataTransferred.setStatus("current")
_SDriveStatsReadDataTransferred_Type = Counter64
_SDriveStatsReadDataTransferred_Object = MibTableColumn
sDriveStatsReadDataTransferred = _SDriveStatsReadDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 2),
    _SDriveStatsReadDataTransferred_Type()
)
sDriveStatsReadDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsReadDataTransferred.setStatus("current")
_SDriveStatsWriteDataTransferred_Type = Counter64
_SDriveStatsWriteDataTransferred_Object = MibTableColumn
sDriveStatsWriteDataTransferred = _SDriveStatsWriteDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 3),
    _SDriveStatsWriteDataTransferred_Type()
)
sDriveStatsWriteDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsWriteDataTransferred.setStatus("current")
_SDriveStatsNumOfErrors_Type = Integer32
_SDriveStatsNumOfErrors_Object = MibTableColumn
sDriveStatsNumOfErrors = _SDriveStatsNumOfErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 4),
    _SDriveStatsNumOfErrors_Type()
)
sDriveStatsNumOfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfErrors.setStatus("current")
_SDriveStatsNumOfNonRWErrors_Type = Integer32
_SDriveStatsNumOfNonRWErrors_Object = MibTableColumn
sDriveStatsNumOfNonRWErrors = _SDriveStatsNumOfNonRWErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 5),
    _SDriveStatsNumOfNonRWErrors_Type()
)
sDriveStatsNumOfNonRWErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfNonRWErrors.setStatus("current")
_SDriveStatsNumOfReadErrors_Type = Integer32
_SDriveStatsNumOfReadErrors_Object = MibTableColumn
sDriveStatsNumOfReadErrors = _SDriveStatsNumOfReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 6),
    _SDriveStatsNumOfReadErrors_Type()
)
sDriveStatsNumOfReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfReadErrors.setStatus("current")
_SDriveStatsNumOfWriteErrors_Type = Integer32
_SDriveStatsNumOfWriteErrors_Object = MibTableColumn
sDriveStatsNumOfWriteErrors = _SDriveStatsNumOfWriteErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 7),
    _SDriveStatsNumOfWriteErrors_Type()
)
sDriveStatsNumOfWriteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfWriteErrors.setStatus("current")
_SDriveStatsNumOfIORequests_Type = Counter64
_SDriveStatsNumOfIORequests_Object = MibTableColumn
sDriveStatsNumOfIORequests = _SDriveStatsNumOfIORequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 8),
    _SDriveStatsNumOfIORequests_Type()
)
sDriveStatsNumOfIORequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfIORequests.setStatus("current")
_SDriveStatsNumOfNonRWRequests_Type = Counter64
_SDriveStatsNumOfNonRWRequests_Object = MibTableColumn
sDriveStatsNumOfNonRWRequests = _SDriveStatsNumOfNonRWRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 9),
    _SDriveStatsNumOfNonRWRequests_Type()
)
sDriveStatsNumOfNonRWRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfNonRWRequests.setStatus("current")
_SDriveStatsNumOfReadRequests_Type = Counter64
_SDriveStatsNumOfReadRequests_Object = MibTableColumn
sDriveStatsNumOfReadRequests = _SDriveStatsNumOfReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 10),
    _SDriveStatsNumOfReadRequests_Type()
)
sDriveStatsNumOfReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfReadRequests.setStatus("current")
_SDriveStatsNumOfWriteRequests_Type = Counter64
_SDriveStatsNumOfWriteRequests_Object = MibTableColumn
sDriveStatsNumOfWriteRequests = _SDriveStatsNumOfWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 11),
    _SDriveStatsNumOfWriteRequests_Type()
)
sDriveStatsNumOfWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsNumOfWriteRequests.setStatus("current")
_SDriveStatsStartTime_Type = Counter64
_SDriveStatsStartTime_Object = MibTableColumn
sDriveStatsStartTime = _SDriveStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 12),
    _SDriveStatsStartTime_Type()
)
sDriveStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsStartTime.setStatus("current")
_SDriveStatsCollectionTime_Type = Counter64
_SDriveStatsCollectionTime_Object = MibTableColumn
sDriveStatsCollectionTime = _SDriveStatsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 205, 3, 1, 13),
    _SDriveStatsCollectionTime_Type()
)
sDriveStatsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDriveStatsCollectionTime.setStatus("current")
sharedDriveEntry.registerAugmentions(
    ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB",
     "sharedDriveStatsEntry")
)
sharedDriveStatsEntry.setIndexNames(*sharedDriveEntry.getIndexNames())

# Managed Objects groups

sDriveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 15)
)
sDriveGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "maxSharedDrives"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "numOfSharedDrives"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDrivePresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplaneVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplaneMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplaneDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplanePart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplaneSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplaneMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplaneNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "driveBackplaneAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveSlotNumber"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDrivePresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveInterface"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveModelNumber"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveSerialNumber"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveFirmwareVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveProtocolVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveOperationalStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveCondition"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveOperation"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveConfiguration"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStoragePoolID"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveSequenceNumber"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveEnclosureID"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveBlockSize"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDrivePhysicalCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveConfigurableCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveUsedCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsReadDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsWriteDataTransferred"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfNonRWErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfReadErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfWriteErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfIORequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfNonRWRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfReadRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsNumOfWriteRequests"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsStartTime"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB", "sDriveStatsCollectionTime"))
)
if mibBuilder.loadTexts:
    sDriveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-DRIVE-MIB",
    **{"multiFlexServerDrivesMibModule": multiFlexServerDrivesMibModule,
       "sDriveGroup": sDriveGroup,
       "maxSharedDrives": maxSharedDrives,
       "numOfSharedDrives": numOfSharedDrives,
       "sDrivePresenceMask": sDrivePresenceMask,
       "sharedDrives": sharedDrives,
       "driveBackplane": driveBackplane,
       "driveBackplaneVendor": driveBackplaneVendor,
       "driveBackplaneMfgDate": driveBackplaneMfgDate,
       "driveBackplaneDeviceName": driveBackplaneDeviceName,
       "driveBackplanePart": driveBackplanePart,
       "driveBackplaneSerialNo": driveBackplaneSerialNo,
       "driveBackplaneMaximumPower": driveBackplaneMaximumPower,
       "driveBackplaneNominalPower": driveBackplaneNominalPower,
       "driveBackplaneAssetTag": driveBackplaneAssetTag,
       "sharedDriveTable": sharedDriveTable,
       "sharedDriveEntry": sharedDriveEntry,
       "sDriveSlotNumber": sDriveSlotNumber,
       "sDrivePresence": sDrivePresence,
       "sDriveInterface": sDriveInterface,
       "sDriveModelNumber": sDriveModelNumber,
       "sDriveSerialNumber": sDriveSerialNumber,
       "sDriveFirmwareVersion": sDriveFirmwareVersion,
       "sDriveProtocolVersion": sDriveProtocolVersion,
       "sDriveOperationalStatus": sDriveOperationalStatus,
       "sDriveCondition": sDriveCondition,
       "sDriveOperation": sDriveOperation,
       "sDriveConfiguration": sDriveConfiguration,
       "sDriveStoragePoolID": sDriveStoragePoolID,
       "sDriveSequenceNumber": sDriveSequenceNumber,
       "sDriveEnclosureID": sDriveEnclosureID,
       "sDriveBlockSize": sDriveBlockSize,
       "sDrivePhysicalCapacity": sDrivePhysicalCapacity,
       "sDriveConfigurableCapacity": sDriveConfigurableCapacity,
       "sDriveUsedCapacity": sDriveUsedCapacity,
       "sDriveType": sDriveType,
       "sharedDriveStatsTable": sharedDriveStatsTable,
       "sharedDriveStatsEntry": sharedDriveStatsEntry,
       "sDriveStatsDataTransferred": sDriveStatsDataTransferred,
       "sDriveStatsReadDataTransferred": sDriveStatsReadDataTransferred,
       "sDriveStatsWriteDataTransferred": sDriveStatsWriteDataTransferred,
       "sDriveStatsNumOfErrors": sDriveStatsNumOfErrors,
       "sDriveStatsNumOfNonRWErrors": sDriveStatsNumOfNonRWErrors,
       "sDriveStatsNumOfReadErrors": sDriveStatsNumOfReadErrors,
       "sDriveStatsNumOfWriteErrors": sDriveStatsNumOfWriteErrors,
       "sDriveStatsNumOfIORequests": sDriveStatsNumOfIORequests,
       "sDriveStatsNumOfNonRWRequests": sDriveStatsNumOfNonRWRequests,
       "sDriveStatsNumOfReadRequests": sDriveStatsNumOfReadRequests,
       "sDriveStatsNumOfWriteRequests": sDriveStatsNumOfWriteRequests,
       "sDriveStatsStartTime": sDriveStatsStartTime,
       "sDriveStatsCollectionTime": sDriveStatsCollectionTime}
)
