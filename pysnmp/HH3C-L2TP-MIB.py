# SNMP MIB module (HH3C-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:43 2024
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

hh3cL2tp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139)
)
hh3cL2tp.setRevisions(
        ("2013-07-05 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cL2tpObjects_ObjectIdentity = ObjectIdentity
hh3cL2tpObjects = _Hh3cL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1)
)
_Hh3cL2tpScalar_ObjectIdentity = ObjectIdentity
hh3cL2tpScalar = _Hh3cL2tpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1)
)
_Hh3cL2tpStats_ObjectIdentity = ObjectIdentity
hh3cL2tpStats = _Hh3cL2tpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1)
)
_Hh3cL2tpStatsTotalTunnels_Type = Counter32
_Hh3cL2tpStatsTotalTunnels_Object = MibScalar
hh3cL2tpStatsTotalTunnels = _Hh3cL2tpStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 1),
    _Hh3cL2tpStatsTotalTunnels_Type()
)
hh3cL2tpStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsTotalTunnels.setStatus("current")
_Hh3cL2tpStatsTotalSessions_Type = Counter32
_Hh3cL2tpStatsTotalSessions_Object = MibScalar
hh3cL2tpStatsTotalSessions = _Hh3cL2tpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 2),
    _Hh3cL2tpStatsTotalSessions_Type()
)
hh3cL2tpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpStatsTotalSessions.setStatus("current")
_Hh3cL2tpSessionRate_Type = Integer32
_Hh3cL2tpSessionRate_Object = MibScalar
hh3cL2tpSessionRate = _Hh3cL2tpSessionRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139, 1, 1, 1, 3),
    _Hh3cL2tpSessionRate_Type()
)
hh3cL2tpSessionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL2tpSessionRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-L2TP-MIB",
    **{"hh3cL2tp": hh3cL2tp,
       "hh3cL2tpObjects": hh3cL2tpObjects,
       "hh3cL2tpScalar": hh3cL2tpScalar,
       "hh3cL2tpStats": hh3cL2tpStats,
       "hh3cL2tpStatsTotalTunnels": hh3cL2tpStatsTotalTunnels,
       "hh3cL2tpStatsTotalSessions": hh3cL2tpStatsTotalSessions,
       "hh3cL2tpSessionRate": hh3cL2tpSessionRate}
)
