# SNMP MIB module (ZHNWIRELESS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNWIRELESS
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:05 2024
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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhnWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46)
)
zhnWireless.setRevisions(
        ("2012-07-11 12:00",
         "2012-06-21 12:00",
         "2012-05-16 12:00",
         "2012-04-18 12:00",
         "2012-01-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WlChannelSelections(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("auto", 14),
          ("channel1", 1),
          ("channel10", 10),
          ("channel11", 11),
          ("channel12", 12),
          ("channel13", 13),
          ("channel2", 2),
          ("channel3", 3),
          ("channel4", 4),
          ("channel5", 5),
          ("channel6", 6),
          ("channel7", 7),
          ("channel8", 8),
          ("channel9", 9))
    )



class WlMimoNEwcModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disabled", 2))
    )



class WlMimoNRates(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("rate104M", 12),
          ("rate117M", 13),
          ("rate130M", 14),
          ("rate13M", 4),
          ("rate19Dot5M", 5),
          ("rate26M", 6),
          ("rate39M", 7),
          ("rate52M", 8),
          ("rate58Dot5M", 9),
          ("rate65M", 10),
          ("rate6Dot5M", 3),
          ("rate78M", 11),
          ("use54g", 2))
    )



class WlMimoNProtectionModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 1))
    )



class Wl54gMulticastRates(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("auto", 13),
          ("rate11M", 6),
          ("rate12M", 7),
          ("rate18M", 8),
          ("rate1M", 1),
          ("rate24M", 9),
          ("rate2M", 2),
          ("rate36M", 10),
          ("rate48M", 11),
          ("rate54M", 12),
          ("rate5Dot5M", 3),
          ("rate6M", 4),
          ("rate9M", 5))
    )



class WlBasicRates(Integer32, TextualConvention):
    status = "current"
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
        *(("all", 2),
          ("default", 1),
          ("rate1And2", 3),
          ("stdRates", 4))
    )



class WlWepModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class WlWpaModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("tkip", 1),
          ("tkipAes", 3))
    )



class WlAuthenticationModes(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("mixedWpa2Wpa", 8),
          ("mixedWpa2WpaPsk", 9),
          ("mode8011x", 1),
          ("open", 2),
          ("shared", 3),
          ("wpa", 4),
          ("wpa2", 5),
          ("wpa2Psk", 7),
          ("wpaPsk", 6))
    )



class WlSecurityKeyCodes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bit128", 2),
          ("bit64", 1))
    )



class WlMACFilterModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("disable", 3))
    )



class WlBridgeAPModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 1),
          ("wirelessBridge", 2))
    )



class WlBridgeRestrictModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 1),
          ("enableScan", 2))
    )



class WlCountryCodes(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class WlWpsAddClientMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessPointPIN", 2),
          ("pushButton", 1),
          ("stationPIN", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ZhnWirelessObjects_ObjectIdentity = ObjectIdentity
zhnWirelessObjects = _ZhnWirelessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1)
)
_WlBaseCfgTable_Object = MibTable
wlBaseCfgTable = _WlBaseCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1)
)
if mibBuilder.loadTexts:
    wlBaseCfgTable.setStatus("current")
_WlBaseCfgEntry_Object = MibTableRow
wlBaseCfgEntry = _WlBaseCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1)
)
wlBaseCfgEntry.setIndexNames(
    (0, "ZHNWIRELESS", "wlBaseCfgIndex"),
)
if mibBuilder.loadTexts:
    wlBaseCfgEntry.setStatus("current")
_WlBaseCfgIndex_Type = Unsigned32
_WlBaseCfgIndex_Object = MibTableColumn
wlBaseCfgIndex = _WlBaseCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 1),
    _WlBaseCfgIndex_Type()
)
wlBaseCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlBaseCfgIndex.setStatus("current")
_WlBaseCfgEnable_Type = TruthValue
_WlBaseCfgEnable_Object = MibTableColumn
wlBaseCfgEnable = _WlBaseCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 2),
    _WlBaseCfgEnable_Type()
)
wlBaseCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgEnable.setStatus("current")
_WlBaseCfgBand_Type = OctetString
_WlBaseCfgBand_Object = MibTableColumn
wlBaseCfgBand = _WlBaseCfgBand_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 3),
    _WlBaseCfgBand_Type()
)
wlBaseCfgBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgBand.setStatus("current")
_WlBaseCfgChannel_Type = WlChannelSelections
_WlBaseCfgChannel_Object = MibTableColumn
wlBaseCfgChannel = _WlBaseCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 4),
    _WlBaseCfgChannel_Type()
)
wlBaseCfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgChannel.setStatus("current")
_WlBaseCfgCurrentChannel_Type = WlChannelSelections
_WlBaseCfgCurrentChannel_Object = MibTableColumn
wlBaseCfgCurrentChannel = _WlBaseCfgCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 5),
    _WlBaseCfgCurrentChannel_Type()
)
wlBaseCfgCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgCurrentChannel.setStatus("current")
_WlBaseCfgBandwidth_Type = OctetString
_WlBaseCfgBandwidth_Object = MibTableColumn
wlBaseCfgBandwidth = _WlBaseCfgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 6),
    _WlBaseCfgBandwidth_Type()
)
wlBaseCfgBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgBandwidth.setStatus("current")
_WlBaseCfgAutoScanTimer_Type = Unsigned32
_WlBaseCfgAutoScanTimer_Object = MibTableColumn
wlBaseCfgAutoScanTimer = _WlBaseCfgAutoScanTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 7),
    _WlBaseCfgAutoScanTimer_Type()
)
wlBaseCfgAutoScanTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgAutoScanTimer.setStatus("current")
_WlBaseCfgMimoNEwc_Type = WlMimoNEwcModes
_WlBaseCfgMimoNEwc_Object = MibTableColumn
wlBaseCfgMimoNEwc = _WlBaseCfgMimoNEwc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 8),
    _WlBaseCfgMimoNEwc_Type()
)
wlBaseCfgMimoNEwc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgMimoNEwc.setStatus("current")
_WlBaseCfgMimoNRate_Type = WlMimoNRates
_WlBaseCfgMimoNRate_Object = MibTableColumn
wlBaseCfgMimoNRate = _WlBaseCfgMimoNRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 9),
    _WlBaseCfgMimoNRate_Type()
)
wlBaseCfgMimoNRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgMimoNRate.setStatus("current")
_WlBaseCfgMimoNProtection_Type = WlMimoNProtectionModes
_WlBaseCfgMimoNProtection_Object = MibTableColumn
wlBaseCfgMimoNProtection = _WlBaseCfgMimoNProtection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 10),
    _WlBaseCfgMimoNProtection_Type()
)
wlBaseCfgMimoNProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgMimoNProtection.setStatus("current")
_WlBaseCfgNClientsOnly_Type = TruthValue
_WlBaseCfgNClientsOnly_Object = MibTableColumn
wlBaseCfgNClientsOnly = _WlBaseCfgNClientsOnly_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 11),
    _WlBaseCfgNClientsOnly_Type()
)
wlBaseCfgNClientsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgNClientsOnly.setStatus("current")
_WlBaseCfg54gRate_Type = Wl54gMulticastRates
_WlBaseCfg54gRate_Object = MibTableColumn
wlBaseCfg54gRate = _WlBaseCfg54gRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 12),
    _WlBaseCfg54gRate_Type()
)
wlBaseCfg54gRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfg54gRate.setStatus("current")
_WlBaseCfgMulticastRate_Type = Wl54gMulticastRates
_WlBaseCfgMulticastRate_Object = MibTableColumn
wlBaseCfgMulticastRate = _WlBaseCfgMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 13),
    _WlBaseCfgMulticastRate_Type()
)
wlBaseCfgMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgMulticastRate.setStatus("current")
_WlBaseCfgBasicRate_Type = WlBasicRates
_WlBaseCfgBasicRate_Object = MibTableColumn
wlBaseCfgBasicRate = _WlBaseCfgBasicRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 14),
    _WlBaseCfgBasicRate_Type()
)
wlBaseCfgBasicRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgBasicRate.setStatus("current")
_WlBaseCfgFragThreshold_Type = Unsigned32
_WlBaseCfgFragThreshold_Object = MibTableColumn
wlBaseCfgFragThreshold = _WlBaseCfgFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 15),
    _WlBaseCfgFragThreshold_Type()
)
wlBaseCfgFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgFragThreshold.setStatus("current")
_WlBaseCfgRTSThreshold_Type = Unsigned32
_WlBaseCfgRTSThreshold_Object = MibTableColumn
wlBaseCfgRTSThreshold = _WlBaseCfgRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 16),
    _WlBaseCfgRTSThreshold_Type()
)
wlBaseCfgRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgRTSThreshold.setStatus("current")
_WlBaseCfgDTIMInterval_Type = Unsigned32
_WlBaseCfgDTIMInterval_Object = MibTableColumn
wlBaseCfgDTIMInterval = _WlBaseCfgDTIMInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 17),
    _WlBaseCfgDTIMInterval_Type()
)
wlBaseCfgDTIMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgDTIMInterval.setStatus("current")
_WlBaseCfgBeaconInterval_Type = Unsigned32
_WlBaseCfgBeaconInterval_Object = MibTableColumn
wlBaseCfgBeaconInterval = _WlBaseCfgBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 18),
    _WlBaseCfgBeaconInterval_Type()
)
wlBaseCfgBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgBeaconInterval.setStatus("current")
_WlBaseCfgGlobalMaxClients_Type = Unsigned32
_WlBaseCfgGlobalMaxClients_Object = MibTableColumn
wlBaseCfgGlobalMaxClients = _WlBaseCfgGlobalMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 19),
    _WlBaseCfgGlobalMaxClients_Type()
)
wlBaseCfgGlobalMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgGlobalMaxClients.setStatus("current")
_WlBaseCfgXPress_Type = TruthValue
_WlBaseCfgXPress_Object = MibTableColumn
wlBaseCfgXPress = _WlBaseCfgXPress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 20),
    _WlBaseCfgXPress_Type()
)
wlBaseCfgXPress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgXPress.setStatus("current")
_WlBaseCfgTxPowerPercent_Type = Unsigned32
_WlBaseCfgTxPowerPercent_Object = MibTableColumn
wlBaseCfgTxPowerPercent = _WlBaseCfgTxPowerPercent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 21),
    _WlBaseCfgTxPowerPercent_Type()
)
wlBaseCfgTxPowerPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgTxPowerPercent.setStatus("current")
_WlBaseCfgWMMEnable_Type = TruthValue
_WlBaseCfgWMMEnable_Object = MibTableColumn
wlBaseCfgWMMEnable = _WlBaseCfgWMMEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 22),
    _WlBaseCfgWMMEnable_Type()
)
wlBaseCfgWMMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgWMMEnable.setStatus("current")
_WlBaseCfgWMMNoAck_Type = TruthValue
_WlBaseCfgWMMNoAck_Object = MibTableColumn
wlBaseCfgWMMNoAck = _WlBaseCfgWMMNoAck_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 23),
    _WlBaseCfgWMMNoAck_Type()
)
wlBaseCfgWMMNoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgWMMNoAck.setStatus("current")
_WlBaseCfgWMMApsd_Type = TruthValue
_WlBaseCfgWMMApsd_Object = MibTableColumn
wlBaseCfgWMMApsd = _WlBaseCfgWMMApsd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 24),
    _WlBaseCfgWMMApsd_Type()
)
wlBaseCfgWMMApsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgWMMApsd.setStatus("current")
_WlBaseCfgWpsAddClientMethod_Type = WlWpsAddClientMethod
_WlBaseCfgWpsAddClientMethod_Object = MibTableColumn
wlBaseCfgWpsAddClientMethod = _WlBaseCfgWpsAddClientMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 25),
    _WlBaseCfgWpsAddClientMethod_Type()
)
wlBaseCfgWpsAddClientMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgWpsAddClientMethod.setStatus("current")
_WlBaseCfgWpsApMode_Type = TruthValue
_WlBaseCfgWpsApMode_Object = MibTableColumn
wlBaseCfgWpsApMode = _WlBaseCfgWpsApMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 26),
    _WlBaseCfgWpsApMode_Type()
)
wlBaseCfgWpsApMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgWpsApMode.setStatus("current")
_WlBaseCfgWpsConfigAp_Type = TruthValue
_WlBaseCfgWpsConfigAp_Object = MibTableColumn
wlBaseCfgWpsConfigAp = _WlBaseCfgWpsConfigAp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 27),
    _WlBaseCfgWpsConfigAp_Type()
)
wlBaseCfgWpsConfigAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgWpsConfigAp.setStatus("current")


class _WlBaseCfgWpsDevicePIN_Type(OctetString):
    """Custom type wlBaseCfgWpsDevicePIN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WlBaseCfgWpsDevicePIN_Type.__name__ = "OctetString"
_WlBaseCfgWpsDevicePIN_Object = MibTableColumn
wlBaseCfgWpsDevicePIN = _WlBaseCfgWpsDevicePIN_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 28),
    _WlBaseCfgWpsDevicePIN_Type()
)
wlBaseCfgWpsDevicePIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgWpsDevicePIN.setStatus("current")
_WlBaseCfgWpsAddEnrollee_Type = TruthValue
_WlBaseCfgWpsAddEnrollee_Object = MibTableColumn
wlBaseCfgWpsAddEnrollee = _WlBaseCfgWpsAddEnrollee_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 29),
    _WlBaseCfgWpsAddEnrollee_Type()
)
wlBaseCfgWpsAddEnrollee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgWpsAddEnrollee.setStatus("current")


class _WlBaseCfgWpsStationPIN_Type(OctetString):
    """Custom type wlBaseCfgWpsStationPIN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WlBaseCfgWpsStationPIN_Type.__name__ = "OctetString"
_WlBaseCfgWpsStationPIN_Object = MibTableColumn
wlBaseCfgWpsStationPIN = _WlBaseCfgWpsStationPIN_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 30),
    _WlBaseCfgWpsStationPIN_Type()
)
wlBaseCfgWpsStationPIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgWpsStationPIN.setStatus("current")
_WlBaseCfgBridgeRestrictMode_Type = WlBridgeRestrictModes
_WlBaseCfgBridgeRestrictMode_Object = MibTableColumn
wlBaseCfgBridgeRestrictMode = _WlBaseCfgBridgeRestrictMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 31),
    _WlBaseCfgBridgeRestrictMode_Type()
)
wlBaseCfgBridgeRestrictMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlBaseCfgBridgeRestrictMode.setStatus("current")
_WlBaseCfgBridgeRefresh_Type = TruthValue
_WlBaseCfgBridgeRefresh_Object = MibTableColumn
wlBaseCfgBridgeRefresh = _WlBaseCfgBridgeRefresh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 1, 1, 32),
    _WlBaseCfgBridgeRefresh_Type()
)
wlBaseCfgBridgeRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlBaseCfgBridgeRefresh.setStatus("current")
_WlVirtualIntfTable_Object = MibTable
wlVirtualIntfTable = _WlVirtualIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2)
)
if mibBuilder.loadTexts:
    wlVirtualIntfTable.setStatus("current")
_WlVirtualIntfEntry_Object = MibTableRow
wlVirtualIntfEntry = _WlVirtualIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1)
)
wlVirtualIntfEntry.setIndexNames(
    (0, "ZHNWIRELESS", "wlBaseCfgIndex"),
    (0, "ZHNWIRELESS", "wlVirtualIndex"),
)
if mibBuilder.loadTexts:
    wlVirtualIntfEntry.setStatus("current")
_WlVirtualIndex_Type = Unsigned32
_WlVirtualIndex_Object = MibTableColumn
wlVirtualIndex = _WlVirtualIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 1),
    _WlVirtualIndex_Type()
)
wlVirtualIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlVirtualIndex.setStatus("current")
_WlVirtualHide_Type = TruthValue
_WlVirtualHide_Object = MibTableColumn
wlVirtualHide = _WlVirtualHide_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 2),
    _WlVirtualHide_Type()
)
wlVirtualHide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlVirtualHide.setStatus("current")
_WlVirtualAPIsolation_Type = TruthValue
_WlVirtualAPIsolation_Object = MibTableColumn
wlVirtualAPIsolation = _WlVirtualAPIsolation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 3),
    _WlVirtualAPIsolation_Type()
)
wlVirtualAPIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlVirtualAPIsolation.setStatus("current")
_WlVirtualDisableWme_Type = TruthValue
_WlVirtualDisableWme_Object = MibTableColumn
wlVirtualDisableWme = _WlVirtualDisableWme_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 4),
    _WlVirtualDisableWme_Type()
)
wlVirtualDisableWme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlVirtualDisableWme.setStatus("current")
_WlVirtualEnableWmf_Type = TruthValue
_WlVirtualEnableWmf_Object = MibTableColumn
wlVirtualEnableWmf = _WlVirtualEnableWmf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 5),
    _WlVirtualEnableWmf_Type()
)
wlVirtualEnableWmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlVirtualEnableWmf.setStatus("current")


class _WlVirtualSsid_Type(OctetString):
    """Custom type wlVirtualSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 72),
    )


_WlVirtualSsid_Type.__name__ = "OctetString"
_WlVirtualSsid_Object = MibTableColumn
wlVirtualSsid = _WlVirtualSsid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 6),
    _WlVirtualSsid_Type()
)
wlVirtualSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlVirtualSsid.setStatus("current")
_WlVirtualBssMacAddr_Type = MacAddress
_WlVirtualBssMacAddr_Object = MibTableColumn
wlVirtualBssMacAddr = _WlVirtualBssMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 7),
    _WlVirtualBssMacAddr_Type()
)
wlVirtualBssMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlVirtualBssMacAddr.setStatus("current")
_WlVirtualCountryCode_Type = WlCountryCodes
_WlVirtualCountryCode_Object = MibTableColumn
wlVirtualCountryCode = _WlVirtualCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 8),
    _WlVirtualCountryCode_Type()
)
wlVirtualCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlVirtualCountryCode.setStatus("current")
_WlVirtualMaxClients_Type = Unsigned32
_WlVirtualMaxClients_Object = MibTableColumn
wlVirtualMaxClients = _WlVirtualMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 9),
    _WlVirtualMaxClients_Type()
)
wlVirtualMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlVirtualMaxClients.setStatus("current")
_WlVirtualEnable_Type = TruthValue
_WlVirtualEnable_Object = MibTableColumn
wlVirtualEnable = _WlVirtualEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 2, 1, 10),
    _WlVirtualEnable_Type()
)
wlVirtualEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlVirtualEnable.setStatus("current")
_WlSecurityTable_Object = MibTable
wlSecurityTable = _WlSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3)
)
if mibBuilder.loadTexts:
    wlSecurityTable.setStatus("current")
_WlSecurityEntry_Object = MibTableRow
wlSecurityEntry = _WlSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1)
)
wlSecurityEntry.setIndexNames(
    (0, "ZHNWIRELESS", "wlBaseCfgIndex"),
    (0, "ZHNWIRELESS", "wlVirtualIndex"),
)
if mibBuilder.loadTexts:
    wlSecurityEntry.setStatus("current")


class _WlSecuritySsid_Type(OctetString):
    """Custom type wlSecuritySsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 72),
    )


_WlSecuritySsid_Type.__name__ = "OctetString"
_WlSecuritySsid_Object = MibTableColumn
wlSecuritySsid = _WlSecuritySsid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 1),
    _WlSecuritySsid_Type()
)
wlSecuritySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlSecuritySsid.setStatus("current")
_WlSecurityWps_Type = TruthValue
_WlSecurityWps_Object = MibTableColumn
wlSecurityWps = _WlSecurityWps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 2),
    _WlSecurityWps_Type()
)
wlSecurityWps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlSecurityWps.setStatus("current")
_WlSecurityAuthMode_Type = WlAuthenticationModes
_WlSecurityAuthMode_Object = MibTableColumn
wlSecurityAuthMode = _WlSecurityAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 3),
    _WlSecurityAuthMode_Type()
)
wlSecurityAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityAuthMode.setStatus("current")


class _WlSecurityWpaPsk_Type(OctetString):
    """Custom type wlSecurityWpaPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 72),
    )


_WlSecurityWpaPsk_Type.__name__ = "OctetString"
_WlSecurityWpaPsk_Object = MibTableColumn
wlSecurityWpaPsk = _WlSecurityWpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 4),
    _WlSecurityWpaPsk_Type()
)
wlSecurityWpaPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWpaPsk.setStatus("current")


class _WlSecurityWpaGTKRekey_Type(Unsigned32):
    """Custom type wlSecurityWpaGTKRekey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WlSecurityWpaGTKRekey_Type.__name__ = "Unsigned32"
_WlSecurityWpaGTKRekey_Object = MibTableColumn
wlSecurityWpaGTKRekey = _WlSecurityWpaGTKRekey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 5),
    _WlSecurityWpaGTKRekey_Type()
)
wlSecurityWpaGTKRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWpaGTKRekey.setStatus("current")
_WlSecurityWpaMode_Type = WlWpaModes
_WlSecurityWpaMode_Object = MibTableColumn
wlSecurityWpaMode = _WlSecurityWpaMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 6),
    _WlSecurityWpaMode_Type()
)
wlSecurityWpaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWpaMode.setStatus("current")
_WlSecurityWepStatus_Type = WlWepModes
_WlSecurityWepStatus_Object = MibTableColumn
wlSecurityWepStatus = _WlSecurityWepStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 7),
    _WlSecurityWepStatus_Type()
)
wlSecurityWepStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWepStatus.setStatus("current")
_WlSecurityRadiusServerIP_Type = IpAddress
_WlSecurityRadiusServerIP_Object = MibTableColumn
wlSecurityRadiusServerIP = _WlSecurityRadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 8),
    _WlSecurityRadiusServerIP_Type()
)
wlSecurityRadiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityRadiusServerIP.setStatus("current")


class _WlSecurityRadiusPort_Type(Unsigned32):
    """Custom type wlSecurityRadiusPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WlSecurityRadiusPort_Type.__name__ = "Unsigned32"
_WlSecurityRadiusPort_Object = MibTableColumn
wlSecurityRadiusPort = _WlSecurityRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 9),
    _WlSecurityRadiusPort_Type()
)
wlSecurityRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityRadiusPort.setStatus("current")


class _WlSecurityRadiusKey_Type(OctetString):
    """Custom type wlSecurityRadiusKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 72),
    )


_WlSecurityRadiusKey_Type.__name__ = "OctetString"
_WlSecurityRadiusKey_Object = MibTableColumn
wlSecurityRadiusKey = _WlSecurityRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 10),
    _WlSecurityRadiusKey_Type()
)
wlSecurityRadiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityRadiusKey.setStatus("current")
_WlSecurityWepKey_Type = WlSecurityKeyCodes
_WlSecurityWepKey_Object = MibTableColumn
wlSecurityWepKey = _WlSecurityWepKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 11),
    _WlSecurityWepKey_Type()
)
wlSecurityWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWepKey.setStatus("current")


class _WlSecurityCurrentWepKeyIndex64_Type(Unsigned32):
    """Custom type wlSecurityCurrentWepKeyIndex64 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlSecurityCurrentWepKeyIndex64_Type.__name__ = "Unsigned32"
_WlSecurityCurrentWepKeyIndex64_Object = MibTableColumn
wlSecurityCurrentWepKeyIndex64 = _WlSecurityCurrentWepKeyIndex64_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 12),
    _WlSecurityCurrentWepKeyIndex64_Type()
)
wlSecurityCurrentWepKeyIndex64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityCurrentWepKeyIndex64.setStatus("current")


class _WlSecurityCurrentWepKeyIndex128_Type(Unsigned32):
    """Custom type wlSecurityCurrentWepKeyIndex128 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlSecurityCurrentWepKeyIndex128_Type.__name__ = "Unsigned32"
_WlSecurityCurrentWepKeyIndex128_Object = MibTableColumn
wlSecurityCurrentWepKeyIndex128 = _WlSecurityCurrentWepKeyIndex128_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 13),
    _WlSecurityCurrentWepKeyIndex128_Type()
)
wlSecurityCurrentWepKeyIndex128.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityCurrentWepKeyIndex128.setStatus("current")


class _WlSecurityWep64Key1_Type(OctetString):
    """Custom type wlSecurityWep64Key1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 10),
    )


_WlSecurityWep64Key1_Type.__name__ = "OctetString"
_WlSecurityWep64Key1_Object = MibTableColumn
wlSecurityWep64Key1 = _WlSecurityWep64Key1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 14),
    _WlSecurityWep64Key1_Type()
)
wlSecurityWep64Key1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep64Key1.setStatus("current")


class _WlSecurityWep64Key2_Type(OctetString):
    """Custom type wlSecurityWep64Key2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 10),
    )


_WlSecurityWep64Key2_Type.__name__ = "OctetString"
_WlSecurityWep64Key2_Object = MibTableColumn
wlSecurityWep64Key2 = _WlSecurityWep64Key2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 15),
    _WlSecurityWep64Key2_Type()
)
wlSecurityWep64Key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep64Key2.setStatus("current")


class _WlSecurityWep64Key3_Type(OctetString):
    """Custom type wlSecurityWep64Key3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 10),
    )


_WlSecurityWep64Key3_Type.__name__ = "OctetString"
_WlSecurityWep64Key3_Object = MibTableColumn
wlSecurityWep64Key3 = _WlSecurityWep64Key3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 16),
    _WlSecurityWep64Key3_Type()
)
wlSecurityWep64Key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep64Key3.setStatus("current")


class _WlSecurityWep64Key4_Type(OctetString):
    """Custom type wlSecurityWep64Key4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 10),
    )


_WlSecurityWep64Key4_Type.__name__ = "OctetString"
_WlSecurityWep64Key4_Object = MibTableColumn
wlSecurityWep64Key4 = _WlSecurityWep64Key4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 17),
    _WlSecurityWep64Key4_Type()
)
wlSecurityWep64Key4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep64Key4.setStatus("current")


class _WlSecurityWep128Key1_Type(OctetString):
    """Custom type wlSecurityWep128Key1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 26),
    )


_WlSecurityWep128Key1_Type.__name__ = "OctetString"
_WlSecurityWep128Key1_Object = MibTableColumn
wlSecurityWep128Key1 = _WlSecurityWep128Key1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 18),
    _WlSecurityWep128Key1_Type()
)
wlSecurityWep128Key1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep128Key1.setStatus("current")


class _WlSecurityWep128Key2_Type(OctetString):
    """Custom type wlSecurityWep128Key2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 26),
    )


_WlSecurityWep128Key2_Type.__name__ = "OctetString"
_WlSecurityWep128Key2_Object = MibTableColumn
wlSecurityWep128Key2 = _WlSecurityWep128Key2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 19),
    _WlSecurityWep128Key2_Type()
)
wlSecurityWep128Key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep128Key2.setStatus("current")


class _WlSecurityWep128Key3_Type(OctetString):
    """Custom type wlSecurityWep128Key3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 26),
    )


_WlSecurityWep128Key3_Type.__name__ = "OctetString"
_WlSecurityWep128Key3_Object = MibTableColumn
wlSecurityWep128Key3 = _WlSecurityWep128Key3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 20),
    _WlSecurityWep128Key3_Type()
)
wlSecurityWep128Key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep128Key3.setStatus("current")


class _WlSecurityWep128Key4_Type(OctetString):
    """Custom type wlSecurityWep128Key4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 26),
    )


_WlSecurityWep128Key4_Type.__name__ = "OctetString"
_WlSecurityWep128Key4_Object = MibTableColumn
wlSecurityWep128Key4 = _WlSecurityWep128Key4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 21),
    _WlSecurityWep128Key4_Type()
)
wlSecurityWep128Key4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWep128Key4.setStatus("current")
_WlSecurityWpa2Preauth_Type = TruthValue
_WlSecurityWpa2Preauth_Object = MibTableColumn
wlSecurityWpa2Preauth = _WlSecurityWpa2Preauth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 22),
    _WlSecurityWpa2Preauth_Type()
)
wlSecurityWpa2Preauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWpa2Preauth.setStatus("current")


class _WlSecurityWpa2NetReauth_Type(Unsigned32):
    """Custom type wlSecurityWpa2NetReauth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_WlSecurityWpa2NetReauth_Type.__name__ = "Unsigned32"
_WlSecurityWpa2NetReauth_Object = MibTableColumn
wlSecurityWpa2NetReauth = _WlSecurityWpa2NetReauth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 23),
    _WlSecurityWpa2NetReauth_Type()
)
wlSecurityWpa2NetReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityWpa2NetReauth.setStatus("current")
_WlSecurityMACFilterMode_Type = WlMACFilterModes
_WlSecurityMACFilterMode_Object = MibTableColumn
wlSecurityMACFilterMode = _WlSecurityMACFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 3, 1, 24),
    _WlSecurityMACFilterMode_Type()
)
wlSecurityMACFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlSecurityMACFilterMode.setStatus("current")
_WlMACFilterTable_Object = MibTable
wlMACFilterTable = _WlMACFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 4)
)
if mibBuilder.loadTexts:
    wlMACFilterTable.setStatus("current")
_WlMACFilterEntry_Object = MibTableRow
wlMACFilterEntry = _WlMACFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 4, 1)
)
wlMACFilterEntry.setIndexNames(
    (0, "ZHNWIRELESS", "wlBaseCfgIndex"),
    (0, "ZHNWIRELESS", "wlVirtualIndex"),
    (0, "ZHNWIRELESS", "wlMACFilterIndex"),
)
if mibBuilder.loadTexts:
    wlMACFilterEntry.setStatus("current")
_WlMACFilterIndex_Type = Unsigned32
_WlMACFilterIndex_Object = MibTableColumn
wlMACFilterIndex = _WlMACFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 4, 1, 1),
    _WlMACFilterIndex_Type()
)
wlMACFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlMACFilterIndex.setStatus("current")


class _WlMACFilterSsid_Type(OctetString):
    """Custom type wlMACFilterSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 72),
    )


_WlMACFilterSsid_Type.__name__ = "OctetString"
_WlMACFilterSsid_Object = MibTableColumn
wlMACFilterSsid = _WlMACFilterSsid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 4, 1, 2),
    _WlMACFilterSsid_Type()
)
wlMACFilterSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlMACFilterSsid.setStatus("current")
_WlMACFilterMacAddr_Type = MacAddress
_WlMACFilterMacAddr_Object = MibTableColumn
wlMACFilterMacAddr = _WlMACFilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 4, 1, 3),
    _WlMACFilterMacAddr_Type()
)
wlMACFilterMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlMACFilterMacAddr.setStatus("current")


class _WlMACFilterIfName_Type(OctetString):
    """Custom type wlMACFilterIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 72),
    )


_WlMACFilterIfName_Type.__name__ = "OctetString"
_WlMACFilterIfName_Object = MibTableColumn
wlMACFilterIfName = _WlMACFilterIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 4, 1, 4),
    _WlMACFilterIfName_Type()
)
wlMACFilterIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlMACFilterIfName.setStatus("current")
_WlMACFilterRowStatus_Type = ZhoneRowStatus
_WlMACFilterRowStatus_Object = MibTableColumn
wlMACFilterRowStatus = _WlMACFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 4, 1, 5),
    _WlMACFilterRowStatus_Type()
)
wlMACFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlMACFilterRowStatus.setStatus("current")
_WlStaticWdsMACAddrTable_Object = MibTable
wlStaticWdsMACAddrTable = _WlStaticWdsMACAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 5)
)
if mibBuilder.loadTexts:
    wlStaticWdsMACAddrTable.setStatus("current")
_WlStaticWdsMACAddrEntry_Object = MibTableRow
wlStaticWdsMACAddrEntry = _WlStaticWdsMACAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 5, 1)
)
wlStaticWdsMACAddrEntry.setIndexNames(
    (0, "ZHNWIRELESS", "wlBaseCfgIndex"),
    (0, "ZHNWIRELESS", "wlStaticWdsMACIndex"),
)
if mibBuilder.loadTexts:
    wlStaticWdsMACAddrEntry.setStatus("current")
_WlStaticWdsMACIndex_Type = Unsigned32
_WlStaticWdsMACIndex_Object = MibTableColumn
wlStaticWdsMACIndex = _WlStaticWdsMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 5, 1, 1),
    _WlStaticWdsMACIndex_Type()
)
wlStaticWdsMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlStaticWdsMACIndex.setStatus("current")
_WlStaticWdsRemoteMACAddr_Type = MacAddress
_WlStaticWdsRemoteMACAddr_Object = MibTableColumn
wlStaticWdsRemoteMACAddr = _WlStaticWdsRemoteMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 5, 1, 2),
    _WlStaticWdsRemoteMACAddr_Type()
)
wlStaticWdsRemoteMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlStaticWdsRemoteMACAddr.setStatus("current")
_WlScanWdsMACAddrTable_Object = MibTable
wlScanWdsMACAddrTable = _WlScanWdsMACAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 6)
)
if mibBuilder.loadTexts:
    wlScanWdsMACAddrTable.setStatus("current")
_WlScanWdsMACAddrEntry_Object = MibTableRow
wlScanWdsMACAddrEntry = _WlScanWdsMACAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 6, 1)
)
wlScanWdsMACAddrEntry.setIndexNames(
    (0, "ZHNWIRELESS", "wlBaseCfgIndex"),
    (0, "ZHNWIRELESS", "wlScanWdsMACIndex"),
)
if mibBuilder.loadTexts:
    wlScanWdsMACAddrEntry.setStatus("current")
_WlScanWdsMACIndex_Type = Unsigned32
_WlScanWdsMACIndex_Object = MibTableColumn
wlScanWdsMACIndex = _WlScanWdsMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 6, 1, 1),
    _WlScanWdsMACIndex_Type()
)
wlScanWdsMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlScanWdsMACIndex.setStatus("current")
_WlScanWdsRemoteMACAddr_Type = MacAddress
_WlScanWdsRemoteMACAddr_Object = MibTableColumn
wlScanWdsRemoteMACAddr = _WlScanWdsRemoteMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 6, 1, 2),
    _WlScanWdsRemoteMACAddr_Type()
)
wlScanWdsRemoteMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlScanWdsRemoteMACAddr.setStatus("current")
_WlAuthStationsTable_Object = MibTable
wlAuthStationsTable = _WlAuthStationsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7)
)
if mibBuilder.loadTexts:
    wlAuthStationsTable.setStatus("current")
_WlAuthStationsEntry_Object = MibTableRow
wlAuthStationsEntry = _WlAuthStationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7, 1)
)
wlAuthStationsEntry.setIndexNames(
    (0, "ZHNWIRELESS", "wlAuthStationIndex"),
)
if mibBuilder.loadTexts:
    wlAuthStationsEntry.setStatus("current")
_WlAuthStationIndex_Type = Unsigned32
_WlAuthStationIndex_Object = MibTableColumn
wlAuthStationIndex = _WlAuthStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7, 1, 1),
    _WlAuthStationIndex_Type()
)
wlAuthStationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlAuthStationIndex.setStatus("current")
_WlAuthStationMACAddr_Type = MacAddress
_WlAuthStationMACAddr_Object = MibTableColumn
wlAuthStationMACAddr = _WlAuthStationMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7, 1, 2),
    _WlAuthStationMACAddr_Type()
)
wlAuthStationMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlAuthStationMACAddr.setStatus("current")
_WlAuthStationAssociationStatus_Type = TruthValue
_WlAuthStationAssociationStatus_Object = MibTableColumn
wlAuthStationAssociationStatus = _WlAuthStationAssociationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7, 1, 3),
    _WlAuthStationAssociationStatus_Type()
)
wlAuthStationAssociationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlAuthStationAssociationStatus.setStatus("current")
_WlAuthStationAuthorizationStatus_Type = TruthValue
_WlAuthStationAuthorizationStatus_Object = MibTableColumn
wlAuthStationAuthorizationStatus = _WlAuthStationAuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7, 1, 4),
    _WlAuthStationAuthorizationStatus_Type()
)
wlAuthStationAuthorizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlAuthStationAuthorizationStatus.setStatus("current")
_WlAuthStationSSID_Type = OctetString
_WlAuthStationSSID_Object = MibTableColumn
wlAuthStationSSID = _WlAuthStationSSID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7, 1, 5),
    _WlAuthStationSSID_Type()
)
wlAuthStationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlAuthStationSSID.setStatus("current")
_WlAuthStationInterface_Type = OctetString
_WlAuthStationInterface_Object = MibTableColumn
wlAuthStationInterface = _WlAuthStationInterface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 1, 7, 1, 6),
    _WlAuthStationInterface_Type()
)
wlAuthStationInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlAuthStationInterface.setStatus("current")
_ZhnWirelessConformance_ObjectIdentity = ObjectIdentity
zhnWirelessConformance = _ZhnWirelessConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2)
)
_ZhnWirelessGroups_ObjectIdentity = ObjectIdentity
zhnWirelessGroups = _ZhnWirelessGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1)
)
_ZhnWirelessCompliances_ObjectIdentity = ObjectIdentity
zhnWirelessCompliances = _ZhnWirelessCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 2)
)

# Managed Objects groups

zhnWlBaseCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1, 1)
)
zhnWlBaseCfgGroup.setObjects(
      *(("ZHNWIRELESS", "wlBaseCfgEnable"),
        ("ZHNWIRELESS", "wlBaseCfgBand"),
        ("ZHNWIRELESS", "wlBaseCfgChannel"),
        ("ZHNWIRELESS", "wlBaseCfgCurrentChannel"),
        ("ZHNWIRELESS", "wlBaseCfgBandwidth"),
        ("ZHNWIRELESS", "wlBaseCfgAutoScanTimer"),
        ("ZHNWIRELESS", "wlBaseCfgMimoNEwc"),
        ("ZHNWIRELESS", "wlBaseCfgMimoNRate"),
        ("ZHNWIRELESS", "wlBaseCfgMimoNProtection"),
        ("ZHNWIRELESS", "wlBaseCfgNClientsOnly"),
        ("ZHNWIRELESS", "wlBaseCfg54gRate"),
        ("ZHNWIRELESS", "wlBaseCfgMulticastRate"),
        ("ZHNWIRELESS", "wlBaseCfgBasicRate"),
        ("ZHNWIRELESS", "wlBaseCfgFragThreshold"),
        ("ZHNWIRELESS", "wlBaseCfgRTSThreshold"),
        ("ZHNWIRELESS", "wlBaseCfgDTIMInterval"),
        ("ZHNWIRELESS", "wlBaseCfgBeaconInterval"),
        ("ZHNWIRELESS", "wlBaseCfgGlobalMaxClients"),
        ("ZHNWIRELESS", "wlBaseCfgXPress"),
        ("ZHNWIRELESS", "wlBaseCfgTxPowerPercent"),
        ("ZHNWIRELESS", "wlBaseCfgWMMEnable"),
        ("ZHNWIRELESS", "wlBaseCfgWMMNoAck"),
        ("ZHNWIRELESS", "wlBaseCfgWMMApsd"),
        ("ZHNWIRELESS", "wlBaseCfgWpsAddClientMethod"),
        ("ZHNWIRELESS", "wlBaseCfgWpsApMode"),
        ("ZHNWIRELESS", "wlBaseCfgWpsConfigAp"),
        ("ZHNWIRELESS", "wlBaseCfgWpsDevicePIN"),
        ("ZHNWIRELESS", "wlBaseCfgWpsAddEnrollee"),
        ("ZHNWIRELESS", "wlBaseCfgWpsStationPIN"),
        ("ZHNWIRELESS", "wlBaseCfgBridgeRestrictMode"),
        ("ZHNWIRELESS", "wlBaseCfgBridgeRefresh"))
)
if mibBuilder.loadTexts:
    zhnWlBaseCfgGroup.setStatus("current")

zhnWlVirtualCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1, 2)
)
zhnWlVirtualCfgGroup.setObjects(
      *(("ZHNWIRELESS", "wlVirtualHide"),
        ("ZHNWIRELESS", "wlVirtualAPIsolation"),
        ("ZHNWIRELESS", "wlVirtualDisableWme"),
        ("ZHNWIRELESS", "wlVirtualEnableWmf"),
        ("ZHNWIRELESS", "wlVirtualSsid"),
        ("ZHNWIRELESS", "wlVirtualBssMacAddr"),
        ("ZHNWIRELESS", "wlVirtualCountryCode"),
        ("ZHNWIRELESS", "wlVirtualMaxClients"),
        ("ZHNWIRELESS", "wlVirtualEnable"))
)
if mibBuilder.loadTexts:
    zhnWlVirtualCfgGroup.setStatus("current")

zhnWlSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1, 3)
)
zhnWlSecurityGroup.setObjects(
      *(("ZHNWIRELESS", "wlSecuritySsid"),
        ("ZHNWIRELESS", "wlSecurityWps"),
        ("ZHNWIRELESS", "wlSecurityAuthMode"),
        ("ZHNWIRELESS", "wlSecurityWpaPsk"),
        ("ZHNWIRELESS", "wlSecurityWpaGTKRekey"),
        ("ZHNWIRELESS", "wlSecurityWpaMode"),
        ("ZHNWIRELESS", "wlSecurityWepStatus"),
        ("ZHNWIRELESS", "wlSecurityRadiusServerIP"),
        ("ZHNWIRELESS", "wlSecurityRadiusPort"),
        ("ZHNWIRELESS", "wlSecurityRadiusKey"),
        ("ZHNWIRELESS", "wlSecurityWepKey"),
        ("ZHNWIRELESS", "wlSecurityCurrentWepKeyIndex64"),
        ("ZHNWIRELESS", "wlSecurityCurrentWepKeyIndex128"),
        ("ZHNWIRELESS", "wlSecurityWep64Key1"),
        ("ZHNWIRELESS", "wlSecurityWep64Key2"),
        ("ZHNWIRELESS", "wlSecurityWep64Key3"),
        ("ZHNWIRELESS", "wlSecurityWep64Key4"),
        ("ZHNWIRELESS", "wlSecurityWep128Key1"),
        ("ZHNWIRELESS", "wlSecurityWep128Key2"),
        ("ZHNWIRELESS", "wlSecurityWep128Key3"),
        ("ZHNWIRELESS", "wlSecurityWep128Key4"),
        ("ZHNWIRELESS", "wlSecurityWpa2Preauth"),
        ("ZHNWIRELESS", "wlSecurityWpa2NetReauth"),
        ("ZHNWIRELESS", "wlSecurityMACFilterMode"))
)
if mibBuilder.loadTexts:
    zhnWlSecurityGroup.setStatus("current")

zhnWlMACFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1, 4)
)
zhnWlMACFilterGroup.setObjects(
      *(("ZHNWIRELESS", "wlMACFilterSsid"),
        ("ZHNWIRELESS", "wlMACFilterMacAddr"),
        ("ZHNWIRELESS", "wlMACFilterIfName"),
        ("ZHNWIRELESS", "wlMACFilterRowStatus"))
)
if mibBuilder.loadTexts:
    zhnWlMACFilterGroup.setStatus("current")

zhnWlStaticWdsMACAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1, 5)
)
zhnWlStaticWdsMACAddrGroup.setObjects(
    ("ZHNWIRELESS", "wlStaticWdsRemoteMACAddr")
)
if mibBuilder.loadTexts:
    zhnWlStaticWdsMACAddrGroup.setStatus("current")

zhnWlScanWdsMACAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1, 6)
)
zhnWlScanWdsMACAddrGroup.setObjects(
    ("ZHNWIRELESS", "wlScanWdsRemoteMACAddr")
)
if mibBuilder.loadTexts:
    zhnWlScanWdsMACAddrGroup.setStatus("current")

zhnWlAuthStationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 1, 7)
)
zhnWlAuthStationsGroup.setObjects(
      *(("ZHNWIRELESS", "wlAuthStationMACAddr"),
        ("ZHNWIRELESS", "wlAuthStationAssociationStatus"),
        ("ZHNWIRELESS", "wlAuthStationAuthorizationStatus"),
        ("ZHNWIRELESS", "wlAuthStationSSID"),
        ("ZHNWIRELESS", "wlAuthStationInterface"))
)
if mibBuilder.loadTexts:
    zhnWlAuthStationsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnWirelessCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 46, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnWirelessCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNWIRELESS",
    **{"WlChannelSelections": WlChannelSelections,
       "WlMimoNEwcModes": WlMimoNEwcModes,
       "WlMimoNRates": WlMimoNRates,
       "WlMimoNProtectionModes": WlMimoNProtectionModes,
       "Wl54gMulticastRates": Wl54gMulticastRates,
       "WlBasicRates": WlBasicRates,
       "WlWepModes": WlWepModes,
       "WlWpaModes": WlWpaModes,
       "WlAuthenticationModes": WlAuthenticationModes,
       "WlSecurityKeyCodes": WlSecurityKeyCodes,
       "WlMACFilterModes": WlMACFilterModes,
       "WlBridgeAPModes": WlBridgeAPModes,
       "WlBridgeRestrictModes": WlBridgeRestrictModes,
       "WlCountryCodes": WlCountryCodes,
       "WlWpsAddClientMethod": WlWpsAddClientMethod,
       "zhnWireless": zhnWireless,
       "zhnWirelessObjects": zhnWirelessObjects,
       "wlBaseCfgTable": wlBaseCfgTable,
       "wlBaseCfgEntry": wlBaseCfgEntry,
       "wlBaseCfgIndex": wlBaseCfgIndex,
       "wlBaseCfgEnable": wlBaseCfgEnable,
       "wlBaseCfgBand": wlBaseCfgBand,
       "wlBaseCfgChannel": wlBaseCfgChannel,
       "wlBaseCfgCurrentChannel": wlBaseCfgCurrentChannel,
       "wlBaseCfgBandwidth": wlBaseCfgBandwidth,
       "wlBaseCfgAutoScanTimer": wlBaseCfgAutoScanTimer,
       "wlBaseCfgMimoNEwc": wlBaseCfgMimoNEwc,
       "wlBaseCfgMimoNRate": wlBaseCfgMimoNRate,
       "wlBaseCfgMimoNProtection": wlBaseCfgMimoNProtection,
       "wlBaseCfgNClientsOnly": wlBaseCfgNClientsOnly,
       "wlBaseCfg54gRate": wlBaseCfg54gRate,
       "wlBaseCfgMulticastRate": wlBaseCfgMulticastRate,
       "wlBaseCfgBasicRate": wlBaseCfgBasicRate,
       "wlBaseCfgFragThreshold": wlBaseCfgFragThreshold,
       "wlBaseCfgRTSThreshold": wlBaseCfgRTSThreshold,
       "wlBaseCfgDTIMInterval": wlBaseCfgDTIMInterval,
       "wlBaseCfgBeaconInterval": wlBaseCfgBeaconInterval,
       "wlBaseCfgGlobalMaxClients": wlBaseCfgGlobalMaxClients,
       "wlBaseCfgXPress": wlBaseCfgXPress,
       "wlBaseCfgTxPowerPercent": wlBaseCfgTxPowerPercent,
       "wlBaseCfgWMMEnable": wlBaseCfgWMMEnable,
       "wlBaseCfgWMMNoAck": wlBaseCfgWMMNoAck,
       "wlBaseCfgWMMApsd": wlBaseCfgWMMApsd,
       "wlBaseCfgWpsAddClientMethod": wlBaseCfgWpsAddClientMethod,
       "wlBaseCfgWpsApMode": wlBaseCfgWpsApMode,
       "wlBaseCfgWpsConfigAp": wlBaseCfgWpsConfigAp,
       "wlBaseCfgWpsDevicePIN": wlBaseCfgWpsDevicePIN,
       "wlBaseCfgWpsAddEnrollee": wlBaseCfgWpsAddEnrollee,
       "wlBaseCfgWpsStationPIN": wlBaseCfgWpsStationPIN,
       "wlBaseCfgBridgeRestrictMode": wlBaseCfgBridgeRestrictMode,
       "wlBaseCfgBridgeRefresh": wlBaseCfgBridgeRefresh,
       "wlVirtualIntfTable": wlVirtualIntfTable,
       "wlVirtualIntfEntry": wlVirtualIntfEntry,
       "wlVirtualIndex": wlVirtualIndex,
       "wlVirtualHide": wlVirtualHide,
       "wlVirtualAPIsolation": wlVirtualAPIsolation,
       "wlVirtualDisableWme": wlVirtualDisableWme,
       "wlVirtualEnableWmf": wlVirtualEnableWmf,
       "wlVirtualSsid": wlVirtualSsid,
       "wlVirtualBssMacAddr": wlVirtualBssMacAddr,
       "wlVirtualCountryCode": wlVirtualCountryCode,
       "wlVirtualMaxClients": wlVirtualMaxClients,
       "wlVirtualEnable": wlVirtualEnable,
       "wlSecurityTable": wlSecurityTable,
       "wlSecurityEntry": wlSecurityEntry,
       "wlSecuritySsid": wlSecuritySsid,
       "wlSecurityWps": wlSecurityWps,
       "wlSecurityAuthMode": wlSecurityAuthMode,
       "wlSecurityWpaPsk": wlSecurityWpaPsk,
       "wlSecurityWpaGTKRekey": wlSecurityWpaGTKRekey,
       "wlSecurityWpaMode": wlSecurityWpaMode,
       "wlSecurityWepStatus": wlSecurityWepStatus,
       "wlSecurityRadiusServerIP": wlSecurityRadiusServerIP,
       "wlSecurityRadiusPort": wlSecurityRadiusPort,
       "wlSecurityRadiusKey": wlSecurityRadiusKey,
       "wlSecurityWepKey": wlSecurityWepKey,
       "wlSecurityCurrentWepKeyIndex64": wlSecurityCurrentWepKeyIndex64,
       "wlSecurityCurrentWepKeyIndex128": wlSecurityCurrentWepKeyIndex128,
       "wlSecurityWep64Key1": wlSecurityWep64Key1,
       "wlSecurityWep64Key2": wlSecurityWep64Key2,
       "wlSecurityWep64Key3": wlSecurityWep64Key3,
       "wlSecurityWep64Key4": wlSecurityWep64Key4,
       "wlSecurityWep128Key1": wlSecurityWep128Key1,
       "wlSecurityWep128Key2": wlSecurityWep128Key2,
       "wlSecurityWep128Key3": wlSecurityWep128Key3,
       "wlSecurityWep128Key4": wlSecurityWep128Key4,
       "wlSecurityWpa2Preauth": wlSecurityWpa2Preauth,
       "wlSecurityWpa2NetReauth": wlSecurityWpa2NetReauth,
       "wlSecurityMACFilterMode": wlSecurityMACFilterMode,
       "wlMACFilterTable": wlMACFilterTable,
       "wlMACFilterEntry": wlMACFilterEntry,
       "wlMACFilterIndex": wlMACFilterIndex,
       "wlMACFilterSsid": wlMACFilterSsid,
       "wlMACFilterMacAddr": wlMACFilterMacAddr,
       "wlMACFilterIfName": wlMACFilterIfName,
       "wlMACFilterRowStatus": wlMACFilterRowStatus,
       "wlStaticWdsMACAddrTable": wlStaticWdsMACAddrTable,
       "wlStaticWdsMACAddrEntry": wlStaticWdsMACAddrEntry,
       "wlStaticWdsMACIndex": wlStaticWdsMACIndex,
       "wlStaticWdsRemoteMACAddr": wlStaticWdsRemoteMACAddr,
       "wlScanWdsMACAddrTable": wlScanWdsMACAddrTable,
       "wlScanWdsMACAddrEntry": wlScanWdsMACAddrEntry,
       "wlScanWdsMACIndex": wlScanWdsMACIndex,
       "wlScanWdsRemoteMACAddr": wlScanWdsRemoteMACAddr,
       "wlAuthStationsTable": wlAuthStationsTable,
       "wlAuthStationsEntry": wlAuthStationsEntry,
       "wlAuthStationIndex": wlAuthStationIndex,
       "wlAuthStationMACAddr": wlAuthStationMACAddr,
       "wlAuthStationAssociationStatus": wlAuthStationAssociationStatus,
       "wlAuthStationAuthorizationStatus": wlAuthStationAuthorizationStatus,
       "wlAuthStationSSID": wlAuthStationSSID,
       "wlAuthStationInterface": wlAuthStationInterface,
       "zhnWirelessConformance": zhnWirelessConformance,
       "zhnWirelessGroups": zhnWirelessGroups,
       "zhnWlBaseCfgGroup": zhnWlBaseCfgGroup,
       "zhnWlVirtualCfgGroup": zhnWlVirtualCfgGroup,
       "zhnWlSecurityGroup": zhnWlSecurityGroup,
       "zhnWlMACFilterGroup": zhnWlMACFilterGroup,
       "zhnWlStaticWdsMACAddrGroup": zhnWlStaticWdsMACAddrGroup,
       "zhnWlScanWdsMACAddrGroup": zhnWlScanWdsMACAddrGroup,
       "zhnWlAuthStationsGroup": zhnWlAuthStationsGroup,
       "zhnWirelessCompliances": zhnWirelessCompliances,
       "zhnWirelessCompliance": zhnWirelessCompliance}
)
