# SNMP MIB module (BAS-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-DHCP-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:23 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 BasSubnetClass,
 basDhcpRelay) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "BasSubnetClass",
    "basDhcpRelay")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

basDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasDhcpRelayTable_Object = MibTable
basDhcpRelayTable = _BasDhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1)
)
if mibBuilder.loadTexts:
    basDhcpRelayTable.setStatus("current")
_BasDhcpRelayEntry_Object = MibTableRow
basDhcpRelayEntry = _BasDhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1)
)
basDhcpRelayEntry.setIndexNames(
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayChassis"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelaySlot"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayIf"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayLPort"),
)
if mibBuilder.loadTexts:
    basDhcpRelayEntry.setStatus("current")
_BasDhcpRelayChassis_Type = BasChassisId
_BasDhcpRelayChassis_Object = MibTableColumn
basDhcpRelayChassis = _BasDhcpRelayChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 1),
    _BasDhcpRelayChassis_Type()
)
basDhcpRelayChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayChassis.setStatus("current")
_BasDhcpRelaySlot_Type = BasSlotId
_BasDhcpRelaySlot_Object = MibTableColumn
basDhcpRelaySlot = _BasDhcpRelaySlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 2),
    _BasDhcpRelaySlot_Type()
)
basDhcpRelaySlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelaySlot.setStatus("current")
_BasDhcpRelayIf_Type = BasInterfaceId
_BasDhcpRelayIf_Object = MibTableColumn
basDhcpRelayIf = _BasDhcpRelayIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 3),
    _BasDhcpRelayIf_Type()
)
basDhcpRelayIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayIf.setStatus("current")
_BasDhcpRelayLPort_Type = BasLogicalPortId
_BasDhcpRelayLPort_Object = MibTableColumn
basDhcpRelayLPort = _BasDhcpRelayLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 4),
    _BasDhcpRelayLPort_Type()
)
basDhcpRelayLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayLPort.setStatus("current")


class _BasDhcpRelayEnable_Type(Integer32):
    """Custom type basDhcpRelayEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasDhcpRelayEnable_Type.__name__ = "Integer32"
_BasDhcpRelayEnable_Object = MibTableColumn
basDhcpRelayEnable = _BasDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 5),
    _BasDhcpRelayEnable_Type()
)
basDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayEnable.setStatus("current")
_BasDhcpRelayDiscover_Type = Counter32
_BasDhcpRelayDiscover_Object = MibTableColumn
basDhcpRelayDiscover = _BasDhcpRelayDiscover_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 6),
    _BasDhcpRelayDiscover_Type()
)
basDhcpRelayDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayDiscover.setStatus("current")
_BasDhcpRelayOffer_Type = Counter32
_BasDhcpRelayOffer_Object = MibTableColumn
basDhcpRelayOffer = _BasDhcpRelayOffer_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 7),
    _BasDhcpRelayOffer_Type()
)
basDhcpRelayOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayOffer.setStatus("current")
_BasDhcpRelayRequest_Type = Counter32
_BasDhcpRelayRequest_Object = MibTableColumn
basDhcpRelayRequest = _BasDhcpRelayRequest_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 8),
    _BasDhcpRelayRequest_Type()
)
basDhcpRelayRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayRequest.setStatus("current")
_BasDhcpRelayDecline_Type = Counter32
_BasDhcpRelayDecline_Object = MibTableColumn
basDhcpRelayDecline = _BasDhcpRelayDecline_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 9),
    _BasDhcpRelayDecline_Type()
)
basDhcpRelayDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayDecline.setStatus("current")
_BasDhcpRelayNak_Type = Counter32
_BasDhcpRelayNak_Object = MibTableColumn
basDhcpRelayNak = _BasDhcpRelayNak_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 10),
    _BasDhcpRelayNak_Type()
)
basDhcpRelayNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayNak.setStatus("current")
_BasDhcpRelayInform_Type = Counter32
_BasDhcpRelayInform_Object = MibTableColumn
basDhcpRelayInform = _BasDhcpRelayInform_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 11),
    _BasDhcpRelayInform_Type()
)
basDhcpRelayInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayInform.setStatus("current")
_BasDhcpRelayAck_Type = Counter32
_BasDhcpRelayAck_Object = MibTableColumn
basDhcpRelayAck = _BasDhcpRelayAck_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 12),
    _BasDhcpRelayAck_Type()
)
basDhcpRelayAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayAck.setStatus("current")
_BasDhcpRelayRelease_Type = Counter32
_BasDhcpRelayRelease_Object = MibTableColumn
basDhcpRelayRelease = _BasDhcpRelayRelease_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 13),
    _BasDhcpRelayRelease_Type()
)
basDhcpRelayRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayRelease.setStatus("current")


class _BasDhcpRelayHelper_Type(Integer32):
    """Custom type basDhcpRelayHelper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasDhcpRelayHelper_Type.__name__ = "Integer32"
_BasDhcpRelayHelper_Object = MibTableColumn
basDhcpRelayHelper = _BasDhcpRelayHelper_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 14),
    _BasDhcpRelayHelper_Type()
)
basDhcpRelayHelper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayHelper.setStatus("current")


class _BasDhcpRelayAlwaysBroadcast_Type(Integer32):
    """Custom type basDhcpRelayAlwaysBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasDhcpRelayAlwaysBroadcast_Type.__name__ = "Integer32"
_BasDhcpRelayAlwaysBroadcast_Object = MibTableColumn
basDhcpRelayAlwaysBroadcast = _BasDhcpRelayAlwaysBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 15),
    _BasDhcpRelayAlwaysBroadcast_Type()
)
basDhcpRelayAlwaysBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayAlwaysBroadcast.setStatus("current")


class _BasDhcpRelayDuplicateResponse_Type(Integer32):
    """Custom type basDhcpRelayDuplicateResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasDhcpRelayDuplicateResponse_Type.__name__ = "Integer32"
_BasDhcpRelayDuplicateResponse_Object = MibTableColumn
basDhcpRelayDuplicateResponse = _BasDhcpRelayDuplicateResponse_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 16),
    _BasDhcpRelayDuplicateResponse_Type()
)
basDhcpRelayDuplicateResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayDuplicateResponse.setStatus("current")


class _BasDhcpRelayBasEnable_Type(Integer32):
    """Custom type basDhcpRelayBasEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasDhcpRelayBasEnable_Type.__name__ = "Integer32"
_BasDhcpRelayBasEnable_Object = MibTableColumn
basDhcpRelayBasEnable = _BasDhcpRelayBasEnable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 17),
    _BasDhcpRelayBasEnable_Type()
)
basDhcpRelayBasEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayBasEnable.setStatus("current")
_BasDhcpRelayBogusAgentDrops_Type = Counter32
_BasDhcpRelayBogusAgentDrops_Object = MibTableColumn
basDhcpRelayBogusAgentDrops = _BasDhcpRelayBogusAgentDrops_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 18),
    _BasDhcpRelayBogusAgentDrops_Type()
)
basDhcpRelayBogusAgentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayBogusAgentDrops.setStatus("current")
_BasDhcpRelayBogusGiaddrDrops_Type = Counter32
_BasDhcpRelayBogusGiaddrDrops_Object = MibTableColumn
basDhcpRelayBogusGiaddrDrops = _BasDhcpRelayBogusGiaddrDrops_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 19),
    _BasDhcpRelayBogusGiaddrDrops_Type()
)
basDhcpRelayBogusGiaddrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayBogusGiaddrDrops.setStatus("current")
_BasDhcpRelayServerPacketErrors_Type = Counter32
_BasDhcpRelayServerPacketErrors_Object = MibTableColumn
basDhcpRelayServerPacketErrors = _BasDhcpRelayServerPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 20),
    _BasDhcpRelayServerPacketErrors_Type()
)
basDhcpRelayServerPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayServerPacketErrors.setStatus("current")
_BasDhcpRelayClientPacketErrors_Type = Counter32
_BasDhcpRelayClientPacketErrors_Object = MibTableColumn
basDhcpRelayClientPacketErrors = _BasDhcpRelayClientPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 21),
    _BasDhcpRelayClientPacketErrors_Type()
)
basDhcpRelayClientPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayClientPacketErrors.setStatus("current")


class _BasDhcpRelayAddAgentOptions_Type(Integer32):
    """Custom type basDhcpRelayAddAgentOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasDhcpRelayAddAgentOptions_Type.__name__ = "Integer32"
_BasDhcpRelayAddAgentOptions_Object = MibTableColumn
basDhcpRelayAddAgentOptions = _BasDhcpRelayAddAgentOptions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 22),
    _BasDhcpRelayAddAgentOptions_Type()
)
basDhcpRelayAddAgentOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayAddAgentOptions.setStatus("current")


class _BasDhcpRelayDropAgentMismatch_Type(Integer32):
    """Custom type basDhcpRelayDropAgentMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasDhcpRelayDropAgentMismatch_Type.__name__ = "Integer32"
_BasDhcpRelayDropAgentMismatch_Object = MibTableColumn
basDhcpRelayDropAgentMismatch = _BasDhcpRelayDropAgentMismatch_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 23),
    _BasDhcpRelayDropAgentMismatch_Type()
)
basDhcpRelayDropAgentMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayDropAgentMismatch.setStatus("current")
_BasDhcpRelayCorruptAgentOptions_Type = Counter32
_BasDhcpRelayCorruptAgentOptions_Object = MibTableColumn
basDhcpRelayCorruptAgentOptions = _BasDhcpRelayCorruptAgentOptions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 24),
    _BasDhcpRelayCorruptAgentOptions_Type()
)
basDhcpRelayCorruptAgentOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayCorruptAgentOptions.setStatus("current")
_BasDhcpRelayMissingAgentOption_Type = Counter32
_BasDhcpRelayMissingAgentOption_Object = MibTableColumn
basDhcpRelayMissingAgentOption = _BasDhcpRelayMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 25),
    _BasDhcpRelayMissingAgentOption_Type()
)
basDhcpRelayMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayMissingAgentOption.setStatus("current")
_BasDhcpRelayBadCircuitId_Type = Counter32
_BasDhcpRelayBadCircuitId_Object = MibTableColumn
basDhcpRelayBadCircuitId = _BasDhcpRelayBadCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 26),
    _BasDhcpRelayBadCircuitId_Type()
)
basDhcpRelayBadCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayBadCircuitId.setStatus("current")
_BasDhcpRelayMissingCircuitId_Type = Counter32
_BasDhcpRelayMissingCircuitId_Object = MibTableColumn
basDhcpRelayMissingCircuitId = _BasDhcpRelayMissingCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 27),
    _BasDhcpRelayMissingCircuitId_Type()
)
basDhcpRelayMissingCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDhcpRelayMissingCircuitId.setStatus("current")


class _BasDhcpRelayMaxAgentOptionPacketLength_Type(Integer32):
    """Custom type basDhcpRelayMaxAgentOptionPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 1518),
    )


_BasDhcpRelayMaxAgentOptionPacketLength_Type.__name__ = "Integer32"
_BasDhcpRelayMaxAgentOptionPacketLength_Object = MibTableColumn
basDhcpRelayMaxAgentOptionPacketLength = _BasDhcpRelayMaxAgentOptionPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 28),
    _BasDhcpRelayMaxAgentOptionPacketLength_Type()
)
basDhcpRelayMaxAgentOptionPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayMaxAgentOptionPacketLength.setStatus("current")


class _BasDhcpRelayAgentRelayMode_Type(Integer32):
    """Custom type basDhcpRelayAgentRelayMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("discard", 4),
          ("forwardAndAppend", 1),
          ("forwardAndReplace", 2),
          ("forwardUntouched", 3))
    )


_BasDhcpRelayAgentRelayMode_Type.__name__ = "Integer32"
_BasDhcpRelayAgentRelayMode_Object = MibTableColumn
basDhcpRelayAgentRelayMode = _BasDhcpRelayAgentRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 1, 1, 29),
    _BasDhcpRelayAgentRelayMode_Type()
)
basDhcpRelayAgentRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDhcpRelayAgentRelayMode.setStatus("current")
_BasDhcpRelayServerTable_Object = MibTable
basDhcpRelayServerTable = _BasDhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    basDhcpRelayServerTable.setStatus("current")
_BasDhcpRelayServerEntry_Object = MibTableRow
basDhcpRelayServerEntry = _BasDhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1)
)
basDhcpRelayServerEntry.setIndexNames(
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayServerChassis"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayServerSlot"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayServerIf"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayServerLPort"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayServerAddress"),
    (0, "BAS-DHCP-RELAY-MIB", "basDhcpRelayServerType"),
)
if mibBuilder.loadTexts:
    basDhcpRelayServerEntry.setStatus("current")
_BasDhcpRelayServerChassis_Type = BasChassisId
_BasDhcpRelayServerChassis_Object = MibTableColumn
basDhcpRelayServerChassis = _BasDhcpRelayServerChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1, 1),
    _BasDhcpRelayServerChassis_Type()
)
basDhcpRelayServerChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayServerChassis.setStatus("current")
_BasDhcpRelayServerSlot_Type = BasSlotId
_BasDhcpRelayServerSlot_Object = MibTableColumn
basDhcpRelayServerSlot = _BasDhcpRelayServerSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1, 2),
    _BasDhcpRelayServerSlot_Type()
)
basDhcpRelayServerSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayServerSlot.setStatus("current")
_BasDhcpRelayServerIf_Type = BasInterfaceId
_BasDhcpRelayServerIf_Object = MibTableColumn
basDhcpRelayServerIf = _BasDhcpRelayServerIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1, 3),
    _BasDhcpRelayServerIf_Type()
)
basDhcpRelayServerIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayServerIf.setStatus("current")
_BasDhcpRelayServerLPort_Type = BasLogicalPortId
_BasDhcpRelayServerLPort_Object = MibTableColumn
basDhcpRelayServerLPort = _BasDhcpRelayServerLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1, 4),
    _BasDhcpRelayServerLPort_Type()
)
basDhcpRelayServerLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayServerLPort.setStatus("current")


class _BasDhcpRelayServerAddress_Type(IpAddress):
    """Custom type basDhcpRelayServerAddress based on IpAddress"""
    defaultValue = 2


_BasDhcpRelayServerAddress_Object = MibTableColumn
basDhcpRelayServerAddress = _BasDhcpRelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1, 5),
    _BasDhcpRelayServerAddress_Type()
)
basDhcpRelayServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayServerAddress.setStatus("current")


class _BasDhcpRelayServerType_Type(BasSubnetClass):
    """Custom type basDhcpRelayServerType based on BasSubnetClass"""
    defaultValue = 1


_BasDhcpRelayServerType_Object = MibTableColumn
basDhcpRelayServerType = _BasDhcpRelayServerType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1, 6),
    _BasDhcpRelayServerType_Type()
)
basDhcpRelayServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDhcpRelayServerType.setStatus("current")


class _BasDhcpRelayServerStatus_Type(RowStatus):
    """Custom type basDhcpRelayServerStatus based on RowStatus"""
    defaultValue = 1


_BasDhcpRelayServerStatus_Object = MibTableColumn
basDhcpRelayServerStatus = _BasDhcpRelayServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 15, 1, 2, 1, 7),
    _BasDhcpRelayServerStatus_Type()
)
basDhcpRelayServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDhcpRelayServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-DHCP-RELAY-MIB",
    **{"basDhcpRelayMIB": basDhcpRelayMIB,
       "basDhcpRelayTable": basDhcpRelayTable,
       "basDhcpRelayEntry": basDhcpRelayEntry,
       "basDhcpRelayChassis": basDhcpRelayChassis,
       "basDhcpRelaySlot": basDhcpRelaySlot,
       "basDhcpRelayIf": basDhcpRelayIf,
       "basDhcpRelayLPort": basDhcpRelayLPort,
       "basDhcpRelayEnable": basDhcpRelayEnable,
       "basDhcpRelayDiscover": basDhcpRelayDiscover,
       "basDhcpRelayOffer": basDhcpRelayOffer,
       "basDhcpRelayRequest": basDhcpRelayRequest,
       "basDhcpRelayDecline": basDhcpRelayDecline,
       "basDhcpRelayNak": basDhcpRelayNak,
       "basDhcpRelayInform": basDhcpRelayInform,
       "basDhcpRelayAck": basDhcpRelayAck,
       "basDhcpRelayRelease": basDhcpRelayRelease,
       "basDhcpRelayHelper": basDhcpRelayHelper,
       "basDhcpRelayAlwaysBroadcast": basDhcpRelayAlwaysBroadcast,
       "basDhcpRelayDuplicateResponse": basDhcpRelayDuplicateResponse,
       "basDhcpRelayBasEnable": basDhcpRelayBasEnable,
       "basDhcpRelayBogusAgentDrops": basDhcpRelayBogusAgentDrops,
       "basDhcpRelayBogusGiaddrDrops": basDhcpRelayBogusGiaddrDrops,
       "basDhcpRelayServerPacketErrors": basDhcpRelayServerPacketErrors,
       "basDhcpRelayClientPacketErrors": basDhcpRelayClientPacketErrors,
       "basDhcpRelayAddAgentOptions": basDhcpRelayAddAgentOptions,
       "basDhcpRelayDropAgentMismatch": basDhcpRelayDropAgentMismatch,
       "basDhcpRelayCorruptAgentOptions": basDhcpRelayCorruptAgentOptions,
       "basDhcpRelayMissingAgentOption": basDhcpRelayMissingAgentOption,
       "basDhcpRelayBadCircuitId": basDhcpRelayBadCircuitId,
       "basDhcpRelayMissingCircuitId": basDhcpRelayMissingCircuitId,
       "basDhcpRelayMaxAgentOptionPacketLength": basDhcpRelayMaxAgentOptionPacketLength,
       "basDhcpRelayAgentRelayMode": basDhcpRelayAgentRelayMode,
       "basDhcpRelayServerTable": basDhcpRelayServerTable,
       "basDhcpRelayServerEntry": basDhcpRelayServerEntry,
       "basDhcpRelayServerChassis": basDhcpRelayServerChassis,
       "basDhcpRelayServerSlot": basDhcpRelayServerSlot,
       "basDhcpRelayServerIf": basDhcpRelayServerIf,
       "basDhcpRelayServerLPort": basDhcpRelayServerLPort,
       "basDhcpRelayServerAddress": basDhcpRelayServerAddress,
       "basDhcpRelayServerType": basDhcpRelayServerType,
       "basDhcpRelayServerStatus": basDhcpRelayServerStatus}
)
