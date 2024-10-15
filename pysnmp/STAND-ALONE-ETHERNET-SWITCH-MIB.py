# SNMP MIB module (STAND-ALONE-ETHERNET-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STAND-ALONE-ETHERNET-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:52 2024
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

(Timeout,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "Timeout")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Grandjunction_ObjectIdentity = ObjectIdentity
grandjunction = _Grandjunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1)
)
_FastLink_ObjectIdentity = ObjectIdentity
fastLink = _FastLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1)
)
_SeriesG2xx_ObjectIdentity = ObjectIdentity
seriesG2xx = _SeriesG2xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2)
)
_EsModuleBasic_ObjectIdentity = ObjectIdentity
esModuleBasic = _EsModuleBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 2, 1)
)
_Series2000_ObjectIdentity = ObjectIdentity
series2000 = _Series2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1)
)
_SysInfoFwdEngineRevision_Type = Integer32
_SysInfoFwdEngineRevision_Object = MibScalar
sysInfoFwdEngineRevision = _SysInfoFwdEngineRevision_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 1),
    _SysInfoFwdEngineRevision_Type()
)
sysInfoFwdEngineRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoFwdEngineRevision.setStatus("mandatory")
_SysInfoBoardRevision_Type = Integer32
_SysInfoBoardRevision_Object = MibScalar
sysInfoBoardRevision = _SysInfoBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 2),
    _SysInfoBoardRevision_Type()
)
sysInfoBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoBoardRevision.setStatus("mandatory")
_SysInfoTotalNumberOfPorts_Type = Integer32
_SysInfoTotalNumberOfPorts_Object = MibScalar
sysInfoTotalNumberOfPorts = _SysInfoTotalNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 3),
    _SysInfoTotalNumberOfPorts_Type()
)
sysInfoTotalNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoTotalNumberOfPorts.setStatus("mandatory")
_SysInfoNumberOfSwitchPorts_Type = Integer32
_SysInfoNumberOfSwitchPorts_Object = MibScalar
sysInfoNumberOfSwitchPorts = _SysInfoNumberOfSwitchPorts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 4),
    _SysInfoNumberOfSwitchPorts_Type()
)
sysInfoNumberOfSwitchPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoNumberOfSwitchPorts.setStatus("mandatory")
_SysInfoNumberOfSharedPorts_Type = Integer32
_SysInfoNumberOfSharedPorts_Object = MibScalar
sysInfoNumberOfSharedPorts = _SysInfoNumberOfSharedPorts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 5),
    _SysInfoNumberOfSharedPorts_Type()
)
sysInfoNumberOfSharedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoNumberOfSharedPorts.setStatus("mandatory")
_SysInfoNumberOfInstalledModules_Type = Counter32
_SysInfoNumberOfInstalledModules_Object = MibScalar
sysInfoNumberOfInstalledModules = _SysInfoNumberOfInstalledModules_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 6),
    _SysInfoNumberOfInstalledModules_Type()
)
sysInfoNumberOfInstalledModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoNumberOfInstalledModules.setStatus("mandatory")
_SysInfoBuffersUsed_Type = Gauge32
_SysInfoBuffersUsed_Object = MibScalar
sysInfoBuffersUsed = _SysInfoBuffersUsed_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 7),
    _SysInfoBuffersUsed_Type()
)
sysInfoBuffersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoBuffersUsed.setStatus("mandatory")
_SysInfoMaxBuffers_Type = Counter32
_SysInfoMaxBuffers_Object = MibScalar
sysInfoMaxBuffers = _SysInfoMaxBuffers_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 8),
    _SysInfoMaxBuffers_Type()
)
sysInfoMaxBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoMaxBuffers.setStatus("mandatory")


class _SysInfoUtilDisplay_Type(Integer32):
    """Custom type sysInfoUtilDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_SysInfoUtilDisplay_Type.__name__ = "Integer32"
_SysInfoUtilDisplay_Object = MibScalar
sysInfoUtilDisplay = _SysInfoUtilDisplay_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 9),
    _SysInfoUtilDisplay_Type()
)
sysInfoUtilDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoUtilDisplay.setStatus("mandatory")
_SysInfoAddrCapacity_Type = Integer32
_SysInfoAddrCapacity_Object = MibScalar
sysInfoAddrCapacity = _SysInfoAddrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 10),
    _SysInfoAddrCapacity_Type()
)
sysInfoAddrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoAddrCapacity.setStatus("mandatory")
_SysInfoRestrictedStaticAddrCapacity_Type = Integer32
_SysInfoRestrictedStaticAddrCapacity_Object = MibScalar
sysInfoRestrictedStaticAddrCapacity = _SysInfoRestrictedStaticAddrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 11),
    _SysInfoRestrictedStaticAddrCapacity_Type()
)
sysInfoRestrictedStaticAddrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoRestrictedStaticAddrCapacity.setStatus("mandatory")
_SysInfoPOSTResult_Type = Integer32
_SysInfoPOSTResult_Object = MibScalar
sysInfoPOSTResult = _SysInfoPOSTResult_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 12),
    _SysInfoPOSTResult_Type()
)
sysInfoPOSTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoPOSTResult.setStatus("mandatory")
_SysInfoPortFailedPOSTMap_Type = OctetString
_SysInfoPortFailedPOSTMap_Object = MibScalar
sysInfoPortFailedPOSTMap = _SysInfoPortFailedPOSTMap_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 13),
    _SysInfoPortFailedPOSTMap_Type()
)
sysInfoPortFailedPOSTMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoPortFailedPOSTMap.setStatus("mandatory")
_SysInfoPortLinkDisplayMap_Type = OctetString
_SysInfoPortLinkDisplayMap_Object = MibScalar
sysInfoPortLinkDisplayMap = _SysInfoPortLinkDisplayMap_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 14),
    _SysInfoPortLinkDisplayMap_Type()
)
sysInfoPortLinkDisplayMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoPortLinkDisplayMap.setStatus("mandatory")
_SysInfoPortDisabledDisplayMap_Type = OctetString
_SysInfoPortDisabledDisplayMap_Object = MibScalar
sysInfoPortDisabledDisplayMap = _SysInfoPortDisabledDisplayMap_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 15),
    _SysInfoPortDisabledDisplayMap_Type()
)
sysInfoPortDisabledDisplayMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoPortDisabledDisplayMap.setStatus("mandatory")
_SysInfoBroadcastStormLastTime_Type = TimeTicks
_SysInfoBroadcastStormLastTime_Object = MibScalar
sysInfoBroadcastStormLastTime = _SysInfoBroadcastStormLastTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 16),
    _SysInfoBroadcastStormLastTime_Type()
)
sysInfoBroadcastStormLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoBroadcastStormLastTime.setStatus("mandatory")


class _SysInfoPortExceedBroadcastStorm_Type(Integer32):
    """Custom type sysInfoPortExceedBroadcastStorm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 27),
    )


_SysInfoPortExceedBroadcastStorm_Type.__name__ = "Integer32"
_SysInfoPortExceedBroadcastStorm_Object = MibScalar
sysInfoPortExceedBroadcastStorm = _SysInfoPortExceedBroadcastStorm_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 17),
    _SysInfoPortExceedBroadcastStorm_Type()
)
sysInfoPortExceedBroadcastStorm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoPortExceedBroadcastStorm.setStatus("mandatory")


class _SysInfoRedundantPowerState_Type(Integer32):
    """Custom type sysInfoRedundantPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("healthy", 2),
          ("off", 1))
    )


_SysInfoRedundantPowerState_Type.__name__ = "Integer32"
_SysInfoRedundantPowerState_Object = MibScalar
sysInfoRedundantPowerState = _SysInfoRedundantPowerState_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 18),
    _SysInfoRedundantPowerState_Type()
)
sysInfoRedundantPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoRedundantPowerState.setStatus("mandatory")


class _SysInfoInternalPowerState_Type(Integer32):
    """Custom type sysInfoInternalPowerState based on Integer32"""
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


_SysInfoInternalPowerState_Type.__name__ = "Integer32"
_SysInfoInternalPowerState_Object = MibScalar
sysInfoInternalPowerState = _SysInfoInternalPowerState_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 19),
    _SysInfoInternalPowerState_Type()
)
sysInfoInternalPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoInternalPowerState.setStatus("mandatory")


class _SysInfoConfigFileStatus_Type(DisplayString):
    """Custom type sysInfoConfigFileStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SysInfoConfigFileStatus_Type.__name__ = "DisplayString"
_SysInfoConfigFileStatus_Object = MibScalar
sysInfoConfigFileStatus = _SysInfoConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 20),
    _SysInfoConfigFileStatus_Type()
)
sysInfoConfigFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoConfigFileStatus.setStatus("mandatory")


class _SysInfoImageCapability_Type(Integer32):
    """Custom type sysInfoImageCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enterprise", 2),
          ("standard", 1))
    )


_SysInfoImageCapability_Type.__name__ = "Integer32"
_SysInfoImageCapability_Object = MibScalar
sysInfoImageCapability = _SysInfoImageCapability_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 1, 21),
    _SysInfoImageCapability_Type()
)
sysInfoImageCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInfoImageCapability.setStatus("mandatory")
_SysConfig_ObjectIdentity = ObjectIdentity
sysConfig = _SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2)
)


class _SysConfigReset_Type(Integer32):
    """Custom type sysConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_SysConfigReset_Type.__name__ = "Integer32"
_SysConfigReset_Object = MibScalar
sysConfigReset = _SysConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 1),
    _SysConfigReset_Type()
)
sysConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigReset.setStatus("mandatory")


class _SysConfigDefaultReset_Type(Integer32):
    """Custom type sysConfigDefaultReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_SysConfigDefaultReset_Type.__name__ = "Integer32"
_SysConfigDefaultReset_Object = MibScalar
sysConfigDefaultReset = _SysConfigDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 2),
    _SysConfigDefaultReset_Type()
)
sysConfigDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigDefaultReset.setStatus("mandatory")


class _SysConfigClearPortStats_Type(Integer32):
    """Custom type sysConfigClearPortStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noClear", 1))
    )


_SysConfigClearPortStats_Type.__name__ = "Integer32"
_SysConfigClearPortStats_Object = MibScalar
sysConfigClearPortStats = _SysConfigClearPortStats_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 3),
    _SysConfigClearPortStats_Type()
)
sysConfigClearPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigClearPortStats.setStatus("mandatory")


class _SysConfigAddressViolationAction_Type(Integer32):
    """Custom type sysConfigAddressViolationAction based on Integer32"""
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
          ("ignore", 3),
          ("suspend", 1))
    )


_SysConfigAddressViolationAction_Type.__name__ = "Integer32"
_SysConfigAddressViolationAction_Object = MibScalar
sysConfigAddressViolationAction = _SysConfigAddressViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 4),
    _SysConfigAddressViolationAction_Type()
)
sysConfigAddressViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigAddressViolationAction.setStatus("mandatory")


class _SysConfigAddressViolationAlert_Type(Integer32):
    """Custom type sysConfigAddressViolationAlert based on Integer32"""
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


_SysConfigAddressViolationAlert_Type.__name__ = "Integer32"
_SysConfigAddressViolationAlert_Object = MibScalar
sysConfigAddressViolationAlert = _SysConfigAddressViolationAlert_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 5),
    _SysConfigAddressViolationAlert_Type()
)
sysConfigAddressViolationAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigAddressViolationAlert.setStatus("mandatory")


class _SysConfigSwitchingMode_Type(Integer32):
    """Custom type sysConfigSwitchingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fastForward", 3),
          ("fragmentFree", 2),
          ("store-and-forward", 1))
    )


_SysConfigSwitchingMode_Type.__name__ = "Integer32"
_SysConfigSwitchingMode_Object = MibScalar
sysConfigSwitchingMode = _SysConfigSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 6),
    _SysConfigSwitchingMode_Type()
)
sysConfigSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigSwitchingMode.setStatus("mandatory")


class _SysConfigMulticastStoreAndForward_Type(Integer32):
    """Custom type sysConfigMulticastStoreAndForward based on Integer32"""
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


_SysConfigMulticastStoreAndForward_Type.__name__ = "Integer32"
_SysConfigMulticastStoreAndForward_Object = MibScalar
sysConfigMulticastStoreAndForward = _SysConfigMulticastStoreAndForward_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 7),
    _SysConfigMulticastStoreAndForward_Type()
)
sysConfigMulticastStoreAndForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigMulticastStoreAndForward.setStatus("mandatory")


class _SysConfigMonitor_Type(Integer32):
    """Custom type sysConfigMonitor based on Integer32"""
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


_SysConfigMonitor_Type.__name__ = "Integer32"
_SysConfigMonitor_Object = MibScalar
sysConfigMonitor = _SysConfigMonitor_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 8),
    _SysConfigMonitor_Type()
)
sysConfigMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigMonitor.setStatus("mandatory")


class _SysConfigMonitorPort_Type(Integer32):
    """Custom type sysConfigMonitorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SysConfigMonitorPort_Type.__name__ = "Integer32"
_SysConfigMonitorPort_Object = MibScalar
sysConfigMonitorPort = _SysConfigMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 9),
    _SysConfigMonitorPort_Type()
)
sysConfigMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigMonitorPort.setStatus("mandatory")


class _SysConfigHigherProtocolMonitor_Type(Integer32):
    """Custom type sysConfigHigherProtocolMonitor based on Integer32"""
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


_SysConfigHigherProtocolMonitor_Type.__name__ = "Integer32"
_SysConfigHigherProtocolMonitor_Object = MibScalar
sysConfigHigherProtocolMonitor = _SysConfigHigherProtocolMonitor_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 10),
    _SysConfigHigherProtocolMonitor_Type()
)
sysConfigHigherProtocolMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigHigherProtocolMonitor.setStatus("obsolete")


class _SysConfigPort25Connector_Type(Integer32):
    """Custom type sysConfigPort25Connector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aui", 4),
          ("rj45", 2),
          ("self-sensing", 1))
    )


_SysConfigPort25Connector_Type.__name__ = "Integer32"
_SysConfigPort25Connector_Object = MibScalar
sysConfigPort25Connector = _SysConfigPort25Connector_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 11),
    _SysConfigPort25Connector_Type()
)
sysConfigPort25Connector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigPort25Connector.setStatus("mandatory")
_SysConfigHeuristics_Type = Integer32
_SysConfigHeuristics_Object = MibScalar
sysConfigHeuristics = _SysConfigHeuristics_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 12),
    _SysConfigHeuristics_Type()
)
sysConfigHeuristics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigHeuristics.setStatus("mandatory")


class _SysConfigEnableSTP_Type(Integer32):
    """Custom type sysConfigEnableSTP based on Integer32"""
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


_SysConfigEnableSTP_Type.__name__ = "Integer32"
_SysConfigEnableSTP_Object = MibScalar
sysConfigEnableSTP = _SysConfigEnableSTP_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 13),
    _SysConfigEnableSTP_Type()
)
sysConfigEnableSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigEnableSTP.setStatus("mandatory")


class _SysConfigStrictSTPTransition_Type(Integer32):
    """Custom type sysConfigStrictSTPTransition based on Integer32"""
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


_SysConfigStrictSTPTransition_Type.__name__ = "Integer32"
_SysConfigStrictSTPTransition_Object = MibScalar
sysConfigStrictSTPTransition = _SysConfigStrictSTPTransition_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 14),
    _SysConfigStrictSTPTransition_Type()
)
sysConfigStrictSTPTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigStrictSTPTransition.setStatus("deprecated")


class _SysConfigBroadcastStormAction_Type(Integer32):
    """Custom type sysConfigBroadcastStormAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("ignore", 2))
    )


_SysConfigBroadcastStormAction_Type.__name__ = "Integer32"
_SysConfigBroadcastStormAction_Object = MibScalar
sysConfigBroadcastStormAction = _SysConfigBroadcastStormAction_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 15),
    _SysConfigBroadcastStormAction_Type()
)
sysConfigBroadcastStormAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigBroadcastStormAction.setStatus("mandatory")


class _SysConfigBroadcastStormAlert_Type(Integer32):
    """Custom type sysConfigBroadcastStormAlert based on Integer32"""
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


_SysConfigBroadcastStormAlert_Type.__name__ = "Integer32"
_SysConfigBroadcastStormAlert_Object = MibScalar
sysConfigBroadcastStormAlert = _SysConfigBroadcastStormAlert_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 16),
    _SysConfigBroadcastStormAlert_Type()
)
sysConfigBroadcastStormAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigBroadcastStormAlert.setStatus("mandatory")


class _SysConfigBroadcastThreshold_Type(Integer32):
    """Custom type sysConfigBroadcastThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 14400),
    )


_SysConfigBroadcastThreshold_Type.__name__ = "Integer32"
_SysConfigBroadcastThreshold_Object = MibScalar
sysConfigBroadcastThreshold = _SysConfigBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 17),
    _SysConfigBroadcastThreshold_Type()
)
sysConfigBroadcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigBroadcastThreshold.setStatus("mandatory")


class _SysConfigBroadcastReEnableThreshold_Type(Integer32):
    """Custom type sysConfigBroadcastReEnableThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 14400),
    )


_SysConfigBroadcastReEnableThreshold_Type.__name__ = "Integer32"
_SysConfigBroadcastReEnableThreshold_Object = MibScalar
sysConfigBroadcastReEnableThreshold = _SysConfigBroadcastReEnableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 18),
    _SysConfigBroadcastReEnableThreshold_Type()
)
sysConfigBroadcastReEnableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigBroadcastReEnableThreshold.setStatus("mandatory")


class _SysConfig10MbpsEnhancedCongestionControl_Type(Integer32):
    """Custom type sysConfig10MbpsEnhancedCongestionControl based on Integer32"""
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
        *(("adaptive", 1),
          ("aggressive", 4),
          ("disabled", 2),
          ("moderate-aggressive", 3))
    )


_SysConfig10MbpsEnhancedCongestionControl_Type.__name__ = "Integer32"
_SysConfig10MbpsEnhancedCongestionControl_Object = MibScalar
sysConfig10MbpsEnhancedCongestionControl = _SysConfig10MbpsEnhancedCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 19),
    _SysConfig10MbpsEnhancedCongestionControl_Type()
)
sysConfig10MbpsEnhancedCongestionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfig10MbpsEnhancedCongestionControl.setStatus("mandatory")


class _SysConfigNetworkPort_Type(Integer32):
    """Custom type sysConfigNetworkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 27),
    )


_SysConfigNetworkPort_Type.__name__ = "Integer32"
_SysConfigNetworkPort_Object = MibScalar
sysConfigNetworkPort = _SysConfigNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 20),
    _SysConfigNetworkPort_Type()
)
sysConfigNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigNetworkPort.setStatus("mandatory")


class _SysConfigHalfDuplexBackPressure_Type(Integer32):
    """Custom type sysConfigHalfDuplexBackPressure based on Integer32"""
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


_SysConfigHalfDuplexBackPressure_Type.__name__ = "Integer32"
_SysConfigHalfDuplexBackPressure_Object = MibScalar
sysConfigHalfDuplexBackPressure = _SysConfigHalfDuplexBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 21),
    _SysConfigHalfDuplexBackPressure_Type()
)
sysConfigHalfDuplexBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigHalfDuplexBackPressure.setStatus("mandatory")


class _SysConfigFastEthcParmsPort_Type(Integer32):
    """Custom type sysConfigFastEthcParmsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(26, 27),
    )


_SysConfigFastEthcParmsPort_Type.__name__ = "Integer32"
_SysConfigFastEthcParmsPort_Object = MibScalar
sysConfigFastEthcParmsPort = _SysConfigFastEthcParmsPort_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 22),
    _SysConfigFastEthcParmsPort_Type()
)
sysConfigFastEthcParmsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigFastEthcParmsPort.setStatus("mandatory")


class _SysConfigTftpServerName_Type(DisplayString):
    """Custom type sysConfigTftpServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysConfigTftpServerName_Type.__name__ = "DisplayString"
_SysConfigTftpServerName_Object = MibScalar
sysConfigTftpServerName = _SysConfigTftpServerName_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 23),
    _SysConfigTftpServerName_Type()
)
sysConfigTftpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigTftpServerName.setStatus("mandatory")


class _SysConfigConfigFileAuto_Type(Integer32):
    """Custom type sysConfigConfigFileAuto based on Integer32"""
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


_SysConfigConfigFileAuto_Type.__name__ = "Integer32"
_SysConfigConfigFileAuto_Object = MibScalar
sysConfigConfigFileAuto = _SysConfigConfigFileAuto_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 24),
    _SysConfigConfigFileAuto_Type()
)
sysConfigConfigFileAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigConfigFileAuto.setStatus("mandatory")


class _SysConfigPortGroupingMode_Type(Integer32):
    """Custom type sysConfigPortGroupingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge-group", 1),
          ("vlan", 2))
    )


_SysConfigPortGroupingMode_Type.__name__ = "Integer32"
_SysConfigPortGroupingMode_Object = MibScalar
sysConfigPortGroupingMode = _SysConfigPortGroupingMode_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 2, 25),
    _SysConfigPortGroupingMode_Type()
)
sysConfigPortGroupingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigPortGroupingMode.setStatus("mandatory")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3)
)
_SwitchPortTable_Object = MibTable
switchPortTable = _SwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    switchPortTable.setStatus("mandatory")
_SwPortEntry_Object = MibTableRow
swPortEntry = _SwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1)
)
swPortEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "swPortIndex"),
)
if mibBuilder.loadTexts:
    swPortEntry.setStatus("mandatory")
_SwPortIndex_Type = Integer32
_SwPortIndex_Object = MibTableColumn
swPortIndex = _SwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 1),
    _SwPortIndex_Type()
)
swPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortIndex.setStatus("mandatory")
_SwPortControllerRevision_Type = Integer32
_SwPortControllerRevision_Object = MibTableColumn
swPortControllerRevision = _SwPortControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 2),
    _SwPortControllerRevision_Type()
)
swPortControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortControllerRevision.setStatus("mandatory")


class _SwPortName_Type(DisplayString):
    """Custom type swPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_SwPortName_Type.__name__ = "DisplayString"
_SwPortName_Object = MibTableColumn
swPortName = _SwPortName_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 3),
    _SwPortName_Type()
)
swPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortName.setStatus("mandatory")


class _SwPortMediaCapability_Type(Integer32):
    """Custom type swPortMediaCapability based on Integer32"""
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
        *(("atm", 8),
          ("fddi", 7),
          ("general-ethernet", 3),
          ("general-fast-ethernet", 4),
          ("other", 1),
          ("private-ethernet", 2),
          ("private-fast-ethernet", 5),
          ("repeated-fast-ethernet", 6))
    )


_SwPortMediaCapability_Type.__name__ = "Integer32"
_SwPortMediaCapability_Object = MibTableColumn
swPortMediaCapability = _SwPortMediaCapability_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 4),
    _SwPortMediaCapability_Type()
)
swPortMediaCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMediaCapability.setStatus("mandatory")


class _SwPortType_Type(Integer32):
    """Custom type swPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("other", 1))
    )


_SwPortType_Type.__name__ = "Integer32"
_SwPortType_Object = MibTableColumn
swPortType = _SwPortType_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 5),
    _SwPortType_Type()
)
swPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortType.setStatus("mandatory")


class _SwPortConnectorType_Type(Integer32):
    """Custom type swPortConnectorType based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("aui", 4),
          ("bnc", 3),
          ("empty", 7),
          ("fddi-mic", 10),
          ("fiber-mtrj", 11),
          ("fiber-sc", 5),
          ("fiber-st", 6),
          ("group", 8),
          ("other", 1),
          ("rj45", 2))
    )


_SwPortConnectorType_Type.__name__ = "Integer32"
_SwPortConnectorType_Object = MibTableColumn
swPortConnectorType = _SwPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 6),
    _SwPortConnectorType_Type()
)
swPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortConnectorType.setStatus("mandatory")


class _SwPortACR_Type(Integer32):
    """Custom type swPortACR based on Integer32"""
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


_SwPortACR_Type.__name__ = "Integer32"
_SwPortACR_Object = MibTableColumn
swPortACR = _SwPortACR_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 7),
    _SwPortACR_Type()
)
swPortACR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortACR.setStatus("deprecated")


class _SwPortFullDuplex_Type(Integer32):
    """Custom type swPortFullDuplex based on Integer32"""
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
        *(("auto-negotiate", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("enabled-flow-control", 4))
    )


_SwPortFullDuplex_Type.__name__ = "Integer32"
_SwPortFullDuplex_Object = MibTableColumn
swPortFullDuplex = _SwPortFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 8),
    _SwPortFullDuplex_Type()
)
swPortFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortFullDuplex.setStatus("mandatory")


class _SwPortStatus_Type(Integer32):
    """Custom type swPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("disabled-mgmt", 2),
          ("disabled-no-vlan", 18),
          ("disabled-self-test", 14),
          ("disabled-violation", 7),
          ("enable-degraded", 15),
          ("enabled", 1),
          ("reset", 11),
          ("suspended-atm-lane-down", 16),
          ("suspended-atm-network-down", 19),
          ("suspended-disl", 20),
          ("suspended-jabber", 4),
          ("suspended-linkbeat", 3),
          ("suspended-no-vlan", 17),
          ("suspended-not-present", 9),
          ("suspended-not-recognized", 10),
          ("suspended-ringdown", 12),
          ("suspended-stp", 13),
          ("suspended-violation", 5))
    )


_SwPortStatus_Type.__name__ = "Integer32"
_SwPortStatus_Object = MibTableColumn
swPortStatus = _SwPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 9),
    _SwPortStatus_Type()
)
swPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatus.setStatus("mandatory")


class _SwPortAdminStatus_Type(Integer32):
    """Custom type swPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled-mgmt", 2),
          ("enabled", 1))
    )


_SwPortAdminStatus_Type.__name__ = "Integer32"
_SwPortAdminStatus_Object = MibTableColumn
swPortAdminStatus = _SwPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 10),
    _SwPortAdminStatus_Type()
)
swPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortAdminStatus.setStatus("mandatory")


class _SwPortLastStatus_Type(Integer32):
    """Custom type swPortLastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("disabled-mgmt", 2),
          ("disabled-no-vlan", 18),
          ("disabled-self-test", 14),
          ("disabled-violation", 7),
          ("enable-degraded", 15),
          ("enabled", 1),
          ("reset", 11),
          ("suspended-atm-lane-down", 16),
          ("suspended-atm-network-down", 19),
          ("suspended-disl", 20),
          ("suspended-jabber", 4),
          ("suspended-linkbeat", 3),
          ("suspended-no-vlan", 17),
          ("suspended-not-present", 9),
          ("suspended-not-recognized", 10),
          ("suspended-ringdown", 12),
          ("suspended-stp", 13),
          ("suspended-violation", 5))
    )


_SwPortLastStatus_Type.__name__ = "Integer32"
_SwPortLastStatus_Object = MibTableColumn
swPortLastStatus = _SwPortLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 11),
    _SwPortLastStatus_Type()
)
swPortLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortLastStatus.setStatus("mandatory")
_SwPortStatusChanges_Type = Counter32
_SwPortStatusChanges_Object = MibTableColumn
swPortStatusChanges = _SwPortStatusChanges_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 12),
    _SwPortStatusChanges_Type()
)
swPortStatusChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatusChanges.setStatus("mandatory")


class _SwPortAddressingSecurity_Type(Integer32):
    """Custom type swPortAddressingSecurity based on Integer32"""
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


_SwPortAddressingSecurity_Type.__name__ = "Integer32"
_SwPortAddressingSecurity_Object = MibTableColumn
swPortAddressingSecurity = _SwPortAddressingSecurity_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 13),
    _SwPortAddressingSecurity_Type()
)
swPortAddressingSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortAddressingSecurity.setStatus("mandatory")


class _SwPortAddressTableSize_Type(Integer32):
    """Custom type swPortAddressTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 132),
    )


_SwPortAddressTableSize_Type.__name__ = "Integer32"
_SwPortAddressTableSize_Object = MibTableColumn
swPortAddressTableSize = _SwPortAddressTableSize_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 14),
    _SwPortAddressTableSize_Type()
)
swPortAddressTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortAddressTableSize.setStatus("mandatory")
_SwPortNumberOfLearnedAddresses_Type = Integer32
_SwPortNumberOfLearnedAddresses_Object = MibTableColumn
swPortNumberOfLearnedAddresses = _SwPortNumberOfLearnedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 15),
    _SwPortNumberOfLearnedAddresses_Type()
)
swPortNumberOfLearnedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumberOfLearnedAddresses.setStatus("mandatory")
_SwPortNumberOfStaticAddresses_Type = Integer32
_SwPortNumberOfStaticAddresses_Object = MibTableColumn
swPortNumberOfStaticAddresses = _SwPortNumberOfStaticAddresses_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 16),
    _SwPortNumberOfStaticAddresses_Type()
)
swPortNumberOfStaticAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumberOfStaticAddresses.setStatus("mandatory")


class _SwPortEraseAddresses_Type(Integer32):
    """Custom type swPortEraseAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erase", 2),
          ("noErase", 1))
    )


_SwPortEraseAddresses_Type.__name__ = "Integer32"
_SwPortEraseAddresses_Object = MibTableColumn
swPortEraseAddresses = _SwPortEraseAddresses_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 17),
    _SwPortEraseAddresses_Type()
)
swPortEraseAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortEraseAddresses.setStatus("mandatory")


class _SwPortFloodUnregisteredMulticasts_Type(Integer32):
    """Custom type swPortFloodUnregisteredMulticasts based on Integer32"""
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


_SwPortFloodUnregisteredMulticasts_Type.__name__ = "Integer32"
_SwPortFloodUnregisteredMulticasts_Object = MibTableColumn
swPortFloodUnregisteredMulticasts = _SwPortFloodUnregisteredMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 18),
    _SwPortFloodUnregisteredMulticasts_Type()
)
swPortFloodUnregisteredMulticasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortFloodUnregisteredMulticasts.setStatus("mandatory")


class _SwPortFloodUnknownUnicasts_Type(Integer32):
    """Custom type swPortFloodUnknownUnicasts based on Integer32"""
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


_SwPortFloodUnknownUnicasts_Type.__name__ = "Integer32"
_SwPortFloodUnknownUnicasts_Object = MibTableColumn
swPortFloodUnknownUnicasts = _SwPortFloodUnknownUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 19),
    _SwPortFloodUnknownUnicasts_Type()
)
swPortFloodUnknownUnicasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortFloodUnknownUnicasts.setStatus("mandatory")


class _SwPortMonitoring_Type(Integer32):
    """Custom type swPortMonitoring based on Integer32"""
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


_SwPortMonitoring_Type.__name__ = "Integer32"
_SwPortMonitoring_Object = MibTableColumn
swPortMonitoring = _SwPortMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 20),
    _SwPortMonitoring_Type()
)
swPortMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMonitoring.setStatus("mandatory")
_SwPortSecuredAddressViolations_Type = Counter32
_SwPortSecuredAddressViolations_Object = MibTableColumn
swPortSecuredAddressViolations = _SwPortSecuredAddressViolations_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 21),
    _SwPortSecuredAddressViolations_Type()
)
swPortSecuredAddressViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortSecuredAddressViolations.setStatus("mandatory")


class _SwPortLinkbeatStatus_Type(Integer32):
    """Custom type swPortLinkbeatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkbeat", 1),
          ("noLinkbeat", 2))
    )


_SwPortLinkbeatStatus_Type.__name__ = "Integer32"
_SwPortLinkbeatStatus_Object = MibTableColumn
swPortLinkbeatStatus = _SwPortLinkbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 22),
    _SwPortLinkbeatStatus_Type()
)
swPortLinkbeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortLinkbeatStatus.setStatus("mandatory")
_SwPortLinkbeatLosses_Type = Counter32
_SwPortLinkbeatLosses_Object = MibTableColumn
swPortLinkbeatLosses = _SwPortLinkbeatLosses_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 23),
    _SwPortLinkbeatLosses_Type()
)
swPortLinkbeatLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortLinkbeatLosses.setStatus("mandatory")


class _SwPortJabberStatus_Type(Integer32):
    """Custom type swPortJabberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jabbering", 2),
          ("notJabbering", 1))
    )


_SwPortJabberStatus_Type.__name__ = "Integer32"
_SwPortJabberStatus_Object = MibTableColumn
swPortJabberStatus = _SwPortJabberStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 24),
    _SwPortJabberStatus_Type()
)
swPortJabberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortJabberStatus.setStatus("mandatory")
_SwPortJabbers_Type = Counter32
_SwPortJabbers_Object = MibTableColumn
swPortJabbers = _SwPortJabbers_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 25),
    _SwPortJabbers_Type()
)
swPortJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortJabbers.setStatus("mandatory")


class _SwPortClearStatistics_Type(Integer32):
    """Custom type swPortClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noClear", 1))
    )


_SwPortClearStatistics_Type.__name__ = "Integer32"
_SwPortClearStatistics_Object = MibTableColumn
swPortClearStatistics = _SwPortClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 26),
    _SwPortClearStatistics_Type()
)
swPortClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortClearStatistics.setStatus("mandatory")


class _SwPortBroadcastStormBlocked_Type(Integer32):
    """Custom type swPortBroadcastStormBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("notBlocked", 1))
    )


_SwPortBroadcastStormBlocked_Type.__name__ = "Integer32"
_SwPortBroadcastStormBlocked_Object = MibTableColumn
swPortBroadcastStormBlocked = _SwPortBroadcastStormBlocked_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 27),
    _SwPortBroadcastStormBlocked_Type()
)
swPortBroadcastStormBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBroadcastStormBlocked.setStatus("mandatory")


class _SwPortSTPPortFastMode_Type(Integer32):
    """Custom type swPortSTPPortFastMode based on Integer32"""
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


_SwPortSTPPortFastMode_Type.__name__ = "Integer32"
_SwPortSTPPortFastMode_Object = MibTableColumn
swPortSTPPortFastMode = _SwPortSTPPortFastMode_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 28),
    _SwPortSTPPortFastMode_Type()
)
swPortSTPPortFastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortSTPPortFastMode.setStatus("mandatory")


class _SwPortHalfDuplexBackPressure_Type(Integer32):
    """Custom type swPortHalfDuplexBackPressure based on Integer32"""
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


_SwPortHalfDuplexBackPressure_Type.__name__ = "Integer32"
_SwPortHalfDuplexBackPressure_Object = MibTableColumn
swPortHalfDuplexBackPressure = _SwPortHalfDuplexBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 29),
    _SwPortHalfDuplexBackPressure_Type()
)
swPortHalfDuplexBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortHalfDuplexBackPressure.setStatus("obsolete")


class _SwPortDuplexStatus_Type(Integer32):
    """Custom type swPortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("full-duplex-flow-control", 3),
          ("half-duplex", 2))
    )


_SwPortDuplexStatus_Type.__name__ = "Integer32"
_SwPortDuplexStatus_Object = MibTableColumn
swPortDuplexStatus = _SwPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 30),
    _SwPortDuplexStatus_Type()
)
swPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortDuplexStatus.setStatus("mandatory")


class _SwPortFullDuplexFlowControl_Type(Integer32):
    """Custom type swPortFullDuplexFlowControl based on Integer32"""
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


_SwPortFullDuplexFlowControl_Type.__name__ = "Integer32"
_SwPortFullDuplexFlowControl_Object = MibTableColumn
swPortFullDuplexFlowControl = _SwPortFullDuplexFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 31),
    _SwPortFullDuplexFlowControl_Type()
)
swPortFullDuplexFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortFullDuplexFlowControl.setStatus("obsolete")


class _SwPortEnhancedCongestionControl_Type(Integer32):
    """Custom type swPortEnhancedCongestionControl based on Integer32"""
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
        *(("adaptive", 1),
          ("aggressive", 4),
          ("disabled", 2),
          ("moderate-aggressive", 3))
    )


_SwPortEnhancedCongestionControl_Type.__name__ = "Integer32"
_SwPortEnhancedCongestionControl_Object = MibTableColumn
swPortEnhancedCongestionControl = _SwPortEnhancedCongestionControl_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 32),
    _SwPortEnhancedCongestionControl_Type()
)
swPortEnhancedCongestionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortEnhancedCongestionControl.setStatus("mandatory")
_SwPortBridgePriority_Type = Integer32
_SwPortBridgePriority_Object = MibTableColumn
swPortBridgePriority = _SwPortBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 33),
    _SwPortBridgePriority_Type()
)
swPortBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBridgePriority.setStatus("mandatory")
_SwPortBridgePriorityAlternate_Type = Integer32
_SwPortBridgePriorityAlternate_Object = MibTableColumn
swPortBridgePriorityAlternate = _SwPortBridgePriorityAlternate_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 34),
    _SwPortBridgePriorityAlternate_Type()
)
swPortBridgePriorityAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBridgePriorityAlternate.setStatus("mandatory")
_SwPortBridgePathCost_Type = Integer32
_SwPortBridgePathCost_Object = MibTableColumn
swPortBridgePathCost = _SwPortBridgePathCost_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 35),
    _SwPortBridgePathCost_Type()
)
swPortBridgePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBridgePathCost.setStatus("mandatory")
_SwPortBridgePathCostAlternate_Type = Integer32
_SwPortBridgePathCostAlternate_Object = MibTableColumn
swPortBridgePathCostAlternate = _SwPortBridgePathCostAlternate_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 36),
    _SwPortBridgePathCostAlternate_Type()
)
swPortBridgePathCostAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBridgePathCostAlternate.setStatus("mandatory")
_SwPortIfIndex_Type = Integer32
_SwPortIfIndex_Object = MibTableColumn
swPortIfIndex = _SwPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 37),
    _SwPortIfIndex_Type()
)
swPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortIfIndex.setStatus("mandatory")


class _SwPortInternal_Type(Integer32):
    """Custom type swPortInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SwPortInternal_Type.__name__ = "Integer32"
_SwPortInternal_Object = MibTableColumn
swPortInternal = _SwPortInternal_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 1, 1, 38),
    _SwPortInternal_Type()
)
swPortInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInternal.setStatus("mandatory")
_SwitchPortRxStatTable_Object = MibTable
switchPortRxStatTable = _SwitchPortRxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    switchPortRxStatTable.setStatus("mandatory")
_SwPortRxStatEntry_Object = MibTableRow
swPortRxStatEntry = _SwPortRxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1)
)
swPortRxStatEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "swPortRxStatIndex"),
)
if mibBuilder.loadTexts:
    swPortRxStatEntry.setStatus("mandatory")
_SwPortRxStatIndex_Type = Integer32
_SwPortRxStatIndex_Object = MibTableColumn
swPortRxStatIndex = _SwPortRxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 1),
    _SwPortRxStatIndex_Type()
)
swPortRxStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxStatIndex.setStatus("mandatory")
_SwPortRxTotalFrames_Type = Counter32
_SwPortRxTotalFrames_Object = MibTableColumn
swPortRxTotalFrames = _SwPortRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 2),
    _SwPortRxTotalFrames_Type()
)
swPortRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxTotalFrames.setStatus("mandatory")
_SwPortRxTotalOctets_Type = Counter32
_SwPortRxTotalOctets_Object = MibTableColumn
swPortRxTotalOctets = _SwPortRxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 3),
    _SwPortRxTotalOctets_Type()
)
swPortRxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxTotalOctets.setStatus("mandatory")
_SwPortRxTotalOctetsWraps_Type = Counter32
_SwPortRxTotalOctetsWraps_Object = MibTableColumn
swPortRxTotalOctetsWraps = _SwPortRxTotalOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 4),
    _SwPortRxTotalOctetsWraps_Type()
)
swPortRxTotalOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxTotalOctetsWraps.setStatus("mandatory")
_SwPortRxUnicastFrames_Type = Counter32
_SwPortRxUnicastFrames_Object = MibTableColumn
swPortRxUnicastFrames = _SwPortRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 5),
    _SwPortRxUnicastFrames_Type()
)
swPortRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxUnicastFrames.setStatus("mandatory")
_SwPortRxUnicastOctets_Type = Counter32
_SwPortRxUnicastOctets_Object = MibTableColumn
swPortRxUnicastOctets = _SwPortRxUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 6),
    _SwPortRxUnicastOctets_Type()
)
swPortRxUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxUnicastOctets.setStatus("mandatory")
_SwPortRxUnicastOctetsWraps_Type = Counter32
_SwPortRxUnicastOctetsWraps_Object = MibTableColumn
swPortRxUnicastOctetsWraps = _SwPortRxUnicastOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 7),
    _SwPortRxUnicastOctetsWraps_Type()
)
swPortRxUnicastOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxUnicastOctetsWraps.setStatus("mandatory")
_SwPortRxBroadcastFrames_Type = Counter32
_SwPortRxBroadcastFrames_Object = MibTableColumn
swPortRxBroadcastFrames = _SwPortRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 8),
    _SwPortRxBroadcastFrames_Type()
)
swPortRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxBroadcastFrames.setStatus("mandatory")
_SwPortRxBroadcastOctets_Type = Counter32
_SwPortRxBroadcastOctets_Object = MibTableColumn
swPortRxBroadcastOctets = _SwPortRxBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 9),
    _SwPortRxBroadcastOctets_Type()
)
swPortRxBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxBroadcastOctets.setStatus("mandatory")
_SwPortRxBroadcastOctetsWraps_Type = Counter32
_SwPortRxBroadcastOctetsWraps_Object = MibTableColumn
swPortRxBroadcastOctetsWraps = _SwPortRxBroadcastOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 10),
    _SwPortRxBroadcastOctetsWraps_Type()
)
swPortRxBroadcastOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxBroadcastOctetsWraps.setStatus("mandatory")
_SwPortRxMulticastFrames_Type = Counter32
_SwPortRxMulticastFrames_Object = MibTableColumn
swPortRxMulticastFrames = _SwPortRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 11),
    _SwPortRxMulticastFrames_Type()
)
swPortRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxMulticastFrames.setStatus("mandatory")
_SwPortRxMulticastOctets_Type = Counter32
_SwPortRxMulticastOctets_Object = MibTableColumn
swPortRxMulticastOctets = _SwPortRxMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 12),
    _SwPortRxMulticastOctets_Type()
)
swPortRxMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxMulticastOctets.setStatus("mandatory")
_SwPortRxMulticastOctetsWraps_Type = Counter32
_SwPortRxMulticastOctetsWraps_Object = MibTableColumn
swPortRxMulticastOctetsWraps = _SwPortRxMulticastOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 13),
    _SwPortRxMulticastOctetsWraps_Type()
)
swPortRxMulticastOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxMulticastOctetsWraps.setStatus("mandatory")
_SwPortRxForwardedFrames_Type = Counter32
_SwPortRxForwardedFrames_Object = MibTableColumn
swPortRxForwardedFrames = _SwPortRxForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 14),
    _SwPortRxForwardedFrames_Type()
)
swPortRxForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxForwardedFrames.setStatus("mandatory")
_SwPortRxFilteredFrames_Type = Counter32
_SwPortRxFilteredFrames_Object = MibTableColumn
swPortRxFilteredFrames = _SwPortRxFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 15),
    _SwPortRxFilteredFrames_Type()
)
swPortRxFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxFilteredFrames.setStatus("mandatory")
_SwPortRxNoBufferDiscards_Type = Counter32
_SwPortRxNoBufferDiscards_Object = MibTableColumn
swPortRxNoBufferDiscards = _SwPortRxNoBufferDiscards_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 16),
    _SwPortRxNoBufferDiscards_Type()
)
swPortRxNoBufferDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxNoBufferDiscards.setStatus("mandatory")
_SwPortRxFCSErrors_Type = Counter32
_SwPortRxFCSErrors_Object = MibTableColumn
swPortRxFCSErrors = _SwPortRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 17),
    _SwPortRxFCSErrors_Type()
)
swPortRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxFCSErrors.setStatus("mandatory")
_SwPortRxAlignmentErrors_Type = Counter32
_SwPortRxAlignmentErrors_Object = MibTableColumn
swPortRxAlignmentErrors = _SwPortRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 18),
    _SwPortRxAlignmentErrors_Type()
)
swPortRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxAlignmentErrors.setStatus("mandatory")
_SwPortRxFrameTooLongs_Type = Counter32
_SwPortRxFrameTooLongs_Object = MibTableColumn
swPortRxFrameTooLongs = _SwPortRxFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 19),
    _SwPortRxFrameTooLongs_Type()
)
swPortRxFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxFrameTooLongs.setStatus("mandatory")
_SwPortRxRunts_Type = Counter32
_SwPortRxRunts_Object = MibTableColumn
swPortRxRunts = _SwPortRxRunts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 2, 1, 20),
    _SwPortRxRunts_Type()
)
swPortRxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortRxRunts.setStatus("mandatory")
_SwitchPortTxStatTable_Object = MibTable
switchPortTxStatTable = _SwitchPortTxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    switchPortTxStatTable.setStatus("mandatory")
_SwPortTxStatEntry_Object = MibTableRow
swPortTxStatEntry = _SwPortTxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1)
)
swPortTxStatEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "swPortTxStatIndex"),
)
if mibBuilder.loadTexts:
    swPortTxStatEntry.setStatus("mandatory")
_SwPortTxStatIndex_Type = Integer32
_SwPortTxStatIndex_Object = MibTableColumn
swPortTxStatIndex = _SwPortTxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 1),
    _SwPortTxStatIndex_Type()
)
swPortTxStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxStatIndex.setStatus("mandatory")
_SwPortTxTotalFrames_Type = Counter32
_SwPortTxTotalFrames_Object = MibTableColumn
swPortTxTotalFrames = _SwPortTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 2),
    _SwPortTxTotalFrames_Type()
)
swPortTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxTotalFrames.setStatus("mandatory")
_SwPortTxTotalOctets_Type = Counter32
_SwPortTxTotalOctets_Object = MibTableColumn
swPortTxTotalOctets = _SwPortTxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 3),
    _SwPortTxTotalOctets_Type()
)
swPortTxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxTotalOctets.setStatus("mandatory")
_SwPortTxTotalOctetsWraps_Type = Counter32
_SwPortTxTotalOctetsWraps_Object = MibTableColumn
swPortTxTotalOctetsWraps = _SwPortTxTotalOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 4),
    _SwPortTxTotalOctetsWraps_Type()
)
swPortTxTotalOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxTotalOctetsWraps.setStatus("mandatory")
_SwPortTxUnicastFrames_Type = Counter32
_SwPortTxUnicastFrames_Object = MibTableColumn
swPortTxUnicastFrames = _SwPortTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 5),
    _SwPortTxUnicastFrames_Type()
)
swPortTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxUnicastFrames.setStatus("mandatory")
_SwPortTxUnicastOctets_Type = Counter32
_SwPortTxUnicastOctets_Object = MibTableColumn
swPortTxUnicastOctets = _SwPortTxUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 6),
    _SwPortTxUnicastOctets_Type()
)
swPortTxUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxUnicastOctets.setStatus("mandatory")
_SwPortTxUnicastOctetsWraps_Type = Counter32
_SwPortTxUnicastOctetsWraps_Object = MibTableColumn
swPortTxUnicastOctetsWraps = _SwPortTxUnicastOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 7),
    _SwPortTxUnicastOctetsWraps_Type()
)
swPortTxUnicastOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxUnicastOctetsWraps.setStatus("mandatory")
_SwPortTxBroadcastFrames_Type = Counter32
_SwPortTxBroadcastFrames_Object = MibTableColumn
swPortTxBroadcastFrames = _SwPortTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 8),
    _SwPortTxBroadcastFrames_Type()
)
swPortTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxBroadcastFrames.setStatus("mandatory")
_SwPortTxBroadcastOctets_Type = Counter32
_SwPortTxBroadcastOctets_Object = MibTableColumn
swPortTxBroadcastOctets = _SwPortTxBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 9),
    _SwPortTxBroadcastOctets_Type()
)
swPortTxBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxBroadcastOctets.setStatus("mandatory")
_SwPortTxBroadcastOctetsWraps_Type = Counter32
_SwPortTxBroadcastOctetsWraps_Object = MibTableColumn
swPortTxBroadcastOctetsWraps = _SwPortTxBroadcastOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 10),
    _SwPortTxBroadcastOctetsWraps_Type()
)
swPortTxBroadcastOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxBroadcastOctetsWraps.setStatus("mandatory")
_SwPortTxMulticastFrames_Type = Counter32
_SwPortTxMulticastFrames_Object = MibTableColumn
swPortTxMulticastFrames = _SwPortTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 11),
    _SwPortTxMulticastFrames_Type()
)
swPortTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxMulticastFrames.setStatus("mandatory")
_SwPortTxMulticastOctets_Type = Counter32
_SwPortTxMulticastOctets_Object = MibTableColumn
swPortTxMulticastOctets = _SwPortTxMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 12),
    _SwPortTxMulticastOctets_Type()
)
swPortTxMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxMulticastOctets.setStatus("mandatory")
_SwPortTxMulticastOctetsWraps_Type = Counter32
_SwPortTxMulticastOctetsWraps_Object = MibTableColumn
swPortTxMulticastOctetsWraps = _SwPortTxMulticastOctetsWraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 13),
    _SwPortTxMulticastOctetsWraps_Type()
)
swPortTxMulticastOctetsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxMulticastOctetsWraps.setStatus("mandatory")
_SwPortTxDeferrals_Type = Counter32
_SwPortTxDeferrals_Object = MibTableColumn
swPortTxDeferrals = _SwPortTxDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 14),
    _SwPortTxDeferrals_Type()
)
swPortTxDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxDeferrals.setStatus("mandatory")
_SwPortTxSingleCollisions_Type = Counter32
_SwPortTxSingleCollisions_Object = MibTableColumn
swPortTxSingleCollisions = _SwPortTxSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 15),
    _SwPortTxSingleCollisions_Type()
)
swPortTxSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxSingleCollisions.setStatus("mandatory")
_SwPortTxMultipleCollisions_Type = Counter32
_SwPortTxMultipleCollisions_Object = MibTableColumn
swPortTxMultipleCollisions = _SwPortTxMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 16),
    _SwPortTxMultipleCollisions_Type()
)
swPortTxMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxMultipleCollisions.setStatus("mandatory")
_SwPortTxLateCollisions_Type = Counter32
_SwPortTxLateCollisions_Object = MibTableColumn
swPortTxLateCollisions = _SwPortTxLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 17),
    _SwPortTxLateCollisions_Type()
)
swPortTxLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxLateCollisions.setStatus("mandatory")
_SwPortTxExcessiveCollisions_Type = Counter32
_SwPortTxExcessiveCollisions_Object = MibTableColumn
swPortTxExcessiveCollisions = _SwPortTxExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 18),
    _SwPortTxExcessiveCollisions_Type()
)
swPortTxExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxExcessiveCollisions.setStatus("mandatory")
_SwPortTxExcessiveDeferrals_Type = Counter32
_SwPortTxExcessiveDeferrals_Object = MibTableColumn
swPortTxExcessiveDeferrals = _SwPortTxExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 19),
    _SwPortTxExcessiveDeferrals_Type()
)
swPortTxExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxExcessiveDeferrals.setStatus("mandatory")
_SwPortTxExcessiveCollision16s_Type = Counter32
_SwPortTxExcessiveCollision16s_Object = MibTableColumn
swPortTxExcessiveCollision16s = _SwPortTxExcessiveCollision16s_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 20),
    _SwPortTxExcessiveCollision16s_Type()
)
swPortTxExcessiveCollision16s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxExcessiveCollision16s.setStatus("mandatory")
_SwPortTxExcessiveCollision4s_Type = Counter32
_SwPortTxExcessiveCollision4s_Object = MibTableColumn
swPortTxExcessiveCollision4s = _SwPortTxExcessiveCollision4s_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 21),
    _SwPortTxExcessiveCollision4s_Type()
)
swPortTxExcessiveCollision4s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxExcessiveCollision4s.setStatus("mandatory")
_SwPortTxQueueFullDiscards_Type = Counter32
_SwPortTxQueueFullDiscards_Object = MibTableColumn
swPortTxQueueFullDiscards = _SwPortTxQueueFullDiscards_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 22),
    _SwPortTxQueueFullDiscards_Type()
)
swPortTxQueueFullDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxQueueFullDiscards.setStatus("mandatory")
_SwPortTxErrors_Type = Counter32
_SwPortTxErrors_Object = MibTableColumn
swPortTxErrors = _SwPortTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 3, 1, 23),
    _SwPortTxErrors_Type()
)
swPortTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxErrors.setStatus("mandatory")
_SwitchPortTxCollTable_Object = MibTable
switchPortTxCollTable = _SwitchPortTxCollTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    switchPortTxCollTable.setStatus("mandatory")
_SwPortTxCollEntry_Object = MibTableRow
swPortTxCollEntry = _SwPortTxCollEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 4, 1)
)
swPortTxCollEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "swPortTxCollIndex"),
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "swPortTxCollCount"),
)
if mibBuilder.loadTexts:
    swPortTxCollEntry.setStatus("mandatory")
_SwPortTxCollIndex_Type = Integer32
_SwPortTxCollIndex_Object = MibTableColumn
swPortTxCollIndex = _SwPortTxCollIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 4, 1, 1),
    _SwPortTxCollIndex_Type()
)
swPortTxCollIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxCollIndex.setStatus("mandatory")


class _SwPortTxCollCount_Type(Integer32):
    """Custom type swPortTxCollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SwPortTxCollCount_Type.__name__ = "Integer32"
_SwPortTxCollCount_Object = MibTableColumn
swPortTxCollCount = _SwPortTxCollCount_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 4, 1, 2),
    _SwPortTxCollCount_Type()
)
swPortTxCollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxCollCount.setStatus("mandatory")
_SwPortTxCollFrequencies_Type = Counter32
_SwPortTxCollFrequencies_Object = MibTableColumn
swPortTxCollFrequencies = _SwPortTxCollFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 3, 4, 1, 3),
    _SwPortTxCollFrequencies_Type()
)
swPortTxCollFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTxCollFrequencies.setStatus("mandatory")
_NetMgmt_ObjectIdentity = ObjectIdentity
netMgmt = _NetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4)
)
_NetMgmtIpAddress_Type = IpAddress
_NetMgmtIpAddress_Object = MibScalar
netMgmtIpAddress = _NetMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 1),
    _NetMgmtIpAddress_Type()
)
netMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtIpAddress.setStatus("mandatory")
_NetMgmtIpSubnetMask_Type = IpAddress
_NetMgmtIpSubnetMask_Object = MibScalar
netMgmtIpSubnetMask = _NetMgmtIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 2),
    _NetMgmtIpSubnetMask_Type()
)
netMgmtIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtIpSubnetMask.setStatus("mandatory")
_NetMgmtDefaultGateway_Type = IpAddress
_NetMgmtDefaultGateway_Object = MibScalar
netMgmtDefaultGateway = _NetMgmtDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 3),
    _NetMgmtDefaultGateway_Type()
)
netMgmtDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtDefaultGateway.setStatus("mandatory")


class _NetMgmtEnableAuthenTraps_Type(Integer32):
    """Custom type netMgmtEnableAuthenTraps based on Integer32"""
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


_NetMgmtEnableAuthenTraps_Type.__name__ = "Integer32"
_NetMgmtEnableAuthenTraps_Object = MibScalar
netMgmtEnableAuthenTraps = _NetMgmtEnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 4),
    _NetMgmtEnableAuthenTraps_Type()
)
netMgmtEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtEnableAuthenTraps.setStatus("mandatory")


class _NetMgmtEnableLinkTraps_Type(Integer32):
    """Custom type netMgmtEnableLinkTraps based on Integer32"""
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


_NetMgmtEnableLinkTraps_Type.__name__ = "Integer32"
_NetMgmtEnableLinkTraps_Object = MibScalar
netMgmtEnableLinkTraps = _NetMgmtEnableLinkTraps_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 5),
    _NetMgmtEnableLinkTraps_Type()
)
netMgmtEnableLinkTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtEnableLinkTraps.setStatus("mandatory")


class _NetMgmtConsoleInactTime_Type(Integer32):
    """Custom type netMgmtConsoleInactTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_NetMgmtConsoleInactTime_Type.__name__ = "Integer32"
_NetMgmtConsoleInactTime_Object = MibScalar
netMgmtConsoleInactTime = _NetMgmtConsoleInactTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 6),
    _NetMgmtConsoleInactTime_Type()
)
netMgmtConsoleInactTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtConsoleInactTime.setStatus("mandatory")


class _NetMgmtConsolePasswordThresh_Type(Integer32):
    """Custom type netMgmtConsolePasswordThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_NetMgmtConsolePasswordThresh_Type.__name__ = "Integer32"
_NetMgmtConsolePasswordThresh_Object = MibScalar
netMgmtConsolePasswordThresh = _NetMgmtConsolePasswordThresh_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 7),
    _NetMgmtConsolePasswordThresh_Type()
)
netMgmtConsolePasswordThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtConsolePasswordThresh.setStatus("mandatory")


class _NetMgmtConsoleSilentTime_Type(Integer32):
    """Custom type netMgmtConsoleSilentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_NetMgmtConsoleSilentTime_Type.__name__ = "Integer32"
_NetMgmtConsoleSilentTime_Object = MibScalar
netMgmtConsoleSilentTime = _NetMgmtConsoleSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 8),
    _NetMgmtConsoleSilentTime_Type()
)
netMgmtConsoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtConsoleSilentTime.setStatus("mandatory")


class _NetMgmtModemInitString_Type(DisplayString):
    """Custom type netMgmtModemInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NetMgmtModemInitString_Type.__name__ = "DisplayString"
_NetMgmtModemInitString_Object = MibScalar
netMgmtModemInitString = _NetMgmtModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 9),
    _NetMgmtModemInitString_Type()
)
netMgmtModemInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtModemInitString.setStatus("mandatory")


class _NetMgmtModemDialString_Type(DisplayString):
    """Custom type netMgmtModemDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NetMgmtModemDialString_Type.__name__ = "DisplayString"
_NetMgmtModemDialString_Object = MibScalar
netMgmtModemDialString = _NetMgmtModemDialString_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 10),
    _NetMgmtModemDialString_Type()
)
netMgmtModemDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtModemDialString.setStatus("mandatory")


class _NetMgmtModemDialDelay_Type(Integer32):
    """Custom type netMgmtModemDialDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_NetMgmtModemDialDelay_Type.__name__ = "Integer32"
_NetMgmtModemDialDelay_Object = MibScalar
netMgmtModemDialDelay = _NetMgmtModemDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 11),
    _NetMgmtModemDialDelay_Type()
)
netMgmtModemDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtModemDialDelay.setStatus("mandatory")


class _NetMgmtModemAutoAnswer_Type(Integer32):
    """Custom type netMgmtModemAutoAnswer based on Integer32"""
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


_NetMgmtModemAutoAnswer_Type.__name__ = "Integer32"
_NetMgmtModemAutoAnswer_Object = MibScalar
netMgmtModemAutoAnswer = _NetMgmtModemAutoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 12),
    _NetMgmtModemAutoAnswer_Type()
)
netMgmtModemAutoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtModemAutoAnswer.setStatus("mandatory")
_NetMgmtSetClientTable_Object = MibTable
netMgmtSetClientTable = _NetMgmtSetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 13)
)
if mibBuilder.loadTexts:
    netMgmtSetClientTable.setStatus("mandatory")
_NetMgmtSetClientEntry_Object = MibTableRow
netMgmtSetClientEntry = _NetMgmtSetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 13, 1)
)
netMgmtSetClientEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "netMgmtSetClientIndex"),
)
if mibBuilder.loadTexts:
    netMgmtSetClientEntry.setStatus("mandatory")


class _NetMgmtSetClientIndex_Type(Integer32):
    """Custom type netMgmtSetClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NetMgmtSetClientIndex_Type.__name__ = "Integer32"
_NetMgmtSetClientIndex_Object = MibTableColumn
netMgmtSetClientIndex = _NetMgmtSetClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 13, 1, 1),
    _NetMgmtSetClientIndex_Type()
)
netMgmtSetClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMgmtSetClientIndex.setStatus("mandatory")
_NetMgmtSetClientAddr_Type = IpAddress
_NetMgmtSetClientAddr_Object = MibTableColumn
netMgmtSetClientAddr = _NetMgmtSetClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 13, 1, 2),
    _NetMgmtSetClientAddr_Type()
)
netMgmtSetClientAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtSetClientAddr.setStatus("mandatory")


class _NetMgmtSetClientStatus_Type(Integer32):
    """Custom type netMgmtSetClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_NetMgmtSetClientStatus_Type.__name__ = "Integer32"
_NetMgmtSetClientStatus_Object = MibTableColumn
netMgmtSetClientStatus = _NetMgmtSetClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 13, 1, 3),
    _NetMgmtSetClientStatus_Type()
)
netMgmtSetClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtSetClientStatus.setStatus("mandatory")


class _NetMgmtSetClientName_Type(DisplayString):
    """Custom type netMgmtSetClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NetMgmtSetClientName_Type.__name__ = "DisplayString"
_NetMgmtSetClientName_Object = MibTableColumn
netMgmtSetClientName = _NetMgmtSetClientName_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 13, 1, 4),
    _NetMgmtSetClientName_Type()
)
netMgmtSetClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtSetClientName.setStatus("mandatory")
_NetMgmtTrapClientTable_Object = MibTable
netMgmtTrapClientTable = _NetMgmtTrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 14)
)
if mibBuilder.loadTexts:
    netMgmtTrapClientTable.setStatus("mandatory")
_NetMgmtTrapClientEntry_Object = MibTableRow
netMgmtTrapClientEntry = _NetMgmtTrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 14, 1)
)
netMgmtTrapClientEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "netMgmtTrapClientIndex"),
)
if mibBuilder.loadTexts:
    netMgmtTrapClientEntry.setStatus("mandatory")


class _NetMgmtTrapClientIndex_Type(Integer32):
    """Custom type netMgmtTrapClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NetMgmtTrapClientIndex_Type.__name__ = "Integer32"
_NetMgmtTrapClientIndex_Object = MibTableColumn
netMgmtTrapClientIndex = _NetMgmtTrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 14, 1, 1),
    _NetMgmtTrapClientIndex_Type()
)
netMgmtTrapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMgmtTrapClientIndex.setStatus("mandatory")
_NetMgmtTrapClientAddr_Type = IpAddress
_NetMgmtTrapClientAddr_Object = MibTableColumn
netMgmtTrapClientAddr = _NetMgmtTrapClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 14, 1, 2),
    _NetMgmtTrapClientAddr_Type()
)
netMgmtTrapClientAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtTrapClientAddr.setStatus("mandatory")


class _NetMgmtTrapClientComm_Type(DisplayString):
    """Custom type netMgmtTrapClientComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NetMgmtTrapClientComm_Type.__name__ = "DisplayString"
_NetMgmtTrapClientComm_Object = MibTableColumn
netMgmtTrapClientComm = _NetMgmtTrapClientComm_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 14, 1, 3),
    _NetMgmtTrapClientComm_Type()
)
netMgmtTrapClientComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtTrapClientComm.setStatus("mandatory")


class _NetMgmtTrapClientStatus_Type(Integer32):
    """Custom type netMgmtTrapClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_NetMgmtTrapClientStatus_Type.__name__ = "Integer32"
_NetMgmtTrapClientStatus_Object = MibTableColumn
netMgmtTrapClientStatus = _NetMgmtTrapClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 14, 1, 4),
    _NetMgmtTrapClientStatus_Type()
)
netMgmtTrapClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtTrapClientStatus.setStatus("mandatory")


class _NetMgmtTrapClientName_Type(DisplayString):
    """Custom type netMgmtTrapClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NetMgmtTrapClientName_Type.__name__ = "DisplayString"
_NetMgmtTrapClientName_Object = MibTableColumn
netMgmtTrapClientName = _NetMgmtTrapClientName_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 14, 1, 5),
    _NetMgmtTrapClientName_Type()
)
netMgmtTrapClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtTrapClientName.setStatus("mandatory")


class _NetMgmtCdpHoldTime_Type(Integer32):
    """Custom type netMgmtCdpHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_NetMgmtCdpHoldTime_Type.__name__ = "Integer32"
_NetMgmtCdpHoldTime_Object = MibScalar
netMgmtCdpHoldTime = _NetMgmtCdpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 15),
    _NetMgmtCdpHoldTime_Type()
)
netMgmtCdpHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtCdpHoldTime.setStatus("mandatory")


class _NetMgmtCdpTransmissionTime_Type(Integer32):
    """Custom type netMgmtCdpTransmissionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_NetMgmtCdpTransmissionTime_Type.__name__ = "Integer32"
_NetMgmtCdpTransmissionTime_Object = MibScalar
netMgmtCdpTransmissionTime = _NetMgmtCdpTransmissionTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 16),
    _NetMgmtCdpTransmissionTime_Type()
)
netMgmtCdpTransmissionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtCdpTransmissionTime.setStatus("mandatory")


class _NetMgmtCgmpEnable_Type(Integer32):
    """Custom type netMgmtCgmpEnable based on Integer32"""
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


_NetMgmtCgmpEnable_Type.__name__ = "Integer32"
_NetMgmtCgmpEnable_Object = MibScalar
netMgmtCgmpEnable = _NetMgmtCgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 17),
    _NetMgmtCgmpEnable_Type()
)
netMgmtCgmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtCgmpEnable.setStatus("mandatory")


class _NetMgmtCgmpRouterHoldTime_Type(Integer32):
    """Custom type netMgmtCgmpRouterHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_NetMgmtCgmpRouterHoldTime_Type.__name__ = "Integer32"
_NetMgmtCgmpRouterHoldTime_Object = MibScalar
netMgmtCgmpRouterHoldTime = _NetMgmtCgmpRouterHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 18),
    _NetMgmtCgmpRouterHoldTime_Type()
)
netMgmtCgmpRouterHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtCgmpRouterHoldTime.setStatus("mandatory")


class _NetMgmtVlan_Type(Integer32):
    """Custom type netMgmtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_NetMgmtVlan_Type.__name__ = "Integer32"
_NetMgmtVlan_Object = MibScalar
netMgmtVlan = _NetMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 19),
    _NetMgmtVlan_Type()
)
netMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtVlan.setStatus("mandatory")


class _NetMgmtEnableRIP_Type(Integer32):
    """Custom type netMgmtEnableRIP based on Integer32"""
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


_NetMgmtEnableRIP_Type.__name__ = "Integer32"
_NetMgmtEnableRIP_Object = MibScalar
netMgmtEnableRIP = _NetMgmtEnableRIP_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 20),
    _NetMgmtEnableRIP_Type()
)
netMgmtEnableRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtEnableRIP.setStatus("mandatory")
_NetMgmtDomainServer1IpAddress_Type = IpAddress
_NetMgmtDomainServer1IpAddress_Object = MibScalar
netMgmtDomainServer1IpAddress = _NetMgmtDomainServer1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 21),
    _NetMgmtDomainServer1IpAddress_Type()
)
netMgmtDomainServer1IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtDomainServer1IpAddress.setStatus("mandatory")
_NetMgmtDomainServer2IpAddress_Type = IpAddress
_NetMgmtDomainServer2IpAddress_Object = MibScalar
netMgmtDomainServer2IpAddress = _NetMgmtDomainServer2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 22),
    _NetMgmtDomainServer2IpAddress_Type()
)
netMgmtDomainServer2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtDomainServer2IpAddress.setStatus("mandatory")


class _NetMgmtDefaultSearchDomain_Type(DisplayString):
    """Custom type netMgmtDefaultSearchDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NetMgmtDefaultSearchDomain_Type.__name__ = "DisplayString"
_NetMgmtDefaultSearchDomain_Object = MibScalar
netMgmtDefaultSearchDomain = _NetMgmtDefaultSearchDomain_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 23),
    _NetMgmtDefaultSearchDomain_Type()
)
netMgmtDefaultSearchDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtDefaultSearchDomain.setStatus("mandatory")


class _NetMgmtHttpServerAdminState_Type(Integer32):
    """Custom type netMgmtHttpServerAdminState based on Integer32"""
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


_NetMgmtHttpServerAdminState_Type.__name__ = "Integer32"
_NetMgmtHttpServerAdminState_Object = MibScalar
netMgmtHttpServerAdminState = _NetMgmtHttpServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 24),
    _NetMgmtHttpServerAdminState_Type()
)
netMgmtHttpServerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtHttpServerAdminState.setStatus("mandatory")


class _NetMgmtHttpPort_Type(Integer32):
    """Custom type netMgmtHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetMgmtHttpPort_Type.__name__ = "Integer32"
_NetMgmtHttpPort_Object = MibScalar
netMgmtHttpPort = _NetMgmtHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 4, 25),
    _NetMgmtHttpPort_Type()
)
netMgmtHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netMgmtHttpPort.setStatus("mandatory")
_Upgrade_ObjectIdentity = ObjectIdentity
upgrade = _Upgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5)
)


class _UpgradeFirmwareSource_Type(Integer32):
    """Custom type upgradeFirmwareSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eprom", 1),
          ("flash", 2))
    )


_UpgradeFirmwareSource_Type.__name__ = "Integer32"
_UpgradeFirmwareSource_Object = MibScalar
upgradeFirmwareSource = _UpgradeFirmwareSource_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 1),
    _UpgradeFirmwareSource_Type()
)
upgradeFirmwareSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeFirmwareSource.setStatus("mandatory")


class _UpgradeEPROMRevision_Type(DisplayString):
    """Custom type upgradeEPROMRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UpgradeEPROMRevision_Type.__name__ = "DisplayString"
_UpgradeEPROMRevision_Object = MibScalar
upgradeEPROMRevision = _UpgradeEPROMRevision_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 2),
    _UpgradeEPROMRevision_Type()
)
upgradeEPROMRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeEPROMRevision.setStatus("mandatory")
_UpgradeFlashSize_Type = Integer32
_UpgradeFlashSize_Object = MibScalar
upgradeFlashSize = _UpgradeFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 3),
    _UpgradeFlashSize_Type()
)
upgradeFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFlashSize.setStatus("mandatory")


class _UpgradeFlashBankStatus_Type(DisplayString):
    """Custom type upgradeFlashBankStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UpgradeFlashBankStatus_Type.__name__ = "DisplayString"
_UpgradeFlashBankStatus_Object = MibScalar
upgradeFlashBankStatus = _UpgradeFlashBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 4),
    _UpgradeFlashBankStatus_Type()
)
upgradeFlashBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeFlashBankStatus.setStatus("mandatory")
_UpgradeTFTPServerAddress_Type = IpAddress
_UpgradeTFTPServerAddress_Object = MibScalar
upgradeTFTPServerAddress = _UpgradeTFTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 5),
    _UpgradeTFTPServerAddress_Type()
)
upgradeTFTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeTFTPServerAddress.setStatus("mandatory")


class _UpgradeTFTPLoadFilename_Type(DisplayString):
    """Custom type upgradeTFTPLoadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UpgradeTFTPLoadFilename_Type.__name__ = "DisplayString"
_UpgradeTFTPLoadFilename_Object = MibScalar
upgradeTFTPLoadFilename = _UpgradeTFTPLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 6),
    _UpgradeTFTPLoadFilename_Type()
)
upgradeTFTPLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeTFTPLoadFilename.setStatus("mandatory")


class _UpgradeTFTPInitiate_Type(Integer32):
    """Custom type upgradeTFTPInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUpgrade", 2),
          ("upgrade", 1))
    )


_UpgradeTFTPInitiate_Type.__name__ = "Integer32"
_UpgradeTFTPInitiate_Object = MibScalar
upgradeTFTPInitiate = _UpgradeTFTPInitiate_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 7),
    _UpgradeTFTPInitiate_Type()
)
upgradeTFTPInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeTFTPInitiate.setStatus("mandatory")


class _UpgradeAutoExecute_Type(Integer32):
    """Custom type upgradeAutoExecute based on Integer32"""
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


_UpgradeAutoExecute_Type.__name__ = "Integer32"
_UpgradeAutoExecute_Object = MibScalar
upgradeAutoExecute = _UpgradeAutoExecute_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 8),
    _UpgradeAutoExecute_Type()
)
upgradeAutoExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeAutoExecute.setStatus("mandatory")


class _UpgradeTFTPAccept_Type(Integer32):
    """Custom type upgradeTFTPAccept based on Integer32"""
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


_UpgradeTFTPAccept_Type.__name__ = "Integer32"
_UpgradeTFTPAccept_Object = MibScalar
upgradeTFTPAccept = _UpgradeTFTPAccept_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 9),
    _UpgradeTFTPAccept_Type()
)
upgradeTFTPAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeTFTPAccept.setStatus("mandatory")


class _UpgradeTFTPServerName_Type(DisplayString):
    """Custom type upgradeTFTPServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_UpgradeTFTPServerName_Type.__name__ = "DisplayString"
_UpgradeTFTPServerName_Object = MibScalar
upgradeTFTPServerName = _UpgradeTFTPServerName_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 5, 10),
    _UpgradeTFTPServerName_Type()
)
upgradeTFTPServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeTFTPServerName.setStatus("mandatory")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6)
)
_VlanMaxSupported_Type = Integer32
_VlanMaxSupported_Object = MibScalar
vlanMaxSupported = _VlanMaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 1),
    _VlanMaxSupported_Type()
)
vlanMaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxSupported.setStatus("mandatory")


class _VlanAllowMembershipOverlap_Type(Integer32):
    """Custom type vlanAllowMembershipOverlap based on Integer32"""
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


_VlanAllowMembershipOverlap_Type.__name__ = "Integer32"
_VlanAllowMembershipOverlap_Object = MibScalar
vlanAllowMembershipOverlap = _VlanAllowMembershipOverlap_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 2),
    _VlanAllowMembershipOverlap_Type()
)
vlanAllowMembershipOverlap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAllowMembershipOverlap.setStatus("deprecated")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("mandatory")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1)
)
vlanEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("mandatory")
_VlanIndex_Type = Integer32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("mandatory")


class _VlanName_Type(DisplayString):
    """Custom type vlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_VlanName_Type.__name__ = "DisplayString"
_VlanName_Object = MibTableColumn
vlanName = _VlanName_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1, 2),
    _VlanName_Type()
)
vlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanName.setStatus("mandatory")
_VlanMemberPorts_Type = OctetString
_VlanMemberPorts_Object = MibTableColumn
vlanMemberPorts = _VlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1, 3),
    _VlanMemberPorts_Type()
)
vlanMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMemberPorts.setStatus("mandatory")
_VlanIpAddress_Type = IpAddress
_VlanIpAddress_Object = MibTableColumn
vlanIpAddress = _VlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1, 4),
    _VlanIpAddress_Type()
)
vlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpAddress.setStatus("mandatory")
_VlanIpSubnetMask_Type = IpAddress
_VlanIpSubnetMask_Object = MibTableColumn
vlanIpSubnetMask = _VlanIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1, 5),
    _VlanIpSubnetMask_Type()
)
vlanIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpSubnetMask.setStatus("mandatory")
_VlanBridgeTemplate_Type = Integer32
_VlanBridgeTemplate_Object = MibTableColumn
vlanBridgeTemplate = _VlanBridgeTemplate_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1, 6),
    _VlanBridgeTemplate_Type()
)
vlanBridgeTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanBridgeTemplate.setStatus("mandatory")


class _VlanStpAdmin_Type(Integer32):
    """Custom type vlanStpAdmin based on Integer32"""
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


_VlanStpAdmin_Type.__name__ = "Integer32"
_VlanStpAdmin_Object = MibTableColumn
vlanStpAdmin = _VlanStpAdmin_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 3, 1, 7),
    _VlanStpAdmin_Type()
)
vlanStpAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStpAdmin.setStatus("mandatory")
_VlanMemberTable_Object = MibTable
vlanMemberTable = _VlanMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 4)
)
if mibBuilder.loadTexts:
    vlanMemberTable.setStatus("mandatory")
_VlanMemberEntry_Object = MibTableRow
vlanMemberEntry = _VlanMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 4, 1)
)
vlanMemberEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "vlanMemberIndex"),
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "vlanMemberPortIndex"),
)
if mibBuilder.loadTexts:
    vlanMemberEntry.setStatus("mandatory")
_VlanMemberIndex_Type = Integer32
_VlanMemberIndex_Object = MibTableColumn
vlanMemberIndex = _VlanMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 4, 1, 1),
    _VlanMemberIndex_Type()
)
vlanMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMemberIndex.setStatus("mandatory")
_VlanMemberPortIndex_Type = Integer32
_VlanMemberPortIndex_Object = MibTableColumn
vlanMemberPortIndex = _VlanMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 4, 1, 2),
    _VlanMemberPortIndex_Type()
)
vlanMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMemberPortIndex.setStatus("mandatory")


class _VlanMemberPortOfVlan_Type(Integer32):
    """Custom type vlanMemberPortOfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_VlanMemberPortOfVlan_Type.__name__ = "Integer32"
_VlanMemberPortOfVlan_Object = MibTableColumn
vlanMemberPortOfVlan = _VlanMemberPortOfVlan_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 4, 1, 3),
    _VlanMemberPortOfVlan_Type()
)
vlanMemberPortOfVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberPortOfVlan.setStatus("mandatory")
_BridgeTemplateMax_Type = Integer32
_BridgeTemplateMax_Object = MibScalar
bridgeTemplateMax = _BridgeTemplateMax_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 5),
    _BridgeTemplateMax_Type()
)
bridgeTemplateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTemplateMax.setStatus("mandatory")
_BridgeTemplateTable_Object = MibTable
bridgeTemplateTable = _BridgeTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 6)
)
if mibBuilder.loadTexts:
    bridgeTemplateTable.setStatus("mandatory")
_BridgeTemplateEntry_Object = MibTableRow
bridgeTemplateEntry = _BridgeTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 6, 1)
)
bridgeTemplateEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "bridgeTemplateIndex"),
)
if mibBuilder.loadTexts:
    bridgeTemplateEntry.setStatus("mandatory")
_BridgeTemplateIndex_Type = Integer32
_BridgeTemplateIndex_Object = MibTableColumn
bridgeTemplateIndex = _BridgeTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 6, 1, 1),
    _BridgeTemplateIndex_Type()
)
bridgeTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTemplateIndex.setStatus("mandatory")
_BridgeTemplatePriority_Type = Integer32
_BridgeTemplatePriority_Object = MibTableColumn
bridgeTemplatePriority = _BridgeTemplatePriority_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 6, 1, 2),
    _BridgeTemplatePriority_Type()
)
bridgeTemplatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTemplatePriority.setStatus("mandatory")
_BridgeTemplateMaxAge_Type = Timeout
_BridgeTemplateMaxAge_Object = MibTableColumn
bridgeTemplateMaxAge = _BridgeTemplateMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 6, 1, 3),
    _BridgeTemplateMaxAge_Type()
)
bridgeTemplateMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTemplateMaxAge.setStatus("mandatory")
_BridgeTemplateHelloTime_Type = Timeout
_BridgeTemplateHelloTime_Object = MibTableColumn
bridgeTemplateHelloTime = _BridgeTemplateHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 6, 1, 4),
    _BridgeTemplateHelloTime_Type()
)
bridgeTemplateHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTemplateHelloTime.setStatus("mandatory")
_BridgeTemplateForwardDelay_Type = Timeout
_BridgeTemplateForwardDelay_Object = MibTableColumn
bridgeTemplateForwardDelay = _BridgeTemplateForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 6, 6, 1, 5),
    _BridgeTemplateForwardDelay_Type()
)
bridgeTemplateForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTemplateForwardDelay.setStatus("mandatory")
_BandwidthUsage_ObjectIdentity = ObjectIdentity
bandwidthUsage = _BandwidthUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7)
)
_BandwidthUsageCurrent_Type = Counter32
_BandwidthUsageCurrent_Object = MibScalar
bandwidthUsageCurrent = _BandwidthUsageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 1),
    _BandwidthUsageCurrent_Type()
)
bandwidthUsageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthUsageCurrent.setStatus("mandatory")
_BandwidthUsageMaxPeakEntries_Type = Integer32
_BandwidthUsageMaxPeakEntries_Object = MibScalar
bandwidthUsageMaxPeakEntries = _BandwidthUsageMaxPeakEntries_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 2),
    _BandwidthUsageMaxPeakEntries_Type()
)
bandwidthUsageMaxPeakEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthUsageMaxPeakEntries.setStatus("mandatory")


class _BandwidthUsagePeakInterval_Type(Integer32):
    """Custom type bandwidthUsagePeakInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              12,
              24,
              48,
              72,
              96,
              120,
              144,
              168)
        )
    )
    namedValues = NamedValues(
        *(("fivedays", 120),
          ("fourdays", 96),
          ("oneday", 24),
          ("onehour", 1),
          ("oneweek", 168),
          ("sixdays", 144),
          ("sixhours", 6),
          ("threedays", 72),
          ("threehours", 3),
          ("twelvehours", 12),
          ("twodays", 48))
    )


_BandwidthUsagePeakInterval_Type.__name__ = "Integer32"
_BandwidthUsagePeakInterval_Object = MibScalar
bandwidthUsagePeakInterval = _BandwidthUsagePeakInterval_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 3),
    _BandwidthUsagePeakInterval_Type()
)
bandwidthUsagePeakInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthUsagePeakInterval.setStatus("mandatory")


class _BandwidthUsagePeakRestart_Type(Integer32):
    """Custom type bandwidthUsagePeakRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestart", 1),
          ("restart", 2))
    )


_BandwidthUsagePeakRestart_Type.__name__ = "Integer32"
_BandwidthUsagePeakRestart_Object = MibScalar
bandwidthUsagePeakRestart = _BandwidthUsagePeakRestart_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 4),
    _BandwidthUsagePeakRestart_Type()
)
bandwidthUsagePeakRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthUsagePeakRestart.setStatus("mandatory")
_BandwidthUsageCurrentPeakEntry_Type = Integer32
_BandwidthUsageCurrentPeakEntry_Object = MibScalar
bandwidthUsageCurrentPeakEntry = _BandwidthUsageCurrentPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 5),
    _BandwidthUsageCurrentPeakEntry_Type()
)
bandwidthUsageCurrentPeakEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthUsageCurrentPeakEntry.setStatus("mandatory")
_BandwidthUsagePeakTable_Object = MibTable
bandwidthUsagePeakTable = _BandwidthUsagePeakTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 6)
)
if mibBuilder.loadTexts:
    bandwidthUsagePeakTable.setStatus("mandatory")
_BandwidthUsagePeakEntry_Object = MibTableRow
bandwidthUsagePeakEntry = _BandwidthUsagePeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 6, 1)
)
bandwidthUsagePeakEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "bandwidthUsagePeakIndex"),
)
if mibBuilder.loadTexts:
    bandwidthUsagePeakEntry.setStatus("mandatory")
_BandwidthUsagePeakIndex_Type = Integer32
_BandwidthUsagePeakIndex_Object = MibTableColumn
bandwidthUsagePeakIndex = _BandwidthUsagePeakIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 6, 1, 1),
    _BandwidthUsagePeakIndex_Type()
)
bandwidthUsagePeakIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthUsagePeakIndex.setStatus("mandatory")


class _BandwidthUsageStartTime_Type(DisplayString):
    """Custom type bandwidthUsageStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BandwidthUsageStartTime_Type.__name__ = "DisplayString"
_BandwidthUsageStartTime_Object = MibTableColumn
bandwidthUsageStartTime = _BandwidthUsageStartTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 6, 1, 2),
    _BandwidthUsageStartTime_Type()
)
bandwidthUsageStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthUsageStartTime.setStatus("mandatory")
_BandwidthUsagePeak_Type = Integer32
_BandwidthUsagePeak_Object = MibTableColumn
bandwidthUsagePeak = _BandwidthUsagePeak_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 6, 1, 3),
    _BandwidthUsagePeak_Type()
)
bandwidthUsagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthUsagePeak.setStatus("mandatory")


class _BandwidthUsagePeakTime_Type(DisplayString):
    """Custom type bandwidthUsagePeakTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BandwidthUsagePeakTime_Type.__name__ = "DisplayString"
_BandwidthUsagePeakTime_Object = MibTableColumn
bandwidthUsagePeakTime = _BandwidthUsagePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 7, 6, 1, 4),
    _BandwidthUsagePeakTime_Type()
)
bandwidthUsagePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthUsagePeakTime.setStatus("mandatory")
_BridgeGroup_ObjectIdentity = ObjectIdentity
bridgeGroup = _BridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8)
)
_BridgeGroupMaxSupported_Type = Integer32
_BridgeGroupMaxSupported_Object = MibScalar
bridgeGroupMaxSupported = _BridgeGroupMaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 1),
    _BridgeGroupMaxSupported_Type()
)
bridgeGroupMaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupMaxSupported.setStatus("mandatory")


class _BridgeGroupAllowMembershipOverlap_Type(Integer32):
    """Custom type bridgeGroupAllowMembershipOverlap based on Integer32"""
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


_BridgeGroupAllowMembershipOverlap_Type.__name__ = "Integer32"
_BridgeGroupAllowMembershipOverlap_Object = MibScalar
bridgeGroupAllowMembershipOverlap = _BridgeGroupAllowMembershipOverlap_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 2),
    _BridgeGroupAllowMembershipOverlap_Type()
)
bridgeGroupAllowMembershipOverlap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupAllowMembershipOverlap.setStatus("mandatory")
_BridgeGroupTable_Object = MibTable
bridgeGroupTable = _BridgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 3)
)
if mibBuilder.loadTexts:
    bridgeGroupTable.setStatus("mandatory")
_BridgeGroupEntry_Object = MibTableRow
bridgeGroupEntry = _BridgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 3, 1)
)
bridgeGroupEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "bridgeGroupIndex"),
)
if mibBuilder.loadTexts:
    bridgeGroupEntry.setStatus("mandatory")
_BridgeGroupIndex_Type = Integer32
_BridgeGroupIndex_Object = MibTableColumn
bridgeGroupIndex = _BridgeGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 3, 1, 1),
    _BridgeGroupIndex_Type()
)
bridgeGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupIndex.setStatus("mandatory")
_BridgeGroupMemberPorts_Type = OctetString
_BridgeGroupMemberPorts_Object = MibTableColumn
bridgeGroupMemberPorts = _BridgeGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 3, 1, 3),
    _BridgeGroupMemberPorts_Type()
)
bridgeGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupMemberPorts.setStatus("mandatory")


class _BridgeGroupStpAdmin_Type(Integer32):
    """Custom type bridgeGroupStpAdmin based on Integer32"""
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


_BridgeGroupStpAdmin_Type.__name__ = "Integer32"
_BridgeGroupStpAdmin_Object = MibTableColumn
bridgeGroupStpAdmin = _BridgeGroupStpAdmin_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 3, 1, 4),
    _BridgeGroupStpAdmin_Type()
)
bridgeGroupStpAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupStpAdmin.setStatus("mandatory")
_BridgeGroupMemberTable_Object = MibTable
bridgeGroupMemberTable = _BridgeGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 4)
)
if mibBuilder.loadTexts:
    bridgeGroupMemberTable.setStatus("mandatory")
_BridgeGroupMemberEntry_Object = MibTableRow
bridgeGroupMemberEntry = _BridgeGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 4, 1)
)
bridgeGroupMemberEntry.setIndexNames(
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "bridgeGroupMemberIndex"),
    (0, "STAND-ALONE-ETHERNET-SWITCH-MIB", "bridgeGroupMemberPortIndex"),
)
if mibBuilder.loadTexts:
    bridgeGroupMemberEntry.setStatus("mandatory")
_BridgeGroupMemberIndex_Type = Integer32
_BridgeGroupMemberIndex_Object = MibTableColumn
bridgeGroupMemberIndex = _BridgeGroupMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 4, 1, 1),
    _BridgeGroupMemberIndex_Type()
)
bridgeGroupMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupMemberIndex.setStatus("mandatory")
_BridgeGroupMemberPortIndex_Type = Integer32
_BridgeGroupMemberPortIndex_Object = MibTableColumn
bridgeGroupMemberPortIndex = _BridgeGroupMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 4, 1, 2),
    _BridgeGroupMemberPortIndex_Type()
)
bridgeGroupMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupMemberPortIndex.setStatus("mandatory")


class _BridgeGroupMemberPortOfBridgeGroup_Type(Integer32):
    """Custom type bridgeGroupMemberPortOfBridgeGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_BridgeGroupMemberPortOfBridgeGroup_Type.__name__ = "Integer32"
_BridgeGroupMemberPortOfBridgeGroup_Object = MibTableColumn
bridgeGroupMemberPortOfBridgeGroup = _BridgeGroupMemberPortOfBridgeGroup_Object(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 8, 4, 1, 3),
    _BridgeGroupMemberPortOfBridgeGroup_Type()
)
bridgeGroupMemberPortOfBridgeGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupMemberPortOfBridgeGroup.setStatus("mandatory")

# Managed Objects groups


# Notification objects

logonIntruder = NotificationType(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 0, 0)
)
logonIntruder.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    logonIntruder.setStatus(
        ""
    )

switchDiagnostic = NotificationType(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 0, 1)
)
switchDiagnostic.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    switchDiagnostic.setStatus(
        ""
    )

addressViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 0, 3)
)
addressViolation.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    addressViolation.setStatus(
        ""
    )

broadcastStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 0, 4)
)
broadcastStorm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    broadcastStorm.setStatus(
        ""
    )

rpsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 0, 5)
)
rpsFailed.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    rpsFailed.setStatus(
        ""
    )

ipAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 437, 1, 1, 3, 0, 6)
)
ipAddressChange.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    ipAddressChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STAND-ALONE-ETHERNET-SWITCH-MIB",
    **{"grandjunction": grandjunction,
       "products": products,
       "fastLink": fastLink,
       "seriesG2xx": seriesG2xx,
       "esModuleBasic": esModuleBasic,
       "series2000": series2000,
       "logonIntruder": logonIntruder,
       "switchDiagnostic": switchDiagnostic,
       "addressViolation": addressViolation,
       "broadcastStorm": broadcastStorm,
       "rpsFailed": rpsFailed,
       "ipAddressChange": ipAddressChange,
       "sysInfo": sysInfo,
       "sysInfoFwdEngineRevision": sysInfoFwdEngineRevision,
       "sysInfoBoardRevision": sysInfoBoardRevision,
       "sysInfoTotalNumberOfPorts": sysInfoTotalNumberOfPorts,
       "sysInfoNumberOfSwitchPorts": sysInfoNumberOfSwitchPorts,
       "sysInfoNumberOfSharedPorts": sysInfoNumberOfSharedPorts,
       "sysInfoNumberOfInstalledModules": sysInfoNumberOfInstalledModules,
       "sysInfoBuffersUsed": sysInfoBuffersUsed,
       "sysInfoMaxBuffers": sysInfoMaxBuffers,
       "sysInfoUtilDisplay": sysInfoUtilDisplay,
       "sysInfoAddrCapacity": sysInfoAddrCapacity,
       "sysInfoRestrictedStaticAddrCapacity": sysInfoRestrictedStaticAddrCapacity,
       "sysInfoPOSTResult": sysInfoPOSTResult,
       "sysInfoPortFailedPOSTMap": sysInfoPortFailedPOSTMap,
       "sysInfoPortLinkDisplayMap": sysInfoPortLinkDisplayMap,
       "sysInfoPortDisabledDisplayMap": sysInfoPortDisabledDisplayMap,
       "sysInfoBroadcastStormLastTime": sysInfoBroadcastStormLastTime,
       "sysInfoPortExceedBroadcastStorm": sysInfoPortExceedBroadcastStorm,
       "sysInfoRedundantPowerState": sysInfoRedundantPowerState,
       "sysInfoInternalPowerState": sysInfoInternalPowerState,
       "sysInfoConfigFileStatus": sysInfoConfigFileStatus,
       "sysInfoImageCapability": sysInfoImageCapability,
       "sysConfig": sysConfig,
       "sysConfigReset": sysConfigReset,
       "sysConfigDefaultReset": sysConfigDefaultReset,
       "sysConfigClearPortStats": sysConfigClearPortStats,
       "sysConfigAddressViolationAction": sysConfigAddressViolationAction,
       "sysConfigAddressViolationAlert": sysConfigAddressViolationAlert,
       "sysConfigSwitchingMode": sysConfigSwitchingMode,
       "sysConfigMulticastStoreAndForward": sysConfigMulticastStoreAndForward,
       "sysConfigMonitor": sysConfigMonitor,
       "sysConfigMonitorPort": sysConfigMonitorPort,
       "sysConfigHigherProtocolMonitor": sysConfigHigherProtocolMonitor,
       "sysConfigPort25Connector": sysConfigPort25Connector,
       "sysConfigHeuristics": sysConfigHeuristics,
       "sysConfigEnableSTP": sysConfigEnableSTP,
       "sysConfigStrictSTPTransition": sysConfigStrictSTPTransition,
       "sysConfigBroadcastStormAction": sysConfigBroadcastStormAction,
       "sysConfigBroadcastStormAlert": sysConfigBroadcastStormAlert,
       "sysConfigBroadcastThreshold": sysConfigBroadcastThreshold,
       "sysConfigBroadcastReEnableThreshold": sysConfigBroadcastReEnableThreshold,
       "sysConfig10MbpsEnhancedCongestionControl": sysConfig10MbpsEnhancedCongestionControl,
       "sysConfigNetworkPort": sysConfigNetworkPort,
       "sysConfigHalfDuplexBackPressure": sysConfigHalfDuplexBackPressure,
       "sysConfigFastEthcParmsPort": sysConfigFastEthcParmsPort,
       "sysConfigTftpServerName": sysConfigTftpServerName,
       "sysConfigConfigFileAuto": sysConfigConfigFileAuto,
       "sysConfigPortGroupingMode": sysConfigPortGroupingMode,
       "port": port,
       "switchPortTable": switchPortTable,
       "swPortEntry": swPortEntry,
       "swPortIndex": swPortIndex,
       "swPortControllerRevision": swPortControllerRevision,
       "swPortName": swPortName,
       "swPortMediaCapability": swPortMediaCapability,
       "swPortType": swPortType,
       "swPortConnectorType": swPortConnectorType,
       "swPortACR": swPortACR,
       "swPortFullDuplex": swPortFullDuplex,
       "swPortStatus": swPortStatus,
       "swPortAdminStatus": swPortAdminStatus,
       "swPortLastStatus": swPortLastStatus,
       "swPortStatusChanges": swPortStatusChanges,
       "swPortAddressingSecurity": swPortAddressingSecurity,
       "swPortAddressTableSize": swPortAddressTableSize,
       "swPortNumberOfLearnedAddresses": swPortNumberOfLearnedAddresses,
       "swPortNumberOfStaticAddresses": swPortNumberOfStaticAddresses,
       "swPortEraseAddresses": swPortEraseAddresses,
       "swPortFloodUnregisteredMulticasts": swPortFloodUnregisteredMulticasts,
       "swPortFloodUnknownUnicasts": swPortFloodUnknownUnicasts,
       "swPortMonitoring": swPortMonitoring,
       "swPortSecuredAddressViolations": swPortSecuredAddressViolations,
       "swPortLinkbeatStatus": swPortLinkbeatStatus,
       "swPortLinkbeatLosses": swPortLinkbeatLosses,
       "swPortJabberStatus": swPortJabberStatus,
       "swPortJabbers": swPortJabbers,
       "swPortClearStatistics": swPortClearStatistics,
       "swPortBroadcastStormBlocked": swPortBroadcastStormBlocked,
       "swPortSTPPortFastMode": swPortSTPPortFastMode,
       "swPortHalfDuplexBackPressure": swPortHalfDuplexBackPressure,
       "swPortDuplexStatus": swPortDuplexStatus,
       "swPortFullDuplexFlowControl": swPortFullDuplexFlowControl,
       "swPortEnhancedCongestionControl": swPortEnhancedCongestionControl,
       "swPortBridgePriority": swPortBridgePriority,
       "swPortBridgePriorityAlternate": swPortBridgePriorityAlternate,
       "swPortBridgePathCost": swPortBridgePathCost,
       "swPortBridgePathCostAlternate": swPortBridgePathCostAlternate,
       "swPortIfIndex": swPortIfIndex,
       "swPortInternal": swPortInternal,
       "switchPortRxStatTable": switchPortRxStatTable,
       "swPortRxStatEntry": swPortRxStatEntry,
       "swPortRxStatIndex": swPortRxStatIndex,
       "swPortRxTotalFrames": swPortRxTotalFrames,
       "swPortRxTotalOctets": swPortRxTotalOctets,
       "swPortRxTotalOctetsWraps": swPortRxTotalOctetsWraps,
       "swPortRxUnicastFrames": swPortRxUnicastFrames,
       "swPortRxUnicastOctets": swPortRxUnicastOctets,
       "swPortRxUnicastOctetsWraps": swPortRxUnicastOctetsWraps,
       "swPortRxBroadcastFrames": swPortRxBroadcastFrames,
       "swPortRxBroadcastOctets": swPortRxBroadcastOctets,
       "swPortRxBroadcastOctetsWraps": swPortRxBroadcastOctetsWraps,
       "swPortRxMulticastFrames": swPortRxMulticastFrames,
       "swPortRxMulticastOctets": swPortRxMulticastOctets,
       "swPortRxMulticastOctetsWraps": swPortRxMulticastOctetsWraps,
       "swPortRxForwardedFrames": swPortRxForwardedFrames,
       "swPortRxFilteredFrames": swPortRxFilteredFrames,
       "swPortRxNoBufferDiscards": swPortRxNoBufferDiscards,
       "swPortRxFCSErrors": swPortRxFCSErrors,
       "swPortRxAlignmentErrors": swPortRxAlignmentErrors,
       "swPortRxFrameTooLongs": swPortRxFrameTooLongs,
       "swPortRxRunts": swPortRxRunts,
       "switchPortTxStatTable": switchPortTxStatTable,
       "swPortTxStatEntry": swPortTxStatEntry,
       "swPortTxStatIndex": swPortTxStatIndex,
       "swPortTxTotalFrames": swPortTxTotalFrames,
       "swPortTxTotalOctets": swPortTxTotalOctets,
       "swPortTxTotalOctetsWraps": swPortTxTotalOctetsWraps,
       "swPortTxUnicastFrames": swPortTxUnicastFrames,
       "swPortTxUnicastOctets": swPortTxUnicastOctets,
       "swPortTxUnicastOctetsWraps": swPortTxUnicastOctetsWraps,
       "swPortTxBroadcastFrames": swPortTxBroadcastFrames,
       "swPortTxBroadcastOctets": swPortTxBroadcastOctets,
       "swPortTxBroadcastOctetsWraps": swPortTxBroadcastOctetsWraps,
       "swPortTxMulticastFrames": swPortTxMulticastFrames,
       "swPortTxMulticastOctets": swPortTxMulticastOctets,
       "swPortTxMulticastOctetsWraps": swPortTxMulticastOctetsWraps,
       "swPortTxDeferrals": swPortTxDeferrals,
       "swPortTxSingleCollisions": swPortTxSingleCollisions,
       "swPortTxMultipleCollisions": swPortTxMultipleCollisions,
       "swPortTxLateCollisions": swPortTxLateCollisions,
       "swPortTxExcessiveCollisions": swPortTxExcessiveCollisions,
       "swPortTxExcessiveDeferrals": swPortTxExcessiveDeferrals,
       "swPortTxExcessiveCollision16s": swPortTxExcessiveCollision16s,
       "swPortTxExcessiveCollision4s": swPortTxExcessiveCollision4s,
       "swPortTxQueueFullDiscards": swPortTxQueueFullDiscards,
       "swPortTxErrors": swPortTxErrors,
       "switchPortTxCollTable": switchPortTxCollTable,
       "swPortTxCollEntry": swPortTxCollEntry,
       "swPortTxCollIndex": swPortTxCollIndex,
       "swPortTxCollCount": swPortTxCollCount,
       "swPortTxCollFrequencies": swPortTxCollFrequencies,
       "netMgmt": netMgmt,
       "netMgmtIpAddress": netMgmtIpAddress,
       "netMgmtIpSubnetMask": netMgmtIpSubnetMask,
       "netMgmtDefaultGateway": netMgmtDefaultGateway,
       "netMgmtEnableAuthenTraps": netMgmtEnableAuthenTraps,
       "netMgmtEnableLinkTraps": netMgmtEnableLinkTraps,
       "netMgmtConsoleInactTime": netMgmtConsoleInactTime,
       "netMgmtConsolePasswordThresh": netMgmtConsolePasswordThresh,
       "netMgmtConsoleSilentTime": netMgmtConsoleSilentTime,
       "netMgmtModemInitString": netMgmtModemInitString,
       "netMgmtModemDialString": netMgmtModemDialString,
       "netMgmtModemDialDelay": netMgmtModemDialDelay,
       "netMgmtModemAutoAnswer": netMgmtModemAutoAnswer,
       "netMgmtSetClientTable": netMgmtSetClientTable,
       "netMgmtSetClientEntry": netMgmtSetClientEntry,
       "netMgmtSetClientIndex": netMgmtSetClientIndex,
       "netMgmtSetClientAddr": netMgmtSetClientAddr,
       "netMgmtSetClientStatus": netMgmtSetClientStatus,
       "netMgmtSetClientName": netMgmtSetClientName,
       "netMgmtTrapClientTable": netMgmtTrapClientTable,
       "netMgmtTrapClientEntry": netMgmtTrapClientEntry,
       "netMgmtTrapClientIndex": netMgmtTrapClientIndex,
       "netMgmtTrapClientAddr": netMgmtTrapClientAddr,
       "netMgmtTrapClientComm": netMgmtTrapClientComm,
       "netMgmtTrapClientStatus": netMgmtTrapClientStatus,
       "netMgmtTrapClientName": netMgmtTrapClientName,
       "netMgmtCdpHoldTime": netMgmtCdpHoldTime,
       "netMgmtCdpTransmissionTime": netMgmtCdpTransmissionTime,
       "netMgmtCgmpEnable": netMgmtCgmpEnable,
       "netMgmtCgmpRouterHoldTime": netMgmtCgmpRouterHoldTime,
       "netMgmtVlan": netMgmtVlan,
       "netMgmtEnableRIP": netMgmtEnableRIP,
       "netMgmtDomainServer1IpAddress": netMgmtDomainServer1IpAddress,
       "netMgmtDomainServer2IpAddress": netMgmtDomainServer2IpAddress,
       "netMgmtDefaultSearchDomain": netMgmtDefaultSearchDomain,
       "netMgmtHttpServerAdminState": netMgmtHttpServerAdminState,
       "netMgmtHttpPort": netMgmtHttpPort,
       "upgrade": upgrade,
       "upgradeFirmwareSource": upgradeFirmwareSource,
       "upgradeEPROMRevision": upgradeEPROMRevision,
       "upgradeFlashSize": upgradeFlashSize,
       "upgradeFlashBankStatus": upgradeFlashBankStatus,
       "upgradeTFTPServerAddress": upgradeTFTPServerAddress,
       "upgradeTFTPLoadFilename": upgradeTFTPLoadFilename,
       "upgradeTFTPInitiate": upgradeTFTPInitiate,
       "upgradeAutoExecute": upgradeAutoExecute,
       "upgradeTFTPAccept": upgradeTFTPAccept,
       "upgradeTFTPServerName": upgradeTFTPServerName,
       "vlan": vlan,
       "vlanMaxSupported": vlanMaxSupported,
       "vlanAllowMembershipOverlap": vlanAllowMembershipOverlap,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanName": vlanName,
       "vlanMemberPorts": vlanMemberPorts,
       "vlanIpAddress": vlanIpAddress,
       "vlanIpSubnetMask": vlanIpSubnetMask,
       "vlanBridgeTemplate": vlanBridgeTemplate,
       "vlanStpAdmin": vlanStpAdmin,
       "vlanMemberTable": vlanMemberTable,
       "vlanMemberEntry": vlanMemberEntry,
       "vlanMemberIndex": vlanMemberIndex,
       "vlanMemberPortIndex": vlanMemberPortIndex,
       "vlanMemberPortOfVlan": vlanMemberPortOfVlan,
       "bridgeTemplateMax": bridgeTemplateMax,
       "bridgeTemplateTable": bridgeTemplateTable,
       "bridgeTemplateEntry": bridgeTemplateEntry,
       "bridgeTemplateIndex": bridgeTemplateIndex,
       "bridgeTemplatePriority": bridgeTemplatePriority,
       "bridgeTemplateMaxAge": bridgeTemplateMaxAge,
       "bridgeTemplateHelloTime": bridgeTemplateHelloTime,
       "bridgeTemplateForwardDelay": bridgeTemplateForwardDelay,
       "bandwidthUsage": bandwidthUsage,
       "bandwidthUsageCurrent": bandwidthUsageCurrent,
       "bandwidthUsageMaxPeakEntries": bandwidthUsageMaxPeakEntries,
       "bandwidthUsagePeakInterval": bandwidthUsagePeakInterval,
       "bandwidthUsagePeakRestart": bandwidthUsagePeakRestart,
       "bandwidthUsageCurrentPeakEntry": bandwidthUsageCurrentPeakEntry,
       "bandwidthUsagePeakTable": bandwidthUsagePeakTable,
       "bandwidthUsagePeakEntry": bandwidthUsagePeakEntry,
       "bandwidthUsagePeakIndex": bandwidthUsagePeakIndex,
       "bandwidthUsageStartTime": bandwidthUsageStartTime,
       "bandwidthUsagePeak": bandwidthUsagePeak,
       "bandwidthUsagePeakTime": bandwidthUsagePeakTime,
       "bridgeGroup": bridgeGroup,
       "bridgeGroupMaxSupported": bridgeGroupMaxSupported,
       "bridgeGroupAllowMembershipOverlap": bridgeGroupAllowMembershipOverlap,
       "bridgeGroupTable": bridgeGroupTable,
       "bridgeGroupEntry": bridgeGroupEntry,
       "bridgeGroupIndex": bridgeGroupIndex,
       "bridgeGroupMemberPorts": bridgeGroupMemberPorts,
       "bridgeGroupStpAdmin": bridgeGroupStpAdmin,
       "bridgeGroupMemberTable": bridgeGroupMemberTable,
       "bridgeGroupMemberEntry": bridgeGroupMemberEntry,
       "bridgeGroupMemberIndex": bridgeGroupMemberIndex,
       "bridgeGroupMemberPortIndex": bridgeGroupMemberPortIndex,
       "bridgeGroupMemberPortOfBridgeGroup": bridgeGroupMemberPortOfBridgeGroup}
)
