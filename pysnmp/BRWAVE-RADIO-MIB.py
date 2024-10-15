# SNMP MIB module (BRWAVE-RADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRWAVE-RADIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:38 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

brwaveRadioMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 1, 1, 3)
)
brwaveRadioMibModule.setRevisions(
        ("2006-07-06 11:00",
         "2005-05-26 11:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BridgeWave_ObjectIdentity = ObjectIdentity
bridgeWave = _BridgeWave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080)
)
if mibBuilder.loadTexts:
    bridgeWave.setStatus("current")
_BrwaveReg_ObjectIdentity = ObjectIdentity
brwaveReg = _BrwaveReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 1)
)
if mibBuilder.loadTexts:
    brwaveReg.setStatus("current")
_BrwaveMibs_ObjectIdentity = ObjectIdentity
brwaveMibs = _BrwaveMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 1, 1)
)
if mibBuilder.loadTexts:
    brwaveMibs.setStatus("current")
_BrwaveModules_ObjectIdentity = ObjectIdentity
brwaveModules = _BrwaveModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 1, 2)
)
if mibBuilder.loadTexts:
    brwaveModules.setStatus("current")
_BrwaveRadioFE60_ObjectIdentity = ObjectIdentity
brwaveRadioFE60 = _BrwaveRadioFE60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 1, 2, 1)
)
if mibBuilder.loadTexts:
    brwaveRadioFE60.setStatus("current")
_BrwaveRadioGE60_ObjectIdentity = ObjectIdentity
brwaveRadioGE60 = _BrwaveRadioGE60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 1, 2, 2)
)
if mibBuilder.loadTexts:
    brwaveRadioGE60.setStatus("current")
_BrwaveRadioAR60_ObjectIdentity = ObjectIdentity
brwaveRadioAR60 = _BrwaveRadioAR60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 1, 2, 3)
)
if mibBuilder.loadTexts:
    brwaveRadioAR60.setStatus("current")
_BrwaveCommon_ObjectIdentity = ObjectIdentity
brwaveCommon = _BrwaveCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 2)
)
if mibBuilder.loadTexts:
    brwaveCommon.setStatus("current")
_BrwaveRadioSn_Type = DisplayString
_BrwaveRadioSn_Object = MibScalar
brwaveRadioSn = _BrwaveRadioSn_Object(
    (1, 3, 6, 1, 4, 1, 6080, 2, 1),
    _BrwaveRadioSn_Type()
)
brwaveRadioSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioSn.setStatus("current")
_BrwaveUnitModel_Type = DisplayString
_BrwaveUnitModel_Object = MibScalar
brwaveUnitModel = _BrwaveUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 6080, 2, 2),
    _BrwaveUnitModel_Type()
)
brwaveUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveUnitModel.setStatus("current")
_BrwaveBbSn_Type = DisplayString
_BrwaveBbSn_Object = MibScalar
brwaveBbSn = _BrwaveBbSn_Object(
    (1, 3, 6, 1, 4, 1, 6080, 2, 3),
    _BrwaveBbSn_Type()
)
brwaveBbSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveBbSn.setStatus("current")
_BrwaveIfSn_Type = DisplayString
_BrwaveIfSn_Object = MibScalar
brwaveIfSn = _BrwaveIfSn_Object(
    (1, 3, 6, 1, 4, 1, 6080, 2, 4),
    _BrwaveIfSn_Type()
)
brwaveIfSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveIfSn.setStatus("current")
_BrwaveMmwSn_Type = DisplayString
_BrwaveMmwSn_Object = MibScalar
brwaveMmwSn = _BrwaveMmwSn_Object(
    (1, 3, 6, 1, 4, 1, 6080, 2, 5),
    _BrwaveMmwSn_Type()
)
brwaveMmwSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveMmwSn.setStatus("current")
_BrwaveTrapCount_Type = Unsigned32
_BrwaveTrapCount_Object = MibScalar
brwaveTrapCount = _BrwaveTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 6080, 2, 6),
    _BrwaveTrapCount_Type()
)
brwaveTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveTrapCount.setStatus("current")
_BrwaveProducts_ObjectIdentity = ObjectIdentity
brwaveProducts = _BrwaveProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3)
)
if mibBuilder.loadTexts:
    brwaveProducts.setStatus("current")
_BrwaveRadio_ObjectIdentity = ObjectIdentity
brwaveRadio = _BrwaveRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1)
)
if mibBuilder.loadTexts:
    brwaveRadio.setStatus("current")
_BrwaveRadioFactorySetup_ObjectIdentity = ObjectIdentity
brwaveRadioFactorySetup = _BrwaveRadioFactorySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 2)
)
if mibBuilder.loadTexts:
    brwaveRadioFactorySetup.setStatus("current")


class _BrwaveRadioTxBand_Type(Integer32):
    """Custom type brwaveRadioTxBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_BrwaveRadioTxBand_Type.__name__ = "Integer32"
_BrwaveRadioTxBand_Object = MibScalar
brwaveRadioTxBand = _BrwaveRadioTxBand_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 2, 1),
    _BrwaveRadioTxBand_Type()
)
brwaveRadioTxBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioTxBand.setStatus("current")


class _BrwaveRadioFactoryRate_Type(Integer32):
    """Custom type brwaveRadioFactoryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptRate", 1),
          ("mbps100", 3),
          ("mbps1000", 2))
    )


_BrwaveRadioFactoryRate_Type.__name__ = "Integer32"
_BrwaveRadioFactoryRate_Object = MibScalar
brwaveRadioFactoryRate = _BrwaveRadioFactoryRate_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 2, 3),
    _BrwaveRadioFactoryRate_Type()
)
brwaveRadioFactoryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioFactoryRate.setStatus("current")
_BrwaveRadioClearStats_Type = Integer32
_BrwaveRadioClearStats_Object = MibScalar
brwaveRadioClearStats = _BrwaveRadioClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 2, 4),
    _BrwaveRadioClearStats_Type()
)
brwaveRadioClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brwaveRadioClearStats.setStatus("current")
_BrwaveRadioStatus_ObjectIdentity = ObjectIdentity
brwaveRadioStatus = _BrwaveRadioStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3)
)
if mibBuilder.loadTexts:
    brwaveRadioStatus.setStatus("current")
_BrwaveRadioInVoltage_Type = Integer32
_BrwaveRadioInVoltage_Object = MibScalar
brwaveRadioInVoltage = _BrwaveRadioInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 1),
    _BrwaveRadioInVoltage_Type()
)
brwaveRadioInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioInVoltage.setStatus("current")
_BrwaveRadioUnitTemperature_Type = Integer32
_BrwaveRadioUnitTemperature_Object = MibScalar
brwaveRadioUnitTemperature = _BrwaveRadioUnitTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 2),
    _BrwaveRadioUnitTemperature_Type()
)
brwaveRadioUnitTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioUnitTemperature.setStatus("current")
_BrwaveRadioTxTemperature_Type = Integer32
_BrwaveRadioTxTemperature_Object = MibScalar
brwaveRadioTxTemperature = _BrwaveRadioTxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 3),
    _BrwaveRadioTxTemperature_Type()
)
brwaveRadioTxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioTxTemperature.setStatus("current")
_BrwaveRadioRSL_Type = Integer32
_BrwaveRadioRSL_Object = MibScalar
brwaveRadioRSL = _BrwaveRadioRSL_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 4),
    _BrwaveRadioRSL_Type()
)
brwaveRadioRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioRSL.setStatus("current")
_BrwaveRadioRSLVoltage_Type = DisplayString
_BrwaveRadioRSLVoltage_Object = MibScalar
brwaveRadioRSLVoltage = _BrwaveRadioRSLVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 5),
    _BrwaveRadioRSLVoltage_Type()
)
brwaveRadioRSLVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioRSLVoltage.setStatus("current")
_BrwaveRadioAbsRSL_Type = Integer32
_BrwaveRadioAbsRSL_Object = MibScalar
brwaveRadioAbsRSL = _BrwaveRadioAbsRSL_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 6),
    _BrwaveRadioAbsRSL_Type()
)
brwaveRadioAbsRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioAbsRSL.setStatus("current")
_BrwaveRadioRSLVoltageInt_Type = Integer32
_BrwaveRadioRSLVoltageInt_Object = MibScalar
brwaveRadioRSLVoltageInt = _BrwaveRadioRSLVoltageInt_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 7),
    _BrwaveRadioRSLVoltageInt_Type()
)
brwaveRadioRSLVoltageInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioRSLVoltageInt.setStatus("current")
_BrwaveCopperUtilization_Type = Integer32
_BrwaveCopperUtilization_Object = MibScalar
brwaveCopperUtilization = _BrwaveCopperUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 8),
    _BrwaveCopperUtilization_Type()
)
brwaveCopperUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveCopperUtilization.setStatus("current")
_BrwaveFiberUtilization_Type = Integer32
_BrwaveFiberUtilization_Object = MibScalar
brwaveFiberUtilization = _BrwaveFiberUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 9),
    _BrwaveFiberUtilization_Type()
)
brwaveFiberUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveFiberUtilization.setStatus("current")
_BrwaveRadioUtilization_Type = Integer32
_BrwaveRadioUtilization_Object = MibScalar
brwaveRadioUtilization = _BrwaveRadioUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 10),
    _BrwaveRadioUtilization_Type()
)
brwaveRadioUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioUtilization.setStatus("current")


class _BrwaveRadioFecError_Type(Integer32):
    """Custom type brwaveRadioFecError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("postFec", 2),
          ("preFec", 1))
    )


_BrwaveRadioFecError_Type.__name__ = "Integer32"
_BrwaveRadioFecError_Object = MibScalar
brwaveRadioFecError = _BrwaveRadioFecError_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 11),
    _BrwaveRadioFecError_Type()
)
brwaveRadioFecError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioFecError.setStatus("current")
_BrwaveRadioPreFecFlag_Type = Integer32
_BrwaveRadioPreFecFlag_Object = MibScalar
brwaveRadioPreFecFlag = _BrwaveRadioPreFecFlag_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 12),
    _BrwaveRadioPreFecFlag_Type()
)
brwaveRadioPreFecFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioPreFecFlag.setStatus("current")
_BrwaveRadioPostFecFlag_Type = Integer32
_BrwaveRadioPostFecFlag_Object = MibScalar
brwaveRadioPostFecFlag = _BrwaveRadioPostFecFlag_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 13),
    _BrwaveRadioPostFecFlag_Type()
)
brwaveRadioPostFecFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioPostFecFlag.setStatus("current")
_BrwaveRadioLinkRate_Type = Integer32
_BrwaveRadioLinkRate_Object = MibScalar
brwaveRadioLinkRate = _BrwaveRadioLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 14),
    _BrwaveRadioLinkRate_Type()
)
brwaveRadioLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brwaveRadioLinkRate.setStatus("current")
_BrwaveRadioEvents_ObjectIdentity = ObjectIdentity
brwaveRadioEvents = _BrwaveRadioEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9)
)
_BrwaveRadioEventsV2_ObjectIdentity = ObjectIdentity
brwaveRadioEventsV2 = _BrwaveRadioEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0)
)
_BrwaveRadioTrapObjs_ObjectIdentity = ObjectIdentity
brwaveRadioTrapObjs = _BrwaveRadioTrapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 1)
)


class _ManagerIP_Type(OctetString):
    """Custom type managerIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ManagerIP_Type.__name__ = "OctetString"
_ManagerIP_Object = MibScalar
managerIP = _ManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 1, 1),
    _ManagerIP_Type()
)
managerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managerIP.setStatus("current")


class _UserName_Type(OctetString):
    """Custom type userName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserName_Type.__name__ = "OctetString"
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_BrwaveConformance_ObjectIdentity = ObjectIdentity
brwaveConformance = _BrwaveConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 10)
)
_BrwaveRadioGroups_ObjectIdentity = ObjectIdentity
brwaveRadioGroups = _BrwaveRadioGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1)
)
_BrwaveCompliances_ObjectIdentity = ObjectIdentity
brwaveCompliances = _BrwaveCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 2)
)

# Managed Objects groups

brwaveCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1, 1)
)
brwaveCommonGroup.setObjects(
      *(("BRWAVE-RADIO-MIB", "brwaveRadioSn"),
        ("BRWAVE-RADIO-MIB", "brwaveUnitModel"),
        ("BRWAVE-RADIO-MIB", "brwaveTrapCount"))
)
if mibBuilder.loadTexts:
    brwaveCommonGroup.setStatus("current")

brwaveFactoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1, 2)
)
brwaveFactoryGroup.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioTxBand")
)
if mibBuilder.loadTexts:
    brwaveFactoryGroup.setStatus("current")

brwaveStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1, 3)
)
brwaveStatusGroup.setObjects(
      *(("BRWAVE-RADIO-MIB", "brwaveRadioInVoltage"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioRSL"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioRSLVoltage"))
)
if mibBuilder.loadTexts:
    brwaveStatusGroup.setStatus("current")


# Notification objects

brwaveErrorsOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 1)
)
brwaveErrorsOverThreshold.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
)
if mibBuilder.loadTexts:
    brwaveErrorsOverThreshold.setStatus(
        "current"
    )

brwaveErrorsUnderThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 2)
)
brwaveErrorsUnderThreshold.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"),
        ("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
)
if mibBuilder.loadTexts:
    brwaveErrorsUnderThreshold.setStatus(
        "current"
    )

brwaveUnitTemperatureAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 3)
)
brwaveUnitTemperatureAbnormal.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature")
)
if mibBuilder.loadTexts:
    brwaveUnitTemperatureAbnormal.setStatus(
        "current"
    )

brwaveUnitTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 4)
)
brwaveUnitTemperatureNormal.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature")
)
if mibBuilder.loadTexts:
    brwaveUnitTemperatureNormal.setStatus(
        "current"
    )

brwaveTxTemperatureAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 5)
)
brwaveTxTemperatureAbnormal.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature")
)
if mibBuilder.loadTexts:
    brwaveTxTemperatureAbnormal.setStatus(
        "current"
    )

brwaveTxTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 6)
)
brwaveTxTemperatureNormal.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature")
)
if mibBuilder.loadTexts:
    brwaveTxTemperatureNormal.setStatus(
        "current"
    )

brwaveInputVoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 7)
)
brwaveInputVoltageAbnormal.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioInVoltage")
)
if mibBuilder.loadTexts:
    brwaveInputVoltageAbnormal.setStatus(
        "current"
    )

brwaveInputVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 8)
)
brwaveInputVoltageNormal.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioInVoltage")
)
if mibBuilder.loadTexts:
    brwaveInputVoltageNormal.setStatus(
        "current"
    )

brwaveRslNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 10)
)
brwaveRslNormal.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioRSL")
)
if mibBuilder.loadTexts:
    brwaveRslNormal.setStatus(
        "current"
    )

brwaveRslMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 11)
)
brwaveRslMinor.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioRSL")
)
if mibBuilder.loadTexts:
    brwaveRslMinor.setStatus(
        "current"
    )

brwaveRslMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 13)
)
brwaveRslMajor.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioRSL")
)
if mibBuilder.loadTexts:
    brwaveRslMajor.setStatus(
        "current"
    )

brwaveConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 26)
)
if mibBuilder.loadTexts:
    brwaveConfigChange.setStatus(
        "current"
    )

brwaveLoginSuccessfull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 27)
)
if mibBuilder.loadTexts:
    brwaveLoginSuccessfull.setStatus(
        "current"
    )

brwaveGeToFeSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 28)
)
brwaveGeToFeSwitch.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioRSL")
)
if mibBuilder.loadTexts:
    brwaveGeToFeSwitch.setStatus(
        "current"
    )

brwaveFeToGeSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 29)
)
brwaveFeToGeSwitch.setObjects(
    ("BRWAVE-RADIO-MIB", "brwaveRadioRSL")
)
if mibBuilder.loadTexts:
    brwaveFeToGeSwitch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRWAVE-RADIO-MIB",
    **{"bridgeWave": bridgeWave,
       "brwaveReg": brwaveReg,
       "brwaveMibs": brwaveMibs,
       "brwaveRadioMibModule": brwaveRadioMibModule,
       "brwaveModules": brwaveModules,
       "brwaveRadioFE60": brwaveRadioFE60,
       "brwaveRadioGE60": brwaveRadioGE60,
       "brwaveRadioAR60": brwaveRadioAR60,
       "brwaveCommon": brwaveCommon,
       "brwaveRadioSn": brwaveRadioSn,
       "brwaveUnitModel": brwaveUnitModel,
       "brwaveBbSn": brwaveBbSn,
       "brwaveIfSn": brwaveIfSn,
       "brwaveMmwSn": brwaveMmwSn,
       "brwaveTrapCount": brwaveTrapCount,
       "brwaveProducts": brwaveProducts,
       "brwaveRadio": brwaveRadio,
       "brwaveRadioFactorySetup": brwaveRadioFactorySetup,
       "brwaveRadioTxBand": brwaveRadioTxBand,
       "brwaveRadioFactoryRate": brwaveRadioFactoryRate,
       "brwaveRadioClearStats": brwaveRadioClearStats,
       "brwaveRadioStatus": brwaveRadioStatus,
       "brwaveRadioInVoltage": brwaveRadioInVoltage,
       "brwaveRadioUnitTemperature": brwaveRadioUnitTemperature,
       "brwaveRadioTxTemperature": brwaveRadioTxTemperature,
       "brwaveRadioRSL": brwaveRadioRSL,
       "brwaveRadioRSLVoltage": brwaveRadioRSLVoltage,
       "brwaveRadioAbsRSL": brwaveRadioAbsRSL,
       "brwaveRadioRSLVoltageInt": brwaveRadioRSLVoltageInt,
       "brwaveCopperUtilization": brwaveCopperUtilization,
       "brwaveFiberUtilization": brwaveFiberUtilization,
       "brwaveRadioUtilization": brwaveRadioUtilization,
       "brwaveRadioFecError": brwaveRadioFecError,
       "brwaveRadioPreFecFlag": brwaveRadioPreFecFlag,
       "brwaveRadioPostFecFlag": brwaveRadioPostFecFlag,
       "brwaveRadioLinkRate": brwaveRadioLinkRate,
       "brwaveRadioEvents": brwaveRadioEvents,
       "brwaveRadioEventsV2": brwaveRadioEventsV2,
       "brwaveErrorsOverThreshold": brwaveErrorsOverThreshold,
       "brwaveErrorsUnderThreshold": brwaveErrorsUnderThreshold,
       "brwaveUnitTemperatureAbnormal": brwaveUnitTemperatureAbnormal,
       "brwaveUnitTemperatureNormal": brwaveUnitTemperatureNormal,
       "brwaveTxTemperatureAbnormal": brwaveTxTemperatureAbnormal,
       "brwaveTxTemperatureNormal": brwaveTxTemperatureNormal,
       "brwaveInputVoltageAbnormal": brwaveInputVoltageAbnormal,
       "brwaveInputVoltageNormal": brwaveInputVoltageNormal,
       "brwaveRslNormal": brwaveRslNormal,
       "brwaveRslMinor": brwaveRslMinor,
       "brwaveRslMajor": brwaveRslMajor,
       "brwaveConfigChange": brwaveConfigChange,
       "brwaveLoginSuccessfull": brwaveLoginSuccessfull,
       "brwaveGeToFeSwitch": brwaveGeToFeSwitch,
       "brwaveFeToGeSwitch": brwaveFeToGeSwitch,
       "brwaveRadioTrapObjs": brwaveRadioTrapObjs,
       "managerIP": managerIP,
       "userName": userName,
       "brwaveConformance": brwaveConformance,
       "brwaveRadioGroups": brwaveRadioGroups,
       "brwaveCommonGroup": brwaveCommonGroup,
       "brwaveFactoryGroup": brwaveFactoryGroup,
       "brwaveStatusGroup": brwaveStatusGroup,
       "brwaveCompliances": brwaveCompliances}
)
