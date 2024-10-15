# SNMP MIB module (LUCENT-GENERIC-DLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LUCENT-GENERIC-DLOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:28 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

luDload = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 677)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LuOpTable_Object = MibTable
luOpTable = _LuOpTable_Object(
    (1, 3, 6, 1, 4, 1, 677, 1)
)
if mibBuilder.loadTexts:
    luOpTable.setStatus("current")
_LuOpEntry_Object = MibTableRow
luOpEntry = _LuOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1)
)
luOpEntry.setIndexNames(
    (0, "LUCENT-GENERIC-DLOAD-MIB", "luOpIndex"),
)
if mibBuilder.loadTexts:
    luOpEntry.setStatus("current")


class _LuOpSerialNumber_Type(OctetString):
    """Custom type luOpSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LuOpSerialNumber_Type.__name__ = "OctetString"
_LuOpSerialNumber_Object = MibTableColumn
luOpSerialNumber = _LuOpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 1),
    _LuOpSerialNumber_Type()
)
luOpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luOpSerialNumber.setStatus("current")


class _LuOpMCodeVersion_Type(OctetString):
    """Custom type luOpMCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LuOpMCodeVersion_Type.__name__ = "OctetString"
_LuOpMCodeVersion_Object = MibTableColumn
luOpMCodeVersion = _LuOpMCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 2),
    _LuOpMCodeVersion_Type()
)
luOpMCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luOpMCodeVersion.setStatus("current")


class _LuOpBCodeVersion_Type(OctetString):
    """Custom type luOpBCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LuOpBCodeVersion_Type.__name__ = "OctetString"
_LuOpBCodeVersion_Object = MibTableColumn
luOpBCodeVersion = _LuOpBCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 3),
    _LuOpBCodeVersion_Type()
)
luOpBCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luOpBCodeVersion.setStatus("current")
_LuOpMCodeFilename_Type = DisplayString
_LuOpMCodeFilename_Object = MibTableColumn
luOpMCodeFilename = _LuOpMCodeFilename_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 4),
    _LuOpMCodeFilename_Type()
)
luOpMCodeFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luOpMCodeFilename.setStatus("current")


class _LuOpAdminStatus_Type(Integer32):
    """Custom type luOpAdminStatus based on Integer32"""
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
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("erase-config", 5),
          ("erase-flash", 6),
          ("file-snapshot", 23),
          ("file-startup", 24),
          ("file-tftp", 17),
          ("halt", 11),
          ("identify", 3),
          ("normal", 1),
          ("reboot", 2),
          ("rpl-ipx", 9),
          ("rpl-llc", 10),
          ("snapshot", 14),
          ("snapshot-startup", 22),
          ("snapshot-tftp", 15),
          ("startup-tftp", 16),
          ("test", 4),
          ("tftp-file", 21),
          ("tftp-ip", 7),
          ("tftp-ipx", 8),
          ("tftp-snapshot", 18),
          ("tftp-start-snap", 20),
          ("tftp-startup", 19),
          ("up-tftp-ip", 12),
          ("up-tftp-ipx", 13))
    )


_LuOpAdminStatus_Type.__name__ = "Integer32"
_LuOpAdminStatus_Object = MibTableColumn
luOpAdminStatus = _LuOpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 5),
    _LuOpAdminStatus_Type()
)
luOpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luOpAdminStatus.setStatus("current")


class _LuOpOperStatus_Type(Integer32):
    """Custom type luOpOperStatus based on Integer32"""
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
        *(("downloading", 5),
          ("identify", 3),
          ("normal", 1),
          ("reading-config", 7),
          ("reboot", 2),
          ("test", 4),
          ("uploading", 6))
    )


_LuOpOperStatus_Type.__name__ = "Integer32"
_LuOpOperStatus_Object = MibTableColumn
luOpOperStatus = _LuOpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 6),
    _LuOpOperStatus_Type()
)
luOpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luOpOperStatus.setStatus("current")
_LuOpEraseFlashVersion_Type = Integer32
_LuOpEraseFlashVersion_Object = MibTableColumn
luOpEraseFlashVersion = _LuOpEraseFlashVersion_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 7),
    _LuOpEraseFlashVersion_Type()
)
luOpEraseFlashVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luOpEraseFlashVersion.setStatus("current")
_LuOpDefaultFlashVersion_Type = Integer32
_LuOpDefaultFlashVersion_Object = MibTableColumn
luOpDefaultFlashVersion = _LuOpDefaultFlashVersion_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 8),
    _LuOpDefaultFlashVersion_Type()
)
luOpDefaultFlashVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luOpDefaultFlashVersion.setStatus("current")
_LuOpConfFileName_Type = DisplayString
_LuOpConfFileName_Object = MibTableColumn
luOpConfFileName = _LuOpConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 9),
    _LuOpConfFileName_Type()
)
luOpConfFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luOpConfFileName.setStatus("current")
_LuOpIndex_Type = Integer32
_LuOpIndex_Object = MibTableColumn
luOpIndex = _LuOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 677, 1, 1, 10),
    _LuOpIndex_Type()
)
luOpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luOpIndex.setStatus("current")
_LuDeviceTable_Object = MibTable
luDeviceTable = _LuDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 677, 2)
)
if mibBuilder.loadTexts:
    luDeviceTable.setStatus("current")
_LuDeviceEntry_Object = MibTableRow
luDeviceEntry = _LuDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 677, 2, 1)
)
luDeviceEntry.setIndexNames(
    (0, "LUCENT-GENERIC-DLOAD-MIB", "luOpIndex"),
    (0, "LUCENT-GENERIC-DLOAD-MIB", "luDeviceIndex"),
)
if mibBuilder.loadTexts:
    luDeviceEntry.setStatus("current")
_LuDeviceIndex_Type = Integer32
_LuDeviceIndex_Object = MibTableColumn
luDeviceIndex = _LuDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 677, 2, 1, 1),
    _LuDeviceIndex_Type()
)
luDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    luDeviceIndex.setStatus("current")


class _LuDeviceDescription_Type(DisplayString):
    """Custom type luDeviceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LuDeviceDescription_Type.__name__ = "DisplayString"
_LuDeviceDescription_Object = MibTableColumn
luDeviceDescription = _LuDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 677, 2, 1, 2),
    _LuDeviceDescription_Type()
)
luDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceDescription.setStatus("current")


class _LuDeviceLocation_Type(DisplayString):
    """Custom type luDeviceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LuDeviceLocation_Type.__name__ = "DisplayString"
_LuDeviceLocation_Object = MibTableColumn
luDeviceLocation = _LuDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 677, 2, 1, 3),
    _LuDeviceLocation_Type()
)
luDeviceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceLocation.setStatus("current")


class _LuDeviceNumber_Type(OctetString):
    """Custom type luDeviceNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LuDeviceNumber_Type.__name__ = "OctetString"
_LuDeviceNumber_Object = MibTableColumn
luDeviceNumber = _LuDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 677, 2, 1, 4),
    _LuDeviceNumber_Type()
)
luDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceNumber.setStatus("current")


class _LuDeviceType_Type(Integer32):
    """Custom type luDeviceType based on Integer32"""
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
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("boot-fixed", 2),
          ("boot-updateable", 3),
          ("default-boot-loader", 11),
          ("default-image", 9),
          ("flash", 1),
          ("hardware-fixed", 4),
          ("hardware-upgradeable", 5),
          ("non-default-boot-loader", 12),
          ("non-default-image", 10),
          ("nvram", 21),
          ("other", 6),
          ("sw-component", 8),
          ("sw-running", 7),
          ("unknown", 20))
    )


_LuDeviceType_Type.__name__ = "Integer32"
_LuDeviceType_Object = MibTableColumn
luDeviceType = _LuDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 677, 2, 1, 5),
    _LuDeviceType_Type()
)
luDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceType.setStatus("current")


class _LuDeviceFileName_Type(DisplayString):
    """Custom type luDeviceFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LuDeviceFileName_Type.__name__ = "DisplayString"
_LuDeviceFileName_Object = MibTableColumn
luDeviceFileName = _LuDeviceFileName_Object(
    (1, 3, 6, 1, 4, 1, 677, 2, 1, 6),
    _LuDeviceFileName_Type()
)
luDeviceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDeviceFileName.setStatus("current")
_LuDeviceCount_Type = Integer32
_LuDeviceCount_Object = MibScalar
luDeviceCount = _LuDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 677, 3),
    _LuDeviceCount_Type()
)
luDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceCount.setStatus("current")
_LuDownloadTable_Object = MibTable
luDownloadTable = _LuDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 677, 4)
)
if mibBuilder.loadTexts:
    luDownloadTable.setStatus("current")
_LuDownloadEntry_Object = MibTableRow
luDownloadEntry = _LuDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1)
)
luDownloadEntry.setIndexNames(
    (0, "LUCENT-GENERIC-DLOAD-MIB", "luOpIndex"),
)
if mibBuilder.loadTexts:
    luDownloadEntry.setStatus("current")
_LuDownloadIPAddress_Type = IpAddress
_LuDownloadIPAddress_Object = MibTableColumn
luDownloadIPAddress = _LuDownloadIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 1),
    _LuDownloadIPAddress_Type()
)
luDownloadIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDownloadIPAddress.setStatus("current")
_LuDownloadIPGateway_Type = IpAddress
_LuDownloadIPGateway_Object = MibTableColumn
luDownloadIPGateway = _LuDownloadIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 2),
    _LuDownloadIPGateway_Type()
)
luDownloadIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDownloadIPGateway.setStatus("current")


class _LuDownloadIPXAddress_Type(OctetString):
    """Custom type luDownloadIPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_LuDownloadIPXAddress_Type.__name__ = "OctetString"
_LuDownloadIPXAddress_Object = MibTableColumn
luDownloadIPXAddress = _LuDownloadIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 3),
    _LuDownloadIPXAddress_Type()
)
luDownloadIPXAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDownloadIPXAddress.setStatus("current")
_LuDownloadNodeAddress_Type = MacAddress
_LuDownloadNodeAddress_Object = MibTableColumn
luDownloadNodeAddress = _LuDownloadNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 4),
    _LuDownloadNodeAddress_Type()
)
luDownloadNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDownloadNodeAddress.setStatus("current")
_LuDownloadFileName_Type = DisplayString
_LuDownloadFileName_Object = MibTableColumn
luDownloadFileName = _LuDownloadFileName_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 5),
    _LuDownloadFileName_Type()
)
luDownloadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDownloadFileName.setStatus("current")
_LuDownloadDestination_Type = Integer32
_LuDownloadDestination_Object = MibTableColumn
luDownloadDestination = _LuDownloadDestination_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 6),
    _LuDownloadDestination_Type()
)
luDownloadDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDownloadDestination.setStatus("current")


class _LuDownloadState_Type(Integer32):
    """Custom type luDownloadState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("reading-configuration", 12),
          ("rpl-running-ipx", 9),
          ("rpl-running-llc", 11),
          ("rpl-waiting-ipx", 8),
          ("rpl-waiting-llc", 10),
          ("running-xmodem", 7),
          ("tftp-running-ip", 3),
          ("tftp-running-ipx", 5),
          ("tftp-waiting-ip", 2),
          ("tftp-waiting-ipx", 4),
          ("waiting-xmodem", 6))
    )


_LuDownloadState_Type.__name__ = "Integer32"
_LuDownloadState_Object = MibTableColumn
luDownloadState = _LuDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 7),
    _LuDownloadState_Type()
)
luDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDownloadState.setStatus("current")


class _LuDownloadFailureCode_Type(Integer32):
    """Custom type luDownloadFailureCode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107)
        )
    )
    namedValues = NamedValues(
        *(("access-violation", 102),
          ("busy", 3),
          ("cancelled", 5),
          ("conf-file-exec-error", 13),
          ("conf-file-gen-err", 11),
          ("conf-file-parse-error", 12),
          ("config-error", 2),
          ("file-already-exists", 106),
          ("file-not-found", 101),
          ("file-too-big", 7),
          ("flash-write-error", 9),
          ("illegal-operation", 104),
          ("incompatible-file", 6),
          ("no-error", 1),
          ("no-such-user", 107),
          ("nvram-write-error", 10),
          ("out-of-memory", 103),
          ("protocol-error", 8),
          ("timeout", 4),
          ("undefined-error", 100),
          ("unknown-transfer-id", 105))
    )


_LuDownloadFailureCode_Type.__name__ = "Integer32"
_LuDownloadFailureCode_Object = MibTableColumn
luDownloadFailureCode = _LuDownloadFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 8),
    _LuDownloadFailureCode_Type()
)
luDownloadFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDownloadFailureCode.setStatus("current")


class _LuDownloadStatusText_Type(DisplayString):
    """Custom type luDownloadStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LuDownloadStatusText_Type.__name__ = "DisplayString"
_LuDownloadStatusText_Object = MibTableColumn
luDownloadStatusText = _LuDownloadStatusText_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 9),
    _LuDownloadStatusText_Type()
)
luDownloadStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDownloadStatusText.setStatus("current")
_LuDownloadSize_Type = Integer32
_LuDownloadSize_Object = MibTableColumn
luDownloadSize = _LuDownloadSize_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 10),
    _LuDownloadSize_Type()
)
luDownloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDownloadSize.setStatus("current")
_LuDownloadErrorLogName_Type = DisplayString
_LuDownloadErrorLogName_Object = MibTableColumn
luDownloadErrorLogName = _LuDownloadErrorLogName_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 11),
    _LuDownloadErrorLogName_Type()
)
luDownloadErrorLogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDownloadErrorLogName.setStatus("current")
_LuDownloadErrorLogLocation_Type = Integer32
_LuDownloadErrorLogLocation_Object = MibTableColumn
luDownloadErrorLogLocation = _LuDownloadErrorLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 677, 4, 1, 12),
    _LuDownloadErrorLogLocation_Type()
)
luDownloadErrorLogLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luDownloadErrorLogLocation.setStatus("current")
_LuUploadTable_Object = MibTable
luUploadTable = _LuUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 677, 5)
)
if mibBuilder.loadTexts:
    luUploadTable.setStatus("current")
_LuUploadEntry_Object = MibTableRow
luUploadEntry = _LuUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1)
)
luUploadEntry.setIndexNames(
    (0, "LUCENT-GENERIC-DLOAD-MIB", "luOpIndex"),
)
if mibBuilder.loadTexts:
    luUploadEntry.setStatus("current")
_LuUploadIPAddress_Type = IpAddress
_LuUploadIPAddress_Object = MibTableColumn
luUploadIPAddress = _LuUploadIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 1),
    _LuUploadIPAddress_Type()
)
luUploadIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luUploadIPAddress.setStatus("current")
_LuUploadIPGateway_Type = IpAddress
_LuUploadIPGateway_Object = MibTableColumn
luUploadIPGateway = _LuUploadIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 2),
    _LuUploadIPGateway_Type()
)
luUploadIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luUploadIPGateway.setStatus("current")


class _LuUploadIPXAddress_Type(OctetString):
    """Custom type luUploadIPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_LuUploadIPXAddress_Type.__name__ = "OctetString"
_LuUploadIPXAddress_Object = MibTableColumn
luUploadIPXAddress = _LuUploadIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 3),
    _LuUploadIPXAddress_Type()
)
luUploadIPXAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luUploadIPXAddress.setStatus("current")
_LuUploadFileName_Type = DisplayString
_LuUploadFileName_Object = MibTableColumn
luUploadFileName = _LuUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 4),
    _LuUploadFileName_Type()
)
luUploadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luUploadFileName.setStatus("current")
_LuUploadSource_Type = Integer32
_LuUploadSource_Object = MibTableColumn
luUploadSource = _LuUploadSource_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 5),
    _LuUploadSource_Type()
)
luUploadSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luUploadSource.setStatus("current")


class _LuUploadState_Type(Integer32):
    """Custom type luUploadState based on Integer32"""
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
        *(("idle", 1),
          ("tftp-running-ip", 3),
          ("tftp-running-ipx", 5),
          ("tftp-waiting-ip", 2),
          ("tftp-waiting-ipx", 4))
    )


_LuUploadState_Type.__name__ = "Integer32"
_LuUploadState_Object = MibTableColumn
luUploadState = _LuUploadState_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 6),
    _LuUploadState_Type()
)
luUploadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luUploadState.setStatus("current")


class _LuUploadFailureCode_Type(Integer32):
    """Custom type luUploadFailureCode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107)
        )
    )
    namedValues = NamedValues(
        *(("access-violation", 102),
          ("busy", 3),
          ("cancelled", 5),
          ("conf-file-exec-error", 12),
          ("conf-file-gen-err", 11),
          ("config-error", 2),
          ("file-already-exists", 106),
          ("file-not-found", 101),
          ("file-too-big", 7),
          ("flash-write-error", 9),
          ("illegal-operation", 104),
          ("incompatible-file", 6),
          ("no-error", 1),
          ("no-such-user", 107),
          ("nvram-read-error", 10),
          ("out-of-memory", 103),
          ("protocol-error", 8),
          ("timeout", 4),
          ("undefined-error", 100),
          ("unknown-transfer-id", 105))
    )


_LuUploadFailureCode_Type.__name__ = "Integer32"
_LuUploadFailureCode_Object = MibTableColumn
luUploadFailureCode = _LuUploadFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 7),
    _LuUploadFailureCode_Type()
)
luUploadFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luUploadFailureCode.setStatus("current")


class _LuUploadStatusText_Type(DisplayString):
    """Custom type luUploadStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LuUploadStatusText_Type.__name__ = "DisplayString"
_LuUploadStatusText_Object = MibTableColumn
luUploadStatusText = _LuUploadStatusText_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 8),
    _LuUploadStatusText_Type()
)
luUploadStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luUploadStatusText.setStatus("current")
_LuUploadSize_Type = Integer32
_LuUploadSize_Object = MibTableColumn
luUploadSize = _LuUploadSize_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 9),
    _LuUploadSize_Type()
)
luUploadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luUploadSize.setStatus("current")
_LuUploadErrorLogName_Type = DisplayString
_LuUploadErrorLogName_Object = MibTableColumn
luUploadErrorLogName = _LuUploadErrorLogName_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 10),
    _LuUploadErrorLogName_Type()
)
luUploadErrorLogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luUploadErrorLogName.setStatus("current")
_LuUploadErrorLogLocation_Type = Integer32
_LuUploadErrorLogLocation_Object = MibTableColumn
luUploadErrorLogLocation = _LuUploadErrorLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 677, 5, 1, 11),
    _LuUploadErrorLogLocation_Type()
)
luUploadErrorLogLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luUploadErrorLogLocation.setStatus("current")
_LuDloadNotifications_ObjectIdentity = ObjectIdentity
luDloadNotifications = _LuDloadNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 677, 6)
)
_LuNotificationNextIndex_Type = Integer32
_LuNotificationNextIndex_Object = MibScalar
luNotificationNextIndex = _LuNotificationNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 1),
    _LuNotificationNextIndex_Type()
)
luNotificationNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationNextIndex.setStatus("current")
_LuNotificationDestTable_Object = MibTable
luNotificationDestTable = _LuNotificationDestTable_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2)
)
if mibBuilder.loadTexts:
    luNotificationDestTable.setStatus("current")
_LuNotificationDestEntry_Object = MibTableRow
luNotificationDestEntry = _LuNotificationDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1)
)
luNotificationDestEntry.setIndexNames(
    (0, "LUCENT-GENERIC-DLOAD-MIB", "luNotificationIndex"),
)
if mibBuilder.loadTexts:
    luNotificationDestEntry.setStatus("current")
_LuNotificationIndex_Type = Integer32
_LuNotificationIndex_Object = MibTableColumn
luNotificationIndex = _LuNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1, 1),
    _LuNotificationIndex_Type()
)
luNotificationIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationIndex.setStatus("current")
_LuNotificationIPAddress_Type = IpAddress
_LuNotificationIPAddress_Object = MibTableColumn
luNotificationIPAddress = _LuNotificationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1, 2),
    _LuNotificationIPAddress_Type()
)
luNotificationIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationIPAddress.setStatus("current")
_LuNotificationIPGateway_Type = IpAddress
_LuNotificationIPGateway_Object = MibTableColumn
luNotificationIPGateway = _LuNotificationIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1, 3),
    _LuNotificationIPGateway_Type()
)
luNotificationIPGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationIPGateway.setStatus("current")


class _LuNotificationIPXAddress_Type(OctetString):
    """Custom type luNotificationIPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_LuNotificationIPXAddress_Type.__name__ = "OctetString"
_LuNotificationIPXAddress_Object = MibTableColumn
luNotificationIPXAddress = _LuNotificationIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1, 4),
    _LuNotificationIPXAddress_Type()
)
luNotificationIPXAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationIPXAddress.setStatus("current")
_LuNotificationNodeAddress_Type = MacAddress
_LuNotificationNodeAddress_Object = MibTableColumn
luNotificationNodeAddress = _LuNotificationNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1, 5),
    _LuNotificationNodeAddress_Type()
)
luNotificationNodeAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationNodeAddress.setStatus("current")


class _LuNotificationTrapTypes_Type(Integer32):
    """Custom type luNotificationTrapTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allDloadTraps", 1),
          ("noDloadTraps", 0))
    )


_LuNotificationTrapTypes_Type.__name__ = "Integer32"
_LuNotificationTrapTypes_Object = MibTableColumn
luNotificationTrapTypes = _LuNotificationTrapTypes_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1, 6),
    _LuNotificationTrapTypes_Type()
)
luNotificationTrapTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationTrapTypes.setStatus("current")
_LuNotificationRowStatus_Type = RowStatus
_LuNotificationRowStatus_Object = MibTableColumn
luNotificationRowStatus = _LuNotificationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 677, 6, 2, 1, 7),
    _LuNotificationRowStatus_Type()
)
luNotificationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    luNotificationRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

luDloadTrapCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 677, 6, 3)
)
luDloadTrapCompleted.setObjects(
      *(("LUCENT-GENERIC-DLOAD-MIB", "luOpIndex"),
        ("LUCENT-GENERIC-DLOAD-MIB", "luDownloadDestination"),
        ("LUCENT-GENERIC-DLOAD-MIB", "luDownloadFileName"),
        ("LUCENT-GENERIC-DLOAD-MIB", "luDownloadFailureCode"))
)
if mibBuilder.loadTexts:
    luDloadTrapCompleted.setStatus(
        "current"
    )

luUpLoadTrapCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 677, 6, 4)
)
luUpLoadTrapCompleted.setObjects(
      *(("LUCENT-GENERIC-DLOAD-MIB", "luOpIndex"),
        ("LUCENT-GENERIC-DLOAD-MIB", "luUploadSource"),
        ("LUCENT-GENERIC-DLOAD-MIB", "luUploadFileName"),
        ("LUCENT-GENERIC-DLOAD-MIB", "luUploadFailureCode"))
)
if mibBuilder.loadTexts:
    luUpLoadTrapCompleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUCENT-GENERIC-DLOAD-MIB",
    **{"luDload": luDload,
       "luOpTable": luOpTable,
       "luOpEntry": luOpEntry,
       "luOpSerialNumber": luOpSerialNumber,
       "luOpMCodeVersion": luOpMCodeVersion,
       "luOpBCodeVersion": luOpBCodeVersion,
       "luOpMCodeFilename": luOpMCodeFilename,
       "luOpAdminStatus": luOpAdminStatus,
       "luOpOperStatus": luOpOperStatus,
       "luOpEraseFlashVersion": luOpEraseFlashVersion,
       "luOpDefaultFlashVersion": luOpDefaultFlashVersion,
       "luOpConfFileName": luOpConfFileName,
       "luOpIndex": luOpIndex,
       "luDeviceTable": luDeviceTable,
       "luDeviceEntry": luDeviceEntry,
       "luDeviceIndex": luDeviceIndex,
       "luDeviceDescription": luDeviceDescription,
       "luDeviceLocation": luDeviceLocation,
       "luDeviceNumber": luDeviceNumber,
       "luDeviceType": luDeviceType,
       "luDeviceFileName": luDeviceFileName,
       "luDeviceCount": luDeviceCount,
       "luDownloadTable": luDownloadTable,
       "luDownloadEntry": luDownloadEntry,
       "luDownloadIPAddress": luDownloadIPAddress,
       "luDownloadIPGateway": luDownloadIPGateway,
       "luDownloadIPXAddress": luDownloadIPXAddress,
       "luDownloadNodeAddress": luDownloadNodeAddress,
       "luDownloadFileName": luDownloadFileName,
       "luDownloadDestination": luDownloadDestination,
       "luDownloadState": luDownloadState,
       "luDownloadFailureCode": luDownloadFailureCode,
       "luDownloadStatusText": luDownloadStatusText,
       "luDownloadSize": luDownloadSize,
       "luDownloadErrorLogName": luDownloadErrorLogName,
       "luDownloadErrorLogLocation": luDownloadErrorLogLocation,
       "luUploadTable": luUploadTable,
       "luUploadEntry": luUploadEntry,
       "luUploadIPAddress": luUploadIPAddress,
       "luUploadIPGateway": luUploadIPGateway,
       "luUploadIPXAddress": luUploadIPXAddress,
       "luUploadFileName": luUploadFileName,
       "luUploadSource": luUploadSource,
       "luUploadState": luUploadState,
       "luUploadFailureCode": luUploadFailureCode,
       "luUploadStatusText": luUploadStatusText,
       "luUploadSize": luUploadSize,
       "luUploadErrorLogName": luUploadErrorLogName,
       "luUploadErrorLogLocation": luUploadErrorLogLocation,
       "luDloadNotifications": luDloadNotifications,
       "luNotificationNextIndex": luNotificationNextIndex,
       "luNotificationDestTable": luNotificationDestTable,
       "luNotificationDestEntry": luNotificationDestEntry,
       "luNotificationIndex": luNotificationIndex,
       "luNotificationIPAddress": luNotificationIPAddress,
       "luNotificationIPGateway": luNotificationIPGateway,
       "luNotificationIPXAddress": luNotificationIPXAddress,
       "luNotificationNodeAddress": luNotificationNodeAddress,
       "luNotificationTrapTypes": luNotificationTrapTypes,
       "luNotificationRowStatus": luNotificationRowStatus,
       "luDloadTrapCompleted": luDloadTrapCompleted,
       "luUpLoadTrapCompleted": luUpLoadTrapCompleted}
)
