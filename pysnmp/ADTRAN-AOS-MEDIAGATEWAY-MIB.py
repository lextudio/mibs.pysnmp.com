# SNMP MIB module (ADTRAN-AOS-MEDIAGATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-MEDIAGATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:08 2024
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

(adGenAOSVoice,) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSVoice")

(adIdentity,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adShared")

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

adGenAOSMediaGatewayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 2)
)
adGenAOSMediaGatewayMIB.setRevisions(
        ("2012-08-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSMediaGateway_ObjectIdentity = ObjectIdentity
adGenAOSMediaGateway = _AdGenAOSMediaGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2)
)
_AdGenAOSMediaGatewayObjects_ObjectIdentity = ObjectIdentity
adGenAOSMediaGatewayObjects = _AdGenAOSMediaGatewayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1)
)
_AdGenAOSRtpSessionTable_Object = MibTable
adGenAOSRtpSessionTable = _AdGenAOSRtpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTable.setStatus("current")
_AdGenAOSRtpSessionEntry_Object = MibTableRow
adGenAOSRtpSessionEntry = _AdGenAOSRtpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1)
)
adGenAOSRtpSessionEntry.setIndexNames(
    (0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionChannelId"),
)
if mibBuilder.loadTexts:
    adGenAOSRtpSessionEntry.setStatus("current")
_AdGenAOSRtpSessionChannelId_Type = Integer32
_AdGenAOSRtpSessionChannelId_Object = MibTableColumn
adGenAOSRtpSessionChannelId = _AdGenAOSRtpSessionChannelId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 1),
    _AdGenAOSRtpSessionChannelId_Type()
)
adGenAOSRtpSessionChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionChannelId.setStatus("current")
_AdGenAOSRtpSessionChannelIdName_Type = DisplayString
_AdGenAOSRtpSessionChannelIdName_Object = MibTableColumn
adGenAOSRtpSessionChannelIdName = _AdGenAOSRtpSessionChannelIdName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 2),
    _AdGenAOSRtpSessionChannelIdName_Type()
)
adGenAOSRtpSessionChannelIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionChannelIdName.setStatus("current")


class _AdGenAOSRtpSessionStatus_Type(Integer32):
    """Custom type adGenAOSRtpSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("allocated", 2),
          ("available", 1),
          ("unavailable", 0))
    )


_AdGenAOSRtpSessionStatus_Type.__name__ = "Integer32"
_AdGenAOSRtpSessionStatus_Object = MibTableColumn
adGenAOSRtpSessionStatus = _AdGenAOSRtpSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 3),
    _AdGenAOSRtpSessionStatus_Type()
)
adGenAOSRtpSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionStatus.setStatus("current")
_AdGenAOSRtpSessionStartTime_Type = DisplayString
_AdGenAOSRtpSessionStartTime_Object = MibTableColumn
adGenAOSRtpSessionStartTime = _AdGenAOSRtpSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 4),
    _AdGenAOSRtpSessionStartTime_Type()
)
adGenAOSRtpSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionStartTime.setStatus("current")
_AdGenAOSRtpSessionDuration_Type = DisplayString
_AdGenAOSRtpSessionDuration_Object = MibTableColumn
adGenAOSRtpSessionDuration = _AdGenAOSRtpSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 5),
    _AdGenAOSRtpSessionDuration_Type()
)
adGenAOSRtpSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionDuration.setStatus("current")


class _AdGenAOSRtpSessionVocoder_Type(Integer32):
    """Custom type adGenAOSRtpSessionVocoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("dynamic100", 12),
          ("dynamic101", 13),
          ("dynamic102", 14),
          ("dynamic103", 15),
          ("dynamic104", 16),
          ("dynamic105", 17),
          ("dynamic106", 18),
          ("dynamic107", 19),
          ("dynamic108", 20),
          ("dynamic109", 21),
          ("dynamic110", 22),
          ("dynamic111", 23),
          ("dynamic112", 24),
          ("dynamic113", 25),
          ("dynamic114", 26),
          ("dynamic115", 27),
          ("dynamic116", 28),
          ("dynamic117", 29),
          ("dynamic118", 30),
          ("dynamic119", 31),
          ("dynamic120", 32),
          ("dynamic121", 33),
          ("dynamic122", 34),
          ("dynamic123", 35),
          ("dynamic124", 36),
          ("dynamic125", 37),
          ("dynamic126", 38),
          ("dynamic127", 39),
          ("dynamic96", 8),
          ("dynamic97", 9),
          ("dynamic98", 10),
          ("dynamic99", 11),
          ("g711alaw", 4),
          ("g711ulaw", 1),
          ("g722", 5),
          ("g723", 3),
          ("g728", 6),
          ("g729a", 7),
          ("gsm", 2),
          ("none", 0))
    )


_AdGenAOSRtpSessionVocoder_Type.__name__ = "Integer32"
_AdGenAOSRtpSessionVocoder_Object = MibTableColumn
adGenAOSRtpSessionVocoder = _AdGenAOSRtpSessionVocoder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 6),
    _AdGenAOSRtpSessionVocoder_Type()
)
adGenAOSRtpSessionVocoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionVocoder.setStatus("current")


class _AdGenAOSRtpSessionVAD_Type(Integer32):
    """Custom type adGenAOSRtpSessionVAD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AdGenAOSRtpSessionVAD_Type.__name__ = "Integer32"
_AdGenAOSRtpSessionVAD_Object = MibTableColumn
adGenAOSRtpSessionVAD = _AdGenAOSRtpSessionVAD_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 7),
    _AdGenAOSRtpSessionVAD_Type()
)
adGenAOSRtpSessionVAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionVAD.setStatus("current")
_AdGenAOSRtpSessionTdmPortDescription_Type = DisplayString
_AdGenAOSRtpSessionTdmPortDescription_Object = MibTableColumn
adGenAOSRtpSessionTdmPortDescription = _AdGenAOSRtpSessionTdmPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 8),
    _AdGenAOSRtpSessionTdmPortDescription_Type()
)
adGenAOSRtpSessionTdmPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTdmPortDescription.setStatus("current")
_AdGenAOSRtpSessionLocalIPAddress_Type = IpAddress
_AdGenAOSRtpSessionLocalIPAddress_Object = MibTableColumn
adGenAOSRtpSessionLocalIPAddress = _AdGenAOSRtpSessionLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 9),
    _AdGenAOSRtpSessionLocalIPAddress_Type()
)
adGenAOSRtpSessionLocalIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionLocalIPAddress.setStatus("current")
_AdGenAOSRtpSessionLocalUdpPort_Type = Integer32
_AdGenAOSRtpSessionLocalUdpPort_Object = MibTableColumn
adGenAOSRtpSessionLocalUdpPort = _AdGenAOSRtpSessionLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 10),
    _AdGenAOSRtpSessionLocalUdpPort_Type()
)
adGenAOSRtpSessionLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionLocalUdpPort.setStatus("current")
_AdGenAOSRtpSessionSIPPortDescription_Type = DisplayString
_AdGenAOSRtpSessionSIPPortDescription_Object = MibTableColumn
adGenAOSRtpSessionSIPPortDescription = _AdGenAOSRtpSessionSIPPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 11),
    _AdGenAOSRtpSessionSIPPortDescription_Type()
)
adGenAOSRtpSessionSIPPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionSIPPortDescription.setStatus("current")
_AdGenAOSRtpSessionRemoteIPAddress_Type = IpAddress
_AdGenAOSRtpSessionRemoteIPAddress_Object = MibTableColumn
adGenAOSRtpSessionRemoteIPAddress = _AdGenAOSRtpSessionRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 12),
    _AdGenAOSRtpSessionRemoteIPAddress_Type()
)
adGenAOSRtpSessionRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRemoteIPAddress.setStatus("current")
_AdGenAOSRtpSessionRemoteUdpPort_Type = Integer32
_AdGenAOSRtpSessionRemoteUdpPort_Object = MibTableColumn
adGenAOSRtpSessionRemoteUdpPort = _AdGenAOSRtpSessionRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 13),
    _AdGenAOSRtpSessionRemoteUdpPort_Type()
)
adGenAOSRtpSessionRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRemoteUdpPort.setStatus("current")
_AdGenAOSRtpSessionTxFramesPerPacket_Type = Integer32
_AdGenAOSRtpSessionTxFramesPerPacket_Object = MibTableColumn
adGenAOSRtpSessionTxFramesPerPacket = _AdGenAOSRtpSessionTxFramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 14),
    _AdGenAOSRtpSessionTxFramesPerPacket_Type()
)
adGenAOSRtpSessionTxFramesPerPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTxFramesPerPacket.setStatus("current")


class _AdGenAOSRtpSessionEchoCancellerEnabled_Type(Integer32):
    """Custom type adGenAOSRtpSessionEchoCancellerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AdGenAOSRtpSessionEchoCancellerEnabled_Type.__name__ = "Integer32"
_AdGenAOSRtpSessionEchoCancellerEnabled_Object = MibTableColumn
adGenAOSRtpSessionEchoCancellerEnabled = _AdGenAOSRtpSessionEchoCancellerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 15),
    _AdGenAOSRtpSessionEchoCancellerEnabled_Type()
)
adGenAOSRtpSessionEchoCancellerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionEchoCancellerEnabled.setStatus("current")
_AdGenAOSRtpSessionRxPackets_Type = Integer32
_AdGenAOSRtpSessionRxPackets_Object = MibTableColumn
adGenAOSRtpSessionRxPackets = _AdGenAOSRtpSessionRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 22),
    _AdGenAOSRtpSessionRxPackets_Type()
)
adGenAOSRtpSessionRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxPackets.setStatus("current")
_AdGenAOSRtpSessionRxOctets_Type = Integer32
_AdGenAOSRtpSessionRxOctets_Object = MibTableColumn
adGenAOSRtpSessionRxOctets = _AdGenAOSRtpSessionRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 23),
    _AdGenAOSRtpSessionRxOctets_Type()
)
adGenAOSRtpSessionRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxOctets.setStatus("current")
_AdGenAOSRtpSessionRxPacketsLost_Type = Integer32
_AdGenAOSRtpSessionRxPacketsLost_Object = MibTableColumn
adGenAOSRtpSessionRxPacketsLost = _AdGenAOSRtpSessionRxPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 24),
    _AdGenAOSRtpSessionRxPacketsLost_Type()
)
adGenAOSRtpSessionRxPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxPacketsLost.setStatus("obsolete")
_AdGenAOSRtpSessionRxPacketsUnknown_Type = Integer32
_AdGenAOSRtpSessionRxPacketsUnknown_Object = MibTableColumn
adGenAOSRtpSessionRxPacketsUnknown = _AdGenAOSRtpSessionRxPacketsUnknown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 25),
    _AdGenAOSRtpSessionRxPacketsUnknown_Type()
)
adGenAOSRtpSessionRxPacketsUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxPacketsUnknown.setStatus("current")
_AdGenAOSRtpSessionRxJitterBufferDepth_Type = Integer32
_AdGenAOSRtpSessionRxJitterBufferDepth_Object = MibTableColumn
adGenAOSRtpSessionRxJitterBufferDepth = _AdGenAOSRtpSessionRxJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 26),
    _AdGenAOSRtpSessionRxJitterBufferDepth_Type()
)
adGenAOSRtpSessionRxJitterBufferDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxJitterBufferDepth.setStatus("current")
_AdGenAOSRtpSessionRxMaxJitterBufferDepth_Type = Integer32
_AdGenAOSRtpSessionRxMaxJitterBufferDepth_Object = MibTableColumn
adGenAOSRtpSessionRxMaxJitterBufferDepth = _AdGenAOSRtpSessionRxMaxJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 27),
    _AdGenAOSRtpSessionRxMaxJitterBufferDepth_Type()
)
adGenAOSRtpSessionRxMaxJitterBufferDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxMaxJitterBufferDepth.setStatus("current")
_AdGenAOSRtpSessionRxFrameLateDiscards_Type = Integer32
_AdGenAOSRtpSessionRxFrameLateDiscards_Object = MibTableColumn
adGenAOSRtpSessionRxFrameLateDiscards = _AdGenAOSRtpSessionRxFrameLateDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 30),
    _AdGenAOSRtpSessionRxFrameLateDiscards_Type()
)
adGenAOSRtpSessionRxFrameLateDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxFrameLateDiscards.setStatus("obsolete")
_AdGenAOSRtpSessionRxFrameOverflows_Type = Integer32
_AdGenAOSRtpSessionRxFrameOverflows_Object = MibTableColumn
adGenAOSRtpSessionRxFrameOverflows = _AdGenAOSRtpSessionRxFrameOverflows_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 31),
    _AdGenAOSRtpSessionRxFrameOverflows_Type()
)
adGenAOSRtpSessionRxFrameOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxFrameOverflows.setStatus("obsolete")
_AdGenAOSRtpSessionRxFrameOutOfOrders_Type = Integer32
_AdGenAOSRtpSessionRxFrameOutOfOrders_Object = MibTableColumn
adGenAOSRtpSessionRxFrameOutOfOrders = _AdGenAOSRtpSessionRxFrameOutOfOrders_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 33),
    _AdGenAOSRtpSessionRxFrameOutOfOrders_Type()
)
adGenAOSRtpSessionRxFrameOutOfOrders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxFrameOutOfOrders.setStatus("current")
_AdGenAOSRtpSessionRxSyncSource_Type = Integer32
_AdGenAOSRtpSessionRxSyncSource_Object = MibTableColumn
adGenAOSRtpSessionRxSyncSource = _AdGenAOSRtpSessionRxSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 34),
    _AdGenAOSRtpSessionRxSyncSource_Type()
)
adGenAOSRtpSessionRxSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionRxSyncSource.setStatus("current")
_AdGenAOSRtpSessionTxPackets_Type = Integer32
_AdGenAOSRtpSessionTxPackets_Object = MibTableColumn
adGenAOSRtpSessionTxPackets = _AdGenAOSRtpSessionTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 35),
    _AdGenAOSRtpSessionTxPackets_Type()
)
adGenAOSRtpSessionTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTxPackets.setStatus("current")
_AdGenAOSRtpSessionTxOctets_Type = Integer32
_AdGenAOSRtpSessionTxOctets_Object = MibTableColumn
adGenAOSRtpSessionTxOctets = _AdGenAOSRtpSessionTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 36),
    _AdGenAOSRtpSessionTxOctets_Type()
)
adGenAOSRtpSessionTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTxOctets.setStatus("current")
_AdGenAOSRtpSessionTxSyncSource_Type = Integer32
_AdGenAOSRtpSessionTxSyncSource_Object = MibTableColumn
adGenAOSRtpSessionTxSyncSource = _AdGenAOSRtpSessionTxSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 1, 1, 37),
    _AdGenAOSRtpSessionTxSyncSource_Type()
)
adGenAOSRtpSessionTxSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTxSyncSource.setStatus("current")
_AdGenAOSRtpSessionTotalsTable_Object = MibTable
adGenAOSRtpSessionTotalsTable = _AdGenAOSRtpSessionTotalsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsTable.setStatus("current")
_AdGenAOSRtpSessionTotalsEntry_Object = MibTableRow
adGenAOSRtpSessionTotalsEntry = _AdGenAOSRtpSessionTotalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1)
)
adGenAOSRtpSessionTotalsEntry.setIndexNames(
    (0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsSessions"),
)
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsEntry.setStatus("current")
_AdGenAOSRtpSessionTotalsSessions_Type = Integer32
_AdGenAOSRtpSessionTotalsSessions_Object = MibTableColumn
adGenAOSRtpSessionTotalsSessions = _AdGenAOSRtpSessionTotalsSessions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 1),
    _AdGenAOSRtpSessionTotalsSessions_Type()
)
adGenAOSRtpSessionTotalsSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsSessions.setStatus("current")
_AdGenAOSRtpSessionTotalsSessionDuration_Type = DisplayString
_AdGenAOSRtpSessionTotalsSessionDuration_Object = MibTableColumn
adGenAOSRtpSessionTotalsSessionDuration = _AdGenAOSRtpSessionTotalsSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 2),
    _AdGenAOSRtpSessionTotalsSessionDuration_Type()
)
adGenAOSRtpSessionTotalsSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsSessionDuration.setStatus("current")
_AdGenAOSRtpSessionTotalsRxPackets_Type = Integer32
_AdGenAOSRtpSessionTotalsRxPackets_Object = MibTableColumn
adGenAOSRtpSessionTotalsRxPackets = _AdGenAOSRtpSessionTotalsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 3),
    _AdGenAOSRtpSessionTotalsRxPackets_Type()
)
adGenAOSRtpSessionTotalsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsRxPackets.setStatus("current")
_AdGenAOSRtpSessionTotalsRxOctets_Type = Integer32
_AdGenAOSRtpSessionTotalsRxOctets_Object = MibTableColumn
adGenAOSRtpSessionTotalsRxOctets = _AdGenAOSRtpSessionTotalsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 4),
    _AdGenAOSRtpSessionTotalsRxOctets_Type()
)
adGenAOSRtpSessionTotalsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsRxOctets.setStatus("current")
_AdGenAOSRtpSessionTotalsRxPacketsLost_Type = Integer32
_AdGenAOSRtpSessionTotalsRxPacketsLost_Object = MibTableColumn
adGenAOSRtpSessionTotalsRxPacketsLost = _AdGenAOSRtpSessionTotalsRxPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 5),
    _AdGenAOSRtpSessionTotalsRxPacketsLost_Type()
)
adGenAOSRtpSessionTotalsRxPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsRxPacketsLost.setStatus("obsolete")
_AdGenAOSRtpSessionTotalsRxPacketsUnknown_Type = Integer32
_AdGenAOSRtpSessionTotalsRxPacketsUnknown_Object = MibTableColumn
adGenAOSRtpSessionTotalsRxPacketsUnknown = _AdGenAOSRtpSessionTotalsRxPacketsUnknown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 6),
    _AdGenAOSRtpSessionTotalsRxPacketsUnknown_Type()
)
adGenAOSRtpSessionTotalsRxPacketsUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsRxPacketsUnknown.setStatus("current")
_AdGenAOSRtpSessionTotalsTxPackets_Type = Integer32
_AdGenAOSRtpSessionTotalsTxPackets_Object = MibTableColumn
adGenAOSRtpSessionTotalsTxPackets = _AdGenAOSRtpSessionTotalsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 7),
    _AdGenAOSRtpSessionTotalsTxPackets_Type()
)
adGenAOSRtpSessionTotalsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsTxPackets.setStatus("current")
_AdGenAOSRtpSessionTotalsTxOctets_Type = Integer32
_AdGenAOSRtpSessionTotalsTxOctets_Object = MibTableColumn
adGenAOSRtpSessionTotalsTxOctets = _AdGenAOSRtpSessionTotalsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 8),
    _AdGenAOSRtpSessionTotalsTxOctets_Type()
)
adGenAOSRtpSessionTotalsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsTxOctets.setStatus("current")
_AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Type = Integer32
_AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Object = MibTableColumn
adGenAOSRtpSessionTotalsRxFrameLateDiscards = _AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 9),
    _AdGenAOSRtpSessionTotalsRxFrameLateDiscards_Type()
)
adGenAOSRtpSessionTotalsRxFrameLateDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsRxFrameLateDiscards.setStatus("obsolete")
_AdGenAOSRtpSessionTotalsRxFrameOverflows_Type = Integer32
_AdGenAOSRtpSessionTotalsRxFrameOverflows_Object = MibTableColumn
adGenAOSRtpSessionTotalsRxFrameOverflows = _AdGenAOSRtpSessionTotalsRxFrameOverflows_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 11),
    _AdGenAOSRtpSessionTotalsRxFrameOverflows_Type()
)
adGenAOSRtpSessionTotalsRxFrameOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsRxFrameOverflows.setStatus("obsolete")
_AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Type = Integer32
_AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Object = MibTableColumn
adGenAOSRtpSessionTotalsRxFrameOutOfOrders = _AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 12),
    _AdGenAOSRtpSessionTotalsRxFrameOutOfOrders_Type()
)
adGenAOSRtpSessionTotalsRxFrameOutOfOrders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsRxFrameOutOfOrders.setStatus("current")
_AdGenAOSRtpSessionTotalsClearCounters_Type = Integer32
_AdGenAOSRtpSessionTotalsClearCounters_Object = MibTableColumn
adGenAOSRtpSessionTotalsClearCounters = _AdGenAOSRtpSessionTotalsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 13),
    _AdGenAOSRtpSessionTotalsClearCounters_Type()
)
adGenAOSRtpSessionTotalsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsClearCounters.setStatus("current")
_AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Type = DisplayString
_AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Object = MibTableColumn
adGenAOSRtpSessionTotalsTimeSinceLastClearCounters = _AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 2, 1, 14),
    _AdGenAOSRtpSessionTotalsTimeSinceLastClearCounters_Type()
)
adGenAOSRtpSessionTotalsTimeSinceLastClearCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpSessionTotalsTimeSinceLastClearCounters.setStatus("current")
_AdGenAOSMediaGatewayInfoTable_Object = MibTable
adGenAOSMediaGatewayInfoTable = _AdGenAOSMediaGatewayInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoTable.setStatus("current")
_AdGenAOSMediaGatewayInfoEntry_Object = MibTableRow
adGenAOSMediaGatewayInfoEntry = _AdGenAOSMediaGatewayInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1)
)
adGenAOSMediaGatewayInfoEntry.setIndexNames(
    (0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoIdentifier"),
)
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoEntry.setStatus("current")
_AdGenAOSMediaGatewayInfoIdentifier_Type = Integer32
_AdGenAOSMediaGatewayInfoIdentifier_Object = MibTableColumn
adGenAOSMediaGatewayInfoIdentifier = _AdGenAOSMediaGatewayInfoIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 1),
    _AdGenAOSMediaGatewayInfoIdentifier_Type()
)
adGenAOSMediaGatewayInfoIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoIdentifier.setStatus("current")
_AdGenAOSMediaGatewayInfoSoftwareVersion_Type = DisplayString
_AdGenAOSMediaGatewayInfoSoftwareVersion_Object = MibTableColumn
adGenAOSMediaGatewayInfoSoftwareVersion = _AdGenAOSMediaGatewayInfoSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 2),
    _AdGenAOSMediaGatewayInfoSoftwareVersion_Type()
)
adGenAOSMediaGatewayInfoSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoSoftwareVersion.setStatus("current")
_AdGenAOSMediaGatewayInfoUtilization_Type = Integer32
_AdGenAOSMediaGatewayInfoUtilization_Object = MibTableColumn
adGenAOSMediaGatewayInfoUtilization = _AdGenAOSMediaGatewayInfoUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 3),
    _AdGenAOSMediaGatewayInfoUtilization_Type()
)
adGenAOSMediaGatewayInfoUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoUtilization.setStatus("current")
_AdGenAOSMediaGatewayInfoUtilizationMaximum_Type = Integer32
_AdGenAOSMediaGatewayInfoUtilizationMaximum_Object = MibTableColumn
adGenAOSMediaGatewayInfoUtilizationMaximum = _AdGenAOSMediaGatewayInfoUtilizationMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 4),
    _AdGenAOSMediaGatewayInfoUtilizationMaximum_Type()
)
adGenAOSMediaGatewayInfoUtilizationMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoUtilizationMaximum.setStatus("current")
_AdGenAOSMediaGatewayInfoFreePacketBuffers_Type = Integer32
_AdGenAOSMediaGatewayInfoFreePacketBuffers_Object = MibTableColumn
adGenAOSMediaGatewayInfoFreePacketBuffers = _AdGenAOSMediaGatewayInfoFreePacketBuffers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 5),
    _AdGenAOSMediaGatewayInfoFreePacketBuffers_Type()
)
adGenAOSMediaGatewayInfoFreePacketBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoFreePacketBuffers.setStatus("current")
_AdGenAOSMediaGatewayInfoUptime_Type = DisplayString
_AdGenAOSMediaGatewayInfoUptime_Object = MibTableColumn
adGenAOSMediaGatewayInfoUptime = _AdGenAOSMediaGatewayInfoUptime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 3, 1, 6),
    _AdGenAOSMediaGatewayInfoUptime_Type()
)
adGenAOSMediaGatewayInfoUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoUptime.setStatus("current")
_AdGenAOSRtpChannelTotalTable_Object = MibTable
adGenAOSRtpChannelTotalTable = _AdGenAOSRtpChannelTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalTable.setStatus("current")
_AdGenAOSRtpChannelTotalEntry_Object = MibTableRow
adGenAOSRtpChannelTotalEntry = _AdGenAOSRtpChannelTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1)
)
adGenAOSRtpChannelTotalEntry.setIndexNames(
    (0, "ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalId"),
)
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalEntry.setStatus("current")
_AdGenAOSRtpChannelTotalId_Type = Integer32
_AdGenAOSRtpChannelTotalId_Object = MibTableColumn
adGenAOSRtpChannelTotalId = _AdGenAOSRtpChannelTotalId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 1),
    _AdGenAOSRtpChannelTotalId_Type()
)
adGenAOSRtpChannelTotalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalId.setStatus("current")
_AdGenAOSRtpChannelTotalIdName_Type = DisplayString
_AdGenAOSRtpChannelTotalIdName_Object = MibTableColumn
adGenAOSRtpChannelTotalIdName = _AdGenAOSRtpChannelTotalIdName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 2),
    _AdGenAOSRtpChannelTotalIdName_Type()
)
adGenAOSRtpChannelTotalIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalIdName.setStatus("current")
_AdGenAOSRtpChannelTotalSessions_Type = Integer32
_AdGenAOSRtpChannelTotalSessions_Object = MibTableColumn
adGenAOSRtpChannelTotalSessions = _AdGenAOSRtpChannelTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 3),
    _AdGenAOSRtpChannelTotalSessions_Type()
)
adGenAOSRtpChannelTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalSessions.setStatus("current")
_AdGenAOSRtpChannelTotalSessionDuration_Type = DisplayString
_AdGenAOSRtpChannelTotalSessionDuration_Object = MibTableColumn
adGenAOSRtpChannelTotalSessionDuration = _AdGenAOSRtpChannelTotalSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 4),
    _AdGenAOSRtpChannelTotalSessionDuration_Type()
)
adGenAOSRtpChannelTotalSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalSessionDuration.setStatus("current")
_AdGenAOSRtpChannelTotalRxPackets_Type = Integer32
_AdGenAOSRtpChannelTotalRxPackets_Object = MibTableColumn
adGenAOSRtpChannelTotalRxPackets = _AdGenAOSRtpChannelTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 5),
    _AdGenAOSRtpChannelTotalRxPackets_Type()
)
adGenAOSRtpChannelTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxPackets.setStatus("current")
_AdGenAOSRtpChannelTotalRxOctets_Type = Integer32
_AdGenAOSRtpChannelTotalRxOctets_Object = MibTableColumn
adGenAOSRtpChannelTotalRxOctets = _AdGenAOSRtpChannelTotalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 6),
    _AdGenAOSRtpChannelTotalRxOctets_Type()
)
adGenAOSRtpChannelTotalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxOctets.setStatus("current")
_AdGenAOSRtpChannelTotalRxPacketsLost_Type = Integer32
_AdGenAOSRtpChannelTotalRxPacketsLost_Object = MibTableColumn
adGenAOSRtpChannelTotalRxPacketsLost = _AdGenAOSRtpChannelTotalRxPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 7),
    _AdGenAOSRtpChannelTotalRxPacketsLost_Type()
)
adGenAOSRtpChannelTotalRxPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxPacketsLost.setStatus("obsolete")
_AdGenAOSRtpChannelTotalRxPacketsUnknown_Type = Integer32
_AdGenAOSRtpChannelTotalRxPacketsUnknown_Object = MibTableColumn
adGenAOSRtpChannelTotalRxPacketsUnknown = _AdGenAOSRtpChannelTotalRxPacketsUnknown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 8),
    _AdGenAOSRtpChannelTotalRxPacketsUnknown_Type()
)
adGenAOSRtpChannelTotalRxPacketsUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxPacketsUnknown.setStatus("current")
_AdGenAOSRtpChannelTotalTxPackets_Type = Integer32
_AdGenAOSRtpChannelTotalTxPackets_Object = MibTableColumn
adGenAOSRtpChannelTotalTxPackets = _AdGenAOSRtpChannelTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 9),
    _AdGenAOSRtpChannelTotalTxPackets_Type()
)
adGenAOSRtpChannelTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalTxPackets.setStatus("current")
_AdGenAOSRtpChannelTotalTxOctets_Type = Integer32
_AdGenAOSRtpChannelTotalTxOctets_Object = MibTableColumn
adGenAOSRtpChannelTotalTxOctets = _AdGenAOSRtpChannelTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 10),
    _AdGenAOSRtpChannelTotalTxOctets_Type()
)
adGenAOSRtpChannelTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalTxOctets.setStatus("current")
_AdGenAOSRtpChannelTotalRxMaxDepth_Type = Integer32
_AdGenAOSRtpChannelTotalRxMaxDepth_Object = MibTableColumn
adGenAOSRtpChannelTotalRxMaxDepth = _AdGenAOSRtpChannelTotalRxMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 11),
    _AdGenAOSRtpChannelTotalRxMaxDepth_Type()
)
adGenAOSRtpChannelTotalRxMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxMaxDepth.setStatus("obsolete")
_AdGenAOSRtpChannelTotalRxFrameLateDiscards_Type = Integer32
_AdGenAOSRtpChannelTotalRxFrameLateDiscards_Object = MibTableColumn
adGenAOSRtpChannelTotalRxFrameLateDiscards = _AdGenAOSRtpChannelTotalRxFrameLateDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 12),
    _AdGenAOSRtpChannelTotalRxFrameLateDiscards_Type()
)
adGenAOSRtpChannelTotalRxFrameLateDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxFrameLateDiscards.setStatus("obsolete")
_AdGenAOSRtpChannelTotalRxFrameOverflows_Type = Integer32
_AdGenAOSRtpChannelTotalRxFrameOverflows_Object = MibTableColumn
adGenAOSRtpChannelTotalRxFrameOverflows = _AdGenAOSRtpChannelTotalRxFrameOverflows_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 14),
    _AdGenAOSRtpChannelTotalRxFrameOverflows_Type()
)
adGenAOSRtpChannelTotalRxFrameOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxFrameOverflows.setStatus("obsolete")
_AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Type = Integer32
_AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Object = MibTableColumn
adGenAOSRtpChannelTotalRxFrameOutOfOrders = _AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 15),
    _AdGenAOSRtpChannelTotalRxFrameOutOfOrders_Type()
)
adGenAOSRtpChannelTotalRxFrameOutOfOrders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTotalRxFrameOutOfOrders.setStatus("current")
_AdGenAOSRtpChannelClearCounters_Type = Integer32
_AdGenAOSRtpChannelClearCounters_Object = MibTableColumn
adGenAOSRtpChannelClearCounters = _AdGenAOSRtpChannelClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 16),
    _AdGenAOSRtpChannelClearCounters_Type()
)
adGenAOSRtpChannelClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelClearCounters.setStatus("current")
_AdGenAOSRtpChannelTimeSinceLastClearCounters_Type = DisplayString
_AdGenAOSRtpChannelTimeSinceLastClearCounters_Object = MibTableColumn
adGenAOSRtpChannelTimeSinceLastClearCounters = _AdGenAOSRtpChannelTimeSinceLastClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 1, 4, 1, 17),
    _AdGenAOSRtpChannelTimeSinceLastClearCounters_Type()
)
adGenAOSRtpChannelTimeSinceLastClearCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSRtpChannelTimeSinceLastClearCounters.setStatus("current")
_AdGenAOSMediaGatewayConformance_ObjectIdentity = ObjectIdentity
adGenAOSMediaGatewayConformance = _AdGenAOSMediaGatewayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99)
)
_AdGenAOSMediaGatewayCompliances_ObjectIdentity = ObjectIdentity
adGenAOSMediaGatewayCompliances = _AdGenAOSMediaGatewayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 1)
)
_AdGenAOSMediaGatewayMIBGroups_ObjectIdentity = ObjectIdentity
adGenAOSMediaGatewayMIBGroups = _AdGenAOSMediaGatewayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2)
)

# Managed Objects groups

adGenAOSMediaGatewayRtpSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 1)
)
adGenAOSMediaGatewayRtpSessionGroup.setObjects(
      *(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionChannelId"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionChannelIdName"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionStatus"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionStartTime"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionDuration"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionVocoder"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionVAD"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTdmPortDescription"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionLocalIPAddress"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionLocalUdpPort"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionSIPPortDescription"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRemoteIPAddress"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRemoteUdpPort"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxFramesPerPacket"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionEchoCancellerEnabled"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxPackets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxOctets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxPacketsLost"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxPacketsUnknown"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxJitterBufferDepth"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxMaxJitterBufferDepth"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxFrameLateDiscards"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxFrameOverflows"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxFrameOutOfOrders"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionRxSyncSource"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxPackets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxOctets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTxSyncSource"))
)
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayRtpSessionGroup.setStatus("current")

adGenAOSMediaGatewayRtpSessionTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 2)
)
adGenAOSMediaGatewayRtpSessionTotalsGroup.setObjects(
      *(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsSessions"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsSessionDuration"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxPackets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxOctets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxPacketsLost"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxPacketsUnknown"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsTxPackets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsTxOctets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxFrameLateDiscards"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxFrameOverflows"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsRxFrameOutOfOrders"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsClearCounters"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpSessionTotalsTimeSinceLastClearCounters"))
)
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayRtpSessionTotalsGroup.setStatus("current")

adGenAOSMediaGatewayInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 3)
)
adGenAOSMediaGatewayInfoGroup.setObjects(
      *(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoIdentifier"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoSoftwareVersion"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoUtilization"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoUtilizationMaximum"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoFreePacketBuffers"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSMediaGatewayInfoUptime"))
)
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayInfoGroup.setStatus("current")

adGenAOSMediaGatewayRtpChannelTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 2, 4)
)
adGenAOSMediaGatewayRtpChannelTotalsGroup.setObjects(
      *(("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalId"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalIdName"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalSessions"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalSessionDuration"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxPackets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxOctets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxPacketsLost"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxPacketsUnknown"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalTxPackets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalTxOctets"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxMaxDepth"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxFrameLateDiscards"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxFrameOverflows"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTotalRxFrameOutOfOrders"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelClearCounters"),
        ("ADTRAN-AOS-MEDIAGATEWAY-MIB", "adGenAOSRtpChannelTimeSinceLastClearCounters"))
)
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayRtpChannelTotalsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAOSMediaGatewayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 2, 99, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAOSMediaGatewayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-MEDIAGATEWAY-MIB",
    **{"adGenAOSMediaGateway": adGenAOSMediaGateway,
       "adGenAOSMediaGatewayObjects": adGenAOSMediaGatewayObjects,
       "adGenAOSRtpSessionTable": adGenAOSRtpSessionTable,
       "adGenAOSRtpSessionEntry": adGenAOSRtpSessionEntry,
       "adGenAOSRtpSessionChannelId": adGenAOSRtpSessionChannelId,
       "adGenAOSRtpSessionChannelIdName": adGenAOSRtpSessionChannelIdName,
       "adGenAOSRtpSessionStatus": adGenAOSRtpSessionStatus,
       "adGenAOSRtpSessionStartTime": adGenAOSRtpSessionStartTime,
       "adGenAOSRtpSessionDuration": adGenAOSRtpSessionDuration,
       "adGenAOSRtpSessionVocoder": adGenAOSRtpSessionVocoder,
       "adGenAOSRtpSessionVAD": adGenAOSRtpSessionVAD,
       "adGenAOSRtpSessionTdmPortDescription": adGenAOSRtpSessionTdmPortDescription,
       "adGenAOSRtpSessionLocalIPAddress": adGenAOSRtpSessionLocalIPAddress,
       "adGenAOSRtpSessionLocalUdpPort": adGenAOSRtpSessionLocalUdpPort,
       "adGenAOSRtpSessionSIPPortDescription": adGenAOSRtpSessionSIPPortDescription,
       "adGenAOSRtpSessionRemoteIPAddress": adGenAOSRtpSessionRemoteIPAddress,
       "adGenAOSRtpSessionRemoteUdpPort": adGenAOSRtpSessionRemoteUdpPort,
       "adGenAOSRtpSessionTxFramesPerPacket": adGenAOSRtpSessionTxFramesPerPacket,
       "adGenAOSRtpSessionEchoCancellerEnabled": adGenAOSRtpSessionEchoCancellerEnabled,
       "adGenAOSRtpSessionRxPackets": adGenAOSRtpSessionRxPackets,
       "adGenAOSRtpSessionRxOctets": adGenAOSRtpSessionRxOctets,
       "adGenAOSRtpSessionRxPacketsLost": adGenAOSRtpSessionRxPacketsLost,
       "adGenAOSRtpSessionRxPacketsUnknown": adGenAOSRtpSessionRxPacketsUnknown,
       "adGenAOSRtpSessionRxJitterBufferDepth": adGenAOSRtpSessionRxJitterBufferDepth,
       "adGenAOSRtpSessionRxMaxJitterBufferDepth": adGenAOSRtpSessionRxMaxJitterBufferDepth,
       "adGenAOSRtpSessionRxFrameLateDiscards": adGenAOSRtpSessionRxFrameLateDiscards,
       "adGenAOSRtpSessionRxFrameOverflows": adGenAOSRtpSessionRxFrameOverflows,
       "adGenAOSRtpSessionRxFrameOutOfOrders": adGenAOSRtpSessionRxFrameOutOfOrders,
       "adGenAOSRtpSessionRxSyncSource": adGenAOSRtpSessionRxSyncSource,
       "adGenAOSRtpSessionTxPackets": adGenAOSRtpSessionTxPackets,
       "adGenAOSRtpSessionTxOctets": adGenAOSRtpSessionTxOctets,
       "adGenAOSRtpSessionTxSyncSource": adGenAOSRtpSessionTxSyncSource,
       "adGenAOSRtpSessionTotalsTable": adGenAOSRtpSessionTotalsTable,
       "adGenAOSRtpSessionTotalsEntry": adGenAOSRtpSessionTotalsEntry,
       "adGenAOSRtpSessionTotalsSessions": adGenAOSRtpSessionTotalsSessions,
       "adGenAOSRtpSessionTotalsSessionDuration": adGenAOSRtpSessionTotalsSessionDuration,
       "adGenAOSRtpSessionTotalsRxPackets": adGenAOSRtpSessionTotalsRxPackets,
       "adGenAOSRtpSessionTotalsRxOctets": adGenAOSRtpSessionTotalsRxOctets,
       "adGenAOSRtpSessionTotalsRxPacketsLost": adGenAOSRtpSessionTotalsRxPacketsLost,
       "adGenAOSRtpSessionTotalsRxPacketsUnknown": adGenAOSRtpSessionTotalsRxPacketsUnknown,
       "adGenAOSRtpSessionTotalsTxPackets": adGenAOSRtpSessionTotalsTxPackets,
       "adGenAOSRtpSessionTotalsTxOctets": adGenAOSRtpSessionTotalsTxOctets,
       "adGenAOSRtpSessionTotalsRxFrameLateDiscards": adGenAOSRtpSessionTotalsRxFrameLateDiscards,
       "adGenAOSRtpSessionTotalsRxFrameOverflows": adGenAOSRtpSessionTotalsRxFrameOverflows,
       "adGenAOSRtpSessionTotalsRxFrameOutOfOrders": adGenAOSRtpSessionTotalsRxFrameOutOfOrders,
       "adGenAOSRtpSessionTotalsClearCounters": adGenAOSRtpSessionTotalsClearCounters,
       "adGenAOSRtpSessionTotalsTimeSinceLastClearCounters": adGenAOSRtpSessionTotalsTimeSinceLastClearCounters,
       "adGenAOSMediaGatewayInfoTable": adGenAOSMediaGatewayInfoTable,
       "adGenAOSMediaGatewayInfoEntry": adGenAOSMediaGatewayInfoEntry,
       "adGenAOSMediaGatewayInfoIdentifier": adGenAOSMediaGatewayInfoIdentifier,
       "adGenAOSMediaGatewayInfoSoftwareVersion": adGenAOSMediaGatewayInfoSoftwareVersion,
       "adGenAOSMediaGatewayInfoUtilization": adGenAOSMediaGatewayInfoUtilization,
       "adGenAOSMediaGatewayInfoUtilizationMaximum": adGenAOSMediaGatewayInfoUtilizationMaximum,
       "adGenAOSMediaGatewayInfoFreePacketBuffers": adGenAOSMediaGatewayInfoFreePacketBuffers,
       "adGenAOSMediaGatewayInfoUptime": adGenAOSMediaGatewayInfoUptime,
       "adGenAOSRtpChannelTotalTable": adGenAOSRtpChannelTotalTable,
       "adGenAOSRtpChannelTotalEntry": adGenAOSRtpChannelTotalEntry,
       "adGenAOSRtpChannelTotalId": adGenAOSRtpChannelTotalId,
       "adGenAOSRtpChannelTotalIdName": adGenAOSRtpChannelTotalIdName,
       "adGenAOSRtpChannelTotalSessions": adGenAOSRtpChannelTotalSessions,
       "adGenAOSRtpChannelTotalSessionDuration": adGenAOSRtpChannelTotalSessionDuration,
       "adGenAOSRtpChannelTotalRxPackets": adGenAOSRtpChannelTotalRxPackets,
       "adGenAOSRtpChannelTotalRxOctets": adGenAOSRtpChannelTotalRxOctets,
       "adGenAOSRtpChannelTotalRxPacketsLost": adGenAOSRtpChannelTotalRxPacketsLost,
       "adGenAOSRtpChannelTotalRxPacketsUnknown": adGenAOSRtpChannelTotalRxPacketsUnknown,
       "adGenAOSRtpChannelTotalTxPackets": adGenAOSRtpChannelTotalTxPackets,
       "adGenAOSRtpChannelTotalTxOctets": adGenAOSRtpChannelTotalTxOctets,
       "adGenAOSRtpChannelTotalRxMaxDepth": adGenAOSRtpChannelTotalRxMaxDepth,
       "adGenAOSRtpChannelTotalRxFrameLateDiscards": adGenAOSRtpChannelTotalRxFrameLateDiscards,
       "adGenAOSRtpChannelTotalRxFrameOverflows": adGenAOSRtpChannelTotalRxFrameOverflows,
       "adGenAOSRtpChannelTotalRxFrameOutOfOrders": adGenAOSRtpChannelTotalRxFrameOutOfOrders,
       "adGenAOSRtpChannelClearCounters": adGenAOSRtpChannelClearCounters,
       "adGenAOSRtpChannelTimeSinceLastClearCounters": adGenAOSRtpChannelTimeSinceLastClearCounters,
       "adGenAOSMediaGatewayConformance": adGenAOSMediaGatewayConformance,
       "adGenAOSMediaGatewayCompliances": adGenAOSMediaGatewayCompliances,
       "adGenAOSMediaGatewayCompliance": adGenAOSMediaGatewayCompliance,
       "adGenAOSMediaGatewayMIBGroups": adGenAOSMediaGatewayMIBGroups,
       "adGenAOSMediaGatewayRtpSessionGroup": adGenAOSMediaGatewayRtpSessionGroup,
       "adGenAOSMediaGatewayRtpSessionTotalsGroup": adGenAOSMediaGatewayRtpSessionTotalsGroup,
       "adGenAOSMediaGatewayInfoGroup": adGenAOSMediaGatewayInfoGroup,
       "adGenAOSMediaGatewayRtpChannelTotalsGroup": adGenAOSMediaGatewayRtpChannelTotalsGroup,
       "adGenAOSMediaGatewayMIB": adGenAOSMediaGatewayMIB}
)
