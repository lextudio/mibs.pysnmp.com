# SNMP MIB module (JUNIPER-JS-IDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-IDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:16 2024
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

(jnxJsIdpRoot,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsIdpRoot")

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

jnxJsIdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsIdpObjects_ObjectIdentity = ObjectIdentity
jnxJsIdpObjects = _JnxJsIdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1)
)
_JnxJsIdpDataPlaneMemoryUsage_Type = Unsigned32
_JnxJsIdpDataPlaneMemoryUsage_Object = MibScalar
jnxJsIdpDataPlaneMemoryUsage = _JnxJsIdpDataPlaneMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 1),
    _JnxJsIdpDataPlaneMemoryUsage_Type()
)
jnxJsIdpDataPlaneMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpDataPlaneMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxJsIdpDataPlaneMemoryUsage.setUnits("percent")
_JnxJsIdpSessionsUsage_Type = Unsigned32
_JnxJsIdpSessionsUsage_Object = MibScalar
jnxJsIdpSessionsUsage = _JnxJsIdpSessionsUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 2),
    _JnxJsIdpSessionsUsage_Type()
)
jnxJsIdpSessionsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpSessionsUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxJsIdpSessionsUsage.setUnits("percent")
_JnxJsIdpSessionsMaximum_Type = Unsigned32
_JnxJsIdpSessionsMaximum_Object = MibScalar
jnxJsIdpSessionsMaximum = _JnxJsIdpSessionsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 3),
    _JnxJsIdpSessionsMaximum_Type()
)
jnxJsIdpSessionsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpSessionsMaximum.setStatus("current")
_JnxJsIdpPoliciesSupported_Type = Gauge32
_JnxJsIdpPoliciesSupported_Object = MibScalar
jnxJsIdpPoliciesSupported = _JnxJsIdpPoliciesSupported_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 4),
    _JnxJsIdpPoliciesSupported_Type()
)
jnxJsIdpPoliciesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpPoliciesSupported.setStatus("current")
_JnxJsIdpPoliciesLoaded_Type = Gauge32
_JnxJsIdpPoliciesLoaded_Object = MibScalar
jnxJsIdpPoliciesLoaded = _JnxJsIdpPoliciesLoaded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 5),
    _JnxJsIdpPoliciesLoaded_Type()
)
jnxJsIdpPoliciesLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpPoliciesLoaded.setStatus("current")


class _JnxJsIdpActivePolicyName_Type(DisplayString):
    """Custom type jnxJsIdpActivePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsIdpActivePolicyName_Type.__name__ = "DisplayString"
_JnxJsIdpActivePolicyName_Object = MibScalar
jnxJsIdpActivePolicyName = _JnxJsIdpActivePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 6),
    _JnxJsIdpActivePolicyName_Type()
)
jnxJsIdpActivePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpActivePolicyName.setStatus("current")
_JnxJsIdpAttackTable_Object = MibTable
jnxJsIdpAttackTable = _JnxJsIdpAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxJsIdpAttackTable.setStatus("current")
_JnxJsIdpAttackEntry_Object = MibTableRow
jnxJsIdpAttackEntry = _JnxJsIdpAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 7, 1)
)
jnxJsIdpAttackEntry.setIndexNames(
    (0, "JUNIPER-JS-IDP-MIB", "jnxJsIdpAttackIndex"),
)
if mibBuilder.loadTexts:
    jnxJsIdpAttackEntry.setStatus("current")
_JnxJsIdpAttackIndex_Type = Unsigned32
_JnxJsIdpAttackIndex_Object = MibTableColumn
jnxJsIdpAttackIndex = _JnxJsIdpAttackIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 7, 1, 1),
    _JnxJsIdpAttackIndex_Type()
)
jnxJsIdpAttackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsIdpAttackIndex.setStatus("current")


class _JnxJsIdpAttackName_Type(DisplayString):
    """Custom type jnxJsIdpAttackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsIdpAttackName_Type.__name__ = "DisplayString"
_JnxJsIdpAttackName_Object = MibTableColumn
jnxJsIdpAttackName = _JnxJsIdpAttackName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 7, 1, 2),
    _JnxJsIdpAttackName_Type()
)
jnxJsIdpAttackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpAttackName.setStatus("current")
_JnxJsIdpAttackHits_Type = Counter32
_JnxJsIdpAttackHits_Object = MibTableColumn
jnxJsIdpAttackHits = _JnxJsIdpAttackHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 7, 1, 3),
    _JnxJsIdpAttackHits_Type()
)
jnxJsIdpAttackHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIdpAttackHits.setStatus("current")


class _JnxJsIdpRunningDetectorVersion_Type(OctetString):
    """Custom type jnxJsIdpRunningDetectorVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsIdpRunningDetectorVersion_Type.__name__ = "OctetString"
_JnxJsIdpRunningDetectorVersion_Object = MibScalar
jnxJsIdpRunningDetectorVersion = _JnxJsIdpRunningDetectorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 8),
    _JnxJsIdpRunningDetectorVersion_Type()
)
jnxJsIdpRunningDetectorVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsIdpRunningDetectorVersion.setStatus("current")


class _JnxJsIdpSecurityPackageVersion_Type(OctetString):
    """Custom type jnxJsIdpSecurityPackageVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsIdpSecurityPackageVersion_Type.__name__ = "OctetString"
_JnxJsIdpSecurityPackageVersion_Object = MibScalar
jnxJsIdpSecurityPackageVersion = _JnxJsIdpSecurityPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 9),
    _JnxJsIdpSecurityPackageVersion_Type()
)
jnxJsIdpSecurityPackageVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsIdpSecurityPackageVersion.setStatus("current")
_JnxJsIdpLastSignatureUpdateTime_Type = TimeTicks
_JnxJsIdpLastSignatureUpdateTime_Object = MibScalar
jnxJsIdpLastSignatureUpdateTime = _JnxJsIdpLastSignatureUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 10),
    _JnxJsIdpLastSignatureUpdateTime_Type()
)
jnxJsIdpLastSignatureUpdateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsIdpLastSignatureUpdateTime.setStatus("current")


class _JnxJsIdpSignatureUpdateStatus_Type(DisplayString):
    """Custom type jnxJsIdpSignatureUpdateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsIdpSignatureUpdateStatus_Type.__name__ = "DisplayString"
_JnxJsIdpSignatureUpdateStatus_Object = MibScalar
jnxJsIdpSignatureUpdateStatus = _JnxJsIdpSignatureUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 1, 11),
    _JnxJsIdpSignatureUpdateStatus_Type()
)
jnxJsIdpSignatureUpdateStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsIdpSignatureUpdateStatus.setStatus("current")
_JnxJsIdpNotifications_ObjectIdentity = ObjectIdentity
jnxJsIdpNotifications = _JnxJsIdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 2)
)
_JnxJsIdpNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxJsIdpNotificationPrefix = _JnxJsIdpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

jnxJsIdpSignatureUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 2, 0, 1)
)
jnxJsIdpSignatureUpdate.setObjects(
      *(("JUNIPER-JS-IDP-MIB", "jnxJsIdpRunningDetectorVersion"),
        ("JUNIPER-JS-IDP-MIB", "jnxJsIdpSecurityPackageVersion"),
        ("JUNIPER-JS-IDP-MIB", "jnxJsIdpLastSignatureUpdateTime"),
        ("JUNIPER-JS-IDP-MIB", "jnxJsIdpSignatureUpdateStatus"))
)
if mibBuilder.loadTexts:
    jnxJsIdpSignatureUpdate.setStatus(
        "current"
    )

jnxJsIdpAttackLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11, 1, 2, 0, 2)
)
jnxJsIdpAttackLog.setObjects(
      *(("JUNIPER-JS-IDP-MIB", "jnxJsIdpAttackName"),
        ("JUNIPER-JS-IDP-MIB", "jnxJsIdpAttackHits"))
)
if mibBuilder.loadTexts:
    jnxJsIdpAttackLog.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-IDP-MIB",
    **{"jnxJsIdpMIB": jnxJsIdpMIB,
       "jnxJsIdpObjects": jnxJsIdpObjects,
       "jnxJsIdpDataPlaneMemoryUsage": jnxJsIdpDataPlaneMemoryUsage,
       "jnxJsIdpSessionsUsage": jnxJsIdpSessionsUsage,
       "jnxJsIdpSessionsMaximum": jnxJsIdpSessionsMaximum,
       "jnxJsIdpPoliciesSupported": jnxJsIdpPoliciesSupported,
       "jnxJsIdpPoliciesLoaded": jnxJsIdpPoliciesLoaded,
       "jnxJsIdpActivePolicyName": jnxJsIdpActivePolicyName,
       "jnxJsIdpAttackTable": jnxJsIdpAttackTable,
       "jnxJsIdpAttackEntry": jnxJsIdpAttackEntry,
       "jnxJsIdpAttackIndex": jnxJsIdpAttackIndex,
       "jnxJsIdpAttackName": jnxJsIdpAttackName,
       "jnxJsIdpAttackHits": jnxJsIdpAttackHits,
       "jnxJsIdpRunningDetectorVersion": jnxJsIdpRunningDetectorVersion,
       "jnxJsIdpSecurityPackageVersion": jnxJsIdpSecurityPackageVersion,
       "jnxJsIdpLastSignatureUpdateTime": jnxJsIdpLastSignatureUpdateTime,
       "jnxJsIdpSignatureUpdateStatus": jnxJsIdpSignatureUpdateStatus,
       "jnxJsIdpNotifications": jnxJsIdpNotifications,
       "jnxJsIdpNotificationPrefix": jnxJsIdpNotificationPrefix,
       "jnxJsIdpSignatureUpdate": jnxJsIdpSignatureUpdate,
       "jnxJsIdpAttackLog": jnxJsIdpAttackLog}
)
