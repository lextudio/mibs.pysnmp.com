# SNMP MIB module (DGS-1100-10ME_A1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-1100-10ME_A1
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:27 2024
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

(dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBridge) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBridge")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(SnmpAdminString,
 SnmpEngineID,
 SnmpSecurityLevel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID",
    "SnmpSecurityLevel")

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


# TEXTUAL-CONVENTIONS



class VlanIndex(Unsigned32, TextualConvention):
    status = "current"


class PortList(OctetString, TextualConvention):
    status = "current"


class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Timeout(Integer32, TextualConvention):
    status = "current"
    displayHint = "d4"


class OwnerString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class RmonStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )



class OperationResponseStatus(Integer32, TextualConvention):
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
        *(("arpFailure", 8),
          ("interfaceInactiveToTarget", 7),
          ("internalError", 3),
          ("invalidHostAddress", 11),
          ("maxConcurrentLimitReached", 9),
          ("noRouteToTarget", 6),
          ("requestTimedOut", 4),
          ("responseReceived", 1),
          ("unableToResolveDnsName", 10),
          ("unknown", 2),
          ("unknownDestinationAddress", 5))
    )



class LldpChassisIdSubtype(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("interfaceName", 6),
          ("local", 7),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("portComponent", 3))
    )



class LldpChassisId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpPortIdSubtype(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("agentCircuitId", 6),
          ("interfaceAlias", 1),
          ("interfaceName", 5),
          ("local", 7),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("portComponent", 2))
    )



class LldpPortId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpManAddrIfSubtype(Integer32, TextualConvention):
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
        *(("ifIndex", 2),
          ("systemPortNumber", 3),
          ("unknown", 1))
    )



class LldpManAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class LldpSystemCapabilitiesMap(Bits, TextualConvention):
    status = "current"


class LldpPortNumber(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class LldpPortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class TimeFilter(TimeTicks, TextualConvention):
    status = "current"


class LldpPowerPortClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pClassPD", 2),
          ("pClassPSE", 1))
    )



class LldpLinkAggStatusMap(Bits, TextualConvention):
    status = "current"


class ZeroBasedCounter32(Gauge32, TextualConvention):
    status = "current"


class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_D_link_ObjectIdentity = ObjectIdentity
d_link = _D_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_DGS1100SeriesProd_ObjectIdentity = ObjectIdentity
dlink_DGS1100SeriesProd = _Dlink_DGS1100SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134)
)
_Dgs_1100_10ME_ObjectIdentity = ObjectIdentity
dgs_1100_10ME = _Dgs_1100_10ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2)
)
_Dgs_1100_10ME_A1_ObjectIdentity = ObjectIdentity
dgs_1100_10ME_A1 = _Dgs_1100_10ME_A1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1)
)
_CompanySystem_ObjectIdentity = ObjectIdentity
companySystem = _CompanySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1)
)
_SysDevInfo_ObjectIdentity = ObjectIdentity
sysDevInfo = _SysDevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 1)
)


class _SysSwitchName_Type(DisplayString):
    """Custom type sysSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysSwitchName_Type.__name__ = "DisplayString"
_SysSwitchName_Object = MibScalar
sysSwitchName = _SysSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 1, 1),
    _SysSwitchName_Type()
)
sysSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSwitchName.setStatus("current")


class _SysHardwareVersion_Type(DisplayString):
    """Custom type sysHardwareVersion based on DisplayString"""
    defaultValue = OctetString("Version of the hardware")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysHardwareVersion_Type.__name__ = "DisplayString"
_SysHardwareVersion_Object = MibScalar
sysHardwareVersion = _SysHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 1, 2),
    _SysHardwareVersion_Type()
)
sysHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersion.setStatus("current")


class _SysFirmwareVersion_Type(DisplayString):
    """Custom type sysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysFirmwareVersion_Type.__name__ = "DisplayString"
_SysFirmwareVersion_Object = MibScalar
sysFirmwareVersion = _SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 1, 3),
    _SysFirmwareVersion_Type()
)
sysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareVersion.setStatus("current")


class _SysDeviceType_Type(DisplayString):
    """Custom type sysDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDeviceType_Type.__name__ = "DisplayString"
_SysDeviceType_Object = MibScalar
sysDeviceType = _SysDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 1, 4),
    _SysDeviceType_Type()
)
sysDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceType.setStatus("current")


class _SysBootVerion_Type(DisplayString):
    """Custom type sysBootVerion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysBootVerion_Type.__name__ = "DisplayString"
_SysBootVerion_Object = MibScalar
sysBootVerion = _SysBootVerion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 1, 5),
    _SysBootVerion_Type()
)
sysBootVerion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootVerion.setStatus("current")


class _SysLoginTimeout_Type(Integer32):
    """Custom type sysLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_SysLoginTimeout_Type.__name__ = "Integer32"
_SysLoginTimeout_Object = MibScalar
sysLoginTimeout = _SysLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 2),
    _SysLoginTimeout_Type()
)
sysLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginTimeout.setStatus("current")


class _SysLocationName_Type(DisplayString):
    """Custom type sysLocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysLocationName_Type.__name__ = "DisplayString"
_SysLocationName_Object = MibScalar
sysLocationName = _SysLocationName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 3),
    _SysLocationName_Type()
)
sysLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationName.setStatus("current")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("current")


class _SysSafeGuardEnable_Type(Integer32):
    """Custom type sysSafeGuardEnable based on Integer32"""
    defaultValue = 1

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


_SysSafeGuardEnable_Type.__name__ = "Integer32"
_SysSafeGuardEnable_Object = MibScalar
sysSafeGuardEnable = _SysSafeGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 8),
    _SysSafeGuardEnable_Type()
)
sysSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSafeGuardEnable.setStatus("current")


class _SysRestart_Type(Integer32):
    """Custom type sysRestart based on Integer32"""
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
        *(("noreboot", 1),
          ("reboot", 2),
          ("reset", 3),
          ("resetwithoutip", 4),
          ("resetwithoutipvlan", 5))
    )


_SysRestart_Type.__name__ = "Integer32"
_SysRestart_Object = MibScalar
sysRestart = _SysRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 9),
    _SysRestart_Type()
)
sysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestart.setStatus("current")


class _SysSave_Type(TruthValue):
    """Custom type sysSave based on TruthValue"""


_SysSave_Object = MibScalar
sysSave = _SysSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 10),
    _SysSave_Type()
)
sysSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSave.setStatus("current")


class _SysJumboFrameEnable_Type(Integer32):
    """Custom type sysJumboFrameEnable based on Integer32"""
    defaultValue = 2

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


_SysJumboFrameEnable_Type.__name__ = "Integer32"
_SysJumboFrameEnable_Object = MibScalar
sysJumboFrameEnable = _SysJumboFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 12),
    _SysJumboFrameEnable_Type()
)
sysJumboFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysJumboFrameEnable.setStatus("current")


class _SysDhcpAutoConfiguration_Type(Integer32):
    """Custom type sysDhcpAutoConfiguration based on Integer32"""
    defaultValue = 2

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


_SysDhcpAutoConfiguration_Type.__name__ = "Integer32"
_SysDhcpAutoConfiguration_Object = MibScalar
sysDhcpAutoConfiguration = _SysDhcpAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 16),
    _SysDhcpAutoConfiguration_Type()
)
sysDhcpAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpAutoConfiguration.setStatus("current")


class _SysWebState_Type(Integer32):
    """Custom type sysWebState based on Integer32"""
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


_SysWebState_Type.__name__ = "Integer32"
_SysWebState_Object = MibScalar
sysWebState = _SysWebState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 17),
    _SysWebState_Type()
)
sysWebState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysWebState.setStatus("current")


class _SysWebPortNumber_Type(Integer32):
    """Custom type sysWebPortNumber based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysWebPortNumber_Type.__name__ = "Integer32"
_SysWebPortNumber_Object = MibScalar
sysWebPortNumber = _SysWebPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 18),
    _SysWebPortNumber_Type()
)
sysWebPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysWebPortNumber.setStatus("current")


class _SysARPAgingTime_Type(Integer32):
    """Custom type sysARPAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysARPAgingTime_Type.__name__ = "Integer32"
_SysARPAgingTime_Object = MibScalar
sysARPAgingTime = _SysARPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 19),
    _SysARPAgingTime_Type()
)
sysARPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysARPAgingTime.setStatus("current")


class _SysMACAgingTime_Type(Integer32):
    """Custom type sysMACAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_SysMACAgingTime_Type.__name__ = "Integer32"
_SysMACAgingTime_Object = MibScalar
sysMACAgingTime = _SysMACAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 20),
    _SysMACAgingTime_Type()
)
sysMACAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMACAgingTime.setStatus("current")


class _SysTelnetsettingManagementOnOff_Type(Integer32):
    """Custom type sysTelnetsettingManagementOnOff based on Integer32"""
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


_SysTelnetsettingManagementOnOff_Type.__name__ = "Integer32"
_SysTelnetsettingManagementOnOff_Object = MibScalar
sysTelnetsettingManagementOnOff = _SysTelnetsettingManagementOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 23),
    _SysTelnetsettingManagementOnOff_Type()
)
sysTelnetsettingManagementOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTelnetsettingManagementOnOff.setStatus("current")


class _SysTelnetUDPPort_Type(Integer32):
    """Custom type sysTelnetUDPPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysTelnetUDPPort_Type.__name__ = "Integer32"
_SysTelnetUDPPort_Object = MibScalar
sysTelnetUDPPort = _SysTelnetUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 24),
    _SysTelnetUDPPort_Type()
)
sysTelnetUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTelnetUDPPort.setStatus("current")


class _SysAutoRefreshConfiguration_Type(Integer32):
    """Custom type sysAutoRefreshConfiguration based on Integer32"""
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
        *(("refreshimenever", 0),
          ("refreshtime10secs", 1),
          ("refreshtime1min", 3),
          ("refreshtime30secs", 2),
          ("refreshtime5mins", 4))
    )


_SysAutoRefreshConfiguration_Type.__name__ = "Integer32"
_SysAutoRefreshConfiguration_Object = MibScalar
sysAutoRefreshConfiguration = _SysAutoRefreshConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 25),
    _SysAutoRefreshConfiguration_Type()
)
sysAutoRefreshConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAutoRefreshConfiguration.setStatus("current")


class _SysMacAddr_Type(MacAddress):
    """Custom type sysMacAddr based on MacAddress"""
    defaultHexValue = "000102030405"


_SysMacAddr_Object = MibScalar
sysMacAddr = _SysMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 26),
    _SysMacAddr_Type()
)
sysMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAddr.setStatus("current")


class _SysSwitchTime_Type(DisplayString):
    """Custom type sysSwitchTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_SysSwitchTime_Type.__name__ = "DisplayString"
_SysSwitchTime_Object = MibScalar
sysSwitchTime = _SysSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 27),
    _SysSwitchTime_Type()
)
sysSwitchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSwitchTime.setStatus("current")


class _SysDhcpTimeout_Type(Integer32):
    """Custom type sysDhcpTimeout based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysDhcpTimeout_Type.__name__ = "Integer32"
_SysDhcpTimeout_Object = MibScalar
sysDhcpTimeout = _SysDhcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 28),
    _SysDhcpTimeout_Type()
)
sysDhcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpTimeout.setStatus("current")


class _SysSerialNumber_Type(DisplayString):
    """Custom type sysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysSerialNumber_Type.__name__ = "DisplayString"
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 29),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")
_SysCPU_ObjectIdentity = ObjectIdentity
sysCPU = _SysCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 30)
)
_CpuLast5SecUsage_Type = Integer32
_CpuLast5SecUsage_Object = MibScalar
cpuLast5SecUsage = _CpuLast5SecUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 30, 1),
    _CpuLast5SecUsage_Type()
)
cpuLast5SecUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLast5SecUsage.setStatus("current")
_CpuLast1MinUsage_Type = Integer32
_CpuLast1MinUsage_Object = MibScalar
cpuLast1MinUsage = _CpuLast1MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 30, 2),
    _CpuLast1MinUsage_Type()
)
cpuLast1MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLast1MinUsage.setStatus("current")
_CpuLast5MinUsage_Type = Integer32
_CpuLast5MinUsage_Object = MibScalar
cpuLast5MinUsage = _CpuLast5MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 30, 3),
    _CpuLast5MinUsage_Type()
)
cpuLast5MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLast5MinUsage.setStatus("current")
_SysRAM_ObjectIdentity = ObjectIdentity
sysRAM = _SysRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 31)
)
_RamLast5SecUsage_Type = Integer32
_RamLast5SecUsage_Object = MibScalar
ramLast5SecUsage = _RamLast5SecUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 31, 1),
    _RamLast5SecUsage_Type()
)
ramLast5SecUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramLast5SecUsage.setStatus("current")
_RamLast1MinUsage_Type = Integer32
_RamLast1MinUsage_Object = MibScalar
ramLast1MinUsage = _RamLast1MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 31, 2),
    _RamLast1MinUsage_Type()
)
ramLast1MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramLast1MinUsage.setStatus("current")
_RamLast5MinUsage_Type = Integer32
_RamLast5MinUsage_Object = MibScalar
ramLast5MinUsage = _RamLast5MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 31, 3),
    _RamLast5MinUsage_Type()
)
ramLast5MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramLast5MinUsage.setStatus("current")


class _SysCliPromptStr_Type(DisplayString):
    """Custom type sysCliPromptStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysCliPromptStr_Type.__name__ = "DisplayString"
_SysCliPromptStr_Object = MibScalar
sysCliPromptStr = _SysCliPromptStr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 32),
    _SysCliPromptStr_Type()
)
sysCliPromptStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCliPromptStr.setStatus("current")


class _SysSshState_Type(Integer32):
    """Custom type sysSshState based on Integer32"""
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


_SysSshState_Type.__name__ = "Integer32"
_SysSshState_Object = MibScalar
sysSshState = _SysSshState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 33),
    _SysSshState_Type()
)
sysSshState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSshState.setStatus("current")


class _SysSshPortNumber_Type(Integer32):
    """Custom type sysSshPortNumber based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysSshPortNumber_Type.__name__ = "Integer32"
_SysSshPortNumber_Object = MibScalar
sysSshPortNumber = _SysSshPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 34),
    _SysSshPortNumber_Type()
)
sysSshPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSshPortNumber.setStatus("current")
_SysPort_ObjectIdentity = ObjectIdentity
sysPort = _SysPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100)
)
_PortCtrlTable_Object = MibTable
portCtrlTable = _PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1)
)
if mibBuilder.loadTexts:
    portCtrlTable.setStatus("current")
_PortCtrlEntry_Object = MibTableRow
portCtrlEntry = _PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1)
)
portCtrlEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "portCtrlIndex"),
    (0, "DGS-1100-10ME_A1", "portCtrlMediumType"),
)
if mibBuilder.loadTexts:
    portCtrlEntry.setStatus("current")


class _PortCtrlIndex_Type(Integer32):
    """Custom type portCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortCtrlIndex_Type.__name__ = "Integer32"
_PortCtrlIndex_Object = MibTableColumn
portCtrlIndex = _PortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 1),
    _PortCtrlIndex_Type()
)
portCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCtrlIndex.setStatus("current")


class _PortCtrlMediumType_Type(Integer32):
    """Custom type portCtrlMediumType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_PortCtrlMediumType_Type.__name__ = "Integer32"
_PortCtrlMediumType_Object = MibTableColumn
portCtrlMediumType = _PortCtrlMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 2),
    _PortCtrlMediumType_Type()
)
portCtrlMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCtrlMediumType.setStatus("current")


class _PortCtrlSpeed_Type(Integer32):
    """Custom type portCtrlSpeed based on Integer32"""
    defaultValue = 6

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
        *(("auto", 6),
          ("disabled", 7),
          ("full1000m", 1),
          ("full100m", 2),
          ("full10m", 4),
          ("half100m", 3),
          ("half10m", 5))
    )


_PortCtrlSpeed_Type.__name__ = "Integer32"
_PortCtrlSpeed_Object = MibTableColumn
portCtrlSpeed = _PortCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 3),
    _PortCtrlSpeed_Type()
)
portCtrlSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlSpeed.setStatus("current")


class _PortCtrlLinkStatus_Type(Integer32):
    """Custom type portCtrlLinkStatus based on Integer32"""
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
        *(("down", 1),
          ("full1000m", 2),
          ("full100m", 3),
          ("full10m", 5),
          ("half100m", 4),
          ("half10m", 6))
    )


_PortCtrlLinkStatus_Type.__name__ = "Integer32"
_PortCtrlLinkStatus_Object = MibTableColumn
portCtrlLinkStatus = _PortCtrlLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 4),
    _PortCtrlLinkStatus_Type()
)
portCtrlLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCtrlLinkStatus.setStatus("current")


class _PortCtrlMDI_Type(Integer32):
    """Custom type portCtrlMDI based on Integer32"""
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
          ("mdi", 2),
          ("mdix", 3))
    )


_PortCtrlMDI_Type.__name__ = "Integer32"
_PortCtrlMDI_Object = MibTableColumn
portCtrlMDI = _PortCtrlMDI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 5),
    _PortCtrlMDI_Type()
)
portCtrlMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlMDI.setStatus("current")


class _PortCtrlFlowControl_Type(Integer32):
    """Custom type portCtrlFlowControl based on Integer32"""
    defaultValue = 2

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


_PortCtrlFlowControl_Type.__name__ = "Integer32"
_PortCtrlFlowControl_Object = MibTableColumn
portCtrlFlowControl = _PortCtrlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 6),
    _PortCtrlFlowControl_Type()
)
portCtrlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlFlowControl.setStatus("current")


class _PortCtrlFlowControlOper_Type(Integer32):
    """Custom type portCtrlFlowControlOper based on Integer32"""
    defaultValue = 2

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


_PortCtrlFlowControlOper_Type.__name__ = "Integer32"
_PortCtrlFlowControlOper_Object = MibTableColumn
portCtrlFlowControlOper = _PortCtrlFlowControlOper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 7),
    _PortCtrlFlowControlOper_Type()
)
portCtrlFlowControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCtrlFlowControlOper.setStatus("current")


class _PortCtrlAdminState_Type(Integer32):
    """Custom type portCtrlAdminState based on Integer32"""
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


_PortCtrlAdminState_Type.__name__ = "Integer32"
_PortCtrlAdminState_Object = MibTableColumn
portCtrlAdminState = _PortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 8),
    _PortCtrlAdminState_Type()
)
portCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlAdminState.setStatus("current")


class _PortCtrlDetailMediumType_Type(Integer32):
    """Custom type portCtrlDetailMediumType based on Integer32"""
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
        *(("fastethernet", 1),
          ("fiberwith100BaseSFPModule", 3),
          ("fiberwith1GBaseSFPModule", 4),
          ("gigabitethernet", 2))
    )


_PortCtrlDetailMediumType_Type.__name__ = "Integer32"
_PortCtrlDetailMediumType_Object = MibTableColumn
portCtrlDetailMediumType = _PortCtrlDetailMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 9),
    _PortCtrlDetailMediumType_Type()
)
portCtrlDetailMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCtrlDetailMediumType.setStatus("current")


class _PortCtrlDynamicMacAutoLearn_Type(Integer32):
    """Custom type portCtrlDynamicMacAutoLearn based on Integer32"""
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


_PortCtrlDynamicMacAutoLearn_Type.__name__ = "Integer32"
_PortCtrlDynamicMacAutoLearn_Object = MibTableColumn
portCtrlDynamicMacAutoLearn = _PortCtrlDynamicMacAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 1, 1, 10),
    _PortCtrlDynamicMacAutoLearn_Type()
)
portCtrlDynamicMacAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlDynamicMacAutoLearn.setStatus("current")
_PortDescriptionTable_Object = MibTable
portDescriptionTable = _PortDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 2)
)
if mibBuilder.loadTexts:
    portDescriptionTable.setStatus("current")
_PortDescriptionEntry_Object = MibTableRow
portDescriptionEntry = _PortDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 2, 1)
)
portDescriptionEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "portDescIndex"),
    (0, "DGS-1100-10ME_A1", "portDescMediumType"),
)
if mibBuilder.loadTexts:
    portDescriptionEntry.setStatus("current")


class _PortDescIndex_Type(Integer32):
    """Custom type portDescIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortDescIndex_Type.__name__ = "Integer32"
_PortDescIndex_Object = MibTableColumn
portDescIndex = _PortDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 2, 1, 1),
    _PortDescIndex_Type()
)
portDescIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDescIndex.setStatus("current")


class _PortDescMediumType_Type(Integer32):
    """Custom type portDescMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_PortDescMediumType_Type.__name__ = "Integer32"
_PortDescMediumType_Object = MibTableColumn
portDescMediumType = _PortDescMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 2, 1, 2),
    _PortDescMediumType_Type()
)
portDescMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDescMediumType.setStatus("current")


class _PortDescString_Type(DisplayString):
    """Custom type portDescString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortDescString_Type.__name__ = "DisplayString"
_PortDescString_Object = MibTableColumn
portDescString = _PortDescString_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 2, 1, 3),
    _PortDescString_Type()
)
portDescString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDescString.setStatus("current")
_PortErrTable_Object = MibTable
portErrTable = _PortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 3)
)
if mibBuilder.loadTexts:
    portErrTable.setStatus("current")
_PortErrEntry_Object = MibTableRow
portErrEntry = _PortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 3, 1)
)
portErrEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "portErrPortIndex"),
)
if mibBuilder.loadTexts:
    portErrEntry.setStatus("current")


class _PortErrPortIndex_Type(Integer32):
    """Custom type portErrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortErrPortIndex_Type.__name__ = "Integer32"
_PortErrPortIndex_Object = MibTableColumn
portErrPortIndex = _PortErrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 3, 1, 1),
    _PortErrPortIndex_Type()
)
portErrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrPortIndex.setStatus("current")


class _PortErrPortState_Type(Integer32):
    """Custom type portErrPortState based on Integer32"""
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


_PortErrPortState_Type.__name__ = "Integer32"
_PortErrPortState_Object = MibTableColumn
portErrPortState = _PortErrPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 3, 1, 2),
    _PortErrPortState_Type()
)
portErrPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrPortState.setStatus("current")


class _PortErrPortStatus_Type(Integer32):
    """Custom type portErrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("err-disabled", 2),
          ("other", 1))
    )


_PortErrPortStatus_Type.__name__ = "Integer32"
_PortErrPortStatus_Object = MibTableColumn
portErrPortStatus = _PortErrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 3, 1, 3),
    _PortErrPortStatus_Type()
)
portErrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrPortStatus.setStatus("current")


class _PortErrPortReason_Type(Integer32):
    """Custom type portErrPortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duld", 3),
          ("lbd", 1),
          ("trafficcontrol", 2))
    )


_PortErrPortReason_Type.__name__ = "Integer32"
_PortErrPortReason_Object = MibTableColumn
portErrPortReason = _PortErrPortReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 3, 1, 4),
    _PortErrPortReason_Type()
)
portErrPortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrPortReason.setStatus("current")
_PortUtilizTable_Object = MibTable
portUtilizTable = _PortUtilizTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 4)
)
if mibBuilder.loadTexts:
    portUtilizTable.setStatus("current")
_PortUtilizEntry_Object = MibTableRow
portUtilizEntry = _PortUtilizEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 4, 1)
)
portUtilizEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "portUtilizIndex"),
)
if mibBuilder.loadTexts:
    portUtilizEntry.setStatus("current")


class _PortUtilizIndex_Type(Integer32):
    """Custom type portUtilizIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PortUtilizIndex_Type.__name__ = "Integer32"
_PortUtilizIndex_Object = MibTableColumn
portUtilizIndex = _PortUtilizIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 4, 1, 1),
    _PortUtilizIndex_Type()
)
portUtilizIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUtilizIndex.setStatus("current")
_PortUtilizTX_Type = Integer32
_PortUtilizTX_Object = MibTableColumn
portUtilizTX = _PortUtilizTX_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 4, 1, 2),
    _PortUtilizTX_Type()
)
portUtilizTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUtilizTX.setStatus("current")
_PortUtilizRX_Type = Integer32
_PortUtilizRX_Object = MibTableColumn
portUtilizRX = _PortUtilizRX_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 4, 1, 3),
    _PortUtilizRX_Type()
)
portUtilizRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUtilizRX.setStatus("current")
_PortUtilizAverage_Type = Integer32
_PortUtilizAverage_Object = MibTableColumn
portUtilizAverage = _PortUtilizAverage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 1, 100, 4, 1, 4),
    _PortUtilizAverage_Type()
)
portUtilizAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUtilizAverage.setStatus("current")
_CompanyIpifGroup_ObjectIdentity = ObjectIdentity
companyIpifGroup = _CompanyIpifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2)
)
_SysIpifSupportV4V6Info_ObjectIdentity = ObjectIdentity
sysIpifSupportV4V6Info = _SysIpifSupportV4V6Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7)
)


class _Ipv4AddrCfgMode_Type(Integer32):
    """Custom type ipv4AddrCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 1))
    )


_Ipv4AddrCfgMode_Type.__name__ = "Integer32"
_Ipv4AddrCfgMode_Object = MibScalar
ipv4AddrCfgMode = _Ipv4AddrCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 1),
    _Ipv4AddrCfgMode_Type()
)
ipv4AddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4AddrCfgMode.setStatus("current")
_Ipv4Address_Type = IpAddress
_Ipv4Address_Object = MibScalar
ipv4Address = _Ipv4Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 2),
    _Ipv4Address_Type()
)
ipv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4Address.setStatus("current")
_Ipv4SubnetMask_Type = IpAddress
_Ipv4SubnetMask_Object = MibScalar
ipv4SubnetMask = _Ipv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 3),
    _Ipv4SubnetMask_Type()
)
ipv4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4SubnetMask.setStatus("current")
_Ipv4DefaultGateway_Type = IpAddress
_Ipv4DefaultGateway_Object = MibScalar
ipv4DefaultGateway = _Ipv4DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 4),
    _Ipv4DefaultGateway_Type()
)
ipv4DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4DefaultGateway.setStatus("current")


class _DhcpOption12Status_Type(Integer32):
    """Custom type dhcpOption12Status based on Integer32"""
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


_DhcpOption12Status_Type.__name__ = "Integer32"
_DhcpOption12Status_Object = MibScalar
dhcpOption12Status = _DhcpOption12Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 5),
    _DhcpOption12Status_Type()
)
dhcpOption12Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12Status.setStatus("current")
_DhcpOption12HostName_Type = DisplayString
_DhcpOption12HostName_Object = MibScalar
dhcpOption12HostName = _DhcpOption12HostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 6),
    _DhcpOption12HostName_Type()
)
dhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12HostName.setStatus("current")


class _Ipv6GlobalStatus_Type(Integer32):
    """Custom type ipv6GlobalStatus based on Integer32"""
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


_Ipv6GlobalStatus_Type.__name__ = "Integer32"
_Ipv6GlobalStatus_Object = MibScalar
ipv6GlobalStatus = _Ipv6GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 9),
    _Ipv6GlobalStatus_Type()
)
ipv6GlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6GlobalStatus.setStatus("current")


class _Ipv6DHCPStatus_Type(Integer32):
    """Custom type ipv6DHCPStatus based on Integer32"""
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


_Ipv6DHCPStatus_Type.__name__ = "Integer32"
_Ipv6DHCPStatus_Object = MibScalar
ipv6DHCPStatus = _Ipv6DHCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 10),
    _Ipv6DHCPStatus_Type()
)
ipv6DHCPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DHCPStatus.setStatus("current")


class _Ipv6AutolinkloStatus_Type(Integer32):
    """Custom type ipv6AutolinkloStatus based on Integer32"""
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


_Ipv6AutolinkloStatus_Type.__name__ = "Integer32"
_Ipv6AutolinkloStatus_Object = MibScalar
ipv6AutolinkloStatus = _Ipv6AutolinkloStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 11),
    _Ipv6AutolinkloStatus_Type()
)
ipv6AutolinkloStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6AutolinkloStatus.setStatus("current")


class _Ipv6NSRetransmitTime_Type(Integer32):
    """Custom type ipv6NSRetransmitTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Ipv6NSRetransmitTime_Type.__name__ = "Integer32"
_Ipv6NSRetransmitTime_Object = MibScalar
ipv6NSRetransmitTime = _Ipv6NSRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 12),
    _Ipv6NSRetransmitTime_Type()
)
ipv6NSRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6NSRetransmitTime.setStatus("current")
_Ipv6DefaultRouteTable_Object = MibTable
ipv6DefaultRouteTable = _Ipv6DefaultRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 13)
)
if mibBuilder.loadTexts:
    ipv6DefaultRouteTable.setStatus("current")
_Ipv6DefaultRouteEntry_Object = MibTableRow
ipv6DefaultRouteEntry = _Ipv6DefaultRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 13, 1)
)
ipv6DefaultRouteEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "ipv6DefaultRouteProtocol"),
    (0, "DGS-1100-10ME_A1", "ipv6DefaultRouteNextHop"),
)
if mibBuilder.loadTexts:
    ipv6DefaultRouteEntry.setStatus("current")


class _Ipv6DefaultRouteProtocol_Type(Integer32):
    """Custom type ipv6DefaultRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 4),
          ("static", 3))
    )


_Ipv6DefaultRouteProtocol_Type.__name__ = "Integer32"
_Ipv6DefaultRouteProtocol_Object = MibTableColumn
ipv6DefaultRouteProtocol = _Ipv6DefaultRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 13, 1, 3),
    _Ipv6DefaultRouteProtocol_Type()
)
ipv6DefaultRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouteProtocol.setStatus("current")
_Ipv6DefaultRouteNextHop_Type = Ipv6Address
_Ipv6DefaultRouteNextHop_Object = MibTableColumn
ipv6DefaultRouteNextHop = _Ipv6DefaultRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 13, 1, 4),
    _Ipv6DefaultRouteNextHop_Type()
)
ipv6DefaultRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouteNextHop.setStatus("current")
_Ipv6DefaultRouteIfIndex_Type = InterfaceIndex
_Ipv6DefaultRouteIfIndex_Object = MibTableColumn
ipv6DefaultRouteIfIndex = _Ipv6DefaultRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 13, 1, 5),
    _Ipv6DefaultRouteIfIndex_Type()
)
ipv6DefaultRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouteIfIndex.setStatus("current")


class _Ipv6DefaultRouteMetric_Type(Unsigned32):
    """Custom type ipv6DefaultRouteMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ipv6DefaultRouteMetric_Type.__name__ = "Unsigned32"
_Ipv6DefaultRouteMetric_Object = MibTableColumn
ipv6DefaultRouteMetric = _Ipv6DefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 13, 1, 6),
    _Ipv6DefaultRouteMetric_Type()
)
ipv6DefaultRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DefaultRouteMetric.setStatus("current")
_Ipv6DefaultRouteAdminStatus_Type = RowStatus
_Ipv6DefaultRouteAdminStatus_Object = MibTableColumn
ipv6DefaultRouteAdminStatus = _Ipv6DefaultRouteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 13, 1, 10),
    _Ipv6DefaultRouteAdminStatus_Type()
)
ipv6DefaultRouteAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6DefaultRouteAdminStatus.setStatus("current")
_Ipv6AddressTable_Object = MibTable
ipv6AddressTable = _Ipv6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 14)
)
if mibBuilder.loadTexts:
    ipv6AddressTable.setStatus("current")
_Ipv6AddressEntry_Object = MibTableRow
ipv6AddressEntry = _Ipv6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 14, 1)
)
ipv6AddressEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "ipv6AddressMainIndex"),
    (0, "DGS-1100-10ME_A1", "ipv6AddressIpAddr"),
    (0, "DGS-1100-10ME_A1", "ipv6AddressIpPrefix"),
)
if mibBuilder.loadTexts:
    ipv6AddressEntry.setStatus("current")
_Ipv6AddressMainIndex_Type = InterfaceIndex
_Ipv6AddressMainIndex_Object = MibTableColumn
ipv6AddressMainIndex = _Ipv6AddressMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 14, 1, 1),
    _Ipv6AddressMainIndex_Type()
)
ipv6AddressMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddressMainIndex.setStatus("current")
_Ipv6AddressIpAddr_Type = Ipv6Address
_Ipv6AddressIpAddr_Object = MibTableColumn
ipv6AddressIpAddr = _Ipv6AddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 14, 1, 2),
    _Ipv6AddressIpAddr_Type()
)
ipv6AddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddressIpAddr.setStatus("current")
_Ipv6AddressIpPrefix_Type = Integer32
_Ipv6AddressIpPrefix_Object = MibTableColumn
ipv6AddressIpPrefix = _Ipv6AddressIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 14, 1, 3),
    _Ipv6AddressIpPrefix_Type()
)
ipv6AddressIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddressIpPrefix.setStatus("current")


class _Ipv6AddressIpType_Type(Integer32):
    """Custom type ipv6AddressIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linklocal", 3),
          ("unicast", 1))
    )


_Ipv6AddressIpType_Type.__name__ = "Integer32"
_Ipv6AddressIpType_Object = MibTableColumn
ipv6AddressIpType = _Ipv6AddressIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 14, 1, 4),
    _Ipv6AddressIpType_Type()
)
ipv6AddressIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddressIpType.setStatus("current")
_Ipv6AddressRowStatus_Type = RowStatus
_Ipv6AddressRowStatus_Object = MibTableColumn
ipv6AddressRowStatus = _Ipv6AddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 14, 1, 5),
    _Ipv6AddressRowStatus_Type()
)
ipv6AddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6AddressRowStatus.setStatus("current")


class _DhcpRetryCount_Type(Integer32):
    """Custom type dhcpRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_DhcpRetryCount_Type.__name__ = "Integer32"
_DhcpRetryCount_Object = MibScalar
dhcpRetryCount = _DhcpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 7, 15),
    _DhcpRetryCount_Type()
)
dhcpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRetryCount.setStatus("current")
_SysIpifTraps_ObjectIdentity = ObjectIdentity
sysIpifTraps = _SysIpifTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 8)
)
_CompanyTftpGroup_ObjectIdentity = ObjectIdentity
companyTftpGroup = _CompanyTftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3)
)
_SysTftpFwTargetGroup_ObjectIdentity = ObjectIdentity
sysTftpFwTargetGroup = _SysTftpFwTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1)
)
_TftpFwTargetServerIpAddress_Type = Ipv6Address
_TftpFwTargetServerIpAddress_Object = MibScalar
tftpFwTargetServerIpAddress = _TftpFwTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1, 1),
    _TftpFwTargetServerIpAddress_Type()
)
tftpFwTargetServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTargetServerIpAddress.setStatus("current")


class _TftpFwTargetServerIpType_Type(Integer32):
    """Custom type tftpFwTargetServerIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2))
    )


_TftpFwTargetServerIpType_Type.__name__ = "Integer32"
_TftpFwTargetServerIpType_Object = MibScalar
tftpFwTargetServerIpType = _TftpFwTargetServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1, 2),
    _TftpFwTargetServerIpType_Type()
)
tftpFwTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTargetServerIpType.setStatus("current")
_TftpFwTargetInterfaceName_Type = OctetString
_TftpFwTargetInterfaceName_Object = MibScalar
tftpFwTargetInterfaceName = _TftpFwTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1, 3),
    _TftpFwTargetInterfaceName_Type()
)
tftpFwTargetInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTargetInterfaceName.setStatus("current")


class _TftpFwTargetImageFileName_Type(DisplayString):
    """Custom type tftpFwTargetImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TftpFwTargetImageFileName_Type.__name__ = "DisplayString"
_TftpFwTargetImageFileName_Object = MibScalar
tftpFwTargetImageFileName = _TftpFwTargetImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1, 4),
    _TftpFwTargetImageFileName_Type()
)
tftpFwTargetImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTargetImageFileName.setStatus("current")


class _TftpFwTargetTftpOperation_Type(Integer32):
    """Custom type tftpFwTargetTftpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("none", 0),
          ("upload", 2))
    )


_TftpFwTargetTftpOperation_Type.__name__ = "Integer32"
_TftpFwTargetTftpOperation_Object = MibScalar
tftpFwTargetTftpOperation = _TftpFwTargetTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1, 5),
    _TftpFwTargetTftpOperation_Type()
)
tftpFwTargetTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTargetTftpOperation.setStatus("current")


class _TftpFwTargetTftpOperationStatus_Type(Integer32):
    """Custom type tftpFwTargetTftpOperationStatus based on Integer32"""
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
        *(("fail", 2),
          ("none", 0),
          ("progressing", 3),
          ("success", 1),
          ("transmit", 4))
    )


_TftpFwTargetTftpOperationStatus_Type.__name__ = "Integer32"
_TftpFwTargetTftpOperationStatus_Object = MibScalar
tftpFwTargetTftpOperationStatus = _TftpFwTargetTftpOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1, 6),
    _TftpFwTargetTftpOperationStatus_Type()
)
tftpFwTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTargetTftpOperationStatus.setStatus("current")


class _TftpFwTargetTransferPercentage_Type(Integer32):
    """Custom type tftpFwTargetTransferPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TftpFwTargetTransferPercentage_Type.__name__ = "Integer32"
_TftpFwTargetTransferPercentage_Object = MibScalar
tftpFwTargetTransferPercentage = _TftpFwTargetTransferPercentage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 1, 7),
    _TftpFwTargetTransferPercentage_Type()
)
tftpFwTargetTransferPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTargetTransferPercentage.setStatus("current")
_SysTftpCfgTargetGroup_ObjectIdentity = ObjectIdentity
sysTftpCfgTargetGroup = _SysTftpCfgTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 2)
)
_TftpCfgTargetServerIpAddress_Type = Ipv6Address
_TftpCfgTargetServerIpAddress_Object = MibScalar
tftpCfgTargetServerIpAddress = _TftpCfgTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 2, 1),
    _TftpCfgTargetServerIpAddress_Type()
)
tftpCfgTargetServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetServerIpAddress.setStatus("current")


class _TftpCfgTargetServerIpType_Type(Integer32):
    """Custom type tftpCfgTargetServerIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2))
    )


_TftpCfgTargetServerIpType_Type.__name__ = "Integer32"
_TftpCfgTargetServerIpType_Object = MibScalar
tftpCfgTargetServerIpType = _TftpCfgTargetServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 2, 2),
    _TftpCfgTargetServerIpType_Type()
)
tftpCfgTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetServerIpType.setStatus("current")
_TftpCfgTargetInterfaceName_Type = OctetString
_TftpCfgTargetInterfaceName_Object = MibScalar
tftpCfgTargetInterfaceName = _TftpCfgTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 2, 3),
    _TftpCfgTargetInterfaceName_Type()
)
tftpCfgTargetInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetInterfaceName.setStatus("current")


class _TftpCfgTargetImageFileName_Type(DisplayString):
    """Custom type tftpCfgTargetImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TftpCfgTargetImageFileName_Type.__name__ = "DisplayString"
_TftpCfgTargetImageFileName_Object = MibScalar
tftpCfgTargetImageFileName = _TftpCfgTargetImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 2, 4),
    _TftpCfgTargetImageFileName_Type()
)
tftpCfgTargetImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetImageFileName.setStatus("current")


class _TftpCfgTargetTftpOperation_Type(Integer32):
    """Custom type tftpCfgTargetTftpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("progressing", 3),
          ("upload", 2))
    )


_TftpCfgTargetTftpOperation_Type.__name__ = "Integer32"
_TftpCfgTargetTftpOperation_Object = MibScalar
tftpCfgTargetTftpOperation = _TftpCfgTargetTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 2, 5),
    _TftpCfgTargetTftpOperation_Type()
)
tftpCfgTargetTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetTftpOperation.setStatus("current")


class _TftpCfgTargetTftpOperationStatus_Type(Integer32):
    """Custom type tftpCfgTargetTftpOperationStatus based on Integer32"""
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
        *(("fail", 2),
          ("none", 0),
          ("progressing", 3),
          ("success", 1))
    )


_TftpCfgTargetTftpOperationStatus_Type.__name__ = "Integer32"
_TftpCfgTargetTftpOperationStatus_Object = MibScalar
tftpCfgTargetTftpOperationStatus = _TftpCfgTargetTftpOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 2, 6),
    _TftpCfgTargetTftpOperationStatus_Type()
)
tftpCfgTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpCfgTargetTftpOperationStatus.setStatus("current")
_SysTftpSyslogTargetGroup_ObjectIdentity = ObjectIdentity
sysTftpSyslogTargetGroup = _SysTftpSyslogTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3)
)


class _SyslogFileSave_Type(Integer32):
    """Custom type syslogFileSave based on Integer32"""
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


_SyslogFileSave_Type.__name__ = "Integer32"
_SyslogFileSave_Object = MibScalar
syslogFileSave = _SyslogFileSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 1),
    _SyslogFileSave_Type()
)
syslogFileSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogFileSave.setStatus("current")
_TftpSyslogTargetServerIpAddress_Type = Ipv6Address
_TftpSyslogTargetServerIpAddress_Object = MibScalar
tftpSyslogTargetServerIpAddress = _TftpSyslogTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 2),
    _TftpSyslogTargetServerIpAddress_Type()
)
tftpSyslogTargetServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSyslogTargetServerIpAddress.setStatus("current")


class _TftpSyslogTargetServerIpType_Type(Integer32):
    """Custom type tftpSyslogTargetServerIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2))
    )


_TftpSyslogTargetServerIpType_Type.__name__ = "Integer32"
_TftpSyslogTargetServerIpType_Object = MibScalar
tftpSyslogTargetServerIpType = _TftpSyslogTargetServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 3),
    _TftpSyslogTargetServerIpType_Type()
)
tftpSyslogTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSyslogTargetServerIpType.setStatus("current")
_TftpSyslogTargetInterfaceName_Type = OctetString
_TftpSyslogTargetInterfaceName_Object = MibScalar
tftpSyslogTargetInterfaceName = _TftpSyslogTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 4),
    _TftpSyslogTargetInterfaceName_Type()
)
tftpSyslogTargetInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSyslogTargetInterfaceName.setStatus("current")


class _TftpSyslogTargetImageFileName_Type(DisplayString):
    """Custom type tftpSyslogTargetImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TftpSyslogTargetImageFileName_Type.__name__ = "DisplayString"
_TftpSyslogTargetImageFileName_Object = MibScalar
tftpSyslogTargetImageFileName = _TftpSyslogTargetImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 5),
    _TftpSyslogTargetImageFileName_Type()
)
tftpSyslogTargetImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSyslogTargetImageFileName.setStatus("current")


class _TftpSyslogTargetTftpOperation_Type(Integer32):
    """Custom type tftpSyslogTargetTftpOperation based on Integer32"""
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


_TftpSyslogTargetTftpOperation_Type.__name__ = "Integer32"
_TftpSyslogTargetTftpOperation_Object = MibScalar
tftpSyslogTargetTftpOperation = _TftpSyslogTargetTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 6),
    _TftpSyslogTargetTftpOperation_Type()
)
tftpSyslogTargetTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSyslogTargetTftpOperation.setStatus("current")


class _TftpSyslogTargetTftpOperationStatus_Type(Integer32):
    """Custom type tftpSyslogTargetTftpOperationStatus based on Integer32"""
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
        *(("fail", 2),
          ("none", 0),
          ("progressing", 3),
          ("success", 1))
    )


_TftpSyslogTargetTftpOperationStatus_Type.__name__ = "Integer32"
_TftpSyslogTargetTftpOperationStatus_Object = MibScalar
tftpSyslogTargetTftpOperationStatus = _TftpSyslogTargetTftpOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 7),
    _TftpSyslogTargetTftpOperationStatus_Type()
)
tftpSyslogTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpSyslogTargetTftpOperationStatus.setStatus("current")


class _TftpSyslogTargetTftpTransferPercentage_Type(Integer32):
    """Custom type tftpSyslogTargetTftpTransferPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TftpSyslogTargetTftpTransferPercentage_Type.__name__ = "Integer32"
_TftpSyslogTargetTftpTransferPercentage_Object = MibScalar
tftpSyslogTargetTftpTransferPercentage = _TftpSyslogTargetTftpTransferPercentage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 3, 8),
    _TftpSyslogTargetTftpTransferPercentage_Type()
)
tftpSyslogTargetTftpTransferPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpSyslogTargetTftpTransferPercentage.setStatus("current")
_SysTftpTrapGroup_ObjectIdentity = ObjectIdentity
sysTftpTrapGroup = _SysTftpTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 4)
)
_SysFimwareTraps_ObjectIdentity = ObjectIdentity
sysFimwareTraps = _SysFimwareTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 4, 0)
)
_CompanyUserAccount_ObjectIdentity = ObjectIdentity
companyUserAccount = _CompanyUserAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4)
)
_SysUserAccount_ObjectIdentity = ObjectIdentity
sysUserAccount = _SysUserAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1)
)
_AdminUserTable_Object = MibTable
adminUserTable = _AdminUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    adminUserTable.setStatus("current")
_AdminUserEntry_Object = MibTableRow
adminUserEntry = _AdminUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1, 1)
)
adminUserEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "userName"),
)
if mibBuilder.loadTexts:
    adminUserEntry.setStatus("current")


class _UserName_Type(SnmpAdminString):
    """Custom type userName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_UserName_Type.__name__ = "SnmpAdminString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserPassword_Type(DisplayString):
    """Custom type userPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UserPassword_Type.__name__ = "DisplayString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1, 1, 2),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")


class _UserAccessRight_Type(Integer32):
    """Custom type userAccessRight based on Integer32"""
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
        *(("admin", 1),
          ("operator", 2),
          ("user", 3))
    )


_UserAccessRight_Type.__name__ = "Integer32"
_UserAccessRight_Object = MibTableColumn
userAccessRight = _UserAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1, 1, 3),
    _UserAccessRight_Type()
)
userAccessRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAccessRight.setStatus("current")


class _UserEncrypt_Type(Integer32):
    """Custom type userEncrypt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plainText", 1),
          ("sha1", 2))
    )


_UserEncrypt_Type.__name__ = "Integer32"
_UserEncrypt_Object = MibTableColumn
userEncrypt = _UserEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1, 1, 4),
    _UserEncrypt_Type()
)
userEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEncrypt.setStatus("current")


class _UserEncryptControl_Type(Integer32):
    """Custom type userEncryptControl based on Integer32"""
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


_UserEncryptControl_Type.__name__ = "Integer32"
_UserEncryptControl_Object = MibTableColumn
userEncryptControl = _UserEncryptControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1, 1, 5),
    _UserEncryptControl_Type()
)
userEncryptControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEncryptControl.setStatus("current")
_UserRowStatus_Type = RowStatus
_UserRowStatus_Object = MibTableColumn
userRowStatus = _UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 1, 1, 1, 6),
    _UserRowStatus_Type()
)
userRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userRowStatus.setStatus("current")


class _SysPasswordEncrypt_Type(Integer32):
    """Custom type sysPasswordEncrypt based on Integer32"""
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


_SysPasswordEncrypt_Type.__name__ = "Integer32"
_SysPasswordEncrypt_Object = MibScalar
sysPasswordEncrypt = _SysPasswordEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 4, 2),
    _SysPasswordEncrypt_Type()
)
sysPasswordEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysPasswordEncrypt.setStatus("current")
_CompanySNMP_ObjectIdentity = ObjectIdentity
companySNMP = _CompanySNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5)
)


class _SysSNMPGlobalState_Type(Integer32):
    """Custom type sysSNMPGlobalState based on Integer32"""
    defaultValue = 1

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


_SysSNMPGlobalState_Type.__name__ = "Integer32"
_SysSNMPGlobalState_Object = MibScalar
sysSNMPGlobalState = _SysSNMPGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 1),
    _SysSNMPGlobalState_Type()
)
sysSNMPGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNMPGlobalState.setStatus("current")
_SysSNMPUser_ObjectIdentity = ObjectIdentity
sysSNMPUser = _SysSNMPUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2)
)
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1)
)
snmpUserEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "snmpUserName"),
    (0, "DGS-1100-10ME_A1", "snmpUserVersion"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")


class _SnmpUserName_Type(SnmpAdminString):
    """Custom type snmpUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserName_Type.__name__ = "SnmpAdminString"
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 1),
    _SnmpUserName_Type()
)
snmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserName.setStatus("current")


class _SnmpUserVersion_Type(Integer32):
    """Custom type snmpUserVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SnmpUserVersion_Type.__name__ = "Integer32"
_SnmpUserVersion_Object = MibTableColumn
snmpUserVersion = _SnmpUserVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 2),
    _SnmpUserVersion_Type()
)
snmpUserVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserVersion.setStatus("current")


class _SnmpUserGroupName_Type(SnmpAdminString):
    """Custom type snmpUserGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserGroupName_Type.__name__ = "SnmpAdminString"
_SnmpUserGroupName_Object = MibTableColumn
snmpUserGroupName = _SnmpUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 3),
    _SnmpUserGroupName_Type()
)
snmpUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserGroupName.setStatus("current")


class _SnmpUserAuthProtocol_Type(Integer32):
    """Custom type snmpUserAuthProtocol based on Integer32"""
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
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )


_SnmpUserAuthProtocol_Type.__name__ = "Integer32"
_SnmpUserAuthProtocol_Object = MibTableColumn
snmpUserAuthProtocol = _SnmpUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 4),
    _SnmpUserAuthProtocol_Type()
)
snmpUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtocol.setStatus("current")


class _SnmpUserAuthProtocolPassword_Type(SnmpAdminString):
    """Custom type snmpUserAuthProtocolPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserAuthProtocolPassword_Type.__name__ = "SnmpAdminString"
_SnmpUserAuthProtocolPassword_Object = MibTableColumn
snmpUserAuthProtocolPassword = _SnmpUserAuthProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 5),
    _SnmpUserAuthProtocolPassword_Type()
)
snmpUserAuthProtocolPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtocolPassword.setStatus("current")


class _SnmpUserPrivProtocol_Type(Integer32):
    """Custom type snmpUserPrivProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("none", 1))
    )


_SnmpUserPrivProtocol_Type.__name__ = "Integer32"
_SnmpUserPrivProtocol_Object = MibTableColumn
snmpUserPrivProtocol = _SnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 6),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")


class _SnmpUserPrivProtocolPassword_Type(SnmpAdminString):
    """Custom type snmpUserPrivProtocolPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpUserPrivProtocolPassword_Type.__name__ = "SnmpAdminString"
_SnmpUserPrivProtocolPassword_Object = MibTableColumn
snmpUserPrivProtocolPassword = _SnmpUserPrivProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 7),
    _SnmpUserPrivProtocolPassword_Type()
)
snmpUserPrivProtocolPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocolPassword.setStatus("current")
_SnmpUserStatus_Type = RowStatus
_SnmpUserStatus_Object = MibTableColumn
snmpUserStatus = _SnmpUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 2, 1, 1, 8),
    _SnmpUserStatus_Type()
)
snmpUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserStatus.setStatus("current")
_SysSNMPGroup_ObjectIdentity = ObjectIdentity
sysSNMPGroup = _SysSNMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3)
)
_SnmpGroupTable_Object = MibTable
snmpGroupTable = _SnmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    snmpGroupTable.setStatus("current")
_SnmpGroupEntry_Object = MibTableRow
snmpGroupEntry = _SnmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1)
)
snmpGroupEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "snmpGroupName"),
    (0, "DGS-1100-10ME_A1", "snmpGroupSecurityModel"),
    (0, "DGS-1100-10ME_A1", "snmpGroupSecurityLevel"),
)
if mibBuilder.loadTexts:
    snmpGroupEntry.setStatus("current")


class _SnmpGroupName_Type(SnmpAdminString):
    """Custom type snmpGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpGroupName_Type.__name__ = "SnmpAdminString"
_SnmpGroupName_Object = MibTableColumn
snmpGroupName = _SnmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1, 1),
    _SnmpGroupName_Type()
)
snmpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupName.setStatus("current")


class _SnmpGroupSecurityModel_Type(Integer32):
    """Custom type snmpGroupSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SnmpGroupSecurityModel_Type.__name__ = "Integer32"
_SnmpGroupSecurityModel_Object = MibTableColumn
snmpGroupSecurityModel = _SnmpGroupSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1, 2),
    _SnmpGroupSecurityModel_Type()
)
snmpGroupSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupSecurityModel.setStatus("current")


class _SnmpGroupSecurityLevel_Type(Integer32):
    """Custom type snmpGroupSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authNoPriv", 2),
          ("authPriv", 3),
          ("noAuthNoPriv", 1))
    )


_SnmpGroupSecurityLevel_Type.__name__ = "Integer32"
_SnmpGroupSecurityLevel_Object = MibTableColumn
snmpGroupSecurityLevel = _SnmpGroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1, 3),
    _SnmpGroupSecurityLevel_Type()
)
snmpGroupSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupSecurityLevel.setStatus("current")


class _SnmpGroupReadViewName_Type(SnmpAdminString):
    """Custom type snmpGroupReadViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpGroupReadViewName_Type.__name__ = "SnmpAdminString"
_SnmpGroupReadViewName_Object = MibTableColumn
snmpGroupReadViewName = _SnmpGroupReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1, 4),
    _SnmpGroupReadViewName_Type()
)
snmpGroupReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupReadViewName.setStatus("current")


class _SnmpGroupWriteViewName_Type(SnmpAdminString):
    """Custom type snmpGroupWriteViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpGroupWriteViewName_Type.__name__ = "SnmpAdminString"
_SnmpGroupWriteViewName_Object = MibTableColumn
snmpGroupWriteViewName = _SnmpGroupWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1, 5),
    _SnmpGroupWriteViewName_Type()
)
snmpGroupWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupWriteViewName.setStatus("current")


class _SnmpGroupNotifyViewName_Type(SnmpAdminString):
    """Custom type snmpGroupNotifyViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpGroupNotifyViewName_Type.__name__ = "SnmpAdminString"
_SnmpGroupNotifyViewName_Object = MibTableColumn
snmpGroupNotifyViewName = _SnmpGroupNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1, 6),
    _SnmpGroupNotifyViewName_Type()
)
snmpGroupNotifyViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupNotifyViewName.setStatus("current")
_SnmpGroupStatus_Type = RowStatus
_SnmpGroupStatus_Object = MibTableColumn
snmpGroupStatus = _SnmpGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 3, 1, 1, 7),
    _SnmpGroupStatus_Type()
)
snmpGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGroupStatus.setStatus("current")
_SysSNMPViewTree_ObjectIdentity = ObjectIdentity
sysSNMPViewTree = _SysSNMPViewTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4)
)
_SnmpViewTreeTable_Object = MibTable
snmpViewTreeTable = _SnmpViewTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    snmpViewTreeTable.setStatus("current")
_SnmpViewTreeEntry_Object = MibTableRow
snmpViewTreeEntry = _SnmpViewTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4, 1, 1)
)
snmpViewTreeEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "snmpViewTreeName"),
    (0, "DGS-1100-10ME_A1", "snmpViewTreeSubtree"),
)
if mibBuilder.loadTexts:
    snmpViewTreeEntry.setStatus("current")


class _SnmpViewTreeName_Type(SnmpAdminString):
    """Custom type snmpViewTreeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpViewTreeName_Type.__name__ = "SnmpAdminString"
_SnmpViewTreeName_Object = MibTableColumn
snmpViewTreeName = _SnmpViewTreeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4, 1, 1, 1),
    _SnmpViewTreeName_Type()
)
snmpViewTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpViewTreeName.setStatus("current")
_SnmpViewTreeSubtree_Type = ObjectIdentifier
_SnmpViewTreeSubtree_Object = MibTableColumn
snmpViewTreeSubtree = _SnmpViewTreeSubtree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4, 1, 1, 2),
    _SnmpViewTreeSubtree_Type()
)
snmpViewTreeSubtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpViewTreeSubtree.setStatus("current")


class _SnmpViewTreeMask_Type(OctetString):
    """Custom type snmpViewTreeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpViewTreeMask_Type.__name__ = "OctetString"
_SnmpViewTreeMask_Object = MibTableColumn
snmpViewTreeMask = _SnmpViewTreeMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4, 1, 1, 3),
    _SnmpViewTreeMask_Type()
)
snmpViewTreeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpViewTreeMask.setStatus("current")


class _SnmpViewTreeType_Type(Integer32):
    """Custom type snmpViewTreeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_SnmpViewTreeType_Type.__name__ = "Integer32"
_SnmpViewTreeType_Object = MibTableColumn
snmpViewTreeType = _SnmpViewTreeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4, 1, 1, 4),
    _SnmpViewTreeType_Type()
)
snmpViewTreeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpViewTreeType.setStatus("current")
_SnmpViewTreeStatus_Type = RowStatus
_SnmpViewTreeStatus_Object = MibTableColumn
snmpViewTreeStatus = _SnmpViewTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 4, 1, 1, 5),
    _SnmpViewTreeStatus_Type()
)
snmpViewTreeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpViewTreeStatus.setStatus("current")
_SysSNMPCommunity_ObjectIdentity = ObjectIdentity
sysSNMPCommunity = _SysSNMPCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 5)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 5, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "snmpCommunityName"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")
_SnmpCommunityName_Type = SnmpAdminString
_SnmpCommunityName_Object = MibTableColumn
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 5, 1, 1, 1),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("current")


class _SnmpCommunityPolicy_Type(SnmpAdminString):
    """Custom type snmpCommunityPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpCommunityPolicy_Type.__name__ = "SnmpAdminString"
_SnmpCommunityPolicy_Object = MibTableColumn
snmpCommunityPolicy = _SnmpCommunityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 5, 1, 1, 2),
    _SnmpCommunityPolicy_Type()
)
snmpCommunityPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityPolicy.setStatus("current")
_SnmpCommunityStatus_Type = RowStatus
_SnmpCommunityStatus_Object = MibTableColumn
snmpCommunityStatus = _SnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 5, 1, 1, 3),
    _SnmpCommunityStatus_Type()
)
snmpCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityStatus.setStatus("current")
_SysSNMPHost_ObjectIdentity = ObjectIdentity
sysSNMPHost = _SysSNMPHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6)
)
_SnmpHostTable_Object = MibTable
snmpHostTable = _SnmpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6, 1)
)
if mibBuilder.loadTexts:
    snmpHostTable.setStatus("current")
_SnmpHostEntry_Object = MibTableRow
snmpHostEntry = _SnmpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6, 1, 1)
)
snmpHostEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "snmpHostAddress"),
    (0, "DGS-1100-10ME_A1", "snmpHostIPType"),
)
if mibBuilder.loadTexts:
    snmpHostEntry.setStatus("current")
_SnmpHostAddress_Type = InetAddress
_SnmpHostAddress_Object = MibTableColumn
snmpHostAddress = _SnmpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6, 1, 1, 1),
    _SnmpHostAddress_Type()
)
snmpHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpHostAddress.setStatus("current")


class _SnmpHostIPType_Type(Integer32):
    """Custom type snmpHostIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2))
    )


_SnmpHostIPType_Type.__name__ = "Integer32"
_SnmpHostIPType_Object = MibTableColumn
snmpHostIPType = _SnmpHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6, 1, 1, 2),
    _SnmpHostIPType_Type()
)
snmpHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpHostIPType.setStatus("current")


class _SnmpHostCommunityName_Type(SnmpAdminString):
    """Custom type snmpHostCommunityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpHostCommunityName_Type.__name__ = "SnmpAdminString"
_SnmpHostCommunityName_Object = MibTableColumn
snmpHostCommunityName = _SnmpHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6, 1, 1, 3),
    _SnmpHostCommunityName_Type()
)
snmpHostCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHostCommunityName.setStatus("current")


class _SnmpHostVersion_Type(Integer32):
    """Custom type snmpHostVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2c", 2),
          ("v3-AuthNoPriv", 4),
          ("v3-AuthPriv", 5),
          ("v3-NoAuthNoPriv", 3))
    )


_SnmpHostVersion_Type.__name__ = "Integer32"
_SnmpHostVersion_Object = MibTableColumn
snmpHostVersion = _SnmpHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6, 1, 1, 4),
    _SnmpHostVersion_Type()
)
snmpHostVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHostVersion.setStatus("current")
_SnmpHostStatus_Type = RowStatus
_SnmpHostStatus_Object = MibTableColumn
snmpHostStatus = _SnmpHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 6, 1, 1, 6),
    _SnmpHostStatus_Type()
)
snmpHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHostStatus.setStatus("current")
_SysSNMPEngineID_Type = SnmpEngineID
_SysSNMPEngineID_Object = MibScalar
sysSNMPEngineID = _SysSNMPEngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 7),
    _SysSNMPEngineID_Type()
)
sysSNMPEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNMPEngineID.setStatus("current")
_SysSNMPTrap_ObjectIdentity = ObjectIdentity
sysSNMPTrap = _SysSNMPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8)
)


class _SnmpTrapSNMPAuthentication_Type(Integer32):
    """Custom type snmpTrapSNMPAuthentication based on Integer32"""
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


_SnmpTrapSNMPAuthentication_Type.__name__ = "Integer32"
_SnmpTrapSNMPAuthentication_Object = MibScalar
snmpTrapSNMPAuthentication = _SnmpTrapSNMPAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 1),
    _SnmpTrapSNMPAuthentication_Type()
)
snmpTrapSNMPAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSNMPAuthentication.setStatus("current")


class _SnmpTrapColdStart_Type(Integer32):
    """Custom type snmpTrapColdStart based on Integer32"""
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


_SnmpTrapColdStart_Type.__name__ = "Integer32"
_SnmpTrapColdStart_Object = MibScalar
snmpTrapColdStart = _SnmpTrapColdStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 2),
    _SnmpTrapColdStart_Type()
)
snmpTrapColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapColdStart.setStatus("current")


class _SnmpTrapWarmStart_Type(Integer32):
    """Custom type snmpTrapWarmStart based on Integer32"""
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


_SnmpTrapWarmStart_Type.__name__ = "Integer32"
_SnmpTrapWarmStart_Object = MibScalar
snmpTrapWarmStart = _SnmpTrapWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 3),
    _SnmpTrapWarmStart_Type()
)
snmpTrapWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapWarmStart.setStatus("current")


class _SnmpTrapFiberLinkUpDown_Type(Integer32):
    """Custom type snmpTrapFiberLinkUpDown based on Integer32"""
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


_SnmpTrapFiberLinkUpDown_Type.__name__ = "Integer32"
_SnmpTrapFiberLinkUpDown_Object = MibScalar
snmpTrapFiberLinkUpDown = _SnmpTrapFiberLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 4),
    _SnmpTrapFiberLinkUpDown_Type()
)
snmpTrapFiberLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapFiberLinkUpDown.setStatus("current")


class _SnmpTrapTwistLinkUpDown_Type(Integer32):
    """Custom type snmpTrapTwistLinkUpDown based on Integer32"""
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


_SnmpTrapTwistLinkUpDown_Type.__name__ = "Integer32"
_SnmpTrapTwistLinkUpDown_Object = MibScalar
snmpTrapTwistLinkUpDown = _SnmpTrapTwistLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 5),
    _SnmpTrapTwistLinkUpDown_Type()
)
snmpTrapTwistLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapTwistLinkUpDown.setStatus("current")


class _SnmpTrapFirmwareUpgrade_Type(Integer32):
    """Custom type snmpTrapFirmwareUpgrade based on Integer32"""
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


_SnmpTrapFirmwareUpgrade_Type.__name__ = "Integer32"
_SnmpTrapFirmwareUpgrade_Object = MibScalar
snmpTrapFirmwareUpgrade = _SnmpTrapFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 6),
    _SnmpTrapFirmwareUpgrade_Type()
)
snmpTrapFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapFirmwareUpgrade.setStatus("current")


class _SnmpTrapPortSecViolation_Type(Integer32):
    """Custom type snmpTrapPortSecViolation based on Integer32"""
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


_SnmpTrapPortSecViolation_Type.__name__ = "Integer32"
_SnmpTrapPortSecViolation_Object = MibScalar
snmpTrapPortSecViolation = _SnmpTrapPortSecViolation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 7),
    _SnmpTrapPortSecViolation_Type()
)
snmpTrapPortSecViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapPortSecViolation.setStatus("current")


class _SnmpTrapLBDDetection_Type(Integer32):
    """Custom type snmpTrapLBDDetection based on Integer32"""
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


_SnmpTrapLBDDetection_Type.__name__ = "Integer32"
_SnmpTrapLBDDetection_Object = MibScalar
snmpTrapLBDDetection = _SnmpTrapLBDDetection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 8),
    _SnmpTrapLBDDetection_Type()
)
snmpTrapLBDDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapLBDDetection.setStatus("current")


class _SnmpTrapDuplicateIPDetected_Type(Integer32):
    """Custom type snmpTrapDuplicateIPDetected based on Integer32"""
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


_SnmpTrapDuplicateIPDetected_Type.__name__ = "Integer32"
_SnmpTrapDuplicateIPDetected_Object = MibScalar
snmpTrapDuplicateIPDetected = _SnmpTrapDuplicateIPDetected_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 5, 8, 9),
    _SnmpTrapDuplicateIPDetected_Type()
)
snmpTrapDuplicateIPDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDuplicateIPDetected.setStatus("current")
_CompanyDot1qVlanGroup_ObjectIdentity = ObjectIdentity
companyDot1qVlanGroup = _CompanyDot1qVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7)
)


class _SysDot1qVlanManagementOnOff_Type(Integer32):
    """Custom type sysDot1qVlanManagementOnOff based on Integer32"""
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


_SysDot1qVlanManagementOnOff_Type.__name__ = "Integer32"
_SysDot1qVlanManagementOnOff_Object = MibScalar
sysDot1qVlanManagementOnOff = _SysDot1qVlanManagementOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 2),
    _SysDot1qVlanManagementOnOff_Type()
)
sysDot1qVlanManagementOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDot1qVlanManagementOnOff.setStatus("current")


class _SysDot1qVlanManagementid_Type(Integer32):
    """Custom type sysDot1qVlanManagementid based on Integer32"""
    defaultValue = 1


_SysDot1qVlanManagementid_Object = MibScalar
sysDot1qVlanManagementid = _SysDot1qVlanManagementid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 3),
    _SysDot1qVlanManagementid_Type()
)
sysDot1qVlanManagementid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDot1qVlanManagementid.setStatus("current")


class _SysDot1qPVIDAutoAssign_Type(Integer32):
    """Custom type sysDot1qPVIDAutoAssign based on Integer32"""
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


_SysDot1qPVIDAutoAssign_Type.__name__ = "Integer32"
_SysDot1qPVIDAutoAssign_Object = MibScalar
sysDot1qPVIDAutoAssign = _SysDot1qPVIDAutoAssign_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 4),
    _SysDot1qPVIDAutoAssign_Type()
)
sysDot1qPVIDAutoAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDot1qPVIDAutoAssign.setStatus("current")


class _SysDot1qVlanAsyOnOff_Type(Integer32):
    """Custom type sysDot1qVlanAsyOnOff based on Integer32"""
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


_SysDot1qVlanAsyOnOff_Type.__name__ = "Integer32"
_SysDot1qVlanAsyOnOff_Object = MibScalar
sysDot1qVlanAsyOnOff = _SysDot1qVlanAsyOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 5),
    _SysDot1qVlanAsyOnOff_Type()
)
sysDot1qVlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDot1qVlanAsyOnOff.setStatus("current")
_SysDot1qVlanTable_Object = MibTable
sysDot1qVlanTable = _SysDot1qVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    sysDot1qVlanTable.setStatus("current")
_Dot1qVlanEntry_Object = MibTableRow
dot1qVlanEntry = _Dot1qVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 6, 1)
)
dot1qVlanEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "dot1qVlanid"),
)
if mibBuilder.loadTexts:
    dot1qVlanEntry.setStatus("current")


class _Dot1qVlanid_Type(Integer32):
    """Custom type dot1qVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot1qVlanid_Type.__name__ = "Integer32"
_Dot1qVlanid_Object = MibTableColumn
dot1qVlanid = _Dot1qVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 6, 1, 1),
    _Dot1qVlanid_Type()
)
dot1qVlanid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanid.setStatus("current")


class _Dot1qVlanName_Type(SnmpAdminString):
    """Custom type dot1qVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Dot1qVlanName_Type.__name__ = "SnmpAdminString"
_Dot1qVlanName_Object = MibTableColumn
dot1qVlanName = _Dot1qVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 6, 1, 2),
    _Dot1qVlanName_Type()
)
dot1qVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanName.setStatus("current")
_Dot1qVlanEgressPorts_Type = PortList
_Dot1qVlanEgressPorts_Object = MibTableColumn
dot1qVlanEgressPorts = _Dot1qVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 6, 1, 3),
    _Dot1qVlanEgressPorts_Type()
)
dot1qVlanEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanEgressPorts.setStatus("current")
_Dot1qVlanUntaggedPorts_Type = PortList
_Dot1qVlanUntaggedPorts_Object = MibTableColumn
dot1qVlanUntaggedPorts = _Dot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 6, 1, 4),
    _Dot1qVlanUntaggedPorts_Type()
)
dot1qVlanUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanUntaggedPorts.setStatus("current")
_Dot1qVlanRowStatus_Type = RowStatus
_Dot1qVlanRowStatus_Object = MibTableColumn
dot1qVlanRowStatus = _Dot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 6, 1, 5),
    _Dot1qVlanRowStatus_Type()
)
dot1qVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanRowStatus.setStatus("current")
_SysDot1qVlanPortTable_Object = MibTable
sysDot1qVlanPortTable = _SysDot1qVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 7)
)
if mibBuilder.loadTexts:
    sysDot1qVlanPortTable.setStatus("current")
_Dot1qVlanPortEntry_Object = MibTableRow
dot1qVlanPortEntry = _Dot1qVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 7, 1)
)
dot1qVlanPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "dot1qVlanPortIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanPortEntry.setStatus("current")
_Dot1qVlanPortIndex_Type = Integer32
_Dot1qVlanPortIndex_Object = MibTableColumn
dot1qVlanPortIndex = _Dot1qVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 7, 1, 1),
    _Dot1qVlanPortIndex_Type()
)
dot1qVlanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanPortIndex.setStatus("current")


class _Dot1qVlanPortVlanId_Type(VlanIndex):
    """Custom type dot1qVlanPortVlanId based on VlanIndex"""
    defaultValue = 1


_Dot1qVlanPortVlanId_Object = MibTableColumn
dot1qVlanPortVlanId = _Dot1qVlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 7, 7, 1, 2),
    _Dot1qVlanPortVlanId_Type()
)
dot1qVlanPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPortVlanId.setStatus("current")
_CompanyStaticMac_ObjectIdentity = ObjectIdentity
companyStaticMac = _CompanyStaticMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9)
)
_SysStaticMacTable_Object = MibTable
sysStaticMacTable = _SysStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    sysStaticMacTable.setStatus("current")
_StaticMacEntry_Object = MibTableRow
staticMacEntry = _StaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 1, 1)
)
staticMacEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "staticMacVlanID"),
    (0, "DGS-1100-10ME_A1", "staticMacAddr"),
)
if mibBuilder.loadTexts:
    staticMacEntry.setStatus("current")
_StaticMacVlanID_Type = Integer32
_StaticMacVlanID_Object = MibTableColumn
staticMacVlanID = _StaticMacVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 1, 1, 1),
    _StaticMacVlanID_Type()
)
staticMacVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMacVlanID.setStatus("current")
_StaticMacAddr_Type = MacAddress
_StaticMacAddr_Object = MibTableColumn
staticMacAddr = _StaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 1, 1, 2),
    _StaticMacAddr_Type()
)
staticMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMacAddr.setStatus("current")
_StaticMacPort_Type = Integer32
_StaticMacPort_Object = MibTableColumn
staticMacPort = _StaticMacPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 1, 1, 3),
    _StaticMacPort_Type()
)
staticMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacPort.setStatus("current")
_StaticMacStatus_Type = RowStatus
_StaticMacStatus_Object = MibTableColumn
staticMacStatus = _StaticMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 1, 1, 4),
    _StaticMacStatus_Type()
)
staticMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacStatus.setStatus("current")
_SysDynamicFdbTable_Object = MibTable
sysDynamicFdbTable = _SysDynamicFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    sysDynamicFdbTable.setStatus("current")
_SysDynamicFdbEntry_Object = MibTableRow
sysDynamicFdbEntry = _SysDynamicFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 2, 1)
)
sysDynamicFdbEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "dynamicFdbId"),
    (0, "DGS-1100-10ME_A1", "dynamicFdbMacAddr"),
)
if mibBuilder.loadTexts:
    sysDynamicFdbEntry.setStatus("current")
_DynamicFdbId_Type = Unsigned32
_DynamicFdbId_Object = MibTableColumn
dynamicFdbId = _DynamicFdbId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 2, 1, 1),
    _DynamicFdbId_Type()
)
dynamicFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicFdbId.setStatus("current")
_DynamicFdbMacAddr_Type = MacAddress
_DynamicFdbMacAddr_Object = MibTableColumn
dynamicFdbMacAddr = _DynamicFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 2, 1, 2),
    _DynamicFdbMacAddr_Type()
)
dynamicFdbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicFdbMacAddr.setStatus("current")
_DynamicFdbPort_Type = DisplayString
_DynamicFdbPort_Object = MibTableColumn
dynamicFdbPort = _DynamicFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 2, 1, 3),
    _DynamicFdbPort_Type()
)
dynamicFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicFdbPort.setStatus("current")


class _DynamicFdbStatus_Type(Integer32):
    """Custom type dynamicFdbStatus based on Integer32"""
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
        *(("deleteOnReset", 6),
          ("deleteOnTimeout", 7),
          ("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 8),
          ("self", 4),
          ("static", 5))
    )


_DynamicFdbStatus_Type.__name__ = "Integer32"
_DynamicFdbStatus_Object = MibTableColumn
dynamicFdbStatus = _DynamicFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 2, 1, 4),
    _DynamicFdbStatus_Type()
)
dynamicFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynamicFdbStatus.setStatus("current")
_SysFdbClear_ObjectIdentity = ObjectIdentity
sysFdbClear = _SysFdbClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 3)
)
_SysFdbClearId_Type = Unsigned32
_SysFdbClearId_Object = MibScalar
sysFdbClearId = _SysFdbClearId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 3, 1),
    _SysFdbClearId_Type()
)
sysFdbClearId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFdbClearId.setStatus("current")


class _SysFdbClearAction_Type(Integer32):
    """Custom type sysFdbClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 1),
          ("clearByPort", 3),
          ("clearByVlanId", 2))
    )


_SysFdbClearAction_Type.__name__ = "Integer32"
_SysFdbClearAction_Object = MibScalar
sysFdbClearAction = _SysFdbClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 9, 3, 2),
    _SysFdbClearAction_Type()
)
sysFdbClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFdbClearAction.setStatus("current")
_CompanyIgsGroup_ObjectIdentity = ObjectIdentity
companyIgsGroup = _CompanyIgsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10)
)
_SysIgsSystem_ObjectIdentity = ObjectIdentity
sysIgsSystem = _SysIgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 1)
)


class _IgsStatus_Type(Integer32):
    """Custom type igsStatus based on Integer32"""
    defaultValue = 2

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


_IgsStatus_Type.__name__ = "Integer32"
_IgsStatus_Object = MibScalar
igsStatus = _IgsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 1, 1),
    _IgsStatus_Type()
)
igsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsStatus.setStatus("current")


class _IgsReportForwardRouterOnly_Type(Integer32):
    """Custom type igsReportForwardRouterOnly based on Integer32"""
    defaultValue = 1

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


_IgsReportForwardRouterOnly_Type.__name__ = "Integer32"
_IgsReportForwardRouterOnly_Object = MibScalar
igsReportForwardRouterOnly = _IgsReportForwardRouterOnly_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 1, 8),
    _IgsReportForwardRouterOnly_Type()
)
igsReportForwardRouterOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsReportForwardRouterOnly.setStatus("current")
_SysIgsVlan_ObjectIdentity = ObjectIdentity
sysIgsVlan = _SysIgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3)
)
_IgsVlanRouterTable_Object = MibTable
igsVlanRouterTable = _IgsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    igsVlanRouterTable.setStatus("current")
_IgsVlanRouterEntry_Object = MibTableRow
igsVlanRouterEntry = _IgsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 3, 1)
)
igsVlanRouterEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "igsVlanRouterVlanId"),
)
if mibBuilder.loadTexts:
    igsVlanRouterEntry.setStatus("current")


class _IgsVlanRouterVlanId_Type(Integer32):
    """Custom type igsVlanRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanRouterVlanId_Type.__name__ = "Integer32"
_IgsVlanRouterVlanId_Object = MibTableColumn
igsVlanRouterVlanId = _IgsVlanRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 3, 1, 1),
    _IgsVlanRouterVlanId_Type()
)
igsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterVlanId.setStatus("current")
_IgsVlanRouterStaticPortList_Type = PortList
_IgsVlanRouterStaticPortList_Object = MibTableColumn
igsVlanRouterStaticPortList = _IgsVlanRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 3, 1, 2),
    _IgsVlanRouterStaticPortList_Type()
)
igsVlanRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRouterStaticPortList.setStatus("current")
_IgsVlanRouterDynamicPortList_Type = PortList
_IgsVlanRouterDynamicPortList_Object = MibTableColumn
igsVlanRouterDynamicPortList = _IgsVlanRouterDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 3, 1, 3),
    _IgsVlanRouterDynamicPortList_Type()
)
igsVlanRouterDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterDynamicPortList.setStatus("current")
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("current")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "igsVlanFilterVlanId"),
)
if mibBuilder.loadTexts:
    igsVlanFilterEntry.setStatus("current")


class _IgsVlanFilterVlanId_Type(Integer32):
    """Custom type igsVlanFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanFilterVlanId_Type.__name__ = "Integer32"
_IgsVlanFilterVlanId_Object = MibTableColumn
igsVlanFilterVlanId = _IgsVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 1),
    _IgsVlanFilterVlanId_Type()
)
igsVlanFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanFilterVlanId.setStatus("current")


class _IgsVlanSnoopStatus_Type(Integer32):
    """Custom type igsVlanSnoopStatus based on Integer32"""
    defaultValue = 2

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


_IgsVlanSnoopStatus_Type.__name__ = "Integer32"
_IgsVlanSnoopStatus_Object = MibTableColumn
igsVlanSnoopStatus = _IgsVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 2),
    _IgsVlanSnoopStatus_Type()
)
igsVlanSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanSnoopStatus.setStatus("current")


class _IgsVlanQuerier_Type(Integer32):
    """Custom type igsVlanQuerier based on Integer32"""
    defaultValue = 2

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


_IgsVlanQuerier_Type.__name__ = "Integer32"
_IgsVlanQuerier_Object = MibTableColumn
igsVlanQuerier = _IgsVlanQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 3),
    _IgsVlanQuerier_Type()
)
igsVlanQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanQuerier.setStatus("current")


class _IgsVlanCfgQuerier_Type(Integer32):
    """Custom type igsVlanCfgQuerier based on Integer32"""
    defaultValue = 2

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


_IgsVlanCfgQuerier_Type.__name__ = "Integer32"
_IgsVlanCfgQuerier_Object = MibTableColumn
igsVlanCfgQuerier = _IgsVlanCfgQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 4),
    _IgsVlanCfgQuerier_Type()
)
igsVlanCfgQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanCfgQuerier.setStatus("current")


class _IgsVlanQueryInterval_Type(Integer32):
    """Custom type igsVlanQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_IgsVlanQueryInterval_Type.__name__ = "Integer32"
_IgsVlanQueryInterval_Object = MibTableColumn
igsVlanQueryInterval = _IgsVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 5),
    _IgsVlanQueryInterval_Type()
)
igsVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanQueryInterval.setStatus("current")


class _IgsVlanFastLeave_Type(Integer32):
    """Custom type igsVlanFastLeave based on Integer32"""
    defaultValue = 2

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


_IgsVlanFastLeave_Type.__name__ = "Integer32"
_IgsVlanFastLeave_Object = MibTableColumn
igsVlanFastLeave = _IgsVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 6),
    _IgsVlanFastLeave_Type()
)
igsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFastLeave.setStatus("current")


class _IgsVlanQuerierVersion_Type(Integer32):
    """Custom type igsVlanQuerierVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmp_v1", 1),
          ("igmp_v2", 2),
          ("igmp_v3", 3))
    )


_IgsVlanQuerierVersion_Type.__name__ = "Integer32"
_IgsVlanQuerierVersion_Object = MibTableColumn
igsVlanQuerierVersion = _IgsVlanQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 7),
    _IgsVlanQuerierVersion_Type()
)
igsVlanQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanQuerierVersion.setStatus("current")


class _IgsVlanRouterPortPurgeInterval_Type(Integer32):
    """Custom type igsVlanRouterPortPurgeInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_IgsVlanRouterPortPurgeInterval_Type.__name__ = "Integer32"
_IgsVlanRouterPortPurgeInterval_Object = MibTableColumn
igsVlanRouterPortPurgeInterval = _IgsVlanRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 8),
    _IgsVlanRouterPortPurgeInterval_Type()
)
igsVlanRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRouterPortPurgeInterval.setStatus("current")


class _IgsVlanHostPortPurgeInterval_Type(Integer32):
    """Custom type igsVlanHostPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 153025),
    )


_IgsVlanHostPortPurgeInterval_Type.__name__ = "Integer32"
_IgsVlanHostPortPurgeInterval_Object = MibTableColumn
igsVlanHostPortPurgeInterval = _IgsVlanHostPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 9),
    _IgsVlanHostPortPurgeInterval_Type()
)
igsVlanHostPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanHostPortPurgeInterval.setStatus("current")


class _IgsVlanRobustnessValue_Type(Integer32):
    """Custom type igsVlanRobustnessValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_IgsVlanRobustnessValue_Type.__name__ = "Integer32"
_IgsVlanRobustnessValue_Object = MibTableColumn
igsVlanRobustnessValue = _IgsVlanRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 10),
    _IgsVlanRobustnessValue_Type()
)
igsVlanRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRobustnessValue.setStatus("current")


class _IgsVlanGrpQueryInterval_Type(Integer32):
    """Custom type igsVlanGrpQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_IgsVlanGrpQueryInterval_Type.__name__ = "Integer32"
_IgsVlanGrpQueryInterval_Object = MibTableColumn
igsVlanGrpQueryInterval = _IgsVlanGrpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 11),
    _IgsVlanGrpQueryInterval_Type()
)
igsVlanGrpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanGrpQueryInterval.setStatus("current")


class _IgsVlanQueryMaxResponseTime_Type(Integer32):
    """Custom type igsVlanQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 25),
    )


_IgsVlanQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgsVlanQueryMaxResponseTime_Object = MibTableColumn
igsVlanQueryMaxResponseTime = _IgsVlanQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 4, 1, 12),
    _IgsVlanQueryMaxResponseTime_Type()
)
igsVlanQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanQueryMaxResponseTime.setStatus("current")
_IgsVlanMulticastGroupTable_Object = MibTable
igsVlanMulticastGroupTable = _IgsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 5)
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupTable.setStatus("current")
_IgsVlanMulticastGroupEntry_Object = MibTableRow
igsVlanMulticastGroupEntry = _IgsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 5, 1)
)
igsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "igsVlanMulticastGroupVlanId"),
    (0, "DGS-1100-10ME_A1", "igsVlanMulticastGroupIpAddress"),
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupEntry.setStatus("current")


class _IgsVlanMulticastGroupVlanId_Type(Integer32):
    """Custom type igsVlanMulticastGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanMulticastGroupVlanId_Type.__name__ = "Integer32"
_IgsVlanMulticastGroupVlanId_Object = MibTableColumn
igsVlanMulticastGroupVlanId = _IgsVlanMulticastGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 5, 1, 1),
    _IgsVlanMulticastGroupVlanId_Type()
)
igsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupVlanId.setStatus("current")
_IgsVlanMulticastGroupIpAddress_Type = IpAddress
_IgsVlanMulticastGroupIpAddress_Object = MibTableColumn
igsVlanMulticastGroupIpAddress = _IgsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 5, 1, 2),
    _IgsVlanMulticastGroupIpAddress_Type()
)
igsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupIpAddress.setStatus("current")
_IgsVlanMulticastGroupMacAddress_Type = MacAddress
_IgsVlanMulticastGroupMacAddress_Object = MibTableColumn
igsVlanMulticastGroupMacAddress = _IgsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 5, 1, 3),
    _IgsVlanMulticastGroupMacAddress_Type()
)
igsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupMacAddress.setStatus("current")
_IgsVlanMulticastGroupPortList_Type = PortList
_IgsVlanMulticastGroupPortList_Object = MibTableColumn
igsVlanMulticastGroupPortList = _IgsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 3, 5, 1, 4),
    _IgsVlanMulticastGroupPortList_Type()
)
igsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupPortList.setStatus("current")
_SysIgsAccessAuth_ObjectIdentity = ObjectIdentity
sysIgsAccessAuth = _SysIgsAccessAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 5)
)
_IgsAccessAuthTable_Object = MibTable
igsAccessAuthTable = _IgsAccessAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    igsAccessAuthTable.setStatus("current")
_IgsAccessAuthEntry_Object = MibTableRow
igsAccessAuthEntry = _IgsAccessAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 5, 1, 1)
)
igsAccessAuthEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "igsAccessAuthPortIndex"),
)
if mibBuilder.loadTexts:
    igsAccessAuthEntry.setStatus("current")
_IgsAccessAuthPortIndex_Type = Integer32
_IgsAccessAuthPortIndex_Object = MibTableColumn
igsAccessAuthPortIndex = _IgsAccessAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 5, 1, 1, 1),
    _IgsAccessAuthPortIndex_Type()
)
igsAccessAuthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsAccessAuthPortIndex.setStatus("current")


class _IgsAccessAuthState_Type(Integer32):
    """Custom type igsAccessAuthState based on Integer32"""
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


_IgsAccessAuthState_Type.__name__ = "Integer32"
_IgsAccessAuthState_Object = MibTableColumn
igsAccessAuthState = _IgsAccessAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 5, 1, 1, 2),
    _IgsAccessAuthState_Type()
)
igsAccessAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsAccessAuthState.setStatus("current")
_SysIgsHost_ObjectIdentity = ObjectIdentity
sysIgsHost = _SysIgsHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 6)
)
_IgsHostTable_Object = MibTable
igsHostTable = _IgsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 6, 1)
)
if mibBuilder.loadTexts:
    igsHostTable.setStatus("current")
_IgsHostEntry_Object = MibTableRow
igsHostEntry = _IgsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 6, 1, 1)
)
igsHostEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "igsHostTableVlanId"),
    (0, "DGS-1100-10ME_A1", "igsHostTableGroupAddress"),
    (0, "DGS-1100-10ME_A1", "igsHostTablePort"),
    (0, "DGS-1100-10ME_A1", "igsHostTableHostIPAddress"),
)
if mibBuilder.loadTexts:
    igsHostEntry.setStatus("current")


class _IgsHostTableVlanId_Type(Integer32):
    """Custom type igsHostTableVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsHostTableVlanId_Type.__name__ = "Integer32"
_IgsHostTableVlanId_Object = MibTableColumn
igsHostTableVlanId = _IgsHostTableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 6, 1, 1, 1),
    _IgsHostTableVlanId_Type()
)
igsHostTableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableVlanId.setStatus("current")
_IgsHostTableGroupAddress_Type = IpAddress
_IgsHostTableGroupAddress_Object = MibTableColumn
igsHostTableGroupAddress = _IgsHostTableGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 6, 1, 1, 2),
    _IgsHostTableGroupAddress_Type()
)
igsHostTableGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableGroupAddress.setStatus("current")
_IgsHostTablePort_Type = Integer32
_IgsHostTablePort_Object = MibTableColumn
igsHostTablePort = _IgsHostTablePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 6, 1, 1, 3),
    _IgsHostTablePort_Type()
)
igsHostTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTablePort.setStatus("current")
_IgsHostTableHostIPAddress_Type = IpAddress
_IgsHostTableHostIPAddress_Object = MibTableColumn
igsHostTableHostIPAddress = _IgsHostTableHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 10, 6, 1, 1, 4),
    _IgsHostTableHostIPAddress_Type()
)
igsHostTableHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableHostIPAddress.setStatus("current")
_CompanyQoSGroup_ObjectIdentity = ObjectIdentity
companyQoSGroup = _CompanyQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12)
)


class _SysQosMode_Type(Integer32):
    """Custom type sysQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 1),
          ("dscp", 2),
          ("portbase", 3))
    )


_SysQosMode_Type.__name__ = "Integer32"
_SysQosMode_Object = MibScalar
sysQosMode = _SysQosMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 1),
    _SysQosMode_Type()
)
sysQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysQosMode.setStatus("current")


class _SysQosQueuingMechanism_Type(Integer32):
    """Custom type sysQosQueuingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 1),
          ("wrr", 2))
    )


_SysQosQueuingMechanism_Type.__name__ = "Integer32"
_SysQosQueuingMechanism_Object = MibScalar
sysQosQueuingMechanism = _SysQosQueuingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 2),
    _SysQosQueuingMechanism_Type()
)
sysQosQueuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysQosQueuingMechanism.setStatus("current")
_SysQosPortBase_ObjectIdentity = ObjectIdentity
sysQosPortBase = _SysQosPortBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 3)
)
_QosPortBaseTable_Object = MibTable
qosPortBaseTable = _QosPortBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    qosPortBaseTable.setStatus("current")
_QosPortBaseEntry_Object = MibTableRow
qosPortBaseEntry = _QosPortBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 3, 1, 1)
)
qosPortBaseEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "qosPortBasePortIndex"),
)
if mibBuilder.loadTexts:
    qosPortBaseEntry.setStatus("current")
_QosPortBasePortIndex_Type = Integer32
_QosPortBasePortIndex_Object = MibTableColumn
qosPortBasePortIndex = _QosPortBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 3, 1, 1, 1),
    _QosPortBasePortIndex_Type()
)
qosPortBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPortBasePortIndex.setStatus("current")


class _QosPortBasePriority_Type(Integer32):
    """Custom type qosPortBasePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPortBasePriority_Type.__name__ = "Integer32"
_QosPortBasePriority_Object = MibTableColumn
qosPortBasePriority = _QosPortBasePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 3, 1, 1, 2),
    _QosPortBasePriority_Type()
)
qosPortBasePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortBasePriority.setStatus("current")


class _QosPortBaseEffectivePriority_Type(Integer32):
    """Custom type qosPortBaseEffectivePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPortBaseEffectivePriority_Type.__name__ = "Integer32"
_QosPortBaseEffectivePriority_Object = MibTableColumn
qosPortBaseEffectivePriority = _QosPortBaseEffectivePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 3, 1, 1, 3),
    _QosPortBaseEffectivePriority_Type()
)
qosPortBaseEffectivePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPortBaseEffectivePriority.setStatus("current")
_SysQos1p_ObjectIdentity = ObjectIdentity
sysQos1p = _SysQos1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 4)
)
_QosTrafficClassTable_Object = MibTable
qosTrafficClassTable = _QosTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 4, 1)
)
if mibBuilder.loadTexts:
    qosTrafficClassTable.setStatus("current")
_QosTrafficClassEntry_Object = MibTableRow
qosTrafficClassEntry = _QosTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 4, 1, 1)
)
qosTrafficClassEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "qosTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    qosTrafficClassEntry.setStatus("current")


class _QosTrafficClassPriority_Type(Integer32):
    """Custom type qosTrafficClassPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTrafficClassPriority_Type.__name__ = "Integer32"
_QosTrafficClassPriority_Object = MibTableColumn
qosTrafficClassPriority = _QosTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 4, 1, 1, 1),
    _QosTrafficClassPriority_Type()
)
qosTrafficClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficClassPriority.setStatus("current")


class _QosTrafficClass_Type(Integer32):
    """Custom type qosTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTrafficClass_Type.__name__ = "Integer32"
_QosTrafficClass_Object = MibTableColumn
qosTrafficClass = _QosTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 4, 1, 1, 2),
    _QosTrafficClass_Type()
)
qosTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficClass.setStatus("current")
_SysQosScheduling_ObjectIdentity = ObjectIdentity
sysQosScheduling = _SysQosScheduling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 5)
)
_QosSchedulingClassTable_Object = MibTable
qosSchedulingClassTable = _QosSchedulingClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 5, 1)
)
if mibBuilder.loadTexts:
    qosSchedulingClassTable.setStatus("current")
_QosSchedulingClassEntry_Object = MibTableRow
qosSchedulingClassEntry = _QosSchedulingClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 5, 1, 1)
)
qosSchedulingClassEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "qosSchedulingClassIndex"),
)
if mibBuilder.loadTexts:
    qosSchedulingClassEntry.setStatus("current")


class _QosSchedulingClassIndex_Type(Integer32):
    """Custom type qosSchedulingClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosSchedulingClassIndex_Type.__name__ = "Integer32"
_QosSchedulingClassIndex_Object = MibTableColumn
qosSchedulingClassIndex = _QosSchedulingClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 5, 1, 1, 1),
    _QosSchedulingClassIndex_Type()
)
qosSchedulingClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSchedulingClassIndex.setStatus("current")


class _QosSchedulingWeight_Type(Integer32):
    """Custom type qosSchedulingWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_QosSchedulingWeight_Type.__name__ = "Integer32"
_QosSchedulingWeight_Object = MibTableColumn
qosSchedulingWeight = _QosSchedulingWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 5, 1, 1, 2),
    _QosSchedulingWeight_Type()
)
qosSchedulingWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSchedulingWeight.setStatus("current")
_SysQosDiffServ_ObjectIdentity = ObjectIdentity
sysQosDiffServ = _SysQosDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6)
)
_QosDiffServTypeGroup_ObjectIdentity = ObjectIdentity
qosDiffServTypeGroup = _QosDiffServTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1)
)


class _QosDiffServType00_Type(Integer32):
    """Custom type qosDiffServType00 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType00_Type.__name__ = "Integer32"
_QosDiffServType00_Object = MibScalar
qosDiffServType00 = _QosDiffServType00_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 1),
    _QosDiffServType00_Type()
)
qosDiffServType00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType00.setStatus("current")


class _QosDiffServType01_Type(Integer32):
    """Custom type qosDiffServType01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType01_Type.__name__ = "Integer32"
_QosDiffServType01_Object = MibScalar
qosDiffServType01 = _QosDiffServType01_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 2),
    _QosDiffServType01_Type()
)
qosDiffServType01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType01.setStatus("current")


class _QosDiffServType02_Type(Integer32):
    """Custom type qosDiffServType02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType02_Type.__name__ = "Integer32"
_QosDiffServType02_Object = MibScalar
qosDiffServType02 = _QosDiffServType02_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 3),
    _QosDiffServType02_Type()
)
qosDiffServType02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType02.setStatus("current")


class _QosDiffServType03_Type(Integer32):
    """Custom type qosDiffServType03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType03_Type.__name__ = "Integer32"
_QosDiffServType03_Object = MibScalar
qosDiffServType03 = _QosDiffServType03_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 4),
    _QosDiffServType03_Type()
)
qosDiffServType03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType03.setStatus("current")


class _QosDiffServType04_Type(Integer32):
    """Custom type qosDiffServType04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType04_Type.__name__ = "Integer32"
_QosDiffServType04_Object = MibScalar
qosDiffServType04 = _QosDiffServType04_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 5),
    _QosDiffServType04_Type()
)
qosDiffServType04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType04.setStatus("current")


class _QosDiffServType05_Type(Integer32):
    """Custom type qosDiffServType05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType05_Type.__name__ = "Integer32"
_QosDiffServType05_Object = MibScalar
qosDiffServType05 = _QosDiffServType05_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 6),
    _QosDiffServType05_Type()
)
qosDiffServType05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType05.setStatus("current")


class _QosDiffServType06_Type(Integer32):
    """Custom type qosDiffServType06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType06_Type.__name__ = "Integer32"
_QosDiffServType06_Object = MibScalar
qosDiffServType06 = _QosDiffServType06_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 7),
    _QosDiffServType06_Type()
)
qosDiffServType06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType06.setStatus("current")


class _QosDiffServType07_Type(Integer32):
    """Custom type qosDiffServType07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType07_Type.__name__ = "Integer32"
_QosDiffServType07_Object = MibScalar
qosDiffServType07 = _QosDiffServType07_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 8),
    _QosDiffServType07_Type()
)
qosDiffServType07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType07.setStatus("current")


class _QosDiffServType08_Type(Integer32):
    """Custom type qosDiffServType08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType08_Type.__name__ = "Integer32"
_QosDiffServType08_Object = MibScalar
qosDiffServType08 = _QosDiffServType08_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 9),
    _QosDiffServType08_Type()
)
qosDiffServType08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType08.setStatus("current")


class _QosDiffServType09_Type(Integer32):
    """Custom type qosDiffServType09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType09_Type.__name__ = "Integer32"
_QosDiffServType09_Object = MibScalar
qosDiffServType09 = _QosDiffServType09_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 10),
    _QosDiffServType09_Type()
)
qosDiffServType09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType09.setStatus("current")


class _QosDiffServType10_Type(Integer32):
    """Custom type qosDiffServType10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType10_Type.__name__ = "Integer32"
_QosDiffServType10_Object = MibScalar
qosDiffServType10 = _QosDiffServType10_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 11),
    _QosDiffServType10_Type()
)
qosDiffServType10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType10.setStatus("current")


class _QosDiffServType11_Type(Integer32):
    """Custom type qosDiffServType11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType11_Type.__name__ = "Integer32"
_QosDiffServType11_Object = MibScalar
qosDiffServType11 = _QosDiffServType11_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 12),
    _QosDiffServType11_Type()
)
qosDiffServType11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType11.setStatus("current")


class _QosDiffServType12_Type(Integer32):
    """Custom type qosDiffServType12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType12_Type.__name__ = "Integer32"
_QosDiffServType12_Object = MibScalar
qosDiffServType12 = _QosDiffServType12_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 13),
    _QosDiffServType12_Type()
)
qosDiffServType12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType12.setStatus("current")


class _QosDiffServType13_Type(Integer32):
    """Custom type qosDiffServType13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType13_Type.__name__ = "Integer32"
_QosDiffServType13_Object = MibScalar
qosDiffServType13 = _QosDiffServType13_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 14),
    _QosDiffServType13_Type()
)
qosDiffServType13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType13.setStatus("current")


class _QosDiffServType14_Type(Integer32):
    """Custom type qosDiffServType14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType14_Type.__name__ = "Integer32"
_QosDiffServType14_Object = MibScalar
qosDiffServType14 = _QosDiffServType14_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 15),
    _QosDiffServType14_Type()
)
qosDiffServType14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType14.setStatus("current")


class _QosDiffServType15_Type(Integer32):
    """Custom type qosDiffServType15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType15_Type.__name__ = "Integer32"
_QosDiffServType15_Object = MibScalar
qosDiffServType15 = _QosDiffServType15_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 16),
    _QosDiffServType15_Type()
)
qosDiffServType15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType15.setStatus("current")


class _QosDiffServType16_Type(Integer32):
    """Custom type qosDiffServType16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType16_Type.__name__ = "Integer32"
_QosDiffServType16_Object = MibScalar
qosDiffServType16 = _QosDiffServType16_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 17),
    _QosDiffServType16_Type()
)
qosDiffServType16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType16.setStatus("current")


class _QosDiffServType17_Type(Integer32):
    """Custom type qosDiffServType17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType17_Type.__name__ = "Integer32"
_QosDiffServType17_Object = MibScalar
qosDiffServType17 = _QosDiffServType17_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 18),
    _QosDiffServType17_Type()
)
qosDiffServType17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType17.setStatus("current")


class _QosDiffServType18_Type(Integer32):
    """Custom type qosDiffServType18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType18_Type.__name__ = "Integer32"
_QosDiffServType18_Object = MibScalar
qosDiffServType18 = _QosDiffServType18_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 19),
    _QosDiffServType18_Type()
)
qosDiffServType18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType18.setStatus("current")


class _QosDiffServType19_Type(Integer32):
    """Custom type qosDiffServType19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType19_Type.__name__ = "Integer32"
_QosDiffServType19_Object = MibScalar
qosDiffServType19 = _QosDiffServType19_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 20),
    _QosDiffServType19_Type()
)
qosDiffServType19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType19.setStatus("current")


class _QosDiffServType20_Type(Integer32):
    """Custom type qosDiffServType20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType20_Type.__name__ = "Integer32"
_QosDiffServType20_Object = MibScalar
qosDiffServType20 = _QosDiffServType20_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 21),
    _QosDiffServType20_Type()
)
qosDiffServType20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType20.setStatus("current")


class _QosDiffServType21_Type(Integer32):
    """Custom type qosDiffServType21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType21_Type.__name__ = "Integer32"
_QosDiffServType21_Object = MibScalar
qosDiffServType21 = _QosDiffServType21_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 22),
    _QosDiffServType21_Type()
)
qosDiffServType21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType21.setStatus("current")


class _QosDiffServType22_Type(Integer32):
    """Custom type qosDiffServType22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType22_Type.__name__ = "Integer32"
_QosDiffServType22_Object = MibScalar
qosDiffServType22 = _QosDiffServType22_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 23),
    _QosDiffServType22_Type()
)
qosDiffServType22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType22.setStatus("current")


class _QosDiffServType23_Type(Integer32):
    """Custom type qosDiffServType23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType23_Type.__name__ = "Integer32"
_QosDiffServType23_Object = MibScalar
qosDiffServType23 = _QosDiffServType23_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 24),
    _QosDiffServType23_Type()
)
qosDiffServType23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType23.setStatus("current")


class _QosDiffServType24_Type(Integer32):
    """Custom type qosDiffServType24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType24_Type.__name__ = "Integer32"
_QosDiffServType24_Object = MibScalar
qosDiffServType24 = _QosDiffServType24_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 25),
    _QosDiffServType24_Type()
)
qosDiffServType24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType24.setStatus("current")


class _QosDiffServType25_Type(Integer32):
    """Custom type qosDiffServType25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType25_Type.__name__ = "Integer32"
_QosDiffServType25_Object = MibScalar
qosDiffServType25 = _QosDiffServType25_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 26),
    _QosDiffServType25_Type()
)
qosDiffServType25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType25.setStatus("current")


class _QosDiffServType26_Type(Integer32):
    """Custom type qosDiffServType26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType26_Type.__name__ = "Integer32"
_QosDiffServType26_Object = MibScalar
qosDiffServType26 = _QosDiffServType26_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 27),
    _QosDiffServType26_Type()
)
qosDiffServType26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType26.setStatus("current")


class _QosDiffServType27_Type(Integer32):
    """Custom type qosDiffServType27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType27_Type.__name__ = "Integer32"
_QosDiffServType27_Object = MibScalar
qosDiffServType27 = _QosDiffServType27_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 28),
    _QosDiffServType27_Type()
)
qosDiffServType27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType27.setStatus("current")


class _QosDiffServType28_Type(Integer32):
    """Custom type qosDiffServType28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType28_Type.__name__ = "Integer32"
_QosDiffServType28_Object = MibScalar
qosDiffServType28 = _QosDiffServType28_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 29),
    _QosDiffServType28_Type()
)
qosDiffServType28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType28.setStatus("current")


class _QosDiffServType29_Type(Integer32):
    """Custom type qosDiffServType29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType29_Type.__name__ = "Integer32"
_QosDiffServType29_Object = MibScalar
qosDiffServType29 = _QosDiffServType29_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 30),
    _QosDiffServType29_Type()
)
qosDiffServType29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType29.setStatus("current")


class _QosDiffServType30_Type(Integer32):
    """Custom type qosDiffServType30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType30_Type.__name__ = "Integer32"
_QosDiffServType30_Object = MibScalar
qosDiffServType30 = _QosDiffServType30_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 31),
    _QosDiffServType30_Type()
)
qosDiffServType30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType30.setStatus("current")


class _QosDiffServType31_Type(Integer32):
    """Custom type qosDiffServType31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType31_Type.__name__ = "Integer32"
_QosDiffServType31_Object = MibScalar
qosDiffServType31 = _QosDiffServType31_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 32),
    _QosDiffServType31_Type()
)
qosDiffServType31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType31.setStatus("current")


class _QosDiffServType32_Type(Integer32):
    """Custom type qosDiffServType32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType32_Type.__name__ = "Integer32"
_QosDiffServType32_Object = MibScalar
qosDiffServType32 = _QosDiffServType32_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 33),
    _QosDiffServType32_Type()
)
qosDiffServType32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType32.setStatus("current")


class _QosDiffServType33_Type(Integer32):
    """Custom type qosDiffServType33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType33_Type.__name__ = "Integer32"
_QosDiffServType33_Object = MibScalar
qosDiffServType33 = _QosDiffServType33_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 34),
    _QosDiffServType33_Type()
)
qosDiffServType33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType33.setStatus("current")


class _QosDiffServType34_Type(Integer32):
    """Custom type qosDiffServType34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType34_Type.__name__ = "Integer32"
_QosDiffServType34_Object = MibScalar
qosDiffServType34 = _QosDiffServType34_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 35),
    _QosDiffServType34_Type()
)
qosDiffServType34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType34.setStatus("current")


class _QosDiffServType35_Type(Integer32):
    """Custom type qosDiffServType35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType35_Type.__name__ = "Integer32"
_QosDiffServType35_Object = MibScalar
qosDiffServType35 = _QosDiffServType35_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 36),
    _QosDiffServType35_Type()
)
qosDiffServType35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType35.setStatus("current")


class _QosDiffServType36_Type(Integer32):
    """Custom type qosDiffServType36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType36_Type.__name__ = "Integer32"
_QosDiffServType36_Object = MibScalar
qosDiffServType36 = _QosDiffServType36_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 37),
    _QosDiffServType36_Type()
)
qosDiffServType36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType36.setStatus("current")


class _QosDiffServType37_Type(Integer32):
    """Custom type qosDiffServType37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType37_Type.__name__ = "Integer32"
_QosDiffServType37_Object = MibScalar
qosDiffServType37 = _QosDiffServType37_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 38),
    _QosDiffServType37_Type()
)
qosDiffServType37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType37.setStatus("current")


class _QosDiffServType38_Type(Integer32):
    """Custom type qosDiffServType38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType38_Type.__name__ = "Integer32"
_QosDiffServType38_Object = MibScalar
qosDiffServType38 = _QosDiffServType38_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 39),
    _QosDiffServType38_Type()
)
qosDiffServType38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType38.setStatus("current")


class _QosDiffServType39_Type(Integer32):
    """Custom type qosDiffServType39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType39_Type.__name__ = "Integer32"
_QosDiffServType39_Object = MibScalar
qosDiffServType39 = _QosDiffServType39_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 40),
    _QosDiffServType39_Type()
)
qosDiffServType39.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType39.setStatus("current")


class _QosDiffServType40_Type(Integer32):
    """Custom type qosDiffServType40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType40_Type.__name__ = "Integer32"
_QosDiffServType40_Object = MibScalar
qosDiffServType40 = _QosDiffServType40_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 41),
    _QosDiffServType40_Type()
)
qosDiffServType40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType40.setStatus("current")


class _QosDiffServType41_Type(Integer32):
    """Custom type qosDiffServType41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType41_Type.__name__ = "Integer32"
_QosDiffServType41_Object = MibScalar
qosDiffServType41 = _QosDiffServType41_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 42),
    _QosDiffServType41_Type()
)
qosDiffServType41.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType41.setStatus("current")


class _QosDiffServType42_Type(Integer32):
    """Custom type qosDiffServType42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType42_Type.__name__ = "Integer32"
_QosDiffServType42_Object = MibScalar
qosDiffServType42 = _QosDiffServType42_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 43),
    _QosDiffServType42_Type()
)
qosDiffServType42.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType42.setStatus("current")


class _QosDiffServType43_Type(Integer32):
    """Custom type qosDiffServType43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType43_Type.__name__ = "Integer32"
_QosDiffServType43_Object = MibScalar
qosDiffServType43 = _QosDiffServType43_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 44),
    _QosDiffServType43_Type()
)
qosDiffServType43.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType43.setStatus("current")


class _QosDiffServType44_Type(Integer32):
    """Custom type qosDiffServType44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType44_Type.__name__ = "Integer32"
_QosDiffServType44_Object = MibScalar
qosDiffServType44 = _QosDiffServType44_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 45),
    _QosDiffServType44_Type()
)
qosDiffServType44.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType44.setStatus("current")


class _QosDiffServType45_Type(Integer32):
    """Custom type qosDiffServType45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType45_Type.__name__ = "Integer32"
_QosDiffServType45_Object = MibScalar
qosDiffServType45 = _QosDiffServType45_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 46),
    _QosDiffServType45_Type()
)
qosDiffServType45.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType45.setStatus("current")


class _QosDiffServType46_Type(Integer32):
    """Custom type qosDiffServType46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType46_Type.__name__ = "Integer32"
_QosDiffServType46_Object = MibScalar
qosDiffServType46 = _QosDiffServType46_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 47),
    _QosDiffServType46_Type()
)
qosDiffServType46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType46.setStatus("current")


class _QosDiffServType47_Type(Integer32):
    """Custom type qosDiffServType47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType47_Type.__name__ = "Integer32"
_QosDiffServType47_Object = MibScalar
qosDiffServType47 = _QosDiffServType47_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 48),
    _QosDiffServType47_Type()
)
qosDiffServType47.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType47.setStatus("current")


class _QosDiffServType48_Type(Integer32):
    """Custom type qosDiffServType48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType48_Type.__name__ = "Integer32"
_QosDiffServType48_Object = MibScalar
qosDiffServType48 = _QosDiffServType48_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 49),
    _QosDiffServType48_Type()
)
qosDiffServType48.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType48.setStatus("current")


class _QosDiffServType49_Type(Integer32):
    """Custom type qosDiffServType49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType49_Type.__name__ = "Integer32"
_QosDiffServType49_Object = MibScalar
qosDiffServType49 = _QosDiffServType49_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 50),
    _QosDiffServType49_Type()
)
qosDiffServType49.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType49.setStatus("current")


class _QosDiffServType50_Type(Integer32):
    """Custom type qosDiffServType50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType50_Type.__name__ = "Integer32"
_QosDiffServType50_Object = MibScalar
qosDiffServType50 = _QosDiffServType50_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 51),
    _QosDiffServType50_Type()
)
qosDiffServType50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType50.setStatus("current")


class _QosDiffServType51_Type(Integer32):
    """Custom type qosDiffServType51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType51_Type.__name__ = "Integer32"
_QosDiffServType51_Object = MibScalar
qosDiffServType51 = _QosDiffServType51_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 52),
    _QosDiffServType51_Type()
)
qosDiffServType51.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType51.setStatus("current")


class _QosDiffServType52_Type(Integer32):
    """Custom type qosDiffServType52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType52_Type.__name__ = "Integer32"
_QosDiffServType52_Object = MibScalar
qosDiffServType52 = _QosDiffServType52_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 53),
    _QosDiffServType52_Type()
)
qosDiffServType52.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType52.setStatus("current")


class _QosDiffServType53_Type(Integer32):
    """Custom type qosDiffServType53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType53_Type.__name__ = "Integer32"
_QosDiffServType53_Object = MibScalar
qosDiffServType53 = _QosDiffServType53_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 54),
    _QosDiffServType53_Type()
)
qosDiffServType53.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType53.setStatus("current")


class _QosDiffServType54_Type(Integer32):
    """Custom type qosDiffServType54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType54_Type.__name__ = "Integer32"
_QosDiffServType54_Object = MibScalar
qosDiffServType54 = _QosDiffServType54_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 55),
    _QosDiffServType54_Type()
)
qosDiffServType54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType54.setStatus("current")


class _QosDiffServType55_Type(Integer32):
    """Custom type qosDiffServType55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType55_Type.__name__ = "Integer32"
_QosDiffServType55_Object = MibScalar
qosDiffServType55 = _QosDiffServType55_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 56),
    _QosDiffServType55_Type()
)
qosDiffServType55.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType55.setStatus("current")


class _QosDiffServType56_Type(Integer32):
    """Custom type qosDiffServType56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType56_Type.__name__ = "Integer32"
_QosDiffServType56_Object = MibScalar
qosDiffServType56 = _QosDiffServType56_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 57),
    _QosDiffServType56_Type()
)
qosDiffServType56.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType56.setStatus("current")


class _QosDiffServType57_Type(Integer32):
    """Custom type qosDiffServType57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType57_Type.__name__ = "Integer32"
_QosDiffServType57_Object = MibScalar
qosDiffServType57 = _QosDiffServType57_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 58),
    _QosDiffServType57_Type()
)
qosDiffServType57.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType57.setStatus("current")


class _QosDiffServType58_Type(Integer32):
    """Custom type qosDiffServType58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType58_Type.__name__ = "Integer32"
_QosDiffServType58_Object = MibScalar
qosDiffServType58 = _QosDiffServType58_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 59),
    _QosDiffServType58_Type()
)
qosDiffServType58.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType58.setStatus("current")


class _QosDiffServType59_Type(Integer32):
    """Custom type qosDiffServType59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType59_Type.__name__ = "Integer32"
_QosDiffServType59_Object = MibScalar
qosDiffServType59 = _QosDiffServType59_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 60),
    _QosDiffServType59_Type()
)
qosDiffServType59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType59.setStatus("current")


class _QosDiffServType60_Type(Integer32):
    """Custom type qosDiffServType60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType60_Type.__name__ = "Integer32"
_QosDiffServType60_Object = MibScalar
qosDiffServType60 = _QosDiffServType60_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 61),
    _QosDiffServType60_Type()
)
qosDiffServType60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType60.setStatus("current")


class _QosDiffServType61_Type(Integer32):
    """Custom type qosDiffServType61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType61_Type.__name__ = "Integer32"
_QosDiffServType61_Object = MibScalar
qosDiffServType61 = _QosDiffServType61_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 62),
    _QosDiffServType61_Type()
)
qosDiffServType61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType61.setStatus("current")


class _QosDiffServType62_Type(Integer32):
    """Custom type qosDiffServType62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType62_Type.__name__ = "Integer32"
_QosDiffServType62_Object = MibScalar
qosDiffServType62 = _QosDiffServType62_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 63),
    _QosDiffServType62_Type()
)
qosDiffServType62.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType62.setStatus("current")


class _QosDiffServType63_Type(Integer32):
    """Custom type qosDiffServType63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosDiffServType63_Type.__name__ = "Integer32"
_QosDiffServType63_Object = MibScalar
qosDiffServType63 = _QosDiffServType63_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 12, 6, 1, 64),
    _QosDiffServType63_Type()
)
qosDiffServType63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType63.setStatus("current")
_CompanyTrafficMgmt_ObjectIdentity = ObjectIdentity
companyTrafficMgmt = _CompanyTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13)
)
_SysBandwidthCtrlSettings_ObjectIdentity = ObjectIdentity
sysBandwidthCtrlSettings = _SysBandwidthCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1)
)
_BandwidthCtrlTable_Object = MibTable
bandwidthCtrlTable = _BandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    bandwidthCtrlTable.setStatus("current")
_BandwidthCtrlEntry_Object = MibTableRow
bandwidthCtrlEntry = _BandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1, 2, 1)
)
bandwidthCtrlEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "bandwidthCtrlIndex"),
)
if mibBuilder.loadTexts:
    bandwidthCtrlEntry.setStatus("current")
_BandwidthCtrlIndex_Type = Integer32
_BandwidthCtrlIndex_Object = MibTableColumn
bandwidthCtrlIndex = _BandwidthCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1, 2, 1, 1),
    _BandwidthCtrlIndex_Type()
)
bandwidthCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthCtrlIndex.setStatus("current")


class _BandwidthCtrlTxThreshold_Type(Integer32):
    """Custom type bandwidthCtrlTxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1000000),
    )


_BandwidthCtrlTxThreshold_Type.__name__ = "Integer32"
_BandwidthCtrlTxThreshold_Object = MibTableColumn
bandwidthCtrlTxThreshold = _BandwidthCtrlTxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1, 2, 1, 2),
    _BandwidthCtrlTxThreshold_Type()
)
bandwidthCtrlTxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlTxThreshold.setStatus("current")


class _BandwidthCtrlEffectiveTxThreshold_Type(Integer32):
    """Custom type bandwidthCtrlEffectiveTxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1000000),
    )


_BandwidthCtrlEffectiveTxThreshold_Type.__name__ = "Integer32"
_BandwidthCtrlEffectiveTxThreshold_Object = MibTableColumn
bandwidthCtrlEffectiveTxThreshold = _BandwidthCtrlEffectiveTxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1, 2, 1, 3),
    _BandwidthCtrlEffectiveTxThreshold_Type()
)
bandwidthCtrlEffectiveTxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthCtrlEffectiveTxThreshold.setStatus("current")


class _BandwidthCtrlRxThreshold_Type(Integer32):
    """Custom type bandwidthCtrlRxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1000000),
    )


_BandwidthCtrlRxThreshold_Type.__name__ = "Integer32"
_BandwidthCtrlRxThreshold_Object = MibTableColumn
bandwidthCtrlRxThreshold = _BandwidthCtrlRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1, 2, 1, 4),
    _BandwidthCtrlRxThreshold_Type()
)
bandwidthCtrlRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlRxThreshold.setStatus("current")


class _BandwidthCtrlEffectiveRxThreshold_Type(Integer32):
    """Custom type bandwidthCtrlEffectiveRxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1000000),
    )


_BandwidthCtrlEffectiveRxThreshold_Type.__name__ = "Integer32"
_BandwidthCtrlEffectiveRxThreshold_Object = MibTableColumn
bandwidthCtrlEffectiveRxThreshold = _BandwidthCtrlEffectiveRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 1, 2, 1, 5),
    _BandwidthCtrlEffectiveRxThreshold_Type()
)
bandwidthCtrlEffectiveRxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthCtrlEffectiveRxThreshold.setStatus("current")
_SysTrafficCtrlSettings_ObjectIdentity = ObjectIdentity
sysTrafficCtrlSettings = _SysTrafficCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4)
)


class _TrafficCtrlTrap_Type(Integer32):
    """Custom type trafficCtrlTrap based on Integer32"""
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
          ("none", 0),
          ("stormCleared", 2),
          ("stormOccurred", 1))
    )


_TrafficCtrlTrap_Type.__name__ = "Integer32"
_TrafficCtrlTrap_Object = MibScalar
trafficCtrlTrap = _TrafficCtrlTrap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 1),
    _TrafficCtrlTrap_Type()
)
trafficCtrlTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlTrap.setStatus("current")
_TrafficCtrlTable_Object = MibTable
trafficCtrlTable = _TrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2)
)
if mibBuilder.loadTexts:
    trafficCtrlTable.setStatus("current")
_TrafficCtrlEntry_Object = MibTableRow
trafficCtrlEntry = _TrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1)
)
trafficCtrlEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "trafficCtrlIndex"),
)
if mibBuilder.loadTexts:
    trafficCtrlEntry.setStatus("current")


class _TrafficCtrlIndex_Type(Integer32):
    """Custom type trafficCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrafficCtrlIndex_Type.__name__ = "Integer32"
_TrafficCtrlIndex_Object = MibTableColumn
trafficCtrlIndex = _TrafficCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1, 1),
    _TrafficCtrlIndex_Type()
)
trafficCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficCtrlIndex.setStatus("current")


class _TrafficCtrlActionMode_Type(Integer32):
    """Custom type trafficCtrlActionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("shutdown", 1))
    )


_TrafficCtrlActionMode_Type.__name__ = "Integer32"
_TrafficCtrlActionMode_Object = MibTableColumn
trafficCtrlActionMode = _TrafficCtrlActionMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1, 2),
    _TrafficCtrlActionMode_Type()
)
trafficCtrlActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlActionMode.setStatus("current")


class _TrafficCtrlType_Type(Integer32):
    """Custom type trafficCtrlType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("b", 1),
          ("m", 2),
          ("mb", 3),
          ("none", 0),
          ("u", 4),
          ("ub", 5),
          ("um", 6),
          ("umb", 7))
    )


_TrafficCtrlType_Type.__name__ = "Integer32"
_TrafficCtrlType_Object = MibTableColumn
trafficCtrlType = _TrafficCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1, 3),
    _TrafficCtrlType_Type()
)
trafficCtrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlType.setStatus("current")


class _TrafficCtrlThreshold_Type(Integer32):
    """Custom type trafficCtrlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 102400),
    )


_TrafficCtrlThreshold_Type.__name__ = "Integer32"
_TrafficCtrlThreshold_Object = MibTableColumn
trafficCtrlThreshold = _TrafficCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1, 4),
    _TrafficCtrlThreshold_Type()
)
trafficCtrlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlThreshold.setStatus("current")


class _TrafficCtrlCountDown_Type(Integer32):
    """Custom type trafficCtrlCountDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_TrafficCtrlCountDown_Type.__name__ = "Integer32"
_TrafficCtrlCountDown_Object = MibTableColumn
trafficCtrlCountDown = _TrafficCtrlCountDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1, 5),
    _TrafficCtrlCountDown_Type()
)
trafficCtrlCountDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlCountDown.setStatus("current")


class _TrafficCtrlTimeInterval_Type(Integer32):
    """Custom type trafficCtrlTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TrafficCtrlTimeInterval_Type.__name__ = "Integer32"
_TrafficCtrlTimeInterval_Object = MibTableColumn
trafficCtrlTimeInterval = _TrafficCtrlTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1, 6),
    _TrafficCtrlTimeInterval_Type()
)
trafficCtrlTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlTimeInterval.setStatus("current")


class _TrafficCtrlPortState_Type(Integer32):
    """Custom type trafficCtrlPortState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("normal", 0),
          ("shutdown", 2))
    )


_TrafficCtrlPortState_Type.__name__ = "Integer32"
_TrafficCtrlPortState_Object = MibTableColumn
trafficCtrlPortState = _TrafficCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 4, 2, 1, 7),
    _TrafficCtrlPortState_Type()
)
trafficCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficCtrlPortState.setStatus("current")
_SysStormCtrlTrap_ObjectIdentity = ObjectIdentity
sysStormCtrlTrap = _SysStormCtrlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 5)
)
_StormCtrlTrap_ObjectIdentity = ObjectIdentity
stormCtrlTrap = _StormCtrlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 5, 0)
)
_CompanySecurity_ObjectIdentity = ObjectIdentity
companySecurity = _CompanySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14)
)
_SysPortSecurity_ObjectIdentity = ObjectIdentity
sysPortSecurity = _SysPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2)
)
_PortSecurityTable_Object = MibTable
portSecurityTable = _PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    portSecurityTable.setStatus("current")
_PortSecurityEntry_Object = MibTableRow
portSecurityEntry = _PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 1, 1)
)
portSecurityEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "portSecurityIndex"),
)
if mibBuilder.loadTexts:
    portSecurityEntry.setStatus("current")
_PortSecurityIndex_Type = Integer32
_PortSecurityIndex_Object = MibTableColumn
portSecurityIndex = _PortSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 1, 1, 1),
    _PortSecurityIndex_Type()
)
portSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityIndex.setStatus("current")


class _PortSecurityState_Type(Integer32):
    """Custom type portSecurityState based on Integer32"""
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


_PortSecurityState_Type.__name__ = "Integer32"
_PortSecurityState_Object = MibTableColumn
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 1, 1, 2),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("current")


class _PortSecurityMLA_Type(Integer32):
    """Custom type portSecurityMLA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PortSecurityMLA_Type.__name__ = "Integer32"
_PortSecurityMLA_Object = MibTableColumn
portSecurityMLA = _PortSecurityMLA_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 1, 1, 3),
    _PortSecurityMLA_Type()
)
portSecurityMLA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMLA.setStatus("current")


class _PortSecurityLockAddrMode_Type(Integer32):
    """Custom type portSecurityLockAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 1),
          ("deleteOnTimeout", 2),
          ("permanent", 3))
    )


_PortSecurityLockAddrMode_Type.__name__ = "Integer32"
_PortSecurityLockAddrMode_Object = MibTableColumn
portSecurityLockAddrMode = _PortSecurityLockAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 1, 1, 4),
    _PortSecurityLockAddrMode_Type()
)
portSecurityLockAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityLockAddrMode.setStatus("current")
_PortSecFDBPermanentTable_Object = MibTable
portSecFDBPermanentTable = _PortSecFDBPermanentTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 2)
)
if mibBuilder.loadTexts:
    portSecFDBPermanentTable.setStatus("current")
_PortSecFDBPermanentEntry_Object = MibTableRow
portSecFDBPermanentEntry = _PortSecFDBPermanentEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 2, 1)
)
portSecFDBPermanentEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "portSecFDBPermVlanID"),
    (0, "DGS-1100-10ME_A1", "portSecFDBPermMac"),
)
if mibBuilder.loadTexts:
    portSecFDBPermanentEntry.setStatus("current")
_PortSecFDBPermVlanID_Type = Integer32
_PortSecFDBPermVlanID_Object = MibTableColumn
portSecFDBPermVlanID = _PortSecFDBPermVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 2, 1, 1),
    _PortSecFDBPermVlanID_Type()
)
portSecFDBPermVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermVlanID.setStatus("current")
_PortSecFDBPermMac_Type = MacAddress
_PortSecFDBPermMac_Object = MibTableColumn
portSecFDBPermMac = _PortSecFDBPermMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 2, 1, 2),
    _PortSecFDBPermMac_Type()
)
portSecFDBPermMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermMac.setStatus("current")
_PortSecFDBPermPort_Type = Integer32
_PortSecFDBPermPort_Object = MibTableColumn
portSecFDBPermPort = _PortSecFDBPermPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 2, 1, 3),
    _PortSecFDBPermPort_Type()
)
portSecFDBPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermPort.setStatus("current")


class _PortSecFDBPermType_Type(Integer32):
    """Custom type portSecFDBPermType based on Integer32"""
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
        *(("deleteOnReset", 1),
          ("deleteOnTimeout", 2),
          ("invalid", 4),
          ("other", 0),
          ("permanent", 3))
    )


_PortSecFDBPermType_Type.__name__ = "Integer32"
_PortSecFDBPermType_Object = MibTableColumn
portSecFDBPermType = _PortSecFDBPermType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 2, 1, 4),
    _PortSecFDBPermType_Type()
)
portSecFDBPermType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermType.setStatus("current")


class _PortSecFDBPermEntryState_Type(Integer32):
    """Custom type portSecFDBPermEntryState based on Integer32"""
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


_PortSecFDBPermEntryState_Type.__name__ = "Integer32"
_PortSecFDBPermEntryState_Object = MibTableColumn
portSecFDBPermEntryState = _PortSecFDBPermEntryState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 2, 2, 1, 5),
    _PortSecFDBPermEntryState_Type()
)
portSecFDBPermEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecFDBPermEntryState.setStatus("current")
_SysTrafficSegmentation_ObjectIdentity = ObjectIdentity
sysTrafficSegmentation = _SysTrafficSegmentation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 9)
)
_TrafficSegmentationTable_Object = MibTable
trafficSegmentationTable = _TrafficSegmentationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 9, 1)
)
if mibBuilder.loadTexts:
    trafficSegmentationTable.setStatus("current")
_TrafficSegmentationEntry_Object = MibTableRow
trafficSegmentationEntry = _TrafficSegmentationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 9, 1, 1)
)
trafficSegmentationEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "trafficSegmentationIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegmentationEntry.setStatus("current")
_TrafficSegmentationIfIndex_Type = InterfaceIndex
_TrafficSegmentationIfIndex_Object = MibTableColumn
trafficSegmentationIfIndex = _TrafficSegmentationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 9, 1, 1, 1),
    _TrafficSegmentationIfIndex_Type()
)
trafficSegmentationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegmentationIfIndex.setStatus("current")
_TrafficSegmentationMemberList_Type = PortList
_TrafficSegmentationMemberList_Object = MibTableColumn
trafficSegmentationMemberList = _TrafficSegmentationMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 9, 1, 1, 2),
    _TrafficSegmentationMemberList_Type()
)
trafficSegmentationMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegmentationMemberList.setStatus("current")
_SysSecurityAAC_ObjectIdentity = ObjectIdentity
sysSecurityAAC = _SysSecurityAAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11)
)


class _AacAuthenAdminState_Type(Integer32):
    """Custom type aacAuthenAdminState based on Integer32"""
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


_AacAuthenAdminState_Type.__name__ = "Integer32"
_AacAuthenAdminState_Object = MibScalar
aacAuthenAdminState = _AacAuthenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 1),
    _AacAuthenAdminState_Type()
)
aacAuthenAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAuthenAdminState.setStatus("current")


class _AacAuthParamResponseTimeout_Type(Integer32):
    """Custom type aacAuthParamResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AacAuthParamResponseTimeout_Type.__name__ = "Integer32"
_AacAuthParamResponseTimeout_Object = MibScalar
aacAuthParamResponseTimeout = _AacAuthParamResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 2),
    _AacAuthParamResponseTimeout_Type()
)
aacAuthParamResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAuthParamResponseTimeout.setStatus("current")


class _AacAuthParamAttempt_Type(Integer32):
    """Custom type aacAuthParamAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AacAuthParamAttempt_Type.__name__ = "Integer32"
_AacAuthParamAttempt_Object = MibScalar
aacAuthParamAttempt = _AacAuthParamAttempt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 3),
    _AacAuthParamAttempt_Type()
)
aacAuthParamAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAuthParamAttempt.setStatus("current")


class _AacLocalEnablePassword_Type(DisplayString):
    """Custom type aacLocalEnablePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacLocalEnablePassword_Type.__name__ = "DisplayString"
_AacLocalEnablePassword_Object = MibScalar
aacLocalEnablePassword = _AacLocalEnablePassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 4),
    _AacLocalEnablePassword_Type()
)
aacLocalEnablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLocalEnablePassword.setStatus("current")
_AacAPAuthMethodGroup_ObjectIdentity = ObjectIdentity
aacAPAuthMethodGroup = _AacAPAuthMethodGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 5)
)
_AacAPLoginMethod_ObjectIdentity = ObjectIdentity
aacAPLoginMethod = _AacAPLoginMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 5, 1)
)


class _AacAPTelnetLoginMethod_Type(DisplayString):
    """Custom type aacAPTelnetLoginMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacAPTelnetLoginMethod_Type.__name__ = "DisplayString"
_AacAPTelnetLoginMethod_Object = MibScalar
aacAPTelnetLoginMethod = _AacAPTelnetLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 5, 1, 2),
    _AacAPTelnetLoginMethod_Type()
)
aacAPTelnetLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPTelnetLoginMethod.setStatus("current")


class _AacAPHttpLoginMethod_Type(DisplayString):
    """Custom type aacAPHttpLoginMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacAPHttpLoginMethod_Type.__name__ = "DisplayString"
_AacAPHttpLoginMethod_Object = MibScalar
aacAPHttpLoginMethod = _AacAPHttpLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 5, 1, 4),
    _AacAPHttpLoginMethod_Type()
)
aacAPHttpLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPHttpLoginMethod.setStatus("current")
_AacAPEnableMethod_ObjectIdentity = ObjectIdentity
aacAPEnableMethod = _AacAPEnableMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 5, 2)
)


class _AacAPTelnetEnableMethod_Type(DisplayString):
    """Custom type aacAPTelnetEnableMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacAPTelnetEnableMethod_Type.__name__ = "DisplayString"
_AacAPTelnetEnableMethod_Object = MibScalar
aacAPTelnetEnableMethod = _AacAPTelnetEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 5, 2, 2),
    _AacAPTelnetEnableMethod_Type()
)
aacAPTelnetEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPTelnetEnableMethod.setStatus("current")


class _AacAPHttpEnableMethod_Type(DisplayString):
    """Custom type aacAPHttpEnableMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacAPHttpEnableMethod_Type.__name__ = "DisplayString"
_AacAPHttpEnableMethod_Object = MibScalar
aacAPHttpEnableMethod = _AacAPHttpEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 5, 2, 4),
    _AacAPHttpEnableMethod_Type()
)
aacAPHttpEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPHttpEnableMethod.setStatus("current")
_AacLoginMethodListTable_Object = MibTable
aacLoginMethodListTable = _AacLoginMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6)
)
if mibBuilder.loadTexts:
    aacLoginMethodListTable.setStatus("current")
_AacLoginMethodListEntry_Object = MibTableRow
aacLoginMethodListEntry = _AacLoginMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6, 1)
)
aacLoginMethodListEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aacLoginMethodListName"),
)
if mibBuilder.loadTexts:
    aacLoginMethodListEntry.setStatus("current")


class _AacLoginMethodListName_Type(DisplayString):
    """Custom type aacLoginMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacLoginMethodListName_Type.__name__ = "DisplayString"
_AacLoginMethodListName_Object = MibTableColumn
aacLoginMethodListName = _AacLoginMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6, 1, 1),
    _AacLoginMethodListName_Type()
)
aacLoginMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacLoginMethodListName.setStatus("current")
_AacLoginMethod1_Type = DisplayString
_AacLoginMethod1_Object = MibTableColumn
aacLoginMethod1 = _AacLoginMethod1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6, 1, 2),
    _AacLoginMethod1_Type()
)
aacLoginMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod1.setStatus("current")
_AacLoginMethod2_Type = DisplayString
_AacLoginMethod2_Object = MibTableColumn
aacLoginMethod2 = _AacLoginMethod2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6, 1, 3),
    _AacLoginMethod2_Type()
)
aacLoginMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod2.setStatus("current")
_AacLoginMethod3_Type = DisplayString
_AacLoginMethod3_Object = MibTableColumn
aacLoginMethod3 = _AacLoginMethod3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6, 1, 4),
    _AacLoginMethod3_Type()
)
aacLoginMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod3.setStatus("current")
_AacLoginMethod4_Type = DisplayString
_AacLoginMethod4_Object = MibTableColumn
aacLoginMethod4 = _AacLoginMethod4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6, 1, 5),
    _AacLoginMethod4_Type()
)
aacLoginMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod4.setStatus("current")
_AacLoginMethodListRowStatus_Type = RowStatus
_AacLoginMethodListRowStatus_Object = MibTableColumn
aacLoginMethodListRowStatus = _AacLoginMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 6, 1, 6),
    _AacLoginMethodListRowStatus_Type()
)
aacLoginMethodListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethodListRowStatus.setStatus("current")
_AacEnableMethodListTable_Object = MibTable
aacEnableMethodListTable = _AacEnableMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7)
)
if mibBuilder.loadTexts:
    aacEnableMethodListTable.setStatus("current")
_AacEnableMethodListEntry_Object = MibTableRow
aacEnableMethodListEntry = _AacEnableMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7, 1)
)
aacEnableMethodListEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aacEnableMethodListName"),
)
if mibBuilder.loadTexts:
    aacEnableMethodListEntry.setStatus("current")


class _AacEnableMethodListName_Type(DisplayString):
    """Custom type aacEnableMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacEnableMethodListName_Type.__name__ = "DisplayString"
_AacEnableMethodListName_Object = MibTableColumn
aacEnableMethodListName = _AacEnableMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7, 1, 1),
    _AacEnableMethodListName_Type()
)
aacEnableMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacEnableMethodListName.setStatus("current")
_AacEnableMethod1_Type = DisplayString
_AacEnableMethod1_Object = MibTableColumn
aacEnableMethod1 = _AacEnableMethod1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7, 1, 2),
    _AacEnableMethod1_Type()
)
aacEnableMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod1.setStatus("current")
_AacEnableMethod2_Type = DisplayString
_AacEnableMethod2_Object = MibTableColumn
aacEnableMethod2 = _AacEnableMethod2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7, 1, 3),
    _AacEnableMethod2_Type()
)
aacEnableMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod2.setStatus("current")
_AacEnableMethod3_Type = DisplayString
_AacEnableMethod3_Object = MibTableColumn
aacEnableMethod3 = _AacEnableMethod3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7, 1, 4),
    _AacEnableMethod3_Type()
)
aacEnableMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod3.setStatus("current")
_AacEnableMethod4_Type = DisplayString
_AacEnableMethod4_Object = MibTableColumn
aacEnableMethod4 = _AacEnableMethod4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7, 1, 5),
    _AacEnableMethod4_Type()
)
aacEnableMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod4.setStatus("current")
_AacEnableMethodListRowStatus_Type = RowStatus
_AacEnableMethodListRowStatus_Object = MibTableColumn
aacEnableMethodListRowStatus = _AacEnableMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 7, 1, 6),
    _AacEnableMethodListRowStatus_Type()
)
aacEnableMethodListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethodListRowStatus.setStatus("current")
_AacServerGroupTable_Object = MibTable
aacServerGroupTable = _AacServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 8)
)
if mibBuilder.loadTexts:
    aacServerGroupTable.setStatus("current")
_AacServerGroupEntry_Object = MibTableRow
aacServerGroupEntry = _AacServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 8, 1)
)
aacServerGroupEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aacServerGroupName"),
)
if mibBuilder.loadTexts:
    aacServerGroupEntry.setStatus("current")


class _AacServerGroupName_Type(DisplayString):
    """Custom type aacServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacServerGroupName_Type.__name__ = "DisplayString"
_AacServerGroupName_Object = MibTableColumn
aacServerGroupName = _AacServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 8, 1, 1),
    _AacServerGroupName_Type()
)
aacServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacServerGroupName.setStatus("current")


class _AacServersInGroup_Type(Bits):
    """Custom type aacServersInGroup based on Bits"""
    namedValues = NamedValues(
        *(("id1", 0),
          ("id10", 9),
          ("id11", 10),
          ("id12", 11),
          ("id13", 12),
          ("id14", 13),
          ("id15", 14),
          ("id16", 15),
          ("id2", 1),
          ("id3", 2),
          ("id4", 3),
          ("id5", 4),
          ("id6", 5),
          ("id7", 6),
          ("id8", 7),
          ("id9", 8))
    )

_AacServersInGroup_Type.__name__ = "Bits"
_AacServersInGroup_Object = MibTableColumn
aacServersInGroup = _AacServersInGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 8, 1, 2),
    _AacServersInGroup_Type()
)
aacServersInGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServersInGroup.setStatus("current")
_AacServerGroupRowStatus_Type = RowStatus
_AacServerGroupRowStatus_Object = MibTableColumn
aacServerGroupRowStatus = _AacServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 8, 1, 3),
    _AacServerGroupRowStatus_Type()
)
aacServerGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerGroupRowStatus.setStatus("current")
_AacServerInfoTable_Object = MibTable
aacServerInfoTable = _AacServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9)
)
if mibBuilder.loadTexts:
    aacServerInfoTable.setStatus("current")
_AacServerInfoEntry_Object = MibTableRow
aacServerInfoEntry = _AacServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1)
)
aacServerInfoEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aacServerIPType"),
    (0, "DGS-1100-10ME_A1", "aacServerIPAddr"),
)
if mibBuilder.loadTexts:
    aacServerInfoEntry.setStatus("current")


class _AacServerIPType_Type(Integer32):
    """Custom type aacServerIPType based on Integer32"""
    defaultValue = 1

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


_AacServerIPType_Type.__name__ = "Integer32"
_AacServerIPType_Object = MibTableColumn
aacServerIPType = _AacServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 1),
    _AacServerIPType_Type()
)
aacServerIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacServerIPType.setStatus("current")
_AacServerIPAddr_Type = InetAddress
_AacServerIPAddr_Object = MibTableColumn
aacServerIPAddr = _AacServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 2),
    _AacServerIPAddr_Type()
)
aacServerIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacServerIPAddr.setStatus("current")


class _AacServerIndex_Type(Integer32):
    """Custom type aacServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AacServerIndex_Type.__name__ = "Integer32"
_AacServerIndex_Object = MibTableColumn
aacServerIndex = _AacServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 3),
    _AacServerIndex_Type()
)
aacServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacServerIndex.setStatus("current")
_AacServerInterfaceName_Type = DisplayString
_AacServerInterfaceName_Object = MibTableColumn
aacServerInterfaceName = _AacServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 4),
    _AacServerInterfaceName_Type()
)
aacServerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerInterfaceName.setStatus("current")


class _AacServerAuthPort_Type(Integer32):
    """Custom type aacServerAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AacServerAuthPort_Type.__name__ = "Integer32"
_AacServerAuthPort_Object = MibTableColumn
aacServerAuthPort = _AacServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 5),
    _AacServerAuthPort_Type()
)
aacServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerAuthPort.setStatus("current")


class _AacServerAuthKey_Type(DisplayString):
    """Custom type aacServerAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_AacServerAuthKey_Type.__name__ = "DisplayString"
_AacServerAuthKey_Object = MibTableColumn
aacServerAuthKey = _AacServerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 6),
    _AacServerAuthKey_Type()
)
aacServerAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerAuthKey.setStatus("current")


class _AacServerTimeout_Type(Integer32):
    """Custom type aacServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AacServerTimeout_Type.__name__ = "Integer32"
_AacServerTimeout_Object = MibTableColumn
aacServerTimeout = _AacServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 7),
    _AacServerTimeout_Type()
)
aacServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerTimeout.setStatus("current")


class _AacServerRetryCount_Type(Integer32):
    """Custom type aacServerRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AacServerRetryCount_Type.__name__ = "Integer32"
_AacServerRetryCount_Object = MibTableColumn
aacServerRetryCount = _AacServerRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 8),
    _AacServerRetryCount_Type()
)
aacServerRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerRetryCount.setStatus("current")
_AacServerRowStatus_Type = RowStatus
_AacServerRowStatus_Object = MibTableColumn
aacServerRowStatus = _AacServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 11, 9, 1, 9),
    _AacServerRowStatus_Type()
)
aacServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerRowStatus.setStatus("current")
_SysPortSecurityTrap_ObjectIdentity = ObjectIdentity
sysPortSecurityTrap = _SysPortSecurityTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 12)
)
_PortSecurityTraps_ObjectIdentity = ObjectIdentity
portSecurityTraps = _PortSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 12, 0)
)
_SysTrustedHost_ObjectIdentity = ObjectIdentity
sysTrustedHost = _SysTrustedHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 13)
)


class _TrustedHostStatus_Type(Integer32):
    """Custom type trustedHostStatus based on Integer32"""
    defaultValue = 2

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


_TrustedHostStatus_Type.__name__ = "Integer32"
_TrustedHostStatus_Object = MibScalar
trustedHostStatus = _TrustedHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 13, 1),
    _TrustedHostStatus_Type()
)
trustedHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostStatus.setStatus("current")
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 13, 2)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("current")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 13, 2, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "trustedHostIpAddr"),
    (0, "DGS-1100-10ME_A1", "trustedHostIpMask"),
)
if mibBuilder.loadTexts:
    trustedHostEntry.setStatus("current")
_TrustedHostIpAddr_Type = InetAddress
_TrustedHostIpAddr_Object = MibTableColumn
trustedHostIpAddr = _TrustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 13, 2, 1, 1),
    _TrustedHostIpAddr_Type()
)
trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpAddr.setStatus("current")
_TrustedHostIpMask_Type = InetAddress
_TrustedHostIpMask_Object = MibTableColumn
trustedHostIpMask = _TrustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 13, 2, 1, 2),
    _TrustedHostIpMask_Type()
)
trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpMask.setStatus("current")
_TrustedHostRowStatus_Type = RowStatus
_TrustedHostRowStatus_Object = MibTableColumn
trustedHostRowStatus = _TrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 13, 2, 1, 3),
    _TrustedHostRowStatus_Type()
)
trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedHostRowStatus.setStatus("current")
_CompanyArp_ObjectIdentity = ObjectIdentity
companyArp = _CompanyArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15)
)
_SysArp_ObjectIdentity = ObjectIdentity
sysArp = _SysArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 1)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("current")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 1, 1, 1)
)
arpEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "arpIpAddr"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("current")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 1, 1, 1, 1),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("current")
_ArpMacAddress_Type = MacAddress
_ArpMacAddress_Object = MibTableColumn
arpMacAddress = _ArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 1, 1, 1, 2),
    _ArpMacAddress_Type()
)
arpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpMacAddress.setStatus("current")


class _ArpType_Type(Integer32):
    """Custom type arpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_ArpType_Type.__name__ = "Integer32"
_ArpType_Object = MibTableColumn
arpType = _ArpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 1, 1, 1, 3),
    _ArpType_Type()
)
arpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpType.setStatus("current")
_ArpRowStatus_Type = RowStatus
_ArpRowStatus_Object = MibTableColumn
arpRowStatus = _ArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 1, 1, 1, 4),
    _ArpRowStatus_Type()
)
arpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpRowStatus.setStatus("current")


class _CmArpClear_Type(Integer32):
    """Custom type cmArpClear based on Integer32"""
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
        *(("clearAll", 1),
          ("clearAllDynamic", 3),
          ("cleatAllStatic", 2),
          ("none", 0))
    )


_CmArpClear_Type.__name__ = "Integer32"
_CmArpClear_Object = MibScalar
cmArpClear = _CmArpClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 15, 2),
    _CmArpClear_Type()
)
cmArpClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmArpClear.setStatus("current")
_CompanySyslog_ObjectIdentity = ObjectIdentity
companySyslog = _CompanySyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16)
)
_SyslogSettingGroup_ObjectIdentity = ObjectIdentity
syslogSettingGroup = _SyslogSettingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 1)
)


class _SyslogEnable_Type(Integer32):
    """Custom type syslogEnable based on Integer32"""
    defaultValue = 2

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


_SyslogEnable_Type.__name__ = "Integer32"
_SyslogEnable_Object = MibScalar
syslogEnable = _SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 1, 1),
    _SyslogEnable_Type()
)
syslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogEnable.setStatus("current")


class _SyslogSaveMode_Type(Integer32):
    """Custom type syslogSaveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logTrigger", 2),
          ("onDemand", 0),
          ("timeInterval", 1))
    )


_SyslogSaveMode_Type.__name__ = "Integer32"
_SyslogSaveMode_Object = MibScalar
syslogSaveMode = _SyslogSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 1, 2),
    _SyslogSaveMode_Type()
)
syslogSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSaveMode.setStatus("current")


class _SyslogSaveMinutes_Type(Integer32):
    """Custom type syslogSaveMinutes based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SyslogSaveMinutes_Type.__name__ = "Integer32"
_SyslogSaveMinutes_Object = MibScalar
syslogSaveMinutes = _SyslogSaveMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 1, 3),
    _SyslogSaveMinutes_Type()
)
syslogSaveMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSaveMinutes.setStatus("current")


class _SyslogClearLog_Type(TruthValue):
    """Custom type syslogClearLog based on TruthValue"""


_SyslogClearLog_Object = MibScalar
syslogClearLog = _SyslogClearLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 1, 4),
    _SyslogClearLog_Type()
)
syslogClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogClearLog.setStatus("current")
_SyslogServerGroup_ObjectIdentity = ObjectIdentity
syslogServerGroup = _SyslogServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3)
)
_SyslogServTable_Object = MibTable
syslogServTable = _SyslogServTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    syslogServTable.setStatus("current")
_SyslogServEntry_Object = MibTableRow
syslogServEntry = _SyslogServEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1)
)
syslogServEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "syslogServIndex"),
)
if mibBuilder.loadTexts:
    syslogServEntry.setStatus("current")


class _SyslogServIndex_Type(Integer32):
    """Custom type syslogServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SyslogServIndex_Type.__name__ = "Integer32"
_SyslogServIndex_Object = MibTableColumn
syslogServIndex = _SyslogServIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 1),
    _SyslogServIndex_Type()
)
syslogServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogServIndex.setStatus("current")


class _SyslogServAddrType_Type(Integer32):
    """Custom type syslogServAddrType based on Integer32"""
    defaultValue = 1

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


_SyslogServAddrType_Type.__name__ = "Integer32"
_SyslogServAddrType_Object = MibTableColumn
syslogServAddrType = _SyslogServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 2),
    _SyslogServAddrType_Type()
)
syslogServAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServAddrType.setStatus("current")
_SyslogServAddr_Type = Ipv6Address
_SyslogServAddr_Object = MibTableColumn
syslogServAddr = _SyslogServAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 3),
    _SyslogServAddr_Type()
)
syslogServAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServAddr.setStatus("current")


class _SyslogServSeverity_Type(Integer32):
    """Custom type syslogServSeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("debug", 7),
          ("information", 6),
          ("warning", 4))
    )


_SyslogServSeverity_Type.__name__ = "Integer32"
_SyslogServSeverity_Object = MibTableColumn
syslogServSeverity = _SyslogServSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 5),
    _SyslogServSeverity_Type()
)
syslogServSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServSeverity.setStatus("current")


class _SyslogServFacility_Type(Integer32):
    """Custom type syslogServFacility based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              136,
              144,
              152,
              160,
              168,
              176,
              184)
        )
    )
    namedValues = NamedValues(
        *(("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184))
    )


_SyslogServFacility_Type.__name__ = "Integer32"
_SyslogServFacility_Object = MibTableColumn
syslogServFacility = _SyslogServFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 6),
    _SyslogServFacility_Type()
)
syslogServFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServFacility.setStatus("current")


class _SyslogServUDPport_Type(Integer32):
    """Custom type syslogServUDPport based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 514),
        ValueRangeConstraint(6000, 65535),
    )


_SyslogServUDPport_Type.__name__ = "Integer32"
_SyslogServUDPport_Object = MibTableColumn
syslogServUDPport = _SyslogServUDPport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 7),
    _SyslogServUDPport_Type()
)
syslogServUDPport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServUDPport.setStatus("current")


class _SyslogServSrvStatus_Type(Integer32):
    """Custom type syslogServSrvStatus based on Integer32"""
    defaultValue = 2

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


_SyslogServSrvStatus_Type.__name__ = "Integer32"
_SyslogServSrvStatus_Object = MibTableColumn
syslogServSrvStatus = _SyslogServSrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 8),
    _SyslogServSrvStatus_Type()
)
syslogServSrvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServSrvStatus.setStatus("current")
_SyslogServSrvRowStatus_Type = RowStatus
_SyslogServSrvRowStatus_Object = MibTableColumn
syslogServSrvRowStatus = _SyslogServSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 3, 1, 1, 9),
    _SyslogServSrvRowStatus_Type()
)
syslogServSrvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServSrvRowStatus.setStatus("current")
_SyslogMsg_ObjectIdentity = ObjectIdentity
syslogMsg = _SyslogMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 4)
)
_SyslogMsgTable_Object = MibTable
syslogMsgTable = _SyslogMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    syslogMsgTable.setStatus("current")
_SyslogMsgEntry_Object = MibTableRow
syslogMsgEntry = _SyslogMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 4, 1, 1)
)
syslogMsgEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "syslogMsgIndex"),
)
if mibBuilder.loadTexts:
    syslogMsgEntry.setStatus("current")


class _SyslogMsgIndex_Type(Integer32):
    """Custom type syslogMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SyslogMsgIndex_Type.__name__ = "Integer32"
_SyslogMsgIndex_Object = MibTableColumn
syslogMsgIndex = _SyslogMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 4, 1, 1, 1),
    _SyslogMsgIndex_Type()
)
syslogMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgIndex.setStatus("current")
_SyslogMsgDescr_Type = DisplayString
_SyslogMsgDescr_Object = MibTableColumn
syslogMsgDescr = _SyslogMsgDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 4, 1, 1, 2),
    _SyslogMsgDescr_Type()
)
syslogMsgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgDescr.setStatus("current")
_SyslogMsgTime_Type = DisplayString
_SyslogMsgTime_Object = MibTableColumn
syslogMsgTime = _SyslogMsgTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 4, 1, 1, 3),
    _SyslogMsgTime_Type()
)
syslogMsgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgTime.setStatus("current")


class _SyslogMsgSeverity_Type(Integer32):
    """Custom type syslogMsgSeverity based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("information", 6),
          ("notice", 5),
          ("warning", 4))
    )


_SyslogMsgSeverity_Type.__name__ = "Integer32"
_SyslogMsgSeverity_Object = MibTableColumn
syslogMsgSeverity = _SyslogMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 16, 4, 1, 1, 4),
    _SyslogMsgSeverity_Type()
)
syslogMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgSeverity.setStatus("current")
_CompanyLBD_ObjectIdentity = ObjectIdentity
companyLBD = _CompanyLBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17)
)


class _SysLBDStateEnable_Type(Integer32):
    """Custom type sysLBDStateEnable based on Integer32"""
    defaultValue = 2

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


_SysLBDStateEnable_Type.__name__ = "Integer32"
_SysLBDStateEnable_Object = MibScalar
sysLBDStateEnable = _SysLBDStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 1),
    _SysLBDStateEnable_Type()
)
sysLBDStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDStateEnable.setStatus("current")


class _SysLBDMode_Type(Integer32):
    """Custom type sysLBDMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("vlan", 2))
    )


_SysLBDMode_Type.__name__ = "Integer32"
_SysLBDMode_Object = MibScalar
sysLBDMode = _SysLBDMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 2),
    _SysLBDMode_Type()
)
sysLBDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDMode.setStatus("current")


class _SysLBDInterval_Type(Integer32):
    """Custom type sysLBDInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SysLBDInterval_Type.__name__ = "Integer32"
_SysLBDInterval_Object = MibScalar
sysLBDInterval = _SysLBDInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 3),
    _SysLBDInterval_Type()
)
sysLBDInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDInterval.setStatus("current")


class _SysLBDRecoverTime_Type(Integer32):
    """Custom type sysLBDRecoverTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_SysLBDRecoverTime_Type.__name__ = "Integer32"
_SysLBDRecoverTime_Object = MibScalar
sysLBDRecoverTime = _SysLBDRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 4),
    _SysLBDRecoverTime_Type()
)
sysLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDRecoverTime.setStatus("current")
_SysLBDCtrlTable_Object = MibTable
sysLBDCtrlTable = _SysLBDCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 5)
)
if mibBuilder.loadTexts:
    sysLBDCtrlTable.setStatus("current")
_SysLBDCtrlEntry_Object = MibTableRow
sysLBDCtrlEntry = _SysLBDCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 5, 1)
)
sysLBDCtrlEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "sysLBDCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysLBDCtrlEntry.setStatus("current")
_SysLBDCtrlIndex_Type = Integer32
_SysLBDCtrlIndex_Object = MibTableColumn
sysLBDCtrlIndex = _SysLBDCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 5, 1, 1),
    _SysLBDCtrlIndex_Type()
)
sysLBDCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDCtrlIndex.setStatus("current")


class _SysLBDPortStatus_Type(Integer32):
    """Custom type sysLBDPortStatus based on Integer32"""
    defaultValue = 2

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


_SysLBDPortStatus_Type.__name__ = "Integer32"
_SysLBDPortStatus_Object = MibTableColumn
sysLBDPortStatus = _SysLBDPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 5, 1, 2),
    _SysLBDPortStatus_Type()
)
sysLBDPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDPortStatus.setStatus("current")


class _SysLBDPortLoopStatus_Type(Integer32):
    """Custom type sysLBDPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 2),
          ("normal", 1))
    )


_SysLBDPortLoopStatus_Type.__name__ = "Integer32"
_SysLBDPortLoopStatus_Object = MibTableColumn
sysLBDPortLoopStatus = _SysLBDPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 5, 1, 3),
    _SysLBDPortLoopStatus_Type()
)
sysLBDPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDPortLoopStatus.setStatus("current")
_SysLBDVlanLoopTable_Object = MibTable
sysLBDVlanLoopTable = _SysLBDVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 6)
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopTable.setStatus("current")
_SysLBDVlanLoopEntry_Object = MibTableRow
sysLBDVlanLoopEntry = _SysLBDVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 6, 1)
)
sysLBDVlanLoopEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "sysLBDVlanLoopIndex"),
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopEntry.setStatus("current")
_SysLBDVlanLoopIndex_Type = Integer32
_SysLBDVlanLoopIndex_Object = MibTableColumn
sysLBDVlanLoopIndex = _SysLBDVlanLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 6, 1, 1),
    _SysLBDVlanLoopIndex_Type()
)
sysLBDVlanLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopIndex.setStatus("current")
_SysLBDVlanLoopPorts_Type = PortList
_SysLBDVlanLoopPorts_Object = MibTableColumn
sysLBDVlanLoopPorts = _SysLBDVlanLoopPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 6, 1, 2),
    _SysLBDVlanLoopPorts_Type()
)
sysLBDVlanLoopPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopPorts.setStatus("current")
_SysLBDEnabledVlanList_Type = DisplayString
_SysLBDEnabledVlanList_Object = MibScalar
sysLBDEnabledVlanList = _SysLBDEnabledVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 7),
    _SysLBDEnabledVlanList_Type()
)
sysLBDEnabledVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDEnabledVlanList.setStatus("current")
_SysLBDTrap_ObjectIdentity = ObjectIdentity
sysLBDTrap = _SysLBDTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 8)
)
_LbdTraps_ObjectIdentity = ObjectIdentity
lbdTraps = _LbdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 8, 0)
)
_CompanyMirror_ObjectIdentity = ObjectIdentity
companyMirror = _CompanyMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18)
)


class _SysMirrorStatus_Type(Integer32):
    """Custom type sysMirrorStatus based on Integer32"""
    defaultValue = 2

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


_SysMirrorStatus_Type.__name__ = "Integer32"
_SysMirrorStatus_Object = MibScalar
sysMirrorStatus = _SysMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 1),
    _SysMirrorStatus_Type()
)
sysMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorStatus.setStatus("current")
_SysMirrorPortTable_Object = MibTable
sysMirrorPortTable = _SysMirrorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 2)
)
if mibBuilder.loadTexts:
    sysMirrorPortTable.setStatus("current")
_MirrorPortEntry_Object = MibTableRow
mirrorPortEntry = _MirrorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 2, 1)
)
mirrorPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "mirrorTargetIfIndex"),
)
if mibBuilder.loadTexts:
    mirrorPortEntry.setStatus("current")


class _MirrorTargetIfIndex_Type(Integer32):
    """Custom type mirrorTargetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MirrorTargetIfIndex_Type.__name__ = "Integer32"
_MirrorTargetIfIndex_Object = MibTableColumn
mirrorTargetIfIndex = _MirrorTargetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 2, 1, 1),
    _MirrorTargetIfIndex_Type()
)
mirrorTargetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorTargetIfIndex.setStatus("current")
_MirrorTargetPort_Type = Integer32
_MirrorTargetPort_Object = MibTableColumn
mirrorTargetPort = _MirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 2, 1, 2),
    _MirrorTargetPort_Type()
)
mirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorTargetPort.setStatus("current")
_MirrorIngressPortList_Type = PortList
_MirrorIngressPortList_Object = MibTableColumn
mirrorIngressPortList = _MirrorIngressPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 2, 1, 3),
    _MirrorIngressPortList_Type()
)
mirrorIngressPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorIngressPortList.setStatus("current")
_MirrorEgressPortList_Type = PortList
_MirrorEgressPortList_Object = MibTableColumn
mirrorEgressPortList = _MirrorEgressPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 2, 1, 4),
    _MirrorEgressPortList_Type()
)
mirrorEgressPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorEgressPortList.setStatus("current")
_MirrorCtrlRowStatus_Type = RowStatus
_MirrorCtrlRowStatus_Object = MibTableColumn
mirrorCtrlRowStatus = _MirrorCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 18, 2, 1, 5),
    _MirrorCtrlRowStatus_Type()
)
mirrorCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorCtrlRowStatus.setStatus("current")
_CompanyStaticMcast_ObjectIdentity = ObjectIdentity
companyStaticMcast = _CompanyStaticMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 19)
)
_SysStaticMcastTable_Object = MibTable
sysStaticMcastTable = _SysStaticMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 19, 1)
)
if mibBuilder.loadTexts:
    sysStaticMcastTable.setStatus("current")
_StaticMcastEntry_Object = MibTableRow
staticMcastEntry = _StaticMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 19, 1, 1)
)
staticMcastEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "staticMcastVlanID"),
    (0, "DGS-1100-10ME_A1", "staticMcastMac"),
    (0, "DGS-1100-10ME_A1", "staticMcastEgressPorts"),
)
if mibBuilder.loadTexts:
    staticMcastEntry.setStatus("current")
_StaticMcastVlanID_Type = Integer32
_StaticMcastVlanID_Object = MibTableColumn
staticMcastVlanID = _StaticMcastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 19, 1, 1, 1),
    _StaticMcastVlanID_Type()
)
staticMcastVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastVlanID.setStatus("current")
_StaticMcastMac_Type = MacAddress
_StaticMcastMac_Object = MibTableColumn
staticMcastMac = _StaticMcastMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 19, 1, 1, 2),
    _StaticMcastMac_Type()
)
staticMcastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastMac.setStatus("current")
_StaticMcastEgressPorts_Type = PortList
_StaticMcastEgressPorts_Object = MibTableColumn
staticMcastEgressPorts = _StaticMcastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 19, 1, 1, 3),
    _StaticMcastEgressPorts_Type()
)
staticMcastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastEgressPorts.setStatus("current")
_StaticMcastStatus_Type = RowStatus
_StaticMcastStatus_Object = MibTableColumn
staticMcastStatus = _StaticMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 19, 1, 1, 4),
    _StaticMcastStatus_Type()
)
staticMcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMcastStatus.setStatus("current")
_CompanySNTPSetting_ObjectIdentity = ObjectIdentity
companySNTPSetting = _CompanySNTPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20)
)
_SysSNTPSettingGroup_ObjectIdentity = ObjectIdentity
sysSNTPSettingGroup = _SysSNTPSettingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17)
)
_SntpTimeSeconds_Type = Integer32
_SntpTimeSeconds_Object = MibScalar
sntpTimeSeconds = _SntpTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 1),
    _SntpTimeSeconds_Type()
)
sntpTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpTimeSeconds.setStatus("current")
_SntpPollInterval_Type = Integer32
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 8),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")


class _SntpGlobalState_Type(Integer32):
    """Custom type sntpGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("sntp", 1))
    )


_SntpGlobalState_Type.__name__ = "Integer32"
_SntpGlobalState_Object = MibScalar
sntpGlobalState = _SntpGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 9),
    _SntpGlobalState_Type()
)
sntpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpGlobalState.setStatus("current")


class _SntpDSTOffset_Type(Integer32):
    """Custom type sntpDSTOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              60,
              90,
              120)
        )
    )
    namedValues = NamedValues(
        *(("offset120min", 120),
          ("offset30min", 30),
          ("offset60min", 60),
          ("offset90min", 90))
    )


_SntpDSTOffset_Type.__name__ = "Integer32"
_SntpDSTOffset_Object = MibScalar
sntpDSTOffset = _SntpDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 10),
    _SntpDSTOffset_Type()
)
sntpDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDSTOffset.setStatus("current")
_SntpGMTMinutes_Type = Integer32
_SntpGMTMinutes_Object = MibScalar
sntpGMTMinutes = _SntpGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 11),
    _SntpGMTMinutes_Type()
)
sntpGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpGMTMinutes.setStatus("current")


class _SntpDSTStartTime_Type(DisplayString):
    """Custom type sntpDSTStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SntpDSTStartTime_Type.__name__ = "DisplayString"
_SntpDSTStartTime_Object = MibScalar
sntpDSTStartTime = _SntpDSTStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 12),
    _SntpDSTStartTime_Type()
)
sntpDSTStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDSTStartTime.setStatus("current")


class _SntpDSTEndTime_Type(DisplayString):
    """Custom type sntpDSTEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SntpDSTEndTime_Type.__name__ = "DisplayString"
_SntpDSTEndTime_Object = MibScalar
sntpDSTEndTime = _SntpDSTEndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 13),
    _SntpDSTEndTime_Type()
)
sntpDSTEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDSTEndTime.setStatus("current")


class _SntpDSTState_Type(Integer32):
    """Custom type sntpDSTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annual", 1),
          ("disabled", 2))
    )


_SntpDSTState_Type.__name__ = "Integer32"
_SntpDSTState_Object = MibScalar
sntpDSTState = _SntpDSTState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 17, 20),
    _SntpDSTState_Type()
)
sntpDSTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDSTState.setStatus("current")
_SysSNTPServerGroup_ObjectIdentity = ObjectIdentity
sysSNTPServerGroup = _SysSNTPServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 18)
)
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 18, 1)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 18, 1, 1)
)
sntpServerEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "sntpServerAddrType"),
    (0, "DGS-1100-10ME_A1", "sntpServerAddr"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")


class _SntpServerAddrType_Type(Integer32):
    """Custom type sntpServerAddrType based on Integer32"""
    defaultValue = 1

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


_SntpServerAddrType_Type.__name__ = "Integer32"
_SntpServerAddrType_Object = MibTableColumn
sntpServerAddrType = _SntpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 18, 1, 1, 1),
    _SntpServerAddrType_Type()
)
sntpServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerAddrType.setStatus("current")
_SntpServerAddr_Type = InetAddress
_SntpServerAddr_Object = MibTableColumn
sntpServerAddr = _SntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 18, 1, 1, 2),
    _SntpServerAddr_Type()
)
sntpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpServerAddr.setStatus("current")


class _SntpServerType_Type(Integer32):
    """Custom type sntpServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SntpServerType_Type.__name__ = "Integer32"
_SntpServerType_Object = MibTableColumn
sntpServerType = _SntpServerType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 18, 1, 1, 4),
    _SntpServerType_Type()
)
sntpServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerType.setStatus("current")
_SntpServerRowStatus_Type = RowStatus
_SntpServerRowStatus_Object = MibTableColumn
sntpServerRowStatus = _SntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 20, 18, 1, 1, 5),
    _SntpServerRowStatus_Type()
)
sntpServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerRowStatus.setStatus("current")
_CompanyRMON_ObjectIdentity = ObjectIdentity
companyRMON = _CompanyRMON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22)
)


class _SysRMONGlobalState_Type(Integer32):
    """Custom type sysRMONGlobalState based on Integer32"""
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


_SysRMONGlobalState_Type.__name__ = "Integer32"
_SysRMONGlobalState_Object = MibScalar
sysRMONGlobalState = _SysRMONGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 1),
    _SysRMONGlobalState_Type()
)
sysRMONGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRMONGlobalState.setStatus("current")
_SysRMONStatistics_ObjectIdentity = ObjectIdentity
sysRMONStatistics = _SysRMONStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2)
)
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1)
)
rmonStatsEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "rmonStatsIndex"),
)
if mibBuilder.loadTexts:
    rmonStatsEntry.setStatus("current")


class _RmonStatsIndex_Type(Integer32):
    """Custom type rmonStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonStatsIndex_Type.__name__ = "Integer32"
_RmonStatsIndex_Object = MibTableColumn
rmonStatsIndex = _RmonStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 1),
    _RmonStatsIndex_Type()
)
rmonStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsIndex.setStatus("current")
_RmonStatsDataSource_Type = ObjectIdentifier
_RmonStatsDataSource_Object = MibTableColumn
rmonStatsDataSource = _RmonStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 2),
    _RmonStatsDataSource_Type()
)
rmonStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatsDataSource.setStatus("current")
_RmonStatsOwner_Type = OwnerString
_RmonStatsOwner_Object = MibTableColumn
rmonStatsOwner = _RmonStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 3),
    _RmonStatsOwner_Type()
)
rmonStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatsOwner.setStatus("current")
_RmonStatsStatus_Type = RmonStatus
_RmonStatsStatus_Object = MibTableColumn
rmonStatsStatus = _RmonStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 4),
    _RmonStatsStatus_Type()
)
rmonStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonStatsStatus.setStatus("current")
_RmonStatsDropEvents_Type = Counter32
_RmonStatsDropEvents_Object = MibTableColumn
rmonStatsDropEvents = _RmonStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 5),
    _RmonStatsDropEvents_Type()
)
rmonStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsDropEvents.setStatus("current")
_RmonStatsOctets_Type = Counter32
_RmonStatsOctets_Object = MibTableColumn
rmonStatsOctets = _RmonStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 6),
    _RmonStatsOctets_Type()
)
rmonStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsOctets.setUnits("Octets")
_RmonStatsPkts_Type = Counter32
_RmonStatsPkts_Object = MibTableColumn
rmonStatsPkts = _RmonStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 7),
    _RmonStatsPkts_Type()
)
rmonStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsPkts.setUnits("Packets")
_RmonStatsBroadcastPkts_Type = Counter32
_RmonStatsBroadcastPkts_Object = MibTableColumn
rmonStatsBroadcastPkts = _RmonStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 8),
    _RmonStatsBroadcastPkts_Type()
)
rmonStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsBroadcastPkts.setUnits("Packets")
_RmonStatsMulticastPkts_Type = Counter32
_RmonStatsMulticastPkts_Object = MibTableColumn
rmonStatsMulticastPkts = _RmonStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 2, 1, 1, 9),
    _RmonStatsMulticastPkts_Type()
)
rmonStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rmonStatsMulticastPkts.setUnits("Packets")
_SysRMONHistory_ObjectIdentity = ObjectIdentity
sysRMONHistory = _SysRMONHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3)
)
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "rmonHistoryIndex"),
)
if mibBuilder.loadTexts:
    rmonHistoryEntry.setStatus("current")


class _RmonHistoryIndex_Type(Integer32):
    """Custom type rmonHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonHistoryIndex_Type.__name__ = "Integer32"
_RmonHistoryIndex_Object = MibTableColumn
rmonHistoryIndex = _RmonHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")
_RmonHistoryDataSource_Type = ObjectIdentifier
_RmonHistoryDataSource_Object = MibTableColumn
rmonHistoryDataSource = _RmonHistoryDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1, 1, 2),
    _RmonHistoryDataSource_Type()
)
rmonHistoryDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryDataSource.setStatus("current")


class _RmonHistoryBucketsRequested_Type(Integer32):
    """Custom type rmonHistoryBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_RmonHistoryBucketsRequested_Type.__name__ = "Integer32"
_RmonHistoryBucketsRequested_Object = MibTableColumn
rmonHistoryBucketsRequested = _RmonHistoryBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1, 1, 3),
    _RmonHistoryBucketsRequested_Type()
)
rmonHistoryBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryBucketsRequested.setStatus("current")


class _RmonHistoryInterval_Type(Integer32):
    """Custom type rmonHistoryInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RmonHistoryInterval_Type.__name__ = "Integer32"
_RmonHistoryInterval_Object = MibTableColumn
rmonHistoryInterval = _RmonHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1, 1, 4),
    _RmonHistoryInterval_Type()
)
rmonHistoryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryInterval.setUnits("Seconds")
_RmonHistoryOwner_Type = OwnerString
_RmonHistoryOwner_Object = MibTableColumn
rmonHistoryOwner = _RmonHistoryOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1, 1, 5),
    _RmonHistoryOwner_Type()
)
rmonHistoryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryOwner.setStatus("current")
_RmonHistoryStatus_Type = RmonStatus
_RmonHistoryStatus_Object = MibTableColumn
rmonHistoryStatus = _RmonHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 3, 1, 1, 6),
    _RmonHistoryStatus_Type()
)
rmonHistoryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHistoryStatus.setStatus("current")
_SysRMONAlarm_ObjectIdentity = ObjectIdentity
sysRMONAlarm = _SysRMONAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4)
)
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "rmonAlarmIndex"),
)
if mibBuilder.loadTexts:
    rmonAlarmEntry.setStatus("current")


class _RmonAlarmIndex_Type(Integer32):
    """Custom type rmonAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonAlarmIndex_Type.__name__ = "Integer32"
_RmonAlarmIndex_Object = MibTableColumn
rmonAlarmIndex = _RmonAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")
_RmonAlarmInterval_Type = Integer32
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 2),
    _RmonAlarmInterval_Type()
)
rmonAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    rmonAlarmInterval.setUnits("Seconds")
_RmonAlarmVariable_Type = ObjectIdentifier
_RmonAlarmVariable_Object = MibTableColumn
rmonAlarmVariable = _RmonAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 3),
    _RmonAlarmVariable_Type()
)
rmonAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmVariable.setStatus("current")


class _RmonAlarmSampleType_Type(Integer32):
    """Custom type rmonAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_RmonAlarmSampleType_Type.__name__ = "Integer32"
_RmonAlarmSampleType_Object = MibTableColumn
rmonAlarmSampleType = _RmonAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")
_RmonAlarmRisingThreshold_Type = Integer32
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 5),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")
_RmonAlarmFallingThreshold_Type = Integer32
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 6),
    _RmonAlarmFallingThreshold_Type()
)
rmonAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmFallingThreshold.setStatus("current")


class _RmonAlarmRisingEventIndex_Type(Integer32):
    """Custom type rmonAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmonAlarmRisingEventIndex_Type.__name__ = "Integer32"
_RmonAlarmRisingEventIndex_Object = MibTableColumn
rmonAlarmRisingEventIndex = _RmonAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 7),
    _RmonAlarmRisingEventIndex_Type()
)
rmonAlarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmRisingEventIndex.setStatus("current")


class _RmonAlarmFallingEventIndex_Type(Integer32):
    """Custom type rmonAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmonAlarmFallingEventIndex_Type.__name__ = "Integer32"
_RmonAlarmFallingEventIndex_Object = MibTableColumn
rmonAlarmFallingEventIndex = _RmonAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 8),
    _RmonAlarmFallingEventIndex_Type()
)
rmonAlarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmFallingEventIndex.setStatus("current")
_RmonAlarmOwner_Type = OwnerString
_RmonAlarmOwner_Object = MibTableColumn
rmonAlarmOwner = _RmonAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 9),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")
_RmonAlarmStatus_Type = RmonStatus
_RmonAlarmStatus_Object = MibTableColumn
rmonAlarmStatus = _RmonAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 4, 1, 1, 10),
    _RmonAlarmStatus_Type()
)
rmonAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmStatus.setStatus("current")
_SysRMONEvent_ObjectIdentity = ObjectIdentity
sysRMONEvent = _SysRMONEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5)
)
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1)
)
rmonEventEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "rmonEventIndex"),
)
if mibBuilder.loadTexts:
    rmonEventEntry.setStatus("current")


class _RmonEventIndex_Type(Integer32):
    """Custom type rmonEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonEventIndex_Type.__name__ = "Integer32"
_RmonEventIndex_Object = MibTableColumn
rmonEventIndex = _RmonEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1, 1),
    _RmonEventIndex_Type()
)
rmonEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonEventIndex.setStatus("current")


class _RmonEventDescription_Type(DisplayString):
    """Custom type rmonEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RmonEventDescription_Type.__name__ = "DisplayString"
_RmonEventDescription_Object = MibTableColumn
rmonEventDescription = _RmonEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1, 2),
    _RmonEventDescription_Type()
)
rmonEventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventDescription.setStatus("current")


class _RmonEventType_Type(Integer32):
    """Custom type rmonEventType based on Integer32"""
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
        *(("log", 2),
          ("logandtrap", 4),
          ("none", 1),
          ("snmptrap", 3))
    )


_RmonEventType_Type.__name__ = "Integer32"
_RmonEventType_Object = MibTableColumn
rmonEventType = _RmonEventType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1, 3),
    _RmonEventType_Type()
)
rmonEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventType.setStatus("current")
_RmonEventCommunity_Type = OwnerString
_RmonEventCommunity_Object = MibTableColumn
rmonEventCommunity = _RmonEventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1, 4),
    _RmonEventCommunity_Type()
)
rmonEventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventCommunity.setStatus("current")
_RmonEventOwner_Type = OwnerString
_RmonEventOwner_Object = MibTableColumn
rmonEventOwner = _RmonEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")
_RmonEventStatus_Type = RmonStatus
_RmonEventStatus_Object = MibTableColumn
rmonEventStatus = _RmonEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1, 6),
    _RmonEventStatus_Type()
)
rmonEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEventStatus.setStatus("current")
_RmonEventLastTimeSent_Type = TimeTicks
_RmonEventLastTimeSent_Object = MibTableColumn
rmonEventLastTimeSent = _RmonEventLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 22, 5, 1, 1, 7),
    _RmonEventLastTimeSent_Type()
)
rmonEventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonEventLastTimeSent.setStatus("current")
_CompanyPnacGroup_ObjectIdentity = ObjectIdentity
companyPnacGroup = _CompanyPnacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23)
)
_SysPnacCtrl_ObjectIdentity = ObjectIdentity
sysPnacCtrl = _SysPnacCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 1)
)


class _PnacStatus_Type(Integer32):
    """Custom type pnacStatus based on Integer32"""
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


_PnacStatus_Type.__name__ = "Integer32"
_PnacStatus_Object = MibScalar
pnacStatus = _PnacStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 1, 1),
    _PnacStatus_Type()
)
pnacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacStatus.setStatus("current")


class _PnacMode_Type(Integer32):
    """Custom type pnacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macBase", 2),
          ("portBase", 1))
    )


_PnacMode_Type.__name__ = "Integer32"
_PnacMode_Object = MibScalar
pnacMode = _PnacMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 1, 2),
    _PnacMode_Type()
)
pnacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacMode.setStatus("current")


class _PnacProtocol_Type(Integer32):
    """Custom type pnacProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pnacProtocolLocal", 2),
          ("pnacProtocolRadiusEap", 1))
    )


_PnacProtocol_Type.__name__ = "Integer32"
_PnacProtocol_Object = MibScalar
pnacProtocol = _PnacProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 1, 3),
    _PnacProtocol_Type()
)
pnacProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacProtocol.setStatus("current")


class _PnacRadiusAccountingState_Type(Integer32):
    """Custom type pnacRadiusAccountingState based on Integer32"""
    defaultValue = 2

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


_PnacRadiusAccountingState_Type.__name__ = "Integer32"
_PnacRadiusAccountingState_Object = MibScalar
pnacRadiusAccountingState = _PnacRadiusAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 1, 4),
    _PnacRadiusAccountingState_Type()
)
pnacRadiusAccountingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusAccountingState.setStatus("current")
_SysPnacPortAccessCtrl_ObjectIdentity = ObjectIdentity
sysPnacPortAccessCtrl = _SysPnacPortAccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2)
)
_PnacPortAccessControlTable_Object = MibTable
pnacPortAccessControlTable = _PnacPortAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    pnacPortAccessControlTable.setStatus("current")
_PnacPortAccessControlEntry_Object = MibTableRow
pnacPortAccessControlEntry = _PnacPortAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1)
)
pnacPortAccessControlEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "pnacConfigPortNumber"),
)
if mibBuilder.loadTexts:
    pnacPortAccessControlEntry.setStatus("current")
_PnacConfigPortNumber_Type = Integer32
_PnacConfigPortNumber_Object = MibTableColumn
pnacConfigPortNumber = _PnacConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 1),
    _PnacConfigPortNumber_Type()
)
pnacConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnacConfigPortNumber.setStatus("current")


class _PnacQuietPeriod_Type(Unsigned32):
    """Custom type pnacQuietPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnacQuietPeriod_Type.__name__ = "Unsigned32"
_PnacQuietPeriod_Object = MibTableColumn
pnacQuietPeriod = _PnacQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 2),
    _PnacQuietPeriod_Type()
)
pnacQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacQuietPeriod.setStatus("current")


class _PnacTxPeriod_Type(Unsigned32):
    """Custom type pnacTxPeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnacTxPeriod_Type.__name__ = "Unsigned32"
_PnacTxPeriod_Object = MibTableColumn
pnacTxPeriod = _PnacTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 3),
    _PnacTxPeriod_Type()
)
pnacTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacTxPeriod.setStatus("current")


class _PnacSuppTimeout_Type(Unsigned32):
    """Custom type pnacSuppTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnacSuppTimeout_Type.__name__ = "Unsigned32"
_PnacSuppTimeout_Object = MibTableColumn
pnacSuppTimeout = _PnacSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 4),
    _PnacSuppTimeout_Type()
)
pnacSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacSuppTimeout.setStatus("current")


class _PnacServerTimeout_Type(Unsigned32):
    """Custom type pnacServerTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnacServerTimeout_Type.__name__ = "Unsigned32"
_PnacServerTimeout_Object = MibTableColumn
pnacServerTimeout = _PnacServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 5),
    _PnacServerTimeout_Type()
)
pnacServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacServerTimeout.setStatus("current")


class _PnacMaxReq_Type(Unsigned32):
    """Custom type pnacMaxReq based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PnacMaxReq_Type.__name__ = "Unsigned32"
_PnacMaxReq_Object = MibTableColumn
pnacMaxReq = _PnacMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 6),
    _PnacMaxReq_Type()
)
pnacMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacMaxReq.setStatus("current")


class _PnacReAuthPeriod_Type(Unsigned32):
    """Custom type pnacReAuthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnacReAuthPeriod_Type.__name__ = "Unsigned32"
_PnacReAuthPeriod_Object = MibTableColumn
pnacReAuthPeriod = _PnacReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 7),
    _PnacReAuthPeriod_Type()
)
pnacReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacReAuthPeriod.setStatus("current")


class _PnacReAuthentication_Type(Integer32):
    """Custom type pnacReAuthentication based on Integer32"""
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


_PnacReAuthentication_Type.__name__ = "Integer32"
_PnacReAuthentication_Object = MibTableColumn
pnacReAuthentication = _PnacReAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 8),
    _PnacReAuthentication_Type()
)
pnacReAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacReAuthentication.setStatus("current")


class _PnacConfigPortControl_Type(Integer32):
    """Custom type pnacConfigPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceAuthorized", 3),
          ("forceUnauthorized", 1))
    )


_PnacConfigPortControl_Type.__name__ = "Integer32"
_PnacConfigPortControl_Object = MibTableColumn
pnacConfigPortControl = _PnacConfigPortControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 9),
    _PnacConfigPortControl_Type()
)
pnacConfigPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacConfigPortControl.setStatus("current")


class _PnacCapability_Type(Integer32):
    """Custom type pnacCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticator", 1),
          ("none", 2))
    )


_PnacCapability_Type.__name__ = "Integer32"
_PnacCapability_Object = MibTableColumn
pnacCapability = _PnacCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 10),
    _PnacCapability_Type()
)
pnacCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacCapability.setStatus("current")


class _PnacDirection_Type(Integer32):
    """Custom type pnacDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("in", 1))
    )


_PnacDirection_Type.__name__ = "Integer32"
_PnacDirection_Object = MibTableColumn
pnacDirection = _PnacDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 11),
    _PnacDirection_Type()
)
pnacDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacDirection.setStatus("current")


class _PnacOperControlledDirections_Type(Integer32):
    """Custom type pnacOperControlledDirections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("in", 1))
    )


_PnacOperControlledDirections_Type.__name__ = "Integer32"
_PnacOperControlledDirections_Object = MibTableColumn
pnacOperControlledDirections = _PnacOperControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 12),
    _PnacOperControlledDirections_Type()
)
pnacOperControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnacOperControlledDirections.setStatus("current")


class _PnacPortAuthStatus_Type(Integer32):
    """Custom type pnacPortAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unAuthorized", 2))
    )


_PnacPortAuthStatus_Type.__name__ = "Integer32"
_PnacPortAuthStatus_Object = MibTableColumn
pnacPortAuthStatus = _PnacPortAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 2, 1, 1, 13),
    _PnacPortAuthStatus_Type()
)
pnacPortAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnacPortAuthStatus.setStatus("current")
_SysPnacUser_ObjectIdentity = ObjectIdentity
sysPnacUser = _SysPnacUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 3)
)
_PnacUserTable_Object = MibTable
pnacUserTable = _PnacUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 3, 1)
)
if mibBuilder.loadTexts:
    pnacUserTable.setStatus("current")
_PnacUserEntry_Object = MibTableRow
pnacUserEntry = _PnacUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 3, 1, 1)
)
pnacUserEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "pnacUserName"),
)
if mibBuilder.loadTexts:
    pnacUserEntry.setStatus("current")


class _PnacUserName_Type(SnmpAdminString):
    """Custom type pnacUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_PnacUserName_Type.__name__ = "SnmpAdminString"
_PnacUserName_Object = MibTableColumn
pnacUserName = _PnacUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 3, 1, 1, 1),
    _PnacUserName_Type()
)
pnacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnacUserName.setStatus("current")


class _PnacUserPassword_Type(DisplayString):
    """Custom type pnacUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_PnacUserPassword_Type.__name__ = "DisplayString"
_PnacUserPassword_Object = MibTableColumn
pnacUserPassword = _PnacUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 3, 1, 1, 2),
    _PnacUserPassword_Type()
)
pnacUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacUserPassword.setStatus("current")
_PnacUserStatus_Type = RowStatus
_PnacUserStatus_Object = MibTableColumn
pnacUserStatus = _PnacUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 3, 1, 1, 3),
    _PnacUserStatus_Type()
)
pnacUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacUserStatus.setStatus("current")
_SysPnacRadiusServer_ObjectIdentity = ObjectIdentity
sysPnacRadiusServer = _SysPnacRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4)
)
_PnacRadiusServerTable_Object = MibTable
pnacRadiusServerTable = _PnacRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1)
)
if mibBuilder.loadTexts:
    pnacRadiusServerTable.setStatus("current")
_PnacRadiusServerEntry_Object = MibTableRow
pnacRadiusServerEntry = _PnacRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1)
)
pnacRadiusServerEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "pnacRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    pnacRadiusServerEntry.setStatus("current")


class _PnacRadiusServerIndex_Type(Integer32):
    """Custom type pnacRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PnacRadiusServerIndex_Type.__name__ = "Integer32"
_PnacRadiusServerIndex_Object = MibTableColumn
pnacRadiusServerIndex = _PnacRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 1),
    _PnacRadiusServerIndex_Type()
)
pnacRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnacRadiusServerIndex.setStatus("current")


class _PnacRadiusIPType_Type(Integer32):
    """Custom type pnacRadiusIPType based on Integer32"""
    defaultValue = 1

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


_PnacRadiusIPType_Type.__name__ = "Integer32"
_PnacRadiusIPType_Object = MibTableColumn
pnacRadiusIPType = _PnacRadiusIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 2),
    _PnacRadiusIPType_Type()
)
pnacRadiusIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusIPType.setStatus("current")
_PnacRadiusServerAddress_Type = InetAddress
_PnacRadiusServerAddress_Object = MibTableColumn
pnacRadiusServerAddress = _PnacRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 3),
    _PnacRadiusServerAddress_Type()
)
pnacRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusServerAddress.setStatus("current")


class _PnacRadiusServerAuthenticationPort_Type(Integer32):
    """Custom type pnacRadiusServerAuthenticationPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnacRadiusServerAuthenticationPort_Type.__name__ = "Integer32"
_PnacRadiusServerAuthenticationPort_Object = MibTableColumn
pnacRadiusServerAuthenticationPort = _PnacRadiusServerAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 5),
    _PnacRadiusServerAuthenticationPort_Type()
)
pnacRadiusServerAuthenticationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusServerAuthenticationPort.setStatus("current")


class _PnacRadiusServerAccountingPort_Type(Integer32):
    """Custom type pnacRadiusServerAccountingPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnacRadiusServerAccountingPort_Type.__name__ = "Integer32"
_PnacRadiusServerAccountingPort_Object = MibTableColumn
pnacRadiusServerAccountingPort = _PnacRadiusServerAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 6),
    _PnacRadiusServerAccountingPort_Type()
)
pnacRadiusServerAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusServerAccountingPort.setStatus("current")


class _PnacRadiusServerTimeout_Type(Integer32):
    """Custom type pnacRadiusServerTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PnacRadiusServerTimeout_Type.__name__ = "Integer32"
_PnacRadiusServerTimeout_Object = MibTableColumn
pnacRadiusServerTimeout = _PnacRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 7),
    _PnacRadiusServerTimeout_Type()
)
pnacRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusServerTimeout.setStatus("current")


class _PnacRadiusServerRetransmit_Type(Integer32):
    """Custom type pnacRadiusServerRetransmit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PnacRadiusServerRetransmit_Type.__name__ = "Integer32"
_PnacRadiusServerRetransmit_Object = MibTableColumn
pnacRadiusServerRetransmit = _PnacRadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 8),
    _PnacRadiusServerRetransmit_Type()
)
pnacRadiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusServerRetransmit.setStatus("current")


class _PnacRadiusServerKey_Type(DisplayString):
    """Custom type pnacRadiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PnacRadiusServerKey_Type.__name__ = "DisplayString"
_PnacRadiusServerKey_Object = MibTableColumn
pnacRadiusServerKey = _PnacRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 9),
    _PnacRadiusServerKey_Type()
)
pnacRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusServerKey.setStatus("current")
_PnacRadiusServerStatus_Type = RowStatus
_PnacRadiusServerStatus_Object = MibTableColumn
pnacRadiusServerStatus = _PnacRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 23, 4, 1, 1, 10),
    _PnacRadiusServerStatus_Type()
)
pnacRadiusServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnacRadiusServerStatus.setStatus("current")
_CompanyGuestVLAN_ObjectIdentity = ObjectIdentity
companyGuestVLAN = _CompanyGuestVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 24)
)


class _SysGuestVlanName_Type(DisplayString):
    """Custom type sysGuestVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SysGuestVlanName_Type.__name__ = "DisplayString"
_SysGuestVlanName_Object = MibScalar
sysGuestVlanName = _SysGuestVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 24, 1),
    _SysGuestVlanName_Type()
)
sysGuestVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGuestVlanName.setStatus("current")
_SysGuestVlanPort_Type = PortList
_SysGuestVlanPort_Object = MibScalar
sysGuestVlanPort = _SysGuestVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 24, 2),
    _SysGuestVlanPort_Type()
)
sysGuestVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGuestVlanPort.setStatus("current")


class _SysGuestVlanDelState_Type(Integer32):
    """Custom type sysGuestVlanDelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SysGuestVlanDelState_Type.__name__ = "Integer32"
_SysGuestVlanDelState_Object = MibScalar
sysGuestVlanDelState = _SysGuestVlanDelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 24, 3),
    _SysGuestVlanDelState_Type()
)
sysGuestVlanDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGuestVlanDelState.setStatus("current")
_CompanyMacNotify_ObjectIdentity = ObjectIdentity
companyMacNotify = _CompanyMacNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25)
)


class _SysMacNotifyState_Type(Integer32):
    """Custom type sysMacNotifyState based on Integer32"""
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


_SysMacNotifyState_Type.__name__ = "Integer32"
_SysMacNotifyState_Object = MibScalar
sysMacNotifyState = _SysMacNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 1),
    _SysMacNotifyState_Type()
)
sysMacNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMacNotifyState.setStatus("current")


class _SysmacNotifyInterval_Type(Integer32):
    """Custom type sysmacNotifyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysmacNotifyInterval_Type.__name__ = "Integer32"
_SysmacNotifyInterval_Object = MibScalar
sysmacNotifyInterval = _SysmacNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 2),
    _SysmacNotifyInterval_Type()
)
sysmacNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysmacNotifyInterval.setStatus("current")


class _SysmacNotifyHistorySize_Type(Integer32):
    """Custom type sysmacNotifyHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SysmacNotifyHistorySize_Type.__name__ = "Integer32"
_SysmacNotifyHistorySize_Object = MibScalar
sysmacNotifyHistorySize = _SysmacNotifyHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 3),
    _SysmacNotifyHistorySize_Type()
)
sysmacNotifyHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysmacNotifyHistorySize.setStatus("current")
_SysmacNotifyCtrlTable_Object = MibTable
sysmacNotifyCtrlTable = _SysmacNotifyCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 4)
)
if mibBuilder.loadTexts:
    sysmacNotifyCtrlTable.setStatus("current")
_MacNotifyCtrlEntry_Object = MibTableRow
macNotifyCtrlEntry = _MacNotifyCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 4, 1)
)
macNotifyCtrlEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "macNotifyPortIndex"),
)
if mibBuilder.loadTexts:
    macNotifyCtrlEntry.setStatus("current")
_MacNotifyPortIndex_Type = Integer32
_MacNotifyPortIndex_Object = MibTableColumn
macNotifyPortIndex = _MacNotifyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 4, 1, 1),
    _MacNotifyPortIndex_Type()
)
macNotifyPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macNotifyPortIndex.setStatus("current")


class _MacNotifyPortStatus_Type(Integer32):
    """Custom type macNotifyPortStatus based on Integer32"""
    defaultValue = 2

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


_MacNotifyPortStatus_Type.__name__ = "Integer32"
_MacNotifyPortStatus_Object = MibTableColumn
macNotifyPortStatus = _MacNotifyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 4, 1, 2),
    _MacNotifyPortStatus_Type()
)
macNotifyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macNotifyPortStatus.setStatus("current")
_SysMacNotifyTraps_ObjectIdentity = ObjectIdentity
sysMacNotifyTraps = _SysMacNotifyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 5)
)
_CompanyISMVLAN_ObjectIdentity = ObjectIdentity
companyISMVLAN = _CompanyISMVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27)
)


class _SysIGMPMulticastVlanStatus_Type(Integer32):
    """Custom type sysIGMPMulticastVlanStatus based on Integer32"""
    defaultValue = 2

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


_SysIGMPMulticastVlanStatus_Type.__name__ = "Integer32"
_SysIGMPMulticastVlanStatus_Object = MibScalar
sysIGMPMulticastVlanStatus = _SysIGMPMulticastVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 1),
    _SysIGMPMulticastVlanStatus_Type()
)
sysIGMPMulticastVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIGMPMulticastVlanStatus.setStatus("current")
_SysIGMPMulticastVlanTable_Object = MibTable
sysIGMPMulticastVlanTable = _SysIGMPMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2)
)
if mibBuilder.loadTexts:
    sysIGMPMulticastVlanTable.setStatus("current")
_SysIGMPMulticastVlanEntry_Object = MibTableRow
sysIGMPMulticastVlanEntry = _SysIGMPMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1)
)
sysIGMPMulticastVlanEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "igmpMulticastVlanid"),
    (0, "DGS-1100-10ME_A1", "igmpMulticastVlanAddressType"),
)
if mibBuilder.loadTexts:
    sysIGMPMulticastVlanEntry.setStatus("current")


class _IgmpMulticastVlanid_Type(Integer32):
    """Custom type igmpMulticastVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpMulticastVlanid_Type.__name__ = "Integer32"
_IgmpMulticastVlanid_Object = MibTableColumn
igmpMulticastVlanid = _IgmpMulticastVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 1),
    _IgmpMulticastVlanid_Type()
)
igmpMulticastVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanid.setStatus("current")
_IgmpMulticastVlanAddressType_Type = InetAddressType
_IgmpMulticastVlanAddressType_Object = MibTableColumn
igmpMulticastVlanAddressType = _IgmpMulticastVlanAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 2),
    _IgmpMulticastVlanAddressType_Type()
)
igmpMulticastVlanAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanAddressType.setStatus("current")


class _IgmpMulticastVlanName_Type(DisplayString):
    """Custom type igmpMulticastVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IgmpMulticastVlanName_Type.__name__ = "DisplayString"
_IgmpMulticastVlanName_Object = MibTableColumn
igmpMulticastVlanName = _IgmpMulticastVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 3),
    _IgmpMulticastVlanName_Type()
)
igmpMulticastVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanName.setStatus("current")
_IgmpMulticastVlanSourcePort_Type = PortList
_IgmpMulticastVlanSourcePort_Object = MibTableColumn
igmpMulticastVlanSourcePort = _IgmpMulticastVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 4),
    _IgmpMulticastVlanSourcePort_Type()
)
igmpMulticastVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanSourcePort.setStatus("current")
_IgmpMulticastVlanMemberPort_Type = PortList
_IgmpMulticastVlanMemberPort_Object = MibTableColumn
igmpMulticastVlanMemberPort = _IgmpMulticastVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 5),
    _IgmpMulticastVlanMemberPort_Type()
)
igmpMulticastVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanMemberPort.setStatus("current")
_IgmpMulticastVlanTagMemberPort_Type = PortList
_IgmpMulticastVlanTagMemberPort_Object = MibTableColumn
igmpMulticastVlanTagMemberPort = _IgmpMulticastVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 6),
    _IgmpMulticastVlanTagMemberPort_Type()
)
igmpMulticastVlanTagMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanTagMemberPort.setStatus("current")


class _IgmpMulticastVlanState_Type(Integer32):
    """Custom type igmpMulticastVlanState based on Integer32"""
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


_IgmpMulticastVlanState_Type.__name__ = "Integer32"
_IgmpMulticastVlanState_Object = MibTableColumn
igmpMulticastVlanState = _IgmpMulticastVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 7),
    _IgmpMulticastVlanState_Type()
)
igmpMulticastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanState.setStatus("current")
_IgmpMulticastVlanReplaceSourceIp_Type = DisplayString
_IgmpMulticastVlanReplaceSourceIp_Object = MibTableColumn
igmpMulticastVlanReplaceSourceIp = _IgmpMulticastVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 8),
    _IgmpMulticastVlanReplaceSourceIp_Type()
)
igmpMulticastVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanReplaceSourceIp.setStatus("current")
_IgmpMulticastVlanRowStatus_Type = RowStatus
_IgmpMulticastVlanRowStatus_Object = MibTableColumn
igmpMulticastVlanRowStatus = _IgmpMulticastVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 2, 1, 9),
    _IgmpMulticastVlanRowStatus_Type()
)
igmpMulticastVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanRowStatus.setStatus("current")
_SysIGMPMulticastVlanGroupTable_Object = MibTable
sysIGMPMulticastVlanGroupTable = _SysIGMPMulticastVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 3)
)
if mibBuilder.loadTexts:
    sysIGMPMulticastVlanGroupTable.setStatus("current")
_SysIGMPMulticastVlanGroupEntry_Object = MibTableRow
sysIGMPMulticastVlanGroupEntry = _SysIGMPMulticastVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 3, 1)
)
sysIGMPMulticastVlanGroupEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "igmpMulticastVlanGroupVid"),
    (0, "DGS-1100-10ME_A1", "igmpMulticastVlanGroupAddressType"),
    (0, "DGS-1100-10ME_A1", "igmpMulticastVlanGroupFromIp"),
    (0, "DGS-1100-10ME_A1", "igmpMulticastVlanGroupToIp"),
)
if mibBuilder.loadTexts:
    sysIGMPMulticastVlanGroupEntry.setStatus("current")


class _IgmpMulticastVlanGroupVid_Type(Integer32):
    """Custom type igmpMulticastVlanGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpMulticastVlanGroupVid_Type.__name__ = "Integer32"
_IgmpMulticastVlanGroupVid_Object = MibTableColumn
igmpMulticastVlanGroupVid = _IgmpMulticastVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 3, 1, 1),
    _IgmpMulticastVlanGroupVid_Type()
)
igmpMulticastVlanGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupVid.setStatus("current")
_IgmpMulticastVlanGroupAddressType_Type = InetAddressType
_IgmpMulticastVlanGroupAddressType_Object = MibTableColumn
igmpMulticastVlanGroupAddressType = _IgmpMulticastVlanGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 3, 1, 2),
    _IgmpMulticastVlanGroupAddressType_Type()
)
igmpMulticastVlanGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupAddressType.setStatus("current")
_IgmpMulticastVlanGroupFromIp_Type = InetAddress
_IgmpMulticastVlanGroupFromIp_Object = MibTableColumn
igmpMulticastVlanGroupFromIp = _IgmpMulticastVlanGroupFromIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 3, 1, 3),
    _IgmpMulticastVlanGroupFromIp_Type()
)
igmpMulticastVlanGroupFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupFromIp.setStatus("current")
_IgmpMulticastVlanGroupToIp_Type = InetAddress
_IgmpMulticastVlanGroupToIp_Object = MibTableColumn
igmpMulticastVlanGroupToIp = _IgmpMulticastVlanGroupToIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 3, 1, 4),
    _IgmpMulticastVlanGroupToIp_Type()
)
igmpMulticastVlanGroupToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupToIp.setStatus("current")
_IgmpMulticastVlanGroupStatus_Type = RowStatus
_IgmpMulticastVlanGroupStatus_Object = MibTableColumn
igmpMulticastVlanGroupStatus = _IgmpMulticastVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 27, 3, 1, 5),
    _IgmpMulticastVlanGroupStatus_Type()
)
igmpMulticastVlanGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanGroupStatus.setStatus("current")
_CompanyDHCPRelay_ObjectIdentity = ObjectIdentity
companyDHCPRelay = _CompanyDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28)
)
_SysDHCPRelayControl_ObjectIdentity = ObjectIdentity
sysDHCPRelayControl = _SysDHCPRelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 1)
)


class _DhcpRelayState_Type(Integer32):
    """Custom type dhcpRelayState based on Integer32"""
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


_DhcpRelayState_Type.__name__ = "Integer32"
_DhcpRelayState_Object = MibScalar
dhcpRelayState = _DhcpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 1, 1),
    _DhcpRelayState_Type()
)
dhcpRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayState.setStatus("current")


class _DhcpRelayHopCount_Type(Integer32):
    """Custom type dhcpRelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DhcpRelayHopCount_Type.__name__ = "Integer32"
_DhcpRelayHopCount_Object = MibScalar
dhcpRelayHopCount = _DhcpRelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 1, 2),
    _DhcpRelayHopCount_Type()
)
dhcpRelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayHopCount.setStatus("current")


class _DhcpRelayTimeThreshold_Type(Integer32):
    """Custom type dhcpRelayTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpRelayTimeThreshold_Type.__name__ = "Integer32"
_DhcpRelayTimeThreshold_Object = MibScalar
dhcpRelayTimeThreshold = _DhcpRelayTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 1, 3),
    _DhcpRelayTimeThreshold_Type()
)
dhcpRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTimeThreshold.setStatus("current")
_SysDHCPRelayManagement_ObjectIdentity = ObjectIdentity
sysDHCPRelayManagement = _SysDHCPRelayManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2)
)
_DhcpRelayInterfaceSettingsTable_Object = MibTable
dhcpRelayInterfaceSettingsTable = _DhcpRelayInterfaceSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayInterfaceSettingsTable.setStatus("current")
_DhcpRelayInterfaceSettingsEntry_Object = MibTableRow
dhcpRelayInterfaceSettingsEntry = _DhcpRelayInterfaceSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 1, 1)
)
dhcpRelayInterfaceSettingsEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "dhcpRelayServerIP"),
)
if mibBuilder.loadTexts:
    dhcpRelayInterfaceSettingsEntry.setStatus("current")
_DhcpRelayServerIP_Type = IpAddress
_DhcpRelayServerIP_Object = MibTableColumn
dhcpRelayServerIP = _DhcpRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 1, 1, 1),
    _DhcpRelayServerIP_Type()
)
dhcpRelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerIP.setStatus("current")
_DhcpRelayInterface_Type = DisplayString
_DhcpRelayInterface_Object = MibTableColumn
dhcpRelayInterface = _DhcpRelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 1, 1, 2),
    _DhcpRelayInterface_Type()
)
dhcpRelayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayInterface.setStatus("current")
_DhcpRelayInterfaceSettingsRowStatus_Type = RowStatus
_DhcpRelayInterfaceSettingsRowStatus_Object = MibTableColumn
dhcpRelayInterfaceSettingsRowStatus = _DhcpRelayInterfaceSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 1, 1, 3),
    _DhcpRelayInterfaceSettingsRowStatus_Type()
)
dhcpRelayInterfaceSettingsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInterfaceSettingsRowStatus.setStatus("current")
_DhcpRelayManagermentOption82_ObjectIdentity = ObjectIdentity
dhcpRelayManagermentOption82 = _DhcpRelayManagermentOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 2)
)


class _DhcpRelayOption82State_Type(Integer32):
    """Custom type dhcpRelayOption82State based on Integer32"""
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


_DhcpRelayOption82State_Type.__name__ = "Integer32"
_DhcpRelayOption82State_Object = MibScalar
dhcpRelayOption82State = _DhcpRelayOption82State_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 2, 1),
    _DhcpRelayOption82State_Type()
)
dhcpRelayOption82State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82State.setStatus("current")


class _DhcpRelayOption82CheckState_Type(Integer32):
    """Custom type dhcpRelayOption82CheckState based on Integer32"""
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


_DhcpRelayOption82CheckState_Type.__name__ = "Integer32"
_DhcpRelayOption82CheckState_Object = MibScalar
dhcpRelayOption82CheckState = _DhcpRelayOption82CheckState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 2, 2),
    _DhcpRelayOption82CheckState_Type()
)
dhcpRelayOption82CheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82CheckState.setStatus("current")


class _DhcpRelayOption82Policy_Type(Integer32):
    """Custom type dhcpRelayOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )


_DhcpRelayOption82Policy_Type.__name__ = "Integer32"
_DhcpRelayOption82Policy_Object = MibScalar
dhcpRelayOption82Policy = _DhcpRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 2, 3),
    _DhcpRelayOption82Policy_Type()
)
dhcpRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Policy.setStatus("current")


class _DhcpRelayOption82RemoteIDType_Type(Integer32):
    """Custom type dhcpRelayOption82RemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("userdefined", 2))
    )


_DhcpRelayOption82RemoteIDType_Type.__name__ = "Integer32"
_DhcpRelayOption82RemoteIDType_Object = MibScalar
dhcpRelayOption82RemoteIDType = _DhcpRelayOption82RemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 2, 4),
    _DhcpRelayOption82RemoteIDType_Type()
)
dhcpRelayOption82RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82RemoteIDType.setStatus("current")
_DhcpRelayOption82RemoteID_Type = DisplayString
_DhcpRelayOption82RemoteID_Object = MibScalar
dhcpRelayOption82RemoteID = _DhcpRelayOption82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 28, 2, 2, 5),
    _DhcpRelayOption82RemoteID_Type()
)
dhcpRelayOption82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82RemoteID.setStatus("current")
_CompanyDHCPLocalRelay_ObjectIdentity = ObjectIdentity
companyDHCPLocalRelay = _CompanyDHCPLocalRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 29)
)


class _SysDHCPLocalRelayGlobalState_Type(Integer32):
    """Custom type sysDHCPLocalRelayGlobalState based on Integer32"""
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


_SysDHCPLocalRelayGlobalState_Type.__name__ = "Integer32"
_SysDHCPLocalRelayGlobalState_Object = MibScalar
sysDHCPLocalRelayGlobalState = _SysDHCPLocalRelayGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 29, 1),
    _SysDHCPLocalRelayGlobalState_Type()
)
sysDHCPLocalRelayGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDHCPLocalRelayGlobalState.setStatus("current")
_SysDHCPLocalRelayTable_Object = MibTable
sysDHCPLocalRelayTable = _SysDHCPLocalRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 29, 2)
)
if mibBuilder.loadTexts:
    sysDHCPLocalRelayTable.setStatus("current")
_DhcpLocalRelayEntry_Object = MibTableRow
dhcpLocalRelayEntry = _DhcpLocalRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 29, 2, 1)
)
dhcpLocalRelayEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "dhcpLocalRelayVlanId"),
)
if mibBuilder.loadTexts:
    dhcpLocalRelayEntry.setStatus("current")


class _DhcpLocalRelayVlanId_Type(Integer32):
    """Custom type dhcpLocalRelayVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpLocalRelayVlanId_Type.__name__ = "Integer32"
_DhcpLocalRelayVlanId_Object = MibTableColumn
dhcpLocalRelayVlanId = _DhcpLocalRelayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 29, 2, 1, 1),
    _DhcpLocalRelayVlanId_Type()
)
dhcpLocalRelayVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLocalRelayVlanId.setStatus("current")


class _DhcpLocalRelayState_Type(Integer32):
    """Custom type dhcpLocalRelayState based on Integer32"""
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


_DhcpLocalRelayState_Type.__name__ = "Integer32"
_DhcpLocalRelayState_Object = MibTableColumn
dhcpLocalRelayState = _DhcpLocalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 29, 2, 1, 2),
    _DhcpLocalRelayState_Type()
)
dhcpLocalRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelayState.setStatus("current")
_CompanyGreenSetting_ObjectIdentity = ObjectIdentity
companyGreenSetting = _CompanyGreenSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31)
)
_SysGreenLEDShutoff_ObjectIdentity = ObjectIdentity
sysGreenLEDShutoff = _SysGreenLEDShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 1)
)
_GreenLEDShutoffPortList_Type = PortList
_GreenLEDShutoffPortList_Object = MibScalar
greenLEDShutoffPortList = _GreenLEDShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 1, 1),
    _GreenLEDShutoffPortList_Type()
)
greenLEDShutoffPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenLEDShutoffPortList.setStatus("current")


class _GreenLEDShutoffState_Type(Integer32):
    """Custom type greenLEDShutoffState based on Integer32"""
    defaultValue = 2

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


_GreenLEDShutoffState_Type.__name__ = "Integer32"
_GreenLEDShutoffState_Object = MibScalar
greenLEDShutoffState = _GreenLEDShutoffState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 1, 2),
    _GreenLEDShutoffState_Type()
)
greenLEDShutoffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenLEDShutoffState.setStatus("current")


class _GreenLEDShutoffTimeProfile1_Type(DisplayString):
    """Custom type greenLEDShutoffTimeProfile1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GreenLEDShutoffTimeProfile1_Type.__name__ = "DisplayString"
_GreenLEDShutoffTimeProfile1_Object = MibScalar
greenLEDShutoffTimeProfile1 = _GreenLEDShutoffTimeProfile1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 1, 3),
    _GreenLEDShutoffTimeProfile1_Type()
)
greenLEDShutoffTimeProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenLEDShutoffTimeProfile1.setStatus("current")


class _GreenLEDShutoffTimeProfile2_Type(DisplayString):
    """Custom type greenLEDShutoffTimeProfile2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GreenLEDShutoffTimeProfile2_Type.__name__ = "DisplayString"
_GreenLEDShutoffTimeProfile2_Object = MibScalar
greenLEDShutoffTimeProfile2 = _GreenLEDShutoffTimeProfile2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 1, 4),
    _GreenLEDShutoffTimeProfile2_Type()
)
greenLEDShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenLEDShutoffTimeProfile2.setStatus("current")
_SysGreenPortShutoff_ObjectIdentity = ObjectIdentity
sysGreenPortShutoff = _SysGreenPortShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 2)
)
_GreenPortShutoffPortList_Type = PortList
_GreenPortShutoffPortList_Object = MibScalar
greenPortShutoffPortList = _GreenPortShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 2, 1),
    _GreenPortShutoffPortList_Type()
)
greenPortShutoffPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenPortShutoffPortList.setStatus("current")


class _GreenPortShutoffState_Type(Integer32):
    """Custom type greenPortShutoffState based on Integer32"""
    defaultValue = 2

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


_GreenPortShutoffState_Type.__name__ = "Integer32"
_GreenPortShutoffState_Object = MibScalar
greenPortShutoffState = _GreenPortShutoffState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 2, 2),
    _GreenPortShutoffState_Type()
)
greenPortShutoffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenPortShutoffState.setStatus("current")


class _GreenPortShutoffTimeProfile1_Type(DisplayString):
    """Custom type greenPortShutoffTimeProfile1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GreenPortShutoffTimeProfile1_Type.__name__ = "DisplayString"
_GreenPortShutoffTimeProfile1_Object = MibScalar
greenPortShutoffTimeProfile1 = _GreenPortShutoffTimeProfile1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 2, 3),
    _GreenPortShutoffTimeProfile1_Type()
)
greenPortShutoffTimeProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenPortShutoffTimeProfile1.setStatus("current")


class _GreenPortShutoffTimeProfile2_Type(DisplayString):
    """Custom type greenPortShutoffTimeProfile2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GreenPortShutoffTimeProfile2_Type.__name__ = "DisplayString"
_GreenPortShutoffTimeProfile2_Object = MibScalar
greenPortShutoffTimeProfile2 = _GreenPortShutoffTimeProfile2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 2, 4),
    _GreenPortShutoffTimeProfile2_Type()
)
greenPortShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenPortShutoffTimeProfile2.setStatus("current")
_SysGreenSystemHibernation_ObjectIdentity = ObjectIdentity
sysGreenSystemHibernation = _SysGreenSystemHibernation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 4)
)


class _GreenSystemHibernationState_Type(Integer32):
    """Custom type greenSystemHibernationState based on Integer32"""
    defaultValue = 2

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


_GreenSystemHibernationState_Type.__name__ = "Integer32"
_GreenSystemHibernationState_Object = MibScalar
greenSystemHibernationState = _GreenSystemHibernationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 4, 1),
    _GreenSystemHibernationState_Type()
)
greenSystemHibernationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenSystemHibernationState.setStatus("current")


class _GreenSystemHibernationTimeProfile1_Type(DisplayString):
    """Custom type greenSystemHibernationTimeProfile1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GreenSystemHibernationTimeProfile1_Type.__name__ = "DisplayString"
_GreenSystemHibernationTimeProfile1_Object = MibScalar
greenSystemHibernationTimeProfile1 = _GreenSystemHibernationTimeProfile1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 4, 2),
    _GreenSystemHibernationTimeProfile1_Type()
)
greenSystemHibernationTimeProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenSystemHibernationTimeProfile1.setStatus("current")


class _GreenSystemHibernationTimeProfile2_Type(DisplayString):
    """Custom type greenSystemHibernationTimeProfile2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_GreenSystemHibernationTimeProfile2_Type.__name__ = "DisplayString"
_GreenSystemHibernationTimeProfile2_Object = MibScalar
greenSystemHibernationTimeProfile2 = _GreenSystemHibernationTimeProfile2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 4, 3),
    _GreenSystemHibernationTimeProfile2_Type()
)
greenSystemHibernationTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenSystemHibernationTimeProfile2.setStatus("current")


class _GreenCableLenDetectionState_Type(Integer32):
    """Custom type greenCableLenDetectionState based on Integer32"""
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


_GreenCableLenDetectionState_Type.__name__ = "Integer32"
_GreenCableLenDetectionState_Object = MibScalar
greenCableLenDetectionState = _GreenCableLenDetectionState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 31, 5),
    _GreenCableLenDetectionState_Type()
)
greenCableLenDetectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    greenCableLenDetectionState.setStatus("current")
_CompanyLLDP_ObjectIdentity = ObjectIdentity
companyLLDP = _CompanyLLDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32)
)


class _SysLLDPState_Type(Integer32):
    """Custom type sysLLDPState based on Integer32"""
    defaultValue = 2

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


_SysLLDPState_Type.__name__ = "Integer32"
_SysLLDPState_Object = MibScalar
sysLLDPState = _SysLLDPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 1),
    _SysLLDPState_Type()
)
sysLLDPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLLDPState.setStatus("current")


class _SysLLDPMsgHoldMultiplier_Type(Integer32):
    """Custom type sysLLDPMsgHoldMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SysLLDPMsgHoldMultiplier_Type.__name__ = "Integer32"
_SysLLDPMsgHoldMultiplier_Object = MibScalar
sysLLDPMsgHoldMultiplier = _SysLLDPMsgHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 2),
    _SysLLDPMsgHoldMultiplier_Type()
)
sysLLDPMsgHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLLDPMsgHoldMultiplier.setStatus("current")


class _SysLLDPMsgTxInterval_Type(Integer32):
    """Custom type sysLLDPMsgTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_SysLLDPMsgTxInterval_Type.__name__ = "Integer32"
_SysLLDPMsgTxInterval_Object = MibScalar
sysLLDPMsgTxInterval = _SysLLDPMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 3),
    _SysLLDPMsgTxInterval_Type()
)
sysLLDPMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLLDPMsgTxInterval.setStatus("current")


class _SysLLDPReinitDelay_Type(Integer32):
    """Custom type sysLLDPReinitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SysLLDPReinitDelay_Type.__name__ = "Integer32"
_SysLLDPReinitDelay_Object = MibScalar
sysLLDPReinitDelay = _SysLLDPReinitDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 4),
    _SysLLDPReinitDelay_Type()
)
sysLLDPReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLLDPReinitDelay.setStatus("current")


class _SysLLDPTxDelay_Type(Integer32):
    """Custom type sysLLDPTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_SysLLDPTxDelay_Type.__name__ = "Integer32"
_SysLLDPTxDelay_Object = MibScalar
sysLLDPTxDelay = _SysLLDPTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 5),
    _SysLLDPTxDelay_Type()
)
sysLLDPTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLLDPTxDelay.setStatus("current")
_SysLLDPConfigManAddrTable_Object = MibTable
sysLLDPConfigManAddrTable = _SysLLDPConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 6)
)
if mibBuilder.loadTexts:
    sysLLDPConfigManAddrTable.setStatus("current")
_SysLLDPConfigManAddrEntry_Object = MibTableRow
sysLLDPConfigManAddrEntry = _SysLLDPConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 6, 1)
)
sysLLDPConfigManAddrEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpConfigManAddrSubtype"),
    (0, "DGS-1100-10ME_A1", "lldpConfigManAddr"),
)
if mibBuilder.loadTexts:
    sysLLDPConfigManAddrEntry.setStatus("current")
_LldpConfigManAddrSubtype_Type = AddressFamilyNumbers
_LldpConfigManAddrSubtype_Object = MibTableColumn
lldpConfigManAddrSubtype = _LldpConfigManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 6, 1, 1),
    _LldpConfigManAddrSubtype_Type()
)
lldpConfigManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpConfigManAddrSubtype.setStatus("current")
_LldpConfigManAddr_Type = InetAddress
_LldpConfigManAddr_Object = MibTableColumn
lldpConfigManAddr = _LldpConfigManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 6, 1, 2),
    _LldpConfigManAddr_Type()
)
lldpConfigManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpConfigManAddr.setStatus("current")


class _LldpConfigManAddrPortsTxEnable_Type(LldpPortList):
    """Custom type lldpConfigManAddrPortsTxEnable based on LldpPortList"""
    defaultHexValue = ""


_LldpConfigManAddrPortsTxEnable_Object = MibTableColumn
lldpConfigManAddrPortsTxEnable = _LldpConfigManAddrPortsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 6, 1, 3),
    _LldpConfigManAddrPortsTxEnable_Type()
)
lldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpConfigManAddrPortsTxEnable.setStatus("current")
_SysLLDPPortConfigTable_Object = MibTable
sysLLDPPortConfigTable = _SysLLDPPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 11)
)
if mibBuilder.loadTexts:
    sysLLDPPortConfigTable.setStatus("current")
_SysLLDPPortConfigEntry_Object = MibTableRow
sysLLDPPortConfigEntry = _SysLLDPPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 11, 1)
)
sysLLDPPortConfigEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    sysLLDPPortConfigEntry.setStatus("current")
_LldpPortConfigPortNum_Type = LldpPortNumber
_LldpPortConfigPortNum_Object = MibTableColumn
lldpPortConfigPortNum = _LldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 11, 1, 1),
    _LldpPortConfigPortNum_Type()
)
lldpPortConfigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpPortConfigPortNum.setStatus("current")


class _LldpPortConfigAdminStatus_Type(Integer32):
    """Custom type lldpPortConfigAdminStatus based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 4),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("txOnly", 1))
    )


_LldpPortConfigAdminStatus_Type.__name__ = "Integer32"
_LldpPortConfigAdminStatus_Object = MibTableColumn
lldpPortConfigAdminStatus = _LldpPortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 11, 1, 2),
    _LldpPortConfigAdminStatus_Type()
)
lldpPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigAdminStatus.setStatus("current")


class _LldpPortConfigNotificationEnable_Type(TruthValue):
    """Custom type lldpPortConfigNotificationEnable based on TruthValue"""


_LldpPortConfigNotificationEnable_Object = MibTableColumn
lldpPortConfigNotificationEnable = _LldpPortConfigNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 11, 1, 3),
    _LldpPortConfigNotificationEnable_Type()
)
lldpPortConfigNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigNotificationEnable.setStatus("current")


class _LldpPortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpPortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysCap", 3),
          ("sysDesc", 2),
          ("sysName", 1))
    )

_LldpPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpPortConfigTLVsTxEnable_Object = MibTableColumn
lldpPortConfigTLVsTxEnable = _LldpPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 11, 1, 4),
    _LldpPortConfigTLVsTxEnable_Type()
)
lldpPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigTLVsTxEnable.setStatus("current")
_SysLLDPXdot3Objects_ObjectIdentity = ObjectIdentity
sysLLDPXdot3Objects = _SysLLDPXdot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12)
)
_LldpXdot3Config_ObjectIdentity = ObjectIdentity
lldpXdot3Config = _LldpXdot3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 1)
)
_LldpXdot3PortConfigTable_Object = MibTable
lldpXdot3PortConfigTable = _LldpXdot3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTable.setStatus("current")
_LldpXdot3PortConfigEntry_Object = MibTableRow
lldpXdot3PortConfigEntry = _LldpXdot3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 1, 1, 1)
)
lldpXdot3PortConfigEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot3PortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigEntry.setStatus("current")
_LldpXdot3PortConfigPortNum_Type = LldpPortNumber
_LldpXdot3PortConfigPortNum_Object = MibTableColumn
lldpXdot3PortConfigPortNum = _LldpXdot3PortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 1, 1, 1, 1),
    _LldpXdot3PortConfigPortNum_Type()
)
lldpXdot3PortConfigPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3PortConfigPortNum.setStatus("current")


class _LldpXdot3PortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpXdot3PortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("macPhyConfigStatus", 0),
          ("maxFrameSize", 1))
    )

_LldpXdot3PortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpXdot3PortConfigTLVsTxEnable_Object = MibTableColumn
lldpXdot3PortConfigTLVsTxEnable = _LldpXdot3PortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 1, 1, 1, 2),
    _LldpXdot3PortConfigTLVsTxEnable_Type()
)
lldpXdot3PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTLVsTxEnable.setStatus("current")
_LldpXdot3LocalData_ObjectIdentity = ObjectIdentity
lldpXdot3LocalData = _LldpXdot3LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2)
)
_LldpXdot3LocPortTable_Object = MibTable
lldpXdot3LocPortTable = _LldpXdot3LocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortTable.setStatus("current")
_LldpXdot3LocPortEntry_Object = MibTableRow
lldpXdot3LocPortEntry = _LldpXdot3LocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 1, 1)
)
lldpXdot3LocPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot3LocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortEntry.setStatus("current")
_LldpXdot3LocPortNum_Type = LldpPortNumber
_LldpXdot3LocPortNum_Object = MibTableColumn
lldpXdot3LocPortNum = _LldpXdot3LocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 1, 1, 1),
    _LldpXdot3LocPortNum_Type()
)
lldpXdot3LocPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3LocPortNum.setStatus("current")
_LldpXdot3LocPortAutoNegSupported_Type = TruthValue
_LldpXdot3LocPortAutoNegSupported_Object = MibTableColumn
lldpXdot3LocPortAutoNegSupported = _LldpXdot3LocPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 1, 1, 2),
    _LldpXdot3LocPortAutoNegSupported_Type()
)
lldpXdot3LocPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegSupported.setStatus("current")
_LldpXdot3LocPortAutoNegEnabled_Type = TruthValue
_LldpXdot3LocPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3LocPortAutoNegEnabled = _LldpXdot3LocPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 1, 1, 3),
    _LldpXdot3LocPortAutoNegEnabled_Type()
)
lldpXdot3LocPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegEnabled.setStatus("current")


class _LldpXdot3LocPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpXdot3LocPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpXdot3LocPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpXdot3LocPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpXdot3LocPortAutoNegAdvertisedCap = _LldpXdot3LocPortAutoNegAdvertisedCap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 1, 1, 4),
    _LldpXdot3LocPortAutoNegAdvertisedCap_Type()
)
lldpXdot3LocPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegAdvertisedCap.setStatus("current")


class _LldpXdot3LocPortOperMauType_Type(Integer32):
    """Custom type lldpXdot3LocPortOperMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpXdot3LocPortOperMauType_Type.__name__ = "Integer32"
_LldpXdot3LocPortOperMauType_Object = MibTableColumn
lldpXdot3LocPortOperMauType = _LldpXdot3LocPortOperMauType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 1, 1, 5),
    _LldpXdot3LocPortOperMauType_Type()
)
lldpXdot3LocPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortOperMauType.setStatus("current")
_LldpXdot3LocMaxFrameSizeTable_Object = MibTable
lldpXdot3LocMaxFrameSizeTable = _LldpXdot3LocMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeTable.setStatus("current")
_LldpXdot3LocMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3LocMaxFrameSizeEntry = _LldpXdot3LocMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 4, 1)
)
lldpXdot3LocMaxFrameSizeEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot3LocMaxFrameSizePortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeEntry.setStatus("current")
_LldpXdot3LocMaxFrameSizePortNum_Type = LldpPortNumber
_LldpXdot3LocMaxFrameSizePortNum_Object = MibTableColumn
lldpXdot3LocMaxFrameSizePortNum = _LldpXdot3LocMaxFrameSizePortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 4, 1, 1),
    _LldpXdot3LocMaxFrameSizePortNum_Type()
)
lldpXdot3LocMaxFrameSizePortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizePortNum.setStatus("current")


class _LldpXdot3LocMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3LocMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3LocMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3LocMaxFrameSize_Object = MibTableColumn
lldpXdot3LocMaxFrameSize = _LldpXdot3LocMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 2, 4, 1, 2),
    _LldpXdot3LocMaxFrameSize_Type()
)
lldpXdot3LocMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSize.setStatus("current")
_LldpXdot3RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot3RemoteData = _LldpXdot3RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3)
)
_LldpXdot3RemPortTable_Object = MibTable
lldpXdot3RemPortTable = _LldpXdot3RemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortTable.setStatus("current")
_LldpXdot3RemPortEntry_Object = MibTableRow
lldpXdot3RemPortEntry = _LldpXdot3RemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1)
)
lldpXdot3RemPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortEntry.setStatus("current")
_LldpXdot3RemTimeMark_Type = TimeFilter
_LldpXdot3RemTimeMark_Object = MibTableColumn
lldpXdot3RemTimeMark = _LldpXdot3RemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1, 1),
    _LldpXdot3RemTimeMark_Type()
)
lldpXdot3RemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemTimeMark.setStatus("current")
_LldpXdot3RemLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemLocalPortNum_Object = MibTableColumn
lldpXdot3RemLocalPortNum = _LldpXdot3RemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1, 2),
    _LldpXdot3RemLocalPortNum_Type()
)
lldpXdot3RemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLocalPortNum.setStatus("current")


class _LldpXdot3RemIndex_Type(Integer32):
    """Custom type lldpXdot3RemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemIndex_Type.__name__ = "Integer32"
_LldpXdot3RemIndex_Object = MibTableColumn
lldpXdot3RemIndex = _LldpXdot3RemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1, 3),
    _LldpXdot3RemIndex_Type()
)
lldpXdot3RemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemIndex.setStatus("current")
_LldpXdot3RemPortAutoNegSupported_Type = TruthValue
_LldpXdot3RemPortAutoNegSupported_Object = MibTableColumn
lldpXdot3RemPortAutoNegSupported = _LldpXdot3RemPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1, 4),
    _LldpXdot3RemPortAutoNegSupported_Type()
)
lldpXdot3RemPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegSupported.setStatus("current")
_LldpXdot3RemPortAutoNegEnabled_Type = TruthValue
_LldpXdot3RemPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3RemPortAutoNegEnabled = _LldpXdot3RemPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1, 5),
    _LldpXdot3RemPortAutoNegEnabled_Type()
)
lldpXdot3RemPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegEnabled.setStatus("current")


class _LldpXdot3RemPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpXdot3RemPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpXdot3RemPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpXdot3RemPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpXdot3RemPortAutoNegAdvertisedCap = _LldpXdot3RemPortAutoNegAdvertisedCap_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1, 6),
    _LldpXdot3RemPortAutoNegAdvertisedCap_Type()
)
lldpXdot3RemPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegAdvertisedCap.setStatus("current")


class _LldpXdot3RemPortOperMauType_Type(Integer32):
    """Custom type lldpXdot3RemPortOperMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpXdot3RemPortOperMauType_Type.__name__ = "Integer32"
_LldpXdot3RemPortOperMauType_Object = MibTableColumn
lldpXdot3RemPortOperMauType = _LldpXdot3RemPortOperMauType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 1, 1, 7),
    _LldpXdot3RemPortOperMauType_Type()
)
lldpXdot3RemPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortOperMauType.setStatus("current")
_LldpXdot3RemPowerTable_Object = MibTable
lldpXdot3RemPowerTable = _LldpXdot3RemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerTable.setStatus("current")
_LldpXdot3RemPowerEntry_Object = MibTableRow
lldpXdot3RemPowerEntry = _LldpXdot3RemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1)
)
lldpXdot3RemPowerEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemPowerTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemPowerLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemPowerIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerEntry.setStatus("current")
_LldpXdot3RemPowerTimeMark_Type = TimeFilter
_LldpXdot3RemPowerTimeMark_Object = MibTableColumn
lldpXdot3RemPowerTimeMark = _LldpXdot3RemPowerTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 1),
    _LldpXdot3RemPowerTimeMark_Type()
)
lldpXdot3RemPowerTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerTimeMark.setStatus("current")
_LldpXdot3RemPowerLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemPowerLocalPortNum_Object = MibTableColumn
lldpXdot3RemPowerLocalPortNum = _LldpXdot3RemPowerLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 2),
    _LldpXdot3RemPowerLocalPortNum_Type()
)
lldpXdot3RemPowerLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerLocalPortNum.setStatus("current")


class _LldpXdot3RemPowerIndex_Type(Integer32):
    """Custom type lldpXdot3RemPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemPowerIndex_Type.__name__ = "Integer32"
_LldpXdot3RemPowerIndex_Object = MibTableColumn
lldpXdot3RemPowerIndex = _LldpXdot3RemPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 3),
    _LldpXdot3RemPowerIndex_Type()
)
lldpXdot3RemPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerIndex.setStatus("current")
_LldpXdot3RemPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3RemPowerPortClass_Object = MibTableColumn
lldpXdot3RemPowerPortClass = _LldpXdot3RemPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 4),
    _LldpXdot3RemPowerPortClass_Type()
)
lldpXdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPortClass.setStatus("current")
_LldpXdot3RemPowerMDISupported_Type = TruthValue
_LldpXdot3RemPowerMDISupported_Object = MibTableColumn
lldpXdot3RemPowerMDISupported = _LldpXdot3RemPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 5),
    _LldpXdot3RemPowerMDISupported_Type()
)
lldpXdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDISupported.setStatus("current")
_LldpXdot3RemPowerMDIEnabled_Type = TruthValue
_LldpXdot3RemPowerMDIEnabled_Object = MibTableColumn
lldpXdot3RemPowerMDIEnabled = _LldpXdot3RemPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 6),
    _LldpXdot3RemPowerMDIEnabled_Type()
)
lldpXdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDIEnabled.setStatus("current")
_LldpXdot3RemPowerPairControlable_Type = TruthValue
_LldpXdot3RemPowerPairControlable_Object = MibTableColumn
lldpXdot3RemPowerPairControlable = _LldpXdot3RemPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 7),
    _LldpXdot3RemPowerPairControlable_Type()
)
lldpXdot3RemPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPairControlable.setStatus("current")


class _LldpXdot3RemPowerPairs_Type(Integer32):
    """Custom type lldpXdot3RemPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpXdot3RemPowerPairs_Type.__name__ = "Integer32"
_LldpXdot3RemPowerPairs_Object = MibTableColumn
lldpXdot3RemPowerPairs = _LldpXdot3RemPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 8),
    _LldpXdot3RemPowerPairs_Type()
)
lldpXdot3RemPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPairs.setStatus("current")


class _LldpXdot3RemPowerClass_Type(Integer32):
    """Custom type lldpXdot3RemPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpXdot3RemPowerClass_Type.__name__ = "Integer32"
_LldpXdot3RemPowerClass_Object = MibTableColumn
lldpXdot3RemPowerClass = _LldpXdot3RemPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 2, 1, 9),
    _LldpXdot3RemPowerClass_Type()
)
lldpXdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerClass.setStatus("current")
_LldpXdot3RemLinkAggTable_Object = MibTable
lldpXdot3RemLinkAggTable = _LldpXdot3RemLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggTable.setStatus("current")
_LldpXdot3RemLinkAggEntry_Object = MibTableRow
lldpXdot3RemLinkAggEntry = _LldpXdot3RemLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 3, 1)
)
lldpXdot3RemLinkAggEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemLinkAggTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemLinkAggLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemLinkAggIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggEntry.setStatus("current")
_LldpXdot3RemLinkAggTimeMark_Type = TimeFilter
_LldpXdot3RemLinkAggTimeMark_Object = MibTableColumn
lldpXdot3RemLinkAggTimeMark = _LldpXdot3RemLinkAggTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 3, 1, 1),
    _LldpXdot3RemLinkAggTimeMark_Type()
)
lldpXdot3RemLinkAggTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggTimeMark.setStatus("current")
_LldpXdot3RemLinkAggLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemLinkAggLocalPortNum_Object = MibTableColumn
lldpXdot3RemLinkAggLocalPortNum = _LldpXdot3RemLinkAggLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 3, 1, 2),
    _LldpXdot3RemLinkAggLocalPortNum_Type()
)
lldpXdot3RemLinkAggLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggLocalPortNum.setStatus("current")


class _LldpXdot3RemLinkAggIndex_Type(Integer32):
    """Custom type lldpXdot3RemLinkAggIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemLinkAggIndex_Type.__name__ = "Integer32"
_LldpXdot3RemLinkAggIndex_Object = MibTableColumn
lldpXdot3RemLinkAggIndex = _LldpXdot3RemLinkAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 3, 1, 3),
    _LldpXdot3RemLinkAggIndex_Type()
)
lldpXdot3RemLinkAggIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggIndex.setStatus("current")
_LldpXdot3RemLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3RemLinkAggStatus_Object = MibTableColumn
lldpXdot3RemLinkAggStatus = _LldpXdot3RemLinkAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 3, 1, 4),
    _LldpXdot3RemLinkAggStatus_Type()
)
lldpXdot3RemLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggStatus.setStatus("current")


class _LldpXdot3RemLinkAggPortId_Type(Integer32):
    """Custom type lldpXdot3RemLinkAggPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemLinkAggPortId_Type.__name__ = "Integer32"
_LldpXdot3RemLinkAggPortId_Object = MibTableColumn
lldpXdot3RemLinkAggPortId = _LldpXdot3RemLinkAggPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 3, 1, 5),
    _LldpXdot3RemLinkAggPortId_Type()
)
lldpXdot3RemLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggPortId.setStatus("current")
_LldpXdot3RemMaxFrameSizeTable_Object = MibTable
lldpXdot3RemMaxFrameSizeTable = _LldpXdot3RemMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeTable.setStatus("current")
_LldpXdot3RemMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3RemMaxFrameSizeEntry = _LldpXdot3RemMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 4, 1)
)
lldpXdot3RemMaxFrameSizeEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemMaxFrameSizeTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemMaxFrameSizeLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot3RemMaxFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeEntry.setStatus("current")
_LldpXdot3RemMaxFrameSizeTimeMark_Type = TimeFilter
_LldpXdot3RemMaxFrameSizeTimeMark_Object = MibTableColumn
lldpXdot3RemMaxFrameSizeTimeMark = _LldpXdot3RemMaxFrameSizeTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 4, 1, 1),
    _LldpXdot3RemMaxFrameSizeTimeMark_Type()
)
lldpXdot3RemMaxFrameSizeTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeTimeMark.setStatus("current")
_LldpXdot3RemMaxFrameSizeLocalPortNum_Type = LldpPortNumber
_LldpXdot3RemMaxFrameSizeLocalPortNum_Object = MibTableColumn
lldpXdot3RemMaxFrameSizeLocalPortNum = _LldpXdot3RemMaxFrameSizeLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 4, 1, 2),
    _LldpXdot3RemMaxFrameSizeLocalPortNum_Type()
)
lldpXdot3RemMaxFrameSizeLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeLocalPortNum.setStatus("current")


class _LldpXdot3RemMaxFrameSizeIndex_Type(Integer32):
    """Custom type lldpXdot3RemMaxFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3RemMaxFrameSizeIndex_Type.__name__ = "Integer32"
_LldpXdot3RemMaxFrameSizeIndex_Object = MibTableColumn
lldpXdot3RemMaxFrameSizeIndex = _LldpXdot3RemMaxFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 4, 1, 3),
    _LldpXdot3RemMaxFrameSizeIndex_Type()
)
lldpXdot3RemMaxFrameSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeIndex.setStatus("current")


class _LldpXdot3RemMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3RemMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3RemMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3RemMaxFrameSize_Object = MibTableColumn
lldpXdot3RemMaxFrameSize = _LldpXdot3RemMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 12, 3, 4, 1, 4),
    _LldpXdot3RemMaxFrameSize_Type()
)
lldpXdot3RemMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSize.setStatus("current")
_SysLLDPXdot1Objects_ObjectIdentity = ObjectIdentity
sysLLDPXdot1Objects = _SysLLDPXdot1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13)
)
_LldpXdot1Config_ObjectIdentity = ObjectIdentity
lldpXdot1Config = _LldpXdot1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1)
)
_LldpXdot1ConfigPortVlanTable_Object = MibTable
lldpXdot1ConfigPortVlanTable = _LldpXdot1ConfigPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTable.setStatus("current")
_LldpXdot1ConfigPortVlanEntry_Object = MibTableRow
lldpXdot1ConfigPortVlanEntry = _LldpXdot1ConfigPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 1, 1)
)
lldpXdot1ConfigPortVlanEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1ConfigVlanPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanEntry.setStatus("current")
_LldpXdot1ConfigVlanPortNum_Type = LldpPortNumber
_LldpXdot1ConfigVlanPortNum_Object = MibTableColumn
lldpXdot1ConfigVlanPortNum = _LldpXdot1ConfigVlanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 1, 1, 1),
    _LldpXdot1ConfigVlanPortNum_Type()
)
lldpXdot1ConfigVlanPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanPortNum.setStatus("current")


class _LldpXdot1ConfigPortVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigPortVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigPortVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigPortVlanTxEnable = _LldpXdot1ConfigPortVlanTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 1, 1, 2),
    _LldpXdot1ConfigPortVlanTxEnable_Type()
)
lldpXdot1ConfigPortVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTxEnable.setStatus("current")
_LldpXdot1ConfigVlanNameTable_Object = MibTable
lldpXdot1ConfigVlanNameTable = _LldpXdot1ConfigVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTable.setStatus("current")
_LldpXdot1ConfigVlanNameEntry_Object = MibTableRow
lldpXdot1ConfigVlanNameEntry = _LldpXdot1ConfigVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 2, 1)
)
lldpXdot1ConfigVlanNameEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1LocConfigVlanNamePortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1ConfigVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameEntry.setStatus("current")
_LldpXdot1LocConfigVlanNamePortNum_Type = LldpPortNumber
_LldpXdot1LocConfigVlanNamePortNum_Object = MibTableColumn
lldpXdot1LocConfigVlanNamePortNum = _LldpXdot1LocConfigVlanNamePortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 2, 1, 1),
    _LldpXdot1LocConfigVlanNamePortNum_Type()
)
lldpXdot1LocConfigVlanNamePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocConfigVlanNamePortNum.setStatus("current")
_LldpXdot1ConfigVlanId_Type = VlanId
_LldpXdot1ConfigVlanId_Object = MibTableColumn
lldpXdot1ConfigVlanId = _LldpXdot1ConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 2, 1, 2),
    _LldpXdot1ConfigVlanId_Type()
)
lldpXdot1ConfigVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanId.setStatus("current")


class _LldpXdot1ConfigVlanNameTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigVlanNameTxEnable based on TruthValue"""


_LldpXdot1ConfigVlanNameTxEnable_Object = MibTableColumn
lldpXdot1ConfigVlanNameTxEnable = _LldpXdot1ConfigVlanNameTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 2, 1, 3),
    _LldpXdot1ConfigVlanNameTxEnable_Type()
)
lldpXdot1ConfigVlanNameTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTxEnable.setStatus("current")
_LldpXdot1ConfigProtocolTable_Object = MibTable
lldpXdot1ConfigProtocolTable = _LldpXdot1ConfigProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTable.setStatus("current")
_LldpXdot1ConfigProtocolEntry_Object = MibTableRow
lldpXdot1ConfigProtocolEntry = _LldpXdot1ConfigProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 4, 1)
)
lldpXdot1ConfigProtocolEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1ConfigProtocolPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1ConfigProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolEntry.setStatus("current")
_LldpXdot1ConfigProtocolPortNum_Type = LldpPortNumber
_LldpXdot1ConfigProtocolPortNum_Object = MibTableColumn
lldpXdot1ConfigProtocolPortNum = _LldpXdot1ConfigProtocolPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 4, 1, 1),
    _LldpXdot1ConfigProtocolPortNum_Type()
)
lldpXdot1ConfigProtocolPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolPortNum.setStatus("current")


class _LldpXdot1ConfigProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1ConfigProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1ConfigProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1ConfigProtocolIndex_Object = MibTableColumn
lldpXdot1ConfigProtocolIndex = _LldpXdot1ConfigProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 4, 1, 2),
    _LldpXdot1ConfigProtocolIndex_Type()
)
lldpXdot1ConfigProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolIndex.setStatus("current")


class _LldpXdot1ConfigProtocolTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtocolTxEnable based on TruthValue"""


_LldpXdot1ConfigProtocolTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtocolTxEnable = _LldpXdot1ConfigProtocolTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 1, 4, 1, 3),
    _LldpXdot1ConfigProtocolTxEnable_Type()
)
lldpXdot1ConfigProtocolTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTxEnable.setStatus("current")
_LldpXdot1LocalData_ObjectIdentity = ObjectIdentity
lldpXdot1LocalData = _LldpXdot1LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2)
)
_LldpXdot1LocTable_Object = MibTable
lldpXdot1LocTable = _LldpXdot1LocTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1LocTable.setStatus("current")
_LldpXdot1LocEntry_Object = MibTableRow
lldpXdot1LocEntry = _LldpXdot1LocEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 1, 1)
)
lldpXdot1LocEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1LocPortNum"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocEntry.setStatus("current")
_LldpXdot1LocPortNum_Type = LldpPortNumber
_LldpXdot1LocPortNum_Object = MibTableColumn
lldpXdot1LocPortNum = _LldpXdot1LocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 1, 1, 1),
    _LldpXdot1LocPortNum_Type()
)
lldpXdot1LocPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocPortNum.setStatus("current")


class _LldpXdot1LocPortVlanId_Type(Integer32):
    """Custom type lldpXdot1LocPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1LocPortVlanId_Type.__name__ = "Integer32"
_LldpXdot1LocPortVlanId_Object = MibTableColumn
lldpXdot1LocPortVlanId = _LldpXdot1LocPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 1, 1, 2),
    _LldpXdot1LocPortVlanId_Type()
)
lldpXdot1LocPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocPortVlanId.setStatus("current")
_LldpXdot1LocVlanNameTable_Object = MibTable
lldpXdot1LocVlanNameTable = _LldpXdot1LocVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameTable.setStatus("current")
_LldpXdot1LocVlanNameEntry_Object = MibTableRow
lldpXdot1LocVlanNameEntry = _LldpXdot1LocVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 3, 1)
)
lldpXdot1LocVlanNameEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1LocVlanNamePortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1LocVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameEntry.setStatus("current")
_LldpXdot1LocVlanNamePortNum_Type = LldpPortNumber
_LldpXdot1LocVlanNamePortNum_Object = MibTableColumn
lldpXdot1LocVlanNamePortNum = _LldpXdot1LocVlanNamePortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 3, 1, 1),
    _LldpXdot1LocVlanNamePortNum_Type()
)
lldpXdot1LocVlanNamePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNamePortNum.setStatus("current")
_LldpXdot1LocVlanId_Type = VlanId
_LldpXdot1LocVlanId_Object = MibTableColumn
lldpXdot1LocVlanId = _LldpXdot1LocVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 3, 1, 2),
    _LldpXdot1LocVlanId_Type()
)
lldpXdot1LocVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanId.setStatus("current")


class _LldpXdot1LocVlanName_Type(SnmpAdminString):
    """Custom type lldpXdot1LocVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpXdot1LocVlanName_Type.__name__ = "SnmpAdminString"
_LldpXdot1LocVlanName_Object = MibTableColumn
lldpXdot1LocVlanName = _LldpXdot1LocVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 3, 1, 3),
    _LldpXdot1LocVlanName_Type()
)
lldpXdot1LocVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanName.setStatus("current")
_LldpXdot1LocProtocolTable_Object = MibTable
lldpXdot1LocProtocolTable = _LldpXdot1LocProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolTable.setStatus("current")
_LldpXdot1LocProtocolEntry_Object = MibTableRow
lldpXdot1LocProtocolEntry = _LldpXdot1LocProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 4, 1)
)
lldpXdot1LocProtocolEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1LocProtocolPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1LocProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolEntry.setStatus("current")
_LldpXdot1LocProtocolPortNum_Type = LldpPortNumber
_LldpXdot1LocProtocolPortNum_Object = MibTableColumn
lldpXdot1LocProtocolPortNum = _LldpXdot1LocProtocolPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 4, 1, 1),
    _LldpXdot1LocProtocolPortNum_Type()
)
lldpXdot1LocProtocolPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolPortNum.setStatus("current")


class _LldpXdot1LocProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1LocProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1LocProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1LocProtocolIndex_Object = MibTableColumn
lldpXdot1LocProtocolIndex = _LldpXdot1LocProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 4, 1, 2),
    _LldpXdot1LocProtocolIndex_Type()
)
lldpXdot1LocProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolIndex.setStatus("current")


class _LldpXdot1LocProtocolId_Type(OctetString):
    """Custom type lldpXdot1LocProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpXdot1LocProtocolId_Type.__name__ = "OctetString"
_LldpXdot1LocProtocolId_Object = MibTableColumn
lldpXdot1LocProtocolId = _LldpXdot1LocProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 2, 4, 1, 3),
    _LldpXdot1LocProtocolId_Type()
)
lldpXdot1LocProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolId.setStatus("current")
_LldpXdot1RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1RemoteData = _LldpXdot1RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3)
)
_LldpXdot1RemTable_Object = MibTable
lldpXdot1RemTable = _LldpXdot1RemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1RemTable.setStatus("current")
_LldpXdot1RemEntry_Object = MibTableRow
lldpXdot1RemEntry = _LldpXdot1RemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 1, 1)
)
lldpXdot1RemEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemEntry.setStatus("current")
_LldpXdot1RemTimeMark_Type = TimeFilter
_LldpXdot1RemTimeMark_Object = MibTableColumn
lldpXdot1RemTimeMark = _LldpXdot1RemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 1, 1, 1),
    _LldpXdot1RemTimeMark_Type()
)
lldpXdot1RemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemTimeMark.setStatus("current")
_LldpXdot1RemLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemLocalPortNum_Object = MibTableColumn
lldpXdot1RemLocalPortNum = _LldpXdot1RemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 1, 1, 2),
    _LldpXdot1RemLocalPortNum_Type()
)
lldpXdot1RemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemLocalPortNum.setStatus("current")


class _LldpXdot1RemIndex_Type(Integer32):
    """Custom type lldpXdot1RemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemIndex_Type.__name__ = "Integer32"
_LldpXdot1RemIndex_Object = MibTableColumn
lldpXdot1RemIndex = _LldpXdot1RemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 1, 1, 3),
    _LldpXdot1RemIndex_Type()
)
lldpXdot1RemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemIndex.setStatus("current")


class _LldpXdot1RemPortVlanId_Type(Integer32):
    """Custom type lldpXdot1RemPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1RemPortVlanId_Type.__name__ = "Integer32"
_LldpXdot1RemPortVlanId_Object = MibTableColumn
lldpXdot1RemPortVlanId = _LldpXdot1RemPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 1, 1, 4),
    _LldpXdot1RemPortVlanId_Type()
)
lldpXdot1RemPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemPortVlanId.setStatus("current")
_LldpXdot1RemProtoVlanTable_Object = MibTable
lldpXdot1RemProtoVlanTable = _LldpXdot1RemProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanTable.setStatus("current")
_LldpXdot1RemProtoVlanEntry_Object = MibTableRow
lldpXdot1RemProtoVlanEntry = _LldpXdot1RemProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2, 1)
)
lldpXdot1RemProtoVlanEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtoVlanTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtoVlanLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtoVlanIndex"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEntry.setStatus("current")
_LldpXdot1RemProtoVlanTimeMark_Type = TimeFilter
_LldpXdot1RemProtoVlanTimeMark_Object = MibTableColumn
lldpXdot1RemProtoVlanTimeMark = _LldpXdot1RemProtoVlanTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2, 1, 1),
    _LldpXdot1RemProtoVlanTimeMark_Type()
)
lldpXdot1RemProtoVlanTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanTimeMark.setStatus("current")
_LldpXdot1RemProtoVlanLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemProtoVlanLocalPortNum_Object = MibTableColumn
lldpXdot1RemProtoVlanLocalPortNum = _LldpXdot1RemProtoVlanLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2, 1, 2),
    _LldpXdot1RemProtoVlanLocalPortNum_Type()
)
lldpXdot1RemProtoVlanLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanLocalPortNum.setStatus("current")


class _LldpXdot1RemProtoVlanIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtoVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtoVlanIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtoVlanIndex_Object = MibTableColumn
lldpXdot1RemProtoVlanIndex = _LldpXdot1RemProtoVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2, 1, 3),
    _LldpXdot1RemProtoVlanIndex_Type()
)
lldpXdot1RemProtoVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanIndex.setStatus("current")


class _LldpXdot1RemProtoVlanId_Type(Integer32):
    """Custom type lldpXdot1RemProtoVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1RemProtoVlanId_Type.__name__ = "Integer32"
_LldpXdot1RemProtoVlanId_Object = MibTableColumn
lldpXdot1RemProtoVlanId = _LldpXdot1RemProtoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2, 1, 4),
    _LldpXdot1RemProtoVlanId_Type()
)
lldpXdot1RemProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanId.setStatus("current")
_LldpXdot1RemProtoVlanSupported_Type = TruthValue
_LldpXdot1RemProtoVlanSupported_Object = MibTableColumn
lldpXdot1RemProtoVlanSupported = _LldpXdot1RemProtoVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2, 1, 5),
    _LldpXdot1RemProtoVlanSupported_Type()
)
lldpXdot1RemProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanSupported.setStatus("current")
_LldpXdot1RemProtoVlanEnabled_Type = TruthValue
_LldpXdot1RemProtoVlanEnabled_Object = MibTableColumn
lldpXdot1RemProtoVlanEnabled = _LldpXdot1RemProtoVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 2, 1, 6),
    _LldpXdot1RemProtoVlanEnabled_Type()
)
lldpXdot1RemProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEnabled.setStatus("current")
_LldpXdot1RemVlanNameTable_Object = MibTable
lldpXdot1RemVlanNameTable = _LldpXdot1RemVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameTable.setStatus("current")
_LldpXdot1RemVlanNameEntry_Object = MibTableRow
lldpXdot1RemVlanNameEntry = _LldpXdot1RemVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 3, 1)
)
lldpXdot1RemVlanNameEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemVlanNameTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemVlanNameLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemVlanNameIndex"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameEntry.setStatus("current")
_LldpXdot1RemVlanNameTimeMark_Type = TimeFilter
_LldpXdot1RemVlanNameTimeMark_Object = MibTableColumn
lldpXdot1RemVlanNameTimeMark = _LldpXdot1RemVlanNameTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 3, 1, 1),
    _LldpXdot1RemVlanNameTimeMark_Type()
)
lldpXdot1RemVlanNameTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameTimeMark.setStatus("current")
_LldpXdot1RemVlanNameLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemVlanNameLocalPortNum_Object = MibTableColumn
lldpXdot1RemVlanNameLocalPortNum = _LldpXdot1RemVlanNameLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 3, 1, 2),
    _LldpXdot1RemVlanNameLocalPortNum_Type()
)
lldpXdot1RemVlanNameLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameLocalPortNum.setStatus("current")


class _LldpXdot1RemVlanNameIndex_Type(Integer32):
    """Custom type lldpXdot1RemVlanNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemVlanNameIndex_Type.__name__ = "Integer32"
_LldpXdot1RemVlanNameIndex_Object = MibTableColumn
lldpXdot1RemVlanNameIndex = _LldpXdot1RemVlanNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 3, 1, 3),
    _LldpXdot1RemVlanNameIndex_Type()
)
lldpXdot1RemVlanNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameIndex.setStatus("current")
_LldpXdot1RemVlanId_Type = VlanId
_LldpXdot1RemVlanId_Object = MibTableColumn
lldpXdot1RemVlanId = _LldpXdot1RemVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 3, 1, 4),
    _LldpXdot1RemVlanId_Type()
)
lldpXdot1RemVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanId.setStatus("current")


class _LldpXdot1RemVlanName_Type(SnmpAdminString):
    """Custom type lldpXdot1RemVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LldpXdot1RemVlanName_Type.__name__ = "SnmpAdminString"
_LldpXdot1RemVlanName_Object = MibTableColumn
lldpXdot1RemVlanName = _LldpXdot1RemVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 3, 1, 5),
    _LldpXdot1RemVlanName_Type()
)
lldpXdot1RemVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanName.setStatus("current")
_LldpXdot1RemProtocolTable_Object = MibTable
lldpXdot1RemProtocolTable = _LldpXdot1RemProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolTable.setStatus("current")
_LldpXdot1RemProtocolEntry_Object = MibTableRow
lldpXdot1RemProtocolEntry = _LldpXdot1RemProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 4, 1)
)
lldpXdot1RemProtocolEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtocolTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtocolLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtocolIndex"),
    (0, "DGS-1100-10ME_A1", "lldpXdot1RemProtocolIdIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolEntry.setStatus("current")
_LldpXdot1RemProtocolTimeMark_Type = TimeFilter
_LldpXdot1RemProtocolTimeMark_Object = MibTableColumn
lldpXdot1RemProtocolTimeMark = _LldpXdot1RemProtocolTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 4, 1, 1),
    _LldpXdot1RemProtocolTimeMark_Type()
)
lldpXdot1RemProtocolTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolTimeMark.setStatus("current")
_LldpXdot1RemProtocolLocalPortNum_Type = LldpPortNumber
_LldpXdot1RemProtocolLocalPortNum_Object = MibTableColumn
lldpXdot1RemProtocolLocalPortNum = _LldpXdot1RemProtocolLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 4, 1, 2),
    _LldpXdot1RemProtocolLocalPortNum_Type()
)
lldpXdot1RemProtocolLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolLocalPortNum.setStatus("current")


class _LldpXdot1RemProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtocolIndex_Object = MibTableColumn
lldpXdot1RemProtocolIndex = _LldpXdot1RemProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 4, 1, 3),
    _LldpXdot1RemProtocolIndex_Type()
)
lldpXdot1RemProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolIndex.setStatus("current")


class _LldpXdot1RemProtocolIdIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtocolIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtocolIdIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtocolIdIndex_Object = MibTableColumn
lldpXdot1RemProtocolIdIndex = _LldpXdot1RemProtocolIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 4, 1, 4),
    _LldpXdot1RemProtocolIdIndex_Type()
)
lldpXdot1RemProtocolIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolIdIndex.setStatus("current")


class _LldpXdot1RemProtocolId_Type(OctetString):
    """Custom type lldpXdot1RemProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpXdot1RemProtocolId_Type.__name__ = "OctetString"
_LldpXdot1RemProtocolId_Object = MibTableColumn
lldpXdot1RemProtocolId = _LldpXdot1RemProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 13, 3, 4, 1, 5),
    _LldpXdot1RemProtocolId_Type()
)
lldpXdot1RemProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolId.setStatus("current")
_SysLLDPStatistics_ObjectIdentity = ObjectIdentity
sysLLDPStatistics = _SysLLDPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14)
)
_LldpStatsRemTablesLastChangeTime_Type = TimeStamp
_LldpStatsRemTablesLastChangeTime_Object = MibScalar
lldpStatsRemTablesLastChangeTime = _LldpStatsRemTablesLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 1),
    _LldpStatsRemTablesLastChangeTime_Type()
)
lldpStatsRemTablesLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesLastChangeTime.setStatus("current")
_LldpStatsRemTablesInserts_Type = ZeroBasedCounter32
_LldpStatsRemTablesInserts_Object = MibScalar
lldpStatsRemTablesInserts = _LldpStatsRemTablesInserts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 2),
    _LldpStatsRemTablesInserts_Type()
)
lldpStatsRemTablesInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesInserts.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesInserts.setUnits("table entries")
_LldpStatsRemTablesDeletes_Type = ZeroBasedCounter32
_LldpStatsRemTablesDeletes_Object = MibScalar
lldpStatsRemTablesDeletes = _LldpStatsRemTablesDeletes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 3),
    _LldpStatsRemTablesDeletes_Type()
)
lldpStatsRemTablesDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDeletes.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDeletes.setUnits("table entries")
_LldpStatsRemTablesDrops_Type = ZeroBasedCounter32
_LldpStatsRemTablesDrops_Object = MibScalar
lldpStatsRemTablesDrops = _LldpStatsRemTablesDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 4),
    _LldpStatsRemTablesDrops_Type()
)
lldpStatsRemTablesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDrops.setStatus("current")
if mibBuilder.loadTexts:
    lldpStatsRemTablesDrops.setUnits("table entries")
_LldpStatsRemTablesAgeouts_Type = ZeroBasedCounter32
_LldpStatsRemTablesAgeouts_Object = MibScalar
lldpStatsRemTablesAgeouts = _LldpStatsRemTablesAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 5),
    _LldpStatsRemTablesAgeouts_Type()
)
lldpStatsRemTablesAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRemTablesAgeouts.setStatus("current")
_LldpStatsTxPortTable_Object = MibTable
lldpStatsTxPortTable = _LldpStatsTxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 6)
)
if mibBuilder.loadTexts:
    lldpStatsTxPortTable.setStatus("current")
_LldpStatsTxPortEntry_Object = MibTableRow
lldpStatsTxPortEntry = _LldpStatsTxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 6, 1)
)
lldpStatsTxPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpStatsTxPortNum"),
)
if mibBuilder.loadTexts:
    lldpStatsTxPortEntry.setStatus("current")
_LldpStatsTxPortNum_Type = LldpPortNumber
_LldpStatsTxPortNum_Object = MibTableColumn
lldpStatsTxPortNum = _LldpStatsTxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 6, 1, 1),
    _LldpStatsTxPortNum_Type()
)
lldpStatsTxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsTxPortNum.setStatus("current")
_LldpStatsTxPortFramesTotal_Type = Counter32
_LldpStatsTxPortFramesTotal_Object = MibTableColumn
lldpStatsTxPortFramesTotal = _LldpStatsTxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 6, 1, 2),
    _LldpStatsTxPortFramesTotal_Type()
)
lldpStatsTxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsTxPortFramesTotal.setStatus("current")
_LldpRxStatsPortTable_Object = MibTable
lldpRxStatsPortTable = _LldpRxStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7)
)
if mibBuilder.loadTexts:
    lldpRxStatsPortTable.setStatus("current")
_LldpRxStatsPortEntry_Object = MibTableRow
lldpRxStatsPortEntry = _LldpRxStatsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1)
)
lldpRxStatsPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpStatsRxPortNum"),
)
if mibBuilder.loadTexts:
    lldpRxStatsPortEntry.setStatus("current")
_LldpStatsRxPortNum_Type = LldpPortNumber
_LldpStatsRxPortNum_Object = MibTableColumn
lldpStatsRxPortNum = _LldpStatsRxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1, 1),
    _LldpStatsRxPortNum_Type()
)
lldpStatsRxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortNum.setStatus("current")
_LldpStatsRxPortFramesDiscardedTotal_Type = Counter32
_LldpStatsRxPortFramesDiscardedTotal_Object = MibTableColumn
lldpStatsRxPortFramesDiscardedTotal = _LldpStatsRxPortFramesDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1, 2),
    _LldpStatsRxPortFramesDiscardedTotal_Type()
)
lldpStatsRxPortFramesDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesDiscardedTotal.setStatus("current")
_LldpStatsRxPortFramesErrors_Type = Counter32
_LldpStatsRxPortFramesErrors_Object = MibTableColumn
lldpStatsRxPortFramesErrors = _LldpStatsRxPortFramesErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1, 3),
    _LldpStatsRxPortFramesErrors_Type()
)
lldpStatsRxPortFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesErrors.setStatus("current")
_LldpStatsRxPortFramesTotal_Type = Counter32
_LldpStatsRxPortFramesTotal_Object = MibTableColumn
lldpStatsRxPortFramesTotal = _LldpStatsRxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1, 4),
    _LldpStatsRxPortFramesTotal_Type()
)
lldpStatsRxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortFramesTotal.setStatus("current")
_LldpStatsRxPortTLVsDiscardedTotal_Type = Counter32
_LldpStatsRxPortTLVsDiscardedTotal_Object = MibTableColumn
lldpStatsRxPortTLVsDiscardedTotal = _LldpStatsRxPortTLVsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1, 5),
    _LldpStatsRxPortTLVsDiscardedTotal_Type()
)
lldpStatsRxPortTLVsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortTLVsDiscardedTotal.setStatus("current")
_LldpStatsRxPortTLVsUnrecognizedTotal_Type = Counter32
_LldpStatsRxPortTLVsUnrecognizedTotal_Object = MibTableColumn
lldpStatsRxPortTLVsUnrecognizedTotal = _LldpStatsRxPortTLVsUnrecognizedTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1, 6),
    _LldpStatsRxPortTLVsUnrecognizedTotal_Type()
)
lldpStatsRxPortTLVsUnrecognizedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortTLVsUnrecognizedTotal.setStatus("current")
_LldpStatsRxPortAgeoutsTotal_Type = ZeroBasedCounter32
_LldpStatsRxPortAgeoutsTotal_Object = MibTableColumn
lldpStatsRxPortAgeoutsTotal = _LldpStatsRxPortAgeoutsTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 14, 7, 1, 7),
    _LldpStatsRxPortAgeoutsTotal_Type()
)
lldpStatsRxPortAgeoutsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpStatsRxPortAgeoutsTotal.setStatus("current")
_SysLLDPLocalSystemData_ObjectIdentity = ObjectIdentity
sysLLDPLocalSystemData = _SysLLDPLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15)
)
_LldpLocChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpLocChassisIdSubtype_Object = MibScalar
lldpLocChassisIdSubtype = _LldpLocChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 1),
    _LldpLocChassisIdSubtype_Type()
)
lldpLocChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocChassisIdSubtype.setStatus("current")
_LldpLocChassisId_Type = LldpChassisId
_LldpLocChassisId_Object = MibScalar
lldpLocChassisId = _LldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 2),
    _LldpLocChassisId_Type()
)
lldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocChassisId.setStatus("current")


class _LldpLocSysName_Type(SnmpAdminString):
    """Custom type lldpLocSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocSysName_Type.__name__ = "SnmpAdminString"
_LldpLocSysName_Object = MibScalar
lldpLocSysName = _LldpLocSysName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 3),
    _LldpLocSysName_Type()
)
lldpLocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysName.setStatus("current")


class _LldpLocSysDesc_Type(SnmpAdminString):
    """Custom type lldpLocSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocSysDesc_Type.__name__ = "SnmpAdminString"
_LldpLocSysDesc_Object = MibScalar
lldpLocSysDesc = _LldpLocSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 4),
    _LldpLocSysDesc_Type()
)
lldpLocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysDesc.setStatus("current")
_LldpLocSysCapEnabled_Type = LldpSystemCapabilitiesMap
_LldpLocSysCapEnabled_Object = MibScalar
lldpLocSysCapEnabled = _LldpLocSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 5),
    _LldpLocSysCapEnabled_Type()
)
lldpLocSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocSysCapEnabled.setStatus("current")
_LldpLocPortTable_Object = MibTable
lldpLocPortTable = _LldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 7)
)
if mibBuilder.loadTexts:
    lldpLocPortTable.setStatus("current")
_LldpLocPortEntry_Object = MibTableRow
lldpLocPortEntry = _LldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 7, 1)
)
lldpLocPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpLocPortNum"),
)
if mibBuilder.loadTexts:
    lldpLocPortEntry.setStatus("current")
_LldpLocPortNum_Type = LldpPortNumber
_LldpLocPortNum_Object = MibTableColumn
lldpLocPortNum = _LldpLocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 7, 1, 1),
    _LldpLocPortNum_Type()
)
lldpLocPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortNum.setStatus("current")
_LldpLocPortIdSubtype_Type = LldpPortIdSubtype
_LldpLocPortIdSubtype_Object = MibTableColumn
lldpLocPortIdSubtype = _LldpLocPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 7, 1, 2),
    _LldpLocPortIdSubtype_Type()
)
lldpLocPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortIdSubtype.setStatus("current")
_LldpLocPortId_Type = LldpPortId
_LldpLocPortId_Object = MibTableColumn
lldpLocPortId = _LldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 7, 1, 3),
    _LldpLocPortId_Type()
)
lldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortId.setStatus("current")


class _LldpLocPortDesc_Type(SnmpAdminString):
    """Custom type lldpLocPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocPortDesc_Type.__name__ = "SnmpAdminString"
_LldpLocPortDesc_Object = MibTableColumn
lldpLocPortDesc = _LldpLocPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 7, 1, 4),
    _LldpLocPortDesc_Type()
)
lldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocPortDesc.setStatus("current")
_LldpLocManAddrTable_Object = MibTable
lldpLocManAddrTable = _LldpLocManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8)
)
if mibBuilder.loadTexts:
    lldpLocManAddrTable.setStatus("current")
_LldpLocManAddrEntry_Object = MibTableRow
lldpLocManAddrEntry = _LldpLocManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8, 1)
)
lldpLocManAddrEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpLocManAddrSubtype"),
    (0, "DGS-1100-10ME_A1", "lldpLocManAddr"),
)
if mibBuilder.loadTexts:
    lldpLocManAddrEntry.setStatus("current")
_LldpLocManAddrSubtype_Type = AddressFamilyNumbers
_LldpLocManAddrSubtype_Object = MibTableColumn
lldpLocManAddrSubtype = _LldpLocManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8, 1, 1),
    _LldpLocManAddrSubtype_Type()
)
lldpLocManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrSubtype.setStatus("current")
_LldpLocManAddr_Type = InetAddress
_LldpLocManAddr_Object = MibTableColumn
lldpLocManAddr = _LldpLocManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8, 1, 2),
    _LldpLocManAddr_Type()
)
lldpLocManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddr.setStatus("current")
_LldpLocManAddrLen_Type = Integer32
_LldpLocManAddrLen_Object = MibTableColumn
lldpLocManAddrLen = _LldpLocManAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8, 1, 3),
    _LldpLocManAddrLen_Type()
)
lldpLocManAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrLen.setStatus("current")
_LldpLocManAddrIfSubtype_Type = LldpManAddrIfSubtype
_LldpLocManAddrIfSubtype_Object = MibTableColumn
lldpLocManAddrIfSubtype = _LldpLocManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8, 1, 4),
    _LldpLocManAddrIfSubtype_Type()
)
lldpLocManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrIfSubtype.setStatus("current")
_LldpLocManAddrIfId_Type = Integer32
_LldpLocManAddrIfId_Object = MibTableColumn
lldpLocManAddrIfId = _LldpLocManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8, 1, 5),
    _LldpLocManAddrIfId_Type()
)
lldpLocManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrIfId.setStatus("current")
_LldpLocManAddrOID_Type = ObjectIdentifier
_LldpLocManAddrOID_Object = MibTableColumn
lldpLocManAddrOID = _LldpLocManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 15, 8, 1, 6),
    _LldpLocManAddrOID_Type()
)
lldpLocManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocManAddrOID.setStatus("current")
_SysLLDPRemoteSystemsData_ObjectIdentity = ObjectIdentity
sysLLDPRemoteSystemsData = _SysLLDPRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16)
)
_LldpRemTable_Object = MibTable
lldpRemTable = _LldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1)
)
if mibBuilder.loadTexts:
    lldpRemTable.setStatus("current")
_LldpRemEntry_Object = MibTableRow
lldpRemEntry = _LldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1)
)
lldpRemEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpRemTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpRemLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    lldpRemEntry.setStatus("current")
_LldpRemTimeMark_Type = TimeFilter
_LldpRemTimeMark_Object = MibTableColumn
lldpRemTimeMark = _LldpRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 1),
    _LldpRemTimeMark_Type()
)
lldpRemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemTimeMark.setStatus("current")
_LldpRemLocalPortNum_Type = LldpPortNumber
_LldpRemLocalPortNum_Object = MibTableColumn
lldpRemLocalPortNum = _LldpRemLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 2),
    _LldpRemLocalPortNum_Type()
)
lldpRemLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemLocalPortNum.setStatus("current")


class _LldpRemIndex_Type(Integer32):
    """Custom type lldpRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemIndex_Type.__name__ = "Integer32"
_LldpRemIndex_Object = MibTableColumn
lldpRemIndex = _LldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 3),
    _LldpRemIndex_Type()
)
lldpRemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemIndex.setStatus("current")
_LldpRemChassisIdSubtype_Type = LldpChassisIdSubtype
_LldpRemChassisIdSubtype_Object = MibTableColumn
lldpRemChassisIdSubtype = _LldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 4),
    _LldpRemChassisIdSubtype_Type()
)
lldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisIdSubtype.setStatus("current")
_LldpRemChassisId_Type = LldpChassisId
_LldpRemChassisId_Object = MibTableColumn
lldpRemChassisId = _LldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 5),
    _LldpRemChassisId_Type()
)
lldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemChassisId.setStatus("current")
_LldpRemPortIdSubtype_Type = LldpPortIdSubtype
_LldpRemPortIdSubtype_Object = MibTableColumn
lldpRemPortIdSubtype = _LldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 6),
    _LldpRemPortIdSubtype_Type()
)
lldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortIdSubtype.setStatus("current")
_LldpRemPortId_Type = LldpPortId
_LldpRemPortId_Object = MibTableColumn
lldpRemPortId = _LldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 7),
    _LldpRemPortId_Type()
)
lldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortId.setStatus("current")


class _LldpRemPortDesc_Type(SnmpAdminString):
    """Custom type lldpRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemPortDesc_Type.__name__ = "SnmpAdminString"
_LldpRemPortDesc_Object = MibTableColumn
lldpRemPortDesc = _LldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 8),
    _LldpRemPortDesc_Type()
)
lldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemPortDesc.setStatus("current")


class _LldpRemSysName_Type(SnmpAdminString):
    """Custom type lldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysName_Type.__name__ = "SnmpAdminString"
_LldpRemSysName_Object = MibTableColumn
lldpRemSysName = _LldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 9),
    _LldpRemSysName_Type()
)
lldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysName.setStatus("current")


class _LldpRemSysDesc_Type(SnmpAdminString):
    """Custom type lldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_LldpRemSysDesc_Object = MibTableColumn
lldpRemSysDesc = _LldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 10),
    _LldpRemSysDesc_Type()
)
lldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysDesc.setStatus("current")
_LldpRemSysCapSupported_Type = LldpSystemCapabilitiesMap
_LldpRemSysCapSupported_Object = MibTableColumn
lldpRemSysCapSupported = _LldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 11),
    _LldpRemSysCapSupported_Type()
)
lldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysCapSupported.setStatus("current")
_LldpRemSysCapEnabled_Type = LldpSystemCapabilitiesMap
_LldpRemSysCapEnabled_Object = MibTableColumn
lldpRemSysCapEnabled = _LldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 1, 1, 12),
    _LldpRemSysCapEnabled_Type()
)
lldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemSysCapEnabled.setStatus("current")
_LldpRemManAddrTable_Object = MibTable
lldpRemManAddrTable = _LldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2)
)
if mibBuilder.loadTexts:
    lldpRemManAddrTable.setStatus("current")
_LldpRemManAddrEntry_Object = MibTableRow
lldpRemManAddrEntry = _LldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1)
)
lldpRemManAddrEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpRemManTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpRemManLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpRemManIndex"),
    (0, "DGS-1100-10ME_A1", "lldpRemManAddrSubtype"),
    (0, "DGS-1100-10ME_A1", "lldpRemManAddr"),
)
if mibBuilder.loadTexts:
    lldpRemManAddrEntry.setStatus("current")
_LldpRemManTimeMark_Type = TimeFilter
_LldpRemManTimeMark_Object = MibTableColumn
lldpRemManTimeMark = _LldpRemManTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 1),
    _LldpRemManTimeMark_Type()
)
lldpRemManTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManTimeMark.setStatus("current")
_LldpRemManLocalPortNum_Type = LldpPortNumber
_LldpRemManLocalPortNum_Object = MibTableColumn
lldpRemManLocalPortNum = _LldpRemManLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 2),
    _LldpRemManLocalPortNum_Type()
)
lldpRemManLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManLocalPortNum.setStatus("current")


class _LldpRemManIndex_Type(Integer32):
    """Custom type lldpRemManIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemManIndex_Type.__name__ = "Integer32"
_LldpRemManIndex_Object = MibTableColumn
lldpRemManIndex = _LldpRemManIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 3),
    _LldpRemManIndex_Type()
)
lldpRemManIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManIndex.setStatus("current")
_LldpRemManAddrSubtype_Type = AddressFamilyNumbers
_LldpRemManAddrSubtype_Object = MibTableColumn
lldpRemManAddrSubtype = _LldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 4),
    _LldpRemManAddrSubtype_Type()
)
lldpRemManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrSubtype.setStatus("current")
_LldpRemManAddr_Type = InetAddress
_LldpRemManAddr_Object = MibTableColumn
lldpRemManAddr = _LldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 5),
    _LldpRemManAddr_Type()
)
lldpRemManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddr.setStatus("current")
_LldpRemManAddrIfSubtype_Type = LldpManAddrIfSubtype
_LldpRemManAddrIfSubtype_Object = MibTableColumn
lldpRemManAddrIfSubtype = _LldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 6),
    _LldpRemManAddrIfSubtype_Type()
)
lldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrIfSubtype.setStatus("current")
_LldpRemManAddrIfId_Type = Integer32
_LldpRemManAddrIfId_Object = MibTableColumn
lldpRemManAddrIfId = _LldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 7),
    _LldpRemManAddrIfId_Type()
)
lldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrIfId.setStatus("current")
_LldpRemManAddrOID_Type = ObjectIdentifier
_LldpRemManAddrOID_Object = MibTableColumn
lldpRemManAddrOID = _LldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 2, 1, 8),
    _LldpRemManAddrOID_Type()
)
lldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemManAddrOID.setStatus("current")
_LldpRemUnknownTLVTable_Object = MibTable
lldpRemUnknownTLVTable = _LldpRemUnknownTLVTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 3)
)
if mibBuilder.loadTexts:
    lldpRemUnknownTLVTable.setStatus("current")
_LldpRemUnknownTLVEntry_Object = MibTableRow
lldpRemUnknownTLVEntry = _LldpRemUnknownTLVEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 3, 1)
)
lldpRemUnknownTLVEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "lldpRemUnknownTimeMark"),
    (0, "DGS-1100-10ME_A1", "lldpRemUnknownLocalPortNum"),
    (0, "DGS-1100-10ME_A1", "lldpRemUnknownIndex"),
    (0, "DGS-1100-10ME_A1", "lldpRemUnknownTLVType"),
)
if mibBuilder.loadTexts:
    lldpRemUnknownTLVEntry.setStatus("current")
_LldpRemUnknownTimeMark_Type = TimeFilter
_LldpRemUnknownTimeMark_Object = MibTableColumn
lldpRemUnknownTimeMark = _LldpRemUnknownTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 3, 1, 1),
    _LldpRemUnknownTimeMark_Type()
)
lldpRemUnknownTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownTimeMark.setStatus("current")
_LldpRemUnknownLocalPortNum_Type = LldpPortNumber
_LldpRemUnknownLocalPortNum_Object = MibTableColumn
lldpRemUnknownLocalPortNum = _LldpRemUnknownLocalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 3, 1, 2),
    _LldpRemUnknownLocalPortNum_Type()
)
lldpRemUnknownLocalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownLocalPortNum.setStatus("current")


class _LldpRemUnknownIndex_Type(Integer32):
    """Custom type lldpRemUnknownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpRemUnknownIndex_Type.__name__ = "Integer32"
_LldpRemUnknownIndex_Object = MibTableColumn
lldpRemUnknownIndex = _LldpRemUnknownIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 3, 1, 3),
    _LldpRemUnknownIndex_Type()
)
lldpRemUnknownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownIndex.setStatus("current")


class _LldpRemUnknownTLVType_Type(Integer32):
    """Custom type lldpRemUnknownTLVType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 126),
    )


_LldpRemUnknownTLVType_Type.__name__ = "Integer32"
_LldpRemUnknownTLVType_Object = MibTableColumn
lldpRemUnknownTLVType = _LldpRemUnknownTLVType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 3, 1, 4),
    _LldpRemUnknownTLVType_Type()
)
lldpRemUnknownTLVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownTLVType.setStatus("current")


class _LldpRemUnknownTLVInfo_Type(OctetString):
    """Custom type lldpRemUnknownTLVInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_LldpRemUnknownTLVInfo_Type.__name__ = "OctetString"
_LldpRemUnknownTLVInfo_Object = MibTableColumn
lldpRemUnknownTLVInfo = _LldpRemUnknownTLVInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 16, 3, 1, 5),
    _LldpRemUnknownTLVInfo_Type()
)
lldpRemUnknownTLVInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemUnknownTLVInfo.setStatus("current")
_SysLLDPNotification_ObjectIdentity = ObjectIdentity
sysLLDPNotification = _SysLLDPNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17)
)
_LldpTraps_ObjectIdentity = ObjectIdentity
lldpTraps = _LldpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0)
)
_CompanyCableDiagnostic_ObjectIdentity = ObjectIdentity
companyCableDiagnostic = _CompanyCableDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35)
)
_SysCableDiagTriggerIndex_Type = Integer32
_SysCableDiagTriggerIndex_Object = MibScalar
sysCableDiagTriggerIndex = _SysCableDiagTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 1),
    _SysCableDiagTriggerIndex_Type()
)
sysCableDiagTriggerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCableDiagTriggerIndex.setStatus("current")


class _SysCableDiagPair1TestResult_Type(Integer32):
    """Custom type sysCableDiagPair1TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_SysCableDiagPair1TestResult_Type.__name__ = "Integer32"
_SysCableDiagPair1TestResult_Object = MibScalar
sysCableDiagPair1TestResult = _SysCableDiagPair1TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 2),
    _SysCableDiagPair1TestResult_Type()
)
sysCableDiagPair1TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair1TestResult.setStatus("current")
_SysCableDiagPair1FaultDistance_Type = Integer32
_SysCableDiagPair1FaultDistance_Object = MibScalar
sysCableDiagPair1FaultDistance = _SysCableDiagPair1FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 3),
    _SysCableDiagPair1FaultDistance_Type()
)
sysCableDiagPair1FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair1FaultDistance.setStatus("current")


class _SysCableDiagPair2TestResult_Type(Integer32):
    """Custom type sysCableDiagPair2TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_SysCableDiagPair2TestResult_Type.__name__ = "Integer32"
_SysCableDiagPair2TestResult_Object = MibScalar
sysCableDiagPair2TestResult = _SysCableDiagPair2TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 4),
    _SysCableDiagPair2TestResult_Type()
)
sysCableDiagPair2TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair2TestResult.setStatus("current")
_SysCableDiagPair2FaultDistance_Type = Integer32
_SysCableDiagPair2FaultDistance_Object = MibScalar
sysCableDiagPair2FaultDistance = _SysCableDiagPair2FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 5),
    _SysCableDiagPair2FaultDistance_Type()
)
sysCableDiagPair2FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair2FaultDistance.setStatus("current")


class _SysCableDiagPair3TestResult_Type(Integer32):
    """Custom type sysCableDiagPair3TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_SysCableDiagPair3TestResult_Type.__name__ = "Integer32"
_SysCableDiagPair3TestResult_Object = MibScalar
sysCableDiagPair3TestResult = _SysCableDiagPair3TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 6),
    _SysCableDiagPair3TestResult_Type()
)
sysCableDiagPair3TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair3TestResult.setStatus("current")
_SysCableDiagPair3FaultDistance_Type = Integer32
_SysCableDiagPair3FaultDistance_Object = MibScalar
sysCableDiagPair3FaultDistance = _SysCableDiagPair3FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 7),
    _SysCableDiagPair3FaultDistance_Type()
)
sysCableDiagPair3FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair3FaultDistance.setStatus("current")


class _SysCableDiagPair4TestResult_Type(Integer32):
    """Custom type sysCableDiagPair4TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 5),
          ("ok", 0),
          ("open", 1),
          ("short", 2))
    )


_SysCableDiagPair4TestResult_Type.__name__ = "Integer32"
_SysCableDiagPair4TestResult_Object = MibScalar
sysCableDiagPair4TestResult = _SysCableDiagPair4TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 8),
    _SysCableDiagPair4TestResult_Type()
)
sysCableDiagPair4TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair4TestResult.setStatus("current")
_SysCableDiagPair4FaultDistance_Type = Integer32
_SysCableDiagPair4FaultDistance_Object = MibScalar
sysCableDiagPair4FaultDistance = _SysCableDiagPair4FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 9),
    _SysCableDiagPair4FaultDistance_Type()
)
sysCableDiagPair4FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagPair4FaultDistance.setStatus("current")


class _SysCableDiagLengthinRange_Type(Integer32):
    """Custom type sysCableDiagLengthinRange based on Integer32"""
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
        *(("from100to140", 4),
          ("from50to80", 2),
          ("from80to100", 3),
          ("less50", 1),
          ("notAvailable", 5))
    )


_SysCableDiagLengthinRange_Type.__name__ = "Integer32"
_SysCableDiagLengthinRange_Object = MibScalar
sysCableDiagLengthinRange = _SysCableDiagLengthinRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 35, 10),
    _SysCableDiagLengthinRange_Type()
)
sysCableDiagLengthinRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCableDiagLengthinRange.setStatus("current")
_CompanyQinQ_ObjectIdentity = ObjectIdentity
companyQinQ = _CompanyQinQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37)
)
_SysQinQSystem_ObjectIdentity = ObjectIdentity
sysQinQSystem = _SysQinQSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1)
)


class _QinQGlobalStatus_Type(Integer32):
    """Custom type qinQGlobalStatus based on Integer32"""
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


_QinQGlobalStatus_Type.__name__ = "Integer32"
_QinQGlobalStatus_Object = MibScalar
qinQGlobalStatus = _QinQGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 1),
    _QinQGlobalStatus_Type()
)
qinQGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQGlobalStatus.setStatus("current")
_QinQConfigTable_Object = MibTable
qinQConfigTable = _QinQConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 2)
)
if mibBuilder.loadTexts:
    qinQConfigTable.setStatus("current")
_QinQConfigEntry_Object = MibTableRow
qinQConfigEntry = _QinQConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 2, 1)
)
qinQConfigEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "qinQIfIndex"),
)
if mibBuilder.loadTexts:
    qinQConfigEntry.setStatus("current")
_QinQIfIndex_Type = InterfaceIndex
_QinQIfIndex_Object = MibTableColumn
qinQIfIndex = _QinQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 2, 1, 1),
    _QinQIfIndex_Type()
)
qinQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qinQIfIndex.setStatus("current")


class _QinQRoleState_Type(Integer32):
    """Custom type qinQRoleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_QinQRoleState_Type.__name__ = "Integer32"
_QinQRoleState_Object = MibTableColumn
qinQRoleState = _QinQRoleState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 2, 1, 2),
    _QinQRoleState_Type()
)
qinQRoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQRoleState.setStatus("current")
_QinQOuterTPID_Type = Unsigned32
_QinQOuterTPID_Object = MibTableColumn
qinQOuterTPID = _QinQOuterTPID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 2, 1, 3),
    _QinQOuterTPID_Type()
)
qinQOuterTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQOuterTPID.setStatus("current")


class _QinQMissDrop_Type(Integer32):
    """Custom type qinQMissDrop based on Integer32"""
    defaultValue = 2

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


_QinQMissDrop_Type.__name__ = "Integer32"
_QinQMissDrop_Object = MibTableColumn
qinQMissDrop = _QinQMissDrop_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 2, 1, 4),
    _QinQMissDrop_Type()
)
qinQMissDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQMissDrop.setStatus("current")
_QinQAddInnerTag_Type = Unsigned32
_QinQAddInnerTag_Object = MibTableColumn
qinQAddInnerTag = _QinQAddInnerTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 2, 1, 5),
    _QinQAddInnerTag_Type()
)
qinQAddInnerTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQAddInnerTag.setStatus("current")
_QinQInnerTPID_Type = Unsigned32
_QinQInnerTPID_Object = MibScalar
qinQInnerTPID = _QinQInnerTPID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 3),
    _QinQInnerTPID_Type()
)
qinQInnerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQInnerTPID.setStatus("current")
_QinQVlanTranslationTable_Object = MibTable
qinQVlanTranslationTable = _QinQVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4)
)
if mibBuilder.loadTexts:
    qinQVlanTranslationTable.setStatus("current")
_QinQVlanTranslationEntry_Object = MibTableRow
qinQVlanTranslationEntry = _QinQVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4, 1)
)
qinQVlanTranslationEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "qinQVlanTransPortNum"),
    (0, "DGS-1100-10ME_A1", "qinQVlanTransCVID"),
)
if mibBuilder.loadTexts:
    qinQVlanTranslationEntry.setStatus("current")
_QinQVlanTransPortNum_Type = Integer32
_QinQVlanTransPortNum_Object = MibTableColumn
qinQVlanTransPortNum = _QinQVlanTransPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4, 1, 1),
    _QinQVlanTransPortNum_Type()
)
qinQVlanTransPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qinQVlanTransPortNum.setStatus("current")


class _QinQVlanTransCVID_Type(Integer32):
    """Custom type qinQVlanTransCVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QinQVlanTransCVID_Type.__name__ = "Integer32"
_QinQVlanTransCVID_Object = MibTableColumn
qinQVlanTransCVID = _QinQVlanTransCVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4, 1, 2),
    _QinQVlanTransCVID_Type()
)
qinQVlanTransCVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qinQVlanTransCVID.setStatus("current")


class _QinQVlanTransSVID_Type(Integer32):
    """Custom type qinQVlanTransSVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QinQVlanTransSVID_Type.__name__ = "Integer32"
_QinQVlanTransSVID_Object = MibTableColumn
qinQVlanTransSVID = _QinQVlanTransSVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4, 1, 3),
    _QinQVlanTransSVID_Type()
)
qinQVlanTransSVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQVlanTransSVID.setStatus("current")


class _QinQVlanTransAction_Type(Integer32):
    """Custom type qinQVlanTransAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("replace", 2))
    )


_QinQVlanTransAction_Type.__name__ = "Integer32"
_QinQVlanTransAction_Object = MibTableColumn
qinQVlanTransAction = _QinQVlanTransAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4, 1, 4),
    _QinQVlanTransAction_Type()
)
qinQVlanTransAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQVlanTransAction.setStatus("current")


class _QinQVlanTransPriority_Type(Integer32):
    """Custom type qinQVlanTransPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_QinQVlanTransPriority_Type.__name__ = "Integer32"
_QinQVlanTransPriority_Object = MibTableColumn
qinQVlanTransPriority = _QinQVlanTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4, 1, 5),
    _QinQVlanTransPriority_Type()
)
qinQVlanTransPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinQVlanTransPriority.setStatus("current")
_QinQVlanTransRowStatus_Type = RowStatus
_QinQVlanTransRowStatus_Object = MibTableColumn
qinQVlanTransRowStatus = _QinQVlanTransRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 37, 1, 4, 1, 6),
    _QinQVlanTransRowStatus_Type()
)
qinQVlanTransRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qinQVlanTransRowStatus.setStatus("current")
_CompanyTimeRangeMgmt_ObjectIdentity = ObjectIdentity
companyTimeRangeMgmt = _CompanyTimeRangeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38)
)
_SysTimeRangeSettingTable_Object = MibTable
sysTimeRangeSettingTable = _SysTimeRangeSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1)
)
if mibBuilder.loadTexts:
    sysTimeRangeSettingTable.setStatus("current")
_TimeRangeSettingEntry_Object = MibTableRow
timeRangeSettingEntry = _TimeRangeSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1)
)
timeRangeSettingEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "timeRangeIndex"),
)
if mibBuilder.loadTexts:
    timeRangeSettingEntry.setStatus("current")


class _TimeRangeIndex_Type(Integer32):
    """Custom type timeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_TimeRangeIndex_Type.__name__ = "Integer32"
_TimeRangeIndex_Object = MibTableColumn
timeRangeIndex = _TimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 1),
    _TimeRangeIndex_Type()
)
timeRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeIndex.setStatus("current")


class _TimeRangeName_Type(DisplayString):
    """Custom type timeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TimeRangeName_Type.__name__ = "DisplayString"
_TimeRangeName_Object = MibTableColumn
timeRangeName = _TimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 2),
    _TimeRangeName_Type()
)
timeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeName.setStatus("current")


class _TimeRangeDate_Type(Integer32):
    """Custom type timeRangeDate based on Integer32"""
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


_TimeRangeDate_Type.__name__ = "Integer32"
_TimeRangeDate_Object = MibTableColumn
timeRangeDate = _TimeRangeDate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 3),
    _TimeRangeDate_Type()
)
timeRangeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeDate.setStatus("current")


class _TimeRangeStartYear_Type(Integer32):
    """Custom type timeRangeStartYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2014,
              2015,
              2016,
              2017,
              2018,
              2019,
              2020,
              2021,
              2022,
              2023,
              2024,
              2025,
              2026,
              2027,
              2028,
              2029)
        )
    )
    namedValues = NamedValues(
        *(("y2014", 2014),
          ("y2015", 2015),
          ("y2016", 2016),
          ("y2017", 2017),
          ("y2018", 2018),
          ("y2019", 2019),
          ("y2020", 2020),
          ("y2021", 2021),
          ("y2022", 2022),
          ("y2023", 2023),
          ("y2024", 2024),
          ("y2025", 2025),
          ("y2026", 2026),
          ("y2027", 2027),
          ("y2028", 2028),
          ("y2029", 2029))
    )


_TimeRangeStartYear_Type.__name__ = "Integer32"
_TimeRangeStartYear_Object = MibTableColumn
timeRangeStartYear = _TimeRangeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 4),
    _TimeRangeStartYear_Type()
)
timeRangeStartYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeStartYear.setStatus("current")


class _TimeRangeStartMonth_Type(Integer32):
    """Custom type timeRangeStartMonth based on Integer32"""
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_TimeRangeStartMonth_Type.__name__ = "Integer32"
_TimeRangeStartMonth_Object = MibTableColumn
timeRangeStartMonth = _TimeRangeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 5),
    _TimeRangeStartMonth_Type()
)
timeRangeStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeStartMonth.setStatus("current")


class _TimeRangeStartDay_Type(Integer32):
    """Custom type timeRangeStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TimeRangeStartDay_Type.__name__ = "Integer32"
_TimeRangeStartDay_Object = MibTableColumn
timeRangeStartDay = _TimeRangeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 6),
    _TimeRangeStartDay_Type()
)
timeRangeStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeStartDay.setStatus("current")


class _TimeRangeStartHour_Type(Integer32):
    """Custom type timeRangeStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeRangeStartHour_Type.__name__ = "Integer32"
_TimeRangeStartHour_Object = MibTableColumn
timeRangeStartHour = _TimeRangeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 7),
    _TimeRangeStartHour_Type()
)
timeRangeStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeStartHour.setStatus("current")


class _TimeRangeStartMinute_Type(Integer32):
    """Custom type timeRangeStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeRangeStartMinute_Type.__name__ = "Integer32"
_TimeRangeStartMinute_Object = MibTableColumn
timeRangeStartMinute = _TimeRangeStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 8),
    _TimeRangeStartMinute_Type()
)
timeRangeStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeStartMinute.setStatus("current")


class _TimeRangeEndYear_Type(Integer32):
    """Custom type timeRangeEndYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2011,
              2012,
              2013,
              2014,
              2015,
              2016,
              2017,
              2018,
              2019,
              2020,
              2021,
              2022,
              2023,
              2024,
              2025,
              2026,
              2027,
              2028,
              2029)
        )
    )
    namedValues = NamedValues(
        *(("y2011", 2011),
          ("y2012", 2012),
          ("y2013", 2013),
          ("y2014", 2014),
          ("y2015", 2015),
          ("y2016", 2016),
          ("y2017", 2017),
          ("y2018", 2018),
          ("y2019", 2019),
          ("y2020", 2020),
          ("y2021", 2021),
          ("y2022", 2022),
          ("y2023", 2023),
          ("y2024", 2024),
          ("y2025", 2025),
          ("y2026", 2026),
          ("y2027", 2027),
          ("y2028", 2028),
          ("y2029", 2029))
    )


_TimeRangeEndYear_Type.__name__ = "Integer32"
_TimeRangeEndYear_Object = MibTableColumn
timeRangeEndYear = _TimeRangeEndYear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 9),
    _TimeRangeEndYear_Type()
)
timeRangeEndYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEndYear.setStatus("current")


class _TimeRangeEndMonth_Type(Integer32):
    """Custom type timeRangeEndMonth based on Integer32"""
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_TimeRangeEndMonth_Type.__name__ = "Integer32"
_TimeRangeEndMonth_Object = MibTableColumn
timeRangeEndMonth = _TimeRangeEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 10),
    _TimeRangeEndMonth_Type()
)
timeRangeEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEndMonth.setStatus("current")


class _TimeRangeEndDay_Type(Integer32):
    """Custom type timeRangeEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TimeRangeEndDay_Type.__name__ = "Integer32"
_TimeRangeEndDay_Object = MibTableColumn
timeRangeEndDay = _TimeRangeEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 11),
    _TimeRangeEndDay_Type()
)
timeRangeEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEndDay.setStatus("current")


class _TimeRangeEndHour_Type(Integer32):
    """Custom type timeRangeEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeRangeEndHour_Type.__name__ = "Integer32"
_TimeRangeEndHour_Object = MibTableColumn
timeRangeEndHour = _TimeRangeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 12),
    _TimeRangeEndHour_Type()
)
timeRangeEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEndHour.setStatus("current")


class _TimeRangeEndMinute_Type(Integer32):
    """Custom type timeRangeEndMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeRangeEndMinute_Type.__name__ = "Integer32"
_TimeRangeEndMinute_Object = MibTableColumn
timeRangeEndMinute = _TimeRangeEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 13),
    _TimeRangeEndMinute_Type()
)
timeRangeEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEndMinute.setStatus("current")


class _TimeRangeMonday_Type(Integer32):
    """Custom type timeRangeMonday based on Integer32"""
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


_TimeRangeMonday_Type.__name__ = "Integer32"
_TimeRangeMonday_Object = MibTableColumn
timeRangeMonday = _TimeRangeMonday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 14),
    _TimeRangeMonday_Type()
)
timeRangeMonday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeMonday.setStatus("current")


class _TimeRangeTuesday_Type(Integer32):
    """Custom type timeRangeTuesday based on Integer32"""
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


_TimeRangeTuesday_Type.__name__ = "Integer32"
_TimeRangeTuesday_Object = MibTableColumn
timeRangeTuesday = _TimeRangeTuesday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 15),
    _TimeRangeTuesday_Type()
)
timeRangeTuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeTuesday.setStatus("current")


class _TimeRangeWednesday_Type(Integer32):
    """Custom type timeRangeWednesday based on Integer32"""
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


_TimeRangeWednesday_Type.__name__ = "Integer32"
_TimeRangeWednesday_Object = MibTableColumn
timeRangeWednesday = _TimeRangeWednesday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 16),
    _TimeRangeWednesday_Type()
)
timeRangeWednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeWednesday.setStatus("current")


class _TimeRangeThursday_Type(Integer32):
    """Custom type timeRangeThursday based on Integer32"""
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


_TimeRangeThursday_Type.__name__ = "Integer32"
_TimeRangeThursday_Object = MibTableColumn
timeRangeThursday = _TimeRangeThursday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 17),
    _TimeRangeThursday_Type()
)
timeRangeThursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeThursday.setStatus("current")


class _TimeRangeFriday_Type(Integer32):
    """Custom type timeRangeFriday based on Integer32"""
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


_TimeRangeFriday_Type.__name__ = "Integer32"
_TimeRangeFriday_Object = MibTableColumn
timeRangeFriday = _TimeRangeFriday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 18),
    _TimeRangeFriday_Type()
)
timeRangeFriday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeFriday.setStatus("current")


class _TimeRangeSaturday_Type(Integer32):
    """Custom type timeRangeSaturday based on Integer32"""
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


_TimeRangeSaturday_Type.__name__ = "Integer32"
_TimeRangeSaturday_Object = MibTableColumn
timeRangeSaturday = _TimeRangeSaturday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 19),
    _TimeRangeSaturday_Type()
)
timeRangeSaturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeSaturday.setStatus("current")


class _TimeRangeSunday_Type(Integer32):
    """Custom type timeRangeSunday based on Integer32"""
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


_TimeRangeSunday_Type.__name__ = "Integer32"
_TimeRangeSunday_Object = MibTableColumn
timeRangeSunday = _TimeRangeSunday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 20),
    _TimeRangeSunday_Type()
)
timeRangeSunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeSunday.setStatus("current")
_TimeRangeRowStatus_Type = RowStatus
_TimeRangeRowStatus_Object = MibTableColumn
timeRangeRowStatus = _TimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 38, 1, 1, 21),
    _TimeRangeRowStatus_Type()
)
timeRangeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRowStatus.setStatus("current")
_CompanyLimitIP_ObjectIdentity = ObjectIdentity
companyLimitIP = _CompanyLimitIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45)
)
_SyslimitIPMulticastProfileTable_Object = MibTable
syslimitIPMulticastProfileTable = _SyslimitIPMulticastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 1)
)
if mibBuilder.loadTexts:
    syslimitIPMulticastProfileTable.setStatus("current")
_LimitIPMulticastProfileEntry_Object = MibTableRow
limitIPMulticastProfileEntry = _LimitIPMulticastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 1, 1)
)
limitIPMulticastProfileEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "limitIPMulticastProfileID"),
    (0, "DGS-1100-10ME_A1", "limitIPMulticastIPType"),
)
if mibBuilder.loadTexts:
    limitIPMulticastProfileEntry.setStatus("current")
_LimitIPMulticastProfileID_Type = Integer32
_LimitIPMulticastProfileID_Object = MibTableColumn
limitIPMulticastProfileID = _LimitIPMulticastProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 1, 1, 1),
    _LimitIPMulticastProfileID_Type()
)
limitIPMulticastProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIPMulticastProfileID.setStatus("current")


class _LimitIPMulticastIPType_Type(Integer32):
    """Custom type limitIPMulticastIPType based on Integer32"""
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


_LimitIPMulticastIPType_Type.__name__ = "Integer32"
_LimitIPMulticastIPType_Object = MibTableColumn
limitIPMulticastIPType = _LimitIPMulticastIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 1, 1, 2),
    _LimitIPMulticastIPType_Type()
)
limitIPMulticastIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIPMulticastIPType.setStatus("current")


class _LimitIPMulticastProfileName_Type(DisplayString):
    """Custom type limitIPMulticastProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LimitIPMulticastProfileName_Type.__name__ = "DisplayString"
_LimitIPMulticastProfileName_Object = MibTableColumn
limitIPMulticastProfileName = _LimitIPMulticastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 1, 1, 3),
    _LimitIPMulticastProfileName_Type()
)
limitIPMulticastProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIPMulticastProfileName.setStatus("current")
_LimitIPMulticastProfileStatus_Type = RowStatus
_LimitIPMulticastProfileStatus_Object = MibTableColumn
limitIPMulticastProfileStatus = _LimitIPMulticastProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 1, 1, 4),
    _LimitIPMulticastProfileStatus_Type()
)
limitIPMulticastProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIPMulticastProfileStatus.setStatus("current")
_SyslimitIPMulticastPortTable_Object = MibTable
syslimitIPMulticastPortTable = _SyslimitIPMulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 3)
)
if mibBuilder.loadTexts:
    syslimitIPMulticastPortTable.setStatus("current")
_LimitIPMulticastPortEntry_Object = MibTableRow
limitIPMulticastPortEntry = _LimitIPMulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 3, 1)
)
limitIPMulticastPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "limitIPMulticastPortID"),
    (0, "DGS-1100-10ME_A1", "limitIPMulticastPortIPType"),
)
if mibBuilder.loadTexts:
    limitIPMulticastPortEntry.setStatus("current")
_LimitIPMulticastPortID_Type = Integer32
_LimitIPMulticastPortID_Object = MibTableColumn
limitIPMulticastPortID = _LimitIPMulticastPortID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 3, 1, 1),
    _LimitIPMulticastPortID_Type()
)
limitIPMulticastPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIPMulticastPortID.setStatus("current")


class _LimitIPMulticastPortIPType_Type(Integer32):
    """Custom type limitIPMulticastPortIPType based on Integer32"""
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


_LimitIPMulticastPortIPType_Type.__name__ = "Integer32"
_LimitIPMulticastPortIPType_Object = MibTableColumn
limitIPMulticastPortIPType = _LimitIPMulticastPortIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 3, 1, 2),
    _LimitIPMulticastPortIPType_Type()
)
limitIPMulticastPortIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIPMulticastPortIPType.setStatus("current")


class _LimitIPMulticastPortState_Type(Integer32):
    """Custom type limitIPMulticastPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_LimitIPMulticastPortState_Type.__name__ = "Integer32"
_LimitIPMulticastPortState_Object = MibTableColumn
limitIPMulticastPortState = _LimitIPMulticastPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 3, 1, 3),
    _LimitIPMulticastPortState_Type()
)
limitIPMulticastPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIPMulticastPortState.setStatus("current")
_LimitIPMulticastPortProfileID_Type = PortList
_LimitIPMulticastPortProfileID_Object = MibTableColumn
limitIPMulticastPortProfileID = _LimitIPMulticastPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 3, 1, 4),
    _LimitIPMulticastPortProfileID_Type()
)
limitIPMulticastPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIPMulticastPortProfileID.setStatus("current")


class _LimitIPMulticastPortMaxGrp_Type(Unsigned32):
    """Custom type limitIPMulticastPortMaxGrp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LimitIPMulticastPortMaxGrp_Type.__name__ = "Unsigned32"
_LimitIPMulticastPortMaxGrp_Object = MibTableColumn
limitIPMulticastPortMaxGrp = _LimitIPMulticastPortMaxGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 3, 1, 5),
    _LimitIPMulticastPortMaxGrp_Type()
)
limitIPMulticastPortMaxGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIPMulticastPortMaxGrp.setStatus("current")
_LimitIpMulticastRangeTable_Object = MibTable
limitIpMulticastRangeTable = _LimitIpMulticastRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 4)
)
if mibBuilder.loadTexts:
    limitIpMulticastRangeTable.setStatus("current")
_LimitIpMulticastRangeEntry_Object = MibTableRow
limitIpMulticastRangeEntry = _LimitIpMulticastRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 4, 1)
)
limitIpMulticastRangeEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "limitIpMulticastRangeProfileID"),
    (0, "DGS-1100-10ME_A1", "limitIpMulticastRangeIPType"),
    (0, "DGS-1100-10ME_A1", "limitIpMulticastRangeStartIpAddr"),
    (0, "DGS-1100-10ME_A1", "limitIpMulticastRangeEndIpAddr"),
)
if mibBuilder.loadTexts:
    limitIpMulticastRangeEntry.setStatus("current")
_LimitIpMulticastRangeProfileID_Type = Integer32
_LimitIpMulticastRangeProfileID_Object = MibTableColumn
limitIpMulticastRangeProfileID = _LimitIpMulticastRangeProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 4, 1, 1),
    _LimitIpMulticastRangeProfileID_Type()
)
limitIpMulticastRangeProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastRangeProfileID.setStatus("current")


class _LimitIpMulticastRangeIPType_Type(Integer32):
    """Custom type limitIpMulticastRangeIPType based on Integer32"""
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


_LimitIpMulticastRangeIPType_Type.__name__ = "Integer32"
_LimitIpMulticastRangeIPType_Object = MibTableColumn
limitIpMulticastRangeIPType = _LimitIpMulticastRangeIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 4, 1, 2),
    _LimitIpMulticastRangeIPType_Type()
)
limitIpMulticastRangeIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastRangeIPType.setStatus("current")
_LimitIpMulticastRangeStartIpAddr_Type = InetAddress
_LimitIpMulticastRangeStartIpAddr_Object = MibTableColumn
limitIpMulticastRangeStartIpAddr = _LimitIpMulticastRangeStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 4, 1, 3),
    _LimitIpMulticastRangeStartIpAddr_Type()
)
limitIpMulticastRangeStartIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastRangeStartIpAddr.setStatus("current")
_LimitIpMulticastRangeEndIpAddr_Type = InetAddress
_LimitIpMulticastRangeEndIpAddr_Object = MibTableColumn
limitIpMulticastRangeEndIpAddr = _LimitIpMulticastRangeEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 4, 1, 4),
    _LimitIpMulticastRangeEndIpAddr_Type()
)
limitIpMulticastRangeEndIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastRangeEndIpAddr.setStatus("current")
_LimitIpMulticastRangeStatus_Type = RowStatus
_LimitIpMulticastRangeStatus_Object = MibTableColumn
limitIpMulticastRangeStatus = _LimitIpMulticastRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 45, 4, 1, 5),
    _LimitIpMulticastRangeStatus_Type()
)
limitIpMulticastRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastRangeStatus.setStatus("current")
_CompanyMulticastFilter_ObjectIdentity = ObjectIdentity
companyMulticastFilter = _CompanyMulticastFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 49)
)
_SysMulticastFilterPortTable_Object = MibTable
sysMulticastFilterPortTable = _SysMulticastFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 49, 1)
)
if mibBuilder.loadTexts:
    sysMulticastFilterPortTable.setStatus("current")
_MulticastFilterPortEntry_Object = MibTableRow
multicastFilterPortEntry = _MulticastFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 49, 1, 1)
)
multicastFilterPortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "multicastFilterPortIndex"),
)
if mibBuilder.loadTexts:
    multicastFilterPortEntry.setStatus("current")
_MulticastFilterPortIndex_Type = Integer32
_MulticastFilterPortIndex_Object = MibTableColumn
multicastFilterPortIndex = _MulticastFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 49, 1, 1, 1),
    _MulticastFilterPortIndex_Type()
)
multicastFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastFilterPortIndex.setStatus("current")


class _MulticastFilterPortType_Type(Integer32):
    """Custom type multicastFilterPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 0))
    )


_MulticastFilterPortType_Type.__name__ = "Integer32"
_MulticastFilterPortType_Object = MibTableColumn
multicastFilterPortType = _MulticastFilterPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 49, 1, 1, 2),
    _MulticastFilterPortType_Type()
)
multicastFilterPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastFilterPortType.setStatus("current")
_CompanyIPv6Neighbor_ObjectIdentity = ObjectIdentity
companyIPv6Neighbor = _CompanyIPv6Neighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50)
)
_SysIPv6neighborTable_Object = MibTable
sysIPv6neighborTable = _SysIPv6neighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    sysIPv6neighborTable.setStatus("current")
_Ipv6NeighborEntry_Object = MibTableRow
ipv6NeighborEntry = _Ipv6NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50, 1, 1)
)
ipv6NeighborEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "ipv6NeighborIndex"),
    (0, "DGS-1100-10ME_A1", "ipv6NeighborAddr"),
)
if mibBuilder.loadTexts:
    ipv6NeighborEntry.setStatus("current")
_Ipv6NeighborIndex_Type = Integer32
_Ipv6NeighborIndex_Object = MibTableColumn
ipv6NeighborIndex = _Ipv6NeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50, 1, 1, 1),
    _Ipv6NeighborIndex_Type()
)
ipv6NeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborIndex.setStatus("current")
_Ipv6NeighborAddr_Type = Ipv6Address
_Ipv6NeighborAddr_Object = MibTableColumn
ipv6NeighborAddr = _Ipv6NeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50, 1, 1, 2),
    _Ipv6NeighborAddr_Type()
)
ipv6NeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborAddr.setStatus("current")
_Ipv6NeighborMacAddr_Type = MacAddress
_Ipv6NeighborMacAddr_Object = MibTableColumn
ipv6NeighborMacAddr = _Ipv6NeighborMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50, 1, 1, 3),
    _Ipv6NeighborMacAddr_Type()
)
ipv6NeighborMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborMacAddr.setStatus("current")


class _Ipv6NeighborCacheState_Type(Integer32):
    """Custom type ipv6NeighborCacheState based on Integer32"""
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
        *(("delay", 5),
          ("incomplete", 3),
          ("notinservice", 7),
          ("probe", 6),
          ("reachable", 2),
          ("stale", 4),
          ("static", 1))
    )


_Ipv6NeighborCacheState_Type.__name__ = "Integer32"
_Ipv6NeighborCacheState_Object = MibTableColumn
ipv6NeighborCacheState = _Ipv6NeighborCacheState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50, 1, 1, 5),
    _Ipv6NeighborCacheState_Type()
)
ipv6NeighborCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NeighborCacheState.setStatus("current")
_Ipv6NeighborRowStatus_Type = RowStatus
_Ipv6NeighborRowStatus_Object = MibTableColumn
ipv6NeighborRowStatus = _Ipv6NeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 50, 1, 1, 7),
    _Ipv6NeighborRowStatus_Type()
)
ipv6NeighborRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6NeighborRowStatus.setStatus("current")
_CompanyEoam_ObjectIdentity = ObjectIdentity
companyEoam = _CompanyEoam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51)
)
_SysEoamSystem_ObjectIdentity = ObjectIdentity
sysEoamSystem = _SysEoamSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1)
)
_EoamTable_Object = MibTable
eoamTable = _EoamTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2)
)
if mibBuilder.loadTexts:
    eoamTable.setStatus("current")
_EoamEntry_Object = MibTableRow
eoamEntry = _EoamEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1)
)
eoamEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "eoamIfIndex"),
)
if mibBuilder.loadTexts:
    eoamEntry.setStatus("current")
_EoamIfIndex_Type = InterfaceIndex
_EoamIfIndex_Object = MibTableColumn
eoamIfIndex = _EoamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 1),
    _EoamIfIndex_Type()
)
eoamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamIfIndex.setStatus("current")


class _EoamState_Type(Integer32):
    """Custom type eoamState based on Integer32"""
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


_EoamState_Type.__name__ = "Integer32"
_EoamState_Object = MibTableColumn
eoamState = _EoamState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 2),
    _EoamState_Type()
)
eoamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamState.setStatus("current")


class _EoamMode_Type(Integer32):
    """Custom type eoamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_EoamMode_Type.__name__ = "Integer32"
_EoamMode_Object = MibTableColumn
eoamMode = _EoamMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 3),
    _EoamMode_Type()
)
eoamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamMode.setStatus("current")


class _EoamReceivedRemoteLoopback_Type(Integer32):
    """Custom type eoamReceivedRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_EoamReceivedRemoteLoopback_Type.__name__ = "Integer32"
_EoamReceivedRemoteLoopback_Object = MibTableColumn
eoamReceivedRemoteLoopback = _EoamReceivedRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 4),
    _EoamReceivedRemoteLoopback_Type()
)
eoamReceivedRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamReceivedRemoteLoopback.setStatus("current")


class _EoamRemoteLoopback_Type(Integer32):
    """Custom type eoamRemoteLoopback based on Integer32"""
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
        *(("localLoopBack", 5),
          ("noLoopBack", 1),
          ("remoteLoopBack", 3),
          ("startLoopBack", 2),
          ("stopLoopBack", 4),
          ("unknownLoopBack", 6))
    )


_EoamRemoteLoopback_Type.__name__ = "Integer32"
_EoamRemoteLoopback_Object = MibTableColumn
eoamRemoteLoopback = _EoamRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 5),
    _EoamRemoteLoopback_Type()
)
eoamRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamRemoteLoopback.setStatus("current")
_EoamMaxOAMPDU_Type = Unsigned32
_EoamMaxOAMPDU_Object = MibTableColumn
eoamMaxOAMPDU = _EoamMaxOAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 6),
    _EoamMaxOAMPDU_Type()
)
eoamMaxOAMPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamMaxOAMPDU.setStatus("current")


class _EoamUnidirection_Type(Integer32):
    """Custom type eoamUnidirection based on Integer32"""
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


_EoamUnidirection_Type.__name__ = "Integer32"
_EoamUnidirection_Object = MibTableColumn
eoamUnidirection = _EoamUnidirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 7),
    _EoamUnidirection_Type()
)
eoamUnidirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamUnidirection.setStatus("current")


class _EoamLinkMonitoring_Type(Integer32):
    """Custom type eoamLinkMonitoring based on Integer32"""
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


_EoamLinkMonitoring_Type.__name__ = "Integer32"
_EoamLinkMonitoring_Object = MibTableColumn
eoamLinkMonitoring = _EoamLinkMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 8),
    _EoamLinkMonitoring_Type()
)
eoamLinkMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLinkMonitoring.setStatus("current")


class _EoamVarReq_Type(Integer32):
    """Custom type eoamVarReq based on Integer32"""
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


_EoamVarReq_Type.__name__ = "Integer32"
_EoamVarReq_Object = MibTableColumn
eoamVarReq = _EoamVarReq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 9),
    _EoamVarReq_Type()
)
eoamVarReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamVarReq.setStatus("current")


class _EoamRemoteLoopbackSupport_Type(Integer32):
    """Custom type eoamRemoteLoopbackSupport based on Integer32"""
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


_EoamRemoteLoopbackSupport_Type.__name__ = "Integer32"
_EoamRemoteLoopbackSupport_Object = MibTableColumn
eoamRemoteLoopbackSupport = _EoamRemoteLoopbackSupport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 10),
    _EoamRemoteLoopbackSupport_Type()
)
eoamRemoteLoopbackSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamRemoteLoopbackSupport.setStatus("current")
_EoamPDURev_Type = Unsigned32
_EoamPDURev_Object = MibTableColumn
eoamPDURev = _EoamPDURev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 11),
    _EoamPDURev_Type()
)
eoamPDURev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPDURev.setStatus("current")


class _EoamOperStatus_Type(Integer32):
    """Custom type eoamOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("activeSendLocal", 4),
          ("disabled", 1),
          ("linkFault", 2),
          ("nonOperHalfDuplex", 10),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemotelyRejected", 8),
          ("operational", 9),
          ("passiveWait", 3),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOk", 6))
    )


_EoamOperStatus_Type.__name__ = "Integer32"
_EoamOperStatus_Object = MibTableColumn
eoamOperStatus = _EoamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 12),
    _EoamOperStatus_Type()
)
eoamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamOperStatus.setStatus("current")


class _EoamPeerMode_Type(Integer32):
    """Custom type eoamPeerMode based on Integer32"""
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
          ("passive", 1),
          ("unknown", 3))
    )


_EoamPeerMode_Type.__name__ = "Integer32"
_EoamPeerMode_Object = MibTableColumn
eoamPeerMode = _EoamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 13),
    _EoamPeerMode_Type()
)
eoamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerMode.setStatus("current")
_EoamPeerMacAddress_Type = MacAddress
_EoamPeerMacAddress_Object = MibTableColumn
eoamPeerMacAddress = _EoamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 14),
    _EoamPeerMacAddress_Type()
)
eoamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerMacAddress.setStatus("current")
_EoamPeerVendorOui_Type = OctetString
_EoamPeerVendorOui_Object = MibTableColumn
eoamPeerVendorOui = _EoamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 15),
    _EoamPeerVendorOui_Type()
)
eoamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerVendorOui.setStatus("current")
_EoamPeerMaxOAMPDU_Type = Unsigned32
_EoamPeerMaxOAMPDU_Object = MibTableColumn
eoamPeerMaxOAMPDU = _EoamPeerMaxOAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 16),
    _EoamPeerMaxOAMPDU_Type()
)
eoamPeerMaxOAMPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerMaxOAMPDU.setStatus("current")


class _EoamPeerUnidirection_Type(Integer32):
    """Custom type eoamPeerUnidirection based on Integer32"""
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


_EoamPeerUnidirection_Type.__name__ = "Integer32"
_EoamPeerUnidirection_Object = MibTableColumn
eoamPeerUnidirection = _EoamPeerUnidirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 17),
    _EoamPeerUnidirection_Type()
)
eoamPeerUnidirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerUnidirection.setStatus("current")


class _EoamPeerLinkMonitoring_Type(Integer32):
    """Custom type eoamPeerLinkMonitoring based on Integer32"""
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


_EoamPeerLinkMonitoring_Type.__name__ = "Integer32"
_EoamPeerLinkMonitoring_Object = MibTableColumn
eoamPeerLinkMonitoring = _EoamPeerLinkMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 18),
    _EoamPeerLinkMonitoring_Type()
)
eoamPeerLinkMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerLinkMonitoring.setStatus("current")


class _EoamPeerVarReq_Type(Integer32):
    """Custom type eoamPeerVarReq based on Integer32"""
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


_EoamPeerVarReq_Type.__name__ = "Integer32"
_EoamPeerVarReq_Object = MibTableColumn
eoamPeerVarReq = _EoamPeerVarReq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 19),
    _EoamPeerVarReq_Type()
)
eoamPeerVarReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerVarReq.setStatus("current")
_EoamPeerPDURev_Type = Unsigned32
_EoamPeerPDURev_Object = MibTableColumn
eoamPeerPDURev = _EoamPeerPDURev_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 1, 2, 1, 20),
    _EoamPeerPDURev_Type()
)
eoamPeerPDURev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamPeerPDURev.setStatus("current")
_SysEoamLinkMonitor_ObjectIdentity = ObjectIdentity
sysEoamLinkMonitor = _SysEoamLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2)
)
_EoamLinkMonitorTable_Object = MibTable
eoamLinkMonitorTable = _EoamLinkMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1)
)
if mibBuilder.loadTexts:
    eoamLinkMonitorTable.setStatus("current")
_EoamLinkMonitorEntry_Object = MibTableRow
eoamLinkMonitorEntry = _EoamLinkMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1)
)
eoamLinkMonitorEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "eoamLinkMonitorIfIndex"),
)
if mibBuilder.loadTexts:
    eoamLinkMonitorEntry.setStatus("current")
_EoamLinkMonitorIfIndex_Type = InterfaceIndex
_EoamLinkMonitorIfIndex_Object = MibTableColumn
eoamLinkMonitorIfIndex = _EoamLinkMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 1),
    _EoamLinkMonitorIfIndex_Type()
)
eoamLinkMonitorIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLinkMonitorIfIndex.setStatus("current")


class _ErrorSymbolNotifyState_Type(Integer32):
    """Custom type errorSymbolNotifyState based on Integer32"""
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


_ErrorSymbolNotifyState_Type.__name__ = "Integer32"
_ErrorSymbolNotifyState_Object = MibTableColumn
errorSymbolNotifyState = _ErrorSymbolNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 2),
    _ErrorSymbolNotifyState_Type()
)
errorSymbolNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorSymbolNotifyState.setStatus("current")
_ErrorSymbolThreshold_Type = Unsigned32
_ErrorSymbolThreshold_Object = MibTableColumn
errorSymbolThreshold = _ErrorSymbolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 3),
    _ErrorSymbolThreshold_Type()
)
errorSymbolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorSymbolThreshold.setStatus("current")


class _ErrorSymbolWindow_Type(Unsigned32):
    """Custom type errorSymbolWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 60000),
    )


_ErrorSymbolWindow_Type.__name__ = "Unsigned32"
_ErrorSymbolWindow_Object = MibTableColumn
errorSymbolWindow = _ErrorSymbolWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 4),
    _ErrorSymbolWindow_Type()
)
errorSymbolWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorSymbolWindow.setStatus("current")


class _ErrorFrameNotifyState_Type(Integer32):
    """Custom type errorFrameNotifyState based on Integer32"""
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


_ErrorFrameNotifyState_Type.__name__ = "Integer32"
_ErrorFrameNotifyState_Object = MibTableColumn
errorFrameNotifyState = _ErrorFrameNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 5),
    _ErrorFrameNotifyState_Type()
)
errorFrameNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameNotifyState.setStatus("current")
_ErrorFrameThreshold_Type = Unsigned32
_ErrorFrameThreshold_Object = MibTableColumn
errorFrameThreshold = _ErrorFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 6),
    _ErrorFrameThreshold_Type()
)
errorFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameThreshold.setStatus("current")


class _ErrorFrameWindow_Type(Unsigned32):
    """Custom type errorFrameWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 60000),
    )


_ErrorFrameWindow_Type.__name__ = "Unsigned32"
_ErrorFrameWindow_Object = MibTableColumn
errorFrameWindow = _ErrorFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 7),
    _ErrorFrameWindow_Type()
)
errorFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameWindow.setStatus("current")


class _ErrorFrameSecondsNotifyState_Type(Integer32):
    """Custom type errorFrameSecondsNotifyState based on Integer32"""
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


_ErrorFrameSecondsNotifyState_Type.__name__ = "Integer32"
_ErrorFrameSecondsNotifyState_Object = MibTableColumn
errorFrameSecondsNotifyState = _ErrorFrameSecondsNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 8),
    _ErrorFrameSecondsNotifyState_Type()
)
errorFrameSecondsNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameSecondsNotifyState.setStatus("current")
_ErrorFrameSecondsThreshold_Type = Integer32
_ErrorFrameSecondsThreshold_Object = MibTableColumn
errorFrameSecondsThreshold = _ErrorFrameSecondsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 9),
    _ErrorFrameSecondsThreshold_Type()
)
errorFrameSecondsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameSecondsThreshold.setStatus("current")


class _ErrorFrameSecondsWindow_Type(Integer32):
    """Custom type errorFrameSecondsWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 900000),
    )


_ErrorFrameSecondsWindow_Type.__name__ = "Integer32"
_ErrorFrameSecondsWindow_Object = MibTableColumn
errorFrameSecondsWindow = _ErrorFrameSecondsWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 10),
    _ErrorFrameSecondsWindow_Type()
)
errorFrameSecondsWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameSecondsWindow.setStatus("current")


class _ErrorFramePeriodNotifyState_Type(Integer32):
    """Custom type errorFramePeriodNotifyState based on Integer32"""
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


_ErrorFramePeriodNotifyState_Type.__name__ = "Integer32"
_ErrorFramePeriodNotifyState_Object = MibTableColumn
errorFramePeriodNotifyState = _ErrorFramePeriodNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 11),
    _ErrorFramePeriodNotifyState_Type()
)
errorFramePeriodNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFramePeriodNotifyState.setStatus("current")
_ErrorFramePeriodThreshold_Type = Unsigned32
_ErrorFramePeriodThreshold_Object = MibTableColumn
errorFramePeriodThreshold = _ErrorFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 12),
    _ErrorFramePeriodThreshold_Type()
)
errorFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFramePeriodThreshold.setStatus("current")


class _ErrorFramePeriodWindow_Type(Unsigned32):
    """Custom type errorFramePeriodWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(148810, 100000000),
    )


_ErrorFramePeriodWindow_Type.__name__ = "Unsigned32"
_ErrorFramePeriodWindow_Object = MibTableColumn
errorFramePeriodWindow = _ErrorFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 13),
    _ErrorFramePeriodWindow_Type()
)
errorFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFramePeriodWindow.setStatus("current")


class _EoamCriticalLinkEventState_Type(Integer32):
    """Custom type eoamCriticalLinkEventState based on Integer32"""
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


_EoamCriticalLinkEventState_Type.__name__ = "Integer32"
_EoamCriticalLinkEventState_Object = MibTableColumn
eoamCriticalLinkEventState = _EoamCriticalLinkEventState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 2, 1, 1, 14),
    _EoamCriticalLinkEventState_Type()
)
eoamCriticalLinkEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamCriticalLinkEventState.setStatus("current")
_SysEoamStats_ObjectIdentity = ObjectIdentity
sysEoamStats = _SysEoamStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3)
)
_SysEoamStatsTable_Object = MibTable
sysEoamStatsTable = _SysEoamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1)
)
if mibBuilder.loadTexts:
    sysEoamStatsTable.setStatus("current")
_EoamStatsEntry_Object = MibTableRow
eoamStatsEntry = _EoamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1)
)
eoamStatsEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "eoamInfomationIndex"),
)
if mibBuilder.loadTexts:
    eoamStatsEntry.setStatus("current")
_EoamInfomationIndex_Type = InterfaceIndex
_EoamInfomationIndex_Object = MibTableColumn
eoamInfomationIndex = _EoamInfomationIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 1),
    _EoamInfomationIndex_Type()
)
eoamInfomationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamInfomationIndex.setStatus("current")
_EoamInformationTx_Type = Counter32
_EoamInformationTx_Object = MibTableColumn
eoamInformationTx = _EoamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 2),
    _EoamInformationTx_Type()
)
eoamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamInformationTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamInformationTx.setUnits("frames")
_EoamInformationRx_Type = Counter32
_EoamInformationRx_Object = MibTableColumn
eoamInformationRx = _EoamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 3),
    _EoamInformationRx_Type()
)
eoamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamInformationRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamInformationRx.setUnits("frames")
_EoamUniqueEventNotificationTx_Type = Counter32
_EoamUniqueEventNotificationTx_Object = MibTableColumn
eoamUniqueEventNotificationTx = _EoamUniqueEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 4),
    _EoamUniqueEventNotificationTx_Type()
)
eoamUniqueEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamUniqueEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamUniqueEventNotificationTx.setUnits("frames")
_EoamUniqueEventNotificationRx_Type = Counter32
_EoamUniqueEventNotificationRx_Object = MibTableColumn
eoamUniqueEventNotificationRx = _EoamUniqueEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 5),
    _EoamUniqueEventNotificationRx_Type()
)
eoamUniqueEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamUniqueEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamUniqueEventNotificationRx.setUnits("frames")
_EoamDuplicateEventNotificationTx_Type = Counter32
_EoamDuplicateEventNotificationTx_Object = MibTableColumn
eoamDuplicateEventNotificationTx = _EoamDuplicateEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 6),
    _EoamDuplicateEventNotificationTx_Type()
)
eoamDuplicateEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamDuplicateEventNotificationTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamDuplicateEventNotificationTx.setUnits("frames")
_EoamDuplicateEventNotificationRx_Type = Counter32
_EoamDuplicateEventNotificationRx_Object = MibTableColumn
eoamDuplicateEventNotificationRx = _EoamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 7),
    _EoamDuplicateEventNotificationRx_Type()
)
eoamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamDuplicateEventNotificationRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamDuplicateEventNotificationRx.setUnits("frames")
_EoamLoopbackControlTx_Type = Counter32
_EoamLoopbackControlTx_Object = MibTableColumn
eoamLoopbackControlTx = _EoamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 8),
    _EoamLoopbackControlTx_Type()
)
eoamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackControlTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamLoopbackControlTx.setUnits("frames")
_EoamLoopbackControlRx_Type = Counter32
_EoamLoopbackControlRx_Object = MibTableColumn
eoamLoopbackControlRx = _EoamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 9),
    _EoamLoopbackControlRx_Type()
)
eoamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackControlRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamLoopbackControlRx.setUnits("frames")
_EoamVariableRequestTx_Type = Counter32
_EoamVariableRequestTx_Object = MibTableColumn
eoamVariableRequestTx = _EoamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 10),
    _EoamVariableRequestTx_Type()
)
eoamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamVariableRequestTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamVariableRequestTx.setUnits("frames")
_EoamVariableRequestRx_Type = Counter32
_EoamVariableRequestRx_Object = MibTableColumn
eoamVariableRequestRx = _EoamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 11),
    _EoamVariableRequestRx_Type()
)
eoamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamVariableRequestRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamVariableRequestRx.setUnits("frames")
_EoamVariableResponseTx_Type = Counter32
_EoamVariableResponseTx_Object = MibTableColumn
eoamVariableResponseTx = _EoamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 12),
    _EoamVariableResponseTx_Type()
)
eoamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamVariableResponseTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamVariableResponseTx.setUnits("frames")
_EoamVariableResponseRx_Type = Counter32
_EoamVariableResponseRx_Object = MibTableColumn
eoamVariableResponseRx = _EoamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 13),
    _EoamVariableResponseRx_Type()
)
eoamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamVariableResponseRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamVariableResponseRx.setUnits("frames")
_EoamOrgSpecificTx_Type = Counter32
_EoamOrgSpecificTx_Object = MibTableColumn
eoamOrgSpecificTx = _EoamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 14),
    _EoamOrgSpecificTx_Type()
)
eoamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamOrgSpecificTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamOrgSpecificTx.setUnits("frames")
_EoamOrgSpecificRx_Type = Counter32
_EoamOrgSpecificRx_Object = MibTableColumn
eoamOrgSpecificRx = _EoamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 15),
    _EoamOrgSpecificRx_Type()
)
eoamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamOrgSpecificRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamOrgSpecificRx.setUnits("frames")
_EoamUnsupportedCodesTx_Type = Counter32
_EoamUnsupportedCodesTx_Object = MibTableColumn
eoamUnsupportedCodesTx = _EoamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 16),
    _EoamUnsupportedCodesTx_Type()
)
eoamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamUnsupportedCodesTx.setStatus("current")
if mibBuilder.loadTexts:
    eoamUnsupportedCodesTx.setUnits("frames")
_EoamUnsupportedCodesRx_Type = Counter32
_EoamUnsupportedCodesRx_Object = MibTableColumn
eoamUnsupportedCodesRx = _EoamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 17),
    _EoamUnsupportedCodesRx_Type()
)
eoamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamUnsupportedCodesRx.setStatus("current")
if mibBuilder.loadTexts:
    eoamUnsupportedCodesRx.setUnits("frames")
_EoamFramesLostDueToOam_Type = Counter32
_EoamFramesLostDueToOam_Object = MibTableColumn
eoamFramesLostDueToOam = _EoamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 1, 1, 18),
    _EoamFramesLostDueToOam_Type()
)
eoamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamFramesLostDueToOam.setStatus("current")
if mibBuilder.loadTexts:
    eoamFramesLostDueToOam.setUnits("frames")
_SysEoamStatsClearPortlist_Type = PortList
_SysEoamStatsClearPortlist_Object = MibScalar
sysEoamStatsClearPortlist = _SysEoamStatsClearPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 3, 2),
    _SysEoamStatsClearPortlist_Type()
)
sysEoamStatsClearPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEoamStatsClearPortlist.setStatus("current")
_SysEoamEventLog_ObjectIdentity = ObjectIdentity
sysEoamEventLog = _SysEoamEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4)
)
_SysOamEventLogTable_Object = MibTable
sysOamEventLogTable = _SysOamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2)
)
if mibBuilder.loadTexts:
    sysOamEventLogTable.setStatus("current")
_EoamEventLogEntry_Object = MibTableRow
eoamEventLogEntry = _EoamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1)
)
eoamEventLogEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "eoamEventLogPort"),
    (0, "DGS-1100-10ME_A1", "eoamEventLogIndex"),
)
if mibBuilder.loadTexts:
    eoamEventLogEntry.setStatus("current")
_EoamEventLogPort_Type = InterfaceIndex
_EoamEventLogPort_Object = MibTableColumn
eoamEventLogPort = _EoamEventLogPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 1),
    _EoamEventLogPort_Type()
)
eoamEventLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogPort.setStatus("current")


class _EoamEventLogIndex_Type(Unsigned32):
    """Custom type eoamEventLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EoamEventLogIndex_Type.__name__ = "Unsigned32"
_EoamEventLogIndex_Object = MibTableColumn
eoamEventLogIndex = _EoamEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 2),
    _EoamEventLogIndex_Type()
)
eoamEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogIndex.setStatus("current")
_EoamEventLogTimestamp_Type = DisplayString
_EoamEventLogTimestamp_Object = MibTableColumn
eoamEventLogTimestamp = _EoamEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 3),
    _EoamEventLogTimestamp_Type()
)
eoamEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogTimestamp.setStatus("current")
_EoamEventLogType_Type = Unsigned32
_EoamEventLogType_Object = MibTableColumn
eoamEventLogType = _EoamEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 4),
    _EoamEventLogType_Type()
)
eoamEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogType.setStatus("current")


class _EoamEventLogLocation_Type(Integer32):
    """Custom type eoamEventLogLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_EoamEventLogLocation_Type.__name__ = "Integer32"
_EoamEventLogLocation_Object = MibTableColumn
eoamEventLogLocation = _EoamEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 5),
    _EoamEventLogLocation_Type()
)
eoamEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogLocation.setStatus("current")
_EoamEventLogValue_Type = Unsigned32
_EoamEventLogValue_Object = MibTableColumn
eoamEventLogValue = _EoamEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 6),
    _EoamEventLogValue_Type()
)
eoamEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogValue.setStatus("current")
_EoamEventLogWindow_Type = Unsigned32
_EoamEventLogWindow_Object = MibTableColumn
eoamEventLogWindow = _EoamEventLogWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 7),
    _EoamEventLogWindow_Type()
)
eoamEventLogWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogWindow.setStatus("current")
_EoamEventLogThreshold_Type = Unsigned32
_EoamEventLogThreshold_Object = MibTableColumn
eoamEventLogThreshold = _EoamEventLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 8),
    _EoamEventLogThreshold_Type()
)
eoamEventLogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogThreshold.setStatus("current")
_EoamEventLogAccError_Type = Unsigned32
_EoamEventLogAccError_Object = MibTableColumn
eoamEventLogAccError = _EoamEventLogAccError_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 2, 1, 9),
    _EoamEventLogAccError_Type()
)
eoamEventLogAccError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamEventLogAccError.setStatus("current")
_SysEoamEventLogClearPortlist_Type = PortList
_SysEoamEventLogClearPortlist_Object = MibScalar
sysEoamEventLogClearPortlist = _SysEoamEventLogClearPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 4, 3),
    _SysEoamEventLogClearPortlist_Type()
)
sysEoamEventLogClearPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEoamEventLogClearPortlist.setStatus("current")
_SysEoamTrap_ObjectIdentity = ObjectIdentity
sysEoamTrap = _SysEoamTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 5)
)
_EoamTrap_ObjectIdentity = ObjectIdentity
eoamTrap = _EoamTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 5, 0)
)
_SysEoamLoopbackTest_ObjectIdentity = ObjectIdentity
sysEoamLoopbackTest = _SysEoamLoopbackTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6)
)
_EoamLoopbackTestTable_Object = MibTable
eoamLoopbackTestTable = _EoamLoopbackTestTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1)
)
if mibBuilder.loadTexts:
    eoamLoopbackTestTable.setStatus("current")
_EoamLoopbackTestEntry_Object = MibTableRow
eoamLoopbackTestEntry = _EoamLoopbackTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1)
)
eoamLoopbackTestEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "eoamLoopbackTestIndex"),
)
if mibBuilder.loadTexts:
    eoamLoopbackTestEntry.setStatus("current")
_EoamLoopbackTestIndex_Type = InterfaceIndex
_EoamLoopbackTestIndex_Object = MibTableColumn
eoamLoopbackTestIndex = _EoamLoopbackTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 1),
    _EoamLoopbackTestIndex_Type()
)
eoamLoopbackTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackTestIndex.setStatus("current")


class _EoamLoopbackStatus_Type(Integer32):
    """Custom type eoamLoopbackStatus based on Integer32"""
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
        *(("noLoopback", 1),
          ("remoteLoopback", 2),
          ("unknown", 3))
    )


_EoamLoopbackStatus_Type.__name__ = "Integer32"
_EoamLoopbackStatus_Object = MibTableColumn
eoamLoopbackStatus = _EoamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 2),
    _EoamLoopbackStatus_Type()
)
eoamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackStatus.setStatus("current")


class _EoamLoopbackTestPattern_Type(OctetString):
    """Custom type eoamLoopbackTestPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EoamLoopbackTestPattern_Type.__name__ = "OctetString"
_EoamLoopbackTestPattern_Object = MibTableColumn
eoamLoopbackTestPattern = _EoamLoopbackTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 3),
    _EoamLoopbackTestPattern_Type()
)
eoamLoopbackTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamLoopbackTestPattern.setStatus("current")


class _EoamLoopbackTestPktSize_Type(Unsigned32):
    """Custom type eoamLoopbackTestPktSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_EoamLoopbackTestPktSize_Type.__name__ = "Unsigned32"
_EoamLoopbackTestPktSize_Object = MibTableColumn
eoamLoopbackTestPktSize = _EoamLoopbackTestPktSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 4),
    _EoamLoopbackTestPktSize_Type()
)
eoamLoopbackTestPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamLoopbackTestPktSize.setStatus("current")


class _EoamLoopbackTestCount_Type(Unsigned32):
    """Custom type eoamLoopbackTestCount based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EoamLoopbackTestCount_Type.__name__ = "Unsigned32"
_EoamLoopbackTestCount_Object = MibTableColumn
eoamLoopbackTestCount = _EoamLoopbackTestCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 5),
    _EoamLoopbackTestCount_Type()
)
eoamLoopbackTestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamLoopbackTestCount.setStatus("current")


class _EoamLoopbackTestWaitTime_Type(Integer32):
    """Custom type eoamLoopbackTestWaitTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EoamLoopbackTestWaitTime_Type.__name__ = "Integer32"
_EoamLoopbackTestWaitTime_Object = MibTableColumn
eoamLoopbackTestWaitTime = _EoamLoopbackTestWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 6),
    _EoamLoopbackTestWaitTime_Type()
)
eoamLoopbackTestWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamLoopbackTestWaitTime.setStatus("current")


class _EoamLoopbackTestCommand_Type(Integer32):
    """Custom type eoamLoopbackTestCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLoopbackTest", 1),
          ("startLoopbackTest", 2))
    )


_EoamLoopbackTestCommand_Type.__name__ = "Integer32"
_EoamLoopbackTestCommand_Object = MibTableColumn
eoamLoopbackTestCommand = _EoamLoopbackTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 7),
    _EoamLoopbackTestCommand_Type()
)
eoamLoopbackTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamLoopbackTestCommand.setStatus("current")


class _EoamLoopbackTestStatus_Type(Integer32):
    """Custom type eoamLoopbackTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopbackTestCompleted", 3),
          ("loopbackTestInprogress", 2),
          ("notInitiated", 1))
    )


_EoamLoopbackTestStatus_Type.__name__ = "Integer32"
_EoamLoopbackTestStatus_Object = MibTableColumn
eoamLoopbackTestStatus = _EoamLoopbackTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 8),
    _EoamLoopbackTestStatus_Type()
)
eoamLoopbackTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackTestStatus.setStatus("current")


class _EoamLoopbackTestStartTimestamp_Type(DisplayString):
    """Custom type eoamLoopbackTestStartTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_EoamLoopbackTestStartTimestamp_Type.__name__ = "DisplayString"
_EoamLoopbackTestStartTimestamp_Object = MibTableColumn
eoamLoopbackTestStartTimestamp = _EoamLoopbackTestStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 9),
    _EoamLoopbackTestStartTimestamp_Type()
)
eoamLoopbackTestStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackTestStartTimestamp.setStatus("current")


class _EoamLoopbackTestEndTimestamp_Type(DisplayString):
    """Custom type eoamLoopbackTestEndTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_EoamLoopbackTestEndTimestamp_Type.__name__ = "DisplayString"
_EoamLoopbackTestEndTimestamp_Object = MibTableColumn
eoamLoopbackTestEndTimestamp = _EoamLoopbackTestEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 10),
    _EoamLoopbackTestEndTimestamp_Type()
)
eoamLoopbackTestEndTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackTestEndTimestamp.setStatus("current")
_EoamLoopbackTestTxCount_Type = Unsigned32
_EoamLoopbackTestTxCount_Object = MibTableColumn
eoamLoopbackTestTxCount = _EoamLoopbackTestTxCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 11),
    _EoamLoopbackTestTxCount_Type()
)
eoamLoopbackTestTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackTestTxCount.setStatus("current")
_EoamLoopbackTestRxCount_Type = Unsigned32
_EoamLoopbackTestRxCount_Object = MibTableColumn
eoamLoopbackTestRxCount = _EoamLoopbackTestRxCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 12),
    _EoamLoopbackTestRxCount_Type()
)
eoamLoopbackTestRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackTestRxCount.setStatus("current")
_EoamLoopbackTestMatchCount_Type = Unsigned32
_EoamLoopbackTestMatchCount_Object = MibTableColumn
eoamLoopbackTestMatchCount = _EoamLoopbackTestMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 1, 1, 13),
    _EoamLoopbackTestMatchCount_Type()
)
eoamLoopbackTestMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackTestMatchCount.setStatus("current")
_EoamLoopbackStatsTable_Object = MibTable
eoamLoopbackStatsTable = _EoamLoopbackStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2)
)
if mibBuilder.loadTexts:
    eoamLoopbackStatsTable.setStatus("current")
_EoamLoopbackStatsEntry_Object = MibTableRow
eoamLoopbackStatsEntry = _EoamLoopbackStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2, 1)
)
eoamLoopbackStatsEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "eoamLoopbackStatsIndex"),
)
if mibBuilder.loadTexts:
    eoamLoopbackStatsEntry.setStatus("current")
_EoamLoopbackStatsIndex_Type = InterfaceIndex
_EoamLoopbackStatsIndex_Object = MibTableColumn
eoamLoopbackStatsIndex = _EoamLoopbackStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2, 1, 1),
    _EoamLoopbackStatsIndex_Type()
)
eoamLoopbackStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackStatsIndex.setStatus("current")


class _EoamLoopbackStatsStartTimestamp_Type(DisplayString):
    """Custom type eoamLoopbackStatsStartTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_EoamLoopbackStatsStartTimestamp_Type.__name__ = "DisplayString"
_EoamLoopbackStatsStartTimestamp_Object = MibTableColumn
eoamLoopbackStatsStartTimestamp = _EoamLoopbackStatsStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2, 1, 2),
    _EoamLoopbackStatsStartTimestamp_Type()
)
eoamLoopbackStatsStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackStatsStartTimestamp.setStatus("current")


class _EoamLoopbackStatsEndTimestamp_Type(DisplayString):
    """Custom type eoamLoopbackStatsEndTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_EoamLoopbackStatsEndTimestamp_Type.__name__ = "DisplayString"
_EoamLoopbackStatsEndTimestamp_Object = MibTableColumn
eoamLoopbackStatsEndTimestamp = _EoamLoopbackStatsEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2, 1, 3),
    _EoamLoopbackStatsEndTimestamp_Type()
)
eoamLoopbackStatsEndTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackStatsEndTimestamp.setStatus("current")
_EoamLoopbackStatsTxCount_Type = Unsigned32
_EoamLoopbackStatsTxCount_Object = MibTableColumn
eoamLoopbackStatsTxCount = _EoamLoopbackStatsTxCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2, 1, 4),
    _EoamLoopbackStatsTxCount_Type()
)
eoamLoopbackStatsTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackStatsTxCount.setStatus("current")
_EoamLoopbackStatsRxCount_Type = Unsigned32
_EoamLoopbackStatsRxCount_Object = MibTableColumn
eoamLoopbackStatsRxCount = _EoamLoopbackStatsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2, 1, 5),
    _EoamLoopbackStatsRxCount_Type()
)
eoamLoopbackStatsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackStatsRxCount.setStatus("current")
_EoamLoopbackStatsMatchCount_Type = Unsigned32
_EoamLoopbackStatsMatchCount_Object = MibTableColumn
eoamLoopbackStatsMatchCount = _EoamLoopbackStatsMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 6, 2, 1, 6),
    _EoamLoopbackStatsMatchCount_Type()
)
eoamLoopbackStatsMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoamLoopbackStatsMatchCount.setStatus("current")
_CompanyDuld_ObjectIdentity = ObjectIdentity
companyDuld = _CompanyDuld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52)
)
_SysDuld_ObjectIdentity = ObjectIdentity
sysDuld = _SysDuld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1)
)
_DuldTable_Object = MibTable
duldTable = _DuldTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1)
)
if mibBuilder.loadTexts:
    duldTable.setStatus("current")
_DuldEntry_Object = MibTableRow
duldEntry = _DuldEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1, 1)
)
duldEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "duldIfIndex"),
)
if mibBuilder.loadTexts:
    duldEntry.setStatus("current")
_DuldIfIndex_Type = InterfaceIndex
_DuldIfIndex_Object = MibTableColumn
duldIfIndex = _DuldIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1, 1, 1),
    _DuldIfIndex_Type()
)
duldIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duldIfIndex.setStatus("current")


class _DuldState_Type(Integer32):
    """Custom type duldState based on Integer32"""
    defaultValue = 2

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


_DuldState_Type.__name__ = "Integer32"
_DuldState_Object = MibTableColumn
duldState = _DuldState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1, 1, 2),
    _DuldState_Type()
)
duldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duldState.setStatus("current")


class _DuldOperState_Type(Integer32):
    """Custom type duldOperState based on Integer32"""
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


_DuldOperState_Type.__name__ = "Integer32"
_DuldOperState_Object = MibTableColumn
duldOperState = _DuldOperState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1, 1, 3),
    _DuldOperState_Type()
)
duldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duldOperState.setStatus("current")


class _DuldMode_Type(Integer32):
    """Custom type duldMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("shutdown", 1))
    )


_DuldMode_Type.__name__ = "Integer32"
_DuldMode_Object = MibTableColumn
duldMode = _DuldMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1, 1, 4),
    _DuldMode_Type()
)
duldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duldMode.setStatus("current")


class _DuldLinkStatus_Type(Integer32):
    """Custom type duldLinkStatus based on Integer32"""
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
        *(("bidirectional", 2),
          ("linkDown", 5),
          ("rxFault", 4),
          ("txFault", 3),
          ("unknown", 1))
    )


_DuldLinkStatus_Type.__name__ = "Integer32"
_DuldLinkStatus_Object = MibTableColumn
duldLinkStatus = _DuldLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1, 1, 5),
    _DuldLinkStatus_Type()
)
duldLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duldLinkStatus.setStatus("current")


class _DuldDiscoveryTime_Type(Unsigned32):
    """Custom type duldDiscoveryTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_DuldDiscoveryTime_Type.__name__ = "Unsigned32"
_DuldDiscoveryTime_Object = MibTableColumn
duldDiscoveryTime = _DuldDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 52, 1, 1, 1, 6),
    _DuldDiscoveryTime_Type()
)
duldDiscoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duldDiscoveryTime.setStatus("current")
_CompanyEee_ObjectIdentity = ObjectIdentity
companyEee = _CompanyEee_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 60)
)
_SysEee_ObjectIdentity = ObjectIdentity
sysEee = _SysEee_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 60, 1)
)
_EeeTable_Object = MibTable
eeeTable = _EeeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 60, 1, 1)
)
if mibBuilder.loadTexts:
    eeeTable.setStatus("current")
_EeeEntry_Object = MibTableRow
eeeEntry = _EeeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 60, 1, 1, 1)
)
eeeEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "eeePort"),
)
if mibBuilder.loadTexts:
    eeeEntry.setStatus("current")
_EeePort_Type = Integer32
_EeePort_Object = MibTableColumn
eeePort = _EeePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 60, 1, 1, 1, 1),
    _EeePort_Type()
)
eeePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eeePort.setStatus("current")


class _Eeestatus_Type(Integer32):
    """Custom type eeestatus based on Integer32"""
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


_Eeestatus_Type.__name__ = "Integer32"
_Eeestatus_Object = MibTableColumn
eeestatus = _Eeestatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 60, 1, 1, 1, 2),
    _Eeestatus_Type()
)
eeestatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eeestatus.setStatus("current")
_CompanyDHCPv6Relay_ObjectIdentity = ObjectIdentity
companyDHCPv6Relay = _CompanyDHCPv6Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86)
)
_SysDHCPv6RelayControl_ObjectIdentity = ObjectIdentity
sysDHCPv6RelayControl = _SysDHCPv6RelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 1)
)


class _Dhcpv6RelayState_Type(Integer32):
    """Custom type dhcpv6RelayState based on Integer32"""
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


_Dhcpv6RelayState_Type.__name__ = "Integer32"
_Dhcpv6RelayState_Object = MibScalar
dhcpv6RelayState = _Dhcpv6RelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 1, 1),
    _Dhcpv6RelayState_Type()
)
dhcpv6RelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayState.setStatus("current")


class _Dhcpv6RelayHopCount_Type(Integer32):
    """Custom type dhcpv6RelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Dhcpv6RelayHopCount_Type.__name__ = "Integer32"
_Dhcpv6RelayHopCount_Object = MibScalar
dhcpv6RelayHopCount = _Dhcpv6RelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 1, 2),
    _Dhcpv6RelayHopCount_Type()
)
dhcpv6RelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayHopCount.setStatus("current")
_SysDHCPv6RelayManagement_ObjectIdentity = ObjectIdentity
sysDHCPv6RelayManagement = _SysDHCPv6RelayManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 2)
)
_Dhcpv6RelayInterfaceTable_Object = MibTable
dhcpv6RelayInterfaceTable = _Dhcpv6RelayInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpv6RelayInterfaceTable.setStatus("current")
_Dhcpv6RelayInterfaceEntry_Object = MibTableRow
dhcpv6RelayInterfaceEntry = _Dhcpv6RelayInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 2, 1, 1)
)
dhcpv6RelayInterfaceEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "dhcpv6RelayServerIP"),
)
if mibBuilder.loadTexts:
    dhcpv6RelayInterfaceEntry.setStatus("current")
_Dhcpv6RelayServerIP_Type = Ipv6Address
_Dhcpv6RelayServerIP_Object = MibTableColumn
dhcpv6RelayServerIP = _Dhcpv6RelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 2, 1, 1, 1),
    _Dhcpv6RelayServerIP_Type()
)
dhcpv6RelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6RelayServerIP.setStatus("current")
_Dhcpv6RelayInterface_Type = DisplayString
_Dhcpv6RelayInterface_Object = MibTableColumn
dhcpv6RelayInterface = _Dhcpv6RelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 2, 1, 1, 2),
    _Dhcpv6RelayInterface_Type()
)
dhcpv6RelayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6RelayInterface.setStatus("current")
_Dhcpv6RelayRowStatus_Type = RowStatus
_Dhcpv6RelayRowStatus_Object = MibTableColumn
dhcpv6RelayRowStatus = _Dhcpv6RelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 2, 1, 1, 3),
    _Dhcpv6RelayRowStatus_Type()
)
dhcpv6RelayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayRowStatus.setStatus("current")
_SysDHCPv6RelayOption37_ObjectIdentity = ObjectIdentity
sysDHCPv6RelayOption37 = _SysDHCPv6RelayOption37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 3)
)


class _Dhcpv6RelayOption37State_Type(Integer32):
    """Custom type dhcpv6RelayOption37State based on Integer32"""
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


_Dhcpv6RelayOption37State_Type.__name__ = "Integer32"
_Dhcpv6RelayOption37State_Object = MibScalar
dhcpv6RelayOption37State = _Dhcpv6RelayOption37State_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 3, 1),
    _Dhcpv6RelayOption37State_Type()
)
dhcpv6RelayOption37State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37State.setStatus("current")


class _Dhcpv6RelayOption37CheckState_Type(Integer32):
    """Custom type dhcpv6RelayOption37CheckState based on Integer32"""
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


_Dhcpv6RelayOption37CheckState_Type.__name__ = "Integer32"
_Dhcpv6RelayOption37CheckState_Object = MibScalar
dhcpv6RelayOption37CheckState = _Dhcpv6RelayOption37CheckState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 3, 2),
    _Dhcpv6RelayOption37CheckState_Type()
)
dhcpv6RelayOption37CheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37CheckState.setStatus("current")


class _Dhcpv6RelayOption37RemoteIDType_Type(Integer32):
    """Custom type dhcpv6RelayOption37RemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cid_with_user_define", 1),
          ("default", 0),
          ("user_define", 2))
    )


_Dhcpv6RelayOption37RemoteIDType_Type.__name__ = "Integer32"
_Dhcpv6RelayOption37RemoteIDType_Object = MibScalar
dhcpv6RelayOption37RemoteIDType = _Dhcpv6RelayOption37RemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 3, 3),
    _Dhcpv6RelayOption37RemoteIDType_Type()
)
dhcpv6RelayOption37RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37RemoteIDType.setStatus("current")
_Dhcpv6RelayOption37RemoteID_Type = DisplayString
_Dhcpv6RelayOption37RemoteID_Object = MibScalar
dhcpv6RelayOption37RemoteID = _Dhcpv6RelayOption37RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 86, 3, 4),
    _Dhcpv6RelayOption37RemoteID_Type()
)
dhcpv6RelayOption37RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37RemoteID.setStatus("current")
_CompanyMldsGroup_ObjectIdentity = ObjectIdentity
companyMldsGroup = _CompanyMldsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88)
)
_SysMldsSystem_ObjectIdentity = ObjectIdentity
sysMldsSystem = _SysMldsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 1)
)


class _MldsStatus_Type(Integer32):
    """Custom type mldsStatus based on Integer32"""
    defaultValue = 2

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


_MldsStatus_Type.__name__ = "Integer32"
_MldsStatus_Object = MibScalar
mldsStatus = _MldsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 1, 1),
    _MldsStatus_Type()
)
mldsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsStatus.setStatus("current")
_SysMldsVlan_ObjectIdentity = ObjectIdentity
sysMldsVlan = _SysMldsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3)
)
_MldsVlanRouterTable_Object = MibTable
mldsVlanRouterTable = _MldsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 3)
)
if mibBuilder.loadTexts:
    mldsVlanRouterTable.setStatus("current")
_MldsVlanRouterEntry_Object = MibTableRow
mldsVlanRouterEntry = _MldsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 3, 1)
)
mldsVlanRouterEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "mldsVlanRouterVlanId"),
)
if mibBuilder.loadTexts:
    mldsVlanRouterEntry.setStatus("current")


class _MldsVlanRouterVlanId_Type(Integer32):
    """Custom type mldsVlanRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldsVlanRouterVlanId_Type.__name__ = "Integer32"
_MldsVlanRouterVlanId_Object = MibTableColumn
mldsVlanRouterVlanId = _MldsVlanRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 3, 1, 1),
    _MldsVlanRouterVlanId_Type()
)
mldsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanRouterVlanId.setStatus("current")
_MldsVlanRouterStaticPortList_Type = PortList
_MldsVlanRouterStaticPortList_Object = MibTableColumn
mldsVlanRouterStaticPortList = _MldsVlanRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 3, 1, 2),
    _MldsVlanRouterStaticPortList_Type()
)
mldsVlanRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanRouterStaticPortList.setStatus("current")
_MldsVlanRouterDynamicPortList_Type = PortList
_MldsVlanRouterDynamicPortList_Object = MibTableColumn
mldsVlanRouterDynamicPortList = _MldsVlanRouterDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 3, 1, 3),
    _MldsVlanRouterDynamicPortList_Type()
)
mldsVlanRouterDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanRouterDynamicPortList.setStatus("current")
_MldsVlanFilterTable_Object = MibTable
mldsVlanFilterTable = _MldsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4)
)
if mibBuilder.loadTexts:
    mldsVlanFilterTable.setStatus("current")
_MldsVlanFilterEntry_Object = MibTableRow
mldsVlanFilterEntry = _MldsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1)
)
mldsVlanFilterEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "mldsVlanFilterVlanId"),
)
if mibBuilder.loadTexts:
    mldsVlanFilterEntry.setStatus("current")


class _MldsVlanFilterVlanId_Type(Integer32):
    """Custom type mldsVlanFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldsVlanFilterVlanId_Type.__name__ = "Integer32"
_MldsVlanFilterVlanId_Object = MibTableColumn
mldsVlanFilterVlanId = _MldsVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 1),
    _MldsVlanFilterVlanId_Type()
)
mldsVlanFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanFilterVlanId.setStatus("current")


class _MldsVlanSnoopStatus_Type(Integer32):
    """Custom type mldsVlanSnoopStatus based on Integer32"""
    defaultValue = 1

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


_MldsVlanSnoopStatus_Type.__name__ = "Integer32"
_MldsVlanSnoopStatus_Object = MibTableColumn
mldsVlanSnoopStatus = _MldsVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 2),
    _MldsVlanSnoopStatus_Type()
)
mldsVlanSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanSnoopStatus.setStatus("current")


class _MldsVlanQuerier_Type(Integer32):
    """Custom type mldsVlanQuerier based on Integer32"""
    defaultValue = 2

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


_MldsVlanQuerier_Type.__name__ = "Integer32"
_MldsVlanQuerier_Object = MibTableColumn
mldsVlanQuerier = _MldsVlanQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 3),
    _MldsVlanQuerier_Type()
)
mldsVlanQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanQuerier.setStatus("current")


class _MldsVlanCfgQuerier_Type(Integer32):
    """Custom type mldsVlanCfgQuerier based on Integer32"""
    defaultValue = 2

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


_MldsVlanCfgQuerier_Type.__name__ = "Integer32"
_MldsVlanCfgQuerier_Object = MibTableColumn
mldsVlanCfgQuerier = _MldsVlanCfgQuerier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 4),
    _MldsVlanCfgQuerier_Type()
)
mldsVlanCfgQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanCfgQuerier.setStatus("current")


class _MldsVlanQueryInterval_Type(Integer32):
    """Custom type mldsVlanQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_MldsVlanQueryInterval_Type.__name__ = "Integer32"
_MldsVlanQueryInterval_Object = MibTableColumn
mldsVlanQueryInterval = _MldsVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 5),
    _MldsVlanQueryInterval_Type()
)
mldsVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanQueryInterval.setStatus("current")


class _MldsVlanFastLeave_Type(Integer32):
    """Custom type mldsVlanFastLeave based on Integer32"""
    defaultValue = 2

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


_MldsVlanFastLeave_Type.__name__ = "Integer32"
_MldsVlanFastLeave_Object = MibTableColumn
mldsVlanFastLeave = _MldsVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 6),
    _MldsVlanFastLeave_Type()
)
mldsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanFastLeave.setStatus("current")


class _MldsVlanQuerierVersion_Type(Integer32):
    """Custom type mldsVlanQuerierVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_MldsVlanQuerierVersion_Type.__name__ = "Integer32"
_MldsVlanQuerierVersion_Object = MibTableColumn
mldsVlanQuerierVersion = _MldsVlanQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 7),
    _MldsVlanQuerierVersion_Type()
)
mldsVlanQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanQuerierVersion.setStatus("current")


class _MldsVlanRouterPortPurgeInterval_Type(Integer32):
    """Custom type mldsVlanRouterPortPurgeInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_MldsVlanRouterPortPurgeInterval_Type.__name__ = "Integer32"
_MldsVlanRouterPortPurgeInterval_Object = MibTableColumn
mldsVlanRouterPortPurgeInterval = _MldsVlanRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 8),
    _MldsVlanRouterPortPurgeInterval_Type()
)
mldsVlanRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanRouterPortPurgeInterval.setStatus("current")


class _MldsVlanHostPortPurgeInterval_Type(Integer32):
    """Custom type mldsVlanHostPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 153025),
    )


_MldsVlanHostPortPurgeInterval_Type.__name__ = "Integer32"
_MldsVlanHostPortPurgeInterval_Object = MibTableColumn
mldsVlanHostPortPurgeInterval = _MldsVlanHostPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 9),
    _MldsVlanHostPortPurgeInterval_Type()
)
mldsVlanHostPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanHostPortPurgeInterval.setStatus("current")


class _MldsVlanRobustnessValue_Type(Integer32):
    """Custom type mldsVlanRobustnessValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_MldsVlanRobustnessValue_Type.__name__ = "Integer32"
_MldsVlanRobustnessValue_Object = MibTableColumn
mldsVlanRobustnessValue = _MldsVlanRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 10),
    _MldsVlanRobustnessValue_Type()
)
mldsVlanRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanRobustnessValue.setStatus("current")


class _MldsVlanGrpQueryInterval_Type(Integer32):
    """Custom type mldsVlanGrpQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MldsVlanGrpQueryInterval_Type.__name__ = "Integer32"
_MldsVlanGrpQueryInterval_Object = MibTableColumn
mldsVlanGrpQueryInterval = _MldsVlanGrpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 11),
    _MldsVlanGrpQueryInterval_Type()
)
mldsVlanGrpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanGrpQueryInterval.setStatus("current")


class _MldsVlanQueryMaxResponseTime_Type(Integer32):
    """Custom type mldsVlanQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 25),
    )


_MldsVlanQueryMaxResponseTime_Type.__name__ = "Integer32"
_MldsVlanQueryMaxResponseTime_Object = MibTableColumn
mldsVlanQueryMaxResponseTime = _MldsVlanQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 4, 1, 12),
    _MldsVlanQueryMaxResponseTime_Type()
)
mldsVlanQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanQueryMaxResponseTime.setStatus("current")
_MldsVlanMulticastGroupTable_Object = MibTable
mldsVlanMulticastGroupTable = _MldsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 5)
)
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupTable.setStatus("current")
_MldsVlanMulticastGroupEntry_Object = MibTableRow
mldsVlanMulticastGroupEntry = _MldsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 5, 1)
)
mldsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "mldsVlanMulticastGroupVlanId"),
    (0, "DGS-1100-10ME_A1", "mldsVlanMulticastGroupIpAddress"),
)
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupEntry.setStatus("current")


class _MldsVlanMulticastGroupVlanId_Type(Integer32):
    """Custom type mldsVlanMulticastGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldsVlanMulticastGroupVlanId_Type.__name__ = "Integer32"
_MldsVlanMulticastGroupVlanId_Object = MibTableColumn
mldsVlanMulticastGroupVlanId = _MldsVlanMulticastGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 5, 1, 1),
    _MldsVlanMulticastGroupVlanId_Type()
)
mldsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupVlanId.setStatus("current")
_MldsVlanMulticastGroupIpAddress_Type = Ipv6Address
_MldsVlanMulticastGroupIpAddress_Object = MibTableColumn
mldsVlanMulticastGroupIpAddress = _MldsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 5, 1, 2),
    _MldsVlanMulticastGroupIpAddress_Type()
)
mldsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupIpAddress.setStatus("current")
_MldsVlanMulticastGroupMacAddress_Type = MacAddress
_MldsVlanMulticastGroupMacAddress_Object = MibTableColumn
mldsVlanMulticastGroupMacAddress = _MldsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 5, 1, 3),
    _MldsVlanMulticastGroupMacAddress_Type()
)
mldsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupMacAddress.setStatus("current")
_MldsVlanMulticastGroupPortList_Type = PortList
_MldsVlanMulticastGroupPortList_Object = MibTableColumn
mldsVlanMulticastGroupPortList = _MldsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 3, 5, 1, 4),
    _MldsVlanMulticastGroupPortList_Type()
)
mldsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupPortList.setStatus("current")
_SysMldsHost_ObjectIdentity = ObjectIdentity
sysMldsHost = _SysMldsHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 4)
)
_MldsHostTable_Object = MibTable
mldsHostTable = _MldsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 4, 1)
)
if mibBuilder.loadTexts:
    mldsHostTable.setStatus("current")
_MldsHostEntry_Object = MibTableRow
mldsHostEntry = _MldsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 4, 1, 1)
)
mldsHostEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "mldsHostTableVLANID"),
    (0, "DGS-1100-10ME_A1", "mldsHostTableGroupAddress"),
    (0, "DGS-1100-10ME_A1", "mldsHostTablePort"),
    (0, "DGS-1100-10ME_A1", "mldsHostTableHostIPAddress"),
)
if mibBuilder.loadTexts:
    mldsHostEntry.setStatus("current")


class _MldsHostTableVLANID_Type(Integer32):
    """Custom type mldsHostTableVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MldsHostTableVLANID_Type.__name__ = "Integer32"
_MldsHostTableVLANID_Object = MibTableColumn
mldsHostTableVLANID = _MldsHostTableVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 4, 1, 1, 1),
    _MldsHostTableVLANID_Type()
)
mldsHostTableVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTableVLANID.setStatus("current")
_MldsHostTableGroupAddress_Type = Ipv6Address
_MldsHostTableGroupAddress_Object = MibTableColumn
mldsHostTableGroupAddress = _MldsHostTableGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 4, 1, 1, 2),
    _MldsHostTableGroupAddress_Type()
)
mldsHostTableGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTableGroupAddress.setStatus("current")
_MldsHostTablePort_Type = Integer32
_MldsHostTablePort_Object = MibTableColumn
mldsHostTablePort = _MldsHostTablePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 4, 1, 1, 3),
    _MldsHostTablePort_Type()
)
mldsHostTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTablePort.setStatus("current")
_MldsHostTableHostIPAddress_Type = Ipv6Address
_MldsHostTableHostIPAddress_Object = MibTableColumn
mldsHostTableHostIPAddress = _MldsHostTableHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 88, 4, 1, 1, 4),
    _MldsHostTableHostIPAddress_Type()
)
mldsHostTableHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTableHostIPAddress.setStatus("current")
_CompanyTraceRoute_ObjectIdentity = ObjectIdentity
companyTraceRoute = _CompanyTraceRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90)
)


class _SysTraceRouteCtlAddressType_Type(Integer32):
    """Custom type sysTraceRouteCtlAddressType based on Integer32"""
    defaultValue = 1

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


_SysTraceRouteCtlAddressType_Type.__name__ = "Integer32"
_SysTraceRouteCtlAddressType_Object = MibScalar
sysTraceRouteCtlAddressType = _SysTraceRouteCtlAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 1),
    _SysTraceRouteCtlAddressType_Type()
)
sysTraceRouteCtlAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTraceRouteCtlAddressType.setStatus("current")
_SysTraceRouteCtlAddress_Type = InetAddress
_SysTraceRouteCtlAddress_Object = MibScalar
sysTraceRouteCtlAddress = _SysTraceRouteCtlAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 2),
    _SysTraceRouteCtlAddress_Type()
)
sysTraceRouteCtlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTraceRouteCtlAddress.setStatus("current")


class _SysTraceRouteCtlTimeOut_Type(Unsigned32):
    """Custom type sysTraceRouteCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SysTraceRouteCtlTimeOut_Type.__name__ = "Unsigned32"
_SysTraceRouteCtlTimeOut_Object = MibScalar
sysTraceRouteCtlTimeOut = _SysTraceRouteCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 3),
    _SysTraceRouteCtlTimeOut_Type()
)
sysTraceRouteCtlTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTraceRouteCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    sysTraceRouteCtlTimeOut.setUnits("seconds")


class _SysTraceRouteCtlTTL_Type(Unsigned32):
    """Custom type sysTraceRouteCtlTTL based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SysTraceRouteCtlTTL_Type.__name__ = "Unsigned32"
_SysTraceRouteCtlTTL_Object = MibScalar
sysTraceRouteCtlTTL = _SysTraceRouteCtlTTL_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 4),
    _SysTraceRouteCtlTTL_Type()
)
sysTraceRouteCtlTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTraceRouteCtlTTL.setStatus("current")
if mibBuilder.loadTexts:
    sysTraceRouteCtlTTL.setUnits("time-to-live value")


class _SysTraceRouteCtlPort_Type(Unsigned32):
    """Custom type sysTraceRouteCtlPort based on Unsigned32"""
    defaultValue = 33434

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 64900),
    )


_SysTraceRouteCtlPort_Type.__name__ = "Unsigned32"
_SysTraceRouteCtlPort_Object = MibScalar
sysTraceRouteCtlPort = _SysTraceRouteCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 5),
    _SysTraceRouteCtlPort_Type()
)
sysTraceRouteCtlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTraceRouteCtlPort.setStatus("current")
if mibBuilder.loadTexts:
    sysTraceRouteCtlPort.setUnits("UDP Port")


class _SysTraceRouteCtlProbe_Type(Unsigned32):
    """Custom type sysTraceRouteCtlProbe based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SysTraceRouteCtlProbe_Type.__name__ = "Unsigned32"
_SysTraceRouteCtlProbe_Object = MibScalar
sysTraceRouteCtlProbe = _SysTraceRouteCtlProbe_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 6),
    _SysTraceRouteCtlProbe_Type()
)
sysTraceRouteCtlProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTraceRouteCtlProbe.setStatus("current")
if mibBuilder.loadTexts:
    sysTraceRouteCtlProbe.setUnits("probes")


class _SysTraceRouteCtlAdminStatus_Type(Integer32):
    """Custom type sysTraceRouteCtlAdminStatus based on Integer32"""
    defaultValue = 2

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


_SysTraceRouteCtlAdminStatus_Type.__name__ = "Integer32"
_SysTraceRouteCtlAdminStatus_Object = MibScalar
sysTraceRouteCtlAdminStatus = _SysTraceRouteCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 7),
    _SysTraceRouteCtlAdminStatus_Type()
)
sysTraceRouteCtlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTraceRouteCtlAdminStatus.setStatus("current")
_SysTraceRouteHistoryTable_Object = MibTable
sysTraceRouteHistoryTable = _SysTraceRouteHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8)
)
if mibBuilder.loadTexts:
    sysTraceRouteHistoryTable.setStatus("current")
_TraceRouteHistoryEntry_Object = MibTableRow
traceRouteHistoryEntry = _TraceRouteHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1)
)
traceRouteHistoryEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "traceRouteHistoryIndex"),
    (0, "DGS-1100-10ME_A1", "traceRouteHistoryHopIndex"),
    (0, "DGS-1100-10ME_A1", "traceRouteHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    traceRouteHistoryEntry.setStatus("current")


class _TraceRouteHistoryIndex_Type(Unsigned32):
    """Custom type traceRouteHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TraceRouteHistoryIndex_Type.__name__ = "Unsigned32"
_TraceRouteHistoryIndex_Object = MibTableColumn
traceRouteHistoryIndex = _TraceRouteHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1, 1),
    _TraceRouteHistoryIndex_Type()
)
traceRouteHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHistoryIndex.setStatus("current")


class _TraceRouteHistoryHopIndex_Type(Unsigned32):
    """Custom type traceRouteHistoryHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteHistoryHopIndex_Type.__name__ = "Unsigned32"
_TraceRouteHistoryHopIndex_Object = MibTableColumn
traceRouteHistoryHopIndex = _TraceRouteHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1, 2),
    _TraceRouteHistoryHopIndex_Type()
)
traceRouteHistoryHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHistoryHopIndex.setStatus("current")


class _TraceRouteHistoryProbeIndex_Type(Unsigned32):
    """Custom type traceRouteHistoryProbeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TraceRouteHistoryProbeIndex_Type.__name__ = "Unsigned32"
_TraceRouteHistoryProbeIndex_Object = MibTableColumn
traceRouteHistoryProbeIndex = _TraceRouteHistoryProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1, 3),
    _TraceRouteHistoryProbeIndex_Type()
)
traceRouteHistoryProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHistoryProbeIndex.setStatus("current")
_TraceRouteHistoryHAddrType_Type = InetAddressType
_TraceRouteHistoryHAddrType_Object = MibTableColumn
traceRouteHistoryHAddrType = _TraceRouteHistoryHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1, 4),
    _TraceRouteHistoryHAddrType_Type()
)
traceRouteHistoryHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHistoryHAddrType.setStatus("current")
_TraceRouteHistoryHAddr_Type = InetAddress
_TraceRouteHistoryHAddr_Object = MibTableColumn
traceRouteHistoryHAddr = _TraceRouteHistoryHAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1, 5),
    _TraceRouteHistoryHAddr_Type()
)
traceRouteHistoryHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHistoryHAddr.setStatus("current")
_TraceRouteHistoryResponse_Type = Unsigned32
_TraceRouteHistoryResponse_Object = MibTableColumn
traceRouteHistoryResponse = _TraceRouteHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1, 6),
    _TraceRouteHistoryResponse_Type()
)
traceRouteHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteHistoryResponse.setUnits("milliseconds")
_TraceRouteHistoryStatus_Type = OperationResponseStatus
_TraceRouteHistoryStatus_Object = MibTableColumn
traceRouteHistoryStatus = _TraceRouteHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 90, 8, 1, 7),
    _TraceRouteHistoryStatus_Type()
)
traceRouteHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHistoryStatus.setStatus("current")
_CompanyPPPoE_ObjectIdentity = ObjectIdentity
companyPPPoE = _CompanyPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98)
)


class _SysPppoeGlobalState_Type(Integer32):
    """Custom type sysPppoeGlobalState based on Integer32"""
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


_SysPppoeGlobalState_Type.__name__ = "Integer32"
_SysPppoeGlobalState_Object = MibScalar
sysPppoeGlobalState = _SysPppoeGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98, 1),
    _SysPppoeGlobalState_Type()
)
sysPppoeGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPppoeGlobalState.setStatus("current")
_SysPppoePortTable_Object = MibTable
sysPppoePortTable = _SysPppoePortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98, 2)
)
if mibBuilder.loadTexts:
    sysPppoePortTable.setStatus("current")
_PppoePortEntry_Object = MibTableRow
pppoePortEntry = _PppoePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98, 2, 1)
)
pppoePortEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "pppoePortIndex"),
)
if mibBuilder.loadTexts:
    pppoePortEntry.setStatus("current")


class _PppoePortIndex_Type(Integer32):
    """Custom type pppoePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PppoePortIndex_Type.__name__ = "Integer32"
_PppoePortIndex_Object = MibTableColumn
pppoePortIndex = _PppoePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98, 2, 1, 1),
    _PppoePortIndex_Type()
)
pppoePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoePortIndex.setStatus("current")


class _PppoePortState_Type(Integer32):
    """Custom type pppoePortState based on Integer32"""
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


_PppoePortState_Type.__name__ = "Integer32"
_PppoePortState_Object = MibTableColumn
pppoePortState = _PppoePortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98, 2, 1, 2),
    _PppoePortState_Type()
)
pppoePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortState.setStatus("current")


class _PppoePortCircuitIDType_Type(Integer32):
    """Custom type pppoePortCircuitIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("udf", 3))
    )


_PppoePortCircuitIDType_Type.__name__ = "Integer32"
_PppoePortCircuitIDType_Object = MibTableColumn
pppoePortCircuitIDType = _PppoePortCircuitIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98, 2, 1, 3),
    _PppoePortCircuitIDType_Type()
)
pppoePortCircuitIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortCircuitIDType.setStatus("current")


class _PppoePortUDFString_Type(DisplayString):
    """Custom type pppoePortUDFString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppoePortUDFString_Type.__name__ = "DisplayString"
_PppoePortUDFString_Object = MibTableColumn
pppoePortUDFString = _PppoePortUDFString_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 98, 2, 1, 4),
    _PppoePortUDFString_Type()
)
pppoePortUDFString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortUDFString.setStatus("current")
_CompanyStatistics_ObjectIdentity = ObjectIdentity
companyStatistics = _CompanyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99)
)
_SysStatisticsTable_Object = MibTable
sysStatisticsTable = _SysStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1)
)
if mibBuilder.loadTexts:
    sysStatisticsTable.setStatus("current")
_StatisticsEntry_Object = MibTableRow
statisticsEntry = _StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1)
)
statisticsEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "statisticsIndex"),
)
if mibBuilder.loadTexts:
    statisticsEntry.setStatus("current")
_StatisticsIndex_Type = InterfaceIndex
_StatisticsIndex_Object = MibTableColumn
statisticsIndex = _StatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 1),
    _StatisticsIndex_Type()
)
statisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsIndex.setStatus("current")
_StatisticsInOctets_Type = Counter64
_StatisticsInOctets_Object = MibTableColumn
statisticsInOctets = _StatisticsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 2),
    _StatisticsInOctets_Type()
)
statisticsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsInOctets.setStatus("current")
_StatisticsInUcastPkts_Type = Counter32
_StatisticsInUcastPkts_Object = MibTableColumn
statisticsInUcastPkts = _StatisticsInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 3),
    _StatisticsInUcastPkts_Type()
)
statisticsInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsInUcastPkts.setStatus("current")
_StatisticsInMcastPkts_Type = Counter32
_StatisticsInMcastPkts_Object = MibTableColumn
statisticsInMcastPkts = _StatisticsInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 4),
    _StatisticsInMcastPkts_Type()
)
statisticsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsInMcastPkts.setStatus("current")
_StatisticsInNUcastPkts_Type = Counter32
_StatisticsInNUcastPkts_Object = MibTableColumn
statisticsInNUcastPkts = _StatisticsInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 5),
    _StatisticsInNUcastPkts_Type()
)
statisticsInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsInNUcastPkts.setStatus("deprecated")
_StatisticsInDiscards_Type = Counter32
_StatisticsInDiscards_Object = MibTableColumn
statisticsInDiscards = _StatisticsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 6),
    _StatisticsInDiscards_Type()
)
statisticsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsInDiscards.setStatus("current")
_StatisticsInErrors_Type = Counter32
_StatisticsInErrors_Object = MibTableColumn
statisticsInErrors = _StatisticsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 7),
    _StatisticsInErrors_Type()
)
statisticsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsInErrors.setStatus("current")
_StatisticsOutOctets_Type = Counter64
_StatisticsOutOctets_Object = MibTableColumn
statisticsOutOctets = _StatisticsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 8),
    _StatisticsOutOctets_Type()
)
statisticsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsOutOctets.setStatus("current")
_StatisticsOutUcastPkts_Type = Counter32
_StatisticsOutUcastPkts_Object = MibTableColumn
statisticsOutUcastPkts = _StatisticsOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 9),
    _StatisticsOutUcastPkts_Type()
)
statisticsOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsOutUcastPkts.setStatus("current")
_StatisticsOutNUcastPkts_Type = Counter32
_StatisticsOutNUcastPkts_Object = MibTableColumn
statisticsOutNUcastPkts = _StatisticsOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 10),
    _StatisticsOutNUcastPkts_Type()
)
statisticsOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsOutNUcastPkts.setStatus("deprecated")
_StatisticsOutErrors_Type = Counter32
_StatisticsOutErrors_Object = MibTableColumn
statisticsOutErrors = _StatisticsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 11),
    _StatisticsOutErrors_Type()
)
statisticsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsOutErrors.setStatus("current")
_StatisticsOutDiscards_Type = Counter32
_StatisticsOutDiscards_Object = MibTableColumn
statisticsOutDiscards = _StatisticsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 12),
    _StatisticsOutDiscards_Type()
)
statisticsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsOutDiscards.setStatus("current")
_StatisticsLateCollisions_Type = Counter32
_StatisticsLateCollisions_Object = MibTableColumn
statisticsLateCollisions = _StatisticsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 13),
    _StatisticsLateCollisions_Type()
)
statisticsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsLateCollisions.setStatus("current")
_StatisticsExcessiveCollisions_Type = Counter32
_StatisticsExcessiveCollisions_Object = MibTableColumn
statisticsExcessiveCollisions = _StatisticsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 14),
    _StatisticsExcessiveCollisions_Type()
)
statisticsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsExcessiveCollisions.setStatus("current")
_StatisticsFCSErrors_Type = Counter32
_StatisticsFCSErrors_Object = MibTableColumn
statisticsFCSErrors = _StatisticsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 15),
    _StatisticsFCSErrors_Type()
)
statisticsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsFCSErrors.setStatus("current")
_StatisticsFrameTooLongs_Type = Counter32
_StatisticsFrameTooLongs_Object = MibTableColumn
statisticsFrameTooLongs = _StatisticsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 16),
    _StatisticsFrameTooLongs_Type()
)
statisticsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsFrameTooLongs.setStatus("current")
_StatisticsEtherUndersizePkts_Type = Counter32
_StatisticsEtherUndersizePkts_Object = MibTableColumn
statisticsEtherUndersizePkts = _StatisticsEtherUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 17),
    _StatisticsEtherUndersizePkts_Type()
)
statisticsEtherUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsEtherUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    statisticsEtherUndersizePkts.setUnits("Packets")
_StatisticsEtherOversizePkts_Type = Counter32
_StatisticsEtherOversizePkts_Object = MibTableColumn
statisticsEtherOversizePkts = _StatisticsEtherOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 18),
    _StatisticsEtherOversizePkts_Type()
)
statisticsEtherOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsEtherOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    statisticsEtherOversizePkts.setUnits("Packets")
_StatisticsEtherFragments_Type = Counter32
_StatisticsEtherFragments_Object = MibTableColumn
statisticsEtherFragments = _StatisticsEtherFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 19),
    _StatisticsEtherFragments_Type()
)
statisticsEtherFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsEtherFragments.setStatus("current")
if mibBuilder.loadTexts:
    statisticsEtherFragments.setUnits("Packets")
_StatisticsEtherJabbers_Type = Counter32
_StatisticsEtherJabbers_Object = MibTableColumn
statisticsEtherJabbers = _StatisticsEtherJabbers_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 20),
    _StatisticsEtherJabbers_Type()
)
statisticsEtherJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsEtherJabbers.setStatus("current")
if mibBuilder.loadTexts:
    statisticsEtherJabbers.setUnits("Packets")
_StatisticsEtherDropEvents_Type = Counter32
_StatisticsEtherDropEvents_Object = MibTableColumn
statisticsEtherDropEvents = _StatisticsEtherDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 21),
    _StatisticsEtherDropEvents_Type()
)
statisticsEtherDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsEtherDropEvents.setStatus("current")
_StatisticsDeferredTransmissions_Type = Counter32
_StatisticsDeferredTransmissions_Object = MibTableColumn
statisticsDeferredTransmissions = _StatisticsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 22),
    _StatisticsDeferredTransmissions_Type()
)
statisticsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsDeferredTransmissions.setStatus("current")
_StatisticsSingleCollisionFrames_Type = Counter32
_StatisticsSingleCollisionFrames_Object = MibTableColumn
statisticsSingleCollisionFrames = _StatisticsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 23),
    _StatisticsSingleCollisionFrames_Type()
)
statisticsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsSingleCollisionFrames.setStatus("current")
_StatisticsStatsCollisions_Type = Counter32
_StatisticsStatsCollisions_Object = MibTableColumn
statisticsStatsCollisions = _StatisticsStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 24),
    _StatisticsStatsCollisions_Type()
)
statisticsStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsStatsCollisions.setStatus("current")
_StatisticsPkts64Octets_Type = Counter32
_StatisticsPkts64Octets_Object = MibTableColumn
statisticsPkts64Octets = _StatisticsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 25),
    _StatisticsPkts64Octets_Type()
)
statisticsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsPkts64Octets.setStatus("current")
_StatisticsPkts65to127Octets_Type = Counter32
_StatisticsPkts65to127Octets_Object = MibTableColumn
statisticsPkts65to127Octets = _StatisticsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 26),
    _StatisticsPkts65to127Octets_Type()
)
statisticsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsPkts65to127Octets.setStatus("current")
_StatisticsPkts128to255Octets_Type = Counter32
_StatisticsPkts128to255Octets_Object = MibTableColumn
statisticsPkts128to255Octets = _StatisticsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 27),
    _StatisticsPkts128to255Octets_Type()
)
statisticsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsPkts128to255Octets.setStatus("current")
_StatisticsPkts256to511Octets_Type = Counter32
_StatisticsPkts256to511Octets_Object = MibTableColumn
statisticsPkts256to511Octets = _StatisticsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 28),
    _StatisticsPkts256to511Octets_Type()
)
statisticsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsPkts256to511Octets.setStatus("current")
_StatisticsPkts512to1023Octets_Type = Counter32
_StatisticsPkts512to1023Octets_Object = MibTableColumn
statisticsPkts512to1023Octets = _StatisticsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 29),
    _StatisticsPkts512to1023Octets_Type()
)
statisticsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsPkts512to1023Octets.setStatus("current")
_StatisticsPkts1024to1518Octets_Type = Counter32
_StatisticsPkts1024to1518Octets_Object = MibTableColumn
statisticsPkts1024to1518Octets = _StatisticsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 1, 1, 30),
    _StatisticsPkts1024to1518Octets_Type()
)
statisticsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsPkts1024to1518Octets.setStatus("current")
_SysStatisticsClearTable_Object = MibTable
sysStatisticsClearTable = _SysStatisticsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 2)
)
if mibBuilder.loadTexts:
    sysStatisticsClearTable.setStatus("current")
_StatisticsClearEntry_Object = MibTableRow
statisticsClearEntry = _StatisticsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 2, 1)
)
statisticsClearEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "statisticsClearIndex"),
)
if mibBuilder.loadTexts:
    statisticsClearEntry.setStatus("current")
_StatisticsClearIndex_Type = Integer32
_StatisticsClearIndex_Object = MibTableColumn
statisticsClearIndex = _StatisticsClearIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 2, 1, 1),
    _StatisticsClearIndex_Type()
)
statisticsClearIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsClearIndex.setStatus("current")


class _StatisticsClearStatus_Type(Integer32):
    """Custom type statisticsClearStatus based on Integer32"""
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


_StatisticsClearStatus_Type.__name__ = "Integer32"
_StatisticsClearStatus_Object = MibTableColumn
statisticsClearStatus = _StatisticsClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 99, 2, 1, 2),
    _StatisticsClearStatus_Type()
)
statisticsClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statisticsClearStatus.setStatus("current")
_CompanyPing_ObjectIdentity = ObjectIdentity
companyPing = _CompanyPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100)
)


class _SysPingDestIpType_Type(Integer32):
    """Custom type sysPingDestIpType based on Integer32"""
    defaultValue = 1

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


_SysPingDestIpType_Type.__name__ = "Integer32"
_SysPingDestIpType_Object = MibScalar
sysPingDestIpType = _SysPingDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100, 1),
    _SysPingDestIpType_Type()
)
sysPingDestIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPingDestIpType.setStatus("current")
_SysPingDestIpAddr_Type = InetAddress
_SysPingDestIpAddr_Object = MibScalar
sysPingDestIpAddr = _SysPingDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100, 2),
    _SysPingDestIpAddr_Type()
)
sysPingDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPingDestIpAddr.setStatus("current")


class _SysPingTimeout_Type(Integer32):
    """Custom type sysPingTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_SysPingTimeout_Type.__name__ = "Integer32"
_SysPingTimeout_Object = MibScalar
sysPingTimeout = _SysPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100, 3),
    _SysPingTimeout_Type()
)
sysPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPingTimeout.setStatus("current")


class _SysPingTimes_Type(Integer32):
    """Custom type sysPingTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysPingTimes_Type.__name__ = "Integer32"
_SysPingTimes_Object = MibScalar
sysPingTimes = _SysPingTimes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100, 4),
    _SysPingTimes_Type()
)
sysPingTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPingTimes.setStatus("current")


class _SysPingStart_Type(Integer32):
    """Custom type sysPingStart based on Integer32"""
    defaultValue = 2

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


_SysPingStart_Type.__name__ = "Integer32"
_SysPingStart_Object = MibScalar
sysPingStart = _SysPingStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100, 5),
    _SysPingStart_Type()
)
sysPingStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPingStart.setStatus("current")


class _SysPingStatus_Type(Integer32):
    """Custom type sysPingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 3),
          ("notinitiated", 1),
          ("progress", 2))
    )


_SysPingStatus_Type.__name__ = "Integer32"
_SysPingStatus_Object = MibScalar
sysPingStatus = _SysPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100, 6),
    _SysPingStatus_Type()
)
sysPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPingStatus.setStatus("current")
_SysPingSuccesses_Type = Integer32
_SysPingSuccesses_Object = MibScalar
sysPingSuccesses = _SysPingSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 100, 7),
    _SysPingSuccesses_Type()
)
sysPingSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPingSuccesses.setStatus("current")
_CompanyDDP_ObjectIdentity = ObjectIdentity
companyDDP = _CompanyDDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 101)
)


class _SysDDPStatus_Type(Integer32):
    """Custom type sysDDPStatus based on Integer32"""
    defaultValue = 1

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


_SysDDPStatus_Type.__name__ = "Integer32"
_SysDDPStatus_Object = MibScalar
sysDDPStatus = _SysDDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 101, 1),
    _SysDDPStatus_Type()
)
sysDDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDDPStatus.setStatus("current")


class _SysDDPReportTime_Type(Integer32):
    """Custom type sysDDPReportTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              90,
              120)
        )
    )
    namedValues = NamedValues(
        *(("never", 0),
          ("offset120sec", 120),
          ("offset30sec", 30),
          ("offset60sec", 60),
          ("offset90sec", 90))
    )


_SysDDPReportTime_Type.__name__ = "Integer32"
_SysDDPReportTime_Object = MibScalar
sysDDPReportTime = _SysDDPReportTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 101, 2),
    _SysDDPReportTime_Type()
)
sysDDPReportTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDDPReportTime.setStatus("current")
_SysDDPTable_Object = MibTable
sysDDPTable = _SysDDPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 101, 3)
)
if mibBuilder.loadTexts:
    sysDDPTable.setStatus("current")
_DdpEntry_Object = MibTableRow
ddpEntry = _DdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 101, 3, 1)
)
ddpEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "ddpPort"),
)
if mibBuilder.loadTexts:
    ddpEntry.setStatus("current")


class _DdpPort_Type(Integer32):
    """Custom type ddpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DdpPort_Type.__name__ = "Integer32"
_DdpPort_Object = MibTableColumn
ddpPort = _DdpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 101, 3, 1, 1),
    _DdpPort_Type()
)
ddpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpPort.setStatus("current")


class _DdpPortStatus_Type(Integer32):
    """Custom type ddpPortStatus based on Integer32"""
    defaultValue = 1

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


_DdpPortStatus_Type.__name__ = "Integer32"
_DdpPortStatus_Object = MibTableColumn
ddpPortStatus = _DdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 101, 3, 1, 2),
    _DdpPortStatus_Type()
)
ddpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddpPortStatus.setStatus("current")
_CompanySession_ObjectIdentity = ObjectIdentity
companySession = _CompanySession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102)
)
_SyssessionTable_Object = MibTable
syssessionTable = _SyssessionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1)
)
if mibBuilder.loadTexts:
    syssessionTable.setStatus("current")
_SyssessionEntry_Object = MibTableRow
syssessionEntry = _SyssessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1)
)
syssessionEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "sessionID"),
)
if mibBuilder.loadTexts:
    syssessionEntry.setStatus("current")
_SessionID_Type = Unsigned32
_SessionID_Object = MibTableColumn
sessionID = _SessionID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1, 1),
    _SessionID_Type()
)
sessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionID.setStatus("current")
_SessionUserName_Type = DisplayString
_SessionUserName_Object = MibTableColumn
sessionUserName = _SessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1, 2),
    _SessionUserName_Type()
)
sessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUserName.setStatus("current")


class _SessionUserPrivilege_Type(Integer32):
    """Custom type sessionUserPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("admin", 5),
          ("operator", 4),
          ("user", 3))
    )


_SessionUserPrivilege_Type.__name__ = "Integer32"
_SessionUserPrivilege_Object = MibTableColumn
sessionUserPrivilege = _SessionUserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1, 3),
    _SessionUserPrivilege_Type()
)
sessionUserPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionUserPrivilege.setStatus("current")
_SessionLoginTime_Type = DisplayString
_SessionLoginTime_Object = MibTableColumn
sessionLoginTime = _SessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1, 4),
    _SessionLoginTime_Type()
)
sessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLoginTime.setStatus("current")
_SessionLiveTime_Type = DisplayString
_SessionLiveTime_Object = MibTableColumn
sessionLiveTime = _SessionLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1, 5),
    _SessionLiveTime_Type()
)
sessionLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLiveTime.setStatus("current")


class _SessionType_Type(Integer32):
    """Custom type sessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("ssh", 3),
          ("telnet", 2))
    )


_SessionType_Type.__name__ = "Integer32"
_SessionType_Object = MibTableColumn
sessionType = _SessionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1, 6),
    _SessionType_Type()
)
sessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionType.setStatus("current")
_SessionIP_Type = InetAddress
_SessionIP_Object = MibTableColumn
sessionIP = _SessionIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 102, 1, 1, 7),
    _SessionIP_Type()
)
sessionIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionIP.setStatus("current")
_CompanyACL_ObjectIdentity = ObjectIdentity
companyACL = _CompanyACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103)
)
_SysAclProfile_ObjectIdentity = ObjectIdentity
sysAclProfile = _SysAclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1)
)
_AclL2ProfileTable_Object = MibTable
aclL2ProfileTable = _AclL2ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1)
)
if mibBuilder.loadTexts:
    aclL2ProfileTable.setStatus("current")
_AclL2ProfileEntry_Object = MibTableRow
aclL2ProfileEntry = _AclL2ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1)
)
aclL2ProfileEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aclL2ProfileID"),
)
if mibBuilder.loadTexts:
    aclL2ProfileEntry.setStatus("current")


class _AclL2ProfileID_Type(Integer32):
    """Custom type aclL2ProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_AclL2ProfileID_Type.__name__ = "Integer32"
_AclL2ProfileID_Object = MibTableColumn
aclL2ProfileID = _AclL2ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 1),
    _AclL2ProfileID_Type()
)
aclL2ProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2ProfileID.setStatus("current")
_AclL2RuleCount_Type = Integer32
_AclL2RuleCount_Object = MibTableColumn
aclL2RuleCount = _AclL2RuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 2),
    _AclL2RuleCount_Type()
)
aclL2RuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleCount.setStatus("current")
_AclL2SrcMacMask_Type = MacAddress
_AclL2SrcMacMask_Object = MibTableColumn
aclL2SrcMacMask = _AclL2SrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 3),
    _AclL2SrcMacMask_Type()
)
aclL2SrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2SrcMacMask.setStatus("current")
_AclL2DstMacMask_Type = MacAddress
_AclL2DstMacMask_Object = MibTableColumn
aclL2DstMacMask = _AclL2DstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 4),
    _AclL2DstMacMask_Type()
)
aclL2DstMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2DstMacMask.setStatus("current")


class _AclL28021pCheck_Type(Integer32):
    """Custom type aclL28021pCheck based on Integer32"""
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


_AclL28021pCheck_Type.__name__ = "Integer32"
_AclL28021pCheck_Object = MibTableColumn
aclL28021pCheck = _AclL28021pCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 5),
    _AclL28021pCheck_Type()
)
aclL28021pCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL28021pCheck.setStatus("current")


class _AclL2VlanIdCheck_Type(Integer32):
    """Custom type aclL2VlanIdCheck based on Integer32"""
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


_AclL2VlanIdCheck_Type.__name__ = "Integer32"
_AclL2VlanIdCheck_Object = MibTableColumn
aclL2VlanIdCheck = _AclL2VlanIdCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 6),
    _AclL2VlanIdCheck_Type()
)
aclL2VlanIdCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2VlanIdCheck.setStatus("current")


class _AclL2EtherTypeCheck_Type(Integer32):
    """Custom type aclL2EtherTypeCheck based on Integer32"""
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


_AclL2EtherTypeCheck_Type.__name__ = "Integer32"
_AclL2EtherTypeCheck_Object = MibTableColumn
aclL2EtherTypeCheck = _AclL2EtherTypeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 7),
    _AclL2EtherTypeCheck_Type()
)
aclL2EtherTypeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2EtherTypeCheck.setStatus("current")
_AclL2ProfileStatus_Type = RowStatus
_AclL2ProfileStatus_Object = MibTableColumn
aclL2ProfileStatus = _AclL2ProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 1, 1, 8),
    _AclL2ProfileStatus_Type()
)
aclL2ProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL2ProfileStatus.setStatus("current")
_AclL3ProfileTable_Object = MibTable
aclL3ProfileTable = _AclL3ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2)
)
if mibBuilder.loadTexts:
    aclL3ProfileTable.setStatus("current")
_AclL3ProfileEntry_Object = MibTableRow
aclL3ProfileEntry = _AclL3ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1)
)
aclL3ProfileEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aclL3ProfileID"),
)
if mibBuilder.loadTexts:
    aclL3ProfileEntry.setStatus("current")


class _AclL3ProfileID_Type(Integer32):
    """Custom type aclL3ProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_AclL3ProfileID_Type.__name__ = "Integer32"
_AclL3ProfileID_Object = MibTableColumn
aclL3ProfileID = _AclL3ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 1),
    _AclL3ProfileID_Type()
)
aclL3ProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3ProfileID.setStatus("current")
_AclL3RuleCount_Type = Integer32
_AclL3RuleCount_Object = MibTableColumn
aclL3RuleCount = _AclL3RuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 2),
    _AclL3RuleCount_Type()
)
aclL3RuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleCount.setStatus("current")
_AclL3ProfileType_Type = InetAddressType
_AclL3ProfileType_Object = MibTableColumn
aclL3ProfileType = _AclL3ProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 3),
    _AclL3ProfileType_Type()
)
aclL3ProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3ProfileType.setStatus("current")
_AclL3Ip4SrcAddrMask_Type = IpAddress
_AclL3Ip4SrcAddrMask_Object = MibTableColumn
aclL3Ip4SrcAddrMask = _AclL3Ip4SrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 4),
    _AclL3Ip4SrcAddrMask_Type()
)
aclL3Ip4SrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip4SrcAddrMask.setStatus("current")
_AclL3Ip4DstAddrMask_Type = IpAddress
_AclL3Ip4DstAddrMask_Object = MibTableColumn
aclL3Ip4DstAddrMask = _AclL3Ip4DstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 5),
    _AclL3Ip4DstAddrMask_Type()
)
aclL3Ip4DstAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip4DstAddrMask.setStatus("current")


class _AclL3Ip4DscpCheck_Type(Integer32):
    """Custom type aclL3Ip4DscpCheck based on Integer32"""
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


_AclL3Ip4DscpCheck_Type.__name__ = "Integer32"
_AclL3Ip4DscpCheck_Object = MibTableColumn
aclL3Ip4DscpCheck = _AclL3Ip4DscpCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 6),
    _AclL3Ip4DscpCheck_Type()
)
aclL3Ip4DscpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip4DscpCheck.setStatus("current")


class _AclL3Ip4TosCheck_Type(Integer32):
    """Custom type aclL3Ip4TosCheck based on Integer32"""
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


_AclL3Ip4TosCheck_Type.__name__ = "Integer32"
_AclL3Ip4TosCheck_Object = MibTableColumn
aclL3Ip4TosCheck = _AclL3Ip4TosCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 7),
    _AclL3Ip4TosCheck_Type()
)
aclL3Ip4TosCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip4TosCheck.setStatus("current")


class _AclL3Ip4Protocol_Type(Integer32):
    """Custom type aclL3Ip4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17,
              58)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("icmpv6", 58),
          ("igmp", 2),
          ("none", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_AclL3Ip4Protocol_Type.__name__ = "Integer32"
_AclL3Ip4Protocol_Object = MibTableColumn
aclL3Ip4Protocol = _AclL3Ip4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 8),
    _AclL3Ip4Protocol_Type()
)
aclL3Ip4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip4Protocol.setStatus("current")
_AclL3Ip4ProtocolMask_Type = OctetString
_AclL3Ip4ProtocolMask_Object = MibTableColumn
aclL3Ip4ProtocolMask = _AclL3Ip4ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 9),
    _AclL3Ip4ProtocolMask_Type()
)
aclL3Ip4ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip4ProtocolMask.setStatus("current")
_AclL3Ip6SrcAddrMask_Type = Ipv6Address
_AclL3Ip6SrcAddrMask_Object = MibTableColumn
aclL3Ip6SrcAddrMask = _AclL3Ip6SrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 10),
    _AclL3Ip6SrcAddrMask_Type()
)
aclL3Ip6SrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip6SrcAddrMask.setStatus("current")
_AclL3Ip6DstAddrMask_Type = Ipv6Address
_AclL3Ip6DstAddrMask_Object = MibTableColumn
aclL3Ip6DstAddrMask = _AclL3Ip6DstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 11),
    _AclL3Ip6DstAddrMask_Type()
)
aclL3Ip6DstAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip6DstAddrMask.setStatus("current")


class _AclL3Ip6TrafficClassCheck_Type(Integer32):
    """Custom type aclL3Ip6TrafficClassCheck based on Integer32"""
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


_AclL3Ip6TrafficClassCheck_Type.__name__ = "Integer32"
_AclL3Ip6TrafficClassCheck_Object = MibTableColumn
aclL3Ip6TrafficClassCheck = _AclL3Ip6TrafficClassCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 12),
    _AclL3Ip6TrafficClassCheck_Type()
)
aclL3Ip6TrafficClassCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip6TrafficClassCheck.setStatus("current")


class _AclL3IcmpTypeCheck_Type(Integer32):
    """Custom type aclL3IcmpTypeCheck based on Integer32"""
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


_AclL3IcmpTypeCheck_Type.__name__ = "Integer32"
_AclL3IcmpTypeCheck_Object = MibTableColumn
aclL3IcmpTypeCheck = _AclL3IcmpTypeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 13),
    _AclL3IcmpTypeCheck_Type()
)
aclL3IcmpTypeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IcmpTypeCheck.setStatus("current")


class _AclL3IcmpCodeCheck_Type(Integer32):
    """Custom type aclL3IcmpCodeCheck based on Integer32"""
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


_AclL3IcmpCodeCheck_Type.__name__ = "Integer32"
_AclL3IcmpCodeCheck_Object = MibTableColumn
aclL3IcmpCodeCheck = _AclL3IcmpCodeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 14),
    _AclL3IcmpCodeCheck_Type()
)
aclL3IcmpCodeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IcmpCodeCheck.setStatus("current")


class _AclL3IgmpTypeCheck_Type(Integer32):
    """Custom type aclL3IgmpTypeCheck based on Integer32"""
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


_AclL3IgmpTypeCheck_Type.__name__ = "Integer32"
_AclL3IgmpTypeCheck_Object = MibTableColumn
aclL3IgmpTypeCheck = _AclL3IgmpTypeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 15),
    _AclL3IgmpTypeCheck_Type()
)
aclL3IgmpTypeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IgmpTypeCheck.setStatus("current")
_AclL3SrcPortMask_Type = OctetString
_AclL3SrcPortMask_Object = MibTableColumn
aclL3SrcPortMask = _AclL3SrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 16),
    _AclL3SrcPortMask_Type()
)
aclL3SrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3SrcPortMask.setStatus("current")
_AclL3DstPortMask_Type = OctetString
_AclL3DstPortMask_Object = MibTableColumn
aclL3DstPortMask = _AclL3DstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 17),
    _AclL3DstPortMask_Type()
)
aclL3DstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3DstPortMask.setStatus("current")


class _AclL3TcpFlagCheck_Type(Integer32):
    """Custom type aclL3TcpFlagCheck based on Integer32"""
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


_AclL3TcpFlagCheck_Type.__name__ = "Integer32"
_AclL3TcpFlagCheck_Object = MibTableColumn
aclL3TcpFlagCheck = _AclL3TcpFlagCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 18),
    _AclL3TcpFlagCheck_Type()
)
aclL3TcpFlagCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3TcpFlagCheck.setStatus("current")
_AclL3ProfileStatus_Type = RowStatus
_AclL3ProfileStatus_Object = MibTableColumn
aclL3ProfileStatus = _AclL3ProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 1, 2, 1, 19),
    _AclL3ProfileStatus_Type()
)
aclL3ProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3ProfileStatus.setStatus("current")
_SysAclRule_ObjectIdentity = ObjectIdentity
sysAclRule = _SysAclRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2)
)
_AclL2RuleTable_Object = MibTable
aclL2RuleTable = _AclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1)
)
if mibBuilder.loadTexts:
    aclL2RuleTable.setStatus("current")
_AclL2RuleEntry_Object = MibTableRow
aclL2RuleEntry = _AclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1)
)
aclL2RuleEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aclL2RuleProfileID"),
    (0, "DGS-1100-10ME_A1", "aclL2RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL2RuleEntry.setStatus("current")


class _AclL2RuleProfileID_Type(Integer32):
    """Custom type aclL2RuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_AclL2RuleProfileID_Type.__name__ = "Integer32"
_AclL2RuleProfileID_Object = MibTableColumn
aclL2RuleProfileID = _AclL2RuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 1),
    _AclL2RuleProfileID_Type()
)
aclL2RuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleProfileID.setStatus("current")


class _AclL2RuleAccessID_Type(Integer32):
    """Custom type aclL2RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL2RuleAccessID_Type.__name__ = "Integer32"
_AclL2RuleAccessID_Object = MibTableColumn
aclL2RuleAccessID = _AclL2RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 2),
    _AclL2RuleAccessID_Type()
)
aclL2RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleAccessID.setStatus("current")


class _AclL2VlanId_Type(Integer32):
    """Custom type aclL2VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AclL2VlanId_Type.__name__ = "Integer32"
_AclL2VlanId_Object = MibTableColumn
aclL2VlanId = _AclL2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 3),
    _AclL2VlanId_Type()
)
aclL2VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2VlanId.setStatus("current")
_AclL2SrcMac_Type = MacAddress
_AclL2SrcMac_Object = MibTableColumn
aclL2SrcMac = _AclL2SrcMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 4),
    _AclL2SrcMac_Type()
)
aclL2SrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2SrcMac.setStatus("current")
_AclL2DstMac_Type = MacAddress
_AclL2DstMac_Object = MibTableColumn
aclL2DstMac = _AclL2DstMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 5),
    _AclL2DstMac_Type()
)
aclL2DstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2DstMac.setStatus("current")


class _AclL28021p_Type(Integer32):
    """Custom type aclL28021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL28021p_Type.__name__ = "Integer32"
_AclL28021p_Object = MibTableColumn
aclL28021p = _AclL28021p_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 6),
    _AclL28021p_Type()
)
aclL28021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL28021p.setStatus("current")


class _AclL2EtherType_Type(Integer32):
    """Custom type aclL2EtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclL2EtherType_Type.__name__ = "Integer32"
_AclL2EtherType_Object = MibTableColumn
aclL2EtherType = _AclL2EtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 7),
    _AclL2EtherType_Type()
)
aclL2EtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2EtherType.setStatus("current")
_AclL2InPortList_Type = PortList
_AclL2InPortList_Object = MibTableColumn
aclL2InPortList = _AclL2InPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 8),
    _AclL2InPortList_Type()
)
aclL2InPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2InPortList.setStatus("current")


class _AclL2Action_Type(Integer32):
    """Custom type aclL2Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("permit", 1),
          ("rateLimit", 4),
          ("replaceDSCP", 6))
    )


_AclL2Action_Type.__name__ = "Integer32"
_AclL2Action_Object = MibTableColumn
aclL2Action = _AclL2Action_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 9),
    _AclL2Action_Type()
)
aclL2Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2Action.setStatus("current")


class _AclL2RateLimit_Type(Unsigned32):
    """Custom type aclL2RateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1000000),
    )


_AclL2RateLimit_Type.__name__ = "Unsigned32"
_AclL2RateLimit_Object = MibTableColumn
aclL2RateLimit = _AclL2RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 10),
    _AclL2RateLimit_Type()
)
aclL2RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RateLimit.setStatus("current")


class _AclL2ReplaceDSCP_Type(Integer32):
    """Custom type aclL2ReplaceDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL2ReplaceDSCP_Type.__name__ = "Integer32"
_AclL2ReplaceDSCP_Object = MibTableColumn
aclL2ReplaceDSCP = _AclL2ReplaceDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 11),
    _AclL2ReplaceDSCP_Type()
)
aclL2ReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2ReplaceDSCP.setStatus("current")
_AclL2RuleStatus_Type = RowStatus
_AclL2RuleStatus_Object = MibTableColumn
aclL2RuleStatus = _AclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 1, 1, 12),
    _AclL2RuleStatus_Type()
)
aclL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL2RuleStatus.setStatus("current")
_AclL3RuleTable_Object = MibTable
aclL3RuleTable = _AclL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2)
)
if mibBuilder.loadTexts:
    aclL3RuleTable.setStatus("current")
_AclL3RuleEntry_Object = MibTableRow
aclL3RuleEntry = _AclL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1)
)
aclL3RuleEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "aclL3RuleProfileID"),
    (0, "DGS-1100-10ME_A1", "aclL3RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3RuleEntry.setStatus("current")


class _AclL3RuleProfileID_Type(Integer32):
    """Custom type aclL3RuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_AclL3RuleProfileID_Type.__name__ = "Integer32"
_AclL3RuleProfileID_Object = MibTableColumn
aclL3RuleProfileID = _AclL3RuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 1),
    _AclL3RuleProfileID_Type()
)
aclL3RuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleProfileID.setStatus("current")


class _AclL3RuleAccessID_Type(Integer32):
    """Custom type aclL3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3RuleAccessID_Type.__name__ = "Integer32"
_AclL3RuleAccessID_Object = MibTableColumn
aclL3RuleAccessID = _AclL3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 2),
    _AclL3RuleAccessID_Type()
)
aclL3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleAccessID.setStatus("current")
_AclL3IP4SrcAddr_Type = IpAddress
_AclL3IP4SrcAddr_Object = MibTableColumn
aclL3IP4SrcAddr = _AclL3IP4SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 3),
    _AclL3IP4SrcAddr_Type()
)
aclL3IP4SrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IP4SrcAddr.setStatus("current")
_AclL3IP4DstAddr_Type = IpAddress
_AclL3IP4DstAddr_Object = MibTableColumn
aclL3IP4DstAddr = _AclL3IP4DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 4),
    _AclL3IP4DstAddr_Type()
)
aclL3IP4DstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IP4DstAddr.setStatus("current")


class _AclL3IP4DSCP_Type(Integer32):
    """Custom type aclL3IP4DSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL3IP4DSCP_Type.__name__ = "Integer32"
_AclL3IP4DSCP_Object = MibTableColumn
aclL3IP4DSCP = _AclL3IP4DSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 5),
    _AclL3IP4DSCP_Type()
)
aclL3IP4DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IP4DSCP.setStatus("current")


class _AclL3IP4ToS_Type(Integer32):
    """Custom type aclL3IP4ToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL3IP4ToS_Type.__name__ = "Integer32"
_AclL3IP4ToS_Object = MibTableColumn
aclL3IP4ToS = _AclL3IP4ToS_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 6),
    _AclL3IP4ToS_Type()
)
aclL3IP4ToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IP4ToS.setStatus("current")


class _AclL3IP4Protocol_Type(Integer32):
    """Custom type aclL3IP4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclL3IP4Protocol_Type.__name__ = "Integer32"
_AclL3IP4Protocol_Object = MibTableColumn
aclL3IP4Protocol = _AclL3IP4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 7),
    _AclL3IP4Protocol_Type()
)
aclL3IP4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IP4Protocol.setStatus("current")
_AclL3IP6SrcAddr_Type = Ipv6Address
_AclL3IP6SrcAddr_Object = MibTableColumn
aclL3IP6SrcAddr = _AclL3IP6SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 8),
    _AclL3IP6SrcAddr_Type()
)
aclL3IP6SrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IP6SrcAddr.setStatus("current")
_AclL3IP6DstAddr_Type = Ipv6Address
_AclL3IP6DstAddr_Object = MibTableColumn
aclL3IP6DstAddr = _AclL3IP6DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 9),
    _AclL3IP6DstAddr_Type()
)
aclL3IP6DstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IP6DstAddr.setStatus("current")


class _AclL3Ip6TrafficClass_Type(Integer32):
    """Custom type aclL3Ip6TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3Ip6TrafficClass_Type.__name__ = "Integer32"
_AclL3Ip6TrafficClass_Object = MibTableColumn
aclL3Ip6TrafficClass = _AclL3Ip6TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 10),
    _AclL3Ip6TrafficClass_Type()
)
aclL3Ip6TrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Ip6TrafficClass.setStatus("current")
_AclL3IcmpType_Type = Integer32
_AclL3IcmpType_Object = MibTableColumn
aclL3IcmpType = _AclL3IcmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 11),
    _AclL3IcmpType_Type()
)
aclL3IcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IcmpType.setStatus("current")
_AclL3IcmpCode_Type = Integer32
_AclL3IcmpCode_Object = MibTableColumn
aclL3IcmpCode = _AclL3IcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 12),
    _AclL3IcmpCode_Type()
)
aclL3IcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IcmpCode.setStatus("current")
_AclL3IgmpType_Type = Integer32
_AclL3IgmpType_Object = MibTableColumn
aclL3IgmpType = _AclL3IgmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 13),
    _AclL3IgmpType_Type()
)
aclL3IgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3IgmpType.setStatus("current")


class _AclL3SrcPort_Type(Integer32):
    """Custom type aclL3SrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3SrcPort_Type.__name__ = "Integer32"
_AclL3SrcPort_Object = MibTableColumn
aclL3SrcPort = _AclL3SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 14),
    _AclL3SrcPort_Type()
)
aclL3SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3SrcPort.setStatus("current")


class _AclL3DstPort_Type(Integer32):
    """Custom type aclL3DstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3DstPort_Type.__name__ = "Integer32"
_AclL3DstPort_Object = MibTableColumn
aclL3DstPort = _AclL3DstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 15),
    _AclL3DstPort_Type()
)
aclL3DstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3DstPort.setStatus("current")


class _AclL3TcpFlagURG_Type(Integer32):
    """Custom type aclL3TcpFlagURG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_AclL3TcpFlagURG_Type.__name__ = "Integer32"
_AclL3TcpFlagURG_Object = MibTableColumn
aclL3TcpFlagURG = _AclL3TcpFlagURG_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 16),
    _AclL3TcpFlagURG_Type()
)
aclL3TcpFlagURG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3TcpFlagURG.setStatus("current")


class _AclL3TcpFlagACK_Type(Integer32):
    """Custom type aclL3TcpFlagACK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_AclL3TcpFlagACK_Type.__name__ = "Integer32"
_AclL3TcpFlagACK_Object = MibTableColumn
aclL3TcpFlagACK = _AclL3TcpFlagACK_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 17),
    _AclL3TcpFlagACK_Type()
)
aclL3TcpFlagACK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3TcpFlagACK.setStatus("current")


class _AclL3TcpFlagPSH_Type(Integer32):
    """Custom type aclL3TcpFlagPSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_AclL3TcpFlagPSH_Type.__name__ = "Integer32"
_AclL3TcpFlagPSH_Object = MibTableColumn
aclL3TcpFlagPSH = _AclL3TcpFlagPSH_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 18),
    _AclL3TcpFlagPSH_Type()
)
aclL3TcpFlagPSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3TcpFlagPSH.setStatus("current")


class _AclL3TcpFlagRST_Type(Integer32):
    """Custom type aclL3TcpFlagRST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_AclL3TcpFlagRST_Type.__name__ = "Integer32"
_AclL3TcpFlagRST_Object = MibTableColumn
aclL3TcpFlagRST = _AclL3TcpFlagRST_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 19),
    _AclL3TcpFlagRST_Type()
)
aclL3TcpFlagRST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3TcpFlagRST.setStatus("current")


class _AclL3TcpFlagSYN_Type(Integer32):
    """Custom type aclL3TcpFlagSYN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_AclL3TcpFlagSYN_Type.__name__ = "Integer32"
_AclL3TcpFlagSYN_Object = MibTableColumn
aclL3TcpFlagSYN = _AclL3TcpFlagSYN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 20),
    _AclL3TcpFlagSYN_Type()
)
aclL3TcpFlagSYN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3TcpFlagSYN.setStatus("current")


class _AclL3TcpFlagFIN_Type(Integer32):
    """Custom type aclL3TcpFlagFIN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_AclL3TcpFlagFIN_Type.__name__ = "Integer32"
_AclL3TcpFlagFIN_Object = MibTableColumn
aclL3TcpFlagFIN = _AclL3TcpFlagFIN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 21),
    _AclL3TcpFlagFIN_Type()
)
aclL3TcpFlagFIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3TcpFlagFIN.setStatus("current")
_AclL3InPortList_Type = PortList
_AclL3InPortList_Object = MibTableColumn
aclL3InPortList = _AclL3InPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 22),
    _AclL3InPortList_Type()
)
aclL3InPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3InPortList.setStatus("current")


class _AclL3Action_Type(Integer32):
    """Custom type aclL3Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("permit", 1),
          ("rateLimit", 4),
          ("replaceDSCP", 6))
    )


_AclL3Action_Type.__name__ = "Integer32"
_AclL3Action_Object = MibTableColumn
aclL3Action = _AclL3Action_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 23),
    _AclL3Action_Type()
)
aclL3Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3Action.setStatus("current")


class _AclL3RateLimit_Type(Unsigned32):
    """Custom type aclL3RateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1000000),
    )


_AclL3RateLimit_Type.__name__ = "Unsigned32"
_AclL3RateLimit_Object = MibTableColumn
aclL3RateLimit = _AclL3RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 24),
    _AclL3RateLimit_Type()
)
aclL3RateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RateLimit.setStatus("current")


class _AclL3ReplaceDSCP_Type(Integer32):
    """Custom type aclL3ReplaceDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL3ReplaceDSCP_Type.__name__ = "Integer32"
_AclL3ReplaceDSCP_Object = MibTableColumn
aclL3ReplaceDSCP = _AclL3ReplaceDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 25),
    _AclL3ReplaceDSCP_Type()
)
aclL3ReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3ReplaceDSCP.setStatus("current")
_AclL3RuleStatus_Type = RowStatus
_AclL3RuleStatus_Object = MibTableColumn
aclL3RuleStatus = _AclL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 2, 2, 1, 26),
    _AclL3RuleStatus_Type()
)
aclL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleStatus.setStatus("current")
_SysAclStatistic_ObjectIdentity = ObjectIdentity
sysAclStatistic = _SysAclStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 3)
)
_AclTotalProfile_Type = Integer32
_AclTotalProfile_Object = MibScalar
aclTotalProfile = _AclTotalProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 3, 1),
    _AclTotalProfile_Type()
)
aclTotalProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotalProfile.setStatus("current")
_AclUsedProfile_Type = Integer32
_AclUsedProfile_Object = MibScalar
aclUsedProfile = _AclUsedProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 3, 2),
    _AclUsedProfile_Type()
)
aclUsedProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclUsedProfile.setStatus("current")
_AclTotalRule_Type = Integer32
_AclTotalRule_Object = MibScalar
aclTotalRule = _AclTotalRule_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 3, 3),
    _AclTotalRule_Type()
)
aclTotalRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTotalRule.setStatus("current")
_AclUsedRule_Type = Integer32
_AclUsedRule_Object = MibScalar
aclUsedRule = _AclUsedRule_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 103, 3, 4),
    _AclUsedRule_Type()
)
aclUsedRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclUsedRule.setStatus("current")
_CompanyCPUACL_ObjectIdentity = ObjectIdentity
companyCPUACL = _CompanyCPUACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104)
)
_SysCpuAclProfile_ObjectIdentity = ObjectIdentity
sysCpuAclProfile = _SysCpuAclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1)
)
_CpuAclL2ProfileTable_Object = MibTable
cpuAclL2ProfileTable = _CpuAclL2ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1)
)
if mibBuilder.loadTexts:
    cpuAclL2ProfileTable.setStatus("current")
_CpuAclL2ProfileEntry_Object = MibTableRow
cpuAclL2ProfileEntry = _CpuAclL2ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1)
)
cpuAclL2ProfileEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "cpuAclL2ProfileID"),
)
if mibBuilder.loadTexts:
    cpuAclL2ProfileEntry.setStatus("current")


class _CpuAclL2ProfileID_Type(Integer32):
    """Custom type cpuAclL2ProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuAclL2ProfileID_Type.__name__ = "Integer32"
_CpuAclL2ProfileID_Object = MibTableColumn
cpuAclL2ProfileID = _CpuAclL2ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 1),
    _CpuAclL2ProfileID_Type()
)
cpuAclL2ProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL2ProfileID.setStatus("current")
_CpuAclL2RuleCount_Type = Integer32
_CpuAclL2RuleCount_Object = MibTableColumn
cpuAclL2RuleCount = _CpuAclL2RuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 2),
    _CpuAclL2RuleCount_Type()
)
cpuAclL2RuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL2RuleCount.setStatus("current")
_CpuAclL2SrcMacMask_Type = MacAddress
_CpuAclL2SrcMacMask_Object = MibTableColumn
cpuAclL2SrcMacMask = _CpuAclL2SrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 3),
    _CpuAclL2SrcMacMask_Type()
)
cpuAclL2SrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2SrcMacMask.setStatus("current")
_CpuAclL2DstMacMask_Type = MacAddress
_CpuAclL2DstMacMask_Object = MibTableColumn
cpuAclL2DstMacMask = _CpuAclL2DstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 4),
    _CpuAclL2DstMacMask_Type()
)
cpuAclL2DstMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2DstMacMask.setStatus("current")


class _CpuAclL28021pCheck_Type(Integer32):
    """Custom type cpuAclL28021pCheck based on Integer32"""
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


_CpuAclL28021pCheck_Type.__name__ = "Integer32"
_CpuAclL28021pCheck_Object = MibTableColumn
cpuAclL28021pCheck = _CpuAclL28021pCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 5),
    _CpuAclL28021pCheck_Type()
)
cpuAclL28021pCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL28021pCheck.setStatus("current")


class _CpuAclL2VlanIdCheck_Type(Integer32):
    """Custom type cpuAclL2VlanIdCheck based on Integer32"""
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


_CpuAclL2VlanIdCheck_Type.__name__ = "Integer32"
_CpuAclL2VlanIdCheck_Object = MibTableColumn
cpuAclL2VlanIdCheck = _CpuAclL2VlanIdCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 6),
    _CpuAclL2VlanIdCheck_Type()
)
cpuAclL2VlanIdCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2VlanIdCheck.setStatus("current")


class _CpuAclL2EtherTypeCheck_Type(Integer32):
    """Custom type cpuAclL2EtherTypeCheck based on Integer32"""
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


_CpuAclL2EtherTypeCheck_Type.__name__ = "Integer32"
_CpuAclL2EtherTypeCheck_Object = MibTableColumn
cpuAclL2EtherTypeCheck = _CpuAclL2EtherTypeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 7),
    _CpuAclL2EtherTypeCheck_Type()
)
cpuAclL2EtherTypeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2EtherTypeCheck.setStatus("current")
_CpuAclL2ProfileStatus_Type = RowStatus
_CpuAclL2ProfileStatus_Object = MibTableColumn
cpuAclL2ProfileStatus = _CpuAclL2ProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 1, 1, 8),
    _CpuAclL2ProfileStatus_Type()
)
cpuAclL2ProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuAclL2ProfileStatus.setStatus("current")
_CpuAclL3ProfileTable_Object = MibTable
cpuAclL3ProfileTable = _CpuAclL3ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2)
)
if mibBuilder.loadTexts:
    cpuAclL3ProfileTable.setStatus("current")
_CpuAclL3ProfileEntry_Object = MibTableRow
cpuAclL3ProfileEntry = _CpuAclL3ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1)
)
cpuAclL3ProfileEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "cpuAclL3ProfileID"),
)
if mibBuilder.loadTexts:
    cpuAclL3ProfileEntry.setStatus("current")


class _CpuAclL3ProfileID_Type(Integer32):
    """Custom type cpuAclL3ProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuAclL3ProfileID_Type.__name__ = "Integer32"
_CpuAclL3ProfileID_Object = MibTableColumn
cpuAclL3ProfileID = _CpuAclL3ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 1),
    _CpuAclL3ProfileID_Type()
)
cpuAclL3ProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL3ProfileID.setStatus("current")
_CpuAclL3RuleCount_Type = Integer32
_CpuAclL3RuleCount_Object = MibTableColumn
cpuAclL3RuleCount = _CpuAclL3RuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 2),
    _CpuAclL3RuleCount_Type()
)
cpuAclL3RuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL3RuleCount.setStatus("current")
_CpuAclL3ProfileType_Type = InetAddressType
_CpuAclL3ProfileType_Object = MibTableColumn
cpuAclL3ProfileType = _CpuAclL3ProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 3),
    _CpuAclL3ProfileType_Type()
)
cpuAclL3ProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3ProfileType.setStatus("current")
_CpuAclL3Ip4SrcAddrMask_Type = IpAddress
_CpuAclL3Ip4SrcAddrMask_Object = MibTableColumn
cpuAclL3Ip4SrcAddrMask = _CpuAclL3Ip4SrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 4),
    _CpuAclL3Ip4SrcAddrMask_Type()
)
cpuAclL3Ip4SrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4SrcAddrMask.setStatus("current")
_CpuAclL3Ip4DstAddrMask_Type = IpAddress
_CpuAclL3Ip4DstAddrMask_Object = MibTableColumn
cpuAclL3Ip4DstAddrMask = _CpuAclL3Ip4DstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 5),
    _CpuAclL3Ip4DstAddrMask_Type()
)
cpuAclL3Ip4DstAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4DstAddrMask.setStatus("current")


class _CpuAclL3Ip4DscpCheck_Type(Integer32):
    """Custom type cpuAclL3Ip4DscpCheck based on Integer32"""
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


_CpuAclL3Ip4DscpCheck_Type.__name__ = "Integer32"
_CpuAclL3Ip4DscpCheck_Object = MibTableColumn
cpuAclL3Ip4DscpCheck = _CpuAclL3Ip4DscpCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 6),
    _CpuAclL3Ip4DscpCheck_Type()
)
cpuAclL3Ip4DscpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4DscpCheck.setStatus("current")


class _CpuAclL3Ip4Protocol_Type(Integer32):
    """Custom type cpuAclL3Ip4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("none", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_CpuAclL3Ip4Protocol_Type.__name__ = "Integer32"
_CpuAclL3Ip4Protocol_Object = MibTableColumn
cpuAclL3Ip4Protocol = _CpuAclL3Ip4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 7),
    _CpuAclL3Ip4Protocol_Type()
)
cpuAclL3Ip4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4Protocol.setStatus("current")
_CpuAclL3Ip4ProtocolMask_Type = OctetString
_CpuAclL3Ip4ProtocolMask_Object = MibTableColumn
cpuAclL3Ip4ProtocolMask = _CpuAclL3Ip4ProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 8),
    _CpuAclL3Ip4ProtocolMask_Type()
)
cpuAclL3Ip4ProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4ProtocolMask.setStatus("current")


class _CpuAclL3Ip4IcmpTypeCheck_Type(Integer32):
    """Custom type cpuAclL3Ip4IcmpTypeCheck based on Integer32"""
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


_CpuAclL3Ip4IcmpTypeCheck_Type.__name__ = "Integer32"
_CpuAclL3Ip4IcmpTypeCheck_Object = MibTableColumn
cpuAclL3Ip4IcmpTypeCheck = _CpuAclL3Ip4IcmpTypeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 9),
    _CpuAclL3Ip4IcmpTypeCheck_Type()
)
cpuAclL3Ip4IcmpTypeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4IcmpTypeCheck.setStatus("current")


class _CpuAclL3Ip4IcmpCodeCheck_Type(Integer32):
    """Custom type cpuAclL3Ip4IcmpCodeCheck based on Integer32"""
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


_CpuAclL3Ip4IcmpCodeCheck_Type.__name__ = "Integer32"
_CpuAclL3Ip4IcmpCodeCheck_Object = MibTableColumn
cpuAclL3Ip4IcmpCodeCheck = _CpuAclL3Ip4IcmpCodeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 10),
    _CpuAclL3Ip4IcmpCodeCheck_Type()
)
cpuAclL3Ip4IcmpCodeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4IcmpCodeCheck.setStatus("current")


class _CpuAclL3Ip4IgmpTypeCheck_Type(Integer32):
    """Custom type cpuAclL3Ip4IgmpTypeCheck based on Integer32"""
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


_CpuAclL3Ip4IgmpTypeCheck_Type.__name__ = "Integer32"
_CpuAclL3Ip4IgmpTypeCheck_Object = MibTableColumn
cpuAclL3Ip4IgmpTypeCheck = _CpuAclL3Ip4IgmpTypeCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 11),
    _CpuAclL3Ip4IgmpTypeCheck_Type()
)
cpuAclL3Ip4IgmpTypeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4IgmpTypeCheck.setStatus("current")
_CpuAclL3Ip4SrcPortMask_Type = OctetString
_CpuAclL3Ip4SrcPortMask_Object = MibTableColumn
cpuAclL3Ip4SrcPortMask = _CpuAclL3Ip4SrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 12),
    _CpuAclL3Ip4SrcPortMask_Type()
)
cpuAclL3Ip4SrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4SrcPortMask.setStatus("current")
_CpuAclL3Ip4DstPortMask_Type = OctetString
_CpuAclL3Ip4DstPortMask_Object = MibTableColumn
cpuAclL3Ip4DstPortMask = _CpuAclL3Ip4DstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 13),
    _CpuAclL3Ip4DstPortMask_Type()
)
cpuAclL3Ip4DstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4DstPortMask.setStatus("current")


class _CpuAclL3Ip4TcpFlagCheck_Type(Integer32):
    """Custom type cpuAclL3Ip4TcpFlagCheck based on Integer32"""
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


_CpuAclL3Ip4TcpFlagCheck_Type.__name__ = "Integer32"
_CpuAclL3Ip4TcpFlagCheck_Object = MibTableColumn
cpuAclL3Ip4TcpFlagCheck = _CpuAclL3Ip4TcpFlagCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 14),
    _CpuAclL3Ip4TcpFlagCheck_Type()
)
cpuAclL3Ip4TcpFlagCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip4TcpFlagCheck.setStatus("current")
_CpuAclL3Ip6SrcAddrMask_Type = Ipv6Address
_CpuAclL3Ip6SrcAddrMask_Object = MibTableColumn
cpuAclL3Ip6SrcAddrMask = _CpuAclL3Ip6SrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 15),
    _CpuAclL3Ip6SrcAddrMask_Type()
)
cpuAclL3Ip6SrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip6SrcAddrMask.setStatus("current")
_CpuAclL3Ip6DstAddrMask_Type = Ipv6Address
_CpuAclL3Ip6DstAddrMask_Object = MibTableColumn
cpuAclL3Ip6DstAddrMask = _CpuAclL3Ip6DstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 16),
    _CpuAclL3Ip6DstAddrMask_Type()
)
cpuAclL3Ip6DstAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip6DstAddrMask.setStatus("current")


class _CpuAclL3Ip6TrafficClassCheck_Type(Integer32):
    """Custom type cpuAclL3Ip6TrafficClassCheck based on Integer32"""
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


_CpuAclL3Ip6TrafficClassCheck_Type.__name__ = "Integer32"
_CpuAclL3Ip6TrafficClassCheck_Object = MibTableColumn
cpuAclL3Ip6TrafficClassCheck = _CpuAclL3Ip6TrafficClassCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 17),
    _CpuAclL3Ip6TrafficClassCheck_Type()
)
cpuAclL3Ip6TrafficClassCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip6TrafficClassCheck.setStatus("current")
_CpuAclL3ProfileStatus_Type = RowStatus
_CpuAclL3ProfileStatus_Object = MibTableColumn
cpuAclL3ProfileStatus = _CpuAclL3ProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 1, 2, 1, 18),
    _CpuAclL3ProfileStatus_Type()
)
cpuAclL3ProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuAclL3ProfileStatus.setStatus("current")
_SysCpuAclRule_ObjectIdentity = ObjectIdentity
sysCpuAclRule = _SysCpuAclRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2)
)
_CpuAclL2RuleTable_Object = MibTable
cpuAclL2RuleTable = _CpuAclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1)
)
if mibBuilder.loadTexts:
    cpuAclL2RuleTable.setStatus("current")
_CpuAclL2RuleEntry_Object = MibTableRow
cpuAclL2RuleEntry = _CpuAclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1)
)
cpuAclL2RuleEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "cpuAclL2RuleProfileID"),
    (0, "DGS-1100-10ME_A1", "cpuAclL2RuleAccessID"),
)
if mibBuilder.loadTexts:
    cpuAclL2RuleEntry.setStatus("current")


class _CpuAclL2RuleProfileID_Type(Integer32):
    """Custom type cpuAclL2RuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuAclL2RuleProfileID_Type.__name__ = "Integer32"
_CpuAclL2RuleProfileID_Object = MibTableColumn
cpuAclL2RuleProfileID = _CpuAclL2RuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 1),
    _CpuAclL2RuleProfileID_Type()
)
cpuAclL2RuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL2RuleProfileID.setStatus("current")


class _CpuAclL2RuleAccessID_Type(Integer32):
    """Custom type cpuAclL2RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CpuAclL2RuleAccessID_Type.__name__ = "Integer32"
_CpuAclL2RuleAccessID_Object = MibTableColumn
cpuAclL2RuleAccessID = _CpuAclL2RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 2),
    _CpuAclL2RuleAccessID_Type()
)
cpuAclL2RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL2RuleAccessID.setStatus("current")


class _CpuAclL2VlanId_Type(Integer32):
    """Custom type cpuAclL2VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CpuAclL2VlanId_Type.__name__ = "Integer32"
_CpuAclL2VlanId_Object = MibTableColumn
cpuAclL2VlanId = _CpuAclL2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 3),
    _CpuAclL2VlanId_Type()
)
cpuAclL2VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2VlanId.setStatus("current")
_CpuAclL2SrcMac_Type = MacAddress
_CpuAclL2SrcMac_Object = MibTableColumn
cpuAclL2SrcMac = _CpuAclL2SrcMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 4),
    _CpuAclL2SrcMac_Type()
)
cpuAclL2SrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2SrcMac.setStatus("current")
_CpuAclL2DstMac_Type = MacAddress
_CpuAclL2DstMac_Object = MibTableColumn
cpuAclL2DstMac = _CpuAclL2DstMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 5),
    _CpuAclL2DstMac_Type()
)
cpuAclL2DstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2DstMac.setStatus("current")


class _CpuAclL28021p_Type(Integer32):
    """Custom type cpuAclL28021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_CpuAclL28021p_Type.__name__ = "Integer32"
_CpuAclL28021p_Object = MibTableColumn
cpuAclL28021p = _CpuAclL28021p_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 6),
    _CpuAclL28021p_Type()
)
cpuAclL28021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL28021p.setStatus("current")


class _CpuAclL2EtherType_Type(Unsigned32):
    """Custom type cpuAclL2EtherType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1501, 65535),
    )


_CpuAclL2EtherType_Type.__name__ = "Unsigned32"
_CpuAclL2EtherType_Object = MibTableColumn
cpuAclL2EtherType = _CpuAclL2EtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 7),
    _CpuAclL2EtherType_Type()
)
cpuAclL2EtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2EtherType.setStatus("current")
_CpuAclL2InPortList_Type = PortList
_CpuAclL2InPortList_Object = MibTableColumn
cpuAclL2InPortList = _CpuAclL2InPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 8),
    _CpuAclL2InPortList_Type()
)
cpuAclL2InPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2InPortList.setStatus("current")


class _CpuAclL2Action_Type(Integer32):
    """Custom type cpuAclL2Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("permit", 1))
    )


_CpuAclL2Action_Type.__name__ = "Integer32"
_CpuAclL2Action_Object = MibTableColumn
cpuAclL2Action = _CpuAclL2Action_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 9),
    _CpuAclL2Action_Type()
)
cpuAclL2Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL2Action.setStatus("current")
_CpuAclL2RuleStatus_Type = RowStatus
_CpuAclL2RuleStatus_Object = MibTableColumn
cpuAclL2RuleStatus = _CpuAclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 1, 1, 10),
    _CpuAclL2RuleStatus_Type()
)
cpuAclL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuAclL2RuleStatus.setStatus("current")
_CpuAclL3RuleTable_Object = MibTable
cpuAclL3RuleTable = _CpuAclL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2)
)
if mibBuilder.loadTexts:
    cpuAclL3RuleTable.setStatus("current")
_CpuAclL3RuleEntry_Object = MibTableRow
cpuAclL3RuleEntry = _CpuAclL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1)
)
cpuAclL3RuleEntry.setIndexNames(
    (0, "DGS-1100-10ME_A1", "cpuAclL3RuleProfileID"),
    (0, "DGS-1100-10ME_A1", "cpuAclL3RuleAccessID"),
)
if mibBuilder.loadTexts:
    cpuAclL3RuleEntry.setStatus("current")


class _CpuAclL3RuleProfileID_Type(Integer32):
    """Custom type cpuAclL3RuleProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuAclL3RuleProfileID_Type.__name__ = "Integer32"
_CpuAclL3RuleProfileID_Object = MibTableColumn
cpuAclL3RuleProfileID = _CpuAclL3RuleProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 1),
    _CpuAclL3RuleProfileID_Type()
)
cpuAclL3RuleProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL3RuleProfileID.setStatus("current")


class _CpuAclL3RuleAccessID_Type(Integer32):
    """Custom type cpuAclL3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CpuAclL3RuleAccessID_Type.__name__ = "Integer32"
_CpuAclL3RuleAccessID_Object = MibTableColumn
cpuAclL3RuleAccessID = _CpuAclL3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 2),
    _CpuAclL3RuleAccessID_Type()
)
cpuAclL3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclL3RuleAccessID.setStatus("current")
_CpuAclL3IP4SrcAddr_Type = IpAddress
_CpuAclL3IP4SrcAddr_Object = MibTableColumn
cpuAclL3IP4SrcAddr = _CpuAclL3IP4SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 3),
    _CpuAclL3IP4SrcAddr_Type()
)
cpuAclL3IP4SrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4SrcAddr.setStatus("current")
_CpuAclL3IP4DstAddr_Type = IpAddress
_CpuAclL3IP4DstAddr_Object = MibTableColumn
cpuAclL3IP4DstAddr = _CpuAclL3IP4DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 4),
    _CpuAclL3IP4DstAddr_Type()
)
cpuAclL3IP4DstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4DstAddr.setStatus("current")


class _CpuAclL3IP4DSCP_Type(Integer32):
    """Custom type cpuAclL3IP4DSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_CpuAclL3IP4DSCP_Type.__name__ = "Integer32"
_CpuAclL3IP4DSCP_Object = MibTableColumn
cpuAclL3IP4DSCP = _CpuAclL3IP4DSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 5),
    _CpuAclL3IP4DSCP_Type()
)
cpuAclL3IP4DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4DSCP.setStatus("current")


class _CpuAclL3IP4Protocol_Type(Integer32):
    """Custom type cpuAclL3IP4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpuAclL3IP4Protocol_Type.__name__ = "Integer32"
_CpuAclL3IP4Protocol_Object = MibTableColumn
cpuAclL3IP4Protocol = _CpuAclL3IP4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 6),
    _CpuAclL3IP4Protocol_Type()
)
cpuAclL3IP4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4Protocol.setStatus("current")
_CpuAclL3IP4IcmpType_Type = Integer32
_CpuAclL3IP4IcmpType_Object = MibTableColumn
cpuAclL3IP4IcmpType = _CpuAclL3IP4IcmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 7),
    _CpuAclL3IP4IcmpType_Type()
)
cpuAclL3IP4IcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4IcmpType.setStatus("current")
_CpuAclL3IP4IcmpCode_Type = Integer32
_CpuAclL3IP4IcmpCode_Object = MibTableColumn
cpuAclL3IP4IcmpCode = _CpuAclL3IP4IcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 8),
    _CpuAclL3IP4IcmpCode_Type()
)
cpuAclL3IP4IcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4IcmpCode.setStatus("current")
_CpuAclL3IP4IgmpType_Type = Integer32
_CpuAclL3IP4IgmpType_Object = MibTableColumn
cpuAclL3IP4IgmpType = _CpuAclL3IP4IgmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 9),
    _CpuAclL3IP4IgmpType_Type()
)
cpuAclL3IP4IgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4IgmpType.setStatus("current")


class _CpuAclL3IP4SrcPort_Type(Integer32):
    """Custom type cpuAclL3IP4SrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CpuAclL3IP4SrcPort_Type.__name__ = "Integer32"
_CpuAclL3IP4SrcPort_Object = MibTableColumn
cpuAclL3IP4SrcPort = _CpuAclL3IP4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 10),
    _CpuAclL3IP4SrcPort_Type()
)
cpuAclL3IP4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4SrcPort.setStatus("current")


class _CpuAclL3IP4DstPort_Type(Integer32):
    """Custom type cpuAclL3IP4DstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CpuAclL3IP4DstPort_Type.__name__ = "Integer32"
_CpuAclL3IP4DstPort_Object = MibTableColumn
cpuAclL3IP4DstPort = _CpuAclL3IP4DstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 11),
    _CpuAclL3IP4DstPort_Type()
)
cpuAclL3IP4DstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4DstPort.setStatus("current")


class _CpuAclL3IP4TcpFlagURG_Type(Integer32):
    """Custom type cpuAclL3IP4TcpFlagURG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_CpuAclL3IP4TcpFlagURG_Type.__name__ = "Integer32"
_CpuAclL3IP4TcpFlagURG_Object = MibTableColumn
cpuAclL3IP4TcpFlagURG = _CpuAclL3IP4TcpFlagURG_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 12),
    _CpuAclL3IP4TcpFlagURG_Type()
)
cpuAclL3IP4TcpFlagURG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4TcpFlagURG.setStatus("current")


class _CpuAclL3IP4TcpFlagACK_Type(Integer32):
    """Custom type cpuAclL3IP4TcpFlagACK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_CpuAclL3IP4TcpFlagACK_Type.__name__ = "Integer32"
_CpuAclL3IP4TcpFlagACK_Object = MibTableColumn
cpuAclL3IP4TcpFlagACK = _CpuAclL3IP4TcpFlagACK_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 13),
    _CpuAclL3IP4TcpFlagACK_Type()
)
cpuAclL3IP4TcpFlagACK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4TcpFlagACK.setStatus("current")


class _CpuAclL3IP4TcpFlagPSH_Type(Integer32):
    """Custom type cpuAclL3IP4TcpFlagPSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_CpuAclL3IP4TcpFlagPSH_Type.__name__ = "Integer32"
_CpuAclL3IP4TcpFlagPSH_Object = MibTableColumn
cpuAclL3IP4TcpFlagPSH = _CpuAclL3IP4TcpFlagPSH_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 14),
    _CpuAclL3IP4TcpFlagPSH_Type()
)
cpuAclL3IP4TcpFlagPSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4TcpFlagPSH.setStatus("current")


class _CpuAclL3IP4TcpFlagRST_Type(Integer32):
    """Custom type cpuAclL3IP4TcpFlagRST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_CpuAclL3IP4TcpFlagRST_Type.__name__ = "Integer32"
_CpuAclL3IP4TcpFlagRST_Object = MibTableColumn
cpuAclL3IP4TcpFlagRST = _CpuAclL3IP4TcpFlagRST_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 15),
    _CpuAclL3IP4TcpFlagRST_Type()
)
cpuAclL3IP4TcpFlagRST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4TcpFlagRST.setStatus("current")


class _CpuAclL3IP4TcpFlagSYN_Type(Integer32):
    """Custom type cpuAclL3IP4TcpFlagSYN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_CpuAclL3IP4TcpFlagSYN_Type.__name__ = "Integer32"
_CpuAclL3IP4TcpFlagSYN_Object = MibTableColumn
cpuAclL3IP4TcpFlagSYN = _CpuAclL3IP4TcpFlagSYN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 16),
    _CpuAclL3IP4TcpFlagSYN_Type()
)
cpuAclL3IP4TcpFlagSYN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4TcpFlagSYN.setStatus("current")


class _CpuAclL3IP4TcpFlagFIN_Type(Integer32):
    """Custom type cpuAclL3IP4TcpFlagFIN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("notSet", 2),
          ("set", 1))
    )


_CpuAclL3IP4TcpFlagFIN_Type.__name__ = "Integer32"
_CpuAclL3IP4TcpFlagFIN_Object = MibTableColumn
cpuAclL3IP4TcpFlagFIN = _CpuAclL3IP4TcpFlagFIN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 17),
    _CpuAclL3IP4TcpFlagFIN_Type()
)
cpuAclL3IP4TcpFlagFIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP4TcpFlagFIN.setStatus("current")
_CpuAclL3InPortList_Type = PortList
_CpuAclL3InPortList_Object = MibTableColumn
cpuAclL3InPortList = _CpuAclL3InPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 18),
    _CpuAclL3InPortList_Type()
)
cpuAclL3InPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3InPortList.setStatus("current")


class _CpuAclL3Action_Type(Integer32):
    """Custom type cpuAclL3Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("permit", 1))
    )


_CpuAclL3Action_Type.__name__ = "Integer32"
_CpuAclL3Action_Object = MibTableColumn
cpuAclL3Action = _CpuAclL3Action_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 19),
    _CpuAclL3Action_Type()
)
cpuAclL3Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Action.setStatus("current")
_CpuAclL3IP6SrcAddr_Type = Ipv6Address
_CpuAclL3IP6SrcAddr_Object = MibTableColumn
cpuAclL3IP6SrcAddr = _CpuAclL3IP6SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 20),
    _CpuAclL3IP6SrcAddr_Type()
)
cpuAclL3IP6SrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP6SrcAddr.setStatus("current")
_CpuAclL3IP6DstAddr_Type = Ipv6Address
_CpuAclL3IP6DstAddr_Object = MibTableColumn
cpuAclL3IP6DstAddr = _CpuAclL3IP6DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 21),
    _CpuAclL3IP6DstAddr_Type()
)
cpuAclL3IP6DstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3IP6DstAddr.setStatus("current")


class _CpuAclL3Ip6TrafficClass_Type(Integer32):
    """Custom type cpuAclL3Ip6TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CpuAclL3Ip6TrafficClass_Type.__name__ = "Integer32"
_CpuAclL3Ip6TrafficClass_Object = MibTableColumn
cpuAclL3Ip6TrafficClass = _CpuAclL3Ip6TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 22),
    _CpuAclL3Ip6TrafficClass_Type()
)
cpuAclL3Ip6TrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuAclL3Ip6TrafficClass.setStatus("current")
_CpuAclL3RuleStatus_Type = RowStatus
_CpuAclL3RuleStatus_Object = MibTableColumn
cpuAclL3RuleStatus = _CpuAclL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 2, 2, 1, 23),
    _CpuAclL3RuleStatus_Type()
)
cpuAclL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuAclL3RuleStatus.setStatus("current")
_SysCpuAclStatistic_ObjectIdentity = ObjectIdentity
sysCpuAclStatistic = _SysCpuAclStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 3)
)
_CpuAclTotalProfile_Type = Integer32
_CpuAclTotalProfile_Object = MibScalar
cpuAclTotalProfile = _CpuAclTotalProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 3, 1),
    _CpuAclTotalProfile_Type()
)
cpuAclTotalProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclTotalProfile.setStatus("current")
_CpuAclUsedProfile_Type = Integer32
_CpuAclUsedProfile_Object = MibScalar
cpuAclUsedProfile = _CpuAclUsedProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 3, 2),
    _CpuAclUsedProfile_Type()
)
cpuAclUsedProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclUsedProfile.setStatus("current")
_CpuAclTotalRule_Type = Integer32
_CpuAclTotalRule_Object = MibScalar
cpuAclTotalRule = _CpuAclTotalRule_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 3, 3),
    _CpuAclTotalRule_Type()
)
cpuAclTotalRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclTotalRule.setStatus("current")
_CpuAclUsedRule_Type = Integer32
_CpuAclUsedRule_Object = MibScalar
cpuAclUsedRule = _CpuAclUsedRule_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 104, 3, 4),
    _CpuAclUsedRule_Type()
)
cpuAclUsedRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuAclUsedRule.setStatus("current")

# Managed Objects groups


# Notification objects

ipifDuplicateIPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ipifDuplicateIPDetected.setStatus(
        "current"
    )

sysFimwareupgradesuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 4, 0, 1)
)
if mibBuilder.loadTexts:
    sysFimwareupgradesuccess.setStatus(
        "current"
    )

sysFimwareillegalfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 4, 0, 2)
)
if mibBuilder.loadTexts:
    sysFimwareillegalfile.setStatus(
        "current"
    )

sysFimwarefiletransferfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 4, 0, 3)
)
if mibBuilder.loadTexts:
    sysFimwarefiletransferfailed.setStatus(
        "current"
    )

sysFimwarewrongchecksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 4, 0, 4)
)
if mibBuilder.loadTexts:
    sysFimwarewrongchecksum.setStatus(
        "current"
    )

sysFimwareuupgradefailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 3, 4, 0, 5)
)
if mibBuilder.loadTexts:
    sysFimwareuupgradefailed.setStatus(
        "current"
    )

stormOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 5, 0, 1)
)
stormOccurred.setObjects(
      *(("DGS-1100-10ME_A1", "trafficCtrlIndex"),
        ("DGS-1100-10ME_A1", "trafficCtrlType"))
)
if mibBuilder.loadTexts:
    stormOccurred.setStatus(
        "current"
    )

stormCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 13, 5, 0, 2)
)
stormCleared.setObjects(
      *(("DGS-1100-10ME_A1", "trafficCtrlIndex"),
        ("DGS-1100-10ME_A1", "trafficCtrlTimeInterval"))
)
if mibBuilder.loadTexts:
    stormCleared.setStatus(
        "current"
    )

portSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 14, 12, 0, 1)
)
portSecurityViolation.setObjects(
      *(("DGS-1100-10ME_A1", "portSecurityIndex"),
        ("DGS-1100-10ME_A1", "portSecurityMLA"))
)
if mibBuilder.loadTexts:
    portSecurityViolation.setStatus(
        "current"
    )

loopbackOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 8, 0, 1)
)
loopbackOccur.setObjects(
      *(("DGS-1100-10ME_A1", "sysLBDCtrlIndex"),
        ("DGS-1100-10ME_A1", "sysLBDPortLoopStatus"))
)
if mibBuilder.loadTexts:
    loopbackOccur.setStatus(
        "current"
    )

loopbackRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 17, 8, 0, 2)
)
loopbackRecovery.setObjects(
      *(("DGS-1100-10ME_A1", "sysLBDCtrlIndex"),
        ("DGS-1100-10ME_A1", "sysLBDRecoverTime"))
)
if mibBuilder.loadTexts:
    loopbackRecovery.setStatus(
        "current"
    )

fdbTableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 25, 5, 1)
)
fdbTableChanged.setObjects(
      *(("DGS-1100-10ME_A1", "portSecFDBPermVlanID"),
        ("DGS-1100-10ME_A1", "portSecFDBPermMac"),
        ("DGS-1100-10ME_A1", "portSecFDBPermPort"))
)
if mibBuilder.loadTexts:
    fdbTableChanged.setStatus(
        "current"
    )

lldpRemTablesChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 1)
)
lldpRemTablesChange.setObjects(
      *(("DGS-1100-10ME_A1", "lldpStatsRemTablesInserts"),
        ("DGS-1100-10ME_A1", "lldpStatsRemTablesDeletes"),
        ("DGS-1100-10ME_A1", "lldpStatsRemTablesDrops"),
        ("DGS-1100-10ME_A1", "lldpStatsRemTablesAgeouts"))
)
if mibBuilder.loadTexts:
    lldpRemTablesChange.setStatus(
        "current"
    )

lldpExceedsMaxFrameSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 2)
)
lldpExceedsMaxFrameSize.setObjects(
    ("DGS-1100-10ME_A1", "lldpLocPortId")
)
if mibBuilder.loadTexts:
    lldpExceedsMaxFrameSize.setStatus(
        "current"
    )

lldpDupChasisId = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 3)
)
lldpDupChasisId.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"))
)
if mibBuilder.loadTexts:
    lldpDupChasisId.setStatus(
        "current"
    )

lldpDupSystemName = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 4)
)
lldpDupSystemName.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"),
        ("DGS-1100-10ME_A1", "lldpRemSysName"))
)
if mibBuilder.loadTexts:
    lldpDupSystemName.setStatus(
        "current"
    )

lldpDupManagmentAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 5)
)
lldpDupManagmentAddress.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"),
        ("DGS-1100-10ME_A1", "lldpRemManAddrIfId"))
)
if mibBuilder.loadTexts:
    lldpDupManagmentAddress.setStatus(
        "current"
    )

lldpMisConfigPortVlanID = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 6)
)
lldpMisConfigPortVlanID.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"),
        ("DGS-1100-10ME_A1", "lldpXdot1RemPortVlanId"))
)
if mibBuilder.loadTexts:
    lldpMisConfigPortVlanID.setStatus(
        "current"
    )

lldpMisConfigVlanName = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 8)
)
lldpMisConfigVlanName.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"),
        ("DGS-1100-10ME_A1", "lldpXdot1RemVlanName"))
)
if mibBuilder.loadTexts:
    lldpMisConfigVlanName.setStatus(
        "current"
    )

lldpMisConfigProtocolIdentity = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 9)
)
lldpMisConfigProtocolIdentity.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"),
        ("DGS-1100-10ME_A1", "lldpXdot1RemProtocolId"))
)
if mibBuilder.loadTexts:
    lldpMisConfigProtocolIdentity.setStatus(
        "current"
    )

lldpMisConfigMaxFrameSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 12)
)
lldpMisConfigMaxFrameSize.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"),
        ("DGS-1100-10ME_A1", "lldpXdot3RemMaxFrameSize"))
)
if mibBuilder.loadTexts:
    lldpMisConfigMaxFrameSize.setStatus(
        "current"
    )

lldpMisConfigOperMauType = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 32, 17, 0, 13)
)
lldpMisConfigOperMauType.setObjects(
      *(("DGS-1100-10ME_A1", "lldpRemChassisId"),
        ("DGS-1100-10ME_A1", "lldpRemPortId"),
        ("DGS-1100-10ME_A1", "lldpXdot3RemPortOperMauType"))
)
if mibBuilder.loadTexts:
    lldpMisConfigOperMauType.setStatus(
        "current"
    )

eoamNotifyThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 5, 0, 1)
)
eoamNotifyThresholdEvent.setObjects(
      *(("DGS-1100-10ME_A1", "eoamEventLogPort"),
        ("DGS-1100-10ME_A1", "eoamEventLogTimestamp"),
        ("DGS-1100-10ME_A1", "eoamEventLogType"),
        ("DGS-1100-10ME_A1", "eoamEventLogLocation"),
        ("DGS-1100-10ME_A1", "eoamEventLogValue"),
        ("DGS-1100-10ME_A1", "eoamEventLogWindow"),
        ("DGS-1100-10ME_A1", "eoamEventLogThreshold"),
        ("DGS-1100-10ME_A1", "eoamEventLogAccError"))
)
if mibBuilder.loadTexts:
    eoamNotifyThresholdEvent.setStatus(
        "current"
    )

eoamNotifyNonThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 2, 1, 51, 5, 0, 2)
)
eoamNotifyNonThresholdEvent.setObjects(
      *(("DGS-1100-10ME_A1", "eoamEventLogPort"),
        ("DGS-1100-10ME_A1", "eoamEventLogTimestamp"),
        ("DGS-1100-10ME_A1", "eoamEventLogType"),
        ("DGS-1100-10ME_A1", "eoamEventLogLocation"),
        ("DGS-1100-10ME_A1", "eoamEventLogAccError"))
)
if mibBuilder.loadTexts:
    eoamNotifyNonThresholdEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-1100-10ME_A1",
    **{"VlanIndex": VlanIndex,
       "PortList": PortList,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "OwnerString": OwnerString,
       "RmonStatus": RmonStatus,
       "OperationResponseStatus": OperationResponseStatus,
       "LldpChassisIdSubtype": LldpChassisIdSubtype,
       "LldpChassisId": LldpChassisId,
       "LldpPortIdSubtype": LldpPortIdSubtype,
       "LldpPortId": LldpPortId,
       "LldpManAddrIfSubtype": LldpManAddrIfSubtype,
       "LldpManAddress": LldpManAddress,
       "LldpSystemCapabilitiesMap": LldpSystemCapabilitiesMap,
       "LldpPortNumber": LldpPortNumber,
       "LldpPortList": LldpPortList,
       "TimeFilter": TimeFilter,
       "LldpPowerPortClass": LldpPowerPortClass,
       "LldpLinkAggStatusMap": LldpLinkAggStatusMap,
       "ZeroBasedCounter32": ZeroBasedCounter32,
       "Ipv6Address": Ipv6Address,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DGS1100SeriesProd": dlink_DGS1100SeriesProd,
       "dgs-1100-10ME": dgs_1100_10ME,
       "dgs-1100-10ME_A1": dgs_1100_10ME_A1,
       "companySystem": companySystem,
       "sysDevInfo": sysDevInfo,
       "sysSwitchName": sysSwitchName,
       "sysHardwareVersion": sysHardwareVersion,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysDeviceType": sysDeviceType,
       "sysBootVerion": sysBootVerion,
       "sysLoginTimeout": sysLoginTimeout,
       "sysLocationName": sysLocationName,
       "sysContact": sysContact,
       "sysSafeGuardEnable": sysSafeGuardEnable,
       "sysRestart": sysRestart,
       "sysSave": sysSave,
       "sysJumboFrameEnable": sysJumboFrameEnable,
       "sysDhcpAutoConfiguration": sysDhcpAutoConfiguration,
       "sysWebState": sysWebState,
       "sysWebPortNumber": sysWebPortNumber,
       "sysARPAgingTime": sysARPAgingTime,
       "sysMACAgingTime": sysMACAgingTime,
       "sysTelnetsettingManagementOnOff": sysTelnetsettingManagementOnOff,
       "sysTelnetUDPPort": sysTelnetUDPPort,
       "sysAutoRefreshConfiguration": sysAutoRefreshConfiguration,
       "sysMacAddr": sysMacAddr,
       "sysSwitchTime": sysSwitchTime,
       "sysDhcpTimeout": sysDhcpTimeout,
       "sysSerialNumber": sysSerialNumber,
       "sysCPU": sysCPU,
       "cpuLast5SecUsage": cpuLast5SecUsage,
       "cpuLast1MinUsage": cpuLast1MinUsage,
       "cpuLast5MinUsage": cpuLast5MinUsage,
       "sysRAM": sysRAM,
       "ramLast5SecUsage": ramLast5SecUsage,
       "ramLast1MinUsage": ramLast1MinUsage,
       "ramLast5MinUsage": ramLast5MinUsage,
       "sysCliPromptStr": sysCliPromptStr,
       "sysSshState": sysSshState,
       "sysSshPortNumber": sysSshPortNumber,
       "sysPort": sysPort,
       "portCtrlTable": portCtrlTable,
       "portCtrlEntry": portCtrlEntry,
       "portCtrlIndex": portCtrlIndex,
       "portCtrlMediumType": portCtrlMediumType,
       "portCtrlSpeed": portCtrlSpeed,
       "portCtrlLinkStatus": portCtrlLinkStatus,
       "portCtrlMDI": portCtrlMDI,
       "portCtrlFlowControl": portCtrlFlowControl,
       "portCtrlFlowControlOper": portCtrlFlowControlOper,
       "portCtrlAdminState": portCtrlAdminState,
       "portCtrlDetailMediumType": portCtrlDetailMediumType,
       "portCtrlDynamicMacAutoLearn": portCtrlDynamicMacAutoLearn,
       "portDescriptionTable": portDescriptionTable,
       "portDescriptionEntry": portDescriptionEntry,
       "portDescIndex": portDescIndex,
       "portDescMediumType": portDescMediumType,
       "portDescString": portDescString,
       "portErrTable": portErrTable,
       "portErrEntry": portErrEntry,
       "portErrPortIndex": portErrPortIndex,
       "portErrPortState": portErrPortState,
       "portErrPortStatus": portErrPortStatus,
       "portErrPortReason": portErrPortReason,
       "portUtilizTable": portUtilizTable,
       "portUtilizEntry": portUtilizEntry,
       "portUtilizIndex": portUtilizIndex,
       "portUtilizTX": portUtilizTX,
       "portUtilizRX": portUtilizRX,
       "portUtilizAverage": portUtilizAverage,
       "companyIpifGroup": companyIpifGroup,
       "sysIpifSupportV4V6Info": sysIpifSupportV4V6Info,
       "ipv4AddrCfgMode": ipv4AddrCfgMode,
       "ipv4Address": ipv4Address,
       "ipv4SubnetMask": ipv4SubnetMask,
       "ipv4DefaultGateway": ipv4DefaultGateway,
       "dhcpOption12Status": dhcpOption12Status,
       "dhcpOption12HostName": dhcpOption12HostName,
       "ipv6GlobalStatus": ipv6GlobalStatus,
       "ipv6DHCPStatus": ipv6DHCPStatus,
       "ipv6AutolinkloStatus": ipv6AutolinkloStatus,
       "ipv6NSRetransmitTime": ipv6NSRetransmitTime,
       "ipv6DefaultRouteTable": ipv6DefaultRouteTable,
       "ipv6DefaultRouteEntry": ipv6DefaultRouteEntry,
       "ipv6DefaultRouteProtocol": ipv6DefaultRouteProtocol,
       "ipv6DefaultRouteNextHop": ipv6DefaultRouteNextHop,
       "ipv6DefaultRouteIfIndex": ipv6DefaultRouteIfIndex,
       "ipv6DefaultRouteMetric": ipv6DefaultRouteMetric,
       "ipv6DefaultRouteAdminStatus": ipv6DefaultRouteAdminStatus,
       "ipv6AddressTable": ipv6AddressTable,
       "ipv6AddressEntry": ipv6AddressEntry,
       "ipv6AddressMainIndex": ipv6AddressMainIndex,
       "ipv6AddressIpAddr": ipv6AddressIpAddr,
       "ipv6AddressIpPrefix": ipv6AddressIpPrefix,
       "ipv6AddressIpType": ipv6AddressIpType,
       "ipv6AddressRowStatus": ipv6AddressRowStatus,
       "dhcpRetryCount": dhcpRetryCount,
       "sysIpifTraps": sysIpifTraps,
       "ipifDuplicateIPDetected": ipifDuplicateIPDetected,
       "companyTftpGroup": companyTftpGroup,
       "sysTftpFwTargetGroup": sysTftpFwTargetGroup,
       "tftpFwTargetServerIpAddress": tftpFwTargetServerIpAddress,
       "tftpFwTargetServerIpType": tftpFwTargetServerIpType,
       "tftpFwTargetInterfaceName": tftpFwTargetInterfaceName,
       "tftpFwTargetImageFileName": tftpFwTargetImageFileName,
       "tftpFwTargetTftpOperation": tftpFwTargetTftpOperation,
       "tftpFwTargetTftpOperationStatus": tftpFwTargetTftpOperationStatus,
       "tftpFwTargetTransferPercentage": tftpFwTargetTransferPercentage,
       "sysTftpCfgTargetGroup": sysTftpCfgTargetGroup,
       "tftpCfgTargetServerIpAddress": tftpCfgTargetServerIpAddress,
       "tftpCfgTargetServerIpType": tftpCfgTargetServerIpType,
       "tftpCfgTargetInterfaceName": tftpCfgTargetInterfaceName,
       "tftpCfgTargetImageFileName": tftpCfgTargetImageFileName,
       "tftpCfgTargetTftpOperation": tftpCfgTargetTftpOperation,
       "tftpCfgTargetTftpOperationStatus": tftpCfgTargetTftpOperationStatus,
       "sysTftpSyslogTargetGroup": sysTftpSyslogTargetGroup,
       "syslogFileSave": syslogFileSave,
       "tftpSyslogTargetServerIpAddress": tftpSyslogTargetServerIpAddress,
       "tftpSyslogTargetServerIpType": tftpSyslogTargetServerIpType,
       "tftpSyslogTargetInterfaceName": tftpSyslogTargetInterfaceName,
       "tftpSyslogTargetImageFileName": tftpSyslogTargetImageFileName,
       "tftpSyslogTargetTftpOperation": tftpSyslogTargetTftpOperation,
       "tftpSyslogTargetTftpOperationStatus": tftpSyslogTargetTftpOperationStatus,
       "tftpSyslogTargetTftpTransferPercentage": tftpSyslogTargetTftpTransferPercentage,
       "sysTftpTrapGroup": sysTftpTrapGroup,
       "sysFimwareTraps": sysFimwareTraps,
       "sysFimwareupgradesuccess": sysFimwareupgradesuccess,
       "sysFimwareillegalfile": sysFimwareillegalfile,
       "sysFimwarefiletransferfailed": sysFimwarefiletransferfailed,
       "sysFimwarewrongchecksum": sysFimwarewrongchecksum,
       "sysFimwareuupgradefailed": sysFimwareuupgradefailed,
       "companyUserAccount": companyUserAccount,
       "sysUserAccount": sysUserAccount,
       "adminUserTable": adminUserTable,
       "adminUserEntry": adminUserEntry,
       "userName": userName,
       "userPassword": userPassword,
       "userAccessRight": userAccessRight,
       "userEncrypt": userEncrypt,
       "userEncryptControl": userEncryptControl,
       "userRowStatus": userRowStatus,
       "sysPasswordEncrypt": sysPasswordEncrypt,
       "companySNMP": companySNMP,
       "sysSNMPGlobalState": sysSNMPGlobalState,
       "sysSNMPUser": sysSNMPUser,
       "snmpUserTable": snmpUserTable,
       "snmpUserEntry": snmpUserEntry,
       "snmpUserName": snmpUserName,
       "snmpUserVersion": snmpUserVersion,
       "snmpUserGroupName": snmpUserGroupName,
       "snmpUserAuthProtocol": snmpUserAuthProtocol,
       "snmpUserAuthProtocolPassword": snmpUserAuthProtocolPassword,
       "snmpUserPrivProtocol": snmpUserPrivProtocol,
       "snmpUserPrivProtocolPassword": snmpUserPrivProtocolPassword,
       "snmpUserStatus": snmpUserStatus,
       "sysSNMPGroup": sysSNMPGroup,
       "snmpGroupTable": snmpGroupTable,
       "snmpGroupEntry": snmpGroupEntry,
       "snmpGroupName": snmpGroupName,
       "snmpGroupSecurityModel": snmpGroupSecurityModel,
       "snmpGroupSecurityLevel": snmpGroupSecurityLevel,
       "snmpGroupReadViewName": snmpGroupReadViewName,
       "snmpGroupWriteViewName": snmpGroupWriteViewName,
       "snmpGroupNotifyViewName": snmpGroupNotifyViewName,
       "snmpGroupStatus": snmpGroupStatus,
       "sysSNMPViewTree": sysSNMPViewTree,
       "snmpViewTreeTable": snmpViewTreeTable,
       "snmpViewTreeEntry": snmpViewTreeEntry,
       "snmpViewTreeName": snmpViewTreeName,
       "snmpViewTreeSubtree": snmpViewTreeSubtree,
       "snmpViewTreeMask": snmpViewTreeMask,
       "snmpViewTreeType": snmpViewTreeType,
       "snmpViewTreeStatus": snmpViewTreeStatus,
       "sysSNMPCommunity": sysSNMPCommunity,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityName": snmpCommunityName,
       "snmpCommunityPolicy": snmpCommunityPolicy,
       "snmpCommunityStatus": snmpCommunityStatus,
       "sysSNMPHost": sysSNMPHost,
       "snmpHostTable": snmpHostTable,
       "snmpHostEntry": snmpHostEntry,
       "snmpHostAddress": snmpHostAddress,
       "snmpHostIPType": snmpHostIPType,
       "snmpHostCommunityName": snmpHostCommunityName,
       "snmpHostVersion": snmpHostVersion,
       "snmpHostStatus": snmpHostStatus,
       "sysSNMPEngineID": sysSNMPEngineID,
       "sysSNMPTrap": sysSNMPTrap,
       "snmpTrapSNMPAuthentication": snmpTrapSNMPAuthentication,
       "snmpTrapColdStart": snmpTrapColdStart,
       "snmpTrapWarmStart": snmpTrapWarmStart,
       "snmpTrapFiberLinkUpDown": snmpTrapFiberLinkUpDown,
       "snmpTrapTwistLinkUpDown": snmpTrapTwistLinkUpDown,
       "snmpTrapFirmwareUpgrade": snmpTrapFirmwareUpgrade,
       "snmpTrapPortSecViolation": snmpTrapPortSecViolation,
       "snmpTrapLBDDetection": snmpTrapLBDDetection,
       "snmpTrapDuplicateIPDetected": snmpTrapDuplicateIPDetected,
       "companyDot1qVlanGroup": companyDot1qVlanGroup,
       "sysDot1qVlanManagementOnOff": sysDot1qVlanManagementOnOff,
       "sysDot1qVlanManagementid": sysDot1qVlanManagementid,
       "sysDot1qPVIDAutoAssign": sysDot1qPVIDAutoAssign,
       "sysDot1qVlanAsyOnOff": sysDot1qVlanAsyOnOff,
       "sysDot1qVlanTable": sysDot1qVlanTable,
       "dot1qVlanEntry": dot1qVlanEntry,
       "dot1qVlanid": dot1qVlanid,
       "dot1qVlanName": dot1qVlanName,
       "dot1qVlanEgressPorts": dot1qVlanEgressPorts,
       "dot1qVlanUntaggedPorts": dot1qVlanUntaggedPorts,
       "dot1qVlanRowStatus": dot1qVlanRowStatus,
       "sysDot1qVlanPortTable": sysDot1qVlanPortTable,
       "dot1qVlanPortEntry": dot1qVlanPortEntry,
       "dot1qVlanPortIndex": dot1qVlanPortIndex,
       "dot1qVlanPortVlanId": dot1qVlanPortVlanId,
       "companyStaticMac": companyStaticMac,
       "sysStaticMacTable": sysStaticMacTable,
       "staticMacEntry": staticMacEntry,
       "staticMacVlanID": staticMacVlanID,
       "staticMacAddr": staticMacAddr,
       "staticMacPort": staticMacPort,
       "staticMacStatus": staticMacStatus,
       "sysDynamicFdbTable": sysDynamicFdbTable,
       "sysDynamicFdbEntry": sysDynamicFdbEntry,
       "dynamicFdbId": dynamicFdbId,
       "dynamicFdbMacAddr": dynamicFdbMacAddr,
       "dynamicFdbPort": dynamicFdbPort,
       "dynamicFdbStatus": dynamicFdbStatus,
       "sysFdbClear": sysFdbClear,
       "sysFdbClearId": sysFdbClearId,
       "sysFdbClearAction": sysFdbClearAction,
       "companyIgsGroup": companyIgsGroup,
       "sysIgsSystem": sysIgsSystem,
       "igsStatus": igsStatus,
       "igsReportForwardRouterOnly": igsReportForwardRouterOnly,
       "sysIgsVlan": sysIgsVlan,
       "igsVlanRouterTable": igsVlanRouterTable,
       "igsVlanRouterEntry": igsVlanRouterEntry,
       "igsVlanRouterVlanId": igsVlanRouterVlanId,
       "igsVlanRouterStaticPortList": igsVlanRouterStaticPortList,
       "igsVlanRouterDynamicPortList": igsVlanRouterDynamicPortList,
       "igsVlanFilterTable": igsVlanFilterTable,
       "igsVlanFilterEntry": igsVlanFilterEntry,
       "igsVlanFilterVlanId": igsVlanFilterVlanId,
       "igsVlanSnoopStatus": igsVlanSnoopStatus,
       "igsVlanQuerier": igsVlanQuerier,
       "igsVlanCfgQuerier": igsVlanCfgQuerier,
       "igsVlanQueryInterval": igsVlanQueryInterval,
       "igsVlanFastLeave": igsVlanFastLeave,
       "igsVlanQuerierVersion": igsVlanQuerierVersion,
       "igsVlanRouterPortPurgeInterval": igsVlanRouterPortPurgeInterval,
       "igsVlanHostPortPurgeInterval": igsVlanHostPortPurgeInterval,
       "igsVlanRobustnessValue": igsVlanRobustnessValue,
       "igsVlanGrpQueryInterval": igsVlanGrpQueryInterval,
       "igsVlanQueryMaxResponseTime": igsVlanQueryMaxResponseTime,
       "igsVlanMulticastGroupTable": igsVlanMulticastGroupTable,
       "igsVlanMulticastGroupEntry": igsVlanMulticastGroupEntry,
       "igsVlanMulticastGroupVlanId": igsVlanMulticastGroupVlanId,
       "igsVlanMulticastGroupIpAddress": igsVlanMulticastGroupIpAddress,
       "igsVlanMulticastGroupMacAddress": igsVlanMulticastGroupMacAddress,
       "igsVlanMulticastGroupPortList": igsVlanMulticastGroupPortList,
       "sysIgsAccessAuth": sysIgsAccessAuth,
       "igsAccessAuthTable": igsAccessAuthTable,
       "igsAccessAuthEntry": igsAccessAuthEntry,
       "igsAccessAuthPortIndex": igsAccessAuthPortIndex,
       "igsAccessAuthState": igsAccessAuthState,
       "sysIgsHost": sysIgsHost,
       "igsHostTable": igsHostTable,
       "igsHostEntry": igsHostEntry,
       "igsHostTableVlanId": igsHostTableVlanId,
       "igsHostTableGroupAddress": igsHostTableGroupAddress,
       "igsHostTablePort": igsHostTablePort,
       "igsHostTableHostIPAddress": igsHostTableHostIPAddress,
       "companyQoSGroup": companyQoSGroup,
       "sysQosMode": sysQosMode,
       "sysQosQueuingMechanism": sysQosQueuingMechanism,
       "sysQosPortBase": sysQosPortBase,
       "qosPortBaseTable": qosPortBaseTable,
       "qosPortBaseEntry": qosPortBaseEntry,
       "qosPortBasePortIndex": qosPortBasePortIndex,
       "qosPortBasePriority": qosPortBasePriority,
       "qosPortBaseEffectivePriority": qosPortBaseEffectivePriority,
       "sysQos1p": sysQos1p,
       "qosTrafficClassTable": qosTrafficClassTable,
       "qosTrafficClassEntry": qosTrafficClassEntry,
       "qosTrafficClassPriority": qosTrafficClassPriority,
       "qosTrafficClass": qosTrafficClass,
       "sysQosScheduling": sysQosScheduling,
       "qosSchedulingClassTable": qosSchedulingClassTable,
       "qosSchedulingClassEntry": qosSchedulingClassEntry,
       "qosSchedulingClassIndex": qosSchedulingClassIndex,
       "qosSchedulingWeight": qosSchedulingWeight,
       "sysQosDiffServ": sysQosDiffServ,
       "qosDiffServTypeGroup": qosDiffServTypeGroup,
       "qosDiffServType00": qosDiffServType00,
       "qosDiffServType01": qosDiffServType01,
       "qosDiffServType02": qosDiffServType02,
       "qosDiffServType03": qosDiffServType03,
       "qosDiffServType04": qosDiffServType04,
       "qosDiffServType05": qosDiffServType05,
       "qosDiffServType06": qosDiffServType06,
       "qosDiffServType07": qosDiffServType07,
       "qosDiffServType08": qosDiffServType08,
       "qosDiffServType09": qosDiffServType09,
       "qosDiffServType10": qosDiffServType10,
       "qosDiffServType11": qosDiffServType11,
       "qosDiffServType12": qosDiffServType12,
       "qosDiffServType13": qosDiffServType13,
       "qosDiffServType14": qosDiffServType14,
       "qosDiffServType15": qosDiffServType15,
       "qosDiffServType16": qosDiffServType16,
       "qosDiffServType17": qosDiffServType17,
       "qosDiffServType18": qosDiffServType18,
       "qosDiffServType19": qosDiffServType19,
       "qosDiffServType20": qosDiffServType20,
       "qosDiffServType21": qosDiffServType21,
       "qosDiffServType22": qosDiffServType22,
       "qosDiffServType23": qosDiffServType23,
       "qosDiffServType24": qosDiffServType24,
       "qosDiffServType25": qosDiffServType25,
       "qosDiffServType26": qosDiffServType26,
       "qosDiffServType27": qosDiffServType27,
       "qosDiffServType28": qosDiffServType28,
       "qosDiffServType29": qosDiffServType29,
       "qosDiffServType30": qosDiffServType30,
       "qosDiffServType31": qosDiffServType31,
       "qosDiffServType32": qosDiffServType32,
       "qosDiffServType33": qosDiffServType33,
       "qosDiffServType34": qosDiffServType34,
       "qosDiffServType35": qosDiffServType35,
       "qosDiffServType36": qosDiffServType36,
       "qosDiffServType37": qosDiffServType37,
       "qosDiffServType38": qosDiffServType38,
       "qosDiffServType39": qosDiffServType39,
       "qosDiffServType40": qosDiffServType40,
       "qosDiffServType41": qosDiffServType41,
       "qosDiffServType42": qosDiffServType42,
       "qosDiffServType43": qosDiffServType43,
       "qosDiffServType44": qosDiffServType44,
       "qosDiffServType45": qosDiffServType45,
       "qosDiffServType46": qosDiffServType46,
       "qosDiffServType47": qosDiffServType47,
       "qosDiffServType48": qosDiffServType48,
       "qosDiffServType49": qosDiffServType49,
       "qosDiffServType50": qosDiffServType50,
       "qosDiffServType51": qosDiffServType51,
       "qosDiffServType52": qosDiffServType52,
       "qosDiffServType53": qosDiffServType53,
       "qosDiffServType54": qosDiffServType54,
       "qosDiffServType55": qosDiffServType55,
       "qosDiffServType56": qosDiffServType56,
       "qosDiffServType57": qosDiffServType57,
       "qosDiffServType58": qosDiffServType58,
       "qosDiffServType59": qosDiffServType59,
       "qosDiffServType60": qosDiffServType60,
       "qosDiffServType61": qosDiffServType61,
       "qosDiffServType62": qosDiffServType62,
       "qosDiffServType63": qosDiffServType63,
       "companyTrafficMgmt": companyTrafficMgmt,
       "sysBandwidthCtrlSettings": sysBandwidthCtrlSettings,
       "bandwidthCtrlTable": bandwidthCtrlTable,
       "bandwidthCtrlEntry": bandwidthCtrlEntry,
       "bandwidthCtrlIndex": bandwidthCtrlIndex,
       "bandwidthCtrlTxThreshold": bandwidthCtrlTxThreshold,
       "bandwidthCtrlEffectiveTxThreshold": bandwidthCtrlEffectiveTxThreshold,
       "bandwidthCtrlRxThreshold": bandwidthCtrlRxThreshold,
       "bandwidthCtrlEffectiveRxThreshold": bandwidthCtrlEffectiveRxThreshold,
       "sysTrafficCtrlSettings": sysTrafficCtrlSettings,
       "trafficCtrlTrap": trafficCtrlTrap,
       "trafficCtrlTable": trafficCtrlTable,
       "trafficCtrlEntry": trafficCtrlEntry,
       "trafficCtrlIndex": trafficCtrlIndex,
       "trafficCtrlActionMode": trafficCtrlActionMode,
       "trafficCtrlType": trafficCtrlType,
       "trafficCtrlThreshold": trafficCtrlThreshold,
       "trafficCtrlCountDown": trafficCtrlCountDown,
       "trafficCtrlTimeInterval": trafficCtrlTimeInterval,
       "trafficCtrlPortState": trafficCtrlPortState,
       "sysStormCtrlTrap": sysStormCtrlTrap,
       "stormCtrlTrap": stormCtrlTrap,
       "stormOccurred": stormOccurred,
       "stormCleared": stormCleared,
       "companySecurity": companySecurity,
       "sysPortSecurity": sysPortSecurity,
       "portSecurityTable": portSecurityTable,
       "portSecurityEntry": portSecurityEntry,
       "portSecurityIndex": portSecurityIndex,
       "portSecurityState": portSecurityState,
       "portSecurityMLA": portSecurityMLA,
       "portSecurityLockAddrMode": portSecurityLockAddrMode,
       "portSecFDBPermanentTable": portSecFDBPermanentTable,
       "portSecFDBPermanentEntry": portSecFDBPermanentEntry,
       "portSecFDBPermVlanID": portSecFDBPermVlanID,
       "portSecFDBPermMac": portSecFDBPermMac,
       "portSecFDBPermPort": portSecFDBPermPort,
       "portSecFDBPermType": portSecFDBPermType,
       "portSecFDBPermEntryState": portSecFDBPermEntryState,
       "sysTrafficSegmentation": sysTrafficSegmentation,
       "trafficSegmentationTable": trafficSegmentationTable,
       "trafficSegmentationEntry": trafficSegmentationEntry,
       "trafficSegmentationIfIndex": trafficSegmentationIfIndex,
       "trafficSegmentationMemberList": trafficSegmentationMemberList,
       "sysSecurityAAC": sysSecurityAAC,
       "aacAuthenAdminState": aacAuthenAdminState,
       "aacAuthParamResponseTimeout": aacAuthParamResponseTimeout,
       "aacAuthParamAttempt": aacAuthParamAttempt,
       "aacLocalEnablePassword": aacLocalEnablePassword,
       "aacAPAuthMethodGroup": aacAPAuthMethodGroup,
       "aacAPLoginMethod": aacAPLoginMethod,
       "aacAPTelnetLoginMethod": aacAPTelnetLoginMethod,
       "aacAPHttpLoginMethod": aacAPHttpLoginMethod,
       "aacAPEnableMethod": aacAPEnableMethod,
       "aacAPTelnetEnableMethod": aacAPTelnetEnableMethod,
       "aacAPHttpEnableMethod": aacAPHttpEnableMethod,
       "aacLoginMethodListTable": aacLoginMethodListTable,
       "aacLoginMethodListEntry": aacLoginMethodListEntry,
       "aacLoginMethodListName": aacLoginMethodListName,
       "aacLoginMethod1": aacLoginMethod1,
       "aacLoginMethod2": aacLoginMethod2,
       "aacLoginMethod3": aacLoginMethod3,
       "aacLoginMethod4": aacLoginMethod4,
       "aacLoginMethodListRowStatus": aacLoginMethodListRowStatus,
       "aacEnableMethodListTable": aacEnableMethodListTable,
       "aacEnableMethodListEntry": aacEnableMethodListEntry,
       "aacEnableMethodListName": aacEnableMethodListName,
       "aacEnableMethod1": aacEnableMethod1,
       "aacEnableMethod2": aacEnableMethod2,
       "aacEnableMethod3": aacEnableMethod3,
       "aacEnableMethod4": aacEnableMethod4,
       "aacEnableMethodListRowStatus": aacEnableMethodListRowStatus,
       "aacServerGroupTable": aacServerGroupTable,
       "aacServerGroupEntry": aacServerGroupEntry,
       "aacServerGroupName": aacServerGroupName,
       "aacServersInGroup": aacServersInGroup,
       "aacServerGroupRowStatus": aacServerGroupRowStatus,
       "aacServerInfoTable": aacServerInfoTable,
       "aacServerInfoEntry": aacServerInfoEntry,
       "aacServerIPType": aacServerIPType,
       "aacServerIPAddr": aacServerIPAddr,
       "aacServerIndex": aacServerIndex,
       "aacServerInterfaceName": aacServerInterfaceName,
       "aacServerAuthPort": aacServerAuthPort,
       "aacServerAuthKey": aacServerAuthKey,
       "aacServerTimeout": aacServerTimeout,
       "aacServerRetryCount": aacServerRetryCount,
       "aacServerRowStatus": aacServerRowStatus,
       "sysPortSecurityTrap": sysPortSecurityTrap,
       "portSecurityTraps": portSecurityTraps,
       "portSecurityViolation": portSecurityViolation,
       "sysTrustedHost": sysTrustedHost,
       "trustedHostStatus": trustedHostStatus,
       "trustedHostTable": trustedHostTable,
       "trustedHostEntry": trustedHostEntry,
       "trustedHostIpAddr": trustedHostIpAddr,
       "trustedHostIpMask": trustedHostIpMask,
       "trustedHostRowStatus": trustedHostRowStatus,
       "companyArp": companyArp,
       "sysArp": sysArp,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpIpAddr": arpIpAddr,
       "arpMacAddress": arpMacAddress,
       "arpType": arpType,
       "arpRowStatus": arpRowStatus,
       "cmArpClear": cmArpClear,
       "companySyslog": companySyslog,
       "syslogSettingGroup": syslogSettingGroup,
       "syslogEnable": syslogEnable,
       "syslogSaveMode": syslogSaveMode,
       "syslogSaveMinutes": syslogSaveMinutes,
       "syslogClearLog": syslogClearLog,
       "syslogServerGroup": syslogServerGroup,
       "syslogServTable": syslogServTable,
       "syslogServEntry": syslogServEntry,
       "syslogServIndex": syslogServIndex,
       "syslogServAddrType": syslogServAddrType,
       "syslogServAddr": syslogServAddr,
       "syslogServSeverity": syslogServSeverity,
       "syslogServFacility": syslogServFacility,
       "syslogServUDPport": syslogServUDPport,
       "syslogServSrvStatus": syslogServSrvStatus,
       "syslogServSrvRowStatus": syslogServSrvRowStatus,
       "syslogMsg": syslogMsg,
       "syslogMsgTable": syslogMsgTable,
       "syslogMsgEntry": syslogMsgEntry,
       "syslogMsgIndex": syslogMsgIndex,
       "syslogMsgDescr": syslogMsgDescr,
       "syslogMsgTime": syslogMsgTime,
       "syslogMsgSeverity": syslogMsgSeverity,
       "companyLBD": companyLBD,
       "sysLBDStateEnable": sysLBDStateEnable,
       "sysLBDMode": sysLBDMode,
       "sysLBDInterval": sysLBDInterval,
       "sysLBDRecoverTime": sysLBDRecoverTime,
       "sysLBDCtrlTable": sysLBDCtrlTable,
       "sysLBDCtrlEntry": sysLBDCtrlEntry,
       "sysLBDCtrlIndex": sysLBDCtrlIndex,
       "sysLBDPortStatus": sysLBDPortStatus,
       "sysLBDPortLoopStatus": sysLBDPortLoopStatus,
       "sysLBDVlanLoopTable": sysLBDVlanLoopTable,
       "sysLBDVlanLoopEntry": sysLBDVlanLoopEntry,
       "sysLBDVlanLoopIndex": sysLBDVlanLoopIndex,
       "sysLBDVlanLoopPorts": sysLBDVlanLoopPorts,
       "sysLBDEnabledVlanList": sysLBDEnabledVlanList,
       "sysLBDTrap": sysLBDTrap,
       "lbdTraps": lbdTraps,
       "loopbackOccur": loopbackOccur,
       "loopbackRecovery": loopbackRecovery,
       "companyMirror": companyMirror,
       "sysMirrorStatus": sysMirrorStatus,
       "sysMirrorPortTable": sysMirrorPortTable,
       "mirrorPortEntry": mirrorPortEntry,
       "mirrorTargetIfIndex": mirrorTargetIfIndex,
       "mirrorTargetPort": mirrorTargetPort,
       "mirrorIngressPortList": mirrorIngressPortList,
       "mirrorEgressPortList": mirrorEgressPortList,
       "mirrorCtrlRowStatus": mirrorCtrlRowStatus,
       "companyStaticMcast": companyStaticMcast,
       "sysStaticMcastTable": sysStaticMcastTable,
       "staticMcastEntry": staticMcastEntry,
       "staticMcastVlanID": staticMcastVlanID,
       "staticMcastMac": staticMcastMac,
       "staticMcastEgressPorts": staticMcastEgressPorts,
       "staticMcastStatus": staticMcastStatus,
       "companySNTPSetting": companySNTPSetting,
       "sysSNTPSettingGroup": sysSNTPSettingGroup,
       "sntpTimeSeconds": sntpTimeSeconds,
       "sntpPollInterval": sntpPollInterval,
       "sntpGlobalState": sntpGlobalState,
       "sntpDSTOffset": sntpDSTOffset,
       "sntpGMTMinutes": sntpGMTMinutes,
       "sntpDSTStartTime": sntpDSTStartTime,
       "sntpDSTEndTime": sntpDSTEndTime,
       "sntpDSTState": sntpDSTState,
       "sysSNTPServerGroup": sysSNTPServerGroup,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerAddrType": sntpServerAddrType,
       "sntpServerAddr": sntpServerAddr,
       "sntpServerType": sntpServerType,
       "sntpServerRowStatus": sntpServerRowStatus,
       "companyRMON": companyRMON,
       "sysRMONGlobalState": sysRMONGlobalState,
       "sysRMONStatistics": sysRMONStatistics,
       "rmonStatsTable": rmonStatsTable,
       "rmonStatsEntry": rmonStatsEntry,
       "rmonStatsIndex": rmonStatsIndex,
       "rmonStatsDataSource": rmonStatsDataSource,
       "rmonStatsOwner": rmonStatsOwner,
       "rmonStatsStatus": rmonStatsStatus,
       "rmonStatsDropEvents": rmonStatsDropEvents,
       "rmonStatsOctets": rmonStatsOctets,
       "rmonStatsPkts": rmonStatsPkts,
       "rmonStatsBroadcastPkts": rmonStatsBroadcastPkts,
       "rmonStatsMulticastPkts": rmonStatsMulticastPkts,
       "sysRMONHistory": sysRMONHistory,
       "rmonHistoryTable": rmonHistoryTable,
       "rmonHistoryEntry": rmonHistoryEntry,
       "rmonHistoryIndex": rmonHistoryIndex,
       "rmonHistoryDataSource": rmonHistoryDataSource,
       "rmonHistoryBucketsRequested": rmonHistoryBucketsRequested,
       "rmonHistoryInterval": rmonHistoryInterval,
       "rmonHistoryOwner": rmonHistoryOwner,
       "rmonHistoryStatus": rmonHistoryStatus,
       "sysRMONAlarm": sysRMONAlarm,
       "rmonAlarmTable": rmonAlarmTable,
       "rmonAlarmEntry": rmonAlarmEntry,
       "rmonAlarmIndex": rmonAlarmIndex,
       "rmonAlarmInterval": rmonAlarmInterval,
       "rmonAlarmVariable": rmonAlarmVariable,
       "rmonAlarmSampleType": rmonAlarmSampleType,
       "rmonAlarmRisingThreshold": rmonAlarmRisingThreshold,
       "rmonAlarmFallingThreshold": rmonAlarmFallingThreshold,
       "rmonAlarmRisingEventIndex": rmonAlarmRisingEventIndex,
       "rmonAlarmFallingEventIndex": rmonAlarmFallingEventIndex,
       "rmonAlarmOwner": rmonAlarmOwner,
       "rmonAlarmStatus": rmonAlarmStatus,
       "sysRMONEvent": sysRMONEvent,
       "rmonEventTable": rmonEventTable,
       "rmonEventEntry": rmonEventEntry,
       "rmonEventIndex": rmonEventIndex,
       "rmonEventDescription": rmonEventDescription,
       "rmonEventType": rmonEventType,
       "rmonEventCommunity": rmonEventCommunity,
       "rmonEventOwner": rmonEventOwner,
       "rmonEventStatus": rmonEventStatus,
       "rmonEventLastTimeSent": rmonEventLastTimeSent,
       "companyPnacGroup": companyPnacGroup,
       "sysPnacCtrl": sysPnacCtrl,
       "pnacStatus": pnacStatus,
       "pnacMode": pnacMode,
       "pnacProtocol": pnacProtocol,
       "pnacRadiusAccountingState": pnacRadiusAccountingState,
       "sysPnacPortAccessCtrl": sysPnacPortAccessCtrl,
       "pnacPortAccessControlTable": pnacPortAccessControlTable,
       "pnacPortAccessControlEntry": pnacPortAccessControlEntry,
       "pnacConfigPortNumber": pnacConfigPortNumber,
       "pnacQuietPeriod": pnacQuietPeriod,
       "pnacTxPeriod": pnacTxPeriod,
       "pnacSuppTimeout": pnacSuppTimeout,
       "pnacServerTimeout": pnacServerTimeout,
       "pnacMaxReq": pnacMaxReq,
       "pnacReAuthPeriod": pnacReAuthPeriod,
       "pnacReAuthentication": pnacReAuthentication,
       "pnacConfigPortControl": pnacConfigPortControl,
       "pnacCapability": pnacCapability,
       "pnacDirection": pnacDirection,
       "pnacOperControlledDirections": pnacOperControlledDirections,
       "pnacPortAuthStatus": pnacPortAuthStatus,
       "sysPnacUser": sysPnacUser,
       "pnacUserTable": pnacUserTable,
       "pnacUserEntry": pnacUserEntry,
       "pnacUserName": pnacUserName,
       "pnacUserPassword": pnacUserPassword,
       "pnacUserStatus": pnacUserStatus,
       "sysPnacRadiusServer": sysPnacRadiusServer,
       "pnacRadiusServerTable": pnacRadiusServerTable,
       "pnacRadiusServerEntry": pnacRadiusServerEntry,
       "pnacRadiusServerIndex": pnacRadiusServerIndex,
       "pnacRadiusIPType": pnacRadiusIPType,
       "pnacRadiusServerAddress": pnacRadiusServerAddress,
       "pnacRadiusServerAuthenticationPort": pnacRadiusServerAuthenticationPort,
       "pnacRadiusServerAccountingPort": pnacRadiusServerAccountingPort,
       "pnacRadiusServerTimeout": pnacRadiusServerTimeout,
       "pnacRadiusServerRetransmit": pnacRadiusServerRetransmit,
       "pnacRadiusServerKey": pnacRadiusServerKey,
       "pnacRadiusServerStatus": pnacRadiusServerStatus,
       "companyGuestVLAN": companyGuestVLAN,
       "sysGuestVlanName": sysGuestVlanName,
       "sysGuestVlanPort": sysGuestVlanPort,
       "sysGuestVlanDelState": sysGuestVlanDelState,
       "companyMacNotify": companyMacNotify,
       "sysMacNotifyState": sysMacNotifyState,
       "sysmacNotifyInterval": sysmacNotifyInterval,
       "sysmacNotifyHistorySize": sysmacNotifyHistorySize,
       "sysmacNotifyCtrlTable": sysmacNotifyCtrlTable,
       "macNotifyCtrlEntry": macNotifyCtrlEntry,
       "macNotifyPortIndex": macNotifyPortIndex,
       "macNotifyPortStatus": macNotifyPortStatus,
       "sysMacNotifyTraps": sysMacNotifyTraps,
       "fdbTableChanged": fdbTableChanged,
       "companyISMVLAN": companyISMVLAN,
       "sysIGMPMulticastVlanStatus": sysIGMPMulticastVlanStatus,
       "sysIGMPMulticastVlanTable": sysIGMPMulticastVlanTable,
       "sysIGMPMulticastVlanEntry": sysIGMPMulticastVlanEntry,
       "igmpMulticastVlanid": igmpMulticastVlanid,
       "igmpMulticastVlanAddressType": igmpMulticastVlanAddressType,
       "igmpMulticastVlanName": igmpMulticastVlanName,
       "igmpMulticastVlanSourcePort": igmpMulticastVlanSourcePort,
       "igmpMulticastVlanMemberPort": igmpMulticastVlanMemberPort,
       "igmpMulticastVlanTagMemberPort": igmpMulticastVlanTagMemberPort,
       "igmpMulticastVlanState": igmpMulticastVlanState,
       "igmpMulticastVlanReplaceSourceIp": igmpMulticastVlanReplaceSourceIp,
       "igmpMulticastVlanRowStatus": igmpMulticastVlanRowStatus,
       "sysIGMPMulticastVlanGroupTable": sysIGMPMulticastVlanGroupTable,
       "sysIGMPMulticastVlanGroupEntry": sysIGMPMulticastVlanGroupEntry,
       "igmpMulticastVlanGroupVid": igmpMulticastVlanGroupVid,
       "igmpMulticastVlanGroupAddressType": igmpMulticastVlanGroupAddressType,
       "igmpMulticastVlanGroupFromIp": igmpMulticastVlanGroupFromIp,
       "igmpMulticastVlanGroupToIp": igmpMulticastVlanGroupToIp,
       "igmpMulticastVlanGroupStatus": igmpMulticastVlanGroupStatus,
       "companyDHCPRelay": companyDHCPRelay,
       "sysDHCPRelayControl": sysDHCPRelayControl,
       "dhcpRelayState": dhcpRelayState,
       "dhcpRelayHopCount": dhcpRelayHopCount,
       "dhcpRelayTimeThreshold": dhcpRelayTimeThreshold,
       "sysDHCPRelayManagement": sysDHCPRelayManagement,
       "dhcpRelayInterfaceSettingsTable": dhcpRelayInterfaceSettingsTable,
       "dhcpRelayInterfaceSettingsEntry": dhcpRelayInterfaceSettingsEntry,
       "dhcpRelayServerIP": dhcpRelayServerIP,
       "dhcpRelayInterface": dhcpRelayInterface,
       "dhcpRelayInterfaceSettingsRowStatus": dhcpRelayInterfaceSettingsRowStatus,
       "dhcpRelayManagermentOption82": dhcpRelayManagermentOption82,
       "dhcpRelayOption82State": dhcpRelayOption82State,
       "dhcpRelayOption82CheckState": dhcpRelayOption82CheckState,
       "dhcpRelayOption82Policy": dhcpRelayOption82Policy,
       "dhcpRelayOption82RemoteIDType": dhcpRelayOption82RemoteIDType,
       "dhcpRelayOption82RemoteID": dhcpRelayOption82RemoteID,
       "companyDHCPLocalRelay": companyDHCPLocalRelay,
       "sysDHCPLocalRelayGlobalState": sysDHCPLocalRelayGlobalState,
       "sysDHCPLocalRelayTable": sysDHCPLocalRelayTable,
       "dhcpLocalRelayEntry": dhcpLocalRelayEntry,
       "dhcpLocalRelayVlanId": dhcpLocalRelayVlanId,
       "dhcpLocalRelayState": dhcpLocalRelayState,
       "companyGreenSetting": companyGreenSetting,
       "sysGreenLEDShutoff": sysGreenLEDShutoff,
       "greenLEDShutoffPortList": greenLEDShutoffPortList,
       "greenLEDShutoffState": greenLEDShutoffState,
       "greenLEDShutoffTimeProfile1": greenLEDShutoffTimeProfile1,
       "greenLEDShutoffTimeProfile2": greenLEDShutoffTimeProfile2,
       "sysGreenPortShutoff": sysGreenPortShutoff,
       "greenPortShutoffPortList": greenPortShutoffPortList,
       "greenPortShutoffState": greenPortShutoffState,
       "greenPortShutoffTimeProfile1": greenPortShutoffTimeProfile1,
       "greenPortShutoffTimeProfile2": greenPortShutoffTimeProfile2,
       "sysGreenSystemHibernation": sysGreenSystemHibernation,
       "greenSystemHibernationState": greenSystemHibernationState,
       "greenSystemHibernationTimeProfile1": greenSystemHibernationTimeProfile1,
       "greenSystemHibernationTimeProfile2": greenSystemHibernationTimeProfile2,
       "greenCableLenDetectionState": greenCableLenDetectionState,
       "companyLLDP": companyLLDP,
       "sysLLDPState": sysLLDPState,
       "sysLLDPMsgHoldMultiplier": sysLLDPMsgHoldMultiplier,
       "sysLLDPMsgTxInterval": sysLLDPMsgTxInterval,
       "sysLLDPReinitDelay": sysLLDPReinitDelay,
       "sysLLDPTxDelay": sysLLDPTxDelay,
       "sysLLDPConfigManAddrTable": sysLLDPConfigManAddrTable,
       "sysLLDPConfigManAddrEntry": sysLLDPConfigManAddrEntry,
       "lldpConfigManAddrSubtype": lldpConfigManAddrSubtype,
       "lldpConfigManAddr": lldpConfigManAddr,
       "lldpConfigManAddrPortsTxEnable": lldpConfigManAddrPortsTxEnable,
       "sysLLDPPortConfigTable": sysLLDPPortConfigTable,
       "sysLLDPPortConfigEntry": sysLLDPPortConfigEntry,
       "lldpPortConfigPortNum": lldpPortConfigPortNum,
       "lldpPortConfigAdminStatus": lldpPortConfigAdminStatus,
       "lldpPortConfigNotificationEnable": lldpPortConfigNotificationEnable,
       "lldpPortConfigTLVsTxEnable": lldpPortConfigTLVsTxEnable,
       "sysLLDPXdot3Objects": sysLLDPXdot3Objects,
       "lldpXdot3Config": lldpXdot3Config,
       "lldpXdot3PortConfigTable": lldpXdot3PortConfigTable,
       "lldpXdot3PortConfigEntry": lldpXdot3PortConfigEntry,
       "lldpXdot3PortConfigPortNum": lldpXdot3PortConfigPortNum,
       "lldpXdot3PortConfigTLVsTxEnable": lldpXdot3PortConfigTLVsTxEnable,
       "lldpXdot3LocalData": lldpXdot3LocalData,
       "lldpXdot3LocPortTable": lldpXdot3LocPortTable,
       "lldpXdot3LocPortEntry": lldpXdot3LocPortEntry,
       "lldpXdot3LocPortNum": lldpXdot3LocPortNum,
       "lldpXdot3LocPortAutoNegSupported": lldpXdot3LocPortAutoNegSupported,
       "lldpXdot3LocPortAutoNegEnabled": lldpXdot3LocPortAutoNegEnabled,
       "lldpXdot3LocPortAutoNegAdvertisedCap": lldpXdot3LocPortAutoNegAdvertisedCap,
       "lldpXdot3LocPortOperMauType": lldpXdot3LocPortOperMauType,
       "lldpXdot3LocMaxFrameSizeTable": lldpXdot3LocMaxFrameSizeTable,
       "lldpXdot3LocMaxFrameSizeEntry": lldpXdot3LocMaxFrameSizeEntry,
       "lldpXdot3LocMaxFrameSizePortNum": lldpXdot3LocMaxFrameSizePortNum,
       "lldpXdot3LocMaxFrameSize": lldpXdot3LocMaxFrameSize,
       "lldpXdot3RemoteData": lldpXdot3RemoteData,
       "lldpXdot3RemPortTable": lldpXdot3RemPortTable,
       "lldpXdot3RemPortEntry": lldpXdot3RemPortEntry,
       "lldpXdot3RemTimeMark": lldpXdot3RemTimeMark,
       "lldpXdot3RemLocalPortNum": lldpXdot3RemLocalPortNum,
       "lldpXdot3RemIndex": lldpXdot3RemIndex,
       "lldpXdot3RemPortAutoNegSupported": lldpXdot3RemPortAutoNegSupported,
       "lldpXdot3RemPortAutoNegEnabled": lldpXdot3RemPortAutoNegEnabled,
       "lldpXdot3RemPortAutoNegAdvertisedCap": lldpXdot3RemPortAutoNegAdvertisedCap,
       "lldpXdot3RemPortOperMauType": lldpXdot3RemPortOperMauType,
       "lldpXdot3RemPowerTable": lldpXdot3RemPowerTable,
       "lldpXdot3RemPowerEntry": lldpXdot3RemPowerEntry,
       "lldpXdot3RemPowerTimeMark": lldpXdot3RemPowerTimeMark,
       "lldpXdot3RemPowerLocalPortNum": lldpXdot3RemPowerLocalPortNum,
       "lldpXdot3RemPowerIndex": lldpXdot3RemPowerIndex,
       "lldpXdot3RemPowerPortClass": lldpXdot3RemPowerPortClass,
       "lldpXdot3RemPowerMDISupported": lldpXdot3RemPowerMDISupported,
       "lldpXdot3RemPowerMDIEnabled": lldpXdot3RemPowerMDIEnabled,
       "lldpXdot3RemPowerPairControlable": lldpXdot3RemPowerPairControlable,
       "lldpXdot3RemPowerPairs": lldpXdot3RemPowerPairs,
       "lldpXdot3RemPowerClass": lldpXdot3RemPowerClass,
       "lldpXdot3RemLinkAggTable": lldpXdot3RemLinkAggTable,
       "lldpXdot3RemLinkAggEntry": lldpXdot3RemLinkAggEntry,
       "lldpXdot3RemLinkAggTimeMark": lldpXdot3RemLinkAggTimeMark,
       "lldpXdot3RemLinkAggLocalPortNum": lldpXdot3RemLinkAggLocalPortNum,
       "lldpXdot3RemLinkAggIndex": lldpXdot3RemLinkAggIndex,
       "lldpXdot3RemLinkAggStatus": lldpXdot3RemLinkAggStatus,
       "lldpXdot3RemLinkAggPortId": lldpXdot3RemLinkAggPortId,
       "lldpXdot3RemMaxFrameSizeTable": lldpXdot3RemMaxFrameSizeTable,
       "lldpXdot3RemMaxFrameSizeEntry": lldpXdot3RemMaxFrameSizeEntry,
       "lldpXdot3RemMaxFrameSizeTimeMark": lldpXdot3RemMaxFrameSizeTimeMark,
       "lldpXdot3RemMaxFrameSizeLocalPortNum": lldpXdot3RemMaxFrameSizeLocalPortNum,
       "lldpXdot3RemMaxFrameSizeIndex": lldpXdot3RemMaxFrameSizeIndex,
       "lldpXdot3RemMaxFrameSize": lldpXdot3RemMaxFrameSize,
       "sysLLDPXdot1Objects": sysLLDPXdot1Objects,
       "lldpXdot1Config": lldpXdot1Config,
       "lldpXdot1ConfigPortVlanTable": lldpXdot1ConfigPortVlanTable,
       "lldpXdot1ConfigPortVlanEntry": lldpXdot1ConfigPortVlanEntry,
       "lldpXdot1ConfigVlanPortNum": lldpXdot1ConfigVlanPortNum,
       "lldpXdot1ConfigPortVlanTxEnable": lldpXdot1ConfigPortVlanTxEnable,
       "lldpXdot1ConfigVlanNameTable": lldpXdot1ConfigVlanNameTable,
       "lldpXdot1ConfigVlanNameEntry": lldpXdot1ConfigVlanNameEntry,
       "lldpXdot1LocConfigVlanNamePortNum": lldpXdot1LocConfigVlanNamePortNum,
       "lldpXdot1ConfigVlanId": lldpXdot1ConfigVlanId,
       "lldpXdot1ConfigVlanNameTxEnable": lldpXdot1ConfigVlanNameTxEnable,
       "lldpXdot1ConfigProtocolTable": lldpXdot1ConfigProtocolTable,
       "lldpXdot1ConfigProtocolEntry": lldpXdot1ConfigProtocolEntry,
       "lldpXdot1ConfigProtocolPortNum": lldpXdot1ConfigProtocolPortNum,
       "lldpXdot1ConfigProtocolIndex": lldpXdot1ConfigProtocolIndex,
       "lldpXdot1ConfigProtocolTxEnable": lldpXdot1ConfigProtocolTxEnable,
       "lldpXdot1LocalData": lldpXdot1LocalData,
       "lldpXdot1LocTable": lldpXdot1LocTable,
       "lldpXdot1LocEntry": lldpXdot1LocEntry,
       "lldpXdot1LocPortNum": lldpXdot1LocPortNum,
       "lldpXdot1LocPortVlanId": lldpXdot1LocPortVlanId,
       "lldpXdot1LocVlanNameTable": lldpXdot1LocVlanNameTable,
       "lldpXdot1LocVlanNameEntry": lldpXdot1LocVlanNameEntry,
       "lldpXdot1LocVlanNamePortNum": lldpXdot1LocVlanNamePortNum,
       "lldpXdot1LocVlanId": lldpXdot1LocVlanId,
       "lldpXdot1LocVlanName": lldpXdot1LocVlanName,
       "lldpXdot1LocProtocolTable": lldpXdot1LocProtocolTable,
       "lldpXdot1LocProtocolEntry": lldpXdot1LocProtocolEntry,
       "lldpXdot1LocProtocolPortNum": lldpXdot1LocProtocolPortNum,
       "lldpXdot1LocProtocolIndex": lldpXdot1LocProtocolIndex,
       "lldpXdot1LocProtocolId": lldpXdot1LocProtocolId,
       "lldpXdot1RemoteData": lldpXdot1RemoteData,
       "lldpXdot1RemTable": lldpXdot1RemTable,
       "lldpXdot1RemEntry": lldpXdot1RemEntry,
       "lldpXdot1RemTimeMark": lldpXdot1RemTimeMark,
       "lldpXdot1RemLocalPortNum": lldpXdot1RemLocalPortNum,
       "lldpXdot1RemIndex": lldpXdot1RemIndex,
       "lldpXdot1RemPortVlanId": lldpXdot1RemPortVlanId,
       "lldpXdot1RemProtoVlanTable": lldpXdot1RemProtoVlanTable,
       "lldpXdot1RemProtoVlanEntry": lldpXdot1RemProtoVlanEntry,
       "lldpXdot1RemProtoVlanTimeMark": lldpXdot1RemProtoVlanTimeMark,
       "lldpXdot1RemProtoVlanLocalPortNum": lldpXdot1RemProtoVlanLocalPortNum,
       "lldpXdot1RemProtoVlanIndex": lldpXdot1RemProtoVlanIndex,
       "lldpXdot1RemProtoVlanId": lldpXdot1RemProtoVlanId,
       "lldpXdot1RemProtoVlanSupported": lldpXdot1RemProtoVlanSupported,
       "lldpXdot1RemProtoVlanEnabled": lldpXdot1RemProtoVlanEnabled,
       "lldpXdot1RemVlanNameTable": lldpXdot1RemVlanNameTable,
       "lldpXdot1RemVlanNameEntry": lldpXdot1RemVlanNameEntry,
       "lldpXdot1RemVlanNameTimeMark": lldpXdot1RemVlanNameTimeMark,
       "lldpXdot1RemVlanNameLocalPortNum": lldpXdot1RemVlanNameLocalPortNum,
       "lldpXdot1RemVlanNameIndex": lldpXdot1RemVlanNameIndex,
       "lldpXdot1RemVlanId": lldpXdot1RemVlanId,
       "lldpXdot1RemVlanName": lldpXdot1RemVlanName,
       "lldpXdot1RemProtocolTable": lldpXdot1RemProtocolTable,
       "lldpXdot1RemProtocolEntry": lldpXdot1RemProtocolEntry,
       "lldpXdot1RemProtocolTimeMark": lldpXdot1RemProtocolTimeMark,
       "lldpXdot1RemProtocolLocalPortNum": lldpXdot1RemProtocolLocalPortNum,
       "lldpXdot1RemProtocolIndex": lldpXdot1RemProtocolIndex,
       "lldpXdot1RemProtocolIdIndex": lldpXdot1RemProtocolIdIndex,
       "lldpXdot1RemProtocolId": lldpXdot1RemProtocolId,
       "sysLLDPStatistics": sysLLDPStatistics,
       "lldpStatsRemTablesLastChangeTime": lldpStatsRemTablesLastChangeTime,
       "lldpStatsRemTablesInserts": lldpStatsRemTablesInserts,
       "lldpStatsRemTablesDeletes": lldpStatsRemTablesDeletes,
       "lldpStatsRemTablesDrops": lldpStatsRemTablesDrops,
       "lldpStatsRemTablesAgeouts": lldpStatsRemTablesAgeouts,
       "lldpStatsTxPortTable": lldpStatsTxPortTable,
       "lldpStatsTxPortEntry": lldpStatsTxPortEntry,
       "lldpStatsTxPortNum": lldpStatsTxPortNum,
       "lldpStatsTxPortFramesTotal": lldpStatsTxPortFramesTotal,
       "lldpRxStatsPortTable": lldpRxStatsPortTable,
       "lldpRxStatsPortEntry": lldpRxStatsPortEntry,
       "lldpStatsRxPortNum": lldpStatsRxPortNum,
       "lldpStatsRxPortFramesDiscardedTotal": lldpStatsRxPortFramesDiscardedTotal,
       "lldpStatsRxPortFramesErrors": lldpStatsRxPortFramesErrors,
       "lldpStatsRxPortFramesTotal": lldpStatsRxPortFramesTotal,
       "lldpStatsRxPortTLVsDiscardedTotal": lldpStatsRxPortTLVsDiscardedTotal,
       "lldpStatsRxPortTLVsUnrecognizedTotal": lldpStatsRxPortTLVsUnrecognizedTotal,
       "lldpStatsRxPortAgeoutsTotal": lldpStatsRxPortAgeoutsTotal,
       "sysLLDPLocalSystemData": sysLLDPLocalSystemData,
       "lldpLocChassisIdSubtype": lldpLocChassisIdSubtype,
       "lldpLocChassisId": lldpLocChassisId,
       "lldpLocSysName": lldpLocSysName,
       "lldpLocSysDesc": lldpLocSysDesc,
       "lldpLocSysCapEnabled": lldpLocSysCapEnabled,
       "lldpLocPortTable": lldpLocPortTable,
       "lldpLocPortEntry": lldpLocPortEntry,
       "lldpLocPortNum": lldpLocPortNum,
       "lldpLocPortIdSubtype": lldpLocPortIdSubtype,
       "lldpLocPortId": lldpLocPortId,
       "lldpLocPortDesc": lldpLocPortDesc,
       "lldpLocManAddrTable": lldpLocManAddrTable,
       "lldpLocManAddrEntry": lldpLocManAddrEntry,
       "lldpLocManAddrSubtype": lldpLocManAddrSubtype,
       "lldpLocManAddr": lldpLocManAddr,
       "lldpLocManAddrLen": lldpLocManAddrLen,
       "lldpLocManAddrIfSubtype": lldpLocManAddrIfSubtype,
       "lldpLocManAddrIfId": lldpLocManAddrIfId,
       "lldpLocManAddrOID": lldpLocManAddrOID,
       "sysLLDPRemoteSystemsData": sysLLDPRemoteSystemsData,
       "lldpRemTable": lldpRemTable,
       "lldpRemEntry": lldpRemEntry,
       "lldpRemTimeMark": lldpRemTimeMark,
       "lldpRemLocalPortNum": lldpRemLocalPortNum,
       "lldpRemIndex": lldpRemIndex,
       "lldpRemChassisIdSubtype": lldpRemChassisIdSubtype,
       "lldpRemChassisId": lldpRemChassisId,
       "lldpRemPortIdSubtype": lldpRemPortIdSubtype,
       "lldpRemPortId": lldpRemPortId,
       "lldpRemPortDesc": lldpRemPortDesc,
       "lldpRemSysName": lldpRemSysName,
       "lldpRemSysDesc": lldpRemSysDesc,
       "lldpRemSysCapSupported": lldpRemSysCapSupported,
       "lldpRemSysCapEnabled": lldpRemSysCapEnabled,
       "lldpRemManAddrTable": lldpRemManAddrTable,
       "lldpRemManAddrEntry": lldpRemManAddrEntry,
       "lldpRemManTimeMark": lldpRemManTimeMark,
       "lldpRemManLocalPortNum": lldpRemManLocalPortNum,
       "lldpRemManIndex": lldpRemManIndex,
       "lldpRemManAddrSubtype": lldpRemManAddrSubtype,
       "lldpRemManAddr": lldpRemManAddr,
       "lldpRemManAddrIfSubtype": lldpRemManAddrIfSubtype,
       "lldpRemManAddrIfId": lldpRemManAddrIfId,
       "lldpRemManAddrOID": lldpRemManAddrOID,
       "lldpRemUnknownTLVTable": lldpRemUnknownTLVTable,
       "lldpRemUnknownTLVEntry": lldpRemUnknownTLVEntry,
       "lldpRemUnknownTimeMark": lldpRemUnknownTimeMark,
       "lldpRemUnknownLocalPortNum": lldpRemUnknownLocalPortNum,
       "lldpRemUnknownIndex": lldpRemUnknownIndex,
       "lldpRemUnknownTLVType": lldpRemUnknownTLVType,
       "lldpRemUnknownTLVInfo": lldpRemUnknownTLVInfo,
       "sysLLDPNotification": sysLLDPNotification,
       "lldpTraps": lldpTraps,
       "lldpRemTablesChange": lldpRemTablesChange,
       "lldpExceedsMaxFrameSize": lldpExceedsMaxFrameSize,
       "lldpDupChasisId": lldpDupChasisId,
       "lldpDupSystemName": lldpDupSystemName,
       "lldpDupManagmentAddress": lldpDupManagmentAddress,
       "lldpMisConfigPortVlanID": lldpMisConfigPortVlanID,
       "lldpMisConfigVlanName": lldpMisConfigVlanName,
       "lldpMisConfigProtocolIdentity": lldpMisConfigProtocolIdentity,
       "lldpMisConfigMaxFrameSize": lldpMisConfigMaxFrameSize,
       "lldpMisConfigOperMauType": lldpMisConfigOperMauType,
       "companyCableDiagnostic": companyCableDiagnostic,
       "sysCableDiagTriggerIndex": sysCableDiagTriggerIndex,
       "sysCableDiagPair1TestResult": sysCableDiagPair1TestResult,
       "sysCableDiagPair1FaultDistance": sysCableDiagPair1FaultDistance,
       "sysCableDiagPair2TestResult": sysCableDiagPair2TestResult,
       "sysCableDiagPair2FaultDistance": sysCableDiagPair2FaultDistance,
       "sysCableDiagPair3TestResult": sysCableDiagPair3TestResult,
       "sysCableDiagPair3FaultDistance": sysCableDiagPair3FaultDistance,
       "sysCableDiagPair4TestResult": sysCableDiagPair4TestResult,
       "sysCableDiagPair4FaultDistance": sysCableDiagPair4FaultDistance,
       "sysCableDiagLengthinRange": sysCableDiagLengthinRange,
       "companyQinQ": companyQinQ,
       "sysQinQSystem": sysQinQSystem,
       "qinQGlobalStatus": qinQGlobalStatus,
       "qinQConfigTable": qinQConfigTable,
       "qinQConfigEntry": qinQConfigEntry,
       "qinQIfIndex": qinQIfIndex,
       "qinQRoleState": qinQRoleState,
       "qinQOuterTPID": qinQOuterTPID,
       "qinQMissDrop": qinQMissDrop,
       "qinQAddInnerTag": qinQAddInnerTag,
       "qinQInnerTPID": qinQInnerTPID,
       "qinQVlanTranslationTable": qinQVlanTranslationTable,
       "qinQVlanTranslationEntry": qinQVlanTranslationEntry,
       "qinQVlanTransPortNum": qinQVlanTransPortNum,
       "qinQVlanTransCVID": qinQVlanTransCVID,
       "qinQVlanTransSVID": qinQVlanTransSVID,
       "qinQVlanTransAction": qinQVlanTransAction,
       "qinQVlanTransPriority": qinQVlanTransPriority,
       "qinQVlanTransRowStatus": qinQVlanTransRowStatus,
       "companyTimeRangeMgmt": companyTimeRangeMgmt,
       "sysTimeRangeSettingTable": sysTimeRangeSettingTable,
       "timeRangeSettingEntry": timeRangeSettingEntry,
       "timeRangeIndex": timeRangeIndex,
       "timeRangeName": timeRangeName,
       "timeRangeDate": timeRangeDate,
       "timeRangeStartYear": timeRangeStartYear,
       "timeRangeStartMonth": timeRangeStartMonth,
       "timeRangeStartDay": timeRangeStartDay,
       "timeRangeStartHour": timeRangeStartHour,
       "timeRangeStartMinute": timeRangeStartMinute,
       "timeRangeEndYear": timeRangeEndYear,
       "timeRangeEndMonth": timeRangeEndMonth,
       "timeRangeEndDay": timeRangeEndDay,
       "timeRangeEndHour": timeRangeEndHour,
       "timeRangeEndMinute": timeRangeEndMinute,
       "timeRangeMonday": timeRangeMonday,
       "timeRangeTuesday": timeRangeTuesday,
       "timeRangeWednesday": timeRangeWednesday,
       "timeRangeThursday": timeRangeThursday,
       "timeRangeFriday": timeRangeFriday,
       "timeRangeSaturday": timeRangeSaturday,
       "timeRangeSunday": timeRangeSunday,
       "timeRangeRowStatus": timeRangeRowStatus,
       "companyLimitIP": companyLimitIP,
       "syslimitIPMulticastProfileTable": syslimitIPMulticastProfileTable,
       "limitIPMulticastProfileEntry": limitIPMulticastProfileEntry,
       "limitIPMulticastProfileID": limitIPMulticastProfileID,
       "limitIPMulticastIPType": limitIPMulticastIPType,
       "limitIPMulticastProfileName": limitIPMulticastProfileName,
       "limitIPMulticastProfileStatus": limitIPMulticastProfileStatus,
       "syslimitIPMulticastPortTable": syslimitIPMulticastPortTable,
       "limitIPMulticastPortEntry": limitIPMulticastPortEntry,
       "limitIPMulticastPortID": limitIPMulticastPortID,
       "limitIPMulticastPortIPType": limitIPMulticastPortIPType,
       "limitIPMulticastPortState": limitIPMulticastPortState,
       "limitIPMulticastPortProfileID": limitIPMulticastPortProfileID,
       "limitIPMulticastPortMaxGrp": limitIPMulticastPortMaxGrp,
       "limitIpMulticastRangeTable": limitIpMulticastRangeTable,
       "limitIpMulticastRangeEntry": limitIpMulticastRangeEntry,
       "limitIpMulticastRangeProfileID": limitIpMulticastRangeProfileID,
       "limitIpMulticastRangeIPType": limitIpMulticastRangeIPType,
       "limitIpMulticastRangeStartIpAddr": limitIpMulticastRangeStartIpAddr,
       "limitIpMulticastRangeEndIpAddr": limitIpMulticastRangeEndIpAddr,
       "limitIpMulticastRangeStatus": limitIpMulticastRangeStatus,
       "companyMulticastFilter": companyMulticastFilter,
       "sysMulticastFilterPortTable": sysMulticastFilterPortTable,
       "multicastFilterPortEntry": multicastFilterPortEntry,
       "multicastFilterPortIndex": multicastFilterPortIndex,
       "multicastFilterPortType": multicastFilterPortType,
       "companyIPv6Neighbor": companyIPv6Neighbor,
       "sysIPv6neighborTable": sysIPv6neighborTable,
       "ipv6NeighborEntry": ipv6NeighborEntry,
       "ipv6NeighborIndex": ipv6NeighborIndex,
       "ipv6NeighborAddr": ipv6NeighborAddr,
       "ipv6NeighborMacAddr": ipv6NeighborMacAddr,
       "ipv6NeighborCacheState": ipv6NeighborCacheState,
       "ipv6NeighborRowStatus": ipv6NeighborRowStatus,
       "companyEoam": companyEoam,
       "sysEoamSystem": sysEoamSystem,
       "eoamTable": eoamTable,
       "eoamEntry": eoamEntry,
       "eoamIfIndex": eoamIfIndex,
       "eoamState": eoamState,
       "eoamMode": eoamMode,
       "eoamReceivedRemoteLoopback": eoamReceivedRemoteLoopback,
       "eoamRemoteLoopback": eoamRemoteLoopback,
       "eoamMaxOAMPDU": eoamMaxOAMPDU,
       "eoamUnidirection": eoamUnidirection,
       "eoamLinkMonitoring": eoamLinkMonitoring,
       "eoamVarReq": eoamVarReq,
       "eoamRemoteLoopbackSupport": eoamRemoteLoopbackSupport,
       "eoamPDURev": eoamPDURev,
       "eoamOperStatus": eoamOperStatus,
       "eoamPeerMode": eoamPeerMode,
       "eoamPeerMacAddress": eoamPeerMacAddress,
       "eoamPeerVendorOui": eoamPeerVendorOui,
       "eoamPeerMaxOAMPDU": eoamPeerMaxOAMPDU,
       "eoamPeerUnidirection": eoamPeerUnidirection,
       "eoamPeerLinkMonitoring": eoamPeerLinkMonitoring,
       "eoamPeerVarReq": eoamPeerVarReq,
       "eoamPeerPDURev": eoamPeerPDURev,
       "sysEoamLinkMonitor": sysEoamLinkMonitor,
       "eoamLinkMonitorTable": eoamLinkMonitorTable,
       "eoamLinkMonitorEntry": eoamLinkMonitorEntry,
       "eoamLinkMonitorIfIndex": eoamLinkMonitorIfIndex,
       "errorSymbolNotifyState": errorSymbolNotifyState,
       "errorSymbolThreshold": errorSymbolThreshold,
       "errorSymbolWindow": errorSymbolWindow,
       "errorFrameNotifyState": errorFrameNotifyState,
       "errorFrameThreshold": errorFrameThreshold,
       "errorFrameWindow": errorFrameWindow,
       "errorFrameSecondsNotifyState": errorFrameSecondsNotifyState,
       "errorFrameSecondsThreshold": errorFrameSecondsThreshold,
       "errorFrameSecondsWindow": errorFrameSecondsWindow,
       "errorFramePeriodNotifyState": errorFramePeriodNotifyState,
       "errorFramePeriodThreshold": errorFramePeriodThreshold,
       "errorFramePeriodWindow": errorFramePeriodWindow,
       "eoamCriticalLinkEventState": eoamCriticalLinkEventState,
       "sysEoamStats": sysEoamStats,
       "sysEoamStatsTable": sysEoamStatsTable,
       "eoamStatsEntry": eoamStatsEntry,
       "eoamInfomationIndex": eoamInfomationIndex,
       "eoamInformationTx": eoamInformationTx,
       "eoamInformationRx": eoamInformationRx,
       "eoamUniqueEventNotificationTx": eoamUniqueEventNotificationTx,
       "eoamUniqueEventNotificationRx": eoamUniqueEventNotificationRx,
       "eoamDuplicateEventNotificationTx": eoamDuplicateEventNotificationTx,
       "eoamDuplicateEventNotificationRx": eoamDuplicateEventNotificationRx,
       "eoamLoopbackControlTx": eoamLoopbackControlTx,
       "eoamLoopbackControlRx": eoamLoopbackControlRx,
       "eoamVariableRequestTx": eoamVariableRequestTx,
       "eoamVariableRequestRx": eoamVariableRequestRx,
       "eoamVariableResponseTx": eoamVariableResponseTx,
       "eoamVariableResponseRx": eoamVariableResponseRx,
       "eoamOrgSpecificTx": eoamOrgSpecificTx,
       "eoamOrgSpecificRx": eoamOrgSpecificRx,
       "eoamUnsupportedCodesTx": eoamUnsupportedCodesTx,
       "eoamUnsupportedCodesRx": eoamUnsupportedCodesRx,
       "eoamFramesLostDueToOam": eoamFramesLostDueToOam,
       "sysEoamStatsClearPortlist": sysEoamStatsClearPortlist,
       "sysEoamEventLog": sysEoamEventLog,
       "sysOamEventLogTable": sysOamEventLogTable,
       "eoamEventLogEntry": eoamEventLogEntry,
       "eoamEventLogPort": eoamEventLogPort,
       "eoamEventLogIndex": eoamEventLogIndex,
       "eoamEventLogTimestamp": eoamEventLogTimestamp,
       "eoamEventLogType": eoamEventLogType,
       "eoamEventLogLocation": eoamEventLogLocation,
       "eoamEventLogValue": eoamEventLogValue,
       "eoamEventLogWindow": eoamEventLogWindow,
       "eoamEventLogThreshold": eoamEventLogThreshold,
       "eoamEventLogAccError": eoamEventLogAccError,
       "sysEoamEventLogClearPortlist": sysEoamEventLogClearPortlist,
       "sysEoamTrap": sysEoamTrap,
       "eoamTrap": eoamTrap,
       "eoamNotifyThresholdEvent": eoamNotifyThresholdEvent,
       "eoamNotifyNonThresholdEvent": eoamNotifyNonThresholdEvent,
       "sysEoamLoopbackTest": sysEoamLoopbackTest,
       "eoamLoopbackTestTable": eoamLoopbackTestTable,
       "eoamLoopbackTestEntry": eoamLoopbackTestEntry,
       "eoamLoopbackTestIndex": eoamLoopbackTestIndex,
       "eoamLoopbackStatus": eoamLoopbackStatus,
       "eoamLoopbackTestPattern": eoamLoopbackTestPattern,
       "eoamLoopbackTestPktSize": eoamLoopbackTestPktSize,
       "eoamLoopbackTestCount": eoamLoopbackTestCount,
       "eoamLoopbackTestWaitTime": eoamLoopbackTestWaitTime,
       "eoamLoopbackTestCommand": eoamLoopbackTestCommand,
       "eoamLoopbackTestStatus": eoamLoopbackTestStatus,
       "eoamLoopbackTestStartTimestamp": eoamLoopbackTestStartTimestamp,
       "eoamLoopbackTestEndTimestamp": eoamLoopbackTestEndTimestamp,
       "eoamLoopbackTestTxCount": eoamLoopbackTestTxCount,
       "eoamLoopbackTestRxCount": eoamLoopbackTestRxCount,
       "eoamLoopbackTestMatchCount": eoamLoopbackTestMatchCount,
       "eoamLoopbackStatsTable": eoamLoopbackStatsTable,
       "eoamLoopbackStatsEntry": eoamLoopbackStatsEntry,
       "eoamLoopbackStatsIndex": eoamLoopbackStatsIndex,
       "eoamLoopbackStatsStartTimestamp": eoamLoopbackStatsStartTimestamp,
       "eoamLoopbackStatsEndTimestamp": eoamLoopbackStatsEndTimestamp,
       "eoamLoopbackStatsTxCount": eoamLoopbackStatsTxCount,
       "eoamLoopbackStatsRxCount": eoamLoopbackStatsRxCount,
       "eoamLoopbackStatsMatchCount": eoamLoopbackStatsMatchCount,
       "companyDuld": companyDuld,
       "sysDuld": sysDuld,
       "duldTable": duldTable,
       "duldEntry": duldEntry,
       "duldIfIndex": duldIfIndex,
       "duldState": duldState,
       "duldOperState": duldOperState,
       "duldMode": duldMode,
       "duldLinkStatus": duldLinkStatus,
       "duldDiscoveryTime": duldDiscoveryTime,
       "companyEee": companyEee,
       "sysEee": sysEee,
       "eeeTable": eeeTable,
       "eeeEntry": eeeEntry,
       "eeePort": eeePort,
       "eeestatus": eeestatus,
       "companyDHCPv6Relay": companyDHCPv6Relay,
       "sysDHCPv6RelayControl": sysDHCPv6RelayControl,
       "dhcpv6RelayState": dhcpv6RelayState,
       "dhcpv6RelayHopCount": dhcpv6RelayHopCount,
       "sysDHCPv6RelayManagement": sysDHCPv6RelayManagement,
       "dhcpv6RelayInterfaceTable": dhcpv6RelayInterfaceTable,
       "dhcpv6RelayInterfaceEntry": dhcpv6RelayInterfaceEntry,
       "dhcpv6RelayServerIP": dhcpv6RelayServerIP,
       "dhcpv6RelayInterface": dhcpv6RelayInterface,
       "dhcpv6RelayRowStatus": dhcpv6RelayRowStatus,
       "sysDHCPv6RelayOption37": sysDHCPv6RelayOption37,
       "dhcpv6RelayOption37State": dhcpv6RelayOption37State,
       "dhcpv6RelayOption37CheckState": dhcpv6RelayOption37CheckState,
       "dhcpv6RelayOption37RemoteIDType": dhcpv6RelayOption37RemoteIDType,
       "dhcpv6RelayOption37RemoteID": dhcpv6RelayOption37RemoteID,
       "companyMldsGroup": companyMldsGroup,
       "sysMldsSystem": sysMldsSystem,
       "mldsStatus": mldsStatus,
       "sysMldsVlan": sysMldsVlan,
       "mldsVlanRouterTable": mldsVlanRouterTable,
       "mldsVlanRouterEntry": mldsVlanRouterEntry,
       "mldsVlanRouterVlanId": mldsVlanRouterVlanId,
       "mldsVlanRouterStaticPortList": mldsVlanRouterStaticPortList,
       "mldsVlanRouterDynamicPortList": mldsVlanRouterDynamicPortList,
       "mldsVlanFilterTable": mldsVlanFilterTable,
       "mldsVlanFilterEntry": mldsVlanFilterEntry,
       "mldsVlanFilterVlanId": mldsVlanFilterVlanId,
       "mldsVlanSnoopStatus": mldsVlanSnoopStatus,
       "mldsVlanQuerier": mldsVlanQuerier,
       "mldsVlanCfgQuerier": mldsVlanCfgQuerier,
       "mldsVlanQueryInterval": mldsVlanQueryInterval,
       "mldsVlanFastLeave": mldsVlanFastLeave,
       "mldsVlanQuerierVersion": mldsVlanQuerierVersion,
       "mldsVlanRouterPortPurgeInterval": mldsVlanRouterPortPurgeInterval,
       "mldsVlanHostPortPurgeInterval": mldsVlanHostPortPurgeInterval,
       "mldsVlanRobustnessValue": mldsVlanRobustnessValue,
       "mldsVlanGrpQueryInterval": mldsVlanGrpQueryInterval,
       "mldsVlanQueryMaxResponseTime": mldsVlanQueryMaxResponseTime,
       "mldsVlanMulticastGroupTable": mldsVlanMulticastGroupTable,
       "mldsVlanMulticastGroupEntry": mldsVlanMulticastGroupEntry,
       "mldsVlanMulticastGroupVlanId": mldsVlanMulticastGroupVlanId,
       "mldsVlanMulticastGroupIpAddress": mldsVlanMulticastGroupIpAddress,
       "mldsVlanMulticastGroupMacAddress": mldsVlanMulticastGroupMacAddress,
       "mldsVlanMulticastGroupPortList": mldsVlanMulticastGroupPortList,
       "sysMldsHost": sysMldsHost,
       "mldsHostTable": mldsHostTable,
       "mldsHostEntry": mldsHostEntry,
       "mldsHostTableVLANID": mldsHostTableVLANID,
       "mldsHostTableGroupAddress": mldsHostTableGroupAddress,
       "mldsHostTablePort": mldsHostTablePort,
       "mldsHostTableHostIPAddress": mldsHostTableHostIPAddress,
       "companyTraceRoute": companyTraceRoute,
       "sysTraceRouteCtlAddressType": sysTraceRouteCtlAddressType,
       "sysTraceRouteCtlAddress": sysTraceRouteCtlAddress,
       "sysTraceRouteCtlTimeOut": sysTraceRouteCtlTimeOut,
       "sysTraceRouteCtlTTL": sysTraceRouteCtlTTL,
       "sysTraceRouteCtlPort": sysTraceRouteCtlPort,
       "sysTraceRouteCtlProbe": sysTraceRouteCtlProbe,
       "sysTraceRouteCtlAdminStatus": sysTraceRouteCtlAdminStatus,
       "sysTraceRouteHistoryTable": sysTraceRouteHistoryTable,
       "traceRouteHistoryEntry": traceRouteHistoryEntry,
       "traceRouteHistoryIndex": traceRouteHistoryIndex,
       "traceRouteHistoryHopIndex": traceRouteHistoryHopIndex,
       "traceRouteHistoryProbeIndex": traceRouteHistoryProbeIndex,
       "traceRouteHistoryHAddrType": traceRouteHistoryHAddrType,
       "traceRouteHistoryHAddr": traceRouteHistoryHAddr,
       "traceRouteHistoryResponse": traceRouteHistoryResponse,
       "traceRouteHistoryStatus": traceRouteHistoryStatus,
       "companyPPPoE": companyPPPoE,
       "sysPppoeGlobalState": sysPppoeGlobalState,
       "sysPppoePortTable": sysPppoePortTable,
       "pppoePortEntry": pppoePortEntry,
       "pppoePortIndex": pppoePortIndex,
       "pppoePortState": pppoePortState,
       "pppoePortCircuitIDType": pppoePortCircuitIDType,
       "pppoePortUDFString": pppoePortUDFString,
       "companyStatistics": companyStatistics,
       "sysStatisticsTable": sysStatisticsTable,
       "statisticsEntry": statisticsEntry,
       "statisticsIndex": statisticsIndex,
       "statisticsInOctets": statisticsInOctets,
       "statisticsInUcastPkts": statisticsInUcastPkts,
       "statisticsInMcastPkts": statisticsInMcastPkts,
       "statisticsInNUcastPkts": statisticsInNUcastPkts,
       "statisticsInDiscards": statisticsInDiscards,
       "statisticsInErrors": statisticsInErrors,
       "statisticsOutOctets": statisticsOutOctets,
       "statisticsOutUcastPkts": statisticsOutUcastPkts,
       "statisticsOutNUcastPkts": statisticsOutNUcastPkts,
       "statisticsOutErrors": statisticsOutErrors,
       "statisticsOutDiscards": statisticsOutDiscards,
       "statisticsLateCollisions": statisticsLateCollisions,
       "statisticsExcessiveCollisions": statisticsExcessiveCollisions,
       "statisticsFCSErrors": statisticsFCSErrors,
       "statisticsFrameTooLongs": statisticsFrameTooLongs,
       "statisticsEtherUndersizePkts": statisticsEtherUndersizePkts,
       "statisticsEtherOversizePkts": statisticsEtherOversizePkts,
       "statisticsEtherFragments": statisticsEtherFragments,
       "statisticsEtherJabbers": statisticsEtherJabbers,
       "statisticsEtherDropEvents": statisticsEtherDropEvents,
       "statisticsDeferredTransmissions": statisticsDeferredTransmissions,
       "statisticsSingleCollisionFrames": statisticsSingleCollisionFrames,
       "statisticsStatsCollisions": statisticsStatsCollisions,
       "statisticsPkts64Octets": statisticsPkts64Octets,
       "statisticsPkts65to127Octets": statisticsPkts65to127Octets,
       "statisticsPkts128to255Octets": statisticsPkts128to255Octets,
       "statisticsPkts256to511Octets": statisticsPkts256to511Octets,
       "statisticsPkts512to1023Octets": statisticsPkts512to1023Octets,
       "statisticsPkts1024to1518Octets": statisticsPkts1024to1518Octets,
       "sysStatisticsClearTable": sysStatisticsClearTable,
       "statisticsClearEntry": statisticsClearEntry,
       "statisticsClearIndex": statisticsClearIndex,
       "statisticsClearStatus": statisticsClearStatus,
       "companyPing": companyPing,
       "sysPingDestIpType": sysPingDestIpType,
       "sysPingDestIpAddr": sysPingDestIpAddr,
       "sysPingTimeout": sysPingTimeout,
       "sysPingTimes": sysPingTimes,
       "sysPingStart": sysPingStart,
       "sysPingStatus": sysPingStatus,
       "sysPingSuccesses": sysPingSuccesses,
       "companyDDP": companyDDP,
       "sysDDPStatus": sysDDPStatus,
       "sysDDPReportTime": sysDDPReportTime,
       "sysDDPTable": sysDDPTable,
       "ddpEntry": ddpEntry,
       "ddpPort": ddpPort,
       "ddpPortStatus": ddpPortStatus,
       "companySession": companySession,
       "syssessionTable": syssessionTable,
       "syssessionEntry": syssessionEntry,
       "sessionID": sessionID,
       "sessionUserName": sessionUserName,
       "sessionUserPrivilege": sessionUserPrivilege,
       "sessionLoginTime": sessionLoginTime,
       "sessionLiveTime": sessionLiveTime,
       "sessionType": sessionType,
       "sessionIP": sessionIP,
       "companyACL": companyACL,
       "sysAclProfile": sysAclProfile,
       "aclL2ProfileTable": aclL2ProfileTable,
       "aclL2ProfileEntry": aclL2ProfileEntry,
       "aclL2ProfileID": aclL2ProfileID,
       "aclL2RuleCount": aclL2RuleCount,
       "aclL2SrcMacMask": aclL2SrcMacMask,
       "aclL2DstMacMask": aclL2DstMacMask,
       "aclL28021pCheck": aclL28021pCheck,
       "aclL2VlanIdCheck": aclL2VlanIdCheck,
       "aclL2EtherTypeCheck": aclL2EtherTypeCheck,
       "aclL2ProfileStatus": aclL2ProfileStatus,
       "aclL3ProfileTable": aclL3ProfileTable,
       "aclL3ProfileEntry": aclL3ProfileEntry,
       "aclL3ProfileID": aclL3ProfileID,
       "aclL3RuleCount": aclL3RuleCount,
       "aclL3ProfileType": aclL3ProfileType,
       "aclL3Ip4SrcAddrMask": aclL3Ip4SrcAddrMask,
       "aclL3Ip4DstAddrMask": aclL3Ip4DstAddrMask,
       "aclL3Ip4DscpCheck": aclL3Ip4DscpCheck,
       "aclL3Ip4TosCheck": aclL3Ip4TosCheck,
       "aclL3Ip4Protocol": aclL3Ip4Protocol,
       "aclL3Ip4ProtocolMask": aclL3Ip4ProtocolMask,
       "aclL3Ip6SrcAddrMask": aclL3Ip6SrcAddrMask,
       "aclL3Ip6DstAddrMask": aclL3Ip6DstAddrMask,
       "aclL3Ip6TrafficClassCheck": aclL3Ip6TrafficClassCheck,
       "aclL3IcmpTypeCheck": aclL3IcmpTypeCheck,
       "aclL3IcmpCodeCheck": aclL3IcmpCodeCheck,
       "aclL3IgmpTypeCheck": aclL3IgmpTypeCheck,
       "aclL3SrcPortMask": aclL3SrcPortMask,
       "aclL3DstPortMask": aclL3DstPortMask,
       "aclL3TcpFlagCheck": aclL3TcpFlagCheck,
       "aclL3ProfileStatus": aclL3ProfileStatus,
       "sysAclRule": sysAclRule,
       "aclL2RuleTable": aclL2RuleTable,
       "aclL2RuleEntry": aclL2RuleEntry,
       "aclL2RuleProfileID": aclL2RuleProfileID,
       "aclL2RuleAccessID": aclL2RuleAccessID,
       "aclL2VlanId": aclL2VlanId,
       "aclL2SrcMac": aclL2SrcMac,
       "aclL2DstMac": aclL2DstMac,
       "aclL28021p": aclL28021p,
       "aclL2EtherType": aclL2EtherType,
       "aclL2InPortList": aclL2InPortList,
       "aclL2Action": aclL2Action,
       "aclL2RateLimit": aclL2RateLimit,
       "aclL2ReplaceDSCP": aclL2ReplaceDSCP,
       "aclL2RuleStatus": aclL2RuleStatus,
       "aclL3RuleTable": aclL3RuleTable,
       "aclL3RuleEntry": aclL3RuleEntry,
       "aclL3RuleProfileID": aclL3RuleProfileID,
       "aclL3RuleAccessID": aclL3RuleAccessID,
       "aclL3IP4SrcAddr": aclL3IP4SrcAddr,
       "aclL3IP4DstAddr": aclL3IP4DstAddr,
       "aclL3IP4DSCP": aclL3IP4DSCP,
       "aclL3IP4ToS": aclL3IP4ToS,
       "aclL3IP4Protocol": aclL3IP4Protocol,
       "aclL3IP6SrcAddr": aclL3IP6SrcAddr,
       "aclL3IP6DstAddr": aclL3IP6DstAddr,
       "aclL3Ip6TrafficClass": aclL3Ip6TrafficClass,
       "aclL3IcmpType": aclL3IcmpType,
       "aclL3IcmpCode": aclL3IcmpCode,
       "aclL3IgmpType": aclL3IgmpType,
       "aclL3SrcPort": aclL3SrcPort,
       "aclL3DstPort": aclL3DstPort,
       "aclL3TcpFlagURG": aclL3TcpFlagURG,
       "aclL3TcpFlagACK": aclL3TcpFlagACK,
       "aclL3TcpFlagPSH": aclL3TcpFlagPSH,
       "aclL3TcpFlagRST": aclL3TcpFlagRST,
       "aclL3TcpFlagSYN": aclL3TcpFlagSYN,
       "aclL3TcpFlagFIN": aclL3TcpFlagFIN,
       "aclL3InPortList": aclL3InPortList,
       "aclL3Action": aclL3Action,
       "aclL3RateLimit": aclL3RateLimit,
       "aclL3ReplaceDSCP": aclL3ReplaceDSCP,
       "aclL3RuleStatus": aclL3RuleStatus,
       "sysAclStatistic": sysAclStatistic,
       "aclTotalProfile": aclTotalProfile,
       "aclUsedProfile": aclUsedProfile,
       "aclTotalRule": aclTotalRule,
       "aclUsedRule": aclUsedRule,
       "companyCPUACL": companyCPUACL,
       "sysCpuAclProfile": sysCpuAclProfile,
       "cpuAclL2ProfileTable": cpuAclL2ProfileTable,
       "cpuAclL2ProfileEntry": cpuAclL2ProfileEntry,
       "cpuAclL2ProfileID": cpuAclL2ProfileID,
       "cpuAclL2RuleCount": cpuAclL2RuleCount,
       "cpuAclL2SrcMacMask": cpuAclL2SrcMacMask,
       "cpuAclL2DstMacMask": cpuAclL2DstMacMask,
       "cpuAclL28021pCheck": cpuAclL28021pCheck,
       "cpuAclL2VlanIdCheck": cpuAclL2VlanIdCheck,
       "cpuAclL2EtherTypeCheck": cpuAclL2EtherTypeCheck,
       "cpuAclL2ProfileStatus": cpuAclL2ProfileStatus,
       "cpuAclL3ProfileTable": cpuAclL3ProfileTable,
       "cpuAclL3ProfileEntry": cpuAclL3ProfileEntry,
       "cpuAclL3ProfileID": cpuAclL3ProfileID,
       "cpuAclL3RuleCount": cpuAclL3RuleCount,
       "cpuAclL3ProfileType": cpuAclL3ProfileType,
       "cpuAclL3Ip4SrcAddrMask": cpuAclL3Ip4SrcAddrMask,
       "cpuAclL3Ip4DstAddrMask": cpuAclL3Ip4DstAddrMask,
       "cpuAclL3Ip4DscpCheck": cpuAclL3Ip4DscpCheck,
       "cpuAclL3Ip4Protocol": cpuAclL3Ip4Protocol,
       "cpuAclL3Ip4ProtocolMask": cpuAclL3Ip4ProtocolMask,
       "cpuAclL3Ip4IcmpTypeCheck": cpuAclL3Ip4IcmpTypeCheck,
       "cpuAclL3Ip4IcmpCodeCheck": cpuAclL3Ip4IcmpCodeCheck,
       "cpuAclL3Ip4IgmpTypeCheck": cpuAclL3Ip4IgmpTypeCheck,
       "cpuAclL3Ip4SrcPortMask": cpuAclL3Ip4SrcPortMask,
       "cpuAclL3Ip4DstPortMask": cpuAclL3Ip4DstPortMask,
       "cpuAclL3Ip4TcpFlagCheck": cpuAclL3Ip4TcpFlagCheck,
       "cpuAclL3Ip6SrcAddrMask": cpuAclL3Ip6SrcAddrMask,
       "cpuAclL3Ip6DstAddrMask": cpuAclL3Ip6DstAddrMask,
       "cpuAclL3Ip6TrafficClassCheck": cpuAclL3Ip6TrafficClassCheck,
       "cpuAclL3ProfileStatus": cpuAclL3ProfileStatus,
       "sysCpuAclRule": sysCpuAclRule,
       "cpuAclL2RuleTable": cpuAclL2RuleTable,
       "cpuAclL2RuleEntry": cpuAclL2RuleEntry,
       "cpuAclL2RuleProfileID": cpuAclL2RuleProfileID,
       "cpuAclL2RuleAccessID": cpuAclL2RuleAccessID,
       "cpuAclL2VlanId": cpuAclL2VlanId,
       "cpuAclL2SrcMac": cpuAclL2SrcMac,
       "cpuAclL2DstMac": cpuAclL2DstMac,
       "cpuAclL28021p": cpuAclL28021p,
       "cpuAclL2EtherType": cpuAclL2EtherType,
       "cpuAclL2InPortList": cpuAclL2InPortList,
       "cpuAclL2Action": cpuAclL2Action,
       "cpuAclL2RuleStatus": cpuAclL2RuleStatus,
       "cpuAclL3RuleTable": cpuAclL3RuleTable,
       "cpuAclL3RuleEntry": cpuAclL3RuleEntry,
       "cpuAclL3RuleProfileID": cpuAclL3RuleProfileID,
       "cpuAclL3RuleAccessID": cpuAclL3RuleAccessID,
       "cpuAclL3IP4SrcAddr": cpuAclL3IP4SrcAddr,
       "cpuAclL3IP4DstAddr": cpuAclL3IP4DstAddr,
       "cpuAclL3IP4DSCP": cpuAclL3IP4DSCP,
       "cpuAclL3IP4Protocol": cpuAclL3IP4Protocol,
       "cpuAclL3IP4IcmpType": cpuAclL3IP4IcmpType,
       "cpuAclL3IP4IcmpCode": cpuAclL3IP4IcmpCode,
       "cpuAclL3IP4IgmpType": cpuAclL3IP4IgmpType,
       "cpuAclL3IP4SrcPort": cpuAclL3IP4SrcPort,
       "cpuAclL3IP4DstPort": cpuAclL3IP4DstPort,
       "cpuAclL3IP4TcpFlagURG": cpuAclL3IP4TcpFlagURG,
       "cpuAclL3IP4TcpFlagACK": cpuAclL3IP4TcpFlagACK,
       "cpuAclL3IP4TcpFlagPSH": cpuAclL3IP4TcpFlagPSH,
       "cpuAclL3IP4TcpFlagRST": cpuAclL3IP4TcpFlagRST,
       "cpuAclL3IP4TcpFlagSYN": cpuAclL3IP4TcpFlagSYN,
       "cpuAclL3IP4TcpFlagFIN": cpuAclL3IP4TcpFlagFIN,
       "cpuAclL3InPortList": cpuAclL3InPortList,
       "cpuAclL3Action": cpuAclL3Action,
       "cpuAclL3IP6SrcAddr": cpuAclL3IP6SrcAddr,
       "cpuAclL3IP6DstAddr": cpuAclL3IP6DstAddr,
       "cpuAclL3Ip6TrafficClass": cpuAclL3Ip6TrafficClass,
       "cpuAclL3RuleStatus": cpuAclL3RuleStatus,
       "sysCpuAclStatistic": sysCpuAclStatistic,
       "cpuAclTotalProfile": cpuAclTotalProfile,
       "cpuAclUsedProfile": cpuAclUsedProfile,
       "cpuAclTotalRule": cpuAclTotalRule,
       "cpuAclUsedRule": cpuAclUsedRule}
)
