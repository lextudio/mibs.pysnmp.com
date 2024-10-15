# SNMP MIB module (Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:44 2024
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
_MsCarrier_ObjectIdentity = ObjectIdentity
msCarrier = _MsCarrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36)
)
_MscProducts_ObjectIdentity = ObjectIdentity
mscProducts = _MscProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 1)
)
_MscPassport7440_ObjectIdentity = ObjectIdentity
mscPassport7440 = _MscPassport7440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 1, 1)
)
_MscPassport7480_ObjectIdentity = ObjectIdentity
mscPassport7480 = _MscPassport7480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 1, 2)
)
_MscPassportVirtualRouter_ObjectIdentity = ObjectIdentity
mscPassportVirtualRouter = _MscPassportVirtualRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 1, 3)
)
_MscPassport15000_ObjectIdentity = ObjectIdentity
mscPassport15000 = _MscPassport15000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 1, 4)
)
_MscPassport_ObjectIdentity = ObjectIdentity
mscPassport = _MscPassport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2)
)
_MscComponents_ObjectIdentity = ObjectIdentity
mscComponents = _MscComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1)
)
_MscPassportTraps_ObjectIdentity = ObjectIdentity
mscPassportTraps = _MscPassportTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3)
)
_MscPassportMIBs_ObjectIdentity = ObjectIdentity
mscPassportMIBs = _MscPassportMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2)
)
_UsefulDefinitionsMIB_ObjectIdentity = ObjectIdentity
usefulDefinitionsMIB = _UsefulDefinitionsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1)
)
_UsefulDefinitionsGroup_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroup = _UsefulDefinitionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1)
)
_UsefulDefinitionsGroupCA_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroupCA = _UsefulDefinitionsGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1, 1)
)
_UsefulDefinitionsGroupCA01_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroupCA01 = _UsefulDefinitionsGroupCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1, 1, 2)
)
_UsefulDefinitionsGroupCA01A_ObjectIdentity = ObjectIdentity
usefulDefinitionsGroupCA01A = _UsefulDefinitionsGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 1, 1, 2, 2)
)
_UsefulDefinitionsCapabilities_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilities = _UsefulDefinitionsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3)
)
_UsefulDefinitionsCapabilitiesCA_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilitiesCA = _UsefulDefinitionsCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3, 1)
)
_UsefulDefinitionsCapabilitiesCA01_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilitiesCA01 = _UsefulDefinitionsCapabilitiesCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3, 1, 2)
)
_UsefulDefinitionsCapabilitiesCA01A_ObjectIdentity = ObjectIdentity
usefulDefinitionsCapabilitiesCA01A = _UsefulDefinitionsCapabilitiesCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 1, 3, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    **{"nortel": nortel,
       "msCarrier": msCarrier,
       "mscProducts": mscProducts,
       "mscPassport7440": mscPassport7440,
       "mscPassport7480": mscPassport7480,
       "mscPassportVirtualRouter": mscPassportVirtualRouter,
       "mscPassport15000": mscPassport15000,
       "mscPassport": mscPassport,
       "mscComponents": mscComponents,
       "mscPassportTraps": mscPassportTraps,
       "mscPassportMIBs": mscPassportMIBs,
       "usefulDefinitionsMIB": usefulDefinitionsMIB,
       "usefulDefinitionsGroup": usefulDefinitionsGroup,
       "usefulDefinitionsGroupCA": usefulDefinitionsGroupCA,
       "usefulDefinitionsGroupCA01": usefulDefinitionsGroupCA01,
       "usefulDefinitionsGroupCA01A": usefulDefinitionsGroupCA01A,
       "usefulDefinitionsCapabilities": usefulDefinitionsCapabilities,
       "usefulDefinitionsCapabilitiesCA": usefulDefinitionsCapabilitiesCA,
       "usefulDefinitionsCapabilitiesCA01": usefulDefinitionsCapabilitiesCA01,
       "usefulDefinitionsCapabilitiesCA01A": usefulDefinitionsCapabilitiesCA01A}
)
