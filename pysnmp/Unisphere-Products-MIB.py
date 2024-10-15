# SNMP MIB module (Unisphere-Products-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Products-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:49 2024
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

(unisphere,) = mibBuilder.importSymbols(
    "Unisphere-SMI",
    "unisphere")


# MODULE-IDENTITY

usProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1)
)
usProducts.setRevisions(
        ("2001-12-07 15:36",
         "2001-10-15 18:29",
         "2001-03-01 15:27",
         "2000-05-24 00:00",
         "1999-12-13 19:36",
         "1999-11-16 00:00",
         "1999-09-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProductFamilies_ObjectIdentity = ObjectIdentity
productFamilies = _ProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1)
)
_UnisphereProductFamilies_ObjectIdentity = ObjectIdentity
unisphereProductFamilies = _UnisphereProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1)
)
_UsErx_ObjectIdentity = ObjectIdentity
usErx = _UsErx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1)
)
_UsEdgeRoutingSwitch1400_ObjectIdentity = ObjectIdentity
usEdgeRoutingSwitch1400 = _UsEdgeRoutingSwitch1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 1)
)
_UsEdgeRoutingSwitch700_ObjectIdentity = ObjectIdentity
usEdgeRoutingSwitch700 = _UsEdgeRoutingSwitch700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 2)
)
_UsEdgeRoutingSwitch1440_ObjectIdentity = ObjectIdentity
usEdgeRoutingSwitch1440 = _UsEdgeRoutingSwitch1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 3)
)
_UsEdgeRoutingSwitch705_ObjectIdentity = ObjectIdentity
usEdgeRoutingSwitch705 = _UsEdgeRoutingSwitch705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 4)
)
_UsMrx_ObjectIdentity = ObjectIdentity
usMrx = _UsMrx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2)
)
_UsMrxRoutingSwitch16000_ObjectIdentity = ObjectIdentity
usMrxRoutingSwitch16000 = _UsMrxRoutingSwitch16000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1)
)
_UsMrxRoutingSwitch32000_ObjectIdentity = ObjectIdentity
usMrxRoutingSwitch32000 = _UsMrxRoutingSwitch32000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 2)
)
_UsSmx_ObjectIdentity = ObjectIdentity
usSmx = _UsSmx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 3)
)
_UsServiceMediationSwitch2100_ObjectIdentity = ObjectIdentity
usServiceMediationSwitch2100 = _UsServiceMediationSwitch2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 3, 1)
)
_UsSrx_ObjectIdentity = ObjectIdentity
usSrx = _UsSrx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 4)
)
_UsServiceReadySwitch3000_ObjectIdentity = ObjectIdentity
usServiceReadySwitch3000 = _UsServiceReadySwitch3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 4, 1)
)
_UsUmc_ObjectIdentity = ObjectIdentity
usUmc = _UsUmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 5)
)
_UsUmcSystemManagement_ObjectIdentity = ObjectIdentity
usUmcSystemManagement = _UsUmcSystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 5, 1)
)
_OemProductFamilies_ObjectIdentity = ObjectIdentity
oemProductFamilies = _OemProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 2)
)
_MarconiProductFamilies_ObjectIdentity = ObjectIdentity
marconiProductFamilies = _MarconiProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 2, 1)
)
_UsSsx_ObjectIdentity = ObjectIdentity
usSsx = _UsSsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 2, 1, 1)
)
_UsSsx1400_ObjectIdentity = ObjectIdentity
usSsx1400 = _UsSsx1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 2, 1, 1, 1)
)
_UsSsx700_ObjectIdentity = ObjectIdentity
usSsx700 = _UsSsx700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 2, 1, 1, 2)
)
_UsSsx1440_ObjectIdentity = ObjectIdentity
usSsx1440 = _UsSsx1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 2, 1, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Products-MIB",
    **{"usProducts": usProducts,
       "productFamilies": productFamilies,
       "unisphereProductFamilies": unisphereProductFamilies,
       "usErx": usErx,
       "usEdgeRoutingSwitch1400": usEdgeRoutingSwitch1400,
       "usEdgeRoutingSwitch700": usEdgeRoutingSwitch700,
       "usEdgeRoutingSwitch1440": usEdgeRoutingSwitch1440,
       "usEdgeRoutingSwitch705": usEdgeRoutingSwitch705,
       "usMrx": usMrx,
       "usMrxRoutingSwitch16000": usMrxRoutingSwitch16000,
       "usMrxRoutingSwitch32000": usMrxRoutingSwitch32000,
       "usSmx": usSmx,
       "usServiceMediationSwitch2100": usServiceMediationSwitch2100,
       "usSrx": usSrx,
       "usServiceReadySwitch3000": usServiceReadySwitch3000,
       "usUmc": usUmc,
       "usUmcSystemManagement": usUmcSystemManagement,
       "oemProductFamilies": oemProductFamilies,
       "marconiProductFamilies": marconiProductFamilies,
       "usSsx": usSsx,
       "usSsx1400": usSsx1400,
       "usSsx700": usSsx700,
       "usSsx1440": usSsx1440}
)
