# SNMP MIB module (MARVELL-EEE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MARVELL-EEE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:04 2024
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

(ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifOperStatus")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlEee = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 149)
)
rlEee.setRevisions(
        ("2010-05-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlEeeEnable_Type(TruthValue):
    """Custom type rlEeeEnable based on TruthValue"""


_RlEeeEnable_Object = MibScalar
rlEeeEnable = _RlEeeEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 1),
    _RlEeeEnable_Type()
)
rlEeeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEeeEnable.setStatus("current")
_RlEeePortTable_Object = MibTable
rlEeePortTable = _RlEeePortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 2)
)
if mibBuilder.loadTexts:
    rlEeePortTable.setStatus("current")
_RlEeePortEntry_Object = MibTableRow
rlEeePortEntry = _RlEeePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 2, 1)
)
rlEeePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlEeePortEntry.setStatus("current")


class _RlEeePortAdminStatus_Type(TruthValue):
    """Custom type rlEeePortAdminStatus based on TruthValue"""


_RlEeePortAdminStatus_Object = MibTableColumn
rlEeePortAdminStatus = _RlEeePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 2, 1, 1),
    _RlEeePortAdminStatus_Type()
)
rlEeePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEeePortAdminStatus.setStatus("current")


class _RlEeePortSupported_Type(Bits):
    """Custom type rlEeePortSupported based on Bits"""
    namedValues = NamedValues(
        *(("rlEeePortSupported100M", 1),
          ("rlEeePortSupported10G", 3),
          ("rlEeePortSupported10M", 0),
          ("rlEeePortSupported1G", 2))
    )

_RlEeePortSupported_Type.__name__ = "Bits"
_RlEeePortSupported_Object = MibTableColumn
rlEeePortSupported = _RlEeePortSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 2, 1, 2),
    _RlEeePortSupported_Type()
)
rlEeePortSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortSupported.setStatus("current")
_RlEeePortRemoteStatus_Type = TruthValue
_RlEeePortRemoteStatus_Object = MibTableColumn
rlEeePortRemoteStatus = _RlEeePortRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 2, 1, 3),
    _RlEeePortRemoteStatus_Type()
)
rlEeePortRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortRemoteStatus.setStatus("current")
_RlEeePortOperStatus_Type = TruthValue
_RlEeePortOperStatus_Object = MibTableColumn
rlEeePortOperStatus = _RlEeePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 2, 1, 4),
    _RlEeePortOperStatus_Type()
)
rlEeePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortOperStatus.setStatus("current")
_RlEeePortLldpTable_Object = MibTable
rlEeePortLldpTable = _RlEeePortLldpTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 3)
)
if mibBuilder.loadTexts:
    rlEeePortLldpTable.setStatus("current")
_RlEeePortLldpEntry_Object = MibTableRow
rlEeePortLldpEntry = _RlEeePortLldpEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 3, 1)
)
rlEeePortLldpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlEeePortLldpEntry.setStatus("current")


class _RlEeePortLldpAdminStatus_Type(TruthValue):
    """Custom type rlEeePortLldpAdminStatus based on TruthValue"""


_RlEeePortLldpAdminStatus_Object = MibTableColumn
rlEeePortLldpAdminStatus = _RlEeePortLldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 3, 1, 1),
    _RlEeePortLldpAdminStatus_Type()
)
rlEeePortLldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEeePortLldpAdminStatus.setStatus("current")
_RlEeePortLldpOperStatus_Type = TruthValue
_RlEeePortLldpOperStatus_Object = MibTableColumn
rlEeePortLldpOperStatus = _RlEeePortLldpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 3, 1, 2),
    _RlEeePortLldpOperStatus_Type()
)
rlEeePortLldpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpOperStatus.setStatus("current")
_RlEeePortLldpLocalTable_Object = MibTable
rlEeePortLldpLocalTable = _RlEeePortLldpLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4)
)
if mibBuilder.loadTexts:
    rlEeePortLldpLocalTable.setStatus("current")
_RlEeePortLldpLocalEntry_Object = MibTableRow
rlEeePortLldpLocalEntry = _RlEeePortLldpLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4, 1)
)
rlEeePortLldpLocalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlEeePortLldpLocalEntry.setStatus("current")
_RlEeePortLldpLocalResolvedTx_Type = Unsigned32
_RlEeePortLldpLocalResolvedTx_Object = MibTableColumn
rlEeePortLldpLocalResolvedTx = _RlEeePortLldpLocalResolvedTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4, 1, 1),
    _RlEeePortLldpLocalResolvedTx_Type()
)
rlEeePortLldpLocalResolvedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalResolvedTx.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalResolvedTx.setUnits("uSec")
_RlEeePortLldpLocalTx_Type = Unsigned32
_RlEeePortLldpLocalTx_Object = MibTableColumn
rlEeePortLldpLocalTx = _RlEeePortLldpLocalTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4, 1, 2),
    _RlEeePortLldpLocalTx_Type()
)
rlEeePortLldpLocalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalTx.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalTx.setUnits("uSec")
_RlEeePortLldpLocalTxEcho_Type = Unsigned32
_RlEeePortLldpLocalTxEcho_Object = MibTableColumn
rlEeePortLldpLocalTxEcho = _RlEeePortLldpLocalTxEcho_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4, 1, 3),
    _RlEeePortLldpLocalTxEcho_Type()
)
rlEeePortLldpLocalTxEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalTxEcho.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalTxEcho.setUnits("uSec")
_RlEeePortLldpLocalResolvedRx_Type = Unsigned32
_RlEeePortLldpLocalResolvedRx_Object = MibTableColumn
rlEeePortLldpLocalResolvedRx = _RlEeePortLldpLocalResolvedRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4, 1, 4),
    _RlEeePortLldpLocalResolvedRx_Type()
)
rlEeePortLldpLocalResolvedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalResolvedRx.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalResolvedRx.setUnits("uSec")
_RlEeePortLldpLocalRx_Type = Unsigned32
_RlEeePortLldpLocalRx_Object = MibTableColumn
rlEeePortLldpLocalRx = _RlEeePortLldpLocalRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4, 1, 5),
    _RlEeePortLldpLocalRx_Type()
)
rlEeePortLldpLocalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalRx.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalRx.setUnits("uSec")
_RlEeePortLldpLocalRxEcho_Type = Unsigned32
_RlEeePortLldpLocalRxEcho_Object = MibTableColumn
rlEeePortLldpLocalRxEcho = _RlEeePortLldpLocalRxEcho_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 4, 1, 6),
    _RlEeePortLldpLocalRxEcho_Type()
)
rlEeePortLldpLocalRxEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalRxEcho.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpLocalRxEcho.setUnits("uSec")
_RlEeePortLldpRemoteTable_Object = MibTable
rlEeePortLldpRemoteTable = _RlEeePortLldpRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 5)
)
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteTable.setStatus("current")
_RlEeePortLldpRemoteEntry_Object = MibTableRow
rlEeePortLldpRemoteEntry = _RlEeePortLldpRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 5, 1)
)
rlEeePortLldpRemoteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteEntry.setStatus("current")
_RlEeePortLldpRemoteTx_Type = Unsigned32
_RlEeePortLldpRemoteTx_Object = MibTableColumn
rlEeePortLldpRemoteTx = _RlEeePortLldpRemoteTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 5, 1, 1),
    _RlEeePortLldpRemoteTx_Type()
)
rlEeePortLldpRemoteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteTx.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteTx.setUnits("uSec")
_RlEeePortLldpRemoteRx_Type = Unsigned32
_RlEeePortLldpRemoteRx_Object = MibTableColumn
rlEeePortLldpRemoteRx = _RlEeePortLldpRemoteRx_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 5, 1, 2),
    _RlEeePortLldpRemoteRx_Type()
)
rlEeePortLldpRemoteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteRx.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteRx.setUnits("uSec")
_RlEeePortLldpRemoteTxEcho_Type = Unsigned32
_RlEeePortLldpRemoteTxEcho_Object = MibTableColumn
rlEeePortLldpRemoteTxEcho = _RlEeePortLldpRemoteTxEcho_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 5, 1, 3),
    _RlEeePortLldpRemoteTxEcho_Type()
)
rlEeePortLldpRemoteTxEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteTxEcho.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteTxEcho.setUnits("uSec")
_RlEeePortLldpRemoteRxEcho_Type = Unsigned32
_RlEeePortLldpRemoteRxEcho_Object = MibTableColumn
rlEeePortLldpRemoteRxEcho = _RlEeePortLldpRemoteRxEcho_Object(
    (1, 3, 6, 1, 4, 1, 89, 149, 5, 1, 4),
    _RlEeePortLldpRemoteRxEcho_Type()
)
rlEeePortLldpRemoteRxEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteRxEcho.setStatus("current")
if mibBuilder.loadTexts:
    rlEeePortLldpRemoteRxEcho.setUnits("uSec")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MARVELL-EEE-MIB",
    **{"rlEee": rlEee,
       "rlEeeEnable": rlEeeEnable,
       "rlEeePortTable": rlEeePortTable,
       "rlEeePortEntry": rlEeePortEntry,
       "rlEeePortAdminStatus": rlEeePortAdminStatus,
       "rlEeePortSupported": rlEeePortSupported,
       "rlEeePortRemoteStatus": rlEeePortRemoteStatus,
       "rlEeePortOperStatus": rlEeePortOperStatus,
       "rlEeePortLldpTable": rlEeePortLldpTable,
       "rlEeePortLldpEntry": rlEeePortLldpEntry,
       "rlEeePortLldpAdminStatus": rlEeePortLldpAdminStatus,
       "rlEeePortLldpOperStatus": rlEeePortLldpOperStatus,
       "rlEeePortLldpLocalTable": rlEeePortLldpLocalTable,
       "rlEeePortLldpLocalEntry": rlEeePortLldpLocalEntry,
       "rlEeePortLldpLocalResolvedTx": rlEeePortLldpLocalResolvedTx,
       "rlEeePortLldpLocalTx": rlEeePortLldpLocalTx,
       "rlEeePortLldpLocalTxEcho": rlEeePortLldpLocalTxEcho,
       "rlEeePortLldpLocalResolvedRx": rlEeePortLldpLocalResolvedRx,
       "rlEeePortLldpLocalRx": rlEeePortLldpLocalRx,
       "rlEeePortLldpLocalRxEcho": rlEeePortLldpLocalRxEcho,
       "rlEeePortLldpRemoteTable": rlEeePortLldpRemoteTable,
       "rlEeePortLldpRemoteEntry": rlEeePortLldpRemoteEntry,
       "rlEeePortLldpRemoteTx": rlEeePortLldpRemoteTx,
       "rlEeePortLldpRemoteRx": rlEeePortLldpRemoteRx,
       "rlEeePortLldpRemoteTxEcho": rlEeePortLldpRemoteTxEcho,
       "rlEeePortLldpRemoteRxEcho": rlEeePortLldpRemoteRxEcho}
)
