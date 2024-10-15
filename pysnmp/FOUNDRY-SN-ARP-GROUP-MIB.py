# SNMP MIB module (FOUNDRY-SN-ARP-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-ARP-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:51 2024
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snSwitch")

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

snArpInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22)
)
snArpInfo.setRevisions(
        ("2010-06-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnArpStats_ObjectIdentity = ObjectIdentity
snArpStats = _SnArpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1)
)
_SnArpStatsTotalReceived_Type = Counter32
_SnArpStatsTotalReceived_Object = MibScalar
snArpStatsTotalReceived = _SnArpStatsTotalReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 1),
    _SnArpStatsTotalReceived_Type()
)
snArpStatsTotalReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snArpStatsTotalReceived.setStatus("current")
_SnArpStatsRequestReceived_Type = Counter32
_SnArpStatsRequestReceived_Object = MibScalar
snArpStatsRequestReceived = _SnArpStatsRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 2),
    _SnArpStatsRequestReceived_Type()
)
snArpStatsRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snArpStatsRequestReceived.setStatus("current")
_SnArpStatsRequestSent_Type = Counter32
_SnArpStatsRequestSent_Object = MibScalar
snArpStatsRequestSent = _SnArpStatsRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 3),
    _SnArpStatsRequestSent_Type()
)
snArpStatsRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snArpStatsRequestSent.setStatus("current")
_SnArpStatsRepliesSent_Type = Counter32
_SnArpStatsRepliesSent_Object = MibScalar
snArpStatsRepliesSent = _SnArpStatsRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 4),
    _SnArpStatsRepliesSent_Type()
)
snArpStatsRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snArpStatsRepliesSent.setStatus("current")
_SnArpStatsPendingDrop_Type = Counter32
_SnArpStatsPendingDrop_Object = MibScalar
snArpStatsPendingDrop = _SnArpStatsPendingDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 5),
    _SnArpStatsPendingDrop_Type()
)
snArpStatsPendingDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snArpStatsPendingDrop.setStatus("current")
_SnArpStatsInvalidSource_Type = Counter32
_SnArpStatsInvalidSource_Object = MibScalar
snArpStatsInvalidSource = _SnArpStatsInvalidSource_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 6),
    _SnArpStatsInvalidSource_Type()
)
snArpStatsInvalidSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snArpStatsInvalidSource.setStatus("current")
_SnArpStatsInvalidDestination_Type = Counter32
_SnArpStatsInvalidDestination_Object = MibScalar
snArpStatsInvalidDestination = _SnArpStatsInvalidDestination_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22, 1, 7),
    _SnArpStatsInvalidDestination_Type()
)
snArpStatsInvalidDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snArpStatsInvalidDestination.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-ARP-GROUP-MIB",
    **{"snArpInfo": snArpInfo,
       "snArpStats": snArpStats,
       "snArpStatsTotalReceived": snArpStatsTotalReceived,
       "snArpStatsRequestReceived": snArpStatsRequestReceived,
       "snArpStatsRequestSent": snArpStatsRequestSent,
       "snArpStatsRepliesSent": snArpStatsRepliesSent,
       "snArpStatsPendingDrop": snArpStatsPendingDrop,
       "snArpStatsInvalidSource": snArpStatsInvalidSource,
       "snArpStatsInvalidDestination": snArpStatsInvalidDestination}
)
