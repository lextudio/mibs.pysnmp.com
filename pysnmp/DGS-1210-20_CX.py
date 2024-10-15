# SNMP MIB module (DGS-1210-20_CX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-1210-20_CX
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:40 2024
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
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
_Dgs_1210_20_ObjectIdentity = ObjectIdentity
dgs_1210_20 = _Dgs_1210_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19)
)
_Dgs_1210_20cx_ObjectIdentity = ObjectIdentity
dgs_1210_20cx = _Dgs_1210_20cx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1)
)
_CompanySystem_ObjectIdentity = ObjectIdentity
companySystem = _CompanySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 5),
    _SysLocationName_Type()
)
sysLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationName.setStatus("current")


class _SysSystemPassword_Type(DisplayString):
    """Custom type sysSystemPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SysSystemPassword_Type.__name__ = "DisplayString"
_SysSystemPassword_Object = MibScalar
sysSystemPassword = _SysSystemPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 8),
    _SysSafeGuardEnable_Type()
)
sysSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSafeGuardEnable.setStatus("current")


class _SysRestart_Type(TruthValue):
    """Custom type sysRestart based on TruthValue"""


_SysRestart_Object = MibScalar
sysRestart = _SysRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 9),
    _SysRestart_Type()
)
sysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestart.setStatus("current")


class _SysSave_Type(TruthValue):
    """Custom type sysSave based on TruthValue"""


_SysSave_Object = MibScalar
sysSave = _SysSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 12),
    _SysJumboFrameEnable_Type()
)
sysJumboFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysJumboFrameEnable.setStatus("current")
_SysPortCtrlTable_Object = MibTable
sysPortCtrlTable = _SysPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13)
)
if mibBuilder.loadTexts:
    sysPortCtrlTable.setStatus("current")
_SysPortCtrlEntry_Object = MibTableRow
sysPortCtrlEntry = _SysPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1)
)
sysPortCtrlEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "sysPortCtrlIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1, 1),
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
          ("rate1000MFull", 1),
          ("rate100MFull", 2),
          ("rate100MHalf", 3),
          ("rate10MFull", 4),
          ("rate10MHalf", 5))
    )


_SysPortCtrlSpeed_Type.__name__ = "Integer32"
_SysPortCtrlSpeed_Object = MibTableColumn
sysPortCtrlSpeed = _SysPortCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1, 2),
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
          ("rate1000MFull", 2),
          ("rate100MFull", 3),
          ("rate100MHalf", 4),
          ("rate10MFull", 5),
          ("rate10MHalf", 6))
    )


_SysPortCtrlOperStatus_Type.__name__ = "Integer32"
_SysPortCtrlOperStatus_Object = MibTableColumn
sysPortCtrlOperStatus = _SysPortCtrlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 13, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 14),
    _SysDhcpAutoConfiguration_Type()
)
sysDhcpAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpAutoConfiguration.setStatus("current")
_SysPortDescriptionTable_Object = MibTable
sysPortDescriptionTable = _SysPortDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 16)
)
if mibBuilder.loadTexts:
    sysPortDescriptionTable.setStatus("current")
_SysPortDescriptionEntry_Object = MibTableRow
sysPortDescriptionEntry = _SysPortDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 16, 1)
)
sysPortDescriptionEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "sysPortDescIndex"),
)
if mibBuilder.loadTexts:
    sysPortDescriptionEntry.setStatus("current")


class _SysPortDescIndex_Type(Integer32):
    """Custom type sysPortDescIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysPortDescIndex_Type.__name__ = "Integer32"
_SysPortDescIndex_Object = MibTableColumn
sysPortDescIndex = _SysPortDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 16, 1, 1),
    _SysPortDescIndex_Type()
)
sysPortDescIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortDescIndex.setStatus("current")


class _SysPortDescString_Type(DisplayString):
    """Custom type sysPortDescString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysPortDescString_Type.__name__ = "DisplayString"
_SysPortDescString_Object = MibTableColumn
sysPortDescString = _SysPortDescString_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 16, 1, 2),
    _SysPortDescString_Type()
)
sysPortDescString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortDescString.setStatus("current")
_SysDdp_ObjectIdentity = ObjectIdentity
sysDdp = _SysDdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30)
)


class _SysDdpGlobalOnOff_Type(Integer32):
    """Custom type sysDdpGlobalOnOff based on Integer32"""
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


_SysDdpGlobalOnOff_Type.__name__ = "Integer32"
_SysDdpGlobalOnOff_Object = MibScalar
sysDdpGlobalOnOff = _SysDdpGlobalOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30, 1),
    _SysDdpGlobalOnOff_Type()
)
sysDdpGlobalOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDdpGlobalOnOff.setStatus("current")


class _SysDdpGeneralReportOnOff_Type(Integer32):
    """Custom type sysDdpGeneralReportOnOff based on Integer32"""
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


_SysDdpGeneralReportOnOff_Type.__name__ = "Integer32"
_SysDdpGeneralReportOnOff_Object = MibScalar
sysDdpGeneralReportOnOff = _SysDdpGeneralReportOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30, 2),
    _SysDdpGeneralReportOnOff_Type()
)
sysDdpGeneralReportOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDdpGeneralReportOnOff.setStatus("current")


class _SysDdpGeneralReportTimer_Type(Integer32):
    """Custom type sysDdpGeneralReportTimer based on Integer32"""
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
        *(("time120seconds", 120),
          ("time30seconds", 30),
          ("time60seconds", 60),
          ("time90seconds", 90))
    )


_SysDdpGeneralReportTimer_Type.__name__ = "Integer32"
_SysDdpGeneralReportTimer_Object = MibScalar
sysDdpGeneralReportTimer = _SysDdpGeneralReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30, 3),
    _SysDdpGeneralReportTimer_Type()
)
sysDdpGeneralReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDdpGeneralReportTimer.setStatus("current")
_SysDdpProtStatusTable_Object = MibTable
sysDdpProtStatusTable = _SysDdpProtStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30, 4)
)
if mibBuilder.loadTexts:
    sysDdpProtStatusTable.setStatus("current")
_SysDdpProtStatusEntry_Object = MibTableRow
sysDdpProtStatusEntry = _SysDdpProtStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30, 4, 1)
)
sysDdpProtStatusEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "sysDdpProtStatusIndex"),
)
if mibBuilder.loadTexts:
    sysDdpProtStatusEntry.setStatus("current")


class _SysDdpProtStatusIndex_Type(Integer32):
    """Custom type sysDdpProtStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysDdpProtStatusIndex_Type.__name__ = "Integer32"
_SysDdpProtStatusIndex_Object = MibTableColumn
sysDdpProtStatusIndex = _SysDdpProtStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30, 4, 1, 1),
    _SysDdpProtStatusIndex_Type()
)
sysDdpProtStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDdpProtStatusIndex.setStatus("current")


class _SysDdpProtStatusControl_Type(Integer32):
    """Custom type sysDdpProtStatusControl based on Integer32"""
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


_SysDdpProtStatusControl_Type.__name__ = "Integer32"
_SysDdpProtStatusControl_Object = MibTableColumn
sysDdpProtStatusControl = _SysDdpProtStatusControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 1, 30, 4, 1, 2),
    _SysDdpProtStatusControl_Type()
)
sysDdpProtStatusControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDdpProtStatusControl.setStatus("current")
_CompanyIpifGroup_ObjectIdentity = ObjectIdentity
companyIpifGroup = _CompanyIpifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2)
)
_IpifSupportV4V6Info_ObjectIdentity = ObjectIdentity
ipifSupportV4V6Info = _IpifSupportV4V6Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5)
)


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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 1),
    _SysIpAddrCfgMode_Type()
)
sysIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddrCfgMode.setStatus("current")
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 2),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("current")
_SysIpSubnetMask_Type = IpAddress
_SysIpSubnetMask_Object = MibScalar
sysIpSubnetMask = _SysIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 3),
    _SysIpSubnetMask_Type()
)
sysIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpSubnetMask.setStatus("current")
_SysGateway_Type = IpAddress
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 4),
    _SysGateway_Type()
)
sysGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGateway.setStatus("current")
_IpifName_Type = OctetString
_IpifName_Object = MibScalar
ipifName = _IpifName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 10),
    _Ipifv6NSRetransmitTime_Type()
)
ipifv6NSRetransmitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifv6NSRetransmitTime.setStatus("current")
_Ipifv6DefaultGateway_Type = Ipv6Address
_Ipifv6DefaultGateway_Object = MibScalar
ipifv6DefaultGateway = _Ipifv6DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 11),
    _Ipifv6DefaultGateway_Type()
)
ipifv6DefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifv6DefaultGateway.setStatus("current")
_IpifV6AddressTable_Object = MibTable
ipifV6AddressTable = _IpifV6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 12)
)
if mibBuilder.loadTexts:
    ipifV6AddressTable.setStatus("current")
_IpifV6AddressEntry_Object = MibTableRow
ipifV6AddressEntry = _IpifV6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 12, 1)
)
ipifV6AddressEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "ipifV6AddressMainIndex"),
    (0, "DGS-1210-20_CX", "ipifV6AddressIpAddr"),
    (0, "DGS-1210-20_CX", "ipifV6AddressIpPrefix"),
)
if mibBuilder.loadTexts:
    ipifV6AddressEntry.setStatus("current")
_IpifV6AddressMainIndex_Type = InterfaceIndex
_IpifV6AddressMainIndex_Object = MibTableColumn
ipifV6AddressMainIndex = _IpifV6AddressMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 12, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 12, 1, 2),
    _IpifV6AddressIpAddr_Type()
)
ipifV6AddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressIpAddr.setStatus("current")
_IpifV6AddressIpPrefix_Type = Integer32
_IpifV6AddressIpPrefix_Object = MibTableColumn
ipifV6AddressIpPrefix = _IpifV6AddressIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 12, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 12, 1, 4),
    _IpifV6AddressIpType_Type()
)
ipifV6AddressIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressIpType.setStatus("current")
_IpifV6AddressRowStatus_Type = RowStatus
_IpifV6AddressRowStatus_Object = MibTableColumn
ipifV6AddressRowStatus = _IpifV6AddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 5, 12, 1, 5),
    _IpifV6AddressRowStatus_Type()
)
ipifV6AddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifV6AddressRowStatus.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 6),
    _DhcpOption12Status_Type()
)
dhcpOption12Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12Status.setStatus("current")
_DhcpOption12HostName_Type = OctetString
_DhcpOption12HostName_Object = MibScalar
dhcpOption12HostName = _DhcpOption12HostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 2, 7),
    _DhcpOption12HostName_Type()
)
dhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12HostName.setStatus("current")
_CompanyTftpGroup_ObjectIdentity = ObjectIdentity
companyTftpGroup = _CompanyTftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3)
)
_TftpFwTargetGroup_ObjectIdentity = ObjectIdentity
tftpFwTargetGroup = _TftpFwTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 9)
)
_TftpFwTargetServerIpAddress_Type = Ipv6Address
_TftpFwTargetServerIpAddress_Object = MibScalar
tftpFwTargetServerIpAddress = _TftpFwTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 9, 2),
    _TftpFwTargetServerIpType_Type()
)
tftpFwTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTargetServerIpType.setStatus("current")
_TftpFwTargetInterfaceName_Type = OctetString
_TftpFwTargetInterfaceName_Object = MibScalar
tftpFwTargetInterfaceName = _TftpFwTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 9, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 9, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 9, 6),
    _TftpFwTargetTftpOperationStatus_Type()
)
tftpFwTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTargetTftpOperationStatus.setStatus("current")
_TftpCfgTargetGroup_ObjectIdentity = ObjectIdentity
tftpCfgTargetGroup = _TftpCfgTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 10)
)
_TftpCfgTargetServerIpAddress_Type = Ipv6Address
_TftpCfgTargetServerIpAddress_Object = MibScalar
tftpCfgTargetServerIpAddress = _TftpCfgTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 10, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 10, 2),
    _TftpCfgTargetServerIpType_Type()
)
tftpCfgTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetServerIpType.setStatus("current")
_TftpCfgTargetInterfaceName_Type = OctetString
_TftpCfgTargetInterfaceName_Object = MibScalar
tftpCfgTargetInterfaceName = _TftpCfgTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 10, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 10, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 3, 10, 6),
    _TftpCfgTargetTftpOperationStatus_Type()
)
tftpCfgTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpCfgTargetTftpOperationStatus.setStatus("current")
_CompanyMiscGroup_ObjectIdentity = ObjectIdentity
companyMiscGroup = _CompanyMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 4, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("current")
_CompanyRSTP_ObjectIdentity = ObjectIdentity
companyRSTP = _CompanyRSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6)
)
_StpGlobal_ObjectIdentity = ObjectIdentity
stpGlobal = _StpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 5),
    _StpProtocolSpecification_Type()
)
stpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpProtocolSpecification.setStatus("current")
_StpTimeSinceTopologyChange_Type = TimeTicks
_StpTimeSinceTopologyChange_Object = MibScalar
stpTimeSinceTopologyChange = _StpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 6),
    _StpTimeSinceTopologyChange_Type()
)
stpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTimeSinceTopologyChange.setStatus("current")
_StpTopChanges_Type = Counter32
_StpTopChanges_Object = MibScalar
stpTopChanges = _StpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 7),
    _StpTopChanges_Type()
)
stpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopChanges.setStatus("current")
_StpDesignatedRoot_Type = BridgeId
_StpDesignatedRoot_Object = MibScalar
stpDesignatedRoot = _StpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 8),
    _StpDesignatedRoot_Type()
)
stpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesignatedRoot.setStatus("current")
_StpRootCost_Type = Integer32
_StpRootCost_Object = MibScalar
stpRootCost = _StpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 9),
    _StpRootCost_Type()
)
stpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootCost.setStatus("current")
_StpRootPort_Type = Integer32
_StpRootPort_Object = MibScalar
stpRootPort = _StpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 10),
    _StpRootPort_Type()
)
stpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootPort.setStatus("current")
_StpMaxAge_Type = Timeout
_StpMaxAge_Object = MibScalar
stpMaxAge = _StpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 11),
    _StpMaxAge_Type()
)
stpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpMaxAge.setStatus("current")
_StpHelloTime_Type = Timeout
_StpHelloTime_Object = MibScalar
stpHelloTime = _StpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 12),
    _StpHelloTime_Type()
)
stpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHelloTime.setStatus("current")
_StpHoldTime_Type = Integer32
_StpHoldTime_Object = MibScalar
stpHoldTime = _StpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 13),
    _StpHoldTime_Type()
)
stpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHoldTime.setStatus("current")
_StpForwardDelay_Type = Timeout
_StpForwardDelay_Object = MibScalar
stpForwardDelay = _StpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 1, 17),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("current")
_StpPortEntry_Object = MibTableRow
stpPortEntry = _StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1)
)
stpPortEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "stpPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 6),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortDesignatedRoot_Type = BridgeId
_StpPortDesignatedRoot_Object = MibTableColumn
stpPortDesignatedRoot = _StpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 7),
    _StpPortDesignatedRoot_Type()
)
stpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedRoot.setStatus("current")
_StpPortDesignatedCost_Type = Integer32
_StpPortDesignatedCost_Object = MibTableColumn
stpPortDesignatedCost = _StpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 8),
    _StpPortDesignatedCost_Type()
)
stpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedCost.setStatus("current")
_StpPortDesignatedBridge_Type = BridgeId
_StpPortDesignatedBridge_Object = MibTableColumn
stpPortDesignatedBridge = _StpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 10),
    _StpPortDesignatedPort_Type()
)
stpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedPort.setStatus("current")
_StpPortForwardTransitions_Type = Counter32
_StpPortForwardTransitions_Object = MibTableColumn
stpPortForwardTransitions = _StpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 11),
    _StpPortForwardTransitions_Type()
)
stpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortForwardTransitions.setStatus("current")
_StpPortProtocolMigration_Type = TruthValue
_StpPortProtocolMigration_Object = MibTableColumn
stpPortProtocolMigration = _StpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 12),
    _StpPortProtocolMigration_Type()
)
stpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortProtocolMigration.setStatus("current")
_StpPortOperEdgePort_Type = TruthValue
_StpPortOperEdgePort_Object = MibTableColumn
stpPortOperEdgePort = _StpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 14),
    _StpPortAdminPointToPoint_Type()
)
stpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortAdminPointToPoint.setStatus("current")
_StpPortOperPointToPoint_Type = TruthValue
_StpPortOperPointToPoint_Object = MibTableColumn
stpPortOperPointToPoint = _StpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 16),
    _StpPortEdge_Type()
)
stpPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEdge.setStatus("current")
_StpPortRestrictedRole_Type = TruthValue
_StpPortRestrictedRole_Object = MibTableColumn
stpPortRestrictedRole = _StpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 17),
    _StpPortRestrictedRole_Type()
)
stpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedRole.setStatus("current")
_StpPortRestrictedTCN_Type = TruthValue
_StpPortRestrictedTCN_Object = MibTableColumn
stpPortRestrictedTCN = _StpPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 6, 2, 1, 18),
    _StpPortRestrictedTCN_Type()
)
stpPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRestrictedTCN.setStatus("current")
_CompanyDot1qVlanGroup_ObjectIdentity = ObjectIdentity
companyDot1qVlanGroup = _CompanyDot1qVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 5),
    _Dot1qVlanAsyOnOff_Type()
)
dot1qVlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanAsyOnOff.setStatus("current")
_Dot1qVlanTable_Object = MibTable
dot1qVlanTable = _Dot1qVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 6)
)
if mibBuilder.loadTexts:
    dot1qVlanTable.setStatus("current")
_Dot1qVlanEntry_Object = MibTableRow
dot1qVlanEntry = _Dot1qVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 6, 1)
)
dot1qVlanEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dot1qVlanName"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 6, 1, 1),
    _Dot1qVlanName_Type()
)
dot1qVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanName.setStatus("current")
_Dot1qVlanEgressPorts_Type = PortList
_Dot1qVlanEgressPorts_Object = MibTableColumn
dot1qVlanEgressPorts = _Dot1qVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 6, 1, 2),
    _Dot1qVlanEgressPorts_Type()
)
dot1qVlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanEgressPorts.setStatus("current")
_Dot1qVlanUntaggedPorts_Type = PortList
_Dot1qVlanUntaggedPorts_Object = MibTableColumn
dot1qVlanUntaggedPorts = _Dot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 6, 1, 4),
    _Dot1qVlanUntaggedPorts_Type()
)
dot1qVlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanUntaggedPorts.setStatus("current")
_Dot1qVlanRowStatus_Type = RowStatus
_Dot1qVlanRowStatus_Object = MibTableColumn
dot1qVlanRowStatus = _Dot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 6, 1, 5),
    _Dot1qVlanRowStatus_Type()
)
dot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanRowStatus.setStatus("current")
_Dot1qVlanPortTable_Object = MibTable
dot1qVlanPortTable = _Dot1qVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 7)
)
if mibBuilder.loadTexts:
    dot1qVlanPortTable.setStatus("current")
_Dot1qVlanPortEntry_Object = MibTableRow
dot1qVlanPortEntry = _Dot1qVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 7, 1)
)
if mibBuilder.loadTexts:
    dot1qVlanPortEntry.setStatus("current")


class _Dot1qVlanPvid_Type(VlanIndex):
    """Custom type dot1qVlanPvid based on VlanIndex"""
    defaultValue = 1


_Dot1qVlanPvid_Object = MibTableColumn
dot1qVlanPvid = _Dot1qVlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 7, 1, 1),
    _Dot1qVlanPvid_Type()
)
dot1qVlanPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPvid.setStatus("current")
_Dot1qVlanUngisterMCFilterTable_Object = MibTable
dot1qVlanUngisterMCFilterTable = _Dot1qVlanUngisterMCFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 8)
)
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFilterTable.setStatus("current")
_Dot1qVlanUngisterMCFilterEntry_Object = MibTableRow
dot1qVlanUngisterMCFilterEntry = _Dot1qVlanUngisterMCFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 8, 1)
)
dot1qVlanUngisterMCFilterEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dot1qVlanUngisterMCFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 7, 8, 1, 2),
    _Dot1qVlanUngisterMCFiltermode_Type()
)
dot1qVlanUngisterMCFiltermode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanUngisterMCFiltermode.setStatus("current")
_CompanyLA_ObjectIdentity = ObjectIdentity
companyLA = _CompanyLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8)
)
_LaSystem_ObjectIdentity = ObjectIdentity
laSystem = _LaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 1, 2),
    _LaStatus_Type()
)
laStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laStatus.setStatus("current")
_LaPortChannelTable_Object = MibTable
laPortChannelTable = _LaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    laPortChannelTable.setStatus("current")
_LaPortChannelEntry_Object = MibTableRow
laPortChannelEntry = _LaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 1, 3, 1)
)
laPortChannelEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "laPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    laPortChannelEntry.setStatus("current")
_LaPortChannelIfIndex_Type = InterfaceIndex
_LaPortChannelIfIndex_Object = MibTableColumn
laPortChannelIfIndex = _LaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 1, 3, 1, 1),
    _LaPortChannelIfIndex_Type()
)
laPortChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laPortChannelIfIndex.setStatus("current")
_LaPortChannelMemberList_Type = PortList
_LaPortChannelMemberList_Object = MibTableColumn
laPortChannelMemberList = _LaPortChannelMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 1, 3, 1, 2),
    _LaPortChannelMemberList_Type()
)
laPortChannelMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMemberList.setStatus("current")
_LaPortChannelMode_Type = PortLaMode
_LaPortChannelMode_Object = MibTableColumn
laPortChannelMode = _LaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 1, 3, 1, 3),
    _LaPortChannelMode_Type()
)
laPortChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortChannelMode.setStatus("current")
_LaPortControl_ObjectIdentity = ObjectIdentity
laPortControl = _LaPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 2)
)
_LaPortControlTable_Object = MibTable
laPortControlTable = _LaPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    laPortControlTable.setStatus("current")
_LaPortControlEntry_Object = MibTableRow
laPortControlEntry = _LaPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 2, 1, 1)
)
laPortControlEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "laPortControlIndex"),
)
if mibBuilder.loadTexts:
    laPortControlEntry.setStatus("current")
_LaPortControlIndex_Type = InterfaceIndex
_LaPortControlIndex_Object = MibTableColumn
laPortControlIndex = _LaPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 8, 2, 1, 1, 4),
    _LaPortActorTimeout_Type()
)
laPortActorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laPortActorTimeout.setStatus("current")
_CompanyStaticMAC_ObjectIdentity = ObjectIdentity
companyStaticMAC = _CompanyStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 1),
    _StaticDisableAutoLearn_Type()
)
staticDisableAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDisableAutoLearn.setStatus("current")
_StaticAutoLearningList_Type = PortList
_StaticAutoLearningList_Object = MibScalar
staticAutoLearningList = _StaticAutoLearningList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 2),
    _StaticAutoLearningList_Type()
)
staticAutoLearningList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticAutoLearningList.setStatus("current")
_StaticTable_Object = MibTable
staticTable = _StaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 3)
)
if mibBuilder.loadTexts:
    staticTable.setStatus("current")
_StaticEntry_Object = MibTableRow
staticEntry = _StaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 3, 1)
)
staticEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "staticVlanID"),
    (0, "DGS-1210-20_CX", "staticMac"),
    (0, "DGS-1210-20_CX", "staticPort"),
)
if mibBuilder.loadTexts:
    staticEntry.setStatus("current")
_StaticVlanID_Type = Integer32
_StaticVlanID_Object = MibTableColumn
staticVlanID = _StaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 3, 1, 1),
    _StaticVlanID_Type()
)
staticVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticVlanID.setStatus("current")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 3, 1, 2),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMac.setStatus("current")
_StaticPort_Type = Integer32
_StaticPort_Object = MibTableColumn
staticPort = _StaticPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 3, 1, 3),
    _StaticPort_Type()
)
staticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticPort.setStatus("current")
_StaticStatus_Type = RowStatus
_StaticStatus_Object = MibTableColumn
staticStatus = _StaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 9, 3, 1, 4),
    _StaticStatus_Type()
)
staticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticStatus.setStatus("current")
_CompanyIgsGroup_ObjectIdentity = ObjectIdentity
companyIgsGroup = _CompanyIgsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10)
)
_IgsSystem_ObjectIdentity = ObjectIdentity
igsSystem = _IgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 1, 8),
    _IgsReportToAllPort_Type()
)
igsReportToAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsReportToAllPort.setStatus("current")
_IgsVlan_ObjectIdentity = ObjectIdentity
igsVlan = _IgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3)
)
_IgsVlanRouterTable_Object = MibTable
igsVlanRouterTable = _IgsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    igsVlanRouterTable.setStatus("current")
_IgsVlanRouterEntry_Object = MibTableRow
igsVlanRouterEntry = _IgsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 3, 1)
)
igsVlanRouterEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "igsVlanRouterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 3, 1, 1),
    _IgsVlanRouterVlanId_Type()
)
igsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterVlanId.setStatus("current")
_IgsVlanRouterPortList_Type = PortList
_IgsVlanRouterPortList_Object = MibTableColumn
igsVlanRouterPortList = _IgsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 3, 1, 2),
    _IgsVlanRouterPortList_Type()
)
igsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterPortList.setStatus("current")
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("current")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "igsVlanFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1, 5),
    _IgsVlanQueryInterval_Type()
)
igsVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanQueryInterval.setStatus("current")
_IgsVlanRtrPortList_Type = PortList
_IgsVlanRtrPortList_Object = MibTableColumn
igsVlanRtrPortList = _IgsVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 4, 1, 8),
    _IgsVlanFastLeave_Type()
)
igsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFastLeave.setStatus("current")
_IgsVlanMulticastGroupTable_Object = MibTable
igsVlanMulticastGroupTable = _IgsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 5)
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupTable.setStatus("current")
_IgsVlanMulticastGroupEntry_Object = MibTableRow
igsVlanMulticastGroupEntry = _IgsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 5, 1)
)
igsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "igsVlanMulticastGroupVlanId"),
    (0, "DGS-1210-20_CX", "igsVlanMulticastGroupIpAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 5, 1, 1),
    _IgsVlanMulticastGroupVlanId_Type()
)
igsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupVlanId.setStatus("current")
_IgsVlanMulticastGroupIpAddress_Type = InetAddress
_IgsVlanMulticastGroupIpAddress_Object = MibTableColumn
igsVlanMulticastGroupIpAddress = _IgsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 5, 1, 2),
    _IgsVlanMulticastGroupIpAddress_Type()
)
igsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupIpAddress.setStatus("current")
_IgsVlanMulticastGroupMacAddress_Type = MacAddress
_IgsVlanMulticastGroupMacAddress_Object = MibTableColumn
igsVlanMulticastGroupMacAddress = _IgsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 5, 1, 3),
    _IgsVlanMulticastGroupMacAddress_Type()
)
igsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupMacAddress.setStatus("current")
_IgsVlanMulticastGroupPortList_Type = PortList
_IgsVlanMulticastGroupPortList_Object = MibTableColumn
igsVlanMulticastGroupPortList = _IgsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 10, 3, 5, 1, 4),
    _IgsVlanMulticastGroupPortList_Type()
)
igsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupPortList.setStatus("current")
_CompanyQoSGroup_ObjectIdentity = ObjectIdentity
companyQoSGroup = _CompanyQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 2),
    _QueuingMechanism_Type()
)
queuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMechanism.setStatus("current")
_QosQ1p_ObjectIdentity = ObjectIdentity
qosQ1p = _QosQ1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 3)
)
_Dot1pPortTable_Object = MibTable
dot1pPortTable = _Dot1pPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    dot1pPortTable.setStatus("current")
_Dot1pPortEntry_Object = MibTableRow
dot1pPortEntry = _Dot1pPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 3, 1, 1)
)
dot1pPortEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dot1pPortIndex"),
)
if mibBuilder.loadTexts:
    dot1pPortEntry.setStatus("current")
_Dot1pPortIndex_Type = Integer32
_Dot1pPortIndex_Object = MibTableColumn
dot1pPortIndex = _Dot1pPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 3, 1, 1, 1),
    _Dot1pPortIndex_Type()
)
dot1pPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pPortIndex.setStatus("current")


class _Dot1pPortPriority_Type(Integer32):
    """Custom type dot1pPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1pPortPriority_Type.__name__ = "Integer32"
_Dot1pPortPriority_Object = MibTableColumn
dot1pPortPriority = _Dot1pPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 3, 1, 1, 2),
    _Dot1pPortPriority_Type()
)
dot1pPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1pPortPriority.setStatus("current")
_QosDiffServ_ObjectIdentity = ObjectIdentity
qosDiffServ = _QosDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 1),
    _QosDiffServEnable_Type()
)
qosDiffServEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDiffServEnable.setStatus("current")
_QosDiffServTypeGroup_ObjectIdentity = ObjectIdentity
qosDiffServTypeGroup = _QosDiffServTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 21),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 23),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 24),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 25),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 26),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 27),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 28),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 29),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 30),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 31),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 32),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 33),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 34),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 35),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 36),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 37),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 38),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 39),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 40),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 41),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 42),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 43),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 44),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 45),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 46),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 47),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 48),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 49),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 50),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 51),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 52),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 53),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 54),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 55),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 56),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 57),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 58),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 59),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 60),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 61),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 62),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 63),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 4, 2, 64),
    _QosDiffServType63_Type()
)
qosDiffServType63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType63.setStatus("current")
_QosTOS_ObjectIdentity = ObjectIdentity
qosTOS = _QosTOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 1),
    _QosTOSEnable_Type()
)
qosTOSEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTOSEnable.setStatus("current")
_QosTOSGroup_ObjectIdentity = ObjectIdentity
qosTOSGroup = _QosTOSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2)
)


class _QosTOSType00_Type(Integer32):
    """Custom type qosTOSType00 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType00_Type.__name__ = "Integer32"
_QosTOSType00_Object = MibScalar
qosTOSType00 = _QosTOSType00_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 1),
    _QosTOSType00_Type()
)
qosTOSType00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType00.setStatus("current")


class _QosTOSType01_Type(Integer32):
    """Custom type qosTOSType01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType01_Type.__name__ = "Integer32"
_QosTOSType01_Object = MibScalar
qosTOSType01 = _QosTOSType01_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 2),
    _QosTOSType01_Type()
)
qosTOSType01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType01.setStatus("current")


class _QosTOSType02_Type(Integer32):
    """Custom type qosTOSType02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType02_Type.__name__ = "Integer32"
_QosTOSType02_Object = MibScalar
qosTOSType02 = _QosTOSType02_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 3),
    _QosTOSType02_Type()
)
qosTOSType02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType02.setStatus("current")


class _QosTOSType03_Type(Integer32):
    """Custom type qosTOSType03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType03_Type.__name__ = "Integer32"
_QosTOSType03_Object = MibScalar
qosTOSType03 = _QosTOSType03_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 4),
    _QosTOSType03_Type()
)
qosTOSType03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType03.setStatus("current")


class _QosTOSType04_Type(Integer32):
    """Custom type qosTOSType04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType04_Type.__name__ = "Integer32"
_QosTOSType04_Object = MibScalar
qosTOSType04 = _QosTOSType04_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 5),
    _QosTOSType04_Type()
)
qosTOSType04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType04.setStatus("current")


class _QosTOSType05_Type(Integer32):
    """Custom type qosTOSType05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType05_Type.__name__ = "Integer32"
_QosTOSType05_Object = MibScalar
qosTOSType05 = _QosTOSType05_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 6),
    _QosTOSType05_Type()
)
qosTOSType05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType05.setStatus("current")


class _QosTOSType06_Type(Integer32):
    """Custom type qosTOSType06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType06_Type.__name__ = "Integer32"
_QosTOSType06_Object = MibScalar
qosTOSType06 = _QosTOSType06_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 7),
    _QosTOSType06_Type()
)
qosTOSType06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType06.setStatus("current")


class _QosTOSType07_Type(Integer32):
    """Custom type qosTOSType07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTOSType07_Type.__name__ = "Integer32"
_QosTOSType07_Object = MibScalar
qosTOSType07 = _QosTOSType07_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 12, 5, 2, 8),
    _QosTOSType07_Type()
)
qosTOSType07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOSType07.setStatus("current")
_CompanyTrafficMgmt_ObjectIdentity = ObjectIdentity
companyTrafficMgmt = _CompanyTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13)
)
_BandwidthCtrlSettings_ObjectIdentity = ObjectIdentity
bandwidthCtrlSettings = _BandwidthCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 1)
)
_BandwidthCtrlTable_Object = MibTable
bandwidthCtrlTable = _BandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    bandwidthCtrlTable.setStatus("current")
_BandwidthCtrlEntry_Object = MibTableRow
bandwidthCtrlEntry = _BandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 1, 2, 1)
)
bandwidthCtrlEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "bandwidthCtrlIndex"),
)
if mibBuilder.loadTexts:
    bandwidthCtrlEntry.setStatus("current")
_BandwidthCtrlIndex_Type = Integer32
_BandwidthCtrlIndex_Object = MibTableColumn
bandwidthCtrlIndex = _BandwidthCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 1, 2, 1, 3),
    _BandwidthCtrlRxThreshold_Type()
)
bandwidthCtrlRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlRxThreshold.setStatus("current")
_BroadcastStormCtrlSettings_ObjectIdentity = ObjectIdentity
broadcastStormCtrlSettings = _BroadcastStormCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 13, 3, 3),
    _BroadcastStormCtrlThreshold_Type()
)
broadcastStormCtrlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormCtrlThreshold.setStatus("current")
_CompanySecurity_ObjectIdentity = ObjectIdentity
companySecurity = _CompanySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14)
)
_SecurityTrustedHost_ObjectIdentity = ObjectIdentity
securityTrustedHost = _SecurityTrustedHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1, 1),
    _TrustedHostStatus_Type()
)
trustedHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostStatus.setStatus("current")
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("current")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1, 3, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "trustedHostIPType"),
    (0, "DGS-1210-20_CX", "trustedHostIpAddr"),
    (0, "DGS-1210-20_CX", "trustedHostIpMask"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1, 3, 1, 1),
    _TrustedHostIPType_Type()
)
trustedHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIPType.setStatus("current")
_TrustedHostIpAddr_Type = DisplayString
_TrustedHostIpAddr_Object = MibTableColumn
trustedHostIpAddr = _TrustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1, 3, 1, 2),
    _TrustedHostIpAddr_Type()
)
trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpAddr.setStatus("current")
_TrustedHostIpMask_Type = DisplayString
_TrustedHostIpMask_Object = MibTableColumn
trustedHostIpMask = _TrustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1, 3, 1, 3),
    _TrustedHostIpMask_Type()
)
trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpMask.setStatus("current")
_TrustedHostRowStatus_Type = RowStatus
_TrustedHostRowStatus_Object = MibTableColumn
trustedHostRowStatus = _TrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 1, 3, 1, 4),
    _TrustedHostRowStatus_Type()
)
trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedHostRowStatus.setStatus("current")
_SecurityPortSecurity_ObjectIdentity = ObjectIdentity
securityPortSecurity = _SecurityPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 2)
)
_PortSecTable_Object = MibTable
portSecTable = _PortSecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    portSecTable.setStatus("current")
_PortSecEntry_Object = MibTableRow
portSecEntry = _PortSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 2, 1, 1)
)
portSecEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "portSecIndex"),
)
if mibBuilder.loadTexts:
    portSecEntry.setStatus("current")
_PortSecIndex_Type = Integer32
_PortSecIndex_Object = MibTableColumn
portSecIndex = _PortSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 2, 1, 1, 3),
    _PortSecMLA_Type()
)
portSecMLA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMLA.setStatus("current")
_SecurityARPSpoofPrevent_ObjectIdentity = ObjectIdentity
securityARPSpoofPrevent = _SecurityARPSpoofPrevent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 3)
)
_ARPSpoofPreventTable_Object = MibTable
aRPSpoofPreventTable = _ARPSpoofPreventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    aRPSpoofPreventTable.setStatus("current")
_ARPSpoofPreventEntry_Object = MibTableRow
aRPSpoofPreventEntry = _ARPSpoofPreventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 3, 1, 1)
)
aRPSpoofPreventEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aRPSpoofPreventIpAddr"),
)
if mibBuilder.loadTexts:
    aRPSpoofPreventEntry.setStatus("current")
_ARPSpoofPreventIpAddr_Type = IpAddress
_ARPSpoofPreventIpAddr_Object = MibTableColumn
aRPSpoofPreventIpAddr = _ARPSpoofPreventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 3, 1, 1, 2),
    _ARPSpoofPreventMacAddress_Type()
)
aRPSpoofPreventMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventMacAddress.setStatus("current")
_ARPSpoofPreventPortList_Type = PortList
_ARPSpoofPreventPortList_Object = MibTableColumn
aRPSpoofPreventPortList = _ARPSpoofPreventPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 3, 1, 1, 3),
    _ARPSpoofPreventPortList_Type()
)
aRPSpoofPreventPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRPSpoofPreventPortList.setStatus("current")
_ARPSpoofPreventRowStatus_Type = RowStatus
_ARPSpoofPreventRowStatus_Object = MibTableColumn
aRPSpoofPreventRowStatus = _ARPSpoofPreventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 3, 1, 1, 4),
    _ARPSpoofPreventRowStatus_Type()
)
aRPSpoofPreventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aRPSpoofPreventRowStatus.setStatus("current")
_SecuritySSL_ObjectIdentity = ObjectIdentity
securitySSL = _SecuritySSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 5)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 5, 1),
    _SslSecurityHttpStatus_Type()
)
sslSecurityHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSecurityHttpStatus.setStatus("current")
_SslCiphers_ObjectIdentity = ObjectIdentity
sslCiphers = _SslCiphers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 5, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 5, 2, 1),
    _SslCipherSuiteList_Type()
)
sslCipherSuiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCipherSuiteList.setStatus("current")
_SecurityDhcpServerScreen_ObjectIdentity = ObjectIdentity
securityDhcpServerScreen = _SecurityDhcpServerScreen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7)
)
_DhcpServerScreenEnablePortlist_Type = PortList
_DhcpServerScreenEnablePortlist_Object = MibScalar
dhcpServerScreenEnablePortlist = _DhcpServerScreenEnablePortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7, 1),
    _DhcpServerScreenEnablePortlist_Type()
)
dhcpServerScreenEnablePortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenEnablePortlist.setStatus("current")
_DhcpServerScreenTrustedServerTable_Object = MibTable
dhcpServerScreenTrustedServerTable = _DhcpServerScreenTrustedServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7, 3)
)
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerTable.setStatus("current")
_DhcpServerScreenTrustedServerEntry_Object = MibTableRow
dhcpServerScreenTrustedServerEntry = _DhcpServerScreenTrustedServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7, 3, 1)
)
dhcpServerScreenTrustedServerEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dhcpServerScreenTrustedServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7, 3, 1, 1),
    _DhcpServerScreenTrustedServerIndex_Type()
)
dhcpServerScreenTrustedServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerIndex.setStatus("current")
_DhcpServerScreenTrustedServerAddress_Type = Ipv6Address
_DhcpServerScreenTrustedServerAddress_Object = MibTableColumn
dhcpServerScreenTrustedServerAddress = _DhcpServerScreenTrustedServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7, 3, 1, 3),
    _DhcpServerScreenIPType_Type()
)
dhcpServerScreenIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerScreenIPType.setStatus("current")
_DhcpServerScreenTrustedServerStatus_Type = RowStatus
_DhcpServerScreenTrustedServerStatus_Object = MibTableColumn
dhcpServerScreenTrustedServerStatus = _DhcpServerScreenTrustedServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 7, 3, 1, 4),
    _DhcpServerScreenTrustedServerStatus_Type()
)
dhcpServerScreenTrustedServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerScreenTrustedServerStatus.setStatus("current")
_SecuritySSH_ObjectIdentity = ObjectIdentity
securitySSH = _SecuritySSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8)
)


class _SshSecurityStatus_Type(Integer32):
    """Custom type sshSecurityStatus based on Integer32"""
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


_SshSecurityStatus_Type.__name__ = "Integer32"
_SshSecurityStatus_Object = MibScalar
sshSecurityStatus = _SshSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 1),
    _SshSecurityStatus_Type()
)
sshSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSecurityStatus.setStatus("current")


class _SshMaxAuthFailAttempts_Type(Integer32):
    """Custom type sshMaxAuthFailAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_SshMaxAuthFailAttempts_Type.__name__ = "Integer32"
_SshMaxAuthFailAttempts_Object = MibScalar
sshMaxAuthFailAttempts = _SshMaxAuthFailAttempts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 2),
    _SshMaxAuthFailAttempts_Type()
)
sshMaxAuthFailAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshMaxAuthFailAttempts.setStatus("current")


class _SshSessionKeyRekeying_Type(Integer32):
    """Custom type sshSessionKeyRekeying based on Integer32"""
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
        *(("never", 0),
          ("sixty-min", 3),
          ("ten-min", 1),
          ("thirty-min", 2))
    )


_SshSessionKeyRekeying_Type.__name__ = "Integer32"
_SshSessionKeyRekeying_Object = MibScalar
sshSessionKeyRekeying = _SshSessionKeyRekeying_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 3),
    _SshSessionKeyRekeying_Type()
)
sshSessionKeyRekeying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSessionKeyRekeying.setStatus("current")


class _SshMaxSession_Type(Integer32):
    """Custom type sshMaxSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SshMaxSession_Type.__name__ = "Integer32"
_SshMaxSession_Object = MibScalar
sshMaxSession = _SshMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 4),
    _SshMaxSession_Type()
)
sshMaxSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshMaxSession.setStatus("current")


class _SshConnectionTimeout_Type(Integer32):
    """Custom type sshConnectionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 600),
    )


_SshConnectionTimeout_Type.__name__ = "Integer32"
_SshConnectionTimeout_Object = MibScalar
sshConnectionTimeout = _SshConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 5),
    _SshConnectionTimeout_Type()
)
sshConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshConnectionTimeout.setStatus("current")


class _SshAuthenMethodPassWordAdmin_Type(Integer32):
    """Custom type sshAuthenMethodPassWordAdmin based on Integer32"""
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


_SshAuthenMethodPassWordAdmin_Type.__name__ = "Integer32"
_SshAuthenMethodPassWordAdmin_Object = MibScalar
sshAuthenMethodPassWordAdmin = _SshAuthenMethodPassWordAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 6),
    _SshAuthenMethodPassWordAdmin_Type()
)
sshAuthenMethodPassWordAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshAuthenMethodPassWordAdmin.setStatus("current")


class _SshAuthenMethodPubKeyAdmin_Type(Integer32):
    """Custom type sshAuthenMethodPubKeyAdmin based on Integer32"""
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


_SshAuthenMethodPubKeyAdmin_Type.__name__ = "Integer32"
_SshAuthenMethodPubKeyAdmin_Object = MibScalar
sshAuthenMethodPubKeyAdmin = _SshAuthenMethodPubKeyAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 7),
    _SshAuthenMethodPubKeyAdmin_Type()
)
sshAuthenMethodPubKeyAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshAuthenMethodPubKeyAdmin.setStatus("current")


class _SshAuthenMethodHostKeyAdmin_Type(Integer32):
    """Custom type sshAuthenMethodHostKeyAdmin based on Integer32"""
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


_SshAuthenMethodHostKeyAdmin_Type.__name__ = "Integer32"
_SshAuthenMethodHostKeyAdmin_Object = MibScalar
sshAuthenMethodHostKeyAdmin = _SshAuthenMethodHostKeyAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 8),
    _SshAuthenMethodHostKeyAdmin_Type()
)
sshAuthenMethodHostKeyAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshAuthenMethodHostKeyAdmin.setStatus("current")


class _SshCipherSuiteList_Type(Bits):
    """Custom type sshCipherSuiteList based on Bits"""
    namedValues = NamedValues(
        ("tripleDESCBC", 0)
    )

_SshCipherSuiteList_Type.__name__ = "Bits"
_SshCipherSuiteList_Object = MibScalar
sshCipherSuiteList = _SshCipherSuiteList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 9),
    _SshCipherSuiteList_Type()
)
sshCipherSuiteList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshCipherSuiteList.setStatus("current")


class _SshMacSuiteList_Type(Bits):
    """Custom type sshMacSuiteList based on Bits"""
    namedValues = NamedValues(
        *(("hMAC-MD5", 1),
          ("hMAC-SHA1", 0))
    )

_SshMacSuiteList_Type.__name__ = "Bits"
_SshMacSuiteList_Object = MibScalar
sshMacSuiteList = _SshMacSuiteList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 10),
    _SshMacSuiteList_Type()
)
sshMacSuiteList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshMacSuiteList.setStatus("current")


class _SshPublKeyRSAAdmin_Type(Integer32):
    """Custom type sshPublKeyRSAAdmin based on Integer32"""
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


_SshPublKeyRSAAdmin_Type.__name__ = "Integer32"
_SshPublKeyRSAAdmin_Object = MibScalar
sshPublKeyRSAAdmin = _SshPublKeyRSAAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 11),
    _SshPublKeyRSAAdmin_Type()
)
sshPublKeyRSAAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshPublKeyRSAAdmin.setStatus("current")
_SshUserInfoTable_Object = MibTable
sshUserInfoTable = _SshUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12)
)
if mibBuilder.loadTexts:
    sshUserInfoTable.setStatus("current")
_SshUserInfoEntry_Object = MibTableRow
sshUserInfoEntry = _SshUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12, 1)
)
sshUserInfoEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "sshUserInfoID"),
)
if mibBuilder.loadTexts:
    sshUserInfoEntry.setStatus("current")
_SshUserInfoID_Type = Integer32
_SshUserInfoID_Object = MibTableColumn
sshUserInfoID = _SshUserInfoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12, 1, 1),
    _SshUserInfoID_Type()
)
sshUserInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserInfoID.setStatus("current")


class _SshUserInfoUserName_Type(DisplayString):
    """Custom type sshUserInfoUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SshUserInfoUserName_Type.__name__ = "DisplayString"
_SshUserInfoUserName_Object = MibTableColumn
sshUserInfoUserName = _SshUserInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12, 1, 2),
    _SshUserInfoUserName_Type()
)
sshUserInfoUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserInfoUserName.setStatus("current")


class _SshUserInfoAuth_Type(Integer32):
    """Custom type sshUserInfoAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hostbased", 1),
          ("password", 2),
          ("publickey", 4))
    )


_SshUserInfoAuth_Type.__name__ = "Integer32"
_SshUserInfoAuth_Object = MibTableColumn
sshUserInfoAuth = _SshUserInfoAuth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12, 1, 3),
    _SshUserInfoAuth_Type()
)
sshUserInfoAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserInfoAuth.setStatus("current")


class _SshUserInfoHostName_Type(DisplayString):
    """Custom type sshUserInfoHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SshUserInfoHostName_Type.__name__ = "DisplayString"
_SshUserInfoHostName_Object = MibTableColumn
sshUserInfoHostName = _SshUserInfoHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12, 1, 4),
    _SshUserInfoHostName_Type()
)
sshUserInfoHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserInfoHostName.setStatus("current")
_SshUserInfoHostIp_Type = IpAddress
_SshUserInfoHostIp_Object = MibTableColumn
sshUserInfoHostIp = _SshUserInfoHostIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12, 1, 5),
    _SshUserInfoHostIp_Type()
)
sshUserInfoHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserInfoHostIp.setStatus("current")
_SshUserInfoHostIpv6_Type = Ipv6Address
_SshUserInfoHostIpv6_Object = MibTableColumn
sshUserInfoHostIpv6 = _SshUserInfoHostIpv6_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 8, 12, 1, 6),
    _SshUserInfoHostIpv6_Type()
)
sshUserInfoHostIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserInfoHostIpv6.setStatus("current")
_SecurityTrafficSeg_ObjectIdentity = ObjectIdentity
securityTrafficSeg = _SecurityTrafficSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 9, 1),
    _TrafficSegStatus_Type()
)
trafficSegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegStatus.setStatus("current")
_TrafficSegTable_Object = MibTable
trafficSegTable = _TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 9, 2)
)
if mibBuilder.loadTexts:
    trafficSegTable.setStatus("current")
_TrafficSegEntry_Object = MibTableRow
trafficSegEntry = _TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 9, 2, 1)
)
trafficSegEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "trafficSegIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegEntry.setStatus("current")
_TrafficSegIfIndex_Type = InterfaceIndex
_TrafficSegIfIndex_Object = MibTableColumn
trafficSegIfIndex = _TrafficSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 9, 2, 1, 1),
    _TrafficSegIfIndex_Type()
)
trafficSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegIfIndex.setStatus("current")
_TrafficSegMemberList_Type = PortList
_TrafficSegMemberList_Object = MibTableColumn
trafficSegMemberList = _TrafficSegMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 9, 2, 1, 2),
    _TrafficSegMemberList_Type()
)
trafficSegMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegMemberList.setStatus("current")
_SecurityIpMacPortBinding_ObjectIdentity = ObjectIdentity
securityIpMacPortBinding = _SecurityIpMacPortBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10)
)
_ImpbSettingTable_Object = MibTable
impbSettingTable = _ImpbSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 1)
)
if mibBuilder.loadTexts:
    impbSettingTable.setStatus("current")
_ImpbSettingEntry_Object = MibTableRow
impbSettingEntry = _ImpbSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 1, 1)
)
impbSettingEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "impbPortIndex"),
)
if mibBuilder.loadTexts:
    impbSettingEntry.setStatus("current")
_ImpbPortIndex_Type = Integer32
_ImpbPortIndex_Object = MibTableColumn
impbPortIndex = _ImpbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 1, 1, 4),
    _ImpbDHCPPortState_Type()
)
impbDHCPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbDHCPPortState.setStatus("current")
_ImpbSmartTable_Object = MibTable
impbSmartTable = _ImpbSmartTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 2)
)
if mibBuilder.loadTexts:
    impbSmartTable.setStatus("current")
_ImpbSmartEntry_Object = MibTableRow
impbSmartEntry = _ImpbSmartEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 2, 1)
)
impbSmartEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "impbSmartMacAddress"),
    (0, "DGS-1210-20_CX", "impbSmartPort"),
    (0, "DGS-1210-20_CX", "impbSmartIpAddress"),
)
if mibBuilder.loadTexts:
    impbSmartEntry.setStatus("current")
_ImpbSmartMacAddress_Type = MacAddress
_ImpbSmartMacAddress_Object = MibTableColumn
impbSmartMacAddress = _ImpbSmartMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 2, 1, 1),
    _ImpbSmartMacAddress_Type()
)
impbSmartMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartMacAddress.setStatus("current")
_ImpbSmartPort_Type = Integer32
_ImpbSmartPort_Object = MibTableColumn
impbSmartPort = _ImpbSmartPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 2, 1, 2),
    _ImpbSmartPort_Type()
)
impbSmartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartPort.setStatus("current")


class _ImpbSmartIpAddress_Type(Ipv6Address):
    """Custom type impbSmartIpAddress based on Ipv6Address"""
    defaultHexValue = "00000000"


_ImpbSmartIpAddress_Object = MibTableColumn
impbSmartIpAddress = _ImpbSmartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 2, 1, 3),
    _ImpbSmartIpAddress_Type()
)
impbSmartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbSmartIpAddress.setStatus("current")
_ImpbSmartVlanId_Type = Integer32
_ImpbSmartVlanId_Object = MibTableColumn
impbSmartVlanId = _ImpbSmartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 2, 1, 5),
    _ImpbSmartBinding_Type()
)
impbSmartBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbSmartBinding.setStatus("current")
_ImpbWhiteListTable_Object = MibTable
impbWhiteListTable = _ImpbWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 3)
)
if mibBuilder.loadTexts:
    impbWhiteListTable.setStatus("current")
_ImpbWhiteListEntry_Object = MibTableRow
impbWhiteListEntry = _ImpbWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 3, 1)
)
impbWhiteListEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "impbWhiteListIpAddress"),
    (0, "DGS-1210-20_CX", "impbWhiteListMacAddress"),
)
if mibBuilder.loadTexts:
    impbWhiteListEntry.setStatus("current")


class _ImpbWhiteListIpAddress_Type(DisplayString):
    """Custom type impbWhiteListIpAddress based on DisplayString"""
    defaultHexValue = "00000000"


_ImpbWhiteListIpAddress_Object = MibTableColumn
impbWhiteListIpAddress = _ImpbWhiteListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 3, 1, 1),
    _ImpbWhiteListIpAddress_Type()
)
impbWhiteListIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbWhiteListIpAddress.setStatus("current")
_ImpbWhiteListMacAddress_Type = MacAddress
_ImpbWhiteListMacAddress_Object = MibTableColumn
impbWhiteListMacAddress = _ImpbWhiteListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 3, 1, 2),
    _ImpbWhiteListMacAddress_Type()
)
impbWhiteListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbWhiteListMacAddress.setStatus("current")
_ImpbWhiteListPort_Type = Integer32
_ImpbWhiteListPort_Object = MibTableColumn
impbWhiteListPort = _ImpbWhiteListPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 3, 1, 3),
    _ImpbWhiteListPort_Type()
)
impbWhiteListPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbWhiteListPort.setStatus("current")
_ImpbWhiteListRowStatus_Type = RowStatus
_ImpbWhiteListRowStatus_Object = MibTableColumn
impbWhiteListRowStatus = _ImpbWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 3, 1, 4),
    _ImpbWhiteListRowStatus_Type()
)
impbWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    impbWhiteListRowStatus.setStatus("current")
_ImpbBlackListTable_Object = MibTable
impbBlackListTable = _ImpbBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 4)
)
if mibBuilder.loadTexts:
    impbBlackListTable.setStatus("current")
_ImpbBlackListEntry_Object = MibTableRow
impbBlackListEntry = _ImpbBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 4, 1)
)
impbBlackListEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "impbBlackListMacAddress"),
    (0, "DGS-1210-20_CX", "impbBlackListVlanId"),
    (0, "DGS-1210-20_CX", "impbBlackListPort"),
)
if mibBuilder.loadTexts:
    impbBlackListEntry.setStatus("current")
_ImpbBlackListMacAddress_Type = MacAddress
_ImpbBlackListMacAddress_Object = MibTableColumn
impbBlackListMacAddress = _ImpbBlackListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 4, 1, 1),
    _ImpbBlackListMacAddress_Type()
)
impbBlackListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListMacAddress.setStatus("current")
_ImpbBlackListVlanId_Type = Integer32
_ImpbBlackListVlanId_Object = MibTableColumn
impbBlackListVlanId = _ImpbBlackListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 4, 1, 2),
    _ImpbBlackListVlanId_Type()
)
impbBlackListVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListVlanId.setStatus("current")
_ImpbBlackListPort_Type = Integer32
_ImpbBlackListPort_Object = MibTableColumn
impbBlackListPort = _ImpbBlackListPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 4, 1, 3),
    _ImpbBlackListPort_Type()
)
impbBlackListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impbBlackListPort.setStatus("current")
_ImpbBlackListIpAddress_Type = DisplayString
_ImpbBlackListIpAddress_Object = MibTableColumn
impbBlackListIpAddress = _ImpbBlackListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 4, 1, 5),
    _ImpbBlackListStatus_Type()
)
impbBlackListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbBlackListStatus.setStatus("current")


class _ImpbAutoScanIpAddressFrom_Type(Ipv6Address):
    """Custom type impbAutoScanIpAddressFrom based on Ipv6Address"""
    defaultHexValue = "00000000"


_ImpbAutoScanIpAddressFrom_Object = MibScalar
impbAutoScanIpAddressFrom = _ImpbAutoScanIpAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 5),
    _ImpbAutoScanIpAddressFrom_Type()
)
impbAutoScanIpAddressFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbAutoScanIpAddressFrom.setStatus("current")


class _ImpbAutoScanIpAddressTo_Type(Ipv6Address):
    """Custom type impbAutoScanIpAddressTo based on Ipv6Address"""
    defaultHexValue = "00000000"


_ImpbAutoScanIpAddressTo_Object = MibScalar
impbAutoScanIpAddressTo = _ImpbAutoScanIpAddressTo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 14, 10, 7),
    _ImpbAutoScanStatus_Type()
)
impbAutoScanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impbAutoScanStatus.setStatus("current")
_CompanyACLGroup_ObjectIdentity = ObjectIdentity
companyACLGroup = _CompanyACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15)
)
_AclProfile_ObjectIdentity = ObjectIdentity
aclProfile = _AclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1)
)
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1, 1, 1)
)
aclProfileEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aclProfileNo"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1, 1, 1, 1),
    _AclProfileNo_Type()
)
aclProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileNo.setStatus("current")


class _AclProfileName_Type(SnmpAdminString):
    """Custom type aclProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AclProfileName_Type.__name__ = "SnmpAdminString"
_AclProfileName_Object = MibTableColumn
aclProfileName = _AclProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1, 1, 1, 2),
    _AclProfileName_Type()
)
aclProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileName.setStatus("current")


class _AclProfileType_Type(Integer32):
    """Custom type aclProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3v4", 2),
          ("l3v4Ext", 13),
          ("l3v6", 11))
    )


_AclProfileType_Type.__name__ = "Integer32"
_AclProfileType_Object = MibTableColumn
aclProfileType = _AclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1, 1, 1, 4),
    _AclProfileRuleCount_Type()
)
aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleCount.setStatus("current")
_AclProfileStatus_Type = RowStatus
_AclProfileStatus_Object = MibTableColumn
aclProfileStatus = _AclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 1, 1, 1, 14),
    _AclProfileStatus_Type()
)
aclProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileStatus.setStatus("current")
_AclL2Rule_ObjectIdentity = ObjectIdentity
aclL2Rule = _AclL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2)
)
_AclL2RuleTable_Object = MibTable
aclL2RuleTable = _AclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    aclL2RuleTable.setStatus("current")
_AclL2RuleEntry_Object = MibTableRow
aclL2RuleEntry = _AclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1)
)
aclL2RuleEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aclL2ProfileID"),
    (0, "DGS-1210-20_CX", "aclL2AccessID"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 3),
    _AclL2RuleEtherType_Type()
)
aclL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleEtherType.setStatus("current")
_AclL2RuleDstMacAddr_Type = MacAddress
_AclL2RuleDstMacAddr_Object = MibTableColumn
aclL2RuleDstMacAddr = _AclL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 4),
    _AclL2RuleDstMacAddr_Type()
)
aclL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddr.setStatus("current")
_AclL2RuleSrcMacAddr_Type = MacAddress
_AclL2RuleSrcMacAddr_Object = MibTableColumn
aclL2RuleSrcMacAddr = _AclL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 7),
    _AclL2Rule1pPriority_Type()
)
aclL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2Rule1pPriority.setStatus("current")
_AclL2RuleDstMacAddrMask_Type = MacAddress
_AclL2RuleDstMacAddrMask_Object = MibTableColumn
aclL2RuleDstMacAddrMask = _AclL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 8),
    _AclL2RuleDstMacAddrMask_Type()
)
aclL2RuleDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddrMask.setStatus("current")
_AclL2RuleSrcMacAddrMask_Type = MacAddress
_AclL2RuleSrcMacAddrMask_Object = MibTableColumn
aclL2RuleSrcMacAddrMask = _AclL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 9),
    _AclL2RuleSrcMacAddrMask_Type()
)
aclL2RuleSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddrMask.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 10),
    _AclL2RuleAction_Type()
)
aclL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleAction.setStatus("current")


class _AclL2RulePriority_Type(Integer32):
    """Custom type aclL2RulePriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL2RulePriority_Type.__name__ = "Integer32"
_AclL2RulePriority_Object = MibTableColumn
aclL2RulePriority = _AclL2RulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 12),
    _AclL2RulePriority_Type()
)
aclL2RulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RulePriority.setStatus("current")


class _AclL2RuleReplacePriority_Type(Integer32):
    """Custom type aclL2RuleReplacePriority based on Integer32"""
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


_AclL2RuleReplacePriority_Type.__name__ = "Integer32"
_AclL2RuleReplacePriority_Object = MibTableColumn
aclL2RuleReplacePriority = _AclL2RuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 13),
    _AclL2RuleReplacePriority_Type()
)
aclL2RuleReplacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleReplacePriority.setStatus("current")
_AclL2RuleStatus_Type = RowStatus
_AclL2RuleStatus_Object = MibTableColumn
aclL2RuleStatus = _AclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 2, 1, 1, 99),
    _AclL2RuleStatus_Type()
)
aclL2RuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleStatus.setStatus("current")
_AclL3v4Rule_ObjectIdentity = ObjectIdentity
aclL3v4Rule = _AclL3v4Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3)
)
_AclL3v4RuleTable_Object = MibTable
aclL3v4RuleTable = _AclL3v4RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    aclL3v4RuleTable.setStatus("current")
_AclL3v4RuleEntry_Object = MibTableRow
aclL3v4RuleEntry = _AclL3v4RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1)
)
aclL3v4RuleEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aclL3v4RuleProfileNo"),
    (0, "DGS-1210-20_CX", "aclL3v4RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3v4RuleEntry.setStatus("current")


class _AclL3v4RuleAccessID_Type(Integer32):
    """Custom type aclL3v4RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3v4RuleAccessID_Type.__name__ = "Integer32"
_AclL3v4RuleAccessID_Object = MibTableColumn
aclL3v4RuleAccessID = _AclL3v4RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 1),
    _AclL3v4RuleAccessID_Type()
)
aclL3v4RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4RuleAccessID.setStatus("current")


class _AclL3v4RuleProfileNo_Type(Integer32):
    """Custom type aclL3v4RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3v4RuleProfileNo_Type.__name__ = "Integer32"
_AclL3v4RuleProfileNo_Object = MibTableColumn
aclL3v4RuleProfileNo = _AclL3v4RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 2),
    _AclL3v4RuleProfileNo_Type()
)
aclL3v4RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4RuleProfileNo.setStatus("current")


class _AclL3v4RuleDstIpAddr_Type(IpAddress):
    """Custom type aclL3v4RuleDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4RuleDstIpAddr_Object = MibTableColumn
aclL3v4RuleDstIpAddr = _AclL3v4RuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 3),
    _AclL3v4RuleDstIpAddr_Type()
)
aclL3v4RuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleDstIpAddr.setStatus("current")


class _AclL3v4RuleSrcIpAddr_Type(IpAddress):
    """Custom type aclL3v4RuleSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4RuleSrcIpAddr_Object = MibTableColumn
aclL3v4RuleSrcIpAddr = _AclL3v4RuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 4),
    _AclL3v4RuleSrcIpAddr_Type()
)
aclL3v4RuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleSrcIpAddr.setStatus("current")


class _AclL3v4RuleDstIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4RuleDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4RuleDstIpAddrMask_Object = MibTableColumn
aclL3v4RuleDstIpAddrMask = _AclL3v4RuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 5),
    _AclL3v4RuleDstIpAddrMask_Type()
)
aclL3v4RuleDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleDstIpAddrMask.setStatus("current")


class _AclL3v4RuleSrcIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4RuleSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4RuleSrcIpAddrMask_Object = MibTableColumn
aclL3v4RuleSrcIpAddrMask = _AclL3v4RuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 6),
    _AclL3v4RuleSrcIpAddrMask_Type()
)
aclL3v4RuleSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleSrcIpAddrMask.setStatus("current")


class _AclL3v4RuleAction_Type(Integer32):
    """Custom type aclL3v4RuleAction based on Integer32"""
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


_AclL3v4RuleAction_Type.__name__ = "Integer32"
_AclL3v4RuleAction_Object = MibTableColumn
aclL3v4RuleAction = _AclL3v4RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 7),
    _AclL3v4RuleAction_Type()
)
aclL3v4RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleAction.setStatus("current")


class _AclL3v4RulePriority_Type(Integer32):
    """Custom type aclL3v4RulePriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL3v4RulePriority_Type.__name__ = "Integer32"
_AclL3v4RulePriority_Object = MibTableColumn
aclL3v4RulePriority = _AclL3v4RulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 9),
    _AclL3v4RulePriority_Type()
)
aclL3v4RulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RulePriority.setStatus("current")


class _AclL3v4RuleReplacePriority_Type(Integer32):
    """Custom type aclL3v4RuleReplacePriority based on Integer32"""
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


_AclL3v4RuleReplacePriority_Type.__name__ = "Integer32"
_AclL3v4RuleReplacePriority_Object = MibTableColumn
aclL3v4RuleReplacePriority = _AclL3v4RuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 10),
    _AclL3v4RuleReplacePriority_Type()
)
aclL3v4RuleReplacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleReplacePriority.setStatus("current")
_AclL3v4RuleStatus_Type = RowStatus
_AclL3v4RuleStatus_Object = MibTableColumn
aclL3v4RuleStatus = _AclL3v4RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 3, 1, 1, 99),
    _AclL3v4RuleStatus_Type()
)
aclL3v4RuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4RuleStatus.setStatus("current")
_AclL3v4ExtRule_ObjectIdentity = ObjectIdentity
aclL3v4ExtRule = _AclL3v4ExtRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4)
)
_AclL3v4ExtRuleTable_Object = MibTable
aclL3v4ExtRuleTable = _AclL3v4ExtRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1)
)
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTable.setStatus("current")
_AclL3v4ExtRuleEntry_Object = MibTableRow
aclL3v4ExtRuleEntry = _AclL3v4ExtRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1)
)
aclL3v4ExtRuleEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aclL3v4ExtRuleProfileNo"),
    (0, "DGS-1210-20_CX", "aclL3v4ExtRuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3v4ExtRuleEntry.setStatus("current")


class _AclL3v4ExtRuleAccessID_Type(Integer32):
    """Custom type aclL3v4ExtRuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3v4ExtRuleAccessID_Type.__name__ = "Integer32"
_AclL3v4ExtRuleAccessID_Object = MibTableColumn
aclL3v4ExtRuleAccessID = _AclL3v4ExtRuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 1),
    _AclL3v4ExtRuleAccessID_Type()
)
aclL3v4ExtRuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleAccessID.setStatus("current")


class _AclL3v4ExtRuleProfileNo_Type(Integer32):
    """Custom type aclL3v4ExtRuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3v4ExtRuleProfileNo_Type.__name__ = "Integer32"
_AclL3v4ExtRuleProfileNo_Object = MibTableColumn
aclL3v4ExtRuleProfileNo = _AclL3v4ExtRuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 2),
    _AclL3v4ExtRuleProfileNo_Type()
)
aclL3v4ExtRuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleProfileNo.setStatus("current")


class _AclL3v4ExtRuleProtocol_Type(Integer32):
    """Custom type aclL3v4ExtRuleProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17,
              24)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("none", 0),
          ("protocolid", 24),
          ("tcp", 6),
          ("udp", 17))
    )


_AclL3v4ExtRuleProtocol_Type.__name__ = "Integer32"
_AclL3v4ExtRuleProtocol_Object = MibTableColumn
aclL3v4ExtRuleProtocol = _AclL3v4ExtRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 3),
    _AclL3v4ExtRuleProtocol_Type()
)
aclL3v4ExtRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleProtocol.setStatus("current")


class _AclL3v4ExtRuleICMPMessageType_Type(Integer32):
    """Custom type aclL3v4ExtRuleICMPMessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v4ExtRuleICMPMessageType_Type.__name__ = "Integer32"
_AclL3v4ExtRuleICMPMessageType_Object = MibTableColumn
aclL3v4ExtRuleICMPMessageType = _AclL3v4ExtRuleICMPMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 4),
    _AclL3v4ExtRuleICMPMessageType_Type()
)
aclL3v4ExtRuleICMPMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleICMPMessageType.setStatus("current")


class _AclL3v4ExtRuleICMPMessageCode_Type(Integer32):
    """Custom type aclL3v4ExtRuleICMPMessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v4ExtRuleICMPMessageCode_Type.__name__ = "Integer32"
_AclL3v4ExtRuleICMPMessageCode_Object = MibTableColumn
aclL3v4ExtRuleICMPMessageCode = _AclL3v4ExtRuleICMPMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 5),
    _AclL3v4ExtRuleICMPMessageCode_Type()
)
aclL3v4ExtRuleICMPMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleICMPMessageCode.setStatus("current")


class _AclL3v4ExtRuleDstIpAddr_Type(IpAddress):
    """Custom type aclL3v4ExtRuleDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4ExtRuleDstIpAddr_Object = MibTableColumn
aclL3v4ExtRuleDstIpAddr = _AclL3v4ExtRuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 6),
    _AclL3v4ExtRuleDstIpAddr_Type()
)
aclL3v4ExtRuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleDstIpAddr.setStatus("current")


class _AclL3v4ExtRuleSrcIpAddr_Type(IpAddress):
    """Custom type aclL3v4ExtRuleSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AclL3v4ExtRuleSrcIpAddr_Object = MibTableColumn
aclL3v4ExtRuleSrcIpAddr = _AclL3v4ExtRuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 7),
    _AclL3v4ExtRuleSrcIpAddr_Type()
)
aclL3v4ExtRuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleSrcIpAddr.setStatus("current")


class _AclL3v4ExtRuleDstIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4ExtRuleDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4ExtRuleDstIpAddrMask_Object = MibTableColumn
aclL3v4ExtRuleDstIpAddrMask = _AclL3v4ExtRuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 8),
    _AclL3v4ExtRuleDstIpAddrMask_Type()
)
aclL3v4ExtRuleDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleDstIpAddrMask.setStatus("current")


class _AclL3v4ExtRuleSrcIpAddrMask_Type(IpAddress):
    """Custom type aclL3v4ExtRuleSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_AclL3v4ExtRuleSrcIpAddrMask_Object = MibTableColumn
aclL3v4ExtRuleSrcIpAddrMask = _AclL3v4ExtRuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 9),
    _AclL3v4ExtRuleSrcIpAddrMask_Type()
)
aclL3v4ExtRuleSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleSrcIpAddrMask.setStatus("current")


class _AclL3v4ExtRuleTcpUdpDstPort_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3v4ExtRuleTcpUdpDstPort_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpUdpDstPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpDstPort = _AclL3v4ExtRuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 10),
    _AclL3v4ExtRuleTcpUdpDstPort_Type()
)
aclL3v4ExtRuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpDstPort.setStatus("current")


class _AclL3v4ExtRuleTcpUdpSrcPort_Type(Integer32):
    """Custom type aclL3v4ExtRuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3v4ExtRuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_AclL3v4ExtRuleTcpUdpSrcPort_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpSrcPort = _AclL3v4ExtRuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 11),
    _AclL3v4ExtRuleTcpUdpSrcPort_Type()
)
aclL3v4ExtRuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpSrcPort.setStatus("current")
_AclL3v4ExtRuleTcpUdpDstPortMask_Type = OctetString
_AclL3v4ExtRuleTcpUdpDstPortMask_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpDstPortMask = _AclL3v4ExtRuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 12),
    _AclL3v4ExtRuleTcpUdpDstPortMask_Type()
)
aclL3v4ExtRuleTcpUdpDstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpDstPortMask.setStatus("current")
_AclL3v4ExtRuleTcpUdpSrcPortMask_Type = OctetString
_AclL3v4ExtRuleTcpUdpSrcPortMask_Object = MibTableColumn
aclL3v4ExtRuleTcpUdpSrcPortMask = _AclL3v4ExtRuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 13),
    _AclL3v4ExtRuleTcpUdpSrcPortMask_Type()
)
aclL3v4ExtRuleTcpUdpSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleTcpUdpSrcPortMask.setStatus("current")


class _AclL3v4ExtRuleDscp_Type(Integer32):
    """Custom type aclL3v4ExtRuleDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL3v4ExtRuleDscp_Type.__name__ = "Integer32"
_AclL3v4ExtRuleDscp_Object = MibTableColumn
aclL3v4ExtRuleDscp = _AclL3v4ExtRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 20),
    _AclL3v4ExtRuleDscp_Type()
)
aclL3v4ExtRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleDscp.setStatus("current")


class _AclL3v4ExtRuleToS_Type(Integer32):
    """Custom type aclL3v4ExtRuleToS based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_AclL3v4ExtRuleToS_Type.__name__ = "Integer32"
_AclL3v4ExtRuleToS_Object = MibTableColumn
aclL3v4ExtRuleToS = _AclL3v4ExtRuleToS_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 21),
    _AclL3v4ExtRuleToS_Type()
)
aclL3v4ExtRuleToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleToS.setStatus("current")


class _AclL3v4ExtRuleIgmpType_Type(Integer32):
    """Custom type aclL3v4ExtRuleIgmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v4ExtRuleIgmpType_Type.__name__ = "Integer32"
_AclL3v4ExtRuleIgmpType_Object = MibTableColumn
aclL3v4ExtRuleIgmpType = _AclL3v4ExtRuleIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 22),
    _AclL3v4ExtRuleIgmpType_Type()
)
aclL3v4ExtRuleIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleIgmpType.setStatus("current")
_AclL3v4ExtRuleProtocolId_Type = Integer32
_AclL3v4ExtRuleProtocolId_Object = MibTableColumn
aclL3v4ExtRuleProtocolId = _AclL3v4ExtRuleProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 26),
    _AclL3v4ExtRuleProtocolId_Type()
)
aclL3v4ExtRuleProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleProtocolId.setStatus("current")


class _AclL3v4ExtRuleAction_Type(Integer32):
    """Custom type aclL3v4ExtRuleAction based on Integer32"""
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


_AclL3v4ExtRuleAction_Type.__name__ = "Integer32"
_AclL3v4ExtRuleAction_Object = MibTableColumn
aclL3v4ExtRuleAction = _AclL3v4ExtRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 31),
    _AclL3v4ExtRuleAction_Type()
)
aclL3v4ExtRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleAction.setStatus("current")


class _AclL3v4ExtRulePriority_Type(Integer32):
    """Custom type aclL3v4ExtRulePriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL3v4ExtRulePriority_Type.__name__ = "Integer32"
_AclL3v4ExtRulePriority_Object = MibTableColumn
aclL3v4ExtRulePriority = _AclL3v4ExtRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 33),
    _AclL3v4ExtRulePriority_Type()
)
aclL3v4ExtRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRulePriority.setStatus("current")


class _AclL3v4ExtRuleReplacePriority_Type(Integer32):
    """Custom type aclL3v4ExtRuleReplacePriority based on Integer32"""
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


_AclL3v4ExtRuleReplacePriority_Type.__name__ = "Integer32"
_AclL3v4ExtRuleReplacePriority_Object = MibTableColumn
aclL3v4ExtRuleReplacePriority = _AclL3v4ExtRuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 34),
    _AclL3v4ExtRuleReplacePriority_Type()
)
aclL3v4ExtRuleReplacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleReplacePriority.setStatus("current")
_AclL3v4ExtRuleStatus_Type = RowStatus
_AclL3v4ExtRuleStatus_Object = MibTableColumn
aclL3v4ExtRuleStatus = _AclL3v4ExtRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 4, 1, 1, 99),
    _AclL3v4ExtRuleStatus_Type()
)
aclL3v4ExtRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v4ExtRuleStatus.setStatus("current")
_AclL3v6Rule_ObjectIdentity = ObjectIdentity
aclL3v6Rule = _AclL3v6Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5)
)
_AclL3v6RuleTable_Object = MibTable
aclL3v6RuleTable = _AclL3v6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1)
)
if mibBuilder.loadTexts:
    aclL3v6RuleTable.setStatus("current")
_AclL3v6RuleEntry_Object = MibTableRow
aclL3v6RuleEntry = _AclL3v6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1)
)
aclL3v6RuleEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aclL3v6RuleProfileNo"),
    (0, "DGS-1210-20_CX", "aclL3v6RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3v6RuleEntry.setStatus("current")


class _AclL3v6RuleAccessID_Type(Integer32):
    """Custom type aclL3v6RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclL3v6RuleAccessID_Type.__name__ = "Integer32"
_AclL3v6RuleAccessID_Object = MibTableColumn
aclL3v6RuleAccessID = _AclL3v6RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 1),
    _AclL3v6RuleAccessID_Type()
)
aclL3v6RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6RuleAccessID.setStatus("current")


class _AclL3v6RuleProfileNo_Type(Integer32):
    """Custom type aclL3v6RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AclL3v6RuleProfileNo_Type.__name__ = "Integer32"
_AclL3v6RuleProfileNo_Object = MibTableColumn
aclL3v6RuleProfileNo = _AclL3v6RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 2),
    _AclL3v6RuleProfileNo_Type()
)
aclL3v6RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3v6RuleProfileNo.setStatus("current")


class _AclL3v6RuleTrafficClass_Type(Integer32):
    """Custom type aclL3v6RuleTrafficClass based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v6RuleTrafficClass_Type.__name__ = "Integer32"
_AclL3v6RuleTrafficClass_Object = MibTableColumn
aclL3v6RuleTrafficClass = _AclL3v6RuleTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 3),
    _AclL3v6RuleTrafficClass_Type()
)
aclL3v6RuleTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleTrafficClass.setStatus("current")


class _AclL3v6RuleProtocol_Type(Integer32):
    """Custom type aclL3v6RuleProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("icmpv6", 25),
          ("none", 0),
          ("protocolid", 24),
          ("tcp", 6),
          ("udp", 17))
    )


_AclL3v6RuleProtocol_Type.__name__ = "Integer32"
_AclL3v6RuleProtocol_Object = MibTableColumn
aclL3v6RuleProtocol = _AclL3v6RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 4),
    _AclL3v6RuleProtocol_Type()
)
aclL3v6RuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleProtocol.setStatus("current")
_AclL3v6RuleProtocolId_Type = Integer32
_AclL3v6RuleProtocolId_Object = MibTableColumn
aclL3v6RuleProtocolId = _AclL3v6RuleProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 5),
    _AclL3v6RuleProtocolId_Type()
)
aclL3v6RuleProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleProtocolId.setStatus("current")


class _AclL3v6RuleTcpUdpDstPort_Type(Integer32):
    """Custom type aclL3v6RuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3v6RuleTcpUdpDstPort_Type.__name__ = "Integer32"
_AclL3v6RuleTcpUdpDstPort_Object = MibTableColumn
aclL3v6RuleTcpUdpDstPort = _AclL3v6RuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 6),
    _AclL3v6RuleTcpUdpDstPort_Type()
)
aclL3v6RuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleTcpUdpDstPort.setStatus("current")


class _AclL3v6RuleTcpUdpSrcPort_Type(Integer32):
    """Custom type aclL3v6RuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AclL3v6RuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_AclL3v6RuleTcpUdpSrcPort_Object = MibTableColumn
aclL3v6RuleTcpUdpSrcPort = _AclL3v6RuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 7),
    _AclL3v6RuleTcpUdpSrcPort_Type()
)
aclL3v6RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleTcpUdpSrcPort.setStatus("current")
_AclL3v6RuleTcpUdpDstPortMask_Type = OctetString
_AclL3v6RuleTcpUdpDstPortMask_Object = MibTableColumn
aclL3v6RuleTcpUdpDstPortMask = _AclL3v6RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 8),
    _AclL3v6RuleTcpUdpDstPortMask_Type()
)
aclL3v6RuleTcpUdpDstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleTcpUdpDstPortMask.setStatus("current")
_AclL3v6RuleTcpUdpSrcPortMask_Type = OctetString
_AclL3v6RuleTcpUdpSrcPortMask_Object = MibTableColumn
aclL3v6RuleTcpUdpSrcPortMask = _AclL3v6RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 9),
    _AclL3v6RuleTcpUdpSrcPortMask_Type()
)
aclL3v6RuleTcpUdpSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleTcpUdpSrcPortMask.setStatus("current")


class _AclL3v6RuleICMPv6MessageType_Type(Integer32):
    """Custom type aclL3v6RuleICMPv6MessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v6RuleICMPv6MessageType_Type.__name__ = "Integer32"
_AclL3v6RuleICMPv6MessageType_Object = MibTableColumn
aclL3v6RuleICMPv6MessageType = _AclL3v6RuleICMPv6MessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 10),
    _AclL3v6RuleICMPv6MessageType_Type()
)
aclL3v6RuleICMPv6MessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleICMPv6MessageType.setStatus("current")


class _AclL3v6RuleICMPv6MessageCode_Type(Integer32):
    """Custom type aclL3v6RuleICMPv6MessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclL3v6RuleICMPv6MessageCode_Type.__name__ = "Integer32"
_AclL3v6RuleICMPv6MessageCode_Object = MibTableColumn
aclL3v6RuleICMPv6MessageCode = _AclL3v6RuleICMPv6MessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 11),
    _AclL3v6RuleICMPv6MessageCode_Type()
)
aclL3v6RuleICMPv6MessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleICMPv6MessageCode.setStatus("current")
_AclL3v6RuleDstIpv6Addr_Type = Ipv6Address
_AclL3v6RuleDstIpv6Addr_Object = MibTableColumn
aclL3v6RuleDstIpv6Addr = _AclL3v6RuleDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 12),
    _AclL3v6RuleDstIpv6Addr_Type()
)
aclL3v6RuleDstIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleDstIpv6Addr.setStatus("current")
_AclL3v6RuleSrcIpv6Addr_Type = Ipv6Address
_AclL3v6RuleSrcIpv6Addr_Object = MibTableColumn
aclL3v6RuleSrcIpv6Addr = _AclL3v6RuleSrcIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 13),
    _AclL3v6RuleSrcIpv6Addr_Type()
)
aclL3v6RuleSrcIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleSrcIpv6Addr.setStatus("current")


class _AclL3v6RuleDstIpv6AddrPrefixLen_Type(Integer32):
    """Custom type aclL3v6RuleDstIpv6AddrPrefixLen based on Integer32"""
    defaultValue = 0


_AclL3v6RuleDstIpv6AddrPrefixLen_Object = MibTableColumn
aclL3v6RuleDstIpv6AddrPrefixLen = _AclL3v6RuleDstIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 14),
    _AclL3v6RuleDstIpv6AddrPrefixLen_Type()
)
aclL3v6RuleDstIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleDstIpv6AddrPrefixLen.setStatus("current")


class _AclL3v6RuleSrcIpv6AddrPrefixLen_Type(Integer32):
    """Custom type aclL3v6RuleSrcIpv6AddrPrefixLen based on Integer32"""
    defaultValue = 0


_AclL3v6RuleSrcIpv6AddrPrefixLen_Object = MibTableColumn
aclL3v6RuleSrcIpv6AddrPrefixLen = _AclL3v6RuleSrcIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 15),
    _AclL3v6RuleSrcIpv6AddrPrefixLen_Type()
)
aclL3v6RuleSrcIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleSrcIpv6AddrPrefixLen.setStatus("current")


class _AclL3v6RuleAction_Type(Integer32):
    """Custom type aclL3v6RuleAction based on Integer32"""
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


_AclL3v6RuleAction_Type.__name__ = "Integer32"
_AclL3v6RuleAction_Object = MibTableColumn
aclL3v6RuleAction = _AclL3v6RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 90),
    _AclL3v6RuleAction_Type()
)
aclL3v6RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleAction.setStatus("current")


class _AclL3v6RulePriority_Type(Integer32):
    """Custom type aclL3v6RulePriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL3v6RulePriority_Type.__name__ = "Integer32"
_AclL3v6RulePriority_Object = MibTableColumn
aclL3v6RulePriority = _AclL3v6RulePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 92),
    _AclL3v6RulePriority_Type()
)
aclL3v6RulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RulePriority.setStatus("current")


class _AclL3v6RuleReplacePriority_Type(Integer32):
    """Custom type aclL3v6RuleReplacePriority based on Integer32"""
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


_AclL3v6RuleReplacePriority_Type.__name__ = "Integer32"
_AclL3v6RuleReplacePriority_Object = MibTableColumn
aclL3v6RuleReplacePriority = _AclL3v6RuleReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 93),
    _AclL3v6RuleReplacePriority_Type()
)
aclL3v6RuleReplacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleReplacePriority.setStatus("current")
_AclL3v6RuleStatus_Type = RowStatus
_AclL3v6RuleStatus_Object = MibTableColumn
aclL3v6RuleStatus = _AclL3v6RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 5, 1, 1, 99),
    _AclL3v6RuleStatus_Type()
)
aclL3v6RuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3v6RuleStatus.setStatus("current")
_AclPortBindGroup_ObjectIdentity = ObjectIdentity
aclPortBindGroup = _AclPortBindGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 6)
)
_AclPortGroupTable_Object = MibTable
aclPortGroupTable = _AclPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 6, 1)
)
if mibBuilder.loadTexts:
    aclPortGroupTable.setStatus("current")
_AclPortGroupEntry_Object = MibTableRow
aclPortGroupEntry = _AclPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 6, 1, 1)
)
aclPortGroupEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aclPortIndex"),
)
if mibBuilder.loadTexts:
    aclPortGroupEntry.setStatus("current")


class _AclPortIndex_Type(Integer32):
    """Custom type aclPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclPortIndex_Type.__name__ = "Integer32"
_AclPortIndex_Object = MibTableColumn
aclPortIndex = _AclPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 6, 1, 1, 1),
    _AclPortIndex_Type()
)
aclPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclPortIndex.setStatus("current")


class _AclPortL2ProfileNo_Type(Integer32):
    """Custom type aclPortL2ProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL2ProfileNo_Type.__name__ = "Integer32"
_AclPortL2ProfileNo_Object = MibTableColumn
aclPortL2ProfileNo = _AclPortL2ProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 6, 1, 1, 2),
    _AclPortL2ProfileNo_Type()
)
aclPortL2ProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL2ProfileNo.setStatus("current")


class _AclPortL3v4ProfileNo_Type(Integer32):
    """Custom type aclPortL3v4ProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL3v4ProfileNo_Type.__name__ = "Integer32"
_AclPortL3v4ProfileNo_Object = MibTableColumn
aclPortL3v4ProfileNo = _AclPortL3v4ProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 6, 1, 1, 3),
    _AclPortL3v4ProfileNo_Type()
)
aclPortL3v4ProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL3v4ProfileNo.setStatus("current")


class _AclPortL3v6ProfileNo_Type(Integer32):
    """Custom type aclPortL3v6ProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AclPortL3v6ProfileNo_Type.__name__ = "Integer32"
_AclPortL3v6ProfileNo_Object = MibTableColumn
aclPortL3v6ProfileNo = _AclPortL3v6ProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 6, 1, 1, 4),
    _AclPortL3v6ProfileNo_Type()
)
aclPortL3v6ProfileNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclPortL3v6ProfileNo.setStatus("current")
_AclHWResourceStatus_ObjectIdentity = ObjectIdentity
aclHWResourceStatus = _AclHWResourceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 8)
)
_AclHWResourceStatusTable_Object = MibTable
aclHWResourceStatusTable = _AclHWResourceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 8, 1)
)
if mibBuilder.loadTexts:
    aclHWResourceStatusTable.setStatus("current")
_AclHWResourceStatusEntry_Object = MibTableRow
aclHWResourceStatusEntry = _AclHWResourceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 8, 1, 1)
)
aclHWResourceStatusEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "aclHWProfileIndex"),
)
if mibBuilder.loadTexts:
    aclHWResourceStatusEntry.setStatus("current")


class _AclHWProfileIndex_Type(Integer32):
    """Custom type aclHWProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AclHWProfileIndex_Type.__name__ = "Integer32"
_AclHWProfileIndex_Object = MibTableColumn
aclHWProfileIndex = _AclHWProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 8, 1, 1, 1),
    _AclHWProfileIndex_Type()
)
aclHWProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclHWProfileIndex.setStatus("current")
_AclAccessListNo_Type = DisplayString
_AclAccessListNo_Object = MibTableColumn
aclAccessListNo = _AclAccessListNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 8, 1, 1, 2),
    _AclAccessListNo_Type()
)
aclAccessListNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAccessListNo.setStatus("current")


class _AclResourceEntryCount_Type(Integer32):
    """Custom type aclResourceEntryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AclResourceEntryCount_Type.__name__ = "Integer32"
_AclResourceEntryCount_Object = MibTableColumn
aclResourceEntryCount = _AclResourceEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 15, 8, 1, 1, 3),
    _AclResourceEntryCount_Type()
)
aclResourceEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclResourceEntryCount.setStatus("current")
_CompanySyslog_ObjectIdentity = ObjectIdentity
companySyslog = _CompanySyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16)
)
_SyslogGeneralGroup_ObjectIdentity = ObjectIdentity
syslogGeneralGroup = _SyslogGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 4),
    _SyslogSrvFacility_Type()
)
syslogSrvFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSrvFacility.setStatus("current")
_SyslogSrvTable_Object = MibTable
syslogSrvTable = _SyslogSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 5)
)
if mibBuilder.loadTexts:
    syslogSrvTable.setStatus("current")
_SyslogSrvEntry_Object = MibTableRow
syslogSrvEntry = _SyslogSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 5, 1)
)
syslogSrvEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "syslogSrvIPType"),
    (0, "DGS-1210-20_CX", "syslogSrvIP"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 5, 1, 1),
    _SyslogSrvIPType_Type()
)
syslogSrvIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogSrvIPType.setStatus("current")
_SyslogSrvIP_Type = Ipv6Address
_SyslogSrvIP_Object = MibTableColumn
syslogSrvIP = _SyslogSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 5, 1, 3),
    _SyslogSrvPort_Type()
)
syslogSrvPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogSrvPort.setStatus("current")
_SyslogInterfaceName_Type = OctetString
_SyslogInterfaceName_Object = MibTableColumn
syslogInterfaceName = _SyslogInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 5, 1, 4),
    _SyslogInterfaceName_Type()
)
syslogInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogInterfaceName.setStatus("current")
_SyslogSrvRowStatus_Type = RowStatus
_SyslogSrvRowStatus_Object = MibTableColumn
syslogSrvRowStatus = _SyslogSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 16, 2, 5, 1, 5),
    _SyslogSrvRowStatus_Type()
)
syslogSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogSrvRowStatus.setStatus("current")
_CompanyLBD_ObjectIdentity = ObjectIdentity
companyLBD = _CompanyLBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 4),
    _SysLBDRecoverTime_Type()
)
sysLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDRecoverTime.setStatus("current")
_SysLBDCtrlTable_Object = MibTable
sysLBDCtrlTable = _SysLBDCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 5)
)
if mibBuilder.loadTexts:
    sysLBDCtrlTable.setStatus("current")
_SysLBDCtrlEntry_Object = MibTableRow
sysLBDCtrlEntry = _SysLBDCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 5, 1)
)
sysLBDCtrlEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "sysLBDCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysLBDCtrlEntry.setStatus("current")
_SysLBDCtrlIndex_Type = Integer32
_SysLBDCtrlIndex_Object = MibTableColumn
sysLBDCtrlIndex = _SysLBDCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 5, 1, 3),
    _SysLBDPortLoopStatus_Type()
)
sysLBDPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDPortLoopStatus.setStatus("current")
_SysLBDVlanLoopTable_Object = MibTable
sysLBDVlanLoopTable = _SysLBDVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 6)
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopTable.setStatus("current")
_SysLBDVlanLoopEntry_Object = MibTableRow
sysLBDVlanLoopEntry = _SysLBDVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 6, 1)
)
sysLBDVlanLoopEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "sysLBDVlanLoopIndex"),
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopEntry.setStatus("current")
_SysLBDVlanLoopIndex_Type = Integer32
_SysLBDVlanLoopIndex_Object = MibTableColumn
sysLBDVlanLoopIndex = _SysLBDVlanLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 6, 1, 1),
    _SysLBDVlanLoopIndex_Type()
)
sysLBDVlanLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopIndex.setStatus("current")
_SysLBDVlanLoopPorts_Type = PortList
_SysLBDVlanLoopPorts_Object = MibTableColumn
sysLBDVlanLoopPorts = _SysLBDVlanLoopPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 6, 1, 2),
    _SysLBDVlanLoopPorts_Type()
)
sysLBDVlanLoopPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopPorts.setStatus("current")
_SwLoopDetectEnabledVlanList_Type = DisplayString
_SwLoopDetectEnabledVlanList_Object = MibScalar
swLoopDetectEnabledVlanList = _SwLoopDetectEnabledVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 17, 7),
    _SwLoopDetectEnabledVlanList_Type()
)
swLoopDetectEnabledVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLoopDetectEnabledVlanList.setStatus("current")
_CompanyMirror_ObjectIdentity = ObjectIdentity
companyMirror = _CompanyMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 18)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 18, 1),
    _SysMirrorStatus_Type()
)
sysMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorStatus.setStatus("current")
_SysMirrorTargetPort_Type = Integer32
_SysMirrorTargetPort_Object = MibScalar
sysMirrorTargetPort = _SysMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 18, 2),
    _SysMirrorTargetPort_Type()
)
sysMirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorTargetPort.setStatus("current")
_SysMirrorCtrlIngressMirroring_Type = PortList
_SysMirrorCtrlIngressMirroring_Object = MibScalar
sysMirrorCtrlIngressMirroring = _SysMirrorCtrlIngressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 18, 3),
    _SysMirrorCtrlIngressMirroring_Type()
)
sysMirrorCtrlIngressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlIngressMirroring.setStatus("current")
_SysMirrorCtrlEgressMirroring_Type = PortList
_SysMirrorCtrlEgressMirroring_Object = MibScalar
sysMirrorCtrlEgressMirroring = _SysMirrorCtrlEgressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 18, 4),
    _SysMirrorCtrlEgressMirroring_Type()
)
sysMirrorCtrlEgressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlEgressMirroring.setStatus("current")
_CompanySNTPSetting_ObjectIdentity = ObjectIdentity
companySNTPSetting = _CompanySNTPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20)
)
_SysSNTPServerTable_ObjectIdentity = ObjectIdentity
sysSNTPServerTable = _SysSNTPServerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17)
)
_SysSNTPTimeSeconds_Type = Integer32
_SysSNTPTimeSeconds_Object = MibScalar
sysSNTPTimeSeconds = _SysSNTPTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 1),
    _SysSNTPTimeSeconds_Type()
)
sysSNTPTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPTimeSeconds.setStatus("current")
_SysSNTPFirstServer_Type = Ipv6Address
_SysSNTPFirstServer_Object = MibScalar
sysSNTPFirstServer = _SysSNTPFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 3),
    _SysSNTPFirstType_Type()
)
sysSNTPFirstType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstType.setStatus("current")
_SysSNTPFirstInterfaceName_Type = OctetString
_SysSNTPFirstInterfaceName_Object = MibScalar
sysSNTPFirstInterfaceName = _SysSNTPFirstInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 4),
    _SysSNTPFirstInterfaceName_Type()
)
sysSNTPFirstInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstInterfaceName.setStatus("current")
_SysSNTPSecondServer_Type = Ipv6Address
_SysSNTPSecondServer_Object = MibScalar
sysSNTPSecondServer = _SysSNTPSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 6),
    _SysSNTPSecondType_Type()
)
sysSNTPSecondType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondType.setStatus("current")
_SysSNTPSecondInterfaceName_Type = OctetString
_SysSNTPSecondInterfaceName_Object = MibScalar
sysSNTPSecondInterfaceName = _SysSNTPSecondInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 7),
    _SysSNTPSecondInterfaceName_Type()
)
sysSNTPSecondInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondInterfaceName.setStatus("current")
_SysSNTPPollInterval_Type = Integer32
_SysSNTPPollInterval_Object = MibScalar
sysSNTPPollInterval = _SysSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 10),
    _SysSNTPDSTOffset_Type()
)
sysSNTPDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTOffset.setStatus("current")
_SysSNTPGMTMinutes_Type = Integer32
_SysSNTPGMTMinutes_Object = MibScalar
sysSNTPGMTMinutes = _SysSNTPGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 11),
    _SysSNTPGMTMinutes_Type()
)
sysSNTPGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPGMTMinutes.setStatus("current")
_SysSNTPDSTStartMon_Type = Integer32
_SysSNTPDSTStartMon_Object = MibScalar
sysSNTPDSTStartMon = _SysSNTPDSTStartMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 12),
    _SysSNTPDSTStartMon_Type()
)
sysSNTPDSTStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMon.setStatus("current")
_SysSNTPDSTStartDay_Type = Integer32
_SysSNTPDSTStartDay_Object = MibScalar
sysSNTPDSTStartDay = _SysSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 13),
    _SysSNTPDSTStartDay_Type()
)
sysSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartDay.setStatus("current")
_SysSNTPDSTStartHour_Type = Integer32
_SysSNTPDSTStartHour_Object = MibScalar
sysSNTPDSTStartHour = _SysSNTPDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 14),
    _SysSNTPDSTStartHour_Type()
)
sysSNTPDSTStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartHour.setStatus("current")
_SysSNTPDSTStartMin_Type = Integer32
_SysSNTPDSTStartMin_Object = MibScalar
sysSNTPDSTStartMin = _SysSNTPDSTStartMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 15),
    _SysSNTPDSTStartMin_Type()
)
sysSNTPDSTStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMin.setStatus("current")
_SysSNTPDSTEndMon_Type = Integer32
_SysSNTPDSTEndMon_Object = MibScalar
sysSNTPDSTEndMon = _SysSNTPDSTEndMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 16),
    _SysSNTPDSTEndMon_Type()
)
sysSNTPDSTEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndMon.setStatus("current")
_SysSNTPDSTEndDay_Type = Integer32
_SysSNTPDSTEndDay_Object = MibScalar
sysSNTPDSTEndDay = _SysSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 17),
    _SysSNTPDSTEndDay_Type()
)
sysSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndDay.setStatus("current")
_SysSNTPDSTEndHour_Type = Integer32
_SysSNTPDSTEndHour_Object = MibScalar
sysSNTPDSTEndHour = _SysSNTPDSTEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 18),
    _SysSNTPDSTEndHour_Type()
)
sysSNTPDSTEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndHour.setStatus("current")
_SysSNTPDSTEndMin_Type = Integer32
_SysSNTPDSTEndMin_Object = MibScalar
sysSNTPDSTEndMin = _SysSNTPDSTEndMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 20, 17, 20),
    _SysSNTPDSTState_Type()
)
sysSNTPDSTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTState.setStatus("current")
_CompanyVoiceVlan_ObjectIdentity = ObjectIdentity
companyVoiceVlan = _CompanyVoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21)
)
_VoicevlanSystem_ObjectIdentity = ObjectIdentity
voicevlanSystem = _VoicevlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 2),
    _VoiceVlanMode_Type()
)
voiceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanMode.setStatus("current")
_VoiceVlanId_Type = Integer32
_VoiceVlanId_Object = MibScalar
voiceVlanId = _VoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 3),
    _VoiceVlanId_Type()
)
voiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanId.setStatus("current")
_VoiceVlanTimeout_Type = Integer32
_VoiceVlanTimeout_Object = MibScalar
voiceVlanTimeout = _VoiceVlanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 4),
    _VoiceVlanTimeout_Type()
)
voiceVlanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanTimeout.setStatus("current")


class _VoiceVlanPriority_Type(Integer32):
    """Custom type voiceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VoiceVlanPriority_Type.__name__ = "Integer32"
_VoiceVlanPriority_Object = MibScalar
voiceVlanPriority = _VoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 5),
    _VoiceVlanPriority_Type()
)
voiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPriority.setStatus("current")
_VoicevlanPortControlTable_Object = MibTable
voicevlanPortControlTable = _VoicevlanPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 6)
)
if mibBuilder.loadTexts:
    voicevlanPortControlTable.setStatus("current")
_VoicevlanPortControlEntry_Object = MibTableRow
voicevlanPortControlEntry = _VoicevlanPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 6, 1)
)
voicevlanPortControlEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "voicevlanPortControlIndex"),
)
if mibBuilder.loadTexts:
    voicevlanPortControlEntry.setStatus("current")
_VoicevlanPortControlIndex_Type = InterfaceIndex
_VoicevlanPortControlIndex_Object = MibTableColumn
voicevlanPortControlIndex = _VoicevlanPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 1, 6, 1, 5),
    _VoicevlanPortState_Type()
)
voicevlanPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanPortState.setStatus("current")
_VoicevlanOUI_ObjectIdentity = ObjectIdentity
voicevlanOUI = _VoicevlanOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 2)
)
_VoicevlanOUITable_Object = MibTable
voicevlanOUITable = _VoicevlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    voicevlanOUITable.setStatus("current")
_VoicevlanOUIEntry_Object = MibTableRow
voicevlanOUIEntry = _VoicevlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 2, 1, 1)
)
voicevlanOUIEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "voicevlanOUITelephonyOUI"),
)
if mibBuilder.loadTexts:
    voicevlanOUIEntry.setStatus("current")
_VoicevlanOUITelephonyOUI_Type = MacAddress
_VoicevlanOUITelephonyOUI_Object = MibTableColumn
voicevlanOUITelephonyOUI = _VoicevlanOUITelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 2, 1, 1, 1),
    _VoicevlanOUITelephonyOUI_Type()
)
voicevlanOUITelephonyOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUITelephonyOUI.setStatus("current")
_VoicevlanOUIDescription_Type = OctetString
_VoicevlanOUIDescription_Object = MibTableColumn
voicevlanOUIDescription = _VoicevlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 2, 1, 1, 2),
    _VoicevlanOUIDescription_Type()
)
voicevlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanOUIDescription.setStatus("current")
_VoicevlanOUIMask_Type = MacAddress
_VoicevlanOUIMask_Object = MibTableColumn
voicevlanOUIMask = _VoicevlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 2, 1, 1, 3),
    _VoicevlanOUIMask_Type()
)
voicevlanOUIMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanOUIMask.setStatus("current")
_VoicevlanOUIStatus_Type = RowStatus
_VoicevlanOUIStatus_Object = MibTableColumn
voicevlanOUIStatus = _VoicevlanOUIStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 2, 1, 1, 4),
    _VoicevlanOUIStatus_Type()
)
voicevlanOUIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanOUIStatus.setStatus("current")
_VoicevlanDevice_ObjectIdentity = ObjectIdentity
voicevlanDevice = _VoicevlanDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3)
)
_VoicevlanDeviceTable_Object = MibTable
voicevlanDeviceTable = _VoicevlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3, 1)
)
if mibBuilder.loadTexts:
    voicevlanDeviceTable.setStatus("current")
_VoicevlanDeviceEntry_Object = MibTableRow
voicevlanDeviceEntry = _VoicevlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3, 1, 1)
)
voicevlanDeviceEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "voicevlanDeviceIndexMac"),
)
if mibBuilder.loadTexts:
    voicevlanDeviceEntry.setStatus("current")
_VoicevlanDeviceIndexMac_Type = MacAddress
_VoicevlanDeviceIndexMac_Object = MibTableColumn
voicevlanDeviceIndexMac = _VoicevlanDeviceIndexMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3, 1, 1, 1),
    _VoicevlanDeviceIndexMac_Type()
)
voicevlanDeviceIndexMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDeviceIndexMac.setStatus("current")
_VoicevlanDevicePort_Type = Integer32
_VoicevlanDevicePort_Object = MibTableColumn
voicevlanDevicePort = _VoicevlanDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3, 1, 1, 2),
    _VoicevlanDevicePort_Type()
)
voicevlanDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicevlanDevicePort.setStatus("current")
_VoicevlanDevicePriority_Type = Integer32
_VoicevlanDevicePriority_Object = MibTableColumn
voicevlanDevicePriority = _VoicevlanDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 21, 3, 1, 1, 5),
    _VoicevlanDeviceStatus_Type()
)
voicevlanDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicevlanDeviceStatus.setStatus("current")
_CompanyAuthGroup_ObjectIdentity = ObjectIdentity
companyAuthGroup = _CompanyAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23)
)
_SwAuthenCtrl_ObjectIdentity = ObjectIdentity
swAuthenCtrl = _SwAuthenCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 1, 4),
    _SwAuthCtrlPktFwdMode_Type()
)
swAuthCtrlPktFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthCtrlPktFwdMode.setStatus("current")
_SwAuthPortAccessCtrl_ObjectIdentity = ObjectIdentity
swAuthPortAccessCtrl = _SwAuthPortAccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2)
)
_SwAuthPortAccessControlTable_Object = MibTable
swAuthPortAccessControlTable = _SwAuthPortAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlTable.setStatus("current")
_SwAuthPortAccessControlEntry_Object = MibTableRow
swAuthPortAccessControlEntry = _SwAuthPortAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1)
)
swAuthPortAccessControlEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "swAuthAuthConfigPortNumber"),
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlEntry.setStatus("current")
_SwAuthAuthConfigPortNumber_Type = Integer32
_SwAuthAuthConfigPortNumber_Object = MibTableColumn
swAuthAuthConfigPortNumber = _SwAuthAuthConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 2, 1, 1, 11),
    _SwAuthAuthDirection_Type()
)
swAuthAuthDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthDirection.setStatus("current")
_SwAuthUser_ObjectIdentity = ObjectIdentity
swAuthUser = _SwAuthUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 3)
)
_SwAuthUserTable_Object = MibTable
swAuthUserTable = _SwAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 3, 1)
)
if mibBuilder.loadTexts:
    swAuthUserTable.setStatus("current")
_SwAuthUserEntry_Object = MibTableRow
swAuthUserEntry = _SwAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 3, 1, 1)
)
swAuthUserEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "swAuthUserName"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 3, 1, 1, 2),
    _SwAuthUserPassword_Type()
)
swAuthUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthUserPassword.setStatus("current")
_SwAuthUserStatus_Type = RowStatus
_SwAuthUserStatus_Object = MibTableColumn
swAuthUserStatus = _SwAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 3, 1, 1, 3),
    _SwAuthUserStatus_Type()
)
swAuthUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthUserStatus.setStatus("current")
_SwAuthRadiusServer_ObjectIdentity = ObjectIdentity
swAuthRadiusServer = _SwAuthRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4)
)
_SwAuthRadiusServerTable_Object = MibTable
swAuthRadiusServerTable = _SwAuthRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2)
)
if mibBuilder.loadTexts:
    swAuthRadiusServerTable.setStatus("current")
_SwAuthRadiusServerEntry_Object = MibTableRow
swAuthRadiusServerEntry = _SwAuthRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1)
)
swAuthRadiusServerEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "swAuthRadiusServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 1),
    _SwAuthRadiusServerIndex_Type()
)
swAuthRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthRadiusServerIndex.setStatus("current")


class _SwAuthRadiusIPType_Type(Integer32):
    """Custom type swAuthRadiusIPType based on Integer32"""
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


_SwAuthRadiusIPType_Type.__name__ = "Integer32"
_SwAuthRadiusIPType_Object = MibTableColumn
swAuthRadiusIPType = _SwAuthRadiusIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 2),
    _SwAuthRadiusIPType_Type()
)
swAuthRadiusIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusIPType.setStatus("current")
_SwAuthRadiusServerAddress_Type = Ipv6Address
_SwAuthRadiusServerAddress_Object = MibTableColumn
swAuthRadiusServerAddress = _SwAuthRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 3),
    _SwAuthRadiusServerAddress_Type()
)
swAuthRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerAddress.setStatus("current")
_SwAuthRadiusServerInterfaceName_Type = OctetString
_SwAuthRadiusServerInterfaceName_Object = MibTableColumn
swAuthRadiusServerInterfaceName = _SwAuthRadiusServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 4),
    _SwAuthRadiusServerInterfaceName_Type()
)
swAuthRadiusServerInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthRadiusServerInterfaceName.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 9),
    _SwAuthRadiusServerKey_Type()
)
swAuthRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerKey.setStatus("current")
_SwAuthRadiusServerStatus_Type = RowStatus
_SwAuthRadiusServerStatus_Object = MibTableColumn
swAuthRadiusServerStatus = _SwAuthRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 23, 4, 2, 1, 10),
    _SwAuthRadiusServerStatus_Type()
)
swAuthRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthRadiusServerStatus.setStatus("current")
_CompanyLLDPSetting_ObjectIdentity = ObjectIdentity
companyLLDPSetting = _CompanyLLDPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 5),
    _DlinklldpTxDelay_Type()
)
dlinklldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpTxDelay.setStatus("current")
_DlinklldpConfigManAddrTable_Object = MibTable
dlinklldpConfigManAddrTable = _DlinklldpConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 7)
)
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrTable.setStatus("current")
_DlinklldpConfigManAddrEntry_Object = MibTableRow
dlinklldpConfigManAddrEntry = _DlinklldpConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 7, 1)
)
dlinklldpConfigManAddrEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dlinklldpLocManAddrSubtype"),
    (0, "DGS-1210-20_CX", "dlinklldpLocManAddr"),
)
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrEntry.setStatus("current")
_DlinklldpLocManAddrSubtype_Type = AddressFamilyNumbers
_DlinklldpLocManAddrSubtype_Object = MibTableColumn
dlinklldpLocManAddrSubtype = _DlinklldpLocManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 7, 1, 1),
    _DlinklldpLocManAddrSubtype_Type()
)
dlinklldpLocManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlinklldpLocManAddrSubtype.setStatus("current")
_DlinklldpLocManAddr_Type = LldpManAddress
_DlinklldpLocManAddr_Object = MibTableColumn
dlinklldpLocManAddr = _DlinklldpLocManAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 24, 7, 1, 3),
    _DlinklldpConfigManAddrPortsTxEnable_Type()
)
dlinklldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrPortsTxEnable.setStatus("current")
_CompanySNMPV3_ObjectIdentity = ObjectIdentity
companySNMPV3 = _CompanySNMPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 1),
    _SnmpGlobalState_Type()
)
snmpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGlobalState.setStatus("current")
_SnmpV3User_ObjectIdentity = ObjectIdentity
snmpV3User = _SnmpV3User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2)
)
_SnmpV3UserTable_Object = MibTable
snmpV3UserTable = _SnmpV3UserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1)
)
if mibBuilder.loadTexts:
    snmpV3UserTable.setStatus("current")
_SnmpV3UserEntry_Object = MibTableRow
snmpV3UserEntry = _SnmpV3UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1)
)
snmpV3UserEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "snmpV3UserName"),
    (0, "DGS-1210-20_CX", "snmpV3UserVersion"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 7),
    _SnmpV3UserPrivProtocolPassword_Type()
)
snmpV3UserPrivProtocolPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserPrivProtocolPassword.setStatus("current")
_SnmpV3UserStatus_Type = RowStatus
_SnmpV3UserStatus_Object = MibTableColumn
snmpV3UserStatus = _SnmpV3UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 2, 1, 1, 8),
    _SnmpV3UserStatus_Type()
)
snmpV3UserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserStatus.setStatus("current")
_SnmpV3Group_ObjectIdentity = ObjectIdentity
snmpV3Group = _SnmpV3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3)
)
_SnmpV3GroupTable_Object = MibTable
snmpV3GroupTable = _SnmpV3GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1)
)
if mibBuilder.loadTexts:
    snmpV3GroupTable.setStatus("current")
_SnmpV3GroupEntry_Object = MibTableRow
snmpV3GroupEntry = _SnmpV3GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1)
)
snmpV3GroupEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "snmpV3GroupName"),
    (0, "DGS-1210-20_CX", "snmpV3GroupSecurityModel"),
    (0, "DGS-1210-20_CX", "snmpV3GroupSecurityLevel"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1, 2),
    _SnmpV3GroupSecurityModel_Type()
)
snmpV3GroupSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3GroupSecurityModel.setStatus("current")
_SnmpV3GroupSecurityLevel_Type = SnmpSecurityLevel
_SnmpV3GroupSecurityLevel_Object = MibTableColumn
snmpV3GroupSecurityLevel = _SnmpV3GroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1, 6),
    _SnmpV3GroupNotifyViewName_Type()
)
snmpV3GroupNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupNotifyViewName.setStatus("current")
_SnmpV3GroupStatus_Type = RowStatus
_SnmpV3GroupStatus_Object = MibTableColumn
snmpV3GroupStatus = _SnmpV3GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 3, 1, 1, 7),
    _SnmpV3GroupStatus_Type()
)
snmpV3GroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupStatus.setStatus("current")
_SnmpV3ViewTree_ObjectIdentity = ObjectIdentity
snmpV3ViewTree = _SnmpV3ViewTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4)
)
_SnmpV3ViewTreeTable_Object = MibTable
snmpV3ViewTreeTable = _SnmpV3ViewTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4, 1)
)
if mibBuilder.loadTexts:
    snmpV3ViewTreeTable.setStatus("current")
_SnmpV3ViewTreeEntry_Object = MibTableRow
snmpV3ViewTreeEntry = _SnmpV3ViewTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4, 1, 1)
)
snmpV3ViewTreeEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "snmpV3viewTreeName"),
    (0, "DGS-1210-20_CX", "snmpV3viewTreeSubtree"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4, 1, 1, 1),
    _SnmpV3viewTreeName_Type()
)
snmpV3viewTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3viewTreeName.setStatus("current")
_SnmpV3viewTreeSubtree_Type = ObjectIdentifier
_SnmpV3viewTreeSubtree_Object = MibTableColumn
snmpV3viewTreeSubtree = _SnmpV3viewTreeSubtree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4, 1, 1, 4),
    _SnmpV3viewTreeType_Type()
)
snmpV3viewTreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeType.setStatus("current")
_SnmpV3viewTreeStatus_Type = RowStatus
_SnmpV3viewTreeStatus_Object = MibTableColumn
snmpV3viewTreeStatus = _SnmpV3viewTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 4, 1, 1, 5),
    _SnmpV3viewTreeStatus_Type()
)
snmpV3viewTreeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeStatus.setStatus("current")
_SnmpV3Community_ObjectIdentity = ObjectIdentity
snmpV3Community = _SnmpV3Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 5)
)
_SnmpV3CommunityTable_Object = MibTable
snmpV3CommunityTable = _SnmpV3CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 5, 1)
)
if mibBuilder.loadTexts:
    snmpV3CommunityTable.setStatus("current")
_SnmpV3CommunityEntry_Object = MibTableRow
snmpV3CommunityEntry = _SnmpV3CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 5, 1, 1)
)
snmpV3CommunityEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "snmpV3CommunityName"),
)
if mibBuilder.loadTexts:
    snmpV3CommunityEntry.setStatus("current")
_SnmpV3CommunityName_Type = OctetString
_SnmpV3CommunityName_Object = MibTableColumn
snmpV3CommunityName = _SnmpV3CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 5, 1, 1, 2),
    _SnmpV3CommunityPolicy_Type()
)
snmpV3CommunityPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityPolicy.setStatus("current")
_SnmpV3CommunityStatus_Type = RowStatus
_SnmpV3CommunityStatus_Object = MibTableColumn
snmpV3CommunityStatus = _SnmpV3CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 5, 1, 1, 3),
    _SnmpV3CommunityStatus_Type()
)
snmpV3CommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityStatus.setStatus("current")
_SnmpV3Host_ObjectIdentity = ObjectIdentity
snmpV3Host = _SnmpV3Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6)
)
_SnmpV3HostTable_Object = MibTable
snmpV3HostTable = _SnmpV3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2)
)
if mibBuilder.loadTexts:
    snmpV3HostTable.setStatus("current")
_SnmpV3HostEntry_Object = MibTableRow
snmpV3HostEntry = _SnmpV3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2, 1)
)
snmpV3HostEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "snmpV3HostAddress"),
    (0, "DGS-1210-20_CX", "snmpV3IPType"),
)
if mibBuilder.loadTexts:
    snmpV3HostEntry.setStatus("current")
_SnmpV3HostAddress_Type = Ipv6Address
_SnmpV3HostAddress_Object = MibTableColumn
snmpV3HostAddress = _SnmpV3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2, 1, 4),
    _SnmpV3HostVersion_Type()
)
snmpV3HostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostVersion.setStatus("current")
_SnmpV3HostInterfaceName_Type = OctetString
_SnmpV3HostInterfaceName_Object = MibTableColumn
snmpV3HostInterfaceName = _SnmpV3HostInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2, 1, 5),
    _SnmpV3HostInterfaceName_Type()
)
snmpV3HostInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostInterfaceName.setStatus("current")
_SnmpV3HostStatus_Type = RowStatus
_SnmpV3HostStatus_Object = MibTableColumn
snmpV3HostStatus = _SnmpV3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 6, 2, 1, 6),
    _SnmpV3HostStatus_Type()
)
snmpV3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostStatus.setStatus("current")
_SnmpV3EngineID_Type = SnmpEngineID
_SnmpV3EngineID_Object = MibScalar
snmpV3EngineID = _SnmpV3EngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 7),
    _SnmpV3EngineID_Type()
)
snmpV3EngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3EngineID.setStatus("current")
_SnmpV3Trap_ObjectIdentity = ObjectIdentity
snmpV3Trap = _SnmpV3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 8)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 8, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 8, 5),
    _SnmpV3TrapFirmUpgrade_Type()
)
snmpV3TrapFirmUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapFirmUpgrade.setStatus("current")


class _SnmpV3TrapLBD_Type(Integer32):
    """Custom type snmpV3TrapLBD based on Integer32"""
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


_SnmpV3TrapLBD_Type.__name__ = "Integer32"
_SnmpV3TrapLBD_Object = MibScalar
snmpV3TrapLBD = _SnmpV3TrapLBD_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 25, 8, 11),
    _SnmpV3TrapLBD_Type()
)
snmpV3TrapLBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapLBD.setStatus("current")
_CompanyAutoSurveillanceVlan_ObjectIdentity = ObjectIdentity
companyAutoSurveillanceVlan = _CompanyAutoSurveillanceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26)
)
_AutoSurveillanceVlanSystem_ObjectIdentity = ObjectIdentity
autoSurveillanceVlanSystem = _AutoSurveillanceVlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 1, 1),
    _AutoSurveillanceVlanMode_Type()
)
autoSurveillanceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanMode.setStatus("current")
_AutoSurveillanceVlanId_Type = Integer32
_AutoSurveillanceVlanId_Object = MibScalar
autoSurveillanceVlanId = _AutoSurveillanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 1, 2),
    _AutoSurveillanceVlanId_Type()
)
autoSurveillanceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanId.setStatus("current")


class _AutoSurveillanceVlanPriority_Type(Integer32):
    """Custom type autoSurveillanceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AutoSurveillanceVlanPriority_Type.__name__ = "Integer32"
_AutoSurveillanceVlanPriority_Object = MibScalar
autoSurveillanceVlanPriority = _AutoSurveillanceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 1, 3),
    _AutoSurveillanceVlanPriority_Type()
)
autoSurveillanceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanPriority.setStatus("current")
_AutoSurveillanceVlanTaggedUplinkDownlinkPort_Type = PortList
_AutoSurveillanceVlanTaggedUplinkDownlinkPort_Object = MibScalar
autoSurveillanceVlanTaggedUplinkDownlinkPort = _AutoSurveillanceVlanTaggedUplinkDownlinkPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 1, 4),
    _AutoSurveillanceVlanTaggedUplinkDownlinkPort_Type()
)
autoSurveillanceVlanTaggedUplinkDownlinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanTaggedUplinkDownlinkPort.setStatus("current")
_AutoSurveillanceVlanOUI_ObjectIdentity = ObjectIdentity
autoSurveillanceVlanOUI = _AutoSurveillanceVlanOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2)
)
_AutoSurveillanceVlanOUITable_Object = MibTable
autoSurveillanceVlanOUITable = _AutoSurveillanceVlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2, 1)
)
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUITable.setStatus("current")
_AutoSurveillanceVlanOUIEntry_Object = MibTableRow
autoSurveillanceVlanOUIEntry = _AutoSurveillanceVlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2, 1, 1)
)
autoSurveillanceVlanOUIEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "autoSurveillanceVlanOUISurveillanceOUI"),
)
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIEntry.setStatus("current")
_AutoSurveillanceVlanOUISurveillanceOUI_Type = MacAddress
_AutoSurveillanceVlanOUISurveillanceOUI_Object = MibTableColumn
autoSurveillanceVlanOUISurveillanceOUI = _AutoSurveillanceVlanOUISurveillanceOUI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2, 1, 1, 1),
    _AutoSurveillanceVlanOUISurveillanceOUI_Type()
)
autoSurveillanceVlanOUISurveillanceOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUISurveillanceOUI.setStatus("current")
_AutoSurveillanceVlanOUIDescription_Type = OctetString
_AutoSurveillanceVlanOUIDescription_Object = MibTableColumn
autoSurveillanceVlanOUIDescription = _AutoSurveillanceVlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2, 1, 1, 2),
    _AutoSurveillanceVlanOUIDescription_Type()
)
autoSurveillanceVlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIDescription.setStatus("current")
_AutoSurveillanceVlanOUIMask_Type = MacAddress
_AutoSurveillanceVlanOUIMask_Object = MibTableColumn
autoSurveillanceVlanOUIMask = _AutoSurveillanceVlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2, 1, 1, 4),
    _AutoSurveillanceVlanOUIComponentType_Type()
)
autoSurveillanceVlanOUIComponentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIComponentType.setStatus("current")
_AutoSurveillanceVlanOUIStatus_Type = RowStatus
_AutoSurveillanceVlanOUIStatus_Object = MibTableColumn
autoSurveillanceVlanOUIStatus = _AutoSurveillanceVlanOUIStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 26, 2, 1, 1, 5),
    _AutoSurveillanceVlanOUIStatus_Type()
)
autoSurveillanceVlanOUIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSurveillanceVlanOUIStatus.setStatus("current")
_CompanyTraps_ObjectIdentity = ObjectIdentity
companyTraps = _CompanyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27, 0)
)
_CompanyGreenSetting_ObjectIdentity = ObjectIdentity
companyGreenSetting = _CompanyGreenSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31)
)
_DlinkGreenLEDShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenLEDShutoff = _DlinkGreenLEDShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 1)
)
_DlinkGreenLEDShutoffPortList_Type = PortList
_DlinkGreenLEDShutoffPortList_Object = MibScalar
dlinkGreenLEDShutoffPortList = _DlinkGreenLEDShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 1, 4),
    _DlinkGreenLEDShutoffTimeProfile2_Type()
)
dlinkGreenLEDShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffTimeProfile2.setStatus("current")
_DlinkGreenPortShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenPortShutoff = _DlinkGreenPortShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 2)
)
_DlinkGreenPortShutoffPortList_Type = PortList
_DlinkGreenPortShutoffPortList_Object = MibScalar
dlinkGreenPortShutoffPortList = _DlinkGreenPortShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 2, 4),
    _DlinkGreenPortShutoffTimeProfile2_Type()
)
dlinkGreenPortShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffTimeProfile2.setStatus("current")
_DlinkGreenSystemHibernation_ObjectIdentity = ObjectIdentity
dlinkGreenSystemHibernation = _DlinkGreenSystemHibernation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 4, 3),
    _DlinkGreenSystemHibernationTimeProfile2_Type()
)
dlinkGreenSystemHibernationTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenSystemHibernationTimeProfile2.setStatus("current")


class _DlinkPowerSavingGlobalSetting_Type(Integer32):
    """Custom type dlinkPowerSavingGlobalSetting based on Integer32"""
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


_DlinkPowerSavingGlobalSetting_Type.__name__ = "Integer32"
_DlinkPowerSavingGlobalSetting_Object = MibScalar
dlinkPowerSavingGlobalSetting = _DlinkPowerSavingGlobalSetting_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 31, 6),
    _DlinkPowerSavingGlobalSetting_Type()
)
dlinkPowerSavingGlobalSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkPowerSavingGlobalSetting.setStatus("current")
_CompanyTimeRangeMgmt_ObjectIdentity = ObjectIdentity
companyTimeRangeMgmt = _CompanyTimeRangeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32)
)
_SwTimeRangeSettingTable_Object = MibTable
swTimeRangeSettingTable = _SwTimeRangeSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1)
)
if mibBuilder.loadTexts:
    swTimeRangeSettingTable.setStatus("current")
_SwTimeRangeSettingEntry_Object = MibTableRow
swTimeRangeSettingEntry = _SwTimeRangeSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1)
)
swTimeRangeSettingEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "swTimeRangeIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 20),
    _SwTimeRangeSunday_Type()
)
swTimeRangeSunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeSunday.setStatus("current")
_SwTimeRangeRowStatus_Type = RowStatus
_SwTimeRangeRowStatus_Object = MibTableColumn
swTimeRangeRowStatus = _SwTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 32, 1, 1, 21),
    _SwTimeRangeRowStatus_Type()
)
swTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeRowStatus.setStatus("current")
_CompanyStaticMcast_ObjectIdentity = ObjectIdentity
companyStaticMcast = _CompanyStaticMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 35)
)
_StaticMcastTable_Object = MibTable
staticMcastTable = _StaticMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 35, 1)
)
if mibBuilder.loadTexts:
    staticMcastTable.setStatus("current")
_StaticMcastEntry_Object = MibTableRow
staticMcastEntry = _StaticMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 35, 1, 1)
)
staticMcastEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "staticMcastVlanID"),
    (0, "DGS-1210-20_CX", "staticMcastMac"),
    (0, "DGS-1210-20_CX", "staticMcastEgressPorts"),
)
if mibBuilder.loadTexts:
    staticMcastEntry.setStatus("current")
_StaticMcastVlanID_Type = Integer32
_StaticMcastVlanID_Object = MibTableColumn
staticMcastVlanID = _StaticMcastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 35, 1, 1, 1),
    _StaticMcastVlanID_Type()
)
staticMcastVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastVlanID.setStatus("current")
_StaticMcastMac_Type = MacAddress
_StaticMcastMac_Object = MibTableColumn
staticMcastMac = _StaticMcastMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 35, 1, 1, 2),
    _StaticMcastMac_Type()
)
staticMcastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastMac.setStatus("current")
_StaticMcastEgressPorts_Type = PortList
_StaticMcastEgressPorts_Object = MibTableColumn
staticMcastEgressPorts = _StaticMcastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 35, 1, 1, 3),
    _StaticMcastEgressPorts_Type()
)
staticMcastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastEgressPorts.setStatus("current")
_StaticMcastStatus_Type = RowStatus
_StaticMcastStatus_Object = MibTableColumn
staticMcastStatus = _StaticMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 35, 1, 1, 4),
    _StaticMcastStatus_Type()
)
staticMcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMcastStatus.setStatus("current")
_CompanyCableDiagnostic_ObjectIdentity = ObjectIdentity
companyCableDiagnostic = _CompanyCableDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37)
)
_CableDiagTriggerIndex_Type = Integer32
_CableDiagTriggerIndex_Object = MibScalar
cableDiagTriggerIndex = _CableDiagTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 2),
    _CableDiagPair1TestResult_Type()
)
cableDiagPair1TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1TestResult.setStatus("current")
_CableDiagPair1FaultDistance_Type = Integer32
_CableDiagPair1FaultDistance_Object = MibScalar
cableDiagPair1FaultDistance = _CableDiagPair1FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 4),
    _CableDiagPair2TestResult_Type()
)
cableDiagPair2TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2TestResult.setStatus("current")
_CableDiagPair2FaultDistance_Type = Integer32
_CableDiagPair2FaultDistance_Object = MibScalar
cableDiagPair2FaultDistance = _CableDiagPair2FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 6),
    _CableDiagPair3TestResult_Type()
)
cableDiagPair3TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3TestResult.setStatus("current")
_CableDiagPair3FaultDistance_Type = Integer32
_CableDiagPair3FaultDistance_Object = MibScalar
cableDiagPair3FaultDistance = _CableDiagPair3FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 8),
    _CableDiagPair4TestResult_Type()
)
cableDiagPair4TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4TestResult.setStatus("current")
_CableDiagPair4FaultDistance_Type = Integer32
_CableDiagPair4FaultDistance_Object = MibScalar
cableDiagPair4FaultDistance = _CableDiagPair4FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 37, 10),
    _CableDiagLengthinRange_Type()
)
cableDiagLengthinRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagLengthinRange.setStatus("current")
_CompanyRMON_ObjectIdentity = ObjectIdentity
companyRMON = _CompanyRMON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 1),
    _RmonGlobalState_Type()
)
rmonGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonGlobalState.setStatus("current")
_RmonStatistics_ObjectIdentity = ObjectIdentity
rmonStatistics = _RmonStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 2)
)
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 2, 1)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 2, 1, 1)
)
rmonStatsEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "rmonStatsIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 2, 1, 1, 1),
    _RmonStatsIndex_Type()
)
rmonStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsIndex.setStatus("current")
_RmonStatsDataSource_Type = ObjectIdentifier
_RmonStatsDataSource_Object = MibTableColumn
rmonStatsDataSource = _RmonStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 2, 1, 1, 3),
    _RmonStatsOwner_Type()
)
rmonStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsOwner.setStatus("current")
_RmonStatsStatus_Type = RmonStatus
_RmonStatsStatus_Object = MibTableColumn
rmonStatsStatus = _RmonStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 2, 1, 1, 4),
    _RmonStatsStatus_Type()
)
rmonStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsStatus.setStatus("current")
_RmonHistory_ObjectIdentity = ObjectIdentity
rmonHistory = _RmonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3)
)
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "rmonHistoryIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")
_RmonHistoryDataSource_Type = ObjectIdentifier
_RmonHistoryDataSource_Object = MibTableColumn
rmonHistoryDataSource = _RmonHistoryDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1, 1, 5),
    _RmonHistoryOwner_Type()
)
rmonHistoryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryOwner.setStatus("current")
_RmonHistoryStatus_Type = RmonStatus
_RmonHistoryStatus_Object = MibTableColumn
rmonHistoryStatus = _RmonHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 3, 1, 1, 6),
    _RmonHistoryStatus_Type()
)
rmonHistoryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryStatus.setStatus("current")
_RmonAlarm_ObjectIdentity = ObjectIdentity
rmonAlarm = _RmonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4)
)
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "rmonAlarmIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")
_RmonAlarmInterval_Type = Integer32
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")
_RmonAlarmRisingThreshold_Type = Integer32
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 5),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")
_RmonAlarmFallingThreshold_Type = Integer32
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 9),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")
_RmonAlarmStatus_Type = RmonStatus
_RmonAlarmStatus_Object = MibTableColumn
rmonAlarmStatus = _RmonAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 4, 1, 1, 10),
    _RmonAlarmStatus_Type()
)
rmonAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmStatus.setStatus("current")
_RmonEvent_ObjectIdentity = ObjectIdentity
rmonEvent = _RmonEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5)
)
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1, 1)
)
rmonEventEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "rmonEventIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")
_RmonEventStatus_Type = RmonStatus
_RmonEventStatus_Object = MibTableColumn
rmonEventStatus = _RmonEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 47, 5, 1, 1, 6),
    _RmonEventStatus_Type()
)
rmonEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventStatus.setStatus("current")
_CompanyNeighbor_ObjectIdentity = ObjectIdentity
companyNeighbor = _CompanyNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50)
)
_NeighborTable_Object = MibTable
neighborTable = _NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1)
)
if mibBuilder.loadTexts:
    neighborTable.setStatus("current")
_NeighborEntry_Object = MibTableRow
neighborEntry = _NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1, 1)
)
neighborEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "neighborIfindex"),
    (0, "DGS-1210-20_CX", "neighborIPv6Addr"),
    (0, "DGS-1210-20_CX", "neighborMACAddr"),
)
if mibBuilder.loadTexts:
    neighborEntry.setStatus("current")
_NeighborIfindex_Type = Integer32
_NeighborIfindex_Object = MibTableColumn
neighborIfindex = _NeighborIfindex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1, 1, 1),
    _NeighborIfindex_Type()
)
neighborIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIfindex.setStatus("current")
_NeighborIPv6Addr_Type = Ipv6Address
_NeighborIPv6Addr_Object = MibTableColumn
neighborIPv6Addr = _NeighborIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1, 1, 2),
    _NeighborIPv6Addr_Type()
)
neighborIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIPv6Addr.setStatus("current")
_NeighborMACAddr_Type = MacAddress
_NeighborMACAddr_Object = MibTableColumn
neighborMACAddr = _NeighborMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1, 1, 5),
    _NeighborCacheState_Type()
)
neighborCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborCacheState.setStatus("current")
_NeighborRowStatus_Type = RowStatus
_NeighborRowStatus_Object = MibTableColumn
neighborRowStatus = _NeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 50, 1, 1, 7),
    _NeighborRowStatus_Type()
)
neighborRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neighborRowStatus.setStatus("current")
_Companydot3azEEE_ObjectIdentity = ObjectIdentity
companydot3azEEE = _Companydot3azEEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 52)
)
_Dot3azEEEset_ObjectIdentity = ObjectIdentity
dot3azEEEset = _Dot3azEEEset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 52, 1)
)
_Dot3azTable_Object = MibTable
dot3azTable = _Dot3azTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 52, 1, 1)
)
if mibBuilder.loadTexts:
    dot3azTable.setStatus("current")
_Dot3azEntry_Object = MibTableRow
dot3azEntry = _Dot3azEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 52, 1, 1, 1)
)
dot3azEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "portD3Index"),
)
if mibBuilder.loadTexts:
    dot3azEntry.setStatus("current")
_PortD3Index_Type = Integer32
_PortD3Index_Object = MibTableColumn
portD3Index = _PortD3Index_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 52, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 52, 1, 1, 1, 2),
    _PortD3State_Type()
)
portD3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portD3State.setStatus("current")
_CompanyDHCPRelay_ObjectIdentity = ObjectIdentity
companyDHCPRelay = _CompanyDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61)
)
_DhcpRelayControl_ObjectIdentity = ObjectIdentity
dhcpRelayControl = _DhcpRelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 1, 3),
    _DhcpRelayTimeThreshold_Type()
)
dhcpRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTimeThreshold.setStatus("current")
_DhcpRelayManagement_ObjectIdentity = ObjectIdentity
dhcpRelayManagement = _DhcpRelayManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2)
)
_DhcpRelayInterfaceSettingsTable_Object = MibTable
dhcpRelayInterfaceSettingsTable = _DhcpRelayInterfaceSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayInterfaceSettingsTable.setStatus("current")
_DhcpRelayInterfaceSettingsEntry_Object = MibTableRow
dhcpRelayInterfaceSettingsEntry = _DhcpRelayInterfaceSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 1, 1)
)
dhcpRelayInterfaceSettingsEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dhcpRelayInterface"),
    (0, "DGS-1210-20_CX", "dhcpRelayServerIP"),
)
if mibBuilder.loadTexts:
    dhcpRelayInterfaceSettingsEntry.setStatus("current")


class _DhcpRelayInterface_Type(DisplayString):
    """Custom type dhcpRelayInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DhcpRelayInterface_Type.__name__ = "DisplayString"
_DhcpRelayInterface_Object = MibTableColumn
dhcpRelayInterface = _DhcpRelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 1, 1, 1),
    _DhcpRelayInterface_Type()
)
dhcpRelayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayInterface.setStatus("current")
_DhcpRelayServerIP_Type = IpAddress
_DhcpRelayServerIP_Object = MibTableColumn
dhcpRelayServerIP = _DhcpRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 1, 1, 2),
    _DhcpRelayServerIP_Type()
)
dhcpRelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerIP.setStatus("current")
_DhcpRelayInterfaceSettingsRowStatus_Type = RowStatus
_DhcpRelayInterfaceSettingsRowStatus_Object = MibTableColumn
dhcpRelayInterfaceSettingsRowStatus = _DhcpRelayInterfaceSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 1, 1, 3),
    _DhcpRelayInterfaceSettingsRowStatus_Type()
)
dhcpRelayInterfaceSettingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayInterfaceSettingsRowStatus.setStatus("current")
_DhcpRelayManagementOption82_ObjectIdentity = ObjectIdentity
dhcpRelayManagementOption82 = _DhcpRelayManagementOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 2, 1),
    _DhcpRelayOption82State_Type()
)
dhcpRelayOption82State.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 2, 4),
    _DhcpRelayOption82RemoteIDType_Type()
)
dhcpRelayOption82RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82RemoteIDType.setStatus("current")
_DhcpRelayOption82RemoteID_Type = DisplayString
_DhcpRelayOption82RemoteID_Object = MibScalar
dhcpRelayOption82RemoteID = _DhcpRelayOption82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 61, 2, 2, 5),
    _DhcpRelayOption82RemoteID_Type()
)
dhcpRelayOption82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82RemoteID.setStatus("current")
_CompanyDHCPLocalRelay_ObjectIdentity = ObjectIdentity
companyDHCPLocalRelay = _CompanyDHCPLocalRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 62)
)


class _DhcpLocalRelayGlobalState_Type(Integer32):
    """Custom type dhcpLocalRelayGlobalState based on Integer32"""
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


_DhcpLocalRelayGlobalState_Type.__name__ = "Integer32"
_DhcpLocalRelayGlobalState_Object = MibScalar
dhcpLocalRelayGlobalState = _DhcpLocalRelayGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 62, 1),
    _DhcpLocalRelayGlobalState_Type()
)
dhcpLocalRelayGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelayGlobalState.setStatus("current")
_DhcpLocalRelayTable_Object = MibTable
dhcpLocalRelayTable = _DhcpLocalRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 62, 2)
)
if mibBuilder.loadTexts:
    dhcpLocalRelayTable.setStatus("current")
_DhcpLocalRelayEntry_Object = MibTableRow
dhcpLocalRelayEntry = _DhcpLocalRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 62, 2, 1)
)
dhcpLocalRelayEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dhcpLocalRelaySettingsVLANID"),
)
if mibBuilder.loadTexts:
    dhcpLocalRelayEntry.setStatus("current")


class _DhcpLocalRelaySettingsVLANID_Type(Integer32):
    """Custom type dhcpLocalRelaySettingsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpLocalRelaySettingsVLANID_Type.__name__ = "Integer32"
_DhcpLocalRelaySettingsVLANID_Object = MibTableColumn
dhcpLocalRelaySettingsVLANID = _DhcpLocalRelaySettingsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 62, 2, 1, 1),
    _DhcpLocalRelaySettingsVLANID_Type()
)
dhcpLocalRelaySettingsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLocalRelaySettingsVLANID.setStatus("current")


class _DhcpLocalRelaySettingsState_Type(Integer32):
    """Custom type dhcpLocalRelaySettingsState based on Integer32"""
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


_DhcpLocalRelaySettingsState_Type.__name__ = "Integer32"
_DhcpLocalRelaySettingsState_Object = MibTableColumn
dhcpLocalRelaySettingsState = _DhcpLocalRelaySettingsState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 62, 2, 1, 2),
    _DhcpLocalRelaySettingsState_Type()
)
dhcpLocalRelaySettingsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelaySettingsState.setStatus("current")
_CompanyDHCPv6Relay_ObjectIdentity = ObjectIdentity
companyDHCPv6Relay = _CompanyDHCPv6Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63)
)
_Dhcpv6RelayControl_ObjectIdentity = ObjectIdentity
dhcpv6RelayControl = _Dhcpv6RelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 1, 2),
    _Dhcpv6RelayHopCount_Type()
)
dhcpv6RelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayHopCount.setStatus("current")
_Dhcpv6RelayManagement_ObjectIdentity = ObjectIdentity
dhcpv6RelayManagement = _Dhcpv6RelayManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 2)
)
_Dhcpv6RelayInterfaceSettingsTable_Object = MibTable
dhcpv6RelayInterfaceSettingsTable = _Dhcpv6RelayInterfaceSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpv6RelayInterfaceSettingsTable.setStatus("current")
_Dhcpv6RelayInterfaceSettingsEntry_Object = MibTableRow
dhcpv6RelayInterfaceSettingsEntry = _Dhcpv6RelayInterfaceSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 2, 1, 1)
)
dhcpv6RelayInterfaceSettingsEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "dhcpv6RelayInterface"),
    (0, "DGS-1210-20_CX", "dhcpv6RelayServerIP"),
)
if mibBuilder.loadTexts:
    dhcpv6RelayInterfaceSettingsEntry.setStatus("current")


class _Dhcpv6RelayInterface_Type(DisplayString):
    """Custom type dhcpv6RelayInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Dhcpv6RelayInterface_Type.__name__ = "DisplayString"
_Dhcpv6RelayInterface_Object = MibTableColumn
dhcpv6RelayInterface = _Dhcpv6RelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 2, 1, 1, 1),
    _Dhcpv6RelayInterface_Type()
)
dhcpv6RelayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6RelayInterface.setStatus("current")
_Dhcpv6RelayServerIP_Type = Ipv6Address
_Dhcpv6RelayServerIP_Object = MibTableColumn
dhcpv6RelayServerIP = _Dhcpv6RelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 2, 1, 1, 2),
    _Dhcpv6RelayServerIP_Type()
)
dhcpv6RelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6RelayServerIP.setStatus("current")
_Dhcpv6RelayInterfaceSettingsRowStatus_Type = RowStatus
_Dhcpv6RelayInterfaceSettingsRowStatus_Object = MibTableColumn
dhcpv6RelayInterfaceSettingsRowStatus = _Dhcpv6RelayInterfaceSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 2, 1, 1, 99),
    _Dhcpv6RelayInterfaceSettingsRowStatus_Type()
)
dhcpv6RelayInterfaceSettingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpv6RelayInterfaceSettingsRowStatus.setStatus("current")
_Dhcpv6RelayOption37_ObjectIdentity = ObjectIdentity
dhcpv6RelayOption37 = _Dhcpv6RelayOption37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 3)
)


class _Dhcpv6RelayOption37State_Type(Integer32):
    """Custom type dhcpv6RelayOption37State based on Integer32"""
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


_Dhcpv6RelayOption37State_Type.__name__ = "Integer32"
_Dhcpv6RelayOption37State_Object = MibScalar
dhcpv6RelayOption37State = _Dhcpv6RelayOption37State_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 3, 1),
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
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Dhcpv6RelayOption37CheckState_Type.__name__ = "Integer32"
_Dhcpv6RelayOption37CheckState_Object = MibScalar
dhcpv6RelayOption37CheckState = _Dhcpv6RelayOption37CheckState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 3, 3),
    _Dhcpv6RelayOption37RemoteIDType_Type()
)
dhcpv6RelayOption37RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37RemoteIDType.setStatus("current")
_Dhcpv6RelayOption37RemoteID_Type = DisplayString
_Dhcpv6RelayOption37RemoteID_Object = MibScalar
dhcpv6RelayOption37RemoteID = _Dhcpv6RelayOption37RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 63, 3, 4),
    _Dhcpv6RelayOption37RemoteID_Type()
)
dhcpv6RelayOption37RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37RemoteID.setStatus("current")
_CompanyMldsGroup_ObjectIdentity = ObjectIdentity
companyMldsGroup = _CompanyMldsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88)
)
_MldsSystem_ObjectIdentity = ObjectIdentity
mldsSystem = _MldsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1, 1),
    _MldsStatus_Type()
)
mldsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsStatus.setStatus("current")


class _MldsRouterPortPurgeInterval_Type(Integer32):
    """Custom type mldsRouterPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_MldsRouterPortPurgeInterval_Type.__name__ = "Integer32"
_MldsRouterPortPurgeInterval_Object = MibScalar
mldsRouterPortPurgeInterval = _MldsRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1, 2),
    _MldsRouterPortPurgeInterval_Type()
)
mldsRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsRouterPortPurgeInterval.setStatus("current")


class _MldsHostPortPurgeInterval_Type(Integer32):
    """Custom type mldsHostPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 153025),
    )


_MldsHostPortPurgeInterval_Type.__name__ = "Integer32"
_MldsHostPortPurgeInterval_Object = MibScalar
mldsHostPortPurgeInterval = _MldsHostPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1, 3),
    _MldsHostPortPurgeInterval_Type()
)
mldsHostPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsHostPortPurgeInterval.setStatus("current")


class _MldsRobustnessValue_Type(Integer32):
    """Custom type mldsRobustnessValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_MldsRobustnessValue_Type.__name__ = "Integer32"
_MldsRobustnessValue_Object = MibScalar
mldsRobustnessValue = _MldsRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1, 4),
    _MldsRobustnessValue_Type()
)
mldsRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsRobustnessValue.setStatus("current")


class _MldsGrpQueryInterval_Type(Integer32):
    """Custom type mldsGrpQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MldsGrpQueryInterval_Type.__name__ = "Integer32"
_MldsGrpQueryInterval_Object = MibScalar
mldsGrpQueryInterval = _MldsGrpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1, 5),
    _MldsGrpQueryInterval_Type()
)
mldsGrpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsGrpQueryInterval.setStatus("current")


class _MldsQueryInterval_Type(Integer32):
    """Custom type mldsQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_MldsQueryInterval_Type.__name__ = "Integer32"
_MldsQueryInterval_Object = MibScalar
mldsQueryInterval = _MldsQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1, 6),
    _MldsQueryInterval_Type()
)
mldsQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsQueryInterval.setStatus("current")


class _MldsQueryMaxResponseTime_Type(Integer32):
    """Custom type mldsQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 25),
    )


_MldsQueryMaxResponseTime_Type.__name__ = "Integer32"
_MldsQueryMaxResponseTime_Object = MibScalar
mldsQueryMaxResponseTime = _MldsQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 1, 7),
    _MldsQueryMaxResponseTime_Type()
)
mldsQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsQueryMaxResponseTime.setStatus("current")
_MldsVlan_ObjectIdentity = ObjectIdentity
mldsVlan = _MldsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3)
)
_MldsVlanRouterTable_Object = MibTable
mldsVlanRouterTable = _MldsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 3)
)
if mibBuilder.loadTexts:
    mldsVlanRouterTable.setStatus("current")
_MldsVlanRouterEntry_Object = MibTableRow
mldsVlanRouterEntry = _MldsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 3, 1)
)
mldsVlanRouterEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "mldsVlanRouterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 3, 1, 1),
    _MldsVlanRouterVlanId_Type()
)
mldsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanRouterVlanId.setStatus("current")
_MldsVlanRouterPortList_Type = PortList
_MldsVlanRouterPortList_Object = MibTableColumn
mldsVlanRouterPortList = _MldsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 3, 1, 2),
    _MldsVlanRouterPortList_Type()
)
mldsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanRouterPortList.setStatus("current")
_MldsVlanFilterTable_Object = MibTable
mldsVlanFilterTable = _MldsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4)
)
if mibBuilder.loadTexts:
    mldsVlanFilterTable.setStatus("current")
_MldsVlanFilterEntry_Object = MibTableRow
mldsVlanFilterEntry = _MldsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1)
)
mldsVlanFilterEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "mldsVlanFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1, 5),
    _MldsVlanQueryInterval_Type()
)
mldsVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanQueryInterval.setStatus("current")
_MldsVlanRtrPortList_Type = PortList
_MldsVlanRtrPortList_Object = MibTableColumn
mldsVlanRtrPortList = _MldsVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1, 6),
    _MldsVlanRtrPortList_Type()
)
mldsVlanRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanRtrPortList.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 4, 1, 8),
    _MldsVlanFastLeave_Type()
)
mldsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanFastLeave.setStatus("current")
_MldsVlanMulticastGroupTable_Object = MibTable
mldsVlanMulticastGroupTable = _MldsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 5)
)
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupTable.setStatus("current")
_MldsVlanMulticastGroupEntry_Object = MibTableRow
mldsVlanMulticastGroupEntry = _MldsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 5, 1)
)
mldsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "mldsVlanMulticastGroupVlanId"),
    (0, "DGS-1210-20_CX", "mldsVlanMulticastGroupIpAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 5, 1, 1),
    _MldsVlanMulticastGroupVlanId_Type()
)
mldsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupVlanId.setStatus("current")
_MldsVlanMulticastGroupIpAddress_Type = InetAddress
_MldsVlanMulticastGroupIpAddress_Object = MibTableColumn
mldsVlanMulticastGroupIpAddress = _MldsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 5, 1, 2),
    _MldsVlanMulticastGroupIpAddress_Type()
)
mldsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupIpAddress.setStatus("current")
_MldsVlanMulticastGroupMacAddress_Type = MacAddress
_MldsVlanMulticastGroupMacAddress_Object = MibTableColumn
mldsVlanMulticastGroupMacAddress = _MldsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 5, 1, 3),
    _MldsVlanMulticastGroupMacAddress_Type()
)
mldsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupMacAddress.setStatus("current")
_MldsVlanMulticastGroupPortList_Type = PortList
_MldsVlanMulticastGroupPortList_Object = MibTableColumn
mldsVlanMulticastGroupPortList = _MldsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 88, 3, 5, 1, 4),
    _MldsVlanMulticastGroupPortList_Type()
)
mldsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupPortList.setStatus("current")
_CompanyDoSCtrl_ObjectIdentity = ObjectIdentity
companyDoSCtrl = _CompanyDoSCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 99)
)


class _DoSCtrlState_Type(Integer32):
    """Custom type doSCtrlState based on Integer32"""
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


_DoSCtrlState_Type.__name__ = "Integer32"
_DoSCtrlState_Object = MibScalar
doSCtrlState = _DoSCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 99, 1),
    _DoSCtrlState_Type()
)
doSCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doSCtrlState.setStatus("current")
_DoSCtrlTable_Object = MibTable
doSCtrlTable = _DoSCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 99, 2)
)
if mibBuilder.loadTexts:
    doSCtrlTable.setStatus("current")
_DoSCtrlEntry_Object = MibTableRow
doSCtrlEntry = _DoSCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 99, 2, 1)
)
doSCtrlEntry.setIndexNames(
    (0, "DGS-1210-20_CX", "doSCtrlType"),
)
if mibBuilder.loadTexts:
    doSCtrlEntry.setStatus("current")


class _DoSCtrlType_Type(Integer32):
    """Custom type doSCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("blatattack", 2),
          ("landattack", 1),
          ("tcpnullscan", 4),
          ("tcpsynfin", 6),
          ("tcpsynsrcportless1024", 7),
          ("tcpxmascan", 5))
    )


_DoSCtrlType_Type.__name__ = "Integer32"
_DoSCtrlType_Object = MibTableColumn
doSCtrlType = _DoSCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 99, 2, 1, 1),
    _DoSCtrlType_Type()
)
doSCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doSCtrlType.setStatus("current")


class _DoSCtrlDisplayState_Type(Integer32):
    """Custom type doSCtrlDisplayState based on Integer32"""
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


_DoSCtrlDisplayState_Type.__name__ = "Integer32"
_DoSCtrlDisplayState_Object = MibTableColumn
doSCtrlDisplayState = _DoSCtrlDisplayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 99, 2, 1, 2),
    _DoSCtrlDisplayState_Type()
)
doSCtrlDisplayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doSCtrlDisplayState.setStatus("current")
dot1dBasePortEntry.registerAugmentions(
    ("DGS-1210-20_CX",
     "dot1qVlanPortEntry")
)
dot1qVlanPortEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27, 0, 4)
)
topologyChange.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )

firmwareUpgradeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27, 0, 8)
)
if mibBuilder.loadTexts:
    firmwareUpgradeSuccess.setStatus(
        "current"
    )

firmwareUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27, 0, 9)
)
if mibBuilder.loadTexts:
    firmwareUpgradeFailure.setStatus(
        "current"
    )

firmwareIllegalFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27, 0, 10)
)
if mibBuilder.loadTexts:
    firmwareIllegalFile.setStatus(
        "current"
    )

firmwareTransferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27, 0, 11)
)
if mibBuilder.loadTexts:
    firmwareTransferError.setStatus(
        "current"
    )

firmwareChecksumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 19, 1, 27, 0, 12)
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
    "DGS-1210-20_CX",
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
       "dgs-1210-20": dgs_1210_20,
       "dgs-1210-20cx": dgs_1210_20cx,
       "companySystem": companySystem,
       "sysSwitchName": sysSwitchName,
       "sysHardwareVersion": sysHardwareVersion,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysLoginTimeoutInterval": sysLoginTimeoutInterval,
       "sysLocationName": sysLocationName,
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
       "sysPortDescriptionTable": sysPortDescriptionTable,
       "sysPortDescriptionEntry": sysPortDescriptionEntry,
       "sysPortDescIndex": sysPortDescIndex,
       "sysPortDescString": sysPortDescString,
       "sysDdp": sysDdp,
       "sysDdpGlobalOnOff": sysDdpGlobalOnOff,
       "sysDdpGeneralReportOnOff": sysDdpGeneralReportOnOff,
       "sysDdpGeneralReportTimer": sysDdpGeneralReportTimer,
       "sysDdpProtStatusTable": sysDdpProtStatusTable,
       "sysDdpProtStatusEntry": sysDdpProtStatusEntry,
       "sysDdpProtStatusIndex": sysDdpProtStatusIndex,
       "sysDdpProtStatusControl": sysDdpProtStatusControl,
       "companyIpifGroup": companyIpifGroup,
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
       "dhcpOption12Status": dhcpOption12Status,
       "dhcpOption12HostName": dhcpOption12HostName,
       "companyTftpGroup": companyTftpGroup,
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
       "dhcpServerScreenTrustedServerTable": dhcpServerScreenTrustedServerTable,
       "dhcpServerScreenTrustedServerEntry": dhcpServerScreenTrustedServerEntry,
       "dhcpServerScreenTrustedServerIndex": dhcpServerScreenTrustedServerIndex,
       "dhcpServerScreenTrustedServerAddress": dhcpServerScreenTrustedServerAddress,
       "dhcpServerScreenIPType": dhcpServerScreenIPType,
       "dhcpServerScreenTrustedServerStatus": dhcpServerScreenTrustedServerStatus,
       "securitySSH": securitySSH,
       "sshSecurityStatus": sshSecurityStatus,
       "sshMaxAuthFailAttempts": sshMaxAuthFailAttempts,
       "sshSessionKeyRekeying": sshSessionKeyRekeying,
       "sshMaxSession": sshMaxSession,
       "sshConnectionTimeout": sshConnectionTimeout,
       "sshAuthenMethodPassWordAdmin": sshAuthenMethodPassWordAdmin,
       "sshAuthenMethodPubKeyAdmin": sshAuthenMethodPubKeyAdmin,
       "sshAuthenMethodHostKeyAdmin": sshAuthenMethodHostKeyAdmin,
       "sshCipherSuiteList": sshCipherSuiteList,
       "sshMacSuiteList": sshMacSuiteList,
       "sshPublKeyRSAAdmin": sshPublKeyRSAAdmin,
       "sshUserInfoTable": sshUserInfoTable,
       "sshUserInfoEntry": sshUserInfoEntry,
       "sshUserInfoID": sshUserInfoID,
       "sshUserInfoUserName": sshUserInfoUserName,
       "sshUserInfoAuth": sshUserInfoAuth,
       "sshUserInfoHostName": sshUserInfoHostName,
       "sshUserInfoHostIp": sshUserInfoHostIp,
       "sshUserInfoHostIpv6": sshUserInfoHostIpv6,
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
       "aclProfileTable": aclProfileTable,
       "aclProfileEntry": aclProfileEntry,
       "aclProfileNo": aclProfileNo,
       "aclProfileName": aclProfileName,
       "aclProfileType": aclProfileType,
       "aclProfileRuleCount": aclProfileRuleCount,
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
       "aclL2RuleAction": aclL2RuleAction,
       "aclL2RulePriority": aclL2RulePriority,
       "aclL2RuleReplacePriority": aclL2RuleReplacePriority,
       "aclL2RuleStatus": aclL2RuleStatus,
       "aclL3v4Rule": aclL3v4Rule,
       "aclL3v4RuleTable": aclL3v4RuleTable,
       "aclL3v4RuleEntry": aclL3v4RuleEntry,
       "aclL3v4RuleAccessID": aclL3v4RuleAccessID,
       "aclL3v4RuleProfileNo": aclL3v4RuleProfileNo,
       "aclL3v4RuleDstIpAddr": aclL3v4RuleDstIpAddr,
       "aclL3v4RuleSrcIpAddr": aclL3v4RuleSrcIpAddr,
       "aclL3v4RuleDstIpAddrMask": aclL3v4RuleDstIpAddrMask,
       "aclL3v4RuleSrcIpAddrMask": aclL3v4RuleSrcIpAddrMask,
       "aclL3v4RuleAction": aclL3v4RuleAction,
       "aclL3v4RulePriority": aclL3v4RulePriority,
       "aclL3v4RuleReplacePriority": aclL3v4RuleReplacePriority,
       "aclL3v4RuleStatus": aclL3v4RuleStatus,
       "aclL3v4ExtRule": aclL3v4ExtRule,
       "aclL3v4ExtRuleTable": aclL3v4ExtRuleTable,
       "aclL3v4ExtRuleEntry": aclL3v4ExtRuleEntry,
       "aclL3v4ExtRuleAccessID": aclL3v4ExtRuleAccessID,
       "aclL3v4ExtRuleProfileNo": aclL3v4ExtRuleProfileNo,
       "aclL3v4ExtRuleProtocol": aclL3v4ExtRuleProtocol,
       "aclL3v4ExtRuleICMPMessageType": aclL3v4ExtRuleICMPMessageType,
       "aclL3v4ExtRuleICMPMessageCode": aclL3v4ExtRuleICMPMessageCode,
       "aclL3v4ExtRuleDstIpAddr": aclL3v4ExtRuleDstIpAddr,
       "aclL3v4ExtRuleSrcIpAddr": aclL3v4ExtRuleSrcIpAddr,
       "aclL3v4ExtRuleDstIpAddrMask": aclL3v4ExtRuleDstIpAddrMask,
       "aclL3v4ExtRuleSrcIpAddrMask": aclL3v4ExtRuleSrcIpAddrMask,
       "aclL3v4ExtRuleTcpUdpDstPort": aclL3v4ExtRuleTcpUdpDstPort,
       "aclL3v4ExtRuleTcpUdpSrcPort": aclL3v4ExtRuleTcpUdpSrcPort,
       "aclL3v4ExtRuleTcpUdpDstPortMask": aclL3v4ExtRuleTcpUdpDstPortMask,
       "aclL3v4ExtRuleTcpUdpSrcPortMask": aclL3v4ExtRuleTcpUdpSrcPortMask,
       "aclL3v4ExtRuleDscp": aclL3v4ExtRuleDscp,
       "aclL3v4ExtRuleToS": aclL3v4ExtRuleToS,
       "aclL3v4ExtRuleIgmpType": aclL3v4ExtRuleIgmpType,
       "aclL3v4ExtRuleProtocolId": aclL3v4ExtRuleProtocolId,
       "aclL3v4ExtRuleAction": aclL3v4ExtRuleAction,
       "aclL3v4ExtRulePriority": aclL3v4ExtRulePriority,
       "aclL3v4ExtRuleReplacePriority": aclL3v4ExtRuleReplacePriority,
       "aclL3v4ExtRuleStatus": aclL3v4ExtRuleStatus,
       "aclL3v6Rule": aclL3v6Rule,
       "aclL3v6RuleTable": aclL3v6RuleTable,
       "aclL3v6RuleEntry": aclL3v6RuleEntry,
       "aclL3v6RuleAccessID": aclL3v6RuleAccessID,
       "aclL3v6RuleProfileNo": aclL3v6RuleProfileNo,
       "aclL3v6RuleTrafficClass": aclL3v6RuleTrafficClass,
       "aclL3v6RuleProtocol": aclL3v6RuleProtocol,
       "aclL3v6RuleProtocolId": aclL3v6RuleProtocolId,
       "aclL3v6RuleTcpUdpDstPort": aclL3v6RuleTcpUdpDstPort,
       "aclL3v6RuleTcpUdpSrcPort": aclL3v6RuleTcpUdpSrcPort,
       "aclL3v6RuleTcpUdpDstPortMask": aclL3v6RuleTcpUdpDstPortMask,
       "aclL3v6RuleTcpUdpSrcPortMask": aclL3v6RuleTcpUdpSrcPortMask,
       "aclL3v6RuleICMPv6MessageType": aclL3v6RuleICMPv6MessageType,
       "aclL3v6RuleICMPv6MessageCode": aclL3v6RuleICMPv6MessageCode,
       "aclL3v6RuleDstIpv6Addr": aclL3v6RuleDstIpv6Addr,
       "aclL3v6RuleSrcIpv6Addr": aclL3v6RuleSrcIpv6Addr,
       "aclL3v6RuleDstIpv6AddrPrefixLen": aclL3v6RuleDstIpv6AddrPrefixLen,
       "aclL3v6RuleSrcIpv6AddrPrefixLen": aclL3v6RuleSrcIpv6AddrPrefixLen,
       "aclL3v6RuleAction": aclL3v6RuleAction,
       "aclL3v6RulePriority": aclL3v6RulePriority,
       "aclL3v6RuleReplacePriority": aclL3v6RuleReplacePriority,
       "aclL3v6RuleStatus": aclL3v6RuleStatus,
       "aclPortBindGroup": aclPortBindGroup,
       "aclPortGroupTable": aclPortGroupTable,
       "aclPortGroupEntry": aclPortGroupEntry,
       "aclPortIndex": aclPortIndex,
       "aclPortL2ProfileNo": aclPortL2ProfileNo,
       "aclPortL3v4ProfileNo": aclPortL3v4ProfileNo,
       "aclPortL3v6ProfileNo": aclPortL3v6ProfileNo,
       "aclHWResourceStatus": aclHWResourceStatus,
       "aclHWResourceStatusTable": aclHWResourceStatusTable,
       "aclHWResourceStatusEntry": aclHWResourceStatusEntry,
       "aclHWProfileIndex": aclHWProfileIndex,
       "aclAccessListNo": aclAccessListNo,
       "aclResourceEntryCount": aclResourceEntryCount,
       "companySyslog": companySyslog,
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
       "swLoopDetectEnabledVlanList": swLoopDetectEnabledVlanList,
       "companyMirror": companyMirror,
       "sysMirrorStatus": sysMirrorStatus,
       "sysMirrorTargetPort": sysMirrorTargetPort,
       "sysMirrorCtrlIngressMirroring": sysMirrorCtrlIngressMirroring,
       "sysMirrorCtrlEgressMirroring": sysMirrorCtrlEgressMirroring,
       "companySNTPSetting": companySNTPSetting,
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
       "swAuthRadiusIPType": swAuthRadiusIPType,
       "swAuthRadiusServerAddress": swAuthRadiusServerAddress,
       "swAuthRadiusServerInterfaceName": swAuthRadiusServerInterfaceName,
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
       "snmpV3TrapLBD": snmpV3TrapLBD,
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
       "dlinkGreenSystemHibernation": dlinkGreenSystemHibernation,
       "dlinkGreenSystemHibernationState": dlinkGreenSystemHibernationState,
       "dlinkGreenSystemHibernationTimeProfile1": dlinkGreenSystemHibernationTimeProfile1,
       "dlinkGreenSystemHibernationTimeProfile2": dlinkGreenSystemHibernationTimeProfile2,
       "dlinkPowerSavingGlobalSetting": dlinkPowerSavingGlobalSetting,
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
       "portD3State": portD3State,
       "companyDHCPRelay": companyDHCPRelay,
       "dhcpRelayControl": dhcpRelayControl,
       "dhcpRelayState": dhcpRelayState,
       "dhcpRelayHopCount": dhcpRelayHopCount,
       "dhcpRelayTimeThreshold": dhcpRelayTimeThreshold,
       "dhcpRelayManagement": dhcpRelayManagement,
       "dhcpRelayInterfaceSettingsTable": dhcpRelayInterfaceSettingsTable,
       "dhcpRelayInterfaceSettingsEntry": dhcpRelayInterfaceSettingsEntry,
       "dhcpRelayInterface": dhcpRelayInterface,
       "dhcpRelayServerIP": dhcpRelayServerIP,
       "dhcpRelayInterfaceSettingsRowStatus": dhcpRelayInterfaceSettingsRowStatus,
       "dhcpRelayManagementOption82": dhcpRelayManagementOption82,
       "dhcpRelayOption82State": dhcpRelayOption82State,
       "dhcpRelayOption82CheckState": dhcpRelayOption82CheckState,
       "dhcpRelayOption82Policy": dhcpRelayOption82Policy,
       "dhcpRelayOption82RemoteIDType": dhcpRelayOption82RemoteIDType,
       "dhcpRelayOption82RemoteID": dhcpRelayOption82RemoteID,
       "companyDHCPLocalRelay": companyDHCPLocalRelay,
       "dhcpLocalRelayGlobalState": dhcpLocalRelayGlobalState,
       "dhcpLocalRelayTable": dhcpLocalRelayTable,
       "dhcpLocalRelayEntry": dhcpLocalRelayEntry,
       "dhcpLocalRelaySettingsVLANID": dhcpLocalRelaySettingsVLANID,
       "dhcpLocalRelaySettingsState": dhcpLocalRelaySettingsState,
       "companyDHCPv6Relay": companyDHCPv6Relay,
       "dhcpv6RelayControl": dhcpv6RelayControl,
       "dhcpv6RelayState": dhcpv6RelayState,
       "dhcpv6RelayHopCount": dhcpv6RelayHopCount,
       "dhcpv6RelayManagement": dhcpv6RelayManagement,
       "dhcpv6RelayInterfaceSettingsTable": dhcpv6RelayInterfaceSettingsTable,
       "dhcpv6RelayInterfaceSettingsEntry": dhcpv6RelayInterfaceSettingsEntry,
       "dhcpv6RelayInterface": dhcpv6RelayInterface,
       "dhcpv6RelayServerIP": dhcpv6RelayServerIP,
       "dhcpv6RelayInterfaceSettingsRowStatus": dhcpv6RelayInterfaceSettingsRowStatus,
       "dhcpv6RelayOption37": dhcpv6RelayOption37,
       "dhcpv6RelayOption37State": dhcpv6RelayOption37State,
       "dhcpv6RelayOption37CheckState": dhcpv6RelayOption37CheckState,
       "dhcpv6RelayOption37RemoteIDType": dhcpv6RelayOption37RemoteIDType,
       "dhcpv6RelayOption37RemoteID": dhcpv6RelayOption37RemoteID,
       "companyMldsGroup": companyMldsGroup,
       "mldsSystem": mldsSystem,
       "mldsStatus": mldsStatus,
       "mldsRouterPortPurgeInterval": mldsRouterPortPurgeInterval,
       "mldsHostPortPurgeInterval": mldsHostPortPurgeInterval,
       "mldsRobustnessValue": mldsRobustnessValue,
       "mldsGrpQueryInterval": mldsGrpQueryInterval,
       "mldsQueryInterval": mldsQueryInterval,
       "mldsQueryMaxResponseTime": mldsQueryMaxResponseTime,
       "mldsVlan": mldsVlan,
       "mldsVlanRouterTable": mldsVlanRouterTable,
       "mldsVlanRouterEntry": mldsVlanRouterEntry,
       "mldsVlanRouterVlanId": mldsVlanRouterVlanId,
       "mldsVlanRouterPortList": mldsVlanRouterPortList,
       "mldsVlanFilterTable": mldsVlanFilterTable,
       "mldsVlanFilterEntry": mldsVlanFilterEntry,
       "mldsVlanFilterVlanId": mldsVlanFilterVlanId,
       "mldsVlanSnoopStatus": mldsVlanSnoopStatus,
       "mldsVlanQuerier": mldsVlanQuerier,
       "mldsVlanCfgQuerier": mldsVlanCfgQuerier,
       "mldsVlanQueryInterval": mldsVlanQueryInterval,
       "mldsVlanRtrPortList": mldsVlanRtrPortList,
       "mldsVlanFastLeave": mldsVlanFastLeave,
       "mldsVlanMulticastGroupTable": mldsVlanMulticastGroupTable,
       "mldsVlanMulticastGroupEntry": mldsVlanMulticastGroupEntry,
       "mldsVlanMulticastGroupVlanId": mldsVlanMulticastGroupVlanId,
       "mldsVlanMulticastGroupIpAddress": mldsVlanMulticastGroupIpAddress,
       "mldsVlanMulticastGroupMacAddress": mldsVlanMulticastGroupMacAddress,
       "mldsVlanMulticastGroupPortList": mldsVlanMulticastGroupPortList,
       "companyDoSCtrl": companyDoSCtrl,
       "doSCtrlState": doSCtrlState,
       "doSCtrlTable": doSCtrlTable,
       "doSCtrlEntry": doSCtrlEntry,
       "doSCtrlType": doSCtrlType,
       "doSCtrlDisplayState": doSCtrlDisplayState}
)
