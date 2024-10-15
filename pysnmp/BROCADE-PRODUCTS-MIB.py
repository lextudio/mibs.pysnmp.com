# SNMP MIB module (BROCADE-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:29 2024
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

(bcsiReg,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiReg")

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

brocadeProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3)
)
brocadeProductsMIB.setRevisions(
        ("2012-02-03 00:00",
         "2013-11-21 00:00",
         "2013-09-25 13:00",
         "2014-10-07 14:05",
         "2015-08-11 13:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrocadeProducts_ObjectIdentity = ObjectIdentity
brocadeProducts = _BrocadeProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1)
)
_Vdx6740_ObjectIdentity = ObjectIdentity
vdx6740 = _Vdx6740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 131)
)
_Vdx6740T_ObjectIdentity = ObjectIdentity
vdx6740T = _Vdx6740T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 137)
)
_Vdx2740_ObjectIdentity = ObjectIdentity
vdx2740 = _Vdx2740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 138)
)
_Vdx6740T1G_ObjectIdentity = ObjectIdentity
vdx6740T1G = _Vdx6740T1G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 151)
)
_Vdx6940Q36_ObjectIdentity = ObjectIdentity
vdx6940Q36 = _Vdx6940Q36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 153)
)
_Vdx6940S144_ObjectIdentity = ObjectIdentity
vdx6940S144 = _Vdx6940S144_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 164)
)
_Vdx8770S4_ObjectIdentity = ObjectIdentity
vdx8770S4 = _Vdx8770S4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1000)
)
_Vdx8770S8_ObjectIdentity = ObjectIdentity
vdx8770S8 = _Vdx8770S8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1001)
)
_Vdx8770S16_ObjectIdentity = ObjectIdentity
vdx8770S16 = _Vdx8770S16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1002)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-PRODUCTS-MIB",
    **{"brocadeProductsMIB": brocadeProductsMIB,
       "brocadeProducts": brocadeProducts,
       "vdx6740": vdx6740,
       "vdx6740T": vdx6740T,
       "vdx2740": vdx2740,
       "vdx6740T1G": vdx6740T1G,
       "vdx6940Q36": vdx6940Q36,
       "vdx6940S144": vdx6940S144,
       "vdx8770S4": vdx8770S4,
       "vdx8770S8": vdx8770S8,
       "vdx8770S16": vdx8770S16}
)
