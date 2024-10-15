# SNMP MIB module (WWP-LEOS-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:06 2024
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

wwpLeosRmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41)
)
wwpLeosRmonMIB.setRevisions(
        ("2012-06-27 00:00",
         "2011-08-01 17:00",
         "2010-06-20 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosRmonMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosRmonMIBObjects = _WwpLeosRmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1)
)
_WwpLeosRmon_ObjectIdentity = ObjectIdentity
wwpLeosRmon = _WwpLeosRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1)
)
_WwpLeosRmonFileTable_Object = MibTable
wwpLeosRmonFileTable = _WwpLeosRmonFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosRmonFileTable.setStatus("current")
_WwpLeosRmonFileEntry_Object = MibTableRow
wwpLeosRmonFileEntry = _WwpLeosRmonFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1)
)
wwpLeosRmonFileEntry.setIndexNames(
    (0, "WWP-LEOS-RMON-MIB", "wwpLeosRmonFileIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosRmonFileEntry.setStatus("current")


class _WwpLeosRmonFileIndex_Type(Integer32):
    """Custom type wwpLeosRmonFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WwpLeosRmonFileIndex_Type.__name__ = "Integer32"
_WwpLeosRmonFileIndex_Object = MibTableColumn
wwpLeosRmonFileIndex = _WwpLeosRmonFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 1),
    _WwpLeosRmonFileIndex_Type()
)
wwpLeosRmonFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRmonFileIndex.setStatus("current")


class _WwpLeosRmonFileName_Type(DisplayString):
    """Custom type wwpLeosRmonFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WwpLeosRmonFileName_Type.__name__ = "DisplayString"
_WwpLeosRmonFileName_Object = MibTableColumn
wwpLeosRmonFileName = _WwpLeosRmonFileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 2),
    _WwpLeosRmonFileName_Type()
)
wwpLeosRmonFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileName.setStatus("current")


class _WwpLeosRmonFileRemoteDir_Type(DisplayString):
    """Custom type wwpLeosRmonFileRemoteDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpLeosRmonFileRemoteDir_Type.__name__ = "DisplayString"
_WwpLeosRmonFileRemoteDir_Object = MibTableColumn
wwpLeosRmonFileRemoteDir = _WwpLeosRmonFileRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 3),
    _WwpLeosRmonFileRemoteDir_Type()
)
wwpLeosRmonFileRemoteDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileRemoteDir.setStatus("current")


class _WwpLeosRmonFileServer_Type(DisplayString):
    """Custom type wwpLeosRmonFileServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpLeosRmonFileServer_Type.__name__ = "DisplayString"
_WwpLeosRmonFileServer_Object = MibTableColumn
wwpLeosRmonFileServer = _WwpLeosRmonFileServer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 4),
    _WwpLeosRmonFileServer_Type()
)
wwpLeosRmonFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileServer.setStatus("current")


class _WwpLeosRmonFileInterval_Type(Integer32):
    """Custom type wwpLeosRmonFileInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 65535),
    )


_WwpLeosRmonFileInterval_Type.__name__ = "Integer32"
_WwpLeosRmonFileInterval_Object = MibTableColumn
wwpLeosRmonFileInterval = _WwpLeosRmonFileInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 5),
    _WwpLeosRmonFileInterval_Type()
)
wwpLeosRmonFileInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileInterval.setStatus("current")
_WwpLeosRmonFilePushLastFile_Type = TruthValue
_WwpLeosRmonFilePushLastFile_Object = MibTableColumn
wwpLeosRmonFilePushLastFile = _WwpLeosRmonFilePushLastFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 6),
    _WwpLeosRmonFilePushLastFile_Type()
)
wwpLeosRmonFilePushLastFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFilePushLastFile.setStatus("current")


class _WwpLeosRmonFileState_Type(Integer32):
    """Custom type wwpLeosRmonFileState based on Integer32"""
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


_WwpLeosRmonFileState_Type.__name__ = "Integer32"
_WwpLeosRmonFileState_Object = MibTableColumn
wwpLeosRmonFileState = _WwpLeosRmonFileState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 7),
    _WwpLeosRmonFileState_Type()
)
wwpLeosRmonFileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileState.setStatus("current")


class _WwpLeosRmonFileLastRemoteName_Type(DisplayString):
    """Custom type wwpLeosRmonFileLastRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpLeosRmonFileLastRemoteName_Type.__name__ = "DisplayString"
_WwpLeosRmonFileLastRemoteName_Object = MibTableColumn
wwpLeosRmonFileLastRemoteName = _WwpLeosRmonFileLastRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 8),
    _WwpLeosRmonFileLastRemoteName_Type()
)
wwpLeosRmonFileLastRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRmonFileLastRemoteName.setStatus("current")


class _WwpLeosRmonFileLastPushTime_Type(DisplayString):
    """Custom type wwpLeosRmonFileLastPushTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosRmonFileLastPushTime_Type.__name__ = "DisplayString"
_WwpLeosRmonFileLastPushTime_Object = MibTableColumn
wwpLeosRmonFileLastPushTime = _WwpLeosRmonFileLastPushTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 9),
    _WwpLeosRmonFileLastPushTime_Type()
)
wwpLeosRmonFileLastPushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRmonFileLastPushTime.setStatus("current")


class _WwpLeosRmonFileLastPushStatus_Type(DisplayString):
    """Custom type wwpLeosRmonFileLastPushStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpLeosRmonFileLastPushStatus_Type.__name__ = "DisplayString"
_WwpLeosRmonFileLastPushStatus_Object = MibTableColumn
wwpLeosRmonFileLastPushStatus = _WwpLeosRmonFileLastPushStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 10),
    _WwpLeosRmonFileLastPushStatus_Type()
)
wwpLeosRmonFileLastPushStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRmonFileLastPushStatus.setStatus("current")


class _WwpLeosRmonFileUserFilesKept_Type(Integer32):
    """Custom type wwpLeosRmonFileUserFilesKept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WwpLeosRmonFileUserFilesKept_Type.__name__ = "Integer32"
_WwpLeosRmonFileUserFilesKept_Object = MibTableColumn
wwpLeosRmonFileUserFilesKept = _WwpLeosRmonFileUserFilesKept_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 11),
    _WwpLeosRmonFileUserFilesKept_Type()
)
wwpLeosRmonFileUserFilesKept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileUserFilesKept.setStatus("current")


class _WwpLeosRmonFileMaxFiles_Type(Integer32):
    """Custom type wwpLeosRmonFileMaxFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WwpLeosRmonFileMaxFiles_Type.__name__ = "Integer32"
_WwpLeosRmonFileMaxFiles_Object = MibTableColumn
wwpLeosRmonFileMaxFiles = _WwpLeosRmonFileMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 12),
    _WwpLeosRmonFileMaxFiles_Type()
)
wwpLeosRmonFileMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRmonFileMaxFiles.setStatus("current")


class _WwpLeosRmonFileXftpTransferMode_Type(Integer32):
    """Custom type wwpLeosRmonFileXftpTransferMode based on Integer32"""
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


_WwpLeosRmonFileXftpTransferMode_Type.__name__ = "Integer32"
_WwpLeosRmonFileXftpTransferMode_Object = MibTableColumn
wwpLeosRmonFileXftpTransferMode = _WwpLeosRmonFileXftpTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 13),
    _WwpLeosRmonFileXftpTransferMode_Type()
)
wwpLeosRmonFileXftpTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileXftpTransferMode.setStatus("current")


class _WwpLeosRmonFileXftpLoginId_Type(DisplayString):
    """Custom type wwpLeosRmonFileXftpLoginId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosRmonFileXftpLoginId_Type.__name__ = "DisplayString"
_WwpLeosRmonFileXftpLoginId_Object = MibTableColumn
wwpLeosRmonFileXftpLoginId = _WwpLeosRmonFileXftpLoginId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 14),
    _WwpLeosRmonFileXftpLoginId_Type()
)
wwpLeosRmonFileXftpLoginId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileXftpLoginId.setStatus("current")


class _WwpLeosRmonFileXftpPassword_Type(DisplayString):
    """Custom type wwpLeosRmonFileXftpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosRmonFileXftpPassword_Type.__name__ = "DisplayString"
_WwpLeosRmonFileXftpPassword_Object = MibTableColumn
wwpLeosRmonFileXftpPassword = _WwpLeosRmonFileXftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 15),
    _WwpLeosRmonFileXftpPassword_Type()
)
wwpLeosRmonFileXftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileXftpPassword.setStatus("current")


class _WwpLeosRmonFileXftpSecret_Type(DisplayString):
    """Custom type wwpLeosRmonFileXftpSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_WwpLeosRmonFileXftpSecret_Type.__name__ = "DisplayString"
_WwpLeosRmonFileXftpSecret_Object = MibTableColumn
wwpLeosRmonFileXftpSecret = _WwpLeosRmonFileXftpSecret_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 1, 1, 16),
    _WwpLeosRmonFileXftpSecret_Type()
)
wwpLeosRmonFileXftpSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonFileXftpSecret.setStatus("current")
_WwpLeosRmonHistoryTable_Object = MibTable
wwpLeosRmonHistoryTable = _WwpLeosRmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryTable.setStatus("current")
_WwpLeosRmonHistoryEntry_Object = MibTableRow
wwpLeosRmonHistoryEntry = _WwpLeosRmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1)
)
wwpLeosRmonHistoryEntry.setIndexNames(
    (0, "WWP-LEOS-RMON-MIB", "wwpLeosRmonHistoryIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryEntry.setStatus("current")


class _WwpLeosRmonHistoryIndex_Type(Integer32):
    """Custom type wwpLeosRmonHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WwpLeosRmonHistoryIndex_Type.__name__ = "Integer32"
_WwpLeosRmonHistoryIndex_Object = MibTableColumn
wwpLeosRmonHistoryIndex = _WwpLeosRmonHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1, 1),
    _WwpLeosRmonHistoryIndex_Type()
)
wwpLeosRmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryIndex.setStatus("current")


class _WwpLeosRmonHistoryAutoConfig_Type(Integer32):
    """Custom type wwpLeosRmonHistoryAutoConfig based on Integer32"""
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


_WwpLeosRmonHistoryAutoConfig_Type.__name__ = "Integer32"
_WwpLeosRmonHistoryAutoConfig_Object = MibTableColumn
wwpLeosRmonHistoryAutoConfig = _WwpLeosRmonHistoryAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1, 2),
    _WwpLeosRmonHistoryAutoConfig_Type()
)
wwpLeosRmonHistoryAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryAutoConfig.setStatus("current")


class _WwpLeosRmonHistoryFileLogging_Type(Integer32):
    """Custom type wwpLeosRmonHistoryFileLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosRmonHistoryFileLogging_Type.__name__ = "Integer32"
_WwpLeosRmonHistoryFileLogging_Object = MibTableColumn
wwpLeosRmonHistoryFileLogging = _WwpLeosRmonHistoryFileLogging_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1, 3),
    _WwpLeosRmonHistoryFileLogging_Type()
)
wwpLeosRmonHistoryFileLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryFileLogging.setStatus("current")


class _WwpLeosRmonHistoryInterval_Type(Integer32):
    """Custom type wwpLeosRmonHistoryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosRmonHistoryInterval_Type.__name__ = "Integer32"
_WwpLeosRmonHistoryInterval_Object = MibTableColumn
wwpLeosRmonHistoryInterval = _WwpLeosRmonHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1, 4),
    _WwpLeosRmonHistoryInterval_Type()
)
wwpLeosRmonHistoryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryInterval.setStatus("current")


class _WwpLeosRmonHistoryNumBuckets_Type(Integer32):
    """Custom type wwpLeosRmonHistoryNumBuckets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosRmonHistoryNumBuckets_Type.__name__ = "Integer32"
_WwpLeosRmonHistoryNumBuckets_Object = MibTableColumn
wwpLeosRmonHistoryNumBuckets = _WwpLeosRmonHistoryNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1, 5),
    _WwpLeosRmonHistoryNumBuckets_Type()
)
wwpLeosRmonHistoryNumBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryNumBuckets.setStatus("current")


class _WwpLeosRmonHistoryOwner_Type(DisplayString):
    """Custom type wwpLeosRmonHistoryOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpLeosRmonHistoryOwner_Type.__name__ = "DisplayString"
_WwpLeosRmonHistoryOwner_Object = MibTableColumn
wwpLeosRmonHistoryOwner = _WwpLeosRmonHistoryOwner_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1, 6),
    _WwpLeosRmonHistoryOwner_Type()
)
wwpLeosRmonHistoryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryOwner.setStatus("current")


class _WwpLeosRmonHistoryStatistics_Type(Integer32):
    """Custom type wwpLeosRmonHistoryStatistics based on Integer32"""
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
              9,
              10,
              13,
              22,
              36,
              37,
              38,
              39,
              45,
              47,
              51,
              54,
              55,
              63,
              71,
              79,
              87,
              95,
              103,
              111,
              119,
              127)
        )
    )
    namedValues = NamedValues(
        *(("allStatsNoStandard", 63),
          ("allStatsWithStandard", 127),
          ("basicAll", 7),
          ("basicError", 4),
          ("basicRx", 2),
          ("basicRxBasicError", 6),
          ("basicRxBasicTx", 3),
          ("basicRxBasicTxErroAll", 39),
          ("basicRxErrorAll", 38),
          ("basicTx", 1),
          ("basicTxBasicError", 5),
          ("basicTxErrorAll", 37),
          ("errorAll", 36),
          ("none", 0),
          ("rxAll", 10),
          ("rxAllBasicError", 22),
          ("rxAllErrorAll", 54),
          ("rxAllTxBasicErrorAll", 55),
          ("rxTxAll", 51),
          ("standardErrorAll", 103),
          ("standardRmon", 71),
          ("standardRxAll", 87),
          ("standardRxAllErrorAll", 119),
          ("standardRxAllTxAll", 95),
          ("standardTxAll", 79),
          ("standardTxAllErrorAll", 111),
          ("txAll", 9),
          ("txAllBasicError", 13),
          ("txAllErrorAll", 45),
          ("txAllRxBasicErrorAll", 47))
    )


_WwpLeosRmonHistoryStatistics_Type.__name__ = "Integer32"
_WwpLeosRmonHistoryStatistics_Object = MibTableColumn
wwpLeosRmonHistoryStatistics = _WwpLeosRmonHistoryStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 1, 1, 2, 1, 7),
    _WwpLeosRmonHistoryStatistics_Type()
)
wwpLeosRmonHistoryStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRmonHistoryStatistics.setStatus("current")
_WwpLeosRmonMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosRmonMIBNotificationPrefix = _WwpLeosRmonMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 2)
)
_WwpLeosRmonMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosRmonMIBNotifications = _WwpLeosRmonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 2, 0)
)
_WwpLeosRmonMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosRmonMIBConformance = _WwpLeosRmonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 3)
)
_WwpLeosRmonsMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosRmonsMIBCompliances = _WwpLeosRmonsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 3, 1)
)
_WwpLeosRmonMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosRmonMIBGroups = _WwpLeosRmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 41, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-RMON-MIB",
    **{"wwpLeosRmonMIB": wwpLeosRmonMIB,
       "wwpLeosRmonMIBObjects": wwpLeosRmonMIBObjects,
       "wwpLeosRmon": wwpLeosRmon,
       "wwpLeosRmonFileTable": wwpLeosRmonFileTable,
       "wwpLeosRmonFileEntry": wwpLeosRmonFileEntry,
       "wwpLeosRmonFileIndex": wwpLeosRmonFileIndex,
       "wwpLeosRmonFileName": wwpLeosRmonFileName,
       "wwpLeosRmonFileRemoteDir": wwpLeosRmonFileRemoteDir,
       "wwpLeosRmonFileServer": wwpLeosRmonFileServer,
       "wwpLeosRmonFileInterval": wwpLeosRmonFileInterval,
       "wwpLeosRmonFilePushLastFile": wwpLeosRmonFilePushLastFile,
       "wwpLeosRmonFileState": wwpLeosRmonFileState,
       "wwpLeosRmonFileLastRemoteName": wwpLeosRmonFileLastRemoteName,
       "wwpLeosRmonFileLastPushTime": wwpLeosRmonFileLastPushTime,
       "wwpLeosRmonFileLastPushStatus": wwpLeosRmonFileLastPushStatus,
       "wwpLeosRmonFileUserFilesKept": wwpLeosRmonFileUserFilesKept,
       "wwpLeosRmonFileMaxFiles": wwpLeosRmonFileMaxFiles,
       "wwpLeosRmonFileXftpTransferMode": wwpLeosRmonFileXftpTransferMode,
       "wwpLeosRmonFileXftpLoginId": wwpLeosRmonFileXftpLoginId,
       "wwpLeosRmonFileXftpPassword": wwpLeosRmonFileXftpPassword,
       "wwpLeosRmonFileXftpSecret": wwpLeosRmonFileXftpSecret,
       "wwpLeosRmonHistoryTable": wwpLeosRmonHistoryTable,
       "wwpLeosRmonHistoryEntry": wwpLeosRmonHistoryEntry,
       "wwpLeosRmonHistoryIndex": wwpLeosRmonHistoryIndex,
       "wwpLeosRmonHistoryAutoConfig": wwpLeosRmonHistoryAutoConfig,
       "wwpLeosRmonHistoryFileLogging": wwpLeosRmonHistoryFileLogging,
       "wwpLeosRmonHistoryInterval": wwpLeosRmonHistoryInterval,
       "wwpLeosRmonHistoryNumBuckets": wwpLeosRmonHistoryNumBuckets,
       "wwpLeosRmonHistoryOwner": wwpLeosRmonHistoryOwner,
       "wwpLeosRmonHistoryStatistics": wwpLeosRmonHistoryStatistics,
       "wwpLeosRmonMIBNotificationPrefix": wwpLeosRmonMIBNotificationPrefix,
       "wwpLeosRmonMIBNotifications": wwpLeosRmonMIBNotifications,
       "wwpLeosRmonMIBConformance": wwpLeosRmonMIBConformance,
       "wwpLeosRmonsMIBCompliances": wwpLeosRmonsMIBCompliances,
       "wwpLeosRmonMIBGroups": wwpLeosRmonMIBGroups}
)
