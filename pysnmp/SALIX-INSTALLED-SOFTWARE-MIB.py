# SNMP MIB module (SALIX-INSTALLED-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-INSTALLED-SOFTWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:28 2024
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

(hrSWInstalledEntry,
 hrSWInstalledIndex,
 hrSWRunEntry) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrSWInstalledEntry",
    "hrSWInstalledIndex",
    "hrSWRunEntry")

(salixGeneric,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "salixGeneric")

(SalixPlugInUnitType,) = mibBuilder.importSymbols(
    "SALIX-PRODUCT-PLUGIN-MIB",
    "SalixPlugInUnitType")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

salixInstalledSWMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixInstalledSWMIBObjects_ObjectIdentity = ObjectIdentity
salixInstalledSWMIBObjects = _SalixInstalledSWMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1)
)
_SalixSysHrSWInstalledTable_Object = MibTable
salixSysHrSWInstalledTable = _SalixSysHrSWInstalledTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    salixSysHrSWInstalledTable.setStatus("current")
_SalixSysHrSWInstalledEntry_Object = MibTableRow
salixSysHrSWInstalledEntry = _SalixSysHrSWInstalledEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    salixSysHrSWInstalledEntry.setStatus("current")


class _SalixSysHrSWInstalledFileVersion_Type(OctetString):
    """Custom type salixSysHrSWInstalledFileVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SalixSysHrSWInstalledFileVersion_Type.__name__ = "OctetString"
_SalixSysHrSWInstalledFileVersion_Object = MibTableColumn
salixSysHrSWInstalledFileVersion = _SalixSysHrSWInstalledFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 1),
    _SalixSysHrSWInstalledFileVersion_Type()
)
salixSysHrSWInstalledFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWInstalledFileVersion.setStatus("current")
_SalixSysHrSWInstalledFileControl_Type = DateAndTime
_SalixSysHrSWInstalledFileControl_Object = MibTableColumn
salixSysHrSWInstalledFileControl = _SalixSysHrSWInstalledFileControl_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 2),
    _SalixSysHrSWInstalledFileControl_Type()
)
salixSysHrSWInstalledFileControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWInstalledFileControl.setStatus("current")
_SalixSysHrSWInstalledFileCreation_Type = DateAndTime
_SalixSysHrSWInstalledFileCreation_Object = MibTableColumn
salixSysHrSWInstalledFileCreation = _SalixSysHrSWInstalledFileCreation_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 3),
    _SalixSysHrSWInstalledFileCreation_Type()
)
salixSysHrSWInstalledFileCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWInstalledFileCreation.setStatus("current")
_SalixSysHrSWInstalledFilePiuType_Type = SalixPlugInUnitType
_SalixSysHrSWInstalledFilePiuType_Object = MibTableColumn
salixSysHrSWInstalledFilePiuType = _SalixSysHrSWInstalledFilePiuType_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 4),
    _SalixSysHrSWInstalledFilePiuType_Type()
)
salixSysHrSWInstalledFilePiuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWInstalledFilePiuType.setStatus("current")


class _SalixSysHrSWInstalledFileBuilderName_Type(OctetString):
    """Custom type salixSysHrSWInstalledFileBuilderName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SalixSysHrSWInstalledFileBuilderName_Type.__name__ = "OctetString"
_SalixSysHrSWInstalledFileBuilderName_Object = MibTableColumn
salixSysHrSWInstalledFileBuilderName = _SalixSysHrSWInstalledFileBuilderName_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 5),
    _SalixSysHrSWInstalledFileBuilderName_Type()
)
salixSysHrSWInstalledFileBuilderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWInstalledFileBuilderName.setStatus("current")


class _SalixSysHrSWInstalledFileReleaseLabel_Type(OctetString):
    """Custom type salixSysHrSWInstalledFileReleaseLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SalixSysHrSWInstalledFileReleaseLabel_Type.__name__ = "OctetString"
_SalixSysHrSWInstalledFileReleaseLabel_Object = MibTableColumn
salixSysHrSWInstalledFileReleaseLabel = _SalixSysHrSWInstalledFileReleaseLabel_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 6),
    _SalixSysHrSWInstalledFileReleaseLabel_Type()
)
salixSysHrSWInstalledFileReleaseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWInstalledFileReleaseLabel.setStatus("current")
_SalixSysSwDownloadTable_Object = MibTable
salixSysSwDownloadTable = _SalixSysSwDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    salixSysSwDownloadTable.setStatus("current")
_SalixSysSwDownloadEntry_Object = MibTableRow
salixSysSwDownloadEntry = _SalixSysSwDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1)
)
salixSysSwDownloadEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrSWInstalledIndex"),
)
if mibBuilder.loadTexts:
    salixSysSwDownloadEntry.setStatus("current")
_SalixSysSwDownloadIpAddress_Type = IpAddress
_SalixSysSwDownloadIpAddress_Object = MibTableColumn
salixSysSwDownloadIpAddress = _SalixSysSwDownloadIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 1),
    _SalixSysSwDownloadIpAddress_Type()
)
salixSysSwDownloadIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSwDownloadIpAddress.setStatus("current")


class _SalixSysSwDownloadFilename_Type(DisplayString):
    """Custom type salixSysSwDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SalixSysSwDownloadFilename_Type.__name__ = "DisplayString"
_SalixSysSwDownloadFilename_Object = MibTableColumn
salixSysSwDownloadFilename = _SalixSysSwDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 2),
    _SalixSysSwDownloadFilename_Type()
)
salixSysSwDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSwDownloadFilename.setStatus("current")


class _SalixSysSwDownloadUsername_Type(DisplayString):
    """Custom type salixSysSwDownloadUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SalixSysSwDownloadUsername_Type.__name__ = "DisplayString"
_SalixSysSwDownloadUsername_Object = MibTableColumn
salixSysSwDownloadUsername = _SalixSysSwDownloadUsername_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 3),
    _SalixSysSwDownloadUsername_Type()
)
salixSysSwDownloadUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSwDownloadUsername.setStatus("current")


class _SalixSysSwDownloadPassword_Type(DisplayString):
    """Custom type salixSysSwDownloadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SalixSysSwDownloadPassword_Type.__name__ = "DisplayString"
_SalixSysSwDownloadPassword_Object = MibTableColumn
salixSysSwDownloadPassword = _SalixSysSwDownloadPassword_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 4),
    _SalixSysSwDownloadPassword_Type()
)
salixSysSwDownloadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSwDownloadPassword.setStatus("current")


class _SalixSysSwDownloadRequest_Type(Integer32):
    """Custom type salixSysSwDownloadRequest based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("start", 1))
    )


_SalixSysSwDownloadRequest_Type.__name__ = "Integer32"
_SalixSysSwDownloadRequest_Object = MibTableColumn
salixSysSwDownloadRequest = _SalixSysSwDownloadRequest_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 5),
    _SalixSysSwDownloadRequest_Type()
)
salixSysSwDownloadRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSwDownloadRequest.setStatus("current")


class _SalixSysSwDownloadState_Type(Integer32):
    """Custom type salixSysSwDownloadState based on Integer32"""
    defaultValue = 1

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
        *(("aborted", 4),
          ("failed", 5),
          ("inProgress", 2),
          ("locked", 6),
          ("none", 1),
          ("success", 3))
    )


_SalixSysSwDownloadState_Type.__name__ = "Integer32"
_SalixSysSwDownloadState_Object = MibTableColumn
salixSysSwDownloadState = _SalixSysSwDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 6),
    _SalixSysSwDownloadState_Type()
)
salixSysSwDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSwDownloadState.setStatus("current")


class _SalixSysSwDownloadStatusMessage_Type(OctetString):
    """Custom type salixSysSwDownloadStatusMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_SalixSysSwDownloadStatusMessage_Type.__name__ = "OctetString"
_SalixSysSwDownloadStatusMessage_Object = MibTableColumn
salixSysSwDownloadStatusMessage = _SalixSysSwDownloadStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 7),
    _SalixSysSwDownloadStatusMessage_Type()
)
salixSysSwDownloadStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSwDownloadStatusMessage.setStatus("current")
_SalixSysHrSWRunTable_Object = MibTable
salixSysHrSWRunTable = _SalixSysHrSWRunTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    salixSysHrSWRunTable.setStatus("current")
_SalixSysHrSWRunEntry_Object = MibTableRow
salixSysHrSWRunEntry = _SalixSysHrSWRunEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    salixSysHrSWRunEntry.setStatus("current")


class _SalixSysHrSWRunFileVersion_Type(OctetString):
    """Custom type salixSysHrSWRunFileVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SalixSysHrSWRunFileVersion_Type.__name__ = "OctetString"
_SalixSysHrSWRunFileVersion_Object = MibTableColumn
salixSysHrSWRunFileVersion = _SalixSysHrSWRunFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 1),
    _SalixSysHrSWRunFileVersion_Type()
)
salixSysHrSWRunFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWRunFileVersion.setStatus("current")
_SalixSysHrSWRunFileControl_Type = DateAndTime
_SalixSysHrSWRunFileControl_Object = MibTableColumn
salixSysHrSWRunFileControl = _SalixSysHrSWRunFileControl_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 2),
    _SalixSysHrSWRunFileControl_Type()
)
salixSysHrSWRunFileControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWRunFileControl.setStatus("current")
_SalixSysHrSWRunFileCreation_Type = DateAndTime
_SalixSysHrSWRunFileCreation_Object = MibTableColumn
salixSysHrSWRunFileCreation = _SalixSysHrSWRunFileCreation_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 3),
    _SalixSysHrSWRunFileCreation_Type()
)
salixSysHrSWRunFileCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWRunFileCreation.setStatus("current")


class _SalixSysHrSWRunFileBuilderName_Type(OctetString):
    """Custom type salixSysHrSWRunFileBuilderName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SalixSysHrSWRunFileBuilderName_Type.__name__ = "OctetString"
_SalixSysHrSWRunFileBuilderName_Object = MibTableColumn
salixSysHrSWRunFileBuilderName = _SalixSysHrSWRunFileBuilderName_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 4),
    _SalixSysHrSWRunFileBuilderName_Type()
)
salixSysHrSWRunFileBuilderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWRunFileBuilderName.setStatus("current")


class _SalixSysHrSWRunFileReleaseLabel_Type(OctetString):
    """Custom type salixSysHrSWRunFileReleaseLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SalixSysHrSWRunFileReleaseLabel_Type.__name__ = "OctetString"
_SalixSysHrSWRunFileReleaseLabel_Object = MibTableColumn
salixSysHrSWRunFileReleaseLabel = _SalixSysHrSWRunFileReleaseLabel_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 5),
    _SalixSysHrSWRunFileReleaseLabel_Type()
)
salixSysHrSWRunFileReleaseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHrSWRunFileReleaseLabel.setStatus("current")
_SalixInstalledSWMIBTraps_ObjectIdentity = ObjectIdentity
salixInstalledSWMIBTraps = _SalixInstalledSWMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 2)
)
_SalixInstalledSWMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixInstalledSWMIBTrapPrefix = _SalixInstalledSWMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 2, 0)
)
_SalixInstalledSWMIBCompliance_ObjectIdentity = ObjectIdentity
salixInstalledSWMIBCompliance = _SalixInstalledSWMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 3)
)
_SalixInstalledSWGroups_ObjectIdentity = ObjectIdentity
salixInstalledSWGroups = _SalixInstalledSWGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 1)
)
_SalixInstalledSWCompliances_ObjectIdentity = ObjectIdentity
salixInstalledSWCompliances = _SalixInstalledSWCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 2)
)
hrSWInstalledEntry.registerAugmentions(
    ("SALIX-INSTALLED-SOFTWARE-MIB",
     "salixSysHrSWInstalledEntry")
)
salixSysHrSWInstalledEntry.setIndexNames(*hrSWInstalledEntry.getIndexNames())
hrSWRunEntry.registerAugmentions(
    ("SALIX-INSTALLED-SOFTWARE-MIB",
     "salixSysHrSWRunEntry")
)
salixSysHrSWRunEntry.setIndexNames(*hrSWRunEntry.getIndexNames())

# Managed Objects groups

salixInstalledSWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 1, 1)
)
salixInstalledSWGroup.setObjects(
      *(("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadIpAddress"),
        ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadFilename"),
        ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadUsername"),
        ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadPassword"),
        ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadRequest"),
        ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadState"),
        ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadStatusMessage"))
)
if mibBuilder.loadTexts:
    salixInstalledSWGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

salixInstalledSWCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixInstalledSWCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-INSTALLED-SOFTWARE-MIB",
    **{"salixInstalledSWMIB": salixInstalledSWMIB,
       "salixInstalledSWMIBObjects": salixInstalledSWMIBObjects,
       "salixSysHrSWInstalledTable": salixSysHrSWInstalledTable,
       "salixSysHrSWInstalledEntry": salixSysHrSWInstalledEntry,
       "salixSysHrSWInstalledFileVersion": salixSysHrSWInstalledFileVersion,
       "salixSysHrSWInstalledFileControl": salixSysHrSWInstalledFileControl,
       "salixSysHrSWInstalledFileCreation": salixSysHrSWInstalledFileCreation,
       "salixSysHrSWInstalledFilePiuType": salixSysHrSWInstalledFilePiuType,
       "salixSysHrSWInstalledFileBuilderName": salixSysHrSWInstalledFileBuilderName,
       "salixSysHrSWInstalledFileReleaseLabel": salixSysHrSWInstalledFileReleaseLabel,
       "salixSysSwDownloadTable": salixSysSwDownloadTable,
       "salixSysSwDownloadEntry": salixSysSwDownloadEntry,
       "salixSysSwDownloadIpAddress": salixSysSwDownloadIpAddress,
       "salixSysSwDownloadFilename": salixSysSwDownloadFilename,
       "salixSysSwDownloadUsername": salixSysSwDownloadUsername,
       "salixSysSwDownloadPassword": salixSysSwDownloadPassword,
       "salixSysSwDownloadRequest": salixSysSwDownloadRequest,
       "salixSysSwDownloadState": salixSysSwDownloadState,
       "salixSysSwDownloadStatusMessage": salixSysSwDownloadStatusMessage,
       "salixSysHrSWRunTable": salixSysHrSWRunTable,
       "salixSysHrSWRunEntry": salixSysHrSWRunEntry,
       "salixSysHrSWRunFileVersion": salixSysHrSWRunFileVersion,
       "salixSysHrSWRunFileControl": salixSysHrSWRunFileControl,
       "salixSysHrSWRunFileCreation": salixSysHrSWRunFileCreation,
       "salixSysHrSWRunFileBuilderName": salixSysHrSWRunFileBuilderName,
       "salixSysHrSWRunFileReleaseLabel": salixSysHrSWRunFileReleaseLabel,
       "salixInstalledSWMIBTraps": salixInstalledSWMIBTraps,
       "salixInstalledSWMIBTrapPrefix": salixInstalledSWMIBTrapPrefix,
       "salixInstalledSWMIBCompliance": salixInstalledSWMIBCompliance,
       "salixInstalledSWGroups": salixInstalledSWGroups,
       "salixInstalledSWGroup": salixInstalledSWGroup,
       "salixInstalledSWCompliances": salixInstalledSWCompliances,
       "salixInstalledSWCompliance": salixInstalledSWCompliance}
)
