# SNMP MIB module (TIARA-DOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-DOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:33 2024
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

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraDenialOfServiceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TiaraDeosGlobal_ObjectIdentity = ObjectIdentity
tiaraDeosGlobal = _TiaraDeosGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 1)
)


class _TiaraDeosWan_Type(TruthValue):
    """Custom type tiaraDeosWan based on TruthValue"""


_TiaraDeosWan_Object = MibScalar
tiaraDeosWan = _TiaraDeosWan_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 1, 1),
    _TiaraDeosWan_Type()
)
tiaraDeosWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraDeosWan.setStatus("current")


class _TiaraDeosPing_Type(TruthValue):
    """Custom type tiaraDeosPing based on TruthValue"""


_TiaraDeosPing_Object = MibScalar
tiaraDeosPing = _TiaraDeosPing_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 1, 2),
    _TiaraDeosPing_Type()
)
tiaraDeosPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraDeosPing.setStatus("current")


class _TiaraDeosIcmp_Type(TruthValue):
    """Custom type tiaraDeosIcmp based on TruthValue"""


_TiaraDeosIcmp_Object = MibScalar
tiaraDeosIcmp = _TiaraDeosIcmp_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 1, 3),
    _TiaraDeosIcmp_Type()
)
tiaraDeosIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraDeosIcmp.setStatus("current")
_TiaraDeosEthTable_Object = MibTable
tiaraDeosEthTable = _TiaraDeosEthTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 2)
)
if mibBuilder.loadTexts:
    tiaraDeosEthTable.setStatus("current")
_TiaraDeosEthEntry_Object = MibTableRow
tiaraDeosEthEntry = _TiaraDeosEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 2, 1)
)
tiaraDeosEthEntry.setIndexNames(
    (0, "TIARA-DOS-MIB", "ethNum"),
)
if mibBuilder.loadTexts:
    tiaraDeosEthEntry.setStatus("current")
_EthNum_Type = Integer32
_EthNum_Object = MibTableColumn
ethNum = _EthNum_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 2, 1, 1),
    _EthNum_Type()
)
ethNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethNum.setStatus("current")


class _StatusDeosEth_Type(TruthValue):
    """Custom type statusDeosEth based on TruthValue"""


_StatusDeosEth_Object = MibTableColumn
statusDeosEth = _StatusDeosEth_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 2, 1, 2),
    _StatusDeosEth_Type()
)
statusDeosEth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusDeosEth.setStatus("current")
_TiaraIncompleteTcpTable_Object = MibTable
tiaraIncompleteTcpTable = _TiaraIncompleteTcpTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 3)
)
if mibBuilder.loadTexts:
    tiaraIncompleteTcpTable.setStatus("current")
_TiaraIncompleteTcpEntry_Object = MibTableRow
tiaraIncompleteTcpEntry = _TiaraIncompleteTcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1)
)
tiaraIncompleteTcpEntry.setIndexNames(
    (0, "TIARA-DOS-MIB", "ethNum"),
)
if mibBuilder.loadTexts:
    tiaraIncompleteTcpEntry.setStatus("current")
_TcpIncompleteIndex_Type = Integer32
_TcpIncompleteIndex_Object = MibTableColumn
tcpIncompleteIndex = _TcpIncompleteIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 1),
    _TcpIncompleteIndex_Type()
)
tcpIncompleteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcpIncompleteIndex.setStatus("current")
_SrcIpAddress_Type = IpAddress
_SrcIpAddress_Object = MibTableColumn
srcIpAddress = _SrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 2),
    _SrcIpAddress_Type()
)
srcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcIpAddress.setStatus("current")
_DestIpAddress_Type = IpAddress
_DestIpAddress_Object = MibTableColumn
destIpAddress = _DestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 3),
    _DestIpAddress_Type()
)
destIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destIpAddress.setStatus("current")
_SrcPort_Type = Integer32
_SrcPort_Object = MibTableColumn
srcPort = _SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 4),
    _SrcPort_Type()
)
srcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcPort.setStatus("current")
_DestPort_Type = Integer32
_DestPort_Object = MibTableColumn
destPort = _DestPort_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 50, 3, 1, 5),
    _DestPort_Type()
)
destPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-DOS-MIB",
    **{"tiaraDenialOfServiceMib": tiaraDenialOfServiceMib,
       "tiaraDeosGlobal": tiaraDeosGlobal,
       "tiaraDeosWan": tiaraDeosWan,
       "tiaraDeosPing": tiaraDeosPing,
       "tiaraDeosIcmp": tiaraDeosIcmp,
       "tiaraDeosEthTable": tiaraDeosEthTable,
       "tiaraDeosEthEntry": tiaraDeosEthEntry,
       "ethNum": ethNum,
       "statusDeosEth": statusDeosEth,
       "tiaraIncompleteTcpTable": tiaraIncompleteTcpTable,
       "tiaraIncompleteTcpEntry": tiaraIncompleteTcpEntry,
       "tcpIncompleteIndex": tcpIncompleteIndex,
       "srcIpAddress": srcIpAddress,
       "destIpAddress": destIpAddress,
       "srcPort": srcPort,
       "destPort": destPort}
)
