# SNMP MIB module (Juniper-FILE-XFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-FILE-XFER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:16 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniName,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniName")

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


# MODULE-IDENTITY

juniFileXferMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23)
)
juniFileXferMIB.setRevisions(
        ("2002-09-16 21:44",
         "2001-03-28 13:46",
         "2000-05-01 00:00",
         "1999-08-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniFileXferObjects_ObjectIdentity = ObjectIdentity
juniFileXferObjects = _JuniFileXferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1)
)
_JuniFileXferTable_Object = MibTable
juniFileXferTable = _JuniFileXferTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    juniFileXferTable.setStatus("current")
_JuniFileXferTableEntry_Object = MibTableRow
juniFileXferTableEntry = _JuniFileXferTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1)
)
juniFileXferTableEntry.setIndexNames(
    (0, "Juniper-FILE-XFER-MIB", "juniFileXferIndex"),
)
if mibBuilder.loadTexts:
    juniFileXferTableEntry.setStatus("current")


class _JuniFileXferIndex_Type(Integer32):
    """Custom type juniFileXferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniFileXferIndex_Type.__name__ = "Integer32"
_JuniFileXferIndex_Object = MibTableColumn
juniFileXferIndex = _JuniFileXferIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 1),
    _JuniFileXferIndex_Type()
)
juniFileXferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFileXferIndex.setStatus("current")


class _JuniFileXferDirection_Type(Integer32):
    """Custom type juniFileXferDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("juniFileXferLocalToRemote", 1),
          ("juniFileXferRemoteToLocal", 2))
    )


_JuniFileXferDirection_Type.__name__ = "Integer32"
_JuniFileXferDirection_Object = MibTableColumn
juniFileXferDirection = _JuniFileXferDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 2),
    _JuniFileXferDirection_Type()
)
juniFileXferDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferDirection.setStatus("current")


class _JuniFileXferFileType_Type(Integer32):
    """Custom type juniFileXferFileType based on Integer32"""
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
        *(("juniFileXferBulkStatistics", 7),
          ("juniFileXferRebootHistory", 6),
          ("juniFileXferRunningConfig", 3),
          ("juniFileXferScript", 5),
          ("juniFileXferSoftwareRelease", 1),
          ("juniFileXferSystemConfig", 2),
          ("juniFileXferSystemLog", 4))
    )


_JuniFileXferFileType_Type.__name__ = "Integer32"
_JuniFileXferFileType_Object = MibTableColumn
juniFileXferFileType = _JuniFileXferFileType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 3),
    _JuniFileXferFileType_Type()
)
juniFileXferFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferFileType.setStatus("current")


class _JuniFileXferRemoteFileName_Type(DisplayString):
    """Custom type juniFileXferRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniFileXferRemoteFileName_Type.__name__ = "DisplayString"
_JuniFileXferRemoteFileName_Object = MibTableColumn
juniFileXferRemoteFileName = _JuniFileXferRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 4),
    _JuniFileXferRemoteFileName_Type()
)
juniFileXferRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferRemoteFileName.setStatus("current")


class _JuniFileXferRemoteUserName_Type(DisplayString):
    """Custom type juniFileXferRemoteUserName based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniFileXferRemoteUserName_Type.__name__ = "DisplayString"
_JuniFileXferRemoteUserName_Object = MibTableColumn
juniFileXferRemoteUserName = _JuniFileXferRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 5),
    _JuniFileXferRemoteUserName_Type()
)
juniFileXferRemoteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferRemoteUserName.setStatus("obsolete")


class _JuniFileXferRemoteUserPassword_Type(OctetString):
    """Custom type juniFileXferRemoteUserPassword based on OctetString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniFileXferRemoteUserPassword_Type.__name__ = "OctetString"
_JuniFileXferRemoteUserPassword_Object = MibTableColumn
juniFileXferRemoteUserPassword = _JuniFileXferRemoteUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 6),
    _JuniFileXferRemoteUserPassword_Type()
)
juniFileXferRemoteUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferRemoteUserPassword.setStatus("obsolete")


class _JuniFileXferLocalFileName_Type(DisplayString):
    """Custom type juniFileXferLocalFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniFileXferLocalFileName_Type.__name__ = "DisplayString"
_JuniFileXferLocalFileName_Object = MibTableColumn
juniFileXferLocalFileName = _JuniFileXferLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 7),
    _JuniFileXferLocalFileName_Type()
)
juniFileXferLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferLocalFileName.setStatus("current")


class _JuniFileXferProtocol_Type(Integer32):
    """Custom type juniFileXferProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("juniFileXferFtp", 1),
          ("juniFileXferTftp", 2))
    )


_JuniFileXferProtocol_Type.__name__ = "Integer32"
_JuniFileXferProtocol_Object = MibTableColumn
juniFileXferProtocol = _JuniFileXferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 8),
    _JuniFileXferProtocol_Type()
)
juniFileXferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferProtocol.setStatus("current")


class _JuniFileXferStatus_Type(Integer32):
    """Custom type juniFileXferStatus based on Integer32"""
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
        *(("juniFileXferCopyRunningCfgFailed", 9),
          ("juniFileXferFileIncompatible", 7),
          ("juniFileXferFileNotFound", 5),
          ("juniFileXferFileTooBig", 6),
          ("juniFileXferInProgress", 2),
          ("juniFileXferPended", 8),
          ("juniFileXferRemoteUnreachable", 3),
          ("juniFileXferSuccessfulCompletion", 1),
          ("juniFileXferUserAuthFailed", 4))
    )


_JuniFileXferStatus_Type.__name__ = "Integer32"
_JuniFileXferStatus_Object = MibTableColumn
juniFileXferStatus = _JuniFileXferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 9),
    _JuniFileXferStatus_Type()
)
juniFileXferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFileXferStatus.setStatus("current")
_JuniFileXferRowStatus_Type = RowStatus
_JuniFileXferRowStatus_Object = MibTableColumn
juniFileXferRowStatus = _JuniFileXferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 10),
    _JuniFileXferRowStatus_Type()
)
juniFileXferRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferRowStatus.setStatus("current")
_JuniFileXferTimeStamp_Type = TimeTicks
_JuniFileXferTimeStamp_Object = MibTableColumn
juniFileXferTimeStamp = _JuniFileXferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 11),
    _JuniFileXferTimeStamp_Type()
)
juniFileXferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFileXferTimeStamp.setStatus("current")
_JuniFileXferRouterName_Type = JuniName
_JuniFileXferRouterName_Object = MibTableColumn
juniFileXferRouterName = _JuniFileXferRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 12),
    _JuniFileXferRouterName_Type()
)
juniFileXferRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferRouterName.setStatus("current")


class _JuniFileXferTrapEnabled_Type(Integer32):
    """Custom type juniFileXferTrapEnabled based on Integer32"""
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


_JuniFileXferTrapEnabled_Type.__name__ = "Integer32"
_JuniFileXferTrapEnabled_Object = MibScalar
juniFileXferTrapEnabled = _JuniFileXferTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 2),
    _JuniFileXferTrapEnabled_Type()
)
juniFileXferTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniFileXferTrapEnabled.setStatus("current")
_JuniFileXferNotifications_ObjectIdentity = ObjectIdentity
juniFileXferNotifications = _JuniFileXferNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2)
)
_JuniFileXferNotifyPrefix_ObjectIdentity = ObjectIdentity
juniFileXferNotifyPrefix = _JuniFileXferNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2, 0)
)
_JuniFileXferConformance_ObjectIdentity = ObjectIdentity
juniFileXferConformance = _JuniFileXferConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4)
)
_JuniFileXferCompliances_ObjectIdentity = ObjectIdentity
juniFileXferCompliances = _JuniFileXferCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1)
)
_JuniFileXferGroups_ObjectIdentity = ObjectIdentity
juniFileXferGroups = _JuniFileXferGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2)
)

# Managed Objects groups

juniFileXferGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 2)
)
juniFileXferGroup1.setObjects(
      *(("Juniper-FILE-XFER-MIB", "juniFileXferIndex"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferDirection"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferFileType"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteFileName"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteUserName"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteUserPassword"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferLocalFileName"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferProtocol"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferStatus"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferRowStatus"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferTimeStamp"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferTrapEnabled"))
)
if mibBuilder.loadTexts:
    juniFileXferGroup1.setStatus("obsolete")

juniFileXferGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 3)
)
juniFileXferGroup2.setObjects(
      *(("Juniper-FILE-XFER-MIB", "juniFileXferIndex"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferDirection"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferFileType"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteFileName"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferLocalFileName"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferProtocol"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferStatus"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferRowStatus"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferTimeStamp"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferRouterName"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferTrapEnabled"))
)
if mibBuilder.loadTexts:
    juniFileXferGroup2.setStatus("current")


# Notification objects

juniFileXferTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2, 0, 1)
)
juniFileXferTrap.setObjects(
      *(("Juniper-FILE-XFER-MIB", "juniFileXferStatus"),
        ("Juniper-FILE-XFER-MIB", "juniFileXferTimeStamp"))
)
if mibBuilder.loadTexts:
    juniFileXferTrap.setStatus(
        "current"
    )


# Notifications groups

juniFileXferTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 4)
)
juniFileXferTrapGroup.setObjects(
    ("Juniper-FILE-XFER-MIB", "juniFileXferTrap")
)
if mibBuilder.loadTexts:
    juniFileXferTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniFileXferCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniFileXferCompliance1.setStatus(
        "obsolete"
    )

juniFileXferCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniFileXferCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-FILE-XFER-MIB",
    **{"juniFileXferMIB": juniFileXferMIB,
       "juniFileXferObjects": juniFileXferObjects,
       "juniFileXferTable": juniFileXferTable,
       "juniFileXferTableEntry": juniFileXferTableEntry,
       "juniFileXferIndex": juniFileXferIndex,
       "juniFileXferDirection": juniFileXferDirection,
       "juniFileXferFileType": juniFileXferFileType,
       "juniFileXferRemoteFileName": juniFileXferRemoteFileName,
       "juniFileXferRemoteUserName": juniFileXferRemoteUserName,
       "juniFileXferRemoteUserPassword": juniFileXferRemoteUserPassword,
       "juniFileXferLocalFileName": juniFileXferLocalFileName,
       "juniFileXferProtocol": juniFileXferProtocol,
       "juniFileXferStatus": juniFileXferStatus,
       "juniFileXferRowStatus": juniFileXferRowStatus,
       "juniFileXferTimeStamp": juniFileXferTimeStamp,
       "juniFileXferRouterName": juniFileXferRouterName,
       "juniFileXferTrapEnabled": juniFileXferTrapEnabled,
       "juniFileXferNotifications": juniFileXferNotifications,
       "juniFileXferNotifyPrefix": juniFileXferNotifyPrefix,
       "juniFileXferTrap": juniFileXferTrap,
       "juniFileXferConformance": juniFileXferConformance,
       "juniFileXferCompliances": juniFileXferCompliances,
       "juniFileXferCompliance1": juniFileXferCompliance1,
       "juniFileXferCompliance2": juniFileXferCompliance2,
       "juniFileXferGroups": juniFileXferGroups,
       "juniFileXferGroup1": juniFileXferGroup1,
       "juniFileXferGroup2": juniFileXferGroup2,
       "juniFileXferTrapGroup": juniFileXferTrapGroup}
)
