# SNMP MIB module (EXTREME-V2TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(bgpPeerRemoteAddr,) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgpPeerRemoteAddr")

(ClientAuthType,
 extremeV2Traps) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ClientAuthType",
    "extremeV2Traps")

(extremeEapsMode,
 extremeEapsName,
 extremeEapsPrevState,
 extremeEapsState) = mibBuilder.importSymbols(
    "EXTREME-EAPS-MIB",
    "extremeEapsMode",
    "extremeEapsName",
    "extremeEapsPrevState",
    "extremeEapsState")

(extremeEsrpGroup,
 extremeEsrpState) = mibBuilder.importSymbols(
    "EXTREME-ESRP-MIB",
    "extremeEsrpGroup",
    "extremeEsrpState")

(extremeNPModuleProcessorState,) = mibBuilder.importSymbols(
    "EXTREME-NP-MIB",
    "extremeNPModuleProcessorState")

(extremePethSlotMainPseIndex,
 extremePethSlotPSUActive) = mibBuilder.importSymbols(
    "EXTREME-POE-MIB",
    "extremePethSlotMainPseIndex",
    "extremePethSlotPSUActive")

(extremeIQosProfileIndex,) = mibBuilder.importSymbols(
    "EXTREME-QOS-MIB",
    "extremeIQosProfileIndex")

(extremeCpuAggregateUtilization,
 extremeCpuTaskUtilPair,
 extremeCpuUtilRisingThreshold,
 extremeHealthCheckAction,
 extremeHealthCheckErrorType,
 extremeHealthCheckMaxRetries,
 extremeMasterMSMSlot,
 extremeMsmFailoverCause,
 extremeSlotNumber) = mibBuilder.importSymbols(
    "EXTREME-SYSTEM-MIB",
    "extremeCpuAggregateUtilization",
    "extremeCpuTaskUtilPair",
    "extremeCpuUtilRisingThreshold",
    "extremeHealthCheckAction",
    "extremeHealthCheckErrorType",
    "extremeHealthCheckMaxRetries",
    "extremeMasterMSMSlot",
    "extremeMsmFailoverCause",
    "extremeSlotNumber")

(extremeVlanIfDescr,
 extremeVlanIfIndex) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfDescr",
    "extremeVlanIfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeCoreSCTraps_ObjectIdentity = ObjectIdentity
extremeCoreSCTraps = _ExtremeCoreSCTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1)
)
_ExtremeCoreSCTrapPrefix_ObjectIdentity = ObjectIdentity
extremeCoreSCTrapPrefix = _ExtremeCoreSCTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0)
)


class _ExtremeRateLimitExceededTrapType_Type(Integer32):
    """Custom type extremeRateLimitExceededTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("droppedBytes", 2),
          ("exceededCIR", 1))
    )


_ExtremeRateLimitExceededTrapType_Type.__name__ = "Integer32"
_ExtremeRateLimitExceededTrapType_Object = MibScalar
extremeRateLimitExceededTrapType = _ExtremeRateLimitExceededTrapType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7, 1),
    _ExtremeRateLimitExceededTrapType_Type()
)
extremeRateLimitExceededTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeRateLimitExceededTrapType.setStatus("current")


class _ExtremeRateLimitExceededTrapIndicator_Type(Integer32):
    """Custom type extremeRateLimitExceededTrapIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_ExtremeRateLimitExceededTrapIndicator_Type.__name__ = "Integer32"
_ExtremeRateLimitExceededTrapIndicator_Object = MibScalar
extremeRateLimitExceededTrapIndicator = _ExtremeRateLimitExceededTrapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7, 2),
    _ExtremeRateLimitExceededTrapIndicator_Type()
)
extremeRateLimitExceededTrapIndicator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeRateLimitExceededTrapIndicator.setStatus("current")
_ExtremeExceededByteCount_Type = Integer32
_ExtremeExceededByteCount_Object = MibScalar
extremeExceededByteCount = _ExtremeExceededByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7, 4),
    _ExtremeExceededByteCount_Type()
)
extremeExceededByteCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeExceededByteCount.setStatus("current")
_ExtremeBgpTraps_ObjectIdentity = ObjectIdentity
extremeBgpTraps = _ExtremeBgpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2)
)
_ExtremeBgpTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeBgpTrapsPrefix = _ExtremeBgpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2, 0)
)
_ExtremeSecurityTraps_ObjectIdentity = ObjectIdentity
extremeSecurityTraps = _ExtremeSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3)
)
_ExtremeSecurityTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeSecurityTrapsPrefix = _ExtremeSecurityTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0)
)
_ExtremeMacSecurityVlanIfIndex_Type = Integer32
_ExtremeMacSecurityVlanIfIndex_Object = MibScalar
extremeMacSecurityVlanIfIndex = _ExtremeMacSecurityVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 1),
    _ExtremeMacSecurityVlanIfIndex_Type()
)
extremeMacSecurityVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityVlanIfIndex.setStatus("current")


class _ExtremeMacSecurityVlanDescr_Type(DisplayString):
    """Custom type extremeMacSecurityVlanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeMacSecurityVlanDescr_Type.__name__ = "DisplayString"
_ExtremeMacSecurityVlanDescr_Object = MibScalar
extremeMacSecurityVlanDescr = _ExtremeMacSecurityVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 2),
    _ExtremeMacSecurityVlanDescr_Type()
)
extremeMacSecurityVlanDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityVlanDescr.setStatus("current")
_ExtremeMacSecurityMacAddress_Type = MacAddress
_ExtremeMacSecurityMacAddress_Object = MibScalar
extremeMacSecurityMacAddress = _ExtremeMacSecurityMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 3),
    _ExtremeMacSecurityMacAddress_Type()
)
extremeMacSecurityMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityMacAddress.setStatus("current")
_ExtremeMacSecurityPortIfIndex_Type = Integer32
_ExtremeMacSecurityPortIfIndex_Object = MibScalar
extremeMacSecurityPortIfIndex = _ExtremeMacSecurityPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 4),
    _ExtremeMacSecurityPortIfIndex_Type()
)
extremeMacSecurityPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityPortIfIndex.setStatus("current")
_ExtremeMacSecurityVlanId_Type = Integer32
_ExtremeMacSecurityVlanId_Object = MibScalar
extremeMacSecurityVlanId = _ExtremeMacSecurityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 5),
    _ExtremeMacSecurityVlanId_Type()
)
extremeMacSecurityVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeMacSecurityVlanId.setStatus("current")
_ExtremeNetloginStationMac_Type = MacAddress
_ExtremeNetloginStationMac_Object = MibScalar
extremeNetloginStationMac = _ExtremeNetloginStationMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 6),
    _ExtremeNetloginStationMac_Type()
)
extremeNetloginStationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginStationMac.setStatus("current")
_ExtremeNetloginStationAddr_Type = IpAddress
_ExtremeNetloginStationAddr_Object = MibScalar
extremeNetloginStationAddr = _ExtremeNetloginStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 7),
    _ExtremeNetloginStationAddr_Type()
)
extremeNetloginStationAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginStationAddr.setStatus("current")
_ExtremeNetloginPortIfIndex_Type = Integer32
_ExtremeNetloginPortIfIndex_Object = MibScalar
extremeNetloginPortIfIndex = _ExtremeNetloginPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 8),
    _ExtremeNetloginPortIfIndex_Type()
)
extremeNetloginPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginPortIfIndex.setStatus("current")
_ExtremeNetloginAuthType_Type = ClientAuthType
_ExtremeNetloginAuthType_Object = MibScalar
extremeNetloginAuthType = _ExtremeNetloginAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 9),
    _ExtremeNetloginAuthType_Type()
)
extremeNetloginAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginAuthType.setStatus("current")
_ExtremeNetloginSystemTime_Type = TimeStamp
_ExtremeNetloginSystemTime_Object = MibScalar
extremeNetloginSystemTime = _ExtremeNetloginSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 10),
    _ExtremeNetloginSystemTime_Type()
)
extremeNetloginSystemTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginSystemTime.setStatus("current")


class _ExtremeNetloginUser_Type(DisplayString):
    """Custom type extremeNetloginUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ExtremeNetloginUser_Type.__name__ = "DisplayString"
_ExtremeNetloginUser_Object = MibScalar
extremeNetloginUser = _ExtremeNetloginUser_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 11),
    _ExtremeNetloginUser_Type()
)
extremeNetloginUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginUser.setStatus("current")


class _ExtremeNetloginSrcVlan_Type(DisplayString):
    """Custom type extremeNetloginSrcVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ExtremeNetloginSrcVlan_Type.__name__ = "DisplayString"
_ExtremeNetloginSrcVlan_Object = MibScalar
extremeNetloginSrcVlan = _ExtremeNetloginSrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 12),
    _ExtremeNetloginSrcVlan_Type()
)
extremeNetloginSrcVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginSrcVlan.setStatus("current")


class _ExtremeNetloginDestVlan_Type(DisplayString):
    """Custom type extremeNetloginDestVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ExtremeNetloginDestVlan_Type.__name__ = "DisplayString"
_ExtremeNetloginDestVlan_Object = MibScalar
extremeNetloginDestVlan = _ExtremeNetloginDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 13),
    _ExtremeNetloginDestVlan_Type()
)
extremeNetloginDestVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginDestVlan.setStatus("current")


class _ExtremeNetloginSessionStatus_Type(Integer32):
    """Custom type extremeNetloginSessionStatus based on Integer32"""
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
        *(("authenticationFailure", 6),
          ("fDBAgingInitiatedLogout", 3),
          ("remoteAuthenticationServerFailure", 7),
          ("sessionRefreshInitiatedLogout", 5),
          ("sessionReset", 2),
          ("success", 1),
          ("userInitiatedLogout", 4))
    )


_ExtremeNetloginSessionStatus_Type.__name__ = "Integer32"
_ExtremeNetloginSessionStatus_Object = MibScalar
extremeNetloginSessionStatus = _ExtremeNetloginSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 14),
    _ExtremeNetloginSessionStatus_Type()
)
extremeNetloginSessionStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetloginSessionStatus.setStatus("current")
_ExtremeNMSTraps_ObjectIdentity = ObjectIdentity
extremeNMSTraps = _ExtremeNMSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4)
)
_ExtremeNMSTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeNMSTrapsPrefix = _ExtremeNMSTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 0)
)
_ExtremeNMSDeviceAddress_Type = IpAddress
_ExtremeNMSDeviceAddress_Object = MibScalar
extremeNMSDeviceAddress = _ExtremeNMSDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 1),
    _ExtremeNMSDeviceAddress_Type()
)
extremeNMSDeviceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNMSDeviceAddress.setStatus("current")
_ExtremeElrpTraps_ObjectIdentity = ObjectIdentity
extremeElrpTraps = _ExtremeElrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 6)
)
_ExtremeElrpTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeElrpTrapsPrefix = _ExtremeElrpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 6, 0)
)
_ExtremeEapsTraps_ObjectIdentity = ObjectIdentity
extremeEapsTraps = _ExtremeEapsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7)
)
_ExtremeEapsTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeEapsTrapsPrefix = _ExtremeEapsTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0)
)
_ExtremeEapsSharedLinkTraps_ObjectIdentity = ObjectIdentity
extremeEapsSharedLinkTraps = _ExtremeEapsSharedLinkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9)
)
_ExtremeEapsSharedLinkTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeEapsSharedLinkTrapsPrefix = _ExtremeEapsSharedLinkTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0)
)


class _ExtremeSegmentPort_Type(Integer32):
    """Custom type extremeSegmentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeSegmentPort_Type.__name__ = "Integer32"
_ExtremeSegmentPort_Object = MibScalar
extremeSegmentPort = _ExtremeSegmentPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 1),
    _ExtremeSegmentPort_Type()
)
extremeSegmentPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeSegmentPort.setStatus("current")


class _ExtremeSharedPort_Type(Integer32):
    """Custom type extremeSharedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeSharedPort_Type.__name__ = "Integer32"
_ExtremeSharedPort_Object = MibScalar
extremeSharedPort = _ExtremeSharedPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 2),
    _ExtremeSharedPort_Type()
)
extremeSharedPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeSharedPort.setStatus("current")
_ExtremePethTraps_ObjectIdentity = ObjectIdentity
extremePethTraps = _ExtremePethTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 12)
)
_ExtremePethNotificationPrefix_ObjectIdentity = ObjectIdentity
extremePethNotificationPrefix = _ExtremePethNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 12, 0)
)

# Managed Objects groups


# Notification objects

extremeHealthCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 1)
)
extremeHealthCheckFailed.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
        ("EXTREME-SYSTEM-MIB", "extremeHealthCheckErrorType"),
        ("EXTREME-SYSTEM-MIB", "extremeHealthCheckAction"),
        ("EXTREME-SYSTEM-MIB", "extremeHealthCheckMaxRetries"))
)
if mibBuilder.loadTexts:
    extremeHealthCheckFailed.setStatus(
        "current"
    )

extremeCpuUtilizationRisingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 2)
)
extremeCpuUtilizationRisingTrap.setObjects(
      *(("EXTREME-SYSTEM-MIB", "extremeCpuTaskUtilPair"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuAggregateUtilization"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuUtilRisingThreshold"))
)
if mibBuilder.loadTexts:
    extremeCpuUtilizationRisingTrap.setStatus(
        "current"
    )

extremeCpuUtilizationFallingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 3)
)
extremeCpuUtilizationFallingTrap.setObjects(
      *(("EXTREME-SYSTEM-MIB", "extremeCpuTaskUtilPair"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuAggregateUtilization"),
        ("EXTREME-SYSTEM-MIB", "extremeCpuUtilRisingThreshold"))
)
if mibBuilder.loadTexts:
    extremeCpuUtilizationFallingTrap.setStatus(
        "current"
    )

extremeProcessorStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 4)
)
extremeProcessorStateChangeTrap.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
        ("EXTREME-NP-MIB", "extremeNPModuleProcessorState"))
)
if mibBuilder.loadTexts:
    extremeProcessorStateChangeTrap.setStatus(
        "current"
    )

extremeMsmFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 5)
)
extremeMsmFailoverTrap.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeMasterMSMSlot"),
        ("EXTREME-SYSTEM-MIB", "extremeMsmFailoverCause"))
)
if mibBuilder.loadTexts:
    extremeMsmFailoverTrap.setStatus(
        "current"
    )

extremeEsrpTimedOutFailedOverMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 6)
)
extremeEsrpTimedOutFailedOverMaster.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
        ("EXTREME-VLAN-MIB", "extremeVlanIfDescr"),
        ("EXTREME-ESRP-MIB", "extremeEsrpState"))
)
if mibBuilder.loadTexts:
    extremeEsrpTimedOutFailedOverMaster.setStatus(
        "current"
    )

extremeRateLimitExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 1, 0, 7)
)
extremeRateLimitExceededTrap.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeRateLimitExceededTrapType"),
        ("EXTREME-V2TRAP-MIB", "extremeRateLimitExceededTrapIndicator"),
        ("IF-MIB", "ifIndex"),
        ("EXTREME-QOS-MIB", "extremeIQosProfileIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeExceededByteCount"))
)
if mibBuilder.loadTexts:
    extremeRateLimitExceededTrap.setStatus(
        "current"
    )

extremeBgpPrefixReachedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2, 0, 1)
)
extremeBgpPrefixReachedThreshold.setObjects(
    ("BGP4-MIB", "bgpPeerRemoteAddr")
)
if mibBuilder.loadTexts:
    extremeBgpPrefixReachedThreshold.setStatus(
        "current"
    )

extremeBgpPrefixMaxExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 2, 0, 2)
)
extremeBgpPrefixMaxExceeded.setObjects(
    ("BGP4-MIB", "bgpPeerRemoteAddr")
)
if mibBuilder.loadTexts:
    extremeBgpPrefixMaxExceeded.setStatus(
        "current"
    )

extremeMacLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 1)
)
extremeMacLimitExceeded.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanDescr"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityMacAddress"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanId"))
)
if mibBuilder.loadTexts:
    extremeMacLimitExceeded.setStatus(
        "current"
    )

extremeUnauthorizedPortForMacDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 2)
)
extremeUnauthorizedPortForMacDetected.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanDescr"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanId"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityMacAddress"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityPortIfIndex"))
)
if mibBuilder.loadTexts:
    extremeUnauthorizedPortForMacDetected.setStatus(
        "current"
    )

extremeMacDetectedOnLockedPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 3)
)
extremeMacDetectedOnLockedPort.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanDescr"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityVlanId"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityMacAddress"),
        ("EXTREME-V2TRAP-MIB", "extremeMacSecurityPortIfIndex"))
)
if mibBuilder.loadTexts:
    extremeMacDetectedOnLockedPort.setStatus(
        "current"
    )

extremeNetloginUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 4)
)
extremeNetloginUserLogin.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeNetloginStationMac"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginStationAddr"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginAuthType"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSystemTime"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginUser"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSrcVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginDestVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSessionStatus"))
)
if mibBuilder.loadTexts:
    extremeNetloginUserLogin.setStatus(
        "current"
    )

extremeNetloginUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 5)
)
extremeNetloginUserLogout.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeNetloginStationMac"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginStationAddr"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginAuthType"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSystemTime"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginUser"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSrcVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginDestVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSessionStatus"))
)
if mibBuilder.loadTexts:
    extremeNetloginUserLogout.setStatus(
        "current"
    )

extremeNetloginAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 3, 0, 6)
)
extremeNetloginAuthFailure.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeNetloginStationMac"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginStationAddr"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginPortIfIndex"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginAuthType"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSystemTime"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginUser"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSrcVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginDestVlan"),
        ("EXTREME-V2TRAP-MIB", "extremeNetloginSessionStatus"))
)
if mibBuilder.loadTexts:
    extremeNetloginAuthFailure.setStatus(
        "current"
    )

extremeNMSInventoryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 0, 1)
)
extremeNMSInventoryChanged.setObjects(
    ("EXTREME-V2TRAP-MIB", "extremeNMSDeviceAddress")
)
if mibBuilder.loadTexts:
    extremeNMSInventoryChanged.setStatus(
        "current"
    )

extremeNMSTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 4, 0, 2)
)
if mibBuilder.loadTexts:
    extremeNMSTopologyChanged.setStatus(
        "current"
    )

extremeElrpVlanLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 6, 0, 1)
)
extremeElrpVlanLoopDetected.setObjects(
    ("EXTREME-VLAN-MIB", "extremeVlanIfDescr")
)
if mibBuilder.loadTexts:
    extremeElrpVlanLoopDetected.setStatus(
        "current"
    )

extremeEapsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 1)
)
extremeEapsStateChange.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"))
)
if mibBuilder.loadTexts:
    extremeEapsStateChange.setStatus(
        "current"
    )

extremeEapsFailTimerExpFlagSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 2)
)
extremeEapsFailTimerExpFlagSet.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"))
)
if mibBuilder.loadTexts:
    extremeEapsFailTimerExpFlagSet.setStatus(
        "current"
    )

extremeEapsFailTimerExpFlagClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 3)
)
extremeEapsFailTimerExpFlagClear.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"))
)
if mibBuilder.loadTexts:
    extremeEapsFailTimerExpFlagClear.setStatus(
        "current"
    )

extremeEapsLinkDownRingComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 7, 0, 4)
)
extremeEapsLinkDownRingComplete.setObjects(
      *(("EXTREME-EAPS-MIB", "extremeEapsName"),
        ("EXTREME-EAPS-MIB", "extremeEapsMode"),
        ("EXTREME-EAPS-MIB", "extremeEapsPrevState"),
        ("EXTREME-EAPS-MIB", "extremeEapsState"))
)
if mibBuilder.loadTexts:
    extremeEapsLinkDownRingComplete.setStatus(
        "current"
    )

extremeEapsSegmentTimerExpFlagSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0, 1)
)
extremeEapsSegmentTimerExpFlagSet.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeSegmentPort"),
        ("EXTREME-V2TRAP-MIB", "extremeSharedPort"))
)
if mibBuilder.loadTexts:
    extremeEapsSegmentTimerExpFlagSet.setStatus(
        "current"
    )

extremeEapsSegmentTimerExpFlagClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 9, 0, 2)
)
extremeEapsSegmentTimerExpFlagClear.setObjects(
      *(("EXTREME-V2TRAP-MIB", "extremeSegmentPort"),
        ("EXTREME-V2TRAP-MIB", "extremeSharedPort"))
)
if mibBuilder.loadTexts:
    extremeEapsSegmentTimerExpFlagClear.setStatus(
        "current"
    )

extremePethPSUStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 12, 0, 1)
)
extremePethPSUStatusNotification.setObjects(
      *(("EXTREME-POE-MIB", "extremePethSlotPSUActive"),
        ("EXTREME-POE-MIB", "extremePethSlotMainPseIndex"))
)
if mibBuilder.loadTexts:
    extremePethPSUStatusNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-V2TRAP-MIB",
    **{"extremeCoreSCTraps": extremeCoreSCTraps,
       "extremeCoreSCTrapPrefix": extremeCoreSCTrapPrefix,
       "extremeHealthCheckFailed": extremeHealthCheckFailed,
       "extremeCpuUtilizationRisingTrap": extremeCpuUtilizationRisingTrap,
       "extremeCpuUtilizationFallingTrap": extremeCpuUtilizationFallingTrap,
       "extremeProcessorStateChangeTrap": extremeProcessorStateChangeTrap,
       "extremeMsmFailoverTrap": extremeMsmFailoverTrap,
       "extremeEsrpTimedOutFailedOverMaster": extremeEsrpTimedOutFailedOverMaster,
       "extremeRateLimitExceededTrap": extremeRateLimitExceededTrap,
       "extremeRateLimitExceededTrapType": extremeRateLimitExceededTrapType,
       "extremeRateLimitExceededTrapIndicator": extremeRateLimitExceededTrapIndicator,
       "extremeExceededByteCount": extremeExceededByteCount,
       "extremeBgpTraps": extremeBgpTraps,
       "extremeBgpTrapsPrefix": extremeBgpTrapsPrefix,
       "extremeBgpPrefixReachedThreshold": extremeBgpPrefixReachedThreshold,
       "extremeBgpPrefixMaxExceeded": extremeBgpPrefixMaxExceeded,
       "extremeSecurityTraps": extremeSecurityTraps,
       "extremeSecurityTrapsPrefix": extremeSecurityTrapsPrefix,
       "extremeMacLimitExceeded": extremeMacLimitExceeded,
       "extremeUnauthorizedPortForMacDetected": extremeUnauthorizedPortForMacDetected,
       "extremeMacDetectedOnLockedPort": extremeMacDetectedOnLockedPort,
       "extremeNetloginUserLogin": extremeNetloginUserLogin,
       "extremeNetloginUserLogout": extremeNetloginUserLogout,
       "extremeNetloginAuthFailure": extremeNetloginAuthFailure,
       "extremeMacSecurityVlanIfIndex": extremeMacSecurityVlanIfIndex,
       "extremeMacSecurityVlanDescr": extremeMacSecurityVlanDescr,
       "extremeMacSecurityMacAddress": extremeMacSecurityMacAddress,
       "extremeMacSecurityPortIfIndex": extremeMacSecurityPortIfIndex,
       "extremeMacSecurityVlanId": extremeMacSecurityVlanId,
       "extremeNetloginStationMac": extremeNetloginStationMac,
       "extremeNetloginStationAddr": extremeNetloginStationAddr,
       "extremeNetloginPortIfIndex": extremeNetloginPortIfIndex,
       "extremeNetloginAuthType": extremeNetloginAuthType,
       "extremeNetloginSystemTime": extremeNetloginSystemTime,
       "extremeNetloginUser": extremeNetloginUser,
       "extremeNetloginSrcVlan": extremeNetloginSrcVlan,
       "extremeNetloginDestVlan": extremeNetloginDestVlan,
       "extremeNetloginSessionStatus": extremeNetloginSessionStatus,
       "extremeNMSTraps": extremeNMSTraps,
       "extremeNMSTrapsPrefix": extremeNMSTrapsPrefix,
       "extremeNMSInventoryChanged": extremeNMSInventoryChanged,
       "extremeNMSTopologyChanged": extremeNMSTopologyChanged,
       "extremeNMSDeviceAddress": extremeNMSDeviceAddress,
       "extremeElrpTraps": extremeElrpTraps,
       "extremeElrpTrapsPrefix": extremeElrpTrapsPrefix,
       "extremeElrpVlanLoopDetected": extremeElrpVlanLoopDetected,
       "extremeEapsTraps": extremeEapsTraps,
       "extremeEapsTrapsPrefix": extremeEapsTrapsPrefix,
       "extremeEapsStateChange": extremeEapsStateChange,
       "extremeEapsFailTimerExpFlagSet": extremeEapsFailTimerExpFlagSet,
       "extremeEapsFailTimerExpFlagClear": extremeEapsFailTimerExpFlagClear,
       "extremeEapsLinkDownRingComplete": extremeEapsLinkDownRingComplete,
       "extremeEapsSharedLinkTraps": extremeEapsSharedLinkTraps,
       "extremeEapsSharedLinkTrapsPrefix": extremeEapsSharedLinkTrapsPrefix,
       "extremeEapsSegmentTimerExpFlagSet": extremeEapsSegmentTimerExpFlagSet,
       "extremeEapsSegmentTimerExpFlagClear": extremeEapsSegmentTimerExpFlagClear,
       "extremeSegmentPort": extremeSegmentPort,
       "extremeSharedPort": extremeSharedPort,
       "extremePethTraps": extremePethTraps,
       "extremePethNotificationPrefix": extremePethNotificationPrefix,
       "extremePethPSUStatusNotification": extremePethPSUStatusNotification}
)
