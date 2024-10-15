# SNMP MIB module (REDLINE-AN80I-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDLINE-AN80I-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:28 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(redlineSystem,) = mibBuilder.importSymbols(
    "REDLINE-MIB",
    "redlineSystem")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

redlineAn80iMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3)
)
redlineAn80iMib.setRevisions(
        ("2005-11-29 15:43",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedlineAn80iTrapDefinitions_ObjectIdentity = ObjectIdentity
redlineAn80iTrapDefinitions = _RedlineAn80iTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0)
)
_RedlineAn80iPtpPmpObjects_ObjectIdentity = ObjectIdentity
redlineAn80iPtpPmpObjects = _RedlineAn80iPtpPmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1)
)
_RedlineAn80iSystemObjects_ObjectIdentity = ObjectIdentity
redlineAn80iSystemObjects = _RedlineAn80iSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1)
)
_An80iOptionsKeyTable_Object = MibTable
an80iOptionsKeyTable = _An80iOptionsKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    an80iOptionsKeyTable.setStatus("current")
_An80iOptionsKeyEntry_Object = MibTableRow
an80iOptionsKeyEntry = _An80iOptionsKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1)
)
an80iOptionsKeyEntry.setIndexNames(
    (0, "REDLINE-AN80I-MIB", "an80iOptionsKeyId"),
)
if mibBuilder.loadTexts:
    an80iOptionsKeyEntry.setStatus("current")


class _An80iOptionsKeyId_Type(Integer32):
    """Custom type an80iOptionsKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_An80iOptionsKeyId_Type.__name__ = "Integer32"
_An80iOptionsKeyId_Object = MibTableColumn
an80iOptionsKeyId = _An80iOptionsKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 1),
    _An80iOptionsKeyId_Type()
)
an80iOptionsKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an80iOptionsKeyId.setStatus("current")
_An80iOptionsKey_Type = DisplayString
_An80iOptionsKey_Object = MibTableColumn
an80iOptionsKey = _An80iOptionsKey_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 2),
    _An80iOptionsKey_Type()
)
an80iOptionsKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iOptionsKey.setStatus("current")
_An80iOptionsKeyStatus_Type = RowStatus
_An80iOptionsKeyStatus_Object = MibTableColumn
an80iOptionsKeyStatus = _An80iOptionsKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 3),
    _An80iOptionsKeyStatus_Type()
)
an80iOptionsKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iOptionsKeyStatus.setStatus("current")
_An80iHardwareType_Type = Integer32
_An80iHardwareType_Object = MibScalar
an80iHardwareType = _An80iHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 2),
    _An80iHardwareType_Type()
)
an80iHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iHardwareType.setStatus("current")
_An80iRadioType_Type = Integer32
_An80iRadioType_Object = MibScalar
an80iRadioType = _An80iRadioType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 3),
    _An80iRadioType_Type()
)
an80iRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iRadioType.setStatus("current")


class _An80iSaveConfig_Type(Integer32):
    """Custom type an80iSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("saveConfig", 2))
    )


_An80iSaveConfig_Type.__name__ = "Integer32"
_An80iSaveConfig_Object = MibScalar
an80iSaveConfig = _An80iSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 4),
    _An80iSaveConfig_Type()
)
an80iSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iSaveConfig.setStatus("current")


class _An80iActivateConfig_Type(Integer32):
    """Custom type an80iActivateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeConfig", 2),
          ("noop", 1))
    )


_An80iActivateConfig_Type.__name__ = "Integer32"
_An80iActivateConfig_Object = MibScalar
an80iActivateConfig = _An80iActivateConfig_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 5),
    _An80iActivateConfig_Type()
)
an80iActivateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iActivateConfig.setStatus("current")
_RedlineAn80iWirelesObjects_ObjectIdentity = ObjectIdentity
redlineAn80iWirelesObjects = _RedlineAn80iWirelesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2)
)


class _An80iAntennaAllignmentMode_Type(Integer32):
    """Custom type an80iAntennaAllignmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("buzzer", 2),
          ("off", 1))
    )


_An80iAntennaAllignmentMode_Type.__name__ = "Integer32"
_An80iAntennaAllignmentMode_Object = MibScalar
an80iAntennaAllignmentMode = _An80iAntennaAllignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 1),
    _An80iAntennaAllignmentMode_Type()
)
an80iAntennaAllignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iAntennaAllignmentMode.setStatus("current")


class _An80iCurrTxPower_Type(Integer32):
    """Custom type an80iCurrTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 20),
    )


_An80iCurrTxPower_Type.__name__ = "Integer32"
_An80iCurrTxPower_Object = MibScalar
an80iCurrTxPower = _An80iCurrTxPower_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 2),
    _An80iCurrTxPower_Type()
)
an80iCurrTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iCurrTxPower.setStatus("current")


class _An80iChannelAutoScan_Type(Integer32):
    """Custom type an80iChannelAutoScan based on Integer32"""
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


_An80iChannelAutoScan_Type.__name__ = "Integer32"
_An80iChannelAutoScan_Object = MibScalar
an80iChannelAutoScan = _An80iChannelAutoScan_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 3),
    _An80iChannelAutoScan_Type()
)
an80iChannelAutoScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iChannelAutoScan.setStatus("current")
_An80iCurrFrequency_Type = Integer32
_An80iCurrFrequency_Object = MibScalar
an80iCurrFrequency = _An80iCurrFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 4),
    _An80iCurrFrequency_Type()
)
an80iCurrFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iCurrFrequency.setStatus("current")
if mibBuilder.loadTexts:
    an80iCurrFrequency.setUnits("KHz")
_An80iOPeratingFrequency_Type = Integer32
_An80iOPeratingFrequency_Object = MibScalar
an80iOPeratingFrequency = _An80iOPeratingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 5),
    _An80iOPeratingFrequency_Type()
)
an80iOPeratingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iOPeratingFrequency.setStatus("current")
if mibBuilder.loadTexts:
    an80iOPeratingFrequency.setUnits("KHz")


class _An80iMaxTxPower_Type(Integer32):
    """Custom type an80iMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_An80iMaxTxPower_Type.__name__ = "Integer32"
_An80iMaxTxPower_Object = MibScalar
an80iMaxTxPower = _An80iMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 6),
    _An80iMaxTxPower_Type()
)
an80iMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iMaxTxPower.setStatus("current")


class _An80iSystemMode_Type(Integer32):
    """Custom type an80iSystemMode based on Integer32"""
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
        *(("pmpMaster", 4),
          ("pmpSlave", 3),
          ("ptpMaster", 2),
          ("ptpSlave", 1))
    )


_An80iSystemMode_Type.__name__ = "Integer32"
_An80iSystemMode_Object = MibScalar
an80iSystemMode = _An80iSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 7),
    _An80iSystemMode_Type()
)
an80iSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iSystemMode.setStatus("current")
_An80iRFStatusCode_Type = Integer32
_An80iRFStatusCode_Object = MibScalar
an80iRFStatusCode = _An80iRFStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 8),
    _An80iRFStatusCode_Type()
)
an80iRFStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iRFStatusCode.setStatus("current")


class _An80iDFSAction_Type(Integer32):
    """Custom type an80iDFSAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("changeFreq", 3),
          ("none", 1),
          ("txDisabled", 2))
    )


_An80iDFSAction_Type.__name__ = "Integer32"
_An80iDFSAction_Object = MibScalar
an80iDFSAction = _An80iDFSAction_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 9),
    _An80iDFSAction_Type()
)
an80iDFSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iDFSAction.setStatus("current")
_An80iAntennaGain_Type = Integer32
_An80iAntennaGain_Object = MibScalar
an80iAntennaGain = _An80iAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 10),
    _An80iAntennaGain_Type()
)
an80iAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iAntennaGain.setStatus("current")
_An80iActiveRFLinks_Type = Integer32
_An80iActiveRFLinks_Object = MibScalar
an80iActiveRFLinks = _An80iActiveRFLinks_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 11),
    _An80iActiveRFLinks_Type()
)
an80iActiveRFLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iActiveRFLinks.setStatus("current")


class _An80iAtpControl_Type(Integer32):
    """Custom type an80iAtpControl based on Integer32"""
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


_An80iAtpControl_Type.__name__ = "Integer32"
_An80iAtpControl_Object = MibScalar
an80iAtpControl = _An80iAtpControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 12),
    _An80iAtpControl_Type()
)
an80iAtpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iAtpControl.setStatus("current")


class _An80iTurboModeControl_Type(Integer32):
    """Custom type an80iTurboModeControl based on Integer32"""
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


_An80iTurboModeControl_Type.__name__ = "Integer32"
_An80iTurboModeControl_Object = MibScalar
an80iTurboModeControl = _An80iTurboModeControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 13),
    _An80iTurboModeControl_Type()
)
an80iTurboModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iTurboModeControl.setStatus("current")


class _An80iChannelWidth_Type(Integer32):
    """Custom type an80iChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("chWidth10MHz", 5),
          ("chWidth20MHz", 6),
          ("chWidth40MHz", 7))
    )


_An80iChannelWidth_Type.__name__ = "Integer32"
_An80iChannelWidth_Object = MibScalar
an80iChannelWidth = _An80iChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 14),
    _An80iChannelWidth_Type()
)
an80iChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iChannelWidth.setStatus("current")
_RedlineAn80iEthernetObjects_ObjectIdentity = ObjectIdentity
redlineAn80iEthernetObjects = _RedlineAn80iEthernetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3)
)


class _An80iEtherPortConn_Type(Integer32):
    """Custom type an80iEtherPortConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("crossover", 3),
          ("normal", 2))
    )


_An80iEtherPortConn_Type.__name__ = "Integer32"
_An80iEtherPortConn_Object = MibScalar
an80iEtherPortConn = _An80iEtherPortConn_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 1),
    _An80iEtherPortConn_Type()
)
an80iEtherPortConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iEtherPortConn.setStatus("current")


class _An80iEtherPortMode_Type(Integer32):
    """Custom type an80iEtherPortMode based on Integer32"""
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
        *(("auto", 1),
          ("e100fd", 5),
          ("e100hd", 4),
          ("e10fd", 3),
          ("e10hd", 2))
    )


_An80iEtherPortMode_Type.__name__ = "Integer32"
_An80iEtherPortMode_Object = MibScalar
an80iEtherPortMode = _An80iEtherPortMode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 2),
    _An80iEtherPortMode_Type()
)
an80iEtherPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iEtherPortMode.setStatus("current")


class _An80iFlowControl_Type(Integer32):
    """Custom type an80iFlowControl based on Integer32"""
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


_An80iFlowControl_Type.__name__ = "Integer32"
_An80iFlowControl_Object = MibScalar
an80iFlowControl = _An80iFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 3),
    _An80iFlowControl_Type()
)
an80iFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iFlowControl.setStatus("current")


class _An80iLowLatencyMode_Type(Integer32):
    """Custom type an80iLowLatencyMode based on Integer32"""
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


_An80iLowLatencyMode_Type.__name__ = "Integer32"
_An80iLowLatencyMode_Object = MibScalar
an80iLowLatencyMode = _An80iLowLatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 4),
    _An80iLowLatencyMode_Type()
)
an80iLowLatencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iLowLatencyMode.setStatus("current")


class _An80iEthernetFollowsWireless_Type(Integer32):
    """Custom type an80iEthernetFollowsWireless based on Integer32"""
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


_An80iEthernetFollowsWireless_Type.__name__ = "Integer32"
_An80iEthernetFollowsWireless_Object = MibScalar
an80iEthernetFollowsWireless = _An80iEthernetFollowsWireless_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 5),
    _An80iEthernetFollowsWireless_Type()
)
an80iEthernetFollowsWireless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iEthernetFollowsWireless.setStatus("current")


class _An80iEthernetFollowsWirelessTimeout_Type(Integer32):
    """Custom type an80iEthernetFollowsWirelessTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_An80iEthernetFollowsWirelessTimeout_Type.__name__ = "Integer32"
_An80iEthernetFollowsWirelessTimeout_Object = MibScalar
an80iEthernetFollowsWirelessTimeout = _An80iEthernetFollowsWirelessTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 6),
    _An80iEthernetFollowsWirelessTimeout_Type()
)
an80iEthernetFollowsWirelessTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iEthernetFollowsWirelessTimeout.setStatus("current")
_RedlineAn80iManagObjects_ObjectIdentity = ObjectIdentity
redlineAn80iManagObjects = _RedlineAn80iManagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4)
)


class _An80iHttpAccess_Type(Integer32):
    """Custom type an80iHttpAccess based on Integer32"""
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


_An80iHttpAccess_Type.__name__ = "Integer32"
_An80iHttpAccess_Object = MibScalar
an80iHttpAccess = _An80iHttpAccess_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 1),
    _An80iHttpAccess_Type()
)
an80iHttpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iHttpAccess.setStatus("current")


class _An80iTelnetAccess_Type(Integer32):
    """Custom type an80iTelnetAccess based on Integer32"""
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


_An80iTelnetAccess_Type.__name__ = "Integer32"
_An80iTelnetAccess_Object = MibScalar
an80iTelnetAccess = _An80iTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 2),
    _An80iTelnetAccess_Type()
)
an80iTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iTelnetAccess.setStatus("current")
_An80iTelnetPort_Type = InetPortNumber
_An80iTelnetPort_Object = MibScalar
an80iTelnetPort = _An80iTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 3),
    _An80iTelnetPort_Type()
)
an80iTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iTelnetPort.setStatus("current")
_RedlineAn80iSWUpgradeObjects_ObjectIdentity = ObjectIdentity
redlineAn80iSWUpgradeObjects = _RedlineAn80iSWUpgradeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5)
)
_An80iSwDownloadTftpAddressType_Type = InetAddressType
_An80iSwDownloadTftpAddressType_Object = MibScalar
an80iSwDownloadTftpAddressType = _An80iSwDownloadTftpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 1),
    _An80iSwDownloadTftpAddressType_Type()
)
an80iSwDownloadTftpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iSwDownloadTftpAddressType.setStatus("current")
_An80iSwDownloadTftpAddress_Type = InetAddress
_An80iSwDownloadTftpAddress_Object = MibScalar
an80iSwDownloadTftpAddress = _An80iSwDownloadTftpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 2),
    _An80iSwDownloadTftpAddress_Type()
)
an80iSwDownloadTftpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iSwDownloadTftpAddress.setStatus("current")


class _An80iSwDownloadTftpFile_Type(DisplayString):
    """Custom type an80iSwDownloadTftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_An80iSwDownloadTftpFile_Type.__name__ = "DisplayString"
_An80iSwDownloadTftpFile_Object = MibScalar
an80iSwDownloadTftpFile = _An80iSwDownloadTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 3),
    _An80iSwDownloadTftpFile_Type()
)
an80iSwDownloadTftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iSwDownloadTftpFile.setStatus("current")


class _An80iSwDownloadStatus_Type(Integer32):
    """Custom type an80iSwDownloadStatus based on Integer32"""
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
        *(("download", 1),
          ("failed", 4),
          ("inProgress", 2),
          ("success", 3))
    )


_An80iSwDownloadStatus_Type.__name__ = "Integer32"
_An80iSwDownloadStatus_Object = MibScalar
an80iSwDownloadStatus = _An80iSwDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 4),
    _An80iSwDownloadStatus_Type()
)
an80iSwDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iSwDownloadStatus.setStatus("current")


class _An80iSwDownloadControl_Type(Integer32):
    """Custom type an80iSwDownloadControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("startUpgrade", 2))
    )


_An80iSwDownloadControl_Type.__name__ = "Integer32"
_An80iSwDownloadControl_Object = MibScalar
an80iSwDownloadControl = _An80iSwDownloadControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 5),
    _An80iSwDownloadControl_Type()
)
an80iSwDownloadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iSwDownloadControl.setStatus("current")
_RedlineAn80iPmpObjects_ObjectIdentity = ObjectIdentity
redlineAn80iPmpObjects = _RedlineAn80iPmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2)
)
_RedlineAn80iPmpWirelesObjects_ObjectIdentity = ObjectIdentity
redlineAn80iPmpWirelesObjects = _RedlineAn80iPmpWirelesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1)
)


class _An80iRegistrationPeriod_Type(Integer32):
    """Custom type an80iRegistrationPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_An80iRegistrationPeriod_Type.__name__ = "Integer32"
_An80iRegistrationPeriod_Object = MibScalar
an80iRegistrationPeriod = _An80iRegistrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 1),
    _An80iRegistrationPeriod_Type()
)
an80iRegistrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iRegistrationPeriod.setStatus("current")


class _An80iMaximumDistance_Type(Integer32):
    """Custom type an80iMaximumDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_An80iMaximumDistance_Type.__name__ = "Integer32"
_An80iMaximumDistance_Object = MibScalar
an80iMaximumDistance = _An80iMaximumDistance_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 2),
    _An80iMaximumDistance_Type()
)
an80iMaximumDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iMaximumDistance.setStatus("current")
_An80iRegisteredStations_Type = Integer32
_An80iRegisteredStations_Object = MibScalar
an80iRegisteredStations = _An80iRegisteredStations_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 3),
    _An80iRegisteredStations_Type()
)
an80iRegisteredStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iRegisteredStations.setStatus("current")
_An80iRegisteredConnections_Type = Integer32
_An80iRegisteredConnections_Object = MibScalar
an80iRegisteredConnections = _An80iRegisteredConnections_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 4),
    _An80iRegisteredConnections_Type()
)
an80iRegisteredConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iRegisteredConnections.setStatus("current")


class _An80iMaxId_Type(Integer32):
    """Custom type an80iMaxId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_An80iMaxId_Type.__name__ = "Integer32"
_An80iMaxId_Object = MibScalar
an80iMaxId = _An80iMaxId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 5),
    _An80iMaxId_Type()
)
an80iMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iMaxId.setStatus("current")
_An80iNextAvailId_Type = Integer32
_An80iNextAvailId_Object = MibScalar
an80iNextAvailId = _An80iNextAvailId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 6),
    _An80iNextAvailId_Type()
)
an80iNextAvailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iNextAvailId.setStatus("current")
_An80iLastModifId_Type = Integer32
_An80iLastModifId_Object = MibScalar
an80iLastModifId = _An80iLastModifId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 7),
    _An80iLastModifId_Type()
)
an80iLastModifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iLastModifId.setStatus("current")


class _An80iSaveIdConfiguration_Type(Integer32):
    """Custom type an80iSaveIdConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("save", 2))
    )


_An80iSaveIdConfiguration_Type.__name__ = "Integer32"
_An80iSaveIdConfiguration_Object = MibScalar
an80iSaveIdConfiguration = _An80iSaveIdConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 8),
    _An80iSaveIdConfiguration_Type()
)
an80iSaveIdConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iSaveIdConfiguration.setStatus("current")
_RedlineAn80iPtpObjects_ObjectIdentity = ObjectIdentity
redlineAn80iPtpObjects = _RedlineAn80iPtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3)
)
_RedlineAn80iPtpSystemObjects_ObjectIdentity = ObjectIdentity
redlineAn80iPtpSystemObjects = _RedlineAn80iPtpSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3, 1)
)


class _An80iResetStatistics_Type(Integer32):
    """Custom type an80iResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_An80iResetStatistics_Type.__name__ = "Integer32"
_An80iResetStatistics_Object = MibScalar
an80iResetStatistics = _An80iResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3, 1, 1),
    _An80iResetStatistics_Type()
)
an80iResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iResetStatistics.setStatus("current")
_RedlineAn80iConformance_ObjectIdentity = ObjectIdentity
redlineAn80iConformance = _RedlineAn80iConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5)
)
_RedlineAn80iGroups_ObjectIdentity = ObjectIdentity
redlineAn80iGroups = _RedlineAn80iGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1)
)
_RedlineAn80iCompls_ObjectIdentity = ObjectIdentity
redlineAn80iCompls = _RedlineAn80iCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 2)
)

# Managed Objects groups

redlineAn80iPtpPmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 1)
)
redlineAn80iPtpPmpGroup.setObjects(
      *(("REDLINE-AN80I-MIB", "an80iOptionsKey"),
        ("REDLINE-AN80I-MIB", "an80iHardwareType"),
        ("REDLINE-AN80I-MIB", "an80iRadioType"),
        ("REDLINE-AN80I-MIB", "an80iSaveConfig"),
        ("REDLINE-AN80I-MIB", "an80iActivateConfig"),
        ("REDLINE-AN80I-MIB", "an80iAntennaAllignmentMode"),
        ("REDLINE-AN80I-MIB", "an80iCurrTxPower"),
        ("REDLINE-AN80I-MIB", "an80iChannelAutoScan"),
        ("REDLINE-AN80I-MIB", "an80iCurrFrequency"),
        ("REDLINE-AN80I-MIB", "an80iOPeratingFrequency"),
        ("REDLINE-AN80I-MIB", "an80iMaxTxPower"),
        ("REDLINE-AN80I-MIB", "an80iSystemMode"),
        ("REDLINE-AN80I-MIB", "an80iRFStatusCode"),
        ("REDLINE-AN80I-MIB", "an80iDFSAction"),
        ("REDLINE-AN80I-MIB", "an80iAntennaGain"),
        ("REDLINE-AN80I-MIB", "an80iActiveRFLinks"),
        ("REDLINE-AN80I-MIB", "an80iAtpControl"),
        ("REDLINE-AN80I-MIB", "an80iTurboModeControl"),
        ("REDLINE-AN80I-MIB", "an80iEtherPortConn"),
        ("REDLINE-AN80I-MIB", "an80iEtherPortMode"),
        ("REDLINE-AN80I-MIB", "an80iFlowControl"),
        ("REDLINE-AN80I-MIB", "an80iLowLatencyMode"),
        ("REDLINE-AN80I-MIB", "an80iEthernetFollowsWireless"),
        ("REDLINE-AN80I-MIB", "an80iEthernetFollowsWirelessTimeout"),
        ("REDLINE-AN80I-MIB", "an80iHttpAccess"),
        ("REDLINE-AN80I-MIB", "an80iTelnetAccess"),
        ("REDLINE-AN80I-MIB", "an80iTelnetPort"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadStatus"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadControl"))
)
if mibBuilder.loadTexts:
    redlineAn80iPtpPmpGroup.setStatus("current")

redlineAn80iPmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 2)
)
redlineAn80iPmpGroup.setObjects(
      *(("REDLINE-AN80I-MIB", "an80iRegistrationPeriod"),
        ("REDLINE-AN80I-MIB", "an80iMaximumDistance"),
        ("REDLINE-AN80I-MIB", "an80iRegisteredStations"),
        ("REDLINE-AN80I-MIB", "an80iRegisteredConnections"),
        ("REDLINE-AN80I-MIB", "an80iMaxId"),
        ("REDLINE-AN80I-MIB", "an80iNextAvailId"),
        ("REDLINE-AN80I-MIB", "an80iLastModifId"),
        ("REDLINE-AN80I-MIB", "an80iSaveIdConfiguration"))
)
if mibBuilder.loadTexts:
    redlineAn80iPmpGroup.setStatus("current")

redlineAn80iPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 3)
)
redlineAn80iPtpGroup.setObjects(
    ("REDLINE-AN80I-MIB", "an80iResetStatistics")
)
if mibBuilder.loadTexts:
    redlineAn80iPtpGroup.setStatus("current")


# Notification objects

an80iPswdChangeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    an80iPswdChangeFailTrap.setStatus(
        "current"
    )

an80iFirmwareConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    an80iFirmwareConfigFailTrap.setStatus(
        "current"
    )

an80iEepromCorruptedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 3)
)
if mibBuilder.loadTexts:
    an80iEepromCorruptedTrap.setStatus(
        "current"
    )

an80iHardwareFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 4)
)
if mibBuilder.loadTexts:
    an80iHardwareFailTrap.setStatus(
        "current"
    )

an80iSaveConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 5)
)
if mibBuilder.loadTexts:
    an80iSaveConfigTrap.setStatus(
        "current"
    )

an80iDFSEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 6)
)
if mibBuilder.loadTexts:
    an80iDFSEventTrap.setStatus(
        "current"
    )

an80iIdChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 7)
)
an80iIdChangedTrap.setObjects(
    ("REDLINE-AN80I-MIB", "an80iLastModifId")
)
if mibBuilder.loadTexts:
    an80iIdChangedTrap.setStatus(
        "current"
    )

an80iSWUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 8)
)
an80iSWUpgradeFailed.setObjects(
      *(("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"))
)
if mibBuilder.loadTexts:
    an80iSWUpgradeFailed.setStatus(
        "current"
    )

an80iSWUpgradeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 9)
)
an80iSWUpgradeSuccess.setObjects(
      *(("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"),
        ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"))
)
if mibBuilder.loadTexts:
    an80iSWUpgradeSuccess.setStatus(
        "current"
    )


# Notifications groups

redlineAn80iNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 4)
)
redlineAn80iNotificationGroup.setObjects(
      *(("REDLINE-AN80I-MIB", "an80iPswdChangeFailTrap"),
        ("REDLINE-AN80I-MIB", "an80iFirmwareConfigFailTrap"),
        ("REDLINE-AN80I-MIB", "an80iEepromCorruptedTrap"),
        ("REDLINE-AN80I-MIB", "an80iHardwareFailTrap"),
        ("REDLINE-AN80I-MIB", "an80iSaveConfigTrap"),
        ("REDLINE-AN80I-MIB", "an80iDFSEventTrap"),
        ("REDLINE-AN80I-MIB", "an80iIdChangedTrap"),
        ("REDLINE-AN80I-MIB", "an80iSWUpgradeFailed"),
        ("REDLINE-AN80I-MIB", "an80iSWUpgradeSuccess"))
)
if mibBuilder.loadTexts:
    redlineAn80iNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

redlineAn80iCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    redlineAn80iCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDLINE-AN80I-MIB",
    **{"redlineAn80iMib": redlineAn80iMib,
       "redlineAn80iTrapDefinitions": redlineAn80iTrapDefinitions,
       "an80iPswdChangeFailTrap": an80iPswdChangeFailTrap,
       "an80iFirmwareConfigFailTrap": an80iFirmwareConfigFailTrap,
       "an80iEepromCorruptedTrap": an80iEepromCorruptedTrap,
       "an80iHardwareFailTrap": an80iHardwareFailTrap,
       "an80iSaveConfigTrap": an80iSaveConfigTrap,
       "an80iDFSEventTrap": an80iDFSEventTrap,
       "an80iIdChangedTrap": an80iIdChangedTrap,
       "an80iSWUpgradeFailed": an80iSWUpgradeFailed,
       "an80iSWUpgradeSuccess": an80iSWUpgradeSuccess,
       "redlineAn80iPtpPmpObjects": redlineAn80iPtpPmpObjects,
       "redlineAn80iSystemObjects": redlineAn80iSystemObjects,
       "an80iOptionsKeyTable": an80iOptionsKeyTable,
       "an80iOptionsKeyEntry": an80iOptionsKeyEntry,
       "an80iOptionsKeyId": an80iOptionsKeyId,
       "an80iOptionsKey": an80iOptionsKey,
       "an80iOptionsKeyStatus": an80iOptionsKeyStatus,
       "an80iHardwareType": an80iHardwareType,
       "an80iRadioType": an80iRadioType,
       "an80iSaveConfig": an80iSaveConfig,
       "an80iActivateConfig": an80iActivateConfig,
       "redlineAn80iWirelesObjects": redlineAn80iWirelesObjects,
       "an80iAntennaAllignmentMode": an80iAntennaAllignmentMode,
       "an80iCurrTxPower": an80iCurrTxPower,
       "an80iChannelAutoScan": an80iChannelAutoScan,
       "an80iCurrFrequency": an80iCurrFrequency,
       "an80iOPeratingFrequency": an80iOPeratingFrequency,
       "an80iMaxTxPower": an80iMaxTxPower,
       "an80iSystemMode": an80iSystemMode,
       "an80iRFStatusCode": an80iRFStatusCode,
       "an80iDFSAction": an80iDFSAction,
       "an80iAntennaGain": an80iAntennaGain,
       "an80iActiveRFLinks": an80iActiveRFLinks,
       "an80iAtpControl": an80iAtpControl,
       "an80iTurboModeControl": an80iTurboModeControl,
       "an80iChannelWidth": an80iChannelWidth,
       "redlineAn80iEthernetObjects": redlineAn80iEthernetObjects,
       "an80iEtherPortConn": an80iEtherPortConn,
       "an80iEtherPortMode": an80iEtherPortMode,
       "an80iFlowControl": an80iFlowControl,
       "an80iLowLatencyMode": an80iLowLatencyMode,
       "an80iEthernetFollowsWireless": an80iEthernetFollowsWireless,
       "an80iEthernetFollowsWirelessTimeout": an80iEthernetFollowsWirelessTimeout,
       "redlineAn80iManagObjects": redlineAn80iManagObjects,
       "an80iHttpAccess": an80iHttpAccess,
       "an80iTelnetAccess": an80iTelnetAccess,
       "an80iTelnetPort": an80iTelnetPort,
       "redlineAn80iSWUpgradeObjects": redlineAn80iSWUpgradeObjects,
       "an80iSwDownloadTftpAddressType": an80iSwDownloadTftpAddressType,
       "an80iSwDownloadTftpAddress": an80iSwDownloadTftpAddress,
       "an80iSwDownloadTftpFile": an80iSwDownloadTftpFile,
       "an80iSwDownloadStatus": an80iSwDownloadStatus,
       "an80iSwDownloadControl": an80iSwDownloadControl,
       "redlineAn80iPmpObjects": redlineAn80iPmpObjects,
       "redlineAn80iPmpWirelesObjects": redlineAn80iPmpWirelesObjects,
       "an80iRegistrationPeriod": an80iRegistrationPeriod,
       "an80iMaximumDistance": an80iMaximumDistance,
       "an80iRegisteredStations": an80iRegisteredStations,
       "an80iRegisteredConnections": an80iRegisteredConnections,
       "an80iMaxId": an80iMaxId,
       "an80iNextAvailId": an80iNextAvailId,
       "an80iLastModifId": an80iLastModifId,
       "an80iSaveIdConfiguration": an80iSaveIdConfiguration,
       "redlineAn80iPtpObjects": redlineAn80iPtpObjects,
       "redlineAn80iPtpSystemObjects": redlineAn80iPtpSystemObjects,
       "an80iResetStatistics": an80iResetStatistics,
       "redlineAn80iConformance": redlineAn80iConformance,
       "redlineAn80iGroups": redlineAn80iGroups,
       "redlineAn80iPtpPmpGroup": redlineAn80iPtpPmpGroup,
       "redlineAn80iPmpGroup": redlineAn80iPmpGroup,
       "redlineAn80iPtpGroup": redlineAn80iPtpGroup,
       "redlineAn80iNotificationGroup": redlineAn80iNotificationGroup,
       "redlineAn80iCompls": redlineAn80iCompls,
       "redlineAn80iCompliance": redlineAn80iCompliance}
)
