# SNMP MIB module (CIENA-CES-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:06 2024
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

(cienaCesConfig,
 cienaCommon) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCommon")

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


# MODULE-IDENTITY

cienaCesRmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34)
)
cienaCesRmonMIB.setRevisions(
        ("2014-11-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesRmonMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesRmonMIBObjects = _CienaCesRmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1)
)
_CienaCesRmon_ObjectIdentity = ObjectIdentity
cienaCesRmon = _CienaCesRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1)
)
_CienaCesRmonTransfer_ObjectIdentity = ObjectIdentity
cienaCesRmonTransfer = _CienaCesRmonTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1)
)
_CienaCesRmonTransferServerTable_Object = MibTable
cienaCesRmonTransferServerTable = _CienaCesRmonTransferServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerTable.setStatus("current")
_CienaCesRmonTransferServerEntry_Object = MibTableRow
cienaCesRmonTransferServerEntry = _CienaCesRmonTransferServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1)
)
cienaCesRmonTransferServerEntry.setIndexNames(
    (0, "CIENA-CES-RMON-MIB", "cienaCesRmonTransferServerIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerEntry.setStatus("current")


class _CienaCesRmonTransferServerIndex_Type(Integer32):
    """Custom type cienaCesRmonTransferServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CienaCesRmonTransferServerIndex_Type.__name__ = "Integer32"
_CienaCesRmonTransferServerIndex_Object = MibTableColumn
cienaCesRmonTransferServerIndex = _CienaCesRmonTransferServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 1),
    _CienaCesRmonTransferServerIndex_Type()
)
cienaCesRmonTransferServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerIndex.setStatus("current")


class _CienaCesRmonTransferServerServer_Type(DisplayString):
    """Custom type cienaCesRmonTransferServerServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CienaCesRmonTransferServerServer_Type.__name__ = "DisplayString"
_CienaCesRmonTransferServerServer_Object = MibTableColumn
cienaCesRmonTransferServerServer = _CienaCesRmonTransferServerServer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 2),
    _CienaCesRmonTransferServerServer_Type()
)
cienaCesRmonTransferServerServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerServer.setStatus("current")


class _CienaCesRmonTransferServerLastRemoteName_Type(DisplayString):
    """Custom type cienaCesRmonTransferServerLastRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CienaCesRmonTransferServerLastRemoteName_Type.__name__ = "DisplayString"
_CienaCesRmonTransferServerLastRemoteName_Object = MibTableColumn
cienaCesRmonTransferServerLastRemoteName = _CienaCesRmonTransferServerLastRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 3),
    _CienaCesRmonTransferServerLastRemoteName_Type()
)
cienaCesRmonTransferServerLastRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerLastRemoteName.setStatus("current")


class _CienaCesRmonTransferServerLastPushTime_Type(DisplayString):
    """Custom type cienaCesRmonTransferServerLastPushTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesRmonTransferServerLastPushTime_Type.__name__ = "DisplayString"
_CienaCesRmonTransferServerLastPushTime_Object = MibTableColumn
cienaCesRmonTransferServerLastPushTime = _CienaCesRmonTransferServerLastPushTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 4),
    _CienaCesRmonTransferServerLastPushTime_Type()
)
cienaCesRmonTransferServerLastPushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerLastPushTime.setStatus("current")


class _CienaCesRmonTransferServerLastPushStatus_Type(DisplayString):
    """Custom type cienaCesRmonTransferServerLastPushStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CienaCesRmonTransferServerLastPushStatus_Type.__name__ = "DisplayString"
_CienaCesRmonTransferServerLastPushStatus_Object = MibTableColumn
cienaCesRmonTransferServerLastPushStatus = _CienaCesRmonTransferServerLastPushStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 5),
    _CienaCesRmonTransferServerLastPushStatus_Type()
)
cienaCesRmonTransferServerLastPushStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerLastPushStatus.setStatus("current")


class _CienaCesRmonTransferServerXftpTransferMode_Type(Integer32):
    """Custom type cienaCesRmonTransferServerXftpTransferMode based on Integer32"""
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


_CienaCesRmonTransferServerXftpTransferMode_Type.__name__ = "Integer32"
_CienaCesRmonTransferServerXftpTransferMode_Object = MibTableColumn
cienaCesRmonTransferServerXftpTransferMode = _CienaCesRmonTransferServerXftpTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 6),
    _CienaCesRmonTransferServerXftpTransferMode_Type()
)
cienaCesRmonTransferServerXftpTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerXftpTransferMode.setStatus("current")


class _CienaCesRmonTransferServerXftpLoginId_Type(DisplayString):
    """Custom type cienaCesRmonTransferServerXftpLoginId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesRmonTransferServerXftpLoginId_Type.__name__ = "DisplayString"
_CienaCesRmonTransferServerXftpLoginId_Object = MibTableColumn
cienaCesRmonTransferServerXftpLoginId = _CienaCesRmonTransferServerXftpLoginId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 7),
    _CienaCesRmonTransferServerXftpLoginId_Type()
)
cienaCesRmonTransferServerXftpLoginId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerXftpLoginId.setStatus("current")


class _CienaCesRmonTransferServerXftpPassword_Type(DisplayString):
    """Custom type cienaCesRmonTransferServerXftpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CienaCesRmonTransferServerXftpPassword_Type.__name__ = "DisplayString"
_CienaCesRmonTransferServerXftpPassword_Object = MibTableColumn
cienaCesRmonTransferServerXftpPassword = _CienaCesRmonTransferServerXftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 8),
    _CienaCesRmonTransferServerXftpPassword_Type()
)
cienaCesRmonTransferServerXftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerXftpPassword.setStatus("current")


class _CienaCesRmonTransferServerXftpSecret_Type(OctetString):
    """Custom type cienaCesRmonTransferServerXftpSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 259),
    )


_CienaCesRmonTransferServerXftpSecret_Type.__name__ = "OctetString"
_CienaCesRmonTransferServerXftpSecret_Object = MibTableColumn
cienaCesRmonTransferServerXftpSecret = _CienaCesRmonTransferServerXftpSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 1, 1, 9),
    _CienaCesRmonTransferServerXftpSecret_Type()
)
cienaCesRmonTransferServerXftpSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferServerXftpSecret.setStatus("current")


class _CienaCesRmonTransferName_Type(DisplayString):
    """Custom type cienaCesRmonTransferName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CienaCesRmonTransferName_Type.__name__ = "DisplayString"
_CienaCesRmonTransferName_Object = MibScalar
cienaCesRmonTransferName = _CienaCesRmonTransferName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 2),
    _CienaCesRmonTransferName_Type()
)
cienaCesRmonTransferName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferName.setStatus("current")


class _CienaCesRmonTransferRemoteDir_Type(DisplayString):
    """Custom type cienaCesRmonTransferRemoteDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CienaCesRmonTransferRemoteDir_Type.__name__ = "DisplayString"
_CienaCesRmonTransferRemoteDir_Object = MibScalar
cienaCesRmonTransferRemoteDir = _CienaCesRmonTransferRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 3),
    _CienaCesRmonTransferRemoteDir_Type()
)
cienaCesRmonTransferRemoteDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferRemoteDir.setStatus("current")


class _CienaCesRmonTransferInterval_Type(Integer32):
    """Custom type cienaCesRmonTransferInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 31536000),
    )


_CienaCesRmonTransferInterval_Type.__name__ = "Integer32"
_CienaCesRmonTransferInterval_Object = MibScalar
cienaCesRmonTransferInterval = _CienaCesRmonTransferInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 4),
    _CienaCesRmonTransferInterval_Type()
)
cienaCesRmonTransferInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferInterval.setStatus("current")


class _CienaCesRmonTransferUserFilesKept_Type(Integer32):
    """Custom type cienaCesRmonTransferUserFilesKept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CienaCesRmonTransferUserFilesKept_Type.__name__ = "Integer32"
_CienaCesRmonTransferUserFilesKept_Object = MibScalar
cienaCesRmonTransferUserFilesKept = _CienaCesRmonTransferUserFilesKept_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 5),
    _CienaCesRmonTransferUserFilesKept_Type()
)
cienaCesRmonTransferUserFilesKept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferUserFilesKept.setStatus("current")


class _CienaCesRmonTransferMaxFiles_Type(Integer32):
    """Custom type cienaCesRmonTransferMaxFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CienaCesRmonTransferMaxFiles_Type.__name__ = "Integer32"
_CienaCesRmonTransferMaxFiles_Object = MibScalar
cienaCesRmonTransferMaxFiles = _CienaCesRmonTransferMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 6),
    _CienaCesRmonTransferMaxFiles_Type()
)
cienaCesRmonTransferMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRmonTransferMaxFiles.setStatus("current")
_CienaCesRmonTransferPushRecentFiles_Type = TruthValue
_CienaCesRmonTransferPushRecentFiles_Object = MibScalar
cienaCesRmonTransferPushRecentFiles = _CienaCesRmonTransferPushRecentFiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 7),
    _CienaCesRmonTransferPushRecentFiles_Type()
)
cienaCesRmonTransferPushRecentFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferPushRecentFiles.setStatus("current")


class _CienaCesRmonTransferState_Type(Integer32):
    """Custom type cienaCesRmonTransferState based on Integer32"""
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


_CienaCesRmonTransferState_Type.__name__ = "Integer32"
_CienaCesRmonTransferState_Object = MibScalar
cienaCesRmonTransferState = _CienaCesRmonTransferState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 1, 8),
    _CienaCesRmonTransferState_Type()
)
cienaCesRmonTransferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonTransferState.setStatus("current")
_CienaCesRmonAutoConfigure_ObjectIdentity = ObjectIdentity
cienaCesRmonAutoConfigure = _CienaCesRmonAutoConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 2)
)


class _CienaCesRmonHistAutoConfigState_Type(Integer32):
    """Custom type cienaCesRmonHistAutoConfigState based on Integer32"""
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


_CienaCesRmonHistAutoConfigState_Type.__name__ = "Integer32"
_CienaCesRmonHistAutoConfigState_Object = MibScalar
cienaCesRmonHistAutoConfigState = _CienaCesRmonHistAutoConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 2, 1),
    _CienaCesRmonHistAutoConfigState_Type()
)
cienaCesRmonHistAutoConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonHistAutoConfigState.setStatus("current")


class _CienaCesRmonHistAutoConfigFileLogging_Type(Integer32):
    """Custom type cienaCesRmonHistAutoConfigFileLogging based on Integer32"""
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


_CienaCesRmonHistAutoConfigFileLogging_Type.__name__ = "Integer32"
_CienaCesRmonHistAutoConfigFileLogging_Object = MibScalar
cienaCesRmonHistAutoConfigFileLogging = _CienaCesRmonHistAutoConfigFileLogging_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 2, 2),
    _CienaCesRmonHistAutoConfigFileLogging_Type()
)
cienaCesRmonHistAutoConfigFileLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonHistAutoConfigFileLogging.setStatus("current")


class _CienaCesRmonHistAutoConfigInterval_Type(Integer32):
    """Custom type cienaCesRmonHistAutoConfigInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRmonHistAutoConfigInterval_Type.__name__ = "Integer32"
_CienaCesRmonHistAutoConfigInterval_Object = MibScalar
cienaCesRmonHistAutoConfigInterval = _CienaCesRmonHistAutoConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 2, 3),
    _CienaCesRmonHistAutoConfigInterval_Type()
)
cienaCesRmonHistAutoConfigInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonHistAutoConfigInterval.setStatus("current")


class _CienaCesRmonHistAutoConfigNumBuckets_Type(Integer32):
    """Custom type cienaCesRmonHistAutoConfigNumBuckets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRmonHistAutoConfigNumBuckets_Type.__name__ = "Integer32"
_CienaCesRmonHistAutoConfigNumBuckets_Object = MibScalar
cienaCesRmonHistAutoConfigNumBuckets = _CienaCesRmonHistAutoConfigNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 2, 4),
    _CienaCesRmonHistAutoConfigNumBuckets_Type()
)
cienaCesRmonHistAutoConfigNumBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonHistAutoConfigNumBuckets.setStatus("current")


class _CienaCesRmonHistAutoConfigOwner_Type(DisplayString):
    """Custom type cienaCesRmonHistAutoConfigOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CienaCesRmonHistAutoConfigOwner_Type.__name__ = "DisplayString"
_CienaCesRmonHistAutoConfigOwner_Object = MibScalar
cienaCesRmonHistAutoConfigOwner = _CienaCesRmonHistAutoConfigOwner_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 2, 5),
    _CienaCesRmonHistAutoConfigOwner_Type()
)
cienaCesRmonHistAutoConfigOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonHistAutoConfigOwner.setStatus("current")


class _CienaCesRmonHistAutoConfigStatistics_Type(Integer32):
    """Custom type cienaCesRmonHistAutoConfigStatistics based on Integer32"""
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
              18,
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
          ("rxAllBasicError", 22),
          ("rxAllBasicRx", 18),
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
          ("txAllBasicRx", 10),
          ("txAllErrorAll", 45),
          ("txAllRxBasicErrorAll", 47))
    )


_CienaCesRmonHistAutoConfigStatistics_Type.__name__ = "Integer32"
_CienaCesRmonHistAutoConfigStatistics_Object = MibScalar
cienaCesRmonHistAutoConfigStatistics = _CienaCesRmonHistAutoConfigStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 1, 1, 2, 6),
    _CienaCesRmonHistAutoConfigStatistics_Type()
)
cienaCesRmonHistAutoConfigStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRmonHistAutoConfigStatistics.setStatus("current")
_CienaCesRmonMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesRmonMIBNotificationPrefix = _CienaCesRmonMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 2)
)
_CienaCesRmonMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesRmonMIBNotifications = _CienaCesRmonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 2, 0)
)
_CienaCesRmonMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesRmonMIBConformance = _CienaCesRmonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 3)
)
_CienaCesRmonsMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesRmonsMIBCompliances = _CienaCesRmonsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 3, 1)
)
_CienaCesRmonMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesRmonMIBGroups = _CienaCesRmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 34, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-RMON-MIB",
    **{"cienaCesRmonMIB": cienaCesRmonMIB,
       "cienaCesRmonMIBObjects": cienaCesRmonMIBObjects,
       "cienaCesRmon": cienaCesRmon,
       "cienaCesRmonTransfer": cienaCesRmonTransfer,
       "cienaCesRmonTransferServerTable": cienaCesRmonTransferServerTable,
       "cienaCesRmonTransferServerEntry": cienaCesRmonTransferServerEntry,
       "cienaCesRmonTransferServerIndex": cienaCesRmonTransferServerIndex,
       "cienaCesRmonTransferServerServer": cienaCesRmonTransferServerServer,
       "cienaCesRmonTransferServerLastRemoteName": cienaCesRmonTransferServerLastRemoteName,
       "cienaCesRmonTransferServerLastPushTime": cienaCesRmonTransferServerLastPushTime,
       "cienaCesRmonTransferServerLastPushStatus": cienaCesRmonTransferServerLastPushStatus,
       "cienaCesRmonTransferServerXftpTransferMode": cienaCesRmonTransferServerXftpTransferMode,
       "cienaCesRmonTransferServerXftpLoginId": cienaCesRmonTransferServerXftpLoginId,
       "cienaCesRmonTransferServerXftpPassword": cienaCesRmonTransferServerXftpPassword,
       "cienaCesRmonTransferServerXftpSecret": cienaCesRmonTransferServerXftpSecret,
       "cienaCesRmonTransferName": cienaCesRmonTransferName,
       "cienaCesRmonTransferRemoteDir": cienaCesRmonTransferRemoteDir,
       "cienaCesRmonTransferInterval": cienaCesRmonTransferInterval,
       "cienaCesRmonTransferUserFilesKept": cienaCesRmonTransferUserFilesKept,
       "cienaCesRmonTransferMaxFiles": cienaCesRmonTransferMaxFiles,
       "cienaCesRmonTransferPushRecentFiles": cienaCesRmonTransferPushRecentFiles,
       "cienaCesRmonTransferState": cienaCesRmonTransferState,
       "cienaCesRmonAutoConfigure": cienaCesRmonAutoConfigure,
       "cienaCesRmonHistAutoConfigState": cienaCesRmonHistAutoConfigState,
       "cienaCesRmonHistAutoConfigFileLogging": cienaCesRmonHistAutoConfigFileLogging,
       "cienaCesRmonHistAutoConfigInterval": cienaCesRmonHistAutoConfigInterval,
       "cienaCesRmonHistAutoConfigNumBuckets": cienaCesRmonHistAutoConfigNumBuckets,
       "cienaCesRmonHistAutoConfigOwner": cienaCesRmonHistAutoConfigOwner,
       "cienaCesRmonHistAutoConfigStatistics": cienaCesRmonHistAutoConfigStatistics,
       "cienaCesRmonMIBNotificationPrefix": cienaCesRmonMIBNotificationPrefix,
       "cienaCesRmonMIBNotifications": cienaCesRmonMIBNotifications,
       "cienaCesRmonMIBConformance": cienaCesRmonMIBConformance,
       "cienaCesRmonsMIBCompliances": cienaCesRmonsMIBCompliances,
       "cienaCesRmonMIBGroups": cienaCesRmonMIBGroups}
)
