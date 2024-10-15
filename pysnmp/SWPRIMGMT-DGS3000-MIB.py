# SNMP MIB module (SWPRIMGMT-DGS3000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWPRIMGMT-DGS3000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:12 2024
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

_Dlink_dgs3000SeriesProd_ObjectIdentity = ObjectIdentity
dlink_dgs3000SeriesProd = _Dlink_dgs3000SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 133)
)
_Dgs_3000_10tc_ObjectIdentity = ObjectIdentity
dgs_3000_10tc = _Dgs_3000_10tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 133, 1)
)
_Dgs_3000_10_tc_ObjectIdentity = ObjectIdentity
dgs_3000_10_tc = _Dgs_3000_10_tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 133, 1, 1)
)
_Dgs_3000_26tc_ObjectIdentity = ObjectIdentity
dgs_3000_26tc = _Dgs_3000_26tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 133, 2)
)
_Dgs_3000_26_tc_ObjectIdentity = ObjectIdentity
dgs_3000_26_tc = _Dgs_3000_26_tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 133, 2, 1)
)
_Dgs_3000_24tc_ObjectIdentity = ObjectIdentity
dgs_3000_24tc = _Dgs_3000_24tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 133, 4)
)
_Dgs_3000_24_tcax_ObjectIdentity = ObjectIdentity
dgs_3000_24_tcax = _Dgs_3000_24_tcax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 133, 4, 1)
)
_Dgs3000SeriesProd_ObjectIdentity = ObjectIdentity
dgs3000SeriesProd = _Dgs3000SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133)
)
_Dgs3000_10tc_ObjectIdentity = ObjectIdentity
dgs3000_10tc = _Dgs3000_10tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 1)
)
_Dgs3000_10_tc_ObjectIdentity = ObjectIdentity
dgs3000_10_tc = _Dgs3000_10_tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 1, 1)
)
_Dgs3000_26tc_ObjectIdentity = ObjectIdentity
dgs3000_26tc = _Dgs3000_26tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 2)
)
_Dgs3000_26_tc_ObjectIdentity = ObjectIdentity
dgs3000_26_tc = _Dgs3000_26_tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 2, 1)
)
_Dgs3000_24tc_ObjectIdentity = ObjectIdentity
dgs3000_24tc = _Dgs3000_24tc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 4)
)
_Dgs3000_24_tcax_ObjectIdentity = ObjectIdentity
dgs3000_24_tcax = _Dgs3000_24_tcax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 4, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWPRIMGMT-DGS3000-MIB",
    **{"dlink-dgs3000SeriesProd": dlink_dgs3000SeriesProd,
       "dgs-3000-10tc": dgs_3000_10tc,
       "dgs-3000-10-tc": dgs_3000_10_tc,
       "dgs-3000-26tc": dgs_3000_26tc,
       "dgs-3000-26-tc": dgs_3000_26_tc,
       "dgs-3000-24tc": dgs_3000_24tc,
       "dgs-3000-24-tcax": dgs_3000_24_tcax,
       "dgs3000SeriesProd": dgs3000SeriesProd,
       "dgs3000-10tc": dgs3000_10tc,
       "dgs3000-10-tc": dgs3000_10_tc,
       "dgs3000-26tc": dgs3000_26tc,
       "dgs3000-26-tc": dgs3000_26_tc,
       "dgs3000-24tc": dgs3000_24tc,
       "dgs3000-24-tcax": dgs3000_24_tcax}
)
