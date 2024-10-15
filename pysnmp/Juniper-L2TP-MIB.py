# SNMP MIB module (Juniper-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:43 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

juniL2tpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35)
)
juniL2tpMIB.setRevisions(
        ("2006-04-20 18:04",
         "2005-08-24 16:00",
         "2005-04-11 18:22",
         "2004-09-02 23:47",
         "2004-05-04 14:31",
         "2004-03-08 18:04",
         "2004-03-08 18:04",
         "2003-02-13 21:12",
         "2003-02-12 21:03",
         "2003-02-07 22:26",
         "2001-10-17 14:51",
         "2001-10-17 13:55",
         "2001-06-18 20:00",
         "2000-02-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniL2tpTunnelId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class JuniL2tpSessionId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class JuniL2tpAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("drain", 2),
          ("enabled", 0))
    )



class JuniL2tpTransport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("udpIp", 1))
    )



class JuniL2tpLockoutAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("test", 1),
          ("unlock", 2))
    )



class JuniL2tpLockoutState(Integer32, TextualConvention):
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
        *(("notLocked", 0),
          ("testing", 3),
          ("waitLockTimeout", 1),
          ("waitTestStart", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JuniL2tpTraps_ObjectIdentity = ObjectIdentity
juniL2tpTraps = _JuniL2tpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 0)
)
_JuniL2tpObjects_ObjectIdentity = ObjectIdentity
juniL2tpObjects = _JuniL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1)
)
_JuniL2tpSystem_ObjectIdentity = ObjectIdentity
juniL2tpSystem = _JuniL2tpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1)
)
_JuniL2tpSystemConfig_ObjectIdentity = ObjectIdentity
juniL2tpSystemConfig = _JuniL2tpSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1)
)
_JuniL2tpSysConfigAdminState_Type = JuniL2tpAdminState
_JuniL2tpSysConfigAdminState_Object = MibScalar
juniL2tpSysConfigAdminState = _JuniL2tpSysConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 1),
    _JuniL2tpSysConfigAdminState_Type()
)
juniL2tpSysConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigAdminState.setStatus("current")


class _JuniL2tpSysConfigDestructTimeout_Type(Integer32):
    """Custom type juniL2tpSysConfigDestructTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_JuniL2tpSysConfigDestructTimeout_Type.__name__ = "Integer32"
_JuniL2tpSysConfigDestructTimeout_Object = MibScalar
juniL2tpSysConfigDestructTimeout = _JuniL2tpSysConfigDestructTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 2),
    _JuniL2tpSysConfigDestructTimeout_Type()
)
juniL2tpSysConfigDestructTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigDestructTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniL2tpSysConfigDestructTimeout.setUnits("seconds")
_JuniL2tpSysConfigIpChecksumEnable_Type = JuniEnable
_JuniL2tpSysConfigIpChecksumEnable_Object = MibScalar
juniL2tpSysConfigIpChecksumEnable = _JuniL2tpSysConfigIpChecksumEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 3),
    _JuniL2tpSysConfigIpChecksumEnable_Type()
)
juniL2tpSysConfigIpChecksumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigIpChecksumEnable.setStatus("current")


class _JuniL2tpSysConfigTunnelSwitchingEnabled_Type(JuniEnable):
    """Custom type juniL2tpSysConfigTunnelSwitchingEnabled based on JuniEnable"""


_JuniL2tpSysConfigTunnelSwitchingEnabled_Object = MibScalar
juniL2tpSysConfigTunnelSwitchingEnabled = _JuniL2tpSysConfigTunnelSwitchingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 4),
    _JuniL2tpSysConfigTunnelSwitchingEnabled_Type()
)
juniL2tpSysConfigTunnelSwitchingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigTunnelSwitchingEnabled.setStatus("current")


class _JuniL2tpSysConfigControlRetransmissions_Type(Integer32):
    """Custom type juniL2tpSysConfigControlRetransmissions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_JuniL2tpSysConfigControlRetransmissions_Type.__name__ = "Integer32"
_JuniL2tpSysConfigControlRetransmissions_Object = MibScalar
juniL2tpSysConfigControlRetransmissions = _JuniL2tpSysConfigControlRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 5),
    _JuniL2tpSysConfigControlRetransmissions_Type()
)
juniL2tpSysConfigControlRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigControlRetransmissions.setStatus("deprecated")


class _JuniL2tpSysConfigTunnelIdleTimeout_Type(Integer32):
    """Custom type juniL2tpSysConfigTunnelIdleTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniL2tpSysConfigTunnelIdleTimeout_Type.__name__ = "Integer32"
_JuniL2tpSysConfigTunnelIdleTimeout_Object = MibScalar
juniL2tpSysConfigTunnelIdleTimeout = _JuniL2tpSysConfigTunnelIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 6),
    _JuniL2tpSysConfigTunnelIdleTimeout_Type()
)
juniL2tpSysConfigTunnelIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigTunnelIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniL2tpSysConfigTunnelIdleTimeout.setUnits("seconds")
_JuniL2tpSysConfigReceiveDataSequencingIgnore_Type = JuniEnable
_JuniL2tpSysConfigReceiveDataSequencingIgnore_Object = MibScalar
juniL2tpSysConfigReceiveDataSequencingIgnore = _JuniL2tpSysConfigReceiveDataSequencingIgnore_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 7),
    _JuniL2tpSysConfigReceiveDataSequencingIgnore_Type()
)
juniL2tpSysConfigReceiveDataSequencingIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigReceiveDataSequencingIgnore.setStatus("current")
_JuniL2tpSysConfigFailoverWithinPreference_Type = JuniEnable
_JuniL2tpSysConfigFailoverWithinPreference_Object = MibScalar
juniL2tpSysConfigFailoverWithinPreference = _JuniL2tpSysConfigFailoverWithinPreference_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 8),
    _JuniL2tpSysConfigFailoverWithinPreference_Type()
)
juniL2tpSysConfigFailoverWithinPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigFailoverWithinPreference.setStatus("current")
_JuniL2tpSysConfigWeightedLoadBalancing_Type = JuniEnable
_JuniL2tpSysConfigWeightedLoadBalancing_Object = MibScalar
juniL2tpSysConfigWeightedLoadBalancing = _JuniL2tpSysConfigWeightedLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 9),
    _JuniL2tpSysConfigWeightedLoadBalancing_Type()
)
juniL2tpSysConfigWeightedLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigWeightedLoadBalancing.setStatus("current")


class _JuniL2tpSysConfigControlRetransmissionsEstablished_Type(Integer32):
    """Custom type juniL2tpSysConfigControlRetransmissionsEstablished based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_JuniL2tpSysConfigControlRetransmissionsEstablished_Type.__name__ = "Integer32"
_JuniL2tpSysConfigControlRetransmissionsEstablished_Object = MibScalar
juniL2tpSysConfigControlRetransmissionsEstablished = _JuniL2tpSysConfigControlRetransmissionsEstablished_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 10),
    _JuniL2tpSysConfigControlRetransmissionsEstablished_Type()
)
juniL2tpSysConfigControlRetransmissionsEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigControlRetransmissionsEstablished.setStatus("current")


class _JuniL2tpSysConfigControlRetransmissionsNotEstablished_Type(Integer32):
    """Custom type juniL2tpSysConfigControlRetransmissionsNotEstablished based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_JuniL2tpSysConfigControlRetransmissionsNotEstablished_Type.__name__ = "Integer32"
_JuniL2tpSysConfigControlRetransmissionsNotEstablished_Object = MibScalar
juniL2tpSysConfigControlRetransmissionsNotEstablished = _JuniL2tpSysConfigControlRetransmissionsNotEstablished_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 11),
    _JuniL2tpSysConfigControlRetransmissionsNotEstablished_Type()
)
juniL2tpSysConfigControlRetransmissionsNotEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigControlRetransmissionsNotEstablished.setStatus("current")


class _JuniL2tpSysConfigDisableChallenge_Type(JuniEnable):
    """Custom type juniL2tpSysConfigDisableChallenge based on JuniEnable"""


_JuniL2tpSysConfigDisableChallenge_Object = MibScalar
juniL2tpSysConfigDisableChallenge = _JuniL2tpSysConfigDisableChallenge_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 12),
    _JuniL2tpSysConfigDisableChallenge_Type()
)
juniL2tpSysConfigDisableChallenge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigDisableChallenge.setStatus("current")
_JuniL2tpSysConfigDisableCallingNumberAvp_Type = JuniEnable
_JuniL2tpSysConfigDisableCallingNumberAvp_Object = MibScalar
juniL2tpSysConfigDisableCallingNumberAvp = _JuniL2tpSysConfigDisableCallingNumberAvp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 13),
    _JuniL2tpSysConfigDisableCallingNumberAvp_Type()
)
juniL2tpSysConfigDisableCallingNumberAvp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigDisableCallingNumberAvp.setStatus("current")


class _JuniL2tpSysConfigIgnoreTxAddressChange_Type(Integer32):
    """Custom type juniL2tpSysConfigIgnoreTxAddressChange based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("ipAddress", 2),
          ("ipAddressAndUdpPort", 1),
          ("udpPort", 3))
    )


_JuniL2tpSysConfigIgnoreTxAddressChange_Type.__name__ = "Integer32"
_JuniL2tpSysConfigIgnoreTxAddressChange_Object = MibScalar
juniL2tpSysConfigIgnoreTxAddressChange = _JuniL2tpSysConfigIgnoreTxAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 14),
    _JuniL2tpSysConfigIgnoreTxAddressChange_Type()
)
juniL2tpSysConfigIgnoreTxAddressChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigIgnoreTxAddressChange.setStatus("current")


class _JuniL2tpSysConfigEnableDisconnectCauseAvp_Type(JuniEnable):
    """Custom type juniL2tpSysConfigEnableDisconnectCauseAvp based on JuniEnable"""


_JuniL2tpSysConfigEnableDisconnectCauseAvp_Object = MibScalar
juniL2tpSysConfigEnableDisconnectCauseAvp = _JuniL2tpSysConfigEnableDisconnectCauseAvp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 15),
    _JuniL2tpSysConfigEnableDisconnectCauseAvp_Type()
)
juniL2tpSysConfigEnableDisconnectCauseAvp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigEnableDisconnectCauseAvp.setStatus("current")


class _JuniL2tpSysConfigReceiveWindowSize_Type(Integer32):
    """Custom type juniL2tpSysConfigReceiveWindowSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 4),
    )


_JuniL2tpSysConfigReceiveWindowSize_Type.__name__ = "Integer32"
_JuniL2tpSysConfigReceiveWindowSize_Object = MibScalar
juniL2tpSysConfigReceiveWindowSize = _JuniL2tpSysConfigReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 16),
    _JuniL2tpSysConfigReceiveWindowSize_Type()
)
juniL2tpSysConfigReceiveWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigReceiveWindowSize.setStatus("current")


class _JuniL2tpSysConfigEnableRxSpeedAvpWhenEqual_Type(JuniEnable):
    """Custom type juniL2tpSysConfigEnableRxSpeedAvpWhenEqual based on JuniEnable"""


_JuniL2tpSysConfigEnableRxSpeedAvpWhenEqual_Object = MibScalar
juniL2tpSysConfigEnableRxSpeedAvpWhenEqual = _JuniL2tpSysConfigEnableRxSpeedAvpWhenEqual_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 17),
    _JuniL2tpSysConfigEnableRxSpeedAvpWhenEqual_Type()
)
juniL2tpSysConfigEnableRxSpeedAvpWhenEqual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigEnableRxSpeedAvpWhenEqual.setStatus("current")


class _JuniL2tpSysConfigRejectTxAddressChange_Type(Integer32):
    """Custom type juniL2tpSysConfigRejectTxAddressChange based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("ipAddress", 2),
          ("ipAddressAndUdpPort", 1),
          ("udpPort", 3))
    )


_JuniL2tpSysConfigRejectTxAddressChange_Type.__name__ = "Integer32"
_JuniL2tpSysConfigRejectTxAddressChange_Object = MibScalar
juniL2tpSysConfigRejectTxAddressChange = _JuniL2tpSysConfigRejectTxAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 18),
    _JuniL2tpSysConfigRejectTxAddressChange_Type()
)
juniL2tpSysConfigRejectTxAddressChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigRejectTxAddressChange.setStatus("current")


class _JuniL2tpSysConfigShortDrainTimeout_Type(Integer32):
    """Custom type juniL2tpSysConfigShortDrainTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_JuniL2tpSysConfigShortDrainTimeout_Type.__name__ = "Integer32"
_JuniL2tpSysConfigShortDrainTimeout_Object = MibScalar
juniL2tpSysConfigShortDrainTimeout = _JuniL2tpSysConfigShortDrainTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 19),
    _JuniL2tpSysConfigShortDrainTimeout_Type()
)
juniL2tpSysConfigShortDrainTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigShortDrainTimeout.setStatus("current")


class _JuniL2tpSysConfigDestinationLockoutTestEnabled_Type(JuniEnable):
    """Custom type juniL2tpSysConfigDestinationLockoutTestEnabled based on JuniEnable"""


_JuniL2tpSysConfigDestinationLockoutTestEnabled_Object = MibScalar
juniL2tpSysConfigDestinationLockoutTestEnabled = _JuniL2tpSysConfigDestinationLockoutTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 20),
    _JuniL2tpSysConfigDestinationLockoutTestEnabled_Type()
)
juniL2tpSysConfigDestinationLockoutTestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigDestinationLockoutTestEnabled.setStatus("current")


class _JuniL2tpSysConfigDestinationLockoutTimeout_Type(Integer32):
    """Custom type juniL2tpSysConfigDestinationLockoutTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_JuniL2tpSysConfigDestinationLockoutTimeout_Type.__name__ = "Integer32"
_JuniL2tpSysConfigDestinationLockoutTimeout_Object = MibScalar
juniL2tpSysConfigDestinationLockoutTimeout = _JuniL2tpSysConfigDestinationLockoutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 21),
    _JuniL2tpSysConfigDestinationLockoutTimeout_Type()
)
juniL2tpSysConfigDestinationLockoutTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigDestinationLockoutTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniL2tpSysConfigDestinationLockoutTimeout.setUnits("seconds")


class _JuniL2tpSysConfigFailoverResync_Type(Integer32):
    """Custom type juniL2tpSysConfigFailoverResync based on Integer32"""
    defaultValue = 3

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
        *(("disable", 0),
          ("failoverProtocol", 1),
          ("failoverProtocolFallbackToSilentFailover", 3),
          ("silentFailover", 2))
    )


_JuniL2tpSysConfigFailoverResync_Type.__name__ = "Integer32"
_JuniL2tpSysConfigFailoverResync_Object = MibScalar
juniL2tpSysConfigFailoverResync = _JuniL2tpSysConfigFailoverResync_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 22),
    _JuniL2tpSysConfigFailoverResync_Type()
)
juniL2tpSysConfigFailoverResync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniL2tpSysConfigFailoverResync.setStatus("current")
_JuniL2tpSystemStatus_ObjectIdentity = ObjectIdentity
juniL2tpSystemStatus = _JuniL2tpSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2)
)


class _JuniL2tpSysStatusProtocolVersion_Type(OctetString):
    """Custom type juniL2tpSysStatusProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_JuniL2tpSysStatusProtocolVersion_Type.__name__ = "OctetString"
_JuniL2tpSysStatusProtocolVersion_Object = MibScalar
juniL2tpSysStatusProtocolVersion = _JuniL2tpSysStatusProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 1),
    _JuniL2tpSysStatusProtocolVersion_Type()
)
juniL2tpSysStatusProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusProtocolVersion.setStatus("current")
_JuniL2tpSysStatusVendorName_Type = DisplayString
_JuniL2tpSysStatusVendorName_Object = MibScalar
juniL2tpSysStatusVendorName = _JuniL2tpSysStatusVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 2),
    _JuniL2tpSysStatusVendorName_Type()
)
juniL2tpSysStatusVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusVendorName.setStatus("current")
_JuniL2tpSysStatusFirmwareRev_Type = Integer32
_JuniL2tpSysStatusFirmwareRev_Object = MibScalar
juniL2tpSysStatusFirmwareRev = _JuniL2tpSysStatusFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 3),
    _JuniL2tpSysStatusFirmwareRev_Type()
)
juniL2tpSysStatusFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusFirmwareRev.setStatus("current")
_JuniL2tpSysStatusTotalDestinations_Type = Counter32
_JuniL2tpSysStatusTotalDestinations_Object = MibScalar
juniL2tpSysStatusTotalDestinations = _JuniL2tpSysStatusTotalDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 4),
    _JuniL2tpSysStatusTotalDestinations_Type()
)
juniL2tpSysStatusTotalDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusTotalDestinations.setStatus("current")
_JuniL2tpSysStatusFailedDestinations_Type = Counter32
_JuniL2tpSysStatusFailedDestinations_Object = MibScalar
juniL2tpSysStatusFailedDestinations = _JuniL2tpSysStatusFailedDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 5),
    _JuniL2tpSysStatusFailedDestinations_Type()
)
juniL2tpSysStatusFailedDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusFailedDestinations.setStatus("current")
_JuniL2tpSysStatusActiveDestinations_Type = Gauge32
_JuniL2tpSysStatusActiveDestinations_Object = MibScalar
juniL2tpSysStatusActiveDestinations = _JuniL2tpSysStatusActiveDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 6),
    _JuniL2tpSysStatusActiveDestinations_Type()
)
juniL2tpSysStatusActiveDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusActiveDestinations.setStatus("current")
_JuniL2tpSysStatusTotalTunnels_Type = Counter32
_JuniL2tpSysStatusTotalTunnels_Object = MibScalar
juniL2tpSysStatusTotalTunnels = _JuniL2tpSysStatusTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 7),
    _JuniL2tpSysStatusTotalTunnels_Type()
)
juniL2tpSysStatusTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusTotalTunnels.setStatus("current")
_JuniL2tpSysStatusFailedTunnels_Type = Counter32
_JuniL2tpSysStatusFailedTunnels_Object = MibScalar
juniL2tpSysStatusFailedTunnels = _JuniL2tpSysStatusFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 8),
    _JuniL2tpSysStatusFailedTunnels_Type()
)
juniL2tpSysStatusFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusFailedTunnels.setStatus("current")
_JuniL2tpSysStatusFailedTunnelAuthens_Type = Counter32
_JuniL2tpSysStatusFailedTunnelAuthens_Object = MibScalar
juniL2tpSysStatusFailedTunnelAuthens = _JuniL2tpSysStatusFailedTunnelAuthens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 9),
    _JuniL2tpSysStatusFailedTunnelAuthens_Type()
)
juniL2tpSysStatusFailedTunnelAuthens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusFailedTunnelAuthens.setStatus("current")
_JuniL2tpSysStatusActiveTunnels_Type = Gauge32
_JuniL2tpSysStatusActiveTunnels_Object = MibScalar
juniL2tpSysStatusActiveTunnels = _JuniL2tpSysStatusActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 10),
    _JuniL2tpSysStatusActiveTunnels_Type()
)
juniL2tpSysStatusActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusActiveTunnels.setStatus("current")
_JuniL2tpSysStatusTotalSessions_Type = Counter32
_JuniL2tpSysStatusTotalSessions_Object = MibScalar
juniL2tpSysStatusTotalSessions = _JuniL2tpSysStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 11),
    _JuniL2tpSysStatusTotalSessions_Type()
)
juniL2tpSysStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusTotalSessions.setStatus("current")
_JuniL2tpSysStatusFailedSessions_Type = Counter32
_JuniL2tpSysStatusFailedSessions_Object = MibScalar
juniL2tpSysStatusFailedSessions = _JuniL2tpSysStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 12),
    _JuniL2tpSysStatusFailedSessions_Type()
)
juniL2tpSysStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusFailedSessions.setStatus("current")
_JuniL2tpSysStatusActiveSessions_Type = Gauge32
_JuniL2tpSysStatusActiveSessions_Object = MibScalar
juniL2tpSysStatusActiveSessions = _JuniL2tpSysStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 13),
    _JuniL2tpSysStatusActiveSessions_Type()
)
juniL2tpSysStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusActiveSessions.setStatus("current")
_JuniL2tpSysStatusTotalSwitchedSessions_Type = Counter32
_JuniL2tpSysStatusTotalSwitchedSessions_Object = MibScalar
juniL2tpSysStatusTotalSwitchedSessions = _JuniL2tpSysStatusTotalSwitchedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 14),
    _JuniL2tpSysStatusTotalSwitchedSessions_Type()
)
juniL2tpSysStatusTotalSwitchedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusTotalSwitchedSessions.setStatus("current")
_JuniL2tpSysStatusFailedSwitchedSessions_Type = Counter32
_JuniL2tpSysStatusFailedSwitchedSessions_Object = MibScalar
juniL2tpSysStatusFailedSwitchedSessions = _JuniL2tpSysStatusFailedSwitchedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 15),
    _JuniL2tpSysStatusFailedSwitchedSessions_Type()
)
juniL2tpSysStatusFailedSwitchedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusFailedSwitchedSessions.setStatus("current")
_JuniL2tpSysStatusActiveSwitchedSessions_Type = Gauge32
_JuniL2tpSysStatusActiveSwitchedSessions_Object = MibScalar
juniL2tpSysStatusActiveSwitchedSessions = _JuniL2tpSysStatusActiveSwitchedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 16),
    _JuniL2tpSysStatusActiveSwitchedSessions_Type()
)
juniL2tpSysStatusActiveSwitchedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusActiveSwitchedSessions.setStatus("current")
_JuniL2tpSysStatusIfCounterDiscontinuityTime_Type = TimeStamp
_JuniL2tpSysStatusIfCounterDiscontinuityTime_Object = MibScalar
juniL2tpSysStatusIfCounterDiscontinuityTime = _JuniL2tpSysStatusIfCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 17),
    _JuniL2tpSysStatusIfCounterDiscontinuityTime_Type()
)
juniL2tpSysStatusIfCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSysStatusIfCounterDiscontinuityTime.setStatus("current")
_JuniL2tpDestination_ObjectIdentity = ObjectIdentity
juniL2tpDestination = _JuniL2tpDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2)
)
_JuniL2tpDestConfig_ObjectIdentity = ObjectIdentity
juniL2tpDestConfig = _JuniL2tpDestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1)
)
_JuniL2tpDestConfigTable_Object = MibTable
juniL2tpDestConfigTable = _JuniL2tpDestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniL2tpDestConfigTable.setStatus("current")
_JuniL2tpDestConfigEntry_Object = MibTableRow
juniL2tpDestConfigEntry = _JuniL2tpDestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1)
)
juniL2tpDestConfigEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpDestConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDestConfigEntry.setStatus("current")
_JuniL2tpDestConfigIfIndex_Type = InterfaceIndex
_JuniL2tpDestConfigIfIndex_Object = MibTableColumn
juniL2tpDestConfigIfIndex = _JuniL2tpDestConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1, 1),
    _JuniL2tpDestConfigIfIndex_Type()
)
juniL2tpDestConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDestConfigIfIndex.setStatus("current")
_JuniL2tpDestConfigRowStatus_Type = RowStatus
_JuniL2tpDestConfigRowStatus_Object = MibTableColumn
juniL2tpDestConfigRowStatus = _JuniL2tpDestConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1, 2),
    _JuniL2tpDestConfigRowStatus_Type()
)
juniL2tpDestConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDestConfigRowStatus.setStatus("current")


class _JuniL2tpDestConfigAdminState_Type(JuniL2tpAdminState):
    """Custom type juniL2tpDestConfigAdminState based on JuniL2tpAdminState"""


_JuniL2tpDestConfigAdminState_Object = MibTableColumn
juniL2tpDestConfigAdminState = _JuniL2tpDestConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1, 3),
    _JuniL2tpDestConfigAdminState_Type()
)
juniL2tpDestConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDestConfigAdminState.setStatus("current")


class _JuniL2tpDestConfigLockoutAction_Type(JuniL2tpLockoutAction):
    """Custom type juniL2tpDestConfigLockoutAction based on JuniL2tpLockoutAction"""


_JuniL2tpDestConfigLockoutAction_Object = MibTableColumn
juniL2tpDestConfigLockoutAction = _JuniL2tpDestConfigLockoutAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1, 4),
    _JuniL2tpDestConfigLockoutAction_Type()
)
juniL2tpDestConfigLockoutAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpDestConfigLockoutAction.setStatus("current")
_JuniL2tpDestStatus_ObjectIdentity = ObjectIdentity
juniL2tpDestStatus = _JuniL2tpDestStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2)
)
_JuniL2tpDestStatusTable_Object = MibTable
juniL2tpDestStatusTable = _JuniL2tpDestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    juniL2tpDestStatusTable.setStatus("current")
_JuniL2tpDestStatusEntry_Object = MibTableRow
juniL2tpDestStatusEntry = _JuniL2tpDestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1)
)
juniL2tpDestStatusEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpDestStatusIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDestStatusEntry.setStatus("current")
_JuniL2tpDestStatusIfIndex_Type = InterfaceIndex
_JuniL2tpDestStatusIfIndex_Object = MibTableColumn
juniL2tpDestStatusIfIndex = _JuniL2tpDestStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 1),
    _JuniL2tpDestStatusIfIndex_Type()
)
juniL2tpDestStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDestStatusIfIndex.setStatus("current")
_JuniL2tpDestStatusTransport_Type = JuniL2tpTransport
_JuniL2tpDestStatusTransport_Object = MibTableColumn
juniL2tpDestStatusTransport = _JuniL2tpDestStatusTransport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 2),
    _JuniL2tpDestStatusTransport_Type()
)
juniL2tpDestStatusTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusTransport.setStatus("current")
_JuniL2tpDestStatusEffectiveAdminState_Type = JuniL2tpAdminState
_JuniL2tpDestStatusEffectiveAdminState_Object = MibTableColumn
juniL2tpDestStatusEffectiveAdminState = _JuniL2tpDestStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 3),
    _JuniL2tpDestStatusEffectiveAdminState_Type()
)
juniL2tpDestStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusEffectiveAdminState.setStatus("current")
_JuniL2tpDestStatusTotalTunnels_Type = Counter32
_JuniL2tpDestStatusTotalTunnels_Object = MibTableColumn
juniL2tpDestStatusTotalTunnels = _JuniL2tpDestStatusTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 4),
    _JuniL2tpDestStatusTotalTunnels_Type()
)
juniL2tpDestStatusTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusTotalTunnels.setStatus("current")
_JuniL2tpDestStatusFailedTunnels_Type = Counter32
_JuniL2tpDestStatusFailedTunnels_Object = MibTableColumn
juniL2tpDestStatusFailedTunnels = _JuniL2tpDestStatusFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 5),
    _JuniL2tpDestStatusFailedTunnels_Type()
)
juniL2tpDestStatusFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusFailedTunnels.setStatus("current")
_JuniL2tpDestStatusFailedTunnelAuthens_Type = Counter32
_JuniL2tpDestStatusFailedTunnelAuthens_Object = MibTableColumn
juniL2tpDestStatusFailedTunnelAuthens = _JuniL2tpDestStatusFailedTunnelAuthens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 6),
    _JuniL2tpDestStatusFailedTunnelAuthens_Type()
)
juniL2tpDestStatusFailedTunnelAuthens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusFailedTunnelAuthens.setStatus("current")
_JuniL2tpDestStatusActiveTunnels_Type = Gauge32
_JuniL2tpDestStatusActiveTunnels_Object = MibTableColumn
juniL2tpDestStatusActiveTunnels = _JuniL2tpDestStatusActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 7),
    _JuniL2tpDestStatusActiveTunnels_Type()
)
juniL2tpDestStatusActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusActiveTunnels.setStatus("current")
_JuniL2tpDestStatusTotalSessions_Type = Counter32
_JuniL2tpDestStatusTotalSessions_Object = MibTableColumn
juniL2tpDestStatusTotalSessions = _JuniL2tpDestStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 8),
    _JuniL2tpDestStatusTotalSessions_Type()
)
juniL2tpDestStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusTotalSessions.setStatus("current")
_JuniL2tpDestStatusFailedSessions_Type = Counter32
_JuniL2tpDestStatusFailedSessions_Object = MibTableColumn
juniL2tpDestStatusFailedSessions = _JuniL2tpDestStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 9),
    _JuniL2tpDestStatusFailedSessions_Type()
)
juniL2tpDestStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusFailedSessions.setStatus("current")
_JuniL2tpDestStatusActiveSessions_Type = Gauge32
_JuniL2tpDestStatusActiveSessions_Object = MibTableColumn
juniL2tpDestStatusActiveSessions = _JuniL2tpDestStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 10),
    _JuniL2tpDestStatusActiveSessions_Type()
)
juniL2tpDestStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusActiveSessions.setStatus("current")
_JuniL2tpDestStatusLockoutState_Type = JuniL2tpLockoutState
_JuniL2tpDestStatusLockoutState_Object = MibTableColumn
juniL2tpDestStatusLockoutState = _JuniL2tpDestStatusLockoutState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 11),
    _JuniL2tpDestStatusLockoutState_Type()
)
juniL2tpDestStatusLockoutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusLockoutState.setStatus("current")
_JuniL2tpDestStatusLockoutTimeRemaining_Type = Gauge32
_JuniL2tpDestStatusLockoutTimeRemaining_Object = MibTableColumn
juniL2tpDestStatusLockoutTimeRemaining = _JuniL2tpDestStatusLockoutTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 12),
    _JuniL2tpDestStatusLockoutTimeRemaining_Type()
)
juniL2tpDestStatusLockoutTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatusLockoutTimeRemaining.setStatus("current")
_JuniL2tpDestStatistics_ObjectIdentity = ObjectIdentity
juniL2tpDestStatistics = _JuniL2tpDestStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3)
)
_JuniL2tpDestStatTable_Object = MibTable
juniL2tpDestStatTable = _JuniL2tpDestStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    juniL2tpDestStatTable.setStatus("current")
_JuniL2tpDestStatEntry_Object = MibTableRow
juniL2tpDestStatEntry = _JuniL2tpDestStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1)
)
juniL2tpDestStatEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpDestStatIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpDestStatEntry.setStatus("current")
_JuniL2tpDestStatIfIndex_Type = InterfaceIndex
_JuniL2tpDestStatIfIndex_Object = MibTableColumn
juniL2tpDestStatIfIndex = _JuniL2tpDestStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 1),
    _JuniL2tpDestStatIfIndex_Type()
)
juniL2tpDestStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpDestStatIfIndex.setStatus("current")
_JuniL2tpDestStatCtlRecvOctets_Type = Counter32
_JuniL2tpDestStatCtlRecvOctets_Object = MibTableColumn
juniL2tpDestStatCtlRecvOctets = _JuniL2tpDestStatCtlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 2),
    _JuniL2tpDestStatCtlRecvOctets_Type()
)
juniL2tpDestStatCtlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlRecvOctets.setStatus("current")
_JuniL2tpDestStatCtlRecvPackets_Type = Counter32
_JuniL2tpDestStatCtlRecvPackets_Object = MibTableColumn
juniL2tpDestStatCtlRecvPackets = _JuniL2tpDestStatCtlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 3),
    _JuniL2tpDestStatCtlRecvPackets_Type()
)
juniL2tpDestStatCtlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlRecvPackets.setStatus("current")
_JuniL2tpDestStatCtlRecvErrors_Type = Counter32
_JuniL2tpDestStatCtlRecvErrors_Object = MibTableColumn
juniL2tpDestStatCtlRecvErrors = _JuniL2tpDestStatCtlRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 4),
    _JuniL2tpDestStatCtlRecvErrors_Type()
)
juniL2tpDestStatCtlRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlRecvErrors.setStatus("current")
_JuniL2tpDestStatCtlRecvDiscards_Type = Counter32
_JuniL2tpDestStatCtlRecvDiscards_Object = MibTableColumn
juniL2tpDestStatCtlRecvDiscards = _JuniL2tpDestStatCtlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 5),
    _JuniL2tpDestStatCtlRecvDiscards_Type()
)
juniL2tpDestStatCtlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlRecvDiscards.setStatus("current")
_JuniL2tpDestStatCtlSendOctets_Type = Counter32
_JuniL2tpDestStatCtlSendOctets_Object = MibTableColumn
juniL2tpDestStatCtlSendOctets = _JuniL2tpDestStatCtlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 6),
    _JuniL2tpDestStatCtlSendOctets_Type()
)
juniL2tpDestStatCtlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlSendOctets.setStatus("current")
_JuniL2tpDestStatCtlSendPackets_Type = Counter32
_JuniL2tpDestStatCtlSendPackets_Object = MibTableColumn
juniL2tpDestStatCtlSendPackets = _JuniL2tpDestStatCtlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 7),
    _JuniL2tpDestStatCtlSendPackets_Type()
)
juniL2tpDestStatCtlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlSendPackets.setStatus("current")
_JuniL2tpDestStatCtlSendErrors_Type = Counter32
_JuniL2tpDestStatCtlSendErrors_Object = MibTableColumn
juniL2tpDestStatCtlSendErrors = _JuniL2tpDestStatCtlSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 8),
    _JuniL2tpDestStatCtlSendErrors_Type()
)
juniL2tpDestStatCtlSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlSendErrors.setStatus("current")
_JuniL2tpDestStatCtlSendDiscards_Type = Counter32
_JuniL2tpDestStatCtlSendDiscards_Object = MibTableColumn
juniL2tpDestStatCtlSendDiscards = _JuniL2tpDestStatCtlSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 9),
    _JuniL2tpDestStatCtlSendDiscards_Type()
)
juniL2tpDestStatCtlSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatCtlSendDiscards.setStatus("current")
_JuniL2tpDestStatPayRecvOctets_Type = Counter32
_JuniL2tpDestStatPayRecvOctets_Object = MibTableColumn
juniL2tpDestStatPayRecvOctets = _JuniL2tpDestStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 10),
    _JuniL2tpDestStatPayRecvOctets_Type()
)
juniL2tpDestStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPayRecvOctets.setStatus("current")
_JuniL2tpDestStatPayRecvPackets_Type = Counter32
_JuniL2tpDestStatPayRecvPackets_Object = MibTableColumn
juniL2tpDestStatPayRecvPackets = _JuniL2tpDestStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 11),
    _JuniL2tpDestStatPayRecvPackets_Type()
)
juniL2tpDestStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPayRecvPackets.setStatus("current")
_JuniL2tpDestStatPayRecvErrors_Type = Counter32
_JuniL2tpDestStatPayRecvErrors_Object = MibTableColumn
juniL2tpDestStatPayRecvErrors = _JuniL2tpDestStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 12),
    _JuniL2tpDestStatPayRecvErrors_Type()
)
juniL2tpDestStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPayRecvErrors.setStatus("current")
_JuniL2tpDestStatPayRecvDiscards_Type = Counter32
_JuniL2tpDestStatPayRecvDiscards_Object = MibTableColumn
juniL2tpDestStatPayRecvDiscards = _JuniL2tpDestStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 13),
    _JuniL2tpDestStatPayRecvDiscards_Type()
)
juniL2tpDestStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPayRecvDiscards.setStatus("current")
_JuniL2tpDestStatPaySendOctets_Type = Counter32
_JuniL2tpDestStatPaySendOctets_Object = MibTableColumn
juniL2tpDestStatPaySendOctets = _JuniL2tpDestStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 14),
    _JuniL2tpDestStatPaySendOctets_Type()
)
juniL2tpDestStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPaySendOctets.setStatus("current")
_JuniL2tpDestStatPaySendPackets_Type = Counter32
_JuniL2tpDestStatPaySendPackets_Object = MibTableColumn
juniL2tpDestStatPaySendPackets = _JuniL2tpDestStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 15),
    _JuniL2tpDestStatPaySendPackets_Type()
)
juniL2tpDestStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPaySendPackets.setStatus("current")
_JuniL2tpDestStatPaySendErrors_Type = Counter32
_JuniL2tpDestStatPaySendErrors_Object = MibTableColumn
juniL2tpDestStatPaySendErrors = _JuniL2tpDestStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 16),
    _JuniL2tpDestStatPaySendErrors_Type()
)
juniL2tpDestStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPaySendErrors.setStatus("current")
_JuniL2tpDestStatPaySendDiscards_Type = Counter32
_JuniL2tpDestStatPaySendDiscards_Object = MibTableColumn
juniL2tpDestStatPaySendDiscards = _JuniL2tpDestStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 17),
    _JuniL2tpDestStatPaySendDiscards_Type()
)
juniL2tpDestStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpDestStatPaySendDiscards.setStatus("current")
_JuniL2tpTunnel_ObjectIdentity = ObjectIdentity
juniL2tpTunnel = _JuniL2tpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3)
)
_JuniL2tpTunnelConfig_ObjectIdentity = ObjectIdentity
juniL2tpTunnelConfig = _JuniL2tpTunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1)
)
_JuniL2tpTunnelConfigTable_Object = MibTable
juniL2tpTunnelConfigTable = _JuniL2tpTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    juniL2tpTunnelConfigTable.setStatus("current")
_JuniL2tpTunnelConfigEntry_Object = MibTableRow
juniL2tpTunnelConfigEntry = _JuniL2tpTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1)
)
juniL2tpTunnelConfigEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpTunnelConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpTunnelConfigEntry.setStatus("current")
_JuniL2tpTunnelConfigIfIndex_Type = InterfaceIndex
_JuniL2tpTunnelConfigIfIndex_Object = MibTableColumn
juniL2tpTunnelConfigIfIndex = _JuniL2tpTunnelConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1, 1),
    _JuniL2tpTunnelConfigIfIndex_Type()
)
juniL2tpTunnelConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpTunnelConfigIfIndex.setStatus("current")
_JuniL2tpTunnelConfigRowStatus_Type = RowStatus
_JuniL2tpTunnelConfigRowStatus_Object = MibTableColumn
juniL2tpTunnelConfigRowStatus = _JuniL2tpTunnelConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1, 2),
    _JuniL2tpTunnelConfigRowStatus_Type()
)
juniL2tpTunnelConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpTunnelConfigRowStatus.setStatus("current")


class _JuniL2tpTunnelConfigAdminState_Type(JuniL2tpAdminState):
    """Custom type juniL2tpTunnelConfigAdminState based on JuniL2tpAdminState"""


_JuniL2tpTunnelConfigAdminState_Object = MibTableColumn
juniL2tpTunnelConfigAdminState = _JuniL2tpTunnelConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1, 3),
    _JuniL2tpTunnelConfigAdminState_Type()
)
juniL2tpTunnelConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpTunnelConfigAdminState.setStatus("current")
_JuniL2tpTunnelStatus_ObjectIdentity = ObjectIdentity
juniL2tpTunnelStatus = _JuniL2tpTunnelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2)
)
_JuniL2tpTunnelStatusTable_Object = MibTable
juniL2tpTunnelStatusTable = _JuniL2tpTunnelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusTable.setStatus("current")
_JuniL2tpTunnelStatusEntry_Object = MibTableRow
juniL2tpTunnelStatusEntry = _JuniL2tpTunnelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1)
)
juniL2tpTunnelStatusEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpTunnelStatusIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusEntry.setStatus("current")
_JuniL2tpTunnelStatusIfIndex_Type = InterfaceIndex
_JuniL2tpTunnelStatusIfIndex_Object = MibTableColumn
juniL2tpTunnelStatusIfIndex = _JuniL2tpTunnelStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 1),
    _JuniL2tpTunnelStatusIfIndex_Type()
)
juniL2tpTunnelStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusIfIndex.setStatus("current")
_JuniL2tpTunnelStatusTransport_Type = JuniL2tpTransport
_JuniL2tpTunnelStatusTransport_Object = MibTableColumn
juniL2tpTunnelStatusTransport = _JuniL2tpTunnelStatusTransport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 2),
    _JuniL2tpTunnelStatusTransport_Type()
)
juniL2tpTunnelStatusTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusTransport.setStatus("current")
_JuniL2tpTunnelStatusLocalTunnelId_Type = JuniL2tpTunnelId
_JuniL2tpTunnelStatusLocalTunnelId_Object = MibTableColumn
juniL2tpTunnelStatusLocalTunnelId = _JuniL2tpTunnelStatusLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 3),
    _JuniL2tpTunnelStatusLocalTunnelId_Type()
)
juniL2tpTunnelStatusLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusLocalTunnelId.setStatus("current")
_JuniL2tpTunnelStatusRemoteTunnelId_Type = JuniL2tpTunnelId
_JuniL2tpTunnelStatusRemoteTunnelId_Object = MibTableColumn
juniL2tpTunnelStatusRemoteTunnelId = _JuniL2tpTunnelStatusRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 4),
    _JuniL2tpTunnelStatusRemoteTunnelId_Type()
)
juniL2tpTunnelStatusRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRemoteTunnelId.setStatus("current")
_JuniL2tpTunnelStatusEffectiveAdminState_Type = JuniL2tpAdminState
_JuniL2tpTunnelStatusEffectiveAdminState_Object = MibTableColumn
juniL2tpTunnelStatusEffectiveAdminState = _JuniL2tpTunnelStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 5),
    _JuniL2tpTunnelStatusEffectiveAdminState_Type()
)
juniL2tpTunnelStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusEffectiveAdminState.setStatus("current")


class _JuniL2tpTunnelStatusState_Type(Integer32):
    """Custom type juniL2tpTunnelStatusState based on Integer32"""
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
        *(("connecting", 1),
          ("disconnecting", 3),
          ("established", 2),
          ("idle", 0))
    )


_JuniL2tpTunnelStatusState_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusState_Object = MibTableColumn
juniL2tpTunnelStatusState = _JuniL2tpTunnelStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 6),
    _JuniL2tpTunnelStatusState_Type()
)
juniL2tpTunnelStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusState.setStatus("current")


class _JuniL2tpTunnelStatusInitiated_Type(Integer32):
    """Custom type juniL2tpTunnelStatusInitiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 0),
          ("remote", 2))
    )


_JuniL2tpTunnelStatusInitiated_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusInitiated_Object = MibTableColumn
juniL2tpTunnelStatusInitiated = _JuniL2tpTunnelStatusInitiated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 7),
    _JuniL2tpTunnelStatusInitiated_Type()
)
juniL2tpTunnelStatusInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusInitiated.setStatus("current")
_JuniL2tpTunnelStatusRemoteHostName_Type = DisplayString
_JuniL2tpTunnelStatusRemoteHostName_Object = MibTableColumn
juniL2tpTunnelStatusRemoteHostName = _JuniL2tpTunnelStatusRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 8),
    _JuniL2tpTunnelStatusRemoteHostName_Type()
)
juniL2tpTunnelStatusRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRemoteHostName.setStatus("current")
_JuniL2tpTunnelStatusRemoteVendorName_Type = DisplayString
_JuniL2tpTunnelStatusRemoteVendorName_Object = MibTableColumn
juniL2tpTunnelStatusRemoteVendorName = _JuniL2tpTunnelStatusRemoteVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 9),
    _JuniL2tpTunnelStatusRemoteVendorName_Type()
)
juniL2tpTunnelStatusRemoteVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRemoteVendorName.setStatus("current")
_JuniL2tpTunnelStatusRemoteFirmwareRevision_Type = Integer32
_JuniL2tpTunnelStatusRemoteFirmwareRevision_Object = MibTableColumn
juniL2tpTunnelStatusRemoteFirmwareRevision = _JuniL2tpTunnelStatusRemoteFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 10),
    _JuniL2tpTunnelStatusRemoteFirmwareRevision_Type()
)
juniL2tpTunnelStatusRemoteFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRemoteFirmwareRevision.setStatus("current")


class _JuniL2tpTunnelStatusRemoteProtocolVersion_Type(OctetString):
    """Custom type juniL2tpTunnelStatusRemoteProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_JuniL2tpTunnelStatusRemoteProtocolVersion_Type.__name__ = "OctetString"
_JuniL2tpTunnelStatusRemoteProtocolVersion_Object = MibTableColumn
juniL2tpTunnelStatusRemoteProtocolVersion = _JuniL2tpTunnelStatusRemoteProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 11),
    _JuniL2tpTunnelStatusRemoteProtocolVersion_Type()
)
juniL2tpTunnelStatusRemoteProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRemoteProtocolVersion.setStatus("current")


class _JuniL2tpTunnelStatusRemoteBearerCapabilities_Type(Integer32):
    """Custom type juniL2tpTunnelStatusRemoteBearerCapabilities based on Integer32"""
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
        *(("analog", 2),
          ("digital", 1),
          ("digitalAnalog", 3),
          ("none", 0))
    )


_JuniL2tpTunnelStatusRemoteBearerCapabilities_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusRemoteBearerCapabilities_Object = MibTableColumn
juniL2tpTunnelStatusRemoteBearerCapabilities = _JuniL2tpTunnelStatusRemoteBearerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 12),
    _JuniL2tpTunnelStatusRemoteBearerCapabilities_Type()
)
juniL2tpTunnelStatusRemoteBearerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRemoteBearerCapabilities.setStatus("current")


class _JuniL2tpTunnelStatusRemoteFramingCapabilities_Type(Integer32):
    """Custom type juniL2tpTunnelStatusRemoteFramingCapabilities based on Integer32"""
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
        *(("async", 2),
          ("none", 0),
          ("sync", 1),
          ("syncAsync", 3))
    )


_JuniL2tpTunnelStatusRemoteFramingCapabilities_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusRemoteFramingCapabilities_Object = MibTableColumn
juniL2tpTunnelStatusRemoteFramingCapabilities = _JuniL2tpTunnelStatusRemoteFramingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 13),
    _JuniL2tpTunnelStatusRemoteFramingCapabilities_Type()
)
juniL2tpTunnelStatusRemoteFramingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRemoteFramingCapabilities.setStatus("current")
_JuniL2tpTunnelStatusRecvWindowSize_Type = Gauge32
_JuniL2tpTunnelStatusRecvWindowSize_Object = MibTableColumn
juniL2tpTunnelStatusRecvWindowSize = _JuniL2tpTunnelStatusRecvWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 14),
    _JuniL2tpTunnelStatusRecvWindowSize_Type()
)
juniL2tpTunnelStatusRecvWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRecvWindowSize.setStatus("current")
_JuniL2tpTunnelStatusSendWindowSize_Type = Gauge32
_JuniL2tpTunnelStatusSendWindowSize_Object = MibTableColumn
juniL2tpTunnelStatusSendWindowSize = _JuniL2tpTunnelStatusSendWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 15),
    _JuniL2tpTunnelStatusSendWindowSize_Type()
)
juniL2tpTunnelStatusSendWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusSendWindowSize.setStatus("current")
_JuniL2tpTunnelStatusSendQueueDepth_Type = Gauge32
_JuniL2tpTunnelStatusSendQueueDepth_Object = MibTableColumn
juniL2tpTunnelStatusSendQueueDepth = _JuniL2tpTunnelStatusSendQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 16),
    _JuniL2tpTunnelStatusSendQueueDepth_Type()
)
juniL2tpTunnelStatusSendQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusSendQueueDepth.setStatus("current")


class _JuniL2tpTunnelStatusRecvSeq_Type(Integer32):
    """Custom type juniL2tpTunnelStatusRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpTunnelStatusRecvSeq_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusRecvSeq_Object = MibTableColumn
juniL2tpTunnelStatusRecvSeq = _JuniL2tpTunnelStatusRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 17),
    _JuniL2tpTunnelStatusRecvSeq_Type()
)
juniL2tpTunnelStatusRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRecvSeq.setStatus("current")


class _JuniL2tpTunnelStatusRecvSeqAck_Type(Integer32):
    """Custom type juniL2tpTunnelStatusRecvSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpTunnelStatusRecvSeqAck_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusRecvSeqAck_Object = MibTableColumn
juniL2tpTunnelStatusRecvSeqAck = _JuniL2tpTunnelStatusRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 18),
    _JuniL2tpTunnelStatusRecvSeqAck_Type()
)
juniL2tpTunnelStatusRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusRecvSeqAck.setStatus("current")


class _JuniL2tpTunnelStatusSendSeq_Type(Integer32):
    """Custom type juniL2tpTunnelStatusSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpTunnelStatusSendSeq_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusSendSeq_Object = MibTableColumn
juniL2tpTunnelStatusSendSeq = _JuniL2tpTunnelStatusSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 19),
    _JuniL2tpTunnelStatusSendSeq_Type()
)
juniL2tpTunnelStatusSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusSendSeq.setStatus("current")


class _JuniL2tpTunnelStatusSendSeqAck_Type(Integer32):
    """Custom type juniL2tpTunnelStatusSendSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpTunnelStatusSendSeqAck_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusSendSeqAck_Object = MibTableColumn
juniL2tpTunnelStatusSendSeqAck = _JuniL2tpTunnelStatusSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 20),
    _JuniL2tpTunnelStatusSendSeqAck_Type()
)
juniL2tpTunnelStatusSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusSendSeqAck.setStatus("current")
_JuniL2tpTunnelStatusTotalSessions_Type = Counter32
_JuniL2tpTunnelStatusTotalSessions_Object = MibTableColumn
juniL2tpTunnelStatusTotalSessions = _JuniL2tpTunnelStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 21),
    _JuniL2tpTunnelStatusTotalSessions_Type()
)
juniL2tpTunnelStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusTotalSessions.setStatus("current")
_JuniL2tpTunnelStatusFailedSessions_Type = Counter32
_JuniL2tpTunnelStatusFailedSessions_Object = MibTableColumn
juniL2tpTunnelStatusFailedSessions = _JuniL2tpTunnelStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 22),
    _JuniL2tpTunnelStatusFailedSessions_Type()
)
juniL2tpTunnelStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusFailedSessions.setStatus("current")
_JuniL2tpTunnelStatusActiveSessions_Type = Gauge32
_JuniL2tpTunnelStatusActiveSessions_Object = MibTableColumn
juniL2tpTunnelStatusActiveSessions = _JuniL2tpTunnelStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 23),
    _JuniL2tpTunnelStatusActiveSessions_Type()
)
juniL2tpTunnelStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusActiveSessions.setStatus("current")


class _JuniL2tpTunnelStatusLastResultCode_Type(Integer32):
    """Custom type juniL2tpTunnelStatusLastResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpTunnelStatusLastResultCode_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusLastResultCode_Object = MibTableColumn
juniL2tpTunnelStatusLastResultCode = _JuniL2tpTunnelStatusLastResultCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 24),
    _JuniL2tpTunnelStatusLastResultCode_Type()
)
juniL2tpTunnelStatusLastResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusLastResultCode.setStatus("current")


class _JuniL2tpTunnelStatusLastErrorCode_Type(Integer32):
    """Custom type juniL2tpTunnelStatusLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpTunnelStatusLastErrorCode_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusLastErrorCode_Object = MibTableColumn
juniL2tpTunnelStatusLastErrorCode = _JuniL2tpTunnelStatusLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 25),
    _JuniL2tpTunnelStatusLastErrorCode_Type()
)
juniL2tpTunnelStatusLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusLastErrorCode.setStatus("current")
_JuniL2tpTunnelStatusLastErrorMessage_Type = DisplayString
_JuniL2tpTunnelStatusLastErrorMessage_Object = MibTableColumn
juniL2tpTunnelStatusLastErrorMessage = _JuniL2tpTunnelStatusLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 26),
    _JuniL2tpTunnelStatusLastErrorMessage_Type()
)
juniL2tpTunnelStatusLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusLastErrorMessage.setStatus("current")
_JuniL2tpTunnelStatusCumEstabTime_Type = Unsigned32
_JuniL2tpTunnelStatusCumEstabTime_Object = MibTableColumn
juniL2tpTunnelStatusCumEstabTime = _JuniL2tpTunnelStatusCumEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 27),
    _JuniL2tpTunnelStatusCumEstabTime_Type()
)
juniL2tpTunnelStatusCumEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusCumEstabTime.setStatus("current")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusCumEstabTime.setUnits("seconds")


class _JuniL2tpTunnelStatusEffectiveFailoverResync_Type(Integer32):
    """Custom type juniL2tpTunnelStatusEffectiveFailoverResync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpTunnelStatusEffectiveFailoverResync_Type.__name__ = "Integer32"
_JuniL2tpTunnelStatusEffectiveFailoverResync_Object = MibTableColumn
juniL2tpTunnelStatusEffectiveFailoverResync = _JuniL2tpTunnelStatusEffectiveFailoverResync_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 28),
    _JuniL2tpTunnelStatusEffectiveFailoverResync_Type()
)
juniL2tpTunnelStatusEffectiveFailoverResync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatusEffectiveFailoverResync.setStatus("current")
_JuniL2tpTunnelStatistics_ObjectIdentity = ObjectIdentity
juniL2tpTunnelStatistics = _JuniL2tpTunnelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3)
)
_JuniL2tpTunnelStatTable_Object = MibTable
juniL2tpTunnelStatTable = _JuniL2tpTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    juniL2tpTunnelStatTable.setStatus("current")
_JuniL2tpTunnelStatEntry_Object = MibTableRow
juniL2tpTunnelStatEntry = _JuniL2tpTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1)
)
juniL2tpTunnelStatEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpTunnelStatIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpTunnelStatEntry.setStatus("current")
_JuniL2tpTunnelStatIfIndex_Type = InterfaceIndex
_JuniL2tpTunnelStatIfIndex_Object = MibTableColumn
juniL2tpTunnelStatIfIndex = _JuniL2tpTunnelStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 1),
    _JuniL2tpTunnelStatIfIndex_Type()
)
juniL2tpTunnelStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatIfIndex.setStatus("current")
_JuniL2tpTunnelStatCtlRecvOctets_Type = Counter32
_JuniL2tpTunnelStatCtlRecvOctets_Object = MibTableColumn
juniL2tpTunnelStatCtlRecvOctets = _JuniL2tpTunnelStatCtlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 2),
    _JuniL2tpTunnelStatCtlRecvOctets_Type()
)
juniL2tpTunnelStatCtlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlRecvOctets.setStatus("current")
_JuniL2tpTunnelStatCtlRecvPackets_Type = Counter32
_JuniL2tpTunnelStatCtlRecvPackets_Object = MibTableColumn
juniL2tpTunnelStatCtlRecvPackets = _JuniL2tpTunnelStatCtlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 3),
    _JuniL2tpTunnelStatCtlRecvPackets_Type()
)
juniL2tpTunnelStatCtlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlRecvPackets.setStatus("current")
_JuniL2tpTunnelStatCtlRecvErrors_Type = Counter32
_JuniL2tpTunnelStatCtlRecvErrors_Object = MibTableColumn
juniL2tpTunnelStatCtlRecvErrors = _JuniL2tpTunnelStatCtlRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 4),
    _JuniL2tpTunnelStatCtlRecvErrors_Type()
)
juniL2tpTunnelStatCtlRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlRecvErrors.setStatus("current")
_JuniL2tpTunnelStatCtlRecvDiscards_Type = Counter32
_JuniL2tpTunnelStatCtlRecvDiscards_Object = MibTableColumn
juniL2tpTunnelStatCtlRecvDiscards = _JuniL2tpTunnelStatCtlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 5),
    _JuniL2tpTunnelStatCtlRecvDiscards_Type()
)
juniL2tpTunnelStatCtlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlRecvDiscards.setStatus("current")
_JuniL2tpTunnelStatCtlSendOctets_Type = Counter32
_JuniL2tpTunnelStatCtlSendOctets_Object = MibTableColumn
juniL2tpTunnelStatCtlSendOctets = _JuniL2tpTunnelStatCtlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 6),
    _JuniL2tpTunnelStatCtlSendOctets_Type()
)
juniL2tpTunnelStatCtlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlSendOctets.setStatus("current")
_JuniL2tpTunnelStatCtlSendPackets_Type = Counter32
_JuniL2tpTunnelStatCtlSendPackets_Object = MibTableColumn
juniL2tpTunnelStatCtlSendPackets = _JuniL2tpTunnelStatCtlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 7),
    _JuniL2tpTunnelStatCtlSendPackets_Type()
)
juniL2tpTunnelStatCtlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlSendPackets.setStatus("current")
_JuniL2tpTunnelStatCtlSendErrors_Type = Counter32
_JuniL2tpTunnelStatCtlSendErrors_Object = MibTableColumn
juniL2tpTunnelStatCtlSendErrors = _JuniL2tpTunnelStatCtlSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 8),
    _JuniL2tpTunnelStatCtlSendErrors_Type()
)
juniL2tpTunnelStatCtlSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlSendErrors.setStatus("current")
_JuniL2tpTunnelStatCtlSendDiscards_Type = Counter32
_JuniL2tpTunnelStatCtlSendDiscards_Object = MibTableColumn
juniL2tpTunnelStatCtlSendDiscards = _JuniL2tpTunnelStatCtlSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 9),
    _JuniL2tpTunnelStatCtlSendDiscards_Type()
)
juniL2tpTunnelStatCtlSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlSendDiscards.setStatus("current")
_JuniL2tpTunnelStatPayRecvOctets_Type = Counter32
_JuniL2tpTunnelStatPayRecvOctets_Object = MibTableColumn
juniL2tpTunnelStatPayRecvOctets = _JuniL2tpTunnelStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 10),
    _JuniL2tpTunnelStatPayRecvOctets_Type()
)
juniL2tpTunnelStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPayRecvOctets.setStatus("current")
_JuniL2tpTunnelStatPayRecvPackets_Type = Counter32
_JuniL2tpTunnelStatPayRecvPackets_Object = MibTableColumn
juniL2tpTunnelStatPayRecvPackets = _JuniL2tpTunnelStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 11),
    _JuniL2tpTunnelStatPayRecvPackets_Type()
)
juniL2tpTunnelStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPayRecvPackets.setStatus("current")
_JuniL2tpTunnelStatPayRecvErrors_Type = Counter32
_JuniL2tpTunnelStatPayRecvErrors_Object = MibTableColumn
juniL2tpTunnelStatPayRecvErrors = _JuniL2tpTunnelStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 12),
    _JuniL2tpTunnelStatPayRecvErrors_Type()
)
juniL2tpTunnelStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPayRecvErrors.setStatus("current")
_JuniL2tpTunnelStatPayRecvDiscards_Type = Counter32
_JuniL2tpTunnelStatPayRecvDiscards_Object = MibTableColumn
juniL2tpTunnelStatPayRecvDiscards = _JuniL2tpTunnelStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 13),
    _JuniL2tpTunnelStatPayRecvDiscards_Type()
)
juniL2tpTunnelStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPayRecvDiscards.setStatus("current")
_JuniL2tpTunnelStatPaySendOctets_Type = Counter32
_JuniL2tpTunnelStatPaySendOctets_Object = MibTableColumn
juniL2tpTunnelStatPaySendOctets = _JuniL2tpTunnelStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 14),
    _JuniL2tpTunnelStatPaySendOctets_Type()
)
juniL2tpTunnelStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPaySendOctets.setStatus("current")
_JuniL2tpTunnelStatPaySendPackets_Type = Counter32
_JuniL2tpTunnelStatPaySendPackets_Object = MibTableColumn
juniL2tpTunnelStatPaySendPackets = _JuniL2tpTunnelStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 15),
    _JuniL2tpTunnelStatPaySendPackets_Type()
)
juniL2tpTunnelStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPaySendPackets.setStatus("current")
_JuniL2tpTunnelStatPaySendErrors_Type = Counter32
_JuniL2tpTunnelStatPaySendErrors_Object = MibTableColumn
juniL2tpTunnelStatPaySendErrors = _JuniL2tpTunnelStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 16),
    _JuniL2tpTunnelStatPaySendErrors_Type()
)
juniL2tpTunnelStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPaySendErrors.setStatus("current")
_JuniL2tpTunnelStatPaySendDiscards_Type = Counter32
_JuniL2tpTunnelStatPaySendDiscards_Object = MibTableColumn
juniL2tpTunnelStatPaySendDiscards = _JuniL2tpTunnelStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 17),
    _JuniL2tpTunnelStatPaySendDiscards_Type()
)
juniL2tpTunnelStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatPaySendDiscards.setStatus("current")
_JuniL2tpTunnelStatCtlRecvZLB_Type = Counter32
_JuniL2tpTunnelStatCtlRecvZLB_Object = MibTableColumn
juniL2tpTunnelStatCtlRecvZLB = _JuniL2tpTunnelStatCtlRecvZLB_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 18),
    _JuniL2tpTunnelStatCtlRecvZLB_Type()
)
juniL2tpTunnelStatCtlRecvZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlRecvZLB.setStatus("current")
_JuniL2tpTunnelStatCtlRecvOutOfSequence_Type = Counter32
_JuniL2tpTunnelStatCtlRecvOutOfSequence_Object = MibTableColumn
juniL2tpTunnelStatCtlRecvOutOfSequence = _JuniL2tpTunnelStatCtlRecvOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 19),
    _JuniL2tpTunnelStatCtlRecvOutOfSequence_Type()
)
juniL2tpTunnelStatCtlRecvOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlRecvOutOfSequence.setStatus("current")
_JuniL2tpTunnelStatCtlRecvOutOfWindow_Type = Counter32
_JuniL2tpTunnelStatCtlRecvOutOfWindow_Object = MibTableColumn
juniL2tpTunnelStatCtlRecvOutOfWindow = _JuniL2tpTunnelStatCtlRecvOutOfWindow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 20),
    _JuniL2tpTunnelStatCtlRecvOutOfWindow_Type()
)
juniL2tpTunnelStatCtlRecvOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlRecvOutOfWindow.setStatus("current")
_JuniL2tpTunnelStatCtlSendZLB_Type = Counter32
_JuniL2tpTunnelStatCtlSendZLB_Object = MibTableColumn
juniL2tpTunnelStatCtlSendZLB = _JuniL2tpTunnelStatCtlSendZLB_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 21),
    _JuniL2tpTunnelStatCtlSendZLB_Type()
)
juniL2tpTunnelStatCtlSendZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlSendZLB.setStatus("current")
_JuniL2tpTunnelStatCtlSendRetransmits_Type = Counter32
_JuniL2tpTunnelStatCtlSendRetransmits_Object = MibTableColumn
juniL2tpTunnelStatCtlSendRetransmits = _JuniL2tpTunnelStatCtlSendRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 22),
    _JuniL2tpTunnelStatCtlSendRetransmits_Type()
)
juniL2tpTunnelStatCtlSendRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpTunnelStatCtlSendRetransmits.setStatus("current")
_JuniL2tpTunnelMap_ObjectIdentity = ObjectIdentity
juniL2tpTunnelMap = _JuniL2tpTunnelMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4)
)
_JuniL2tpMapTifSidToSifTable_Object = MibTable
juniL2tpMapTifSidToSifTable = _JuniL2tpMapTifSidToSifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    juniL2tpMapTifSidToSifTable.setStatus("current")
_JuniL2tpMapTifSidToSifEntry_Object = MibTableRow
juniL2tpMapTifSidToSifEntry = _JuniL2tpMapTifSidToSifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1)
)
juniL2tpMapTifSidToSifEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpMapTifSidToSifTunnelIfIndex"),
    (0, "Juniper-L2TP-MIB", "juniL2tpMapTifSidToSifLocalSessionId"),
)
if mibBuilder.loadTexts:
    juniL2tpMapTifSidToSifEntry.setStatus("current")
_JuniL2tpMapTifSidToSifTunnelIfIndex_Type = InterfaceIndex
_JuniL2tpMapTifSidToSifTunnelIfIndex_Object = MibTableColumn
juniL2tpMapTifSidToSifTunnelIfIndex = _JuniL2tpMapTifSidToSifTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1, 1),
    _JuniL2tpMapTifSidToSifTunnelIfIndex_Type()
)
juniL2tpMapTifSidToSifTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpMapTifSidToSifTunnelIfIndex.setStatus("current")
_JuniL2tpMapTifSidToSifLocalSessionId_Type = JuniL2tpSessionId
_JuniL2tpMapTifSidToSifLocalSessionId_Object = MibTableColumn
juniL2tpMapTifSidToSifLocalSessionId = _JuniL2tpMapTifSidToSifLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1, 2),
    _JuniL2tpMapTifSidToSifLocalSessionId_Type()
)
juniL2tpMapTifSidToSifLocalSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpMapTifSidToSifLocalSessionId.setStatus("current")
_JuniL2tpMapTifSidToSifSessionIfIndex_Type = InterfaceIndex
_JuniL2tpMapTifSidToSifSessionIfIndex_Object = MibTableColumn
juniL2tpMapTifSidToSifSessionIfIndex = _JuniL2tpMapTifSidToSifSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1, 3),
    _JuniL2tpMapTifSidToSifSessionIfIndex_Type()
)
juniL2tpMapTifSidToSifSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpMapTifSidToSifSessionIfIndex.setStatus("current")
_JuniL2tpMapTidToTifTable_Object = MibTable
juniL2tpMapTidToTifTable = _JuniL2tpMapTidToTifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    juniL2tpMapTidToTifTable.setStatus("current")
_JuniL2tpMapTidToTifEntry_Object = MibTableRow
juniL2tpMapTidToTifEntry = _JuniL2tpMapTidToTifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2, 1)
)
juniL2tpMapTidToTifEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpMapTidToTifLocalTunnelId"),
)
if mibBuilder.loadTexts:
    juniL2tpMapTidToTifEntry.setStatus("current")
_JuniL2tpMapTidToTifLocalTunnelId_Type = JuniL2tpTunnelId
_JuniL2tpMapTidToTifLocalTunnelId_Object = MibTableColumn
juniL2tpMapTidToTifLocalTunnelId = _JuniL2tpMapTidToTifLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2, 1, 1),
    _JuniL2tpMapTidToTifLocalTunnelId_Type()
)
juniL2tpMapTidToTifLocalTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpMapTidToTifLocalTunnelId.setStatus("current")
_JuniL2tpMapTidToTifIfIndex_Type = InterfaceIndex
_JuniL2tpMapTidToTifIfIndex_Object = MibTableColumn
juniL2tpMapTidToTifIfIndex = _JuniL2tpMapTidToTifIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2, 1, 2),
    _JuniL2tpMapTidToTifIfIndex_Type()
)
juniL2tpMapTidToTifIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpMapTidToTifIfIndex.setStatus("current")
_JuniL2tpSession_ObjectIdentity = ObjectIdentity
juniL2tpSession = _JuniL2tpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4)
)
_JuniL2tpSessionConfig_ObjectIdentity = ObjectIdentity
juniL2tpSessionConfig = _JuniL2tpSessionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1)
)
_JuniL2tpSessionConfigTable_Object = MibTable
juniL2tpSessionConfigTable = _JuniL2tpSessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniL2tpSessionConfigTable.setStatus("current")
_JuniL2tpSessionConfigEntry_Object = MibTableRow
juniL2tpSessionConfigEntry = _JuniL2tpSessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1)
)
juniL2tpSessionConfigEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpSessionConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpSessionConfigEntry.setStatus("current")
_JuniL2tpSessionConfigIfIndex_Type = InterfaceIndex
_JuniL2tpSessionConfigIfIndex_Object = MibTableColumn
juniL2tpSessionConfigIfIndex = _JuniL2tpSessionConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1, 1),
    _JuniL2tpSessionConfigIfIndex_Type()
)
juniL2tpSessionConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpSessionConfigIfIndex.setStatus("current")
_JuniL2tpSessionConfigRowStatus_Type = RowStatus
_JuniL2tpSessionConfigRowStatus_Object = MibTableColumn
juniL2tpSessionConfigRowStatus = _JuniL2tpSessionConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1, 2),
    _JuniL2tpSessionConfigRowStatus_Type()
)
juniL2tpSessionConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpSessionConfigRowStatus.setStatus("current")


class _JuniL2tpSessionConfigAdminState_Type(JuniL2tpAdminState):
    """Custom type juniL2tpSessionConfigAdminState based on JuniL2tpAdminState"""


_JuniL2tpSessionConfigAdminState_Object = MibTableColumn
juniL2tpSessionConfigAdminState = _JuniL2tpSessionConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1, 3),
    _JuniL2tpSessionConfigAdminState_Type()
)
juniL2tpSessionConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniL2tpSessionConfigAdminState.setStatus("current")
_JuniL2tpSessionStatus_ObjectIdentity = ObjectIdentity
juniL2tpSessionStatus = _JuniL2tpSessionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2)
)
_JuniL2tpSessionStatusTable_Object = MibTable
juniL2tpSessionStatusTable = _JuniL2tpSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    juniL2tpSessionStatusTable.setStatus("current")
_JuniL2tpSessionStatusEntry_Object = MibTableRow
juniL2tpSessionStatusEntry = _JuniL2tpSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1)
)
juniL2tpSessionStatusEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpSessionStatusIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpSessionStatusEntry.setStatus("current")
_JuniL2tpSessionStatusIfIndex_Type = InterfaceIndex
_JuniL2tpSessionStatusIfIndex_Object = MibTableColumn
juniL2tpSessionStatusIfIndex = _JuniL2tpSessionStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 1),
    _JuniL2tpSessionStatusIfIndex_Type()
)
juniL2tpSessionStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusIfIndex.setStatus("current")
_JuniL2tpSessionStatusLacPppIfIndex_Type = InterfaceIndexOrZero
_JuniL2tpSessionStatusLacPppIfIndex_Object = MibTableColumn
juniL2tpSessionStatusLacPppIfIndex = _JuniL2tpSessionStatusLacPppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 2),
    _JuniL2tpSessionStatusLacPppIfIndex_Type()
)
juniL2tpSessionStatusLacPppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusLacPppIfIndex.setStatus("deprecated")
_JuniL2tpSessionStatusLocalSessionId_Type = JuniL2tpSessionId
_JuniL2tpSessionStatusLocalSessionId_Object = MibTableColumn
juniL2tpSessionStatusLocalSessionId = _JuniL2tpSessionStatusLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 3),
    _JuniL2tpSessionStatusLocalSessionId_Type()
)
juniL2tpSessionStatusLocalSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusLocalSessionId.setStatus("current")
_JuniL2tpSessionStatusRemoteSessionId_Type = JuniL2tpSessionId
_JuniL2tpSessionStatusRemoteSessionId_Object = MibTableColumn
juniL2tpSessionStatusRemoteSessionId = _JuniL2tpSessionStatusRemoteSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 4),
    _JuniL2tpSessionStatusRemoteSessionId_Type()
)
juniL2tpSessionStatusRemoteSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusRemoteSessionId.setStatus("current")
_JuniL2tpSessionStatusUserName_Type = DisplayString
_JuniL2tpSessionStatusUserName_Object = MibTableColumn
juniL2tpSessionStatusUserName = _JuniL2tpSessionStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 5),
    _JuniL2tpSessionStatusUserName_Type()
)
juniL2tpSessionStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusUserName.setStatus("current")
_JuniL2tpSessionStatusEffectiveAdminState_Type = JuniL2tpAdminState
_JuniL2tpSessionStatusEffectiveAdminState_Object = MibTableColumn
juniL2tpSessionStatusEffectiveAdminState = _JuniL2tpSessionStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 6),
    _JuniL2tpSessionStatusEffectiveAdminState_Type()
)
juniL2tpSessionStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusEffectiveAdminState.setStatus("current")


class _JuniL2tpSessionStatusState_Type(Integer32):
    """Custom type juniL2tpSessionStatusState based on Integer32"""
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
        *(("connecting", 1),
          ("disconnecting", 3),
          ("established", 2),
          ("idle", 0))
    )


_JuniL2tpSessionStatusState_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusState_Object = MibTableColumn
juniL2tpSessionStatusState = _JuniL2tpSessionStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 7),
    _JuniL2tpSessionStatusState_Type()
)
juniL2tpSessionStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusState.setStatus("current")


class _JuniL2tpSessionStatusCallType_Type(Integer32):
    """Custom type juniL2tpSessionStatusCallType based on Integer32"""
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
        *(("lacIncoming", 1),
          ("lacOutgoing", 3),
          ("lnsIncoming", 2),
          ("lnsOutgoing", 4),
          ("none", 0))
    )


_JuniL2tpSessionStatusCallType_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusCallType_Object = MibTableColumn
juniL2tpSessionStatusCallType = _JuniL2tpSessionStatusCallType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 8),
    _JuniL2tpSessionStatusCallType_Type()
)
juniL2tpSessionStatusCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusCallType.setStatus("current")
_JuniL2tpSessionStatusCallSerialNumber_Type = Integer32
_JuniL2tpSessionStatusCallSerialNumber_Object = MibTableColumn
juniL2tpSessionStatusCallSerialNumber = _JuniL2tpSessionStatusCallSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 9),
    _JuniL2tpSessionStatusCallSerialNumber_Type()
)
juniL2tpSessionStatusCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusCallSerialNumber.setStatus("current")
_JuniL2tpSessionStatusTxConnectSpeed_Type = Integer32
_JuniL2tpSessionStatusTxConnectSpeed_Object = MibTableColumn
juniL2tpSessionStatusTxConnectSpeed = _JuniL2tpSessionStatusTxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 10),
    _JuniL2tpSessionStatusTxConnectSpeed_Type()
)
juniL2tpSessionStatusTxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusTxConnectSpeed.setStatus("current")
_JuniL2tpSessionStatusRxConnectSpeed_Type = Integer32
_JuniL2tpSessionStatusRxConnectSpeed_Object = MibTableColumn
juniL2tpSessionStatusRxConnectSpeed = _JuniL2tpSessionStatusRxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 11),
    _JuniL2tpSessionStatusRxConnectSpeed_Type()
)
juniL2tpSessionStatusRxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusRxConnectSpeed.setStatus("current")


class _JuniL2tpSessionStatusCallBearerType_Type(Integer32):
    """Custom type juniL2tpSessionStatusCallBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 1),
          ("none", 0))
    )


_JuniL2tpSessionStatusCallBearerType_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusCallBearerType_Object = MibTableColumn
juniL2tpSessionStatusCallBearerType = _JuniL2tpSessionStatusCallBearerType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 12),
    _JuniL2tpSessionStatusCallBearerType_Type()
)
juniL2tpSessionStatusCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusCallBearerType.setStatus("current")


class _JuniL2tpSessionStatusFramingType_Type(Integer32):
    """Custom type juniL2tpSessionStatusFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("none", 0),
          ("sync", 1))
    )


_JuniL2tpSessionStatusFramingType_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusFramingType_Object = MibTableColumn
juniL2tpSessionStatusFramingType = _JuniL2tpSessionStatusFramingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 13),
    _JuniL2tpSessionStatusFramingType_Type()
)
juniL2tpSessionStatusFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusFramingType.setStatus("current")
_JuniL2tpSessionStatusPhysChanId_Type = Integer32
_JuniL2tpSessionStatusPhysChanId_Object = MibTableColumn
juniL2tpSessionStatusPhysChanId = _JuniL2tpSessionStatusPhysChanId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 14),
    _JuniL2tpSessionStatusPhysChanId_Type()
)
juniL2tpSessionStatusPhysChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusPhysChanId.setStatus("current")
_JuniL2tpSessionStatusDnis_Type = DisplayString
_JuniL2tpSessionStatusDnis_Object = MibTableColumn
juniL2tpSessionStatusDnis = _JuniL2tpSessionStatusDnis_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 15),
    _JuniL2tpSessionStatusDnis_Type()
)
juniL2tpSessionStatusDnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusDnis.setStatus("current")
_JuniL2tpSessionStatusClid_Type = DisplayString
_JuniL2tpSessionStatusClid_Object = MibTableColumn
juniL2tpSessionStatusClid = _JuniL2tpSessionStatusClid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 16),
    _JuniL2tpSessionStatusClid_Type()
)
juniL2tpSessionStatusClid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusClid.setStatus("current")
_JuniL2tpSessionStatusSubAddress_Type = DisplayString
_JuniL2tpSessionStatusSubAddress_Object = MibTableColumn
juniL2tpSessionStatusSubAddress = _JuniL2tpSessionStatusSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 17),
    _JuniL2tpSessionStatusSubAddress_Type()
)
juniL2tpSessionStatusSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusSubAddress.setStatus("current")
_JuniL2tpSessionStatusPrivateGroupId_Type = DisplayString
_JuniL2tpSessionStatusPrivateGroupId_Object = MibTableColumn
juniL2tpSessionStatusPrivateGroupId = _JuniL2tpSessionStatusPrivateGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 18),
    _JuniL2tpSessionStatusPrivateGroupId_Type()
)
juniL2tpSessionStatusPrivateGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusPrivateGroupId.setStatus("current")
_JuniL2tpSessionStatusProxyLcp_Type = TruthValue
_JuniL2tpSessionStatusProxyLcp_Object = MibTableColumn
juniL2tpSessionStatusProxyLcp = _JuniL2tpSessionStatusProxyLcp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 19),
    _JuniL2tpSessionStatusProxyLcp_Type()
)
juniL2tpSessionStatusProxyLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusProxyLcp.setStatus("current")


class _JuniL2tpSessionStatusAuthMethod_Type(Integer32):
    """Custom type juniL2tpSessionStatusAuthMethod based on Integer32"""
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
        *(("none", 0),
          ("pppChap", 1),
          ("pppMsChap", 3),
          ("pppPap", 2))
    )


_JuniL2tpSessionStatusAuthMethod_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusAuthMethod_Object = MibTableColumn
juniL2tpSessionStatusAuthMethod = _JuniL2tpSessionStatusAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 20),
    _JuniL2tpSessionStatusAuthMethod_Type()
)
juniL2tpSessionStatusAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusAuthMethod.setStatus("current")


class _JuniL2tpSessionStatusSequencingState_Type(Integer32):
    """Custom type juniL2tpSessionStatusSequencingState based on Integer32"""
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
        *(("both", 3),
          ("local", 2),
          ("none", 0),
          ("remote", 1))
    )


_JuniL2tpSessionStatusSequencingState_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusSequencingState_Object = MibTableColumn
juniL2tpSessionStatusSequencingState = _JuniL2tpSessionStatusSequencingState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 21),
    _JuniL2tpSessionStatusSequencingState_Type()
)
juniL2tpSessionStatusSequencingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusSequencingState.setStatus("current")


class _JuniL2tpSessionStatusSendSeq_Type(Integer32):
    """Custom type juniL2tpSessionStatusSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpSessionStatusSendSeq_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusSendSeq_Object = MibTableColumn
juniL2tpSessionStatusSendSeq = _JuniL2tpSessionStatusSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 22),
    _JuniL2tpSessionStatusSendSeq_Type()
)
juniL2tpSessionStatusSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusSendSeq.setStatus("current")


class _JuniL2tpSessionStatusRecvSeq_Type(Integer32):
    """Custom type juniL2tpSessionStatusRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniL2tpSessionStatusRecvSeq_Type.__name__ = "Integer32"
_JuniL2tpSessionStatusRecvSeq_Object = MibTableColumn
juniL2tpSessionStatusRecvSeq = _JuniL2tpSessionStatusRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 23),
    _JuniL2tpSessionStatusRecvSeq_Type()
)
juniL2tpSessionStatusRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusRecvSeq.setStatus("current")
_JuniL2tpSessionStatusLacTunneledIfIndex_Type = InterfaceIndexOrZero
_JuniL2tpSessionStatusLacTunneledIfIndex_Object = MibTableColumn
juniL2tpSessionStatusLacTunneledIfIndex = _JuniL2tpSessionStatusLacTunneledIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 24),
    _JuniL2tpSessionStatusLacTunneledIfIndex_Type()
)
juniL2tpSessionStatusLacTunneledIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusLacTunneledIfIndex.setStatus("current")
_JuniL2tpSessionStatusCumEstabTime_Type = Unsigned32
_JuniL2tpSessionStatusCumEstabTime_Object = MibTableColumn
juniL2tpSessionStatusCumEstabTime = _JuniL2tpSessionStatusCumEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 25),
    _JuniL2tpSessionStatusCumEstabTime_Type()
)
juniL2tpSessionStatusCumEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusCumEstabTime.setStatus("current")
if mibBuilder.loadTexts:
    juniL2tpSessionStatusCumEstabTime.setUnits("seconds")
_JuniL2tpSessionStatistics_ObjectIdentity = ObjectIdentity
juniL2tpSessionStatistics = _JuniL2tpSessionStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3)
)
_JuniL2tpSessionStatTable_Object = MibTable
juniL2tpSessionStatTable = _JuniL2tpSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    juniL2tpSessionStatTable.setStatus("current")
_JuniL2tpSessionStatEntry_Object = MibTableRow
juniL2tpSessionStatEntry = _JuniL2tpSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1)
)
juniL2tpSessionStatEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpSessionStatIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpSessionStatEntry.setStatus("current")
_JuniL2tpSessionStatIfIndex_Type = InterfaceIndex
_JuniL2tpSessionStatIfIndex_Object = MibTableColumn
juniL2tpSessionStatIfIndex = _JuniL2tpSessionStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 1),
    _JuniL2tpSessionStatIfIndex_Type()
)
juniL2tpSessionStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpSessionStatIfIndex.setStatus("current")
_JuniL2tpSessionStatPayRecvOctets_Type = Counter32
_JuniL2tpSessionStatPayRecvOctets_Object = MibTableColumn
juniL2tpSessionStatPayRecvOctets = _JuniL2tpSessionStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 2),
    _JuniL2tpSessionStatPayRecvOctets_Type()
)
juniL2tpSessionStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPayRecvOctets.setStatus("current")
_JuniL2tpSessionStatPayRecvPackets_Type = Counter32
_JuniL2tpSessionStatPayRecvPackets_Object = MibTableColumn
juniL2tpSessionStatPayRecvPackets = _JuniL2tpSessionStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 3),
    _JuniL2tpSessionStatPayRecvPackets_Type()
)
juniL2tpSessionStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPayRecvPackets.setStatus("current")
_JuniL2tpSessionStatPayRecvErrors_Type = Counter32
_JuniL2tpSessionStatPayRecvErrors_Object = MibTableColumn
juniL2tpSessionStatPayRecvErrors = _JuniL2tpSessionStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 4),
    _JuniL2tpSessionStatPayRecvErrors_Type()
)
juniL2tpSessionStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPayRecvErrors.setStatus("current")
_JuniL2tpSessionStatPayRecvDiscards_Type = Counter32
_JuniL2tpSessionStatPayRecvDiscards_Object = MibTableColumn
juniL2tpSessionStatPayRecvDiscards = _JuniL2tpSessionStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 5),
    _JuniL2tpSessionStatPayRecvDiscards_Type()
)
juniL2tpSessionStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPayRecvDiscards.setStatus("current")
_JuniL2tpSessionStatPaySendOctets_Type = Counter32
_JuniL2tpSessionStatPaySendOctets_Object = MibTableColumn
juniL2tpSessionStatPaySendOctets = _JuniL2tpSessionStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 6),
    _JuniL2tpSessionStatPaySendOctets_Type()
)
juniL2tpSessionStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPaySendOctets.setStatus("current")
_JuniL2tpSessionStatPaySendPackets_Type = Counter32
_JuniL2tpSessionStatPaySendPackets_Object = MibTableColumn
juniL2tpSessionStatPaySendPackets = _JuniL2tpSessionStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 7),
    _JuniL2tpSessionStatPaySendPackets_Type()
)
juniL2tpSessionStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPaySendPackets.setStatus("current")
_JuniL2tpSessionStatPaySendErrors_Type = Counter32
_JuniL2tpSessionStatPaySendErrors_Object = MibTableColumn
juniL2tpSessionStatPaySendErrors = _JuniL2tpSessionStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 8),
    _JuniL2tpSessionStatPaySendErrors_Type()
)
juniL2tpSessionStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPaySendErrors.setStatus("current")
_JuniL2tpSessionStatPaySendDiscards_Type = Counter32
_JuniL2tpSessionStatPaySendDiscards_Object = MibTableColumn
juniL2tpSessionStatPaySendDiscards = _JuniL2tpSessionStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 9),
    _JuniL2tpSessionStatPaySendDiscards_Type()
)
juniL2tpSessionStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPaySendDiscards.setStatus("current")
_JuniL2tpSessionStatRecvOutOfSequence_Type = Counter32
_JuniL2tpSessionStatRecvOutOfSequence_Object = MibTableColumn
juniL2tpSessionStatRecvOutOfSequence = _JuniL2tpSessionStatRecvOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 10),
    _JuniL2tpSessionStatRecvOutOfSequence_Type()
)
juniL2tpSessionStatRecvOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatRecvOutOfSequence.setStatus("current")
_JuniL2tpSessionStatResequencingTimeouts_Type = Counter32
_JuniL2tpSessionStatResequencingTimeouts_Object = MibTableColumn
juniL2tpSessionStatResequencingTimeouts = _JuniL2tpSessionStatResequencingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 11),
    _JuniL2tpSessionStatResequencingTimeouts_Type()
)
juniL2tpSessionStatResequencingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatResequencingTimeouts.setStatus("current")
_JuniL2tpSessionStatPayLostPackets_Type = Unsigned32
_JuniL2tpSessionStatPayLostPackets_Object = MibTableColumn
juniL2tpSessionStatPayLostPackets = _JuniL2tpSessionStatPayLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 12),
    _JuniL2tpSessionStatPayLostPackets_Type()
)
juniL2tpSessionStatPayLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpSessionStatPayLostPackets.setStatus("current")
_JuniL2tpTransport_ObjectIdentity = ObjectIdentity
juniL2tpTransport = _JuniL2tpTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5)
)
_JuniL2tpTransportUdpIp_ObjectIdentity = ObjectIdentity
juniL2tpTransportUdpIp = _JuniL2tpTransportUdpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1)
)
_JuniL2tpUdpIpSystem_ObjectIdentity = ObjectIdentity
juniL2tpUdpIpSystem = _JuniL2tpUdpIpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 1)
)
_JuniL2tpUdpIpDestination_ObjectIdentity = ObjectIdentity
juniL2tpUdpIpDestination = _JuniL2tpUdpIpDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2)
)
_JuniL2tpUdpIpDestTable_Object = MibTable
juniL2tpUdpIpDestTable = _JuniL2tpUdpIpDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniL2tpUdpIpDestTable.setStatus("current")
_JuniL2tpUdpIpDestEntry_Object = MibTableRow
juniL2tpUdpIpDestEntry = _JuniL2tpUdpIpDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1)
)
juniL2tpUdpIpDestEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpUdpIpDestIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpUdpIpDestEntry.setStatus("current")
_JuniL2tpUdpIpDestIfIndex_Type = InterfaceIndex
_JuniL2tpUdpIpDestIfIndex_Object = MibTableColumn
juniL2tpUdpIpDestIfIndex = _JuniL2tpUdpIpDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 1),
    _JuniL2tpUdpIpDestIfIndex_Type()
)
juniL2tpUdpIpDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpUdpIpDestIfIndex.setStatus("current")
_JuniL2tpUdpIpDestRouterIndex_Type = Unsigned32
_JuniL2tpUdpIpDestRouterIndex_Object = MibTableColumn
juniL2tpUdpIpDestRouterIndex = _JuniL2tpUdpIpDestRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 2),
    _JuniL2tpUdpIpDestRouterIndex_Type()
)
juniL2tpUdpIpDestRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpDestRouterIndex.setStatus("current")
_JuniL2tpUdpIpDestLocalAddress_Type = IpAddress
_JuniL2tpUdpIpDestLocalAddress_Object = MibTableColumn
juniL2tpUdpIpDestLocalAddress = _JuniL2tpUdpIpDestLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 3),
    _JuniL2tpUdpIpDestLocalAddress_Type()
)
juniL2tpUdpIpDestLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpDestLocalAddress.setStatus("current")
_JuniL2tpUdpIpDestRemoteAddress_Type = IpAddress
_JuniL2tpUdpIpDestRemoteAddress_Object = MibTableColumn
juniL2tpUdpIpDestRemoteAddress = _JuniL2tpUdpIpDestRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 4),
    _JuniL2tpUdpIpDestRemoteAddress_Type()
)
juniL2tpUdpIpDestRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpDestRemoteAddress.setStatus("current")
_JuniL2tpUdpIpTunnel_ObjectIdentity = ObjectIdentity
juniL2tpUdpIpTunnel = _JuniL2tpUdpIpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3)
)
_JuniL2tpUdpIpTunnelTable_Object = MibTable
juniL2tpUdpIpTunnelTable = _JuniL2tpUdpIpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelTable.setStatus("current")
_JuniL2tpUdpIpTunnelEntry_Object = MibTableRow
juniL2tpUdpIpTunnelEntry = _JuniL2tpUdpIpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1)
)
juniL2tpUdpIpTunnelEntry.setIndexNames(
    (0, "Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelEntry.setStatus("current")
_JuniL2tpUdpIpTunnelIfIndex_Type = InterfaceIndex
_JuniL2tpUdpIpTunnelIfIndex_Object = MibTableColumn
juniL2tpUdpIpTunnelIfIndex = _JuniL2tpUdpIpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 1),
    _JuniL2tpUdpIpTunnelIfIndex_Type()
)
juniL2tpUdpIpTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelIfIndex.setStatus("current")
_JuniL2tpUdpIpTunnelRouterIndex_Type = Unsigned32
_JuniL2tpUdpIpTunnelRouterIndex_Object = MibTableColumn
juniL2tpUdpIpTunnelRouterIndex = _JuniL2tpUdpIpTunnelRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 2),
    _JuniL2tpUdpIpTunnelRouterIndex_Type()
)
juniL2tpUdpIpTunnelRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelRouterIndex.setStatus("current")
_JuniL2tpUdpIpTunnelLocalAddress_Type = IpAddress
_JuniL2tpUdpIpTunnelLocalAddress_Object = MibTableColumn
juniL2tpUdpIpTunnelLocalAddress = _JuniL2tpUdpIpTunnelLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 3),
    _JuniL2tpUdpIpTunnelLocalAddress_Type()
)
juniL2tpUdpIpTunnelLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelLocalAddress.setStatus("current")
_JuniL2tpUdpIpTunnelLocalPort_Type = Integer32
_JuniL2tpUdpIpTunnelLocalPort_Object = MibTableColumn
juniL2tpUdpIpTunnelLocalPort = _JuniL2tpUdpIpTunnelLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 4),
    _JuniL2tpUdpIpTunnelLocalPort_Type()
)
juniL2tpUdpIpTunnelLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelLocalPort.setStatus("current")
_JuniL2tpUdpIpTunnelRemoteAddress_Type = IpAddress
_JuniL2tpUdpIpTunnelRemoteAddress_Object = MibTableColumn
juniL2tpUdpIpTunnelRemoteAddress = _JuniL2tpUdpIpTunnelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 5),
    _JuniL2tpUdpIpTunnelRemoteAddress_Type()
)
juniL2tpUdpIpTunnelRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelRemoteAddress.setStatus("current")
_JuniL2tpUdpIpTunnelRemotePort_Type = Integer32
_JuniL2tpUdpIpTunnelRemotePort_Object = MibTableColumn
juniL2tpUdpIpTunnelRemotePort = _JuniL2tpUdpIpTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 6),
    _JuniL2tpUdpIpTunnelRemotePort_Type()
)
juniL2tpUdpIpTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelRemotePort.setStatus("current")
_JuniL2tpUdpIpTunnelRemoteReceiveAddress_Type = IpAddress
_JuniL2tpUdpIpTunnelRemoteReceiveAddress_Object = MibTableColumn
juniL2tpUdpIpTunnelRemoteReceiveAddress = _JuniL2tpUdpIpTunnelRemoteReceiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 7),
    _JuniL2tpUdpIpTunnelRemoteReceiveAddress_Type()
)
juniL2tpUdpIpTunnelRemoteReceiveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelRemoteReceiveAddress.setStatus("current")
_JuniL2tpUdpIpTunnelRemoteReceivePort_Type = Integer32
_JuniL2tpUdpIpTunnelRemoteReceivePort_Object = MibTableColumn
juniL2tpUdpIpTunnelRemoteReceivePort = _JuniL2tpUdpIpTunnelRemoteReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 8),
    _JuniL2tpUdpIpTunnelRemoteReceivePort_Type()
)
juniL2tpUdpIpTunnelRemoteReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniL2tpUdpIpTunnelRemoteReceivePort.setStatus("current")
_JuniL2tpUdpIpSession_ObjectIdentity = ObjectIdentity
juniL2tpUdpIpSession = _JuniL2tpUdpIpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 4)
)
_JuniL2tpTrapControl_ObjectIdentity = ObjectIdentity
juniL2tpTrapControl = _JuniL2tpTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 2)
)
_JuniL2tpConformance_ObjectIdentity = ObjectIdentity
juniL2tpConformance = _JuniL2tpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3)
)
_JuniL2tpGroups_ObjectIdentity = ObjectIdentity
juniL2tpGroups = _JuniL2tpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1)
)
_JuniL2tpCompliances_ObjectIdentity = ObjectIdentity
juniL2tpCompliances = _JuniL2tpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2)
)

# Managed Objects groups

juniL2tpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 1)
)
juniL2tpConfigGroup.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup.setStatus("obsolete")

juniL2tpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 2)
)
juniL2tpStatusGroup.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysStatusProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFirmwareRev"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLocalTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusInitiated"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteHostName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFirmwareRevision"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteBearerCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFramingCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendQueueDepth"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastResultCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorMessage"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLacPppIfIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLocalSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRemoteSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusUserName"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallSerialNumber"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusTxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallBearerType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusFramingType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPhysChanId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusDnis"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusClid"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSubAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPrivateGroupId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusProxyLcp"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusAuthMethod"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSequencingState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRecvSeq"))
)
if mibBuilder.loadTexts:
    juniL2tpStatusGroup.setStatus("obsolete")

juniL2tpStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 3)
)
juniL2tpStatGroup.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvZLB"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvOutOfSequence"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvOutOfWindow"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendZLB"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendRetransmits"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatRecvOutOfSequence"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatResequencingTimeouts"))
)
if mibBuilder.loadTexts:
    juniL2tpStatGroup.setStatus("obsolete")

juniL2tpMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 4)
)
juniL2tpMapGroup.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpMapTifSidToSifSessionIfIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpMapTidToTifIfIndex"))
)
if mibBuilder.loadTexts:
    juniL2tpMapGroup.setStatus("current")

juniL2tpUdpIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 5)
)
juniL2tpUdpIpGroup.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpUdpIpDestRouterIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpDestLocalAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpDestRemoteAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRouterIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelLocalAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelLocalPort"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRemoteAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRemotePort"))
)
if mibBuilder.loadTexts:
    juniL2tpUdpIpGroup.setStatus("obsolete")

juniL2tpStatusGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 6)
)
juniL2tpStatusGroup2.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysStatusProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFirmwareRev"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLocalTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusInitiated"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteHostName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFirmwareRevision"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteBearerCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFramingCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendQueueDepth"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastResultCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorMessage"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusCumEstabTime"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLocalSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRemoteSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusUserName"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallSerialNumber"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusTxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallBearerType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusFramingType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPhysChanId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusDnis"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusClid"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSubAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPrivateGroupId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusProxyLcp"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusAuthMethod"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSequencingState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLacTunneledIfIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCumEstabTime"))
)
if mibBuilder.loadTexts:
    juniL2tpStatusGroup2.setStatus("obsolete")

juniL2tpStatGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 7)
)
juniL2tpStatGroup2.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatCtlSendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPayRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatPaySendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPayRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatPaySendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvZLB"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvOutOfSequence"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlRecvOutOfWindow"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendZLB"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatCtlSendRetransmits"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayRecvDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendOctets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendPackets"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendErrors"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPaySendDiscards"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatRecvOutOfSequence"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatResequencingTimeouts"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatPayLostPackets"))
)
if mibBuilder.loadTexts:
    juniL2tpStatGroup2.setStatus("current")

juniL2tpConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 8)
)
juniL2tpConfigGroup2.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup2.setStatus("obsolete")

juniL2tpConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 9)
)
juniL2tpConfigGroup3.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup3.setStatus("obsolete")

juniL2tpConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 10)
)
juniL2tpConfigGroup4.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup4.setStatus("obsolete")

juniL2tpConfigGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 11)
)
juniL2tpConfigGroup5.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup5.setStatus("obsolete")

juniL2tpConfigGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 12)
)
juniL2tpConfigGroup6.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup6.setStatus("obsolete")

juniL2tpConfigGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 13)
)
juniL2tpConfigGroup7.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIgnoreTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup7.setStatus("obsolete")

juniL2tpUdpIpGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 14)
)
juniL2tpUdpIpGroup1.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpUdpIpDestRouterIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpDestLocalAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpDestRemoteAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRouterIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelLocalAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelLocalPort"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRemoteAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRemotePort"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRemoteReceiveAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpUdpIpTunnelRemoteReceivePort"))
)
if mibBuilder.loadTexts:
    juniL2tpUdpIpGroup1.setStatus("current")

juniL2tpConfigGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 15)
)
juniL2tpConfigGroup8.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIgnoreTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableDisconnectCauseAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup8.setStatus("obsolete")

juniL2tpConfigGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 16)
)
juniL2tpConfigGroup9.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIgnoreTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableDisconnectCauseAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup9.setStatus("obsolete")

juniL2tpConfigGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 17)
)
juniL2tpConfigGroup10.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIgnoreTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableDisconnectCauseAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableRxSpeedAvpWhenEqual"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup10.setStatus("obsolete")

juniL2tpStatusGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 18)
)
juniL2tpStatusGroup3.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysStatusProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFirmwareRev"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusIfCounterDiscontinuityTime"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLocalTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusInitiated"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteHostName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFirmwareRevision"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteBearerCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFramingCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendQueueDepth"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastResultCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorMessage"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusCumEstabTime"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLocalSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRemoteSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusUserName"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallSerialNumber"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusTxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallBearerType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusFramingType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPhysChanId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusDnis"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusClid"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSubAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPrivateGroupId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusProxyLcp"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusAuthMethod"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSequencingState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLacTunneledIfIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCumEstabTime"))
)
if mibBuilder.loadTexts:
    juniL2tpStatusGroup3.setStatus("obsolete")

juniL2tpConfigGroup11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 19)
)
juniL2tpConfigGroup11.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIgnoreTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableDisconnectCauseAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableRxSpeedAvpWhenEqual"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigRejectTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigShortDrainTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup11.setStatus("obsolete")

juniL2tpConfigGroup12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 20)
)
juniL2tpConfigGroup12.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIgnoreTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableDisconnectCauseAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableRxSpeedAvpWhenEqual"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigRejectTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigShortDrainTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestinationLockoutTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestinationLockoutTestEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigLockoutAction"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup12.setStatus("obsolete")

juniL2tpStatusGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 21)
)
juniL2tpStatusGroup4.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysStatusProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFirmwareRev"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusIfCounterDiscontinuityTime"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusLockoutState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusLockoutTimeRemaining"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLocalTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusInitiated"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteHostName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFirmwareRevision"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteBearerCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFramingCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendQueueDepth"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastResultCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorMessage"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusCumEstabTime"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLocalSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRemoteSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusUserName"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallSerialNumber"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusTxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallBearerType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusFramingType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPhysChanId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusDnis"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusClid"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSubAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPrivateGroupId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusProxyLcp"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusAuthMethod"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSequencingState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLacTunneledIfIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCumEstabTime"))
)
if mibBuilder.loadTexts:
    juniL2tpStatusGroup4.setStatus("obsolete")

juniL2tpConfigGroup13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 22)
)
juniL2tpConfigGroup13.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestructTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIpChecksumEnable"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelSwitchingEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigTunnelIdleTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverWithinPreference"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigWeightedLoadBalancing"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigControlRetransmissionsNotEstablished"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableChallenge"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDisableCallingNumberAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigIgnoreTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableDisconnectCauseAvp"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigReceiveWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigEnableRxSpeedAvpWhenEqual"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigRejectTxAddressChange"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigShortDrainTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestinationLockoutTimeout"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigDestinationLockoutTestEnabled"),
        ("Juniper-L2TP-MIB", "juniL2tpSysConfigFailoverResync"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestConfigLockoutAction"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelConfigAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigRowStatus"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    juniL2tpConfigGroup13.setStatus("current")

juniL2tpStatusGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 23)
)
juniL2tpStatusGroup5.setObjects(
      *(("Juniper-L2TP-MIB", "juniL2tpSysStatusProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFirmwareRev"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveDestinations"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusTotalSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusFailedSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusActiveSwitchedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpSysStatusIfCounterDiscontinuityTime"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedTunnelAuthens"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveTunnels"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusLockoutState"),
        ("Juniper-L2TP-MIB", "juniL2tpDestStatusLockoutTimeRemaining"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTransport"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLocalTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteTunnelId"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusInitiated"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteHostName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteVendorName"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFirmwareRevision"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteProtocolVersion"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteBearerCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRemoteFramingCapabilities"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendWindowSize"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendQueueDepth"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusRecvSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusSendSeqAck"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusTotalSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusFailedSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusActiveSessions"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastResultCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorCode"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusLastErrorMessage"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusCumEstabTime"),
        ("Juniper-L2TP-MIB", "juniL2tpTunnelStatusEffectiveFailoverResync"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLocalSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRemoteSessionId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusUserName"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusEffectiveAdminState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallSerialNumber"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusTxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRxConnectSpeed"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCallBearerType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusFramingType"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPhysChanId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusDnis"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusClid"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSubAddress"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusPrivateGroupId"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusProxyLcp"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusAuthMethod"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSequencingState"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusSendSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusRecvSeq"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusLacTunneledIfIndex"),
        ("Juniper-L2TP-MIB", "juniL2tpSessionStatusCumEstabTime"))
)
if mibBuilder.loadTexts:
    juniL2tpStatusGroup5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniL2tpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 1)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance.setStatus(
        "obsolete"
    )

juniL2tpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 2)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance2.setStatus(
        "obsolete"
    )

juniL2tpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 3)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance3.setStatus(
        "obsolete"
    )

juniL2tpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 4)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance4.setStatus(
        "obsolete"
    )

juniL2tpCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 5)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance5.setStatus(
        "obsolete"
    )

juniL2tpCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 6)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance6.setStatus(
        "obsolete"
    )

juniL2tpCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 7)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance7.setStatus(
        "obsolete"
    )

juniL2tpCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 8)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance8.setStatus(
        "obsolete"
    )

juniL2tpCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 9)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance9.setStatus(
        "obsolete"
    )

juniL2tpCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 10)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance10.setStatus(
        "obsolete"
    )

juniL2tpCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 11)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance11.setStatus(
        "obsolete"
    )

juniL2tpCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 12)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance12.setStatus(
        "obsolete"
    )

juniL2tpCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 13)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance13.setStatus(
        "current"
    )

juniL2tpCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 14)
)
if mibBuilder.loadTexts:
    juniL2tpCompliance14.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-L2TP-MIB",
    **{"JuniL2tpTunnelId": JuniL2tpTunnelId,
       "JuniL2tpSessionId": JuniL2tpSessionId,
       "JuniL2tpAdminState": JuniL2tpAdminState,
       "JuniL2tpTransport": JuniL2tpTransport,
       "JuniL2tpLockoutAction": JuniL2tpLockoutAction,
       "JuniL2tpLockoutState": JuniL2tpLockoutState,
       "juniL2tpMIB": juniL2tpMIB,
       "juniL2tpTraps": juniL2tpTraps,
       "juniL2tpObjects": juniL2tpObjects,
       "juniL2tpSystem": juniL2tpSystem,
       "juniL2tpSystemConfig": juniL2tpSystemConfig,
       "juniL2tpSysConfigAdminState": juniL2tpSysConfigAdminState,
       "juniL2tpSysConfigDestructTimeout": juniL2tpSysConfigDestructTimeout,
       "juniL2tpSysConfigIpChecksumEnable": juniL2tpSysConfigIpChecksumEnable,
       "juniL2tpSysConfigTunnelSwitchingEnabled": juniL2tpSysConfigTunnelSwitchingEnabled,
       "juniL2tpSysConfigControlRetransmissions": juniL2tpSysConfigControlRetransmissions,
       "juniL2tpSysConfigTunnelIdleTimeout": juniL2tpSysConfigTunnelIdleTimeout,
       "juniL2tpSysConfigReceiveDataSequencingIgnore": juniL2tpSysConfigReceiveDataSequencingIgnore,
       "juniL2tpSysConfigFailoverWithinPreference": juniL2tpSysConfigFailoverWithinPreference,
       "juniL2tpSysConfigWeightedLoadBalancing": juniL2tpSysConfigWeightedLoadBalancing,
       "juniL2tpSysConfigControlRetransmissionsEstablished": juniL2tpSysConfigControlRetransmissionsEstablished,
       "juniL2tpSysConfigControlRetransmissionsNotEstablished": juniL2tpSysConfigControlRetransmissionsNotEstablished,
       "juniL2tpSysConfigDisableChallenge": juniL2tpSysConfigDisableChallenge,
       "juniL2tpSysConfigDisableCallingNumberAvp": juniL2tpSysConfigDisableCallingNumberAvp,
       "juniL2tpSysConfigIgnoreTxAddressChange": juniL2tpSysConfigIgnoreTxAddressChange,
       "juniL2tpSysConfigEnableDisconnectCauseAvp": juniL2tpSysConfigEnableDisconnectCauseAvp,
       "juniL2tpSysConfigReceiveWindowSize": juniL2tpSysConfigReceiveWindowSize,
       "juniL2tpSysConfigEnableRxSpeedAvpWhenEqual": juniL2tpSysConfigEnableRxSpeedAvpWhenEqual,
       "juniL2tpSysConfigRejectTxAddressChange": juniL2tpSysConfigRejectTxAddressChange,
       "juniL2tpSysConfigShortDrainTimeout": juniL2tpSysConfigShortDrainTimeout,
       "juniL2tpSysConfigDestinationLockoutTestEnabled": juniL2tpSysConfigDestinationLockoutTestEnabled,
       "juniL2tpSysConfigDestinationLockoutTimeout": juniL2tpSysConfigDestinationLockoutTimeout,
       "juniL2tpSysConfigFailoverResync": juniL2tpSysConfigFailoverResync,
       "juniL2tpSystemStatus": juniL2tpSystemStatus,
       "juniL2tpSysStatusProtocolVersion": juniL2tpSysStatusProtocolVersion,
       "juniL2tpSysStatusVendorName": juniL2tpSysStatusVendorName,
       "juniL2tpSysStatusFirmwareRev": juniL2tpSysStatusFirmwareRev,
       "juniL2tpSysStatusTotalDestinations": juniL2tpSysStatusTotalDestinations,
       "juniL2tpSysStatusFailedDestinations": juniL2tpSysStatusFailedDestinations,
       "juniL2tpSysStatusActiveDestinations": juniL2tpSysStatusActiveDestinations,
       "juniL2tpSysStatusTotalTunnels": juniL2tpSysStatusTotalTunnels,
       "juniL2tpSysStatusFailedTunnels": juniL2tpSysStatusFailedTunnels,
       "juniL2tpSysStatusFailedTunnelAuthens": juniL2tpSysStatusFailedTunnelAuthens,
       "juniL2tpSysStatusActiveTunnels": juniL2tpSysStatusActiveTunnels,
       "juniL2tpSysStatusTotalSessions": juniL2tpSysStatusTotalSessions,
       "juniL2tpSysStatusFailedSessions": juniL2tpSysStatusFailedSessions,
       "juniL2tpSysStatusActiveSessions": juniL2tpSysStatusActiveSessions,
       "juniL2tpSysStatusTotalSwitchedSessions": juniL2tpSysStatusTotalSwitchedSessions,
       "juniL2tpSysStatusFailedSwitchedSessions": juniL2tpSysStatusFailedSwitchedSessions,
       "juniL2tpSysStatusActiveSwitchedSessions": juniL2tpSysStatusActiveSwitchedSessions,
       "juniL2tpSysStatusIfCounterDiscontinuityTime": juniL2tpSysStatusIfCounterDiscontinuityTime,
       "juniL2tpDestination": juniL2tpDestination,
       "juniL2tpDestConfig": juniL2tpDestConfig,
       "juniL2tpDestConfigTable": juniL2tpDestConfigTable,
       "juniL2tpDestConfigEntry": juniL2tpDestConfigEntry,
       "juniL2tpDestConfigIfIndex": juniL2tpDestConfigIfIndex,
       "juniL2tpDestConfigRowStatus": juniL2tpDestConfigRowStatus,
       "juniL2tpDestConfigAdminState": juniL2tpDestConfigAdminState,
       "juniL2tpDestConfigLockoutAction": juniL2tpDestConfigLockoutAction,
       "juniL2tpDestStatus": juniL2tpDestStatus,
       "juniL2tpDestStatusTable": juniL2tpDestStatusTable,
       "juniL2tpDestStatusEntry": juniL2tpDestStatusEntry,
       "juniL2tpDestStatusIfIndex": juniL2tpDestStatusIfIndex,
       "juniL2tpDestStatusTransport": juniL2tpDestStatusTransport,
       "juniL2tpDestStatusEffectiveAdminState": juniL2tpDestStatusEffectiveAdminState,
       "juniL2tpDestStatusTotalTunnels": juniL2tpDestStatusTotalTunnels,
       "juniL2tpDestStatusFailedTunnels": juniL2tpDestStatusFailedTunnels,
       "juniL2tpDestStatusFailedTunnelAuthens": juniL2tpDestStatusFailedTunnelAuthens,
       "juniL2tpDestStatusActiveTunnels": juniL2tpDestStatusActiveTunnels,
       "juniL2tpDestStatusTotalSessions": juniL2tpDestStatusTotalSessions,
       "juniL2tpDestStatusFailedSessions": juniL2tpDestStatusFailedSessions,
       "juniL2tpDestStatusActiveSessions": juniL2tpDestStatusActiveSessions,
       "juniL2tpDestStatusLockoutState": juniL2tpDestStatusLockoutState,
       "juniL2tpDestStatusLockoutTimeRemaining": juniL2tpDestStatusLockoutTimeRemaining,
       "juniL2tpDestStatistics": juniL2tpDestStatistics,
       "juniL2tpDestStatTable": juniL2tpDestStatTable,
       "juniL2tpDestStatEntry": juniL2tpDestStatEntry,
       "juniL2tpDestStatIfIndex": juniL2tpDestStatIfIndex,
       "juniL2tpDestStatCtlRecvOctets": juniL2tpDestStatCtlRecvOctets,
       "juniL2tpDestStatCtlRecvPackets": juniL2tpDestStatCtlRecvPackets,
       "juniL2tpDestStatCtlRecvErrors": juniL2tpDestStatCtlRecvErrors,
       "juniL2tpDestStatCtlRecvDiscards": juniL2tpDestStatCtlRecvDiscards,
       "juniL2tpDestStatCtlSendOctets": juniL2tpDestStatCtlSendOctets,
       "juniL2tpDestStatCtlSendPackets": juniL2tpDestStatCtlSendPackets,
       "juniL2tpDestStatCtlSendErrors": juniL2tpDestStatCtlSendErrors,
       "juniL2tpDestStatCtlSendDiscards": juniL2tpDestStatCtlSendDiscards,
       "juniL2tpDestStatPayRecvOctets": juniL2tpDestStatPayRecvOctets,
       "juniL2tpDestStatPayRecvPackets": juniL2tpDestStatPayRecvPackets,
       "juniL2tpDestStatPayRecvErrors": juniL2tpDestStatPayRecvErrors,
       "juniL2tpDestStatPayRecvDiscards": juniL2tpDestStatPayRecvDiscards,
       "juniL2tpDestStatPaySendOctets": juniL2tpDestStatPaySendOctets,
       "juniL2tpDestStatPaySendPackets": juniL2tpDestStatPaySendPackets,
       "juniL2tpDestStatPaySendErrors": juniL2tpDestStatPaySendErrors,
       "juniL2tpDestStatPaySendDiscards": juniL2tpDestStatPaySendDiscards,
       "juniL2tpTunnel": juniL2tpTunnel,
       "juniL2tpTunnelConfig": juniL2tpTunnelConfig,
       "juniL2tpTunnelConfigTable": juniL2tpTunnelConfigTable,
       "juniL2tpTunnelConfigEntry": juniL2tpTunnelConfigEntry,
       "juniL2tpTunnelConfigIfIndex": juniL2tpTunnelConfigIfIndex,
       "juniL2tpTunnelConfigRowStatus": juniL2tpTunnelConfigRowStatus,
       "juniL2tpTunnelConfigAdminState": juniL2tpTunnelConfigAdminState,
       "juniL2tpTunnelStatus": juniL2tpTunnelStatus,
       "juniL2tpTunnelStatusTable": juniL2tpTunnelStatusTable,
       "juniL2tpTunnelStatusEntry": juniL2tpTunnelStatusEntry,
       "juniL2tpTunnelStatusIfIndex": juniL2tpTunnelStatusIfIndex,
       "juniL2tpTunnelStatusTransport": juniL2tpTunnelStatusTransport,
       "juniL2tpTunnelStatusLocalTunnelId": juniL2tpTunnelStatusLocalTunnelId,
       "juniL2tpTunnelStatusRemoteTunnelId": juniL2tpTunnelStatusRemoteTunnelId,
       "juniL2tpTunnelStatusEffectiveAdminState": juniL2tpTunnelStatusEffectiveAdminState,
       "juniL2tpTunnelStatusState": juniL2tpTunnelStatusState,
       "juniL2tpTunnelStatusInitiated": juniL2tpTunnelStatusInitiated,
       "juniL2tpTunnelStatusRemoteHostName": juniL2tpTunnelStatusRemoteHostName,
       "juniL2tpTunnelStatusRemoteVendorName": juniL2tpTunnelStatusRemoteVendorName,
       "juniL2tpTunnelStatusRemoteFirmwareRevision": juniL2tpTunnelStatusRemoteFirmwareRevision,
       "juniL2tpTunnelStatusRemoteProtocolVersion": juniL2tpTunnelStatusRemoteProtocolVersion,
       "juniL2tpTunnelStatusRemoteBearerCapabilities": juniL2tpTunnelStatusRemoteBearerCapabilities,
       "juniL2tpTunnelStatusRemoteFramingCapabilities": juniL2tpTunnelStatusRemoteFramingCapabilities,
       "juniL2tpTunnelStatusRecvWindowSize": juniL2tpTunnelStatusRecvWindowSize,
       "juniL2tpTunnelStatusSendWindowSize": juniL2tpTunnelStatusSendWindowSize,
       "juniL2tpTunnelStatusSendQueueDepth": juniL2tpTunnelStatusSendQueueDepth,
       "juniL2tpTunnelStatusRecvSeq": juniL2tpTunnelStatusRecvSeq,
       "juniL2tpTunnelStatusRecvSeqAck": juniL2tpTunnelStatusRecvSeqAck,
       "juniL2tpTunnelStatusSendSeq": juniL2tpTunnelStatusSendSeq,
       "juniL2tpTunnelStatusSendSeqAck": juniL2tpTunnelStatusSendSeqAck,
       "juniL2tpTunnelStatusTotalSessions": juniL2tpTunnelStatusTotalSessions,
       "juniL2tpTunnelStatusFailedSessions": juniL2tpTunnelStatusFailedSessions,
       "juniL2tpTunnelStatusActiveSessions": juniL2tpTunnelStatusActiveSessions,
       "juniL2tpTunnelStatusLastResultCode": juniL2tpTunnelStatusLastResultCode,
       "juniL2tpTunnelStatusLastErrorCode": juniL2tpTunnelStatusLastErrorCode,
       "juniL2tpTunnelStatusLastErrorMessage": juniL2tpTunnelStatusLastErrorMessage,
       "juniL2tpTunnelStatusCumEstabTime": juniL2tpTunnelStatusCumEstabTime,
       "juniL2tpTunnelStatusEffectiveFailoverResync": juniL2tpTunnelStatusEffectiveFailoverResync,
       "juniL2tpTunnelStatistics": juniL2tpTunnelStatistics,
       "juniL2tpTunnelStatTable": juniL2tpTunnelStatTable,
       "juniL2tpTunnelStatEntry": juniL2tpTunnelStatEntry,
       "juniL2tpTunnelStatIfIndex": juniL2tpTunnelStatIfIndex,
       "juniL2tpTunnelStatCtlRecvOctets": juniL2tpTunnelStatCtlRecvOctets,
       "juniL2tpTunnelStatCtlRecvPackets": juniL2tpTunnelStatCtlRecvPackets,
       "juniL2tpTunnelStatCtlRecvErrors": juniL2tpTunnelStatCtlRecvErrors,
       "juniL2tpTunnelStatCtlRecvDiscards": juniL2tpTunnelStatCtlRecvDiscards,
       "juniL2tpTunnelStatCtlSendOctets": juniL2tpTunnelStatCtlSendOctets,
       "juniL2tpTunnelStatCtlSendPackets": juniL2tpTunnelStatCtlSendPackets,
       "juniL2tpTunnelStatCtlSendErrors": juniL2tpTunnelStatCtlSendErrors,
       "juniL2tpTunnelStatCtlSendDiscards": juniL2tpTunnelStatCtlSendDiscards,
       "juniL2tpTunnelStatPayRecvOctets": juniL2tpTunnelStatPayRecvOctets,
       "juniL2tpTunnelStatPayRecvPackets": juniL2tpTunnelStatPayRecvPackets,
       "juniL2tpTunnelStatPayRecvErrors": juniL2tpTunnelStatPayRecvErrors,
       "juniL2tpTunnelStatPayRecvDiscards": juniL2tpTunnelStatPayRecvDiscards,
       "juniL2tpTunnelStatPaySendOctets": juniL2tpTunnelStatPaySendOctets,
       "juniL2tpTunnelStatPaySendPackets": juniL2tpTunnelStatPaySendPackets,
       "juniL2tpTunnelStatPaySendErrors": juniL2tpTunnelStatPaySendErrors,
       "juniL2tpTunnelStatPaySendDiscards": juniL2tpTunnelStatPaySendDiscards,
       "juniL2tpTunnelStatCtlRecvZLB": juniL2tpTunnelStatCtlRecvZLB,
       "juniL2tpTunnelStatCtlRecvOutOfSequence": juniL2tpTunnelStatCtlRecvOutOfSequence,
       "juniL2tpTunnelStatCtlRecvOutOfWindow": juniL2tpTunnelStatCtlRecvOutOfWindow,
       "juniL2tpTunnelStatCtlSendZLB": juniL2tpTunnelStatCtlSendZLB,
       "juniL2tpTunnelStatCtlSendRetransmits": juniL2tpTunnelStatCtlSendRetransmits,
       "juniL2tpTunnelMap": juniL2tpTunnelMap,
       "juniL2tpMapTifSidToSifTable": juniL2tpMapTifSidToSifTable,
       "juniL2tpMapTifSidToSifEntry": juniL2tpMapTifSidToSifEntry,
       "juniL2tpMapTifSidToSifTunnelIfIndex": juniL2tpMapTifSidToSifTunnelIfIndex,
       "juniL2tpMapTifSidToSifLocalSessionId": juniL2tpMapTifSidToSifLocalSessionId,
       "juniL2tpMapTifSidToSifSessionIfIndex": juniL2tpMapTifSidToSifSessionIfIndex,
       "juniL2tpMapTidToTifTable": juniL2tpMapTidToTifTable,
       "juniL2tpMapTidToTifEntry": juniL2tpMapTidToTifEntry,
       "juniL2tpMapTidToTifLocalTunnelId": juniL2tpMapTidToTifLocalTunnelId,
       "juniL2tpMapTidToTifIfIndex": juniL2tpMapTidToTifIfIndex,
       "juniL2tpSession": juniL2tpSession,
       "juniL2tpSessionConfig": juniL2tpSessionConfig,
       "juniL2tpSessionConfigTable": juniL2tpSessionConfigTable,
       "juniL2tpSessionConfigEntry": juniL2tpSessionConfigEntry,
       "juniL2tpSessionConfigIfIndex": juniL2tpSessionConfigIfIndex,
       "juniL2tpSessionConfigRowStatus": juniL2tpSessionConfigRowStatus,
       "juniL2tpSessionConfigAdminState": juniL2tpSessionConfigAdminState,
       "juniL2tpSessionStatus": juniL2tpSessionStatus,
       "juniL2tpSessionStatusTable": juniL2tpSessionStatusTable,
       "juniL2tpSessionStatusEntry": juniL2tpSessionStatusEntry,
       "juniL2tpSessionStatusIfIndex": juniL2tpSessionStatusIfIndex,
       "juniL2tpSessionStatusLacPppIfIndex": juniL2tpSessionStatusLacPppIfIndex,
       "juniL2tpSessionStatusLocalSessionId": juniL2tpSessionStatusLocalSessionId,
       "juniL2tpSessionStatusRemoteSessionId": juniL2tpSessionStatusRemoteSessionId,
       "juniL2tpSessionStatusUserName": juniL2tpSessionStatusUserName,
       "juniL2tpSessionStatusEffectiveAdminState": juniL2tpSessionStatusEffectiveAdminState,
       "juniL2tpSessionStatusState": juniL2tpSessionStatusState,
       "juniL2tpSessionStatusCallType": juniL2tpSessionStatusCallType,
       "juniL2tpSessionStatusCallSerialNumber": juniL2tpSessionStatusCallSerialNumber,
       "juniL2tpSessionStatusTxConnectSpeed": juniL2tpSessionStatusTxConnectSpeed,
       "juniL2tpSessionStatusRxConnectSpeed": juniL2tpSessionStatusRxConnectSpeed,
       "juniL2tpSessionStatusCallBearerType": juniL2tpSessionStatusCallBearerType,
       "juniL2tpSessionStatusFramingType": juniL2tpSessionStatusFramingType,
       "juniL2tpSessionStatusPhysChanId": juniL2tpSessionStatusPhysChanId,
       "juniL2tpSessionStatusDnis": juniL2tpSessionStatusDnis,
       "juniL2tpSessionStatusClid": juniL2tpSessionStatusClid,
       "juniL2tpSessionStatusSubAddress": juniL2tpSessionStatusSubAddress,
       "juniL2tpSessionStatusPrivateGroupId": juniL2tpSessionStatusPrivateGroupId,
       "juniL2tpSessionStatusProxyLcp": juniL2tpSessionStatusProxyLcp,
       "juniL2tpSessionStatusAuthMethod": juniL2tpSessionStatusAuthMethod,
       "juniL2tpSessionStatusSequencingState": juniL2tpSessionStatusSequencingState,
       "juniL2tpSessionStatusSendSeq": juniL2tpSessionStatusSendSeq,
       "juniL2tpSessionStatusRecvSeq": juniL2tpSessionStatusRecvSeq,
       "juniL2tpSessionStatusLacTunneledIfIndex": juniL2tpSessionStatusLacTunneledIfIndex,
       "juniL2tpSessionStatusCumEstabTime": juniL2tpSessionStatusCumEstabTime,
       "juniL2tpSessionStatistics": juniL2tpSessionStatistics,
       "juniL2tpSessionStatTable": juniL2tpSessionStatTable,
       "juniL2tpSessionStatEntry": juniL2tpSessionStatEntry,
       "juniL2tpSessionStatIfIndex": juniL2tpSessionStatIfIndex,
       "juniL2tpSessionStatPayRecvOctets": juniL2tpSessionStatPayRecvOctets,
       "juniL2tpSessionStatPayRecvPackets": juniL2tpSessionStatPayRecvPackets,
       "juniL2tpSessionStatPayRecvErrors": juniL2tpSessionStatPayRecvErrors,
       "juniL2tpSessionStatPayRecvDiscards": juniL2tpSessionStatPayRecvDiscards,
       "juniL2tpSessionStatPaySendOctets": juniL2tpSessionStatPaySendOctets,
       "juniL2tpSessionStatPaySendPackets": juniL2tpSessionStatPaySendPackets,
       "juniL2tpSessionStatPaySendErrors": juniL2tpSessionStatPaySendErrors,
       "juniL2tpSessionStatPaySendDiscards": juniL2tpSessionStatPaySendDiscards,
       "juniL2tpSessionStatRecvOutOfSequence": juniL2tpSessionStatRecvOutOfSequence,
       "juniL2tpSessionStatResequencingTimeouts": juniL2tpSessionStatResequencingTimeouts,
       "juniL2tpSessionStatPayLostPackets": juniL2tpSessionStatPayLostPackets,
       "juniL2tpTransport": juniL2tpTransport,
       "juniL2tpTransportUdpIp": juniL2tpTransportUdpIp,
       "juniL2tpUdpIpSystem": juniL2tpUdpIpSystem,
       "juniL2tpUdpIpDestination": juniL2tpUdpIpDestination,
       "juniL2tpUdpIpDestTable": juniL2tpUdpIpDestTable,
       "juniL2tpUdpIpDestEntry": juniL2tpUdpIpDestEntry,
       "juniL2tpUdpIpDestIfIndex": juniL2tpUdpIpDestIfIndex,
       "juniL2tpUdpIpDestRouterIndex": juniL2tpUdpIpDestRouterIndex,
       "juniL2tpUdpIpDestLocalAddress": juniL2tpUdpIpDestLocalAddress,
       "juniL2tpUdpIpDestRemoteAddress": juniL2tpUdpIpDestRemoteAddress,
       "juniL2tpUdpIpTunnel": juniL2tpUdpIpTunnel,
       "juniL2tpUdpIpTunnelTable": juniL2tpUdpIpTunnelTable,
       "juniL2tpUdpIpTunnelEntry": juniL2tpUdpIpTunnelEntry,
       "juniL2tpUdpIpTunnelIfIndex": juniL2tpUdpIpTunnelIfIndex,
       "juniL2tpUdpIpTunnelRouterIndex": juniL2tpUdpIpTunnelRouterIndex,
       "juniL2tpUdpIpTunnelLocalAddress": juniL2tpUdpIpTunnelLocalAddress,
       "juniL2tpUdpIpTunnelLocalPort": juniL2tpUdpIpTunnelLocalPort,
       "juniL2tpUdpIpTunnelRemoteAddress": juniL2tpUdpIpTunnelRemoteAddress,
       "juniL2tpUdpIpTunnelRemotePort": juniL2tpUdpIpTunnelRemotePort,
       "juniL2tpUdpIpTunnelRemoteReceiveAddress": juniL2tpUdpIpTunnelRemoteReceiveAddress,
       "juniL2tpUdpIpTunnelRemoteReceivePort": juniL2tpUdpIpTunnelRemoteReceivePort,
       "juniL2tpUdpIpSession": juniL2tpUdpIpSession,
       "juniL2tpTrapControl": juniL2tpTrapControl,
       "juniL2tpConformance": juniL2tpConformance,
       "juniL2tpGroups": juniL2tpGroups,
       "juniL2tpConfigGroup": juniL2tpConfigGroup,
       "juniL2tpStatusGroup": juniL2tpStatusGroup,
       "juniL2tpStatGroup": juniL2tpStatGroup,
       "juniL2tpMapGroup": juniL2tpMapGroup,
       "juniL2tpUdpIpGroup": juniL2tpUdpIpGroup,
       "juniL2tpStatusGroup2": juniL2tpStatusGroup2,
       "juniL2tpStatGroup2": juniL2tpStatGroup2,
       "juniL2tpConfigGroup2": juniL2tpConfigGroup2,
       "juniL2tpConfigGroup3": juniL2tpConfigGroup3,
       "juniL2tpConfigGroup4": juniL2tpConfigGroup4,
       "juniL2tpConfigGroup5": juniL2tpConfigGroup5,
       "juniL2tpConfigGroup6": juniL2tpConfigGroup6,
       "juniL2tpConfigGroup7": juniL2tpConfigGroup7,
       "juniL2tpUdpIpGroup1": juniL2tpUdpIpGroup1,
       "juniL2tpConfigGroup8": juniL2tpConfigGroup8,
       "juniL2tpConfigGroup9": juniL2tpConfigGroup9,
       "juniL2tpConfigGroup10": juniL2tpConfigGroup10,
       "juniL2tpStatusGroup3": juniL2tpStatusGroup3,
       "juniL2tpConfigGroup11": juniL2tpConfigGroup11,
       "juniL2tpConfigGroup12": juniL2tpConfigGroup12,
       "juniL2tpStatusGroup4": juniL2tpStatusGroup4,
       "juniL2tpConfigGroup13": juniL2tpConfigGroup13,
       "juniL2tpStatusGroup5": juniL2tpStatusGroup5,
       "juniL2tpCompliances": juniL2tpCompliances,
       "juniL2tpCompliance": juniL2tpCompliance,
       "juniL2tpCompliance2": juniL2tpCompliance2,
       "juniL2tpCompliance3": juniL2tpCompliance3,
       "juniL2tpCompliance4": juniL2tpCompliance4,
       "juniL2tpCompliance5": juniL2tpCompliance5,
       "juniL2tpCompliance6": juniL2tpCompliance6,
       "juniL2tpCompliance7": juniL2tpCompliance7,
       "juniL2tpCompliance8": juniL2tpCompliance8,
       "juniL2tpCompliance9": juniL2tpCompliance9,
       "juniL2tpCompliance10": juniL2tpCompliance10,
       "juniL2tpCompliance11": juniL2tpCompliance11,
       "juniL2tpCompliance12": juniL2tpCompliance12,
       "juniL2tpCompliance13": juniL2tpCompliance13,
       "juniL2tpCompliance14": juniL2tpCompliance14}
)
