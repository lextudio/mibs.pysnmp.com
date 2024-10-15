# SNMP MIB module (DLINK-3100-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:23 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

rlStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141)
)
rlStatistics.setRevisions(
        ("2007-11-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlStatisticsPacketTable_Object = MibTable
rlStatisticsPacketTable = _RlStatisticsPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1)
)
if mibBuilder.loadTexts:
    rlStatisticsPacketTable.setStatus("current")
_RlStatisticsPacketEntry_Object = MibTableRow
rlStatisticsPacketEntry = _RlStatisticsPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1)
)
rlStatisticsPacketEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlStatisticsPacketEntry.setStatus("current")
_RlStatisticsPacket64Octets_Type = Counter32
_RlStatisticsPacket64Octets_Object = MibTableColumn
rlStatisticsPacket64Octets = _RlStatisticsPacket64Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 1),
    _RlStatisticsPacket64Octets_Type()
)
rlStatisticsPacket64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacket64Octets.setStatus("current")
_RlStatisticsPacket65to127Octets_Type = Counter32
_RlStatisticsPacket65to127Octets_Object = MibTableColumn
rlStatisticsPacket65to127Octets = _RlStatisticsPacket65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 2),
    _RlStatisticsPacket65to127Octets_Type()
)
rlStatisticsPacket65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacket65to127Octets.setStatus("current")
_RlStatisticsPacket128to255Octets_Type = Counter32
_RlStatisticsPacket128to255Octets_Object = MibTableColumn
rlStatisticsPacket128to255Octets = _RlStatisticsPacket128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 3),
    _RlStatisticsPacket128to255Octets_Type()
)
rlStatisticsPacket128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacket128to255Octets.setStatus("current")
_RlStatisticsPacket256to511Octets_Type = Counter32
_RlStatisticsPacket256to511Octets_Object = MibTableColumn
rlStatisticsPacket256to511Octets = _RlStatisticsPacket256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 4),
    _RlStatisticsPacket256to511Octets_Type()
)
rlStatisticsPacket256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacket256to511Octets.setStatus("current")
_RlStatisticsPacket512to1023Octets_Type = Counter32
_RlStatisticsPacket512to1023Octets_Object = MibTableColumn
rlStatisticsPacket512to1023Octets = _RlStatisticsPacket512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 5),
    _RlStatisticsPacket512to1023Octets_Type()
)
rlStatisticsPacket512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacket512to1023Octets.setStatus("current")
_RlStatisticsPacket1024to1518Octets_Type = Counter32
_RlStatisticsPacket1024to1518Octets_Object = MibTableColumn
rlStatisticsPacket1024to1518Octets = _RlStatisticsPacket1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 6),
    _RlStatisticsPacket1024to1518Octets_Type()
)
rlStatisticsPacket1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacket1024to1518Octets.setStatus("current")
_RlStatisticsPacketOversizePkts_Type = Counter32
_RlStatisticsPacketOversizePkts_Object = MibTableColumn
rlStatisticsPacketOversizePkts = _RlStatisticsPacketOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 7),
    _RlStatisticsPacketOversizePkts_Type()
)
rlStatisticsPacketOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketOversizePkts.setStatus("current")
_RlStatisticsPacketUnicastRx_Type = Counter32
_RlStatisticsPacketUnicastRx_Object = MibTableColumn
rlStatisticsPacketUnicastRx = _RlStatisticsPacketUnicastRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 8),
    _RlStatisticsPacketUnicastRx_Type()
)
rlStatisticsPacketUnicastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketUnicastRx.setStatus("current")
_RlStatisticsPacketMulticastRx_Type = Counter32
_RlStatisticsPacketMulticastRx_Object = MibTableColumn
rlStatisticsPacketMulticastRx = _RlStatisticsPacketMulticastRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 9),
    _RlStatisticsPacketMulticastRx_Type()
)
rlStatisticsPacketMulticastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketMulticastRx.setStatus("current")
_RlStatisticsPacketBroadcastRx_Type = Counter32
_RlStatisticsPacketBroadcastRx_Object = MibTableColumn
rlStatisticsPacketBroadcastRx = _RlStatisticsPacketBroadcastRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 10),
    _RlStatisticsPacketBroadcastRx_Type()
)
rlStatisticsPacketBroadcastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketBroadcastRx.setStatus("current")
_RlStatisticsPacketRxBytes_Type = Counter32
_RlStatisticsPacketRxBytes_Object = MibTableColumn
rlStatisticsPacketRxBytes = _RlStatisticsPacketRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 11),
    _RlStatisticsPacketRxBytes_Type()
)
rlStatisticsPacketRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketRxBytes.setStatus("current")
_RlStatisticsPacketRxFrames_Type = Counter32
_RlStatisticsPacketRxFrames_Object = MibTableColumn
rlStatisticsPacketRxFrames = _RlStatisticsPacketRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 12),
    _RlStatisticsPacketRxFrames_Type()
)
rlStatisticsPacketRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketRxFrames.setStatus("current")
_RlStatisticsPacketTxBytes_Type = Counter32
_RlStatisticsPacketTxBytes_Object = MibTableColumn
rlStatisticsPacketTxBytes = _RlStatisticsPacketTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 13),
    _RlStatisticsPacketTxBytes_Type()
)
rlStatisticsPacketTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketTxBytes.setStatus("current")
_RlStatisticsPacketTxFrames_Type = Counter32
_RlStatisticsPacketTxFrames_Object = MibTableColumn
rlStatisticsPacketTxFrames = _RlStatisticsPacketTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 1, 1, 14),
    _RlStatisticsPacketTxFrames_Type()
)
rlStatisticsPacketTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPacketTxFrames.setStatus("current")
_RlStatisticsPortTable_Object = MibTable
rlStatisticsPortTable = _RlStatisticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2)
)
if mibBuilder.loadTexts:
    rlStatisticsPortTable.setStatus("current")
_RlStatisticsPortEntry_Object = MibTableRow
rlStatisticsPortEntry = _RlStatisticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1)
)
rlStatisticsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlStatisticsPortEntry.setStatus("current")
_RlStatisticsPortRx_Type = Counter32
_RlStatisticsPortRx_Object = MibTableColumn
rlStatisticsPortRx = _RlStatisticsPortRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1, 1),
    _RlStatisticsPortRx_Type()
)
rlStatisticsPortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPortRx.setStatus("current")
_RlStatisticsPortTx_Type = Counter32
_RlStatisticsPortTx_Object = MibTableColumn
rlStatisticsPortTx = _RlStatisticsPortTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1, 2),
    _RlStatisticsPortTx_Type()
)
rlStatisticsPortTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPortTx.setStatus("current")


class _RlStatisticsPortUtilization_Type(Integer32):
    """Custom type rlStatisticsPortUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RlStatisticsPortUtilization_Type.__name__ = "Integer32"
_RlStatisticsPortUtilization_Object = MibTableColumn
rlStatisticsPortUtilization = _RlStatisticsPortUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 141, 2, 1, 3),
    _RlStatisticsPortUtilization_Type()
)
rlStatisticsPortUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStatisticsPortUtilization.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-STATISTICS-MIB",
    **{"rlStatistics": rlStatistics,
       "rlStatisticsPacketTable": rlStatisticsPacketTable,
       "rlStatisticsPacketEntry": rlStatisticsPacketEntry,
       "rlStatisticsPacket64Octets": rlStatisticsPacket64Octets,
       "rlStatisticsPacket65to127Octets": rlStatisticsPacket65to127Octets,
       "rlStatisticsPacket128to255Octets": rlStatisticsPacket128to255Octets,
       "rlStatisticsPacket256to511Octets": rlStatisticsPacket256to511Octets,
       "rlStatisticsPacket512to1023Octets": rlStatisticsPacket512to1023Octets,
       "rlStatisticsPacket1024to1518Octets": rlStatisticsPacket1024to1518Octets,
       "rlStatisticsPacketOversizePkts": rlStatisticsPacketOversizePkts,
       "rlStatisticsPacketUnicastRx": rlStatisticsPacketUnicastRx,
       "rlStatisticsPacketMulticastRx": rlStatisticsPacketMulticastRx,
       "rlStatisticsPacketBroadcastRx": rlStatisticsPacketBroadcastRx,
       "rlStatisticsPacketRxBytes": rlStatisticsPacketRxBytes,
       "rlStatisticsPacketRxFrames": rlStatisticsPacketRxFrames,
       "rlStatisticsPacketTxBytes": rlStatisticsPacketTxBytes,
       "rlStatisticsPacketTxFrames": rlStatisticsPacketTxFrames,
       "rlStatisticsPortTable": rlStatisticsPortTable,
       "rlStatisticsPortEntry": rlStatisticsPortEntry,
       "rlStatisticsPortRx": rlStatisticsPortRx,
       "rlStatisticsPortTx": rlStatisticsPortTx,
       "rlStatisticsPortUtilization": rlStatisticsPortUtilization}
)
