# SNMP MIB module (REDSTONE-FILE-XFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-FILE-XFER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:36 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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

rsFileXferMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23)
)
rsFileXferMIB.setRevisions(
        ("1999-03-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsFileXferObjects_ObjectIdentity = ObjectIdentity
rsFileXferObjects = _RsFileXferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1)
)
_RsFileXferTable_Object = MibTable
rsFileXferTable = _RsFileXferTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    rsFileXferTable.setStatus("current")
_RsFileXferTableEntry_Object = MibTableRow
rsFileXferTableEntry = _RsFileXferTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1)
)
rsFileXferTableEntry.setIndexNames(
    (0, "REDSTONE-FILE-XFER-MIB", "rsFileXferIndex"),
)
if mibBuilder.loadTexts:
    rsFileXferTableEntry.setStatus("current")


class _RsFileXferIndex_Type(Integer32):
    """Custom type rsFileXferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsFileXferIndex_Type.__name__ = "Integer32"
_RsFileXferIndex_Object = MibTableColumn
rsFileXferIndex = _RsFileXferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 1),
    _RsFileXferIndex_Type()
)
rsFileXferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFileXferIndex.setStatus("current")


class _RsFileXferDirection_Type(Integer32):
    """Custom type rsFileXferDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsFileXferLocalToRemote", 1),
          ("rsFileXferRemoteToLocal", 2))
    )


_RsFileXferDirection_Type.__name__ = "Integer32"
_RsFileXferDirection_Object = MibTableColumn
rsFileXferDirection = _RsFileXferDirection_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 2),
    _RsFileXferDirection_Type()
)
rsFileXferDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferDirection.setStatus("current")


class _RsFileXferFileType_Type(Integer32):
    """Custom type rsFileXferFileType based on Integer32"""
    defaultValue = 7

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
        *(("rsFileXferBulkStatistics", 7),
          ("rsFileXferRebootHistory", 6),
          ("rsFileXferRunningConfig", 3),
          ("rsFileXferScript", 5),
          ("rsFileXferSoftwareRelease", 1),
          ("rsFileXferSystemConfig", 2),
          ("rsFileXferSystemLog", 4))
    )


_RsFileXferFileType_Type.__name__ = "Integer32"
_RsFileXferFileType_Object = MibTableColumn
rsFileXferFileType = _RsFileXferFileType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 3),
    _RsFileXferFileType_Type()
)
rsFileXferFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferFileType.setStatus("current")


class _RsFileXferRemoteFileName_Type(DisplayString):
    """Custom type rsFileXferRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsFileXferRemoteFileName_Type.__name__ = "DisplayString"
_RsFileXferRemoteFileName_Object = MibTableColumn
rsFileXferRemoteFileName = _RsFileXferRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 4),
    _RsFileXferRemoteFileName_Type()
)
rsFileXferRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferRemoteFileName.setStatus("current")


class _RsFileXferRemoteUserName_Type(DisplayString):
    """Custom type rsFileXferRemoteUserName based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsFileXferRemoteUserName_Type.__name__ = "DisplayString"
_RsFileXferRemoteUserName_Object = MibTableColumn
rsFileXferRemoteUserName = _RsFileXferRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 5),
    _RsFileXferRemoteUserName_Type()
)
rsFileXferRemoteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferRemoteUserName.setStatus("current")


class _RsFileXferRemoteUserPassword_Type(OctetString):
    """Custom type rsFileXferRemoteUserPassword based on OctetString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsFileXferRemoteUserPassword_Type.__name__ = "OctetString"
_RsFileXferRemoteUserPassword_Object = MibTableColumn
rsFileXferRemoteUserPassword = _RsFileXferRemoteUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 6),
    _RsFileXferRemoteUserPassword_Type()
)
rsFileXferRemoteUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferRemoteUserPassword.setStatus("current")


class _RsFileXferLocalFileName_Type(DisplayString):
    """Custom type rsFileXferLocalFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RsFileXferLocalFileName_Type.__name__ = "DisplayString"
_RsFileXferLocalFileName_Object = MibTableColumn
rsFileXferLocalFileName = _RsFileXferLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 7),
    _RsFileXferLocalFileName_Type()
)
rsFileXferLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferLocalFileName.setStatus("current")


class _RsFileXferProtocol_Type(Integer32):
    """Custom type rsFileXferProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsFileXferFtp", 1),
          ("rsFileXferTftp", 2))
    )


_RsFileXferProtocol_Type.__name__ = "Integer32"
_RsFileXferProtocol_Object = MibTableColumn
rsFileXferProtocol = _RsFileXferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 8),
    _RsFileXferProtocol_Type()
)
rsFileXferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferProtocol.setStatus("current")


class _RsFileXferStatus_Type(Integer32):
    """Custom type rsFileXferStatus based on Integer32"""
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
        *(("rsFileXferFileIncompatible", 7),
          ("rsFileXferFileNotFound", 5),
          ("rsFileXferFileTooBig", 6),
          ("rsFileXferInProgress", 2),
          ("rsFileXferPended", 8),
          ("rsFileXferRemoteUnreachable", 3),
          ("rsFileXferSuccessfulCompletion", 1),
          ("rsFileXferUserAuthFailed", 4))
    )


_RsFileXferStatus_Type.__name__ = "Integer32"
_RsFileXferStatus_Object = MibTableColumn
rsFileXferStatus = _RsFileXferStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 9),
    _RsFileXferStatus_Type()
)
rsFileXferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFileXferStatus.setStatus("current")
_RsFileXferRowStatus_Type = RowStatus
_RsFileXferRowStatus_Object = MibTableColumn
rsFileXferRowStatus = _RsFileXferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 10),
    _RsFileXferRowStatus_Type()
)
rsFileXferRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferRowStatus.setStatus("current")
_RsFileXferTimeStamp_Type = TimeTicks
_RsFileXferTimeStamp_Object = MibTableColumn
rsFileXferTimeStamp = _RsFileXferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 1, 1, 11),
    _RsFileXferTimeStamp_Type()
)
rsFileXferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFileXferTimeStamp.setStatus("current")


class _RsFileXferTrapEnabled_Type(Integer32):
    """Custom type rsFileXferTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_RsFileXferTrapEnabled_Type.__name__ = "Integer32"
_RsFileXferTrapEnabled_Object = MibScalar
rsFileXferTrapEnabled = _RsFileXferTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 1, 2),
    _RsFileXferTrapEnabled_Type()
)
rsFileXferTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileXferTrapEnabled.setStatus("current")
_RsFileXferNotifications_ObjectIdentity = ObjectIdentity
rsFileXferNotifications = _RsFileXferNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 2)
)
_RsFileXferNotifyPrefix_ObjectIdentity = ObjectIdentity
rsFileXferNotifyPrefix = _RsFileXferNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 2, 0)
)

# Managed Objects groups


# Notification objects

rsFileXferTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2773, 2, 23, 2, 0, 1)
)
rsFileXferTrap.setObjects(
      *(("REDSTONE-FILE-XFER-MIB", "rsFileXferStatus"),
        ("REDSTONE-FILE-XFER-MIB", "rsFileXferTimeStamp"))
)
if mibBuilder.loadTexts:
    rsFileXferTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-FILE-XFER-MIB",
    **{"rsFileXferMIB": rsFileXferMIB,
       "rsFileXferObjects": rsFileXferObjects,
       "rsFileXferTable": rsFileXferTable,
       "rsFileXferTableEntry": rsFileXferTableEntry,
       "rsFileXferIndex": rsFileXferIndex,
       "rsFileXferDirection": rsFileXferDirection,
       "rsFileXferFileType": rsFileXferFileType,
       "rsFileXferRemoteFileName": rsFileXferRemoteFileName,
       "rsFileXferRemoteUserName": rsFileXferRemoteUserName,
       "rsFileXferRemoteUserPassword": rsFileXferRemoteUserPassword,
       "rsFileXferLocalFileName": rsFileXferLocalFileName,
       "rsFileXferProtocol": rsFileXferProtocol,
       "rsFileXferStatus": rsFileXferStatus,
       "rsFileXferRowStatus": rsFileXferRowStatus,
       "rsFileXferTimeStamp": rsFileXferTimeStamp,
       "rsFileXferTrapEnabled": rsFileXferTrapEnabled,
       "rsFileXferNotifications": rsFileXferNotifications,
       "rsFileXferNotifyPrefix": rsFileXferNotifyPrefix,
       "rsFileXferTrap": rsFileXferTrap}
)
