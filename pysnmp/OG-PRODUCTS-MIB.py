# SNMP MIB module (OG-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:50 2024
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

(ogModules,
 ogProducts) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "ogModules",
    "ogProducts")

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

ogProductsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 11, 2)
)
ogProductsMib.setRevisions(
        ("2016-02-10 00:00",
         "2015-06-02 00:00",
         "2013-08-11 00:00",
         "2011-08-15 01:23",
         "2010-04-15 11:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgCM4001_ObjectIdentity = ObjectIdentity
ogCM4001 = _OgCM4001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 1)
)
_OgCM4002_ObjectIdentity = ObjectIdentity
ogCM4002 = _OgCM4002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 2)
)
_OgCM4008_ObjectIdentity = ObjectIdentity
ogCM4008 = _OgCM4008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 3)
)
_OgCM41xx_ObjectIdentity = ObjectIdentity
ogCM41xx = _OgCM41xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 10)
)
_OgCM71xx_ObjectIdentity = ObjectIdentity
ogCM71xx = _OgCM71xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 11)
)
_OgSD4001_ObjectIdentity = ObjectIdentity
ogSD4001 = _OgSD4001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 20)
)
_OgSD4002_ObjectIdentity = ObjectIdentity
ogSD4002 = _OgSD4002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 21)
)
_OgSD4008_ObjectIdentity = ObjectIdentity
ogSD4008 = _OgSD4008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 22)
)
_OgSD4001DW_ObjectIdentity = ObjectIdentity
ogSD4001DW = _OgSD4001DW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 23)
)
_OgSD4002DX_ObjectIdentity = ObjectIdentity
ogSD4002DX = _OgSD4002DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 24)
)
_OgCD_ObjectIdentity = ObjectIdentity
ogCD = _OgCD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 30)
)
_OgCMx86_ObjectIdentity = ObjectIdentity
ogCMx86 = _OgCMx86_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 31)
)
_OgCMS61xx_ObjectIdentity = ObjectIdentity
ogCMS61xx = _OgCMS61xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 40)
)
_OgLighthouse_ObjectIdentity = ObjectIdentity
ogLighthouse = _OgLighthouse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 41)
)
_OgIM4004_ObjectIdentity = ObjectIdentity
ogIM4004 = _OgIM4004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 50)
)
_OgIM42xx_ObjectIdentity = ObjectIdentity
ogIM42xx = _OgIM42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 60)
)
_OgIM72xx_ObjectIdentity = ObjectIdentity
ogIM72xx = _OgIM72xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 61)
)
_OgKCS61xx_ObjectIdentity = ObjectIdentity
ogKCS61xx = _OgKCS61xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 70)
)
_OgACM500x_ObjectIdentity = ObjectIdentity
ogACM500x = _OgACM500x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 80)
)
_OgACM550x_ObjectIdentity = ObjectIdentity
ogACM550x = _OgACM550x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 81)
)
_OgACM700x_ObjectIdentity = ObjectIdentity
ogACM700x = _OgACM700x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 90)
)
_OgACM70045_ObjectIdentity = ObjectIdentity
ogACM70045 = _OgACM70045_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 91)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-PRODUCTS-MIB",
    **{"ogCM4001": ogCM4001,
       "ogCM4002": ogCM4002,
       "ogCM4008": ogCM4008,
       "ogCM41xx": ogCM41xx,
       "ogCM71xx": ogCM71xx,
       "ogSD4001": ogSD4001,
       "ogSD4002": ogSD4002,
       "ogSD4008": ogSD4008,
       "ogSD4001DW": ogSD4001DW,
       "ogSD4002DX": ogSD4002DX,
       "ogCD": ogCD,
       "ogCMx86": ogCMx86,
       "ogCMS61xx": ogCMS61xx,
       "ogLighthouse": ogLighthouse,
       "ogIM4004": ogIM4004,
       "ogIM42xx": ogIM42xx,
       "ogIM72xx": ogIM72xx,
       "ogKCS61xx": ogKCS61xx,
       "ogACM500x": ogACM500x,
       "ogACM550x": ogACM550x,
       "ogACM700x": ogACM700x,
       "ogACM70045": ogACM70045,
       "ogProductsMib": ogProductsMib}
)
