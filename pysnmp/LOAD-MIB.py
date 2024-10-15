# SNMP MIB module (LOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:34 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

load = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53)
)
load.setRevisions(
        ("1900-09-13 15:55",
         "1900-09-13 14:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2)
)
_GenOperations_ObjectIdentity = ObjectIdentity
genOperations = _GenOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1)
)
_GenLoadNumberOfSession_Type = Integer32
_GenLoadNumberOfSession_Object = MibScalar
genLoadNumberOfSession = _GenLoadNumberOfSession_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 1),
    _GenLoadNumberOfSession_Type()
)
genLoadNumberOfSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genLoadNumberOfSession.setStatus("current")
_GenOpTable_Object = MibTable
genOpTable = _GenOpTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2)
)
if mibBuilder.loadTexts:
    genOpTable.setStatus("current")
_GenOpEntry_Object = MibTableRow
genOpEntry = _GenOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1)
)
genOpEntry.setIndexNames(
    (0, "LOAD-MIB", "genOpModuleId"),
    (0, "LOAD-MIB", "genOpIndex"),
)
if mibBuilder.loadTexts:
    genOpEntry.setStatus("current")


class _GenOpModuleId_Type(Integer32):
    """Custom type genOpModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GenOpModuleId_Type.__name__ = "Integer32"
_GenOpModuleId_Object = MibTableColumn
genOpModuleId = _GenOpModuleId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 1),
    _GenOpModuleId_Type()
)
genOpModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpModuleId.setStatus("current")


class _GenOpIndex_Type(Integer32):
    """Custom type genOpIndex based on Integer32"""
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
        *(("downloadConfig", 2),
          ("downloadSoftware", 5),
          ("eraseFile", 9),
          ("localConfigFileCopy", 6),
          ("localSWFileCopy", 7),
          ("report", 3),
          ("show", 10),
          ("syncStandbyAgent", 11),
          ("uploadConfig", 1),
          ("uploadLogfile", 8),
          ("uploadSoftware", 4))
    )


_GenOpIndex_Type.__name__ = "Integer32"
_GenOpIndex_Object = MibTableColumn
genOpIndex = _GenOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 2),
    _GenOpIndex_Type()
)
genOpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpIndex.setStatus("current")


class _GenOpRunningState_Type(Integer32):
    """Custom type genOpRunningState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("beginOperation", 2),
          ("copyingLocal", 5),
          ("executing", 7),
          ("idle", 1),
          ("readingConfiguration", 6),
          ("runningIp", 4),
          ("waitingIp", 3))
    )


_GenOpRunningState_Type.__name__ = "Integer32"
_GenOpRunningState_Object = MibTableColumn
genOpRunningState = _GenOpRunningState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 3),
    _GenOpRunningState_Type()
)
genOpRunningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpRunningState.setStatus("current")
_GenOpSourceIndex_Type = Integer32
_GenOpSourceIndex_Object = MibTableColumn
genOpSourceIndex = _GenOpSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 4),
    _GenOpSourceIndex_Type()
)
genOpSourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpSourceIndex.setStatus("current")
_GenOpDestIndex_Type = Integer32
_GenOpDestIndex_Object = MibTableColumn
genOpDestIndex = _GenOpDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 5),
    _GenOpDestIndex_Type()
)
genOpDestIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpDestIndex.setStatus("current")
_GenOpServerIP_Type = IpAddress
_GenOpServerIP_Object = MibTableColumn
genOpServerIP = _GenOpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 6),
    _GenOpServerIP_Type()
)
genOpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpServerIP.setStatus("current")


class _GenOpUserName_Type(DisplayString):
    """Custom type genOpUserName based on DisplayString"""
    defaultHexValue = "0"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GenOpUserName_Type.__name__ = "DisplayString"
_GenOpUserName_Object = MibTableColumn
genOpUserName = _GenOpUserName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 7),
    _GenOpUserName_Type()
)
genOpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpUserName.setStatus("current")


class _GenOpPassword_Type(OctetString):
    """Custom type genOpPassword based on OctetString"""
    defaultHexValue = "0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GenOpPassword_Type.__name__ = "OctetString"
_GenOpPassword_Object = MibTableColumn
genOpPassword = _GenOpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 8),
    _GenOpPassword_Type()
)
genOpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpPassword.setStatus("current")


class _GenOpProtocolType_Type(Integer32):
    """Custom type genOpProtocolType based on Integer32"""
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
        *(("ftp", 2),
          ("localPeerTransport", 3),
          ("localServerTransport", 4),
          ("tftp", 1))
    )


_GenOpProtocolType_Type.__name__ = "Integer32"
_GenOpProtocolType_Object = MibTableColumn
genOpProtocolType = _GenOpProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 9),
    _GenOpProtocolType_Type()
)
genOpProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpProtocolType.setStatus("current")
_GenOpFileName_Type = DisplayString
_GenOpFileName_Object = MibTableColumn
genOpFileName = _GenOpFileName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 10),
    _GenOpFileName_Type()
)
genOpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpFileName.setStatus("current")


class _GenOpRunningStateDisplay_Type(DisplayString):
    """Custom type genOpRunningStateDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenOpRunningStateDisplay_Type.__name__ = "DisplayString"
_GenOpRunningStateDisplay_Object = MibTableColumn
genOpRunningStateDisplay = _GenOpRunningStateDisplay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 11),
    _GenOpRunningStateDisplay_Type()
)
genOpRunningStateDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpRunningStateDisplay.setStatus("current")


class _GenOpLastFailureIndex_Type(Integer32):
    """Custom type genOpLastFailureIndex based on Integer32"""
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
        *(("accessViolation", 102),
          ("busy", 4),
          ("cancelled", 6),
          ("confFileExecError", 14),
          ("confFileGenErr", 12),
          ("confFileParseError", 13),
          ("configError", 3),
          ("fileAlreadyExists", 106),
          ("fileNotFound", 101),
          ("fileTooBig", 8),
          ("flashWriteError", 10),
          ("genError", 2),
          ("illegalOperation", 104),
          ("incompatibleFile", 7),
          ("noError", 1),
          ("noSuchUser", 107),
          ("nvramWriteError", 11),
          ("outOfMemory", 103),
          ("protocolError", 9),
          ("timeout", 5),
          ("undefinedError", 100),
          ("unknownTransferId", 105))
    )


_GenOpLastFailureIndex_Type.__name__ = "Integer32"
_GenOpLastFailureIndex_Object = MibTableColumn
genOpLastFailureIndex = _GenOpLastFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 12),
    _GenOpLastFailureIndex_Type()
)
genOpLastFailureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpLastFailureIndex.setStatus("current")


class _GenOpLastFailureDisplay_Type(DisplayString):
    """Custom type genOpLastFailureDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenOpLastFailureDisplay_Type.__name__ = "DisplayString"
_GenOpLastFailureDisplay_Object = MibTableColumn
genOpLastFailureDisplay = _GenOpLastFailureDisplay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 13),
    _GenOpLastFailureDisplay_Type()
)
genOpLastFailureDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpLastFailureDisplay.setStatus("current")


class _GenOpLastWarningDisplay_Type(DisplayString):
    """Custom type genOpLastWarningDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenOpLastWarningDisplay_Type.__name__ = "DisplayString"
_GenOpLastWarningDisplay_Object = MibTableColumn
genOpLastWarningDisplay = _GenOpLastWarningDisplay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 14),
    _GenOpLastWarningDisplay_Type()
)
genOpLastWarningDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpLastWarningDisplay.setStatus("current")
_GenOpErrorLogIndex_Type = Integer32
_GenOpErrorLogIndex_Object = MibTableColumn
genOpErrorLogIndex = _GenOpErrorLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 15),
    _GenOpErrorLogIndex_Type()
)
genOpErrorLogIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpErrorLogIndex.setStatus("current")


class _GenOpResetSupported_Type(Integer32):
    """Custom type genOpResetSupported based on Integer32"""
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


_GenOpResetSupported_Type.__name__ = "Integer32"
_GenOpResetSupported_Object = MibTableColumn
genOpResetSupported = _GenOpResetSupported_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 16),
    _GenOpResetSupported_Type()
)
genOpResetSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpResetSupported.setStatus("current")


class _GenOpEnableReset_Type(Integer32):
    """Custom type genOpEnableReset based on Integer32"""
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


_GenOpEnableReset_Type.__name__ = "Integer32"
_GenOpEnableReset_Object = MibTableColumn
genOpEnableReset = _GenOpEnableReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 17),
    _GenOpEnableReset_Type()
)
genOpEnableReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpEnableReset.setStatus("current")
_GenOpNextBootImageIndex_Type = Integer32
_GenOpNextBootImageIndex_Object = MibTableColumn
genOpNextBootImageIndex = _GenOpNextBootImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 18),
    _GenOpNextBootImageIndex_Type()
)
genOpNextBootImageIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpNextBootImageIndex.setStatus("current")
_GenOpLastBootImageIndex_Type = Integer32
_GenOpLastBootImageIndex_Object = MibTableColumn
genOpLastBootImageIndex = _GenOpLastBootImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 19),
    _GenOpLastBootImageIndex_Type()
)
genOpLastBootImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpLastBootImageIndex.setStatus("current")


class _GenOpFileSystemType_Type(Integer32):
    """Custom type genOpFileSystemType based on Integer32"""
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


_GenOpFileSystemType_Type.__name__ = "Integer32"
_GenOpFileSystemType_Object = MibTableColumn
genOpFileSystemType = _GenOpFileSystemType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 20),
    _GenOpFileSystemType_Type()
)
genOpFileSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpFileSystemType.setStatus("current")


class _GenOpReportSpecificFlags_Type(Integer32):
    """Custom type genOpReportSpecificFlags based on Integer32"""
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


_GenOpReportSpecificFlags_Type.__name__ = "Integer32"
_GenOpReportSpecificFlags_Object = MibTableColumn
genOpReportSpecificFlags = _GenOpReportSpecificFlags_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 21),
    _GenOpReportSpecificFlags_Type()
)
genOpReportSpecificFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genOpReportSpecificFlags.setStatus("current")
_GenOpOctetsReceived_Type = Integer32
_GenOpOctetsReceived_Object = MibTableColumn
genOpOctetsReceived = _GenOpOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 22),
    _GenOpOctetsReceived_Type()
)
genOpOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genOpOctetsReceived.setStatus("current")
_GenApplications_ObjectIdentity = ObjectIdentity
genApplications = _GenApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2)
)
_GenAppFileTable_Object = MibTable
genAppFileTable = _GenAppFileTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1)
)
if mibBuilder.loadTexts:
    genAppFileTable.setStatus("current")
_GenAppFileEntry_Object = MibTableRow
genAppFileEntry = _GenAppFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1)
)
genAppFileEntry.setIndexNames(
    (0, "LOAD-MIB", "genOpModuleId"),
    (0, "LOAD-MIB", "genAppFileId"),
)
if mibBuilder.loadTexts:
    genAppFileEntry.setStatus("current")


class _GenAppFileId_Type(Integer32):
    """Custom type genAppFileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GenAppFileId_Type.__name__ = "Integer32"
_GenAppFileId_Object = MibTableColumn
genAppFileId = _GenAppFileId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 1),
    _GenAppFileId_Type()
)
genAppFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAppFileId.setStatus("current")


class _GenAppFileName_Type(DisplayString):
    """Custom type genAppFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenAppFileName_Type.__name__ = "DisplayString"
_GenAppFileName_Object = MibTableColumn
genAppFileName = _GenAppFileName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 2),
    _GenAppFileName_Type()
)
genAppFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genAppFileName.setStatus("current")


class _GenAppFileType_Type(Integer32):
    """Custom type genAppFileType based on Integer32"""
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
        *(("defaultConfiguration", 3),
          ("genConfigFile", 5),
          ("logFile", 6),
          ("nvramFile", 7),
          ("other", 11),
          ("report", 4),
          ("runningConfiguration", 1),
          ("startupConfiguration", 2),
          ("swBootImage", 9),
          ("swComponent", 10),
          ("swRuntimeImage", 8),
          ("swWebImage", 12))
    )


_GenAppFileType_Type.__name__ = "Integer32"
_GenAppFileType_Object = MibTableColumn
genAppFileType = _GenAppFileType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 3),
    _GenAppFileType_Type()
)
genAppFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genAppFileType.setStatus("current")


class _GenAppFileDescription_Type(DisplayString):
    """Custom type genAppFileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenAppFileDescription_Type.__name__ = "DisplayString"
_GenAppFileDescription_Object = MibTableColumn
genAppFileDescription = _GenAppFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 4),
    _GenAppFileDescription_Type()
)
genAppFileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genAppFileDescription.setStatus("current")
_GenAppFileSize_Type = Integer32
_GenAppFileSize_Object = MibTableColumn
genAppFileSize = _GenAppFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 5),
    _GenAppFileSize_Type()
)
genAppFileSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genAppFileSize.setStatus("current")
_GenAppFileVersionNumber_Type = OctetString
_GenAppFileVersionNumber_Object = MibTableColumn
genAppFileVersionNumber = _GenAppFileVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 6),
    _GenAppFileVersionNumber_Type()
)
genAppFileVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAppFileVersionNumber.setStatus("current")


class _GenAppFileLocation_Type(Integer32):
    """Custom type genAppFileLocation based on Integer32"""
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


_GenAppFileLocation_Type.__name__ = "Integer32"
_GenAppFileLocation_Object = MibTableColumn
genAppFileLocation = _GenAppFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 7),
    _GenAppFileLocation_Type()
)
genAppFileLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genAppFileLocation.setStatus("current")


class _GenAppFileDateStamp_Type(DisplayString):
    """Custom type genAppFileDateStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenAppFileDateStamp_Type.__name__ = "DisplayString"
_GenAppFileDateStamp_Object = MibTableColumn
genAppFileDateStamp = _GenAppFileDateStamp_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 8),
    _GenAppFileDateStamp_Type()
)
genAppFileDateStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAppFileDateStamp.setStatus("current")
_GenAppFileRowStatus_Type = RowStatus
_GenAppFileRowStatus_Object = MibTableColumn
genAppFileRowStatus = _GenAppFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 9),
    _GenAppFileRowStatus_Type()
)
genAppFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genAppFileRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOAD-MIB",
    **{"lucent": lucent,
       "products": products,
       "mibs": mibs,
       "load": load,
       "genOperations": genOperations,
       "genLoadNumberOfSession": genLoadNumberOfSession,
       "genOpTable": genOpTable,
       "genOpEntry": genOpEntry,
       "genOpModuleId": genOpModuleId,
       "genOpIndex": genOpIndex,
       "genOpRunningState": genOpRunningState,
       "genOpSourceIndex": genOpSourceIndex,
       "genOpDestIndex": genOpDestIndex,
       "genOpServerIP": genOpServerIP,
       "genOpUserName": genOpUserName,
       "genOpPassword": genOpPassword,
       "genOpProtocolType": genOpProtocolType,
       "genOpFileName": genOpFileName,
       "genOpRunningStateDisplay": genOpRunningStateDisplay,
       "genOpLastFailureIndex": genOpLastFailureIndex,
       "genOpLastFailureDisplay": genOpLastFailureDisplay,
       "genOpLastWarningDisplay": genOpLastWarningDisplay,
       "genOpErrorLogIndex": genOpErrorLogIndex,
       "genOpResetSupported": genOpResetSupported,
       "genOpEnableReset": genOpEnableReset,
       "genOpNextBootImageIndex": genOpNextBootImageIndex,
       "genOpLastBootImageIndex": genOpLastBootImageIndex,
       "genOpFileSystemType": genOpFileSystemType,
       "genOpReportSpecificFlags": genOpReportSpecificFlags,
       "genOpOctetsReceived": genOpOctetsReceived,
       "genApplications": genApplications,
       "genAppFileTable": genAppFileTable,
       "genAppFileEntry": genAppFileEntry,
       "genAppFileId": genAppFileId,
       "genAppFileName": genAppFileName,
       "genAppFileType": genAppFileType,
       "genAppFileDescription": genAppFileDescription,
       "genAppFileSize": genAppFileSize,
       "genAppFileVersionNumber": genAppFileVersionNumber,
       "genAppFileLocation": genAppFileLocation,
       "genAppFileDateStamp": genAppFileDateStamp,
       "genAppFileRowStatus": genAppFileRowStatus}
)
