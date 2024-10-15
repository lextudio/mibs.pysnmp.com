# SNMP MIB module (LEFTHAND-NETWORKS-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:40 2024
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

leftHandNetworksGlobalRegistrationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LeftHandNetworks_ObjectIdentity = ObjectIdentity
leftHandNetworks = _LeftHandNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804)
)
if mibBuilder.loadTexts:
    leftHandNetworks.setStatus("current")
_LhnRegistrations_ObjectIdentity = ObjectIdentity
lhnRegistrations = _LhnRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1)
)
if mibBuilder.loadTexts:
    lhnRegistrations.setStatus("current")
_LhnModules_ObjectIdentity = ObjectIdentity
lhnModules = _LhnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1)
)
if mibBuilder.loadTexts:
    lhnModules.setStatus("current")
_LhnNusDevices_ObjectIdentity = ObjectIdentity
lhnNusDevices = _LhnNusDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 2)
)
if mibBuilder.loadTexts:
    lhnNusDevices.setStatus("current")
_LhnNusCommon_ObjectIdentity = ObjectIdentity
lhnNusCommon = _LhnNusCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lhnNusCommon.setStatus("current")
_LhnGeneric_ObjectIdentity = ObjectIdentity
lhnGeneric = _LhnGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2)
)
if mibBuilder.loadTexts:
    lhnGeneric.setStatus("current")
_LhnProducts_ObjectIdentity = ObjectIdentity
lhnProducts = _LhnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3)
)
if mibBuilder.loadTexts:
    lhnProducts.setStatus("current")
_LhnNusDevicesMIBs_ObjectIdentity = ObjectIdentity
lhnNusDevicesMIBs = _LhnNusDevicesMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1)
)
if mibBuilder.loadTexts:
    lhnNusDevicesMIBs.setStatus("current")
_LhnNusCommonMIB_ObjectIdentity = ObjectIdentity
lhnNusCommonMIB = _LhnNusCommonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lhnNusCommonMIB.setStatus("current")
_LhnCapabilities_ObjectIdentity = ObjectIdentity
lhnCapabilities = _LhnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 4)
)
if mibBuilder.loadTexts:
    lhnCapabilities.setStatus("current")
_LhnRequirements_ObjectIdentity = ObjectIdentity
lhnRequirements = _LhnRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 5)
)
if mibBuilder.loadTexts:
    lhnRequirements.setStatus("current")
_LhnExperimental_ObjectIdentity = ObjectIdentity
lhnExperimental = _LhnExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 6)
)
if mibBuilder.loadTexts:
    lhnExperimental.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    **{"leftHandNetworks": leftHandNetworks,
       "lhnRegistrations": lhnRegistrations,
       "lhnModules": lhnModules,
       "leftHandNetworksGlobalRegistrationModule": leftHandNetworksGlobalRegistrationModule,
       "lhnNusDevices": lhnNusDevices,
       "lhnNusCommon": lhnNusCommon,
       "lhnGeneric": lhnGeneric,
       "lhnProducts": lhnProducts,
       "lhnNusDevicesMIBs": lhnNusDevicesMIBs,
       "lhnNusCommonMIB": lhnNusCommonMIB,
       "lhnCapabilities": lhnCapabilities,
       "lhnRequirements": lhnRequirements,
       "lhnExperimental": lhnExperimental}
)
