# SNMP MIB module (A3COM-HUAWEI-VOICE-CALL-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VOICE-CALL-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:25 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

(AbsoluteCounter32,) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32")

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

h3cVoCallHistory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16)
)
h3cVoCallHistory.setRevisions(
        ("2008-02-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cGUid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class H3cCodecType(Integer32, TextualConvention):
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

_H3cVoiceCallHistoryObjects_ObjectIdentity = ObjectIdentity
h3cVoiceCallHistoryObjects = _H3cVoiceCallHistoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1)
)
_H3cCallHistoryTable_Object = MibTable
h3cCallHistoryTable = _H3cCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1)
)
if mibBuilder.loadTexts:
    h3cCallHistoryTable.setStatus("current")
_H3cCallHistoryEntry_Object = MibTableRow
h3cCallHistoryEntry = _H3cCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1)
)
h3cCallHistoryEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOICE-CALL-HISTORY-MIB", "h3cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    h3cCallHistoryEntry.setStatus("current")


class _H3cCallHistoryIndex_Type(Integer32):
    """Custom type h3cCallHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cCallHistoryIndex_Type.__name__ = "Integer32"
_H3cCallHistoryIndex_Object = MibTableColumn
h3cCallHistoryIndex = _H3cCallHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 1),
    _H3cCallHistoryIndex_Type()
)
h3cCallHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCallHistoryIndex.setStatus("current")
_H3cCallHistorySetupTime_Type = TimeStamp
_H3cCallHistorySetupTime_Object = MibTableColumn
h3cCallHistorySetupTime = _H3cCallHistorySetupTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 2),
    _H3cCallHistorySetupTime_Type()
)
h3cCallHistorySetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistorySetupTime.setStatus("current")
_H3cCallHistoryConnectTime_Type = TimeStamp
_H3cCallHistoryConnectTime_Object = MibTableColumn
h3cCallHistoryConnectTime = _H3cCallHistoryConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 3),
    _H3cCallHistoryConnectTime_Type()
)
h3cCallHistoryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryConnectTime.setStatus("current")
_H3cCallHistoryTerminateTime_Type = TimeStamp
_H3cCallHistoryTerminateTime_Object = MibTableColumn
h3cCallHistoryTerminateTime = _H3cCallHistoryTerminateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 4),
    _H3cCallHistoryTerminateTime_Type()
)
h3cCallHistoryTerminateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryTerminateTime.setStatus("current")
_H3cCallHistoryPeerAddress_Type = DisplayString
_H3cCallHistoryPeerAddress_Object = MibTableColumn
h3cCallHistoryPeerAddress = _H3cCallHistoryPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 5),
    _H3cCallHistoryPeerAddress_Type()
)
h3cCallHistoryPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryPeerAddress.setStatus("current")


class _H3cCallHistoryPeerId_Type(Integer32):
    """Custom type h3cCallHistoryPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cCallHistoryPeerId_Type.__name__ = "Integer32"
_H3cCallHistoryPeerId_Object = MibTableColumn
h3cCallHistoryPeerId = _H3cCallHistoryPeerId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 6),
    _H3cCallHistoryPeerId_Type()
)
h3cCallHistoryPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryPeerId.setStatus("current")
_H3cCallHistoryLogicalIfIndex_Type = InterfaceIndexOrZero
_H3cCallHistoryLogicalIfIndex_Object = MibTableColumn
h3cCallHistoryLogicalIfIndex = _H3cCallHistoryLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 7),
    _H3cCallHistoryLogicalIfIndex_Type()
)
h3cCallHistoryLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryLogicalIfIndex.setStatus("current")


class _H3cCallHistoryCallOrigin_Type(Integer32):
    """Custom type h3cCallHistoryCallOrigin based on Integer32"""
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


_H3cCallHistoryCallOrigin_Type.__name__ = "Integer32"
_H3cCallHistoryCallOrigin_Object = MibTableColumn
h3cCallHistoryCallOrigin = _H3cCallHistoryCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 8),
    _H3cCallHistoryCallOrigin_Type()
)
h3cCallHistoryCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryCallOrigin.setStatus("current")
_H3cCallHistoryChargedUnits_Type = AbsoluteCounter32
_H3cCallHistoryChargedUnits_Object = MibTableColumn
h3cCallHistoryChargedUnits = _H3cCallHistoryChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 9),
    _H3cCallHistoryChargedUnits_Type()
)
h3cCallHistoryChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryChargedUnits.setStatus("current")


class _H3cCallHistoryInfoType_Type(Integer32):
    """Custom type h3cCallHistoryInfoType based on Integer32"""
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


_H3cCallHistoryInfoType_Type.__name__ = "Integer32"
_H3cCallHistoryInfoType_Object = MibTableColumn
h3cCallHistoryInfoType = _H3cCallHistoryInfoType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 10),
    _H3cCallHistoryInfoType_Type()
)
h3cCallHistoryInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryInfoType.setStatus("current")
_H3cCallHistoryTransmitPackets_Type = AbsoluteCounter32
_H3cCallHistoryTransmitPackets_Object = MibTableColumn
h3cCallHistoryTransmitPackets = _H3cCallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 11),
    _H3cCallHistoryTransmitPackets_Type()
)
h3cCallHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryTransmitPackets.setStatus("current")
_H3cCallHistoryTransmitBytes_Type = AbsoluteCounter32
_H3cCallHistoryTransmitBytes_Object = MibTableColumn
h3cCallHistoryTransmitBytes = _H3cCallHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 12),
    _H3cCallHistoryTransmitBytes_Type()
)
h3cCallHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryTransmitBytes.setStatus("current")
_H3cCallHistoryReceivePackets_Type = AbsoluteCounter32
_H3cCallHistoryReceivePackets_Object = MibTableColumn
h3cCallHistoryReceivePackets = _H3cCallHistoryReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 13),
    _H3cCallHistoryReceivePackets_Type()
)
h3cCallHistoryReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryReceivePackets.setStatus("current")
_H3cCallHistoryReceiveBytes_Type = AbsoluteCounter32
_H3cCallHistoryReceiveBytes_Object = MibTableColumn
h3cCallHistoryReceiveBytes = _H3cCallHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 1, 1, 14),
    _H3cCallHistoryReceiveBytes_Type()
)
h3cCallHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCallHistoryReceiveBytes.setStatus("current")
_H3cVoiceCallHistoryTable_Object = MibTable
h3cVoiceCallHistoryTable = _H3cVoiceCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVoiceCallHistoryTable.setStatus("current")
_H3cVoiceCallHistoryEntry_Object = MibTableRow
h3cVoiceCallHistoryEntry = _H3cVoiceCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2, 1)
)
h3cVoiceCallHistoryEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOICE-CALL-HISTORY-MIB", "h3cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    h3cVoiceCallHistoryEntry.setStatus("current")
_H3cVoCallHistoryConnectionId_Type = H3cGUid
_H3cVoCallHistoryConnectionId_Object = MibTableColumn
h3cVoCallHistoryConnectionId = _H3cVoCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2, 1, 1),
    _H3cVoCallHistoryConnectionId_Type()
)
h3cVoCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHistoryConnectionId.setStatus("current")
_H3cVoCallHistoryTxDuration_Type = Gauge32
_H3cVoCallHistoryTxDuration_Object = MibTableColumn
h3cVoCallHistoryTxDuration = _H3cVoCallHistoryTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2, 1, 2),
    _H3cVoCallHistoryTxDuration_Type()
)
h3cVoCallHistoryTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHistoryTxDuration.setStatus("current")
_H3cVoCallHistoryVoiceTxDuration_Type = Gauge32
_H3cVoCallHistoryVoiceTxDuration_Object = MibTableColumn
h3cVoCallHistoryVoiceTxDuration = _H3cVoCallHistoryVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2, 1, 3),
    _H3cVoCallHistoryVoiceTxDuration_Type()
)
h3cVoCallHistoryVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHistoryVoiceTxDuration.setStatus("current")
_H3cVoCallHistoryFaxTxDuration_Type = Gauge32
_H3cVoCallHistoryFaxTxDuration_Object = MibTableColumn
h3cVoCallHistoryFaxTxDuration = _H3cVoCallHistoryFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2, 1, 4),
    _H3cVoCallHistoryFaxTxDuration_Type()
)
h3cVoCallHistoryFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHistoryFaxTxDuration.setStatus("current")
_H3cVoCallHistoryCoderType_Type = H3cCodecType
_H3cVoCallHistoryCoderType_Object = MibTableColumn
h3cVoCallHistoryCoderType = _H3cVoCallHistoryCoderType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2, 1, 5),
    _H3cVoCallHistoryCoderType_Type()
)
h3cVoCallHistoryCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHistoryCoderType.setStatus("current")
_H3cVoCallHistoryImgPageCount_Type = Gauge32
_H3cVoCallHistoryImgPageCount_Object = MibTableColumn
h3cVoCallHistoryImgPageCount = _H3cVoCallHistoryImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 2, 1, 6),
    _H3cVoCallHistoryImgPageCount_Type()
)
h3cVoCallHistoryImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallHistoryImgPageCount.setStatus("current")
_H3cVoiceVoIPCallHistoryTable_Object = MibTable
h3cVoiceVoIPCallHistoryTable = _H3cVoiceVoIPCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3)
)
if mibBuilder.loadTexts:
    h3cVoiceVoIPCallHistoryTable.setStatus("current")
_H3cVoiceVoIPCallHistoryEntry_Object = MibTableRow
h3cVoiceVoIPCallHistoryEntry = _H3cVoiceVoIPCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1)
)
h3cVoiceVoIPCallHistoryEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOICE-CALL-HISTORY-MIB", "h3cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    h3cVoiceVoIPCallHistoryEntry.setStatus("current")
_H3cVoVoIPCallHistoryConnectionId_Type = H3cGUid
_H3cVoVoIPCallHistoryConnectionId_Object = MibTableColumn
h3cVoVoIPCallHistoryConnectionId = _H3cVoVoIPCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 1),
    _H3cVoVoIPCallHistoryConnectionId_Type()
)
h3cVoVoIPCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryConnectionId.setStatus("current")
_H3cVoVoIPCallHistoryRemSigIPType_Type = InetAddressType
_H3cVoVoIPCallHistoryRemSigIPType_Object = MibTableColumn
h3cVoVoIPCallHistoryRemSigIPType = _H3cVoVoIPCallHistoryRemSigIPType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 2),
    _H3cVoVoIPCallHistoryRemSigIPType_Type()
)
h3cVoVoIPCallHistoryRemSigIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryRemSigIPType.setStatus("current")
_H3cVoVoIPCallHistoryRemSigIPAddr_Type = InetAddress
_H3cVoVoIPCallHistoryRemSigIPAddr_Object = MibTableColumn
h3cVoVoIPCallHistoryRemSigIPAddr = _H3cVoVoIPCallHistoryRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 3),
    _H3cVoVoIPCallHistoryRemSigIPAddr_Type()
)
h3cVoVoIPCallHistoryRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryRemSigIPAddr.setStatus("current")


class _H3cVoVoIPCallHistoryRemSigPort_Type(Integer32):
    """Custom type h3cVoVoIPCallHistoryRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cVoVoIPCallHistoryRemSigPort_Type.__name__ = "Integer32"
_H3cVoVoIPCallHistoryRemSigPort_Object = MibTableColumn
h3cVoVoIPCallHistoryRemSigPort = _H3cVoVoIPCallHistoryRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 4),
    _H3cVoVoIPCallHistoryRemSigPort_Type()
)
h3cVoVoIPCallHistoryRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryRemSigPort.setStatus("current")
_H3cVoVoIPCallHistoryRemMedIPType_Type = InetAddressType
_H3cVoVoIPCallHistoryRemMedIPType_Object = MibTableColumn
h3cVoVoIPCallHistoryRemMedIPType = _H3cVoVoIPCallHistoryRemMedIPType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 5),
    _H3cVoVoIPCallHistoryRemMedIPType_Type()
)
h3cVoVoIPCallHistoryRemMedIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryRemMedIPType.setStatus("current")
_H3cVoVoIPCallHistoryRemMedIPAddr_Type = InetAddress
_H3cVoVoIPCallHistoryRemMedIPAddr_Object = MibTableColumn
h3cVoVoIPCallHistoryRemMedIPAddr = _H3cVoVoIPCallHistoryRemMedIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 6),
    _H3cVoVoIPCallHistoryRemMedIPAddr_Type()
)
h3cVoVoIPCallHistoryRemMedIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryRemMedIPAddr.setStatus("current")


class _H3cVoVoIPCallHistoryRemMedPort_Type(Integer32):
    """Custom type h3cVoVoIPCallHistoryRemMedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cVoVoIPCallHistoryRemMedPort_Type.__name__ = "Integer32"
_H3cVoVoIPCallHistoryRemMedPort_Object = MibTableColumn
h3cVoVoIPCallHistoryRemMedPort = _H3cVoVoIPCallHistoryRemMedPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 7),
    _H3cVoVoIPCallHistoryRemMedPort_Type()
)
h3cVoVoIPCallHistoryRemMedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryRemMedPort.setStatus("current")


class _H3cVoVoIPCallHistorySessProtocol_Type(Integer32):
    """Custom type h3cVoVoIPCallHistorySessProtocol based on Integer32"""
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


_H3cVoVoIPCallHistorySessProtocol_Type.__name__ = "Integer32"
_H3cVoVoIPCallHistorySessProtocol_Object = MibTableColumn
h3cVoVoIPCallHistorySessProtocol = _H3cVoVoIPCallHistorySessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 8),
    _H3cVoVoIPCallHistorySessProtocol_Type()
)
h3cVoVoIPCallHistorySessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistorySessProtocol.setStatus("current")
_H3cVoVoIPCallHistoryCoderType_Type = H3cCodecType
_H3cVoVoIPCallHistoryCoderType_Object = MibTableColumn
h3cVoVoIPCallHistoryCoderType = _H3cVoVoIPCallHistoryCoderType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 16, 1, 3, 1, 9),
    _H3cVoVoIPCallHistoryCoderType_Type()
)
h3cVoVoIPCallHistoryCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoVoIPCallHistoryCoderType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VOICE-CALL-HISTORY-MIB",
    **{"H3cGUid": H3cGUid,
       "H3cCodecType": H3cCodecType,
       "h3cVoCallHistory": h3cVoCallHistory,
       "h3cVoiceCallHistoryObjects": h3cVoiceCallHistoryObjects,
       "h3cCallHistoryTable": h3cCallHistoryTable,
       "h3cCallHistoryEntry": h3cCallHistoryEntry,
       "h3cCallHistoryIndex": h3cCallHistoryIndex,
       "h3cCallHistorySetupTime": h3cCallHistorySetupTime,
       "h3cCallHistoryConnectTime": h3cCallHistoryConnectTime,
       "h3cCallHistoryTerminateTime": h3cCallHistoryTerminateTime,
       "h3cCallHistoryPeerAddress": h3cCallHistoryPeerAddress,
       "h3cCallHistoryPeerId": h3cCallHistoryPeerId,
       "h3cCallHistoryLogicalIfIndex": h3cCallHistoryLogicalIfIndex,
       "h3cCallHistoryCallOrigin": h3cCallHistoryCallOrigin,
       "h3cCallHistoryChargedUnits": h3cCallHistoryChargedUnits,
       "h3cCallHistoryInfoType": h3cCallHistoryInfoType,
       "h3cCallHistoryTransmitPackets": h3cCallHistoryTransmitPackets,
       "h3cCallHistoryTransmitBytes": h3cCallHistoryTransmitBytes,
       "h3cCallHistoryReceivePackets": h3cCallHistoryReceivePackets,
       "h3cCallHistoryReceiveBytes": h3cCallHistoryReceiveBytes,
       "h3cVoiceCallHistoryTable": h3cVoiceCallHistoryTable,
       "h3cVoiceCallHistoryEntry": h3cVoiceCallHistoryEntry,
       "h3cVoCallHistoryConnectionId": h3cVoCallHistoryConnectionId,
       "h3cVoCallHistoryTxDuration": h3cVoCallHistoryTxDuration,
       "h3cVoCallHistoryVoiceTxDuration": h3cVoCallHistoryVoiceTxDuration,
       "h3cVoCallHistoryFaxTxDuration": h3cVoCallHistoryFaxTxDuration,
       "h3cVoCallHistoryCoderType": h3cVoCallHistoryCoderType,
       "h3cVoCallHistoryImgPageCount": h3cVoCallHistoryImgPageCount,
       "h3cVoiceVoIPCallHistoryTable": h3cVoiceVoIPCallHistoryTable,
       "h3cVoiceVoIPCallHistoryEntry": h3cVoiceVoIPCallHistoryEntry,
       "h3cVoVoIPCallHistoryConnectionId": h3cVoVoIPCallHistoryConnectionId,
       "h3cVoVoIPCallHistoryRemSigIPType": h3cVoVoIPCallHistoryRemSigIPType,
       "h3cVoVoIPCallHistoryRemSigIPAddr": h3cVoVoIPCallHistoryRemSigIPAddr,
       "h3cVoVoIPCallHistoryRemSigPort": h3cVoVoIPCallHistoryRemSigPort,
       "h3cVoVoIPCallHistoryRemMedIPType": h3cVoVoIPCallHistoryRemMedIPType,
       "h3cVoVoIPCallHistoryRemMedIPAddr": h3cVoVoIPCallHistoryRemMedIPAddr,
       "h3cVoVoIPCallHistoryRemMedPort": h3cVoVoIPCallHistoryRemMedPort,
       "h3cVoVoIPCallHistorySessProtocol": h3cVoVoIPCallHistorySessProtocol,
       "h3cVoVoIPCallHistoryCoderType": h3cVoVoIPCallHistoryCoderType}
)
