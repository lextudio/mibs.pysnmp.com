# SNMP MIB module (NEXANS-BM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NEXANS-BM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:23 2024
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

(nexansANS,) = mibBuilder.importSymbols(
    "NEXANS-MIB",
    "nexansANS")

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

bmSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 266, 20)
)
bmSwitchMIB.setRevisions(
        ("2014-01-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BmTraps_ObjectIdentity = ObjectIdentity
bmTraps = _BmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 20, 0)
)
_BmSwitchInfo_ObjectIdentity = ObjectIdentity
bmSwitchInfo = _BmSwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 20, 1)
)


class _InfoDescr_Type(DisplayString):
    """Custom type infoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_InfoDescr_Type.__name__ = "DisplayString"
_InfoDescr_Object = MibScalar
infoDescr = _InfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 1),
    _InfoDescr_Type()
)
infoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDescr.setStatus("current")
_InfoType_Type = Integer32
_InfoType_Object = MibScalar
infoType = _InfoType_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 2),
    _InfoType_Type()
)
infoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoType.setStatus("current")


class _InfoProductNo_Type(DisplayString):
    """Custom type infoProductNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_InfoProductNo_Type.__name__ = "DisplayString"
_InfoProductNo_Object = MibScalar
infoProductNo = _InfoProductNo_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 3),
    _InfoProductNo_Type()
)
infoProductNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProductNo.setStatus("current")


class _InfoSerie_Type(DisplayString):
    """Custom type infoSerie based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_InfoSerie_Type.__name__ = "DisplayString"
_InfoSerie_Object = MibScalar
infoSerie = _InfoSerie_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 4),
    _InfoSerie_Type()
)
infoSerie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSerie.setStatus("current")


class _InfoSeriesNo_Type(DisplayString):
    """Custom type infoSeriesNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_InfoSeriesNo_Type.__name__ = "DisplayString"
_InfoSeriesNo_Object = MibScalar
infoSeriesNo = _InfoSeriesNo_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 5),
    _InfoSeriesNo_Type()
)
infoSeriesNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSeriesNo.setStatus("current")


class _InfoManufactureDate_Type(DisplayString):
    """Custom type infoManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_InfoManufactureDate_Type.__name__ = "DisplayString"
_InfoManufactureDate_Object = MibScalar
infoManufactureDate = _InfoManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 6),
    _InfoManufactureDate_Type()
)
infoManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoManufactureDate.setStatus("current")


class _InfoSwitchHardwareVersion_Type(DisplayString):
    """Custom type infoSwitchHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_InfoSwitchHardwareVersion_Type.__name__ = "DisplayString"
_InfoSwitchHardwareVersion_Object = MibScalar
infoSwitchHardwareVersion = _InfoSwitchHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 7),
    _InfoSwitchHardwareVersion_Type()
)
infoSwitchHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSwitchHardwareVersion.setStatus("current")


class _InfoMgmtHardwareVersion_Type(DisplayString):
    """Custom type infoMgmtHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_InfoMgmtHardwareVersion_Type.__name__ = "DisplayString"
_InfoMgmtHardwareVersion_Object = MibScalar
infoMgmtHardwareVersion = _InfoMgmtHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 8),
    _InfoMgmtHardwareVersion_Type()
)
infoMgmtHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMgmtHardwareVersion.setStatus("current")


class _InfoMgmtFirmwareVersion_Type(DisplayString):
    """Custom type infoMgmtFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_InfoMgmtFirmwareVersion_Type.__name__ = "DisplayString"
_InfoMgmtFirmwareVersion_Object = MibScalar
infoMgmtFirmwareVersion = _InfoMgmtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 9),
    _InfoMgmtFirmwareVersion_Type()
)
infoMgmtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMgmtFirmwareVersion.setStatus("current")
_InfoNoOfPorts_Type = Integer32
_InfoNoOfPorts_Object = MibScalar
infoNoOfPorts = _InfoNoOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 10),
    _InfoNoOfPorts_Type()
)
infoNoOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoNoOfPorts.setStatus("current")
_InfoNoOfReboots_Type = Counter32
_InfoNoOfReboots_Object = MibScalar
infoNoOfReboots = _InfoNoOfReboots_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 11),
    _InfoNoOfReboots_Type()
)
infoNoOfReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoNoOfReboots.setStatus("current")
_InfoTemperature_Type = Integer32
_InfoTemperature_Object = MibScalar
infoTemperature = _InfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 12),
    _InfoTemperature_Type()
)
infoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperature.setStatus("current")
_InfoTemperatureMaxAllowed_Type = Integer32
_InfoTemperatureMaxAllowed_Object = MibScalar
infoTemperatureMaxAllowed = _InfoTemperatureMaxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 13),
    _InfoTemperatureMaxAllowed_Type()
)
infoTemperatureMaxAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureMaxAllowed.setStatus("current")
_InfoPowerVoltage2500_Type = Integer32
_InfoPowerVoltage2500_Object = MibScalar
infoPowerVoltage2500 = _InfoPowerVoltage2500_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 14),
    _InfoPowerVoltage2500_Type()
)
infoPowerVoltage2500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerVoltage2500.setStatus("current")
_InfoPowerVoltage3300_Type = Integer32
_InfoPowerVoltage3300_Object = MibScalar
infoPowerVoltage3300 = _InfoPowerVoltage3300_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 15),
    _InfoPowerVoltage3300_Type()
)
infoPowerVoltage3300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerVoltage3300.setStatus("current")
_InfoUnauthIpAddr_Type = IpAddress
_InfoUnauthIpAddr_Object = MibScalar
infoUnauthIpAddr = _InfoUnauthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 16),
    _InfoUnauthIpAddr_Type()
)
infoUnauthIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoUnauthIpAddr.setStatus("current")


class _InfoSecurityFailMacAddr_Type(DisplayString):
    """Custom type infoSecurityFailMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_InfoSecurityFailMacAddr_Type.__name__ = "DisplayString"
_InfoSecurityFailMacAddr_Object = MibScalar
infoSecurityFailMacAddr = _InfoSecurityFailMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 17),
    _InfoSecurityFailMacAddr_Type()
)
infoSecurityFailMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSecurityFailMacAddr.setStatus("current")


class _InfoNewMacAddr_Type(DisplayString):
    """Custom type infoNewMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_InfoNewMacAddr_Type.__name__ = "DisplayString"
_InfoNewMacAddr_Object = MibScalar
infoNewMacAddr = _InfoNewMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 18),
    _InfoNewMacAddr_Type()
)
infoNewMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoNewMacAddr.setStatus("current")
_InfoPoeInputVoltage_Type = Integer32
_InfoPoeInputVoltage_Object = MibScalar
infoPoeInputVoltage = _InfoPoeInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 19),
    _InfoPoeInputVoltage_Type()
)
infoPoeInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPoeInputVoltage.setStatus("current")
_InfoPoeInputPower_Type = Integer32
_InfoPoeInputPower_Object = MibScalar
infoPoeInputPower = _InfoPoeInputPower_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 20),
    _InfoPoeInputPower_Type()
)
infoPoeInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPoeInputPower.setStatus("current")


class _InfoAlarmStateM1_Type(Integer32):
    """Custom type infoAlarmStateM1 based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("alarmContactForcedOpen", 16),
          ("alarmContactForcedShorted", 15),
          ("alarmOff", 2),
          ("alarmOffForced", 6),
          ("alarmOn", 3),
          ("alarmOnForced", 5),
          ("alarmOnFunctionInputOpen", 11),
          ("alarmOnFunctionInputShorted", 10),
          ("alarmOnLinkDown", 4),
          ("alarmOnLocalAlarmDestTable", 14),
          ("alarmOnPowerSupplyS1", 7),
          ("alarmOnPowerSupplyS1orS2", 9),
          ("alarmOnPowerSupplyS2", 8),
          ("alarmOnRemoteAlarmDestTable", 13),
          ("alarmOnRemoteFunctionInput", 12),
          ("notSupported", 1))
    )


_InfoAlarmStateM1_Type.__name__ = "Integer32"
_InfoAlarmStateM1_Object = MibScalar
infoAlarmStateM1 = _InfoAlarmStateM1_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 21),
    _InfoAlarmStateM1_Type()
)
infoAlarmStateM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoAlarmStateM1.setStatus("current")


class _InfoAlarmStateM2_Type(Integer32):
    """Custom type infoAlarmStateM2 based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("alarmContactForcedOpen", 16),
          ("alarmContactForcedShorted", 15),
          ("alarmOff", 2),
          ("alarmOffForced", 6),
          ("alarmOn", 3),
          ("alarmOnForced", 5),
          ("alarmOnFunctionInputOpen", 11),
          ("alarmOnFunctionInputShorted", 10),
          ("alarmOnLinkDown", 4),
          ("alarmOnLocalAlarmDestTable", 14),
          ("alarmOnPowerSupplyS1", 7),
          ("alarmOnPowerSupplyS1orS2", 9),
          ("alarmOnPowerSupplyS2", 8),
          ("alarmOnRemoteAlarmDestTable", 13),
          ("alarmOnRemoteFunctionInput", 12),
          ("notSupported", 1))
    )


_InfoAlarmStateM2_Type.__name__ = "Integer32"
_InfoAlarmStateM2_Object = MibScalar
infoAlarmStateM2 = _InfoAlarmStateM2_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 22),
    _InfoAlarmStateM2_Type()
)
infoAlarmStateM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoAlarmStateM2.setStatus("current")


class _InfoLastTftpMessage_Type(DisplayString):
    """Custom type infoLastTftpMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_InfoLastTftpMessage_Type.__name__ = "DisplayString"
_InfoLastTftpMessage_Object = MibScalar
infoLastTftpMessage = _InfoLastTftpMessage_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 23),
    _InfoLastTftpMessage_Type()
)
infoLastTftpMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoLastTftpMessage.setStatus("current")


class _InfoLastSfpEventMessage_Type(DisplayString):
    """Custom type infoLastSfpEventMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_InfoLastSfpEventMessage_Type.__name__ = "DisplayString"
_InfoLastSfpEventMessage_Object = MibScalar
infoLastSfpEventMessage = _InfoLastSfpEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 24),
    _InfoLastSfpEventMessage_Type()
)
infoLastSfpEventMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoLastSfpEventMessage.setStatus("current")


class _InfoLastInternalMgmtWarning_Type(DisplayString):
    """Custom type infoLastInternalMgmtWarning based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_InfoLastInternalMgmtWarning_Type.__name__ = "DisplayString"
_InfoLastInternalMgmtWarning_Object = MibScalar
infoLastInternalMgmtWarning = _InfoLastInternalMgmtWarning_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 25),
    _InfoLastInternalMgmtWarning_Type()
)
infoLastInternalMgmtWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoLastInternalMgmtWarning.setStatus("current")


class _InfoFunctionInputStateF1_Type(Integer32):
    """Custom type infoFunctionInputStateF1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("functionInputOpen", 3),
          ("functionInputShorted", 2),
          ("notSupported", 1))
    )


_InfoFunctionInputStateF1_Type.__name__ = "Integer32"
_InfoFunctionInputStateF1_Object = MibScalar
infoFunctionInputStateF1 = _InfoFunctionInputStateF1_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 26),
    _InfoFunctionInputStateF1_Type()
)
infoFunctionInputStateF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFunctionInputStateF1.setStatus("current")
_InfoTotalConfigChanges_Type = Counter32
_InfoTotalConfigChanges_Object = MibScalar
infoTotalConfigChanges = _InfoTotalConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 1, 27),
    _InfoTotalConfigChanges_Type()
)
infoTotalConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTotalConfigChanges.setStatus("current")
_BmSwitchAdmin_ObjectIdentity = ObjectIdentity
bmSwitchAdmin = _BmSwitchAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 20, 2)
)


class _AdminReset_Type(Integer32):
    """Custom type adminReset based on Integer32"""
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
        *(("rebootSwitch", 3),
          ("rebootToFactoryDefaults", 4),
          ("renewIpAndVlanParameter", 5),
          ("resetCounters", 2),
          ("resetIdle", 1))
    )


_AdminReset_Type.__name__ = "Integer32"
_AdminReset_Object = MibScalar
adminReset = _AdminReset_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 1),
    _AdminReset_Type()
)
adminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminReset.setStatus("current")


class _AdminAgentDhcp_Type(Integer32):
    """Custom type adminAgentDhcp based on Integer32"""
    defaultValue = 1

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


_AdminAgentDhcp_Type.__name__ = "Integer32"
_AdminAgentDhcp_Object = MibScalar
adminAgentDhcp = _AdminAgentDhcp_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 2),
    _AdminAgentDhcp_Type()
)
adminAgentDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAgentDhcp.setStatus("current")
_AdminAgentIpAddress_Type = IpAddress
_AdminAgentIpAddress_Object = MibScalar
adminAgentIpAddress = _AdminAgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 3),
    _AdminAgentIpAddress_Type()
)
adminAgentIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAgentIpAddress.setStatus("current")
_AdminAgentPhysAddress_Type = MacAddress
_AdminAgentPhysAddress_Object = MibScalar
adminAgentPhysAddress = _AdminAgentPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 4),
    _AdminAgentPhysAddress_Type()
)
adminAgentPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminAgentPhysAddress.setStatus("current")
_AdminAgentDefRouterIpAddress_Type = IpAddress
_AdminAgentDefRouterIpAddress_Object = MibScalar
adminAgentDefRouterIpAddress = _AdminAgentDefRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 5),
    _AdminAgentDefRouterIpAddress_Type()
)
adminAgentDefRouterIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAgentDefRouterIpAddress.setStatus("current")
_AdminAgentNetmask_Type = IpAddress
_AdminAgentNetmask_Object = MibScalar
adminAgentNetmask = _AdminAgentNetmask_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 6),
    _AdminAgentNetmask_Type()
)
adminAgentNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAgentNetmask.setStatus("current")
_AdminAgentDhcpServerIpAddress_Type = IpAddress
_AdminAgentDhcpServerIpAddress_Object = MibScalar
adminAgentDhcpServerIpAddress = _AdminAgentDhcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 7),
    _AdminAgentDhcpServerIpAddress_Type()
)
adminAgentDhcpServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminAgentDhcpServerIpAddress.setStatus("current")


class _AdminAgentVlanId_Type(Integer32):
    """Custom type adminAgentVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdminAgentVlanId_Type.__name__ = "Integer32"
_AdminAgentVlanId_Object = MibScalar
adminAgentVlanId = _AdminAgentVlanId_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 8),
    _AdminAgentVlanId_Type()
)
adminAgentVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAgentVlanId.setStatus("current")


class _AdminAgentPrioValue_Type(Integer32):
    """Custom type adminAgentPrioValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdminAgentPrioValue_Type.__name__ = "Integer32"
_AdminAgentPrioValue_Object = MibScalar
adminAgentPrioValue = _AdminAgentPrioValue_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 9),
    _AdminAgentPrioValue_Type()
)
adminAgentPrioValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAgentPrioValue.setStatus("current")


class _AdminAddrAgingTimeMinutes_Type(Integer32):
    """Custom type adminAddrAgingTimeMinutes based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 68),
    )


_AdminAddrAgingTimeMinutes_Type.__name__ = "Integer32"
_AdminAddrAgingTimeMinutes_Object = MibScalar
adminAddrAgingTimeMinutes = _AdminAddrAgingTimeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 10),
    _AdminAddrAgingTimeMinutes_Type()
)
adminAddrAgingTimeMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAddrAgingTimeMinutes.setStatus("current")


class _AdminSwitchPortMirror_Type(Integer32):
    """Custom type adminSwitchPortMirror based on Integer32"""
    defaultValue = 2

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


_AdminSwitchPortMirror_Type.__name__ = "Integer32"
_AdminSwitchPortMirror_Object = MibScalar
adminSwitchPortMirror = _AdminSwitchPortMirror_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 11),
    _AdminSwitchPortMirror_Type()
)
adminSwitchPortMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSwitchPortMirror.setStatus("current")


class _AdminMgmtAccessList_Type(Integer32):
    """Custom type adminMgmtAccessList based on Integer32"""
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
        *(("disable", 1),
          ("enableForAllAccess", 3),
          ("enableForNexManAccess", 2),
          ("enableForSnmpAccess", 4))
    )


_AdminMgmtAccessList_Type.__name__ = "Integer32"
_AdminMgmtAccessList_Object = MibScalar
adminMgmtAccessList = _AdminMgmtAccessList_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 12),
    _AdminMgmtAccessList_Type()
)
adminMgmtAccessList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMgmtAccessList.setStatus("current")
_AdminSwitchPoEPowerLimit_Type = Integer32
_AdminSwitchPoEPowerLimit_Object = MibScalar
adminSwitchPoEPowerLimit = _AdminSwitchPoEPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 13),
    _AdminSwitchPoEPowerLimit_Type()
)
adminSwitchPoEPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSwitchPoEPowerLimit.setStatus("current")


class _AdminSwitchVlanTableMode_Type(Integer32):
    """Custom type adminSwitchVlanTableMode based on Integer32"""
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
        *(("dynamicMode", 2),
          ("staticMode", 1),
          ("staticModePortBased", 4),
          ("staticModeVlans64", 3))
    )


_AdminSwitchVlanTableMode_Type.__name__ = "Integer32"
_AdminSwitchVlanTableMode_Object = MibScalar
adminSwitchVlanTableMode = _AdminSwitchVlanTableMode_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 14),
    _AdminSwitchVlanTableMode_Type()
)
adminSwitchVlanTableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSwitchVlanTableMode.setStatus("current")


class _AdminUnsecureVlanId_Type(Integer32):
    """Custom type adminUnsecureVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdminUnsecureVlanId_Type.__name__ = "Integer32"
_AdminUnsecureVlanId_Object = MibScalar
adminUnsecureVlanId = _AdminUnsecureVlanId_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 15),
    _AdminUnsecureVlanId_Type()
)
adminUnsecureVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminUnsecureVlanId.setStatus("current")


class _AdminDot1xAuthFailureVlanId_Type(Integer32):
    """Custom type adminDot1xAuthFailureVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AdminDot1xAuthFailureVlanId_Type.__name__ = "Integer32"
_AdminDot1xAuthFailureVlanId_Object = MibScalar
adminDot1xAuthFailureVlanId = _AdminDot1xAuthFailureVlanId_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 16),
    _AdminDot1xAuthFailureVlanId_Type()
)
adminDot1xAuthFailureVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDot1xAuthFailureVlanId.setStatus("current")


class _AdminTftpAccess_Type(Integer32):
    """Custom type adminTftpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftpAccessDisable", 1),
          ("tftpAccessReadOnly", 2),
          ("tftpAccessReadWrite", 3))
    )


_AdminTftpAccess_Type.__name__ = "Integer32"
_AdminTftpAccess_Object = MibScalar
adminTftpAccess = _AdminTftpAccess_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 17),
    _AdminTftpAccess_Type()
)
adminTftpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTftpAccess.setStatus("current")


class _AdminSnmpMacTableMode_Type(Integer32):
    """Custom type adminSnmpMacTableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("listAllPorts", 1),
          ("listUserPortsOnly", 2))
    )


_AdminSnmpMacTableMode_Type.__name__ = "Integer32"
_AdminSnmpMacTableMode_Object = MibScalar
adminSnmpMacTableMode = _AdminSnmpMacTableMode_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 18),
    _AdminSnmpMacTableMode_Type()
)
adminSnmpMacTableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSnmpMacTableMode.setStatus("current")


class _AdminAlarmM1_Type(Integer32):
    """Custom type adminAlarmM1 based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("alarmForceContactOpen", 14),
          ("alarmForceContactOpenShorted", 15),
          ("alarmForceContactShorted", 13),
          ("alarmLinkDown", 2),
          ("alarmLocalAlarmDestination", 12),
          ("alarmLocalFunctionInputOpen", 9),
          ("alarmLocalFunctionInputShorted", 8),
          ("alarmOffForced", 4),
          ("alarmOnForced", 3),
          ("alarmPowerSupply1Failure", 5),
          ("alarmPowerSupply1or2Failure", 7),
          ("alarmPowerSupply2Failure", 6),
          ("alarmRemoteAlarmDestination", 11),
          ("alarmRemoteFunctionInput", 10),
          ("notSupported", 1))
    )


_AdminAlarmM1_Type.__name__ = "Integer32"
_AdminAlarmM1_Object = MibScalar
adminAlarmM1 = _AdminAlarmM1_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 19),
    _AdminAlarmM1_Type()
)
adminAlarmM1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAlarmM1.setStatus("current")


class _AdminAlarmM2_Type(Integer32):
    """Custom type adminAlarmM2 based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("alarmForceContactOpen", 14),
          ("alarmForceContactOpenShorted", 15),
          ("alarmForceContactShorted", 13),
          ("alarmLinkDown", 2),
          ("alarmLocalAlarmDestination", 12),
          ("alarmLocalFunctionInputOpen", 9),
          ("alarmLocalFunctionInputShorted", 8),
          ("alarmOffForced", 4),
          ("alarmOnForced", 3),
          ("alarmPowerSupply1Failure", 5),
          ("alarmPowerSupply1or2Failure", 7),
          ("alarmPowerSupply2Failure", 6),
          ("alarmRemoteAlarmDestination", 11),
          ("alarmRemoteFunctionInput", 10),
          ("notSupported", 1))
    )


_AdminAlarmM2_Type.__name__ = "Integer32"
_AdminAlarmM2_Object = MibScalar
adminAlarmM2 = _AdminAlarmM2_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 20),
    _AdminAlarmM2_Type()
)
adminAlarmM2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAlarmM2.setStatus("current")


class _AdminMemoryCardMode_Type(Integer32):
    """Custom type adminMemoryCardMode based on Integer32"""
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
        *(("mcDisabled", 3),
          ("mcEnabled", 2),
          ("mcPermanentDisabled", 4),
          ("notSupported", 1))
    )


_AdminMemoryCardMode_Type.__name__ = "Integer32"
_AdminMemoryCardMode_Object = MibScalar
adminMemoryCardMode = _AdminMemoryCardMode_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 21),
    _AdminMemoryCardMode_Type()
)
adminMemoryCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMemoryCardMode.setStatus("current")


class _AdminAlarmNameM1_Type(DisplayString):
    """Custom type adminAlarmNameM1 based on DisplayString"""
    defaultValue = OctetString("not defined")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminAlarmNameM1_Type.__name__ = "DisplayString"
_AdminAlarmNameM1_Object = MibScalar
adminAlarmNameM1 = _AdminAlarmNameM1_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 22),
    _AdminAlarmNameM1_Type()
)
adminAlarmNameM1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAlarmNameM1.setStatus("current")


class _AdminAlarmNameM2_Type(DisplayString):
    """Custom type adminAlarmNameM2 based on DisplayString"""
    defaultValue = OctetString("not defined")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminAlarmNameM2_Type.__name__ = "DisplayString"
_AdminAlarmNameM2_Object = MibScalar
adminAlarmNameM2 = _AdminAlarmNameM2_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 23),
    _AdminAlarmNameM2_Type()
)
adminAlarmNameM2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAlarmNameM2.setStatus("current")


class _AdminFunctionInputNameF1_Type(DisplayString):
    """Custom type adminFunctionInputNameF1 based on DisplayString"""
    defaultValue = OctetString("not defined")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdminFunctionInputNameF1_Type.__name__ = "DisplayString"
_AdminFunctionInputNameF1_Object = MibScalar
adminFunctionInputNameF1 = _AdminFunctionInputNameF1_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 24),
    _AdminFunctionInputNameF1_Type()
)
adminFunctionInputNameF1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminFunctionInputNameF1.setStatus("current")


class _AdminLedGlobalMode_Type(Integer32):
    """Custom type adminLedGlobalMode based on Integer32"""
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
        *(("ledGlobalModeAllOff", 3),
          ("ledGlobalModeAllOn", 4),
          ("ledGlobalModeMgmtOnly", 5),
          ("ledGlobalModeNotSupported", 1),
          ("ledGlobalModeStandard", 2))
    )


_AdminLedGlobalMode_Type.__name__ = "Integer32"
_AdminLedGlobalMode_Object = MibScalar
adminLedGlobalMode = _AdminLedGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 2, 25),
    _AdminLedGlobalMode_Type()
)
adminLedGlobalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminLedGlobalMode.setStatus("current")
_BmSwitchPort_ObjectIdentity = ObjectIdentity
bmSwitchPort = _BmSwitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 20, 3)
)
_BmSwitchPortTable_Object = MibTable
bmSwitchPortTable = _BmSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1)
)
if mibBuilder.loadTexts:
    bmSwitchPortTable.setStatus("current")
_BmSwitchPortEntry_Object = MibTableRow
bmSwitchPortEntry = _BmSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1)
)
bmSwitchPortEntry.setIndexNames(
    (0, "NEXANS-BM-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    bmSwitchPortEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortDescr_Type(DisplayString):
    """Custom type portDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortDescr_Type.__name__ = "DisplayString"
_PortDescr_Object = MibTableColumn
portDescr = _PortDescr_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 2),
    _PortDescr_Type()
)
portDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDescr.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 3),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortAdminState_Type(Integer32):
    """Custom type portAdminState based on Integer32"""
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
        *(("adminDisable", 3),
          ("allwaysEnable", 1),
          ("bpduDisable", 6),
          ("enable", 2),
          ("errorCountDisable", 9),
          ("linkFlapDisable", 8),
          ("loopDisable", 5),
          ("redundanyLoopDisable", 11),
          ("securityDisable", 4),
          ("sfpErrorDisable", 10),
          ("udldDisable", 7))
    )


_PortAdminState_Type.__name__ = "Integer32"
_PortAdminState_Object = MibTableColumn
portAdminState = _PortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 4),
    _PortAdminState_Type()
)
portAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminState.setStatus("current")


class _PortSpeedDuplexSetup_Type(Integer32):
    """Custom type portSpeedDuplexSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("autoneg", 1),
          ("eco", 9),
          ("ecoOverTemp", 10),
          ("ecoPowerSave", 11),
          ("fix1000Fdx", 8),
          ("fix1000Hdx", 7),
          ("fix1000fdxNoAutoneg", 12),
          ("fix100Fdx", 5),
          ("fix100Hdx", 4),
          ("fix10Fdx", 3),
          ("fix10Hdx", 2))
    )


_PortSpeedDuplexSetup_Type.__name__ = "Integer32"
_PortSpeedDuplexSetup_Object = MibTableColumn
portSpeedDuplexSetup = _PortSpeedDuplexSetup_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 5),
    _PortSpeedDuplexSetup_Type()
)
portSpeedDuplexSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDuplexSetup.setStatus("current")


class _PortLinkState_Type(Integer32):
    """Custom type portLinkState based on Integer32"""
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
        *(("down", 1),
          ("up1000Fdx", 7),
          ("up1000Hdx", 6),
          ("up100Fdx", 5),
          ("up100Hdx", 4),
          ("up10Fdx", 3),
          ("up10Hdx", 2))
    )


_PortLinkState_Type.__name__ = "Integer32"
_PortLinkState_Object = MibTableColumn
portLinkState = _PortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 6),
    _PortLinkState_Type()
)
portLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkState.setStatus("current")
_PortErrorCounter_Type = Counter32
_PortErrorCounter_Object = MibTableColumn
portErrorCounter = _PortErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 7),
    _PortErrorCounter_Type()
)
portErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrorCounter.setStatus("current")


class _PortRemoteFault_Type(Integer32):
    """Custom type portRemoteFault based on Integer32"""
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
          ("enable", 2),
          ("notSupported", 1))
    )


_PortRemoteFault_Type.__name__ = "Integer32"
_PortRemoteFault_Object = MibTableColumn
portRemoteFault = _PortRemoteFault_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 8),
    _PortRemoteFault_Type()
)
portRemoteFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRemoteFault.setStatus("current")


class _PortDefaultVlanId_Type(Integer32):
    """Custom type portDefaultVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PortDefaultVlanId_Type.__name__ = "Integer32"
_PortDefaultVlanId_Object = MibTableColumn
portDefaultVlanId = _PortDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 9),
    _PortDefaultVlanId_Type()
)
portDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDefaultVlanId.setStatus("current")


class _PortTrunkingMode_Type(Integer32):
    """Custom type portTrunkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("dot1qTagging", 1),
          ("enableWithoutTagging", 3))
    )


_PortTrunkingMode_Type.__name__ = "Integer32"
_PortTrunkingMode_Object = MibTableColumn
portTrunkingMode = _PortTrunkingMode_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 10),
    _PortTrunkingMode_Type()
)
portTrunkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkingMode.setStatus("current")


class _PortDot1qDefaultPrioValue_Type(Integer32):
    """Custom type portDot1qDefaultPrioValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortDot1qDefaultPrioValue_Type.__name__ = "Integer32"
_PortDot1qDefaultPrioValue_Object = MibTableColumn
portDot1qDefaultPrioValue = _PortDot1qDefaultPrioValue_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 11),
    _PortDot1qDefaultPrioValue_Type()
)
portDot1qDefaultPrioValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDot1qDefaultPrioValue.setStatus("current")


class _PortDefaultPrioQueue_Type(Integer32):
    """Custom type portDefaultPrioQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PortDefaultPrioQueue_Type.__name__ = "Integer32"
_PortDefaultPrioQueue_Object = MibTableColumn
portDefaultPrioQueue = _PortDefaultPrioQueue_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 12),
    _PortDefaultPrioQueue_Type()
)
portDefaultPrioQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDefaultPrioQueue.setStatus("current")


class _PortLEDGreen_Type(Integer32):
    """Custom type portLEDGreen based on Integer32"""
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
        *(("allwaysOff", 4),
          ("allwaysOn", 5),
          ("blink", 3),
          ("notSupported", 1),
          ("showLinkSpeedDuplex", 6),
          ("showLinkState", 2))
    )


_PortLEDGreen_Type.__name__ = "Integer32"
_PortLEDGreen_Object = MibTableColumn
portLEDGreen = _PortLEDGreen_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 13),
    _PortLEDGreen_Type()
)
portLEDGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLEDGreen.setStatus("current")


class _PortLEDYellow_Type(Integer32):
    """Custom type portLEDYellow based on Integer32"""
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
        *(("allwaysOff", 4),
          ("allwaysOn", 5),
          ("blink", 3),
          ("notSupported", 1),
          ("showDuplexState", 2),
          ("showPoeEnabled", 6),
          ("showSpeed", 7))
    )


_PortLEDYellow_Type.__name__ = "Integer32"
_PortLEDYellow_Object = MibTableColumn
portLEDYellow = _PortLEDYellow_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 14),
    _PortLEDYellow_Type()
)
portLEDYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLEDYellow.setStatus("current")


class _PortBandwidthLimitRxd_Type(Integer32):
    """Custom type portBandwidthLimitRxd based on Integer32"""
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
        *(("disable", 2),
          ("limit128M", 13),
          ("limit128k", 3),
          ("limit16M", 10),
          ("limit1M", 6),
          ("limit256M", 14),
          ("limit256k", 4),
          ("limit2M", 7),
          ("limit32M", 11),
          ("limit4M", 8),
          ("limit512k", 5),
          ("limit64M", 12),
          ("limit8M", 9),
          ("notSupported", 1))
    )


_PortBandwidthLimitRxd_Type.__name__ = "Integer32"
_PortBandwidthLimitRxd_Object = MibTableColumn
portBandwidthLimitRxd = _PortBandwidthLimitRxd_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 15),
    _PortBandwidthLimitRxd_Type()
)
portBandwidthLimitRxd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBandwidthLimitRxd.setStatus("current")


class _PortBandwidthLimitTxd_Type(Integer32):
    """Custom type portBandwidthLimitTxd based on Integer32"""
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
        *(("disable", 2),
          ("limit128M", 13),
          ("limit128k", 3),
          ("limit16M", 10),
          ("limit1M", 6),
          ("limit256M", 14),
          ("limit256k", 4),
          ("limit2M", 7),
          ("limit32M", 11),
          ("limit4M", 8),
          ("limit512k", 5),
          ("limit64M", 12),
          ("limit8M", 9),
          ("notSupported", 1))
    )


_PortBandwidthLimitTxd_Type.__name__ = "Integer32"
_PortBandwidthLimitTxd_Object = MibTableColumn
portBandwidthLimitTxd = _PortBandwidthLimitTxd_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 16),
    _PortBandwidthLimitTxd_Type()
)
portBandwidthLimitTxd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBandwidthLimitTxd.setStatus("current")


class _PortSecurityAdminState_Type(Integer32):
    """Custom type portSecurityAdminState based on Integer32"""
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
        *(("autoAllowOneMacAddr", 4),
          ("autoAllowThreeMacAddr", 6),
          ("autoAllowTwoMacAddr", 5),
          ("disable", 2),
          ("ieee802AllowMultiMacAddr", 13),
          ("ieee802AllowOneMacAddr", 11),
          ("ieee802AndRadiusTwoMac", 15),
          ("ieee802OrRadiusOneMac", 14),
          ("learnOneMacAddr", 16),
          ("learnTwoMacAddr", 17),
          ("manualSettingMacAddr", 3),
          ("notSupported", 1),
          ("radiusAllowOneMacAddr", 7),
          ("radiusAllowThreeMacAddr", 9),
          ("radiusAllowTwoMacAddr", 8),
          ("renew", 10),
          ("vendorSettingMacAddr", 12))
    )


_PortSecurityAdminState_Type.__name__ = "Integer32"
_PortSecurityAdminState_Object = MibTableColumn
portSecurityAdminState = _PortSecurityAdminState_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 17),
    _PortSecurityAdminState_Type()
)
portSecurityAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityAdminState.setStatus("current")
_PortSecurityMacAddr1_Type = MacAddress
_PortSecurityMacAddr1_Object = MibTableColumn
portSecurityMacAddr1 = _PortSecurityMacAddr1_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 18),
    _PortSecurityMacAddr1_Type()
)
portSecurityMacAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacAddr1.setStatus("current")
_PortSecurityMacAddr2_Type = MacAddress
_PortSecurityMacAddr2_Object = MibTableColumn
portSecurityMacAddr2 = _PortSecurityMacAddr2_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 19),
    _PortSecurityMacAddr2_Type()
)
portSecurityMacAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacAddr2.setStatus("current")
_PortSecurityMacAddr3_Type = MacAddress
_PortSecurityMacAddr3_Object = MibTableColumn
portSecurityMacAddr3 = _PortSecurityMacAddr3_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 20),
    _PortSecurityMacAddr3_Type()
)
portSecurityMacAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacAddr3.setStatus("current")


class _PortPoeAdminState_Type(Integer32):
    """Custom type portPoeAdminState based on Integer32"""
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
        *(("afHighPower", 7),
          ("atHighPower", 8),
          ("autoOn", 4),
          ("forcedOn", 3),
          ("notSupported", 1),
          ("off", 2),
          ("overloadFail", 5),
          ("reset", 6))
    )


_PortPoeAdminState_Type.__name__ = "Integer32"
_PortPoeAdminState_Object = MibTableColumn
portPoeAdminState = _PortPoeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 21),
    _PortPoeAdminState_Type()
)
portPoeAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPoeAdminState.setStatus("current")
_PortPoeVoltage_Type = Integer32
_PortPoeVoltage_Object = MibTableColumn
portPoeVoltage = _PortPoeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 22),
    _PortPoeVoltage_Type()
)
portPoeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPoeVoltage.setStatus("current")
_PortPoeCurrent_Type = Integer32
_PortPoeCurrent_Object = MibTableColumn
portPoeCurrent = _PortPoeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 23),
    _PortPoeCurrent_Type()
)
portPoeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPoeCurrent.setStatus("current")
_PortPoePower_Type = Integer32
_PortPoePower_Object = MibTableColumn
portPoePower = _PortPoePower_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 24),
    _PortPoePower_Type()
)
portPoePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPoePower.setStatus("current")


class _PortSecurityForwardingState_Type(Integer32):
    """Custom type portSecurityForwardingState based on Integer32"""
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
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("allRadiusServersDown", 12),
          ("authFailureVLAN", 8),
          ("authenticatingClients", 10),
          ("notSupported", 1),
          ("portAdminDisabled", 2),
          ("portAuthenticated", 5),
          ("portBpduDisabled", 13),
          ("portErrorCountDisabled", 16),
          ("portLinkFlapDisabled", 15),
          ("portLoopDisabled", 7),
          ("portRedundanyLoopDisable", 18),
          ("portSecurityDisabled", 6),
          ("portSfpErrorDisabled", 17),
          ("portUdldDisabled", 14),
          ("securityWarning", 9),
          ("unsecureVLAN", 4),
          ("waitingForLink", 3),
          ("waitingForMacAddress", 11))
    )


_PortSecurityForwardingState_Type.__name__ = "Integer32"
_PortSecurityForwardingState_Object = MibTableColumn
portSecurityForwardingState = _PortSecurityForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 25),
    _PortSecurityForwardingState_Type()
)
portSecurityForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityForwardingState.setStatus("current")
_PortPoePowerLimit_Type = Integer32
_PortPoePowerLimit_Object = MibTableColumn
portPoePowerLimit = _PortPoePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 26),
    _PortPoePowerLimit_Type()
)
portPoePowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPoePowerLimit.setStatus("current")


class _PortLimiterPacketType_Type(Integer32):
    """Custom type portLimiterPacketType based on Integer32"""
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
        *(("limitAllPackets", 2),
          ("limitAllPacketsBurstsAllowed", 4),
          ("limitLoopBcastPackets", 3),
          ("notSupported", 1))
    )


_PortLimiterPacketType_Type.__name__ = "Integer32"
_PortLimiterPacketType_Object = MibTableColumn
portLimiterPacketType = _PortLimiterPacketType_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 27),
    _PortLimiterPacketType_Type()
)
portLimiterPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLimiterPacketType.setStatus("current")


class _PortAcApSetup_Type(Integer32):
    """Custom type portAcApSetup based on Integer32"""
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
        *(("allwaysEnable", 2),
          ("disable", 4),
          ("enable", 3),
          ("notSupported", 1))
    )


_PortAcApSetup_Type.__name__ = "Integer32"
_PortAcApSetup_Object = MibTableColumn
portAcApSetup = _PortAcApSetup_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 28),
    _PortAcApSetup_Type()
)
portAcApSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAcApSetup.setStatus("current")


class _PortLinkType_Type(Integer32):
    """Custom type portLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upDownlink", 3),
          ("user", 1),
          ("userWithLoopProtection", 2))
    )


_PortLinkType_Type.__name__ = "Integer32"
_PortLinkType_Object = MibTableColumn
portLinkType = _PortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 29),
    _PortLinkType_Type()
)
portLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLinkType.setStatus("current")


class _PortVoiceVlanId_Type(Integer32):
    """Custom type portVoiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PortVoiceVlanId_Type.__name__ = "Integer32"
_PortVoiceVlanId_Object = MibTableColumn
portVoiceVlanId = _PortVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 30),
    _PortVoiceVlanId_Type()
)
portVoiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVoiceVlanId.setStatus("current")


class _PortPrioDot1p_Type(Integer32):
    """Custom type portPrioDot1p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prioDot1pDisabled", 1),
          ("prioDot1pEnabled", 2))
    )


_PortPrioDot1p_Type.__name__ = "Integer32"
_PortPrioDot1p_Object = MibTableColumn
portPrioDot1p = _PortPrioDot1p_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 31),
    _PortPrioDot1p_Type()
)
portPrioDot1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPrioDot1p.setStatus("current")


class _PortPrioIp_Type(Integer32):
    """Custom type portPrioIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prioIpDisabled", 1),
          ("prioIpEnabled", 2))
    )


_PortPrioIp_Type.__name__ = "Integer32"
_PortPrioIp_Object = MibTableColumn
portPrioIp = _PortPrioIp_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 3, 1, 1, 32),
    _PortPrioIp_Type()
)
portPrioIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPrioIp.setStatus("current")
_BmSwitchVlan_ObjectIdentity = ObjectIdentity
bmSwitchVlan = _BmSwitchVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 20, 4)
)
_BmSwitchVlanTable_Object = MibTable
bmSwitchVlanTable = _BmSwitchVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 4, 1)
)
if mibBuilder.loadTexts:
    bmSwitchVlanTable.setStatus("current")
_BmSwitchVlanEntry_Object = MibTableRow
bmSwitchVlanEntry = _BmSwitchVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 4, 1, 1)
)
bmSwitchVlanEntry.setIndexNames(
    (0, "NEXANS-BM-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    bmSwitchVlanEntry.setStatus("current")


class _VlanIndex_Type(Integer32):
    """Custom type vlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VlanIndex_Type.__name__ = "Integer32"
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 4, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 4, 1, 1, 2),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")


class _VlanDescr_Type(DisplayString):
    """Custom type vlanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_VlanDescr_Type.__name__ = "DisplayString"
_VlanDescr_Object = MibTableColumn
vlanDescr = _VlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 4, 1, 1, 3),
    _VlanDescr_Type()
)
vlanDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDescr.setStatus("current")
_BmSwitchSfp_ObjectIdentity = ObjectIdentity
bmSwitchSfp = _BmSwitchSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 266, 20, 5)
)
_BmSwitchSfpTable_Object = MibTable
bmSwitchSfpTable = _BmSwitchSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1)
)
if mibBuilder.loadTexts:
    bmSwitchSfpTable.setStatus("current")
_BmSwitchSfpEntry_Object = MibTableRow
bmSwitchSfpEntry = _BmSwitchSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1)
)
bmSwitchSfpEntry.setIndexNames(
    (0, "NEXANS-BM-MIB", "sfpPortIndex"),
)
if mibBuilder.loadTexts:
    bmSwitchSfpEntry.setStatus("current")


class _SfpPortIndex_Type(Integer32):
    """Custom type sfpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SfpPortIndex_Type.__name__ = "Integer32"
_SfpPortIndex_Object = MibTableColumn
sfpPortIndex = _SfpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 1),
    _SfpPortIndex_Type()
)
sfpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPortIndex.setStatus("current")


class _SfpState_Type(Integer32):
    """Custom type sfpState based on Integer32"""
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
        *(("noSfpInserted", 2),
          ("notSupported", 1),
          ("validSfpNoDiagnostic", 3),
          ("validSfpWithDiagnostic", 4))
    )


_SfpState_Type.__name__ = "Integer32"
_SfpState_Object = MibTableColumn
sfpState = _SfpState_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 2),
    _SfpState_Type()
)
sfpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpState.setStatus("current")


class _SfpInfoVendorName_Type(DisplayString):
    """Custom type sfpInfoVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoVendorName_Type.__name__ = "DisplayString"
_SfpInfoVendorName_Object = MibTableColumn
sfpInfoVendorName = _SfpInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 3),
    _SfpInfoVendorName_Type()
)
sfpInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoVendorName.setStatus("current")


class _SfpInfoPartNumber_Type(DisplayString):
    """Custom type sfpInfoPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoPartNumber_Type.__name__ = "DisplayString"
_SfpInfoPartNumber_Object = MibTableColumn
sfpInfoPartNumber = _SfpInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 4),
    _SfpInfoPartNumber_Type()
)
sfpInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoPartNumber.setStatus("current")


class _SfpInfoRevisionNumber_Type(DisplayString):
    """Custom type sfpInfoRevisionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoRevisionNumber_Type.__name__ = "DisplayString"
_SfpInfoRevisionNumber_Object = MibTableColumn
sfpInfoRevisionNumber = _SfpInfoRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 5),
    _SfpInfoRevisionNumber_Type()
)
sfpInfoRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoRevisionNumber.setStatus("current")


class _SfpInfoSerialNumber_Type(DisplayString):
    """Custom type sfpInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoSerialNumber_Type.__name__ = "DisplayString"
_SfpInfoSerialNumber_Object = MibTableColumn
sfpInfoSerialNumber = _SfpInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 6),
    _SfpInfoSerialNumber_Type()
)
sfpInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoSerialNumber.setStatus("current")


class _SfpInfoDateCode_Type(DisplayString):
    """Custom type sfpInfoDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoDateCode_Type.__name__ = "DisplayString"
_SfpInfoDateCode_Object = MibTableColumn
sfpInfoDateCode = _SfpInfoDateCode_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 7),
    _SfpInfoDateCode_Type()
)
sfpInfoDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoDateCode.setStatus("current")


class _SfpInfoBitRate_Type(DisplayString):
    """Custom type sfpInfoBitRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoBitRate_Type.__name__ = "DisplayString"
_SfpInfoBitRate_Object = MibTableColumn
sfpInfoBitRate = _SfpInfoBitRate_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 8),
    _SfpInfoBitRate_Type()
)
sfpInfoBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoBitRate.setStatus("current")


class _SfpInfoWavelength_Type(DisplayString):
    """Custom type sfpInfoWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoWavelength_Type.__name__ = "DisplayString"
_SfpInfoWavelength_Object = MibTableColumn
sfpInfoWavelength = _SfpInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 9),
    _SfpInfoWavelength_Type()
)
sfpInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoWavelength.setStatus("current")


class _SfpInfoLength9um_Type(DisplayString):
    """Custom type sfpInfoLength9um based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoLength9um_Type.__name__ = "DisplayString"
_SfpInfoLength9um_Object = MibTableColumn
sfpInfoLength9um = _SfpInfoLength9um_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 10),
    _SfpInfoLength9um_Type()
)
sfpInfoLength9um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoLength9um.setStatus("current")


class _SfpInfoLength50um_Type(DisplayString):
    """Custom type sfpInfoLength50um based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoLength50um_Type.__name__ = "DisplayString"
_SfpInfoLength50um_Object = MibTableColumn
sfpInfoLength50um = _SfpInfoLength50um_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 11),
    _SfpInfoLength50um_Type()
)
sfpInfoLength50um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoLength50um.setStatus("current")


class _SfpInfoLength62um_Type(DisplayString):
    """Custom type sfpInfoLength62um based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoLength62um_Type.__name__ = "DisplayString"
_SfpInfoLength62um_Object = MibTableColumn
sfpInfoLength62um = _SfpInfoLength62um_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 12),
    _SfpInfoLength62um_Type()
)
sfpInfoLength62um.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoLength62um.setStatus("current")


class _SfpInfoConnectorDescr_Type(DisplayString):
    """Custom type sfpInfoConnectorDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SfpInfoConnectorDescr_Type.__name__ = "DisplayString"
_SfpInfoConnectorDescr_Object = MibTableColumn
sfpInfoConnectorDescr = _SfpInfoConnectorDescr_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 13),
    _SfpInfoConnectorDescr_Type()
)
sfpInfoConnectorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoConnectorDescr.setStatus("current")
_SfpDiagTemperature_Type = Integer32
_SfpDiagTemperature_Object = MibTableColumn
sfpDiagTemperature = _SfpDiagTemperature_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 14),
    _SfpDiagTemperature_Type()
)
sfpDiagTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagTemperature.setStatus("current")
_SfpDiagSupplyVoltage_Type = Integer32
_SfpDiagSupplyVoltage_Object = MibTableColumn
sfpDiagSupplyVoltage = _SfpDiagSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 15),
    _SfpDiagSupplyVoltage_Type()
)
sfpDiagSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagSupplyVoltage.setStatus("current")
_SfpDiagTxBiasCurrent_Type = Integer32
_SfpDiagTxBiasCurrent_Object = MibTableColumn
sfpDiagTxBiasCurrent = _SfpDiagTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 16),
    _SfpDiagTxBiasCurrent_Type()
)
sfpDiagTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagTxBiasCurrent.setStatus("current")
_SfpDiagTxOutputPower_Type = Integer32
_SfpDiagTxOutputPower_Object = MibTableColumn
sfpDiagTxOutputPower = _SfpDiagTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 17),
    _SfpDiagTxOutputPower_Type()
)
sfpDiagTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagTxOutputPower.setStatus("current")
_SfpDiagTxOutputPowerDbm_Type = Integer32
_SfpDiagTxOutputPowerDbm_Object = MibTableColumn
sfpDiagTxOutputPowerDbm = _SfpDiagTxOutputPowerDbm_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 18),
    _SfpDiagTxOutputPowerDbm_Type()
)
sfpDiagTxOutputPowerDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagTxOutputPowerDbm.setStatus("current")
_SfpDiagRxIntputPower_Type = Integer32
_SfpDiagRxIntputPower_Object = MibTableColumn
sfpDiagRxIntputPower = _SfpDiagRxIntputPower_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 19),
    _SfpDiagRxIntputPower_Type()
)
sfpDiagRxIntputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagRxIntputPower.setStatus("current")
_SfpDiagRxInputPowerDbm_Type = Integer32
_SfpDiagRxInputPowerDbm_Object = MibTableColumn
sfpDiagRxInputPowerDbm = _SfpDiagRxInputPowerDbm_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 20),
    _SfpDiagRxInputPowerDbm_Type()
)
sfpDiagRxInputPowerDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagRxInputPowerDbm.setStatus("current")
_SfpAlarmTxBiasCurrentUpperLimit_Type = Integer32
_SfpAlarmTxBiasCurrentUpperLimit_Object = MibTableColumn
sfpAlarmTxBiasCurrentUpperLimit = _SfpAlarmTxBiasCurrentUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 21),
    _SfpAlarmTxBiasCurrentUpperLimit_Type()
)
sfpAlarmTxBiasCurrentUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpAlarmTxBiasCurrentUpperLimit.setStatus("current")
_SfpAlarmTxOutputPowerLowerLimit_Type = Integer32
_SfpAlarmTxOutputPowerLowerLimit_Object = MibTableColumn
sfpAlarmTxOutputPowerLowerLimit = _SfpAlarmTxOutputPowerLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 22),
    _SfpAlarmTxOutputPowerLowerLimit_Type()
)
sfpAlarmTxOutputPowerLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpAlarmTxOutputPowerLowerLimit.setStatus("current")
_SfpAlarmRxInputPowerLowerLimit_Type = Integer32
_SfpAlarmRxInputPowerLowerLimit_Object = MibTableColumn
sfpAlarmRxInputPowerLowerLimit = _SfpAlarmRxInputPowerLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 266, 20, 5, 1, 1, 23),
    _SfpAlarmRxInputPowerLowerLimit_Type()
)
sfpAlarmRxInputPowerLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpAlarmRxInputPowerLowerLimit.setStatus("current")

# Managed Objects groups


# Notification objects

switchTemperatureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 1)
)
switchTemperatureFailure.setObjects(
    ("NEXANS-BM-MIB", "infoTemperature")
)
if mibBuilder.loadTexts:
    switchTemperatureFailure.setStatus(
        "current"
    )

portLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 2)
)
portLinkChange.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "portLinkState"))
)
if mibBuilder.loadTexts:
    portLinkChange.setStatus(
        "current"
    )

portNewMacAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 3)
)
portNewMacAddress.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "infoNewMacAddr"))
)
if mibBuilder.loadTexts:
    portNewMacAddress.setStatus(
        "current"
    )

portSecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 4)
)
portSecurityFailure.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "infoSecurityFailMacAddr"))
)
if mibBuilder.loadTexts:
    portSecurityFailure.setStatus(
        "current"
    )

portErrorCountFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 5)
)
portErrorCountFailure.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "portErrorCounter"))
)
if mibBuilder.loadTexts:
    portErrorCountFailure.setStatus(
        "current"
    )

switchMgmtAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 6)
)
switchMgmtAuthFailure.setObjects(
    ("NEXANS-BM-MIB", "infoUnauthIpAddr")
)
if mibBuilder.loadTexts:
    switchMgmtAuthFailure.setStatus(
        "current"
    )

radiusMgmtAuthReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 7)
)
radiusMgmtAuthReject.setObjects(
    ("NEXANS-BM-MIB", "infoUnauthIpAddr")
)
if mibBuilder.loadTexts:
    radiusMgmtAuthReject.setStatus(
        "current"
    )

radiusPortSecurityReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 8)
)
radiusPortSecurityReject.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "infoSecurityFailMacAddr"))
)
if mibBuilder.loadTexts:
    radiusPortSecurityReject.setStatus(
        "current"
    )

portLoopBcastFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 9)
)
portLoopBcastFailure.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    portLoopBcastFailure.setStatus(
        "current"
    )

switchPoeVoltageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 10)
)
switchPoeVoltageFailure.setObjects(
    ("NEXANS-BM-MIB", "infoPoeInputVoltage")
)
if mibBuilder.loadTexts:
    switchPoeVoltageFailure.setStatus(
        "current"
    )

switchPoeOverloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 11)
)
switchPoeOverloadFailure.setObjects(
    ("NEXANS-BM-MIB", "infoPoeInputPower")
)
if mibBuilder.loadTexts:
    switchPoeOverloadFailure.setStatus(
        "current"
    )

portPoeOverloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 12)
)
portPoeOverloadFailure.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "portPoePower"))
)
if mibBuilder.loadTexts:
    portPoeOverloadFailure.setStatus(
        "current"
    )

portActiveLoopDetectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 13)
)
portActiveLoopDetectionFailure.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    portActiveLoopDetectionFailure.setStatus(
        "current"
    )

switchIndustrialAlarmM1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 14)
)
switchIndustrialAlarmM1.setObjects(
      *(("NEXANS-BM-MIB", "infoAlarmStateM1"),
        ("NEXANS-BM-MIB", "adminAlarmNameM1"))
)
if mibBuilder.loadTexts:
    switchIndustrialAlarmM1.setStatus(
        "current"
    )

switchIndustrialAlarmM2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 15)
)
switchIndustrialAlarmM2.setObjects(
      *(("NEXANS-BM-MIB", "infoAlarmStateM2"),
        ("NEXANS-BM-MIB", "adminAlarmNameM2"))
)
if mibBuilder.loadTexts:
    switchIndustrialAlarmM2.setStatus(
        "current"
    )

switchInternalVoltageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 16)
)
switchInternalVoltageFailure.setObjects(
      *(("NEXANS-BM-MIB", "infoPowerVoltage2500"),
        ("NEXANS-BM-MIB", "infoPowerVoltage3300"))
)
if mibBuilder.loadTexts:
    switchInternalVoltageFailure.setStatus(
        "current"
    )

tftpMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 17)
)
tftpMessage.setObjects(
    ("NEXANS-BM-MIB", "infoLastTftpMessage")
)
if mibBuilder.loadTexts:
    tftpMessage.setStatus(
        "current"
    )

sfpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 18)
)
sfpEvent.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "infoLastSfpEventMessage"))
)
if mibBuilder.loadTexts:
    sfpEvent.setStatus(
        "current"
    )

clientRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 19)
)
clientRemoved.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    clientRemoved.setStatus(
        "current"
    )

internalMgmtWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 20)
)
internalMgmtWarning.setObjects(
    ("NEXANS-BM-MIB", "infoLastInternalMgmtWarning")
)
if mibBuilder.loadTexts:
    internalMgmtWarning.setStatus(
        "current"
    )

switchFunctionInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 21)
)
switchFunctionInputAlarm.setObjects(
      *(("NEXANS-BM-MIB", "infoFunctionInputStateF1"),
        ("NEXANS-BM-MIB", "adminFunctionInputNameF1"))
)
if mibBuilder.loadTexts:
    switchFunctionInputAlarm.setStatus(
        "current"
    )

switchConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 22)
)
switchConfigurationChanged.setObjects(
    ("NEXANS-BM-MIB", "infoTotalConfigChanges")
)
if mibBuilder.loadTexts:
    switchConfigurationChanged.setStatus(
        "current"
    )

portErrorDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 266, 20, 0, 23)
)
portErrorDisabled.setObjects(
      *(("NEXANS-BM-MIB", "portIndex"),
        ("NEXANS-BM-MIB", "portDescr"),
        ("NEXANS-BM-MIB", "portName"),
        ("NEXANS-BM-MIB", "portAdminState"))
)
if mibBuilder.loadTexts:
    portErrorDisabled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEXANS-BM-MIB",
    **{"bmSwitchMIB": bmSwitchMIB,
       "bmTraps": bmTraps,
       "switchTemperatureFailure": switchTemperatureFailure,
       "portLinkChange": portLinkChange,
       "portNewMacAddress": portNewMacAddress,
       "portSecurityFailure": portSecurityFailure,
       "portErrorCountFailure": portErrorCountFailure,
       "switchMgmtAuthFailure": switchMgmtAuthFailure,
       "radiusMgmtAuthReject": radiusMgmtAuthReject,
       "radiusPortSecurityReject": radiusPortSecurityReject,
       "portLoopBcastFailure": portLoopBcastFailure,
       "switchPoeVoltageFailure": switchPoeVoltageFailure,
       "switchPoeOverloadFailure": switchPoeOverloadFailure,
       "portPoeOverloadFailure": portPoeOverloadFailure,
       "portActiveLoopDetectionFailure": portActiveLoopDetectionFailure,
       "switchIndustrialAlarmM1": switchIndustrialAlarmM1,
       "switchIndustrialAlarmM2": switchIndustrialAlarmM2,
       "switchInternalVoltageFailure": switchInternalVoltageFailure,
       "tftpMessage": tftpMessage,
       "sfpEvent": sfpEvent,
       "clientRemoved": clientRemoved,
       "internalMgmtWarning": internalMgmtWarning,
       "switchFunctionInputAlarm": switchFunctionInputAlarm,
       "switchConfigurationChanged": switchConfigurationChanged,
       "portErrorDisabled": portErrorDisabled,
       "bmSwitchInfo": bmSwitchInfo,
       "infoDescr": infoDescr,
       "infoType": infoType,
       "infoProductNo": infoProductNo,
       "infoSerie": infoSerie,
       "infoSeriesNo": infoSeriesNo,
       "infoManufactureDate": infoManufactureDate,
       "infoSwitchHardwareVersion": infoSwitchHardwareVersion,
       "infoMgmtHardwareVersion": infoMgmtHardwareVersion,
       "infoMgmtFirmwareVersion": infoMgmtFirmwareVersion,
       "infoNoOfPorts": infoNoOfPorts,
       "infoNoOfReboots": infoNoOfReboots,
       "infoTemperature": infoTemperature,
       "infoTemperatureMaxAllowed": infoTemperatureMaxAllowed,
       "infoPowerVoltage2500": infoPowerVoltage2500,
       "infoPowerVoltage3300": infoPowerVoltage3300,
       "infoUnauthIpAddr": infoUnauthIpAddr,
       "infoSecurityFailMacAddr": infoSecurityFailMacAddr,
       "infoNewMacAddr": infoNewMacAddr,
       "infoPoeInputVoltage": infoPoeInputVoltage,
       "infoPoeInputPower": infoPoeInputPower,
       "infoAlarmStateM1": infoAlarmStateM1,
       "infoAlarmStateM2": infoAlarmStateM2,
       "infoLastTftpMessage": infoLastTftpMessage,
       "infoLastSfpEventMessage": infoLastSfpEventMessage,
       "infoLastInternalMgmtWarning": infoLastInternalMgmtWarning,
       "infoFunctionInputStateF1": infoFunctionInputStateF1,
       "infoTotalConfigChanges": infoTotalConfigChanges,
       "bmSwitchAdmin": bmSwitchAdmin,
       "adminReset": adminReset,
       "adminAgentDhcp": adminAgentDhcp,
       "adminAgentIpAddress": adminAgentIpAddress,
       "adminAgentPhysAddress": adminAgentPhysAddress,
       "adminAgentDefRouterIpAddress": adminAgentDefRouterIpAddress,
       "adminAgentNetmask": adminAgentNetmask,
       "adminAgentDhcpServerIpAddress": adminAgentDhcpServerIpAddress,
       "adminAgentVlanId": adminAgentVlanId,
       "adminAgentPrioValue": adminAgentPrioValue,
       "adminAddrAgingTimeMinutes": adminAddrAgingTimeMinutes,
       "adminSwitchPortMirror": adminSwitchPortMirror,
       "adminMgmtAccessList": adminMgmtAccessList,
       "adminSwitchPoEPowerLimit": adminSwitchPoEPowerLimit,
       "adminSwitchVlanTableMode": adminSwitchVlanTableMode,
       "adminUnsecureVlanId": adminUnsecureVlanId,
       "adminDot1xAuthFailureVlanId": adminDot1xAuthFailureVlanId,
       "adminTftpAccess": adminTftpAccess,
       "adminSnmpMacTableMode": adminSnmpMacTableMode,
       "adminAlarmM1": adminAlarmM1,
       "adminAlarmM2": adminAlarmM2,
       "adminMemoryCardMode": adminMemoryCardMode,
       "adminAlarmNameM1": adminAlarmNameM1,
       "adminAlarmNameM2": adminAlarmNameM2,
       "adminFunctionInputNameF1": adminFunctionInputNameF1,
       "adminLedGlobalMode": adminLedGlobalMode,
       "bmSwitchPort": bmSwitchPort,
       "bmSwitchPortTable": bmSwitchPortTable,
       "bmSwitchPortEntry": bmSwitchPortEntry,
       "portIndex": portIndex,
       "portDescr": portDescr,
       "portName": portName,
       "portAdminState": portAdminState,
       "portSpeedDuplexSetup": portSpeedDuplexSetup,
       "portLinkState": portLinkState,
       "portErrorCounter": portErrorCounter,
       "portRemoteFault": portRemoteFault,
       "portDefaultVlanId": portDefaultVlanId,
       "portTrunkingMode": portTrunkingMode,
       "portDot1qDefaultPrioValue": portDot1qDefaultPrioValue,
       "portDefaultPrioQueue": portDefaultPrioQueue,
       "portLEDGreen": portLEDGreen,
       "portLEDYellow": portLEDYellow,
       "portBandwidthLimitRxd": portBandwidthLimitRxd,
       "portBandwidthLimitTxd": portBandwidthLimitTxd,
       "portSecurityAdminState": portSecurityAdminState,
       "portSecurityMacAddr1": portSecurityMacAddr1,
       "portSecurityMacAddr2": portSecurityMacAddr2,
       "portSecurityMacAddr3": portSecurityMacAddr3,
       "portPoeAdminState": portPoeAdminState,
       "portPoeVoltage": portPoeVoltage,
       "portPoeCurrent": portPoeCurrent,
       "portPoePower": portPoePower,
       "portSecurityForwardingState": portSecurityForwardingState,
       "portPoePowerLimit": portPoePowerLimit,
       "portLimiterPacketType": portLimiterPacketType,
       "portAcApSetup": portAcApSetup,
       "portLinkType": portLinkType,
       "portVoiceVlanId": portVoiceVlanId,
       "portPrioDot1p": portPrioDot1p,
       "portPrioIp": portPrioIp,
       "bmSwitchVlan": bmSwitchVlan,
       "bmSwitchVlanTable": bmSwitchVlanTable,
       "bmSwitchVlanEntry": bmSwitchVlanEntry,
       "vlanIndex": vlanIndex,
       "vlanId": vlanId,
       "vlanDescr": vlanDescr,
       "bmSwitchSfp": bmSwitchSfp,
       "bmSwitchSfpTable": bmSwitchSfpTable,
       "bmSwitchSfpEntry": bmSwitchSfpEntry,
       "sfpPortIndex": sfpPortIndex,
       "sfpState": sfpState,
       "sfpInfoVendorName": sfpInfoVendorName,
       "sfpInfoPartNumber": sfpInfoPartNumber,
       "sfpInfoRevisionNumber": sfpInfoRevisionNumber,
       "sfpInfoSerialNumber": sfpInfoSerialNumber,
       "sfpInfoDateCode": sfpInfoDateCode,
       "sfpInfoBitRate": sfpInfoBitRate,
       "sfpInfoWavelength": sfpInfoWavelength,
       "sfpInfoLength9um": sfpInfoLength9um,
       "sfpInfoLength50um": sfpInfoLength50um,
       "sfpInfoLength62um": sfpInfoLength62um,
       "sfpInfoConnectorDescr": sfpInfoConnectorDescr,
       "sfpDiagTemperature": sfpDiagTemperature,
       "sfpDiagSupplyVoltage": sfpDiagSupplyVoltage,
       "sfpDiagTxBiasCurrent": sfpDiagTxBiasCurrent,
       "sfpDiagTxOutputPower": sfpDiagTxOutputPower,
       "sfpDiagTxOutputPowerDbm": sfpDiagTxOutputPowerDbm,
       "sfpDiagRxIntputPower": sfpDiagRxIntputPower,
       "sfpDiagRxInputPowerDbm": sfpDiagRxInputPowerDbm,
       "sfpAlarmTxBiasCurrentUpperLimit": sfpAlarmTxBiasCurrentUpperLimit,
       "sfpAlarmTxOutputPowerLowerLimit": sfpAlarmTxOutputPowerLowerLimit,
       "sfpAlarmRxInputPowerLowerLimit": sfpAlarmRxInputPowerLowerLimit}
)
