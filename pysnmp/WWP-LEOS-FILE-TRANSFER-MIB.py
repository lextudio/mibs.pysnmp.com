# SNMP MIB module (WWP-LEOS-FILE-TRANSFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-FILE-TRANSFER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:52 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

wwpLeosFileTransferMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23)
)
wwpLeosFileTransferMIB.setRevisions(
        ("2012-03-22 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FileTransferState(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 5),
          ("idle", 1),
          ("receiving", 3),
          ("sending", 2),
          ("transferComplete", 4))
    )



class FileTransferFailCause(Integer32, TextualConvention):
    status = "current"
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
        *(("commandCompleted", 6),
          ("commandFileParseError", 8),
          ("internalError", 7),
          ("invalidFileName", 5),
          ("networkError", 3),
          ("noSpace", 4),
          ("noStatus", 1),
          ("timeout", 2))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosFileTransferMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosFileTransferMIBObjects = _WwpLeosFileTransferMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1)
)
_WwpLeosFileTransfer_ObjectIdentity = ObjectIdentity
wwpLeosFileTransfer = _WwpLeosFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1)
)


class _WwpLeosFTransferOp_Type(Integer32):
    """Custom type wwpLeosFTransferOp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("getCmdFile", 3),
          ("getFile", 2),
          ("none", 0),
          ("sendFile", 1))
    )


_WwpLeosFTransferOp_Type.__name__ = "Integer32"
_WwpLeosFTransferOp_Object = MibScalar
wwpLeosFTransferOp = _WwpLeosFTransferOp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 1),
    _WwpLeosFTransferOp_Type()
)
wwpLeosFTransferOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferOp.setStatus("current")


class _WwpLeosFTransferServerAddr_Type(IpAddress):
    """Custom type wwpLeosFTransferServerAddr based on IpAddress"""
    defaultHexValue = "00000000"


_WwpLeosFTransferServerAddr_Object = MibScalar
wwpLeosFTransferServerAddr = _WwpLeosFTransferServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 2),
    _WwpLeosFTransferServerAddr_Type()
)
wwpLeosFTransferServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferServerAddr.setStatus("current")


class _WwpLeosFTransferRemoteFilename_Type(OctetString):
    """Custom type wwpLeosFTransferRemoteFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WwpLeosFTransferRemoteFilename_Type.__name__ = "OctetString"
_WwpLeosFTransferRemoteFilename_Object = MibScalar
wwpLeosFTransferRemoteFilename = _WwpLeosFTransferRemoteFilename_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 3),
    _WwpLeosFTransferRemoteFilename_Type()
)
wwpLeosFTransferRemoteFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferRemoteFilename.setStatus("current")


class _WwpLeosFTransferLocalFilename_Type(OctetString):
    """Custom type wwpLeosFTransferLocalFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WwpLeosFTransferLocalFilename_Type.__name__ = "OctetString"
_WwpLeosFTransferLocalFilename_Object = MibScalar
wwpLeosFTransferLocalFilename = _WwpLeosFTransferLocalFilename_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 4),
    _WwpLeosFTransferLocalFilename_Type()
)
wwpLeosFTransferLocalFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferLocalFilename.setStatus("current")


class _WwpLeosFTransferActivate_Type(TruthValue):
    """Custom type wwpLeosFTransferActivate based on TruthValue"""


_WwpLeosFTransferActivate_Object = MibScalar
wwpLeosFTransferActivate = _WwpLeosFTransferActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 5),
    _WwpLeosFTransferActivate_Type()
)
wwpLeosFTransferActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferActivate.setStatus("current")


class _WwpLeosFTransferNotifOnCompletion_Type(TruthValue):
    """Custom type wwpLeosFTransferNotifOnCompletion based on TruthValue"""


_WwpLeosFTransferNotifOnCompletion_Object = MibScalar
wwpLeosFTransferNotifOnCompletion = _WwpLeosFTransferNotifOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 6),
    _WwpLeosFTransferNotifOnCompletion_Type()
)
wwpLeosFTransferNotifOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferNotifOnCompletion.setStatus("current")
_WwpLeosFTransferStatus_Type = FileTransferState
_WwpLeosFTransferStatus_Object = MibScalar
wwpLeosFTransferStatus = _WwpLeosFTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 7),
    _WwpLeosFTransferStatus_Type()
)
wwpLeosFTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFTransferStatus.setStatus("current")
_WwpLeosFTransferFailCause_Type = FileTransferFailCause
_WwpLeosFTransferFailCause_Object = MibScalar
wwpLeosFTransferFailCause = _WwpLeosFTransferFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 8),
    _WwpLeosFTransferFailCause_Type()
)
wwpLeosFTransferFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFTransferFailCause.setStatus("current")


class _WwpLeosFTransferNotificationStatus_Type(Integer32):
    """Custom type wwpLeosFTransferNotificationStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
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
        *(("allFilesSkipped", 11),
          ("badFileCrc", 10),
          ("cmdFileParseError", 3),
          ("couldNotGetFile", 2),
          ("couldNotPutFile", 9),
          ("downloadSuccess", 0),
          ("fileAlreadyExist", 12),
          ("fileContentsInvalid", 16),
          ("fileGetError", 13),
          ("fileNameInvalid", 20),
          ("fileNameNeeded", 22),
          ("filePathInvalid", 19),
          ("filePutError", 14),
          ("fileSystemError", 15),
          ("flashOffline", 6),
          ("inValidFileContents", 5),
          ("internalError", 24),
          ("internalFilesystemError", 4),
          ("noStatus", 7),
          ("notEnoughSpace", 23),
          ("putSuccessful", 8),
          ("serverIpAddrInvalid", 18),
          ("sourceNotFound", 21),
          ("tftpServerNotFound", 1))
    )


_WwpLeosFTransferNotificationStatus_Type.__name__ = "Integer32"
_WwpLeosFTransferNotificationStatus_Object = MibScalar
wwpLeosFTransferNotificationStatus = _WwpLeosFTransferNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 9),
    _WwpLeosFTransferNotificationStatus_Type()
)
wwpLeosFTransferNotificationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFTransferNotificationStatus.setStatus("current")


class _WwpLeosFTransferNotificationInfo_Type(OctetString):
    """Custom type wwpLeosFTransferNotificationInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_WwpLeosFTransferNotificationInfo_Type.__name__ = "OctetString"
_WwpLeosFTransferNotificationInfo_Object = MibScalar
wwpLeosFTransferNotificationInfo = _WwpLeosFTransferNotificationInfo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 10),
    _WwpLeosFTransferNotificationInfo_Type()
)
wwpLeosFTransferNotificationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFTransferNotificationInfo.setStatus("current")
_WwpLeosFTransferServerInetAddrType_Type = InetAddressType
_WwpLeosFTransferServerInetAddrType_Object = MibScalar
wwpLeosFTransferServerInetAddrType = _WwpLeosFTransferServerInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 11),
    _WwpLeosFTransferServerInetAddrType_Type()
)
wwpLeosFTransferServerInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferServerInetAddrType.setStatus("current")
_WwpLeosFTransferServerInetAddr_Type = InetAddress
_WwpLeosFTransferServerInetAddr_Object = MibScalar
wwpLeosFTransferServerInetAddr = _WwpLeosFTransferServerInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 12),
    _WwpLeosFTransferServerInetAddr_Type()
)
wwpLeosFTransferServerInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFTransferServerInetAddr.setStatus("current")
_WwpLeosFileTransferMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosFileTransferMIBNotificationPrefix = _WwpLeosFileTransferMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2)
)
_WwpLeosFiletransferMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosFiletransferMIBNotifications = _WwpLeosFiletransferMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2, 0)
)
_WwpLeosFileTransferMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosFileTransferMIBConformance = _WwpLeosFileTransferMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3)
)
_WwpLeosFileTransferMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosFileTransferMIBCompliances = _WwpLeosFileTransferMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 1)
)
_WwpLeosFileTransferMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosFileTransferMIBGroups = _WwpLeosFileTransferMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 2)
)

# Managed Objects groups

wwpLeosFileTransferIPv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 2, 1)
)
wwpLeosFileTransferIPv6Group.setObjects(
      *(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferServerInetAddrType"),
        ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferServerInetAddr"))
)
if mibBuilder.loadTexts:
    wwpLeosFileTransferIPv6Group.setStatus("current")


# Notification objects

wwpLeosFTransferCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2, 0, 1)
)
wwpLeosFTransferCompletion.setObjects(
      *(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferRemoteFilename"),
        ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferLocalFilename"),
        ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferNotificationStatus"),
        ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferNotificationInfo"))
)
if mibBuilder.loadTexts:
    wwpLeosFTransferCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

wwpLeosFileTransferCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosFileTransferCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-FILE-TRANSFER-MIB",
    **{"FileTransferState": FileTransferState,
       "FileTransferFailCause": FileTransferFailCause,
       "wwpLeosFileTransferMIB": wwpLeosFileTransferMIB,
       "wwpLeosFileTransferMIBObjects": wwpLeosFileTransferMIBObjects,
       "wwpLeosFileTransfer": wwpLeosFileTransfer,
       "wwpLeosFTransferOp": wwpLeosFTransferOp,
       "wwpLeosFTransferServerAddr": wwpLeosFTransferServerAddr,
       "wwpLeosFTransferRemoteFilename": wwpLeosFTransferRemoteFilename,
       "wwpLeosFTransferLocalFilename": wwpLeosFTransferLocalFilename,
       "wwpLeosFTransferActivate": wwpLeosFTransferActivate,
       "wwpLeosFTransferNotifOnCompletion": wwpLeosFTransferNotifOnCompletion,
       "wwpLeosFTransferStatus": wwpLeosFTransferStatus,
       "wwpLeosFTransferFailCause": wwpLeosFTransferFailCause,
       "wwpLeosFTransferNotificationStatus": wwpLeosFTransferNotificationStatus,
       "wwpLeosFTransferNotificationInfo": wwpLeosFTransferNotificationInfo,
       "wwpLeosFTransferServerInetAddrType": wwpLeosFTransferServerInetAddrType,
       "wwpLeosFTransferServerInetAddr": wwpLeosFTransferServerInetAddr,
       "wwpLeosFileTransferMIBNotificationPrefix": wwpLeosFileTransferMIBNotificationPrefix,
       "wwpLeosFiletransferMIBNotifications": wwpLeosFiletransferMIBNotifications,
       "wwpLeosFTransferCompletion": wwpLeosFTransferCompletion,
       "wwpLeosFileTransferMIBConformance": wwpLeosFileTransferMIBConformance,
       "wwpLeosFileTransferMIBCompliances": wwpLeosFileTransferMIBCompliances,
       "wwpLeosFileTransferCompliance": wwpLeosFileTransferCompliance,
       "wwpLeosFileTransferMIBGroups": wwpLeosFileTransferMIBGroups,
       "wwpLeosFileTransferIPv6Group": wwpLeosFileTransferIPv6Group}
)
