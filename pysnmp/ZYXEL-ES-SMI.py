# SNMP MIB module (ZYXEL-ES-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-ES-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:17 2024
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

enterpriseSolution = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_EsAgentCapability_ObjectIdentity = ObjectIdentity
esAgentCapability = _EsAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 1)
)
if mibBuilder.loadTexts:
    esAgentCapability.setStatus("current")
_EsConformance_ObjectIdentity = ObjectIdentity
esConformance = _EsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 2)
)
if mibBuilder.loadTexts:
    esConformance.setStatus("current")
_EsMgmt_ObjectIdentity = ObjectIdentity
esMgmt = _EsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3)
)
if mibBuilder.loadTexts:
    esMgmt.setStatus("current")
_EsProductSpecific_ObjectIdentity = ObjectIdentity
esProductSpecific = _EsProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4)
)
if mibBuilder.loadTexts:
    esProductSpecific.setStatus("current")
_Tenders_ObjectIdentity = ObjectIdentity
tenders = _Tenders_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 4)
)
_ZyxelNAS_ObjectIdentity = ObjectIdentity
zyxelNAS = _ZyxelNAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 4, 5)
)
if mibBuilder.loadTexts:
    zyxelNAS.setStatus("current")
_EsPartnerProducts_ObjectIdentity = ObjectIdentity
esPartnerProducts = _EsPartnerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5)
)
if mibBuilder.loadTexts:
    esPartnerProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-SMI",
    **{"zyxel": zyxel,
       "products": products,
       "enterpriseSolution": enterpriseSolution,
       "esAgentCapability": esAgentCapability,
       "esConformance": esConformance,
       "esMgmt": esMgmt,
       "esProductSpecific": esProductSpecific,
       "tenders": tenders,
       "zyxelNAS": zyxelNAS,
       "esPartnerProducts": esPartnerProducts}
)
