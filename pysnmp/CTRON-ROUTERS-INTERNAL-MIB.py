# SNMP MIB module (CTRON-ROUTERS-INTERNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ROUTERS-INTERNAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:13 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_Ctron_ObjectIdentity = ObjectIdentity
ctron = _Ctron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1)
)
_CtNetwork_ObjectIdentity = ObjectIdentity
ctNetwork = _CtNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3)
)
_CtronExp_ObjectIdentity = ObjectIdentity
ctronExp = _CtronExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2)
)
_CtronRouterExp_ObjectIdentity = ObjectIdentity
ctronRouterExp = _CtronRouterExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2)
)
_NwRouter_ObjectIdentity = ObjectIdentity
nwRouter = _NwRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2)
)
_NwRtrTemp_ObjectIdentity = ObjectIdentity
nwRtrTemp = _NwRtrTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99)
)
_NwRtrTemp1_ObjectIdentity = ObjectIdentity
nwRtrTemp1 = _NwRtrTemp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2)
)
_NwRtrTemp2_ObjectIdentity = ObjectIdentity
nwRtrTemp2 = _NwRtrTemp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2)
)


class _NwRtrSoftReset_Type(Integer32):
    """Custom type nwRtrSoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_NwRtrSoftReset_Type.__name__ = "Integer32"
_NwRtrSoftReset_Object = MibScalar
nwRtrSoftReset = _NwRtrSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2, 1),
    _NwRtrSoftReset_Type()
)
nwRtrSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwRtrSoftReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ROUTERS-INTERNAL-MIB",
    **{"cabletron": cabletron,
       "mibs": mibs,
       "ctron": ctron,
       "ctNetwork": ctNetwork,
       "ctronExp": ctronExp,
       "ctronRouterExp": ctronRouterExp,
       "nwRouter": nwRouter,
       "nwRtrTemp": nwRtrTemp,
       "nwRtrTemp1": nwRtrTemp1,
       "nwRtrTemp2": nwRtrTemp2,
       "nwRtrSoftReset": nwRtrSoftReset}
)
