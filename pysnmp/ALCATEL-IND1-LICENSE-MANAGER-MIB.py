# SNMP MIB module (ALCATEL-IND1-LICENSE-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-LICENSE-MANAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:26 2024
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

(softentIND1LicenseManager,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1LicenseManager")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aluLicenseManagerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1)
)
aluLicenseManagerMIB.setRevisions(
        ("2009-03-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluLicenseManagerMIBNotifications_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBNotifications = _AluLicenseManagerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 0)
)
_AluLicenseManagerMIBObjects_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBObjects = _AluLicenseManagerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBObjects.setStatus("current")
_AluLicenseManagerConfig_ObjectIdentity = ObjectIdentity
aluLicenseManagerConfig = _AluLicenseManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 1)
)


class _AluLicenseManagerApplyLicense_Type(Integer32):
    """Custom type aluLicenseManagerApplyLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("default", 0))
    )


_AluLicenseManagerApplyLicense_Type.__name__ = "Integer32"
_AluLicenseManagerApplyLicense_Object = MibScalar
aluLicenseManagerApplyLicense = _AluLicenseManagerApplyLicense_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 1, 1),
    _AluLicenseManagerApplyLicense_Type()
)
aluLicenseManagerApplyLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicenseManagerApplyLicense.setStatus("current")
_AluLicenseManagerInfoTable_Object = MibTable
aluLicenseManagerInfoTable = _AluLicenseManagerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aluLicenseManagerInfoTable.setStatus("current")
_AluLicenseManagerInfoEntry_Object = MibTableRow
aluLicenseManagerInfoEntry = _AluLicenseManagerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 2, 1)
)
aluLicenseManagerInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseId"),
)
if mibBuilder.loadTexts:
    aluLicenseManagerInfoEntry.setStatus("current")


class _AluLicenseId_Type(Unsigned32):
    """Custom type aluLicenseId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AluLicenseId_Type.__name__ = "Unsigned32"
_AluLicenseId_Object = MibTableColumn
aluLicenseId = _AluLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 2, 1, 1),
    _AluLicenseId_Type()
)
aluLicenseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicenseId.setStatus("current")


class _AluLicensedApplication_Type(DisplayString):
    """Custom type aluLicensedApplication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AluLicensedApplication_Type.__name__ = "DisplayString"
_AluLicensedApplication_Object = MibTableColumn
aluLicensedApplication = _AluLicensedApplication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 2, 1, 2),
    _AluLicensedApplication_Type()
)
aluLicensedApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicensedApplication.setStatus("current")


class _AluLicenseType_Type(Integer32):
    """Custom type aluLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("demo", 1),
          ("permanent", 2))
    )


_AluLicenseType_Type.__name__ = "Integer32"
_AluLicenseType_Object = MibTableColumn
aluLicenseType = _AluLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 2, 1, 3),
    _AluLicenseType_Type()
)
aluLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseType.setStatus("current")


class _AluLicenseTimeRemaining_Type(Integer32):
    """Custom type aluLicenseTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AluLicenseTimeRemaining_Type.__name__ = "Integer32"
_AluLicenseTimeRemaining_Object = MibTableColumn
aluLicenseTimeRemaining = _AluLicenseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 2, 1, 4),
    _AluLicenseTimeRemaining_Type()
)
aluLicenseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseTimeRemaining.setStatus("current")
_AluLicenseManagerFileInfoTable_Object = MibTable
aluLicenseManagerFileInfoTable = _AluLicenseManagerFileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 3)
)
if mibBuilder.loadTexts:
    aluLicenseManagerFileInfoTable.setStatus("current")
_AluLicenseManagerFileInfoEntry_Object = MibTableRow
aluLicenseManagerFileInfoEntry = _AluLicenseManagerFileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 3, 1)
)
aluLicenseManagerFileInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseFileIndex"),
)
if mibBuilder.loadTexts:
    aluLicenseManagerFileInfoEntry.setStatus("current")
_AluLicenseFileIndex_Type = Counter32
_AluLicenseFileIndex_Object = MibTableColumn
aluLicenseFileIndex = _AluLicenseFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 3, 1, 1),
    _AluLicenseFileIndex_Type()
)
aluLicenseFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicenseFileIndex.setStatus("current")
_AluSwitchMacAddress_Type = MacAddress
_AluSwitchMacAddress_Object = MibTableColumn
aluSwitchMacAddress = _AluSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 3, 1, 2),
    _AluSwitchMacAddress_Type()
)
aluSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSwitchMacAddress.setStatus("current")


class _AluLicensedFileApplication_Type(DisplayString):
    """Custom type aluLicensedFileApplication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AluLicensedFileApplication_Type.__name__ = "DisplayString"
_AluLicensedFileApplication_Object = MibTableColumn
aluLicensedFileApplication = _AluLicensedFileApplication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 1, 3, 1, 3),
    _AluLicensedFileApplication_Type()
)
aluLicensedFileApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicensedFileApplication.setStatus("current")
_AluLicenseManagerMIBConformance_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBConformance = _AluLicenseManagerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBConformance.setStatus("current")
_AluLicenseManagerMIBGroups_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBGroups = _AluLicenseManagerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBGroups.setStatus("current")
_AluLicenseManagerMIBCompliances_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBCompliances = _AluLicenseManagerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBCompliances.setStatus("current")

# Managed Objects groups

aluLicenseManagerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2, 1, 1)
)
aluLicenseManagerConfigGroup.setObjects(
    ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerApplyLicense")
)
if mibBuilder.loadTexts:
    aluLicenseManagerConfigGroup.setStatus("current")

aluLicenseManagerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2, 1, 2)
)
aluLicenseManagerInfoGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedApplication"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseType"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseTimeRemaining"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerInfoGroup.setStatus("current")

aluLicenseManagerFileInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2, 1, 4)
)
aluLicenseManagerFileInfoGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluSwitchMacAddress"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedFileApplication"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerFileInfoGroup.setStatus("current")


# Notification objects

aluLicenseManagerLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 0, 0, 1)
)
aluLicenseManagerLicenseExpired.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedApplication"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseTimeRemaining"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerLicenseExpired.setStatus(
        "current"
    )


# Notifications groups

aluLicenseManagerNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2, 1, 3)
)
aluLicenseManagerNotificationsGroup.setObjects(
    ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerLicenseExpired")
)
if mibBuilder.loadTexts:
    aluLicenseManagerNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluLicenseManagerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-LICENSE-MANAGER-MIB",
    **{"aluLicenseManagerMIB": aluLicenseManagerMIB,
       "aluLicenseManagerMIBNotifications": aluLicenseManagerMIBNotifications,
       "aluLicenseManagerLicenseExpired": aluLicenseManagerLicenseExpired,
       "aluLicenseManagerMIBObjects": aluLicenseManagerMIBObjects,
       "aluLicenseManagerConfig": aluLicenseManagerConfig,
       "aluLicenseManagerApplyLicense": aluLicenseManagerApplyLicense,
       "aluLicenseManagerInfoTable": aluLicenseManagerInfoTable,
       "aluLicenseManagerInfoEntry": aluLicenseManagerInfoEntry,
       "aluLicenseId": aluLicenseId,
       "aluLicensedApplication": aluLicensedApplication,
       "aluLicenseType": aluLicenseType,
       "aluLicenseTimeRemaining": aluLicenseTimeRemaining,
       "aluLicenseManagerFileInfoTable": aluLicenseManagerFileInfoTable,
       "aluLicenseManagerFileInfoEntry": aluLicenseManagerFileInfoEntry,
       "aluLicenseFileIndex": aluLicenseFileIndex,
       "aluSwitchMacAddress": aluSwitchMacAddress,
       "aluLicensedFileApplication": aluLicensedFileApplication,
       "aluLicenseManagerMIBConformance": aluLicenseManagerMIBConformance,
       "aluLicenseManagerMIBGroups": aluLicenseManagerMIBGroups,
       "aluLicenseManagerConfigGroup": aluLicenseManagerConfigGroup,
       "aluLicenseManagerInfoGroup": aluLicenseManagerInfoGroup,
       "aluLicenseManagerNotificationsGroup": aluLicenseManagerNotificationsGroup,
       "aluLicenseManagerFileInfoGroup": aluLicenseManagerFileInfoGroup,
       "aluLicenseManagerMIBCompliances": aluLicenseManagerMIBCompliances,
       "aluLicenseManagerMIBCompliance": aluLicenseManagerMIBCompliance}
)
