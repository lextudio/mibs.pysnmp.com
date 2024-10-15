# SNMP MIB module (DGS-1500-52_AX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-1500-52_AX
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:06 2024
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


class LldpManAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
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
_Dlink_DGS1500Series_ObjectIdentity = ObjectIdentity
dlink_DGS1500Series = _Dlink_DGS1500Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126)
)
_Dgs_1500_52_ObjectIdentity = ObjectIdentity
dgs_1500_52 = _Dgs_1500_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4)
)
_Dgs_1500_52ax_ObjectIdentity = ObjectIdentity
dgs_1500_52ax = _Dgs_1500_52ax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1)
)
_CompanySystem_ObjectIdentity = ObjectIdentity
companySystem = _CompanySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 8),
    _SysSafeGuardEnable_Type()
)
sysSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSafeGuardEnable.setStatus("current")


class _SysRestart_Type(TruthValue):
    """Custom type sysRestart based on TruthValue"""


_SysRestart_Object = MibScalar
sysRestart = _SysRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 10),
    _SysRestart_Type()
)
sysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestart.setStatus("current")


class _SysSave_Type(TruthValue):
    """Custom type sysSave based on TruthValue"""


_SysSave_Object = MibScalar
sysSave = _SysSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 12),
    _SysJumboFrameEnable_Type()
)
sysJumboFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysJumboFrameEnable.setStatus("current")
_SysPortCtrlTable_Object = MibTable
sysPortCtrlTable = _SysPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    sysPortCtrlTable.setStatus("current")
_SysPortCtrlEntry_Object = MibTableRow
sysPortCtrlEntry = _SysPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1)
)
sysPortCtrlEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "sysPortCtrlIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 13, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 14),
    _SysDhcpAutoConfiguration_Type()
)
sysDhcpAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpAutoConfiguration.setStatus("current")
_SysGPIOStatus_ObjectIdentity = ObjectIdentity
sysGPIOStatus = _SysGPIOStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 15)
)


class _SysFanStatus_Type(Integer32):
    """Custom type sysFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("normal", 1))
    )


_SysFanStatus_Type.__name__ = "Integer32"
_SysFanStatus_Object = MibScalar
sysFanStatus = _SysFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 1, 15, 1),
    _SysFanStatus_Type()
)
sysFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanStatus.setStatus("current")
_CompanyIpifGroup_ObjectIdentity = ObjectIdentity
companyIpifGroup = _CompanyIpifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2)
)
_SysIpInterfaceName_Type = OctetString
_SysIpInterfaceName_Object = MibScalar
sysIpInterfaceName = _SysIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2, 1),
    _SysIpInterfaceName_Type()
)
sysIpInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpInterfaceName.setStatus("current")
_SysIpManagementVLANName_Type = OctetString
_SysIpManagementVLANName_Object = MibScalar
sysIpManagementVLANName = _SysIpManagementVLANName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2, 2),
    _SysIpManagementVLANName_Type()
)
sysIpManagementVLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpManagementVLANName.setStatus("current")


class _SysIpInterfaceAdminStatus_Type(Integer32):
    """Custom type sysIpInterfaceAdminStatus based on Integer32"""
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


_SysIpInterfaceAdminStatus_Type.__name__ = "Integer32"
_SysIpInterfaceAdminStatus_Object = MibScalar
sysIpInterfaceAdminStatus = _SysIpInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2, 3),
    _SysIpInterfaceAdminStatus_Type()
)
sysIpInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysIpInterfaceAdminStatus.setStatus("current")


class _SysIpAddrCfgMode_Type(Integer32):
    """Custom type sysIpAddrCfgMode based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 2),
          ("manual", 1))
    )


_SysIpAddrCfgMode_Type.__name__ = "Integer32"
_SysIpAddrCfgMode_Object = MibScalar
sysIpAddrCfgMode = _SysIpAddrCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2, 4),
    _SysIpAddrCfgMode_Type()
)
sysIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddrCfgMode.setStatus("current")
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2, 5),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("current")
_SysIpSubnetMask_Type = IpAddress
_SysIpSubnetMask_Object = MibScalar
sysIpSubnetMask = _SysIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2, 6),
    _SysIpSubnetMask_Type()
)
sysIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpSubnetMask.setStatus("current")
_SysGateway_Type = IpAddress
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 2, 7),
    _SysGateway_Type()
)
sysGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGateway.setStatus("current")
_CompanyTftpGroup_ObjectIdentity = ObjectIdentity
companyTftpGroup = _CompanyTftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3)
)
_TftpFwServerIpAddress_Type = IpAddress
_TftpFwServerIpAddress_Object = MibScalar
tftpFwServerIpAddress = _TftpFwServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 1),
    _TftpFwServerIpAddress_Type()
)
tftpFwServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwServerIpAddress.setStatus("current")


class _TftpFwImageFileName_Type(DisplayString):
    """Custom type tftpFwImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TftpFwImageFileName_Type.__name__ = "DisplayString"
_TftpFwImageFileName_Object = MibScalar
tftpFwImageFileName = _TftpFwImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 2),
    _TftpFwImageFileName_Type()
)
tftpFwImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwImageFileName.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 3),
    _TftpFwTftpOperation_Type()
)
tftpFwTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTftpOperation.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 4),
    _TftpFwTftpOperationStatus_Type()
)
tftpFwTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTftpOperationStatus.setStatus("current")
_TftpCfgServerIpAddress_Type = IpAddress
_TftpCfgServerIpAddress_Object = MibScalar
tftpCfgServerIpAddress = _TftpCfgServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 5),
    _TftpCfgServerIpAddress_Type()
)
tftpCfgServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgServerIpAddress.setStatus("current")


class _TftpConfigFileName_Type(DisplayString):
    """Custom type tftpConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TftpConfigFileName_Type.__name__ = "DisplayString"
_TftpConfigFileName_Object = MibScalar
tftpConfigFileName = _TftpConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 6),
    _TftpConfigFileName_Type()
)
tftpConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConfigFileName.setStatus("current")


class _TftpConfigTftpOperation_Type(Integer32):
    """Custom type tftpConfigTftpOperation based on Integer32"""
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


_TftpConfigTftpOperation_Type.__name__ = "Integer32"
_TftpConfigTftpOperation_Object = MibScalar
tftpConfigTftpOperation = _TftpConfigTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 7),
    _TftpConfigTftpOperation_Type()
)
tftpConfigTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConfigTftpOperation.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 3, 8),
    _TftpConfigTftpOperationStatus_Type()
)
tftpConfigTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpConfigTftpOperationStatus.setStatus("current")
_CompanyMiscGroup_ObjectIdentity = ObjectIdentity
companyMiscGroup = _CompanyMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 4, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("current")
_CompanyRSTP_ObjectIdentity = ObjectIdentity
companyRSTP = _CompanyRSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6)
)
_StpGlobal_ObjectIdentity = ObjectIdentity
stpGlobal = _StpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 5),
    _StpProtocolSpecification_Type()
)
stpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpProtocolSpecification.setStatus("current")
_StpTimeSinceTopologyChange_Type = TimeTicks
_StpTimeSinceTopologyChange_Object = MibScalar
stpTimeSinceTopologyChange = _StpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 6),
    _StpTimeSinceTopologyChange_Type()
)
stpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTimeSinceTopologyChange.setStatus("current")
_StpTopChanges_Type = Counter32
_StpTopChanges_Object = MibScalar
stpTopChanges = _StpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 7),
    _StpTopChanges_Type()
)
stpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopChanges.setStatus("current")
_StpDesignatedRoot_Type = BridgeId
_StpDesignatedRoot_Object = MibScalar
stpDesignatedRoot = _StpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 8),
    _StpDesignatedRoot_Type()
)
stpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesignatedRoot.setStatus("current")
_StpRootCost_Type = Integer32
_StpRootCost_Object = MibScalar
stpRootCost = _StpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 9),
    _StpRootCost_Type()
)
stpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootCost.setStatus("current")
_StpRootPort_Type = Integer32
_StpRootPort_Object = MibScalar
stpRootPort = _StpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 10),
    _StpRootPort_Type()
)
stpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootPort.setStatus("current")
_StpMaxAge_Type = Timeout
_StpMaxAge_Object = MibScalar
stpMaxAge = _StpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 11),
    _StpMaxAge_Type()
)
stpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpMaxAge.setStatus("current")
_StpHelloTime_Type = Timeout
_StpHelloTime_Object = MibScalar
stpHelloTime = _StpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 12),
    _StpHelloTime_Type()
)
stpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHelloTime.setStatus("current")
_StpHoldTime_Type = Integer32
_StpHoldTime_Object = MibScalar
stpHoldTime = _StpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 13),
    _StpHoldTime_Type()
)
stpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHoldTime.setStatus("current")
_StpForwardDelay_Type = Timeout
_StpForwardDelay_Object = MibScalar
stpForwardDelay = _StpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 1, 17),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("current")
_StpPortEntry_Object = MibTableRow
stpPortEntry = _StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1)
)
stpPortEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "stpPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 6),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortDesignatedRoot_Type = BridgeId
_StpPortDesignatedRoot_Object = MibTableColumn
stpPortDesignatedRoot = _StpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 7),
    _StpPortDesignatedRoot_Type()
)
stpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedRoot.setStatus("current")
_StpPortDesignatedCost_Type = Integer32
_StpPortDesignatedCost_Object = MibTableColumn
stpPortDesignatedCost = _StpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 8),
    _StpPortDesignatedCost_Type()
)
stpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedCost.setStatus("current")
_StpPortDesignatedBridge_Type = BridgeId
_StpPortDesignatedBridge_Object = MibTableColumn
stpPortDesignatedBridge = _StpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 10),
    _StpPortDesignatedPort_Type()
)
stpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedPort.setStatus("current")
_StpPortForwardTransitions_Type = Counter32
_StpPortForwardTransitions_Object = MibTableColumn
stpPortForwardTransitions = _StpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 11),
    _StpPortForwardTransitions_Type()
)
stpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortForwardTransitions.setStatus("current")
_StpPortProtocolMigration_Type = TruthValue
_StpPortProtocolMigration_Object = MibTableColumn
stpPortProtocolMigration = _StpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 12),
    _StpPortProtocolMigration_Type()
)
stpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortProtocolMigration.setStatus("current")
_StpPortOperEdgePort_Type = TruthValue
_StpPortOperEdgePort_Object = MibTableColumn
stpPortOperEdgePort = _StpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 14),
    _StpPortAdminPointToPoint_Type()
)
stpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortAdminPointToPoint.setStatus("current")
_StpPortOperPointToPoint_Type = TruthValue
_StpPortOperPointToPoint_Object = MibTableColumn
stpPortOperPointToPoint = _StpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 16),
    _StpPortEdge_Type()
)
stpPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEdge.setStatus("current")
_StpPortRestrictedRole_Type = TruthValue
_StpPortRestrictedRole_Object = MibTableColumn
stpPortRestrictedRole = _StpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 17),
    _StpPortRestrictedRole_Type()
)
stpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedRole.setStatus("current")
_StpPortRestrictedTCN_Type = TruthValue
_StpPortRestrictedTCN_Object = MibTableColumn
stpPortRestrictedTCN = _StpPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 6, 2, 1, 18),
    _StpPortRestrictedTCN_Type()
)
stpPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedTCN.setStatus("current")
_CompanyDot1qVlanGroup_ObjectIdentity = ObjectIdentity
companyDot1qVlanGroup = _CompanyDot1qVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7)
)


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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 5),
    _Dot1qVlanAsyOnOff_Type()
)
dot1qVlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanAsyOnOff.setStatus("current")
_Dot1qVlanTable_Object = MibTable
dot1qVlanTable = _Dot1qVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6)
)
if mibBuilder.loadTexts:
    dot1qVlanTable.setStatus("current")
_Dot1qVlanEntry_Object = MibTableRow
dot1qVlanEntry = _Dot1qVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6, 1)
)
dot1qVlanEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "dot1qVlanName"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6, 1, 1),
    _Dot1qVlanName_Type()
)
dot1qVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanName.setStatus("current")
_Dot1qVlanEgressPorts_Type = PortList
_Dot1qVlanEgressPorts_Object = MibTableColumn
dot1qVlanEgressPorts = _Dot1qVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6, 1, 2),
    _Dot1qVlanEgressPorts_Type()
)
dot1qVlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanEgressPorts.setStatus("current")
_Dot1qVlanForbiddenPorts_Type = PortList
_Dot1qVlanForbiddenPorts_Object = MibTableColumn
dot1qVlanForbiddenPorts = _Dot1qVlanForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6, 1, 3),
    _Dot1qVlanForbiddenPorts_Type()
)
dot1qVlanForbiddenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanForbiddenPorts.setStatus("current")
_Dot1qVlanUntaggedPorts_Type = PortList
_Dot1qVlanUntaggedPorts_Object = MibTableColumn
dot1qVlanUntaggedPorts = _Dot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6, 1, 4),
    _Dot1qVlanUntaggedPorts_Type()
)
dot1qVlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanUntaggedPorts.setStatus("current")


class _Dot1qVlanAdvertisementStatus_Type(Integer32):
    """Custom type dot1qVlanAdvertisementStatus based on Integer32"""
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


_Dot1qVlanAdvertisementStatus_Type.__name__ = "Integer32"
_Dot1qVlanAdvertisementStatus_Object = MibTableColumn
dot1qVlanAdvertisementStatus = _Dot1qVlanAdvertisementStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6, 1, 5),
    _Dot1qVlanAdvertisementStatus_Type()
)
dot1qVlanAdvertisementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanAdvertisementStatus.setStatus("current")
_Dot1qVlanRowStatus_Type = RowStatus
_Dot1qVlanRowStatus_Object = MibTableColumn
dot1qVlanRowStatus = _Dot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 6, 1, 6),
    _Dot1qVlanRowStatus_Type()
)
dot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanRowStatus.setStatus("current")
_Dot1qVlanUngisterMCFilterTable_Object = MibTable
dot1qVlanUngisterMCFilterTable = _Dot1qVlanUngisterMCFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 8)
)
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFilterTable.setStatus("current")
_Dot1qVlanUngisterMCFilterEntry_Object = MibTableRow
dot1qVlanUngisterMCFilterEntry = _Dot1qVlanUngisterMCFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 8, 1)
)
dot1qVlanUngisterMCFilterEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "dot1qVlanUngisterMCFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 7, 8, 1, 2),
    _Dot1qVlanUngisterMCFiltermode_Type()
)
dot1qVlanUngisterMCFiltermode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFiltermode.setStatus("current")
_CompanyLA_ObjectIdentity = ObjectIdentity
companyLA = _CompanyLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8)
)
_LaSystem_ObjectIdentity = ObjectIdentity
laSystem = _LaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 1, 2),
    _LaStatus_Type()
)
laStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laStatus.setStatus("current")
_LaPortChannelTable_Object = MibTable
laPortChannelTable = _LaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    laPortChannelTable.setStatus("current")
_LaPortChannelEntry_Object = MibTableRow
laPortChannelEntry = _LaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 1, 3, 1)
)
laPortChannelEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "laPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    laPortChannelEntry.setStatus("current")
_LaPortChannelIfIndex_Type = InterfaceIndex
_LaPortChannelIfIndex_Object = MibTableColumn
laPortChannelIfIndex = _LaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 1, 3, 1, 1),
    _LaPortChannelIfIndex_Type()
)
laPortChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortChannelIfIndex.setStatus("current")
_LaPortChannelMemberList_Type = PortList
_LaPortChannelMemberList_Object = MibTableColumn
laPortChannelMemberList = _LaPortChannelMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 1, 3, 1, 2),
    _LaPortChannelMemberList_Type()
)
laPortChannelMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMemberList.setStatus("current")
_LaPortChannelMode_Type = PortLaMode
_LaPortChannelMode_Object = MibTableColumn
laPortChannelMode = _LaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 1, 3, 1, 3),
    _LaPortChannelMode_Type()
)
laPortChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMode.setStatus("current")
_LaPortControl_ObjectIdentity = ObjectIdentity
laPortControl = _LaPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 2)
)
_LaPortControlTable_Object = MibTable
laPortControlTable = _LaPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    laPortControlTable.setStatus("current")
_LaPortControlEntry_Object = MibTableRow
laPortControlEntry = _LaPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 2, 1, 1)
)
laPortControlEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "laPortControlIndex"),
)
if mibBuilder.loadTexts:
    laPortControlEntry.setStatus("current")
_LaPortControlIndex_Type = InterfaceIndex
_LaPortControlIndex_Object = MibTableColumn
laPortControlIndex = _LaPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 2, 1, 1, 1),
    _LaPortControlIndex_Type()
)
laPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortControlIndex.setStatus("current")


class _LaPortActorPortPriority_Type(Integer32):
    """Custom type laPortActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LaPortActorPortPriority_Type.__name__ = "Integer32"
_LaPortActorPortPriority_Object = MibTableColumn
laPortActorPortPriority = _LaPortActorPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 2, 1, 1, 2),
    _LaPortActorPortPriority_Type()
)
laPortActorPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortActorPortPriority.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 8, 2, 1, 1, 4),
    _LaPortActorTimeout_Type()
)
laPortActorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortActorTimeout.setStatus("current")
_CompanyStaticMAC_ObjectIdentity = ObjectIdentity
companyStaticMAC = _CompanyStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 1),
    _StaticDisableAutoLearn_Type()
)
staticDisableAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDisableAutoLearn.setStatus("current")
_StaticAutoLearningList_Type = PortList
_StaticAutoLearningList_Object = MibScalar
staticAutoLearningList = _StaticAutoLearningList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 2),
    _StaticAutoLearningList_Type()
)
staticAutoLearningList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticAutoLearningList.setStatus("current")
_StaticTable_Object = MibTable
staticTable = _StaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 3)
)
if mibBuilder.loadTexts:
    staticTable.setStatus("current")
_StaticEntry_Object = MibTableRow
staticEntry = _StaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 3, 1)
)
staticEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "staticVlanID"),
    (0, "DGS-1500-52_AX", "staticMac"),
    (0, "DGS-1500-52_AX", "staticPort"),
)
if mibBuilder.loadTexts:
    staticEntry.setStatus("current")
_StaticVlanID_Type = Integer32
_StaticVlanID_Object = MibTableColumn
staticVlanID = _StaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 3, 1, 1),
    _StaticVlanID_Type()
)
staticVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticVlanID.setStatus("current")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 3, 1, 2),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMac.setStatus("current")
_StaticPort_Type = Integer32
_StaticPort_Object = MibTableColumn
staticPort = _StaticPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 3, 1, 3),
    _StaticPort_Type()
)
staticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticPort.setStatus("current")
_StaticStatus_Type = RowStatus
_StaticStatus_Object = MibTableColumn
staticStatus = _StaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 9, 3, 1, 4),
    _StaticStatus_Type()
)
staticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticStatus.setStatus("current")
_CompanyIgsGroup_ObjectIdentity = ObjectIdentity
companyIgsGroup = _CompanyIgsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10)
)
_IgsSystem_ObjectIdentity = ObjectIdentity
igsSystem = _IgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 1, 7),
    _IgsQueryMaxResponseTime_Type()
)
igsQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsQueryMaxResponseTime.setStatus("current")
_IgsVlan_ObjectIdentity = ObjectIdentity
igsVlan = _IgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3)
)
_IgsVlanRouterTable_Object = MibTable
igsVlanRouterTable = _IgsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    igsVlanRouterTable.setStatus("current")
_IgsVlanRouterEntry_Object = MibTableRow
igsVlanRouterEntry = _IgsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 3, 1)
)
igsVlanRouterEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "igsVlanRouterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 3, 1, 1),
    _IgsVlanRouterVlanId_Type()
)
igsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterVlanId.setStatus("current")
_IgsVlanRouterPortList_Type = PortList
_IgsVlanRouterPortList_Object = MibTableColumn
igsVlanRouterPortList = _IgsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 3, 1, 2),
    _IgsVlanRouterPortList_Type()
)
igsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterPortList.setStatus("current")
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("current")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "igsVlanFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1, 5),
    _IgsVlanQueryInterval_Type()
)
igsVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanQueryInterval.setStatus("current")
_IgsVlanRtrPortList_Type = PortList
_IgsVlanRtrPortList_Object = MibTableColumn
igsVlanRtrPortList = _IgsVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 4, 1, 8),
    _IgsVlanFastLeave_Type()
)
igsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFastLeave.setStatus("current")
_IgsVlanMulticastGroupTable_Object = MibTable
igsVlanMulticastGroupTable = _IgsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 5)
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupTable.setStatus("current")
_IgsVlanMulticastGroupEntry_Object = MibTableRow
igsVlanMulticastGroupEntry = _IgsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 5, 1)
)
igsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "igsVlanMulticastGroupVlanId"),
    (0, "DGS-1500-52_AX", "igsVlanMulticastGroupIpAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 5, 1, 1),
    _IgsVlanMulticastGroupVlanId_Type()
)
igsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupVlanId.setStatus("current")
_IgsVlanMulticastGroupIpAddress_Type = InetAddress
_IgsVlanMulticastGroupIpAddress_Object = MibTableColumn
igsVlanMulticastGroupIpAddress = _IgsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 5, 1, 2),
    _IgsVlanMulticastGroupIpAddress_Type()
)
igsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupIpAddress.setStatus("current")
_IgsVlanMulticastGroupMacAddress_Type = MacAddress
_IgsVlanMulticastGroupMacAddress_Object = MibTableColumn
igsVlanMulticastGroupMacAddress = _IgsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 5, 1, 3),
    _IgsVlanMulticastGroupMacAddress_Type()
)
igsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupMacAddress.setStatus("current")
_IgsVlanMulticastGroupPortList_Type = PortList
_IgsVlanMulticastGroupPortList_Object = MibTableColumn
igsVlanMulticastGroupPortList = _IgsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 10, 3, 5, 1, 4),
    _IgsVlanMulticastGroupPortList_Type()
)
igsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupPortList.setStatus("current")
_CompanyQoSGroup_ObjectIdentity = ObjectIdentity
companyQoSGroup = _CompanyQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12)
)


class _QosMode_Type(Integer32):
    """Custom type qosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 1),
          ("dscp", 2))
    )


_QosMode_Type.__name__ = "Integer32"
_QosMode_Object = MibScalar
qosMode = _QosMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 2),
    _QueuingMechanism_Type()
)
queuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMechanism.setStatus("current")
_QosQ1p_ObjectIdentity = ObjectIdentity
qosQ1p = _QosQ1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 3)
)
_Dot1pPortTable_Object = MibTable
dot1pPortTable = _Dot1pPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    dot1pPortTable.setStatus("current")
_Dot1pPortEntry_Object = MibTableRow
dot1pPortEntry = _Dot1pPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 3, 1, 1)
)
dot1pPortEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "dot1pPortIndex"),
)
if mibBuilder.loadTexts:
    dot1pPortEntry.setStatus("current")
_Dot1pPortIndex_Type = Integer32
_Dot1pPortIndex_Object = MibTableColumn
dot1pPortIndex = _Dot1pPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 3, 1, 1, 2),
    _Dot1pPortPriority_Type()
)
dot1pPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1pPortPriority.setStatus("current")
_QosDiffServ_ObjectIdentity = ObjectIdentity
qosDiffServ = _QosDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 1),
    _QosDiffServEnable_Type()
)
qosDiffServEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDiffServEnable.setStatus("current")
_QosDiffServTypeGroup_ObjectIdentity = ObjectIdentity
qosDiffServTypeGroup = _QosDiffServTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 21),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 23),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 24),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 25),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 26),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 27),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 28),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 29),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 30),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 31),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 32),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 33),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 34),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 35),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 36),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 37),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 38),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 39),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 40),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 41),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 42),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 43),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 44),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 45),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 46),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 47),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 48),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 49),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 50),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 51),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 52),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 53),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 54),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 55),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 56),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 57),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 58),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 59),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 60),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 61),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 62),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 63),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 12, 4, 2, 64),
    _QosDiffServType63_Type()
)
qosDiffServType63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType63.setStatus("current")
_CompanyTrafficMgmt_ObjectIdentity = ObjectIdentity
companyTrafficMgmt = _CompanyTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13)
)
_BandwidthCtrlSettings_ObjectIdentity = ObjectIdentity
bandwidthCtrlSettings = _BandwidthCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 1)
)
_BandwidthCtrlTable_Object = MibTable
bandwidthCtrlTable = _BandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    bandwidthCtrlTable.setStatus("current")
_BandwidthCtrlEntry_Object = MibTableRow
bandwidthCtrlEntry = _BandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 1, 2, 1)
)
bandwidthCtrlEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "bandwidthCtrlIndex"),
)
if mibBuilder.loadTexts:
    bandwidthCtrlEntry.setStatus("current")
_BandwidthCtrlIndex_Type = Integer32
_BandwidthCtrlIndex_Object = MibTableColumn
bandwidthCtrlIndex = _BandwidthCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 1, 2, 1, 3),
    _BandwidthCtrlRxThreshold_Type()
)
bandwidthCtrlRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlRxThreshold.setStatus("current")
_BroadcastStormCtrlSettings_ObjectIdentity = ObjectIdentity
broadcastStormCtrlSettings = _BroadcastStormCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 13, 3, 3),
    _BroadcastStormCtrlThreshold_Type()
)
broadcastStormCtrlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormCtrlThreshold.setStatus("current")
_CompanySecurity_ObjectIdentity = ObjectIdentity
companySecurity = _CompanySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14)
)
_SecurityTrustedHost_ObjectIdentity = ObjectIdentity
securityTrustedHost = _SecurityTrustedHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 1, 1),
    _TrustedHostStatus_Type()
)
trustedHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostStatus.setStatus("current")
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("current")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 1, 2, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "trustedHostIpAddr"),
    (0, "DGS-1500-52_AX", "trustedHostIpMask"),
)
if mibBuilder.loadTexts:
    trustedHostEntry.setStatus("current")
_TrustedHostIpAddr_Type = IpAddress
_TrustedHostIpAddr_Object = MibTableColumn
trustedHostIpAddr = _TrustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 1, 2, 1, 1),
    _TrustedHostIpAddr_Type()
)
trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpAddr.setStatus("current")
_TrustedHostIpMask_Type = IpAddress
_TrustedHostIpMask_Object = MibTableColumn
trustedHostIpMask = _TrustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 1, 2, 1, 2),
    _TrustedHostIpMask_Type()
)
trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpMask.setStatus("current")
_TrustedHostRowStatus_Type = RowStatus
_TrustedHostRowStatus_Object = MibTableColumn
trustedHostRowStatus = _TrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 1, 2, 1, 3),
    _TrustedHostRowStatus_Type()
)
trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedHostRowStatus.setStatus("current")
_SecurityPortSecurity_ObjectIdentity = ObjectIdentity
securityPortSecurity = _SecurityPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 2)
)
_PortSecTable_Object = MibTable
portSecTable = _PortSecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    portSecTable.setStatus("current")
_PortSecEntry_Object = MibTableRow
portSecEntry = _PortSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 2, 1, 1)
)
portSecEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "portSecIndex"),
)
if mibBuilder.loadTexts:
    portSecEntry.setStatus("current")
_PortSecIndex_Type = Integer32
_PortSecIndex_Object = MibTableColumn
portSecIndex = _PortSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 2, 1, 1, 3),
    _PortSecMLA_Type()
)
portSecMLA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMLA.setStatus("current")
_SecurityARPSpoofPrevent_ObjectIdentity = ObjectIdentity
securityARPSpoofPrevent = _SecurityARPSpoofPrevent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 3)
)
_ARPSpoofPreventTable_Object = MibTable
aRPSpoofPreventTable = _ARPSpoofPreventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    aRPSpoofPreventTable.setStatus("current")
_ARPSpoofPreventEntry_Object = MibTableRow
aRPSpoofPreventEntry = _ARPSpoofPreventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 3, 1, 1)
)
aRPSpoofPreventEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "aRPSpoofPreventIpAddr"),
)
if mibBuilder.loadTexts:
    aRPSpoofPreventEntry.setStatus("current")
_ARPSpoofPreventIpAddr_Type = IpAddress
_ARPSpoofPreventIpAddr_Object = MibTableColumn
aRPSpoofPreventIpAddr = _ARPSpoofPreventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 3, 1, 1, 2),
    _ARPSpoofPreventMacAddress_Type()
)
aRPSpoofPreventMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventMacAddress.setStatus("current")
_ARPSpoofPreventPortList_Type = PortList
_ARPSpoofPreventPortList_Object = MibTableColumn
aRPSpoofPreventPortList = _ARPSpoofPreventPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 3, 1, 1, 3),
    _ARPSpoofPreventPortList_Type()
)
aRPSpoofPreventPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventPortList.setStatus("current")
_ARPSpoofPreventRowStatus_Type = RowStatus
_ARPSpoofPreventRowStatus_Object = MibTableColumn
aRPSpoofPreventRowStatus = _ARPSpoofPreventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 3, 1, 1, 4),
    _ARPSpoofPreventRowStatus_Type()
)
aRPSpoofPreventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aRPSpoofPreventRowStatus.setStatus("current")
_SecuritySSL_ObjectIdentity = ObjectIdentity
securitySSL = _SecuritySSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 5)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 5, 1),
    _SslSecurityHttpStatus_Type()
)
sslSecurityHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSecurityHttpStatus.setStatus("current")
_SslCiphers_ObjectIdentity = ObjectIdentity
sslCiphers = _SslCiphers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 5, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 5, 2, 1),
    _SslCipherSuiteList_Type()
)
sslCipherSuiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCipherSuiteList.setStatus("current")
_SecurityDhcpServerScreen_ObjectIdentity = ObjectIdentity
securityDhcpServerScreen = _SecurityDhcpServerScreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 7)
)
_DhcpServerScreenEnablePortlist_Type = PortList
_DhcpServerScreenEnablePortlist_Object = MibScalar
dhcpServerScreenEnablePortlist = _DhcpServerScreenEnablePortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 7, 1),
    _DhcpServerScreenEnablePortlist_Type()
)
dhcpServerScreenEnablePortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenEnablePortlist.setStatus("current")
_DhcpServerScreenServerTable_Object = MibTable
dhcpServerScreenServerTable = _DhcpServerScreenServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 7, 2)
)
if mibBuilder.loadTexts:
    dhcpServerScreenServerTable.setStatus("current")
_DhcpServerScreenServerEntry_Object = MibTableRow
dhcpServerScreenServerEntry = _DhcpServerScreenServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 7, 2, 1)
)
dhcpServerScreenServerEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "dhcpServerScreenServerIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerScreenServerEntry.setStatus("current")


class _DhcpServerScreenServerIndex_Type(Integer32):
    """Custom type dhcpServerScreenServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DhcpServerScreenServerIndex_Type.__name__ = "Integer32"
_DhcpServerScreenServerIndex_Object = MibTableColumn
dhcpServerScreenServerIndex = _DhcpServerScreenServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 7, 2, 1, 1),
    _DhcpServerScreenServerIndex_Type()
)
dhcpServerScreenServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerScreenServerIndex.setStatus("current")
_DhcpServerScreenServerAddress_Type = IpAddress
_DhcpServerScreenServerAddress_Object = MibTableColumn
dhcpServerScreenServerAddress = _DhcpServerScreenServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 7, 2, 1, 2),
    _DhcpServerScreenServerAddress_Type()
)
dhcpServerScreenServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenServerAddress.setStatus("current")
_DhcpServerScreenServerStatus_Type = RowStatus
_DhcpServerScreenServerStatus_Object = MibTableColumn
dhcpServerScreenServerStatus = _DhcpServerScreenServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 7, 2, 1, 3),
    _DhcpServerScreenServerStatus_Type()
)
dhcpServerScreenServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerScreenServerStatus.setStatus("current")
_SecurityTrafficSeg_ObjectIdentity = ObjectIdentity
securityTrafficSeg = _SecurityTrafficSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 9, 1),
    _TrafficSegStatus_Type()
)
trafficSegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegStatus.setStatus("current")
_TrafficSegTable_Object = MibTable
trafficSegTable = _TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 9, 2)
)
if mibBuilder.loadTexts:
    trafficSegTable.setStatus("current")
_TrafficSegEntry_Object = MibTableRow
trafficSegEntry = _TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 9, 2, 1)
)
trafficSegEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "trafficSegIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegEntry.setStatus("current")
_TrafficSegIfIndex_Type = InterfaceIndex
_TrafficSegIfIndex_Object = MibTableColumn
trafficSegIfIndex = _TrafficSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 9, 2, 1, 1),
    _TrafficSegIfIndex_Type()
)
trafficSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegIfIndex.setStatus("current")
_TrafficSegMemberList_Type = PortList
_TrafficSegMemberList_Object = MibTableColumn
trafficSegMemberList = _TrafficSegMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 14, 9, 2, 1, 2),
    _TrafficSegMemberList_Type()
)
trafficSegMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegMemberList.setStatus("current")
_CompanyACLGroup_ObjectIdentity = ObjectIdentity
companyACLGroup = _CompanyACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15)
)
_AclProfile_ObjectIdentity = ObjectIdentity
aclProfile = _AclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1)
)
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1)
)
aclProfileEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "aclProfileNo"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 1),
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
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("arpSP_deny", 5),
          ("arpSP_permit", 4),
          ("l2", 1),
          ("l3", 2),
          ("voiceVlan", 6))
    )


_AclProfileType_Type.__name__ = "Integer32"
_AclProfileType_Object = MibTableColumn
aclProfileType = _AclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 3),
    _AclProfileRuleCount_Type()
)
aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleCount.setStatus("current")
_AclProfileMask_Type = OctetString
_AclProfileMask_Object = MibTableColumn
aclProfileMask = _AclProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 4),
    _AclProfileMask_Type()
)
aclProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileMask.setStatus("current")
_AclProfileDstMacAddrMask_Type = MacAddress
_AclProfileDstMacAddrMask_Object = MibTableColumn
aclProfileDstMacAddrMask = _AclProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 5),
    _AclProfileDstMacAddrMask_Type()
)
aclProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstMacAddrMask.setStatus("current")
_AclProfileSrcMacAddrMask_Type = MacAddress
_AclProfileSrcMacAddrMask_Object = MibTableColumn
aclProfileSrcMacAddrMask = _AclProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 6),
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


_AclProfileIPProtocol_Type.__name__ = "Integer32"
_AclProfileIPProtocol_Object = MibTableColumn
aclProfileIPProtocol = _AclProfileIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 7),
    _AclProfileIPProtocol_Type()
)
aclProfileIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileIPProtocol.setStatus("current")


class _AclProfileDstIpAddrMask_Type(IpAddress):
    """Custom type aclProfileDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclProfileDstIpAddrMask_Object = MibTableColumn
aclProfileDstIpAddrMask = _AclProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 8),
    _AclProfileDstIpAddrMask_Type()
)
aclProfileDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstIpAddrMask.setStatus("current")


class _AclProfileSrcIpAddrMask_Type(IpAddress):
    """Custom type aclProfileSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclProfileSrcIpAddrMask_Object = MibTableColumn
aclProfileSrcIpAddrMask = _AclProfileSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 12),
    _AclProfileArpSenderMacAddrMask_Type()
)
aclProfileArpSenderMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileArpSenderMacAddrMask.setStatus("current")


class _AclProfileArpSenderIpAddrMask_Type(IpAddress):
    """Custom type aclProfileArpSenderIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclProfileArpSenderIpAddrMask_Object = MibTableColumn
aclProfileArpSenderIpAddrMask = _AclProfileArpSenderIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 13),
    _AclProfileArpSenderIpAddrMask_Type()
)
aclProfileArpSenderIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileArpSenderIpAddrMask.setStatus("current")
_AclProfileStatus_Type = RowStatus
_AclProfileStatus_Object = MibTableColumn
aclProfileStatus = _AclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 1, 1, 1, 14),
    _AclProfileStatus_Type()
)
aclProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileStatus.setStatus("current")
_AclL2Rule_ObjectIdentity = ObjectIdentity
aclL2Rule = _AclL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2)
)
_AclL2RuleTable_Object = MibTable
aclL2RuleTable = _AclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    aclL2RuleTable.setStatus("current")
_AclL2RuleEntry_Object = MibTableRow
aclL2RuleEntry = _AclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1)
)
aclL2RuleEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "aclL2AccessID"),
    (0, "DGS-1500-52_AX", "aclL2ProfileID"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 3),
    _AclL2RuleEtherType_Type()
)
aclL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleEtherType.setStatus("current")
_AclL2RuleDstMacAddr_Type = MacAddress
_AclL2RuleDstMacAddr_Object = MibTableColumn
aclL2RuleDstMacAddr = _AclL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 4),
    _AclL2RuleDstMacAddr_Type()
)
aclL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddr.setStatus("current")
_AclL2RuleSrcMacAddr_Type = MacAddress
_AclL2RuleSrcMacAddr_Object = MibTableColumn
aclL2RuleSrcMacAddr = _AclL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 7),
    _AclL2Rule1pPriority_Type()
)
aclL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2Rule1pPriority.setStatus("current")
_AclL2RuleDstMacAddrMask_Type = MacAddress
_AclL2RuleDstMacAddrMask_Object = MibTableColumn
aclL2RuleDstMacAddrMask = _AclL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 8),
    _AclL2RuleDstMacAddrMask_Type()
)
aclL2RuleDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddrMask.setStatus("current")
_AclL2RuleSrcMacAddrMask_Type = MacAddress
_AclL2RuleSrcMacAddrMask_Object = MibTableColumn
aclL2RuleSrcMacAddrMask = _AclL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 9),
    _AclL2RuleSrcMacAddrMask_Type()
)
aclL2RuleSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddrMask.setStatus("current")
_AclL2RuleInPortList_Type = PortList
_AclL2RuleInPortList_Object = MibTableColumn
aclL2RuleInPortList = _AclL2RuleInPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 11),
    _AclL2RuleAction_Type()
)
aclL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleAction.setStatus("current")
_AclL2RuleStatus_Type = RowStatus
_AclL2RuleStatus_Object = MibTableColumn
aclL2RuleStatus = _AclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 2, 1, 1, 13),
    _AclL2RuleStatus_Type()
)
aclL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL2RuleStatus.setStatus("current")
_AclL3Rule_ObjectIdentity = ObjectIdentity
aclL3Rule = _AclL3Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3)
)
_AclL3RuleTable_Object = MibTable
aclL3RuleTable = _AclL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    aclL3RuleTable.setStatus("current")
_AclL3RuleEntry_Object = MibTableRow
aclL3RuleEntry = _AclL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1)
)
aclL3RuleEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "aclL3RuleAccessID"),
    (0, "DGS-1500-52_AX", "aclL3RuleProfileNo"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 11),
    _AclL3RuleTcpUdpSrcPort_Type()
)
aclL3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpSrcPort.setStatus("current")
_AclL3RuleTcpUdpDstPortMask_Type = OctetString
_AclL3RuleTcpUdpDstPortMask_Object = MibTableColumn
aclL3RuleTcpUdpDstPortMask = _AclL3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 12),
    _AclL3RuleTcpUdpDstPortMask_Type()
)
aclL3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpDstPortMask.setStatus("current")
_AclL3RuleTcpUdpSrcPortMask_Type = OctetString
_AclL3RuleTcpUdpSrcPortMask_Object = MibTableColumn
aclL3RuleTcpUdpSrcPortMask = _AclL3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 21),
    _AclL3RuleIgmpType_Type()
)
aclL3RuleIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleIgmpType.setStatus("current")
_AclL3RulePortList_Type = PortList
_AclL3RulePortList_Object = MibTableColumn
aclL3RulePortList = _AclL3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 23),
    _AclL3RuleAction_Type()
)
aclL3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleAction.setStatus("current")
_AclL3RuleStatus_Type = RowStatus
_AclL3RuleStatus_Object = MibTableColumn
aclL3RuleStatus = _AclL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 15, 3, 1, 1, 25),
    _AclL3RuleStatus_Type()
)
aclL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleStatus.setStatus("current")
_CompanySyslog_ObjectIdentity = ObjectIdentity
companySyslog = _CompanySyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16)
)
_SyslogGeneralGroup_ObjectIdentity = ObjectIdentity
syslogGeneralGroup = _SyslogGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16, 1)
)
_SyslogLogSrvAddr_Type = IpAddress
_SyslogLogSrvAddr_Object = MibScalar
syslogLogSrvAddr = _SyslogLogSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16, 1, 1),
    _SyslogLogSrvAddr_Type()
)
syslogLogSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogLogSrvAddr.setStatus("current")


class _SyslogUDPPort_Type(Integer32):
    """Custom type syslogUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SyslogUDPPort_Type.__name__ = "Integer32"
_SyslogUDPPort_Object = MibScalar
syslogUDPPort = _SyslogUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16, 1, 2),
    _SyslogUDPPort_Type()
)
syslogUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogUDPPort.setStatus("current")


class _SyslogTimeStamp_Type(Integer32):
    """Custom type syslogTimeStamp based on Integer32"""
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


_SyslogTimeStamp_Type.__name__ = "Integer32"
_SyslogTimeStamp_Object = MibScalar
syslogTimeStamp = _SyslogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16, 1, 3),
    _SyslogTimeStamp_Type()
)
syslogTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogTimeStamp.setStatus("current")


class _SyslogSeverity_Type(Integer32):
    """Custom type syslogSeverity based on Integer32"""
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


_SyslogSeverity_Type.__name__ = "Integer32"
_SyslogSeverity_Object = MibScalar
syslogSeverity = _SyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16, 1, 4),
    _SyslogSeverity_Type()
)
syslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSeverity.setStatus("current")


class _SyslogFacility_Type(Integer32):
    """Custom type syslogFacility based on Integer32"""
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


_SyslogFacility_Type.__name__ = "Integer32"
_SyslogFacility_Object = MibScalar
syslogFacility = _SyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16, 1, 5),
    _SyslogFacility_Type()
)
syslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogFacility.setStatus("current")


class _SyslogLogging_Type(Integer32):
    """Custom type syslogLogging based on Integer32"""
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


_SyslogLogging_Type.__name__ = "Integer32"
_SyslogLogging_Object = MibScalar
syslogLogging = _SyslogLogging_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 16, 1, 6),
    _SyslogLogging_Type()
)
syslogLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogLogging.setStatus("current")
_CompanyLBD_ObjectIdentity = ObjectIdentity
companyLBD = _CompanyLBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 4),
    _SysLBDRecoverTime_Type()
)
sysLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDRecoverTime.setStatus("current")
_SysLBDCtrlTable_Object = MibTable
sysLBDCtrlTable = _SysLBDCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 5)
)
if mibBuilder.loadTexts:
    sysLBDCtrlTable.setStatus("current")
_SysLBDCtrlEntry_Object = MibTableRow
sysLBDCtrlEntry = _SysLBDCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 5, 1)
)
sysLBDCtrlEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "sysLBDCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysLBDCtrlEntry.setStatus("current")
_SysLBDCtrlIndex_Type = Integer32
_SysLBDCtrlIndex_Object = MibTableColumn
sysLBDCtrlIndex = _SysLBDCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 5, 1, 3),
    _SysLBDPortLoopStatus_Type()
)
sysLBDPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDPortLoopStatus.setStatus("current")
_SysLBDVlanLoopTable_Object = MibTable
sysLBDVlanLoopTable = _SysLBDVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 6)
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopTable.setStatus("current")
_SysLBDVlanLoopEntry_Object = MibTableRow
sysLBDVlanLoopEntry = _SysLBDVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 6, 1)
)
sysLBDVlanLoopEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "sysLBDVlanLoopIndex"),
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopEntry.setStatus("current")
_SysLBDVlanLoopIndex_Type = Integer32
_SysLBDVlanLoopIndex_Object = MibTableColumn
sysLBDVlanLoopIndex = _SysLBDVlanLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 6, 1, 1),
    _SysLBDVlanLoopIndex_Type()
)
sysLBDVlanLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopIndex.setStatus("current")
_SysLBDVlanLoopPorts_Type = PortList
_SysLBDVlanLoopPorts_Object = MibTableColumn
sysLBDVlanLoopPorts = _SysLBDVlanLoopPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 17, 6, 1, 2),
    _SysLBDVlanLoopPorts_Type()
)
sysLBDVlanLoopPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopPorts.setStatus("current")
_CompanyMirror_ObjectIdentity = ObjectIdentity
companyMirror = _CompanyMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 18)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 18, 1),
    _SysMirrorStatus_Type()
)
sysMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorStatus.setStatus("current")
_SysMirrorTargetPort_Type = Integer32
_SysMirrorTargetPort_Object = MibScalar
sysMirrorTargetPort = _SysMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 18, 2),
    _SysMirrorTargetPort_Type()
)
sysMirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorTargetPort.setStatus("current")
_SysMirrorCtrlIngressMirroring_Type = PortList
_SysMirrorCtrlIngressMirroring_Object = MibScalar
sysMirrorCtrlIngressMirroring = _SysMirrorCtrlIngressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 18, 3),
    _SysMirrorCtrlIngressMirroring_Type()
)
sysMirrorCtrlIngressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlIngressMirroring.setStatus("current")
_SysMirrorCtrlEgressMirroring_Type = PortList
_SysMirrorCtrlEgressMirroring_Object = MibScalar
sysMirrorCtrlEgressMirroring = _SysMirrorCtrlEgressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 18, 4),
    _SysMirrorCtrlEgressMirroring_Type()
)
sysMirrorCtrlEgressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlEgressMirroring.setStatus("current")
_CompanyTrapSetting_ObjectIdentity = ObjectIdentity
companyTrapSetting = _CompanyTrapSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19)
)
_SysTrapIP_Type = IpAddress
_SysTrapIP_Object = MibScalar
sysTrapIP = _SysTrapIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19, 2),
    _SysTrapSystemEvent_Type()
)
sysTrapSystemEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapSystemEvent.setStatus("current")


class _SysTrapPortLinkUpDownEvent_Type(Integer32):
    """Custom type sysTrapPortLinkUpDownEvent based on Integer32"""
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


_SysTrapPortLinkUpDownEvent_Type.__name__ = "Integer32"
_SysTrapPortLinkUpDownEvent_Object = MibScalar
sysTrapPortLinkUpDownEvent = _SysTrapPortLinkUpDownEvent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19, 3),
    _SysTrapPortLinkUpDownEvent_Type()
)
sysTrapPortLinkUpDownEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPortLinkUpDownEvent.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19, 5),
    _SysTrapFirmUpgradeEvent_Type()
)
sysTrapFirmUpgradeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapFirmUpgradeEvent.setStatus("current")


class _SysTrapGratuitousARP_Type(Integer32):
    """Custom type sysTrapGratuitousARP based on Integer32"""
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


_SysTrapGratuitousARP_Type.__name__ = "Integer32"
_SysTrapGratuitousARP_Object = MibScalar
sysTrapGratuitousARP = _SysTrapGratuitousARP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19, 9),
    _SysTrapGratuitousARP_Type()
)
sysTrapGratuitousARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapGratuitousARP.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 19, 11),
    _SysTrapStatus_Type()
)
sysTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapStatus.setStatus("current")
_CompanySNTPSetting_ObjectIdentity = ObjectIdentity
companySNTPSetting = _CompanySNTPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20)
)
_SysSNTPTimeSeconds_Type = Integer32
_SysSNTPTimeSeconds_Object = MibScalar
sysSNTPTimeSeconds = _SysSNTPTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 1),
    _SysSNTPTimeSeconds_Type()
)
sysSNTPTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPTimeSeconds.setStatus("current")
_SysSNTPFirstServer_Type = IpAddress
_SysSNTPFirstServer_Object = MibScalar
sysSNTPFirstServer = _SysSNTPFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 2),
    _SysSNTPFirstServer_Type()
)
sysSNTPFirstServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstServer.setStatus("current")
_SysSNTPSecondServer_Type = IpAddress
_SysSNTPSecondServer_Object = MibScalar
sysSNTPSecondServer = _SysSNTPSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 3),
    _SysSNTPSecondServer_Type()
)
sysSNTPSecondServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondServer.setStatus("current")
_SysSNTPPollInterval_Type = Integer32
_SysSNTPPollInterval_Object = MibScalar
sysSNTPPollInterval = _SysSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 6),
    _SysSNTPDSTOffset_Type()
)
sysSNTPDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTOffset.setStatus("current")
_SysSNTPGMTMinutes_Type = Integer32
_SysSNTPGMTMinutes_Object = MibScalar
sysSNTPGMTMinutes = _SysSNTPGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 7),
    _SysSNTPGMTMinutes_Type()
)
sysSNTPGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPGMTMinutes.setStatus("current")
_SysSNTPDSTStartMon_Type = Integer32
_SysSNTPDSTStartMon_Object = MibScalar
sysSNTPDSTStartMon = _SysSNTPDSTStartMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 8),
    _SysSNTPDSTStartMon_Type()
)
sysSNTPDSTStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMon.setStatus("current")
_SysSNTPDSTStartDay_Type = Integer32
_SysSNTPDSTStartDay_Object = MibScalar
sysSNTPDSTStartDay = _SysSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 9),
    _SysSNTPDSTStartDay_Type()
)
sysSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartDay.setStatus("current")
_SysSNTPDSTStartHour_Type = Integer32
_SysSNTPDSTStartHour_Object = MibScalar
sysSNTPDSTStartHour = _SysSNTPDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 10),
    _SysSNTPDSTStartHour_Type()
)
sysSNTPDSTStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartHour.setStatus("current")
_SysSNTPDSTStartMin_Type = Integer32
_SysSNTPDSTStartMin_Object = MibScalar
sysSNTPDSTStartMin = _SysSNTPDSTStartMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 11),
    _SysSNTPDSTStartMin_Type()
)
sysSNTPDSTStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMin.setStatus("current")
_SysSNTPDSTEndMon_Type = Integer32
_SysSNTPDSTEndMon_Object = MibScalar
sysSNTPDSTEndMon = _SysSNTPDSTEndMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 12),
    _SysSNTPDSTEndMon_Type()
)
sysSNTPDSTEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndMon.setStatus("current")
_SysSNTPDSTEndDay_Type = Integer32
_SysSNTPDSTEndDay_Object = MibScalar
sysSNTPDSTEndDay = _SysSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 13),
    _SysSNTPDSTEndDay_Type()
)
sysSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndDay.setStatus("current")
_SysSNTPDSTEndHour_Type = Integer32
_SysSNTPDSTEndHour_Object = MibScalar
sysSNTPDSTEndHour = _SysSNTPDSTEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 14),
    _SysSNTPDSTEndHour_Type()
)
sysSNTPDSTEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndHour.setStatus("current")
_SysSNTPDSTEndMin_Type = Integer32
_SysSNTPDSTEndMin_Object = MibScalar
sysSNTPDSTEndMin = _SysSNTPDSTEndMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 20, 16),
    _SysSNTPDSTState_Type()
)
sysSNTPDSTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTState.setStatus("current")
_CompanyVoiceVlan_ObjectIdentity = ObjectIdentity
companyVoiceVlan = _CompanyVoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21)
)
_VoicevlanSystem_ObjectIdentity = ObjectIdentity
voicevlanSystem = _VoicevlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 2),
    _VoiceVlanMode_Type()
)
voiceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanMode.setStatus("current")
_VoiceVlanId_Type = Integer32
_VoiceVlanId_Object = MibScalar
voiceVlanId = _VoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 3),
    _VoiceVlanId_Type()
)
voiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanId.setStatus("current")
_VoiceVlanTimeout_Type = Integer32
_VoiceVlanTimeout_Object = MibScalar
voiceVlanTimeout = _VoiceVlanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 5),
    _VoiceVlanPriority_Type()
)
voiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPriority.setStatus("current")
_VoicevlanPortControlTable_Object = MibTable
voicevlanPortControlTable = _VoicevlanPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 6)
)
if mibBuilder.loadTexts:
    voicevlanPortControlTable.setStatus("current")
_VoicevlanPortControlEntry_Object = MibTableRow
voicevlanPortControlEntry = _VoicevlanPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 6, 1)
)
voicevlanPortControlEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "voicevlanPortControlIndex"),
)
if mibBuilder.loadTexts:
    voicevlanPortControlEntry.setStatus("current")
_VoicevlanPortControlIndex_Type = InterfaceIndex
_VoicevlanPortControlIndex_Object = MibTableColumn
voicevlanPortControlIndex = _VoicevlanPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 6, 1, 3),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_VoicevlanPortCurrentTagMode_Type.__name__ = "Integer32"
_VoicevlanPortCurrentTagMode_Object = MibTableColumn
voicevlanPortCurrentTagMode = _VoicevlanPortCurrentTagMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 1, 6, 1, 5),
    _VoicevlanPortState_Type()
)
voicevlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanPortState.setStatus("current")
_VoicevlanOUI_ObjectIdentity = ObjectIdentity
voicevlanOUI = _VoicevlanOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 2)
)
_VoicevlanOUITable_Object = MibTable
voicevlanOUITable = _VoicevlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    voicevlanOUITable.setStatus("current")
_VoicevlanOUIEntry_Object = MibTableRow
voicevlanOUIEntry = _VoicevlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 2, 1, 1)
)
voicevlanOUIEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "voicevlanOUITelephonyOUI"),
)
if mibBuilder.loadTexts:
    voicevlanOUIEntry.setStatus("current")
_VoicevlanOUITelephonyOUI_Type = MacAddress
_VoicevlanOUITelephonyOUI_Object = MibTableColumn
voicevlanOUITelephonyOUI = _VoicevlanOUITelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 2, 1, 1, 1),
    _VoicevlanOUITelephonyOUI_Type()
)
voicevlanOUITelephonyOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUITelephonyOUI.setStatus("current")
_VoicevlanOUIDescription_Type = OctetString
_VoicevlanOUIDescription_Object = MibTableColumn
voicevlanOUIDescription = _VoicevlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 2, 1, 1, 2),
    _VoicevlanOUIDescription_Type()
)
voicevlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanOUIDescription.setStatus("current")
_VoicevlanOUIMask_Type = MacAddress
_VoicevlanOUIMask_Object = MibTableColumn
voicevlanOUIMask = _VoicevlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 2, 1, 1, 3),
    _VoicevlanOUIMask_Type()
)
voicevlanOUIMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUIMask.setStatus("current")
_VoicevlanOUIStatus_Type = RowStatus
_VoicevlanOUIStatus_Object = MibTableColumn
voicevlanOUIStatus = _VoicevlanOUIStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 2, 1, 1, 4),
    _VoicevlanOUIStatus_Type()
)
voicevlanOUIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanOUIStatus.setStatus("current")
_VoicevlanDevice_ObjectIdentity = ObjectIdentity
voicevlanDevice = _VoicevlanDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3)
)
_VoicevlanDeviceTable_Object = MibTable
voicevlanDeviceTable = _VoicevlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3, 1)
)
if mibBuilder.loadTexts:
    voicevlanDeviceTable.setStatus("current")
_VoicevlanDeviceEntry_Object = MibTableRow
voicevlanDeviceEntry = _VoicevlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3, 1, 1)
)
voicevlanDeviceEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "voicevlanDeviceIndexMac"),
)
if mibBuilder.loadTexts:
    voicevlanDeviceEntry.setStatus("current")
_VoicevlanDeviceIndexMac_Type = MacAddress
_VoicevlanDeviceIndexMac_Object = MibTableColumn
voicevlanDeviceIndexMac = _VoicevlanDeviceIndexMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3, 1, 1, 1),
    _VoicevlanDeviceIndexMac_Type()
)
voicevlanDeviceIndexMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDeviceIndexMac.setStatus("current")
_VoicevlanDevicePort_Type = Integer32
_VoicevlanDevicePort_Object = MibTableColumn
voicevlanDevicePort = _VoicevlanDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3, 1, 1, 2),
    _VoicevlanDevicePort_Type()
)
voicevlanDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDevicePort.setStatus("current")
_VoicevlanDevicePriority_Type = Integer32
_VoicevlanDevicePriority_Object = MibTableColumn
voicevlanDevicePriority = _VoicevlanDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 21, 3, 1, 1, 5),
    _VoicevlanDeviceStatus_Type()
)
voicevlanDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanDeviceStatus.setStatus("current")
_CompanyRMON_ObjectIdentity = ObjectIdentity
companyRMON = _CompanyRMON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 1),
    _RmonGlobalState_Type()
)
rmonGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonGlobalState.setStatus("current")
_RmonStatistics_ObjectIdentity = ObjectIdentity
rmonStatistics = _RmonStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 2)
)
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 2, 1)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 2, 1, 1)
)
rmonStatsEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "rmonStatsIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 2, 1, 1, 1),
    _RmonStatsIndex_Type()
)
rmonStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsIndex.setStatus("current")
_RmonStatsDataSource_Type = ObjectIdentifier
_RmonStatsDataSource_Object = MibTableColumn
rmonStatsDataSource = _RmonStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 2, 1, 1, 3),
    _RmonStatsOwner_Type()
)
rmonStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsOwner.setStatus("current")
_RmonStatsStatus_Type = RmonStatus
_RmonStatsStatus_Object = MibTableColumn
rmonStatsStatus = _RmonStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 2, 1, 1, 4),
    _RmonStatsStatus_Type()
)
rmonStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsStatus.setStatus("current")
_RmonHistory_ObjectIdentity = ObjectIdentity
rmonHistory = _RmonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3)
)
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "rmonHistoryIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")
_RmonHistoryDataSource_Type = ObjectIdentifier
_RmonHistoryDataSource_Object = MibTableColumn
rmonHistoryDataSource = _RmonHistoryDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1, 1, 5),
    _RmonHistoryOwner_Type()
)
rmonHistoryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryOwner.setStatus("current")
_RmonHistoryStatus_Type = RmonStatus
_RmonHistoryStatus_Object = MibTableColumn
rmonHistoryStatus = _RmonHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 3, 1, 1, 6),
    _RmonHistoryStatus_Type()
)
rmonHistoryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryStatus.setStatus("current")
_RmonAlarm_ObjectIdentity = ObjectIdentity
rmonAlarm = _RmonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4)
)
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "rmonAlarmIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")
_RmonAlarmInterval_Type = Integer32
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")
_RmonAlarmRisingThreshold_Type = Integer32
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 5),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")
_RmonAlarmFallingThreshold_Type = Integer32
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 9),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")
_RmonAlarmStatus_Type = RmonStatus
_RmonAlarmStatus_Object = MibTableColumn
rmonAlarmStatus = _RmonAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 4, 1, 1, 10),
    _RmonAlarmStatus_Type()
)
rmonAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmStatus.setStatus("current")
_RmonEvent_ObjectIdentity = ObjectIdentity
rmonEvent = _RmonEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5)
)
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1, 1)
)
rmonEventEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "rmonEventIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")
_RmonEventStatus_Type = RmonStatus
_RmonEventStatus_Object = MibTableColumn
rmonEventStatus = _RmonEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 22, 5, 1, 1, 6),
    _RmonEventStatus_Type()
)
rmonEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventStatus.setStatus("current")
_CompanyAuthGroup_ObjectIdentity = ObjectIdentity
companyAuthGroup = _CompanyAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23)
)
_SwAuthenCtrl_ObjectIdentity = ObjectIdentity
swAuthenCtrl = _SwAuthenCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 1)
)


class _SwAuthStatus_Type(Integer32):
    """Custom type swAuthStatus based on Integer32"""
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


_SwAuthStatus_Type.__name__ = "Integer32"
_SwAuthStatus_Object = MibScalar
swAuthStatus = _SwAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 1, 1),
    _SwAuthStatus_Type()
)
swAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthStatus.setStatus("current")


class _AuthProtocol_Type(Integer32):
    """Custom type authProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authProtocolLocal", 2),
          ("authProtocolRadiusEap", 1))
    )


_AuthProtocol_Type.__name__ = "Integer32"
_AuthProtocol_Object = MibScalar
authProtocol = _AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 1, 3),
    _AuthProtocol_Type()
)
authProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authProtocol.setStatus("current")


class _SwAuthCtrlPktFwdMode_Type(Integer32):
    """Custom type swAuthCtrlPktFwdMode based on Integer32"""
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


_SwAuthCtrlPktFwdMode_Type.__name__ = "Integer32"
_SwAuthCtrlPktFwdMode_Object = MibScalar
swAuthCtrlPktFwdMode = _SwAuthCtrlPktFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 1, 4),
    _SwAuthCtrlPktFwdMode_Type()
)
swAuthCtrlPktFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthCtrlPktFwdMode.setStatus("current")
_SwAuthPortAccessCtrl_ObjectIdentity = ObjectIdentity
swAuthPortAccessCtrl = _SwAuthPortAccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2)
)
_SwAuthPortAccessControlTable_Object = MibTable
swAuthPortAccessControlTable = _SwAuthPortAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlTable.setStatus("current")
_SwAuthPortAccessControlEntry_Object = MibTableRow
swAuthPortAccessControlEntry = _SwAuthPortAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1)
)
swAuthPortAccessControlEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "swAuthAuthConfigPortNumber"),
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlEntry.setStatus("current")
_SwAuthAuthConfigPortNumber_Type = Integer32
_SwAuthAuthConfigPortNumber_Object = MibTableColumn
swAuthAuthConfigPortNumber = _SwAuthAuthConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 1),
    _SwAuthAuthConfigPortNumber_Type()
)
swAuthAuthConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthConfigPortNumber.setStatus("current")


class _SwAuthAuthQuietPeriod_Type(Integer32):
    """Custom type swAuthAuthQuietPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwAuthAuthQuietPeriod_Type.__name__ = "Integer32"
_SwAuthAuthQuietPeriod_Object = MibTableColumn
swAuthAuthQuietPeriod = _SwAuthAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 2),
    _SwAuthAuthQuietPeriod_Type()
)
swAuthAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthQuietPeriod.setStatus("current")


class _SwAuthAuthSuppTimeout_Type(Integer32):
    """Custom type swAuthAuthSuppTimeout based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAuthAuthSuppTimeout_Type.__name__ = "Integer32"
_SwAuthAuthSuppTimeout_Object = MibTableColumn
swAuthAuthSuppTimeout = _SwAuthAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 3),
    _SwAuthAuthSuppTimeout_Type()
)
swAuthAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthSuppTimeout.setStatus("current")


class _SwAuthAuthServerTimeout_Type(Integer32):
    """Custom type swAuthAuthServerTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAuthAuthServerTimeout_Type.__name__ = "Integer32"
_SwAuthAuthServerTimeout_Object = MibTableColumn
swAuthAuthServerTimeout = _SwAuthAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 4),
    _SwAuthAuthServerTimeout_Type()
)
swAuthAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthServerTimeout.setStatus("current")


class _SwAuthAuthMaxReq_Type(Integer32):
    """Custom type swAuthAuthMaxReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SwAuthAuthMaxReq_Type.__name__ = "Integer32"
_SwAuthAuthMaxReq_Object = MibTableColumn
swAuthAuthMaxReq = _SwAuthAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 5),
    _SwAuthAuthMaxReq_Type()
)
swAuthAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthMaxReq.setStatus("current")


class _SwAuthAuthTxPeriod_Type(Integer32):
    """Custom type swAuthAuthTxPeriod based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAuthAuthTxPeriod_Type.__name__ = "Integer32"
_SwAuthAuthTxPeriod_Object = MibTableColumn
swAuthAuthTxPeriod = _SwAuthAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 6),
    _SwAuthAuthTxPeriod_Type()
)
swAuthAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthTxPeriod.setStatus("current")


class _SwAuthAuthReAuthPeriod_Type(Integer32):
    """Custom type swAuthAuthReAuthPeriod based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAuthAuthReAuthPeriod_Type.__name__ = "Integer32"
_SwAuthAuthReAuthPeriod_Object = MibTableColumn
swAuthAuthReAuthPeriod = _SwAuthAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 7),
    _SwAuthAuthReAuthPeriod_Type()
)
swAuthAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthReAuthPeriod.setStatus("current")


class _SwAuthAuthReAuthentication_Type(Integer32):
    """Custom type swAuthAuthReAuthentication based on Integer32"""
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


_SwAuthAuthReAuthentication_Type.__name__ = "Integer32"
_SwAuthAuthReAuthentication_Object = MibTableColumn
swAuthAuthReAuthentication = _SwAuthAuthReAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 8),
    _SwAuthAuthReAuthentication_Type()
)
swAuthAuthReAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthReAuthentication.setStatus("current")


class _SwAuthAuthConfigPortControl_Type(Integer32):
    """Custom type swAuthAuthConfigPortControl based on Integer32"""
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


_SwAuthAuthConfigPortControl_Type.__name__ = "Integer32"
_SwAuthAuthConfigPortControl_Object = MibTableColumn
swAuthAuthConfigPortControl = _SwAuthAuthConfigPortControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 9),
    _SwAuthAuthConfigPortControl_Type()
)
swAuthAuthConfigPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthConfigPortControl.setStatus("current")


class _SwAuthAuthCapability_Type(Integer32):
    """Custom type swAuthAuthCapability based on Integer32"""
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


_SwAuthAuthCapability_Type.__name__ = "Integer32"
_SwAuthAuthCapability_Object = MibTableColumn
swAuthAuthCapability = _SwAuthAuthCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 10),
    _SwAuthAuthCapability_Type()
)
swAuthAuthCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthCapability.setStatus("current")


class _SwAuthAuthDirection_Type(Integer32):
    """Custom type swAuthAuthDirection based on Integer32"""
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


_SwAuthAuthDirection_Type.__name__ = "Integer32"
_SwAuthAuthDirection_Object = MibTableColumn
swAuthAuthDirection = _SwAuthAuthDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 2, 1, 1, 11),
    _SwAuthAuthDirection_Type()
)
swAuthAuthDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthDirection.setStatus("current")
_SwAuthUser_ObjectIdentity = ObjectIdentity
swAuthUser = _SwAuthUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 3)
)
_SwAuthUserTable_Object = MibTable
swAuthUserTable = _SwAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 3, 1)
)
if mibBuilder.loadTexts:
    swAuthUserTable.setStatus("current")
_SwAuthUserEntry_Object = MibTableRow
swAuthUserEntry = _SwAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 3, 1, 1)
)
swAuthUserEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "swAuthUserName"),
)
if mibBuilder.loadTexts:
    swAuthUserEntry.setStatus("current")


class _SwAuthUserName_Type(SnmpAdminString):
    """Custom type swAuthUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAuthUserName_Type.__name__ = "SnmpAdminString"
_SwAuthUserName_Object = MibTableColumn
swAuthUserName = _SwAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 3, 1, 1, 1),
    _SwAuthUserName_Type()
)
swAuthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthUserName.setStatus("current")


class _SwAuthUserPassword_Type(DisplayString):
    """Custom type swAuthUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAuthUserPassword_Type.__name__ = "DisplayString"
_SwAuthUserPassword_Object = MibTableColumn
swAuthUserPassword = _SwAuthUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 3, 1, 1, 2),
    _SwAuthUserPassword_Type()
)
swAuthUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthUserPassword.setStatus("current")
_SwAuthUserStatus_Type = RowStatus
_SwAuthUserStatus_Object = MibTableColumn
swAuthUserStatus = _SwAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 3, 1, 1, 3),
    _SwAuthUserStatus_Type()
)
swAuthUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthUserStatus.setStatus("current")
_SwAuthRadiusServer_ObjectIdentity = ObjectIdentity
swAuthRadiusServer = _SwAuthRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4)
)
_SwAuthRadiusServerTable_Object = MibTable
swAuthRadiusServerTable = _SwAuthRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1)
)
if mibBuilder.loadTexts:
    swAuthRadiusServerTable.setStatus("current")
_SwAuthRadiusServerEntry_Object = MibTableRow
swAuthRadiusServerEntry = _SwAuthRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1)
)
swAuthRadiusServerEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "swAuthRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    swAuthRadiusServerEntry.setStatus("current")


class _SwAuthRadiusServerIndex_Type(Integer32):
    """Custom type swAuthRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwAuthRadiusServerIndex_Type.__name__ = "Integer32"
_SwAuthRadiusServerIndex_Object = MibTableColumn
swAuthRadiusServerIndex = _SwAuthRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 1),
    _SwAuthRadiusServerIndex_Type()
)
swAuthRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthRadiusServerIndex.setStatus("current")
_SwAuthRadiusServerAddress_Type = IpAddress
_SwAuthRadiusServerAddress_Object = MibTableColumn
swAuthRadiusServerAddress = _SwAuthRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 2),
    _SwAuthRadiusServerAddress_Type()
)
swAuthRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerAddress.setStatus("current")


class _SwAuthRadiusServerAuthenticationPort_Type(Integer32):
    """Custom type swAuthRadiusServerAuthenticationPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAuthRadiusServerAuthenticationPort_Type.__name__ = "Integer32"
_SwAuthRadiusServerAuthenticationPort_Object = MibTableColumn
swAuthRadiusServerAuthenticationPort = _SwAuthRadiusServerAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 3),
    _SwAuthRadiusServerAuthenticationPort_Type()
)
swAuthRadiusServerAuthenticationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerAuthenticationPort.setStatus("current")


class _SwAuthRadiusServerAccountingPort_Type(Integer32):
    """Custom type swAuthRadiusServerAccountingPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwAuthRadiusServerAccountingPort_Type.__name__ = "Integer32"
_SwAuthRadiusServerAccountingPort_Object = MibTableColumn
swAuthRadiusServerAccountingPort = _SwAuthRadiusServerAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 4),
    _SwAuthRadiusServerAccountingPort_Type()
)
swAuthRadiusServerAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerAccountingPort.setStatus("current")


class _SwAuthRadiusServerTimeout_Type(Integer32):
    """Custom type swAuthRadiusServerTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwAuthRadiusServerTimeout_Type.__name__ = "Integer32"
_SwAuthRadiusServerTimeout_Object = MibTableColumn
swAuthRadiusServerTimeout = _SwAuthRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 5),
    _SwAuthRadiusServerTimeout_Type()
)
swAuthRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerTimeout.setStatus("current")


class _SwAuthRadiusServerRetransmit_Type(Integer32):
    """Custom type swAuthRadiusServerRetransmit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwAuthRadiusServerRetransmit_Type.__name__ = "Integer32"
_SwAuthRadiusServerRetransmit_Object = MibTableColumn
swAuthRadiusServerRetransmit = _SwAuthRadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 6),
    _SwAuthRadiusServerRetransmit_Type()
)
swAuthRadiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerRetransmit.setStatus("current")


class _SwAuthRadiusServerKey_Type(DisplayString):
    """Custom type swAuthRadiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwAuthRadiusServerKey_Type.__name__ = "DisplayString"
_SwAuthRadiusServerKey_Object = MibTableColumn
swAuthRadiusServerKey = _SwAuthRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 7),
    _SwAuthRadiusServerKey_Type()
)
swAuthRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerKey.setStatus("current")
_SwAuthRadiusServerStatus_Type = RowStatus
_SwAuthRadiusServerStatus_Object = MibTableColumn
swAuthRadiusServerStatus = _SwAuthRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 23, 4, 1, 1, 8),
    _SwAuthRadiusServerStatus_Type()
)
swAuthRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthRadiusServerStatus.setStatus("current")
_CompanyLLDPSetting_ObjectIdentity = ObjectIdentity
companyLLDPSetting = _CompanyLLDPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 5),
    _DlinklldpTxDelay_Type()
)
dlinklldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpTxDelay.setStatus("current")
_DlinklldpConfigManAddrTable_Object = MibTable
dlinklldpConfigManAddrTable = _DlinklldpConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 7)
)
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrTable.setStatus("current")
_DlinklldpConfigManAddrEntry_Object = MibTableRow
dlinklldpConfigManAddrEntry = _DlinklldpConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 7, 1)
)
dlinklldpConfigManAddrEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "dlinklldpLocManAddrSubtype"),
    (0, "DGS-1500-52_AX", "dlinklldpLocManAddr"),
)
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrEntry.setStatus("current")
_DlinklldpLocManAddrSubtype_Type = AddressFamilyNumbers
_DlinklldpLocManAddrSubtype_Object = MibTableColumn
dlinklldpLocManAddrSubtype = _DlinklldpLocManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 7, 1, 1),
    _DlinklldpLocManAddrSubtype_Type()
)
dlinklldpLocManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlinklldpLocManAddrSubtype.setStatus("current")
_DlinklldpLocManAddr_Type = LldpManAddress
_DlinklldpLocManAddr_Object = MibTableColumn
dlinklldpLocManAddr = _DlinklldpLocManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 24, 7, 1, 3),
    _DlinklldpConfigManAddrPortsTxEnable_Type()
)
dlinklldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrPortsTxEnable.setStatus("current")
_CompanySNMPV3_ObjectIdentity = ObjectIdentity
companySNMPV3 = _CompanySNMPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 1),
    _SnmpGlobalState_Type()
)
snmpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGlobalState.setStatus("current")
_SnmpV3User_ObjectIdentity = ObjectIdentity
snmpV3User = _SnmpV3User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2)
)
_SnmpV3UserTable_Object = MibTable
snmpV3UserTable = _SnmpV3UserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1)
)
if mibBuilder.loadTexts:
    snmpV3UserTable.setStatus("current")
_SnmpV3UserEntry_Object = MibTableRow
snmpV3UserEntry = _SnmpV3UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1)
)
snmpV3UserEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "snmpV3UserName"),
    (0, "DGS-1500-52_AX", "snmpV3UserVersion"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 7),
    _SnmpV3UserPrivProtocolPassword_Type()
)
snmpV3UserPrivProtocolPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserPrivProtocolPassword.setStatus("current")
_SnmpV3UserStatus_Type = RowStatus
_SnmpV3UserStatus_Object = MibTableColumn
snmpV3UserStatus = _SnmpV3UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 2, 1, 1, 8),
    _SnmpV3UserStatus_Type()
)
snmpV3UserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserStatus.setStatus("current")
_SnmpV3Group_ObjectIdentity = ObjectIdentity
snmpV3Group = _SnmpV3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3)
)
_SnmpV3GroupTable_Object = MibTable
snmpV3GroupTable = _SnmpV3GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1)
)
if mibBuilder.loadTexts:
    snmpV3GroupTable.setStatus("current")
_SnmpV3GroupEntry_Object = MibTableRow
snmpV3GroupEntry = _SnmpV3GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1)
)
snmpV3GroupEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "snmpV3GroupName"),
    (0, "DGS-1500-52_AX", "snmpV3GroupSecurityModel"),
    (0, "DGS-1500-52_AX", "snmpV3GroupSecurityLevel"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1, 2),
    _SnmpV3GroupSecurityModel_Type()
)
snmpV3GroupSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3GroupSecurityModel.setStatus("current")
_SnmpV3GroupSecurityLevel_Type = SnmpSecurityLevel
_SnmpV3GroupSecurityLevel_Object = MibTableColumn
snmpV3GroupSecurityLevel = _SnmpV3GroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1, 6),
    _SnmpV3GroupNotifyViewName_Type()
)
snmpV3GroupNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupNotifyViewName.setStatus("current")
_SnmpV3GroupStatus_Type = RowStatus
_SnmpV3GroupStatus_Object = MibTableColumn
snmpV3GroupStatus = _SnmpV3GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 3, 1, 1, 7),
    _SnmpV3GroupStatus_Type()
)
snmpV3GroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupStatus.setStatus("current")
_SnmpV3ViewTree_ObjectIdentity = ObjectIdentity
snmpV3ViewTree = _SnmpV3ViewTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4)
)
_SnmpV3ViewTreeTable_Object = MibTable
snmpV3ViewTreeTable = _SnmpV3ViewTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4, 1)
)
if mibBuilder.loadTexts:
    snmpV3ViewTreeTable.setStatus("current")
_SnmpV3ViewTreeEntry_Object = MibTableRow
snmpV3ViewTreeEntry = _SnmpV3ViewTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4, 1, 1)
)
snmpV3ViewTreeEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "snmpV3viewTreeName"),
    (0, "DGS-1500-52_AX", "snmpV3viewTreeSubtree"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4, 1, 1, 1),
    _SnmpV3viewTreeName_Type()
)
snmpV3viewTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3viewTreeName.setStatus("current")
_SnmpV3viewTreeSubtree_Type = ObjectIdentifier
_SnmpV3viewTreeSubtree_Object = MibTableColumn
snmpV3viewTreeSubtree = _SnmpV3viewTreeSubtree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4, 1, 1, 4),
    _SnmpV3viewTreeType_Type()
)
snmpV3viewTreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeType.setStatus("current")
_SnmpV3viewTreeStatus_Type = RowStatus
_SnmpV3viewTreeStatus_Object = MibTableColumn
snmpV3viewTreeStatus = _SnmpV3viewTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 4, 1, 1, 5),
    _SnmpV3viewTreeStatus_Type()
)
snmpV3viewTreeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeStatus.setStatus("current")
_SnmpV3Community_ObjectIdentity = ObjectIdentity
snmpV3Community = _SnmpV3Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 5)
)
_SnmpV3CommunityTable_Object = MibTable
snmpV3CommunityTable = _SnmpV3CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 5, 1)
)
if mibBuilder.loadTexts:
    snmpV3CommunityTable.setStatus("current")
_SnmpV3CommunityEntry_Object = MibTableRow
snmpV3CommunityEntry = _SnmpV3CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 5, 1, 1)
)
snmpV3CommunityEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "snmpV3CommunityName"),
)
if mibBuilder.loadTexts:
    snmpV3CommunityEntry.setStatus("current")
_SnmpV3CommunityName_Type = OctetString
_SnmpV3CommunityName_Object = MibTableColumn
snmpV3CommunityName = _SnmpV3CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 5, 1, 1, 2),
    _SnmpV3CommunityPolicy_Type()
)
snmpV3CommunityPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityPolicy.setStatus("current")
_SnmpV3CommunityStatus_Type = RowStatus
_SnmpV3CommunityStatus_Object = MibTableColumn
snmpV3CommunityStatus = _SnmpV3CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 5, 1, 1, 3),
    _SnmpV3CommunityStatus_Type()
)
snmpV3CommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityStatus.setStatus("current")
_SnmpV3Host_ObjectIdentity = ObjectIdentity
snmpV3Host = _SnmpV3Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 6)
)
_SnmpV3HostTable_Object = MibTable
snmpV3HostTable = _SnmpV3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 6, 1)
)
if mibBuilder.loadTexts:
    snmpV3HostTable.setStatus("current")
_SnmpV3HostEntry_Object = MibTableRow
snmpV3HostEntry = _SnmpV3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 6, 1, 1)
)
snmpV3HostEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "snmpV3HostAddress"),
)
if mibBuilder.loadTexts:
    snmpV3HostEntry.setStatus("current")
_SnmpV3HostAddress_Type = IpAddress
_SnmpV3HostAddress_Object = MibTableColumn
snmpV3HostAddress = _SnmpV3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 6, 1, 1, 1),
    _SnmpV3HostAddress_Type()
)
snmpV3HostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3HostAddress.setStatus("current")


class _SnmpV3HostCommunityName_Type(SnmpAdminString):
    """Custom type snmpV3HostCommunityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpV3HostCommunityName_Type.__name__ = "SnmpAdminString"
_SnmpV3HostCommunityName_Object = MibTableColumn
snmpV3HostCommunityName = _SnmpV3HostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 6, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 6, 1, 1, 3),
    _SnmpV3HostVersion_Type()
)
snmpV3HostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostVersion.setStatus("current")
_SnmpV3HostStatus_Type = RowStatus
_SnmpV3HostStatus_Object = MibTableColumn
snmpV3HostStatus = _SnmpV3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 6, 1, 1, 4),
    _SnmpV3HostStatus_Type()
)
snmpV3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostStatus.setStatus("current")
_SnmpV3EngineID_Type = SnmpEngineID
_SnmpV3EngineID_Object = MibScalar
snmpV3EngineID = _SnmpV3EngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 7),
    _SnmpV3EngineID_Type()
)
snmpV3EngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3EngineID.setStatus("current")
_SnmpV3Trap_ObjectIdentity = ObjectIdentity
snmpV3Trap = _SnmpV3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 8)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 8, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 8, 5),
    _SnmpV3TrapFirmUpgrade_Type()
)
snmpV3TrapFirmUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapFirmUpgrade.setStatus("current")


class _SnmpV3TrapGratuitousARP_Type(Integer32):
    """Custom type snmpV3TrapGratuitousARP based on Integer32"""
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


_SnmpV3TrapGratuitousARP_Type.__name__ = "Integer32"
_SnmpV3TrapGratuitousARP_Object = MibScalar
snmpV3TrapGratuitousARP = _SnmpV3TrapGratuitousARP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 25, 8, 9),
    _SnmpV3TrapGratuitousARP_Type()
)
snmpV3TrapGratuitousARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapGratuitousARP.setStatus("current")
_CompanyAutoSurveillanceVlan_ObjectIdentity = ObjectIdentity
companyAutoSurveillanceVlan = _CompanyAutoSurveillanceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26)
)
_AutoSurveillanceVlanSystem_ObjectIdentity = ObjectIdentity
autoSurveillanceVlanSystem = _AutoSurveillanceVlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 1, 1),
    _AutoSurveillanceVlanMode_Type()
)
autoSurveillanceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanMode.setStatus("current")
_AutoSurveillanceVlanId_Type = Integer32
_AutoSurveillanceVlanId_Object = MibScalar
autoSurveillanceVlanId = _AutoSurveillanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 1, 3),
    _AutoSurveillanceVlanPriority_Type()
)
autoSurveillanceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanPriority.setStatus("current")
_AutoSurveillanceVlanTaggedUplinkDownlinkPort_Type = PortList
_AutoSurveillanceVlanTaggedUplinkDownlinkPort_Object = MibScalar
autoSurveillanceVlanTaggedUplinkDownlinkPort = _AutoSurveillanceVlanTaggedUplinkDownlinkPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 1, 4),
    _AutoSurveillanceVlanTaggedUplinkDownlinkPort_Type()
)
autoSurveillanceVlanTaggedUplinkDownlinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanTaggedUplinkDownlinkPort.setStatus("current")
_AutoSurveillanceVlanOUI_ObjectIdentity = ObjectIdentity
autoSurveillanceVlanOUI = _AutoSurveillanceVlanOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2)
)
_AutoSurveillanceVlanOUITable_Object = MibTable
autoSurveillanceVlanOUITable = _AutoSurveillanceVlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2, 1)
)
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUITable.setStatus("current")
_AutoSurveillanceVlanOUIEntry_Object = MibTableRow
autoSurveillanceVlanOUIEntry = _AutoSurveillanceVlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2, 1, 1)
)
autoSurveillanceVlanOUIEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "autoSurveillanceVlanOUISurveillanceOUI"),
)
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIEntry.setStatus("current")
_AutoSurveillanceVlanOUISurveillanceOUI_Type = MacAddress
_AutoSurveillanceVlanOUISurveillanceOUI_Object = MibTableColumn
autoSurveillanceVlanOUISurveillanceOUI = _AutoSurveillanceVlanOUISurveillanceOUI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2, 1, 1, 1),
    _AutoSurveillanceVlanOUISurveillanceOUI_Type()
)
autoSurveillanceVlanOUISurveillanceOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUISurveillanceOUI.setStatus("current")
_AutoSurveillanceVlanOUIDescription_Type = OctetString
_AutoSurveillanceVlanOUIDescription_Object = MibTableColumn
autoSurveillanceVlanOUIDescription = _AutoSurveillanceVlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2, 1, 1, 2),
    _AutoSurveillanceVlanOUIDescription_Type()
)
autoSurveillanceVlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIDescription.setStatus("current")
_AutoSurveillanceVlanOUIMask_Type = MacAddress
_AutoSurveillanceVlanOUIMask_Object = MibTableColumn
autoSurveillanceVlanOUIMask = _AutoSurveillanceVlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2, 1, 1, 4),
    _AutoSurveillanceVlanOUIComponentType_Type()
)
autoSurveillanceVlanOUIComponentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIComponentType.setStatus("current")
_AutoSurveillanceVlanOUIStatus_Type = RowStatus
_AutoSurveillanceVlanOUIStatus_Object = MibTableColumn
autoSurveillanceVlanOUIStatus = _AutoSurveillanceVlanOUIStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 26, 2, 1, 1, 5),
    _AutoSurveillanceVlanOUIStatus_Type()
)
autoSurveillanceVlanOUIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIStatus.setStatus("current")
_CompanyTraps_ObjectIdentity = ObjectIdentity
companyTraps = _CompanyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0)
)
_CompanySIM_ObjectIdentity = ObjectIdentity
companySIM = _CompanySIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29)
)
_CmSingleIPMgmt_ObjectIdentity = ObjectIdentity
cmSingleIPMgmt = _CmSingleIPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1)
)
_CmSingleIPInfo_ObjectIdentity = ObjectIdentity
cmSingleIPInfo = _CmSingleIPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 1)
)


class _CmSingleIPVersion_Type(DisplayString):
    """Custom type cmSingleIPVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPVersion_Type.__name__ = "DisplayString"
_CmSingleIPVersion_Object = MibScalar
cmSingleIPVersion = _CmSingleIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 1, 1),
    _CmSingleIPVersion_Type()
)
cmSingleIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPVersion.setStatus("current")


class _CmSingleIPCapability_Type(DisplayString):
    """Custom type cmSingleIPCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPCapability_Type.__name__ = "DisplayString"
_CmSingleIPCapability_Object = MibScalar
cmSingleIPCapability = _CmSingleIPCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 1, 2),
    _CmSingleIPCapability_Type()
)
cmSingleIPCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCapability.setStatus("current")


class _CmSingleIPPlatform_Type(DisplayString):
    """Custom type cmSingleIPPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPPlatform_Type.__name__ = "DisplayString"
_CmSingleIPPlatform_Object = MibScalar
cmSingleIPPlatform = _CmSingleIPPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 1, 3),
    _CmSingleIPPlatform_Type()
)
cmSingleIPPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPPlatform.setStatus("current")
_CmSingleIPCtrl_ObjectIdentity = ObjectIdentity
cmSingleIPCtrl = _CmSingleIPCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 2)
)


class _CmSingleIPAdmin_Type(Integer32):
    """Custom type cmSingleIPAdmin based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_CmSingleIPAdmin_Type.__name__ = "Integer32"
_CmSingleIPAdmin_Object = MibScalar
cmSingleIPAdmin = _CmSingleIPAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 2, 1),
    _CmSingleIPAdmin_Type()
)
cmSingleIPAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSingleIPAdmin.setStatus("current")


class _CmSingleIPRoleState_Type(Integer32):
    """Custom type cmSingleIPRoleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("cs", 1),
          ("ms", 3))
    )


_CmSingleIPRoleState_Type.__name__ = "Integer32"
_CmSingleIPRoleState_Object = MibScalar
cmSingleIPRoleState = _CmSingleIPRoleState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 2, 2),
    _CmSingleIPRoleState_Type()
)
cmSingleIPRoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSingleIPRoleState.setStatus("current")


class _CmSingleIPHoldtime_Type(Integer32):
    """Custom type cmSingleIPHoldtime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 255),
    )


_CmSingleIPHoldtime_Type.__name__ = "Integer32"
_CmSingleIPHoldtime_Object = MibScalar
cmSingleIPHoldtime = _CmSingleIPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 2, 3),
    _CmSingleIPHoldtime_Type()
)
cmSingleIPHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSingleIPHoldtime.setStatus("current")


class _CmSingleIPTimeInterval_Type(Integer32):
    """Custom type cmSingleIPTimeInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 90),
    )


_CmSingleIPTimeInterval_Type.__name__ = "Integer32"
_CmSingleIPTimeInterval_Object = MibScalar
cmSingleIPTimeInterval = _CmSingleIPTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 2, 4),
    _CmSingleIPTimeInterval_Type()
)
cmSingleIPTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSingleIPTimeInterval.setStatus("current")
_CmSingleIPMSTable_Object = MibTable
cmSingleIPMSTable = _CmSingleIPMSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3)
)
if mibBuilder.loadTexts:
    cmSingleIPMSTable.setStatus("current")
_CmSingleIPMSEntry_Object = MibTableRow
cmSingleIPMSEntry = _CmSingleIPMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1)
)
cmSingleIPMSEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "cmSingleIPMSID"),
)
if mibBuilder.loadTexts:
    cmSingleIPMSEntry.setStatus("current")


class _CmSingleIPMSID_Type(Integer32):
    """Custom type cmSingleIPMSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CmSingleIPMSID_Type.__name__ = "Integer32"
_CmSingleIPMSID_Object = MibTableColumn
cmSingleIPMSID = _CmSingleIPMSID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 1),
    _CmSingleIPMSID_Type()
)
cmSingleIPMSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSID.setStatus("current")


class _CmSingleIPMSDeviceName_Type(DisplayString):
    """Custom type cmSingleIPMSDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPMSDeviceName_Type.__name__ = "DisplayString"
_CmSingleIPMSDeviceName_Object = MibTableColumn
cmSingleIPMSDeviceName = _CmSingleIPMSDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 2),
    _CmSingleIPMSDeviceName_Type()
)
cmSingleIPMSDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSDeviceName.setStatus("current")
_CmSingleIPMSMacAddr_Type = MacAddress
_CmSingleIPMSMacAddr_Object = MibTableColumn
cmSingleIPMSMacAddr = _CmSingleIPMSMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 3),
    _CmSingleIPMSMacAddr_Type()
)
cmSingleIPMSMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSMacAddr.setStatus("current")


class _CmSingleIPMSFirmwareVer_Type(DisplayString):
    """Custom type cmSingleIPMSFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPMSFirmwareVer_Type.__name__ = "DisplayString"
_CmSingleIPMSFirmwareVer_Object = MibTableColumn
cmSingleIPMSFirmwareVer = _CmSingleIPMSFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 4),
    _CmSingleIPMSFirmwareVer_Type()
)
cmSingleIPMSFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSFirmwareVer.setStatus("current")


class _CmSingleIPMSCapability_Type(DisplayString):
    """Custom type cmSingleIPMSCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPMSCapability_Type.__name__ = "DisplayString"
_CmSingleIPMSCapability_Object = MibTableColumn
cmSingleIPMSCapability = _CmSingleIPMSCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 5),
    _CmSingleIPMSCapability_Type()
)
cmSingleIPMSCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSCapability.setStatus("current")


class _CmSingleIPMSPlatform_Type(DisplayString):
    """Custom type cmSingleIPMSPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPMSPlatform_Type.__name__ = "DisplayString"
_CmSingleIPMSPlatform_Object = MibTableColumn
cmSingleIPMSPlatform = _CmSingleIPMSPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 6),
    _CmSingleIPMSPlatform_Type()
)
cmSingleIPMSPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSPlatform.setStatus("current")
_CmSingleIPMSHoldtime_Type = Integer32
_CmSingleIPMSHoldtime_Object = MibTableColumn
cmSingleIPMSHoldtime = _CmSingleIPMSHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 7),
    _CmSingleIPMSHoldtime_Type()
)
cmSingleIPMSHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSHoldtime.setStatus("current")
_CmSingleIPMSCasSource_Type = Integer32
_CmSingleIPMSCasSource_Object = MibTableColumn
cmSingleIPMSCasSource = _CmSingleIPMSCasSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 8),
    _CmSingleIPMSCasSource_Type()
)
cmSingleIPMSCasSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSingleIPMSCasSource.setStatus("current")
_CmSingleIPMSPassword_Type = DisplayString
_CmSingleIPMSPassword_Object = MibTableColumn
cmSingleIPMSPassword = _CmSingleIPMSPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 9),
    _CmSingleIPMSPassword_Type()
)
cmSingleIPMSPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSingleIPMSPassword.setStatus("current")
_CmSingleIPMSRowStatus_Type = RowStatus
_CmSingleIPMSRowStatus_Object = MibTableColumn
cmSingleIPMSRowStatus = _CmSingleIPMSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 3, 1, 10),
    _CmSingleIPMSRowStatus_Type()
)
cmSingleIPMSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSingleIPMSRowStatus.setStatus("current")
_CmSingleIPCaSTable_Object = MibTable
cmSingleIPCaSTable = _CmSingleIPCaSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4)
)
if mibBuilder.loadTexts:
    cmSingleIPCaSTable.setStatus("current")
_CmSingleIPCaSEntry_Object = MibTableRow
cmSingleIPCaSEntry = _CmSingleIPCaSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1)
)
cmSingleIPCaSEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "cmSingleIPCaSID"),
)
if mibBuilder.loadTexts:
    cmSingleIPCaSEntry.setStatus("current")


class _CmSingleIPCaSID_Type(Integer32):
    """Custom type cmSingleIPCaSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CmSingleIPCaSID_Type.__name__ = "Integer32"
_CmSingleIPCaSID_Object = MibTableColumn
cmSingleIPCaSID = _CmSingleIPCaSID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1, 1),
    _CmSingleIPCaSID_Type()
)
cmSingleIPCaSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCaSID.setStatus("current")


class _CmSingleIPCaSDeviceName_Type(DisplayString):
    """Custom type cmSingleIPCaSDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPCaSDeviceName_Type.__name__ = "DisplayString"
_CmSingleIPCaSDeviceName_Object = MibTableColumn
cmSingleIPCaSDeviceName = _CmSingleIPCaSDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1, 2),
    _CmSingleIPCaSDeviceName_Type()
)
cmSingleIPCaSDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCaSDeviceName.setStatus("current")
_CmSingleIPCaSMacAddr_Type = MacAddress
_CmSingleIPCaSMacAddr_Object = MibTableColumn
cmSingleIPCaSMacAddr = _CmSingleIPCaSMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1, 3),
    _CmSingleIPCaSMacAddr_Type()
)
cmSingleIPCaSMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCaSMacAddr.setStatus("current")


class _CmSingleIPCaSFirmwareVer_Type(DisplayString):
    """Custom type cmSingleIPCaSFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPCaSFirmwareVer_Type.__name__ = "DisplayString"
_CmSingleIPCaSFirmwareVer_Object = MibTableColumn
cmSingleIPCaSFirmwareVer = _CmSingleIPCaSFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1, 4),
    _CmSingleIPCaSFirmwareVer_Type()
)
cmSingleIPCaSFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCaSFirmwareVer.setStatus("current")


class _CmSingleIPCaSCapability_Type(DisplayString):
    """Custom type cmSingleIPCaSCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPCaSCapability_Type.__name__ = "DisplayString"
_CmSingleIPCaSCapability_Object = MibTableColumn
cmSingleIPCaSCapability = _CmSingleIPCaSCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1, 5),
    _CmSingleIPCaSCapability_Type()
)
cmSingleIPCaSCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCaSCapability.setStatus("current")


class _CmSingleIPCaSPlatform_Type(DisplayString):
    """Custom type cmSingleIPCaSPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPCaSPlatform_Type.__name__ = "DisplayString"
_CmSingleIPCaSPlatform_Object = MibTableColumn
cmSingleIPCaSPlatform = _CmSingleIPCaSPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1, 6),
    _CmSingleIPCaSPlatform_Type()
)
cmSingleIPCaSPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCaSPlatform.setStatus("current")
_CmSingleIPCaSHoldtime_Type = Integer32
_CmSingleIPCaSHoldtime_Object = MibTableColumn
cmSingleIPCaSHoldtime = _CmSingleIPCaSHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 4, 1, 7),
    _CmSingleIPCaSHoldtime_Type()
)
cmSingleIPCaSHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPCaSHoldtime.setStatus("current")
_CmSingleIPGroupTable_Object = MibTable
cmSingleIPGroupTable = _CmSingleIPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5)
)
if mibBuilder.loadTexts:
    cmSingleIPGroupTable.setStatus("current")
_CmSingleIPGroupEntry_Object = MibTableRow
cmSingleIPGroupEntry = _CmSingleIPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1)
)
cmSingleIPGroupEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "cmSingleIPGroupMacAddr"),
)
if mibBuilder.loadTexts:
    cmSingleIPGroupEntry.setStatus("current")
_CmSingleIPGroupMacAddr_Type = MacAddress
_CmSingleIPGroupMacAddr_Object = MibTableColumn
cmSingleIPGroupMacAddr = _CmSingleIPGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 1),
    _CmSingleIPGroupMacAddr_Type()
)
cmSingleIPGroupMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupMacAddr.setStatus("current")


class _CmSingleIPGroupName_Type(DisplayString):
    """Custom type cmSingleIPGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPGroupName_Type.__name__ = "DisplayString"
_CmSingleIPGroupName_Object = MibTableColumn
cmSingleIPGroupName = _CmSingleIPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 2),
    _CmSingleIPGroupName_Type()
)
cmSingleIPGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupName.setStatus("current")


class _CmSingleIPGroupDeviceName_Type(DisplayString):
    """Custom type cmSingleIPGroupDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPGroupDeviceName_Type.__name__ = "DisplayString"
_CmSingleIPGroupDeviceName_Object = MibTableColumn
cmSingleIPGroupDeviceName = _CmSingleIPGroupDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 3),
    _CmSingleIPGroupDeviceName_Type()
)
cmSingleIPGroupDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupDeviceName.setStatus("current")
_CmSingleIPGroupMSNumber_Type = Integer32
_CmSingleIPGroupMSNumber_Object = MibTableColumn
cmSingleIPGroupMSNumber = _CmSingleIPGroupMSNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 4),
    _CmSingleIPGroupMSNumber_Type()
)
cmSingleIPGroupMSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupMSNumber.setStatus("current")


class _CmSingleIPGroupFirmwareVer_Type(DisplayString):
    """Custom type cmSingleIPGroupFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPGroupFirmwareVer_Type.__name__ = "DisplayString"
_CmSingleIPGroupFirmwareVer_Object = MibTableColumn
cmSingleIPGroupFirmwareVer = _CmSingleIPGroupFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 5),
    _CmSingleIPGroupFirmwareVer_Type()
)
cmSingleIPGroupFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupFirmwareVer.setStatus("current")


class _CmSingleIPGroupCapability_Type(DisplayString):
    """Custom type cmSingleIPGroupCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPGroupCapability_Type.__name__ = "DisplayString"
_CmSingleIPGroupCapability_Object = MibTableColumn
cmSingleIPGroupCapability = _CmSingleIPGroupCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 6),
    _CmSingleIPGroupCapability_Type()
)
cmSingleIPGroupCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupCapability.setStatus("current")


class _CmSingleIPGroupPlatform_Type(DisplayString):
    """Custom type cmSingleIPGroupPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmSingleIPGroupPlatform_Type.__name__ = "DisplayString"
_CmSingleIPGroupPlatform_Object = MibTableColumn
cmSingleIPGroupPlatform = _CmSingleIPGroupPlatform_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 7),
    _CmSingleIPGroupPlatform_Type()
)
cmSingleIPGroupPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupPlatform.setStatus("current")
_CmSingleIPGroupHoldtime_Type = Integer32
_CmSingleIPGroupHoldtime_Object = MibTableColumn
cmSingleIPGroupHoldtime = _CmSingleIPGroupHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 5, 1, 8),
    _CmSingleIPGroupHoldtime_Type()
)
cmSingleIPGroupHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPGroupHoldtime.setStatus("current")
_CmSingleIPNeighborTable_Object = MibTable
cmSingleIPNeighborTable = _CmSingleIPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 6)
)
if mibBuilder.loadTexts:
    cmSingleIPNeighborTable.setStatus("current")
_CmSingleIPNeighborEntry_Object = MibTableRow
cmSingleIPNeighborEntry = _CmSingleIPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 6, 1)
)
cmSingleIPNeighborEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "cmSingleIPNBReceivedPort"),
    (0, "DGS-1500-52_AX", "cmSingleIPNBMacAddr"),
)
if mibBuilder.loadTexts:
    cmSingleIPNeighborEntry.setStatus("current")
_CmSingleIPNBReceivedPort_Type = Integer32
_CmSingleIPNBReceivedPort_Object = MibTableColumn
cmSingleIPNBReceivedPort = _CmSingleIPNBReceivedPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 6, 1, 1),
    _CmSingleIPNBReceivedPort_Type()
)
cmSingleIPNBReceivedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPNBReceivedPort.setStatus("current")
_CmSingleIPNBMacAddr_Type = MacAddress
_CmSingleIPNBMacAddr_Object = MibTableColumn
cmSingleIPNBMacAddr = _CmSingleIPNBMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 6, 1, 2),
    _CmSingleIPNBMacAddr_Type()
)
cmSingleIPNBMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPNBMacAddr.setStatus("current")


class _CmSingleIPNBRoleState_Type(Integer32):
    """Custom type cmSingleIPNBRoleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("candidate", 2),
          ("commander", 1),
          ("member", 3))
    )


_CmSingleIPNBRoleState_Type.__name__ = "Integer32"
_CmSingleIPNBRoleState_Object = MibTableColumn
cmSingleIPNBRoleState = _CmSingleIPNBRoleState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 1, 6, 1, 3),
    _CmSingleIPNBRoleState_Type()
)
cmSingleIPNBRoleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPNBRoleState.setStatus("current")
_SingleIPMSNotify_ObjectIdentity = ObjectIdentity
singleIPMSNotify = _SingleIPMSNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6)
)
_SingleIPMSNotifyPrefix_ObjectIdentity = ObjectIdentity
singleIPMSNotifyPrefix = _SingleIPMSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0)
)
_SingleIPNotifyBidings_ObjectIdentity = ObjectIdentity
singleIPNotifyBidings = _SingleIPNotifyBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 1)
)


class _CmSingleIPMSTrapMessage_Type(OctetString):
    """Custom type cmSingleIPMSTrapMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CmSingleIPMSTrapMessage_Type.__name__ = "OctetString"
_CmSingleIPMSTrapMessage_Object = MibScalar
cmSingleIPMSTrapMessage = _CmSingleIPMSTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 1, 1),
    _CmSingleIPMSTrapMessage_Type()
)
cmSingleIPMSTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSingleIPMSTrapMessage.setStatus("current")
_CompanyGVRPGroup_ObjectIdentity = ObjectIdentity
companyGVRPGroup = _CompanyGVRPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30)
)


class _GvrpGVRPGlobalSettingsOnOff_Type(Integer32):
    """Custom type gvrpGVRPGlobalSettingsOnOff based on Integer32"""
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


_GvrpGVRPGlobalSettingsOnOff_Type.__name__ = "Integer32"
_GvrpGVRPGlobalSettingsOnOff_Object = MibScalar
gvrpGVRPGlobalSettingsOnOff = _GvrpGVRPGlobalSettingsOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 1),
    _GvrpGVRPGlobalSettingsOnOff_Type()
)
gvrpGVRPGlobalSettingsOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpGVRPGlobalSettingsOnOff.setStatus("current")


class _GvrpSettingsJoinTime_Type(Integer32):
    """Custom type gvrpSettingsJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_GvrpSettingsJoinTime_Type.__name__ = "Integer32"
_GvrpSettingsJoinTime_Object = MibScalar
gvrpSettingsJoinTime = _GvrpSettingsJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 2),
    _GvrpSettingsJoinTime_Type()
)
gvrpSettingsJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsJoinTime.setStatus("current")


class _GvrpSettingsLeaveTime_Type(Integer32):
    """Custom type gvrpSettingsLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_GvrpSettingsLeaveTime_Type.__name__ = "Integer32"
_GvrpSettingsLeaveTime_Object = MibScalar
gvrpSettingsLeaveTime = _GvrpSettingsLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 3),
    _GvrpSettingsLeaveTime_Type()
)
gvrpSettingsLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsLeaveTime.setStatus("current")


class _GvrpSettingsLeaveAllTime_Type(Integer32):
    """Custom type gvrpSettingsLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_GvrpSettingsLeaveAllTime_Type.__name__ = "Integer32"
_GvrpSettingsLeaveAllTime_Object = MibScalar
gvrpSettingsLeaveAllTime = _GvrpSettingsLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 4),
    _GvrpSettingsLeaveAllTime_Type()
)
gvrpSettingsLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsLeaveAllTime.setStatus("current")
_GvrpSettingsTable_Object = MibTable
gvrpSettingsTable = _GvrpSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 5)
)
if mibBuilder.loadTexts:
    gvrpSettingsTable.setStatus("current")
_GvrpSettingsEntry_Object = MibTableRow
gvrpSettingsEntry = _GvrpSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 5, 1)
)
gvrpSettingsEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "gvrpSettingsPortControlIndex"),
)
if mibBuilder.loadTexts:
    gvrpSettingsEntry.setStatus("current")
_GvrpSettingsPortControlIndex_Type = InterfaceIndex
_GvrpSettingsPortControlIndex_Object = MibTableColumn
gvrpSettingsPortControlIndex = _GvrpSettingsPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 5, 1, 1),
    _GvrpSettingsPortControlIndex_Type()
)
gvrpSettingsPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gvrpSettingsPortControlIndex.setStatus("current")


class _GvrpSettingsPVID_Type(Integer32):
    """Custom type gvrpSettingsPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_GvrpSettingsPVID_Type.__name__ = "Integer32"
_GvrpSettingsPVID_Object = MibTableColumn
gvrpSettingsPVID = _GvrpSettingsPVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 5, 1, 2),
    _GvrpSettingsPVID_Type()
)
gvrpSettingsPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsPVID.setStatus("current")


class _GvrpSettingsGVRPState_Type(Integer32):
    """Custom type gvrpSettingsGVRPState based on Integer32"""
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


_GvrpSettingsGVRPState_Type.__name__ = "Integer32"
_GvrpSettingsGVRPState_Object = MibTableColumn
gvrpSettingsGVRPState = _GvrpSettingsGVRPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 5, 1, 3),
    _GvrpSettingsGVRPState_Type()
)
gvrpSettingsGVRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsGVRPState.setStatus("current")


class _GvrpSettingsIngressChecking_Type(Integer32):
    """Custom type gvrpSettingsIngressChecking based on Integer32"""
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


_GvrpSettingsIngressChecking_Type.__name__ = "Integer32"
_GvrpSettingsIngressChecking_Object = MibTableColumn
gvrpSettingsIngressChecking = _GvrpSettingsIngressChecking_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 5, 1, 4),
    _GvrpSettingsIngressChecking_Type()
)
gvrpSettingsIngressChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsIngressChecking.setStatus("current")


class _GvrpSettingsAcceptableFrameType_Type(Integer32):
    """Custom type gvrpSettingsAcceptableFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allFrames", 1),
          ("taggedOnly", 2))
    )


_GvrpSettingsAcceptableFrameType_Type.__name__ = "Integer32"
_GvrpSettingsAcceptableFrameType_Object = MibTableColumn
gvrpSettingsAcceptableFrameType = _GvrpSettingsAcceptableFrameType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 30, 5, 1, 5),
    _GvrpSettingsAcceptableFrameType_Type()
)
gvrpSettingsAcceptableFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gvrpSettingsAcceptableFrameType.setStatus("current")
_CompanyGreenSetting_ObjectIdentity = ObjectIdentity
companyGreenSetting = _CompanyGreenSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31)
)
_DlinkGreenLEDShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenLEDShutoff = _DlinkGreenLEDShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 1)
)
_DlinkGreenLEDShutoffPortList_Type = PortList
_DlinkGreenLEDShutoffPortList_Object = MibScalar
dlinkGreenLEDShutoffPortList = _DlinkGreenLEDShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 1, 1),
    _DlinkGreenLEDShutoffPortList_Type()
)
dlinkGreenLEDShutoffPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffPortList.setStatus("current")


class _DlinkGreenLEDShutoffState_Type(Integer32):
    """Custom type dlinkGreenLEDShutoffState based on Integer32"""
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


_DlinkGreenLEDShutoffState_Type.__name__ = "Integer32"
_DlinkGreenLEDShutoffState_Object = MibScalar
dlinkGreenLEDShutoffState = _DlinkGreenLEDShutoffState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 1, 4),
    _DlinkGreenLEDShutoffTimeProfile2_Type()
)
dlinkGreenLEDShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffTimeProfile2.setStatus("current")
_DlinkGreenPortShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenPortShutoff = _DlinkGreenPortShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 2)
)
_DlinkGreenPortShutoffPortList_Type = PortList
_DlinkGreenPortShutoffPortList_Object = MibScalar
dlinkGreenPortShutoffPortList = _DlinkGreenPortShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 2, 1),
    _DlinkGreenPortShutoffPortList_Type()
)
dlinkGreenPortShutoffPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffPortList.setStatus("current")


class _DlinkGreenPortShutoffState_Type(Integer32):
    """Custom type dlinkGreenPortShutoffState based on Integer32"""
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


_DlinkGreenPortShutoffState_Type.__name__ = "Integer32"
_DlinkGreenPortShutoffState_Object = MibScalar
dlinkGreenPortShutoffState = _DlinkGreenPortShutoffState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 2, 4),
    _DlinkGreenPortShutoffTimeProfile2_Type()
)
dlinkGreenPortShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffTimeProfile2.setStatus("current")
_DlinkGreenPortStandby_ObjectIdentity = ObjectIdentity
dlinkGreenPortStandby = _DlinkGreenPortStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 3)
)
_DlinkGreenPortStandbyPortList_Type = PortList
_DlinkGreenPortStandbyPortList_Object = MibScalar
dlinkGreenPortStandbyPortList = _DlinkGreenPortStandbyPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 3, 1),
    _DlinkGreenPortStandbyPortList_Type()
)
dlinkGreenPortStandbyPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortStandbyPortList.setStatus("current")


class _DlinkGreenPortStandbyState_Type(Integer32):
    """Custom type dlinkGreenPortStandbyState based on Integer32"""
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


_DlinkGreenPortStandbyState_Type.__name__ = "Integer32"
_DlinkGreenPortStandbyState_Object = MibScalar
dlinkGreenPortStandbyState = _DlinkGreenPortStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 3, 4),
    _DlinkGreenPortStandbyTimeProfile2_Type()
)
dlinkGreenPortStandbyTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortStandbyTimeProfile2.setStatus("current")
_DlinkGreenSystemHibernation_ObjectIdentity = ObjectIdentity
dlinkGreenSystemHibernation = _DlinkGreenSystemHibernation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 4)
)


class _DlinkGreenSystemHibernationState_Type(Integer32):
    """Custom type dlinkGreenSystemHibernationState based on Integer32"""
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


_DlinkGreenSystemHibernationState_Type.__name__ = "Integer32"
_DlinkGreenSystemHibernationState_Object = MibScalar
dlinkGreenSystemHibernationState = _DlinkGreenSystemHibernationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 31, 6),
    _DlinkPowerSavLinkStatusDetectState_Type()
)
dlinkPowerSavLinkStatusDetectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkPowerSavLinkStatusDetectState.setStatus("current")
_CompanyTimeRangeMgmt_ObjectIdentity = ObjectIdentity
companyTimeRangeMgmt = _CompanyTimeRangeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32)
)
_SwTimeRangeSettingTable_Object = MibTable
swTimeRangeSettingTable = _SwTimeRangeSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1)
)
if mibBuilder.loadTexts:
    swTimeRangeSettingTable.setStatus("current")
_SwTimeRangeSettingEntry_Object = MibTableRow
swTimeRangeSettingEntry = _SwTimeRangeSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1)
)
swTimeRangeSettingEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "swTimeRangeIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 20),
    _SwTimeRangeSunday_Type()
)
swTimeRangeSunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeSunday.setStatus("current")
_SwTimeRangeRowStatus_Type = RowStatus
_SwTimeRangeRowStatus_Object = MibTableColumn
swTimeRangeRowStatus = _SwTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 32, 1, 1, 21),
    _SwTimeRangeRowStatus_Type()
)
swTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeRowStatus.setStatus("current")
_CompanyGratuitousARP_ObjectIdentity = ObjectIdentity
companyGratuitousARP = _CompanyGratuitousARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33)
)
_SysGratuitousARPGlobalSettings_ObjectIdentity = ObjectIdentity
sysGratuitousARPGlobalSettings = _SysGratuitousARPGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 1)
)


class _SysGratuitousARPIPIfStatusUp_Type(Integer32):
    """Custom type sysGratuitousARPIPIfStatusUp based on Integer32"""
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


_SysGratuitousARPIPIfStatusUp_Type.__name__ = "Integer32"
_SysGratuitousARPIPIfStatusUp_Object = MibScalar
sysGratuitousARPIPIfStatusUp = _SysGratuitousARPIPIfStatusUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 1, 1),
    _SysGratuitousARPIPIfStatusUp_Type()
)
sysGratuitousARPIPIfStatusUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGratuitousARPIPIfStatusUp.setStatus("current")


class _SysGratuitousARPDuplicateIPDetected_Type(Integer32):
    """Custom type sysGratuitousARPDuplicateIPDetected based on Integer32"""
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


_SysGratuitousARPDuplicateIPDetected_Type.__name__ = "Integer32"
_SysGratuitousARPDuplicateIPDetected_Object = MibScalar
sysGratuitousARPDuplicateIPDetected = _SysGratuitousARPDuplicateIPDetected_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 1, 2),
    _SysGratuitousARPDuplicateIPDetected_Type()
)
sysGratuitousARPDuplicateIPDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGratuitousARPDuplicateIPDetected.setStatus("current")


class _SysGratuitousARPLearning_Type(Integer32):
    """Custom type sysGratuitousARPLearning based on Integer32"""
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


_SysGratuitousARPLearning_Type.__name__ = "Integer32"
_SysGratuitousARPLearning_Object = MibScalar
sysGratuitousARPLearning = _SysGratuitousARPLearning_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 1, 3),
    _SysGratuitousARPLearning_Type()
)
sysGratuitousARPLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGratuitousARPLearning.setStatus("current")
_SysGratuitousARPSettings_ObjectIdentity = ObjectIdentity
sysGratuitousARPSettings = _SysGratuitousARPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 2)
)
_SysGratuitousARPTable_Object = MibTable
sysGratuitousARPTable = _SysGratuitousARPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 2, 1)
)
if mibBuilder.loadTexts:
    sysGratuitousARPTable.setStatus("current")
_SysGratuitousARPEntry_Object = MibTableRow
sysGratuitousARPEntry = _SysGratuitousARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 2, 1, 1)
)
sysGratuitousARPEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "sysGratuitousARPIFName"),
)
if mibBuilder.loadTexts:
    sysGratuitousARPEntry.setStatus("current")
_SysGratuitousARPIFName_Type = OctetString
_SysGratuitousARPIFName_Object = MibTableColumn
sysGratuitousARPIFName = _SysGratuitousARPIFName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 2, 1, 1, 1),
    _SysGratuitousARPIFName_Type()
)
sysGratuitousARPIFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGratuitousARPIFName.setStatus("current")


class _SysGratuitousARPInterval_Type(Integer32):
    """Custom type sysGratuitousARPInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysGratuitousARPInterval_Type.__name__ = "Integer32"
_SysGratuitousARPInterval_Object = MibTableColumn
sysGratuitousARPInterval = _SysGratuitousARPInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 33, 2, 1, 1, 2),
    _SysGratuitousARPInterval_Type()
)
sysGratuitousARPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGratuitousARPInterval.setStatus("current")
_CompanyStaticARP_ObjectIdentity = ObjectIdentity
companyStaticARP = _CompanyStaticARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34)
)


class _SysARPAgingTime_Type(Integer32):
    """Custom type sysARPAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysARPAgingTime_Type.__name__ = "Integer32"
_SysARPAgingTime_Object = MibScalar
sysARPAgingTime = _SysARPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 1),
    _SysARPAgingTime_Type()
)
sysARPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysARPAgingTime.setStatus("current")
_StaticARPTable_Object = MibTable
staticARPTable = _StaticARPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 2)
)
if mibBuilder.loadTexts:
    staticARPTable.setStatus("current")
_StaticARPEntry_Object = MibTableRow
staticARPEntry = _StaticARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 2, 1)
)
staticARPEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "staticARPIP"),
    (0, "DGS-1500-52_AX", "staticARPMac"),
)
if mibBuilder.loadTexts:
    staticARPEntry.setStatus("current")
_StaticARPIPInterface_Type = OctetString
_StaticARPIPInterface_Object = MibTableColumn
staticARPIPInterface = _StaticARPIPInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 2, 1, 1),
    _StaticARPIPInterface_Type()
)
staticARPIPInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticARPIPInterface.setStatus("current")
_StaticARPIP_Type = IpAddress
_StaticARPIP_Object = MibTableColumn
staticARPIP = _StaticARPIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 2, 1, 2),
    _StaticARPIP_Type()
)
staticARPIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticARPIP.setStatus("current")
_StaticARPMac_Type = MacAddress
_StaticARPMac_Object = MibTableColumn
staticARPMac = _StaticARPMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 2, 1, 3),
    _StaticARPMac_Type()
)
staticARPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticARPMac.setStatus("current")


class _StaticARPType_Type(Integer32):
    """Custom type staticARPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("local", 0),
          ("static", 2))
    )


_StaticARPType_Type.__name__ = "Integer32"
_StaticARPType_Object = MibTableColumn
staticARPType = _StaticARPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 2, 1, 4),
    _StaticARPType_Type()
)
staticARPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticARPType.setStatus("current")
_StaticARPRowStatus_Type = RowStatus
_StaticARPRowStatus_Object = MibTableColumn
staticARPRowStatus = _StaticARPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 34, 2, 1, 5),
    _StaticARPRowStatus_Type()
)
staticARPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticARPRowStatus.setStatus("current")
_CompanyStaticMcast_ObjectIdentity = ObjectIdentity
companyStaticMcast = _CompanyStaticMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 35)
)
_StaticMcastTable_Object = MibTable
staticMcastTable = _StaticMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 35, 1)
)
if mibBuilder.loadTexts:
    staticMcastTable.setStatus("current")
_StaticMcastEntry_Object = MibTableRow
staticMcastEntry = _StaticMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 35, 1, 1)
)
staticMcastEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "staticMcastVlanID"),
    (0, "DGS-1500-52_AX", "staticMcastMac"),
    (0, "DGS-1500-52_AX", "staticMcastEgressPorts"),
)
if mibBuilder.loadTexts:
    staticMcastEntry.setStatus("current")
_StaticMcastVlanID_Type = Integer32
_StaticMcastVlanID_Object = MibTableColumn
staticMcastVlanID = _StaticMcastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 35, 1, 1, 1),
    _StaticMcastVlanID_Type()
)
staticMcastVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastVlanID.setStatus("current")
_StaticMcastMac_Type = MacAddress
_StaticMcastMac_Object = MibTableColumn
staticMcastMac = _StaticMcastMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 35, 1, 1, 2),
    _StaticMcastMac_Type()
)
staticMcastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastMac.setStatus("current")
_StaticMcastEgressPorts_Type = PortList
_StaticMcastEgressPorts_Object = MibTableColumn
staticMcastEgressPorts = _StaticMcastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 35, 1, 1, 3),
    _StaticMcastEgressPorts_Type()
)
staticMcastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastEgressPorts.setStatus("current")
_StaticMcastStatus_Type = RowStatus
_StaticMcastStatus_Object = MibTableColumn
staticMcastStatus = _StaticMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 35, 1, 1, 4),
    _StaticMcastStatus_Type()
)
staticMcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMcastStatus.setStatus("current")
_CompanyStaticRoute_ObjectIdentity = ObjectIdentity
companyStaticRoute = _CompanyStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36)
)
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1)
)
staticRouteEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "staticRouteIpAddr"),
    (0, "DGS-1500-52_AX", "staticRouteNetmask"),
    (0, "DGS-1500-52_AX", "staticRouteGateway"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")
_StaticRouteInterfaceID_Type = Integer32
_StaticRouteInterfaceID_Object = MibTableColumn
staticRouteInterfaceID = _StaticRouteInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 1),
    _StaticRouteInterfaceID_Type()
)
staticRouteInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteInterfaceID.setStatus("current")
_StaticRouteIpAddr_Type = IpAddress
_StaticRouteIpAddr_Object = MibTableColumn
staticRouteIpAddr = _StaticRouteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 2),
    _StaticRouteIpAddr_Type()
)
staticRouteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteIpAddr.setStatus("current")
_StaticRouteNetmask_Type = IpAddress
_StaticRouteNetmask_Object = MibTableColumn
staticRouteNetmask = _StaticRouteNetmask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 3),
    _StaticRouteNetmask_Type()
)
staticRouteNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteNetmask.setStatus("current")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("current")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("current")


class _StaticRouteProtocol_Type(Integer32):
    """Custom type staticRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("static", 1))
    )


_StaticRouteProtocol_Type.__name__ = "Integer32"
_StaticRouteProtocol_Object = MibTableColumn
staticRouteProtocol = _StaticRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 6),
    _StaticRouteProtocol_Type()
)
staticRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteProtocol.setStatus("current")


class _StaticRouteBackup_Type(Integer32):
    """Custom type staticRouteBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("primary", 0))
    )


_StaticRouteBackup_Type.__name__ = "Integer32"
_StaticRouteBackup_Object = MibTableColumn
staticRouteBackup = _StaticRouteBackup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 7),
    _StaticRouteBackup_Type()
)
staticRouteBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteBackup.setStatus("current")


class _StaticRouteActiveStatus_Type(Integer32):
    """Custom type staticRouteActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_StaticRouteActiveStatus_Type.__name__ = "Integer32"
_StaticRouteActiveStatus_Object = MibTableColumn
staticRouteActiveStatus = _StaticRouteActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 8),
    _StaticRouteActiveStatus_Type()
)
staticRouteActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteActiveStatus.setStatus("current")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 36, 1, 1, 9),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("current")
_CompanyMultiIPInterface_ObjectIdentity = ObjectIdentity
companyMultiIPInterface = _CompanyMultiIPInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41)
)
_MultiIFInfo_ObjectIdentity = ObjectIdentity
multiIFInfo = _MultiIFInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1)
)
_MulifMainTable_Object = MibTable
mulifMainTable = _MulifMainTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1)
)
if mibBuilder.loadTexts:
    mulifMainTable.setStatus("current")
_MulIfMainEntry_Object = MibTableRow
mulIfMainEntry = _MulIfMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1)
)
mulIfMainEntry.setIndexNames(
    (0, "DGS-1500-52_AX", "mulifMainIndex"),
    (0, "DGS-1500-52_AX", "mulifVLANID"),
)
if mibBuilder.loadTexts:
    mulIfMainEntry.setStatus("current")
_MulifMainIndex_Type = InterfaceIndex
_MulifMainIndex_Object = MibTableColumn
mulifMainIndex = _MulifMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 1),
    _MulifMainIndex_Type()
)
mulifMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulifMainIndex.setStatus("current")
_MulifVLANID_Type = Integer32
_MulifVLANID_Object = MibTableColumn
mulifVLANID = _MulifVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 2),
    _MulifVLANID_Type()
)
mulifVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulifVLANID.setStatus("current")
_MulifName_Type = OctetString
_MulifName_Object = MibTableColumn
mulifName = _MulifName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 3),
    _MulifName_Type()
)
mulifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mulifName.setStatus("current")
_MulifVLANname_Type = OctetString
_MulifVLANname_Object = MibTableColumn
mulifVLANname = _MulifVLANname_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 4),
    _MulifVLANname_Type()
)
mulifVLANname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulifVLANname.setStatus("current")


class _MulifIpAddr_Type(IpAddress):
    """Custom type mulifIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_MulifIpAddr_Object = MibTableColumn
mulifIpAddr = _MulifIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 6),
    _MulifIpAddr_Type()
)
mulifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mulifIpAddr.setStatus("current")
_MulifIpSubnetMask_Type = IpAddress
_MulifIpSubnetMask_Object = MibTableColumn
mulifIpSubnetMask = _MulifIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 7),
    _MulifIpSubnetMask_Type()
)
mulifIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mulifIpSubnetMask.setStatus("current")


class _MulifMainAdminStatus_Type(Integer32):
    """Custom type mulifMainAdminStatus based on Integer32"""
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


_MulifMainAdminStatus_Type.__name__ = "Integer32"
_MulifMainAdminStatus_Object = MibTableColumn
mulifMainAdminStatus = _MulifMainAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 8),
    _MulifMainAdminStatus_Type()
)
mulifMainAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mulifMainAdminStatus.setStatus("current")


class _MulifMainOperStatus_Type(Integer32):
    """Custom type mulifMainOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 2),
          ("linkup", 1))
    )


_MulifMainOperStatus_Type.__name__ = "Integer32"
_MulifMainOperStatus_Object = MibTableColumn
mulifMainOperStatus = _MulifMainOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 9),
    _MulifMainOperStatus_Type()
)
mulifMainOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulifMainOperStatus.setStatus("current")
_MulifMainRowStatus_Type = RowStatus
_MulifMainRowStatus_Object = MibTableColumn
mulifMainRowStatus = _MulifMainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 41, 1, 1, 1, 10),
    _MulifMainRowStatus_Type()
)
mulifMainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mulifMainRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0, 4)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )

firmwareUpgradeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0, 8)
)
if mibBuilder.loadTexts:
    firmwareUpgradeSuccess.setStatus(
        "current"
    )

firmwareUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0, 9)
)
if mibBuilder.loadTexts:
    firmwareUpgradeFailure.setStatus(
        "current"
    )

firmwareIllegalFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0, 10)
)
if mibBuilder.loadTexts:
    firmwareIllegalFile.setStatus(
        "current"
    )

firmwareTransferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0, 11)
)
if mibBuilder.loadTexts:
    firmwareTransferError.setStatus(
        "current"
    )

firmwareChecksumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0, 12)
)
if mibBuilder.loadTexts:
    firmwareChecksumError.setStatus(
        "current"
    )

gratuitousARPDuplicatedIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 27, 0, 20)
)
if mibBuilder.loadTexts:
    gratuitousARPDuplicatedIP.setStatus(
        "current"
    )

cmSingleIPMSColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 11)
)
cmSingleIPMSColdStart.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSColdStart.setStatus(
        "current"
    )

cmSingleIPMSWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 12)
)
cmSingleIPMSWarmStart.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSWarmStart.setStatus(
        "current"
    )

cmSingleIPMSLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 13)
)
cmSingleIPMSLinkDown.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSLinkDown.setStatus(
        "current"
    )

cmSingleIPMSLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 14)
)
cmSingleIPMSLinkUp.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSLinkUp.setStatus(
        "current"
    )

cmSingleIPMSAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 15)
)
cmSingleIPMSAuthFail.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSAuthFail.setStatus(
        "current"
    )

cmSingleIPMSnewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 16)
)
cmSingleIPMSnewRoot.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSnewRoot.setStatus(
        "current"
    )

cmSingleIPMSTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 17)
)
cmSingleIPMSTopologyChange.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSTopologyChange.setStatus(
        "current"
    )

cmSingleIPMSrisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 18)
)
cmSingleIPMSrisingAlarm.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSrisingAlarm.setStatus(
        "current"
    )

cmSingleIPMSfallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 19)
)
cmSingleIPMSfallingAlarm.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSfallingAlarm.setStatus(
        "current"
    )

cmSingleIPMSmacNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 20)
)
cmSingleIPMSmacNotification.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"),
        ("DGS-1500-52_AX", "cmSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSmacNotification.setStatus(
        "current"
    )

cmSingleIPMSPortTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 21)
)
cmSingleIPMSPortTypeChange.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"),
        ("DGS-1500-52_AX", "cmSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSPortTypeChange.setStatus(
        "current"
    )

cmSingleIPMSPowerStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 22)
)
cmSingleIPMSPowerStatusChg.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"),
        ("DGS-1500-52_AX", "cmSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSPowerStatusChg.setStatus(
        "current"
    )

cmSingleIPMSPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 23)
)
cmSingleIPMSPowerFailure.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"),
        ("DGS-1500-52_AX", "cmSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSPowerFailure.setStatus(
        "current"
    )

cmSingleIPMSPowerRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 126, 4, 1, 29, 6, 0, 24)
)
cmSingleIPMSPowerRecover.setObjects(
      *(("DGS-1500-52_AX", "cmSingleIPMSID"),
        ("DGS-1500-52_AX", "cmSingleIPMSMacAddr"),
        ("DGS-1500-52_AX", "cmSingleIPMSTrapMessage"))
)
if mibBuilder.loadTexts:
    cmSingleIPMSPowerRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-1500-52_AX",
    **{"VlanIndex": VlanIndex,
       "PortList": PortList,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "LldpManAddress": LldpManAddress,
       "RmonStatus": RmonStatus,
       "PortLaMode": PortLaMode,
       "LacpKey": LacpKey,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DGS1500Series": dlink_DGS1500Series,
       "dgs-1500-52": dgs_1500_52,
       "dgs-1500-52ax": dgs_1500_52ax,
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
       "sysGPIOStatus": sysGPIOStatus,
       "sysFanStatus": sysFanStatus,
       "companyIpifGroup": companyIpifGroup,
       "sysIpInterfaceName": sysIpInterfaceName,
       "sysIpManagementVLANName": sysIpManagementVLANName,
       "sysIpInterfaceAdminStatus": sysIpInterfaceAdminStatus,
       "sysIpAddrCfgMode": sysIpAddrCfgMode,
       "sysIpAddr": sysIpAddr,
       "sysIpSubnetMask": sysIpSubnetMask,
       "sysGateway": sysGateway,
       "companyTftpGroup": companyTftpGroup,
       "tftpFwServerIpAddress": tftpFwServerIpAddress,
       "tftpFwImageFileName": tftpFwImageFileName,
       "tftpFwTftpOperation": tftpFwTftpOperation,
       "tftpFwTftpOperationStatus": tftpFwTftpOperationStatus,
       "tftpCfgServerIpAddress": tftpCfgServerIpAddress,
       "tftpConfigFileName": tftpConfigFileName,
       "tftpConfigTftpOperation": tftpConfigTftpOperation,
       "tftpConfigTftpOperationStatus": tftpConfigTftpOperationStatus,
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
       "dot1qVlanAsyOnOff": dot1qVlanAsyOnOff,
       "dot1qVlanTable": dot1qVlanTable,
       "dot1qVlanEntry": dot1qVlanEntry,
       "dot1qVlanName": dot1qVlanName,
       "dot1qVlanEgressPorts": dot1qVlanEgressPorts,
       "dot1qVlanForbiddenPorts": dot1qVlanForbiddenPorts,
       "dot1qVlanUntaggedPorts": dot1qVlanUntaggedPorts,
       "dot1qVlanAdvertisementStatus": dot1qVlanAdvertisementStatus,
       "dot1qVlanRowStatus": dot1qVlanRowStatus,
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
       "laPortActorPortPriority": laPortActorPortPriority,
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
       "trustedHostTable": trustedHostTable,
       "trustedHostEntry": trustedHostEntry,
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
       "dhcpServerScreenServerTable": dhcpServerScreenServerTable,
       "dhcpServerScreenServerEntry": dhcpServerScreenServerEntry,
       "dhcpServerScreenServerIndex": dhcpServerScreenServerIndex,
       "dhcpServerScreenServerAddress": dhcpServerScreenServerAddress,
       "dhcpServerScreenServerStatus": dhcpServerScreenServerStatus,
       "securityTrafficSeg": securityTrafficSeg,
       "trafficSegStatus": trafficSegStatus,
       "trafficSegTable": trafficSegTable,
       "trafficSegEntry": trafficSegEntry,
       "trafficSegIfIndex": trafficSegIfIndex,
       "trafficSegMemberList": trafficSegMemberList,
       "companyACLGroup": companyACLGroup,
       "aclProfile": aclProfile,
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileNo": aclProfileNo,
       "aclProfileType": aclProfileType,
       "aclProfileRuleCount": aclProfileRuleCount,
       "aclProfileMask": aclProfileMask,
       "aclProfileDstMacAddrMask": aclProfileDstMacAddrMask,
       "aclProfileSrcMacAddrMask": aclProfileSrcMacAddrMask,
       "aclProfileIPProtocol": aclProfileIPProtocol,
       "aclProfileDstIpAddrMask": aclProfileDstIpAddrMask,
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
       "companySyslog": companySyslog,
       "syslogGeneralGroup": syslogGeneralGroup,
       "syslogLogSrvAddr": syslogLogSrvAddr,
       "syslogUDPPort": syslogUDPPort,
       "syslogTimeStamp": syslogTimeStamp,
       "syslogSeverity": syslogSeverity,
       "syslogFacility": syslogFacility,
       "syslogLogging": syslogLogging,
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
       "sysTrapPortLinkUpDownEvent": sysTrapPortLinkUpDownEvent,
       "sysTrapStateChangeEvent": sysTrapStateChangeEvent,
       "sysTrapFirmUpgradeEvent": sysTrapFirmUpgradeEvent,
       "sysTrapGratuitousARP": sysTrapGratuitousARP,
       "sysTrapStatus": sysTrapStatus,
       "companySNTPSetting": companySNTPSetting,
       "sysSNTPTimeSeconds": sysSNTPTimeSeconds,
       "sysSNTPFirstServer": sysSNTPFirstServer,
       "sysSNTPSecondServer": sysSNTPSecondServer,
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
       "companyAuthGroup": companyAuthGroup,
       "swAuthenCtrl": swAuthenCtrl,
       "swAuthStatus": swAuthStatus,
       "authProtocol": authProtocol,
       "swAuthCtrlPktFwdMode": swAuthCtrlPktFwdMode,
       "swAuthPortAccessCtrl": swAuthPortAccessCtrl,
       "swAuthPortAccessControlTable": swAuthPortAccessControlTable,
       "swAuthPortAccessControlEntry": swAuthPortAccessControlEntry,
       "swAuthAuthConfigPortNumber": swAuthAuthConfigPortNumber,
       "swAuthAuthQuietPeriod": swAuthAuthQuietPeriod,
       "swAuthAuthSuppTimeout": swAuthAuthSuppTimeout,
       "swAuthAuthServerTimeout": swAuthAuthServerTimeout,
       "swAuthAuthMaxReq": swAuthAuthMaxReq,
       "swAuthAuthTxPeriod": swAuthAuthTxPeriod,
       "swAuthAuthReAuthPeriod": swAuthAuthReAuthPeriod,
       "swAuthAuthReAuthentication": swAuthAuthReAuthentication,
       "swAuthAuthConfigPortControl": swAuthAuthConfigPortControl,
       "swAuthAuthCapability": swAuthAuthCapability,
       "swAuthAuthDirection": swAuthAuthDirection,
       "swAuthUser": swAuthUser,
       "swAuthUserTable": swAuthUserTable,
       "swAuthUserEntry": swAuthUserEntry,
       "swAuthUserName": swAuthUserName,
       "swAuthUserPassword": swAuthUserPassword,
       "swAuthUserStatus": swAuthUserStatus,
       "swAuthRadiusServer": swAuthRadiusServer,
       "swAuthRadiusServerTable": swAuthRadiusServerTable,
       "swAuthRadiusServerEntry": swAuthRadiusServerEntry,
       "swAuthRadiusServerIndex": swAuthRadiusServerIndex,
       "swAuthRadiusServerAddress": swAuthRadiusServerAddress,
       "swAuthRadiusServerAuthenticationPort": swAuthRadiusServerAuthenticationPort,
       "swAuthRadiusServerAccountingPort": swAuthRadiusServerAccountingPort,
       "swAuthRadiusServerTimeout": swAuthRadiusServerTimeout,
       "swAuthRadiusServerRetransmit": swAuthRadiusServerRetransmit,
       "swAuthRadiusServerKey": swAuthRadiusServerKey,
       "swAuthRadiusServerStatus": swAuthRadiusServerStatus,
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
       "snmpV3HostTable": snmpV3HostTable,
       "snmpV3HostEntry": snmpV3HostEntry,
       "snmpV3HostAddress": snmpV3HostAddress,
       "snmpV3HostCommunityName": snmpV3HostCommunityName,
       "snmpV3HostVersion": snmpV3HostVersion,
       "snmpV3HostStatus": snmpV3HostStatus,
       "snmpV3EngineID": snmpV3EngineID,
       "snmpV3Trap": snmpV3Trap,
       "snmpV3TrapSNMPAuthentication": snmpV3TrapSNMPAuthentication,
       "snmpV3TrapBootup": snmpV3TrapBootup,
       "snmpV3TrapPortLinkUpDown": snmpV3TrapPortLinkUpDown,
       "snmpV3TrapRSTPStateChange": snmpV3TrapRSTPStateChange,
       "snmpV3TrapFirmUpgrade": snmpV3TrapFirmUpgrade,
       "snmpV3TrapGratuitousARP": snmpV3TrapGratuitousARP,
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
       "gratuitousARPDuplicatedIP": gratuitousARPDuplicatedIP,
       "companySIM": companySIM,
       "cmSingleIPMgmt": cmSingleIPMgmt,
       "cmSingleIPInfo": cmSingleIPInfo,
       "cmSingleIPVersion": cmSingleIPVersion,
       "cmSingleIPCapability": cmSingleIPCapability,
       "cmSingleIPPlatform": cmSingleIPPlatform,
       "cmSingleIPCtrl": cmSingleIPCtrl,
       "cmSingleIPAdmin": cmSingleIPAdmin,
       "cmSingleIPRoleState": cmSingleIPRoleState,
       "cmSingleIPHoldtime": cmSingleIPHoldtime,
       "cmSingleIPTimeInterval": cmSingleIPTimeInterval,
       "cmSingleIPMSTable": cmSingleIPMSTable,
       "cmSingleIPMSEntry": cmSingleIPMSEntry,
       "cmSingleIPMSID": cmSingleIPMSID,
       "cmSingleIPMSDeviceName": cmSingleIPMSDeviceName,
       "cmSingleIPMSMacAddr": cmSingleIPMSMacAddr,
       "cmSingleIPMSFirmwareVer": cmSingleIPMSFirmwareVer,
       "cmSingleIPMSCapability": cmSingleIPMSCapability,
       "cmSingleIPMSPlatform": cmSingleIPMSPlatform,
       "cmSingleIPMSHoldtime": cmSingleIPMSHoldtime,
       "cmSingleIPMSCasSource": cmSingleIPMSCasSource,
       "cmSingleIPMSPassword": cmSingleIPMSPassword,
       "cmSingleIPMSRowStatus": cmSingleIPMSRowStatus,
       "cmSingleIPCaSTable": cmSingleIPCaSTable,
       "cmSingleIPCaSEntry": cmSingleIPCaSEntry,
       "cmSingleIPCaSID": cmSingleIPCaSID,
       "cmSingleIPCaSDeviceName": cmSingleIPCaSDeviceName,
       "cmSingleIPCaSMacAddr": cmSingleIPCaSMacAddr,
       "cmSingleIPCaSFirmwareVer": cmSingleIPCaSFirmwareVer,
       "cmSingleIPCaSCapability": cmSingleIPCaSCapability,
       "cmSingleIPCaSPlatform": cmSingleIPCaSPlatform,
       "cmSingleIPCaSHoldtime": cmSingleIPCaSHoldtime,
       "cmSingleIPGroupTable": cmSingleIPGroupTable,
       "cmSingleIPGroupEntry": cmSingleIPGroupEntry,
       "cmSingleIPGroupMacAddr": cmSingleIPGroupMacAddr,
       "cmSingleIPGroupName": cmSingleIPGroupName,
       "cmSingleIPGroupDeviceName": cmSingleIPGroupDeviceName,
       "cmSingleIPGroupMSNumber": cmSingleIPGroupMSNumber,
       "cmSingleIPGroupFirmwareVer": cmSingleIPGroupFirmwareVer,
       "cmSingleIPGroupCapability": cmSingleIPGroupCapability,
       "cmSingleIPGroupPlatform": cmSingleIPGroupPlatform,
       "cmSingleIPGroupHoldtime": cmSingleIPGroupHoldtime,
       "cmSingleIPNeighborTable": cmSingleIPNeighborTable,
       "cmSingleIPNeighborEntry": cmSingleIPNeighborEntry,
       "cmSingleIPNBReceivedPort": cmSingleIPNBReceivedPort,
       "cmSingleIPNBMacAddr": cmSingleIPNBMacAddr,
       "cmSingleIPNBRoleState": cmSingleIPNBRoleState,
       "singleIPMSNotify": singleIPMSNotify,
       "singleIPMSNotifyPrefix": singleIPMSNotifyPrefix,
       "cmSingleIPMSColdStart": cmSingleIPMSColdStart,
       "cmSingleIPMSWarmStart": cmSingleIPMSWarmStart,
       "cmSingleIPMSLinkDown": cmSingleIPMSLinkDown,
       "cmSingleIPMSLinkUp": cmSingleIPMSLinkUp,
       "cmSingleIPMSAuthFail": cmSingleIPMSAuthFail,
       "cmSingleIPMSnewRoot": cmSingleIPMSnewRoot,
       "cmSingleIPMSTopologyChange": cmSingleIPMSTopologyChange,
       "cmSingleIPMSrisingAlarm": cmSingleIPMSrisingAlarm,
       "cmSingleIPMSfallingAlarm": cmSingleIPMSfallingAlarm,
       "cmSingleIPMSmacNotification": cmSingleIPMSmacNotification,
       "cmSingleIPMSPortTypeChange": cmSingleIPMSPortTypeChange,
       "cmSingleIPMSPowerStatusChg": cmSingleIPMSPowerStatusChg,
       "cmSingleIPMSPowerFailure": cmSingleIPMSPowerFailure,
       "cmSingleIPMSPowerRecover": cmSingleIPMSPowerRecover,
       "singleIPNotifyBidings": singleIPNotifyBidings,
       "cmSingleIPMSTrapMessage": cmSingleIPMSTrapMessage,
       "companyGVRPGroup": companyGVRPGroup,
       "gvrpGVRPGlobalSettingsOnOff": gvrpGVRPGlobalSettingsOnOff,
       "gvrpSettingsJoinTime": gvrpSettingsJoinTime,
       "gvrpSettingsLeaveTime": gvrpSettingsLeaveTime,
       "gvrpSettingsLeaveAllTime": gvrpSettingsLeaveAllTime,
       "gvrpSettingsTable": gvrpSettingsTable,
       "gvrpSettingsEntry": gvrpSettingsEntry,
       "gvrpSettingsPortControlIndex": gvrpSettingsPortControlIndex,
       "gvrpSettingsPVID": gvrpSettingsPVID,
       "gvrpSettingsGVRPState": gvrpSettingsGVRPState,
       "gvrpSettingsIngressChecking": gvrpSettingsIngressChecking,
       "gvrpSettingsAcceptableFrameType": gvrpSettingsAcceptableFrameType,
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
       "companyGratuitousARP": companyGratuitousARP,
       "sysGratuitousARPGlobalSettings": sysGratuitousARPGlobalSettings,
       "sysGratuitousARPIPIfStatusUp": sysGratuitousARPIPIfStatusUp,
       "sysGratuitousARPDuplicateIPDetected": sysGratuitousARPDuplicateIPDetected,
       "sysGratuitousARPLearning": sysGratuitousARPLearning,
       "sysGratuitousARPSettings": sysGratuitousARPSettings,
       "sysGratuitousARPTable": sysGratuitousARPTable,
       "sysGratuitousARPEntry": sysGratuitousARPEntry,
       "sysGratuitousARPIFName": sysGratuitousARPIFName,
       "sysGratuitousARPInterval": sysGratuitousARPInterval,
       "companyStaticARP": companyStaticARP,
       "sysARPAgingTime": sysARPAgingTime,
       "staticARPTable": staticARPTable,
       "staticARPEntry": staticARPEntry,
       "staticARPIPInterface": staticARPIPInterface,
       "staticARPIP": staticARPIP,
       "staticARPMac": staticARPMac,
       "staticARPType": staticARPType,
       "staticARPRowStatus": staticARPRowStatus,
       "companyStaticMcast": companyStaticMcast,
       "staticMcastTable": staticMcastTable,
       "staticMcastEntry": staticMcastEntry,
       "staticMcastVlanID": staticMcastVlanID,
       "staticMcastMac": staticMcastMac,
       "staticMcastEgressPorts": staticMcastEgressPorts,
       "staticMcastStatus": staticMcastStatus,
       "companyStaticRoute": companyStaticRoute,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteInterfaceID": staticRouteInterfaceID,
       "staticRouteIpAddr": staticRouteIpAddr,
       "staticRouteNetmask": staticRouteNetmask,
       "staticRouteGateway": staticRouteGateway,
       "staticRouteMetric": staticRouteMetric,
       "staticRouteProtocol": staticRouteProtocol,
       "staticRouteBackup": staticRouteBackup,
       "staticRouteActiveStatus": staticRouteActiveStatus,
       "staticRouteRowStatus": staticRouteRowStatus,
       "companyMultiIPInterface": companyMultiIPInterface,
       "multiIFInfo": multiIFInfo,
       "mulifMainTable": mulifMainTable,
       "mulIfMainEntry": mulIfMainEntry,
       "mulifMainIndex": mulifMainIndex,
       "mulifVLANID": mulifVLANID,
       "mulifName": mulifName,
       "mulifVLANname": mulifVLANname,
       "mulifIpAddr": mulifIpAddr,
       "mulifIpSubnetMask": mulifIpSubnetMask,
       "mulifMainAdminStatus": mulifMainAdminStatus,
       "mulifMainOperStatus": mulifMainOperStatus,
       "mulifMainRowStatus": mulifMainRowStatus}
)
