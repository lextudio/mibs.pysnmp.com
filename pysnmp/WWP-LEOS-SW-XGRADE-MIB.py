# SNMP MIB module (WWP-LEOS-SW-XGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-SW-XGRADE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:09 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosSwXgradeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10)
)
wwpLeosSwXgradeMIB.setRevisions(
        ("2012-06-27 00:00",
         "2011-08-01 00:00",
         "2011-07-07 00:01",
         "2011-07-07 00:00",
         "2003-04-21 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SwDownloadState(Integer32, TextualConvention):
    status = "current"
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
        *(("downloadComplete", 3),
          ("downloadFailed", 4),
          ("downloading", 2),
          ("idle", 1))
    )



class SwDownloadFailCause(Integer32, TextualConvention):
    status = "current"
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("alreadyUpgradeMode", 9),
          ("badFileCrc", 8),
          ("cmdFileParseError", 4),
          ("couldNotGetFile", 2),
          ("downloadSuccess", 0),
          ("flashOffline", 6),
          ("internalFilesystemError", 5),
          ("invalidPkgFile", 1),
          ("noStatus", 7),
          ("tftpServerNotFound", 3),
          ("unknownError", 10))
    )



class SwXgradeOp(Integer32, TextualConvention):
    status = "current"
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cancelDownload", 9),
          ("download", 8),
          ("inServiceActivate", 2),
          ("inServiceXgrade", 4),
          ("install", 1),
          ("none", 0),
          ("servAffectingXgradeReport", 6),
          ("servNonAffectingXgradeReport", 7),
          ("serviceAffectingActivate", 3),
          ("serviceAffectingXgrade", 5))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosSwXgradeMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosSwXgradeMIBObjects = _WwpLeosSwXgradeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1)
)
_WwpLeosSwXgrade_ObjectIdentity = ObjectIdentity
wwpLeosSwXgrade = _WwpLeosSwXgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1)
)
_WwpLeosSwDownload_ObjectIdentity = ObjectIdentity
wwpLeosSwDownload = _WwpLeosSwDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1)
)


class _WwpLeosSwDownloadServerAddrType_Type(AddressFamilyNumbers):
    """Custom type wwpLeosSwDownloadServerAddrType based on AddressFamilyNumbers"""
    defaultValue = 0


_WwpLeosSwDownloadServerAddrType_Object = MibScalar
wwpLeosSwDownloadServerAddrType = _WwpLeosSwDownloadServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 1),
    _WwpLeosSwDownloadServerAddrType_Type()
)
wwpLeosSwDownloadServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwDownloadServerAddrType.setStatus("deprecated")
_WwpLeosSwDownloadServerAddr_Type = DisplayString
_WwpLeosSwDownloadServerAddr_Object = MibScalar
wwpLeosSwDownloadServerAddr = _WwpLeosSwDownloadServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 2),
    _WwpLeosSwDownloadServerAddr_Type()
)
wwpLeosSwDownloadServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwDownloadServerAddr.setStatus("deprecated")


class _WwpLeosSwDownloadPackageName_Type(DisplayString):
    """Custom type wwpLeosSwDownloadPackageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosSwDownloadPackageName_Type.__name__ = "DisplayString"
_WwpLeosSwDownloadPackageName_Object = MibScalar
wwpLeosSwDownloadPackageName = _WwpLeosSwDownloadPackageName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 3),
    _WwpLeosSwDownloadPackageName_Type()
)
wwpLeosSwDownloadPackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwDownloadPackageName.setStatus("deprecated")


class _WwpLeosSwDownLoadActivate_Type(TruthValue):
    """Custom type wwpLeosSwDownLoadActivate based on TruthValue"""


_WwpLeosSwDownLoadActivate_Object = MibScalar
wwpLeosSwDownLoadActivate = _WwpLeosSwDownLoadActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 4),
    _WwpLeosSwDownLoadActivate_Type()
)
wwpLeosSwDownLoadActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwDownLoadActivate.setStatus("deprecated")


class _WwpLeosSwDownloadNotifOnCompletion_Type(TruthValue):
    """Custom type wwpLeosSwDownloadNotifOnCompletion based on TruthValue"""


_WwpLeosSwDownloadNotifOnCompletion_Object = MibScalar
wwpLeosSwDownloadNotifOnCompletion = _WwpLeosSwDownloadNotifOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 5),
    _WwpLeosSwDownloadNotifOnCompletion_Type()
)
wwpLeosSwDownloadNotifOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwDownloadNotifOnCompletion.setStatus("deprecated")
_WwpLeosSwDownloadStatus_Type = SwDownloadState
_WwpLeosSwDownloadStatus_Object = MibScalar
wwpLeosSwDownloadStatus = _WwpLeosSwDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 6),
    _WwpLeosSwDownloadStatus_Type()
)
wwpLeosSwDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSwDownloadStatus.setStatus("deprecated")
_WwpLeosSwDownloadFailCause_Type = SwDownloadFailCause
_WwpLeosSwDownloadFailCause_Object = MibScalar
wwpLeosSwDownloadFailCause = _WwpLeosSwDownloadFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 7),
    _WwpLeosSwDownloadFailCause_Type()
)
wwpLeosSwDownloadFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSwDownloadFailCause.setStatus("deprecated")


class _WwpLeosSwDownloadNotificationInfo_Type(DisplayString):
    """Custom type wwpLeosSwDownloadNotificationInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpLeosSwDownloadNotificationInfo_Type.__name__ = "DisplayString"
_WwpLeosSwDownloadNotificationInfo_Object = MibScalar
wwpLeosSwDownloadNotificationInfo = _WwpLeosSwDownloadNotificationInfo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 1, 8),
    _WwpLeosSwDownloadNotificationInfo_Type()
)
wwpLeosSwDownloadNotificationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSwDownloadNotificationInfo.setStatus("deprecated")
_WwpLeosSwXgradeBladeTable_Object = MibTable
wwpLeosSwXgradeBladeTable = _WwpLeosSwXgradeBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosSwXgradeBladeTable.setStatus("current")
_WwpLeosSwXgradeBladeEntry_Object = MibTableRow
wwpLeosSwXgradeBladeEntry = _WwpLeosSwXgradeBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1)
)
wwpLeosSwXgradeBladeEntry.setIndexNames(
    (0, "WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeBladeId"),
)
if mibBuilder.loadTexts:
    wwpLeosSwXgradeBladeEntry.setStatus("current")


class _WwpLeosSwXgradeBladeId_Type(Integer32):
    """Custom type wwpLeosSwXgradeBladeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosSwXgradeBladeId_Type.__name__ = "Integer32"
_WwpLeosSwXgradeBladeId_Object = MibTableColumn
wwpLeosSwXgradeBladeId = _WwpLeosSwXgradeBladeId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 1),
    _WwpLeosSwXgradeBladeId_Type()
)
wwpLeosSwXgradeBladeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeBladeId.setStatus("current")


class _WwpLeosSwXgradePackage_Type(DisplayString):
    """Custom type wwpLeosSwXgradePackage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosSwXgradePackage_Type.__name__ = "DisplayString"
_WwpLeosSwXgradePackage_Object = MibTableColumn
wwpLeosSwXgradePackage = _WwpLeosSwXgradePackage_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 2),
    _WwpLeosSwXgradePackage_Type()
)
wwpLeosSwXgradePackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradePackage.setStatus("current")
_WwpLeosSwXgradeOp_Type = SwXgradeOp
_WwpLeosSwXgradeOp_Object = MibTableColumn
wwpLeosSwXgradeOp = _WwpLeosSwXgradeOp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 3),
    _WwpLeosSwXgradeOp_Type()
)
wwpLeosSwXgradeOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeOp.setStatus("current")


class _WwpLeosSwXgradeTftpAddrType_Type(AddressFamilyNumbers):
    """Custom type wwpLeosSwXgradeTftpAddrType based on AddressFamilyNumbers"""
    defaultValue = 0


_WwpLeosSwXgradeTftpAddrType_Object = MibTableColumn
wwpLeosSwXgradeTftpAddrType = _WwpLeosSwXgradeTftpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 4),
    _WwpLeosSwXgradeTftpAddrType_Type()
)
wwpLeosSwXgradeTftpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeTftpAddrType.setStatus("current")
_WwpLeosSwXgradeTftpAddr_Type = DisplayString
_WwpLeosSwXgradeTftpAddr_Object = MibTableColumn
wwpLeosSwXgradeTftpAddr = _WwpLeosSwXgradeTftpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 5),
    _WwpLeosSwXgradeTftpAddr_Type()
)
wwpLeosSwXgradeTftpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeTftpAddr.setStatus("current")
_WwpLeosSwXgradeOpActivate_Type = TruthValue
_WwpLeosSwXgradeOpActivate_Object = MibTableColumn
wwpLeosSwXgradeOpActivate = _WwpLeosSwXgradeOpActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 6),
    _WwpLeosSwXgradeOpActivate_Type()
)
wwpLeosSwXgradeOpActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeOpActivate.setStatus("current")


class _WwpLeosSwXgradeOpStatus_Type(Integer32):
    """Custom type wwpLeosSwXgradeOpStatus based on Integer32"""
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
        *(("failure", 4),
          ("none", 1),
          ("processing", 2),
          ("success", 3))
    )


_WwpLeosSwXgradeOpStatus_Type.__name__ = "Integer32"
_WwpLeosSwXgradeOpStatus_Object = MibTableColumn
wwpLeosSwXgradeOpStatus = _WwpLeosSwXgradeOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 7),
    _WwpLeosSwXgradeOpStatus_Type()
)
wwpLeosSwXgradeOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeOpStatus.setStatus("current")
_WwpLeosSwXgradePackagePath_Type = DisplayString
_WwpLeosSwXgradePackagePath_Object = MibTableColumn
wwpLeosSwXgradePackagePath = _WwpLeosSwXgradePackagePath_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 8),
    _WwpLeosSwXgradePackagePath_Type()
)
wwpLeosSwXgradePackagePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradePackagePath.setStatus("current")


class _WwpLeosSwXgradeTransferMode_Type(Integer32):
    """Custom type wwpLeosSwXgradeTransferMode based on Integer32"""
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
        *(("default", 7),
          ("defaultFtp", 5),
          ("defaultSftp", 6),
          ("defaultTftp", 4),
          ("ftp", 2),
          ("sftp", 3),
          ("tftp", 1))
    )


_WwpLeosSwXgradeTransferMode_Type.__name__ = "Integer32"
_WwpLeosSwXgradeTransferMode_Object = MibTableColumn
wwpLeosSwXgradeTransferMode = _WwpLeosSwXgradeTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 9),
    _WwpLeosSwXgradeTransferMode_Type()
)
wwpLeosSwXgradeTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeTransferMode.setStatus("current")


class _WwpLeosSwXgradeLoginId_Type(DisplayString):
    """Custom type wwpLeosSwXgradeLoginId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosSwXgradeLoginId_Type.__name__ = "DisplayString"
_WwpLeosSwXgradeLoginId_Object = MibTableColumn
wwpLeosSwXgradeLoginId = _WwpLeosSwXgradeLoginId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 10),
    _WwpLeosSwXgradeLoginId_Type()
)
wwpLeosSwXgradeLoginId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeLoginId.setStatus("current")


class _WwpLeosSwXgradePassword_Type(DisplayString):
    """Custom type wwpLeosSwXgradePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosSwXgradePassword_Type.__name__ = "DisplayString"
_WwpLeosSwXgradePassword_Object = MibTableColumn
wwpLeosSwXgradePassword = _WwpLeosSwXgradePassword_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 11),
    _WwpLeosSwXgradePassword_Type()
)
wwpLeosSwXgradePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradePassword.setStatus("current")


class _WwpLeosSwXgradeSecret_Type(DisplayString):
    """Custom type wwpLeosSwXgradeSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WwpLeosSwXgradeSecret_Type.__name__ = "DisplayString"
_WwpLeosSwXgradeSecret_Object = MibTableColumn
wwpLeosSwXgradeSecret = _WwpLeosSwXgradeSecret_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 2, 1, 12),
    _WwpLeosSwXgradeSecret_Type()
)
wwpLeosSwXgradeSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeSecret.setStatus("current")
_WwpLeosBladePackageInfoTable_Object = MibTable
wwpLeosBladePackageInfoTable = _WwpLeosBladePackageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosBladePackageInfoTable.setStatus("current")
_WwpLeosBladePackageInfoEntry_Object = MibTableRow
wwpLeosBladePackageInfoEntry = _WwpLeosBladePackageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 3, 1)
)
wwpLeosBladePackageInfoEntry.setIndexNames(
    (0, "WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeBladeId"),
)
if mibBuilder.loadTexts:
    wwpLeosBladePackageInfoEntry.setStatus("current")


class _WwpLeosBladeInstPackageVer_Type(OctetString):
    """Custom type wwpLeosBladeInstPackageVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosBladeInstPackageVer_Type.__name__ = "OctetString"
_WwpLeosBladeInstPackageVer_Object = MibTableColumn
wwpLeosBladeInstPackageVer = _WwpLeosBladeInstPackageVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 3, 1, 1),
    _WwpLeosBladeInstPackageVer_Type()
)
wwpLeosBladeInstPackageVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeInstPackageVer.setStatus("current")


class _WwpLeosBladeRunPackageVer_Type(OctetString):
    """Custom type wwpLeosBladeRunPackageVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosBladeRunPackageVer_Type.__name__ = "OctetString"
_WwpLeosBladeRunPackageVer_Object = MibTableColumn
wwpLeosBladeRunPackageVer = _WwpLeosBladeRunPackageVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 3, 1, 2),
    _WwpLeosBladeRunPackageVer_Type()
)
wwpLeosBladeRunPackageVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeRunPackageVer.setStatus("current")


class _WwpLeosBladeDnldPackageVer_Type(OctetString):
    """Custom type wwpLeosBladeDnldPackageVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosBladeDnldPackageVer_Type.__name__ = "OctetString"
_WwpLeosBladeDnldPackageVer_Object = MibTableColumn
wwpLeosBladeDnldPackageVer = _WwpLeosBladeDnldPackageVer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 3, 1, 3),
    _WwpLeosBladeDnldPackageVer_Type()
)
wwpLeosBladeDnldPackageVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeDnldPackageVer.setStatus("current")


class _WwpLeosBladeInstPackageRlsStatus_Type(OctetString):
    """Custom type wwpLeosBladeInstPackageRlsStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WwpLeosBladeInstPackageRlsStatus_Type.__name__ = "OctetString"
_WwpLeosBladeInstPackageRlsStatus_Object = MibTableColumn
wwpLeosBladeInstPackageRlsStatus = _WwpLeosBladeInstPackageRlsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 3, 1, 4),
    _WwpLeosBladeInstPackageRlsStatus_Type()
)
wwpLeosBladeInstPackageRlsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBladeInstPackageRlsStatus.setStatus("current")
_WwpLeosSwXgradeGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeosSwXgradeGlobalAttrs = _WwpLeosSwXgradeGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 4)
)
_WwpLeosSwMIBVersion_Type = DisplayString
_WwpLeosSwMIBVersion_Object = MibScalar
wwpLeosSwMIBVersion = _WwpLeosSwMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 4, 1),
    _WwpLeosSwMIBVersion_Type()
)
wwpLeosSwMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSwMIBVersion.setStatus("current")


class _WwpLeosSwXgradeDestPath_Type(OctetString):
    """Custom type wwpLeosSwXgradeDestPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosSwXgradeDestPath_Type.__name__ = "OctetString"
_WwpLeosSwXgradeDestPath_Object = MibScalar
wwpLeosSwXgradeDestPath = _WwpLeosSwXgradeDestPath_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 4, 2),
    _WwpLeosSwXgradeDestPath_Type()
)
wwpLeosSwXgradeDestPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeDestPath.setStatus("current")


class _WwpLeosSwXgradePackagePathName_Type(OctetString):
    """Custom type wwpLeosSwXgradePackagePathName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosSwXgradePackagePathName_Type.__name__ = "OctetString"
_WwpLeosSwXgradePackagePathName_Object = MibScalar
wwpLeosSwXgradePackagePathName = _WwpLeosSwXgradePackagePathName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 4, 3),
    _WwpLeosSwXgradePackagePathName_Type()
)
wwpLeosSwXgradePackagePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradePackagePathName.setStatus("current")


class _WwpLeosSwXgradeTftpServer_Type(OctetString):
    """Custom type wwpLeosSwXgradeTftpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosSwXgradeTftpServer_Type.__name__ = "OctetString"
_WwpLeosSwXgradeTftpServer_Object = MibScalar
wwpLeosSwXgradeTftpServer = _WwpLeosSwXgradeTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 4, 4),
    _WwpLeosSwXgradeTftpServer_Type()
)
wwpLeosSwXgradeTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeTftpServer.setStatus("current")


class _WwpLeosSwXgradeRevertTimeout_Type(Integer32):
    """Custom type wwpLeosSwXgradeRevertTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosSwXgradeRevertTimeout_Type.__name__ = "Integer32"
_WwpLeosSwXgradeRevertTimeout_Object = MibScalar
wwpLeosSwXgradeRevertTimeout = _WwpLeosSwXgradeRevertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 4, 5),
    _WwpLeosSwXgradeRevertTimeout_Type()
)
wwpLeosSwXgradeRevertTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeRevertTimeout.setStatus("current")


class _WwpLeosSwXgradeBootOrder_Type(Integer32):
    """Custom type wwpLeosSwXgradeBootOrder based on Integer32"""
    defaultValue = 1

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
        *(("compactFlashThenLocalFlash", 3),
          ("localFlash", 1),
          ("localFlashThenCompactFlash", 2),
          ("unknown", 4))
    )


_WwpLeosSwXgradeBootOrder_Type.__name__ = "Integer32"
_WwpLeosSwXgradeBootOrder_Object = MibScalar
wwpLeosSwXgradeBootOrder = _WwpLeosSwXgradeBootOrder_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 4, 6),
    _WwpLeosSwXgradeBootOrder_Type()
)
wwpLeosSwXgradeBootOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeBootOrder.setStatus("current")


class _WwpLeosSwXgradeOptype_Type(Integer32):
    """Custom type wwpLeosSwXgradeOptype based on Integer32"""
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
        *(("activate", 3),
          ("download", 1),
          ("install", 2),
          ("none", 0),
          ("protect", 4),
          ("revert", 5),
          ("run", 7),
          ("validate", 6))
    )


_WwpLeosSwXgradeOptype_Type.__name__ = "Integer32"
_WwpLeosSwXgradeOptype_Object = MibScalar
wwpLeosSwXgradeOptype = _WwpLeosSwXgradeOptype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 25),
    _WwpLeosSwXgradeOptype_Type()
)
wwpLeosSwXgradeOptype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeOptype.setStatus("current")


class _WwpLeosSwXgradeStatus_Type(Integer32):
    """Custom type wwpLeosSwXgradeStatus based on Integer32"""
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
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("cannotResolveHostName", 8),
          ("failed", 2),
          ("fileNotExist", 18),
          ("fileSystemError", 7),
          ("internalError", 17),
          ("invalidCfgRule", 5),
          ("invalidFileName", 6),
          ("invalidXgradeOp", 20),
          ("missingAttribute", 19),
          ("needBackupSw", 16),
          ("networkError", 13),
          ("noDefaultTftpConfigured", 21),
          ("platformTypeNotSupported", 14),
          ("processing", 4),
          ("success", 1),
          ("swMgrBusy", 15),
          ("tftpBadTag", 11),
          ("tftpBadValue", 12),
          ("tftpClientTimeout", 9),
          ("tftpServerError", 10),
          ("unknown", 3))
    )


_WwpLeosSwXgradeStatus_Type.__name__ = "Integer32"
_WwpLeosSwXgradeStatus_Object = MibScalar
wwpLeosSwXgradeStatus = _WwpLeosSwXgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 1, 1, 30),
    _WwpLeosSwXgradeStatus_Type()
)
wwpLeosSwXgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSwXgradeStatus.setStatus("current")
_WwpLeosSwXgradeMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosSwXgradeMIBNotificationPrefix = _WwpLeosSwXgradeMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 2)
)
_WwpLeosSwXgradeMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosSwXgradeMIBNotifications = _WwpLeosSwXgradeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 2, 0)
)
_WwpLeosSwXgradeMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosSwXgradeMIBConformance = _WwpLeosSwXgradeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 3)
)
_WwpLeosSwXgradeMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosSwXgradeMIBCompliances = _WwpLeosSwXgradeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 3, 1)
)
_WwpLeosSwXgradeMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosSwXgradeMIBGroups = _WwpLeosSwXgradeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosSwDownloadCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 2, 0, 1)
)
wwpLeosSwDownloadCompletion.setObjects(
      *(("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwDownloadPackageName"),
        ("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwDownloadFailCause"),
        ("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwDownloadNotificationInfo"))
)
if mibBuilder.loadTexts:
    wwpLeosSwDownloadCompletion.setStatus(
        "current"
    )

wwpLeosSwXgradeOpCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 2, 0, 2)
)
wwpLeosSwXgradeOpCompletion.setObjects(
      *(("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeBladeId"),
        ("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradePackage"),
        ("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeOp"),
        ("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeOpStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosSwXgradeOpCompletion.setStatus(
        "current"
    )

wwpLeosSwXgradeBladePkgIncorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 2, 0, 3)
)
wwpLeosSwXgradeBladePkgIncorrect.setObjects(
    ("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeBladeId")
)
if mibBuilder.loadTexts:
    wwpLeosSwXgradeBladePkgIncorrect.setStatus(
        "current"
    )

wwpLeosSwXgradeCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 10, 2, 0, 4)
)
wwpLeosSwXgradeCompletion.setObjects(
      *(("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeOp"),
        ("WWP-LEOS-SW-XGRADE-MIB", "wwpLeosSwXgradeStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosSwXgradeCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-SW-XGRADE-MIB",
    **{"SwDownloadState": SwDownloadState,
       "SwDownloadFailCause": SwDownloadFailCause,
       "SwXgradeOp": SwXgradeOp,
       "wwpLeosSwXgradeMIB": wwpLeosSwXgradeMIB,
       "wwpLeosSwXgradeMIBObjects": wwpLeosSwXgradeMIBObjects,
       "wwpLeosSwXgrade": wwpLeosSwXgrade,
       "wwpLeosSwDownload": wwpLeosSwDownload,
       "wwpLeosSwDownloadServerAddrType": wwpLeosSwDownloadServerAddrType,
       "wwpLeosSwDownloadServerAddr": wwpLeosSwDownloadServerAddr,
       "wwpLeosSwDownloadPackageName": wwpLeosSwDownloadPackageName,
       "wwpLeosSwDownLoadActivate": wwpLeosSwDownLoadActivate,
       "wwpLeosSwDownloadNotifOnCompletion": wwpLeosSwDownloadNotifOnCompletion,
       "wwpLeosSwDownloadStatus": wwpLeosSwDownloadStatus,
       "wwpLeosSwDownloadFailCause": wwpLeosSwDownloadFailCause,
       "wwpLeosSwDownloadNotificationInfo": wwpLeosSwDownloadNotificationInfo,
       "wwpLeosSwXgradeBladeTable": wwpLeosSwXgradeBladeTable,
       "wwpLeosSwXgradeBladeEntry": wwpLeosSwXgradeBladeEntry,
       "wwpLeosSwXgradeBladeId": wwpLeosSwXgradeBladeId,
       "wwpLeosSwXgradePackage": wwpLeosSwXgradePackage,
       "wwpLeosSwXgradeOp": wwpLeosSwXgradeOp,
       "wwpLeosSwXgradeTftpAddrType": wwpLeosSwXgradeTftpAddrType,
       "wwpLeosSwXgradeTftpAddr": wwpLeosSwXgradeTftpAddr,
       "wwpLeosSwXgradeOpActivate": wwpLeosSwXgradeOpActivate,
       "wwpLeosSwXgradeOpStatus": wwpLeosSwXgradeOpStatus,
       "wwpLeosSwXgradePackagePath": wwpLeosSwXgradePackagePath,
       "wwpLeosSwXgradeTransferMode": wwpLeosSwXgradeTransferMode,
       "wwpLeosSwXgradeLoginId": wwpLeosSwXgradeLoginId,
       "wwpLeosSwXgradePassword": wwpLeosSwXgradePassword,
       "wwpLeosSwXgradeSecret": wwpLeosSwXgradeSecret,
       "wwpLeosBladePackageInfoTable": wwpLeosBladePackageInfoTable,
       "wwpLeosBladePackageInfoEntry": wwpLeosBladePackageInfoEntry,
       "wwpLeosBladeInstPackageVer": wwpLeosBladeInstPackageVer,
       "wwpLeosBladeRunPackageVer": wwpLeosBladeRunPackageVer,
       "wwpLeosBladeDnldPackageVer": wwpLeosBladeDnldPackageVer,
       "wwpLeosBladeInstPackageRlsStatus": wwpLeosBladeInstPackageRlsStatus,
       "wwpLeosSwXgradeGlobalAttrs": wwpLeosSwXgradeGlobalAttrs,
       "wwpLeosSwMIBVersion": wwpLeosSwMIBVersion,
       "wwpLeosSwXgradeDestPath": wwpLeosSwXgradeDestPath,
       "wwpLeosSwXgradePackagePathName": wwpLeosSwXgradePackagePathName,
       "wwpLeosSwXgradeTftpServer": wwpLeosSwXgradeTftpServer,
       "wwpLeosSwXgradeRevertTimeout": wwpLeosSwXgradeRevertTimeout,
       "wwpLeosSwXgradeBootOrder": wwpLeosSwXgradeBootOrder,
       "wwpLeosSwXgradeOptype": wwpLeosSwXgradeOptype,
       "wwpLeosSwXgradeStatus": wwpLeosSwXgradeStatus,
       "wwpLeosSwXgradeMIBNotificationPrefix": wwpLeosSwXgradeMIBNotificationPrefix,
       "wwpLeosSwXgradeMIBNotifications": wwpLeosSwXgradeMIBNotifications,
       "wwpLeosSwDownloadCompletion": wwpLeosSwDownloadCompletion,
       "wwpLeosSwXgradeOpCompletion": wwpLeosSwXgradeOpCompletion,
       "wwpLeosSwXgradeBladePkgIncorrect": wwpLeosSwXgradeBladePkgIncorrect,
       "wwpLeosSwXgradeCompletion": wwpLeosSwXgradeCompletion,
       "wwpLeosSwXgradeMIBConformance": wwpLeosSwXgradeMIBConformance,
       "wwpLeosSwXgradeMIBCompliances": wwpLeosSwXgradeMIBCompliances,
       "wwpLeosSwXgradeMIBGroups": wwpLeosSwXgradeMIBGroups}
)
