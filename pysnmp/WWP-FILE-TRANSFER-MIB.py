# SNMP MIB module (WWP-FILE-TRANSFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-FILE-TRANSFER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:41 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpFileTransferMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7)
)
wwpFileTransferMIB.setRevisions(
        ("2001-04-03 17:00",)
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

_WwpFileTransferMIBObjects_ObjectIdentity = ObjectIdentity
wwpFileTransferMIBObjects = _WwpFileTransferMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1)
)
_WwpFileTransfer_ObjectIdentity = ObjectIdentity
wwpFileTransfer = _WwpFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1)
)


class _WwpFTransferOp_Type(Integer32):
    """Custom type wwpFTransferOp based on Integer32"""
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


_WwpFTransferOp_Type.__name__ = "Integer32"
_WwpFTransferOp_Object = MibScalar
wwpFTransferOp = _WwpFTransferOp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 1),
    _WwpFTransferOp_Type()
)
wwpFTransferOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpFTransferOp.setStatus("current")


class _WwpFTransferServerAddr_Type(IpAddress):
    """Custom type wwpFTransferServerAddr based on IpAddress"""
    defaultValue = 0


_WwpFTransferServerAddr_Object = MibScalar
wwpFTransferServerAddr = _WwpFTransferServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 2),
    _WwpFTransferServerAddr_Type()
)
wwpFTransferServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpFTransferServerAddr.setStatus("current")
_WwpFTransferRemoteFilename_Type = DisplayString
_WwpFTransferRemoteFilename_Object = MibScalar
wwpFTransferRemoteFilename = _WwpFTransferRemoteFilename_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 3),
    _WwpFTransferRemoteFilename_Type()
)
wwpFTransferRemoteFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpFTransferRemoteFilename.setStatus("current")
_WwpFTransferLocalFilename_Type = DisplayString
_WwpFTransferLocalFilename_Object = MibScalar
wwpFTransferLocalFilename = _WwpFTransferLocalFilename_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 4),
    _WwpFTransferLocalFilename_Type()
)
wwpFTransferLocalFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpFTransferLocalFilename.setStatus("current")


class _WwpFTransferActivate_Type(TruthValue):
    """Custom type wwpFTransferActivate based on TruthValue"""


_WwpFTransferActivate_Object = MibScalar
wwpFTransferActivate = _WwpFTransferActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 5),
    _WwpFTransferActivate_Type()
)
wwpFTransferActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpFTransferActivate.setStatus("current")


class _WwpFTransferNotifOnCompletion_Type(TruthValue):
    """Custom type wwpFTransferNotifOnCompletion based on TruthValue"""


_WwpFTransferNotifOnCompletion_Object = MibScalar
wwpFTransferNotifOnCompletion = _WwpFTransferNotifOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 6),
    _WwpFTransferNotifOnCompletion_Type()
)
wwpFTransferNotifOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpFTransferNotifOnCompletion.setStatus("current")
_WwpFTransferStatus_Type = FileTransferState
_WwpFTransferStatus_Object = MibScalar
wwpFTransferStatus = _WwpFTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 7),
    _WwpFTransferStatus_Type()
)
wwpFTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpFTransferStatus.setStatus("current")
_WwpFTransferFailCause_Type = FileTransferFailCause
_WwpFTransferFailCause_Object = MibScalar
wwpFTransferFailCause = _WwpFTransferFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 8),
    _WwpFTransferFailCause_Type()
)
wwpFTransferFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpFTransferFailCause.setStatus("current")


class _WwpFTransferNotificationStatus_Type(Integer32):
    """Custom type wwpFTransferNotificationStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("allFilesSkipped", 11),
          ("badFileCrc", 10),
          ("cmdFileParseError", 3),
          ("couldNotGetFile", 2),
          ("couldNotPutFile", 9),
          ("downloadSuccess", 0),
          ("flashOffline", 6),
          ("inValidFileContents", 5),
          ("internalFilesystemError", 4),
          ("noStatus", 7),
          ("putSuccessful", 8),
          ("tftpServerNotFound", 1))
    )


_WwpFTransferNotificationStatus_Type.__name__ = "Integer32"
_WwpFTransferNotificationStatus_Object = MibScalar
wwpFTransferNotificationStatus = _WwpFTransferNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 9),
    _WwpFTransferNotificationStatus_Type()
)
wwpFTransferNotificationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpFTransferNotificationStatus.setStatus("current")


class _WwpFTransferNotificationInfo_Type(DisplayString):
    """Custom type wwpFTransferNotificationInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_WwpFTransferNotificationInfo_Type.__name__ = "DisplayString"
_WwpFTransferNotificationInfo_Object = MibScalar
wwpFTransferNotificationInfo = _WwpFTransferNotificationInfo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 10),
    _WwpFTransferNotificationInfo_Type()
)
wwpFTransferNotificationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpFTransferNotificationInfo.setStatus("current")
_WwpFileTransferMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpFileTransferMIBNotificationPrefix = _WwpFileTransferMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 2)
)
_WwpFiletransferMIBNotifications_ObjectIdentity = ObjectIdentity
wwpFiletransferMIBNotifications = _WwpFiletransferMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0)
)
_WwpFileTransferMIBConformance_ObjectIdentity = ObjectIdentity
wwpFileTransferMIBConformance = _WwpFileTransferMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 3)
)
_WwpFileTransferMIBCompliances_ObjectIdentity = ObjectIdentity
wwpFileTransferMIBCompliances = _WwpFileTransferMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 3, 1)
)
_WwpFileTransferMIBGroups_ObjectIdentity = ObjectIdentity
wwpFileTransferMIBGroups = _WwpFileTransferMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpFTransferCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0, 1)
)
wwpFTransferCompletion.setObjects(
      *(("WWP-FILE-TRANSFER-MIB", "wwpFTransferRemoteFilename"),
        ("WWP-FILE-TRANSFER-MIB", "wwpFTransferLocalFilename"),
        ("WWP-FILE-TRANSFER-MIB", "wwpFTransferNotificationStatus"),
        ("WWP-FILE-TRANSFER-MIB", "wwpFTransferNotificationInfo"))
)
if mibBuilder.loadTexts:
    wwpFTransferCompletion.setStatus(
        "current"
    )

wwpFTransferCmdParseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0, 2)
)
wwpFTransferCmdParseError.setObjects(
    ("WWP-FILE-TRANSFER-MIB", "wwpFTransferRemoteFilename")
)
if mibBuilder.loadTexts:
    wwpFTransferCmdParseError.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-FILE-TRANSFER-MIB",
    **{"FileTransferState": FileTransferState,
       "FileTransferFailCause": FileTransferFailCause,
       "wwpFileTransferMIB": wwpFileTransferMIB,
       "wwpFileTransferMIBObjects": wwpFileTransferMIBObjects,
       "wwpFileTransfer": wwpFileTransfer,
       "wwpFTransferOp": wwpFTransferOp,
       "wwpFTransferServerAddr": wwpFTransferServerAddr,
       "wwpFTransferRemoteFilename": wwpFTransferRemoteFilename,
       "wwpFTransferLocalFilename": wwpFTransferLocalFilename,
       "wwpFTransferActivate": wwpFTransferActivate,
       "wwpFTransferNotifOnCompletion": wwpFTransferNotifOnCompletion,
       "wwpFTransferStatus": wwpFTransferStatus,
       "wwpFTransferFailCause": wwpFTransferFailCause,
       "wwpFTransferNotificationStatus": wwpFTransferNotificationStatus,
       "wwpFTransferNotificationInfo": wwpFTransferNotificationInfo,
       "wwpFileTransferMIBNotificationPrefix": wwpFileTransferMIBNotificationPrefix,
       "wwpFiletransferMIBNotifications": wwpFiletransferMIBNotifications,
       "wwpFTransferCompletion": wwpFTransferCompletion,
       "wwpFTransferCmdParseError": wwpFTransferCmdParseError,
       "wwpFileTransferMIBConformance": wwpFileTransferMIBConformance,
       "wwpFileTransferMIBCompliances": wwpFileTransferMIBCompliances,
       "wwpFileTransferMIBGroups": wwpFileTransferMIBGroups}
)
