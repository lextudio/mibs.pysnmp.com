# SNMP MIB module (WATCHGUARD-IPSEC-ENDPOINT-PAIR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-IPSEC-ENDPOINT-PAIR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:33 2024
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

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

wgIpsecEndpointPairModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 5)
)
wgIpsecEndpointPairModule.setRevisions(
        ("2007-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgIpsecEndpointPairMIB_ObjectIdentity = ObjectIdentity
wgIpsecEndpointPairMIB = _WgIpsecEndpointPairMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1)
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPairMIB.setStatus("current")
_WgIpsecEndpointPair_ObjectIdentity = ObjectIdentity
wgIpsecEndpointPair = _WgIpsecEndpointPair_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1)
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPair.setStatus("current")
_WgIpsecEndpointPairNum_Type = Unsigned32
_WgIpsecEndpointPairNum_Object = MibScalar
wgIpsecEndpointPairNum = _WgIpsecEndpointPairNum_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 1),
    _WgIpsecEndpointPairNum_Type()
)
wgIpsecEndpointPairNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairNum.setStatus("current")
_WgIpsecEndpointPairTable_Object = MibTable
wgIpsecEndpointPairTable = _WgIpsecEndpointPairTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTable.setStatus("current")
_WgIpsecEndpointPairEntry_Object = MibTableRow
wgIpsecEndpointPairEntry = _WgIpsecEndpointPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1)
)
wgIpsecEndpointPairEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-ENDPOINT-PAIR-MIB", "wgIpsecEndpointPairIndex"),
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPairEntry.setStatus("current")
_WgIpsecEndpointPairIndex_Type = Integer32
_WgIpsecEndpointPairIndex_Object = MibTableColumn
wgIpsecEndpointPairIndex = _WgIpsecEndpointPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 1),
    _WgIpsecEndpointPairIndex_Type()
)
wgIpsecEndpointPairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairIndex.setStatus("current")
_WgIpsecEndpointPairLocalAddr_Type = IpAddress
_WgIpsecEndpointPairLocalAddr_Object = MibTableColumn
wgIpsecEndpointPairLocalAddr = _WgIpsecEndpointPairLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 2),
    _WgIpsecEndpointPairLocalAddr_Type()
)
wgIpsecEndpointPairLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairLocalAddr.setStatus("current")
_WgIpsecEndpointPairPeerAddr_Type = IpAddress
_WgIpsecEndpointPairPeerAddr_Object = MibTableColumn
wgIpsecEndpointPairPeerAddr = _WgIpsecEndpointPairPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 3),
    _WgIpsecEndpointPairPeerAddr_Type()
)
wgIpsecEndpointPairPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPeerAddr.setStatus("current")
_WgIpsecEndpointPairInSAs_Type = Unsigned32
_WgIpsecEndpointPairInSAs_Object = MibTableColumn
wgIpsecEndpointPairInSAs = _WgIpsecEndpointPairInSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 4),
    _WgIpsecEndpointPairInSAs_Type()
)
wgIpsecEndpointPairInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairInSAs.setStatus("current")
_WgIpsecEndpointPairOutSAs_Type = Unsigned32
_WgIpsecEndpointPairOutSAs_Object = MibTableColumn
wgIpsecEndpointPairOutSAs = _WgIpsecEndpointPairOutSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 5),
    _WgIpsecEndpointPairOutSAs_Type()
)
wgIpsecEndpointPairOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairOutSAs.setStatus("current")
_WgIpsecEndpointPairInAccKbytes_Type = Counter32
_WgIpsecEndpointPairInAccKbytes_Object = MibTableColumn
wgIpsecEndpointPairInAccKbytes = _WgIpsecEndpointPairInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 6),
    _WgIpsecEndpointPairInAccKbytes_Type()
)
wgIpsecEndpointPairInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairInAccKbytes.setUnits("Kbytes")
_WgIpsecEndpointPairOutAccKbytes_Type = Counter32
_WgIpsecEndpointPairOutAccKbytes_Object = MibTableColumn
wgIpsecEndpointPairOutAccKbytes = _WgIpsecEndpointPairOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 7),
    _WgIpsecEndpointPairOutAccKbytes_Type()
)
wgIpsecEndpointPairOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairOutAccKbytes.setUnits("Kbytes")
_WgIpsecEndpointPairInPackets_Type = Counter32
_WgIpsecEndpointPairInPackets_Object = MibTableColumn
wgIpsecEndpointPairInPackets = _WgIpsecEndpointPairInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 8),
    _WgIpsecEndpointPairInPackets_Type()
)
wgIpsecEndpointPairInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairInPackets.setStatus("current")
_WgIpsecEndpointPairOutPackets_Type = Counter32
_WgIpsecEndpointPairOutPackets_Object = MibTableColumn
wgIpsecEndpointPairOutPackets = _WgIpsecEndpointPairOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 9),
    _WgIpsecEndpointPairOutPackets_Type()
)
wgIpsecEndpointPairOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairOutPackets.setStatus("current")
_WgIpsecEndpointPairDecryptErrors_Type = Counter32
_WgIpsecEndpointPairDecryptErrors_Object = MibTableColumn
wgIpsecEndpointPairDecryptErrors = _WgIpsecEndpointPairDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 10),
    _WgIpsecEndpointPairDecryptErrors_Type()
)
wgIpsecEndpointPairDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairDecryptErrors.setStatus("current")
_WgIpsecEndpointPairAuthErrors_Type = Counter32
_WgIpsecEndpointPairAuthErrors_Object = MibTableColumn
wgIpsecEndpointPairAuthErrors = _WgIpsecEndpointPairAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 11),
    _WgIpsecEndpointPairAuthErrors_Type()
)
wgIpsecEndpointPairAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairAuthErrors.setStatus("current")
_WgIpsecEndpointPairReplayErrors_Type = Counter32
_WgIpsecEndpointPairReplayErrors_Object = MibTableColumn
wgIpsecEndpointPairReplayErrors = _WgIpsecEndpointPairReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 12),
    _WgIpsecEndpointPairReplayErrors_Type()
)
wgIpsecEndpointPairReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairReplayErrors.setStatus("current")
_WgIpsecEndpointPairPolicyErrors_Type = Counter32
_WgIpsecEndpointPairPolicyErrors_Object = MibTableColumn
wgIpsecEndpointPairPolicyErrors = _WgIpsecEndpointPairPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 13),
    _WgIpsecEndpointPairPolicyErrors_Type()
)
wgIpsecEndpointPairPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPolicyErrors.setStatus("current")
_WgIpsecEndpointPairPadErrors_Type = Counter32
_WgIpsecEndpointPairPadErrors_Object = MibTableColumn
wgIpsecEndpointPairPadErrors = _WgIpsecEndpointPairPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 14),
    _WgIpsecEndpointPairPadErrors_Type()
)
wgIpsecEndpointPairPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPadErrors.setStatus("current")
_WgIpsecEndpointPairOtherReceiveErrors_Type = Counter32
_WgIpsecEndpointPairOtherReceiveErrors_Object = MibTableColumn
wgIpsecEndpointPairOtherReceiveErrors = _WgIpsecEndpointPairOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 15),
    _WgIpsecEndpointPairOtherReceiveErrors_Type()
)
wgIpsecEndpointPairOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairOtherReceiveErrors.setStatus("current")
_WgIpsecEndpointPairSendErrors_Type = Counter32
_WgIpsecEndpointPairSendErrors_Object = MibTableColumn
wgIpsecEndpointPairSendErrors = _WgIpsecEndpointPairSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 1, 2, 1, 16),
    _WgIpsecEndpointPairSendErrors_Type()
)
wgIpsecEndpointPairSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairSendErrors.setStatus("current")
_WgIpsecEndpointPairStatistics_ObjectIdentity = ObjectIdentity
wgIpsecEndpointPairStatistics = _WgIpsecEndpointPairStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2)
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPairStatistics.setStatus("current")
_WgIpsecEndpointPairTotalInSAs_Type = Gauge32
_WgIpsecEndpointPairTotalInSAs_Object = MibScalar
wgIpsecEndpointPairTotalInSAs = _WgIpsecEndpointPairTotalInSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 1),
    _WgIpsecEndpointPairTotalInSAs_Type()
)
wgIpsecEndpointPairTotalInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalInSAs.setStatus("current")
_WgIpsecEndpointPairTotalOutSAs_Type = Gauge32
_WgIpsecEndpointPairTotalOutSAs_Object = MibScalar
wgIpsecEndpointPairTotalOutSAs = _WgIpsecEndpointPairTotalOutSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 2),
    _WgIpsecEndpointPairTotalOutSAs_Type()
)
wgIpsecEndpointPairTotalOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalOutSAs.setStatus("current")
_WgIpsecEndpointPairTotalInAccKbytes_Type = Counter32
_WgIpsecEndpointPairTotalInAccKbytes_Object = MibScalar
wgIpsecEndpointPairTotalInAccKbytes = _WgIpsecEndpointPairTotalInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 3),
    _WgIpsecEndpointPairTotalInAccKbytes_Type()
)
wgIpsecEndpointPairTotalInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalInAccKbytes.setUnits("Kbytes")
_WgIpsecEndpointPairTotalOutAccKbytes_Type = Counter32
_WgIpsecEndpointPairTotalOutAccKbytes_Object = MibScalar
wgIpsecEndpointPairTotalOutAccKbytes = _WgIpsecEndpointPairTotalOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 4),
    _WgIpsecEndpointPairTotalOutAccKbytes_Type()
)
wgIpsecEndpointPairTotalOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalOutAccKbytes.setStatus("current")
_WgIpsecEndpointPairTotalInPackets_Type = Counter32
_WgIpsecEndpointPairTotalInPackets_Object = MibScalar
wgIpsecEndpointPairTotalInPackets = _WgIpsecEndpointPairTotalInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 5),
    _WgIpsecEndpointPairTotalInPackets_Type()
)
wgIpsecEndpointPairTotalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalInPackets.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalInPackets.setUnits("Kbytes")
_WgIpsecEndpointPairTotalOutPackets_Type = Counter32
_WgIpsecEndpointPairTotalOutPackets_Object = MibScalar
wgIpsecEndpointPairTotalOutPackets = _WgIpsecEndpointPairTotalOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 6),
    _WgIpsecEndpointPairTotalOutPackets_Type()
)
wgIpsecEndpointPairTotalOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalOutPackets.setStatus("current")
_WgIpsecEndpointPairTotalDecryptErrors_Type = Counter32
_WgIpsecEndpointPairTotalDecryptErrors_Object = MibScalar
wgIpsecEndpointPairTotalDecryptErrors = _WgIpsecEndpointPairTotalDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 7),
    _WgIpsecEndpointPairTotalDecryptErrors_Type()
)
wgIpsecEndpointPairTotalDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalDecryptErrors.setStatus("current")
_WgIpsecEndpointPairTotalAuthErrors_Type = Counter32
_WgIpsecEndpointPairTotalAuthErrors_Object = MibScalar
wgIpsecEndpointPairTotalAuthErrors = _WgIpsecEndpointPairTotalAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 8),
    _WgIpsecEndpointPairTotalAuthErrors_Type()
)
wgIpsecEndpointPairTotalAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalAuthErrors.setStatus("current")
_WgIpsecEndpointPairTotalReplayErrors_Type = Counter32
_WgIpsecEndpointPairTotalReplayErrors_Object = MibScalar
wgIpsecEndpointPairTotalReplayErrors = _WgIpsecEndpointPairTotalReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 9),
    _WgIpsecEndpointPairTotalReplayErrors_Type()
)
wgIpsecEndpointPairTotalReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalReplayErrors.setStatus("current")
_WgIpsecEndpointPairTotalPolicyErrors_Type = Counter32
_WgIpsecEndpointPairTotalPolicyErrors_Object = MibScalar
wgIpsecEndpointPairTotalPolicyErrors = _WgIpsecEndpointPairTotalPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 10),
    _WgIpsecEndpointPairTotalPolicyErrors_Type()
)
wgIpsecEndpointPairTotalPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalPolicyErrors.setStatus("current")
_WgIpsecEndpointPairTotalPadErrors_Type = Counter32
_WgIpsecEndpointPairTotalPadErrors_Object = MibScalar
wgIpsecEndpointPairTotalPadErrors = _WgIpsecEndpointPairTotalPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 11),
    _WgIpsecEndpointPairTotalPadErrors_Type()
)
wgIpsecEndpointPairTotalPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalPadErrors.setStatus("current")
_WgIpsecEndpointPairTotalOtherReceiveErrors_Type = Counter32
_WgIpsecEndpointPairTotalOtherReceiveErrors_Object = MibScalar
wgIpsecEndpointPairTotalOtherReceiveErrors = _WgIpsecEndpointPairTotalOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 12),
    _WgIpsecEndpointPairTotalOtherReceiveErrors_Type()
)
wgIpsecEndpointPairTotalOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalOtherReceiveErrors.setStatus("current")
_WgIpsecEndpointPairTotalSendErrors_Type = Counter32
_WgIpsecEndpointPairTotalSendErrors_Object = MibScalar
wgIpsecEndpointPairTotalSendErrors = _WgIpsecEndpointPairTotalSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 2, 13),
    _WgIpsecEndpointPairTotalSendErrors_Type()
)
wgIpsecEndpointPairTotalSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairTotalSendErrors.setStatus("current")
_WgIpsecEndpointPairPeerIPToTunnel_ObjectIdentity = ObjectIdentity
wgIpsecEndpointPairPeerIPToTunnel = _WgIpsecEndpointPairPeerIPToTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 3)
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPeerIPToTunnel.setStatus("current")
_WgIpsecEndpointPairPeerIPToTunnelNum_Type = Unsigned32
_WgIpsecEndpointPairPeerIPToTunnelNum_Object = MibScalar
wgIpsecEndpointPairPeerIPToTunnelNum = _WgIpsecEndpointPairPeerIPToTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 3, 1),
    _WgIpsecEndpointPairPeerIPToTunnelNum_Type()
)
wgIpsecEndpointPairPeerIPToTunnelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPeerIPToTunnelNum.setStatus("current")
_WgIpsecEndpointPairPeerIPToTunnelTable_Object = MibTable
wgIpsecEndpointPairPeerIPToTunnelTable = _WgIpsecEndpointPairPeerIPToTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPeerIPToTunnelTable.setStatus("current")
_WgIpsecEndpointPairPeerIPToTunnelEntry_Object = MibTableRow
wgIpsecEndpointPairPeerIPToTunnelEntry = _WgIpsecEndpointPairPeerIPToTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 3, 2, 1)
)
wgIpsecEndpointPairPeerIPToTunnelEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-ENDPOINT-PAIR-MIB", "wgIpsecEndpointPairPeerIPToTunnelPeerIP"),
    (0, "WATCHGUARD-IPSEC-ENDPOINT-PAIR-MIB", "wgIpsecEndpointPairPeerIPToTunnelTunnelID"),
)
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPeerIPToTunnelEntry.setStatus("current")
_WgIpsecEndpointPairPeerIPToTunnelPeerIP_Type = IpAddress
_WgIpsecEndpointPairPeerIPToTunnelPeerIP_Object = MibTableColumn
wgIpsecEndpointPairPeerIPToTunnelPeerIP = _WgIpsecEndpointPairPeerIPToTunnelPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 3, 2, 1, 1),
    _WgIpsecEndpointPairPeerIPToTunnelPeerIP_Type()
)
wgIpsecEndpointPairPeerIPToTunnelPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPeerIPToTunnelPeerIP.setStatus("current")
_WgIpsecEndpointPairPeerIPToTunnelTunnelID_Type = Integer32
_WgIpsecEndpointPairPeerIPToTunnelTunnelID_Object = MibTableColumn
wgIpsecEndpointPairPeerIPToTunnelTunnelID = _WgIpsecEndpointPairPeerIPToTunnelTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 3097, 5, 1, 3, 2, 1, 2),
    _WgIpsecEndpointPairPeerIPToTunnelTunnelID_Type()
)
wgIpsecEndpointPairPeerIPToTunnelTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEndpointPairPeerIPToTunnelTunnelID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-IPSEC-ENDPOINT-PAIR-MIB",
    **{"wgIpsecEndpointPairModule": wgIpsecEndpointPairModule,
       "wgIpsecEndpointPairMIB": wgIpsecEndpointPairMIB,
       "wgIpsecEndpointPair": wgIpsecEndpointPair,
       "wgIpsecEndpointPairNum": wgIpsecEndpointPairNum,
       "wgIpsecEndpointPairTable": wgIpsecEndpointPairTable,
       "wgIpsecEndpointPairEntry": wgIpsecEndpointPairEntry,
       "wgIpsecEndpointPairIndex": wgIpsecEndpointPairIndex,
       "wgIpsecEndpointPairLocalAddr": wgIpsecEndpointPairLocalAddr,
       "wgIpsecEndpointPairPeerAddr": wgIpsecEndpointPairPeerAddr,
       "wgIpsecEndpointPairInSAs": wgIpsecEndpointPairInSAs,
       "wgIpsecEndpointPairOutSAs": wgIpsecEndpointPairOutSAs,
       "wgIpsecEndpointPairInAccKbytes": wgIpsecEndpointPairInAccKbytes,
       "wgIpsecEndpointPairOutAccKbytes": wgIpsecEndpointPairOutAccKbytes,
       "wgIpsecEndpointPairInPackets": wgIpsecEndpointPairInPackets,
       "wgIpsecEndpointPairOutPackets": wgIpsecEndpointPairOutPackets,
       "wgIpsecEndpointPairDecryptErrors": wgIpsecEndpointPairDecryptErrors,
       "wgIpsecEndpointPairAuthErrors": wgIpsecEndpointPairAuthErrors,
       "wgIpsecEndpointPairReplayErrors": wgIpsecEndpointPairReplayErrors,
       "wgIpsecEndpointPairPolicyErrors": wgIpsecEndpointPairPolicyErrors,
       "wgIpsecEndpointPairPadErrors": wgIpsecEndpointPairPadErrors,
       "wgIpsecEndpointPairOtherReceiveErrors": wgIpsecEndpointPairOtherReceiveErrors,
       "wgIpsecEndpointPairSendErrors": wgIpsecEndpointPairSendErrors,
       "wgIpsecEndpointPairStatistics": wgIpsecEndpointPairStatistics,
       "wgIpsecEndpointPairTotalInSAs": wgIpsecEndpointPairTotalInSAs,
       "wgIpsecEndpointPairTotalOutSAs": wgIpsecEndpointPairTotalOutSAs,
       "wgIpsecEndpointPairTotalInAccKbytes": wgIpsecEndpointPairTotalInAccKbytes,
       "wgIpsecEndpointPairTotalOutAccKbytes": wgIpsecEndpointPairTotalOutAccKbytes,
       "wgIpsecEndpointPairTotalInPackets": wgIpsecEndpointPairTotalInPackets,
       "wgIpsecEndpointPairTotalOutPackets": wgIpsecEndpointPairTotalOutPackets,
       "wgIpsecEndpointPairTotalDecryptErrors": wgIpsecEndpointPairTotalDecryptErrors,
       "wgIpsecEndpointPairTotalAuthErrors": wgIpsecEndpointPairTotalAuthErrors,
       "wgIpsecEndpointPairTotalReplayErrors": wgIpsecEndpointPairTotalReplayErrors,
       "wgIpsecEndpointPairTotalPolicyErrors": wgIpsecEndpointPairTotalPolicyErrors,
       "wgIpsecEndpointPairTotalPadErrors": wgIpsecEndpointPairTotalPadErrors,
       "wgIpsecEndpointPairTotalOtherReceiveErrors": wgIpsecEndpointPairTotalOtherReceiveErrors,
       "wgIpsecEndpointPairTotalSendErrors": wgIpsecEndpointPairTotalSendErrors,
       "wgIpsecEndpointPairPeerIPToTunnel": wgIpsecEndpointPairPeerIPToTunnel,
       "wgIpsecEndpointPairPeerIPToTunnelNum": wgIpsecEndpointPairPeerIPToTunnelNum,
       "wgIpsecEndpointPairPeerIPToTunnelTable": wgIpsecEndpointPairPeerIPToTunnelTable,
       "wgIpsecEndpointPairPeerIPToTunnelEntry": wgIpsecEndpointPairPeerIPToTunnelEntry,
       "wgIpsecEndpointPairPeerIPToTunnelPeerIP": wgIpsecEndpointPairPeerIPToTunnelPeerIP,
       "wgIpsecEndpointPairPeerIPToTunnelTunnelID": wgIpsecEndpointPairPeerIPToTunnelTunnelID}
)
