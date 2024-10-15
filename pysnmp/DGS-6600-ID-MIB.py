# SNMP MIB module (DGS-6600-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-6600-ID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:58 2024
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

(dlink_products,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-products")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dgs6600Series_ObjectIdentity = ObjectIdentity
dgs6600Series = _Dgs6600Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120)
)
_Dgs6604_ObjectIdentity = ObjectIdentity
dgs6604 = _Dgs6604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 1)
)
_Dgs6608_ObjectIdentity = ObjectIdentity
dgs6608 = _Dgs6608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 2)
)
_Dgs6600Private_ObjectIdentity = ObjectIdentity
dgs6600Private = _Dgs6600Private_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100)
)
_Dgs6600_system_ObjectIdentity = ObjectIdentity
dgs6600_system = _Dgs6600_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1)
)
_Dgs6600_l2_ObjectIdentity = ObjectIdentity
dgs6600_l2 = _Dgs6600_l2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 2)
)
_Dgs6600_l3_ObjectIdentity = ObjectIdentity
dgs6600_l3 = _Dgs6600_l3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 3)
)
_Dgs6600_mpls_ObjectIdentity = ObjectIdentity
dgs6600_mpls = _Dgs6600_mpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4)
)
_Dgs6600_qosacl_ObjectIdentity = ObjectIdentity
dgs6600_qosacl = _Dgs6600_qosacl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 5)
)
_Dgs6600_security_ObjectIdentity = ObjectIdentity
dgs6600_security = _Dgs6600_security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 6)
)
_Dgs6600_mgmt_ObjectIdentity = ObjectIdentity
dgs6600_mgmt = _Dgs6600_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 7)
)
_Dgs6600_others_ObjectIdentity = ObjectIdentity
dgs6600_others = _Dgs6600_others_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-6600-ID-MIB",
    **{"dgs6600Series": dgs6600Series,
       "dgs6604": dgs6604,
       "dgs6608": dgs6608,
       "dgs6600Private": dgs6600Private,
       "dgs6600-system": dgs6600_system,
       "dgs6600-l2": dgs6600_l2,
       "dgs6600-l3": dgs6600_l3,
       "dgs6600-mpls": dgs6600_mpls,
       "dgs6600-qosacl": dgs6600_qosacl,
       "dgs6600-security": dgs6600_security,
       "dgs6600-mgmt": dgs6600_mgmt,
       "dgs6600-others": dgs6600_others}
)
