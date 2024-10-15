# SNMP MIB module (SW-PROJECTX-SRPRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-PROJECTX-SRPRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:38 2024
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

_Dlink_ProjectXSeriesProd_ObjectIdentity = ObjectIdentity
dlink_ProjectXSeriesProd = _Dlink_ProjectXSeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59)
)
_Dlink_Dgs3224SRi_ObjectIdentity = ObjectIdentity
dlink_Dgs3224SRi = _Dlink_Dgs3224SRi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 1)
)
_Dlink_Dgs3224SR_ObjectIdentity = ObjectIdentity
dlink_Dgs3224SR = _Dlink_Dgs3224SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 2)
)
_Dlink_Des3252SR_ObjectIdentity = ObjectIdentity
dlink_Des3252SR = _Dlink_Des3252SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 3)
)
_Dlink_Dgs3324SRi_ObjectIdentity = ObjectIdentity
dlink_Dgs3324SRi = _Dlink_Dgs3324SRi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 4)
)
_Dlink_Dgs3324SR_ObjectIdentity = ObjectIdentity
dlink_Dgs3324SR = _Dlink_Dgs3324SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 5)
)
_Dlink_Des3352SR_ObjectIdentity = ObjectIdentity
dlink_Des3352SR = _Dlink_Des3352SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 6)
)
_Dlink_Dxs3326GSR_ObjectIdentity = ObjectIdentity
dlink_Dxs3326GSR = _Dlink_Dxs3326GSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 7)
)
_Dlink_Dxs3350SR_ObjectIdentity = ObjectIdentity
dlink_Dxs3350SR = _Dlink_Dxs3350SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 59, 8)
)
_Dlink_Des6500SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Des6500SeriesProd = _Dlink_Des6500SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 61)
)
_Dlink_Des6500_ObjectIdentity = ObjectIdentity
dlink_Des6500 = _Dlink_Des6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 61, 1)
)
_DgsProjectXSeriesProd_ObjectIdentity = ObjectIdentity
dgsProjectXSeriesProd = _DgsProjectXSeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59)
)
_Dgs3224SRi_ObjectIdentity = ObjectIdentity
dgs3224SRi = _Dgs3224SRi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 1)
)
_Dgs3224SR_ObjectIdentity = ObjectIdentity
dgs3224SR = _Dgs3224SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 2)
)
_Des3252SR_ObjectIdentity = ObjectIdentity
des3252SR = _Des3252SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 3)
)
_Dgs3324SRi_ObjectIdentity = ObjectIdentity
dgs3324SRi = _Dgs3324SRi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 4)
)
_Dgs3324SR_ObjectIdentity = ObjectIdentity
dgs3324SR = _Dgs3324SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 5)
)
_Des3352SR_ObjectIdentity = ObjectIdentity
des3352SR = _Des3352SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 6)
)
_Dxs3326GSR_ObjectIdentity = ObjectIdentity
dxs3326GSR = _Dxs3326GSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 7)
)
_Dxs3350SR_ObjectIdentity = ObjectIdentity
dxs3350SR = _Dxs3350SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 59, 8)
)
_Des6500SeriesProd_ObjectIdentity = ObjectIdentity
des6500SeriesProd = _Des6500SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 61)
)
_Des6500_ObjectIdentity = ObjectIdentity
des6500 = _Des6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 61, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-PROJECTX-SRPRIMGMT-MIB",
    **{"dlink-ProjectXSeriesProd": dlink_ProjectXSeriesProd,
       "dlink-Dgs3224SRi": dlink_Dgs3224SRi,
       "dlink-Dgs3224SR": dlink_Dgs3224SR,
       "dlink-Des3252SR": dlink_Des3252SR,
       "dlink-Dgs3324SRi": dlink_Dgs3324SRi,
       "dlink-Dgs3324SR": dlink_Dgs3324SR,
       "dlink-Des3352SR": dlink_Des3352SR,
       "dlink-Dxs3326GSR": dlink_Dxs3326GSR,
       "dlink-Dxs3350SR": dlink_Dxs3350SR,
       "dlink-Des6500SeriesProd": dlink_Des6500SeriesProd,
       "dlink-Des6500": dlink_Des6500,
       "dgsProjectXSeriesProd": dgsProjectXSeriesProd,
       "dgs3224SRi": dgs3224SRi,
       "dgs3224SR": dgs3224SR,
       "des3252SR": des3252SR,
       "dgs3324SRi": dgs3324SRi,
       "dgs3324SR": dgs3324SR,
       "des3352SR": des3352SR,
       "dxs3326GSR": dxs3326GSR,
       "dxs3350SR": dxs3350SR,
       "des6500SeriesProd": des6500SeriesProd,
       "des6500": des6500}
)
