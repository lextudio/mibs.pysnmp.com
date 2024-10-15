# SNMP MIB module (BTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BTI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:51 2024
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

btiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 1, 1)
)
btiMib.setRevisions(
        ("2012-11-30 12:00",
         "2012-03-09 12:00",
         "2012-02-10 12:00",
         "2011-09-26 12:00",
         "2008-05-30 12:00",
         "2007-08-27 12:00",
         "2005-07-25 12:00",
         "2004-09-23 12:00",
         "2003-12-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BtiSystems_ObjectIdentity = ObjectIdentity
btiSystems = _BtiSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070)
)
_BtiModules_ObjectIdentity = ObjectIdentity
btiModules = _BtiModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 1)
)
_BtiProducts_ObjectIdentity = ObjectIdentity
btiProducts = _BtiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2)
)
_Bti7000_ObjectIdentity = ObjectIdentity
bti7000 = _Bti7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 2)
)
_Btiems_ObjectIdentity = ObjectIdentity
btiems = _Btiems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 4)
)
_BtiPSM_ObjectIdentity = ObjectIdentity
btiPSM = _BtiPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 6)
)
_WidecastCache_ObjectIdentity = ObjectIdentity
widecastCache = _WidecastCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 7)
)
_Bti800_ObjectIdentity = ObjectIdentity
bti800 = _Bti800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 8)
)
_Bti7800_ObjectIdentity = ObjectIdentity
bti7800 = _Bti7800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI-MIB",
    **{"btiSystems": btiSystems,
       "btiModules": btiModules,
       "btiMib": btiMib,
       "btiProducts": btiProducts,
       "bti7000": bti7000,
       "btiems": btiems,
       "btiPSM": btiPSM,
       "widecastCache": widecastCache,
       "bti800": bti800,
       "bti7800": bti7800}
)
