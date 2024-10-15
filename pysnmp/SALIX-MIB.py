# SNMP MIB module (SALIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-MIB
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

salixTechnologies = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixExperimental_ObjectIdentity = ObjectIdentity
salixExperimental = _SalixExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 1)
)
if mibBuilder.loadTexts:
    salixExperimental.setStatus("current")
_SalixGeneric_ObjectIdentity = ObjectIdentity
salixGeneric = _SalixGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2)
)
if mibBuilder.loadTexts:
    salixGeneric.setStatus("current")
_SalixProducts_ObjectIdentity = ObjectIdentity
salixProducts = _SalixProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3)
)
if mibBuilder.loadTexts:
    salixProducts.setStatus("current")
_HybridSwitch_ObjectIdentity = ObjectIdentity
hybridSwitch = _HybridSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 1)
)
if mibBuilder.loadTexts:
    hybridSwitch.setStatus("current")
_Voip_ObjectIdentity = ObjectIdentity
voip = _Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 3, 2)
)
if mibBuilder.loadTexts:
    voip.setStatus("current")
_SalixRegistrations_ObjectIdentity = ObjectIdentity
salixRegistrations = _SalixRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 4)
)
if mibBuilder.loadTexts:
    salixRegistrations.setStatus("current")
_SalixPlatforms_ObjectIdentity = ObjectIdentity
salixPlatforms = _SalixPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5)
)
if mibBuilder.loadTexts:
    salixPlatforms.setStatus("current")
_Platform1_ObjectIdentity = ObjectIdentity
platform1 = _Platform1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1)
)
if mibBuilder.loadTexts:
    platform1.setStatus("current")
_SalixMIBCompliance_ObjectIdentity = ObjectIdentity
salixMIBCompliance = _SalixMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 6)
)
_SalixGroups_ObjectIdentity = ObjectIdentity
salixGroups = _SalixGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 6, 1)
)
_SalixCompliances_ObjectIdentity = ObjectIdentity
salixCompliances = _SalixCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 6, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

salixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 6, 2, 1)
)
if mibBuilder.loadTexts:
    salixCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-MIB",
    **{"salixTechnologies": salixTechnologies,
       "salixExperimental": salixExperimental,
       "salixGeneric": salixGeneric,
       "salixProducts": salixProducts,
       "hybridSwitch": hybridSwitch,
       "voip": voip,
       "salixRegistrations": salixRegistrations,
       "salixPlatforms": salixPlatforms,
       "platform1": platform1,
       "salixMIBCompliance": salixMIBCompliance,
       "salixGroups": salixGroups,
       "salixCompliances": salixCompliances,
       "salixCompliance": salixCompliance}
)
