# SNMP MIB module (SW36XXPRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW36XXPRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:48 2024
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

(dlink_mgmt,
 dlink_products) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-mgmt",
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

_Dlink_ProjectXStackIISeriesProd_ObjectIdentity = ObjectIdentity
dlink_ProjectXStackIISeriesProd = _Dlink_ProjectXStackIISeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70)
)
_Dlink_Dgs3650_ObjectIdentity = ObjectIdentity
dlink_Dgs3650 = _Dlink_Dgs3650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 5)
)
_Dlink_Dgs3627_ObjectIdentity = ObjectIdentity
dlink_Dgs3627 = _Dlink_Dgs3627_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 6)
)
_Dlink_Dgs3627g_ObjectIdentity = ObjectIdentity
dlink_Dgs3627g = _Dlink_Dgs3627g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 8)
)
_Dlink_Dgs3612g_ObjectIdentity = ObjectIdentity
dlink_Dgs3612g = _Dlink_Dgs3612g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 9)
)
_Dlink_Dgs3612_ObjectIdentity = ObjectIdentity
dlink_Dgs3612 = _Dlink_Dgs3612_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 10)
)
_DgsProjectXStackIISeriesProd_ObjectIdentity = ObjectIdentity
dgsProjectXStackIISeriesProd = _DgsProjectXStackIISeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70)
)
_Dgs3650_ObjectIdentity = ObjectIdentity
dgs3650 = _Dgs3650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 5)
)
_Dgs3627_ObjectIdentity = ObjectIdentity
dgs3627 = _Dgs3627_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 6)
)
_Dgs3627g_ObjectIdentity = ObjectIdentity
dgs3627g = _Dgs3627g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 8)
)
_Dgs3612g_ObjectIdentity = ObjectIdentity
dgs3612g = _Dgs3612g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 9)
)
_Dgs3612_ObjectIdentity = ObjectIdentity
dgs3612 = _Dgs3612_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW36XXPRIMGMT-MIB",
    **{"dlink-ProjectXStackIISeriesProd": dlink_ProjectXStackIISeriesProd,
       "dlink-Dgs3650": dlink_Dgs3650,
       "dlink-Dgs3627": dlink_Dgs3627,
       "dlink-Dgs3627g": dlink_Dgs3627g,
       "dlink-Dgs3612g": dlink_Dgs3612g,
       "dlink-Dgs3612": dlink_Dgs3612,
       "dgsProjectXStackIISeriesProd": dgsProjectXStackIISeriesProd,
       "dgs3650": dgs3650,
       "dgs3627": dgs3627,
       "dgs3627g": dgs3627g,
       "dgs3612g": dgs3612g,
       "dgs3612": dgs3612}
)
