# SNMP MIB module (ENTERASYS-LICENSE-KEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-LICENSE-KEY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:02 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

etsysLicenseKeyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54)
)
etsysLicenseKeyMIB.setRevisions(
        ("2009-09-02 18:59",
         "2004-11-03 19:52",
         "2004-08-30 14:52",
         "2004-08-17 16:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LicenseKeyStatus(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("expired", 4),
          ("invalid", 3),
          ("other", 1),
          ("restricted", 5),
          ("uninitialized", 6),
          ("validNotActive", 7))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysLicenseKeyObjects_ObjectIdentity = ObjectIdentity
etsysLicenseKeyObjects = _EtsysLicenseKeyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1)
)
_EtsysLicenseKeyConfiguration_ObjectIdentity = ObjectIdentity
etsysLicenseKeyConfiguration = _EtsysLicenseKeyConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1)
)
_EtsysLicenseKeyTable_Object = MibTable
etsysLicenseKeyTable = _EtsysLicenseKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysLicenseKeyTable.setStatus("obsolete")
_EtsysLicenseKeyEntry_Object = MibTableRow
etsysLicenseKeyEntry = _EtsysLicenseKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1)
)
etsysLicenseKeyEntry.setIndexNames(
    (0, "ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyIndex"),
)
if mibBuilder.loadTexts:
    etsysLicenseKeyEntry.setStatus("obsolete")
_EtsysLicenseKeyIndex_Type = Unsigned32
_EtsysLicenseKeyIndex_Object = MibTableColumn
etsysLicenseKeyIndex = _EtsysLicenseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 1),
    _EtsysLicenseKeyIndex_Type()
)
etsysLicenseKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLicenseKeyIndex.setStatus("obsolete")
_EtsysLicenseKeyIdentifier_Type = ObjectIdentifier
_EtsysLicenseKeyIdentifier_Object = MibTableColumn
etsysLicenseKeyIdentifier = _EtsysLicenseKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 2),
    _EtsysLicenseKeyIdentifier_Type()
)
etsysLicenseKeyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyIdentifier.setStatus("obsolete")
_EtsysLicenseKeyDescription_Type = SnmpAdminString
_EtsysLicenseKeyDescription_Object = MibTableColumn
etsysLicenseKeyDescription = _EtsysLicenseKeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 3),
    _EtsysLicenseKeyDescription_Type()
)
etsysLicenseKeyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyDescription.setStatus("obsolete")
_EtsysLicenseKeyString_Type = SnmpAdminString
_EtsysLicenseKeyString_Object = MibTableColumn
etsysLicenseKeyString = _EtsysLicenseKeyString_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 4),
    _EtsysLicenseKeyString_Type()
)
etsysLicenseKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLicenseKeyString.setStatus("obsolete")
_EtsysLicenseKeyStatus_Type = LicenseKeyStatus
_EtsysLicenseKeyStatus_Object = MibTableColumn
etsysLicenseKeyStatus = _EtsysLicenseKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 5),
    _EtsysLicenseKeyStatus_Type()
)
etsysLicenseKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyStatus.setStatus("obsolete")
_EtsysLicenseKeyStatusText_Type = SnmpAdminString
_EtsysLicenseKeyStatusText_Object = MibTableColumn
etsysLicenseKeyStatusText = _EtsysLicenseKeyStatusText_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 6),
    _EtsysLicenseKeyStatusText_Type()
)
etsysLicenseKeyStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyStatusText.setStatus("obsolete")


class _EtsysLicenseKeyLastModified_Type(DateAndTime):
    """Custom type etsysLicenseKeyLastModified based on DateAndTime"""
    defaultHexValue = "00000000"


_EtsysLicenseKeyLastModified_Object = MibTableColumn
etsysLicenseKeyLastModified = _EtsysLicenseKeyLastModified_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 7),
    _EtsysLicenseKeyLastModified_Type()
)
etsysLicenseKeyLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyLastModified.setStatus("obsolete")


class _EtsysLicenseKeyExpiration_Type(DateAndTime):
    """Custom type etsysLicenseKeyExpiration based on DateAndTime"""
    defaultHexValue = "00000000"


_EtsysLicenseKeyExpiration_Object = MibTableColumn
etsysLicenseKeyExpiration = _EtsysLicenseKeyExpiration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 1, 1, 8),
    _EtsysLicenseKeyExpiration_Type()
)
etsysLicenseKeyExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyExpiration.setStatus("obsolete")
_EtsysLicenseKeyPhysicalTable_Object = MibTable
etsysLicenseKeyPhysicalTable = _EtsysLicenseKeyPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalTable.setStatus("current")
_EtsysLicenseKeyPhysicalEntry_Object = MibTableRow
etsysLicenseKeyPhysicalEntry = _EtsysLicenseKeyPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1)
)
etsysLicenseKeyPhysicalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalIndex"),
)
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalEntry.setStatus("current")
_EtsysLicenseKeyPhysicalIndex_Type = Unsigned32
_EtsysLicenseKeyPhysicalIndex_Object = MibTableColumn
etsysLicenseKeyPhysicalIndex = _EtsysLicenseKeyPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 1),
    _EtsysLicenseKeyPhysicalIndex_Type()
)
etsysLicenseKeyPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalIndex.setStatus("current")
_EtsysLicenseKeyPhysicalIdentifier_Type = ObjectIdentifier
_EtsysLicenseKeyPhysicalIdentifier_Object = MibTableColumn
etsysLicenseKeyPhysicalIdentifier = _EtsysLicenseKeyPhysicalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 2),
    _EtsysLicenseKeyPhysicalIdentifier_Type()
)
etsysLicenseKeyPhysicalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalIdentifier.setStatus("current")
_EtsysLicenseKeyPhysicalDescription_Type = SnmpAdminString
_EtsysLicenseKeyPhysicalDescription_Object = MibTableColumn
etsysLicenseKeyPhysicalDescription = _EtsysLicenseKeyPhysicalDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 3),
    _EtsysLicenseKeyPhysicalDescription_Type()
)
etsysLicenseKeyPhysicalDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalDescription.setStatus("current")


class _EtsysLicenseKeyPhysicalString_Type(OctetString):
    """Custom type etsysLicenseKeyPhysicalString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EtsysLicenseKeyPhysicalString_Type.__name__ = "OctetString"
_EtsysLicenseKeyPhysicalString_Object = MibTableColumn
etsysLicenseKeyPhysicalString = _EtsysLicenseKeyPhysicalString_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 4),
    _EtsysLicenseKeyPhysicalString_Type()
)
etsysLicenseKeyPhysicalString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalString.setStatus("current")
_EtsysLicenseKeyPhysicalStatus_Type = LicenseKeyStatus
_EtsysLicenseKeyPhysicalStatus_Object = MibTableColumn
etsysLicenseKeyPhysicalStatus = _EtsysLicenseKeyPhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 5),
    _EtsysLicenseKeyPhysicalStatus_Type()
)
etsysLicenseKeyPhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalStatus.setStatus("current")
_EtsysLicenseKeyPhysicalStatusText_Type = SnmpAdminString
_EtsysLicenseKeyPhysicalStatusText_Object = MibTableColumn
etsysLicenseKeyPhysicalStatusText = _EtsysLicenseKeyPhysicalStatusText_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 6),
    _EtsysLicenseKeyPhysicalStatusText_Type()
)
etsysLicenseKeyPhysicalStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalStatusText.setStatus("current")


class _EtsysLicenseKeyPhysicalLastModified_Type(DateAndTime):
    """Custom type etsysLicenseKeyPhysicalLastModified based on DateAndTime"""
    defaultHexValue = "00000000"


_EtsysLicenseKeyPhysicalLastModified_Object = MibTableColumn
etsysLicenseKeyPhysicalLastModified = _EtsysLicenseKeyPhysicalLastModified_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 7),
    _EtsysLicenseKeyPhysicalLastModified_Type()
)
etsysLicenseKeyPhysicalLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalLastModified.setStatus("current")


class _EtsysLicenseKeyPhysicalExpiration_Type(DateAndTime):
    """Custom type etsysLicenseKeyPhysicalExpiration based on DateAndTime"""
    defaultHexValue = "00000000"


_EtsysLicenseKeyPhysicalExpiration_Object = MibTableColumn
etsysLicenseKeyPhysicalExpiration = _EtsysLicenseKeyPhysicalExpiration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 1, 1, 2, 1, 8),
    _EtsysLicenseKeyPhysicalExpiration_Type()
)
etsysLicenseKeyPhysicalExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalExpiration.setStatus("current")
_EtsysLicenseKeyConformance_ObjectIdentity = ObjectIdentity
etsysLicenseKeyConformance = _EtsysLicenseKeyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 2)
)
_EtsysLicenseKeyGroups_ObjectIdentity = ObjectIdentity
etsysLicenseKeyGroups = _EtsysLicenseKeyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 2, 1)
)
_EtsysLicenseKeyCompliances_ObjectIdentity = ObjectIdentity
etsysLicenseKeyCompliances = _EtsysLicenseKeyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 2, 2)
)

# Managed Objects groups

etsysLicenseKeyConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 2, 1, 1)
)
etsysLicenseKeyConfigurationGroup.setObjects(
      *(("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyIdentifier"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyDescription"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyString"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyStatus"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyStatusText"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyLastModified"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyExpiration"))
)
if mibBuilder.loadTexts:
    etsysLicenseKeyConfigurationGroup.setStatus("obsolete")

etsysLicenseKeyPhysicalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 2, 1, 2)
)
etsysLicenseKeyPhysicalConfigGroup.setObjects(
      *(("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalIdentifier"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalDescription"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalString"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalStatus"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalStatusText"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalLastModified"),
        ("ENTERASYS-LICENSE-KEY-MIB", "etsysLicenseKeyPhysicalExpiration"))
)
if mibBuilder.loadTexts:
    etsysLicenseKeyPhysicalConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysLicenseKeyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysLicenseKeyCompliance.setStatus(
        "obsolete"
    )

etsysLicenseKeyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 54, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysLicenseKeyCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-LICENSE-KEY-MIB",
    **{"LicenseKeyStatus": LicenseKeyStatus,
       "etsysLicenseKeyMIB": etsysLicenseKeyMIB,
       "etsysLicenseKeyObjects": etsysLicenseKeyObjects,
       "etsysLicenseKeyConfiguration": etsysLicenseKeyConfiguration,
       "etsysLicenseKeyTable": etsysLicenseKeyTable,
       "etsysLicenseKeyEntry": etsysLicenseKeyEntry,
       "etsysLicenseKeyIndex": etsysLicenseKeyIndex,
       "etsysLicenseKeyIdentifier": etsysLicenseKeyIdentifier,
       "etsysLicenseKeyDescription": etsysLicenseKeyDescription,
       "etsysLicenseKeyString": etsysLicenseKeyString,
       "etsysLicenseKeyStatus": etsysLicenseKeyStatus,
       "etsysLicenseKeyStatusText": etsysLicenseKeyStatusText,
       "etsysLicenseKeyLastModified": etsysLicenseKeyLastModified,
       "etsysLicenseKeyExpiration": etsysLicenseKeyExpiration,
       "etsysLicenseKeyPhysicalTable": etsysLicenseKeyPhysicalTable,
       "etsysLicenseKeyPhysicalEntry": etsysLicenseKeyPhysicalEntry,
       "etsysLicenseKeyPhysicalIndex": etsysLicenseKeyPhysicalIndex,
       "etsysLicenseKeyPhysicalIdentifier": etsysLicenseKeyPhysicalIdentifier,
       "etsysLicenseKeyPhysicalDescription": etsysLicenseKeyPhysicalDescription,
       "etsysLicenseKeyPhysicalString": etsysLicenseKeyPhysicalString,
       "etsysLicenseKeyPhysicalStatus": etsysLicenseKeyPhysicalStatus,
       "etsysLicenseKeyPhysicalStatusText": etsysLicenseKeyPhysicalStatusText,
       "etsysLicenseKeyPhysicalLastModified": etsysLicenseKeyPhysicalLastModified,
       "etsysLicenseKeyPhysicalExpiration": etsysLicenseKeyPhysicalExpiration,
       "etsysLicenseKeyConformance": etsysLicenseKeyConformance,
       "etsysLicenseKeyGroups": etsysLicenseKeyGroups,
       "etsysLicenseKeyConfigurationGroup": etsysLicenseKeyConfigurationGroup,
       "etsysLicenseKeyPhysicalConfigGroup": etsysLicenseKeyPhysicalConfigGroup,
       "etsysLicenseKeyCompliances": etsysLicenseKeyCompliances,
       "etsysLicenseKeyCompliance": etsysLicenseKeyCompliance,
       "etsysLicenseKeyCompliance2": etsysLicenseKeyCompliance2}
)
