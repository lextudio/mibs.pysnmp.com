# SNMP MIB module (HUAWEI-WLAN-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:39 2024
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

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

(hwStaAccessChannel,
 hwStaIp,
 hwStaNoise,
 hwStaReSendBytes,
 hwStaReSendFrames,
 hwStaRecvDropFrames,
 hwStaRecvErrorFrames,
 hwStaRssi,
 hwStaSendDropFrames,
 hwStaSendErrorFrames,
 hwStaUsername,
 hwStaVlan,
 hwStaWirelessStatRxBytes,
 hwStaWirelessStatRxPkts,
 hwStaWirelessStatRxRate,
 hwStaWirelessStatTxBytes,
 hwStaWirelessStatTxPkts,
 hwStaWirelessStatTxRate,
 hwWlanServiceStaApId,
 hwWlanServiceStaEssName,
 hwWlanServiceStaMac,
 hwWlanServiceStaOnlineTime,
 hwWlanServiceStaRadioId,
 hwWlanServiceStaRxPowerUs,
 hwWlanServiceStaSnrUs,
 hwWlanServiceStaSsid) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-SERVICE-MIB",
    "hwStaAccessChannel",
    "hwStaIp",
    "hwStaNoise",
    "hwStaReSendBytes",
    "hwStaReSendFrames",
    "hwStaRecvDropFrames",
    "hwStaRecvErrorFrames",
    "hwStaRssi",
    "hwStaSendDropFrames",
    "hwStaSendErrorFrames",
    "hwStaUsername",
    "hwStaVlan",
    "hwStaWirelessStatRxBytes",
    "hwStaWirelessStatRxPkts",
    "hwStaWirelessStatRxRate",
    "hwStaWirelessStatTxBytes",
    "hwStaWirelessStatTxPkts",
    "hwStaWirelessStatTxRate",
    "hwWlanServiceStaApId",
    "hwWlanServiceStaEssName",
    "hwWlanServiceStaMac",
    "hwWlanServiceStaOnlineTime",
    "hwWlanServiceStaRadioId",
    "hwWlanServiceStaRxPowerUs",
    "hwWlanServiceStaSnrUs",
    "hwWlanServiceStaSsid")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwWlanDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2)
)
hwWlanDevice.setRevisions(
        ("2015-06-18 20:10",
         "2015-01-20 20:10",
         "2014-12-16 10:10",
         "2014-11-20 09:10",
         "2014-09-01 09:45",
         "2014-07-03 15:51",
         "2014-06-16 15:31",
         "2014-06-04 11:51",
         "2014-04-24 20:18",
         "2014-03-21 16:28",
         "2013-12-04 09:56",
         "2013-10-26 10:56",
         "2013-09-02 00:00",
         "2010-11-04 00:00",
         "2010-09-10 00:00",
         "2010-08-13 00:00",
         "2010-07-07 00:00",
         "2010-05-25 10:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwWlanDeviceNotifications_ObjectIdentity = ObjectIdentity
hwWlanDeviceNotifications = _HwWlanDeviceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1)
)
_HwWlanDeviceNotify_ObjectIdentity = ObjectIdentity
hwWlanDeviceNotify = _HwWlanDeviceNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1)
)
_HwWlanDeviceNotifyObjects_ObjectIdentity = ObjectIdentity
hwWlanDeviceNotifyObjects = _HwWlanDeviceNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2)
)
_HwApActualType_Type = OctetString
_HwApActualType_Object = MibScalar
hwApActualType = _HwApActualType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 1),
    _HwApActualType_Type()
)
hwApActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApActualType.setStatus("current")
_HwApCpuOccupancyRate_Type = Integer32
_HwApCpuOccupancyRate_Object = MibScalar
hwApCpuOccupancyRate = _HwApCpuOccupancyRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 2),
    _HwApCpuOccupancyRate_Type()
)
hwApCpuOccupancyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApCpuOccupancyRate.setStatus("current")
_HwApMemoryOccupancyRate_Type = Integer32
_HwApMemoryOccupancyRate_Object = MibScalar
hwApMemoryOccupancyRate = _HwApMemoryOccupancyRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 3),
    _HwApMemoryOccupancyRate_Type()
)
hwApMemoryOccupancyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMemoryOccupancyRate.setStatus("current")
_HwApPermitStaNum_Type = Integer32
_HwApPermitStaNum_Object = MibScalar
hwApPermitStaNum = _HwApPermitStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 4),
    _HwApPermitStaNum_Type()
)
hwApPermitStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPermitStaNum.setStatus("current")
_HwStaAuthFailCause_Type = Integer32
_HwStaAuthFailCause_Object = MibScalar
hwStaAuthFailCause = _HwStaAuthFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 5),
    _HwStaAuthFailCause_Type()
)
hwStaAuthFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthFailCause.setStatus("current")
_HwAcSystemSwitchType_Type = Integer32
_HwAcSystemSwitchType_Object = MibScalar
hwAcSystemSwitchType = _HwAcSystemSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 6),
    _HwAcSystemSwitchType_Type()
)
hwAcSystemSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcSystemSwitchType.setStatus("current")
_HwApRadioNotifyPara_Type = Integer32
_HwApRadioNotifyPara_Object = MibScalar
hwApRadioNotifyPara = _HwApRadioNotifyPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 8),
    _HwApRadioNotifyPara_Type()
)
hwApRadioNotifyPara.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRadioNotifyPara.setStatus("current")
_HwApOpticalRxPower_Type = Integer32
_HwApOpticalRxPower_Object = MibScalar
hwApOpticalRxPower = _HwApOpticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 9),
    _HwApOpticalRxPower_Type()
)
hwApOpticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalRxPower.setStatus("current")
_HwApOpticalTemperature_Type = Integer32
_HwApOpticalTemperature_Object = MibScalar
hwApOpticalTemperature = _HwApOpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 10),
    _HwApOpticalTemperature_Type()
)
hwApOpticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalTemperature.setStatus("current")
_HwApCfgCountryCode_Type = OctetString
_HwApCfgCountryCode_Object = MibScalar
hwApCfgCountryCode = _HwApCfgCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 11),
    _HwApCfgCountryCode_Type()
)
hwApCfgCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApCfgCountryCode.setStatus("current")
_HwApArpAttackSrcMac_Type = MacAddress
_HwApArpAttackSrcMac_Object = MibScalar
hwApArpAttackSrcMac = _HwApArpAttackSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 12),
    _HwApArpAttackSrcMac_Type()
)
hwApArpAttackSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApArpAttackSrcMac.setStatus("current")
_HwApArpAttackDstMac_Type = MacAddress
_HwApArpAttackDstMac_Object = MibScalar
hwApArpAttackDstMac = _HwApArpAttackDstMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 13),
    _HwApArpAttackDstMac_Type()
)
hwApArpAttackDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApArpAttackDstMac.setStatus("current")
_HwApArpAttackSrcIP_Type = IpAddress
_HwApArpAttackSrcIP_Object = MibScalar
hwApArpAttackSrcIP = _HwApArpAttackSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 14),
    _HwApArpAttackSrcIP_Type()
)
hwApArpAttackSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApArpAttackSrcIP.setStatus("current")
_HwApArpCfgRateThreshold_Type = Integer32
_HwApArpCfgRateThreshold_Object = MibScalar
hwApArpCfgRateThreshold = _HwApArpCfgRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 15),
    _HwApArpCfgRateThreshold_Type()
)
hwApArpCfgRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApArpCfgRateThreshold.setStatus("current")
_HwApArpActualRate_Type = Integer32
_HwApArpActualRate_Object = MibScalar
hwApArpActualRate = _HwApArpActualRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 16),
    _HwApArpActualRate_Type()
)
hwApArpActualRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApArpActualRate.setStatus("current")
_HwApNotifyRadioId_Type = Integer32
_HwApNotifyRadioId_Object = MibScalar
hwApNotifyRadioId = _HwApNotifyRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 17),
    _HwApNotifyRadioId_Type()
)
hwApNotifyRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApNotifyRadioId.setStatus("current")
_HwApNotifyOrRestoreTemperature_Type = Integer32
_HwApNotifyOrRestoreTemperature_Object = MibScalar
hwApNotifyOrRestoreTemperature = _HwApNotifyOrRestoreTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 18),
    _HwApNotifyOrRestoreTemperature_Type()
)
hwApNotifyOrRestoreTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApNotifyOrRestoreTemperature.setStatus("current")
_HwOccurTime_Type = OctetString
_HwOccurTime_Object = MibScalar
hwOccurTime = _HwOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 19),
    _HwOccurTime_Type()
)
hwOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOccurTime.setStatus("current")
_HwApBootNotifyName_Type = OctetString
_HwApBootNotifyName_Object = MibScalar
hwApBootNotifyName = _HwApBootNotifyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 20),
    _HwApBootNotifyName_Type()
)
hwApBootNotifyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApBootNotifyName.setStatus("current")
_HwApFaultTimes_Type = Integer32
_HwApFaultTimes_Object = MibScalar
hwApFaultTimes = _HwApFaultTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 21),
    _HwApFaultTimes_Type()
)
hwApFaultTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApFaultTimes.setStatus("current")
_HwSignalStrengthThreshold_Type = Integer32
_HwSignalStrengthThreshold_Object = MibScalar
hwSignalStrengthThreshold = _HwSignalStrengthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 22),
    _HwSignalStrengthThreshold_Type()
)
hwSignalStrengthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSignalStrengthThreshold.setStatus("current")
_HwStaBroadcastFlux_Type = Unsigned32
_HwStaBroadcastFlux_Object = MibScalar
hwStaBroadcastFlux = _HwStaBroadcastFlux_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 23),
    _HwStaBroadcastFlux_Type()
)
hwStaBroadcastFlux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaBroadcastFlux.setStatus("current")
_HwBroadcastWarnThresholdDown_Type = Unsigned32
_HwBroadcastWarnThresholdDown_Object = MibScalar
hwBroadcastWarnThresholdDown = _HwBroadcastWarnThresholdDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 24),
    _HwBroadcastWarnThresholdDown_Type()
)
hwBroadcastWarnThresholdDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBroadcastWarnThresholdDown.setStatus("current")
_HwBroadcastWarnThresholdUp_Type = Unsigned32
_HwBroadcastWarnThresholdUp_Object = MibScalar
hwBroadcastWarnThresholdUp = _HwBroadcastWarnThresholdUp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 25),
    _HwBroadcastWarnThresholdUp_Type()
)
hwBroadcastWarnThresholdUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBroadcastWarnThresholdUp.setStatus("current")
_HwBroadcastRestrainThresholdDown_Type = Unsigned32
_HwBroadcastRestrainThresholdDown_Object = MibScalar
hwBroadcastRestrainThresholdDown = _HwBroadcastRestrainThresholdDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 26),
    _HwBroadcastRestrainThresholdDown_Type()
)
hwBroadcastRestrainThresholdDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBroadcastRestrainThresholdDown.setStatus("current")
_HwBroadcastRestrainThresholdUp_Type = Unsigned32
_HwBroadcastRestrainThresholdUp_Object = MibScalar
hwBroadcastRestrainThresholdUp = _HwBroadcastRestrainThresholdUp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 27),
    _HwBroadcastRestrainThresholdUp_Type()
)
hwBroadcastRestrainThresholdUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBroadcastRestrainThresholdUp.setStatus("current")
_HwApBroadcastFlux_Type = Integer32
_HwApBroadcastFlux_Object = MibScalar
hwApBroadcastFlux = _HwApBroadcastFlux_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 28),
    _HwApBroadcastFlux_Type()
)
hwApBroadcastFlux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApBroadcastFlux.setStatus("current")
_HwCrcErrActual_Type = Unsigned32
_HwCrcErrActual_Object = MibScalar
hwCrcErrActual = _HwCrcErrActual_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 29),
    _HwCrcErrActual_Type()
)
hwCrcErrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCrcErrActual.setStatus("current")
_HwCrcThreshold_Type = Unsigned32
_HwCrcThreshold_Object = MibScalar
hwCrcThreshold = _HwCrcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 30),
    _HwCrcThreshold_Type()
)
hwCrcThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCrcThreshold.setStatus("current")
_HwApNotifyWlanId_Type = Integer32
_HwApNotifyWlanId_Object = MibScalar
hwApNotifyWlanId = _HwApNotifyWlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 31),
    _HwApNotifyWlanId_Type()
)
hwApNotifyWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApNotifyWlanId.setStatus("current")
_HwApLicenseInfo_Type = OctetString
_HwApLicenseInfo_Object = MibScalar
hwApLicenseInfo = _HwApLicenseInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 32),
    _HwApLicenseInfo_Type()
)
hwApLicenseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLicenseInfo.setStatus("current")
_HwCrcPortType_Type = OctetString
_HwCrcPortType_Object = MibScalar
hwCrcPortType = _HwCrcPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 33),
    _HwCrcPortType_Type()
)
hwCrcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCrcPortType.setStatus("current")
_HwCrcPortID_Type = Integer32
_HwCrcPortID_Object = MibScalar
hwCrcPortID = _HwCrcPortID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 34),
    _HwCrcPortID_Type()
)
hwCrcPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCrcPortID.setStatus("current")
_HwApArpAttackDropNum_Type = Integer32
_HwApArpAttackDropNum_Object = MibScalar
hwApArpAttackDropNum = _HwApArpAttackDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 35),
    _HwApArpAttackDropNum_Type()
)
hwApArpAttackDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApArpAttackDropNum.setStatus("current")


class _HwApFaultID_Type(Integer32):
    """Custom type hwApFaultID based on Integer32"""
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
        *(("cpld", 2),
          ("lm75", 3),
          ("phy", 1),
          ("sfp", 4),
          ("wifi", 5))
    )


_HwApFaultID_Type.__name__ = "Integer32"
_HwApFaultID_Object = MibScalar
hwApFaultID = _HwApFaultID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 36),
    _HwApFaultID_Type()
)
hwApFaultID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApFaultID.setStatus("current")
_HwApIfIndex_Type = Integer32
_HwApIfIndex_Object = MibScalar
hwApIfIndex = _HwApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 37),
    _HwApIfIndex_Type()
)
hwApIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApIfIndex.setStatus("current")
_HwApFaultInfo_Type = OctetString
_HwApFaultInfo_Object = MibScalar
hwApFaultInfo = _HwApFaultInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 2, 38),
    _HwApFaultInfo_Type()
)
hwApFaultInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApFaultInfo.setStatus("current")
_HwApTypeObjects_ObjectIdentity = ObjectIdentity
hwApTypeObjects = _HwApTypeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2)
)
_HwApTypeTable_Object = MibTable
hwApTypeTable = _HwApTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwApTypeTable.setStatus("current")
_HwApTypeEntry_Object = MibTableRow
hwApTypeEntry = _HwApTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1)
)
hwApTypeEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
)
if mibBuilder.loadTexts:
    hwApTypeEntry.setStatus("current")
_HwApType_Type = OctetString
_HwApType_Object = MibTableColumn
hwApType = _HwApType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 1),
    _HwApType_Type()
)
hwApType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwApType.setStatus("current")
_HwApTypeDesc_Type = OctetString
_HwApTypeDesc_Object = MibTableColumn
hwApTypeDesc = _HwApTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 2),
    _HwApTypeDesc_Type()
)
hwApTypeDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeDesc.setStatus("current")
_HwApTypeLineatePortNum_Type = Integer32
_HwApTypeLineatePortNum_Object = MibTableColumn
hwApTypeLineatePortNum = _HwApTypeLineatePortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 3),
    _HwApTypeLineatePortNum_Type()
)
hwApTypeLineatePortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeLineatePortNum.setStatus("current")
_HwApTypeRadioNum_Type = Integer32
_HwApTypeRadioNum_Object = MibTableColumn
hwApTypeRadioNum = _HwApTypeRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 4),
    _HwApTypeRadioNum_Type()
)
hwApTypeRadioNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeRadioNum.setStatus("current")
_HwApTypeMaxStaNum_Type = Integer32
_HwApTypeMaxStaNum_Object = MibTableColumn
hwApTypeMaxStaNum = _HwApTypeMaxStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 5),
    _HwApTypeMaxStaNum_Type()
)
hwApTypeMaxStaNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeMaxStaNum.setStatus("current")
_HwApTypeMaxSsidNum_Type = Integer32
_HwApTypeMaxSsidNum_Object = MibTableColumn
hwApTypeMaxSsidNum = _HwApTypeMaxSsidNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 6),
    _HwApTypeMaxSsidNum_Type()
)
hwApTypeMaxSsidNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeMaxSsidNum.setStatus("current")
_HwApTypeAntennaGain_Type = Integer32
_HwApTypeAntennaGain_Object = MibTableColumn
hwApTypeAntennaGain = _HwApTypeAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 7),
    _HwApTypeAntennaGain_Type()
)
hwApTypeAntennaGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    hwApTypeAntennaGain.setUnits("dBi")
_HwApTypeRowStatus_Type = RowStatus
_HwApTypeRowStatus_Object = MibTableColumn
hwApTypeRowStatus = _HwApTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 8),
    _HwApTypeRowStatus_Type()
)
hwApTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApTypeRowStatus.setStatus("current")
_HwApTypeReset_Type = Integer32
_HwApTypeReset_Object = MibTableColumn
hwApTypeReset = _HwApTypeReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 1, 1, 9),
    _HwApTypeReset_Type()
)
hwApTypeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApTypeReset.setStatus("current")
_HwApTypeRadioTable_Object = MibTable
hwApTypeRadioTable = _HwApTypeRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwApTypeRadioTable.setStatus("current")
_HwApTypeRadioEntry_Object = MibTableRow
hwApTypeRadioEntry = _HwApTypeRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3, 1)
)
hwApTypeRadioEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApTypeRadioIndex"),
)
if mibBuilder.loadTexts:
    hwApTypeRadioEntry.setStatus("current")
_HwApTypeRadioIndex_Type = Integer32
_HwApTypeRadioIndex_Object = MibTableColumn
hwApTypeRadioIndex = _HwApTypeRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3, 1, 1),
    _HwApTypeRadioIndex_Type()
)
hwApTypeRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApTypeRadioIndex.setStatus("current")


class _HwApTypeRadioType_Type(Integer32):
    """Custom type hwApTypeRadioType based on Integer32"""
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
        *(("wlan80211a", 1),
          ("wlan80211an", 5),
          ("wlan80211b", 2),
          ("wlan80211bg", 4),
          ("wlan80211bgn", 6),
          ("wlan80211g", 3))
    )


_HwApTypeRadioType_Type.__name__ = "Integer32"
_HwApTypeRadioType_Object = MibTableColumn
hwApTypeRadioType = _HwApTypeRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3, 1, 2),
    _HwApTypeRadioType_Type()
)
hwApTypeRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApTypeRadioType.setStatus("current")


class _HwRadioMaxSpatialStreamsNum_Type(Unsigned32):
    """Custom type hwRadioMaxSpatialStreamsNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwRadioMaxSpatialStreamsNum_Type.__name__ = "Unsigned32"
_HwRadioMaxSpatialStreamsNum_Object = MibTableColumn
hwRadioMaxSpatialStreamsNum = _HwRadioMaxSpatialStreamsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3, 1, 3),
    _HwRadioMaxSpatialStreamsNum_Type()
)
hwRadioMaxSpatialStreamsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMaxSpatialStreamsNum.setStatus("current")


class _HwRadioMaxAntennasNum_Type(Unsigned32):
    """Custom type hwRadioMaxAntennasNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwRadioMaxAntennasNum_Type.__name__ = "Unsigned32"
_HwRadioMaxAntennasNum_Object = MibTableColumn
hwRadioMaxAntennasNum = _HwRadioMaxAntennasNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3, 1, 4),
    _HwRadioMaxAntennasNum_Type()
)
hwRadioMaxAntennasNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMaxAntennasNum.setStatus("current")


class _HwRadioMaxVAPNum_Type(Unsigned32):
    """Custom type hwRadioMaxVAPNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwRadioMaxVAPNum_Type.__name__ = "Unsigned32"
_HwRadioMaxVAPNum_Object = MibTableColumn
hwRadioMaxVAPNum = _HwRadioMaxVAPNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3, 1, 5),
    _HwRadioMaxVAPNum_Type()
)
hwRadioMaxVAPNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadioMaxVAPNum.setStatus("current")


class _HwApTypeRadioAntennaGain_Type(Integer32):
    """Custom type hwApTypeRadioAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_HwApTypeRadioAntennaGain_Type.__name__ = "Integer32"
_HwApTypeRadioAntennaGain_Object = MibTableColumn
hwApTypeRadioAntennaGain = _HwApTypeRadioAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 3, 1, 6),
    _HwApTypeRadioAntennaGain_Type()
)
hwApTypeRadioAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApTypeRadioAntennaGain.setStatus("current")
_HwApTypeLineatePortInfoTable_Object = MibTable
hwApTypeLineatePortInfoTable = _HwApTypeLineatePortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hwApTypeLineatePortInfoTable.setStatus("current")
_HwApTypeLineatePortInfoEntry_Object = MibTableRow
hwApTypeLineatePortInfoEntry = _HwApTypeLineatePortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 4, 1)
)
hwApTypeLineatePortInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApTypeLineatePortIndex"),
)
if mibBuilder.loadTexts:
    hwApTypeLineatePortInfoEntry.setStatus("current")
_HwApTypeLineatePortIndex_Type = Integer32
_HwApTypeLineatePortIndex_Object = MibTableColumn
hwApTypeLineatePortIndex = _HwApTypeLineatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 4, 1, 1),
    _HwApTypeLineatePortIndex_Type()
)
hwApTypeLineatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApTypeLineatePortIndex.setStatus("current")


class _HwApTypeLineatePortType_Type(Integer32):
    """Custom type hwApTypeLineatePortType based on Integer32"""
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
        *(("adsl2plus", 5),
          ("epon", 4),
          ("fe", 1),
          ("ge", 2),
          ("gpon", 3))
    )


_HwApTypeLineatePortType_Type.__name__ = "Integer32"
_HwApTypeLineatePortType_Object = MibTableColumn
hwApTypeLineatePortType = _HwApTypeLineatePortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 4, 1, 2),
    _HwApTypeLineatePortType_Type()
)
hwApTypeLineatePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApTypeLineatePortType.setStatus("current")
_HwApTypeLineatePortName_Type = OctetString
_HwApTypeLineatePortName_Object = MibTableColumn
hwApTypeLineatePortName = _HwApTypeLineatePortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 2, 4, 1, 3),
    _HwApTypeLineatePortName_Type()
)
hwApTypeLineatePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApTypeLineatePortName.setStatus("current")
_HwApProfileObjects_ObjectIdentity = ObjectIdentity
hwApProfileObjects = _HwApProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3)
)
_HwApProfileTable_Object = MibTable
hwApProfileTable = _HwApProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hwApProfileTable.setStatus("current")
_HwApProfileEntry_Object = MibTableRow
hwApProfileEntry = _HwApProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1)
)
hwApProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApProfileName"),
)
if mibBuilder.loadTexts:
    hwApProfileEntry.setStatus("current")
_HwApProfileName_Type = OctetString
_HwApProfileName_Object = MibTableColumn
hwApProfileName = _HwApProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 1),
    _HwApProfileName_Type()
)
hwApProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApProfileName.setStatus("current")
_HwApEthPortMtu_Type = Integer32
_HwApEthPortMtu_Object = MibTableColumn
hwApEthPortMtu = _HwApEthPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 2),
    _HwApEthPortMtu_Type()
)
hwApEthPortMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApEthPortMtu.setStatus("current")


class _HwApDosDefend_Type(Integer32):
    """Custom type hwApDosDefend based on Integer32"""
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


_HwApDosDefend_Type.__name__ = "Integer32"
_HwApDosDefend_Object = MibTableColumn
hwApDosDefend = _HwApDosDefend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 3),
    _HwApDosDefend_Type()
)
hwApDosDefend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApDosDefend.setStatus("current")


class _HwApWorkMode_Type(Integer32):
    """Custom type hwApWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("routing", 2))
    )


_HwApWorkMode_Type.__name__ = "Integer32"
_HwApWorkMode_Object = MibTableColumn
hwApWorkMode = _HwApWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 4),
    _HwApWorkMode_Type()
)
hwApWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApWorkMode.setStatus("current")
_HwApLogBackupServerIp_Type = IpAddress
_HwApLogBackupServerIp_Object = MibTableColumn
hwApLogBackupServerIp = _HwApLogBackupServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 5),
    _HwApLogBackupServerIp_Type()
)
hwApLogBackupServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLogBackupServerIp.setStatus("current")


class _HwApLogBackupMode_Type(Integer32):
    """Custom type hwApLogBackupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoBackup", 1),
          ("disable", 3),
          ("manualBackup", 2))
    )


_HwApLogBackupMode_Type.__name__ = "Integer32"
_HwApLogBackupMode_Object = MibTableColumn
hwApLogBackupMode = _HwApLogBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 6),
    _HwApLogBackupMode_Type()
)
hwApLogBackupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLogBackupMode.setStatus("current")
_HwApProfileRowStatus_Type = RowStatus
_HwApProfileRowStatus_Object = MibTableColumn
hwApProfileRowStatus = _HwApProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 7),
    _HwApProfileRowStatus_Type()
)
hwApProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApProfileRowStatus.setStatus("current")


class _HwApSampleTime_Type(Integer32):
    """Custom type hwApSampleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 300),
    )


_HwApSampleTime_Type.__name__ = "Integer32"
_HwApSampleTime_Object = MibTableColumn
hwApSampleTime = _HwApSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 8),
    _HwApSampleTime_Type()
)
hwApSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApSampleTime.setStatus("current")


class _HwApStatisticsInterval_Type(Integer32):
    """Custom type hwApStatisticsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_HwApStatisticsInterval_Type.__name__ = "Integer32"
_HwApStatisticsInterval_Object = MibTableColumn
hwApStatisticsInterval = _HwApStatisticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 9),
    _HwApStatisticsInterval_Type()
)
hwApStatisticsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApStatisticsInterval.setStatus("current")


class _HwApEapStartMode_Type(Integer32):
    """Custom type hwApEapStartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_HwApEapStartMode_Type.__name__ = "Integer32"
_HwApEapStartMode_Object = MibTableColumn
hwApEapStartMode = _HwApEapStartMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 10),
    _HwApEapStartMode_Type()
)
hwApEapStartMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApEapStartMode.setStatus("current")
_HwApEapStartUnicastMac_Type = MacAddress
_HwApEapStartUnicastMac_Object = MibTableColumn
hwApEapStartUnicastMac = _HwApEapStartUnicastMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 11),
    _HwApEapStartUnicastMac_Type()
)
hwApEapStartUnicastMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApEapStartUnicastMac.setStatus("current")


class _HwApEapStartTransform_Type(Integer32):
    """Custom type hwApEapStartTransform based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("specific", 1))
    )


_HwApEapStartTransform_Type.__name__ = "Integer32"
_HwApEapStartTransform_Object = MibTableColumn
hwApEapStartTransform = _HwApEapStartTransform_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 12),
    _HwApEapStartTransform_Type()
)
hwApEapStartTransform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApEapStartTransform.setStatus("current")


class _HwApEapResponseMode_Type(Integer32):
    """Custom type hwApEapResponseMode based on Integer32"""
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
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicastLearning", 4),
          ("unicastSpecific", 3))
    )


_HwApEapResponseMode_Type.__name__ = "Integer32"
_HwApEapResponseMode_Object = MibTableColumn
hwApEapResponseMode = _HwApEapResponseMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 13),
    _HwApEapResponseMode_Type()
)
hwApEapResponseMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApEapResponseMode.setStatus("current")
_HwApEapResponseUnicastMac_Type = MacAddress
_HwApEapResponseUnicastMac_Object = MibTableColumn
hwApEapResponseUnicastMac = _HwApEapResponseUnicastMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 14),
    _HwApEapResponseUnicastMac_Type()
)
hwApEapResponseUnicastMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApEapResponseUnicastMac.setStatus("current")


class _HwApEapResponseTransform_Type(Integer32):
    """Custom type hwApEapResponseTransform based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("specific", 1))
    )


_HwApEapResponseTransform_Type.__name__ = "Integer32"
_HwApEapResponseTransform_Object = MibTableColumn
hwApEapResponseTransform = _HwApEapResponseTransform_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 15),
    _HwApEapResponseTransform_Type()
)
hwApEapResponseTransform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApEapResponseTransform.setStatus("current")


class _HwApOfflineManagement_Type(Integer32):
    """Custom type hwApOfflineManagement based on Integer32"""
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


_HwApOfflineManagement_Type.__name__ = "Integer32"
_HwApOfflineManagement_Object = MibTableColumn
hwApOfflineManagement = _HwApOfflineManagement_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 16),
    _HwApOfflineManagement_Type()
)
hwApOfflineManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApOfflineManagement.setStatus("current")


class _HwApAlarmRestrictionMode_Type(Integer32):
    """Custom type hwApAlarmRestrictionMode based on Integer32"""
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


_HwApAlarmRestrictionMode_Type.__name__ = "Integer32"
_HwApAlarmRestrictionMode_Object = MibTableColumn
hwApAlarmRestrictionMode = _HwApAlarmRestrictionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 17),
    _HwApAlarmRestrictionMode_Type()
)
hwApAlarmRestrictionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAlarmRestrictionMode.setStatus("current")


class _HwApAlarmRestrictionPeriod_Type(Integer32):
    """Custom type hwApAlarmRestrictionPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_HwApAlarmRestrictionPeriod_Type.__name__ = "Integer32"
_HwApAlarmRestrictionPeriod_Object = MibTableColumn
hwApAlarmRestrictionPeriod = _HwApAlarmRestrictionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 18),
    _HwApAlarmRestrictionPeriod_Type()
)
hwApAlarmRestrictionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAlarmRestrictionPeriod.setStatus("current")


class _HwAp4WayHandshakeRoamPolicy_Type(Integer32):
    """Custom type hwAp4WayHandshakeRoamPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("ap", 2))
    )


_HwAp4WayHandshakeRoamPolicy_Type.__name__ = "Integer32"
_HwAp4WayHandshakeRoamPolicy_Object = MibTableColumn
hwAp4WayHandshakeRoamPolicy = _HwAp4WayHandshakeRoamPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 19),
    _HwAp4WayHandshakeRoamPolicy_Type()
)
hwAp4WayHandshakeRoamPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAp4WayHandshakeRoamPolicy.setStatus("current")


class _HwApLogRecordLevel_Type(Integer32):
    """Custom type hwApLogRecordLevel based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_HwApLogRecordLevel_Type.__name__ = "Integer32"
_HwApLogRecordLevel_Object = MibTableColumn
hwApLogRecordLevel = _HwApLogRecordLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 20),
    _HwApLogRecordLevel_Type()
)
hwApLogRecordLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLogRecordLevel.setStatus("current")


class _HwApLogBackupPeriodTime_Type(Integer32):
    """Custom type hwApLogBackupPeriodTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_HwApLogBackupPeriodTime_Type.__name__ = "Integer32"
_HwApLogBackupPeriodTime_Object = MibTableColumn
hwApLogBackupPeriodTime = _HwApLogBackupPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 21),
    _HwApLogBackupPeriodTime_Type()
)
hwApLogBackupPeriodTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLogBackupPeriodTime.setStatus("current")


class _HwApLogRecordFtpMode_Type(Integer32):
    """Custom type hwApLogRecordFtpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ftp", 2),
          ("sftp", 3))
    )


_HwApLogRecordFtpMode_Type.__name__ = "Integer32"
_HwApLogRecordFtpMode_Object = MibTableColumn
hwApLogRecordFtpMode = _HwApLogRecordFtpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 22),
    _HwApLogRecordFtpMode_Type()
)
hwApLogRecordFtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLogRecordFtpMode.setStatus("current")


class _HwApLogServerUsername_Type(OctetString):
    """Custom type hwApLogServerUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwApLogServerUsername_Type.__name__ = "OctetString"
_HwApLogServerUsername_Object = MibTableColumn
hwApLogServerUsername = _HwApLogServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 23),
    _HwApLogServerUsername_Type()
)
hwApLogServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLogServerUsername.setStatus("current")


class _HwApLogServerUserPassword_Type(OctetString):
    """Custom type hwApLogServerUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwApLogServerUserPassword_Type.__name__ = "OctetString"
_HwApLogServerUserPassword_Object = MibTableColumn
hwApLogServerUserPassword = _HwApLogServerUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 24),
    _HwApLogServerUserPassword_Type()
)
hwApLogServerUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLogServerUserPassword.setStatus("current")
_HwApLogServerIp_Type = IpAddress
_HwApLogServerIp_Object = MibTableColumn
hwApLogServerIp = _HwApLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 25),
    _HwApLogServerIp_Type()
)
hwApLogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLogServerIp.setStatus("current")


class _HwApProfileTelnetSwitch_Type(Integer32):
    """Custom type hwApProfileTelnetSwitch based on Integer32"""
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


_HwApProfileTelnetSwitch_Type.__name__ = "Integer32"
_HwApProfileTelnetSwitch_Object = MibTableColumn
hwApProfileTelnetSwitch = _HwApProfileTelnetSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 26),
    _HwApProfileTelnetSwitch_Type()
)
hwApProfileTelnetSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApProfileTelnetSwitch.setStatus("current")


class _HwApSshSwitch_Type(Integer32):
    """Custom type hwApSshSwitch based on Integer32"""
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


_HwApSshSwitch_Type.__name__ = "Integer32"
_HwApSshSwitch_Object = MibTableColumn
hwApSshSwitch = _HwApSshSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 27),
    _HwApSshSwitch_Type()
)
hwApSshSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApSshSwitch.setStatus("current")


class _HwApProfileDhcpTrustPort_Type(Integer32):
    """Custom type hwApProfileDhcpTrustPort based on Integer32"""
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


_HwApProfileDhcpTrustPort_Type.__name__ = "Integer32"
_HwApProfileDhcpTrustPort_Object = MibTableColumn
hwApProfileDhcpTrustPort = _HwApProfileDhcpTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 28),
    _HwApProfileDhcpTrustPort_Type()
)
hwApProfileDhcpTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApProfileDhcpTrustPort.setStatus("current")


class _HwApProfileConsoleSwitch_Type(Integer32):
    """Custom type hwApProfileConsoleSwitch based on Integer32"""
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


_HwApProfileConsoleSwitch_Type.__name__ = "Integer32"
_HwApProfileConsoleSwitch_Object = MibTableColumn
hwApProfileConsoleSwitch = _HwApProfileConsoleSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 29),
    _HwApProfileConsoleSwitch_Type()
)
hwApProfileConsoleSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApProfileConsoleSwitch.setStatus("current")


class _HwApProfileMaxUserNum_Type(Integer32):
    """Custom type hwApProfileMaxUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwApProfileMaxUserNum_Type.__name__ = "Integer32"
_HwApProfileMaxUserNum_Object = MibTableColumn
hwApProfileMaxUserNum = _HwApProfileMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 30),
    _HwApProfileMaxUserNum_Type()
)
hwApProfileMaxUserNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApProfileMaxUserNum.setStatus("current")


class _HwApProfileNdTrustPort_Type(Integer32):
    """Custom type hwApProfileNdTrustPort based on Integer32"""
    defaultValue = 2

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


_HwApProfileNdTrustPort_Type.__name__ = "Integer32"
_HwApProfileNdTrustPort_Object = MibTableColumn
hwApProfileNdTrustPort = _HwApProfileNdTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 31),
    _HwApProfileNdTrustPort_Type()
)
hwApProfileNdTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApProfileNdTrustPort.setStatus("current")


class _HwApLogBackupServerIpv6Addr_Type(OctetString):
    """Custom type hwApLogBackupServerIpv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApLogBackupServerIpv6Addr_Type.__name__ = "OctetString"
_HwApLogBackupServerIpv6Addr_Object = MibTableColumn
hwApLogBackupServerIpv6Addr = _HwApLogBackupServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 32),
    _HwApLogBackupServerIpv6Addr_Type()
)
hwApLogBackupServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLogBackupServerIpv6Addr.setStatus("current")


class _HwApLedSwitch_Type(Integer32):
    """Custom type hwApLedSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HwApLedSwitch_Type.__name__ = "Integer32"
_HwApLedSwitch_Object = MibTableColumn
hwApLedSwitch = _HwApLedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 33),
    _HwApLedSwitch_Type()
)
hwApLedSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLedSwitch.setStatus("current")


class _HwApLocalAssocResSwitch_Type(Integer32):
    """Custom type hwApLocalAssocResSwitch based on Integer32"""
    defaultValue = 1

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


_HwApLocalAssocResSwitch_Type.__name__ = "Integer32"
_HwApLocalAssocResSwitch_Object = MibTableColumn
hwApLocalAssocResSwitch = _HwApLocalAssocResSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 1, 1, 34),
    _HwApLocalAssocResSwitch_Type()
)
hwApLocalAssocResSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLocalAssocResSwitch.setStatus("current")
_HwApProfileDefault_Type = OctetString
_HwApProfileDefault_Object = MibScalar
hwApProfileDefault = _HwApProfileDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 2),
    _HwApProfileDefault_Type()
)
hwApProfileDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApProfileDefault.setStatus("current")
_HwApProfileBatchInfo_ObjectIdentity = ObjectIdentity
hwApProfileBatchInfo = _HwApProfileBatchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 3)
)
_HwApProfileBatchStart_Type = Integer32
_HwApProfileBatchStart_Object = MibScalar
hwApProfileBatchStart = _HwApProfileBatchStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 3, 1),
    _HwApProfileBatchStart_Type()
)
hwApProfileBatchStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApProfileBatchStart.setStatus("current")
_HwApProfileBatchNumber_Type = Integer32
_HwApProfileBatchNumber_Object = MibScalar
hwApProfileBatchNumber = _HwApProfileBatchNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 3, 2),
    _HwApProfileBatchNumber_Type()
)
hwApProfileBatchNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApProfileBatchNumber.setStatus("current")
_HwApProfileBatchReturnNumber_Type = Integer32
_HwApProfileBatchReturnNumber_Object = MibScalar
hwApProfileBatchReturnNumber = _HwApProfileBatchReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 3, 3),
    _HwApProfileBatchReturnNumber_Type()
)
hwApProfileBatchReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApProfileBatchReturnNumber.setStatus("current")
_HwApProfileBatchNameList_Type = OctetString
_HwApProfileBatchNameList_Object = MibScalar
hwApProfileBatchNameList = _HwApProfileBatchNameList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 3, 3, 4),
    _HwApProfileBatchNameList_Type()
)
hwApProfileBatchNameList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApProfileBatchNameList.setStatus("current")
_HwApAuthListObjects_ObjectIdentity = ObjectIdentity
hwApAuthListObjects = _HwApAuthListObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4)
)
_HwApMacWhitelistTable_Object = MibTable
hwApMacWhitelistTable = _HwApMacWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hwApMacWhitelistTable.setStatus("current")
_HwApMacWhitelistEntry_Object = MibTableRow
hwApMacWhitelistEntry = _HwApMacWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 1, 1)
)
hwApMacWhitelistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMacWhitelistMacAddr"),
)
if mibBuilder.loadTexts:
    hwApMacWhitelistEntry.setStatus("current")
_HwApMacWhitelistMacAddr_Type = MacAddress
_HwApMacWhitelistMacAddr_Object = MibTableColumn
hwApMacWhitelistMacAddr = _HwApMacWhitelistMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 1, 1, 1),
    _HwApMacWhitelistMacAddr_Type()
)
hwApMacWhitelistMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApMacWhitelistMacAddr.setStatus("current")
_HwApMacWhitelistRowStatus_Type = RowStatus
_HwApMacWhitelistRowStatus_Object = MibTableColumn
hwApMacWhitelistRowStatus = _HwApMacWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 1, 1, 2),
    _HwApMacWhitelistRowStatus_Type()
)
hwApMacWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApMacWhitelistRowStatus.setStatus("current")
_HwApSnWhitelistTable_Object = MibTable
hwApSnWhitelistTable = _HwApSnWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 2)
)
if mibBuilder.loadTexts:
    hwApSnWhitelistTable.setStatus("current")
_HwApSnWhitelistEntry_Object = MibTableRow
hwApSnWhitelistEntry = _HwApSnWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 2, 1)
)
hwApSnWhitelistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApSnWhitelistSn"),
)
if mibBuilder.loadTexts:
    hwApSnWhitelistEntry.setStatus("current")
_HwApSnWhitelistSn_Type = OctetString
_HwApSnWhitelistSn_Object = MibTableColumn
hwApSnWhitelistSn = _HwApSnWhitelistSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 2, 1, 1),
    _HwApSnWhitelistSn_Type()
)
hwApSnWhitelistSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApSnWhitelistSn.setStatus("current")
_HwApSnWhitelistRowStatus_Type = RowStatus
_HwApSnWhitelistRowStatus_Object = MibTableColumn
hwApSnWhitelistRowStatus = _HwApSnWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 2, 1, 2),
    _HwApSnWhitelistRowStatus_Type()
)
hwApSnWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApSnWhitelistRowStatus.setStatus("current")


class _HwApAuthMode_Type(Integer32):
    """Custom type hwApAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAuth", 1),
          ("noAuth", 3),
          ("snAuth", 2))
    )


_HwApAuthMode_Type.__name__ = "Integer32"
_HwApAuthMode_Object = MibScalar
hwApAuthMode = _HwApAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 3),
    _HwApAuthMode_Type()
)
hwApAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAuthMode.setStatus("current")
_HwApMacWhitelistBatchQueryInfo_ObjectIdentity = ObjectIdentity
hwApMacWhitelistBatchQueryInfo = _HwApMacWhitelistBatchQueryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 4)
)
_HwApMacWhitelistBatchQueryStartNumber_Type = Integer32
_HwApMacWhitelistBatchQueryStartNumber_Object = MibScalar
hwApMacWhitelistBatchQueryStartNumber = _HwApMacWhitelistBatchQueryStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 4, 1),
    _HwApMacWhitelistBatchQueryStartNumber_Type()
)
hwApMacWhitelistBatchQueryStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMacWhitelistBatchQueryStartNumber.setStatus("current")
_HwApMacWhitelistBatchQueryNumber_Type = Integer32
_HwApMacWhitelistBatchQueryNumber_Object = MibScalar
hwApMacWhitelistBatchQueryNumber = _HwApMacWhitelistBatchQueryNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 4, 2),
    _HwApMacWhitelistBatchQueryNumber_Type()
)
hwApMacWhitelistBatchQueryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMacWhitelistBatchQueryNumber.setStatus("current")


class _HwApMacWhitelistBatchQueryList_Type(OctetString):
    """Custom type hwApMacWhitelistBatchQueryList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 768),
    )


_HwApMacWhitelistBatchQueryList_Type.__name__ = "OctetString"
_HwApMacWhitelistBatchQueryList_Object = MibScalar
hwApMacWhitelistBatchQueryList = _HwApMacWhitelistBatchQueryList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 4, 3),
    _HwApMacWhitelistBatchQueryList_Type()
)
hwApMacWhitelistBatchQueryList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMacWhitelistBatchQueryList.setStatus("current")
_HwApMacWhitelistBatchQueryReturnNumber_Type = Integer32
_HwApMacWhitelistBatchQueryReturnNumber_Object = MibScalar
hwApMacWhitelistBatchQueryReturnNumber = _HwApMacWhitelistBatchQueryReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 4, 4),
    _HwApMacWhitelistBatchQueryReturnNumber_Type()
)
hwApMacWhitelistBatchQueryReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMacWhitelistBatchQueryReturnNumber.setStatus("current")
_HwApSnWhitelistBatchQueryInfo_ObjectIdentity = ObjectIdentity
hwApSnWhitelistBatchQueryInfo = _HwApSnWhitelistBatchQueryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 5)
)
_HwApSnWhitelistBatchQueryStartNumber_Type = Integer32
_HwApSnWhitelistBatchQueryStartNumber_Object = MibScalar
hwApSnWhitelistBatchQueryStartNumber = _HwApSnWhitelistBatchQueryStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 5, 1),
    _HwApSnWhitelistBatchQueryStartNumber_Type()
)
hwApSnWhitelistBatchQueryStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApSnWhitelistBatchQueryStartNumber.setStatus("current")
_HwApSnWhitelistBatchQueryNumber_Type = Integer32
_HwApSnWhitelistBatchQueryNumber_Object = MibScalar
hwApSnWhitelistBatchQueryNumber = _HwApSnWhitelistBatchQueryNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 5, 2),
    _HwApSnWhitelistBatchQueryNumber_Type()
)
hwApSnWhitelistBatchQueryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApSnWhitelistBatchQueryNumber.setStatus("current")


class _HwApSnWhitelistBatchQueryList_Type(OctetString):
    """Custom type hwApSnWhitelistBatchQueryList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_HwApSnWhitelistBatchQueryList_Type.__name__ = "OctetString"
_HwApSnWhitelistBatchQueryList_Object = MibScalar
hwApSnWhitelistBatchQueryList = _HwApSnWhitelistBatchQueryList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 5, 3),
    _HwApSnWhitelistBatchQueryList_Type()
)
hwApSnWhitelistBatchQueryList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSnWhitelistBatchQueryList.setStatus("current")
_HwApSnWhitelistBatchQueryReturnNumber_Type = Integer32
_HwApSnWhitelistBatchQueryReturnNumber_Object = MibScalar
hwApSnWhitelistBatchQueryReturnNumber = _HwApSnWhitelistBatchQueryReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 5, 4),
    _HwApSnWhitelistBatchQueryReturnNumber_Type()
)
hwApSnWhitelistBatchQueryReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSnWhitelistBatchQueryReturnNumber.setStatus("current")
_HwApMacBlacklistTable_Object = MibTable
hwApMacBlacklistTable = _HwApMacBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 6)
)
if mibBuilder.loadTexts:
    hwApMacBlacklistTable.setStatus("current")
_HwApMacBlacklistEntry_Object = MibTableRow
hwApMacBlacklistEntry = _HwApMacBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 6, 1)
)
hwApMacBlacklistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMacBlacklistMacAddr"),
)
if mibBuilder.loadTexts:
    hwApMacBlacklistEntry.setStatus("current")
_HwApMacBlacklistMacAddr_Type = MacAddress
_HwApMacBlacklistMacAddr_Object = MibTableColumn
hwApMacBlacklistMacAddr = _HwApMacBlacklistMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 6, 1, 1),
    _HwApMacBlacklistMacAddr_Type()
)
hwApMacBlacklistMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApMacBlacklistMacAddr.setStatus("current")
_HwApMacBlacklistRowStatus_Type = RowStatus
_HwApMacBlacklistRowStatus_Object = MibTableColumn
hwApMacBlacklistRowStatus = _HwApMacBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 6, 1, 2),
    _HwApMacBlacklistRowStatus_Type()
)
hwApMacBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApMacBlacklistRowStatus.setStatus("current")
_HwApSnBlacklistTable_Object = MibTable
hwApSnBlacklistTable = _HwApSnBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 7)
)
if mibBuilder.loadTexts:
    hwApSnBlacklistTable.setStatus("current")
_HwApSnBlacklistEntry_Object = MibTableRow
hwApSnBlacklistEntry = _HwApSnBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 7, 1)
)
hwApSnBlacklistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApSnBlacklistSn"),
)
if mibBuilder.loadTexts:
    hwApSnBlacklistEntry.setStatus("current")
_HwApSnBlacklistSn_Type = OctetString
_HwApSnBlacklistSn_Object = MibTableColumn
hwApSnBlacklistSn = _HwApSnBlacklistSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 7, 1, 1),
    _HwApSnBlacklistSn_Type()
)
hwApSnBlacklistSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApSnBlacklistSn.setStatus("current")
_HwApSnBlacklistRowStatus_Type = RowStatus
_HwApSnBlacklistRowStatus_Object = MibTableColumn
hwApSnBlacklistRowStatus = _HwApSnBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 4, 7, 1, 2),
    _HwApSnBlacklistRowStatus_Type()
)
hwApSnBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApSnBlacklistRowStatus.setStatus("current")
_HwApRegionObjects_ObjectIdentity = ObjectIdentity
hwApRegionObjects = _HwApRegionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5)
)
_HwApRegionTable_Object = MibTable
hwApRegionTable = _HwApRegionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hwApRegionTable.setStatus("current")
_HwApRegionEntry_Object = MibTableRow
hwApRegionEntry = _HwApRegionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1)
)
hwApRegionEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApRegionIndex"),
)
if mibBuilder.loadTexts:
    hwApRegionEntry.setStatus("current")
_HwApRegionIndex_Type = Integer32
_HwApRegionIndex_Object = MibTableColumn
hwApRegionIndex = _HwApRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 1),
    _HwApRegionIndex_Type()
)
hwApRegionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApRegionIndex.setStatus("current")
_HwApRegionName_Type = OctetString
_HwApRegionName_Object = MibTableColumn
hwApRegionName = _HwApRegionName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 2),
    _HwApRegionName_Type()
)
hwApRegionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApRegionName.setStatus("current")


class _HwApRegionDeployMode_Type(Integer32):
    """Custom type hwApRegionDeployMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("denselyDeploy", 3),
          ("discreteDeploy", 1),
          ("normalDeploy", 2))
    )


_HwApRegionDeployMode_Type.__name__ = "Integer32"
_HwApRegionDeployMode_Object = MibTableColumn
hwApRegionDeployMode = _HwApRegionDeployMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 3),
    _HwApRegionDeployMode_Type()
)
hwApRegionDeployMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApRegionDeployMode.setStatus("current")
_HwApRegionApNumber_Type = Integer32
_HwApRegionApNumber_Object = MibTableColumn
hwApRegionApNumber = _HwApRegionApNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 4),
    _HwApRegionApNumber_Type()
)
hwApRegionApNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRegionApNumber.setStatus("current")
_HwApRegionApIndexMask_Type = OctetString
_HwApRegionApIndexMask_Object = MibTableColumn
hwApRegionApIndexMask = _HwApRegionApIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 5),
    _HwApRegionApIndexMask_Type()
)
hwApRegionApIndexMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRegionApIndexMask.setStatus("current")
_HwApRegionRowStatus_Type = RowStatus
_HwApRegionRowStatus_Object = MibTableColumn
hwApRegionRowStatus = _HwApRegionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 6),
    _HwApRegionRowStatus_Type()
)
hwApRegionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApRegionRowStatus.setStatus("current")


class _HwApRegionForwardMode_Type(Integer32):
    """Custom type hwApRegionForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directForward", 1),
          ("tunnel", 2),
          ("unknown", -1))
    )


_HwApRegionForwardMode_Type.__name__ = "Integer32"
_HwApRegionForwardMode_Object = MibTableColumn
hwApRegionForwardMode = _HwApRegionForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 7),
    _HwApRegionForwardMode_Type()
)
hwApRegionForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionForwardMode.setStatus("current")
_HwApRegionCountryCode_Type = OctetString
_HwApRegionCountryCode_Object = MibTableColumn
hwApRegionCountryCode = _HwApRegionCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 8),
    _HwApRegionCountryCode_Type()
)
hwApRegionCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionCountryCode.setStatus("current")
_HwApRegionScanChannel2G_Type = OctetString
_HwApRegionScanChannel2G_Object = MibTableColumn
hwApRegionScanChannel2G = _HwApRegionScanChannel2G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 9),
    _HwApRegionScanChannel2G_Type()
)
hwApRegionScanChannel2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionScanChannel2G.setStatus("current")
_HwApRegionScanChannel5G_Type = OctetString
_HwApRegionScanChannel5G_Object = MibTableColumn
hwApRegionScanChannel5G = _HwApRegionScanChannel5G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 10),
    _HwApRegionScanChannel5G_Type()
)
hwApRegionScanChannel5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionScanChannel5G.setStatus("current")
_HwApRegionCalibrateChannel2G_Type = OctetString
_HwApRegionCalibrateChannel2G_Object = MibTableColumn
hwApRegionCalibrateChannel2G = _HwApRegionCalibrateChannel2G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 11),
    _HwApRegionCalibrateChannel2G_Type()
)
hwApRegionCalibrateChannel2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionCalibrateChannel2G.setStatus("current")
_HwApRegionCalibrateChannel5G_Type = OctetString
_HwApRegionCalibrateChannel5G_Object = MibTableColumn
hwApRegionCalibrateChannel5G = _HwApRegionCalibrateChannel5G_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 12),
    _HwApRegionCalibrateChannel5G_Type()
)
hwApRegionCalibrateChannel5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionCalibrateChannel5G.setStatus("current")


class _HwApRegionCalibrate5gBandWidth_Type(Integer32):
    """Custom type hwApRegionCalibrate5gBandWidth based on Integer32"""
    defaultValue = 1

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
        *(("ht20", 1),
          ("ht40", 2),
          ("ht80", 3),
          ("unknown", 0))
    )


_HwApRegionCalibrate5gBandWidth_Type.__name__ = "Integer32"
_HwApRegionCalibrate5gBandWidth_Object = MibTableColumn
hwApRegionCalibrate5gBandWidth = _HwApRegionCalibrate5gBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 1, 1, 13),
    _HwApRegionCalibrate5gBandWidth_Type()
)
hwApRegionCalibrate5gBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionCalibrate5gBandWidth.setStatus("current")
_HwApRegionGlobalInfo_ObjectIdentity = ObjectIdentity
hwApRegionGlobalInfo = _HwApRegionGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2)
)
_HwApRegionDefault_Type = Integer32
_HwApRegionDefault_Object = MibScalar
hwApRegionDefault = _HwApRegionDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 1),
    _HwApRegionDefault_Type()
)
hwApRegionDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionDefault.setStatus("current")
_HwApRegionAllExistRegionIndexMask_Type = OctetString
_HwApRegionAllExistRegionIndexMask_Object = MibScalar
hwApRegionAllExistRegionIndexMask = _HwApRegionAllExistRegionIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 2),
    _HwApRegionAllExistRegionIndexMask_Type()
)
hwApRegionAllExistRegionIndexMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRegionAllExistRegionIndexMask.setStatus("current")
_HwApRegionBatchInfo_ObjectIdentity = ObjectIdentity
hwApRegionBatchInfo = _HwApRegionBatchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 3)
)
_HwApRegionBatchStart_Type = Integer32
_HwApRegionBatchStart_Object = MibScalar
hwApRegionBatchStart = _HwApRegionBatchStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 3, 1),
    _HwApRegionBatchStart_Type()
)
hwApRegionBatchStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionBatchStart.setStatus("current")
_HwApRegionBatchNumber_Type = Integer32
_HwApRegionBatchNumber_Object = MibScalar
hwApRegionBatchNumber = _HwApRegionBatchNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 3, 2),
    _HwApRegionBatchNumber_Type()
)
hwApRegionBatchNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRegionBatchNumber.setStatus("current")
_HwApRegionBatchReturnNumber_Type = Integer32
_HwApRegionBatchReturnNumber_Object = MibScalar
hwApRegionBatchReturnNumber = _HwApRegionBatchReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 3, 3),
    _HwApRegionBatchReturnNumber_Type()
)
hwApRegionBatchReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRegionBatchReturnNumber.setStatus("current")
_HwApRegionBatchNameList_Type = OctetString
_HwApRegionBatchNameList_Object = MibScalar
hwApRegionBatchNameList = _HwApRegionBatchNameList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 3, 4),
    _HwApRegionBatchNameList_Type()
)
hwApRegionBatchNameList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRegionBatchNameList.setStatus("current")
_HwApRegionBatchDeployMode_Type = OctetString
_HwApRegionBatchDeployMode_Object = MibScalar
hwApRegionBatchDeployMode = _HwApRegionBatchDeployMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 2, 3, 5),
    _HwApRegionBatchDeployMode_Type()
)
hwApRegionBatchDeployMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRegionBatchDeployMode.setStatus("current")
_HwApRegionMerge_ObjectIdentity = ObjectIdentity
hwApRegionMerge = _HwApRegionMerge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 3)
)
_HwApSrcRegionIndex_Type = Integer32
_HwApSrcRegionIndex_Object = MibScalar
hwApSrcRegionIndex = _HwApSrcRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 3, 1),
    _HwApSrcRegionIndex_Type()
)
hwApSrcRegionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApSrcRegionIndex.setStatus("current")
_HwApDestRegionIndex_Type = Integer32
_HwApDestRegionIndex_Object = MibScalar
hwApDestRegionIndex = _HwApDestRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 5, 3, 2),
    _HwApDestRegionIndex_Type()
)
hwApDestRegionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApDestRegionIndex.setStatus("current")
_HwApObjects_ObjectIdentity = ObjectIdentity
hwApObjects = _HwApObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6)
)
_HwApTable_Object = MibTable
hwApTable = _HwApTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hwApTable.setStatus("current")
_HwApEntry_Object = MibTableRow
hwApEntry = _HwApEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1)
)
hwApEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
)
if mibBuilder.loadTexts:
    hwApEntry.setStatus("current")
_HwApIndex_Type = Integer32
_HwApIndex_Object = MibTableColumn
hwApIndex = _HwApIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 1),
    _HwApIndex_Type()
)
hwApIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwApIndex.setStatus("current")
_HwApUsedType_Type = OctetString
_HwApUsedType_Object = MibTableColumn
hwApUsedType = _HwApUsedType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 2),
    _HwApUsedType_Type()
)
hwApUsedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApUsedType.setStatus("current")
_HwApUsedProfileName_Type = OctetString
_HwApUsedProfileName_Object = MibTableColumn
hwApUsedProfileName = _HwApUsedProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 3),
    _HwApUsedProfileName_Type()
)
hwApUsedProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApUsedProfileName.setStatus("current")
_HwApUsedRegionIndex_Type = Integer32
_HwApUsedRegionIndex_Object = MibTableColumn
hwApUsedRegionIndex = _HwApUsedRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 4),
    _HwApUsedRegionIndex_Type()
)
hwApUsedRegionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApUsedRegionIndex.setStatus("current")
_HwApMac_Type = MacAddress
_HwApMac_Object = MibTableColumn
hwApMac = _HwApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 5),
    _HwApMac_Type()
)
hwApMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApMac.setStatus("current")
_HwApSn_Type = OctetString
_HwApSn_Object = MibTableColumn
hwApSn = _HwApSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 6),
    _HwApSn_Type()
)
hwApSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApSn.setStatus("current")
_HwApSysName_Type = OctetString
_HwApSysName_Object = MibTableColumn
hwApSysName = _HwApSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 7),
    _HwApSysName_Type()
)
hwApSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApSysName.setStatus("current")


class _HwApRunState_Type(Integer32):
    """Custom type hwApRunState based on Integer32"""
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
        *(("autofind", 2),
          ("commitFailed", 10),
          ("committing", 9),
          ("config", 5),
          ("configFailed", 6),
          ("download", 7),
          ("fault", 4),
          ("idle", 1),
          ("normal", 8),
          ("standby", 11),
          ("typeNotMatch", 3),
          ("vermismatch", 12))
    )


_HwApRunState_Type.__name__ = "Integer32"
_HwApRunState_Object = MibTableColumn
hwApRunState = _HwApRunState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 8),
    _HwApRunState_Type()
)
hwApRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRunState.setStatus("current")
_HwApSoftwareVersion_Type = OctetString
_HwApSoftwareVersion_Object = MibTableColumn
hwApSoftwareVersion = _HwApSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 9),
    _HwApSoftwareVersion_Type()
)
hwApSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSoftwareVersion.setStatus("current")
_HwApHardwareVersion_Type = OctetString
_HwApHardwareVersion_Object = MibTableColumn
hwApHardwareVersion = _HwApHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 10),
    _HwApHardwareVersion_Type()
)
hwApHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApHardwareVersion.setStatus("current")
_HwApCpuType_Type = OctetString
_HwApCpuType_Object = MibTableColumn
hwApCpuType = _HwApCpuType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 11),
    _HwApCpuType_Type()
)
hwApCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApCpuType.setStatus("current")
_HwApCpufrequency_Type = Integer32
_HwApCpufrequency_Object = MibTableColumn
hwApCpufrequency = _HwApCpufrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 12),
    _HwApCpufrequency_Type()
)
hwApCpufrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApCpufrequency.setStatus("current")
if mibBuilder.loadTexts:
    hwApCpufrequency.setUnits("MHZ")
_HwApMemoryType_Type = OctetString
_HwApMemoryType_Object = MibTableColumn
hwApMemoryType = _HwApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 13),
    _HwApMemoryType_Type()
)
hwApMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMemoryType.setStatus("current")
_HwApDomain_Type = OctetString
_HwApDomain_Object = MibTableColumn
hwApDomain = _HwApDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 14),
    _HwApDomain_Type()
)
hwApDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApDomain.setStatus("current")
_HwApIpAddress_Type = IpAddress
_HwApIpAddress_Object = MibTableColumn
hwApIpAddress = _HwApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 15),
    _HwApIpAddress_Type()
)
hwApIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApIpAddress.setStatus("current")
_HwApIpNetMask_Type = IpAddress
_HwApIpNetMask_Object = MibTableColumn
hwApIpNetMask = _HwApIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 16),
    _HwApIpNetMask_Type()
)
hwApIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApIpNetMask.setStatus("current")
_HwApGatewayIp_Type = IpAddress
_HwApGatewayIp_Object = MibTableColumn
hwApGatewayIp = _HwApGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 17),
    _HwApGatewayIp_Type()
)
hwApGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApGatewayIp.setStatus("current")
_HwApMemorySize_Type = Integer32
_HwApMemorySize_Object = MibTableColumn
hwApMemorySize = _HwApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 18),
    _HwApMemorySize_Type()
)
hwApMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hwApMemorySize.setUnits("MB")
_HwApFlashSize_Type = Integer32
_HwApFlashSize_Object = MibTableColumn
hwApFlashSize = _HwApFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 19),
    _HwApFlashSize_Type()
)
hwApFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    hwApFlashSize.setUnits("MB")
_HwApRunTime_Type = Unsigned32
_HwApRunTime_Object = MibTableColumn
hwApRunTime = _HwApRunTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 20),
    _HwApRunTime_Type()
)
hwApRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApRunTime.setStatus("current")


class _HwApUpEthPortSpeed_Type(Integer32):
    """Custom type hwApUpEthPortSpeed based on Integer32"""
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
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4))
    )


_HwApUpEthPortSpeed_Type.__name__ = "Integer32"
_HwApUpEthPortSpeed_Object = MibTableColumn
hwApUpEthPortSpeed = _HwApUpEthPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 21),
    _HwApUpEthPortSpeed_Type()
)
hwApUpEthPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpEthPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hwApUpEthPortSpeed.setUnits("Mbps")


class _HwApUpEthPortSpeedMode_Type(Integer32):
    """Custom type hwApUpEthPortSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forced", 2))
    )


_HwApUpEthPortSpeedMode_Type.__name__ = "Integer32"
_HwApUpEthPortSpeedMode_Object = MibTableColumn
hwApUpEthPortSpeedMode = _HwApUpEthPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 22),
    _HwApUpEthPortSpeedMode_Type()
)
hwApUpEthPortSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpEthPortSpeedMode.setStatus("current")


class _HwApUpEthPortDuplex_Type(Integer32):
    """Custom type hwApUpEthPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_HwApUpEthPortDuplex_Type.__name__ = "Integer32"
_HwApUpEthPortDuplex_Object = MibTableColumn
hwApUpEthPortDuplex = _HwApUpEthPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 23),
    _HwApUpEthPortDuplex_Type()
)
hwApUpEthPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpEthPortDuplex.setStatus("current")


class _HwApUpEthPortDuplexMode_Type(Integer32):
    """Custom type hwApUpEthPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forced", 2))
    )


_HwApUpEthPortDuplexMode_Type.__name__ = "Integer32"
_HwApUpEthPortDuplexMode_Object = MibTableColumn
hwApUpEthPortDuplexMode = _HwApUpEthPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 24),
    _HwApUpEthPortDuplexMode_Type()
)
hwApUpEthPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpEthPortDuplexMode.setStatus("current")


class _HwApAdminOper_Type(Integer32):
    """Custom type hwApAdminOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 2),
          ("manufacturerConfig", 3),
          ("replaceAp", 6),
          ("reset", 1))
    )


_HwApAdminOper_Type.__name__ = "Integer32"
_HwApAdminOper_Object = MibTableColumn
hwApAdminOper = _HwApAdminOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 25),
    _HwApAdminOper_Type()
)
hwApAdminOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAdminOper.setStatus("current")
_HwApRowstatus_Type = RowStatus
_HwApRowstatus_Object = MibTableColumn
hwApRowstatus = _HwApRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 26),
    _HwApRowstatus_Type()
)
hwApRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApRowstatus.setStatus("current")


class _HwApPerformanceStatCycle_Type(Integer32):
    """Custom type hwApPerformanceStatCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 3),
          ("fiveMinutes", 1),
          ("tenMinutes", 2))
    )


_HwApPerformanceStatCycle_Type.__name__ = "Integer32"
_HwApPerformanceStatCycle_Object = MibTableColumn
hwApPerformanceStatCycle = _HwApPerformanceStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 27),
    _HwApPerformanceStatCycle_Type()
)
hwApPerformanceStatCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPerformanceStatCycle.setStatus("current")
_HwApDNS_Type = IpAddress
_HwApDNS_Object = MibTableColumn
hwApDNS = _HwApDNS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 28),
    _HwApDNS_Type()
)
hwApDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApDNS.setStatus("current")


class _HwApRunningMode_Type(Integer32):
    """Custom type hwApRunningMode based on Integer32"""
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
          ("fat", 2),
          ("fit", 3))
    )


_HwApRunningMode_Type.__name__ = "Integer32"
_HwApRunningMode_Object = MibTableColumn
hwApRunningMode = _HwApRunningMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 29),
    _HwApRunningMode_Type()
)
hwApRunningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRunningMode.setStatus("current")


class _HwApForwardMode_Type(Integer32):
    """Custom type hwApForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directForward", 1),
          ("tunnel", 2),
          ("unknown", -1))
    )


_HwApForwardMode_Type.__name__ = "Integer32"
_HwApForwardMode_Object = MibTableColumn
hwApForwardMode = _HwApForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 30),
    _HwApForwardMode_Type()
)
hwApForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApForwardMode.setStatus("current")


class _HwApAntennaMode_Type(Integer32):
    """Custom type hwApAntennaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 1),
          ("leftMode", 2),
          ("rightMode", 3))
    )


_HwApAntennaMode_Type.__name__ = "Integer32"
_HwApAntennaMode_Object = MibTableColumn
hwApAntennaMode = _HwApAntennaMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 31),
    _HwApAntennaMode_Type()
)
hwApAntennaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAntennaMode.setStatus("current")
_HwApCpuThreshold_Type = Integer32
_HwApCpuThreshold_Object = MibTableColumn
hwApCpuThreshold = _HwApCpuThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 32),
    _HwApCpuThreshold_Type()
)
hwApCpuThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApCpuThreshold.setStatus("current")
_HwApMemThreshold_Type = Integer32
_HwApMemThreshold_Object = MibTableColumn
hwApMemThreshold = _HwApMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 33),
    _HwApMemThreshold_Type()
)
hwApMemThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApMemThreshold.setStatus("current")
_HwApNEnumber_Type = OctetString
_HwApNEnumber_Object = MibTableColumn
hwApNEnumber = _HwApNEnumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 34),
    _HwApNEnumber_Type()
)
hwApNEnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApNEnumber.setStatus("current")
_HwApOnlineTime_Type = Unsigned32
_HwApOnlineTime_Object = MibTableColumn
hwApOnlineTime = _HwApOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 35),
    _HwApOnlineTime_Type()
)
hwApOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOnlineTime.setStatus("current")
_HwApSysSoftwareDesc_Type = OctetString
_HwApSysSoftwareDesc_Object = MibTableColumn
hwApSysSoftwareDesc = _HwApSysSoftwareDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 36),
    _HwApSysSoftwareDesc_Type()
)
hwApSysSoftwareDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSysSoftwareDesc.setStatus("current")
_HwApSysHardtwareDesc_Type = OctetString
_HwApSysHardtwareDesc_Object = MibTableColumn
hwApSysHardtwareDesc = _HwApSysHardtwareDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 37),
    _HwApSysHardtwareDesc_Type()
)
hwApSysHardtwareDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSysHardtwareDesc.setStatus("current")
_HwApSysManufacture_Type = OctetString
_HwApSysManufacture_Object = MibTableColumn
hwApSysManufacture = _HwApSysManufacture_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 38),
    _HwApSysManufacture_Type()
)
hwApSysManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSysManufacture.setStatus("current")
_HwApSysSoftwareName_Type = OctetString
_HwApSysSoftwareName_Object = MibTableColumn
hwApSysSoftwareName = _HwApSysSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 39),
    _HwApSysSoftwareName_Type()
)
hwApSysSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSysSoftwareName.setStatus("current")
_HwApSysSoftwareVendor_Type = OctetString
_HwApSysSoftwareVendor_Object = MibTableColumn
hwApSysSoftwareVendor = _HwApSysSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 40),
    _HwApSysSoftwareVendor_Type()
)
hwApSysSoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSysSoftwareVendor.setStatus("current")
_HwApManagementVlanID_Type = Integer32
_HwApManagementVlanID_Object = MibTableColumn
hwApManagementVlanID = _HwApManagementVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 41),
    _HwApManagementVlanID_Type()
)
hwApManagementVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApManagementVlanID.setStatus("current")


class _HwApUsername_Type(OctetString):
    """Custom type hwApUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwApUsername_Type.__name__ = "OctetString"
_HwApUsername_Object = MibTableColumn
hwApUsername = _HwApUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 42),
    _HwApUsername_Type()
)
hwApUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApUsername.setStatus("current")


class _HwApPassword_Type(OctetString):
    """Custom type hwApPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwApPassword_Type.__name__ = "OctetString"
_HwApPassword_Object = MibTableColumn
hwApPassword = _HwApPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 43),
    _HwApPassword_Type()
)
hwApPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPassword.setStatus("current")
_HwApAcIP1_Type = IpAddress
_HwApAcIP1_Object = MibTableColumn
hwApAcIP1 = _HwApAcIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 44),
    _HwApAcIP1_Type()
)
hwApAcIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAcIP1.setStatus("current")
_HwApAcIP2_Type = IpAddress
_HwApAcIP2_Object = MibTableColumn
hwApAcIP2 = _HwApAcIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 45),
    _HwApAcIP2_Type()
)
hwApAcIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAcIP2.setStatus("current")
_HwApAcIP3_Type = IpAddress
_HwApAcIP3_Object = MibTableColumn
hwApAcIP3 = _HwApAcIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 46),
    _HwApAcIP3_Type()
)
hwApAcIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAcIP3.setStatus("current")
_HwApAcIP4_Type = IpAddress
_HwApAcIP4_Object = MibTableColumn
hwApAcIP4 = _HwApAcIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 47),
    _HwApAcIP4_Type()
)
hwApAcIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAcIP4.setStatus("current")


class _HwApIpMode_Type(Integer32):
    """Custom type hwApIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dchp", 1),
          ("pppoe", 2),
          ("static", 3))
    )


_HwApIpMode_Type.__name__ = "Integer32"
_HwApIpMode_Object = MibTableColumn
hwApIpMode = _HwApIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 48),
    _HwApIpMode_Type()
)
hwApIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApIpMode.setStatus("current")


class _HwApLldpEnable_Type(Integer32):
    """Custom type hwApLldpEnable based on Integer32"""
    defaultValue = 2

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


_HwApLldpEnable_Type.__name__ = "Integer32"
_HwApLldpEnable_Object = MibTableColumn
hwApLldpEnable = _HwApLldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 49),
    _HwApLldpEnable_Type()
)
hwApLldpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpEnable.setStatus("current")


class _HwApLldpManageAddr_Type(Integer32):
    """Custom type hwApLldpManageAddr based on Integer32"""
    defaultValue = 2

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


_HwApLldpManageAddr_Type.__name__ = "Integer32"
_HwApLldpManageAddr_Object = MibTableColumn
hwApLldpManageAddr = _HwApLldpManageAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 50),
    _HwApLldpManageAddr_Type()
)
hwApLldpManageAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpManageAddr.setStatus("current")


class _HwApLldpPortDes_Type(Integer32):
    """Custom type hwApLldpPortDes based on Integer32"""
    defaultValue = 2

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


_HwApLldpPortDes_Type.__name__ = "Integer32"
_HwApLldpPortDes_Object = MibTableColumn
hwApLldpPortDes = _HwApLldpPortDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 51),
    _HwApLldpPortDes_Type()
)
hwApLldpPortDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpPortDes.setStatus("current")


class _HwApLldpSysCab_Type(Integer32):
    """Custom type hwApLldpSysCab based on Integer32"""
    defaultValue = 2

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


_HwApLldpSysCab_Type.__name__ = "Integer32"
_HwApLldpSysCab_Object = MibTableColumn
hwApLldpSysCab = _HwApLldpSysCab_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 52),
    _HwApLldpSysCab_Type()
)
hwApLldpSysCab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpSysCab.setStatus("current")


class _HwApLldpSysDes_Type(Integer32):
    """Custom type hwApLldpSysDes based on Integer32"""
    defaultValue = 2

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


_HwApLldpSysDes_Type.__name__ = "Integer32"
_HwApLldpSysDes_Object = MibTableColumn
hwApLldpSysDes = _HwApLldpSysDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 53),
    _HwApLldpSysDes_Type()
)
hwApLldpSysDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpSysDes.setStatus("current")


class _HwApLldpSysName_Type(Integer32):
    """Custom type hwApLldpSysName based on Integer32"""
    defaultValue = 2

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


_HwApLldpSysName_Type.__name__ = "Integer32"
_HwApLldpSysName_Object = MibTableColumn
hwApLldpSysName = _HwApLldpSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 54),
    _HwApLldpSysName_Type()
)
hwApLldpSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpSysName.setStatus("current")


class _HwApLldpDelay_Type(Integer32):
    """Custom type hwApLldpDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_HwApLldpDelay_Type.__name__ = "Integer32"
_HwApLldpDelay_Object = MibTableColumn
hwApLldpDelay = _HwApLldpDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 55),
    _HwApLldpDelay_Type()
)
hwApLldpDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpDelay.setStatus("current")


class _HwApLldpHoldMultiplier_Type(Integer32):
    """Custom type hwApLldpHoldMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_HwApLldpHoldMultiplier_Type.__name__ = "Integer32"
_HwApLldpHoldMultiplier_Object = MibTableColumn
hwApLldpHoldMultiplier = _HwApLldpHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 56),
    _HwApLldpHoldMultiplier_Type()
)
hwApLldpHoldMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpHoldMultiplier.setStatus("current")


class _HwApLldpInterval_Type(Integer32):
    """Custom type hwApLldpInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_HwApLldpInterval_Type.__name__ = "Integer32"
_HwApLldpInterval_Object = MibTableColumn
hwApLldpInterval = _HwApLldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 57),
    _HwApLldpInterval_Type()
)
hwApLldpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpInterval.setStatus("current")


class _HwApLldpRestartDelay_Type(Integer32):
    """Custom type hwApLldpRestartDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwApLldpRestartDelay_Type.__name__ = "Integer32"
_HwApLldpRestartDelay_Object = MibTableColumn
hwApLldpRestartDelay = _HwApLldpRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 58),
    _HwApLldpRestartDelay_Type()
)
hwApLldpRestartDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpRestartDelay.setStatus("current")


class _HwApLldpAdminStatus_Type(Integer32):
    """Custom type hwApLldpAdminStatus based on Integer32"""
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
        *(("rx", 2),
          ("tx", 3),
          ("txrx", 1))
    )


_HwApLldpAdminStatus_Type.__name__ = "Integer32"
_HwApLldpAdminStatus_Object = MibTableColumn
hwApLldpAdminStatus = _HwApLldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 59),
    _HwApLldpAdminStatus_Type()
)
hwApLldpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpAdminStatus.setStatus("current")


class _HwApLldpReportInterval_Type(Integer32):
    """Custom type hwApLldpReportInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_HwApLldpReportInterval_Type.__name__ = "Integer32"
_HwApLldpReportInterval_Object = MibTableColumn
hwApLldpReportInterval = _HwApLldpReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 60),
    _HwApLldpReportInterval_Type()
)
hwApLldpReportInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApLldpReportInterval.setStatus("current")
_HwApBomCode_Type = OctetString
_HwApBomCode_Object = MibTableColumn
hwApBomCode = _HwApBomCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 61),
    _HwApBomCode_Type()
)
hwApBomCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApBomCode.setStatus("current")
_HwApSaveMode_Type = Integer32
_HwApSaveMode_Object = MibTableColumn
hwApSaveMode = _HwApSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 62),
    _HwApSaveMode_Type()
)
hwApSaveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApSaveMode.setStatus("obsolete")
_HwApProtectAcPriority_Type = Integer32
_HwApProtectAcPriority_Object = MibTableColumn
hwApProtectAcPriority = _HwApProtectAcPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 63),
    _HwApProtectAcPriority_Type()
)
hwApProtectAcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApProtectAcPriority.setStatus("current")
_HwApProtectAcIP_Type = IpAddress
_HwApProtectAcIP_Object = MibTableColumn
hwApProtectAcIP = _HwApProtectAcIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 64),
    _HwApProtectAcIP_Type()
)
hwApProtectAcIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApProtectAcIP.setStatus("current")


class _HwApOpticalHighRxPowerThreshold_Type(Integer32):
    """Custom type hwApOpticalHighRxPowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_HwApOpticalHighRxPowerThreshold_Type.__name__ = "Integer32"
_HwApOpticalHighRxPowerThreshold_Object = MibTableColumn
hwApOpticalHighRxPowerThreshold = _HwApOpticalHighRxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 65),
    _HwApOpticalHighRxPowerThreshold_Type()
)
hwApOpticalHighRxPowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApOpticalHighRxPowerThreshold.setStatus("current")


class _HwApOpticalLowRxPowerThreshold_Type(Integer32):
    """Custom type hwApOpticalLowRxPowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HwApOpticalLowRxPowerThreshold_Type.__name__ = "Integer32"
_HwApOpticalLowRxPowerThreshold_Object = MibTableColumn
hwApOpticalLowRxPowerThreshold = _HwApOpticalLowRxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 66),
    _HwApOpticalLowRxPowerThreshold_Type()
)
hwApOpticalLowRxPowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApOpticalLowRxPowerThreshold.setStatus("current")


class _HwApOpticalHighTemperatureThreshold_Type(Integer32):
    """Custom type hwApOpticalHighTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 125),
    )


_HwApOpticalHighTemperatureThreshold_Type.__name__ = "Integer32"
_HwApOpticalHighTemperatureThreshold_Object = MibTableColumn
hwApOpticalHighTemperatureThreshold = _HwApOpticalHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 67),
    _HwApOpticalHighTemperatureThreshold_Type()
)
hwApOpticalHighTemperatureThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApOpticalHighTemperatureThreshold.setStatus("current")


class _HwApOpticalLowTemperatureThreshold_Type(Integer32):
    """Custom type hwApOpticalLowTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, -5),
    )


_HwApOpticalLowTemperatureThreshold_Type.__name__ = "Integer32"
_HwApOpticalLowTemperatureThreshold_Object = MibTableColumn
hwApOpticalLowTemperatureThreshold = _HwApOpticalLowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 68),
    _HwApOpticalLowTemperatureThreshold_Type()
)
hwApOpticalLowTemperatureThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApOpticalLowTemperatureThreshold.setStatus("current")


class _HwApKeepService_Type(Integer32):
    """Custom type hwApKeepService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowaccess", 3),
          ("disable", 2),
          ("enable", 1))
    )


_HwApKeepService_Type.__name__ = "Integer32"
_HwApKeepService_Object = MibTableColumn
hwApKeepService = _HwApKeepService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 69),
    _HwApKeepService_Type()
)
hwApKeepService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApKeepService.setStatus("current")


class _HwApPriorityAccessMode_Type(Integer32):
    """Custom type hwApPriorityAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwApPriorityAccessMode_Type.__name__ = "Integer32"
_HwApPriorityAccessMode_Object = MibTableColumn
hwApPriorityAccessMode = _HwApPriorityAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 70),
    _HwApPriorityAccessMode_Type()
)
hwApPriorityAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPriorityAccessMode.setStatus("current")


class _HwApLineateportMode_Type(Integer32):
    """Custom type hwApLineateportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpoint", 2),
          ("root", 1))
    )


_HwApLineateportMode_Type.__name__ = "Integer32"
_HwApLineateportMode_Object = MibTableColumn
hwApLineateportMode = _HwApLineateportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 71),
    _HwApLineateportMode_Type()
)
hwApLineateportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineateportMode.setStatus("current")


class _HwApLineateportVlanTagged_Type(OctetString):
    """Custom type hwApLineateportVlanTagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwApLineateportVlanTagged_Type.__name__ = "OctetString"
_HwApLineateportVlanTagged_Object = MibTableColumn
hwApLineateportVlanTagged = _HwApLineateportVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 72),
    _HwApLineateportVlanTagged_Type()
)
hwApLineateportVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineateportVlanTagged.setStatus("current")


class _HwApLineateportVlanUntagged_Type(OctetString):
    """Custom type hwApLineateportVlanUntagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwApLineateportVlanUntagged_Type.__name__ = "OctetString"
_HwApLineateportVlanUntagged_Object = MibTableColumn
hwApLineateportVlanUntagged = _HwApLineateportVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 73),
    _HwApLineateportVlanUntagged_Type()
)
hwApLineateportVlanUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineateportVlanUntagged.setStatus("current")


class _HwApLineateportPvidVlan_Type(Integer32):
    """Custom type hwApLineateportPvidVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwApLineateportPvidVlan_Type.__name__ = "Integer32"
_HwApLineateportPvidVlan_Object = MibTableColumn
hwApLineateportPvidVlan = _HwApLineateportPvidVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 74),
    _HwApLineateportPvidVlan_Type()
)
hwApLineateportPvidVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineateportPvidVlan.setStatus("current")


class _HwApLineateportUserIsolate_Type(Integer32):
    """Custom type hwApLineateportUserIsolate based on Integer32"""
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


_HwApLineateportUserIsolate_Type.__name__ = "Integer32"
_HwApLineateportUserIsolate_Object = MibTableColumn
hwApLineateportUserIsolate = _HwApLineateportUserIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 75),
    _HwApLineateportUserIsolate_Type()
)
hwApLineateportUserIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineateportUserIsolate.setStatus("current")


class _HwApLineateportStpEnable_Type(Integer32):
    """Custom type hwApLineateportStpEnable based on Integer32"""
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


_HwApLineateportStpEnable_Type.__name__ = "Integer32"
_HwApLineateportStpEnable_Object = MibTableColumn
hwApLineateportStpEnable = _HwApLineateportStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 76),
    _HwApLineateportStpEnable_Type()
)
hwApLineateportStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineateportStpEnable.setStatus("current")


class _HwApHighTemperatureThreshold_Type(Integer32):
    """Custom type hwApHighTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 110),
    )


_HwApHighTemperatureThreshold_Type.__name__ = "Integer32"
_HwApHighTemperatureThreshold_Object = MibTableColumn
hwApHighTemperatureThreshold = _HwApHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 77),
    _HwApHighTemperatureThreshold_Type()
)
hwApHighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApHighTemperatureThreshold.setStatus("current")


class _HwApLowTemperatureThreshold_Type(Integer32):
    """Custom type hwApLowTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, 10),
    )


_HwApLowTemperatureThreshold_Type.__name__ = "Integer32"
_HwApLowTemperatureThreshold_Object = MibTableColumn
hwApLowTemperatureThreshold = _HwApLowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 78),
    _HwApLowTemperatureThreshold_Type()
)
hwApLowTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLowTemperatureThreshold.setStatus("current")
_HwApReset_Type = Integer32
_HwApReset_Object = MibTableColumn
hwApReset = _HwApReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 79),
    _HwApReset_Type()
)
hwApReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApReset.setStatus("current")
_HwApStaticIpAddress_Type = IpAddress
_HwApStaticIpAddress_Object = MibTableColumn
hwApStaticIpAddress = _HwApStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 80),
    _HwApStaticIpAddress_Type()
)
hwApStaticIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApStaticIpAddress.setStatus("current")
_HwApStaticNetMask_Type = IpAddress
_HwApStaticNetMask_Object = MibTableColumn
hwApStaticNetMask = _HwApStaticNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 81),
    _HwApStaticNetMask_Type()
)
hwApStaticNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApStaticNetMask.setStatus("current")
_HwApStaticGatewayIp_Type = IpAddress
_HwApStaticGatewayIp_Object = MibTableColumn
hwApStaticGatewayIp = _HwApStaticGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 82),
    _HwApStaticGatewayIp_Type()
)
hwApStaticGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApStaticGatewayIp.setStatus("current")
_HwApAttackFloodInterval_Type = Integer32
_HwApAttackFloodInterval_Object = MibTableColumn
hwApAttackFloodInterval = _HwApAttackFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 83),
    _HwApAttackFloodInterval_Type()
)
hwApAttackFloodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackFloodInterval.setStatus("current")
_HwApAttackFloodTimes_Type = Integer32
_HwApAttackFloodTimes_Object = MibTableColumn
hwApAttackFloodTimes = _HwApAttackFloodTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 84),
    _HwApAttackFloodTimes_Type()
)
hwApAttackFloodTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackFloodTimes.setStatus("current")
_HwApDynamicBlacklistEnable_Type = Integer32
_HwApDynamicBlacklistEnable_Object = MibTableColumn
hwApDynamicBlacklistEnable = _HwApDynamicBlacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 85),
    _HwApDynamicBlacklistEnable_Type()
)
hwApDynamicBlacklistEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApDynamicBlacklistEnable.setStatus("current")
_HwApDynamicBlacklistAgingInt_Type = Integer32
_HwApDynamicBlacklistAgingInt_Object = MibTableColumn
hwApDynamicBlacklistAgingInt = _HwApDynamicBlacklistAgingInt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 86),
    _HwApDynamicBlacklistAgingInt_Type()
)
hwApDynamicBlacklistAgingInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApDynamicBlacklistAgingInt.setStatus("current")
_HwApAttackPskInterval_Type = Integer32
_HwApAttackPskInterval_Object = MibTableColumn
hwApAttackPskInterval = _HwApAttackPskInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 87),
    _HwApAttackPskInterval_Type()
)
hwApAttackPskInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackPskInterval.setStatus("current")
_HwApAttackPskTimes_Type = Integer32
_HwApAttackPskTimes_Object = MibTableColumn
hwApAttackPskTimes = _HwApAttackPskTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 88),
    _HwApAttackPskTimes_Type()
)
hwApAttackPskTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackPskTimes.setStatus("current")


class _HwApAccessBalanceGap_Type(Integer32):
    """Custom type hwApAccessBalanceGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwApAccessBalanceGap_Type.__name__ = "Integer32"
_HwApAccessBalanceGap_Object = MibTableColumn
hwApAccessBalanceGap = _HwApAccessBalanceGap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 89),
    _HwApAccessBalanceGap_Type()
)
hwApAccessBalanceGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAccessBalanceGap.setStatus("current")


class _HwApIpv6Address_Type(OctetString):
    """Custom type hwApIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApIpv6Address_Type.__name__ = "OctetString"
_HwApIpv6Address_Object = MibTableColumn
hwApIpv6Address = _HwApIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 90),
    _HwApIpv6Address_Type()
)
hwApIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApIpv6Address.setStatus("current")


class _HwApIpv6NetMask_Type(OctetString):
    """Custom type hwApIpv6NetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApIpv6NetMask_Type.__name__ = "OctetString"
_HwApIpv6NetMask_Object = MibTableColumn
hwApIpv6NetMask = _HwApIpv6NetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 91),
    _HwApIpv6NetMask_Type()
)
hwApIpv6NetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApIpv6NetMask.setStatus("current")


class _HwApGatewayIpv6_Type(OctetString):
    """Custom type hwApGatewayIpv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApGatewayIpv6_Type.__name__ = "OctetString"
_HwApGatewayIpv6_Object = MibTableColumn
hwApGatewayIpv6 = _HwApGatewayIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 92),
    _HwApGatewayIpv6_Type()
)
hwApGatewayIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApGatewayIpv6.setStatus("current")


class _HwApIpv6DNS_Type(OctetString):
    """Custom type hwApIpv6DNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApIpv6DNS_Type.__name__ = "OctetString"
_HwApIpv6DNS_Object = MibTableColumn
hwApIpv6DNS = _HwApIpv6DNS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 93),
    _HwApIpv6DNS_Type()
)
hwApIpv6DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApIpv6DNS.setStatus("current")


class _HwApProtectAcIPv6Addr_Type(OctetString):
    """Custom type hwApProtectAcIPv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwApProtectAcIPv6Addr_Type.__name__ = "OctetString"
_HwApProtectAcIPv6Addr_Object = MibTableColumn
hwApProtectAcIPv6Addr = _HwApProtectAcIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 94),
    _HwApProtectAcIPv6Addr_Type()
)
hwApProtectAcIPv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApProtectAcIPv6Addr.setStatus("current")
_HwApLineatePortCfgMtu_Type = Integer32
_HwApLineatePortCfgMtu_Object = MibTableColumn
hwApLineatePortCfgMtu = _HwApLineatePortCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 95),
    _HwApLineatePortCfgMtu_Type()
)
hwApLineatePortCfgMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortCfgMtu.setStatus("current")
_HwApLineatePortMacAddress_Type = MacAddress
_HwApLineatePortMacAddress_Object = MibTableColumn
hwApLineatePortMacAddress = _HwApLineatePortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 96),
    _HwApLineatePortMacAddress_Type()
)
hwApLineatePortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortMacAddress.setStatus("current")


class _HwApAccessBalanceSwitch_Type(Integer32):
    """Custom type hwApAccessBalanceSwitch based on Integer32"""
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


_HwApAccessBalanceSwitch_Type.__name__ = "Integer32"
_HwApAccessBalanceSwitch_Object = MibTableColumn
hwApAccessBalanceSwitch = _HwApAccessBalanceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 97),
    _HwApAccessBalanceSwitch_Type()
)
hwApAccessBalanceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApAccessBalanceSwitch.setStatus("current")
_HwApNatIpAddress_Type = OctetString
_HwApNatIpAddress_Object = MibTableColumn
hwApNatIpAddress = _HwApNatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 98),
    _HwApNatIpAddress_Type()
)
hwApNatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApNatIpAddress.setStatus("current")


class _HwApAttackFloodQuietTime_Type(Integer32):
    """Custom type hwApAttackFloodQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwApAttackFloodQuietTime_Type.__name__ = "Integer32"
_HwApAttackFloodQuietTime_Object = MibTableColumn
hwApAttackFloodQuietTime = _HwApAttackFloodQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 99),
    _HwApAttackFloodQuietTime_Type()
)
hwApAttackFloodQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackFloodQuietTime.setStatus("current")


class _HwApAttackPskQuietTime_Type(Integer32):
    """Custom type hwApAttackPskQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwApAttackPskQuietTime_Type.__name__ = "Integer32"
_HwApAttackPskQuietTime_Object = MibTableColumn
hwApAttackPskQuietTime = _HwApAttackPskQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 100),
    _HwApAttackPskQuietTime_Type()
)
hwApAttackPskQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackPskQuietTime.setStatus("current")


class _HwApAttackWeakivQuietTime_Type(Integer32):
    """Custom type hwApAttackWeakivQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwApAttackWeakivQuietTime_Type.__name__ = "Integer32"
_HwApAttackWeakivQuietTime_Object = MibTableColumn
hwApAttackWeakivQuietTime = _HwApAttackWeakivQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 101),
    _HwApAttackWeakivQuietTime_Type()
)
hwApAttackWeakivQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackWeakivQuietTime.setStatus("current")


class _HwApAttackSpoofQuietTime_Type(Integer32):
    """Custom type hwApAttackSpoofQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwApAttackSpoofQuietTime_Type.__name__ = "Integer32"
_HwApAttackSpoofQuietTime_Object = MibTableColumn
hwApAttackSpoofQuietTime = _HwApAttackSpoofQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 102),
    _HwApAttackSpoofQuietTime_Type()
)
hwApAttackSpoofQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApAttackSpoofQuietTime.setStatus("current")
_HwApBootCountTotal_Type = Integer32
_HwApBootCountTotal_Object = MibTableColumn
hwApBootCountTotal = _HwApBootCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 103),
    _HwApBootCountTotal_Type()
)
hwApBootCountTotal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApBootCountTotal.setStatus("current")
_HwApBootCountPowerOff_Type = Integer32
_HwApBootCountPowerOff_Object = MibTableColumn
hwApBootCountPowerOff = _HwApBootCountPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 104),
    _HwApBootCountPowerOff_Type()
)
hwApBootCountPowerOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApBootCountPowerOff.setStatus("current")
_HwApBootCountRowStatus_Type = RowStatus
_HwApBootCountRowStatus_Object = MibTableColumn
hwApBootCountRowStatus = _HwApBootCountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 1, 1, 105),
    _HwApBootCountRowStatus_Type()
)
hwApBootCountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApBootCountRowStatus.setStatus("current")
_HwApLineatePortTable_Object = MibTable
hwApLineatePortTable = _HwApLineatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2)
)
if mibBuilder.loadTexts:
    hwApLineatePortTable.setStatus("current")
_HwApLineatePortEntry_Object = MibTableRow
hwApLineatePortEntry = _HwApLineatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1)
)
hwApLineatePortEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortIndex"),
)
if mibBuilder.loadTexts:
    hwApLineatePortEntry.setStatus("current")
_HwApLineatePortIndex_Type = Integer32
_HwApLineatePortIndex_Object = MibTableColumn
hwApLineatePortIndex = _HwApLineatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 1),
    _HwApLineatePortIndex_Type()
)
hwApLineatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLineatePortIndex.setStatus("current")


class _HwApLineatePortType_Type(Integer32):
    """Custom type hwApLineatePortType based on Integer32"""
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
        *(("adsl2plus", 5),
          ("epon", 4),
          ("fe", 1),
          ("ge", 2),
          ("gpon", 3),
          ("trunk", 6))
    )


_HwApLineatePortType_Type.__name__ = "Integer32"
_HwApLineatePortType_Object = MibTableColumn
hwApLineatePortType = _HwApLineatePortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 2),
    _HwApLineatePortType_Type()
)
hwApLineatePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortType.setStatus("current")
_HwApLineatePortDesc_Type = OctetString
_HwApLineatePortDesc_Object = MibTableColumn
hwApLineatePortDesc = _HwApLineatePortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 3),
    _HwApLineatePortDesc_Type()
)
hwApLineatePortDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortDesc.setStatus("current")


class _HwApLineatePortState_Type(Integer32):
    """Custom type hwApLineatePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("unknown", -1),
          ("up", 2))
    )


_HwApLineatePortState_Type.__name__ = "Integer32"
_HwApLineatePortState_Object = MibTableColumn
hwApLineatePortState = _HwApLineatePortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 4),
    _HwApLineatePortState_Type()
)
hwApLineatePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortState.setStatus("current")
_HwApLineatePortSpeed_Type = Integer32
_HwApLineatePortSpeed_Object = MibTableColumn
hwApLineatePortSpeed = _HwApLineatePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 5),
    _HwApLineatePortSpeed_Type()
)
hwApLineatePortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hwApLineatePortSpeed.setUnits("Mbps")


class _HwApMultiLineatePortDuplex_Type(Integer32):
    """Custom type hwApMultiLineatePortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("unknown", -1))
    )


_HwApMultiLineatePortDuplex_Type.__name__ = "Integer32"
_HwApMultiLineatePortDuplex_Object = MibTableColumn
hwApMultiLineatePortDuplex = _HwApMultiLineatePortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 6),
    _HwApMultiLineatePortDuplex_Type()
)
hwApMultiLineatePortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortDuplex.setStatus("current")


class _HwApMultiLineatePortNegotiation_Type(Integer32):
    """Custom type hwApMultiLineatePortNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forced", 2),
          ("unknown", -1))
    )


_HwApMultiLineatePortNegotiation_Type.__name__ = "Integer32"
_HwApMultiLineatePortNegotiation_Object = MibTableColumn
hwApMultiLineatePortNegotiation = _HwApMultiLineatePortNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 7),
    _HwApMultiLineatePortNegotiation_Type()
)
hwApMultiLineatePortNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMultiLineatePortNegotiation.setStatus("current")


class _HwApMultiLineatePortMode_Type(Integer32):
    """Custom type hwApMultiLineatePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpoint", 2),
          ("root", 1))
    )


_HwApMultiLineatePortMode_Type.__name__ = "Integer32"
_HwApMultiLineatePortMode_Object = MibTableColumn
hwApMultiLineatePortMode = _HwApMultiLineatePortMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 8),
    _HwApMultiLineatePortMode_Type()
)
hwApMultiLineatePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortMode.setStatus("current")


class _HwApMultiLineatePortUserIsolate_Type(Integer32):
    """Custom type hwApMultiLineatePortUserIsolate based on Integer32"""
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


_HwApMultiLineatePortUserIsolate_Type.__name__ = "Integer32"
_HwApMultiLineatePortUserIsolate_Object = MibTableColumn
hwApMultiLineatePortUserIsolate = _HwApMultiLineatePortUserIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 9),
    _HwApMultiLineatePortUserIsolate_Type()
)
hwApMultiLineatePortUserIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortUserIsolate.setStatus("current")


class _HwApMultiLineatePortStpEnable_Type(Integer32):
    """Custom type hwApMultiLineatePortStpEnable based on Integer32"""
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


_HwApMultiLineatePortStpEnable_Type.__name__ = "Integer32"
_HwApMultiLineatePortStpEnable_Object = MibTableColumn
hwApMultiLineatePortStpEnable = _HwApMultiLineatePortStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 10),
    _HwApMultiLineatePortStpEnable_Type()
)
hwApMultiLineatePortStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortStpEnable.setStatus("current")


class _HwApMultiLineatePortVlanTagged_Type(OctetString):
    """Custom type hwApMultiLineatePortVlanTagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwApMultiLineatePortVlanTagged_Type.__name__ = "OctetString"
_HwApMultiLineatePortVlanTagged_Object = MibTableColumn
hwApMultiLineatePortVlanTagged = _HwApMultiLineatePortVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 11),
    _HwApMultiLineatePortVlanTagged_Type()
)
hwApMultiLineatePortVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortVlanTagged.setStatus("current")


class _HwApMultiLineatePortVlanUntagged_Type(OctetString):
    """Custom type hwApMultiLineatePortVlanUntagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwApMultiLineatePortVlanUntagged_Type.__name__ = "OctetString"
_HwApMultiLineatePortVlanUntagged_Object = MibTableColumn
hwApMultiLineatePortVlanUntagged = _HwApMultiLineatePortVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 12),
    _HwApMultiLineatePortVlanUntagged_Type()
)
hwApMultiLineatePortVlanUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortVlanUntagged.setStatus("current")


class _HwApMultiLineatePortPvidVlan_Type(Integer32):
    """Custom type hwApMultiLineatePortPvidVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwApMultiLineatePortPvidVlan_Type.__name__ = "Integer32"
_HwApMultiLineatePortPvidVlan_Object = MibTableColumn
hwApMultiLineatePortPvidVlan = _HwApMultiLineatePortPvidVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 13),
    _HwApMultiLineatePortPvidVlan_Type()
)
hwApMultiLineatePortPvidVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortPvidVlan.setStatus("current")
_HwApMultiLineatePortCRCErrorHighThreshold_Type = Integer32
_HwApMultiLineatePortCRCErrorHighThreshold_Object = MibTableColumn
hwApMultiLineatePortCRCErrorHighThreshold = _HwApMultiLineatePortCRCErrorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 14),
    _HwApMultiLineatePortCRCErrorHighThreshold_Type()
)
hwApMultiLineatePortCRCErrorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortCRCErrorHighThreshold.setStatus("current")
_HwApMultiLineatePortCRCErrorLowThreshold_Type = Integer32
_HwApMultiLineatePortCRCErrorLowThreshold_Object = MibTableColumn
hwApMultiLineatePortCRCErrorLowThreshold = _HwApMultiLineatePortCRCErrorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 15),
    _HwApMultiLineatePortCRCErrorLowThreshold_Type()
)
hwApMultiLineatePortCRCErrorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortCRCErrorLowThreshold.setStatus("current")


class _HwApMultiLineatePortCRCErrorSwitch_Type(Integer32):
    """Custom type hwApMultiLineatePortCRCErrorSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("unknown", -1))
    )


_HwApMultiLineatePortCRCErrorSwitch_Type.__name__ = "Integer32"
_HwApMultiLineatePortCRCErrorSwitch_Object = MibTableColumn
hwApMultiLineatePortCRCErrorSwitch = _HwApMultiLineatePortCRCErrorSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 16),
    _HwApMultiLineatePortCRCErrorSwitch_Type()
)
hwApMultiLineatePortCRCErrorSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortCRCErrorSwitch.setStatus("current")
_HwApLineatePortAclNumInbound_Type = Integer32
_HwApLineatePortAclNumInbound_Object = MibTableColumn
hwApLineatePortAclNumInbound = _HwApLineatePortAclNumInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 17),
    _HwApLineatePortAclNumInbound_Type()
)
hwApLineatePortAclNumInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNumInbound.setStatus("current")
_HwApLineatePortAclNumOutbound_Type = Integer32
_HwApLineatePortAclNumOutbound_Object = MibTableColumn
hwApLineatePortAclNumOutbound = _HwApLineatePortAclNumOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 18),
    _HwApLineatePortAclNumOutbound_Type()
)
hwApLineatePortAclNumOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNumOutbound.setStatus("current")
_HwApLineatePortAclNameInbound_Type = OctetString
_HwApLineatePortAclNameInbound_Object = MibTableColumn
hwApLineatePortAclNameInbound = _HwApLineatePortAclNameInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 19),
    _HwApLineatePortAclNameInbound_Type()
)
hwApLineatePortAclNameInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNameInbound.setStatus("current")
_HwApLineatePortAclNameOutbound_Type = OctetString
_HwApLineatePortAclNameOutbound_Object = MibTableColumn
hwApLineatePortAclNameOutbound = _HwApLineatePortAclNameOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 20),
    _HwApLineatePortAclNameOutbound_Type()
)
hwApLineatePortAclNameOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNameOutbound.setStatus("current")


class _HwApLineatePortAclSwitchInbound_Type(Integer32):
    """Custom type hwApLineatePortAclSwitchInbound based on Integer32"""
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


_HwApLineatePortAclSwitchInbound_Type.__name__ = "Integer32"
_HwApLineatePortAclSwitchInbound_Object = MibTableColumn
hwApLineatePortAclSwitchInbound = _HwApLineatePortAclSwitchInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 21),
    _HwApLineatePortAclSwitchInbound_Type()
)
hwApLineatePortAclSwitchInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclSwitchInbound.setStatus("current")


class _HwApLineatePortAclSwitchOutbound_Type(Integer32):
    """Custom type hwApLineatePortAclSwitchOutbound based on Integer32"""
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


_HwApLineatePortAclSwitchOutbound_Type.__name__ = "Integer32"
_HwApLineatePortAclSwitchOutbound_Object = MibTableColumn
hwApLineatePortAclSwitchOutbound = _HwApLineatePortAclSwitchOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 22),
    _HwApLineatePortAclSwitchOutbound_Type()
)
hwApLineatePortAclSwitchOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclSwitchOutbound.setStatus("current")
_HwApLineatePortAclNumInboundIPV6_Type = Integer32
_HwApLineatePortAclNumInboundIPV6_Object = MibTableColumn
hwApLineatePortAclNumInboundIPV6 = _HwApLineatePortAclNumInboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 23),
    _HwApLineatePortAclNumInboundIPV6_Type()
)
hwApLineatePortAclNumInboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNumInboundIPV6.setStatus("current")
_HwApLineatePortAclNumOutboundIPV6_Type = Integer32
_HwApLineatePortAclNumOutboundIPV6_Object = MibTableColumn
hwApLineatePortAclNumOutboundIPV6 = _HwApLineatePortAclNumOutboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 24),
    _HwApLineatePortAclNumOutboundIPV6_Type()
)
hwApLineatePortAclNumOutboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNumOutboundIPV6.setStatus("current")
_HwApLineatePortAclNameInboundIPV6_Type = OctetString
_HwApLineatePortAclNameInboundIPV6_Object = MibTableColumn
hwApLineatePortAclNameInboundIPV6 = _HwApLineatePortAclNameInboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 25),
    _HwApLineatePortAclNameInboundIPV6_Type()
)
hwApLineatePortAclNameInboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNameInboundIPV6.setStatus("current")
_HwApLineatePortAclNameOutboundIPV6_Type = OctetString
_HwApLineatePortAclNameOutboundIPV6_Object = MibTableColumn
hwApLineatePortAclNameOutboundIPV6 = _HwApLineatePortAclNameOutboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 26),
    _HwApLineatePortAclNameOutboundIPV6_Type()
)
hwApLineatePortAclNameOutboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclNameOutboundIPV6.setStatus("current")


class _HwApLineatePortAclSwitchInboundIPV6_Type(Integer32):
    """Custom type hwApLineatePortAclSwitchInboundIPV6 based on Integer32"""
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


_HwApLineatePortAclSwitchInboundIPV6_Type.__name__ = "Integer32"
_HwApLineatePortAclSwitchInboundIPV6_Object = MibTableColumn
hwApLineatePortAclSwitchInboundIPV6 = _HwApLineatePortAclSwitchInboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 27),
    _HwApLineatePortAclSwitchInboundIPV6_Type()
)
hwApLineatePortAclSwitchInboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclSwitchInboundIPV6.setStatus("current")


class _HwApLineatePortAclSwitchOutboundIPV6_Type(Integer32):
    """Custom type hwApLineatePortAclSwitchOutboundIPV6 based on Integer32"""
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


_HwApLineatePortAclSwitchOutboundIPV6_Type.__name__ = "Integer32"
_HwApLineatePortAclSwitchOutboundIPV6_Object = MibTableColumn
hwApLineatePortAclSwitchOutboundIPV6 = _HwApLineatePortAclSwitchOutboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 28),
    _HwApLineatePortAclSwitchOutboundIPV6_Type()
)
hwApLineatePortAclSwitchOutboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortAclSwitchOutboundIPV6.setStatus("current")


class _HwApMultiLineatePortIsAddInTrunk_Type(Integer32):
    """Custom type hwApMultiLineatePortIsAddInTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("exit", 1),
          ("unknow", -1))
    )


_HwApMultiLineatePortIsAddInTrunk_Type.__name__ = "Integer32"
_HwApMultiLineatePortIsAddInTrunk_Object = MibTableColumn
hwApMultiLineatePortIsAddInTrunk = _HwApMultiLineatePortIsAddInTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 29),
    _HwApMultiLineatePortIsAddInTrunk_Type()
)
hwApMultiLineatePortIsAddInTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortIsAddInTrunk.setStatus("current")


class _HwApMultiLineatePortAddedOrExitTrunkID_Type(Integer32):
    """Custom type hwApMultiLineatePortAddedOrExitTrunkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_HwApMultiLineatePortAddedOrExitTrunkID_Type.__name__ = "Integer32"
_HwApMultiLineatePortAddedOrExitTrunkID_Object = MibTableColumn
hwApMultiLineatePortAddedOrExitTrunkID = _HwApMultiLineatePortAddedOrExitTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 2, 1, 30),
    _HwApMultiLineatePortAddedOrExitTrunkID_Type()
)
hwApMultiLineatePortAddedOrExitTrunkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApMultiLineatePortAddedOrExitTrunkID.setStatus("current")
_HwApGlobalInfo_ObjectIdentity = ObjectIdentity
hwApGlobalInfo = _HwApGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 3)
)
_HwApAllExistApIndexMask_Type = OctetString
_HwApAllExistApIndexMask_Object = MibScalar
hwApAllExistApIndexMask = _HwApAllExistApIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 3, 1),
    _HwApAllExistApIndexMask_Type()
)
hwApAllExistApIndexMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAllExistApIndexMask.setStatus("current")
_HwUnAuthorizedApRecordNumber_Type = Integer32
_HwUnAuthorizedApRecordNumber_Object = MibScalar
hwUnAuthorizedApRecordNumber = _HwUnAuthorizedApRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 3, 2),
    _HwUnAuthorizedApRecordNumber_Type()
)
hwUnAuthorizedApRecordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUnAuthorizedApRecordNumber.setStatus("current")


class _HwUnAuthorizedApRecordAdmin_Type(Integer32):
    """Custom type hwUnAuthorizedApRecordAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwUnAuthorizedApRecordAdmin_Type.__name__ = "Integer32"
_HwUnAuthorizedApRecordAdmin_Object = MibScalar
hwUnAuthorizedApRecordAdmin = _HwUnAuthorizedApRecordAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 3, 3),
    _HwUnAuthorizedApRecordAdmin_Type()
)
hwUnAuthorizedApRecordAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUnAuthorizedApRecordAdmin.setStatus("current")


class _HwApResetAllOnlineFailRecord_Type(Integer32):
    """Custom type hwApResetAllOnlineFailRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unknown", -1))
    )


_HwApResetAllOnlineFailRecord_Type.__name__ = "Integer32"
_HwApResetAllOnlineFailRecord_Object = MibScalar
hwApResetAllOnlineFailRecord = _HwApResetAllOnlineFailRecord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 3, 4),
    _HwApResetAllOnlineFailRecord_Type()
)
hwApResetAllOnlineFailRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApResetAllOnlineFailRecord.setStatus("current")


class _HwApResetAllOfflineRecord_Type(Integer32):
    """Custom type hwApResetAllOfflineRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwApResetAllOfflineRecord_Type.__name__ = "Integer32"
_HwApResetAllOfflineRecord_Object = MibScalar
hwApResetAllOfflineRecord = _HwApResetAllOfflineRecord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 3, 5),
    _HwApResetAllOfflineRecord_Type()
)
hwApResetAllOfflineRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApResetAllOfflineRecord.setStatus("current")


class _HwApResetAllBootCountRecord_Type(Integer32):
    """Custom type hwApResetAllBootCountRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwApResetAllBootCountRecord_Type.__name__ = "Integer32"
_HwApResetAllBootCountRecord_Object = MibScalar
hwApResetAllBootCountRecord = _HwApResetAllBootCountRecord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 3, 6),
    _HwApResetAllBootCountRecord_Type()
)
hwApResetAllBootCountRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApResetAllBootCountRecord.setStatus("current")
_HwApBatchInfo_ObjectIdentity = ObjectIdentity
hwApBatchInfo = _HwApBatchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 4)
)
_HwApBatchIndexStart_Type = Integer32
_HwApBatchIndexStart_Object = MibScalar
hwApBatchIndexStart = _HwApBatchIndexStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 4, 1),
    _HwApBatchIndexStart_Type()
)
hwApBatchIndexStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApBatchIndexStart.setStatus("current")
_HwApBatchIndexNumber_Type = Integer32
_HwApBatchIndexNumber_Object = MibScalar
hwApBatchIndexNumber = _HwApBatchIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 4, 2),
    _HwApBatchIndexNumber_Type()
)
hwApBatchIndexNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApBatchIndexNumber.setStatus("current")
_HwApBatchIndexReturnNumber_Type = Integer32
_HwApBatchIndexReturnNumber_Object = MibScalar
hwApBatchIndexReturnNumber = _HwApBatchIndexReturnNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 4, 3),
    _HwApBatchIndexReturnNumber_Type()
)
hwApBatchIndexReturnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApBatchIndexReturnNumber.setStatus("current")
_HwApBatchState_Type = OctetString
_HwApBatchState_Object = MibScalar
hwApBatchState = _HwApBatchState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 4, 4),
    _HwApBatchState_Type()
)
hwApBatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApBatchState.setStatus("current")
_HwApBatchNameList_Type = OctetString
_HwApBatchNameList_Object = MibScalar
hwApBatchNameList = _HwApBatchNameList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 4, 5),
    _HwApBatchNameList_Type()
)
hwApBatchNameList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApBatchNameList.setStatus("current")
_HwApPing_ObjectIdentity = ObjectIdentity
hwApPing = _HwApPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5)
)
_HwApPingIndex_Type = Integer32
_HwApPingIndex_Object = MibScalar
hwApPingIndex = _HwApPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 1),
    _HwApPingIndex_Type()
)
hwApPingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPingIndex.setStatus("current")
_HwApPingAddress_Type = OctetString
_HwApPingAddress_Object = MibScalar
hwApPingAddress = _HwApPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 2),
    _HwApPingAddress_Type()
)
hwApPingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPingAddress.setStatus("current")
_HwApPingCount_Type = Integer32
_HwApPingCount_Object = MibScalar
hwApPingCount = _HwApPingCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 3),
    _HwApPingCount_Type()
)
hwApPingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPingCount.setStatus("current")
_HwApPingPacketSize_Type = Integer32
_HwApPingPacketSize_Object = MibScalar
hwApPingPacketSize = _HwApPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 4),
    _HwApPingPacketSize_Type()
)
hwApPingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPingPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    hwApPingPacketSize.setUnits("Bytes")
_HwApPingWaitTime_Type = Integer32
_HwApPingWaitTime_Object = MibScalar
hwApPingWaitTime = _HwApPingWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 5),
    _HwApPingWaitTime_Type()
)
hwApPingWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPingWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    hwApPingWaitTime.setUnits("ms")
_HwApPingTimeOut_Type = Integer32
_HwApPingTimeOut_Object = MibScalar
hwApPingTimeOut = _HwApPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 6),
    _HwApPingTimeOut_Type()
)
hwApPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    hwApPingTimeOut.setUnits("ms")
_HwApPingResultSuccessCount_Type = Integer32
_HwApPingResultSuccessCount_Object = MibScalar
hwApPingResultSuccessCount = _HwApPingResultSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 7),
    _HwApPingResultSuccessCount_Type()
)
hwApPingResultSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPingResultSuccessCount.setStatus("current")
_HwApPingResultFailureCount_Type = Integer32
_HwApPingResultFailureCount_Object = MibScalar
hwApPingResultFailureCount = _HwApPingResultFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 8),
    _HwApPingResultFailureCount_Type()
)
hwApPingResultFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPingResultFailureCount.setStatus("current")
_HwApPingResultAverageResponseTime_Type = Integer32
_HwApPingResultAverageResponseTime_Object = MibScalar
hwApPingResultAverageResponseTime = _HwApPingResultAverageResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 9),
    _HwApPingResultAverageResponseTime_Type()
)
hwApPingResultAverageResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPingResultAverageResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    hwApPingResultAverageResponseTime.setUnits("ms")
_HwApPingResultMinimumResponseTime_Type = Integer32
_HwApPingResultMinimumResponseTime_Object = MibScalar
hwApPingResultMinimumResponseTime = _HwApPingResultMinimumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 10),
    _HwApPingResultMinimumResponseTime_Type()
)
hwApPingResultMinimumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPingResultMinimumResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    hwApPingResultMinimumResponseTime.setUnits("ms")
_HwApPingResultMaximumResponseTime_Type = Integer32
_HwApPingResultMaximumResponseTime_Object = MibScalar
hwApPingResultMaximumResponseTime = _HwApPingResultMaximumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 11),
    _HwApPingResultMaximumResponseTime_Type()
)
hwApPingResultMaximumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPingResultMaximumResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    hwApPingResultMaximumResponseTime.setUnits("ms")
_HwApPingApMac_Type = MacAddress
_HwApPingApMac_Object = MibScalar
hwApPingApMac = _HwApPingApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 12),
    _HwApPingApMac_Type()
)
hwApPingApMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPingApMac.setStatus("current")


class _HwApPingResultFlag_Type(Integer32):
    """Custom type hwApPingResultFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_HwApPingResultFlag_Type.__name__ = "Integer32"
_HwApPingResultFlag_Object = MibScalar
hwApPingResultFlag = _HwApPingResultFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 5, 13),
    _HwApPingResultFlag_Type()
)
hwApPingResultFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApPingResultFlag.setStatus("current")
_HwApPerformanceStatTable_Object = MibTable
hwApPerformanceStatTable = _HwApPerformanceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6)
)
if mibBuilder.loadTexts:
    hwApPerformanceStatTable.setStatus("current")
_HwApPerformanceStatEntry_Object = MibTableRow
hwApPerformanceStatEntry = _HwApPerformanceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1)
)
hwApPerformanceStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
)
if mibBuilder.loadTexts:
    hwApPerformanceStatEntry.setStatus("current")
_HwApMemoryUseRate_Type = Integer32
_HwApMemoryUseRate_Object = MibTableColumn
hwApMemoryUseRate = _HwApMemoryUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 1),
    _HwApMemoryUseRate_Type()
)
hwApMemoryUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApMemoryUseRate.setStatus("current")
if mibBuilder.loadTexts:
    hwApMemoryUseRate.setUnits("%")
_HwApCpuUseRate_Type = Integer32
_HwApCpuUseRate_Object = MibTableColumn
hwApCpuUseRate = _HwApCpuUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 2),
    _HwApCpuUseRate_Type()
)
hwApCpuUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApCpuUseRate.setStatus("current")
if mibBuilder.loadTexts:
    hwApCpuUseRate.setUnits("%")
_HwApFlashFreeSize_Type = Integer32
_HwApFlashFreeSize_Object = MibTableColumn
hwApFlashFreeSize = _HwApFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 3),
    _HwApFlashFreeSize_Type()
)
hwApFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApFlashFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hwApFlashFreeSize.setUnits("kb")
_HwApTemperature_Type = Integer32
_HwApTemperature_Object = MibTableColumn
hwApTemperature = _HwApTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 4),
    _HwApTemperature_Type()
)
hwApTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApTemperature.setStatus("current")
if mibBuilder.loadTexts:
    hwApTemperature.setUnits("C")
_HwApOnlineUserNum_Type = Integer32
_HwApOnlineUserNum_Object = MibTableColumn
hwApOnlineUserNum = _HwApOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 5),
    _HwApOnlineUserNum_Type()
)
hwApOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOnlineUserNum.setStatus("current")
_HwApUpPortSpeed_Type = Integer32
_HwApUpPortSpeed_Object = MibTableColumn
hwApUpPortSpeed = _HwApUpPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 6),
    _HwApUpPortSpeed_Type()
)
hwApUpPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hwApUpPortSpeed.setUnits("Mbps")
_HwApUpPortRecvFrames_Type = Unsigned32
_HwApUpPortRecvFrames_Object = MibTableColumn
hwApUpPortRecvFrames = _HwApUpPortRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 7),
    _HwApUpPortRecvFrames_Type()
)
hwApUpPortRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvFrames.setStatus("current")
_HwApUpPortRecvRightFrames_Type = Unsigned32
_HwApUpPortRecvRightFrames_Object = MibTableColumn
hwApUpPortRecvRightFrames = _HwApUpPortRecvRightFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 8),
    _HwApUpPortRecvRightFrames_Type()
)
hwApUpPortRecvRightFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvRightFrames.setStatus("current")
_HwApUpPortRecvErrorFrames_Type = Unsigned32
_HwApUpPortRecvErrorFrames_Object = MibTableColumn
hwApUpPortRecvErrorFrames = _HwApUpPortRecvErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 9),
    _HwApUpPortRecvErrorFrames_Type()
)
hwApUpPortRecvErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvErrorFrames.setStatus("current")
_HwApUpPortSendFrames_Type = Unsigned32
_HwApUpPortSendFrames_Object = MibTableColumn
hwApUpPortSendFrames = _HwApUpPortSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 10),
    _HwApUpPortSendFrames_Type()
)
hwApUpPortSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortSendFrames.setStatus("current")
_HwApUpPortRecvBytes_Type = Unsigned32
_HwApUpPortRecvBytes_Object = MibTableColumn
hwApUpPortRecvBytes = _HwApUpPortRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 11),
    _HwApUpPortRecvBytes_Type()
)
hwApUpPortRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvBytes.setStatus("current")
_HwApUpPortSendBytes_Type = Unsigned32
_HwApUpPortSendBytes_Object = MibTableColumn
hwApUpPortSendBytes = _HwApUpPortSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 12),
    _HwApUpPortSendBytes_Type()
)
hwApUpPortSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortSendBytes.setStatus("current")
_HwAPUpPortPER_Type = Integer32
_HwAPUpPortPER_Object = MibTableColumn
hwAPUpPortPER = _HwAPUpPortPER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 13),
    _HwAPUpPortPER_Type()
)
hwAPUpPortPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAPUpPortPER.setStatus("current")
if mibBuilder.loadTexts:
    hwAPUpPortPER.setUnits("%")
_HwAPWirelessUpPortTraffic_Type = Unsigned32
_HwAPWirelessUpPortTraffic_Object = MibTableColumn
hwAPWirelessUpPortTraffic = _HwAPWirelessUpPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 14),
    _HwAPWirelessUpPortTraffic_Type()
)
hwAPWirelessUpPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAPWirelessUpPortTraffic.setStatus("current")
_HwAPUpPortTraffic_Type = Unsigned32
_HwAPUpPortTraffic_Object = MibTableColumn
hwAPUpPortTraffic = _HwAPUpPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 15),
    _HwAPUpPortTraffic_Type()
)
hwAPUpPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAPUpPortTraffic.setStatus("current")
_HwApAirportSendDropFrames_Type = Unsigned32
_HwApAirportSendDropFrames_Object = MibTableColumn
hwApAirportSendDropFrames = _HwApAirportSendDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 16),
    _HwApAirportSendDropFrames_Type()
)
hwApAirportSendDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportSendDropFrames.setStatus("current")
_HwApEthportRecvDropFrames_Type = Unsigned32
_HwApEthportRecvDropFrames_Object = MibTableColumn
hwApEthportRecvDropFrames = _HwApEthportRecvDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 17),
    _HwApEthportRecvDropFrames_Type()
)
hwApEthportRecvDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportRecvDropFrames.setStatus("current")
_HwApAirportUpTraffic_Type = OctetString
_HwApAirportUpTraffic_Object = MibTableColumn
hwApAirportUpTraffic = _HwApAirportUpTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 18),
    _HwApAirportUpTraffic_Type()
)
hwApAirportUpTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportUpTraffic.setStatus("current")
_HwApAirportDwTraffic_Type = OctetString
_HwApAirportDwTraffic_Object = MibTableColumn
hwApAirportDwTraffic = _HwApAirportDwTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 19),
    _HwApAirportDwTraffic_Type()
)
hwApAirportDwTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportDwTraffic.setStatus("current")
_HwApEthportDwTraffic_Type = OctetString
_HwApEthportDwTraffic_Object = MibTableColumn
hwApEthportDwTraffic = _HwApEthportDwTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 20),
    _HwApEthportDwTraffic_Type()
)
hwApEthportDwTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportDwTraffic.setStatus("current")
_HwApEthportUpTraffic_Type = OctetString
_HwApEthportUpTraffic_Object = MibTableColumn
hwApEthportUpTraffic = _HwApEthportUpTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 21),
    _HwApEthportUpTraffic_Type()
)
hwApEthportUpTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportUpTraffic.setStatus("current")
_HwApAirportRecvDropPacket_Type = Unsigned32
_HwApAirportRecvDropPacket_Object = MibTableColumn
hwApAirportRecvDropPacket = _HwApAirportRecvDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 22),
    _HwApAirportRecvDropPacket_Type()
)
hwApAirportRecvDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportRecvDropPacket.setStatus("current")
_HwApAirportRecvErrorPacket_Type = Unsigned32
_HwApAirportRecvErrorPacket_Object = MibTableColumn
hwApAirportRecvErrorPacket = _HwApAirportRecvErrorPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 23),
    _HwApAirportRecvErrorPacket_Type()
)
hwApAirportRecvErrorPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportRecvErrorPacket.setStatus("current")
_HwApEthportRecvUnicastPacket_Type = Unsigned32
_HwApEthportRecvUnicastPacket_Object = MibTableColumn
hwApEthportRecvUnicastPacket = _HwApEthportRecvUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 24),
    _HwApEthportRecvUnicastPacket_Type()
)
hwApEthportRecvUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportRecvUnicastPacket.setStatus("current")
_HwApEthportRecvNonUnicastPacket_Type = Unsigned32
_HwApEthportRecvNonUnicastPacket_Object = MibTableColumn
hwApEthportRecvNonUnicastPacket = _HwApEthportRecvNonUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 25),
    _HwApEthportRecvNonUnicastPacket_Type()
)
hwApEthportRecvNonUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportRecvNonUnicastPacket.setStatus("current")
_HwApEthportSendUnicastPacket_Type = Unsigned32
_HwApEthportSendUnicastPacket_Object = MibTableColumn
hwApEthportSendUnicastPacket = _HwApEthportSendUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 26),
    _HwApEthportSendUnicastPacket_Type()
)
hwApEthportSendUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportSendUnicastPacket.setStatus("current")
_HwApEthportSendNonUnicastPacket_Type = Unsigned32
_HwApEthportSendNonUnicastPacket_Object = MibTableColumn
hwApEthportSendNonUnicastPacket = _HwApEthportSendNonUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 27),
    _HwApEthportSendNonUnicastPacket_Type()
)
hwApEthportSendNonUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportSendNonUnicastPacket.setStatus("current")
_HwApAvgRCPUUseRate_Type = Integer32
_HwApAvgRCPUUseRate_Object = MibTableColumn
hwApAvgRCPUUseRate = _HwApAvgRCPUUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 28),
    _HwApAvgRCPUUseRate_Type()
)
hwApAvgRCPUUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAvgRCPUUseRate.setStatus("current")
_HwApAvgRMemoryUseRate_Type = Integer32
_HwApAvgRMemoryUseRate_Object = MibTableColumn
hwApAvgRMemoryUseRate = _HwApAvgRMemoryUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 29),
    _HwApAvgRMemoryUseRate_Type()
)
hwApAvgRMemoryUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAvgRMemoryUseRate.setStatus("current")
_HwEthportSendDropFrames_Type = Counter64
_HwEthportSendDropFrames_Object = MibTableColumn
hwEthportSendDropFrames = _HwEthportSendDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 30),
    _HwEthportSendDropFrames_Type()
)
hwEthportSendDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthportSendDropFrames.setStatus("current")
_HwEthportSendErrorFrames_Type = Counter64
_HwEthportSendErrorFrames_Object = MibTableColumn
hwEthportSendErrorFrames = _HwEthportSendErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 31),
    _HwEthportSendErrorFrames_Type()
)
hwEthportSendErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthportSendErrorFrames.setStatus("current")
_HwEthportUpDwnTimes_Type = Unsigned32
_HwEthportUpDwnTimes_Object = MibTableColumn
hwEthportUpDwnTimes = _HwEthportUpDwnTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 32),
    _HwEthportUpDwnTimes_Type()
)
hwEthportUpDwnTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthportUpDwnTimes.setStatus("current")
_HwApAirportRecvUnicastFrames_Type = Counter64
_HwApAirportRecvUnicastFrames_Object = MibTableColumn
hwApAirportRecvUnicastFrames = _HwApAirportRecvUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 33),
    _HwApAirportRecvUnicastFrames_Type()
)
hwApAirportRecvUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportRecvUnicastFrames.setStatus("current")
_HwApEthportRecvUnknownFrames_Type = Counter64
_HwApEthportRecvUnknownFrames_Object = MibTableColumn
hwApEthportRecvUnknownFrames = _HwApEthportRecvUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 34),
    _HwApEthportRecvUnknownFrames_Type()
)
hwApEthportRecvUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportRecvUnknownFrames.setStatus("current")
_HwApEthportUpRate_Type = Integer32
_HwApEthportUpRate_Object = MibTableColumn
hwApEthportUpRate = _HwApEthportUpRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 35),
    _HwApEthportUpRate_Type()
)
hwApEthportUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportUpRate.setStatus("current")
_HwApEthportDownRate_Type = Integer32
_HwApEthportDownRate_Object = MibTableColumn
hwApEthportDownRate = _HwApEthportDownRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 36),
    _HwApEthportDownRate_Type()
)
hwApEthportDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportDownRate.setStatus("current")
_HwApUpPortRecvFrames64Bits_Type = Counter64
_HwApUpPortRecvFrames64Bits_Object = MibTableColumn
hwApUpPortRecvFrames64Bits = _HwApUpPortRecvFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 37),
    _HwApUpPortRecvFrames64Bits_Type()
)
hwApUpPortRecvFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvFrames64Bits.setStatus("current")
_HwApUpPortRecvRightFrames64Bits_Type = Counter64
_HwApUpPortRecvRightFrames64Bits_Object = MibTableColumn
hwApUpPortRecvRightFrames64Bits = _HwApUpPortRecvRightFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 38),
    _HwApUpPortRecvRightFrames64Bits_Type()
)
hwApUpPortRecvRightFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvRightFrames64Bits.setStatus("current")
_HwApUpPortRecvErrorFrames64Bits_Type = Counter64
_HwApUpPortRecvErrorFrames64Bits_Object = MibTableColumn
hwApUpPortRecvErrorFrames64Bits = _HwApUpPortRecvErrorFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 39),
    _HwApUpPortRecvErrorFrames64Bits_Type()
)
hwApUpPortRecvErrorFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvErrorFrames64Bits.setStatus("current")
_HwApUpPortSendFrames64Bits_Type = Counter64
_HwApUpPortSendFrames64Bits_Object = MibTableColumn
hwApUpPortSendFrames64Bits = _HwApUpPortSendFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 40),
    _HwApUpPortSendFrames64Bits_Type()
)
hwApUpPortSendFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortSendFrames64Bits.setStatus("current")
_HwApUpPortRecvBytes64Bits_Type = Counter64
_HwApUpPortRecvBytes64Bits_Object = MibTableColumn
hwApUpPortRecvBytes64Bits = _HwApUpPortRecvBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 41),
    _HwApUpPortRecvBytes64Bits_Type()
)
hwApUpPortRecvBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortRecvBytes64Bits.setStatus("current")
_HwApUpPortSendBytes64Bits_Type = Counter64
_HwApUpPortSendBytes64Bits_Object = MibTableColumn
hwApUpPortSendBytes64Bits = _HwApUpPortSendBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 42),
    _HwApUpPortSendBytes64Bits_Type()
)
hwApUpPortSendBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUpPortSendBytes64Bits.setStatus("current")
_HwAPWirelessUpPortTraffic64Bits_Type = Counter64
_HwAPWirelessUpPortTraffic64Bits_Object = MibTableColumn
hwAPWirelessUpPortTraffic64Bits = _HwAPWirelessUpPortTraffic64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 43),
    _HwAPWirelessUpPortTraffic64Bits_Type()
)
hwAPWirelessUpPortTraffic64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAPWirelessUpPortTraffic64Bits.setStatus("current")
_HwAPUpPortTraffic64Bits_Type = Counter64
_HwAPUpPortTraffic64Bits_Object = MibTableColumn
hwAPUpPortTraffic64Bits = _HwAPUpPortTraffic64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 44),
    _HwAPUpPortTraffic64Bits_Type()
)
hwAPUpPortTraffic64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAPUpPortTraffic64Bits.setStatus("current")
_HwApAirportSendDropFrames64Bits_Type = Counter64
_HwApAirportSendDropFrames64Bits_Object = MibTableColumn
hwApAirportSendDropFrames64Bits = _HwApAirportSendDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 45),
    _HwApAirportSendDropFrames64Bits_Type()
)
hwApAirportSendDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportSendDropFrames64Bits.setStatus("current")
_HwApEthportRecvDropFrames64Bits_Type = Counter64
_HwApEthportRecvDropFrames64Bits_Object = MibTableColumn
hwApEthportRecvDropFrames64Bits = _HwApEthportRecvDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 46),
    _HwApEthportRecvDropFrames64Bits_Type()
)
hwApEthportRecvDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportRecvDropFrames64Bits.setStatus("current")
_HwApAirportRecvDropPacket64Bits_Type = Counter64
_HwApAirportRecvDropPacket64Bits_Object = MibTableColumn
hwApAirportRecvDropPacket64Bits = _HwApAirportRecvDropPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 47),
    _HwApAirportRecvDropPacket64Bits_Type()
)
hwApAirportRecvDropPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportRecvDropPacket64Bits.setStatus("current")
_HwApAirportRecvErrorPacket64Bits_Type = Counter64
_HwApAirportRecvErrorPacket64Bits_Object = MibTableColumn
hwApAirportRecvErrorPacket64Bits = _HwApAirportRecvErrorPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 48),
    _HwApAirportRecvErrorPacket64Bits_Type()
)
hwApAirportRecvErrorPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApAirportRecvErrorPacket64Bits.setStatus("current")
_HwApEthportRecvUnicastPacket64Bits_Type = Counter64
_HwApEthportRecvUnicastPacket64Bits_Object = MibTableColumn
hwApEthportRecvUnicastPacket64Bits = _HwApEthportRecvUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 49),
    _HwApEthportRecvUnicastPacket64Bits_Type()
)
hwApEthportRecvUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportRecvUnicastPacket64Bits.setStatus("current")
_HwApEthportRecvNonUnicastPacket64Bits_Type = Counter64
_HwApEthportRecvNonUnicastPacket64Bits_Object = MibTableColumn
hwApEthportRecvNonUnicastPacket64Bits = _HwApEthportRecvNonUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 50),
    _HwApEthportRecvNonUnicastPacket64Bits_Type()
)
hwApEthportRecvNonUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportRecvNonUnicastPacket64Bits.setStatus("current")
_HwApEthportSendUnicastPacket64Bits_Type = Counter64
_HwApEthportSendUnicastPacket64Bits_Object = MibTableColumn
hwApEthportSendUnicastPacket64Bits = _HwApEthportSendUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 51),
    _HwApEthportSendUnicastPacket64Bits_Type()
)
hwApEthportSendUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportSendUnicastPacket64Bits.setStatus("current")
_HwApEthportSendNonUnicastPacket64Bits_Type = Counter64
_HwApEthportSendNonUnicastPacket64Bits_Object = MibTableColumn
hwApEthportSendNonUnicastPacket64Bits = _HwApEthportSendNonUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 6, 1, 52),
    _HwApEthportSendNonUnicastPacket64Bits_Type()
)
hwApEthportSendNonUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApEthportSendNonUnicastPacket64Bits.setStatus("current")
_HwApUnauthorizedApRecordTable_Object = MibTable
hwApUnauthorizedApRecordTable = _HwApUnauthorizedApRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7)
)
if mibBuilder.loadTexts:
    hwApUnauthorizedApRecordTable.setStatus("current")
_HwApUnauthorizedApRecordEntry_Object = MibTableRow
hwApUnauthorizedApRecordEntry = _HwApUnauthorizedApRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7, 1)
)
hwApUnauthorizedApRecordEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApUnauthorizedApRecordIndex"),
)
if mibBuilder.loadTexts:
    hwApUnauthorizedApRecordEntry.setStatus("current")
_HwApUnauthorizedApRecordIndex_Type = Integer32
_HwApUnauthorizedApRecordIndex_Object = MibTableColumn
hwApUnauthorizedApRecordIndex = _HwApUnauthorizedApRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7, 1, 1),
    _HwApUnauthorizedApRecordIndex_Type()
)
hwApUnauthorizedApRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApUnauthorizedApRecordIndex.setStatus("current")
_HwApUnauthorizedApType_Type = OctetString
_HwApUnauthorizedApType_Object = MibTableColumn
hwApUnauthorizedApType = _HwApUnauthorizedApType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7, 1, 2),
    _HwApUnauthorizedApType_Type()
)
hwApUnauthorizedApType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUnauthorizedApType.setStatus("current")
_HwApUnauthorizedApMacAddress_Type = MacAddress
_HwApUnauthorizedApMacAddress_Object = MibTableColumn
hwApUnauthorizedApMacAddress = _HwApUnauthorizedApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7, 1, 3),
    _HwApUnauthorizedApMacAddress_Type()
)
hwApUnauthorizedApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUnauthorizedApMacAddress.setStatus("current")
_HwApUnauthorizedApSn_Type = OctetString
_HwApUnauthorizedApSn_Object = MibTableColumn
hwApUnauthorizedApSn = _HwApUnauthorizedApSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7, 1, 4),
    _HwApUnauthorizedApSn_Type()
)
hwApUnauthorizedApSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUnauthorizedApSn.setStatus("current")
_HwApUnauthorizedApIpAddress_Type = IpAddress
_HwApUnauthorizedApIpAddress_Object = MibTableColumn
hwApUnauthorizedApIpAddress = _HwApUnauthorizedApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7, 1, 5),
    _HwApUnauthorizedApIpAddress_Type()
)
hwApUnauthorizedApIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUnauthorizedApIpAddress.setStatus("current")
_HwApUnauthorizedApRecordTime_Type = DateAndTime
_HwApUnauthorizedApRecordTime_Object = MibTableColumn
hwApUnauthorizedApRecordTime = _HwApUnauthorizedApRecordTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 7, 1, 6),
    _HwApUnauthorizedApRecordTime_Type()
)
hwApUnauthorizedApRecordTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApUnauthorizedApRecordTime.setStatus("current")
_HwApParaStatisticTable_Object = MibTable
hwApParaStatisticTable = _HwApParaStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 8)
)
if mibBuilder.loadTexts:
    hwApParaStatisticTable.setStatus("current")
_HwApParaStatisticEntry_Object = MibTableRow
hwApParaStatisticEntry = _HwApParaStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 8, 1)
)
hwApParaStatisticEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
)
if mibBuilder.loadTexts:
    hwApParaStatisticEntry.setStatus("current")
_HwApStaAveSignalStrength_Type = Integer32
_HwApStaAveSignalStrength_Object = MibTableColumn
hwApStaAveSignalStrength = _HwApStaAveSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 8, 1, 1),
    _HwApStaAveSignalStrength_Type()
)
hwApStaAveSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaAveSignalStrength.setStatus("current")
_HwMacApTable_Object = MibTable
hwMacApTable = _HwMacApTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9)
)
if mibBuilder.loadTexts:
    hwMacApTable.setStatus("current")
_HwMacApEntry_Object = MibTableRow
hwMacApEntry = _HwMacApEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1)
)
hwMacApEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
)
if mibBuilder.loadTexts:
    hwMacApEntry.setStatus("current")
_HwMacApMac_Type = MacAddress
_HwMacApMac_Object = MibTableColumn
hwMacApMac = _HwMacApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 1),
    _HwMacApMac_Type()
)
hwMacApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApMac.setStatus("current")
_HwMacApIndex_Type = Integer32
_HwMacApIndex_Object = MibTableColumn
hwMacApIndex = _HwMacApIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 2),
    _HwMacApIndex_Type()
)
hwMacApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApIndex.setStatus("current")
_HwMacApUsedType_Type = OctetString
_HwMacApUsedType_Object = MibTableColumn
hwMacApUsedType = _HwMacApUsedType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 3),
    _HwMacApUsedType_Type()
)
hwMacApUsedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApUsedType.setStatus("current")
_HwMacApUsedProfileName_Type = OctetString
_HwMacApUsedProfileName_Object = MibTableColumn
hwMacApUsedProfileName = _HwMacApUsedProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 4),
    _HwMacApUsedProfileName_Type()
)
hwMacApUsedProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApUsedProfileName.setStatus("current")
_HwMacApUsedRegionIndex_Type = Integer32
_HwMacApUsedRegionIndex_Object = MibTableColumn
hwMacApUsedRegionIndex = _HwMacApUsedRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 5),
    _HwMacApUsedRegionIndex_Type()
)
hwMacApUsedRegionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApUsedRegionIndex.setStatus("current")
_HwMacApSn_Type = OctetString
_HwMacApSn_Object = MibTableColumn
hwMacApSn = _HwMacApSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 6),
    _HwMacApSn_Type()
)
hwMacApSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApSn.setStatus("current")
_HwMacApSysName_Type = OctetString
_HwMacApSysName_Object = MibTableColumn
hwMacApSysName = _HwMacApSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 7),
    _HwMacApSysName_Type()
)
hwMacApSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApSysName.setStatus("current")


class _HwMacApRunState_Type(Integer32):
    """Custom type hwMacApRunState based on Integer32"""
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
        *(("autofind", 2),
          ("commitFailed", 10),
          ("committing", 9),
          ("config", 5),
          ("configFailed", 6),
          ("download", 7),
          ("fault", 4),
          ("idle", 1),
          ("normal", 8),
          ("standby", 11),
          ("typeNotMatch", 3))
    )


_HwMacApRunState_Type.__name__ = "Integer32"
_HwMacApRunState_Object = MibTableColumn
hwMacApRunState = _HwMacApRunState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 8),
    _HwMacApRunState_Type()
)
hwMacApRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApRunState.setStatus("current")
_HwMacApSoftwareVersion_Type = OctetString
_HwMacApSoftwareVersion_Object = MibTableColumn
hwMacApSoftwareVersion = _HwMacApSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 9),
    _HwMacApSoftwareVersion_Type()
)
hwMacApSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApSoftwareVersion.setStatus("current")
_HwMacApHardwareVersion_Type = OctetString
_HwMacApHardwareVersion_Object = MibTableColumn
hwMacApHardwareVersion = _HwMacApHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 10),
    _HwMacApHardwareVersion_Type()
)
hwMacApHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApHardwareVersion.setStatus("current")
_HwMacApCpuType_Type = OctetString
_HwMacApCpuType_Object = MibTableColumn
hwMacApCpuType = _HwMacApCpuType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 11),
    _HwMacApCpuType_Type()
)
hwMacApCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApCpuType.setStatus("current")
_HwMacApCpufrequency_Type = Integer32
_HwMacApCpufrequency_Object = MibTableColumn
hwMacApCpufrequency = _HwMacApCpufrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 12),
    _HwMacApCpufrequency_Type()
)
hwMacApCpufrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApCpufrequency.setStatus("current")
_HwMacApMemoryType_Type = OctetString
_HwMacApMemoryType_Object = MibTableColumn
hwMacApMemoryType = _HwMacApMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 13),
    _HwMacApMemoryType_Type()
)
hwMacApMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApMemoryType.setStatus("current")
_HwMacApDomain_Type = OctetString
_HwMacApDomain_Object = MibTableColumn
hwMacApDomain = _HwMacApDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 14),
    _HwMacApDomain_Type()
)
hwMacApDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApDomain.setStatus("current")
_HwMacApIpAddress_Type = IpAddress
_HwMacApIpAddress_Object = MibTableColumn
hwMacApIpAddress = _HwMacApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 15),
    _HwMacApIpAddress_Type()
)
hwMacApIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApIpAddress.setStatus("current")
_HwMacApIpNetMask_Type = IpAddress
_HwMacApIpNetMask_Object = MibTableColumn
hwMacApIpNetMask = _HwMacApIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 16),
    _HwMacApIpNetMask_Type()
)
hwMacApIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApIpNetMask.setStatus("current")
_HwMacApGatewayIp_Type = IpAddress
_HwMacApGatewayIp_Object = MibTableColumn
hwMacApGatewayIp = _HwMacApGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 17),
    _HwMacApGatewayIp_Type()
)
hwMacApGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApGatewayIp.setStatus("current")
_HwMacApMemorySize_Type = Integer32
_HwMacApMemorySize_Object = MibTableColumn
hwMacApMemorySize = _HwMacApMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 18),
    _HwMacApMemorySize_Type()
)
hwMacApMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApMemorySize.setStatus("current")
_HwMacApFlashSize_Type = Integer32
_HwMacApFlashSize_Object = MibTableColumn
hwMacApFlashSize = _HwMacApFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 19),
    _HwMacApFlashSize_Type()
)
hwMacApFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApFlashSize.setStatus("current")
_HwMacApRunTime_Type = Unsigned32
_HwMacApRunTime_Object = MibTableColumn
hwMacApRunTime = _HwMacApRunTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 20),
    _HwMacApRunTime_Type()
)
hwMacApRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApRunTime.setStatus("current")


class _HwMacApUpEthPortSpeed_Type(Integer32):
    """Custom type hwMacApUpEthPortSpeed based on Integer32"""
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
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4))
    )


_HwMacApUpEthPortSpeed_Type.__name__ = "Integer32"
_HwMacApUpEthPortSpeed_Object = MibTableColumn
hwMacApUpEthPortSpeed = _HwMacApUpEthPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 21),
    _HwMacApUpEthPortSpeed_Type()
)
hwMacApUpEthPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpEthPortSpeed.setStatus("current")


class _HwMacApUpEthPortSpeedMode_Type(Integer32):
    """Custom type hwMacApUpEthPortSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forced", 2))
    )


_HwMacApUpEthPortSpeedMode_Type.__name__ = "Integer32"
_HwMacApUpEthPortSpeedMode_Object = MibTableColumn
hwMacApUpEthPortSpeedMode = _HwMacApUpEthPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 22),
    _HwMacApUpEthPortSpeedMode_Type()
)
hwMacApUpEthPortSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpEthPortSpeedMode.setStatus("current")


class _HwMacApUpEthPortDuplex_Type(Integer32):
    """Custom type hwMacApUpEthPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_HwMacApUpEthPortDuplex_Type.__name__ = "Integer32"
_HwMacApUpEthPortDuplex_Object = MibTableColumn
hwMacApUpEthPortDuplex = _HwMacApUpEthPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 23),
    _HwMacApUpEthPortDuplex_Type()
)
hwMacApUpEthPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpEthPortDuplex.setStatus("current")


class _HwMacApUpEthPortDuplexMode_Type(Integer32):
    """Custom type hwMacApUpEthPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forced", 2))
    )


_HwMacApUpEthPortDuplexMode_Type.__name__ = "Integer32"
_HwMacApUpEthPortDuplexMode_Object = MibTableColumn
hwMacApUpEthPortDuplexMode = _HwMacApUpEthPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 24),
    _HwMacApUpEthPortDuplexMode_Type()
)
hwMacApUpEthPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpEthPortDuplexMode.setStatus("current")


class _HwMacApAdminOper_Type(Integer32):
    """Custom type hwMacApAdminOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 2),
          ("manufacturerConfig", 3),
          ("replaceAp", 6),
          ("reset", 1))
    )


_HwMacApAdminOper_Type.__name__ = "Integer32"
_HwMacApAdminOper_Object = MibTableColumn
hwMacApAdminOper = _HwMacApAdminOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 25),
    _HwMacApAdminOper_Type()
)
hwMacApAdminOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApAdminOper.setStatus("current")
_HwMacApRowstatus_Type = RowStatus
_HwMacApRowstatus_Object = MibTableColumn
hwMacApRowstatus = _HwMacApRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 26),
    _HwMacApRowstatus_Type()
)
hwMacApRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApRowstatus.setStatus("current")


class _HwMacApPerformanceStatCycle_Type(Integer32):
    """Custom type hwMacApPerformanceStatCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 3),
          ("fiveMinutes", 1),
          ("tenMinutes", 2))
    )


_HwMacApPerformanceStatCycle_Type.__name__ = "Integer32"
_HwMacApPerformanceStatCycle_Object = MibTableColumn
hwMacApPerformanceStatCycle = _HwMacApPerformanceStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 27),
    _HwMacApPerformanceStatCycle_Type()
)
hwMacApPerformanceStatCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApPerformanceStatCycle.setStatus("current")
_HwMacApDNS_Type = IpAddress
_HwMacApDNS_Object = MibTableColumn
hwMacApDNS = _HwMacApDNS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 28),
    _HwMacApDNS_Type()
)
hwMacApDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApDNS.setStatus("current")


class _HwMacApRunningMode_Type(Integer32):
    """Custom type hwMacApRunningMode based on Integer32"""
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
          ("fat", 2),
          ("fit", 3))
    )


_HwMacApRunningMode_Type.__name__ = "Integer32"
_HwMacApRunningMode_Object = MibTableColumn
hwMacApRunningMode = _HwMacApRunningMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 29),
    _HwMacApRunningMode_Type()
)
hwMacApRunningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApRunningMode.setStatus("current")


class _HwMacApForwardMode_Type(Integer32):
    """Custom type hwMacApForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directForward", 1),
          ("tunnel", 2),
          ("unknown", -1))
    )


_HwMacApForwardMode_Type.__name__ = "Integer32"
_HwMacApForwardMode_Object = MibTableColumn
hwMacApForwardMode = _HwMacApForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 30),
    _HwMacApForwardMode_Type()
)
hwMacApForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApForwardMode.setStatus("current")


class _HwMacApAntennaMode_Type(Integer32):
    """Custom type hwMacApAntennaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 1),
          ("leftMode", 2),
          ("rightMode", 3))
    )


_HwMacApAntennaMode_Type.__name__ = "Integer32"
_HwMacApAntennaMode_Object = MibTableColumn
hwMacApAntennaMode = _HwMacApAntennaMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 31),
    _HwMacApAntennaMode_Type()
)
hwMacApAntennaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApAntennaMode.setStatus("current")
_HwMacApCpuThreshold_Type = Integer32
_HwMacApCpuThreshold_Object = MibTableColumn
hwMacApCpuThreshold = _HwMacApCpuThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 32),
    _HwMacApCpuThreshold_Type()
)
hwMacApCpuThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApCpuThreshold.setStatus("current")
_HwMacApMemThreshold_Type = Integer32
_HwMacApMemThreshold_Object = MibTableColumn
hwMacApMemThreshold = _HwMacApMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 33),
    _HwMacApMemThreshold_Type()
)
hwMacApMemThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApMemThreshold.setStatus("current")
_HwMacApNEnumber_Type = OctetString
_HwMacApNEnumber_Object = MibTableColumn
hwMacApNEnumber = _HwMacApNEnumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 34),
    _HwMacApNEnumber_Type()
)
hwMacApNEnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApNEnumber.setStatus("current")
_HwMacApOnlineTime_Type = Unsigned32
_HwMacApOnlineTime_Object = MibTableColumn
hwMacApOnlineTime = _HwMacApOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 35),
    _HwMacApOnlineTime_Type()
)
hwMacApOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOnlineTime.setStatus("current")
_HwMacApSysSoftwareDesc_Type = OctetString
_HwMacApSysSoftwareDesc_Object = MibTableColumn
hwMacApSysSoftwareDesc = _HwMacApSysSoftwareDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 36),
    _HwMacApSysSoftwareDesc_Type()
)
hwMacApSysSoftwareDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApSysSoftwareDesc.setStatus("current")
_HwMacApSysHardtwareDesc_Type = OctetString
_HwMacApSysHardtwareDesc_Object = MibTableColumn
hwMacApSysHardtwareDesc = _HwMacApSysHardtwareDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 37),
    _HwMacApSysHardtwareDesc_Type()
)
hwMacApSysHardtwareDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApSysHardtwareDesc.setStatus("current")
_HwMacApSysManufacture_Type = OctetString
_HwMacApSysManufacture_Object = MibTableColumn
hwMacApSysManufacture = _HwMacApSysManufacture_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 38),
    _HwMacApSysManufacture_Type()
)
hwMacApSysManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApSysManufacture.setStatus("current")
_HwMacApSysSoftwareName_Type = OctetString
_HwMacApSysSoftwareName_Object = MibTableColumn
hwMacApSysSoftwareName = _HwMacApSysSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 39),
    _HwMacApSysSoftwareName_Type()
)
hwMacApSysSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApSysSoftwareName.setStatus("current")
_HwMacApSysSoftwareVendor_Type = OctetString
_HwMacApSysSoftwareVendor_Object = MibTableColumn
hwMacApSysSoftwareVendor = _HwMacApSysSoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 40),
    _HwMacApSysSoftwareVendor_Type()
)
hwMacApSysSoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApSysSoftwareVendor.setStatus("current")
_HwMacApManagementVlanID_Type = Integer32
_HwMacApManagementVlanID_Object = MibTableColumn
hwMacApManagementVlanID = _HwMacApManagementVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 41),
    _HwMacApManagementVlanID_Type()
)
hwMacApManagementVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApManagementVlanID.setStatus("current")


class _HwMacApUsername_Type(OctetString):
    """Custom type hwMacApUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwMacApUsername_Type.__name__ = "OctetString"
_HwMacApUsername_Object = MibTableColumn
hwMacApUsername = _HwMacApUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 42),
    _HwMacApUsername_Type()
)
hwMacApUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApUsername.setStatus("current")


class _HwMacApPassword_Type(OctetString):
    """Custom type hwMacApPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwMacApPassword_Type.__name__ = "OctetString"
_HwMacApPassword_Object = MibTableColumn
hwMacApPassword = _HwMacApPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 43),
    _HwMacApPassword_Type()
)
hwMacApPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApPassword.setStatus("current")
_HwMacApAcIP1_Type = IpAddress
_HwMacApAcIP1_Object = MibTableColumn
hwMacApAcIP1 = _HwMacApAcIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 44),
    _HwMacApAcIP1_Type()
)
hwMacApAcIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApAcIP1.setStatus("current")
_HwMacApAcIP2_Type = IpAddress
_HwMacApAcIP2_Object = MibTableColumn
hwMacApAcIP2 = _HwMacApAcIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 45),
    _HwMacApAcIP2_Type()
)
hwMacApAcIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApAcIP2.setStatus("current")
_HwMacApAcIP3_Type = IpAddress
_HwMacApAcIP3_Object = MibTableColumn
hwMacApAcIP3 = _HwMacApAcIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 46),
    _HwMacApAcIP3_Type()
)
hwMacApAcIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApAcIP3.setStatus("current")
_HwMacApAcIP4_Type = IpAddress
_HwMacApAcIP4_Object = MibTableColumn
hwMacApAcIP4 = _HwMacApAcIP4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 47),
    _HwMacApAcIP4_Type()
)
hwMacApAcIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApAcIP4.setStatus("current")


class _HwMacApIpMode_Type(Integer32):
    """Custom type hwMacApIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("pppoe", 2),
          ("static", 3))
    )


_HwMacApIpMode_Type.__name__ = "Integer32"
_HwMacApIpMode_Object = MibTableColumn
hwMacApIpMode = _HwMacApIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 48),
    _HwMacApIpMode_Type()
)
hwMacApIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApIpMode.setStatus("current")


class _HwMacApLldpEnable_Type(Integer32):
    """Custom type hwMacApLldpEnable based on Integer32"""
    defaultValue = 1

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


_HwMacApLldpEnable_Type.__name__ = "Integer32"
_HwMacApLldpEnable_Object = MibTableColumn
hwMacApLldpEnable = _HwMacApLldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 49),
    _HwMacApLldpEnable_Type()
)
hwMacApLldpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpEnable.setStatus("current")


class _HwMacApLldpManageAddr_Type(Integer32):
    """Custom type hwMacApLldpManageAddr based on Integer32"""
    defaultValue = 2

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


_HwMacApLldpManageAddr_Type.__name__ = "Integer32"
_HwMacApLldpManageAddr_Object = MibTableColumn
hwMacApLldpManageAddr = _HwMacApLldpManageAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 50),
    _HwMacApLldpManageAddr_Type()
)
hwMacApLldpManageAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpManageAddr.setStatus("current")


class _HwMacApLldpPortDes_Type(Integer32):
    """Custom type hwMacApLldpPortDes based on Integer32"""
    defaultValue = 2

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


_HwMacApLldpPortDes_Type.__name__ = "Integer32"
_HwMacApLldpPortDes_Object = MibTableColumn
hwMacApLldpPortDes = _HwMacApLldpPortDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 51),
    _HwMacApLldpPortDes_Type()
)
hwMacApLldpPortDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpPortDes.setStatus("current")


class _HwMacApLldpSysCab_Type(Integer32):
    """Custom type hwMacApLldpSysCab based on Integer32"""
    defaultValue = 2

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


_HwMacApLldpSysCab_Type.__name__ = "Integer32"
_HwMacApLldpSysCab_Object = MibTableColumn
hwMacApLldpSysCab = _HwMacApLldpSysCab_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 52),
    _HwMacApLldpSysCab_Type()
)
hwMacApLldpSysCab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpSysCab.setStatus("current")


class _HwMacApLldpSysDes_Type(Integer32):
    """Custom type hwMacApLldpSysDes based on Integer32"""
    defaultValue = 2

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


_HwMacApLldpSysDes_Type.__name__ = "Integer32"
_HwMacApLldpSysDes_Object = MibTableColumn
hwMacApLldpSysDes = _HwMacApLldpSysDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 53),
    _HwMacApLldpSysDes_Type()
)
hwMacApLldpSysDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpSysDes.setStatus("current")


class _HwMacApLldpSysName_Type(Integer32):
    """Custom type hwMacApLldpSysName based on Integer32"""
    defaultValue = 2

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


_HwMacApLldpSysName_Type.__name__ = "Integer32"
_HwMacApLldpSysName_Object = MibTableColumn
hwMacApLldpSysName = _HwMacApLldpSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 54),
    _HwMacApLldpSysName_Type()
)
hwMacApLldpSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpSysName.setStatus("current")


class _HwMacApLldpDelay_Type(Integer32):
    """Custom type hwMacApLldpDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_HwMacApLldpDelay_Type.__name__ = "Integer32"
_HwMacApLldpDelay_Object = MibTableColumn
hwMacApLldpDelay = _HwMacApLldpDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 55),
    _HwMacApLldpDelay_Type()
)
hwMacApLldpDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpDelay.setStatus("current")


class _HwMacApLldpHoldMultiplier_Type(Integer32):
    """Custom type hwMacApLldpHoldMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_HwMacApLldpHoldMultiplier_Type.__name__ = "Integer32"
_HwMacApLldpHoldMultiplier_Object = MibTableColumn
hwMacApLldpHoldMultiplier = _HwMacApLldpHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 56),
    _HwMacApLldpHoldMultiplier_Type()
)
hwMacApLldpHoldMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpHoldMultiplier.setStatus("current")


class _HwMacApLldpInterval_Type(Integer32):
    """Custom type hwMacApLldpInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_HwMacApLldpInterval_Type.__name__ = "Integer32"
_HwMacApLldpInterval_Object = MibTableColumn
hwMacApLldpInterval = _HwMacApLldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 57),
    _HwMacApLldpInterval_Type()
)
hwMacApLldpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpInterval.setStatus("current")


class _HwMacApLldpRestartDelay_Type(Integer32):
    """Custom type hwMacApLldpRestartDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMacApLldpRestartDelay_Type.__name__ = "Integer32"
_HwMacApLldpRestartDelay_Object = MibTableColumn
hwMacApLldpRestartDelay = _HwMacApLldpRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 58),
    _HwMacApLldpRestartDelay_Type()
)
hwMacApLldpRestartDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpRestartDelay.setStatus("current")


class _HwMacApLldpAdminStatus_Type(Integer32):
    """Custom type hwMacApLldpAdminStatus based on Integer32"""
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
        *(("rx", 2),
          ("tx", 3),
          ("txrx", 1))
    )


_HwMacApLldpAdminStatus_Type.__name__ = "Integer32"
_HwMacApLldpAdminStatus_Object = MibTableColumn
hwMacApLldpAdminStatus = _HwMacApLldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 59),
    _HwMacApLldpAdminStatus_Type()
)
hwMacApLldpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpAdminStatus.setStatus("current")


class _HwMacApLldpReportInterval_Type(Integer32):
    """Custom type hwMacApLldpReportInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_HwMacApLldpReportInterval_Type.__name__ = "Integer32"
_HwMacApLldpReportInterval_Object = MibTableColumn
hwMacApLldpReportInterval = _HwMacApLldpReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 60),
    _HwMacApLldpReportInterval_Type()
)
hwMacApLldpReportInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApLldpReportInterval.setStatus("current")
_HwMacApBomCode_Type = OctetString
_HwMacApBomCode_Object = MibTableColumn
hwMacApBomCode = _HwMacApBomCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 61),
    _HwMacApBomCode_Type()
)
hwMacApBomCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApBomCode.setStatus("current")
_HwMacApSaveMode_Type = Integer32
_HwMacApSaveMode_Object = MibTableColumn
hwMacApSaveMode = _HwMacApSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 62),
    _HwMacApSaveMode_Type()
)
hwMacApSaveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApSaveMode.setStatus("obsolete")
_HwMacApProtectAcPriority_Type = Integer32
_HwMacApProtectAcPriority_Object = MibTableColumn
hwMacApProtectAcPriority = _HwMacApProtectAcPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 63),
    _HwMacApProtectAcPriority_Type()
)
hwMacApProtectAcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApProtectAcPriority.setStatus("current")
_HwMacApProtectAcIP_Type = IpAddress
_HwMacApProtectAcIP_Object = MibTableColumn
hwMacApProtectAcIP = _HwMacApProtectAcIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 64),
    _HwMacApProtectAcIP_Type()
)
hwMacApProtectAcIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApProtectAcIP.setStatus("current")


class _HwMacApOpticalHighRxPowerThreshold_Type(Integer32):
    """Custom type hwMacApOpticalHighRxPowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_HwMacApOpticalHighRxPowerThreshold_Type.__name__ = "Integer32"
_HwMacApOpticalHighRxPowerThreshold_Object = MibTableColumn
hwMacApOpticalHighRxPowerThreshold = _HwMacApOpticalHighRxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 65),
    _HwMacApOpticalHighRxPowerThreshold_Type()
)
hwMacApOpticalHighRxPowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApOpticalHighRxPowerThreshold.setStatus("current")


class _HwMacApOpticalLowRxPowerThreshold_Type(Integer32):
    """Custom type hwMacApOpticalLowRxPowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HwMacApOpticalLowRxPowerThreshold_Type.__name__ = "Integer32"
_HwMacApOpticalLowRxPowerThreshold_Object = MibTableColumn
hwMacApOpticalLowRxPowerThreshold = _HwMacApOpticalLowRxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 66),
    _HwMacApOpticalLowRxPowerThreshold_Type()
)
hwMacApOpticalLowRxPowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApOpticalLowRxPowerThreshold.setStatus("current")


class _HwMacApOpticalHighTemperatureThreshold_Type(Integer32):
    """Custom type hwMacApOpticalHighTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 125),
    )


_HwMacApOpticalHighTemperatureThreshold_Type.__name__ = "Integer32"
_HwMacApOpticalHighTemperatureThreshold_Object = MibTableColumn
hwMacApOpticalHighTemperatureThreshold = _HwMacApOpticalHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 67),
    _HwMacApOpticalHighTemperatureThreshold_Type()
)
hwMacApOpticalHighTemperatureThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApOpticalHighTemperatureThreshold.setStatus("current")


class _HwMacApOpticalLowTemperatureThreshold_Type(Integer32):
    """Custom type hwMacApOpticalLowTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, -5),
    )


_HwMacApOpticalLowTemperatureThreshold_Type.__name__ = "Integer32"
_HwMacApOpticalLowTemperatureThreshold_Object = MibTableColumn
hwMacApOpticalLowTemperatureThreshold = _HwMacApOpticalLowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 68),
    _HwMacApOpticalLowTemperatureThreshold_Type()
)
hwMacApOpticalLowTemperatureThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApOpticalLowTemperatureThreshold.setStatus("current")


class _HwMacApKeepService_Type(Integer32):
    """Custom type hwMacApKeepService based on Integer32"""
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


_HwMacApKeepService_Type.__name__ = "Integer32"
_HwMacApKeepService_Object = MibTableColumn
hwMacApKeepService = _HwMacApKeepService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 69),
    _HwMacApKeepService_Type()
)
hwMacApKeepService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApKeepService.setStatus("current")


class _HwMacApPriorityAccessMode_Type(Integer32):
    """Custom type hwMacApPriorityAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwMacApPriorityAccessMode_Type.__name__ = "Integer32"
_HwMacApPriorityAccessMode_Object = MibTableColumn
hwMacApPriorityAccessMode = _HwMacApPriorityAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 70),
    _HwMacApPriorityAccessMode_Type()
)
hwMacApPriorityAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApPriorityAccessMode.setStatus("current")


class _HwMacApLineateportMode_Type(Integer32):
    """Custom type hwMacApLineateportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpoint", 2),
          ("root", 1))
    )


_HwMacApLineateportMode_Type.__name__ = "Integer32"
_HwMacApLineateportMode_Object = MibTableColumn
hwMacApLineateportMode = _HwMacApLineateportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 71),
    _HwMacApLineateportMode_Type()
)
hwMacApLineateportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineateportMode.setStatus("current")


class _HwMacApLineateportVlanTagged_Type(OctetString):
    """Custom type hwMacApLineateportVlanTagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwMacApLineateportVlanTagged_Type.__name__ = "OctetString"
_HwMacApLineateportVlanTagged_Object = MibTableColumn
hwMacApLineateportVlanTagged = _HwMacApLineateportVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 72),
    _HwMacApLineateportVlanTagged_Type()
)
hwMacApLineateportVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineateportVlanTagged.setStatus("current")


class _HwMacApLineateportVlanUntagged_Type(OctetString):
    """Custom type hwMacApLineateportVlanUntagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwMacApLineateportVlanUntagged_Type.__name__ = "OctetString"
_HwMacApLineateportVlanUntagged_Object = MibTableColumn
hwMacApLineateportVlanUntagged = _HwMacApLineateportVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 73),
    _HwMacApLineateportVlanUntagged_Type()
)
hwMacApLineateportVlanUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineateportVlanUntagged.setStatus("current")


class _HwMacApLineateportPvidVlan_Type(Integer32):
    """Custom type hwMacApLineateportPvidVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMacApLineateportPvidVlan_Type.__name__ = "Integer32"
_HwMacApLineateportPvidVlan_Object = MibTableColumn
hwMacApLineateportPvidVlan = _HwMacApLineateportPvidVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 74),
    _HwMacApLineateportPvidVlan_Type()
)
hwMacApLineateportPvidVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineateportPvidVlan.setStatus("current")


class _HwMacApLineateportUserIsolate_Type(Integer32):
    """Custom type hwMacApLineateportUserIsolate based on Integer32"""
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


_HwMacApLineateportUserIsolate_Type.__name__ = "Integer32"
_HwMacApLineateportUserIsolate_Object = MibTableColumn
hwMacApLineateportUserIsolate = _HwMacApLineateportUserIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 75),
    _HwMacApLineateportUserIsolate_Type()
)
hwMacApLineateportUserIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineateportUserIsolate.setStatus("current")


class _HwMacApLineateportStpEnable_Type(Integer32):
    """Custom type hwMacApLineateportStpEnable based on Integer32"""
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


_HwMacApLineateportStpEnable_Type.__name__ = "Integer32"
_HwMacApLineateportStpEnable_Object = MibTableColumn
hwMacApLineateportStpEnable = _HwMacApLineateportStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 76),
    _HwMacApLineateportStpEnable_Type()
)
hwMacApLineateportStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineateportStpEnable.setStatus("current")


class _HwMacApHighTemperatureThreshold_Type(Integer32):
    """Custom type hwMacApHighTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 70),
    )


_HwMacApHighTemperatureThreshold_Type.__name__ = "Integer32"
_HwMacApHighTemperatureThreshold_Object = MibTableColumn
hwMacApHighTemperatureThreshold = _HwMacApHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 77),
    _HwMacApHighTemperatureThreshold_Type()
)
hwMacApHighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApHighTemperatureThreshold.setStatus("current")


class _HwMacApLowTemperatureThreshold_Type(Integer32):
    """Custom type hwMacApLowTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 10),
    )


_HwMacApLowTemperatureThreshold_Type.__name__ = "Integer32"
_HwMacApLowTemperatureThreshold_Object = MibTableColumn
hwMacApLowTemperatureThreshold = _HwMacApLowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 78),
    _HwMacApLowTemperatureThreshold_Type()
)
hwMacApLowTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLowTemperatureThreshold.setStatus("current")
_HwMacApReset_Type = Integer32
_HwMacApReset_Object = MibTableColumn
hwMacApReset = _HwMacApReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 79),
    _HwMacApReset_Type()
)
hwMacApReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApReset.setStatus("current")
_HwMacApStaticIpAddress_Type = IpAddress
_HwMacApStaticIpAddress_Object = MibTableColumn
hwMacApStaticIpAddress = _HwMacApStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 80),
    _HwMacApStaticIpAddress_Type()
)
hwMacApStaticIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApStaticIpAddress.setStatus("current")
_HwMacApStaticNetMask_Type = IpAddress
_HwMacApStaticNetMask_Object = MibTableColumn
hwMacApStaticNetMask = _HwMacApStaticNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 81),
    _HwMacApStaticNetMask_Type()
)
hwMacApStaticNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApStaticNetMask.setStatus("current")
_HwMacApStaticGatewayIp_Type = IpAddress
_HwMacApStaticGatewayIp_Object = MibTableColumn
hwMacApStaticGatewayIp = _HwMacApStaticGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 82),
    _HwMacApStaticGatewayIp_Type()
)
hwMacApStaticGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApStaticGatewayIp.setStatus("current")
_HwMacApAttackFloodInterval_Type = Integer32
_HwMacApAttackFloodInterval_Object = MibTableColumn
hwMacApAttackFloodInterval = _HwMacApAttackFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 83),
    _HwMacApAttackFloodInterval_Type()
)
hwMacApAttackFloodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApAttackFloodInterval.setStatus("current")
_HwMACApAttackFloodTimes_Type = Integer32
_HwMACApAttackFloodTimes_Object = MibTableColumn
hwMACApAttackFloodTimes = _HwMACApAttackFloodTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 84),
    _HwMACApAttackFloodTimes_Type()
)
hwMACApAttackFloodTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApAttackFloodTimes.setStatus("current")
_HwMACApDynamicBlacklistEnable_Type = Integer32
_HwMACApDynamicBlacklistEnable_Object = MibTableColumn
hwMACApDynamicBlacklistEnable = _HwMACApDynamicBlacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 85),
    _HwMACApDynamicBlacklistEnable_Type()
)
hwMACApDynamicBlacklistEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApDynamicBlacklistEnable.setStatus("current")
_HwMACApDynamicBlacklistAgingInt_Type = Integer32
_HwMACApDynamicBlacklistAgingInt_Object = MibTableColumn
hwMACApDynamicBlacklistAgingInt = _HwMACApDynamicBlacklistAgingInt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 86),
    _HwMACApDynamicBlacklistAgingInt_Type()
)
hwMACApDynamicBlacklistAgingInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApDynamicBlacklistAgingInt.setStatus("current")
_HwMACApAttackPskInterval_Type = Integer32
_HwMACApAttackPskInterval_Object = MibTableColumn
hwMACApAttackPskInterval = _HwMACApAttackPskInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 87),
    _HwMACApAttackPskInterval_Type()
)
hwMACApAttackPskInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApAttackPskInterval.setStatus("current")
_HwMACApAttackPskTimes_Type = Integer32
_HwMACApAttackPskTimes_Object = MibTableColumn
hwMACApAttackPskTimes = _HwMACApAttackPskTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 88),
    _HwMACApAttackPskTimes_Type()
)
hwMACApAttackPskTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApAttackPskTimes.setStatus("current")


class _HwMACApAccessBalanceGap_Type(Integer32):
    """Custom type hwMACApAccessBalanceGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwMACApAccessBalanceGap_Type.__name__ = "Integer32"
_HwMACApAccessBalanceGap_Object = MibTableColumn
hwMACApAccessBalanceGap = _HwMACApAccessBalanceGap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 89),
    _HwMACApAccessBalanceGap_Type()
)
hwMACApAccessBalanceGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMACApAccessBalanceGap.setStatus("current")


class _HwMACApIpv6Address_Type(OctetString):
    """Custom type hwMACApIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwMACApIpv6Address_Type.__name__ = "OctetString"
_HwMACApIpv6Address_Object = MibTableColumn
hwMACApIpv6Address = _HwMACApIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 90),
    _HwMACApIpv6Address_Type()
)
hwMACApIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMACApIpv6Address.setStatus("current")


class _HwMACApIpv6NetMask_Type(OctetString):
    """Custom type hwMACApIpv6NetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwMACApIpv6NetMask_Type.__name__ = "OctetString"
_HwMACApIpv6NetMask_Object = MibTableColumn
hwMACApIpv6NetMask = _HwMACApIpv6NetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 91),
    _HwMACApIpv6NetMask_Type()
)
hwMACApIpv6NetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApIpv6NetMask.setStatus("current")


class _HwMACApGatewayIpv6_Type(OctetString):
    """Custom type hwMACApGatewayIpv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwMACApGatewayIpv6_Type.__name__ = "OctetString"
_HwMACApGatewayIpv6_Object = MibTableColumn
hwMACApGatewayIpv6 = _HwMACApGatewayIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 92),
    _HwMACApGatewayIpv6_Type()
)
hwMACApGatewayIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApGatewayIpv6.setStatus("current")


class _HwMACApIpv6DNS_Type(OctetString):
    """Custom type hwMACApIpv6DNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwMACApIpv6DNS_Type.__name__ = "OctetString"
_HwMACApIpv6DNS_Object = MibTableColumn
hwMACApIpv6DNS = _HwMACApIpv6DNS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 93),
    _HwMACApIpv6DNS_Type()
)
hwMACApIpv6DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApIpv6DNS.setStatus("current")


class _HwMACApProtectAcIPv6Addr_Type(OctetString):
    """Custom type hwMACApProtectAcIPv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwMACApProtectAcIPv6Addr_Type.__name__ = "OctetString"
_HwMACApProtectAcIPv6Addr_Object = MibTableColumn
hwMACApProtectAcIPv6Addr = _HwMACApProtectAcIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 94),
    _HwMACApProtectAcIPv6Addr_Type()
)
hwMACApProtectAcIPv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApProtectAcIPv6Addr.setStatus("current")
_HwMACApLineatePortCfgMtu_Type = Integer32
_HwMACApLineatePortCfgMtu_Object = MibTableColumn
hwMACApLineatePortCfgMtu = _HwMACApLineatePortCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 95),
    _HwMACApLineatePortCfgMtu_Type()
)
hwMACApLineatePortCfgMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLineatePortCfgMtu.setStatus("current")
_HwMACApLineatePortMacAddress_Type = MacAddress
_HwMACApLineatePortMacAddress_Object = MibTableColumn
hwMACApLineatePortMacAddress = _HwMACApLineatePortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 96),
    _HwMACApLineatePortMacAddress_Type()
)
hwMACApLineatePortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLineatePortMacAddress.setStatus("current")


class _HwMACApAccessBalanceSwitch_Type(Integer32):
    """Custom type hwMACApAccessBalanceSwitch based on Integer32"""
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


_HwMACApAccessBalanceSwitch_Type.__name__ = "Integer32"
_HwMACApAccessBalanceSwitch_Object = MibTableColumn
hwMACApAccessBalanceSwitch = _HwMACApAccessBalanceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 97),
    _HwMACApAccessBalanceSwitch_Type()
)
hwMACApAccessBalanceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMACApAccessBalanceSwitch.setStatus("current")
_HwMACApNatIpAddress_Type = OctetString
_HwMACApNatIpAddress_Object = MibTableColumn
hwMACApNatIpAddress = _HwMACApNatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 98),
    _HwMACApNatIpAddress_Type()
)
hwMACApNatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApNatIpAddress.setStatus("current")


class _HwMACApAttackFloodQuietTime_Type(Integer32):
    """Custom type hwMACApAttackFloodQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwMACApAttackFloodQuietTime_Type.__name__ = "Integer32"
_HwMACApAttackFloodQuietTime_Object = MibTableColumn
hwMACApAttackFloodQuietTime = _HwMACApAttackFloodQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 99),
    _HwMACApAttackFloodQuietTime_Type()
)
hwMACApAttackFloodQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApAttackFloodQuietTime.setStatus("current")


class _HwMACApAttackPskQuietTime_Type(Integer32):
    """Custom type hwMACApAttackPskQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwMACApAttackPskQuietTime_Type.__name__ = "Integer32"
_HwMACApAttackPskQuietTime_Object = MibTableColumn
hwMACApAttackPskQuietTime = _HwMACApAttackPskQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 100),
    _HwMACApAttackPskQuietTime_Type()
)
hwMACApAttackPskQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApAttackPskQuietTime.setStatus("current")


class _HwMACApAttackWeakivQuietTime_Type(Integer32):
    """Custom type hwMACApAttackWeakivQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwMACApAttackWeakivQuietTime_Type.__name__ = "Integer32"
_HwMACApAttackWeakivQuietTime_Object = MibTableColumn
hwMACApAttackWeakivQuietTime = _HwMACApAttackWeakivQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 101),
    _HwMACApAttackWeakivQuietTime_Type()
)
hwMACApAttackWeakivQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApAttackWeakivQuietTime.setStatus("current")


class _HwMACApAttackSpoofQuietTime_Type(Integer32):
    """Custom type hwMACApAttackSpoofQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_HwMACApAttackSpoofQuietTime_Type.__name__ = "Integer32"
_HwMACApAttackSpoofQuietTime_Object = MibTableColumn
hwMACApAttackSpoofQuietTime = _HwMACApAttackSpoofQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 102),
    _HwMACApAttackSpoofQuietTime_Type()
)
hwMACApAttackSpoofQuietTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApAttackSpoofQuietTime.setStatus("current")
_HwMACApBootCountTotal_Type = Integer32
_HwMACApBootCountTotal_Object = MibTableColumn
hwMACApBootCountTotal = _HwMACApBootCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 103),
    _HwMACApBootCountTotal_Type()
)
hwMACApBootCountTotal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApBootCountTotal.setStatus("current")
_HwMACApBootCountPowerOff_Type = Integer32
_HwMACApBootCountPowerOff_Object = MibTableColumn
hwMACApBootCountPowerOff = _HwMACApBootCountPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 104),
    _HwMACApBootCountPowerOff_Type()
)
hwMACApBootCountPowerOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApBootCountPowerOff.setStatus("current")
_HwMACApBootCountRowStatus_Type = RowStatus
_HwMACApBootCountRowStatus_Object = MibTableColumn
hwMACApBootCountRowStatus = _HwMACApBootCountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 9, 1, 105),
    _HwMACApBootCountRowStatus_Type()
)
hwMACApBootCountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMACApBootCountRowStatus.setStatus("current")
_HwMacApLineatePortTable_Object = MibTable
hwMacApLineatePortTable = _HwMacApLineatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10)
)
if mibBuilder.loadTexts:
    hwMacApLineatePortTable.setStatus("current")
_HwMacApLineatePortEntry_Object = MibTableRow
hwMacApLineatePortEntry = _HwMacApLineatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1)
)
hwMacApLineatePortEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortIndex"),
)
if mibBuilder.loadTexts:
    hwMacApLineatePortEntry.setStatus("current")
_HwMacApLineatePortIndex_Type = Integer32
_HwMacApLineatePortIndex_Object = MibTableColumn
hwMacApLineatePortIndex = _HwMacApLineatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 1),
    _HwMacApLineatePortIndex_Type()
)
hwMacApLineatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApLineatePortIndex.setStatus("current")


class _HwMacApLineatePortType_Type(Integer32):
    """Custom type hwMacApLineatePortType based on Integer32"""
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
        *(("adsl2plus", 5),
          ("epon", 4),
          ("fe", 1),
          ("ge", 2),
          ("gpon", 3),
          ("trunk", 6))
    )


_HwMacApLineatePortType_Type.__name__ = "Integer32"
_HwMacApLineatePortType_Object = MibTableColumn
hwMacApLineatePortType = _HwMacApLineatePortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 2),
    _HwMacApLineatePortType_Type()
)
hwMacApLineatePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortType.setStatus("current")
_HwMacApLineatePortDesc_Type = OctetString
_HwMacApLineatePortDesc_Object = MibTableColumn
hwMacApLineatePortDesc = _HwMacApLineatePortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 3),
    _HwMacApLineatePortDesc_Type()
)
hwMacApLineatePortDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortDesc.setStatus("current")


class _HwMacApLineatePortState_Type(Integer32):
    """Custom type hwMacApLineatePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("unknown", -1),
          ("up", 2))
    )


_HwMacApLineatePortState_Type.__name__ = "Integer32"
_HwMacApLineatePortState_Object = MibTableColumn
hwMacApLineatePortState = _HwMacApLineatePortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 4),
    _HwMacApLineatePortState_Type()
)
hwMacApLineatePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortState.setStatus("current")
_HwMacApLineatePortSpeed_Type = Integer32
_HwMacApLineatePortSpeed_Object = MibTableColumn
hwMacApLineatePortSpeed = _HwMacApLineatePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 5),
    _HwMacApLineatePortSpeed_Type()
)
hwMacApLineatePortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortSpeed.setStatus("current")


class _HwMacApMultiLineatePortDuplex_Type(Integer32):
    """Custom type hwMacApMultiLineatePortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("unknown", -1))
    )


_HwMacApMultiLineatePortDuplex_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortDuplex_Object = MibTableColumn
hwMacApMultiLineatePortDuplex = _HwMacApMultiLineatePortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 6),
    _HwMacApMultiLineatePortDuplex_Type()
)
hwMacApMultiLineatePortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortDuplex.setStatus("current")


class _HwMacApMultiLineatePortNegotiation_Type(Integer32):
    """Custom type hwMacApMultiLineatePortNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forced", 2),
          ("unknown", -1))
    )


_HwMacApMultiLineatePortNegotiation_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortNegotiation_Object = MibTableColumn
hwMacApMultiLineatePortNegotiation = _HwMacApMultiLineatePortNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 7),
    _HwMacApMultiLineatePortNegotiation_Type()
)
hwMacApMultiLineatePortNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortNegotiation.setStatus("current")


class _HwMacApMultiLineatePortMode_Type(Integer32):
    """Custom type hwMacApMultiLineatePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpoint", 2),
          ("root", 1))
    )


_HwMacApMultiLineatePortMode_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortMode_Object = MibTableColumn
hwMacApMultiLineatePortMode = _HwMacApMultiLineatePortMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 8),
    _HwMacApMultiLineatePortMode_Type()
)
hwMacApMultiLineatePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortMode.setStatus("current")


class _HwMacApMultiLineatePortUserIsolate_Type(Integer32):
    """Custom type hwMacApMultiLineatePortUserIsolate based on Integer32"""
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


_HwMacApMultiLineatePortUserIsolate_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortUserIsolate_Object = MibTableColumn
hwMacApMultiLineatePortUserIsolate = _HwMacApMultiLineatePortUserIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 9),
    _HwMacApMultiLineatePortUserIsolate_Type()
)
hwMacApMultiLineatePortUserIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortUserIsolate.setStatus("current")


class _HwMacApMultiLineatePortStpEnable_Type(Integer32):
    """Custom type hwMacApMultiLineatePortStpEnable based on Integer32"""
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


_HwMacApMultiLineatePortStpEnable_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortStpEnable_Object = MibTableColumn
hwMacApMultiLineatePortStpEnable = _HwMacApMultiLineatePortStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 10),
    _HwMacApMultiLineatePortStpEnable_Type()
)
hwMacApMultiLineatePortStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortStpEnable.setStatus("current")


class _HwMacApMultiLineatePortVlanTagged_Type(OctetString):
    """Custom type hwMacApMultiLineatePortVlanTagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwMacApMultiLineatePortVlanTagged_Type.__name__ = "OctetString"
_HwMacApMultiLineatePortVlanTagged_Object = MibTableColumn
hwMacApMultiLineatePortVlanTagged = _HwMacApMultiLineatePortVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 11),
    _HwMacApMultiLineatePortVlanTagged_Type()
)
hwMacApMultiLineatePortVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortVlanTagged.setStatus("current")


class _HwMacApMultiLineatePortVlanUntagged_Type(OctetString):
    """Custom type hwMacApMultiLineatePortVlanUntagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwMacApMultiLineatePortVlanUntagged_Type.__name__ = "OctetString"
_HwMacApMultiLineatePortVlanUntagged_Object = MibTableColumn
hwMacApMultiLineatePortVlanUntagged = _HwMacApMultiLineatePortVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 12),
    _HwMacApMultiLineatePortVlanUntagged_Type()
)
hwMacApMultiLineatePortVlanUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortVlanUntagged.setStatus("current")


class _HwMacApMultiLineatePortPvidVlan_Type(Integer32):
    """Custom type hwMacApMultiLineatePortPvidVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMacApMultiLineatePortPvidVlan_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortPvidVlan_Object = MibTableColumn
hwMacApMultiLineatePortPvidVlan = _HwMacApMultiLineatePortPvidVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 13),
    _HwMacApMultiLineatePortPvidVlan_Type()
)
hwMacApMultiLineatePortPvidVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortPvidVlan.setStatus("current")
_HwMacApMultiLineatePortCRCErrorHighThreshold_Type = Integer32
_HwMacApMultiLineatePortCRCErrorHighThreshold_Object = MibTableColumn
hwMacApMultiLineatePortCRCErrorHighThreshold = _HwMacApMultiLineatePortCRCErrorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 14),
    _HwMacApMultiLineatePortCRCErrorHighThreshold_Type()
)
hwMacApMultiLineatePortCRCErrorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortCRCErrorHighThreshold.setStatus("current")
_HwMacApMultiLineatePortCRCErrorLowThreshold_Type = Integer32
_HwMacApMultiLineatePortCRCErrorLowThreshold_Object = MibTableColumn
hwMacApMultiLineatePortCRCErrorLowThreshold = _HwMacApMultiLineatePortCRCErrorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 15),
    _HwMacApMultiLineatePortCRCErrorLowThreshold_Type()
)
hwMacApMultiLineatePortCRCErrorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortCRCErrorLowThreshold.setStatus("current")


class _HwMacApMultiLineatePortCRCErrorSwitch_Type(Integer32):
    """Custom type hwMacApMultiLineatePortCRCErrorSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("unknown", -1))
    )


_HwMacApMultiLineatePortCRCErrorSwitch_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortCRCErrorSwitch_Object = MibTableColumn
hwMacApMultiLineatePortCRCErrorSwitch = _HwMacApMultiLineatePortCRCErrorSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 16),
    _HwMacApMultiLineatePortCRCErrorSwitch_Type()
)
hwMacApMultiLineatePortCRCErrorSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortCRCErrorSwitch.setStatus("current")
_HwMacApLineatePortAclNumInbound_Type = Integer32
_HwMacApLineatePortAclNumInbound_Object = MibTableColumn
hwMacApLineatePortAclNumInbound = _HwMacApLineatePortAclNumInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 17),
    _HwMacApLineatePortAclNumInbound_Type()
)
hwMacApLineatePortAclNumInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNumInbound.setStatus("current")
_HwMacApLineatePortAclNumOutbound_Type = Integer32
_HwMacApLineatePortAclNumOutbound_Object = MibTableColumn
hwMacApLineatePortAclNumOutbound = _HwMacApLineatePortAclNumOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 18),
    _HwMacApLineatePortAclNumOutbound_Type()
)
hwMacApLineatePortAclNumOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNumOutbound.setStatus("current")
_HwMacApLineatePortAclNameInbound_Type = OctetString
_HwMacApLineatePortAclNameInbound_Object = MibTableColumn
hwMacApLineatePortAclNameInbound = _HwMacApLineatePortAclNameInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 19),
    _HwMacApLineatePortAclNameInbound_Type()
)
hwMacApLineatePortAclNameInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNameInbound.setStatus("current")
_HwMacApLineatePortAclNameOutbound_Type = OctetString
_HwMacApLineatePortAclNameOutbound_Object = MibTableColumn
hwMacApLineatePortAclNameOutbound = _HwMacApLineatePortAclNameOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 20),
    _HwMacApLineatePortAclNameOutbound_Type()
)
hwMacApLineatePortAclNameOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNameOutbound.setStatus("current")


class _HwMacApLineatePortAclSwitchInbound_Type(Integer32):
    """Custom type hwMacApLineatePortAclSwitchInbound based on Integer32"""
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


_HwMacApLineatePortAclSwitchInbound_Type.__name__ = "Integer32"
_HwMacApLineatePortAclSwitchInbound_Object = MibTableColumn
hwMacApLineatePortAclSwitchInbound = _HwMacApLineatePortAclSwitchInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 21),
    _HwMacApLineatePortAclSwitchInbound_Type()
)
hwMacApLineatePortAclSwitchInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclSwitchInbound.setStatus("current")


class _HwMacApLineatePortAclSwitchOutbound_Type(Integer32):
    """Custom type hwMacApLineatePortAclSwitchOutbound based on Integer32"""
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


_HwMacApLineatePortAclSwitchOutbound_Type.__name__ = "Integer32"
_HwMacApLineatePortAclSwitchOutbound_Object = MibTableColumn
hwMacApLineatePortAclSwitchOutbound = _HwMacApLineatePortAclSwitchOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 22),
    _HwMacApLineatePortAclSwitchOutbound_Type()
)
hwMacApLineatePortAclSwitchOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclSwitchOutbound.setStatus("current")
_HwMacApLineatePortAclNumInboundIPV6_Type = Integer32
_HwMacApLineatePortAclNumInboundIPV6_Object = MibTableColumn
hwMacApLineatePortAclNumInboundIPV6 = _HwMacApLineatePortAclNumInboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 23),
    _HwMacApLineatePortAclNumInboundIPV6_Type()
)
hwMacApLineatePortAclNumInboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNumInboundIPV6.setStatus("current")
_HwMacApLineatePortAclNumOutboundIPV6_Type = Integer32
_HwMacApLineatePortAclNumOutboundIPV6_Object = MibTableColumn
hwMacApLineatePortAclNumOutboundIPV6 = _HwMacApLineatePortAclNumOutboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 24),
    _HwMacApLineatePortAclNumOutboundIPV6_Type()
)
hwMacApLineatePortAclNumOutboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNumOutboundIPV6.setStatus("current")
_HwMacApLineatePortAclNameInboundIPV6_Type = OctetString
_HwMacApLineatePortAclNameInboundIPV6_Object = MibTableColumn
hwMacApLineatePortAclNameInboundIPV6 = _HwMacApLineatePortAclNameInboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 25),
    _HwMacApLineatePortAclNameInboundIPV6_Type()
)
hwMacApLineatePortAclNameInboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNameInboundIPV6.setStatus("current")
_HwMacApLineatePortAclNameOutboundIPV6_Type = OctetString
_HwMacApLineatePortAclNameOutboundIPV6_Object = MibTableColumn
hwMacApLineatePortAclNameOutboundIPV6 = _HwMacApLineatePortAclNameOutboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 26),
    _HwMacApLineatePortAclNameOutboundIPV6_Type()
)
hwMacApLineatePortAclNameOutboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclNameOutboundIPV6.setStatus("current")


class _HwMacApLineatePortAclSwitchInboundIPV6_Type(Integer32):
    """Custom type hwMacApLineatePortAclSwitchInboundIPV6 based on Integer32"""
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


_HwMacApLineatePortAclSwitchInboundIPV6_Type.__name__ = "Integer32"
_HwMacApLineatePortAclSwitchInboundIPV6_Object = MibTableColumn
hwMacApLineatePortAclSwitchInboundIPV6 = _HwMacApLineatePortAclSwitchInboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 27),
    _HwMacApLineatePortAclSwitchInboundIPV6_Type()
)
hwMacApLineatePortAclSwitchInboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclSwitchInboundIPV6.setStatus("current")


class _HwMacApLineatePortAclSwitchOutboundIPV6_Type(Integer32):
    """Custom type hwMacApLineatePortAclSwitchOutboundIPV6 based on Integer32"""
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


_HwMacApLineatePortAclSwitchOutboundIPV6_Type.__name__ = "Integer32"
_HwMacApLineatePortAclSwitchOutboundIPV6_Object = MibTableColumn
hwMacApLineatePortAclSwitchOutboundIPV6 = _HwMacApLineatePortAclSwitchOutboundIPV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 28),
    _HwMacApLineatePortAclSwitchOutboundIPV6_Type()
)
hwMacApLineatePortAclSwitchOutboundIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortAclSwitchOutboundIPV6.setStatus("current")


class _HwMacApMultiLineatePortIsAddInTrunk_Type(Integer32):
    """Custom type hwMacApMultiLineatePortIsAddInTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("exit", 1),
          ("unknown", -1))
    )


_HwMacApMultiLineatePortIsAddInTrunk_Type.__name__ = "Integer32"
_HwMacApMultiLineatePortIsAddInTrunk_Object = MibTableColumn
hwMacApMultiLineatePortIsAddInTrunk = _HwMacApMultiLineatePortIsAddInTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 29),
    _HwMacApMultiLineatePortIsAddInTrunk_Type()
)
hwMacApMultiLineatePortIsAddInTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortIsAddInTrunk.setStatus("current")
_HwMacApMultiLineatePortAddedOrExitTrunkID_Type = Integer32
_HwMacApMultiLineatePortAddedOrExitTrunkID_Object = MibTableColumn
hwMacApMultiLineatePortAddedOrExitTrunkID = _HwMacApMultiLineatePortAddedOrExitTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 10, 1, 30),
    _HwMacApMultiLineatePortAddedOrExitTrunkID_Type()
)
hwMacApMultiLineatePortAddedOrExitTrunkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApMultiLineatePortAddedOrExitTrunkID.setStatus("current")
_HwMacApPerformanceStatTable_Object = MibTable
hwMacApPerformanceStatTable = _HwMacApPerformanceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11)
)
if mibBuilder.loadTexts:
    hwMacApPerformanceStatTable.setStatus("current")
_HwMacApPerformanceStatEntry_Object = MibTableRow
hwMacApPerformanceStatEntry = _HwMacApPerformanceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1)
)
hwMacApPerformanceStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
)
if mibBuilder.loadTexts:
    hwMacApPerformanceStatEntry.setStatus("current")
_HwMacApMemoryUseRate_Type = Integer32
_HwMacApMemoryUseRate_Object = MibTableColumn
hwMacApMemoryUseRate = _HwMacApMemoryUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 1),
    _HwMacApMemoryUseRate_Type()
)
hwMacApMemoryUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApMemoryUseRate.setStatus("current")
_HwMacApCpuUseRate_Type = Integer32
_HwMacApCpuUseRate_Object = MibTableColumn
hwMacApCpuUseRate = _HwMacApCpuUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 2),
    _HwMacApCpuUseRate_Type()
)
hwMacApCpuUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApCpuUseRate.setStatus("current")
_HwMacApFlashFreeSize_Type = Integer32
_HwMacApFlashFreeSize_Object = MibTableColumn
hwMacApFlashFreeSize = _HwMacApFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 3),
    _HwMacApFlashFreeSize_Type()
)
hwMacApFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApFlashFreeSize.setStatus("current")
_HwMacApTemperature_Type = Integer32
_HwMacApTemperature_Object = MibTableColumn
hwMacApTemperature = _HwMacApTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 4),
    _HwMacApTemperature_Type()
)
hwMacApTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApTemperature.setStatus("current")
_HwMacApOnlineUserNum_Type = Integer32
_HwMacApOnlineUserNum_Object = MibTableColumn
hwMacApOnlineUserNum = _HwMacApOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 5),
    _HwMacApOnlineUserNum_Type()
)
hwMacApOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOnlineUserNum.setStatus("current")
_HwMacApUpPortSpeed_Type = Integer32
_HwMacApUpPortSpeed_Object = MibTableColumn
hwMacApUpPortSpeed = _HwMacApUpPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 6),
    _HwMacApUpPortSpeed_Type()
)
hwMacApUpPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortSpeed.setStatus("current")
_HwMacApUpPortRecvFrames_Type = Unsigned32
_HwMacApUpPortRecvFrames_Object = MibTableColumn
hwMacApUpPortRecvFrames = _HwMacApUpPortRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 7),
    _HwMacApUpPortRecvFrames_Type()
)
hwMacApUpPortRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvFrames.setStatus("current")
_HwMacApUpPortRecvRightFrames_Type = Unsigned32
_HwMacApUpPortRecvRightFrames_Object = MibTableColumn
hwMacApUpPortRecvRightFrames = _HwMacApUpPortRecvRightFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 8),
    _HwMacApUpPortRecvRightFrames_Type()
)
hwMacApUpPortRecvRightFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvRightFrames.setStatus("current")
_HwMacApUpPortRecvErrorFrames_Type = Unsigned32
_HwMacApUpPortRecvErrorFrames_Object = MibTableColumn
hwMacApUpPortRecvErrorFrames = _HwMacApUpPortRecvErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 9),
    _HwMacApUpPortRecvErrorFrames_Type()
)
hwMacApUpPortRecvErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvErrorFrames.setStatus("current")
_HwMacApUpPortSendFrames_Type = Unsigned32
_HwMacApUpPortSendFrames_Object = MibTableColumn
hwMacApUpPortSendFrames = _HwMacApUpPortSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 10),
    _HwMacApUpPortSendFrames_Type()
)
hwMacApUpPortSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortSendFrames.setStatus("current")
_HwMacApUpPortRecvBytes_Type = Unsigned32
_HwMacApUpPortRecvBytes_Object = MibTableColumn
hwMacApUpPortRecvBytes = _HwMacApUpPortRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 11),
    _HwMacApUpPortRecvBytes_Type()
)
hwMacApUpPortRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvBytes.setStatus("current")
_HwMacApUpPortSendBytes_Type = Unsigned32
_HwMacApUpPortSendBytes_Object = MibTableColumn
hwMacApUpPortSendBytes = _HwMacApUpPortSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 12),
    _HwMacApUpPortSendBytes_Type()
)
hwMacApUpPortSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortSendBytes.setStatus("current")
_HwMacAPUpPortPER_Type = Integer32
_HwMacAPUpPortPER_Object = MibTableColumn
hwMacAPUpPortPER = _HwMacAPUpPortPER_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 13),
    _HwMacAPUpPortPER_Type()
)
hwMacAPUpPortPER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAPUpPortPER.setStatus("current")
_HwMacAPWirelessUpPortTraffic_Type = Unsigned32
_HwMacAPWirelessUpPortTraffic_Object = MibTableColumn
hwMacAPWirelessUpPortTraffic = _HwMacAPWirelessUpPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 14),
    _HwMacAPWirelessUpPortTraffic_Type()
)
hwMacAPWirelessUpPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAPWirelessUpPortTraffic.setStatus("current")
_HwMacAPUpPortTraffic_Type = Unsigned32
_HwMacAPUpPortTraffic_Object = MibTableColumn
hwMacAPUpPortTraffic = _HwMacAPUpPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 15),
    _HwMacAPUpPortTraffic_Type()
)
hwMacAPUpPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAPUpPortTraffic.setStatus("current")
_HwMacApAirportSendDropFrames_Type = Unsigned32
_HwMacApAirportSendDropFrames_Object = MibTableColumn
hwMacApAirportSendDropFrames = _HwMacApAirportSendDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 16),
    _HwMacApAirportSendDropFrames_Type()
)
hwMacApAirportSendDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportSendDropFrames.setStatus("current")
_HwMacApEthportRecvDropFrames_Type = Unsigned32
_HwMacApEthportRecvDropFrames_Object = MibTableColumn
hwMacApEthportRecvDropFrames = _HwMacApEthportRecvDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 17),
    _HwMacApEthportRecvDropFrames_Type()
)
hwMacApEthportRecvDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportRecvDropFrames.setStatus("current")
_HwMacApAirportUpTraffic_Type = OctetString
_HwMacApAirportUpTraffic_Object = MibTableColumn
hwMacApAirportUpTraffic = _HwMacApAirportUpTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 18),
    _HwMacApAirportUpTraffic_Type()
)
hwMacApAirportUpTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportUpTraffic.setStatus("current")
_HwMacApAirportDwTraffic_Type = OctetString
_HwMacApAirportDwTraffic_Object = MibTableColumn
hwMacApAirportDwTraffic = _HwMacApAirportDwTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 19),
    _HwMacApAirportDwTraffic_Type()
)
hwMacApAirportDwTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportDwTraffic.setStatus("current")
_HwMacApEthportDwTraffic_Type = OctetString
_HwMacApEthportDwTraffic_Object = MibTableColumn
hwMacApEthportDwTraffic = _HwMacApEthportDwTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 20),
    _HwMacApEthportDwTraffic_Type()
)
hwMacApEthportDwTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportDwTraffic.setStatus("current")
_HwMacApEthportUpTraffic_Type = OctetString
_HwMacApEthportUpTraffic_Object = MibTableColumn
hwMacApEthportUpTraffic = _HwMacApEthportUpTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 21),
    _HwMacApEthportUpTraffic_Type()
)
hwMacApEthportUpTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportUpTraffic.setStatus("current")
_HwMacApAirportRecvDropPacket_Type = Unsigned32
_HwMacApAirportRecvDropPacket_Object = MibTableColumn
hwMacApAirportRecvDropPacket = _HwMacApAirportRecvDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 22),
    _HwMacApAirportRecvDropPacket_Type()
)
hwMacApAirportRecvDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportRecvDropPacket.setStatus("current")
_HwMacApAirportRecvErrorPacket_Type = Unsigned32
_HwMacApAirportRecvErrorPacket_Object = MibTableColumn
hwMacApAirportRecvErrorPacket = _HwMacApAirportRecvErrorPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 23),
    _HwMacApAirportRecvErrorPacket_Type()
)
hwMacApAirportRecvErrorPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportRecvErrorPacket.setStatus("current")
_HwMacApEthportRecvUnicastPacket_Type = Unsigned32
_HwMacApEthportRecvUnicastPacket_Object = MibTableColumn
hwMacApEthportRecvUnicastPacket = _HwMacApEthportRecvUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 24),
    _HwMacApEthportRecvUnicastPacket_Type()
)
hwMacApEthportRecvUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportRecvUnicastPacket.setStatus("current")
_HwMacApEthportRecvNonUnicastPacket_Type = Unsigned32
_HwMacApEthportRecvNonUnicastPacket_Object = MibTableColumn
hwMacApEthportRecvNonUnicastPacket = _HwMacApEthportRecvNonUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 25),
    _HwMacApEthportRecvNonUnicastPacket_Type()
)
hwMacApEthportRecvNonUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportRecvNonUnicastPacket.setStatus("current")
_HwMacApEthportSendUnicastPacket_Type = Unsigned32
_HwMacApEthportSendUnicastPacket_Object = MibTableColumn
hwMacApEthportSendUnicastPacket = _HwMacApEthportSendUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 26),
    _HwMacApEthportSendUnicastPacket_Type()
)
hwMacApEthportSendUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportSendUnicastPacket.setStatus("current")
_HwMacApEthportSendNonUnicastPacket_Type = Unsigned32
_HwMacApEthportSendNonUnicastPacket_Object = MibTableColumn
hwMacApEthportSendNonUnicastPacket = _HwMacApEthportSendNonUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 27),
    _HwMacApEthportSendNonUnicastPacket_Type()
)
hwMacApEthportSendNonUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportSendNonUnicastPacket.setStatus("current")
_HwMacApAvgRCPUUseRate_Type = Integer32
_HwMacApAvgRCPUUseRate_Object = MibTableColumn
hwMacApAvgRCPUUseRate = _HwMacApAvgRCPUUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 28),
    _HwMacApAvgRCPUUseRate_Type()
)
hwMacApAvgRCPUUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAvgRCPUUseRate.setStatus("current")
_HwMacApAvgRMemoryUseRate_Type = Integer32
_HwMacApAvgRMemoryUseRate_Object = MibTableColumn
hwMacApAvgRMemoryUseRate = _HwMacApAvgRMemoryUseRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 29),
    _HwMacApAvgRMemoryUseRate_Type()
)
hwMacApAvgRMemoryUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAvgRMemoryUseRate.setStatus("current")
_HwMacEthportSendDropFrames_Type = Counter64
_HwMacEthportSendDropFrames_Object = MibTableColumn
hwMacEthportSendDropFrames = _HwMacEthportSendDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 30),
    _HwMacEthportSendDropFrames_Type()
)
hwMacEthportSendDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacEthportSendDropFrames.setStatus("current")
_HwMacEthportSendErrorFrames_Type = Counter64
_HwMacEthportSendErrorFrames_Object = MibTableColumn
hwMacEthportSendErrorFrames = _HwMacEthportSendErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 31),
    _HwMacEthportSendErrorFrames_Type()
)
hwMacEthportSendErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacEthportSendErrorFrames.setStatus("current")
_HwMacEthportUpDwnTimes_Type = Unsigned32
_HwMacEthportUpDwnTimes_Object = MibTableColumn
hwMacEthportUpDwnTimes = _HwMacEthportUpDwnTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 32),
    _HwMacEthportUpDwnTimes_Type()
)
hwMacEthportUpDwnTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacEthportUpDwnTimes.setStatus("current")
_HwMacApAirportRecvUnicastFrames_Type = Counter64
_HwMacApAirportRecvUnicastFrames_Object = MibTableColumn
hwMacApAirportRecvUnicastFrames = _HwMacApAirportRecvUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 33),
    _HwMacApAirportRecvUnicastFrames_Type()
)
hwMacApAirportRecvUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportRecvUnicastFrames.setStatus("current")
_HwMacApEthportRecvUnknownFrames_Type = Counter64
_HwMacApEthportRecvUnknownFrames_Object = MibTableColumn
hwMacApEthportRecvUnknownFrames = _HwMacApEthportRecvUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 34),
    _HwMacApEthportRecvUnknownFrames_Type()
)
hwMacApEthportRecvUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportRecvUnknownFrames.setStatus("current")
_HwMacEthportUpRate_Type = Integer32
_HwMacEthportUpRate_Object = MibTableColumn
hwMacEthportUpRate = _HwMacEthportUpRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 35),
    _HwMacEthportUpRate_Type()
)
hwMacEthportUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacEthportUpRate.setStatus("current")
_HwMacEthportDownRate_Type = Integer32
_HwMacEthportDownRate_Object = MibTableColumn
hwMacEthportDownRate = _HwMacEthportDownRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 36),
    _HwMacEthportDownRate_Type()
)
hwMacEthportDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacEthportDownRate.setStatus("current")
_HwMacApUpPortRecvFrames64Bits_Type = Counter64
_HwMacApUpPortRecvFrames64Bits_Object = MibTableColumn
hwMacApUpPortRecvFrames64Bits = _HwMacApUpPortRecvFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 37),
    _HwMacApUpPortRecvFrames64Bits_Type()
)
hwMacApUpPortRecvFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvFrames64Bits.setStatus("current")
_HwMacApUpPortRecvRightFrames64Bits_Type = Counter64
_HwMacApUpPortRecvRightFrames64Bits_Object = MibTableColumn
hwMacApUpPortRecvRightFrames64Bits = _HwMacApUpPortRecvRightFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 38),
    _HwMacApUpPortRecvRightFrames64Bits_Type()
)
hwMacApUpPortRecvRightFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvRightFrames64Bits.setStatus("current")
_HwMacApUpPortRecvErrorFrames64Bits_Type = Counter64
_HwMacApUpPortRecvErrorFrames64Bits_Object = MibTableColumn
hwMacApUpPortRecvErrorFrames64Bits = _HwMacApUpPortRecvErrorFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 39),
    _HwMacApUpPortRecvErrorFrames64Bits_Type()
)
hwMacApUpPortRecvErrorFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvErrorFrames64Bits.setStatus("current")
_HwMacApUpPortSendFrames64Bits_Type = Counter64
_HwMacApUpPortSendFrames64Bits_Object = MibTableColumn
hwMacApUpPortSendFrames64Bits = _HwMacApUpPortSendFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 40),
    _HwMacApUpPortSendFrames64Bits_Type()
)
hwMacApUpPortSendFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortSendFrames64Bits.setStatus("current")
_HwMacApUpPortRecvBytes64Bits_Type = Counter64
_HwMacApUpPortRecvBytes64Bits_Object = MibTableColumn
hwMacApUpPortRecvBytes64Bits = _HwMacApUpPortRecvBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 41),
    _HwMacApUpPortRecvBytes64Bits_Type()
)
hwMacApUpPortRecvBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortRecvBytes64Bits.setStatus("current")
_HwMacApUpPortSendBytes64Bits_Type = Counter64
_HwMacApUpPortSendBytes64Bits_Object = MibTableColumn
hwMacApUpPortSendBytes64Bits = _HwMacApUpPortSendBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 42),
    _HwMacApUpPortSendBytes64Bits_Type()
)
hwMacApUpPortSendBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApUpPortSendBytes64Bits.setStatus("current")
_HwMacAPWirelessUpPortTraffic64Bits_Type = Counter64
_HwMacAPWirelessUpPortTraffic64Bits_Object = MibTableColumn
hwMacAPWirelessUpPortTraffic64Bits = _HwMacAPWirelessUpPortTraffic64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 43),
    _HwMacAPWirelessUpPortTraffic64Bits_Type()
)
hwMacAPWirelessUpPortTraffic64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAPWirelessUpPortTraffic64Bits.setStatus("current")
_HwMacAPUpPortTraffic64Bits_Type = Counter64
_HwMacAPUpPortTraffic64Bits_Object = MibTableColumn
hwMacAPUpPortTraffic64Bits = _HwMacAPUpPortTraffic64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 44),
    _HwMacAPUpPortTraffic64Bits_Type()
)
hwMacAPUpPortTraffic64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAPUpPortTraffic64Bits.setStatus("current")
_HwMacApAirportSendDropFrames64Bits_Type = Counter64
_HwMacApAirportSendDropFrames64Bits_Object = MibTableColumn
hwMacApAirportSendDropFrames64Bits = _HwMacApAirportSendDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 45),
    _HwMacApAirportSendDropFrames64Bits_Type()
)
hwMacApAirportSendDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportSendDropFrames64Bits.setStatus("current")
_HwMacApEthportRecvDropFrames64Bits_Type = Counter64
_HwMacApEthportRecvDropFrames64Bits_Object = MibTableColumn
hwMacApEthportRecvDropFrames64Bits = _HwMacApEthportRecvDropFrames64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 46),
    _HwMacApEthportRecvDropFrames64Bits_Type()
)
hwMacApEthportRecvDropFrames64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportRecvDropFrames64Bits.setStatus("current")
_HwMacApAirportRecvDropPacket64Bits_Type = Counter64
_HwMacApAirportRecvDropPacket64Bits_Object = MibTableColumn
hwMacApAirportRecvDropPacket64Bits = _HwMacApAirportRecvDropPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 47),
    _HwMacApAirportRecvDropPacket64Bits_Type()
)
hwMacApAirportRecvDropPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportRecvDropPacket64Bits.setStatus("current")
_HwMacApAirportRecvErrorPacket64Bits_Type = Counter64
_HwMacApAirportRecvErrorPacket64Bits_Object = MibTableColumn
hwMacApAirportRecvErrorPacket64Bits = _HwMacApAirportRecvErrorPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 48),
    _HwMacApAirportRecvErrorPacket64Bits_Type()
)
hwMacApAirportRecvErrorPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApAirportRecvErrorPacket64Bits.setStatus("current")
_HwMacApEthportRecvUnicastPacket64Bits_Type = Counter64
_HwMacApEthportRecvUnicastPacket64Bits_Object = MibTableColumn
hwMacApEthportRecvUnicastPacket64Bits = _HwMacApEthportRecvUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 49),
    _HwMacApEthportRecvUnicastPacket64Bits_Type()
)
hwMacApEthportRecvUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportRecvUnicastPacket64Bits.setStatus("current")
_HwMacApEthportRecvNonUnicastPacket64Bits_Type = Counter64
_HwMacApEthportRecvNonUnicastPacket64Bits_Object = MibTableColumn
hwMacApEthportRecvNonUnicastPacket64Bits = _HwMacApEthportRecvNonUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 50),
    _HwMacApEthportRecvNonUnicastPacket64Bits_Type()
)
hwMacApEthportRecvNonUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportRecvNonUnicastPacket64Bits.setStatus("current")
_HwMacApEthportSendUnicastPacket64Bits_Type = Counter64
_HwMacApEthportSendUnicastPacket64Bits_Object = MibTableColumn
hwMacApEthportSendUnicastPacket64Bits = _HwMacApEthportSendUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 51),
    _HwMacApEthportSendUnicastPacket64Bits_Type()
)
hwMacApEthportSendUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportSendUnicastPacket64Bits.setStatus("current")
_HwMacApEthportSendNonUnicastPacket64Bits_Type = Counter64
_HwMacApEthportSendNonUnicastPacket64Bits_Object = MibTableColumn
hwMacApEthportSendNonUnicastPacket64Bits = _HwMacApEthportSendNonUnicastPacket64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 11, 1, 52),
    _HwMacApEthportSendNonUnicastPacket64Bits_Type()
)
hwMacApEthportSendNonUnicastPacket64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApEthportSendNonUnicastPacket64Bits.setStatus("current")
_HwApLineportInfoTable_Object = MibTable
hwApLineportInfoTable = _HwApLineportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12)
)
if mibBuilder.loadTexts:
    hwApLineportInfoTable.setStatus("current")
_HwApLineportInfoEntry_Object = MibTableRow
hwApLineportInfoEntry = _HwApLineportInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1)
)
hwApLineportInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineportIndex"),
)
if mibBuilder.loadTexts:
    hwApLineportInfoEntry.setStatus("current")


class _HwApLineportIndex_Type(Integer32):
    """Custom type hwApLineportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwApLineportIndex_Type.__name__ = "Integer32"
_HwApLineportIndex_Object = MibTableColumn
hwApLineportIndex = _HwApLineportIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 1),
    _HwApLineportIndex_Type()
)
hwApLineportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLineportIndex.setStatus("current")
_HwApLineportDesc_Type = OctetString
_HwApLineportDesc_Object = MibTableColumn
hwApLineportDesc = _HwApLineportDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 2),
    _HwApLineportDesc_Type()
)
hwApLineportDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineportDesc.setStatus("current")
_HwApLineportType_Type = OctetString
_HwApLineportType_Object = MibTableColumn
hwApLineportType = _HwApLineportType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 3),
    _HwApLineportType_Type()
)
hwApLineportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineportType.setStatus("current")
_HwApLineportMtu_Type = Integer32
_HwApLineportMtu_Object = MibTableColumn
hwApLineportMtu = _HwApLineportMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 4),
    _HwApLineportMtu_Type()
)
hwApLineportMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineportMtu.setStatus("current")
_HwApLineportSpeed_Type = Integer32
_HwApLineportSpeed_Object = MibTableColumn
hwApLineportSpeed = _HwApLineportSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 5),
    _HwApLineportSpeed_Type()
)
hwApLineportSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineportSpeed.setStatus("current")
_HwApLineportMac_Type = MacAddress
_HwApLineportMac_Object = MibTableColumn
hwApLineportMac = _HwApLineportMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 6),
    _HwApLineportMac_Type()
)
hwApLineportMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineportMac.setStatus("current")


class _HwApLineportAdminStatus_Type(Integer32):
    """Custom type hwApLineportAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 3),
          ("adminUp", 1),
          ("down", 2))
    )


_HwApLineportAdminStatus_Type.__name__ = "Integer32"
_HwApLineportAdminStatus_Object = MibTableColumn
hwApLineportAdminStatus = _HwApLineportAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 7),
    _HwApLineportAdminStatus_Type()
)
hwApLineportAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineportAdminStatus.setStatus("current")
_HwApLineportNum_Type = Integer32
_HwApLineportNum_Object = MibTableColumn
hwApLineportNum = _HwApLineportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 12, 1, 8),
    _HwApLineportNum_Type()
)
hwApLineportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineportNum.setStatus("current")
_HwMacApLineportInfoTable_Object = MibTable
hwMacApLineportInfoTable = _HwMacApLineportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13)
)
if mibBuilder.loadTexts:
    hwMacApLineportInfoTable.setStatus("current")
_HwMacApLineportInfoEntry_Object = MibTableRow
hwMacApLineportInfoEntry = _HwMacApLineportInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1)
)
hwMacApLineportInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportIndex"),
)
if mibBuilder.loadTexts:
    hwMacApLineportInfoEntry.setStatus("current")


class _HwMacApLineportIndex_Type(Integer32):
    """Custom type hwMacApLineportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwMacApLineportIndex_Type.__name__ = "Integer32"
_HwMacApLineportIndex_Object = MibTableColumn
hwMacApLineportIndex = _HwMacApLineportIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 1),
    _HwMacApLineportIndex_Type()
)
hwMacApLineportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApLineportIndex.setStatus("current")
_HwMacApLineportDesc_Type = OctetString
_HwMacApLineportDesc_Object = MibTableColumn
hwMacApLineportDesc = _HwMacApLineportDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 2),
    _HwMacApLineportDesc_Type()
)
hwMacApLineportDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineportDesc.setStatus("current")
_HwMacApLineportType_Type = OctetString
_HwMacApLineportType_Object = MibTableColumn
hwMacApLineportType = _HwMacApLineportType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 3),
    _HwMacApLineportType_Type()
)
hwMacApLineportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineportType.setStatus("current")
_HwMacApLineportMtu_Type = Integer32
_HwMacApLineportMtu_Object = MibTableColumn
hwMacApLineportMtu = _HwMacApLineportMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 4),
    _HwMacApLineportMtu_Type()
)
hwMacApLineportMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineportMtu.setStatus("current")
_HwMacApLineportSpeed_Type = Integer32
_HwMacApLineportSpeed_Object = MibTableColumn
hwMacApLineportSpeed = _HwMacApLineportSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 5),
    _HwMacApLineportSpeed_Type()
)
hwMacApLineportSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineportSpeed.setStatus("current")
_HwMacApLineportMac_Type = MacAddress
_HwMacApLineportMac_Object = MibTableColumn
hwMacApLineportMac = _HwMacApLineportMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 6),
    _HwMacApLineportMac_Type()
)
hwMacApLineportMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineportMac.setStatus("current")


class _HwMacApLineportAdminStatus_Type(Integer32):
    """Custom type hwMacApLineportAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 3),
          ("adminUp", 1),
          ("down1", 2))
    )


_HwMacApLineportAdminStatus_Type.__name__ = "Integer32"
_HwMacApLineportAdminStatus_Object = MibTableColumn
hwMacApLineportAdminStatus = _HwMacApLineportAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 7),
    _HwMacApLineportAdminStatus_Type()
)
hwMacApLineportAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineportAdminStatus.setStatus("current")
_HwMacApLineportNum_Type = Integer32
_HwMacApLineportNum_Object = MibTableColumn
hwMacApLineportNum = _HwMacApLineportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 13, 1, 8),
    _HwMacApLineportNum_Type()
)
hwMacApLineportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineportNum.setStatus("current")
_HwApLldpTable_Object = MibTable
hwApLldpTable = _HwApLldpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14)
)
if mibBuilder.loadTexts:
    hwApLldpTable.setStatus("current")
_HwApLldpEntry_Object = MibTableRow
hwApLldpEntry = _HwApLldpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1)
)
hwApLldpEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemIndex"),
)
if mibBuilder.loadTexts:
    hwApLldpEntry.setStatus("current")
_HwApLldpRemLocalPortNum_Type = Integer32
_HwApLldpRemLocalPortNum_Object = MibTableColumn
hwApLldpRemLocalPortNum = _HwApLldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 1),
    _HwApLldpRemLocalPortNum_Type()
)
hwApLldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLldpRemLocalPortNum.setStatus("current")
_HwApLldpRemIndex_Type = Integer32
_HwApLldpRemIndex_Object = MibTableColumn
hwApLldpRemIndex = _HwApLldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 2),
    _HwApLldpRemIndex_Type()
)
hwApLldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLldpRemIndex.setStatus("current")
_HwApLldpRemChassisIdSubtype_Type = Integer32
_HwApLldpRemChassisIdSubtype_Object = MibTableColumn
hwApLldpRemChassisIdSubtype = _HwApLldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 3),
    _HwApLldpRemChassisIdSubtype_Type()
)
hwApLldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemChassisIdSubtype.setStatus("current")


class _HwApLldpRemChassisId_Type(OctetString):
    """Custom type hwApLldpRemChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLldpRemChassisId_Type.__name__ = "OctetString"
_HwApLldpRemChassisId_Object = MibTableColumn
hwApLldpRemChassisId = _HwApLldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 4),
    _HwApLldpRemChassisId_Type()
)
hwApLldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemChassisId.setStatus("current")
_HwApLldpRemPortIdSubtype_Type = Integer32
_HwApLldpRemPortIdSubtype_Object = MibTableColumn
hwApLldpRemPortIdSubtype = _HwApLldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 5),
    _HwApLldpRemPortIdSubtype_Type()
)
hwApLldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemPortIdSubtype.setStatus("current")


class _HwApLldpRemPortId_Type(OctetString):
    """Custom type hwApLldpRemPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLldpRemPortId_Type.__name__ = "OctetString"
_HwApLldpRemPortId_Object = MibTableColumn
hwApLldpRemPortId = _HwApLldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 6),
    _HwApLldpRemPortId_Type()
)
hwApLldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemPortId.setStatus("current")


class _HwApLldpRemPortDesc_Type(OctetString):
    """Custom type hwApLldpRemPortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLldpRemPortDesc_Type.__name__ = "OctetString"
_HwApLldpRemPortDesc_Object = MibTableColumn
hwApLldpRemPortDesc = _HwApLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 7),
    _HwApLldpRemPortDesc_Type()
)
hwApLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemPortDesc.setStatus("current")


class _HwApLldpRemSysName_Type(OctetString):
    """Custom type hwApLldpRemSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLldpRemSysName_Type.__name__ = "OctetString"
_HwApLldpRemSysName_Object = MibTableColumn
hwApLldpRemSysName = _HwApLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 8),
    _HwApLldpRemSysName_Type()
)
hwApLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemSysName.setStatus("current")


class _HwApLldpRemSysDesc_Type(OctetString):
    """Custom type hwApLldpRemSysDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLldpRemSysDesc_Type.__name__ = "OctetString"
_HwApLldpRemSysDesc_Object = MibTableColumn
hwApLldpRemSysDesc = _HwApLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 9),
    _HwApLldpRemSysDesc_Type()
)
hwApLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemSysDesc.setStatus("current")
_HwApLldpRemSysCapSupported_Type = Integer32
_HwApLldpRemSysCapSupported_Object = MibTableColumn
hwApLldpRemSysCapSupported = _HwApLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 10),
    _HwApLldpRemSysCapSupported_Type()
)
hwApLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemSysCapSupported.setStatus("current")
_HwApLldpRemSysCapEnabled_Type = Integer32
_HwApLldpRemSysCapEnabled_Object = MibTableColumn
hwApLldpRemSysCapEnabled = _HwApLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 14, 1, 11),
    _HwApLldpRemSysCapEnabled_Type()
)
hwApLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemSysCapEnabled.setStatus("current")
_HwMacApLldpTable_Object = MibTable
hwMacApLldpTable = _HwMacApLldpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15)
)
if mibBuilder.loadTexts:
    hwMacApLldpTable.setStatus("current")
_HwMacApLldpEntry_Object = MibTableRow
hwMacApLldpEntry = _HwMacApLldpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1)
)
hwMacApLldpEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemIndex"),
)
if mibBuilder.loadTexts:
    hwMacApLldpEntry.setStatus("current")
_HwMacApLldpRemLocalPortNum_Type = Integer32
_HwMacApLldpRemLocalPortNum_Object = MibTableColumn
hwMacApLldpRemLocalPortNum = _HwMacApLldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 1),
    _HwMacApLldpRemLocalPortNum_Type()
)
hwMacApLldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApLldpRemLocalPortNum.setStatus("current")
_HwMacApLldpRemIndex_Type = Integer32
_HwMacApLldpRemIndex_Object = MibTableColumn
hwMacApLldpRemIndex = _HwMacApLldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 2),
    _HwMacApLldpRemIndex_Type()
)
hwMacApLldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApLldpRemIndex.setStatus("current")
_HwMacApLldpRemChassisIdSubtype_Type = Integer32
_HwMacApLldpRemChassisIdSubtype_Object = MibTableColumn
hwMacApLldpRemChassisIdSubtype = _HwMacApLldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 3),
    _HwMacApLldpRemChassisIdSubtype_Type()
)
hwMacApLldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemChassisIdSubtype.setStatus("current")


class _HwMacApLldpRemChassisId_Type(OctetString):
    """Custom type hwMacApLldpRemChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLldpRemChassisId_Type.__name__ = "OctetString"
_HwMacApLldpRemChassisId_Object = MibTableColumn
hwMacApLldpRemChassisId = _HwMacApLldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 4),
    _HwMacApLldpRemChassisId_Type()
)
hwMacApLldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemChassisId.setStatus("current")
_HwMacApLldpRemPortIdSubtype_Type = Integer32
_HwMacApLldpRemPortIdSubtype_Object = MibTableColumn
hwMacApLldpRemPortIdSubtype = _HwMacApLldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 5),
    _HwMacApLldpRemPortIdSubtype_Type()
)
hwMacApLldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemPortIdSubtype.setStatus("current")


class _HwMacApLldpRemPortId_Type(OctetString):
    """Custom type hwMacApLldpRemPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLldpRemPortId_Type.__name__ = "OctetString"
_HwMacApLldpRemPortId_Object = MibTableColumn
hwMacApLldpRemPortId = _HwMacApLldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 6),
    _HwMacApLldpRemPortId_Type()
)
hwMacApLldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemPortId.setStatus("current")


class _HwMacApLldpRemPortDesc_Type(OctetString):
    """Custom type hwMacApLldpRemPortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLldpRemPortDesc_Type.__name__ = "OctetString"
_HwMacApLldpRemPortDesc_Object = MibTableColumn
hwMacApLldpRemPortDesc = _HwMacApLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 7),
    _HwMacApLldpRemPortDesc_Type()
)
hwMacApLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemPortDesc.setStatus("current")


class _HwMacApLldpRemSysName_Type(OctetString):
    """Custom type hwMacApLldpRemSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLldpRemSysName_Type.__name__ = "OctetString"
_HwMacApLldpRemSysName_Object = MibTableColumn
hwMacApLldpRemSysName = _HwMacApLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 8),
    _HwMacApLldpRemSysName_Type()
)
hwMacApLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemSysName.setStatus("current")


class _HwMacApLldpRemSysDesc_Type(OctetString):
    """Custom type hwMacApLldpRemSysDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLldpRemSysDesc_Type.__name__ = "OctetString"
_HwMacApLldpRemSysDesc_Object = MibTableColumn
hwMacApLldpRemSysDesc = _HwMacApLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 9),
    _HwMacApLldpRemSysDesc_Type()
)
hwMacApLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemSysDesc.setStatus("current")
_HwMacApLldpRemSysCapSupported_Type = Integer32
_HwMacApLldpRemSysCapSupported_Object = MibTableColumn
hwMacApLldpRemSysCapSupported = _HwMacApLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 10),
    _HwMacApLldpRemSysCapSupported_Type()
)
hwMacApLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemSysCapSupported.setStatus("current")
_HwMacApLldpRemSysCapEnabled_Type = Integer32
_HwMacApLldpRemSysCapEnabled_Object = MibTableColumn
hwMacApLldpRemSysCapEnabled = _HwMacApLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 15, 1, 11),
    _HwMacApLldpRemSysCapEnabled_Type()
)
hwMacApLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLldpRemSysCapEnabled.setStatus("current")
_HwAplldpRemManAddrTable_Object = MibTable
hwAplldpRemManAddrTable = _HwAplldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 16)
)
if mibBuilder.loadTexts:
    hwAplldpRemManAddrTable.setStatus("current")
_HwAplldpRemManAddrEntry_Object = MibTableRow
hwAplldpRemManAddrEntry = _HwAplldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 16, 1)
)
hwAplldpRemManAddrEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemManAddrSubtype"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    hwAplldpRemManAddrEntry.setStatus("current")
_HwApLldpRemManAddrSubtype_Type = Integer32
_HwApLldpRemManAddrSubtype_Object = MibTableColumn
hwApLldpRemManAddrSubtype = _HwApLldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 16, 1, 1),
    _HwApLldpRemManAddrSubtype_Type()
)
hwApLldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLldpRemManAddrSubtype.setStatus("current")


class _HwApLldpRemManAddr_Type(OctetString):
    """Custom type hwApLldpRemManAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwApLldpRemManAddr_Type.__name__ = "OctetString"
_HwApLldpRemManAddr_Object = MibTableColumn
hwApLldpRemManAddr = _HwApLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 16, 1, 2),
    _HwApLldpRemManAddr_Type()
)
hwApLldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLldpRemManAddr.setStatus("current")
_HwApLldpRemManAddrIfSubtype_Type = Integer32
_HwApLldpRemManAddrIfSubtype_Object = MibTableColumn
hwApLldpRemManAddrIfSubtype = _HwApLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 16, 1, 3),
    _HwApLldpRemManAddrIfSubtype_Type()
)
hwApLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemManAddrIfSubtype.setStatus("current")
_HwApLldpRemManAddrIfId_Type = Integer32
_HwApLldpRemManAddrIfId_Object = MibTableColumn
hwApLldpRemManAddrIfId = _HwApLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 16, 1, 4),
    _HwApLldpRemManAddrIfId_Type()
)
hwApLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemManAddrIfId.setStatus("current")


class _HwApLldpRemManAddrOID_Type(OctetString):
    """Custom type hwApLldpRemManAddrOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwApLldpRemManAddrOID_Type.__name__ = "OctetString"
_HwApLldpRemManAddrOID_Object = MibTableColumn
hwApLldpRemManAddrOID = _HwApLldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 16, 1, 5),
    _HwApLldpRemManAddrOID_Type()
)
hwApLldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLldpRemManAddrOID.setStatus("current")
_HwMacAplldpRemManAddrTable_Object = MibTable
hwMacAplldpRemManAddrTable = _HwMacAplldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 17)
)
if mibBuilder.loadTexts:
    hwMacAplldpRemManAddrTable.setStatus("current")
_HwMacAplldpRemManAddrEntry_Object = MibTableRow
hwMacAplldpRemManAddrEntry = _HwMacAplldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 17, 1)
)
hwMacAplldpRemManAddrEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMACApLldpRemManAddrSubtype"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMACApLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    hwMacAplldpRemManAddrEntry.setStatus("current")
_HwMACApLldpRemManAddrSubtype_Type = Integer32
_HwMACApLldpRemManAddrSubtype_Object = MibTableColumn
hwMACApLldpRemManAddrSubtype = _HwMACApLldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 17, 1, 1),
    _HwMACApLldpRemManAddrSubtype_Type()
)
hwMACApLldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMACApLldpRemManAddrSubtype.setStatus("current")


class _HwMACApLldpRemManAddr_Type(OctetString):
    """Custom type hwMACApLldpRemManAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwMACApLldpRemManAddr_Type.__name__ = "OctetString"
_HwMACApLldpRemManAddr_Object = MibTableColumn
hwMACApLldpRemManAddr = _HwMACApLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 17, 1, 2),
    _HwMACApLldpRemManAddr_Type()
)
hwMACApLldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMACApLldpRemManAddr.setStatus("current")
_HwMACApLldpRemManAddrIfSubtype_Type = Integer32
_HwMACApLldpRemManAddrIfSubtype_Object = MibTableColumn
hwMACApLldpRemManAddrIfSubtype = _HwMACApLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 17, 1, 3),
    _HwMACApLldpRemManAddrIfSubtype_Type()
)
hwMACApLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLldpRemManAddrIfSubtype.setStatus("current")
_HwMACApLldpRemManAddrIfId_Type = Integer32
_HwMACApLldpRemManAddrIfId_Object = MibTableColumn
hwMACApLldpRemManAddrIfId = _HwMACApLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 17, 1, 4),
    _HwMACApLldpRemManAddrIfId_Type()
)
hwMACApLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLldpRemManAddrIfId.setStatus("current")


class _HwMACApLldpRemManAddrOID_Type(OctetString):
    """Custom type hwMACApLldpRemManAddrOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwMACApLldpRemManAddrOID_Type.__name__ = "OctetString"
_HwMACApLldpRemManAddrOID_Object = MibTableColumn
hwMACApLldpRemManAddrOID = _HwMACApLldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 17, 1, 5),
    _HwMACApLldpRemManAddrOID_Type()
)
hwMACApLldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLldpRemManAddrOID.setStatus("current")
_HwApOpticalInfoTable_Object = MibTable
hwApOpticalInfoTable = _HwApOpticalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18)
)
if mibBuilder.loadTexts:
    hwApOpticalInfoTable.setStatus("current")
_HwApOpticalInfoEntry_Object = MibTableRow
hwApOpticalInfoEntry = _HwApOpticalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1)
)
hwApOpticalInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
)
if mibBuilder.loadTexts:
    hwApOpticalInfoEntry.setStatus("current")
_HwApOpticalNominalBitRate_Type = Integer32
_HwApOpticalNominalBitRate_Object = MibTableColumn
hwApOpticalNominalBitRate = _HwApOpticalNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 1),
    _HwApOpticalNominalBitRate_Type()
)
hwApOpticalNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalNominalBitRate.setStatus("current")
_HwApOpticalLinkLen9X125km_Type = Integer32
_HwApOpticalLinkLen9X125km_Object = MibTableColumn
hwApOpticalLinkLen9X125km = _HwApOpticalLinkLen9X125km_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 2),
    _HwApOpticalLinkLen9X125km_Type()
)
hwApOpticalLinkLen9X125km.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalLinkLen9X125km.setStatus("current")
_HwApOpticalLinkLen50X125X100m_Type = Integer32
_HwApOpticalLinkLen50X125X100m_Object = MibTableColumn
hwApOpticalLinkLen50X125X100m = _HwApOpticalLinkLen50X125X100m_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 3),
    _HwApOpticalLinkLen50X125X100m_Type()
)
hwApOpticalLinkLen50X125X100m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalLinkLen50X125X100m.setStatus("current")
_HwApOpticalLinkLen62p5X125X10m_Type = Integer32
_HwApOpticalLinkLen62p5X125X10m_Object = MibTableColumn
hwApOpticalLinkLen62p5X125X10m = _HwApOpticalLinkLen62p5X125X10m_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 4),
    _HwApOpticalLinkLen62p5X125X10m_Type()
)
hwApOpticalLinkLen62p5X125X10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalLinkLen62p5X125X10m.setStatus("current")
_HwApOpticalLinkLenCopper_Type = Integer32
_HwApOpticalLinkLenCopper_Object = MibTableColumn
hwApOpticalLinkLenCopper = _HwApOpticalLinkLenCopper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 5),
    _HwApOpticalLinkLenCopper_Type()
)
hwApOpticalLinkLenCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalLinkLenCopper.setStatus("current")
_HwApOpticalSfpConnector_Type = OctetString
_HwApOpticalSfpConnector_Object = MibTableColumn
hwApOpticalSfpConnector = _HwApOpticalSfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 6),
    _HwApOpticalSfpConnector_Type()
)
hwApOpticalSfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalSfpConnector.setStatus("current")
_HwApOpticalDdmVoltage_Type = Integer32
_HwApOpticalDdmVoltage_Object = MibTableColumn
hwApOpticalDdmVoltage = _HwApOpticalDdmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 7),
    _HwApOpticalDdmVoltage_Type()
)
hwApOpticalDdmVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalDdmVoltage.setStatus("current")
_HwApOpticalDdmTxBiasCurrent_Type = Integer32
_HwApOpticalDdmTxBiasCurrent_Object = MibTableColumn
hwApOpticalDdmTxBiasCurrent = _HwApOpticalDdmTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 8),
    _HwApOpticalDdmTxBiasCurrent_Type()
)
hwApOpticalDdmTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalDdmTxBiasCurrent.setStatus("current")
_HwApOpticalDdmTxPower_Type = Integer32
_HwApOpticalDdmTxPower_Object = MibTableColumn
hwApOpticalDdmTxPower = _HwApOpticalDdmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 9),
    _HwApOpticalDdmTxPower_Type()
)
hwApOpticalDdmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalDdmTxPower.setStatus("current")
_HwApOpticalDdmRxPower_Type = Integer32
_HwApOpticalDdmRxPower_Object = MibTableColumn
hwApOpticalDdmRxPower = _HwApOpticalDdmRxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 10),
    _HwApOpticalDdmRxPower_Type()
)
hwApOpticalDdmRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalDdmRxPower.setStatus("current")
_HwApOpticalDdmTemperature_Type = Integer32
_HwApOpticalDdmTemperature_Object = MibTableColumn
hwApOpticalDdmTemperature = _HwApOpticalDdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 11),
    _HwApOpticalDdmTemperature_Type()
)
hwApOpticalDdmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalDdmTemperature.setStatus("current")
_HwApOpticalVdndorOui_Type = Integer32
_HwApOpticalVdndorOui_Object = MibTableColumn
hwApOpticalVdndorOui = _HwApOpticalVdndorOui_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 12),
    _HwApOpticalVdndorOui_Type()
)
hwApOpticalVdndorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalVdndorOui.setStatus("current")
_HwApOpticalVendorName_Type = OctetString
_HwApOpticalVendorName_Object = MibTableColumn
hwApOpticalVendorName = _HwApOpticalVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 13),
    _HwApOpticalVendorName_Type()
)
hwApOpticalVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalVendorName.setStatus("current")
_HwApOpticalVendorPn_Type = OctetString
_HwApOpticalVendorPn_Object = MibTableColumn
hwApOpticalVendorPn = _HwApOpticalVendorPn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 14),
    _HwApOpticalVendorPn_Type()
)
hwApOpticalVendorPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalVendorPn.setStatus("current")
_HwApOpticalVendorRev_Type = OctetString
_HwApOpticalVendorRev_Object = MibTableColumn
hwApOpticalVendorRev = _HwApOpticalVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 15),
    _HwApOpticalVendorRev_Type()
)
hwApOpticalVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalVendorRev.setStatus("current")
_HwApOpticalVendorSn_Type = OctetString
_HwApOpticalVendorSn_Object = MibTableColumn
hwApOpticalVendorSn = _HwApOpticalVendorSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 18, 1, 16),
    _HwApOpticalVendorSn_Type()
)
hwApOpticalVendorSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApOpticalVendorSn.setStatus("current")
_HwMacApOpticalInfoTable_Object = MibTable
hwMacApOpticalInfoTable = _HwMacApOpticalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19)
)
if mibBuilder.loadTexts:
    hwMacApOpticalInfoTable.setStatus("current")
_HwMacApOpticalInfoEntry_Object = MibTableRow
hwMacApOpticalInfoEntry = _HwMacApOpticalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1)
)
hwMacApOpticalInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
)
if mibBuilder.loadTexts:
    hwMacApOpticalInfoEntry.setStatus("current")
_HwMacApOpticalNominalBitRate_Type = Integer32
_HwMacApOpticalNominalBitRate_Object = MibTableColumn
hwMacApOpticalNominalBitRate = _HwMacApOpticalNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 1),
    _HwMacApOpticalNominalBitRate_Type()
)
hwMacApOpticalNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalNominalBitRate.setStatus("current")
_HwMacApOpticalLinkLen9X125km_Type = Integer32
_HwMacApOpticalLinkLen9X125km_Object = MibTableColumn
hwMacApOpticalLinkLen9X125km = _HwMacApOpticalLinkLen9X125km_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 2),
    _HwMacApOpticalLinkLen9X125km_Type()
)
hwMacApOpticalLinkLen9X125km.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalLinkLen9X125km.setStatus("current")
_HwMacApOpticalLinkLen50X125X100m_Type = Integer32
_HwMacApOpticalLinkLen50X125X100m_Object = MibTableColumn
hwMacApOpticalLinkLen50X125X100m = _HwMacApOpticalLinkLen50X125X100m_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 3),
    _HwMacApOpticalLinkLen50X125X100m_Type()
)
hwMacApOpticalLinkLen50X125X100m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalLinkLen50X125X100m.setStatus("current")
_HwMacApOpticalLinkLen62p5X125X10m_Type = Integer32
_HwMacApOpticalLinkLen62p5X125X10m_Object = MibTableColumn
hwMacApOpticalLinkLen62p5X125X10m = _HwMacApOpticalLinkLen62p5X125X10m_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 4),
    _HwMacApOpticalLinkLen62p5X125X10m_Type()
)
hwMacApOpticalLinkLen62p5X125X10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalLinkLen62p5X125X10m.setStatus("current")
_HwMacApOpticalLinkLenCopper_Type = Integer32
_HwMacApOpticalLinkLenCopper_Object = MibTableColumn
hwMacApOpticalLinkLenCopper = _HwMacApOpticalLinkLenCopper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 5),
    _HwMacApOpticalLinkLenCopper_Type()
)
hwMacApOpticalLinkLenCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalLinkLenCopper.setStatus("current")
_HwMacApOpticalSfpConnector_Type = OctetString
_HwMacApOpticalSfpConnector_Object = MibTableColumn
hwMacApOpticalSfpConnector = _HwMacApOpticalSfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 6),
    _HwMacApOpticalSfpConnector_Type()
)
hwMacApOpticalSfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalSfpConnector.setStatus("current")
_HwMacApOpticalDdmVoltage_Type = Integer32
_HwMacApOpticalDdmVoltage_Object = MibTableColumn
hwMacApOpticalDdmVoltage = _HwMacApOpticalDdmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 7),
    _HwMacApOpticalDdmVoltage_Type()
)
hwMacApOpticalDdmVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalDdmVoltage.setStatus("current")
_HwMacApOpticalDdmTxBiasCurrent_Type = Integer32
_HwMacApOpticalDdmTxBiasCurrent_Object = MibTableColumn
hwMacApOpticalDdmTxBiasCurrent = _HwMacApOpticalDdmTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 8),
    _HwMacApOpticalDdmTxBiasCurrent_Type()
)
hwMacApOpticalDdmTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalDdmTxBiasCurrent.setStatus("current")
_HwMacApOpticalDdmTxPower_Type = Integer32
_HwMacApOpticalDdmTxPower_Object = MibTableColumn
hwMacApOpticalDdmTxPower = _HwMacApOpticalDdmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 9),
    _HwMacApOpticalDdmTxPower_Type()
)
hwMacApOpticalDdmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalDdmTxPower.setStatus("current")
_HwMacApOpticalDdmRxPower_Type = Integer32
_HwMacApOpticalDdmRxPower_Object = MibTableColumn
hwMacApOpticalDdmRxPower = _HwMacApOpticalDdmRxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 10),
    _HwMacApOpticalDdmRxPower_Type()
)
hwMacApOpticalDdmRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalDdmRxPower.setStatus("current")
_HwMacApOpticalDdmTemperature_Type = Integer32
_HwMacApOpticalDdmTemperature_Object = MibTableColumn
hwMacApOpticalDdmTemperature = _HwMacApOpticalDdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 11),
    _HwMacApOpticalDdmTemperature_Type()
)
hwMacApOpticalDdmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalDdmTemperature.setStatus("current")
_HwMacApOpticalVdndorOui_Type = Integer32
_HwMacApOpticalVdndorOui_Object = MibTableColumn
hwMacApOpticalVdndorOui = _HwMacApOpticalVdndorOui_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 12),
    _HwMacApOpticalVdndorOui_Type()
)
hwMacApOpticalVdndorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalVdndorOui.setStatus("current")
_HwMacApOpticalVendorName_Type = OctetString
_HwMacApOpticalVendorName_Object = MibTableColumn
hwMacApOpticalVendorName = _HwMacApOpticalVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 13),
    _HwMacApOpticalVendorName_Type()
)
hwMacApOpticalVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalVendorName.setStatus("current")
_HwMacApOpticalVendorPn_Type = OctetString
_HwMacApOpticalVendorPn_Object = MibTableColumn
hwMacApOpticalVendorPn = _HwMacApOpticalVendorPn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 14),
    _HwMacApOpticalVendorPn_Type()
)
hwMacApOpticalVendorPn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalVendorPn.setStatus("current")
_HwMacApOpticalVendorRev_Type = OctetString
_HwMacApOpticalVendorRev_Object = MibTableColumn
hwMacApOpticalVendorRev = _HwMacApOpticalVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 15),
    _HwMacApOpticalVendorRev_Type()
)
hwMacApOpticalVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalVendorRev.setStatus("current")
_HwMacApOpticalVendorSn_Type = OctetString
_HwMacApOpticalVendorSn_Object = MibTableColumn
hwMacApOpticalVendorSn = _HwMacApOpticalVendorSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 19, 1, 16),
    _HwMacApOpticalVendorSn_Type()
)
hwMacApOpticalVendorSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOpticalVendorSn.setStatus("current")
_HwApSysnameTable_Object = MibTable
hwApSysnameTable = _HwApSysnameTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 20)
)
if mibBuilder.loadTexts:
    hwApSysnameTable.setStatus("current")
_HwApSysnameEntry_Object = MibTableRow
hwApSysnameEntry = _HwApSysnameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 20, 1)
)
hwApSysnameEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
)
if mibBuilder.loadTexts:
    hwApSysnameEntry.setStatus("current")
_HwApSysnameApId_Type = Integer32
_HwApSysnameApId_Object = MibTableColumn
hwApSysnameApId = _HwApSysnameApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 20, 1, 1),
    _HwApSysnameApId_Type()
)
hwApSysnameApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSysnameApId.setStatus("current")
_HwApSysnameApMac_Type = MacAddress
_HwApSysnameApMac_Object = MibTableColumn
hwApSysnameApMac = _HwApSysnameApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 20, 1, 2),
    _HwApSysnameApMac_Type()
)
hwApSysnameApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApSysnameApMac.setStatus("current")
_HwApPhysicalAttrTable_Object = MibTable
hwApPhysicalAttrTable = _HwApPhysicalAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 21)
)
if mibBuilder.loadTexts:
    hwApPhysicalAttrTable.setStatus("current")
_HwApPhysicalAttrEntry_Object = MibTableRow
hwApPhysicalAttrEntry = _HwApPhysicalAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 21, 1)
)
hwApPhysicalAttrEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
)
if mibBuilder.loadTexts:
    hwApPhysicalAttrEntry.setStatus("current")


class _HwApElectronicLabel_Type(OctetString):
    """Custom type hwApElectronicLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1025),
    )


_HwApElectronicLabel_Type.__name__ = "OctetString"
_HwApElectronicLabel_Object = MibTableColumn
hwApElectronicLabel = _HwApElectronicLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 21, 1, 1),
    _HwApElectronicLabel_Type()
)
hwApElectronicLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApElectronicLabel.setStatus("current")
_HwMacApPhysicalAttrTable_Object = MibTable
hwMacApPhysicalAttrTable = _HwMacApPhysicalAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 22)
)
if mibBuilder.loadTexts:
    hwMacApPhysicalAttrTable.setStatus("current")
_HwMacApPhysicalAttrEntry_Object = MibTableRow
hwMacApPhysicalAttrEntry = _HwMacApPhysicalAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 22, 1)
)
hwMacApPhysicalAttrEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
)
if mibBuilder.loadTexts:
    hwMacApPhysicalAttrEntry.setStatus("current")


class _HwMacApElectronicLabel_Type(OctetString):
    """Custom type hwMacApElectronicLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1025),
    )


_HwMacApElectronicLabel_Type.__name__ = "OctetString"
_HwMacApElectronicLabel_Object = MibTableColumn
hwMacApElectronicLabel = _HwMacApElectronicLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 22, 1, 1),
    _HwMacApElectronicLabel_Type()
)
hwMacApElectronicLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApElectronicLabel.setStatus("current")
_HwApLineportStatTable_Object = MibTable
hwApLineportStatTable = _HwApLineportStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23)
)
if mibBuilder.loadTexts:
    hwApLineportStatTable.setStatus("current")
_HwApLineportStatEntry_Object = MibTableRow
hwApLineportStatEntry = _HwApLineportStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1)
)
hwApLineportStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortIndex"),
)
if mibBuilder.loadTexts:
    hwApLineportStatEntry.setStatus("current")
_HwApLinePortStatClear_Type = Integer32
_HwApLinePortStatClear_Object = MibTableColumn
hwApLinePortStatClear = _HwApLinePortStatClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 1),
    _HwApLinePortStatClear_Type()
)
hwApLinePortStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLinePortStatClear.setStatus("current")
_HwApLinePortUpDwnTimes_Type = Unsigned32
_HwApLinePortUpDwnTimes_Object = MibTableColumn
hwApLinePortUpDwnTimes = _HwApLinePortUpDwnTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 2),
    _HwApLinePortUpDwnTimes_Type()
)
hwApLinePortUpDwnTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortUpDwnTimes.setStatus("current")
_HwApLinePortInPkts_Type = Counter64
_HwApLinePortInPkts_Object = MibTableColumn
hwApLinePortInPkts = _HwApLinePortInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 3),
    _HwApLinePortInPkts_Type()
)
hwApLinePortInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortInPkts.setStatus("current")
_HwApLinePortInUnicastPkts_Type = Counter64
_HwApLinePortInUnicastPkts_Object = MibTableColumn
hwApLinePortInUnicastPkts = _HwApLinePortInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 4),
    _HwApLinePortInUnicastPkts_Type()
)
hwApLinePortInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortInUnicastPkts.setStatus("current")
_HwApLinePortInNonUnicastPkts_Type = Counter64
_HwApLinePortInNonUnicastPkts_Object = MibTableColumn
hwApLinePortInNonUnicastPkts = _HwApLinePortInNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 5),
    _HwApLinePortInNonUnicastPkts_Type()
)
hwApLinePortInNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortInNonUnicastPkts.setStatus("current")
_HwApLinePortInBytes_Type = Counter64
_HwApLinePortInBytes_Object = MibTableColumn
hwApLinePortInBytes = _HwApLinePortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 6),
    _HwApLinePortInBytes_Type()
)
hwApLinePortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortInBytes.setStatus("current")
_HwApLinePortInErrorPkts_Type = Counter64
_HwApLinePortInErrorPkts_Object = MibTableColumn
hwApLinePortInErrorPkts = _HwApLinePortInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 7),
    _HwApLinePortInErrorPkts_Type()
)
hwApLinePortInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortInErrorPkts.setStatus("current")
_HwApLinePortInDiscardPkts_Type = Counter64
_HwApLinePortInDiscardPkts_Object = MibTableColumn
hwApLinePortInDiscardPkts = _HwApLinePortInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 8),
    _HwApLinePortInDiscardPkts_Type()
)
hwApLinePortInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortInDiscardPkts.setStatus("current")
_HwApLinePortOutPkts_Type = Counter64
_HwApLinePortOutPkts_Object = MibTableColumn
hwApLinePortOutPkts = _HwApLinePortOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 9),
    _HwApLinePortOutPkts_Type()
)
hwApLinePortOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortOutPkts.setStatus("current")
_HwApLinePortOutUnicastPkts_Type = Counter64
_HwApLinePortOutUnicastPkts_Object = MibTableColumn
hwApLinePortOutUnicastPkts = _HwApLinePortOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 10),
    _HwApLinePortOutUnicastPkts_Type()
)
hwApLinePortOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortOutUnicastPkts.setStatus("current")
_HwApLinePortOutNonUnicastPkts_Type = Counter64
_HwApLinePortOutNonUnicastPkts_Object = MibTableColumn
hwApLinePortOutNonUnicastPkts = _HwApLinePortOutNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 11),
    _HwApLinePortOutNonUnicastPkts_Type()
)
hwApLinePortOutNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortOutNonUnicastPkts.setStatus("current")
_HwApLinePortOutBytes_Type = Counter64
_HwApLinePortOutBytes_Object = MibTableColumn
hwApLinePortOutBytes = _HwApLinePortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 12),
    _HwApLinePortOutBytes_Type()
)
hwApLinePortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortOutBytes.setStatus("current")
_HwApLinePortOutErrorsPkts_Type = Counter64
_HwApLinePortOutErrorsPkts_Object = MibTableColumn
hwApLinePortOutErrorsPkts = _HwApLinePortOutErrorsPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 13),
    _HwApLinePortOutErrorsPkts_Type()
)
hwApLinePortOutErrorsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortOutErrorsPkts.setStatus("current")
_HwApLinePortOutDiscardPkts_Type = Counter64
_HwApLinePortOutDiscardPkts_Object = MibTableColumn
hwApLinePortOutDiscardPkts = _HwApLinePortOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 23, 1, 14),
    _HwApLinePortOutDiscardPkts_Type()
)
hwApLinePortOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLinePortOutDiscardPkts.setStatus("current")
_HwMacApLineportStatTable_Object = MibTable
hwMacApLineportStatTable = _HwMacApLineportStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24)
)
if mibBuilder.loadTexts:
    hwMacApLineportStatTable.setStatus("current")
_HwMacApLineportStatEntry_Object = MibTableRow
hwMacApLineportStatEntry = _HwMacApLineportStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1)
)
hwMacApLineportStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortIndex"),
)
if mibBuilder.loadTexts:
    hwMacApLineportStatEntry.setStatus("current")
_HwMacApLinePortStatClear_Type = Integer32
_HwMacApLinePortStatClear_Object = MibTableColumn
hwMacApLinePortStatClear = _HwMacApLinePortStatClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 1),
    _HwMacApLinePortStatClear_Type()
)
hwMacApLinePortStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLinePortStatClear.setStatus("current")
_HwMacApLinePortUpDwnTimes_Type = Unsigned32
_HwMacApLinePortUpDwnTimes_Object = MibTableColumn
hwMacApLinePortUpDwnTimes = _HwMacApLinePortUpDwnTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 2),
    _HwMacApLinePortUpDwnTimes_Type()
)
hwMacApLinePortUpDwnTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortUpDwnTimes.setStatus("current")
_HwMacApLinePortInPkts_Type = Counter64
_HwMacApLinePortInPkts_Object = MibTableColumn
hwMacApLinePortInPkts = _HwMacApLinePortInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 3),
    _HwMacApLinePortInPkts_Type()
)
hwMacApLinePortInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortInPkts.setStatus("current")
_HwMacApLinePortInUnicastPkts_Type = Counter64
_HwMacApLinePortInUnicastPkts_Object = MibTableColumn
hwMacApLinePortInUnicastPkts = _HwMacApLinePortInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 4),
    _HwMacApLinePortInUnicastPkts_Type()
)
hwMacApLinePortInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortInUnicastPkts.setStatus("current")
_HwMacApLinePortInNonUnicastPkts_Type = Counter64
_HwMacApLinePortInNonUnicastPkts_Object = MibTableColumn
hwMacApLinePortInNonUnicastPkts = _HwMacApLinePortInNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 5),
    _HwMacApLinePortInNonUnicastPkts_Type()
)
hwMacApLinePortInNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortInNonUnicastPkts.setStatus("current")
_HwMacApLinePortInBytes_Type = Counter64
_HwMacApLinePortInBytes_Object = MibTableColumn
hwMacApLinePortInBytes = _HwMacApLinePortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 6),
    _HwMacApLinePortInBytes_Type()
)
hwMacApLinePortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortInBytes.setStatus("current")
_HwMacApLinePortInErrorPkts_Type = Counter64
_HwMacApLinePortInErrorPkts_Object = MibTableColumn
hwMacApLinePortInErrorPkts = _HwMacApLinePortInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 7),
    _HwMacApLinePortInErrorPkts_Type()
)
hwMacApLinePortInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortInErrorPkts.setStatus("current")
_HwMacApLinePortInDiscardPkts_Type = Counter64
_HwMacApLinePortInDiscardPkts_Object = MibTableColumn
hwMacApLinePortInDiscardPkts = _HwMacApLinePortInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 8),
    _HwMacApLinePortInDiscardPkts_Type()
)
hwMacApLinePortInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortInDiscardPkts.setStatus("current")
_HwMacApLinePortOutPkts_Type = Counter64
_HwMacApLinePortOutPkts_Object = MibTableColumn
hwMacApLinePortOutPkts = _HwMacApLinePortOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 9),
    _HwMacApLinePortOutPkts_Type()
)
hwMacApLinePortOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortOutPkts.setStatus("current")
_HwMacApLinePortOutUnicastPkts_Type = Counter64
_HwMacApLinePortOutUnicastPkts_Object = MibTableColumn
hwMacApLinePortOutUnicastPkts = _HwMacApLinePortOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 10),
    _HwMacApLinePortOutUnicastPkts_Type()
)
hwMacApLinePortOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortOutUnicastPkts.setStatus("current")
_HwMacApLinePortOutNonUnicastPkts_Type = Counter64
_HwMacApLinePortOutNonUnicastPkts_Object = MibTableColumn
hwMacApLinePortOutNonUnicastPkts = _HwMacApLinePortOutNonUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 11),
    _HwMacApLinePortOutNonUnicastPkts_Type()
)
hwMacApLinePortOutNonUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortOutNonUnicastPkts.setStatus("current")
_HwMacApLinePortOutBytes_Type = Counter64
_HwMacApLinePortOutBytes_Object = MibTableColumn
hwMacApLinePortOutBytes = _HwMacApLinePortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 12),
    _HwMacApLinePortOutBytes_Type()
)
hwMacApLinePortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortOutBytes.setStatus("current")
_HwMacApLinePortOutErrorsPkts_Type = Counter64
_HwMacApLinePortOutErrorsPkts_Object = MibTableColumn
hwMacApLinePortOutErrorsPkts = _HwMacApLinePortOutErrorsPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 13),
    _HwMacApLinePortOutErrorsPkts_Type()
)
hwMacApLinePortOutErrorsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortOutErrorsPkts.setStatus("current")
_HwMacApLinePortOutDiscardPkts_Type = Counter64
_HwMacApLinePortOutDiscardPkts_Object = MibTableColumn
hwMacApLinePortOutDiscardPkts = _HwMacApLinePortOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 24, 1, 14),
    _HwMacApLinePortOutDiscardPkts_Type()
)
hwMacApLinePortOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLinePortOutDiscardPkts.setStatus("current")
_HwApLineatePortLldpCfgTable_Object = MibTable
hwApLineatePortLldpCfgTable = _HwApLineatePortLldpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25)
)
if mibBuilder.loadTexts:
    hwApLineatePortLldpCfgTable.setStatus("current")
_HwApLineatePortLldpCfgEntry_Object = MibTableRow
hwApLineatePortLldpCfgEntry = _HwApLineatePortLldpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1)
)
hwApLineatePortLldpCfgEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortLldpIndex"),
)
if mibBuilder.loadTexts:
    hwApLineatePortLldpCfgEntry.setStatus("current")
_HwApLineatePortLldpIndex_Type = Integer32
_HwApLineatePortLldpIndex_Object = MibTableColumn
hwApLineatePortLldpIndex = _HwApLineatePortLldpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 1),
    _HwApLineatePortLldpIndex_Type()
)
hwApLineatePortLldpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLineatePortLldpIndex.setStatus("current")


class _HwApLineatePortLldpEnable_Type(Integer32):
    """Custom type hwApLineatePortLldpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwApLineatePortLldpEnable_Type.__name__ = "Integer32"
_HwApLineatePortLldpEnable_Object = MibTableColumn
hwApLineatePortLldpEnable = _HwApLineatePortLldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 2),
    _HwApLineatePortLldpEnable_Type()
)
hwApLineatePortLldpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpEnable.setStatus("current")


class _HwApLineatePortLldpManageAddr_Type(Integer32):
    """Custom type hwApLineatePortLldpManageAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwApLineatePortLldpManageAddr_Type.__name__ = "Integer32"
_HwApLineatePortLldpManageAddr_Object = MibTableColumn
hwApLineatePortLldpManageAddr = _HwApLineatePortLldpManageAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 3),
    _HwApLineatePortLldpManageAddr_Type()
)
hwApLineatePortLldpManageAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpManageAddr.setStatus("current")


class _HwApLineatePortLldpPortDes_Type(Integer32):
    """Custom type hwApLineatePortLldpPortDes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwApLineatePortLldpPortDes_Type.__name__ = "Integer32"
_HwApLineatePortLldpPortDes_Object = MibTableColumn
hwApLineatePortLldpPortDes = _HwApLineatePortLldpPortDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 4),
    _HwApLineatePortLldpPortDes_Type()
)
hwApLineatePortLldpPortDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpPortDes.setStatus("current")


class _HwApLineatePortLldpSysCab_Type(Integer32):
    """Custom type hwApLineatePortLldpSysCab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwApLineatePortLldpSysCab_Type.__name__ = "Integer32"
_HwApLineatePortLldpSysCab_Object = MibTableColumn
hwApLineatePortLldpSysCab = _HwApLineatePortLldpSysCab_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 5),
    _HwApLineatePortLldpSysCab_Type()
)
hwApLineatePortLldpSysCab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpSysCab.setStatus("current")


class _HwApLineatePortLldpSysDes_Type(Integer32):
    """Custom type hwApLineatePortLldpSysDes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwApLineatePortLldpSysDes_Type.__name__ = "Integer32"
_HwApLineatePortLldpSysDes_Object = MibTableColumn
hwApLineatePortLldpSysDes = _HwApLineatePortLldpSysDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 6),
    _HwApLineatePortLldpSysDes_Type()
)
hwApLineatePortLldpSysDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpSysDes.setStatus("current")


class _HwApLineatePortLldpSysName_Type(Integer32):
    """Custom type hwApLineatePortLldpSysName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwApLineatePortLldpSysName_Type.__name__ = "Integer32"
_HwApLineatePortLldpSysName_Object = MibTableColumn
hwApLineatePortLldpSysName = _HwApLineatePortLldpSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 7),
    _HwApLineatePortLldpSysName_Type()
)
hwApLineatePortLldpSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpSysName.setStatus("current")
_HwApLineatePortLldpDelay_Type = Integer32
_HwApLineatePortLldpDelay_Object = MibTableColumn
hwApLineatePortLldpDelay = _HwApLineatePortLldpDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 8),
    _HwApLineatePortLldpDelay_Type()
)
hwApLineatePortLldpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpDelay.setStatus("current")
_HwApLineatePortLldpHoldMultiplier_Type = Integer32
_HwApLineatePortLldpHoldMultiplier_Object = MibTableColumn
hwApLineatePortLldpHoldMultiplier = _HwApLineatePortLldpHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 9),
    _HwApLineatePortLldpHoldMultiplier_Type()
)
hwApLineatePortLldpHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpHoldMultiplier.setStatus("current")
_HwApLineatePortLldpInterval_Type = Integer32
_HwApLineatePortLldpInterval_Object = MibTableColumn
hwApLineatePortLldpInterval = _HwApLineatePortLldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 10),
    _HwApLineatePortLldpInterval_Type()
)
hwApLineatePortLldpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpInterval.setStatus("current")
_HwApLineatePortLldpRestartDelay_Type = Integer32
_HwApLineatePortLldpRestartDelay_Object = MibTableColumn
hwApLineatePortLldpRestartDelay = _HwApLineatePortLldpRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 11),
    _HwApLineatePortLldpRestartDelay_Type()
)
hwApLineatePortLldpRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRestartDelay.setStatus("current")


class _HwApLineatePortLldpAdminStatus_Type(Integer32):
    """Custom type hwApLineatePortLldpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwApLineatePortLldpAdminStatus_Type.__name__ = "Integer32"
_HwApLineatePortLldpAdminStatus_Object = MibTableColumn
hwApLineatePortLldpAdminStatus = _HwApLineatePortLldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 12),
    _HwApLineatePortLldpAdminStatus_Type()
)
hwApLineatePortLldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpAdminStatus.setStatus("current")
_HwApLineatePortLldpReportInterval_Type = Unsigned32
_HwApLineatePortLldpReportInterval_Object = MibTableColumn
hwApLineatePortLldpReportInterval = _HwApLineatePortLldpReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 25, 1, 13),
    _HwApLineatePortLldpReportInterval_Type()
)
hwApLineatePortLldpReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApLineatePortLldpReportInterval.setStatus("current")
_HwMacApLineatePortLldpCfgTable_Object = MibTable
hwMacApLineatePortLldpCfgTable = _HwMacApLineatePortLldpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26)
)
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpCfgTable.setStatus("current")
_HwMacApLineatePortLldpCfgEntry_Object = MibTableRow
hwMacApLineatePortLldpCfgEntry = _HwMacApLineatePortLldpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1)
)
hwMacApLineatePortLldpCfgEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortLldpIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
)
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpCfgEntry.setStatus("current")
_HwMacApLineatePortLldpIndex_Type = Integer32
_HwMacApLineatePortLldpIndex_Object = MibTableColumn
hwMacApLineatePortLldpIndex = _HwMacApLineatePortLldpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 1),
    _HwMacApLineatePortLldpIndex_Type()
)
hwMacApLineatePortLldpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpIndex.setStatus("current")


class _HwMacApLineatePortLldpEnable_Type(Integer32):
    """Custom type hwMacApLineatePortLldpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacApLineatePortLldpEnable_Type.__name__ = "Integer32"
_HwMacApLineatePortLldpEnable_Object = MibTableColumn
hwMacApLineatePortLldpEnable = _HwMacApLineatePortLldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 2),
    _HwMacApLineatePortLldpEnable_Type()
)
hwMacApLineatePortLldpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpEnable.setStatus("current")


class _HwMacApLineatePortLldpManageAddr_Type(Integer32):
    """Custom type hwMacApLineatePortLldpManageAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacApLineatePortLldpManageAddr_Type.__name__ = "Integer32"
_HwMacApLineatePortLldpManageAddr_Object = MibTableColumn
hwMacApLineatePortLldpManageAddr = _HwMacApLineatePortLldpManageAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 3),
    _HwMacApLineatePortLldpManageAddr_Type()
)
hwMacApLineatePortLldpManageAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpManageAddr.setStatus("current")


class _HwMacApLineatePortLldpPortDes_Type(Integer32):
    """Custom type hwMacApLineatePortLldpPortDes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacApLineatePortLldpPortDes_Type.__name__ = "Integer32"
_HwMacApLineatePortLldpPortDes_Object = MibTableColumn
hwMacApLineatePortLldpPortDes = _HwMacApLineatePortLldpPortDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 4),
    _HwMacApLineatePortLldpPortDes_Type()
)
hwMacApLineatePortLldpPortDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpPortDes.setStatus("current")


class _HwMacApLineatePortLldpSysCab_Type(Integer32):
    """Custom type hwMacApLineatePortLldpSysCab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacApLineatePortLldpSysCab_Type.__name__ = "Integer32"
_HwMacApLineatePortLldpSysCab_Object = MibTableColumn
hwMacApLineatePortLldpSysCab = _HwMacApLineatePortLldpSysCab_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 5),
    _HwMacApLineatePortLldpSysCab_Type()
)
hwMacApLineatePortLldpSysCab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpSysCab.setStatus("current")


class _HwMacApLineatePortLldpSysDes_Type(Integer32):
    """Custom type hwMacApLineatePortLldpSysDes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacApLineatePortLldpSysDes_Type.__name__ = "Integer32"
_HwMacApLineatePortLldpSysDes_Object = MibTableColumn
hwMacApLineatePortLldpSysDes = _HwMacApLineatePortLldpSysDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 6),
    _HwMacApLineatePortLldpSysDes_Type()
)
hwMacApLineatePortLldpSysDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpSysDes.setStatus("current")


class _HwMacApLineatePortLldpSysName_Type(Integer32):
    """Custom type hwMacApLineatePortLldpSysName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMacApLineatePortLldpSysName_Type.__name__ = "Integer32"
_HwMacApLineatePortLldpSysName_Object = MibTableColumn
hwMacApLineatePortLldpSysName = _HwMacApLineatePortLldpSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 7),
    _HwMacApLineatePortLldpSysName_Type()
)
hwMacApLineatePortLldpSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpSysName.setStatus("current")
_HwMacApLineatePortLldpDelay_Type = Integer32
_HwMacApLineatePortLldpDelay_Object = MibTableColumn
hwMacApLineatePortLldpDelay = _HwMacApLineatePortLldpDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 8),
    _HwMacApLineatePortLldpDelay_Type()
)
hwMacApLineatePortLldpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpDelay.setStatus("current")
_HwMacApLineatePortLldpHoldMultiplier_Type = Integer32
_HwMacApLineatePortLldpHoldMultiplier_Object = MibTableColumn
hwMacApLineatePortLldpHoldMultiplier = _HwMacApLineatePortLldpHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 9),
    _HwMacApLineatePortLldpHoldMultiplier_Type()
)
hwMacApLineatePortLldpHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpHoldMultiplier.setStatus("current")
_HwMacApLineatePortLldpInterval_Type = Integer32
_HwMacApLineatePortLldpInterval_Object = MibTableColumn
hwMacApLineatePortLldpInterval = _HwMacApLineatePortLldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 10),
    _HwMacApLineatePortLldpInterval_Type()
)
hwMacApLineatePortLldpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpInterval.setStatus("current")
_HwMacApLineatePortLldpRestartDelay_Type = Integer32
_HwMacApLineatePortLldpRestartDelay_Object = MibTableColumn
hwMacApLineatePortLldpRestartDelay = _HwMacApLineatePortLldpRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 11),
    _HwMacApLineatePortLldpRestartDelay_Type()
)
hwMacApLineatePortLldpRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRestartDelay.setStatus("current")


class _HwMacApLineatePortLldpAdminStatus_Type(Integer32):
    """Custom type hwMacApLineatePortLldpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwMacApLineatePortLldpAdminStatus_Type.__name__ = "Integer32"
_HwMacApLineatePortLldpAdminStatus_Object = MibTableColumn
hwMacApLineatePortLldpAdminStatus = _HwMacApLineatePortLldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 12),
    _HwMacApLineatePortLldpAdminStatus_Type()
)
hwMacApLineatePortLldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpAdminStatus.setStatus("current")
_HwMacApLineatePortLldpReportInterval_Type = Integer32
_HwMacApLineatePortLldpReportInterval_Object = MibTableColumn
hwMacApLineatePortLldpReportInterval = _HwMacApLineatePortLldpReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 26, 1, 13),
    _HwMacApLineatePortLldpReportInterval_Type()
)
hwMacApLineatePortLldpReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpReportInterval.setStatus("current")
_HwApLineatePortLldpTable_Object = MibTable
hwApLineatePortLldpTable = _HwApLineatePortLldpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27)
)
if mibBuilder.loadTexts:
    hwApLineatePortLldpTable.setStatus("current")
_HwApLineatePortLldpEntry_Object = MibTableRow
hwApLineatePortLldpEntry = _HwApLineatePortLldpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1)
)
hwApLineatePortLldpEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortLldpRemIndex"),
)
if mibBuilder.loadTexts:
    hwApLineatePortLldpEntry.setStatus("current")
_HwApLineatePortLldpRemLocalPortNum_Type = Integer32
_HwApLineatePortLldpRemLocalPortNum_Object = MibTableColumn
hwApLineatePortLldpRemLocalPortNum = _HwApLineatePortLldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 1),
    _HwApLineatePortLldpRemLocalPortNum_Type()
)
hwApLineatePortLldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemLocalPortNum.setStatus("current")
_HwApLineatePortLldpRemIndex_Type = Integer32
_HwApLineatePortLldpRemIndex_Object = MibTableColumn
hwApLineatePortLldpRemIndex = _HwApLineatePortLldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 2),
    _HwApLineatePortLldpRemIndex_Type()
)
hwApLineatePortLldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemIndex.setStatus("current")
_HwApLineatePortLldpRemChassisIdSubtype_Type = Integer32
_HwApLineatePortLldpRemChassisIdSubtype_Object = MibTableColumn
hwApLineatePortLldpRemChassisIdSubtype = _HwApLineatePortLldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 3),
    _HwApLineatePortLldpRemChassisIdSubtype_Type()
)
hwApLineatePortLldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemChassisIdSubtype.setStatus("current")


class _HwApLineatePortLldpRemChassisId_Type(OctetString):
    """Custom type hwApLineatePortLldpRemChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLineatePortLldpRemChassisId_Type.__name__ = "OctetString"
_HwApLineatePortLldpRemChassisId_Object = MibTableColumn
hwApLineatePortLldpRemChassisId = _HwApLineatePortLldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 4),
    _HwApLineatePortLldpRemChassisId_Type()
)
hwApLineatePortLldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemChassisId.setStatus("current")
_HwApLineatePortLldpRemPortIdSubtype_Type = Integer32
_HwApLineatePortLldpRemPortIdSubtype_Object = MibTableColumn
hwApLineatePortLldpRemPortIdSubtype = _HwApLineatePortLldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 5),
    _HwApLineatePortLldpRemPortIdSubtype_Type()
)
hwApLineatePortLldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemPortIdSubtype.setStatus("current")


class _HwApLineatePortLldpRemPortId_Type(OctetString):
    """Custom type hwApLineatePortLldpRemPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLineatePortLldpRemPortId_Type.__name__ = "OctetString"
_HwApLineatePortLldpRemPortId_Object = MibTableColumn
hwApLineatePortLldpRemPortId = _HwApLineatePortLldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 6),
    _HwApLineatePortLldpRemPortId_Type()
)
hwApLineatePortLldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemPortId.setStatus("current")


class _HwApLineatePortLldpRemPortDesc_Type(OctetString):
    """Custom type hwApLineatePortLldpRemPortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLineatePortLldpRemPortDesc_Type.__name__ = "OctetString"
_HwApLineatePortLldpRemPortDesc_Object = MibTableColumn
hwApLineatePortLldpRemPortDesc = _HwApLineatePortLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 7),
    _HwApLineatePortLldpRemPortDesc_Type()
)
hwApLineatePortLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemPortDesc.setStatus("current")


class _HwApLineatePortLldpRemSysName_Type(OctetString):
    """Custom type hwApLineatePortLldpRemSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLineatePortLldpRemSysName_Type.__name__ = "OctetString"
_HwApLineatePortLldpRemSysName_Object = MibTableColumn
hwApLineatePortLldpRemSysName = _HwApLineatePortLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 8),
    _HwApLineatePortLldpRemSysName_Type()
)
hwApLineatePortLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemSysName.setStatus("current")


class _HwApLineatePortLldpRemSysDesc_Type(OctetString):
    """Custom type hwApLineatePortLldpRemSysDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwApLineatePortLldpRemSysDesc_Type.__name__ = "OctetString"
_HwApLineatePortLldpRemSysDesc_Object = MibTableColumn
hwApLineatePortLldpRemSysDesc = _HwApLineatePortLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 9),
    _HwApLineatePortLldpRemSysDesc_Type()
)
hwApLineatePortLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemSysDesc.setStatus("current")
_HwApLineatePortLldpRemSysCapSupported_Type = Integer32
_HwApLineatePortLldpRemSysCapSupported_Object = MibTableColumn
hwApLineatePortLldpRemSysCapSupported = _HwApLineatePortLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 10),
    _HwApLineatePortLldpRemSysCapSupported_Type()
)
hwApLineatePortLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemSysCapSupported.setStatus("current")
_HwApLineatePortLldpRemSysCapEnabled_Type = Integer32
_HwApLineatePortLldpRemSysCapEnabled_Object = MibTableColumn
hwApLineatePortLldpRemSysCapEnabled = _HwApLineatePortLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 27, 1, 11),
    _HwApLineatePortLldpRemSysCapEnabled_Type()
)
hwApLineatePortLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemSysCapEnabled.setStatus("current")
_HwMacApLineatePortLldpTable_Object = MibTable
hwMacApLineatePortLldpTable = _HwMacApLineatePortLldpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28)
)
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpTable.setStatus("current")
_HwMacApLineatePortLldpEntry_Object = MibTableRow
hwMacApLineatePortLldpEntry = _HwMacApLineatePortLldpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1)
)
hwMacApLineatePortLldpEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortLldpRemIndex"),
)
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpEntry.setStatus("current")
_HwMacApLineatePortLldpRemLocalPortNum_Type = Integer32
_HwMacApLineatePortLldpRemLocalPortNum_Object = MibTableColumn
hwMacApLineatePortLldpRemLocalPortNum = _HwMacApLineatePortLldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 1),
    _HwMacApLineatePortLldpRemLocalPortNum_Type()
)
hwMacApLineatePortLldpRemLocalPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemLocalPortNum.setStatus("current")
_HwMacApLineatePortLldpRemIndex_Type = Integer32
_HwMacApLineatePortLldpRemIndex_Object = MibTableColumn
hwMacApLineatePortLldpRemIndex = _HwMacApLineatePortLldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 2),
    _HwMacApLineatePortLldpRemIndex_Type()
)
hwMacApLineatePortLldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemIndex.setStatus("current")
_HwMacApLineatePortLldpRemChassisIdSubtype_Type = Integer32
_HwMacApLineatePortLldpRemChassisIdSubtype_Object = MibTableColumn
hwMacApLineatePortLldpRemChassisIdSubtype = _HwMacApLineatePortLldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 3),
    _HwMacApLineatePortLldpRemChassisIdSubtype_Type()
)
hwMacApLineatePortLldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemChassisIdSubtype.setStatus("current")


class _HwMacApLineatePortLldpRemChassisId_Type(OctetString):
    """Custom type hwMacApLineatePortLldpRemChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLineatePortLldpRemChassisId_Type.__name__ = "OctetString"
_HwMacApLineatePortLldpRemChassisId_Object = MibTableColumn
hwMacApLineatePortLldpRemChassisId = _HwMacApLineatePortLldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 4),
    _HwMacApLineatePortLldpRemChassisId_Type()
)
hwMacApLineatePortLldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemChassisId.setStatus("current")
_HwMacApLineatePortLldpRemPortIdSubtype_Type = Integer32
_HwMacApLineatePortLldpRemPortIdSubtype_Object = MibTableColumn
hwMacApLineatePortLldpRemPortIdSubtype = _HwMacApLineatePortLldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 5),
    _HwMacApLineatePortLldpRemPortIdSubtype_Type()
)
hwMacApLineatePortLldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemPortIdSubtype.setStatus("current")


class _HwMacApLineatePortLldpRemPortId_Type(OctetString):
    """Custom type hwMacApLineatePortLldpRemPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLineatePortLldpRemPortId_Type.__name__ = "OctetString"
_HwMacApLineatePortLldpRemPortId_Object = MibTableColumn
hwMacApLineatePortLldpRemPortId = _HwMacApLineatePortLldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 6),
    _HwMacApLineatePortLldpRemPortId_Type()
)
hwMacApLineatePortLldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemPortId.setStatus("current")


class _HwMacApLineatePortLldpRemPortDesc_Type(OctetString):
    """Custom type hwMacApLineatePortLldpRemPortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLineatePortLldpRemPortDesc_Type.__name__ = "OctetString"
_HwMacApLineatePortLldpRemPortDesc_Object = MibTableColumn
hwMacApLineatePortLldpRemPortDesc = _HwMacApLineatePortLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 7),
    _HwMacApLineatePortLldpRemPortDesc_Type()
)
hwMacApLineatePortLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemPortDesc.setStatus("current")


class _HwMacApLineatePortLldpRemSysName_Type(OctetString):
    """Custom type hwMacApLineatePortLldpRemSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLineatePortLldpRemSysName_Type.__name__ = "OctetString"
_HwMacApLineatePortLldpRemSysName_Object = MibTableColumn
hwMacApLineatePortLldpRemSysName = _HwMacApLineatePortLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 8),
    _HwMacApLineatePortLldpRemSysName_Type()
)
hwMacApLineatePortLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemSysName.setStatus("current")


class _HwMacApLineatePortLldpRemSysDesc_Type(OctetString):
    """Custom type hwMacApLineatePortLldpRemSysDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMacApLineatePortLldpRemSysDesc_Type.__name__ = "OctetString"
_HwMacApLineatePortLldpRemSysDesc_Object = MibTableColumn
hwMacApLineatePortLldpRemSysDesc = _HwMacApLineatePortLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 9),
    _HwMacApLineatePortLldpRemSysDesc_Type()
)
hwMacApLineatePortLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemSysDesc.setStatus("current")
_HwMacApLineatePortLldpRemSysCapSupported_Type = Integer32
_HwMacApLineatePortLldpRemSysCapSupported_Object = MibTableColumn
hwMacApLineatePortLldpRemSysCapSupported = _HwMacApLineatePortLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 10),
    _HwMacApLineatePortLldpRemSysCapSupported_Type()
)
hwMacApLineatePortLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemSysCapSupported.setStatus("current")
_HwMacApLineatePortLldpRemSysCapEnabled_Type = Integer32
_HwMacApLineatePortLldpRemSysCapEnabled_Object = MibTableColumn
hwMacApLineatePortLldpRemSysCapEnabled = _HwMacApLineatePortLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 28, 1, 11),
    _HwMacApLineatePortLldpRemSysCapEnabled_Type()
)
hwMacApLineatePortLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemSysCapEnabled.setStatus("current")
_HwApLineatePortLldpRemManAddrTable_Object = MibTable
hwApLineatePortLldpRemManAddrTable = _HwApLineatePortLldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 29)
)
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemManAddrTable.setStatus("current")
_HwApLineatePortLldpRemManAddrEntry_Object = MibTableRow
hwApLineatePortLldpRemManAddrEntry = _HwApLineatePortLldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 29, 1)
)
hwApLineatePortLldpRemManAddrEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortLldpRemIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortLldpRemManAddrSubtype"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemManAddrEntry.setStatus("current")
_HwApLineatePortLldpRemManAddrSubtype_Type = Integer32
_HwApLineatePortLldpRemManAddrSubtype_Object = MibTableColumn
hwApLineatePortLldpRemManAddrSubtype = _HwApLineatePortLldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 29, 1, 1),
    _HwApLineatePortLldpRemManAddrSubtype_Type()
)
hwApLineatePortLldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemManAddrSubtype.setStatus("current")


class _HwApLineatePortLldpRemManAddr_Type(OctetString):
    """Custom type hwApLineatePortLldpRemManAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwApLineatePortLldpRemManAddr_Type.__name__ = "OctetString"
_HwApLineatePortLldpRemManAddr_Object = MibTableColumn
hwApLineatePortLldpRemManAddr = _HwApLineatePortLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 29, 1, 2),
    _HwApLineatePortLldpRemManAddr_Type()
)
hwApLineatePortLldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemManAddr.setStatus("current")
_HwApLineatePortLldpRemManAddrIfSubtype_Type = Integer32
_HwApLineatePortLldpRemManAddrIfSubtype_Object = MibTableColumn
hwApLineatePortLldpRemManAddrIfSubtype = _HwApLineatePortLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 29, 1, 3),
    _HwApLineatePortLldpRemManAddrIfSubtype_Type()
)
hwApLineatePortLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemManAddrIfSubtype.setStatus("current")
_HwApLineatePortLldpRemManAddrIfId_Type = Integer32
_HwApLineatePortLldpRemManAddrIfId_Object = MibTableColumn
hwApLineatePortLldpRemManAddrIfId = _HwApLineatePortLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 29, 1, 4),
    _HwApLineatePortLldpRemManAddrIfId_Type()
)
hwApLineatePortLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemManAddrIfId.setStatus("current")


class _HwApLineatePortLldpRemManAddrOID_Type(OctetString):
    """Custom type hwApLineatePortLldpRemManAddrOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwApLineatePortLldpRemManAddrOID_Type.__name__ = "OctetString"
_HwApLineatePortLldpRemManAddrOID_Object = MibTableColumn
hwApLineatePortLldpRemManAddrOID = _HwApLineatePortLldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 29, 1, 5),
    _HwApLineatePortLldpRemManAddrOID_Type()
)
hwApLineatePortLldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApLineatePortLldpRemManAddrOID.setStatus("current")
_HwMacApLineatePortLldpRemManAddrTable_Object = MibTable
hwMacApLineatePortLldpRemManAddrTable = _HwMacApLineatePortLldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 30)
)
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemManAddrTable.setStatus("current")
_HwMacApLineatePortLldpRemManAddrEntry_Object = MibTableRow
hwMacApLineatePortLldpRemManAddrEntry = _HwMacApLineatePortLldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 30, 1)
)
hwMacApLineatePortLldpRemManAddrEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApMac"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortLldpRemLocalPortNum"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortLldpRemIndex"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMACApLineatePortLldpRemManAddrSubtype"),
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMACApLineatePortLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    hwMacApLineatePortLldpRemManAddrEntry.setStatus("current")
_HwMACApLineatePortLldpRemManAddrSubtype_Type = Integer32
_HwMACApLineatePortLldpRemManAddrSubtype_Object = MibTableColumn
hwMACApLineatePortLldpRemManAddrSubtype = _HwMACApLineatePortLldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 30, 1, 1),
    _HwMACApLineatePortLldpRemManAddrSubtype_Type()
)
hwMACApLineatePortLldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMACApLineatePortLldpRemManAddrSubtype.setStatus("current")


class _HwMACApLineatePortLldpRemManAddr_Type(OctetString):
    """Custom type hwMACApLineatePortLldpRemManAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwMACApLineatePortLldpRemManAddr_Type.__name__ = "OctetString"
_HwMACApLineatePortLldpRemManAddr_Object = MibTableColumn
hwMACApLineatePortLldpRemManAddr = _HwMACApLineatePortLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 30, 1, 2),
    _HwMACApLineatePortLldpRemManAddr_Type()
)
hwMACApLineatePortLldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMACApLineatePortLldpRemManAddr.setStatus("current")
_HwMACApLineatePortLldpRemManAddrIfSubtype_Type = Integer32
_HwMACApLineatePortLldpRemManAddrIfSubtype_Object = MibTableColumn
hwMACApLineatePortLldpRemManAddrIfSubtype = _HwMACApLineatePortLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 30, 1, 3),
    _HwMACApLineatePortLldpRemManAddrIfSubtype_Type()
)
hwMACApLineatePortLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLineatePortLldpRemManAddrIfSubtype.setStatus("current")
_HwMACApLineatePortLldpRemManAddrIfId_Type = Integer32
_HwMACApLineatePortLldpRemManAddrIfId_Object = MibTableColumn
hwMACApLineatePortLldpRemManAddrIfId = _HwMACApLineatePortLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 30, 1, 4),
    _HwMACApLineatePortLldpRemManAddrIfId_Type()
)
hwMACApLineatePortLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLineatePortLldpRemManAddrIfId.setStatus("current")


class _HwMACApLineatePortLldpRemManAddrOID_Type(OctetString):
    """Custom type hwMACApLineatePortLldpRemManAddrOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwMACApLineatePortLldpRemManAddrOID_Type.__name__ = "OctetString"
_HwMACApLineatePortLldpRemManAddrOID_Object = MibTableColumn
hwMACApLineatePortLldpRemManAddrOID = _HwMACApLineatePortLldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 30, 1, 5),
    _HwMACApLineatePortLldpRemManAddrOID_Type()
)
hwMACApLineatePortLldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACApLineatePortLldpRemManAddrOID.setStatus("current")
_HwApOnlineFailTable_Object = MibTable
hwApOnlineFailTable = _HwApOnlineFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 31)
)
if mibBuilder.loadTexts:
    hwApOnlineFailTable.setStatus("current")
_HwApOnlineFailEntry_Object = MibTableRow
hwApOnlineFailEntry = _HwApOnlineFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 31, 1)
)
hwApOnlineFailEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApOnlineFailMac"),
)
if mibBuilder.loadTexts:
    hwApOnlineFailEntry.setStatus("current")
_HwApOnlineFailMac_Type = MacAddress
_HwApOnlineFailMac_Object = MibTableColumn
hwApOnlineFailMac = _HwApOnlineFailMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 31, 1, 1),
    _HwApOnlineFailMac_Type()
)
hwApOnlineFailMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApOnlineFailMac.setStatus("current")
_HwMacApOnlineFailTime_Type = OctetString
_HwMacApOnlineFailTime_Object = MibTableColumn
hwMacApOnlineFailTime = _HwMacApOnlineFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 31, 1, 2),
    _HwMacApOnlineFailTime_Type()
)
hwMacApOnlineFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOnlineFailTime.setStatus("current")


class _HwMacApOnlineFailReason_Type(OctetString):
    """Custom type hwMacApOnlineFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwMacApOnlineFailReason_Type.__name__ = "OctetString"
_HwMacApOnlineFailReason_Object = MibTableColumn
hwMacApOnlineFailReason = _HwMacApOnlineFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 31, 1, 3),
    _HwMacApOnlineFailReason_Type()
)
hwMacApOnlineFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOnlineFailReason.setStatus("current")
_HwMacApOnlineFailRowStatus_Type = RowStatus
_HwMacApOnlineFailRowStatus_Object = MibTableColumn
hwMacApOnlineFailRowStatus = _HwMacApOnlineFailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 31, 1, 4),
    _HwMacApOnlineFailRowStatus_Type()
)
hwMacApOnlineFailRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApOnlineFailRowStatus.setStatus("current")
_HwApOfflineTable_Object = MibTable
hwApOfflineTable = _HwApOfflineTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 32)
)
if mibBuilder.loadTexts:
    hwApOfflineTable.setStatus("current")
_HwApOfflineEntry_Object = MibTableRow
hwApOfflineEntry = _HwApOfflineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 32, 1)
)
hwApOfflineEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwApOfflineMac"),
)
if mibBuilder.loadTexts:
    hwApOfflineEntry.setStatus("current")
_HwApOfflineMac_Type = MacAddress
_HwApOfflineMac_Object = MibTableColumn
hwApOfflineMac = _HwApOfflineMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 32, 1, 1),
    _HwApOfflineMac_Type()
)
hwApOfflineMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApOfflineMac.setStatus("current")
_HwMacApOfflineTime_Type = OctetString
_HwMacApOfflineTime_Object = MibTableColumn
hwMacApOfflineTime = _HwMacApOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 32, 1, 2),
    _HwMacApOfflineTime_Type()
)
hwMacApOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOfflineTime.setStatus("current")


class _HwMacApOfflineReason_Type(OctetString):
    """Custom type hwMacApOfflineReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwMacApOfflineReason_Type.__name__ = "OctetString"
_HwMacApOfflineReason_Object = MibTableColumn
hwMacApOfflineReason = _HwMacApOfflineReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 32, 1, 3),
    _HwMacApOfflineReason_Type()
)
hwMacApOfflineReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApOfflineReason.setStatus("current")
_HwMacApOfflineRowStatus_Type = RowStatus
_HwMacApOfflineRowStatus_Object = MibTableColumn
hwMacApOfflineRowStatus = _HwMacApOfflineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 6, 32, 1, 4),
    _HwMacApOfflineRowStatus_Type()
)
hwMacApOfflineRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApOfflineRowStatus.setStatus("current")
_HwAcObjects_ObjectIdentity = ObjectIdentity
hwAcObjects = _HwAcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7)
)
_HwAcTable_Object = MibTable
hwAcTable = _HwAcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1)
)
if mibBuilder.loadTexts:
    hwAcTable.setStatus("current")
_HwAcEntry_Object = MibTableRow
hwAcEntry = _HwAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1, 1)
)
hwAcEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMemAcIndex"),
)
if mibBuilder.loadTexts:
    hwAcEntry.setStatus("current")
_HwMemAcIndex_Type = Integer32
_HwMemAcIndex_Object = MibTableColumn
hwMemAcIndex = _HwMemAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1, 1, 1),
    _HwMemAcIndex_Type()
)
hwMemAcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMemAcIndex.setStatus("current")


class _HwAcIpVersion_Type(Integer32):
    """Custom type hwAcIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_HwAcIpVersion_Type.__name__ = "Integer32"
_HwAcIpVersion_Object = MibTableColumn
hwAcIpVersion = _HwAcIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1, 1, 2),
    _HwAcIpVersion_Type()
)
hwAcIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAcIpVersion.setStatus("current")
_HwAcIPv4Address_Type = IpAddress
_HwAcIPv4Address_Object = MibTableColumn
hwAcIPv4Address = _HwAcIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1, 1, 3),
    _HwAcIPv4Address_Type()
)
hwAcIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAcIPv4Address.setStatus("current")
_HwAcIPv6Address_Type = OctetString
_HwAcIPv6Address_Object = MibTableColumn
hwAcIPv6Address = _HwAcIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1, 1, 4),
    _HwAcIPv6Address_Type()
)
hwAcIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAcIPv6Address.setStatus("current")


class _HwAcState_Type(Integer32):
    """Custom type hwAcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1))
    )


_HwAcState_Type.__name__ = "Integer32"
_HwAcState_Object = MibTableColumn
hwAcState = _HwAcState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1, 1, 5),
    _HwAcState_Type()
)
hwAcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcState.setStatus("current")
_HwAcRowStatus_Type = RowStatus
_HwAcRowStatus_Object = MibTableColumn
hwAcRowStatus = _HwAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 1, 1, 6),
    _HwAcRowStatus_Type()
)
hwAcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAcRowStatus.setStatus("current")
_HwMobilityGroupTable_Object = MibTable
hwMobilityGroupTable = _HwMobilityGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 2)
)
if mibBuilder.loadTexts:
    hwMobilityGroupTable.setStatus("current")
_HwMobilityGroupEntry_Object = MibTableRow
hwMobilityGroupEntry = _HwMobilityGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 2, 1)
)
hwMobilityGroupEntry.setIndexNames(
    (0, "HUAWEI-WLAN-DEVICE-MIB", "hwMobilityGroupName"),
)
if mibBuilder.loadTexts:
    hwMobilityGroupEntry.setStatus("current")
_HwMobilityGroupName_Type = OctetString
_HwMobilityGroupName_Object = MibTableColumn
hwMobilityGroupName = _HwMobilityGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 2, 1, 1),
    _HwMobilityGroupName_Type()
)
hwMobilityGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMobilityGroupName.setStatus("current")
_HwMobilityGroupMemberList_Type = OctetString
_HwMobilityGroupMemberList_Object = MibTableColumn
hwMobilityGroupMemberList = _HwMobilityGroupMemberList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 2, 1, 2),
    _HwMobilityGroupMemberList_Type()
)
hwMobilityGroupMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMobilityGroupMemberList.setStatus("current")
_HwMobilityGroupStatus_Type = RowStatus
_HwMobilityGroupStatus_Object = MibTableColumn
hwMobilityGroupStatus = _HwMobilityGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 2, 1, 3),
    _HwMobilityGroupStatus_Type()
)
hwMobilityGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMobilityGroupStatus.setStatus("current")


class _HwMobilityGroupMemberOpcode_Type(Integer32):
    """Custom type hwMobilityGroupMemberOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2))
    )


_HwMobilityGroupMemberOpcode_Type.__name__ = "Integer32"
_HwMobilityGroupMemberOpcode_Object = MibTableColumn
hwMobilityGroupMemberOpcode = _HwMobilityGroupMemberOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 2, 1, 4),
    _HwMobilityGroupMemberOpcode_Type()
)
hwMobilityGroupMemberOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMobilityGroupMemberOpcode.setStatus("current")


class _HwMobilityGroupMemberIndex_Type(Integer32):
    """Custom type hwMobilityGroupMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwMobilityGroupMemberIndex_Type.__name__ = "Integer32"
_HwMobilityGroupMemberIndex_Object = MibTableColumn
hwMobilityGroupMemberIndex = _HwMobilityGroupMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 7, 2, 1, 5),
    _HwMobilityGroupMemberIndex_Type()
)
hwMobilityGroupMemberIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMobilityGroupMemberIndex.setStatus("current")
_HwWlanDeviceObjects_ObjectIdentity = ObjectIdentity
hwWlanDeviceObjects = _HwWlanDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 8)
)
_HwWlanDeviceConformance_ObjectIdentity = ObjectIdentity
hwWlanDeviceConformance = _HwWlanDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9)
)
_HwWlanDeviceCompliances_ObjectIdentity = ObjectIdentity
hwWlanDeviceCompliances = _HwWlanDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 1)
)
_HwWlanDeviceObjectGroups_ObjectIdentity = ObjectIdentity
hwWlanDeviceObjectGroups = _HwWlanDeviceObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2)
)

# Managed Objects groups

hwWlanDeviceNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 2)
)
hwWlanDeviceNotifyObjectsGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApActualType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuOccupancyRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemoryOccupancyRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPermitStaNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwStaAuthFailCause"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAcSystemSwitchType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRadioNotifyPara"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPower"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperature"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCfgCountryCode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackSrcMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackDstMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackSrcIP"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpCfgRateThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpActualRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyRadioId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyOrRestoreTemperature"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootNotifyName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultTimes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwSignalStrengthThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwStaBroadcastFlux"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwBroadcastWarnThresholdDown"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwBroadcastWarnThresholdUp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwBroadcastRestrainThresholdDown"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwBroadcastRestrainThresholdUp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBroadcastFlux"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcErrActual"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyWlanId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLicenseInfo"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcPortType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcPortID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackDropNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIfIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultInfo"))
)
if mibBuilder.loadTexts:
    hwWlanDeviceNotifyObjectsGroup.setStatus("current")

hwApTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 3)
)
hwApTypeGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeLineatePortNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeRadioNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeMaxStaNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeMaxSsidNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeAntennaGain"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeReset"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeLineatePortType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeRadioType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwRadioMaxSpatialStreamsNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwRadioMaxAntennasNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwRadioMaxVAPNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeRadioAntennaGain"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLocalAssocResSwitch"))
)
if mibBuilder.loadTexts:
    hwApTypeGroup.setStatus("current")

hwApProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 4)
)
hwApProfileGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApEthPortMtu"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApDosDefend"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApWorkMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogBackupServerIp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogBackupMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSampleTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApStatisticsInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEapStartMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEapStartUnicastMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEapStartTransform"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEapResponseMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEapResponseUnicastMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEapResponseTransform"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOfflineManagement"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAlarmRestrictionMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAlarmRestrictionPeriod"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAp4WayHandshakeRoamPolicy"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogRecordLevel"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogBackupPeriodTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogRecordFtpMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogServerUsername"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogServerUserPassword"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLogServerIp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileTelnetSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSshSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileDhcpTrustPort"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileConsoleSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileMaxUserNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileNdTrustPort"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLedSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileDefault"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileBatchStart"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileBatchNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileBatchReturnNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProfileBatchNameList"))
)
if mibBuilder.loadTexts:
    hwApProfileGroup.setStatus("current")

hwApAuthListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 5)
)
hwApAuthListGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApMacWhitelistRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSnWhitelistRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAuthMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMacWhitelistBatchQueryStartNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMacWhitelistBatchQueryNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMacWhitelistBatchQueryList"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMacWhitelistBatchQueryReturnNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSnWhitelistBatchQueryStartNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSnWhitelistBatchQueryNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSnWhitelistBatchQueryList"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSnWhitelistBatchQueryReturnNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMacBlacklistRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSnBlacklistRowStatus"))
)
if mibBuilder.loadTexts:
    hwApAuthListGroup.setStatus("current")

hwApRegionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 6)
)
hwApRegionGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionDeployMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionApNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionApIndexMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionForwardMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionCountryCode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionDefault"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionAllExistRegionIndexMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionBatchStart"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionBatchNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionBatchReturnNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionBatchNameList"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionBatchDeployMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSrcRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApDestRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionScanChannel2G"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionScanChannel5G"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionCalibrateChannel2G"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionCalibrateChannel5G"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRegionCalibrate5gBandWidth"))
)
if mibBuilder.loadTexts:
    hwApRegionGroup.setStatus("current")

hwApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 7)
)
hwApGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedProfileName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRunState"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSoftwareVersion"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApHardwareVersion"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpufrequency"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemoryType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApDomain"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIpAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIpNetMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApGatewayIp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemorySize"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFlashSize"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRunTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpEthPortSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpEthPortSpeedMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpEthPortDuplex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpEthPortDuplexMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAdminOper"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRowstatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPerformanceStatCycle"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApDNS"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRunningMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApForwardMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAntennaMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNEnumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOnlineTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysSoftwareDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysHardtwareDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysManufacture"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysSoftwareName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysSoftwareVendor"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApManagementVlanID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsername"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPassword"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAcIP1"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAcIP2"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAcIP3"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAcIP4"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIpMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpManageAddr"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpPortDes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpSysCab"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpSysDes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpDelay"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpHoldMultiplier"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRestartDelay"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpAdminStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpReportInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBomCode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProtectAcPriority"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProtectAcIP"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalHighRxPowerThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalLowRxPowerThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalHighTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalLowTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApKeepService"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPriorityAccessMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineateportMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineateportVlanTagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineateportVlanUntagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineateportPvidVlan"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineateportUserIsolate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineateportStpEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApHighTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLowTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApReset"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApStaticIpAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApStaticNetMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApStaticGatewayIp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackFloodInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackFloodTimes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApDynamicBlacklistEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApDynamicBlacklistAgingInt"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackPskInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackPskTimes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAccessBalanceGap"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIpv6Address"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIpv6NetMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApGatewayIpv6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIpv6DNS"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApProtectAcIPv6Addr"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortCfgMtu"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortMacAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAccessBalanceSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNatIpAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackFloodQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackPskQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackWeakivQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAttackSpoofQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootCountTotal"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootCountPowerOff"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootCountRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortState"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortDuplex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortNegotiation"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortUserIsolate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortStpEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortVlanTagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortVlanUntagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortPvidVlan"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortCRCErrorHighThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortCRCErrorLowThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortCRCErrorSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNumInbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNumOutbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNameInbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNameOutbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclSwitchInbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclSwitchOutbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNumInboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNumOutboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNameInboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclNameOutboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclSwitchInboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineatePortAclSwitchOutboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortIsAddInTrunk"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMultiLineatePortAddedOrExitTrunkID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAllExistApIndexMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwUnAuthorizedApRecordNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwUnAuthorizedApRecordAdmin"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBatchIndexStart"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBatchIndexNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBatchIndexReturnNumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBatchState"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBatchNameList"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingCount"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingPacketSize"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingWaitTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingTimeOut"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultSuccessCount"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultFailureCount"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultAverageResponseTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultMinimumResponseTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultMaximumResponseTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultFlag"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemoryUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFlashFreeSize"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTemperature"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOnlineUserNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpPortSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpPortRecvFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpPortRecvRightFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpPortRecvErrorFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpPortSendFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpPortRecvBytes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUpPortSendBytes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPUpPortPER"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPWirelessUpPortTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPUpPortTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAirportSendDropFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportRecvDropFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAirportUpTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAirportDwTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportDwTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportUpTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAirportRecvDropPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAirportRecvErrorPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportRecvUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportRecvNonUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportSendUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportSendNonUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAvgRCPUUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAvgRMemoryUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwEthportSendDropFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwEthportSendErrorFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwEthportUpDwnTimes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAirportRecvUnicastFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportRecvUnknownFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportUpRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApEthportDownRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUnauthorizedApType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUnauthorizedApMacAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUnauthorizedApSn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUnauthorizedApIpAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUnauthorizedApRecordTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApStaAveSignalStrength"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUsedProfileName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUsedRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApRunState"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSoftwareVersion"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApHardwareVersion"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApCpuType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApCpufrequency"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMemoryType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApDomain"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApIpAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApIpNetMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApGatewayIp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMemorySize"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApFlashSize"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApRunTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpEthPortSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpEthPortSpeedMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpEthPortDuplex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpEthPortDuplexMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAdminOper"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApRowstatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApPerformanceStatCycle"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApDNS"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApRunningMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApForwardMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAntennaMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApCpuThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMemThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApNEnumber"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOnlineTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSysSoftwareDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSysHardtwareDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSysManufacture"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSysSoftwareName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApSysSoftwareVendor"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApManagementVlanID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUsername"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApPassword"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAcIP1"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAcIP2"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAcIP3"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAcIP4"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApIpMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpManageAddr"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpPortDes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpSysCab"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpSysDes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpDelay"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpHoldMultiplier"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRestartDelay"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpAdminStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpReportInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApBomCode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApProtectAcPriority"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApProtectAcIP"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalHighRxPowerThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalLowRxPowerThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalHighTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalLowTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApKeepService"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApPriorityAccessMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineateportMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineateportVlanTagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineateportVlanUntagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineateportPvidVlan"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineateportUserIsolate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineateportStpEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApHighTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLowTemperatureThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApReset"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApStaticIpAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApStaticNetMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApStaticGatewayIp"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAttackFloodInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAttackFloodTimes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApDynamicBlacklistEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApDynamicBlacklistAgingInt"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAttackPskInterval"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAttackPskTimes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAccessBalanceGap"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApIpv6Address"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApIpv6NetMask"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApGatewayIpv6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApIpv6DNS"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApProtectAcIPv6Addr"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApLineatePortCfgMtu"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApLineatePortMacAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAccessBalanceSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApNatIpAddress"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAttackFloodQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAttackPskQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAttackWeakivQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApAttackSpoofQuietTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApBootCountTotal"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApBootCountPowerOff"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApBootCountRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortState"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortDuplex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortNegotiation"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortMode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortUserIsolate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortStpEnable"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortVlanTagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortVlanUntagged"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortPvidVlan"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortCRCErrorHighThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortCRCErrorLowThreshold"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortCRCErrorSwitch"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNumInbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNumOutbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNameInbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNameOutbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclSwitchInbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclSwitchOutbound"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNumInboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNumOutboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNameInboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclNameOutboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclSwitchInboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineatePortAclSwitchOutboundIPV6"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortIsAddInTrunk"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMultiLineatePortAddedOrExitTrunkID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApMemoryUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApCpuUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApFlashFreeSize"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApTemperature"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOnlineUserNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpPortSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpPortRecvFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpPortRecvRightFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpPortRecvErrorFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpPortSendFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpPortRecvBytes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApUpPortSendBytes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacAPUpPortPER"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacAPWirelessUpPortTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacAPUpPortTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAirportSendDropFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportRecvDropFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAirportUpTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAirportDwTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportDwTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportUpTraffic"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAirportRecvDropPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAirportRecvErrorPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportRecvUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportRecvNonUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportSendUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportSendNonUnicastPacket"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAvgRCPUUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAvgRMemoryUseRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacEthportSendDropFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacEthportSendErrorFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacEthportUpDwnTimes"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApAirportRecvUnicastFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApEthportRecvUnknownFrames"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacEthportUpRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacEthportDownRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineportDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineportType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineportMtu"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineportSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineportMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineportAdminStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLineportNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportMtu"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportSpeed"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportAdminStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLineportNum"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemChassisIdSubtype"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemChassisId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemPortIdSubtype"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemPortId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemPortDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemSysDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemSysCapSupported"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemSysCapEnabled"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemChassisIdSubtype"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemChassisId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemPortIdSubtype"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemPortId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemPortDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemSysDesc"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemSysCapSupported"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApLldpRemSysCapEnabled"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemManAddrIfSubtype"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemManAddrIfId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLldpRemManAddrOID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApLldpRemManAddrIfSubtype"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApLldpRemManAddrIfId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMACApLldpRemManAddrOID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalNominalBitRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalLinkLen9X125km"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalLinkLen50X125X100m"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalLinkLen62p5X125X10m"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalLinkLenCopper"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalSfpConnector"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalDdmVoltage"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalDdmTxBiasCurrent"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalDdmTxPower"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalDdmRxPower"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalDdmTemperature"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalVdndorOui"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalVendorName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalVendorPn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalVendorRev"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalVendorSn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalNominalBitRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalLinkLen9X125km"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalLinkLen50X125X100m"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalLinkLen62p5X125X10m"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalLinkLenCopper"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalSfpConnector"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalDdmVoltage"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalDdmTxBiasCurrent"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalDdmTxPower"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalDdmRxPower"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalDdmTemperature"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalVdndorOui"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalVendorName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalVendorPn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalVendorRev"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApOpticalVendorSn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysnameApId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysnameApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApElectronicLabel"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMacApElectronicLabel"))
)
if mibBuilder.loadTexts:
    hwApGroup.setStatus("current")

hwAcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 8)
)
hwAcGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwAcIpVersion"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAcIPv4Address"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAcIPv6Address"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAcState"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAcRowStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMobilityGroupMemberList"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMobilityGroupStatus"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMobilityGroupMemberOpcode"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwMobilityGroupMemberIndex"))
)
if mibBuilder.loadTexts:
    hwAcGroup.setStatus("current")


# Notification objects

hwApFaultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 1)
)
hwApFaultNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultTimes"))
)
if mibBuilder.loadTexts:
    hwApFaultNotify.setStatus(
        "current"
    )

hwApNormalNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 2)
)
hwApNormalNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApNormalNotify.setStatus(
        "current"
    )

hwApTypeNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 3)
)
hwApTypeNotMatchNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApActualType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApTypeNotMatchNotify.setStatus(
        "current"
    )

hwApPingResultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 4)
)
hwApPingResultNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultSuccessCount"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultFailureCount"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultAverageResponseTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultMinimumResponseTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultMaximumResponseTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApPingResultNotify.setStatus(
        "current"
    )

hwApColdstartNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 5)
)
hwApColdstartNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedRegionIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApColdstartNotify.setStatus(
        "current"
    )

hwApConfigCommitNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 8)
)
hwApConfigCommitNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApConfigCommitNotify.setStatus(
        "current"
    )

hwApAddOffLineNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 9)
)
hwApAddOffLineNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSn"))
)
if mibBuilder.loadTexts:
    hwApAddOffLineNotify.setStatus(
        "current"
    )

hwApConfirmNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 10)
)
hwApConfirmNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSn"))
)
if mibBuilder.loadTexts:
    hwApConfirmNotify.setStatus(
        "current"
    )

hwUnAuthorizedApRecordExistNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 11)
)
hwUnAuthorizedApRecordExistNotify.setObjects(
    ("HUAWEI-WLAN-DEVICE-MIB", "hwUnAuthorizedApRecordNumber")
)
if mibBuilder.loadTexts:
    hwUnAuthorizedApRecordExistNotify.setStatus(
        "current"
    )

hwUnAuthorizedApRecordClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hwUnAuthorizedApRecordClearNotify.setStatus(
        "current"
    )

hwApCpuOverloadNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 13)
)
hwApCpuOverloadNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuOccupancyRate"))
)
if mibBuilder.loadTexts:
    hwApCpuOverloadNotify.setStatus(
        "current"
    )

hwApCpuOverloadRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 14)
)
hwApCpuOverloadRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuOccupancyRate"))
)
if mibBuilder.loadTexts:
    hwApCpuOverloadRestoreNotify.setStatus(
        "current"
    )

hwApMemoryOverloadNOtify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 15)
)
hwApMemoryOverloadNOtify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemoryOccupancyRate"))
)
if mibBuilder.loadTexts:
    hwApMemoryOverloadNOtify.setStatus(
        "current"
    )

hwApMemoryOverloadRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 16)
)
hwApMemoryOverloadRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemoryOccupancyRate"))
)
if mibBuilder.loadTexts:
    hwApMemoryOverloadRestoreNotify.setStatus(
        "current"
    )

hwAPStaFullNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 17)
)
hwAPStaFullNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwStaAuthFailCause"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPermitStaNum"))
)
if mibBuilder.loadTexts:
    hwAPStaFullNotify.setStatus(
        "current"
    )

hwAPStaFullRecoverNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 18)
)
hwAPStaFullRecoverNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwStaAuthFailCause"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPermitStaNum"))
)
if mibBuilder.loadTexts:
    hwAPStaFullRecoverNotify.setStatus(
        "current"
    )

hwAcDevicesSwitchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 19)
)
hwAcDevicesSwitchNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSn"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAcSystemSwitchType"))
)
if mibBuilder.loadTexts:
    hwAcDevicesSwitchNotify.setStatus(
        "current"
    )

hwApTimeSynFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 20)
)
hwApTimeSynFailNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApTimeSynFailNotify.setStatus(
        "current"
    )

hwDyingGaspTrapNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 21)
)
hwDyingGaspTrapNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwDyingGaspTrapNotify.setStatus(
        "current"
    )

hwApFaultNotifyFat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 22)
)
hwApFaultNotifyFat.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"))
)
if mibBuilder.loadTexts:
    hwApFaultNotifyFat.setStatus(
        "current"
    )

hwApNormalNotifyFat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 23)
)
hwApNormalNotifyFat.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApUsedType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"))
)
if mibBuilder.loadTexts:
    hwApNormalNotifyFat.setStatus(
        "current"
    )

hwApTemperatureTooLowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 24)
)
hwApTemperatureTooLowNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyOrRestoreTemperature"))
)
if mibBuilder.loadTexts:
    hwApTemperatureTooLowNotify.setStatus(
        "current"
    )

hwApTemperatureTooLowRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 25)
)
hwApTemperatureTooLowRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyOrRestoreTemperature"))
)
if mibBuilder.loadTexts:
    hwApTemperatureTooLowRestoreNotify.setStatus(
        "current"
    )

hwApTemperatureTooHighNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 26)
)
hwApTemperatureTooHighNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyOrRestoreTemperature"))
)
if mibBuilder.loadTexts:
    hwApTemperatureTooHighNotify.setStatus(
        "current"
    )

hwApTemperatureTooHighRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 27)
)
hwApTemperatureTooHighRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyOrRestoreTemperature"))
)
if mibBuilder.loadTexts:
    hwApTemperatureTooHighRestoreNotify.setStatus(
        "current"
    )

hwRadioDownNotifyFat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 29)
)
hwRadioDownNotifyFat.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRadioNotifyPara"))
)
if mibBuilder.loadTexts:
    hwRadioDownNotifyFat.setStatus(
        "current"
    )

hwRadioDownRecovNotifyFat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 30)
)
hwRadioDownRecovNotifyFat.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApRadioNotifyPara"))
)
if mibBuilder.loadTexts:
    hwRadioDownRecovNotifyFat.setStatus(
        "current"
    )

hwApOpticalRxPowerTooHighNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 31)
)
hwApOpticalRxPowerTooHighNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPower"))
)
if mibBuilder.loadTexts:
    hwApOpticalRxPowerTooHighNotify.setStatus(
        "current"
    )

hwApOpticalRxPowerTooHighRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 32)
)
hwApOpticalRxPowerTooHighRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPower"))
)
if mibBuilder.loadTexts:
    hwApOpticalRxPowerTooHighRestoreNotify.setStatus(
        "current"
    )

hwApOpticalRxPowerTooLowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 33)
)
hwApOpticalRxPowerTooLowNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPower"))
)
if mibBuilder.loadTexts:
    hwApOpticalRxPowerTooLowNotify.setStatus(
        "current"
    )

hwApOpticalRxPowerTooLowRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 34)
)
hwApOpticalRxPowerTooLowRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPower"))
)
if mibBuilder.loadTexts:
    hwApOpticalRxPowerTooLowRestoreNotify.setStatus(
        "current"
    )

hwApOpticalTemperatureTooHighNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 35)
)
hwApOpticalTemperatureTooHighNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperature"))
)
if mibBuilder.loadTexts:
    hwApOpticalTemperatureTooHighNotify.setStatus(
        "current"
    )

hwApOpticalTemperatureTooHighRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 36)
)
hwApOpticalTemperatureTooHighRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperature"))
)
if mibBuilder.loadTexts:
    hwApOpticalTemperatureTooHighRestoreNotify.setStatus(
        "current"
    )

hwApOpticalTemperatureTooLowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 37)
)
hwApOpticalTemperatureTooLowNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperature"))
)
if mibBuilder.loadTexts:
    hwApOpticalTemperatureTooLowNotify.setStatus(
        "current"
    )

hwApOpticalTemperatureTooLowRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 38)
)
hwApOpticalTemperatureTooLowRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperature"))
)
if mibBuilder.loadTexts:
    hwApOpticalTemperatureTooLowRestoreNotify.setStatus(
        "current"
    )

hwApNotSupportCountryCodeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 39)
)
hwApNotSupportCountryCodeNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCfgCountryCode"))
)
if mibBuilder.loadTexts:
    hwApNotSupportCountryCodeNotify.setStatus(
        "current"
    )

hwApReceivedInvalidArpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 40)
)
hwApReceivedInvalidArpNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyRadioId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyWlanId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackSrcMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackDstMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackSrcIP"))
)
if mibBuilder.loadTexts:
    hwApReceivedInvalidArpNotify.setStatus(
        "current"
    )

hwApArpExceedThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 41)
)
hwApArpExceedThresholdNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyRadioId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyWlanId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpActualRate"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpCfgRateThreshold"))
)
if mibBuilder.loadTexts:
    hwApArpExceedThresholdNotify.setStatus(
        "current"
    )

hwApColdBootNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 42)
)
hwApColdBootNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootNotifyName"))
)
if mibBuilder.loadTexts:
    hwApColdBootNotify.setStatus(
        "current"
    )

hwApColdBootRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 43)
)
hwApColdBootRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootNotifyName"))
)
if mibBuilder.loadTexts:
    hwApColdBootRestoreNotify.setStatus(
        "current"
    )

hwApHotBootNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 44)
)
hwApHotBootNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootNotifyName"))
)
if mibBuilder.loadTexts:
    hwApHotBootNotify.setStatus(
        "current"
    )

hwApHotBootRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 45)
)
hwApHotBootRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBootNotifyName"))
)
if mibBuilder.loadTexts:
    hwApHotBootRestoreNotify.setStatus(
        "current"
    )

hwStationOnlineNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 46)
)
hwStationOnlineNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaRadioId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAccessChannel"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRssi"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"))
)
if mibBuilder.loadTexts:
    hwStationOnlineNotify.setStatus(
        "current"
    )

hwStationOfflineNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 47)
)
hwStationOfflineNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaRadioId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAccessChannel"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRssi"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"))
)
if mibBuilder.loadTexts:
    hwStationOfflineNotify.setStatus(
        "current"
    )

hwStationSignalStrengthLowThanThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 48)
)
hwStationSignalStrengthLowThanThresholdNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaRadioId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRssi"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwSignalStrengthThreshold"))
)
if mibBuilder.loadTexts:
    hwStationSignalStrengthLowThanThresholdNotify.setStatus(
        "current"
    )

hwAPBroadcastStormDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 49)
)
if mibBuilder.loadTexts:
    hwAPBroadcastStormDownNotify.setStatus(
        "current"
    )

hwAPBroadcastStormDownRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 50)
)
if mibBuilder.loadTexts:
    hwAPBroadcastStormDownRestoreNotify.setStatus(
        "current"
    )

hwAPBroadcastStormUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 51)
)
if mibBuilder.loadTexts:
    hwAPBroadcastStormUpNotify.setStatus(
        "current"
    )

hwAPBroadcastStormUpRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 52)
)
if mibBuilder.loadTexts:
    hwAPBroadcastStormUpRestoreNotify.setStatus(
        "current"
    )

hwApBroadcastRestrainDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 53)
)
if mibBuilder.loadTexts:
    hwApBroadcastRestrainDownNotify.setStatus(
        "current"
    )

hwApBroadcastRestrainDownRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 54)
)
if mibBuilder.loadTexts:
    hwApBroadcastRestrainDownRestoreNotify.setStatus(
        "current"
    )

hwApBroadcastRestrainUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 55)
)
if mibBuilder.loadTexts:
    hwApBroadcastRestrainUpNotify.setStatus(
        "current"
    )

hwApBroadcastRestrainUpRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 56)
)
if mibBuilder.loadTexts:
    hwApBroadcastRestrainUpRestoreNotify.setStatus(
        "current"
    )

hwApCRCTooHighNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 57)
)
hwApCRCTooHighNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcErrActual"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcPortType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcPortID"))
)
if mibBuilder.loadTexts:
    hwApCRCTooHighNotify.setStatus(
        "current"
    )

hwApCRCTooHighRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 58)
)
hwApCRCTooHighRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcErrActual"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcPortType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwCrcPortID"))
)
if mibBuilder.loadTexts:
    hwApCRCTooHighRestoreNotify.setStatus(
        "current"
    )

hwApConflictApNameNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 59)
)
hwApConflictApNameNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSysName"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwOccurTime"))
)
if mibBuilder.loadTexts:
    hwApConflictApNameNotify.setStatus(
        "current"
    )

hwApLicenseNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 60)
)
hwApLicenseNotify.setObjects(
    ("HUAWEI-WLAN-DEVICE-MIB", "hwApLicenseInfo")
)
if mibBuilder.loadTexts:
    hwApLicenseNotify.setStatus(
        "current"
    )

hwApFmeaIICFaultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 61)
)
hwApFmeaIICFaultNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApFmeaIICFaultNotify.setStatus(
        "current"
    )

hwApFmeaIICFaultRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 62)
)
hwApFmeaIICFaultRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApFmeaIICFaultRestoreNotify.setStatus(
        "current"
    )

hwApFmeaPHYFaultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 63)
)
hwApFmeaPHYFaultNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApFmeaPHYFaultNotify.setStatus(
        "current"
    )

hwApFmeaPHYFaultRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 64)
)
hwApFmeaPHYFaultRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"))
)
if mibBuilder.loadTexts:
    hwApFmeaPHYFaultRestoreNotify.setStatus(
        "current"
    )

hwApFmeaFaultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 65)
)
hwApFmeaFaultNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIfIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultInfo"))
)
if mibBuilder.loadTexts:
    hwApFmeaFaultNotify.setStatus(
        "current"
    )

hwApFmeaFaultRestoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 66)
)
hwApFmeaFaultRestoreNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultID"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIfIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultInfo"))
)
if mibBuilder.loadTexts:
    hwApFmeaFaultRestoreNotify.setStatus(
        "current"
    )

hwApOpticalInsertNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 67)
)
hwApOpticalInsertNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIfIndex"))
)
if mibBuilder.loadTexts:
    hwApOpticalInsertNotify.setStatus(
        "current"
    )

hwApOpticalRemoveNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 68)
)
hwApOpticalRemoveNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApIfIndex"))
)
if mibBuilder.loadTexts:
    hwApOpticalRemoveNotify.setStatus(
        "current"
    )

hwApReceivedInvalidArpNewNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 69)
)
hwApReceivedInvalidArpNewNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyRadioId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotifyWlanId"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpAttackDropNum"))
)
if mibBuilder.loadTexts:
    hwApReceivedInvalidArpNewNotify.setStatus(
        "current"
    )

hwApVersionMismatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 1, 1, 70)
)
hwApVersionMismatchNotify.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApIndex"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMac"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApActualType"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApSoftwareVersion"))
)
if mibBuilder.loadTexts:
    hwApVersionMismatchNotify.setStatus(
        "current"
    )


# Notifications groups

hwWlanDeviceNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 2, 1)
)
hwWlanDeviceNotifyGroup.setObjects(
      *(("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNormalNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTypeNotMatchNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApPingResultNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApColdstartNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApConfigCommitNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApAddOffLineNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApConfirmNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwUnAuthorizedApRecordExistNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwUnAuthorizedApRecordClearNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuOverloadNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCpuOverloadRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemoryOverloadNOtify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApMemoryOverloadRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPStaFullNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPStaFullRecoverNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAcDevicesSwitchNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTimeSynFailNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwDyingGaspTrapNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFaultNotifyFat"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNormalNotifyFat"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTemperatureTooLowNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTemperatureTooLowRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTemperatureTooHighNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApTemperatureTooHighRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwRadioDownNotifyFat"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwRadioDownRecovNotifyFat"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPowerTooHighNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPowerTooHighRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPowerTooLowNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRxPowerTooLowRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperatureTooHighNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperatureTooHighRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperatureTooLowNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalTemperatureTooLowRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApNotSupportCountryCodeNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApReceivedInvalidArpNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApArpExceedThresholdNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApColdBootNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApColdBootRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApHotBootNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApHotBootRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwStationOnlineNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwStationOfflineNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwStationSignalStrengthLowThanThresholdNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPBroadcastStormDownNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPBroadcastStormDownRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPBroadcastStormUpNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwAPBroadcastStormUpRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBroadcastRestrainDownNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBroadcastRestrainDownRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBroadcastRestrainUpNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApBroadcastRestrainUpRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCRCTooHighNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApCRCTooHighRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApConflictApNameNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApLicenseNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFmeaIICFaultNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFmeaIICFaultRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFmeaPHYFaultNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFmeaPHYFaultRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFmeaFaultNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApFmeaFaultRestoreNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalInsertNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApOpticalRemoveNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApReceivedInvalidArpNewNotify"),
        ("HUAWEI-WLAN-DEVICE-MIB", "hwApVersionMismatchNotify"))
)
if mibBuilder.loadTexts:
    hwWlanDeviceNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwWlanDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hwWlanDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-DEVICE-MIB",
    **{"hwWlanDevice": hwWlanDevice,
       "hwWlanDeviceNotifications": hwWlanDeviceNotifications,
       "hwWlanDeviceNotify": hwWlanDeviceNotify,
       "hwApFaultNotify": hwApFaultNotify,
       "hwApNormalNotify": hwApNormalNotify,
       "hwApTypeNotMatchNotify": hwApTypeNotMatchNotify,
       "hwApPingResultNotify": hwApPingResultNotify,
       "hwApColdstartNotify": hwApColdstartNotify,
       "hwApConfigCommitNotify": hwApConfigCommitNotify,
       "hwApAddOffLineNotify": hwApAddOffLineNotify,
       "hwApConfirmNotify": hwApConfirmNotify,
       "hwUnAuthorizedApRecordExistNotify": hwUnAuthorizedApRecordExistNotify,
       "hwUnAuthorizedApRecordClearNotify": hwUnAuthorizedApRecordClearNotify,
       "hwApCpuOverloadNotify": hwApCpuOverloadNotify,
       "hwApCpuOverloadRestoreNotify": hwApCpuOverloadRestoreNotify,
       "hwApMemoryOverloadNOtify": hwApMemoryOverloadNOtify,
       "hwApMemoryOverloadRestoreNotify": hwApMemoryOverloadRestoreNotify,
       "hwAPStaFullNotify": hwAPStaFullNotify,
       "hwAPStaFullRecoverNotify": hwAPStaFullRecoverNotify,
       "hwAcDevicesSwitchNotify": hwAcDevicesSwitchNotify,
       "hwApTimeSynFailNotify": hwApTimeSynFailNotify,
       "hwDyingGaspTrapNotify": hwDyingGaspTrapNotify,
       "hwApFaultNotifyFat": hwApFaultNotifyFat,
       "hwApNormalNotifyFat": hwApNormalNotifyFat,
       "hwApTemperatureTooLowNotify": hwApTemperatureTooLowNotify,
       "hwApTemperatureTooLowRestoreNotify": hwApTemperatureTooLowRestoreNotify,
       "hwApTemperatureTooHighNotify": hwApTemperatureTooHighNotify,
       "hwApTemperatureTooHighRestoreNotify": hwApTemperatureTooHighRestoreNotify,
       "hwRadioDownNotifyFat": hwRadioDownNotifyFat,
       "hwRadioDownRecovNotifyFat": hwRadioDownRecovNotifyFat,
       "hwApOpticalRxPowerTooHighNotify": hwApOpticalRxPowerTooHighNotify,
       "hwApOpticalRxPowerTooHighRestoreNotify": hwApOpticalRxPowerTooHighRestoreNotify,
       "hwApOpticalRxPowerTooLowNotify": hwApOpticalRxPowerTooLowNotify,
       "hwApOpticalRxPowerTooLowRestoreNotify": hwApOpticalRxPowerTooLowRestoreNotify,
       "hwApOpticalTemperatureTooHighNotify": hwApOpticalTemperatureTooHighNotify,
       "hwApOpticalTemperatureTooHighRestoreNotify": hwApOpticalTemperatureTooHighRestoreNotify,
       "hwApOpticalTemperatureTooLowNotify": hwApOpticalTemperatureTooLowNotify,
       "hwApOpticalTemperatureTooLowRestoreNotify": hwApOpticalTemperatureTooLowRestoreNotify,
       "hwApNotSupportCountryCodeNotify": hwApNotSupportCountryCodeNotify,
       "hwApReceivedInvalidArpNotify": hwApReceivedInvalidArpNotify,
       "hwApArpExceedThresholdNotify": hwApArpExceedThresholdNotify,
       "hwApColdBootNotify": hwApColdBootNotify,
       "hwApColdBootRestoreNotify": hwApColdBootRestoreNotify,
       "hwApHotBootNotify": hwApHotBootNotify,
       "hwApHotBootRestoreNotify": hwApHotBootRestoreNotify,
       "hwStationOnlineNotify": hwStationOnlineNotify,
       "hwStationOfflineNotify": hwStationOfflineNotify,
       "hwStationSignalStrengthLowThanThresholdNotify": hwStationSignalStrengthLowThanThresholdNotify,
       "hwAPBroadcastStormDownNotify": hwAPBroadcastStormDownNotify,
       "hwAPBroadcastStormDownRestoreNotify": hwAPBroadcastStormDownRestoreNotify,
       "hwAPBroadcastStormUpNotify": hwAPBroadcastStormUpNotify,
       "hwAPBroadcastStormUpRestoreNotify": hwAPBroadcastStormUpRestoreNotify,
       "hwApBroadcastRestrainDownNotify": hwApBroadcastRestrainDownNotify,
       "hwApBroadcastRestrainDownRestoreNotify": hwApBroadcastRestrainDownRestoreNotify,
       "hwApBroadcastRestrainUpNotify": hwApBroadcastRestrainUpNotify,
       "hwApBroadcastRestrainUpRestoreNotify": hwApBroadcastRestrainUpRestoreNotify,
       "hwApCRCTooHighNotify": hwApCRCTooHighNotify,
       "hwApCRCTooHighRestoreNotify": hwApCRCTooHighRestoreNotify,
       "hwApConflictApNameNotify": hwApConflictApNameNotify,
       "hwApLicenseNotify": hwApLicenseNotify,
       "hwApFmeaIICFaultNotify": hwApFmeaIICFaultNotify,
       "hwApFmeaIICFaultRestoreNotify": hwApFmeaIICFaultRestoreNotify,
       "hwApFmeaPHYFaultNotify": hwApFmeaPHYFaultNotify,
       "hwApFmeaPHYFaultRestoreNotify": hwApFmeaPHYFaultRestoreNotify,
       "hwApFmeaFaultNotify": hwApFmeaFaultNotify,
       "hwApFmeaFaultRestoreNotify": hwApFmeaFaultRestoreNotify,
       "hwApOpticalInsertNotify": hwApOpticalInsertNotify,
       "hwApOpticalRemoveNotify": hwApOpticalRemoveNotify,
       "hwApReceivedInvalidArpNewNotify": hwApReceivedInvalidArpNewNotify,
       "hwApVersionMismatchNotify": hwApVersionMismatchNotify,
       "hwWlanDeviceNotifyObjects": hwWlanDeviceNotifyObjects,
       "hwApActualType": hwApActualType,
       "hwApCpuOccupancyRate": hwApCpuOccupancyRate,
       "hwApMemoryOccupancyRate": hwApMemoryOccupancyRate,
       "hwApPermitStaNum": hwApPermitStaNum,
       "hwStaAuthFailCause": hwStaAuthFailCause,
       "hwAcSystemSwitchType": hwAcSystemSwitchType,
       "hwApRadioNotifyPara": hwApRadioNotifyPara,
       "hwApOpticalRxPower": hwApOpticalRxPower,
       "hwApOpticalTemperature": hwApOpticalTemperature,
       "hwApCfgCountryCode": hwApCfgCountryCode,
       "hwApArpAttackSrcMac": hwApArpAttackSrcMac,
       "hwApArpAttackDstMac": hwApArpAttackDstMac,
       "hwApArpAttackSrcIP": hwApArpAttackSrcIP,
       "hwApArpCfgRateThreshold": hwApArpCfgRateThreshold,
       "hwApArpActualRate": hwApArpActualRate,
       "hwApNotifyRadioId": hwApNotifyRadioId,
       "hwApNotifyOrRestoreTemperature": hwApNotifyOrRestoreTemperature,
       "hwOccurTime": hwOccurTime,
       "hwApBootNotifyName": hwApBootNotifyName,
       "hwApFaultTimes": hwApFaultTimes,
       "hwSignalStrengthThreshold": hwSignalStrengthThreshold,
       "hwStaBroadcastFlux": hwStaBroadcastFlux,
       "hwBroadcastWarnThresholdDown": hwBroadcastWarnThresholdDown,
       "hwBroadcastWarnThresholdUp": hwBroadcastWarnThresholdUp,
       "hwBroadcastRestrainThresholdDown": hwBroadcastRestrainThresholdDown,
       "hwBroadcastRestrainThresholdUp": hwBroadcastRestrainThresholdUp,
       "hwApBroadcastFlux": hwApBroadcastFlux,
       "hwCrcErrActual": hwCrcErrActual,
       "hwCrcThreshold": hwCrcThreshold,
       "hwApNotifyWlanId": hwApNotifyWlanId,
       "hwApLicenseInfo": hwApLicenseInfo,
       "hwCrcPortType": hwCrcPortType,
       "hwCrcPortID": hwCrcPortID,
       "hwApArpAttackDropNum": hwApArpAttackDropNum,
       "hwApFaultID": hwApFaultID,
       "hwApIfIndex": hwApIfIndex,
       "hwApFaultInfo": hwApFaultInfo,
       "hwApTypeObjects": hwApTypeObjects,
       "hwApTypeTable": hwApTypeTable,
       "hwApTypeEntry": hwApTypeEntry,
       "hwApType": hwApType,
       "hwApTypeDesc": hwApTypeDesc,
       "hwApTypeLineatePortNum": hwApTypeLineatePortNum,
       "hwApTypeRadioNum": hwApTypeRadioNum,
       "hwApTypeMaxStaNum": hwApTypeMaxStaNum,
       "hwApTypeMaxSsidNum": hwApTypeMaxSsidNum,
       "hwApTypeAntennaGain": hwApTypeAntennaGain,
       "hwApTypeRowStatus": hwApTypeRowStatus,
       "hwApTypeReset": hwApTypeReset,
       "hwApTypeRadioTable": hwApTypeRadioTable,
       "hwApTypeRadioEntry": hwApTypeRadioEntry,
       "hwApTypeRadioIndex": hwApTypeRadioIndex,
       "hwApTypeRadioType": hwApTypeRadioType,
       "hwRadioMaxSpatialStreamsNum": hwRadioMaxSpatialStreamsNum,
       "hwRadioMaxAntennasNum": hwRadioMaxAntennasNum,
       "hwRadioMaxVAPNum": hwRadioMaxVAPNum,
       "hwApTypeRadioAntennaGain": hwApTypeRadioAntennaGain,
       "hwApTypeLineatePortInfoTable": hwApTypeLineatePortInfoTable,
       "hwApTypeLineatePortInfoEntry": hwApTypeLineatePortInfoEntry,
       "hwApTypeLineatePortIndex": hwApTypeLineatePortIndex,
       "hwApTypeLineatePortType": hwApTypeLineatePortType,
       "hwApTypeLineatePortName": hwApTypeLineatePortName,
       "hwApProfileObjects": hwApProfileObjects,
       "hwApProfileTable": hwApProfileTable,
       "hwApProfileEntry": hwApProfileEntry,
       "hwApProfileName": hwApProfileName,
       "hwApEthPortMtu": hwApEthPortMtu,
       "hwApDosDefend": hwApDosDefend,
       "hwApWorkMode": hwApWorkMode,
       "hwApLogBackupServerIp": hwApLogBackupServerIp,
       "hwApLogBackupMode": hwApLogBackupMode,
       "hwApProfileRowStatus": hwApProfileRowStatus,
       "hwApSampleTime": hwApSampleTime,
       "hwApStatisticsInterval": hwApStatisticsInterval,
       "hwApEapStartMode": hwApEapStartMode,
       "hwApEapStartUnicastMac": hwApEapStartUnicastMac,
       "hwApEapStartTransform": hwApEapStartTransform,
       "hwApEapResponseMode": hwApEapResponseMode,
       "hwApEapResponseUnicastMac": hwApEapResponseUnicastMac,
       "hwApEapResponseTransform": hwApEapResponseTransform,
       "hwApOfflineManagement": hwApOfflineManagement,
       "hwApAlarmRestrictionMode": hwApAlarmRestrictionMode,
       "hwApAlarmRestrictionPeriod": hwApAlarmRestrictionPeriod,
       "hwAp4WayHandshakeRoamPolicy": hwAp4WayHandshakeRoamPolicy,
       "hwApLogRecordLevel": hwApLogRecordLevel,
       "hwApLogBackupPeriodTime": hwApLogBackupPeriodTime,
       "hwApLogRecordFtpMode": hwApLogRecordFtpMode,
       "hwApLogServerUsername": hwApLogServerUsername,
       "hwApLogServerUserPassword": hwApLogServerUserPassword,
       "hwApLogServerIp": hwApLogServerIp,
       "hwApProfileTelnetSwitch": hwApProfileTelnetSwitch,
       "hwApSshSwitch": hwApSshSwitch,
       "hwApProfileDhcpTrustPort": hwApProfileDhcpTrustPort,
       "hwApProfileConsoleSwitch": hwApProfileConsoleSwitch,
       "hwApProfileMaxUserNum": hwApProfileMaxUserNum,
       "hwApProfileNdTrustPort": hwApProfileNdTrustPort,
       "hwApLogBackupServerIpv6Addr": hwApLogBackupServerIpv6Addr,
       "hwApLedSwitch": hwApLedSwitch,
       "hwApLocalAssocResSwitch": hwApLocalAssocResSwitch,
       "hwApProfileDefault": hwApProfileDefault,
       "hwApProfileBatchInfo": hwApProfileBatchInfo,
       "hwApProfileBatchStart": hwApProfileBatchStart,
       "hwApProfileBatchNumber": hwApProfileBatchNumber,
       "hwApProfileBatchReturnNumber": hwApProfileBatchReturnNumber,
       "hwApProfileBatchNameList": hwApProfileBatchNameList,
       "hwApAuthListObjects": hwApAuthListObjects,
       "hwApMacWhitelistTable": hwApMacWhitelistTable,
       "hwApMacWhitelistEntry": hwApMacWhitelistEntry,
       "hwApMacWhitelistMacAddr": hwApMacWhitelistMacAddr,
       "hwApMacWhitelistRowStatus": hwApMacWhitelistRowStatus,
       "hwApSnWhitelistTable": hwApSnWhitelistTable,
       "hwApSnWhitelistEntry": hwApSnWhitelistEntry,
       "hwApSnWhitelistSn": hwApSnWhitelistSn,
       "hwApSnWhitelistRowStatus": hwApSnWhitelistRowStatus,
       "hwApAuthMode": hwApAuthMode,
       "hwApMacWhitelistBatchQueryInfo": hwApMacWhitelistBatchQueryInfo,
       "hwApMacWhitelistBatchQueryStartNumber": hwApMacWhitelistBatchQueryStartNumber,
       "hwApMacWhitelistBatchQueryNumber": hwApMacWhitelistBatchQueryNumber,
       "hwApMacWhitelistBatchQueryList": hwApMacWhitelistBatchQueryList,
       "hwApMacWhitelistBatchQueryReturnNumber": hwApMacWhitelistBatchQueryReturnNumber,
       "hwApSnWhitelistBatchQueryInfo": hwApSnWhitelistBatchQueryInfo,
       "hwApSnWhitelistBatchQueryStartNumber": hwApSnWhitelistBatchQueryStartNumber,
       "hwApSnWhitelistBatchQueryNumber": hwApSnWhitelistBatchQueryNumber,
       "hwApSnWhitelistBatchQueryList": hwApSnWhitelistBatchQueryList,
       "hwApSnWhitelistBatchQueryReturnNumber": hwApSnWhitelistBatchQueryReturnNumber,
       "hwApMacBlacklistTable": hwApMacBlacklistTable,
       "hwApMacBlacklistEntry": hwApMacBlacklistEntry,
       "hwApMacBlacklistMacAddr": hwApMacBlacklistMacAddr,
       "hwApMacBlacklistRowStatus": hwApMacBlacklistRowStatus,
       "hwApSnBlacklistTable": hwApSnBlacklistTable,
       "hwApSnBlacklistEntry": hwApSnBlacklistEntry,
       "hwApSnBlacklistSn": hwApSnBlacklistSn,
       "hwApSnBlacklistRowStatus": hwApSnBlacklistRowStatus,
       "hwApRegionObjects": hwApRegionObjects,
       "hwApRegionTable": hwApRegionTable,
       "hwApRegionEntry": hwApRegionEntry,
       "hwApRegionIndex": hwApRegionIndex,
       "hwApRegionName": hwApRegionName,
       "hwApRegionDeployMode": hwApRegionDeployMode,
       "hwApRegionApNumber": hwApRegionApNumber,
       "hwApRegionApIndexMask": hwApRegionApIndexMask,
       "hwApRegionRowStatus": hwApRegionRowStatus,
       "hwApRegionForwardMode": hwApRegionForwardMode,
       "hwApRegionCountryCode": hwApRegionCountryCode,
       "hwApRegionScanChannel2G": hwApRegionScanChannel2G,
       "hwApRegionScanChannel5G": hwApRegionScanChannel5G,
       "hwApRegionCalibrateChannel2G": hwApRegionCalibrateChannel2G,
       "hwApRegionCalibrateChannel5G": hwApRegionCalibrateChannel5G,
       "hwApRegionCalibrate5gBandWidth": hwApRegionCalibrate5gBandWidth,
       "hwApRegionGlobalInfo": hwApRegionGlobalInfo,
       "hwApRegionDefault": hwApRegionDefault,
       "hwApRegionAllExistRegionIndexMask": hwApRegionAllExistRegionIndexMask,
       "hwApRegionBatchInfo": hwApRegionBatchInfo,
       "hwApRegionBatchStart": hwApRegionBatchStart,
       "hwApRegionBatchNumber": hwApRegionBatchNumber,
       "hwApRegionBatchReturnNumber": hwApRegionBatchReturnNumber,
       "hwApRegionBatchNameList": hwApRegionBatchNameList,
       "hwApRegionBatchDeployMode": hwApRegionBatchDeployMode,
       "hwApRegionMerge": hwApRegionMerge,
       "hwApSrcRegionIndex": hwApSrcRegionIndex,
       "hwApDestRegionIndex": hwApDestRegionIndex,
       "hwApObjects": hwApObjects,
       "hwApTable": hwApTable,
       "hwApEntry": hwApEntry,
       "hwApIndex": hwApIndex,
       "hwApUsedType": hwApUsedType,
       "hwApUsedProfileName": hwApUsedProfileName,
       "hwApUsedRegionIndex": hwApUsedRegionIndex,
       "hwApMac": hwApMac,
       "hwApSn": hwApSn,
       "hwApSysName": hwApSysName,
       "hwApRunState": hwApRunState,
       "hwApSoftwareVersion": hwApSoftwareVersion,
       "hwApHardwareVersion": hwApHardwareVersion,
       "hwApCpuType": hwApCpuType,
       "hwApCpufrequency": hwApCpufrequency,
       "hwApMemoryType": hwApMemoryType,
       "hwApDomain": hwApDomain,
       "hwApIpAddress": hwApIpAddress,
       "hwApIpNetMask": hwApIpNetMask,
       "hwApGatewayIp": hwApGatewayIp,
       "hwApMemorySize": hwApMemorySize,
       "hwApFlashSize": hwApFlashSize,
       "hwApRunTime": hwApRunTime,
       "hwApUpEthPortSpeed": hwApUpEthPortSpeed,
       "hwApUpEthPortSpeedMode": hwApUpEthPortSpeedMode,
       "hwApUpEthPortDuplex": hwApUpEthPortDuplex,
       "hwApUpEthPortDuplexMode": hwApUpEthPortDuplexMode,
       "hwApAdminOper": hwApAdminOper,
       "hwApRowstatus": hwApRowstatus,
       "hwApPerformanceStatCycle": hwApPerformanceStatCycle,
       "hwApDNS": hwApDNS,
       "hwApRunningMode": hwApRunningMode,
       "hwApForwardMode": hwApForwardMode,
       "hwApAntennaMode": hwApAntennaMode,
       "hwApCpuThreshold": hwApCpuThreshold,
       "hwApMemThreshold": hwApMemThreshold,
       "hwApNEnumber": hwApNEnumber,
       "hwApOnlineTime": hwApOnlineTime,
       "hwApSysSoftwareDesc": hwApSysSoftwareDesc,
       "hwApSysHardtwareDesc": hwApSysHardtwareDesc,
       "hwApSysManufacture": hwApSysManufacture,
       "hwApSysSoftwareName": hwApSysSoftwareName,
       "hwApSysSoftwareVendor": hwApSysSoftwareVendor,
       "hwApManagementVlanID": hwApManagementVlanID,
       "hwApUsername": hwApUsername,
       "hwApPassword": hwApPassword,
       "hwApAcIP1": hwApAcIP1,
       "hwApAcIP2": hwApAcIP2,
       "hwApAcIP3": hwApAcIP3,
       "hwApAcIP4": hwApAcIP4,
       "hwApIpMode": hwApIpMode,
       "hwApLldpEnable": hwApLldpEnable,
       "hwApLldpManageAddr": hwApLldpManageAddr,
       "hwApLldpPortDes": hwApLldpPortDes,
       "hwApLldpSysCab": hwApLldpSysCab,
       "hwApLldpSysDes": hwApLldpSysDes,
       "hwApLldpSysName": hwApLldpSysName,
       "hwApLldpDelay": hwApLldpDelay,
       "hwApLldpHoldMultiplier": hwApLldpHoldMultiplier,
       "hwApLldpInterval": hwApLldpInterval,
       "hwApLldpRestartDelay": hwApLldpRestartDelay,
       "hwApLldpAdminStatus": hwApLldpAdminStatus,
       "hwApLldpReportInterval": hwApLldpReportInterval,
       "hwApBomCode": hwApBomCode,
       "hwApSaveMode": hwApSaveMode,
       "hwApProtectAcPriority": hwApProtectAcPriority,
       "hwApProtectAcIP": hwApProtectAcIP,
       "hwApOpticalHighRxPowerThreshold": hwApOpticalHighRxPowerThreshold,
       "hwApOpticalLowRxPowerThreshold": hwApOpticalLowRxPowerThreshold,
       "hwApOpticalHighTemperatureThreshold": hwApOpticalHighTemperatureThreshold,
       "hwApOpticalLowTemperatureThreshold": hwApOpticalLowTemperatureThreshold,
       "hwApKeepService": hwApKeepService,
       "hwApPriorityAccessMode": hwApPriorityAccessMode,
       "hwApLineateportMode": hwApLineateportMode,
       "hwApLineateportVlanTagged": hwApLineateportVlanTagged,
       "hwApLineateportVlanUntagged": hwApLineateportVlanUntagged,
       "hwApLineateportPvidVlan": hwApLineateportPvidVlan,
       "hwApLineateportUserIsolate": hwApLineateportUserIsolate,
       "hwApLineateportStpEnable": hwApLineateportStpEnable,
       "hwApHighTemperatureThreshold": hwApHighTemperatureThreshold,
       "hwApLowTemperatureThreshold": hwApLowTemperatureThreshold,
       "hwApReset": hwApReset,
       "hwApStaticIpAddress": hwApStaticIpAddress,
       "hwApStaticNetMask": hwApStaticNetMask,
       "hwApStaticGatewayIp": hwApStaticGatewayIp,
       "hwApAttackFloodInterval": hwApAttackFloodInterval,
       "hwApAttackFloodTimes": hwApAttackFloodTimes,
       "hwApDynamicBlacklistEnable": hwApDynamicBlacklistEnable,
       "hwApDynamicBlacklistAgingInt": hwApDynamicBlacklistAgingInt,
       "hwApAttackPskInterval": hwApAttackPskInterval,
       "hwApAttackPskTimes": hwApAttackPskTimes,
       "hwApAccessBalanceGap": hwApAccessBalanceGap,
       "hwApIpv6Address": hwApIpv6Address,
       "hwApIpv6NetMask": hwApIpv6NetMask,
       "hwApGatewayIpv6": hwApGatewayIpv6,
       "hwApIpv6DNS": hwApIpv6DNS,
       "hwApProtectAcIPv6Addr": hwApProtectAcIPv6Addr,
       "hwApLineatePortCfgMtu": hwApLineatePortCfgMtu,
       "hwApLineatePortMacAddress": hwApLineatePortMacAddress,
       "hwApAccessBalanceSwitch": hwApAccessBalanceSwitch,
       "hwApNatIpAddress": hwApNatIpAddress,
       "hwApAttackFloodQuietTime": hwApAttackFloodQuietTime,
       "hwApAttackPskQuietTime": hwApAttackPskQuietTime,
       "hwApAttackWeakivQuietTime": hwApAttackWeakivQuietTime,
       "hwApAttackSpoofQuietTime": hwApAttackSpoofQuietTime,
       "hwApBootCountTotal": hwApBootCountTotal,
       "hwApBootCountPowerOff": hwApBootCountPowerOff,
       "hwApBootCountRowStatus": hwApBootCountRowStatus,
       "hwApLineatePortTable": hwApLineatePortTable,
       "hwApLineatePortEntry": hwApLineatePortEntry,
       "hwApLineatePortIndex": hwApLineatePortIndex,
       "hwApLineatePortType": hwApLineatePortType,
       "hwApLineatePortDesc": hwApLineatePortDesc,
       "hwApLineatePortState": hwApLineatePortState,
       "hwApLineatePortSpeed": hwApLineatePortSpeed,
       "hwApMultiLineatePortDuplex": hwApMultiLineatePortDuplex,
       "hwApMultiLineatePortNegotiation": hwApMultiLineatePortNegotiation,
       "hwApMultiLineatePortMode": hwApMultiLineatePortMode,
       "hwApMultiLineatePortUserIsolate": hwApMultiLineatePortUserIsolate,
       "hwApMultiLineatePortStpEnable": hwApMultiLineatePortStpEnable,
       "hwApMultiLineatePortVlanTagged": hwApMultiLineatePortVlanTagged,
       "hwApMultiLineatePortVlanUntagged": hwApMultiLineatePortVlanUntagged,
       "hwApMultiLineatePortPvidVlan": hwApMultiLineatePortPvidVlan,
       "hwApMultiLineatePortCRCErrorHighThreshold": hwApMultiLineatePortCRCErrorHighThreshold,
       "hwApMultiLineatePortCRCErrorLowThreshold": hwApMultiLineatePortCRCErrorLowThreshold,
       "hwApMultiLineatePortCRCErrorSwitch": hwApMultiLineatePortCRCErrorSwitch,
       "hwApLineatePortAclNumInbound": hwApLineatePortAclNumInbound,
       "hwApLineatePortAclNumOutbound": hwApLineatePortAclNumOutbound,
       "hwApLineatePortAclNameInbound": hwApLineatePortAclNameInbound,
       "hwApLineatePortAclNameOutbound": hwApLineatePortAclNameOutbound,
       "hwApLineatePortAclSwitchInbound": hwApLineatePortAclSwitchInbound,
       "hwApLineatePortAclSwitchOutbound": hwApLineatePortAclSwitchOutbound,
       "hwApLineatePortAclNumInboundIPV6": hwApLineatePortAclNumInboundIPV6,
       "hwApLineatePortAclNumOutboundIPV6": hwApLineatePortAclNumOutboundIPV6,
       "hwApLineatePortAclNameInboundIPV6": hwApLineatePortAclNameInboundIPV6,
       "hwApLineatePortAclNameOutboundIPV6": hwApLineatePortAclNameOutboundIPV6,
       "hwApLineatePortAclSwitchInboundIPV6": hwApLineatePortAclSwitchInboundIPV6,
       "hwApLineatePortAclSwitchOutboundIPV6": hwApLineatePortAclSwitchOutboundIPV6,
       "hwApMultiLineatePortIsAddInTrunk": hwApMultiLineatePortIsAddInTrunk,
       "hwApMultiLineatePortAddedOrExitTrunkID": hwApMultiLineatePortAddedOrExitTrunkID,
       "hwApGlobalInfo": hwApGlobalInfo,
       "hwApAllExistApIndexMask": hwApAllExistApIndexMask,
       "hwUnAuthorizedApRecordNumber": hwUnAuthorizedApRecordNumber,
       "hwUnAuthorizedApRecordAdmin": hwUnAuthorizedApRecordAdmin,
       "hwApResetAllOnlineFailRecord": hwApResetAllOnlineFailRecord,
       "hwApResetAllOfflineRecord": hwApResetAllOfflineRecord,
       "hwApResetAllBootCountRecord": hwApResetAllBootCountRecord,
       "hwApBatchInfo": hwApBatchInfo,
       "hwApBatchIndexStart": hwApBatchIndexStart,
       "hwApBatchIndexNumber": hwApBatchIndexNumber,
       "hwApBatchIndexReturnNumber": hwApBatchIndexReturnNumber,
       "hwApBatchState": hwApBatchState,
       "hwApBatchNameList": hwApBatchNameList,
       "hwApPing": hwApPing,
       "hwApPingIndex": hwApPingIndex,
       "hwApPingAddress": hwApPingAddress,
       "hwApPingCount": hwApPingCount,
       "hwApPingPacketSize": hwApPingPacketSize,
       "hwApPingWaitTime": hwApPingWaitTime,
       "hwApPingTimeOut": hwApPingTimeOut,
       "hwApPingResultSuccessCount": hwApPingResultSuccessCount,
       "hwApPingResultFailureCount": hwApPingResultFailureCount,
       "hwApPingResultAverageResponseTime": hwApPingResultAverageResponseTime,
       "hwApPingResultMinimumResponseTime": hwApPingResultMinimumResponseTime,
       "hwApPingResultMaximumResponseTime": hwApPingResultMaximumResponseTime,
       "hwApPingApMac": hwApPingApMac,
       "hwApPingResultFlag": hwApPingResultFlag,
       "hwApPerformanceStatTable": hwApPerformanceStatTable,
       "hwApPerformanceStatEntry": hwApPerformanceStatEntry,
       "hwApMemoryUseRate": hwApMemoryUseRate,
       "hwApCpuUseRate": hwApCpuUseRate,
       "hwApFlashFreeSize": hwApFlashFreeSize,
       "hwApTemperature": hwApTemperature,
       "hwApOnlineUserNum": hwApOnlineUserNum,
       "hwApUpPortSpeed": hwApUpPortSpeed,
       "hwApUpPortRecvFrames": hwApUpPortRecvFrames,
       "hwApUpPortRecvRightFrames": hwApUpPortRecvRightFrames,
       "hwApUpPortRecvErrorFrames": hwApUpPortRecvErrorFrames,
       "hwApUpPortSendFrames": hwApUpPortSendFrames,
       "hwApUpPortRecvBytes": hwApUpPortRecvBytes,
       "hwApUpPortSendBytes": hwApUpPortSendBytes,
       "hwAPUpPortPER": hwAPUpPortPER,
       "hwAPWirelessUpPortTraffic": hwAPWirelessUpPortTraffic,
       "hwAPUpPortTraffic": hwAPUpPortTraffic,
       "hwApAirportSendDropFrames": hwApAirportSendDropFrames,
       "hwApEthportRecvDropFrames": hwApEthportRecvDropFrames,
       "hwApAirportUpTraffic": hwApAirportUpTraffic,
       "hwApAirportDwTraffic": hwApAirportDwTraffic,
       "hwApEthportDwTraffic": hwApEthportDwTraffic,
       "hwApEthportUpTraffic": hwApEthportUpTraffic,
       "hwApAirportRecvDropPacket": hwApAirportRecvDropPacket,
       "hwApAirportRecvErrorPacket": hwApAirportRecvErrorPacket,
       "hwApEthportRecvUnicastPacket": hwApEthportRecvUnicastPacket,
       "hwApEthportRecvNonUnicastPacket": hwApEthportRecvNonUnicastPacket,
       "hwApEthportSendUnicastPacket": hwApEthportSendUnicastPacket,
       "hwApEthportSendNonUnicastPacket": hwApEthportSendNonUnicastPacket,
       "hwApAvgRCPUUseRate": hwApAvgRCPUUseRate,
       "hwApAvgRMemoryUseRate": hwApAvgRMemoryUseRate,
       "hwEthportSendDropFrames": hwEthportSendDropFrames,
       "hwEthportSendErrorFrames": hwEthportSendErrorFrames,
       "hwEthportUpDwnTimes": hwEthportUpDwnTimes,
       "hwApAirportRecvUnicastFrames": hwApAirportRecvUnicastFrames,
       "hwApEthportRecvUnknownFrames": hwApEthportRecvUnknownFrames,
       "hwApEthportUpRate": hwApEthportUpRate,
       "hwApEthportDownRate": hwApEthportDownRate,
       "hwApUpPortRecvFrames64Bits": hwApUpPortRecvFrames64Bits,
       "hwApUpPortRecvRightFrames64Bits": hwApUpPortRecvRightFrames64Bits,
       "hwApUpPortRecvErrorFrames64Bits": hwApUpPortRecvErrorFrames64Bits,
       "hwApUpPortSendFrames64Bits": hwApUpPortSendFrames64Bits,
       "hwApUpPortRecvBytes64Bits": hwApUpPortRecvBytes64Bits,
       "hwApUpPortSendBytes64Bits": hwApUpPortSendBytes64Bits,
       "hwAPWirelessUpPortTraffic64Bits": hwAPWirelessUpPortTraffic64Bits,
       "hwAPUpPortTraffic64Bits": hwAPUpPortTraffic64Bits,
       "hwApAirportSendDropFrames64Bits": hwApAirportSendDropFrames64Bits,
       "hwApEthportRecvDropFrames64Bits": hwApEthportRecvDropFrames64Bits,
       "hwApAirportRecvDropPacket64Bits": hwApAirportRecvDropPacket64Bits,
       "hwApAirportRecvErrorPacket64Bits": hwApAirportRecvErrorPacket64Bits,
       "hwApEthportRecvUnicastPacket64Bits": hwApEthportRecvUnicastPacket64Bits,
       "hwApEthportRecvNonUnicastPacket64Bits": hwApEthportRecvNonUnicastPacket64Bits,
       "hwApEthportSendUnicastPacket64Bits": hwApEthportSendUnicastPacket64Bits,
       "hwApEthportSendNonUnicastPacket64Bits": hwApEthportSendNonUnicastPacket64Bits,
       "hwApUnauthorizedApRecordTable": hwApUnauthorizedApRecordTable,
       "hwApUnauthorizedApRecordEntry": hwApUnauthorizedApRecordEntry,
       "hwApUnauthorizedApRecordIndex": hwApUnauthorizedApRecordIndex,
       "hwApUnauthorizedApType": hwApUnauthorizedApType,
       "hwApUnauthorizedApMacAddress": hwApUnauthorizedApMacAddress,
       "hwApUnauthorizedApSn": hwApUnauthorizedApSn,
       "hwApUnauthorizedApIpAddress": hwApUnauthorizedApIpAddress,
       "hwApUnauthorizedApRecordTime": hwApUnauthorizedApRecordTime,
       "hwApParaStatisticTable": hwApParaStatisticTable,
       "hwApParaStatisticEntry": hwApParaStatisticEntry,
       "hwApStaAveSignalStrength": hwApStaAveSignalStrength,
       "hwMacApTable": hwMacApTable,
       "hwMacApEntry": hwMacApEntry,
       "hwMacApMac": hwMacApMac,
       "hwMacApIndex": hwMacApIndex,
       "hwMacApUsedType": hwMacApUsedType,
       "hwMacApUsedProfileName": hwMacApUsedProfileName,
       "hwMacApUsedRegionIndex": hwMacApUsedRegionIndex,
       "hwMacApSn": hwMacApSn,
       "hwMacApSysName": hwMacApSysName,
       "hwMacApRunState": hwMacApRunState,
       "hwMacApSoftwareVersion": hwMacApSoftwareVersion,
       "hwMacApHardwareVersion": hwMacApHardwareVersion,
       "hwMacApCpuType": hwMacApCpuType,
       "hwMacApCpufrequency": hwMacApCpufrequency,
       "hwMacApMemoryType": hwMacApMemoryType,
       "hwMacApDomain": hwMacApDomain,
       "hwMacApIpAddress": hwMacApIpAddress,
       "hwMacApIpNetMask": hwMacApIpNetMask,
       "hwMacApGatewayIp": hwMacApGatewayIp,
       "hwMacApMemorySize": hwMacApMemorySize,
       "hwMacApFlashSize": hwMacApFlashSize,
       "hwMacApRunTime": hwMacApRunTime,
       "hwMacApUpEthPortSpeed": hwMacApUpEthPortSpeed,
       "hwMacApUpEthPortSpeedMode": hwMacApUpEthPortSpeedMode,
       "hwMacApUpEthPortDuplex": hwMacApUpEthPortDuplex,
       "hwMacApUpEthPortDuplexMode": hwMacApUpEthPortDuplexMode,
       "hwMacApAdminOper": hwMacApAdminOper,
       "hwMacApRowstatus": hwMacApRowstatus,
       "hwMacApPerformanceStatCycle": hwMacApPerformanceStatCycle,
       "hwMacApDNS": hwMacApDNS,
       "hwMacApRunningMode": hwMacApRunningMode,
       "hwMacApForwardMode": hwMacApForwardMode,
       "hwMacApAntennaMode": hwMacApAntennaMode,
       "hwMacApCpuThreshold": hwMacApCpuThreshold,
       "hwMacApMemThreshold": hwMacApMemThreshold,
       "hwMacApNEnumber": hwMacApNEnumber,
       "hwMacApOnlineTime": hwMacApOnlineTime,
       "hwMacApSysSoftwareDesc": hwMacApSysSoftwareDesc,
       "hwMacApSysHardtwareDesc": hwMacApSysHardtwareDesc,
       "hwMacApSysManufacture": hwMacApSysManufacture,
       "hwMacApSysSoftwareName": hwMacApSysSoftwareName,
       "hwMacApSysSoftwareVendor": hwMacApSysSoftwareVendor,
       "hwMacApManagementVlanID": hwMacApManagementVlanID,
       "hwMacApUsername": hwMacApUsername,
       "hwMacApPassword": hwMacApPassword,
       "hwMacApAcIP1": hwMacApAcIP1,
       "hwMacApAcIP2": hwMacApAcIP2,
       "hwMacApAcIP3": hwMacApAcIP3,
       "hwMacApAcIP4": hwMacApAcIP4,
       "hwMacApIpMode": hwMacApIpMode,
       "hwMacApLldpEnable": hwMacApLldpEnable,
       "hwMacApLldpManageAddr": hwMacApLldpManageAddr,
       "hwMacApLldpPortDes": hwMacApLldpPortDes,
       "hwMacApLldpSysCab": hwMacApLldpSysCab,
       "hwMacApLldpSysDes": hwMacApLldpSysDes,
       "hwMacApLldpSysName": hwMacApLldpSysName,
       "hwMacApLldpDelay": hwMacApLldpDelay,
       "hwMacApLldpHoldMultiplier": hwMacApLldpHoldMultiplier,
       "hwMacApLldpInterval": hwMacApLldpInterval,
       "hwMacApLldpRestartDelay": hwMacApLldpRestartDelay,
       "hwMacApLldpAdminStatus": hwMacApLldpAdminStatus,
       "hwMacApLldpReportInterval": hwMacApLldpReportInterval,
       "hwMacApBomCode": hwMacApBomCode,
       "hwMacApSaveMode": hwMacApSaveMode,
       "hwMacApProtectAcPriority": hwMacApProtectAcPriority,
       "hwMacApProtectAcIP": hwMacApProtectAcIP,
       "hwMacApOpticalHighRxPowerThreshold": hwMacApOpticalHighRxPowerThreshold,
       "hwMacApOpticalLowRxPowerThreshold": hwMacApOpticalLowRxPowerThreshold,
       "hwMacApOpticalHighTemperatureThreshold": hwMacApOpticalHighTemperatureThreshold,
       "hwMacApOpticalLowTemperatureThreshold": hwMacApOpticalLowTemperatureThreshold,
       "hwMacApKeepService": hwMacApKeepService,
       "hwMacApPriorityAccessMode": hwMacApPriorityAccessMode,
       "hwMacApLineateportMode": hwMacApLineateportMode,
       "hwMacApLineateportVlanTagged": hwMacApLineateportVlanTagged,
       "hwMacApLineateportVlanUntagged": hwMacApLineateportVlanUntagged,
       "hwMacApLineateportPvidVlan": hwMacApLineateportPvidVlan,
       "hwMacApLineateportUserIsolate": hwMacApLineateportUserIsolate,
       "hwMacApLineateportStpEnable": hwMacApLineateportStpEnable,
       "hwMacApHighTemperatureThreshold": hwMacApHighTemperatureThreshold,
       "hwMacApLowTemperatureThreshold": hwMacApLowTemperatureThreshold,
       "hwMacApReset": hwMacApReset,
       "hwMacApStaticIpAddress": hwMacApStaticIpAddress,
       "hwMacApStaticNetMask": hwMacApStaticNetMask,
       "hwMacApStaticGatewayIp": hwMacApStaticGatewayIp,
       "hwMacApAttackFloodInterval": hwMacApAttackFloodInterval,
       "hwMACApAttackFloodTimes": hwMACApAttackFloodTimes,
       "hwMACApDynamicBlacklistEnable": hwMACApDynamicBlacklistEnable,
       "hwMACApDynamicBlacklistAgingInt": hwMACApDynamicBlacklistAgingInt,
       "hwMACApAttackPskInterval": hwMACApAttackPskInterval,
       "hwMACApAttackPskTimes": hwMACApAttackPskTimes,
       "hwMACApAccessBalanceGap": hwMACApAccessBalanceGap,
       "hwMACApIpv6Address": hwMACApIpv6Address,
       "hwMACApIpv6NetMask": hwMACApIpv6NetMask,
       "hwMACApGatewayIpv6": hwMACApGatewayIpv6,
       "hwMACApIpv6DNS": hwMACApIpv6DNS,
       "hwMACApProtectAcIPv6Addr": hwMACApProtectAcIPv6Addr,
       "hwMACApLineatePortCfgMtu": hwMACApLineatePortCfgMtu,
       "hwMACApLineatePortMacAddress": hwMACApLineatePortMacAddress,
       "hwMACApAccessBalanceSwitch": hwMACApAccessBalanceSwitch,
       "hwMACApNatIpAddress": hwMACApNatIpAddress,
       "hwMACApAttackFloodQuietTime": hwMACApAttackFloodQuietTime,
       "hwMACApAttackPskQuietTime": hwMACApAttackPskQuietTime,
       "hwMACApAttackWeakivQuietTime": hwMACApAttackWeakivQuietTime,
       "hwMACApAttackSpoofQuietTime": hwMACApAttackSpoofQuietTime,
       "hwMACApBootCountTotal": hwMACApBootCountTotal,
       "hwMACApBootCountPowerOff": hwMACApBootCountPowerOff,
       "hwMACApBootCountRowStatus": hwMACApBootCountRowStatus,
       "hwMacApLineatePortTable": hwMacApLineatePortTable,
       "hwMacApLineatePortEntry": hwMacApLineatePortEntry,
       "hwMacApLineatePortIndex": hwMacApLineatePortIndex,
       "hwMacApLineatePortType": hwMacApLineatePortType,
       "hwMacApLineatePortDesc": hwMacApLineatePortDesc,
       "hwMacApLineatePortState": hwMacApLineatePortState,
       "hwMacApLineatePortSpeed": hwMacApLineatePortSpeed,
       "hwMacApMultiLineatePortDuplex": hwMacApMultiLineatePortDuplex,
       "hwMacApMultiLineatePortNegotiation": hwMacApMultiLineatePortNegotiation,
       "hwMacApMultiLineatePortMode": hwMacApMultiLineatePortMode,
       "hwMacApMultiLineatePortUserIsolate": hwMacApMultiLineatePortUserIsolate,
       "hwMacApMultiLineatePortStpEnable": hwMacApMultiLineatePortStpEnable,
       "hwMacApMultiLineatePortVlanTagged": hwMacApMultiLineatePortVlanTagged,
       "hwMacApMultiLineatePortVlanUntagged": hwMacApMultiLineatePortVlanUntagged,
       "hwMacApMultiLineatePortPvidVlan": hwMacApMultiLineatePortPvidVlan,
       "hwMacApMultiLineatePortCRCErrorHighThreshold": hwMacApMultiLineatePortCRCErrorHighThreshold,
       "hwMacApMultiLineatePortCRCErrorLowThreshold": hwMacApMultiLineatePortCRCErrorLowThreshold,
       "hwMacApMultiLineatePortCRCErrorSwitch": hwMacApMultiLineatePortCRCErrorSwitch,
       "hwMacApLineatePortAclNumInbound": hwMacApLineatePortAclNumInbound,
       "hwMacApLineatePortAclNumOutbound": hwMacApLineatePortAclNumOutbound,
       "hwMacApLineatePortAclNameInbound": hwMacApLineatePortAclNameInbound,
       "hwMacApLineatePortAclNameOutbound": hwMacApLineatePortAclNameOutbound,
       "hwMacApLineatePortAclSwitchInbound": hwMacApLineatePortAclSwitchInbound,
       "hwMacApLineatePortAclSwitchOutbound": hwMacApLineatePortAclSwitchOutbound,
       "hwMacApLineatePortAclNumInboundIPV6": hwMacApLineatePortAclNumInboundIPV6,
       "hwMacApLineatePortAclNumOutboundIPV6": hwMacApLineatePortAclNumOutboundIPV6,
       "hwMacApLineatePortAclNameInboundIPV6": hwMacApLineatePortAclNameInboundIPV6,
       "hwMacApLineatePortAclNameOutboundIPV6": hwMacApLineatePortAclNameOutboundIPV6,
       "hwMacApLineatePortAclSwitchInboundIPV6": hwMacApLineatePortAclSwitchInboundIPV6,
       "hwMacApLineatePortAclSwitchOutboundIPV6": hwMacApLineatePortAclSwitchOutboundIPV6,
       "hwMacApMultiLineatePortIsAddInTrunk": hwMacApMultiLineatePortIsAddInTrunk,
       "hwMacApMultiLineatePortAddedOrExitTrunkID": hwMacApMultiLineatePortAddedOrExitTrunkID,
       "hwMacApPerformanceStatTable": hwMacApPerformanceStatTable,
       "hwMacApPerformanceStatEntry": hwMacApPerformanceStatEntry,
       "hwMacApMemoryUseRate": hwMacApMemoryUseRate,
       "hwMacApCpuUseRate": hwMacApCpuUseRate,
       "hwMacApFlashFreeSize": hwMacApFlashFreeSize,
       "hwMacApTemperature": hwMacApTemperature,
       "hwMacApOnlineUserNum": hwMacApOnlineUserNum,
       "hwMacApUpPortSpeed": hwMacApUpPortSpeed,
       "hwMacApUpPortRecvFrames": hwMacApUpPortRecvFrames,
       "hwMacApUpPortRecvRightFrames": hwMacApUpPortRecvRightFrames,
       "hwMacApUpPortRecvErrorFrames": hwMacApUpPortRecvErrorFrames,
       "hwMacApUpPortSendFrames": hwMacApUpPortSendFrames,
       "hwMacApUpPortRecvBytes": hwMacApUpPortRecvBytes,
       "hwMacApUpPortSendBytes": hwMacApUpPortSendBytes,
       "hwMacAPUpPortPER": hwMacAPUpPortPER,
       "hwMacAPWirelessUpPortTraffic": hwMacAPWirelessUpPortTraffic,
       "hwMacAPUpPortTraffic": hwMacAPUpPortTraffic,
       "hwMacApAirportSendDropFrames": hwMacApAirportSendDropFrames,
       "hwMacApEthportRecvDropFrames": hwMacApEthportRecvDropFrames,
       "hwMacApAirportUpTraffic": hwMacApAirportUpTraffic,
       "hwMacApAirportDwTraffic": hwMacApAirportDwTraffic,
       "hwMacApEthportDwTraffic": hwMacApEthportDwTraffic,
       "hwMacApEthportUpTraffic": hwMacApEthportUpTraffic,
       "hwMacApAirportRecvDropPacket": hwMacApAirportRecvDropPacket,
       "hwMacApAirportRecvErrorPacket": hwMacApAirportRecvErrorPacket,
       "hwMacApEthportRecvUnicastPacket": hwMacApEthportRecvUnicastPacket,
       "hwMacApEthportRecvNonUnicastPacket": hwMacApEthportRecvNonUnicastPacket,
       "hwMacApEthportSendUnicastPacket": hwMacApEthportSendUnicastPacket,
       "hwMacApEthportSendNonUnicastPacket": hwMacApEthportSendNonUnicastPacket,
       "hwMacApAvgRCPUUseRate": hwMacApAvgRCPUUseRate,
       "hwMacApAvgRMemoryUseRate": hwMacApAvgRMemoryUseRate,
       "hwMacEthportSendDropFrames": hwMacEthportSendDropFrames,
       "hwMacEthportSendErrorFrames": hwMacEthportSendErrorFrames,
       "hwMacEthportUpDwnTimes": hwMacEthportUpDwnTimes,
       "hwMacApAirportRecvUnicastFrames": hwMacApAirportRecvUnicastFrames,
       "hwMacApEthportRecvUnknownFrames": hwMacApEthportRecvUnknownFrames,
       "hwMacEthportUpRate": hwMacEthportUpRate,
       "hwMacEthportDownRate": hwMacEthportDownRate,
       "hwMacApUpPortRecvFrames64Bits": hwMacApUpPortRecvFrames64Bits,
       "hwMacApUpPortRecvRightFrames64Bits": hwMacApUpPortRecvRightFrames64Bits,
       "hwMacApUpPortRecvErrorFrames64Bits": hwMacApUpPortRecvErrorFrames64Bits,
       "hwMacApUpPortSendFrames64Bits": hwMacApUpPortSendFrames64Bits,
       "hwMacApUpPortRecvBytes64Bits": hwMacApUpPortRecvBytes64Bits,
       "hwMacApUpPortSendBytes64Bits": hwMacApUpPortSendBytes64Bits,
       "hwMacAPWirelessUpPortTraffic64Bits": hwMacAPWirelessUpPortTraffic64Bits,
       "hwMacAPUpPortTraffic64Bits": hwMacAPUpPortTraffic64Bits,
       "hwMacApAirportSendDropFrames64Bits": hwMacApAirportSendDropFrames64Bits,
       "hwMacApEthportRecvDropFrames64Bits": hwMacApEthportRecvDropFrames64Bits,
       "hwMacApAirportRecvDropPacket64Bits": hwMacApAirportRecvDropPacket64Bits,
       "hwMacApAirportRecvErrorPacket64Bits": hwMacApAirportRecvErrorPacket64Bits,
       "hwMacApEthportRecvUnicastPacket64Bits": hwMacApEthportRecvUnicastPacket64Bits,
       "hwMacApEthportRecvNonUnicastPacket64Bits": hwMacApEthportRecvNonUnicastPacket64Bits,
       "hwMacApEthportSendUnicastPacket64Bits": hwMacApEthportSendUnicastPacket64Bits,
       "hwMacApEthportSendNonUnicastPacket64Bits": hwMacApEthportSendNonUnicastPacket64Bits,
       "hwApLineportInfoTable": hwApLineportInfoTable,
       "hwApLineportInfoEntry": hwApLineportInfoEntry,
       "hwApLineportIndex": hwApLineportIndex,
       "hwApLineportDesc": hwApLineportDesc,
       "hwApLineportType": hwApLineportType,
       "hwApLineportMtu": hwApLineportMtu,
       "hwApLineportSpeed": hwApLineportSpeed,
       "hwApLineportMac": hwApLineportMac,
       "hwApLineportAdminStatus": hwApLineportAdminStatus,
       "hwApLineportNum": hwApLineportNum,
       "hwMacApLineportInfoTable": hwMacApLineportInfoTable,
       "hwMacApLineportInfoEntry": hwMacApLineportInfoEntry,
       "hwMacApLineportIndex": hwMacApLineportIndex,
       "hwMacApLineportDesc": hwMacApLineportDesc,
       "hwMacApLineportType": hwMacApLineportType,
       "hwMacApLineportMtu": hwMacApLineportMtu,
       "hwMacApLineportSpeed": hwMacApLineportSpeed,
       "hwMacApLineportMac": hwMacApLineportMac,
       "hwMacApLineportAdminStatus": hwMacApLineportAdminStatus,
       "hwMacApLineportNum": hwMacApLineportNum,
       "hwApLldpTable": hwApLldpTable,
       "hwApLldpEntry": hwApLldpEntry,
       "hwApLldpRemLocalPortNum": hwApLldpRemLocalPortNum,
       "hwApLldpRemIndex": hwApLldpRemIndex,
       "hwApLldpRemChassisIdSubtype": hwApLldpRemChassisIdSubtype,
       "hwApLldpRemChassisId": hwApLldpRemChassisId,
       "hwApLldpRemPortIdSubtype": hwApLldpRemPortIdSubtype,
       "hwApLldpRemPortId": hwApLldpRemPortId,
       "hwApLldpRemPortDesc": hwApLldpRemPortDesc,
       "hwApLldpRemSysName": hwApLldpRemSysName,
       "hwApLldpRemSysDesc": hwApLldpRemSysDesc,
       "hwApLldpRemSysCapSupported": hwApLldpRemSysCapSupported,
       "hwApLldpRemSysCapEnabled": hwApLldpRemSysCapEnabled,
       "hwMacApLldpTable": hwMacApLldpTable,
       "hwMacApLldpEntry": hwMacApLldpEntry,
       "hwMacApLldpRemLocalPortNum": hwMacApLldpRemLocalPortNum,
       "hwMacApLldpRemIndex": hwMacApLldpRemIndex,
       "hwMacApLldpRemChassisIdSubtype": hwMacApLldpRemChassisIdSubtype,
       "hwMacApLldpRemChassisId": hwMacApLldpRemChassisId,
       "hwMacApLldpRemPortIdSubtype": hwMacApLldpRemPortIdSubtype,
       "hwMacApLldpRemPortId": hwMacApLldpRemPortId,
       "hwMacApLldpRemPortDesc": hwMacApLldpRemPortDesc,
       "hwMacApLldpRemSysName": hwMacApLldpRemSysName,
       "hwMacApLldpRemSysDesc": hwMacApLldpRemSysDesc,
       "hwMacApLldpRemSysCapSupported": hwMacApLldpRemSysCapSupported,
       "hwMacApLldpRemSysCapEnabled": hwMacApLldpRemSysCapEnabled,
       "hwAplldpRemManAddrTable": hwAplldpRemManAddrTable,
       "hwAplldpRemManAddrEntry": hwAplldpRemManAddrEntry,
       "hwApLldpRemManAddrSubtype": hwApLldpRemManAddrSubtype,
       "hwApLldpRemManAddr": hwApLldpRemManAddr,
       "hwApLldpRemManAddrIfSubtype": hwApLldpRemManAddrIfSubtype,
       "hwApLldpRemManAddrIfId": hwApLldpRemManAddrIfId,
       "hwApLldpRemManAddrOID": hwApLldpRemManAddrOID,
       "hwMacAplldpRemManAddrTable": hwMacAplldpRemManAddrTable,
       "hwMacAplldpRemManAddrEntry": hwMacAplldpRemManAddrEntry,
       "hwMACApLldpRemManAddrSubtype": hwMACApLldpRemManAddrSubtype,
       "hwMACApLldpRemManAddr": hwMACApLldpRemManAddr,
       "hwMACApLldpRemManAddrIfSubtype": hwMACApLldpRemManAddrIfSubtype,
       "hwMACApLldpRemManAddrIfId": hwMACApLldpRemManAddrIfId,
       "hwMACApLldpRemManAddrOID": hwMACApLldpRemManAddrOID,
       "hwApOpticalInfoTable": hwApOpticalInfoTable,
       "hwApOpticalInfoEntry": hwApOpticalInfoEntry,
       "hwApOpticalNominalBitRate": hwApOpticalNominalBitRate,
       "hwApOpticalLinkLen9X125km": hwApOpticalLinkLen9X125km,
       "hwApOpticalLinkLen50X125X100m": hwApOpticalLinkLen50X125X100m,
       "hwApOpticalLinkLen62p5X125X10m": hwApOpticalLinkLen62p5X125X10m,
       "hwApOpticalLinkLenCopper": hwApOpticalLinkLenCopper,
       "hwApOpticalSfpConnector": hwApOpticalSfpConnector,
       "hwApOpticalDdmVoltage": hwApOpticalDdmVoltage,
       "hwApOpticalDdmTxBiasCurrent": hwApOpticalDdmTxBiasCurrent,
       "hwApOpticalDdmTxPower": hwApOpticalDdmTxPower,
       "hwApOpticalDdmRxPower": hwApOpticalDdmRxPower,
       "hwApOpticalDdmTemperature": hwApOpticalDdmTemperature,
       "hwApOpticalVdndorOui": hwApOpticalVdndorOui,
       "hwApOpticalVendorName": hwApOpticalVendorName,
       "hwApOpticalVendorPn": hwApOpticalVendorPn,
       "hwApOpticalVendorRev": hwApOpticalVendorRev,
       "hwApOpticalVendorSn": hwApOpticalVendorSn,
       "hwMacApOpticalInfoTable": hwMacApOpticalInfoTable,
       "hwMacApOpticalInfoEntry": hwMacApOpticalInfoEntry,
       "hwMacApOpticalNominalBitRate": hwMacApOpticalNominalBitRate,
       "hwMacApOpticalLinkLen9X125km": hwMacApOpticalLinkLen9X125km,
       "hwMacApOpticalLinkLen50X125X100m": hwMacApOpticalLinkLen50X125X100m,
       "hwMacApOpticalLinkLen62p5X125X10m": hwMacApOpticalLinkLen62p5X125X10m,
       "hwMacApOpticalLinkLenCopper": hwMacApOpticalLinkLenCopper,
       "hwMacApOpticalSfpConnector": hwMacApOpticalSfpConnector,
       "hwMacApOpticalDdmVoltage": hwMacApOpticalDdmVoltage,
       "hwMacApOpticalDdmTxBiasCurrent": hwMacApOpticalDdmTxBiasCurrent,
       "hwMacApOpticalDdmTxPower": hwMacApOpticalDdmTxPower,
       "hwMacApOpticalDdmRxPower": hwMacApOpticalDdmRxPower,
       "hwMacApOpticalDdmTemperature": hwMacApOpticalDdmTemperature,
       "hwMacApOpticalVdndorOui": hwMacApOpticalVdndorOui,
       "hwMacApOpticalVendorName": hwMacApOpticalVendorName,
       "hwMacApOpticalVendorPn": hwMacApOpticalVendorPn,
       "hwMacApOpticalVendorRev": hwMacApOpticalVendorRev,
       "hwMacApOpticalVendorSn": hwMacApOpticalVendorSn,
       "hwApSysnameTable": hwApSysnameTable,
       "hwApSysnameEntry": hwApSysnameEntry,
       "hwApSysnameApId": hwApSysnameApId,
       "hwApSysnameApMac": hwApSysnameApMac,
       "hwApPhysicalAttrTable": hwApPhysicalAttrTable,
       "hwApPhysicalAttrEntry": hwApPhysicalAttrEntry,
       "hwApElectronicLabel": hwApElectronicLabel,
       "hwMacApPhysicalAttrTable": hwMacApPhysicalAttrTable,
       "hwMacApPhysicalAttrEntry": hwMacApPhysicalAttrEntry,
       "hwMacApElectronicLabel": hwMacApElectronicLabel,
       "hwApLineportStatTable": hwApLineportStatTable,
       "hwApLineportStatEntry": hwApLineportStatEntry,
       "hwApLinePortStatClear": hwApLinePortStatClear,
       "hwApLinePortUpDwnTimes": hwApLinePortUpDwnTimes,
       "hwApLinePortInPkts": hwApLinePortInPkts,
       "hwApLinePortInUnicastPkts": hwApLinePortInUnicastPkts,
       "hwApLinePortInNonUnicastPkts": hwApLinePortInNonUnicastPkts,
       "hwApLinePortInBytes": hwApLinePortInBytes,
       "hwApLinePortInErrorPkts": hwApLinePortInErrorPkts,
       "hwApLinePortInDiscardPkts": hwApLinePortInDiscardPkts,
       "hwApLinePortOutPkts": hwApLinePortOutPkts,
       "hwApLinePortOutUnicastPkts": hwApLinePortOutUnicastPkts,
       "hwApLinePortOutNonUnicastPkts": hwApLinePortOutNonUnicastPkts,
       "hwApLinePortOutBytes": hwApLinePortOutBytes,
       "hwApLinePortOutErrorsPkts": hwApLinePortOutErrorsPkts,
       "hwApLinePortOutDiscardPkts": hwApLinePortOutDiscardPkts,
       "hwMacApLineportStatTable": hwMacApLineportStatTable,
       "hwMacApLineportStatEntry": hwMacApLineportStatEntry,
       "hwMacApLinePortStatClear": hwMacApLinePortStatClear,
       "hwMacApLinePortUpDwnTimes": hwMacApLinePortUpDwnTimes,
       "hwMacApLinePortInPkts": hwMacApLinePortInPkts,
       "hwMacApLinePortInUnicastPkts": hwMacApLinePortInUnicastPkts,
       "hwMacApLinePortInNonUnicastPkts": hwMacApLinePortInNonUnicastPkts,
       "hwMacApLinePortInBytes": hwMacApLinePortInBytes,
       "hwMacApLinePortInErrorPkts": hwMacApLinePortInErrorPkts,
       "hwMacApLinePortInDiscardPkts": hwMacApLinePortInDiscardPkts,
       "hwMacApLinePortOutPkts": hwMacApLinePortOutPkts,
       "hwMacApLinePortOutUnicastPkts": hwMacApLinePortOutUnicastPkts,
       "hwMacApLinePortOutNonUnicastPkts": hwMacApLinePortOutNonUnicastPkts,
       "hwMacApLinePortOutBytes": hwMacApLinePortOutBytes,
       "hwMacApLinePortOutErrorsPkts": hwMacApLinePortOutErrorsPkts,
       "hwMacApLinePortOutDiscardPkts": hwMacApLinePortOutDiscardPkts,
       "hwApLineatePortLldpCfgTable": hwApLineatePortLldpCfgTable,
       "hwApLineatePortLldpCfgEntry": hwApLineatePortLldpCfgEntry,
       "hwApLineatePortLldpIndex": hwApLineatePortLldpIndex,
       "hwApLineatePortLldpEnable": hwApLineatePortLldpEnable,
       "hwApLineatePortLldpManageAddr": hwApLineatePortLldpManageAddr,
       "hwApLineatePortLldpPortDes": hwApLineatePortLldpPortDes,
       "hwApLineatePortLldpSysCab": hwApLineatePortLldpSysCab,
       "hwApLineatePortLldpSysDes": hwApLineatePortLldpSysDes,
       "hwApLineatePortLldpSysName": hwApLineatePortLldpSysName,
       "hwApLineatePortLldpDelay": hwApLineatePortLldpDelay,
       "hwApLineatePortLldpHoldMultiplier": hwApLineatePortLldpHoldMultiplier,
       "hwApLineatePortLldpInterval": hwApLineatePortLldpInterval,
       "hwApLineatePortLldpRestartDelay": hwApLineatePortLldpRestartDelay,
       "hwApLineatePortLldpAdminStatus": hwApLineatePortLldpAdminStatus,
       "hwApLineatePortLldpReportInterval": hwApLineatePortLldpReportInterval,
       "hwMacApLineatePortLldpCfgTable": hwMacApLineatePortLldpCfgTable,
       "hwMacApLineatePortLldpCfgEntry": hwMacApLineatePortLldpCfgEntry,
       "hwMacApLineatePortLldpIndex": hwMacApLineatePortLldpIndex,
       "hwMacApLineatePortLldpEnable": hwMacApLineatePortLldpEnable,
       "hwMacApLineatePortLldpManageAddr": hwMacApLineatePortLldpManageAddr,
       "hwMacApLineatePortLldpPortDes": hwMacApLineatePortLldpPortDes,
       "hwMacApLineatePortLldpSysCab": hwMacApLineatePortLldpSysCab,
       "hwMacApLineatePortLldpSysDes": hwMacApLineatePortLldpSysDes,
       "hwMacApLineatePortLldpSysName": hwMacApLineatePortLldpSysName,
       "hwMacApLineatePortLldpDelay": hwMacApLineatePortLldpDelay,
       "hwMacApLineatePortLldpHoldMultiplier": hwMacApLineatePortLldpHoldMultiplier,
       "hwMacApLineatePortLldpInterval": hwMacApLineatePortLldpInterval,
       "hwMacApLineatePortLldpRestartDelay": hwMacApLineatePortLldpRestartDelay,
       "hwMacApLineatePortLldpAdminStatus": hwMacApLineatePortLldpAdminStatus,
       "hwMacApLineatePortLldpReportInterval": hwMacApLineatePortLldpReportInterval,
       "hwApLineatePortLldpTable": hwApLineatePortLldpTable,
       "hwApLineatePortLldpEntry": hwApLineatePortLldpEntry,
       "hwApLineatePortLldpRemLocalPortNum": hwApLineatePortLldpRemLocalPortNum,
       "hwApLineatePortLldpRemIndex": hwApLineatePortLldpRemIndex,
       "hwApLineatePortLldpRemChassisIdSubtype": hwApLineatePortLldpRemChassisIdSubtype,
       "hwApLineatePortLldpRemChassisId": hwApLineatePortLldpRemChassisId,
       "hwApLineatePortLldpRemPortIdSubtype": hwApLineatePortLldpRemPortIdSubtype,
       "hwApLineatePortLldpRemPortId": hwApLineatePortLldpRemPortId,
       "hwApLineatePortLldpRemPortDesc": hwApLineatePortLldpRemPortDesc,
       "hwApLineatePortLldpRemSysName": hwApLineatePortLldpRemSysName,
       "hwApLineatePortLldpRemSysDesc": hwApLineatePortLldpRemSysDesc,
       "hwApLineatePortLldpRemSysCapSupported": hwApLineatePortLldpRemSysCapSupported,
       "hwApLineatePortLldpRemSysCapEnabled": hwApLineatePortLldpRemSysCapEnabled,
       "hwMacApLineatePortLldpTable": hwMacApLineatePortLldpTable,
       "hwMacApLineatePortLldpEntry": hwMacApLineatePortLldpEntry,
       "hwMacApLineatePortLldpRemLocalPortNum": hwMacApLineatePortLldpRemLocalPortNum,
       "hwMacApLineatePortLldpRemIndex": hwMacApLineatePortLldpRemIndex,
       "hwMacApLineatePortLldpRemChassisIdSubtype": hwMacApLineatePortLldpRemChassisIdSubtype,
       "hwMacApLineatePortLldpRemChassisId": hwMacApLineatePortLldpRemChassisId,
       "hwMacApLineatePortLldpRemPortIdSubtype": hwMacApLineatePortLldpRemPortIdSubtype,
       "hwMacApLineatePortLldpRemPortId": hwMacApLineatePortLldpRemPortId,
       "hwMacApLineatePortLldpRemPortDesc": hwMacApLineatePortLldpRemPortDesc,
       "hwMacApLineatePortLldpRemSysName": hwMacApLineatePortLldpRemSysName,
       "hwMacApLineatePortLldpRemSysDesc": hwMacApLineatePortLldpRemSysDesc,
       "hwMacApLineatePortLldpRemSysCapSupported": hwMacApLineatePortLldpRemSysCapSupported,
       "hwMacApLineatePortLldpRemSysCapEnabled": hwMacApLineatePortLldpRemSysCapEnabled,
       "hwApLineatePortLldpRemManAddrTable": hwApLineatePortLldpRemManAddrTable,
       "hwApLineatePortLldpRemManAddrEntry": hwApLineatePortLldpRemManAddrEntry,
       "hwApLineatePortLldpRemManAddrSubtype": hwApLineatePortLldpRemManAddrSubtype,
       "hwApLineatePortLldpRemManAddr": hwApLineatePortLldpRemManAddr,
       "hwApLineatePortLldpRemManAddrIfSubtype": hwApLineatePortLldpRemManAddrIfSubtype,
       "hwApLineatePortLldpRemManAddrIfId": hwApLineatePortLldpRemManAddrIfId,
       "hwApLineatePortLldpRemManAddrOID": hwApLineatePortLldpRemManAddrOID,
       "hwMacApLineatePortLldpRemManAddrTable": hwMacApLineatePortLldpRemManAddrTable,
       "hwMacApLineatePortLldpRemManAddrEntry": hwMacApLineatePortLldpRemManAddrEntry,
       "hwMACApLineatePortLldpRemManAddrSubtype": hwMACApLineatePortLldpRemManAddrSubtype,
       "hwMACApLineatePortLldpRemManAddr": hwMACApLineatePortLldpRemManAddr,
       "hwMACApLineatePortLldpRemManAddrIfSubtype": hwMACApLineatePortLldpRemManAddrIfSubtype,
       "hwMACApLineatePortLldpRemManAddrIfId": hwMACApLineatePortLldpRemManAddrIfId,
       "hwMACApLineatePortLldpRemManAddrOID": hwMACApLineatePortLldpRemManAddrOID,
       "hwApOnlineFailTable": hwApOnlineFailTable,
       "hwApOnlineFailEntry": hwApOnlineFailEntry,
       "hwApOnlineFailMac": hwApOnlineFailMac,
       "hwMacApOnlineFailTime": hwMacApOnlineFailTime,
       "hwMacApOnlineFailReason": hwMacApOnlineFailReason,
       "hwMacApOnlineFailRowStatus": hwMacApOnlineFailRowStatus,
       "hwApOfflineTable": hwApOfflineTable,
       "hwApOfflineEntry": hwApOfflineEntry,
       "hwApOfflineMac": hwApOfflineMac,
       "hwMacApOfflineTime": hwMacApOfflineTime,
       "hwMacApOfflineReason": hwMacApOfflineReason,
       "hwMacApOfflineRowStatus": hwMacApOfflineRowStatus,
       "hwAcObjects": hwAcObjects,
       "hwAcTable": hwAcTable,
       "hwAcEntry": hwAcEntry,
       "hwMemAcIndex": hwMemAcIndex,
       "hwAcIpVersion": hwAcIpVersion,
       "hwAcIPv4Address": hwAcIPv4Address,
       "hwAcIPv6Address": hwAcIPv6Address,
       "hwAcState": hwAcState,
       "hwAcRowStatus": hwAcRowStatus,
       "hwMobilityGroupTable": hwMobilityGroupTable,
       "hwMobilityGroupEntry": hwMobilityGroupEntry,
       "hwMobilityGroupName": hwMobilityGroupName,
       "hwMobilityGroupMemberList": hwMobilityGroupMemberList,
       "hwMobilityGroupStatus": hwMobilityGroupStatus,
       "hwMobilityGroupMemberOpcode": hwMobilityGroupMemberOpcode,
       "hwMobilityGroupMemberIndex": hwMobilityGroupMemberIndex,
       "hwWlanDeviceObjects": hwWlanDeviceObjects,
       "hwWlanDeviceConformance": hwWlanDeviceConformance,
       "hwWlanDeviceCompliances": hwWlanDeviceCompliances,
       "hwWlanDeviceCompliance": hwWlanDeviceCompliance,
       "hwWlanDeviceObjectGroups": hwWlanDeviceObjectGroups,
       "hwWlanDeviceNotifyGroup": hwWlanDeviceNotifyGroup,
       "hwWlanDeviceNotifyObjectsGroup": hwWlanDeviceNotifyObjectsGroup,
       "hwApTypeGroup": hwApTypeGroup,
       "hwApProfileGroup": hwApProfileGroup,
       "hwApAuthListGroup": hwApAuthListGroup,
       "hwApRegionGroup": hwApRegionGroup,
       "hwApGroup": hwApGroup,
       "hwAcGroup": hwAcGroup}
)
