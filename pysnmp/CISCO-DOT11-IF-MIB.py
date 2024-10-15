# SNMP MIB module (CISCO-DOT11-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:45 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(dot11AuthenticationAlgorithmsIndex,
 dot11SupportedDataRatesRxIndex) = mibBuilder.importSymbols(
    "IEEE802dot11-MIB",
    "dot11AuthenticationAlgorithmsIndex",
    "dot11SupportedDataRatesRxIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoDot11IfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272)
)
ciscoDot11IfMIB.setRevisions(
        ("2006-12-20 00:00",
         "2005-03-10 00:00",
         "2004-06-06 00:00",
         "2004-05-06 00:00",
         "2004-04-17 00:00",
         "2004-02-27 00:00",
         "2003-11-17 00:00",
         "2003-07-13 00:00",
         "2002-12-29 00:00",
         "2002-08-01 00:00",
         "2002-07-04 00:00",
         "2002-05-10 00:00",
         "2002-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDot11IfVlanIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class WepKeyType128(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 13),
    )



class CDot11IfMicAlgorithm(Integer32, TextualConvention):
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
        *(("micMXX", 2),
          ("micMichael", 3),
          ("micNone", 1))
    )



class CDot11IfWepKeyPermuteAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wepPermuteIV", 2),
          ("wepPermuteNone", 1))
    )



class CDot11IfCipherType(Bits, TextualConvention):
    status = "current"


class CDot11RadioFrequencyBandType(Bits, TextualConvention):
    status = "current"


class CDot11RadioModulationClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsss", 1),
          ("ofdm", 2))
    )



class Cd11IfDot11UpgradeStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("upgradeDone", 5),
          ("upgradeNotApplicable", 2),
          ("upgradeNotDone", 3),
          ("upgradeNotNeeded", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDot11IfMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoDot11IfMIBNotifications = _CiscoDot11IfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 0)
)
_CiscoDot11IfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11IfMIBObjects = _CiscoDot11IfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1)
)
_Cd11IfConfigurations_ObjectIdentity = ObjectIdentity
cd11IfConfigurations = _Cd11IfConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1)
)
_Cd11IfManagement_ObjectIdentity = ObjectIdentity
cd11IfManagement = _Cd11IfManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1)
)
_Cd11IfStationConfigTable_Object = MibTable
cd11IfStationConfigTable = _Cd11IfStationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cd11IfStationConfigTable.setStatus("current")
_Cd11IfStationConfigEntry_Object = MibTableRow
cd11IfStationConfigEntry = _Cd11IfStationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1)
)
cd11IfStationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfStationConfigEntry.setStatus("current")


class _Cd11IfStationRole_Type(Integer32):
    """Custom type cd11IfStationRole based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("roleApBridge", 6),
          ("roleApNrBridge", 10),
          ("roleApRepeater", 7),
          ("roleBridge", 2),
          ("roleClient", 3),
          ("roleIBSS", 8),
          ("roleNrBridge", 9),
          ("roleRepeater", 5),
          ("roleRoot", 4),
          ("roleScanner", 11),
          ("roleWgb", 1))
    )


_Cd11IfStationRole_Type.__name__ = "Integer32"
_Cd11IfStationRole_Object = MibTableColumn
cd11IfStationRole = _Cd11IfStationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 1),
    _Cd11IfStationRole_Type()
)
cd11IfStationRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfStationRole.setStatus("current")
_Cd11IfCiscoExtensionsEnable_Type = TruthValue
_Cd11IfCiscoExtensionsEnable_Object = MibTableColumn
cd11IfCiscoExtensionsEnable = _Cd11IfCiscoExtensionsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 2),
    _Cd11IfCiscoExtensionsEnable_Type()
)
cd11IfCiscoExtensionsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfCiscoExtensionsEnable.setStatus("current")
_Cd11IfAllowBroadcastSsidAssoc_Type = TruthValue
_Cd11IfAllowBroadcastSsidAssoc_Object = MibTableColumn
cd11IfAllowBroadcastSsidAssoc = _Cd11IfAllowBroadcastSsidAssoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 3),
    _Cd11IfAllowBroadcastSsidAssoc_Type()
)
cd11IfAllowBroadcastSsidAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAllowBroadcastSsidAssoc.setStatus("current")


class _Cd11IfPrivacyOptionMaxRate_Type(Integer32):
    """Custom type cd11IfPrivacyOptionMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Cd11IfPrivacyOptionMaxRate_Type.__name__ = "Integer32"
_Cd11IfPrivacyOptionMaxRate_Object = MibTableColumn
cd11IfPrivacyOptionMaxRate = _Cd11IfPrivacyOptionMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 4),
    _Cd11IfPrivacyOptionMaxRate_Type()
)
cd11IfPrivacyOptionMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfPrivacyOptionMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfPrivacyOptionMaxRate.setUnits("500 Kb per second")


class _Cd11IfEthernetEncapsulDefault_Type(Integer32):
    """Custom type cd11IfEthernetEncapsulDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encap802dot1H", 1),
          ("encapRfc1042", 2))
    )


_Cd11IfEthernetEncapsulDefault_Type.__name__ = "Integer32"
_Cd11IfEthernetEncapsulDefault_Object = MibTableColumn
cd11IfEthernetEncapsulDefault = _Cd11IfEthernetEncapsulDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 5),
    _Cd11IfEthernetEncapsulDefault_Type()
)
cd11IfEthernetEncapsulDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfEthernetEncapsulDefault.setStatus("current")


class _Cd11IfBridgeSpacing_Type(Unsigned32):
    """Custom type cd11IfBridgeSpacing based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 38640),
    )


_Cd11IfBridgeSpacing_Type.__name__ = "Unsigned32"
_Cd11IfBridgeSpacing_Object = MibTableColumn
cd11IfBridgeSpacing = _Cd11IfBridgeSpacing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 6),
    _Cd11IfBridgeSpacing_Type()
)
cd11IfBridgeSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfBridgeSpacing.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfBridgeSpacing.setUnits("Kilometers")


class _Cd11IfDesiredSsidMaxAssocSta_Type(Unsigned32):
    """Custom type cd11IfDesiredSsidMaxAssocSta based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_Cd11IfDesiredSsidMaxAssocSta_Type.__name__ = "Unsigned32"
_Cd11IfDesiredSsidMaxAssocSta_Object = MibTableColumn
cd11IfDesiredSsidMaxAssocSta = _Cd11IfDesiredSsidMaxAssocSta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 7),
    _Cd11IfDesiredSsidMaxAssocSta_Type()
)
cd11IfDesiredSsidMaxAssocSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfDesiredSsidMaxAssocSta.setStatus("current")


class _Cd11IfAuxiliarySsidLength_Type(Unsigned32):
    """Custom type cd11IfAuxiliarySsidLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cd11IfAuxiliarySsidLength_Type.__name__ = "Unsigned32"
_Cd11IfAuxiliarySsidLength_Object = MibTableColumn
cd11IfAuxiliarySsidLength = _Cd11IfAuxiliarySsidLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 8),
    _Cd11IfAuxiliarySsidLength_Type()
)
cd11IfAuxiliarySsidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfAuxiliarySsidLength.setStatus("current")
_Cd11IfVoipExtensionsEnable_Type = TruthValue
_Cd11IfVoipExtensionsEnable_Object = MibTableColumn
cd11IfVoipExtensionsEnable = _Cd11IfVoipExtensionsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 9),
    _Cd11IfVoipExtensionsEnable_Type()
)
cd11IfVoipExtensionsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfVoipExtensionsEnable.setStatus("current")
_Cd11IfDesiredSsidMicAlgorithm_Type = CDot11IfMicAlgorithm
_Cd11IfDesiredSsidMicAlgorithm_Object = MibTableColumn
cd11IfDesiredSsidMicAlgorithm = _Cd11IfDesiredSsidMicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 10),
    _Cd11IfDesiredSsidMicAlgorithm_Type()
)
cd11IfDesiredSsidMicAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfDesiredSsidMicAlgorithm.setStatus("current")
_Cd11IfDesiredSsidWepPermuteAlg_Type = CDot11IfWepKeyPermuteAlgorithm
_Cd11IfDesiredSsidWepPermuteAlg_Object = MibTableColumn
cd11IfDesiredSsidWepPermuteAlg = _Cd11IfDesiredSsidWepPermuteAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 11),
    _Cd11IfDesiredSsidWepPermuteAlg_Type()
)
cd11IfDesiredSsidWepPermuteAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfDesiredSsidWepPermuteAlg.setStatus("current")


class _Cd11IfWorldMode_Type(Integer32):
    """Custom type cd11IfWorldMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11d", 3),
          ("legacy", 2),
          ("none", 1))
    )


_Cd11IfWorldMode_Type.__name__ = "Integer32"
_Cd11IfWorldMode_Object = MibTableColumn
cd11IfWorldMode = _Cd11IfWorldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 12),
    _Cd11IfWorldMode_Type()
)
cd11IfWorldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfWorldMode.setStatus("current")


class _Cd11IfWorldModeCountry_Type(OctetString):
    """Custom type cd11IfWorldModeCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Cd11IfWorldModeCountry_Type.__name__ = "OctetString"
_Cd11IfWorldModeCountry_Object = MibTableColumn
cd11IfWorldModeCountry = _Cd11IfWorldModeCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 13),
    _Cd11IfWorldModeCountry_Type()
)
cd11IfWorldModeCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfWorldModeCountry.setStatus("current")


class _Cd11IfMobileStationScanParent_Type(TruthValue):
    """Custom type cd11IfMobileStationScanParent based on TruthValue"""


_Cd11IfMobileStationScanParent_Object = MibTableColumn
cd11IfMobileStationScanParent = _Cd11IfMobileStationScanParent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 14),
    _Cd11IfMobileStationScanParent_Type()
)
cd11IfMobileStationScanParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfMobileStationScanParent.setStatus("current")


class _Cd11IfPsPacketForwardEnable_Type(TruthValue):
    """Custom type cd11IfPsPacketForwardEnable based on TruthValue"""


_Cd11IfPsPacketForwardEnable_Object = MibTableColumn
cd11IfPsPacketForwardEnable = _Cd11IfPsPacketForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 15),
    _Cd11IfPsPacketForwardEnable_Type()
)
cd11IfPsPacketForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPsPacketForwardEnable.setStatus("current")


class _Cd11IfMultipleBssidEnable_Type(TruthValue):
    """Custom type cd11IfMultipleBssidEnable based on TruthValue"""


_Cd11IfMultipleBssidEnable_Object = MibTableColumn
cd11IfMultipleBssidEnable = _Cd11IfMultipleBssidEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 16),
    _Cd11IfMultipleBssidEnable_Type()
)
cd11IfMultipleBssidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfMultipleBssidEnable.setStatus("current")


class _Cd11IfMobileStationListIgnore_Type(TruthValue):
    """Custom type cd11IfMobileStationListIgnore based on TruthValue"""


_Cd11IfMobileStationListIgnore_Object = MibTableColumn
cd11IfMobileStationListIgnore = _Cd11IfMobileStationListIgnore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 17),
    _Cd11IfMobileStationListIgnore_Type()
)
cd11IfMobileStationListIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfMobileStationListIgnore.setStatus("current")


class _Cd11IfMobileStationScanChannel_Type(OctetString):
    """Custom type cd11IfMobileStationScanChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Cd11IfMobileStationScanChannel_Type.__name__ = "OctetString"
_Cd11IfMobileStationScanChannel_Object = MibTableColumn
cd11IfMobileStationScanChannel = _Cd11IfMobileStationScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 1, 1, 18),
    _Cd11IfMobileStationScanChannel_Type()
)
cd11IfMobileStationScanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfMobileStationScanChannel.setStatus("current")
_Cd11IfAuthAlgorithmTable_Object = MibTable
cd11IfAuthAlgorithmTable = _Cd11IfAuthAlgorithmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cd11IfAuthAlgorithmTable.setStatus("current")
_Cd11IfAuthAlgorithmEntry_Object = MibTableRow
cd11IfAuthAlgorithmEntry = _Cd11IfAuthAlgorithmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 2, 1)
)
cd11IfAuthAlgorithmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsIndex"),
)
if mibBuilder.loadTexts:
    cd11IfAuthAlgorithmEntry.setStatus("current")
_Cd11IfAuthAlgRequireEap_Type = TruthValue
_Cd11IfAuthAlgRequireEap_Object = MibTableColumn
cd11IfAuthAlgRequireEap = _Cd11IfAuthAlgRequireEap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 2, 1, 1),
    _Cd11IfAuthAlgRequireEap_Type()
)
cd11IfAuthAlgRequireEap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuthAlgRequireEap.setStatus("current")
_Cd11IfAuthAlgRequireMacAddr_Type = TruthValue
_Cd11IfAuthAlgRequireMacAddr_Object = MibTableColumn
cd11IfAuthAlgRequireMacAddr = _Cd11IfAuthAlgRequireMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 2, 1, 2),
    _Cd11IfAuthAlgRequireMacAddr_Type()
)
cd11IfAuthAlgRequireMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuthAlgRequireMacAddr.setStatus("current")
_Cd11IfAuthAlgDefaultVlan_Type = CDot11IfVlanIdOrZero
_Cd11IfAuthAlgDefaultVlan_Object = MibTableColumn
cd11IfAuthAlgDefaultVlan = _Cd11IfAuthAlgDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 2, 1, 3),
    _Cd11IfAuthAlgDefaultVlan_Type()
)
cd11IfAuthAlgDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuthAlgDefaultVlan.setStatus("current")
_Cd11IfAuthAlgEapMethod_Type = SnmpAdminString
_Cd11IfAuthAlgEapMethod_Object = MibTableColumn
cd11IfAuthAlgEapMethod = _Cd11IfAuthAlgEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 2, 1, 4),
    _Cd11IfAuthAlgEapMethod_Type()
)
cd11IfAuthAlgEapMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuthAlgEapMethod.setStatus("current")
_Cd11IfAuthAlgMacAddrMethod_Type = SnmpAdminString
_Cd11IfAuthAlgMacAddrMethod_Object = MibTableColumn
cd11IfAuthAlgMacAddrMethod = _Cd11IfAuthAlgMacAddrMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 2, 1, 5),
    _Cd11IfAuthAlgMacAddrMethod_Type()
)
cd11IfAuthAlgMacAddrMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuthAlgMacAddrMethod.setStatus("current")
_Cd11IfWepDefaultKeysTable_Object = MibTable
cd11IfWepDefaultKeysTable = _Cd11IfWepDefaultKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cd11IfWepDefaultKeysTable.setStatus("current")
_Cd11IfWepDefaultKeysEntry_Object = MibTableRow
cd11IfWepDefaultKeysEntry = _Cd11IfWepDefaultKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 3, 1)
)
cd11IfWepDefaultKeysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfWepDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    cd11IfWepDefaultKeysEntry.setStatus("current")


class _Cd11IfWepDefaultKeyIndex_Type(Unsigned32):
    """Custom type cd11IfWepDefaultKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cd11IfWepDefaultKeyIndex_Type.__name__ = "Unsigned32"
_Cd11IfWepDefaultKeyIndex_Object = MibTableColumn
cd11IfWepDefaultKeyIndex = _Cd11IfWepDefaultKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 3, 1, 1),
    _Cd11IfWepDefaultKeyIndex_Type()
)
cd11IfWepDefaultKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfWepDefaultKeyIndex.setStatus("current")


class _Cd11IfWepDefaultKeyLen_Type(Unsigned32):
    """Custom type cd11IfWepDefaultKeyLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 13),
    )


_Cd11IfWepDefaultKeyLen_Type.__name__ = "Unsigned32"
_Cd11IfWepDefaultKeyLen_Object = MibTableColumn
cd11IfWepDefaultKeyLen = _Cd11IfWepDefaultKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 3, 1, 2),
    _Cd11IfWepDefaultKeyLen_Type()
)
cd11IfWepDefaultKeyLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfWepDefaultKeyLen.setStatus("current")
_Cd11IfWepDefaultKeyValue_Type = WepKeyType128
_Cd11IfWepDefaultKeyValue_Object = MibTableColumn
cd11IfWepDefaultKeyValue = _Cd11IfWepDefaultKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 3, 1, 3),
    _Cd11IfWepDefaultKeyValue_Type()
)
cd11IfWepDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfWepDefaultKeyValue.setStatus("current")
_Cd11IfDesiredBssTable_Object = MibTable
cd11IfDesiredBssTable = _Cd11IfDesiredBssTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cd11IfDesiredBssTable.setStatus("current")
_Cd11IfDesiredBssEntry_Object = MibTableRow
cd11IfDesiredBssEntry = _Cd11IfDesiredBssEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 5, 1)
)
cd11IfDesiredBssEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfDesiredBssIndex"),
)
if mibBuilder.loadTexts:
    cd11IfDesiredBssEntry.setStatus("current")


class _Cd11IfDesiredBssIndex_Type(Unsigned32):
    """Custom type cd11IfDesiredBssIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cd11IfDesiredBssIndex_Type.__name__ = "Unsigned32"
_Cd11IfDesiredBssIndex_Object = MibTableColumn
cd11IfDesiredBssIndex = _Cd11IfDesiredBssIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 5, 1, 1),
    _Cd11IfDesiredBssIndex_Type()
)
cd11IfDesiredBssIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfDesiredBssIndex.setStatus("current")
_Cd11IfDesiredBssAddr_Type = MacAddress
_Cd11IfDesiredBssAddr_Object = MibTableColumn
cd11IfDesiredBssAddr = _Cd11IfDesiredBssAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 5, 1, 2),
    _Cd11IfDesiredBssAddr_Type()
)
cd11IfDesiredBssAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfDesiredBssAddr.setStatus("current")
_Cd11IfAuxSsidTable_Object = MibTable
cd11IfAuxSsidTable = _Cd11IfAuxSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cd11IfAuxSsidTable.setStatus("current")
_Cd11IfAuxSsidEntry_Object = MibTableRow
cd11IfAuxSsidEntry = _Cd11IfAuxSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6, 1)
)
cd11IfAuxSsidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfAuxSsidIndex"),
)
if mibBuilder.loadTexts:
    cd11IfAuxSsidEntry.setStatus("current")


class _Cd11IfAuxSsidIndex_Type(Unsigned32):
    """Custom type cd11IfAuxSsidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cd11IfAuxSsidIndex_Type.__name__ = "Unsigned32"
_Cd11IfAuxSsidIndex_Object = MibTableColumn
cd11IfAuxSsidIndex = _Cd11IfAuxSsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6, 1, 1),
    _Cd11IfAuxSsidIndex_Type()
)
cd11IfAuxSsidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfAuxSsidIndex.setStatus("current")


class _Cd11IfAuxSsid_Type(OctetString):
    """Custom type cd11IfAuxSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cd11IfAuxSsid_Type.__name__ = "OctetString"
_Cd11IfAuxSsid_Object = MibTableColumn
cd11IfAuxSsid = _Cd11IfAuxSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6, 1, 2),
    _Cd11IfAuxSsid_Type()
)
cd11IfAuxSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsid.setStatus("current")
_Cd11IfAuxSsidBroadcastSsid_Type = TruthValue
_Cd11IfAuxSsidBroadcastSsid_Object = MibTableColumn
cd11IfAuxSsidBroadcastSsid = _Cd11IfAuxSsidBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6, 1, 3),
    _Cd11IfAuxSsidBroadcastSsid_Type()
)
cd11IfAuxSsidBroadcastSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidBroadcastSsid.setStatus("current")


class _Cd11IfAuxSsidMaxAssocSta_Type(Unsigned32):
    """Custom type cd11IfAuxSsidMaxAssocSta based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_Cd11IfAuxSsidMaxAssocSta_Type.__name__ = "Unsigned32"
_Cd11IfAuxSsidMaxAssocSta_Object = MibTableColumn
cd11IfAuxSsidMaxAssocSta = _Cd11IfAuxSsidMaxAssocSta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6, 1, 4),
    _Cd11IfAuxSsidMaxAssocSta_Type()
)
cd11IfAuxSsidMaxAssocSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidMaxAssocSta.setStatus("current")
_Cd11IfAuxSsidMicAlgorithm_Type = CDot11IfMicAlgorithm
_Cd11IfAuxSsidMicAlgorithm_Object = MibTableColumn
cd11IfAuxSsidMicAlgorithm = _Cd11IfAuxSsidMicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6, 1, 5),
    _Cd11IfAuxSsidMicAlgorithm_Type()
)
cd11IfAuxSsidMicAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidMicAlgorithm.setStatus("current")
_Cd11IfAuxSsidWepPermuteAlg_Type = CDot11IfWepKeyPermuteAlgorithm
_Cd11IfAuxSsidWepPermuteAlg_Object = MibTableColumn
cd11IfAuxSsidWepPermuteAlg = _Cd11IfAuxSsidWepPermuteAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 6, 1, 6),
    _Cd11IfAuxSsidWepPermuteAlg_Type()
)
cd11IfAuxSsidWepPermuteAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidWepPermuteAlg.setStatus("current")
_Cd11IfAuxSsidAuthAlgTable_Object = MibTable
cd11IfAuxSsidAuthAlgTable = _Cd11IfAuxSsidAuthAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgTable.setStatus("current")
_Cd11IfAuxSsidAuthAlgEntry_Object = MibTableRow
cd11IfAuxSsidAuthAlgEntry = _Cd11IfAuxSsidAuthAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7, 1)
)
cd11IfAuxSsidAuthAlgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfAuxSsidIndex"),
    (0, "IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsIndex"),
)
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgEntry.setStatus("current")
_Cd11IfAuxSsidAuthAlgEnable_Type = TruthValue
_Cd11IfAuxSsidAuthAlgEnable_Object = MibTableColumn
cd11IfAuxSsidAuthAlgEnable = _Cd11IfAuxSsidAuthAlgEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7, 1, 1),
    _Cd11IfAuxSsidAuthAlgEnable_Type()
)
cd11IfAuxSsidAuthAlgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgEnable.setStatus("current")
_Cd11IfAuxSsidAuthAlgRequireEap_Type = TruthValue
_Cd11IfAuxSsidAuthAlgRequireEap_Object = MibTableColumn
cd11IfAuxSsidAuthAlgRequireEap = _Cd11IfAuxSsidAuthAlgRequireEap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7, 1, 2),
    _Cd11IfAuxSsidAuthAlgRequireEap_Type()
)
cd11IfAuxSsidAuthAlgRequireEap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgRequireEap.setStatus("current")
_Cd11IfAuxSsidAuthAlgRequireMac_Type = TruthValue
_Cd11IfAuxSsidAuthAlgRequireMac_Object = MibTableColumn
cd11IfAuxSsidAuthAlgRequireMac = _Cd11IfAuxSsidAuthAlgRequireMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7, 1, 3),
    _Cd11IfAuxSsidAuthAlgRequireMac_Type()
)
cd11IfAuxSsidAuthAlgRequireMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgRequireMac.setStatus("current")
_Cd11IfAuxSsidAuthAlgDefaultVlan_Type = CDot11IfVlanIdOrZero
_Cd11IfAuxSsidAuthAlgDefaultVlan_Object = MibTableColumn
cd11IfAuxSsidAuthAlgDefaultVlan = _Cd11IfAuxSsidAuthAlgDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7, 1, 4),
    _Cd11IfAuxSsidAuthAlgDefaultVlan_Type()
)
cd11IfAuxSsidAuthAlgDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgDefaultVlan.setStatus("current")
_Cd11IfAuxSsidAuthAlgEapMethod_Type = SnmpAdminString
_Cd11IfAuxSsidAuthAlgEapMethod_Object = MibTableColumn
cd11IfAuxSsidAuthAlgEapMethod = _Cd11IfAuxSsidAuthAlgEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7, 1, 5),
    _Cd11IfAuxSsidAuthAlgEapMethod_Type()
)
cd11IfAuxSsidAuthAlgEapMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgEapMethod.setStatus("current")
_Cd11IfAuxSsidAuthAlgMacMethod_Type = SnmpAdminString
_Cd11IfAuxSsidAuthAlgMacMethod_Object = MibTableColumn
cd11IfAuxSsidAuthAlgMacMethod = _Cd11IfAuxSsidAuthAlgMacMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 7, 1, 6),
    _Cd11IfAuxSsidAuthAlgMacMethod_Type()
)
cd11IfAuxSsidAuthAlgMacMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAuxSsidAuthAlgMacMethod.setStatus("current")
_Cd11IfAssignedAidTable_Object = MibTable
cd11IfAssignedAidTable = _Cd11IfAssignedAidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cd11IfAssignedAidTable.setStatus("current")
_Cd11IfAssignedAidEntry_Object = MibTableRow
cd11IfAssignedAidEntry = _Cd11IfAssignedAidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 8, 1)
)
cd11IfAssignedAidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfAssignedAid"),
)
if mibBuilder.loadTexts:
    cd11IfAssignedAidEntry.setStatus("current")


class _Cd11IfAssignedAid_Type(Unsigned32):
    """Custom type cd11IfAssignedAid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2007),
    )


_Cd11IfAssignedAid_Type.__name__ = "Unsigned32"
_Cd11IfAssignedAid_Object = MibTableColumn
cd11IfAssignedAid = _Cd11IfAssignedAid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 8, 1, 1),
    _Cd11IfAssignedAid_Type()
)
cd11IfAssignedAid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfAssignedAid.setStatus("current")
_Cd11IfAssignedSta_Type = MacAddress
_Cd11IfAssignedSta_Object = MibTableColumn
cd11IfAssignedSta = _Cd11IfAssignedSta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 8, 1, 2),
    _Cd11IfAssignedSta_Type()
)
cd11IfAssignedSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfAssignedSta.setStatus("current")
_Cd11IfVlanEncryptKeyTable_Object = MibTable
cd11IfVlanEncryptKeyTable = _Cd11IfVlanEncryptKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyTable.setStatus("current")
_Cd11IfVlanEncryptKeyEntry_Object = MibTableRow
cd11IfVlanEncryptKeyEntry = _Cd11IfVlanEncryptKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9, 1)
)
cd11IfVlanEncryptKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfVlanId"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyIndex"),
)
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyEntry.setStatus("current")
_Cd11IfVlanId_Type = CDot11IfVlanIdOrZero
_Cd11IfVlanId_Object = MibTableColumn
cd11IfVlanId = _Cd11IfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9, 1, 1),
    _Cd11IfVlanId_Type()
)
cd11IfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfVlanId.setStatus("current")


class _Cd11IfVlanEncryptKeyIndex_Type(Unsigned32):
    """Custom type cd11IfVlanEncryptKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cd11IfVlanEncryptKeyIndex_Type.__name__ = "Unsigned32"
_Cd11IfVlanEncryptKeyIndex_Object = MibTableColumn
cd11IfVlanEncryptKeyIndex = _Cd11IfVlanEncryptKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9, 1, 2),
    _Cd11IfVlanEncryptKeyIndex_Type()
)
cd11IfVlanEncryptKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyIndex.setStatus("current")


class _Cd11IfVlanEncryptKeyLen_Type(Unsigned32):
    """Custom type cd11IfVlanEncryptKeyLen based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_Cd11IfVlanEncryptKeyLen_Type.__name__ = "Unsigned32"
_Cd11IfVlanEncryptKeyLen_Object = MibTableColumn
cd11IfVlanEncryptKeyLen = _Cd11IfVlanEncryptKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9, 1, 3),
    _Cd11IfVlanEncryptKeyLen_Type()
)
cd11IfVlanEncryptKeyLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyLen.setStatus("current")
_Cd11IfVlanEncryptKeyValue_Type = WepKeyType128
_Cd11IfVlanEncryptKeyValue_Object = MibTableColumn
cd11IfVlanEncryptKeyValue = _Cd11IfVlanEncryptKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9, 1, 4),
    _Cd11IfVlanEncryptKeyValue_Type()
)
cd11IfVlanEncryptKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyValue.setStatus("current")
_Cd11IfVlanEncryptKeyStatus_Type = RowStatus
_Cd11IfVlanEncryptKeyStatus_Object = MibTableColumn
cd11IfVlanEncryptKeyStatus = _Cd11IfVlanEncryptKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9, 1, 5),
    _Cd11IfVlanEncryptKeyStatus_Type()
)
cd11IfVlanEncryptKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyStatus.setStatus("current")
_Cd11IfVlanEncryptKeyTransmit_Type = TruthValue
_Cd11IfVlanEncryptKeyTransmit_Object = MibTableColumn
cd11IfVlanEncryptKeyTransmit = _Cd11IfVlanEncryptKeyTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 9, 1, 6),
    _Cd11IfVlanEncryptKeyTransmit_Type()
)
cd11IfVlanEncryptKeyTransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyTransmit.setStatus("current")
_Cd11IfVlanSecurityTable_Object = MibTable
cd11IfVlanSecurityTable = _Cd11IfVlanSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cd11IfVlanSecurityTable.setStatus("current")
_Cd11IfVlanSecurityEntry_Object = MibTableRow
cd11IfVlanSecurityEntry = _Cd11IfVlanSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1)
)
cd11IfVlanSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfVlanSecurityVlanId"),
)
if mibBuilder.loadTexts:
    cd11IfVlanSecurityEntry.setStatus("current")
_Cd11IfVlanSecurityVlanId_Type = CDot11IfVlanIdOrZero
_Cd11IfVlanSecurityVlanId_Object = MibTableColumn
cd11IfVlanSecurityVlanId = _Cd11IfVlanSecurityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 1),
    _Cd11IfVlanSecurityVlanId_Type()
)
cd11IfVlanSecurityVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfVlanSecurityVlanId.setStatus("current")
_Cd11IfVlanSecurityVlanEnabled_Type = TruthValue
_Cd11IfVlanSecurityVlanEnabled_Object = MibTableColumn
cd11IfVlanSecurityVlanEnabled = _Cd11IfVlanSecurityVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 2),
    _Cd11IfVlanSecurityVlanEnabled_Type()
)
cd11IfVlanSecurityVlanEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanSecurityVlanEnabled.setStatus("current")


class _Cd11IfVlanBcastKeyChangeInterval_Type(Unsigned32):
    """Custom type cd11IfVlanBcastKeyChangeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000000),
    )


_Cd11IfVlanBcastKeyChangeInterval_Type.__name__ = "Unsigned32"
_Cd11IfVlanBcastKeyChangeInterval_Object = MibTableColumn
cd11IfVlanBcastKeyChangeInterval = _Cd11IfVlanBcastKeyChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 3),
    _Cd11IfVlanBcastKeyChangeInterval_Type()
)
cd11IfVlanBcastKeyChangeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanBcastKeyChangeInterval.setStatus("current")


class _Cd11IfVlanBcastKeyCapabilChange_Type(TruthValue):
    """Custom type cd11IfVlanBcastKeyCapabilChange based on TruthValue"""


_Cd11IfVlanBcastKeyCapabilChange_Object = MibTableColumn
cd11IfVlanBcastKeyCapabilChange = _Cd11IfVlanBcastKeyCapabilChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 4),
    _Cd11IfVlanBcastKeyCapabilChange_Type()
)
cd11IfVlanBcastKeyCapabilChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanBcastKeyCapabilChange.setStatus("current")


class _Cd11IfVlanBcastKeyClientLeave_Type(TruthValue):
    """Custom type cd11IfVlanBcastKeyClientLeave based on TruthValue"""


_Cd11IfVlanBcastKeyClientLeave_Object = MibTableColumn
cd11IfVlanBcastKeyClientLeave = _Cd11IfVlanBcastKeyClientLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 5),
    _Cd11IfVlanBcastKeyClientLeave_Type()
)
cd11IfVlanBcastKeyClientLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanBcastKeyClientLeave.setStatus("current")
_Cd11IfVlanSecurityCiphers_Type = CDot11IfCipherType
_Cd11IfVlanSecurityCiphers_Object = MibTableColumn
cd11IfVlanSecurityCiphers = _Cd11IfVlanSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 6),
    _Cd11IfVlanSecurityCiphers_Type()
)
cd11IfVlanSecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanSecurityCiphers.setStatus("current")
_Cd11IfVlanSecurityRowStatus_Type = RowStatus
_Cd11IfVlanSecurityRowStatus_Object = MibTableColumn
cd11IfVlanSecurityRowStatus = _Cd11IfVlanSecurityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 7),
    _Cd11IfVlanSecurityRowStatus_Type()
)
cd11IfVlanSecurityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanSecurityRowStatus.setStatus("current")


class _Cd11IfVlanEncryptionMode_Type(Integer32):
    """Custom type cd11IfVlanEncryptionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("wep", 2))
    )


_Cd11IfVlanEncryptionMode_Type.__name__ = "Integer32"
_Cd11IfVlanEncryptionMode_Object = MibTableColumn
cd11IfVlanEncryptionMode = _Cd11IfVlanEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 8),
    _Cd11IfVlanEncryptionMode_Type()
)
cd11IfVlanEncryptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanEncryptionMode.setStatus("current")


class _Cd11IfVlanWepEncryptOptions_Type(Integer32):
    """Custom type cd11IfVlanWepEncryptOptions based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 1),
          ("optional", 2))
    )


_Cd11IfVlanWepEncryptOptions_Type.__name__ = "Integer32"
_Cd11IfVlanWepEncryptOptions_Object = MibTableColumn
cd11IfVlanWepEncryptOptions = _Cd11IfVlanWepEncryptOptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 9),
    _Cd11IfVlanWepEncryptOptions_Type()
)
cd11IfVlanWepEncryptOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanWepEncryptOptions.setStatus("current")


class _Cd11IfVlanWepEncryptMic_Type(TruthValue):
    """Custom type cd11IfVlanWepEncryptMic based on TruthValue"""


_Cd11IfVlanWepEncryptMic_Object = MibTableColumn
cd11IfVlanWepEncryptMic = _Cd11IfVlanWepEncryptMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 10),
    _Cd11IfVlanWepEncryptMic_Type()
)
cd11IfVlanWepEncryptMic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanWepEncryptMic.setStatus("current")


class _Cd11IfVlanWepEncryptKeyHashing_Type(TruthValue):
    """Custom type cd11IfVlanWepEncryptKeyHashing based on TruthValue"""


_Cd11IfVlanWepEncryptKeyHashing_Object = MibTableColumn
cd11IfVlanWepEncryptKeyHashing = _Cd11IfVlanWepEncryptKeyHashing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 11),
    _Cd11IfVlanWepEncryptKeyHashing_Type()
)
cd11IfVlanWepEncryptKeyHashing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanWepEncryptKeyHashing.setStatus("current")


class _Cd11IfVlanPsPacketForwardEnable_Type(TruthValue):
    """Custom type cd11IfVlanPsPacketForwardEnable based on TruthValue"""


_Cd11IfVlanPsPacketForwardEnable_Object = MibTableColumn
cd11IfVlanPsPacketForwardEnable = _Cd11IfVlanPsPacketForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 10, 1, 12),
    _Cd11IfVlanPsPacketForwardEnable_Type()
)
cd11IfVlanPsPacketForwardEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfVlanPsPacketForwardEnable.setStatus("current")
_Cd11IfRadioMonitoringTable_Object = MibTable
cd11IfRadioMonitoringTable = _Cd11IfRadioMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cd11IfRadioMonitoringTable.setStatus("current")
_Cd11IfRadioMonitoringEntry_Object = MibTableRow
cd11IfRadioMonitoringEntry = _Cd11IfRadioMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 11, 1)
)
cd11IfRadioMonitoringEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRemoteRadioMacAddr"),
)
if mibBuilder.loadTexts:
    cd11IfRadioMonitoringEntry.setStatus("current")
_Cd11IfRemoteRadioMacAddr_Type = MacAddress
_Cd11IfRemoteRadioMacAddr_Object = MibTableColumn
cd11IfRemoteRadioMacAddr = _Cd11IfRemoteRadioMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 11, 1, 1),
    _Cd11IfRemoteRadioMacAddr_Type()
)
cd11IfRemoteRadioMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfRemoteRadioMacAddr.setStatus("current")


class _Cd11IfRadioMonitorPollingFreq_Type(Unsigned32):
    """Custom type cd11IfRadioMonitorPollingFreq based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Cd11IfRadioMonitorPollingFreq_Type.__name__ = "Unsigned32"
_Cd11IfRadioMonitorPollingFreq_Object = MibTableColumn
cd11IfRadioMonitorPollingFreq = _Cd11IfRadioMonitorPollingFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 11, 1, 2),
    _Cd11IfRadioMonitorPollingFreq_Type()
)
cd11IfRadioMonitorPollingFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfRadioMonitorPollingFreq.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfRadioMonitorPollingFreq.setUnits("seconds")


class _Cd11IfRadioMonitorPollingTimeOut_Type(Unsigned32):
    """Custom type cd11IfRadioMonitorPollingTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Cd11IfRadioMonitorPollingTimeOut_Type.__name__ = "Unsigned32"
_Cd11IfRadioMonitorPollingTimeOut_Object = MibTableColumn
cd11IfRadioMonitorPollingTimeOut = _Cd11IfRadioMonitorPollingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 11, 1, 3),
    _Cd11IfRadioMonitorPollingTimeOut_Type()
)
cd11IfRadioMonitorPollingTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfRadioMonitorPollingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfRadioMonitorPollingTimeOut.setUnits("seconds")


class _Cd11IfLocalRadioMonitorStatus_Type(Integer32):
    """Custom type cd11IfLocalRadioMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 3),
          ("monitor", 2))
    )


_Cd11IfLocalRadioMonitorStatus_Type.__name__ = "Integer32"
_Cd11IfLocalRadioMonitorStatus_Object = MibTableColumn
cd11IfLocalRadioMonitorStatus = _Cd11IfLocalRadioMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 11, 1, 4),
    _Cd11IfLocalRadioMonitorStatus_Type()
)
cd11IfLocalRadioMonitorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfLocalRadioMonitorStatus.setStatus("current")
_Cd11IfRadioMonitorRowStatus_Type = RowStatus
_Cd11IfRadioMonitorRowStatus_Object = MibTableColumn
cd11IfRadioMonitorRowStatus = _Cd11IfRadioMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 11, 1, 5),
    _Cd11IfRadioMonitorRowStatus_Type()
)
cd11IfRadioMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cd11IfRadioMonitorRowStatus.setStatus("current")
_Cd11IfDot11UpgradeStatusTable_Object = MibTable
cd11IfDot11UpgradeStatusTable = _Cd11IfDot11UpgradeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cd11IfDot11UpgradeStatusTable.setStatus("current")
_Cd11IfDot11UpgradeStatusEntry_Object = MibTableRow
cd11IfDot11UpgradeStatusEntry = _Cd11IfDot11UpgradeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 12, 1)
)
cd11IfDot11UpgradeStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfDot11UpgradeStatusEntry.setStatus("current")
_Cd11IfDot11UpgradeStatus_Type = Cd11IfDot11UpgradeStatus
_Cd11IfDot11UpgradeStatus_Object = MibTableColumn
cd11IfDot11UpgradeStatus = _Cd11IfDot11UpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 1, 12, 1, 1),
    _Cd11IfDot11UpgradeStatus_Type()
)
cd11IfDot11UpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfDot11UpgradeStatus.setStatus("current")
_Cd11IfPhyConfig_ObjectIdentity = ObjectIdentity
cd11IfPhyConfig = _Cd11IfPhyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2)
)
_Cd11IfPhyOperationTable_Object = MibTable
cd11IfPhyOperationTable = _Cd11IfPhyOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cd11IfPhyOperationTable.setStatus("current")
_Cd11IfPhyOperationEntry_Object = MibTableRow
cd11IfPhyOperationEntry = _Cd11IfPhyOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1)
)
cd11IfPhyOperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfPhyOperationEntry.setStatus("current")


class _Cd11IfCurrentCarrierSet_Type(Integer32):
    """Custom type cd11IfCurrentCarrierSet based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("australia", 8),
          ("belgium", 5),
          ("canada", 7),
          ("china", 16),
          ("china5GHz", 22),
          ("chnIreAus5GHzUNI3", 18),
          ("europe", 1),
          ("europe5GHz", 12),
          ("france", 4),
          ("hkNZ5GHzUNI3", 19),
          ("israel", 6),
          ("israel5GhzUNI12", 26),
          ("japan", 2),
          ("japan5GHz", 13),
          ("japan5GHzUNI1", 28),
          ("japan5GHzUNI12", 24),
          ("japanWide", 9),
          ("korea5GHzUNI123E", 23),
          ("korea5GHzUNI3", 20),
          ("mexAusNZ5GHz", 21),
          ("northAmer5GHzUNI3", 17),
          ("singapore5GHz", 14),
          ("spain", 3),
          ("taiwan5GHz", 15),
          ("taiwan5GHzUNI23E", 25),
          ("usa", 0),
          ("usa5GHz", 11),
          ("usaFCC49PS", 27),
          ("world", 10))
    )


_Cd11IfCurrentCarrierSet_Type.__name__ = "Integer32"
_Cd11IfCurrentCarrierSet_Object = MibTableColumn
cd11IfCurrentCarrierSet = _Cd11IfCurrentCarrierSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 1),
    _Cd11IfCurrentCarrierSet_Type()
)
cd11IfCurrentCarrierSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfCurrentCarrierSet.setStatus("current")


class _Cd11IfModulationType_Type(Integer32):
    """Custom type cd11IfModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mok", 2),
          ("standard", 1))
    )


_Cd11IfModulationType_Type.__name__ = "Integer32"
_Cd11IfModulationType_Object = MibTableColumn
cd11IfModulationType = _Cd11IfModulationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 2),
    _Cd11IfModulationType_Type()
)
cd11IfModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfModulationType.setStatus("current")


class _Cd11IfPreambleType_Type(Integer32):
    """Custom type cd11IfPreambleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_Cd11IfPreambleType_Type.__name__ = "Integer32"
_Cd11IfPreambleType_Object = MibTableColumn
cd11IfPreambleType = _Cd11IfPreambleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 3),
    _Cd11IfPreambleType_Type()
)
cd11IfPreambleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPreambleType.setStatus("current")
_Cd11IfDomainCapabilitySet_Type = Integer32
_Cd11IfDomainCapabilitySet_Object = MibTableColumn
cd11IfDomainCapabilitySet = _Cd11IfDomainCapabilitySet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 4),
    _Cd11IfDomainCapabilitySet_Type()
)
cd11IfDomainCapabilitySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfDomainCapabilitySet.setStatus("current")


class _Cd11IfPhyBasicRateSet_Type(OctetString):
    """Custom type cd11IfPhyBasicRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_Cd11IfPhyBasicRateSet_Type.__name__ = "OctetString"
_Cd11IfPhyBasicRateSet_Object = MibTableColumn
cd11IfPhyBasicRateSet = _Cd11IfPhyBasicRateSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 5),
    _Cd11IfPhyBasicRateSet_Type()
)
cd11IfPhyBasicRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPhyBasicRateSet.setStatus("current")


class _Cd11IfPhyMacSpecification_Type(Integer32):
    """Custom type cd11IfPhyMacSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11g", 3))
    )


_Cd11IfPhyMacSpecification_Type.__name__ = "Integer32"
_Cd11IfPhyMacSpecification_Object = MibTableColumn
cd11IfPhyMacSpecification = _Cd11IfPhyMacSpecification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 6),
    _Cd11IfPhyMacSpecification_Type()
)
cd11IfPhyMacSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfPhyMacSpecification.setStatus("current")
_Cd11IfPhyConcatenation_Type = Integer32
_Cd11IfPhyConcatenation_Object = MibTableColumn
cd11IfPhyConcatenation = _Cd11IfPhyConcatenation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 7),
    _Cd11IfPhyConcatenation_Type()
)
cd11IfPhyConcatenation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPhyConcatenation.setStatus("current")


class _Cd11IfPhyNativePowerUseStandard_Type(TruthValue):
    """Custom type cd11IfPhyNativePowerUseStandard based on TruthValue"""


_Cd11IfPhyNativePowerUseStandard_Object = MibTableColumn
cd11IfPhyNativePowerUseStandard = _Cd11IfPhyNativePowerUseStandard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 1, 1, 8),
    _Cd11IfPhyNativePowerUseStandard_Type()
)
cd11IfPhyNativePowerUseStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPhyNativePowerUseStandard.setStatus("current")
_Cd11IfPhyFhssTable_Object = MibTable
cd11IfPhyFhssTable = _Cd11IfPhyFhssTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cd11IfPhyFhssTable.setStatus("current")
_Cd11IfPhyFhssEntry_Object = MibTableRow
cd11IfPhyFhssEntry = _Cd11IfPhyFhssEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 4, 1)
)
cd11IfPhyFhssEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfPhyFhssEntry.setStatus("current")


class _Cd11IfPhyFhssMaxCompatibleRate_Type(Integer32):
    """Custom type cd11IfPhyFhssMaxCompatibleRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Cd11IfPhyFhssMaxCompatibleRate_Type.__name__ = "Integer32"
_Cd11IfPhyFhssMaxCompatibleRate_Object = MibTableColumn
cd11IfPhyFhssMaxCompatibleRate = _Cd11IfPhyFhssMaxCompatibleRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 4, 1, 1),
    _Cd11IfPhyFhssMaxCompatibleRate_Type()
)
cd11IfPhyFhssMaxCompatibleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPhyFhssMaxCompatibleRate.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfPhyFhssMaxCompatibleRate.setUnits("500 Kb per second")
_Cd11IfPhyDsssTable_Object = MibTable
cd11IfPhyDsssTable = _Cd11IfPhyDsssTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cd11IfPhyDsssTable.setStatus("current")
_Cd11IfPhyDsssEntry_Object = MibTableRow
cd11IfPhyDsssEntry = _Cd11IfPhyDsssEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 5, 1)
)
cd11IfPhyDsssEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfPhyDsssEntry.setStatus("current")


class _Cd11IfPhyDsssMaxCompatibleRate_Type(Integer32):
    """Custom type cd11IfPhyDsssMaxCompatibleRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Cd11IfPhyDsssMaxCompatibleRate_Type.__name__ = "Integer32"
_Cd11IfPhyDsssMaxCompatibleRate_Object = MibTableColumn
cd11IfPhyDsssMaxCompatibleRate = _Cd11IfPhyDsssMaxCompatibleRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 5, 1, 1),
    _Cd11IfPhyDsssMaxCompatibleRate_Type()
)
cd11IfPhyDsssMaxCompatibleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPhyDsssMaxCompatibleRate.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfPhyDsssMaxCompatibleRate.setUnits("500 Kb per second")
_Cd11IfPhyDsssChannelAutoEnable_Type = TruthValue
_Cd11IfPhyDsssChannelAutoEnable_Object = MibTableColumn
cd11IfPhyDsssChannelAutoEnable = _Cd11IfPhyDsssChannelAutoEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 5, 1, 2),
    _Cd11IfPhyDsssChannelAutoEnable_Type()
)
cd11IfPhyDsssChannelAutoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfPhyDsssChannelAutoEnable.setStatus("current")


class _Cd11IfPhyDsssCurrentChannel_Type(Integer32):
    """Custom type cd11IfPhyDsssCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
    )


_Cd11IfPhyDsssCurrentChannel_Type.__name__ = "Integer32"
_Cd11IfPhyDsssCurrentChannel_Object = MibTableColumn
cd11IfPhyDsssCurrentChannel = _Cd11IfPhyDsssCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 5, 1, 3),
    _Cd11IfPhyDsssCurrentChannel_Type()
)
cd11IfPhyDsssCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfPhyDsssCurrentChannel.setStatus("current")
_Cd11IfSuppDataRatesPrivacyTable_Object = MibTable
cd11IfSuppDataRatesPrivacyTable = _Cd11IfSuppDataRatesPrivacyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cd11IfSuppDataRatesPrivacyTable.setStatus("current")
_Cd11IfSuppDataRatesPrivacyEntry_Object = MibTableRow
cd11IfSuppDataRatesPrivacyEntry = _Cd11IfSuppDataRatesPrivacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 11, 1)
)
cd11IfSuppDataRatesPrivacyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfSuppDataRatesPrivacyIndex"),
)
if mibBuilder.loadTexts:
    cd11IfSuppDataRatesPrivacyEntry.setStatus("current")


class _Cd11IfSuppDataRatesPrivacyIndex_Type(Integer32):
    """Custom type cd11IfSuppDataRatesPrivacyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cd11IfSuppDataRatesPrivacyIndex_Type.__name__ = "Integer32"
_Cd11IfSuppDataRatesPrivacyIndex_Object = MibTableColumn
cd11IfSuppDataRatesPrivacyIndex = _Cd11IfSuppDataRatesPrivacyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 11, 1, 1),
    _Cd11IfSuppDataRatesPrivacyIndex_Type()
)
cd11IfSuppDataRatesPrivacyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfSuppDataRatesPrivacyIndex.setStatus("current")


class _Cd11IfSuppDataRatesPrivacyValue_Type(Integer32):
    """Custom type cd11IfSuppDataRatesPrivacyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_Cd11IfSuppDataRatesPrivacyValue_Type.__name__ = "Integer32"
_Cd11IfSuppDataRatesPrivacyValue_Object = MibTableColumn
cd11IfSuppDataRatesPrivacyValue = _Cd11IfSuppDataRatesPrivacyValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 11, 1, 2),
    _Cd11IfSuppDataRatesPrivacyValue_Type()
)
cd11IfSuppDataRatesPrivacyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfSuppDataRatesPrivacyValue.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfSuppDataRatesPrivacyValue.setUnits("500 Kb per second")
_Cd11IfSuppDataRatesPrivacyEnabl_Type = TruthValue
_Cd11IfSuppDataRatesPrivacyEnabl_Object = MibTableColumn
cd11IfSuppDataRatesPrivacyEnabl = _Cd11IfSuppDataRatesPrivacyEnabl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 11, 1, 3),
    _Cd11IfSuppDataRatesPrivacyEnabl_Type()
)
cd11IfSuppDataRatesPrivacyEnabl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfSuppDataRatesPrivacyEnabl.setStatus("current")
_Cd11IfChanSelectTable_Object = MibTable
cd11IfChanSelectTable = _Cd11IfChanSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cd11IfChanSelectTable.setStatus("current")
_Cd11IfChanSelectEntry_Object = MibTableRow
cd11IfChanSelectEntry = _Cd11IfChanSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 12, 1)
)
cd11IfChanSelectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfChanSelectChannel"),
)
if mibBuilder.loadTexts:
    cd11IfChanSelectEntry.setStatus("current")


class _Cd11IfChanSelectChannel_Type(Integer32):
    """Custom type cd11IfChanSelectChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
    )


_Cd11IfChanSelectChannel_Type.__name__ = "Integer32"
_Cd11IfChanSelectChannel_Object = MibTableColumn
cd11IfChanSelectChannel = _Cd11IfChanSelectChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 12, 1, 1),
    _Cd11IfChanSelectChannel_Type()
)
cd11IfChanSelectChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfChanSelectChannel.setStatus("current")
_Cd11IfChanSelectEnable_Type = TruthValue
_Cd11IfChanSelectEnable_Object = MibTableColumn
cd11IfChanSelectEnable = _Cd11IfChanSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 12, 1, 2),
    _Cd11IfChanSelectEnable_Type()
)
cd11IfChanSelectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfChanSelectEnable.setStatus("current")
_Cd11IfClientTxPowerTable_Object = MibTable
cd11IfClientTxPowerTable = _Cd11IfClientTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cd11IfClientTxPowerTable.setStatus("current")
_Cd11IfClientTxPowerEntry_Object = MibTableRow
cd11IfClientTxPowerEntry = _Cd11IfClientTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1)
)
cd11IfClientTxPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfClientTxPowerEntry.setStatus("current")


class _Cd11IfClientNumberTxPowerLevels_Type(Integer32):
    """Custom type cd11IfClientNumberTxPowerLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cd11IfClientNumberTxPowerLevels_Type.__name__ = "Integer32"
_Cd11IfClientNumberTxPowerLevels_Object = MibTableColumn
cd11IfClientNumberTxPowerLevels = _Cd11IfClientNumberTxPowerLevels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 1),
    _Cd11IfClientNumberTxPowerLevels_Type()
)
cd11IfClientNumberTxPowerLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientNumberTxPowerLevels.setStatus("current")


class _Cd11IfClientTxPowerLevel1_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel1_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel1_Object = MibTableColumn
cd11IfClientTxPowerLevel1 = _Cd11IfClientTxPowerLevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 2),
    _Cd11IfClientTxPowerLevel1_Type()
)
cd11IfClientTxPowerLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel1.setStatus("current")


class _Cd11IfClientTxPowerLevel2_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel2_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel2_Object = MibTableColumn
cd11IfClientTxPowerLevel2 = _Cd11IfClientTxPowerLevel2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 3),
    _Cd11IfClientTxPowerLevel2_Type()
)
cd11IfClientTxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel2.setStatus("current")


class _Cd11IfClientTxPowerLevel3_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel3_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel3_Object = MibTableColumn
cd11IfClientTxPowerLevel3 = _Cd11IfClientTxPowerLevel3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 4),
    _Cd11IfClientTxPowerLevel3_Type()
)
cd11IfClientTxPowerLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel3.setStatus("current")


class _Cd11IfClientTxPowerLevel4_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel4_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel4_Object = MibTableColumn
cd11IfClientTxPowerLevel4 = _Cd11IfClientTxPowerLevel4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 5),
    _Cd11IfClientTxPowerLevel4_Type()
)
cd11IfClientTxPowerLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel4.setStatus("current")


class _Cd11IfClientTxPowerLevel5_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel5_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel5_Object = MibTableColumn
cd11IfClientTxPowerLevel5 = _Cd11IfClientTxPowerLevel5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 6),
    _Cd11IfClientTxPowerLevel5_Type()
)
cd11IfClientTxPowerLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel5.setStatus("current")


class _Cd11IfClientTxPowerLevel6_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel6_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel6_Object = MibTableColumn
cd11IfClientTxPowerLevel6 = _Cd11IfClientTxPowerLevel6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 7),
    _Cd11IfClientTxPowerLevel6_Type()
)
cd11IfClientTxPowerLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel6.setStatus("current")


class _Cd11IfClientTxPowerLevel7_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel7_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel7_Object = MibTableColumn
cd11IfClientTxPowerLevel7 = _Cd11IfClientTxPowerLevel7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 8),
    _Cd11IfClientTxPowerLevel7_Type()
)
cd11IfClientTxPowerLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel7.setStatus("current")


class _Cd11IfClientTxPowerLevel8_Type(Integer32):
    """Custom type cd11IfClientTxPowerLevel8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Cd11IfClientTxPowerLevel8_Type.__name__ = "Integer32"
_Cd11IfClientTxPowerLevel8_Object = MibTableColumn
cd11IfClientTxPowerLevel8 = _Cd11IfClientTxPowerLevel8_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 9),
    _Cd11IfClientTxPowerLevel8_Type()
)
cd11IfClientTxPowerLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfClientTxPowerLevel8.setStatus("current")


class _Cd11IfClientCurrentTxPowerLevel_Type(Integer32):
    """Custom type cd11IfClientCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cd11IfClientCurrentTxPowerLevel_Type.__name__ = "Integer32"
_Cd11IfClientCurrentTxPowerLevel_Object = MibTableColumn
cd11IfClientCurrentTxPowerLevel = _Cd11IfClientCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 13, 1, 10),
    _Cd11IfClientCurrentTxPowerLevel_Type()
)
cd11IfClientCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfClientCurrentTxPowerLevel.setStatus("current")
_Cd11IfErpOfdmTxPowerTable_Object = MibTable
cd11IfErpOfdmTxPowerTable = _Cd11IfErpOfdmTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerTable.setStatus("current")
_Cd11IfErpOfdmTxPowerEntry_Object = MibTableRow
cd11IfErpOfdmTxPowerEntry = _Cd11IfErpOfdmTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1)
)
cd11IfErpOfdmTxPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerEntry.setStatus("current")


class _Cd11IfErpOfdmNumberTxPowerLevels_Type(Integer32):
    """Custom type cd11IfErpOfdmNumberTxPowerLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cd11IfErpOfdmNumberTxPowerLevels_Type.__name__ = "Integer32"
_Cd11IfErpOfdmNumberTxPowerLevels_Object = MibTableColumn
cd11IfErpOfdmNumberTxPowerLevels = _Cd11IfErpOfdmNumberTxPowerLevels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 1),
    _Cd11IfErpOfdmNumberTxPowerLevels_Type()
)
cd11IfErpOfdmNumberTxPowerLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmNumberTxPowerLevels.setStatus("current")


class _Cd11IfErpOfdmTxPowerLevel1_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel1_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel1_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel1 = _Cd11IfErpOfdmTxPowerLevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 2),
    _Cd11IfErpOfdmTxPowerLevel1_Type()
)
cd11IfErpOfdmTxPowerLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel1.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel1.setUnits("mW")


class _Cd11IfErpOfdmTxPowerLevel2_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel2_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel2_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel2 = _Cd11IfErpOfdmTxPowerLevel2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 3),
    _Cd11IfErpOfdmTxPowerLevel2_Type()
)
cd11IfErpOfdmTxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel2.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel2.setUnits("mW")


class _Cd11IfErpOfdmTxPowerLevel3_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel3_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel3_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel3 = _Cd11IfErpOfdmTxPowerLevel3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 4),
    _Cd11IfErpOfdmTxPowerLevel3_Type()
)
cd11IfErpOfdmTxPowerLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel3.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel3.setUnits("mW")


class _Cd11IfErpOfdmTxPowerLevel4_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel4_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel4_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel4 = _Cd11IfErpOfdmTxPowerLevel4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 5),
    _Cd11IfErpOfdmTxPowerLevel4_Type()
)
cd11IfErpOfdmTxPowerLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel4.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel4.setUnits("mW")


class _Cd11IfErpOfdmTxPowerLevel5_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel5_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel5_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel5 = _Cd11IfErpOfdmTxPowerLevel5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 6),
    _Cd11IfErpOfdmTxPowerLevel5_Type()
)
cd11IfErpOfdmTxPowerLevel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel5.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel5.setUnits("mW")


class _Cd11IfErpOfdmTxPowerLevel6_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel6_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel6_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel6 = _Cd11IfErpOfdmTxPowerLevel6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 7),
    _Cd11IfErpOfdmTxPowerLevel6_Type()
)
cd11IfErpOfdmTxPowerLevel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel6.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel6.setUnits("mW")


class _Cd11IfErpOfdmTxPowerLevel7_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel7_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel7_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel7 = _Cd11IfErpOfdmTxPowerLevel7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 8),
    _Cd11IfErpOfdmTxPowerLevel7_Type()
)
cd11IfErpOfdmTxPowerLevel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel7.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel7.setUnits("mW")


class _Cd11IfErpOfdmTxPowerLevel8_Type(Integer32):
    """Custom type cd11IfErpOfdmTxPowerLevel8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfErpOfdmTxPowerLevel8_Type.__name__ = "Integer32"
_Cd11IfErpOfdmTxPowerLevel8_Object = MibTableColumn
cd11IfErpOfdmTxPowerLevel8 = _Cd11IfErpOfdmTxPowerLevel8_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 9),
    _Cd11IfErpOfdmTxPowerLevel8_Type()
)
cd11IfErpOfdmTxPowerLevel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel8.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfErpOfdmTxPowerLevel8.setUnits("mW")


class _Cd11IfErpOfdmCurrentTxPowerLevel_Type(Integer32):
    """Custom type cd11IfErpOfdmCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cd11IfErpOfdmCurrentTxPowerLevel_Type.__name__ = "Integer32"
_Cd11IfErpOfdmCurrentTxPowerLevel_Object = MibTableColumn
cd11IfErpOfdmCurrentTxPowerLevel = _Cd11IfErpOfdmCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 14, 1, 10),
    _Cd11IfErpOfdmCurrentTxPowerLevel_Type()
)
cd11IfErpOfdmCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfErpOfdmCurrentTxPowerLevel.setStatus("current")
_Cd11IfFrequencyBandTable_Object = MibTable
cd11IfFrequencyBandTable = _Cd11IfFrequencyBandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cd11IfFrequencyBandTable.setStatus("current")
_Cd11IfFrequencyBandEntry_Object = MibTableRow
cd11IfFrequencyBandEntry = _Cd11IfFrequencyBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1)
)
cd11IfFrequencyBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRfFrequencyBand"),
)
if mibBuilder.loadTexts:
    cd11IfFrequencyBandEntry.setStatus("current")
_Cd11IfRfFrequencyBand_Type = Unsigned32
_Cd11IfRfFrequencyBand_Object = MibTableColumn
cd11IfRfFrequencyBand = _Cd11IfRfFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 1),
    _Cd11IfRfFrequencyBand_Type()
)
cd11IfRfFrequencyBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfRfFrequencyBand.setStatus("current")


class _Cd11IfRfFrequencyUnits_Type(Integer32):
    """Custom type cd11IfRfFrequencyUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mHz", 1)
    )


_Cd11IfRfFrequencyUnits_Type.__name__ = "Integer32"
_Cd11IfRfFrequencyUnits_Object = MibTableColumn
cd11IfRfFrequencyUnits = _Cd11IfRfFrequencyUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 2),
    _Cd11IfRfFrequencyUnits_Type()
)
cd11IfRfFrequencyUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRfFrequencyUnits.setStatus("current")
_Cd11IfRfStartChannelNumber_Type = Unsigned32
_Cd11IfRfStartChannelNumber_Object = MibTableColumn
cd11IfRfStartChannelNumber = _Cd11IfRfStartChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 3),
    _Cd11IfRfStartChannelNumber_Type()
)
cd11IfRfStartChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRfStartChannelNumber.setStatus("current")
_Cd11IfRfEndChannelNumber_Type = Unsigned32
_Cd11IfRfEndChannelNumber_Object = MibTableColumn
cd11IfRfEndChannelNumber = _Cd11IfRfEndChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 4),
    _Cd11IfRfEndChannelNumber_Type()
)
cd11IfRfEndChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRfEndChannelNumber.setStatus("current")
_Cd11IfRfChannelSpacingNumber_Type = Unsigned32
_Cd11IfRfChannelSpacingNumber_Object = MibTableColumn
cd11IfRfChannelSpacingNumber = _Cd11IfRfChannelSpacingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 5),
    _Cd11IfRfChannelSpacingNumber_Type()
)
cd11IfRfChannelSpacingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRfChannelSpacingNumber.setStatus("current")


class _Cd11IfRfStartChannelFrequency_Type(Unsigned32):
    """Custom type cd11IfRfStartChannelFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Cd11IfRfStartChannelFrequency_Type.__name__ = "Unsigned32"
_Cd11IfRfStartChannelFrequency_Object = MibTableColumn
cd11IfRfStartChannelFrequency = _Cd11IfRfStartChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 6),
    _Cd11IfRfStartChannelFrequency_Type()
)
cd11IfRfStartChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRfStartChannelFrequency.setStatus("current")
_Cd11IfRfFrequencySpacing_Type = Unsigned32
_Cd11IfRfFrequencySpacing_Object = MibTableColumn
cd11IfRfFrequencySpacing = _Cd11IfRfFrequencySpacing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 7),
    _Cd11IfRfFrequencySpacing_Type()
)
cd11IfRfFrequencySpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRfFrequencySpacing.setStatus("current")
_Cd11IfRfFrequencyBandType_Type = CDot11RadioFrequencyBandType
_Cd11IfRfFrequencyBandType_Object = MibTableColumn
cd11IfRfFrequencyBandType = _Cd11IfRfFrequencyBandType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 8),
    _Cd11IfRfFrequencyBandType_Type()
)
cd11IfRfFrequencyBandType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRfFrequencyBandType.setStatus("current")
_Cd11IfMaxChannelSwitchTime_Type = Unsigned32
_Cd11IfMaxChannelSwitchTime_Object = MibTableColumn
cd11IfMaxChannelSwitchTime = _Cd11IfMaxChannelSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 15, 1, 9),
    _Cd11IfMaxChannelSwitchTime_Type()
)
cd11IfMaxChannelSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfMaxChannelSwitchTime.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfMaxChannelSwitchTime.setUnits("milliseconds")
_Cd11IfNativeTxPowerSupportTable_Object = MibTable
cd11IfNativeTxPowerSupportTable = _Cd11IfNativeTxPowerSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cd11IfNativeTxPowerSupportTable.setStatus("current")
_Cd11IfNativeTxPowerSupportEntry_Object = MibTableRow
cd11IfNativeTxPowerSupportEntry = _Cd11IfNativeTxPowerSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 16, 1)
)
cd11IfNativeTxPowerSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRfFrequencyBand"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRadioModulationClass"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfNativeTxPowerLevel"),
)
if mibBuilder.loadTexts:
    cd11IfNativeTxPowerSupportEntry.setStatus("current")
_Cd11IfRadioModulationClass_Type = CDot11RadioModulationClass
_Cd11IfRadioModulationClass_Object = MibTableColumn
cd11IfRadioModulationClass = _Cd11IfRadioModulationClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 16, 1, 1),
    _Cd11IfRadioModulationClass_Type()
)
cd11IfRadioModulationClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfRadioModulationClass.setStatus("current")
_Cd11IfNativeTxPowerLevel_Type = Unsigned32
_Cd11IfNativeTxPowerLevel_Object = MibTableColumn
cd11IfNativeTxPowerLevel = _Cd11IfNativeTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 16, 1, 2),
    _Cd11IfNativeTxPowerLevel_Type()
)
cd11IfNativeTxPowerLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfNativeTxPowerLevel.setStatus("current")
_Cd11IfNativeTxPower_Type = Integer32
_Cd11IfNativeTxPower_Object = MibTableColumn
cd11IfNativeTxPower = _Cd11IfNativeTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 16, 1, 3),
    _Cd11IfNativeTxPower_Type()
)
cd11IfNativeTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfNativeTxPower.setStatus("current")
_Cd11IfRfNativePowerTable_Object = MibTable
cd11IfRfNativePowerTable = _Cd11IfRfNativePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 17)
)
if mibBuilder.loadTexts:
    cd11IfRfNativePowerTable.setStatus("current")
_Cd11IfRfNativePowerEntry_Object = MibTableRow
cd11IfRfNativePowerEntry = _Cd11IfRfNativePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 17, 1)
)
cd11IfRfNativePowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRfFrequencyBand"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRadioModulationClass"),
)
if mibBuilder.loadTexts:
    cd11IfRfNativePowerEntry.setStatus("current")
_Cd11IfNativeNumberPowerLevels_Type = Unsigned32
_Cd11IfNativeNumberPowerLevels_Object = MibTableColumn
cd11IfNativeNumberPowerLevels = _Cd11IfNativeNumberPowerLevels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 17, 1, 1),
    _Cd11IfNativeNumberPowerLevels_Type()
)
cd11IfNativeNumberPowerLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfNativeNumberPowerLevels.setStatus("current")
_Cd11IfNativeCurrentPowerLevel_Type = Unsigned32
_Cd11IfNativeCurrentPowerLevel_Object = MibTableColumn
cd11IfNativeCurrentPowerLevel = _Cd11IfNativeCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 17, 1, 2),
    _Cd11IfNativeCurrentPowerLevel_Type()
)
cd11IfNativeCurrentPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cd11IfNativeCurrentPowerLevel.setStatus("current")


class _Cd11IfNativePowerUnits_Type(Integer32):
    """Custom type cd11IfNativePowerUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dBm", 2),
          ("mW", 1))
    )


_Cd11IfNativePowerUnits_Type.__name__ = "Integer32"
_Cd11IfNativePowerUnits_Object = MibTableColumn
cd11IfNativePowerUnits = _Cd11IfNativePowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 17, 1, 3),
    _Cd11IfNativePowerUnits_Type()
)
cd11IfNativePowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfNativePowerUnits.setStatus("current")
_Cd11IfDataRatesSensitivityTable_Object = MibTable
cd11IfDataRatesSensitivityTable = _Cd11IfDataRatesSensitivityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 18)
)
if mibBuilder.loadTexts:
    cd11IfDataRatesSensitivityTable.setStatus("current")
_Cd11IfDataRatesSensitivityEntry_Object = MibTableRow
cd11IfDataRatesSensitivityEntry = _Cd11IfDataRatesSensitivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 18, 1)
)
cd11IfDataRatesSensitivityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRadioModulationClass"),
    (0, "IEEE802dot11-MIB", "dot11SupportedDataRatesRxIndex"),
)
if mibBuilder.loadTexts:
    cd11IfDataRatesSensitivityEntry.setStatus("current")
_Cd11IfRatesSensRequiredSnr_Type = Integer32
_Cd11IfRatesSensRequiredSnr_Object = MibTableColumn
cd11IfRatesSensRequiredSnr = _Cd11IfRatesSensRequiredSnr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 18, 1, 1),
    _Cd11IfRatesSensRequiredSnr_Type()
)
cd11IfRatesSensRequiredSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRatesSensRequiredSnr.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfRatesSensRequiredSnr.setUnits("dB")
_Cd11IfRatesSensContention_Type = Integer32
_Cd11IfRatesSensContention_Object = MibTableColumn
cd11IfRatesSensContention = _Cd11IfRatesSensContention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 1, 2, 18, 1, 2),
    _Cd11IfRatesSensContention_Type()
)
cd11IfRatesSensContention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRatesSensContention.setStatus("current")
if mibBuilder.loadTexts:
    cd11IfRatesSensContention.setUnits("dBm")
_Cd11IfStatistics_ObjectIdentity = ObjectIdentity
cd11IfStatistics = _Cd11IfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2)
)
_Cd11IfMacStatistics_ObjectIdentity = ObjectIdentity
cd11IfMacStatistics = _Cd11IfMacStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1)
)
_Cd11IfMacLayerCountersTable_Object = MibTable
cd11IfMacLayerCountersTable = _Cd11IfMacLayerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cd11IfMacLayerCountersTable.setStatus("current")
_Cd11IfMacLayerCountersEntry_Object = MibTableRow
cd11IfMacLayerCountersEntry = _Cd11IfMacLayerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 1, 1)
)
cd11IfMacLayerCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfMacLayerCountersEntry.setStatus("current")
_Cd11IfTransDeferEnerDetects_Type = Counter32
_Cd11IfTransDeferEnerDetects_Object = MibTableColumn
cd11IfTransDeferEnerDetects = _Cd11IfTransDeferEnerDetects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 1, 1, 1),
    _Cd11IfTransDeferEnerDetects_Type()
)
cd11IfTransDeferEnerDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfTransDeferEnerDetects.setStatus("current")
_Cd11IfRecFrameMacCrcErrors_Type = Counter32
_Cd11IfRecFrameMacCrcErrors_Object = MibTableColumn
cd11IfRecFrameMacCrcErrors = _Cd11IfRecFrameMacCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 1, 1, 2),
    _Cd11IfRecFrameMacCrcErrors_Type()
)
cd11IfRecFrameMacCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRecFrameMacCrcErrors.setStatus("current")
_Cd11IfSsidMismatches_Type = Counter32
_Cd11IfSsidMismatches_Object = MibTableColumn
cd11IfSsidMismatches = _Cd11IfSsidMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 1, 1, 3),
    _Cd11IfSsidMismatches_Type()
)
cd11IfSsidMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfSsidMismatches.setStatus("current")
_Cd11IfRogueApDetectedTable_Object = MibTable
cd11IfRogueApDetectedTable = _Cd11IfRogueApDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cd11IfRogueApDetectedTable.setStatus("current")
_Cd11IfRogueApDetectedEntry_Object = MibTableRow
cd11IfRogueApDetectedEntry = _Cd11IfRogueApDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 2, 1)
)
cd11IfRogueApDetectedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfRogueApMacAddr"),
)
if mibBuilder.loadTexts:
    cd11IfRogueApDetectedEntry.setStatus("current")
_Cd11IfRogueApMacAddr_Type = MacAddress
_Cd11IfRogueApMacAddr_Object = MibTableColumn
cd11IfRogueApMacAddr = _Cd11IfRogueApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 2, 1, 1),
    _Cd11IfRogueApMacAddr_Type()
)
cd11IfRogueApMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cd11IfRogueApMacAddr.setStatus("current")
_Cd11IfRogueApName_Type = SnmpAdminString
_Cd11IfRogueApName_Object = MibTableColumn
cd11IfRogueApName = _Cd11IfRogueApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 1, 2, 1, 2, 1, 2),
    _Cd11IfRogueApName_Type()
)
cd11IfRogueApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfRogueApName.setStatus("current")
_CiscoDot11IfMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11IfMIBConformance = _CiscoDot11IfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3)
)
_CiscoDot11IfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11IfMIBCompliances = _CiscoDot11IfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 1)
)
_CiscoDot11IfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11IfMIBGroups = _CiscoDot11IfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2)
)

# Managed Objects groups

cd11IfManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 1)
)
cd11IfManagementGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfStationRole"),
        ("CISCO-DOT11-IF-MIB", "cd11IfCiscoExtensionsEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAllowBroadcastSsidAssoc"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPrivacyOptionMaxRate"),
        ("CISCO-DOT11-IF-MIB", "cd11IfEthernetEncapsulDefault"),
        ("CISCO-DOT11-IF-MIB", "cd11IfBridgeSpacing"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredSsidMaxAssocSta"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxiliarySsidLength"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVoipExtensionsEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredSsidMicAlgorithm"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredSsidWepPermuteAlg"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgRequireEap"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgRequireMacAddr"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgDefaultVlan"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWepDefaultKeyLen"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWepDefaultKeyValue"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredBssAddr"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsid"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidBroadcastSsid"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidMaxAssocSta"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidMicAlgorithm"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidWepPermuteAlg"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgRequireEap"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgRequireMac"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgDefaultVlan"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAssignedSta"))
)
if mibBuilder.loadTexts:
    cd11IfManagementGroup.setStatus("deprecated")

cd11IfPhyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 2)
)
cd11IfPhyConfigGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfCurrentCarrierSet"),
        ("CISCO-DOT11-IF-MIB", "cd11IfModulationType"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPreambleType"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyFhssMaxCompatibleRate"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyDsssMaxCompatibleRate"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyDsssChannelAutoEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyDsssCurrentChannel"),
        ("CISCO-DOT11-IF-MIB", "cd11IfSuppDataRatesPrivacyValue"),
        ("CISCO-DOT11-IF-MIB", "cd11IfSuppDataRatesPrivacyEnabl"),
        ("CISCO-DOT11-IF-MIB", "cd11IfChanSelectEnable"))
)
if mibBuilder.loadTexts:
    cd11IfPhyConfigGroup.setStatus("deprecated")

cd11IfMacStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 3)
)
cd11IfMacStatisticsGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfTransDeferEnerDetects"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRecFrameMacCrcErrors"),
        ("CISCO-DOT11-IF-MIB", "cd11IfSsidMismatches"))
)
if mibBuilder.loadTexts:
    cd11IfMacStatisticsGroup.setStatus("current")

cd11IfVlanEncryptKeyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 4)
)
cd11IfVlanEncryptKeyConfigGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyLen"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyValue"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyStatus"))
)
if mibBuilder.loadTexts:
    cd11IfVlanEncryptKeyConfigGroup.setStatus("deprecated")

cd11IfDomainCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 5)
)
cd11IfDomainCapabilityGroup.setObjects(
    ("CISCO-DOT11-IF-MIB", "cd11IfDomainCapabilitySet")
)
if mibBuilder.loadTexts:
    cd11IfDomainCapabilityGroup.setStatus("deprecated")

cd11IfPhyMacCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 6)
)
cd11IfPhyMacCapabilityGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfPhyBasicRateSet"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyMacSpecification"))
)
if mibBuilder.loadTexts:
    cd11IfPhyMacCapabilityGroup.setStatus("deprecated")

cd11IfAuthAlgMethodListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 7)
)
cd11IfAuthAlgMethodListGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgEapMethod"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgMacAddrMethod"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgEapMethod"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgMacMethod"))
)
if mibBuilder.loadTexts:
    cd11IfAuthAlgMethodListGroup.setStatus("deprecated")

cd11IfRadioManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 8)
)
cd11IfRadioManageGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfStationRole"),
        ("CISCO-DOT11-IF-MIB", "cd11IfCiscoExtensionsEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPrivacyOptionMaxRate"),
        ("CISCO-DOT11-IF-MIB", "cd11IfEthernetEncapsulDefault"),
        ("CISCO-DOT11-IF-MIB", "cd11IfBridgeSpacing"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVoipExtensionsEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxiliarySsidLength"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAllowBroadcastSsidAssoc"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredBssAddr"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAssignedSta"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWorldMode"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWorldModeCountry"),
        ("CISCO-DOT11-IF-MIB", "cd11IfMobileStationScanParent"))
)
if mibBuilder.loadTexts:
    cd11IfRadioManageGroup.setStatus("deprecated")

cd11IfAssociationManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 9)
)
cd11IfAssociationManageGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfDesiredSsidMaxAssocSta"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredSsidMicAlgorithm"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredSsidWepPermuteAlg"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgRequireEap"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgRequireMacAddr"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgDefaultVlan"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgEapMethod"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuthAlgMacAddrMethod"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWepDefaultKeyLen"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWepDefaultKeyValue"))
)
if mibBuilder.loadTexts:
    cd11IfAssociationManageGroup.setStatus("current")

cd11IfSsidAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 10)
)
cd11IfSsidAssociationGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfAuxSsid"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidBroadcastSsid"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidMaxAssocSta"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidMicAlgorithm"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidWepPermuteAlg"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgRequireEap"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgRequireMac"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgDefaultVlan"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgEapMethod"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxSsidAuthAlgMacMethod"))
)
if mibBuilder.loadTexts:
    cd11IfSsidAssociationGroup.setStatus("current")

cd11IfVlanManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 11)
)
cd11IfVlanManageGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyLen"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyValue"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyStatus"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptKeyTransmit"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanSecurityVlanEnabled"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanBcastKeyChangeInterval"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanBcastKeyCapabilChange"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanBcastKeyClientLeave"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanSecurityCiphers"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanSecurityRowStatus"))
)
if mibBuilder.loadTexts:
    cd11IfVlanManageGroup.setStatus("current")

cd11IfRemoteMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 12)
)
cd11IfRemoteMonitoringGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfRadioMonitorPollingFreq"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRadioMonitorPollingTimeOut"),
        ("CISCO-DOT11-IF-MIB", "cd11IfLocalRadioMonitorStatus"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRadioMonitorRowStatus"))
)
if mibBuilder.loadTexts:
    cd11IfRemoteMonitoringGroup.setStatus("current")

cd11IfPhyConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 13)
)
cd11IfPhyConfigGroupRev1.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfCurrentCarrierSet"),
        ("CISCO-DOT11-IF-MIB", "cd11IfModulationType"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPreambleType"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDomainCapabilitySet"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyBasicRateSet"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyMacSpecification"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyConcatenation"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyDsssMaxCompatibleRate"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyDsssChannelAutoEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyDsssCurrentChannel"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPhyFhssMaxCompatibleRate"),
        ("CISCO-DOT11-IF-MIB", "cd11IfSuppDataRatesPrivacyValue"),
        ("CISCO-DOT11-IF-MIB", "cd11IfSuppDataRatesPrivacyEnabl"),
        ("CISCO-DOT11-IF-MIB", "cd11IfChanSelectEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientNumberTxPowerLevels"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel1"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel2"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel3"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel4"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel5"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel6"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel7"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientTxPowerLevel8"),
        ("CISCO-DOT11-IF-MIB", "cd11IfClientCurrentTxPowerLevel"))
)
if mibBuilder.loadTexts:
    cd11IfPhyConfigGroupRev1.setStatus("current")

cd11IfPhyErpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 14)
)
cd11IfPhyErpConfigGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmNumberTxPowerLevels"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel1"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel2"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel3"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel4"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel5"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel6"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel7"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmTxPowerLevel8"),
        ("CISCO-DOT11-IF-MIB", "cd11IfErpOfdmCurrentTxPowerLevel"))
)
if mibBuilder.loadTexts:
    cd11IfPhyErpConfigGroup.setStatus("current")

cd11IfVlanWepManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 15)
)
cd11IfVlanWepManageGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfVlanEncryptionMode"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanWepEncryptOptions"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanWepEncryptMic"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanWepEncryptKeyHashing"))
)
if mibBuilder.loadTexts:
    cd11IfVlanWepManageGroup.setStatus("current")

cd11IfRogueApDetectedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 16)
)
cd11IfRogueApDetectedGroup.setObjects(
    ("CISCO-DOT11-IF-MIB", "cd11IfRogueApName")
)
if mibBuilder.loadTexts:
    cd11IfRogueApDetectedGroup.setStatus("current")

cd11IfStationManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 17)
)
cd11IfStationManageGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfStationRole"),
        ("CISCO-DOT11-IF-MIB", "cd11IfCiscoExtensionsEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPrivacyOptionMaxRate"),
        ("CISCO-DOT11-IF-MIB", "cd11IfEthernetEncapsulDefault"),
        ("CISCO-DOT11-IF-MIB", "cd11IfBridgeSpacing"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVoipExtensionsEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAuxiliarySsidLength"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAllowBroadcastSsidAssoc"),
        ("CISCO-DOT11-IF-MIB", "cd11IfDesiredBssAddr"),
        ("CISCO-DOT11-IF-MIB", "cd11IfAssignedSta"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWorldMode"),
        ("CISCO-DOT11-IF-MIB", "cd11IfWorldModeCountry"),
        ("CISCO-DOT11-IF-MIB", "cd11IfMobileStationScanParent"),
        ("CISCO-DOT11-IF-MIB", "cd11IfPsPacketForwardEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfMultipleBssidEnable"),
        ("CISCO-DOT11-IF-MIB", "cd11IfVlanPsPacketForwardEnable"))
)
if mibBuilder.loadTexts:
    cd11IfStationManageGroup.setStatus("current")

cd11IfNativeRadioManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 18)
)
cd11IfNativeRadioManageGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfPhyNativePowerUseStandard"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRfFrequencyUnits"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRfStartChannelNumber"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRfEndChannelNumber"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRfChannelSpacingNumber"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRfStartChannelFrequency"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRfFrequencySpacing"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRfFrequencyBandType"),
        ("CISCO-DOT11-IF-MIB", "cd11IfMaxChannelSwitchTime"),
        ("CISCO-DOT11-IF-MIB", "cd11IfNativeNumberPowerLevels"),
        ("CISCO-DOT11-IF-MIB", "cd11IfNativeCurrentPowerLevel"),
        ("CISCO-DOT11-IF-MIB", "cd11IfNativePowerUnits"),
        ("CISCO-DOT11-IF-MIB", "cd11IfNativeTxPower"))
)
if mibBuilder.loadTexts:
    cd11IfNativeRadioManageGroup.setStatus("current")

cd11IfDataRatesSensitivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 19)
)
cd11IfDataRatesSensitivityGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfRatesSensRequiredSnr"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRatesSensContention"))
)
if mibBuilder.loadTexts:
    cd11IfDataRatesSensitivityGroup.setStatus("current")

cd11Ifdot11UpgradeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 21)
)
cd11Ifdot11UpgradeStatusGroup.setObjects(
    ("CISCO-DOT11-IF-MIB", "cd11IfDot11UpgradeStatus")
)
if mibBuilder.loadTexts:
    cd11Ifdot11UpgradeStatusGroup.setStatus("current")

cd11Ifdot11MobileStationScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 22)
)
cd11Ifdot11MobileStationScanGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfMobileStationListIgnore"),
        ("CISCO-DOT11-IF-MIB", "cd11IfMobileStationScanChannel"))
)
if mibBuilder.loadTexts:
    cd11Ifdot11MobileStationScanGroup.setStatus("current")


# Notification objects

cd11IfStationSwitchOverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 0, 1)
)
cd11IfStationSwitchOverNotif.setObjects(
    ("CISCO-DOT11-IF-MIB", "cd11IfLocalRadioMonitorStatus")
)
if mibBuilder.loadTexts:
    cd11IfStationSwitchOverNotif.setStatus(
        "current"
    )

cd11IfRogueApDetectedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 0, 2)
)
cd11IfRogueApDetectedNotif.setObjects(
    ("CISCO-DOT11-IF-MIB", "cd11IfRogueApName")
)
if mibBuilder.loadTexts:
    cd11IfRogueApDetectedNotif.setStatus(
        "current"
    )


# Notifications groups

cd11IfMonitorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 2, 20)
)
cd11IfMonitorNotificationGroup.setObjects(
      *(("CISCO-DOT11-IF-MIB", "cd11IfStationSwitchOverNotif"),
        ("CISCO-DOT11-IF-MIB", "cd11IfRogueApDetectedNotif"))
)
if mibBuilder.loadTexts:
    cd11IfMonitorNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDot11IfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11IfCompliance.setStatus(
        "deprecated"
    )

ciscoDot11IfComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDot11IfComplianceRev1.setStatus(
        "deprecated"
    )

ciscoDot11IfComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoDot11IfComplianceRev2.setStatus(
        "deprecated"
    )

ciscoDot11IfComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoDot11IfComplianceRev3.setStatus(
        "deprecated"
    )

ciscoDot11IfComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 272, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoDot11IfComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-IF-MIB",
    **{"CDot11IfVlanIdOrZero": CDot11IfVlanIdOrZero,
       "WepKeyType128": WepKeyType128,
       "CDot11IfMicAlgorithm": CDot11IfMicAlgorithm,
       "CDot11IfWepKeyPermuteAlgorithm": CDot11IfWepKeyPermuteAlgorithm,
       "CDot11IfCipherType": CDot11IfCipherType,
       "CDot11RadioFrequencyBandType": CDot11RadioFrequencyBandType,
       "CDot11RadioModulationClass": CDot11RadioModulationClass,
       "Cd11IfDot11UpgradeStatus": Cd11IfDot11UpgradeStatus,
       "ciscoDot11IfMIB": ciscoDot11IfMIB,
       "ciscoDot11IfMIBNotifications": ciscoDot11IfMIBNotifications,
       "cd11IfStationSwitchOverNotif": cd11IfStationSwitchOverNotif,
       "cd11IfRogueApDetectedNotif": cd11IfRogueApDetectedNotif,
       "ciscoDot11IfMIBObjects": ciscoDot11IfMIBObjects,
       "cd11IfConfigurations": cd11IfConfigurations,
       "cd11IfManagement": cd11IfManagement,
       "cd11IfStationConfigTable": cd11IfStationConfigTable,
       "cd11IfStationConfigEntry": cd11IfStationConfigEntry,
       "cd11IfStationRole": cd11IfStationRole,
       "cd11IfCiscoExtensionsEnable": cd11IfCiscoExtensionsEnable,
       "cd11IfAllowBroadcastSsidAssoc": cd11IfAllowBroadcastSsidAssoc,
       "cd11IfPrivacyOptionMaxRate": cd11IfPrivacyOptionMaxRate,
       "cd11IfEthernetEncapsulDefault": cd11IfEthernetEncapsulDefault,
       "cd11IfBridgeSpacing": cd11IfBridgeSpacing,
       "cd11IfDesiredSsidMaxAssocSta": cd11IfDesiredSsidMaxAssocSta,
       "cd11IfAuxiliarySsidLength": cd11IfAuxiliarySsidLength,
       "cd11IfVoipExtensionsEnable": cd11IfVoipExtensionsEnable,
       "cd11IfDesiredSsidMicAlgorithm": cd11IfDesiredSsidMicAlgorithm,
       "cd11IfDesiredSsidWepPermuteAlg": cd11IfDesiredSsidWepPermuteAlg,
       "cd11IfWorldMode": cd11IfWorldMode,
       "cd11IfWorldModeCountry": cd11IfWorldModeCountry,
       "cd11IfMobileStationScanParent": cd11IfMobileStationScanParent,
       "cd11IfPsPacketForwardEnable": cd11IfPsPacketForwardEnable,
       "cd11IfMultipleBssidEnable": cd11IfMultipleBssidEnable,
       "cd11IfMobileStationListIgnore": cd11IfMobileStationListIgnore,
       "cd11IfMobileStationScanChannel": cd11IfMobileStationScanChannel,
       "cd11IfAuthAlgorithmTable": cd11IfAuthAlgorithmTable,
       "cd11IfAuthAlgorithmEntry": cd11IfAuthAlgorithmEntry,
       "cd11IfAuthAlgRequireEap": cd11IfAuthAlgRequireEap,
       "cd11IfAuthAlgRequireMacAddr": cd11IfAuthAlgRequireMacAddr,
       "cd11IfAuthAlgDefaultVlan": cd11IfAuthAlgDefaultVlan,
       "cd11IfAuthAlgEapMethod": cd11IfAuthAlgEapMethod,
       "cd11IfAuthAlgMacAddrMethod": cd11IfAuthAlgMacAddrMethod,
       "cd11IfWepDefaultKeysTable": cd11IfWepDefaultKeysTable,
       "cd11IfWepDefaultKeysEntry": cd11IfWepDefaultKeysEntry,
       "cd11IfWepDefaultKeyIndex": cd11IfWepDefaultKeyIndex,
       "cd11IfWepDefaultKeyLen": cd11IfWepDefaultKeyLen,
       "cd11IfWepDefaultKeyValue": cd11IfWepDefaultKeyValue,
       "cd11IfDesiredBssTable": cd11IfDesiredBssTable,
       "cd11IfDesiredBssEntry": cd11IfDesiredBssEntry,
       "cd11IfDesiredBssIndex": cd11IfDesiredBssIndex,
       "cd11IfDesiredBssAddr": cd11IfDesiredBssAddr,
       "cd11IfAuxSsidTable": cd11IfAuxSsidTable,
       "cd11IfAuxSsidEntry": cd11IfAuxSsidEntry,
       "cd11IfAuxSsidIndex": cd11IfAuxSsidIndex,
       "cd11IfAuxSsid": cd11IfAuxSsid,
       "cd11IfAuxSsidBroadcastSsid": cd11IfAuxSsidBroadcastSsid,
       "cd11IfAuxSsidMaxAssocSta": cd11IfAuxSsidMaxAssocSta,
       "cd11IfAuxSsidMicAlgorithm": cd11IfAuxSsidMicAlgorithm,
       "cd11IfAuxSsidWepPermuteAlg": cd11IfAuxSsidWepPermuteAlg,
       "cd11IfAuxSsidAuthAlgTable": cd11IfAuxSsidAuthAlgTable,
       "cd11IfAuxSsidAuthAlgEntry": cd11IfAuxSsidAuthAlgEntry,
       "cd11IfAuxSsidAuthAlgEnable": cd11IfAuxSsidAuthAlgEnable,
       "cd11IfAuxSsidAuthAlgRequireEap": cd11IfAuxSsidAuthAlgRequireEap,
       "cd11IfAuxSsidAuthAlgRequireMac": cd11IfAuxSsidAuthAlgRequireMac,
       "cd11IfAuxSsidAuthAlgDefaultVlan": cd11IfAuxSsidAuthAlgDefaultVlan,
       "cd11IfAuxSsidAuthAlgEapMethod": cd11IfAuxSsidAuthAlgEapMethod,
       "cd11IfAuxSsidAuthAlgMacMethod": cd11IfAuxSsidAuthAlgMacMethod,
       "cd11IfAssignedAidTable": cd11IfAssignedAidTable,
       "cd11IfAssignedAidEntry": cd11IfAssignedAidEntry,
       "cd11IfAssignedAid": cd11IfAssignedAid,
       "cd11IfAssignedSta": cd11IfAssignedSta,
       "cd11IfVlanEncryptKeyTable": cd11IfVlanEncryptKeyTable,
       "cd11IfVlanEncryptKeyEntry": cd11IfVlanEncryptKeyEntry,
       "cd11IfVlanId": cd11IfVlanId,
       "cd11IfVlanEncryptKeyIndex": cd11IfVlanEncryptKeyIndex,
       "cd11IfVlanEncryptKeyLen": cd11IfVlanEncryptKeyLen,
       "cd11IfVlanEncryptKeyValue": cd11IfVlanEncryptKeyValue,
       "cd11IfVlanEncryptKeyStatus": cd11IfVlanEncryptKeyStatus,
       "cd11IfVlanEncryptKeyTransmit": cd11IfVlanEncryptKeyTransmit,
       "cd11IfVlanSecurityTable": cd11IfVlanSecurityTable,
       "cd11IfVlanSecurityEntry": cd11IfVlanSecurityEntry,
       "cd11IfVlanSecurityVlanId": cd11IfVlanSecurityVlanId,
       "cd11IfVlanSecurityVlanEnabled": cd11IfVlanSecurityVlanEnabled,
       "cd11IfVlanBcastKeyChangeInterval": cd11IfVlanBcastKeyChangeInterval,
       "cd11IfVlanBcastKeyCapabilChange": cd11IfVlanBcastKeyCapabilChange,
       "cd11IfVlanBcastKeyClientLeave": cd11IfVlanBcastKeyClientLeave,
       "cd11IfVlanSecurityCiphers": cd11IfVlanSecurityCiphers,
       "cd11IfVlanSecurityRowStatus": cd11IfVlanSecurityRowStatus,
       "cd11IfVlanEncryptionMode": cd11IfVlanEncryptionMode,
       "cd11IfVlanWepEncryptOptions": cd11IfVlanWepEncryptOptions,
       "cd11IfVlanWepEncryptMic": cd11IfVlanWepEncryptMic,
       "cd11IfVlanWepEncryptKeyHashing": cd11IfVlanWepEncryptKeyHashing,
       "cd11IfVlanPsPacketForwardEnable": cd11IfVlanPsPacketForwardEnable,
       "cd11IfRadioMonitoringTable": cd11IfRadioMonitoringTable,
       "cd11IfRadioMonitoringEntry": cd11IfRadioMonitoringEntry,
       "cd11IfRemoteRadioMacAddr": cd11IfRemoteRadioMacAddr,
       "cd11IfRadioMonitorPollingFreq": cd11IfRadioMonitorPollingFreq,
       "cd11IfRadioMonitorPollingTimeOut": cd11IfRadioMonitorPollingTimeOut,
       "cd11IfLocalRadioMonitorStatus": cd11IfLocalRadioMonitorStatus,
       "cd11IfRadioMonitorRowStatus": cd11IfRadioMonitorRowStatus,
       "cd11IfDot11UpgradeStatusTable": cd11IfDot11UpgradeStatusTable,
       "cd11IfDot11UpgradeStatusEntry": cd11IfDot11UpgradeStatusEntry,
       "cd11IfDot11UpgradeStatus": cd11IfDot11UpgradeStatus,
       "cd11IfPhyConfig": cd11IfPhyConfig,
       "cd11IfPhyOperationTable": cd11IfPhyOperationTable,
       "cd11IfPhyOperationEntry": cd11IfPhyOperationEntry,
       "cd11IfCurrentCarrierSet": cd11IfCurrentCarrierSet,
       "cd11IfModulationType": cd11IfModulationType,
       "cd11IfPreambleType": cd11IfPreambleType,
       "cd11IfDomainCapabilitySet": cd11IfDomainCapabilitySet,
       "cd11IfPhyBasicRateSet": cd11IfPhyBasicRateSet,
       "cd11IfPhyMacSpecification": cd11IfPhyMacSpecification,
       "cd11IfPhyConcatenation": cd11IfPhyConcatenation,
       "cd11IfPhyNativePowerUseStandard": cd11IfPhyNativePowerUseStandard,
       "cd11IfPhyFhssTable": cd11IfPhyFhssTable,
       "cd11IfPhyFhssEntry": cd11IfPhyFhssEntry,
       "cd11IfPhyFhssMaxCompatibleRate": cd11IfPhyFhssMaxCompatibleRate,
       "cd11IfPhyDsssTable": cd11IfPhyDsssTable,
       "cd11IfPhyDsssEntry": cd11IfPhyDsssEntry,
       "cd11IfPhyDsssMaxCompatibleRate": cd11IfPhyDsssMaxCompatibleRate,
       "cd11IfPhyDsssChannelAutoEnable": cd11IfPhyDsssChannelAutoEnable,
       "cd11IfPhyDsssCurrentChannel": cd11IfPhyDsssCurrentChannel,
       "cd11IfSuppDataRatesPrivacyTable": cd11IfSuppDataRatesPrivacyTable,
       "cd11IfSuppDataRatesPrivacyEntry": cd11IfSuppDataRatesPrivacyEntry,
       "cd11IfSuppDataRatesPrivacyIndex": cd11IfSuppDataRatesPrivacyIndex,
       "cd11IfSuppDataRatesPrivacyValue": cd11IfSuppDataRatesPrivacyValue,
       "cd11IfSuppDataRatesPrivacyEnabl": cd11IfSuppDataRatesPrivacyEnabl,
       "cd11IfChanSelectTable": cd11IfChanSelectTable,
       "cd11IfChanSelectEntry": cd11IfChanSelectEntry,
       "cd11IfChanSelectChannel": cd11IfChanSelectChannel,
       "cd11IfChanSelectEnable": cd11IfChanSelectEnable,
       "cd11IfClientTxPowerTable": cd11IfClientTxPowerTable,
       "cd11IfClientTxPowerEntry": cd11IfClientTxPowerEntry,
       "cd11IfClientNumberTxPowerLevels": cd11IfClientNumberTxPowerLevels,
       "cd11IfClientTxPowerLevel1": cd11IfClientTxPowerLevel1,
       "cd11IfClientTxPowerLevel2": cd11IfClientTxPowerLevel2,
       "cd11IfClientTxPowerLevel3": cd11IfClientTxPowerLevel3,
       "cd11IfClientTxPowerLevel4": cd11IfClientTxPowerLevel4,
       "cd11IfClientTxPowerLevel5": cd11IfClientTxPowerLevel5,
       "cd11IfClientTxPowerLevel6": cd11IfClientTxPowerLevel6,
       "cd11IfClientTxPowerLevel7": cd11IfClientTxPowerLevel7,
       "cd11IfClientTxPowerLevel8": cd11IfClientTxPowerLevel8,
       "cd11IfClientCurrentTxPowerLevel": cd11IfClientCurrentTxPowerLevel,
       "cd11IfErpOfdmTxPowerTable": cd11IfErpOfdmTxPowerTable,
       "cd11IfErpOfdmTxPowerEntry": cd11IfErpOfdmTxPowerEntry,
       "cd11IfErpOfdmNumberTxPowerLevels": cd11IfErpOfdmNumberTxPowerLevels,
       "cd11IfErpOfdmTxPowerLevel1": cd11IfErpOfdmTxPowerLevel1,
       "cd11IfErpOfdmTxPowerLevel2": cd11IfErpOfdmTxPowerLevel2,
       "cd11IfErpOfdmTxPowerLevel3": cd11IfErpOfdmTxPowerLevel3,
       "cd11IfErpOfdmTxPowerLevel4": cd11IfErpOfdmTxPowerLevel4,
       "cd11IfErpOfdmTxPowerLevel5": cd11IfErpOfdmTxPowerLevel5,
       "cd11IfErpOfdmTxPowerLevel6": cd11IfErpOfdmTxPowerLevel6,
       "cd11IfErpOfdmTxPowerLevel7": cd11IfErpOfdmTxPowerLevel7,
       "cd11IfErpOfdmTxPowerLevel8": cd11IfErpOfdmTxPowerLevel8,
       "cd11IfErpOfdmCurrentTxPowerLevel": cd11IfErpOfdmCurrentTxPowerLevel,
       "cd11IfFrequencyBandTable": cd11IfFrequencyBandTable,
       "cd11IfFrequencyBandEntry": cd11IfFrequencyBandEntry,
       "cd11IfRfFrequencyBand": cd11IfRfFrequencyBand,
       "cd11IfRfFrequencyUnits": cd11IfRfFrequencyUnits,
       "cd11IfRfStartChannelNumber": cd11IfRfStartChannelNumber,
       "cd11IfRfEndChannelNumber": cd11IfRfEndChannelNumber,
       "cd11IfRfChannelSpacingNumber": cd11IfRfChannelSpacingNumber,
       "cd11IfRfStartChannelFrequency": cd11IfRfStartChannelFrequency,
       "cd11IfRfFrequencySpacing": cd11IfRfFrequencySpacing,
       "cd11IfRfFrequencyBandType": cd11IfRfFrequencyBandType,
       "cd11IfMaxChannelSwitchTime": cd11IfMaxChannelSwitchTime,
       "cd11IfNativeTxPowerSupportTable": cd11IfNativeTxPowerSupportTable,
       "cd11IfNativeTxPowerSupportEntry": cd11IfNativeTxPowerSupportEntry,
       "cd11IfRadioModulationClass": cd11IfRadioModulationClass,
       "cd11IfNativeTxPowerLevel": cd11IfNativeTxPowerLevel,
       "cd11IfNativeTxPower": cd11IfNativeTxPower,
       "cd11IfRfNativePowerTable": cd11IfRfNativePowerTable,
       "cd11IfRfNativePowerEntry": cd11IfRfNativePowerEntry,
       "cd11IfNativeNumberPowerLevels": cd11IfNativeNumberPowerLevels,
       "cd11IfNativeCurrentPowerLevel": cd11IfNativeCurrentPowerLevel,
       "cd11IfNativePowerUnits": cd11IfNativePowerUnits,
       "cd11IfDataRatesSensitivityTable": cd11IfDataRatesSensitivityTable,
       "cd11IfDataRatesSensitivityEntry": cd11IfDataRatesSensitivityEntry,
       "cd11IfRatesSensRequiredSnr": cd11IfRatesSensRequiredSnr,
       "cd11IfRatesSensContention": cd11IfRatesSensContention,
       "cd11IfStatistics": cd11IfStatistics,
       "cd11IfMacStatistics": cd11IfMacStatistics,
       "cd11IfMacLayerCountersTable": cd11IfMacLayerCountersTable,
       "cd11IfMacLayerCountersEntry": cd11IfMacLayerCountersEntry,
       "cd11IfTransDeferEnerDetects": cd11IfTransDeferEnerDetects,
       "cd11IfRecFrameMacCrcErrors": cd11IfRecFrameMacCrcErrors,
       "cd11IfSsidMismatches": cd11IfSsidMismatches,
       "cd11IfRogueApDetectedTable": cd11IfRogueApDetectedTable,
       "cd11IfRogueApDetectedEntry": cd11IfRogueApDetectedEntry,
       "cd11IfRogueApMacAddr": cd11IfRogueApMacAddr,
       "cd11IfRogueApName": cd11IfRogueApName,
       "ciscoDot11IfMIBConformance": ciscoDot11IfMIBConformance,
       "ciscoDot11IfMIBCompliances": ciscoDot11IfMIBCompliances,
       "ciscoDot11IfCompliance": ciscoDot11IfCompliance,
       "ciscoDot11IfComplianceRev1": ciscoDot11IfComplianceRev1,
       "ciscoDot11IfComplianceRev2": ciscoDot11IfComplianceRev2,
       "ciscoDot11IfComplianceRev3": ciscoDot11IfComplianceRev3,
       "ciscoDot11IfComplianceRev4": ciscoDot11IfComplianceRev4,
       "ciscoDot11IfMIBGroups": ciscoDot11IfMIBGroups,
       "cd11IfManagementGroup": cd11IfManagementGroup,
       "cd11IfPhyConfigGroup": cd11IfPhyConfigGroup,
       "cd11IfMacStatisticsGroup": cd11IfMacStatisticsGroup,
       "cd11IfVlanEncryptKeyConfigGroup": cd11IfVlanEncryptKeyConfigGroup,
       "cd11IfDomainCapabilityGroup": cd11IfDomainCapabilityGroup,
       "cd11IfPhyMacCapabilityGroup": cd11IfPhyMacCapabilityGroup,
       "cd11IfAuthAlgMethodListGroup": cd11IfAuthAlgMethodListGroup,
       "cd11IfRadioManageGroup": cd11IfRadioManageGroup,
       "cd11IfAssociationManageGroup": cd11IfAssociationManageGroup,
       "cd11IfSsidAssociationGroup": cd11IfSsidAssociationGroup,
       "cd11IfVlanManageGroup": cd11IfVlanManageGroup,
       "cd11IfRemoteMonitoringGroup": cd11IfRemoteMonitoringGroup,
       "cd11IfPhyConfigGroupRev1": cd11IfPhyConfigGroupRev1,
       "cd11IfPhyErpConfigGroup": cd11IfPhyErpConfigGroup,
       "cd11IfVlanWepManageGroup": cd11IfVlanWepManageGroup,
       "cd11IfRogueApDetectedGroup": cd11IfRogueApDetectedGroup,
       "cd11IfStationManageGroup": cd11IfStationManageGroup,
       "cd11IfNativeRadioManageGroup": cd11IfNativeRadioManageGroup,
       "cd11IfDataRatesSensitivityGroup": cd11IfDataRatesSensitivityGroup,
       "cd11IfMonitorNotificationGroup": cd11IfMonitorNotificationGroup,
       "cd11Ifdot11UpgradeStatusGroup": cd11Ifdot11UpgradeStatusGroup,
       "cd11Ifdot11MobileStationScanGroup": cd11Ifdot11MobileStationScanGroup}
)
