# SNMP MIB module (HM2-PLATFORM-MMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-MMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:14 2024
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

hm2PlatformMMRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1)
)
hm2PlatformMMRP.setRevisions(
        ("2013-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentDot1qMmrp_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMmrp = _Hm2AgentDot1qMmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 1)
)
_Hm2AgentDot1qPortMmrpTable_Object = MibTable
hm2AgentDot1qPortMmrpTable = _Hm2AgentDot1qPortMmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMmrpTable.setStatus("current")
_Hm2AgentDot1qPortMmrpEntry_Object = MibTableRow
hm2AgentDot1qPortMmrpEntry = _Hm2AgentDot1qPortMmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 1, 1, 1)
)
hm2AgentDot1qPortMmrpEntry.setIndexNames(
    (0, "HM2-PLATFORM-MMRP-MIB", "hm2AgentDot1qMmrpPort"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMmrpEntry.setStatus("current")


class _Hm2AgentDot1qMmrpPort_Type(Integer32):
    """Custom type hm2AgentDot1qMmrpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentDot1qMmrpPort_Type.__name__ = "Integer32"
_Hm2AgentDot1qMmrpPort_Object = MibTableColumn
hm2AgentDot1qMmrpPort = _Hm2AgentDot1qMmrpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 1, 1, 1, 1),
    _Hm2AgentDot1qMmrpPort_Type()
)
hm2AgentDot1qMmrpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMmrpPort.setStatus("current")


class _Hm2AgentDot1qPortMmrpMode_Type(EnabledStatus):
    """Custom type hm2AgentDot1qPortMmrpMode based on EnabledStatus"""


_Hm2AgentDot1qPortMmrpMode_Object = MibTableColumn
hm2AgentDot1qPortMmrpMode = _Hm2AgentDot1qPortMmrpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 1, 1, 1, 2),
    _Hm2AgentDot1qPortMmrpMode_Type()
)
hm2AgentDot1qPortMmrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMmrpMode.setStatus("current")


class _Hm2AgentDot1qBridgeMmrpMode_Type(EnabledStatus):
    """Custom type hm2AgentDot1qBridgeMmrpMode based on EnabledStatus"""


_Hm2AgentDot1qBridgeMmrpMode_Object = MibScalar
hm2AgentDot1qBridgeMmrpMode = _Hm2AgentDot1qBridgeMmrpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 1, 2),
    _Hm2AgentDot1qBridgeMmrpMode_Type()
)
hm2AgentDot1qBridgeMmrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMmrpMode.setStatus("current")


class _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type(EnabledStatus):
    """Custom type hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp based on EnabledStatus"""


_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object = MibScalar
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp = _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 1, 3),
    _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type()
)
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp.setStatus("current")
_Hm2AgentDot1qMrpMmrpStats_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMrpMmrpStats = _Hm2AgentDot1qMrpMmrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2)
)
_Hm2AgentDot1qMrpMmrpPktTx_Type = Counter32
_Hm2AgentDot1qMrpMmrpPktTx_Object = MibScalar
hm2AgentDot1qMrpMmrpPktTx = _Hm2AgentDot1qMrpMmrpPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 1),
    _Hm2AgentDot1qMrpMmrpPktTx_Type()
)
hm2AgentDot1qMrpMmrpPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPktTx.setStatus("current")
_Hm2AgentDot1qMrpMmrpPktRx_Type = Counter32
_Hm2AgentDot1qMrpMmrpPktRx_Object = MibScalar
hm2AgentDot1qMrpMmrpPktRx = _Hm2AgentDot1qMrpMmrpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 2),
    _Hm2AgentDot1qMrpMmrpPktRx_Type()
)
hm2AgentDot1qMrpMmrpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPktRx.setStatus("current")
_Hm2AgentDot1qMrpMmrpPktRxBadHeader_Type = Counter32
_Hm2AgentDot1qMrpMmrpPktRxBadHeader_Object = MibScalar
hm2AgentDot1qMrpMmrpPktRxBadHeader = _Hm2AgentDot1qMrpMmrpPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 3),
    _Hm2AgentDot1qMrpMmrpPktRxBadHeader_Type()
)
hm2AgentDot1qMrpMmrpPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPktRxBadHeader.setStatus("current")
_Hm2AgentDot1qMrpMmrpPktRxBadFormat_Type = Counter32
_Hm2AgentDot1qMrpMmrpPktRxBadFormat_Object = MibScalar
hm2AgentDot1qMrpMmrpPktRxBadFormat = _Hm2AgentDot1qMrpMmrpPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 4),
    _Hm2AgentDot1qMrpMmrpPktRxBadFormat_Type()
)
hm2AgentDot1qMrpMmrpPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPktRxBadFormat.setStatus("current")
_Hm2AgentDot1qMrpMmrpPktTxFailure_Type = Counter32
_Hm2AgentDot1qMrpMmrpPktTxFailure_Object = MibScalar
hm2AgentDot1qMrpMmrpPktTxFailure = _Hm2AgentDot1qMrpMmrpPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 5),
    _Hm2AgentDot1qMrpMmrpPktTxFailure_Type()
)
hm2AgentDot1qMrpMmrpPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPktTxFailure.setStatus("current")
_Hm2AgentDot1qMrpMmrpStatsTable_Object = MibTable
hm2AgentDot1qMrpMmrpStatsTable = _Hm2AgentDot1qMrpMmrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpStatsTable.setStatus("current")
_Hm2AgentDot1qMrpMmrpStatsEntry_Object = MibTableRow
hm2AgentDot1qMrpMmrpStatsEntry = _Hm2AgentDot1qMrpMmrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6, 1)
)
hm2AgentDot1qMrpMmrpStatsEntry.setIndexNames(
    (0, "HM2-PLATFORM-MMRP-MIB", "hm2AgentDot1qMrpMmrpIntf"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpStatsEntry.setStatus("current")


class _Hm2AgentDot1qMrpMmrpIntf_Type(Integer32):
    """Custom type hm2AgentDot1qMrpMmrpIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentDot1qMrpMmrpIntf_Type.__name__ = "Integer32"
_Hm2AgentDot1qMrpMmrpIntf_Object = MibTableColumn
hm2AgentDot1qMrpMmrpIntf = _Hm2AgentDot1qMrpMmrpIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6, 1, 1),
    _Hm2AgentDot1qMrpMmrpIntf_Type()
)
hm2AgentDot1qMrpMmrpIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpIntf.setStatus("current")
_Hm2AgentDot1qMrpMmrpPortPktTx_Type = Counter32
_Hm2AgentDot1qMrpMmrpPortPktTx_Object = MibTableColumn
hm2AgentDot1qMrpMmrpPortPktTx = _Hm2AgentDot1qMrpMmrpPortPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6, 1, 2),
    _Hm2AgentDot1qMrpMmrpPortPktTx_Type()
)
hm2AgentDot1qMrpMmrpPortPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPortPktTx.setStatus("current")
_Hm2AgentDot1qMrpMmrpPortPktRx_Type = Counter32
_Hm2AgentDot1qMrpMmrpPortPktRx_Object = MibTableColumn
hm2AgentDot1qMrpMmrpPortPktRx = _Hm2AgentDot1qMrpMmrpPortPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6, 1, 3),
    _Hm2AgentDot1qMrpMmrpPortPktRx_Type()
)
hm2AgentDot1qMrpMmrpPortPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPortPktRx.setStatus("current")
_Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Type = Counter32
_Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Object = MibTableColumn
hm2AgentDot1qMrpMmrpPortPktRxBadHeader = _Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6, 1, 4),
    _Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Type()
)
hm2AgentDot1qMrpMmrpPortPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPortPktRxBadHeader.setStatus("current")
_Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Type = Counter32
_Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Object = MibTableColumn
hm2AgentDot1qMrpMmrpPortPktRxBadFormat = _Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6, 1, 5),
    _Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Type()
)
hm2AgentDot1qMrpMmrpPortPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPortPktRxBadFormat.setStatus("current")
_Hm2AgentDot1qMrpMmrpPortPktTxFailure_Type = Counter32
_Hm2AgentDot1qMrpMmrpPortPktTxFailure_Object = MibTableColumn
hm2AgentDot1qMrpMmrpPortPktTxFailure = _Hm2AgentDot1qMrpMmrpPortPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 6, 1, 6),
    _Hm2AgentDot1qMrpMmrpPortPktTxFailure_Type()
)
hm2AgentDot1qMrpMmrpPortPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpPortPktTxFailure.setStatus("current")
_Hm2AgentDot1qMrpMmrpDynamicAddrCount_Type = Counter32
_Hm2AgentDot1qMrpMmrpDynamicAddrCount_Object = MibScalar
hm2AgentDot1qMrpMmrpDynamicAddrCount = _Hm2AgentDot1qMrpMmrpDynamicAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 1, 2, 248),
    _Hm2AgentDot1qMrpMmrpDynamicAddrCount_Type()
)
hm2AgentDot1qMrpMmrpDynamicAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMmrpDynamicAddrCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-MMRP-MIB",
    **{"hm2PlatformMMRP": hm2PlatformMMRP,
       "hm2AgentDot1qMmrp": hm2AgentDot1qMmrp,
       "hm2AgentDot1qPortMmrpTable": hm2AgentDot1qPortMmrpTable,
       "hm2AgentDot1qPortMmrpEntry": hm2AgentDot1qPortMmrpEntry,
       "hm2AgentDot1qMmrpPort": hm2AgentDot1qMmrpPort,
       "hm2AgentDot1qPortMmrpMode": hm2AgentDot1qPortMmrpMode,
       "hm2AgentDot1qBridgeMmrpMode": hm2AgentDot1qBridgeMmrpMode,
       "hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp": hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp,
       "hm2AgentDot1qMrpMmrpStats": hm2AgentDot1qMrpMmrpStats,
       "hm2AgentDot1qMrpMmrpPktTx": hm2AgentDot1qMrpMmrpPktTx,
       "hm2AgentDot1qMrpMmrpPktRx": hm2AgentDot1qMrpMmrpPktRx,
       "hm2AgentDot1qMrpMmrpPktRxBadHeader": hm2AgentDot1qMrpMmrpPktRxBadHeader,
       "hm2AgentDot1qMrpMmrpPktRxBadFormat": hm2AgentDot1qMrpMmrpPktRxBadFormat,
       "hm2AgentDot1qMrpMmrpPktTxFailure": hm2AgentDot1qMrpMmrpPktTxFailure,
       "hm2AgentDot1qMrpMmrpStatsTable": hm2AgentDot1qMrpMmrpStatsTable,
       "hm2AgentDot1qMrpMmrpStatsEntry": hm2AgentDot1qMrpMmrpStatsEntry,
       "hm2AgentDot1qMrpMmrpIntf": hm2AgentDot1qMrpMmrpIntf,
       "hm2AgentDot1qMrpMmrpPortPktTx": hm2AgentDot1qMrpMmrpPortPktTx,
       "hm2AgentDot1qMrpMmrpPortPktRx": hm2AgentDot1qMrpMmrpPortPktRx,
       "hm2AgentDot1qMrpMmrpPortPktRxBadHeader": hm2AgentDot1qMrpMmrpPortPktRxBadHeader,
       "hm2AgentDot1qMrpMmrpPortPktRxBadFormat": hm2AgentDot1qMrpMmrpPortPktRxBadFormat,
       "hm2AgentDot1qMrpMmrpPortPktTxFailure": hm2AgentDot1qMrpMmrpPortPktTxFailure,
       "hm2AgentDot1qMrpMmrpDynamicAddrCount": hm2AgentDot1qMrpMmrpDynamicAddrCount}
)
