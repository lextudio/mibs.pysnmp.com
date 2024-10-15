# SNMP MIB module (AVAYA-LOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-LOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:32 2024
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

(avGatewayMibs,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "avGatewayMibs")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

avLoad = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AvLoadItuPerceivedSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AvLoadNotification_ObjectIdentity = ObjectIdentity
avLoadNotification = _AvLoadNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 0)
)
_AvGenOperations_ObjectIdentity = ObjectIdentity
avGenOperations = _AvGenOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1)
)
_AvGenLoadNumberOfSession_Type = Integer32
_AvGenLoadNumberOfSession_Object = MibScalar
avGenLoadNumberOfSession = _AvGenLoadNumberOfSession_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 1),
    _AvGenLoadNumberOfSession_Type()
)
avGenLoadNumberOfSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenLoadNumberOfSession.setStatus("current")
_AvGenOpTable_Object = MibTable
avGenOpTable = _AvGenOpTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    avGenOpTable.setStatus("current")
_AvGenOpEntry_Object = MibTableRow
avGenOpEntry = _AvGenOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1)
)
avGenOpEntry.setIndexNames(
    (0, "AVAYA-LOAD-MIB", "avGenOpModuleId"),
    (0, "AVAYA-LOAD-MIB", "avGenOpIndex"),
)
if mibBuilder.loadTexts:
    avGenOpEntry.setStatus("current")


class _AvGenOpModuleId_Type(Integer32):
    """Custom type avGenOpModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AvGenOpModuleId_Type.__name__ = "Integer32"
_AvGenOpModuleId_Object = MibTableColumn
avGenOpModuleId = _AvGenOpModuleId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 1),
    _AvGenOpModuleId_Type()
)
avGenOpModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpModuleId.setStatus("current")


class _AvGenOpIndex_Type(Integer32):
    """Custom type avGenOpIndex based on Integer32"""
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
              24,
              25,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("backup", 34),
          ("backupConfig", 28),
          ("commit", 30),
          ("downloadAnnouncements", 19),
          ("downloadAuthFile", 12),
          ("downloadCertificate", 36),
          ("downloadConfig", 2),
          ("downloadConfigurationWizardTaskFile", 44),
          ("downloadLicFile", 13),
          ("downloadPhoneImageFile", 16),
          ("downloadPhoneMessageFile", 42),
          ("downloadPhoneScriptFile", 14),
          ("downloadServicePack", 32),
          ("downloadSoftware", 5),
          ("downloadVoiceMailFile", 40),
          ("eraseAnnouncement", 21),
          ("eraseFile", 9),
          ("generateFile", 35),
          ("localConfigFileCopy", 6),
          ("localSWFileCopy", 7),
          ("localSWFileMove", 46),
          ("localServicePackFileCopy", 33),
          ("localVoiceMailFileMove", 47),
          ("renameAnnouncement", 20),
          ("report", 3),
          ("reset", 48),
          ("restore", 29),
          ("show", 10),
          ("switchPartitions", 38),
          ("syncStandbyAgent", 11),
          ("uploadAnnouncements", 18),
          ("uploadAuthFile", 22),
          ("uploadCDRFile", 25),
          ("uploadCertificate", 37),
          ("uploadConfig", 1),
          ("uploadConfigurationWizardTaskFile", 45),
          ("uploadDhcpBindingFile", 17),
          ("uploadLicFile", 23),
          ("uploadLogfile", 8),
          ("uploadPhoneImageFile", 39),
          ("uploadPhoneMessageFile", 43),
          ("uploadPhoneScriptFile", 15),
          ("uploadServicePack", 31),
          ("uploadSoftware", 4),
          ("uploadSyslogFile", 24),
          ("uploadVoiceMailFile", 41))
    )


_AvGenOpIndex_Type.__name__ = "Integer32"
_AvGenOpIndex_Object = MibTableColumn
avGenOpIndex = _AvGenOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 2),
    _AvGenOpIndex_Type()
)
avGenOpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpIndex.setStatus("current")


class _AvGenOpRunningState_Type(Integer32):
    """Custom type avGenOpRunningState based on Integer32"""
    defaultValue = 1

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
        *(("beginOperation", 2),
          ("blocked", 8),
          ("copyingLocal", 5),
          ("executing", 7),
          ("idle", 1),
          ("readingConfiguration", 6),
          ("reset", 9),
          ("runningIp", 4),
          ("waitingIp", 3))
    )


_AvGenOpRunningState_Type.__name__ = "Integer32"
_AvGenOpRunningState_Object = MibTableColumn
avGenOpRunningState = _AvGenOpRunningState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 3),
    _AvGenOpRunningState_Type()
)
avGenOpRunningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpRunningState.setStatus("current")
_AvGenOpSourceIndex_Type = Integer32
_AvGenOpSourceIndex_Object = MibTableColumn
avGenOpSourceIndex = _AvGenOpSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 4),
    _AvGenOpSourceIndex_Type()
)
avGenOpSourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpSourceIndex.setStatus("current")
_AvGenOpDestIndex_Type = Integer32
_AvGenOpDestIndex_Object = MibTableColumn
avGenOpDestIndex = _AvGenOpDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 5),
    _AvGenOpDestIndex_Type()
)
avGenOpDestIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpDestIndex.setStatus("current")
_AvGenOpServerIP_Type = IpAddress
_AvGenOpServerIP_Object = MibTableColumn
avGenOpServerIP = _AvGenOpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 6),
    _AvGenOpServerIP_Type()
)
avGenOpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpServerIP.setStatus("current")


class _AvGenOpUserName_Type(DisplayString):
    """Custom type avGenOpUserName based on DisplayString"""
    defaultHexValue = "00"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvGenOpUserName_Type.__name__ = "DisplayString"
_AvGenOpUserName_Object = MibTableColumn
avGenOpUserName = _AvGenOpUserName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 7),
    _AvGenOpUserName_Type()
)
avGenOpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpUserName.setStatus("current")


class _AvGenOpPassword_Type(OctetString):
    """Custom type avGenOpPassword based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvGenOpPassword_Type.__name__ = "OctetString"
_AvGenOpPassword_Object = MibTableColumn
avGenOpPassword = _AvGenOpPassword_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 8),
    _AvGenOpPassword_Type()
)
avGenOpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpPassword.setStatus("current")


class _AvGenOpProtocolType_Type(Integer32):
    """Custom type avGenOpProtocolType based on Integer32"""
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
        *(("ftp", 2),
          ("ftpResume", 10),
          ("http", 8),
          ("https", 9),
          ("localPeerTransport", 3),
          ("localServerTransport", 4),
          ("scp", 5),
          ("sftp", 6),
          ("tftp", 1),
          ("usb", 7))
    )


_AvGenOpProtocolType_Type.__name__ = "Integer32"
_AvGenOpProtocolType_Object = MibTableColumn
avGenOpProtocolType = _AvGenOpProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 9),
    _AvGenOpProtocolType_Type()
)
avGenOpProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpProtocolType.setStatus("current")
_AvGenOpFileName_Type = DisplayString
_AvGenOpFileName_Object = MibTableColumn
avGenOpFileName = _AvGenOpFileName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 10),
    _AvGenOpFileName_Type()
)
avGenOpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpFileName.setStatus("current")


class _AvGenOpRunningStateDisplay_Type(DisplayString):
    """Custom type avGenOpRunningStateDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvGenOpRunningStateDisplay_Type.__name__ = "DisplayString"
_AvGenOpRunningStateDisplay_Object = MibTableColumn
avGenOpRunningStateDisplay = _AvGenOpRunningStateDisplay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 11),
    _AvGenOpRunningStateDisplay_Type()
)
avGenOpRunningStateDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpRunningStateDisplay.setStatus("current")


class _AvGenOpLastFailureIndex_Type(Integer32):
    """Custom type avGenOpLastFailureIndex based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              210,
              220,
              221,
              222)
        )
    )
    namedValues = NamedValues(
        *(("accessViolation", 102),
          ("authDSFailure", 208),
          ("badChainOfTrust", 201),
          ("badChainOfTrustFormat", 202),
          ("badDSFormat", 207),
          ("badPublicKeyFormat", 205),
          ("busy", 4),
          ("cancelled", 6),
          ("confFileExecError", 14),
          ("confFileGenErr", 12),
          ("confFileParseError", 13),
          ("configError", 3),
          ("configFileSecretIntegrityFault", 210),
          ("emptyFile", 16),
          ("fileAlreadyExists", 106),
          ("fileNotFound", 101),
          ("fileTooBig", 8),
          ("flashWriteError", 10),
          ("ftpResumeBadFilename", 220),
          ("ftpResumeEmptyFile", 221),
          ("ftpResumeNotSupported", 222),
          ("genError", 2),
          ("illegalDSA", 204),
          ("illegalDSKeySize", 206),
          ("illegalOperation", 104),
          ("incompatibleFile", 7),
          ("noEnoughFreeMemoryLeft", 17),
          ("noError", 1),
          ("noSuchUser", 107),
          ("notCodeSigningAuthority", 203),
          ("nvramWriteError", 11),
          ("outOfMemory", 103),
          ("protocolError", 9),
          ("readOnlyFile", 15),
          ("sshDeviceAuth", 109),
          ("sshServerAuth", 108),
          ("timeout", 5),
          ("undefinedError", 100),
          ("unknownTransferId", 105))
    )


_AvGenOpLastFailureIndex_Type.__name__ = "Integer32"
_AvGenOpLastFailureIndex_Object = MibTableColumn
avGenOpLastFailureIndex = _AvGenOpLastFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 12),
    _AvGenOpLastFailureIndex_Type()
)
avGenOpLastFailureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpLastFailureIndex.setStatus("current")


class _AvGenOpLastFailureDisplay_Type(DisplayString):
    """Custom type avGenOpLastFailureDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AvGenOpLastFailureDisplay_Type.__name__ = "DisplayString"
_AvGenOpLastFailureDisplay_Object = MibTableColumn
avGenOpLastFailureDisplay = _AvGenOpLastFailureDisplay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 13),
    _AvGenOpLastFailureDisplay_Type()
)
avGenOpLastFailureDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpLastFailureDisplay.setStatus("current")


class _AvGenOpLastWarningDisplay_Type(DisplayString):
    """Custom type avGenOpLastWarningDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AvGenOpLastWarningDisplay_Type.__name__ = "DisplayString"
_AvGenOpLastWarningDisplay_Object = MibTableColumn
avGenOpLastWarningDisplay = _AvGenOpLastWarningDisplay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 14),
    _AvGenOpLastWarningDisplay_Type()
)
avGenOpLastWarningDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpLastWarningDisplay.setStatus("current")
_AvGenOpErrorLogIndex_Type = Integer32
_AvGenOpErrorLogIndex_Object = MibTableColumn
avGenOpErrorLogIndex = _AvGenOpErrorLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 15),
    _AvGenOpErrorLogIndex_Type()
)
avGenOpErrorLogIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpErrorLogIndex.setStatus("current")


class _AvGenOpResetSupported_Type(Integer32):
    """Custom type avGenOpResetSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_AvGenOpResetSupported_Type.__name__ = "Integer32"
_AvGenOpResetSupported_Object = MibTableColumn
avGenOpResetSupported = _AvGenOpResetSupported_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 16),
    _AvGenOpResetSupported_Type()
)
avGenOpResetSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpResetSupported.setStatus("current")


class _AvGenOpEnableReset_Type(Integer32):
    """Custom type avGenOpEnableReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AvGenOpEnableReset_Type.__name__ = "Integer32"
_AvGenOpEnableReset_Object = MibTableColumn
avGenOpEnableReset = _AvGenOpEnableReset_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 17),
    _AvGenOpEnableReset_Type()
)
avGenOpEnableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpEnableReset.setStatus("current")
_AvGenOpNextBootImageIndex_Type = Integer32
_AvGenOpNextBootImageIndex_Object = MibTableColumn
avGenOpNextBootImageIndex = _AvGenOpNextBootImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 18),
    _AvGenOpNextBootImageIndex_Type()
)
avGenOpNextBootImageIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpNextBootImageIndex.setStatus("current")
_AvGenOpLastBootImageIndex_Type = Integer32
_AvGenOpLastBootImageIndex_Object = MibTableColumn
avGenOpLastBootImageIndex = _AvGenOpLastBootImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 19),
    _AvGenOpLastBootImageIndex_Type()
)
avGenOpLastBootImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpLastBootImageIndex.setStatus("current")


class _AvGenOpFileSystemType_Type(Integer32):
    """Custom type avGenOpFileSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AvGenOpFileSystemType_Type.__name__ = "Integer32"
_AvGenOpFileSystemType_Object = MibTableColumn
avGenOpFileSystemType = _AvGenOpFileSystemType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 20),
    _AvGenOpFileSystemType_Type()
)
avGenOpFileSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpFileSystemType.setStatus("current")


class _AvGenOpReportSpecificFlags_Type(Integer32):
    """Custom type avGenOpReportSpecificFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fullReport", 1),
          ("notSupported", 255),
          ("partialReport", 2))
    )


_AvGenOpReportSpecificFlags_Type.__name__ = "Integer32"
_AvGenOpReportSpecificFlags_Object = MibTableColumn
avGenOpReportSpecificFlags = _AvGenOpReportSpecificFlags_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 21),
    _AvGenOpReportSpecificFlags_Type()
)
avGenOpReportSpecificFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpReportSpecificFlags.setStatus("current")
_AvGenOpOctetsReceived_Type = Integer32
_AvGenOpOctetsReceived_Object = MibTableColumn
avGenOpOctetsReceived = _AvGenOpOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 22),
    _AvGenOpOctetsReceived_Type()
)
avGenOpOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenOpOctetsReceived.setStatus("current")
_AvGenOpDownloadProxy_Type = Integer32
_AvGenOpDownloadProxy_Object = MibTableColumn
avGenOpDownloadProxy = _AvGenOpDownloadProxy_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 23),
    _AvGenOpDownloadProxy_Type()
)
avGenOpDownloadProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpDownloadProxy.setStatus("current")
_AvGenOpServerInetAddressType_Type = InetAddressType
_AvGenOpServerInetAddressType_Object = MibTableColumn
avGenOpServerInetAddressType = _AvGenOpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 24),
    _AvGenOpServerInetAddressType_Type()
)
avGenOpServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpServerInetAddressType.setStatus("current")
_AvGenOpServerInetAddress_Type = InetAddress
_AvGenOpServerInetAddress_Object = MibTableColumn
avGenOpServerInetAddress = _AvGenOpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 1, 2, 1, 25),
    _AvGenOpServerInetAddress_Type()
)
avGenOpServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenOpServerInetAddress.setStatus("current")
_AvGenApplications_ObjectIdentity = ObjectIdentity
avGenApplications = _AvGenApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2)
)
_AvGenAppFileTable_Object = MibTable
avGenAppFileTable = _AvGenAppFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1)
)
if mibBuilder.loadTexts:
    avGenAppFileTable.setStatus("current")
_AvGenAppFileEntry_Object = MibTableRow
avGenAppFileEntry = _AvGenAppFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1)
)
avGenAppFileEntry.setIndexNames(
    (0, "AVAYA-LOAD-MIB", "avGenOpModuleId"),
    (0, "AVAYA-LOAD-MIB", "avGenAppFileId"),
)
if mibBuilder.loadTexts:
    avGenAppFileEntry.setStatus("current")


class _AvGenAppFileId_Type(Integer32):
    """Custom type avGenAppFileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AvGenAppFileId_Type.__name__ = "Integer32"
_AvGenAppFileId_Object = MibTableColumn
avGenAppFileId = _AvGenAppFileId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 1),
    _AvGenAppFileId_Type()
)
avGenAppFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenAppFileId.setStatus("current")


class _AvGenAppFileName_Type(DisplayString):
    """Custom type avGenAppFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvGenAppFileName_Type.__name__ = "DisplayString"
_AvGenAppFileName_Object = MibTableColumn
avGenAppFileName = _AvGenAppFileName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 2),
    _AvGenAppFileName_Type()
)
avGenAppFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avGenAppFileName.setStatus("current")


class _AvGenAppFileType_Type(Integer32):
    """Custom type avGenAppFileType based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("announcementFile", 20),
          ("asgAuthFile", 15),
          ("backupDatabase", 21),
          ("cdrFile", 23),
          ("certificateRequest", 27),
          ("defaultConfiguration", 3),
          ("dhcpBindingFile", 19),
          ("genConfigFile", 5),
          ("genConfigurationWizardTaskFile", 34),
          ("licenseFile", 16),
          ("logFile", 6),
          ("nvramFile", 7),
          ("other", 11),
          ("phoneAvayaUnicodeMessageFile", 31),
          ("phoneCustomUnicodeMessageFile", 32),
          ("phoneImageFile", 18),
          ("phoneScriptFile", 17),
          ("privateKey", 29),
          ("report", 4),
          ("runningConfiguration", 1),
          ("serverCertificate", 28),
          ("startupConfiguration", 2),
          ("startupConfigurationWizardTaskFile", 33),
          ("staticLanguagePack", 30),
          ("swAPImage", 13),
          ("swBootImage", 9),
          ("swComponent", 10),
          ("swComponentServicePack", 25),
          ("swNonDownLoadRunTimeImage", 14),
          ("swRuntimeImage", 8),
          ("swRuntimeServicePack", 24),
          ("swWebImage", 12),
          ("syslogFile", 22),
          ("trustedCertificate", 26))
    )


_AvGenAppFileType_Type.__name__ = "Integer32"
_AvGenAppFileType_Object = MibTableColumn
avGenAppFileType = _AvGenAppFileType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 3),
    _AvGenAppFileType_Type()
)
avGenAppFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avGenAppFileType.setStatus("current")


class _AvGenAppFileDescription_Type(DisplayString):
    """Custom type avGenAppFileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvGenAppFileDescription_Type.__name__ = "DisplayString"
_AvGenAppFileDescription_Object = MibTableColumn
avGenAppFileDescription = _AvGenAppFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 4),
    _AvGenAppFileDescription_Type()
)
avGenAppFileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avGenAppFileDescription.setStatus("current")
_AvGenAppFileSize_Type = Integer32
_AvGenAppFileSize_Object = MibTableColumn
avGenAppFileSize = _AvGenAppFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 5),
    _AvGenAppFileSize_Type()
)
avGenAppFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenAppFileSize.setStatus("current")
_AvGenAppFileVersionNumber_Type = DisplayString
_AvGenAppFileVersionNumber_Object = MibTableColumn
avGenAppFileVersionNumber = _AvGenAppFileVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 6),
    _AvGenAppFileVersionNumber_Type()
)
avGenAppFileVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenAppFileVersionNumber.setStatus("current")


class _AvGenAppFileLocation_Type(Integer32):
    """Custom type avGenAppFileLocation based on Integer32"""
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
        *(("bootProm", 5),
          ("compactFlash", 6),
          ("flash", 7),
          ("flashBankA", 2),
          ("flashBankB", 3),
          ("nvram", 4),
          ("ram", 1))
    )


_AvGenAppFileLocation_Type.__name__ = "Integer32"
_AvGenAppFileLocation_Object = MibTableColumn
avGenAppFileLocation = _AvGenAppFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 7),
    _AvGenAppFileLocation_Type()
)
avGenAppFileLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avGenAppFileLocation.setStatus("current")


class _AvGenAppFileDateStamp_Type(DisplayString):
    """Custom type avGenAppFileDateStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvGenAppFileDateStamp_Type.__name__ = "DisplayString"
_AvGenAppFileDateStamp_Object = MibTableColumn
avGenAppFileDateStamp = _AvGenAppFileDateStamp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 8),
    _AvGenAppFileDateStamp_Type()
)
avGenAppFileDateStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenAppFileDateStamp.setStatus("current")
_AvGenAppFileRowStatus_Type = RowStatus
_AvGenAppFileRowStatus_Object = MibTableColumn
avGenAppFileRowStatus = _AvGenAppFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 9),
    _AvGenAppFileRowStatus_Type()
)
avGenAppFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avGenAppFileRowStatus.setStatus("current")
_AvGenAppFilePortNetwork_Type = Integer32
_AvGenAppFilePortNetwork_Object = MibTableColumn
avGenAppFilePortNetwork = _AvGenAppFilePortNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 10),
    _AvGenAppFilePortNetwork_Type()
)
avGenAppFilePortNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenAppFilePortNetwork.setStatus("current")


class _AvGenAppFileDuplStatus_Type(Integer32):
    """Custom type avGenAppFileDuplStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("not-administered", 3),
          ("standby", 2))
    )


_AvGenAppFileDuplStatus_Type.__name__ = "Integer32"
_AvGenAppFileDuplStatus_Object = MibTableColumn
avGenAppFileDuplStatus = _AvGenAppFileDuplStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 11),
    _AvGenAppFileDuplStatus_Type()
)
avGenAppFileDuplStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenAppFileDuplStatus.setStatus("current")
_AvGenAppFileCompatibleVersionNumber_Type = DisplayString
_AvGenAppFileCompatibleVersionNumber_Object = MibTableColumn
avGenAppFileCompatibleVersionNumber = _AvGenAppFileCompatibleVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 2, 1, 1, 12),
    _AvGenAppFileCompatibleVersionNumber_Type()
)
avGenAppFileCompatibleVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenAppFileCompatibleVersionNumber.setStatus("current")
_AvLoadNotificationDefinitions_ObjectIdentity = ObjectIdentity
avLoadNotificationDefinitions = _AvLoadNotificationDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 3)
)
_AvLoadSysDescription_Type = DisplayString
_AvLoadSysDescription_Object = MibScalar
avLoadSysDescription = _AvLoadSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 3, 1),
    _AvLoadSysDescription_Type()
)
avLoadSysDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avLoadSysDescription.setStatus("current")
_AvLoadSeverity_Type = AvLoadItuPerceivedSeverity
_AvLoadSeverity_Object = MibScalar
avLoadSeverity = _AvLoadSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 3, 2),
    _AvLoadSeverity_Type()
)
avLoadSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avLoadSeverity.setStatus("current")
_AvLoadGeneralInformation_ObjectIdentity = ObjectIdentity
avLoadGeneralInformation = _AvLoadGeneralInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 4)
)


class _AvGenLoadConnectionState_Type(Integer32):
    """Custom type avGenLoadConnectionState based on Integer32"""
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
        *(("down", 3),
          ("idle", 6),
          ("init", 4),
          ("off", 2),
          ("other", 1),
          ("up", 5))
    )


_AvGenLoadConnectionState_Type.__name__ = "Integer32"
_AvGenLoadConnectionState_Object = MibScalar
avGenLoadConnectionState = _AvGenLoadConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 4, 1),
    _AvGenLoadConnectionState_Type()
)
avGenLoadConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avGenLoadConnectionState.setStatus("current")


class _AvGenRestoreOperationState_Type(Integer32):
    """Custom type avGenRestoreOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("executing", 2),
          ("idle", 1))
    )


_AvGenRestoreOperationState_Type.__name__ = "Integer32"
_AvGenRestoreOperationState_Object = MibScalar
avGenRestoreOperationState = _AvGenRestoreOperationState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 4, 2),
    _AvGenRestoreOperationState_Type()
)
avGenRestoreOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avGenRestoreOperationState.setStatus("current")
_AvLoadApplMemTable_Object = MibTable
avLoadApplMemTable = _AvLoadApplMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5)
)
if mibBuilder.loadTexts:
    avLoadApplMemTable.setStatus("current")
_AvLoadApplMemEntry_Object = MibTableRow
avLoadApplMemEntry = _AvLoadApplMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5, 1)
)
avLoadApplMemEntry.setIndexNames(
    (0, "AVAYA-LOAD-MIB", "avLoadApplMemModuleId"),
    (0, "AVAYA-LOAD-MIB", "avLoadApplMemLocation"),
    (0, "AVAYA-LOAD-MIB", "avLoadApplMemType"),
)
if mibBuilder.loadTexts:
    avLoadApplMemEntry.setStatus("current")
_AvLoadApplMemModuleId_Type = Integer32
_AvLoadApplMemModuleId_Object = MibTableColumn
avLoadApplMemModuleId = _AvLoadApplMemModuleId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5, 1, 1),
    _AvLoadApplMemModuleId_Type()
)
avLoadApplMemModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadApplMemModuleId.setStatus("current")


class _AvLoadApplMemLocation_Type(Integer32):
    """Custom type avLoadApplMemLocation based on Integer32"""
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
        *(("bootProm", 5),
          ("flashBankA", 2),
          ("flashBankB", 3),
          ("nvram", 4),
          ("ram", 1))
    )


_AvLoadApplMemLocation_Type.__name__ = "Integer32"
_AvLoadApplMemLocation_Object = MibTableColumn
avLoadApplMemLocation = _AvLoadApplMemLocation_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5, 1, 2),
    _AvLoadApplMemLocation_Type()
)
avLoadApplMemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadApplMemLocation.setStatus("current")


class _AvLoadApplMemType_Type(Integer32):
    """Custom type avLoadApplMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("announcementFile", 20)
    )


_AvLoadApplMemType_Type.__name__ = "Integer32"
_AvLoadApplMemType_Object = MibTableColumn
avLoadApplMemType = _AvLoadApplMemType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5, 1, 3),
    _AvLoadApplMemType_Type()
)
avLoadApplMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadApplMemType.setStatus("current")
_AvLoadApplMemSize_Type = Integer32
_AvLoadApplMemSize_Object = MibTableColumn
avLoadApplMemSize = _AvLoadApplMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5, 1, 4),
    _AvLoadApplMemSize_Type()
)
avLoadApplMemSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avLoadApplMemSize.setStatus("current")
_AvLoadApplMemTotalBytesUsed_Type = Integer32
_AvLoadApplMemTotalBytesUsed_Object = MibTableColumn
avLoadApplMemTotalBytesUsed = _AvLoadApplMemTotalBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5, 1, 5),
    _AvLoadApplMemTotalBytesUsed_Type()
)
avLoadApplMemTotalBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadApplMemTotalBytesUsed.setStatus("current")
_AvLoadApplMemTotalBytesFree_Type = Integer32
_AvLoadApplMemTotalBytesFree_Object = MibTableColumn
avLoadApplMemTotalBytesFree = _AvLoadApplMemTotalBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 5, 1, 6),
    _AvLoadApplMemTotalBytesFree_Type()
)
avLoadApplMemTotalBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadApplMemTotalBytesFree.setStatus("current")
_AvLoadAppDynamicFileTable_Object = MibTable
avLoadAppDynamicFileTable = _AvLoadAppDynamicFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 6)
)
if mibBuilder.loadTexts:
    avLoadAppDynamicFileTable.setStatus("current")
_AvLoadAppDynamicFileEntry_Object = MibTableRow
avLoadAppDynamicFileEntry = _AvLoadAppDynamicFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 6, 1)
)
avLoadAppDynamicFileEntry.setIndexNames(
    (0, "AVAYA-LOAD-MIB", "avLoadAppDynamicFileName"),
)
if mibBuilder.loadTexts:
    avLoadAppDynamicFileEntry.setStatus("current")


class _AvLoadAppDynamicFileName_Type(DisplayString):
    """Custom type avLoadAppDynamicFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AvLoadAppDynamicFileName_Type.__name__ = "DisplayString"
_AvLoadAppDynamicFileName_Object = MibTableColumn
avLoadAppDynamicFileName = _AvLoadAppDynamicFileName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 6, 1, 1),
    _AvLoadAppDynamicFileName_Type()
)
avLoadAppDynamicFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadAppDynamicFileName.setStatus("current")


class _AvLoadAppDynamicFileType_Type(Integer32):
    """Custom type avLoadAppDynamicFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directory", 2),
          ("file", 1))
    )


_AvLoadAppDynamicFileType_Type.__name__ = "Integer32"
_AvLoadAppDynamicFileType_Object = MibTableColumn
avLoadAppDynamicFileType = _AvLoadAppDynamicFileType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 6, 1, 2),
    _AvLoadAppDynamicFileType_Type()
)
avLoadAppDynamicFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadAppDynamicFileType.setStatus("current")
_AvLoadAppDynamicFileSize_Type = Integer32
_AvLoadAppDynamicFileSize_Object = MibTableColumn
avLoadAppDynamicFileSize = _AvLoadAppDynamicFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 6, 1, 3),
    _AvLoadAppDynamicFileSize_Type()
)
avLoadAppDynamicFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadAppDynamicFileSize.setStatus("current")


class _AvLoadAppDynamicFileDateStamp_Type(DisplayString):
    """Custom type avLoadAppDynamicFileDateStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvLoadAppDynamicFileDateStamp_Type.__name__ = "DisplayString"
_AvLoadAppDynamicFileDateStamp_Object = MibTableColumn
avLoadAppDynamicFileDateStamp = _AvLoadAppDynamicFileDateStamp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 6, 1, 4),
    _AvLoadAppDynamicFileDateStamp_Type()
)
avLoadAppDynamicFileDateStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLoadAppDynamicFileDateStamp.setStatus("current")
_AvLoadAppDynamicFileRowStatus_Type = RowStatus
_AvLoadAppDynamicFileRowStatus_Object = MibTableColumn
avLoadAppDynamicFileRowStatus = _AvLoadAppDynamicFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 6, 1, 5),
    _AvLoadAppDynamicFileRowStatus_Type()
)
avLoadAppDynamicFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avLoadAppDynamicFileRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

avDownloadBegun = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 0, 1)
)
avDownloadBegun.setObjects(
      *(("AVAYA-LOAD-MIB", "avLoadSysDescription"),
        ("AVAYA-LOAD-MIB", "avGenOpModuleId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileName"),
        ("AVAYA-LOAD-MIB", "avGenAppFileDescription"),
        ("AVAYA-LOAD-MIB", "avGenAppFileVersionNumber"),
        ("AVAYA-LOAD-MIB", "avLoadSeverity"))
)
if mibBuilder.loadTexts:
    avDownloadBegun.setStatus(
        "current"
    )

avDownloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 0, 2)
)
avDownloadSuccess.setObjects(
      *(("AVAYA-LOAD-MIB", "avLoadSysDescription"),
        ("AVAYA-LOAD-MIB", "avGenOpModuleId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileName"),
        ("AVAYA-LOAD-MIB", "avGenAppFileDescription"),
        ("AVAYA-LOAD-MIB", "avGenAppFileVersionNumber"),
        ("AVAYA-LOAD-MIB", "avLoadSeverity"))
)
if mibBuilder.loadTexts:
    avDownloadSuccess.setStatus(
        "current"
    )

avDownloadFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 0, 3)
)
avDownloadFault.setObjects(
      *(("AVAYA-LOAD-MIB", "avLoadSysDescription"),
        ("AVAYA-LOAD-MIB", "avGenOpModuleId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileName"),
        ("AVAYA-LOAD-MIB", "avGenAppFileDescription"),
        ("AVAYA-LOAD-MIB", "avGenAppFileVersionNumber"),
        ("AVAYA-LOAD-MIB", "avGenOpLastFailureIndex"),
        ("AVAYA-LOAD-MIB", "avGenOpLastFailureDisplay"),
        ("AVAYA-LOAD-MIB", "avLoadSeverity"))
)
if mibBuilder.loadTexts:
    avDownloadFault.setStatus(
        "current"
    )

avUploadBegun = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 0, 4)
)
avUploadBegun.setObjects(
      *(("AVAYA-LOAD-MIB", "avLoadSysDescription"),
        ("AVAYA-LOAD-MIB", "avGenOpModuleId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileName"),
        ("AVAYA-LOAD-MIB", "avGenAppFileDescription"),
        ("AVAYA-LOAD-MIB", "avGenAppFileVersionNumber"),
        ("AVAYA-LOAD-MIB", "avLoadSeverity"))
)
if mibBuilder.loadTexts:
    avUploadBegun.setStatus(
        "current"
    )

avUploadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 0, 5)
)
avUploadSuccess.setObjects(
      *(("AVAYA-LOAD-MIB", "avLoadSysDescription"),
        ("AVAYA-LOAD-MIB", "avGenOpModuleId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileName"),
        ("AVAYA-LOAD-MIB", "avGenAppFileDescription"),
        ("AVAYA-LOAD-MIB", "avGenAppFileVersionNumber"),
        ("AVAYA-LOAD-MIB", "avLoadSeverity"))
)
if mibBuilder.loadTexts:
    avUploadSuccess.setStatus(
        "current"
    )

avUploadFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 5, 0, 6)
)
avUploadFault.setObjects(
      *(("AVAYA-LOAD-MIB", "avLoadSysDescription"),
        ("AVAYA-LOAD-MIB", "avGenOpModuleId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileId"),
        ("AVAYA-LOAD-MIB", "avGenAppFileName"),
        ("AVAYA-LOAD-MIB", "avGenAppFileDescription"),
        ("AVAYA-LOAD-MIB", "avGenAppFileVersionNumber"),
        ("AVAYA-LOAD-MIB", "avGenOpLastFailureIndex"),
        ("AVAYA-LOAD-MIB", "avGenOpLastFailureDisplay"),
        ("AVAYA-LOAD-MIB", "avLoadSeverity"))
)
if mibBuilder.loadTexts:
    avUploadFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-LOAD-MIB",
    **{"AvLoadItuPerceivedSeverity": AvLoadItuPerceivedSeverity,
       "avLoad": avLoad,
       "avLoadNotification": avLoadNotification,
       "avDownloadBegun": avDownloadBegun,
       "avDownloadSuccess": avDownloadSuccess,
       "avDownloadFault": avDownloadFault,
       "avUploadBegun": avUploadBegun,
       "avUploadSuccess": avUploadSuccess,
       "avUploadFault": avUploadFault,
       "avGenOperations": avGenOperations,
       "avGenLoadNumberOfSession": avGenLoadNumberOfSession,
       "avGenOpTable": avGenOpTable,
       "avGenOpEntry": avGenOpEntry,
       "avGenOpModuleId": avGenOpModuleId,
       "avGenOpIndex": avGenOpIndex,
       "avGenOpRunningState": avGenOpRunningState,
       "avGenOpSourceIndex": avGenOpSourceIndex,
       "avGenOpDestIndex": avGenOpDestIndex,
       "avGenOpServerIP": avGenOpServerIP,
       "avGenOpUserName": avGenOpUserName,
       "avGenOpPassword": avGenOpPassword,
       "avGenOpProtocolType": avGenOpProtocolType,
       "avGenOpFileName": avGenOpFileName,
       "avGenOpRunningStateDisplay": avGenOpRunningStateDisplay,
       "avGenOpLastFailureIndex": avGenOpLastFailureIndex,
       "avGenOpLastFailureDisplay": avGenOpLastFailureDisplay,
       "avGenOpLastWarningDisplay": avGenOpLastWarningDisplay,
       "avGenOpErrorLogIndex": avGenOpErrorLogIndex,
       "avGenOpResetSupported": avGenOpResetSupported,
       "avGenOpEnableReset": avGenOpEnableReset,
       "avGenOpNextBootImageIndex": avGenOpNextBootImageIndex,
       "avGenOpLastBootImageIndex": avGenOpLastBootImageIndex,
       "avGenOpFileSystemType": avGenOpFileSystemType,
       "avGenOpReportSpecificFlags": avGenOpReportSpecificFlags,
       "avGenOpOctetsReceived": avGenOpOctetsReceived,
       "avGenOpDownloadProxy": avGenOpDownloadProxy,
       "avGenOpServerInetAddressType": avGenOpServerInetAddressType,
       "avGenOpServerInetAddress": avGenOpServerInetAddress,
       "avGenApplications": avGenApplications,
       "avGenAppFileTable": avGenAppFileTable,
       "avGenAppFileEntry": avGenAppFileEntry,
       "avGenAppFileId": avGenAppFileId,
       "avGenAppFileName": avGenAppFileName,
       "avGenAppFileType": avGenAppFileType,
       "avGenAppFileDescription": avGenAppFileDescription,
       "avGenAppFileSize": avGenAppFileSize,
       "avGenAppFileVersionNumber": avGenAppFileVersionNumber,
       "avGenAppFileLocation": avGenAppFileLocation,
       "avGenAppFileDateStamp": avGenAppFileDateStamp,
       "avGenAppFileRowStatus": avGenAppFileRowStatus,
       "avGenAppFilePortNetwork": avGenAppFilePortNetwork,
       "avGenAppFileDuplStatus": avGenAppFileDuplStatus,
       "avGenAppFileCompatibleVersionNumber": avGenAppFileCompatibleVersionNumber,
       "avLoadNotificationDefinitions": avLoadNotificationDefinitions,
       "avLoadSysDescription": avLoadSysDescription,
       "avLoadSeverity": avLoadSeverity,
       "avLoadGeneralInformation": avLoadGeneralInformation,
       "avGenLoadConnectionState": avGenLoadConnectionState,
       "avGenRestoreOperationState": avGenRestoreOperationState,
       "avLoadApplMemTable": avLoadApplMemTable,
       "avLoadApplMemEntry": avLoadApplMemEntry,
       "avLoadApplMemModuleId": avLoadApplMemModuleId,
       "avLoadApplMemLocation": avLoadApplMemLocation,
       "avLoadApplMemType": avLoadApplMemType,
       "avLoadApplMemSize": avLoadApplMemSize,
       "avLoadApplMemTotalBytesUsed": avLoadApplMemTotalBytesUsed,
       "avLoadApplMemTotalBytesFree": avLoadApplMemTotalBytesFree,
       "avLoadAppDynamicFileTable": avLoadAppDynamicFileTable,
       "avLoadAppDynamicFileEntry": avLoadAppDynamicFileEntry,
       "avLoadAppDynamicFileName": avLoadAppDynamicFileName,
       "avLoadAppDynamicFileType": avLoadAppDynamicFileType,
       "avLoadAppDynamicFileSize": avLoadAppDynamicFileSize,
       "avLoadAppDynamicFileDateStamp": avLoadAppDynamicFileDateStamp,
       "avLoadAppDynamicFileRowStatus": avLoadAppDynamicFileRowStatus}
)
