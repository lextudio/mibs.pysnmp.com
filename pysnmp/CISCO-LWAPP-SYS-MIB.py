# SNMP MIB module (CISCO-LWAPP-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:02 2024
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

(cldcClientAccessVLAN,
 cldcClientMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientAccessVLAN",
    "cldcClientMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

ciscoLwappSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618)
)
ciscoLwappSysMIB.setRevisions(
        ("2012-08-06 00:00",
         "2012-06-18 00:00",
         "2010-02-09 00:00",
         "2007-03-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappSysMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBNotifs = _CiscoLwappSysMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0)
)
_CiscoLwappSysMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBObjects = _CiscoLwappSysMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1)
)
_ClsConfig_ObjectIdentity = ObjectIdentity
clsConfig = _ClsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1)
)
_ClsDot3BridgeEnabled_Type = TruthValue
_ClsDot3BridgeEnabled_Object = MibScalar
clsDot3BridgeEnabled = _ClsDot3BridgeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 1),
    _ClsDot3BridgeEnabled_Type()
)
clsDot3BridgeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsDot3BridgeEnabled.setStatus("current")
_ClsConfigDownload_ObjectIdentity = ObjectIdentity
clsConfigDownload = _ClsConfigDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 2)
)


class _ClsDownloadFileType_Type(Integer32):
    """Custom type clsDownloadFileType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("code", 2),
          ("config", 3),
          ("customWebAuth", 7),
          ("signatures", 6),
          ("unknown", 1),
          ("vendorCaCert", 9),
          ("vendorDeviceCert", 8),
          ("webAdminCert", 5),
          ("webAuthCert", 4))
    )


_ClsDownloadFileType_Type.__name__ = "Integer32"
_ClsDownloadFileType_Object = MibScalar
clsDownloadFileType = _ClsDownloadFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 2, 1),
    _ClsDownloadFileType_Type()
)
clsDownloadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsDownloadFileType.setStatus("current")


class _ClsDownloadCertificateKey_Type(SnmpAdminString):
    """Custom type clsDownloadCertificateKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClsDownloadCertificateKey_Type.__name__ = "SnmpAdminString"
_ClsDownloadCertificateKey_Object = MibScalar
clsDownloadCertificateKey = _ClsDownloadCertificateKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 2, 2),
    _ClsDownloadCertificateKey_Type()
)
clsDownloadCertificateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsDownloadCertificateKey.setStatus("current")
_ClsConfigUpload_ObjectIdentity = ObjectIdentity
clsConfigUpload = _ClsConfigUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3)
)


class _ClsUploadFileType_Type(Integer32):
    """Custom type clsUploadFileType based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("crashFile", 6),
          ("debugfile", 11),
          ("errorLog", 3),
          ("invalidConfig", 10),
          ("pac", 8),
          ("panicCrash", 14),
          ("pktCapture", 12),
          ("radioCoreDump", 9),
          ("signatures", 7),
          ("systemTrace", 4),
          ("trapLog", 5),
          ("unknown", 1),
          ("vendorCaCert", 16),
          ("vendorDevCert", 15),
          ("watchdogCrash", 13),
          ("webAdminCert", 17),
          ("webAuthCert", 18))
    )


_ClsUploadFileType_Type.__name__ = "Integer32"
_ClsUploadFileType_Object = MibScalar
clsUploadFileType = _ClsUploadFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 1),
    _ClsUploadFileType_Type()
)
clsUploadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadFileType.setStatus("current")


class _ClsUploadPacUsername_Type(SnmpAdminString):
    """Custom type clsUploadPacUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ClsUploadPacUsername_Type.__name__ = "SnmpAdminString"
_ClsUploadPacUsername_Object = MibScalar
clsUploadPacUsername = _ClsUploadPacUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 2),
    _ClsUploadPacUsername_Type()
)
clsUploadPacUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadPacUsername.setStatus("current")


class _ClsUploadPacPassword_Type(SnmpAdminString):
    """Custom type clsUploadPacPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClsUploadPacPassword_Type.__name__ = "SnmpAdminString"
_ClsUploadPacPassword_Object = MibScalar
clsUploadPacPassword = _ClsUploadPacPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 3),
    _ClsUploadPacPassword_Type()
)
clsUploadPacPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadPacPassword.setStatus("current")


class _ClsUploadPacValidity_Type(Unsigned32):
    """Custom type clsUploadPacValidity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClsUploadPacValidity_Type.__name__ = "Unsigned32"
_ClsUploadPacValidity_Object = MibScalar
clsUploadPacValidity = _ClsUploadPacValidity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 3, 4),
    _ClsUploadPacValidity_Type()
)
clsUploadPacValidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsUploadPacValidity.setStatus("current")
if mibBuilder.loadTexts:
    clsUploadPacValidity.setUnits("days")
_ClsTransferConfigGroup_ObjectIdentity = ObjectIdentity
clsTransferConfigGroup = _ClsTransferConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 4)
)


class _ClsTransferConfigFileEncryption_Type(Integer32):
    """Custom type clsTransferConfigFileEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ClsTransferConfigFileEncryption_Type.__name__ = "Integer32"
_ClsTransferConfigFileEncryption_Object = MibScalar
clsTransferConfigFileEncryption = _ClsTransferConfigFileEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 4, 1),
    _ClsTransferConfigFileEncryption_Type()
)
clsTransferConfigFileEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferConfigFileEncryption.setStatus("current")


class _ClsTransferConfigFileEncryptionKey_Type(SnmpAdminString):
    """Custom type clsTransferConfigFileEncryptionKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClsTransferConfigFileEncryptionKey_Type.__name__ = "SnmpAdminString"
_ClsTransferConfigFileEncryptionKey_Object = MibScalar
clsTransferConfigFileEncryptionKey = _ClsTransferConfigFileEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 4, 2),
    _ClsTransferConfigFileEncryptionKey_Type()
)
clsTransferConfigFileEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferConfigFileEncryptionKey.setStatus("current")
_ClsConfigGeneral_ObjectIdentity = ObjectIdentity
clsConfigGeneral = _ClsConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5)
)
_ClsTimeZone_Type = Unsigned32
_ClsTimeZone_Object = MibScalar
clsTimeZone = _ClsTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 1),
    _ClsTimeZone_Type()
)
clsTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTimeZone.setStatus("current")
_ClsTimeZoneDescription_Type = SnmpAdminString
_ClsTimeZoneDescription_Object = MibScalar
clsTimeZoneDescription = _ClsTimeZoneDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 2),
    _ClsTimeZoneDescription_Type()
)
clsTimeZoneDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTimeZoneDescription.setStatus("current")
_ClsMaxClientsTrapThreshold_Type = Unsigned32
_ClsMaxClientsTrapThreshold_Object = MibScalar
clsMaxClientsTrapThreshold = _ClsMaxClientsTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 3),
    _ClsMaxClientsTrapThreshold_Type()
)
clsMaxClientsTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxClientsTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsMaxClientsTrapThreshold.setUnits("Percent")
_ClsMaxRFIDTagsTrapThreshold_Type = Unsigned32
_ClsMaxRFIDTagsTrapThreshold_Object = MibScalar
clsMaxRFIDTagsTrapThreshold = _ClsMaxRFIDTagsTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 5, 4),
    _ClsMaxRFIDTagsTrapThreshold_Type()
)
clsMaxRFIDTagsTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsTrapThreshold.setUnits("Percent")
_ClsSyslogIpConfig_ObjectIdentity = ObjectIdentity
clsSyslogIpConfig = _ClsSyslogIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6)
)
_CLSysLogConfigTable_Object = MibTable
cLSysLogConfigTable = _CLSysLogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLSysLogConfigTable.setStatus("current")
_CLSysLogConfigEntry_Object = MibTableRow
cLSysLogConfigEntry = _CLSysLogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1)
)
cLSysLogConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "cLSysLogServerIndex"),
)
if mibBuilder.loadTexts:
    cLSysLogConfigEntry.setStatus("current")
_CLSysLogServerIndex_Type = Unsigned32
_CLSysLogServerIndex_Object = MibTableColumn
cLSysLogServerIndex = _CLSysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 1),
    _CLSysLogServerIndex_Type()
)
cLSysLogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSysLogServerIndex.setStatus("current")
_CLSysLogAddressType_Type = InetAddressType
_CLSysLogAddressType_Object = MibTableColumn
cLSysLogAddressType = _CLSysLogAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 2),
    _CLSysLogAddressType_Type()
)
cLSysLogAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSysLogAddressType.setStatus("current")
_CLSysLogAddress_Type = InetAddress
_CLSysLogAddress_Object = MibTableColumn
cLSysLogAddress = _CLSysLogAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 3),
    _CLSysLogAddress_Type()
)
cLSysLogAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSysLogAddress.setStatus("current")
_CLSysLogHostRowStatus_Type = RowStatus
_CLSysLogHostRowStatus_Object = MibTableColumn
cLSysLogHostRowStatus = _CLSysLogHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 6, 1, 1, 4),
    _CLSysLogHostRowStatus_Type()
)
cLSysLogHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSysLogHostRowStatus.setStatus("current")
_CLSysArpUnicastEnabled_Type = TruthValue
_CLSysArpUnicastEnabled_Object = MibScalar
cLSysArpUnicastEnabled = _CLSysArpUnicastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 7),
    _CLSysArpUnicastEnabled_Type()
)
cLSysArpUnicastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysArpUnicastEnabled.setStatus("current")
_ClsTransferConfig_ObjectIdentity = ObjectIdentity
clsTransferConfig = _ClsTransferConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8)
)
_ClsTransferConfigTable_Object = MibTable
clsTransferConfigTable = _ClsTransferConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    clsTransferConfigTable.setStatus("current")
_ClsTransferConfigEntry_Object = MibTableRow
clsTransferConfigEntry = _ClsTransferConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1)
)
clsTransferConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsTransferType"),
    (0, "CISCO-LWAPP-SYS-MIB", "clsTransferMode"),
)
if mibBuilder.loadTexts:
    clsTransferConfigEntry.setStatus("current")


class _ClsTransferType_Type(Integer32):
    """Custom type clsTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_ClsTransferType_Type.__name__ = "Integer32"
_ClsTransferType_Object = MibTableColumn
clsTransferType = _ClsTransferType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 1),
    _ClsTransferType_Type()
)
clsTransferType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsTransferType.setStatus("current")


class _ClsTransferMode_Type(Integer32):
    """Custom type clsTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("sftp", 3),
          ("tftp", 1))
    )


_ClsTransferMode_Type.__name__ = "Integer32"
_ClsTransferMode_Object = MibTableColumn
clsTransferMode = _ClsTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 2),
    _ClsTransferMode_Type()
)
clsTransferMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsTransferMode.setStatus("current")
_ClsTransferServerAddressType_Type = InetAddressType
_ClsTransferServerAddressType_Object = MibTableColumn
clsTransferServerAddressType = _ClsTransferServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 3),
    _ClsTransferServerAddressType_Type()
)
clsTransferServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferServerAddressType.setStatus("current")
_ClsTransferServerAddress_Type = InetAddress
_ClsTransferServerAddress_Object = MibTableColumn
clsTransferServerAddress = _ClsTransferServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 4),
    _ClsTransferServerAddress_Type()
)
clsTransferServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferServerAddress.setStatus("current")


class _ClsTransferPath_Type(SnmpAdminString):
    """Custom type clsTransferPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferPath_Type.__name__ = "SnmpAdminString"
_ClsTransferPath_Object = MibTableColumn
clsTransferPath = _ClsTransferPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 5),
    _ClsTransferPath_Type()
)
clsTransferPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferPath.setStatus("current")


class _ClsTransferFilename_Type(SnmpAdminString):
    """Custom type clsTransferFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClsTransferFilename_Type.__name__ = "SnmpAdminString"
_ClsTransferFilename_Object = MibTableColumn
clsTransferFilename = _ClsTransferFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 6),
    _ClsTransferFilename_Type()
)
clsTransferFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFilename.setStatus("current")


class _ClsTransferFtpUsername_Type(SnmpAdminString):
    """Custom type clsTransferFtpUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClsTransferFtpUsername_Type.__name__ = "SnmpAdminString"
_ClsTransferFtpUsername_Object = MibTableColumn
clsTransferFtpUsername = _ClsTransferFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 7),
    _ClsTransferFtpUsername_Type()
)
clsTransferFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFtpUsername.setStatus("current")


class _ClsTransferFtpPassword_Type(SnmpAdminString):
    """Custom type clsTransferFtpPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClsTransferFtpPassword_Type.__name__ = "SnmpAdminString"
_ClsTransferFtpPassword_Object = MibTableColumn
clsTransferFtpPassword = _ClsTransferFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 8),
    _ClsTransferFtpPassword_Type()
)
clsTransferFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFtpPassword.setStatus("current")


class _ClsTransferFtpPortNum_Type(InetPortNumber):
    """Custom type clsTransferFtpPortNum based on InetPortNumber"""
    defaultValue = 21


_ClsTransferFtpPortNum_Object = MibTableColumn
clsTransferFtpPortNum = _ClsTransferFtpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 9),
    _ClsTransferFtpPortNum_Type()
)
clsTransferFtpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferFtpPortNum.setStatus("current")


class _ClsTransferTftpMaxRetries_Type(Unsigned32):
    """Custom type clsTransferTftpMaxRetries based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ClsTransferTftpMaxRetries_Type.__name__ = "Unsigned32"
_ClsTransferTftpMaxRetries_Object = MibTableColumn
clsTransferTftpMaxRetries = _ClsTransferTftpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 10),
    _ClsTransferTftpMaxRetries_Type()
)
clsTransferTftpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferTftpMaxRetries.setStatus("current")


class _ClsTransferTftpTimeout_Type(Unsigned32):
    """Custom type clsTransferTftpTimeout based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ClsTransferTftpTimeout_Type.__name__ = "Unsigned32"
_ClsTransferTftpTimeout_Object = MibTableColumn
clsTransferTftpTimeout = _ClsTransferTftpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 11),
    _ClsTransferTftpTimeout_Type()
)
clsTransferTftpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferTftpTimeout.setStatus("current")


class _ClsTransferStart_Type(Integer32):
    """Custom type clsTransferStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 2),
          ("initiatePeer", 3),
          ("none", 1))
    )


_ClsTransferStart_Type.__name__ = "Integer32"
_ClsTransferStart_Object = MibTableColumn
clsTransferStart = _ClsTransferStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 12),
    _ClsTransferStart_Type()
)
clsTransferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsTransferStart.setStatus("current")


class _ClsTransferStatus_Type(Integer32):
    """Custom type clsTransferStatus based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("bootBreakOff", 14),
          ("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("invalidTarFile", 15),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknown", 99),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_ClsTransferStatus_Type.__name__ = "Integer32"
_ClsTransferStatus_Object = MibTableColumn
clsTransferStatus = _ClsTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 13),
    _ClsTransferStatus_Type()
)
clsTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTransferStatus.setStatus("current")


class _ClsTransferStatusString_Type(SnmpAdminString):
    """Custom type clsTransferStatusString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClsTransferStatusString_Type.__name__ = "SnmpAdminString"
_ClsTransferStatusString_Object = MibTableColumn
clsTransferStatusString = _ClsTransferStatusString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 8, 1, 1, 14),
    _ClsTransferStatusString_Type()
)
clsTransferStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsTransferStatusString.setStatus("current")
_CLSysBroadcastForwardingEnabled_Type = TruthValue
_CLSysBroadcastForwardingEnabled_Object = MibScalar
cLSysBroadcastForwardingEnabled = _CLSysBroadcastForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 9),
    _CLSysBroadcastForwardingEnabled_Type()
)
cLSysBroadcastForwardingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysBroadcastForwardingEnabled.setStatus("current")
_CLSysLagModeEnabled_Type = TruthValue
_CLSysLagModeEnabled_Object = MibScalar
cLSysLagModeEnabled = _CLSysLagModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 10),
    _CLSysLagModeEnabled_Type()
)
cLSysLagModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysLagModeEnabled.setStatus("current")
_ClsConfigProductBranchVersion_Type = DisplayString
_ClsConfigProductBranchVersion_Object = MibScalar
clsConfigProductBranchVersion = _ClsConfigProductBranchVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 11),
    _ClsConfigProductBranchVersion_Type()
)
clsConfigProductBranchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsConfigProductBranchVersion.setStatus("current")


class _ClsConfigDhcpProxyEnabled_Type(TruthValue):
    """Custom type clsConfigDhcpProxyEnabled based on TruthValue"""


_ClsConfigDhcpProxyEnabled_Object = MibScalar
clsConfigDhcpProxyEnabled = _ClsConfigDhcpProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 12),
    _ClsConfigDhcpProxyEnabled_Type()
)
clsConfigDhcpProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigDhcpProxyEnabled.setStatus("current")
_CLSysMulticastIGMP_ObjectIdentity = ObjectIdentity
cLSysMulticastIGMP = _CLSysMulticastIGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13)
)


class _CLSysMulticastIGMPSnoopingEnabled_Type(TruthValue):
    """Custom type cLSysMulticastIGMPSnoopingEnabled based on TruthValue"""


_CLSysMulticastIGMPSnoopingEnabled_Object = MibScalar
cLSysMulticastIGMPSnoopingEnabled = _CLSysMulticastIGMPSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13, 1),
    _CLSysMulticastIGMPSnoopingEnabled_Type()
)
cLSysMulticastIGMPSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPSnoopingEnabled.setStatus("current")
_CLSysMulticastIGMPSnoopingTimeout_Type = Unsigned32
_CLSysMulticastIGMPSnoopingTimeout_Object = MibScalar
cLSysMulticastIGMPSnoopingTimeout = _CLSysMulticastIGMPSnoopingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13, 2),
    _CLSysMulticastIGMPSnoopingTimeout_Type()
)
cLSysMulticastIGMPSnoopingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPSnoopingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPSnoopingTimeout.setUnits("Seconds")
_CLSysMulticastIGMPQueryInterval_Type = Unsigned32
_CLSysMulticastIGMPQueryInterval_Object = MibScalar
cLSysMulticastIGMPQueryInterval = _CLSysMulticastIGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 13, 3),
    _CLSysMulticastIGMPQueryInterval_Type()
)
cLSysMulticastIGMPQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastIGMPQueryInterval.setUnits("Seconds")
_CLSPortModeConfig_ObjectIdentity = ObjectIdentity
cLSPortModeConfig = _CLSPortModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14)
)
_ClsPortModeConfigTable_Object = MibTable
clsPortModeConfigTable = _ClsPortModeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    clsPortModeConfigTable.setStatus("current")
_ClsPortModeConfigEntry_Object = MibTableRow
clsPortModeConfigEntry = _ClsPortModeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1)
)
clsPortModeConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-SYS-MIB", "clsPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    clsPortModeConfigEntry.setStatus("current")


class _ClsPortDot1dBasePort_Type(Unsigned32):
    """Custom type clsPortDot1dBasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClsPortDot1dBasePort_Type.__name__ = "Unsigned32"
_ClsPortDot1dBasePort_Object = MibTableColumn
clsPortDot1dBasePort = _ClsPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 1),
    _ClsPortDot1dBasePort_Type()
)
clsPortDot1dBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsPortDot1dBasePort.setStatus("current")


class _ClsPortModePhysicalMode_Type(Integer32):
    """Custom type clsPortModePhysicalMode based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("full10", 3),
          ("full100", 5),
          ("full1000", 8),
          ("full10000", 10),
          ("full1000sx", 6),
          ("half10", 2),
          ("half100", 4),
          ("half1000", 7),
          ("half10000", 9))
    )


_ClsPortModePhysicalMode_Type.__name__ = "Integer32"
_ClsPortModePhysicalMode_Object = MibTableColumn
clsPortModePhysicalMode = _ClsPortModePhysicalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 2),
    _ClsPortModePhysicalMode_Type()
)
clsPortModePhysicalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsPortModePhysicalMode.setStatus("current")


class _ClsPortModePhysicalStatus_Type(Integer32):
    """Custom type clsPortModePhysicalStatus based on Integer32"""
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
        *(("autonegotiate", 2),
          ("full10", 4),
          ("full100", 6),
          ("full1000", 9),
          ("full10000", 11),
          ("full1000sx", 7),
          ("half10", 3),
          ("half100", 5),
          ("half1000", 8),
          ("half10000", 10),
          ("unknown", 1))
    )


_ClsPortModePhysicalStatus_Type.__name__ = "Integer32"
_ClsPortModePhysicalStatus_Object = MibTableColumn
clsPortModePhysicalStatus = _ClsPortModePhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 3),
    _ClsPortModePhysicalStatus_Type()
)
clsPortModePhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortModePhysicalStatus.setStatus("current")
_ClsPortModeSfpType_Type = SnmpAdminString
_ClsPortModeSfpType_Object = MibTableColumn
clsPortModeSfpType = _ClsPortModeSfpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 4),
    _ClsPortModeSfpType_Type()
)
clsPortModeSfpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortModeSfpType.setStatus("current")
_ClsPortUpDownCount_Type = Counter32
_ClsPortUpDownCount_Object = MibTableColumn
clsPortUpDownCount = _ClsPortUpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 14, 1, 1, 5),
    _ClsPortUpDownCount_Type()
)
clsPortUpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortUpDownCount.setStatus("current")
_ClsCoreDump_ObjectIdentity = ObjectIdentity
clsCoreDump = _ClsCoreDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15)
)


class _ClsCoreDumpTransferEnable_Type(TruthValue):
    """Custom type clsCoreDumpTransferEnable based on TruthValue"""


_ClsCoreDumpTransferEnable_Object = MibScalar
clsCoreDumpTransferEnable = _ClsCoreDumpTransferEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 1),
    _ClsCoreDumpTransferEnable_Type()
)
clsCoreDumpTransferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpTransferEnable.setStatus("current")


class _ClsCoreDumpTransferMode_Type(Integer32):
    """Custom type clsCoreDumpTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("unknown", 1))
    )


_ClsCoreDumpTransferMode_Type.__name__ = "Integer32"
_ClsCoreDumpTransferMode_Object = MibScalar
clsCoreDumpTransferMode = _ClsCoreDumpTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 2),
    _ClsCoreDumpTransferMode_Type()
)
clsCoreDumpTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpTransferMode.setStatus("current")
_ClsCoreDumpServerIPAddressType_Type = InetAddressType
_ClsCoreDumpServerIPAddressType_Object = MibScalar
clsCoreDumpServerIPAddressType = _ClsCoreDumpServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 3),
    _ClsCoreDumpServerIPAddressType_Type()
)
clsCoreDumpServerIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpServerIPAddressType.setStatus("current")
_ClsCoreDumpServerIPAddress_Type = InetAddress
_ClsCoreDumpServerIPAddress_Object = MibScalar
clsCoreDumpServerIPAddress = _ClsCoreDumpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 4),
    _ClsCoreDumpServerIPAddress_Type()
)
clsCoreDumpServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpServerIPAddress.setStatus("current")
_ClsCoreDumpFileName_Type = SnmpAdminString
_ClsCoreDumpFileName_Object = MibScalar
clsCoreDumpFileName = _ClsCoreDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 5),
    _ClsCoreDumpFileName_Type()
)
clsCoreDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpFileName.setStatus("current")
_ClsCoreDumpUserName_Type = SnmpAdminString
_ClsCoreDumpUserName_Object = MibScalar
clsCoreDumpUserName = _ClsCoreDumpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 6),
    _ClsCoreDumpUserName_Type()
)
clsCoreDumpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpUserName.setStatus("current")
_ClsCoreDumpPassword_Type = SnmpAdminString
_ClsCoreDumpPassword_Object = MibScalar
clsCoreDumpPassword = _ClsCoreDumpPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 15, 7),
    _ClsCoreDumpPassword_Type()
)
clsCoreDumpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCoreDumpPassword.setStatus("current")


class _ClsConfigMulticastEnabled_Type(TruthValue):
    """Custom type clsConfigMulticastEnabled based on TruthValue"""


_ClsConfigMulticastEnabled_Object = MibScalar
clsConfigMulticastEnabled = _ClsConfigMulticastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 16),
    _ClsConfigMulticastEnabled_Type()
)
clsConfigMulticastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsConfigMulticastEnabled.setStatus("current")
_CLSysMulticastMLD_ObjectIdentity = ObjectIdentity
cLSysMulticastMLD = _CLSysMulticastMLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17)
)


class _CLSysMulticastMLDSnoopingEnabled_Type(TruthValue):
    """Custom type cLSysMulticastMLDSnoopingEnabled based on TruthValue"""


_CLSysMulticastMLDSnoopingEnabled_Object = MibScalar
cLSysMulticastMLDSnoopingEnabled = _CLSysMulticastMLDSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17, 1),
    _CLSysMulticastMLDSnoopingEnabled_Type()
)
cLSysMulticastMLDSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastMLDSnoopingEnabled.setStatus("current")
_CLSysMulticastMLDSnoopingTimeout_Type = Unsigned32
_CLSysMulticastMLDSnoopingTimeout_Object = MibScalar
cLSysMulticastMLDSnoopingTimeout = _CLSysMulticastMLDSnoopingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17, 2),
    _CLSysMulticastMLDSnoopingTimeout_Type()
)
cLSysMulticastMLDSnoopingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastMLDSnoopingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastMLDSnoopingTimeout.setUnits("Seconds")
_CLSysMulticastMLDQueryInterval_Type = Unsigned32
_CLSysMulticastMLDQueryInterval_Object = MibScalar
cLSysMulticastMLDQueryInterval = _CLSysMulticastMLDQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 17, 3),
    _CLSysMulticastMLDQueryInterval_Type()
)
cLSysMulticastMLDQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSysMulticastMLDQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLSysMulticastMLDQueryInterval.setUnits("Seconds")
_ClsConfigStats_ObjectIdentity = ObjectIdentity
clsConfigStats = _ClsConfigStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18)
)


class _ClsSysRealtimeStatsTimer_Type(Unsigned32):
    """Custom type clsSysRealtimeStatsTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ClsSysRealtimeStatsTimer_Type.__name__ = "Unsigned32"
_ClsSysRealtimeStatsTimer_Object = MibScalar
clsSysRealtimeStatsTimer = _ClsSysRealtimeStatsTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 1),
    _ClsSysRealtimeStatsTimer_Type()
)
clsSysRealtimeStatsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysRealtimeStatsTimer.setStatus("current")
if mibBuilder.loadTexts:
    clsSysRealtimeStatsTimer.setUnits("Seconds")


class _ClsSysNormalStatsTimer_Type(Unsigned32):
    """Custom type clsSysNormalStatsTimer based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_ClsSysNormalStatsTimer_Type.__name__ = "Unsigned32"
_ClsSysNormalStatsTimer_Object = MibScalar
clsSysNormalStatsTimer = _ClsSysNormalStatsTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 2),
    _ClsSysNormalStatsTimer_Type()
)
clsSysNormalStatsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysNormalStatsTimer.setStatus("current")
if mibBuilder.loadTexts:
    clsSysNormalStatsTimer.setUnits("Seconds")
_ClsSysStatsSamplingInterval_Type = Unsigned32
_ClsSysStatsSamplingInterval_Object = MibScalar
clsSysStatsSamplingInterval = _ClsSysStatsSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 3),
    _ClsSysStatsSamplingInterval_Type()
)
clsSysStatsSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysStatsSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsSysStatsSamplingInterval.setUnits("Seconds")
_ClsSysStatsAverageInterval_Type = Unsigned32
_ClsSysStatsAverageInterval_Object = MibScalar
clsSysStatsAverageInterval = _ClsSysStatsAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 18, 4),
    _ClsSysStatsAverageInterval_Type()
)
clsSysStatsAverageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysStatsAverageInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsSysStatsAverageInterval.setUnits("Seconds")
_ClsAlarmObjects_ObjectIdentity = ObjectIdentity
clsAlarmObjects = _ClsAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 19)
)


class _ClsAlarmHoldTime_Type(Unsigned32):
    """Custom type clsAlarmHoldTime based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ClsAlarmHoldTime_Type.__name__ = "Unsigned32"
_ClsAlarmHoldTime_Object = MibScalar
clsAlarmHoldTime = _ClsAlarmHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 19, 1),
    _ClsAlarmHoldTime_Type()
)
clsAlarmHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsAlarmHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    clsAlarmHoldTime.setUnits("second")


class _ClsAlarmTrapRetransmitInterval_Type(Unsigned32):
    """Custom type clsAlarmTrapRetransmitInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClsAlarmTrapRetransmitInterval_Type.__name__ = "Unsigned32"
_ClsAlarmTrapRetransmitInterval_Object = MibScalar
clsAlarmTrapRetransmitInterval = _ClsAlarmTrapRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 19, 2),
    _ClsAlarmTrapRetransmitInterval_Type()
)
clsAlarmTrapRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsAlarmTrapRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsAlarmTrapRetransmitInterval.setUnits("second")
_ClsSysThresholdConfig_ObjectIdentity = ObjectIdentity
clsSysThresholdConfig = _ClsSysThresholdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20)
)


class _ClsSysControllerCpuUsageThreshold_Type(Unsigned32):
    """Custom type clsSysControllerCpuUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysControllerCpuUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysControllerCpuUsageThreshold_Object = MibScalar
clsSysControllerCpuUsageThreshold = _ClsSysControllerCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 1),
    _ClsSysControllerCpuUsageThreshold_Type()
)
clsSysControllerCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysControllerCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysControllerCpuUsageThreshold.setUnits("Percent")


class _ClsSysControllerMemoryUsageThreshold_Type(Unsigned32):
    """Custom type clsSysControllerMemoryUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysControllerMemoryUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysControllerMemoryUsageThreshold_Object = MibScalar
clsSysControllerMemoryUsageThreshold = _ClsSysControllerMemoryUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 2),
    _ClsSysControllerMemoryUsageThreshold_Type()
)
clsSysControllerMemoryUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysControllerMemoryUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysControllerMemoryUsageThreshold.setUnits("Percent")


class _ClsSysApCpuUsageThreshold_Type(Unsigned32):
    """Custom type clsSysApCpuUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysApCpuUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysApCpuUsageThreshold_Object = MibScalar
clsSysApCpuUsageThreshold = _ClsSysApCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 3),
    _ClsSysApCpuUsageThreshold_Type()
)
clsSysApCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysApCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysApCpuUsageThreshold.setUnits("Percent")


class _ClsSysApMemoryUsageThreshold_Type(Unsigned32):
    """Custom type clsSysApMemoryUsageThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClsSysApMemoryUsageThreshold_Type.__name__ = "Unsigned32"
_ClsSysApMemoryUsageThreshold_Object = MibScalar
clsSysApMemoryUsageThreshold = _ClsSysApMemoryUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 20, 4),
    _ClsSysApMemoryUsageThreshold_Type()
)
clsSysApMemoryUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysApMemoryUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clsSysApMemoryUsageThreshold.setUnits("Percent")
_ClsNMHeartBeat_ObjectIdentity = ObjectIdentity
clsNMHeartBeat = _ClsNMHeartBeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 21)
)


class _ClsNMHeartBeatEnable_Type(TruthValue):
    """Custom type clsNMHeartBeatEnable based on TruthValue"""


_ClsNMHeartBeatEnable_Object = MibScalar
clsNMHeartBeatEnable = _ClsNMHeartBeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 21, 1),
    _ClsNMHeartBeatEnable_Type()
)
clsNMHeartBeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNMHeartBeatEnable.setStatus("current")


class _ClsNMHeartBeatInterval_Type(Unsigned32):
    """Custom type clsNMHeartBeatInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClsNMHeartBeatInterval_Type.__name__ = "Unsigned32"
_ClsNMHeartBeatInterval_Object = MibScalar
clsNMHeartBeatInterval = _ClsNMHeartBeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 21, 2),
    _ClsNMHeartBeatInterval_Type()
)
clsNMHeartBeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsNMHeartBeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    clsNMHeartBeatInterval.setUnits("Seconds")
_ClsCrashSystem_Type = TruthValue
_ClsCrashSystem_Object = MibScalar
clsCrashSystem = _ClsCrashSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 1, 99),
    _ClsCrashSystem_Type()
)
clsCrashSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsCrashSystem.setStatus("current")
_ClsStatus_ObjectIdentity = ObjectIdentity
clsStatus = _ClsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2)
)
_CLSysLagModeInTransition_Type = TruthValue
_CLSysLagModeInTransition_Object = MibScalar
cLSysLagModeInTransition = _CLSysLagModeInTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 2, 1),
    _CLSysLagModeInTransition_Type()
)
cLSysLagModeInTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSysLagModeInTransition.setStatus("current")
_ClsImageInfo_ObjectIdentity = ObjectIdentity
clsImageInfo = _ClsImageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 3)
)
_ClsEmergencyImageVersion_Type = DisplayString
_ClsEmergencyImageVersion_Object = MibScalar
clsEmergencyImageVersion = _ClsEmergencyImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 3, 1),
    _ClsEmergencyImageVersion_Type()
)
clsEmergencyImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsEmergencyImageVersion.setStatus("current")
_ClsCpuInfo_ObjectIdentity = ObjectIdentity
clsCpuInfo = _ClsCpuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 4)
)
_ClsAllCpuUsage_Type = DisplayString
_ClsAllCpuUsage_Object = MibScalar
clsAllCpuUsage = _ClsAllCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 4, 1),
    _ClsAllCpuUsage_Type()
)
clsAllCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsAllCpuUsage.setStatus("current")
_ClsSecurityGroup_ObjectIdentity = ObjectIdentity
clsSecurityGroup = _ClsSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5)
)
_ClsSecStrongPwdCaseCheck_Type = TruthValue
_ClsSecStrongPwdCaseCheck_Object = MibScalar
clsSecStrongPwdCaseCheck = _ClsSecStrongPwdCaseCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 1),
    _ClsSecStrongPwdCaseCheck_Type()
)
clsSecStrongPwdCaseCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdCaseCheck.setStatus("current")
_ClsSecStrongPwdConsecutiveCheck_Type = TruthValue
_ClsSecStrongPwdConsecutiveCheck_Object = MibScalar
clsSecStrongPwdConsecutiveCheck = _ClsSecStrongPwdConsecutiveCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 2),
    _ClsSecStrongPwdConsecutiveCheck_Type()
)
clsSecStrongPwdConsecutiveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdConsecutiveCheck.setStatus("current")
_ClsSecStrongPwdDefaultCheck_Type = TruthValue
_ClsSecStrongPwdDefaultCheck_Object = MibScalar
clsSecStrongPwdDefaultCheck = _ClsSecStrongPwdDefaultCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 3),
    _ClsSecStrongPwdDefaultCheck_Type()
)
clsSecStrongPwdDefaultCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdDefaultCheck.setStatus("current")
_ClsSecStrongPwdAsUserNameCheck_Type = TruthValue
_ClsSecStrongPwdAsUserNameCheck_Object = MibScalar
clsSecStrongPwdAsUserNameCheck = _ClsSecStrongPwdAsUserNameCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 5, 4),
    _ClsSecStrongPwdAsUserNameCheck_Type()
)
clsSecStrongPwdAsUserNameCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdAsUserNameCheck.setStatus("current")
_CiscoLwappSysMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBNotifObjects = _CiscoLwappSysMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6)
)


class _ClsSecStrongPwdManagementUser_Type(OctetString):
    """Custom type clsSecStrongPwdManagementUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_ClsSecStrongPwdManagementUser_Type.__name__ = "OctetString"
_ClsSecStrongPwdManagementUser_Object = MibScalar
clsSecStrongPwdManagementUser = _ClsSecStrongPwdManagementUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 1),
    _ClsSecStrongPwdManagementUser_Type()
)
clsSecStrongPwdManagementUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsSecStrongPwdManagementUser.setStatus("current")


class _ClsSecStrongPwdCheckType_Type(Integer32):
    """Custom type clsSecStrongPwdCheckType based on Integer32"""
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
        *(("allChecks", 5),
          ("caseCheck", 1),
          ("consecutiveCheck", 2),
          ("defaultCheck", 3),
          ("usernameCheck", 4))
    )


_ClsSecStrongPwdCheckType_Type.__name__ = "Integer32"
_ClsSecStrongPwdCheckType_Object = MibScalar
clsSecStrongPwdCheckType = _ClsSecStrongPwdCheckType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 2),
    _ClsSecStrongPwdCheckType_Type()
)
clsSecStrongPwdCheckType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsSecStrongPwdCheckType.setStatus("current")
_ClsSecStrongPwdCheckOption_Type = TruthValue
_ClsSecStrongPwdCheckOption_Object = MibScalar
clsSecStrongPwdCheckOption = _ClsSecStrongPwdCheckOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 3),
    _ClsSecStrongPwdCheckOption_Type()
)
clsSecStrongPwdCheckOption.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsSecStrongPwdCheckOption.setStatus("current")
_ClsSysAlarmSet_Type = TruthValue
_ClsSysAlarmSet_Object = MibScalar
clsSysAlarmSet = _ClsSysAlarmSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 6, 4),
    _ClsSysAlarmSet_Type()
)
clsSysAlarmSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clsSysAlarmSet.setStatus("current")
_CiscoLwappSysMIBNotifControlObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBNotifControlObjects = _CiscoLwappSysMIBNotifControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7)
)


class _ClsSecStrongPwdCheckTrapEnabled_Type(TruthValue):
    """Custom type clsSecStrongPwdCheckTrapEnabled based on TruthValue"""


_ClsSecStrongPwdCheckTrapEnabled_Object = MibScalar
clsSecStrongPwdCheckTrapEnabled = _ClsSecStrongPwdCheckTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 1),
    _ClsSecStrongPwdCheckTrapEnabled_Type()
)
clsSecStrongPwdCheckTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSecStrongPwdCheckTrapEnabled.setStatus("current")


class _ClsMaxClientsTrapEnabled_Type(TruthValue):
    """Custom type clsMaxClientsTrapEnabled based on TruthValue"""


_ClsMaxClientsTrapEnabled_Object = MibScalar
clsMaxClientsTrapEnabled = _ClsMaxClientsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 2),
    _ClsMaxClientsTrapEnabled_Type()
)
clsMaxClientsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxClientsTrapEnabled.setStatus("current")


class _ClsMaxRFIDTagsTrapEnabled_Type(TruthValue):
    """Custom type clsMaxRFIDTagsTrapEnabled based on TruthValue"""


_ClsMaxRFIDTagsTrapEnabled_Object = MibScalar
clsMaxRFIDTagsTrapEnabled = _ClsMaxRFIDTagsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 7, 3),
    _ClsMaxRFIDTagsTrapEnabled_Type()
)
clsMaxRFIDTagsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsTrapEnabled.setStatus("current")
_ClsSysInfo_ObjectIdentity = ObjectIdentity
clsSysInfo = _ClsSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8)
)
_ClsSysFlashSize_Type = Unsigned32
_ClsSysFlashSize_Object = MibScalar
clsSysFlashSize = _ClsSysFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 1),
    _ClsSysFlashSize_Type()
)
clsSysFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysFlashSize.setStatus("current")
_ClsSysMemoryType_Type = DisplayString
_ClsSysMemoryType_Object = MibScalar
clsSysMemoryType = _ClsSysMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 2),
    _ClsSysMemoryType_Type()
)
clsSysMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysMemoryType.setStatus("current")
_ClsSysMaxClients_Type = Unsigned32
_ClsSysMaxClients_Object = MibScalar
clsSysMaxClients = _ClsSysMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 3),
    _ClsSysMaxClients_Type()
)
clsSysMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysMaxClients.setStatus("current")
_ClsSysApConnectCount_Type = Unsigned32
_ClsSysApConnectCount_Object = MibScalar
clsSysApConnectCount = _ClsSysApConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 4),
    _ClsSysApConnectCount_Type()
)
clsSysApConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysApConnectCount.setStatus("current")


class _ClsSysNetId_Type(SnmpAdminString):
    """Custom type clsSysNetId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClsSysNetId_Type.__name__ = "SnmpAdminString"
_ClsSysNetId_Object = MibScalar
clsSysNetId = _ClsSysNetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 5),
    _ClsSysNetId_Type()
)
clsSysNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsSysNetId.setStatus("current")
_ClsSysCurrentMemoryUsage_Type = Unsigned32
_ClsSysCurrentMemoryUsage_Object = MibScalar
clsSysCurrentMemoryUsage = _ClsSysCurrentMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 6),
    _ClsSysCurrentMemoryUsage_Type()
)
clsSysCurrentMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysCurrentMemoryUsage.setStatus("current")
_ClsSysAverageMemoryUsage_Type = Unsigned32
_ClsSysAverageMemoryUsage_Object = MibScalar
clsSysAverageMemoryUsage = _ClsSysAverageMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 7),
    _ClsSysAverageMemoryUsage_Type()
)
clsSysAverageMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysAverageMemoryUsage.setStatus("current")
_ClsSysCurrentCpuUsage_Type = Unsigned32
_ClsSysCurrentCpuUsage_Object = MibScalar
clsSysCurrentCpuUsage = _ClsSysCurrentCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 8),
    _ClsSysCurrentCpuUsage_Type()
)
clsSysCurrentCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysCurrentCpuUsage.setStatus("current")
_ClsSysAverageCpuUsage_Type = Unsigned32
_ClsSysAverageCpuUsage_Object = MibScalar
clsSysAverageCpuUsage = _ClsSysAverageCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 9),
    _ClsSysAverageCpuUsage_Type()
)
clsSysAverageCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysAverageCpuUsage.setStatus("current")
_ClsSysCpuType_Type = DisplayString
_ClsSysCpuType_Object = MibScalar
clsSysCpuType = _ClsSysCpuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 10),
    _ClsSysCpuType_Type()
)
clsSysCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsSysCpuType.setStatus("current")
_ClsMaxRFIDTagsCount_Type = Unsigned32
_ClsMaxRFIDTagsCount_Object = MibScalar
clsMaxRFIDTagsCount = _ClsMaxRFIDTagsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 11),
    _ClsMaxRFIDTagsCount_Type()
)
clsMaxRFIDTagsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsMaxRFIDTagsCount.setStatus("current")
_ClsMaxClientsCount_Type = Unsigned32
_ClsMaxClientsCount_Object = MibScalar
clsMaxClientsCount = _ClsMaxClientsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 1, 8, 12),
    _ClsMaxClientsCount_Type()
)
clsMaxClientsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsMaxClientsCount.setStatus("current")
_CiscoLwappSysMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBConform = _CiscoLwappSysMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2)
)
_CiscoLwappSysMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBCompliances = _CiscoLwappSysMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1)
)
_CiscoLwappSysMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappSysMIBGroups = _CiscoLwappSysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2)
)

# Managed Objects groups

ciscoLwappSysConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 1)
)
ciscoLwappSysConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsDot3BridgeEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsDownloadFileType"),
        ("CISCO-LWAPP-SYS-MIB", "clsDownloadCertificateKey"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadFileType"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadPacUsername"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadPacPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsUploadPacValidity"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysBroadcastForwardingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigProductBranchVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigDhcpProxyEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCrashSystem"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigGroup.setStatus("current")

ciscoLwappSysConfigFileEncryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 2)
)
ciscoLwappSysConfigFileEncryptionGroup.setObjects(
    ("CISCO-LWAPP-SYS-MIB", "clsTransferConfigFileEncryptionKey")
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigFileEncryptionGroup.setStatus("current")

ciscoLwappSysTransferOperationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 3)
)
ciscoLwappSysTransferOperationConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsTransferServerAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferServerAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferPath"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFilename"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFtpUsername"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFtpPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferFtpPortNum"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferTftpMaxRetries"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferTftpTimeout"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStart"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferStatusString"),
        ("CISCO-LWAPP-SYS-MIB", "clsTransferConfigFileEncryption"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysTransferOperationConfigGroup.setStatus("current")

ciscoLwappSysPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 4)
)
ciscoLwappSysPortConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsPortModePhysicalMode"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortModePhysicalStatus"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortModeSfpType"),
        ("CISCO-LWAPP-SYS-MIB", "clsPortUpDownCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysPortConfigGroup.setStatus("current")

ciscoLwappSysSecurityConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 5)
)
ciscoLwappSysSecurityConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCaseCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdConsecutiveCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdDefaultCheck"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdAsUserNameCheck"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysSecurityConfigGroup.setStatus("current")

ciscoLwappSysIgmpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 6)
)
ciscoLwappSysIgmpConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "cLSysMulticastIGMPSnoopingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastIGMPSnoopingTimeout"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastIGMPQueryInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysIgmpConfigGroup.setStatus("current")

ciscoLwappSysSecNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 7)
)
ciscoLwappSysSecNotifObjsGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdManagementUser"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckOption"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAlarmSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysSecNotifObjsGroup.setStatus("current")

ciscoLwappSysNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 9)
)
ciscoLwappSysNotifControlGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckTrapEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsTrapEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsTrapEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysNotifControlGroup.setStatus("current")

ciscoLwappSysConfigGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 10)
)
ciscoLwappSysConfigGroupVer1.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "cLSysBroadcastForwardingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLagModeEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigProductBranchVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigDhcpProxyEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpTransferEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpTransferMode"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpServerIPAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpServerIPAddress"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpFileName"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpUserName"),
        ("CISCO-LWAPP-SYS-MIB", "clsCoreDumpPassword"),
        ("CISCO-LWAPP-SYS-MIB", "clsConfigMulticastEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLagModeInTransition"),
        ("CISCO-LWAPP-SYS-MIB", "clsEmergencyImageVersion"),
        ("CISCO-LWAPP-SYS-MIB", "clsAllCpuUsage"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigGroupVer1.setStatus("current")

ciscoLwappSysConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 11)
)
ciscoLwappSysConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsTimeZone"),
        ("CISCO-LWAPP-SYS-MIB", "clsTimeZoneDescription"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLogAddressType"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLogAddress"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysLogHostRowStatus"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysArpUnicastEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsTrapThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsTrapThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigGroupSup1.setStatus("current")

ciscoLwappSysMldConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 12)
)
ciscoLwappSysMldConfigGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "cLSysMulticastMLDSnoopingEnabled"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastMLDSnoopingTimeout"),
        ("CISCO-LWAPP-SYS-MIB", "cLSysMulticastMLDQueryInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMldConfigGroup.setStatus("current")

ciscoLwappSysConfigStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 13)
)
ciscoLwappSysConfigStatsGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysRealtimeStatsTimer"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysNormalStatsTimer"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysStatsSamplingInterval"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysStatsAverageInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysConfigStatsGroup.setStatus("current")

ciscoLwappSysAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 14)
)
ciscoLwappSysAlarmObjectGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsAlarmHoldTime"),
        ("CISCO-LWAPP-SYS-MIB", "clsAlarmTrapRetransmitInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysAlarmObjectGroup.setStatus("current")

ciscoLwappSysThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 15)
)
ciscoLwappSysThresholdGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysControllerCpuUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysControllerMemoryUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApCpuUsageThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApMemoryUsageThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysThresholdGroup.setStatus("current")

ciscoLwappSysHeartBeatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 16)
)
ciscoLwappSysHeartBeatGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsNMHeartBeatEnable"),
        ("CISCO-LWAPP-SYS-MIB", "clsNMHeartBeatInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysHeartBeatGroup.setStatus("current")

ciscoLwappSysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 17)
)
ciscoLwappSysInfoGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysFlashSize"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysMemoryType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysMaxClients"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysApConnectCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysNetId"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCurrentMemoryUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAverageMemoryUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCurrentCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAverageCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysCpuType"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsCount"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysInfoGroup.setStatus("current")


# Notification objects

ciscoLwappSysInvalidXmlConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappSysInvalidXmlConfig.setStatus(
        "current"
    )

ciscoLwappNoVlanConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 2)
)
ciscoLwappNoVlanConfigured.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAccessVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappNoVlanConfigured.setStatus(
        "current"
    )

ciscoLwappStrongPwdCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 3)
)
ciscoLwappStrongPwdCheck.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdManagementUser"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckType"),
        ("CISCO-LWAPP-SYS-MIB", "clsSecStrongPwdCheckOption"))
)
if mibBuilder.loadTexts:
    ciscoLwappStrongPwdCheck.setStatus(
        "current"
    )

ciscoLwappSysCpuUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 4)
)
ciscoLwappSysCpuUsageHigh.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysCurrentCpuUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAlarmSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysCpuUsageHigh.setStatus(
        "current"
    )

ciscoLwappSysMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 5)
)
ciscoLwappSysMemoryUsageHigh.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsSysCurrentMemoryUsage"),
        ("CISCO-LWAPP-SYS-MIB", "clsSysAlarmSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysMemoryUsageHigh.setStatus(
        "current"
    )

ciscoLwappMaxRFIDTagsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 6)
)
ciscoLwappMaxRFIDTagsReached.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsTrapThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxRFIDTagsCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMaxRFIDTagsReached.setStatus(
        "current"
    )

ciscoLwappMaxClientsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 7)
)
ciscoLwappMaxClientsReached.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "clsMaxClientsTrapThreshold"),
        ("CISCO-LWAPP-SYS-MIB", "clsMaxClientsCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMaxClientsReached.setStatus(
        "current"
    )

ciscoLwappNMHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 0, 8)
)
if mibBuilder.loadTexts:
    ciscoLwappNMHeartBeat.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappSysNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 2, 8)
)
ciscoLwappSysNotifsGroup.setObjects(
      *(("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysInvalidXmlConfig"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappNoVlanConfigured"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappStrongPwdCheck"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysCpuUsageHigh"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappSysMemoryUsageHigh"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappMaxRFIDTagsReached"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappMaxClientsReached"),
        ("CISCO-LWAPP-SYS-MIB", "ciscoLwappNMHeartBeat"))
)
if mibBuilder.loadTexts:
    ciscoLwappSysNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappSysMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappSysMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappSysMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappSysMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 618, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoLwappSysMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-SYS-MIB",
    **{"ciscoLwappSysMIB": ciscoLwappSysMIB,
       "ciscoLwappSysMIBNotifs": ciscoLwappSysMIBNotifs,
       "ciscoLwappSysInvalidXmlConfig": ciscoLwappSysInvalidXmlConfig,
       "ciscoLwappNoVlanConfigured": ciscoLwappNoVlanConfigured,
       "ciscoLwappStrongPwdCheck": ciscoLwappStrongPwdCheck,
       "ciscoLwappSysCpuUsageHigh": ciscoLwappSysCpuUsageHigh,
       "ciscoLwappSysMemoryUsageHigh": ciscoLwappSysMemoryUsageHigh,
       "ciscoLwappMaxRFIDTagsReached": ciscoLwappMaxRFIDTagsReached,
       "ciscoLwappMaxClientsReached": ciscoLwappMaxClientsReached,
       "ciscoLwappNMHeartBeat": ciscoLwappNMHeartBeat,
       "ciscoLwappSysMIBObjects": ciscoLwappSysMIBObjects,
       "clsConfig": clsConfig,
       "clsDot3BridgeEnabled": clsDot3BridgeEnabled,
       "clsConfigDownload": clsConfigDownload,
       "clsDownloadFileType": clsDownloadFileType,
       "clsDownloadCertificateKey": clsDownloadCertificateKey,
       "clsConfigUpload": clsConfigUpload,
       "clsUploadFileType": clsUploadFileType,
       "clsUploadPacUsername": clsUploadPacUsername,
       "clsUploadPacPassword": clsUploadPacPassword,
       "clsUploadPacValidity": clsUploadPacValidity,
       "clsTransferConfigGroup": clsTransferConfigGroup,
       "clsTransferConfigFileEncryption": clsTransferConfigFileEncryption,
       "clsTransferConfigFileEncryptionKey": clsTransferConfigFileEncryptionKey,
       "clsConfigGeneral": clsConfigGeneral,
       "clsTimeZone": clsTimeZone,
       "clsTimeZoneDescription": clsTimeZoneDescription,
       "clsMaxClientsTrapThreshold": clsMaxClientsTrapThreshold,
       "clsMaxRFIDTagsTrapThreshold": clsMaxRFIDTagsTrapThreshold,
       "clsSyslogIpConfig": clsSyslogIpConfig,
       "cLSysLogConfigTable": cLSysLogConfigTable,
       "cLSysLogConfigEntry": cLSysLogConfigEntry,
       "cLSysLogServerIndex": cLSysLogServerIndex,
       "cLSysLogAddressType": cLSysLogAddressType,
       "cLSysLogAddress": cLSysLogAddress,
       "cLSysLogHostRowStatus": cLSysLogHostRowStatus,
       "cLSysArpUnicastEnabled": cLSysArpUnicastEnabled,
       "clsTransferConfig": clsTransferConfig,
       "clsTransferConfigTable": clsTransferConfigTable,
       "clsTransferConfigEntry": clsTransferConfigEntry,
       "clsTransferType": clsTransferType,
       "clsTransferMode": clsTransferMode,
       "clsTransferServerAddressType": clsTransferServerAddressType,
       "clsTransferServerAddress": clsTransferServerAddress,
       "clsTransferPath": clsTransferPath,
       "clsTransferFilename": clsTransferFilename,
       "clsTransferFtpUsername": clsTransferFtpUsername,
       "clsTransferFtpPassword": clsTransferFtpPassword,
       "clsTransferFtpPortNum": clsTransferFtpPortNum,
       "clsTransferTftpMaxRetries": clsTransferTftpMaxRetries,
       "clsTransferTftpTimeout": clsTransferTftpTimeout,
       "clsTransferStart": clsTransferStart,
       "clsTransferStatus": clsTransferStatus,
       "clsTransferStatusString": clsTransferStatusString,
       "cLSysBroadcastForwardingEnabled": cLSysBroadcastForwardingEnabled,
       "cLSysLagModeEnabled": cLSysLagModeEnabled,
       "clsConfigProductBranchVersion": clsConfigProductBranchVersion,
       "clsConfigDhcpProxyEnabled": clsConfigDhcpProxyEnabled,
       "cLSysMulticastIGMP": cLSysMulticastIGMP,
       "cLSysMulticastIGMPSnoopingEnabled": cLSysMulticastIGMPSnoopingEnabled,
       "cLSysMulticastIGMPSnoopingTimeout": cLSysMulticastIGMPSnoopingTimeout,
       "cLSysMulticastIGMPQueryInterval": cLSysMulticastIGMPQueryInterval,
       "cLSPortModeConfig": cLSPortModeConfig,
       "clsPortModeConfigTable": clsPortModeConfigTable,
       "clsPortModeConfigEntry": clsPortModeConfigEntry,
       "clsPortDot1dBasePort": clsPortDot1dBasePort,
       "clsPortModePhysicalMode": clsPortModePhysicalMode,
       "clsPortModePhysicalStatus": clsPortModePhysicalStatus,
       "clsPortModeSfpType": clsPortModeSfpType,
       "clsPortUpDownCount": clsPortUpDownCount,
       "clsCoreDump": clsCoreDump,
       "clsCoreDumpTransferEnable": clsCoreDumpTransferEnable,
       "clsCoreDumpTransferMode": clsCoreDumpTransferMode,
       "clsCoreDumpServerIPAddressType": clsCoreDumpServerIPAddressType,
       "clsCoreDumpServerIPAddress": clsCoreDumpServerIPAddress,
       "clsCoreDumpFileName": clsCoreDumpFileName,
       "clsCoreDumpUserName": clsCoreDumpUserName,
       "clsCoreDumpPassword": clsCoreDumpPassword,
       "clsConfigMulticastEnabled": clsConfigMulticastEnabled,
       "cLSysMulticastMLD": cLSysMulticastMLD,
       "cLSysMulticastMLDSnoopingEnabled": cLSysMulticastMLDSnoopingEnabled,
       "cLSysMulticastMLDSnoopingTimeout": cLSysMulticastMLDSnoopingTimeout,
       "cLSysMulticastMLDQueryInterval": cLSysMulticastMLDQueryInterval,
       "clsConfigStats": clsConfigStats,
       "clsSysRealtimeStatsTimer": clsSysRealtimeStatsTimer,
       "clsSysNormalStatsTimer": clsSysNormalStatsTimer,
       "clsSysStatsSamplingInterval": clsSysStatsSamplingInterval,
       "clsSysStatsAverageInterval": clsSysStatsAverageInterval,
       "clsAlarmObjects": clsAlarmObjects,
       "clsAlarmHoldTime": clsAlarmHoldTime,
       "clsAlarmTrapRetransmitInterval": clsAlarmTrapRetransmitInterval,
       "clsSysThresholdConfig": clsSysThresholdConfig,
       "clsSysControllerCpuUsageThreshold": clsSysControllerCpuUsageThreshold,
       "clsSysControllerMemoryUsageThreshold": clsSysControllerMemoryUsageThreshold,
       "clsSysApCpuUsageThreshold": clsSysApCpuUsageThreshold,
       "clsSysApMemoryUsageThreshold": clsSysApMemoryUsageThreshold,
       "clsNMHeartBeat": clsNMHeartBeat,
       "clsNMHeartBeatEnable": clsNMHeartBeatEnable,
       "clsNMHeartBeatInterval": clsNMHeartBeatInterval,
       "clsCrashSystem": clsCrashSystem,
       "clsStatus": clsStatus,
       "cLSysLagModeInTransition": cLSysLagModeInTransition,
       "clsImageInfo": clsImageInfo,
       "clsEmergencyImageVersion": clsEmergencyImageVersion,
       "clsCpuInfo": clsCpuInfo,
       "clsAllCpuUsage": clsAllCpuUsage,
       "clsSecurityGroup": clsSecurityGroup,
       "clsSecStrongPwdCaseCheck": clsSecStrongPwdCaseCheck,
       "clsSecStrongPwdConsecutiveCheck": clsSecStrongPwdConsecutiveCheck,
       "clsSecStrongPwdDefaultCheck": clsSecStrongPwdDefaultCheck,
       "clsSecStrongPwdAsUserNameCheck": clsSecStrongPwdAsUserNameCheck,
       "ciscoLwappSysMIBNotifObjects": ciscoLwappSysMIBNotifObjects,
       "clsSecStrongPwdManagementUser": clsSecStrongPwdManagementUser,
       "clsSecStrongPwdCheckType": clsSecStrongPwdCheckType,
       "clsSecStrongPwdCheckOption": clsSecStrongPwdCheckOption,
       "clsSysAlarmSet": clsSysAlarmSet,
       "ciscoLwappSysMIBNotifControlObjects": ciscoLwappSysMIBNotifControlObjects,
       "clsSecStrongPwdCheckTrapEnabled": clsSecStrongPwdCheckTrapEnabled,
       "clsMaxClientsTrapEnabled": clsMaxClientsTrapEnabled,
       "clsMaxRFIDTagsTrapEnabled": clsMaxRFIDTagsTrapEnabled,
       "clsSysInfo": clsSysInfo,
       "clsSysFlashSize": clsSysFlashSize,
       "clsSysMemoryType": clsSysMemoryType,
       "clsSysMaxClients": clsSysMaxClients,
       "clsSysApConnectCount": clsSysApConnectCount,
       "clsSysNetId": clsSysNetId,
       "clsSysCurrentMemoryUsage": clsSysCurrentMemoryUsage,
       "clsSysAverageMemoryUsage": clsSysAverageMemoryUsage,
       "clsSysCurrentCpuUsage": clsSysCurrentCpuUsage,
       "clsSysAverageCpuUsage": clsSysAverageCpuUsage,
       "clsSysCpuType": clsSysCpuType,
       "clsMaxRFIDTagsCount": clsMaxRFIDTagsCount,
       "clsMaxClientsCount": clsMaxClientsCount,
       "ciscoLwappSysMIBConform": ciscoLwappSysMIBConform,
       "ciscoLwappSysMIBCompliances": ciscoLwappSysMIBCompliances,
       "ciscoLwappSysMIBCompliance": ciscoLwappSysMIBCompliance,
       "ciscoLwappSysMIBComplianceRev1": ciscoLwappSysMIBComplianceRev1,
       "ciscoLwappSysMIBComplianceRev2": ciscoLwappSysMIBComplianceRev2,
       "ciscoLwappSysMIBComplianceRev3": ciscoLwappSysMIBComplianceRev3,
       "ciscoLwappSysMIBGroups": ciscoLwappSysMIBGroups,
       "ciscoLwappSysConfigGroup": ciscoLwappSysConfigGroup,
       "ciscoLwappSysConfigFileEncryptionGroup": ciscoLwappSysConfigFileEncryptionGroup,
       "ciscoLwappSysTransferOperationConfigGroup": ciscoLwappSysTransferOperationConfigGroup,
       "ciscoLwappSysPortConfigGroup": ciscoLwappSysPortConfigGroup,
       "ciscoLwappSysSecurityConfigGroup": ciscoLwappSysSecurityConfigGroup,
       "ciscoLwappSysIgmpConfigGroup": ciscoLwappSysIgmpConfigGroup,
       "ciscoLwappSysSecNotifObjsGroup": ciscoLwappSysSecNotifObjsGroup,
       "ciscoLwappSysNotifsGroup": ciscoLwappSysNotifsGroup,
       "ciscoLwappSysNotifControlGroup": ciscoLwappSysNotifControlGroup,
       "ciscoLwappSysConfigGroupVer1": ciscoLwappSysConfigGroupVer1,
       "ciscoLwappSysConfigGroupSup1": ciscoLwappSysConfigGroupSup1,
       "ciscoLwappSysMldConfigGroup": ciscoLwappSysMldConfigGroup,
       "ciscoLwappSysConfigStatsGroup": ciscoLwappSysConfigStatsGroup,
       "ciscoLwappSysAlarmObjectGroup": ciscoLwappSysAlarmObjectGroup,
       "ciscoLwappSysThresholdGroup": ciscoLwappSysThresholdGroup,
       "ciscoLwappSysHeartBeatGroup": ciscoLwappSysHeartBeatGroup,
       "ciscoLwappSysInfoGroup": ciscoLwappSysInfoGroup}
)
