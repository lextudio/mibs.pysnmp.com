# SNMP MIB module (CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:56 2024
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

(dot1dStpPortDesignatedBridge,
 dot1dStpPortDesignatedPort,
 dot1dStpPortState) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPortDesignatedBridge",
    "dot1dStpPortDesignatedPort",
    "dot1dStpPortState")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(HpPartnerDeviceType,
 HpPartnerDeviceTypeList) = mibBuilder.importSymbols(
    "HP-ICF-DEV-CONF-MIB",
    "HpPartnerDeviceType",
    "HpPartnerDeviceTypeList")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ConfigStatus,
 HpSwitchIfMauAutoNegCapAdvertisedBits,
 HpSwitchIfMauAutoNegCapReceivedBits,
 HpSwitchIfMauAutoNegCapabilityBits,
 HpSwitchIfMauTypeListBits,
 HpSwitchPortType) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "ConfigStatus",
    "HpSwitchIfMauAutoNegCapAdvertisedBits",
    "HpSwitchIfMauAutoNegCapReceivedBits",
    "HpSwitchIfMauAutoNegCapabilityBits",
    "HpSwitchIfMauTypeListBits",
    "HpSwitchPortType")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class VlanID(Integer32):
    """Custom type VlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



class HpicfUsrProfilePortSpeed(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("speed1000FDx", 6),
          ("speed100FDx", 4),
          ("speed100HDX", 2),
          ("speed10FDx", 3),
          ("speed10HDX", 1),
          ("speedAuto", 5),
          ("speedAuto-10Gbits", 10),
          ("speedAuto1000Mbits", 9),
          ("speedAuto100Mbits", 8),
          ("speedAuto10Mbits", 7),
          ("speedAuto10or100Mbits", 11))
    )



# MIB Managed Objects in the order of their OIDs

_HpConfig_ObjectIdentity = ObjectIdentity
hpConfig = _HpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7)
)
_HpSwitchConfig_ObjectIdentity = ObjectIdentity
hpSwitchConfig = _HpSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1)
)
_HpSwitchTraps_ObjectIdentity = ObjectIdentity
hpSwitchTraps = _HpSwitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 0)
)
_HpSwitchTrapsObjects_ObjectIdentity = ObjectIdentity
hpSwitchTrapsObjects = _HpSwitchTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 0, 1)
)


class _HpSwitchStpErrantBpduDetector_Type(Integer32):
    """Custom type hpSwitchStpErrantBpduDetector based on Integer32"""
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
        *(("bpduFilter", 1),
          ("bpduProtection", 2),
          ("pvstFilter", 3),
          ("pvstProtection", 4))
    )


_HpSwitchStpErrantBpduDetector_Type.__name__ = "Integer32"
_HpSwitchStpErrantBpduDetector_Object = MibScalar
hpSwitchStpErrantBpduDetector = _HpSwitchStpErrantBpduDetector_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 0, 1, 1),
    _HpSwitchStpErrantBpduDetector_Type()
)
hpSwitchStpErrantBpduDetector.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpSwitchStpErrantBpduDetector.setStatus("optional")
_HpSwitchStpErrantBpduSrcMac_Type = MacAddress
_HpSwitchStpErrantBpduSrcMac_Object = MibScalar
hpSwitchStpErrantBpduSrcMac = _HpSwitchStpErrantBpduSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 0, 1, 2),
    _HpSwitchStpErrantBpduSrcMac_Type()
)
hpSwitchStpErrantBpduSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpSwitchStpErrantBpduSrcMac.setStatus("optional")
_HpSwitchSystemConfig_ObjectIdentity = ObjectIdentity
hpSwitchSystemConfig = _HpSwitchSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1)
)


class _HpSwitchAutoReboot_Type(Integer32):
    """Custom type hpSwitchAutoReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("useHw", 3),
          ("yes", 1))
    )


_HpSwitchAutoReboot_Type.__name__ = "Integer32"
_HpSwitchAutoReboot_Object = MibScalar
hpSwitchAutoReboot = _HpSwitchAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 1),
    _HpSwitchAutoReboot_Type()
)
hpSwitchAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAutoReboot.setStatus("mandatory")


class _HpSwitchTimeZone_Type(Integer32):
    """Custom type hpSwitchTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 840),
    )


_HpSwitchTimeZone_Type.__name__ = "Integer32"
_HpSwitchTimeZone_Object = MibScalar
hpSwitchTimeZone = _HpSwitchTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 2),
    _HpSwitchTimeZone_Type()
)
hpSwitchTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTimeZone.setStatus("mandatory")


class _HpSwitchDaylightTimeRule_Type(Integer32):
    """Custom type hpSwitchDaylightTimeRule based on Integer32"""
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
        *(("alaska", 2),
          ("canadaAndContinentalUS", 3),
          ("middleEuropeAndPortugal", 4),
          ("none", 1),
          ("southernHemisphere", 5),
          ("userDefined", 7),
          ("westernEurop", 6))
    )


_HpSwitchDaylightTimeRule_Type.__name__ = "Integer32"
_HpSwitchDaylightTimeRule_Object = MibScalar
hpSwitchDaylightTimeRule = _HpSwitchDaylightTimeRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 3),
    _HpSwitchDaylightTimeRule_Type()
)
hpSwitchDaylightTimeRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDaylightTimeRule.setStatus("mandatory")


class _HpSwitchDaylightBeginningMonth_Type(Integer32):
    """Custom type hpSwitchDaylightBeginningMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HpSwitchDaylightBeginningMonth_Type.__name__ = "Integer32"
_HpSwitchDaylightBeginningMonth_Object = MibScalar
hpSwitchDaylightBeginningMonth = _HpSwitchDaylightBeginningMonth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 4),
    _HpSwitchDaylightBeginningMonth_Type()
)
hpSwitchDaylightBeginningMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDaylightBeginningMonth.setStatus("mandatory")


class _HpSwitchDaylightBeginningDay_Type(Integer32):
    """Custom type hpSwitchDaylightBeginningDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HpSwitchDaylightBeginningDay_Type.__name__ = "Integer32"
_HpSwitchDaylightBeginningDay_Object = MibScalar
hpSwitchDaylightBeginningDay = _HpSwitchDaylightBeginningDay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 5),
    _HpSwitchDaylightBeginningDay_Type()
)
hpSwitchDaylightBeginningDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDaylightBeginningDay.setStatus("mandatory")


class _HpSwitchDaylightEndingMonth_Type(Integer32):
    """Custom type hpSwitchDaylightEndingMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HpSwitchDaylightEndingMonth_Type.__name__ = "Integer32"
_HpSwitchDaylightEndingMonth_Object = MibScalar
hpSwitchDaylightEndingMonth = _HpSwitchDaylightEndingMonth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 6),
    _HpSwitchDaylightEndingMonth_Type()
)
hpSwitchDaylightEndingMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDaylightEndingMonth.setStatus("mandatory")


class _HpSwitchDaylightEndingDay_Type(Integer32):
    """Custom type hpSwitchDaylightEndingDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HpSwitchDaylightEndingDay_Type.__name__ = "Integer32"
_HpSwitchDaylightEndingDay_Object = MibScalar
hpSwitchDaylightEndingDay = _HpSwitchDaylightEndingDay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 7),
    _HpSwitchDaylightEndingDay_Type()
)
hpSwitchDaylightEndingDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDaylightEndingDay.setStatus("mandatory")
_HpSwitchSystemConfigStatus_Type = ConfigStatus
_HpSwitchSystemConfigStatus_Object = MibScalar
hpSwitchSystemConfigStatus = _HpSwitchSystemConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 8),
    _HpSwitchSystemConfigStatus_Type()
)
hpSwitchSystemConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchSystemConfigStatus.setStatus("mandatory")


class _HpSwitchSystemPortLEDMode_Type(Integer32):
    """Custom type hpSwitchSystemPortLEDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-activity", 1),
          ("link-only", 2))
    )


_HpSwitchSystemPortLEDMode_Type.__name__ = "Integer32"
_HpSwitchSystemPortLEDMode_Object = MibScalar
hpSwitchSystemPortLEDMode = _HpSwitchSystemPortLEDMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 9),
    _HpSwitchSystemPortLEDMode_Type()
)
hpSwitchSystemPortLEDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSystemPortLEDMode.setStatus("mandatory")


class _HpSwitchControlUnknownIPMulticast_Type(Integer32):
    """Custom type hpSwitchControlUnknownIPMulticast based on Integer32"""
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


_HpSwitchControlUnknownIPMulticast_Type.__name__ = "Integer32"
_HpSwitchControlUnknownIPMulticast_Object = MibScalar
hpSwitchControlUnknownIPMulticast = _HpSwitchControlUnknownIPMulticast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 10),
    _HpSwitchControlUnknownIPMulticast_Type()
)
hpSwitchControlUnknownIPMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchControlUnknownIPMulticast.setStatus("mandatory")


class _HpSwitchIgmpDelayedGroupFlushTimer_Type(Integer32):
    """Custom type hpSwitchIgmpDelayedGroupFlushTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchIgmpDelayedGroupFlushTimer_Type.__name__ = "Integer32"
_HpSwitchIgmpDelayedGroupFlushTimer_Object = MibScalar
hpSwitchIgmpDelayedGroupFlushTimer = _HpSwitchIgmpDelayedGroupFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 11),
    _HpSwitchIgmpDelayedGroupFlushTimer_Type()
)
hpSwitchIgmpDelayedGroupFlushTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpDelayedGroupFlushTimer.setStatus("mandatory")


class _HpSwitchMaxFrameSize_Type(Integer32):
    """Custom type hpSwitchMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchMaxFrameSize_Type.__name__ = "Integer32"
_HpSwitchMaxFrameSize_Object = MibScalar
hpSwitchMaxFrameSize = _HpSwitchMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 12),
    _HpSwitchMaxFrameSize_Type()
)
hpSwitchMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMaxFrameSize.setStatus("mandatory")


class _HpSwitchIpMTU_Type(Integer32):
    """Custom type hpSwitchIpMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIpMTU_Type.__name__ = "Integer32"
_HpSwitchIpMTU_Object = MibScalar
hpSwitchIpMTU = _HpSwitchIpMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 13),
    _HpSwitchIpMTU_Type()
)
hpSwitchIpMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpMTU.setStatus("mandatory")


class _HpSwitchAllowV1Modules_Type(Integer32):
    """Custom type hpSwitchAllowV1Modules based on Integer32"""
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


_HpSwitchAllowV1Modules_Type.__name__ = "Integer32"
_HpSwitchAllowV1Modules_Object = MibScalar
hpSwitchAllowV1Modules = _HpSwitchAllowV1Modules_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 14),
    _HpSwitchAllowV1Modules_Type()
)
hpSwitchAllowV1Modules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAllowV1Modules.setStatus("mandatory")


class _HpSwitchAllowV2Modules_Type(Integer32):
    """Custom type hpSwitchAllowV2Modules based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("erase", 3))
    )


_HpSwitchAllowV2Modules_Type.__name__ = "Integer32"
_HpSwitchAllowV2Modules_Object = MibScalar
hpSwitchAllowV2Modules = _HpSwitchAllowV2Modules_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 15),
    _HpSwitchAllowV2Modules_Type()
)
hpSwitchAllowV2Modules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAllowV2Modules.setStatus("mandatory")
_HpicfPrivateVlanPromiscuousPorts_Type = PortList
_HpicfPrivateVlanPromiscuousPorts_Object = MibScalar
hpicfPrivateVlanPromiscuousPorts = _HpicfPrivateVlanPromiscuousPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 16),
    _HpicfPrivateVlanPromiscuousPorts_Type()
)
hpicfPrivateVlanPromiscuousPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPrivateVlanPromiscuousPorts.setStatus("optional")


class _HpSwitchPreviewMode_Type(Integer32):
    """Custom type hpSwitchPreviewMode based on Integer32"""
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


_HpSwitchPreviewMode_Type.__name__ = "Integer32"
_HpSwitchPreviewMode_Object = MibScalar
hpSwitchPreviewMode = _HpSwitchPreviewMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 17),
    _HpSwitchPreviewMode_Type()
)
hpSwitchPreviewMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPreviewMode.setStatus("mandatory")


class _HpSwitchHibernate_Type(Integer32):
    """Custom type hpSwitchHibernate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpSwitchHibernate_Type.__name__ = "Integer32"
_HpSwitchHibernate_Object = MibScalar
hpSwitchHibernate = _HpSwitchHibernate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 18),
    _HpSwitchHibernate_Type()
)
hpSwitchHibernate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchHibernate.setStatus("mandatory")


class _HpSwitchMacDelimiter_Type(Integer32):
    """Custom type hpSwitchMacDelimiter based on Integer32"""
    defaultValue = 1

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
        *(("colon", 2),
          ("default", 1),
          ("hyphen", 3),
          ("none", 5),
          ("ouinic", 4))
    )


_HpSwitchMacDelimiter_Type.__name__ = "Integer32"
_HpSwitchMacDelimiter_Object = MibScalar
hpSwitchMacDelimiter = _HpSwitchMacDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 19),
    _HpSwitchMacDelimiter_Type()
)
hpSwitchMacDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMacDelimiter.setStatus("mandatory")


class _HpicfSwitchCLIOptimization_Type(Integer32):
    """Custom type hpicfSwitchCLIOptimization based on Integer32"""
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


_HpicfSwitchCLIOptimization_Type.__name__ = "Integer32"
_HpicfSwitchCLIOptimization_Object = MibScalar
hpicfSwitchCLIOptimization = _HpicfSwitchCLIOptimization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 1, 20),
    _HpicfSwitchCLIOptimization_Type()
)
hpicfSwitchCLIOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSwitchCLIOptimization.setStatus("mandatory")
_HpSwitchConsoleConfig_ObjectIdentity = ObjectIdentity
hpSwitchConsoleConfig = _HpSwitchConsoleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2)
)


class _HpSwitchTelnetAdminStatus_Type(Integer32):
    """Custom type hpSwitchTelnetAdminStatus based on Integer32"""
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


_HpSwitchTelnetAdminStatus_Type.__name__ = "Integer32"
_HpSwitchTelnetAdminStatus_Object = MibScalar
hpSwitchTelnetAdminStatus = _HpSwitchTelnetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 1),
    _HpSwitchTelnetAdminStatus_Type()
)
hpSwitchTelnetAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTelnetAdminStatus.setStatus("obsolete")


class _HpSwitchTerminalType_Type(Integer32):
    """Custom type hpSwitchTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 4),
          ("vt100", 2))
    )


_HpSwitchTerminalType_Type.__name__ = "Integer32"
_HpSwitchTerminalType_Object = MibScalar
hpSwitchTerminalType = _HpSwitchTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 2),
    _HpSwitchTerminalType_Type()
)
hpSwitchTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTerminalType.setStatus("mandatory")


class _HpSwitchConsoleRefRate_Type(Integer32):
    """Custom type hpSwitchConsoleRefRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              10,
              20,
              30,
              45,
              60)
        )
    )
    namedValues = NamedValues(
        *(("refRate", 60),
          ("refRate1", 1),
          ("refRate10", 10),
          ("refRate20", 20),
          ("refRate3", 3),
          ("refRate30", 30),
          ("refRate45", 45),
          ("refRate5", 5))
    )


_HpSwitchConsoleRefRate_Type.__name__ = "Integer32"
_HpSwitchConsoleRefRate_Object = MibScalar
hpSwitchConsoleRefRate = _HpSwitchConsoleRefRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 3),
    _HpSwitchConsoleRefRate_Type()
)
hpSwitchConsoleRefRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchConsoleRefRate.setStatus("mandatory")


class _HpSwitchDisplayedEvent_Type(Integer32):
    """Custom type hpSwitchDisplayedEvent based on Integer32"""
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
        *(("all", 4),
          ("debug", 5),
          ("major", 2),
          ("none", 1),
          ("notInfo", 3))
    )


_HpSwitchDisplayedEvent_Type.__name__ = "Integer32"
_HpSwitchDisplayedEvent_Object = MibScalar
hpSwitchDisplayedEvent = _HpSwitchDisplayedEvent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 4),
    _HpSwitchDisplayedEvent_Type()
)
hpSwitchDisplayedEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDisplayedEvent.setStatus("mandatory")
_HpSwitchConsoleConfigStatus_Type = ConfigStatus
_HpSwitchConsoleConfigStatus_Object = MibScalar
hpSwitchConsoleConfigStatus = _HpSwitchConsoleConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 5),
    _HpSwitchConsoleConfigStatus_Type()
)
hpSwitchConsoleConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchConsoleConfigStatus.setStatus("mandatory")


class _HpSwitchConsoleConfigLogoutPrompt_Type(TruthValue):
    """Custom type hpSwitchConsoleConfigLogoutPrompt based on TruthValue"""


_HpSwitchConsoleConfigLogoutPrompt_Object = MibScalar
hpSwitchConsoleConfigLogoutPrompt = _HpSwitchConsoleConfigLogoutPrompt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 6),
    _HpSwitchConsoleConfigLogoutPrompt_Type()
)
hpSwitchConsoleConfigLogoutPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchConsoleConfigLogoutPrompt.setStatus("mandatory")


class _HpSwitchUsbConsoleAdminStatus_Type(Integer32):
    """Custom type hpSwitchUsbConsoleAdminStatus based on Integer32"""
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


_HpSwitchUsbConsoleAdminStatus_Type.__name__ = "Integer32"
_HpSwitchUsbConsoleAdminStatus_Object = MibScalar
hpSwitchUsbConsoleAdminStatus = _HpSwitchUsbConsoleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 7),
    _HpSwitchUsbConsoleAdminStatus_Type()
)
hpSwitchUsbConsoleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchUsbConsoleAdminStatus.setStatus("optional")


class _HpSwitchSessionGlobalIdleTimeout_Type(Integer32):
    """Custom type hpSwitchSessionGlobalIdleTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_HpSwitchSessionGlobalIdleTimeout_Type.__name__ = "Integer32"
_HpSwitchSessionGlobalIdleTimeout_Object = MibScalar
hpSwitchSessionGlobalIdleTimeout = _HpSwitchSessionGlobalIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 8),
    _HpSwitchSessionGlobalIdleTimeout_Type()
)
hpSwitchSessionGlobalIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSessionGlobalIdleTimeout.setStatus("mandatory")


class _HpSwitchSessionConsoleIdleTimeout_Type(Integer32):
    """Custom type hpSwitchSessionConsoleIdleTimeout based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7200),
    )


_HpSwitchSessionConsoleIdleTimeout_Type.__name__ = "Integer32"
_HpSwitchSessionConsoleIdleTimeout_Object = MibScalar
hpSwitchSessionConsoleIdleTimeout = _HpSwitchSessionConsoleIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 9),
    _HpSwitchSessionConsoleIdleTimeout_Type()
)
hpSwitchSessionConsoleIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSessionConsoleIdleTimeout.setStatus("mandatory")


class _HpSwitchMaxSessions_Type(Integer32):
    """Custom type hpSwitchMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_HpSwitchMaxSessions_Type.__name__ = "Integer32"
_HpSwitchMaxSessions_Object = MibScalar
hpSwitchMaxSessions = _HpSwitchMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 10),
    _HpSwitchMaxSessions_Type()
)
hpSwitchMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMaxSessions.setStatus("mandatory")


class _HpSwitchMaxUserSessions_Type(Integer32):
    """Custom type hpSwitchMaxUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_HpSwitchMaxUserSessions_Type.__name__ = "Integer32"
_HpSwitchMaxUserSessions_Object = MibScalar
hpSwitchMaxUserSessions = _HpSwitchMaxUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 2, 11),
    _HpSwitchMaxUserSessions_Type()
)
hpSwitchMaxUserSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMaxUserSessions.setStatus("mandatory")
_HpSwitchPortConfig_ObjectIdentity = ObjectIdentity
hpSwitchPortConfig = _HpSwitchPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3)
)
_HpSwitchPortTable_Object = MibTable
hpSwitchPortTable = _HpSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpSwitchPortTable.setStatus("mandatory")
_HpSwitchPortEntry_Object = MibTableRow
hpSwitchPortEntry = _HpSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1)
)
hpSwitchPortEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchPortEntry.setStatus("mandatory")


class _HpSwitchPortIndex_Type(Integer32):
    """Custom type hpSwitchPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchPortIndex_Type.__name__ = "Integer32"
_HpSwitchPortIndex_Object = MibTableColumn
hpSwitchPortIndex = _HpSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 1),
    _HpSwitchPortIndex_Type()
)
hpSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortIndex.setStatus("mandatory")
_HpSwitchPortType_Type = HpSwitchPortType
_HpSwitchPortType_Object = MibTableColumn
hpSwitchPortType = _HpSwitchPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 2),
    _HpSwitchPortType_Type()
)
hpSwitchPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortType.setStatus("mandatory")


class _HpSwitchPortDescr_Type(DisplayString):
    """Custom type hpSwitchPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchPortDescr_Type.__name__ = "DisplayString"
_HpSwitchPortDescr_Object = MibTableColumn
hpSwitchPortDescr = _HpSwitchPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 3),
    _HpSwitchPortDescr_Type()
)
hpSwitchPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortDescr.setStatus("mandatory")


class _HpSwitchPortAdminStatus_Type(Integer32):
    """Custom type hpSwitchPortAdminStatus based on Integer32"""
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


_HpSwitchPortAdminStatus_Type.__name__ = "Integer32"
_HpSwitchPortAdminStatus_Object = MibTableColumn
hpSwitchPortAdminStatus = _HpSwitchPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 4),
    _HpSwitchPortAdminStatus_Type()
)
hpSwitchPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortAdminStatus.setStatus("obsolete")


class _HpSwitchPortEtherMode_Type(Integer32):
    """Custom type hpSwitchPortEtherMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1))
    )


_HpSwitchPortEtherMode_Type.__name__ = "Integer32"
_HpSwitchPortEtherMode_Object = MibTableColumn
hpSwitchPortEtherMode = _HpSwitchPortEtherMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 5),
    _HpSwitchPortEtherMode_Type()
)
hpSwitchPortEtherMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortEtherMode.setStatus("mandatory")


class _HpSwitchPortVgMode_Type(Integer32):
    """Custom type hpSwitchPortVgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 3),
          ("endNode", 2),
          ("master", 1))
    )


_HpSwitchPortVgMode_Type.__name__ = "Integer32"
_HpSwitchPortVgMode_Object = MibTableColumn
hpSwitchPortVgMode = _HpSwitchPortVgMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 6),
    _HpSwitchPortVgMode_Type()
)
hpSwitchPortVgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortVgMode.setStatus("mandatory")


class _HpSwitchPortLinkbeat_Type(Integer32):
    """Custom type hpSwitchPortLinkbeat based on Integer32"""
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


_HpSwitchPortLinkbeat_Type.__name__ = "Integer32"
_HpSwitchPortLinkbeat_Object = MibTableColumn
hpSwitchPortLinkbeat = _HpSwitchPortLinkbeat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 7),
    _HpSwitchPortLinkbeat_Type()
)
hpSwitchPortLinkbeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortLinkbeat.setStatus("mandatory")


class _HpSwitchPortTrunkGroup_Type(Integer32):
    """Custom type hpSwitchPortTrunkGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchPortTrunkGroup_Type.__name__ = "Integer32"
_HpSwitchPortTrunkGroup_Object = MibTableColumn
hpSwitchPortTrunkGroup = _HpSwitchPortTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 8),
    _HpSwitchPortTrunkGroup_Type()
)
hpSwitchPortTrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortTrunkGroup.setStatus("mandatory")


class _HpSwitchPortBcastLimit_Type(Integer32):
    """Custom type hpSwitchPortBcastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_HpSwitchPortBcastLimit_Type.__name__ = "Integer32"
_HpSwitchPortBcastLimit_Object = MibTableColumn
hpSwitchPortBcastLimit = _HpSwitchPortBcastLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 9),
    _HpSwitchPortBcastLimit_Type()
)
hpSwitchPortBcastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortBcastLimit.setStatus("mandatory")


class _HpSwitchPortFastEtherMode_Type(Integer32):
    """Custom type hpSwitchPortFastEtherMode based on Integer32"""
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
        *(("auto-10-100Mbits", 11),
          ("auto-1000-2500-5000Mbits", 17),
          ("auto-1000-2500Mbits", 16),
          ("auto-1000Mbits", 9),
          ("auto-100Mbits", 8),
          ("auto-10Gbits", 10),
          ("auto-10Mbits", 7),
          ("auto-2500-5000Mbits", 15),
          ("auto-2500Mbits", 13),
          ("auto-40Gbits", 12),
          ("auto-5000Mbits", 14),
          ("auto-neg", 5),
          ("full-duplex-1000Mbits", 6),
          ("full-duplex-100Mbits", 4),
          ("full-duplex-10Mbits", 3),
          ("half-duplex-100Mbits", 2),
          ("half-duplex-10Mbits", 1))
    )


_HpSwitchPortFastEtherMode_Type.__name__ = "Integer32"
_HpSwitchPortFastEtherMode_Object = MibTableColumn
hpSwitchPortFastEtherMode = _HpSwitchPortFastEtherMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 10),
    _HpSwitchPortFastEtherMode_Type()
)
hpSwitchPortFastEtherMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortFastEtherMode.setStatus("mandatory")


class _HpSwitchPortFlowControl_Type(Integer32):
    """Custom type hpSwitchPortFlowControl based on Integer32"""
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


_HpSwitchPortFlowControl_Type.__name__ = "Integer32"
_HpSwitchPortFlowControl_Object = MibTableColumn
hpSwitchPortFlowControl = _HpSwitchPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 11),
    _HpSwitchPortFlowControl_Type()
)
hpSwitchPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortFlowControl.setStatus("mandatory")


class _HpSwitchPortTrunkType_Type(Integer32):
    """Custom type hpSwitchPortTrunkType based on Integer32"""
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
        *(("dtLacpTrk", 6),
          ("dtTrunk", 7),
          ("fecAuto", 2),
          ("lacpTrk", 4),
          ("none", 5),
          ("saTrunk", 3),
          ("trunk", 1))
    )


_HpSwitchPortTrunkType_Type.__name__ = "Integer32"
_HpSwitchPortTrunkType_Object = MibTableColumn
hpSwitchPortTrunkType = _HpSwitchPortTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 13),
    _HpSwitchPortTrunkType_Type()
)
hpSwitchPortTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortTrunkType.setStatus("mandatory")


class _HpSwitchPortTrunkLACPStatus_Type(Integer32):
    """Custom type hpSwitchPortTrunkLACPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 1),
          ("passive", 3))
    )


_HpSwitchPortTrunkLACPStatus_Type.__name__ = "Integer32"
_HpSwitchPortTrunkLACPStatus_Object = MibTableColumn
hpSwitchPortTrunkLACPStatus = _HpSwitchPortTrunkLACPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 14),
    _HpSwitchPortTrunkLACPStatus_Type()
)
hpSwitchPortTrunkLACPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortTrunkLACPStatus.setStatus("mandatory")


class _HpSwitchPortMDIXStatus_Type(Integer32):
    """Custom type hpSwitchPortMDIXStatus based on Integer32"""
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
        *(("automdix", 4),
          ("mdi", 2),
          ("mdix", 3),
          ("not-applicable", 1))
    )


_HpSwitchPortMDIXStatus_Type.__name__ = "Integer32"
_HpSwitchPortMDIXStatus_Object = MibTableColumn
hpSwitchPortMDIXStatus = _HpSwitchPortMDIXStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 15),
    _HpSwitchPortMDIXStatus_Type()
)
hpSwitchPortMDIXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortMDIXStatus.setStatus("mandatory")


class _HpSwitchPortAutoMDIX_Type(Integer32):
    """Custom type hpSwitchPortAutoMDIX based on Integer32"""
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
        *(("automdix", 4),
          ("mdi", 2),
          ("mdix", 3),
          ("not-applicable", 1))
    )


_HpSwitchPortAutoMDIX_Type.__name__ = "Integer32"
_HpSwitchPortAutoMDIX_Object = MibTableColumn
hpSwitchPortAutoMDIX = _HpSwitchPortAutoMDIX_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 16),
    _HpSwitchPortAutoMDIX_Type()
)
hpSwitchPortAutoMDIX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortAutoMDIX.setStatus("mandatory")


class _HpSwitchPortLACPKey_Type(Integer32):
    """Custom type hpSwitchPortLACPKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchPortLACPKey_Type.__name__ = "Integer32"
_HpSwitchPortLACPKey_Object = MibTableColumn
hpSwitchPortLACPKey = _HpSwitchPortLACPKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 17),
    _HpSwitchPortLACPKey_Type()
)
hpSwitchPortLACPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortLACPKey.setStatus("mandatory")


class _HpSwitchPortTrafficTemplateName_Type(OctetString):
    """Custom type hpSwitchPortTrafficTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchPortTrafficTemplateName_Type.__name__ = "OctetString"
_HpSwitchPortTrafficTemplateName_Object = MibTableColumn
hpSwitchPortTrafficTemplateName = _HpSwitchPortTrafficTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 18),
    _HpSwitchPortTrafficTemplateName_Type()
)
hpSwitchPortTrafficTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortTrafficTemplateName.setStatus("mandatory")


class _HpSwitchPortEEEAdminStatus_Type(Integer32):
    """Custom type hpSwitchPortEEEAdminStatus based on Integer32"""
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


_HpSwitchPortEEEAdminStatus_Type.__name__ = "Integer32"
_HpSwitchPortEEEAdminStatus_Object = MibTableColumn
hpSwitchPortEEEAdminStatus = _HpSwitchPortEEEAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 19),
    _HpSwitchPortEEEAdminStatus_Type()
)
hpSwitchPortEEEAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortEEEAdminStatus.setStatus("mandatory")


class _HpSwitchPortEEEOperStatus_Type(Integer32):
    """Custom type hpSwitchPortEEEOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("notSupported", 1))
    )


_HpSwitchPortEEEOperStatus_Type.__name__ = "Integer32"
_HpSwitchPortEEEOperStatus_Object = MibTableColumn
hpSwitchPortEEEOperStatus = _HpSwitchPortEEEOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 20),
    _HpSwitchPortEEEOperStatus_Type()
)
hpSwitchPortEEEOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortEEEOperStatus.setStatus("mandatory")


class _HpSwitchPortEEECurrentTwSysTx_Type(Integer32):
    """Custom type hpSwitchPortEEECurrentTwSysTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchPortEEECurrentTwSysTx_Type.__name__ = "Integer32"
_HpSwitchPortEEECurrentTwSysTx_Object = MibTableColumn
hpSwitchPortEEECurrentTwSysTx = _HpSwitchPortEEECurrentTwSysTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 21),
    _HpSwitchPortEEECurrentTwSysTx_Type()
)
hpSwitchPortEEECurrentTwSysTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortEEECurrentTwSysTx.setStatus("deprecated")
if mibBuilder.loadTexts:
    hpSwitchPortEEECurrentTwSysTx.setUnits("microseconds")


class _HpSwitchPortEEEMinTwSysTx_Type(Integer32):
    """Custom type hpSwitchPortEEEMinTwSysTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchPortEEEMinTwSysTx_Type.__name__ = "Integer32"
_HpSwitchPortEEEMinTwSysTx_Object = MibTableColumn
hpSwitchPortEEEMinTwSysTx = _HpSwitchPortEEEMinTwSysTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 22),
    _HpSwitchPortEEEMinTwSysTx_Type()
)
hpSwitchPortEEEMinTwSysTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMinTwSysTx.setStatus("deprecated")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMinTwSysTx.setUnits("microseconds")


class _HpSwitchPortEEEMaxTwSysTx_Type(Integer32):
    """Custom type hpSwitchPortEEEMaxTwSysTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchPortEEEMaxTwSysTx_Type.__name__ = "Integer32"
_HpSwitchPortEEEMaxTwSysTx_Object = MibTableColumn
hpSwitchPortEEEMaxTwSysTx = _HpSwitchPortEEEMaxTwSysTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 23),
    _HpSwitchPortEEEMaxTwSysTx_Type()
)
hpSwitchPortEEEMaxTwSysTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMaxTwSysTx.setStatus("deprecated")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMaxTwSysTx.setUnits("microseconds")


class _HpSwitchPortPvid_Type(Integer32):
    """Custom type hpSwitchPortPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HpSwitchPortPvid_Type.__name__ = "Integer32"
_HpSwitchPortPvid_Object = MibTableColumn
hpSwitchPortPvid = _HpSwitchPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 25),
    _HpSwitchPortPvid_Type()
)
hpSwitchPortPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortPvid.setStatus("mandatory")


class _HpSwitchPortTaggedVlanMap1k_Type(OctetString):
    """Custom type hpSwitchPortTaggedVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpSwitchPortTaggedVlanMap1k_Type.__name__ = "OctetString"
_HpSwitchPortTaggedVlanMap1k_Object = MibTableColumn
hpSwitchPortTaggedVlanMap1k = _HpSwitchPortTaggedVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 26),
    _HpSwitchPortTaggedVlanMap1k_Type()
)
hpSwitchPortTaggedVlanMap1k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortTaggedVlanMap1k.setStatus("mandatory")


class _HpSwitchPortTaggedVlanMap2k_Type(OctetString):
    """Custom type hpSwitchPortTaggedVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpSwitchPortTaggedVlanMap2k_Type.__name__ = "OctetString"
_HpSwitchPortTaggedVlanMap2k_Object = MibTableColumn
hpSwitchPortTaggedVlanMap2k = _HpSwitchPortTaggedVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 27),
    _HpSwitchPortTaggedVlanMap2k_Type()
)
hpSwitchPortTaggedVlanMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortTaggedVlanMap2k.setStatus("mandatory")


class _HpSwitchPortTaggedVlanMap3k_Type(OctetString):
    """Custom type hpSwitchPortTaggedVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpSwitchPortTaggedVlanMap3k_Type.__name__ = "OctetString"
_HpSwitchPortTaggedVlanMap3k_Object = MibTableColumn
hpSwitchPortTaggedVlanMap3k = _HpSwitchPortTaggedVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 28),
    _HpSwitchPortTaggedVlanMap3k_Type()
)
hpSwitchPortTaggedVlanMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortTaggedVlanMap3k.setStatus("mandatory")


class _HpSwitchPortTaggedVlanMap4k_Type(OctetString):
    """Custom type hpSwitchPortTaggedVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpSwitchPortTaggedVlanMap4k_Type.__name__ = "OctetString"
_HpSwitchPortTaggedVlanMap4k_Object = MibTableColumn
hpSwitchPortTaggedVlanMap4k = _HpSwitchPortTaggedVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 29),
    _HpSwitchPortTaggedVlanMap4k_Type()
)
hpSwitchPortTaggedVlanMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortTaggedVlanMap4k.setStatus("mandatory")


class _HpSwitchPortEEECurrentTwSysTx1_Type(Integer32):
    """Custom type hpSwitchPortEEECurrentTwSysTx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchPortEEECurrentTwSysTx1_Type.__name__ = "Integer32"
_HpSwitchPortEEECurrentTwSysTx1_Object = MibTableColumn
hpSwitchPortEEECurrentTwSysTx1 = _HpSwitchPortEEECurrentTwSysTx1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 30),
    _HpSwitchPortEEECurrentTwSysTx1_Type()
)
hpSwitchPortEEECurrentTwSysTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortEEECurrentTwSysTx1.setStatus("mandatory")
if mibBuilder.loadTexts:
    hpSwitchPortEEECurrentTwSysTx1.setUnits("microseconds")


class _HpSwitchPortEEEMinTwSysTx1_Type(Integer32):
    """Custom type hpSwitchPortEEEMinTwSysTx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchPortEEEMinTwSysTx1_Type.__name__ = "Integer32"
_HpSwitchPortEEEMinTwSysTx1_Object = MibTableColumn
hpSwitchPortEEEMinTwSysTx1 = _HpSwitchPortEEEMinTwSysTx1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 31),
    _HpSwitchPortEEEMinTwSysTx1_Type()
)
hpSwitchPortEEEMinTwSysTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMinTwSysTx1.setStatus("mandatory")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMinTwSysTx1.setUnits("microseconds")


class _HpSwitchPortEEEMaxTwSysTx1_Type(Integer32):
    """Custom type hpSwitchPortEEEMaxTwSysTx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchPortEEEMaxTwSysTx1_Type.__name__ = "Integer32"
_HpSwitchPortEEEMaxTwSysTx1_Object = MibTableColumn
hpSwitchPortEEEMaxTwSysTx1 = _HpSwitchPortEEEMaxTwSysTx1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 32),
    _HpSwitchPortEEEMaxTwSysTx1_Type()
)
hpSwitchPortEEEMaxTwSysTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMaxTwSysTx1.setStatus("mandatory")
if mibBuilder.loadTexts:
    hpSwitchPortEEEMaxTwSysTx1.setUnits("microseconds")


class _HpSwitchPortPtpAdminStatus_Type(Integer32):
    """Custom type hpSwitchPortPtpAdminStatus based on Integer32"""
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


_HpSwitchPortPtpAdminStatus_Type.__name__ = "Integer32"
_HpSwitchPortPtpAdminStatus_Object = MibTableColumn
hpSwitchPortPtpAdminStatus = _HpSwitchPortPtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 35),
    _HpSwitchPortPtpAdminStatus_Type()
)
hpSwitchPortPtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortPtpAdminStatus.setStatus("mandatory")


class _HpSwitchPortPtpOperStatus_Type(Integer32):
    """Custom type hpSwitchPortPtpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("notSupported", 1))
    )


_HpSwitchPortPtpOperStatus_Type.__name__ = "Integer32"
_HpSwitchPortPtpOperStatus_Object = MibTableColumn
hpSwitchPortPtpOperStatus = _HpSwitchPortPtpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 36),
    _HpSwitchPortPtpOperStatus_Type()
)
hpSwitchPortPtpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortPtpOperStatus.setStatus("mandatory")
_HpSwitchPortPtpRxCount_Type = Counter32
_HpSwitchPortPtpRxCount_Object = MibTableColumn
hpSwitchPortPtpRxCount = _HpSwitchPortPtpRxCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 37),
    _HpSwitchPortPtpRxCount_Type()
)
hpSwitchPortPtpRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortPtpRxCount.setStatus("mandatory")
_HpSwitchPortPtpTxCount_Type = Counter32
_HpSwitchPortPtpTxCount_Object = MibTableColumn
hpSwitchPortPtpTxCount = _HpSwitchPortPtpTxCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 38),
    _HpSwitchPortPtpTxCount_Type()
)
hpSwitchPortPtpTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortPtpTxCount.setStatus("mandatory")


class _HpSwitchPortNetworkDevice_Type(Integer32):
    """Custom type hpSwitchPortNetworkDevice based on Integer32"""
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


_HpSwitchPortNetworkDevice_Type.__name__ = "Integer32"
_HpSwitchPortNetworkDevice_Object = MibTableColumn
hpSwitchPortNetworkDevice = _HpSwitchPortNetworkDevice_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 1, 1, 39),
    _HpSwitchPortNetworkDevice_Type()
)
hpSwitchPortNetworkDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortNetworkDevice.setStatus("mandatory")
_HpSwitchPortConfigStatus_Type = ConfigStatus
_HpSwitchPortConfigStatus_Object = MibScalar
hpSwitchPortConfigStatus = _HpSwitchPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 2),
    _HpSwitchPortConfigStatus_Type()
)
hpSwitchPortConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchPortConfigStatus.setStatus("mandatory")


class _HpSwitchLinkUpDownTrapAllPortsStatus_Type(Integer32):
    """Custom type hpSwitchLinkUpDownTrapAllPortsStatus based on Integer32"""
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


_HpSwitchLinkUpDownTrapAllPortsStatus_Type.__name__ = "Integer32"
_HpSwitchLinkUpDownTrapAllPortsStatus_Object = MibScalar
hpSwitchLinkUpDownTrapAllPortsStatus = _HpSwitchLinkUpDownTrapAllPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 3, 3),
    _HpSwitchLinkUpDownTrapAllPortsStatus_Type()
)
hpSwitchLinkUpDownTrapAllPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchLinkUpDownTrapAllPortsStatus.setStatus("mandatory")
_HpSwitchIpxConfig_ObjectIdentity = ObjectIdentity
hpSwitchIpxConfig = _HpSwitchIpxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 4)
)
_HpSwitchIpxConfigStatus_Type = ConfigStatus
_HpSwitchIpxConfigStatus_Object = MibScalar
hpSwitchIpxConfigStatus = _HpSwitchIpxConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 4, 2),
    _HpSwitchIpxConfigStatus_Type()
)
hpSwitchIpxConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpxConfigStatus.setStatus("mandatory")
_HpSwitchIpConfig_ObjectIdentity = ObjectIdentity
hpSwitchIpConfig = _HpSwitchIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5)
)


class _HpSwitchIpTimepAdminStatus_Type(Integer32):
    """Custom type hpSwitchIpTimepAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 3),
          ("disable", 2),
          ("manual", 1))
    )


_HpSwitchIpTimepAdminStatus_Type.__name__ = "Integer32"
_HpSwitchIpTimepAdminStatus_Object = MibScalar
hpSwitchIpTimepAdminStatus = _HpSwitchIpTimepAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 1),
    _HpSwitchIpTimepAdminStatus_Type()
)
hpSwitchIpTimepAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpTimepAdminStatus.setStatus("mandatory")
_HpSwitchIpTimepServerAddr_Type = IpAddress
_HpSwitchIpTimepServerAddr_Object = MibScalar
hpSwitchIpTimepServerAddr = _HpSwitchIpTimepServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 2),
    _HpSwitchIpTimepServerAddr_Type()
)
hpSwitchIpTimepServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpTimepServerAddr.setStatus("deprecated")


class _HpSwitchIpTimepPollInterval_Type(Integer32):
    """Custom type hpSwitchIpTimepPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIpTimepPollInterval_Type.__name__ = "Integer32"
_HpSwitchIpTimepPollInterval_Object = MibScalar
hpSwitchIpTimepPollInterval = _HpSwitchIpTimepPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 3),
    _HpSwitchIpTimepPollInterval_Type()
)
hpSwitchIpTimepPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpTimepPollInterval.setStatus("mandatory")
_HpSwitchIpConfigStatus_Type = ConfigStatus
_HpSwitchIpConfigStatus_Object = MibScalar
hpSwitchIpConfigStatus = _HpSwitchIpConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 5),
    _HpSwitchIpConfigStatus_Type()
)
hpSwitchIpConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIpConfigStatus.setStatus("obsolete")


class _HpSwitchIpTftpMode_Type(Integer32):
    """Custom type hpSwitchIpTftpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secure", 1),
          ("unsecure", 2))
    )


_HpSwitchIpTftpMode_Type.__name__ = "Integer32"
_HpSwitchIpTftpMode_Object = MibScalar
hpSwitchIpTftpMode = _HpSwitchIpTftpMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 6),
    _HpSwitchIpTftpMode_Type()
)
hpSwitchIpTftpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpTftpMode.setStatus("obsolete")
_HpSwitchIpTimepInetServerAddrType_Type = InetAddressType
_HpSwitchIpTimepInetServerAddrType_Object = MibScalar
hpSwitchIpTimepInetServerAddrType = _HpSwitchIpTimepInetServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 7),
    _HpSwitchIpTimepInetServerAddrType_Type()
)
hpSwitchIpTimepInetServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpTimepInetServerAddrType.setStatus("mandatory")
_HpSwitchIpTimepInetServerAddr_Type = InetAddress
_HpSwitchIpTimepInetServerAddr_Object = MibScalar
hpSwitchIpTimepInetServerAddr = _HpSwitchIpTimepInetServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 8),
    _HpSwitchIpTimepInetServerAddr_Type()
)
hpSwitchIpTimepInetServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpTimepInetServerAddr.setStatus("mandatory")


class _HpSwitchIpTimepIsOobm_Type(TruthValue):
    """Custom type hpSwitchIpTimepIsOobm based on TruthValue"""


_HpSwitchIpTimepIsOobm_Object = MibScalar
hpSwitchIpTimepIsOobm = _HpSwitchIpTimepIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 5, 9),
    _HpSwitchIpTimepIsOobm_Type()
)
hpSwitchIpTimepIsOobm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIpTimepIsOobm.setStatus("mandatory")
_HpSwitchSerialLinkConfig_ObjectIdentity = ObjectIdentity
hpSwitchSerialLinkConfig = _HpSwitchSerialLinkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6)
)


class _HpSwitchSLinkBaudRate_Type(Integer32):
    """Custom type hpSwitchSLinkBaudRate based on Integer32"""
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
        *(("baudRate115200", 11),
          ("baudRate1200", 4),
          ("baudRate19200", 8),
          ("baudRate2400", 5),
          ("baudRate300", 2),
          ("baudRate38400", 9),
          ("baudRate4800", 6),
          ("baudRate57600", 10),
          ("baudRate600", 3),
          ("baudRate9600", 7),
          ("speedSense", 1))
    )


_HpSwitchSLinkBaudRate_Type.__name__ = "Integer32"
_HpSwitchSLinkBaudRate_Object = MibScalar
hpSwitchSLinkBaudRate = _HpSwitchSLinkBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 1),
    _HpSwitchSLinkBaudRate_Type()
)
hpSwitchSLinkBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSLinkBaudRate.setStatus("mandatory")


class _HpSwitchSLinkFlowCtrl_Type(Integer32):
    """Custom type hpSwitchSLinkFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("robustXonXoff", 3),
          ("xonXoff", 2))
    )


_HpSwitchSLinkFlowCtrl_Type.__name__ = "Integer32"
_HpSwitchSLinkFlowCtrl_Object = MibScalar
hpSwitchSLinkFlowCtrl = _HpSwitchSLinkFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 2),
    _HpSwitchSLinkFlowCtrl_Type()
)
hpSwitchSLinkFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSLinkFlowCtrl.setStatus("mandatory")


class _HpSwitchSLinkConnInactTime_Type(Integer32):
    """Custom type hpSwitchSLinkConnInactTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HpSwitchSLinkConnInactTime_Type.__name__ = "Integer32"
_HpSwitchSLinkConnInactTime_Object = MibScalar
hpSwitchSLinkConnInactTime = _HpSwitchSLinkConnInactTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 3),
    _HpSwitchSLinkConnInactTime_Type()
)
hpSwitchSLinkConnInactTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSLinkConnInactTime.setStatus("deprecated")


class _HpSwitchSLinkModemConnTime_Type(Integer32):
    """Custom type hpSwitchSLinkModemConnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HpSwitchSLinkModemConnTime_Type.__name__ = "Integer32"
_HpSwitchSLinkModemConnTime_Object = MibScalar
hpSwitchSLinkModemConnTime = _HpSwitchSLinkModemConnTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 4),
    _HpSwitchSLinkModemConnTime_Type()
)
hpSwitchSLinkModemConnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSLinkModemConnTime.setStatus("mandatory")


class _HpSwitchSLinkModemLostRecvTime_Type(Integer32):
    """Custom type hpSwitchSLinkModemLostRecvTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_HpSwitchSLinkModemLostRecvTime_Type.__name__ = "Integer32"
_HpSwitchSLinkModemLostRecvTime_Object = MibScalar
hpSwitchSLinkModemLostRecvTime = _HpSwitchSLinkModemLostRecvTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 5),
    _HpSwitchSLinkModemLostRecvTime_Type()
)
hpSwitchSLinkModemLostRecvTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSLinkModemLostRecvTime.setStatus("mandatory")


class _HpSwitchSLinkModemDisConnTime_Type(Integer32):
    """Custom type hpSwitchSLinkModemDisConnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HpSwitchSLinkModemDisConnTime_Type.__name__ = "Integer32"
_HpSwitchSLinkModemDisConnTime_Object = MibScalar
hpSwitchSLinkModemDisConnTime = _HpSwitchSLinkModemDisConnTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 6),
    _HpSwitchSLinkModemDisConnTime_Type()
)
hpSwitchSLinkModemDisConnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSLinkModemDisConnTime.setStatus("mandatory")


class _HpSwitchSLinkParity_Type(Integer32):
    """Custom type hpSwitchSLinkParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("parityEven", 3),
          ("parityNone", 1),
          ("parityOdd", 2))
    )


_HpSwitchSLinkParity_Type.__name__ = "Integer32"
_HpSwitchSLinkParity_Object = MibScalar
hpSwitchSLinkParity = _HpSwitchSLinkParity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 7),
    _HpSwitchSLinkParity_Type()
)
hpSwitchSLinkParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchSLinkParity.setStatus("mandatory")


class _HpSwitchSLinkCharBits_Type(Integer32):
    """Custom type hpSwitchSLinkCharBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("char7Bits", 2),
          ("char8Bits", 1))
    )


_HpSwitchSLinkCharBits_Type.__name__ = "Integer32"
_HpSwitchSLinkCharBits_Object = MibScalar
hpSwitchSLinkCharBits = _HpSwitchSLinkCharBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 8),
    _HpSwitchSLinkCharBits_Type()
)
hpSwitchSLinkCharBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchSLinkCharBits.setStatus("mandatory")


class _HpSwitchSLinkStopBits_Type(Integer32):
    """Custom type hpSwitchSLinkStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stop1Bits", 1),
          ("stop1andHalfBits", 2),
          ("stop2Bits", 3))
    )


_HpSwitchSLinkStopBits_Type.__name__ = "Integer32"
_HpSwitchSLinkStopBits_Object = MibScalar
hpSwitchSLinkStopBits = _HpSwitchSLinkStopBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 9),
    _HpSwitchSLinkStopBits_Type()
)
hpSwitchSLinkStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchSLinkStopBits.setStatus("mandatory")
_HpSwitchSLinkConfigStatus_Type = ConfigStatus
_HpSwitchSLinkConfigStatus_Object = MibScalar
hpSwitchSLinkConfigStatus = _HpSwitchSLinkConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 6, 10),
    _HpSwitchSLinkConfigStatus_Type()
)
hpSwitchSLinkConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchSLinkConfigStatus.setStatus("mandatory")
_HpSwitchFilterConfig_ObjectIdentity = ObjectIdentity
hpSwitchFilterConfig = _HpSwitchFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8)
)
_HpSwitchFilterConfigTable_Object = MibTable
hpSwitchFilterConfigTable = _HpSwitchFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFilterConfigTable.setStatus("mandatory")
_HpSwitchFilterConfigEntry_Object = MibTableRow
hpSwitchFilterConfigEntry = _HpSwitchFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1)
)
hpSwitchFilterConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchFilterIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchFilterConfigEntry.setStatus("mandatory")


class _HpSwitchFilterIndex_Type(Integer32):
    """Custom type hpSwitchFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchFilterIndex_Type.__name__ = "Integer32"
_HpSwitchFilterIndex_Object = MibTableColumn
hpSwitchFilterIndex = _HpSwitchFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 1),
    _HpSwitchFilterIndex_Type()
)
hpSwitchFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFilterIndex.setStatus("mandatory")


class _HpSwitchFilterType_Type(Integer32):
    """Custom type hpSwitchFilterType based on Integer32"""
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
        *(("level-3", 2),
          ("multicast", 1),
          ("port", 3),
          ("unicast", 4))
    )


_HpSwitchFilterType_Type.__name__ = "Integer32"
_HpSwitchFilterType_Object = MibTableColumn
hpSwitchFilterType = _HpSwitchFilterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 2),
    _HpSwitchFilterType_Type()
)
hpSwitchFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFilterType.setStatus("mandatory")


class _HpSwitchFilterSrcPort_Type(Integer32):
    """Custom type hpSwitchFilterSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchFilterSrcPort_Type.__name__ = "Integer32"
_HpSwitchFilterSrcPort_Object = MibTableColumn
hpSwitchFilterSrcPort = _HpSwitchFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 3),
    _HpSwitchFilterSrcPort_Type()
)
hpSwitchFilterSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFilterSrcPort.setStatus("mandatory")
_HpSwitchFilterMacAddr_Type = MacAddress
_HpSwitchFilterMacAddr_Object = MibTableColumn
hpSwitchFilterMacAddr = _HpSwitchFilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 4),
    _HpSwitchFilterMacAddr_Type()
)
hpSwitchFilterMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFilterMacAddr.setStatus("mandatory")


class _HpSwitchFilterProtocolType_Type(Integer32):
    """Custom type hpSwitchFilterProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchFilterProtocolType_Type.__name__ = "Integer32"
_HpSwitchFilterProtocolType_Object = MibTableColumn
hpSwitchFilterProtocolType = _HpSwitchFilterProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 5),
    _HpSwitchFilterProtocolType_Type()
)
hpSwitchFilterProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFilterProtocolType.setStatus("mandatory")
_HpSwitchFilterPortMask_Type = OctetString
_HpSwitchFilterPortMask_Object = MibTableColumn
hpSwitchFilterPortMask = _HpSwitchFilterPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 6),
    _HpSwitchFilterPortMask_Type()
)
hpSwitchFilterPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFilterPortMask.setStatus("mandatory")
_HpSwitchFilterEntryStatus_Type = RowStatus
_HpSwitchFilterEntryStatus_Object = MibTableColumn
hpSwitchFilterEntryStatus = _HpSwitchFilterEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 7),
    _HpSwitchFilterEntryStatus_Type()
)
hpSwitchFilterEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFilterEntryStatus.setStatus("mandatory")
_HpSwitchFilterName_Type = DisplayString
_HpSwitchFilterName_Object = MibTableColumn
hpSwitchFilterName = _HpSwitchFilterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 1, 1, 8),
    _HpSwitchFilterName_Type()
)
hpSwitchFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFilterName.setStatus("mandatory")
_HpSwitchProbeConfig_ObjectIdentity = ObjectIdentity
hpSwitchProbeConfig = _HpSwitchProbeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 9)
)


class _HpSwitchProbeType_Type(Integer32):
    """Custom type hpSwitchProbeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ports", 1),
          ("vlan", 2))
    )


_HpSwitchProbeType_Type.__name__ = "Integer32"
_HpSwitchProbeType_Object = MibScalar
hpSwitchProbeType = _HpSwitchProbeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 9, 1),
    _HpSwitchProbeType_Type()
)
hpSwitchProbeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchProbeType.setStatus("obsolete")
_HpSwitchProbedVlanId_Type = VlanID
_HpSwitchProbedVlanId_Object = MibScalar
hpSwitchProbedVlanId = _HpSwitchProbedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 9, 2),
    _HpSwitchProbedVlanId_Type()
)
hpSwitchProbedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchProbedVlanId.setStatus("obsolete")


class _HpSwitchProbePort_Type(Integer32):
    """Custom type hpSwitchProbePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchProbePort_Type.__name__ = "Integer32"
_HpSwitchProbePort_Object = MibScalar
hpSwitchProbePort = _HpSwitchProbePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 9, 3),
    _HpSwitchProbePort_Type()
)
hpSwitchProbePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchProbePort.setStatus("obsolete")


class _HpSwitchProbeAdminStatus_Type(Integer32):
    """Custom type hpSwitchProbeAdminStatus based on Integer32"""
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


_HpSwitchProbeAdminStatus_Type.__name__ = "Integer32"
_HpSwitchProbeAdminStatus_Object = MibScalar
hpSwitchProbeAdminStatus = _HpSwitchProbeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 9, 4),
    _HpSwitchProbeAdminStatus_Type()
)
hpSwitchProbeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchProbeAdminStatus.setStatus("obsolete")
_HpSwitchProbedPortMask_Type = OctetString
_HpSwitchProbedPortMask_Object = MibScalar
hpSwitchProbedPortMask = _HpSwitchProbedPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 9, 5),
    _HpSwitchProbedPortMask_Type()
)
hpSwitchProbedPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchProbedPortMask.setStatus("obsolete")
_HpSwitchFddiIpFragConfig_ObjectIdentity = ObjectIdentity
hpSwitchFddiIpFragConfig = _HpSwitchFddiIpFragConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 11)
)
_HpSwitchFddiIpFragConfigTable_Object = MibTable
hpSwitchFddiIpFragConfigTable = _HpSwitchFddiIpFragConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragConfigTable.setStatus("mandatory")
_HpSwitchFddiIpFragConfigEntry_Object = MibTableRow
hpSwitchFddiIpFragConfigEntry = _HpSwitchFddiIpFragConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 11, 1, 1)
)
hpSwitchFddiIpFragConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchFddiIpFragConfigIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragConfigEntry.setStatus("mandatory")


class _HpSwitchFddiIpFragConfigIndex_Type(Integer32):
    """Custom type hpSwitchFddiIpFragConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchFddiIpFragConfigIndex_Type.__name__ = "Integer32"
_HpSwitchFddiIpFragConfigIndex_Object = MibTableColumn
hpSwitchFddiIpFragConfigIndex = _HpSwitchFddiIpFragConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 11, 1, 1, 1),
    _HpSwitchFddiIpFragConfigIndex_Type()
)
hpSwitchFddiIpFragConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragConfigIndex.setStatus("mandatory")


class _HpSwitchFddiIpFragConfigStatus_Type(Integer32):
    """Custom type hpSwitchFddiIpFragConfigStatus based on Integer32"""
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


_HpSwitchFddiIpFragConfigStatus_Type.__name__ = "Integer32"
_HpSwitchFddiIpFragConfigStatus_Object = MibTableColumn
hpSwitchFddiIpFragConfigStatus = _HpSwitchFddiIpFragConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 11, 1, 1, 2),
    _HpSwitchFddiIpFragConfigStatus_Type()
)
hpSwitchFddiIpFragConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFddiIpFragConfigStatus.setStatus("mandatory")
_HpSwitchABCConfig_ObjectIdentity = ObjectIdentity
hpSwitchABCConfig = _HpSwitchABCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12)
)
_HpSwitchABCConfigTable_Object = MibTable
hpSwitchABCConfigTable = _HpSwitchABCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    hpSwitchABCConfigTable.setStatus("mandatory")
_HpSwitchABCConfigEntry_Object = MibTableRow
hpSwitchABCConfigEntry = _HpSwitchABCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1, 1)
)
hpSwitchABCConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchABCConfigVlan"),
)
if mibBuilder.loadTexts:
    hpSwitchABCConfigEntry.setStatus("mandatory")
_HpSwitchABCConfigVlan_Type = VlanID
_HpSwitchABCConfigVlan_Object = MibTableColumn
hpSwitchABCConfigVlan = _HpSwitchABCConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1, 1, 1),
    _HpSwitchABCConfigVlan_Type()
)
hpSwitchABCConfigVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchABCConfigVlan.setStatus("mandatory")


class _HpSwitchABCConfigControl_Type(Integer32):
    """Custom type hpSwitchABCConfigControl based on Integer32"""
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
        *(("disable", 4),
          ("ip", 2),
          ("ipipx", 1),
          ("ipx", 3))
    )


_HpSwitchABCConfigControl_Type.__name__ = "Integer32"
_HpSwitchABCConfigControl_Object = MibTableColumn
hpSwitchABCConfigControl = _HpSwitchABCConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1, 1, 2),
    _HpSwitchABCConfigControl_Type()
)
hpSwitchABCConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchABCConfigControl.setStatus("mandatory")


class _HpSwitchABCConfigIpRipControl_Type(Integer32):
    """Custom type hpSwitchABCConfigIpRipControl based on Integer32"""
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


_HpSwitchABCConfigIpRipControl_Type.__name__ = "Integer32"
_HpSwitchABCConfigIpRipControl_Object = MibTableColumn
hpSwitchABCConfigIpRipControl = _HpSwitchABCConfigIpRipControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1, 1, 3),
    _HpSwitchABCConfigIpRipControl_Type()
)
hpSwitchABCConfigIpRipControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchABCConfigIpRipControl.setStatus("mandatory")


class _HpSwitchABCConfigIpxRipSapControl_Type(Integer32):
    """Custom type hpSwitchABCConfigIpxRipSapControl based on Integer32"""
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


_HpSwitchABCConfigIpxRipSapControl_Type.__name__ = "Integer32"
_HpSwitchABCConfigIpxRipSapControl_Object = MibTableColumn
hpSwitchABCConfigIpxRipSapControl = _HpSwitchABCConfigIpxRipSapControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1, 1, 4),
    _HpSwitchABCConfigIpxRipSapControl_Type()
)
hpSwitchABCConfigIpxRipSapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchABCConfigIpxRipSapControl.setStatus("mandatory")


class _HpSwitchABCConfigVlanBcastLimit_Type(Integer32):
    """Custom type hpSwitchABCConfigVlanBcastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_HpSwitchABCConfigVlanBcastLimit_Type.__name__ = "Integer32"
_HpSwitchABCConfigVlanBcastLimit_Object = MibTableColumn
hpSwitchABCConfigVlanBcastLimit = _HpSwitchABCConfigVlanBcastLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1, 1, 5),
    _HpSwitchABCConfigVlanBcastLimit_Type()
)
hpSwitchABCConfigVlanBcastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchABCConfigVlanBcastLimit.setStatus("mandatory")


class _HpSwitchABCConfigAutoGatewayConfig_Type(Integer32):
    """Custom type hpSwitchABCConfigAutoGatewayConfig based on Integer32"""
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


_HpSwitchABCConfigAutoGatewayConfig_Type.__name__ = "Integer32"
_HpSwitchABCConfigAutoGatewayConfig_Object = MibTableColumn
hpSwitchABCConfigAutoGatewayConfig = _HpSwitchABCConfigAutoGatewayConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 12, 1, 1, 7),
    _HpSwitchABCConfigAutoGatewayConfig_Type()
)
hpSwitchABCConfigAutoGatewayConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchABCConfigAutoGatewayConfig.setStatus("mandatory")
_HpSwitchStpConfig_ObjectIdentity = ObjectIdentity
hpSwitchStpConfig = _HpSwitchStpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14)
)
_HpSwitchStpVlanTable_Object = MibTable
hpSwitchStpVlanTable = _HpSwitchStpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1)
)
if mibBuilder.loadTexts:
    hpSwitchStpVlanTable.setStatus("mandatory")
_HpSwitchStpVlanEntry_Object = MibTableRow
hpSwitchStpVlanEntry = _HpSwitchStpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1, 1)
)
hpSwitchStpVlanEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchStpVlan"),
)
if mibBuilder.loadTexts:
    hpSwitchStpVlanEntry.setStatus("mandatory")
_HpSwitchStpVlan_Type = VlanID
_HpSwitchStpVlan_Object = MibTableColumn
hpSwitchStpVlan = _HpSwitchStpVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1, 1, 1),
    _HpSwitchStpVlan_Type()
)
hpSwitchStpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchStpVlan.setStatus("mandatory")


class _HpSwitchStpAdminStatus_Type(Integer32):
    """Custom type hpSwitchStpAdminStatus based on Integer32"""
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


_HpSwitchStpAdminStatus_Type.__name__ = "Integer32"
_HpSwitchStpAdminStatus_Object = MibTableColumn
hpSwitchStpAdminStatus = _HpSwitchStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1, 1, 2),
    _HpSwitchStpAdminStatus_Type()
)
hpSwitchStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpAdminStatus.setStatus("mandatory")


class _HpSwitchStpPriority_Type(Integer32):
    """Custom type hpSwitchStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchStpPriority_Type.__name__ = "Integer32"
_HpSwitchStpPriority_Object = MibTableColumn
hpSwitchStpPriority = _HpSwitchStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1, 1, 3),
    _HpSwitchStpPriority_Type()
)
hpSwitchStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPriority.setStatus("mandatory")
_HpSwitchStpMaxAge_Type = Timeout
_HpSwitchStpMaxAge_Object = MibTableColumn
hpSwitchStpMaxAge = _HpSwitchStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1, 1, 4),
    _HpSwitchStpMaxAge_Type()
)
hpSwitchStpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpMaxAge.setStatus("mandatory")
_HpSwitchStpHelloTime_Type = Timeout
_HpSwitchStpHelloTime_Object = MibTableColumn
hpSwitchStpHelloTime = _HpSwitchStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1, 1, 5),
    _HpSwitchStpHelloTime_Type()
)
hpSwitchStpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpHelloTime.setStatus("mandatory")
_HpSwitchStpForwardDelay_Type = Timeout
_HpSwitchStpForwardDelay_Object = MibTableColumn
hpSwitchStpForwardDelay = _HpSwitchStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 1, 1, 6),
    _HpSwitchStpForwardDelay_Type()
)
hpSwitchStpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpForwardDelay.setStatus("mandatory")
_HpSwitchStpPortTable_Object = MibTable
hpSwitchStpPortTable = _HpSwitchStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2)
)
if mibBuilder.loadTexts:
    hpSwitchStpPortTable.setStatus("mandatory")
_HpSwitchStpPortEntry_Object = MibTableRow
hpSwitchStpPortEntry = _HpSwitchStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1)
)
hpSwitchStpPortEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchStpPort"),
)
if mibBuilder.loadTexts:
    hpSwitchStpPortEntry.setStatus("mandatory")


class _HpSwitchStpPort_Type(Integer32):
    """Custom type hpSwitchStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchStpPort_Type.__name__ = "Integer32"
_HpSwitchStpPort_Object = MibTableColumn
hpSwitchStpPort = _HpSwitchStpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 1),
    _HpSwitchStpPort_Type()
)
hpSwitchStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchStpPort.setStatus("mandatory")
_HpSwitchStpPortType_Type = HpSwitchPortType
_HpSwitchStpPortType_Object = MibTableColumn
hpSwitchStpPortType = _HpSwitchStpPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 2),
    _HpSwitchStpPortType_Type()
)
hpSwitchStpPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchStpPortType.setStatus("mandatory")
_HpSwitchStpPortSrcMac_Type = MacAddress
_HpSwitchStpPortSrcMac_Object = MibTableColumn
hpSwitchStpPortSrcMac = _HpSwitchStpPortSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 3),
    _HpSwitchStpPortSrcMac_Type()
)
hpSwitchStpPortSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchStpPortSrcMac.setStatus("mandatory")


class _HpSwitchStpPortPriority_Type(Integer32):
    """Custom type hpSwitchStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchStpPortPriority_Type.__name__ = "Integer32"
_HpSwitchStpPortPriority_Object = MibTableColumn
hpSwitchStpPortPriority = _HpSwitchStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 4),
    _HpSwitchStpPortPriority_Type()
)
hpSwitchStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPortPriority.setStatus("mandatory")


class _HpSwitchStpPortPathCost_Type(Integer32):
    """Custom type hpSwitchStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchStpPortPathCost_Type.__name__ = "Integer32"
_HpSwitchStpPortPathCost_Object = MibTableColumn
hpSwitchStpPortPathCost = _HpSwitchStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 5),
    _HpSwitchStpPortPathCost_Type()
)
hpSwitchStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPortPathCost.setStatus("mandatory")


class _HpSwitchStpPortMode_Type(Integer32):
    """Custom type hpSwitchStpPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("normal", 1),
          ("uplink", 3))
    )


_HpSwitchStpPortMode_Type.__name__ = "Integer32"
_HpSwitchStpPortMode_Object = MibTableColumn
hpSwitchStpPortMode = _HpSwitchStpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 6),
    _HpSwitchStpPortMode_Type()
)
hpSwitchStpPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPortMode.setStatus("mandatory")


class _HpSwitchStpPortBpduFilter_Type(Integer32):
    """Custom type hpSwitchStpPortBpduFilter based on Integer32"""
    defaultValue = 2

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


_HpSwitchStpPortBpduFilter_Type.__name__ = "Integer32"
_HpSwitchStpPortBpduFilter_Object = MibTableColumn
hpSwitchStpPortBpduFilter = _HpSwitchStpPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 7),
    _HpSwitchStpPortBpduFilter_Type()
)
hpSwitchStpPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPortBpduFilter.setStatus("optional")


class _HpSwitchStpPortBpduProtection_Type(Integer32):
    """Custom type hpSwitchStpPortBpduProtection based on Integer32"""
    defaultValue = 2

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


_HpSwitchStpPortBpduProtection_Type.__name__ = "Integer32"
_HpSwitchStpPortBpduProtection_Object = MibTableColumn
hpSwitchStpPortBpduProtection = _HpSwitchStpPortBpduProtection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 8),
    _HpSwitchStpPortBpduProtection_Type()
)
hpSwitchStpPortBpduProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPortBpduProtection.setStatus("optional")
_HpSwitchStpPortErrantBpduCounter_Type = Counter32
_HpSwitchStpPortErrantBpduCounter_Object = MibTableColumn
hpSwitchStpPortErrantBpduCounter = _HpSwitchStpPortErrantBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 9),
    _HpSwitchStpPortErrantBpduCounter_Type()
)
hpSwitchStpPortErrantBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchStpPortErrantBpduCounter.setStatus("optional")


class _HpSwitchStpPortPvstFilter_Type(TruthValue):
    """Custom type hpSwitchStpPortPvstFilter based on TruthValue"""


_HpSwitchStpPortPvstFilter_Object = MibTableColumn
hpSwitchStpPortPvstFilter = _HpSwitchStpPortPvstFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 10),
    _HpSwitchStpPortPvstFilter_Type()
)
hpSwitchStpPortPvstFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPortPvstFilter.setStatus("optional")


class _HpSwitchStpPortPvstProtection_Type(TruthValue):
    """Custom type hpSwitchStpPortPvstProtection based on TruthValue"""


_HpSwitchStpPortPvstProtection_Object = MibTableColumn
hpSwitchStpPortPvstProtection = _HpSwitchStpPortPvstProtection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 2, 1, 11),
    _HpSwitchStpPortPvstProtection_Type()
)
hpSwitchStpPortPvstProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpPortPvstProtection.setStatus("optional")


class _HpSwitchStpTrapCntl_Type(Bits):
    """Custom type hpSwitchStpTrapCntl based on Bits"""
    namedValues = NamedValues(
        *(("errantBpdu", 0),
          ("loopGuard", 3),
          ("newRoot", 1),
          ("rootGuard", 2))
    )

_HpSwitchStpTrapCntl_Type.__name__ = "Bits"
_HpSwitchStpTrapCntl_Object = MibScalar
hpSwitchStpTrapCntl = _HpSwitchStpTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 3),
    _HpSwitchStpTrapCntl_Type()
)
hpSwitchStpTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpTrapCntl.setStatus("optional")


class _HpSwitchStpBpduProtectionTimeout_Type(Integer32):
    """Custom type hpSwitchStpBpduProtectionTimeout based on Integer32"""
    defaultValue = 0


_HpSwitchStpBpduProtectionTimeout_Object = MibScalar
hpSwitchStpBpduProtectionTimeout = _HpSwitchStpBpduProtectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 4),
    _HpSwitchStpBpduProtectionTimeout_Type()
)
hpSwitchStpBpduProtectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStpBpduProtectionTimeout.setStatus("optional")


class _HpSwitchSTPAdminStatus_Type(Integer32):
    """Custom type hpSwitchSTPAdminStatus based on Integer32"""
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


_HpSwitchSTPAdminStatus_Type.__name__ = "Integer32"
_HpSwitchSTPAdminStatus_Object = MibScalar
hpSwitchSTPAdminStatus = _HpSwitchSTPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 5),
    _HpSwitchSTPAdminStatus_Type()
)
hpSwitchSTPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSTPAdminStatus.setStatus("mandatory")


class _HpicfSwitchSTPVersion_Type(Integer32):
    """Custom type hpicfSwitchSTPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rapidPvst", 4))
    )


_HpicfSwitchSTPVersion_Type.__name__ = "Integer32"
_HpicfSwitchSTPVersion_Object = MibScalar
hpicfSwitchSTPVersion = _HpicfSwitchSTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 14, 6),
    _HpicfSwitchSTPVersion_Type()
)
hpicfSwitchSTPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSwitchSTPVersion.setStatus("mandatory")
_HpSwitchIgmpConfig_ObjectIdentity = ObjectIdentity
hpSwitchIgmpConfig = _HpSwitchIgmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15)
)
_HpSwitchIgmpConfigTable_Object = MibTable
hpSwitchIgmpConfigTable = _HpSwitchIgmpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1)
)
if mibBuilder.loadTexts:
    hpSwitchIgmpConfigTable.setStatus("mandatory")
_HpSwitchIgmpConfigEntry_Object = MibTableRow
hpSwitchIgmpConfigEntry = _HpSwitchIgmpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1, 1)
)
hpSwitchIgmpConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchIgmpVlanIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchIgmpConfigEntry.setStatus("mandatory")
_HpSwitchIgmpVlanIndex_Type = VlanID
_HpSwitchIgmpVlanIndex_Object = MibTableColumn
hpSwitchIgmpVlanIndex = _HpSwitchIgmpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1, 1, 1),
    _HpSwitchIgmpVlanIndex_Type()
)
hpSwitchIgmpVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIgmpVlanIndex.setStatus("mandatory")


class _HpSwitchIgmpState_Type(Integer32):
    """Custom type hpSwitchIgmpState based on Integer32"""
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


_HpSwitchIgmpState_Type.__name__ = "Integer32"
_HpSwitchIgmpState_Object = MibTableColumn
hpSwitchIgmpState = _HpSwitchIgmpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1, 1, 2),
    _HpSwitchIgmpState_Type()
)
hpSwitchIgmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpState.setStatus("mandatory")


class _HpSwitchIgmpQuerierState_Type(Integer32):
    """Custom type hpSwitchIgmpQuerierState based on Integer32"""
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


_HpSwitchIgmpQuerierState_Type.__name__ = "Integer32"
_HpSwitchIgmpQuerierState_Object = MibTableColumn
hpSwitchIgmpQuerierState = _HpSwitchIgmpQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1, 1, 3),
    _HpSwitchIgmpQuerierState_Type()
)
hpSwitchIgmpQuerierState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpQuerierState.setStatus("mandatory")


class _HpSwitchIgmpPriorityState_Type(Integer32):
    """Custom type hpSwitchIgmpPriorityState based on Integer32"""
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


_HpSwitchIgmpPriorityState_Type.__name__ = "Integer32"
_HpSwitchIgmpPriorityState_Object = MibTableColumn
hpSwitchIgmpPriorityState = _HpSwitchIgmpPriorityState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1, 1, 4),
    _HpSwitchIgmpPriorityState_Type()
)
hpSwitchIgmpPriorityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpPriorityState.setStatus("deprecated")


class _HpSwitchIgmpQuerierInterval_Type(Integer32):
    """Custom type hpSwitchIgmpQuerierInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HpSwitchIgmpQuerierInterval_Type.__name__ = "Integer32"
_HpSwitchIgmpQuerierInterval_Object = MibTableColumn
hpSwitchIgmpQuerierInterval = _HpSwitchIgmpQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1, 1, 5),
    _HpSwitchIgmpQuerierInterval_Type()
)
hpSwitchIgmpQuerierInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpQuerierInterval.setStatus("mandatory")
_HpSwitchIgmpProxyDomainMap_Type = Integer32
_HpSwitchIgmpProxyDomainMap_Object = MibTableColumn
hpSwitchIgmpProxyDomainMap = _HpSwitchIgmpProxyDomainMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 1, 1, 6),
    _HpSwitchIgmpProxyDomainMap_Type()
)
hpSwitchIgmpProxyDomainMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainMap.setStatus("mandatory")
_HpSwitchIgmpPortConfigTable_Object = MibTable
hpSwitchIgmpPortConfigTable = _HpSwitchIgmpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 2)
)
if mibBuilder.loadTexts:
    hpSwitchIgmpPortConfigTable.setStatus("mandatory")
_HpSwitchIgmpPortConfigEntry_Object = MibTableRow
hpSwitchIgmpPortConfigEntry = _HpSwitchIgmpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 2, 1)
)
hpSwitchIgmpPortConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchIgmpPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchIgmpPortConfigEntry.setStatus("mandatory")


class _HpSwitchIgmpPortIndex_Type(Integer32):
    """Custom type hpSwitchIgmpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIgmpPortIndex_Type.__name__ = "Integer32"
_HpSwitchIgmpPortIndex_Object = MibTableColumn
hpSwitchIgmpPortIndex = _HpSwitchIgmpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 2, 1, 1),
    _HpSwitchIgmpPortIndex_Type()
)
hpSwitchIgmpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIgmpPortIndex.setStatus("mandatory")
_HpSwitchIgmpPortType_Type = HpSwitchPortType
_HpSwitchIgmpPortType_Object = MibTableColumn
hpSwitchIgmpPortType = _HpSwitchIgmpPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 2, 1, 2),
    _HpSwitchIgmpPortType_Type()
)
hpSwitchIgmpPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIgmpPortType.setStatus("mandatory")


class _HpSwitchIgmpIpMcastState_Type(Integer32):
    """Custom type hpSwitchIgmpIpMcastState based on Integer32"""
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
          ("blocked", 2),
          ("forward", 3))
    )


_HpSwitchIgmpIpMcastState_Type.__name__ = "Integer32"
_HpSwitchIgmpIpMcastState_Object = MibTableColumn
hpSwitchIgmpIpMcastState = _HpSwitchIgmpIpMcastState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 2, 1, 3),
    _HpSwitchIgmpIpMcastState_Type()
)
hpSwitchIgmpIpMcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpIpMcastState.setStatus("mandatory")
_HpSwitchIgmpPortConfigTable2_Object = MibTable
hpSwitchIgmpPortConfigTable2 = _HpSwitchIgmpPortConfigTable2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3)
)
if mibBuilder.loadTexts:
    hpSwitchIgmpPortConfigTable2.setStatus("mandatory")
_HpSwitchIgmpPortConfigEntry2_Object = MibTableRow
hpSwitchIgmpPortConfigEntry2 = _HpSwitchIgmpPortConfigEntry2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3, 1)
)
hpSwitchIgmpPortConfigEntry2.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchIgmpPortVlanIndex2"),
    (0, "CONFIG-MIB", "hpSwitchIgmpPortIndex2"),
)
if mibBuilder.loadTexts:
    hpSwitchIgmpPortConfigEntry2.setStatus("mandatory")


class _HpSwitchIgmpPortVlanIndex2_Type(Integer32):
    """Custom type hpSwitchIgmpPortVlanIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIgmpPortVlanIndex2_Type.__name__ = "Integer32"
_HpSwitchIgmpPortVlanIndex2_Object = MibTableColumn
hpSwitchIgmpPortVlanIndex2 = _HpSwitchIgmpPortVlanIndex2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3, 1, 1),
    _HpSwitchIgmpPortVlanIndex2_Type()
)
hpSwitchIgmpPortVlanIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIgmpPortVlanIndex2.setStatus("mandatory")


class _HpSwitchIgmpPortIndex2_Type(Integer32):
    """Custom type hpSwitchIgmpPortIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIgmpPortIndex2_Type.__name__ = "Integer32"
_HpSwitchIgmpPortIndex2_Object = MibTableColumn
hpSwitchIgmpPortIndex2 = _HpSwitchIgmpPortIndex2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3, 1, 2),
    _HpSwitchIgmpPortIndex2_Type()
)
hpSwitchIgmpPortIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIgmpPortIndex2.setStatus("mandatory")
_HpSwitchIgmpPortType2_Type = HpSwitchPortType
_HpSwitchIgmpPortType2_Object = MibTableColumn
hpSwitchIgmpPortType2 = _HpSwitchIgmpPortType2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3, 1, 3),
    _HpSwitchIgmpPortType2_Type()
)
hpSwitchIgmpPortType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIgmpPortType2.setStatus("mandatory")


class _HpSwitchIgmpIpMcastState2_Type(Integer32):
    """Custom type hpSwitchIgmpIpMcastState2 based on Integer32"""
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
          ("blocked", 2),
          ("forward", 3))
    )


_HpSwitchIgmpIpMcastState2_Type.__name__ = "Integer32"
_HpSwitchIgmpIpMcastState2_Object = MibTableColumn
hpSwitchIgmpIpMcastState2 = _HpSwitchIgmpIpMcastState2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3, 1, 4),
    _HpSwitchIgmpIpMcastState2_Type()
)
hpSwitchIgmpIpMcastState2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpIpMcastState2.setStatus("mandatory")


class _HpSwitchIgmpPortForcedLeaveState_Type(Integer32):
    """Custom type hpSwitchIgmpPortForcedLeaveState based on Integer32"""
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


_HpSwitchIgmpPortForcedLeaveState_Type.__name__ = "Integer32"
_HpSwitchIgmpPortForcedLeaveState_Object = MibTableColumn
hpSwitchIgmpPortForcedLeaveState = _HpSwitchIgmpPortForcedLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3, 1, 5),
    _HpSwitchIgmpPortForcedLeaveState_Type()
)
hpSwitchIgmpPortForcedLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpPortForcedLeaveState.setStatus("mandatory")


class _HpSwitchIgmpPortFastLeaveState_Type(Integer32):
    """Custom type hpSwitchIgmpPortFastLeaveState based on Integer32"""
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


_HpSwitchIgmpPortFastLeaveState_Type.__name__ = "Integer32"
_HpSwitchIgmpPortFastLeaveState_Object = MibTableColumn
hpSwitchIgmpPortFastLeaveState = _HpSwitchIgmpPortFastLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 3, 1, 6),
    _HpSwitchIgmpPortFastLeaveState_Type()
)
hpSwitchIgmpPortFastLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpPortFastLeaveState.setStatus("mandatory")


class _HpSwitchIgmpForcedLeaveInterval_Type(Integer32):
    """Custom type hpSwitchIgmpForcedLeaveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIgmpForcedLeaveInterval_Type.__name__ = "Integer32"
_HpSwitchIgmpForcedLeaveInterval_Object = MibScalar
hpSwitchIgmpForcedLeaveInterval = _HpSwitchIgmpForcedLeaveInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 4),
    _HpSwitchIgmpForcedLeaveInterval_Type()
)
hpSwitchIgmpForcedLeaveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgmpForcedLeaveInterval.setStatus("mandatory")
_HpSwitchCosConfig_ObjectIdentity = ObjectIdentity
hpSwitchCosConfig = _HpSwitchCosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17)
)
_HpSwitchCosPortConfigTable_Object = MibTable
hpSwitchCosPortConfigTable = _HpSwitchCosPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1)
)
if mibBuilder.loadTexts:
    hpSwitchCosPortConfigTable.setStatus("mandatory")
_HpSwitchCosPortConfigEntry_Object = MibTableRow
hpSwitchCosPortConfigEntry = _HpSwitchCosPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1)
)
hpSwitchCosPortConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchCosPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchCosPortConfigEntry.setStatus("mandatory")


class _HpSwitchCosPortIndex_Type(Integer32):
    """Custom type hpSwitchCosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchCosPortIndex_Type.__name__ = "Integer32"
_HpSwitchCosPortIndex_Object = MibTableColumn
hpSwitchCosPortIndex = _HpSwitchCosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 1),
    _HpSwitchCosPortIndex_Type()
)
hpSwitchCosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosPortIndex.setStatus("mandatory")
_HpSwitchCosPortType_Type = HpSwitchPortType
_HpSwitchCosPortType_Object = MibTableColumn
hpSwitchCosPortType = _HpSwitchCosPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 2),
    _HpSwitchCosPortType_Type()
)
hpSwitchCosPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosPortType.setStatus("deprecated")


class _HpSwitchCosPortPriority_Type(Integer32):
    """Custom type hpSwitchCosPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchCosPortPriority_Type.__name__ = "Integer32"
_HpSwitchCosPortPriority_Object = MibTableColumn
hpSwitchCosPortPriority = _HpSwitchCosPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 3),
    _HpSwitchCosPortPriority_Type()
)
hpSwitchCosPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosPortPriority.setStatus("mandatory")


class _HpSwitchCosPortDSCPPolicy_Type(Integer32):
    """Custom type hpSwitchCosPortDSCPPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpSwitchCosPortDSCPPolicy_Type.__name__ = "Integer32"
_HpSwitchCosPortDSCPPolicy_Object = MibTableColumn
hpSwitchCosPortDSCPPolicy = _HpSwitchCosPortDSCPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 4),
    _HpSwitchCosPortDSCPPolicy_Type()
)
hpSwitchCosPortDSCPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosPortDSCPPolicy.setStatus("mandatory")


class _HpSwitchCosPortResolvedPriority_Type(Integer32):
    """Custom type hpSwitchCosPortResolvedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpSwitchCosPortResolvedPriority_Type.__name__ = "Integer32"
_HpSwitchCosPortResolvedPriority_Object = MibTableColumn
hpSwitchCosPortResolvedPriority = _HpSwitchCosPortResolvedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 5),
    _HpSwitchCosPortResolvedPriority_Type()
)
hpSwitchCosPortResolvedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosPortResolvedPriority.setStatus("mandatory")


class _HpSwitchCosPortApplyPolicy_Type(Integer32):
    """Custom type hpSwitchCosPortApplyPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyHpSwitchCosPortDSCPPolicy", 3),
          ("applyHpSwitchCosPortPriority", 2),
          ("noPolicyOverride", 1))
    )


_HpSwitchCosPortApplyPolicy_Type.__name__ = "Integer32"
_HpSwitchCosPortApplyPolicy_Object = MibTableColumn
hpSwitchCosPortApplyPolicy = _HpSwitchCosPortApplyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 6),
    _HpSwitchCosPortApplyPolicy_Type()
)
hpSwitchCosPortApplyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosPortApplyPolicy.setStatus("mandatory")


class _HpSwitchCosPortTrustMode_Type(Integer32):
    """Custom type hpSwitchCosPortTrustMode based on Integer32"""
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
        *(("trust8021pCos", 2),
          ("trustAll", 5),
          ("trustNone", 1),
          ("trustPartnerDevice", 6),
          ("trustTosDiffserv", 4),
          ("trustTosIpPrecedence", 3))
    )


_HpSwitchCosPortTrustMode_Type.__name__ = "Integer32"
_HpSwitchCosPortTrustMode_Object = MibTableColumn
hpSwitchCosPortTrustMode = _HpSwitchCosPortTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 7),
    _HpSwitchCosPortTrustMode_Type()
)
hpSwitchCosPortTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosPortTrustMode.setStatus("mandatory")
_HpSwitchCosPortPartnerDevice_Type = HpPartnerDeviceTypeList
_HpSwitchCosPortPartnerDevice_Object = MibTableColumn
hpSwitchCosPortPartnerDevice = _HpSwitchCosPortPartnerDevice_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 8),
    _HpSwitchCosPortPartnerDevice_Type()
)
hpSwitchCosPortPartnerDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosPortPartnerDevice.setStatus("mandatory")


class _HpSwitchCosPortTrustedPartnerState_Type(Integer32):
    """Custom type hpSwitchCosPortTrustedPartnerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 2),
          ("untrusted", 1))
    )


_HpSwitchCosPortTrustedPartnerState_Type.__name__ = "Integer32"
_HpSwitchCosPortTrustedPartnerState_Object = MibTableColumn
hpSwitchCosPortTrustedPartnerState = _HpSwitchCosPortTrustedPartnerState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 1, 1, 9),
    _HpSwitchCosPortTrustedPartnerState_Type()
)
hpSwitchCosPortTrustedPartnerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosPortTrustedPartnerState.setStatus("mandatory")
_HpSwitchCosVlanConfigTable_Object = MibTable
hpSwitchCosVlanConfigTable = _HpSwitchCosVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 2)
)
if mibBuilder.loadTexts:
    hpSwitchCosVlanConfigTable.setStatus("mandatory")
_HpSwitchCosVlanConfigEntry_Object = MibTableRow
hpSwitchCosVlanConfigEntry = _HpSwitchCosVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 2, 1)
)
hpSwitchCosVlanConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchCosVlanIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchCosVlanConfigEntry.setStatus("mandatory")
_HpSwitchCosVlanIndex_Type = VlanID
_HpSwitchCosVlanIndex_Object = MibTableColumn
hpSwitchCosVlanIndex = _HpSwitchCosVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 2, 1, 1),
    _HpSwitchCosVlanIndex_Type()
)
hpSwitchCosVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosVlanIndex.setStatus("mandatory")


class _HpSwitchCosVlanPriority_Type(Integer32):
    """Custom type hpSwitchCosVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchCosVlanPriority_Type.__name__ = "Integer32"
_HpSwitchCosVlanPriority_Object = MibTableColumn
hpSwitchCosVlanPriority = _HpSwitchCosVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 2, 1, 2),
    _HpSwitchCosVlanPriority_Type()
)
hpSwitchCosVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosVlanPriority.setStatus("mandatory")


class _HpSwitchCosVlanDSCPPolicy_Type(Integer32):
    """Custom type hpSwitchCosVlanDSCPPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpSwitchCosVlanDSCPPolicy_Type.__name__ = "Integer32"
_HpSwitchCosVlanDSCPPolicy_Object = MibTableColumn
hpSwitchCosVlanDSCPPolicy = _HpSwitchCosVlanDSCPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 2, 1, 3),
    _HpSwitchCosVlanDSCPPolicy_Type()
)
hpSwitchCosVlanDSCPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosVlanDSCPPolicy.setStatus("mandatory")


class _HpSwitchCosVlanResolvedPriority_Type(Integer32):
    """Custom type hpSwitchCosVlanResolvedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpSwitchCosVlanResolvedPriority_Type.__name__ = "Integer32"
_HpSwitchCosVlanResolvedPriority_Object = MibTableColumn
hpSwitchCosVlanResolvedPriority = _HpSwitchCosVlanResolvedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 2, 1, 4),
    _HpSwitchCosVlanResolvedPriority_Type()
)
hpSwitchCosVlanResolvedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosVlanResolvedPriority.setStatus("mandatory")


class _HpSwitchCosVlanApplyPolicy_Type(Integer32):
    """Custom type hpSwitchCosVlanApplyPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyHpSwitchCosVlanDSCPPolicy", 3),
          ("applyHpSwitchCosVlanPriority", 2),
          ("noPolicyOverride", 1))
    )


_HpSwitchCosVlanApplyPolicy_Type.__name__ = "Integer32"
_HpSwitchCosVlanApplyPolicy_Object = MibTableColumn
hpSwitchCosVlanApplyPolicy = _HpSwitchCosVlanApplyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 2, 1, 5),
    _HpSwitchCosVlanApplyPolicy_Type()
)
hpSwitchCosVlanApplyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosVlanApplyPolicy.setStatus("mandatory")
_HpSwitchCosProtocolConfigTable_Object = MibTable
hpSwitchCosProtocolConfigTable = _HpSwitchCosProtocolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 3)
)
if mibBuilder.loadTexts:
    hpSwitchCosProtocolConfigTable.setStatus("mandatory")
_HpSwitchCosProtocolConfigEntry_Object = MibTableRow
hpSwitchCosProtocolConfigEntry = _HpSwitchCosProtocolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 3, 1)
)
hpSwitchCosProtocolConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchCosProtocolType"),
)
if mibBuilder.loadTexts:
    hpSwitchCosProtocolConfigEntry.setStatus("mandatory")


class _HpSwitchCosProtocolType_Type(Integer32):
    """Custom type hpSwitchCosProtocolType based on Integer32"""
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
        *(("appletalk", 5),
          ("arp", 3),
          ("decnet", 4),
          ("ip", 1),
          ("ipx", 2),
          ("netbios", 7),
          ("sna", 6))
    )


_HpSwitchCosProtocolType_Type.__name__ = "Integer32"
_HpSwitchCosProtocolType_Object = MibTableColumn
hpSwitchCosProtocolType = _HpSwitchCosProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 3, 1, 1),
    _HpSwitchCosProtocolType_Type()
)
hpSwitchCosProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosProtocolType.setStatus("mandatory")


class _HpSwitchCosProtocolPriority_Type(Integer32):
    """Custom type hpSwitchCosProtocolPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchCosProtocolPriority_Type.__name__ = "Integer32"
_HpSwitchCosProtocolPriority_Object = MibTableColumn
hpSwitchCosProtocolPriority = _HpSwitchCosProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 3, 1, 2),
    _HpSwitchCosProtocolPriority_Type()
)
hpSwitchCosProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosProtocolPriority.setStatus("mandatory")
_HpSwitchCosAddressConfigTable_Object = MibTable
hpSwitchCosAddressConfigTable = _HpSwitchCosAddressConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4)
)
if mibBuilder.loadTexts:
    hpSwitchCosAddressConfigTable.setStatus("mandatory")
_HpSwitchCosAddressConfigEntry_Object = MibTableRow
hpSwitchCosAddressConfigEntry = _HpSwitchCosAddressConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1)
)
hpSwitchCosAddressConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchCosAddressIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchCosAddressConfigEntry.setStatus("mandatory")


class _HpSwitchCosAddressIndex_Type(Integer32):
    """Custom type hpSwitchCosAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchCosAddressIndex_Type.__name__ = "Integer32"
_HpSwitchCosAddressIndex_Object = MibTableColumn
hpSwitchCosAddressIndex = _HpSwitchCosAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 1),
    _HpSwitchCosAddressIndex_Type()
)
hpSwitchCosAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosAddressIndex.setStatus("mandatory")


class _HpSwitchCosAddressType_Type(Integer32):
    """Custom type hpSwitchCosAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipv6", 2))
    )


_HpSwitchCosAddressType_Type.__name__ = "Integer32"
_HpSwitchCosAddressType_Object = MibTableColumn
hpSwitchCosAddressType = _HpSwitchCosAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 2),
    _HpSwitchCosAddressType_Type()
)
hpSwitchCosAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressType.setStatus("mandatory")
_HpSwitchCosAddressIp_Type = IpAddress
_HpSwitchCosAddressIp_Object = MibTableColumn
hpSwitchCosAddressIp = _HpSwitchCosAddressIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 3),
    _HpSwitchCosAddressIp_Type()
)
hpSwitchCosAddressIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressIp.setStatus("mandatory")


class _HpSwitchCosAddressPriority_Type(Integer32):
    """Custom type hpSwitchCosAddressPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchCosAddressPriority_Type.__name__ = "Integer32"
_HpSwitchCosAddressPriority_Object = MibTableColumn
hpSwitchCosAddressPriority = _HpSwitchCosAddressPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 4),
    _HpSwitchCosAddressPriority_Type()
)
hpSwitchCosAddressPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressPriority.setStatus("mandatory")
_HpSwitchCosAddressStatus_Type = RowStatus
_HpSwitchCosAddressStatus_Object = MibTableColumn
hpSwitchCosAddressStatus = _HpSwitchCosAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 5),
    _HpSwitchCosAddressStatus_Type()
)
hpSwitchCosAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressStatus.setStatus("mandatory")


class _HpSwitchCosAddressDSCPPolicy_Type(Integer32):
    """Custom type hpSwitchCosAddressDSCPPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpSwitchCosAddressDSCPPolicy_Type.__name__ = "Integer32"
_HpSwitchCosAddressDSCPPolicy_Object = MibTableColumn
hpSwitchCosAddressDSCPPolicy = _HpSwitchCosAddressDSCPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 6),
    _HpSwitchCosAddressDSCPPolicy_Type()
)
hpSwitchCosAddressDSCPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressDSCPPolicy.setStatus("mandatory")


class _HpSwitchCosAddressResolvedPriority_Type(Integer32):
    """Custom type hpSwitchCosAddressResolvedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpSwitchCosAddressResolvedPriority_Type.__name__ = "Integer32"
_HpSwitchCosAddressResolvedPriority_Object = MibTableColumn
hpSwitchCosAddressResolvedPriority = _HpSwitchCosAddressResolvedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 7),
    _HpSwitchCosAddressResolvedPriority_Type()
)
hpSwitchCosAddressResolvedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosAddressResolvedPriority.setStatus("mandatory")


class _HpSwitchCosAddressApplyPolicy_Type(Integer32):
    """Custom type hpSwitchCosAddressApplyPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("applyHpSwitchCosAddressDSCPPolicy", 2),
          ("applyHpSwitchCosAddressPriority", 1))
    )


_HpSwitchCosAddressApplyPolicy_Type.__name__ = "Integer32"
_HpSwitchCosAddressApplyPolicy_Object = MibTableColumn
hpSwitchCosAddressApplyPolicy = _HpSwitchCosAddressApplyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 8),
    _HpSwitchCosAddressApplyPolicy_Type()
)
hpSwitchCosAddressApplyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressApplyPolicy.setStatus("mandatory")
_HpSwitchCosIpv4AddressMask_Type = IpAddress
_HpSwitchCosIpv4AddressMask_Object = MibTableColumn
hpSwitchCosIpv4AddressMask = _HpSwitchCosIpv4AddressMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 9),
    _HpSwitchCosIpv4AddressMask_Type()
)
hpSwitchCosIpv4AddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosIpv4AddressMask.setStatus("mandatory")
_HpSwitchCosAddressIpv6_Type = InetAddress
_HpSwitchCosAddressIpv6_Object = MibTableColumn
hpSwitchCosAddressIpv6 = _HpSwitchCosAddressIpv6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 10),
    _HpSwitchCosAddressIpv6_Type()
)
hpSwitchCosAddressIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressIpv6.setStatus("mandatory")
_HpSwitchCosAddressIpv6PrefixLength_Type = InetAddressPrefixLength
_HpSwitchCosAddressIpv6PrefixLength_Object = MibTableColumn
hpSwitchCosAddressIpv6PrefixLength = _HpSwitchCosAddressIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 4, 1, 11),
    _HpSwitchCosAddressIpv6PrefixLength_Type()
)
hpSwitchCosAddressIpv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAddressIpv6PrefixLength.setStatus("mandatory")
_HpSwitchCosTosConfig_ObjectIdentity = ObjectIdentity
hpSwitchCosTosConfig = _HpSwitchCosTosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5)
)


class _HpSwitchCosTosConfigMode_Type(Integer32):
    """Custom type hpSwitchCosTosConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diffserv", 3),
          ("disable", 1),
          ("ipprecedence", 2))
    )


_HpSwitchCosTosConfigMode_Type.__name__ = "Integer32"
_HpSwitchCosTosConfigMode_Object = MibScalar
hpSwitchCosTosConfigMode = _HpSwitchCosTosConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 1),
    _HpSwitchCosTosConfigMode_Type()
)
hpSwitchCosTosConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosTosConfigMode.setStatus("mandatory")
_HpSwitchCosTosConfigTable_Object = MibTable
hpSwitchCosTosConfigTable = _HpSwitchCosTosConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 2)
)
if mibBuilder.loadTexts:
    hpSwitchCosTosConfigTable.setStatus("mandatory")
_HpSwitchCosTosConfigEntry_Object = MibTableRow
hpSwitchCosTosConfigEntry = _HpSwitchCosTosConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 2, 1)
)
hpSwitchCosTosConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchCosTosIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchCosTosConfigEntry.setStatus("mandatory")
_HpSwitchCosTosIndex_Type = Integer32
_HpSwitchCosTosIndex_Object = MibTableColumn
hpSwitchCosTosIndex = _HpSwitchCosTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 2, 1, 1),
    _HpSwitchCosTosIndex_Type()
)
hpSwitchCosTosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosTosIndex.setStatus("mandatory")


class _HpSwitchCosTosPriority_Type(Integer32):
    """Custom type hpSwitchCosTosPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchCosTosPriority_Type.__name__ = "Integer32"
_HpSwitchCosTosPriority_Object = MibTableColumn
hpSwitchCosTosPriority = _HpSwitchCosTosPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 2, 1, 2),
    _HpSwitchCosTosPriority_Type()
)
hpSwitchCosTosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosTosPriority.setStatus("deprecated")


class _HpSwitchCosTosDSCPPolicy_Type(Integer32):
    """Custom type hpSwitchCosTosDSCPPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpSwitchCosTosDSCPPolicy_Type.__name__ = "Integer32"
_HpSwitchCosTosDSCPPolicy_Object = MibTableColumn
hpSwitchCosTosDSCPPolicy = _HpSwitchCosTosDSCPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 2, 1, 3),
    _HpSwitchCosTosDSCPPolicy_Type()
)
hpSwitchCosTosDSCPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosTosDSCPPolicy.setStatus("mandatory")


class _HpSwitchCosTosResolvedPriority_Type(Integer32):
    """Custom type hpSwitchCosTosResolvedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpSwitchCosTosResolvedPriority_Type.__name__ = "Integer32"
_HpSwitchCosTosResolvedPriority_Object = MibTableColumn
hpSwitchCosTosResolvedPriority = _HpSwitchCosTosResolvedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 2, 1, 4),
    _HpSwitchCosTosResolvedPriority_Type()
)
hpSwitchCosTosResolvedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosTosResolvedPriority.setStatus("mandatory")


class _HpSwitchCosTosApplyPolicy_Type(Integer32):
    """Custom type hpSwitchCosTosApplyPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("applyHpSwitchCosTosDSCPPolicy", 2),
          ("applyInheritedPriority", 1))
    )


_HpSwitchCosTosApplyPolicy_Type.__name__ = "Integer32"
_HpSwitchCosTosApplyPolicy_Object = MibTableColumn
hpSwitchCosTosApplyPolicy = _HpSwitchCosTosApplyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 5, 2, 1, 5),
    _HpSwitchCosTosApplyPolicy_Type()
)
hpSwitchCosTosApplyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosTosApplyPolicy.setStatus("mandatory")
_HpSwitchCosDSCPPolicyConfigTable_Object = MibTable
hpSwitchCosDSCPPolicyConfigTable = _HpSwitchCosDSCPPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 6)
)
if mibBuilder.loadTexts:
    hpSwitchCosDSCPPolicyConfigTable.setStatus("mandatory")
_HpSwitchCosDSCPPolicyConfigEntry_Object = MibTableRow
hpSwitchCosDSCPPolicyConfigEntry = _HpSwitchCosDSCPPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 6, 1)
)
hpSwitchCosDSCPPolicyConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchCosDSCPPolicyIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchCosDSCPPolicyConfigEntry.setStatus("mandatory")


class _HpSwitchCosDSCPPolicyIndex_Type(Integer32):
    """Custom type hpSwitchCosDSCPPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpSwitchCosDSCPPolicyIndex_Type.__name__ = "Integer32"
_HpSwitchCosDSCPPolicyIndex_Object = MibTableColumn
hpSwitchCosDSCPPolicyIndex = _HpSwitchCosDSCPPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 6, 1, 1),
    _HpSwitchCosDSCPPolicyIndex_Type()
)
hpSwitchCosDSCPPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchCosDSCPPolicyIndex.setStatus("mandatory")


class _HpSwitchCosDSCPPolicyPriority_Type(Integer32):
    """Custom type hpSwitchCosDSCPPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpSwitchCosDSCPPolicyPriority_Type.__name__ = "Integer32"
_HpSwitchCosDSCPPolicyPriority_Object = MibTableColumn
hpSwitchCosDSCPPolicyPriority = _HpSwitchCosDSCPPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 6, 1, 2),
    _HpSwitchCosDSCPPolicyPriority_Type()
)
hpSwitchCosDSCPPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosDSCPPolicyPriority.setStatus("mandatory")


class _HpSwitchCosDSCPPolicyName_Type(OctetString):
    """Custom type hpSwitchCosDSCPPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpSwitchCosDSCPPolicyName_Type.__name__ = "OctetString"
_HpSwitchCosDSCPPolicyName_Object = MibTableColumn
hpSwitchCosDSCPPolicyName = _HpSwitchCosDSCPPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 6, 1, 3),
    _HpSwitchCosDSCPPolicyName_Type()
)
hpSwitchCosDSCPPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosDSCPPolicyName.setStatus("mandatory")
_HpSwitchCosAppTypeConfigTable_Object = MibTable
hpSwitchCosAppTypeConfigTable = _HpSwitchCosAppTypeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7)
)
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeConfigTable.setStatus("mandatory")
_HpSwitchCosAppTypeConfigEntry_Object = MibTableRow
hpSwitchCosAppTypeConfigEntry = _HpSwitchCosAppTypeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1)
)
hpSwitchCosAppTypeConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchCosAppTypeConfigIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeConfigEntry.setStatus("mandatory")


class _HpSwitchCosAppTypeConfigIndex_Type(Integer32):
    """Custom type hpSwitchCosAppTypeConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchCosAppTypeConfigIndex_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeConfigIndex_Object = MibTableColumn
hpSwitchCosAppTypeConfigIndex = _HpSwitchCosAppTypeConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 1),
    _HpSwitchCosAppTypeConfigIndex_Type()
)
hpSwitchCosAppTypeConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeConfigIndex.setStatus("mandatory")


class _HpSwitchCosAppTypeConfigType_Type(Integer32):
    """Custom type hpSwitchCosAppTypeConfigType based on Integer32"""
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
        *(("tcpBothPortsConfig", 6),
          ("tcpDestPortConfig", 5),
          ("tcpSrcPortConfig", 4),
          ("udpBothPortsConfig", 3),
          ("udpDestPortConfig", 2),
          ("udpSrcPortConfig", 1))
    )


_HpSwitchCosAppTypeConfigType_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeConfigType_Object = MibTableColumn
hpSwitchCosAppTypeConfigType = _HpSwitchCosAppTypeConfigType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 2),
    _HpSwitchCosAppTypeConfigType_Type()
)
hpSwitchCosAppTypeConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeConfigType.setStatus("mandatory")


class _HpSwitchCosAppTypeSrcPort_Type(Integer32):
    """Custom type hpSwitchCosAppTypeSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchCosAppTypeSrcPort_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeSrcPort_Object = MibTableColumn
hpSwitchCosAppTypeSrcPort = _HpSwitchCosAppTypeSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 3),
    _HpSwitchCosAppTypeSrcPort_Type()
)
hpSwitchCosAppTypeSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeSrcPort.setStatus("mandatory")


class _HpSwitchCosAppTypeDestPort_Type(Integer32):
    """Custom type hpSwitchCosAppTypeDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchCosAppTypeDestPort_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeDestPort_Object = MibTableColumn
hpSwitchCosAppTypeDestPort = _HpSwitchCosAppTypeDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 4),
    _HpSwitchCosAppTypeDestPort_Type()
)
hpSwitchCosAppTypeDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeDestPort.setStatus("mandatory")


class _HpSwitchCosAppTypePriority_Type(Integer32):
    """Custom type hpSwitchCosAppTypePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpSwitchCosAppTypePriority_Type.__name__ = "Integer32"
_HpSwitchCosAppTypePriority_Object = MibTableColumn
hpSwitchCosAppTypePriority = _HpSwitchCosAppTypePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 5),
    _HpSwitchCosAppTypePriority_Type()
)
hpSwitchCosAppTypePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypePriority.setStatus("mandatory")


class _HpSwitchCosAppTypeDSCPPolicy_Type(Integer32):
    """Custom type hpSwitchCosAppTypeDSCPPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpSwitchCosAppTypeDSCPPolicy_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeDSCPPolicy_Object = MibTableColumn
hpSwitchCosAppTypeDSCPPolicy = _HpSwitchCosAppTypeDSCPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 6),
    _HpSwitchCosAppTypeDSCPPolicy_Type()
)
hpSwitchCosAppTypeDSCPPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeDSCPPolicy.setStatus("mandatory")


class _HpSwitchCosAppTypeResolvedPriority_Type(Integer32):
    """Custom type hpSwitchCosAppTypeResolvedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpSwitchCosAppTypeResolvedPriority_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeResolvedPriority_Object = MibTableColumn
hpSwitchCosAppTypeResolvedPriority = _HpSwitchCosAppTypeResolvedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 7),
    _HpSwitchCosAppTypeResolvedPriority_Type()
)
hpSwitchCosAppTypeResolvedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeResolvedPriority.setStatus("mandatory")


class _HpSwitchCosAppTypeApplyPolicy_Type(Integer32):
    """Custom type hpSwitchCosAppTypeApplyPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("applyHpSwitchCosAppTypeDSCPPolicy", 2),
          ("applyHpSwitchCosAppTypePriority", 1))
    )


_HpSwitchCosAppTypeApplyPolicy_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeApplyPolicy_Object = MibTableColumn
hpSwitchCosAppTypeApplyPolicy = _HpSwitchCosAppTypeApplyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 8),
    _HpSwitchCosAppTypeApplyPolicy_Type()
)
hpSwitchCosAppTypeApplyPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeApplyPolicy.setStatus("mandatory")
_HpSwitchCosAppTypeStatus_Type = RowStatus
_HpSwitchCosAppTypeStatus_Object = MibTableColumn
hpSwitchCosAppTypeStatus = _HpSwitchCosAppTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 9),
    _HpSwitchCosAppTypeStatus_Type()
)
hpSwitchCosAppTypeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeStatus.setStatus("mandatory")


class _HpSwitchCosAppTypeMaxSrcPort_Type(Integer32):
    """Custom type hpSwitchCosAppTypeMaxSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchCosAppTypeMaxSrcPort_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeMaxSrcPort_Object = MibTableColumn
hpSwitchCosAppTypeMaxSrcPort = _HpSwitchCosAppTypeMaxSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 10),
    _HpSwitchCosAppTypeMaxSrcPort_Type()
)
hpSwitchCosAppTypeMaxSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeMaxSrcPort.setStatus("mandatory")


class _HpSwitchCosAppTypeMaxDestPort_Type(Integer32):
    """Custom type hpSwitchCosAppTypeMaxDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchCosAppTypeMaxDestPort_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeMaxDestPort_Object = MibTableColumn
hpSwitchCosAppTypeMaxDestPort = _HpSwitchCosAppTypeMaxDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 11),
    _HpSwitchCosAppTypeMaxDestPort_Type()
)
hpSwitchCosAppTypeMaxDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeMaxDestPort.setStatus("mandatory")


class _HpSwitchCosAppTypeIpPacketType_Type(Integer32):
    """Custom type hpSwitchCosAppTypeIpPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4AndIpv6Packets", 3),
          ("ipv4PacketsOnly", 1),
          ("ipv6PacketsOnly", 2))
    )


_HpSwitchCosAppTypeIpPacketType_Type.__name__ = "Integer32"
_HpSwitchCosAppTypeIpPacketType_Object = MibTableColumn
hpSwitchCosAppTypeIpPacketType = _HpSwitchCosAppTypeIpPacketType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 7, 1, 12),
    _HpSwitchCosAppTypeIpPacketType_Type()
)
hpSwitchCosAppTypeIpPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCosAppTypeIpPacketType.setStatus("mandatory")
_HpSwitchCosLastChange_Type = TimeStamp
_HpSwitchCosLastChange_Object = MibScalar
hpSwitchCosLastChange = _HpSwitchCosLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 8),
    _HpSwitchCosLastChange_Type()
)
hpSwitchCosLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchCosLastChange.setStatus("mandatory")


class _HpSwitchConfigCosLastConfigError_Type(Integer32):
    """Custom type hpSwitchConfigCosLastConfigError based on Integer32"""
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
        *(("aclQosNoError", 1),
          ("aclQosTooManyLookupsError", 6),
          ("aclQosTooManyMasksError", 3),
          ("aclQosTooManyMetersError", 5),
          ("aclQosTooManyRangesError", 4),
          ("aclQosTooManyRulesError", 2))
    )


_HpSwitchConfigCosLastConfigError_Type.__name__ = "Integer32"
_HpSwitchConfigCosLastConfigError_Object = MibScalar
hpSwitchConfigCosLastConfigError = _HpSwitchConfigCosLastConfigError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 9),
    _HpSwitchConfigCosLastConfigError_Type()
)
hpSwitchConfigCosLastConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchConfigCosLastConfigError.setStatus("mandatory")
_HpSwitchQueueWatchTable_Object = MibTable
hpSwitchQueueWatchTable = _HpSwitchQueueWatchTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 10)
)
if mibBuilder.loadTexts:
    hpSwitchQueueWatchTable.setStatus("mandatory")
_HpSwitchQueueWatchEntry_Object = MibTableRow
hpSwitchQueueWatchEntry = _HpSwitchQueueWatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 10, 1)
)
hpSwitchQueueWatchEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchQueueWatchPort"),
)
if mibBuilder.loadTexts:
    hpSwitchQueueWatchEntry.setStatus("mandatory")


class _HpSwitchQueueWatchPort_Type(Integer32):
    """Custom type hpSwitchQueueWatchPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchQueueWatchPort_Type.__name__ = "Integer32"
_HpSwitchQueueWatchPort_Object = MibTableColumn
hpSwitchQueueWatchPort = _HpSwitchQueueWatchPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 10, 1, 1),
    _HpSwitchQueueWatchPort_Type()
)
hpSwitchQueueWatchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchQueueWatchPort.setStatus("mandatory")


class _HpSwitchQueueWatchState_Type(Integer32):
    """Custom type hpSwitchQueueWatchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("outbound", 2))
    )


_HpSwitchQueueWatchState_Type.__name__ = "Integer32"
_HpSwitchQueueWatchState_Object = MibTableColumn
hpSwitchQueueWatchState = _HpSwitchQueueWatchState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 17, 10, 1, 2),
    _HpSwitchQueueWatchState_Type()
)
hpSwitchQueueWatchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchQueueWatchState.setStatus("mandatory")
_HpSwitchMeshConfig_ObjectIdentity = ObjectIdentity
hpSwitchMeshConfig = _HpSwitchMeshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 18)
)


class _HpSwitchMeshMulticastAgingMode_Type(Integer32):
    """Custom type hpSwitchMeshMulticastAgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aging", 1),
          ("nonaging", 2))
    )


_HpSwitchMeshMulticastAgingMode_Type.__name__ = "Integer32"
_HpSwitchMeshMulticastAgingMode_Object = MibScalar
hpSwitchMeshMulticastAgingMode = _HpSwitchMeshMulticastAgingMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 18, 1),
    _HpSwitchMeshMulticastAgingMode_Type()
)
hpSwitchMeshMulticastAgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMeshMulticastAgingMode.setStatus("deprecated")


class _HpSwitchMeshBackwardCompatibility_Type(Integer32):
    """Custom type hpSwitchMeshBackwardCompatibility based on Integer32"""
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


_HpSwitchMeshBackwardCompatibility_Type.__name__ = "Integer32"
_HpSwitchMeshBackwardCompatibility_Object = MibScalar
hpSwitchMeshBackwardCompatibility = _HpSwitchMeshBackwardCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 18, 2),
    _HpSwitchMeshBackwardCompatibility_Type()
)
hpSwitchMeshBackwardCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMeshBackwardCompatibility.setStatus("mandatory")


class _HpSwitchMeshConfiguredId_Type(Integer32):
    """Custom type hpSwitchMeshConfiguredId based on Integer32"""
    defaultValue = 0


_HpSwitchMeshConfiguredId_Object = MibScalar
hpSwitchMeshConfiguredId = _HpSwitchMeshConfiguredId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 18, 3),
    _HpSwitchMeshConfiguredId_Type()
)
hpSwitchMeshConfiguredId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMeshConfiguredId.setStatus("mandatory")
_HpSwitchMeshActualId_Type = Integer32
_HpSwitchMeshActualId_Object = MibScalar
hpSwitchMeshActualId = _HpSwitchMeshActualId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 18, 4),
    _HpSwitchMeshActualId_Type()
)
hpSwitchMeshActualId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMeshActualId.setStatus("mandatory")
_HpSwitchPortIsolationConfig_ObjectIdentity = ObjectIdentity
hpSwitchPortIsolationConfig = _HpSwitchPortIsolationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 19)
)


class _HpSwitchPortIsolationMode_Type(Integer32):
    """Custom type hpSwitchPortIsolationMode based on Integer32"""
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


_HpSwitchPortIsolationMode_Type.__name__ = "Integer32"
_HpSwitchPortIsolationMode_Object = MibScalar
hpSwitchPortIsolationMode = _HpSwitchPortIsolationMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 19, 1),
    _HpSwitchPortIsolationMode_Type()
)
hpSwitchPortIsolationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortIsolationMode.setStatus("mandatory")
_HpSwitchPortIsolationConfigTable_Object = MibTable
hpSwitchPortIsolationConfigTable = _HpSwitchPortIsolationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 19, 2)
)
if mibBuilder.loadTexts:
    hpSwitchPortIsolationConfigTable.setStatus("mandatory")
_HpSwitchPortIsolationConfigEntry_Object = MibTableRow
hpSwitchPortIsolationConfigEntry = _HpSwitchPortIsolationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 19, 2, 1)
)
hpSwitchPortIsolationConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchPortIsolationPort"),
)
if mibBuilder.loadTexts:
    hpSwitchPortIsolationConfigEntry.setStatus("mandatory")


class _HpSwitchPortIsolationPort_Type(Integer32):
    """Custom type hpSwitchPortIsolationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchPortIsolationPort_Type.__name__ = "Integer32"
_HpSwitchPortIsolationPort_Object = MibTableColumn
hpSwitchPortIsolationPort = _HpSwitchPortIsolationPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 19, 2, 1, 1),
    _HpSwitchPortIsolationPort_Type()
)
hpSwitchPortIsolationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchPortIsolationPort.setStatus("mandatory")


class _HpSwitchPortIsolationPortMode_Type(Integer32):
    """Custom type hpSwitchPortIsolationPortMode based on Integer32"""
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
        *(("group1", 5),
          ("group2", 6),
          ("local", 4),
          ("private", 3),
          ("public", 2),
          ("uplink", 1))
    )


_HpSwitchPortIsolationPortMode_Type.__name__ = "Integer32"
_HpSwitchPortIsolationPortMode_Object = MibTableColumn
hpSwitchPortIsolationPortMode = _HpSwitchPortIsolationPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 19, 2, 1, 2),
    _HpSwitchPortIsolationPortMode_Type()
)
hpSwitchPortIsolationPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPortIsolationPortMode.setStatus("mandatory")
_HpSwitchSshConfig_ObjectIdentity = ObjectIdentity
hpSwitchSshConfig = _HpSwitchSshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20)
)


class _HpSwitchSshAdminStatus_Type(Integer32):
    """Custom type hpSwitchSshAdminStatus based on Integer32"""
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


_HpSwitchSshAdminStatus_Type.__name__ = "Integer32"
_HpSwitchSshAdminStatus_Object = MibScalar
hpSwitchSshAdminStatus = _HpSwitchSshAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 1),
    _HpSwitchSshAdminStatus_Type()
)
hpSwitchSshAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshAdminStatus.setStatus("mandatory")


class _HpSwitchSshVersion_Type(Integer32):
    """Custom type hpSwitchSshVersion based on Integer32"""
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
        *(("version1", 1),
          ("version1or2", 3),
          ("version2", 2))
    )


_HpSwitchSshVersion_Type.__name__ = "Integer32"
_HpSwitchSshVersion_Object = MibScalar
hpSwitchSshVersion = _HpSwitchSshVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 2),
    _HpSwitchSshVersion_Type()
)
hpSwitchSshVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshVersion.setStatus("mandatory")


class _HpSwitchSshTimeout_Type(Timeout):
    """Custom type hpSwitchSshTimeout based on Timeout"""
    defaultValue = 120

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_HpSwitchSshTimeout_Type.__name__ = "Timeout"
_HpSwitchSshTimeout_Object = MibScalar
hpSwitchSshTimeout = _HpSwitchSshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 3),
    _HpSwitchSshTimeout_Type()
)
hpSwitchSshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshTimeout.setStatus("mandatory")


class _HpSwitchSshPortNumber_Type(Integer32):
    """Custom type hpSwitchSshPortNumber based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchSshPortNumber_Type.__name__ = "Integer32"
_HpSwitchSshPortNumber_Object = MibScalar
hpSwitchSshPortNumber = _HpSwitchSshPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 4),
    _HpSwitchSshPortNumber_Type()
)
hpSwitchSshPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshPortNumber.setStatus("mandatory")


class _HpSwitchSshServerKeySize_Type(Integer32):
    """Custom type hpSwitchSshServerKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits1024", 3),
          ("bits512", 1),
          ("bits768", 2))
    )


_HpSwitchSshServerKeySize_Type.__name__ = "Integer32"
_HpSwitchSshServerKeySize_Object = MibScalar
hpSwitchSshServerKeySize = _HpSwitchSshServerKeySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 5),
    _HpSwitchSshServerKeySize_Type()
)
hpSwitchSshServerKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshServerKeySize.setStatus("mandatory")


class _HpSwitchSshFileServerAdminStatus_Type(Integer32):
    """Custom type hpSwitchSshFileServerAdminStatus based on Integer32"""
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


_HpSwitchSshFileServerAdminStatus_Type.__name__ = "Integer32"
_HpSwitchSshFileServerAdminStatus_Object = MibScalar
hpSwitchSshFileServerAdminStatus = _HpSwitchSshFileServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 6),
    _HpSwitchSshFileServerAdminStatus_Type()
)
hpSwitchSshFileServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshFileServerAdminStatus.setStatus("mandatory")


class _HpSwitchSshIpVersion_Type(Integer32):
    """Custom type hpSwitchSshIpVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv4or6", 3),
          ("ipv6", 2))
    )


_HpSwitchSshIpVersion_Type.__name__ = "Integer32"
_HpSwitchSshIpVersion_Object = MibScalar
hpSwitchSshIpVersion = _HpSwitchSshIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 7),
    _HpSwitchSshIpVersion_Type()
)
hpSwitchSshIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshIpVersion.setStatus("deprecated")


class _HpSwitchSshReKeyStatus_Type(TruthValue):
    """Custom type hpSwitchSshReKeyStatus based on TruthValue"""


_HpSwitchSshReKeyStatus_Object = MibScalar
hpSwitchSshReKeyStatus = _HpSwitchSshReKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 8),
    _HpSwitchSshReKeyStatus_Type()
)
hpSwitchSshReKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshReKeyStatus.setStatus("mandatory")


class _HpSwitchSshReKeyTime_Type(Integer32):
    """Custom type hpSwitchSshReKeyTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_HpSwitchSshReKeyTime_Type.__name__ = "Integer32"
_HpSwitchSshReKeyTime_Object = MibScalar
hpSwitchSshReKeyTime = _HpSwitchSshReKeyTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 9),
    _HpSwitchSshReKeyTime_Type()
)
hpSwitchSshReKeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshReKeyTime.setStatus("mandatory")


class _HpSwitchSshReKeyVolume_Type(Integer32):
    """Custom type hpSwitchSshReKeyVolume based on Integer32"""
    defaultValue = 1048576

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1048576),
    )


_HpSwitchSshReKeyVolume_Type.__name__ = "Integer32"
_HpSwitchSshReKeyVolume_Object = MibScalar
hpSwitchSshReKeyVolume = _HpSwitchSshReKeyVolume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 20, 10),
    _HpSwitchSshReKeyVolume_Type()
)
hpSwitchSshReKeyVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSshReKeyVolume.setStatus("mandatory")
_HpSwitchPendingConfig_ObjectIdentity = ObjectIdentity
hpSwitchPendingConfig = _HpSwitchPendingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 21)
)


class _HpSwitchPendingConfigControl_Type(Integer32):
    """Custom type hpSwitchPendingConfigControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applyMstp", 1),
          ("noAction", 3),
          ("resetMstp", 2))
    )


_HpSwitchPendingConfigControl_Type.__name__ = "Integer32"
_HpSwitchPendingConfigControl_Object = MibScalar
hpSwitchPendingConfigControl = _HpSwitchPendingConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 21, 1),
    _HpSwitchPendingConfigControl_Type()
)
hpSwitchPendingConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchPendingConfigControl.setStatus("mandatory")
_HpSwitchBWMinConfig_ObjectIdentity = ObjectIdentity
hpSwitchBWMinConfig = _HpSwitchBWMinConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22)
)
_HpSwitchBWMinEgressPortConfigTable_Object = MibTable
hpSwitchBWMinEgressPortConfigTable = _HpSwitchBWMinEgressPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22, 1)
)
if mibBuilder.loadTexts:
    hpSwitchBWMinEgressPortConfigTable.setStatus("deprecated")
_HpSwitchBWMinEgressPortConfigEntry_Object = MibTableRow
hpSwitchBWMinEgressPortConfigEntry = _HpSwitchBWMinEgressPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22, 1, 1)
)
hpSwitchBWMinEgressPortConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchBWMinEgressPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchBWMinEgressPortConfigEntry.setStatus("deprecated")


class _HpSwitchBWMinEgressPortIndex_Type(Integer32):
    """Custom type hpSwitchBWMinEgressPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchBWMinEgressPortIndex_Type.__name__ = "Integer32"
_HpSwitchBWMinEgressPortIndex_Object = MibTableColumn
hpSwitchBWMinEgressPortIndex = _HpSwitchBWMinEgressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22, 1, 1, 1),
    _HpSwitchBWMinEgressPortIndex_Type()
)
hpSwitchBWMinEgressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchBWMinEgressPortIndex.setStatus("deprecated")


class _HpSwitchBWMinEgressPortPrctLowPriority_Type(Integer32):
    """Custom type hpSwitchBWMinEgressPortPrctLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchBWMinEgressPortPrctLowPriority_Type.__name__ = "Integer32"
_HpSwitchBWMinEgressPortPrctLowPriority_Object = MibTableColumn
hpSwitchBWMinEgressPortPrctLowPriority = _HpSwitchBWMinEgressPortPrctLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22, 1, 1, 2),
    _HpSwitchBWMinEgressPortPrctLowPriority_Type()
)
hpSwitchBWMinEgressPortPrctLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchBWMinEgressPortPrctLowPriority.setStatus("deprecated")


class _HpSwitchBWMinEgressPortPrctNormalPriority_Type(Integer32):
    """Custom type hpSwitchBWMinEgressPortPrctNormalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchBWMinEgressPortPrctNormalPriority_Type.__name__ = "Integer32"
_HpSwitchBWMinEgressPortPrctNormalPriority_Object = MibTableColumn
hpSwitchBWMinEgressPortPrctNormalPriority = _HpSwitchBWMinEgressPortPrctNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22, 1, 1, 3),
    _HpSwitchBWMinEgressPortPrctNormalPriority_Type()
)
hpSwitchBWMinEgressPortPrctNormalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchBWMinEgressPortPrctNormalPriority.setStatus("deprecated")


class _HpSwitchBWMinEgressPortPrctMedPriority_Type(Integer32):
    """Custom type hpSwitchBWMinEgressPortPrctMedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchBWMinEgressPortPrctMedPriority_Type.__name__ = "Integer32"
_HpSwitchBWMinEgressPortPrctMedPriority_Object = MibTableColumn
hpSwitchBWMinEgressPortPrctMedPriority = _HpSwitchBWMinEgressPortPrctMedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22, 1, 1, 4),
    _HpSwitchBWMinEgressPortPrctMedPriority_Type()
)
hpSwitchBWMinEgressPortPrctMedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchBWMinEgressPortPrctMedPriority.setStatus("deprecated")


class _HpSwitchBWMinEgressPortPrctHighPriority_Type(Integer32):
    """Custom type hpSwitchBWMinEgressPortPrctHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchBWMinEgressPortPrctHighPriority_Type.__name__ = "Integer32"
_HpSwitchBWMinEgressPortPrctHighPriority_Object = MibTableColumn
hpSwitchBWMinEgressPortPrctHighPriority = _HpSwitchBWMinEgressPortPrctHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 22, 1, 1, 5),
    _HpSwitchBWMinEgressPortPrctHighPriority_Type()
)
hpSwitchBWMinEgressPortPrctHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchBWMinEgressPortPrctHighPriority.setStatus("deprecated")
_HpSwitchRateLimitPortConfig_ObjectIdentity = ObjectIdentity
hpSwitchRateLimitPortConfig = _HpSwitchRateLimitPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23)
)
_HpSwitchRateLimitPortConfigTable_Object = MibTable
hpSwitchRateLimitPortConfigTable = _HpSwitchRateLimitPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1)
)
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortConfigTable.setStatus("mandatory")
_HpSwitchRateLimitPortConfigEntry_Object = MibTableRow
hpSwitchRateLimitPortConfigEntry = _HpSwitchRateLimitPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1)
)
hpSwitchRateLimitPortConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchRateLimitPortIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortConfigEntry.setStatus("mandatory")


class _HpSwitchRateLimitPortIndex_Type(Integer32):
    """Custom type hpSwitchRateLimitPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchRateLimitPortIndex_Type.__name__ = "Integer32"
_HpSwitchRateLimitPortIndex_Object = MibTableColumn
hpSwitchRateLimitPortIndex = _HpSwitchRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1, 1),
    _HpSwitchRateLimitPortIndex_Type()
)
hpSwitchRateLimitPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortIndex.setStatus("mandatory")


class _HpSwitchRateLimitPortControlMode_Type(Integer32):
    """Custom type hpSwitchRateLimitPortControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("rateLimitPerPortOnly", 2),
          ("rateLimitPerQueue", 3))
    )


_HpSwitchRateLimitPortControlMode_Type.__name__ = "Integer32"
_HpSwitchRateLimitPortControlMode_Object = MibTableColumn
hpSwitchRateLimitPortControlMode = _HpSwitchRateLimitPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1, 2),
    _HpSwitchRateLimitPortControlMode_Type()
)
hpSwitchRateLimitPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortControlMode.setStatus("mandatory")


class _HpSwitchRateLimitPortSingleControlPrct_Type(Integer32):
    """Custom type hpSwitchRateLimitPortSingleControlPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchRateLimitPortSingleControlPrct_Type.__name__ = "Integer32"
_HpSwitchRateLimitPortSingleControlPrct_Object = MibTableColumn
hpSwitchRateLimitPortSingleControlPrct = _HpSwitchRateLimitPortSingleControlPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1, 3),
    _HpSwitchRateLimitPortSingleControlPrct_Type()
)
hpSwitchRateLimitPortSingleControlPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortSingleControlPrct.setStatus("mandatory")


class _HpSwitchRateLimitPortPrctLowPriority_Type(Integer32):
    """Custom type hpSwitchRateLimitPortPrctLowPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchRateLimitPortPrctLowPriority_Type.__name__ = "Integer32"
_HpSwitchRateLimitPortPrctLowPriority_Object = MibTableColumn
hpSwitchRateLimitPortPrctLowPriority = _HpSwitchRateLimitPortPrctLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1, 4),
    _HpSwitchRateLimitPortPrctLowPriority_Type()
)
hpSwitchRateLimitPortPrctLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortPrctLowPriority.setStatus("mandatory")


class _HpSwitchRateLimitPortPrctNormalPriority_Type(Integer32):
    """Custom type hpSwitchRateLimitPortPrctNormalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchRateLimitPortPrctNormalPriority_Type.__name__ = "Integer32"
_HpSwitchRateLimitPortPrctNormalPriority_Object = MibTableColumn
hpSwitchRateLimitPortPrctNormalPriority = _HpSwitchRateLimitPortPrctNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1, 5),
    _HpSwitchRateLimitPortPrctNormalPriority_Type()
)
hpSwitchRateLimitPortPrctNormalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortPrctNormalPriority.setStatus("mandatory")


class _HpSwitchRateLimitPortPrctMedPriority_Type(Integer32):
    """Custom type hpSwitchRateLimitPortPrctMedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchRateLimitPortPrctMedPriority_Type.__name__ = "Integer32"
_HpSwitchRateLimitPortPrctMedPriority_Object = MibTableColumn
hpSwitchRateLimitPortPrctMedPriority = _HpSwitchRateLimitPortPrctMedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1, 6),
    _HpSwitchRateLimitPortPrctMedPriority_Type()
)
hpSwitchRateLimitPortPrctMedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortPrctMedPriority.setStatus("mandatory")


class _HpSwitchRateLimitPortPrctHighPriority_Type(Integer32):
    """Custom type hpSwitchRateLimitPortPrctHighPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpSwitchRateLimitPortPrctHighPriority_Type.__name__ = "Integer32"
_HpSwitchRateLimitPortPrctHighPriority_Object = MibTableColumn
hpSwitchRateLimitPortPrctHighPriority = _HpSwitchRateLimitPortPrctHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 23, 1, 1, 7),
    _HpSwitchRateLimitPortPrctHighPriority_Type()
)
hpSwitchRateLimitPortPrctHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRateLimitPortPrctHighPriority.setStatus("mandatory")
_HpSwitchQosPassThroughMode_ObjectIdentity = ObjectIdentity
hpSwitchQosPassThroughMode = _HpSwitchQosPassThroughMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 24)
)


class _HpSwitchQosPassThroughModeConfig_Type(Integer32):
    """Custom type hpSwitchQosPassThroughModeConfig based on Integer32"""
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
        *(("balanced", 3),
          ("onequeue", 4),
          ("optimized", 1),
          ("typical", 2))
    )


_HpSwitchQosPassThroughModeConfig_Type.__name__ = "Integer32"
_HpSwitchQosPassThroughModeConfig_Object = MibScalar
hpSwitchQosPassThroughModeConfig = _HpSwitchQosPassThroughModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 24, 1),
    _HpSwitchQosPassThroughModeConfig_Type()
)
hpSwitchQosPassThroughModeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchQosPassThroughModeConfig.setStatus("mandatory")
_HpSwitchReboot_ObjectIdentity = ObjectIdentity
hpSwitchReboot = _HpSwitchReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 25)
)


class _HpSwitchRebootConfig_Type(Integer32):
    """Custom type hpSwitchRebootConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HpSwitchRebootConfig_Type.__name__ = "Integer32"
_HpSwitchRebootConfig_Object = MibScalar
hpSwitchRebootConfig = _HpSwitchRebootConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 25, 1),
    _HpSwitchRebootConfig_Type()
)
hpSwitchRebootConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRebootConfig.setStatus("mandatory")


class _HpSwitchRebootFastBoot_Type(Integer32):
    """Custom type hpSwitchRebootFastBoot based on Integer32"""
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


_HpSwitchRebootFastBoot_Type.__name__ = "Integer32"
_HpSwitchRebootFastBoot_Object = MibScalar
hpSwitchRebootFastBoot = _HpSwitchRebootFastBoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 25, 2),
    _HpSwitchRebootFastBoot_Type()
)
hpSwitchRebootFastBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRebootFastBoot.setStatus("mandatory")
_HpSwitchProtectedPortsConfig_ObjectIdentity = ObjectIdentity
hpSwitchProtectedPortsConfig = _HpSwitchProtectedPortsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 26)
)
_HpSwitchProtectedPortsMask_Type = OctetString
_HpSwitchProtectedPortsMask_Object = MibScalar
hpSwitchProtectedPortsMask = _HpSwitchProtectedPortsMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 26, 1),
    _HpSwitchProtectedPortsMask_Type()
)
hpSwitchProtectedPortsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchProtectedPortsMask.setStatus("mandatory")
_HpSwitchLACPConfig_ObjectIdentity = ObjectIdentity
hpSwitchLACPConfig = _HpSwitchLACPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 28)
)


class _HpSwitchLACPAllPortsStatus_Type(Integer32):
    """Custom type hpSwitchLACPAllPortsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 1),
          ("passive", 3))
    )


_HpSwitchLACPAllPortsStatus_Type.__name__ = "Integer32"
_HpSwitchLACPAllPortsStatus_Object = MibScalar
hpSwitchLACPAllPortsStatus = _HpSwitchLACPAllPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 28, 1),
    _HpSwitchLACPAllPortsStatus_Type()
)
hpSwitchLACPAllPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchLACPAllPortsStatus.setStatus("mandatory")
_HpSwitchDSCPRateLimitConfig_ObjectIdentity = ObjectIdentity
hpSwitchDSCPRateLimitConfig = _HpSwitchDSCPRateLimitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 31)
)
_HpSwitchDSCPRateLimitConfigTable_Object = MibTable
hpSwitchDSCPRateLimitConfigTable = _HpSwitchDSCPRateLimitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 31, 1)
)
if mibBuilder.loadTexts:
    hpSwitchDSCPRateLimitConfigTable.setStatus("mandatory")
_HpSwitchDSCPRateLimitConfigEntry_Object = MibTableRow
hpSwitchDSCPRateLimitConfigEntry = _HpSwitchDSCPRateLimitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 31, 1, 1)
)
hpSwitchDSCPRateLimitConfigEntry.setIndexNames(
    (0, "CONFIG-MIB", "hpSwitchDSCPRateLimitIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchDSCPRateLimitConfigEntry.setStatus("mandatory")
_HpSwitchDSCPRateLimitIndex_Type = Dscp
_HpSwitchDSCPRateLimitIndex_Object = MibTableColumn
hpSwitchDSCPRateLimitIndex = _HpSwitchDSCPRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 31, 1, 1, 1),
    _HpSwitchDSCPRateLimitIndex_Type()
)
hpSwitchDSCPRateLimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchDSCPRateLimitIndex.setStatus("mandatory")


class _HpSwitchDSCPRateLimitKbps_Type(Integer32):
    """Custom type hpSwitchDSCPRateLimitKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000000),
    )


_HpSwitchDSCPRateLimitKbps_Type.__name__ = "Integer32"
_HpSwitchDSCPRateLimitKbps_Object = MibTableColumn
hpSwitchDSCPRateLimitKbps = _HpSwitchDSCPRateLimitKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 31, 1, 1, 2),
    _HpSwitchDSCPRateLimitKbps_Type()
)
hpSwitchDSCPRateLimitKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDSCPRateLimitKbps.setStatus("mandatory")
_HpSwitchDSCPRateLimitPorts_Type = PortList
_HpSwitchDSCPRateLimitPorts_Object = MibTableColumn
hpSwitchDSCPRateLimitPorts = _HpSwitchDSCPRateLimitPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 31, 1, 1, 3),
    _HpSwitchDSCPRateLimitPorts_Type()
)
hpSwitchDSCPRateLimitPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDSCPRateLimitPorts.setStatus("mandatory")
_HpSwitchTcpPushPreserve_ObjectIdentity = ObjectIdentity
hpSwitchTcpPushPreserve = _HpSwitchTcpPushPreserve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 33)
)


class _HpSwitchTcpPushPreserveConfig_Type(Integer32):
    """Custom type hpSwitchTcpPushPreserveConfig based on Integer32"""
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


_HpSwitchTcpPushPreserveConfig_Type.__name__ = "Integer32"
_HpSwitchTcpPushPreserveConfig_Object = MibScalar
hpSwitchTcpPushPreserveConfig = _HpSwitchTcpPushPreserveConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 33, 1),
    _HpSwitchTcpPushPreserveConfig_Type()
)
hpSwitchTcpPushPreserveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTcpPushPreserveConfig.setStatus("mandatory")
_HpSwitchIfMau_ObjectIdentity = ObjectIdentity
hpSwitchIfMau = _HpSwitchIfMau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 34)
)
_HpSwitchIfMauTypeListBits_Type = HpSwitchIfMauTypeListBits
_HpSwitchIfMauTypeListBits_Object = MibScalar
hpSwitchIfMauTypeListBits = _HpSwitchIfMauTypeListBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 34, 1),
    _HpSwitchIfMauTypeListBits_Type()
)
hpSwitchIfMauTypeListBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIfMauTypeListBits.setStatus("mandatory")
_HpSwitchIfMauAutoNegCapabilityBits_Type = HpSwitchIfMauAutoNegCapabilityBits
_HpSwitchIfMauAutoNegCapabilityBits_Object = MibScalar
hpSwitchIfMauAutoNegCapabilityBits = _HpSwitchIfMauAutoNegCapabilityBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 34, 2),
    _HpSwitchIfMauAutoNegCapabilityBits_Type()
)
hpSwitchIfMauAutoNegCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIfMauAutoNegCapabilityBits.setStatus("mandatory")
_HpSwitchIfMauAutoNegCapAdvertisedBits_Type = HpSwitchIfMauAutoNegCapAdvertisedBits
_HpSwitchIfMauAutoNegCapAdvertisedBits_Object = MibScalar
hpSwitchIfMauAutoNegCapAdvertisedBits = _HpSwitchIfMauAutoNegCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 34, 3),
    _HpSwitchIfMauAutoNegCapAdvertisedBits_Type()
)
hpSwitchIfMauAutoNegCapAdvertisedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIfMauAutoNegCapAdvertisedBits.setStatus("mandatory")
_HpSwitchIfMauAutoNegCapReceivedBits_Type = HpSwitchIfMauAutoNegCapReceivedBits
_HpSwitchIfMauAutoNegCapReceivedBits_Object = MibScalar
hpSwitchIfMauAutoNegCapReceivedBits = _HpSwitchIfMauAutoNegCapReceivedBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 34, 4),
    _HpSwitchIfMauAutoNegCapReceivedBits_Type()
)
hpSwitchIfMauAutoNegCapReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchIfMauAutoNegCapReceivedBits.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hpSwitchStpErrantBpduReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 0, 0, 1)
)
hpSwitchStpErrantBpduReceived.setObjects(
      *(("CONFIG-MIB", "hpSwitchStpPort"),
        ("CONFIG-MIB", "hpSwitchStpPortErrantBpduCounter"),
        ("BRIDGE-MIB", "dot1dStpPortState"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedBridge"),
        ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"),
        ("CONFIG-MIB", "hpSwitchStpErrantBpduSrcMac"),
        ("CONFIG-MIB", "hpSwitchStpErrantBpduDetector"))
)
if mibBuilder.loadTexts:
    hpSwitchStpErrantBpduReceived.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONFIG-MIB",
    **{"VlanID": VlanID,
       "Timeout": Timeout,
       "HpicfUsrProfilePortSpeed": HpicfUsrProfilePortSpeed,
       "hpConfig": hpConfig,
       "hpSwitchConfig": hpSwitchConfig,
       "hpSwitchTraps": hpSwitchTraps,
       "hpSwitchStpErrantBpduReceived": hpSwitchStpErrantBpduReceived,
       "hpSwitchTrapsObjects": hpSwitchTrapsObjects,
       "hpSwitchStpErrantBpduDetector": hpSwitchStpErrantBpduDetector,
       "hpSwitchStpErrantBpduSrcMac": hpSwitchStpErrantBpduSrcMac,
       "hpSwitchSystemConfig": hpSwitchSystemConfig,
       "hpSwitchAutoReboot": hpSwitchAutoReboot,
       "hpSwitchTimeZone": hpSwitchTimeZone,
       "hpSwitchDaylightTimeRule": hpSwitchDaylightTimeRule,
       "hpSwitchDaylightBeginningMonth": hpSwitchDaylightBeginningMonth,
       "hpSwitchDaylightBeginningDay": hpSwitchDaylightBeginningDay,
       "hpSwitchDaylightEndingMonth": hpSwitchDaylightEndingMonth,
       "hpSwitchDaylightEndingDay": hpSwitchDaylightEndingDay,
       "hpSwitchSystemConfigStatus": hpSwitchSystemConfigStatus,
       "hpSwitchSystemPortLEDMode": hpSwitchSystemPortLEDMode,
       "hpSwitchControlUnknownIPMulticast": hpSwitchControlUnknownIPMulticast,
       "hpSwitchIgmpDelayedGroupFlushTimer": hpSwitchIgmpDelayedGroupFlushTimer,
       "hpSwitchMaxFrameSize": hpSwitchMaxFrameSize,
       "hpSwitchIpMTU": hpSwitchIpMTU,
       "hpSwitchAllowV1Modules": hpSwitchAllowV1Modules,
       "hpSwitchAllowV2Modules": hpSwitchAllowV2Modules,
       "hpicfPrivateVlanPromiscuousPorts": hpicfPrivateVlanPromiscuousPorts,
       "hpSwitchPreviewMode": hpSwitchPreviewMode,
       "hpSwitchHibernate": hpSwitchHibernate,
       "hpSwitchMacDelimiter": hpSwitchMacDelimiter,
       "hpicfSwitchCLIOptimization": hpicfSwitchCLIOptimization,
       "hpSwitchConsoleConfig": hpSwitchConsoleConfig,
       "hpSwitchTelnetAdminStatus": hpSwitchTelnetAdminStatus,
       "hpSwitchTerminalType": hpSwitchTerminalType,
       "hpSwitchConsoleRefRate": hpSwitchConsoleRefRate,
       "hpSwitchDisplayedEvent": hpSwitchDisplayedEvent,
       "hpSwitchConsoleConfigStatus": hpSwitchConsoleConfigStatus,
       "hpSwitchConsoleConfigLogoutPrompt": hpSwitchConsoleConfigLogoutPrompt,
       "hpSwitchUsbConsoleAdminStatus": hpSwitchUsbConsoleAdminStatus,
       "hpSwitchSessionGlobalIdleTimeout": hpSwitchSessionGlobalIdleTimeout,
       "hpSwitchSessionConsoleIdleTimeout": hpSwitchSessionConsoleIdleTimeout,
       "hpSwitchMaxSessions": hpSwitchMaxSessions,
       "hpSwitchMaxUserSessions": hpSwitchMaxUserSessions,
       "hpSwitchPortConfig": hpSwitchPortConfig,
       "hpSwitchPortTable": hpSwitchPortTable,
       "hpSwitchPortEntry": hpSwitchPortEntry,
       "hpSwitchPortIndex": hpSwitchPortIndex,
       "hpSwitchPortType": hpSwitchPortType,
       "hpSwitchPortDescr": hpSwitchPortDescr,
       "hpSwitchPortAdminStatus": hpSwitchPortAdminStatus,
       "hpSwitchPortEtherMode": hpSwitchPortEtherMode,
       "hpSwitchPortVgMode": hpSwitchPortVgMode,
       "hpSwitchPortLinkbeat": hpSwitchPortLinkbeat,
       "hpSwitchPortTrunkGroup": hpSwitchPortTrunkGroup,
       "hpSwitchPortBcastLimit": hpSwitchPortBcastLimit,
       "hpSwitchPortFastEtherMode": hpSwitchPortFastEtherMode,
       "hpSwitchPortFlowControl": hpSwitchPortFlowControl,
       "hpSwitchPortTrunkType": hpSwitchPortTrunkType,
       "hpSwitchPortTrunkLACPStatus": hpSwitchPortTrunkLACPStatus,
       "hpSwitchPortMDIXStatus": hpSwitchPortMDIXStatus,
       "hpSwitchPortAutoMDIX": hpSwitchPortAutoMDIX,
       "hpSwitchPortLACPKey": hpSwitchPortLACPKey,
       "hpSwitchPortTrafficTemplateName": hpSwitchPortTrafficTemplateName,
       "hpSwitchPortEEEAdminStatus": hpSwitchPortEEEAdminStatus,
       "hpSwitchPortEEEOperStatus": hpSwitchPortEEEOperStatus,
       "hpSwitchPortEEECurrentTwSysTx": hpSwitchPortEEECurrentTwSysTx,
       "hpSwitchPortEEEMinTwSysTx": hpSwitchPortEEEMinTwSysTx,
       "hpSwitchPortEEEMaxTwSysTx": hpSwitchPortEEEMaxTwSysTx,
       "hpSwitchPortPvid": hpSwitchPortPvid,
       "hpSwitchPortTaggedVlanMap1k": hpSwitchPortTaggedVlanMap1k,
       "hpSwitchPortTaggedVlanMap2k": hpSwitchPortTaggedVlanMap2k,
       "hpSwitchPortTaggedVlanMap3k": hpSwitchPortTaggedVlanMap3k,
       "hpSwitchPortTaggedVlanMap4k": hpSwitchPortTaggedVlanMap4k,
       "hpSwitchPortEEECurrentTwSysTx1": hpSwitchPortEEECurrentTwSysTx1,
       "hpSwitchPortEEEMinTwSysTx1": hpSwitchPortEEEMinTwSysTx1,
       "hpSwitchPortEEEMaxTwSysTx1": hpSwitchPortEEEMaxTwSysTx1,
       "hpSwitchPortPtpAdminStatus": hpSwitchPortPtpAdminStatus,
       "hpSwitchPortPtpOperStatus": hpSwitchPortPtpOperStatus,
       "hpSwitchPortPtpRxCount": hpSwitchPortPtpRxCount,
       "hpSwitchPortPtpTxCount": hpSwitchPortPtpTxCount,
       "hpSwitchPortNetworkDevice": hpSwitchPortNetworkDevice,
       "hpSwitchPortConfigStatus": hpSwitchPortConfigStatus,
       "hpSwitchLinkUpDownTrapAllPortsStatus": hpSwitchLinkUpDownTrapAllPortsStatus,
       "hpSwitchIpxConfig": hpSwitchIpxConfig,
       "hpSwitchIpxConfigStatus": hpSwitchIpxConfigStatus,
       "hpSwitchIpConfig": hpSwitchIpConfig,
       "hpSwitchIpTimepAdminStatus": hpSwitchIpTimepAdminStatus,
       "hpSwitchIpTimepServerAddr": hpSwitchIpTimepServerAddr,
       "hpSwitchIpTimepPollInterval": hpSwitchIpTimepPollInterval,
       "hpSwitchIpConfigStatus": hpSwitchIpConfigStatus,
       "hpSwitchIpTftpMode": hpSwitchIpTftpMode,
       "hpSwitchIpTimepInetServerAddrType": hpSwitchIpTimepInetServerAddrType,
       "hpSwitchIpTimepInetServerAddr": hpSwitchIpTimepInetServerAddr,
       "hpSwitchIpTimepIsOobm": hpSwitchIpTimepIsOobm,
       "hpSwitchSerialLinkConfig": hpSwitchSerialLinkConfig,
       "hpSwitchSLinkBaudRate": hpSwitchSLinkBaudRate,
       "hpSwitchSLinkFlowCtrl": hpSwitchSLinkFlowCtrl,
       "hpSwitchSLinkConnInactTime": hpSwitchSLinkConnInactTime,
       "hpSwitchSLinkModemConnTime": hpSwitchSLinkModemConnTime,
       "hpSwitchSLinkModemLostRecvTime": hpSwitchSLinkModemLostRecvTime,
       "hpSwitchSLinkModemDisConnTime": hpSwitchSLinkModemDisConnTime,
       "hpSwitchSLinkParity": hpSwitchSLinkParity,
       "hpSwitchSLinkCharBits": hpSwitchSLinkCharBits,
       "hpSwitchSLinkStopBits": hpSwitchSLinkStopBits,
       "hpSwitchSLinkConfigStatus": hpSwitchSLinkConfigStatus,
       "hpSwitchFilterConfig": hpSwitchFilterConfig,
       "hpSwitchFilterConfigTable": hpSwitchFilterConfigTable,
       "hpSwitchFilterConfigEntry": hpSwitchFilterConfigEntry,
       "hpSwitchFilterIndex": hpSwitchFilterIndex,
       "hpSwitchFilterType": hpSwitchFilterType,
       "hpSwitchFilterSrcPort": hpSwitchFilterSrcPort,
       "hpSwitchFilterMacAddr": hpSwitchFilterMacAddr,
       "hpSwitchFilterProtocolType": hpSwitchFilterProtocolType,
       "hpSwitchFilterPortMask": hpSwitchFilterPortMask,
       "hpSwitchFilterEntryStatus": hpSwitchFilterEntryStatus,
       "hpSwitchFilterName": hpSwitchFilterName,
       "hpSwitchProbeConfig": hpSwitchProbeConfig,
       "hpSwitchProbeType": hpSwitchProbeType,
       "hpSwitchProbedVlanId": hpSwitchProbedVlanId,
       "hpSwitchProbePort": hpSwitchProbePort,
       "hpSwitchProbeAdminStatus": hpSwitchProbeAdminStatus,
       "hpSwitchProbedPortMask": hpSwitchProbedPortMask,
       "hpSwitchFddiIpFragConfig": hpSwitchFddiIpFragConfig,
       "hpSwitchFddiIpFragConfigTable": hpSwitchFddiIpFragConfigTable,
       "hpSwitchFddiIpFragConfigEntry": hpSwitchFddiIpFragConfigEntry,
       "hpSwitchFddiIpFragConfigIndex": hpSwitchFddiIpFragConfigIndex,
       "hpSwitchFddiIpFragConfigStatus": hpSwitchFddiIpFragConfigStatus,
       "hpSwitchABCConfig": hpSwitchABCConfig,
       "hpSwitchABCConfigTable": hpSwitchABCConfigTable,
       "hpSwitchABCConfigEntry": hpSwitchABCConfigEntry,
       "hpSwitchABCConfigVlan": hpSwitchABCConfigVlan,
       "hpSwitchABCConfigControl": hpSwitchABCConfigControl,
       "hpSwitchABCConfigIpRipControl": hpSwitchABCConfigIpRipControl,
       "hpSwitchABCConfigIpxRipSapControl": hpSwitchABCConfigIpxRipSapControl,
       "hpSwitchABCConfigVlanBcastLimit": hpSwitchABCConfigVlanBcastLimit,
       "hpSwitchABCConfigAutoGatewayConfig": hpSwitchABCConfigAutoGatewayConfig,
       "hpSwitchStpConfig": hpSwitchStpConfig,
       "hpSwitchStpVlanTable": hpSwitchStpVlanTable,
       "hpSwitchStpVlanEntry": hpSwitchStpVlanEntry,
       "hpSwitchStpVlan": hpSwitchStpVlan,
       "hpSwitchStpAdminStatus": hpSwitchStpAdminStatus,
       "hpSwitchStpPriority": hpSwitchStpPriority,
       "hpSwitchStpMaxAge": hpSwitchStpMaxAge,
       "hpSwitchStpHelloTime": hpSwitchStpHelloTime,
       "hpSwitchStpForwardDelay": hpSwitchStpForwardDelay,
       "hpSwitchStpPortTable": hpSwitchStpPortTable,
       "hpSwitchStpPortEntry": hpSwitchStpPortEntry,
       "hpSwitchStpPort": hpSwitchStpPort,
       "hpSwitchStpPortType": hpSwitchStpPortType,
       "hpSwitchStpPortSrcMac": hpSwitchStpPortSrcMac,
       "hpSwitchStpPortPriority": hpSwitchStpPortPriority,
       "hpSwitchStpPortPathCost": hpSwitchStpPortPathCost,
       "hpSwitchStpPortMode": hpSwitchStpPortMode,
       "hpSwitchStpPortBpduFilter": hpSwitchStpPortBpduFilter,
       "hpSwitchStpPortBpduProtection": hpSwitchStpPortBpduProtection,
       "hpSwitchStpPortErrantBpduCounter": hpSwitchStpPortErrantBpduCounter,
       "hpSwitchStpPortPvstFilter": hpSwitchStpPortPvstFilter,
       "hpSwitchStpPortPvstProtection": hpSwitchStpPortPvstProtection,
       "hpSwitchStpTrapCntl": hpSwitchStpTrapCntl,
       "hpSwitchStpBpduProtectionTimeout": hpSwitchStpBpduProtectionTimeout,
       "hpSwitchSTPAdminStatus": hpSwitchSTPAdminStatus,
       "hpicfSwitchSTPVersion": hpicfSwitchSTPVersion,
       "hpSwitchIgmpConfig": hpSwitchIgmpConfig,
       "hpSwitchIgmpConfigTable": hpSwitchIgmpConfigTable,
       "hpSwitchIgmpConfigEntry": hpSwitchIgmpConfigEntry,
       "hpSwitchIgmpVlanIndex": hpSwitchIgmpVlanIndex,
       "hpSwitchIgmpState": hpSwitchIgmpState,
       "hpSwitchIgmpQuerierState": hpSwitchIgmpQuerierState,
       "hpSwitchIgmpPriorityState": hpSwitchIgmpPriorityState,
       "hpSwitchIgmpQuerierInterval": hpSwitchIgmpQuerierInterval,
       "hpSwitchIgmpProxyDomainMap": hpSwitchIgmpProxyDomainMap,
       "hpSwitchIgmpPortConfigTable": hpSwitchIgmpPortConfigTable,
       "hpSwitchIgmpPortConfigEntry": hpSwitchIgmpPortConfigEntry,
       "hpSwitchIgmpPortIndex": hpSwitchIgmpPortIndex,
       "hpSwitchIgmpPortType": hpSwitchIgmpPortType,
       "hpSwitchIgmpIpMcastState": hpSwitchIgmpIpMcastState,
       "hpSwitchIgmpPortConfigTable2": hpSwitchIgmpPortConfigTable2,
       "hpSwitchIgmpPortConfigEntry2": hpSwitchIgmpPortConfigEntry2,
       "hpSwitchIgmpPortVlanIndex2": hpSwitchIgmpPortVlanIndex2,
       "hpSwitchIgmpPortIndex2": hpSwitchIgmpPortIndex2,
       "hpSwitchIgmpPortType2": hpSwitchIgmpPortType2,
       "hpSwitchIgmpIpMcastState2": hpSwitchIgmpIpMcastState2,
       "hpSwitchIgmpPortForcedLeaveState": hpSwitchIgmpPortForcedLeaveState,
       "hpSwitchIgmpPortFastLeaveState": hpSwitchIgmpPortFastLeaveState,
       "hpSwitchIgmpForcedLeaveInterval": hpSwitchIgmpForcedLeaveInterval,
       "hpSwitchCosConfig": hpSwitchCosConfig,
       "hpSwitchCosPortConfigTable": hpSwitchCosPortConfigTable,
       "hpSwitchCosPortConfigEntry": hpSwitchCosPortConfigEntry,
       "hpSwitchCosPortIndex": hpSwitchCosPortIndex,
       "hpSwitchCosPortType": hpSwitchCosPortType,
       "hpSwitchCosPortPriority": hpSwitchCosPortPriority,
       "hpSwitchCosPortDSCPPolicy": hpSwitchCosPortDSCPPolicy,
       "hpSwitchCosPortResolvedPriority": hpSwitchCosPortResolvedPriority,
       "hpSwitchCosPortApplyPolicy": hpSwitchCosPortApplyPolicy,
       "hpSwitchCosPortTrustMode": hpSwitchCosPortTrustMode,
       "hpSwitchCosPortPartnerDevice": hpSwitchCosPortPartnerDevice,
       "hpSwitchCosPortTrustedPartnerState": hpSwitchCosPortTrustedPartnerState,
       "hpSwitchCosVlanConfigTable": hpSwitchCosVlanConfigTable,
       "hpSwitchCosVlanConfigEntry": hpSwitchCosVlanConfigEntry,
       "hpSwitchCosVlanIndex": hpSwitchCosVlanIndex,
       "hpSwitchCosVlanPriority": hpSwitchCosVlanPriority,
       "hpSwitchCosVlanDSCPPolicy": hpSwitchCosVlanDSCPPolicy,
       "hpSwitchCosVlanResolvedPriority": hpSwitchCosVlanResolvedPriority,
       "hpSwitchCosVlanApplyPolicy": hpSwitchCosVlanApplyPolicy,
       "hpSwitchCosProtocolConfigTable": hpSwitchCosProtocolConfigTable,
       "hpSwitchCosProtocolConfigEntry": hpSwitchCosProtocolConfigEntry,
       "hpSwitchCosProtocolType": hpSwitchCosProtocolType,
       "hpSwitchCosProtocolPriority": hpSwitchCosProtocolPriority,
       "hpSwitchCosAddressConfigTable": hpSwitchCosAddressConfigTable,
       "hpSwitchCosAddressConfigEntry": hpSwitchCosAddressConfigEntry,
       "hpSwitchCosAddressIndex": hpSwitchCosAddressIndex,
       "hpSwitchCosAddressType": hpSwitchCosAddressType,
       "hpSwitchCosAddressIp": hpSwitchCosAddressIp,
       "hpSwitchCosAddressPriority": hpSwitchCosAddressPriority,
       "hpSwitchCosAddressStatus": hpSwitchCosAddressStatus,
       "hpSwitchCosAddressDSCPPolicy": hpSwitchCosAddressDSCPPolicy,
       "hpSwitchCosAddressResolvedPriority": hpSwitchCosAddressResolvedPriority,
       "hpSwitchCosAddressApplyPolicy": hpSwitchCosAddressApplyPolicy,
       "hpSwitchCosIpv4AddressMask": hpSwitchCosIpv4AddressMask,
       "hpSwitchCosAddressIpv6": hpSwitchCosAddressIpv6,
       "hpSwitchCosAddressIpv6PrefixLength": hpSwitchCosAddressIpv6PrefixLength,
       "hpSwitchCosTosConfig": hpSwitchCosTosConfig,
       "hpSwitchCosTosConfigMode": hpSwitchCosTosConfigMode,
       "hpSwitchCosTosConfigTable": hpSwitchCosTosConfigTable,
       "hpSwitchCosTosConfigEntry": hpSwitchCosTosConfigEntry,
       "hpSwitchCosTosIndex": hpSwitchCosTosIndex,
       "hpSwitchCosTosPriority": hpSwitchCosTosPriority,
       "hpSwitchCosTosDSCPPolicy": hpSwitchCosTosDSCPPolicy,
       "hpSwitchCosTosResolvedPriority": hpSwitchCosTosResolvedPriority,
       "hpSwitchCosTosApplyPolicy": hpSwitchCosTosApplyPolicy,
       "hpSwitchCosDSCPPolicyConfigTable": hpSwitchCosDSCPPolicyConfigTable,
       "hpSwitchCosDSCPPolicyConfigEntry": hpSwitchCosDSCPPolicyConfigEntry,
       "hpSwitchCosDSCPPolicyIndex": hpSwitchCosDSCPPolicyIndex,
       "hpSwitchCosDSCPPolicyPriority": hpSwitchCosDSCPPolicyPriority,
       "hpSwitchCosDSCPPolicyName": hpSwitchCosDSCPPolicyName,
       "hpSwitchCosAppTypeConfigTable": hpSwitchCosAppTypeConfigTable,
       "hpSwitchCosAppTypeConfigEntry": hpSwitchCosAppTypeConfigEntry,
       "hpSwitchCosAppTypeConfigIndex": hpSwitchCosAppTypeConfigIndex,
       "hpSwitchCosAppTypeConfigType": hpSwitchCosAppTypeConfigType,
       "hpSwitchCosAppTypeSrcPort": hpSwitchCosAppTypeSrcPort,
       "hpSwitchCosAppTypeDestPort": hpSwitchCosAppTypeDestPort,
       "hpSwitchCosAppTypePriority": hpSwitchCosAppTypePriority,
       "hpSwitchCosAppTypeDSCPPolicy": hpSwitchCosAppTypeDSCPPolicy,
       "hpSwitchCosAppTypeResolvedPriority": hpSwitchCosAppTypeResolvedPriority,
       "hpSwitchCosAppTypeApplyPolicy": hpSwitchCosAppTypeApplyPolicy,
       "hpSwitchCosAppTypeStatus": hpSwitchCosAppTypeStatus,
       "hpSwitchCosAppTypeMaxSrcPort": hpSwitchCosAppTypeMaxSrcPort,
       "hpSwitchCosAppTypeMaxDestPort": hpSwitchCosAppTypeMaxDestPort,
       "hpSwitchCosAppTypeIpPacketType": hpSwitchCosAppTypeIpPacketType,
       "hpSwitchCosLastChange": hpSwitchCosLastChange,
       "hpSwitchConfigCosLastConfigError": hpSwitchConfigCosLastConfigError,
       "hpSwitchQueueWatchTable": hpSwitchQueueWatchTable,
       "hpSwitchQueueWatchEntry": hpSwitchQueueWatchEntry,
       "hpSwitchQueueWatchPort": hpSwitchQueueWatchPort,
       "hpSwitchQueueWatchState": hpSwitchQueueWatchState,
       "hpSwitchMeshConfig": hpSwitchMeshConfig,
       "hpSwitchMeshMulticastAgingMode": hpSwitchMeshMulticastAgingMode,
       "hpSwitchMeshBackwardCompatibility": hpSwitchMeshBackwardCompatibility,
       "hpSwitchMeshConfiguredId": hpSwitchMeshConfiguredId,
       "hpSwitchMeshActualId": hpSwitchMeshActualId,
       "hpSwitchPortIsolationConfig": hpSwitchPortIsolationConfig,
       "hpSwitchPortIsolationMode": hpSwitchPortIsolationMode,
       "hpSwitchPortIsolationConfigTable": hpSwitchPortIsolationConfigTable,
       "hpSwitchPortIsolationConfigEntry": hpSwitchPortIsolationConfigEntry,
       "hpSwitchPortIsolationPort": hpSwitchPortIsolationPort,
       "hpSwitchPortIsolationPortMode": hpSwitchPortIsolationPortMode,
       "hpSwitchSshConfig": hpSwitchSshConfig,
       "hpSwitchSshAdminStatus": hpSwitchSshAdminStatus,
       "hpSwitchSshVersion": hpSwitchSshVersion,
       "hpSwitchSshTimeout": hpSwitchSshTimeout,
       "hpSwitchSshPortNumber": hpSwitchSshPortNumber,
       "hpSwitchSshServerKeySize": hpSwitchSshServerKeySize,
       "hpSwitchSshFileServerAdminStatus": hpSwitchSshFileServerAdminStatus,
       "hpSwitchSshIpVersion": hpSwitchSshIpVersion,
       "hpSwitchSshReKeyStatus": hpSwitchSshReKeyStatus,
       "hpSwitchSshReKeyTime": hpSwitchSshReKeyTime,
       "hpSwitchSshReKeyVolume": hpSwitchSshReKeyVolume,
       "hpSwitchPendingConfig": hpSwitchPendingConfig,
       "hpSwitchPendingConfigControl": hpSwitchPendingConfigControl,
       "hpSwitchBWMinConfig": hpSwitchBWMinConfig,
       "hpSwitchBWMinEgressPortConfigTable": hpSwitchBWMinEgressPortConfigTable,
       "hpSwitchBWMinEgressPortConfigEntry": hpSwitchBWMinEgressPortConfigEntry,
       "hpSwitchBWMinEgressPortIndex": hpSwitchBWMinEgressPortIndex,
       "hpSwitchBWMinEgressPortPrctLowPriority": hpSwitchBWMinEgressPortPrctLowPriority,
       "hpSwitchBWMinEgressPortPrctNormalPriority": hpSwitchBWMinEgressPortPrctNormalPriority,
       "hpSwitchBWMinEgressPortPrctMedPriority": hpSwitchBWMinEgressPortPrctMedPriority,
       "hpSwitchBWMinEgressPortPrctHighPriority": hpSwitchBWMinEgressPortPrctHighPriority,
       "hpSwitchRateLimitPortConfig": hpSwitchRateLimitPortConfig,
       "hpSwitchRateLimitPortConfigTable": hpSwitchRateLimitPortConfigTable,
       "hpSwitchRateLimitPortConfigEntry": hpSwitchRateLimitPortConfigEntry,
       "hpSwitchRateLimitPortIndex": hpSwitchRateLimitPortIndex,
       "hpSwitchRateLimitPortControlMode": hpSwitchRateLimitPortControlMode,
       "hpSwitchRateLimitPortSingleControlPrct": hpSwitchRateLimitPortSingleControlPrct,
       "hpSwitchRateLimitPortPrctLowPriority": hpSwitchRateLimitPortPrctLowPriority,
       "hpSwitchRateLimitPortPrctNormalPriority": hpSwitchRateLimitPortPrctNormalPriority,
       "hpSwitchRateLimitPortPrctMedPriority": hpSwitchRateLimitPortPrctMedPriority,
       "hpSwitchRateLimitPortPrctHighPriority": hpSwitchRateLimitPortPrctHighPriority,
       "hpSwitchQosPassThroughMode": hpSwitchQosPassThroughMode,
       "hpSwitchQosPassThroughModeConfig": hpSwitchQosPassThroughModeConfig,
       "hpSwitchReboot": hpSwitchReboot,
       "hpSwitchRebootConfig": hpSwitchRebootConfig,
       "hpSwitchRebootFastBoot": hpSwitchRebootFastBoot,
       "hpSwitchProtectedPortsConfig": hpSwitchProtectedPortsConfig,
       "hpSwitchProtectedPortsMask": hpSwitchProtectedPortsMask,
       "hpSwitchLACPConfig": hpSwitchLACPConfig,
       "hpSwitchLACPAllPortsStatus": hpSwitchLACPAllPortsStatus,
       "hpSwitchDSCPRateLimitConfig": hpSwitchDSCPRateLimitConfig,
       "hpSwitchDSCPRateLimitConfigTable": hpSwitchDSCPRateLimitConfigTable,
       "hpSwitchDSCPRateLimitConfigEntry": hpSwitchDSCPRateLimitConfigEntry,
       "hpSwitchDSCPRateLimitIndex": hpSwitchDSCPRateLimitIndex,
       "hpSwitchDSCPRateLimitKbps": hpSwitchDSCPRateLimitKbps,
       "hpSwitchDSCPRateLimitPorts": hpSwitchDSCPRateLimitPorts,
       "hpSwitchTcpPushPreserve": hpSwitchTcpPushPreserve,
       "hpSwitchTcpPushPreserveConfig": hpSwitchTcpPushPreserveConfig,
       "hpSwitchIfMau": hpSwitchIfMau,
       "hpSwitchIfMauTypeListBits": hpSwitchIfMauTypeListBits,
       "hpSwitchIfMauAutoNegCapabilityBits": hpSwitchIfMauAutoNegCapabilityBits,
       "hpSwitchIfMauAutoNegCapAdvertisedBits": hpSwitchIfMauAutoNegCapAdvertisedBits,
       "hpSwitchIfMauAutoNegCapReceivedBits": hpSwitchIfMauAutoNegCapReceivedBits}
)
