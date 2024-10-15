# SNMP MIB module (TIPPINGPOINT-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIPPINGPOINT-REG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:21 2024
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

tippingpoint = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734)
)
tippingpoint.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tpt_reg_ObjectIdentity = ObjectIdentity
tpt_reg = _Tpt_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1)
)
if mibBuilder.loadTexts:
    tpt_reg.setStatus("current")
_Tpt_generic_ObjectIdentity = ObjectIdentity
tpt_generic = _Tpt_generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 2)
)
if mibBuilder.loadTexts:
    tpt_generic.setStatus("current")
_Tpt_products_ObjectIdentity = ObjectIdentity
tpt_products = _Tpt_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3)
)
if mibBuilder.loadTexts:
    tpt_products.setStatus("current")
_Tpt_caps_ObjectIdentity = ObjectIdentity
tpt_caps = _Tpt_caps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 4)
)
if mibBuilder.loadTexts:
    tpt_caps.setStatus("current")
_Tpt_reqs_ObjectIdentity = ObjectIdentity
tpt_reqs = _Tpt_reqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 5)
)
if mibBuilder.loadTexts:
    tpt_reqs.setStatus("current")
_Tpt_expr_ObjectIdentity = ObjectIdentity
tpt_expr = _Tpt_expr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 6)
)
if mibBuilder.loadTexts:
    tpt_expr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIPPINGPOINT-REG-MIB",
    **{"tippingpoint": tippingpoint,
       "tpt-reg": tpt_reg,
       "tpt-generic": tpt_generic,
       "tpt-products": tpt_products,
       "tpt-caps": tpt_caps,
       "tpt-reqs": tpt_reqs,
       "tpt-expr": tpt_expr}
)
