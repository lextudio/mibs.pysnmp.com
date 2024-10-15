# SNMP MIB module (JUNIPER-Services-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-Services-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:18 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

jnxServicesInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27)
)
jnxServicesInfoMib.setRevisions(
        ("2004-01-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxSvcFlowTableAggStatsTable_Object = MibTable
jnxSvcFlowTableAggStatsTable = _JnxSvcFlowTableAggStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1)
)
if mibBuilder.loadTexts:
    jnxSvcFlowTableAggStatsTable.setStatus("current")
_JnxSvcFlowTableAggStatsEntry_Object = MibTableRow
jnxSvcFlowTableAggStatsEntry = _JnxSvcFlowTableAggStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1)
)
jnxSvcFlowTableAggStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxSvcFlowTableAggStatsEntry.setStatus("current")
_JnxSvcAggFlow_Type = Gauge32
_JnxSvcAggFlow_Object = MibTableColumn
jnxSvcAggFlow = _JnxSvcAggFlow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 1),
    _JnxSvcAggFlow_Type()
)
jnxSvcAggFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlow.setStatus("current")
_JnxSvcAggFlowMaximum_Type = Gauge32
_JnxSvcAggFlowMaximum_Object = MibTableColumn
jnxSvcAggFlowMaximum = _JnxSvcAggFlowMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 2),
    _JnxSvcAggFlowMaximum_Type()
)
jnxSvcAggFlowMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowMaximum.setStatus("current")
_JnxSvcAggFlowCreated_Type = Counter64
_JnxSvcAggFlowCreated_Object = MibTableColumn
jnxSvcAggFlowCreated = _JnxSvcAggFlowCreated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 3),
    _JnxSvcAggFlowCreated_Type()
)
jnxSvcAggFlowCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowCreated.setStatus("current")
_JnxSvcAggFlowFreed_Type = Counter64
_JnxSvcAggFlowFreed_Object = MibTableColumn
jnxSvcAggFlowFreed = _JnxSvcAggFlowFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 4),
    _JnxSvcAggFlowFreed_Type()
)
jnxSvcAggFlowFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowFreed.setStatus("current")
_JnxSvcAggFlowIdleFreed_Type = Counter64
_JnxSvcAggFlowIdleFreed_Object = MibTableColumn
jnxSvcAggFlowIdleFreed = _JnxSvcAggFlowIdleFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 5),
    _JnxSvcAggFlowIdleFreed_Type()
)
jnxSvcAggFlowIdleFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowIdleFreed.setStatus("current")
_JnxSvcAggFlowTcp_Type = Gauge32
_JnxSvcAggFlowTcp_Object = MibTableColumn
jnxSvcAggFlowTcp = _JnxSvcAggFlowTcp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 6),
    _JnxSvcAggFlowTcp_Type()
)
jnxSvcAggFlowTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcp.setStatus("current")
_JnxSvcAggFlowTcpMaximum_Type = Gauge32
_JnxSvcAggFlowTcpMaximum_Object = MibTableColumn
jnxSvcAggFlowTcpMaximum = _JnxSvcAggFlowTcpMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 7),
    _JnxSvcAggFlowTcpMaximum_Type()
)
jnxSvcAggFlowTcpMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpMaximum.setStatus("current")
_JnxSvcAggFlowTcpCreated_Type = Counter64
_JnxSvcAggFlowTcpCreated_Object = MibTableColumn
jnxSvcAggFlowTcpCreated = _JnxSvcAggFlowTcpCreated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 8),
    _JnxSvcAggFlowTcpCreated_Type()
)
jnxSvcAggFlowTcpCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpCreated.setStatus("current")
_JnxSvcAggFlowTcpFreed_Type = Counter64
_JnxSvcAggFlowTcpFreed_Object = MibTableColumn
jnxSvcAggFlowTcpFreed = _JnxSvcAggFlowTcpFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 9),
    _JnxSvcAggFlowTcpFreed_Type()
)
jnxSvcAggFlowTcpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpFreed.setStatus("current")
_JnxSvcAggFlowTcpIdleFreed_Type = Counter64
_JnxSvcAggFlowTcpIdleFreed_Object = MibTableColumn
jnxSvcAggFlowTcpIdleFreed = _JnxSvcAggFlowTcpIdleFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 10),
    _JnxSvcAggFlowTcpIdleFreed_Type()
)
jnxSvcAggFlowTcpIdleFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpIdleFreed.setStatus("current")
_JnxSvcAggFlowUdp_Type = Gauge32
_JnxSvcAggFlowUdp_Object = MibTableColumn
jnxSvcAggFlowUdp = _JnxSvcAggFlowUdp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 11),
    _JnxSvcAggFlowUdp_Type()
)
jnxSvcAggFlowUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdp.setStatus("current")
_JnxSvcAggFlowUdpMaximum_Type = Gauge32
_JnxSvcAggFlowUdpMaximum_Object = MibTableColumn
jnxSvcAggFlowUdpMaximum = _JnxSvcAggFlowUdpMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 12),
    _JnxSvcAggFlowUdpMaximum_Type()
)
jnxSvcAggFlowUdpMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpMaximum.setStatus("current")
_JnxSvcAggFlowUdpCreated_Type = Counter64
_JnxSvcAggFlowUdpCreated_Object = MibTableColumn
jnxSvcAggFlowUdpCreated = _JnxSvcAggFlowUdpCreated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 13),
    _JnxSvcAggFlowUdpCreated_Type()
)
jnxSvcAggFlowUdpCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpCreated.setStatus("current")
_JnxSvcAggFlowUdpFreed_Type = Counter64
_JnxSvcAggFlowUdpFreed_Object = MibTableColumn
jnxSvcAggFlowUdpFreed = _JnxSvcAggFlowUdpFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 14),
    _JnxSvcAggFlowUdpFreed_Type()
)
jnxSvcAggFlowUdpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpFreed.setStatus("current")
_JnxSvcAggFlowUdpIdleFreed_Type = Counter64
_JnxSvcAggFlowUdpIdleFreed_Object = MibTableColumn
jnxSvcAggFlowUdpIdleFreed = _JnxSvcAggFlowUdpIdleFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 15),
    _JnxSvcAggFlowUdpIdleFreed_Type()
)
jnxSvcAggFlowUdpIdleFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpIdleFreed.setStatus("current")
_JnxSvcAggFlowPkt_Type = Counter64
_JnxSvcAggFlowPkt_Object = MibTableColumn
jnxSvcAggFlowPkt = _JnxSvcAggFlowPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 16),
    _JnxSvcAggFlowPkt_Type()
)
jnxSvcAggFlowPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowPkt.setStatus("current")
_JnxSvcAggFlowPktErr_Type = Counter64
_JnxSvcAggFlowPktErr_Object = MibTableColumn
jnxSvcAggFlowPktErr = _JnxSvcAggFlowPktErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 17),
    _JnxSvcAggFlowPktErr_Type()
)
jnxSvcAggFlowPktErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowPktErr.setStatus("current")
_JnxSvcAggFlowByte_Type = Counter64
_JnxSvcAggFlowByte_Object = MibTableColumn
jnxSvcAggFlowByte = _JnxSvcAggFlowByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 18),
    _JnxSvcAggFlowByte_Type()
)
jnxSvcAggFlowByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowByte.setStatus("current")
_JnxSvcAggFlowByteErr_Type = Counter64
_JnxSvcAggFlowByteErr_Object = MibTableColumn
jnxSvcAggFlowByteErr = _JnxSvcAggFlowByteErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 19),
    _JnxSvcAggFlowByteErr_Type()
)
jnxSvcAggFlowByteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowByteErr.setStatus("current")
_JnxSvcAggFlowIcmpPkt_Type = Counter64
_JnxSvcAggFlowIcmpPkt_Object = MibTableColumn
jnxSvcAggFlowIcmpPkt = _JnxSvcAggFlowIcmpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 20),
    _JnxSvcAggFlowIcmpPkt_Type()
)
jnxSvcAggFlowIcmpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowIcmpPkt.setStatus("current")
_JnxSvcAggFlowIcmpPktErr_Type = Counter64
_JnxSvcAggFlowIcmpPktErr_Object = MibTableColumn
jnxSvcAggFlowIcmpPktErr = _JnxSvcAggFlowIcmpPktErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 21),
    _JnxSvcAggFlowIcmpPktErr_Type()
)
jnxSvcAggFlowIcmpPktErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowIcmpPktErr.setStatus("current")
_JnxSvcAggFlowIcmpPktErrBadFlow_Type = Counter64
_JnxSvcAggFlowIcmpPktErrBadFlow_Object = MibTableColumn
jnxSvcAggFlowIcmpPktErrBadFlow = _JnxSvcAggFlowIcmpPktErrBadFlow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 22),
    _JnxSvcAggFlowIcmpPktErrBadFlow_Type()
)
jnxSvcAggFlowIcmpPktErrBadFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowIcmpPktErrBadFlow.setStatus("current")
_JnxSvcAggFlowIcmpByte_Type = Counter64
_JnxSvcAggFlowIcmpByte_Object = MibTableColumn
jnxSvcAggFlowIcmpByte = _JnxSvcAggFlowIcmpByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 23),
    _JnxSvcAggFlowIcmpByte_Type()
)
jnxSvcAggFlowIcmpByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowIcmpByte.setStatus("current")
_JnxSvcAggFlowIcmpByteErr_Type = Counter64
_JnxSvcAggFlowIcmpByteErr_Object = MibTableColumn
jnxSvcAggFlowIcmpByteErr = _JnxSvcAggFlowIcmpByteErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 24),
    _JnxSvcAggFlowIcmpByteErr_Type()
)
jnxSvcAggFlowIcmpByteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowIcmpByteErr.setStatus("current")
_JnxSvcAggFlowTcpPkt_Type = Counter64
_JnxSvcAggFlowTcpPkt_Object = MibTableColumn
jnxSvcAggFlowTcpPkt = _JnxSvcAggFlowTcpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 25),
    _JnxSvcAggFlowTcpPkt_Type()
)
jnxSvcAggFlowTcpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpPkt.setStatus("current")
_JnxSvcAggFlowTcpPktErr_Type = Counter64
_JnxSvcAggFlowTcpPktErr_Object = MibTableColumn
jnxSvcAggFlowTcpPktErr = _JnxSvcAggFlowTcpPktErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 26),
    _JnxSvcAggFlowTcpPktErr_Type()
)
jnxSvcAggFlowTcpPktErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpPktErr.setStatus("current")
_JnxSvcAggFlowTcpPktErrBadFlow_Type = Counter64
_JnxSvcAggFlowTcpPktErrBadFlow_Object = MibTableColumn
jnxSvcAggFlowTcpPktErrBadFlow = _JnxSvcAggFlowTcpPktErrBadFlow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 27),
    _JnxSvcAggFlowTcpPktErrBadFlow_Type()
)
jnxSvcAggFlowTcpPktErrBadFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpPktErrBadFlow.setStatus("current")
_JnxSvcAggFlowTcpByte_Type = Counter64
_JnxSvcAggFlowTcpByte_Object = MibTableColumn
jnxSvcAggFlowTcpByte = _JnxSvcAggFlowTcpByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 28),
    _JnxSvcAggFlowTcpByte_Type()
)
jnxSvcAggFlowTcpByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpByte.setStatus("current")
_JnxSvcAggFlowTcpByteErr_Type = Counter64
_JnxSvcAggFlowTcpByteErr_Object = MibTableColumn
jnxSvcAggFlowTcpByteErr = _JnxSvcAggFlowTcpByteErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 29),
    _JnxSvcAggFlowTcpByteErr_Type()
)
jnxSvcAggFlowTcpByteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowTcpByteErr.setStatus("current")
_JnxSvcAggFlowUdpPkt_Type = Counter64
_JnxSvcAggFlowUdpPkt_Object = MibTableColumn
jnxSvcAggFlowUdpPkt = _JnxSvcAggFlowUdpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 30),
    _JnxSvcAggFlowUdpPkt_Type()
)
jnxSvcAggFlowUdpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpPkt.setStatus("current")
_JnxSvcAggFlowUdpPktErr_Type = Counter64
_JnxSvcAggFlowUdpPktErr_Object = MibTableColumn
jnxSvcAggFlowUdpPktErr = _JnxSvcAggFlowUdpPktErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 31),
    _JnxSvcAggFlowUdpPktErr_Type()
)
jnxSvcAggFlowUdpPktErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpPktErr.setStatus("current")
_JnxSvcAggFlowUdpPktErrBadFlow_Type = Counter64
_JnxSvcAggFlowUdpPktErrBadFlow_Object = MibTableColumn
jnxSvcAggFlowUdpPktErrBadFlow = _JnxSvcAggFlowUdpPktErrBadFlow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 32),
    _JnxSvcAggFlowUdpPktErrBadFlow_Type()
)
jnxSvcAggFlowUdpPktErrBadFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpPktErrBadFlow.setStatus("current")
_JnxSvcAggFlowUdpByte_Type = Counter64
_JnxSvcAggFlowUdpByte_Object = MibTableColumn
jnxSvcAggFlowUdpByte = _JnxSvcAggFlowUdpByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 33),
    _JnxSvcAggFlowUdpByte_Type()
)
jnxSvcAggFlowUdpByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpByte.setStatus("current")
_JnxSvcAggFlowUdpByteErr_Type = Counter64
_JnxSvcAggFlowUdpByteErr_Object = MibTableColumn
jnxSvcAggFlowUdpByteErr = _JnxSvcAggFlowUdpByteErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 1, 1, 34),
    _JnxSvcAggFlowUdpByteErr_Type()
)
jnxSvcAggFlowUdpByteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcAggFlowUdpByteErr.setStatus("current")
_JnxSvcServIdTable_Object = MibTable
jnxSvcServIdTable = _JnxSvcServIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2)
)
if mibBuilder.loadTexts:
    jnxSvcServIdTable.setStatus("current")
_JnxSvcServIdTableEntry_Object = MibTableRow
jnxSvcServIdTableEntry = _JnxSvcServIdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1)
)
jnxSvcServIdTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxSvcServIdTableEntry.setStatus("current")
_JnxSvcServIdPkt_Type = Counter64
_JnxSvcServIdPkt_Object = MibTableColumn
jnxSvcServIdPkt = _JnxSvcServIdPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 1),
    _JnxSvcServIdPkt_Type()
)
jnxSvcServIdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdPkt.setStatus("current")
_JnxSvcServIdByte_Type = Counter64
_JnxSvcServIdByte_Object = MibTableColumn
jnxSvcServIdByte = _JnxSvcServIdByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 2),
    _JnxSvcServIdByte_Type()
)
jnxSvcServIdByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdByte.setStatus("current")
_JnxSvcServIdErrPkt_Type = Counter64
_JnxSvcServIdErrPkt_Object = MibTableColumn
jnxSvcServIdErrPkt = _JnxSvcServIdErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 3),
    _JnxSvcServIdErrPkt_Type()
)
jnxSvcServIdErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdErrPkt.setStatus("current")
_JnxSvcServIdErrByte_Type = Counter64
_JnxSvcServIdErrByte_Object = MibTableColumn
jnxSvcServIdErrByte = _JnxSvcServIdErrByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 4),
    _JnxSvcServIdErrByte_Type()
)
jnxSvcServIdErrByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdErrByte.setStatus("current")
_JnxSvcServIdHeadExPkt_Type = Counter64
_JnxSvcServIdHeadExPkt_Object = MibTableColumn
jnxSvcServIdHeadExPkt = _JnxSvcServIdHeadExPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 5),
    _JnxSvcServIdHeadExPkt_Type()
)
jnxSvcServIdHeadExPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExPkt.setStatus("current")
_JnxSvcServIdHeadExByte_Type = Counter64
_JnxSvcServIdHeadExByte_Object = MibTableColumn
jnxSvcServIdHeadExByte = _JnxSvcServIdHeadExByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 6),
    _JnxSvcServIdHeadExByte_Type()
)
jnxSvcServIdHeadExByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExByte.setStatus("current")
_JnxSvcServIdHeadExFlow_Type = Counter64
_JnxSvcServIdHeadExFlow_Object = MibTableColumn
jnxSvcServIdHeadExFlow = _JnxSvcServIdHeadExFlow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 7),
    _JnxSvcServIdHeadExFlow_Type()
)
jnxSvcServIdHeadExFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExFlow.setStatus("current")
_JnxSvcServIdHeadExFlowMtch_Type = Counter64
_JnxSvcServIdHeadExFlowMtch_Object = MibTableColumn
jnxSvcServIdHeadExFlowMtch = _JnxSvcServIdHeadExFlowMtch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 8),
    _JnxSvcServIdHeadExFlowMtch_Type()
)
jnxSvcServIdHeadExFlowMtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExFlowMtch.setStatus("current")
_JnxSvcServIdHeadExProtoReq_Type = Counter64
_JnxSvcServIdHeadExProtoReq_Object = MibTableColumn
jnxSvcServIdHeadExProtoReq = _JnxSvcServIdHeadExProtoReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 13),
    _JnxSvcServIdHeadExProtoReq_Type()
)
jnxSvcServIdHeadExProtoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExProtoReq.setStatus("current")
_JnxSvcServIdHeadExHttpProtoReq_Type = Counter64
_JnxSvcServIdHeadExHttpProtoReq_Object = MibTableColumn
jnxSvcServIdHeadExHttpProtoReq = _JnxSvcServIdHeadExHttpProtoReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 14),
    _JnxSvcServIdHeadExHttpProtoReq_Type()
)
jnxSvcServIdHeadExHttpProtoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExHttpProtoReq.setStatus("current")
_JnxSvcServIdHeadExWapProtoReq_Type = Counter64
_JnxSvcServIdHeadExWapProtoReq_Object = MibTableColumn
jnxSvcServIdHeadExWapProtoReq = _JnxSvcServIdHeadExWapProtoReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 15),
    _JnxSvcServIdHeadExWapProtoReq_Type()
)
jnxSvcServIdHeadExWapProtoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExWapProtoReq.setStatus("current")
_JnxSvcServIdProtFlow_Type = Gauge32
_JnxSvcServIdProtFlow_Object = MibTableColumn
jnxSvcServIdProtFlow = _JnxSvcServIdProtFlow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 16),
    _JnxSvcServIdProtFlow_Type()
)
jnxSvcServIdProtFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtFlow.setStatus("current")
_JnxSvcServIdProtInsPkt_Type = Counter64
_JnxSvcServIdProtInsPkt_Object = MibTableColumn
jnxSvcServIdProtInsPkt = _JnxSvcServIdProtInsPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 17),
    _JnxSvcServIdProtInsPkt_Type()
)
jnxSvcServIdProtInsPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsPkt.setStatus("current")
_JnxSvcServIdProtInsByte_Type = Counter64
_JnxSvcServIdProtInsByte_Object = MibTableColumn
jnxSvcServIdProtInsByte = _JnxSvcServIdProtInsByte_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 18),
    _JnxSvcServIdProtInsByte_Type()
)
jnxSvcServIdProtInsByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsByte.setStatus("current")
_JnxSvcServIdProtInsFlowInsp_Type = Counter64
_JnxSvcServIdProtInsFlowInsp_Object = MibTableColumn
jnxSvcServIdProtInsFlowInsp = _JnxSvcServIdProtInsFlowInsp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 19),
    _JnxSvcServIdProtInsFlowInsp_Type()
)
jnxSvcServIdProtInsFlowInsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsFlowInsp.setStatus("current")
_JnxSvcServIdProtInsFlowProtIdent_Type = Counter64
_JnxSvcServIdProtInsFlowProtIdent_Object = MibTableColumn
jnxSvcServIdProtInsFlowProtIdent = _JnxSvcServIdProtInsFlowProtIdent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 20),
    _JnxSvcServIdProtInsFlowProtIdent_Type()
)
jnxSvcServIdProtInsFlowProtIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsFlowProtIdent.setStatus("current")
_JnxSvcServIdProtInsHttpUri_Type = Counter64
_JnxSvcServIdProtInsHttpUri_Object = MibTableColumn
jnxSvcServIdProtInsHttpUri = _JnxSvcServIdProtInsHttpUri_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 24),
    _JnxSvcServIdProtInsHttpUri_Type()
)
jnxSvcServIdProtInsHttpUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsHttpUri.setStatus("current")
_JnxSvcServIdProtInsHttpUriMtch_Type = Counter64
_JnxSvcServIdProtInsHttpUriMtch_Object = MibTableColumn
jnxSvcServIdProtInsHttpUriMtch = _JnxSvcServIdProtInsHttpUriMtch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 25),
    _JnxSvcServIdProtInsHttpUriMtch_Type()
)
jnxSvcServIdProtInsHttpUriMtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsHttpUriMtch.setStatus("current")
_JnxSvcServIdProtInsWapUri_Type = Counter64
_JnxSvcServIdProtInsWapUri_Object = MibTableColumn
jnxSvcServIdProtInsWapUri = _JnxSvcServIdProtInsWapUri_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 26),
    _JnxSvcServIdProtInsWapUri_Type()
)
jnxSvcServIdProtInsWapUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsWapUri.setStatus("current")
_JnxSvcServIdProtInsWapUriMtch_Type = Counter64
_JnxSvcServIdProtInsWapUriMtch_Object = MibTableColumn
jnxSvcServIdProtInsWapUriMtch = _JnxSvcServIdProtInsWapUriMtch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 27),
    _JnxSvcServIdProtInsWapUriMtch_Type()
)
jnxSvcServIdProtInsWapUriMtch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsWapUriMtch.setStatus("current")
_JnxSvcServIdPktTcpMalform_Type = Counter64
_JnxSvcServIdPktTcpMalform_Object = MibTableColumn
jnxSvcServIdPktTcpMalform = _JnxSvcServIdPktTcpMalform_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 28),
    _JnxSvcServIdPktTcpMalform_Type()
)
jnxSvcServIdPktTcpMalform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdPktTcpMalform.setStatus("current")
_JnxSvcServIdWAPInvalidTxn_Type = Counter64
_JnxSvcServIdWAPInvalidTxn_Object = MibTableColumn
jnxSvcServIdWAPInvalidTxn = _JnxSvcServIdWAPInvalidTxn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 29),
    _JnxSvcServIdWAPInvalidTxn_Type()
)
jnxSvcServIdWAPInvalidTxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdWAPInvalidTxn.setStatus("current")
_JnxSvcServIdErrWAPTxn_Type = Counter64
_JnxSvcServIdErrWAPTxn_Object = MibTableColumn
jnxSvcServIdErrWAPTxn = _JnxSvcServIdErrWAPTxn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 30),
    _JnxSvcServIdErrWAPTxn_Type()
)
jnxSvcServIdErrWAPTxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdErrWAPTxn.setStatus("current")
_JnxSvcServIdErrHTTPTxn_Type = Counter64
_JnxSvcServIdErrHTTPTxn_Object = MibTableColumn
jnxSvcServIdErrHTTPTxn = _JnxSvcServIdErrHTTPTxn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 31),
    _JnxSvcServIdErrHTTPTxn_Type()
)
jnxSvcServIdErrHTTPTxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdErrHTTPTxn.setStatus("current")
_JnxSvcServIdHeadExFailCfgState_Type = Counter64
_JnxSvcServIdHeadExFailCfgState_Object = MibTableColumn
jnxSvcServIdHeadExFailCfgState = _JnxSvcServIdHeadExFailCfgState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 32),
    _JnxSvcServIdHeadExFailCfgState_Type()
)
jnxSvcServIdHeadExFailCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdHeadExFailCfgState.setStatus("current")
_JnxSvcServIdProtInsFailCfgState_Type = Counter64
_JnxSvcServIdProtInsFailCfgState_Object = MibTableColumn
jnxSvcServIdProtInsFailCfgState = _JnxSvcServIdProtInsFailCfgState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 33),
    _JnxSvcServIdProtInsFailCfgState_Type()
)
jnxSvcServIdProtInsFailCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServIdProtInsFailCfgState.setStatus("current")
_JnxSvcTransactionWapCreated_Type = Counter64
_JnxSvcTransactionWapCreated_Object = MibTableColumn
jnxSvcTransactionWapCreated = _JnxSvcTransactionWapCreated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 34),
    _JnxSvcTransactionWapCreated_Type()
)
jnxSvcTransactionWapCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionWapCreated.setStatus("current")
_JnxSvcTransactionWapMaximum_Type = Gauge32
_JnxSvcTransactionWapMaximum_Object = MibTableColumn
jnxSvcTransactionWapMaximum = _JnxSvcTransactionWapMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 35),
    _JnxSvcTransactionWapMaximum_Type()
)
jnxSvcTransactionWapMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionWapMaximum.setStatus("current")
_JnxSvcTransactionWapFreed_Type = Counter64
_JnxSvcTransactionWapFreed_Object = MibTableColumn
jnxSvcTransactionWapFreed = _JnxSvcTransactionWapFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 36),
    _JnxSvcTransactionWapFreed_Type()
)
jnxSvcTransactionWapFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionWapFreed.setStatus("current")
_JnxSvcTransactionWapIdleFreed_Type = Counter64
_JnxSvcTransactionWapIdleFreed_Object = MibTableColumn
jnxSvcTransactionWapIdleFreed = _JnxSvcTransactionWapIdleFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 37),
    _JnxSvcTransactionWapIdleFreed_Type()
)
jnxSvcTransactionWapIdleFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionWapIdleFreed.setStatus("current")
_JnxSvcTransactionHttpCreated_Type = Counter64
_JnxSvcTransactionHttpCreated_Object = MibTableColumn
jnxSvcTransactionHttpCreated = _JnxSvcTransactionHttpCreated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 38),
    _JnxSvcTransactionHttpCreated_Type()
)
jnxSvcTransactionHttpCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionHttpCreated.setStatus("current")
_JnxSvcTransactionHttpMaximum_Type = Gauge32
_JnxSvcTransactionHttpMaximum_Object = MibTableColumn
jnxSvcTransactionHttpMaximum = _JnxSvcTransactionHttpMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 39),
    _JnxSvcTransactionHttpMaximum_Type()
)
jnxSvcTransactionHttpMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionHttpMaximum.setStatus("current")
_JnxSvcTransactionHttpFreed_Type = Counter64
_JnxSvcTransactionHttpFreed_Object = MibTableColumn
jnxSvcTransactionHttpFreed = _JnxSvcTransactionHttpFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 40),
    _JnxSvcTransactionHttpFreed_Type()
)
jnxSvcTransactionHttpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionHttpFreed.setStatus("current")
_JnxSvcTransactionHttpIdleFreed_Type = Counter64
_JnxSvcTransactionHttpIdleFreed_Object = MibTableColumn
jnxSvcTransactionHttpIdleFreed = _JnxSvcTransactionHttpIdleFreed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 41),
    _JnxSvcTransactionHttpIdleFreed_Type()
)
jnxSvcTransactionHttpIdleFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcTransactionHttpIdleFreed.setStatus("current")
_JnxSvcServidProtInsUriErrProcess_Type = Counter64
_JnxSvcServidProtInsUriErrProcess_Object = MibTableColumn
jnxSvcServidProtInsUriErrProcess = _JnxSvcServidProtInsUriErrProcess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 42),
    _JnxSvcServidProtInsUriErrProcess_Type()
)
jnxSvcServidProtInsUriErrProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServidProtInsUriErrProcess.setStatus("current")
_JnxSvcServidProtInsUriErrTooLong_Type = Counter64
_JnxSvcServidProtInsUriErrTooLong_Object = MibTableColumn
jnxSvcServidProtInsUriErrTooLong = _JnxSvcServidProtInsUriErrTooLong_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 43),
    _JnxSvcServidProtInsUriErrTooLong_Type()
)
jnxSvcServidProtInsUriErrTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServidProtInsUriErrTooLong.setStatus("current")
_JnxSvcServidProtInsErrParseTx_Type = Counter64
_JnxSvcServidProtInsErrParseTx_Object = MibTableColumn
jnxSvcServidProtInsErrParseTx = _JnxSvcServidProtInsErrParseTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 44),
    _JnxSvcServidProtInsErrParseTx_Type()
)
jnxSvcServidProtInsErrParseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServidProtInsErrParseTx.setStatus("current")
_JnxSvcServidProtInsUriErrNoRes_Type = Counter64
_JnxSvcServidProtInsUriErrNoRes_Object = MibTableColumn
jnxSvcServidProtInsUriErrNoRes = _JnxSvcServidProtInsUriErrNoRes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 2, 1, 45),
    _JnxSvcServidProtInsUriErrNoRes_Type()
)
jnxSvcServidProtInsUriErrNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSvcServidProtInsUriErrNoRes.setStatus("current")
_JnxSvcMIBConformance_ObjectIdentity = ObjectIdentity
jnxSvcMIBConformance = _JnxSvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 20)
)
_JnxSvcMIBCompliances_ObjectIdentity = ObjectIdentity
jnxSvcMIBCompliances = _JnxSvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 20, 1)
)
_JnxSvcMIBGroups_ObjectIdentity = ObjectIdentity
jnxSvcMIBGroups = _JnxSvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 20, 2)
)

# Managed Objects groups

jnxSvcFlowTableAggStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 20, 2, 1)
)
jnxSvcFlowTableAggStatsGroup.setObjects(
      *(("JUNIPER-Services-MIB", "jnxSvcAggFlow"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowMaximum"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowCreated"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowIdleFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcp"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpMaximum"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpCreated"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpIdleFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdp"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpMaximum"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpCreated"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpIdleFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowPktErr"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowByte"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowByteErr"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowIcmpPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowIcmpPktErr"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowIcmpPktErrBadFlow"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowIcmpByte"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowIcmpByteErr"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpPktErr"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpPktErrBadFlow"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpByte"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowTcpByteErr"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpPktErr"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpPktErrBadFlow"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpByte"),
        ("JUNIPER-Services-MIB", "jnxSvcAggFlowUdpByteErr"))
)
if mibBuilder.loadTexts:
    jnxSvcFlowTableAggStatsGroup.setStatus("current")

jnxSvcServIdiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 20, 2, 2)
)
jnxSvcServIdiceGroup.setObjects(
      *(("JUNIPER-Services-MIB", "jnxSvcServIdPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdByte"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdErrPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdErrByte"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExByte"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExFlow"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExFlowMtch"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExProtoReq"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExHttpProtoReq"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExWapProtoReq"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtFlow"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsPkt"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsByte"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsFlowInsp"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsFlowProtIdent"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsHttpUri"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsHttpUriMtch"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsWapUri"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsWapUriMtch"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdPktTcpMalform"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdWAPInvalidTxn"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdErrWAPTxn"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdErrHTTPTxn"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdHeadExFailCfgState"),
        ("JUNIPER-Services-MIB", "jnxSvcServIdProtInsFailCfgState"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionWapCreated"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionWapMaximum"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionWapFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionWapIdleFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionHttpCreated"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionHttpMaximum"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionHttpFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcTransactionHttpIdleFreed"),
        ("JUNIPER-Services-MIB", "jnxSvcServidProtInsUriErrProcess"),
        ("JUNIPER-Services-MIB", "jnxSvcServidProtInsUriErrTooLong"),
        ("JUNIPER-Services-MIB", "jnxSvcServidProtInsErrParseTx"),
        ("JUNIPER-Services-MIB", "jnxSvcServidProtInsUriErrNoRes"))
)
if mibBuilder.loadTexts:
    jnxSvcServIdiceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

jnxSvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 27, 20, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSvcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-Services-MIB",
    **{"jnxServicesInfoMib": jnxServicesInfoMib,
       "jnxSvcFlowTableAggStatsTable": jnxSvcFlowTableAggStatsTable,
       "jnxSvcFlowTableAggStatsEntry": jnxSvcFlowTableAggStatsEntry,
       "jnxSvcAggFlow": jnxSvcAggFlow,
       "jnxSvcAggFlowMaximum": jnxSvcAggFlowMaximum,
       "jnxSvcAggFlowCreated": jnxSvcAggFlowCreated,
       "jnxSvcAggFlowFreed": jnxSvcAggFlowFreed,
       "jnxSvcAggFlowIdleFreed": jnxSvcAggFlowIdleFreed,
       "jnxSvcAggFlowTcp": jnxSvcAggFlowTcp,
       "jnxSvcAggFlowTcpMaximum": jnxSvcAggFlowTcpMaximum,
       "jnxSvcAggFlowTcpCreated": jnxSvcAggFlowTcpCreated,
       "jnxSvcAggFlowTcpFreed": jnxSvcAggFlowTcpFreed,
       "jnxSvcAggFlowTcpIdleFreed": jnxSvcAggFlowTcpIdleFreed,
       "jnxSvcAggFlowUdp": jnxSvcAggFlowUdp,
       "jnxSvcAggFlowUdpMaximum": jnxSvcAggFlowUdpMaximum,
       "jnxSvcAggFlowUdpCreated": jnxSvcAggFlowUdpCreated,
       "jnxSvcAggFlowUdpFreed": jnxSvcAggFlowUdpFreed,
       "jnxSvcAggFlowUdpIdleFreed": jnxSvcAggFlowUdpIdleFreed,
       "jnxSvcAggFlowPkt": jnxSvcAggFlowPkt,
       "jnxSvcAggFlowPktErr": jnxSvcAggFlowPktErr,
       "jnxSvcAggFlowByte": jnxSvcAggFlowByte,
       "jnxSvcAggFlowByteErr": jnxSvcAggFlowByteErr,
       "jnxSvcAggFlowIcmpPkt": jnxSvcAggFlowIcmpPkt,
       "jnxSvcAggFlowIcmpPktErr": jnxSvcAggFlowIcmpPktErr,
       "jnxSvcAggFlowIcmpPktErrBadFlow": jnxSvcAggFlowIcmpPktErrBadFlow,
       "jnxSvcAggFlowIcmpByte": jnxSvcAggFlowIcmpByte,
       "jnxSvcAggFlowIcmpByteErr": jnxSvcAggFlowIcmpByteErr,
       "jnxSvcAggFlowTcpPkt": jnxSvcAggFlowTcpPkt,
       "jnxSvcAggFlowTcpPktErr": jnxSvcAggFlowTcpPktErr,
       "jnxSvcAggFlowTcpPktErrBadFlow": jnxSvcAggFlowTcpPktErrBadFlow,
       "jnxSvcAggFlowTcpByte": jnxSvcAggFlowTcpByte,
       "jnxSvcAggFlowTcpByteErr": jnxSvcAggFlowTcpByteErr,
       "jnxSvcAggFlowUdpPkt": jnxSvcAggFlowUdpPkt,
       "jnxSvcAggFlowUdpPktErr": jnxSvcAggFlowUdpPktErr,
       "jnxSvcAggFlowUdpPktErrBadFlow": jnxSvcAggFlowUdpPktErrBadFlow,
       "jnxSvcAggFlowUdpByte": jnxSvcAggFlowUdpByte,
       "jnxSvcAggFlowUdpByteErr": jnxSvcAggFlowUdpByteErr,
       "jnxSvcServIdTable": jnxSvcServIdTable,
       "jnxSvcServIdTableEntry": jnxSvcServIdTableEntry,
       "jnxSvcServIdPkt": jnxSvcServIdPkt,
       "jnxSvcServIdByte": jnxSvcServIdByte,
       "jnxSvcServIdErrPkt": jnxSvcServIdErrPkt,
       "jnxSvcServIdErrByte": jnxSvcServIdErrByte,
       "jnxSvcServIdHeadExPkt": jnxSvcServIdHeadExPkt,
       "jnxSvcServIdHeadExByte": jnxSvcServIdHeadExByte,
       "jnxSvcServIdHeadExFlow": jnxSvcServIdHeadExFlow,
       "jnxSvcServIdHeadExFlowMtch": jnxSvcServIdHeadExFlowMtch,
       "jnxSvcServIdHeadExProtoReq": jnxSvcServIdHeadExProtoReq,
       "jnxSvcServIdHeadExHttpProtoReq": jnxSvcServIdHeadExHttpProtoReq,
       "jnxSvcServIdHeadExWapProtoReq": jnxSvcServIdHeadExWapProtoReq,
       "jnxSvcServIdProtFlow": jnxSvcServIdProtFlow,
       "jnxSvcServIdProtInsPkt": jnxSvcServIdProtInsPkt,
       "jnxSvcServIdProtInsByte": jnxSvcServIdProtInsByte,
       "jnxSvcServIdProtInsFlowInsp": jnxSvcServIdProtInsFlowInsp,
       "jnxSvcServIdProtInsFlowProtIdent": jnxSvcServIdProtInsFlowProtIdent,
       "jnxSvcServIdProtInsHttpUri": jnxSvcServIdProtInsHttpUri,
       "jnxSvcServIdProtInsHttpUriMtch": jnxSvcServIdProtInsHttpUriMtch,
       "jnxSvcServIdProtInsWapUri": jnxSvcServIdProtInsWapUri,
       "jnxSvcServIdProtInsWapUriMtch": jnxSvcServIdProtInsWapUriMtch,
       "jnxSvcServIdPktTcpMalform": jnxSvcServIdPktTcpMalform,
       "jnxSvcServIdWAPInvalidTxn": jnxSvcServIdWAPInvalidTxn,
       "jnxSvcServIdErrWAPTxn": jnxSvcServIdErrWAPTxn,
       "jnxSvcServIdErrHTTPTxn": jnxSvcServIdErrHTTPTxn,
       "jnxSvcServIdHeadExFailCfgState": jnxSvcServIdHeadExFailCfgState,
       "jnxSvcServIdProtInsFailCfgState": jnxSvcServIdProtInsFailCfgState,
       "jnxSvcTransactionWapCreated": jnxSvcTransactionWapCreated,
       "jnxSvcTransactionWapMaximum": jnxSvcTransactionWapMaximum,
       "jnxSvcTransactionWapFreed": jnxSvcTransactionWapFreed,
       "jnxSvcTransactionWapIdleFreed": jnxSvcTransactionWapIdleFreed,
       "jnxSvcTransactionHttpCreated": jnxSvcTransactionHttpCreated,
       "jnxSvcTransactionHttpMaximum": jnxSvcTransactionHttpMaximum,
       "jnxSvcTransactionHttpFreed": jnxSvcTransactionHttpFreed,
       "jnxSvcTransactionHttpIdleFreed": jnxSvcTransactionHttpIdleFreed,
       "jnxSvcServidProtInsUriErrProcess": jnxSvcServidProtInsUriErrProcess,
       "jnxSvcServidProtInsUriErrTooLong": jnxSvcServidProtInsUriErrTooLong,
       "jnxSvcServidProtInsErrParseTx": jnxSvcServidProtInsErrParseTx,
       "jnxSvcServidProtInsUriErrNoRes": jnxSvcServidProtInsUriErrNoRes,
       "jnxSvcMIBConformance": jnxSvcMIBConformance,
       "jnxSvcMIBCompliances": jnxSvcMIBCompliances,
       "jnxSvcMIBCompliance": jnxSvcMIBCompliance,
       "jnxSvcMIBGroups": jnxSvcMIBGroups,
       "jnxSvcFlowTableAggStatsGroup": jnxSvcFlowTableAggStatsGroup,
       "jnxSvcServIdiceGroup": jnxSvcServIdiceGroup}
)
