# SNMP MIB module (Unisphere-Data-FILE-XFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-FILE-XFER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:42 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdName,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdName")


# MODULE-IDENTITY

usdFileXferMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23)
)
usdFileXferMIB.setRevisions(
        ("2001-03-28 13:46",
         "2000-05-01 00:00",
         "1999-08-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdFileXferObjects_ObjectIdentity = ObjectIdentity
usdFileXferObjects = _UsdFileXferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1)
)
_UsdFileXferTable_Object = MibTable
usdFileXferTable = _UsdFileXferTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    usdFileXferTable.setStatus("current")
_UsdFileXferTableEntry_Object = MibTableRow
usdFileXferTableEntry = _UsdFileXferTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1)
)
usdFileXferTableEntry.setIndexNames(
    (0, "Unisphere-Data-FILE-XFER-MIB", "usdFileXferIndex"),
)
if mibBuilder.loadTexts:
    usdFileXferTableEntry.setStatus("current")


class _UsdFileXferIndex_Type(Integer32):
    """Custom type usdFileXferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdFileXferIndex_Type.__name__ = "Integer32"
_UsdFileXferIndex_Object = MibTableColumn
usdFileXferIndex = _UsdFileXferIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 1),
    _UsdFileXferIndex_Type()
)
usdFileXferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFileXferIndex.setStatus("current")


class _UsdFileXferDirection_Type(Integer32):
    """Custom type usdFileXferDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usdFileXferLocalToRemote", 1),
          ("usdFileXferRemoteToLocal", 2))
    )


_UsdFileXferDirection_Type.__name__ = "Integer32"
_UsdFileXferDirection_Object = MibTableColumn
usdFileXferDirection = _UsdFileXferDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 2),
    _UsdFileXferDirection_Type()
)
usdFileXferDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferDirection.setStatus("current")


class _UsdFileXferFileType_Type(Integer32):
    """Custom type usdFileXferFileType based on Integer32"""
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
        *(("usdFileXferBulkStatistics", 7),
          ("usdFileXferRebootHistory", 6),
          ("usdFileXferRunningConfig", 3),
          ("usdFileXferScript", 5),
          ("usdFileXferSoftwareRelease", 1),
          ("usdFileXferSystemConfig", 2),
          ("usdFileXferSystemLog", 4))
    )


_UsdFileXferFileType_Type.__name__ = "Integer32"
_UsdFileXferFileType_Object = MibTableColumn
usdFileXferFileType = _UsdFileXferFileType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 3),
    _UsdFileXferFileType_Type()
)
usdFileXferFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferFileType.setStatus("current")


class _UsdFileXferRemoteFileName_Type(DisplayString):
    """Custom type usdFileXferRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdFileXferRemoteFileName_Type.__name__ = "DisplayString"
_UsdFileXferRemoteFileName_Object = MibTableColumn
usdFileXferRemoteFileName = _UsdFileXferRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 4),
    _UsdFileXferRemoteFileName_Type()
)
usdFileXferRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferRemoteFileName.setStatus("current")


class _UsdFileXferRemoteUserName_Type(DisplayString):
    """Custom type usdFileXferRemoteUserName based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdFileXferRemoteUserName_Type.__name__ = "DisplayString"
_UsdFileXferRemoteUserName_Object = MibTableColumn
usdFileXferRemoteUserName = _UsdFileXferRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 5),
    _UsdFileXferRemoteUserName_Type()
)
usdFileXferRemoteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferRemoteUserName.setStatus("obsolete")


class _UsdFileXferRemoteUserPassword_Type(OctetString):
    """Custom type usdFileXferRemoteUserPassword based on OctetString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdFileXferRemoteUserPassword_Type.__name__ = "OctetString"
_UsdFileXferRemoteUserPassword_Object = MibTableColumn
usdFileXferRemoteUserPassword = _UsdFileXferRemoteUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 6),
    _UsdFileXferRemoteUserPassword_Type()
)
usdFileXferRemoteUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferRemoteUserPassword.setStatus("obsolete")


class _UsdFileXferLocalFileName_Type(DisplayString):
    """Custom type usdFileXferLocalFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdFileXferLocalFileName_Type.__name__ = "DisplayString"
_UsdFileXferLocalFileName_Object = MibTableColumn
usdFileXferLocalFileName = _UsdFileXferLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 7),
    _UsdFileXferLocalFileName_Type()
)
usdFileXferLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferLocalFileName.setStatus("current")


class _UsdFileXferProtocol_Type(Integer32):
    """Custom type usdFileXferProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("usdFileXferFtp", 1),
          ("usdFileXferTftp", 2))
    )


_UsdFileXferProtocol_Type.__name__ = "Integer32"
_UsdFileXferProtocol_Object = MibTableColumn
usdFileXferProtocol = _UsdFileXferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 8),
    _UsdFileXferProtocol_Type()
)
usdFileXferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferProtocol.setStatus("current")


class _UsdFileXferStatus_Type(Integer32):
    """Custom type usdFileXferStatus based on Integer32"""
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
        *(("usdFileXferCopyRunningCfgFailed", 9),
          ("usdFileXferFileIncompatible", 7),
          ("usdFileXferFileNotFound", 5),
          ("usdFileXferFileTooBig", 6),
          ("usdFileXferInProgress", 2),
          ("usdFileXferPended", 8),
          ("usdFileXferRemoteUnreachable", 3),
          ("usdFileXferSuccessfulCompletion", 1),
          ("usdFileXferUserAuthFailed", 4))
    )


_UsdFileXferStatus_Type.__name__ = "Integer32"
_UsdFileXferStatus_Object = MibTableColumn
usdFileXferStatus = _UsdFileXferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 9),
    _UsdFileXferStatus_Type()
)
usdFileXferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFileXferStatus.setStatus("current")
_UsdFileXferRowStatus_Type = RowStatus
_UsdFileXferRowStatus_Object = MibTableColumn
usdFileXferRowStatus = _UsdFileXferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 10),
    _UsdFileXferRowStatus_Type()
)
usdFileXferRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferRowStatus.setStatus("current")
_UsdFileXferTimeStamp_Type = TimeTicks
_UsdFileXferTimeStamp_Object = MibTableColumn
usdFileXferTimeStamp = _UsdFileXferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 11),
    _UsdFileXferTimeStamp_Type()
)
usdFileXferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFileXferTimeStamp.setStatus("current")
_UsdFileXferRouterName_Type = UsdName
_UsdFileXferRouterName_Object = MibTableColumn
usdFileXferRouterName = _UsdFileXferRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 12),
    _UsdFileXferRouterName_Type()
)
usdFileXferRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferRouterName.setStatus("current")


class _UsdFileXferTrapEnabled_Type(Integer32):
    """Custom type usdFileXferTrapEnabled based on Integer32"""
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


_UsdFileXferTrapEnabled_Type.__name__ = "Integer32"
_UsdFileXferTrapEnabled_Object = MibScalar
usdFileXferTrapEnabled = _UsdFileXferTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 2),
    _UsdFileXferTrapEnabled_Type()
)
usdFileXferTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdFileXferTrapEnabled.setStatus("current")
_UsdFileXferNotifications_ObjectIdentity = ObjectIdentity
usdFileXferNotifications = _UsdFileXferNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2)
)
_UsdFileXferNotifyPrefix_ObjectIdentity = ObjectIdentity
usdFileXferNotifyPrefix = _UsdFileXferNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2, 0)
)
_UsdFileXferConformance_ObjectIdentity = ObjectIdentity
usdFileXferConformance = _UsdFileXferConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4)
)
_UsdFileXferCompliances_ObjectIdentity = ObjectIdentity
usdFileXferCompliances = _UsdFileXferCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1)
)
_UsdFileXferGroups_ObjectIdentity = ObjectIdentity
usdFileXferGroups = _UsdFileXferGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2)
)

# Managed Objects groups

usdFileXferGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 2)
)
usdFileXferGroup1.setObjects(
      *(("Unisphere-Data-FILE-XFER-MIB", "usdFileXferIndex"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferDirection"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferFileType"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferRemoteFileName"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferRemoteUserName"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferRemoteUserPassword"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferLocalFileName"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferProtocol"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferStatus"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferRowStatus"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferTimeStamp"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferTrapEnabled"))
)
if mibBuilder.loadTexts:
    usdFileXferGroup1.setStatus("obsolete")

usdFileXferGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 3)
)
usdFileXferGroup2.setObjects(
      *(("Unisphere-Data-FILE-XFER-MIB", "usdFileXferIndex"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferDirection"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferFileType"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferRemoteFileName"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferLocalFileName"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferProtocol"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferStatus"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferRowStatus"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferTimeStamp"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferRouterName"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferTrapEnabled"))
)
if mibBuilder.loadTexts:
    usdFileXferGroup2.setStatus("current")


# Notification objects

usdFileXferTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2, 0, 1)
)
usdFileXferTrap.setObjects(
      *(("Unisphere-Data-FILE-XFER-MIB", "usdFileXferStatus"),
        ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferTimeStamp"))
)
if mibBuilder.loadTexts:
    usdFileXferTrap.setStatus(
        "current"
    )


# Notifications groups

usdFileXferTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 4)
)
usdFileXferTrapGroup.setObjects(
    ("Unisphere-Data-FILE-XFER-MIB", "usdFileXferTrap")
)
if mibBuilder.loadTexts:
    usdFileXferTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

usdFileXferCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdFileXferCompliance1.setStatus(
        "obsolete"
    )

usdFileXferCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdFileXferCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-FILE-XFER-MIB",
    **{"usdFileXferMIB": usdFileXferMIB,
       "usdFileXferObjects": usdFileXferObjects,
       "usdFileXferTable": usdFileXferTable,
       "usdFileXferTableEntry": usdFileXferTableEntry,
       "usdFileXferIndex": usdFileXferIndex,
       "usdFileXferDirection": usdFileXferDirection,
       "usdFileXferFileType": usdFileXferFileType,
       "usdFileXferRemoteFileName": usdFileXferRemoteFileName,
       "usdFileXferRemoteUserName": usdFileXferRemoteUserName,
       "usdFileXferRemoteUserPassword": usdFileXferRemoteUserPassword,
       "usdFileXferLocalFileName": usdFileXferLocalFileName,
       "usdFileXferProtocol": usdFileXferProtocol,
       "usdFileXferStatus": usdFileXferStatus,
       "usdFileXferRowStatus": usdFileXferRowStatus,
       "usdFileXferTimeStamp": usdFileXferTimeStamp,
       "usdFileXferRouterName": usdFileXferRouterName,
       "usdFileXferTrapEnabled": usdFileXferTrapEnabled,
       "usdFileXferNotifications": usdFileXferNotifications,
       "usdFileXferNotifyPrefix": usdFileXferNotifyPrefix,
       "usdFileXferTrap": usdFileXferTrap,
       "usdFileXferConformance": usdFileXferConformance,
       "usdFileXferCompliances": usdFileXferCompliances,
       "usdFileXferCompliance1": usdFileXferCompliance1,
       "usdFileXferCompliance2": usdFileXferCompliance2,
       "usdFileXferGroups": usdFileXferGroups,
       "usdFileXferGroup1": usdFileXferGroup1,
       "usdFileXferGroup2": usdFileXferGroup2,
       "usdFileXferTrapGroup": usdFileXferTrapGroup}
)
