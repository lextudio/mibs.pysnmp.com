# SNMP MIB module (HH3C-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FIREWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:24 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cFireWall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFirewallobject_ObjectIdentity = ObjectIdentity
hh3cFirewallobject = _Hh3cFirewallobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1)
)
_Hh3cFirewallSpecs_ObjectIdentity = ObjectIdentity
hh3cFirewallSpecs = _Hh3cFirewallSpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1)
)
_Hh3cFWMaxConnNum_Type = Unsigned32
_Hh3cFWMaxConnNum_Object = MibScalar
hh3cFWMaxConnNum = _Hh3cFWMaxConnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1, 1),
    _Hh3cFWMaxConnNum_Type()
)
hh3cFWMaxConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFWMaxConnNum.setStatus("current")
_Hh3cFirewallGlobalStats_ObjectIdentity = ObjectIdentity
hh3cFirewallGlobalStats = _Hh3cFirewallGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2)
)
_Hh3cFWConnNumCurr_Type = Gauge32
_Hh3cFWConnNumCurr_Object = MibScalar
hh3cFWConnNumCurr = _Hh3cFWConnNumCurr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2, 1),
    _Hh3cFWConnNumCurr_Type()
)
hh3cFWConnNumCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFWConnNumCurr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FIREWALL-MIB",
    **{"hh3cFireWall": hh3cFireWall,
       "hh3cFirewallobject": hh3cFirewallobject,
       "hh3cFirewallSpecs": hh3cFirewallSpecs,
       "hh3cFWMaxConnNum": hh3cFWMaxConnNum,
       "hh3cFirewallGlobalStats": hh3cFirewallGlobalStats,
       "hh3cFWConnNumCurr": hh3cFWConnNumCurr}
)
