# SNMP MIB module (CISCO-LICENSE-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LICENSE-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:01 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

ciscoLicenseMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369)
)
ciscoLicenseMgrMIB.setRevisions(
        ("2004-07-20 00:00",
         "2003-11-27 00:00",
         "2003-10-30 00:00",
         "2003-09-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLicenseMgrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrMIBObjects = _CiscoLicenseMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1)
)
_CiscoLicenseMgrConfig_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrConfig = _CiscoLicenseMgrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 1)
)


class _ClmHostId_Type(SnmpAdminString):
    """Custom type clmHostId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_ClmHostId_Type.__name__ = "SnmpAdminString"
_ClmHostId_Object = MibScalar
clmHostId = _ClmHostId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 1, 1),
    _ClmHostId_Type()
)
clmHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmHostId.setStatus("current")


class _ClmNotificationsEnable_Type(TruthValue):
    """Custom type clmNotificationsEnable based on TruthValue"""


_ClmNotificationsEnable_Object = MibScalar
clmNotificationsEnable = _ClmNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 1, 2),
    _ClmNotificationsEnable_Type()
)
clmNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmNotificationsEnable.setStatus("current")
_ClmLicenseConfiguration_ObjectIdentity = ObjectIdentity
clmLicenseConfiguration = _ClmLicenseConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2)
)
_ClmLicenseConfigSpinLock_Type = TestAndIncr
_ClmLicenseConfigSpinLock_Object = MibScalar
clmLicenseConfigSpinLock = _ClmLicenseConfigSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 1),
    _ClmLicenseConfigSpinLock_Type()
)
clmLicenseConfigSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseConfigSpinLock.setStatus("current")


class _ClmLicenseFileURI_Type(SnmpAdminString):
    """Custom type clmLicenseFileURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmLicenseFileURI_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileURI_Object = MibScalar
clmLicenseFileURI = _ClmLicenseFileURI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 2),
    _ClmLicenseFileURI_Type()
)
clmLicenseFileURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseFileURI.setStatus("current")


class _ClmLicenseFileTargetName_Type(SnmpAdminString):
    """Custom type clmLicenseFileTargetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClmLicenseFileTargetName_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileTargetName_Object = MibScalar
clmLicenseFileTargetName = _ClmLicenseFileTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 3),
    _ClmLicenseFileTargetName_Type()
)
clmLicenseFileTargetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseFileTargetName.setStatus("current")


class _ClmLicenseConfigCommand_Type(Integer32):
    """Custom type clmLicenseConfigCommand based on Integer32"""
    defaultValue = 3

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
        *(("install", 1),
          ("noOp", 3),
          ("uninstall", 2),
          ("update", 4))
    )


_ClmLicenseConfigCommand_Type.__name__ = "Integer32"
_ClmLicenseConfigCommand_Object = MibScalar
clmLicenseConfigCommand = _ClmLicenseConfigCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 4),
    _ClmLicenseConfigCommand_Type()
)
clmLicenseConfigCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseConfigCommand.setStatus("current")


class _ClmLicenseConfigCommandStatus_Type(Integer32):
    """Custom type clmLicenseConfigCommandStatus based on Integer32"""
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("corruptedLicenseFile", 3),
          ("duplicateLicense", 6),
          ("generalLicensingFailure", 8),
          ("inProgress", 2),
          ("invalidLicenseCount", 11),
          ("invalidLicenseFileExtension", 16),
          ("invalidLicenseFileName", 5),
          ("invalidPlatform", 19),
          ("invalidURI", 17),
          ("licenseExpiryConflict", 10),
          ("licenseFileMissing", 15),
          ("licenseFileNotFound", 14),
          ("licenseInGraceMore", 13),
          ("licenseInUse", 7),
          ("noDemoLicenseSupport", 18),
          ("none", 9),
          ("notThisHost", 12),
          ("success", 1),
          ("targetLicenseFileAlreadyExist", 4))
    )


_ClmLicenseConfigCommandStatus_Type.__name__ = "Integer32"
_ClmLicenseConfigCommandStatus_Object = MibScalar
clmLicenseConfigCommandStatus = _ClmLicenseConfigCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 5),
    _ClmLicenseConfigCommandStatus_Type()
)
clmLicenseConfigCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseConfigCommandStatus.setStatus("current")
_ClmLicenseRequestSpinLock_Type = TestAndIncr
_ClmLicenseRequestSpinLock_Object = MibScalar
clmLicenseRequestSpinLock = _ClmLicenseRequestSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 6),
    _ClmLicenseRequestSpinLock_Type()
)
clmLicenseRequestSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestSpinLock.setStatus("current")


class _ClmLicenseRequestFeatureName_Type(SnmpAdminString):
    """Custom type clmLicenseRequestFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ClmLicenseRequestFeatureName_Type.__name__ = "SnmpAdminString"
_ClmLicenseRequestFeatureName_Object = MibScalar
clmLicenseRequestFeatureName = _ClmLicenseRequestFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 7),
    _ClmLicenseRequestFeatureName_Type()
)
clmLicenseRequestFeatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestFeatureName.setStatus("current")


class _ClmLicenseRequestAppName_Type(SnmpAdminString):
    """Custom type clmLicenseRequestAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClmLicenseRequestAppName_Type.__name__ = "SnmpAdminString"
_ClmLicenseRequestAppName_Object = MibScalar
clmLicenseRequestAppName = _ClmLicenseRequestAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 8),
    _ClmLicenseRequestAppName_Type()
)
clmLicenseRequestAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestAppName.setStatus("current")


class _ClmLicenseRequestCommand_Type(Integer32):
    """Custom type clmLicenseRequestCommand based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checkIn", 1),
          ("checkOut", 2),
          ("noOp", 3))
    )


_ClmLicenseRequestCommand_Type.__name__ = "Integer32"
_ClmLicenseRequestCommand_Object = MibScalar
clmLicenseRequestCommand = _ClmLicenseRequestCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 9),
    _ClmLicenseRequestCommand_Type()
)
clmLicenseRequestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestCommand.setStatus("current")


class _ClmLicenseRequestCommandStatus_Type(Integer32):
    """Custom type clmLicenseRequestCommandStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("generalLicensingFailure", 5),
          ("invalidFeature", 6),
          ("licenseDenied", 3),
          ("licenseExpired", 7),
          ("licenseServerDown", 8),
          ("licenseTooMany", 4),
          ("none", 2),
          ("success", 1))
    )


_ClmLicenseRequestCommandStatus_Type.__name__ = "Integer32"
_ClmLicenseRequestCommandStatus_Object = MibScalar
clmLicenseRequestCommandStatus = _ClmLicenseRequestCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 10),
    _ClmLicenseRequestCommandStatus_Type()
)
clmLicenseRequestCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseRequestCommandStatus.setStatus("current")
_ClmLicenseInformation_ObjectIdentity = ObjectIdentity
clmLicenseInformation = _ClmLicenseInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3)
)


class _ClmNoOfLicenseFilesInstalled_Type(Integer32):
    """Custom type clmNoOfLicenseFilesInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ClmNoOfLicenseFilesInstalled_Type.__name__ = "Integer32"
_ClmNoOfLicenseFilesInstalled_Object = MibScalar
clmNoOfLicenseFilesInstalled = _ClmNoOfLicenseFilesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 1),
    _ClmNoOfLicenseFilesInstalled_Type()
)
clmNoOfLicenseFilesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicenseFilesInstalled.setStatus("current")
_ClmLicenseFileContentsTable_Object = MibTable
clmLicenseFileContentsTable = _ClmLicenseFileContentsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2)
)
if mibBuilder.loadTexts:
    clmLicenseFileContentsTable.setStatus("current")
_ClmLicenseFileContentsEntry_Object = MibTableRow
clmLicenseFileContentsEntry = _ClmLicenseFileContentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1)
)
clmLicenseFileContentsEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFileName"),
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowNumber"),
)
if mibBuilder.loadTexts:
    clmLicenseFileContentsEntry.setStatus("current")


class _ClmLicenseFileName_Type(SnmpAdminString):
    """Custom type clmLicenseFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ClmLicenseFileName_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileName_Object = MibTableColumn
clmLicenseFileName = _ClmLicenseFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 1),
    _ClmLicenseFileName_Type()
)
clmLicenseFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicenseFileName.setStatus("current")
_ClmLicenseFileRowNumber_Type = Unsigned32
_ClmLicenseFileRowNumber_Object = MibTableColumn
clmLicenseFileRowNumber = _ClmLicenseFileRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 2),
    _ClmLicenseFileRowNumber_Type()
)
clmLicenseFileRowNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicenseFileRowNumber.setStatus("current")
_ClmLicenseFileTimeStamp_Type = DateAndTime
_ClmLicenseFileTimeStamp_Object = MibTableColumn
clmLicenseFileTimeStamp = _ClmLicenseFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 3),
    _ClmLicenseFileTimeStamp_Type()
)
clmLicenseFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFileTimeStamp.setStatus("current")
_ClmLicenseFileNoOfRows_Type = Unsigned32
_ClmLicenseFileNoOfRows_Object = MibTableColumn
clmLicenseFileNoOfRows = _ClmLicenseFileNoOfRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 4),
    _ClmLicenseFileNoOfRows_Type()
)
clmLicenseFileNoOfRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFileNoOfRows.setStatus("current")


class _ClmLicenseFileRowContents_Type(SnmpAdminString):
    """Custom type clmLicenseFileRowContents based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClmLicenseFileRowContents_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileRowContents_Object = MibTableColumn
clmLicenseFileRowContents = _ClmLicenseFileRowContents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 5),
    _ClmLicenseFileRowContents_Type()
)
clmLicenseFileRowContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFileRowContents.setStatus("current")


class _ClmNoOfLicensedFeatures_Type(Integer32):
    """Custom type clmNoOfLicensedFeatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ClmNoOfLicensedFeatures_Type.__name__ = "Integer32"
_ClmNoOfLicensedFeatures_Object = MibScalar
clmNoOfLicensedFeatures = _ClmNoOfLicensedFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 3),
    _ClmNoOfLicensedFeatures_Type()
)
clmNoOfLicensedFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicensedFeatures.setStatus("current")
_ClmLicenseFeatureUsageTable_Object = MibTable
clmLicenseFeatureUsageTable = _ClmLicenseFeatureUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4)
)
if mibBuilder.loadTexts:
    clmLicenseFeatureUsageTable.setStatus("current")
_ClmLicenseFeatureUsageEntry_Object = MibTableRow
clmLicenseFeatureUsageEntry = _ClmLicenseFeatureUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1)
)
clmLicenseFeatureUsageEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFeatureName"),
)
if mibBuilder.loadTexts:
    clmLicenseFeatureUsageEntry.setStatus("current")


class _ClmLicenseFeatureName_Type(SnmpAdminString):
    """Custom type clmLicenseFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ClmLicenseFeatureName_Type.__name__ = "SnmpAdminString"
_ClmLicenseFeatureName_Object = MibTableColumn
clmLicenseFeatureName = _ClmLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 1),
    _ClmLicenseFeatureName_Type()
)
clmLicenseFeatureName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicenseFeatureName.setStatus("current")


class _ClmLicenseFlag_Type(Bits):
    """Custom type clmLicenseFlag based on Bits"""
    namedValues = NamedValues(
        *(("counted", 2),
          ("demo", 0),
          ("inGracePeriod", 4),
          ("permanent", 1),
          ("unlicensed", 3))
    )

_ClmLicenseFlag_Type.__name__ = "Bits"
_ClmLicenseFlag_Object = MibTableColumn
clmLicenseFlag = _ClmLicenseFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 2),
    _ClmLicenseFlag_Type()
)
clmLicenseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFlag.setStatus("current")


class _ClmNoOfLicenseMaxUsages_Type(Integer32):
    """Custom type clmNoOfLicenseMaxUsages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClmNoOfLicenseMaxUsages_Type.__name__ = "Integer32"
_ClmNoOfLicenseMaxUsages_Object = MibTableColumn
clmNoOfLicenseMaxUsages = _ClmNoOfLicenseMaxUsages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 3),
    _ClmNoOfLicenseMaxUsages_Type()
)
clmNoOfLicenseMaxUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicenseMaxUsages.setStatus("current")


class _ClmNoOfMissingUsageLicenses_Type(Integer32):
    """Custom type clmNoOfMissingUsageLicenses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClmNoOfMissingUsageLicenses_Type.__name__ = "Integer32"
_ClmNoOfMissingUsageLicenses_Object = MibTableColumn
clmNoOfMissingUsageLicenses = _ClmNoOfMissingUsageLicenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 4),
    _ClmNoOfMissingUsageLicenses_Type()
)
clmNoOfMissingUsageLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfMissingUsageLicenses.setStatus("current")


class _ClmNoOfLicenseCurrentUsages_Type(Integer32):
    """Custom type clmNoOfLicenseCurrentUsages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClmNoOfLicenseCurrentUsages_Type.__name__ = "Integer32"
_ClmNoOfLicenseCurrentUsages_Object = MibTableColumn
clmNoOfLicenseCurrentUsages = _ClmNoOfLicenseCurrentUsages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 5),
    _ClmNoOfLicenseCurrentUsages_Type()
)
clmNoOfLicenseCurrentUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicenseCurrentUsages.setStatus("current")
_ClmLicenseExpiryDate_Type = DateAndTime
_ClmLicenseExpiryDate_Object = MibTableColumn
clmLicenseExpiryDate = _ClmLicenseExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 6),
    _ClmLicenseExpiryDate_Type()
)
clmLicenseExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseExpiryDate.setStatus("current")


class _ClmLicenseGracePeriod_Type(Integer32):
    """Custom type clmLicenseGracePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5184000),
    )


_ClmLicenseGracePeriod_Type.__name__ = "Integer32"
_ClmLicenseGracePeriod_Object = MibTableColumn
clmLicenseGracePeriod = _ClmLicenseGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 7),
    _ClmLicenseGracePeriod_Type()
)
clmLicenseGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    clmLicenseGracePeriod.setUnits("seconds")
_ClmFeatureUsageDetailsTable_Object = MibTable
clmFeatureUsageDetailsTable = _ClmFeatureUsageDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5)
)
if mibBuilder.loadTexts:
    clmFeatureUsageDetailsTable.setStatus("current")
_ClmFeatureUsageDetailsEntry_Object = MibTableRow
clmFeatureUsageDetailsEntry = _ClmFeatureUsageDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5, 1)
)
clmFeatureUsageDetailsEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFeatureName"),
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicensedAppIndex"),
)
if mibBuilder.loadTexts:
    clmFeatureUsageDetailsEntry.setStatus("current")
_ClmLicensedAppIndex_Type = Unsigned32
_ClmLicensedAppIndex_Object = MibTableColumn
clmLicensedAppIndex = _ClmLicensedAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5, 1, 1),
    _ClmLicensedAppIndex_Type()
)
clmLicensedAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicensedAppIndex.setStatus("current")


class _ClmLicensedAppName_Type(SnmpAdminString):
    """Custom type clmLicensedAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ClmLicensedAppName_Type.__name__ = "SnmpAdminString"
_ClmLicensedAppName_Object = MibTableColumn
clmLicensedAppName = _ClmLicensedAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5, 1, 2),
    _ClmLicensedAppName_Type()
)
clmLicensedAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicensedAppName.setStatus("current")
_ClmLicenseViolationWarnFlag_Type = TruthValue
_ClmLicenseViolationWarnFlag_Object = MibScalar
clmLicenseViolationWarnFlag = _ClmLicenseViolationWarnFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 6),
    _ClmLicenseViolationWarnFlag_Type()
)
clmLicenseViolationWarnFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseViolationWarnFlag.setStatus("current")
_CiscoLicenseMgrMIBConform_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrMIBConform = _CiscoLicenseMgrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2)
)
_CiscoLicenseMgrCompliances_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrCompliances = _CiscoLicenseMgrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1)
)
_CiscoLicenseMgrGroups_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrGroups = _CiscoLicenseMgrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2)
)
_CiscoLicenseMgrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrMIBNotifs = _CiscoLicenseMgrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3)
)
_CiscoLicenseMgrNotifications_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrNotifications = _CiscoLicenseMgrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0)
)

# Managed Objects groups

clmLicenseInstallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 1)
)
clmLicenseInstallGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmHostId"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseConfigSpinLock"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileURI"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTargetName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseConfigCommand"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseConfigCommandStatus"))
)
if mibBuilder.loadTexts:
    clmLicenseInstallGroup.setStatus("current")

clmNoOfInstalledLicensesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 2)
)
clmNoOfInstalledLicensesGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseFilesInstalled"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicensedFeatures"))
)
if mibBuilder.loadTexts:
    clmNoOfInstalledLicensesGroup.setStatus("current")

clmLicenseInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 3)
)
clmLicenseInformationGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTimeStamp"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileNoOfRows"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowContents"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFlag"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseMaxUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseCurrentUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriod"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroup.setStatus("deprecated")

clmNotificationsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 4)
)
clmNotificationsEnableGroup.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnable")
)
if mibBuilder.loadTexts:
    clmNotificationsEnableGroup.setStatus("current")

clmLicenseRequestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 6)
)
clmLicenseRequestGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestSpinLock"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestFeatureName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestAppName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestCommand"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestCommandStatus"))
)
if mibBuilder.loadTexts:
    clmLicenseRequestGroup.setStatus("current")

clmLicenseInformationGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 7)
)
clmLicenseInformationGroup1.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTimeStamp"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileNoOfRows"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowContents"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFlag"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseMaxUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseCurrentUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriod"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicensedAppName"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroup1.setStatus("deprecated")

clmLicenseInformationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 8)
)
clmLicenseInformationGroup2.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTimeStamp"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileNoOfRows"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowContents"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFlag"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseMaxUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseCurrentUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriod"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicensedAppName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseViolationWarnFlag"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroup2.setStatus("current")


# Notification objects

clmLicenseExpiryNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 1)
)
clmLicenseExpiryNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate")
)
if mibBuilder.loadTexts:
    clmLicenseExpiryNotify.setStatus(
        "current"
    )

clmNoLicenseForFeatureNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 2)
)
clmNoLicenseForFeatureNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriod")
)
if mibBuilder.loadTexts:
    clmNoLicenseForFeatureNotify.setStatus(
        "current"
    )

clmLicenseFileMissingNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 3)
)
clmLicenseFileMissingNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses")
)
if mibBuilder.loadTexts:
    clmLicenseFileMissingNotify.setStatus(
        "current"
    )

clmLicenseExpiryWarningNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 4)
)
clmLicenseExpiryWarningNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate")
)
if mibBuilder.loadTexts:
    clmLicenseExpiryWarningNotify.setStatus(
        "current"
    )


# Notifications groups

clmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 5)
)
clmNotificationGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryNotify"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoLicenseForFeatureNotify"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileMissingNotify"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryWarningNotify"))
)
if mibBuilder.loadTexts:
    clmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLicenseMgrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance.setStatus(
        "deprecated"
    )

ciscoLicenseMgrCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance1.setStatus(
        "deprecated"
    )

ciscoLicenseMgrCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LICENSE-MGR-MIB",
    **{"ciscoLicenseMgrMIB": ciscoLicenseMgrMIB,
       "ciscoLicenseMgrMIBObjects": ciscoLicenseMgrMIBObjects,
       "ciscoLicenseMgrConfig": ciscoLicenseMgrConfig,
       "clmHostId": clmHostId,
       "clmNotificationsEnable": clmNotificationsEnable,
       "clmLicenseConfiguration": clmLicenseConfiguration,
       "clmLicenseConfigSpinLock": clmLicenseConfigSpinLock,
       "clmLicenseFileURI": clmLicenseFileURI,
       "clmLicenseFileTargetName": clmLicenseFileTargetName,
       "clmLicenseConfigCommand": clmLicenseConfigCommand,
       "clmLicenseConfigCommandStatus": clmLicenseConfigCommandStatus,
       "clmLicenseRequestSpinLock": clmLicenseRequestSpinLock,
       "clmLicenseRequestFeatureName": clmLicenseRequestFeatureName,
       "clmLicenseRequestAppName": clmLicenseRequestAppName,
       "clmLicenseRequestCommand": clmLicenseRequestCommand,
       "clmLicenseRequestCommandStatus": clmLicenseRequestCommandStatus,
       "clmLicenseInformation": clmLicenseInformation,
       "clmNoOfLicenseFilesInstalled": clmNoOfLicenseFilesInstalled,
       "clmLicenseFileContentsTable": clmLicenseFileContentsTable,
       "clmLicenseFileContentsEntry": clmLicenseFileContentsEntry,
       "clmLicenseFileName": clmLicenseFileName,
       "clmLicenseFileRowNumber": clmLicenseFileRowNumber,
       "clmLicenseFileTimeStamp": clmLicenseFileTimeStamp,
       "clmLicenseFileNoOfRows": clmLicenseFileNoOfRows,
       "clmLicenseFileRowContents": clmLicenseFileRowContents,
       "clmNoOfLicensedFeatures": clmNoOfLicensedFeatures,
       "clmLicenseFeatureUsageTable": clmLicenseFeatureUsageTable,
       "clmLicenseFeatureUsageEntry": clmLicenseFeatureUsageEntry,
       "clmLicenseFeatureName": clmLicenseFeatureName,
       "clmLicenseFlag": clmLicenseFlag,
       "clmNoOfLicenseMaxUsages": clmNoOfLicenseMaxUsages,
       "clmNoOfMissingUsageLicenses": clmNoOfMissingUsageLicenses,
       "clmNoOfLicenseCurrentUsages": clmNoOfLicenseCurrentUsages,
       "clmLicenseExpiryDate": clmLicenseExpiryDate,
       "clmLicenseGracePeriod": clmLicenseGracePeriod,
       "clmFeatureUsageDetailsTable": clmFeatureUsageDetailsTable,
       "clmFeatureUsageDetailsEntry": clmFeatureUsageDetailsEntry,
       "clmLicensedAppIndex": clmLicensedAppIndex,
       "clmLicensedAppName": clmLicensedAppName,
       "clmLicenseViolationWarnFlag": clmLicenseViolationWarnFlag,
       "ciscoLicenseMgrMIBConform": ciscoLicenseMgrMIBConform,
       "ciscoLicenseMgrCompliances": ciscoLicenseMgrCompliances,
       "ciscoLicenseMgrCompliance": ciscoLicenseMgrCompliance,
       "ciscoLicenseMgrCompliance1": ciscoLicenseMgrCompliance1,
       "ciscoLicenseMgrCompliance2": ciscoLicenseMgrCompliance2,
       "ciscoLicenseMgrGroups": ciscoLicenseMgrGroups,
       "clmLicenseInstallGroup": clmLicenseInstallGroup,
       "clmNoOfInstalledLicensesGroup": clmNoOfInstalledLicensesGroup,
       "clmLicenseInformationGroup": clmLicenseInformationGroup,
       "clmNotificationsEnableGroup": clmNotificationsEnableGroup,
       "clmNotificationGroup": clmNotificationGroup,
       "clmLicenseRequestGroup": clmLicenseRequestGroup,
       "clmLicenseInformationGroup1": clmLicenseInformationGroup1,
       "clmLicenseInformationGroup2": clmLicenseInformationGroup2,
       "ciscoLicenseMgrMIBNotifs": ciscoLicenseMgrMIBNotifs,
       "ciscoLicenseMgrNotifications": ciscoLicenseMgrNotifications,
       "clmLicenseExpiryNotify": clmLicenseExpiryNotify,
       "clmNoLicenseForFeatureNotify": clmNoLicenseForFeatureNotify,
       "clmLicenseFileMissingNotify": clmLicenseFileMissingNotify,
       "clmLicenseExpiryWarningNotify": clmLicenseExpiryWarningNotify}
)
