# SNMP MIB module (SALIX-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:33 2024
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

(salixGeneric,
 salixGroups,
 salixProducts,
 salixRegistrations) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "salixGeneric",
    "salixGroups",
    "salixProducts",
    "salixRegistrations")

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

salixProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hne_ObjectIdentity = ObjectIdentity
hne = _Hne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 4, 1)
)
_HneAgent_ObjectIdentity = ObjectIdentity
hneAgent = _HneAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 4, 2)
)
_HneAgentMajorVersion_Type = Unsigned32
_HneAgentMajorVersion_Object = MibScalar
hneAgentMajorVersion = _HneAgentMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2158, 4, 2, 1),
    _HneAgentMajorVersion_Type()
)
hneAgentMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAgentMajorVersion.setStatus("current")
_HneAgentSubVersion_Type = Unsigned32
_HneAgentSubVersion_Object = MibScalar
hneAgentSubVersion = _HneAgentSubVersion_Object(
    (1, 3, 6, 1, 4, 1, 2158, 4, 2, 2),
    _HneAgentSubVersion_Type()
)
hneAgentSubVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneAgentSubVersion.setStatus("current")
_Itx_ObjectIdentity = ObjectIdentity
itx = _Itx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 4, 3)
)
if mibBuilder.loadTexts:
    itx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-PRODUCTS-MIB",
    **{"salixProductsMIB": salixProductsMIB,
       "hne": hne,
       "hneAgent": hneAgent,
       "hneAgentMajorVersion": hneAgentMajorVersion,
       "hneAgentSubVersion": hneAgentSubVersion,
       "itx": itx}
)
