# SNMP MIB module (BLUESOCKET-PRODUCTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUESOCKET-PRODUCTS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:26 2024
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

(blueSocket,) = mibBuilder.importSymbols(
    "BLUESOCKET-ROOT",
    "blueSocket")

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

blueProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Blue600_ObjectIdentity = ObjectIdentity
blue600 = _Blue600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 600)
)
_Gw600_ObjectIdentity = ObjectIdentity
gw600 = _Gw600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 600, 1)
)
_Blue1000_ObjectIdentity = ObjectIdentity
blue1000 = _Blue1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 1000)
)
_Gw1000_810_ObjectIdentity = ObjectIdentity
gw1000_810 = _Gw1000_810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 1000, 1)
)
_Gw1000_815_ObjectIdentity = ObjectIdentity
gw1000_815 = _Gw1000_815_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 1000, 2)
)
_Blue1100_ObjectIdentity = ObjectIdentity
blue1100 = _Blue1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 1100)
)
_Gw1100_ObjectIdentity = ObjectIdentity
gw1100 = _Gw1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 1100, 1)
)
_Blue1200_ObjectIdentity = ObjectIdentity
blue1200 = _Blue1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 1200)
)
_Gw1200_ObjectIdentity = ObjectIdentity
gw1200 = _Gw1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 1200, 1)
)
_Blue2000_ObjectIdentity = ObjectIdentity
blue2000 = _Blue2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2000)
)
_Gw2000_ObjectIdentity = ObjectIdentity
gw2000 = _Gw2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2000, 1)
)
_Gw2000_TF_ObjectIdentity = ObjectIdentity
gw2000_TF = _Gw2000_TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2000, 2)
)
_Gw2000_FT_ObjectIdentity = ObjectIdentity
gw2000_FT = _Gw2000_FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2000, 3)
)
_Gw2000_FF_ObjectIdentity = ObjectIdentity
gw2000_FF = _Gw2000_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2000, 4)
)
_Blue2100_ObjectIdentity = ObjectIdentity
blue2100 = _Blue2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2100)
)
_Gw2100_ObjectIdentity = ObjectIdentity
gw2100 = _Gw2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2100, 1)
)
_Gw2100_TF_ObjectIdentity = ObjectIdentity
gw2100_TF = _Gw2100_TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2100, 2)
)
_Gw2100_FT_ObjectIdentity = ObjectIdentity
gw2100_FT = _Gw2100_FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2100, 3)
)
_Gw2100_FF_ObjectIdentity = ObjectIdentity
gw2100_FF = _Gw2100_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2100, 4)
)
_Blue2200_ObjectIdentity = ObjectIdentity
blue2200 = _Blue2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2200)
)
_Gw2200_ObjectIdentity = ObjectIdentity
gw2200 = _Gw2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2200, 1)
)
_Gw2200_FF_ObjectIdentity = ObjectIdentity
gw2200_FF = _Gw2200_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2200, 4)
)
_Gw2200C_ObjectIdentity = ObjectIdentity
gw2200C = _Gw2200C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2200, 5)
)
_Gw2200C_FF_ObjectIdentity = ObjectIdentity
gw2200C_FF = _Gw2200C_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 2200, 8)
)
_Blue3200_ObjectIdentity = ObjectIdentity
blue3200 = _Blue3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 3200)
)
_Gw3200_ObjectIdentity = ObjectIdentity
gw3200 = _Gw3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 3200, 1)
)
_Gw3200_FF_ObjectIdentity = ObjectIdentity
gw3200_FF = _Gw3200_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 3200, 4)
)
_Gw3200C_ObjectIdentity = ObjectIdentity
gw3200C = _Gw3200C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 3200, 5)
)
_Gw3200C_FF_ObjectIdentity = ObjectIdentity
gw3200C_FF = _Gw3200C_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 3200, 8)
)
_Blue5000_ObjectIdentity = ObjectIdentity
blue5000 = _Blue5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5000)
)
_Gw5000_ObjectIdentity = ObjectIdentity
gw5000 = _Gw5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5000, 1)
)
_Gw5000_TF_ObjectIdentity = ObjectIdentity
gw5000_TF = _Gw5000_TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5000, 2)
)
_Gw5000_FT_ObjectIdentity = ObjectIdentity
gw5000_FT = _Gw5000_FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5000, 3)
)
_Gw5000_FF_ObjectIdentity = ObjectIdentity
gw5000_FF = _Gw5000_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5000, 4)
)
_Blue5200_ObjectIdentity = ObjectIdentity
blue5200 = _Blue5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5200)
)
_Gw5200_ObjectIdentity = ObjectIdentity
gw5200 = _Gw5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5200, 1)
)
_Gw5200_FF_ObjectIdentity = ObjectIdentity
gw5200_FF = _Gw5200_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5200, 4)
)
_Gw5200C_ObjectIdentity = ObjectIdentity
gw5200C = _Gw5200C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5200, 5)
)
_Gw5200C_FF_ObjectIdentity = ObjectIdentity
gw5200C_FF = _Gw5200C_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 5200, 8)
)
_Blue7200_ObjectIdentity = ObjectIdentity
blue7200 = _Blue7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 7200)
)
_Gw7200_ObjectIdentity = ObjectIdentity
gw7200 = _Gw7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 7200, 1)
)
_Gw7200_FF_ObjectIdentity = ObjectIdentity
gw7200_FF = _Gw7200_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 7200, 4)
)
_Gw7200C_ObjectIdentity = ObjectIdentity
gw7200C = _Gw7200C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 7200, 5)
)
_Gw7200C_FF_ObjectIdentity = ObjectIdentity
gw7200C_FF = _Gw7200C_FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 100, 7200, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUESOCKET-PRODUCTS",
    **{"blueProducts": blueProducts,
       "blue600": blue600,
       "gw600": gw600,
       "blue1000": blue1000,
       "gw1000-810": gw1000_810,
       "gw1000-815": gw1000_815,
       "blue1100": blue1100,
       "gw1100": gw1100,
       "blue1200": blue1200,
       "gw1200": gw1200,
       "blue2000": blue2000,
       "gw2000": gw2000,
       "gw2000-TF": gw2000_TF,
       "gw2000-FT": gw2000_FT,
       "gw2000-FF": gw2000_FF,
       "blue2100": blue2100,
       "gw2100": gw2100,
       "gw2100-TF": gw2100_TF,
       "gw2100-FT": gw2100_FT,
       "gw2100-FF": gw2100_FF,
       "blue2200": blue2200,
       "gw2200": gw2200,
       "gw2200-FF": gw2200_FF,
       "gw2200C": gw2200C,
       "gw2200C-FF": gw2200C_FF,
       "blue3200": blue3200,
       "gw3200": gw3200,
       "gw3200-FF": gw3200_FF,
       "gw3200C": gw3200C,
       "gw3200C-FF": gw3200C_FF,
       "blue5000": blue5000,
       "gw5000": gw5000,
       "gw5000-TF": gw5000_TF,
       "gw5000-FT": gw5000_FT,
       "gw5000-FF": gw5000_FF,
       "blue5200": blue5200,
       "gw5200": gw5200,
       "gw5200-FF": gw5200_FF,
       "gw5200C": gw5200C,
       "gw5200C-FF": gw5200C_FF,
       "blue7200": blue7200,
       "gw7200": gw7200,
       "gw7200-FF": gw7200_FF,
       "gw7200C": gw7200C,
       "gw7200C-FF": gw7200C_FF}
)
