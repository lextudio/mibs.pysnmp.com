# SNMP MIB module (JUNIPER-PAE-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-PAE-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:59 2024
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

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(jnxExPaeExtension,) = mibBuilder.importSymbols(
    "JUNIPER-EX-SMI",
    "jnxExPaeExtension")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxPaeExtensionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxPaeExtensionMIBNotification_ObjectIdentity = ObjectIdentity
jnxPaeExtensionMIBNotification = _JnxPaeExtensionMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 0)
)
_JnxPaeExtensionMIBObjects_ObjectIdentity = ObjectIdentity
jnxPaeExtensionMIBObjects = _JnxPaeExtensionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1)
)


class _JnxAuthProfileName_Type(DisplayString):
    """Custom type jnxAuthProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxAuthProfileName_Type.__name__ = "DisplayString"
_JnxAuthProfileName_Object = MibScalar
jnxAuthProfileName = _JnxAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 1),
    _JnxAuthProfileName_Type()
)
jnxAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAuthProfileName.setStatus("current")
_JnxPaeAuthConfigTable_Object = MibTable
jnxPaeAuthConfigTable = _JnxPaeAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxPaeAuthConfigTable.setStatus("current")
_JnxPaeAuthConfigEntry_Object = MibTableRow
jnxPaeAuthConfigEntry = _JnxPaeAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1)
)
jnxPaeAuthConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    jnxPaeAuthConfigEntry.setStatus("current")
_JnxPaeAuthConfigMacAuthStatus_Type = TruthValue
_JnxPaeAuthConfigMacAuthStatus_Object = MibTableColumn
jnxPaeAuthConfigMacAuthStatus = _JnxPaeAuthConfigMacAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 1),
    _JnxPaeAuthConfigMacAuthStatus_Type()
)
jnxPaeAuthConfigMacAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigMacAuthStatus.setStatus("current")


class _JnxPaeAuthConfigGuestVlan_Type(DisplayString):
    """Custom type jnxPaeAuthConfigGuestVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxPaeAuthConfigGuestVlan_Type.__name__ = "DisplayString"
_JnxPaeAuthConfigGuestVlan_Object = MibTableColumn
jnxPaeAuthConfigGuestVlan = _JnxPaeAuthConfigGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 2),
    _JnxPaeAuthConfigGuestVlan_Type()
)
jnxPaeAuthConfigGuestVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigGuestVlan.setStatus("current")
_JnxPaeAuthConfigNumberRetries_Type = Unsigned32
_JnxPaeAuthConfigNumberRetries_Object = MibTableColumn
jnxPaeAuthConfigNumberRetries = _JnxPaeAuthConfigNumberRetries_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 3),
    _JnxPaeAuthConfigNumberRetries_Type()
)
jnxPaeAuthConfigNumberRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigNumberRetries.setStatus("current")


class _JnxPaeAuthConfigSupplicantMode_Type(Integer32):
    """Custom type jnxPaeAuthConfigSupplicantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 3),
          ("single", 1),
          ("single-secure", 2))
    )


_JnxPaeAuthConfigSupplicantMode_Type.__name__ = "Integer32"
_JnxPaeAuthConfigSupplicantMode_Object = MibTableColumn
jnxPaeAuthConfigSupplicantMode = _JnxPaeAuthConfigSupplicantMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 4),
    _JnxPaeAuthConfigSupplicantMode_Type()
)
jnxPaeAuthConfigSupplicantMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigSupplicantMode.setStatus("current")


class _JnxPaeAuthConfigMacRadius_Type(Integer32):
    """Custom type jnxPaeAuthConfigMacRadius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPaeAuthConfigMacRadius_Type.__name__ = "Integer32"
_JnxPaeAuthConfigMacRadius_Object = MibTableColumn
jnxPaeAuthConfigMacRadius = _JnxPaeAuthConfigMacRadius_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 5),
    _JnxPaeAuthConfigMacRadius_Type()
)
jnxPaeAuthConfigMacRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigMacRadius.setStatus("current")


class _JnxPaeAuthConfigMacRadiusRestrict_Type(Integer32):
    """Custom type jnxPaeAuthConfigMacRadiusRestrict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPaeAuthConfigMacRadiusRestrict_Type.__name__ = "Integer32"
_JnxPaeAuthConfigMacRadiusRestrict_Object = MibTableColumn
jnxPaeAuthConfigMacRadiusRestrict = _JnxPaeAuthConfigMacRadiusRestrict_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 6),
    _JnxPaeAuthConfigMacRadiusRestrict_Type()
)
jnxPaeAuthConfigMacRadiusRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigMacRadiusRestrict.setStatus("current")
_JnxPaeAuthConfigReAuthenticate_Type = TruthValue
_JnxPaeAuthConfigReAuthenticate_Object = MibTableColumn
jnxPaeAuthConfigReAuthenticate = _JnxPaeAuthConfigReAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 7),
    _JnxPaeAuthConfigReAuthenticate_Type()
)
jnxPaeAuthConfigReAuthenticate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigReAuthenticate.setStatus("current")
_JnxPaeAuthConfigQuietPeriod_Type = Unsigned32
_JnxPaeAuthConfigQuietPeriod_Object = MibTableColumn
jnxPaeAuthConfigQuietPeriod = _JnxPaeAuthConfigQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 8),
    _JnxPaeAuthConfigQuietPeriod_Type()
)
jnxPaeAuthConfigQuietPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigQuietPeriod.setUnits("seconds")
_JnxPaeAuthConfigMaxRequests_Type = Unsigned32
_JnxPaeAuthConfigMaxRequests_Object = MibTableColumn
jnxPaeAuthConfigMaxRequests = _JnxPaeAuthConfigMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 9),
    _JnxPaeAuthConfigMaxRequests_Type()
)
jnxPaeAuthConfigMaxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigMaxRequests.setStatus("current")


class _JnxPaeAuthConfigClientsRejected_Type(DisplayString):
    """Custom type jnxPaeAuthConfigClientsRejected based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxPaeAuthConfigClientsRejected_Type.__name__ = "DisplayString"
_JnxPaeAuthConfigClientsRejected_Object = MibTableColumn
jnxPaeAuthConfigClientsRejected = _JnxPaeAuthConfigClientsRejected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 10),
    _JnxPaeAuthConfigClientsRejected_Type()
)
jnxPaeAuthConfigClientsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigClientsRejected.setStatus("current")


class _JnxPaeAuthConfigServerTimeout_Type(Unsigned32):
    """Custom type jnxPaeAuthConfigServerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JnxPaeAuthConfigServerTimeout_Type.__name__ = "Unsigned32"
_JnxPaeAuthConfigServerTimeout_Object = MibTableColumn
jnxPaeAuthConfigServerTimeout = _JnxPaeAuthConfigServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 11),
    _JnxPaeAuthConfigServerTimeout_Type()
)
jnxPaeAuthConfigServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigServerTimeout.setUnits("seconds")


class _JnxPaeAuthConfigSuppTimeout_Type(Unsigned32):
    """Custom type jnxPaeAuthConfigSuppTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JnxPaeAuthConfigSuppTimeout_Type.__name__ = "Unsigned32"
_JnxPaeAuthConfigSuppTimeout_Object = MibTableColumn
jnxPaeAuthConfigSuppTimeout = _JnxPaeAuthConfigSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 12),
    _JnxPaeAuthConfigSuppTimeout_Type()
)
jnxPaeAuthConfigSuppTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigSuppTimeout.setStatus("current")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigSuppTimeout.setUnits("seconds")
_JnxPaeAuthConfigTransmitPeriod_Type = Unsigned32
_JnxPaeAuthConfigTransmitPeriod_Object = MibTableColumn
jnxPaeAuthConfigTransmitPeriod = _JnxPaeAuthConfigTransmitPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 2, 1, 13),
    _JnxPaeAuthConfigTransmitPeriod_Type()
)
jnxPaeAuthConfigTransmitPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPaeAuthConfigTransmitPeriod.setStatus("current")
_JnxStaticMacAuthBypassTable_Object = MibTable
jnxStaticMacAuthBypassTable = _JnxStaticMacAuthBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxStaticMacAuthBypassTable.setStatus("current")
_JnxStaticMacAuthBypassEntry_Object = MibTableRow
jnxStaticMacAuthBypassEntry = _JnxStaticMacAuthBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 3, 1)
)
jnxStaticMacAuthBypassEntry.setIndexNames(
    (0, "JUNIPER-PAE-EXTENSION-MIB", "jnxStaticMacAddress"),
)
if mibBuilder.loadTexts:
    jnxStaticMacAuthBypassEntry.setStatus("current")
_JnxStaticMacAddress_Type = MacAddress
_JnxStaticMacAddress_Object = MibTableColumn
jnxStaticMacAddress = _JnxStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 3, 1, 1),
    _JnxStaticMacAddress_Type()
)
jnxStaticMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxStaticMacAddress.setStatus("current")


class _JnxStaticMacVlanName_Type(DisplayString):
    """Custom type jnxStaticMacVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxStaticMacVlanName_Type.__name__ = "DisplayString"
_JnxStaticMacVlanName_Object = MibTableColumn
jnxStaticMacVlanName = _JnxStaticMacVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 3, 1, 2),
    _JnxStaticMacVlanName_Type()
)
jnxStaticMacVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStaticMacVlanName.setStatus("current")
_JnxStaticMacAuthBypassIfTable_Object = MibTable
jnxStaticMacAuthBypassIfTable = _JnxStaticMacAuthBypassIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxStaticMacAuthBypassIfTable.setStatus("current")
_JnxStaticMacAuthBypassIfEntry_Object = MibTableRow
jnxStaticMacAuthBypassIfEntry = _JnxStaticMacAuthBypassIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 4, 1)
)
jnxStaticMacAuthBypassIfEntry.setIndexNames(
    (0, "JUNIPER-PAE-EXTENSION-MIB", "jnxStaticMacAddress"),
    (0, "JUNIPER-PAE-EXTENSION-MIB", "jnxStaticMacIfIndex"),
)
if mibBuilder.loadTexts:
    jnxStaticMacAuthBypassIfEntry.setStatus("current")
_JnxStaticMacIfIndex_Type = InterfaceIndex
_JnxStaticMacIfIndex_Object = MibTableColumn
jnxStaticMacIfIndex = _JnxStaticMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3, 1, 1, 4, 1, 1),
    _JnxStaticMacIfIndex_Type()
)
jnxStaticMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStaticMacIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-PAE-EXTENSION-MIB",
    **{"jnxPaeExtensionMIB": jnxPaeExtensionMIB,
       "jnxPaeExtensionMIBNotification": jnxPaeExtensionMIBNotification,
       "jnxPaeExtensionMIBObjects": jnxPaeExtensionMIBObjects,
       "jnxAuthProfileName": jnxAuthProfileName,
       "jnxPaeAuthConfigTable": jnxPaeAuthConfigTable,
       "jnxPaeAuthConfigEntry": jnxPaeAuthConfigEntry,
       "jnxPaeAuthConfigMacAuthStatus": jnxPaeAuthConfigMacAuthStatus,
       "jnxPaeAuthConfigGuestVlan": jnxPaeAuthConfigGuestVlan,
       "jnxPaeAuthConfigNumberRetries": jnxPaeAuthConfigNumberRetries,
       "jnxPaeAuthConfigSupplicantMode": jnxPaeAuthConfigSupplicantMode,
       "jnxPaeAuthConfigMacRadius": jnxPaeAuthConfigMacRadius,
       "jnxPaeAuthConfigMacRadiusRestrict": jnxPaeAuthConfigMacRadiusRestrict,
       "jnxPaeAuthConfigReAuthenticate": jnxPaeAuthConfigReAuthenticate,
       "jnxPaeAuthConfigQuietPeriod": jnxPaeAuthConfigQuietPeriod,
       "jnxPaeAuthConfigMaxRequests": jnxPaeAuthConfigMaxRequests,
       "jnxPaeAuthConfigClientsRejected": jnxPaeAuthConfigClientsRejected,
       "jnxPaeAuthConfigServerTimeout": jnxPaeAuthConfigServerTimeout,
       "jnxPaeAuthConfigSuppTimeout": jnxPaeAuthConfigSuppTimeout,
       "jnxPaeAuthConfigTransmitPeriod": jnxPaeAuthConfigTransmitPeriod,
       "jnxStaticMacAuthBypassTable": jnxStaticMacAuthBypassTable,
       "jnxStaticMacAuthBypassEntry": jnxStaticMacAuthBypassEntry,
       "jnxStaticMacAddress": jnxStaticMacAddress,
       "jnxStaticMacVlanName": jnxStaticMacVlanName,
       "jnxStaticMacAuthBypassIfTable": jnxStaticMacAuthBypassIfTable,
       "jnxStaticMacAuthBypassIfEntry": jnxStaticMacAuthBypassIfEntry,
       "jnxStaticMacIfIndex": jnxStaticMacIfIndex}
)
