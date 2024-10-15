# SNMP MIB module (BEGEMOT-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEGEMOT-WIRELESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:48 2024
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

begemotWlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210)
)
begemotWlan.setRevisions(
        ("2010-05-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WlanMgmtReasonCode(Integer32, TextualConvention):
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
        *(("akmpInvalid", 20),
          ("associationExpire", 4),
          ("associationLeave", 8),
          ("associationNotAuthenticated", 9),
          ("associationTooMany", 5),
          ("authenticationExpire", 2),
          ("authenticationLeave", 3),
          ("badMechanism", 37),
          ("cipherSuiteRejected", 24),
          ("dissassocPwrcapBad", 10),
          ("dissassocSuperchanBad", 11),
          ("dot1xAuthFailed", 23),
          ("fourWayHandshakeTimeout", 15),
          ("groupCipherInvalid", 18),
          ("groupKeyUpdateTimeout", 16),
          ("ieIn4FourWayDiffers", 17),
          ("ieInvalid", 13),
          ("insufficientBw", 33),
          ("invalidRsnIeCap", 22),
          ("leavingQbss", 36),
          ("micFailure", 14),
          ("notAssociated", 7),
          ("notAuthenticated", 6),
          ("outsideTxOp", 35),
          ("pairwiseCiherInvalid", 19),
          ("setupNeeded", 38),
          ("timeout", 39),
          ("tooManyFrames", 34),
          ("unspeciffiedQos", 32),
          ("unspecified", 1),
          ("unsupportedRsnIeVersion", 21))
    )



class WlanMgmtMeshReasonCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("closeRcvd", 5),
          ("confirmTimeout", 7),
          ("cpViolation", 4),
          ("inconsistentParams", 9),
          ("invalidGtk", 8),
          ("invalidSecurity", 10),
          ("maxPeers", 3),
          ("maxRetries", 6),
          ("peerLinkCancelled", 2),
          ("perrDestUnreach", 13),
          ("perrNoFI", 12),
          ("perrUnspecified", 11))
    )



class WlanMgmtStatusCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              40,
              41,
              42,
              43,
              44,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("akmpInvalid", 43),
          ("algorithm", 13),
          ("basicRate", 18),
          ("caRequired", 21),
          ("capabilitiesInfo", 10),
          ("challenge", 15),
          ("cipherSuiteRejected", 46),
          ("dssofdmRequired", 26),
          ("groupCipherInvalid", 41),
          ("invalidIE", 40),
          ("invalidRsnIECap", 45),
          ("missingHTCaps", 27),
          ("notAssociated", 11),
          ("other", 12),
          ("pairwiseCipherInvalid", 42),
          ("pbccRequired", 20),
          ("pwrcapRequire", 23),
          ("sequence", 14),
          ("shortSlotRequired", 25),
          ("spRequired", 19),
          ("specMgmtRequired", 22),
          ("success", 0),
          ("superchanRequired", 24),
          ("timeout", 16),
          ("tooMany", 17),
          ("unspecified", 1),
          ("unsupportedRsnIEVersion", 44))
    )



class WlanRegDomainCode(Integer32, TextualConvention):
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("apac", 9),
          ("apac2", 10),
          ("apac3", 11),
          ("ca", 2),
          ("debug", 14),
          ("etsi", 3),
          ("etsi2", 4),
          ("etsi3", 5),
          ("fcc", 1),
          ("fcc3", 6),
          ("gz901", 17),
          ("japan", 7),
          ("korea", 8),
          ("none", 13),
          ("row", 12),
          ("sr9", 15),
          ("xr9", 16))
    )



class WlanIfaceDot11nPduType(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 0),
          ("rxOnly", 1),
          ("txAndRx", 3),
          ("txOnly", 2))
    )



class WlanPeerCapabilityFlags(Bits, TextualConvention):
    status = "current"


class WlanIfPhyMode(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("dot11a", 2),
          ("dot11b", 3),
          ("dot11g", 4),
          ("dot11na", 9),
          ("dot11ng", 10),
          ("fh", 5),
          ("ofdmHalf", 11),
          ("ofdmQuarter", 12),
          ("sturboA", 8),
          ("turboA", 6),
          ("turboG", 7))
    )



# MIB Managed Objects in the order of their OIDs

_BegemotWlanNotifications_ObjectIdentity = ObjectIdentity
begemotWlanNotifications = _BegemotWlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 0)
)
_BegemotWlanInterface_ObjectIdentity = ObjectIdentity
begemotWlanInterface = _BegemotWlanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1)
)
_WlanInterfaceTable_Object = MibTable
wlanInterfaceTable = _WlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1)
)
if mibBuilder.loadTexts:
    wlanInterfaceTable.setStatus("current")
_WlanInterfaceEntry_Object = MibTableRow
wlanInterfaceEntry = _WlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1)
)
wlanInterfaceEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanInterfaceEntry.setStatus("current")
_WlanIfaceIndex_Type = InterfaceIndex
_WlanIfaceIndex_Object = MibTableColumn
wlanIfaceIndex = _WlanIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 1),
    _WlanIfaceIndex_Type()
)
wlanIfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceIndex.setStatus("current")


class _WlanIfaceName_Type(DisplayString):
    """Custom type wlanIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanIfaceName_Type.__name__ = "DisplayString"
_WlanIfaceName_Object = MibTableColumn
wlanIfaceName = _WlanIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 2),
    _WlanIfaceName_Type()
)
wlanIfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanIfaceName.setStatus("current")


class _WlanParentIfName_Type(DisplayString):
    """Custom type wlanParentIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanParentIfName_Type.__name__ = "DisplayString"
_WlanParentIfName_Object = MibTableColumn
wlanParentIfName = _WlanParentIfName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 3),
    _WlanParentIfName_Type()
)
wlanParentIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanParentIfName.setStatus("current")


class _WlanIfaceOperatingMode_Type(Integer32):
    """Custom type wlanIfaceOperatingMode based on Integer32"""
    defaultValue = 1

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("adhocDemo", 3),
          ("hostAp", 4),
          ("ibss", 0),
          ("meshPoint", 6),
          ("monitor", 5),
          ("station", 1),
          ("tdma", 7),
          ("wds", 2))
    )


_WlanIfaceOperatingMode_Type.__name__ = "Integer32"
_WlanIfaceOperatingMode_Object = MibTableColumn
wlanIfaceOperatingMode = _WlanIfaceOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 4),
    _WlanIfaceOperatingMode_Type()
)
wlanIfaceOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanIfaceOperatingMode.setStatus("current")


class _WlanIfaceFlags_Type(Bits):
    """Custom type wlanIfaceFlags based on Bits"""
    namedValues = NamedValues(
        *(("noBeacons", 2),
          ("uniqueBssid", 1),
          ("wdsLegacy", 3))
    )

_WlanIfaceFlags_Type.__name__ = "Bits"
_WlanIfaceFlags_Object = MibTableColumn
wlanIfaceFlags = _WlanIfaceFlags_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 5),
    _WlanIfaceFlags_Type()
)
wlanIfaceFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanIfaceFlags.setStatus("current")
_WlanIfaceBssid_Type = MacAddress
_WlanIfaceBssid_Object = MibTableColumn
wlanIfaceBssid = _WlanIfaceBssid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 6),
    _WlanIfaceBssid_Type()
)
wlanIfaceBssid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanIfaceBssid.setStatus("current")
_WlanIfaceLocalAddress_Type = MacAddress
_WlanIfaceLocalAddress_Object = MibTableColumn
wlanIfaceLocalAddress = _WlanIfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 7),
    _WlanIfaceLocalAddress_Type()
)
wlanIfaceLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanIfaceLocalAddress.setStatus("current")
_WlanIfaceStatus_Type = RowStatus
_WlanIfaceStatus_Object = MibTableColumn
wlanIfaceStatus = _WlanIfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 8),
    _WlanIfaceStatus_Type()
)
wlanIfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanIfaceStatus.setStatus("current")


class _WlanIfaceState_Type(Integer32):
    """Custom type wlanIfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WlanIfaceState_Type.__name__ = "Integer32"
_WlanIfaceState_Object = MibTableColumn
wlanIfaceState = _WlanIfaceState_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 1, 1, 9),
    _WlanIfaceState_Type()
)
wlanIfaceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanIfaceState.setStatus("current")
_WlanIfParentTable_Object = MibTable
wlanIfParentTable = _WlanIfParentTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 2)
)
if mibBuilder.loadTexts:
    wlanIfParentTable.setStatus("current")
_WlanIfParentEntry_Object = MibTableRow
wlanIfParentEntry = _WlanIfParentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wlanIfParentEntry.setStatus("current")


class _WlanIfParentDriverCapabilities_Type(Bits):
    """Custom type wlanIfParentDriverCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ahDemo", 8),
          ("athFastFrames", 3),
          ("athTurbo", 4),
          ("bgScan", 21),
          ("burst", 18),
          ("dfs", 14),
          ("hostAp", 7),
          ("ibss", 5),
          ("ieee8023encap", 2),
          ("mbss", 15),
          ("monitor", 13),
          ("pmgt", 6),
          ("shortPreamble", 12),
          ("shortSlot", 11),
          ("station", 1),
          ("swRetry", 9),
          ("tdma", 23),
          ("txFrag", 22),
          ("txPmgt", 10),
          ("wds", 20),
          ("wme", 19),
          ("wpa1", 16),
          ("wpa2", 17))
    )

_WlanIfParentDriverCapabilities_Type.__name__ = "Bits"
_WlanIfParentDriverCapabilities_Object = MibTableColumn
wlanIfParentDriverCapabilities = _WlanIfParentDriverCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 2, 1, 1),
    _WlanIfParentDriverCapabilities_Type()
)
wlanIfParentDriverCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfParentDriverCapabilities.setStatus("current")


class _WlanIfParentCryptoCapabilities_Type(Bits):
    """Custom type wlanIfParentCryptoCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("aes", 3),
          ("aesCcm", 4),
          ("ckip", 6),
          ("tkip", 2),
          ("tkipMic", 5),
          ("wep", 1))
    )

_WlanIfParentCryptoCapabilities_Type.__name__ = "Bits"
_WlanIfParentCryptoCapabilities_Object = MibTableColumn
wlanIfParentCryptoCapabilities = _WlanIfParentCryptoCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 2, 1, 2),
    _WlanIfParentCryptoCapabilities_Type()
)
wlanIfParentCryptoCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfParentCryptoCapabilities.setStatus("current")


class _WlanIfParentHTCapabilities_Type(Bits):
    """Custom type wlanIfParentHTCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("amsdu7935", 8),
          ("chwidth40", 2),
          ("delba", 7),
          ("dssscck40", 9),
          ("fortyMHzIntolerant", 11),
          ("greenField", 3),
          ("htcAmpdu", 13),
          ("htcAmsdu", 14),
          ("htcHt", 15),
          ("htcRifs", 17),
          ("htcSmps", 16),
          ("ldpc", 1),
          ("lsigTxOpProt", 12),
          ("psmp", 10),
          ("shortGi20", 4),
          ("shortGi40", 5),
          ("txStbc", 6))
    )

_WlanIfParentHTCapabilities_Type.__name__ = "Bits"
_WlanIfParentHTCapabilities_Object = MibTableColumn
wlanIfParentHTCapabilities = _WlanIfParentHTCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 2, 1, 3),
    _WlanIfParentHTCapabilities_Type()
)
wlanIfParentHTCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfParentHTCapabilities.setStatus("current")
_WlanIfaceConfigTable_Object = MibTable
wlanIfaceConfigTable = _WlanIfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3)
)
if mibBuilder.loadTexts:
    wlanIfaceConfigTable.setStatus("current")
_WlanIfaceConfigEntry_Object = MibTableRow
wlanIfaceConfigEntry = _WlanIfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wlanIfaceConfigEntry.setStatus("current")
_WlanIfacePacketBurst_Type = TruthValue
_WlanIfacePacketBurst_Object = MibTableColumn
wlanIfacePacketBurst = _WlanIfacePacketBurst_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 1),
    _WlanIfacePacketBurst_Type()
)
wlanIfacePacketBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfacePacketBurst.setStatus("current")


class _WlanIfaceCountryCode_Type(OctetString):
    """Custom type wlanIfaceCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_WlanIfaceCountryCode_Type.__name__ = "OctetString"
_WlanIfaceCountryCode_Object = MibTableColumn
wlanIfaceCountryCode = _WlanIfaceCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 2),
    _WlanIfaceCountryCode_Type()
)
wlanIfaceCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceCountryCode.setStatus("current")
_WlanIfaceRegDomain_Type = WlanRegDomainCode
_WlanIfaceRegDomain_Object = MibTableColumn
wlanIfaceRegDomain = _WlanIfaceRegDomain_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 3),
    _WlanIfaceRegDomain_Type()
)
wlanIfaceRegDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceRegDomain.setStatus("current")


class _WlanIfaceDesiredSsid_Type(OctetString):
    """Custom type wlanIfaceDesiredSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanIfaceDesiredSsid_Type.__name__ = "OctetString"
_WlanIfaceDesiredSsid_Object = MibTableColumn
wlanIfaceDesiredSsid = _WlanIfaceDesiredSsid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 4),
    _WlanIfaceDesiredSsid_Type()
)
wlanIfaceDesiredSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDesiredSsid.setStatus("current")
_WlanIfaceDesiredChannel_Type = Integer32
_WlanIfaceDesiredChannel_Object = MibTableColumn
wlanIfaceDesiredChannel = _WlanIfaceDesiredChannel_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 5),
    _WlanIfaceDesiredChannel_Type()
)
wlanIfaceDesiredChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDesiredChannel.setStatus("current")


class _WlanIfaceDynamicFreqSelection_Type(TruthValue):
    """Custom type wlanIfaceDynamicFreqSelection based on TruthValue"""


_WlanIfaceDynamicFreqSelection_Object = MibTableColumn
wlanIfaceDynamicFreqSelection = _WlanIfaceDynamicFreqSelection_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 6),
    _WlanIfaceDynamicFreqSelection_Type()
)
wlanIfaceDynamicFreqSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDynamicFreqSelection.setStatus("current")
_WlanIfaceFastFrames_Type = TruthValue
_WlanIfaceFastFrames_Object = MibTableColumn
wlanIfaceFastFrames = _WlanIfaceFastFrames_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 7),
    _WlanIfaceFastFrames_Type()
)
wlanIfaceFastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceFastFrames.setStatus("current")
_WlanIfaceDturbo_Type = TruthValue
_WlanIfaceDturbo_Object = MibTableColumn
wlanIfaceDturbo = _WlanIfaceDturbo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 8),
    _WlanIfaceDturbo_Type()
)
wlanIfaceDturbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDturbo.setStatus("current")
_WlanIfaceTxPower_Type = Integer32
_WlanIfaceTxPower_Object = MibTableColumn
wlanIfaceTxPower = _WlanIfaceTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 9),
    _WlanIfaceTxPower_Type()
)
wlanIfaceTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceTxPower.setStatus("current")


class _WlanIfaceFragmentThreshold_Type(Integer32):
    """Custom type wlanIfaceFragmentThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WlanIfaceFragmentThreshold_Type.__name__ = "Integer32"
_WlanIfaceFragmentThreshold_Object = MibTableColumn
wlanIfaceFragmentThreshold = _WlanIfaceFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 10),
    _WlanIfaceFragmentThreshold_Type()
)
wlanIfaceFragmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceFragmentThreshold.setStatus("current")


class _WlanIfaceRTSThreshold_Type(Integer32):
    """Custom type wlanIfaceRTSThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2346),
    )


_WlanIfaceRTSThreshold_Type.__name__ = "Integer32"
_WlanIfaceRTSThreshold_Object = MibTableColumn
wlanIfaceRTSThreshold = _WlanIfaceRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 11),
    _WlanIfaceRTSThreshold_Type()
)
wlanIfaceRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceRTSThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wlanIfaceRTSThreshold.setUnits("bytes")
_WlanIfaceWlanPrivacySubscribe_Type = TruthValue
_WlanIfaceWlanPrivacySubscribe_Object = MibTableColumn
wlanIfaceWlanPrivacySubscribe = _WlanIfaceWlanPrivacySubscribe_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 12),
    _WlanIfaceWlanPrivacySubscribe_Type()
)
wlanIfaceWlanPrivacySubscribe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceWlanPrivacySubscribe.setStatus("current")
_WlanIfaceBgScan_Type = TruthValue
_WlanIfaceBgScan_Object = MibTableColumn
wlanIfaceBgScan = _WlanIfaceBgScan_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 13),
    _WlanIfaceBgScan_Type()
)
wlanIfaceBgScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceBgScan.setStatus("current")


class _WlanIfaceBgScanIdle_Type(Integer32):
    """Custom type wlanIfaceBgScanIdle based on Integer32"""
    defaultValue = 250


_WlanIfaceBgScanIdle_Object = MibTableColumn
wlanIfaceBgScanIdle = _WlanIfaceBgScanIdle_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 14),
    _WlanIfaceBgScanIdle_Type()
)
wlanIfaceBgScanIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceBgScanIdle.setStatus("current")
if mibBuilder.loadTexts:
    wlanIfaceBgScanIdle.setUnits("milliseconds")


class _WlanIfaceBgScanInterval_Type(Integer32):
    """Custom type wlanIfaceBgScanInterval based on Integer32"""
    defaultValue = 300


_WlanIfaceBgScanInterval_Object = MibTableColumn
wlanIfaceBgScanInterval = _WlanIfaceBgScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 15),
    _WlanIfaceBgScanInterval_Type()
)
wlanIfaceBgScanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceBgScanInterval.setStatus("current")
if mibBuilder.loadTexts:
    wlanIfaceBgScanInterval.setUnits("seconds")


class _WlanIfaceBeaconMissedThreshold_Type(Integer32):
    """Custom type wlanIfaceBeaconMissedThreshold based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WlanIfaceBeaconMissedThreshold_Type.__name__ = "Integer32"
_WlanIfaceBeaconMissedThreshold_Object = MibTableColumn
wlanIfaceBeaconMissedThreshold = _WlanIfaceBeaconMissedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 16),
    _WlanIfaceBeaconMissedThreshold_Type()
)
wlanIfaceBeaconMissedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceBeaconMissedThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wlanIfaceBeaconMissedThreshold.setUnits("frames")
_WlanIfaceDesiredBssid_Type = MacAddress
_WlanIfaceDesiredBssid_Object = MibTableColumn
wlanIfaceDesiredBssid = _WlanIfaceDesiredBssid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 17),
    _WlanIfaceDesiredBssid_Type()
)
wlanIfaceDesiredBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDesiredBssid.setStatus("current")


class _WlanIfaceRoamingMode_Type(Integer32):
    """Custom type wlanIfaceRoamingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("device", 1),
          ("manual", 3))
    )


_WlanIfaceRoamingMode_Type.__name__ = "Integer32"
_WlanIfaceRoamingMode_Object = MibTableColumn
wlanIfaceRoamingMode = _WlanIfaceRoamingMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 18),
    _WlanIfaceRoamingMode_Type()
)
wlanIfaceRoamingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceRoamingMode.setStatus("current")


class _WlanIfaceDot11d_Type(TruthValue):
    """Custom type wlanIfaceDot11d based on TruthValue"""


_WlanIfaceDot11d_Object = MibTableColumn
wlanIfaceDot11d = _WlanIfaceDot11d_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 19),
    _WlanIfaceDot11d_Type()
)
wlanIfaceDot11d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11d.setStatus("current")


class _WlanIfaceDot11h_Type(TruthValue):
    """Custom type wlanIfaceDot11h based on TruthValue"""


_WlanIfaceDot11h_Object = MibTableColumn
wlanIfaceDot11h = _WlanIfaceDot11h_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 20),
    _WlanIfaceDot11h_Type()
)
wlanIfaceDot11h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11h.setStatus("current")
_WlanIfaceDynamicWds_Type = TruthValue
_WlanIfaceDynamicWds_Object = MibTableColumn
wlanIfaceDynamicWds = _WlanIfaceDynamicWds_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 21),
    _WlanIfaceDynamicWds_Type()
)
wlanIfaceDynamicWds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDynamicWds.setStatus("current")
_WlanIfacePowerSave_Type = TruthValue
_WlanIfacePowerSave_Object = MibTableColumn
wlanIfacePowerSave = _WlanIfacePowerSave_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 22),
    _WlanIfacePowerSave_Type()
)
wlanIfacePowerSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfacePowerSave.setStatus("current")


class _WlanIfaceApBridge_Type(TruthValue):
    """Custom type wlanIfaceApBridge based on TruthValue"""


_WlanIfaceApBridge_Object = MibTableColumn
wlanIfaceApBridge = _WlanIfaceApBridge_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 23),
    _WlanIfaceApBridge_Type()
)
wlanIfaceApBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceApBridge.setStatus("current")


class _WlanIfaceBeaconInterval_Type(Integer32):
    """Custom type wlanIfaceBeaconInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 1000),
    )


_WlanIfaceBeaconInterval_Type.__name__ = "Integer32"
_WlanIfaceBeaconInterval_Object = MibTableColumn
wlanIfaceBeaconInterval = _WlanIfaceBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 24),
    _WlanIfaceBeaconInterval_Type()
)
wlanIfaceBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceBeaconInterval.setStatus("current")


class _WlanIfaceDtimPeriod_Type(Integer32):
    """Custom type wlanIfaceDtimPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WlanIfaceDtimPeriod_Type.__name__ = "Integer32"
_WlanIfaceDtimPeriod_Object = MibTableColumn
wlanIfaceDtimPeriod = _WlanIfaceDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 25),
    _WlanIfaceDtimPeriod_Type()
)
wlanIfaceDtimPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDtimPeriod.setStatus("current")


class _WlanIfaceHideSsid_Type(TruthValue):
    """Custom type wlanIfaceHideSsid based on TruthValue"""


_WlanIfaceHideSsid_Object = MibTableColumn
wlanIfaceHideSsid = _WlanIfaceHideSsid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 26),
    _WlanIfaceHideSsid_Type()
)
wlanIfaceHideSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceHideSsid.setStatus("current")


class _WlanIfaceInactivityProccess_Type(TruthValue):
    """Custom type wlanIfaceInactivityProccess based on TruthValue"""


_WlanIfaceInactivityProccess_Object = MibTableColumn
wlanIfaceInactivityProccess = _WlanIfaceInactivityProccess_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 27),
    _WlanIfaceInactivityProccess_Type()
)
wlanIfaceInactivityProccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceInactivityProccess.setStatus("current")


class _WlanIfaceDot11gProtMode_Type(Integer32):
    """Custom type wlanIfaceDot11gProtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cts", 2),
          ("off", 1),
          ("rtscts", 3))
    )


_WlanIfaceDot11gProtMode_Type.__name__ = "Integer32"
_WlanIfaceDot11gProtMode_Object = MibTableColumn
wlanIfaceDot11gProtMode = _WlanIfaceDot11gProtMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 28),
    _WlanIfaceDot11gProtMode_Type()
)
wlanIfaceDot11gProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11gProtMode.setStatus("current")
_WlanIfaceDot11gPureMode_Type = TruthValue
_WlanIfaceDot11gPureMode_Object = MibTableColumn
wlanIfaceDot11gPureMode = _WlanIfaceDot11gPureMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 29),
    _WlanIfaceDot11gPureMode_Type()
)
wlanIfaceDot11gPureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11gPureMode.setStatus("current")
_WlanIfaceDot11nPureMode_Type = TruthValue
_WlanIfaceDot11nPureMode_Object = MibTableColumn
wlanIfaceDot11nPureMode = _WlanIfaceDot11nPureMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 30),
    _WlanIfaceDot11nPureMode_Type()
)
wlanIfaceDot11nPureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nPureMode.setStatus("current")


class _WlanIfaceDot11nAmpdu_Type(WlanIfaceDot11nPduType):
    """Custom type wlanIfaceDot11nAmpdu based on WlanIfaceDot11nPduType"""


_WlanIfaceDot11nAmpdu_Object = MibTableColumn
wlanIfaceDot11nAmpdu = _WlanIfaceDot11nAmpdu_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 31),
    _WlanIfaceDot11nAmpdu_Type()
)
wlanIfaceDot11nAmpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nAmpdu.setStatus("current")


class _WlanIfaceDot11nAmpduDensity_Type(Integer32):
    """Custom type wlanIfaceDot11nAmpduDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(400, 400),
        ValueRangeConstraint(800, 800),
        ValueRangeConstraint(1600, 1600),
    )


_WlanIfaceDot11nAmpduDensity_Type.__name__ = "Integer32"
_WlanIfaceDot11nAmpduDensity_Object = MibTableColumn
wlanIfaceDot11nAmpduDensity = _WlanIfaceDot11nAmpduDensity_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 32),
    _WlanIfaceDot11nAmpduDensity_Type()
)
wlanIfaceDot11nAmpduDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nAmpduDensity.setStatus("current")
if mibBuilder.loadTexts:
    wlanIfaceDot11nAmpduDensity.setUnits("1/100ths-of-microsecond")


class _WlanIfaceDot11nAmpduLimit_Type(Integer32):
    """Custom type wlanIfaceDot11nAmpduLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 8192),
        ValueRangeConstraint(16384, 16384),
        ValueRangeConstraint(32768, 32768),
        ValueRangeConstraint(65536, 65536),
    )


_WlanIfaceDot11nAmpduLimit_Type.__name__ = "Integer32"
_WlanIfaceDot11nAmpduLimit_Object = MibTableColumn
wlanIfaceDot11nAmpduLimit = _WlanIfaceDot11nAmpduLimit_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 33),
    _WlanIfaceDot11nAmpduLimit_Type()
)
wlanIfaceDot11nAmpduLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nAmpduLimit.setStatus("current")


class _WlanIfaceDot11nAmsdu_Type(WlanIfaceDot11nPduType):
    """Custom type wlanIfaceDot11nAmsdu based on WlanIfaceDot11nPduType"""


_WlanIfaceDot11nAmsdu_Object = MibTableColumn
wlanIfaceDot11nAmsdu = _WlanIfaceDot11nAmsdu_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 34),
    _WlanIfaceDot11nAmsdu_Type()
)
wlanIfaceDot11nAmsdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nAmsdu.setStatus("current")


class _WlanIfaceDot11nAmsduLimit_Type(Integer32):
    """Custom type wlanIfaceDot11nAmsduLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3839, 3839),
        ValueRangeConstraint(7935, 7935),
    )


_WlanIfaceDot11nAmsduLimit_Type.__name__ = "Integer32"
_WlanIfaceDot11nAmsduLimit_Object = MibTableColumn
wlanIfaceDot11nAmsduLimit = _WlanIfaceDot11nAmsduLimit_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 35),
    _WlanIfaceDot11nAmsduLimit_Type()
)
wlanIfaceDot11nAmsduLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nAmsduLimit.setStatus("current")


class _WlanIfaceDot11nHighThroughput_Type(TruthValue):
    """Custom type wlanIfaceDot11nHighThroughput based on TruthValue"""


_WlanIfaceDot11nHighThroughput_Object = MibTableColumn
wlanIfaceDot11nHighThroughput = _WlanIfaceDot11nHighThroughput_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 36),
    _WlanIfaceDot11nHighThroughput_Type()
)
wlanIfaceDot11nHighThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nHighThroughput.setStatus("current")


class _WlanIfaceDot11nHTCompatible_Type(TruthValue):
    """Custom type wlanIfaceDot11nHTCompatible based on TruthValue"""


_WlanIfaceDot11nHTCompatible_Object = MibTableColumn
wlanIfaceDot11nHTCompatible = _WlanIfaceDot11nHTCompatible_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 37),
    _WlanIfaceDot11nHTCompatible_Type()
)
wlanIfaceDot11nHTCompatible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nHTCompatible.setStatus("current")


class _WlanIfaceDot11nHTProtMode_Type(Integer32):
    """Custom type wlanIfaceDot11nHTProtMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("rts", 2))
    )


_WlanIfaceDot11nHTProtMode_Type.__name__ = "Integer32"
_WlanIfaceDot11nHTProtMode_Object = MibTableColumn
wlanIfaceDot11nHTProtMode = _WlanIfaceDot11nHTProtMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 38),
    _WlanIfaceDot11nHTProtMode_Type()
)
wlanIfaceDot11nHTProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nHTProtMode.setStatus("current")
_WlanIfaceDot11nRIFS_Type = TruthValue
_WlanIfaceDot11nRIFS_Object = MibTableColumn
wlanIfaceDot11nRIFS = _WlanIfaceDot11nRIFS_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 39),
    _WlanIfaceDot11nRIFS_Type()
)
wlanIfaceDot11nRIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nRIFS.setStatus("current")
_WlanIfaceDot11nShortGI_Type = TruthValue
_WlanIfaceDot11nShortGI_Object = MibTableColumn
wlanIfaceDot11nShortGI = _WlanIfaceDot11nShortGI_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 40),
    _WlanIfaceDot11nShortGI_Type()
)
wlanIfaceDot11nShortGI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nShortGI.setStatus("current")


class _WlanIfaceDot11nSMPSMode_Type(Integer32):
    """Custom type wlanIfaceDot11nSMPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("dynamic", 3),
          ("static", 2))
    )


_WlanIfaceDot11nSMPSMode_Type.__name__ = "Integer32"
_WlanIfaceDot11nSMPSMode_Object = MibTableColumn
wlanIfaceDot11nSMPSMode = _WlanIfaceDot11nSMPSMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 41),
    _WlanIfaceDot11nSMPSMode_Type()
)
wlanIfaceDot11nSMPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceDot11nSMPSMode.setStatus("current")


class _WlanIfaceTdmaSlot_Type(Integer32):
    """Custom type wlanIfaceTdmaSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WlanIfaceTdmaSlot_Type.__name__ = "Integer32"
_WlanIfaceTdmaSlot_Object = MibTableColumn
wlanIfaceTdmaSlot = _WlanIfaceTdmaSlot_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 42),
    _WlanIfaceTdmaSlot_Type()
)
wlanIfaceTdmaSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceTdmaSlot.setStatus("current")


class _WlanIfaceTdmaSlotCount_Type(Integer32):
    """Custom type wlanIfaceTdmaSlotCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WlanIfaceTdmaSlotCount_Type.__name__ = "Integer32"
_WlanIfaceTdmaSlotCount_Object = MibTableColumn
wlanIfaceTdmaSlotCount = _WlanIfaceTdmaSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 43),
    _WlanIfaceTdmaSlotCount_Type()
)
wlanIfaceTdmaSlotCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceTdmaSlotCount.setStatus("current")


class _WlanIfaceTdmaSlotLength_Type(Integer32):
    """Custom type wlanIfaceTdmaSlotLength based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 65000),
    )


_WlanIfaceTdmaSlotLength_Type.__name__ = "Integer32"
_WlanIfaceTdmaSlotLength_Object = MibTableColumn
wlanIfaceTdmaSlotLength = _WlanIfaceTdmaSlotLength_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 44),
    _WlanIfaceTdmaSlotLength_Type()
)
wlanIfaceTdmaSlotLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceTdmaSlotLength.setStatus("current")
if mibBuilder.loadTexts:
    wlanIfaceTdmaSlotLength.setUnits("microseconds")


class _WlanIfaceTdmaBeaconInterval_Type(Integer32):
    """Custom type wlanIfaceTdmaBeaconInterval based on Integer32"""
    defaultValue = 5


_WlanIfaceTdmaBeaconInterval_Object = MibTableColumn
wlanIfaceTdmaBeaconInterval = _WlanIfaceTdmaBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 3, 1, 45),
    _WlanIfaceTdmaBeaconInterval_Type()
)
wlanIfaceTdmaBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfaceTdmaBeaconInterval.setStatus("current")
_WlanIfacePeerTable_Object = MibTable
wlanIfacePeerTable = _WlanIfacePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4)
)
if mibBuilder.loadTexts:
    wlanIfacePeerTable.setStatus("current")
_WlanIfacePeerEntry_Object = MibTableRow
wlanIfacePeerEntry = _WlanIfacePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1)
)
wlanIfacePeerEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfacePeerAddress"),
)
if mibBuilder.loadTexts:
    wlanIfacePeerEntry.setStatus("current")
_WlanIfacePeerAddress_Type = MacAddress
_WlanIfacePeerAddress_Object = MibTableColumn
wlanIfacePeerAddress = _WlanIfacePeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 1),
    _WlanIfacePeerAddress_Type()
)
wlanIfacePeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerAddress.setStatus("current")
_WlanIfacePeerAssociationId_Type = Integer32
_WlanIfacePeerAssociationId_Object = MibTableColumn
wlanIfacePeerAssociationId = _WlanIfacePeerAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 2),
    _WlanIfacePeerAssociationId_Type()
)
wlanIfacePeerAssociationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerAssociationId.setStatus("current")


class _WlanIfacePeerVlanTag_Type(Integer32):
    """Custom type wlanIfacePeerVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_WlanIfacePeerVlanTag_Type.__name__ = "Integer32"
_WlanIfacePeerVlanTag_Object = MibTableColumn
wlanIfacePeerVlanTag = _WlanIfacePeerVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 3),
    _WlanIfacePeerVlanTag_Type()
)
wlanIfacePeerVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfacePeerVlanTag.setStatus("current")
_WlanIfacePeerFrequency_Type = Integer32
_WlanIfacePeerFrequency_Object = MibTableColumn
wlanIfacePeerFrequency = _WlanIfacePeerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 4),
    _WlanIfacePeerFrequency_Type()
)
wlanIfacePeerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerFrequency.setStatus("current")
_WlanIfacePeerCurrentTXRate_Type = Integer32
_WlanIfacePeerCurrentTXRate_Object = MibTableColumn
wlanIfacePeerCurrentTXRate = _WlanIfacePeerCurrentTXRate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 5),
    _WlanIfacePeerCurrentTXRate_Type()
)
wlanIfacePeerCurrentTXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerCurrentTXRate.setStatus("current")
_WlanIfacePeerRxSignalStrength_Type = Integer32
_WlanIfacePeerRxSignalStrength_Object = MibTableColumn
wlanIfacePeerRxSignalStrength = _WlanIfacePeerRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 6),
    _WlanIfacePeerRxSignalStrength_Type()
)
wlanIfacePeerRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerRxSignalStrength.setStatus("current")
_WlanIfacePeerIdleTimer_Type = Integer32
_WlanIfacePeerIdleTimer_Object = MibTableColumn
wlanIfacePeerIdleTimer = _WlanIfacePeerIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 7),
    _WlanIfacePeerIdleTimer_Type()
)
wlanIfacePeerIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    wlanIfacePeerIdleTimer.setUnits("seconds")
_WlanIfacePeerTxSequenceNo_Type = Integer32
_WlanIfacePeerTxSequenceNo_Object = MibTableColumn
wlanIfacePeerTxSequenceNo = _WlanIfacePeerTxSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 8),
    _WlanIfacePeerTxSequenceNo_Type()
)
wlanIfacePeerTxSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerTxSequenceNo.setStatus("current")
_WlanIfacePeerRxSequenceNo_Type = Integer32
_WlanIfacePeerRxSequenceNo_Object = MibTableColumn
wlanIfacePeerRxSequenceNo = _WlanIfacePeerRxSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 9),
    _WlanIfacePeerRxSequenceNo_Type()
)
wlanIfacePeerRxSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerRxSequenceNo.setStatus("current")
_WlanIfacePeerTxPower_Type = Integer32
_WlanIfacePeerTxPower_Object = MibTableColumn
wlanIfacePeerTxPower = _WlanIfacePeerTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 10),
    _WlanIfacePeerTxPower_Type()
)
wlanIfacePeerTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerTxPower.setStatus("current")
_WlanIfacePeerCapabilities_Type = WlanPeerCapabilityFlags
_WlanIfacePeerCapabilities_Object = MibTableColumn
wlanIfacePeerCapabilities = _WlanIfacePeerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 11),
    _WlanIfacePeerCapabilities_Type()
)
wlanIfacePeerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerCapabilities.setStatus("current")


class _WlanIfacePeerFlags_Type(Bits):
    """Custom type wlanIfacePeerFlags based on Bits"""
    namedValues = NamedValues(
        *(("ampduRx", 10),
          ("ampduTx", 11),
          ("amsduRx", 17),
          ("amsduTx", 18),
          ("authRefHeld", 5),
          ("authorizedForData", 1),
          ("erpEnabled", 3),
          ("htCompat", 7),
          ("htEnabled", 6),
          ("mimoPowerSave", 12),
          ("powerSaveMode", 4),
          ("qosEnabled", 2),
          ("rifs", 14),
          ("sendRts", 13),
          ("shortGiHT20", 15),
          ("shortGiHT40", 16),
          ("tsnAssoc", 9),
          ("wpsAssoc", 8))
    )

_WlanIfacePeerFlags_Type.__name__ = "Bits"
_WlanIfacePeerFlags_Object = MibTableColumn
wlanIfacePeerFlags = _WlanIfacePeerFlags_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 4, 1, 12),
    _WlanIfacePeerFlags_Type()
)
wlanIfacePeerFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfacePeerFlags.setStatus("current")
_WlanIfaceChannelTable_Object = MibTable
wlanIfaceChannelTable = _WlanIfaceChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5)
)
if mibBuilder.loadTexts:
    wlanIfaceChannelTable.setStatus("current")
_WlanIfaceChannelEntry_Object = MibTableRow
wlanIfaceChannelEntry = _WlanIfaceChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1)
)
wlanIfaceChannelEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceChannelId"),
)
if mibBuilder.loadTexts:
    wlanIfaceChannelEntry.setStatus("current")


class _WlanIfaceChannelId_Type(Integer32):
    """Custom type wlanIfaceChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1536),
    )


_WlanIfaceChannelId_Type.__name__ = "Integer32"
_WlanIfaceChannelId_Object = MibTableColumn
wlanIfaceChannelId = _WlanIfaceChannelId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 1),
    _WlanIfaceChannelId_Type()
)
wlanIfaceChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanIfaceChannelId.setStatus("current")


class _WlanIfaceChannelIeeeId_Type(Integer32):
    """Custom type wlanIfaceChannelIeeeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WlanIfaceChannelIeeeId_Type.__name__ = "Integer32"
_WlanIfaceChannelIeeeId_Object = MibTableColumn
wlanIfaceChannelIeeeId = _WlanIfaceChannelIeeeId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 2),
    _WlanIfaceChannelIeeeId_Type()
)
wlanIfaceChannelIeeeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelIeeeId.setStatus("current")


class _WlanIfaceChannelType_Type(Integer32):
    """Custom type wlanIfaceChannelType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11b", 3),
          ("dot11g", 4),
          ("fhss", 1),
          ("fiveMHz", 6),
          ("ht", 8),
          ("tenMHz", 5),
          ("turbo", 7))
    )


_WlanIfaceChannelType_Type.__name__ = "Integer32"
_WlanIfaceChannelType_Object = MibTableColumn
wlanIfaceChannelType = _WlanIfaceChannelType_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 3),
    _WlanIfaceChannelType_Type()
)
wlanIfaceChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelType.setStatus("current")


class _WlanIfaceChannelFlags_Type(Bits):
    """Custom type wlanIfaceChannelFlags based on Bits"""
    namedValues = NamedValues(
        *(("cck", 2),
          ("dfs", 16),
          ("dot11aStaticTurbo", 10),
          ("dot11d", 20),
          ("dynamicCckOfdm", 7),
          ("gfsk", 8),
          ("halfRate", 11),
          ("ht20", 13),
          ("ht40d", 15),
          ("ht40u", 14),
          ("noAdhoc", 18),
          ("noHostAp", 19),
          ("ofdm", 3),
          ("passiveScan", 6),
          ("quarterRate", 12),
          ("spectrum2Ghz", 4),
          ("spectrum5Ghz", 5),
          ("spectrum900Mhz", 9),
          ("turbo", 1),
          ("xmit4ms", 17))
    )

_WlanIfaceChannelFlags_Type.__name__ = "Bits"
_WlanIfaceChannelFlags_Object = MibTableColumn
wlanIfaceChannelFlags = _WlanIfaceChannelFlags_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 4),
    _WlanIfaceChannelFlags_Type()
)
wlanIfaceChannelFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelFlags.setStatus("current")
_WlanIfaceChannelFrequency_Type = Integer32
_WlanIfaceChannelFrequency_Object = MibTableColumn
wlanIfaceChannelFrequency = _WlanIfaceChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 5),
    _WlanIfaceChannelFrequency_Type()
)
wlanIfaceChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelFrequency.setStatus("current")
_WlanIfaceChannelMaxRegPower_Type = Integer32
_WlanIfaceChannelMaxRegPower_Object = MibTableColumn
wlanIfaceChannelMaxRegPower = _WlanIfaceChannelMaxRegPower_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 6),
    _WlanIfaceChannelMaxRegPower_Type()
)
wlanIfaceChannelMaxRegPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelMaxRegPower.setStatus("current")
_WlanIfaceChannelMaxTxPower_Type = Integer32
_WlanIfaceChannelMaxTxPower_Object = MibTableColumn
wlanIfaceChannelMaxTxPower = _WlanIfaceChannelMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 7),
    _WlanIfaceChannelMaxTxPower_Type()
)
wlanIfaceChannelMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelMaxTxPower.setStatus("current")
_WlanIfaceChannelMinTxPower_Type = Integer32
_WlanIfaceChannelMinTxPower_Object = MibTableColumn
wlanIfaceChannelMinTxPower = _WlanIfaceChannelMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 8),
    _WlanIfaceChannelMinTxPower_Type()
)
wlanIfaceChannelMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelMinTxPower.setStatus("current")


class _WlanIfaceChannelState_Type(Bits):
    """Custom type wlanIfaceChannelState based on Bits"""
    namedValues = NamedValues(
        *(("cacDone", 2),
          ("interferenceDetected", 3),
          ("radar", 1),
          ("radarClear", 4))
    )

_WlanIfaceChannelState_Type.__name__ = "Bits"
_WlanIfaceChannelState_Object = MibTableColumn
wlanIfaceChannelState = _WlanIfaceChannelState_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 9),
    _WlanIfaceChannelState_Type()
)
wlanIfaceChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelState.setStatus("current")
_WlanIfaceChannelHTExtension_Type = Integer32
_WlanIfaceChannelHTExtension_Object = MibTableColumn
wlanIfaceChannelHTExtension = _WlanIfaceChannelHTExtension_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 10),
    _WlanIfaceChannelHTExtension_Type()
)
wlanIfaceChannelHTExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelHTExtension.setStatus("current")
_WlanIfaceChannelMaxAntennaGain_Type = Integer32
_WlanIfaceChannelMaxAntennaGain_Object = MibTableColumn
wlanIfaceChannelMaxAntennaGain = _WlanIfaceChannelMaxAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 5, 1, 11),
    _WlanIfaceChannelMaxAntennaGain_Type()
)
wlanIfaceChannelMaxAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfaceChannelMaxAntennaGain.setStatus("current")
_WlanIfRoamParamsTable_Object = MibTable
wlanIfRoamParamsTable = _WlanIfRoamParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 6)
)
if mibBuilder.loadTexts:
    wlanIfRoamParamsTable.setStatus("current")
_WlanIfRoamParamsEntry_Object = MibTableRow
wlanIfRoamParamsEntry = _WlanIfRoamParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 6, 1)
)
wlanIfRoamParamsEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfRoamPhyMode"),
)
if mibBuilder.loadTexts:
    wlanIfRoamParamsEntry.setStatus("current")
_WlanIfRoamPhyMode_Type = WlanIfPhyMode
_WlanIfRoamPhyMode_Object = MibTableColumn
wlanIfRoamPhyMode = _WlanIfRoamPhyMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 6, 1, 1),
    _WlanIfRoamPhyMode_Type()
)
wlanIfRoamPhyMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanIfRoamPhyMode.setStatus("current")
_WlanIfRoamRxSignalStrength_Type = Integer32
_WlanIfRoamRxSignalStrength_Object = MibTableColumn
wlanIfRoamRxSignalStrength = _WlanIfRoamRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 6, 1, 2),
    _WlanIfRoamRxSignalStrength_Type()
)
wlanIfRoamRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfRoamRxSignalStrength.setStatus("current")
_WlanIfRoamTxRateThreshold_Type = Integer32
_WlanIfRoamTxRateThreshold_Object = MibTableColumn
wlanIfRoamTxRateThreshold = _WlanIfRoamTxRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 6, 1, 3),
    _WlanIfRoamTxRateThreshold_Type()
)
wlanIfRoamTxRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIfRoamTxRateThreshold.setStatus("current")
_WlanIfTxParamsTable_Object = MibTable
wlanIfTxParamsTable = _WlanIfTxParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 7)
)
if mibBuilder.loadTexts:
    wlanIfTxParamsTable.setStatus("current")
_WlanIfTxParamsEntry_Object = MibTableRow
wlanIfTxParamsEntry = _WlanIfTxParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 7, 1)
)
wlanIfTxParamsEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfTxPhyMode"),
)
if mibBuilder.loadTexts:
    wlanIfTxParamsEntry.setStatus("current")
_WlanIfTxPhyMode_Type = WlanIfPhyMode
_WlanIfTxPhyMode_Object = MibTableColumn
wlanIfTxPhyMode = _WlanIfTxPhyMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 7, 1, 1),
    _WlanIfTxPhyMode_Type()
)
wlanIfTxPhyMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanIfTxPhyMode.setStatus("current")
_WlanIfTxUnicastRate_Type = Integer32
_WlanIfTxUnicastRate_Object = MibTableColumn
wlanIfTxUnicastRate = _WlanIfTxUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 7, 1, 2),
    _WlanIfTxUnicastRate_Type()
)
wlanIfTxUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfTxUnicastRate.setStatus("current")
_WlanIfTxMcastRate_Type = Integer32
_WlanIfTxMcastRate_Object = MibTableColumn
wlanIfTxMcastRate = _WlanIfTxMcastRate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 7, 1, 3),
    _WlanIfTxMcastRate_Type()
)
wlanIfTxMcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfTxMcastRate.setStatus("current")
_WlanIfTxMgmtRate_Type = Integer32
_WlanIfTxMgmtRate_Object = MibTableColumn
wlanIfTxMgmtRate = _WlanIfTxMgmtRate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 7, 1, 4),
    _WlanIfTxMgmtRate_Type()
)
wlanIfTxMgmtRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfTxMgmtRate.setStatus("current")
_WlanIfTxMaxRetryCount_Type = Integer32
_WlanIfTxMaxRetryCount_Object = MibTableColumn
wlanIfTxMaxRetryCount = _WlanIfTxMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 1, 7, 1, 5),
    _WlanIfTxMaxRetryCount_Type()
)
wlanIfTxMaxRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIfTxMaxRetryCount.setStatus("current")
_BegemotWlanScanning_ObjectIdentity = ObjectIdentity
begemotWlanScanning = _BegemotWlanScanning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2)
)
_WlanScanConfigTable_Object = MibTable
wlanScanConfigTable = _WlanScanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 1)
)
if mibBuilder.loadTexts:
    wlanScanConfigTable.setStatus("current")
_WlanScanConfigEntry_Object = MibTableRow
wlanScanConfigEntry = _WlanScanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 1, 1)
)
wlanScanConfigEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanScanConfigEntry.setStatus("current")


class _WlanScanFlags_Type(Bits):
    """Custom type wlanScanFlags based on Bits"""
    namedValues = NamedValues(
        *(("activeScan", 2),
          ("backgroundScan", 4),
          ("chechCashe", 9),
          ("flushCashe", 8),
          ("noAutoSequencing", 7),
          ("noBroadcast", 6),
          ("noSelection", 1),
          ("once", 5),
          ("pickFirst", 3))
    )

_WlanScanFlags_Type.__name__ = "Bits"
_WlanScanFlags_Object = MibTableColumn
wlanScanFlags = _WlanScanFlags_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 1, 1, 1),
    _WlanScanFlags_Type()
)
wlanScanFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanScanFlags.setStatus("current")


class _WlanScanDuration_Type(Integer32):
    """Custom type wlanScanDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WlanScanDuration_Type.__name__ = "Integer32"
_WlanScanDuration_Object = MibTableColumn
wlanScanDuration = _WlanScanDuration_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 1, 1, 2),
    _WlanScanDuration_Type()
)
wlanScanDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanScanDuration.setStatus("current")
if mibBuilder.loadTexts:
    wlanScanDuration.setUnits("milliseconds")
_WlanScanMinChannelDwellTime_Type = Integer32
_WlanScanMinChannelDwellTime_Object = MibTableColumn
wlanScanMinChannelDwellTime = _WlanScanMinChannelDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 1, 1, 3),
    _WlanScanMinChannelDwellTime_Type()
)
wlanScanMinChannelDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanScanMinChannelDwellTime.setStatus("current")
if mibBuilder.loadTexts:
    wlanScanMinChannelDwellTime.setUnits("milliseconds")
_WlanScanMaxChannelDwellTime_Type = Integer32
_WlanScanMaxChannelDwellTime_Object = MibTableColumn
wlanScanMaxChannelDwellTime = _WlanScanMaxChannelDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 1, 1, 4),
    _WlanScanMaxChannelDwellTime_Type()
)
wlanScanMaxChannelDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanScanMaxChannelDwellTime.setStatus("current")
if mibBuilder.loadTexts:
    wlanScanMaxChannelDwellTime.setUnits("milliseconds")


class _WlanScanConfigStatus_Type(Integer32):
    """Custom type wlanScanConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 4),
          ("finished", 3),
          ("notStarted", 1),
          ("running", 2),
          ("unknown", 0))
    )


_WlanScanConfigStatus_Type.__name__ = "Integer32"
_WlanScanConfigStatus_Object = MibTableColumn
wlanScanConfigStatus = _WlanScanConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 1, 1, 5),
    _WlanScanConfigStatus_Type()
)
wlanScanConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanScanConfigStatus.setStatus("current")
_WlanScanResultsTable_Object = MibTable
wlanScanResultsTable = _WlanScanResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2)
)
if mibBuilder.loadTexts:
    wlanScanResultsTable.setStatus("current")
_WlanScanResultsEntry_Object = MibTableRow
wlanScanResultsEntry = _WlanScanResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1)
)
wlanScanResultsEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanScanResultID"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanScanResultBssid"),
)
if mibBuilder.loadTexts:
    wlanScanResultsEntry.setStatus("current")


class _WlanScanResultID_Type(OctetString):
    """Custom type wlanScanResultID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanScanResultID_Type.__name__ = "OctetString"
_WlanScanResultID_Object = MibTableColumn
wlanScanResultID = _WlanScanResultID_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1, 1),
    _WlanScanResultID_Type()
)
wlanScanResultID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanScanResultID.setStatus("current")
_WlanScanResultBssid_Type = MacAddress
_WlanScanResultBssid_Object = MibTableColumn
wlanScanResultBssid = _WlanScanResultBssid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1, 2),
    _WlanScanResultBssid_Type()
)
wlanScanResultBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanScanResultBssid.setStatus("current")
_WlanScanResultChannel_Type = Integer32
_WlanScanResultChannel_Object = MibTableColumn
wlanScanResultChannel = _WlanScanResultChannel_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1, 3),
    _WlanScanResultChannel_Type()
)
wlanScanResultChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanScanResultChannel.setStatus("current")
_WlanScanResultRate_Type = Integer32
_WlanScanResultRate_Object = MibTableColumn
wlanScanResultRate = _WlanScanResultRate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1, 4),
    _WlanScanResultRate_Type()
)
wlanScanResultRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanScanResultRate.setStatus("current")
_WlanScanResultNoise_Type = Integer32
_WlanScanResultNoise_Object = MibTableColumn
wlanScanResultNoise = _WlanScanResultNoise_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1, 5),
    _WlanScanResultNoise_Type()
)
wlanScanResultNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanScanResultNoise.setStatus("current")
_WlanScanResultBeaconInterval_Type = Integer32
_WlanScanResultBeaconInterval_Object = MibTableColumn
wlanScanResultBeaconInterval = _WlanScanResultBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1, 6),
    _WlanScanResultBeaconInterval_Type()
)
wlanScanResultBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanScanResultBeaconInterval.setStatus("current")
_WlanScanResultCapabilities_Type = WlanPeerCapabilityFlags
_WlanScanResultCapabilities_Object = MibTableColumn
wlanScanResultCapabilities = _WlanScanResultCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 2, 2, 1, 7),
    _WlanScanResultCapabilities_Type()
)
wlanScanResultCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanScanResultCapabilities.setStatus("current")
_BegemotWlanStatistics_ObjectIdentity = ObjectIdentity
begemotWlanStatistics = _BegemotWlanStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3)
)
_WlanIfaceStatisticsTable_Object = MibTable
wlanIfaceStatisticsTable = _WlanIfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1)
)
if mibBuilder.loadTexts:
    wlanIfaceStatisticsTable.setStatus("current")
_WlanIfaceStatisticsEntry_Object = MibTableRow
wlanIfaceStatisticsEntry = _WlanIfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wlanIfaceStatisticsEntry.setStatus("current")
_WlanStatsRxBadVersion_Type = Counter32
_WlanStatsRxBadVersion_Object = MibTableColumn
wlanStatsRxBadVersion = _WlanStatsRxBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 1),
    _WlanStatsRxBadVersion_Type()
)
wlanStatsRxBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxBadVersion.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxBadVersion.setUnits("frames")
_WlanStatsRxTooShort_Type = Counter32
_WlanStatsRxTooShort_Object = MibTableColumn
wlanStatsRxTooShort = _WlanStatsRxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 2),
    _WlanStatsRxTooShort_Type()
)
wlanStatsRxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxTooShort.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxTooShort.setUnits("frames")
_WlanStatsRxWrongBssid_Type = Counter32
_WlanStatsRxWrongBssid_Object = MibTableColumn
wlanStatsRxWrongBssid = _WlanStatsRxWrongBssid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 3),
    _WlanStatsRxWrongBssid_Type()
)
wlanStatsRxWrongBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxWrongBssid.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxWrongBssid.setUnits("frames")
_WlanStatsRxDiscardedDups_Type = Counter32
_WlanStatsRxDiscardedDups_Object = MibTableColumn
wlanStatsRxDiscardedDups = _WlanStatsRxDiscardedDups_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 4),
    _WlanStatsRxDiscardedDups_Type()
)
wlanStatsRxDiscardedDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardedDups.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardedDups.setUnits("frames")
_WlanStatsRxWrongDir_Type = Counter32
_WlanStatsRxWrongDir_Object = MibTableColumn
wlanStatsRxWrongDir = _WlanStatsRxWrongDir_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 5),
    _WlanStatsRxWrongDir_Type()
)
wlanStatsRxWrongDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxWrongDir.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxWrongDir.setUnits("frames")
_WlanStatsRxDiscardMcastEcho_Type = Counter32
_WlanStatsRxDiscardMcastEcho_Object = MibTableColumn
wlanStatsRxDiscardMcastEcho = _WlanStatsRxDiscardMcastEcho_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 6),
    _WlanStatsRxDiscardMcastEcho_Type()
)
wlanStatsRxDiscardMcastEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardMcastEcho.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardMcastEcho.setUnits("frames")
_WlanStatsRxDiscardNoAssoc_Type = Counter32
_WlanStatsRxDiscardNoAssoc_Object = MibTableColumn
wlanStatsRxDiscardNoAssoc = _WlanStatsRxDiscardNoAssoc_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 7),
    _WlanStatsRxDiscardNoAssoc_Type()
)
wlanStatsRxDiscardNoAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardNoAssoc.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardNoAssoc.setUnits("frames")
_WlanStatsRxWepNoPrivacy_Type = Counter32
_WlanStatsRxWepNoPrivacy_Object = MibTableColumn
wlanStatsRxWepNoPrivacy = _WlanStatsRxWepNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 8),
    _WlanStatsRxWepNoPrivacy_Type()
)
wlanStatsRxWepNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxWepNoPrivacy.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxWepNoPrivacy.setUnits("frames")
_WlanStatsRxWepUnencrypted_Type = Counter32
_WlanStatsRxWepUnencrypted_Object = MibTableColumn
wlanStatsRxWepUnencrypted = _WlanStatsRxWepUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 9),
    _WlanStatsRxWepUnencrypted_Type()
)
wlanStatsRxWepUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxWepUnencrypted.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxWepUnencrypted.setUnits("frames")
_WlanStatsRxWepFailed_Type = Counter32
_WlanStatsRxWepFailed_Object = MibTableColumn
wlanStatsRxWepFailed = _WlanStatsRxWepFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 10),
    _WlanStatsRxWepFailed_Type()
)
wlanStatsRxWepFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxWepFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxWepFailed.setUnits("frames")
_WlanStatsRxDecapsulationFailed_Type = Counter32
_WlanStatsRxDecapsulationFailed_Object = MibTableColumn
wlanStatsRxDecapsulationFailed = _WlanStatsRxDecapsulationFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 11),
    _WlanStatsRxDecapsulationFailed_Type()
)
wlanStatsRxDecapsulationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDecapsulationFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDecapsulationFailed.setUnits("frames")
_WlanStatsRxDiscardMgmt_Type = Counter32
_WlanStatsRxDiscardMgmt_Object = MibTableColumn
wlanStatsRxDiscardMgmt = _WlanStatsRxDiscardMgmt_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 12),
    _WlanStatsRxDiscardMgmt_Type()
)
wlanStatsRxDiscardMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardMgmt.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardMgmt.setUnits("frames")
_WlanStatsRxControl_Type = Counter32
_WlanStatsRxControl_Object = MibTableColumn
wlanStatsRxControl = _WlanStatsRxControl_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 13),
    _WlanStatsRxControl_Type()
)
wlanStatsRxControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxControl.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxControl.setUnits("frames")
_WlanStatsRxBeacon_Type = Counter32
_WlanStatsRxBeacon_Object = MibTableColumn
wlanStatsRxBeacon = _WlanStatsRxBeacon_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 14),
    _WlanStatsRxBeacon_Type()
)
wlanStatsRxBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxBeacon.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxBeacon.setUnits("frames")
_WlanStatsRxRateSetTooBig_Type = Counter32
_WlanStatsRxRateSetTooBig_Object = MibTableColumn
wlanStatsRxRateSetTooBig = _WlanStatsRxRateSetTooBig_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 15),
    _WlanStatsRxRateSetTooBig_Type()
)
wlanStatsRxRateSetTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxRateSetTooBig.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxRateSetTooBig.setUnits("frames")
_WlanStatsRxElemMissing_Type = Counter32
_WlanStatsRxElemMissing_Object = MibTableColumn
wlanStatsRxElemMissing = _WlanStatsRxElemMissing_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 16),
    _WlanStatsRxElemMissing_Type()
)
wlanStatsRxElemMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxElemMissing.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxElemMissing.setUnits("frames")
_WlanStatsRxElemTooBig_Type = Counter32
_WlanStatsRxElemTooBig_Object = MibTableColumn
wlanStatsRxElemTooBig = _WlanStatsRxElemTooBig_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 17),
    _WlanStatsRxElemTooBig_Type()
)
wlanStatsRxElemTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxElemTooBig.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxElemTooBig.setUnits("frames")
_WlanStatsRxElemTooSmall_Type = Counter32
_WlanStatsRxElemTooSmall_Object = MibTableColumn
wlanStatsRxElemTooSmall = _WlanStatsRxElemTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 18),
    _WlanStatsRxElemTooSmall_Type()
)
wlanStatsRxElemTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxElemTooSmall.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxElemTooSmall.setUnits("frames")
_WlanStatsRxElemUnknown_Type = Counter32
_WlanStatsRxElemUnknown_Object = MibTableColumn
wlanStatsRxElemUnknown = _WlanStatsRxElemUnknown_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 19),
    _WlanStatsRxElemUnknown_Type()
)
wlanStatsRxElemUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxElemUnknown.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxElemUnknown.setUnits("frames")
_WlanStatsRxChannelMismatch_Type = Counter32
_WlanStatsRxChannelMismatch_Object = MibTableColumn
wlanStatsRxChannelMismatch = _WlanStatsRxChannelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 20),
    _WlanStatsRxChannelMismatch_Type()
)
wlanStatsRxChannelMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxChannelMismatch.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxChannelMismatch.setUnits("frames")
_WlanStatsRxDropped_Type = Counter32
_WlanStatsRxDropped_Object = MibTableColumn
wlanStatsRxDropped = _WlanStatsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 21),
    _WlanStatsRxDropped_Type()
)
wlanStatsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDropped.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDropped.setUnits("frames")
_WlanStatsRxSsidMismatch_Type = Counter32
_WlanStatsRxSsidMismatch_Object = MibTableColumn
wlanStatsRxSsidMismatch = _WlanStatsRxSsidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 22),
    _WlanStatsRxSsidMismatch_Type()
)
wlanStatsRxSsidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxSsidMismatch.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxSsidMismatch.setUnits("frames")
_WlanStatsRxAuthNotSupported_Type = Counter32
_WlanStatsRxAuthNotSupported_Object = MibTableColumn
wlanStatsRxAuthNotSupported = _WlanStatsRxAuthNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 23),
    _WlanStatsRxAuthNotSupported_Type()
)
wlanStatsRxAuthNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAuthNotSupported.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAuthNotSupported.setUnits("frames")
_WlanStatsRxAuthFailed_Type = Counter32
_WlanStatsRxAuthFailed_Object = MibTableColumn
wlanStatsRxAuthFailed = _WlanStatsRxAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 24),
    _WlanStatsRxAuthFailed_Type()
)
wlanStatsRxAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAuthFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAuthFailed.setUnits("frames")
_WlanStatsRxAuthCM_Type = Counter32
_WlanStatsRxAuthCM_Object = MibTableColumn
wlanStatsRxAuthCM = _WlanStatsRxAuthCM_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 25),
    _WlanStatsRxAuthCM_Type()
)
wlanStatsRxAuthCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAuthCM.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAuthCM.setUnits("frames")
_WlanStatsRxAssocWrongBssid_Type = Counter32
_WlanStatsRxAssocWrongBssid_Object = MibTableColumn
wlanStatsRxAssocWrongBssid = _WlanStatsRxAssocWrongBssid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 26),
    _WlanStatsRxAssocWrongBssid_Type()
)
wlanStatsRxAssocWrongBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAssocWrongBssid.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAssocWrongBssid.setUnits("frames")
_WlanStatsRxAssocNoAuth_Type = Counter32
_WlanStatsRxAssocNoAuth_Object = MibTableColumn
wlanStatsRxAssocNoAuth = _WlanStatsRxAssocNoAuth_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 27),
    _WlanStatsRxAssocNoAuth_Type()
)
wlanStatsRxAssocNoAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAssocNoAuth.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAssocNoAuth.setUnits("frames")
_WlanStatsRxAssocCapMismatch_Type = Counter32
_WlanStatsRxAssocCapMismatch_Object = MibTableColumn
wlanStatsRxAssocCapMismatch = _WlanStatsRxAssocCapMismatch_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 28),
    _WlanStatsRxAssocCapMismatch_Type()
)
wlanStatsRxAssocCapMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAssocCapMismatch.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAssocCapMismatch.setUnits("frames")
_WlanStatsRxAssocNoRateMatch_Type = Counter32
_WlanStatsRxAssocNoRateMatch_Object = MibTableColumn
wlanStatsRxAssocNoRateMatch = _WlanStatsRxAssocNoRateMatch_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 29),
    _WlanStatsRxAssocNoRateMatch_Type()
)
wlanStatsRxAssocNoRateMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAssocNoRateMatch.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAssocNoRateMatch.setUnits("frames")
_WlanStatsRxBadWpaIE_Type = Counter32
_WlanStatsRxBadWpaIE_Object = MibTableColumn
wlanStatsRxBadWpaIE = _WlanStatsRxBadWpaIE_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 30),
    _WlanStatsRxBadWpaIE_Type()
)
wlanStatsRxBadWpaIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxBadWpaIE.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxBadWpaIE.setUnits("frames")
_WlanStatsRxDeauthenticate_Type = Counter32
_WlanStatsRxDeauthenticate_Object = MibTableColumn
wlanStatsRxDeauthenticate = _WlanStatsRxDeauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 31),
    _WlanStatsRxDeauthenticate_Type()
)
wlanStatsRxDeauthenticate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDeauthenticate.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDeauthenticate.setUnits("frames")
_WlanStatsRxDisassociate_Type = Counter32
_WlanStatsRxDisassociate_Object = MibTableColumn
wlanStatsRxDisassociate = _WlanStatsRxDisassociate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 32),
    _WlanStatsRxDisassociate_Type()
)
wlanStatsRxDisassociate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDisassociate.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDisassociate.setUnits("frames")
_WlanStatsRxUnknownSubtype_Type = Counter32
_WlanStatsRxUnknownSubtype_Object = MibTableColumn
wlanStatsRxUnknownSubtype = _WlanStatsRxUnknownSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 33),
    _WlanStatsRxUnknownSubtype_Type()
)
wlanStatsRxUnknownSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxUnknownSubtype.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxUnknownSubtype.setUnits("frames")
_WlanStatsRxFailedNoBuf_Type = Counter32
_WlanStatsRxFailedNoBuf_Object = MibTableColumn
wlanStatsRxFailedNoBuf = _WlanStatsRxFailedNoBuf_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 34),
    _WlanStatsRxFailedNoBuf_Type()
)
wlanStatsRxFailedNoBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxFailedNoBuf.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxFailedNoBuf.setUnits("frames")
_WlanStatsRxBadAuthRequest_Type = Counter32
_WlanStatsRxBadAuthRequest_Object = MibTableColumn
wlanStatsRxBadAuthRequest = _WlanStatsRxBadAuthRequest_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 35),
    _WlanStatsRxBadAuthRequest_Type()
)
wlanStatsRxBadAuthRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxBadAuthRequest.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxBadAuthRequest.setUnits("frames")
_WlanStatsRxUnAuthorized_Type = Counter32
_WlanStatsRxUnAuthorized_Object = MibTableColumn
wlanStatsRxUnAuthorized = _WlanStatsRxUnAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 36),
    _WlanStatsRxUnAuthorized_Type()
)
wlanStatsRxUnAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxUnAuthorized.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxUnAuthorized.setUnits("frames")
_WlanStatsRxBadKeyId_Type = Counter32
_WlanStatsRxBadKeyId_Object = MibTableColumn
wlanStatsRxBadKeyId = _WlanStatsRxBadKeyId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 37),
    _WlanStatsRxBadKeyId_Type()
)
wlanStatsRxBadKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxBadKeyId.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxBadKeyId.setUnits("frames")
_WlanStatsRxCCMPSeqViolation_Type = Counter32
_WlanStatsRxCCMPSeqViolation_Object = MibTableColumn
wlanStatsRxCCMPSeqViolation = _WlanStatsRxCCMPSeqViolation_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 38),
    _WlanStatsRxCCMPSeqViolation_Type()
)
wlanStatsRxCCMPSeqViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxCCMPSeqViolation.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxCCMPSeqViolation.setUnits("frames")
_WlanStatsRxCCMPBadFormat_Type = Counter32
_WlanStatsRxCCMPBadFormat_Object = MibTableColumn
wlanStatsRxCCMPBadFormat = _WlanStatsRxCCMPBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 39),
    _WlanStatsRxCCMPBadFormat_Type()
)
wlanStatsRxCCMPBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxCCMPBadFormat.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxCCMPBadFormat.setUnits("frames")
_WlanStatsRxCCMPFailedMIC_Type = Counter32
_WlanStatsRxCCMPFailedMIC_Object = MibTableColumn
wlanStatsRxCCMPFailedMIC = _WlanStatsRxCCMPFailedMIC_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 40),
    _WlanStatsRxCCMPFailedMIC_Type()
)
wlanStatsRxCCMPFailedMIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxCCMPFailedMIC.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxCCMPFailedMIC.setUnits("frames")
_WlanStatsRxTKIPSeqViolation_Type = Counter32
_WlanStatsRxTKIPSeqViolation_Object = MibTableColumn
wlanStatsRxTKIPSeqViolation = _WlanStatsRxTKIPSeqViolation_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 41),
    _WlanStatsRxTKIPSeqViolation_Type()
)
wlanStatsRxTKIPSeqViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPSeqViolation.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPSeqViolation.setUnits("frames")
_WlanStatsRxTKIPBadFormat_Type = Counter32
_WlanStatsRxTKIPBadFormat_Object = MibTableColumn
wlanStatsRxTKIPBadFormat = _WlanStatsRxTKIPBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 42),
    _WlanStatsRxTKIPBadFormat_Type()
)
wlanStatsRxTKIPBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPBadFormat.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPBadFormat.setUnits("frames")
_WlanStatsRxTKIPFailedMIC_Type = Counter32
_WlanStatsRxTKIPFailedMIC_Object = MibTableColumn
wlanStatsRxTKIPFailedMIC = _WlanStatsRxTKIPFailedMIC_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 43),
    _WlanStatsRxTKIPFailedMIC_Type()
)
wlanStatsRxTKIPFailedMIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPFailedMIC.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPFailedMIC.setUnits("frames")
_WlanStatsRxTKIPFailedICV_Type = Counter32
_WlanStatsRxTKIPFailedICV_Object = MibTableColumn
wlanStatsRxTKIPFailedICV = _WlanStatsRxTKIPFailedICV_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 44),
    _WlanStatsRxTKIPFailedICV_Type()
)
wlanStatsRxTKIPFailedICV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPFailedICV.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxTKIPFailedICV.setUnits("frames")
_WlanStatsRxDiscardACL_Type = Counter32
_WlanStatsRxDiscardACL_Object = MibTableColumn
wlanStatsRxDiscardACL = _WlanStatsRxDiscardACL_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 45),
    _WlanStatsRxDiscardACL_Type()
)
wlanStatsRxDiscardACL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardACL.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardACL.setUnits("frames")
_WlanStatsTxFailedNoBuf_Type = Counter32
_WlanStatsTxFailedNoBuf_Object = MibTableColumn
wlanStatsTxFailedNoBuf = _WlanStatsTxFailedNoBuf_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 46),
    _WlanStatsTxFailedNoBuf_Type()
)
wlanStatsTxFailedNoBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxFailedNoBuf.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxFailedNoBuf.setUnits("frames")
_WlanStatsTxFailedNoNode_Type = Counter32
_WlanStatsTxFailedNoNode_Object = MibTableColumn
wlanStatsTxFailedNoNode = _WlanStatsTxFailedNoNode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 47),
    _WlanStatsTxFailedNoNode_Type()
)
wlanStatsTxFailedNoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxFailedNoNode.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxFailedNoNode.setUnits("frames")
_WlanStatsTxUnknownMgmt_Type = Counter32
_WlanStatsTxUnknownMgmt_Object = MibTableColumn
wlanStatsTxUnknownMgmt = _WlanStatsTxUnknownMgmt_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 48),
    _WlanStatsTxUnknownMgmt_Type()
)
wlanStatsTxUnknownMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxUnknownMgmt.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxUnknownMgmt.setUnits("frames")
_WlanStatsTxBadCipher_Type = Counter32
_WlanStatsTxBadCipher_Object = MibTableColumn
wlanStatsTxBadCipher = _WlanStatsTxBadCipher_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 49),
    _WlanStatsTxBadCipher_Type()
)
wlanStatsTxBadCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxBadCipher.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxBadCipher.setUnits("frames")
_WlanStatsTxNoDefKey_Type = Counter32
_WlanStatsTxNoDefKey_Object = MibTableColumn
wlanStatsTxNoDefKey = _WlanStatsTxNoDefKey_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 50),
    _WlanStatsTxNoDefKey_Type()
)
wlanStatsTxNoDefKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxNoDefKey.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxNoDefKey.setUnits("frames")
_WlanStatsTxFragmented_Type = Counter32
_WlanStatsTxFragmented_Object = MibTableColumn
wlanStatsTxFragmented = _WlanStatsTxFragmented_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 51),
    _WlanStatsTxFragmented_Type()
)
wlanStatsTxFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxFragmented.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxFragmented.setUnits("frames")
_WlanStatsTxFragmentsCreated_Type = Counter32
_WlanStatsTxFragmentsCreated_Object = MibTableColumn
wlanStatsTxFragmentsCreated = _WlanStatsTxFragmentsCreated_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 52),
    _WlanStatsTxFragmentsCreated_Type()
)
wlanStatsTxFragmentsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxFragmentsCreated.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxFragmentsCreated.setUnits("frames")
_WlanStatsActiveScans_Type = Counter32
_WlanStatsActiveScans_Object = MibTableColumn
wlanStatsActiveScans = _WlanStatsActiveScans_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 53),
    _WlanStatsActiveScans_Type()
)
wlanStatsActiveScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsActiveScans.setStatus("current")
_WlanStatsPassiveScans_Type = Counter32
_WlanStatsPassiveScans_Object = MibTableColumn
wlanStatsPassiveScans = _WlanStatsPassiveScans_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 54),
    _WlanStatsPassiveScans_Type()
)
wlanStatsPassiveScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsPassiveScans.setStatus("current")
_WlanStatsTimeoutInactivity_Type = Counter32
_WlanStatsTimeoutInactivity_Object = MibTableColumn
wlanStatsTimeoutInactivity = _WlanStatsTimeoutInactivity_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 55),
    _WlanStatsTimeoutInactivity_Type()
)
wlanStatsTimeoutInactivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTimeoutInactivity.setStatus("current")
_WlanStatsCryptoNoMem_Type = Counter32
_WlanStatsCryptoNoMem_Object = MibTableColumn
wlanStatsCryptoNoMem = _WlanStatsCryptoNoMem_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 56),
    _WlanStatsCryptoNoMem_Type()
)
wlanStatsCryptoNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoNoMem.setStatus("current")
_WlanStatsSwCryptoTKIP_Type = Counter32
_WlanStatsSwCryptoTKIP_Object = MibTableColumn
wlanStatsSwCryptoTKIP = _WlanStatsSwCryptoTKIP_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 57),
    _WlanStatsSwCryptoTKIP_Type()
)
wlanStatsSwCryptoTKIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsSwCryptoTKIP.setStatus("current")
_WlanStatsSwCryptoTKIPEnMIC_Type = Counter32
_WlanStatsSwCryptoTKIPEnMIC_Object = MibTableColumn
wlanStatsSwCryptoTKIPEnMIC = _WlanStatsSwCryptoTKIPEnMIC_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 58),
    _WlanStatsSwCryptoTKIPEnMIC_Type()
)
wlanStatsSwCryptoTKIPEnMIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsSwCryptoTKIPEnMIC.setStatus("current")
_WlanStatsSwCryptoTKIPDeMIC_Type = Counter32
_WlanStatsSwCryptoTKIPDeMIC_Object = MibTableColumn
wlanStatsSwCryptoTKIPDeMIC = _WlanStatsSwCryptoTKIPDeMIC_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 59),
    _WlanStatsSwCryptoTKIPDeMIC_Type()
)
wlanStatsSwCryptoTKIPDeMIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsSwCryptoTKIPDeMIC.setStatus("current")
_WlanStatsCryptoTKIPCM_Type = Counter32
_WlanStatsCryptoTKIPCM_Object = MibTableColumn
wlanStatsCryptoTKIPCM = _WlanStatsCryptoTKIPCM_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 60),
    _WlanStatsCryptoTKIPCM_Type()
)
wlanStatsCryptoTKIPCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoTKIPCM.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsCryptoTKIPCM.setUnits("frames")
_WlanStatsSwCryptoCCMP_Type = Counter32
_WlanStatsSwCryptoCCMP_Object = MibTableColumn
wlanStatsSwCryptoCCMP = _WlanStatsSwCryptoCCMP_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 61),
    _WlanStatsSwCryptoCCMP_Type()
)
wlanStatsSwCryptoCCMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsSwCryptoCCMP.setStatus("current")
_WlanStatsSwCryptoWEP_Type = Counter32
_WlanStatsSwCryptoWEP_Object = MibTableColumn
wlanStatsSwCryptoWEP = _WlanStatsSwCryptoWEP_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 62),
    _WlanStatsSwCryptoWEP_Type()
)
wlanStatsSwCryptoWEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsSwCryptoWEP.setStatus("current")
_WlanStatsCryptoCipherKeyRejected_Type = Counter32
_WlanStatsCryptoCipherKeyRejected_Object = MibTableColumn
wlanStatsCryptoCipherKeyRejected = _WlanStatsCryptoCipherKeyRejected_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 63),
    _WlanStatsCryptoCipherKeyRejected_Type()
)
wlanStatsCryptoCipherKeyRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoCipherKeyRejected.setStatus("current")
_WlanStatsCryptoNoKey_Type = Counter32
_WlanStatsCryptoNoKey_Object = MibTableColumn
wlanStatsCryptoNoKey = _WlanStatsCryptoNoKey_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 64),
    _WlanStatsCryptoNoKey_Type()
)
wlanStatsCryptoNoKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoNoKey.setStatus("current")
_WlanStatsCryptoDeleteKeyFailed_Type = Counter32
_WlanStatsCryptoDeleteKeyFailed_Object = MibTableColumn
wlanStatsCryptoDeleteKeyFailed = _WlanStatsCryptoDeleteKeyFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 65),
    _WlanStatsCryptoDeleteKeyFailed_Type()
)
wlanStatsCryptoDeleteKeyFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoDeleteKeyFailed.setStatus("current")
_WlanStatsCryptoUnknownCipher_Type = Counter32
_WlanStatsCryptoUnknownCipher_Object = MibTableColumn
wlanStatsCryptoUnknownCipher = _WlanStatsCryptoUnknownCipher_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 66),
    _WlanStatsCryptoUnknownCipher_Type()
)
wlanStatsCryptoUnknownCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoUnknownCipher.setStatus("current")
_WlanStatsCryptoAttachFailed_Type = Counter32
_WlanStatsCryptoAttachFailed_Object = MibTableColumn
wlanStatsCryptoAttachFailed = _WlanStatsCryptoAttachFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 67),
    _WlanStatsCryptoAttachFailed_Type()
)
wlanStatsCryptoAttachFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoAttachFailed.setStatus("current")
_WlanStatsCryptoKeyFailed_Type = Counter32
_WlanStatsCryptoKeyFailed_Object = MibTableColumn
wlanStatsCryptoKeyFailed = _WlanStatsCryptoKeyFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 68),
    _WlanStatsCryptoKeyFailed_Type()
)
wlanStatsCryptoKeyFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoKeyFailed.setStatus("current")
_WlanStatsCryptoEnMICFailed_Type = Counter32
_WlanStatsCryptoEnMICFailed_Object = MibTableColumn
wlanStatsCryptoEnMICFailed = _WlanStatsCryptoEnMICFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 69),
    _WlanStatsCryptoEnMICFailed_Type()
)
wlanStatsCryptoEnMICFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsCryptoEnMICFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsCryptoEnMICFailed.setUnits("frames")
_WlanStatsIBSSCapMismatch_Type = Counter32
_WlanStatsIBSSCapMismatch_Object = MibTableColumn
wlanStatsIBSSCapMismatch = _WlanStatsIBSSCapMismatch_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 70),
    _WlanStatsIBSSCapMismatch_Type()
)
wlanStatsIBSSCapMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsIBSSCapMismatch.setStatus("current")
_WlanStatsUnassocStaPSPoll_Type = Counter32
_WlanStatsUnassocStaPSPoll_Object = MibTableColumn
wlanStatsUnassocStaPSPoll = _WlanStatsUnassocStaPSPoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 71),
    _WlanStatsUnassocStaPSPoll_Type()
)
wlanStatsUnassocStaPSPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsUnassocStaPSPoll.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsUnassocStaPSPoll.setUnits("frames")
_WlanStatsBadAidPSPoll_Type = Counter32
_WlanStatsBadAidPSPoll_Object = MibTableColumn
wlanStatsBadAidPSPoll = _WlanStatsBadAidPSPoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 72),
    _WlanStatsBadAidPSPoll_Type()
)
wlanStatsBadAidPSPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsBadAidPSPoll.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsBadAidPSPoll.setUnits("frames")
_WlanStatsEmptyPSPoll_Type = Counter32
_WlanStatsEmptyPSPoll_Object = MibTableColumn
wlanStatsEmptyPSPoll = _WlanStatsEmptyPSPoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 73),
    _WlanStatsEmptyPSPoll_Type()
)
wlanStatsEmptyPSPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsEmptyPSPoll.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsEmptyPSPoll.setUnits("frames")
_WlanStatsRxFFBadHdr_Type = Counter32
_WlanStatsRxFFBadHdr_Object = MibTableColumn
wlanStatsRxFFBadHdr = _WlanStatsRxFFBadHdr_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 74),
    _WlanStatsRxFFBadHdr_Type()
)
wlanStatsRxFFBadHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxFFBadHdr.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxFFBadHdr.setUnits("frames")
_WlanStatsRxFFTooShort_Type = Counter32
_WlanStatsRxFFTooShort_Object = MibTableColumn
wlanStatsRxFFTooShort = _WlanStatsRxFFTooShort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 75),
    _WlanStatsRxFFTooShort_Type()
)
wlanStatsRxFFTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxFFTooShort.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxFFTooShort.setUnits("frames")
_WlanStatsRxFFSplitError_Type = Counter32
_WlanStatsRxFFSplitError_Object = MibTableColumn
wlanStatsRxFFSplitError = _WlanStatsRxFFSplitError_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 76),
    _WlanStatsRxFFSplitError_Type()
)
wlanStatsRxFFSplitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxFFSplitError.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxFFSplitError.setUnits("frames")
_WlanStatsRxFFDecap_Type = Counter32
_WlanStatsRxFFDecap_Object = MibTableColumn
wlanStatsRxFFDecap = _WlanStatsRxFFDecap_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 77),
    _WlanStatsRxFFDecap_Type()
)
wlanStatsRxFFDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxFFDecap.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxFFDecap.setUnits("frames")
_WlanStatsTxFFEncap_Type = Counter32
_WlanStatsTxFFEncap_Object = MibTableColumn
wlanStatsTxFFEncap = _WlanStatsTxFFEncap_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 78),
    _WlanStatsTxFFEncap_Type()
)
wlanStatsTxFFEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxFFEncap.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxFFEncap.setUnits("frames")
_WlanStatsRxBadBintval_Type = Counter32
_WlanStatsRxBadBintval_Object = MibTableColumn
wlanStatsRxBadBintval = _WlanStatsRxBadBintval_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 79),
    _WlanStatsRxBadBintval_Type()
)
wlanStatsRxBadBintval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxBadBintval.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxBadBintval.setUnits("frames")
_WlanStatsRxDemicFailed_Type = Counter32
_WlanStatsRxDemicFailed_Object = MibTableColumn
wlanStatsRxDemicFailed = _WlanStatsRxDemicFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 80),
    _WlanStatsRxDemicFailed_Type()
)
wlanStatsRxDemicFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDemicFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDemicFailed.setUnits("frames")
_WlanStatsRxDefragFailed_Type = Counter32
_WlanStatsRxDefragFailed_Object = MibTableColumn
wlanStatsRxDefragFailed = _WlanStatsRxDefragFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 81),
    _WlanStatsRxDefragFailed_Type()
)
wlanStatsRxDefragFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDefragFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDefragFailed.setUnits("frames")
_WlanStatsRxMgmt_Type = Counter32
_WlanStatsRxMgmt_Object = MibTableColumn
wlanStatsRxMgmt = _WlanStatsRxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 82),
    _WlanStatsRxMgmt_Type()
)
wlanStatsRxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxMgmt.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxMgmt.setUnits("frames")
_WlanStatsRxActionMgmt_Type = Counter32
_WlanStatsRxActionMgmt_Object = MibTableColumn
wlanStatsRxActionMgmt = _WlanStatsRxActionMgmt_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 83),
    _WlanStatsRxActionMgmt_Type()
)
wlanStatsRxActionMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxActionMgmt.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxActionMgmt.setUnits("frames")
_WlanStatsRxAMSDUTooShort_Type = Counter32
_WlanStatsRxAMSDUTooShort_Object = MibTableColumn
wlanStatsRxAMSDUTooShort = _WlanStatsRxAMSDUTooShort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 84),
    _WlanStatsRxAMSDUTooShort_Type()
)
wlanStatsRxAMSDUTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAMSDUTooShort.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAMSDUTooShort.setUnits("frames")
_WlanStatsRxAMSDUSplitError_Type = Counter32
_WlanStatsRxAMSDUSplitError_Object = MibTableColumn
wlanStatsRxAMSDUSplitError = _WlanStatsRxAMSDUSplitError_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 85),
    _WlanStatsRxAMSDUSplitError_Type()
)
wlanStatsRxAMSDUSplitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAMSDUSplitError.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAMSDUSplitError.setUnits("frames")
_WlanStatsRxAMSDUDecap_Type = Counter32
_WlanStatsRxAMSDUDecap_Object = MibTableColumn
wlanStatsRxAMSDUDecap = _WlanStatsRxAMSDUDecap_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 86),
    _WlanStatsRxAMSDUDecap_Type()
)
wlanStatsRxAMSDUDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxAMSDUDecap.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxAMSDUDecap.setUnits("frames")
_WlanStatsTxAMSDUEncap_Type = Counter32
_WlanStatsTxAMSDUEncap_Object = MibTableColumn
wlanStatsTxAMSDUEncap = _WlanStatsTxAMSDUEncap_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 87),
    _WlanStatsTxAMSDUEncap_Type()
)
wlanStatsTxAMSDUEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxAMSDUEncap.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxAMSDUEncap.setUnits("frames")
_WlanStatsAMPDUBadBAR_Type = Counter32
_WlanStatsAMPDUBadBAR_Object = MibTableColumn
wlanStatsAMPDUBadBAR = _WlanStatsAMPDUBadBAR_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 88),
    _WlanStatsAMPDUBadBAR_Type()
)
wlanStatsAMPDUBadBAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDUBadBAR.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDUBadBAR.setUnits("frames")
_WlanStatsAMPDUOowBar_Type = Counter32
_WlanStatsAMPDUOowBar_Object = MibTableColumn
wlanStatsAMPDUOowBar = _WlanStatsAMPDUOowBar_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 89),
    _WlanStatsAMPDUOowBar_Type()
)
wlanStatsAMPDUOowBar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDUOowBar.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDUOowBar.setUnits("frames")
_WlanStatsAMPDUMovedBAR_Type = Counter32
_WlanStatsAMPDUMovedBAR_Object = MibTableColumn
wlanStatsAMPDUMovedBAR = _WlanStatsAMPDUMovedBAR_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 90),
    _WlanStatsAMPDUMovedBAR_Type()
)
wlanStatsAMPDUMovedBAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDUMovedBAR.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDUMovedBAR.setUnits("frames")
_WlanStatsAMPDURxBAR_Type = Counter32
_WlanStatsAMPDURxBAR_Object = MibTableColumn
wlanStatsAMPDURxBAR = _WlanStatsAMPDURxBAR_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 91),
    _WlanStatsAMPDURxBAR_Type()
)
wlanStatsAMPDURxBAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxBAR.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxBAR.setUnits("frames")
_WlanStatsAMPDURxOor_Type = Counter32
_WlanStatsAMPDURxOor_Object = MibTableColumn
wlanStatsAMPDURxOor = _WlanStatsAMPDURxOor_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 92),
    _WlanStatsAMPDURxOor_Type()
)
wlanStatsAMPDURxOor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxOor.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxOor.setUnits("frames")
_WlanStatsAMPDURxCopied_Type = Counter32
_WlanStatsAMPDURxCopied_Object = MibTableColumn
wlanStatsAMPDURxCopied = _WlanStatsAMPDURxCopied_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 93),
    _WlanStatsAMPDURxCopied_Type()
)
wlanStatsAMPDURxCopied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxCopied.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxCopied.setUnits("frames")
_WlanStatsAMPDURxDropped_Type = Counter32
_WlanStatsAMPDURxDropped_Object = MibTableColumn
wlanStatsAMPDURxDropped = _WlanStatsAMPDURxDropped_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 94),
    _WlanStatsAMPDURxDropped_Type()
)
wlanStatsAMPDURxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxDropped.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxDropped.setUnits("frames")
_WlanStatsTxDiscardBadState_Type = Counter32
_WlanStatsTxDiscardBadState_Object = MibTableColumn
wlanStatsTxDiscardBadState = _WlanStatsTxDiscardBadState_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 95),
    _WlanStatsTxDiscardBadState_Type()
)
wlanStatsTxDiscardBadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxDiscardBadState.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxDiscardBadState.setUnits("frames")
_WlanStatsTxFailedNoAssoc_Type = Counter32
_WlanStatsTxFailedNoAssoc_Object = MibTableColumn
wlanStatsTxFailedNoAssoc = _WlanStatsTxFailedNoAssoc_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 96),
    _WlanStatsTxFailedNoAssoc_Type()
)
wlanStatsTxFailedNoAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxFailedNoAssoc.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxFailedNoAssoc.setUnits("frames")
_WlanStatsTxClassifyFailed_Type = Counter32
_WlanStatsTxClassifyFailed_Object = MibTableColumn
wlanStatsTxClassifyFailed = _WlanStatsTxClassifyFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 97),
    _WlanStatsTxClassifyFailed_Type()
)
wlanStatsTxClassifyFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxClassifyFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxClassifyFailed.setUnits("frames")
_WlanStatsDwdsMcastDiscard_Type = Counter32
_WlanStatsDwdsMcastDiscard_Object = MibTableColumn
wlanStatsDwdsMcastDiscard = _WlanStatsDwdsMcastDiscard_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 98),
    _WlanStatsDwdsMcastDiscard_Type()
)
wlanStatsDwdsMcastDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsDwdsMcastDiscard.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsDwdsMcastDiscard.setUnits("frames")
_WlanStatsHTAssocRejectNoHT_Type = Counter32
_WlanStatsHTAssocRejectNoHT_Object = MibTableColumn
wlanStatsHTAssocRejectNoHT = _WlanStatsHTAssocRejectNoHT_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 99),
    _WlanStatsHTAssocRejectNoHT_Type()
)
wlanStatsHTAssocRejectNoHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsHTAssocRejectNoHT.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsHTAssocRejectNoHT.setUnits("frames")
_WlanStatsHTAssocDowngrade_Type = Counter32
_WlanStatsHTAssocDowngrade_Object = MibTableColumn
wlanStatsHTAssocDowngrade = _WlanStatsHTAssocDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 100),
    _WlanStatsHTAssocDowngrade_Type()
)
wlanStatsHTAssocDowngrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsHTAssocDowngrade.setStatus("current")
_WlanStatsHTAssocRateMismatch_Type = Counter32
_WlanStatsHTAssocRateMismatch_Object = MibTableColumn
wlanStatsHTAssocRateMismatch = _WlanStatsHTAssocRateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 101),
    _WlanStatsHTAssocRateMismatch_Type()
)
wlanStatsHTAssocRateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsHTAssocRateMismatch.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsHTAssocRateMismatch.setUnits("frames")
_WlanStatsAMPDURxAge_Type = Counter32
_WlanStatsAMPDURxAge_Object = MibTableColumn
wlanStatsAMPDURxAge = _WlanStatsAMPDURxAge_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 102),
    _WlanStatsAMPDURxAge_Type()
)
wlanStatsAMPDURxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxAge.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxAge.setUnits("frames")
_WlanStatsAMPDUMoved_Type = Counter32
_WlanStatsAMPDUMoved_Object = MibTableColumn
wlanStatsAMPDUMoved = _WlanStatsAMPDUMoved_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 103),
    _WlanStatsAMPDUMoved_Type()
)
wlanStatsAMPDUMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDUMoved.setStatus("current")
_WlanStatsADDBADisabledReject_Type = Counter32
_WlanStatsADDBADisabledReject_Object = MibTableColumn
wlanStatsADDBADisabledReject = _WlanStatsADDBADisabledReject_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 104),
    _WlanStatsADDBADisabledReject_Type()
)
wlanStatsADDBADisabledReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsADDBADisabledReject.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsADDBADisabledReject.setUnits("frames")
_WlanStatsADDBANoRequest_Type = Counter32
_WlanStatsADDBANoRequest_Object = MibTableColumn
wlanStatsADDBANoRequest = _WlanStatsADDBANoRequest_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 105),
    _WlanStatsADDBANoRequest_Type()
)
wlanStatsADDBANoRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsADDBANoRequest.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsADDBANoRequest.setUnits("frames")
_WlanStatsADDBABadToken_Type = Counter32
_WlanStatsADDBABadToken_Object = MibTableColumn
wlanStatsADDBABadToken = _WlanStatsADDBABadToken_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 106),
    _WlanStatsADDBABadToken_Type()
)
wlanStatsADDBABadToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsADDBABadToken.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsADDBABadToken.setUnits("frames")
_WlanStatsADDBABadPolicy_Type = Counter32
_WlanStatsADDBABadPolicy_Object = MibTableColumn
wlanStatsADDBABadPolicy = _WlanStatsADDBABadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 107),
    _WlanStatsADDBABadPolicy_Type()
)
wlanStatsADDBABadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsADDBABadPolicy.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsADDBABadPolicy.setUnits("frames")
_WlanStatsAMPDUStopped_Type = Counter32
_WlanStatsAMPDUStopped_Object = MibTableColumn
wlanStatsAMPDUStopped = _WlanStatsAMPDUStopped_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 108),
    _WlanStatsAMPDUStopped_Type()
)
wlanStatsAMPDUStopped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDUStopped.setStatus("current")
_WlanStatsAMPDUStopFailed_Type = Counter32
_WlanStatsAMPDUStopFailed_Object = MibTableColumn
wlanStatsAMPDUStopFailed = _WlanStatsAMPDUStopFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 109),
    _WlanStatsAMPDUStopFailed_Type()
)
wlanStatsAMPDUStopFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDUStopFailed.setStatus("current")
_WlanStatsAMPDURxReorder_Type = Counter32
_WlanStatsAMPDURxReorder_Object = MibTableColumn
wlanStatsAMPDURxReorder = _WlanStatsAMPDURxReorder_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 110),
    _WlanStatsAMPDURxReorder_Type()
)
wlanStatsAMPDURxReorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxReorder.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURxReorder.setUnits("frames")
_WlanStatsScansBackground_Type = Counter32
_WlanStatsScansBackground_Object = MibTableColumn
wlanStatsScansBackground = _WlanStatsScansBackground_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 111),
    _WlanStatsScansBackground_Type()
)
wlanStatsScansBackground.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsScansBackground.setStatus("current")
_WlanLastDeauthReason_Type = WlanMgmtReasonCode
_WlanLastDeauthReason_Object = MibTableColumn
wlanLastDeauthReason = _WlanLastDeauthReason_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 112),
    _WlanLastDeauthReason_Type()
)
wlanLastDeauthReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanLastDeauthReason.setStatus("current")
_WlanLastDissasocReason_Type = WlanMgmtReasonCode
_WlanLastDissasocReason_Object = MibTableColumn
wlanLastDissasocReason = _WlanLastDissasocReason_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 113),
    _WlanLastDissasocReason_Type()
)
wlanLastDissasocReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanLastDissasocReason.setStatus("current")
_WlanLastAuthFailReason_Type = WlanMgmtReasonCode
_WlanLastAuthFailReason_Object = MibTableColumn
wlanLastAuthFailReason = _WlanLastAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 114),
    _WlanLastAuthFailReason_Type()
)
wlanLastAuthFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanLastAuthFailReason.setStatus("current")
_WlanStatsBeaconMissedEvents_Type = Counter32
_WlanStatsBeaconMissedEvents_Object = MibTableColumn
wlanStatsBeaconMissedEvents = _WlanStatsBeaconMissedEvents_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 115),
    _WlanStatsBeaconMissedEvents_Type()
)
wlanStatsBeaconMissedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsBeaconMissedEvents.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsBeaconMissedEvents.setUnits("frames")
_WlanStatsRxDiscardBadStates_Type = Counter32
_WlanStatsRxDiscardBadStates_Object = MibTableColumn
wlanStatsRxDiscardBadStates = _WlanStatsRxDiscardBadStates_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 116),
    _WlanStatsRxDiscardBadStates_Type()
)
wlanStatsRxDiscardBadStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardBadStates.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsRxDiscardBadStates.setUnits("frames")
_WlanStatsFFFlushed_Type = Counter32
_WlanStatsFFFlushed_Object = MibTableColumn
wlanStatsFFFlushed = _WlanStatsFFFlushed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 117),
    _WlanStatsFFFlushed_Type()
)
wlanStatsFFFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsFFFlushed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsFFFlushed.setUnits("frames")
_WlanStatsTxControlFrames_Type = Counter32
_WlanStatsTxControlFrames_Object = MibTableColumn
wlanStatsTxControlFrames = _WlanStatsTxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 118),
    _WlanStatsTxControlFrames_Type()
)
wlanStatsTxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsTxControlFrames.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsTxControlFrames.setUnits("frames")
_WlanStatsAMPDURexmt_Type = Counter32
_WlanStatsAMPDURexmt_Object = MibTableColumn
wlanStatsAMPDURexmt = _WlanStatsAMPDURexmt_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 119),
    _WlanStatsAMPDURexmt_Type()
)
wlanStatsAMPDURexmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURexmt.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURexmt.setUnits("frames")
_WlanStatsAMPDURexmtFailed_Type = Counter32
_WlanStatsAMPDURexmtFailed_Object = MibTableColumn
wlanStatsAMPDURexmtFailed = _WlanStatsAMPDURexmtFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 120),
    _WlanStatsAMPDURexmtFailed_Type()
)
wlanStatsAMPDURexmtFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAMPDURexmtFailed.setStatus("current")
if mibBuilder.loadTexts:
    wlanStatsAMPDURexmtFailed.setUnits("frames")


class _WlanStatsReset_Type(Integer32):
    """Custom type wlanStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("no-op", 1))
    )


_WlanStatsReset_Type.__name__ = "Integer32"
_WlanStatsReset_Object = MibTableColumn
wlanStatsReset = _WlanStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 3, 1, 1, 121),
    _WlanStatsReset_Type()
)
wlanStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanStatsReset.setStatus("current")
_BegemotWlanWep_ObjectIdentity = ObjectIdentity
begemotWlanWep = _BegemotWlanWep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4)
)
_WlanWepInterfaceTable_Object = MibTable
wlanWepInterfaceTable = _WlanWepInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 1)
)
if mibBuilder.loadTexts:
    wlanWepInterfaceTable.setStatus("current")
_WlanWepInterfaceEntry_Object = MibTableRow
wlanWepInterfaceEntry = _WlanWepInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 1, 1)
)
wlanWepInterfaceEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanWepInterfaceEntry.setStatus("current")


class _WlanWepMode_Type(Integer32):
    """Custom type wlanWepMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 2),
          ("off", 0),
          ("on", 1))
    )


_WlanWepMode_Type.__name__ = "Integer32"
_WlanWepMode_Object = MibTableColumn
wlanWepMode = _WlanWepMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 1, 1, 1),
    _WlanWepMode_Type()
)
wlanWepMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepMode.setStatus("current")
_WlanWepDefTxKey_Type = Integer32
_WlanWepDefTxKey_Object = MibTableColumn
wlanWepDefTxKey = _WlanWepDefTxKey_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 1, 1, 2),
    _WlanWepDefTxKey_Type()
)
wlanWepDefTxKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepDefTxKey.setStatus("current")
_WlanWepKeyTable_Object = MibTable
wlanWepKeyTable = _WlanWepKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 2)
)
if mibBuilder.loadTexts:
    wlanWepKeyTable.setStatus("current")
_WlanWepKeyEntry_Object = MibTableRow
wlanWepKeyEntry = _WlanWepKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 2, 1)
)
wlanWepKeyEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanWepKeyID"),
)
if mibBuilder.loadTexts:
    wlanWepKeyEntry.setStatus("current")


class _WlanWepKeyID_Type(Integer32):
    """Custom type wlanWepKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlanWepKeyID_Type.__name__ = "Integer32"
_WlanWepKeyID_Object = MibTableColumn
wlanWepKeyID = _WlanWepKeyID_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 2, 1, 1),
    _WlanWepKeyID_Type()
)
wlanWepKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKeyID.setStatus("current")
_WlanWepKeyLength_Type = Integer32
_WlanWepKeyLength_Object = MibTableColumn
wlanWepKeyLength = _WlanWepKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 2, 1, 2),
    _WlanWepKeyLength_Type()
)
wlanWepKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanWepKeyLength.setStatus("current")
_WlanWepKeySet_Type = OctetString
_WlanWepKeySet_Object = MibTableColumn
wlanWepKeySet = _WlanWepKeySet_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 2, 1, 3),
    _WlanWepKeySet_Type()
)
wlanWepKeySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKeySet.setStatus("current")
_WlanWepKeyHash_Type = OctetString
_WlanWepKeyHash_Object = MibTableColumn
wlanWepKeyHash = _WlanWepKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 2, 1, 4),
    _WlanWepKeyHash_Type()
)
wlanWepKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanWepKeyHash.setStatus("current")
_WlanWepKeyStatus_Type = RowStatus
_WlanWepKeyStatus_Object = MibTableColumn
wlanWepKeyStatus = _WlanWepKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 4, 2, 1, 5),
    _WlanWepKeyStatus_Type()
)
wlanWepKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanWepKeyStatus.setStatus("current")
_BegemotWlanMACAccessControl_ObjectIdentity = ObjectIdentity
begemotWlanMACAccessControl = _BegemotWlanMACAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5)
)
_WlanMACAccessControlTable_Object = MibTable
wlanMACAccessControlTable = _WlanMACAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 1)
)
if mibBuilder.loadTexts:
    wlanMACAccessControlTable.setStatus("current")
_WlanMACAccessControlEntry_Object = MibTableRow
wlanMACAccessControlEntry = _WlanMACAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 1, 1)
)
wlanMACAccessControlEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanMACAccessControlEntry.setStatus("current")


class _WlanMACAccessControlPolicy_Type(Integer32):
    """Custom type wlanMACAccessControlPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("open", 0),
          ("radius", 7))
    )


_WlanMACAccessControlPolicy_Type.__name__ = "Integer32"
_WlanMACAccessControlPolicy_Object = MibTableColumn
wlanMACAccessControlPolicy = _WlanMACAccessControlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 1, 1, 1),
    _WlanMACAccessControlPolicy_Type()
)
wlanMACAccessControlPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMACAccessControlPolicy.setStatus("current")
_WlanMACAccessControlNacl_Type = Counter32
_WlanMACAccessControlNacl_Object = MibTableColumn
wlanMACAccessControlNacl = _WlanMACAccessControlNacl_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 1, 1, 2),
    _WlanMACAccessControlNacl_Type()
)
wlanMACAccessControlNacl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMACAccessControlNacl.setStatus("current")


class _WlanMACAccessControlFlush_Type(Integer32):
    """Custom type wlanMACAccessControlFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flush", 1),
          ("no-op", 0))
    )


_WlanMACAccessControlFlush_Type.__name__ = "Integer32"
_WlanMACAccessControlFlush_Object = MibTableColumn
wlanMACAccessControlFlush = _WlanMACAccessControlFlush_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 1, 1, 3),
    _WlanMACAccessControlFlush_Type()
)
wlanMACAccessControlFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMACAccessControlFlush.setStatus("current")
_WlanMACAccessControlMACTable_Object = MibTable
wlanMACAccessControlMACTable = _WlanMACAccessControlMACTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 2)
)
if mibBuilder.loadTexts:
    wlanMACAccessControlMACTable.setStatus("current")
_WlanMACAccessControlMACEntry_Object = MibTableRow
wlanMACAccessControlMACEntry = _WlanMACAccessControlMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 2, 1)
)
wlanMACAccessControlMACEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanMACAccessControlMAC"),
)
if mibBuilder.loadTexts:
    wlanMACAccessControlMACEntry.setStatus("current")
_WlanMACAccessControlMAC_Type = MacAddress
_WlanMACAccessControlMAC_Object = MibTableColumn
wlanMACAccessControlMAC = _WlanMACAccessControlMAC_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 2, 1, 1),
    _WlanMACAccessControlMAC_Type()
)
wlanMACAccessControlMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMACAccessControlMAC.setStatus("current")
_WlanMACAccessControlMACStatus_Type = RowStatus
_WlanMACAccessControlMACStatus_Object = MibTableColumn
wlanMACAccessControlMACStatus = _WlanMACAccessControlMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 5, 2, 1, 2),
    _WlanMACAccessControlMACStatus_Type()
)
wlanMACAccessControlMACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMACAccessControlMACStatus.setStatus("current")
_BegemotWlanMeshRouting_ObjectIdentity = ObjectIdentity
begemotWlanMeshRouting = _BegemotWlanMeshRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6)
)
_WlanMeshRoutingConfig_ObjectIdentity = ObjectIdentity
wlanMeshRoutingConfig = _WlanMeshRoutingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 1)
)


class _WlanMeshMaxRetries_Type(Integer32):
    """Custom type wlanMeshMaxRetries based on Integer32"""
    defaultValue = 2


_WlanMeshMaxRetries_Object = MibScalar
wlanMeshMaxRetries = _WlanMeshMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 1, 1),
    _WlanMeshMaxRetries_Type()
)
wlanMeshMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshMaxRetries.setStatus("current")


class _WlanMeshConfirmTimeout_Type(Integer32):
    """Custom type wlanMeshConfirmTimeout based on Integer32"""
    defaultValue = 40


_WlanMeshConfirmTimeout_Object = MibScalar
wlanMeshConfirmTimeout = _WlanMeshConfirmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 1, 2),
    _WlanMeshConfirmTimeout_Type()
)
wlanMeshConfirmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshConfirmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshConfirmTimeout.setUnits("milliseconds")


class _WlanMeshHoldingTimeout_Type(Integer32):
    """Custom type wlanMeshHoldingTimeout based on Integer32"""
    defaultValue = 40


_WlanMeshHoldingTimeout_Object = MibScalar
wlanMeshHoldingTimeout = _WlanMeshHoldingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 1, 3),
    _WlanMeshHoldingTimeout_Type()
)
wlanMeshHoldingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshHoldingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshHoldingTimeout.setUnits("milliseconds")


class _WlanMeshRetryTimeout_Type(Integer32):
    """Custom type wlanMeshRetryTimeout based on Integer32"""
    defaultValue = 40


_WlanMeshRetryTimeout_Object = MibScalar
wlanMeshRetryTimeout = _WlanMeshRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 1, 4),
    _WlanMeshRetryTimeout_Type()
)
wlanMeshRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshRetryTimeout.setUnits("milliseconds")
_WlanMeshInterface_ObjectIdentity = ObjectIdentity
wlanMeshInterface = _WlanMeshInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2)
)
_WlanMeshInterfaceTable_Object = MibTable
wlanMeshInterfaceTable = _WlanMeshInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1)
)
if mibBuilder.loadTexts:
    wlanMeshInterfaceTable.setStatus("current")
_WlanMeshInterfaceEntry_Object = MibTableRow
wlanMeshInterfaceEntry = _WlanMeshInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1)
)
wlanMeshInterfaceEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanMeshInterfaceEntry.setStatus("current")


class _WlanMeshId_Type(OctetString):
    """Custom type wlanMeshId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanMeshId_Type.__name__ = "OctetString"
_WlanMeshId_Object = MibTableColumn
wlanMeshId = _WlanMeshId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1, 1),
    _WlanMeshId_Type()
)
wlanMeshId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshId.setStatus("current")


class _WlanMeshTTL_Type(Integer32):
    """Custom type wlanMeshTTL based on Integer32"""
    defaultValue = 31


_WlanMeshTTL_Object = MibTableColumn
wlanMeshTTL = _WlanMeshTTL_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1, 2),
    _WlanMeshTTL_Type()
)
wlanMeshTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshTTL.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshTTL.setUnits("hops")


class _WlanMeshPeeringEnabled_Type(TruthValue):
    """Custom type wlanMeshPeeringEnabled based on TruthValue"""


_WlanMeshPeeringEnabled_Object = MibTableColumn
wlanMeshPeeringEnabled = _WlanMeshPeeringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1, 3),
    _WlanMeshPeeringEnabled_Type()
)
wlanMeshPeeringEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshPeeringEnabled.setStatus("current")


class _WlanMeshForwardingEnabled_Type(TruthValue):
    """Custom type wlanMeshForwardingEnabled based on TruthValue"""


_WlanMeshForwardingEnabled_Object = MibTableColumn
wlanMeshForwardingEnabled = _WlanMeshForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1, 4),
    _WlanMeshForwardingEnabled_Type()
)
wlanMeshForwardingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshForwardingEnabled.setStatus("current")


class _WlanMeshMetric_Type(Integer32):
    """Custom type wlanMeshMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("airtime", 1),
          ("unknown", 0))
    )


_WlanMeshMetric_Type.__name__ = "Integer32"
_WlanMeshMetric_Object = MibTableColumn
wlanMeshMetric = _WlanMeshMetric_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1, 5),
    _WlanMeshMetric_Type()
)
wlanMeshMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshMetric.setStatus("current")


class _WlanMeshPath_Type(Integer32):
    """Custom type wlanMeshPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hwmp", 1),
          ("unknown", 0))
    )


_WlanMeshPath_Type.__name__ = "Integer32"
_WlanMeshPath_Object = MibTableColumn
wlanMeshPath = _WlanMeshPath_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1, 6),
    _WlanMeshPath_Type()
)
wlanMeshPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshPath.setStatus("current")


class _WlanMeshRoutesFlush_Type(Integer32):
    """Custom type wlanMeshRoutesFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flush", 1),
          ("no-op", 0))
    )


_WlanMeshRoutesFlush_Type.__name__ = "Integer32"
_WlanMeshRoutesFlush_Object = MibTableColumn
wlanMeshRoutesFlush = _WlanMeshRoutesFlush_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 1, 1, 7),
    _WlanMeshRoutesFlush_Type()
)
wlanMeshRoutesFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshRoutesFlush.setStatus("current")
_WlanMeshNeighborTable_Object = MibTable
wlanMeshNeighborTable = _WlanMeshNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2)
)
if mibBuilder.loadTexts:
    wlanMeshNeighborTable.setStatus("current")
_WlanMeshNeighborEntry_Object = MibTableRow
wlanMeshNeighborEntry = _WlanMeshNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1)
)
wlanMeshNeighborEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanMeshNeighborAddress"),
)
if mibBuilder.loadTexts:
    wlanMeshNeighborEntry.setStatus("current")
_WlanMeshNeighborAddress_Type = MacAddress
_WlanMeshNeighborAddress_Object = MibTableColumn
wlanMeshNeighborAddress = _WlanMeshNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 1),
    _WlanMeshNeighborAddress_Type()
)
wlanMeshNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborAddress.setStatus("current")
_WlanMeshNeighborFrequency_Type = Integer32
_WlanMeshNeighborFrequency_Object = MibTableColumn
wlanMeshNeighborFrequency = _WlanMeshNeighborFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 2),
    _WlanMeshNeighborFrequency_Type()
)
wlanMeshNeighborFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborFrequency.setStatus("current")
_WlanMeshNeighborLocalId_Type = Integer32
_WlanMeshNeighborLocalId_Object = MibTableColumn
wlanMeshNeighborLocalId = _WlanMeshNeighborLocalId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 3),
    _WlanMeshNeighborLocalId_Type()
)
wlanMeshNeighborLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborLocalId.setStatus("current")
_WlanMeshNeighborPeerId_Type = Integer32
_WlanMeshNeighborPeerId_Object = MibTableColumn
wlanMeshNeighborPeerId = _WlanMeshNeighborPeerId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 4),
    _WlanMeshNeighborPeerId_Type()
)
wlanMeshNeighborPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborPeerId.setStatus("current")


class _WlanMeshNeighborPeerState_Type(Integer32):
    """Custom type wlanMeshNeighborPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("closing", 5),
          ("confirmRx", 3),
          ("established", 4),
          ("idle", 0),
          ("openRx", 2),
          ("openTx", 1))
    )


_WlanMeshNeighborPeerState_Type.__name__ = "Integer32"
_WlanMeshNeighborPeerState_Object = MibTableColumn
wlanMeshNeighborPeerState = _WlanMeshNeighborPeerState_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 5),
    _WlanMeshNeighborPeerState_Type()
)
wlanMeshNeighborPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborPeerState.setStatus("current")
_WlanMeshNeighborCurrentTXRate_Type = Integer32
_WlanMeshNeighborCurrentTXRate_Object = MibTableColumn
wlanMeshNeighborCurrentTXRate = _WlanMeshNeighborCurrentTXRate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 6),
    _WlanMeshNeighborCurrentTXRate_Type()
)
wlanMeshNeighborCurrentTXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborCurrentTXRate.setStatus("current")
_WlanMeshNeighborRxSignalStrength_Type = Integer32
_WlanMeshNeighborRxSignalStrength_Object = MibTableColumn
wlanMeshNeighborRxSignalStrength = _WlanMeshNeighborRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 7),
    _WlanMeshNeighborRxSignalStrength_Type()
)
wlanMeshNeighborRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborRxSignalStrength.setStatus("current")
_WlanMeshNeighborIdleTimer_Type = Integer32
_WlanMeshNeighborIdleTimer_Object = MibTableColumn
wlanMeshNeighborIdleTimer = _WlanMeshNeighborIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 8),
    _WlanMeshNeighborIdleTimer_Type()
)
wlanMeshNeighborIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshNeighborIdleTimer.setUnits("seconds")
_WlanMeshNeighborTxSequenceNo_Type = Integer32
_WlanMeshNeighborTxSequenceNo_Object = MibTableColumn
wlanMeshNeighborTxSequenceNo = _WlanMeshNeighborTxSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 9),
    _WlanMeshNeighborTxSequenceNo_Type()
)
wlanMeshNeighborTxSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborTxSequenceNo.setStatus("current")
_WlanMeshNeighborRxSequenceNo_Type = Integer32
_WlanMeshNeighborRxSequenceNo_Object = MibTableColumn
wlanMeshNeighborRxSequenceNo = _WlanMeshNeighborRxSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 2, 2, 1, 10),
    _WlanMeshNeighborRxSequenceNo_Type()
)
wlanMeshNeighborRxSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNeighborRxSequenceNo.setStatus("current")
_WlanMeshRoute_ObjectIdentity = ObjectIdentity
wlanMeshRoute = _WlanMeshRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3)
)
_WlanMeshRouteTable_Object = MibTable
wlanMeshRouteTable = _WlanMeshRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1)
)
if mibBuilder.loadTexts:
    wlanMeshRouteTable.setStatus("current")
_WlanMeshRouteEntry_Object = MibTableRow
wlanMeshRouteEntry = _WlanMeshRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1)
)
wlanMeshRouteEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
    (0, "BEGEMOT-WIRELESS-MIB", "wlanMeshRouteDestination"),
)
if mibBuilder.loadTexts:
    wlanMeshRouteEntry.setStatus("current")
_WlanMeshRouteDestination_Type = MacAddress
_WlanMeshRouteDestination_Object = MibTableColumn
wlanMeshRouteDestination = _WlanMeshRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 1),
    _WlanMeshRouteDestination_Type()
)
wlanMeshRouteDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanMeshRouteDestination.setStatus("current")
_WlanMeshRouteNextHop_Type = MacAddress
_WlanMeshRouteNextHop_Object = MibTableColumn
wlanMeshRouteNextHop = _WlanMeshRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 2),
    _WlanMeshRouteNextHop_Type()
)
wlanMeshRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshRouteNextHop.setStatus("current")
_WlanMeshRouteHops_Type = Integer32
_WlanMeshRouteHops_Object = MibTableColumn
wlanMeshRouteHops = _WlanMeshRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 3),
    _WlanMeshRouteHops_Type()
)
wlanMeshRouteHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshRouteHops.setStatus("current")
_WlanMeshRouteMetric_Type = Unsigned32
_WlanMeshRouteMetric_Object = MibTableColumn
wlanMeshRouteMetric = _WlanMeshRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 4),
    _WlanMeshRouteMetric_Type()
)
wlanMeshRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshRouteMetric.setStatus("current")
_WlanMeshRouteLifeTime_Type = Unsigned32
_WlanMeshRouteLifeTime_Object = MibTableColumn
wlanMeshRouteLifeTime = _WlanMeshRouteLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 5),
    _WlanMeshRouteLifeTime_Type()
)
wlanMeshRouteLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshRouteLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshRouteLifeTime.setUnits("seconds")
_WlanMeshRouteLastMseq_Type = Unsigned32
_WlanMeshRouteLastMseq_Object = MibTableColumn
wlanMeshRouteLastMseq = _WlanMeshRouteLastMseq_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 6),
    _WlanMeshRouteLastMseq_Type()
)
wlanMeshRouteLastMseq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshRouteLastMseq.setStatus("current")


class _WlanMeshRouteFlags_Type(Bits):
    """Custom type wlanMeshRouteFlags based on Bits"""
    namedValues = NamedValues(
        *(("proxy", 2),
          ("valid", 1))
    )

_WlanMeshRouteFlags_Type.__name__ = "Bits"
_WlanMeshRouteFlags_Object = MibTableColumn
wlanMeshRouteFlags = _WlanMeshRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 7),
    _WlanMeshRouteFlags_Type()
)
wlanMeshRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshRouteFlags.setStatus("current")
_WlanMeshRouteStatus_Type = RowStatus
_WlanMeshRouteStatus_Object = MibTableColumn
wlanMeshRouteStatus = _WlanMeshRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 3, 1, 1, 8),
    _WlanMeshRouteStatus_Type()
)
wlanMeshRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMeshRouteStatus.setStatus("current")
_WlanMeshStatistics_ObjectIdentity = ObjectIdentity
wlanMeshStatistics = _WlanMeshStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4)
)
_WlanMeshStatsTable_Object = MibTable
wlanMeshStatsTable = _WlanMeshStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1)
)
if mibBuilder.loadTexts:
    wlanMeshStatsTable.setStatus("current")
_WlanMeshStatsEntry_Object = MibTableRow
wlanMeshStatsEntry = _WlanMeshStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1)
)
wlanMeshStatsEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanMeshStatsEntry.setStatus("current")
_WlanMeshDroppedBadSta_Type = Counter32
_WlanMeshDroppedBadSta_Object = MibTableColumn
wlanMeshDroppedBadSta = _WlanMeshDroppedBadSta_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 1),
    _WlanMeshDroppedBadSta_Type()
)
wlanMeshDroppedBadSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshDroppedBadSta.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshDroppedBadSta.setUnits("frames")
_WlanMeshDroppedNoLink_Type = Counter32
_WlanMeshDroppedNoLink_Object = MibTableColumn
wlanMeshDroppedNoLink = _WlanMeshDroppedNoLink_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 2),
    _WlanMeshDroppedNoLink_Type()
)
wlanMeshDroppedNoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshDroppedNoLink.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshDroppedNoLink.setUnits("frames")
_WlanMeshNoFwdTtl_Type = Counter32
_WlanMeshNoFwdTtl_Object = MibTableColumn
wlanMeshNoFwdTtl = _WlanMeshNoFwdTtl_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 3),
    _WlanMeshNoFwdTtl_Type()
)
wlanMeshNoFwdTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNoFwdTtl.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshNoFwdTtl.setUnits("frames")
_WlanMeshNoFwdBuf_Type = Counter32
_WlanMeshNoFwdBuf_Object = MibTableColumn
wlanMeshNoFwdBuf = _WlanMeshNoFwdBuf_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 4),
    _WlanMeshNoFwdBuf_Type()
)
wlanMeshNoFwdBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNoFwdBuf.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshNoFwdBuf.setUnits("frames")
_WlanMeshNoFwdTooShort_Type = Counter32
_WlanMeshNoFwdTooShort_Object = MibTableColumn
wlanMeshNoFwdTooShort = _WlanMeshNoFwdTooShort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 5),
    _WlanMeshNoFwdTooShort_Type()
)
wlanMeshNoFwdTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNoFwdTooShort.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshNoFwdTooShort.setUnits("frames")
_WlanMeshNoFwdDisabled_Type = Counter32
_WlanMeshNoFwdDisabled_Object = MibTableColumn
wlanMeshNoFwdDisabled = _WlanMeshNoFwdDisabled_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 6),
    _WlanMeshNoFwdDisabled_Type()
)
wlanMeshNoFwdDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNoFwdDisabled.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshNoFwdDisabled.setUnits("frames")
_WlanMeshNoFwdPathUnknown_Type = Counter32
_WlanMeshNoFwdPathUnknown_Object = MibTableColumn
wlanMeshNoFwdPathUnknown = _WlanMeshNoFwdPathUnknown_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 7),
    _WlanMeshNoFwdPathUnknown_Type()
)
wlanMeshNoFwdPathUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshNoFwdPathUnknown.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshNoFwdPathUnknown.setUnits("frames")
_WlanMeshDroppedBadAE_Type = Counter32
_WlanMeshDroppedBadAE_Object = MibTableColumn
wlanMeshDroppedBadAE = _WlanMeshDroppedBadAE_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 8),
    _WlanMeshDroppedBadAE_Type()
)
wlanMeshDroppedBadAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshDroppedBadAE.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshDroppedBadAE.setUnits("frames")
_WlanMeshRouteAddFailed_Type = Counter32
_WlanMeshRouteAddFailed_Object = MibTableColumn
wlanMeshRouteAddFailed = _WlanMeshRouteAddFailed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 9),
    _WlanMeshRouteAddFailed_Type()
)
wlanMeshRouteAddFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshRouteAddFailed.setStatus("current")
_WlanMeshDroppedNoProxy_Type = Counter32
_WlanMeshDroppedNoProxy_Object = MibTableColumn
wlanMeshDroppedNoProxy = _WlanMeshDroppedNoProxy_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 10),
    _WlanMeshDroppedNoProxy_Type()
)
wlanMeshDroppedNoProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshDroppedNoProxy.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshDroppedNoProxy.setUnits("frames")
_WlanMeshDroppedMisaligned_Type = Counter32
_WlanMeshDroppedMisaligned_Object = MibTableColumn
wlanMeshDroppedMisaligned = _WlanMeshDroppedMisaligned_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 4, 1, 1, 11),
    _WlanMeshDroppedMisaligned_Type()
)
wlanMeshDroppedMisaligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshDroppedMisaligned.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshDroppedMisaligned.setUnits("frames")
_WlanMeshRouteProtocols_ObjectIdentity = ObjectIdentity
wlanMeshRouteProtocols = _WlanMeshRouteProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5)
)
_WlanMeshProtoHWMP_ObjectIdentity = ObjectIdentity
wlanMeshProtoHWMP = _WlanMeshProtoHWMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1)
)
_WlanMeshHWMPConfig_ObjectIdentity = ObjectIdentity
wlanMeshHWMPConfig = _WlanMeshHWMPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1)
)


class _WlanHWMPRouteInactiveTimeout_Type(Integer32):
    """Custom type wlanHWMPRouteInactiveTimeout based on Integer32"""
    defaultValue = 5000


_WlanHWMPRouteInactiveTimeout_Object = MibScalar
wlanHWMPRouteInactiveTimeout = _WlanHWMPRouteInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1, 1),
    _WlanHWMPRouteInactiveTimeout_Type()
)
wlanHWMPRouteInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPRouteInactiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wlanHWMPRouteInactiveTimeout.setUnits("milliseconds")


class _WlanHWMPRootAnnounceInterval_Type(Integer32):
    """Custom type wlanHWMPRootAnnounceInterval based on Integer32"""
    defaultValue = 1000


_WlanHWMPRootAnnounceInterval_Object = MibScalar
wlanHWMPRootAnnounceInterval = _WlanHWMPRootAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1, 2),
    _WlanHWMPRootAnnounceInterval_Type()
)
wlanHWMPRootAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPRootAnnounceInterval.setStatus("current")
if mibBuilder.loadTexts:
    wlanHWMPRootAnnounceInterval.setUnits("milliseconds")


class _WlanHWMPRootInterval_Type(Integer32):
    """Custom type wlanHWMPRootInterval based on Integer32"""
    defaultValue = 2000


_WlanHWMPRootInterval_Object = MibScalar
wlanHWMPRootInterval = _WlanHWMPRootInterval_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1, 3),
    _WlanHWMPRootInterval_Type()
)
wlanHWMPRootInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPRootInterval.setStatus("current")
if mibBuilder.loadTexts:
    wlanHWMPRootInterval.setUnits("milliseconds")


class _WlanHWMPRootTimeout_Type(Integer32):
    """Custom type wlanHWMPRootTimeout based on Integer32"""
    defaultValue = 5000


_WlanHWMPRootTimeout_Object = MibScalar
wlanHWMPRootTimeout = _WlanHWMPRootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1, 4),
    _WlanHWMPRootTimeout_Type()
)
wlanHWMPRootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPRootTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wlanHWMPRootTimeout.setUnits("milliseconds")


class _WlanHWMPPathLifetime_Type(Integer32):
    """Custom type wlanHWMPPathLifetime based on Integer32"""
    defaultValue = 500


_WlanHWMPPathLifetime_Object = MibScalar
wlanHWMPPathLifetime = _WlanHWMPPathLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1, 5),
    _WlanHWMPPathLifetime_Type()
)
wlanHWMPPathLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPPathLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wlanHWMPPathLifetime.setUnits("milliseconds")


class _WlanHWMPReplyForwardBit_Type(Integer32):
    """Custom type wlanHWMPReplyForwardBit based on Integer32"""
    defaultValue = 1


_WlanHWMPReplyForwardBit_Object = MibScalar
wlanHWMPReplyForwardBit = _WlanHWMPReplyForwardBit_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1, 6),
    _WlanHWMPReplyForwardBit_Type()
)
wlanHWMPReplyForwardBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPReplyForwardBit.setStatus("current")


class _WlanHWMPTargetOnlyBit_Type(Integer32):
    """Custom type wlanHWMPTargetOnlyBit based on Integer32"""
    defaultValue = 0


_WlanHWMPTargetOnlyBit_Object = MibScalar
wlanHWMPTargetOnlyBit = _WlanHWMPTargetOnlyBit_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 1, 7),
    _WlanHWMPTargetOnlyBit_Type()
)
wlanHWMPTargetOnlyBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPTargetOnlyBit.setStatus("current")
_WlanMeshHWMPInterface_ObjectIdentity = ObjectIdentity
wlanMeshHWMPInterface = _WlanMeshHWMPInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 2)
)
_WlanHWMPInterfaceTable_Object = MibTable
wlanHWMPInterfaceTable = _WlanHWMPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wlanHWMPInterfaceTable.setStatus("current")
_WlanHWMPInterfaceEntry_Object = MibTableRow
wlanHWMPInterfaceEntry = _WlanHWMPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 2, 1, 1)
)
wlanHWMPInterfaceEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanHWMPInterfaceEntry.setStatus("current")


class _WlanHWMPRootMode_Type(Integer32):
    """Custom type wlanHWMPRootMode based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("normal", 2),
          ("proactive", 3),
          ("rann", 4))
    )


_WlanHWMPRootMode_Type.__name__ = "Integer32"
_WlanHWMPRootMode_Object = MibTableColumn
wlanHWMPRootMode = _WlanHWMPRootMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 2, 1, 1, 1),
    _WlanHWMPRootMode_Type()
)
wlanHWMPRootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPRootMode.setStatus("current")


class _WlanHWMPMaxHops_Type(Integer32):
    """Custom type wlanHWMPMaxHops based on Integer32"""
    defaultValue = 31


_WlanHWMPMaxHops_Object = MibTableColumn
wlanHWMPMaxHops = _WlanHWMPMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 2, 1, 1, 2),
    _WlanHWMPMaxHops_Type()
)
wlanHWMPMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanHWMPMaxHops.setStatus("current")
_WlanMeshHWMPStatistics_ObjectIdentity = ObjectIdentity
wlanMeshHWMPStatistics = _WlanMeshHWMPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 3)
)
_WlanMeshHWMPStatsTable_Object = MibTable
wlanMeshHWMPStatsTable = _WlanMeshHWMPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wlanMeshHWMPStatsTable.setStatus("current")
_WlanMeshHWMPStatsEntry_Object = MibTableRow
wlanMeshHWMPStatsEntry = _WlanMeshHWMPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 3, 1, 1)
)
wlanMeshHWMPStatsEntry.setIndexNames(
    (0, "BEGEMOT-WIRELESS-MIB", "wlanIfaceName"),
)
if mibBuilder.loadTexts:
    wlanMeshHWMPStatsEntry.setStatus("current")
_WlanMeshHWMPWrongSeqNo_Type = Counter32
_WlanMeshHWMPWrongSeqNo_Object = MibTableColumn
wlanMeshHWMPWrongSeqNo = _WlanMeshHWMPWrongSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 3, 1, 1, 1),
    _WlanMeshHWMPWrongSeqNo_Type()
)
wlanMeshHWMPWrongSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshHWMPWrongSeqNo.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshHWMPWrongSeqNo.setUnits("frames")
_WlanMeshHWMPTxRootPREQ_Type = Counter32
_WlanMeshHWMPTxRootPREQ_Object = MibTableColumn
wlanMeshHWMPTxRootPREQ = _WlanMeshHWMPTxRootPREQ_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 3, 1, 1, 2),
    _WlanMeshHWMPTxRootPREQ_Type()
)
wlanMeshHWMPTxRootPREQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshHWMPTxRootPREQ.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshHWMPTxRootPREQ.setUnits("frames")
_WlanMeshHWMPTxRootRANN_Type = Counter32
_WlanMeshHWMPTxRootRANN_Object = MibTableColumn
wlanMeshHWMPTxRootRANN = _WlanMeshHWMPTxRootRANN_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 3, 1, 1, 3),
    _WlanMeshHWMPTxRootRANN_Type()
)
wlanMeshHWMPTxRootRANN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshHWMPTxRootRANN.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshHWMPTxRootRANN.setUnits("frames")
_WlanMeshHWMPProxy_Type = Counter32
_WlanMeshHWMPProxy_Object = MibTableColumn
wlanMeshHWMPProxy = _WlanMeshHWMPProxy_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 210, 6, 5, 1, 3, 1, 1, 4),
    _WlanMeshHWMPProxy_Type()
)
wlanMeshHWMPProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMeshHWMPProxy.setStatus("current")
if mibBuilder.loadTexts:
    wlanMeshHWMPProxy.setUnits("frames")
wlanInterfaceEntry.registerAugmentions(
    ("BEGEMOT-WIRELESS-MIB",
     "wlanIfParentEntry")
)
wlanIfParentEntry.setIndexNames(*wlanInterfaceEntry.getIndexNames())
wlanInterfaceEntry.registerAugmentions(
    ("BEGEMOT-WIRELESS-MIB",
     "wlanIfaceConfigEntry")
)
wlanIfaceConfigEntry.setIndexNames(*wlanInterfaceEntry.getIndexNames())
wlanInterfaceEntry.registerAugmentions(
    ("BEGEMOT-WIRELESS-MIB",
     "wlanIfaceStatisticsEntry")
)
wlanIfaceStatisticsEntry.setIndexNames(*wlanInterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-WIRELESS-MIB",
    **{"WlanMgmtReasonCode": WlanMgmtReasonCode,
       "WlanMgmtMeshReasonCode": WlanMgmtMeshReasonCode,
       "WlanMgmtStatusCode": WlanMgmtStatusCode,
       "WlanRegDomainCode": WlanRegDomainCode,
       "WlanIfaceDot11nPduType": WlanIfaceDot11nPduType,
       "WlanPeerCapabilityFlags": WlanPeerCapabilityFlags,
       "WlanIfPhyMode": WlanIfPhyMode,
       "begemotWlan": begemotWlan,
       "begemotWlanNotifications": begemotWlanNotifications,
       "begemotWlanInterface": begemotWlanInterface,
       "wlanInterfaceTable": wlanInterfaceTable,
       "wlanInterfaceEntry": wlanInterfaceEntry,
       "wlanIfaceIndex": wlanIfaceIndex,
       "wlanIfaceName": wlanIfaceName,
       "wlanParentIfName": wlanParentIfName,
       "wlanIfaceOperatingMode": wlanIfaceOperatingMode,
       "wlanIfaceFlags": wlanIfaceFlags,
       "wlanIfaceBssid": wlanIfaceBssid,
       "wlanIfaceLocalAddress": wlanIfaceLocalAddress,
       "wlanIfaceStatus": wlanIfaceStatus,
       "wlanIfaceState": wlanIfaceState,
       "wlanIfParentTable": wlanIfParentTable,
       "wlanIfParentEntry": wlanIfParentEntry,
       "wlanIfParentDriverCapabilities": wlanIfParentDriverCapabilities,
       "wlanIfParentCryptoCapabilities": wlanIfParentCryptoCapabilities,
       "wlanIfParentHTCapabilities": wlanIfParentHTCapabilities,
       "wlanIfaceConfigTable": wlanIfaceConfigTable,
       "wlanIfaceConfigEntry": wlanIfaceConfigEntry,
       "wlanIfacePacketBurst": wlanIfacePacketBurst,
       "wlanIfaceCountryCode": wlanIfaceCountryCode,
       "wlanIfaceRegDomain": wlanIfaceRegDomain,
       "wlanIfaceDesiredSsid": wlanIfaceDesiredSsid,
       "wlanIfaceDesiredChannel": wlanIfaceDesiredChannel,
       "wlanIfaceDynamicFreqSelection": wlanIfaceDynamicFreqSelection,
       "wlanIfaceFastFrames": wlanIfaceFastFrames,
       "wlanIfaceDturbo": wlanIfaceDturbo,
       "wlanIfaceTxPower": wlanIfaceTxPower,
       "wlanIfaceFragmentThreshold": wlanIfaceFragmentThreshold,
       "wlanIfaceRTSThreshold": wlanIfaceRTSThreshold,
       "wlanIfaceWlanPrivacySubscribe": wlanIfaceWlanPrivacySubscribe,
       "wlanIfaceBgScan": wlanIfaceBgScan,
       "wlanIfaceBgScanIdle": wlanIfaceBgScanIdle,
       "wlanIfaceBgScanInterval": wlanIfaceBgScanInterval,
       "wlanIfaceBeaconMissedThreshold": wlanIfaceBeaconMissedThreshold,
       "wlanIfaceDesiredBssid": wlanIfaceDesiredBssid,
       "wlanIfaceRoamingMode": wlanIfaceRoamingMode,
       "wlanIfaceDot11d": wlanIfaceDot11d,
       "wlanIfaceDot11h": wlanIfaceDot11h,
       "wlanIfaceDynamicWds": wlanIfaceDynamicWds,
       "wlanIfacePowerSave": wlanIfacePowerSave,
       "wlanIfaceApBridge": wlanIfaceApBridge,
       "wlanIfaceBeaconInterval": wlanIfaceBeaconInterval,
       "wlanIfaceDtimPeriod": wlanIfaceDtimPeriod,
       "wlanIfaceHideSsid": wlanIfaceHideSsid,
       "wlanIfaceInactivityProccess": wlanIfaceInactivityProccess,
       "wlanIfaceDot11gProtMode": wlanIfaceDot11gProtMode,
       "wlanIfaceDot11gPureMode": wlanIfaceDot11gPureMode,
       "wlanIfaceDot11nPureMode": wlanIfaceDot11nPureMode,
       "wlanIfaceDot11nAmpdu": wlanIfaceDot11nAmpdu,
       "wlanIfaceDot11nAmpduDensity": wlanIfaceDot11nAmpduDensity,
       "wlanIfaceDot11nAmpduLimit": wlanIfaceDot11nAmpduLimit,
       "wlanIfaceDot11nAmsdu": wlanIfaceDot11nAmsdu,
       "wlanIfaceDot11nAmsduLimit": wlanIfaceDot11nAmsduLimit,
       "wlanIfaceDot11nHighThroughput": wlanIfaceDot11nHighThroughput,
       "wlanIfaceDot11nHTCompatible": wlanIfaceDot11nHTCompatible,
       "wlanIfaceDot11nHTProtMode": wlanIfaceDot11nHTProtMode,
       "wlanIfaceDot11nRIFS": wlanIfaceDot11nRIFS,
       "wlanIfaceDot11nShortGI": wlanIfaceDot11nShortGI,
       "wlanIfaceDot11nSMPSMode": wlanIfaceDot11nSMPSMode,
       "wlanIfaceTdmaSlot": wlanIfaceTdmaSlot,
       "wlanIfaceTdmaSlotCount": wlanIfaceTdmaSlotCount,
       "wlanIfaceTdmaSlotLength": wlanIfaceTdmaSlotLength,
       "wlanIfaceTdmaBeaconInterval": wlanIfaceTdmaBeaconInterval,
       "wlanIfacePeerTable": wlanIfacePeerTable,
       "wlanIfacePeerEntry": wlanIfacePeerEntry,
       "wlanIfacePeerAddress": wlanIfacePeerAddress,
       "wlanIfacePeerAssociationId": wlanIfacePeerAssociationId,
       "wlanIfacePeerVlanTag": wlanIfacePeerVlanTag,
       "wlanIfacePeerFrequency": wlanIfacePeerFrequency,
       "wlanIfacePeerCurrentTXRate": wlanIfacePeerCurrentTXRate,
       "wlanIfacePeerRxSignalStrength": wlanIfacePeerRxSignalStrength,
       "wlanIfacePeerIdleTimer": wlanIfacePeerIdleTimer,
       "wlanIfacePeerTxSequenceNo": wlanIfacePeerTxSequenceNo,
       "wlanIfacePeerRxSequenceNo": wlanIfacePeerRxSequenceNo,
       "wlanIfacePeerTxPower": wlanIfacePeerTxPower,
       "wlanIfacePeerCapabilities": wlanIfacePeerCapabilities,
       "wlanIfacePeerFlags": wlanIfacePeerFlags,
       "wlanIfaceChannelTable": wlanIfaceChannelTable,
       "wlanIfaceChannelEntry": wlanIfaceChannelEntry,
       "wlanIfaceChannelId": wlanIfaceChannelId,
       "wlanIfaceChannelIeeeId": wlanIfaceChannelIeeeId,
       "wlanIfaceChannelType": wlanIfaceChannelType,
       "wlanIfaceChannelFlags": wlanIfaceChannelFlags,
       "wlanIfaceChannelFrequency": wlanIfaceChannelFrequency,
       "wlanIfaceChannelMaxRegPower": wlanIfaceChannelMaxRegPower,
       "wlanIfaceChannelMaxTxPower": wlanIfaceChannelMaxTxPower,
       "wlanIfaceChannelMinTxPower": wlanIfaceChannelMinTxPower,
       "wlanIfaceChannelState": wlanIfaceChannelState,
       "wlanIfaceChannelHTExtension": wlanIfaceChannelHTExtension,
       "wlanIfaceChannelMaxAntennaGain": wlanIfaceChannelMaxAntennaGain,
       "wlanIfRoamParamsTable": wlanIfRoamParamsTable,
       "wlanIfRoamParamsEntry": wlanIfRoamParamsEntry,
       "wlanIfRoamPhyMode": wlanIfRoamPhyMode,
       "wlanIfRoamRxSignalStrength": wlanIfRoamRxSignalStrength,
       "wlanIfRoamTxRateThreshold": wlanIfRoamTxRateThreshold,
       "wlanIfTxParamsTable": wlanIfTxParamsTable,
       "wlanIfTxParamsEntry": wlanIfTxParamsEntry,
       "wlanIfTxPhyMode": wlanIfTxPhyMode,
       "wlanIfTxUnicastRate": wlanIfTxUnicastRate,
       "wlanIfTxMcastRate": wlanIfTxMcastRate,
       "wlanIfTxMgmtRate": wlanIfTxMgmtRate,
       "wlanIfTxMaxRetryCount": wlanIfTxMaxRetryCount,
       "begemotWlanScanning": begemotWlanScanning,
       "wlanScanConfigTable": wlanScanConfigTable,
       "wlanScanConfigEntry": wlanScanConfigEntry,
       "wlanScanFlags": wlanScanFlags,
       "wlanScanDuration": wlanScanDuration,
       "wlanScanMinChannelDwellTime": wlanScanMinChannelDwellTime,
       "wlanScanMaxChannelDwellTime": wlanScanMaxChannelDwellTime,
       "wlanScanConfigStatus": wlanScanConfigStatus,
       "wlanScanResultsTable": wlanScanResultsTable,
       "wlanScanResultsEntry": wlanScanResultsEntry,
       "wlanScanResultID": wlanScanResultID,
       "wlanScanResultBssid": wlanScanResultBssid,
       "wlanScanResultChannel": wlanScanResultChannel,
       "wlanScanResultRate": wlanScanResultRate,
       "wlanScanResultNoise": wlanScanResultNoise,
       "wlanScanResultBeaconInterval": wlanScanResultBeaconInterval,
       "wlanScanResultCapabilities": wlanScanResultCapabilities,
       "begemotWlanStatistics": begemotWlanStatistics,
       "wlanIfaceStatisticsTable": wlanIfaceStatisticsTable,
       "wlanIfaceStatisticsEntry": wlanIfaceStatisticsEntry,
       "wlanStatsRxBadVersion": wlanStatsRxBadVersion,
       "wlanStatsRxTooShort": wlanStatsRxTooShort,
       "wlanStatsRxWrongBssid": wlanStatsRxWrongBssid,
       "wlanStatsRxDiscardedDups": wlanStatsRxDiscardedDups,
       "wlanStatsRxWrongDir": wlanStatsRxWrongDir,
       "wlanStatsRxDiscardMcastEcho": wlanStatsRxDiscardMcastEcho,
       "wlanStatsRxDiscardNoAssoc": wlanStatsRxDiscardNoAssoc,
       "wlanStatsRxWepNoPrivacy": wlanStatsRxWepNoPrivacy,
       "wlanStatsRxWepUnencrypted": wlanStatsRxWepUnencrypted,
       "wlanStatsRxWepFailed": wlanStatsRxWepFailed,
       "wlanStatsRxDecapsulationFailed": wlanStatsRxDecapsulationFailed,
       "wlanStatsRxDiscardMgmt": wlanStatsRxDiscardMgmt,
       "wlanStatsRxControl": wlanStatsRxControl,
       "wlanStatsRxBeacon": wlanStatsRxBeacon,
       "wlanStatsRxRateSetTooBig": wlanStatsRxRateSetTooBig,
       "wlanStatsRxElemMissing": wlanStatsRxElemMissing,
       "wlanStatsRxElemTooBig": wlanStatsRxElemTooBig,
       "wlanStatsRxElemTooSmall": wlanStatsRxElemTooSmall,
       "wlanStatsRxElemUnknown": wlanStatsRxElemUnknown,
       "wlanStatsRxChannelMismatch": wlanStatsRxChannelMismatch,
       "wlanStatsRxDropped": wlanStatsRxDropped,
       "wlanStatsRxSsidMismatch": wlanStatsRxSsidMismatch,
       "wlanStatsRxAuthNotSupported": wlanStatsRxAuthNotSupported,
       "wlanStatsRxAuthFailed": wlanStatsRxAuthFailed,
       "wlanStatsRxAuthCM": wlanStatsRxAuthCM,
       "wlanStatsRxAssocWrongBssid": wlanStatsRxAssocWrongBssid,
       "wlanStatsRxAssocNoAuth": wlanStatsRxAssocNoAuth,
       "wlanStatsRxAssocCapMismatch": wlanStatsRxAssocCapMismatch,
       "wlanStatsRxAssocNoRateMatch": wlanStatsRxAssocNoRateMatch,
       "wlanStatsRxBadWpaIE": wlanStatsRxBadWpaIE,
       "wlanStatsRxDeauthenticate": wlanStatsRxDeauthenticate,
       "wlanStatsRxDisassociate": wlanStatsRxDisassociate,
       "wlanStatsRxUnknownSubtype": wlanStatsRxUnknownSubtype,
       "wlanStatsRxFailedNoBuf": wlanStatsRxFailedNoBuf,
       "wlanStatsRxBadAuthRequest": wlanStatsRxBadAuthRequest,
       "wlanStatsRxUnAuthorized": wlanStatsRxUnAuthorized,
       "wlanStatsRxBadKeyId": wlanStatsRxBadKeyId,
       "wlanStatsRxCCMPSeqViolation": wlanStatsRxCCMPSeqViolation,
       "wlanStatsRxCCMPBadFormat": wlanStatsRxCCMPBadFormat,
       "wlanStatsRxCCMPFailedMIC": wlanStatsRxCCMPFailedMIC,
       "wlanStatsRxTKIPSeqViolation": wlanStatsRxTKIPSeqViolation,
       "wlanStatsRxTKIPBadFormat": wlanStatsRxTKIPBadFormat,
       "wlanStatsRxTKIPFailedMIC": wlanStatsRxTKIPFailedMIC,
       "wlanStatsRxTKIPFailedICV": wlanStatsRxTKIPFailedICV,
       "wlanStatsRxDiscardACL": wlanStatsRxDiscardACL,
       "wlanStatsTxFailedNoBuf": wlanStatsTxFailedNoBuf,
       "wlanStatsTxFailedNoNode": wlanStatsTxFailedNoNode,
       "wlanStatsTxUnknownMgmt": wlanStatsTxUnknownMgmt,
       "wlanStatsTxBadCipher": wlanStatsTxBadCipher,
       "wlanStatsTxNoDefKey": wlanStatsTxNoDefKey,
       "wlanStatsTxFragmented": wlanStatsTxFragmented,
       "wlanStatsTxFragmentsCreated": wlanStatsTxFragmentsCreated,
       "wlanStatsActiveScans": wlanStatsActiveScans,
       "wlanStatsPassiveScans": wlanStatsPassiveScans,
       "wlanStatsTimeoutInactivity": wlanStatsTimeoutInactivity,
       "wlanStatsCryptoNoMem": wlanStatsCryptoNoMem,
       "wlanStatsSwCryptoTKIP": wlanStatsSwCryptoTKIP,
       "wlanStatsSwCryptoTKIPEnMIC": wlanStatsSwCryptoTKIPEnMIC,
       "wlanStatsSwCryptoTKIPDeMIC": wlanStatsSwCryptoTKIPDeMIC,
       "wlanStatsCryptoTKIPCM": wlanStatsCryptoTKIPCM,
       "wlanStatsSwCryptoCCMP": wlanStatsSwCryptoCCMP,
       "wlanStatsSwCryptoWEP": wlanStatsSwCryptoWEP,
       "wlanStatsCryptoCipherKeyRejected": wlanStatsCryptoCipherKeyRejected,
       "wlanStatsCryptoNoKey": wlanStatsCryptoNoKey,
       "wlanStatsCryptoDeleteKeyFailed": wlanStatsCryptoDeleteKeyFailed,
       "wlanStatsCryptoUnknownCipher": wlanStatsCryptoUnknownCipher,
       "wlanStatsCryptoAttachFailed": wlanStatsCryptoAttachFailed,
       "wlanStatsCryptoKeyFailed": wlanStatsCryptoKeyFailed,
       "wlanStatsCryptoEnMICFailed": wlanStatsCryptoEnMICFailed,
       "wlanStatsIBSSCapMismatch": wlanStatsIBSSCapMismatch,
       "wlanStatsUnassocStaPSPoll": wlanStatsUnassocStaPSPoll,
       "wlanStatsBadAidPSPoll": wlanStatsBadAidPSPoll,
       "wlanStatsEmptyPSPoll": wlanStatsEmptyPSPoll,
       "wlanStatsRxFFBadHdr": wlanStatsRxFFBadHdr,
       "wlanStatsRxFFTooShort": wlanStatsRxFFTooShort,
       "wlanStatsRxFFSplitError": wlanStatsRxFFSplitError,
       "wlanStatsRxFFDecap": wlanStatsRxFFDecap,
       "wlanStatsTxFFEncap": wlanStatsTxFFEncap,
       "wlanStatsRxBadBintval": wlanStatsRxBadBintval,
       "wlanStatsRxDemicFailed": wlanStatsRxDemicFailed,
       "wlanStatsRxDefragFailed": wlanStatsRxDefragFailed,
       "wlanStatsRxMgmt": wlanStatsRxMgmt,
       "wlanStatsRxActionMgmt": wlanStatsRxActionMgmt,
       "wlanStatsRxAMSDUTooShort": wlanStatsRxAMSDUTooShort,
       "wlanStatsRxAMSDUSplitError": wlanStatsRxAMSDUSplitError,
       "wlanStatsRxAMSDUDecap": wlanStatsRxAMSDUDecap,
       "wlanStatsTxAMSDUEncap": wlanStatsTxAMSDUEncap,
       "wlanStatsAMPDUBadBAR": wlanStatsAMPDUBadBAR,
       "wlanStatsAMPDUOowBar": wlanStatsAMPDUOowBar,
       "wlanStatsAMPDUMovedBAR": wlanStatsAMPDUMovedBAR,
       "wlanStatsAMPDURxBAR": wlanStatsAMPDURxBAR,
       "wlanStatsAMPDURxOor": wlanStatsAMPDURxOor,
       "wlanStatsAMPDURxCopied": wlanStatsAMPDURxCopied,
       "wlanStatsAMPDURxDropped": wlanStatsAMPDURxDropped,
       "wlanStatsTxDiscardBadState": wlanStatsTxDiscardBadState,
       "wlanStatsTxFailedNoAssoc": wlanStatsTxFailedNoAssoc,
       "wlanStatsTxClassifyFailed": wlanStatsTxClassifyFailed,
       "wlanStatsDwdsMcastDiscard": wlanStatsDwdsMcastDiscard,
       "wlanStatsHTAssocRejectNoHT": wlanStatsHTAssocRejectNoHT,
       "wlanStatsHTAssocDowngrade": wlanStatsHTAssocDowngrade,
       "wlanStatsHTAssocRateMismatch": wlanStatsHTAssocRateMismatch,
       "wlanStatsAMPDURxAge": wlanStatsAMPDURxAge,
       "wlanStatsAMPDUMoved": wlanStatsAMPDUMoved,
       "wlanStatsADDBADisabledReject": wlanStatsADDBADisabledReject,
       "wlanStatsADDBANoRequest": wlanStatsADDBANoRequest,
       "wlanStatsADDBABadToken": wlanStatsADDBABadToken,
       "wlanStatsADDBABadPolicy": wlanStatsADDBABadPolicy,
       "wlanStatsAMPDUStopped": wlanStatsAMPDUStopped,
       "wlanStatsAMPDUStopFailed": wlanStatsAMPDUStopFailed,
       "wlanStatsAMPDURxReorder": wlanStatsAMPDURxReorder,
       "wlanStatsScansBackground": wlanStatsScansBackground,
       "wlanLastDeauthReason": wlanLastDeauthReason,
       "wlanLastDissasocReason": wlanLastDissasocReason,
       "wlanLastAuthFailReason": wlanLastAuthFailReason,
       "wlanStatsBeaconMissedEvents": wlanStatsBeaconMissedEvents,
       "wlanStatsRxDiscardBadStates": wlanStatsRxDiscardBadStates,
       "wlanStatsFFFlushed": wlanStatsFFFlushed,
       "wlanStatsTxControlFrames": wlanStatsTxControlFrames,
       "wlanStatsAMPDURexmt": wlanStatsAMPDURexmt,
       "wlanStatsAMPDURexmtFailed": wlanStatsAMPDURexmtFailed,
       "wlanStatsReset": wlanStatsReset,
       "begemotWlanWep": begemotWlanWep,
       "wlanWepInterfaceTable": wlanWepInterfaceTable,
       "wlanWepInterfaceEntry": wlanWepInterfaceEntry,
       "wlanWepMode": wlanWepMode,
       "wlanWepDefTxKey": wlanWepDefTxKey,
       "wlanWepKeyTable": wlanWepKeyTable,
       "wlanWepKeyEntry": wlanWepKeyEntry,
       "wlanWepKeyID": wlanWepKeyID,
       "wlanWepKeyLength": wlanWepKeyLength,
       "wlanWepKeySet": wlanWepKeySet,
       "wlanWepKeyHash": wlanWepKeyHash,
       "wlanWepKeyStatus": wlanWepKeyStatus,
       "begemotWlanMACAccessControl": begemotWlanMACAccessControl,
       "wlanMACAccessControlTable": wlanMACAccessControlTable,
       "wlanMACAccessControlEntry": wlanMACAccessControlEntry,
       "wlanMACAccessControlPolicy": wlanMACAccessControlPolicy,
       "wlanMACAccessControlNacl": wlanMACAccessControlNacl,
       "wlanMACAccessControlFlush": wlanMACAccessControlFlush,
       "wlanMACAccessControlMACTable": wlanMACAccessControlMACTable,
       "wlanMACAccessControlMACEntry": wlanMACAccessControlMACEntry,
       "wlanMACAccessControlMAC": wlanMACAccessControlMAC,
       "wlanMACAccessControlMACStatus": wlanMACAccessControlMACStatus,
       "begemotWlanMeshRouting": begemotWlanMeshRouting,
       "wlanMeshRoutingConfig": wlanMeshRoutingConfig,
       "wlanMeshMaxRetries": wlanMeshMaxRetries,
       "wlanMeshConfirmTimeout": wlanMeshConfirmTimeout,
       "wlanMeshHoldingTimeout": wlanMeshHoldingTimeout,
       "wlanMeshRetryTimeout": wlanMeshRetryTimeout,
       "wlanMeshInterface": wlanMeshInterface,
       "wlanMeshInterfaceTable": wlanMeshInterfaceTable,
       "wlanMeshInterfaceEntry": wlanMeshInterfaceEntry,
       "wlanMeshId": wlanMeshId,
       "wlanMeshTTL": wlanMeshTTL,
       "wlanMeshPeeringEnabled": wlanMeshPeeringEnabled,
       "wlanMeshForwardingEnabled": wlanMeshForwardingEnabled,
       "wlanMeshMetric": wlanMeshMetric,
       "wlanMeshPath": wlanMeshPath,
       "wlanMeshRoutesFlush": wlanMeshRoutesFlush,
       "wlanMeshNeighborTable": wlanMeshNeighborTable,
       "wlanMeshNeighborEntry": wlanMeshNeighborEntry,
       "wlanMeshNeighborAddress": wlanMeshNeighborAddress,
       "wlanMeshNeighborFrequency": wlanMeshNeighborFrequency,
       "wlanMeshNeighborLocalId": wlanMeshNeighborLocalId,
       "wlanMeshNeighborPeerId": wlanMeshNeighborPeerId,
       "wlanMeshNeighborPeerState": wlanMeshNeighborPeerState,
       "wlanMeshNeighborCurrentTXRate": wlanMeshNeighborCurrentTXRate,
       "wlanMeshNeighborRxSignalStrength": wlanMeshNeighborRxSignalStrength,
       "wlanMeshNeighborIdleTimer": wlanMeshNeighborIdleTimer,
       "wlanMeshNeighborTxSequenceNo": wlanMeshNeighborTxSequenceNo,
       "wlanMeshNeighborRxSequenceNo": wlanMeshNeighborRxSequenceNo,
       "wlanMeshRoute": wlanMeshRoute,
       "wlanMeshRouteTable": wlanMeshRouteTable,
       "wlanMeshRouteEntry": wlanMeshRouteEntry,
       "wlanMeshRouteDestination": wlanMeshRouteDestination,
       "wlanMeshRouteNextHop": wlanMeshRouteNextHop,
       "wlanMeshRouteHops": wlanMeshRouteHops,
       "wlanMeshRouteMetric": wlanMeshRouteMetric,
       "wlanMeshRouteLifeTime": wlanMeshRouteLifeTime,
       "wlanMeshRouteLastMseq": wlanMeshRouteLastMseq,
       "wlanMeshRouteFlags": wlanMeshRouteFlags,
       "wlanMeshRouteStatus": wlanMeshRouteStatus,
       "wlanMeshStatistics": wlanMeshStatistics,
       "wlanMeshStatsTable": wlanMeshStatsTable,
       "wlanMeshStatsEntry": wlanMeshStatsEntry,
       "wlanMeshDroppedBadSta": wlanMeshDroppedBadSta,
       "wlanMeshDroppedNoLink": wlanMeshDroppedNoLink,
       "wlanMeshNoFwdTtl": wlanMeshNoFwdTtl,
       "wlanMeshNoFwdBuf": wlanMeshNoFwdBuf,
       "wlanMeshNoFwdTooShort": wlanMeshNoFwdTooShort,
       "wlanMeshNoFwdDisabled": wlanMeshNoFwdDisabled,
       "wlanMeshNoFwdPathUnknown": wlanMeshNoFwdPathUnknown,
       "wlanMeshDroppedBadAE": wlanMeshDroppedBadAE,
       "wlanMeshRouteAddFailed": wlanMeshRouteAddFailed,
       "wlanMeshDroppedNoProxy": wlanMeshDroppedNoProxy,
       "wlanMeshDroppedMisaligned": wlanMeshDroppedMisaligned,
       "wlanMeshRouteProtocols": wlanMeshRouteProtocols,
       "wlanMeshProtoHWMP": wlanMeshProtoHWMP,
       "wlanMeshHWMPConfig": wlanMeshHWMPConfig,
       "wlanHWMPRouteInactiveTimeout": wlanHWMPRouteInactiveTimeout,
       "wlanHWMPRootAnnounceInterval": wlanHWMPRootAnnounceInterval,
       "wlanHWMPRootInterval": wlanHWMPRootInterval,
       "wlanHWMPRootTimeout": wlanHWMPRootTimeout,
       "wlanHWMPPathLifetime": wlanHWMPPathLifetime,
       "wlanHWMPReplyForwardBit": wlanHWMPReplyForwardBit,
       "wlanHWMPTargetOnlyBit": wlanHWMPTargetOnlyBit,
       "wlanMeshHWMPInterface": wlanMeshHWMPInterface,
       "wlanHWMPInterfaceTable": wlanHWMPInterfaceTable,
       "wlanHWMPInterfaceEntry": wlanHWMPInterfaceEntry,
       "wlanHWMPRootMode": wlanHWMPRootMode,
       "wlanHWMPMaxHops": wlanHWMPMaxHops,
       "wlanMeshHWMPStatistics": wlanMeshHWMPStatistics,
       "wlanMeshHWMPStatsTable": wlanMeshHWMPStatsTable,
       "wlanMeshHWMPStatsEntry": wlanMeshHWMPStatsEntry,
       "wlanMeshHWMPWrongSeqNo": wlanMeshHWMPWrongSeqNo,
       "wlanMeshHWMPTxRootPREQ": wlanMeshHWMPTxRootPREQ,
       "wlanMeshHWMPTxRootRANN": wlanMeshHWMPTxRootRANN,
       "wlanMeshHWMPProxy": wlanMeshHWMPProxy}
)
