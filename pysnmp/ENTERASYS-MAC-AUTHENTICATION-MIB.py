# SNMP MIB module (ENTERASYS-MAC-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MAC-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:06 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysMACAuthenticationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25)
)
etsysMACAuthenticationMIB.setRevisions(
        ("2002-07-18 18:12",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysMACAuthenticationObjects_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationObjects = _EtsysMACAuthenticationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1)
)
_EtsysMACAuthenticationSystem_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationSystem = _EtsysMACAuthenticationSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 1)
)


class _EtsysMACAuthenticationSystemEnable_Type(EnabledStatus):
    """Custom type etsysMACAuthenticationSystemEnable based on EnabledStatus"""


_EtsysMACAuthenticationSystemEnable_Object = MibScalar
etsysMACAuthenticationSystemEnable = _EtsysMACAuthenticationSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 1, 1),
    _EtsysMACAuthenticationSystemEnable_Type()
)
etsysMACAuthenticationSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationSystemEnable.setStatus("current")


class _EtsysMACAuthenticationMACUserPassword_Type(SnmpAdminString):
    """Custom type etsysMACAuthenticationMACUserPassword based on SnmpAdminString"""
    defaultValue = OctetString("NOPASSWORD")


_EtsysMACAuthenticationMACUserPassword_Object = MibScalar
etsysMACAuthenticationMACUserPassword = _EtsysMACAuthenticationMACUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 1, 2),
    _EtsysMACAuthenticationMACUserPassword_Type()
)
etsysMACAuthenticationMACUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACUserPassword.setStatus("current")


class _EtsysMACAuthenticationPortUserNameSignificantBits_Type(Integer32):
    """Custom type etsysMACAuthenticationPortUserNameSignificantBits based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_EtsysMACAuthenticationPortUserNameSignificantBits_Type.__name__ = "Integer32"
_EtsysMACAuthenticationPortUserNameSignificantBits_Object = MibScalar
etsysMACAuthenticationPortUserNameSignificantBits = _EtsysMACAuthenticationPortUserNameSignificantBits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 1, 3),
    _EtsysMACAuthenticationPortUserNameSignificantBits_Type()
)
etsysMACAuthenticationPortUserNameSignificantBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortUserNameSignificantBits.setStatus("current")
_EtsysMACAuthenticationPortConfig_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationPortConfig = _EtsysMACAuthenticationPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2)
)
_EtsysMACAuthenticationPortConfigTable_Object = MibTable
etsysMACAuthenticationPortConfigTable = _EtsysMACAuthenticationPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortConfigTable.setStatus("current")
_EtsysMACAuthenticationPortConfigEntry_Object = MibTableRow
etsysMACAuthenticationPortConfigEntry = _EtsysMACAuthenticationPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1)
)
etsysMACAuthenticationPortConfigEntry.setIndexNames(
    (0, "ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPort"),
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortConfigEntry.setStatus("current")
_EtsysMACAuthenticationPort_Type = InterfaceIndex
_EtsysMACAuthenticationPort_Object = MibTableColumn
etsysMACAuthenticationPort = _EtsysMACAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 1),
    _EtsysMACAuthenticationPort_Type()
)
etsysMACAuthenticationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPort.setStatus("current")
_EtsysMACAuthenticationPortInitialize_Type = TruthValue
_EtsysMACAuthenticationPortInitialize_Object = MibTableColumn
etsysMACAuthenticationPortInitialize = _EtsysMACAuthenticationPortInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 2),
    _EtsysMACAuthenticationPortInitialize_Type()
)
etsysMACAuthenticationPortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortInitialize.setStatus("current")
_EtsysMACAuthenticationPortReauthenticate_Type = TruthValue
_EtsysMACAuthenticationPortReauthenticate_Object = MibTableColumn
etsysMACAuthenticationPortReauthenticate = _EtsysMACAuthenticationPortReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 3),
    _EtsysMACAuthenticationPortReauthenticate_Type()
)
etsysMACAuthenticationPortReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortReauthenticate.setStatus("current")


class _EtsysMACAuthenticationPortEnable_Type(EnabledStatus):
    """Custom type etsysMACAuthenticationPortEnable based on EnabledStatus"""


_EtsysMACAuthenticationPortEnable_Object = MibTableColumn
etsysMACAuthenticationPortEnable = _EtsysMACAuthenticationPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 4),
    _EtsysMACAuthenticationPortEnable_Type()
)
etsysMACAuthenticationPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortEnable.setStatus("current")


class _EtsysMACAuthenticationPortQuietPeriod_Type(Unsigned32):
    """Custom type etsysMACAuthenticationPortQuietPeriod based on Unsigned32"""
    defaultValue = 30


_EtsysMACAuthenticationPortQuietPeriod_Object = MibTableColumn
etsysMACAuthenticationPortQuietPeriod = _EtsysMACAuthenticationPortQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 5),
    _EtsysMACAuthenticationPortQuietPeriod_Type()
)
etsysMACAuthenticationPortQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortQuietPeriod.setStatus("current")


class _EtsysMACAuthenticationPortReauthPeriod_Type(Unsigned32):
    """Custom type etsysMACAuthenticationPortReauthPeriod based on Unsigned32"""
    defaultValue = 3600


_EtsysMACAuthenticationPortReauthPeriod_Object = MibTableColumn
etsysMACAuthenticationPortReauthPeriod = _EtsysMACAuthenticationPortReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 6),
    _EtsysMACAuthenticationPortReauthPeriod_Type()
)
etsysMACAuthenticationPortReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortReauthPeriod.setStatus("current")


class _EtsysMACAuthenticationPortReauthEnabled_Type(EnabledStatus):
    """Custom type etsysMACAuthenticationPortReauthEnabled based on EnabledStatus"""


_EtsysMACAuthenticationPortReauthEnabled_Object = MibTableColumn
etsysMACAuthenticationPortReauthEnabled = _EtsysMACAuthenticationPortReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 7),
    _EtsysMACAuthenticationPortReauthEnabled_Type()
)
etsysMACAuthenticationPortReauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortReauthEnabled.setStatus("current")
_EtsysMACAuthenticationAuthenticationsAllowed_Type = Unsigned32
_EtsysMACAuthenticationAuthenticationsAllowed_Object = MibTableColumn
etsysMACAuthenticationAuthenticationsAllowed = _EtsysMACAuthenticationAuthenticationsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 8),
    _EtsysMACAuthenticationAuthenticationsAllowed_Type()
)
etsysMACAuthenticationAuthenticationsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACAuthenticationAuthenticationsAllowed.setStatus("current")
_EtsysMACAuthenticationAuthenticationsAllocated_Type = Unsigned32
_EtsysMACAuthenticationAuthenticationsAllocated_Object = MibTableColumn
etsysMACAuthenticationAuthenticationsAllocated = _EtsysMACAuthenticationAuthenticationsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 9),
    _EtsysMACAuthenticationAuthenticationsAllocated_Type()
)
etsysMACAuthenticationAuthenticationsAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationAuthenticationsAllocated.setStatus("current")
_EtsysMACAuthenticationLastFailedAuthCause_Type = SnmpAdminString
_EtsysMACAuthenticationLastFailedAuthCause_Object = MibTableColumn
etsysMACAuthenticationLastFailedAuthCause = _EtsysMACAuthenticationLastFailedAuthCause_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 2, 1, 1, 10),
    _EtsysMACAuthenticationLastFailedAuthCause_Type()
)
etsysMACAuthenticationLastFailedAuthCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACAuthenticationLastFailedAuthCause.setStatus("current")
_EtsysMACAuthenticationMACConfig_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationMACConfig = _EtsysMACAuthenticationMACConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3)
)
_EtsysMACAuthenticationMACConfigTable_Object = MibTable
etsysMACAuthenticationMACConfigTable = _EtsysMACAuthenticationMACConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACConfigTable.setStatus("current")
_EtsysMACAuthenticationMACConfigEntry_Object = MibTableRow
etsysMACAuthenticationMACConfigEntry = _EtsysMACAuthenticationMACConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1, 1)
)
etsysMACAuthenticationMACConfigEntry.setIndexNames(
    (0, "ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationMACAddress"),
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACConfigEntry.setStatus("current")
_EtsysMACAuthenticationMACAddress_Type = MacAddress
_EtsysMACAuthenticationMACAddress_Object = MibTableColumn
etsysMACAuthenticationMACAddress = _EtsysMACAuthenticationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1, 1, 1),
    _EtsysMACAuthenticationMACAddress_Type()
)
etsysMACAuthenticationMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACAddress.setStatus("current")
_EtsysMACAuthenticationSupplicantPort_Type = InterfaceIndex
_EtsysMACAuthenticationSupplicantPort_Object = MibTableColumn
etsysMACAuthenticationSupplicantPort = _EtsysMACAuthenticationSupplicantPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1, 1, 2),
    _EtsysMACAuthenticationSupplicantPort_Type()
)
etsysMACAuthenticationSupplicantPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACAuthenticationSupplicantPort.setStatus("current")
_EtsysMACAuthenticationMACInitialize_Type = TruthValue
_EtsysMACAuthenticationMACInitialize_Object = MibTableColumn
etsysMACAuthenticationMACInitialize = _EtsysMACAuthenticationMACInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1, 1, 3),
    _EtsysMACAuthenticationMACInitialize_Type()
)
etsysMACAuthenticationMACInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACInitialize.setStatus("current")
_EtsysMACAuthenticationMACReauthenticate_Type = TruthValue
_EtsysMACAuthenticationMACReauthenticate_Object = MibTableColumn
etsysMACAuthenticationMACReauthenticate = _EtsysMACAuthenticationMACReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1, 1, 4),
    _EtsysMACAuthenticationMACReauthenticate_Type()
)
etsysMACAuthenticationMACReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACReauthenticate.setStatus("current")
_EtsysMACAuthenticationMACReauthPeriod_Type = Unsigned32
_EtsysMACAuthenticationMACReauthPeriod_Object = MibTableColumn
etsysMACAuthenticationMACReauthPeriod = _EtsysMACAuthenticationMACReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1, 1, 5),
    _EtsysMACAuthenticationMACReauthPeriod_Type()
)
etsysMACAuthenticationMACReauthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACReauthPeriod.setStatus("current")
_EtsysMACAuthenticationMACReauthEnabled_Type = EnabledStatus
_EtsysMACAuthenticationMACReauthEnabled_Object = MibTableColumn
etsysMACAuthenticationMACReauthEnabled = _EtsysMACAuthenticationMACReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 3, 1, 1, 6),
    _EtsysMACAuthenticationMACReauthEnabled_Type()
)
etsysMACAuthenticationMACReauthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACReauthEnabled.setStatus("current")
_EtsysMACAuthenticationMACSession_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationMACSession = _EtsysMACAuthenticationMACSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 4)
)
_EtsysMACAuthenticationSessionTable_Object = MibTable
etsysMACAuthenticationSessionTable = _EtsysMACAuthenticationSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationSessionTable.setStatus("current")
_EtsysMACAuthenticationSessionEntry_Object = MibTableRow
etsysMACAuthenticationSessionEntry = _EtsysMACAuthenticationSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 4, 1, 1)
)
etsysMACAuthenticationSessionEntry.setIndexNames(
    (0, "ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationMACAddress"),
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationSessionEntry.setStatus("current")
_EtsysMACAuthenticationSessionPort_Type = InterfaceIndex
_EtsysMACAuthenticationSessionPort_Object = MibTableColumn
etsysMACAuthenticationSessionPort = _EtsysMACAuthenticationSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 4, 1, 1, 1),
    _EtsysMACAuthenticationSessionPort_Type()
)
etsysMACAuthenticationSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACAuthenticationSessionPort.setStatus("current")
_EtsysMACAuthenticationDuration_Type = Unsigned32
_EtsysMACAuthenticationDuration_Object = MibTableColumn
etsysMACAuthenticationDuration = _EtsysMACAuthenticationDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 1, 4, 1, 1, 2),
    _EtsysMACAuthenticationDuration_Type()
)
etsysMACAuthenticationDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACAuthenticationDuration.setStatus("current")
_EtsysMACAuthenticationConformance_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationConformance = _EtsysMACAuthenticationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2)
)
_EtsysMACAuthenticationGroups_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationGroups = _EtsysMACAuthenticationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2, 1)
)
_EtsysMACAuthenticationCompliances_ObjectIdentity = ObjectIdentity
etsysMACAuthenticationCompliances = _EtsysMACAuthenticationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2, 2)
)

# Managed Objects groups

etsysMACAuthenticationSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2, 1, 1)
)
etsysMACAuthenticationSystemGroup.setObjects(
      *(("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationSystemEnable"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationMACUserPassword"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPortUserNameSignificantBits"))
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationSystemGroup.setStatus("current")

etsysMACAuthenticationPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2, 1, 2)
)
etsysMACAuthenticationPortConfigGroup.setObjects(
      *(("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPortInitialize"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPortReauthenticate"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPortEnable"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPortQuietPeriod"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPortReauthPeriod"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationPortReauthEnabled"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationAuthenticationsAllowed"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationAuthenticationsAllocated"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationLastFailedAuthCause"))
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationPortConfigGroup.setStatus("current")

etsysMACAuthenticationMACConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2, 1, 3)
)
etsysMACAuthenticationMACConfigGroup.setObjects(
      *(("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationSupplicantPort"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationMACInitialize"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationMACReauthenticate"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationMACReauthPeriod"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationMACReauthEnabled"))
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACConfigGroup.setStatus("current")

etsysMACAuthenticationMACSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2, 1, 4)
)
etsysMACAuthenticationMACSessionGroup.setObjects(
      *(("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationSessionPort"),
        ("ENTERASYS-MAC-AUTHENTICATION-MIB", "etsysMACAuthenticationDuration"))
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationMACSessionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysMACAuthenticationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 25, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMACAuthenticationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MAC-AUTHENTICATION-MIB",
    **{"etsysMACAuthenticationMIB": etsysMACAuthenticationMIB,
       "etsysMACAuthenticationObjects": etsysMACAuthenticationObjects,
       "etsysMACAuthenticationSystem": etsysMACAuthenticationSystem,
       "etsysMACAuthenticationSystemEnable": etsysMACAuthenticationSystemEnable,
       "etsysMACAuthenticationMACUserPassword": etsysMACAuthenticationMACUserPassword,
       "etsysMACAuthenticationPortUserNameSignificantBits": etsysMACAuthenticationPortUserNameSignificantBits,
       "etsysMACAuthenticationPortConfig": etsysMACAuthenticationPortConfig,
       "etsysMACAuthenticationPortConfigTable": etsysMACAuthenticationPortConfigTable,
       "etsysMACAuthenticationPortConfigEntry": etsysMACAuthenticationPortConfigEntry,
       "etsysMACAuthenticationPort": etsysMACAuthenticationPort,
       "etsysMACAuthenticationPortInitialize": etsysMACAuthenticationPortInitialize,
       "etsysMACAuthenticationPortReauthenticate": etsysMACAuthenticationPortReauthenticate,
       "etsysMACAuthenticationPortEnable": etsysMACAuthenticationPortEnable,
       "etsysMACAuthenticationPortQuietPeriod": etsysMACAuthenticationPortQuietPeriod,
       "etsysMACAuthenticationPortReauthPeriod": etsysMACAuthenticationPortReauthPeriod,
       "etsysMACAuthenticationPortReauthEnabled": etsysMACAuthenticationPortReauthEnabled,
       "etsysMACAuthenticationAuthenticationsAllowed": etsysMACAuthenticationAuthenticationsAllowed,
       "etsysMACAuthenticationAuthenticationsAllocated": etsysMACAuthenticationAuthenticationsAllocated,
       "etsysMACAuthenticationLastFailedAuthCause": etsysMACAuthenticationLastFailedAuthCause,
       "etsysMACAuthenticationMACConfig": etsysMACAuthenticationMACConfig,
       "etsysMACAuthenticationMACConfigTable": etsysMACAuthenticationMACConfigTable,
       "etsysMACAuthenticationMACConfigEntry": etsysMACAuthenticationMACConfigEntry,
       "etsysMACAuthenticationMACAddress": etsysMACAuthenticationMACAddress,
       "etsysMACAuthenticationSupplicantPort": etsysMACAuthenticationSupplicantPort,
       "etsysMACAuthenticationMACInitialize": etsysMACAuthenticationMACInitialize,
       "etsysMACAuthenticationMACReauthenticate": etsysMACAuthenticationMACReauthenticate,
       "etsysMACAuthenticationMACReauthPeriod": etsysMACAuthenticationMACReauthPeriod,
       "etsysMACAuthenticationMACReauthEnabled": etsysMACAuthenticationMACReauthEnabled,
       "etsysMACAuthenticationMACSession": etsysMACAuthenticationMACSession,
       "etsysMACAuthenticationSessionTable": etsysMACAuthenticationSessionTable,
       "etsysMACAuthenticationSessionEntry": etsysMACAuthenticationSessionEntry,
       "etsysMACAuthenticationSessionPort": etsysMACAuthenticationSessionPort,
       "etsysMACAuthenticationDuration": etsysMACAuthenticationDuration,
       "etsysMACAuthenticationConformance": etsysMACAuthenticationConformance,
       "etsysMACAuthenticationGroups": etsysMACAuthenticationGroups,
       "etsysMACAuthenticationSystemGroup": etsysMACAuthenticationSystemGroup,
       "etsysMACAuthenticationPortConfigGroup": etsysMACAuthenticationPortConfigGroup,
       "etsysMACAuthenticationMACConfigGroup": etsysMACAuthenticationMACConfigGroup,
       "etsysMACAuthenticationMACSessionGroup": etsysMACAuthenticationMACSessionGroup,
       "etsysMACAuthenticationCompliances": etsysMACAuthenticationCompliances,
       "etsysMACAuthenticationCompliance": etsysMACAuthenticationCompliance}
)
