# SNMP MIB module (NOKIA-IPSO-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-IPSO-REGISTRATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:40 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ipsoProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21)
)
ipsoProducts.setRevisions(
        ("1998-12-02 00:00",
         "1900-01-14 00:00",
         "1901-07-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nokia_ObjectIdentity = ObjectIdentity
nokia = _Nokia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94)
)
_NokiaProducts_ObjectIdentity = ObjectIdentity
nokiaProducts = _NokiaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1)
)
_IpsoProductIds_ObjectIdentity = ObjectIdentity
ipsoProductIds = _IpsoProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2)
)
_IpsoAgentID_ObjectIdentity = ObjectIdentity
ipsoAgentID = _IpsoAgentID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1)
)
_IpsoIPUnknown_ObjectIdentity = ObjectIdentity
ipsoIPUnknown = _IpsoIPUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 1)
)
_IpsoIP4xx_ObjectIdentity = ObjectIdentity
ipsoIP4xx = _IpsoIP4xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 2)
)
_IpsoIP400_ObjectIdentity = ObjectIdentity
ipsoIP400 = _IpsoIP400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 3)
)
_IpsoIP410_ObjectIdentity = ObjectIdentity
ipsoIP410 = _IpsoIP410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 4)
)
_IpsoIP440_ObjectIdentity = ObjectIdentity
ipsoIP440 = _IpsoIP440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 5)
)
_IpsoIP6xx_ObjectIdentity = ObjectIdentity
ipsoIP6xx = _IpsoIP6xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 6)
)
_IpsoIP600_ObjectIdentity = ObjectIdentity
ipsoIP600 = _IpsoIP600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 7)
)
_IpsoIP650_ObjectIdentity = ObjectIdentity
ipsoIP650 = _IpsoIP650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 8)
)
_IpsoIP3xx_ObjectIdentity = ObjectIdentity
ipsoIP3xx = _IpsoIP3xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 9)
)
_IpsoIP110_ObjectIdentity = ObjectIdentity
ipsoIP110 = _IpsoIP110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 10)
)
_IpsoIP530_ObjectIdentity = ObjectIdentity
ipsoIP530 = _IpsoIP530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 11)
)
_IpsoIP740_ObjectIdentity = ObjectIdentity
ipsoIP740 = _IpsoIP740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 12)
)
_IpsoIP3400_ObjectIdentity = ObjectIdentity
ipsoIP3400 = _IpsoIP3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 13)
)
_IpsoVPNUnknown_ObjectIdentity = ObjectIdentity
ipsoVPNUnknown = _IpsoVPNUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 128)
)
_IpsoVPN1RL50_ObjectIdentity = ObjectIdentity
ipsoVPN1RL50 = _IpsoVPN1RL50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 129)
)
_IpsoVPN1RL250_ObjectIdentity = ObjectIdentity
ipsoVPN1RL250 = _IpsoVPN1RL250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 130)
)
_IpsoVPN1RL500_ObjectIdentity = ObjectIdentity
ipsoVPN1RL500 = _IpsoVPN1RL500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 131)
)
_IpsoVPN1RLU_ObjectIdentity = ObjectIdentity
ipsoVPN1RLU = _IpsoVPN1RLU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 132)
)
_IpsoVPN210_ObjectIdentity = ObjectIdentity
ipsoVPN210 = _IpsoVPN210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 133)
)
_IpsoVPN220_ObjectIdentity = ObjectIdentity
ipsoVPN220 = _IpsoVPN220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 134)
)
_IpsoVPN230_ObjectIdentity = ObjectIdentity
ipsoVPN230 = _IpsoVPN230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 135)
)
_IpsoVPN240_ObjectIdentity = ObjectIdentity
ipsoVPN240 = _IpsoVPN240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 2, 1, 136)
)
_IpsoSosSystem_ObjectIdentity = ObjectIdentity
ipsoSosSystem = _IpsoSosSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-IPSO-REGISTRATION-MIB",
    **{"nokia": nokia,
       "nokiaProducts": nokiaProducts,
       "ipsoProducts": ipsoProducts,
       "ipsoProductIds": ipsoProductIds,
       "ipsoAgentID": ipsoAgentID,
       "ipsoIPUnknown": ipsoIPUnknown,
       "ipsoIP4xx": ipsoIP4xx,
       "ipsoIP400": ipsoIP400,
       "ipsoIP410": ipsoIP410,
       "ipsoIP440": ipsoIP440,
       "ipsoIP6xx": ipsoIP6xx,
       "ipsoIP600": ipsoIP600,
       "ipsoIP650": ipsoIP650,
       "ipsoIP3xx": ipsoIP3xx,
       "ipsoIP110": ipsoIP110,
       "ipsoIP530": ipsoIP530,
       "ipsoIP740": ipsoIP740,
       "ipsoIP3400": ipsoIP3400,
       "ipsoVPNUnknown": ipsoVPNUnknown,
       "ipsoVPN1RL50": ipsoVPN1RL50,
       "ipsoVPN1RL250": ipsoVPN1RL250,
       "ipsoVPN1RL500": ipsoVPN1RL500,
       "ipsoVPN1RLU": ipsoVPN1RLU,
       "ipsoVPN210": ipsoVPN210,
       "ipsoVPN220": ipsoVPN220,
       "ipsoVPN230": ipsoVPN230,
       "ipsoVPN240": ipsoVPN240,
       "ipsoSosSystem": ipsoSosSystem}
)
