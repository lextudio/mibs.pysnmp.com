# SNMP MIB module (COM21-HCXSTUPRXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXSTUPRXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:38 2024
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

(com21,
 com21Hcx,
 com21Stu,
 com21Traps) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx",
    "com21Stu",
    "com21Traps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21StuPrxy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 1)
)


# Types definitions



class FrequencyKhz(Integer32):
    """Custom type FrequencyKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800000),
    )





class UpstrmFreqKhz(Integer32):
    """Custom type UpstrmFreqKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 40000),
    )





class EpochTime(Integer32):
    """Custom type EpochTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class Offset(Integer32):
    """Custom type Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )





class AlarmSeverity(Integer32):
    """Custom type AlarmSeverity based on Integer32"""
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
        *(("clear", 1),
          ("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21StuControlGroup_ObjectIdentity = ObjectIdentity
com21StuControlGroup = _Com21StuControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2)
)
_Com21StuControlTable_Object = MibTable
com21StuControlTable = _Com21StuControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1)
)
if mibBuilder.loadTexts:
    com21StuControlTable.setStatus("current")
_Com21StuControlEntry_Object = MibTableRow
com21StuControlEntry = _Com21StuControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1)
)
com21StuControlEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuCtrlMacAddress"),
)
if mibBuilder.loadTexts:
    com21StuControlEntry.setStatus("current")
_StuCtrlMacAddress_Type = MacAddress
_StuCtrlMacAddress_Object = MibTableColumn
stuCtrlMacAddress = _StuCtrlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 1),
    _StuCtrlMacAddress_Type()
)
stuCtrlMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCtrlMacAddress.setStatus("current")


class _StuUserText_Type(DisplayString):
    """Custom type stuUserText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_StuUserText_Type.__name__ = "DisplayString"
_StuUserText_Object = MibTableColumn
stuUserText = _StuUserText_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 2),
    _StuUserText_Type()
)
stuUserText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuUserText.setStatus("current")


class _StuSerialNumber_Type(DisplayString):
    """Custom type stuSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_StuSerialNumber_Type.__name__ = "DisplayString"
_StuSerialNumber_Object = MibTableColumn
stuSerialNumber = _StuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 3),
    _StuSerialNumber_Type()
)
stuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuSerialNumber.setStatus("current")


class _StuBoardRevision_Type(DisplayString):
    """Custom type stuBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_StuBoardRevision_Type.__name__ = "DisplayString"
_StuBoardRevision_Object = MibTableColumn
stuBoardRevision = _StuBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 4),
    _StuBoardRevision_Type()
)
stuBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuBoardRevision.setStatus("current")


class _StuUnitRevision_Type(DisplayString):
    """Custom type stuUnitRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_StuUnitRevision_Type.__name__ = "DisplayString"
_StuUnitRevision_Object = MibTableColumn
stuUnitRevision = _StuUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 5),
    _StuUnitRevision_Type()
)
stuUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuUnitRevision.setStatus("current")


class _StuTunerRevision_Type(DisplayString):
    """Custom type stuTunerRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_StuTunerRevision_Type.__name__ = "DisplayString"
_StuTunerRevision_Object = MibTableColumn
stuTunerRevision = _StuTunerRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 6),
    _StuTunerRevision_Type()
)
stuTunerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuTunerRevision.setStatus("current")


class _StuModelName_Type(DisplayString):
    """Custom type stuModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_StuModelName_Type.__name__ = "DisplayString"
_StuModelName_Object = MibTableColumn
stuModelName = _StuModelName_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 7),
    _StuModelName_Type()
)
stuModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuModelName.setStatus("current")


class _StuUnitManufacturer_Type(DisplayString):
    """Custom type stuUnitManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_StuUnitManufacturer_Type.__name__ = "DisplayString"
_StuUnitManufacturer_Object = MibTableColumn
stuUnitManufacturer = _StuUnitManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 8),
    _StuUnitManufacturer_Type()
)
stuUnitManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuUnitManufacturer.setStatus("current")


class _StuDesKeySize_Type(Integer32):
    """Custom type stuDesKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bit40key", 2),
          ("bit56key", 1))
    )


_StuDesKeySize_Type.__name__ = "Integer32"
_StuDesKeySize_Object = MibTableColumn
stuDesKeySize = _StuDesKeySize_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 9),
    _StuDesKeySize_Type()
)
stuDesKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuDesKeySize.setStatus("current")


class _StuMibRevision_Type(DisplayString):
    """Custom type stuMibRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_StuMibRevision_Type.__name__ = "DisplayString"
_StuMibRevision_Object = MibTableColumn
stuMibRevision = _StuMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 10),
    _StuMibRevision_Type()
)
stuMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuMibRevision.setStatus("current")
_StuEpochTime_Type = EpochTime
_StuEpochTime_Object = MibTableColumn
stuEpochTime = _StuEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 11),
    _StuEpochTime_Type()
)
stuEpochTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEpochTime.setStatus("current")


class _StuRestartAction_Type(Integer32):
    """Custom type stuRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("restart", 2))
    )


_StuRestartAction_Type.__name__ = "Integer32"
_StuRestartAction_Object = MibTableColumn
stuRestartAction = _StuRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 12),
    _StuRestartAction_Type()
)
stuRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuRestartAction.setStatus("current")


class _StuPrevTestResult_Type(Integer32):
    """Custom type stuPrevTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_StuPrevTestResult_Type.__name__ = "Integer32"
_StuPrevTestResult_Object = MibTableColumn
stuPrevTestResult = _StuPrevTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 13),
    _StuPrevTestResult_Type()
)
stuPrevTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevTestResult.setStatus("current")


class _StuPrevTestFailCode_Type(Integer32):
    """Custom type stuPrevTestFailCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, -1),
    )


_StuPrevTestFailCode_Type.__name__ = "Integer32"
_StuPrevTestFailCode_Object = MibTableColumn
stuPrevTestFailCode = _StuPrevTestFailCode_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 14),
    _StuPrevTestFailCode_Type()
)
stuPrevTestFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevTestFailCode.setStatus("current")


class _StuOperationState_Type(Integer32):
    """Custom type stuOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("deauthorized", 2),
          ("downloading", 6),
          ("etherLoopback", 5),
          ("failedRanging", 7),
          ("offline", 3),
          ("operational", 1),
          ("upstreamTest", 4))
    )


_StuOperationState_Type.__name__ = "Integer32"
_StuOperationState_Object = MibTableColumn
stuOperationState = _StuOperationState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 15),
    _StuOperationState_Type()
)
stuOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuOperationState.setStatus("current")


class _StuAimModuleId_Type(Integer32):
    """Custom type stuAimModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm", 7),
          ("debugModule", 2),
          ("none", 1),
          ("teleReturn", 3),
          ("telephony1", 4),
          ("telephony2", 5),
          ("wirelessEthernet", 6))
    )


_StuAimModuleId_Type.__name__ = "Integer32"
_StuAimModuleId_Object = MibTableColumn
stuAimModuleId = _StuAimModuleId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 16),
    _StuAimModuleId_Type()
)
stuAimModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAimModuleId.setStatus("current")
_StuUpstrmTestFreq_Type = UpstrmFreqKhz
_StuUpstrmTestFreq_Object = MibTableColumn
stuUpstrmTestFreq = _StuUpstrmTestFreq_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 17),
    _StuUpstrmTestFreq_Type()
)
stuUpstrmTestFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuUpstrmTestFreq.setStatus("current")


class _StuInbPresent_Type(Integer32):
    """Custom type stuInbPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbInstalled", 1),
          ("inbReady", 3),
          ("noInbSupport", 2))
    )


_StuInbPresent_Type.__name__ = "Integer32"
_StuInbPresent_Object = MibTableColumn
stuInbPresent = _StuInbPresent_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 19),
    _StuInbPresent_Type()
)
stuInbPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuInbPresent.setStatus("current")


class _StuInbContToneEnable_Type(Integer32):
    """Custom type stuInbContToneEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuInbContToneEnable_Type.__name__ = "Integer32"
_StuInbContToneEnable_Object = MibTableColumn
stuInbContToneEnable = _StuInbContToneEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 20),
    _StuInbContToneEnable_Type()
)
stuInbContToneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuInbContToneEnable.setStatus("current")


class _StuLastRestartCause_Type(Integer32):
    """Custom type stuLastRestartCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fault", 6),
          ("hcxDirected", 2),
          ("imageRefresh", 4),
          ("lof", 5),
          ("pingFail", 3),
          ("unknown", 1))
    )


_StuLastRestartCause_Type.__name__ = "Integer32"
_StuLastRestartCause_Object = MibTableColumn
stuLastRestartCause = _StuLastRestartCause_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 21),
    _StuLastRestartCause_Type()
)
stuLastRestartCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuLastRestartCause.setStatus("current")


class _StuUpstrmPingCntrl_Type(Integer32):
    """Custom type stuUpstrmPingCntrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuUpstrmPingCntrl_Type.__name__ = "Integer32"
_StuUpstrmPingCntrl_Object = MibTableColumn
stuUpstrmPingCntrl = _StuUpstrmPingCntrl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 22),
    _StuUpstrmPingCntrl_Type()
)
stuUpstrmPingCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuUpstrmPingCntrl.setStatus("current")


class _StuUpstrmTestTimeout_Type(Integer32):
    """Custom type stuUpstrmTestTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_StuUpstrmTestTimeout_Type.__name__ = "Integer32"
_StuUpstrmTestTimeout_Object = MibTableColumn
stuUpstrmTestTimeout = _StuUpstrmTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 23),
    _StuUpstrmTestTimeout_Type()
)
stuUpstrmTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuUpstrmTestTimeout.setStatus("current")
_StuDnstrmAltFreq_Type = FrequencyKhz
_StuDnstrmAltFreq_Object = MibTableColumn
stuDnstrmAltFreq = _StuDnstrmAltFreq_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 24),
    _StuDnstrmAltFreq_Type()
)
stuDnstrmAltFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuDnstrmAltFreq.setStatus("current")


class _StuAsicRevision_Type(Integer32):
    """Custom type stuAsicRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StuAsicRevision_Type.__name__ = "Integer32"
_StuAsicRevision_Object = MibTableColumn
stuAsicRevision = _StuAsicRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 25),
    _StuAsicRevision_Type()
)
stuAsicRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAsicRevision.setStatus("current")


class _StuVoiceAimLpBk_Type(Integer32):
    """Custom type stuVoiceAimLpBk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("stuLpBk", 2))
    )


_StuVoiceAimLpBk_Type.__name__ = "Integer32"
_StuVoiceAimLpBk_Object = MibTableColumn
stuVoiceAimLpBk = _StuVoiceAimLpBk_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 26),
    _StuVoiceAimLpBk_Type()
)
stuVoiceAimLpBk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuVoiceAimLpBk.setStatus("current")


class _StuVoiceAimPort1Status_Type(Integer32):
    """Custom type stuVoiceAimPort1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1))
    )


_StuVoiceAimPort1Status_Type.__name__ = "Integer32"
_StuVoiceAimPort1Status_Object = MibTableColumn
stuVoiceAimPort1Status = _StuVoiceAimPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 27),
    _StuVoiceAimPort1Status_Type()
)
stuVoiceAimPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceAimPort1Status.setStatus("current")


class _StuVoiceAimPort2Status_Type(Integer32):
    """Custom type stuVoiceAimPort2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1))
    )


_StuVoiceAimPort2Status_Type.__name__ = "Integer32"
_StuVoiceAimPort2Status_Object = MibTableColumn
stuVoiceAimPort2Status = _StuVoiceAimPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 2, 1, 1, 28),
    _StuVoiceAimPort2Status_Type()
)
stuVoiceAimPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceAimPort2Status.setStatus("current")
_Com21StuPhysicalGroup_ObjectIdentity = ObjectIdentity
com21StuPhysicalGroup = _Com21StuPhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3)
)
_Com21StuPhysicalTable_Object = MibTable
com21StuPhysicalTable = _Com21StuPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1)
)
if mibBuilder.loadTexts:
    com21StuPhysicalTable.setStatus("current")
_Com21StuPhysicalEntry_Object = MibTableRow
com21StuPhysicalEntry = _Com21StuPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1)
)
com21StuPhysicalEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuPhyMacAddress"),
)
if mibBuilder.loadTexts:
    com21StuPhysicalEntry.setStatus("current")
_StuPhyMacAddress_Type = MacAddress
_StuPhyMacAddress_Object = MibTableColumn
stuPhyMacAddress = _StuPhyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 1),
    _StuPhyMacAddress_Type()
)
stuPhyMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPhyMacAddress.setStatus("current")
_StuXmitFrequency_Type = UpstrmFreqKhz
_StuXmitFrequency_Object = MibTableColumn
stuXmitFrequency = _StuXmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 2),
    _StuXmitFrequency_Type()
)
stuXmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuXmitFrequency.setStatus("current")
_StuRecvFrequency_Type = FrequencyKhz
_StuRecvFrequency_Object = MibTableColumn
stuRecvFrequency = _StuRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 3),
    _StuRecvFrequency_Type()
)
stuRecvFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuRecvFrequency.setStatus("current")
_StuRecvRfSrEstimate_Type = Integer32
_StuRecvRfSrEstimate_Object = MibTableColumn
stuRecvRfSrEstimate = _StuRecvRfSrEstimate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 4),
    _StuRecvRfSrEstimate_Type()
)
stuRecvRfSrEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuRecvRfSrEstimate.setStatus("current")
_StuRecvRfSigLevel_Type = Integer32
_StuRecvRfSigLevel_Object = MibTableColumn
stuRecvRfSigLevel = _StuRecvRfSigLevel_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 5),
    _StuRecvRfSigLevel_Type()
)
stuRecvRfSigLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuRecvRfSigLevel.setStatus("current")
_StuXmitOffset_Type = Offset
_StuXmitOffset_Object = MibTableColumn
stuXmitOffset = _StuXmitOffset_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 6),
    _StuXmitOffset_Type()
)
stuXmitOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuXmitOffset.setStatus("current")


class _StuXmitDacVRef_Type(Integer32):
    """Custom type stuXmitDacVRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StuXmitDacVRef_Type.__name__ = "Integer32"
_StuXmitDacVRef_Object = MibTableColumn
stuXmitDacVRef = _StuXmitDacVRef_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 7),
    _StuXmitDacVRef_Type()
)
stuXmitDacVRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuXmitDacVRef.setStatus("current")


class _StuRecvFreqDrift_Type(Integer32):
    """Custom type stuRecvFreqDrift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 250),
    )


_StuRecvFreqDrift_Type.__name__ = "Integer32"
_StuRecvFreqDrift_Object = MibTableColumn
stuRecvFreqDrift = _StuRecvFreqDrift_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 3, 1, 1, 8),
    _StuRecvFreqDrift_Type()
)
stuRecvFreqDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuRecvFreqDrift.setStatus("current")
_Com21StuAlarmGroup_ObjectIdentity = ObjectIdentity
com21StuAlarmGroup = _Com21StuAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 4)
)
_Com21StuAlarmTable_Object = MibTable
com21StuAlarmTable = _Com21StuAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 4, 1)
)
if mibBuilder.loadTexts:
    com21StuAlarmTable.setStatus("current")
_Com21StuAlarmEntry_Object = MibTableRow
com21StuAlarmEntry = _Com21StuAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 4, 1, 1)
)
com21StuAlarmEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuAlmMacAddress"),
    (0, "COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
)
if mibBuilder.loadTexts:
    com21StuAlarmEntry.setStatus("current")
_StuAlmMacAddress_Type = MacAddress
_StuAlmMacAddress_Object = MibTableColumn
stuAlmMacAddress = _StuAlmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 4, 1, 1, 1),
    _StuAlmMacAddress_Type()
)
stuAlmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAlmMacAddress.setStatus("current")
_StuAlmTime_Type = EpochTime
_StuAlmTime_Object = MibTableColumn
stuAlmTime = _StuAlmTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 4, 1, 1, 2),
    _StuAlmTime_Type()
)
stuAlmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAlmTime.setStatus("current")


class _StuAlmTrapId_Type(Integer32):
    """Custom type stuAlmTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_StuAlmTrapId_Type.__name__ = "Integer32"
_StuAlmTrapId_Object = MibTableColumn
stuAlmTrapId = _StuAlmTrapId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 4, 1, 1, 3),
    _StuAlmTrapId_Type()
)
stuAlmTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAlmTrapId.setStatus("current")
_StuAlmSeverity_Type = AlarmSeverity
_StuAlmSeverity_Object = MibTableColumn
stuAlmSeverity = _StuAlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 4, 1, 1, 4),
    _StuAlmSeverity_Type()
)
stuAlmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAlmSeverity.setStatus("current")
_Com21StuEtherConfigGroup_ObjectIdentity = ObjectIdentity
com21StuEtherConfigGroup = _Com21StuEtherConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5)
)
_Com21StuEtherConfigTable_Object = MibTable
com21StuEtherConfigTable = _Com21StuEtherConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1)
)
if mibBuilder.loadTexts:
    com21StuEtherConfigTable.setStatus("current")
_Com21StuEtherConfigEntry_Object = MibTableRow
com21StuEtherConfigEntry = _Com21StuEtherConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1)
)
com21StuEtherConfigEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuEthMacAddress"),
)
if mibBuilder.loadTexts:
    com21StuEtherConfigEntry.setStatus("current")
_StuEthMacAddress_Type = MacAddress
_StuEthMacAddress_Object = MibTableColumn
stuEthMacAddress = _StuEthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 1),
    _StuEthMacAddress_Type()
)
stuEthMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuEthMacAddress.setStatus("current")


class _StuEtherFiltFlushAction_Type(Integer32):
    """Custom type stuEtherFiltFlushAction based on Integer32"""
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
        *(("flushEtherType", 3),
          ("flushIp", 4),
          ("flushMac", 2),
          ("none", 1))
    )


_StuEtherFiltFlushAction_Type.__name__ = "Integer32"
_StuEtherFiltFlushAction_Object = MibTableColumn
stuEtherFiltFlushAction = _StuEtherFiltFlushAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 2),
    _StuEtherFiltFlushAction_Type()
)
stuEtherFiltFlushAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherFiltFlushAction.setStatus("current")


class _StuEtherForwArpOnly_Type(Integer32):
    """Custom type stuEtherForwArpOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherForwArpOnly_Type.__name__ = "Integer32"
_StuEtherForwArpOnly_Object = MibTableColumn
stuEtherForwArpOnly = _StuEtherForwArpOnly_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 3),
    _StuEtherForwArpOnly_Type()
)
stuEtherForwArpOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherForwArpOnly.setStatus("current")


class _StuEtherMacFiltAge_Type(Integer32):
    """Custom type stuEtherMacFiltAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_StuEtherMacFiltAge_Type.__name__ = "Integer32"
_StuEtherMacFiltAge_Object = MibTableColumn
stuEtherMacFiltAge = _StuEtherMacFiltAge_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 4),
    _StuEtherMacFiltAge_Type()
)
stuEtherMacFiltAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherMacFiltAge.setStatus("current")


class _StuEtherBCastRateEn_Type(Integer32):
    """Custom type stuEtherBCastRateEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherBCastRateEn_Type.__name__ = "Integer32"
_StuEtherBCastRateEn_Object = MibTableColumn
stuEtherBCastRateEn = _StuEtherBCastRateEn_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 5),
    _StuEtherBCastRateEn_Type()
)
stuEtherBCastRateEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherBCastRateEn.setStatus("current")


class _StuEtherBCastRateCo_Type(Integer32):
    """Custom type stuEtherBCastRateCo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StuEtherBCastRateCo_Type.__name__ = "Integer32"
_StuEtherBCastRateCo_Object = MibTableColumn
stuEtherBCastRateCo = _StuEtherBCastRateCo_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 6),
    _StuEtherBCastRateCo_Type()
)
stuEtherBCastRateCo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherBCastRateCo.setStatus("current")


class _StuEtherStickyBitCtrl_Type(Integer32):
    """Custom type stuEtherStickyBitCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherStickyBitCtrl_Type.__name__ = "Integer32"
_StuEtherStickyBitCtrl_Object = MibTableColumn
stuEtherStickyBitCtrl = _StuEtherStickyBitCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 7),
    _StuEtherStickyBitCtrl_Type()
)
stuEtherStickyBitCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherStickyBitCtrl.setStatus("current")


class _StuEther8021QEnable_Type(Integer32):
    """Custom type stuEther8021QEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEther8021QEnable_Type.__name__ = "Integer32"
_StuEther8021QEnable_Object = MibTableColumn
stuEther8021QEnable = _StuEther8021QEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 8),
    _StuEther8021QEnable_Type()
)
stuEther8021QEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEther8021QEnable.setStatus("current")


class _StuEtherNonSnapRej_Type(Integer32):
    """Custom type stuEtherNonSnapRej based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherNonSnapRej_Type.__name__ = "Integer32"
_StuEtherNonSnapRej_Object = MibTableColumn
stuEtherNonSnapRej = _StuEtherNonSnapRej_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 9),
    _StuEtherNonSnapRej_Type()
)
stuEtherNonSnapRej.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherNonSnapRej.setStatus("current")


class _StuEtherIgmpEnable_Type(Integer32):
    """Custom type stuEtherIgmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherIgmpEnable_Type.__name__ = "Integer32"
_StuEtherIgmpEnable_Object = MibTableColumn
stuEtherIgmpEnable = _StuEtherIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 10),
    _StuEtherIgmpEnable_Type()
)
stuEtherIgmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherIgmpEnable.setStatus("current")


class _StuEtherNonIpMultiEn_Type(Integer32):
    """Custom type stuEtherNonIpMultiEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherNonIpMultiEn_Type.__name__ = "Integer32"
_StuEtherNonIpMultiEn_Object = MibTableColumn
stuEtherNonIpMultiEn = _StuEtherNonIpMultiEn_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 11),
    _StuEtherNonIpMultiEn_Type()
)
stuEtherNonIpMultiEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherNonIpMultiEn.setStatus("current")


class _StuEtherBcmpOnly_Type(Integer32):
    """Custom type stuEtherBcmpOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherBcmpOnly_Type.__name__ = "Integer32"
_StuEtherBcmpOnly_Object = MibTableColumn
stuEtherBcmpOnly = _StuEtherBcmpOnly_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 12),
    _StuEtherBcmpOnly_Type()
)
stuEtherBcmpOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherBcmpOnly.setStatus("current")


class _StuEtherIgmpSnoopEnable_Type(Integer32):
    """Custom type stuEtherIgmpSnoopEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_StuEtherIgmpSnoopEnable_Type.__name__ = "Integer32"
_StuEtherIgmpSnoopEnable_Object = MibTableColumn
stuEtherIgmpSnoopEnable = _StuEtherIgmpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 5, 1, 1, 13),
    _StuEtherIgmpSnoopEnable_Type()
)
stuEtherIgmpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherIgmpSnoopEnable.setStatus("current")
_Com21StuEtherTypeGroup_ObjectIdentity = ObjectIdentity
com21StuEtherTypeGroup = _Com21StuEtherTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 6)
)
_Com21StuEtherTypeTable_Object = MibTable
com21StuEtherTypeTable = _Com21StuEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 6, 1)
)
if mibBuilder.loadTexts:
    com21StuEtherTypeTable.setStatus("current")
_Com21StuFiltEthTypeEntry_Object = MibTableRow
com21StuFiltEthTypeEntry = _Com21StuFiltEthTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 6, 1, 1)
)
com21StuFiltEthTypeEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuFiltEtherMacAddr"),
    (0, "COM21-HCXSTUPRXY-MIB", "stuFiltEtherType"),
)
if mibBuilder.loadTexts:
    com21StuFiltEthTypeEntry.setStatus("current")
_StuFiltEtherMacAddr_Type = MacAddress
_StuFiltEtherMacAddr_Object = MibTableColumn
stuFiltEtherMacAddr = _StuFiltEtherMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 6, 1, 1, 1),
    _StuFiltEtherMacAddr_Type()
)
stuFiltEtherMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuFiltEtherMacAddr.setStatus("current")


class _StuFiltEtherType_Type(Integer32):
    """Custom type stuFiltEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StuFiltEtherType_Type.__name__ = "Integer32"
_StuFiltEtherType_Object = MibTableColumn
stuFiltEtherType = _StuFiltEtherType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 6, 1, 1, 2),
    _StuFiltEtherType_Type()
)
stuFiltEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuFiltEtherType.setStatus("current")
_StuFiltEtherStatus_Type = Com21RowStatus
_StuFiltEtherStatus_Object = MibTableColumn
stuFiltEtherStatus = _StuFiltEtherStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 6, 1, 1, 3),
    _StuFiltEtherStatus_Type()
)
stuFiltEtherStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stuFiltEtherStatus.setStatus("current")
_Com21StuFiltIpMultiGroup_ObjectIdentity = ObjectIdentity
com21StuFiltIpMultiGroup = _Com21StuFiltIpMultiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 7)
)
_Com21StuFiltIpMultiTable_Object = MibTable
com21StuFiltIpMultiTable = _Com21StuFiltIpMultiTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 7, 1)
)
if mibBuilder.loadTexts:
    com21StuFiltIpMultiTable.setStatus("current")
_Com21StuFiltIpMultiEntry_Object = MibTableRow
com21StuFiltIpMultiEntry = _Com21StuFiltIpMultiEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 7, 1, 1)
)
com21StuFiltIpMultiEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuFiltIpMacAddr"),
    (0, "COM21-HCXSTUPRXY-MIB", "stuFiltIpMultiAddr"),
)
if mibBuilder.loadTexts:
    com21StuFiltIpMultiEntry.setStatus("current")
_StuFiltIpMacAddr_Type = MacAddress
_StuFiltIpMacAddr_Object = MibTableColumn
stuFiltIpMacAddr = _StuFiltIpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 7, 1, 1, 1),
    _StuFiltIpMacAddr_Type()
)
stuFiltIpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuFiltIpMacAddr.setStatus("current")
_StuFiltIpMultiAddr_Type = MacAddress
_StuFiltIpMultiAddr_Object = MibTableColumn
stuFiltIpMultiAddr = _StuFiltIpMultiAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 7, 1, 1, 2),
    _StuFiltIpMultiAddr_Type()
)
stuFiltIpMultiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuFiltIpMultiAddr.setStatus("current")
_StuFiltIpMultiStatus_Type = Com21RowStatus
_StuFiltIpMultiStatus_Object = MibTableColumn
stuFiltIpMultiStatus = _StuFiltIpMultiStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 7, 1, 1, 3),
    _StuFiltIpMultiStatus_Type()
)
stuFiltIpMultiStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stuFiltIpMultiStatus.setStatus("current")


class _StuFiltIpDirectCntrl_Type(Integer32):
    """Custom type stuFiltIpDirectCntrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bothDirections", 3),
          ("downstreamOnly", 2),
          ("upstreamOnly", 1))
    )


_StuFiltIpDirectCntrl_Type.__name__ = "Integer32"
_StuFiltIpDirectCntrl_Object = MibTableColumn
stuFiltIpDirectCntrl = _StuFiltIpDirectCntrl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 7, 1, 1, 4),
    _StuFiltIpDirectCntrl_Type()
)
stuFiltIpDirectCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuFiltIpDirectCntrl.setStatus("current")
_Com21StuEtherMacGroup_ObjectIdentity = ObjectIdentity
com21StuEtherMacGroup = _Com21StuEtherMacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 8)
)
_Com21StuEtherMacTable_Object = MibTable
com21StuEtherMacTable = _Com21StuEtherMacTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 8, 1)
)
if mibBuilder.loadTexts:
    com21StuEtherMacTable.setStatus("current")
_Com21StuEtherMacEntry_Object = MibTableRow
com21StuEtherMacEntry = _Com21StuEtherMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 8, 1, 1)
)
com21StuEtherMacEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuEtherStuMac"),
    (0, "COM21-HCXSTUPRXY-MIB", "stuEtherMacAddr"),
)
if mibBuilder.loadTexts:
    com21StuEtherMacEntry.setStatus("current")
_StuEtherStuMac_Type = MacAddress
_StuEtherStuMac_Object = MibTableColumn
stuEtherStuMac = _StuEtherStuMac_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 8, 1, 1, 1),
    _StuEtherStuMac_Type()
)
stuEtherStuMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuEtherStuMac.setStatus("current")
_StuEtherMacAddr_Type = MacAddress
_StuEtherMacAddr_Object = MibTableColumn
stuEtherMacAddr = _StuEtherMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 8, 1, 1, 2),
    _StuEtherMacAddr_Type()
)
stuEtherMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuEtherMacAddr.setStatus("current")


class _StuEtherMacType_Type(Integer32):
    """Custom type stuEtherMacType based on Integer32"""
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
        *(("learned", 1),
          ("processor", 2),
          ("reject", 4),
          ("upstream", 3))
    )


_StuEtherMacType_Type.__name__ = "Integer32"
_StuEtherMacType_Object = MibTableColumn
stuEtherMacType = _StuEtherMacType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 8, 1, 1, 3),
    _StuEtherMacType_Type()
)
stuEtherMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherMacType.setStatus("current")
_StuEtherMacStatus_Type = Com21RowStatus
_StuEtherMacStatus_Object = MibTableColumn
stuEtherMacStatus = _StuEtherMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 8, 1, 1, 4),
    _StuEtherMacStatus_Type()
)
stuEtherMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stuEtherMacStatus.setStatus("current")
_Com21StuEtherStatsGroup_ObjectIdentity = ObjectIdentity
com21StuEtherStatsGroup = _Com21StuEtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9)
)
_Com21StuEtherStatsTable_Object = MibTable
com21StuEtherStatsTable = _Com21StuEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1)
)
if mibBuilder.loadTexts:
    com21StuEtherStatsTable.setStatus("current")
_Com21StuEtherStatsEntry_Object = MibTableRow
com21StuEtherStatsEntry = _Com21StuEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1)
)
com21StuEtherStatsEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuEthStatsMacAddr"),
)
if mibBuilder.loadTexts:
    com21StuEtherStatsEntry.setStatus("current")
_StuEthStatsMacAddr_Type = MacAddress
_StuEthStatsMacAddr_Object = MibTableColumn
stuEthStatsMacAddr = _StuEthStatsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 1),
    _StuEthStatsMacAddr_Type()
)
stuEthStatsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuEthStatsMacAddr.setStatus("current")
_StuCurrEtherRunts_Type = Gauge32
_StuCurrEtherRunts_Object = MibTableColumn
stuCurrEtherRunts = _StuCurrEtherRunts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 2),
    _StuCurrEtherRunts_Type()
)
stuCurrEtherRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCurrEtherRunts.setStatus("current")
_StuCurrEtherCollitns_Type = Gauge32
_StuCurrEtherCollitns_Object = MibTableColumn
stuCurrEtherCollitns = _StuCurrEtherCollitns_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 3),
    _StuCurrEtherCollitns_Type()
)
stuCurrEtherCollitns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCurrEtherCollitns.setStatus("current")
_StuCurrEtherFramErrs_Type = Gauge32
_StuCurrEtherFramErrs_Object = MibTableColumn
stuCurrEtherFramErrs = _StuCurrEtherFramErrs_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 4),
    _StuCurrEtherFramErrs_Type()
)
stuCurrEtherFramErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCurrEtherFramErrs.setStatus("current")
_StuCurrEtherCrcErrs_Type = Gauge32
_StuCurrEtherCrcErrs_Object = MibTableColumn
stuCurrEtherCrcErrs = _StuCurrEtherCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 5),
    _StuCurrEtherCrcErrs_Type()
)
stuCurrEtherCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCurrEtherCrcErrs.setStatus("current")
_StuCurrEtherCrcThres_Type = Integer32
_StuCurrEtherCrcThres_Object = MibTableColumn
stuCurrEtherCrcThres = _StuCurrEtherCrcThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 6),
    _StuCurrEtherCrcThres_Type()
)
stuCurrEtherCrcThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuCurrEtherCrcThres.setStatus("current")
_StuCurrEtherTxUnder_Type = Gauge32
_StuCurrEtherTxUnder_Object = MibTableColumn
stuCurrEtherTxUnder = _StuCurrEtherTxUnder_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 7),
    _StuCurrEtherTxUnder_Type()
)
stuCurrEtherTxUnder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCurrEtherTxUnder.setStatus("current")
_StuCurrEtherRxOver_Type = Gauge32
_StuCurrEtherRxOver_Object = MibTableColumn
stuCurrEtherRxOver = _StuCurrEtherRxOver_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 8),
    _StuCurrEtherRxOver_Type()
)
stuCurrEtherRxOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCurrEtherRxOver.setStatus("current")
_StuCurrEtherDropFrms_Type = Gauge32
_StuCurrEtherDropFrms_Object = MibTableColumn
stuCurrEtherDropFrms = _StuCurrEtherDropFrms_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 9),
    _StuCurrEtherDropFrms_Type()
)
stuCurrEtherDropFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCurrEtherDropFrms.setStatus("current")
_StuPrevEtherRunts_Type = Gauge32
_StuPrevEtherRunts_Object = MibTableColumn
stuPrevEtherRunts = _StuPrevEtherRunts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 10),
    _StuPrevEtherRunts_Type()
)
stuPrevEtherRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevEtherRunts.setStatus("current")
_StuPrevEtherCollitns_Type = Gauge32
_StuPrevEtherCollitns_Object = MibTableColumn
stuPrevEtherCollitns = _StuPrevEtherCollitns_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 11),
    _StuPrevEtherCollitns_Type()
)
stuPrevEtherCollitns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevEtherCollitns.setStatus("current")
_StuPrevEtherFramErrs_Type = Gauge32
_StuPrevEtherFramErrs_Object = MibTableColumn
stuPrevEtherFramErrs = _StuPrevEtherFramErrs_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 12),
    _StuPrevEtherFramErrs_Type()
)
stuPrevEtherFramErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevEtherFramErrs.setStatus("current")
_StuPrevEtherCrcErrs_Type = Gauge32
_StuPrevEtherCrcErrs_Object = MibTableColumn
stuPrevEtherCrcErrs = _StuPrevEtherCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 13),
    _StuPrevEtherCrcErrs_Type()
)
stuPrevEtherCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevEtherCrcErrs.setStatus("current")
_StuPrevEtherTxUnder_Type = Gauge32
_StuPrevEtherTxUnder_Object = MibTableColumn
stuPrevEtherTxUnder = _StuPrevEtherTxUnder_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 14),
    _StuPrevEtherTxUnder_Type()
)
stuPrevEtherTxUnder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevEtherTxUnder.setStatus("current")
_StuPrevEtherRxOver_Type = Gauge32
_StuPrevEtherRxOver_Object = MibTableColumn
stuPrevEtherRxOver = _StuPrevEtherRxOver_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 15),
    _StuPrevEtherRxOver_Type()
)
stuPrevEtherRxOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevEtherRxOver.setStatus("current")
_StuPrevEtherDropFrms_Type = Gauge32
_StuPrevEtherDropFrms_Object = MibTableColumn
stuPrevEtherDropFrms = _StuPrevEtherDropFrms_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 16),
    _StuPrevEtherDropFrms_Type()
)
stuPrevEtherDropFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuPrevEtherDropFrms.setStatus("current")


class _StuEtherConnState_Type(Integer32):
    """Custom type stuEtherConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 2),
          ("oos", 3),
          ("unint", 1))
    )


_StuEtherConnState_Type.__name__ = "Integer32"
_StuEtherConnState_Object = MibTableColumn
stuEtherConnState = _StuEtherConnState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 17),
    _StuEtherConnState_Type()
)
stuEtherConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuEtherConnState.setStatus("current")


class _StuEtherClearStats_Type(Integer32):
    """Custom type stuEtherClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_StuEtherClearStats_Type.__name__ = "Integer32"
_StuEtherClearStats_Object = MibTableColumn
stuEtherClearStats = _StuEtherClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 9, 1, 1, 18),
    _StuEtherClearStats_Type()
)
stuEtherClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuEtherClearStats.setStatus("current")
_Com21StuStatsGroup_ObjectIdentity = ObjectIdentity
com21StuStatsGroup = _Com21StuStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10)
)
_Com21StuStatsTable_Object = MibTable
com21StuStatsTable = _Com21StuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1)
)
if mibBuilder.loadTexts:
    com21StuStatsTable.setStatus("current")
_Com21StuStatsEntry_Object = MibTableRow
com21StuStatsEntry = _Com21StuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1)
)
com21StuStatsEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuStatsMacAddress"),
)
if mibBuilder.loadTexts:
    com21StuStatsEntry.setStatus("current")
_StuStatsMacAddress_Type = MacAddress
_StuStatsMacAddress_Object = MibTableColumn
stuStatsMacAddress = _StuStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 1),
    _StuStatsMacAddress_Type()
)
stuStatsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsMacAddress.setStatus("current")
_StuStatsCurrAtmTei_Type = Gauge32
_StuStatsCurrAtmTei_Object = MibTableColumn
stuStatsCurrAtmTei = _StuStatsCurrAtmTei_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 2),
    _StuStatsCurrAtmTei_Type()
)
stuStatsCurrAtmTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsCurrAtmTei.setStatus("current")
_StuAtmTeiThreshold_Type = Integer32
_StuAtmTeiThreshold_Object = MibTableColumn
stuAtmTeiThreshold = _StuAtmTeiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 3),
    _StuAtmTeiThreshold_Type()
)
stuAtmTeiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAtmTeiThreshold.setStatus("current")
_StuStatsCurrAtmHec_Type = Gauge32
_StuStatsCurrAtmHec_Object = MibTableColumn
stuStatsCurrAtmHec = _StuStatsCurrAtmHec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 4),
    _StuStatsCurrAtmHec_Type()
)
stuStatsCurrAtmHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsCurrAtmHec.setStatus("current")
_StuAtmHecThreshold_Type = Integer32
_StuAtmHecThreshold_Object = MibTableColumn
stuAtmHecThreshold = _StuAtmHecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 5),
    _StuAtmHecThreshold_Type()
)
stuAtmHecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAtmHecThreshold.setStatus("current")
_StuStatsCurrESMin_Type = Gauge32
_StuStatsCurrESMin_Object = MibTableColumn
stuStatsCurrESMin = _StuStatsCurrESMin_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 6),
    _StuStatsCurrESMin_Type()
)
stuStatsCurrESMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsCurrESMin.setStatus("current")
_StuESMinThreshold_Type = Integer32
_StuESMinThreshold_Object = MibTableColumn
stuESMinThreshold = _StuESMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 7),
    _StuESMinThreshold_Type()
)
stuESMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuESMinThreshold.setStatus("current")
_StuStatsCurrFecCorrect_Type = Gauge32
_StuStatsCurrFecCorrect_Object = MibTableColumn
stuStatsCurrFecCorrect = _StuStatsCurrFecCorrect_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 8),
    _StuStatsCurrFecCorrect_Type()
)
stuStatsCurrFecCorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsCurrFecCorrect.setStatus("current")
_StuFecCorrectThreshold_Type = Integer32
_StuFecCorrectThreshold_Object = MibTableColumn
stuFecCorrectThreshold = _StuFecCorrectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 9),
    _StuFecCorrectThreshold_Type()
)
stuFecCorrectThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuFecCorrectThreshold.setStatus("current")
_StuStatsCurrUASMin_Type = Gauge32
_StuStatsCurrUASMin_Object = MibTableColumn
stuStatsCurrUASMin = _StuStatsCurrUASMin_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 10),
    _StuStatsCurrUASMin_Type()
)
stuStatsCurrUASMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsCurrUASMin.setStatus("current")
_StuStatsPrevAtmTei_Type = Gauge32
_StuStatsPrevAtmTei_Object = MibTableColumn
stuStatsPrevAtmTei = _StuStatsPrevAtmTei_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 11),
    _StuStatsPrevAtmTei_Type()
)
stuStatsPrevAtmTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsPrevAtmTei.setStatus("current")
_StuStatsPrevAtmHec_Type = Gauge32
_StuStatsPrevAtmHec_Object = MibTableColumn
stuStatsPrevAtmHec = _StuStatsPrevAtmHec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 12),
    _StuStatsPrevAtmHec_Type()
)
stuStatsPrevAtmHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsPrevAtmHec.setStatus("current")
_StuStatsPrevESMin_Type = Gauge32
_StuStatsPrevESMin_Object = MibTableColumn
stuStatsPrevESMin = _StuStatsPrevESMin_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 13),
    _StuStatsPrevESMin_Type()
)
stuStatsPrevESMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsPrevESMin.setStatus("current")
_StuStatsPrevFecCorrect_Type = Gauge32
_StuStatsPrevFecCorrect_Object = MibTableColumn
stuStatsPrevFecCorrect = _StuStatsPrevFecCorrect_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 14),
    _StuStatsPrevFecCorrect_Type()
)
stuStatsPrevFecCorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsPrevFecCorrect.setStatus("current")
_StuStatsPrevUASMin_Type = Gauge32
_StuStatsPrevUASMin_Object = MibTableColumn
stuStatsPrevUASMin = _StuStatsPrevUASMin_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 15),
    _StuStatsPrevUASMin_Type()
)
stuStatsPrevUASMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuStatsPrevUASMin.setStatus("current")


class _StuStatsClearStats_Type(Integer32):
    """Custom type stuStatsClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_StuStatsClearStats_Type.__name__ = "Integer32"
_StuStatsClearStats_Object = MibTableColumn
stuStatsClearStats = _StuStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 10, 1, 1, 16),
    _StuStatsClearStats_Type()
)
stuStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuStatsClearStats.setStatus("current")
_Com21StuQStatsGroup_ObjectIdentity = ObjectIdentity
com21StuQStatsGroup = _Com21StuQStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11)
)
_Com21StuQStatsTable_Object = MibTable
com21StuQStatsTable = _Com21StuQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1)
)
if mibBuilder.loadTexts:
    com21StuQStatsTable.setStatus("current")
_Com21StuQStatsEntry_Object = MibTableRow
com21StuQStatsEntry = _Com21StuQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1)
)
com21StuQStatsEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuAtmStuMacAddr"),
    (0, "COM21-HCXSTUPRXY-MIB", "stuAtmStuQNo"),
)
if mibBuilder.loadTexts:
    com21StuQStatsEntry.setStatus("current")
_StuAtmStuMacAddr_Type = MacAddress
_StuAtmStuMacAddr_Object = MibTableColumn
stuAtmStuMacAddr = _StuAtmStuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 1),
    _StuAtmStuMacAddr_Type()
)
stuAtmStuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStuMacAddr.setStatus("current")
_StuAtmStuQNo_Type = Integer32
_StuAtmStuQNo_Object = MibTableColumn
stuAtmStuQNo = _StuAtmStuQNo_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 2),
    _StuAtmStuQNo_Type()
)
stuAtmStuQNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStuQNo.setStatus("current")
_StuAtmStatsCurrMinRx_Type = Gauge32
_StuAtmStatsCurrMinRx_Object = MibTableColumn
stuAtmStatsCurrMinRx = _StuAtmStatsCurrMinRx_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 3),
    _StuAtmStatsCurrMinRx_Type()
)
stuAtmStatsCurrMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStatsCurrMinRx.setStatus("current")
_StuAtmStatsCurrMinRxDropped_Type = Gauge32
_StuAtmStatsCurrMinRxDropped_Object = MibTableColumn
stuAtmStatsCurrMinRxDropped = _StuAtmStatsCurrMinRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 4),
    _StuAtmStatsCurrMinRxDropped_Type()
)
stuAtmStatsCurrMinRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStatsCurrMinRxDropped.setStatus("current")
_StuAtmStatsCurrMinCRCErrors_Type = Gauge32
_StuAtmStatsCurrMinCRCErrors_Object = MibTableColumn
stuAtmStatsCurrMinCRCErrors = _StuAtmStatsCurrMinCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 5),
    _StuAtmStatsCurrMinCRCErrors_Type()
)
stuAtmStatsCurrMinCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStatsCurrMinCRCErrors.setStatus("current")
_StuAtmStatsPrevMinRx_Type = Gauge32
_StuAtmStatsPrevMinRx_Object = MibTableColumn
stuAtmStatsPrevMinRx = _StuAtmStatsPrevMinRx_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 6),
    _StuAtmStatsPrevMinRx_Type()
)
stuAtmStatsPrevMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStatsPrevMinRx.setStatus("current")
_StuAtmStatsPrevMinRxDropped_Type = Gauge32
_StuAtmStatsPrevMinRxDropped_Object = MibTableColumn
stuAtmStatsPrevMinRxDropped = _StuAtmStatsPrevMinRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 7),
    _StuAtmStatsPrevMinRxDropped_Type()
)
stuAtmStatsPrevMinRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStatsPrevMinRxDropped.setStatus("current")
_StuAtmStatsPrevMinCRCErrors_Type = Gauge32
_StuAtmStatsPrevMinCRCErrors_Object = MibTableColumn
stuAtmStatsPrevMinCRCErrors = _StuAtmStatsPrevMinCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 8),
    _StuAtmStatsPrevMinCRCErrors_Type()
)
stuAtmStatsPrevMinCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAtmStatsPrevMinCRCErrors.setStatus("current")


class _StuAtmStatsClearStats_Type(Integer32):
    """Custom type stuAtmStatsClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_StuAtmStatsClearStats_Type.__name__ = "Integer32"
_StuAtmStatsClearStats_Object = MibTableColumn
stuAtmStatsClearStats = _StuAtmStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 11, 1, 1, 9),
    _StuAtmStatsClearStats_Type()
)
stuAtmStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAtmStatsClearStats.setStatus("current")
_Com21StuAlarmSevGroup_ObjectIdentity = ObjectIdentity
com21StuAlarmSevGroup = _Com21StuAlarmSevGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12)
)
_Com21StuAlarmSevTable_Object = MibTable
com21StuAlarmSevTable = _Com21StuAlarmSevTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1)
)
if mibBuilder.loadTexts:
    com21StuAlarmSevTable.setStatus("current")
_Com21StuAlarmSevEntry_Object = MibTableRow
com21StuAlarmSevEntry = _Com21StuAlarmSevEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1, 1)
)
com21StuAlarmSevEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuAlmSevMacAddress"),
)
if mibBuilder.loadTexts:
    com21StuAlarmSevEntry.setStatus("current")
_StuAlmSevMacAddress_Type = MacAddress
_StuAlmSevMacAddress_Object = MibTableColumn
stuAlmSevMacAddress = _StuAlmSevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1, 1, 1),
    _StuAlmSevMacAddress_Type()
)
stuAlmSevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuAlmSevMacAddress.setStatus("current")
_StuAlmSevCrcThres_Type = AlarmSeverity
_StuAlmSevCrcThres_Object = MibTableColumn
stuAlmSevCrcThres = _StuAlmSevCrcThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1, 1, 2),
    _StuAlmSevCrcThres_Type()
)
stuAlmSevCrcThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAlmSevCrcThres.setStatus("current")
_StuAlmSevTeiThres_Type = AlarmSeverity
_StuAlmSevTeiThres_Object = MibTableColumn
stuAlmSevTeiThres = _StuAlmSevTeiThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1, 1, 3),
    _StuAlmSevTeiThres_Type()
)
stuAlmSevTeiThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAlmSevTeiThres.setStatus("current")
_StuAlmSevHecThres_Type = AlarmSeverity
_StuAlmSevHecThres_Object = MibTableColumn
stuAlmSevHecThres = _StuAlmSevHecThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1, 1, 4),
    _StuAlmSevHecThres_Type()
)
stuAlmSevHecThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAlmSevHecThres.setStatus("current")
_StuAlmSevEsThres_Type = AlarmSeverity
_StuAlmSevEsThres_Object = MibTableColumn
stuAlmSevEsThres = _StuAlmSevEsThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1, 1, 5),
    _StuAlmSevEsThres_Type()
)
stuAlmSevEsThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAlmSevEsThres.setStatus("current")
_StuAlmSevFecThres_Type = AlarmSeverity
_StuAlmSevFecThres_Object = MibTableColumn
stuAlmSevFecThres = _StuAlmSevFecThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 12, 1, 1, 6),
    _StuAlmSevFecThres_Type()
)
stuAlmSevFecThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuAlmSevFecThres.setStatus("current")
_Com21StuCodeImageGroup_ObjectIdentity = ObjectIdentity
com21StuCodeImageGroup = _Com21StuCodeImageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13)
)
_Com21StuCodeImageTable_Object = MibTable
com21StuCodeImageTable = _Com21StuCodeImageTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1)
)
if mibBuilder.loadTexts:
    com21StuCodeImageTable.setStatus("current")
_Com21StuCodeImageEntry_Object = MibTableRow
com21StuCodeImageEntry = _Com21StuCodeImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1)
)
com21StuCodeImageEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuCodeStuMacAddr"),
    (0, "COM21-HCXSTUPRXY-MIB", "stuCodeImageIndex"),
)
if mibBuilder.loadTexts:
    com21StuCodeImageEntry.setStatus("current")
_StuCodeStuMacAddr_Type = MacAddress
_StuCodeStuMacAddr_Object = MibTableColumn
stuCodeStuMacAddr = _StuCodeStuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1, 1),
    _StuCodeStuMacAddr_Type()
)
stuCodeStuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCodeStuMacAddr.setStatus("current")


class _StuCodeImageIndex_Type(Integer32):
    """Custom type stuCodeImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applicationStu", 2),
          ("downloadImage", 3),
          ("vxWorksImage", 1))
    )


_StuCodeImageIndex_Type.__name__ = "Integer32"
_StuCodeImageIndex_Object = MibTableColumn
stuCodeImageIndex = _StuCodeImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1, 2),
    _StuCodeImageIndex_Type()
)
stuCodeImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCodeImageIndex.setStatus("current")


class _StuCodeImageType_Type(Integer32):
    """Custom type stuCodeImageType based on Integer32"""
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
        *(("reserved1", 2),
          ("reserved2", 6),
          ("reserved3", 7),
          ("reserved4", 8),
          ("reserved5", 10),
          ("stuBoot", 1),
          ("stuDnld", 4),
          ("stuNewapp", 3),
          ("updateApp", 5),
          ("updateBoth", 9),
          ("vxWorks", 11))
    )


_StuCodeImageType_Type.__name__ = "Integer32"
_StuCodeImageType_Object = MibTableColumn
stuCodeImageType = _StuCodeImageType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1, 3),
    _StuCodeImageType_Type()
)
stuCodeImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCodeImageType.setStatus("current")


class _StuCodeImageVersion_Type(DisplayString):
    """Custom type stuCodeImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_StuCodeImageVersion_Type.__name__ = "DisplayString"
_StuCodeImageVersion_Object = MibTableColumn
stuCodeImageVersion = _StuCodeImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1, 4),
    _StuCodeImageVersion_Type()
)
stuCodeImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCodeImageVersion.setStatus("current")


class _StuCodeImageBuildDir_Type(DisplayString):
    """Custom type stuCodeImageBuildDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_StuCodeImageBuildDir_Type.__name__ = "DisplayString"
_StuCodeImageBuildDir_Object = MibTableColumn
stuCodeImageBuildDir = _StuCodeImageBuildDir_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1, 5),
    _StuCodeImageBuildDir_Type()
)
stuCodeImageBuildDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCodeImageBuildDir.setStatus("current")


class _StuCodeImageDate_Type(DisplayString):
    """Custom type stuCodeImageDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_StuCodeImageDate_Type.__name__ = "DisplayString"
_StuCodeImageDate_Object = MibTableColumn
stuCodeImageDate = _StuCodeImageDate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1, 6),
    _StuCodeImageDate_Type()
)
stuCodeImageDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCodeImageDate.setStatus("current")


class _StuCodeImageTime_Type(DisplayString):
    """Custom type stuCodeImageTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_StuCodeImageTime_Type.__name__ = "DisplayString"
_StuCodeImageTime_Object = MibTableColumn
stuCodeImageTime = _StuCodeImageTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 13, 1, 1, 7),
    _StuCodeImageTime_Type()
)
stuCodeImageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuCodeImageTime.setStatus("current")
_Com21StuVoiceChanStatsGroup_ObjectIdentity = ObjectIdentity
com21StuVoiceChanStatsGroup = _Com21StuVoiceChanStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14)
)
_Com21StuVoiceChanStatsTable_Object = MibTable
com21StuVoiceChanStatsTable = _Com21StuVoiceChanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1)
)
if mibBuilder.loadTexts:
    com21StuVoiceChanStatsTable.setStatus("current")
_Com21StuVoiceChanStatsEntry_Object = MibTableRow
com21StuVoiceChanStatsEntry = _Com21StuVoiceChanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1)
)
com21StuVoiceChanStatsEntry.setIndexNames(
    (0, "COM21-HCXSTUPRXY-MIB", "stuVoiceChanStatsMacAddr"),
    (0, "COM21-HCXSTUPRXY-MIB", "stuVoiceChanStatsNum"),
)
if mibBuilder.loadTexts:
    com21StuVoiceChanStatsEntry.setStatus("current")
_StuVoiceChanStatsMacAddr_Type = MacAddress
_StuVoiceChanStatsMacAddr_Object = MibTableColumn
stuVoiceChanStatsMacAddr = _StuVoiceChanStatsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 1),
    _StuVoiceChanStatsMacAddr_Type()
)
stuVoiceChanStatsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsMacAddr.setStatus("current")


class _StuVoiceChanStatsNum_Type(Integer32):
    """Custom type stuVoiceChanStatsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_StuVoiceChanStatsNum_Type.__name__ = "Integer32"
_StuVoiceChanStatsNum_Object = MibTableColumn
stuVoiceChanStatsNum = _StuVoiceChanStatsNum_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 2),
    _StuVoiceChanStatsNum_Type()
)
stuVoiceChanStatsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsNum.setStatus("current")
_StuVoiceChanStatsCurrLostCellCnt_Type = Integer32
_StuVoiceChanStatsCurrLostCellCnt_Object = MibTableColumn
stuVoiceChanStatsCurrLostCellCnt = _StuVoiceChanStatsCurrLostCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 3),
    _StuVoiceChanStatsCurrLostCellCnt_Type()
)
stuVoiceChanStatsCurrLostCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrLostCellCnt.setStatus("current")
_StuVoiceChanStatsCurrDrpdCellCnt_Type = Integer32
_StuVoiceChanStatsCurrDrpdCellCnt_Object = MibTableColumn
stuVoiceChanStatsCurrDrpdCellCnt = _StuVoiceChanStatsCurrDrpdCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 4),
    _StuVoiceChanStatsCurrDrpdCellCnt_Type()
)
stuVoiceChanStatsCurrDrpdCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrDrpdCellCnt.setStatus("current")
_StuVoiceChanStatsCurrCrc3ErrCnt_Type = Integer32
_StuVoiceChanStatsCurrCrc3ErrCnt_Object = MibTableColumn
stuVoiceChanStatsCurrCrc3ErrCnt = _StuVoiceChanStatsCurrCrc3ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 5),
    _StuVoiceChanStatsCurrCrc3ErrCnt_Type()
)
stuVoiceChanStatsCurrCrc3ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrCrc3ErrCnt.setStatus("current")
_StuVoiceChanStatsCurrSetUpFailCnt_Type = Integer32
_StuVoiceChanStatsCurrSetUpFailCnt_Object = MibTableColumn
stuVoiceChanStatsCurrSetUpFailCnt = _StuVoiceChanStatsCurrSetUpFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 6),
    _StuVoiceChanStatsCurrSetUpFailCnt_Type()
)
stuVoiceChanStatsCurrSetUpFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrSetUpFailCnt.setStatus("current")
_StuVoiceChanStatsCurrTxVoiceCellCnt_Type = Integer32
_StuVoiceChanStatsCurrTxVoiceCellCnt_Object = MibTableColumn
stuVoiceChanStatsCurrTxVoiceCellCnt = _StuVoiceChanStatsCurrTxVoiceCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 7),
    _StuVoiceChanStatsCurrTxVoiceCellCnt_Type()
)
stuVoiceChanStatsCurrTxVoiceCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrTxVoiceCellCnt.setStatus("current")
_StuVoiceChanStatsCurrRxVoiceCellCnt_Type = Integer32
_StuVoiceChanStatsCurrRxVoiceCellCnt_Object = MibTableColumn
stuVoiceChanStatsCurrRxVoiceCellCnt = _StuVoiceChanStatsCurrRxVoiceCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 8),
    _StuVoiceChanStatsCurrRxVoiceCellCnt_Type()
)
stuVoiceChanStatsCurrRxVoiceCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrRxVoiceCellCnt.setStatus("current")
_StuVoiceChanStatsCurrTxOamCellCnt_Type = Integer32
_StuVoiceChanStatsCurrTxOamCellCnt_Object = MibTableColumn
stuVoiceChanStatsCurrTxOamCellCnt = _StuVoiceChanStatsCurrTxOamCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 9),
    _StuVoiceChanStatsCurrTxOamCellCnt_Type()
)
stuVoiceChanStatsCurrTxOamCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrTxOamCellCnt.setStatus("current")
_StuVoiceChanStatsCurrRxOamCellCnt_Type = Integer32
_StuVoiceChanStatsCurrRxOamCellCnt_Object = MibTableColumn
stuVoiceChanStatsCurrRxOamCellCnt = _StuVoiceChanStatsCurrRxOamCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 10),
    _StuVoiceChanStatsCurrRxOamCellCnt_Type()
)
stuVoiceChanStatsCurrRxOamCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsCurrRxOamCellCnt.setStatus("current")
_StuVoiceChanStatsPrevLostCellCnt_Type = Integer32
_StuVoiceChanStatsPrevLostCellCnt_Object = MibTableColumn
stuVoiceChanStatsPrevLostCellCnt = _StuVoiceChanStatsPrevLostCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 11),
    _StuVoiceChanStatsPrevLostCellCnt_Type()
)
stuVoiceChanStatsPrevLostCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevLostCellCnt.setStatus("current")
_StuVoiceChanStatsPrevDrpdCellCnt_Type = Integer32
_StuVoiceChanStatsPrevDrpdCellCnt_Object = MibTableColumn
stuVoiceChanStatsPrevDrpdCellCnt = _StuVoiceChanStatsPrevDrpdCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 12),
    _StuVoiceChanStatsPrevDrpdCellCnt_Type()
)
stuVoiceChanStatsPrevDrpdCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevDrpdCellCnt.setStatus("current")
_StuVoiceChanStatsPrevCrc3ErrCnt_Type = Integer32
_StuVoiceChanStatsPrevCrc3ErrCnt_Object = MibTableColumn
stuVoiceChanStatsPrevCrc3ErrCnt = _StuVoiceChanStatsPrevCrc3ErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 13),
    _StuVoiceChanStatsPrevCrc3ErrCnt_Type()
)
stuVoiceChanStatsPrevCrc3ErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevCrc3ErrCnt.setStatus("current")
_StuVoiceChanStatsPrevSetUpFailCnt_Type = Integer32
_StuVoiceChanStatsPrevSetUpFailCnt_Object = MibTableColumn
stuVoiceChanStatsPrevSetUpFailCnt = _StuVoiceChanStatsPrevSetUpFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 14),
    _StuVoiceChanStatsPrevSetUpFailCnt_Type()
)
stuVoiceChanStatsPrevSetUpFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevSetUpFailCnt.setStatus("current")
_StuVoiceChanStatsPrevTxVoiceCellCnt_Type = Integer32
_StuVoiceChanStatsPrevTxVoiceCellCnt_Object = MibTableColumn
stuVoiceChanStatsPrevTxVoiceCellCnt = _StuVoiceChanStatsPrevTxVoiceCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 15),
    _StuVoiceChanStatsPrevTxVoiceCellCnt_Type()
)
stuVoiceChanStatsPrevTxVoiceCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevTxVoiceCellCnt.setStatus("current")
_StuVoiceChanStatsPrevRxVoiceCellCnt_Type = Integer32
_StuVoiceChanStatsPrevRxVoiceCellCnt_Object = MibTableColumn
stuVoiceChanStatsPrevRxVoiceCellCnt = _StuVoiceChanStatsPrevRxVoiceCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 16),
    _StuVoiceChanStatsPrevRxVoiceCellCnt_Type()
)
stuVoiceChanStatsPrevRxVoiceCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevRxVoiceCellCnt.setStatus("current")
_StuVoiceChanStatsPrevTxOamCellCnt_Type = Integer32
_StuVoiceChanStatsPrevTxOamCellCnt_Object = MibTableColumn
stuVoiceChanStatsPrevTxOamCellCnt = _StuVoiceChanStatsPrevTxOamCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 17),
    _StuVoiceChanStatsPrevTxOamCellCnt_Type()
)
stuVoiceChanStatsPrevTxOamCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevTxOamCellCnt.setStatus("current")
_StuVoiceChanStatsPrevRxOamCellCnt_Type = Integer32
_StuVoiceChanStatsPrevRxOamCellCnt_Object = MibTableColumn
stuVoiceChanStatsPrevRxOamCellCnt = _StuVoiceChanStatsPrevRxOamCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 18),
    _StuVoiceChanStatsPrevRxOamCellCnt_Type()
)
stuVoiceChanStatsPrevRxOamCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stuVoiceChanStatsPrevRxOamCellCnt.setStatus("current")


class _StuVoiceChanStatsClear_Type(Integer32):
    """Custom type stuVoiceChanStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_StuVoiceChanStatsClear_Type.__name__ = "Integer32"
_StuVoiceChanStatsClear_Object = MibTableColumn
stuVoiceChanStatsClear = _StuVoiceChanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1141, 3, 14, 1, 1, 19),
    _StuVoiceChanStatsClear_Type()
)
stuVoiceChanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stuVoiceChanStatsClear.setStatus("current")

# Managed Objects groups


# Notification objects

stuOperationStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 110)
)
stuOperationStateChange.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuCtrlMacAddress"),
        ("COM21-HCXSTUPRXY-MIB", "stuOperationState"))
)
if mibBuilder.loadTexts:
    stuOperationStateChange.setStatus(
        "current"
    )

stuXmitFeqChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 111)
)
stuXmitFeqChange.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuPhyMacAddress"),
        ("COM21-HCXSTUPRXY-MIB", "stuXmitFrequency"))
)
if mibBuilder.loadTexts:
    stuXmitFeqChange.setStatus(
        "current"
    )

stuEtherCrcThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 112)
)
stuEtherCrcThres.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuEthStatsMacAddr"),
        ("COM21-HCXSTUPRXY-MIB", "stuCurrEtherCrcErrs"),
        ("COM21-HCXSTUPRXY-MIB", "stuCurrEtherCrcThres"))
)
if mibBuilder.loadTexts:
    stuEtherCrcThres.setStatus(
        "current"
    )

stuAtmTeiThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 113)
)
stuAtmTeiThres.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsMacAddress"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsCurrAtmTei"),
        ("COM21-HCXSTUPRXY-MIB", "stuAtmTeiThreshold"))
)
if mibBuilder.loadTexts:
    stuAtmTeiThres.setStatus(
        "current"
    )

stuAtmHecThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 114)
)
stuAtmHecThres.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsMacAddress"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsCurrAtmHec"),
        ("COM21-HCXSTUPRXY-MIB", "stuAtmHecThreshold"))
)
if mibBuilder.loadTexts:
    stuAtmHecThres.setStatus(
        "current"
    )

stuESMinThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 115)
)
stuESMinThres.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsMacAddress"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsCurrESMin"),
        ("COM21-HCXSTUPRXY-MIB", "stuESMinThreshold"))
)
if mibBuilder.loadTexts:
    stuESMinThres.setStatus(
        "current"
    )

stuFecCorrectThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 116)
)
stuFecCorrectThres.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsMacAddress"),
        ("COM21-HCXSTUPRXY-MIB", "stuStatsCurrFecCorrect"),
        ("COM21-HCXSTUPRXY-MIB", "stuFecCorrectThreshold"))
)
if mibBuilder.loadTexts:
    stuFecCorrectThres.setStatus(
        "current"
    )

stuOutOfSpecRFCond = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 117)
)
stuOutOfSpecRFCond.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuPhyMacAddress"),
        ("COM21-HCXSTUPRXY-MIB", "stuRecvRfSigLevel"))
)
if mibBuilder.loadTexts:
    stuOutOfSpecRFCond.setStatus(
        "current"
    )

stuMaceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 119)
)
stuMaceFail.setObjects(
      *(("COM21-HCXSTUPRXY-MIB", "stuAlmSeverity"),
        ("COM21-HCXSTUPRXY-MIB", "stuAlmTime"),
        ("COM21-HCXSTUPRXY-MIB", "stuCtrlMacAddress"))
)
if mibBuilder.loadTexts:
    stuMaceFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXSTUPRXY-MIB",
    **{"FrequencyKhz": FrequencyKhz,
       "UpstrmFreqKhz": UpstrmFreqKhz,
       "EpochTime": EpochTime,
       "Offset": Offset,
       "AlarmSeverity": AlarmSeverity,
       "Com21RowStatus": Com21RowStatus,
       "com21StuPrxy": com21StuPrxy,
       "com21StuControlGroup": com21StuControlGroup,
       "com21StuControlTable": com21StuControlTable,
       "com21StuControlEntry": com21StuControlEntry,
       "stuCtrlMacAddress": stuCtrlMacAddress,
       "stuUserText": stuUserText,
       "stuSerialNumber": stuSerialNumber,
       "stuBoardRevision": stuBoardRevision,
       "stuUnitRevision": stuUnitRevision,
       "stuTunerRevision": stuTunerRevision,
       "stuModelName": stuModelName,
       "stuUnitManufacturer": stuUnitManufacturer,
       "stuDesKeySize": stuDesKeySize,
       "stuMibRevision": stuMibRevision,
       "stuEpochTime": stuEpochTime,
       "stuRestartAction": stuRestartAction,
       "stuPrevTestResult": stuPrevTestResult,
       "stuPrevTestFailCode": stuPrevTestFailCode,
       "stuOperationState": stuOperationState,
       "stuAimModuleId": stuAimModuleId,
       "stuUpstrmTestFreq": stuUpstrmTestFreq,
       "stuInbPresent": stuInbPresent,
       "stuInbContToneEnable": stuInbContToneEnable,
       "stuLastRestartCause": stuLastRestartCause,
       "stuUpstrmPingCntrl": stuUpstrmPingCntrl,
       "stuUpstrmTestTimeout": stuUpstrmTestTimeout,
       "stuDnstrmAltFreq": stuDnstrmAltFreq,
       "stuAsicRevision": stuAsicRevision,
       "stuVoiceAimLpBk": stuVoiceAimLpBk,
       "stuVoiceAimPort1Status": stuVoiceAimPort1Status,
       "stuVoiceAimPort2Status": stuVoiceAimPort2Status,
       "com21StuPhysicalGroup": com21StuPhysicalGroup,
       "com21StuPhysicalTable": com21StuPhysicalTable,
       "com21StuPhysicalEntry": com21StuPhysicalEntry,
       "stuPhyMacAddress": stuPhyMacAddress,
       "stuXmitFrequency": stuXmitFrequency,
       "stuRecvFrequency": stuRecvFrequency,
       "stuRecvRfSrEstimate": stuRecvRfSrEstimate,
       "stuRecvRfSigLevel": stuRecvRfSigLevel,
       "stuXmitOffset": stuXmitOffset,
       "stuXmitDacVRef": stuXmitDacVRef,
       "stuRecvFreqDrift": stuRecvFreqDrift,
       "com21StuAlarmGroup": com21StuAlarmGroup,
       "com21StuAlarmTable": com21StuAlarmTable,
       "com21StuAlarmEntry": com21StuAlarmEntry,
       "stuAlmMacAddress": stuAlmMacAddress,
       "stuAlmTime": stuAlmTime,
       "stuAlmTrapId": stuAlmTrapId,
       "stuAlmSeverity": stuAlmSeverity,
       "com21StuEtherConfigGroup": com21StuEtherConfigGroup,
       "com21StuEtherConfigTable": com21StuEtherConfigTable,
       "com21StuEtherConfigEntry": com21StuEtherConfigEntry,
       "stuEthMacAddress": stuEthMacAddress,
       "stuEtherFiltFlushAction": stuEtherFiltFlushAction,
       "stuEtherForwArpOnly": stuEtherForwArpOnly,
       "stuEtherMacFiltAge": stuEtherMacFiltAge,
       "stuEtherBCastRateEn": stuEtherBCastRateEn,
       "stuEtherBCastRateCo": stuEtherBCastRateCo,
       "stuEtherStickyBitCtrl": stuEtherStickyBitCtrl,
       "stuEther8021QEnable": stuEther8021QEnable,
       "stuEtherNonSnapRej": stuEtherNonSnapRej,
       "stuEtherIgmpEnable": stuEtherIgmpEnable,
       "stuEtherNonIpMultiEn": stuEtherNonIpMultiEn,
       "stuEtherBcmpOnly": stuEtherBcmpOnly,
       "stuEtherIgmpSnoopEnable": stuEtherIgmpSnoopEnable,
       "com21StuEtherTypeGroup": com21StuEtherTypeGroup,
       "com21StuEtherTypeTable": com21StuEtherTypeTable,
       "com21StuFiltEthTypeEntry": com21StuFiltEthTypeEntry,
       "stuFiltEtherMacAddr": stuFiltEtherMacAddr,
       "stuFiltEtherType": stuFiltEtherType,
       "stuFiltEtherStatus": stuFiltEtherStatus,
       "com21StuFiltIpMultiGroup": com21StuFiltIpMultiGroup,
       "com21StuFiltIpMultiTable": com21StuFiltIpMultiTable,
       "com21StuFiltIpMultiEntry": com21StuFiltIpMultiEntry,
       "stuFiltIpMacAddr": stuFiltIpMacAddr,
       "stuFiltIpMultiAddr": stuFiltIpMultiAddr,
       "stuFiltIpMultiStatus": stuFiltIpMultiStatus,
       "stuFiltIpDirectCntrl": stuFiltIpDirectCntrl,
       "com21StuEtherMacGroup": com21StuEtherMacGroup,
       "com21StuEtherMacTable": com21StuEtherMacTable,
       "com21StuEtherMacEntry": com21StuEtherMacEntry,
       "stuEtherStuMac": stuEtherStuMac,
       "stuEtherMacAddr": stuEtherMacAddr,
       "stuEtherMacType": stuEtherMacType,
       "stuEtherMacStatus": stuEtherMacStatus,
       "com21StuEtherStatsGroup": com21StuEtherStatsGroup,
       "com21StuEtherStatsTable": com21StuEtherStatsTable,
       "com21StuEtherStatsEntry": com21StuEtherStatsEntry,
       "stuEthStatsMacAddr": stuEthStatsMacAddr,
       "stuCurrEtherRunts": stuCurrEtherRunts,
       "stuCurrEtherCollitns": stuCurrEtherCollitns,
       "stuCurrEtherFramErrs": stuCurrEtherFramErrs,
       "stuCurrEtherCrcErrs": stuCurrEtherCrcErrs,
       "stuCurrEtherCrcThres": stuCurrEtherCrcThres,
       "stuCurrEtherTxUnder": stuCurrEtherTxUnder,
       "stuCurrEtherRxOver": stuCurrEtherRxOver,
       "stuCurrEtherDropFrms": stuCurrEtherDropFrms,
       "stuPrevEtherRunts": stuPrevEtherRunts,
       "stuPrevEtherCollitns": stuPrevEtherCollitns,
       "stuPrevEtherFramErrs": stuPrevEtherFramErrs,
       "stuPrevEtherCrcErrs": stuPrevEtherCrcErrs,
       "stuPrevEtherTxUnder": stuPrevEtherTxUnder,
       "stuPrevEtherRxOver": stuPrevEtherRxOver,
       "stuPrevEtherDropFrms": stuPrevEtherDropFrms,
       "stuEtherConnState": stuEtherConnState,
       "stuEtherClearStats": stuEtherClearStats,
       "com21StuStatsGroup": com21StuStatsGroup,
       "com21StuStatsTable": com21StuStatsTable,
       "com21StuStatsEntry": com21StuStatsEntry,
       "stuStatsMacAddress": stuStatsMacAddress,
       "stuStatsCurrAtmTei": stuStatsCurrAtmTei,
       "stuAtmTeiThreshold": stuAtmTeiThreshold,
       "stuStatsCurrAtmHec": stuStatsCurrAtmHec,
       "stuAtmHecThreshold": stuAtmHecThreshold,
       "stuStatsCurrESMin": stuStatsCurrESMin,
       "stuESMinThreshold": stuESMinThreshold,
       "stuStatsCurrFecCorrect": stuStatsCurrFecCorrect,
       "stuFecCorrectThreshold": stuFecCorrectThreshold,
       "stuStatsCurrUASMin": stuStatsCurrUASMin,
       "stuStatsPrevAtmTei": stuStatsPrevAtmTei,
       "stuStatsPrevAtmHec": stuStatsPrevAtmHec,
       "stuStatsPrevESMin": stuStatsPrevESMin,
       "stuStatsPrevFecCorrect": stuStatsPrevFecCorrect,
       "stuStatsPrevUASMin": stuStatsPrevUASMin,
       "stuStatsClearStats": stuStatsClearStats,
       "com21StuQStatsGroup": com21StuQStatsGroup,
       "com21StuQStatsTable": com21StuQStatsTable,
       "com21StuQStatsEntry": com21StuQStatsEntry,
       "stuAtmStuMacAddr": stuAtmStuMacAddr,
       "stuAtmStuQNo": stuAtmStuQNo,
       "stuAtmStatsCurrMinRx": stuAtmStatsCurrMinRx,
       "stuAtmStatsCurrMinRxDropped": stuAtmStatsCurrMinRxDropped,
       "stuAtmStatsCurrMinCRCErrors": stuAtmStatsCurrMinCRCErrors,
       "stuAtmStatsPrevMinRx": stuAtmStatsPrevMinRx,
       "stuAtmStatsPrevMinRxDropped": stuAtmStatsPrevMinRxDropped,
       "stuAtmStatsPrevMinCRCErrors": stuAtmStatsPrevMinCRCErrors,
       "stuAtmStatsClearStats": stuAtmStatsClearStats,
       "com21StuAlarmSevGroup": com21StuAlarmSevGroup,
       "com21StuAlarmSevTable": com21StuAlarmSevTable,
       "com21StuAlarmSevEntry": com21StuAlarmSevEntry,
       "stuAlmSevMacAddress": stuAlmSevMacAddress,
       "stuAlmSevCrcThres": stuAlmSevCrcThres,
       "stuAlmSevTeiThres": stuAlmSevTeiThres,
       "stuAlmSevHecThres": stuAlmSevHecThres,
       "stuAlmSevEsThres": stuAlmSevEsThres,
       "stuAlmSevFecThres": stuAlmSevFecThres,
       "com21StuCodeImageGroup": com21StuCodeImageGroup,
       "com21StuCodeImageTable": com21StuCodeImageTable,
       "com21StuCodeImageEntry": com21StuCodeImageEntry,
       "stuCodeStuMacAddr": stuCodeStuMacAddr,
       "stuCodeImageIndex": stuCodeImageIndex,
       "stuCodeImageType": stuCodeImageType,
       "stuCodeImageVersion": stuCodeImageVersion,
       "stuCodeImageBuildDir": stuCodeImageBuildDir,
       "stuCodeImageDate": stuCodeImageDate,
       "stuCodeImageTime": stuCodeImageTime,
       "com21StuVoiceChanStatsGroup": com21StuVoiceChanStatsGroup,
       "com21StuVoiceChanStatsTable": com21StuVoiceChanStatsTable,
       "com21StuVoiceChanStatsEntry": com21StuVoiceChanStatsEntry,
       "stuVoiceChanStatsMacAddr": stuVoiceChanStatsMacAddr,
       "stuVoiceChanStatsNum": stuVoiceChanStatsNum,
       "stuVoiceChanStatsCurrLostCellCnt": stuVoiceChanStatsCurrLostCellCnt,
       "stuVoiceChanStatsCurrDrpdCellCnt": stuVoiceChanStatsCurrDrpdCellCnt,
       "stuVoiceChanStatsCurrCrc3ErrCnt": stuVoiceChanStatsCurrCrc3ErrCnt,
       "stuVoiceChanStatsCurrSetUpFailCnt": stuVoiceChanStatsCurrSetUpFailCnt,
       "stuVoiceChanStatsCurrTxVoiceCellCnt": stuVoiceChanStatsCurrTxVoiceCellCnt,
       "stuVoiceChanStatsCurrRxVoiceCellCnt": stuVoiceChanStatsCurrRxVoiceCellCnt,
       "stuVoiceChanStatsCurrTxOamCellCnt": stuVoiceChanStatsCurrTxOamCellCnt,
       "stuVoiceChanStatsCurrRxOamCellCnt": stuVoiceChanStatsCurrRxOamCellCnt,
       "stuVoiceChanStatsPrevLostCellCnt": stuVoiceChanStatsPrevLostCellCnt,
       "stuVoiceChanStatsPrevDrpdCellCnt": stuVoiceChanStatsPrevDrpdCellCnt,
       "stuVoiceChanStatsPrevCrc3ErrCnt": stuVoiceChanStatsPrevCrc3ErrCnt,
       "stuVoiceChanStatsPrevSetUpFailCnt": stuVoiceChanStatsPrevSetUpFailCnt,
       "stuVoiceChanStatsPrevTxVoiceCellCnt": stuVoiceChanStatsPrevTxVoiceCellCnt,
       "stuVoiceChanStatsPrevRxVoiceCellCnt": stuVoiceChanStatsPrevRxVoiceCellCnt,
       "stuVoiceChanStatsPrevTxOamCellCnt": stuVoiceChanStatsPrevTxOamCellCnt,
       "stuVoiceChanStatsPrevRxOamCellCnt": stuVoiceChanStatsPrevRxOamCellCnt,
       "stuVoiceChanStatsClear": stuVoiceChanStatsClear,
       "stuOperationStateChange": stuOperationStateChange,
       "stuXmitFeqChange": stuXmitFeqChange,
       "stuEtherCrcThres": stuEtherCrcThres,
       "stuAtmTeiThres": stuAtmTeiThres,
       "stuAtmHecThres": stuAtmHecThres,
       "stuESMinThres": stuESMinThres,
       "stuFecCorrectThres": stuFecCorrectThres,
       "stuOutOfSpecRFCond": stuOutOfSpecRFCond,
       "stuMaceFail": stuMaceFail}
)
