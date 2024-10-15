# SNMP MIB module (RAPID-IPSEC-ENDPOINT-PAIR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-IPSEC-ENDPOINT-PAIR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:37 2024
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

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rsIpsecEndpointPairModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 5)
)
rsIpsecEndpointPairModule.setRevisions(
        ("2000-03-21 12:00",
         "2002-11-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIpsecEndpointPairMIB_ObjectIdentity = ObjectIdentity
rsIpsecEndpointPairMIB = _RsIpsecEndpointPairMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1)
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPairMIB.setStatus("current")
_RsIpsecEndpointPair_ObjectIdentity = ObjectIdentity
rsIpsecEndpointPair = _RsIpsecEndpointPair_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPair.setStatus("current")
_RsIpsecEndpointPairNum_Type = Unsigned32
_RsIpsecEndpointPairNum_Object = MibScalar
rsIpsecEndpointPairNum = _RsIpsecEndpointPairNum_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 1),
    _RsIpsecEndpointPairNum_Type()
)
rsIpsecEndpointPairNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairNum.setStatus("current")
_RsIpsecEndpointPairTable_Object = MibTable
rsIpsecEndpointPairTable = _RsIpsecEndpointPairTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTable.setStatus("current")
_RsIpsecEndpointPairEntry_Object = MibTableRow
rsIpsecEndpointPairEntry = _RsIpsecEndpointPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1)
)
rsIpsecEndpointPairEntry.setIndexNames(
    (0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairIndex"),
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPairEntry.setStatus("current")
_RsIpsecEndpointPairIndex_Type = Integer32
_RsIpsecEndpointPairIndex_Object = MibTableColumn
rsIpsecEndpointPairIndex = _RsIpsecEndpointPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 1),
    _RsIpsecEndpointPairIndex_Type()
)
rsIpsecEndpointPairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairIndex.setStatus("current")
_RsIpsecEndpointPairLocalAddr_Type = IpAddress
_RsIpsecEndpointPairLocalAddr_Object = MibTableColumn
rsIpsecEndpointPairLocalAddr = _RsIpsecEndpointPairLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 2),
    _RsIpsecEndpointPairLocalAddr_Type()
)
rsIpsecEndpointPairLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairLocalAddr.setStatus("current")
_RsIpsecEndpointPairPeerAddr_Type = IpAddress
_RsIpsecEndpointPairPeerAddr_Object = MibTableColumn
rsIpsecEndpointPairPeerAddr = _RsIpsecEndpointPairPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 3),
    _RsIpsecEndpointPairPeerAddr_Type()
)
rsIpsecEndpointPairPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPeerAddr.setStatus("current")
_RsIpsecEndpointPairInSAs_Type = Unsigned32
_RsIpsecEndpointPairInSAs_Object = MibTableColumn
rsIpsecEndpointPairInSAs = _RsIpsecEndpointPairInSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 4),
    _RsIpsecEndpointPairInSAs_Type()
)
rsIpsecEndpointPairInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairInSAs.setStatus("current")
_RsIpsecEndpointPairOutSAs_Type = Unsigned32
_RsIpsecEndpointPairOutSAs_Object = MibTableColumn
rsIpsecEndpointPairOutSAs = _RsIpsecEndpointPairOutSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 5),
    _RsIpsecEndpointPairOutSAs_Type()
)
rsIpsecEndpointPairOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairOutSAs.setStatus("current")
_RsIpsecEndpointPairInAccKbytes_Type = Counter32
_RsIpsecEndpointPairInAccKbytes_Object = MibTableColumn
rsIpsecEndpointPairInAccKbytes = _RsIpsecEndpointPairInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 6),
    _RsIpsecEndpointPairInAccKbytes_Type()
)
rsIpsecEndpointPairInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairInAccKbytes.setUnits("Kbytes")
_RsIpsecEndpointPairOutAccKbytes_Type = Counter32
_RsIpsecEndpointPairOutAccKbytes_Object = MibTableColumn
rsIpsecEndpointPairOutAccKbytes = _RsIpsecEndpointPairOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 7),
    _RsIpsecEndpointPairOutAccKbytes_Type()
)
rsIpsecEndpointPairOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairOutAccKbytes.setUnits("Kbytes")
_RsIpsecEndpointPairInPackets_Type = Counter32
_RsIpsecEndpointPairInPackets_Object = MibTableColumn
rsIpsecEndpointPairInPackets = _RsIpsecEndpointPairInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 8),
    _RsIpsecEndpointPairInPackets_Type()
)
rsIpsecEndpointPairInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairInPackets.setStatus("current")
_RsIpsecEndpointPairOutPackets_Type = Counter32
_RsIpsecEndpointPairOutPackets_Object = MibTableColumn
rsIpsecEndpointPairOutPackets = _RsIpsecEndpointPairOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 9),
    _RsIpsecEndpointPairOutPackets_Type()
)
rsIpsecEndpointPairOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairOutPackets.setStatus("current")
_RsIpsecEndpointPairDecryptErrors_Type = Counter32
_RsIpsecEndpointPairDecryptErrors_Object = MibTableColumn
rsIpsecEndpointPairDecryptErrors = _RsIpsecEndpointPairDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 10),
    _RsIpsecEndpointPairDecryptErrors_Type()
)
rsIpsecEndpointPairDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairDecryptErrors.setStatus("current")
_RsIpsecEndpointPairAuthErrors_Type = Counter32
_RsIpsecEndpointPairAuthErrors_Object = MibTableColumn
rsIpsecEndpointPairAuthErrors = _RsIpsecEndpointPairAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 11),
    _RsIpsecEndpointPairAuthErrors_Type()
)
rsIpsecEndpointPairAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairAuthErrors.setStatus("current")
_RsIpsecEndpointPairReplayErrors_Type = Counter32
_RsIpsecEndpointPairReplayErrors_Object = MibTableColumn
rsIpsecEndpointPairReplayErrors = _RsIpsecEndpointPairReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 12),
    _RsIpsecEndpointPairReplayErrors_Type()
)
rsIpsecEndpointPairReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairReplayErrors.setStatus("current")
_RsIpsecEndpointPairPolicyErrors_Type = Counter32
_RsIpsecEndpointPairPolicyErrors_Object = MibTableColumn
rsIpsecEndpointPairPolicyErrors = _RsIpsecEndpointPairPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 13),
    _RsIpsecEndpointPairPolicyErrors_Type()
)
rsIpsecEndpointPairPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPolicyErrors.setStatus("current")
_RsIpsecEndpointPairPadErrors_Type = Counter32
_RsIpsecEndpointPairPadErrors_Object = MibTableColumn
rsIpsecEndpointPairPadErrors = _RsIpsecEndpointPairPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 14),
    _RsIpsecEndpointPairPadErrors_Type()
)
rsIpsecEndpointPairPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPadErrors.setStatus("current")
_RsIpsecEndpointPairOtherReceiveErrors_Type = Counter32
_RsIpsecEndpointPairOtherReceiveErrors_Object = MibTableColumn
rsIpsecEndpointPairOtherReceiveErrors = _RsIpsecEndpointPairOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 15),
    _RsIpsecEndpointPairOtherReceiveErrors_Type()
)
rsIpsecEndpointPairOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairOtherReceiveErrors.setStatus("current")
_RsIpsecEndpointPairSendErrors_Type = Counter32
_RsIpsecEndpointPairSendErrors_Object = MibTableColumn
rsIpsecEndpointPairSendErrors = _RsIpsecEndpointPairSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 16),
    _RsIpsecEndpointPairSendErrors_Type()
)
rsIpsecEndpointPairSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairSendErrors.setStatus("current")
_RsIpsecEndpointPairStatistics_ObjectIdentity = ObjectIdentity
rsIpsecEndpointPairStatistics = _RsIpsecEndpointPairStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2)
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPairStatistics.setStatus("current")
_RsIpsecEndpointPairTotalInSAs_Type = Gauge32
_RsIpsecEndpointPairTotalInSAs_Object = MibScalar
rsIpsecEndpointPairTotalInSAs = _RsIpsecEndpointPairTotalInSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 1),
    _RsIpsecEndpointPairTotalInSAs_Type()
)
rsIpsecEndpointPairTotalInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalInSAs.setStatus("current")
_RsIpsecEndpointPairTotalOutSAs_Type = Gauge32
_RsIpsecEndpointPairTotalOutSAs_Object = MibScalar
rsIpsecEndpointPairTotalOutSAs = _RsIpsecEndpointPairTotalOutSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 2),
    _RsIpsecEndpointPairTotalOutSAs_Type()
)
rsIpsecEndpointPairTotalOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalOutSAs.setStatus("current")
_RsIpsecEndpointPairTotalInAccKbytes_Type = Counter32
_RsIpsecEndpointPairTotalInAccKbytes_Object = MibScalar
rsIpsecEndpointPairTotalInAccKbytes = _RsIpsecEndpointPairTotalInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 3),
    _RsIpsecEndpointPairTotalInAccKbytes_Type()
)
rsIpsecEndpointPairTotalInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalInAccKbytes.setUnits("Kbytes")
_RsIpsecEndpointPairTotalOutAccKbytes_Type = Counter32
_RsIpsecEndpointPairTotalOutAccKbytes_Object = MibScalar
rsIpsecEndpointPairTotalOutAccKbytes = _RsIpsecEndpointPairTotalOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 4),
    _RsIpsecEndpointPairTotalOutAccKbytes_Type()
)
rsIpsecEndpointPairTotalOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalOutAccKbytes.setStatus("current")
_RsIpsecEndpointPairTotalInPackets_Type = Counter32
_RsIpsecEndpointPairTotalInPackets_Object = MibScalar
rsIpsecEndpointPairTotalInPackets = _RsIpsecEndpointPairTotalInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 5),
    _RsIpsecEndpointPairTotalInPackets_Type()
)
rsIpsecEndpointPairTotalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalInPackets.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalInPackets.setUnits("Kbytes")
_RsIpsecEndpointPairTotalOutPackets_Type = Counter32
_RsIpsecEndpointPairTotalOutPackets_Object = MibScalar
rsIpsecEndpointPairTotalOutPackets = _RsIpsecEndpointPairTotalOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 6),
    _RsIpsecEndpointPairTotalOutPackets_Type()
)
rsIpsecEndpointPairTotalOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalOutPackets.setStatus("current")
_RsIpsecEndpointPairTotalDecryptErrors_Type = Counter32
_RsIpsecEndpointPairTotalDecryptErrors_Object = MibScalar
rsIpsecEndpointPairTotalDecryptErrors = _RsIpsecEndpointPairTotalDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 7),
    _RsIpsecEndpointPairTotalDecryptErrors_Type()
)
rsIpsecEndpointPairTotalDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalDecryptErrors.setStatus("current")
_RsIpsecEndpointPairTotalAuthErrors_Type = Counter32
_RsIpsecEndpointPairTotalAuthErrors_Object = MibScalar
rsIpsecEndpointPairTotalAuthErrors = _RsIpsecEndpointPairTotalAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 8),
    _RsIpsecEndpointPairTotalAuthErrors_Type()
)
rsIpsecEndpointPairTotalAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalAuthErrors.setStatus("current")
_RsIpsecEndpointPairTotalReplayErrors_Type = Counter32
_RsIpsecEndpointPairTotalReplayErrors_Object = MibScalar
rsIpsecEndpointPairTotalReplayErrors = _RsIpsecEndpointPairTotalReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 9),
    _RsIpsecEndpointPairTotalReplayErrors_Type()
)
rsIpsecEndpointPairTotalReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalReplayErrors.setStatus("current")
_RsIpsecEndpointPairTotalPolicyErrors_Type = Counter32
_RsIpsecEndpointPairTotalPolicyErrors_Object = MibScalar
rsIpsecEndpointPairTotalPolicyErrors = _RsIpsecEndpointPairTotalPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 10),
    _RsIpsecEndpointPairTotalPolicyErrors_Type()
)
rsIpsecEndpointPairTotalPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalPolicyErrors.setStatus("current")
_RsIpsecEndpointPairTotalPadErrors_Type = Counter32
_RsIpsecEndpointPairTotalPadErrors_Object = MibScalar
rsIpsecEndpointPairTotalPadErrors = _RsIpsecEndpointPairTotalPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 11),
    _RsIpsecEndpointPairTotalPadErrors_Type()
)
rsIpsecEndpointPairTotalPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalPadErrors.setStatus("current")
_RsIpsecEndpointPairTotalOtherReceiveErrors_Type = Counter32
_RsIpsecEndpointPairTotalOtherReceiveErrors_Object = MibScalar
rsIpsecEndpointPairTotalOtherReceiveErrors = _RsIpsecEndpointPairTotalOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 12),
    _RsIpsecEndpointPairTotalOtherReceiveErrors_Type()
)
rsIpsecEndpointPairTotalOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalOtherReceiveErrors.setStatus("current")
_RsIpsecEndpointPairTotalSendErrors_Type = Counter32
_RsIpsecEndpointPairTotalSendErrors_Object = MibScalar
rsIpsecEndpointPairTotalSendErrors = _RsIpsecEndpointPairTotalSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 13),
    _RsIpsecEndpointPairTotalSendErrors_Type()
)
rsIpsecEndpointPairTotalSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairTotalSendErrors.setStatus("current")
_RsIpsecEndpointPairPeerIPToTunnel_ObjectIdentity = ObjectIdentity
rsIpsecEndpointPairPeerIPToTunnel = _RsIpsecEndpointPairPeerIPToTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 3)
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPeerIPToTunnel.setStatus("current")
_RsIpsecEndpointPairPeerIPToTunnelNum_Type = Unsigned32
_RsIpsecEndpointPairPeerIPToTunnelNum_Object = MibScalar
rsIpsecEndpointPairPeerIPToTunnelNum = _RsIpsecEndpointPairPeerIPToTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 1),
    _RsIpsecEndpointPairPeerIPToTunnelNum_Type()
)
rsIpsecEndpointPairPeerIPToTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPeerIPToTunnelNum.setStatus("current")
_RsIpsecEndpointPairPeerIPToTunnelTable_Object = MibTable
rsIpsecEndpointPairPeerIPToTunnelTable = _RsIpsecEndpointPairPeerIPToTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPeerIPToTunnelTable.setStatus("current")
_RsIpsecEndpointPairPeerIPToTunnelEntry_Object = MibTableRow
rsIpsecEndpointPairPeerIPToTunnelEntry = _RsIpsecEndpointPairPeerIPToTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1)
)
rsIpsecEndpointPairPeerIPToTunnelEntry.setIndexNames(
    (0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairPeerIPToTunnelPeerIP"),
    (0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairPeerIPToTunnelTunnelID"),
)
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPeerIPToTunnelEntry.setStatus("current")
_RsIpsecEndpointPairPeerIPToTunnelPeerIP_Type = IpAddress
_RsIpsecEndpointPairPeerIPToTunnelPeerIP_Object = MibTableColumn
rsIpsecEndpointPairPeerIPToTunnelPeerIP = _RsIpsecEndpointPairPeerIPToTunnelPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1, 1),
    _RsIpsecEndpointPairPeerIPToTunnelPeerIP_Type()
)
rsIpsecEndpointPairPeerIPToTunnelPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPeerIPToTunnelPeerIP.setStatus("current")
_RsIpsecEndpointPairPeerIPToTunnelTunnelID_Type = Integer32
_RsIpsecEndpointPairPeerIPToTunnelTunnelID_Object = MibTableColumn
rsIpsecEndpointPairPeerIPToTunnelTunnelID = _RsIpsecEndpointPairPeerIPToTunnelTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1, 2),
    _RsIpsecEndpointPairPeerIPToTunnelTunnelID_Type()
)
rsIpsecEndpointPairPeerIPToTunnelTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEndpointPairPeerIPToTunnelTunnelID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-IPSEC-ENDPOINT-PAIR-MIB",
    **{"rsIpsecEndpointPairModule": rsIpsecEndpointPairModule,
       "rsIpsecEndpointPairMIB": rsIpsecEndpointPairMIB,
       "rsIpsecEndpointPair": rsIpsecEndpointPair,
       "rsIpsecEndpointPairNum": rsIpsecEndpointPairNum,
       "rsIpsecEndpointPairTable": rsIpsecEndpointPairTable,
       "rsIpsecEndpointPairEntry": rsIpsecEndpointPairEntry,
       "rsIpsecEndpointPairIndex": rsIpsecEndpointPairIndex,
       "rsIpsecEndpointPairLocalAddr": rsIpsecEndpointPairLocalAddr,
       "rsIpsecEndpointPairPeerAddr": rsIpsecEndpointPairPeerAddr,
       "rsIpsecEndpointPairInSAs": rsIpsecEndpointPairInSAs,
       "rsIpsecEndpointPairOutSAs": rsIpsecEndpointPairOutSAs,
       "rsIpsecEndpointPairInAccKbytes": rsIpsecEndpointPairInAccKbytes,
       "rsIpsecEndpointPairOutAccKbytes": rsIpsecEndpointPairOutAccKbytes,
       "rsIpsecEndpointPairInPackets": rsIpsecEndpointPairInPackets,
       "rsIpsecEndpointPairOutPackets": rsIpsecEndpointPairOutPackets,
       "rsIpsecEndpointPairDecryptErrors": rsIpsecEndpointPairDecryptErrors,
       "rsIpsecEndpointPairAuthErrors": rsIpsecEndpointPairAuthErrors,
       "rsIpsecEndpointPairReplayErrors": rsIpsecEndpointPairReplayErrors,
       "rsIpsecEndpointPairPolicyErrors": rsIpsecEndpointPairPolicyErrors,
       "rsIpsecEndpointPairPadErrors": rsIpsecEndpointPairPadErrors,
       "rsIpsecEndpointPairOtherReceiveErrors": rsIpsecEndpointPairOtherReceiveErrors,
       "rsIpsecEndpointPairSendErrors": rsIpsecEndpointPairSendErrors,
       "rsIpsecEndpointPairStatistics": rsIpsecEndpointPairStatistics,
       "rsIpsecEndpointPairTotalInSAs": rsIpsecEndpointPairTotalInSAs,
       "rsIpsecEndpointPairTotalOutSAs": rsIpsecEndpointPairTotalOutSAs,
       "rsIpsecEndpointPairTotalInAccKbytes": rsIpsecEndpointPairTotalInAccKbytes,
       "rsIpsecEndpointPairTotalOutAccKbytes": rsIpsecEndpointPairTotalOutAccKbytes,
       "rsIpsecEndpointPairTotalInPackets": rsIpsecEndpointPairTotalInPackets,
       "rsIpsecEndpointPairTotalOutPackets": rsIpsecEndpointPairTotalOutPackets,
       "rsIpsecEndpointPairTotalDecryptErrors": rsIpsecEndpointPairTotalDecryptErrors,
       "rsIpsecEndpointPairTotalAuthErrors": rsIpsecEndpointPairTotalAuthErrors,
       "rsIpsecEndpointPairTotalReplayErrors": rsIpsecEndpointPairTotalReplayErrors,
       "rsIpsecEndpointPairTotalPolicyErrors": rsIpsecEndpointPairTotalPolicyErrors,
       "rsIpsecEndpointPairTotalPadErrors": rsIpsecEndpointPairTotalPadErrors,
       "rsIpsecEndpointPairTotalOtherReceiveErrors": rsIpsecEndpointPairTotalOtherReceiveErrors,
       "rsIpsecEndpointPairTotalSendErrors": rsIpsecEndpointPairTotalSendErrors,
       "rsIpsecEndpointPairPeerIPToTunnel": rsIpsecEndpointPairPeerIPToTunnel,
       "rsIpsecEndpointPairPeerIPToTunnelNum": rsIpsecEndpointPairPeerIPToTunnelNum,
       "rsIpsecEndpointPairPeerIPToTunnelTable": rsIpsecEndpointPairPeerIPToTunnelTable,
       "rsIpsecEndpointPairPeerIPToTunnelEntry": rsIpsecEndpointPairPeerIPToTunnelEntry,
       "rsIpsecEndpointPairPeerIPToTunnelPeerIP": rsIpsecEndpointPairPeerIPToTunnelPeerIP,
       "rsIpsecEndpointPairPeerIPToTunnelTunnelID": rsIpsecEndpointPairPeerIPToTunnelTunnelID}
)
