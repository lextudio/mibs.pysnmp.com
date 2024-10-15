# SNMP MIB module (WWP-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:20 2024
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

(wwpModules,
 wwpProducts) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpProducts")


# MODULE-IDENTITY

wwpProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 1)
)
wwpProductsMIB.setRevisions(
        ("2005-07-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLe21_ObjectIdentity = ObjectIdentity
wwpLe21 = _WwpLe21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 1)
)
_WwpLe22_ObjectIdentity = ObjectIdentity
wwpLe22 = _WwpLe22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 2)
)
_WwpLe31_ObjectIdentity = ObjectIdentity
wwpLe31 = _WwpLe31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 3)
)
_WwpLe32_ObjectIdentity = ObjectIdentity
wwpLe32 = _WwpLe32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 4)
)
_WwpLe41_ObjectIdentity = ObjectIdentity
wwpLe41 = _WwpLe41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 5)
)
_WwpLe42_ObjectIdentity = ObjectIdentity
wwpLe42 = _WwpLe42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 6)
)
_WwpLe200_ObjectIdentity = ObjectIdentity
wwpLe200 = _WwpLe200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 7)
)
_WwpLe210_ObjectIdentity = ObjectIdentity
wwpLe210 = _WwpLe210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 8)
)
_WwpLe220_ObjectIdentity = ObjectIdentity
wwpLe220 = _WwpLe220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 9)
)
_WwpLe410_ObjectIdentity = ObjectIdentity
wwpLe410 = _WwpLe410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 10)
)
_WwpLe3700_ObjectIdentity = ObjectIdentity
wwpLe3700 = _WwpLe3700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 11)
)
_WwpLe4400_ObjectIdentity = ObjectIdentity
wwpLe4400 = _WwpLe4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 12)
)
_WwpLe211_ObjectIdentity = ObjectIdentity
wwpLe211 = _WwpLe211_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 13)
)
_WwpLe211H_ObjectIdentity = ObjectIdentity
wwpLe211H = _WwpLe211H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 14)
)
_WwpLe216_ObjectIdentity = ObjectIdentity
wwpLe216 = _WwpLe216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 15)
)
_WwpLe216H_ObjectIdentity = ObjectIdentity
wwpLe216H = _WwpLe216H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 16)
)
_WwpLe218_ObjectIdentity = ObjectIdentity
wwpLe218 = _WwpLe218_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 17)
)
_WwpLe218H_ObjectIdentity = ObjectIdentity
wwpLe218H = _WwpLe218H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 18)
)
_WwpLe410H_ObjectIdentity = ObjectIdentity
wwpLe410H = _WwpLe410H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 19)
)
_WwpLe22H_ObjectIdentity = ObjectIdentity
wwpLe22H = _WwpLe22H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 20)
)
_WwpLe32H_ObjectIdentity = ObjectIdentity
wwpLe32H = _WwpLe32H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 21)
)
_WwpLe36_ObjectIdentity = ObjectIdentity
wwpLe36 = _WwpLe36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 22)
)
_WwpLe36H_ObjectIdentity = ObjectIdentity
wwpLe36H = _WwpLe36H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 23)
)
_WwpLe217_ObjectIdentity = ObjectIdentity
wwpLe217 = _WwpLe217_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 24)
)
_WwpLe217H_ObjectIdentity = ObjectIdentity
wwpLe217H = _WwpLe217H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 25)
)
_WwpLe217DC_ObjectIdentity = ObjectIdentity
wwpLe217DC = _WwpLe217DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 26)
)
_WwpLe410DC_ObjectIdentity = ObjectIdentity
wwpLe410DC = _WwpLe410DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 27)
)
_WwpLe317_ObjectIdentity = ObjectIdentity
wwpLe317 = _WwpLe317_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 28)
)
_WwpLe317H_ObjectIdentity = ObjectIdentity
wwpLe317H = _WwpLe317H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 29)
)
_WwpLe317DC_ObjectIdentity = ObjectIdentity
wwpLe317DC = _WwpLe317DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 30)
)
_WwpLe38_ObjectIdentity = ObjectIdentity
wwpLe38 = _WwpLe38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 31)
)
_WwpLe46_ObjectIdentity = ObjectIdentity
wwpLe46 = _WwpLe46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 32)
)
_WwpLe46Voip_ObjectIdentity = ObjectIdentity
wwpLe46Voip = _WwpLe46Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 33)
)
_WwpLe42H_ObjectIdentity = ObjectIdentity
wwpLe42H = _WwpLe42H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 34)
)
_WwpLe42HVoip_ObjectIdentity = ObjectIdentity
wwpLe42HVoip = _WwpLe42HVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 35)
)
_WwpLe407_ObjectIdentity = ObjectIdentity
wwpLe407 = _WwpLe407_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 36)
)
_WwpLe427_ObjectIdentity = ObjectIdentity
wwpLe427 = _WwpLe427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 37)
)
_WwpLe307_ObjectIdentity = ObjectIdentity
wwpLe307 = _WwpLe307_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 38)
)
_WwpLe327_ObjectIdentity = ObjectIdentity
wwpLe327 = _WwpLe327_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 39)
)
_WwpLe337_ObjectIdentity = ObjectIdentity
wwpLe337 = _WwpLe337_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 40)
)
_WwpLe22P0100_ObjectIdentity = ObjectIdentity
wwpLe22P0100 = _WwpLe22P0100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 41)
)
_WwpLe46H_ObjectIdentity = ObjectIdentity
wwpLe46H = _WwpLe46H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 42)
)
_WwpLe46HVoip_ObjectIdentity = ObjectIdentity
wwpLe46HVoip = _WwpLe46HVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 43)
)
_WwpLe42Voip_ObjectIdentity = ObjectIdentity
wwpLe42Voip = _WwpLe42Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 44)
)
_WwpLe17_ObjectIdentity = ObjectIdentity
wwpLe17 = _WwpLe17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 45)
)
_WwpLe17Voip_ObjectIdentity = ObjectIdentity
wwpLe17Voip = _WwpLe17Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 46)
)
_WwpLe311_ObjectIdentity = ObjectIdentity
wwpLe311 = _WwpLe311_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 47)
)
_WwpLe38Sfp_ObjectIdentity = ObjectIdentity
wwpLe38Sfp = _WwpLe38Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 48)
)
_WwpLe38SfpVoip_ObjectIdentity = ObjectIdentity
wwpLe38SfpVoip = _WwpLe38SfpVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 49)
)
_WwpLe311v_ObjectIdentity = ObjectIdentity
wwpLe311v = _WwpLe311v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 70)
)
_WwpLe310_ObjectIdentity = ObjectIdentity
wwpLe310 = _WwpLe310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 71)
)
_WwpLe135_ObjectIdentity = ObjectIdentity
wwpLe135 = _WwpLe135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 72)
)
_WwpLe3300_ObjectIdentity = ObjectIdentity
wwpLe3300 = _WwpLe3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 73)
)
_WwpLe3300Rev2_ObjectIdentity = ObjectIdentity
wwpLe3300Rev2 = _WwpLe3300Rev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 74)
)
_WwpLe3300FanTray_ObjectIdentity = ObjectIdentity
wwpLe3300FanTray = _WwpLe3300FanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 75)
)
_WwpLe58H_ObjectIdentity = ObjectIdentity
wwpLe58H = _WwpLe58H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 76)
)
_Cn3920_ObjectIdentity = ObjectIdentity
cn3920 = _Cn3920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 77)
)
_Cn3911_ObjectIdentity = ObjectIdentity
cn3911 = _Cn3911_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 78)
)
_Cn3940_ObjectIdentity = ObjectIdentity
cn3940 = _Cn3940_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 79)
)
_Cn5150_ObjectIdentity = ObjectIdentity
cn5150 = _Cn5150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 80)
)
_Cn3960_ObjectIdentity = ObjectIdentity
cn3960 = _Cn3960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 81)
)
_Cn5140_ObjectIdentity = ObjectIdentity
cn5140 = _Cn5140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 82)
)
_Cn5305_ObjectIdentity = ObjectIdentity
cn5305 = _Cn5305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 83)
)
_Cn3916_ObjectIdentity = ObjectIdentity
cn3916 = _Cn3916_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 84)
)
_Cn3930_ObjectIdentity = ObjectIdentity
cn3930 = _Cn3930_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 85)
)
_Cn3931_ObjectIdentity = ObjectIdentity
cn3931 = _Cn3931_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 86)
)
_Cn5142_ObjectIdentity = ObjectIdentity
cn5142 = _Cn5142_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 88)
)
_Cn3932_ObjectIdentity = ObjectIdentity
cn3932 = _Cn3932_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 89)
)
_Cn5160_ObjectIdentity = ObjectIdentity
cn5160 = _Cn5160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 90)
)
_Cn3902_ObjectIdentity = ObjectIdentity
cn3902 = _Cn3902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 1, 94)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-PRODUCTS-MIB",
    **{"wwpLe21": wwpLe21,
       "wwpLe22": wwpLe22,
       "wwpLe31": wwpLe31,
       "wwpLe32": wwpLe32,
       "wwpLe41": wwpLe41,
       "wwpLe42": wwpLe42,
       "wwpLe200": wwpLe200,
       "wwpLe210": wwpLe210,
       "wwpLe220": wwpLe220,
       "wwpLe410": wwpLe410,
       "wwpLe3700": wwpLe3700,
       "wwpLe4400": wwpLe4400,
       "wwpLe211": wwpLe211,
       "wwpLe211H": wwpLe211H,
       "wwpLe216": wwpLe216,
       "wwpLe216H": wwpLe216H,
       "wwpLe218": wwpLe218,
       "wwpLe218H": wwpLe218H,
       "wwpLe410H": wwpLe410H,
       "wwpLe22H": wwpLe22H,
       "wwpLe32H": wwpLe32H,
       "wwpLe36": wwpLe36,
       "wwpLe36H": wwpLe36H,
       "wwpLe217": wwpLe217,
       "wwpLe217H": wwpLe217H,
       "wwpLe217DC": wwpLe217DC,
       "wwpLe410DC": wwpLe410DC,
       "wwpLe317": wwpLe317,
       "wwpLe317H": wwpLe317H,
       "wwpLe317DC": wwpLe317DC,
       "wwpLe38": wwpLe38,
       "wwpLe46": wwpLe46,
       "wwpLe46Voip": wwpLe46Voip,
       "wwpLe42H": wwpLe42H,
       "wwpLe42HVoip": wwpLe42HVoip,
       "wwpLe407": wwpLe407,
       "wwpLe427": wwpLe427,
       "wwpLe307": wwpLe307,
       "wwpLe327": wwpLe327,
       "wwpLe337": wwpLe337,
       "wwpLe22P0100": wwpLe22P0100,
       "wwpLe46H": wwpLe46H,
       "wwpLe46HVoip": wwpLe46HVoip,
       "wwpLe42Voip": wwpLe42Voip,
       "wwpLe17": wwpLe17,
       "wwpLe17Voip": wwpLe17Voip,
       "wwpLe311": wwpLe311,
       "wwpLe38Sfp": wwpLe38Sfp,
       "wwpLe38SfpVoip": wwpLe38SfpVoip,
       "wwpLe311v": wwpLe311v,
       "wwpLe310": wwpLe310,
       "wwpLe135": wwpLe135,
       "wwpLe3300": wwpLe3300,
       "wwpLe3300Rev2": wwpLe3300Rev2,
       "wwpLe3300FanTray": wwpLe3300FanTray,
       "wwpLe58H": wwpLe58H,
       "cn3920": cn3920,
       "cn3911": cn3911,
       "cn3940": cn3940,
       "cn5150": cn5150,
       "cn3960": cn3960,
       "cn5140": cn5140,
       "cn5305": cn5305,
       "cn3916": cn3916,
       "cn3930": cn3930,
       "cn3931": cn3931,
       "cn5142": cn5142,
       "cn3932": cn3932,
       "cn5160": cn5160,
       "cn3902": cn3902,
       "wwpProductsMIB": wwpProductsMIB}
)
