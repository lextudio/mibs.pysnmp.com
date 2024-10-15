# SNMP MIB module (FASTTRAKIDERAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTTRAKIDERAID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:16 2024
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



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Promise_ObjectIdentity = ObjectIdentity
promise = _Promise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7933)
)
_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7933, 343)
)
_Fasttrak_ObjectIdentity = ObjectIdentity
fasttrak = _Fasttrak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1)
)
_Isc3xtraps_ObjectIdentity = ObjectIdentity
isc3xtraps = _Isc3xtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
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
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4),
          ("vVerificationIsNotSupported", 2))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TDiskController_Object = MibTable
tDiskController = _TDiskController_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45)
)
if mibBuilder.loadTexts:
    tDiskController.setStatus("mandatory")
_EDiskController_Object = MibTableRow
eDiskController = _EDiskController_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1)
)
eDiskController.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a45DiskControllerIndex"),
)
if mibBuilder.loadTexts:
    eDiskController.setStatus("mandatory")
_A45DiskControllerIndex_Type = DmiInteger
_A45DiskControllerIndex_Object = MibTableColumn
a45DiskControllerIndex = _A45DiskControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 1),
    _A45DiskControllerIndex_Type()
)
a45DiskControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45DiskControllerIndex.setStatus("mandatory")
_A45FruGroupIndex_Type = DmiInteger
_A45FruGroupIndex_Object = MibTableColumn
a45FruGroupIndex = _A45FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 2),
    _A45FruGroupIndex_Type()
)
a45FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45FruGroupIndex.setStatus("mandatory")
_A45OperationalGroupIndex_Type = DmiInteger
_A45OperationalGroupIndex_Object = MibTableColumn
a45OperationalGroupIndex = _A45OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 3),
    _A45OperationalGroupIndex_Type()
)
a45OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45OperationalGroupIndex.setStatus("mandatory")
_A45SystemSlotIndex_Type = DmiInteger
_A45SystemSlotIndex_Object = MibTableColumn
a45SystemSlotIndex = _A45SystemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 4),
    _A45SystemSlotIndex_Type()
)
a45SystemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45SystemSlotIndex.setStatus("mandatory")
_A45DiskControllerIdentification_Type = DmiDisplaystring
_A45DiskControllerIdentification_Object = MibTableColumn
a45DiskControllerIdentification = _A45DiskControllerIdentification_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 5),
    _A45DiskControllerIdentification_Type()
)
a45DiskControllerIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45DiskControllerIdentification.setStatus("mandatory")
_A45ControllerSoftwareRevisionLevel_Type = DmiDisplaystring
_A45ControllerSoftwareRevisionLevel_Object = MibTableColumn
a45ControllerSoftwareRevisionLevel = _A45ControllerSoftwareRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 6),
    _A45ControllerSoftwareRevisionLevel_Type()
)
a45ControllerSoftwareRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45ControllerSoftwareRevisionLevel.setStatus("mandatory")
_A45ControllerChannelCount_Type = DmiInteger
_A45ControllerChannelCount_Object = MibTableColumn
a45ControllerChannelCount = _A45ControllerChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 7),
    _A45ControllerChannelCount_Type()
)
a45ControllerChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45ControllerChannelCount.setStatus("mandatory")
_A45ControllerMaximumDevices_Type = DmiInteger
_A45ControllerMaximumDevices_Object = MibTableColumn
a45ControllerMaximumDevices = _A45ControllerMaximumDevices_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 45, 1, 8),
    _A45ControllerMaximumDevices_Type()
)
a45ControllerMaximumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45ControllerMaximumDevices.setStatus("mandatory")
_TDisks_Object = MibTable
tDisks = _TDisks_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49)
)
if mibBuilder.loadTexts:
    tDisks.setStatus("mandatory")
_EDisks_Object = MibTableRow
eDisks = _EDisks_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1)
)
eDisks.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a49StorageType"),
    (0, "FASTTRAKIDERAID-MIB", "a49DiskIndex"),
)
if mibBuilder.loadTexts:
    eDisks.setStatus("mandatory")


class _A49StorageType_Type(Integer32):
    """Custom type a49StorageType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("vBernoulli", 10),
          ("vCompactDisk", 8),
          ("vDigitalVersatileDiskDvdDrive", 12),
          ("vDigitalVersatileDiskDvdRamDrive", 13),
          ("vFlashDisk", 9),
          ("vFloppyDisk", 4),
          ("vHardDisk", 3),
          ("vOpticalFloppyDisk", 11),
          ("vOpticalRom", 5),
          ("vOpticalRw", 7),
          ("vOpticalWorm", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A49StorageType_Type.__name__ = "Integer32"
_A49StorageType_Object = MibTableColumn
a49StorageType = _A49StorageType_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 1),
    _A49StorageType_Type()
)
a49StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49StorageType.setStatus("mandatory")
_A49DiskIndex_Type = DmiInteger
_A49DiskIndex_Object = MibTableColumn
a49DiskIndex = _A49DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 2),
    _A49DiskIndex_Type()
)
a49DiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49DiskIndex.setStatus("mandatory")


class _A49StorageInterfaceType_Type(Integer32):
    """Custom type a49StorageInterfaceType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("vCmd", 6),
          ("vDssi", 9),
          ("vEnhancedAtaide", 15),
          ("vEsdi", 4),
          ("vFloppyDiskInterface", 13),
          ("vHippi", 11),
          ("vIde", 5),
          ("vIpi", 7),
          ("vOther", 1),
          ("vParallelPort", 10),
          ("vPcmcia", 14),
          ("vQic2", 12),
          ("vScsi", 3),
          ("vSt506", 8),
          ("vUnknown", 2))
    )


_A49StorageInterfaceType_Type.__name__ = "Integer32"
_A49StorageInterfaceType_Object = MibTableColumn
a49StorageInterfaceType = _A49StorageInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 3),
    _A49StorageInterfaceType_Type()
)
a49StorageInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49StorageInterfaceType.setStatus("mandatory")
_A49InterfaceDescription_Type = DmiDisplaystring
_A49InterfaceDescription_Object = MibTableColumn
a49InterfaceDescription = _A49InterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 4),
    _A49InterfaceDescription_Type()
)
a49InterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49InterfaceDescription.setStatus("mandatory")


class _A49MediaLoaded_Type(Integer32):
    """Custom type a49MediaLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A49MediaLoaded_Type.__name__ = "Integer32"
_A49MediaLoaded_Object = MibTableColumn
a49MediaLoaded = _A49MediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 5),
    _A49MediaLoaded_Type()
)
a49MediaLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49MediaLoaded.setStatus("mandatory")


class _A49RemovableDrive_Type(Integer32):
    """Custom type a49RemovableDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A49RemovableDrive_Type.__name__ = "Integer32"
_A49RemovableDrive_Object = MibTableColumn
a49RemovableDrive = _A49RemovableDrive_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 6),
    _A49RemovableDrive_Type()
)
a49RemovableDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49RemovableDrive.setStatus("mandatory")


class _A49RemovableMedia_Type(Integer32):
    """Custom type a49RemovableMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A49RemovableMedia_Type.__name__ = "Integer32"
_A49RemovableMedia_Object = MibTableColumn
a49RemovableMedia = _A49RemovableMedia_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 7),
    _A49RemovableMedia_Type()
)
a49RemovableMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49RemovableMedia.setStatus("mandatory")
_A49DeviceId_Type = DmiInteger
_A49DeviceId_Object = MibTableColumn
a49DeviceId = _A49DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 8),
    _A49DeviceId_Type()
)
a49DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49DeviceId.setStatus("mandatory")
_A49LogicalUnitNumber_Type = DmiInteger
_A49LogicalUnitNumber_Object = MibTableColumn
a49LogicalUnitNumber = _A49LogicalUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 9),
    _A49LogicalUnitNumber_Type()
)
a49LogicalUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49LogicalUnitNumber.setStatus("mandatory")
_A49NumberOfPhysicalCylinders_Type = DmiInteger
_A49NumberOfPhysicalCylinders_Object = MibTableColumn
a49NumberOfPhysicalCylinders = _A49NumberOfPhysicalCylinders_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 10),
    _A49NumberOfPhysicalCylinders_Type()
)
a49NumberOfPhysicalCylinders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49NumberOfPhysicalCylinders.setStatus("mandatory")
_A49NumberOfPhysicalSectorsPerTrack_Type = DmiInteger
_A49NumberOfPhysicalSectorsPerTrack_Object = MibTableColumn
a49NumberOfPhysicalSectorsPerTrack = _A49NumberOfPhysicalSectorsPerTrack_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 11),
    _A49NumberOfPhysicalSectorsPerTrack_Type()
)
a49NumberOfPhysicalSectorsPerTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49NumberOfPhysicalSectorsPerTrack.setStatus("mandatory")
_A49NumberOfPhysicalHeads_Type = DmiInteger
_A49NumberOfPhysicalHeads_Object = MibTableColumn
a49NumberOfPhysicalHeads = _A49NumberOfPhysicalHeads_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 12),
    _A49NumberOfPhysicalHeads_Type()
)
a49NumberOfPhysicalHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49NumberOfPhysicalHeads.setStatus("mandatory")
_A49PhysicalCylinderForWritePrecompensati_Type = DmiInteger
_A49PhysicalCylinderForWritePrecompensati_Object = MibTableColumn
a49PhysicalCylinderForWritePrecompensati = _A49PhysicalCylinderForWritePrecompensati_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 13),
    _A49PhysicalCylinderForWritePrecompensati_Type()
)
a49PhysicalCylinderForWritePrecompensati.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49PhysicalCylinderForWritePrecompensati.setStatus("mandatory")
_A49PhysicalCylinderForLandingZone_Type = DmiInteger
_A49PhysicalCylinderForLandingZone_Object = MibTableColumn
a49PhysicalCylinderForLandingZone = _A49PhysicalCylinderForLandingZone_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 14),
    _A49PhysicalCylinderForLandingZone_Type()
)
a49PhysicalCylinderForLandingZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49PhysicalCylinderForLandingZone.setStatus("mandatory")
_A49SectorSize_Type = DmiInteger
_A49SectorSize_Object = MibTableColumn
a49SectorSize = _A49SectorSize_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 15),
    _A49SectorSize_Type()
)
a49SectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49SectorSize.setStatus("mandatory")
_A49TotalPhysicalSize_Type = DmiInteger
_A49TotalPhysicalSize_Object = MibTableColumn
a49TotalPhysicalSize = _A49TotalPhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 16),
    _A49TotalPhysicalSize_Type()
)
a49TotalPhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49TotalPhysicalSize.setStatus("mandatory")
_A49NumberOfCurrentBadBlocksOrSectors_Type = DmiInteger
_A49NumberOfCurrentBadBlocksOrSectors_Object = MibTableColumn
a49NumberOfCurrentBadBlocksOrSectors = _A49NumberOfCurrentBadBlocksOrSectors_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 17),
    _A49NumberOfCurrentBadBlocksOrSectors_Type()
)
a49NumberOfCurrentBadBlocksOrSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49NumberOfCurrentBadBlocksOrSectors.setStatus("mandatory")
_A49Partitions_Type = DmiInteger
_A49Partitions_Object = MibTableColumn
a49Partitions = _A49Partitions_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 18),
    _A49Partitions_Type()
)
a49Partitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49Partitions.setStatus("mandatory")


class _A49PhysicalLocation_Type(Integer32):
    """Custom type a49PhysicalLocation based on Integer32"""
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
        *(("vExternal", 4),
          ("vInternal", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A49PhysicalLocation_Type.__name__ = "Integer32"
_A49PhysicalLocation_Object = MibTableColumn
a49PhysicalLocation = _A49PhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 19),
    _A49PhysicalLocation_Type()
)
a49PhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49PhysicalLocation.setStatus("mandatory")
_A49FruGroupIndex_Type = DmiInteger
_A49FruGroupIndex_Object = MibTableColumn
a49FruGroupIndex = _A49FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 20),
    _A49FruGroupIndex_Type()
)
a49FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49FruGroupIndex.setStatus("mandatory")
_A49OperationalGroupIndex_Type = DmiInteger
_A49OperationalGroupIndex_Object = MibTableColumn
a49OperationalGroupIndex = _A49OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 21),
    _A49OperationalGroupIndex_Type()
)
a49OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49OperationalGroupIndex.setStatus("mandatory")


class _A49SecuritySettings_Type(Integer32):
    """Custom type a49SecuritySettings based on Integer32"""
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
        *(("vBoot-bypass", 6),
          ("vBoot-bypass-Read-only", 7),
          ("vLockoutEnabled", 5),
          ("vNone", 3),
          ("vOther", 1),
          ("vRead-only", 4),
          ("vUnknown", 2))
    )


_A49SecuritySettings_Type.__name__ = "Integer32"
_A49SecuritySettings_Object = MibTableColumn
a49SecuritySettings = _A49SecuritySettings_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 49, 1, 22),
    _A49SecuritySettings_Type()
)
a49SecuritySettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a49SecuritySettings.setStatus("mandatory")
_TMassStoreArrayInfoTable_Object = MibTable
tMassStoreArrayInfoTable = _TMassStoreArrayInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 85)
)
if mibBuilder.loadTexts:
    tMassStoreArrayInfoTable.setStatus("mandatory")
_EMassStoreArrayInfoTable_Object = MibTableRow
eMassStoreArrayInfoTable = _EMassStoreArrayInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 85, 1)
)
eMassStoreArrayInfoTable.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a85LogicalDriveIndex"),
)
if mibBuilder.loadTexts:
    eMassStoreArrayInfoTable.setStatus("mandatory")
_A85LogicalDriveIndex_Type = DmiInteger
_A85LogicalDriveIndex_Object = MibTableColumn
a85LogicalDriveIndex = _A85LogicalDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 85, 1, 1),
    _A85LogicalDriveIndex_Type()
)
a85LogicalDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a85LogicalDriveIndex.setStatus("mandatory")


class _A85DriveArrayLevel_Type(Integer32):
    """Custom type a85DriveArrayLevel based on Integer32"""
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
        *(("vOther", 1),
          ("vRaid0", 3),
          ("vRaid1", 4),
          ("vRaid10", 10),
          ("vRaid2", 5),
          ("vRaid3", 6),
          ("vRaid4", 7),
          ("vRaid5", 8),
          ("vRaid7", 9),
          ("vUnknown", 2))
    )


_A85DriveArrayLevel_Type.__name__ = "Integer32"
_A85DriveArrayLevel_Object = MibTableColumn
a85DriveArrayLevel = _A85DriveArrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 85, 1, 2),
    _A85DriveArrayLevel_Type()
)
a85DriveArrayLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a85DriveArrayLevel.setStatus("mandatory")


class _A85DriveArrayRedundancyStatus_Type(Integer32):
    """Custom type a85DriveArrayRedundancyStatus based on Integer32"""
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
        *(("vDegradedRedundancy", 4),
          ("vFullyRedundant", 3),
          ("vNotApplicableUnitNotRedundant", 6),
          ("vOther", 1),
          ("vRedundancyLost", 5),
          ("vUnitFailed", 7),
          ("vUnknown", 2))
    )


_A85DriveArrayRedundancyStatus_Type.__name__ = "Integer32"
_A85DriveArrayRedundancyStatus_Object = MibTableColumn
a85DriveArrayRedundancyStatus = _A85DriveArrayRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 85, 1, 5),
    _A85DriveArrayRedundancyStatus_Type()
)
a85DriveArrayRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a85DriveArrayRedundancyStatus.setStatus("mandatory")


class _A85DriveArrayOperationInProgress_Type(Integer32):
    """Custom type a85DriveArrayOperationInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vNone", 6),
          ("vOther", 1),
          ("vRebuild", 5),
          ("vUnknown", 2),
          ("vVerify", 3))
    )


_A85DriveArrayOperationInProgress_Type.__name__ = "Integer32"
_A85DriveArrayOperationInProgress_Object = MibTableColumn
a85DriveArrayOperationInProgress = _A85DriveArrayOperationInProgress_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 85, 1, 6),
    _A85DriveArrayOperationInProgress_Type()
)
a85DriveArrayOperationInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a85DriveArrayOperationInProgress.setStatus("mandatory")
_TMassStoreLogicalDrivesTable_Object = MibTable
tMassStoreLogicalDrivesTable = _TMassStoreLogicalDrivesTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86)
)
if mibBuilder.loadTexts:
    tMassStoreLogicalDrivesTable.setStatus("mandatory")
_EMassStoreLogicalDrivesTable_Object = MibTableRow
eMassStoreLogicalDrivesTable = _EMassStoreLogicalDrivesTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86, 1)
)
eMassStoreLogicalDrivesTable.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a86LogicalDriveIndex"),
)
if mibBuilder.loadTexts:
    eMassStoreLogicalDrivesTable.setStatus("mandatory")
_A86LogicalDriveIndex_Type = DmiInteger
_A86LogicalDriveIndex_Object = MibTableColumn
a86LogicalDriveIndex = _A86LogicalDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86, 1, 1),
    _A86LogicalDriveIndex_Type()
)
a86LogicalDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a86LogicalDriveIndex.setStatus("mandatory")


class _A86TopOfHierarchy_Type(Integer32):
    """Custom type a86TopOfHierarchy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A86TopOfHierarchy_Type.__name__ = "Integer32"
_A86TopOfHierarchy_Object = MibTableColumn
a86TopOfHierarchy = _A86TopOfHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86, 1, 2),
    _A86TopOfHierarchy_Type()
)
a86TopOfHierarchy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a86TopOfHierarchy.setStatus("mandatory")


class _A86DriveArray_Type(Integer32):
    """Custom type a86DriveArray based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A86DriveArray_Type.__name__ = "Integer32"
_A86DriveArray_Object = MibTableColumn
a86DriveArray = _A86DriveArray_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86, 1, 3),
    _A86DriveArray_Type()
)
a86DriveArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a86DriveArray.setStatus("mandatory")
_A86LogicalDriveSizeInKb_Type = DmiInteger
_A86LogicalDriveSizeInKb_Object = MibTableColumn
a86LogicalDriveSizeInKb = _A86LogicalDriveSizeInKb_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86, 1, 4),
    _A86LogicalDriveSizeInKb_Type()
)
a86LogicalDriveSizeInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a86LogicalDriveSizeInKb.setStatus("mandatory")
_A86LogicalDriveBlockSizeInBytes_Type = DmiInteger
_A86LogicalDriveBlockSizeInBytes_Object = MibTableColumn
a86LogicalDriveBlockSizeInBytes = _A86LogicalDriveBlockSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86, 1, 5),
    _A86LogicalDriveBlockSizeInBytes_Type()
)
a86LogicalDriveBlockSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a86LogicalDriveBlockSizeInBytes.setStatus("mandatory")
_A86LogicalDriveNameString_Type = DmiDisplaystring
_A86LogicalDriveNameString_Object = MibTableColumn
a86LogicalDriveNameString = _A86LogicalDriveNameString_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 86, 1, 6),
    _A86LogicalDriveNameString_Type()
)
a86LogicalDriveNameString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a86LogicalDriveNameString.setStatus("mandatory")
_TMassStoreMappingTable_Object = MibTable
tMassStoreMappingTable = _TMassStoreMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 87)
)
if mibBuilder.loadTexts:
    tMassStoreMappingTable.setStatus("mandatory")
_EMassStoreMappingTable_Object = MibTableRow
eMassStoreMappingTable = _EMassStoreMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 87, 1)
)
eMassStoreMappingTable.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a87MappingIndex"),
)
if mibBuilder.loadTexts:
    eMassStoreMappingTable.setStatus("mandatory")
_A87MappingIndex_Type = DmiInteger
_A87MappingIndex_Object = MibTableColumn
a87MappingIndex = _A87MappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 87, 1, 1),
    _A87MappingIndex_Type()
)
a87MappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a87MappingIndex.setStatus("mandatory")
_A87ParentDrive_Type = DmiInteger
_A87ParentDrive_Object = MibTableColumn
a87ParentDrive = _A87ParentDrive_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 87, 1, 2),
    _A87ParentDrive_Type()
)
a87ParentDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a87ParentDrive.setStatus("mandatory")
_A87ChildSegment_Type = DmiInteger
_A87ChildSegment_Object = MibTableColumn
a87ChildSegment = _A87ChildSegment_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 87, 1, 3),
    _A87ChildSegment_Type()
)
a87ChildSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a87ChildSegment.setStatus("mandatory")
_TMassStoreSegmentTable_Object = MibTable
tMassStoreSegmentTable = _TMassStoreSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88)
)
if mibBuilder.loadTexts:
    tMassStoreSegmentTable.setStatus("mandatory")
_EMassStoreSegmentTable_Object = MibTableRow
eMassStoreSegmentTable = _EMassStoreSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1)
)
eMassStoreSegmentTable.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a88SegmentIndex"),
)
if mibBuilder.loadTexts:
    eMassStoreSegmentTable.setStatus("mandatory")
_A88SegmentIndex_Type = DmiInteger
_A88SegmentIndex_Object = MibTableColumn
a88SegmentIndex = _A88SegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 1),
    _A88SegmentIndex_Type()
)
a88SegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88SegmentIndex.setStatus("mandatory")


class _A88SegmentType_Type(Integer32):
    """Custom type a88SegmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vLogical", 2),
          ("vPhysical", 1))
    )


_A88SegmentType_Type.__name__ = "Integer32"
_A88SegmentType_Object = MibTableColumn
a88SegmentType = _A88SegmentType_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 2),
    _A88SegmentType_Type()
)
a88SegmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88SegmentType.setStatus("mandatory")
_A88SegmentStart_Type = DmiInteger
_A88SegmentStart_Object = MibTableColumn
a88SegmentStart = _A88SegmentStart_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 3),
    _A88SegmentStart_Type()
)
a88SegmentStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88SegmentStart.setStatus("mandatory")
_A88SegmentLength_Type = DmiInteger
_A88SegmentLength_Object = MibTableColumn
a88SegmentLength = _A88SegmentLength_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 4),
    _A88SegmentLength_Type()
)
a88SegmentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88SegmentLength.setStatus("mandatory")


class _A88SegmentAllocationUnit_Type(Integer32):
    """Custom type a88SegmentAllocationUnit based on Integer32"""
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
        *(("vLogicalBlock", 4),
          ("vOther", 1),
          ("vPhysicalSector", 3),
          ("vUnknown", 2))
    )


_A88SegmentAllocationUnit_Type.__name__ = "Integer32"
_A88SegmentAllocationUnit_Object = MibTableColumn
a88SegmentAllocationUnit = _A88SegmentAllocationUnit_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 5),
    _A88SegmentAllocationUnit_Type()
)
a88SegmentAllocationUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88SegmentAllocationUnit.setStatus("mandatory")


class _A88SegmentAllocationState_Type(Integer32):
    """Custom type a88SegmentAllocationState based on Integer32"""
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
        *(("vAllocated", 3),
          ("vAvailable", 4),
          ("vDefective", 5),
          ("vOther", 1),
          ("vReserved1", 6),
          ("vSpare", 7),
          ("vUnknown", 2))
    )


_A88SegmentAllocationState_Type.__name__ = "Integer32"
_A88SegmentAllocationState_Object = MibTableColumn
a88SegmentAllocationState = _A88SegmentAllocationState_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 6),
    _A88SegmentAllocationState_Type()
)
a88SegmentAllocationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88SegmentAllocationState.setStatus("mandatory")


class _A88DriveKey1_Type(Integer32):
    """Custom type a88DriveKey1 based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("vBernoulli", 10),
          ("vCompactDisk", 8),
          ("vFlashDisk", 9),
          ("vFloppyDisk", 4),
          ("vHardDisk", 3),
          ("vOpticalFloppyDisk", 11),
          ("vOpticalRom", 5),
          ("vOpticalRw", 7),
          ("vOpticalWorm", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A88DriveKey1_Type.__name__ = "Integer32"
_A88DriveKey1_Object = MibTableColumn
a88DriveKey1 = _A88DriveKey1_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 7),
    _A88DriveKey1_Type()
)
a88DriveKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88DriveKey1.setStatus("mandatory")
_A88DriveKey2_Type = DmiInteger
_A88DriveKey2_Object = MibTableColumn
a88DriveKey2 = _A88DriveKey2_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 88, 1, 8),
    _A88DriveKey2_Type()
)
a88DriveKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a88DriveKey2.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")
_TEventState_Object = MibTable
tEventState = _TEventState_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 100)
)
if mibBuilder.loadTexts:
    tEventState.setStatus("mandatory")
_EEventState_Object = MibTableRow
eEventState = _EEventState_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 100, 1)
)
eEventState.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a100EventIndex"),
)
if mibBuilder.loadTexts:
    eEventState.setStatus("mandatory")
_A100EventIndex_Type = DmiInteger
_A100EventIndex_Object = MibTableColumn
a100EventIndex = _A100EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 100, 1, 1),
    _A100EventIndex_Type()
)
a100EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventIndex.setStatus("mandatory")
_A100EventGenerationGroupClass_Type = DmiDisplaystring
_A100EventGenerationGroupClass_Object = MibTableColumn
a100EventGenerationGroupClass = _A100EventGenerationGroupClass_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 100, 1, 2),
    _A100EventGenerationGroupClass_Type()
)
a100EventGenerationGroupClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventGenerationGroupClass.setStatus("mandatory")
_A100EventType_Type = DmiInteger
_A100EventType_Object = MibTableColumn
a100EventType = _A100EventType_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 100, 1, 3),
    _A100EventType_Type()
)
a100EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventType.setStatus("mandatory")


class _A100CurrentState_Type(Integer32):
    """Custom type a100CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A100CurrentState_Type.__name__ = "Integer32"
_A100CurrentState_Object = MibTableColumn
a100CurrentState = _A100CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 100, 1, 4),
    _A100CurrentState_Type()
)
a100CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100CurrentState.setStatus("mandatory")
_A100AssociatedGroupObject_Type = DmiDisplaystring
_A100AssociatedGroupObject_Object = MibTableColumn
a100AssociatedGroupObject = _A100AssociatedGroupObject_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 100, 1, 5),
    _A100AssociatedGroupObject_Type()
)
a100AssociatedGroupObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100AssociatedGroupObject.setStatus("mandatory")
_TEventGenerationForDiskController_Object = MibTable
tEventGenerationForDiskController = _TEventGenerationForDiskController_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238)
)
if mibBuilder.loadTexts:
    tEventGenerationForDiskController.setStatus("mandatory")
_EEventGenerationForDiskController_Object = MibTableRow
eEventGenerationForDiskController = _EEventGenerationForDiskController_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1)
)
eEventGenerationForDiskController.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a238AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForDiskController.setStatus("mandatory")


class _A238EventType_Type(Integer32):
    """Custom type a238EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vConfigurationError", 2),
          ("vInitializationFailure", 1))
    )


_A238EventType_Type.__name__ = "Integer32"
_A238EventType_Object = MibTableColumn
a238EventType = _A238EventType_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1, 1),
    _A238EventType_Type()
)
a238EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a238EventType.setStatus("mandatory")


class _A238EventSeverity_Type(Integer32):
    """Custom type a238EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical1", 8),
          ("vNon-recoverable1", 32),
          ("vOk", 4))
    )


_A238EventSeverity_Type.__name__ = "Integer32"
_A238EventSeverity_Object = MibTableColumn
a238EventSeverity = _A238EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1, 2),
    _A238EventSeverity_Type()
)
a238EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a238EventSeverity.setStatus("mandatory")


class _A238IsEventState_based_Type(Integer32):
    """Custom type a238IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A238IsEventState_based_Type.__name__ = "Integer32"
_A238IsEventState_based_Object = MibScalar
a238IsEventState_based = _A238IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1, 3),
    _A238IsEventState_based_Type()
)
a238IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a238IsEventState_based.setStatus("mandatory")
_A238EventStateKey_Type = DmiInteger
_A238EventStateKey_Object = MibTableColumn
a238EventStateKey = _A238EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1, 4),
    _A238EventStateKey_Type()
)
a238EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a238EventStateKey.setStatus("mandatory")
_A238AssociatedGroup_Type = DmiDisplaystring
_A238AssociatedGroup_Object = MibTableColumn
a238AssociatedGroup = _A238AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1, 5),
    _A238AssociatedGroup_Type()
)
a238AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a238AssociatedGroup.setStatus("mandatory")


class _A238EventSystem_Type(Integer32):
    """Custom type a238EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A238EventSystem_Type.__name__ = "Integer32"
_A238EventSystem_Object = MibTableColumn
a238EventSystem = _A238EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1, 6),
    _A238EventSystem_Type()
)
a238EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a238EventSystem.setStatus("mandatory")


class _A238EventSubsystem_Type(Integer32):
    """Custom type a238EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A238EventSubsystem_Type.__name__ = "Integer32"
_A238EventSubsystem_Object = MibTableColumn
a238EventSubsystem = _A238EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 238, 1, 7),
    _A238EventSubsystem_Type()
)
a238EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a238EventSubsystem.setStatus("mandatory")
_TEventGenerationForDisks_Object = MibTable
tEventGenerationForDisks = _TEventGenerationForDisks_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239)
)
if mibBuilder.loadTexts:
    tEventGenerationForDisks.setStatus("mandatory")
_EEventGenerationForDisks_Object = MibTableRow
eEventGenerationForDisks = _EEventGenerationForDisks_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1)
)
eEventGenerationForDisks.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a239AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForDisks.setStatus("mandatory")


class _A239EventType_Type(Integer32):
    """Custom type a239EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vConfigurationError", 3),
          ("vInitializationFailure", 2),
          ("vPhysicalDeviceStatusChange", 1))
    )


_A239EventType_Type.__name__ = "Integer32"
_A239EventType_Object = MibTableColumn
a239EventType = _A239EventType_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1, 1),
    _A239EventType_Type()
)
a239EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a239EventType.setStatus("mandatory")


class _A239EventSeverity_Type(Integer32):
    """Custom type a239EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A239EventSeverity_Type.__name__ = "Integer32"
_A239EventSeverity_Object = MibTableColumn
a239EventSeverity = _A239EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1, 2),
    _A239EventSeverity_Type()
)
a239EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a239EventSeverity.setStatus("mandatory")


class _A239IsEventState_based_Type(Integer32):
    """Custom type a239IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A239IsEventState_based_Type.__name__ = "Integer32"
_A239IsEventState_based_Object = MibScalar
a239IsEventState_based = _A239IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1, 3),
    _A239IsEventState_based_Type()
)
a239IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a239IsEventState_based.setStatus("mandatory")
_A239EventStateKey_Type = DmiInteger
_A239EventStateKey_Object = MibTableColumn
a239EventStateKey = _A239EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1, 4),
    _A239EventStateKey_Type()
)
a239EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a239EventStateKey.setStatus("mandatory")
_A239AssociatedGroup_Type = DmiDisplaystring
_A239AssociatedGroup_Object = MibTableColumn
a239AssociatedGroup = _A239AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1, 5),
    _A239AssociatedGroup_Type()
)
a239AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a239AssociatedGroup.setStatus("mandatory")


class _A239EventSystem_Type(Integer32):
    """Custom type a239EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A239EventSystem_Type.__name__ = "Integer32"
_A239EventSystem_Object = MibTableColumn
a239EventSystem = _A239EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1, 6),
    _A239EventSystem_Type()
)
a239EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a239EventSystem.setStatus("mandatory")


class _A239EventSubsystem_Type(Integer32):
    """Custom type a239EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A239EventSubsystem_Type.__name__ = "Integer32"
_A239EventSubsystem_Object = MibTableColumn
a239EventSubsystem = _A239EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 239, 1, 7),
    _A239EventSubsystem_Type()
)
a239EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a239EventSubsystem.setStatus("mandatory")
_TEventGenerationForMassStoreLogicalDrive_Object = MibTable
tEventGenerationForMassStoreLogicalDrive = _TEventGenerationForMassStoreLogicalDrive_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244)
)
if mibBuilder.loadTexts:
    tEventGenerationForMassStoreLogicalDrive.setStatus("mandatory")
_EEventGenerationForMassStoreLogicalDrive_Object = MibTableRow
eEventGenerationForMassStoreLogicalDrive = _EEventGenerationForMassStoreLogicalDrive_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1)
)
eEventGenerationForMassStoreLogicalDrive.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
    (0, "FASTTRAKIDERAID-MIB", "a244AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForMassStoreLogicalDrive.setStatus("mandatory")


class _A244EventType_Type(Integer32):
    """Custom type a244EventType based on Integer32"""
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
        *(("vConfigurationError", 5),
          ("vHotSpareActivated", 2),
          ("vInitializationFailure", 4),
          ("vLogicalDeviceStatusChange", 3),
          ("vPhysicalDeviceStatusChange", 1))
    )


_A244EventType_Type.__name__ = "Integer32"
_A244EventType_Object = MibTableColumn
a244EventType = _A244EventType_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1, 1),
    _A244EventType_Type()
)
a244EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a244EventType.setStatus("mandatory")


class _A244EventSeverity_Type(Integer32):
    """Custom type a244EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A244EventSeverity_Type.__name__ = "Integer32"
_A244EventSeverity_Object = MibTableColumn
a244EventSeverity = _A244EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1, 2),
    _A244EventSeverity_Type()
)
a244EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a244EventSeverity.setStatus("mandatory")


class _A244IsEventState_based_Type(Integer32):
    """Custom type a244IsEventState_based based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A244IsEventState_based_Type.__name__ = "Integer32"
_A244IsEventState_based_Object = MibScalar
a244IsEventState_based = _A244IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1, 3),
    _A244IsEventState_based_Type()
)
a244IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a244IsEventState_based.setStatus("mandatory")
_A244EventStateKey_Type = DmiInteger
_A244EventStateKey_Object = MibTableColumn
a244EventStateKey = _A244EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1, 4),
    _A244EventStateKey_Type()
)
a244EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a244EventStateKey.setStatus("mandatory")
_A244AssociatedGroup_Type = DmiDisplaystring
_A244AssociatedGroup_Object = MibTableColumn
a244AssociatedGroup = _A244AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1, 5),
    _A244AssociatedGroup_Type()
)
a244AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a244AssociatedGroup.setStatus("mandatory")


class _A244EventSystem_Type(Integer32):
    """Custom type a244EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A244EventSystem_Type.__name__ = "Integer32"
_A244EventSystem_Object = MibTableColumn
a244EventSystem = _A244EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1, 6),
    _A244EventSystem_Type()
)
a244EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a244EventSystem.setStatus("mandatory")


class _A244EventSubsystem_Type(Integer32):
    """Custom type a244EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A244EventSubsystem_Type.__name__ = "Integer32"
_A244EventSubsystem_Object = MibTableColumn
a244EventSubsystem = _A244EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 244, 1, 7),
    _A244EventSubsystem_Type()
)
a244EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a244EventSubsystem.setStatus("mandatory")
_TTrapGroup_Object = MibTable
tTrapGroup = _TTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999)
)
if mibBuilder.loadTexts:
    tTrapGroup.setStatus("mandatory")
_ETrapGroup_Object = MibTableRow
eTrapGroup = _ETrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1)
)
eTrapGroup.setIndexNames(
    (0, "FASTTRAKIDERAID-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eTrapGroup.setStatus("mandatory")
_A9999ErrorTime_Type = DisplayString
_A9999ErrorTime_Object = MibTableColumn
a9999ErrorTime = _A9999ErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 1),
    _A9999ErrorTime_Type()
)
a9999ErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorTime.setStatus("mandatory")
_A9999ErrorStatus_Type = DmiInteger
_A9999ErrorStatus_Object = MibTableColumn
a9999ErrorStatus = _A9999ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 2),
    _A9999ErrorStatus_Type()
)
a9999ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorStatus.setStatus("mandatory")
_A9999ErrorGroupId_Type = DmiInteger
_A9999ErrorGroupId_Object = MibTableColumn
a9999ErrorGroupId = _A9999ErrorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 3),
    _A9999ErrorGroupId_Type()
)
a9999ErrorGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorGroupId.setStatus("mandatory")
_A9999ErrorInstanceId_Type = DmiInteger
_A9999ErrorInstanceId_Object = MibTableColumn
a9999ErrorInstanceId = _A9999ErrorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 4),
    _A9999ErrorInstanceId_Type()
)
a9999ErrorInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorInstanceId.setStatus("mandatory")
_A9999ComponentId_Type = DmiInteger
_A9999ComponentId_Object = MibTableColumn
a9999ComponentId = _A9999ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 5),
    _A9999ComponentId_Type()
)
a9999ComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ComponentId.setStatus("mandatory")
_A9999GroupId_Type = DmiInteger
_A9999GroupId_Object = MibTableColumn
a9999GroupId = _A9999GroupId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 6),
    _A9999GroupId_Type()
)
a9999GroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999GroupId.setStatus("mandatory")
_A9999InstanceId_Type = DmiInteger
_A9999InstanceId_Object = MibTableColumn
a9999InstanceId = _A9999InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 7),
    _A9999InstanceId_Type()
)
a9999InstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999InstanceId.setStatus("mandatory")
_A9999VendorCode1_Type = DmiInteger
_A9999VendorCode1_Object = MibTableColumn
a9999VendorCode1 = _A9999VendorCode1_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 8),
    _A9999VendorCode1_Type()
)
a9999VendorCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode1.setStatus("mandatory")
_A9999VendorCode2_Type = DmiInteger
_A9999VendorCode2_Object = MibTableColumn
a9999VendorCode2 = _A9999VendorCode2_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 9),
    _A9999VendorCode2_Type()
)
a9999VendorCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode2.setStatus("mandatory")
_A9999VendorText_Type = OctetString
_A9999VendorText_Object = MibTableColumn
a9999VendorText = _A9999VendorText_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 10),
    _A9999VendorText_Type()
)
a9999VendorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorText.setStatus("mandatory")
_A9999ParentGroupId_Type = DmiInteger
_A9999ParentGroupId_Object = MibTableColumn
a9999ParentGroupId = _A9999ParentGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 11),
    _A9999ParentGroupId_Type()
)
a9999ParentGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentGroupId.setStatus("mandatory")
_A9999ParentInstanceId_Type = DmiInteger
_A9999ParentInstanceId_Object = MibTableColumn
a9999ParentInstanceId = _A9999ParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 12),
    _A9999ParentInstanceId_Type()
)
a9999ParentInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentInstanceId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dmtfEventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 7933, 343, 1, 1, 1, 9999, 1, 0, 1)
)
dmtfEventError.setObjects(
      *(("FASTTRAKIDERAID-MIB", "a9999ErrorTime"),
        ("FASTTRAKIDERAID-MIB", "a9999ErrorStatus"),
        ("FASTTRAKIDERAID-MIB", "a9999ErrorGroupId"),
        ("FASTTRAKIDERAID-MIB", "a9999ErrorInstanceId"),
        ("FASTTRAKIDERAID-MIB", "a9999ComponentId"),
        ("FASTTRAKIDERAID-MIB", "a9999GroupId"),
        ("FASTTRAKIDERAID-MIB", "a9999InstanceId"),
        ("FASTTRAKIDERAID-MIB", "a9999VendorCode1"),
        ("FASTTRAKIDERAID-MIB", "a9999VendorCode2"),
        ("FASTTRAKIDERAID-MIB", "a9999VendorText"),
        ("FASTTRAKIDERAID-MIB", "a9999ParentGroupId"),
        ("FASTTRAKIDERAID-MIB", "a9999ParentInstanceId"))
)
if mibBuilder.loadTexts:
    dmtfEventError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTTRAKIDERAID-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "promise": promise,
       "intel": intel,
       "fasttrak": fasttrak,
       "isc3xtraps": isc3xtraps,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tDiskController": tDiskController,
       "eDiskController": eDiskController,
       "a45DiskControllerIndex": a45DiskControllerIndex,
       "a45FruGroupIndex": a45FruGroupIndex,
       "a45OperationalGroupIndex": a45OperationalGroupIndex,
       "a45SystemSlotIndex": a45SystemSlotIndex,
       "a45DiskControllerIdentification": a45DiskControllerIdentification,
       "a45ControllerSoftwareRevisionLevel": a45ControllerSoftwareRevisionLevel,
       "a45ControllerChannelCount": a45ControllerChannelCount,
       "a45ControllerMaximumDevices": a45ControllerMaximumDevices,
       "tDisks": tDisks,
       "eDisks": eDisks,
       "a49StorageType": a49StorageType,
       "a49DiskIndex": a49DiskIndex,
       "a49StorageInterfaceType": a49StorageInterfaceType,
       "a49InterfaceDescription": a49InterfaceDescription,
       "a49MediaLoaded": a49MediaLoaded,
       "a49RemovableDrive": a49RemovableDrive,
       "a49RemovableMedia": a49RemovableMedia,
       "a49DeviceId": a49DeviceId,
       "a49LogicalUnitNumber": a49LogicalUnitNumber,
       "a49NumberOfPhysicalCylinders": a49NumberOfPhysicalCylinders,
       "a49NumberOfPhysicalSectorsPerTrack": a49NumberOfPhysicalSectorsPerTrack,
       "a49NumberOfPhysicalHeads": a49NumberOfPhysicalHeads,
       "a49PhysicalCylinderForWritePrecompensati": a49PhysicalCylinderForWritePrecompensati,
       "a49PhysicalCylinderForLandingZone": a49PhysicalCylinderForLandingZone,
       "a49SectorSize": a49SectorSize,
       "a49TotalPhysicalSize": a49TotalPhysicalSize,
       "a49NumberOfCurrentBadBlocksOrSectors": a49NumberOfCurrentBadBlocksOrSectors,
       "a49Partitions": a49Partitions,
       "a49PhysicalLocation": a49PhysicalLocation,
       "a49FruGroupIndex": a49FruGroupIndex,
       "a49OperationalGroupIndex": a49OperationalGroupIndex,
       "a49SecuritySettings": a49SecuritySettings,
       "tMassStoreArrayInfoTable": tMassStoreArrayInfoTable,
       "eMassStoreArrayInfoTable": eMassStoreArrayInfoTable,
       "a85LogicalDriveIndex": a85LogicalDriveIndex,
       "a85DriveArrayLevel": a85DriveArrayLevel,
       "a85DriveArrayRedundancyStatus": a85DriveArrayRedundancyStatus,
       "a85DriveArrayOperationInProgress": a85DriveArrayOperationInProgress,
       "tMassStoreLogicalDrivesTable": tMassStoreLogicalDrivesTable,
       "eMassStoreLogicalDrivesTable": eMassStoreLogicalDrivesTable,
       "a86LogicalDriveIndex": a86LogicalDriveIndex,
       "a86TopOfHierarchy": a86TopOfHierarchy,
       "a86DriveArray": a86DriveArray,
       "a86LogicalDriveSizeInKb": a86LogicalDriveSizeInKb,
       "a86LogicalDriveBlockSizeInBytes": a86LogicalDriveBlockSizeInBytes,
       "a86LogicalDriveNameString": a86LogicalDriveNameString,
       "tMassStoreMappingTable": tMassStoreMappingTable,
       "eMassStoreMappingTable": eMassStoreMappingTable,
       "a87MappingIndex": a87MappingIndex,
       "a87ParentDrive": a87ParentDrive,
       "a87ChildSegment": a87ChildSegment,
       "tMassStoreSegmentTable": tMassStoreSegmentTable,
       "eMassStoreSegmentTable": eMassStoreSegmentTable,
       "a88SegmentIndex": a88SegmentIndex,
       "a88SegmentType": a88SegmentType,
       "a88SegmentStart": a88SegmentStart,
       "a88SegmentLength": a88SegmentLength,
       "a88SegmentAllocationUnit": a88SegmentAllocationUnit,
       "a88SegmentAllocationState": a88SegmentAllocationState,
       "a88DriveKey1": a88DriveKey1,
       "a88DriveKey2": a88DriveKey2,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap,
       "tEventState": tEventState,
       "eEventState": eEventState,
       "a100EventIndex": a100EventIndex,
       "a100EventGenerationGroupClass": a100EventGenerationGroupClass,
       "a100EventType": a100EventType,
       "a100CurrentState": a100CurrentState,
       "a100AssociatedGroupObject": a100AssociatedGroupObject,
       "tEventGenerationForDiskController": tEventGenerationForDiskController,
       "eEventGenerationForDiskController": eEventGenerationForDiskController,
       "a238EventType": a238EventType,
       "a238EventSeverity": a238EventSeverity,
       "a238IsEventState-based": a238IsEventState_based,
       "a238EventStateKey": a238EventStateKey,
       "a238AssociatedGroup": a238AssociatedGroup,
       "a238EventSystem": a238EventSystem,
       "a238EventSubsystem": a238EventSubsystem,
       "tEventGenerationForDisks": tEventGenerationForDisks,
       "eEventGenerationForDisks": eEventGenerationForDisks,
       "a239EventType": a239EventType,
       "a239EventSeverity": a239EventSeverity,
       "a239IsEventState-based": a239IsEventState_based,
       "a239EventStateKey": a239EventStateKey,
       "a239AssociatedGroup": a239AssociatedGroup,
       "a239EventSystem": a239EventSystem,
       "a239EventSubsystem": a239EventSubsystem,
       "tEventGenerationForMassStoreLogicalDrive": tEventGenerationForMassStoreLogicalDrive,
       "eEventGenerationForMassStoreLogicalDrive": eEventGenerationForMassStoreLogicalDrive,
       "a244EventType": a244EventType,
       "a244EventSeverity": a244EventSeverity,
       "a244IsEventState-based": a244IsEventState_based,
       "a244EventStateKey": a244EventStateKey,
       "a244AssociatedGroup": a244AssociatedGroup,
       "a244EventSystem": a244EventSystem,
       "a244EventSubsystem": a244EventSubsystem,
       "tTrapGroup": tTrapGroup,
       "eTrapGroup": eTrapGroup,
       "dmtfEventError": dmtfEventError,
       "a9999ErrorTime": a9999ErrorTime,
       "a9999ErrorStatus": a9999ErrorStatus,
       "a9999ErrorGroupId": a9999ErrorGroupId,
       "a9999ErrorInstanceId": a9999ErrorInstanceId,
       "a9999ComponentId": a9999ComponentId,
       "a9999GroupId": a9999GroupId,
       "a9999InstanceId": a9999InstanceId,
       "a9999VendorCode1": a9999VendorCode1,
       "a9999VendorCode2": a9999VendorCode2,
       "a9999VendorText": a9999VendorText,
       "a9999ParentGroupId": a9999ParentGroupId,
       "a9999ParentInstanceId": a9999ParentInstanceId}
)
