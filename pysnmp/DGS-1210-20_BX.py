# SNMP MIB module (DGS-1210-20_BX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-1210-20_BX
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:39 2024
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
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



class LldpManAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class PortLaMode(Integer32, TextualConvention):
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
        *(("disable", 3),
          ("lacp", 1),
          ("static", 2))
    )



class LacpKey(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
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
_Dlink_DGS12XXSeriesProd_ObjectIdentity = ObjectIdentity
dlink_DGS12XXSeriesProd = _Dlink_DGS12XXSeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76)
)
_Dgs_1210_20bx_ObjectIdentity = ObjectIdentity
dgs_1210_20bx = _Dgs_1210_20bx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14)
)
_CompanySystem_ObjectIdentity = ObjectIdentity
companySystem = _CompanySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1)
)


class _SysSwitchName_Type(DisplayString):
    """Custom type sysSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SysSwitchName_Type.__name__ = "DisplayString"
_SysSwitchName_Object = MibScalar
sysSwitchName = _SysSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 1),
    _SysSwitchName_Type()
)
sysSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSwitchName.setStatus("current")


class _SysHardwareVersion_Type(DisplayString):
    """Custom type sysHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysHardwareVersion_Type.__name__ = "DisplayString"
_SysHardwareVersion_Object = MibScalar
sysHardwareVersion = _SysHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 3),
    _SysFirmwareVersion_Type()
)
sysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareVersion.setStatus("current")


class _SysLoginTimeoutInterval_Type(Integer32):
    """Custom type sysLoginTimeoutInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_SysLoginTimeoutInterval_Type.__name__ = "Integer32"
_SysLoginTimeoutInterval_Object = MibScalar
sysLoginTimeoutInterval = _SysLoginTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 4),
    _SysLoginTimeoutInterval_Type()
)
sysLoginTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginTimeoutInterval.setStatus("current")


class _SysLocationName_Type(DisplayString):
    """Custom type sysLocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SysLocationName_Type.__name__ = "DisplayString"
_SysLocationName_Object = MibScalar
sysLocationName = _SysLocationName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 5),
    _SysLocationName_Type()
)
sysLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationName.setStatus("current")


class _SysGroupInterval_Type(Integer32):
    """Custom type sysGroupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 1225),
    )


_SysGroupInterval_Type.__name__ = "Integer32"
_SysGroupInterval_Object = MibScalar
sysGroupInterval = _SysGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 6),
    _SysGroupInterval_Type()
)
sysGroupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGroupInterval.setStatus("current")


class _SysSystemPassword_Type(DisplayString):
    """Custom type sysSystemPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SysSystemPassword_Type.__name__ = "DisplayString"
_SysSystemPassword_Object = MibScalar
sysSystemPassword = _SysSystemPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 7),
    _SysSystemPassword_Type()
)
sysSystemPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSystemPassword.setStatus("current")


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
        *(("disable", 2),
          ("enable", 1))
    )


_SysSafeGuardEnable_Type.__name__ = "Integer32"
_SysSafeGuardEnable_Object = MibScalar
sysSafeGuardEnable = _SysSafeGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 8),
    _SysSafeGuardEnable_Type()
)
sysSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSafeGuardEnable.setStatus("current")


class _SysRestart_Type(TruthValue):
    """Custom type sysRestart based on TruthValue"""


_SysRestart_Object = MibScalar
sysRestart = _SysRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 9),
    _SysRestart_Type()
)
sysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestart.setStatus("current")


class _SysSave_Type(TruthValue):
    """Custom type sysSave based on TruthValue"""


_SysSave_Object = MibScalar
sysSave = _SysSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 10),
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
        *(("disable", 2),
          ("enable", 1))
    )


_SysJumboFrameEnable_Type.__name__ = "Integer32"
_SysJumboFrameEnable_Object = MibScalar
sysJumboFrameEnable = _SysJumboFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 12),
    _SysJumboFrameEnable_Type()
)
sysJumboFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysJumboFrameEnable.setStatus("current")
_SysPortCtrlTable_Object = MibTable
sysPortCtrlTable = _SysPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13)
)
if mibBuilder.loadTexts:
    sysPortCtrlTable.setStatus("current")
_SysPortCtrlEntry_Object = MibTableRow
sysPortCtrlEntry = _SysPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1)
)
sysPortCtrlEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "sysPortCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysPortCtrlEntry.setStatus("current")


class _SysPortCtrlIndex_Type(Integer32):
    """Custom type sysPortCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysPortCtrlIndex_Type.__name__ = "Integer32"
_SysPortCtrlIndex_Object = MibTableColumn
sysPortCtrlIndex = _SysPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1, 1),
    _SysPortCtrlIndex_Type()
)
sysPortCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlIndex.setStatus("current")


class _SysPortCtrlSpeed_Type(Integer32):
    """Custom type sysPortCtrlSpeed based on Integer32"""
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
          ("disable", 7),
          ("rate1000M-Full", 1),
          ("rate100M-Full", 2),
          ("rate100M-Half", 3),
          ("rate10M-Full", 4),
          ("rate10M-Half", 5))
    )


_SysPortCtrlSpeed_Type.__name__ = "Integer32"
_SysPortCtrlSpeed_Object = MibTableColumn
sysPortCtrlSpeed = _SysPortCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1, 2),
    _SysPortCtrlSpeed_Type()
)
sysPortCtrlSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlSpeed.setStatus("current")


class _SysPortCtrlOperStatus_Type(Integer32):
    """Custom type sysPortCtrlOperStatus based on Integer32"""
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
          ("rate1000M-Full", 2),
          ("rate100M-Full", 3),
          ("rate100M-Half", 4),
          ("rate10M-Full", 5),
          ("rate10M-Half", 6))
    )


_SysPortCtrlOperStatus_Type.__name__ = "Integer32"
_SysPortCtrlOperStatus_Object = MibTableColumn
sysPortCtrlOperStatus = _SysPortCtrlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1, 3),
    _SysPortCtrlOperStatus_Type()
)
sysPortCtrlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlOperStatus.setStatus("current")


class _SysPortCtrlMDI_Type(Integer32):
    """Custom type sysPortCtrlMDI based on Integer32"""
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


_SysPortCtrlMDI_Type.__name__ = "Integer32"
_SysPortCtrlMDI_Object = MibTableColumn
sysPortCtrlMDI = _SysPortCtrlMDI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1, 4),
    _SysPortCtrlMDI_Type()
)
sysPortCtrlMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlMDI.setStatus("current")


class _SysPortCtrlFlowControl_Type(Integer32):
    """Custom type sysPortCtrlFlowControl based on Integer32"""
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


_SysPortCtrlFlowControl_Type.__name__ = "Integer32"
_SysPortCtrlFlowControl_Object = MibTableColumn
sysPortCtrlFlowControl = _SysPortCtrlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1, 5),
    _SysPortCtrlFlowControl_Type()
)
sysPortCtrlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlFlowControl.setStatus("current")


class _SysPortCtrlFlowControlOper_Type(Integer32):
    """Custom type sysPortCtrlFlowControlOper based on Integer32"""
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


_SysPortCtrlFlowControlOper_Type.__name__ = "Integer32"
_SysPortCtrlFlowControlOper_Object = MibTableColumn
sysPortCtrlFlowControlOper = _SysPortCtrlFlowControlOper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1, 6),
    _SysPortCtrlFlowControlOper_Type()
)
sysPortCtrlFlowControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlFlowControlOper.setStatus("current")


class _SysPortCtrlType_Type(Integer32):
    """Custom type sysPortCtrlType based on Integer32"""
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
          ("fiberwith1000BaseSFPModule", 4),
          ("fiberwith100BaseSFPModule", 3),
          ("gigabitethernet", 2))
    )


_SysPortCtrlType_Type.__name__ = "Integer32"
_SysPortCtrlType_Object = MibTableColumn
sysPortCtrlType = _SysPortCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 13, 1, 7),
    _SysPortCtrlType_Type()
)
sysPortCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlType.setStatus("current")


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
        *(("disable", 2),
          ("enable", 1))
    )


_SysDhcpAutoConfiguration_Type.__name__ = "Integer32"
_SysDhcpAutoConfiguration_Object = MibScalar
sysDhcpAutoConfiguration = _SysDhcpAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 1, 14),
    _SysDhcpAutoConfiguration_Type()
)
sysDhcpAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpAutoConfiguration.setStatus("current")
_CompanyIpifGroup_ObjectIdentity = ObjectIdentity
companyIpifGroup = _CompanyIpifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2)
)


class _Ipv4sysIpAddrCfgMode_Type(Integer32):
    """Custom type ipv4sysIpAddrCfgMode based on Integer32"""
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


_Ipv4sysIpAddrCfgMode_Type.__name__ = "Integer32"
_Ipv4sysIpAddrCfgMode_Object = MibScalar
ipv4sysIpAddrCfgMode = _Ipv4sysIpAddrCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 1),
    _Ipv4sysIpAddrCfgMode_Type()
)
ipv4sysIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysIpAddrCfgMode.setStatus("obsolete")
_Ipv4sysIpAddr_Type = IpAddress
_Ipv4sysIpAddr_Object = MibScalar
ipv4sysIpAddr = _Ipv4sysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 2),
    _Ipv4sysIpAddr_Type()
)
ipv4sysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysIpAddr.setStatus("obsolete")
_Ipv4sysIpSubnetMask_Type = IpAddress
_Ipv4sysIpSubnetMask_Object = MibScalar
ipv4sysIpSubnetMask = _Ipv4sysIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 3),
    _Ipv4sysIpSubnetMask_Type()
)
ipv4sysIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysIpSubnetMask.setStatus("obsolete")
_Ipv4sysGateway_Type = IpAddress
_Ipv4sysGateway_Object = MibScalar
ipv4sysGateway = _Ipv4sysGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 4),
    _Ipv4sysGateway_Type()
)
ipv4sysGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysGateway.setStatus("obsolete")
_IpifSupportV4V6Info_ObjectIdentity = ObjectIdentity
ipifSupportV4V6Info = _IpifSupportV4V6Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5)
)


class _SysIpAddrCfgMode_Type(Integer32):
    """Custom type sysIpAddrCfgMode based on Integer32"""
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


_SysIpAddrCfgMode_Type.__name__ = "Integer32"
_SysIpAddrCfgMode_Object = MibScalar
sysIpAddrCfgMode = _SysIpAddrCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 1),
    _SysIpAddrCfgMode_Type()
)
sysIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddrCfgMode.setStatus("current")
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 2),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("current")
_SysIpSubnetMask_Type = IpAddress
_SysIpSubnetMask_Object = MibScalar
sysIpSubnetMask = _SysIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 3),
    _SysIpSubnetMask_Type()
)
sysIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpSubnetMask.setStatus("current")
_SysGateway_Type = IpAddress
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 4),
    _SysGateway_Type()
)
sysGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGateway.setStatus("current")
_IpifName_Type = OctetString
_IpifName_Object = MibScalar
ipifName = _IpifName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 5),
    _IpifName_Type()
)
ipifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifName.setStatus("current")


class _Ipifv6GlobalStatus_Type(Integer32):
    """Custom type ipifv6GlobalStatus based on Integer32"""
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


_Ipifv6GlobalStatus_Type.__name__ = "Integer32"
_Ipifv6GlobalStatus_Object = MibScalar
ipifv6GlobalStatus = _Ipifv6GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 7),
    _Ipifv6GlobalStatus_Type()
)
ipifv6GlobalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifv6GlobalStatus.setStatus("current")


class _Ipifv6DHCPStatus_Type(Integer32):
    """Custom type ipifv6DHCPStatus based on Integer32"""
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


_Ipifv6DHCPStatus_Type.__name__ = "Integer32"
_Ipifv6DHCPStatus_Object = MibScalar
ipifv6DHCPStatus = _Ipifv6DHCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 8),
    _Ipifv6DHCPStatus_Type()
)
ipifv6DHCPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifv6DHCPStatus.setStatus("current")


class _Ipifv6AutolinkloStatus_Type(Integer32):
    """Custom type ipifv6AutolinkloStatus based on Integer32"""
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


_Ipifv6AutolinkloStatus_Type.__name__ = "Integer32"
_Ipifv6AutolinkloStatus_Object = MibScalar
ipifv6AutolinkloStatus = _Ipifv6AutolinkloStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 9),
    _Ipifv6AutolinkloStatus_Type()
)
ipifv6AutolinkloStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifv6AutolinkloStatus.setStatus("current")


class _Ipifv6NSRetransmitTime_Type(Integer32):
    """Custom type ipifv6NSRetransmitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Ipifv6NSRetransmitTime_Type.__name__ = "Integer32"
_Ipifv6NSRetransmitTime_Object = MibScalar
ipifv6NSRetransmitTime = _Ipifv6NSRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 10),
    _Ipifv6NSRetransmitTime_Type()
)
ipifv6NSRetransmitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifv6NSRetransmitTime.setStatus("current")
_Ipifv6DefaultGateway_Type = Ipv6Address
_Ipifv6DefaultGateway_Object = MibScalar
ipifv6DefaultGateway = _Ipifv6DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 11),
    _Ipifv6DefaultGateway_Type()
)
ipifv6DefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifv6DefaultGateway.setStatus("current")
_IpifV6AddressTable_Object = MibTable
ipifV6AddressTable = _IpifV6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 12)
)
if mibBuilder.loadTexts:
    ipifV6AddressTable.setStatus("current")
_IpifV6AddressEntry_Object = MibTableRow
ipifV6AddressEntry = _IpifV6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 12, 1)
)
ipifV6AddressEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "ipifV6AddressMainIndex"),
    (0, "DGS-1210-20_BX", "ipifV6AddressIpAddr"),
    (0, "DGS-1210-20_BX", "ipifV6AddressIpPrefix"),
)
if mibBuilder.loadTexts:
    ipifV6AddressEntry.setStatus("current")
_IpifV6AddressMainIndex_Type = InterfaceIndex
_IpifV6AddressMainIndex_Object = MibTableColumn
ipifV6AddressMainIndex = _IpifV6AddressMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 12, 1, 1),
    _IpifV6AddressMainIndex_Type()
)
ipifV6AddressMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressMainIndex.setStatus("current")


class _IpifV6AddressIpAddr_Type(Ipv6Address):
    """Custom type ipifV6AddressIpAddr based on Ipv6Address"""
    defaultHexValue = "00000000"


_IpifV6AddressIpAddr_Object = MibTableColumn
ipifV6AddressIpAddr = _IpifV6AddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 12, 1, 2),
    _IpifV6AddressIpAddr_Type()
)
ipifV6AddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressIpAddr.setStatus("current")
_IpifV6AddressIpPrefix_Type = Integer32
_IpifV6AddressIpPrefix_Object = MibTableColumn
ipifV6AddressIpPrefix = _IpifV6AddressIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 12, 1, 3),
    _IpifV6AddressIpPrefix_Type()
)
ipifV6AddressIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressIpPrefix.setStatus("current")


class _IpifV6AddressIpType_Type(Integer32):
    """Custom type ipifV6AddressIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 2),
          ("linklocal", 3),
          ("unicast", 1))
    )


_IpifV6AddressIpType_Type.__name__ = "Integer32"
_IpifV6AddressIpType_Object = MibTableColumn
ipifV6AddressIpType = _IpifV6AddressIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 12, 1, 4),
    _IpifV6AddressIpType_Type()
)
ipifV6AddressIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressIpType.setStatus("current")
_IpifV6AddressRowStatus_Type = RowStatus
_IpifV6AddressRowStatus_Object = MibTableColumn
ipifV6AddressRowStatus = _IpifV6AddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 2, 5, 12, 1, 5),
    _IpifV6AddressRowStatus_Type()
)
ipifV6AddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifV6AddressRowStatus.setStatus("current")
_CompanyTftpGroup_ObjectIdentity = ObjectIdentity
companyTftpGroup = _CompanyTftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3)
)
_TftpFwServerIpAddress_Type = IpAddress
_TftpFwServerIpAddress_Object = MibScalar
tftpFwServerIpAddress = _TftpFwServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 1),
    _TftpFwServerIpAddress_Type()
)
tftpFwServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwServerIpAddress.setStatus("obsolete")


class _TftpFwImageFileName_Type(DisplayString):
    """Custom type tftpFwImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TftpFwImageFileName_Type.__name__ = "DisplayString"
_TftpFwImageFileName_Object = MibScalar
tftpFwImageFileName = _TftpFwImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 2),
    _TftpFwImageFileName_Type()
)
tftpFwImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwImageFileName.setStatus("obsolete")


class _TftpFwTftpOperation_Type(Integer32):
    """Custom type tftpFwTftpOperation based on Integer32"""
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


_TftpFwTftpOperation_Type.__name__ = "Integer32"
_TftpFwTftpOperation_Object = MibScalar
tftpFwTftpOperation = _TftpFwTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 3),
    _TftpFwTftpOperation_Type()
)
tftpFwTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTftpOperation.setStatus("obsolete")


class _TftpFwTftpOperationStatus_Type(Integer32):
    """Custom type tftpFwTftpOperationStatus based on Integer32"""
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


_TftpFwTftpOperationStatus_Type.__name__ = "Integer32"
_TftpFwTftpOperationStatus_Object = MibScalar
tftpFwTftpOperationStatus = _TftpFwTftpOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 4),
    _TftpFwTftpOperationStatus_Type()
)
tftpFwTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTftpOperationStatus.setStatus("obsolete")
_TftpCfgServerIpAddress_Type = IpAddress
_TftpCfgServerIpAddress_Object = MibScalar
tftpCfgServerIpAddress = _TftpCfgServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 5),
    _TftpCfgServerIpAddress_Type()
)
tftpCfgServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgServerIpAddress.setStatus("obsolete")


class _TftpConfigFileName_Type(DisplayString):
    """Custom type tftpConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TftpConfigFileName_Type.__name__ = "DisplayString"
_TftpConfigFileName_Object = MibScalar
tftpConfigFileName = _TftpConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 6),
    _TftpConfigFileName_Type()
)
tftpConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConfigFileName.setStatus("obsolete")


class _TftpConfigTftpOperation_Type(Integer32):
    """Custom type tftpConfigTftpOperation based on Integer32"""
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
        *(("download", 1),
          ("none", 0),
          ("progressing", 3),
          ("upload", 2))
    )


_TftpConfigTftpOperation_Type.__name__ = "Integer32"
_TftpConfigTftpOperation_Object = MibScalar
tftpConfigTftpOperation = _TftpConfigTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 7),
    _TftpConfigTftpOperation_Type()
)
tftpConfigTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConfigTftpOperation.setStatus("obsolete")


class _TftpConfigTftpOperationStatus_Type(Integer32):
    """Custom type tftpConfigTftpOperationStatus based on Integer32"""
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


_TftpConfigTftpOperationStatus_Type.__name__ = "Integer32"
_TftpConfigTftpOperationStatus_Object = MibScalar
tftpConfigTftpOperationStatus = _TftpConfigTftpOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 8),
    _TftpConfigTftpOperationStatus_Type()
)
tftpConfigTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpConfigTftpOperationStatus.setStatus("obsolete")
_TftpFwTargetGroup_ObjectIdentity = ObjectIdentity
tftpFwTargetGroup = _TftpFwTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 9)
)
_TftpFwTargetServerIpAddress_Type = Ipv6Address
_TftpFwTargetServerIpAddress_Object = MibScalar
tftpFwTargetServerIpAddress = _TftpFwTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 9, 2),
    _TftpFwTargetServerIpType_Type()
)
tftpFwTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTargetServerIpType.setStatus("current")
_TftpFwTargetInterfaceName_Type = OctetString
_TftpFwTargetInterfaceName_Object = MibScalar
tftpFwTargetInterfaceName = _TftpFwTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 9, 3),
    _TftpFwTargetInterfaceName_Type()
)
tftpFwTargetInterfaceName.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 9, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 9, 6),
    _TftpFwTargetTftpOperationStatus_Type()
)
tftpFwTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTargetTftpOperationStatus.setStatus("current")
_TftpCfgTargetGroup_ObjectIdentity = ObjectIdentity
tftpCfgTargetGroup = _TftpCfgTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 10)
)
_TftpCfgTargetServerIpAddress_Type = Ipv6Address
_TftpCfgTargetServerIpAddress_Object = MibScalar
tftpCfgTargetServerIpAddress = _TftpCfgTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 10, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 10, 2),
    _TftpCfgTargetServerIpType_Type()
)
tftpCfgTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetServerIpType.setStatus("current")
_TftpCfgTargetInterfaceName_Type = OctetString
_TftpCfgTargetInterfaceName_Object = MibScalar
tftpCfgTargetInterfaceName = _TftpCfgTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 10, 4),
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
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("none", 0),
          ("progressing", 3),
          ("upload", 2))
    )


_TftpCfgTargetTftpOperation_Type.__name__ = "Integer32"
_TftpCfgTargetTftpOperation_Object = MibScalar
tftpCfgTargetTftpOperation = _TftpCfgTargetTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 10, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 3, 10, 6),
    _TftpCfgTargetTftpOperationStatus_Type()
)
tftpCfgTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpCfgTargetTftpOperationStatus.setStatus("current")
_CompanyMiscGroup_ObjectIdentity = ObjectIdentity
companyMiscGroup = _CompanyMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 4)
)


class _MiscReset_Type(Integer32):
    """Custom type miscReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("reset", 1))
    )


_MiscReset_Type.__name__ = "Integer32"
_MiscReset_Object = MibScalar
miscReset = _MiscReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 4, 2),
    _MiscReset_Type()
)
miscReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscReset.setStatus("current")


class _MiscStatisticsReset_Type(Integer32):
    """Custom type miscStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("reset", 1))
    )


_MiscStatisticsReset_Type.__name__ = "Integer32"
_MiscStatisticsReset_Object = MibScalar
miscStatisticsReset = _MiscStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 4, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("current")
_CompanyRSTP_ObjectIdentity = ObjectIdentity
companyRSTP = _CompanyRSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6)
)
_StpGlobal_ObjectIdentity = ObjectIdentity
stpGlobal = _StpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1)
)


class _RstpStatus_Type(Integer32):
    """Custom type rstpStatus based on Integer32"""
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


_RstpStatus_Type.__name__ = "Integer32"
_RstpStatus_Object = MibScalar
rstpStatus = _RstpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 1),
    _RstpStatus_Type()
)
rstpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpStatus.setStatus("current")


class _StpVersion_Type(Integer32):
    """Custom type stpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_StpVersion_Type.__name__ = "Integer32"
_StpVersion_Object = MibScalar
stpVersion = _StpVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 2),
    _StpVersion_Type()
)
stpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpVersion.setStatus("current")


class _StpPriority_Type(Integer32):
    """Custom type stpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_StpPriority_Type.__name__ = "Integer32"
_StpPriority_Object = MibScalar
stpPriority = _StpPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 3),
    _StpPriority_Type()
)
stpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPriority.setStatus("current")


class _StpTxHoldCount_Type(Integer32):
    """Custom type stpTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpTxHoldCount_Type.__name__ = "Integer32"
_StpTxHoldCount_Object = MibScalar
stpTxHoldCount = _StpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 4),
    _StpTxHoldCount_Type()
)
stpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpTxHoldCount.setStatus("current")


class _StpProtocolSpecification_Type(Integer32):
    """Custom type stpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_StpProtocolSpecification_Type.__name__ = "Integer32"
_StpProtocolSpecification_Object = MibScalar
stpProtocolSpecification = _StpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 5),
    _StpProtocolSpecification_Type()
)
stpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpProtocolSpecification.setStatus("current")
_StpTimeSinceTopologyChange_Type = TimeTicks
_StpTimeSinceTopologyChange_Object = MibScalar
stpTimeSinceTopologyChange = _StpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 6),
    _StpTimeSinceTopologyChange_Type()
)
stpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTimeSinceTopologyChange.setStatus("current")
_StpTopChanges_Type = Counter32
_StpTopChanges_Object = MibScalar
stpTopChanges = _StpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 7),
    _StpTopChanges_Type()
)
stpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopChanges.setStatus("current")
_StpDesignatedRoot_Type = BridgeId
_StpDesignatedRoot_Object = MibScalar
stpDesignatedRoot = _StpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 8),
    _StpDesignatedRoot_Type()
)
stpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesignatedRoot.setStatus("current")
_StpRootCost_Type = Integer32
_StpRootCost_Object = MibScalar
stpRootCost = _StpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 9),
    _StpRootCost_Type()
)
stpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootCost.setStatus("current")
_StpRootPort_Type = Integer32
_StpRootPort_Object = MibScalar
stpRootPort = _StpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 10),
    _StpRootPort_Type()
)
stpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootPort.setStatus("current")
_StpMaxAge_Type = Timeout
_StpMaxAge_Object = MibScalar
stpMaxAge = _StpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 11),
    _StpMaxAge_Type()
)
stpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpMaxAge.setStatus("current")
_StpHelloTime_Type = Timeout
_StpHelloTime_Object = MibScalar
stpHelloTime = _StpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 12),
    _StpHelloTime_Type()
)
stpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHelloTime.setStatus("current")
_StpHoldTime_Type = Integer32
_StpHoldTime_Object = MibScalar
stpHoldTime = _StpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 13),
    _StpHoldTime_Type()
)
stpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHoldTime.setStatus("current")
_StpForwardDelay_Type = Timeout
_StpForwardDelay_Object = MibScalar
stpForwardDelay = _StpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 14),
    _StpForwardDelay_Type()
)
stpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpForwardDelay.setStatus("current")


class _StpBridgeMaxAge_Type(Timeout):
    """Custom type stpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_StpBridgeMaxAge_Type.__name__ = "Timeout"
_StpBridgeMaxAge_Object = MibScalar
stpBridgeMaxAge = _StpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 15),
    _StpBridgeMaxAge_Type()
)
stpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeMaxAge.setStatus("current")


class _StpBridgeHelloTime_Type(Timeout):
    """Custom type stpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_StpBridgeHelloTime_Type.__name__ = "Timeout"
_StpBridgeHelloTime_Object = MibScalar
stpBridgeHelloTime = _StpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 16),
    _StpBridgeHelloTime_Type()
)
stpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeHelloTime.setStatus("current")


class _StpBridgeForwardDelay_Type(Timeout):
    """Custom type stpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_StpBridgeForwardDelay_Type.__name__ = "Timeout"
_StpBridgeForwardDelay_Object = MibScalar
stpBridgeForwardDelay = _StpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 1, 17),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("current")
_StpPortEntry_Object = MibTableRow
stpPortEntry = _StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1)
)
stpPortEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "stpPort"),
)
if mibBuilder.loadTexts:
    stpPortEntry.setStatus("current")


class _StpPort_Type(Integer32):
    """Custom type stpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpPort_Type.__name__ = "Integer32"
_StpPort_Object = MibTableColumn
stpPort = _StpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 1),
    _StpPort_Type()
)
stpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPort.setStatus("current")


class _StpPortPriority_Type(Integer32):
    """Custom type stpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_StpPortPriority_Type.__name__ = "Integer32"
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 2),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("current")


class _StpPortState_Type(Integer32):
    """Custom type stpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_StpPortState_Type.__name__ = "Integer32"
_StpPortState_Object = MibTableColumn
stpPortState = _StpPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 3),
    _StpPortState_Type()
)
stpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortState.setStatus("current")


class _StpPortEnable_Type(Integer32):
    """Custom type stpPortEnable based on Integer32"""
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


_StpPortEnable_Type.__name__ = "Integer32"
_StpPortEnable_Object = MibTableColumn
stpPortEnable = _StpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 4),
    _StpPortEnable_Type()
)
stpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEnable.setStatus("current")


class _StpAdminPortPathCost_Type(Integer32):
    """Custom type stpAdminPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_StpAdminPortPathCost_Type.__name__ = "Integer32"
_StpAdminPortPathCost_Object = MibTableColumn
stpAdminPortPathCost = _StpAdminPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 5),
    _StpAdminPortPathCost_Type()
)
stpAdminPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpAdminPortPathCost.setStatus("current")


class _StpPortPathCost_Type(Integer32):
    """Custom type stpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StpPortPathCost_Type.__name__ = "Integer32"
_StpPortPathCost_Object = MibTableColumn
stpPortPathCost = _StpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 6),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortDesignatedRoot_Type = BridgeId
_StpPortDesignatedRoot_Object = MibTableColumn
stpPortDesignatedRoot = _StpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 7),
    _StpPortDesignatedRoot_Type()
)
stpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedRoot.setStatus("current")
_StpPortDesignatedCost_Type = Integer32
_StpPortDesignatedCost_Object = MibTableColumn
stpPortDesignatedCost = _StpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 8),
    _StpPortDesignatedCost_Type()
)
stpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedCost.setStatus("current")
_StpPortDesignatedBridge_Type = BridgeId
_StpPortDesignatedBridge_Object = MibTableColumn
stpPortDesignatedBridge = _StpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 9),
    _StpPortDesignatedBridge_Type()
)
stpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedBridge.setStatus("current")


class _StpPortDesignatedPort_Type(OctetString):
    """Custom type stpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_StpPortDesignatedPort_Type.__name__ = "OctetString"
_StpPortDesignatedPort_Object = MibTableColumn
stpPortDesignatedPort = _StpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 10),
    _StpPortDesignatedPort_Type()
)
stpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedPort.setStatus("current")
_StpPortForwardTransitions_Type = Counter32
_StpPortForwardTransitions_Object = MibTableColumn
stpPortForwardTransitions = _StpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 11),
    _StpPortForwardTransitions_Type()
)
stpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortForwardTransitions.setStatus("current")
_StpPortProtocolMigration_Type = TruthValue
_StpPortProtocolMigration_Object = MibTableColumn
stpPortProtocolMigration = _StpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 12),
    _StpPortProtocolMigration_Type()
)
stpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortProtocolMigration.setStatus("current")
_StpPortOperEdgePort_Type = TruthValue
_StpPortOperEdgePort_Object = MibTableColumn
stpPortOperEdgePort = _StpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 13),
    _StpPortOperEdgePort_Type()
)
stpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortOperEdgePort.setStatus("current")


class _StpPortAdminPointToPoint_Type(Integer32):
    """Custom type stpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_StpPortAdminPointToPoint_Type.__name__ = "Integer32"
_StpPortAdminPointToPoint_Object = MibTableColumn
stpPortAdminPointToPoint = _StpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 14),
    _StpPortAdminPointToPoint_Type()
)
stpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortAdminPointToPoint.setStatus("current")
_StpPortOperPointToPoint_Type = TruthValue
_StpPortOperPointToPoint_Object = MibTableColumn
stpPortOperPointToPoint = _StpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 15),
    _StpPortOperPointToPoint_Type()
)
stpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortOperPointToPoint.setStatus("current")


class _StpPortEdge_Type(Integer32):
    """Custom type stpPortEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("false", 0),
          ("true", 1))
    )


_StpPortEdge_Type.__name__ = "Integer32"
_StpPortEdge_Object = MibTableColumn
stpPortEdge = _StpPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 16),
    _StpPortEdge_Type()
)
stpPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEdge.setStatus("current")
_StpPortRestrictedRole_Type = TruthValue
_StpPortRestrictedRole_Object = MibTableColumn
stpPortRestrictedRole = _StpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 17),
    _StpPortRestrictedRole_Type()
)
stpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedRole.setStatus("current")
_StpPortRestrictedTCN_Type = TruthValue
_StpPortRestrictedTCN_Object = MibTableColumn
stpPortRestrictedTCN = _StpPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 6, 2, 1, 18),
    _StpPortRestrictedTCN_Type()
)
stpPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedTCN.setStatus("current")
_CompanyDot1qVlanGroup_ObjectIdentity = ObjectIdentity
companyDot1qVlanGroup = _CompanyDot1qVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7)
)


class _Dot1qVlanManagementOnOff_Type(Integer32):
    """Custom type dot1qVlanManagementOnOff based on Integer32"""
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


_Dot1qVlanManagementOnOff_Type.__name__ = "Integer32"
_Dot1qVlanManagementOnOff_Object = MibScalar
dot1qVlanManagementOnOff = _Dot1qVlanManagementOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 2),
    _Dot1qVlanManagementOnOff_Type()
)
dot1qVlanManagementOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanManagementOnOff.setStatus("current")


class _Dot1qVlanManagementid_Type(Integer32):
    """Custom type dot1qVlanManagementid based on Integer32"""
    defaultValue = 1


_Dot1qVlanManagementid_Object = MibScalar
dot1qVlanManagementid = _Dot1qVlanManagementid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 3),
    _Dot1qVlanManagementid_Type()
)
dot1qVlanManagementid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanManagementid.setStatus("current")


class _Dot1qVlanAsyOnOff_Type(Integer32):
    """Custom type dot1qVlanAsyOnOff based on Integer32"""
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


_Dot1qVlanAsyOnOff_Type.__name__ = "Integer32"
_Dot1qVlanAsyOnOff_Object = MibScalar
dot1qVlanAsyOnOff = _Dot1qVlanAsyOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 5),
    _Dot1qVlanAsyOnOff_Type()
)
dot1qVlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanAsyOnOff.setStatus("current")
_Dot1qVlanTable_Object = MibTable
dot1qVlanTable = _Dot1qVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 6)
)
if mibBuilder.loadTexts:
    dot1qVlanTable.setStatus("current")
_Dot1qVlanEntry_Object = MibTableRow
dot1qVlanEntry = _Dot1qVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 6, 1)
)
dot1qVlanEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "dot1qVlanName"),
)
if mibBuilder.loadTexts:
    dot1qVlanEntry.setStatus("current")


class _Dot1qVlanName_Type(SnmpAdminString):
    """Custom type dot1qVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Dot1qVlanName_Type.__name__ = "SnmpAdminString"
_Dot1qVlanName_Object = MibTableColumn
dot1qVlanName = _Dot1qVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 6, 1, 1),
    _Dot1qVlanName_Type()
)
dot1qVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanName.setStatus("current")
_Dot1qVlanEgressPorts_Type = PortList
_Dot1qVlanEgressPorts_Object = MibTableColumn
dot1qVlanEgressPorts = _Dot1qVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 6, 1, 2),
    _Dot1qVlanEgressPorts_Type()
)
dot1qVlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanEgressPorts.setStatus("current")
_Dot1qVlanUntaggedPorts_Type = PortList
_Dot1qVlanUntaggedPorts_Object = MibTableColumn
dot1qVlanUntaggedPorts = _Dot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 6, 1, 4),
    _Dot1qVlanUntaggedPorts_Type()
)
dot1qVlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanUntaggedPorts.setStatus("current")
_Dot1qVlanRowStatus_Type = RowStatus
_Dot1qVlanRowStatus_Object = MibTableColumn
dot1qVlanRowStatus = _Dot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 6, 1, 5),
    _Dot1qVlanRowStatus_Type()
)
dot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanRowStatus.setStatus("current")
_Dot1qVlanPortTable_Object = MibTable
dot1qVlanPortTable = _Dot1qVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 7)
)
if mibBuilder.loadTexts:
    dot1qVlanPortTable.setStatus("current")
_Dot1qVlanPortEntry_Object = MibTableRow
dot1qVlanPortEntry = _Dot1qVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 7, 1)
)
if mibBuilder.loadTexts:
    dot1qVlanPortEntry.setStatus("current")


class _Dot1qVlanPvid_Type(VlanIndex):
    """Custom type dot1qVlanPvid based on VlanIndex"""
    defaultValue = 1


_Dot1qVlanPvid_Object = MibTableColumn
dot1qVlanPvid = _Dot1qVlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 7, 1, 1),
    _Dot1qVlanPvid_Type()
)
dot1qVlanPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPvid.setStatus("current")
_Dot1qVlanUngisterMCFilterTable_Object = MibTable
dot1qVlanUngisterMCFilterTable = _Dot1qVlanUngisterMCFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 8)
)
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFilterTable.setStatus("current")
_Dot1qVlanUngisterMCFilterEntry_Object = MibTableRow
dot1qVlanUngisterMCFilterEntry = _Dot1qVlanUngisterMCFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 8, 1)
)
dot1qVlanUngisterMCFilterEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "dot1qVlanUngisterMCFilterVlanId"),
)
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFilterEntry.setStatus("current")


class _Dot1qVlanUngisterMCFilterVlanId_Type(Integer32):
    """Custom type dot1qVlanUngisterMCFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot1qVlanUngisterMCFilterVlanId_Type.__name__ = "Integer32"
_Dot1qVlanUngisterMCFilterVlanId_Object = MibTableColumn
dot1qVlanUngisterMCFilterVlanId = _Dot1qVlanUngisterMCFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 8, 1, 1),
    _Dot1qVlanUngisterMCFilterVlanId_Type()
)
dot1qVlanUngisterMCFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFilterVlanId.setStatus("current")


class _Dot1qVlanUngisterMCFiltermode_Type(Integer32):
    """Custom type dot1qVlanUngisterMCFiltermode based on Integer32"""
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


_Dot1qVlanUngisterMCFiltermode_Type.__name__ = "Integer32"
_Dot1qVlanUngisterMCFiltermode_Object = MibTableColumn
dot1qVlanUngisterMCFiltermode = _Dot1qVlanUngisterMCFiltermode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 7, 8, 1, 2),
    _Dot1qVlanUngisterMCFiltermode_Type()
)
dot1qVlanUngisterMCFiltermode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFiltermode.setStatus("current")
_CompanyLA_ObjectIdentity = ObjectIdentity
companyLA = _CompanyLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8)
)
_LaSystem_ObjectIdentity = ObjectIdentity
laSystem = _LaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 1)
)


class _LaStatus_Type(Integer32):
    """Custom type laStatus based on Integer32"""
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


_LaStatus_Type.__name__ = "Integer32"
_LaStatus_Object = MibScalar
laStatus = _LaStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 1, 2),
    _LaStatus_Type()
)
laStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laStatus.setStatus("current")
_LaPortChannelTable_Object = MibTable
laPortChannelTable = _LaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 1, 3)
)
if mibBuilder.loadTexts:
    laPortChannelTable.setStatus("current")
_LaPortChannelEntry_Object = MibTableRow
laPortChannelEntry = _LaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 1, 3, 1)
)
laPortChannelEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "laPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    laPortChannelEntry.setStatus("current")
_LaPortChannelIfIndex_Type = InterfaceIndex
_LaPortChannelIfIndex_Object = MibTableColumn
laPortChannelIfIndex = _LaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 1, 3, 1, 1),
    _LaPortChannelIfIndex_Type()
)
laPortChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortChannelIfIndex.setStatus("current")
_LaPortChannelMemberList_Type = PortList
_LaPortChannelMemberList_Object = MibTableColumn
laPortChannelMemberList = _LaPortChannelMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 1, 3, 1, 2),
    _LaPortChannelMemberList_Type()
)
laPortChannelMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMemberList.setStatus("current")
_LaPortChannelMode_Type = PortLaMode
_LaPortChannelMode_Object = MibTableColumn
laPortChannelMode = _LaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 1, 3, 1, 3),
    _LaPortChannelMode_Type()
)
laPortChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMode.setStatus("current")
_LaPortControl_ObjectIdentity = ObjectIdentity
laPortControl = _LaPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 2)
)
_LaPortControlTable_Object = MibTable
laPortControlTable = _LaPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 2, 1)
)
if mibBuilder.loadTexts:
    laPortControlTable.setStatus("current")
_LaPortControlEntry_Object = MibTableRow
laPortControlEntry = _LaPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 2, 1, 1)
)
laPortControlEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "laPortControlIndex"),
)
if mibBuilder.loadTexts:
    laPortControlEntry.setStatus("current")
_LaPortControlIndex_Type = InterfaceIndex
_LaPortControlIndex_Object = MibTableColumn
laPortControlIndex = _LaPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 2, 1, 1, 1),
    _LaPortControlIndex_Type()
)
laPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortControlIndex.setStatus("current")


class _LaPortActorActivity_Type(Integer32):
    """Custom type laPortActorActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_LaPortActorActivity_Type.__name__ = "Integer32"
_LaPortActorActivity_Object = MibTableColumn
laPortActorActivity = _LaPortActorActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 2, 1, 1, 3),
    _LaPortActorActivity_Type()
)
laPortActorActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortActorActivity.setStatus("current")


class _LaPortActorTimeout_Type(Integer32):
    """Custom type laPortActorTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_LaPortActorTimeout_Type.__name__ = "Integer32"
_LaPortActorTimeout_Object = MibTableColumn
laPortActorTimeout = _LaPortActorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 8, 2, 1, 1, 4),
    _LaPortActorTimeout_Type()
)
laPortActorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortActorTimeout.setStatus("current")
_CompanyStaticMAC_ObjectIdentity = ObjectIdentity
companyStaticMAC = _CompanyStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9)
)


class _StaticDisableAutoLearn_Type(Integer32):
    """Custom type staticDisableAutoLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StaticDisableAutoLearn_Type.__name__ = "Integer32"
_StaticDisableAutoLearn_Object = MibScalar
staticDisableAutoLearn = _StaticDisableAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 1),
    _StaticDisableAutoLearn_Type()
)
staticDisableAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDisableAutoLearn.setStatus("current")
_StaticAutoLearningList_Type = PortList
_StaticAutoLearningList_Object = MibScalar
staticAutoLearningList = _StaticAutoLearningList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 2),
    _StaticAutoLearningList_Type()
)
staticAutoLearningList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticAutoLearningList.setStatus("current")
_StaticTable_Object = MibTable
staticTable = _StaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 3)
)
if mibBuilder.loadTexts:
    staticTable.setStatus("current")
_StaticEntry_Object = MibTableRow
staticEntry = _StaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 3, 1)
)
staticEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "staticVlanID"),
    (0, "DGS-1210-20_BX", "staticMac"),
    (0, "DGS-1210-20_BX", "staticPort"),
)
if mibBuilder.loadTexts:
    staticEntry.setStatus("current")
_StaticVlanID_Type = Integer32
_StaticVlanID_Object = MibTableColumn
staticVlanID = _StaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 3, 1, 1),
    _StaticVlanID_Type()
)
staticVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticVlanID.setStatus("current")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 3, 1, 2),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMac.setStatus("current")
_StaticPort_Type = Integer32
_StaticPort_Object = MibTableColumn
staticPort = _StaticPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 3, 1, 3),
    _StaticPort_Type()
)
staticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticPort.setStatus("current")
_StaticStatus_Type = RowStatus
_StaticStatus_Object = MibTableColumn
staticStatus = _StaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 9, 3, 1, 4),
    _StaticStatus_Type()
)
staticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticStatus.setStatus("current")
_CompanyIgsGroup_ObjectIdentity = ObjectIdentity
companyIgsGroup = _CompanyIgsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10)
)
_IgsSystem_ObjectIdentity = ObjectIdentity
igsSystem = _IgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 1),
    _IgsStatus_Type()
)
igsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsStatus.setStatus("current")


class _IgsRouterPortPurgeInterval_Type(Integer32):
    """Custom type igsRouterPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_IgsRouterPortPurgeInterval_Type.__name__ = "Integer32"
_IgsRouterPortPurgeInterval_Object = MibScalar
igsRouterPortPurgeInterval = _IgsRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 2),
    _IgsRouterPortPurgeInterval_Type()
)
igsRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsRouterPortPurgeInterval.setStatus("current")


class _IgsHostPortPurgeInterval_Type(Integer32):
    """Custom type igsHostPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 153025),
    )


_IgsHostPortPurgeInterval_Type.__name__ = "Integer32"
_IgsHostPortPurgeInterval_Object = MibScalar
igsHostPortPurgeInterval = _IgsHostPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 3),
    _IgsHostPortPurgeInterval_Type()
)
igsHostPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsHostPortPurgeInterval.setStatus("current")


class _IgsRobustnessValue_Type(Integer32):
    """Custom type igsRobustnessValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_IgsRobustnessValue_Type.__name__ = "Integer32"
_IgsRobustnessValue_Object = MibScalar
igsRobustnessValue = _IgsRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 4),
    _IgsRobustnessValue_Type()
)
igsRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsRobustnessValue.setStatus("current")


class _IgsGrpQueryInterval_Type(Integer32):
    """Custom type igsGrpQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_IgsGrpQueryInterval_Type.__name__ = "Integer32"
_IgsGrpQueryInterval_Object = MibScalar
igsGrpQueryInterval = _IgsGrpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 5),
    _IgsGrpQueryInterval_Type()
)
igsGrpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsGrpQueryInterval.setStatus("current")


class _IgsQueryInterval_Type(Integer32):
    """Custom type igsQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_IgsQueryInterval_Type.__name__ = "Integer32"
_IgsQueryInterval_Object = MibScalar
igsQueryInterval = _IgsQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 6),
    _IgsQueryInterval_Type()
)
igsQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsQueryInterval.setStatus("current")


class _IgsQueryMaxResponseTime_Type(Integer32):
    """Custom type igsQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 25),
    )


_IgsQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgsQueryMaxResponseTime_Object = MibScalar
igsQueryMaxResponseTime = _IgsQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 7),
    _IgsQueryMaxResponseTime_Type()
)
igsQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsQueryMaxResponseTime.setStatus("current")


class _IgsReportToAllPort_Type(Integer32):
    """Custom type igsReportToAllPort based on Integer32"""
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


_IgsReportToAllPort_Type.__name__ = "Integer32"
_IgsReportToAllPort_Object = MibScalar
igsReportToAllPort = _IgsReportToAllPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 1, 8),
    _IgsReportToAllPort_Type()
)
igsReportToAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsReportToAllPort.setStatus("current")
_IgsVlan_ObjectIdentity = ObjectIdentity
igsVlan = _IgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3)
)
_IgsVlanRouterTable_Object = MibTable
igsVlanRouterTable = _IgsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 3)
)
if mibBuilder.loadTexts:
    igsVlanRouterTable.setStatus("current")
_IgsVlanRouterEntry_Object = MibTableRow
igsVlanRouterEntry = _IgsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 3, 1)
)
igsVlanRouterEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "igsVlanRouterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 3, 1, 1),
    _IgsVlanRouterVlanId_Type()
)
igsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterVlanId.setStatus("current")
_IgsVlanRouterPortList_Type = PortList
_IgsVlanRouterPortList_Object = MibTableColumn
igsVlanRouterPortList = _IgsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 3, 1, 2),
    _IgsVlanRouterPortList_Type()
)
igsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterPortList.setStatus("current")
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("current")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "igsVlanFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1, 1),
    _IgsVlanFilterVlanId_Type()
)
igsVlanFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanFilterVlanId.setStatus("current")


class _IgsVlanSnoopStatus_Type(Integer32):
    """Custom type igsVlanSnoopStatus based on Integer32"""
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


_IgsVlanSnoopStatus_Type.__name__ = "Integer32"
_IgsVlanSnoopStatus_Object = MibTableColumn
igsVlanSnoopStatus = _IgsVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1, 5),
    _IgsVlanQueryInterval_Type()
)
igsVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanQueryInterval.setStatus("current")
_IgsVlanRtrPortList_Type = PortList
_IgsVlanRtrPortList_Object = MibTableColumn
igsVlanRtrPortList = _IgsVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1, 6),
    _IgsVlanRtrPortList_Type()
)
igsVlanRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanRtrPortList.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 4, 1, 8),
    _IgsVlanFastLeave_Type()
)
igsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFastLeave.setStatus("current")
_IgsVlanMulticastGroupTable_Object = MibTable
igsVlanMulticastGroupTable = _IgsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 5)
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupTable.setStatus("current")
_IgsVlanMulticastGroupEntry_Object = MibTableRow
igsVlanMulticastGroupEntry = _IgsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 5, 1)
)
igsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "igsVlanMulticastGroupVlanId"),
    (0, "DGS-1210-20_BX", "igsVlanMulticastGroupIpAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 5, 1, 1),
    _IgsVlanMulticastGroupVlanId_Type()
)
igsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupVlanId.setStatus("current")
_IgsVlanMulticastGroupIpAddress_Type = InetAddress
_IgsVlanMulticastGroupIpAddress_Object = MibTableColumn
igsVlanMulticastGroupIpAddress = _IgsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 5, 1, 2),
    _IgsVlanMulticastGroupIpAddress_Type()
)
igsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupIpAddress.setStatus("current")
_IgsVlanMulticastGroupMacAddress_Type = MacAddress
_IgsVlanMulticastGroupMacAddress_Object = MibTableColumn
igsVlanMulticastGroupMacAddress = _IgsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 5, 1, 3),
    _IgsVlanMulticastGroupMacAddress_Type()
)
igsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupMacAddress.setStatus("current")
_IgsVlanMulticastGroupPortList_Type = PortList
_IgsVlanMulticastGroupPortList_Object = MibTableColumn
igsVlanMulticastGroupPortList = _IgsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 10, 3, 5, 1, 4),
    _IgsVlanMulticastGroupPortList_Type()
)
igsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupPortList.setStatus("current")
_CompanyDot1xGroup_ObjectIdentity = ObjectIdentity
companyDot1xGroup = _CompanyDot1xGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11)
)
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1)
)
_Ipv4radiusServerAddress_Type = IpAddress
_Ipv4radiusServerAddress_Object = MibScalar
ipv4radiusServerAddress = _Ipv4radiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1, 1),
    _Ipv4radiusServerAddress_Type()
)
ipv4radiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4radiusServerAddress.setStatus("obsolete")


class _Ipv4radiusServerSharedSecret_Type(DisplayString):
    """Custom type ipv4radiusServerSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Ipv4radiusServerSharedSecret_Type.__name__ = "DisplayString"
_Ipv4radiusServerSharedSecret_Object = MibScalar
ipv4radiusServerSharedSecret = _Ipv4radiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1, 2),
    _Ipv4radiusServerSharedSecret_Type()
)
ipv4radiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4radiusServerSharedSecret.setStatus("obsolete")
_RadiusServerTable_ObjectIdentity = ObjectIdentity
radiusServerTable = _RadiusServerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1, 3)
)


class _SwRadiusServerIPType_Type(Integer32):
    """Custom type swRadiusServerIPType based on Integer32"""
    defaultValue = 1

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


_SwRadiusServerIPType_Type.__name__ = "Integer32"
_SwRadiusServerIPType_Object = MibScalar
swRadiusServerIPType = _SwRadiusServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1, 3, 1),
    _SwRadiusServerIPType_Type()
)
swRadiusServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusServerIPType.setStatus("current")
_SwRadiusServerAddress_Type = Ipv6Address
_SwRadiusServerAddress_Object = MibScalar
swRadiusServerAddress = _SwRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1, 3, 2),
    _SwRadiusServerAddress_Type()
)
swRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusServerAddress.setStatus("current")
_SwRadiusServerInterfaceName_Type = OctetString
_SwRadiusServerInterfaceName_Object = MibScalar
swRadiusServerInterfaceName = _SwRadiusServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1, 3, 3),
    _SwRadiusServerInterfaceName_Type()
)
swRadiusServerInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRadiusServerInterfaceName.setStatus("current")


class _SwRadiusServerSharedSecret_Type(DisplayString):
    """Custom type swRadiusServerSharedSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwRadiusServerSharedSecret_Type.__name__ = "DisplayString"
_SwRadiusServerSharedSecret_Object = MibScalar
swRadiusServerSharedSecret = _SwRadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 1, 3, 4),
    _SwRadiusServerSharedSecret_Type()
)
swRadiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusServerSharedSecret.setStatus("current")
_Dot1xAuth_ObjectIdentity = ObjectIdentity
dot1xAuth = _Dot1xAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2)
)


class _Dot1xAuthStatus_Type(Integer32):
    """Custom type dot1xAuthStatus based on Integer32"""
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


_Dot1xAuthStatus_Type.__name__ = "Integer32"
_Dot1xAuthStatus_Object = MibScalar
dot1xAuthStatus = _Dot1xAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 1),
    _Dot1xAuthStatus_Type()
)
dot1xAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthStatus.setStatus("current")


class _Dot1xAuthQuietPeriod_Type(Integer32):
    """Custom type dot1xAuthQuietPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1xAuthQuietPeriod_Type.__name__ = "Integer32"
_Dot1xAuthQuietPeriod_Object = MibScalar
dot1xAuthQuietPeriod = _Dot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 2),
    _Dot1xAuthQuietPeriod_Type()
)
dot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthQuietPeriod.setStatus("current")


class _Dot1xAuthTxPeriod_Type(Integer32):
    """Custom type dot1xAuthTxPeriod based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xAuthTxPeriod_Type.__name__ = "Integer32"
_Dot1xAuthTxPeriod_Object = MibScalar
dot1xAuthTxPeriod = _Dot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 3),
    _Dot1xAuthTxPeriod_Type()
)
dot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthTxPeriod.setStatus("current")


class _Dot1xAuthSuppTimeout_Type(Integer32):
    """Custom type dot1xAuthSuppTimeout based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xAuthSuppTimeout_Type.__name__ = "Integer32"
_Dot1xAuthSuppTimeout_Object = MibScalar
dot1xAuthSuppTimeout = _Dot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 4),
    _Dot1xAuthSuppTimeout_Type()
)
dot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthSuppTimeout.setStatus("current")


class _Dot1xAuthServerTimeout_Type(Integer32):
    """Custom type dot1xAuthServerTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xAuthServerTimeout_Type.__name__ = "Integer32"
_Dot1xAuthServerTimeout_Object = MibScalar
dot1xAuthServerTimeout = _Dot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 5),
    _Dot1xAuthServerTimeout_Type()
)
dot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthServerTimeout.setStatus("current")


class _Dot1xAuthMaxReq_Type(Integer32):
    """Custom type dot1xAuthMaxReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1xAuthMaxReq_Type.__name__ = "Integer32"
_Dot1xAuthMaxReq_Object = MibScalar
dot1xAuthMaxReq = _Dot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 6),
    _Dot1xAuthMaxReq_Type()
)
dot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthMaxReq.setStatus("current")


class _Dot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type dot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1xAuthReAuthPeriod_Type.__name__ = "Unsigned32"
_Dot1xAuthReAuthPeriod_Object = MibScalar
dot1xAuthReAuthPeriod = _Dot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 7),
    _Dot1xAuthReAuthPeriod_Type()
)
dot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthReAuthPeriod.setStatus("current")


class _Dot1xAuthReAuthEnabled_Type(Integer32):
    """Custom type dot1xAuthReAuthEnabled based on Integer32"""
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


_Dot1xAuthReAuthEnabled_Type.__name__ = "Integer32"
_Dot1xAuthReAuthEnabled_Object = MibScalar
dot1xAuthReAuthEnabled = _Dot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 8),
    _Dot1xAuthReAuthEnabled_Type()
)
dot1xAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthReAuthEnabled.setStatus("current")
_Dot1xAuthConfigPortTable_Object = MibTable
dot1xAuthConfigPortTable = _Dot1xAuthConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 9)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigPortTable.setStatus("current")
_Dot1xAuthConfigPortEntry_Object = MibTableRow
dot1xAuthConfigPortEntry = _Dot1xAuthConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 9, 1)
)
dot1xAuthConfigPortEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "dot1xAuthConfigPortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthConfigPortEntry.setStatus("current")
_Dot1xAuthConfigPortNumber_Type = Integer32
_Dot1xAuthConfigPortNumber_Object = MibTableColumn
dot1xAuthConfigPortNumber = _Dot1xAuthConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 9, 1, 1),
    _Dot1xAuthConfigPortNumber_Type()
)
dot1xAuthConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortNumber.setStatus("current")


class _Dot1xAuthConfigPortControl_Type(Integer32):
    """Custom type dot1xAuthConfigPortControl based on Integer32"""
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


_Dot1xAuthConfigPortControl_Type.__name__ = "Integer32"
_Dot1xAuthConfigPortControl_Object = MibTableColumn
dot1xAuthConfigPortControl = _Dot1xAuthConfigPortControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 9, 1, 2),
    _Dot1xAuthConfigPortControl_Type()
)
dot1xAuthConfigPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortControl.setStatus("current")


class _Dot1xAuthConfigPortStatus_Type(Integer32):
    """Custom type dot1xAuthConfigPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )


_Dot1xAuthConfigPortStatus_Type.__name__ = "Integer32"
_Dot1xAuthConfigPortStatus_Object = MibTableColumn
dot1xAuthConfigPortStatus = _Dot1xAuthConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 9, 1, 3),
    _Dot1xAuthConfigPortStatus_Type()
)
dot1xAuthConfigPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortStatus.setStatus("current")
_Dot1xAuthConfigPortSessionTime_Type = TimeTicks
_Dot1xAuthConfigPortSessionTime_Object = MibTableColumn
dot1xAuthConfigPortSessionTime = _Dot1xAuthConfigPortSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 9, 1, 4),
    _Dot1xAuthConfigPortSessionTime_Type()
)
dot1xAuthConfigPortSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortSessionTime.setStatus("current")
_Dot1xAuthConfigPortSessionUserName_Type = SnmpAdminString
_Dot1xAuthConfigPortSessionUserName_Object = MibTableColumn
dot1xAuthConfigPortSessionUserName = _Dot1xAuthConfigPortSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 11, 2, 9, 1, 5),
    _Dot1xAuthConfigPortSessionUserName_Type()
)
dot1xAuthConfigPortSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortSessionUserName.setStatus("current")
_CompanyQoSGroup_ObjectIdentity = ObjectIdentity
companyQoSGroup = _CompanyQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12)
)


class _QosMode_Type(Integer32):
    """Custom type qosMode based on Integer32"""
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
          ("tos", 3))
    )


_QosMode_Type.__name__ = "Integer32"
_QosMode_Object = MibScalar
qosMode = _QosMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 1),
    _QosMode_Type()
)
qosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMode.setStatus("current")


class _QueuingMechanism_Type(Integer32):
    """Custom type queuingMechanism based on Integer32"""
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


_QueuingMechanism_Type.__name__ = "Integer32"
_QueuingMechanism_Object = MibScalar
queuingMechanism = _QueuingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 2),
    _QueuingMechanism_Type()
)
queuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMechanism.setStatus("current")
_QosQ1p_ObjectIdentity = ObjectIdentity
qosQ1p = _QosQ1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 3)
)
_Dot1pPortTable_Object = MibTable
dot1pPortTable = _Dot1pPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 3, 1)
)
if mibBuilder.loadTexts:
    dot1pPortTable.setStatus("current")
_Dot1pPortEntry_Object = MibTableRow
dot1pPortEntry = _Dot1pPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 3, 1, 1)
)
dot1pPortEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "dot1pPortIndex"),
)
if mibBuilder.loadTexts:
    dot1pPortEntry.setStatus("current")
_Dot1pPortIndex_Type = Integer32
_Dot1pPortIndex_Object = MibTableColumn
dot1pPortIndex = _Dot1pPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 3, 1, 1, 1),
    _Dot1pPortIndex_Type()
)
dot1pPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pPortIndex.setStatus("current")


class _Dot1pPortPriority_Type(Integer32):
    """Custom type dot1pPortPriority based on Integer32"""
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
        *(("high", 3),
          ("highest", 4),
          ("low", 1),
          ("medium", 2))
    )


_Dot1pPortPriority_Type.__name__ = "Integer32"
_Dot1pPortPriority_Object = MibTableColumn
dot1pPortPriority = _Dot1pPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 3, 1, 1, 2),
    _Dot1pPortPriority_Type()
)
dot1pPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1pPortPriority.setStatus("current")
_QosDiffServ_ObjectIdentity = ObjectIdentity
qosDiffServ = _QosDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4)
)


class _QosDiffServEnable_Type(Integer32):
    """Custom type qosDiffServEnable based on Integer32"""
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


_QosDiffServEnable_Type.__name__ = "Integer32"
_QosDiffServEnable_Object = MibScalar
qosDiffServEnable = _QosDiffServEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 1),
    _QosDiffServEnable_Type()
)
qosDiffServEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDiffServEnable.setStatus("current")
_QosDiffServTypeGroup_ObjectIdentity = ObjectIdentity
qosDiffServTypeGroup = _QosDiffServTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2)
)


class _QosDiffServType00_Type(Integer32):
    """Custom type qosDiffServType00 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType00_Type.__name__ = "Integer32"
_QosDiffServType00_Object = MibScalar
qosDiffServType00 = _QosDiffServType00_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 1),
    _QosDiffServType00_Type()
)
qosDiffServType00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType00.setStatus("current")


class _QosDiffServType01_Type(Integer32):
    """Custom type qosDiffServType01 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType01_Type.__name__ = "Integer32"
_QosDiffServType01_Object = MibScalar
qosDiffServType01 = _QosDiffServType01_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 2),
    _QosDiffServType01_Type()
)
qosDiffServType01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType01.setStatus("current")


class _QosDiffServType02_Type(Integer32):
    """Custom type qosDiffServType02 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType02_Type.__name__ = "Integer32"
_QosDiffServType02_Object = MibScalar
qosDiffServType02 = _QosDiffServType02_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 3),
    _QosDiffServType02_Type()
)
qosDiffServType02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType02.setStatus("current")


class _QosDiffServType03_Type(Integer32):
    """Custom type qosDiffServType03 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType03_Type.__name__ = "Integer32"
_QosDiffServType03_Object = MibScalar
qosDiffServType03 = _QosDiffServType03_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 4),
    _QosDiffServType03_Type()
)
qosDiffServType03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType03.setStatus("current")


class _QosDiffServType04_Type(Integer32):
    """Custom type qosDiffServType04 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType04_Type.__name__ = "Integer32"
_QosDiffServType04_Object = MibScalar
qosDiffServType04 = _QosDiffServType04_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 5),
    _QosDiffServType04_Type()
)
qosDiffServType04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType04.setStatus("current")


class _QosDiffServType05_Type(Integer32):
    """Custom type qosDiffServType05 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType05_Type.__name__ = "Integer32"
_QosDiffServType05_Object = MibScalar
qosDiffServType05 = _QosDiffServType05_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 6),
    _QosDiffServType05_Type()
)
qosDiffServType05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType05.setStatus("current")


class _QosDiffServType06_Type(Integer32):
    """Custom type qosDiffServType06 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType06_Type.__name__ = "Integer32"
_QosDiffServType06_Object = MibScalar
qosDiffServType06 = _QosDiffServType06_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 7),
    _QosDiffServType06_Type()
)
qosDiffServType06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType06.setStatus("current")


class _QosDiffServType07_Type(Integer32):
    """Custom type qosDiffServType07 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType07_Type.__name__ = "Integer32"
_QosDiffServType07_Object = MibScalar
qosDiffServType07 = _QosDiffServType07_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 8),
    _QosDiffServType07_Type()
)
qosDiffServType07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType07.setStatus("current")


class _QosDiffServType08_Type(Integer32):
    """Custom type qosDiffServType08 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType08_Type.__name__ = "Integer32"
_QosDiffServType08_Object = MibScalar
qosDiffServType08 = _QosDiffServType08_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 9),
    _QosDiffServType08_Type()
)
qosDiffServType08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType08.setStatus("current")


class _QosDiffServType09_Type(Integer32):
    """Custom type qosDiffServType09 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType09_Type.__name__ = "Integer32"
_QosDiffServType09_Object = MibScalar
qosDiffServType09 = _QosDiffServType09_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 10),
    _QosDiffServType09_Type()
)
qosDiffServType09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType09.setStatus("current")


class _QosDiffServType10_Type(Integer32):
    """Custom type qosDiffServType10 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType10_Type.__name__ = "Integer32"
_QosDiffServType10_Object = MibScalar
qosDiffServType10 = _QosDiffServType10_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 11),
    _QosDiffServType10_Type()
)
qosDiffServType10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType10.setStatus("current")


class _QosDiffServType11_Type(Integer32):
    """Custom type qosDiffServType11 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType11_Type.__name__ = "Integer32"
_QosDiffServType11_Object = MibScalar
qosDiffServType11 = _QosDiffServType11_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 12),
    _QosDiffServType11_Type()
)
qosDiffServType11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType11.setStatus("current")


class _QosDiffServType12_Type(Integer32):
    """Custom type qosDiffServType12 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType12_Type.__name__ = "Integer32"
_QosDiffServType12_Object = MibScalar
qosDiffServType12 = _QosDiffServType12_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 13),
    _QosDiffServType12_Type()
)
qosDiffServType12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType12.setStatus("current")


class _QosDiffServType13_Type(Integer32):
    """Custom type qosDiffServType13 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType13_Type.__name__ = "Integer32"
_QosDiffServType13_Object = MibScalar
qosDiffServType13 = _QosDiffServType13_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 14),
    _QosDiffServType13_Type()
)
qosDiffServType13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType13.setStatus("current")


class _QosDiffServType14_Type(Integer32):
    """Custom type qosDiffServType14 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType14_Type.__name__ = "Integer32"
_QosDiffServType14_Object = MibScalar
qosDiffServType14 = _QosDiffServType14_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 15),
    _QosDiffServType14_Type()
)
qosDiffServType14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType14.setStatus("current")


class _QosDiffServType15_Type(Integer32):
    """Custom type qosDiffServType15 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType15_Type.__name__ = "Integer32"
_QosDiffServType15_Object = MibScalar
qosDiffServType15 = _QosDiffServType15_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 16),
    _QosDiffServType15_Type()
)
qosDiffServType15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType15.setStatus("current")


class _QosDiffServType16_Type(Integer32):
    """Custom type qosDiffServType16 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType16_Type.__name__ = "Integer32"
_QosDiffServType16_Object = MibScalar
qosDiffServType16 = _QosDiffServType16_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 17),
    _QosDiffServType16_Type()
)
qosDiffServType16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType16.setStatus("current")


class _QosDiffServType17_Type(Integer32):
    """Custom type qosDiffServType17 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType17_Type.__name__ = "Integer32"
_QosDiffServType17_Object = MibScalar
qosDiffServType17 = _QosDiffServType17_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 18),
    _QosDiffServType17_Type()
)
qosDiffServType17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType17.setStatus("current")


class _QosDiffServType18_Type(Integer32):
    """Custom type qosDiffServType18 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType18_Type.__name__ = "Integer32"
_QosDiffServType18_Object = MibScalar
qosDiffServType18 = _QosDiffServType18_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 19),
    _QosDiffServType18_Type()
)
qosDiffServType18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType18.setStatus("current")


class _QosDiffServType19_Type(Integer32):
    """Custom type qosDiffServType19 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType19_Type.__name__ = "Integer32"
_QosDiffServType19_Object = MibScalar
qosDiffServType19 = _QosDiffServType19_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 20),
    _QosDiffServType19_Type()
)
qosDiffServType19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType19.setStatus("current")


class _QosDiffServType20_Type(Integer32):
    """Custom type qosDiffServType20 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType20_Type.__name__ = "Integer32"
_QosDiffServType20_Object = MibScalar
qosDiffServType20 = _QosDiffServType20_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 21),
    _QosDiffServType20_Type()
)
qosDiffServType20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType20.setStatus("current")


class _QosDiffServType21_Type(Integer32):
    """Custom type qosDiffServType21 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType21_Type.__name__ = "Integer32"
_QosDiffServType21_Object = MibScalar
qosDiffServType21 = _QosDiffServType21_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 22),
    _QosDiffServType21_Type()
)
qosDiffServType21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType21.setStatus("current")


class _QosDiffServType22_Type(Integer32):
    """Custom type qosDiffServType22 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType22_Type.__name__ = "Integer32"
_QosDiffServType22_Object = MibScalar
qosDiffServType22 = _QosDiffServType22_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 23),
    _QosDiffServType22_Type()
)
qosDiffServType22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType22.setStatus("current")


class _QosDiffServType23_Type(Integer32):
    """Custom type qosDiffServType23 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType23_Type.__name__ = "Integer32"
_QosDiffServType23_Object = MibScalar
qosDiffServType23 = _QosDiffServType23_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 24),
    _QosDiffServType23_Type()
)
qosDiffServType23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType23.setStatus("current")


class _QosDiffServType24_Type(Integer32):
    """Custom type qosDiffServType24 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType24_Type.__name__ = "Integer32"
_QosDiffServType24_Object = MibScalar
qosDiffServType24 = _QosDiffServType24_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 25),
    _QosDiffServType24_Type()
)
qosDiffServType24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType24.setStatus("current")


class _QosDiffServType25_Type(Integer32):
    """Custom type qosDiffServType25 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType25_Type.__name__ = "Integer32"
_QosDiffServType25_Object = MibScalar
qosDiffServType25 = _QosDiffServType25_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 26),
    _QosDiffServType25_Type()
)
qosDiffServType25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType25.setStatus("current")


class _QosDiffServType26_Type(Integer32):
    """Custom type qosDiffServType26 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType26_Type.__name__ = "Integer32"
_QosDiffServType26_Object = MibScalar
qosDiffServType26 = _QosDiffServType26_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 27),
    _QosDiffServType26_Type()
)
qosDiffServType26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType26.setStatus("current")


class _QosDiffServType27_Type(Integer32):
    """Custom type qosDiffServType27 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType27_Type.__name__ = "Integer32"
_QosDiffServType27_Object = MibScalar
qosDiffServType27 = _QosDiffServType27_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 28),
    _QosDiffServType27_Type()
)
qosDiffServType27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType27.setStatus("current")


class _QosDiffServType28_Type(Integer32):
    """Custom type qosDiffServType28 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType28_Type.__name__ = "Integer32"
_QosDiffServType28_Object = MibScalar
qosDiffServType28 = _QosDiffServType28_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 29),
    _QosDiffServType28_Type()
)
qosDiffServType28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType28.setStatus("current")


class _QosDiffServType29_Type(Integer32):
    """Custom type qosDiffServType29 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType29_Type.__name__ = "Integer32"
_QosDiffServType29_Object = MibScalar
qosDiffServType29 = _QosDiffServType29_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 30),
    _QosDiffServType29_Type()
)
qosDiffServType29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType29.setStatus("current")


class _QosDiffServType30_Type(Integer32):
    """Custom type qosDiffServType30 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType30_Type.__name__ = "Integer32"
_QosDiffServType30_Object = MibScalar
qosDiffServType30 = _QosDiffServType30_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 31),
    _QosDiffServType30_Type()
)
qosDiffServType30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType30.setStatus("current")


class _QosDiffServType31_Type(Integer32):
    """Custom type qosDiffServType31 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType31_Type.__name__ = "Integer32"
_QosDiffServType31_Object = MibScalar
qosDiffServType31 = _QosDiffServType31_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 32),
    _QosDiffServType31_Type()
)
qosDiffServType31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType31.setStatus("current")


class _QosDiffServType32_Type(Integer32):
    """Custom type qosDiffServType32 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType32_Type.__name__ = "Integer32"
_QosDiffServType32_Object = MibScalar
qosDiffServType32 = _QosDiffServType32_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 33),
    _QosDiffServType32_Type()
)
qosDiffServType32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType32.setStatus("current")


class _QosDiffServType33_Type(Integer32):
    """Custom type qosDiffServType33 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType33_Type.__name__ = "Integer32"
_QosDiffServType33_Object = MibScalar
qosDiffServType33 = _QosDiffServType33_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 34),
    _QosDiffServType33_Type()
)
qosDiffServType33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType33.setStatus("current")


class _QosDiffServType34_Type(Integer32):
    """Custom type qosDiffServType34 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType34_Type.__name__ = "Integer32"
_QosDiffServType34_Object = MibScalar
qosDiffServType34 = _QosDiffServType34_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 35),
    _QosDiffServType34_Type()
)
qosDiffServType34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType34.setStatus("current")


class _QosDiffServType35_Type(Integer32):
    """Custom type qosDiffServType35 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType35_Type.__name__ = "Integer32"
_QosDiffServType35_Object = MibScalar
qosDiffServType35 = _QosDiffServType35_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 36),
    _QosDiffServType35_Type()
)
qosDiffServType35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType35.setStatus("current")


class _QosDiffServType36_Type(Integer32):
    """Custom type qosDiffServType36 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType36_Type.__name__ = "Integer32"
_QosDiffServType36_Object = MibScalar
qosDiffServType36 = _QosDiffServType36_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 37),
    _QosDiffServType36_Type()
)
qosDiffServType36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType36.setStatus("current")


class _QosDiffServType37_Type(Integer32):
    """Custom type qosDiffServType37 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType37_Type.__name__ = "Integer32"
_QosDiffServType37_Object = MibScalar
qosDiffServType37 = _QosDiffServType37_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 38),
    _QosDiffServType37_Type()
)
qosDiffServType37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType37.setStatus("current")


class _QosDiffServType38_Type(Integer32):
    """Custom type qosDiffServType38 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType38_Type.__name__ = "Integer32"
_QosDiffServType38_Object = MibScalar
qosDiffServType38 = _QosDiffServType38_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 39),
    _QosDiffServType38_Type()
)
qosDiffServType38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType38.setStatus("current")


class _QosDiffServType39_Type(Integer32):
    """Custom type qosDiffServType39 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType39_Type.__name__ = "Integer32"
_QosDiffServType39_Object = MibScalar
qosDiffServType39 = _QosDiffServType39_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 40),
    _QosDiffServType39_Type()
)
qosDiffServType39.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType39.setStatus("current")


class _QosDiffServType40_Type(Integer32):
    """Custom type qosDiffServType40 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType40_Type.__name__ = "Integer32"
_QosDiffServType40_Object = MibScalar
qosDiffServType40 = _QosDiffServType40_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 41),
    _QosDiffServType40_Type()
)
qosDiffServType40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType40.setStatus("current")


class _QosDiffServType41_Type(Integer32):
    """Custom type qosDiffServType41 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType41_Type.__name__ = "Integer32"
_QosDiffServType41_Object = MibScalar
qosDiffServType41 = _QosDiffServType41_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 42),
    _QosDiffServType41_Type()
)
qosDiffServType41.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType41.setStatus("current")


class _QosDiffServType42_Type(Integer32):
    """Custom type qosDiffServType42 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType42_Type.__name__ = "Integer32"
_QosDiffServType42_Object = MibScalar
qosDiffServType42 = _QosDiffServType42_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 43),
    _QosDiffServType42_Type()
)
qosDiffServType42.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType42.setStatus("current")


class _QosDiffServType43_Type(Integer32):
    """Custom type qosDiffServType43 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType43_Type.__name__ = "Integer32"
_QosDiffServType43_Object = MibScalar
qosDiffServType43 = _QosDiffServType43_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 44),
    _QosDiffServType43_Type()
)
qosDiffServType43.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType43.setStatus("current")


class _QosDiffServType44_Type(Integer32):
    """Custom type qosDiffServType44 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType44_Type.__name__ = "Integer32"
_QosDiffServType44_Object = MibScalar
qosDiffServType44 = _QosDiffServType44_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 45),
    _QosDiffServType44_Type()
)
qosDiffServType44.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType44.setStatus("current")


class _QosDiffServType45_Type(Integer32):
    """Custom type qosDiffServType45 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType45_Type.__name__ = "Integer32"
_QosDiffServType45_Object = MibScalar
qosDiffServType45 = _QosDiffServType45_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 46),
    _QosDiffServType45_Type()
)
qosDiffServType45.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType45.setStatus("current")


class _QosDiffServType46_Type(Integer32):
    """Custom type qosDiffServType46 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType46_Type.__name__ = "Integer32"
_QosDiffServType46_Object = MibScalar
qosDiffServType46 = _QosDiffServType46_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 47),
    _QosDiffServType46_Type()
)
qosDiffServType46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType46.setStatus("current")


class _QosDiffServType47_Type(Integer32):
    """Custom type qosDiffServType47 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType47_Type.__name__ = "Integer32"
_QosDiffServType47_Object = MibScalar
qosDiffServType47 = _QosDiffServType47_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 48),
    _QosDiffServType47_Type()
)
qosDiffServType47.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType47.setStatus("current")


class _QosDiffServType48_Type(Integer32):
    """Custom type qosDiffServType48 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType48_Type.__name__ = "Integer32"
_QosDiffServType48_Object = MibScalar
qosDiffServType48 = _QosDiffServType48_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 49),
    _QosDiffServType48_Type()
)
qosDiffServType48.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType48.setStatus("current")


class _QosDiffServType49_Type(Integer32):
    """Custom type qosDiffServType49 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType49_Type.__name__ = "Integer32"
_QosDiffServType49_Object = MibScalar
qosDiffServType49 = _QosDiffServType49_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 50),
    _QosDiffServType49_Type()
)
qosDiffServType49.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType49.setStatus("current")


class _QosDiffServType50_Type(Integer32):
    """Custom type qosDiffServType50 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType50_Type.__name__ = "Integer32"
_QosDiffServType50_Object = MibScalar
qosDiffServType50 = _QosDiffServType50_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 51),
    _QosDiffServType50_Type()
)
qosDiffServType50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType50.setStatus("current")


class _QosDiffServType51_Type(Integer32):
    """Custom type qosDiffServType51 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType51_Type.__name__ = "Integer32"
_QosDiffServType51_Object = MibScalar
qosDiffServType51 = _QosDiffServType51_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 52),
    _QosDiffServType51_Type()
)
qosDiffServType51.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType51.setStatus("current")


class _QosDiffServType52_Type(Integer32):
    """Custom type qosDiffServType52 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType52_Type.__name__ = "Integer32"
_QosDiffServType52_Object = MibScalar
qosDiffServType52 = _QosDiffServType52_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 53),
    _QosDiffServType52_Type()
)
qosDiffServType52.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType52.setStatus("current")


class _QosDiffServType53_Type(Integer32):
    """Custom type qosDiffServType53 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType53_Type.__name__ = "Integer32"
_QosDiffServType53_Object = MibScalar
qosDiffServType53 = _QosDiffServType53_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 54),
    _QosDiffServType53_Type()
)
qosDiffServType53.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType53.setStatus("current")


class _QosDiffServType54_Type(Integer32):
    """Custom type qosDiffServType54 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType54_Type.__name__ = "Integer32"
_QosDiffServType54_Object = MibScalar
qosDiffServType54 = _QosDiffServType54_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 55),
    _QosDiffServType54_Type()
)
qosDiffServType54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType54.setStatus("current")


class _QosDiffServType55_Type(Integer32):
    """Custom type qosDiffServType55 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType55_Type.__name__ = "Integer32"
_QosDiffServType55_Object = MibScalar
qosDiffServType55 = _QosDiffServType55_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 56),
    _QosDiffServType55_Type()
)
qosDiffServType55.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType55.setStatus("current")


class _QosDiffServType56_Type(Integer32):
    """Custom type qosDiffServType56 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType56_Type.__name__ = "Integer32"
_QosDiffServType56_Object = MibScalar
qosDiffServType56 = _QosDiffServType56_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 57),
    _QosDiffServType56_Type()
)
qosDiffServType56.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType56.setStatus("current")


class _QosDiffServType57_Type(Integer32):
    """Custom type qosDiffServType57 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType57_Type.__name__ = "Integer32"
_QosDiffServType57_Object = MibScalar
qosDiffServType57 = _QosDiffServType57_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 58),
    _QosDiffServType57_Type()
)
qosDiffServType57.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType57.setStatus("current")


class _QosDiffServType58_Type(Integer32):
    """Custom type qosDiffServType58 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType58_Type.__name__ = "Integer32"
_QosDiffServType58_Object = MibScalar
qosDiffServType58 = _QosDiffServType58_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 59),
    _QosDiffServType58_Type()
)
qosDiffServType58.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType58.setStatus("current")


class _QosDiffServType59_Type(Integer32):
    """Custom type qosDiffServType59 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType59_Type.__name__ = "Integer32"
_QosDiffServType59_Object = MibScalar
qosDiffServType59 = _QosDiffServType59_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 60),
    _QosDiffServType59_Type()
)
qosDiffServType59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType59.setStatus("current")


class _QosDiffServType60_Type(Integer32):
    """Custom type qosDiffServType60 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType60_Type.__name__ = "Integer32"
_QosDiffServType60_Object = MibScalar
qosDiffServType60 = _QosDiffServType60_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 61),
    _QosDiffServType60_Type()
)
qosDiffServType60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType60.setStatus("current")


class _QosDiffServType61_Type(Integer32):
    """Custom type qosDiffServType61 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType61_Type.__name__ = "Integer32"
_QosDiffServType61_Object = MibScalar
qosDiffServType61 = _QosDiffServType61_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 62),
    _QosDiffServType61_Type()
)
qosDiffServType61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType61.setStatus("current")


class _QosDiffServType62_Type(Integer32):
    """Custom type qosDiffServType62 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType62_Type.__name__ = "Integer32"
_QosDiffServType62_Object = MibScalar
qosDiffServType62 = _QosDiffServType62_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 63),
    _QosDiffServType62_Type()
)
qosDiffServType62.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType62.setStatus("current")


class _QosDiffServType63_Type(Integer32):
    """Custom type qosDiffServType63 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosDiffServType63_Type.__name__ = "Integer32"
_QosDiffServType63_Object = MibScalar
qosDiffServType63 = _QosDiffServType63_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 4, 2, 64),
    _QosDiffServType63_Type()
)
qosDiffServType63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType63.setStatus("current")
_QosTOS_ObjectIdentity = ObjectIdentity
qosTOS = _QosTOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5)
)


class _QosTOSEnable_Type(Integer32):
    """Custom type qosTOSEnable based on Integer32"""
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


_QosTOSEnable_Type.__name__ = "Integer32"
_QosTOSEnable_Object = MibScalar
qosTOSEnable = _QosTOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 1),
    _QosTOSEnable_Type()
)
qosTOSEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTOSEnable.setStatus("current")
_QosTOSGroup_ObjectIdentity = ObjectIdentity
qosTOSGroup = _QosTOSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2)
)


class _QosTOSType00_Type(Integer32):
    """Custom type qosTOSType00 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType00_Type.__name__ = "Integer32"
_QosTOSType00_Object = MibScalar
qosTOSType00 = _QosTOSType00_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 1),
    _QosTOSType00_Type()
)
qosTOSType00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType00.setStatus("current")


class _QosTOSType01_Type(Integer32):
    """Custom type qosTOSType01 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType01_Type.__name__ = "Integer32"
_QosTOSType01_Object = MibScalar
qosTOSType01 = _QosTOSType01_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 2),
    _QosTOSType01_Type()
)
qosTOSType01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType01.setStatus("current")


class _QosTOSType02_Type(Integer32):
    """Custom type qosTOSType02 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType02_Type.__name__ = "Integer32"
_QosTOSType02_Object = MibScalar
qosTOSType02 = _QosTOSType02_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 3),
    _QosTOSType02_Type()
)
qosTOSType02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType02.setStatus("current")


class _QosTOSType03_Type(Integer32):
    """Custom type qosTOSType03 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType03_Type.__name__ = "Integer32"
_QosTOSType03_Object = MibScalar
qosTOSType03 = _QosTOSType03_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 4),
    _QosTOSType03_Type()
)
qosTOSType03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType03.setStatus("current")


class _QosTOSType04_Type(Integer32):
    """Custom type qosTOSType04 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType04_Type.__name__ = "Integer32"
_QosTOSType04_Object = MibScalar
qosTOSType04 = _QosTOSType04_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 5),
    _QosTOSType04_Type()
)
qosTOSType04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType04.setStatus("current")


class _QosTOSType05_Type(Integer32):
    """Custom type qosTOSType05 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType05_Type.__name__ = "Integer32"
_QosTOSType05_Object = MibScalar
qosTOSType05 = _QosTOSType05_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 6),
    _QosTOSType05_Type()
)
qosTOSType05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType05.setStatus("current")


class _QosTOSType06_Type(Integer32):
    """Custom type qosTOSType06 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType06_Type.__name__ = "Integer32"
_QosTOSType06_Object = MibScalar
qosTOSType06 = _QosTOSType06_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 7),
    _QosTOSType06_Type()
)
qosTOSType06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType06.setStatus("current")


class _QosTOSType07_Type(Integer32):
    """Custom type qosTOSType07 based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_QosTOSType07_Type.__name__ = "Integer32"
_QosTOSType07_Object = MibScalar
qosTOSType07 = _QosTOSType07_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 5, 2, 8),
    _QosTOSType07_Type()
)
qosTOSType07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType07.setStatus("current")
_QosAclPrioritySettings_ObjectIdentity = ObjectIdentity
qosAclPrioritySettings = _QosAclPrioritySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6)
)
_AclQosTable_Object = MibTable
aclQosTable = _AclQosTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1)
)
if mibBuilder.loadTexts:
    aclQosTable.setStatus("current")
_AclQosEntry_Object = MibTableRow
aclQosEntry = _AclQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1, 1)
)
aclQosEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "aclQosIndex"),
)
if mibBuilder.loadTexts:
    aclQosEntry.setStatus("current")


class _AclQosIndex_Type(Integer32):
    """Custom type aclQosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclQosIndex_Type.__name__ = "Integer32"
_AclQosIndex_Object = MibTableColumn
aclQosIndex = _AclQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1, 1, 1),
    _AclQosIndex_Type()
)
aclQosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclQosIndex.setStatus("current")


class _AclQosType_Type(Integer32):
    """Custom type aclQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipv6traffic_class", 7),
          ("tcp", 2),
          ("udp", 3))
    )


_AclQosType_Type.__name__ = "Integer32"
_AclQosType_Object = MibTableColumn
aclQosType = _AclQosType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1, 1, 2),
    _AclQosType_Type()
)
aclQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosType.setStatus("current")


class _AclQosTCPUDPPort_Type(Integer32):
    """Custom type aclQosTCPUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclQosTCPUDPPort_Type.__name__ = "Integer32"
_AclQosTCPUDPPort_Object = MibTableColumn
aclQosTCPUDPPort = _AclQosTCPUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1, 1, 5),
    _AclQosTCPUDPPort_Type()
)
aclQosTCPUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosTCPUDPPort.setStatus("current")


class _AclQosIP6TC_Type(Integer32):
    """Custom type aclQosIP6TC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclQosIP6TC_Type.__name__ = "Integer32"
_AclQosIP6TC_Object = MibTableColumn
aclQosIP6TC = _AclQosIP6TC_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1, 1, 10),
    _AclQosIP6TC_Type()
)
aclQosIP6TC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosIP6TC.setStatus("current")


class _AclQosAssignPriority_Type(Integer32):
    """Custom type aclQosAssignPriority based on Integer32"""
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
        *(("high", 2),
          ("highest", 3),
          ("low", 0),
          ("medium", 1))
    )


_AclQosAssignPriority_Type.__name__ = "Integer32"
_AclQosAssignPriority_Object = MibTableColumn
aclQosAssignPriority = _AclQosAssignPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1, 1, 98),
    _AclQosAssignPriority_Type()
)
aclQosAssignPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosAssignPriority.setStatus("current")
_AclQosStatus_Type = RowStatus
_AclQosStatus_Object = MibTableColumn
aclQosStatus = _AclQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 12, 6, 1, 1, 99),
    _AclQosStatus_Type()
)
aclQosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosStatus.setStatus("current")
_CompanyTrafficMgmt_ObjectIdentity = ObjectIdentity
companyTrafficMgmt = _CompanyTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13)
)
_BandwidthCtrlSettings_ObjectIdentity = ObjectIdentity
bandwidthCtrlSettings = _BandwidthCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 1)
)
_BandwidthCtrlTable_Object = MibTable
bandwidthCtrlTable = _BandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 1, 2)
)
if mibBuilder.loadTexts:
    bandwidthCtrlTable.setStatus("current")
_BandwidthCtrlEntry_Object = MibTableRow
bandwidthCtrlEntry = _BandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 1, 2, 1)
)
bandwidthCtrlEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "bandwidthCtrlIndex"),
)
if mibBuilder.loadTexts:
    bandwidthCtrlEntry.setStatus("current")
_BandwidthCtrlIndex_Type = Integer32
_BandwidthCtrlIndex_Object = MibTableColumn
bandwidthCtrlIndex = _BandwidthCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 1, 2, 1, 1),
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
        ValueRangeConstraint(64, 1024000),
    )


_BandwidthCtrlTxThreshold_Type.__name__ = "Integer32"
_BandwidthCtrlTxThreshold_Object = MibTableColumn
bandwidthCtrlTxThreshold = _BandwidthCtrlTxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 1, 2, 1, 2),
    _BandwidthCtrlTxThreshold_Type()
)
bandwidthCtrlTxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlTxThreshold.setStatus("current")


class _BandwidthCtrlRxThreshold_Type(Integer32):
    """Custom type bandwidthCtrlRxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1024000),
    )


_BandwidthCtrlRxThreshold_Type.__name__ = "Integer32"
_BandwidthCtrlRxThreshold_Object = MibTableColumn
bandwidthCtrlRxThreshold = _BandwidthCtrlRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 1, 2, 1, 3),
    _BandwidthCtrlRxThreshold_Type()
)
bandwidthCtrlRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlRxThreshold.setStatus("current")
_BroadcastStormCtrlSettings_ObjectIdentity = ObjectIdentity
broadcastStormCtrlSettings = _BroadcastStormCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 3)
)


class _BroadcastStormCtrlGlobalOnOff_Type(Integer32):
    """Custom type broadcastStormCtrlGlobalOnOff based on Integer32"""
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


_BroadcastStormCtrlGlobalOnOff_Type.__name__ = "Integer32"
_BroadcastStormCtrlGlobalOnOff_Object = MibScalar
broadcastStormCtrlGlobalOnOff = _BroadcastStormCtrlGlobalOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 3, 1),
    _BroadcastStormCtrlGlobalOnOff_Type()
)
broadcastStormCtrlGlobalOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormCtrlGlobalOnOff.setStatus("current")


class _BroadcastStormCtrlLimitType_Type(Integer32):
    """Custom type broadcastStormCtrlLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcastonly", 1),
          ("dlfMulticastAndbroadcast", 3),
          ("multicastAndbroadcast", 2))
    )


_BroadcastStormCtrlLimitType_Type.__name__ = "Integer32"
_BroadcastStormCtrlLimitType_Object = MibScalar
broadcastStormCtrlLimitType = _BroadcastStormCtrlLimitType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 3, 2),
    _BroadcastStormCtrlLimitType_Type()
)
broadcastStormCtrlLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormCtrlLimitType.setStatus("current")


class _BroadcastStormCtrlThreshold_Type(Integer32):
    """Custom type broadcastStormCtrlThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1024000),
    )


_BroadcastStormCtrlThreshold_Type.__name__ = "Integer32"
_BroadcastStormCtrlThreshold_Object = MibScalar
broadcastStormCtrlThreshold = _BroadcastStormCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 13, 3, 3),
    _BroadcastStormCtrlThreshold_Type()
)
broadcastStormCtrlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormCtrlThreshold.setStatus("current")
_CompanySecurity_ObjectIdentity = ObjectIdentity
companySecurity = _CompanySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14)
)
_SecurityTrustedHost_ObjectIdentity = ObjectIdentity
securityTrustedHost = _SecurityTrustedHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 1),
    _TrustedHostStatus_Type()
)
trustedHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostStatus.setStatus("current")
_Ipv4trustedHostTable_Object = MibTable
ipv4trustedHostTable = _Ipv4trustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 2)
)
if mibBuilder.loadTexts:
    ipv4trustedHostTable.setStatus("obsolete")
_Ipv4trustedHostEntry_Object = MibTableRow
ipv4trustedHostEntry = _Ipv4trustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 2, 1)
)
ipv4trustedHostEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "ipv4trustedHostIpAddr"),
    (0, "DGS-1210-20_BX", "ipv4trustedHostIpMask"),
)
if mibBuilder.loadTexts:
    ipv4trustedHostEntry.setStatus("obsolete")
_Ipv4trustedHostIpAddr_Type = IpAddress
_Ipv4trustedHostIpAddr_Object = MibTableColumn
ipv4trustedHostIpAddr = _Ipv4trustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 2, 1, 1),
    _Ipv4trustedHostIpAddr_Type()
)
ipv4trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4trustedHostIpAddr.setStatus("obsolete")
_Ipv4trustedHostIpMask_Type = IpAddress
_Ipv4trustedHostIpMask_Object = MibTableColumn
ipv4trustedHostIpMask = _Ipv4trustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 2, 1, 2),
    _Ipv4trustedHostIpMask_Type()
)
ipv4trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4trustedHostIpMask.setStatus("obsolete")
_Ipv4trustedHostRowStatus_Type = RowStatus
_Ipv4trustedHostRowStatus_Object = MibTableColumn
ipv4trustedHostRowStatus = _Ipv4trustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 2, 1, 3),
    _Ipv4trustedHostRowStatus_Type()
)
ipv4trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4trustedHostRowStatus.setStatus("obsolete")
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 3)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("current")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 3, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "trustedHostIPType"),
    (0, "DGS-1210-20_BX", "trustedHostIpAddr"),
    (0, "DGS-1210-20_BX", "trustedHostIpMask"),
)
if mibBuilder.loadTexts:
    trustedHostEntry.setStatus("current")


class _TrustedHostIPType_Type(Integer32):
    """Custom type trustedHostIPType based on Integer32"""
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


_TrustedHostIPType_Type.__name__ = "Integer32"
_TrustedHostIPType_Object = MibTableColumn
trustedHostIPType = _TrustedHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 3, 1, 1),
    _TrustedHostIPType_Type()
)
trustedHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIPType.setStatus("current")
_TrustedHostIpAddr_Type = Ipv6Address
_TrustedHostIpAddr_Object = MibTableColumn
trustedHostIpAddr = _TrustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 3, 1, 2),
    _TrustedHostIpAddr_Type()
)
trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpAddr.setStatus("current")
_TrustedHostIpMask_Type = Ipv6Address
_TrustedHostIpMask_Object = MibTableColumn
trustedHostIpMask = _TrustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 3, 1, 3),
    _TrustedHostIpMask_Type()
)
trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpMask.setStatus("current")
_TrustedHostRowStatus_Type = RowStatus
_TrustedHostRowStatus_Object = MibTableColumn
trustedHostRowStatus = _TrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 1, 3, 1, 4),
    _TrustedHostRowStatus_Type()
)
trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedHostRowStatus.setStatus("current")
_SecurityPortSecurity_ObjectIdentity = ObjectIdentity
securityPortSecurity = _SecurityPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 2)
)
_PortSecTable_Object = MibTable
portSecTable = _PortSecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 2, 1)
)
if mibBuilder.loadTexts:
    portSecTable.setStatus("current")
_PortSecEntry_Object = MibTableRow
portSecEntry = _PortSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 2, 1, 1)
)
portSecEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "portSecIndex"),
)
if mibBuilder.loadTexts:
    portSecEntry.setStatus("current")
_PortSecIndex_Type = Integer32
_PortSecIndex_Object = MibTableColumn
portSecIndex = _PortSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 2, 1, 1, 1),
    _PortSecIndex_Type()
)
portSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecIndex.setStatus("current")


class _PortSecState_Type(Integer32):
    """Custom type portSecState based on Integer32"""
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


_PortSecState_Type.__name__ = "Integer32"
_PortSecState_Object = MibTableColumn
portSecState = _PortSecState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 2, 1, 1, 2),
    _PortSecState_Type()
)
portSecState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecState.setStatus("current")


class _PortSecMLA_Type(Integer32):
    """Custom type portSecMLA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PortSecMLA_Type.__name__ = "Integer32"
_PortSecMLA_Object = MibTableColumn
portSecMLA = _PortSecMLA_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 2, 1, 1, 3),
    _PortSecMLA_Type()
)
portSecMLA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMLA.setStatus("current")
_SecurityARPSpoofPrevent_ObjectIdentity = ObjectIdentity
securityARPSpoofPrevent = _SecurityARPSpoofPrevent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 3)
)
_ARPSpoofPreventTable_Object = MibTable
aRPSpoofPreventTable = _ARPSpoofPreventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 3, 1)
)
if mibBuilder.loadTexts:
    aRPSpoofPreventTable.setStatus("current")
_ARPSpoofPreventEntry_Object = MibTableRow
aRPSpoofPreventEntry = _ARPSpoofPreventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 3, 1, 1)
)
aRPSpoofPreventEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "aRPSpoofPreventIpAddr"),
)
if mibBuilder.loadTexts:
    aRPSpoofPreventEntry.setStatus("current")
_ARPSpoofPreventIpAddr_Type = IpAddress
_ARPSpoofPreventIpAddr_Object = MibTableColumn
aRPSpoofPreventIpAddr = _ARPSpoofPreventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 3, 1, 1, 1),
    _ARPSpoofPreventIpAddr_Type()
)
aRPSpoofPreventIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aRPSpoofPreventIpAddr.setStatus("current")


class _ARPSpoofPreventMacAddress_Type(MacAddress):
    """Custom type aRPSpoofPreventMacAddress based on MacAddress"""
    defaultHexValue = "000102030405"


_ARPSpoofPreventMacAddress_Object = MibTableColumn
aRPSpoofPreventMacAddress = _ARPSpoofPreventMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 3, 1, 1, 2),
    _ARPSpoofPreventMacAddress_Type()
)
aRPSpoofPreventMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventMacAddress.setStatus("current")
_ARPSpoofPreventPortList_Type = PortList
_ARPSpoofPreventPortList_Object = MibTableColumn
aRPSpoofPreventPortList = _ARPSpoofPreventPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 3, 1, 1, 3),
    _ARPSpoofPreventPortList_Type()
)
aRPSpoofPreventPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventPortList.setStatus("current")
_ARPSpoofPreventRowStatus_Type = RowStatus
_ARPSpoofPreventRowStatus_Object = MibTableColumn
aRPSpoofPreventRowStatus = _ARPSpoofPreventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 3, 1, 1, 4),
    _ARPSpoofPreventRowStatus_Type()
)
aRPSpoofPreventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aRPSpoofPreventRowStatus.setStatus("current")
_SecuritySSL_ObjectIdentity = ObjectIdentity
securitySSL = _SecuritySSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 5)
)


class _SslSecurityHttpStatus_Type(Integer32):
    """Custom type sslSecurityHttpStatus based on Integer32"""
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


_SslSecurityHttpStatus_Type.__name__ = "Integer32"
_SslSecurityHttpStatus_Object = MibScalar
sslSecurityHttpStatus = _SslSecurityHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 5, 1),
    _SslSecurityHttpStatus_Type()
)
sslSecurityHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSecurityHttpStatus.setStatus("current")
_SslCiphers_ObjectIdentity = ObjectIdentity
sslCiphers = _SslCiphers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 5, 2)
)


class _SslCipherSuiteList_Type(Bits):
    """Custom type sslCipherSuiteList based on Bits"""
    namedValues = NamedValues(
        *(("dh-rsa-3des-sha", 5),
          ("dh-rsa-des-sha", 4),
          ("rsa-3des-sha", 3),
          ("rsa-des-sha", 2),
          ("rsa-exp1024-des-sha", 6),
          ("rsa-null-md5", 0),
          ("rsa-null-sha", 1))
    )

_SslCipherSuiteList_Type.__name__ = "Bits"
_SslCipherSuiteList_Object = MibScalar
sslCipherSuiteList = _SslCipherSuiteList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 5, 2, 1),
    _SslCipherSuiteList_Type()
)
sslCipherSuiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCipherSuiteList.setStatus("current")
_SecurityDhcpServerScreen_ObjectIdentity = ObjectIdentity
securityDhcpServerScreen = _SecurityDhcpServerScreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7)
)
_DhcpServerScreenEnablePortlist_Type = PortList
_DhcpServerScreenEnablePortlist_Object = MibScalar
dhcpServerScreenEnablePortlist = _DhcpServerScreenEnablePortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 1),
    _DhcpServerScreenEnablePortlist_Type()
)
dhcpServerScreenEnablePortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenEnablePortlist.setStatus("current")
_Ipv4dhcpServerScreenServerTable_Object = MibTable
ipv4dhcpServerScreenServerTable = _Ipv4dhcpServerScreenServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 2)
)
if mibBuilder.loadTexts:
    ipv4dhcpServerScreenServerTable.setStatus("obsolete")
_Ipv4dhcpServerScreenServerEntry_Object = MibTableRow
ipv4dhcpServerScreenServerEntry = _Ipv4dhcpServerScreenServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 2, 1)
)
ipv4dhcpServerScreenServerEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "ipv4dhcpServerScreenServerIndex"),
)
if mibBuilder.loadTexts:
    ipv4dhcpServerScreenServerEntry.setStatus("obsolete")


class _Ipv4dhcpServerScreenServerIndex_Type(Integer32):
    """Custom type ipv4dhcpServerScreenServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Ipv4dhcpServerScreenServerIndex_Type.__name__ = "Integer32"
_Ipv4dhcpServerScreenServerIndex_Object = MibTableColumn
ipv4dhcpServerScreenServerIndex = _Ipv4dhcpServerScreenServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 2, 1, 1),
    _Ipv4dhcpServerScreenServerIndex_Type()
)
ipv4dhcpServerScreenServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4dhcpServerScreenServerIndex.setStatus("obsolete")
_Ipv4dhcpServerScreenServerAddress_Type = IpAddress
_Ipv4dhcpServerScreenServerAddress_Object = MibTableColumn
ipv4dhcpServerScreenServerAddress = _Ipv4dhcpServerScreenServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 2, 1, 2),
    _Ipv4dhcpServerScreenServerAddress_Type()
)
ipv4dhcpServerScreenServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4dhcpServerScreenServerAddress.setStatus("obsolete")
_Ipv4dhcpServerScreenServerStatus_Type = RowStatus
_Ipv4dhcpServerScreenServerStatus_Object = MibTableColumn
ipv4dhcpServerScreenServerStatus = _Ipv4dhcpServerScreenServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 2, 1, 3),
    _Ipv4dhcpServerScreenServerStatus_Type()
)
ipv4dhcpServerScreenServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4dhcpServerScreenServerStatus.setStatus("obsolete")
_DhcpServerScreenTrustedServerTable_Object = MibTable
dhcpServerScreenTrustedServerTable = _DhcpServerScreenTrustedServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 3)
)
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerTable.setStatus("current")
_DhcpServerScreenTrustedServerEntry_Object = MibTableRow
dhcpServerScreenTrustedServerEntry = _DhcpServerScreenTrustedServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 3, 1)
)
dhcpServerScreenTrustedServerEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "dhcpServerScreenTrustedServerIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerEntry.setStatus("current")


class _DhcpServerScreenTrustedServerIndex_Type(Integer32):
    """Custom type dhcpServerScreenTrustedServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DhcpServerScreenTrustedServerIndex_Type.__name__ = "Integer32"
_DhcpServerScreenTrustedServerIndex_Object = MibTableColumn
dhcpServerScreenTrustedServerIndex = _DhcpServerScreenTrustedServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 3, 1, 1),
    _DhcpServerScreenTrustedServerIndex_Type()
)
dhcpServerScreenTrustedServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerIndex.setStatus("current")
_DhcpServerScreenTrustedServerAddress_Type = Ipv6Address
_DhcpServerScreenTrustedServerAddress_Object = MibTableColumn
dhcpServerScreenTrustedServerAddress = _DhcpServerScreenTrustedServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 3, 1, 2),
    _DhcpServerScreenTrustedServerAddress_Type()
)
dhcpServerScreenTrustedServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerAddress.setStatus("current")


class _DhcpServerScreenIPType_Type(Integer32):
    """Custom type dhcpServerScreenIPType based on Integer32"""
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


_DhcpServerScreenIPType_Type.__name__ = "Integer32"
_DhcpServerScreenIPType_Object = MibTableColumn
dhcpServerScreenIPType = _DhcpServerScreenIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 3, 1, 3),
    _DhcpServerScreenIPType_Type()
)
dhcpServerScreenIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenIPType.setStatus("current")
_DhcpServerScreenTrustedServerStatus_Type = RowStatus
_DhcpServerScreenTrustedServerStatus_Object = MibTableColumn
dhcpServerScreenTrustedServerStatus = _DhcpServerScreenTrustedServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 7, 3, 1, 4),
    _DhcpServerScreenTrustedServerStatus_Type()
)
dhcpServerScreenTrustedServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerStatus.setStatus("current")
_SecurityTrafficSeg_ObjectIdentity = ObjectIdentity
securityTrafficSeg = _SecurityTrafficSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 9)
)


class _TrafficSegStatus_Type(Integer32):
    """Custom type trafficSegStatus based on Integer32"""
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


_TrafficSegStatus_Type.__name__ = "Integer32"
_TrafficSegStatus_Object = MibScalar
trafficSegStatus = _TrafficSegStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 9, 1),
    _TrafficSegStatus_Type()
)
trafficSegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegStatus.setStatus("current")
_TrafficSegTable_Object = MibTable
trafficSegTable = _TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 9, 2)
)
if mibBuilder.loadTexts:
    trafficSegTable.setStatus("current")
_TrafficSegEntry_Object = MibTableRow
trafficSegEntry = _TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 9, 2, 1)
)
trafficSegEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "trafficSegIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegEntry.setStatus("current")
_TrafficSegIfIndex_Type = InterfaceIndex
_TrafficSegIfIndex_Object = MibTableColumn
trafficSegIfIndex = _TrafficSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 9, 2, 1, 1),
    _TrafficSegIfIndex_Type()
)
trafficSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegIfIndex.setStatus("current")
_TrafficSegMemberList_Type = PortList
_TrafficSegMemberList_Object = MibTableColumn
trafficSegMemberList = _TrafficSegMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 9, 2, 1, 2),
    _TrafficSegMemberList_Type()
)
trafficSegMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegMemberList.setStatus("current")
_SecurityIpMacPortBinding_ObjectIdentity = ObjectIdentity
securityIpMacPortBinding = _SecurityIpMacPortBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10)
)
_ImpbSettingTable_Object = MibTable
impbSettingTable = _ImpbSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 1)
)
if mibBuilder.loadTexts:
    impbSettingTable.setStatus("current")
_ImpbSettingEntry_Object = MibTableRow
impbSettingEntry = _ImpbSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 1, 1)
)
impbSettingEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "impbPortIndex"),
)
if mibBuilder.loadTexts:
    impbSettingEntry.setStatus("current")
_ImpbPortIndex_Type = Integer32
_ImpbPortIndex_Object = MibTableColumn
impbPortIndex = _ImpbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 1, 1, 1),
    _ImpbPortIndex_Type()
)
impbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbPortIndex.setStatus("current")


class _ImpbPortState_Type(Integer32):
    """Custom type impbPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ImpbPortState_Type.__name__ = "Integer32"
_ImpbPortState_Object = MibTableColumn
impbPortState = _ImpbPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 1, 1, 2),
    _ImpbPortState_Type()
)
impbPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbPortState.setStatus("current")


class _ImpbInsIpPacPortState_Type(Integer32):
    """Custom type impbInsIpPacPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ImpbInsIpPacPortState_Type.__name__ = "Integer32"
_ImpbInsIpPacPortState_Object = MibTableColumn
impbInsIpPacPortState = _ImpbInsIpPacPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 1, 1, 3),
    _ImpbInsIpPacPortState_Type()
)
impbInsIpPacPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbInsIpPacPortState.setStatus("current")


class _ImpbDHCPPortState_Type(Integer32):
    """Custom type impbDHCPPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ImpbDHCPPortState_Type.__name__ = "Integer32"
_ImpbDHCPPortState_Object = MibTableColumn
impbDHCPPortState = _ImpbDHCPPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 1, 1, 4),
    _ImpbDHCPPortState_Type()
)
impbDHCPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbDHCPPortState.setStatus("current")
_ImpbSmartTable_Object = MibTable
impbSmartTable = _ImpbSmartTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 2)
)
if mibBuilder.loadTexts:
    impbSmartTable.setStatus("current")
_ImpbSmartEntry_Object = MibTableRow
impbSmartEntry = _ImpbSmartEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 2, 1)
)
impbSmartEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "impbSmartMacAddress"),
    (0, "DGS-1210-20_BX", "impbSmartPort"),
    (0, "DGS-1210-20_BX", "impbSmartIpAddress"),
)
if mibBuilder.loadTexts:
    impbSmartEntry.setStatus("current")
_ImpbSmartMacAddress_Type = MacAddress
_ImpbSmartMacAddress_Object = MibTableColumn
impbSmartMacAddress = _ImpbSmartMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 2, 1, 1),
    _ImpbSmartMacAddress_Type()
)
impbSmartMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartMacAddress.setStatus("current")
_ImpbSmartPort_Type = Integer32
_ImpbSmartPort_Object = MibTableColumn
impbSmartPort = _ImpbSmartPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 2, 1, 2),
    _ImpbSmartPort_Type()
)
impbSmartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartPort.setStatus("current")
_ImpbSmartIpAddress_Type = IpAddress
_ImpbSmartIpAddress_Object = MibTableColumn
impbSmartIpAddress = _ImpbSmartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 2, 1, 3),
    _ImpbSmartIpAddress_Type()
)
impbSmartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartIpAddress.setStatus("current")
_ImpbSmartVlanId_Type = Integer32
_ImpbSmartVlanId_Object = MibTableColumn
impbSmartVlanId = _ImpbSmartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 2, 1, 4),
    _ImpbSmartVlanId_Type()
)
impbSmartVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartVlanId.setStatus("current")


class _ImpbSmartBinding_Type(Integer32):
    """Custom type impbSmartBinding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ImpbSmartBinding_Type.__name__ = "Integer32"
_ImpbSmartBinding_Object = MibTableColumn
impbSmartBinding = _ImpbSmartBinding_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 2, 1, 5),
    _ImpbSmartBinding_Type()
)
impbSmartBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbSmartBinding.setStatus("current")
_ImpbWhiteListTable_Object = MibTable
impbWhiteListTable = _ImpbWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 3)
)
if mibBuilder.loadTexts:
    impbWhiteListTable.setStatus("current")
_ImpbWhiteListEntry_Object = MibTableRow
impbWhiteListEntry = _ImpbWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 3, 1)
)
impbWhiteListEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "impbWhiteListIpAddress"),
    (0, "DGS-1210-20_BX", "impbWhiteListMacAddress"),
)
if mibBuilder.loadTexts:
    impbWhiteListEntry.setStatus("current")
_ImpbWhiteListIpAddress_Type = IpAddress
_ImpbWhiteListIpAddress_Object = MibTableColumn
impbWhiteListIpAddress = _ImpbWhiteListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 3, 1, 1),
    _ImpbWhiteListIpAddress_Type()
)
impbWhiteListIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbWhiteListIpAddress.setStatus("current")
_ImpbWhiteListMacAddress_Type = MacAddress
_ImpbWhiteListMacAddress_Object = MibTableColumn
impbWhiteListMacAddress = _ImpbWhiteListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 3, 1, 2),
    _ImpbWhiteListMacAddress_Type()
)
impbWhiteListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbWhiteListMacAddress.setStatus("current")
_ImpbWhiteListPort_Type = Integer32
_ImpbWhiteListPort_Object = MibTableColumn
impbWhiteListPort = _ImpbWhiteListPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 3, 1, 3),
    _ImpbWhiteListPort_Type()
)
impbWhiteListPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbWhiteListPort.setStatus("current")
_ImpbWhiteListRowStatus_Type = RowStatus
_ImpbWhiteListRowStatus_Object = MibTableColumn
impbWhiteListRowStatus = _ImpbWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 3, 1, 4),
    _ImpbWhiteListRowStatus_Type()
)
impbWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    impbWhiteListRowStatus.setStatus("current")
_ImpbBlackListTable_Object = MibTable
impbBlackListTable = _ImpbBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 4)
)
if mibBuilder.loadTexts:
    impbBlackListTable.setStatus("current")
_ImpbBlackListEntry_Object = MibTableRow
impbBlackListEntry = _ImpbBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 4, 1)
)
impbBlackListEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "impbBlackListMacAddress"),
    (0, "DGS-1210-20_BX", "impbBlackListVlanId"),
    (0, "DGS-1210-20_BX", "impbBlackListPort"),
)
if mibBuilder.loadTexts:
    impbBlackListEntry.setStatus("current")
_ImpbBlackListMacAddress_Type = MacAddress
_ImpbBlackListMacAddress_Object = MibTableColumn
impbBlackListMacAddress = _ImpbBlackListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 4, 1, 1),
    _ImpbBlackListMacAddress_Type()
)
impbBlackListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListMacAddress.setStatus("current")
_ImpbBlackListVlanId_Type = Integer32
_ImpbBlackListVlanId_Object = MibTableColumn
impbBlackListVlanId = _ImpbBlackListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 4, 1, 2),
    _ImpbBlackListVlanId_Type()
)
impbBlackListVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListVlanId.setStatus("current")
_ImpbBlackListPort_Type = Integer32
_ImpbBlackListPort_Object = MibTableColumn
impbBlackListPort = _ImpbBlackListPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 4, 1, 3),
    _ImpbBlackListPort_Type()
)
impbBlackListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListPort.setStatus("current")
_ImpbBlackListIpAddress_Type = IpAddress
_ImpbBlackListIpAddress_Object = MibTableColumn
impbBlackListIpAddress = _ImpbBlackListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 4, 1, 4),
    _ImpbBlackListIpAddress_Type()
)
impbBlackListIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListIpAddress.setStatus("current")


class _ImpbBlackListStatus_Type(Integer32):
    """Custom type impbBlackListStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("nothing", 0))
    )


_ImpbBlackListStatus_Type.__name__ = "Integer32"
_ImpbBlackListStatus_Object = MibTableColumn
impbBlackListStatus = _ImpbBlackListStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 4, 1, 5),
    _ImpbBlackListStatus_Type()
)
impbBlackListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbBlackListStatus.setStatus("current")
_ImpbAutoScanIpAddressFrom_Type = IpAddress
_ImpbAutoScanIpAddressFrom_Object = MibScalar
impbAutoScanIpAddressFrom = _ImpbAutoScanIpAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 5),
    _ImpbAutoScanIpAddressFrom_Type()
)
impbAutoScanIpAddressFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbAutoScanIpAddressFrom.setStatus("current")
_ImpbAutoScanIpAddressTo_Type = IpAddress
_ImpbAutoScanIpAddressTo_Object = MibScalar
impbAutoScanIpAddressTo = _ImpbAutoScanIpAddressTo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 6),
    _ImpbAutoScanIpAddressTo_Type()
)
impbAutoScanIpAddressTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbAutoScanIpAddressTo.setStatus("current")


class _ImpbAutoScanStatus_Type(Integer32):
    """Custom type impbAutoScanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("scan", 1))
    )


_ImpbAutoScanStatus_Type.__name__ = "Integer32"
_ImpbAutoScanStatus_Object = MibScalar
impbAutoScanStatus = _ImpbAutoScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 14, 10, 7),
    _ImpbAutoScanStatus_Type()
)
impbAutoScanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbAutoScanStatus.setStatus("current")
_CompanyACLGroup_ObjectIdentity = ObjectIdentity
companyACLGroup = _CompanyACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15)
)
_AclProfile_ObjectIdentity = ObjectIdentity
aclProfile = _AclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1)
)
_Ipv4aclProfileTable_Object = MibTable
ipv4aclProfileTable = _Ipv4aclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1)
)
if mibBuilder.loadTexts:
    ipv4aclProfileTable.setStatus("obsolete")
_Ipv4aclProfileEntry_Object = MibTableRow
ipv4aclProfileEntry = _Ipv4aclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1)
)
ipv4aclProfileEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "ipv4aclProfileNo"),
)
if mibBuilder.loadTexts:
    ipv4aclProfileEntry.setStatus("obsolete")


class _Ipv4aclProfileNo_Type(Integer32):
    """Custom type ipv4aclProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Ipv4aclProfileNo_Type.__name__ = "Integer32"
_Ipv4aclProfileNo_Object = MibTableColumn
ipv4aclProfileNo = _Ipv4aclProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 1),
    _Ipv4aclProfileNo_Type()
)
ipv4aclProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4aclProfileNo.setStatus("obsolete")


class _Ipv4aclProfileType_Type(Integer32):
    """Custom type ipv4aclProfileType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aclQoS", 8),
          ("arpSP_deny", 5),
          ("arpSP_permit", 4),
          ("dhcpServerScreen", 10),
          ("impb", 3),
          ("l2", 1),
          ("l3", 2),
          ("surveillanceVlan", 7),
          ("voiceVlan", 6))
    )


_Ipv4aclProfileType_Type.__name__ = "Integer32"
_Ipv4aclProfileType_Object = MibTableColumn
ipv4aclProfileType = _Ipv4aclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 2),
    _Ipv4aclProfileType_Type()
)
ipv4aclProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileType.setStatus("obsolete")


class _Ipv4aclProfileRuleCount_Type(Integer32):
    """Custom type ipv4aclProfileRuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv4aclProfileRuleCount_Type.__name__ = "Integer32"
_Ipv4aclProfileRuleCount_Object = MibTableColumn
ipv4aclProfileRuleCount = _Ipv4aclProfileRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 3),
    _Ipv4aclProfileRuleCount_Type()
)
ipv4aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4aclProfileRuleCount.setStatus("obsolete")
_Ipv4aclProfileMask_Type = OctetString
_Ipv4aclProfileMask_Object = MibTableColumn
ipv4aclProfileMask = _Ipv4aclProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 4),
    _Ipv4aclProfileMask_Type()
)
ipv4aclProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileMask.setStatus("obsolete")
_Ipv4aclProfileDstMacAddrMask_Type = MacAddress
_Ipv4aclProfileDstMacAddrMask_Object = MibTableColumn
ipv4aclProfileDstMacAddrMask = _Ipv4aclProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 5),
    _Ipv4aclProfileDstMacAddrMask_Type()
)
ipv4aclProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileDstMacAddrMask.setStatus("obsolete")
_Ipv4aclProfileSrcMacAddrMask_Type = MacAddress
_Ipv4aclProfileSrcMacAddrMask_Object = MibTableColumn
ipv4aclProfileSrcMacAddrMask = _Ipv4aclProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 6),
    _Ipv4aclProfileSrcMacAddrMask_Type()
)
ipv4aclProfileSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileSrcMacAddrMask.setStatus("obsolete")


class _Ipv4aclProfileIPProtocol_Type(Integer32):
    """Custom type ipv4aclProfileIPProtocol based on Integer32"""
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


_Ipv4aclProfileIPProtocol_Type.__name__ = "Integer32"
_Ipv4aclProfileIPProtocol_Object = MibTableColumn
ipv4aclProfileIPProtocol = _Ipv4aclProfileIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 7),
    _Ipv4aclProfileIPProtocol_Type()
)
ipv4aclProfileIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileIPProtocol.setStatus("obsolete")


class _Ipv4aclProfileDstIpAddrMask_Type(IpAddress):
    """Custom type ipv4aclProfileDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Ipv4aclProfileDstIpAddrMask_Object = MibTableColumn
ipv4aclProfileDstIpAddrMask = _Ipv4aclProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 8),
    _Ipv4aclProfileDstIpAddrMask_Type()
)
ipv4aclProfileDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileDstIpAddrMask.setStatus("obsolete")


class _Ipv4aclProfileSrcIpAddrMask_Type(IpAddress):
    """Custom type ipv4aclProfileSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Ipv4aclProfileSrcIpAddrMask_Object = MibTableColumn
ipv4aclProfileSrcIpAddrMask = _Ipv4aclProfileSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 9),
    _Ipv4aclProfileSrcIpAddrMask_Type()
)
ipv4aclProfileSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileSrcIpAddrMask.setStatus("obsolete")


class _Ipv4aclProfileDstPortMask_Type(OctetString):
    """Custom type ipv4aclProfileDstPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_Ipv4aclProfileDstPortMask_Object = MibTableColumn
ipv4aclProfileDstPortMask = _Ipv4aclProfileDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 10),
    _Ipv4aclProfileDstPortMask_Type()
)
ipv4aclProfileDstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileDstPortMask.setStatus("obsolete")


class _Ipv4aclProfileSrcPortMask_Type(OctetString):
    """Custom type ipv4aclProfileSrcPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_Ipv4aclProfileSrcPortMask_Object = MibTableColumn
ipv4aclProfileSrcPortMask = _Ipv4aclProfileSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 11),
    _Ipv4aclProfileSrcPortMask_Type()
)
ipv4aclProfileSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileSrcPortMask.setStatus("obsolete")


class _Ipv4aclProfileArpSenderMacAddrMask_Type(MacAddress):
    """Custom type ipv4aclProfileArpSenderMacAddrMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFF"


_Ipv4aclProfileArpSenderMacAddrMask_Object = MibTableColumn
ipv4aclProfileArpSenderMacAddrMask = _Ipv4aclProfileArpSenderMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 12),
    _Ipv4aclProfileArpSenderMacAddrMask_Type()
)
ipv4aclProfileArpSenderMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4aclProfileArpSenderMacAddrMask.setStatus("obsolete")


class _Ipv4aclProfileArpSenderIpAddrMask_Type(IpAddress):
    """Custom type ipv4aclProfileArpSenderIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Ipv4aclProfileArpSenderIpAddrMask_Object = MibTableColumn
ipv4aclProfileArpSenderIpAddrMask = _Ipv4aclProfileArpSenderIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 13),
    _Ipv4aclProfileArpSenderIpAddrMask_Type()
)
ipv4aclProfileArpSenderIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4aclProfileArpSenderIpAddrMask.setStatus("obsolete")
_Ipv4aclProfileStatus_Type = RowStatus
_Ipv4aclProfileStatus_Object = MibTableColumn
ipv4aclProfileStatus = _Ipv4aclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 1, 1, 14),
    _Ipv4aclProfileStatus_Type()
)
ipv4aclProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4aclProfileStatus.setStatus("obsolete")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1)
)
aclProfileEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "aclProfileNo"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")


class _AclProfileNo_Type(Integer32):
    """Custom type aclProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclProfileNo_Type.__name__ = "Integer32"
_AclProfileNo_Object = MibTableColumn
aclProfileNo = _AclProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 1),
    _AclProfileNo_Type()
)
aclProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileNo.setStatus("current")


class _AclProfileType_Type(Integer32):
    """Custom type aclProfileType based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aclQoS", 8),
          ("arpSP_deny", 5),
          ("arpSP_permit", 4),
          ("dhcpServerScreen", 10),
          ("impb", 3),
          ("l2", 1),
          ("l3v4", 2),
          ("l3v6", 11),
          ("surveillanceVlan", 7),
          ("voiceVlan", 6),
          ("zone_defense", 12))
    )


_AclProfileType_Type.__name__ = "Integer32"
_AclProfileType_Object = MibTableColumn
aclProfileType = _AclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 2),
    _AclProfileType_Type()
)
aclProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileType.setStatus("current")


class _AclProfileRuleCount_Type(Integer32):
    """Custom type aclProfileRuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclProfileRuleCount_Type.__name__ = "Integer32"
_AclProfileRuleCount_Object = MibTableColumn
aclProfileRuleCount = _AclProfileRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 3),
    _AclProfileRuleCount_Type()
)
aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleCount.setStatus("current")
_AclProfileMask_Type = OctetString
_AclProfileMask_Object = MibTableColumn
aclProfileMask = _AclProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 4),
    _AclProfileMask_Type()
)
aclProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileMask.setStatus("current")
_AclProfileDstMacAddrMask_Type = MacAddress
_AclProfileDstMacAddrMask_Object = MibTableColumn
aclProfileDstMacAddrMask = _AclProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 5),
    _AclProfileDstMacAddrMask_Type()
)
aclProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstMacAddrMask.setStatus("current")
_AclProfileSrcMacAddrMask_Type = MacAddress
_AclProfileSrcMacAddrMask_Object = MibTableColumn
aclProfileSrcMacAddrMask = _AclProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 6),
    _AclProfileSrcMacAddrMask_Type()
)
aclProfileSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileSrcMacAddrMask.setStatus("current")


class _AclProfileIPProtocol_Type(Integer32):
    """Custom type aclProfileIPProtocol based on Integer32"""
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


_AclProfileIPProtocol_Type.__name__ = "Integer32"
_AclProfileIPProtocol_Object = MibTableColumn
aclProfileIPProtocol = _AclProfileIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 7),
    _AclProfileIPProtocol_Type()
)
aclProfileIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileIPProtocol.setStatus("current")


class _AclProfileDstIpAddrMaskType_Type(Integer32):
    """Custom type aclProfileDstIpAddrMaskType based on Integer32"""
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


_AclProfileDstIpAddrMaskType_Type.__name__ = "Integer32"
_AclProfileDstIpAddrMaskType_Object = MibTableColumn
aclProfileDstIpAddrMaskType = _AclProfileDstIpAddrMaskType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 8),
    _AclProfileDstIpAddrMaskType_Type()
)
aclProfileDstIpAddrMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstIpAddrMaskType.setStatus("current")


class _AclProfileDstIpAddrMask_Type(Ipv6Address):
    """Custom type aclProfileDstIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_AclProfileDstIpAddrMask_Object = MibTableColumn
aclProfileDstIpAddrMask = _AclProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 9),
    _AclProfileDstIpAddrMask_Type()
)
aclProfileDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstIpAddrMask.setStatus("current")


class _AclProfileSrcIpAddrMaskType_Type(Integer32):
    """Custom type aclProfileSrcIpAddrMaskType based on Integer32"""
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


_AclProfileSrcIpAddrMaskType_Type.__name__ = "Integer32"
_AclProfileSrcIpAddrMaskType_Object = MibTableColumn
aclProfileSrcIpAddrMaskType = _AclProfileSrcIpAddrMaskType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 10),
    _AclProfileSrcIpAddrMaskType_Type()
)
aclProfileSrcIpAddrMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileSrcIpAddrMaskType.setStatus("current")


class _AclProfileSrcIpAddrMask_Type(Ipv6Address):
    """Custom type aclProfileSrcIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_AclProfileSrcIpAddrMask_Object = MibTableColumn
aclProfileSrcIpAddrMask = _AclProfileSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 11),
    _AclProfileSrcIpAddrMask_Type()
)
aclProfileSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileSrcIpAddrMask.setStatus("current")


class _AclProfileDstPortMask_Type(OctetString):
    """Custom type aclProfileDstPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_AclProfileDstPortMask_Object = MibTableColumn
aclProfileDstPortMask = _AclProfileDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 12),
    _AclProfileDstPortMask_Type()
)
aclProfileDstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstPortMask.setStatus("current")


class _AclProfileSrcPortMask_Type(OctetString):
    """Custom type aclProfileSrcPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_AclProfileSrcPortMask_Object = MibTableColumn
aclProfileSrcPortMask = _AclProfileSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 13),
    _AclProfileSrcPortMask_Type()
)
aclProfileSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileSrcPortMask.setStatus("current")


class _AclProfileArpSenderMacAddrMask_Type(MacAddress):
    """Custom type aclProfileArpSenderMacAddrMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFF"


_AclProfileArpSenderMacAddrMask_Object = MibTableColumn
aclProfileArpSenderMacAddrMask = _AclProfileArpSenderMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 14),
    _AclProfileArpSenderMacAddrMask_Type()
)
aclProfileArpSenderMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileArpSenderMacAddrMask.setStatus("current")


class _AclProfileArpSenderIpAddrMask_Type(Ipv6Address):
    """Custom type aclProfileArpSenderIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_AclProfileArpSenderIpAddrMask_Object = MibTableColumn
aclProfileArpSenderIpAddrMask = _AclProfileArpSenderIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 15),
    _AclProfileArpSenderIpAddrMask_Type()
)
aclProfileArpSenderIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileArpSenderIpAddrMask.setStatus("current")
_AclProfileStatus_Type = RowStatus
_AclProfileStatus_Object = MibTableColumn
aclProfileStatus = _AclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 1, 2, 1, 16),
    _AclProfileStatus_Type()
)
aclProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileStatus.setStatus("current")
_AclL2Rule_ObjectIdentity = ObjectIdentity
aclL2Rule = _AclL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2)
)
_AclL2RuleTable_Object = MibTable
aclL2RuleTable = _AclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1)
)
if mibBuilder.loadTexts:
    aclL2RuleTable.setStatus("current")
_AclL2RuleEntry_Object = MibTableRow
aclL2RuleEntry = _AclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1)
)
aclL2RuleEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "aclL2AccessID"),
    (0, "DGS-1210-20_BX", "aclL2ProfileID"),
)
if mibBuilder.loadTexts:
    aclL2RuleEntry.setStatus("current")


class _AclL2AccessID_Type(Integer32):
    """Custom type aclL2AccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL2AccessID_Type.__name__ = "Integer32"
_AclL2AccessID_Object = MibTableColumn
aclL2AccessID = _AclL2AccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 1),
    _AclL2AccessID_Type()
)
aclL2AccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2AccessID.setStatus("current")


class _AclL2ProfileID_Type(Integer32):
    """Custom type aclL2ProfileID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL2ProfileID_Type.__name__ = "Integer32"
_AclL2ProfileID_Object = MibTableColumn
aclL2ProfileID = _AclL2ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 2),
    _AclL2ProfileID_Type()
)
aclL2ProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2ProfileID.setStatus("current")


class _AclL2RuleEtherType_Type(Integer32):
    """Custom type aclL2RuleEtherType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1501, 65535),
    )


_AclL2RuleEtherType_Type.__name__ = "Integer32"
_AclL2RuleEtherType_Object = MibTableColumn
aclL2RuleEtherType = _AclL2RuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 3),
    _AclL2RuleEtherType_Type()
)
aclL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleEtherType.setStatus("current")
_AclL2RuleDstMacAddr_Type = MacAddress
_AclL2RuleDstMacAddr_Object = MibTableColumn
aclL2RuleDstMacAddr = _AclL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 4),
    _AclL2RuleDstMacAddr_Type()
)
aclL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddr.setStatus("current")
_AclL2RuleSrcMacAddr_Type = MacAddress
_AclL2RuleSrcMacAddr_Object = MibTableColumn
aclL2RuleSrcMacAddr = _AclL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 5),
    _AclL2RuleSrcMacAddr_Type()
)
aclL2RuleSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddr.setStatus("current")


class _AclL2RuleVlanId_Type(Integer32):
    """Custom type aclL2RuleVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_AclL2RuleVlanId_Type.__name__ = "Integer32"
_AclL2RuleVlanId_Object = MibTableColumn
aclL2RuleVlanId = _AclL2RuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 6),
    _AclL2RuleVlanId_Type()
)
aclL2RuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleVlanId.setStatus("current")


class _AclL2Rule1pPriority_Type(Integer32):
    """Custom type aclL2Rule1pPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL2Rule1pPriority_Type.__name__ = "Integer32"
_AclL2Rule1pPriority_Object = MibTableColumn
aclL2Rule1pPriority = _AclL2Rule1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 7),
    _AclL2Rule1pPriority_Type()
)
aclL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2Rule1pPriority.setStatus("current")
_AclL2RuleDstMacAddrMask_Type = MacAddress
_AclL2RuleDstMacAddrMask_Object = MibTableColumn
aclL2RuleDstMacAddrMask = _AclL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 8),
    _AclL2RuleDstMacAddrMask_Type()
)
aclL2RuleDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddrMask.setStatus("current")
_AclL2RuleSrcMacAddrMask_Type = MacAddress
_AclL2RuleSrcMacAddrMask_Object = MibTableColumn
aclL2RuleSrcMacAddrMask = _AclL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 9),
    _AclL2RuleSrcMacAddrMask_Type()
)
aclL2RuleSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddrMask.setStatus("current")
_AclL2RuleInPortList_Type = PortList
_AclL2RuleInPortList_Object = MibTableColumn
aclL2RuleInPortList = _AclL2RuleInPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 10),
    _AclL2RuleInPortList_Type()
)
aclL2RuleInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleInPortList.setStatus("current")


class _AclL2RuleAction_Type(Integer32):
    """Custom type aclL2RuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclL2RuleAction_Type.__name__ = "Integer32"
_AclL2RuleAction_Object = MibTableColumn
aclL2RuleAction = _AclL2RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 11),
    _AclL2RuleAction_Type()
)
aclL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleAction.setStatus("current")
_AclL2RuleStatus_Type = RowStatus
_AclL2RuleStatus_Object = MibTableColumn
aclL2RuleStatus = _AclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 2, 1, 1, 13),
    _AclL2RuleStatus_Type()
)
aclL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL2RuleStatus.setStatus("current")
_AclL3Rule_ObjectIdentity = ObjectIdentity
aclL3Rule = _AclL3Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3)
)
_AclL3RuleTable_Object = MibTable
aclL3RuleTable = _AclL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1)
)
if mibBuilder.loadTexts:
    aclL3RuleTable.setStatus("current")
_AclL3RuleEntry_Object = MibTableRow
aclL3RuleEntry = _AclL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1)
)
aclL3RuleEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "aclL3RuleAccessID"),
    (0, "DGS-1210-20_BX", "aclL3RuleProfileNo"),
)
if mibBuilder.loadTexts:
    aclL3RuleEntry.setStatus("current")


class _AclL3RuleAccessID_Type(Integer32):
    """Custom type aclL3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3RuleAccessID_Type.__name__ = "Integer32"
_AclL3RuleAccessID_Object = MibTableColumn
aclL3RuleAccessID = _AclL3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 1),
    _AclL3RuleAccessID_Type()
)
aclL3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleAccessID.setStatus("current")


class _AclL3RuleProfileNo_Type(Integer32):
    """Custom type aclL3RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3RuleProfileNo_Type.__name__ = "Integer32"
_AclL3RuleProfileNo_Object = MibTableColumn
aclL3RuleProfileNo = _AclL3RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 2),
    _AclL3RuleProfileNo_Type()
)
aclL3RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleProfileNo.setStatus("current")


class _AclL3RuleProtocol_Type(Integer32):
    """Custom type aclL3RuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("tcp", 6),
          ("udp", 17))
    )


_AclL3RuleProtocol_Type.__name__ = "Integer32"
_AclL3RuleProtocol_Object = MibTableColumn
aclL3RuleProtocol = _AclL3RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 3),
    _AclL3RuleProtocol_Type()
)
aclL3RuleProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleProtocol.setStatus("current")


class _AclL3RuleICMPMessageType_Type(Integer32):
    """Custom type aclL3RuleICMPMessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3RuleICMPMessageType_Type.__name__ = "Integer32"
_AclL3RuleICMPMessageType_Object = MibTableColumn
aclL3RuleICMPMessageType = _AclL3RuleICMPMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 4),
    _AclL3RuleICMPMessageType_Type()
)
aclL3RuleICMPMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleICMPMessageType.setStatus("current")


class _AclL3RuleICMPMessageCode_Type(Integer32):
    """Custom type aclL3RuleICMPMessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3RuleICMPMessageCode_Type.__name__ = "Integer32"
_AclL3RuleICMPMessageCode_Object = MibTableColumn
aclL3RuleICMPMessageCode = _AclL3RuleICMPMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 5),
    _AclL3RuleICMPMessageCode_Type()
)
aclL3RuleICMPMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleICMPMessageCode.setStatus("current")


class _AclL3RuleDstIpAddr_Type(IpAddress):
    """Custom type aclL3RuleDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3RuleDstIpAddr_Object = MibTableColumn
aclL3RuleDstIpAddr = _AclL3RuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 6),
    _AclL3RuleDstIpAddr_Type()
)
aclL3RuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleDstIpAddr.setStatus("current")


class _AclL3RuleSrcIpAddr_Type(IpAddress):
    """Custom type aclL3RuleSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3RuleSrcIpAddr_Object = MibTableColumn
aclL3RuleSrcIpAddr = _AclL3RuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 7),
    _AclL3RuleSrcIpAddr_Type()
)
aclL3RuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleSrcIpAddr.setStatus("current")


class _AclL3RuleDstIpAddrMask_Type(IpAddress):
    """Custom type aclL3RuleDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3RuleDstIpAddrMask_Object = MibTableColumn
aclL3RuleDstIpAddrMask = _AclL3RuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 8),
    _AclL3RuleDstIpAddrMask_Type()
)
aclL3RuleDstIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleDstIpAddrMask.setStatus("current")


class _AclL3RuleSrcIpAddrMask_Type(IpAddress):
    """Custom type aclL3RuleSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3RuleSrcIpAddrMask_Object = MibTableColumn
aclL3RuleSrcIpAddrMask = _AclL3RuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 9),
    _AclL3RuleSrcIpAddrMask_Type()
)
aclL3RuleSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleSrcIpAddrMask.setStatus("current")


class _AclL3RuleTcpUdpDstPort_Type(Integer32):
    """Custom type aclL3RuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3RuleTcpUdpDstPort_Type.__name__ = "Integer32"
_AclL3RuleTcpUdpDstPort_Object = MibTableColumn
aclL3RuleTcpUdpDstPort = _AclL3RuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 10),
    _AclL3RuleTcpUdpDstPort_Type()
)
aclL3RuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpDstPort.setStatus("current")


class _AclL3RuleTcpUdpSrcPort_Type(Integer32):
    """Custom type aclL3RuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3RuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_AclL3RuleTcpUdpSrcPort_Object = MibTableColumn
aclL3RuleTcpUdpSrcPort = _AclL3RuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 11),
    _AclL3RuleTcpUdpSrcPort_Type()
)
aclL3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpSrcPort.setStatus("current")
_AclL3RuleTcpUdpDstPortMask_Type = OctetString
_AclL3RuleTcpUdpDstPortMask_Object = MibTableColumn
aclL3RuleTcpUdpDstPortMask = _AclL3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 12),
    _AclL3RuleTcpUdpDstPortMask_Type()
)
aclL3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpDstPortMask.setStatus("current")
_AclL3RuleTcpUdpSrcPortMask_Type = OctetString
_AclL3RuleTcpUdpSrcPortMask_Object = MibTableColumn
aclL3RuleTcpUdpSrcPortMask = _AclL3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 13),
    _AclL3RuleTcpUdpSrcPortMask_Type()
)
aclL3RuleTcpUdpSrcPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpSrcPortMask.setStatus("current")


class _AclL3RuleTcpAckBit_Type(Integer32):
    """Custom type aclL3RuleTcpAckBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpAckBit_Type.__name__ = "Integer32"
_AclL3RuleTcpAckBit_Object = MibTableColumn
aclL3RuleTcpAckBit = _AclL3RuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 14),
    _AclL3RuleTcpAckBit_Type()
)
aclL3RuleTcpAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleTcpAckBit.setStatus("current")


class _AclL3RuleTcpRstBit_Type(Integer32):
    """Custom type aclL3RuleTcpRstBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpRstBit_Type.__name__ = "Integer32"
_AclL3RuleTcpRstBit_Object = MibTableColumn
aclL3RuleTcpRstBit = _AclL3RuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 15),
    _AclL3RuleTcpRstBit_Type()
)
aclL3RuleTcpRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleTcpRstBit.setStatus("current")


class _AclL3RuleTcpUrgBit_Type(Integer32):
    """Custom type aclL3RuleTcpUrgBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpUrgBit_Type.__name__ = "Integer32"
_AclL3RuleTcpUrgBit_Object = MibTableColumn
aclL3RuleTcpUrgBit = _AclL3RuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 16),
    _AclL3RuleTcpUrgBit_Type()
)
aclL3RuleTcpUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleTcpUrgBit.setStatus("current")


class _AclL3RuleTcpPshBit_Type(Integer32):
    """Custom type aclL3RuleTcpPshBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpPshBit_Type.__name__ = "Integer32"
_AclL3RuleTcpPshBit_Object = MibTableColumn
aclL3RuleTcpPshBit = _AclL3RuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 17),
    _AclL3RuleTcpPshBit_Type()
)
aclL3RuleTcpPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleTcpPshBit.setStatus("current")


class _AclL3RuleTcpSynBit_Type(Integer32):
    """Custom type aclL3RuleTcpSynBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpSynBit_Type.__name__ = "Integer32"
_AclL3RuleTcpSynBit_Object = MibTableColumn
aclL3RuleTcpSynBit = _AclL3RuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 18),
    _AclL3RuleTcpSynBit_Type()
)
aclL3RuleTcpSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleTcpSynBit.setStatus("current")


class _AclL3RuleTcpFinBit_Type(Integer32):
    """Custom type aclL3RuleTcpFinBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpFinBit_Type.__name__ = "Integer32"
_AclL3RuleTcpFinBit_Object = MibTableColumn
aclL3RuleTcpFinBit = _AclL3RuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 19),
    _AclL3RuleTcpFinBit_Type()
)
aclL3RuleTcpFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleTcpFinBit.setStatus("current")


class _AclL3RuleDscp_Type(Integer32):
    """Custom type aclL3RuleDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL3RuleDscp_Type.__name__ = "Integer32"
_AclL3RuleDscp_Object = MibTableColumn
aclL3RuleDscp = _AclL3RuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 20),
    _AclL3RuleDscp_Type()
)
aclL3RuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleDscp.setStatus("current")


class _AclL3RuleIgmpType_Type(Integer32):
    """Custom type aclL3RuleIgmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3RuleIgmpType_Type.__name__ = "Integer32"
_AclL3RuleIgmpType_Object = MibTableColumn
aclL3RuleIgmpType = _AclL3RuleIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 21),
    _AclL3RuleIgmpType_Type()
)
aclL3RuleIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleIgmpType.setStatus("current")
_AclL3RulePortList_Type = PortList
_AclL3RulePortList_Object = MibTableColumn
aclL3RulePortList = _AclL3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 22),
    _AclL3RulePortList_Type()
)
aclL3RulePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RulePortList.setStatus("current")


class _AclL3RuleAction_Type(Integer32):
    """Custom type aclL3RuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_AclL3RuleAction_Type.__name__ = "Integer32"
_AclL3RuleAction_Object = MibTableColumn
aclL3RuleAction = _AclL3RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 23),
    _AclL3RuleAction_Type()
)
aclL3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleAction.setStatus("current")
_AclL3RuleStatus_Type = RowStatus
_AclL3RuleStatus_Object = MibTableColumn
aclL3RuleStatus = _AclL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 1, 1, 25),
    _AclL3RuleStatus_Type()
)
aclL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleStatus.setStatus("current")
_Aclv6L3RuleTable_Object = MibTable
aclv6L3RuleTable = _Aclv6L3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2)
)
if mibBuilder.loadTexts:
    aclv6L3RuleTable.setStatus("current")
_Aclv6L3RuleEntry_Object = MibTableRow
aclv6L3RuleEntry = _Aclv6L3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1)
)
aclv6L3RuleEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "aclv6L3RuleAccessID"),
    (0, "DGS-1210-20_BX", "aclv6L3RuleProfileNo"),
)
if mibBuilder.loadTexts:
    aclv6L3RuleEntry.setStatus("current")


class _Aclv6L3RuleAccessID_Type(Integer32):
    """Custom type aclv6L3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Aclv6L3RuleAccessID_Type.__name__ = "Integer32"
_Aclv6L3RuleAccessID_Object = MibTableColumn
aclv6L3RuleAccessID = _Aclv6L3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 1),
    _Aclv6L3RuleAccessID_Type()
)
aclv6L3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleAccessID.setStatus("current")


class _Aclv6L3RuleProfileNo_Type(Integer32):
    """Custom type aclv6L3RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Aclv6L3RuleProfileNo_Type.__name__ = "Integer32"
_Aclv6L3RuleProfileNo_Object = MibTableColumn
aclv6L3RuleProfileNo = _Aclv6L3RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 2),
    _Aclv6L3RuleProfileNo_Type()
)
aclv6L3RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleProfileNo.setStatus("current")


class _Aclv6L3RuleProtocol_Type(Integer32):
    """Custom type aclv6L3RuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_Aclv6L3RuleProtocol_Type.__name__ = "Integer32"
_Aclv6L3RuleProtocol_Object = MibTableColumn
aclv6L3RuleProtocol = _Aclv6L3RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 3),
    _Aclv6L3RuleProtocol_Type()
)
aclv6L3RuleProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleProtocol.setStatus("current")


class _Aclv6L3RuleICMPMessageType_Type(Integer32):
    """Custom type aclv6L3RuleICMPMessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Aclv6L3RuleICMPMessageType_Type.__name__ = "Integer32"
_Aclv6L3RuleICMPMessageType_Object = MibTableColumn
aclv6L3RuleICMPMessageType = _Aclv6L3RuleICMPMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 4),
    _Aclv6L3RuleICMPMessageType_Type()
)
aclv6L3RuleICMPMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleICMPMessageType.setStatus("current")


class _Aclv6L3RuleICMPMessageCode_Type(Integer32):
    """Custom type aclv6L3RuleICMPMessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Aclv6L3RuleICMPMessageCode_Type.__name__ = "Integer32"
_Aclv6L3RuleICMPMessageCode_Object = MibTableColumn
aclv6L3RuleICMPMessageCode = _Aclv6L3RuleICMPMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 5),
    _Aclv6L3RuleICMPMessageCode_Type()
)
aclv6L3RuleICMPMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleICMPMessageCode.setStatus("current")


class _Aclv6L3RuleDstIpAddr_Type(Ipv6Address):
    """Custom type aclv6L3RuleDstIpAddr based on Ipv6Address"""
    defaultHexValue = "00000000"


_Aclv6L3RuleDstIpAddr_Object = MibTableColumn
aclv6L3RuleDstIpAddr = _Aclv6L3RuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 6),
    _Aclv6L3RuleDstIpAddr_Type()
)
aclv6L3RuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleDstIpAddr.setStatus("current")


class _Aclv6L3RuleSrcIpAddr_Type(Ipv6Address):
    """Custom type aclv6L3RuleSrcIpAddr based on Ipv6Address"""
    defaultHexValue = "00000000"


_Aclv6L3RuleSrcIpAddr_Object = MibTableColumn
aclv6L3RuleSrcIpAddr = _Aclv6L3RuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 7),
    _Aclv6L3RuleSrcIpAddr_Type()
)
aclv6L3RuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleSrcIpAddr.setStatus("current")


class _Aclv6L3RuleDstIpAddrMask_Type(Ipv6Address):
    """Custom type aclv6L3RuleDstIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_Aclv6L3RuleDstIpAddrMask_Object = MibTableColumn
aclv6L3RuleDstIpAddrMask = _Aclv6L3RuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 8),
    _Aclv6L3RuleDstIpAddrMask_Type()
)
aclv6L3RuleDstIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleDstIpAddrMask.setStatus("current")


class _Aclv6L3RuleSrcIpAddrMask_Type(Ipv6Address):
    """Custom type aclv6L3RuleSrcIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_Aclv6L3RuleSrcIpAddrMask_Object = MibTableColumn
aclv6L3RuleSrcIpAddrMask = _Aclv6L3RuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 9),
    _Aclv6L3RuleSrcIpAddrMask_Type()
)
aclv6L3RuleSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleSrcIpAddrMask.setStatus("current")


class _Aclv6L3RuleTcpUdpDstPort_Type(Integer32):
    """Custom type aclv6L3RuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_Aclv6L3RuleTcpUdpDstPort_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpUdpDstPort_Object = MibTableColumn
aclv6L3RuleTcpUdpDstPort = _Aclv6L3RuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 10),
    _Aclv6L3RuleTcpUdpDstPort_Type()
)
aclv6L3RuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpUdpDstPort.setStatus("current")


class _Aclv6L3RuleTcpUdpSrcPort_Type(Integer32):
    """Custom type aclv6L3RuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_Aclv6L3RuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpUdpSrcPort_Object = MibTableColumn
aclv6L3RuleTcpUdpSrcPort = _Aclv6L3RuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 11),
    _Aclv6L3RuleTcpUdpSrcPort_Type()
)
aclv6L3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpUdpSrcPort.setStatus("current")
_Aclv6L3RuleTcpUdpDstPortMask_Type = OctetString
_Aclv6L3RuleTcpUdpDstPortMask_Object = MibTableColumn
aclv6L3RuleTcpUdpDstPortMask = _Aclv6L3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 12),
    _Aclv6L3RuleTcpUdpDstPortMask_Type()
)
aclv6L3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpUdpDstPortMask.setStatus("current")
_Aclv6L3RuleTcpUdpSrcPortMask_Type = OctetString
_Aclv6L3RuleTcpUdpSrcPortMask_Object = MibTableColumn
aclv6L3RuleTcpUdpSrcPortMask = _Aclv6L3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 13),
    _Aclv6L3RuleTcpUdpSrcPortMask_Type()
)
aclv6L3RuleTcpUdpSrcPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpUdpSrcPortMask.setStatus("current")


class _Aclv6L3RuleTcpAckBit_Type(Integer32):
    """Custom type aclv6L3RuleTcpAckBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpAckBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpAckBit_Object = MibTableColumn
aclv6L3RuleTcpAckBit = _Aclv6L3RuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 14),
    _Aclv6L3RuleTcpAckBit_Type()
)
aclv6L3RuleTcpAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpAckBit.setStatus("current")


class _Aclv6L3RuleTcpRstBit_Type(Integer32):
    """Custom type aclv6L3RuleTcpRstBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpRstBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpRstBit_Object = MibTableColumn
aclv6L3RuleTcpRstBit = _Aclv6L3RuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 15),
    _Aclv6L3RuleTcpRstBit_Type()
)
aclv6L3RuleTcpRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpRstBit.setStatus("current")


class _Aclv6L3RuleTcpUrgBit_Type(Integer32):
    """Custom type aclv6L3RuleTcpUrgBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpUrgBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpUrgBit_Object = MibTableColumn
aclv6L3RuleTcpUrgBit = _Aclv6L3RuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 16),
    _Aclv6L3RuleTcpUrgBit_Type()
)
aclv6L3RuleTcpUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpUrgBit.setStatus("current")


class _Aclv6L3RuleTcpPshBit_Type(Integer32):
    """Custom type aclv6L3RuleTcpPshBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpPshBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpPshBit_Object = MibTableColumn
aclv6L3RuleTcpPshBit = _Aclv6L3RuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 17),
    _Aclv6L3RuleTcpPshBit_Type()
)
aclv6L3RuleTcpPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpPshBit.setStatus("current")


class _Aclv6L3RuleTcpSynBit_Type(Integer32):
    """Custom type aclv6L3RuleTcpSynBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpSynBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpSynBit_Object = MibTableColumn
aclv6L3RuleTcpSynBit = _Aclv6L3RuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 18),
    _Aclv6L3RuleTcpSynBit_Type()
)
aclv6L3RuleTcpSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpSynBit.setStatus("current")


class _Aclv6L3RuleTcpFinBit_Type(Integer32):
    """Custom type aclv6L3RuleTcpFinBit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont_care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpFinBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpFinBit_Object = MibTableColumn
aclv6L3RuleTcpFinBit = _Aclv6L3RuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 19),
    _Aclv6L3RuleTcpFinBit_Type()
)
aclv6L3RuleTcpFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpFinBit.setStatus("current")


class _Aclv6L3RuleTrafficClass_Type(Integer32):
    """Custom type aclv6L3RuleTrafficClass based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_Aclv6L3RuleTrafficClass_Type.__name__ = "Integer32"
_Aclv6L3RuleTrafficClass_Object = MibTableColumn
aclv6L3RuleTrafficClass = _Aclv6L3RuleTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 20),
    _Aclv6L3RuleTrafficClass_Type()
)
aclv6L3RuleTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTrafficClass.setStatus("current")
_Aclv6L3RulePortList_Type = PortList
_Aclv6L3RulePortList_Object = MibTableColumn
aclv6L3RulePortList = _Aclv6L3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 21),
    _Aclv6L3RulePortList_Type()
)
aclv6L3RulePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RulePortList.setStatus("current")


class _Aclv6L3RuleAction_Type(Integer32):
    """Custom type aclv6L3RuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_Aclv6L3RuleAction_Type.__name__ = "Integer32"
_Aclv6L3RuleAction_Object = MibTableColumn
aclv6L3RuleAction = _Aclv6L3RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 22),
    _Aclv6L3RuleAction_Type()
)
aclv6L3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleAction.setStatus("current")
_Aclv6L3RuleStatus_Type = RowStatus
_Aclv6L3RuleStatus_Object = MibTableColumn
aclv6L3RuleStatus = _Aclv6L3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 15, 3, 2, 1, 24),
    _Aclv6L3RuleStatus_Type()
)
aclv6L3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleStatus.setStatus("current")
_CompanySyslog_ObjectIdentity = ObjectIdentity
companySyslog = _CompanySyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16)
)
_Ipv4syslogGeneralGroup_ObjectIdentity = ObjectIdentity
ipv4syslogGeneralGroup = _Ipv4syslogGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 1)
)
_Ipv4syslogLogSrvAddr_Type = IpAddress
_Ipv4syslogLogSrvAddr_Object = MibScalar
ipv4syslogLogSrvAddr = _Ipv4syslogLogSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 1, 1),
    _Ipv4syslogLogSrvAddr_Type()
)
ipv4syslogLogSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4syslogLogSrvAddr.setStatus("obsolete")


class _Ipv4syslogUDPPort_Type(Integer32):
    """Custom type ipv4syslogUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ipv4syslogUDPPort_Type.__name__ = "Integer32"
_Ipv4syslogUDPPort_Object = MibScalar
ipv4syslogUDPPort = _Ipv4syslogUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 1, 2),
    _Ipv4syslogUDPPort_Type()
)
ipv4syslogUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4syslogUDPPort.setStatus("obsolete")


class _Ipv4syslogTimeStamp_Type(Integer32):
    """Custom type ipv4syslogTimeStamp based on Integer32"""
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


_Ipv4syslogTimeStamp_Type.__name__ = "Integer32"
_Ipv4syslogTimeStamp_Object = MibScalar
ipv4syslogTimeStamp = _Ipv4syslogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 1, 3),
    _Ipv4syslogTimeStamp_Type()
)
ipv4syslogTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4syslogTimeStamp.setStatus("obsolete")


class _Ipv4syslogSeverity_Type(Integer32):
    """Custom type ipv4syslogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 7),
          ("info", 6),
          ("warning", 4))
    )


_Ipv4syslogSeverity_Type.__name__ = "Integer32"
_Ipv4syslogSeverity_Object = MibScalar
ipv4syslogSeverity = _Ipv4syslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 1, 4),
    _Ipv4syslogSeverity_Type()
)
ipv4syslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4syslogSeverity.setStatus("obsolete")


class _Ipv4syslogFacility_Type(Integer32):
    """Custom type ipv4syslogFacility based on Integer32"""
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


_Ipv4syslogFacility_Type.__name__ = "Integer32"
_Ipv4syslogFacility_Object = MibScalar
ipv4syslogFacility = _Ipv4syslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 1, 5),
    _Ipv4syslogFacility_Type()
)
ipv4syslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4syslogFacility.setStatus("obsolete")


class _Ipv4syslogLogging_Type(Integer32):
    """Custom type ipv4syslogLogging based on Integer32"""
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


_Ipv4syslogLogging_Type.__name__ = "Integer32"
_Ipv4syslogLogging_Object = MibScalar
ipv4syslogLogging = _Ipv4syslogLogging_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 1, 6),
    _Ipv4syslogLogging_Type()
)
ipv4syslogLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4syslogLogging.setStatus("obsolete")
_SyslogGeneralGroup_ObjectIdentity = ObjectIdentity
syslogGeneralGroup = _SyslogGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2)
)


class _SyslogState_Type(Integer32):
    """Custom type syslogState based on Integer32"""
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


_SyslogState_Type.__name__ = "Integer32"
_SyslogState_Object = MibScalar
syslogState = _SyslogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 1),
    _SyslogState_Type()
)
syslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogState.setStatus("current")


class _SyslogTimeStampOption_Type(Integer32):
    """Custom type syslogTimeStampOption based on Integer32"""
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


_SyslogTimeStampOption_Type.__name__ = "Integer32"
_SyslogTimeStampOption_Object = MibScalar
syslogTimeStampOption = _SyslogTimeStampOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 2),
    _SyslogTimeStampOption_Type()
)
syslogTimeStampOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogTimeStampOption.setStatus("current")


class _SyslogSrvSeverity_Type(Integer32):
    """Custom type syslogSrvSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 7),
          ("info", 6),
          ("warning", 4))
    )


_SyslogSrvSeverity_Type.__name__ = "Integer32"
_SyslogSrvSeverity_Object = MibScalar
syslogSrvSeverity = _SyslogSrvSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 3),
    _SyslogSrvSeverity_Type()
)
syslogSrvSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSrvSeverity.setStatus("current")


class _SyslogSrvFacility_Type(Integer32):
    """Custom type syslogSrvFacility based on Integer32"""
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


_SyslogSrvFacility_Type.__name__ = "Integer32"
_SyslogSrvFacility_Object = MibScalar
syslogSrvFacility = _SyslogSrvFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 4),
    _SyslogSrvFacility_Type()
)
syslogSrvFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSrvFacility.setStatus("current")
_SyslogSrvTable_Object = MibTable
syslogSrvTable = _SyslogSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 5)
)
if mibBuilder.loadTexts:
    syslogSrvTable.setStatus("current")
_SyslogSrvEntry_Object = MibTableRow
syslogSrvEntry = _SyslogSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 5, 1)
)
syslogSrvEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "syslogSrvIPType"),
    (0, "DGS-1210-20_BX", "syslogSrvIP"),
)
if mibBuilder.loadTexts:
    syslogSrvEntry.setStatus("current")


class _SyslogSrvIPType_Type(Integer32):
    """Custom type syslogSrvIPType based on Integer32"""
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


_SyslogSrvIPType_Type.__name__ = "Integer32"
_SyslogSrvIPType_Object = MibTableColumn
syslogSrvIPType = _SyslogSrvIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 5, 1, 1),
    _SyslogSrvIPType_Type()
)
syslogSrvIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogSrvIPType.setStatus("current")
_SyslogSrvIP_Type = Ipv6Address
_SyslogSrvIP_Object = MibTableColumn
syslogSrvIP = _SyslogSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 5, 1, 2),
    _SyslogSrvIP_Type()
)
syslogSrvIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogSrvIP.setStatus("current")


class _SyslogSrvPort_Type(Integer32):
    """Custom type syslogSrvPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyslogSrvPort_Type.__name__ = "Integer32"
_SyslogSrvPort_Object = MibTableColumn
syslogSrvPort = _SyslogSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 5, 1, 3),
    _SyslogSrvPort_Type()
)
syslogSrvPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogSrvPort.setStatus("current")
_SyslogInterfaceName_Type = OctetString
_SyslogInterfaceName_Object = MibTableColumn
syslogInterfaceName = _SyslogInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 5, 1, 4),
    _SyslogInterfaceName_Type()
)
syslogInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogInterfaceName.setStatus("current")
_SyslogSrvRowStatus_Type = RowStatus
_SyslogSrvRowStatus_Object = MibTableColumn
syslogSrvRowStatus = _SyslogSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 16, 2, 5, 1, 5),
    _SyslogSrvRowStatus_Type()
)
syslogSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogSrvRowStatus.setStatus("current")
_CompanyLBD_ObjectIdentity = ObjectIdentity
companyLBD = _CompanyLBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 4),
    _SysLBDRecoverTime_Type()
)
sysLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDRecoverTime.setStatus("current")
_SysLBDCtrlTable_Object = MibTable
sysLBDCtrlTable = _SysLBDCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 5)
)
if mibBuilder.loadTexts:
    sysLBDCtrlTable.setStatus("current")
_SysLBDCtrlEntry_Object = MibTableRow
sysLBDCtrlEntry = _SysLBDCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 5, 1)
)
sysLBDCtrlEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "sysLBDCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysLBDCtrlEntry.setStatus("current")
_SysLBDCtrlIndex_Type = Integer32
_SysLBDCtrlIndex_Object = MibTableColumn
sysLBDCtrlIndex = _SysLBDCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 5, 1, 2),
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
        *(("disabled", 2),
          ("normal", 1))
    )


_SysLBDPortLoopStatus_Type.__name__ = "Integer32"
_SysLBDPortLoopStatus_Object = MibTableColumn
sysLBDPortLoopStatus = _SysLBDPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 5, 1, 3),
    _SysLBDPortLoopStatus_Type()
)
sysLBDPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDPortLoopStatus.setStatus("current")
_SysLBDVlanLoopTable_Object = MibTable
sysLBDVlanLoopTable = _SysLBDVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 6)
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopTable.setStatus("current")
_SysLBDVlanLoopEntry_Object = MibTableRow
sysLBDVlanLoopEntry = _SysLBDVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 6, 1)
)
sysLBDVlanLoopEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "sysLBDVlanLoopIndex"),
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopEntry.setStatus("current")
_SysLBDVlanLoopIndex_Type = Integer32
_SysLBDVlanLoopIndex_Object = MibTableColumn
sysLBDVlanLoopIndex = _SysLBDVlanLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 6, 1, 1),
    _SysLBDVlanLoopIndex_Type()
)
sysLBDVlanLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopIndex.setStatus("current")
_SysLBDVlanLoopPorts_Type = PortList
_SysLBDVlanLoopPorts_Object = MibTableColumn
sysLBDVlanLoopPorts = _SysLBDVlanLoopPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 17, 6, 1, 2),
    _SysLBDVlanLoopPorts_Type()
)
sysLBDVlanLoopPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopPorts.setStatus("current")
_CompanyMirror_ObjectIdentity = ObjectIdentity
companyMirror = _CompanyMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 18)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 18, 1),
    _SysMirrorStatus_Type()
)
sysMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorStatus.setStatus("current")
_SysMirrorTargetPort_Type = Integer32
_SysMirrorTargetPort_Object = MibScalar
sysMirrorTargetPort = _SysMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 18, 2),
    _SysMirrorTargetPort_Type()
)
sysMirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorTargetPort.setStatus("current")
_SysMirrorCtrlIngressMirroring_Type = PortList
_SysMirrorCtrlIngressMirroring_Object = MibScalar
sysMirrorCtrlIngressMirroring = _SysMirrorCtrlIngressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 18, 3),
    _SysMirrorCtrlIngressMirroring_Type()
)
sysMirrorCtrlIngressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlIngressMirroring.setStatus("current")
_SysMirrorCtrlEgressMirroring_Type = PortList
_SysMirrorCtrlEgressMirroring_Object = MibScalar
sysMirrorCtrlEgressMirroring = _SysMirrorCtrlEgressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 18, 4),
    _SysMirrorCtrlEgressMirroring_Type()
)
sysMirrorCtrlEgressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlEgressMirroring.setStatus("current")
_CompanyTrapSetting_ObjectIdentity = ObjectIdentity
companyTrapSetting = _CompanyTrapSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 19)
)
_SysTrapIP_Type = IpAddress
_SysTrapIP_Object = MibScalar
sysTrapIP = _SysTrapIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 19, 1),
    _SysTrapIP_Type()
)
sysTrapIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapIP.setStatus("current")


class _SysTrapSystemEvent_Type(Integer32):
    """Custom type sysTrapSystemEvent based on Integer32"""
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
        *(("both", 3),
          ("deviceBootUp", 1),
          ("illegalLogin", 2),
          ("none", 0))
    )


_SysTrapSystemEvent_Type.__name__ = "Integer32"
_SysTrapSystemEvent_Object = MibScalar
sysTrapSystemEvent = _SysTrapSystemEvent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 19, 2),
    _SysTrapSystemEvent_Type()
)
sysTrapSystemEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapSystemEvent.setStatus("current")


class _SysTrapPortEvent_Type(Integer32):
    """Custom type sysTrapPortEvent based on Integer32"""
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


_SysTrapPortEvent_Type.__name__ = "Integer32"
_SysTrapPortEvent_Object = MibScalar
sysTrapPortEvent = _SysTrapPortEvent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 19, 3),
    _SysTrapPortEvent_Type()
)
sysTrapPortEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPortEvent.setStatus("current")


class _SysTrapStateChangeEvent_Type(Integer32):
    """Custom type sysTrapStateChangeEvent based on Integer32"""
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


_SysTrapStateChangeEvent_Type.__name__ = "Integer32"
_SysTrapStateChangeEvent_Object = MibScalar
sysTrapStateChangeEvent = _SysTrapStateChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 19, 4),
    _SysTrapStateChangeEvent_Type()
)
sysTrapStateChangeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapStateChangeEvent.setStatus("current")


class _SysTrapFirmUpgradeEvent_Type(Integer32):
    """Custom type sysTrapFirmUpgradeEvent based on Integer32"""
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


_SysTrapFirmUpgradeEvent_Type.__name__ = "Integer32"
_SysTrapFirmUpgradeEvent_Object = MibScalar
sysTrapFirmUpgradeEvent = _SysTrapFirmUpgradeEvent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 19, 5),
    _SysTrapFirmUpgradeEvent_Type()
)
sysTrapFirmUpgradeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapFirmUpgradeEvent.setStatus("current")


class _SysTrapStatus_Type(Integer32):
    """Custom type sysTrapStatus based on Integer32"""
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


_SysTrapStatus_Type.__name__ = "Integer32"
_SysTrapStatus_Object = MibScalar
sysTrapStatus = _SysTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 19, 11),
    _SysTrapStatus_Type()
)
sysTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapStatus.setStatus("current")
_CompanySNTPSetting_ObjectIdentity = ObjectIdentity
companySNTPSetting = _CompanySNTPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20)
)
_Ipv4sysSNTPTimeSeconds_Type = Integer32
_Ipv4sysSNTPTimeSeconds_Object = MibScalar
ipv4sysSNTPTimeSeconds = _Ipv4sysSNTPTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 1),
    _Ipv4sysSNTPTimeSeconds_Type()
)
ipv4sysSNTPTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPTimeSeconds.setStatus("obsolete")
_Ipv4sysSNTPFirstServer_Type = IpAddress
_Ipv4sysSNTPFirstServer_Object = MibScalar
ipv4sysSNTPFirstServer = _Ipv4sysSNTPFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 2),
    _Ipv4sysSNTPFirstServer_Type()
)
ipv4sysSNTPFirstServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPFirstServer.setStatus("obsolete")
_Ipv4sysSNTPSecondServer_Type = IpAddress
_Ipv4sysSNTPSecondServer_Object = MibScalar
ipv4sysSNTPSecondServer = _Ipv4sysSNTPSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 3),
    _Ipv4sysSNTPSecondServer_Type()
)
ipv4sysSNTPSecondServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPSecondServer.setStatus("obsolete")
_Ipv4sysSNTPPollInterval_Type = Integer32
_Ipv4sysSNTPPollInterval_Object = MibScalar
ipv4sysSNTPPollInterval = _Ipv4sysSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 4),
    _Ipv4sysSNTPPollInterval_Type()
)
ipv4sysSNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPPollInterval.setStatus("obsolete")


class _Ipv4sysSNTPState_Type(Integer32):
    """Custom type ipv4sysSNTPState based on Integer32"""
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


_Ipv4sysSNTPState_Type.__name__ = "Integer32"
_Ipv4sysSNTPState_Object = MibScalar
ipv4sysSNTPState = _Ipv4sysSNTPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 5),
    _Ipv4sysSNTPState_Type()
)
ipv4sysSNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPState.setStatus("obsolete")


class _Ipv4sysSNTPDSTOffset_Type(Integer32):
    """Custom type ipv4sysSNTPDSTOffset based on Integer32"""
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


_Ipv4sysSNTPDSTOffset_Type.__name__ = "Integer32"
_Ipv4sysSNTPDSTOffset_Object = MibScalar
ipv4sysSNTPDSTOffset = _Ipv4sysSNTPDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 6),
    _Ipv4sysSNTPDSTOffset_Type()
)
ipv4sysSNTPDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTOffset.setStatus("obsolete")
_Ipv4sysSNTPGMTMinutes_Type = Integer32
_Ipv4sysSNTPGMTMinutes_Object = MibScalar
ipv4sysSNTPGMTMinutes = _Ipv4sysSNTPGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 7),
    _Ipv4sysSNTPGMTMinutes_Type()
)
ipv4sysSNTPGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPGMTMinutes.setStatus("obsolete")
_Ipv4sysSNTPDSTStartMon_Type = Integer32
_Ipv4sysSNTPDSTStartMon_Object = MibScalar
ipv4sysSNTPDSTStartMon = _Ipv4sysSNTPDSTStartMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 8),
    _Ipv4sysSNTPDSTStartMon_Type()
)
ipv4sysSNTPDSTStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTStartMon.setStatus("obsolete")
_Ipv4sysSNTPDSTStartDay_Type = Integer32
_Ipv4sysSNTPDSTStartDay_Object = MibScalar
ipv4sysSNTPDSTStartDay = _Ipv4sysSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 9),
    _Ipv4sysSNTPDSTStartDay_Type()
)
ipv4sysSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTStartDay.setStatus("obsolete")
_Ipv4sysSNTPDSTStartHour_Type = Integer32
_Ipv4sysSNTPDSTStartHour_Object = MibScalar
ipv4sysSNTPDSTStartHour = _Ipv4sysSNTPDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 10),
    _Ipv4sysSNTPDSTStartHour_Type()
)
ipv4sysSNTPDSTStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTStartHour.setStatus("obsolete")
_Ipv4sysSNTPDSTStartMin_Type = Integer32
_Ipv4sysSNTPDSTStartMin_Object = MibScalar
ipv4sysSNTPDSTStartMin = _Ipv4sysSNTPDSTStartMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 11),
    _Ipv4sysSNTPDSTStartMin_Type()
)
ipv4sysSNTPDSTStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTStartMin.setStatus("obsolete")
_Ipv4sysSNTPDSTEndMon_Type = Integer32
_Ipv4sysSNTPDSTEndMon_Object = MibScalar
ipv4sysSNTPDSTEndMon = _Ipv4sysSNTPDSTEndMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 12),
    _Ipv4sysSNTPDSTEndMon_Type()
)
ipv4sysSNTPDSTEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTEndMon.setStatus("obsolete")
_Ipv4sysSNTPDSTEndDay_Type = Integer32
_Ipv4sysSNTPDSTEndDay_Object = MibScalar
ipv4sysSNTPDSTEndDay = _Ipv4sysSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 13),
    _Ipv4sysSNTPDSTEndDay_Type()
)
ipv4sysSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTEndDay.setStatus("obsolete")
_Ipv4sysSNTPDSTEndHour_Type = Integer32
_Ipv4sysSNTPDSTEndHour_Object = MibScalar
ipv4sysSNTPDSTEndHour = _Ipv4sysSNTPDSTEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 14),
    _Ipv4sysSNTPDSTEndHour_Type()
)
ipv4sysSNTPDSTEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTEndHour.setStatus("obsolete")
_Ipv4sysSNTPDSTEndMin_Type = Integer32
_Ipv4sysSNTPDSTEndMin_Object = MibScalar
ipv4sysSNTPDSTEndMin = _Ipv4sysSNTPDSTEndMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 15),
    _Ipv4sysSNTPDSTEndMin_Type()
)
ipv4sysSNTPDSTEndMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTEndMin.setStatus("obsolete")


class _Ipv4sysSNTPDSTState_Type(Integer32):
    """Custom type ipv4sysSNTPDSTState based on Integer32"""
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


_Ipv4sysSNTPDSTState_Type.__name__ = "Integer32"
_Ipv4sysSNTPDSTState_Object = MibScalar
ipv4sysSNTPDSTState = _Ipv4sysSNTPDSTState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 16),
    _Ipv4sysSNTPDSTState_Type()
)
ipv4sysSNTPDSTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4sysSNTPDSTState.setStatus("obsolete")
_SysSNTPServerTable_ObjectIdentity = ObjectIdentity
sysSNTPServerTable = _SysSNTPServerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17)
)
_SysSNTPTimeSeconds_Type = Integer32
_SysSNTPTimeSeconds_Object = MibScalar
sysSNTPTimeSeconds = _SysSNTPTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 1),
    _SysSNTPTimeSeconds_Type()
)
sysSNTPTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPTimeSeconds.setStatus("current")
_SysSNTPFirstServer_Type = Ipv6Address
_SysSNTPFirstServer_Object = MibScalar
sysSNTPFirstServer = _SysSNTPFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 2),
    _SysSNTPFirstServer_Type()
)
sysSNTPFirstServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstServer.setStatus("current")


class _SysSNTPFirstType_Type(Integer32):
    """Custom type sysSNTPFirstType based on Integer32"""
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


_SysSNTPFirstType_Type.__name__ = "Integer32"
_SysSNTPFirstType_Object = MibScalar
sysSNTPFirstType = _SysSNTPFirstType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 3),
    _SysSNTPFirstType_Type()
)
sysSNTPFirstType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstType.setStatus("current")
_SysSNTPFirstInterfaceName_Type = OctetString
_SysSNTPFirstInterfaceName_Object = MibScalar
sysSNTPFirstInterfaceName = _SysSNTPFirstInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 4),
    _SysSNTPFirstInterfaceName_Type()
)
sysSNTPFirstInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstInterfaceName.setStatus("current")
_SysSNTPSecondServer_Type = Ipv6Address
_SysSNTPSecondServer_Object = MibScalar
sysSNTPSecondServer = _SysSNTPSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 5),
    _SysSNTPSecondServer_Type()
)
sysSNTPSecondServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondServer.setStatus("current")


class _SysSNTPSecondType_Type(Integer32):
    """Custom type sysSNTPSecondType based on Integer32"""
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


_SysSNTPSecondType_Type.__name__ = "Integer32"
_SysSNTPSecondType_Object = MibScalar
sysSNTPSecondType = _SysSNTPSecondType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 6),
    _SysSNTPSecondType_Type()
)
sysSNTPSecondType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondType.setStatus("current")
_SysSNTPSecondInterfaceName_Type = OctetString
_SysSNTPSecondInterfaceName_Object = MibScalar
sysSNTPSecondInterfaceName = _SysSNTPSecondInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 7),
    _SysSNTPSecondInterfaceName_Type()
)
sysSNTPSecondInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondInterfaceName.setStatus("current")
_SysSNTPPollInterval_Type = Integer32
_SysSNTPPollInterval_Object = MibScalar
sysSNTPPollInterval = _SysSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 8),
    _SysSNTPPollInterval_Type()
)
sysSNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPPollInterval.setStatus("current")


class _SysSNTPState_Type(Integer32):
    """Custom type sysSNTPState based on Integer32"""
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


_SysSNTPState_Type.__name__ = "Integer32"
_SysSNTPState_Object = MibScalar
sysSNTPState = _SysSNTPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 9),
    _SysSNTPState_Type()
)
sysSNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPState.setStatus("current")


class _SysSNTPDSTOffset_Type(Integer32):
    """Custom type sysSNTPDSTOffset based on Integer32"""
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


_SysSNTPDSTOffset_Type.__name__ = "Integer32"
_SysSNTPDSTOffset_Object = MibScalar
sysSNTPDSTOffset = _SysSNTPDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 10),
    _SysSNTPDSTOffset_Type()
)
sysSNTPDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTOffset.setStatus("current")
_SysSNTPGMTMinutes_Type = Integer32
_SysSNTPGMTMinutes_Object = MibScalar
sysSNTPGMTMinutes = _SysSNTPGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 11),
    _SysSNTPGMTMinutes_Type()
)
sysSNTPGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPGMTMinutes.setStatus("current")
_SysSNTPDSTStartMon_Type = Integer32
_SysSNTPDSTStartMon_Object = MibScalar
sysSNTPDSTStartMon = _SysSNTPDSTStartMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 12),
    _SysSNTPDSTStartMon_Type()
)
sysSNTPDSTStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMon.setStatus("current")
_SysSNTPDSTStartDay_Type = Integer32
_SysSNTPDSTStartDay_Object = MibScalar
sysSNTPDSTStartDay = _SysSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 13),
    _SysSNTPDSTStartDay_Type()
)
sysSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartDay.setStatus("current")
_SysSNTPDSTStartHour_Type = Integer32
_SysSNTPDSTStartHour_Object = MibScalar
sysSNTPDSTStartHour = _SysSNTPDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 14),
    _SysSNTPDSTStartHour_Type()
)
sysSNTPDSTStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartHour.setStatus("current")
_SysSNTPDSTStartMin_Type = Integer32
_SysSNTPDSTStartMin_Object = MibScalar
sysSNTPDSTStartMin = _SysSNTPDSTStartMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 15),
    _SysSNTPDSTStartMin_Type()
)
sysSNTPDSTStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMin.setStatus("current")
_SysSNTPDSTEndMon_Type = Integer32
_SysSNTPDSTEndMon_Object = MibScalar
sysSNTPDSTEndMon = _SysSNTPDSTEndMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 16),
    _SysSNTPDSTEndMon_Type()
)
sysSNTPDSTEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndMon.setStatus("current")
_SysSNTPDSTEndDay_Type = Integer32
_SysSNTPDSTEndDay_Object = MibScalar
sysSNTPDSTEndDay = _SysSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 17),
    _SysSNTPDSTEndDay_Type()
)
sysSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndDay.setStatus("current")
_SysSNTPDSTEndHour_Type = Integer32
_SysSNTPDSTEndHour_Object = MibScalar
sysSNTPDSTEndHour = _SysSNTPDSTEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 18),
    _SysSNTPDSTEndHour_Type()
)
sysSNTPDSTEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndHour.setStatus("current")
_SysSNTPDSTEndMin_Type = Integer32
_SysSNTPDSTEndMin_Object = MibScalar
sysSNTPDSTEndMin = _SysSNTPDSTEndMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 19),
    _SysSNTPDSTEndMin_Type()
)
sysSNTPDSTEndMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndMin.setStatus("current")


class _SysSNTPDSTState_Type(Integer32):
    """Custom type sysSNTPDSTState based on Integer32"""
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


_SysSNTPDSTState_Type.__name__ = "Integer32"
_SysSNTPDSTState_Object = MibScalar
sysSNTPDSTState = _SysSNTPDSTState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 20, 17, 20),
    _SysSNTPDSTState_Type()
)
sysSNTPDSTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTState.setStatus("current")
_CompanyVoiceVlan_ObjectIdentity = ObjectIdentity
companyVoiceVlan = _CompanyVoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21)
)
_VoicevlanSystem_ObjectIdentity = ObjectIdentity
voicevlanSystem = _VoicevlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1)
)


class _VoiceVlanMode_Type(Integer32):
    """Custom type voiceVlanMode based on Integer32"""
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


_VoiceVlanMode_Type.__name__ = "Integer32"
_VoiceVlanMode_Object = MibScalar
voiceVlanMode = _VoiceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 2),
    _VoiceVlanMode_Type()
)
voiceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanMode.setStatus("current")
_VoiceVlanId_Type = Integer32
_VoiceVlanId_Object = MibScalar
voiceVlanId = _VoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 3),
    _VoiceVlanId_Type()
)
voiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanId.setStatus("current")
_VoiceVlanTimeout_Type = Integer32
_VoiceVlanTimeout_Object = MibScalar
voiceVlanTimeout = _VoiceVlanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 4),
    _VoiceVlanTimeout_Type()
)
voiceVlanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanTimeout.setStatus("current")


class _VoiceVlanPriority_Type(Integer32):
    """Custom type voiceVlanPriority based on Integer32"""
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
        *(("high", 1),
          ("highest", 0),
          ("low", 3),
          ("medium", 2))
    )


_VoiceVlanPriority_Type.__name__ = "Integer32"
_VoiceVlanPriority_Object = MibScalar
voiceVlanPriority = _VoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 5),
    _VoiceVlanPriority_Type()
)
voiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPriority.setStatus("current")
_VoicevlanPortControlTable_Object = MibTable
voicevlanPortControlTable = _VoicevlanPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 6)
)
if mibBuilder.loadTexts:
    voicevlanPortControlTable.setStatus("current")
_VoicevlanPortControlEntry_Object = MibTableRow
voicevlanPortControlEntry = _VoicevlanPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 6, 1)
)
voicevlanPortControlEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "voicevlanPortControlIndex"),
)
if mibBuilder.loadTexts:
    voicevlanPortControlEntry.setStatus("current")
_VoicevlanPortControlIndex_Type = InterfaceIndex
_VoicevlanPortControlIndex_Object = MibTableColumn
voicevlanPortControlIndex = _VoicevlanPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 6, 1, 1),
    _VoicevlanPortControlIndex_Type()
)
voicevlanPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanPortControlIndex.setStatus("current")


class _VoicevlanPortAutoDetection_Type(Integer32):
    """Custom type voicevlanPortAutoDetection based on Integer32"""
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


_VoicevlanPortAutoDetection_Type.__name__ = "Integer32"
_VoicevlanPortAutoDetection_Object = MibTableColumn
voicevlanPortAutoDetection = _VoicevlanPortAutoDetection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 6, 1, 2),
    _VoicevlanPortAutoDetection_Type()
)
voicevlanPortAutoDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanPortAutoDetection.setStatus("current")


class _VoicevlanPortManuTagMode_Type(Integer32):
    """Custom type voicevlanPortManuTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_VoicevlanPortManuTagMode_Type.__name__ = "Integer32"
_VoicevlanPortManuTagMode_Object = MibTableColumn
voicevlanPortManuTagMode = _VoicevlanPortManuTagMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 6, 1, 3),
    _VoicevlanPortManuTagMode_Type()
)
voicevlanPortManuTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanPortManuTagMode.setStatus("current")


class _VoicevlanPortCurrentTagMode_Type(Integer32):
    """Custom type voicevlanPortCurrentTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("tag", 1),
          ("untag", 2))
    )


_VoicevlanPortCurrentTagMode_Type.__name__ = "Integer32"
_VoicevlanPortCurrentTagMode_Object = MibTableColumn
voicevlanPortCurrentTagMode = _VoicevlanPortCurrentTagMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 6, 1, 4),
    _VoicevlanPortCurrentTagMode_Type()
)
voicevlanPortCurrentTagMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanPortCurrentTagMode.setStatus("current")


class _VoicevlanPortState_Type(Integer32):
    """Custom type voicevlanPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 1),
          ("none", 3))
    )


_VoicevlanPortState_Type.__name__ = "Integer32"
_VoicevlanPortState_Object = MibTableColumn
voicevlanPortState = _VoicevlanPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 1, 6, 1, 5),
    _VoicevlanPortState_Type()
)
voicevlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanPortState.setStatus("current")
_VoicevlanOUI_ObjectIdentity = ObjectIdentity
voicevlanOUI = _VoicevlanOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 2)
)
_VoicevlanOUITable_Object = MibTable
voicevlanOUITable = _VoicevlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 2, 1)
)
if mibBuilder.loadTexts:
    voicevlanOUITable.setStatus("current")
_VoicevlanOUIEntry_Object = MibTableRow
voicevlanOUIEntry = _VoicevlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 2, 1, 1)
)
voicevlanOUIEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "voicevlanOUITelephonyOUI"),
)
if mibBuilder.loadTexts:
    voicevlanOUIEntry.setStatus("current")
_VoicevlanOUITelephonyOUI_Type = MacAddress
_VoicevlanOUITelephonyOUI_Object = MibTableColumn
voicevlanOUITelephonyOUI = _VoicevlanOUITelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 2, 1, 1, 1),
    _VoicevlanOUITelephonyOUI_Type()
)
voicevlanOUITelephonyOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUITelephonyOUI.setStatus("current")
_VoicevlanOUIDescription_Type = OctetString
_VoicevlanOUIDescription_Object = MibTableColumn
voicevlanOUIDescription = _VoicevlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 2, 1, 1, 2),
    _VoicevlanOUIDescription_Type()
)
voicevlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanOUIDescription.setStatus("current")
_VoicevlanOUIMask_Type = MacAddress
_VoicevlanOUIMask_Object = MibTableColumn
voicevlanOUIMask = _VoicevlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 2, 1, 1, 3),
    _VoicevlanOUIMask_Type()
)
voicevlanOUIMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUIMask.setStatus("current")
_VoicevlanOUIStatus_Type = RowStatus
_VoicevlanOUIStatus_Object = MibTableColumn
voicevlanOUIStatus = _VoicevlanOUIStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 2, 1, 1, 4),
    _VoicevlanOUIStatus_Type()
)
voicevlanOUIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanOUIStatus.setStatus("current")
_VoicevlanDevice_ObjectIdentity = ObjectIdentity
voicevlanDevice = _VoicevlanDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3)
)
_VoicevlanDeviceTable_Object = MibTable
voicevlanDeviceTable = _VoicevlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3, 1)
)
if mibBuilder.loadTexts:
    voicevlanDeviceTable.setStatus("current")
_VoicevlanDeviceEntry_Object = MibTableRow
voicevlanDeviceEntry = _VoicevlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3, 1, 1)
)
voicevlanDeviceEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "voicevlanDeviceIndexMac"),
)
if mibBuilder.loadTexts:
    voicevlanDeviceEntry.setStatus("current")
_VoicevlanDeviceIndexMac_Type = MacAddress
_VoicevlanDeviceIndexMac_Object = MibTableColumn
voicevlanDeviceIndexMac = _VoicevlanDeviceIndexMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3, 1, 1, 1),
    _VoicevlanDeviceIndexMac_Type()
)
voicevlanDeviceIndexMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDeviceIndexMac.setStatus("current")
_VoicevlanDevicePort_Type = Integer32
_VoicevlanDevicePort_Object = MibTableColumn
voicevlanDevicePort = _VoicevlanDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3, 1, 1, 2),
    _VoicevlanDevicePort_Type()
)
voicevlanDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDevicePort.setStatus("current")
_VoicevlanDevicePriority_Type = Integer32
_VoicevlanDevicePriority_Object = MibTableColumn
voicevlanDevicePriority = _VoicevlanDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3, 1, 1, 3),
    _VoicevlanDevicePriority_Type()
)
voicevlanDevicePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDevicePriority.setStatus("current")


class _VoicevlanDeviceTagType_Type(Integer32):
    """Custom type voicevlanDeviceTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_VoicevlanDeviceTagType_Type.__name__ = "Integer32"
_VoicevlanDeviceTagType_Object = MibTableColumn
voicevlanDeviceTagType = _VoicevlanDeviceTagType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3, 1, 1, 4),
    _VoicevlanDeviceTagType_Type()
)
voicevlanDeviceTagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDeviceTagType.setStatus("current")


class _VoicevlanDeviceStatus_Type(Integer32):
    """Custom type voicevlanDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_VoicevlanDeviceStatus_Type.__name__ = "Integer32"
_VoicevlanDeviceStatus_Object = MibTableColumn
voicevlanDeviceStatus = _VoicevlanDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 21, 3, 1, 1, 5),
    _VoicevlanDeviceStatus_Type()
)
voicevlanDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanDeviceStatus.setStatus("current")
_CompanyLLDPSetting_ObjectIdentity = ObjectIdentity
companyLLDPSetting = _CompanyLLDPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24)
)


class _DlinklldpState_Type(Integer32):
    """Custom type dlinklldpState based on Integer32"""
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


_DlinklldpState_Type.__name__ = "Integer32"
_DlinklldpState_Object = MibScalar
dlinklldpState = _DlinklldpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 1),
    _DlinklldpState_Type()
)
dlinklldpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpState.setStatus("current")


class _DlinklldpMsgHoldMultiplier_Type(Integer32):
    """Custom type dlinklldpMsgHoldMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_DlinklldpMsgHoldMultiplier_Type.__name__ = "Integer32"
_DlinklldpMsgHoldMultiplier_Object = MibScalar
dlinklldpMsgHoldMultiplier = _DlinklldpMsgHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 2),
    _DlinklldpMsgHoldMultiplier_Type()
)
dlinklldpMsgHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpMsgHoldMultiplier.setStatus("current")


class _DlinklldpMsgTxInterval_Type(Integer32):
    """Custom type dlinklldpMsgTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_DlinklldpMsgTxInterval_Type.__name__ = "Integer32"
_DlinklldpMsgTxInterval_Object = MibScalar
dlinklldpMsgTxInterval = _DlinklldpMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 3),
    _DlinklldpMsgTxInterval_Type()
)
dlinklldpMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpMsgTxInterval.setStatus("current")


class _DlinklldpReinitDelay_Type(Integer32):
    """Custom type dlinklldpReinitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DlinklldpReinitDelay_Type.__name__ = "Integer32"
_DlinklldpReinitDelay_Object = MibScalar
dlinklldpReinitDelay = _DlinklldpReinitDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 4),
    _DlinklldpReinitDelay_Type()
)
dlinklldpReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpReinitDelay.setStatus("current")


class _DlinklldpTxDelay_Type(Integer32):
    """Custom type dlinklldpTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_DlinklldpTxDelay_Type.__name__ = "Integer32"
_DlinklldpTxDelay_Object = MibScalar
dlinklldpTxDelay = _DlinklldpTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 5),
    _DlinklldpTxDelay_Type()
)
dlinklldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpTxDelay.setStatus("current")
_DlinklldpConfigManAddrTable_Object = MibTable
dlinklldpConfigManAddrTable = _DlinklldpConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 7)
)
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrTable.setStatus("current")
_DlinklldpConfigManAddrEntry_Object = MibTableRow
dlinklldpConfigManAddrEntry = _DlinklldpConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 7, 1)
)
dlinklldpConfigManAddrEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "dlinklldpLocManAddrSubtype"),
    (0, "DGS-1210-20_BX", "dlinklldpLocManAddr"),
)
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrEntry.setStatus("current")
_DlinklldpLocManAddrSubtype_Type = AddressFamilyNumbers
_DlinklldpLocManAddrSubtype_Object = MibTableColumn
dlinklldpLocManAddrSubtype = _DlinklldpLocManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 7, 1, 1),
    _DlinklldpLocManAddrSubtype_Type()
)
dlinklldpLocManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlinklldpLocManAddrSubtype.setStatus("current")
_DlinklldpLocManAddr_Type = LldpManAddress
_DlinklldpLocManAddr_Object = MibTableColumn
dlinklldpLocManAddr = _DlinklldpLocManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 7, 1, 2),
    _DlinklldpLocManAddr_Type()
)
dlinklldpLocManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlinklldpLocManAddr.setStatus("current")


class _DlinklldpConfigManAddrPortsTxEnable_Type(PortList):
    """Custom type dlinklldpConfigManAddrPortsTxEnable based on PortList"""
    defaultHexValue = ""


_DlinklldpConfigManAddrPortsTxEnable_Object = MibTableColumn
dlinklldpConfigManAddrPortsTxEnable = _DlinklldpConfigManAddrPortsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 24, 7, 1, 3),
    _DlinklldpConfigManAddrPortsTxEnable_Type()
)
dlinklldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrPortsTxEnable.setStatus("current")
_CompanySNMPV3_ObjectIdentity = ObjectIdentity
companySNMPV3 = _CompanySNMPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25)
)


class _SnmpGlobalState_Type(Integer32):
    """Custom type snmpGlobalState based on Integer32"""
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


_SnmpGlobalState_Type.__name__ = "Integer32"
_SnmpGlobalState_Object = MibScalar
snmpGlobalState = _SnmpGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 1),
    _SnmpGlobalState_Type()
)
snmpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGlobalState.setStatus("current")
_SnmpV3User_ObjectIdentity = ObjectIdentity
snmpV3User = _SnmpV3User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2)
)
_SnmpV3UserTable_Object = MibTable
snmpV3UserTable = _SnmpV3UserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1)
)
if mibBuilder.loadTexts:
    snmpV3UserTable.setStatus("current")
_SnmpV3UserEntry_Object = MibTableRow
snmpV3UserEntry = _SnmpV3UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1)
)
snmpV3UserEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "snmpV3UserName"),
    (0, "DGS-1210-20_BX", "snmpV3UserVersion"),
)
if mibBuilder.loadTexts:
    snmpV3UserEntry.setStatus("current")


class _SnmpV3UserName_Type(SnmpAdminString):
    """Custom type snmpV3UserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3UserName_Type.__name__ = "SnmpAdminString"
_SnmpV3UserName_Object = MibTableColumn
snmpV3UserName = _SnmpV3UserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 1),
    _SnmpV3UserName_Type()
)
snmpV3UserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3UserName.setStatus("current")


class _SnmpV3UserVersion_Type(Integer32):
    """Custom type snmpV3UserVersion based on Integer32"""
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


_SnmpV3UserVersion_Type.__name__ = "Integer32"
_SnmpV3UserVersion_Object = MibTableColumn
snmpV3UserVersion = _SnmpV3UserVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 2),
    _SnmpV3UserVersion_Type()
)
snmpV3UserVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3UserVersion.setStatus("current")


class _SnmpV3UserGroupName_Type(SnmpAdminString):
    """Custom type snmpV3UserGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3UserGroupName_Type.__name__ = "SnmpAdminString"
_SnmpV3UserGroupName_Object = MibTableColumn
snmpV3UserGroupName = _SnmpV3UserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 3),
    _SnmpV3UserGroupName_Type()
)
snmpV3UserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserGroupName.setStatus("current")


class _SnmpV3UserAuthProtocol_Type(Integer32):
    """Custom type snmpV3UserAuthProtocol based on Integer32"""
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


_SnmpV3UserAuthProtocol_Type.__name__ = "Integer32"
_SnmpV3UserAuthProtocol_Object = MibTableColumn
snmpV3UserAuthProtocol = _SnmpV3UserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 4),
    _SnmpV3UserAuthProtocol_Type()
)
snmpV3UserAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserAuthProtocol.setStatus("current")


class _SnmpV3UserAuthProtocolPassword_Type(SnmpAdminString):
    """Custom type snmpV3UserAuthProtocolPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3UserAuthProtocolPassword_Type.__name__ = "SnmpAdminString"
_SnmpV3UserAuthProtocolPassword_Object = MibTableColumn
snmpV3UserAuthProtocolPassword = _SnmpV3UserAuthProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 5),
    _SnmpV3UserAuthProtocolPassword_Type()
)
snmpV3UserAuthProtocolPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserAuthProtocolPassword.setStatus("current")


class _SnmpV3UserPrivProtocol_Type(Integer32):
    """Custom type snmpV3UserPrivProtocol based on Integer32"""
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


_SnmpV3UserPrivProtocol_Type.__name__ = "Integer32"
_SnmpV3UserPrivProtocol_Object = MibTableColumn
snmpV3UserPrivProtocol = _SnmpV3UserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 6),
    _SnmpV3UserPrivProtocol_Type()
)
snmpV3UserPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserPrivProtocol.setStatus("current")


class _SnmpV3UserPrivProtocolPassword_Type(SnmpAdminString):
    """Custom type snmpV3UserPrivProtocolPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3UserPrivProtocolPassword_Type.__name__ = "SnmpAdminString"
_SnmpV3UserPrivProtocolPassword_Object = MibTableColumn
snmpV3UserPrivProtocolPassword = _SnmpV3UserPrivProtocolPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 7),
    _SnmpV3UserPrivProtocolPassword_Type()
)
snmpV3UserPrivProtocolPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserPrivProtocolPassword.setStatus("current")
_SnmpV3UserStatus_Type = RowStatus
_SnmpV3UserStatus_Object = MibTableColumn
snmpV3UserStatus = _SnmpV3UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 2, 1, 1, 8),
    _SnmpV3UserStatus_Type()
)
snmpV3UserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserStatus.setStatus("current")
_SnmpV3Group_ObjectIdentity = ObjectIdentity
snmpV3Group = _SnmpV3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3)
)
_SnmpV3GroupTable_Object = MibTable
snmpV3GroupTable = _SnmpV3GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1)
)
if mibBuilder.loadTexts:
    snmpV3GroupTable.setStatus("current")
_SnmpV3GroupEntry_Object = MibTableRow
snmpV3GroupEntry = _SnmpV3GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1)
)
snmpV3GroupEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "snmpV3GroupName"),
    (0, "DGS-1210-20_BX", "snmpV3GroupSecurityModel"),
    (0, "DGS-1210-20_BX", "snmpV3GroupSecurityLevel"),
)
if mibBuilder.loadTexts:
    snmpV3GroupEntry.setStatus("current")


class _SnmpV3GroupName_Type(SnmpAdminString):
    """Custom type snmpV3GroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3GroupName_Type.__name__ = "SnmpAdminString"
_SnmpV3GroupName_Object = MibTableColumn
snmpV3GroupName = _SnmpV3GroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1, 1),
    _SnmpV3GroupName_Type()
)
snmpV3GroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3GroupName.setStatus("current")


class _SnmpV3GroupSecurityModel_Type(Integer32):
    """Custom type snmpV3GroupSecurityModel based on Integer32"""
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


_SnmpV3GroupSecurityModel_Type.__name__ = "Integer32"
_SnmpV3GroupSecurityModel_Object = MibTableColumn
snmpV3GroupSecurityModel = _SnmpV3GroupSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1, 2),
    _SnmpV3GroupSecurityModel_Type()
)
snmpV3GroupSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3GroupSecurityModel.setStatus("current")
_SnmpV3GroupSecurityLevel_Type = SnmpSecurityLevel
_SnmpV3GroupSecurityLevel_Object = MibTableColumn
snmpV3GroupSecurityLevel = _SnmpV3GroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1, 3),
    _SnmpV3GroupSecurityLevel_Type()
)
snmpV3GroupSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3GroupSecurityLevel.setStatus("current")


class _SnmpV3GroupReadViewName_Type(SnmpAdminString):
    """Custom type snmpV3GroupReadViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3GroupReadViewName_Type.__name__ = "SnmpAdminString"
_SnmpV3GroupReadViewName_Object = MibTableColumn
snmpV3GroupReadViewName = _SnmpV3GroupReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1, 4),
    _SnmpV3GroupReadViewName_Type()
)
snmpV3GroupReadViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupReadViewName.setStatus("current")


class _SnmpV3GroupWriteViewName_Type(SnmpAdminString):
    """Custom type snmpV3GroupWriteViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3GroupWriteViewName_Type.__name__ = "SnmpAdminString"
_SnmpV3GroupWriteViewName_Object = MibTableColumn
snmpV3GroupWriteViewName = _SnmpV3GroupWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1, 5),
    _SnmpV3GroupWriteViewName_Type()
)
snmpV3GroupWriteViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupWriteViewName.setStatus("current")


class _SnmpV3GroupNotifyViewName_Type(SnmpAdminString):
    """Custom type snmpV3GroupNotifyViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpV3GroupNotifyViewName_Type.__name__ = "SnmpAdminString"
_SnmpV3GroupNotifyViewName_Object = MibTableColumn
snmpV3GroupNotifyViewName = _SnmpV3GroupNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1, 6),
    _SnmpV3GroupNotifyViewName_Type()
)
snmpV3GroupNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupNotifyViewName.setStatus("current")
_SnmpV3GroupStatus_Type = RowStatus
_SnmpV3GroupStatus_Object = MibTableColumn
snmpV3GroupStatus = _SnmpV3GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 3, 1, 1, 7),
    _SnmpV3GroupStatus_Type()
)
snmpV3GroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupStatus.setStatus("current")
_SnmpV3ViewTree_ObjectIdentity = ObjectIdentity
snmpV3ViewTree = _SnmpV3ViewTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4)
)
_SnmpV3ViewTreeTable_Object = MibTable
snmpV3ViewTreeTable = _SnmpV3ViewTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4, 1)
)
if mibBuilder.loadTexts:
    snmpV3ViewTreeTable.setStatus("current")
_SnmpV3ViewTreeEntry_Object = MibTableRow
snmpV3ViewTreeEntry = _SnmpV3ViewTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4, 1, 1)
)
snmpV3ViewTreeEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "snmpV3viewTreeName"),
    (0, "DGS-1210-20_BX", "snmpV3viewTreeSubtree"),
)
if mibBuilder.loadTexts:
    snmpV3ViewTreeEntry.setStatus("current")


class _SnmpV3viewTreeName_Type(SnmpAdminString):
    """Custom type snmpV3viewTreeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3viewTreeName_Type.__name__ = "SnmpAdminString"
_SnmpV3viewTreeName_Object = MibTableColumn
snmpV3viewTreeName = _SnmpV3viewTreeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4, 1, 1, 1),
    _SnmpV3viewTreeName_Type()
)
snmpV3viewTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3viewTreeName.setStatus("current")
_SnmpV3viewTreeSubtree_Type = ObjectIdentifier
_SnmpV3viewTreeSubtree_Object = MibTableColumn
snmpV3viewTreeSubtree = _SnmpV3viewTreeSubtree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4, 1, 1, 2),
    _SnmpV3viewTreeSubtree_Type()
)
snmpV3viewTreeSubtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3viewTreeSubtree.setStatus("current")


class _SnmpV3viewTreeMask_Type(OctetString):
    """Custom type snmpV3viewTreeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpV3viewTreeMask_Type.__name__ = "OctetString"
_SnmpV3viewTreeMask_Object = MibTableColumn
snmpV3viewTreeMask = _SnmpV3viewTreeMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4, 1, 1, 3),
    _SnmpV3viewTreeMask_Type()
)
snmpV3viewTreeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeMask.setStatus("current")


class _SnmpV3viewTreeType_Type(Integer32):
    """Custom type snmpV3viewTreeType based on Integer32"""
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


_SnmpV3viewTreeType_Type.__name__ = "Integer32"
_SnmpV3viewTreeType_Object = MibTableColumn
snmpV3viewTreeType = _SnmpV3viewTreeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4, 1, 1, 4),
    _SnmpV3viewTreeType_Type()
)
snmpV3viewTreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeType.setStatus("current")
_SnmpV3viewTreeStatus_Type = RowStatus
_SnmpV3viewTreeStatus_Object = MibTableColumn
snmpV3viewTreeStatus = _SnmpV3viewTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 4, 1, 1, 5),
    _SnmpV3viewTreeStatus_Type()
)
snmpV3viewTreeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeStatus.setStatus("current")
_SnmpV3Community_ObjectIdentity = ObjectIdentity
snmpV3Community = _SnmpV3Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 5)
)
_SnmpV3CommunityTable_Object = MibTable
snmpV3CommunityTable = _SnmpV3CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 5, 1)
)
if mibBuilder.loadTexts:
    snmpV3CommunityTable.setStatus("current")
_SnmpV3CommunityEntry_Object = MibTableRow
snmpV3CommunityEntry = _SnmpV3CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 5, 1, 1)
)
snmpV3CommunityEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "snmpV3CommunityName"),
)
if mibBuilder.loadTexts:
    snmpV3CommunityEntry.setStatus("current")
_SnmpV3CommunityName_Type = OctetString
_SnmpV3CommunityName_Object = MibTableColumn
snmpV3CommunityName = _SnmpV3CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 5, 1, 1, 1),
    _SnmpV3CommunityName_Type()
)
snmpV3CommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3CommunityName.setStatus("current")


class _SnmpV3CommunityPolicy_Type(SnmpAdminString):
    """Custom type snmpV3CommunityPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3CommunityPolicy_Type.__name__ = "SnmpAdminString"
_SnmpV3CommunityPolicy_Object = MibTableColumn
snmpV3CommunityPolicy = _SnmpV3CommunityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 5, 1, 1, 2),
    _SnmpV3CommunityPolicy_Type()
)
snmpV3CommunityPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityPolicy.setStatus("current")
_SnmpV3CommunityStatus_Type = RowStatus
_SnmpV3CommunityStatus_Object = MibTableColumn
snmpV3CommunityStatus = _SnmpV3CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 5, 1, 1, 3),
    _SnmpV3CommunityStatus_Type()
)
snmpV3CommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityStatus.setStatus("current")
_SnmpV3Host_ObjectIdentity = ObjectIdentity
snmpV3Host = _SnmpV3Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6)
)
_Ipv4snmpV3HostTable_Object = MibTable
ipv4snmpV3HostTable = _Ipv4snmpV3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 1)
)
if mibBuilder.loadTexts:
    ipv4snmpV3HostTable.setStatus("obsolete")
_Ipv4snmpV3HostEntry_Object = MibTableRow
ipv4snmpV3HostEntry = _Ipv4snmpV3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 1, 1)
)
ipv4snmpV3HostEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "ipv4snmpV3HostAddress"),
)
if mibBuilder.loadTexts:
    ipv4snmpV3HostEntry.setStatus("obsolete")
_Ipv4snmpV3HostAddress_Type = IpAddress
_Ipv4snmpV3HostAddress_Object = MibTableColumn
ipv4snmpV3HostAddress = _Ipv4snmpV3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 1, 1, 1),
    _Ipv4snmpV3HostAddress_Type()
)
ipv4snmpV3HostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4snmpV3HostAddress.setStatus("obsolete")


class _Ipv4snmpV3HostCommunityName_Type(SnmpAdminString):
    """Custom type ipv4snmpV3HostCommunityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Ipv4snmpV3HostCommunityName_Type.__name__ = "SnmpAdminString"
_Ipv4snmpV3HostCommunityName_Object = MibTableColumn
ipv4snmpV3HostCommunityName = _Ipv4snmpV3HostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 1, 1, 2),
    _Ipv4snmpV3HostCommunityName_Type()
)
ipv4snmpV3HostCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4snmpV3HostCommunityName.setStatus("obsolete")


class _Ipv4snmpV3HostVersion_Type(Integer32):
    """Custom type ipv4snmpV3HostVersion based on Integer32"""
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
          ("v3AuthNoPriv", 4),
          ("v3AuthPriv", 5),
          ("v3NoAuthNoPriv", 3))
    )


_Ipv4snmpV3HostVersion_Type.__name__ = "Integer32"
_Ipv4snmpV3HostVersion_Object = MibTableColumn
ipv4snmpV3HostVersion = _Ipv4snmpV3HostVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 1, 1, 3),
    _Ipv4snmpV3HostVersion_Type()
)
ipv4snmpV3HostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4snmpV3HostVersion.setStatus("obsolete")
_Ipv4snmpV3HostStatus_Type = RowStatus
_Ipv4snmpV3HostStatus_Object = MibTableColumn
ipv4snmpV3HostStatus = _Ipv4snmpV3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 1, 1, 4),
    _Ipv4snmpV3HostStatus_Type()
)
ipv4snmpV3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4snmpV3HostStatus.setStatus("obsolete")
_SnmpV3HostTable_Object = MibTable
snmpV3HostTable = _SnmpV3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2)
)
if mibBuilder.loadTexts:
    snmpV3HostTable.setStatus("current")
_SnmpV3HostEntry_Object = MibTableRow
snmpV3HostEntry = _SnmpV3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2, 1)
)
snmpV3HostEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "snmpV3HostAddress"),
    (0, "DGS-1210-20_BX", "snmpV3IPType"),
)
if mibBuilder.loadTexts:
    snmpV3HostEntry.setStatus("current")
_SnmpV3HostAddress_Type = Ipv6Address
_SnmpV3HostAddress_Object = MibTableColumn
snmpV3HostAddress = _SnmpV3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2, 1, 1),
    _SnmpV3HostAddress_Type()
)
snmpV3HostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3HostAddress.setStatus("current")


class _SnmpV3IPType_Type(Integer32):
    """Custom type snmpV3IPType based on Integer32"""
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


_SnmpV3IPType_Type.__name__ = "Integer32"
_SnmpV3IPType_Object = MibTableColumn
snmpV3IPType = _SnmpV3IPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2, 1, 2),
    _SnmpV3IPType_Type()
)
snmpV3IPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3IPType.setStatus("current")


class _SnmpV3HostCommunityName_Type(SnmpAdminString):
    """Custom type snmpV3HostCommunityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3HostCommunityName_Type.__name__ = "SnmpAdminString"
_SnmpV3HostCommunityName_Object = MibTableColumn
snmpV3HostCommunityName = _SnmpV3HostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2, 1, 3),
    _SnmpV3HostCommunityName_Type()
)
snmpV3HostCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostCommunityName.setStatus("current")


class _SnmpV3HostVersion_Type(Integer32):
    """Custom type snmpV3HostVersion based on Integer32"""
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
          ("v3AuthNoPriv", 4),
          ("v3AuthPriv", 5),
          ("v3NoAuthNoPriv", 3))
    )


_SnmpV3HostVersion_Type.__name__ = "Integer32"
_SnmpV3HostVersion_Object = MibTableColumn
snmpV3HostVersion = _SnmpV3HostVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2, 1, 4),
    _SnmpV3HostVersion_Type()
)
snmpV3HostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostVersion.setStatus("current")
_SnmpV3HostInterfaceName_Type = OctetString
_SnmpV3HostInterfaceName_Object = MibTableColumn
snmpV3HostInterfaceName = _SnmpV3HostInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2, 1, 5),
    _SnmpV3HostInterfaceName_Type()
)
snmpV3HostInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostInterfaceName.setStatus("current")
_SnmpV3HostStatus_Type = RowStatus
_SnmpV3HostStatus_Object = MibTableColumn
snmpV3HostStatus = _SnmpV3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 6, 2, 1, 6),
    _SnmpV3HostStatus_Type()
)
snmpV3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostStatus.setStatus("current")
_SnmpV3EngineID_Type = SnmpEngineID
_SnmpV3EngineID_Object = MibScalar
snmpV3EngineID = _SnmpV3EngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 7),
    _SnmpV3EngineID_Type()
)
snmpV3EngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3EngineID.setStatus("current")
_SnmpV3Trap_ObjectIdentity = ObjectIdentity
snmpV3Trap = _SnmpV3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 8)
)


class _SnmpV3TrapSNMPAuthentication_Type(Integer32):
    """Custom type snmpV3TrapSNMPAuthentication based on Integer32"""
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


_SnmpV3TrapSNMPAuthentication_Type.__name__ = "Integer32"
_SnmpV3TrapSNMPAuthentication_Object = MibScalar
snmpV3TrapSNMPAuthentication = _SnmpV3TrapSNMPAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 8, 1),
    _SnmpV3TrapSNMPAuthentication_Type()
)
snmpV3TrapSNMPAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapSNMPAuthentication.setStatus("current")


class _SnmpV3TrapBootup_Type(Integer32):
    """Custom type snmpV3TrapBootup based on Integer32"""
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


_SnmpV3TrapBootup_Type.__name__ = "Integer32"
_SnmpV3TrapBootup_Object = MibScalar
snmpV3TrapBootup = _SnmpV3TrapBootup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 8, 2),
    _SnmpV3TrapBootup_Type()
)
snmpV3TrapBootup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapBootup.setStatus("current")


class _SnmpV3TrapPortLinkUpDown_Type(Integer32):
    """Custom type snmpV3TrapPortLinkUpDown based on Integer32"""
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


_SnmpV3TrapPortLinkUpDown_Type.__name__ = "Integer32"
_SnmpV3TrapPortLinkUpDown_Object = MibScalar
snmpV3TrapPortLinkUpDown = _SnmpV3TrapPortLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 8, 3),
    _SnmpV3TrapPortLinkUpDown_Type()
)
snmpV3TrapPortLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapPortLinkUpDown.setStatus("current")


class _SnmpV3TrapRSTPStateChange_Type(Integer32):
    """Custom type snmpV3TrapRSTPStateChange based on Integer32"""
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


_SnmpV3TrapRSTPStateChange_Type.__name__ = "Integer32"
_SnmpV3TrapRSTPStateChange_Object = MibScalar
snmpV3TrapRSTPStateChange = _SnmpV3TrapRSTPStateChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 8, 4),
    _SnmpV3TrapRSTPStateChange_Type()
)
snmpV3TrapRSTPStateChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapRSTPStateChange.setStatus("current")


class _SnmpV3TrapFirmUpgrade_Type(Integer32):
    """Custom type snmpV3TrapFirmUpgrade based on Integer32"""
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


_SnmpV3TrapFirmUpgrade_Type.__name__ = "Integer32"
_SnmpV3TrapFirmUpgrade_Object = MibScalar
snmpV3TrapFirmUpgrade = _SnmpV3TrapFirmUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 25, 8, 5),
    _SnmpV3TrapFirmUpgrade_Type()
)
snmpV3TrapFirmUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapFirmUpgrade.setStatus("current")
_CompanyAutoSurveillanceVlan_ObjectIdentity = ObjectIdentity
companyAutoSurveillanceVlan = _CompanyAutoSurveillanceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26)
)
_AutoSurveillanceVlanSystem_ObjectIdentity = ObjectIdentity
autoSurveillanceVlanSystem = _AutoSurveillanceVlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 1)
)


class _AutoSurveillanceVlanMode_Type(Integer32):
    """Custom type autoSurveillanceVlanMode based on Integer32"""
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


_AutoSurveillanceVlanMode_Type.__name__ = "Integer32"
_AutoSurveillanceVlanMode_Object = MibScalar
autoSurveillanceVlanMode = _AutoSurveillanceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 1, 1),
    _AutoSurveillanceVlanMode_Type()
)
autoSurveillanceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanMode.setStatus("current")
_AutoSurveillanceVlanId_Type = Integer32
_AutoSurveillanceVlanId_Object = MibScalar
autoSurveillanceVlanId = _AutoSurveillanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 1, 2),
    _AutoSurveillanceVlanId_Type()
)
autoSurveillanceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanId.setStatus("current")


class _AutoSurveillanceVlanPriority_Type(Integer32):
    """Custom type autoSurveillanceVlanPriority based on Integer32"""
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
        *(("high", 1),
          ("highest", 0),
          ("low", 3),
          ("medium", 2))
    )


_AutoSurveillanceVlanPriority_Type.__name__ = "Integer32"
_AutoSurveillanceVlanPriority_Object = MibScalar
autoSurveillanceVlanPriority = _AutoSurveillanceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 1, 3),
    _AutoSurveillanceVlanPriority_Type()
)
autoSurveillanceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanPriority.setStatus("current")
_AutoSurveillanceVlanTaggedUplinkDownlinkPort_Type = PortList
_AutoSurveillanceVlanTaggedUplinkDownlinkPort_Object = MibScalar
autoSurveillanceVlanTaggedUplinkDownlinkPort = _AutoSurveillanceVlanTaggedUplinkDownlinkPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 1, 4),
    _AutoSurveillanceVlanTaggedUplinkDownlinkPort_Type()
)
autoSurveillanceVlanTaggedUplinkDownlinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanTaggedUplinkDownlinkPort.setStatus("current")
_AutoSurveillanceVlanOUI_ObjectIdentity = ObjectIdentity
autoSurveillanceVlanOUI = _AutoSurveillanceVlanOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2)
)
_AutoSurveillanceVlanOUITable_Object = MibTable
autoSurveillanceVlanOUITable = _AutoSurveillanceVlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2, 1)
)
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUITable.setStatus("current")
_AutoSurveillanceVlanOUIEntry_Object = MibTableRow
autoSurveillanceVlanOUIEntry = _AutoSurveillanceVlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2, 1, 1)
)
autoSurveillanceVlanOUIEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "autoSurveillanceVlanOUISurveillanceOUI"),
)
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIEntry.setStatus("current")
_AutoSurveillanceVlanOUISurveillanceOUI_Type = MacAddress
_AutoSurveillanceVlanOUISurveillanceOUI_Object = MibTableColumn
autoSurveillanceVlanOUISurveillanceOUI = _AutoSurveillanceVlanOUISurveillanceOUI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2, 1, 1, 1),
    _AutoSurveillanceVlanOUISurveillanceOUI_Type()
)
autoSurveillanceVlanOUISurveillanceOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUISurveillanceOUI.setStatus("current")
_AutoSurveillanceVlanOUIDescription_Type = OctetString
_AutoSurveillanceVlanOUIDescription_Object = MibTableColumn
autoSurveillanceVlanOUIDescription = _AutoSurveillanceVlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2, 1, 1, 2),
    _AutoSurveillanceVlanOUIDescription_Type()
)
autoSurveillanceVlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIDescription.setStatus("current")
_AutoSurveillanceVlanOUIMask_Type = MacAddress
_AutoSurveillanceVlanOUIMask_Object = MibTableColumn
autoSurveillanceVlanOUIMask = _AutoSurveillanceVlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2, 1, 1, 3),
    _AutoSurveillanceVlanOUIMask_Type()
)
autoSurveillanceVlanOUIMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIMask.setStatus("current")


class _AutoSurveillanceVlanOUIComponentType_Type(Integer32):
    """Custom type autoSurveillanceVlanOUIComponentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("d-Link_Surveillance_Device", 5),
          ("network_Storage", 3),
          ("other_IP_Surveillance_Devices", 4),
          ("vMS_Client", 1),
          ("video_Encoder", 2),
          ("video_Management_Server", 0))
    )


_AutoSurveillanceVlanOUIComponentType_Type.__name__ = "Integer32"
_AutoSurveillanceVlanOUIComponentType_Object = MibTableColumn
autoSurveillanceVlanOUIComponentType = _AutoSurveillanceVlanOUIComponentType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2, 1, 1, 4),
    _AutoSurveillanceVlanOUIComponentType_Type()
)
autoSurveillanceVlanOUIComponentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIComponentType.setStatus("current")
_AutoSurveillanceVlanOUIStatus_Type = RowStatus
_AutoSurveillanceVlanOUIStatus_Object = MibTableColumn
autoSurveillanceVlanOUIStatus = _AutoSurveillanceVlanOUIStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 26, 2, 1, 1, 5),
    _AutoSurveillanceVlanOUIStatus_Type()
)
autoSurveillanceVlanOUIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIStatus.setStatus("current")
_CompanyTraps_ObjectIdentity = ObjectIdentity
companyTraps = _CompanyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27, 0)
)
_CompanyGreenSetting_ObjectIdentity = ObjectIdentity
companyGreenSetting = _CompanyGreenSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31)
)
_DlinkGreenLEDShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenLEDShutoff = _DlinkGreenLEDShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 1)
)
_DlinkGreenLEDShutoffPortList_Type = PortList
_DlinkGreenLEDShutoffPortList_Object = MibScalar
dlinkGreenLEDShutoffPortList = _DlinkGreenLEDShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 1, 1),
    _DlinkGreenLEDShutoffPortList_Type()
)
dlinkGreenLEDShutoffPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffPortList.setStatus("current")


class _DlinkGreenLEDShutoffState_Type(Integer32):
    """Custom type dlinkGreenLEDShutoffState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DlinkGreenLEDShutoffState_Type.__name__ = "Integer32"
_DlinkGreenLEDShutoffState_Object = MibScalar
dlinkGreenLEDShutoffState = _DlinkGreenLEDShutoffState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 1, 2),
    _DlinkGreenLEDShutoffState_Type()
)
dlinkGreenLEDShutoffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffState.setStatus("current")


class _DlinkGreenLEDShutoffTimeProfile1_Type(DisplayString):
    """Custom type dlinkGreenLEDShutoffTimeProfile1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenLEDShutoffTimeProfile1_Type.__name__ = "DisplayString"
_DlinkGreenLEDShutoffTimeProfile1_Object = MibScalar
dlinkGreenLEDShutoffTimeProfile1 = _DlinkGreenLEDShutoffTimeProfile1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 1, 3),
    _DlinkGreenLEDShutoffTimeProfile1_Type()
)
dlinkGreenLEDShutoffTimeProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffTimeProfile1.setStatus("current")


class _DlinkGreenLEDShutoffTimeProfile2_Type(DisplayString):
    """Custom type dlinkGreenLEDShutoffTimeProfile2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenLEDShutoffTimeProfile2_Type.__name__ = "DisplayString"
_DlinkGreenLEDShutoffTimeProfile2_Object = MibScalar
dlinkGreenLEDShutoffTimeProfile2 = _DlinkGreenLEDShutoffTimeProfile2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 1, 4),
    _DlinkGreenLEDShutoffTimeProfile2_Type()
)
dlinkGreenLEDShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffTimeProfile2.setStatus("current")
_DlinkGreenPortShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenPortShutoff = _DlinkGreenPortShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 2)
)
_DlinkGreenPortShutoffPortList_Type = PortList
_DlinkGreenPortShutoffPortList_Object = MibScalar
dlinkGreenPortShutoffPortList = _DlinkGreenPortShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 2, 1),
    _DlinkGreenPortShutoffPortList_Type()
)
dlinkGreenPortShutoffPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffPortList.setStatus("current")


class _DlinkGreenPortShutoffState_Type(Integer32):
    """Custom type dlinkGreenPortShutoffState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DlinkGreenPortShutoffState_Type.__name__ = "Integer32"
_DlinkGreenPortShutoffState_Object = MibScalar
dlinkGreenPortShutoffState = _DlinkGreenPortShutoffState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 2, 2),
    _DlinkGreenPortShutoffState_Type()
)
dlinkGreenPortShutoffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffState.setStatus("current")


class _DlinkGreenPortShutoffTimeProfile1_Type(DisplayString):
    """Custom type dlinkGreenPortShutoffTimeProfile1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenPortShutoffTimeProfile1_Type.__name__ = "DisplayString"
_DlinkGreenPortShutoffTimeProfile1_Object = MibScalar
dlinkGreenPortShutoffTimeProfile1 = _DlinkGreenPortShutoffTimeProfile1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 2, 3),
    _DlinkGreenPortShutoffTimeProfile1_Type()
)
dlinkGreenPortShutoffTimeProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffTimeProfile1.setStatus("current")


class _DlinkGreenPortShutoffTimeProfile2_Type(DisplayString):
    """Custom type dlinkGreenPortShutoffTimeProfile2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenPortShutoffTimeProfile2_Type.__name__ = "DisplayString"
_DlinkGreenPortShutoffTimeProfile2_Object = MibScalar
dlinkGreenPortShutoffTimeProfile2 = _DlinkGreenPortShutoffTimeProfile2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 2, 4),
    _DlinkGreenPortShutoffTimeProfile2_Type()
)
dlinkGreenPortShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffTimeProfile2.setStatus("current")
_DlinkGreenPortStandby_ObjectIdentity = ObjectIdentity
dlinkGreenPortStandby = _DlinkGreenPortStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 3)
)
_DlinkGreenPortStandbyPortList_Type = PortList
_DlinkGreenPortStandbyPortList_Object = MibScalar
dlinkGreenPortStandbyPortList = _DlinkGreenPortStandbyPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 3, 1),
    _DlinkGreenPortStandbyPortList_Type()
)
dlinkGreenPortStandbyPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortStandbyPortList.setStatus("current")


class _DlinkGreenPortStandbyState_Type(Integer32):
    """Custom type dlinkGreenPortStandbyState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DlinkGreenPortStandbyState_Type.__name__ = "Integer32"
_DlinkGreenPortStandbyState_Object = MibScalar
dlinkGreenPortStandbyState = _DlinkGreenPortStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 3, 2),
    _DlinkGreenPortStandbyState_Type()
)
dlinkGreenPortStandbyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortStandbyState.setStatus("current")


class _DlinkGreenPortStandbyTimeProfile1_Type(DisplayString):
    """Custom type dlinkGreenPortStandbyTimeProfile1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenPortStandbyTimeProfile1_Type.__name__ = "DisplayString"
_DlinkGreenPortStandbyTimeProfile1_Object = MibScalar
dlinkGreenPortStandbyTimeProfile1 = _DlinkGreenPortStandbyTimeProfile1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 3, 3),
    _DlinkGreenPortStandbyTimeProfile1_Type()
)
dlinkGreenPortStandbyTimeProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortStandbyTimeProfile1.setStatus("current")


class _DlinkGreenPortStandbyTimeProfile2_Type(DisplayString):
    """Custom type dlinkGreenPortStandbyTimeProfile2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenPortStandbyTimeProfile2_Type.__name__ = "DisplayString"
_DlinkGreenPortStandbyTimeProfile2_Object = MibScalar
dlinkGreenPortStandbyTimeProfile2 = _DlinkGreenPortStandbyTimeProfile2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 3, 4),
    _DlinkGreenPortStandbyTimeProfile2_Type()
)
dlinkGreenPortStandbyTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortStandbyTimeProfile2.setStatus("current")
_DlinkGreenSystemHibernation_ObjectIdentity = ObjectIdentity
dlinkGreenSystemHibernation = _DlinkGreenSystemHibernation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 4)
)


class _DlinkGreenSystemHibernationState_Type(Integer32):
    """Custom type dlinkGreenSystemHibernationState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DlinkGreenSystemHibernationState_Type.__name__ = "Integer32"
_DlinkGreenSystemHibernationState_Object = MibScalar
dlinkGreenSystemHibernationState = _DlinkGreenSystemHibernationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 4, 1),
    _DlinkGreenSystemHibernationState_Type()
)
dlinkGreenSystemHibernationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenSystemHibernationState.setStatus("current")


class _DlinkGreenSystemHibernationTimeProfile1_Type(DisplayString):
    """Custom type dlinkGreenSystemHibernationTimeProfile1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenSystemHibernationTimeProfile1_Type.__name__ = "DisplayString"
_DlinkGreenSystemHibernationTimeProfile1_Object = MibScalar
dlinkGreenSystemHibernationTimeProfile1 = _DlinkGreenSystemHibernationTimeProfile1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 4, 2),
    _DlinkGreenSystemHibernationTimeProfile1_Type()
)
dlinkGreenSystemHibernationTimeProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenSystemHibernationTimeProfile1.setStatus("current")


class _DlinkGreenSystemHibernationTimeProfile2_Type(DisplayString):
    """Custom type dlinkGreenSystemHibernationTimeProfile2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DlinkGreenSystemHibernationTimeProfile2_Type.__name__ = "DisplayString"
_DlinkGreenSystemHibernationTimeProfile2_Object = MibScalar
dlinkGreenSystemHibernationTimeProfile2 = _DlinkGreenSystemHibernationTimeProfile2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 4, 3),
    _DlinkGreenSystemHibernationTimeProfile2_Type()
)
dlinkGreenSystemHibernationTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenSystemHibernationTimeProfile2.setStatus("current")


class _DlinkPowerSavCableLenDetectionState_Type(Integer32):
    """Custom type dlinkPowerSavCableLenDetectionState based on Integer32"""
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


_DlinkPowerSavCableLenDetectionState_Type.__name__ = "Integer32"
_DlinkPowerSavCableLenDetectionState_Object = MibScalar
dlinkPowerSavCableLenDetectionState = _DlinkPowerSavCableLenDetectionState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 5),
    _DlinkPowerSavCableLenDetectionState_Type()
)
dlinkPowerSavCableLenDetectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkPowerSavCableLenDetectionState.setStatus("current")


class _DlinkPowerSavLinkStatusDetectState_Type(Integer32):
    """Custom type dlinkPowerSavLinkStatusDetectState based on Integer32"""
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


_DlinkPowerSavLinkStatusDetectState_Type.__name__ = "Integer32"
_DlinkPowerSavLinkStatusDetectState_Object = MibScalar
dlinkPowerSavLinkStatusDetectState = _DlinkPowerSavLinkStatusDetectState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 31, 6),
    _DlinkPowerSavLinkStatusDetectState_Type()
)
dlinkPowerSavLinkStatusDetectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkPowerSavLinkStatusDetectState.setStatus("current")
_CompanyTimeRangeMgmt_ObjectIdentity = ObjectIdentity
companyTimeRangeMgmt = _CompanyTimeRangeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32)
)
_SwTimeRangeSettingTable_Object = MibTable
swTimeRangeSettingTable = _SwTimeRangeSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1)
)
if mibBuilder.loadTexts:
    swTimeRangeSettingTable.setStatus("current")
_SwTimeRangeSettingEntry_Object = MibTableRow
swTimeRangeSettingEntry = _SwTimeRangeSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1)
)
swTimeRangeSettingEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "swTimeRangeIndex"),
)
if mibBuilder.loadTexts:
    swTimeRangeSettingEntry.setStatus("current")


class _SwTimeRangeIndex_Type(Integer32):
    """Custom type swTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_SwTimeRangeIndex_Type.__name__ = "Integer32"
_SwTimeRangeIndex_Object = MibTableColumn
swTimeRangeIndex = _SwTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 1),
    _SwTimeRangeIndex_Type()
)
swTimeRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTimeRangeIndex.setStatus("current")


class _SwTimeRangeName_Type(DisplayString):
    """Custom type swTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SwTimeRangeName_Type.__name__ = "DisplayString"
_SwTimeRangeName_Object = MibTableColumn
swTimeRangeName = _SwTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 2),
    _SwTimeRangeName_Type()
)
swTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeName.setStatus("current")


class _SwTimeRangeDate_Type(Integer32):
    """Custom type swTimeRangeDate based on Integer32"""
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


_SwTimeRangeDate_Type.__name__ = "Integer32"
_SwTimeRangeDate_Object = MibTableColumn
swTimeRangeDate = _SwTimeRangeDate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 3),
    _SwTimeRangeDate_Type()
)
swTimeRangeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeDate.setStatus("current")


class _SwTimeRangeStartYear_Type(Integer32):
    """Custom type swTimeRangeStartYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2009,
              2010,
              2011,
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
              2029,
              2030,
              2031,
              2032,
              2033,
              2034,
              2035,
              2036,
              2037)
        )
    )
    namedValues = NamedValues(
        *(("y2009", 2009),
          ("y2010", 2010),
          ("y2011", 2011),
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
          ("y2029", 2029),
          ("y2030", 2030),
          ("y2031", 2031),
          ("y2032", 2032),
          ("y2033", 2033),
          ("y2034", 2034),
          ("y2035", 2035),
          ("y2036", 2036),
          ("y2037", 2037))
    )


_SwTimeRangeStartYear_Type.__name__ = "Integer32"
_SwTimeRangeStartYear_Object = MibTableColumn
swTimeRangeStartYear = _SwTimeRangeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 4),
    _SwTimeRangeStartYear_Type()
)
swTimeRangeStartYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeStartYear.setStatus("current")


class _SwTimeRangeStartMonth_Type(Integer32):
    """Custom type swTimeRangeStartMonth based on Integer32"""
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


_SwTimeRangeStartMonth_Type.__name__ = "Integer32"
_SwTimeRangeStartMonth_Object = MibTableColumn
swTimeRangeStartMonth = _SwTimeRangeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 5),
    _SwTimeRangeStartMonth_Type()
)
swTimeRangeStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeStartMonth.setStatus("current")


class _SwTimeRangeStartDay_Type(Integer32):
    """Custom type swTimeRangeStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SwTimeRangeStartDay_Type.__name__ = "Integer32"
_SwTimeRangeStartDay_Object = MibTableColumn
swTimeRangeStartDay = _SwTimeRangeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 6),
    _SwTimeRangeStartDay_Type()
)
swTimeRangeStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeStartDay.setStatus("current")


class _SwTimeRangeStartHour_Type(Integer32):
    """Custom type swTimeRangeStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SwTimeRangeStartHour_Type.__name__ = "Integer32"
_SwTimeRangeStartHour_Object = MibTableColumn
swTimeRangeStartHour = _SwTimeRangeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 7),
    _SwTimeRangeStartHour_Type()
)
swTimeRangeStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeStartHour.setStatus("current")


class _SwTimeRangeStartMinute_Type(Integer32):
    """Custom type swTimeRangeStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SwTimeRangeStartMinute_Type.__name__ = "Integer32"
_SwTimeRangeStartMinute_Object = MibTableColumn
swTimeRangeStartMinute = _SwTimeRangeStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 8),
    _SwTimeRangeStartMinute_Type()
)
swTimeRangeStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeStartMinute.setStatus("current")


class _SwTimeRangeEndYear_Type(Integer32):
    """Custom type swTimeRangeEndYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2009,
              2010,
              2011,
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
              2029,
              2030,
              2031,
              2032,
              2033,
              2034,
              2035,
              2036,
              2037)
        )
    )
    namedValues = NamedValues(
        *(("y2009", 2009),
          ("y2010", 2010),
          ("y2011", 2011),
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
          ("y2029", 2029),
          ("y2030", 2030),
          ("y2031", 2031),
          ("y2032", 2032),
          ("y2033", 2033),
          ("y2034", 2034),
          ("y2035", 2035),
          ("y2036", 2036),
          ("y2037", 2037))
    )


_SwTimeRangeEndYear_Type.__name__ = "Integer32"
_SwTimeRangeEndYear_Object = MibTableColumn
swTimeRangeEndYear = _SwTimeRangeEndYear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 9),
    _SwTimeRangeEndYear_Type()
)
swTimeRangeEndYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeEndYear.setStatus("current")


class _SwTimeRangeEndMonth_Type(Integer32):
    """Custom type swTimeRangeEndMonth based on Integer32"""
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


_SwTimeRangeEndMonth_Type.__name__ = "Integer32"
_SwTimeRangeEndMonth_Object = MibTableColumn
swTimeRangeEndMonth = _SwTimeRangeEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 10),
    _SwTimeRangeEndMonth_Type()
)
swTimeRangeEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeEndMonth.setStatus("current")


class _SwTimeRangeEndDay_Type(Integer32):
    """Custom type swTimeRangeEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SwTimeRangeEndDay_Type.__name__ = "Integer32"
_SwTimeRangeEndDay_Object = MibTableColumn
swTimeRangeEndDay = _SwTimeRangeEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 11),
    _SwTimeRangeEndDay_Type()
)
swTimeRangeEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeEndDay.setStatus("current")


class _SwTimeRangeEndHour_Type(Integer32):
    """Custom type swTimeRangeEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SwTimeRangeEndHour_Type.__name__ = "Integer32"
_SwTimeRangeEndHour_Object = MibTableColumn
swTimeRangeEndHour = _SwTimeRangeEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 12),
    _SwTimeRangeEndHour_Type()
)
swTimeRangeEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeEndHour.setStatus("current")


class _SwTimeRangeEndMinute_Type(Integer32):
    """Custom type swTimeRangeEndMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SwTimeRangeEndMinute_Type.__name__ = "Integer32"
_SwTimeRangeEndMinute_Object = MibTableColumn
swTimeRangeEndMinute = _SwTimeRangeEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 13),
    _SwTimeRangeEndMinute_Type()
)
swTimeRangeEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeEndMinute.setStatus("current")


class _SwTimeRangeMonday_Type(Integer32):
    """Custom type swTimeRangeMonday based on Integer32"""
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


_SwTimeRangeMonday_Type.__name__ = "Integer32"
_SwTimeRangeMonday_Object = MibTableColumn
swTimeRangeMonday = _SwTimeRangeMonday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 14),
    _SwTimeRangeMonday_Type()
)
swTimeRangeMonday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeMonday.setStatus("current")


class _SwTimeRangeTuesday_Type(Integer32):
    """Custom type swTimeRangeTuesday based on Integer32"""
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


_SwTimeRangeTuesday_Type.__name__ = "Integer32"
_SwTimeRangeTuesday_Object = MibTableColumn
swTimeRangeTuesday = _SwTimeRangeTuesday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 15),
    _SwTimeRangeTuesday_Type()
)
swTimeRangeTuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeTuesday.setStatus("current")


class _SwTimeRangeWednesday_Type(Integer32):
    """Custom type swTimeRangeWednesday based on Integer32"""
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


_SwTimeRangeWednesday_Type.__name__ = "Integer32"
_SwTimeRangeWednesday_Object = MibTableColumn
swTimeRangeWednesday = _SwTimeRangeWednesday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 16),
    _SwTimeRangeWednesday_Type()
)
swTimeRangeWednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeWednesday.setStatus("current")


class _SwTimeRangeThursday_Type(Integer32):
    """Custom type swTimeRangeThursday based on Integer32"""
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


_SwTimeRangeThursday_Type.__name__ = "Integer32"
_SwTimeRangeThursday_Object = MibTableColumn
swTimeRangeThursday = _SwTimeRangeThursday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 17),
    _SwTimeRangeThursday_Type()
)
swTimeRangeThursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeThursday.setStatus("current")


class _SwTimeRangeFriday_Type(Integer32):
    """Custom type swTimeRangeFriday based on Integer32"""
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


_SwTimeRangeFriday_Type.__name__ = "Integer32"
_SwTimeRangeFriday_Object = MibTableColumn
swTimeRangeFriday = _SwTimeRangeFriday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 18),
    _SwTimeRangeFriday_Type()
)
swTimeRangeFriday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeFriday.setStatus("current")


class _SwTimeRangeSaturday_Type(Integer32):
    """Custom type swTimeRangeSaturday based on Integer32"""
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


_SwTimeRangeSaturday_Type.__name__ = "Integer32"
_SwTimeRangeSaturday_Object = MibTableColumn
swTimeRangeSaturday = _SwTimeRangeSaturday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 19),
    _SwTimeRangeSaturday_Type()
)
swTimeRangeSaturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeSaturday.setStatus("current")


class _SwTimeRangeSunday_Type(Integer32):
    """Custom type swTimeRangeSunday based on Integer32"""
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


_SwTimeRangeSunday_Type.__name__ = "Integer32"
_SwTimeRangeSunday_Object = MibTableColumn
swTimeRangeSunday = _SwTimeRangeSunday_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 20),
    _SwTimeRangeSunday_Type()
)
swTimeRangeSunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeSunday.setStatus("current")
_SwTimeRangeRowStatus_Type = RowStatus
_SwTimeRangeRowStatus_Object = MibTableColumn
swTimeRangeRowStatus = _SwTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 32, 1, 1, 21),
    _SwTimeRangeRowStatus_Type()
)
swTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeRowStatus.setStatus("current")
_CompanyStaticMcast_ObjectIdentity = ObjectIdentity
companyStaticMcast = _CompanyStaticMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 35)
)
_StaticMcastTable_Object = MibTable
staticMcastTable = _StaticMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 35, 1)
)
if mibBuilder.loadTexts:
    staticMcastTable.setStatus("current")
_StaticMcastEntry_Object = MibTableRow
staticMcastEntry = _StaticMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 35, 1, 1)
)
staticMcastEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "staticMcastVlanID"),
    (0, "DGS-1210-20_BX", "staticMcastMac"),
    (0, "DGS-1210-20_BX", "staticMcastEgressPorts"),
)
if mibBuilder.loadTexts:
    staticMcastEntry.setStatus("current")
_StaticMcastVlanID_Type = Integer32
_StaticMcastVlanID_Object = MibTableColumn
staticMcastVlanID = _StaticMcastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 35, 1, 1, 1),
    _StaticMcastVlanID_Type()
)
staticMcastVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastVlanID.setStatus("current")
_StaticMcastMac_Type = MacAddress
_StaticMcastMac_Object = MibTableColumn
staticMcastMac = _StaticMcastMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 35, 1, 1, 2),
    _StaticMcastMac_Type()
)
staticMcastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastMac.setStatus("current")
_StaticMcastEgressPorts_Type = PortList
_StaticMcastEgressPorts_Object = MibTableColumn
staticMcastEgressPorts = _StaticMcastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 35, 1, 1, 3),
    _StaticMcastEgressPorts_Type()
)
staticMcastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastEgressPorts.setStatus("current")
_StaticMcastStatus_Type = RowStatus
_StaticMcastStatus_Object = MibTableColumn
staticMcastStatus = _StaticMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 35, 1, 1, 4),
    _StaticMcastStatus_Type()
)
staticMcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMcastStatus.setStatus("current")
_CompanyCableDiagnostic_ObjectIdentity = ObjectIdentity
companyCableDiagnostic = _CompanyCableDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37)
)
_CableDiagTriggerIndex_Type = Integer32
_CableDiagTriggerIndex_Object = MibScalar
cableDiagTriggerIndex = _CableDiagTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 1),
    _CableDiagTriggerIndex_Type()
)
cableDiagTriggerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagTriggerIndex.setStatus("current")


class _CableDiagPair1TestResult_Type(Integer32):
    """Custom type cableDiagPair1TestResult based on Integer32"""
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


_CableDiagPair1TestResult_Type.__name__ = "Integer32"
_CableDiagPair1TestResult_Object = MibScalar
cableDiagPair1TestResult = _CableDiagPair1TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 2),
    _CableDiagPair1TestResult_Type()
)
cableDiagPair1TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1TestResult.setStatus("current")
_CableDiagPair1FaultDistance_Type = Integer32
_CableDiagPair1FaultDistance_Object = MibScalar
cableDiagPair1FaultDistance = _CableDiagPair1FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 3),
    _CableDiagPair1FaultDistance_Type()
)
cableDiagPair1FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1FaultDistance.setStatus("current")


class _CableDiagPair2TestResult_Type(Integer32):
    """Custom type cableDiagPair2TestResult based on Integer32"""
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


_CableDiagPair2TestResult_Type.__name__ = "Integer32"
_CableDiagPair2TestResult_Object = MibScalar
cableDiagPair2TestResult = _CableDiagPair2TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 4),
    _CableDiagPair2TestResult_Type()
)
cableDiagPair2TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2TestResult.setStatus("current")
_CableDiagPair2FaultDistance_Type = Integer32
_CableDiagPair2FaultDistance_Object = MibScalar
cableDiagPair2FaultDistance = _CableDiagPair2FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 5),
    _CableDiagPair2FaultDistance_Type()
)
cableDiagPair2FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2FaultDistance.setStatus("current")


class _CableDiagPair3TestResult_Type(Integer32):
    """Custom type cableDiagPair3TestResult based on Integer32"""
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


_CableDiagPair3TestResult_Type.__name__ = "Integer32"
_CableDiagPair3TestResult_Object = MibScalar
cableDiagPair3TestResult = _CableDiagPair3TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 6),
    _CableDiagPair3TestResult_Type()
)
cableDiagPair3TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3TestResult.setStatus("current")
_CableDiagPair3FaultDistance_Type = Integer32
_CableDiagPair3FaultDistance_Object = MibScalar
cableDiagPair3FaultDistance = _CableDiagPair3FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 7),
    _CableDiagPair3FaultDistance_Type()
)
cableDiagPair3FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3FaultDistance.setStatus("current")


class _CableDiagPair4TestResult_Type(Integer32):
    """Custom type cableDiagPair4TestResult based on Integer32"""
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


_CableDiagPair4TestResult_Type.__name__ = "Integer32"
_CableDiagPair4TestResult_Object = MibScalar
cableDiagPair4TestResult = _CableDiagPair4TestResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 8),
    _CableDiagPair4TestResult_Type()
)
cableDiagPair4TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4TestResult.setStatus("current")
_CableDiagPair4FaultDistance_Type = Integer32
_CableDiagPair4FaultDistance_Object = MibScalar
cableDiagPair4FaultDistance = _CableDiagPair4FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 9),
    _CableDiagPair4FaultDistance_Type()
)
cableDiagPair4FaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4FaultDistance.setStatus("current")


class _CableDiagLengthinRange_Type(Integer32):
    """Custom type cableDiagLengthinRange based on Integer32"""
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


_CableDiagLengthinRange_Type.__name__ = "Integer32"
_CableDiagLengthinRange_Object = MibScalar
cableDiagLengthinRange = _CableDiagLengthinRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 37, 10),
    _CableDiagLengthinRange_Type()
)
cableDiagLengthinRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagLengthinRange.setStatus("current")
_CompanyRMON_ObjectIdentity = ObjectIdentity
companyRMON = _CompanyRMON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47)
)


class _RmonGlobalState_Type(Integer32):
    """Custom type rmonGlobalState based on Integer32"""
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


_RmonGlobalState_Type.__name__ = "Integer32"
_RmonGlobalState_Object = MibScalar
rmonGlobalState = _RmonGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 1),
    _RmonGlobalState_Type()
)
rmonGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonGlobalState.setStatus("current")
_RmonStatistics_ObjectIdentity = ObjectIdentity
rmonStatistics = _RmonStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 2)
)
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 2, 1)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 2, 1, 1)
)
rmonStatsEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "rmonStatsIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 2, 1, 1, 1),
    _RmonStatsIndex_Type()
)
rmonStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsIndex.setStatus("current")
_RmonStatsDataSource_Type = ObjectIdentifier
_RmonStatsDataSource_Object = MibTableColumn
rmonStatsDataSource = _RmonStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 2, 1, 1, 2),
    _RmonStatsDataSource_Type()
)
rmonStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsDataSource.setStatus("current")


class _RmonStatsOwner_Type(OctetString):
    """Custom type rmonStatsOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RmonStatsOwner_Type.__name__ = "OctetString"
_RmonStatsOwner_Object = MibTableColumn
rmonStatsOwner = _RmonStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 2, 1, 1, 3),
    _RmonStatsOwner_Type()
)
rmonStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsOwner.setStatus("current")
_RmonStatsStatus_Type = RmonStatus
_RmonStatsStatus_Object = MibTableColumn
rmonStatsStatus = _RmonStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 2, 1, 1, 4),
    _RmonStatsStatus_Type()
)
rmonStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsStatus.setStatus("current")
_RmonHistory_ObjectIdentity = ObjectIdentity
rmonHistory = _RmonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3)
)
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "rmonHistoryIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")
_RmonHistoryDataSource_Type = ObjectIdentifier
_RmonHistoryDataSource_Object = MibTableColumn
rmonHistoryDataSource = _RmonHistoryDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1, 1, 2),
    _RmonHistoryDataSource_Type()
)
rmonHistoryDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryDataSource.setStatus("current")


class _RmonHistoryBucketsRequested_Type(Integer32):
    """Custom type rmonHistoryBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmonHistoryBucketsRequested_Type.__name__ = "Integer32"
_RmonHistoryBucketsRequested_Object = MibTableColumn
rmonHistoryBucketsRequested = _RmonHistoryBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1, 1, 3),
    _RmonHistoryBucketsRequested_Type()
)
rmonHistoryBucketsRequested.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1, 1, 4),
    _RmonHistoryInterval_Type()
)
rmonHistoryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryInterval.setUnits("Seconds")


class _RmonHistoryOwner_Type(OctetString):
    """Custom type rmonHistoryOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RmonHistoryOwner_Type.__name__ = "OctetString"
_RmonHistoryOwner_Object = MibTableColumn
rmonHistoryOwner = _RmonHistoryOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1, 1, 5),
    _RmonHistoryOwner_Type()
)
rmonHistoryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryOwner.setStatus("current")
_RmonHistoryStatus_Type = RmonStatus
_RmonHistoryStatus_Object = MibTableColumn
rmonHistoryStatus = _RmonHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 3, 1, 1, 6),
    _RmonHistoryStatus_Type()
)
rmonHistoryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryStatus.setStatus("current")
_RmonAlarm_ObjectIdentity = ObjectIdentity
rmonAlarm = _RmonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4)
)
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "rmonAlarmIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")
_RmonAlarmInterval_Type = Integer32
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 2),
    _RmonAlarmInterval_Type()
)
rmonAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    rmonAlarmInterval.setUnits("Seconds")
_RmonAlarmVariable_Type = ObjectIdentifier
_RmonAlarmVariable_Object = MibTableColumn
rmonAlarmVariable = _RmonAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 3),
    _RmonAlarmVariable_Type()
)
rmonAlarmVariable.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")
_RmonAlarmRisingThreshold_Type = Integer32
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 5),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")
_RmonAlarmFallingThreshold_Type = Integer32
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 6),
    _RmonAlarmFallingThreshold_Type()
)
rmonAlarmFallingThreshold.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 7),
    _RmonAlarmRisingEventIndex_Type()
)
rmonAlarmRisingEventIndex.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 8),
    _RmonAlarmFallingEventIndex_Type()
)
rmonAlarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmFallingEventIndex.setStatus("current")


class _RmonAlarmOwner_Type(OctetString):
    """Custom type rmonAlarmOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RmonAlarmOwner_Type.__name__ = "OctetString"
_RmonAlarmOwner_Object = MibTableColumn
rmonAlarmOwner = _RmonAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 9),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")
_RmonAlarmStatus_Type = RmonStatus
_RmonAlarmStatus_Object = MibTableColumn
rmonAlarmStatus = _RmonAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 4, 1, 1, 10),
    _RmonAlarmStatus_Type()
)
rmonAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmStatus.setStatus("current")
_RmonEvent_ObjectIdentity = ObjectIdentity
rmonEvent = _RmonEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5)
)
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1, 1)
)
rmonEventEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "rmonEventIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1, 1, 1),
    _RmonEventIndex_Type()
)
rmonEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonEventIndex.setStatus("current")


class _RmonEventDescription_Type(DisplayString):
    """Custom type rmonEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RmonEventDescription_Type.__name__ = "DisplayString"
_RmonEventDescription_Object = MibTableColumn
rmonEventDescription = _RmonEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1, 1, 2),
    _RmonEventDescription_Type()
)
rmonEventDescription.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1, 1, 3),
    _RmonEventType_Type()
)
rmonEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventType.setStatus("current")


class _RmonEventCommunity_Type(OctetString):
    """Custom type rmonEventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RmonEventCommunity_Type.__name__ = "OctetString"
_RmonEventCommunity_Object = MibTableColumn
rmonEventCommunity = _RmonEventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1, 1, 4),
    _RmonEventCommunity_Type()
)
rmonEventCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventCommunity.setStatus("current")


class _RmonEventOwner_Type(OctetString):
    """Custom type rmonEventOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RmonEventOwner_Type.__name__ = "OctetString"
_RmonEventOwner_Object = MibTableColumn
rmonEventOwner = _RmonEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")
_RmonEventStatus_Type = RmonStatus
_RmonEventStatus_Object = MibTableColumn
rmonEventStatus = _RmonEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 47, 5, 1, 1, 6),
    _RmonEventStatus_Type()
)
rmonEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventStatus.setStatus("current")
_CompanyNeighbor_ObjectIdentity = ObjectIdentity
companyNeighbor = _CompanyNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50)
)
_NeighborTable_Object = MibTable
neighborTable = _NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1)
)
if mibBuilder.loadTexts:
    neighborTable.setStatus("current")
_NeighborEntry_Object = MibTableRow
neighborEntry = _NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1, 1)
)
neighborEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "neighborIfindex"),
    (0, "DGS-1210-20_BX", "neighborIPv6Addr"),
    (0, "DGS-1210-20_BX", "neighborMACAddr"),
)
if mibBuilder.loadTexts:
    neighborEntry.setStatus("current")
_NeighborIfindex_Type = Integer32
_NeighborIfindex_Object = MibTableColumn
neighborIfindex = _NeighborIfindex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1, 1, 1),
    _NeighborIfindex_Type()
)
neighborIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIfindex.setStatus("current")
_NeighborIPv6Addr_Type = Ipv6Address
_NeighborIPv6Addr_Object = MibTableColumn
neighborIPv6Addr = _NeighborIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1, 1, 2),
    _NeighborIPv6Addr_Type()
)
neighborIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIPv6Addr.setStatus("current")
_NeighborMACAddr_Type = MacAddress
_NeighborMACAddr_Object = MibTableColumn
neighborMACAddr = _NeighborMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1, 1, 3),
    _NeighborMACAddr_Type()
)
neighborMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborMACAddr.setStatus("current")


class _NeighborType_Type(Integer32):
    """Custom type neighborType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_NeighborType_Type.__name__ = "Integer32"
_NeighborType_Object = MibTableColumn
neighborType = _NeighborType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1, 1, 4),
    _NeighborType_Type()
)
neighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborType.setStatus("current")


class _NeighborCacheState_Type(Integer32):
    """Custom type neighborCacheState based on Integer32"""
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


_NeighborCacheState_Type.__name__ = "Integer32"
_NeighborCacheState_Object = MibTableColumn
neighborCacheState = _NeighborCacheState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1, 1, 5),
    _NeighborCacheState_Type()
)
neighborCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborCacheState.setStatus("current")
_NeighborRowStatus_Type = RowStatus
_NeighborRowStatus_Object = MibTableColumn
neighborRowStatus = _NeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 50, 1, 1, 7),
    _NeighborRowStatus_Type()
)
neighborRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neighborRowStatus.setStatus("current")
_Companydot3azEEE_ObjectIdentity = ObjectIdentity
companydot3azEEE = _Companydot3azEEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 52)
)
_Dot3azEEEset_ObjectIdentity = ObjectIdentity
dot3azEEEset = _Dot3azEEEset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 52, 1)
)
_Dot3azTable_Object = MibTable
dot3azTable = _Dot3azTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 52, 1, 1)
)
if mibBuilder.loadTexts:
    dot3azTable.setStatus("current")
_Dot3azEntry_Object = MibTableRow
dot3azEntry = _Dot3azEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 52, 1, 1, 1)
)
dot3azEntry.setIndexNames(
    (0, "DGS-1210-20_BX", "portD3Index"),
)
if mibBuilder.loadTexts:
    dot3azEntry.setStatus("current")
_PortD3Index_Type = Integer32
_PortD3Index_Object = MibTableColumn
portD3Index = _PortD3Index_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 52, 1, 1, 1, 1),
    _PortD3Index_Type()
)
portD3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portD3Index.setStatus("current")


class _PortD3State_Type(Integer32):
    """Custom type portD3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_PortD3State_Type.__name__ = "Integer32"
_PortD3State_Object = MibTableColumn
portD3State = _PortD3State_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 52, 1, 1, 1, 2),
    _PortD3State_Type()
)
portD3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portD3State.setStatus("current")
dot1dBasePortEntry.registerAugmentions(
    ("DGS-1210-20_BX",
     "dot1qVlanPortEntry")
)
dot1qVlanPortEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27, 0, 4)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )

firmwareUpgradeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27, 0, 8)
)
if mibBuilder.loadTexts:
    firmwareUpgradeSuccess.setStatus(
        "current"
    )

firmwareUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27, 0, 9)
)
if mibBuilder.loadTexts:
    firmwareUpgradeFailure.setStatus(
        "current"
    )

firmwareIllegalFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27, 0, 10)
)
if mibBuilder.loadTexts:
    firmwareIllegalFile.setStatus(
        "current"
    )

firmwareTransferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27, 0, 11)
)
if mibBuilder.loadTexts:
    firmwareTransferError.setStatus(
        "current"
    )

firmwareChecksumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 14, 27, 0, 12)
)
if mibBuilder.loadTexts:
    firmwareChecksumError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-1210-20_BX",
    **{"VlanIndex": VlanIndex,
       "PortList": PortList,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "RmonStatus": RmonStatus,
       "LldpManAddress": LldpManAddress,
       "Ipv6Address": Ipv6Address,
       "PortLaMode": PortLaMode,
       "LacpKey": LacpKey,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DGS12XXSeriesProd": dlink_DGS12XXSeriesProd,
       "dgs-1210-20bx": dgs_1210_20bx,
       "companySystem": companySystem,
       "sysSwitchName": sysSwitchName,
       "sysHardwareVersion": sysHardwareVersion,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysLoginTimeoutInterval": sysLoginTimeoutInterval,
       "sysLocationName": sysLocationName,
       "sysGroupInterval": sysGroupInterval,
       "sysSystemPassword": sysSystemPassword,
       "sysSafeGuardEnable": sysSafeGuardEnable,
       "sysRestart": sysRestart,
       "sysSave": sysSave,
       "sysJumboFrameEnable": sysJumboFrameEnable,
       "sysPortCtrlTable": sysPortCtrlTable,
       "sysPortCtrlEntry": sysPortCtrlEntry,
       "sysPortCtrlIndex": sysPortCtrlIndex,
       "sysPortCtrlSpeed": sysPortCtrlSpeed,
       "sysPortCtrlOperStatus": sysPortCtrlOperStatus,
       "sysPortCtrlMDI": sysPortCtrlMDI,
       "sysPortCtrlFlowControl": sysPortCtrlFlowControl,
       "sysPortCtrlFlowControlOper": sysPortCtrlFlowControlOper,
       "sysPortCtrlType": sysPortCtrlType,
       "sysDhcpAutoConfiguration": sysDhcpAutoConfiguration,
       "companyIpifGroup": companyIpifGroup,
       "ipv4sysIpAddrCfgMode": ipv4sysIpAddrCfgMode,
       "ipv4sysIpAddr": ipv4sysIpAddr,
       "ipv4sysIpSubnetMask": ipv4sysIpSubnetMask,
       "ipv4sysGateway": ipv4sysGateway,
       "ipifSupportV4V6Info": ipifSupportV4V6Info,
       "sysIpAddrCfgMode": sysIpAddrCfgMode,
       "sysIpAddr": sysIpAddr,
       "sysIpSubnetMask": sysIpSubnetMask,
       "sysGateway": sysGateway,
       "ipifName": ipifName,
       "ipifv6GlobalStatus": ipifv6GlobalStatus,
       "ipifv6DHCPStatus": ipifv6DHCPStatus,
       "ipifv6AutolinkloStatus": ipifv6AutolinkloStatus,
       "ipifv6NSRetransmitTime": ipifv6NSRetransmitTime,
       "ipifv6DefaultGateway": ipifv6DefaultGateway,
       "ipifV6AddressTable": ipifV6AddressTable,
       "ipifV6AddressEntry": ipifV6AddressEntry,
       "ipifV6AddressMainIndex": ipifV6AddressMainIndex,
       "ipifV6AddressIpAddr": ipifV6AddressIpAddr,
       "ipifV6AddressIpPrefix": ipifV6AddressIpPrefix,
       "ipifV6AddressIpType": ipifV6AddressIpType,
       "ipifV6AddressRowStatus": ipifV6AddressRowStatus,
       "companyTftpGroup": companyTftpGroup,
       "tftpFwServerIpAddress": tftpFwServerIpAddress,
       "tftpFwImageFileName": tftpFwImageFileName,
       "tftpFwTftpOperation": tftpFwTftpOperation,
       "tftpFwTftpOperationStatus": tftpFwTftpOperationStatus,
       "tftpCfgServerIpAddress": tftpCfgServerIpAddress,
       "tftpConfigFileName": tftpConfigFileName,
       "tftpConfigTftpOperation": tftpConfigTftpOperation,
       "tftpConfigTftpOperationStatus": tftpConfigTftpOperationStatus,
       "tftpFwTargetGroup": tftpFwTargetGroup,
       "tftpFwTargetServerIpAddress": tftpFwTargetServerIpAddress,
       "tftpFwTargetServerIpType": tftpFwTargetServerIpType,
       "tftpFwTargetInterfaceName": tftpFwTargetInterfaceName,
       "tftpFwTargetImageFileName": tftpFwTargetImageFileName,
       "tftpFwTargetTftpOperation": tftpFwTargetTftpOperation,
       "tftpFwTargetTftpOperationStatus": tftpFwTargetTftpOperationStatus,
       "tftpCfgTargetGroup": tftpCfgTargetGroup,
       "tftpCfgTargetServerIpAddress": tftpCfgTargetServerIpAddress,
       "tftpCfgTargetServerIpType": tftpCfgTargetServerIpType,
       "tftpCfgTargetInterfaceName": tftpCfgTargetInterfaceName,
       "tftpCfgTargetImageFileName": tftpCfgTargetImageFileName,
       "tftpCfgTargetTftpOperation": tftpCfgTargetTftpOperation,
       "tftpCfgTargetTftpOperationStatus": tftpCfgTargetTftpOperationStatus,
       "companyMiscGroup": companyMiscGroup,
       "miscReset": miscReset,
       "miscStatisticsReset": miscStatisticsReset,
       "companyRSTP": companyRSTP,
       "stpGlobal": stpGlobal,
       "rstpStatus": rstpStatus,
       "stpVersion": stpVersion,
       "stpPriority": stpPriority,
       "stpTxHoldCount": stpTxHoldCount,
       "stpProtocolSpecification": stpProtocolSpecification,
       "stpTimeSinceTopologyChange": stpTimeSinceTopologyChange,
       "stpTopChanges": stpTopChanges,
       "stpDesignatedRoot": stpDesignatedRoot,
       "stpRootCost": stpRootCost,
       "stpRootPort": stpRootPort,
       "stpMaxAge": stpMaxAge,
       "stpHelloTime": stpHelloTime,
       "stpHoldTime": stpHoldTime,
       "stpForwardDelay": stpForwardDelay,
       "stpBridgeMaxAge": stpBridgeMaxAge,
       "stpBridgeHelloTime": stpBridgeHelloTime,
       "stpBridgeForwardDelay": stpBridgeForwardDelay,
       "stpPortTable": stpPortTable,
       "stpPortEntry": stpPortEntry,
       "stpPort": stpPort,
       "stpPortPriority": stpPortPriority,
       "stpPortState": stpPortState,
       "stpPortEnable": stpPortEnable,
       "stpAdminPortPathCost": stpAdminPortPathCost,
       "stpPortPathCost": stpPortPathCost,
       "stpPortDesignatedRoot": stpPortDesignatedRoot,
       "stpPortDesignatedCost": stpPortDesignatedCost,
       "stpPortDesignatedBridge": stpPortDesignatedBridge,
       "stpPortDesignatedPort": stpPortDesignatedPort,
       "stpPortForwardTransitions": stpPortForwardTransitions,
       "stpPortProtocolMigration": stpPortProtocolMigration,
       "stpPortOperEdgePort": stpPortOperEdgePort,
       "stpPortAdminPointToPoint": stpPortAdminPointToPoint,
       "stpPortOperPointToPoint": stpPortOperPointToPoint,
       "stpPortEdge": stpPortEdge,
       "stpPortRestrictedRole": stpPortRestrictedRole,
       "stpPortRestrictedTCN": stpPortRestrictedTCN,
       "companyDot1qVlanGroup": companyDot1qVlanGroup,
       "dot1qVlanManagementOnOff": dot1qVlanManagementOnOff,
       "dot1qVlanManagementid": dot1qVlanManagementid,
       "dot1qVlanAsyOnOff": dot1qVlanAsyOnOff,
       "dot1qVlanTable": dot1qVlanTable,
       "dot1qVlanEntry": dot1qVlanEntry,
       "dot1qVlanName": dot1qVlanName,
       "dot1qVlanEgressPorts": dot1qVlanEgressPorts,
       "dot1qVlanUntaggedPorts": dot1qVlanUntaggedPorts,
       "dot1qVlanRowStatus": dot1qVlanRowStatus,
       "dot1qVlanPortTable": dot1qVlanPortTable,
       "dot1qVlanPortEntry": dot1qVlanPortEntry,
       "dot1qVlanPvid": dot1qVlanPvid,
       "dot1qVlanUngisterMCFilterTable": dot1qVlanUngisterMCFilterTable,
       "dot1qVlanUngisterMCFilterEntry": dot1qVlanUngisterMCFilterEntry,
       "dot1qVlanUngisterMCFilterVlanId": dot1qVlanUngisterMCFilterVlanId,
       "dot1qVlanUngisterMCFiltermode": dot1qVlanUngisterMCFiltermode,
       "companyLA": companyLA,
       "laSystem": laSystem,
       "laStatus": laStatus,
       "laPortChannelTable": laPortChannelTable,
       "laPortChannelEntry": laPortChannelEntry,
       "laPortChannelIfIndex": laPortChannelIfIndex,
       "laPortChannelMemberList": laPortChannelMemberList,
       "laPortChannelMode": laPortChannelMode,
       "laPortControl": laPortControl,
       "laPortControlTable": laPortControlTable,
       "laPortControlEntry": laPortControlEntry,
       "laPortControlIndex": laPortControlIndex,
       "laPortActorActivity": laPortActorActivity,
       "laPortActorTimeout": laPortActorTimeout,
       "companyStaticMAC": companyStaticMAC,
       "staticDisableAutoLearn": staticDisableAutoLearn,
       "staticAutoLearningList": staticAutoLearningList,
       "staticTable": staticTable,
       "staticEntry": staticEntry,
       "staticVlanID": staticVlanID,
       "staticMac": staticMac,
       "staticPort": staticPort,
       "staticStatus": staticStatus,
       "companyIgsGroup": companyIgsGroup,
       "igsSystem": igsSystem,
       "igsStatus": igsStatus,
       "igsRouterPortPurgeInterval": igsRouterPortPurgeInterval,
       "igsHostPortPurgeInterval": igsHostPortPurgeInterval,
       "igsRobustnessValue": igsRobustnessValue,
       "igsGrpQueryInterval": igsGrpQueryInterval,
       "igsQueryInterval": igsQueryInterval,
       "igsQueryMaxResponseTime": igsQueryMaxResponseTime,
       "igsReportToAllPort": igsReportToAllPort,
       "igsVlan": igsVlan,
       "igsVlanRouterTable": igsVlanRouterTable,
       "igsVlanRouterEntry": igsVlanRouterEntry,
       "igsVlanRouterVlanId": igsVlanRouterVlanId,
       "igsVlanRouterPortList": igsVlanRouterPortList,
       "igsVlanFilterTable": igsVlanFilterTable,
       "igsVlanFilterEntry": igsVlanFilterEntry,
       "igsVlanFilterVlanId": igsVlanFilterVlanId,
       "igsVlanSnoopStatus": igsVlanSnoopStatus,
       "igsVlanQuerier": igsVlanQuerier,
       "igsVlanCfgQuerier": igsVlanCfgQuerier,
       "igsVlanQueryInterval": igsVlanQueryInterval,
       "igsVlanRtrPortList": igsVlanRtrPortList,
       "igsVlanFastLeave": igsVlanFastLeave,
       "igsVlanMulticastGroupTable": igsVlanMulticastGroupTable,
       "igsVlanMulticastGroupEntry": igsVlanMulticastGroupEntry,
       "igsVlanMulticastGroupVlanId": igsVlanMulticastGroupVlanId,
       "igsVlanMulticastGroupIpAddress": igsVlanMulticastGroupIpAddress,
       "igsVlanMulticastGroupMacAddress": igsVlanMulticastGroupMacAddress,
       "igsVlanMulticastGroupPortList": igsVlanMulticastGroupPortList,
       "companyDot1xGroup": companyDot1xGroup,
       "radius": radius,
       "ipv4radiusServerAddress": ipv4radiusServerAddress,
       "ipv4radiusServerSharedSecret": ipv4radiusServerSharedSecret,
       "radiusServerTable": radiusServerTable,
       "swRadiusServerIPType": swRadiusServerIPType,
       "swRadiusServerAddress": swRadiusServerAddress,
       "swRadiusServerInterfaceName": swRadiusServerInterfaceName,
       "swRadiusServerSharedSecret": swRadiusServerSharedSecret,
       "dot1xAuth": dot1xAuth,
       "dot1xAuthStatus": dot1xAuthStatus,
       "dot1xAuthQuietPeriod": dot1xAuthQuietPeriod,
       "dot1xAuthTxPeriod": dot1xAuthTxPeriod,
       "dot1xAuthSuppTimeout": dot1xAuthSuppTimeout,
       "dot1xAuthServerTimeout": dot1xAuthServerTimeout,
       "dot1xAuthMaxReq": dot1xAuthMaxReq,
       "dot1xAuthReAuthPeriod": dot1xAuthReAuthPeriod,
       "dot1xAuthReAuthEnabled": dot1xAuthReAuthEnabled,
       "dot1xAuthConfigPortTable": dot1xAuthConfigPortTable,
       "dot1xAuthConfigPortEntry": dot1xAuthConfigPortEntry,
       "dot1xAuthConfigPortNumber": dot1xAuthConfigPortNumber,
       "dot1xAuthConfigPortControl": dot1xAuthConfigPortControl,
       "dot1xAuthConfigPortStatus": dot1xAuthConfigPortStatus,
       "dot1xAuthConfigPortSessionTime": dot1xAuthConfigPortSessionTime,
       "dot1xAuthConfigPortSessionUserName": dot1xAuthConfigPortSessionUserName,
       "companyQoSGroup": companyQoSGroup,
       "qosMode": qosMode,
       "queuingMechanism": queuingMechanism,
       "qosQ1p": qosQ1p,
       "dot1pPortTable": dot1pPortTable,
       "dot1pPortEntry": dot1pPortEntry,
       "dot1pPortIndex": dot1pPortIndex,
       "dot1pPortPriority": dot1pPortPriority,
       "qosDiffServ": qosDiffServ,
       "qosDiffServEnable": qosDiffServEnable,
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
       "qosTOS": qosTOS,
       "qosTOSEnable": qosTOSEnable,
       "qosTOSGroup": qosTOSGroup,
       "qosTOSType00": qosTOSType00,
       "qosTOSType01": qosTOSType01,
       "qosTOSType02": qosTOSType02,
       "qosTOSType03": qosTOSType03,
       "qosTOSType04": qosTOSType04,
       "qosTOSType05": qosTOSType05,
       "qosTOSType06": qosTOSType06,
       "qosTOSType07": qosTOSType07,
       "qosAclPrioritySettings": qosAclPrioritySettings,
       "aclQosTable": aclQosTable,
       "aclQosEntry": aclQosEntry,
       "aclQosIndex": aclQosIndex,
       "aclQosType": aclQosType,
       "aclQosTCPUDPPort": aclQosTCPUDPPort,
       "aclQosIP6TC": aclQosIP6TC,
       "aclQosAssignPriority": aclQosAssignPriority,
       "aclQosStatus": aclQosStatus,
       "companyTrafficMgmt": companyTrafficMgmt,
       "bandwidthCtrlSettings": bandwidthCtrlSettings,
       "bandwidthCtrlTable": bandwidthCtrlTable,
       "bandwidthCtrlEntry": bandwidthCtrlEntry,
       "bandwidthCtrlIndex": bandwidthCtrlIndex,
       "bandwidthCtrlTxThreshold": bandwidthCtrlTxThreshold,
       "bandwidthCtrlRxThreshold": bandwidthCtrlRxThreshold,
       "broadcastStormCtrlSettings": broadcastStormCtrlSettings,
       "broadcastStormCtrlGlobalOnOff": broadcastStormCtrlGlobalOnOff,
       "broadcastStormCtrlLimitType": broadcastStormCtrlLimitType,
       "broadcastStormCtrlThreshold": broadcastStormCtrlThreshold,
       "companySecurity": companySecurity,
       "securityTrustedHost": securityTrustedHost,
       "trustedHostStatus": trustedHostStatus,
       "ipv4trustedHostTable": ipv4trustedHostTable,
       "ipv4trustedHostEntry": ipv4trustedHostEntry,
       "ipv4trustedHostIpAddr": ipv4trustedHostIpAddr,
       "ipv4trustedHostIpMask": ipv4trustedHostIpMask,
       "ipv4trustedHostRowStatus": ipv4trustedHostRowStatus,
       "trustedHostTable": trustedHostTable,
       "trustedHostEntry": trustedHostEntry,
       "trustedHostIPType": trustedHostIPType,
       "trustedHostIpAddr": trustedHostIpAddr,
       "trustedHostIpMask": trustedHostIpMask,
       "trustedHostRowStatus": trustedHostRowStatus,
       "securityPortSecurity": securityPortSecurity,
       "portSecTable": portSecTable,
       "portSecEntry": portSecEntry,
       "portSecIndex": portSecIndex,
       "portSecState": portSecState,
       "portSecMLA": portSecMLA,
       "securityARPSpoofPrevent": securityARPSpoofPrevent,
       "aRPSpoofPreventTable": aRPSpoofPreventTable,
       "aRPSpoofPreventEntry": aRPSpoofPreventEntry,
       "aRPSpoofPreventIpAddr": aRPSpoofPreventIpAddr,
       "aRPSpoofPreventMacAddress": aRPSpoofPreventMacAddress,
       "aRPSpoofPreventPortList": aRPSpoofPreventPortList,
       "aRPSpoofPreventRowStatus": aRPSpoofPreventRowStatus,
       "securitySSL": securitySSL,
       "sslSecurityHttpStatus": sslSecurityHttpStatus,
       "sslCiphers": sslCiphers,
       "sslCipherSuiteList": sslCipherSuiteList,
       "securityDhcpServerScreen": securityDhcpServerScreen,
       "dhcpServerScreenEnablePortlist": dhcpServerScreenEnablePortlist,
       "ipv4dhcpServerScreenServerTable": ipv4dhcpServerScreenServerTable,
       "ipv4dhcpServerScreenServerEntry": ipv4dhcpServerScreenServerEntry,
       "ipv4dhcpServerScreenServerIndex": ipv4dhcpServerScreenServerIndex,
       "ipv4dhcpServerScreenServerAddress": ipv4dhcpServerScreenServerAddress,
       "ipv4dhcpServerScreenServerStatus": ipv4dhcpServerScreenServerStatus,
       "dhcpServerScreenTrustedServerTable": dhcpServerScreenTrustedServerTable,
       "dhcpServerScreenTrustedServerEntry": dhcpServerScreenTrustedServerEntry,
       "dhcpServerScreenTrustedServerIndex": dhcpServerScreenTrustedServerIndex,
       "dhcpServerScreenTrustedServerAddress": dhcpServerScreenTrustedServerAddress,
       "dhcpServerScreenIPType": dhcpServerScreenIPType,
       "dhcpServerScreenTrustedServerStatus": dhcpServerScreenTrustedServerStatus,
       "securityTrafficSeg": securityTrafficSeg,
       "trafficSegStatus": trafficSegStatus,
       "trafficSegTable": trafficSegTable,
       "trafficSegEntry": trafficSegEntry,
       "trafficSegIfIndex": trafficSegIfIndex,
       "trafficSegMemberList": trafficSegMemberList,
       "securityIpMacPortBinding": securityIpMacPortBinding,
       "impbSettingTable": impbSettingTable,
       "impbSettingEntry": impbSettingEntry,
       "impbPortIndex": impbPortIndex,
       "impbPortState": impbPortState,
       "impbInsIpPacPortState": impbInsIpPacPortState,
       "impbDHCPPortState": impbDHCPPortState,
       "impbSmartTable": impbSmartTable,
       "impbSmartEntry": impbSmartEntry,
       "impbSmartMacAddress": impbSmartMacAddress,
       "impbSmartPort": impbSmartPort,
       "impbSmartIpAddress": impbSmartIpAddress,
       "impbSmartVlanId": impbSmartVlanId,
       "impbSmartBinding": impbSmartBinding,
       "impbWhiteListTable": impbWhiteListTable,
       "impbWhiteListEntry": impbWhiteListEntry,
       "impbWhiteListIpAddress": impbWhiteListIpAddress,
       "impbWhiteListMacAddress": impbWhiteListMacAddress,
       "impbWhiteListPort": impbWhiteListPort,
       "impbWhiteListRowStatus": impbWhiteListRowStatus,
       "impbBlackListTable": impbBlackListTable,
       "impbBlackListEntry": impbBlackListEntry,
       "impbBlackListMacAddress": impbBlackListMacAddress,
       "impbBlackListVlanId": impbBlackListVlanId,
       "impbBlackListPort": impbBlackListPort,
       "impbBlackListIpAddress": impbBlackListIpAddress,
       "impbBlackListStatus": impbBlackListStatus,
       "impbAutoScanIpAddressFrom": impbAutoScanIpAddressFrom,
       "impbAutoScanIpAddressTo": impbAutoScanIpAddressTo,
       "impbAutoScanStatus": impbAutoScanStatus,
       "companyACLGroup": companyACLGroup,
       "aclProfile": aclProfile,
       "ipv4aclProfileTable": ipv4aclProfileTable,
       "ipv4aclProfileEntry": ipv4aclProfileEntry,
       "ipv4aclProfileNo": ipv4aclProfileNo,
       "ipv4aclProfileType": ipv4aclProfileType,
       "ipv4aclProfileRuleCount": ipv4aclProfileRuleCount,
       "ipv4aclProfileMask": ipv4aclProfileMask,
       "ipv4aclProfileDstMacAddrMask": ipv4aclProfileDstMacAddrMask,
       "ipv4aclProfileSrcMacAddrMask": ipv4aclProfileSrcMacAddrMask,
       "ipv4aclProfileIPProtocol": ipv4aclProfileIPProtocol,
       "ipv4aclProfileDstIpAddrMask": ipv4aclProfileDstIpAddrMask,
       "ipv4aclProfileSrcIpAddrMask": ipv4aclProfileSrcIpAddrMask,
       "ipv4aclProfileDstPortMask": ipv4aclProfileDstPortMask,
       "ipv4aclProfileSrcPortMask": ipv4aclProfileSrcPortMask,
       "ipv4aclProfileArpSenderMacAddrMask": ipv4aclProfileArpSenderMacAddrMask,
       "ipv4aclProfileArpSenderIpAddrMask": ipv4aclProfileArpSenderIpAddrMask,
       "ipv4aclProfileStatus": ipv4aclProfileStatus,
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileNo": aclProfileNo,
       "aclProfileType": aclProfileType,
       "aclProfileRuleCount": aclProfileRuleCount,
       "aclProfileMask": aclProfileMask,
       "aclProfileDstMacAddrMask": aclProfileDstMacAddrMask,
       "aclProfileSrcMacAddrMask": aclProfileSrcMacAddrMask,
       "aclProfileIPProtocol": aclProfileIPProtocol,
       "aclProfileDstIpAddrMaskType": aclProfileDstIpAddrMaskType,
       "aclProfileDstIpAddrMask": aclProfileDstIpAddrMask,
       "aclProfileSrcIpAddrMaskType": aclProfileSrcIpAddrMaskType,
       "aclProfileSrcIpAddrMask": aclProfileSrcIpAddrMask,
       "aclProfileDstPortMask": aclProfileDstPortMask,
       "aclProfileSrcPortMask": aclProfileSrcPortMask,
       "aclProfileArpSenderMacAddrMask": aclProfileArpSenderMacAddrMask,
       "aclProfileArpSenderIpAddrMask": aclProfileArpSenderIpAddrMask,
       "aclProfileStatus": aclProfileStatus,
       "aclL2Rule": aclL2Rule,
       "aclL2RuleTable": aclL2RuleTable,
       "aclL2RuleEntry": aclL2RuleEntry,
       "aclL2AccessID": aclL2AccessID,
       "aclL2ProfileID": aclL2ProfileID,
       "aclL2RuleEtherType": aclL2RuleEtherType,
       "aclL2RuleDstMacAddr": aclL2RuleDstMacAddr,
       "aclL2RuleSrcMacAddr": aclL2RuleSrcMacAddr,
       "aclL2RuleVlanId": aclL2RuleVlanId,
       "aclL2Rule1pPriority": aclL2Rule1pPriority,
       "aclL2RuleDstMacAddrMask": aclL2RuleDstMacAddrMask,
       "aclL2RuleSrcMacAddrMask": aclL2RuleSrcMacAddrMask,
       "aclL2RuleInPortList": aclL2RuleInPortList,
       "aclL2RuleAction": aclL2RuleAction,
       "aclL2RuleStatus": aclL2RuleStatus,
       "aclL3Rule": aclL3Rule,
       "aclL3RuleTable": aclL3RuleTable,
       "aclL3RuleEntry": aclL3RuleEntry,
       "aclL3RuleAccessID": aclL3RuleAccessID,
       "aclL3RuleProfileNo": aclL3RuleProfileNo,
       "aclL3RuleProtocol": aclL3RuleProtocol,
       "aclL3RuleICMPMessageType": aclL3RuleICMPMessageType,
       "aclL3RuleICMPMessageCode": aclL3RuleICMPMessageCode,
       "aclL3RuleDstIpAddr": aclL3RuleDstIpAddr,
       "aclL3RuleSrcIpAddr": aclL3RuleSrcIpAddr,
       "aclL3RuleDstIpAddrMask": aclL3RuleDstIpAddrMask,
       "aclL3RuleSrcIpAddrMask": aclL3RuleSrcIpAddrMask,
       "aclL3RuleTcpUdpDstPort": aclL3RuleTcpUdpDstPort,
       "aclL3RuleTcpUdpSrcPort": aclL3RuleTcpUdpSrcPort,
       "aclL3RuleTcpUdpDstPortMask": aclL3RuleTcpUdpDstPortMask,
       "aclL3RuleTcpUdpSrcPortMask": aclL3RuleTcpUdpSrcPortMask,
       "aclL3RuleTcpAckBit": aclL3RuleTcpAckBit,
       "aclL3RuleTcpRstBit": aclL3RuleTcpRstBit,
       "aclL3RuleTcpUrgBit": aclL3RuleTcpUrgBit,
       "aclL3RuleTcpPshBit": aclL3RuleTcpPshBit,
       "aclL3RuleTcpSynBit": aclL3RuleTcpSynBit,
       "aclL3RuleTcpFinBit": aclL3RuleTcpFinBit,
       "aclL3RuleDscp": aclL3RuleDscp,
       "aclL3RuleIgmpType": aclL3RuleIgmpType,
       "aclL3RulePortList": aclL3RulePortList,
       "aclL3RuleAction": aclL3RuleAction,
       "aclL3RuleStatus": aclL3RuleStatus,
       "aclv6L3RuleTable": aclv6L3RuleTable,
       "aclv6L3RuleEntry": aclv6L3RuleEntry,
       "aclv6L3RuleAccessID": aclv6L3RuleAccessID,
       "aclv6L3RuleProfileNo": aclv6L3RuleProfileNo,
       "aclv6L3RuleProtocol": aclv6L3RuleProtocol,
       "aclv6L3RuleICMPMessageType": aclv6L3RuleICMPMessageType,
       "aclv6L3RuleICMPMessageCode": aclv6L3RuleICMPMessageCode,
       "aclv6L3RuleDstIpAddr": aclv6L3RuleDstIpAddr,
       "aclv6L3RuleSrcIpAddr": aclv6L3RuleSrcIpAddr,
       "aclv6L3RuleDstIpAddrMask": aclv6L3RuleDstIpAddrMask,
       "aclv6L3RuleSrcIpAddrMask": aclv6L3RuleSrcIpAddrMask,
       "aclv6L3RuleTcpUdpDstPort": aclv6L3RuleTcpUdpDstPort,
       "aclv6L3RuleTcpUdpSrcPort": aclv6L3RuleTcpUdpSrcPort,
       "aclv6L3RuleTcpUdpDstPortMask": aclv6L3RuleTcpUdpDstPortMask,
       "aclv6L3RuleTcpUdpSrcPortMask": aclv6L3RuleTcpUdpSrcPortMask,
       "aclv6L3RuleTcpAckBit": aclv6L3RuleTcpAckBit,
       "aclv6L3RuleTcpRstBit": aclv6L3RuleTcpRstBit,
       "aclv6L3RuleTcpUrgBit": aclv6L3RuleTcpUrgBit,
       "aclv6L3RuleTcpPshBit": aclv6L3RuleTcpPshBit,
       "aclv6L3RuleTcpSynBit": aclv6L3RuleTcpSynBit,
       "aclv6L3RuleTcpFinBit": aclv6L3RuleTcpFinBit,
       "aclv6L3RuleTrafficClass": aclv6L3RuleTrafficClass,
       "aclv6L3RulePortList": aclv6L3RulePortList,
       "aclv6L3RuleAction": aclv6L3RuleAction,
       "aclv6L3RuleStatus": aclv6L3RuleStatus,
       "companySyslog": companySyslog,
       "ipv4syslogGeneralGroup": ipv4syslogGeneralGroup,
       "ipv4syslogLogSrvAddr": ipv4syslogLogSrvAddr,
       "ipv4syslogUDPPort": ipv4syslogUDPPort,
       "ipv4syslogTimeStamp": ipv4syslogTimeStamp,
       "ipv4syslogSeverity": ipv4syslogSeverity,
       "ipv4syslogFacility": ipv4syslogFacility,
       "ipv4syslogLogging": ipv4syslogLogging,
       "syslogGeneralGroup": syslogGeneralGroup,
       "syslogState": syslogState,
       "syslogTimeStampOption": syslogTimeStampOption,
       "syslogSrvSeverity": syslogSrvSeverity,
       "syslogSrvFacility": syslogSrvFacility,
       "syslogSrvTable": syslogSrvTable,
       "syslogSrvEntry": syslogSrvEntry,
       "syslogSrvIPType": syslogSrvIPType,
       "syslogSrvIP": syslogSrvIP,
       "syslogSrvPort": syslogSrvPort,
       "syslogInterfaceName": syslogInterfaceName,
       "syslogSrvRowStatus": syslogSrvRowStatus,
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
       "companyMirror": companyMirror,
       "sysMirrorStatus": sysMirrorStatus,
       "sysMirrorTargetPort": sysMirrorTargetPort,
       "sysMirrorCtrlIngressMirroring": sysMirrorCtrlIngressMirroring,
       "sysMirrorCtrlEgressMirroring": sysMirrorCtrlEgressMirroring,
       "companyTrapSetting": companyTrapSetting,
       "sysTrapIP": sysTrapIP,
       "sysTrapSystemEvent": sysTrapSystemEvent,
       "sysTrapPortEvent": sysTrapPortEvent,
       "sysTrapStateChangeEvent": sysTrapStateChangeEvent,
       "sysTrapFirmUpgradeEvent": sysTrapFirmUpgradeEvent,
       "sysTrapStatus": sysTrapStatus,
       "companySNTPSetting": companySNTPSetting,
       "ipv4sysSNTPTimeSeconds": ipv4sysSNTPTimeSeconds,
       "ipv4sysSNTPFirstServer": ipv4sysSNTPFirstServer,
       "ipv4sysSNTPSecondServer": ipv4sysSNTPSecondServer,
       "ipv4sysSNTPPollInterval": ipv4sysSNTPPollInterval,
       "ipv4sysSNTPState": ipv4sysSNTPState,
       "ipv4sysSNTPDSTOffset": ipv4sysSNTPDSTOffset,
       "ipv4sysSNTPGMTMinutes": ipv4sysSNTPGMTMinutes,
       "ipv4sysSNTPDSTStartMon": ipv4sysSNTPDSTStartMon,
       "ipv4sysSNTPDSTStartDay": ipv4sysSNTPDSTStartDay,
       "ipv4sysSNTPDSTStartHour": ipv4sysSNTPDSTStartHour,
       "ipv4sysSNTPDSTStartMin": ipv4sysSNTPDSTStartMin,
       "ipv4sysSNTPDSTEndMon": ipv4sysSNTPDSTEndMon,
       "ipv4sysSNTPDSTEndDay": ipv4sysSNTPDSTEndDay,
       "ipv4sysSNTPDSTEndHour": ipv4sysSNTPDSTEndHour,
       "ipv4sysSNTPDSTEndMin": ipv4sysSNTPDSTEndMin,
       "ipv4sysSNTPDSTState": ipv4sysSNTPDSTState,
       "sysSNTPServerTable": sysSNTPServerTable,
       "sysSNTPTimeSeconds": sysSNTPTimeSeconds,
       "sysSNTPFirstServer": sysSNTPFirstServer,
       "sysSNTPFirstType": sysSNTPFirstType,
       "sysSNTPFirstInterfaceName": sysSNTPFirstInterfaceName,
       "sysSNTPSecondServer": sysSNTPSecondServer,
       "sysSNTPSecondType": sysSNTPSecondType,
       "sysSNTPSecondInterfaceName": sysSNTPSecondInterfaceName,
       "sysSNTPPollInterval": sysSNTPPollInterval,
       "sysSNTPState": sysSNTPState,
       "sysSNTPDSTOffset": sysSNTPDSTOffset,
       "sysSNTPGMTMinutes": sysSNTPGMTMinutes,
       "sysSNTPDSTStartMon": sysSNTPDSTStartMon,
       "sysSNTPDSTStartDay": sysSNTPDSTStartDay,
       "sysSNTPDSTStartHour": sysSNTPDSTStartHour,
       "sysSNTPDSTStartMin": sysSNTPDSTStartMin,
       "sysSNTPDSTEndMon": sysSNTPDSTEndMon,
       "sysSNTPDSTEndDay": sysSNTPDSTEndDay,
       "sysSNTPDSTEndHour": sysSNTPDSTEndHour,
       "sysSNTPDSTEndMin": sysSNTPDSTEndMin,
       "sysSNTPDSTState": sysSNTPDSTState,
       "companyVoiceVlan": companyVoiceVlan,
       "voicevlanSystem": voicevlanSystem,
       "voiceVlanMode": voiceVlanMode,
       "voiceVlanId": voiceVlanId,
       "voiceVlanTimeout": voiceVlanTimeout,
       "voiceVlanPriority": voiceVlanPriority,
       "voicevlanPortControlTable": voicevlanPortControlTable,
       "voicevlanPortControlEntry": voicevlanPortControlEntry,
       "voicevlanPortControlIndex": voicevlanPortControlIndex,
       "voicevlanPortAutoDetection": voicevlanPortAutoDetection,
       "voicevlanPortManuTagMode": voicevlanPortManuTagMode,
       "voicevlanPortCurrentTagMode": voicevlanPortCurrentTagMode,
       "voicevlanPortState": voicevlanPortState,
       "voicevlanOUI": voicevlanOUI,
       "voicevlanOUITable": voicevlanOUITable,
       "voicevlanOUIEntry": voicevlanOUIEntry,
       "voicevlanOUITelephonyOUI": voicevlanOUITelephonyOUI,
       "voicevlanOUIDescription": voicevlanOUIDescription,
       "voicevlanOUIMask": voicevlanOUIMask,
       "voicevlanOUIStatus": voicevlanOUIStatus,
       "voicevlanDevice": voicevlanDevice,
       "voicevlanDeviceTable": voicevlanDeviceTable,
       "voicevlanDeviceEntry": voicevlanDeviceEntry,
       "voicevlanDeviceIndexMac": voicevlanDeviceIndexMac,
       "voicevlanDevicePort": voicevlanDevicePort,
       "voicevlanDevicePriority": voicevlanDevicePriority,
       "voicevlanDeviceTagType": voicevlanDeviceTagType,
       "voicevlanDeviceStatus": voicevlanDeviceStatus,
       "companyLLDPSetting": companyLLDPSetting,
       "dlinklldpState": dlinklldpState,
       "dlinklldpMsgHoldMultiplier": dlinklldpMsgHoldMultiplier,
       "dlinklldpMsgTxInterval": dlinklldpMsgTxInterval,
       "dlinklldpReinitDelay": dlinklldpReinitDelay,
       "dlinklldpTxDelay": dlinklldpTxDelay,
       "dlinklldpConfigManAddrTable": dlinklldpConfigManAddrTable,
       "dlinklldpConfigManAddrEntry": dlinklldpConfigManAddrEntry,
       "dlinklldpLocManAddrSubtype": dlinklldpLocManAddrSubtype,
       "dlinklldpLocManAddr": dlinklldpLocManAddr,
       "dlinklldpConfigManAddrPortsTxEnable": dlinklldpConfigManAddrPortsTxEnable,
       "companySNMPV3": companySNMPV3,
       "snmpGlobalState": snmpGlobalState,
       "snmpV3User": snmpV3User,
       "snmpV3UserTable": snmpV3UserTable,
       "snmpV3UserEntry": snmpV3UserEntry,
       "snmpV3UserName": snmpV3UserName,
       "snmpV3UserVersion": snmpV3UserVersion,
       "snmpV3UserGroupName": snmpV3UserGroupName,
       "snmpV3UserAuthProtocol": snmpV3UserAuthProtocol,
       "snmpV3UserAuthProtocolPassword": snmpV3UserAuthProtocolPassword,
       "snmpV3UserPrivProtocol": snmpV3UserPrivProtocol,
       "snmpV3UserPrivProtocolPassword": snmpV3UserPrivProtocolPassword,
       "snmpV3UserStatus": snmpV3UserStatus,
       "snmpV3Group": snmpV3Group,
       "snmpV3GroupTable": snmpV3GroupTable,
       "snmpV3GroupEntry": snmpV3GroupEntry,
       "snmpV3GroupName": snmpV3GroupName,
       "snmpV3GroupSecurityModel": snmpV3GroupSecurityModel,
       "snmpV3GroupSecurityLevel": snmpV3GroupSecurityLevel,
       "snmpV3GroupReadViewName": snmpV3GroupReadViewName,
       "snmpV3GroupWriteViewName": snmpV3GroupWriteViewName,
       "snmpV3GroupNotifyViewName": snmpV3GroupNotifyViewName,
       "snmpV3GroupStatus": snmpV3GroupStatus,
       "snmpV3ViewTree": snmpV3ViewTree,
       "snmpV3ViewTreeTable": snmpV3ViewTreeTable,
       "snmpV3ViewTreeEntry": snmpV3ViewTreeEntry,
       "snmpV3viewTreeName": snmpV3viewTreeName,
       "snmpV3viewTreeSubtree": snmpV3viewTreeSubtree,
       "snmpV3viewTreeMask": snmpV3viewTreeMask,
       "snmpV3viewTreeType": snmpV3viewTreeType,
       "snmpV3viewTreeStatus": snmpV3viewTreeStatus,
       "snmpV3Community": snmpV3Community,
       "snmpV3CommunityTable": snmpV3CommunityTable,
       "snmpV3CommunityEntry": snmpV3CommunityEntry,
       "snmpV3CommunityName": snmpV3CommunityName,
       "snmpV3CommunityPolicy": snmpV3CommunityPolicy,
       "snmpV3CommunityStatus": snmpV3CommunityStatus,
       "snmpV3Host": snmpV3Host,
       "ipv4snmpV3HostTable": ipv4snmpV3HostTable,
       "ipv4snmpV3HostEntry": ipv4snmpV3HostEntry,
       "ipv4snmpV3HostAddress": ipv4snmpV3HostAddress,
       "ipv4snmpV3HostCommunityName": ipv4snmpV3HostCommunityName,
       "ipv4snmpV3HostVersion": ipv4snmpV3HostVersion,
       "ipv4snmpV3HostStatus": ipv4snmpV3HostStatus,
       "snmpV3HostTable": snmpV3HostTable,
       "snmpV3HostEntry": snmpV3HostEntry,
       "snmpV3HostAddress": snmpV3HostAddress,
       "snmpV3IPType": snmpV3IPType,
       "snmpV3HostCommunityName": snmpV3HostCommunityName,
       "snmpV3HostVersion": snmpV3HostVersion,
       "snmpV3HostInterfaceName": snmpV3HostInterfaceName,
       "snmpV3HostStatus": snmpV3HostStatus,
       "snmpV3EngineID": snmpV3EngineID,
       "snmpV3Trap": snmpV3Trap,
       "snmpV3TrapSNMPAuthentication": snmpV3TrapSNMPAuthentication,
       "snmpV3TrapBootup": snmpV3TrapBootup,
       "snmpV3TrapPortLinkUpDown": snmpV3TrapPortLinkUpDown,
       "snmpV3TrapRSTPStateChange": snmpV3TrapRSTPStateChange,
       "snmpV3TrapFirmUpgrade": snmpV3TrapFirmUpgrade,
       "companyAutoSurveillanceVlan": companyAutoSurveillanceVlan,
       "autoSurveillanceVlanSystem": autoSurveillanceVlanSystem,
       "autoSurveillanceVlanMode": autoSurveillanceVlanMode,
       "autoSurveillanceVlanId": autoSurveillanceVlanId,
       "autoSurveillanceVlanPriority": autoSurveillanceVlanPriority,
       "autoSurveillanceVlanTaggedUplinkDownlinkPort": autoSurveillanceVlanTaggedUplinkDownlinkPort,
       "autoSurveillanceVlanOUI": autoSurveillanceVlanOUI,
       "autoSurveillanceVlanOUITable": autoSurveillanceVlanOUITable,
       "autoSurveillanceVlanOUIEntry": autoSurveillanceVlanOUIEntry,
       "autoSurveillanceVlanOUISurveillanceOUI": autoSurveillanceVlanOUISurveillanceOUI,
       "autoSurveillanceVlanOUIDescription": autoSurveillanceVlanOUIDescription,
       "autoSurveillanceVlanOUIMask": autoSurveillanceVlanOUIMask,
       "autoSurveillanceVlanOUIComponentType": autoSurveillanceVlanOUIComponentType,
       "autoSurveillanceVlanOUIStatus": autoSurveillanceVlanOUIStatus,
       "companyTraps": companyTraps,
       "traps": traps,
       "topologyChange": topologyChange,
       "firmwareUpgradeSuccess": firmwareUpgradeSuccess,
       "firmwareUpgradeFailure": firmwareUpgradeFailure,
       "firmwareIllegalFile": firmwareIllegalFile,
       "firmwareTransferError": firmwareTransferError,
       "firmwareChecksumError": firmwareChecksumError,
       "companyGreenSetting": companyGreenSetting,
       "dlinkGreenLEDShutoff": dlinkGreenLEDShutoff,
       "dlinkGreenLEDShutoffPortList": dlinkGreenLEDShutoffPortList,
       "dlinkGreenLEDShutoffState": dlinkGreenLEDShutoffState,
       "dlinkGreenLEDShutoffTimeProfile1": dlinkGreenLEDShutoffTimeProfile1,
       "dlinkGreenLEDShutoffTimeProfile2": dlinkGreenLEDShutoffTimeProfile2,
       "dlinkGreenPortShutoff": dlinkGreenPortShutoff,
       "dlinkGreenPortShutoffPortList": dlinkGreenPortShutoffPortList,
       "dlinkGreenPortShutoffState": dlinkGreenPortShutoffState,
       "dlinkGreenPortShutoffTimeProfile1": dlinkGreenPortShutoffTimeProfile1,
       "dlinkGreenPortShutoffTimeProfile2": dlinkGreenPortShutoffTimeProfile2,
       "dlinkGreenPortStandby": dlinkGreenPortStandby,
       "dlinkGreenPortStandbyPortList": dlinkGreenPortStandbyPortList,
       "dlinkGreenPortStandbyState": dlinkGreenPortStandbyState,
       "dlinkGreenPortStandbyTimeProfile1": dlinkGreenPortStandbyTimeProfile1,
       "dlinkGreenPortStandbyTimeProfile2": dlinkGreenPortStandbyTimeProfile2,
       "dlinkGreenSystemHibernation": dlinkGreenSystemHibernation,
       "dlinkGreenSystemHibernationState": dlinkGreenSystemHibernationState,
       "dlinkGreenSystemHibernationTimeProfile1": dlinkGreenSystemHibernationTimeProfile1,
       "dlinkGreenSystemHibernationTimeProfile2": dlinkGreenSystemHibernationTimeProfile2,
       "dlinkPowerSavCableLenDetectionState": dlinkPowerSavCableLenDetectionState,
       "dlinkPowerSavLinkStatusDetectState": dlinkPowerSavLinkStatusDetectState,
       "companyTimeRangeMgmt": companyTimeRangeMgmt,
       "swTimeRangeSettingTable": swTimeRangeSettingTable,
       "swTimeRangeSettingEntry": swTimeRangeSettingEntry,
       "swTimeRangeIndex": swTimeRangeIndex,
       "swTimeRangeName": swTimeRangeName,
       "swTimeRangeDate": swTimeRangeDate,
       "swTimeRangeStartYear": swTimeRangeStartYear,
       "swTimeRangeStartMonth": swTimeRangeStartMonth,
       "swTimeRangeStartDay": swTimeRangeStartDay,
       "swTimeRangeStartHour": swTimeRangeStartHour,
       "swTimeRangeStartMinute": swTimeRangeStartMinute,
       "swTimeRangeEndYear": swTimeRangeEndYear,
       "swTimeRangeEndMonth": swTimeRangeEndMonth,
       "swTimeRangeEndDay": swTimeRangeEndDay,
       "swTimeRangeEndHour": swTimeRangeEndHour,
       "swTimeRangeEndMinute": swTimeRangeEndMinute,
       "swTimeRangeMonday": swTimeRangeMonday,
       "swTimeRangeTuesday": swTimeRangeTuesday,
       "swTimeRangeWednesday": swTimeRangeWednesday,
       "swTimeRangeThursday": swTimeRangeThursday,
       "swTimeRangeFriday": swTimeRangeFriday,
       "swTimeRangeSaturday": swTimeRangeSaturday,
       "swTimeRangeSunday": swTimeRangeSunday,
       "swTimeRangeRowStatus": swTimeRangeRowStatus,
       "companyStaticMcast": companyStaticMcast,
       "staticMcastTable": staticMcastTable,
       "staticMcastEntry": staticMcastEntry,
       "staticMcastVlanID": staticMcastVlanID,
       "staticMcastMac": staticMcastMac,
       "staticMcastEgressPorts": staticMcastEgressPorts,
       "staticMcastStatus": staticMcastStatus,
       "companyCableDiagnostic": companyCableDiagnostic,
       "cableDiagTriggerIndex": cableDiagTriggerIndex,
       "cableDiagPair1TestResult": cableDiagPair1TestResult,
       "cableDiagPair1FaultDistance": cableDiagPair1FaultDistance,
       "cableDiagPair2TestResult": cableDiagPair2TestResult,
       "cableDiagPair2FaultDistance": cableDiagPair2FaultDistance,
       "cableDiagPair3TestResult": cableDiagPair3TestResult,
       "cableDiagPair3FaultDistance": cableDiagPair3FaultDistance,
       "cableDiagPair4TestResult": cableDiagPair4TestResult,
       "cableDiagPair4FaultDistance": cableDiagPair4FaultDistance,
       "cableDiagLengthinRange": cableDiagLengthinRange,
       "companyRMON": companyRMON,
       "rmonGlobalState": rmonGlobalState,
       "rmonStatistics": rmonStatistics,
       "rmonStatsTable": rmonStatsTable,
       "rmonStatsEntry": rmonStatsEntry,
       "rmonStatsIndex": rmonStatsIndex,
       "rmonStatsDataSource": rmonStatsDataSource,
       "rmonStatsOwner": rmonStatsOwner,
       "rmonStatsStatus": rmonStatsStatus,
       "rmonHistory": rmonHistory,
       "rmonHistoryTable": rmonHistoryTable,
       "rmonHistoryEntry": rmonHistoryEntry,
       "rmonHistoryIndex": rmonHistoryIndex,
       "rmonHistoryDataSource": rmonHistoryDataSource,
       "rmonHistoryBucketsRequested": rmonHistoryBucketsRequested,
       "rmonHistoryInterval": rmonHistoryInterval,
       "rmonHistoryOwner": rmonHistoryOwner,
       "rmonHistoryStatus": rmonHistoryStatus,
       "rmonAlarm": rmonAlarm,
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
       "rmonEvent": rmonEvent,
       "rmonEventTable": rmonEventTable,
       "rmonEventEntry": rmonEventEntry,
       "rmonEventIndex": rmonEventIndex,
       "rmonEventDescription": rmonEventDescription,
       "rmonEventType": rmonEventType,
       "rmonEventCommunity": rmonEventCommunity,
       "rmonEventOwner": rmonEventOwner,
       "rmonEventStatus": rmonEventStatus,
       "companyNeighbor": companyNeighbor,
       "neighborTable": neighborTable,
       "neighborEntry": neighborEntry,
       "neighborIfindex": neighborIfindex,
       "neighborIPv6Addr": neighborIPv6Addr,
       "neighborMACAddr": neighborMACAddr,
       "neighborType": neighborType,
       "neighborCacheState": neighborCacheState,
       "neighborRowStatus": neighborRowStatus,
       "companydot3azEEE": companydot3azEEE,
       "dot3azEEEset": dot3azEEEset,
       "dot3azTable": dot3azTable,
       "dot3azEntry": dot3azEntry,
       "portD3Index": portD3Index,
       "portD3State": portD3State}
)
