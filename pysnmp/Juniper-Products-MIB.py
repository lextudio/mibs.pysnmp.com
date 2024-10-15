# SNMP MIB module (Juniper-Products-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-Products-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:05 2024
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

(juniperUni,) = mibBuilder.importSymbols(
    "Juniper-UNI-SMI",
    "juniperUni")

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

juniProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1)
)
juniProducts.setRevisions(
        ("2006-11-24 09:13",
         "2005-05-25 06:04",
         "2003-12-16 18:54",
         "2002-11-13 20:18",
         "2001-12-07 15:36",
         "2001-03-01 15:27",
         "2000-05-24 00:00",
         "1999-12-13 19:36",
         "1999-11-16 00:00",
         "1999-09-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniperUniProductFamilies_ObjectIdentity = ObjectIdentity
juniperUniProductFamilies = _JuniperUniProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1)
)
_JuniProductFamilies_ObjectIdentity = ObjectIdentity
juniProductFamilies = _JuniProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1)
)
_JuniErx_ObjectIdentity = ObjectIdentity
juniErx = _JuniErx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1)
)
_JuniErx1400_ObjectIdentity = ObjectIdentity
juniErx1400 = _JuniErx1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 1)
)
_JuniErx700_ObjectIdentity = ObjectIdentity
juniErx700 = _JuniErx700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 2)
)
_JuniErx1440_ObjectIdentity = ObjectIdentity
juniErx1440 = _JuniErx1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 3)
)
_JuniErx705_ObjectIdentity = ObjectIdentity
juniErx705 = _JuniErx705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 4)
)
_JuniErx310_ObjectIdentity = ObjectIdentity
juniErx310 = _JuniErx310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 1, 5)
)
_JuniOemProductFamilies_ObjectIdentity = ObjectIdentity
juniOemProductFamilies = _JuniOemProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2)
)
_JuniMarconiProductFamilies_ObjectIdentity = ObjectIdentity
juniMarconiProductFamilies = _JuniMarconiProductFamilies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1)
)
_JuniSsx_ObjectIdentity = ObjectIdentity
juniSsx = _JuniSsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1)
)
_JuniSsx1400_ObjectIdentity = ObjectIdentity
juniSsx1400 = _JuniSsx1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1, 1)
)
_JuniSsx700_ObjectIdentity = ObjectIdentity
juniSsx700 = _JuniSsx700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1, 2)
)
_JuniSsx1440_ObjectIdentity = ObjectIdentity
juniSsx1440 = _JuniSsx1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 2, 1, 1, 3)
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
_JuniUmc_ObjectIdentity = ObjectIdentity
juniUmc = _JuniUmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 5)
)
_JuniUmcSystemManagement_ObjectIdentity = ObjectIdentity
juniUmcSystemManagement = _JuniUmcSystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 5, 1)
)
_JuniEseries2_ObjectIdentity = ObjectIdentity
juniEseries2 = _JuniEseries2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 6)
)
_JuniE320_ObjectIdentity = ObjectIdentity
juniE320 = _JuniE320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 6, 1)
)
_JuniE120_ObjectIdentity = ObjectIdentity
juniE120 = _JuniE120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1, 1, 1, 6, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Products-MIB",
    **{"juniProducts": juniProducts,
       "juniperUniProductFamilies": juniperUniProductFamilies,
       "juniProductFamilies": juniProductFamilies,
       "juniErx": juniErx,
       "juniErx1400": juniErx1400,
       "juniErx700": juniErx700,
       "juniErx1440": juniErx1440,
       "juniErx705": juniErx705,
       "juniErx310": juniErx310,
       "juniOemProductFamilies": juniOemProductFamilies,
       "juniMarconiProductFamilies": juniMarconiProductFamilies,
       "juniSsx": juniSsx,
       "juniSsx1400": juniSsx1400,
       "juniSsx700": juniSsx700,
       "juniSsx1440": juniSsx1440,
       "usSmx": usSmx,
       "usServiceMediationSwitch2100": usServiceMediationSwitch2100,
       "usSrx": usSrx,
       "usServiceReadySwitch3000": usServiceReadySwitch3000,
       "juniUmc": juniUmc,
       "juniUmcSystemManagement": juniUmcSystemManagement,
       "juniEseries2": juniEseries2,
       "juniE320": juniE320,
       "juniE120": juniE120}
)
