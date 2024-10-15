# SNMP MIB module (Nortel-Magellan-Passport-UsefulDefinitionsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-UsefulDefinitionsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:13 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nortel_ObjectIdentity = ObjectIdentity
nortel = _Nortel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562)
)
_Magellan_ObjectIdentity = ObjectIdentity
magellan = _Magellan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 1)
)
_Passport50_ObjectIdentity = ObjectIdentity
passport50 = _Passport50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 1, 1)
)
_Passport160_ObjectIdentity = ObjectIdentity
passport160 = _Passport160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 1, 2)
)
_MeridianPassport_ObjectIdentity = ObjectIdentity
meridianPassport = _MeridianPassport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 1, 8)
)
_Passport30_ObjectIdentity = ObjectIdentity
passport30 = _Passport30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 1, 11)
)
_PassportVirtualRouter_ObjectIdentity = ObjectIdentity
passportVirtualRouter = _PassportVirtualRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 1, 12)
)
_Passport_ObjectIdentity = ObjectIdentity
passport = _Passport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4)
)
_Components_ObjectIdentity = ObjectIdentity
components = _Components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1)
)
_PassportTraps_ObjectIdentity = ObjectIdentity
passportTraps = _PassportTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3)
)
_PassportMIBs_ObjectIdentity = ObjectIdentity
passportMIBs = _PassportMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2)
)
_UsefulDefinitionsMIB_ObjectIdentity = ObjectIdentity
usefulDefinitionsMIB = _UsefulDefinitionsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1)
)
_UsefulDefinitionsGroup_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroup = _UsefulDefinitionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1)
)
_UsefulDefinitionsGroupBC_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroupBC = _UsefulDefinitionsGroupBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1, 3)
)
_UsefulDefinitionsGroupBC03_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroupBC03 = _UsefulDefinitionsGroupBC03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1, 3, 3)
)
_UsefulDefinitionsGroupBC03A_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroupBC03A = _UsefulDefinitionsGroupBC03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 1, 3, 3, 2)
)
_UsefulDefinitionsCapabilities_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilities = _UsefulDefinitionsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3)
)
_UsefulDefinitionsCapabilitiesBC_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilitiesBC = _UsefulDefinitionsCapabilitiesBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3, 3)
)
_UsefulDefinitionsCapabilitiesBC03_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilitiesBC03 = _UsefulDefinitionsCapabilitiesBC03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3, 3, 3)
)
_UsefulDefinitionsCapabilitiesBC03A_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilitiesBC03A = _UsefulDefinitionsCapabilitiesBC03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 1, 3, 3, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    **{"nortel": nortel,
       "magellan": magellan,
       "products": products,
       "passport50": passport50,
       "passport160": passport160,
       "meridianPassport": meridianPassport,
       "passport30": passport30,
       "passportVirtualRouter": passportVirtualRouter,
       "passport": passport,
       "components": components,
       "passportTraps": passportTraps,
       "passportMIBs": passportMIBs,
       "usefulDefinitionsMIB": usefulDefinitionsMIB,
       "usefulDefinitionsGroup": usefulDefinitionsGroup,
       "usefulDefinitionsGroupBC": usefulDefinitionsGroupBC,
       "usefulDefinitionsGroupBC03": usefulDefinitionsGroupBC03,
       "usefulDefinitionsGroupBC03A": usefulDefinitionsGroupBC03A,
       "usefulDefinitionsCapabilities": usefulDefinitionsCapabilities,
       "usefulDefinitionsCapabilitiesBC": usefulDefinitionsCapabilitiesBC,
       "usefulDefinitionsCapabilitiesBC03": usefulDefinitionsCapabilitiesBC03,
       "usefulDefinitionsCapabilitiesBC03A": usefulDefinitionsCapabilitiesBC03A}
)
