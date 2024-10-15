# SNMP MIB module (HPN-ICF-VOICE-CALL-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VOICE-CALL-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:10 2024
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

(AbsoluteCounter32,) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32")

(hpnicfVoice,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfVoice")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hpnicfVoCallHistory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16)
)
hpnicfVoCallHistory.setRevisions(
        ("2008-02-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfGUid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class HpnicfCodecType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711u", 2),
          ("g723r53", 3),
          ("g723r63", 4),
          ("g726r16", 7),
          ("g726r24", 8),
          ("g726r32", 9),
          ("g726r40", 10),
          ("g729a", 6),
          ("g729br8", 12),
          ("g729r8", 5),
          ("unknown", 11))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfVoiceCallHistoryObjects_ObjectIdentity = ObjectIdentity
hpnicfVoiceCallHistoryObjects = _HpnicfVoiceCallHistoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1)
)
_HpnicfCallHistoryTable_Object = MibTable
hpnicfCallHistoryTable = _HpnicfCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfCallHistoryTable.setStatus("current")
_HpnicfCallHistoryEntry_Object = MibTableRow
hpnicfCallHistoryEntry = _HpnicfCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1)
)
hpnicfCallHistoryEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-CALL-HISTORY-MIB", "hpnicfCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCallHistoryEntry.setStatus("current")


class _HpnicfCallHistoryIndex_Type(Integer32):
    """Custom type hpnicfCallHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCallHistoryIndex_Type.__name__ = "Integer32"
_HpnicfCallHistoryIndex_Object = MibTableColumn
hpnicfCallHistoryIndex = _HpnicfCallHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 1),
    _HpnicfCallHistoryIndex_Type()
)
hpnicfCallHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCallHistoryIndex.setStatus("current")
_HpnicfCallHistorySetupTime_Type = TimeStamp
_HpnicfCallHistorySetupTime_Object = MibTableColumn
hpnicfCallHistorySetupTime = _HpnicfCallHistorySetupTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 2),
    _HpnicfCallHistorySetupTime_Type()
)
hpnicfCallHistorySetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistorySetupTime.setStatus("current")
_HpnicfCallHistoryConnectTime_Type = TimeStamp
_HpnicfCallHistoryConnectTime_Object = MibTableColumn
hpnicfCallHistoryConnectTime = _HpnicfCallHistoryConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 3),
    _HpnicfCallHistoryConnectTime_Type()
)
hpnicfCallHistoryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryConnectTime.setStatus("current")
_HpnicfCallHistoryTerminateTime_Type = TimeStamp
_HpnicfCallHistoryTerminateTime_Object = MibTableColumn
hpnicfCallHistoryTerminateTime = _HpnicfCallHistoryTerminateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 4),
    _HpnicfCallHistoryTerminateTime_Type()
)
hpnicfCallHistoryTerminateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryTerminateTime.setStatus("current")
_HpnicfCallHistoryPeerAddress_Type = DisplayString
_HpnicfCallHistoryPeerAddress_Object = MibTableColumn
hpnicfCallHistoryPeerAddress = _HpnicfCallHistoryPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 5),
    _HpnicfCallHistoryPeerAddress_Type()
)
hpnicfCallHistoryPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryPeerAddress.setStatus("current")


class _HpnicfCallHistoryPeerId_Type(Integer32):
    """Custom type hpnicfCallHistoryPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfCallHistoryPeerId_Type.__name__ = "Integer32"
_HpnicfCallHistoryPeerId_Object = MibTableColumn
hpnicfCallHistoryPeerId = _HpnicfCallHistoryPeerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 6),
    _HpnicfCallHistoryPeerId_Type()
)
hpnicfCallHistoryPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryPeerId.setStatus("current")
_HpnicfCallHistoryLogicalIfIndex_Type = InterfaceIndexOrZero
_HpnicfCallHistoryLogicalIfIndex_Object = MibTableColumn
hpnicfCallHistoryLogicalIfIndex = _HpnicfCallHistoryLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 7),
    _HpnicfCallHistoryLogicalIfIndex_Type()
)
hpnicfCallHistoryLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryLogicalIfIndex.setStatus("current")


class _HpnicfCallHistoryCallOrigin_Type(Integer32):
    """Custom type hpnicfCallHistoryCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("callback", 3),
          ("originate", 1))
    )


_HpnicfCallHistoryCallOrigin_Type.__name__ = "Integer32"
_HpnicfCallHistoryCallOrigin_Object = MibTableColumn
hpnicfCallHistoryCallOrigin = _HpnicfCallHistoryCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 8),
    _HpnicfCallHistoryCallOrigin_Type()
)
hpnicfCallHistoryCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryCallOrigin.setStatus("current")
_HpnicfCallHistoryChargedUnits_Type = AbsoluteCounter32
_HpnicfCallHistoryChargedUnits_Object = MibTableColumn
hpnicfCallHistoryChargedUnits = _HpnicfCallHistoryChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 9),
    _HpnicfCallHistoryChargedUnits_Type()
)
hpnicfCallHistoryChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryChargedUnits.setStatus("current")


class _HpnicfCallHistoryInfoType_Type(Integer32):
    """Custom type hpnicfCallHistoryInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("audio31", 6),
          ("audio7", 7),
          ("fax", 10),
          ("other", 1),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_HpnicfCallHistoryInfoType_Type.__name__ = "Integer32"
_HpnicfCallHistoryInfoType_Object = MibTableColumn
hpnicfCallHistoryInfoType = _HpnicfCallHistoryInfoType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 10),
    _HpnicfCallHistoryInfoType_Type()
)
hpnicfCallHistoryInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryInfoType.setStatus("current")
_HpnicfCallHistoryTransmitPackets_Type = AbsoluteCounter32
_HpnicfCallHistoryTransmitPackets_Object = MibTableColumn
hpnicfCallHistoryTransmitPackets = _HpnicfCallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 11),
    _HpnicfCallHistoryTransmitPackets_Type()
)
hpnicfCallHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryTransmitPackets.setStatus("current")
_HpnicfCallHistoryTransmitBytes_Type = AbsoluteCounter32
_HpnicfCallHistoryTransmitBytes_Object = MibTableColumn
hpnicfCallHistoryTransmitBytes = _HpnicfCallHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 12),
    _HpnicfCallHistoryTransmitBytes_Type()
)
hpnicfCallHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryTransmitBytes.setStatus("current")
_HpnicfCallHistoryReceivePackets_Type = AbsoluteCounter32
_HpnicfCallHistoryReceivePackets_Object = MibTableColumn
hpnicfCallHistoryReceivePackets = _HpnicfCallHistoryReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 13),
    _HpnicfCallHistoryReceivePackets_Type()
)
hpnicfCallHistoryReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryReceivePackets.setStatus("current")
_HpnicfCallHistoryReceiveBytes_Type = AbsoluteCounter32
_HpnicfCallHistoryReceiveBytes_Object = MibTableColumn
hpnicfCallHistoryReceiveBytes = _HpnicfCallHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 14),
    _HpnicfCallHistoryReceiveBytes_Type()
)
hpnicfCallHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCallHistoryReceiveBytes.setStatus("current")
_HpnicfVoiceCallHistoryTable_Object = MibTable
hpnicfVoiceCallHistoryTable = _HpnicfVoiceCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfVoiceCallHistoryTable.setStatus("current")
_HpnicfVoiceCallHistoryEntry_Object = MibTableRow
hpnicfVoiceCallHistoryEntry = _HpnicfVoiceCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1)
)
hpnicfVoiceCallHistoryEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-CALL-HISTORY-MIB", "hpnicfCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoiceCallHistoryEntry.setStatus("current")
_HpnicfVoCallHistoryConnectionId_Type = HpnicfGUid
_HpnicfVoCallHistoryConnectionId_Object = MibTableColumn
hpnicfVoCallHistoryConnectionId = _HpnicfVoCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 1),
    _HpnicfVoCallHistoryConnectionId_Type()
)
hpnicfVoCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallHistoryConnectionId.setStatus("current")
_HpnicfVoCallHistoryTxDuration_Type = Gauge32
_HpnicfVoCallHistoryTxDuration_Object = MibTableColumn
hpnicfVoCallHistoryTxDuration = _HpnicfVoCallHistoryTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 2),
    _HpnicfVoCallHistoryTxDuration_Type()
)
hpnicfVoCallHistoryTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallHistoryTxDuration.setStatus("current")
_HpnicfVoCallHistoryVoiceTxDuration_Type = Gauge32
_HpnicfVoCallHistoryVoiceTxDuration_Object = MibTableColumn
hpnicfVoCallHistoryVoiceTxDuration = _HpnicfVoCallHistoryVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 3),
    _HpnicfVoCallHistoryVoiceTxDuration_Type()
)
hpnicfVoCallHistoryVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallHistoryVoiceTxDuration.setStatus("current")
_HpnicfVoCallHistoryFaxTxDuration_Type = Gauge32
_HpnicfVoCallHistoryFaxTxDuration_Object = MibTableColumn
hpnicfVoCallHistoryFaxTxDuration = _HpnicfVoCallHistoryFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 4),
    _HpnicfVoCallHistoryFaxTxDuration_Type()
)
hpnicfVoCallHistoryFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallHistoryFaxTxDuration.setStatus("current")
_HpnicfVoCallHistoryCoderType_Type = HpnicfCodecType
_HpnicfVoCallHistoryCoderType_Object = MibTableColumn
hpnicfVoCallHistoryCoderType = _HpnicfVoCallHistoryCoderType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 5),
    _HpnicfVoCallHistoryCoderType_Type()
)
hpnicfVoCallHistoryCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallHistoryCoderType.setStatus("current")
_HpnicfVoCallHistoryImgPageCount_Type = Gauge32
_HpnicfVoCallHistoryImgPageCount_Object = MibTableColumn
hpnicfVoCallHistoryImgPageCount = _HpnicfVoCallHistoryImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 6),
    _HpnicfVoCallHistoryImgPageCount_Type()
)
hpnicfVoCallHistoryImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoCallHistoryImgPageCount.setStatus("current")
_HpnicfVoiceVoIPCallHistoryTable_Object = MibTable
hpnicfVoiceVoIPCallHistoryTable = _HpnicfVoiceVoIPCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfVoiceVoIPCallHistoryTable.setStatus("current")
_HpnicfVoiceVoIPCallHistoryEntry_Object = MibTableRow
hpnicfVoiceVoIPCallHistoryEntry = _HpnicfVoiceVoIPCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1)
)
hpnicfVoiceVoIPCallHistoryEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-CALL-HISTORY-MIB", "hpnicfCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoiceVoIPCallHistoryEntry.setStatus("current")
_HpnicfVoVoIPCallHistoryConnectionId_Type = HpnicfGUid
_HpnicfVoVoIPCallHistoryConnectionId_Object = MibTableColumn
hpnicfVoVoIPCallHistoryConnectionId = _HpnicfVoVoIPCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 1),
    _HpnicfVoVoIPCallHistoryConnectionId_Type()
)
hpnicfVoVoIPCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryConnectionId.setStatus("current")
_HpnicfVoVoIPCallHistoryRemSigIPType_Type = InetAddressType
_HpnicfVoVoIPCallHistoryRemSigIPType_Object = MibTableColumn
hpnicfVoVoIPCallHistoryRemSigIPType = _HpnicfVoVoIPCallHistoryRemSigIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 2),
    _HpnicfVoVoIPCallHistoryRemSigIPType_Type()
)
hpnicfVoVoIPCallHistoryRemSigIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryRemSigIPType.setStatus("current")
_HpnicfVoVoIPCallHistoryRemSigIPAddr_Type = InetAddress
_HpnicfVoVoIPCallHistoryRemSigIPAddr_Object = MibTableColumn
hpnicfVoVoIPCallHistoryRemSigIPAddr = _HpnicfVoVoIPCallHistoryRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 3),
    _HpnicfVoVoIPCallHistoryRemSigIPAddr_Type()
)
hpnicfVoVoIPCallHistoryRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryRemSigIPAddr.setStatus("current")


class _HpnicfVoVoIPCallHistoryRemSigPort_Type(Integer32):
    """Custom type hpnicfVoVoIPCallHistoryRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfVoVoIPCallHistoryRemSigPort_Type.__name__ = "Integer32"
_HpnicfVoVoIPCallHistoryRemSigPort_Object = MibTableColumn
hpnicfVoVoIPCallHistoryRemSigPort = _HpnicfVoVoIPCallHistoryRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 4),
    _HpnicfVoVoIPCallHistoryRemSigPort_Type()
)
hpnicfVoVoIPCallHistoryRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryRemSigPort.setStatus("current")
_HpnicfVoVoIPCallHistoryRemMedIPType_Type = InetAddressType
_HpnicfVoVoIPCallHistoryRemMedIPType_Object = MibTableColumn
hpnicfVoVoIPCallHistoryRemMedIPType = _HpnicfVoVoIPCallHistoryRemMedIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 5),
    _HpnicfVoVoIPCallHistoryRemMedIPType_Type()
)
hpnicfVoVoIPCallHistoryRemMedIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryRemMedIPType.setStatus("current")
_HpnicfVoVoIPCallHistoryRemMedIPAddr_Type = InetAddress
_HpnicfVoVoIPCallHistoryRemMedIPAddr_Object = MibTableColumn
hpnicfVoVoIPCallHistoryRemMedIPAddr = _HpnicfVoVoIPCallHistoryRemMedIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 6),
    _HpnicfVoVoIPCallHistoryRemMedIPAddr_Type()
)
hpnicfVoVoIPCallHistoryRemMedIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryRemMedIPAddr.setStatus("current")


class _HpnicfVoVoIPCallHistoryRemMedPort_Type(Integer32):
    """Custom type hpnicfVoVoIPCallHistoryRemMedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfVoVoIPCallHistoryRemMedPort_Type.__name__ = "Integer32"
_HpnicfVoVoIPCallHistoryRemMedPort_Object = MibTableColumn
hpnicfVoVoIPCallHistoryRemMedPort = _HpnicfVoVoIPCallHistoryRemMedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 7),
    _HpnicfVoVoIPCallHistoryRemMedPort_Type()
)
hpnicfVoVoIPCallHistoryRemMedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryRemMedPort.setStatus("current")


class _HpnicfVoVoIPCallHistorySessProtocol_Type(Integer32):
    """Custom type hpnicfVoVoIPCallHistorySessProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("h323", 2),
          ("sip", 3),
          ("unknown", 1))
    )


_HpnicfVoVoIPCallHistorySessProtocol_Type.__name__ = "Integer32"
_HpnicfVoVoIPCallHistorySessProtocol_Object = MibTableColumn
hpnicfVoVoIPCallHistorySessProtocol = _HpnicfVoVoIPCallHistorySessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 8),
    _HpnicfVoVoIPCallHistorySessProtocol_Type()
)
hpnicfVoVoIPCallHistorySessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistorySessProtocol.setStatus("current")
_HpnicfVoVoIPCallHistoryCoderType_Type = HpnicfCodecType
_HpnicfVoVoIPCallHistoryCoderType_Object = MibTableColumn
hpnicfVoVoIPCallHistoryCoderType = _HpnicfVoVoIPCallHistoryCoderType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 9),
    _HpnicfVoVoIPCallHistoryCoderType_Type()
)
hpnicfVoVoIPCallHistoryCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoVoIPCallHistoryCoderType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VOICE-CALL-HISTORY-MIB",
    **{"HpnicfGUid": HpnicfGUid,
       "HpnicfCodecType": HpnicfCodecType,
       "hpnicfVoCallHistory": hpnicfVoCallHistory,
       "hpnicfVoiceCallHistoryObjects": hpnicfVoiceCallHistoryObjects,
       "hpnicfCallHistoryTable": hpnicfCallHistoryTable,
       "hpnicfCallHistoryEntry": hpnicfCallHistoryEntry,
       "hpnicfCallHistoryIndex": hpnicfCallHistoryIndex,
       "hpnicfCallHistorySetupTime": hpnicfCallHistorySetupTime,
       "hpnicfCallHistoryConnectTime": hpnicfCallHistoryConnectTime,
       "hpnicfCallHistoryTerminateTime": hpnicfCallHistoryTerminateTime,
       "hpnicfCallHistoryPeerAddress": hpnicfCallHistoryPeerAddress,
       "hpnicfCallHistoryPeerId": hpnicfCallHistoryPeerId,
       "hpnicfCallHistoryLogicalIfIndex": hpnicfCallHistoryLogicalIfIndex,
       "hpnicfCallHistoryCallOrigin": hpnicfCallHistoryCallOrigin,
       "hpnicfCallHistoryChargedUnits": hpnicfCallHistoryChargedUnits,
       "hpnicfCallHistoryInfoType": hpnicfCallHistoryInfoType,
       "hpnicfCallHistoryTransmitPackets": hpnicfCallHistoryTransmitPackets,
       "hpnicfCallHistoryTransmitBytes": hpnicfCallHistoryTransmitBytes,
       "hpnicfCallHistoryReceivePackets": hpnicfCallHistoryReceivePackets,
       "hpnicfCallHistoryReceiveBytes": hpnicfCallHistoryReceiveBytes,
       "hpnicfVoiceCallHistoryTable": hpnicfVoiceCallHistoryTable,
       "hpnicfVoiceCallHistoryEntry": hpnicfVoiceCallHistoryEntry,
       "hpnicfVoCallHistoryConnectionId": hpnicfVoCallHistoryConnectionId,
       "hpnicfVoCallHistoryTxDuration": hpnicfVoCallHistoryTxDuration,
       "hpnicfVoCallHistoryVoiceTxDuration": hpnicfVoCallHistoryVoiceTxDuration,
       "hpnicfVoCallHistoryFaxTxDuration": hpnicfVoCallHistoryFaxTxDuration,
       "hpnicfVoCallHistoryCoderType": hpnicfVoCallHistoryCoderType,
       "hpnicfVoCallHistoryImgPageCount": hpnicfVoCallHistoryImgPageCount,
       "hpnicfVoiceVoIPCallHistoryTable": hpnicfVoiceVoIPCallHistoryTable,
       "hpnicfVoiceVoIPCallHistoryEntry": hpnicfVoiceVoIPCallHistoryEntry,
       "hpnicfVoVoIPCallHistoryConnectionId": hpnicfVoVoIPCallHistoryConnectionId,
       "hpnicfVoVoIPCallHistoryRemSigIPType": hpnicfVoVoIPCallHistoryRemSigIPType,
       "hpnicfVoVoIPCallHistoryRemSigIPAddr": hpnicfVoVoIPCallHistoryRemSigIPAddr,
       "hpnicfVoVoIPCallHistoryRemSigPort": hpnicfVoVoIPCallHistoryRemSigPort,
       "hpnicfVoVoIPCallHistoryRemMedIPType": hpnicfVoVoIPCallHistoryRemMedIPType,
       "hpnicfVoVoIPCallHistoryRemMedIPAddr": hpnicfVoVoIPCallHistoryRemMedIPAddr,
       "hpnicfVoVoIPCallHistoryRemMedPort": hpnicfVoVoIPCallHistoryRemMedPort,
       "hpnicfVoVoIPCallHistorySessProtocol": hpnicfVoVoIPCallHistorySessProtocol,
       "hpnicfVoVoIPCallHistoryCoderType": hpnicfVoVoIPCallHistoryCoderType}
)
