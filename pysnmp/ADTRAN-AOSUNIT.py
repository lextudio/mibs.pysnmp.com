# SNMP MIB module (ADTRAN-AOSUNIT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOSUNIT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:20 2024
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention")


# MODULE-IDENTITY

adGenAOSUnitMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 1)
)
adGenAOSUnitMib.setRevisions(
        ("2004-09-28 00:00",
         "2005-05-12 00:00",
         "2008-07-30 00:00",
         "2010-04-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Utf8String(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_AdGenAOSUnit_ObjectIdentity = ObjectIdentity
adGenAOSUnit = _AdGenAOSUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1)
)


class _AdAOSBootRevision_Type(DisplayString):
    """Custom type adAOSBootRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_AdAOSBootRevision_Type.__name__ = "DisplayString"
_AdAOSBootRevision_Object = MibScalar
adAOSBootRevision = _AdAOSBootRevision_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 1),
    _AdAOSBootRevision_Type()
)
adAOSBootRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSBootRevision.setStatus("current")


class _AdAOSCurrentImage_Type(DisplayString):
    """Custom type adAOSCurrentImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdAOSCurrentImage_Type.__name__ = "DisplayString"
_AdAOSCurrentImage_Object = MibScalar
adAOSCurrentImage = _AdAOSCurrentImage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 2),
    _AdAOSCurrentImage_Type()
)
adAOSCurrentImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSCurrentImage.setStatus("current")


class _AdAOSRunConfigChecksum_Type(DisplayString):
    """Custom type adAOSRunConfigChecksum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AdAOSRunConfigChecksum_Type.__name__ = "DisplayString"
_AdAOSRunConfigChecksum_Object = MibScalar
adAOSRunConfigChecksum = _AdAOSRunConfigChecksum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 3),
    _AdAOSRunConfigChecksum_Type()
)
adAOSRunConfigChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSRunConfigChecksum.setStatus("current")


class _AdAOSStartConfigChecksum_Type(DisplayString):
    """Custom type adAOSStartConfigChecksum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AdAOSStartConfigChecksum_Type.__name__ = "DisplayString"
_AdAOSStartConfigChecksum_Object = MibScalar
adAOSStartConfigChecksum = _AdAOSStartConfigChecksum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 4),
    _AdAOSStartConfigChecksum_Type()
)
adAOSStartConfigChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSStartConfigChecksum.setStatus("current")


class _AdAOSDeviceIndex_Type(Integer32):
    """Custom type adAOSDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdAOSDeviceIndex_Type.__name__ = "Integer32"
_AdAOSDeviceIndex_Object = MibScalar
adAOSDeviceIndex = _AdAOSDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 5),
    _AdAOSDeviceIndex_Type()
)
adAOSDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceIndex.setStatus("current")
_AdAOSDeviceGlobalUniqueID_Type = Utf8String
_AdAOSDeviceGlobalUniqueID_Object = MibScalar
adAOSDeviceGlobalUniqueID = _AdAOSDeviceGlobalUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 6),
    _AdAOSDeviceGlobalUniqueID_Type()
)
adAOSDeviceGlobalUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceGlobalUniqueID.setStatus("current")


class _AdAOSDeviceHealth_Type(Integer32):
    """Custom type adAOSDeviceHealth based on Integer32"""
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
        *(("critical", 5),
          ("nonrecoverable", 6),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_AdAOSDeviceHealth_Type.__name__ = "Integer32"
_AdAOSDeviceHealth_Object = MibScalar
adAOSDeviceHealth = _AdAOSDeviceHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 7),
    _AdAOSDeviceHealth_Type()
)
adAOSDeviceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceHealth.setStatus("current")
_AdAOSDeviceSysObjID_Type = Utf8String
_AdAOSDeviceSysObjID_Object = MibScalar
adAOSDeviceSysObjID = _AdAOSDeviceSysObjID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 8),
    _AdAOSDeviceSysObjID_Type()
)
adAOSDeviceSysObjID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceSysObjID.setStatus("current")
_AdAOSDeviceManagementURL_Type = Utf8String
_AdAOSDeviceManagementURL_Object = MibScalar
adAOSDeviceManagementURL = _AdAOSDeviceManagementURL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 9),
    _AdAOSDeviceManagementURL_Type()
)
adAOSDeviceManagementURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSDeviceManagementURL.setStatus("current")
_AdAOSDeviceManagementURLLabel_Type = Utf8String
_AdAOSDeviceManagementURLLabel_Object = MibScalar
adAOSDeviceManagementURLLabel = _AdAOSDeviceManagementURLLabel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 10),
    _AdAOSDeviceManagementURLLabel_Type()
)
adAOSDeviceManagementURLLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSDeviceManagementURLLabel.setStatus("current")
_AdAOSDeviceManufacturer_Type = Utf8String
_AdAOSDeviceManufacturer_Object = MibScalar
adAOSDeviceManufacturer = _AdAOSDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 11),
    _AdAOSDeviceManufacturer_Type()
)
adAOSDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceManufacturer.setStatus("current")
_AdAOSDeviceProductName_Type = Utf8String
_AdAOSDeviceProductName_Object = MibScalar
adAOSDeviceProductName = _AdAOSDeviceProductName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 12),
    _AdAOSDeviceProductName_Type()
)
adAOSDeviceProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceProductName.setStatus("current")
_AdAOSDeviceSerialNumber_Type = Utf8String
_AdAOSDeviceSerialNumber_Object = MibScalar
adAOSDeviceSerialNumber = _AdAOSDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 13),
    _AdAOSDeviceSerialNumber_Type()
)
adAOSDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceSerialNumber.setStatus("current")


class _AdAOSDeviceVersion_Type(Utf8String):
    """Custom type adAOSDeviceVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdAOSDeviceVersion_Type.__name__ = "Utf8String"
_AdAOSDeviceVersion_Object = MibScalar
adAOSDeviceVersion = _AdAOSDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 14),
    _AdAOSDeviceVersion_Type()
)
adAOSDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceVersion.setStatus("current")


class _AdAOSDeviceHWVersion_Type(Utf8String):
    """Custom type adAOSDeviceHWVersion based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdAOSDeviceHWVersion_Type.__name__ = "Utf8String"
_AdAOSDeviceHWVersion_Object = MibScalar
adAOSDeviceHWVersion = _AdAOSDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 15),
    _AdAOSDeviceHWVersion_Type()
)
adAOSDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDeviceHWVersion.setStatus("current")
_AdAOSDeviceContactPerson_Type = Utf8String
_AdAOSDeviceContactPerson_Object = MibScalar
adAOSDeviceContactPerson = _AdAOSDeviceContactPerson_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 16),
    _AdAOSDeviceContactPerson_Type()
)
adAOSDeviceContactPerson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSDeviceContactPerson.setStatus("current")


class _AdAOSDeviceContactPhone_Type(Utf8String):
    """Custom type adAOSDeviceContactPhone based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdAOSDeviceContactPhone_Type.__name__ = "Utf8String"
_AdAOSDeviceContactPhone_Object = MibScalar
adAOSDeviceContactPhone = _AdAOSDeviceContactPhone_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 17),
    _AdAOSDeviceContactPhone_Type()
)
adAOSDeviceContactPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSDeviceContactPhone.setStatus("current")
_AdAOSDeviceContactEmail_Type = Utf8String
_AdAOSDeviceContactEmail_Object = MibScalar
adAOSDeviceContactEmail = _AdAOSDeviceContactEmail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 18),
    _AdAOSDeviceContactEmail_Type()
)
adAOSDeviceContactEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSDeviceContactEmail.setStatus("current")


class _AdAOSDeviceContactPagerNumber_Type(Utf8String):
    """Custom type adAOSDeviceContactPagerNumber based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdAOSDeviceContactPagerNumber_Type.__name__ = "Utf8String"
_AdAOSDeviceContactPagerNumber_Object = MibScalar
adAOSDeviceContactPagerNumber = _AdAOSDeviceContactPagerNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 19),
    _AdAOSDeviceContactPagerNumber_Type()
)
adAOSDeviceContactPagerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSDeviceContactPagerNumber.setStatus("current")
_AdAOSDeviceLocation_Type = Utf8String
_AdAOSDeviceLocation_Object = MibScalar
adAOSDeviceLocation = _AdAOSDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 20),
    _AdAOSDeviceLocation_Type()
)
adAOSDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSDeviceLocation.setStatus("current")


class _AdGenAOSSaveConfig_Type(Integer32):
    """Custom type adGenAOSSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("saveconfig", 1)
    )


_AdGenAOSSaveConfig_Type.__name__ = "Integer32"
_AdGenAOSSaveConfig_Object = MibScalar
adGenAOSSaveConfig = _AdGenAOSSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 21),
    _AdGenAOSSaveConfig_Type()
)
adGenAOSSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSSaveConfig.setStatus("current")


class _AdGenAOSReloadSystem_Type(Integer32):
    """Custom type adGenAOSReloadSystem based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdGenAOSReloadSystem_Type.__name__ = "Integer32"
_AdGenAOSReloadSystem_Object = MibScalar
adGenAOSReloadSystem = _AdGenAOSReloadSystem_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 22),
    _AdGenAOSReloadSystem_Type()
)
adGenAOSReloadSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSReloadSystem.setStatus("current")


class _AdGenAOSCancelReload_Type(Integer32):
    """Custom type adGenAOSCancelReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancelreload", 1)
    )


_AdGenAOSCancelReload_Type.__name__ = "Integer32"
_AdGenAOSCancelReload_Object = MibScalar
adGenAOSCancelReload = _AdGenAOSCancelReload_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 23),
    _AdGenAOSCancelReload_Type()
)
adGenAOSCancelReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSCancelReload.setStatus("current")


class _AdAOSPrimaryImage_Type(DisplayString):
    """Custom type adAOSPrimaryImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdAOSPrimaryImage_Type.__name__ = "DisplayString"
_AdAOSPrimaryImage_Object = MibScalar
adAOSPrimaryImage = _AdAOSPrimaryImage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 24),
    _AdAOSPrimaryImage_Type()
)
adAOSPrimaryImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSPrimaryImage.setStatus("current")


class _AdAOSBackupImage_Type(DisplayString):
    """Custom type adAOSBackupImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdAOSBackupImage_Type.__name__ = "DisplayString"
_AdAOSBackupImage_Object = MibScalar
adAOSBackupImage = _AdAOSBackupImage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 25),
    _AdAOSBackupImage_Type()
)
adAOSBackupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSBackupImage.setStatus("current")
_AdAOSDevicePartNumber_Type = Utf8String
_AdAOSDevicePartNumber_Object = MibScalar
adAOSDevicePartNumber = _AdAOSDevicePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 26),
    _AdAOSDevicePartNumber_Type()
)
adAOSDevicePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adAOSDevicePartNumber.setStatus("current")
_AdGenAOSUnitConformance_ObjectIdentity = ObjectIdentity
adGenAOSUnitConformance = _AdGenAOSUnitConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1)
)
_AdAOSUnitCompliances_ObjectIdentity = ObjectIdentity
adAOSUnitCompliances = _AdAOSUnitCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 1)
)
_AdAOSUnitGroups_ObjectIdentity = ObjectIdentity
adAOSUnitGroups = _AdAOSUnitGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 2)
)

# Managed Objects groups

adGenAOSUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 2, 1)
)
adGenAOSUnitGroup.setObjects(
      *(("ADTRAN-AOSUNIT", "adAOSBootRevision"),
        ("ADTRAN-AOSUNIT", "adAOSCurrentImage"),
        ("ADTRAN-AOSUNIT", "adAOSRunConfigChecksum"),
        ("ADTRAN-AOSUNIT", "adAOSStartConfigChecksum"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceIndex"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceGlobalUniqueID"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceHealth"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceSysObjID"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceManagementURL"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceManufacturer"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceProductName"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceSerialNumber"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceVersion"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceHWVersion"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceContactPerson"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceContactPhone"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceContactEmail"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceContactPagerNumber"),
        ("ADTRAN-AOSUNIT", "adAOSDeviceLocation"),
        ("ADTRAN-AOSUNIT", "adGenAOSSaveConfig"),
        ("ADTRAN-AOSUNIT", "adGenAOSReloadSystem"),
        ("ADTRAN-AOSUNIT", "adGenAOSCancelReload"),
        ("ADTRAN-AOSUNIT", "adAOSPrimaryImage"),
        ("ADTRAN-AOSUNIT", "adAOSBackupImage"),
        ("ADTRAN-AOSUNIT", "adAOSDevicePartNumber"))
)
if mibBuilder.loadTexts:
    adGenAOSUnitGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adAOSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adAOSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOSUNIT",
    **{"Utf8String": Utf8String,
       "adGenAOSUnit": adGenAOSUnit,
       "adAOSBootRevision": adAOSBootRevision,
       "adAOSCurrentImage": adAOSCurrentImage,
       "adAOSRunConfigChecksum": adAOSRunConfigChecksum,
       "adAOSStartConfigChecksum": adAOSStartConfigChecksum,
       "adAOSDeviceIndex": adAOSDeviceIndex,
       "adAOSDeviceGlobalUniqueID": adAOSDeviceGlobalUniqueID,
       "adAOSDeviceHealth": adAOSDeviceHealth,
       "adAOSDeviceSysObjID": adAOSDeviceSysObjID,
       "adAOSDeviceManagementURL": adAOSDeviceManagementURL,
       "adAOSDeviceManagementURLLabel": adAOSDeviceManagementURLLabel,
       "adAOSDeviceManufacturer": adAOSDeviceManufacturer,
       "adAOSDeviceProductName": adAOSDeviceProductName,
       "adAOSDeviceSerialNumber": adAOSDeviceSerialNumber,
       "adAOSDeviceVersion": adAOSDeviceVersion,
       "adAOSDeviceHWVersion": adAOSDeviceHWVersion,
       "adAOSDeviceContactPerson": adAOSDeviceContactPerson,
       "adAOSDeviceContactPhone": adAOSDeviceContactPhone,
       "adAOSDeviceContactEmail": adAOSDeviceContactEmail,
       "adAOSDeviceContactPagerNumber": adAOSDeviceContactPagerNumber,
       "adAOSDeviceLocation": adAOSDeviceLocation,
       "adGenAOSSaveConfig": adGenAOSSaveConfig,
       "adGenAOSReloadSystem": adGenAOSReloadSystem,
       "adGenAOSCancelReload": adGenAOSCancelReload,
       "adAOSPrimaryImage": adAOSPrimaryImage,
       "adAOSBackupImage": adAOSBackupImage,
       "adAOSDevicePartNumber": adAOSDevicePartNumber,
       "adGenAOSUnitConformance": adGenAOSUnitConformance,
       "adAOSUnitCompliances": adAOSUnitCompliances,
       "adAOSCompliance": adAOSCompliance,
       "adAOSUnitGroups": adAOSUnitGroups,
       "adGenAOSUnitGroup": adGenAOSUnitGroup,
       "adGenAOSUnitMib": adGenAOSUnitMib}
)
