# SNMP MIB module (JUNIPER-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:27 2024
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

(jnxLicenseMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxLicenseMibRoot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1)
)
jnxLicenseMIB.setRevisions(
        ("2010-07-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLicenseNotifications_ObjectIdentity = ObjectIdentity
jnxLicenseNotifications = _JnxLicenseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0)
)
_JnxLicenseObjects_ObjectIdentity = ObjectIdentity
jnxLicenseObjects = _JnxLicenseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1)
)
_JnxLicenseInstallObjects_ObjectIdentity = ObjectIdentity
jnxLicenseInstallObjects = _JnxLicenseInstallObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1)
)
_JnxLicenseInstallTable_Object = MibTable
jnxLicenseInstallTable = _JnxLicenseInstallTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLicenseInstallTable.setStatus("current")
_JnxLicenseInstallEntry_Object = MibTableRow
jnxLicenseInstallEntry = _JnxLicenseInstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1)
)
jnxLicenseInstallEntry.setIndexNames(
    (1, "JUNIPER-LICENSE-MIB", "jnxLicenseId"),
)
if mibBuilder.loadTexts:
    jnxLicenseInstallEntry.setStatus("current")
_JnxLicenseId_Type = DisplayString
_JnxLicenseId_Object = MibTableColumn
jnxLicenseId = _JnxLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 1),
    _JnxLicenseId_Type()
)
jnxLicenseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLicenseId.setStatus("current")
_JnxLicenseVersion_Type = Integer32
_JnxLicenseVersion_Object = MibTableColumn
jnxLicenseVersion = _JnxLicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 2),
    _JnxLicenseVersion_Type()
)
jnxLicenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseVersion.setStatus("current")
_JnxLicenseDeviceId_Type = DisplayString
_JnxLicenseDeviceId_Object = MibTableColumn
jnxLicenseDeviceId = _JnxLicenseDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 3),
    _JnxLicenseDeviceId_Type()
)
jnxLicenseDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseDeviceId.setStatus("current")


class _JnxLicenseType_Type(Integer32):
    """Custom type jnxLicenseType based on Integer32"""
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
        *(("count-down", 1),
          ("date-based", 2),
          ("invalid", 0),
          ("permanent", 3))
    )


_JnxLicenseType_Type.__name__ = "Integer32"
_JnxLicenseType_Object = MibTableColumn
jnxLicenseType = _JnxLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 4),
    _JnxLicenseType_Type()
)
jnxLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseType.setStatus("current")
_JnxLicenseKeys_Type = OctetString
_JnxLicenseKeys_Object = MibTableColumn
jnxLicenseKeys = _JnxLicenseKeys_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 5),
    _JnxLicenseKeys_Type()
)
jnxLicenseKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseKeys.setStatus("current")
_JnxLicenseFeatureListTable_Object = MibTable
jnxLicenseFeatureListTable = _JnxLicenseFeatureListTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxLicenseFeatureListTable.setStatus("current")
_JnxLicenseFeatureListEntry_Object = MibTableRow
jnxLicenseFeatureListEntry = _JnxLicenseFeatureListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1)
)
jnxLicenseFeatureListEntry.setIndexNames(
    (0, "JUNIPER-LICENSE-MIB", "jnxLicenseFeatureId"),
)
if mibBuilder.loadTexts:
    jnxLicenseFeatureListEntry.setStatus("current")
_JnxLicenseFeatureId_Type = Integer32
_JnxLicenseFeatureId_Object = MibTableColumn
jnxLicenseFeatureId = _JnxLicenseFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 1),
    _JnxLicenseFeatureId_Type()
)
jnxLicenseFeatureId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLicenseFeatureId.setStatus("current")
_JnxLicenseFeatureName_Type = DisplayString
_JnxLicenseFeatureName_Object = MibTableColumn
jnxLicenseFeatureName = _JnxLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 2),
    _JnxLicenseFeatureName_Type()
)
jnxLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseFeatureName.setStatus("current")
_JnxLicenseFeatureDescr_Type = DisplayString
_JnxLicenseFeatureDescr_Object = MibTableColumn
jnxLicenseFeatureDescr = _JnxLicenseFeatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 3),
    _JnxLicenseFeatureDescr_Type()
)
jnxLicenseFeatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseFeatureDescr.setStatus("current")
_JnxLicenseFeatureLicenseId_Type = DisplayString
_JnxLicenseFeatureLicenseId_Object = MibTableColumn
jnxLicenseFeatureLicenseId = _JnxLicenseFeatureLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 4),
    _JnxLicenseFeatureLicenseId_Type()
)
jnxLicenseFeatureLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseFeatureLicenseId.setStatus("current")
_JnxLicenseFeatureLicenseUsed_Type = Integer32
_JnxLicenseFeatureLicenseUsed_Object = MibTableColumn
jnxLicenseFeatureLicenseUsed = _JnxLicenseFeatureLicenseUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 5),
    _JnxLicenseFeatureLicenseUsed_Type()
)
jnxLicenseFeatureLicenseUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseFeatureLicenseUsed.setStatus("current")
_JnxLicenseFeatureLicenseInstalled_Type = Integer32
_JnxLicenseFeatureLicenseInstalled_Object = MibTableColumn
jnxLicenseFeatureLicenseInstalled = _JnxLicenseFeatureLicenseInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 6),
    _JnxLicenseFeatureLicenseInstalled_Type()
)
jnxLicenseFeatureLicenseInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseFeatureLicenseInstalled.setStatus("current")
_JnxLicenseFeatureLicenseNeeded_Type = Integer32
_JnxLicenseFeatureLicenseNeeded_Object = MibTableColumn
jnxLicenseFeatureLicenseNeeded = _JnxLicenseFeatureLicenseNeeded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 7),
    _JnxLicenseFeatureLicenseNeeded_Type()
)
jnxLicenseFeatureLicenseNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseFeatureLicenseNeeded.setStatus("current")
_JnxLicenseSettings_ObjectIdentity = ObjectIdentity
jnxLicenseSettings = _JnxLicenseSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2)
)
_JnxLicenseRenewBeforExpiration_Type = Integer32
_JnxLicenseRenewBeforExpiration_Object = MibScalar
jnxLicenseRenewBeforExpiration = _JnxLicenseRenewBeforExpiration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 1),
    _JnxLicenseRenewBeforExpiration_Type()
)
jnxLicenseRenewBeforExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseRenewBeforExpiration.setStatus("current")
_JnxLicenseRenewInterval_Type = Integer32
_JnxLicenseRenewInterval_Object = MibScalar
jnxLicenseRenewInterval = _JnxLicenseRenewInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 2),
    _JnxLicenseRenewInterval_Type()
)
jnxLicenseRenewInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseRenewInterval.setStatus("current")
_JnxLicenseAutoUpdate_Type = DisplayString
_JnxLicenseAutoUpdate_Object = MibScalar
jnxLicenseAutoUpdate = _JnxLicenseAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 3),
    _JnxLicenseAutoUpdate_Type()
)
jnxLicenseAutoUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLicenseAutoUpdate.setStatus("current")

# Managed Objects groups


# Notification objects

jnxLicenseGraceExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 1)
)
jnxLicenseGraceExpired.setObjects(
    ("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName")
)
if mibBuilder.loadTexts:
    jnxLicenseGraceExpired.setStatus(
        "current"
    )

jnxLicenseGraceAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 2)
)
jnxLicenseGraceAboutToExpire.setObjects(
    ("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName")
)
if mibBuilder.loadTexts:
    jnxLicenseGraceAboutToExpire.setStatus(
        "current"
    )

jnxLicenseAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 3)
)
jnxLicenseAboutToExpire.setObjects(
    ("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName")
)
if mibBuilder.loadTexts:
    jnxLicenseAboutToExpire.setStatus(
        "current"
    )

jnxLicenseInfringeCumulative = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 4)
)
jnxLicenseInfringeCumulative.setObjects(
    ("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName")
)
if mibBuilder.loadTexts:
    jnxLicenseInfringeCumulative.setStatus(
        "current"
    )

jnxLicenseInfringeSingle = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 5)
)
jnxLicenseInfringeSingle.setObjects(
    ("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName")
)
if mibBuilder.loadTexts:
    jnxLicenseInfringeSingle.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LICENSE-MIB",
    **{"jnxLicenseMIB": jnxLicenseMIB,
       "jnxLicenseNotifications": jnxLicenseNotifications,
       "jnxLicenseGraceExpired": jnxLicenseGraceExpired,
       "jnxLicenseGraceAboutToExpire": jnxLicenseGraceAboutToExpire,
       "jnxLicenseAboutToExpire": jnxLicenseAboutToExpire,
       "jnxLicenseInfringeCumulative": jnxLicenseInfringeCumulative,
       "jnxLicenseInfringeSingle": jnxLicenseInfringeSingle,
       "jnxLicenseObjects": jnxLicenseObjects,
       "jnxLicenseInstallObjects": jnxLicenseInstallObjects,
       "jnxLicenseInstallTable": jnxLicenseInstallTable,
       "jnxLicenseInstallEntry": jnxLicenseInstallEntry,
       "jnxLicenseId": jnxLicenseId,
       "jnxLicenseVersion": jnxLicenseVersion,
       "jnxLicenseDeviceId": jnxLicenseDeviceId,
       "jnxLicenseType": jnxLicenseType,
       "jnxLicenseKeys": jnxLicenseKeys,
       "jnxLicenseFeatureListTable": jnxLicenseFeatureListTable,
       "jnxLicenseFeatureListEntry": jnxLicenseFeatureListEntry,
       "jnxLicenseFeatureId": jnxLicenseFeatureId,
       "jnxLicenseFeatureName": jnxLicenseFeatureName,
       "jnxLicenseFeatureDescr": jnxLicenseFeatureDescr,
       "jnxLicenseFeatureLicenseId": jnxLicenseFeatureLicenseId,
       "jnxLicenseFeatureLicenseUsed": jnxLicenseFeatureLicenseUsed,
       "jnxLicenseFeatureLicenseInstalled": jnxLicenseFeatureLicenseInstalled,
       "jnxLicenseFeatureLicenseNeeded": jnxLicenseFeatureLicenseNeeded,
       "jnxLicenseSettings": jnxLicenseSettings,
       "jnxLicenseRenewBeforExpiration": jnxLicenseRenewBeforExpiration,
       "jnxLicenseRenewInterval": jnxLicenseRenewInterval,
       "jnxLicenseAutoUpdate": jnxLicenseAutoUpdate}
)
