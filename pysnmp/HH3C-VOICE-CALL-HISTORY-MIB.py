# SNMP MIB module (HH3C-VOICE-CALL-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VOICE-CALL-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:17 2024
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

(hh3cVoice,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cVoice")

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

hh3cVoCallHistory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16)
)
hh3cVoCallHistory.setRevisions(
        ("2008-02-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cGUid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class Hh3cCodecType(Integer32, TextualConvention):
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

_Hh3cVoiceCallHistoryObjects_ObjectIdentity = ObjectIdentity
hh3cVoiceCallHistoryObjects = _Hh3cVoiceCallHistoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1)
)
_Hh3cCallHistoryTable_Object = MibTable
hh3cCallHistoryTable = _Hh3cCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cCallHistoryTable.setStatus("current")
_Hh3cCallHistoryEntry_Object = MibTableRow
hh3cCallHistoryEntry = _Hh3cCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1)
)
hh3cCallHistoryEntry.setIndexNames(
    (0, "HH3C-VOICE-CALL-HISTORY-MIB", "hh3cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    hh3cCallHistoryEntry.setStatus("current")


class _Hh3cCallHistoryIndex_Type(Integer32):
    """Custom type hh3cCallHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCallHistoryIndex_Type.__name__ = "Integer32"
_Hh3cCallHistoryIndex_Object = MibTableColumn
hh3cCallHistoryIndex = _Hh3cCallHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 1),
    _Hh3cCallHistoryIndex_Type()
)
hh3cCallHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCallHistoryIndex.setStatus("current")
_Hh3cCallHistorySetupTime_Type = TimeStamp
_Hh3cCallHistorySetupTime_Object = MibTableColumn
hh3cCallHistorySetupTime = _Hh3cCallHistorySetupTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 2),
    _Hh3cCallHistorySetupTime_Type()
)
hh3cCallHistorySetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistorySetupTime.setStatus("current")
_Hh3cCallHistoryConnectTime_Type = TimeStamp
_Hh3cCallHistoryConnectTime_Object = MibTableColumn
hh3cCallHistoryConnectTime = _Hh3cCallHistoryConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 3),
    _Hh3cCallHistoryConnectTime_Type()
)
hh3cCallHistoryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryConnectTime.setStatus("current")
_Hh3cCallHistoryTerminateTime_Type = TimeStamp
_Hh3cCallHistoryTerminateTime_Object = MibTableColumn
hh3cCallHistoryTerminateTime = _Hh3cCallHistoryTerminateTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 4),
    _Hh3cCallHistoryTerminateTime_Type()
)
hh3cCallHistoryTerminateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryTerminateTime.setStatus("current")
_Hh3cCallHistoryPeerAddress_Type = DisplayString
_Hh3cCallHistoryPeerAddress_Object = MibTableColumn
hh3cCallHistoryPeerAddress = _Hh3cCallHistoryPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 5),
    _Hh3cCallHistoryPeerAddress_Type()
)
hh3cCallHistoryPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryPeerAddress.setStatus("current")


class _Hh3cCallHistoryPeerId_Type(Integer32):
    """Custom type hh3cCallHistoryPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cCallHistoryPeerId_Type.__name__ = "Integer32"
_Hh3cCallHistoryPeerId_Object = MibTableColumn
hh3cCallHistoryPeerId = _Hh3cCallHistoryPeerId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 6),
    _Hh3cCallHistoryPeerId_Type()
)
hh3cCallHistoryPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryPeerId.setStatus("current")
_Hh3cCallHistoryLogicalIfIndex_Type = InterfaceIndexOrZero
_Hh3cCallHistoryLogicalIfIndex_Object = MibTableColumn
hh3cCallHistoryLogicalIfIndex = _Hh3cCallHistoryLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 7),
    _Hh3cCallHistoryLogicalIfIndex_Type()
)
hh3cCallHistoryLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryLogicalIfIndex.setStatus("current")


class _Hh3cCallHistoryCallOrigin_Type(Integer32):
    """Custom type hh3cCallHistoryCallOrigin based on Integer32"""
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


_Hh3cCallHistoryCallOrigin_Type.__name__ = "Integer32"
_Hh3cCallHistoryCallOrigin_Object = MibTableColumn
hh3cCallHistoryCallOrigin = _Hh3cCallHistoryCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 8),
    _Hh3cCallHistoryCallOrigin_Type()
)
hh3cCallHistoryCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryCallOrigin.setStatus("current")
_Hh3cCallHistoryChargedUnits_Type = AbsoluteCounter32
_Hh3cCallHistoryChargedUnits_Object = MibTableColumn
hh3cCallHistoryChargedUnits = _Hh3cCallHistoryChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 9),
    _Hh3cCallHistoryChargedUnits_Type()
)
hh3cCallHistoryChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryChargedUnits.setStatus("current")


class _Hh3cCallHistoryInfoType_Type(Integer32):
    """Custom type hh3cCallHistoryInfoType based on Integer32"""
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


_Hh3cCallHistoryInfoType_Type.__name__ = "Integer32"
_Hh3cCallHistoryInfoType_Object = MibTableColumn
hh3cCallHistoryInfoType = _Hh3cCallHistoryInfoType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 10),
    _Hh3cCallHistoryInfoType_Type()
)
hh3cCallHistoryInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryInfoType.setStatus("current")
_Hh3cCallHistoryTransmitPackets_Type = AbsoluteCounter32
_Hh3cCallHistoryTransmitPackets_Object = MibTableColumn
hh3cCallHistoryTransmitPackets = _Hh3cCallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 11),
    _Hh3cCallHistoryTransmitPackets_Type()
)
hh3cCallHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryTransmitPackets.setStatus("current")
_Hh3cCallHistoryTransmitBytes_Type = AbsoluteCounter32
_Hh3cCallHistoryTransmitBytes_Object = MibTableColumn
hh3cCallHistoryTransmitBytes = _Hh3cCallHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 12),
    _Hh3cCallHistoryTransmitBytes_Type()
)
hh3cCallHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryTransmitBytes.setStatus("current")
_Hh3cCallHistoryReceivePackets_Type = AbsoluteCounter32
_Hh3cCallHistoryReceivePackets_Object = MibTableColumn
hh3cCallHistoryReceivePackets = _Hh3cCallHistoryReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 13),
    _Hh3cCallHistoryReceivePackets_Type()
)
hh3cCallHistoryReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryReceivePackets.setStatus("current")
_Hh3cCallHistoryReceiveBytes_Type = AbsoluteCounter32
_Hh3cCallHistoryReceiveBytes_Object = MibTableColumn
hh3cCallHistoryReceiveBytes = _Hh3cCallHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 1, 1, 14),
    _Hh3cCallHistoryReceiveBytes_Type()
)
hh3cCallHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCallHistoryReceiveBytes.setStatus("current")
_Hh3cVoiceCallHistoryTable_Object = MibTable
hh3cVoiceCallHistoryTable = _Hh3cVoiceCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVoiceCallHistoryTable.setStatus("current")
_Hh3cVoiceCallHistoryEntry_Object = MibTableRow
hh3cVoiceCallHistoryEntry = _Hh3cVoiceCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2, 1)
)
hh3cVoiceCallHistoryEntry.setIndexNames(
    (0, "HH3C-VOICE-CALL-HISTORY-MIB", "hh3cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoiceCallHistoryEntry.setStatus("current")
_Hh3cVoCallHistoryConnectionId_Type = Hh3cGUid
_Hh3cVoCallHistoryConnectionId_Object = MibTableColumn
hh3cVoCallHistoryConnectionId = _Hh3cVoCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2, 1, 1),
    _Hh3cVoCallHistoryConnectionId_Type()
)
hh3cVoCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallHistoryConnectionId.setStatus("current")
_Hh3cVoCallHistoryTxDuration_Type = Gauge32
_Hh3cVoCallHistoryTxDuration_Object = MibTableColumn
hh3cVoCallHistoryTxDuration = _Hh3cVoCallHistoryTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2, 1, 2),
    _Hh3cVoCallHistoryTxDuration_Type()
)
hh3cVoCallHistoryTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallHistoryTxDuration.setStatus("current")
_Hh3cVoCallHistoryVoiceTxDuration_Type = Gauge32
_Hh3cVoCallHistoryVoiceTxDuration_Object = MibTableColumn
hh3cVoCallHistoryVoiceTxDuration = _Hh3cVoCallHistoryVoiceTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2, 1, 3),
    _Hh3cVoCallHistoryVoiceTxDuration_Type()
)
hh3cVoCallHistoryVoiceTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallHistoryVoiceTxDuration.setStatus("current")
_Hh3cVoCallHistoryFaxTxDuration_Type = Gauge32
_Hh3cVoCallHistoryFaxTxDuration_Object = MibTableColumn
hh3cVoCallHistoryFaxTxDuration = _Hh3cVoCallHistoryFaxTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2, 1, 4),
    _Hh3cVoCallHistoryFaxTxDuration_Type()
)
hh3cVoCallHistoryFaxTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallHistoryFaxTxDuration.setStatus("current")
_Hh3cVoCallHistoryCoderType_Type = Hh3cCodecType
_Hh3cVoCallHistoryCoderType_Object = MibTableColumn
hh3cVoCallHistoryCoderType = _Hh3cVoCallHistoryCoderType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2, 1, 5),
    _Hh3cVoCallHistoryCoderType_Type()
)
hh3cVoCallHistoryCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallHistoryCoderType.setStatus("current")
_Hh3cVoCallHistoryImgPageCount_Type = Gauge32
_Hh3cVoCallHistoryImgPageCount_Object = MibTableColumn
hh3cVoCallHistoryImgPageCount = _Hh3cVoCallHistoryImgPageCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 2, 1, 6),
    _Hh3cVoCallHistoryImgPageCount_Type()
)
hh3cVoCallHistoryImgPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoCallHistoryImgPageCount.setStatus("current")
_Hh3cVoiceVoIPCallHistoryTable_Object = MibTable
hh3cVoiceVoIPCallHistoryTable = _Hh3cVoiceVoIPCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cVoiceVoIPCallHistoryTable.setStatus("current")
_Hh3cVoiceVoIPCallHistoryEntry_Object = MibTableRow
hh3cVoiceVoIPCallHistoryEntry = _Hh3cVoiceVoIPCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1)
)
hh3cVoiceVoIPCallHistoryEntry.setIndexNames(
    (0, "HH3C-VOICE-CALL-HISTORY-MIB", "hh3cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoiceVoIPCallHistoryEntry.setStatus("current")
_Hh3cVoVoIPCallHistoryConnectionId_Type = Hh3cGUid
_Hh3cVoVoIPCallHistoryConnectionId_Object = MibTableColumn
hh3cVoVoIPCallHistoryConnectionId = _Hh3cVoVoIPCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 1),
    _Hh3cVoVoIPCallHistoryConnectionId_Type()
)
hh3cVoVoIPCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryConnectionId.setStatus("current")
_Hh3cVoVoIPCallHistoryRemSigIPType_Type = InetAddressType
_Hh3cVoVoIPCallHistoryRemSigIPType_Object = MibTableColumn
hh3cVoVoIPCallHistoryRemSigIPType = _Hh3cVoVoIPCallHistoryRemSigIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 2),
    _Hh3cVoVoIPCallHistoryRemSigIPType_Type()
)
hh3cVoVoIPCallHistoryRemSigIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryRemSigIPType.setStatus("current")
_Hh3cVoVoIPCallHistoryRemSigIPAddr_Type = InetAddress
_Hh3cVoVoIPCallHistoryRemSigIPAddr_Object = MibTableColumn
hh3cVoVoIPCallHistoryRemSigIPAddr = _Hh3cVoVoIPCallHistoryRemSigIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 3),
    _Hh3cVoVoIPCallHistoryRemSigIPAddr_Type()
)
hh3cVoVoIPCallHistoryRemSigIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryRemSigIPAddr.setStatus("current")


class _Hh3cVoVoIPCallHistoryRemSigPort_Type(Integer32):
    """Custom type hh3cVoVoIPCallHistoryRemSigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVoVoIPCallHistoryRemSigPort_Type.__name__ = "Integer32"
_Hh3cVoVoIPCallHistoryRemSigPort_Object = MibTableColumn
hh3cVoVoIPCallHistoryRemSigPort = _Hh3cVoVoIPCallHistoryRemSigPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 4),
    _Hh3cVoVoIPCallHistoryRemSigPort_Type()
)
hh3cVoVoIPCallHistoryRemSigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryRemSigPort.setStatus("current")
_Hh3cVoVoIPCallHistoryRemMedIPType_Type = InetAddressType
_Hh3cVoVoIPCallHistoryRemMedIPType_Object = MibTableColumn
hh3cVoVoIPCallHistoryRemMedIPType = _Hh3cVoVoIPCallHistoryRemMedIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 5),
    _Hh3cVoVoIPCallHistoryRemMedIPType_Type()
)
hh3cVoVoIPCallHistoryRemMedIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryRemMedIPType.setStatus("current")
_Hh3cVoVoIPCallHistoryRemMedIPAddr_Type = InetAddress
_Hh3cVoVoIPCallHistoryRemMedIPAddr_Object = MibTableColumn
hh3cVoVoIPCallHistoryRemMedIPAddr = _Hh3cVoVoIPCallHistoryRemMedIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 6),
    _Hh3cVoVoIPCallHistoryRemMedIPAddr_Type()
)
hh3cVoVoIPCallHistoryRemMedIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryRemMedIPAddr.setStatus("current")


class _Hh3cVoVoIPCallHistoryRemMedPort_Type(Integer32):
    """Custom type hh3cVoVoIPCallHistoryRemMedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cVoVoIPCallHistoryRemMedPort_Type.__name__ = "Integer32"
_Hh3cVoVoIPCallHistoryRemMedPort_Object = MibTableColumn
hh3cVoVoIPCallHistoryRemMedPort = _Hh3cVoVoIPCallHistoryRemMedPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 7),
    _Hh3cVoVoIPCallHistoryRemMedPort_Type()
)
hh3cVoVoIPCallHistoryRemMedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryRemMedPort.setStatus("current")


class _Hh3cVoVoIPCallHistorySessProtocol_Type(Integer32):
    """Custom type hh3cVoVoIPCallHistorySessProtocol based on Integer32"""
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


_Hh3cVoVoIPCallHistorySessProtocol_Type.__name__ = "Integer32"
_Hh3cVoVoIPCallHistorySessProtocol_Object = MibTableColumn
hh3cVoVoIPCallHistorySessProtocol = _Hh3cVoVoIPCallHistorySessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 8),
    _Hh3cVoVoIPCallHistorySessProtocol_Type()
)
hh3cVoVoIPCallHistorySessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistorySessProtocol.setStatus("current")
_Hh3cVoVoIPCallHistoryCoderType_Type = Hh3cCodecType
_Hh3cVoVoIPCallHistoryCoderType_Object = MibTableColumn
hh3cVoVoIPCallHistoryCoderType = _Hh3cVoVoIPCallHistoryCoderType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 16, 1, 3, 1, 9),
    _Hh3cVoVoIPCallHistoryCoderType_Type()
)
hh3cVoVoIPCallHistoryCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoVoIPCallHistoryCoderType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VOICE-CALL-HISTORY-MIB",
    **{"Hh3cGUid": Hh3cGUid,
       "Hh3cCodecType": Hh3cCodecType,
       "hh3cVoCallHistory": hh3cVoCallHistory,
       "hh3cVoiceCallHistoryObjects": hh3cVoiceCallHistoryObjects,
       "hh3cCallHistoryTable": hh3cCallHistoryTable,
       "hh3cCallHistoryEntry": hh3cCallHistoryEntry,
       "hh3cCallHistoryIndex": hh3cCallHistoryIndex,
       "hh3cCallHistorySetupTime": hh3cCallHistorySetupTime,
       "hh3cCallHistoryConnectTime": hh3cCallHistoryConnectTime,
       "hh3cCallHistoryTerminateTime": hh3cCallHistoryTerminateTime,
       "hh3cCallHistoryPeerAddress": hh3cCallHistoryPeerAddress,
       "hh3cCallHistoryPeerId": hh3cCallHistoryPeerId,
       "hh3cCallHistoryLogicalIfIndex": hh3cCallHistoryLogicalIfIndex,
       "hh3cCallHistoryCallOrigin": hh3cCallHistoryCallOrigin,
       "hh3cCallHistoryChargedUnits": hh3cCallHistoryChargedUnits,
       "hh3cCallHistoryInfoType": hh3cCallHistoryInfoType,
       "hh3cCallHistoryTransmitPackets": hh3cCallHistoryTransmitPackets,
       "hh3cCallHistoryTransmitBytes": hh3cCallHistoryTransmitBytes,
       "hh3cCallHistoryReceivePackets": hh3cCallHistoryReceivePackets,
       "hh3cCallHistoryReceiveBytes": hh3cCallHistoryReceiveBytes,
       "hh3cVoiceCallHistoryTable": hh3cVoiceCallHistoryTable,
       "hh3cVoiceCallHistoryEntry": hh3cVoiceCallHistoryEntry,
       "hh3cVoCallHistoryConnectionId": hh3cVoCallHistoryConnectionId,
       "hh3cVoCallHistoryTxDuration": hh3cVoCallHistoryTxDuration,
       "hh3cVoCallHistoryVoiceTxDuration": hh3cVoCallHistoryVoiceTxDuration,
       "hh3cVoCallHistoryFaxTxDuration": hh3cVoCallHistoryFaxTxDuration,
       "hh3cVoCallHistoryCoderType": hh3cVoCallHistoryCoderType,
       "hh3cVoCallHistoryImgPageCount": hh3cVoCallHistoryImgPageCount,
       "hh3cVoiceVoIPCallHistoryTable": hh3cVoiceVoIPCallHistoryTable,
       "hh3cVoiceVoIPCallHistoryEntry": hh3cVoiceVoIPCallHistoryEntry,
       "hh3cVoVoIPCallHistoryConnectionId": hh3cVoVoIPCallHistoryConnectionId,
       "hh3cVoVoIPCallHistoryRemSigIPType": hh3cVoVoIPCallHistoryRemSigIPType,
       "hh3cVoVoIPCallHistoryRemSigIPAddr": hh3cVoVoIPCallHistoryRemSigIPAddr,
       "hh3cVoVoIPCallHistoryRemSigPort": hh3cVoVoIPCallHistoryRemSigPort,
       "hh3cVoVoIPCallHistoryRemMedIPType": hh3cVoVoIPCallHistoryRemMedIPType,
       "hh3cVoVoIPCallHistoryRemMedIPAddr": hh3cVoVoIPCallHistoryRemMedIPAddr,
       "hh3cVoVoIPCallHistoryRemMedPort": hh3cVoVoIPCallHistoryRemMedPort,
       "hh3cVoVoIPCallHistorySessProtocol": hh3cVoVoIPCallHistorySessProtocol,
       "hh3cVoVoIPCallHistoryCoderType": hh3cVoVoIPCallHistoryCoderType}
)
