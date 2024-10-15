# SNMP MIB module (SWPRIMGMT-DES3200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWPRIMGMT-DES3200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:10 2024
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

_Dlink_des3200SeriesProd_ObjectIdentity = ObjectIdentity
dlink_des3200SeriesProd = _Dlink_des3200SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113)
)
_Dlink_des3200ProdModel_ObjectIdentity = ObjectIdentity
dlink_des3200ProdModel = _Dlink_des3200ProdModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 1)
)
_Dlink_des3200_10Prod_ObjectIdentity = ObjectIdentity
dlink_des3200_10Prod = _Dlink_des3200_10Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 1, 1)
)
_Dlink_des3200_18Prod_ObjectIdentity = ObjectIdentity
dlink_des3200_18Prod = _Dlink_des3200_18Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 1, 2)
)
_Dlink_des3200_28Prod_ObjectIdentity = ObjectIdentity
dlink_des3200_28Prod = _Dlink_des3200_28Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 1, 3)
)
_Dlink_des3200_28fProd_ObjectIdentity = ObjectIdentity
dlink_des3200_28fProd = _Dlink_des3200_28fProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 1, 4)
)
_Dlink_des3200_26Prod_ObjectIdentity = ObjectIdentity
dlink_des3200_26Prod = _Dlink_des3200_26Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 1, 5)
)
_Dlink_des3200me_28Prod_ObjectIdentity = ObjectIdentity
dlink_des3200me_28Prod = _Dlink_des3200me_28Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 1, 6)
)
_Des_3200_10_ObjectIdentity = ObjectIdentity
des_3200_10 = _Des_3200_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 2)
)
_Des_3200_10_cx_ObjectIdentity = ObjectIdentity
des_3200_10_cx = _Des_3200_10_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 2, 1)
)
_Des_3200_18_ObjectIdentity = ObjectIdentity
des_3200_18 = _Des_3200_18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 3)
)
_Des_3200_18_cx_ObjectIdentity = ObjectIdentity
des_3200_18_cx = _Des_3200_18_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 3, 1)
)
_Des_3200_26_ObjectIdentity = ObjectIdentity
des_3200_26 = _Des_3200_26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 4)
)
_Des_3200_26_cx_ObjectIdentity = ObjectIdentity
des_3200_26_cx = _Des_3200_26_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 4, 1)
)
_Des_3200_28_ObjectIdentity = ObjectIdentity
des_3200_28 = _Des_3200_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 5)
)
_Des_3200_28_cx_ObjectIdentity = ObjectIdentity
des_3200_28_cx = _Des_3200_28_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 5, 1)
)
_Des_3200_28f_ObjectIdentity = ObjectIdentity
des_3200_28f = _Des_3200_28f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 6)
)
_Des_3200_28f_cx_ObjectIdentity = ObjectIdentity
des_3200_28f_cx = _Des_3200_28f_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 6, 1)
)
_Des_3200_28me_ObjectIdentity = ObjectIdentity
des_3200_28me = _Des_3200_28me_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 7)
)
_Des_3200_28me_cx_ObjectIdentity = ObjectIdentity
des_3200_28me_cx = _Des_3200_28me_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 7, 1)
)
_Des_3200_28p_ObjectIdentity = ObjectIdentity
des_3200_28p = _Des_3200_28p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 8)
)
_Des_3200_28p_cx_ObjectIdentity = ObjectIdentity
des_3200_28p_cx = _Des_3200_28p_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 8, 1)
)
_Des_3200_52_ObjectIdentity = ObjectIdentity
des_3200_52 = _Des_3200_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 9)
)
_Des_3200_52_cx_ObjectIdentity = ObjectIdentity
des_3200_52_cx = _Des_3200_52_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 9, 1)
)
_Des_3200_52p_ObjectIdentity = ObjectIdentity
des_3200_52p = _Des_3200_52p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 10)
)
_Des_3200_52p_cx_ObjectIdentity = ObjectIdentity
des_3200_52p_cx = _Des_3200_52p_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 10, 1)
)
_Des_3200_10_dc_ObjectIdentity = ObjectIdentity
des_3200_10_dc = _Des_3200_10_dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 11)
)
_Des_3200_10_dc_cx_ObjectIdentity = ObjectIdentity
des_3200_10_dc_cx = _Des_3200_10_dc_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 11, 1)
)
_Des_3200_26_dc_ObjectIdentity = ObjectIdentity
des_3200_26_dc = _Des_3200_26_dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 12)
)
_Des_3200_26_dc_cx_ObjectIdentity = ObjectIdentity
des_3200_26_dc_cx = _Des_3200_26_dc_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 113, 12, 1)
)
_Des3200SeriesProd_ObjectIdentity = ObjectIdentity
des3200SeriesProd = _Des3200SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113)
)
_Des3200ProdModel_ObjectIdentity = ObjectIdentity
des3200ProdModel = _Des3200ProdModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 1)
)
_Des3200_10_ObjectIdentity = ObjectIdentity
des3200_10 = _Des3200_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 2)
)
_Des3200_10_cx_ObjectIdentity = ObjectIdentity
des3200_10_cx = _Des3200_10_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 2, 1)
)
_Des3200_18_ObjectIdentity = ObjectIdentity
des3200_18 = _Des3200_18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3)
)
_Des3200_18_cx_ObjectIdentity = ObjectIdentity
des3200_18_cx = _Des3200_18_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 1)
)
_Des3200_26_ObjectIdentity = ObjectIdentity
des3200_26 = _Des3200_26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 4)
)
_Des3200_26_cx_ObjectIdentity = ObjectIdentity
des3200_26_cx = _Des3200_26_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 4, 1)
)
_Des3200_28_ObjectIdentity = ObjectIdentity
des3200_28 = _Des3200_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 5)
)
_Des3200_28_cx_ObjectIdentity = ObjectIdentity
des3200_28_cx = _Des3200_28_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 5, 1)
)
_Des3200_28f_ObjectIdentity = ObjectIdentity
des3200_28f = _Des3200_28f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 6)
)
_Des3200_28f_cx_ObjectIdentity = ObjectIdentity
des3200_28f_cx = _Des3200_28f_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 6, 1)
)
_Des3200_28me_ObjectIdentity = ObjectIdentity
des3200_28me = _Des3200_28me_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 7)
)
_Des3200_28me_cx_ObjectIdentity = ObjectIdentity
des3200_28me_cx = _Des3200_28me_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 7, 1)
)
_Des3200_28p_ObjectIdentity = ObjectIdentity
des3200_28p = _Des3200_28p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 8)
)
_Des3200_28p_cx_ObjectIdentity = ObjectIdentity
des3200_28p_cx = _Des3200_28p_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 8, 1)
)
_Des3200_52_ObjectIdentity = ObjectIdentity
des3200_52 = _Des3200_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 9)
)
_Des3200_52_cx_ObjectIdentity = ObjectIdentity
des3200_52_cx = _Des3200_52_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 9, 1)
)
_Des3200_52p_ObjectIdentity = ObjectIdentity
des3200_52p = _Des3200_52p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10)
)
_Des3200_52p_cx_ObjectIdentity = ObjectIdentity
des3200_52p_cx = _Des3200_52p_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1)
)
_Des3200_10_dc_ObjectIdentity = ObjectIdentity
des3200_10_dc = _Des3200_10_dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 11)
)
_Des3200_10_dc_cx_ObjectIdentity = ObjectIdentity
des3200_10_dc_cx = _Des3200_10_dc_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 11, 1)
)
_Des3200_26_dc_ObjectIdentity = ObjectIdentity
des3200_26_dc = _Des3200_26_dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 12)
)
_Des3200_26_dc_cx_ObjectIdentity = ObjectIdentity
des3200_26_dc_cx = _Des3200_26_dc_cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 12, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWPRIMGMT-DES3200-MIB",
    **{"dlink-des3200SeriesProd": dlink_des3200SeriesProd,
       "dlink-des3200ProdModel": dlink_des3200ProdModel,
       "dlink-des3200-10Prod": dlink_des3200_10Prod,
       "dlink-des3200-18Prod": dlink_des3200_18Prod,
       "dlink-des3200-28Prod": dlink_des3200_28Prod,
       "dlink-des3200-28fProd": dlink_des3200_28fProd,
       "dlink-des3200-26Prod": dlink_des3200_26Prod,
       "dlink-des3200me-28Prod": dlink_des3200me_28Prod,
       "des-3200-10": des_3200_10,
       "des-3200-10-cx": des_3200_10_cx,
       "des-3200-18": des_3200_18,
       "des-3200-18-cx": des_3200_18_cx,
       "des-3200-26": des_3200_26,
       "des-3200-26-cx": des_3200_26_cx,
       "des-3200-28": des_3200_28,
       "des-3200-28-cx": des_3200_28_cx,
       "des-3200-28f": des_3200_28f,
       "des-3200-28f-cx": des_3200_28f_cx,
       "des-3200-28me": des_3200_28me,
       "des-3200-28me-cx": des_3200_28me_cx,
       "des-3200-28p": des_3200_28p,
       "des-3200-28p-cx": des_3200_28p_cx,
       "des-3200-52": des_3200_52,
       "des-3200-52-cx": des_3200_52_cx,
       "des-3200-52p": des_3200_52p,
       "des-3200-52p-cx": des_3200_52p_cx,
       "des-3200-10-dc": des_3200_10_dc,
       "des-3200-10-dc-cx": des_3200_10_dc_cx,
       "des-3200-26-dc": des_3200_26_dc,
       "des-3200-26-dc-cx": des_3200_26_dc_cx,
       "des3200SeriesProd": des3200SeriesProd,
       "des3200ProdModel": des3200ProdModel,
       "des3200-10": des3200_10,
       "des3200-10-cx": des3200_10_cx,
       "des3200-18": des3200_18,
       "des3200-18-cx": des3200_18_cx,
       "des3200-26": des3200_26,
       "des3200-26-cx": des3200_26_cx,
       "des3200-28": des3200_28,
       "des3200-28-cx": des3200_28_cx,
       "des3200-28f": des3200_28f,
       "des3200-28f-cx": des3200_28f_cx,
       "des3200-28me": des3200_28me,
       "des3200-28me-cx": des3200_28me_cx,
       "des3200-28p": des3200_28p,
       "des3200-28p-cx": des3200_28p_cx,
       "des3200-52": des3200_52,
       "des3200-52-cx": des3200_52_cx,
       "des3200-52p": des3200_52p,
       "des3200-52p-cx": des3200_52p_cx,
       "des3200-10-dc": des3200_10_dc,
       "des3200-10-dc-cx": des3200_10_dc_cx,
       "des3200-26-dc": des3200_26_dc,
       "des3200-26-dc-cx": des3200_26_dc_cx}
)
