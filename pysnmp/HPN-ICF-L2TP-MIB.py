# SNMP MIB module (HPN-ICF-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:42 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfL2tp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139)
)
hpnicfL2tp.setRevisions(
        ("2013-07-05 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfL2tpObjects_ObjectIdentity = ObjectIdentity
hpnicfL2tpObjects = _HpnicfL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1)
)
_HpnicfL2tpScalar_ObjectIdentity = ObjectIdentity
hpnicfL2tpScalar = _HpnicfL2tpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1)
)
_HpnicfL2tpStats_ObjectIdentity = ObjectIdentity
hpnicfL2tpStats = _HpnicfL2tpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1)
)
_HpnicfL2tpStatsTotalTunnels_Type = Counter32
_HpnicfL2tpStatsTotalTunnels_Object = MibScalar
hpnicfL2tpStatsTotalTunnels = _HpnicfL2tpStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 1),
    _HpnicfL2tpStatsTotalTunnels_Type()
)
hpnicfL2tpStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL2tpStatsTotalTunnels.setStatus("current")
_HpnicfL2tpStatsTotalSessions_Type = Counter32
_HpnicfL2tpStatsTotalSessions_Object = MibScalar
hpnicfL2tpStatsTotalSessions = _HpnicfL2tpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 2),
    _HpnicfL2tpStatsTotalSessions_Type()
)
hpnicfL2tpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL2tpStatsTotalSessions.setStatus("current")
_HpnicfL2tpSessionRate_Type = Integer32
_HpnicfL2tpSessionRate_Object = MibScalar
hpnicfL2tpSessionRate = _HpnicfL2tpSessionRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 3),
    _HpnicfL2tpSessionRate_Type()
)
hpnicfL2tpSessionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL2tpSessionRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-L2TP-MIB",
    **{"hpnicfL2tp": hpnicfL2tp,
       "hpnicfL2tpObjects": hpnicfL2tpObjects,
       "hpnicfL2tpScalar": hpnicfL2tpScalar,
       "hpnicfL2tpStats": hpnicfL2tpStats,
       "hpnicfL2tpStatsTotalTunnels": hpnicfL2tpStatsTotalTunnels,
       "hpnicfL2tpStatsTotalSessions": hpnicfL2tpStatsTotalSessions,
       "hpnicfL2tpSessionRate": hpnicfL2tpSessionRate}
)
