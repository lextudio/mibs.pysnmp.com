# SNMP MIB module (SONOMASYSTEMS-SONOMA-IPPROP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-IPPROP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:45 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(sonomaRouting,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaRouting")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpRouting_ObjectIdentity = ObjectIdentity
ipRouting = _IpRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1)
)


class _IpRIPState_Type(Integer32):
    """Custom type ipRIPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpRIPState_Type.__name__ = "Integer32"
_IpRIPState_Object = MibScalar
ipRIPState = _IpRIPState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 1),
    _IpRIPState_Type()
)
ipRIPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRIPState.setStatus("mandatory")


class _IpSecurity_Type(Integer32):
    """Custom type ipSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpSecurity_Type.__name__ = "Integer32"
_IpSecurity_Object = MibScalar
ipSecurity = _IpSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 2),
    _IpSecurity_Type()
)
ipSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurity.setStatus("mandatory")
_IpPortConfigTable_Object = MibTable
ipPortConfigTable = _IpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3)
)
if mibBuilder.loadTexts:
    ipPortConfigTable.setStatus("mandatory")
_IpPortConfigEntry_Object = MibTableRow
ipPortConfigEntry = _IpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1)
)
ipPortConfigEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-IPPROP-MIB", "ipPortConfigIndex"),
)
if mibBuilder.loadTexts:
    ipPortConfigEntry.setStatus("mandatory")
_IpPortConfigIndex_Type = Integer32
_IpPortConfigIndex_Object = MibTableColumn
ipPortConfigIndex = _IpPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1, 1),
    _IpPortConfigIndex_Type()
)
ipPortConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPortConfigIndex.setStatus("mandatory")


class _IpPortForwarding_Type(Integer32):
    """Custom type ipPortForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpPortForwarding_Type.__name__ = "Integer32"
_IpPortForwarding_Object = MibTableColumn
ipPortForwarding = _IpPortForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1, 2),
    _IpPortForwarding_Type()
)
ipPortForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortForwarding.setStatus("mandatory")


class _IpPortMACEncapsulation_Type(Integer32):
    """Custom type ipPortMACEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("fddiSnap", 6),
          ("ieee8023", 3),
          ("noencap", 1),
          ("tokenRing", 4),
          ("tokenRingSnap", 5))
    )


_IpPortMACEncapsulation_Type.__name__ = "Integer32"
_IpPortMACEncapsulation_Object = MibTableColumn
ipPortMACEncapsulation = _IpPortMACEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1, 3),
    _IpPortMACEncapsulation_Type()
)
ipPortMACEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortMACEncapsulation.setStatus("mandatory")


class _IpPortDisposition_Type(Integer32):
    """Custom type ipPortDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("discard", 2))
    )


_IpPortDisposition_Type.__name__ = "Integer32"
_IpPortDisposition_Object = MibTableColumn
ipPortDisposition = _IpPortDisposition_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1, 4),
    _IpPortDisposition_Type()
)
ipPortDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortDisposition.setStatus("mandatory")
_IpPortMTU_Type = Integer32
_IpPortMTU_Object = MibTableColumn
ipPortMTU = _IpPortMTU_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1, 5),
    _IpPortMTU_Type()
)
ipPortMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortMTU.setStatus("mandatory")
_IpPortDefaultGateway_Type = IpAddress
_IpPortDefaultGateway_Object = MibTableColumn
ipPortDefaultGateway = _IpPortDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1, 6),
    _IpPortDefaultGateway_Type()
)
ipPortDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortDefaultGateway.setStatus("mandatory")
_IpPortDefaultGatewayLP_Type = Integer32
_IpPortDefaultGatewayLP_Object = MibTableColumn
ipPortDefaultGatewayLP = _IpPortDefaultGatewayLP_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 3, 1, 7),
    _IpPortDefaultGatewayLP_Type()
)
ipPortDefaultGatewayLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortDefaultGatewayLP.setStatus("mandatory")
_IpPortAddrTable_Object = MibTable
ipPortAddrTable = _IpPortAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ipPortAddrTable.setStatus("mandatory")
_IpPortAddrEntry_Object = MibTableRow
ipPortAddrEntry = _IpPortAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 4, 1)
)
ipPortAddrEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-IPPROP-MIB", "ipPortAddrIndex"),
    (0, "SONOMASYSTEMS-SONOMA-IPPROP-MIB", "ipPortIpAddress"),
)
if mibBuilder.loadTexts:
    ipPortAddrEntry.setStatus("mandatory")
_IpPortAddrIndex_Type = Integer32
_IpPortAddrIndex_Object = MibTableColumn
ipPortAddrIndex = _IpPortAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 4, 1, 1),
    _IpPortAddrIndex_Type()
)
ipPortAddrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortAddrIndex.setStatus("mandatory")
_IpPortIpAddress_Type = IpAddress
_IpPortIpAddress_Object = MibTableColumn
ipPortIpAddress = _IpPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 4, 1, 2),
    _IpPortIpAddress_Type()
)
ipPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortIpAddress.setStatus("mandatory")
_IpPortIpAddressMask_Type = IpAddress
_IpPortIpAddressMask_Object = MibTableColumn
ipPortIpAddressMask = _IpPortIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 4, 1, 3),
    _IpPortIpAddressMask_Type()
)
ipPortIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortIpAddressMask.setStatus("mandatory")


class _IpPortAddrType_Type(Integer32):
    """Custom type ipPortAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IpPortAddrType_Type.__name__ = "Integer32"
_IpPortAddrType_Object = MibTableColumn
ipPortAddrType = _IpPortAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 4, 1, 4),
    _IpPortAddrType_Type()
)
ipPortAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPortAddrType.setStatus("mandatory")
_IpAccessViolations_Type = Counter32
_IpAccessViolations_Object = MibScalar
ipAccessViolations = _IpAccessViolations_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 5),
    _IpAccessViolations_Type()
)
ipAccessViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAccessViolations.setStatus("mandatory")
_IpOtherDiscards_Type = Counter32
_IpOtherDiscards_Object = MibScalar
ipOtherDiscards = _IpOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 6),
    _IpOtherDiscards_Type()
)
ipOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOtherDiscards.setStatus("mandatory")
_IpOutTransmits_Type = Counter32
_IpOutTransmits_Object = MibScalar
ipOutTransmits = _IpOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 7),
    _IpOutTransmits_Type()
)
ipOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutTransmits.setStatus("mandatory")


class _IpRelay_Type(Integer32):
    """Custom type ipRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpRelay_Type.__name__ = "Integer32"
_IpRelay_Object = MibScalar
ipRelay = _IpRelay_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 8),
    _IpRelay_Type()
)
ipRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRelay.setStatus("mandatory")
_IpRelayServerTable_Object = MibTable
ipRelayServerTable = _IpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 9)
)
if mibBuilder.loadTexts:
    ipRelayServerTable.setStatus("mandatory")
_IpRelayServerEntry_Object = MibTableRow
ipRelayServerEntry = _IpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 9, 1)
)
ipRelayServerEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-IPPROP-MIB", "ipRelayServerAddress"),
)
if mibBuilder.loadTexts:
    ipRelayServerEntry.setStatus("mandatory")
_IpRelayServerAddress_Type = IpAddress
_IpRelayServerAddress_Object = MibTableColumn
ipRelayServerAddress = _IpRelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 9, 1, 1),
    _IpRelayServerAddress_Type()
)
ipRelayServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRelayServerAddress.setStatus("mandatory")


class _IpRelayServerStatus_Type(Integer32):
    """Custom type ipRelayServerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IpRelayServerStatus_Type.__name__ = "Integer32"
_IpRelayServerStatus_Object = MibTableColumn
ipRelayServerStatus = _IpRelayServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 9, 1, 2),
    _IpRelayServerStatus_Type()
)
ipRelayServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRelayServerStatus.setStatus("mandatory")


class _IpDhcpClient_Type(Integer32):
    """Custom type ipDhcpClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpDhcpClient_Type.__name__ = "Integer32"
_IpDhcpClient_Object = MibScalar
ipDhcpClient = _IpDhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 10),
    _IpDhcpClient_Type()
)
ipDhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpClient.setStatus("mandatory")
_IpCounters_ObjectIdentity = ObjectIdentity
ipCounters = _IpCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11)
)
_IpInternalReceived_Type = Counter32
_IpInternalReceived_Object = MibScalar
ipInternalReceived = _IpInternalReceived_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 1),
    _IpInternalReceived_Type()
)
ipInternalReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInternalReceived.setStatus("mandatory")
_IpLoopback_Type = Counter32
_IpLoopback_Object = MibScalar
ipLoopback = _IpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 2),
    _IpLoopback_Type()
)
ipLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLoopback.setStatus("mandatory")
_IpNonFastPath_Type = Counter32
_IpNonFastPath_Object = MibScalar
ipNonFastPath = _IpNonFastPath_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 3),
    _IpNonFastPath_Type()
)
ipNonFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNonFastPath.setStatus("mandatory")
_IpBackgroundPath_Type = Counter32
_IpBackgroundPath_Object = MibScalar
ipBackgroundPath = _IpBackgroundPath_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 4),
    _IpBackgroundPath_Type()
)
ipBackgroundPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBackgroundPath.setStatus("mandatory")
_IpNotForwarding_Type = Counter32
_IpNotForwarding_Object = MibScalar
ipNotForwarding = _IpNotForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 5),
    _IpNotForwarding_Type()
)
ipNotForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNotForwarding.setStatus("mandatory")
_IpVlanMismatch_Type = Counter32
_IpVlanMismatch_Object = MibScalar
ipVlanMismatch = _IpVlanMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 6),
    _IpVlanMismatch_Type()
)
ipVlanMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipVlanMismatch.setStatus("mandatory")
_IpShortHeader_Type = Counter32
_IpShortHeader_Object = MibScalar
ipShortHeader = _IpShortHeader_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 7),
    _IpShortHeader_Type()
)
ipShortHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipShortHeader.setStatus("mandatory")
_IpHeaderLengthError_Type = Counter32
_IpHeaderLengthError_Object = MibScalar
ipHeaderLengthError = _IpHeaderLengthError_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 8),
    _IpHeaderLengthError_Type()
)
ipHeaderLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipHeaderLengthError.setStatus("mandatory")
_IpVersionError_Type = Counter32
_IpVersionError_Object = MibScalar
ipVersionError = _IpVersionError_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 9),
    _IpVersionError_Type()
)
ipVersionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipVersionError.setStatus("mandatory")
_IpCsumError_Type = Counter32
_IpCsumError_Object = MibScalar
ipCsumError = _IpCsumError_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 10),
    _IpCsumError_Type()
)
ipCsumError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCsumError.setStatus("mandatory")
_IpFwdFormatError_Type = Counter32
_IpFwdFormatError_Object = MibScalar
ipFwdFormatError = _IpFwdFormatError_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 11),
    _IpFwdFormatError_Type()
)
ipFwdFormatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdFormatError.setStatus("mandatory")
_IpConvFailedInbound_Type = Counter32
_IpConvFailedInbound_Object = MibScalar
ipConvFailedInbound = _IpConvFailedInbound_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 12),
    _IpConvFailedInbound_Type()
)
ipConvFailedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipConvFailedInbound.setStatus("mandatory")
_IpConvFailedOutbound_Type = Counter32
_IpConvFailedOutbound_Object = MibScalar
ipConvFailedOutbound = _IpConvFailedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 13),
    _IpConvFailedOutbound_Type()
)
ipConvFailedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipConvFailedOutbound.setStatus("mandatory")
_IpArpRequestsSent_Type = Counter32
_IpArpRequestsSent_Object = MibScalar
ipArpRequestsSent = _IpArpRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 14),
    _IpArpRequestsSent_Type()
)
ipArpRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipArpRequestsSent.setStatus("mandatory")
_IpArpRepliesSent_Type = Counter32
_IpArpRepliesSent_Object = MibScalar
ipArpRepliesSent = _IpArpRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 15),
    _IpArpRepliesSent_Type()
)
ipArpRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipArpRepliesSent.setStatus("mandatory")
_IpArpRequestsRecv_Type = Counter32
_IpArpRequestsRecv_Object = MibScalar
ipArpRequestsRecv = _IpArpRequestsRecv_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 16),
    _IpArpRequestsRecv_Type()
)
ipArpRequestsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipArpRequestsRecv.setStatus("mandatory")
_IpArpRepliesRecv_Type = Counter32
_IpArpRepliesRecv_Object = MibScalar
ipArpRepliesRecv = _IpArpRepliesRecv_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 17),
    _IpArpRepliesRecv_Type()
)
ipArpRepliesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipArpRepliesRecv.setStatus("mandatory")
_IpArpQueueSatisfied_Type = Counter32
_IpArpQueueSatisfied_Object = MibScalar
ipArpQueueSatisfied = _IpArpQueueSatisfied_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 18),
    _IpArpQueueSatisfied_Type()
)
ipArpQueueSatisfied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipArpQueueSatisfied.setStatus("mandatory")
_IpArpQueueDropped_Type = Counter32
_IpArpQueueDropped_Object = MibScalar
ipArpQueueDropped = _IpArpQueueDropped_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 19),
    _IpArpQueueDropped_Type()
)
ipArpQueueDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipArpQueueDropped.setStatus("mandatory")
_IpArpNotQueuedLimit_Type = Counter32
_IpArpNotQueuedLimit_Object = MibScalar
ipArpNotQueuedLimit = _IpArpNotQueuedLimit_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 20),
    _IpArpNotQueuedLimit_Type()
)
ipArpNotQueuedLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipArpNotQueuedLimit.setStatus("mandatory")
_IpRequestsThrottled_Type = Counter32
_IpRequestsThrottled_Object = MibScalar
ipRequestsThrottled = _IpRequestsThrottled_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 21),
    _IpRequestsThrottled_Type()
)
ipRequestsThrottled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRequestsThrottled.setStatus("mandatory")
_IpRequestsThrottledLastSecond_Type = Counter32
_IpRequestsThrottledLastSecond_Object = MibScalar
ipRequestsThrottledLastSecond = _IpRequestsThrottledLastSecond_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 11, 22),
    _IpRequestsThrottledLastSecond_Type()
)
ipRequestsThrottledLastSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRequestsThrottledLastSecond.setStatus("mandatory")
_IpParameters_ObjectIdentity = ObjectIdentity
ipParameters = _IpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 12)
)


class _IpparamBackwardingThrottle_Type(Integer32):
    """Custom type ipparamBackwardingThrottle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 64000),
    )


_IpparamBackwardingThrottle_Type.__name__ = "Integer32"
_IpparamBackwardingThrottle_Object = MibScalar
ipparamBackwardingThrottle = _IpparamBackwardingThrottle_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 4, 1, 12, 1),
    _IpparamBackwardingThrottle_Type()
)
ipparamBackwardingThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipparamBackwardingThrottle.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-IPPROP-MIB",
    **{"ipRouting": ipRouting,
       "ipRIPState": ipRIPState,
       "ipSecurity": ipSecurity,
       "ipPortConfigTable": ipPortConfigTable,
       "ipPortConfigEntry": ipPortConfigEntry,
       "ipPortConfigIndex": ipPortConfigIndex,
       "ipPortForwarding": ipPortForwarding,
       "ipPortMACEncapsulation": ipPortMACEncapsulation,
       "ipPortDisposition": ipPortDisposition,
       "ipPortMTU": ipPortMTU,
       "ipPortDefaultGateway": ipPortDefaultGateway,
       "ipPortDefaultGatewayLP": ipPortDefaultGatewayLP,
       "ipPortAddrTable": ipPortAddrTable,
       "ipPortAddrEntry": ipPortAddrEntry,
       "ipPortAddrIndex": ipPortAddrIndex,
       "ipPortIpAddress": ipPortIpAddress,
       "ipPortIpAddressMask": ipPortIpAddressMask,
       "ipPortAddrType": ipPortAddrType,
       "ipAccessViolations": ipAccessViolations,
       "ipOtherDiscards": ipOtherDiscards,
       "ipOutTransmits": ipOutTransmits,
       "ipRelay": ipRelay,
       "ipRelayServerTable": ipRelayServerTable,
       "ipRelayServerEntry": ipRelayServerEntry,
       "ipRelayServerAddress": ipRelayServerAddress,
       "ipRelayServerStatus": ipRelayServerStatus,
       "ipDhcpClient": ipDhcpClient,
       "ipCounters": ipCounters,
       "ipInternalReceived": ipInternalReceived,
       "ipLoopback": ipLoopback,
       "ipNonFastPath": ipNonFastPath,
       "ipBackgroundPath": ipBackgroundPath,
       "ipNotForwarding": ipNotForwarding,
       "ipVlanMismatch": ipVlanMismatch,
       "ipShortHeader": ipShortHeader,
       "ipHeaderLengthError": ipHeaderLengthError,
       "ipVersionError": ipVersionError,
       "ipCsumError": ipCsumError,
       "ipFwdFormatError": ipFwdFormatError,
       "ipConvFailedInbound": ipConvFailedInbound,
       "ipConvFailedOutbound": ipConvFailedOutbound,
       "ipArpRequestsSent": ipArpRequestsSent,
       "ipArpRepliesSent": ipArpRepliesSent,
       "ipArpRequestsRecv": ipArpRequestsRecv,
       "ipArpRepliesRecv": ipArpRepliesRecv,
       "ipArpQueueSatisfied": ipArpQueueSatisfied,
       "ipArpQueueDropped": ipArpQueueDropped,
       "ipArpNotQueuedLimit": ipArpNotQueuedLimit,
       "ipRequestsThrottled": ipRequestsThrottled,
       "ipRequestsThrottledLastSecond": ipRequestsThrottledLastSecond,
       "ipParameters": ipParameters,
       "ipparamBackwardingThrottle": ipparamBackwardingThrottle}
)
