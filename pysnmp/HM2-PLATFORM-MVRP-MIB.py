# SNMP MIB module (HM2-PLATFORM-MVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-MVRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:18 2024
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

(hm2AgentDot1qMrpMxrp,) = mibBuilder.importSymbols(
    "HM2-PLATFORM-MRP-MIB",
    "hm2AgentDot1qMrpMxrp")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

hm2PlatformMVRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2)
)
hm2PlatformMVRP.setRevisions(
        ("2013-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentDot1qMvrp_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMvrp = _Hm2AgentDot1qMvrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 1)
)
_Hm2AgentDot1qPortMvrpTable_Object = MibTable
hm2AgentDot1qPortMvrpTable = _Hm2AgentDot1qPortMvrpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMvrpTable.setStatus("current")
_Hm2AgentDot1qPortMvrpEntry_Object = MibTableRow
hm2AgentDot1qPortMvrpEntry = _Hm2AgentDot1qPortMvrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 1, 1, 1)
)
hm2AgentDot1qPortMvrpEntry.setIndexNames(
    (0, "HM2-PLATFORM-MVRP-MIB", "hm2AgentDot1qMvrpPort"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMvrpEntry.setStatus("current")


class _Hm2AgentDot1qMvrpPort_Type(Integer32):
    """Custom type hm2AgentDot1qMvrpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentDot1qMvrpPort_Type.__name__ = "Integer32"
_Hm2AgentDot1qMvrpPort_Object = MibTableColumn
hm2AgentDot1qMvrpPort = _Hm2AgentDot1qMvrpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 1, 1, 1, 1),
    _Hm2AgentDot1qMvrpPort_Type()
)
hm2AgentDot1qMvrpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMvrpPort.setStatus("current")


class _Hm2AgentDot1qPortMvrpMode_Type(EnabledStatus):
    """Custom type hm2AgentDot1qPortMvrpMode based on EnabledStatus"""


_Hm2AgentDot1qPortMvrpMode_Object = MibTableColumn
hm2AgentDot1qPortMvrpMode = _Hm2AgentDot1qPortMvrpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 1, 1, 1, 10),
    _Hm2AgentDot1qPortMvrpMode_Type()
)
hm2AgentDot1qPortMvrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMvrpMode.setStatus("current")


class _Hm2AgentDot1qBridgeMvrpMode_Type(EnabledStatus):
    """Custom type hm2AgentDot1qBridgeMvrpMode based on EnabledStatus"""


_Hm2AgentDot1qBridgeMvrpMode_Object = MibScalar
hm2AgentDot1qBridgeMvrpMode = _Hm2AgentDot1qBridgeMvrpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 1, 2),
    _Hm2AgentDot1qBridgeMvrpMode_Type()
)
hm2AgentDot1qBridgeMvrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMvrpMode.setStatus("current")


class _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type(EnabledStatus):
    """Custom type hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp based on EnabledStatus"""


_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object = MibScalar
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp = _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 1, 3),
    _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type()
)
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp.setStatus("current")
_Hm2AgentDot1qMrpMvrpStats_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMrpMvrpStats = _Hm2AgentDot1qMrpMvrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2)
)
_Hm2AgentDot1qMrpMvrpPktTx_Type = Counter32
_Hm2AgentDot1qMrpMvrpPktTx_Object = MibScalar
hm2AgentDot1qMrpMvrpPktTx = _Hm2AgentDot1qMrpMvrpPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 1),
    _Hm2AgentDot1qMrpMvrpPktTx_Type()
)
hm2AgentDot1qMrpMvrpPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPktTx.setStatus("current")
_Hm2AgentDot1qMrpMvrpPktRx_Type = Counter32
_Hm2AgentDot1qMrpMvrpPktRx_Object = MibScalar
hm2AgentDot1qMrpMvrpPktRx = _Hm2AgentDot1qMrpMvrpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 2),
    _Hm2AgentDot1qMrpMvrpPktRx_Type()
)
hm2AgentDot1qMrpMvrpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPktRx.setStatus("current")
_Hm2AgentDot1qMrpMvrpPktRxBadHeader_Type = Counter32
_Hm2AgentDot1qMrpMvrpPktRxBadHeader_Object = MibScalar
hm2AgentDot1qMrpMvrpPktRxBadHeader = _Hm2AgentDot1qMrpMvrpPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 3),
    _Hm2AgentDot1qMrpMvrpPktRxBadHeader_Type()
)
hm2AgentDot1qMrpMvrpPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPktRxBadHeader.setStatus("current")
_Hm2AgentDot1qMrpMvrpPktRxBadFormat_Type = Counter32
_Hm2AgentDot1qMrpMvrpPktRxBadFormat_Object = MibScalar
hm2AgentDot1qMrpMvrpPktRxBadFormat = _Hm2AgentDot1qMrpMvrpPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 4),
    _Hm2AgentDot1qMrpMvrpPktRxBadFormat_Type()
)
hm2AgentDot1qMrpMvrpPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPktRxBadFormat.setStatus("current")
_Hm2AgentDot1qMrpMvrpPktTxFailure_Type = Counter32
_Hm2AgentDot1qMrpMvrpPktTxFailure_Object = MibScalar
hm2AgentDot1qMrpMvrpPktTxFailure = _Hm2AgentDot1qMrpMvrpPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 5),
    _Hm2AgentDot1qMrpMvrpPktTxFailure_Type()
)
hm2AgentDot1qMrpMvrpPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPktTxFailure.setStatus("current")
_Hm2AgentDot1qMrpMvrpStatsTable_Object = MibTable
hm2AgentDot1qMrpMvrpStatsTable = _Hm2AgentDot1qMrpMvrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpStatsTable.setStatus("current")
_Hm2AgentDot1qMrpMvrpStatsEntry_Object = MibTableRow
hm2AgentDot1qMrpMvrpStatsEntry = _Hm2AgentDot1qMrpMvrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1)
)
hm2AgentDot1qMrpMvrpStatsEntry.setIndexNames(
    (0, "HM2-PLATFORM-MVRP-MIB", "hm2AgentDot1qMrpMvrpIntf"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpStatsEntry.setStatus("current")


class _Hm2AgentDot1qMrpMvrpIntf_Type(Integer32):
    """Custom type hm2AgentDot1qMrpMvrpIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentDot1qMrpMvrpIntf_Type.__name__ = "Integer32"
_Hm2AgentDot1qMrpMvrpIntf_Object = MibTableColumn
hm2AgentDot1qMrpMvrpIntf = _Hm2AgentDot1qMrpMvrpIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1, 1),
    _Hm2AgentDot1qMrpMvrpIntf_Type()
)
hm2AgentDot1qMrpMvrpIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpIntf.setStatus("current")
_Hm2AgentDot1qMrpMvrpPortPktTx_Type = Counter32
_Hm2AgentDot1qMrpMvrpPortPktTx_Object = MibTableColumn
hm2AgentDot1qMrpMvrpPortPktTx = _Hm2AgentDot1qMrpMvrpPortPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1, 2),
    _Hm2AgentDot1qMrpMvrpPortPktTx_Type()
)
hm2AgentDot1qMrpMvrpPortPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPortPktTx.setStatus("current")
_Hm2AgentDot1qMrpMvrpPortPktRx_Type = Counter32
_Hm2AgentDot1qMrpMvrpPortPktRx_Object = MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRx = _Hm2AgentDot1qMrpMvrpPortPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1, 3),
    _Hm2AgentDot1qMrpMvrpPortPktRx_Type()
)
hm2AgentDot1qMrpMvrpPortPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPortPktRx.setStatus("current")
_Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Type = Counter32
_Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Object = MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRxBadHeader = _Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1, 4),
    _Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Type()
)
hm2AgentDot1qMrpMvrpPortPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPortPktRxBadHeader.setStatus("current")
_Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Type = Counter32
_Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Object = MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRxBadFormat = _Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1, 5),
    _Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Type()
)
hm2AgentDot1qMrpMvrpPortPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPortPktRxBadFormat.setStatus("current")
_Hm2AgentDot1qMrpMvrpPortPktTxFailure_Type = Counter32
_Hm2AgentDot1qMrpMvrpPortPktTxFailure_Object = MibTableColumn
hm2AgentDot1qMrpMvrpPortPktTxFailure = _Hm2AgentDot1qMrpMvrpPortPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1, 6),
    _Hm2AgentDot1qMrpMvrpPortPktTxFailure_Type()
)
hm2AgentDot1qMrpMvrpPortPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPortPktTxFailure.setStatus("current")
_Hm2AgentDot1qMrpMvrpPortPktRegFailure_Type = Counter32
_Hm2AgentDot1qMrpMvrpPortPktRegFailure_Object = MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRegFailure = _Hm2AgentDot1qMrpMvrpPortPktRegFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 6, 1, 7),
    _Hm2AgentDot1qMrpMvrpPortPktRegFailure_Type()
)
hm2AgentDot1qMrpMvrpPortPktRegFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPortPktRegFailure.setStatus("current")
_Hm2AgentDot1qMrpMvrpPktMessageFailure_Type = Counter32
_Hm2AgentDot1qMrpMvrpPktMessageFailure_Object = MibScalar
hm2AgentDot1qMrpMvrpPktMessageFailure = _Hm2AgentDot1qMrpMvrpPktMessageFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 2, 2, 7),
    _Hm2AgentDot1qMrpMvrpPktMessageFailure_Type()
)
hm2AgentDot1qMrpMvrpPktMessageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMvrpPktMessageFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-MVRP-MIB",
    **{"hm2PlatformMVRP": hm2PlatformMVRP,
       "hm2AgentDot1qMvrp": hm2AgentDot1qMvrp,
       "hm2AgentDot1qPortMvrpTable": hm2AgentDot1qPortMvrpTable,
       "hm2AgentDot1qPortMvrpEntry": hm2AgentDot1qPortMvrpEntry,
       "hm2AgentDot1qMvrpPort": hm2AgentDot1qMvrpPort,
       "hm2AgentDot1qPortMvrpMode": hm2AgentDot1qPortMvrpMode,
       "hm2AgentDot1qBridgeMvrpMode": hm2AgentDot1qBridgeMvrpMode,
       "hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp": hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp,
       "hm2AgentDot1qMrpMvrpStats": hm2AgentDot1qMrpMvrpStats,
       "hm2AgentDot1qMrpMvrpPktTx": hm2AgentDot1qMrpMvrpPktTx,
       "hm2AgentDot1qMrpMvrpPktRx": hm2AgentDot1qMrpMvrpPktRx,
       "hm2AgentDot1qMrpMvrpPktRxBadHeader": hm2AgentDot1qMrpMvrpPktRxBadHeader,
       "hm2AgentDot1qMrpMvrpPktRxBadFormat": hm2AgentDot1qMrpMvrpPktRxBadFormat,
       "hm2AgentDot1qMrpMvrpPktTxFailure": hm2AgentDot1qMrpMvrpPktTxFailure,
       "hm2AgentDot1qMrpMvrpStatsTable": hm2AgentDot1qMrpMvrpStatsTable,
       "hm2AgentDot1qMrpMvrpStatsEntry": hm2AgentDot1qMrpMvrpStatsEntry,
       "hm2AgentDot1qMrpMvrpIntf": hm2AgentDot1qMrpMvrpIntf,
       "hm2AgentDot1qMrpMvrpPortPktTx": hm2AgentDot1qMrpMvrpPortPktTx,
       "hm2AgentDot1qMrpMvrpPortPktRx": hm2AgentDot1qMrpMvrpPortPktRx,
       "hm2AgentDot1qMrpMvrpPortPktRxBadHeader": hm2AgentDot1qMrpMvrpPortPktRxBadHeader,
       "hm2AgentDot1qMrpMvrpPortPktRxBadFormat": hm2AgentDot1qMrpMvrpPortPktRxBadFormat,
       "hm2AgentDot1qMrpMvrpPortPktTxFailure": hm2AgentDot1qMrpMvrpPortPktTxFailure,
       "hm2AgentDot1qMrpMvrpPortPktRegFailure": hm2AgentDot1qMrpMvrpPortPktRegFailure,
       "hm2AgentDot1qMrpMvrpPktMessageFailure": hm2AgentDot1qMrpMvrpPktMessageFailure}
)
