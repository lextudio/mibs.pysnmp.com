# SNMP MIB module (SALIX-ANNOUNCEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-ANNOUNCEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:21 2024
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

(atmfM4TrapAlarmSeverity,) = mibBuilder.importSymbols(
    "ATM-FORUM-M4-MIB",
    "atmfM4TrapAlarmSeverity")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(DateAndTime,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "DateAndTime")

(salixGeneric,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "salixGeneric")

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


# MODULE-IDENTITY

salixAnnouncementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixAnnouncementMIBObjects_ObjectIdentity = ObjectIdentity
salixAnnouncementMIBObjects = _SalixAnnouncementMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1)
)
_SalixAnnouncementTable_Object = MibTable
salixAnnouncementTable = _SalixAnnouncementTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    salixAnnouncementTable.setStatus("current")
_SalixAnnouncementEntry_Object = MibTableRow
salixAnnouncementEntry = _SalixAnnouncementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1)
)
salixAnnouncementEntry.setIndexNames(
    (0, "SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"),
)
if mibBuilder.loadTexts:
    salixAnnouncementEntry.setStatus("current")


class _SalixAnnouncementIndex_Type(Integer32):
    """Custom type salixAnnouncementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SalixAnnouncementIndex_Type.__name__ = "Integer32"
_SalixAnnouncementIndex_Object = MibTableColumn
salixAnnouncementIndex = _SalixAnnouncementIndex_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 1),
    _SalixAnnouncementIndex_Type()
)
salixAnnouncementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAnnouncementIndex.setStatus("current")
_SalixAnnouncementIpAddress_Type = IpAddress
_SalixAnnouncementIpAddress_Object = MibTableColumn
salixAnnouncementIpAddress = _SalixAnnouncementIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 2),
    _SalixAnnouncementIpAddress_Type()
)
salixAnnouncementIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAnnouncementIpAddress.setStatus("current")


class _SalixAnnouncementFilename_Type(DisplayString):
    """Custom type salixAnnouncementFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SalixAnnouncementFilename_Type.__name__ = "DisplayString"
_SalixAnnouncementFilename_Object = MibTableColumn
salixAnnouncementFilename = _SalixAnnouncementFilename_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 3),
    _SalixAnnouncementFilename_Type()
)
salixAnnouncementFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAnnouncementFilename.setStatus("current")


class _SalixAnnouncementUsername_Type(DisplayString):
    """Custom type salixAnnouncementUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SalixAnnouncementUsername_Type.__name__ = "DisplayString"
_SalixAnnouncementUsername_Object = MibTableColumn
salixAnnouncementUsername = _SalixAnnouncementUsername_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 4),
    _SalixAnnouncementUsername_Type()
)
salixAnnouncementUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAnnouncementUsername.setStatus("current")


class _SalixAnnouncementPassword_Type(DisplayString):
    """Custom type salixAnnouncementPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SalixAnnouncementPassword_Type.__name__ = "DisplayString"
_SalixAnnouncementPassword_Object = MibTableColumn
salixAnnouncementPassword = _SalixAnnouncementPassword_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 5),
    _SalixAnnouncementPassword_Type()
)
salixAnnouncementPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAnnouncementPassword.setStatus("current")


class _SalixAnnouncementRequest_Type(Integer32):
    """Custom type salixAnnouncementRequest based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("start", 1),
          ("update", 2))
    )


_SalixAnnouncementRequest_Type.__name__ = "Integer32"
_SalixAnnouncementRequest_Object = MibTableColumn
salixAnnouncementRequest = _SalixAnnouncementRequest_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 6),
    _SalixAnnouncementRequest_Type()
)
salixAnnouncementRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAnnouncementRequest.setStatus("current")


class _SalixAnnouncementState_Type(Integer32):
    """Custom type salixAnnouncementState based on Integer32"""
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
        *(("aborted", 4),
          ("failed", 5),
          ("inProgress", 2),
          ("installInProgress", 7),
          ("locked", 6),
          ("none", 1),
          ("success", 3))
    )


_SalixAnnouncementState_Type.__name__ = "Integer32"
_SalixAnnouncementState_Object = MibTableColumn
salixAnnouncementState = _SalixAnnouncementState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 7),
    _SalixAnnouncementState_Type()
)
salixAnnouncementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAnnouncementState.setStatus("current")


class _SalixAnnouncementDescription_Type(DisplayString):
    """Custom type salixAnnouncementDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SalixAnnouncementDescription_Type.__name__ = "DisplayString"
_SalixAnnouncementDescription_Object = MibTableColumn
salixAnnouncementDescription = _SalixAnnouncementDescription_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 8),
    _SalixAnnouncementDescription_Type()
)
salixAnnouncementDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixAnnouncementDescription.setStatus("current")
_SalixAnnouncementInstall_Type = DateAndTime
_SalixAnnouncementInstall_Object = MibTableColumn
salixAnnouncementInstall = _SalixAnnouncementInstall_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 9),
    _SalixAnnouncementInstall_Type()
)
salixAnnouncementInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAnnouncementInstall.setStatus("current")
_SalixAnnouncementFull_Type = TruthValue
_SalixAnnouncementFull_Object = MibTableColumn
salixAnnouncementFull = _SalixAnnouncementFull_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 10),
    _SalixAnnouncementFull_Type()
)
salixAnnouncementFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAnnouncementFull.setStatus("current")


class _SalixAnnouncementStatusMessage_Type(OctetString):
    """Custom type salixAnnouncementStatusMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_SalixAnnouncementStatusMessage_Type.__name__ = "OctetString"
_SalixAnnouncementStatusMessage_Object = MibTableColumn
salixAnnouncementStatusMessage = _SalixAnnouncementStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 1, 1, 11),
    _SalixAnnouncementStatusMessage_Type()
)
salixAnnouncementStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAnnouncementStatusMessage.setStatus("current")
_SalixAnnouncementMappingTable_Object = MibTable
salixAnnouncementMappingTable = _SalixAnnouncementMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    salixAnnouncementMappingTable.setStatus("current")
_SalixAnnouncementMappingEntry_Object = MibTableRow
salixAnnouncementMappingEntry = _SalixAnnouncementMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 2, 1)
)
salixAnnouncementMappingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"),
)
if mibBuilder.loadTexts:
    salixAnnouncementMappingEntry.setStatus("current")


class _SalixAnnouncementMappingStatus_Type(Integer32):
    """Custom type salixAnnouncementMappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadInProgress", 2),
          ("error", 3),
          ("ready", 1))
    )


_SalixAnnouncementMappingStatus_Type.__name__ = "Integer32"
_SalixAnnouncementMappingStatus_Object = MibTableColumn
salixAnnouncementMappingStatus = _SalixAnnouncementMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 1, 2, 1, 1),
    _SalixAnnouncementMappingStatus_Type()
)
salixAnnouncementMappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixAnnouncementMappingStatus.setStatus("current")
_SalixAnnouncementMIBTraps_ObjectIdentity = ObjectIdentity
salixAnnouncementMIBTraps = _SalixAnnouncementMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 2)
)
_SalixAnnouncementMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixAnnouncementMIBTrapPrefix = _SalixAnnouncementMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 2, 0)
)
_SalixAnnouncementMIBCompliance_ObjectIdentity = ObjectIdentity
salixAnnouncementMIBCompliance = _SalixAnnouncementMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 3)
)
_SalixAnnouncementGroups_ObjectIdentity = ObjectIdentity
salixAnnouncementGroups = _SalixAnnouncementGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 1)
)
_SalixAnnouncementCompliances_ObjectIdentity = ObjectIdentity
salixAnnouncementCompliances = _SalixAnnouncementCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 2)
)

# Managed Objects groups

salixAnnouncementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 1, 1)
)
salixAnnouncementGroup.setObjects(
      *(("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIpAddress"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementFilename"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementUsername"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementPassword"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementRequest"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementState"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementDescription"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementInstall"))
)
if mibBuilder.loadTexts:
    salixAnnouncementGroup.setStatus("current")

salixAnnouncementMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 1, 2)
)
salixAnnouncementMappingGroup.setObjects(
    ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementMappingStatus")
)
if mibBuilder.loadTexts:
    salixAnnouncementMappingGroup.setStatus("current")


# Notification objects

salixAnnouncementInstallFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 2, 0, 1)
)
salixAnnouncementInstallFailure.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixAnnouncementInstallFailure.setStatus(
        "current"
    )

salixAnnouncementInstallSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 2, 0, 2)
)
salixAnnouncementInstallSuccess.setObjects(
      *(("SALIX-ANNOUNCEMENT-MIB", "salixAnnouncementIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixAnnouncementInstallSuccess.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

salixAnnouncementCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 2, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixAnnouncementCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-ANNOUNCEMENT-MIB",
    **{"salixAnnouncementMIB": salixAnnouncementMIB,
       "salixAnnouncementMIBObjects": salixAnnouncementMIBObjects,
       "salixAnnouncementTable": salixAnnouncementTable,
       "salixAnnouncementEntry": salixAnnouncementEntry,
       "salixAnnouncementIndex": salixAnnouncementIndex,
       "salixAnnouncementIpAddress": salixAnnouncementIpAddress,
       "salixAnnouncementFilename": salixAnnouncementFilename,
       "salixAnnouncementUsername": salixAnnouncementUsername,
       "salixAnnouncementPassword": salixAnnouncementPassword,
       "salixAnnouncementRequest": salixAnnouncementRequest,
       "salixAnnouncementState": salixAnnouncementState,
       "salixAnnouncementDescription": salixAnnouncementDescription,
       "salixAnnouncementInstall": salixAnnouncementInstall,
       "salixAnnouncementFull": salixAnnouncementFull,
       "salixAnnouncementStatusMessage": salixAnnouncementStatusMessage,
       "salixAnnouncementMappingTable": salixAnnouncementMappingTable,
       "salixAnnouncementMappingEntry": salixAnnouncementMappingEntry,
       "salixAnnouncementMappingStatus": salixAnnouncementMappingStatus,
       "salixAnnouncementMIBTraps": salixAnnouncementMIBTraps,
       "salixAnnouncementMIBTrapPrefix": salixAnnouncementMIBTrapPrefix,
       "salixAnnouncementInstallFailure": salixAnnouncementInstallFailure,
       "salixAnnouncementInstallSuccess": salixAnnouncementInstallSuccess,
       "salixAnnouncementMIBCompliance": salixAnnouncementMIBCompliance,
       "salixAnnouncementGroups": salixAnnouncementGroups,
       "salixAnnouncementGroup": salixAnnouncementGroup,
       "salixAnnouncementMappingGroup": salixAnnouncementMappingGroup,
       "salixAnnouncementCompliances": salixAnnouncementCompliances,
       "salixAnnouncementCompliance": salixAnnouncementCompliance}
)
