# SNMP MIB module (DGS-1100-06ME-AX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-1100-06ME-AX
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:26 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dgs_1100_06ME_A1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1)
)
dgs_1100_06ME_A1.setRevisions(
        ("2015-06-03 00:00",
         "2015-04-16 00:00",
         "2014-03-06 00:00")
)


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



class OwnerString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
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



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class LldpPortNumber(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



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
_Dgs_1100_06ME_ObjectIdentity = ObjectIdentity
dgs_1100_06ME = _Dgs_1100_06ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1)
)
_CompanySystem_ObjectIdentity = ObjectIdentity
companySystem = _CompanySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 6),
    _SysGroupInterval_Type()
)
sysGroupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGroupInterval.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 8),
    _SysSafeGuardEnable_Type()
)
sysSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSafeGuardEnable.setStatus("current")


class _SysRestart_Type(TruthValue):
    """Custom type sysRestart based on TruthValue"""


_SysRestart_Object = MibScalar
sysRestart = _SysRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 9),
    _SysRestart_Type()
)
sysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestart.setStatus("current")


class _SysSave_Type(Integer32):
    """Custom type sysSave based on Integer32"""
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
        *(("config-1", 3),
          ("config-2", 4),
          ("false", 2),
          ("true", 1))
    )


_SysSave_Type.__name__ = "Integer32"
_SysSave_Object = MibScalar
sysSave = _SysSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 12),
    _SysJumboFrameEnable_Type()
)
sysJumboFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysJumboFrameEnable.setStatus("current")
_SysPortCtrlTable_Object = MibTable
sysPortCtrlTable = _SysPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    sysPortCtrlTable.setStatus("current")
_SysPortCtrlEntry_Object = MibTableRow
sysPortCtrlEntry = _SysPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1)
)
sysPortCtrlEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "sysPortCtrlIndex"),
    (0, "DGS-1100-06ME-AX", "sysPortCtrlMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 1),
    _SysPortCtrlIndex_Type()
)
sysPortCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlIndex.setStatus("current")


class _SysPortCtrlMediumType_Type(Integer32):
    """Custom type sysPortCtrlMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("copper", 100),
          ("fiber", 101))
    )


_SysPortCtrlMediumType_Type.__name__ = "Integer32"
_SysPortCtrlMediumType_Object = MibTableColumn
sysPortCtrlMediumType = _SysPortCtrlMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 2),
    _SysPortCtrlMediumType_Type()
)
sysPortCtrlMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlMediumType.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 7),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("fastethernet", 1),
          ("fiberwith100Base-and-1000BaseSFPModule", 3),
          ("gigabitethernet", 2))
    )


_SysPortCtrlType_Type.__name__ = "Integer32"
_SysPortCtrlType_Object = MibTableColumn
sysPortCtrlType = _SysPortCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 8),
    _SysPortCtrlType_Type()
)
sysPortCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCtrlType.setStatus("current")


class _SysPortCtrlCapability_Type(Bits):
    """Custom type sysPortCtrlCapability based on Bits"""
    namedValues = NamedValues(
        *(("rate10-full", 1),
          ("rate10-half", 0),
          ("rate100-full", 3),
          ("rate100-half", 2),
          ("rate1000-full", 5),
          ("reserve", 4))
    )

_SysPortCtrlCapability_Type.__name__ = "Bits"
_SysPortCtrlCapability_Object = MibTableColumn
sysPortCtrlCapability = _SysPortCtrlCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 13, 1, 9),
    _SysPortCtrlCapability_Type()
)
sysPortCtrlCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortCtrlCapability.setStatus("current")
_SysPortDescriptionTable_Object = MibTable
sysPortDescriptionTable = _SysPortDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    sysPortDescriptionTable.setStatus("current")
_SysPortDescriptionEntry_Object = MibTableRow
sysPortDescriptionEntry = _SysPortDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 14, 1)
)
sysPortDescriptionEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "sysPortDescIndex"),
    (0, "DGS-1100-06ME-AX", "sysPortDescMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 14, 1, 1),
    _SysPortDescIndex_Type()
)
sysPortDescIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortDescIndex.setStatus("current")


class _SysPortDescMediumType_Type(Integer32):
    """Custom type sysPortDescMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("copper", 100),
          ("fiber", 101))
    )


_SysPortDescMediumType_Type.__name__ = "Integer32"
_SysPortDescMediumType_Object = MibTableColumn
sysPortDescMediumType = _SysPortDescMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 14, 1, 2),
    _SysPortDescMediumType_Type()
)
sysPortDescMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortDescMediumType.setStatus("current")


class _SysPortDescString_Type(DisplayString):
    """Custom type sysPortDescString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysPortDescString_Type.__name__ = "DisplayString"
_SysPortDescString_Object = MibTableColumn
sysPortDescString = _SysPortDescString_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 14, 1, 3),
    _SysPortDescString_Type()
)
sysPortDescString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortDescString.setStatus("current")
_SysPortErrTable_Object = MibTable
sysPortErrTable = _SysPortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    sysPortErrTable.setStatus("current")
_SysPortErrEntry_Object = MibTableRow
sysPortErrEntry = _SysPortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 15, 1)
)
sysPortErrEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "sysPortErrPortIndex"),
)
if mibBuilder.loadTexts:
    sysPortErrEntry.setStatus("current")


class _SysPortErrPortIndex_Type(Integer32):
    """Custom type sysPortErrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysPortErrPortIndex_Type.__name__ = "Integer32"
_SysPortErrPortIndex_Object = MibTableColumn
sysPortErrPortIndex = _SysPortErrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 15, 1, 1),
    _SysPortErrPortIndex_Type()
)
sysPortErrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortErrPortIndex.setStatus("current")


class _SysPortErrPortState_Type(Integer32):
    """Custom type sysPortErrPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SysPortErrPortState_Type.__name__ = "Integer32"
_SysPortErrPortState_Object = MibTableColumn
sysPortErrPortState = _SysPortErrPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 15, 1, 2),
    _SysPortErrPortState_Type()
)
sysPortErrPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortErrPortState.setStatus("current")


class _SysPortErrPortStatus_Type(Integer32):
    """Custom type sysPortErrPortStatus based on Integer32"""
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


_SysPortErrPortStatus_Type.__name__ = "Integer32"
_SysPortErrPortStatus_Object = MibTableColumn
sysPortErrPortStatus = _SysPortErrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 15, 1, 3),
    _SysPortErrPortStatus_Type()
)
sysPortErrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortErrPortStatus.setStatus("current")


class _SysPortErrPortReason_Type(Integer32):
    """Custom type sysPortErrPortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("lbd", 1)
    )


_SysPortErrPortReason_Type.__name__ = "Integer32"
_SysPortErrPortReason_Object = MibTableColumn
sysPortErrPortReason = _SysPortErrPortReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 15, 1, 4),
    _SysPortErrPortReason_Type()
)
sysPortErrPortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortErrPortReason.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 20),
    _SysMACAgingTime_Type()
)
sysMACAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMACAgingTime.setStatus("current")


class _TelnetsettingManagementOnOff_Type(Integer32):
    """Custom type telnetsettingManagementOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TelnetsettingManagementOnOff_Type.__name__ = "Integer32"
_TelnetsettingManagementOnOff_Object = MibScalar
telnetsettingManagementOnOff = _TelnetsettingManagementOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 23),
    _TelnetsettingManagementOnOff_Type()
)
telnetsettingManagementOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetsettingManagementOnOff.setStatus("current")


class _TelnetUDPPort_Type(Integer32):
    """Custom type telnetUDPPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetUDPPort_Type.__name__ = "Integer32"
_TelnetUDPPort_Object = MibScalar
telnetUDPPort = _TelnetUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 24),
    _TelnetUDPPort_Type()
)
telnetUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetUDPPort.setStatus("current")


class _AutoRefreshConfiguration_Type(Integer32):
    """Custom type autoRefreshConfiguration based on Integer32"""
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


_AutoRefreshConfiguration_Type.__name__ = "Integer32"
_AutoRefreshConfiguration_Object = MibScalar
autoRefreshConfiguration = _AutoRefreshConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 25),
    _AutoRefreshConfiguration_Type()
)
autoRefreshConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRefreshConfiguration.setStatus("current")


class _FloodfdbOnOff_Type(Integer32):
    """Custom type floodfdbOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FloodfdbOnOff_Type.__name__ = "Integer32"
_FloodfdbOnOff_Object = MibScalar
floodfdbOnOff = _FloodfdbOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 26),
    _FloodfdbOnOff_Type()
)
floodfdbOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    floodfdbOnOff.setStatus("current")


class _SysContactName_Type(DisplayString):
    """Custom type sysContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysContactName_Type.__name__ = "DisplayString"
_SysContactName_Object = MibScalar
sysContactName = _SysContactName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 27),
    _SysContactName_Type()
)
sysContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContactName.setStatus("current")


class _SysCommandLogging_Type(Integer32):
    """Custom type sysCommandLogging based on Integer32"""
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


_SysCommandLogging_Type.__name__ = "Integer32"
_SysCommandLogging_Object = MibScalar
sysCommandLogging = _SysCommandLogging_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 29),
    _SysCommandLogging_Type()
)
sysCommandLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCommandLogging.setStatus("current")


class _SysSerialNumber_Type(DisplayString):
    """Custom type sysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_SysSerialNumber_Type.__name__ = "DisplayString"
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 30),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")


class _SysDhcpAutoImage_Type(Integer32):
    """Custom type sysDhcpAutoImage based on Integer32"""
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


_SysDhcpAutoImage_Type.__name__ = "Integer32"
_SysDhcpAutoImage_Object = MibScalar
sysDhcpAutoImage = _SysDhcpAutoImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 34),
    _SysDhcpAutoImage_Type()
)
sysDhcpAutoImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpAutoImage.setStatus("current")


class _SysBootupConfigID_Type(Integer32):
    """Custom type sysBootupConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SysBootupConfigID_Type.__name__ = "Integer32"
_SysBootupConfigID_Object = MibScalar
sysBootupConfigID = _SysBootupConfigID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 35),
    _SysBootupConfigID_Type()
)
sysBootupConfigID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBootupConfigID.setStatus("current")


class _SysBootupImage_Type(Integer32):
    """Custom type sysBootupImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SysBootupImage_Type.__name__ = "Integer32"
_SysBootupImage_Object = MibScalar
sysBootupImage = _SysBootupImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 1, 36),
    _SysBootupImage_Type()
)
sysBootupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBootupImage.setStatus("current")
_CompanyIpifGroup_ObjectIdentity = ObjectIdentity
companyIpifGroup = _CompanyIpifGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2)
)
_IpifSupportV4V6Info_ObjectIdentity = ObjectIdentity
ipifSupportV4V6Info = _IpifSupportV4V6Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 1),
    _SysIpAddrCfgMode_Type()
)
sysIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddrCfgMode.setStatus("current")
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 2),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("current")
_SysIpSubnetMask_Type = IpAddress
_SysIpSubnetMask_Object = MibScalar
sysIpSubnetMask = _SysIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 3),
    _SysIpSubnetMask_Type()
)
sysIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpSubnetMask.setStatus("current")
_SysGateway_Type = IpAddress
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 4),
    _SysGateway_Type()
)
sysGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGateway.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 5),
    _DhcpOption12Status_Type()
)
dhcpOption12Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12Status.setStatus("current")
_DhcpOption12HostName_Type = OctetString
_DhcpOption12HostName_Object = MibScalar
dhcpOption12HostName = _DhcpOption12HostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 6),
    _DhcpOption12HostName_Type()
)
dhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption12HostName.setStatus("current")
_IpifName_Type = OctetString
_IpifName_Object = MibScalar
ipifName = _IpifName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 7),
    _IpifName_Type()
)
ipifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifName.setStatus("current")
_IpifVLANname_Type = OctetString
_IpifVLANname_Object = MibScalar
ipifVLANname = _IpifVLANname_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 8),
    _IpifVLANname_Type()
)
ipifVLANname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifVLANname.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 9),
    _Ipifv6GlobalStatus_Type()
)
ipifv6GlobalStatus.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 10),
    _Ipifv6DHCPStatus_Type()
)
ipifv6DHCPStatus.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 11),
    _Ipifv6AutolinkloStatus_Type()
)
ipifv6AutolinkloStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipifv6AutolinkloStatus.setStatus("current")
_Ipifv6NSRetransmitTime_Type = Integer32
_Ipifv6NSRetransmitTime_Object = MibScalar
ipifv6NSRetransmitTime = _Ipifv6NSRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 12),
    _Ipifv6NSRetransmitTime_Type()
)
ipifv6NSRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipifv6NSRetransmitTime.setStatus("current")
_Ipifv6DefaultGateway_Type = Ipv6Address
_Ipifv6DefaultGateway_Object = MibScalar
ipifv6DefaultGateway = _Ipifv6DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 13),
    _Ipifv6DefaultGateway_Type()
)
ipifv6DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipifv6DefaultGateway.setStatus("current")
_IpifV6AddressTable_Object = MibTable
ipifV6AddressTable = _IpifV6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 14)
)
if mibBuilder.loadTexts:
    ipifV6AddressTable.setStatus("current")
_IpifV6AddressEntry_Object = MibTableRow
ipifV6AddressEntry = _IpifV6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 14, 1)
)
ipifV6AddressEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "ipifV6AddressMainIndex"),
    (0, "DGS-1100-06ME-AX", "ipifV6AddressIpAddr"),
    (0, "DGS-1100-06ME-AX", "ipifV6AddressIpPrefix"),
)
if mibBuilder.loadTexts:
    ipifV6AddressEntry.setStatus("current")
_IpifV6AddressMainIndex_Type = InterfaceIndex
_IpifV6AddressMainIndex_Object = MibTableColumn
ipifV6AddressMainIndex = _IpifV6AddressMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 14, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 14, 1, 2),
    _IpifV6AddressIpAddr_Type()
)
ipifV6AddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressIpAddr.setStatus("current")


class _IpifV6AddressIpPrefix_Type(Integer32):
    """Custom type ipifV6AddressIpPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IpifV6AddressIpPrefix_Type.__name__ = "Integer32"
_IpifV6AddressIpPrefix_Object = MibTableColumn
ipifV6AddressIpPrefix = _IpifV6AddressIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 14, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 14, 1, 4),
    _IpifV6AddressIpType_Type()
)
ipifV6AddressIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipifV6AddressIpType.setStatus("current")
_IpifV6AddressRowStatus_Type = RowStatus
_IpifV6AddressRowStatus_Object = MibTableColumn
ipifV6AddressRowStatus = _IpifV6AddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 14, 1, 5),
    _IpifV6AddressRowStatus_Type()
)
ipifV6AddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipifV6AddressRowStatus.setStatus("current")


class _DhcpRetryCount_Type(Integer32):
    """Custom type dhcpRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_DhcpRetryCount_Type.__name__ = "Integer32"
_DhcpRetryCount_Object = MibScalar
dhcpRetryCount = _DhcpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 2, 7, 15),
    _DhcpRetryCount_Type()
)
dhcpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRetryCount.setStatus("current")
_CompanyTftpGroup_ObjectIdentity = ObjectIdentity
companyTftpGroup = _CompanyTftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3)
)
_TftpFwTargetGroup_ObjectIdentity = ObjectIdentity
tftpFwTargetGroup = _TftpFwTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 9)
)
_TftpFwTargetServerIpAddress_Type = Ipv6Address
_TftpFwTargetServerIpAddress_Object = MibScalar
tftpFwTargetServerIpAddress = _TftpFwTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 9, 2),
    _TftpFwTargetServerIpType_Type()
)
tftpFwTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFwTargetServerIpType.setStatus("current")
_TftpFwTargetInterfaceName_Type = OctetString
_TftpFwTargetInterfaceName_Object = MibScalar
tftpFwTargetInterfaceName = _TftpFwTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 9, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 9, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 9, 6),
    _TftpFwTargetTftpOperationStatus_Type()
)
tftpFwTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpFwTargetTftpOperationStatus.setStatus("current")
_TftpCfgTargetGroup_ObjectIdentity = ObjectIdentity
tftpCfgTargetGroup = _TftpCfgTargetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 10)
)
_TftpCfgTargetServerIpAddress_Type = Ipv6Address
_TftpCfgTargetServerIpAddress_Object = MibScalar
tftpCfgTargetServerIpAddress = _TftpCfgTargetServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 10, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 10, 2),
    _TftpCfgTargetServerIpType_Type()
)
tftpCfgTargetServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCfgTargetServerIpType.setStatus("current")
_TftpCfgTargetInterfaceName_Type = OctetString
_TftpCfgTargetInterfaceName_Object = MibScalar
tftpCfgTargetInterfaceName = _TftpCfgTargetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 10, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 10, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 3, 10, 6),
    _TftpCfgTargetTftpOperationStatus_Type()
)
tftpCfgTargetTftpOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpCfgTargetTftpOperationStatus.setStatus("current")
_CompanyMiscGroup_ObjectIdentity = ObjectIdentity
companyMiscGroup = _CompanyMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 4, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("current")
_CompanySNMPV3_ObjectIdentity = ObjectIdentity
companySNMPV3 = _CompanySNMPV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 1),
    _SnmpGlobalState_Type()
)
snmpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGlobalState.setStatus("current")
_SnmpV3User_ObjectIdentity = ObjectIdentity
snmpV3User = _SnmpV3User_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2)
)
_SnmpV3UserTable_Object = MibTable
snmpV3UserTable = _SnmpV3UserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    snmpV3UserTable.setStatus("current")
_SnmpV3UserEntry_Object = MibTableRow
snmpV3UserEntry = _SnmpV3UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1)
)
snmpV3UserEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "snmpV3UserName"),
    (0, "DGS-1100-06ME-AX", "snmpV3UserVersion"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 7),
    _SnmpV3UserPrivProtocolPassword_Type()
)
snmpV3UserPrivProtocolPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserPrivProtocolPassword.setStatus("current")
_SnmpV3UserStatus_Type = RowStatus
_SnmpV3UserStatus_Object = MibTableColumn
snmpV3UserStatus = _SnmpV3UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 2, 1, 1, 8),
    _SnmpV3UserStatus_Type()
)
snmpV3UserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3UserStatus.setStatus("current")
_SnmpV3Group_ObjectIdentity = ObjectIdentity
snmpV3Group = _SnmpV3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3)
)
_SnmpV3GroupTable_Object = MibTable
snmpV3GroupTable = _SnmpV3GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    snmpV3GroupTable.setStatus("current")
_SnmpV3GroupEntry_Object = MibTableRow
snmpV3GroupEntry = _SnmpV3GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1)
)
snmpV3GroupEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "snmpV3GroupName"),
    (0, "DGS-1100-06ME-AX", "snmpV3GroupSecurityModel"),
    (0, "DGS-1100-06ME-AX", "snmpV3GroupSecurityLevel"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1, 2),
    _SnmpV3GroupSecurityModel_Type()
)
snmpV3GroupSecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3GroupSecurityModel.setStatus("current")
_SnmpV3GroupSecurityLevel_Type = SnmpSecurityLevel
_SnmpV3GroupSecurityLevel_Object = MibTableColumn
snmpV3GroupSecurityLevel = _SnmpV3GroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1, 6),
    _SnmpV3GroupNotifyViewName_Type()
)
snmpV3GroupNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupNotifyViewName.setStatus("current")
_SnmpV3GroupStatus_Type = RowStatus
_SnmpV3GroupStatus_Object = MibTableColumn
snmpV3GroupStatus = _SnmpV3GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 3, 1, 1, 7),
    _SnmpV3GroupStatus_Type()
)
snmpV3GroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3GroupStatus.setStatus("current")
_SnmpV3ViewTree_ObjectIdentity = ObjectIdentity
snmpV3ViewTree = _SnmpV3ViewTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4)
)
_SnmpV3ViewTreeTable_Object = MibTable
snmpV3ViewTreeTable = _SnmpV3ViewTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    snmpV3ViewTreeTable.setStatus("current")
_SnmpV3ViewTreeEntry_Object = MibTableRow
snmpV3ViewTreeEntry = _SnmpV3ViewTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4, 1, 1)
)
snmpV3ViewTreeEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "snmpV3viewTreeName"),
    (0, "DGS-1100-06ME-AX", "snmpV3viewTreeSubtree"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4, 1, 1, 1),
    _SnmpV3viewTreeName_Type()
)
snmpV3viewTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpV3viewTreeName.setStatus("current")
_SnmpV3viewTreeSubtree_Type = ObjectIdentifier
_SnmpV3viewTreeSubtree_Object = MibTableColumn
snmpV3viewTreeSubtree = _SnmpV3viewTreeSubtree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4, 1, 1, 4),
    _SnmpV3viewTreeType_Type()
)
snmpV3viewTreeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeType.setStatus("current")
_SnmpV3viewTreeStatus_Type = RowStatus
_SnmpV3viewTreeStatus_Object = MibTableColumn
snmpV3viewTreeStatus = _SnmpV3viewTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 4, 1, 1, 5),
    _SnmpV3viewTreeStatus_Type()
)
snmpV3viewTreeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3viewTreeStatus.setStatus("current")
_SnmpV3Community_ObjectIdentity = ObjectIdentity
snmpV3Community = _SnmpV3Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 5)
)
_SnmpV3CommunityTable_Object = MibTable
snmpV3CommunityTable = _SnmpV3CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    snmpV3CommunityTable.setStatus("current")
_SnmpV3CommunityEntry_Object = MibTableRow
snmpV3CommunityEntry = _SnmpV3CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 5, 1, 1)
)
snmpV3CommunityEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "snmpV3CommunityName"),
)
if mibBuilder.loadTexts:
    snmpV3CommunityEntry.setStatus("current")


class _SnmpV3CommunityName_Type(OctetString):
    """Custom type snmpV3CommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SnmpV3CommunityName_Type.__name__ = "OctetString"
_SnmpV3CommunityName_Object = MibTableColumn
snmpV3CommunityName = _SnmpV3CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 5, 1, 1, 2),
    _SnmpV3CommunityPolicy_Type()
)
snmpV3CommunityPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityPolicy.setStatus("current")
_SnmpV3CommunityStatus_Type = RowStatus
_SnmpV3CommunityStatus_Object = MibTableColumn
snmpV3CommunityStatus = _SnmpV3CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 5, 1, 1, 3),
    _SnmpV3CommunityStatus_Type()
)
snmpV3CommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3CommunityStatus.setStatus("current")
_SnmpV3Host_ObjectIdentity = ObjectIdentity
snmpV3Host = _SnmpV3Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6)
)
_SnmpV3HostTable_Object = MibTable
snmpV3HostTable = _SnmpV3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    snmpV3HostTable.setStatus("current")
_SnmpV3HostEntry_Object = MibTableRow
snmpV3HostEntry = _SnmpV3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2, 1)
)
snmpV3HostEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "snmpV3HostAddress"),
    (0, "DGS-1100-06ME-AX", "snmpV3IPType"),
)
if mibBuilder.loadTexts:
    snmpV3HostEntry.setStatus("current")
_SnmpV3HostAddress_Type = Ipv6Address
_SnmpV3HostAddress_Object = MibTableColumn
snmpV3HostAddress = _SnmpV3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2, 1, 4),
    _SnmpV3HostVersion_Type()
)
snmpV3HostVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostVersion.setStatus("current")
_SnmpV3HostInterfaceName_Type = OctetString
_SnmpV3HostInterfaceName_Object = MibTableColumn
snmpV3HostInterfaceName = _SnmpV3HostInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2, 1, 5),
    _SnmpV3HostInterfaceName_Type()
)
snmpV3HostInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostInterfaceName.setStatus("current")
_SnmpV3HostStatus_Type = RowStatus
_SnmpV3HostStatus_Object = MibTableColumn
snmpV3HostStatus = _SnmpV3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 6, 2, 1, 6),
    _SnmpV3HostStatus_Type()
)
snmpV3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpV3HostStatus.setStatus("current")
_SnmpV3EngineID_Type = SnmpEngineID
_SnmpV3EngineID_Object = MibScalar
snmpV3EngineID = _SnmpV3EngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 7),
    _SnmpV3EngineID_Type()
)
snmpV3EngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3EngineID.setStatus("current")
_SnmpV3Trap_ObjectIdentity = ObjectIdentity
snmpV3Trap = _SnmpV3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 8)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 8, 1),
    _SnmpV3TrapSNMPAuthentication_Type()
)
snmpV3TrapSNMPAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapSNMPAuthentication.setStatus("current")


class _SnmpV3TrapColdStart_Type(Integer32):
    """Custom type snmpV3TrapColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapColdStart_Type.__name__ = "Integer32"
_SnmpV3TrapColdStart_Object = MibScalar
snmpV3TrapColdStart = _SnmpV3TrapColdStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 8, 2),
    _SnmpV3TrapColdStart_Type()
)
snmpV3TrapColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapColdStart.setStatus("current")


class _SnmpV3TrapWarmStart_Type(Integer32):
    """Custom type snmpV3TrapWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapWarmStart_Type.__name__ = "Integer32"
_SnmpV3TrapWarmStart_Object = MibScalar
snmpV3TrapWarmStart = _SnmpV3TrapWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 8, 3),
    _SnmpV3TrapWarmStart_Type()
)
snmpV3TrapWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapWarmStart.setStatus("current")


class _SnmpV3TrapLinkUpDown_Type(Integer32):
    """Custom type snmpV3TrapLinkUpDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapLinkUpDown_Type.__name__ = "Integer32"
_SnmpV3TrapLinkUpDown_Object = MibScalar
snmpV3TrapLinkUpDown = _SnmpV3TrapLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 8, 4),
    _SnmpV3TrapLinkUpDown_Type()
)
snmpV3TrapLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapLinkUpDown.setStatus("current")


class _SnmpV3TrapPortSecurity_Type(Integer32):
    """Custom type snmpV3TrapPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpV3TrapPortSecurity_Type.__name__ = "Integer32"
_SnmpV3TrapPortSecurity_Object = MibScalar
snmpV3TrapPortSecurity = _SnmpV3TrapPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 8, 12),
    _SnmpV3TrapPortSecurity_Type()
)
snmpV3TrapPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapPortSecurity.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 5, 8, 14),
    _SnmpV3TrapLBD_Type()
)
snmpV3TrapLBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3TrapLBD.setStatus("current")
_CompanyDot1qVlanGroup_ObjectIdentity = ObjectIdentity
companyDot1qVlanGroup = _CompanyDot1qVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 5),
    _Dot1qVlanAsyOnOff_Type()
)
dot1qVlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanAsyOnOff.setStatus("current")
_Dot1qVlanTable_Object = MibTable
dot1qVlanTable = _Dot1qVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 6)
)
if mibBuilder.loadTexts:
    dot1qVlanTable.setStatus("current")
_Dot1qVlanEntry_Object = MibTableRow
dot1qVlanEntry = _Dot1qVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 6, 1)
)
dot1qVlanEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "dot1qVlanName"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 6, 1, 1),
    _Dot1qVlanName_Type()
)
dot1qVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanName.setStatus("current")
_Dot1qVlanEgressPorts_Type = PortList
_Dot1qVlanEgressPorts_Object = MibTableColumn
dot1qVlanEgressPorts = _Dot1qVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 6, 1, 2),
    _Dot1qVlanEgressPorts_Type()
)
dot1qVlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanEgressPorts.setStatus("current")
_Dot1qVlanForbiddenPorts_Type = PortList
_Dot1qVlanForbiddenPorts_Object = MibTableColumn
dot1qVlanForbiddenPorts = _Dot1qVlanForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 6, 1, 3),
    _Dot1qVlanForbiddenPorts_Type()
)
dot1qVlanForbiddenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanForbiddenPorts.setStatus("current")
_Dot1qVlanUntaggedPorts_Type = PortList
_Dot1qVlanUntaggedPorts_Object = MibTableColumn
dot1qVlanUntaggedPorts = _Dot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 6, 1, 4),
    _Dot1qVlanUntaggedPorts_Type()
)
dot1qVlanUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanUntaggedPorts.setStatus("current")
_Dot1qVlanRowStatus_Type = RowStatus
_Dot1qVlanRowStatus_Object = MibTableColumn
dot1qVlanRowStatus = _Dot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 6, 1, 6),
    _Dot1qVlanRowStatus_Type()
)
dot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanRowStatus.setStatus("current")
_Dot1qVlanPortTable_Object = MibTable
dot1qVlanPortTable = _Dot1qVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 7)
)
if mibBuilder.loadTexts:
    dot1qVlanPortTable.setStatus("current")
_Dot1qVlanPortEntry_Object = MibTableRow
dot1qVlanPortEntry = _Dot1qVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 7, 1)
)
if mibBuilder.loadTexts:
    dot1qVlanPortEntry.setStatus("current")


class _Dot1qVlanPvid_Type(VlanIndex):
    """Custom type dot1qVlanPvid based on VlanIndex"""
    defaultValue = 1


_Dot1qVlanPvid_Object = MibTableColumn
dot1qVlanPvid = _Dot1qVlanPvid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 7, 1, 1),
    _Dot1qVlanPvid_Type()
)
dot1qVlanPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPvid.setStatus("current")


class _Dot1qVlanPVIDAutoAssignOnOff_Type(Integer32):
    """Custom type dot1qVlanPVIDAutoAssignOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Dot1qVlanPVIDAutoAssignOnOff_Type.__name__ = "Integer32"
_Dot1qVlanPVIDAutoAssignOnOff_Object = MibScalar
dot1qVlanPVIDAutoAssignOnOff = _Dot1qVlanPVIDAutoAssignOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 7, 9),
    _Dot1qVlanPVIDAutoAssignOnOff_Type()
)
dot1qVlanPVIDAutoAssignOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qVlanPVIDAutoAssignOnOff.setStatus("current")
_CompanyStaticMAC_ObjectIdentity = ObjectIdentity
companyStaticMAC = _CompanyStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 1),
    _StaticDisableAutoLearn_Type()
)
staticDisableAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDisableAutoLearn.setStatus("current")
_StaticAutoLearningList_Type = PortList
_StaticAutoLearningList_Object = MibScalar
staticAutoLearningList = _StaticAutoLearningList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 2),
    _StaticAutoLearningList_Type()
)
staticAutoLearningList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticAutoLearningList.setStatus("current")
_StaticTable_Object = MibTable
staticTable = _StaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 3)
)
if mibBuilder.loadTexts:
    staticTable.setStatus("current")
_StaticEntry_Object = MibTableRow
staticEntry = _StaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 3, 1)
)
staticEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "staticVlanID"),
    (0, "DGS-1100-06ME-AX", "staticMac"),
    (0, "DGS-1100-06ME-AX", "staticPort"),
)
if mibBuilder.loadTexts:
    staticEntry.setStatus("current")


class _StaticVlanID_Type(Integer32):
    """Custom type staticVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_StaticVlanID_Type.__name__ = "Integer32"
_StaticVlanID_Object = MibTableColumn
staticVlanID = _StaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 3, 1, 1),
    _StaticVlanID_Type()
)
staticVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticVlanID.setStatus("current")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 3, 1, 2),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMac.setStatus("current")


class _StaticPort_Type(Integer32):
    """Custom type staticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_StaticPort_Type.__name__ = "Integer32"
_StaticPort_Object = MibTableColumn
staticPort = _StaticPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 3, 1, 3),
    _StaticPort_Type()
)
staticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticPort.setStatus("current")
_StaticStatus_Type = RowStatus
_StaticStatus_Object = MibTableColumn
staticStatus = _StaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 3, 1, 4),
    _StaticStatus_Type()
)
staticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticStatus.setStatus("current")
_AutoFdbTable_Object = MibTable
autoFdbTable = _AutoFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    autoFdbTable.setStatus("current")
_AutoFdbEntry_Object = MibTableRow
autoFdbEntry = _AutoFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4, 1)
)
autoFdbEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "autoFdbIPAddress"),
)
if mibBuilder.loadTexts:
    autoFdbEntry.setStatus("current")
_AutoFdbIPAddress_Type = IpAddress
_AutoFdbIPAddress_Object = MibTableColumn
autoFdbIPAddress = _AutoFdbIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4, 1, 1),
    _AutoFdbIPAddress_Type()
)
autoFdbIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFdbIPAddress.setStatus("current")
_AutoFdbVlanID_Type = Integer32
_AutoFdbVlanID_Object = MibTableColumn
autoFdbVlanID = _AutoFdbVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4, 1, 2),
    _AutoFdbVlanID_Type()
)
autoFdbVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFdbVlanID.setStatus("current")
_AutoFdbMacAddress_Type = MacAddress
_AutoFdbMacAddress_Object = MibTableColumn
autoFdbMacAddress = _AutoFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4, 1, 3),
    _AutoFdbMacAddress_Type()
)
autoFdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFdbMacAddress.setStatus("current")
_AutoFdbPort_Type = Integer32
_AutoFdbPort_Object = MibTableColumn
autoFdbPort = _AutoFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4, 1, 4),
    _AutoFdbPort_Type()
)
autoFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFdbPort.setStatus("current")
_AutoFdbTimeStamp_Type = Integer32
_AutoFdbTimeStamp_Object = MibTableColumn
autoFdbTimeStamp = _AutoFdbTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4, 1, 5),
    _AutoFdbTimeStamp_Type()
)
autoFdbTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFdbTimeStamp.setStatus("current")
_AutoFdbStatus_Type = RowStatus
_AutoFdbStatus_Object = MibTableColumn
autoFdbStatus = _AutoFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 9, 4, 1, 6),
    _AutoFdbStatus_Type()
)
autoFdbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFdbStatus.setStatus("current")
_CompanyIgsGroup_ObjectIdentity = ObjectIdentity
companyIgsGroup = _CompanyIgsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10)
)
_IgsSystem_ObjectIdentity = ObjectIdentity
igsSystem = _IgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 1, 9),
    _IgsReportToAllPort_Type()
)
igsReportToAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsReportToAllPort.setStatus("current")
_IgsVlan_ObjectIdentity = ObjectIdentity
igsVlan = _IgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3)
)
_IgsVlanRouterTable_Object = MibTable
igsVlanRouterTable = _IgsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    igsVlanRouterTable.setStatus("current")
_IgsVlanRouterEntry_Object = MibTableRow
igsVlanRouterEntry = _IgsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 3, 1)
)
igsVlanRouterEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "igsVlanRouterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 3, 1, 1),
    _IgsVlanRouterVlanId_Type()
)
igsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterVlanId.setStatus("current")
_IgsVlanRouterPortList_Type = PortList
_IgsVlanRouterPortList_Object = MibTableColumn
igsVlanRouterPortList = _IgsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 3, 1, 2),
    _IgsVlanRouterPortList_Type()
)
igsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterPortList.setStatus("current")
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("current")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "igsVlanFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1, 5),
    _IgsVlanQueryInterval_Type()
)
igsVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanQueryInterval.setStatus("current")
_IgsVlanRtrPortList_Type = PortList
_IgsVlanRtrPortList_Object = MibTableColumn
igsVlanRtrPortList = _IgsVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 4, 1, 8),
    _IgsVlanFastLeave_Type()
)
igsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFastLeave.setStatus("current")
_IgsVlanMulticastGroupTable_Object = MibTable
igsVlanMulticastGroupTable = _IgsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 5)
)
if mibBuilder.loadTexts:
    igsVlanMulticastGroupTable.setStatus("current")
_IgsVlanMulticastGroupEntry_Object = MibTableRow
igsVlanMulticastGroupEntry = _IgsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 5, 1)
)
igsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "igsVlanMulticastGroupVlanId"),
    (0, "DGS-1100-06ME-AX", "igsVlanMulticastGroupIpAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 5, 1, 1),
    _IgsVlanMulticastGroupVlanId_Type()
)
igsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupVlanId.setStatus("current")
_IgsVlanMulticastGroupIpAddress_Type = InetAddress
_IgsVlanMulticastGroupIpAddress_Object = MibTableColumn
igsVlanMulticastGroupIpAddress = _IgsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 5, 1, 2),
    _IgsVlanMulticastGroupIpAddress_Type()
)
igsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupIpAddress.setStatus("current")
_IgsVlanMulticastGroupMacAddress_Type = MacAddress
_IgsVlanMulticastGroupMacAddress_Object = MibTableColumn
igsVlanMulticastGroupMacAddress = _IgsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 5, 1, 3),
    _IgsVlanMulticastGroupMacAddress_Type()
)
igsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupMacAddress.setStatus("current")
_IgsVlanMulticastGroupPortList_Type = PortList
_IgsVlanMulticastGroupPortList_Object = MibTableColumn
igsVlanMulticastGroupPortList = _IgsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 3, 5, 1, 4),
    _IgsVlanMulticastGroupPortList_Type()
)
igsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMulticastGroupPortList.setStatus("current")
_IgsAccessAuth_ObjectIdentity = ObjectIdentity
igsAccessAuth = _IgsAccessAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 5)
)
_IgsAccessAuthTable_Object = MibTable
igsAccessAuthTable = _IgsAccessAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    igsAccessAuthTable.setStatus("current")
_IgsAccessAuthEntry_Object = MibTableRow
igsAccessAuthEntry = _IgsAccessAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 5, 1, 1)
)
igsAccessAuthEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "igsAccessAuthPortIndex"),
)
if mibBuilder.loadTexts:
    igsAccessAuthEntry.setStatus("current")


class _IgsAccessAuthPortIndex_Type(Integer32):
    """Custom type igsAccessAuthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_IgsAccessAuthPortIndex_Type.__name__ = "Integer32"
_IgsAccessAuthPortIndex_Object = MibTableColumn
igsAccessAuthPortIndex = _IgsAccessAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 5, 1, 1, 2),
    _IgsAccessAuthState_Type()
)
igsAccessAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsAccessAuthState.setStatus("current")
_IgsHost_ObjectIdentity = ObjectIdentity
igsHost = _IgsHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 6)
)
_IgsHostTable_Object = MibTable
igsHostTable = _IgsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 6, 1)
)
if mibBuilder.loadTexts:
    igsHostTable.setStatus("current")
_IgsHostEntry_Object = MibTableRow
igsHostEntry = _IgsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 6, 1, 1)
)
igsHostEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "igsHostTableVLANID"),
    (0, "DGS-1100-06ME-AX", "igsHostTableGroupAddress"),
    (0, "DGS-1100-06ME-AX", "igsHostTablePort"),
    (0, "DGS-1100-06ME-AX", "igsHostTableHostIPAddress"),
)
if mibBuilder.loadTexts:
    igsHostEntry.setStatus("current")


class _IgsHostTableVLANID_Type(Integer32):
    """Custom type igsHostTableVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsHostTableVLANID_Type.__name__ = "Integer32"
_IgsHostTableVLANID_Object = MibTableColumn
igsHostTableVLANID = _IgsHostTableVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 6, 1, 1, 1),
    _IgsHostTableVLANID_Type()
)
igsHostTableVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableVLANID.setStatus("current")
_IgsHostTableGroupAddress_Type = InetAddress
_IgsHostTableGroupAddress_Object = MibTableColumn
igsHostTableGroupAddress = _IgsHostTableGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 6, 1, 1, 2),
    _IgsHostTableGroupAddress_Type()
)
igsHostTableGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableGroupAddress.setStatus("current")


class _IgsHostTablePort_Type(Integer32):
    """Custom type igsHostTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_IgsHostTablePort_Type.__name__ = "Integer32"
_IgsHostTablePort_Object = MibTableColumn
igsHostTablePort = _IgsHostTablePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 6, 1, 1, 3),
    _IgsHostTablePort_Type()
)
igsHostTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTablePort.setStatus("current")
_IgsHostTableHostIPAddress_Type = InetAddress
_IgsHostTableHostIPAddress_Object = MibTableColumn
igsHostTableHostIPAddress = _IgsHostTableHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 10, 6, 1, 1, 4),
    _IgsHostTableHostIPAddress_Type()
)
igsHostTableHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostTableHostIPAddress.setStatus("current")
_CompanyQoSGroup_ObjectIdentity = ObjectIdentity
companyQoSGroup = _CompanyQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12)
)


class _QosMode_Type(Integer32):
    """Custom type qosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 1),
          ("dscp", 2),
          ("portbase", 4))
    )


_QosMode_Type.__name__ = "Integer32"
_QosMode_Object = MibScalar
qosMode = _QosMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 2),
    _QueuingMechanism_Type()
)
queuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMechanism.setStatus("current")
_QosQ1p_ObjectIdentity = ObjectIdentity
qosQ1p = _QosQ1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 3)
)
_Dot1pPortTable_Object = MibTable
dot1pPortTable = _Dot1pPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    dot1pPortTable.setStatus("current")
_Dot1pPortEntry_Object = MibTableRow
dot1pPortEntry = _Dot1pPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 3, 1, 1)
)
dot1pPortEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "dot1pPortIndex"),
)
if mibBuilder.loadTexts:
    dot1pPortEntry.setStatus("current")


class _Dot1pPortIndex_Type(Integer32):
    """Custom type dot1pPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Dot1pPortIndex_Type.__name__ = "Integer32"
_Dot1pPortIndex_Object = MibTableColumn
dot1pPortIndex = _Dot1pPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 3, 1, 1, 2),
    _Dot1pPortPriority_Type()
)
dot1pPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1pPortPriority.setStatus("current")
_QosDiffServ_ObjectIdentity = ObjectIdentity
qosDiffServ = _QosDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 1),
    _QosDiffServEnable_Type()
)
qosDiffServEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDiffServEnable.setStatus("current")
_QosDiffServTypeGroup_ObjectIdentity = ObjectIdentity
qosDiffServTypeGroup = _QosDiffServTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 21),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 23),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 24),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 25),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 26),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 27),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 28),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 29),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 30),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 31),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 32),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 33),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 34),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 35),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 36),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 37),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 38),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 39),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 40),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 41),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 42),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 43),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 44),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 45),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 46),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 47),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 48),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 49),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 50),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 51),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 52),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 53),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 54),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 55),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 56),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 57),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 58),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 59),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 60),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 61),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 62),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 63),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 4, 2, 64),
    _QosDiffServType63_Type()
)
qosDiffServType63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosDiffServType63.setStatus("current")
_QosAclPrioritySettings_ObjectIdentity = ObjectIdentity
qosAclPrioritySettings = _QosAclPrioritySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8)
)
_AclQosTable_Object = MibTable
aclQosTable = _AclQosTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8, 2)
)
if mibBuilder.loadTexts:
    aclQosTable.setStatus("current")
_AclQosEntry_Object = MibTableRow
aclQosEntry = _AclQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8, 2, 1)
)
aclQosEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aclQosIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8, 2, 1, 1),
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
            7
        )
    )
    namedValues = NamedValues(
        ("ipv6traffic-class", 7)
    )


_AclQosType_Type.__name__ = "Integer32"
_AclQosType_Object = MibTableColumn
aclQosType = _AclQosType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8, 2, 1, 2),
    _AclQosType_Type()
)
aclQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosType.setStatus("current")


class _AclQosIP6TC_Type(Integer32):
    """Custom type aclQosIP6TC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclQosIP6TC_Type.__name__ = "Integer32"
_AclQosIP6TC_Object = MibTableColumn
aclQosIP6TC = _AclQosIP6TC_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8, 2, 1, 98),
    _AclQosAssignPriority_Type()
)
aclQosAssignPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosAssignPriority.setStatus("current")
_AclQosStatus_Type = RowStatus
_AclQosStatus_Object = MibTableColumn
aclQosStatus = _AclQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 12, 8, 2, 1, 99),
    _AclQosStatus_Type()
)
aclQosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclQosStatus.setStatus("current")
_CompanyTrafficMgmt_ObjectIdentity = ObjectIdentity
companyTrafficMgmt = _CompanyTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13)
)
_BandwidthCtrlSettings_ObjectIdentity = ObjectIdentity
bandwidthCtrlSettings = _BandwidthCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1)
)
_BandwidthCtrlTable_Object = MibTable
bandwidthCtrlTable = _BandwidthCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    bandwidthCtrlTable.setStatus("current")
_BandwidthCtrlEntry_Object = MibTableRow
bandwidthCtrlEntry = _BandwidthCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1, 2, 1)
)
bandwidthCtrlEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "bandwidthCtrlIndex"),
)
if mibBuilder.loadTexts:
    bandwidthCtrlEntry.setStatus("current")


class _BandwidthCtrlIndex_Type(Integer32):
    """Custom type bandwidthCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_BandwidthCtrlIndex_Type.__name__ = "Integer32"
_BandwidthCtrlIndex_Object = MibTableColumn
bandwidthCtrlIndex = _BandwidthCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1, 2, 1, 2),
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
        ValueRangeConstraint(64, 1000000),
    )


_BandwidthCtrlRxThreshold_Type.__name__ = "Integer32"
_BandwidthCtrlRxThreshold_Object = MibTableColumn
bandwidthCtrlRxThreshold = _BandwidthCtrlRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1, 2, 1, 3),
    _BandwidthCtrlRxThreshold_Type()
)
bandwidthCtrlRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthCtrlRxThreshold.setStatus("current")
_BandwidthEffecTxThreshold_Type = Integer32
_BandwidthEffecTxThreshold_Object = MibTableColumn
bandwidthEffecTxThreshold = _BandwidthEffecTxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1, 2, 1, 4),
    _BandwidthEffecTxThreshold_Type()
)
bandwidthEffecTxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthEffecTxThreshold.setStatus("current")
_BandwidthEffecRxThreshold_Type = Integer32
_BandwidthEffecRxThreshold_Object = MibTableColumn
bandwidthEffecRxThreshold = _BandwidthEffecRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 1, 2, 1, 5),
    _BandwidthEffecRxThreshold_Type()
)
bandwidthEffecRxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthEffecRxThreshold.setStatus("current")
_TrafficCtrlSettings_ObjectIdentity = ObjectIdentity
trafficCtrlSettings = _TrafficCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 1),
    _TrafficCtrlTrap_Type()
)
trafficCtrlTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlTrap.setStatus("current")
_TrafficCtrlTable_Object = MibTable
trafficCtrlTable = _TrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2)
)
if mibBuilder.loadTexts:
    trafficCtrlTable.setStatus("current")
_TrafficCtrlEntry_Object = MibTableRow
trafficCtrlEntry = _TrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2, 1)
)
trafficCtrlEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "trafficCtrlIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 2, 1, 6),
    _TrafficCtrlTimeInterval_Type()
)
trafficCtrlTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlTimeInterval.setStatus("current")


class _TrafficCtrlAutoRecoverTime_Type(Integer32):
    """Custom type trafficCtrlAutoRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrafficCtrlAutoRecoverTime_Type.__name__ = "Integer32"
_TrafficCtrlAutoRecoverTime_Object = MibScalar
trafficCtrlAutoRecoverTime = _TrafficCtrlAutoRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 13, 4, 3),
    _TrafficCtrlAutoRecoverTime_Type()
)
trafficCtrlAutoRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficCtrlAutoRecoverTime.setStatus("current")
_CompanySecurity_ObjectIdentity = ObjectIdentity
companySecurity = _CompanySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14)
)
_SecurityTrustedHost_ObjectIdentity = ObjectIdentity
securityTrustedHost = _SecurityTrustedHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 1),
    _TrustedHostStatus_Type()
)
trustedHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostStatus.setStatus("current")
_Ipv4trustedHostTable_Object = MibTable
ipv4trustedHostTable = _Ipv4trustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    ipv4trustedHostTable.setStatus("obsolete")
_Ipv4trustedHostEntry_Object = MibTableRow
ipv4trustedHostEntry = _Ipv4trustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 2, 1)
)
ipv4trustedHostEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "ipv4trustedHostIpAddr"),
    (0, "DGS-1100-06ME-AX", "ipv4trustedHostIpMask"),
)
if mibBuilder.loadTexts:
    ipv4trustedHostEntry.setStatus("obsolete")
_Ipv4trustedHostIpAddr_Type = IpAddress
_Ipv4trustedHostIpAddr_Object = MibTableColumn
ipv4trustedHostIpAddr = _Ipv4trustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 2, 1, 1),
    _Ipv4trustedHostIpAddr_Type()
)
ipv4trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4trustedHostIpAddr.setStatus("obsolete")
_Ipv4trustedHostIpMask_Type = IpAddress
_Ipv4trustedHostIpMask_Object = MibTableColumn
ipv4trustedHostIpMask = _Ipv4trustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 2, 1, 2),
    _Ipv4trustedHostIpMask_Type()
)
ipv4trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4trustedHostIpMask.setStatus("obsolete")
_Ipv4trustedHostRowStatus_Type = RowStatus
_Ipv4trustedHostRowStatus_Object = MibTableColumn
ipv4trustedHostRowStatus = _Ipv4trustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 2, 1, 3),
    _Ipv4trustedHostRowStatus_Type()
)
ipv4trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4trustedHostRowStatus.setStatus("obsolete")
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("current")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 3, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "trustedHostIPType"),
    (0, "DGS-1100-06ME-AX", "trustedHostIpAddr"),
    (0, "DGS-1100-06ME-AX", "trustedHostIpMask"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 3, 1, 1),
    _TrustedHostIPType_Type()
)
trustedHostIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIPType.setStatus("current")
_TrustedHostIpAddr_Type = Ipv6Address
_TrustedHostIpAddr_Object = MibTableColumn
trustedHostIpAddr = _TrustedHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 3, 1, 2),
    _TrustedHostIpAddr_Type()
)
trustedHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpAddr.setStatus("current")
_TrustedHostIpMask_Type = Ipv6Address
_TrustedHostIpMask_Object = MibTableColumn
trustedHostIpMask = _TrustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 3, 1, 3),
    _TrustedHostIpMask_Type()
)
trustedHostIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostIpMask.setStatus("current")
_TrustedHostRowStatus_Type = RowStatus
_TrustedHostRowStatus_Object = MibTableColumn
trustedHostRowStatus = _TrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 1, 3, 1, 4),
    _TrustedHostRowStatus_Type()
)
trustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trustedHostRowStatus.setStatus("current")
_SecurityPortSecurity_ObjectIdentity = ObjectIdentity
securityPortSecurity = _SecurityPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2)
)
_PortSecTable_Object = MibTable
portSecTable = _PortSecTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    portSecTable.setStatus("current")
_PortSecEntry_Object = MibTableRow
portSecEntry = _PortSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 1, 1)
)
portSecEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "portSecIndex"),
)
if mibBuilder.loadTexts:
    portSecEntry.setStatus("current")


class _PortSecIndex_Type(Integer32):
    """Custom type portSecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PortSecIndex_Type.__name__ = "Integer32"
_PortSecIndex_Object = MibTableColumn
portSecIndex = _PortSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 1, 1, 3),
    _PortSecMLA_Type()
)
portSecMLA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMLA.setStatus("current")


class _PortSecLockAddrMode_Type(Integer32):
    """Custom type portSecLockAddrMode based on Integer32"""
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


_PortSecLockAddrMode_Type.__name__ = "Integer32"
_PortSecLockAddrMode_Object = MibTableColumn
portSecLockAddrMode = _PortSecLockAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 1, 1, 4),
    _PortSecLockAddrMode_Type()
)
portSecLockAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecLockAddrMode.setStatus("current")
_PortSecFDBPermanentTable_Object = MibTable
portSecFDBPermanentTable = _PortSecFDBPermanentTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 2)
)
if mibBuilder.loadTexts:
    portSecFDBPermanentTable.setStatus("current")
_PortSecFDBPermanentEntry_Object = MibTableRow
portSecFDBPermanentEntry = _PortSecFDBPermanentEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 2, 1)
)
portSecFDBPermanentEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "portSecFDBPermPort"),
    (0, "DGS-1100-06ME-AX", "portSecFDBPermIndex"),
)
if mibBuilder.loadTexts:
    portSecFDBPermanentEntry.setStatus("current")


class _PortSecFDBPermIndex_Type(Integer32):
    """Custom type portSecFDBPermIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PortSecFDBPermIndex_Type.__name__ = "Integer32"
_PortSecFDBPermIndex_Object = MibTableColumn
portSecFDBPermIndex = _PortSecFDBPermIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 2, 1, 1),
    _PortSecFDBPermIndex_Type()
)
portSecFDBPermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermIndex.setStatus("current")
_PortSecFDBPermVlanID_Type = Integer32
_PortSecFDBPermVlanID_Object = MibTableColumn
portSecFDBPermVlanID = _PortSecFDBPermVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 2, 1, 2),
    _PortSecFDBPermVlanID_Type()
)
portSecFDBPermVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermVlanID.setStatus("current")
_PortSecFDBPermMac_Type = MacAddress
_PortSecFDBPermMac_Object = MibTableColumn
portSecFDBPermMac = _PortSecFDBPermMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 2, 1, 3),
    _PortSecFDBPermMac_Type()
)
portSecFDBPermMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermMac.setStatus("current")


class _PortSecFDBPermPort_Type(Integer32):
    """Custom type portSecFDBPermPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PortSecFDBPermPort_Type.__name__ = "Integer32"
_PortSecFDBPermPort_Object = MibTableColumn
portSecFDBPermPort = _PortSecFDBPermPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 2, 2, 1, 4),
    _PortSecFDBPermPort_Type()
)
portSecFDBPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecFDBPermPort.setStatus("current")
_SecurityTrafficSeg_ObjectIdentity = ObjectIdentity
securityTrafficSeg = _SecurityTrafficSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 9)
)
_TrafficSegTable_Object = MibTable
trafficSegTable = _TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 9, 1)
)
if mibBuilder.loadTexts:
    trafficSegTable.setStatus("current")
_TrafficSegEntry_Object = MibTableRow
trafficSegEntry = _TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 9, 1, 1)
)
trafficSegEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "trafficSegIfIndex"),
)
if mibBuilder.loadTexts:
    trafficSegEntry.setStatus("current")
_TrafficSegIfIndex_Type = InterfaceIndex
_TrafficSegIfIndex_Object = MibTableColumn
trafficSegIfIndex = _TrafficSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 9, 1, 1, 1),
    _TrafficSegIfIndex_Type()
)
trafficSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficSegIfIndex.setStatus("current")
_TrafficSegMemberList_Type = PortList
_TrafficSegMemberList_Object = MibTableColumn
trafficSegMemberList = _TrafficSegMemberList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 9, 1, 1, 2),
    _TrafficSegMemberList_Type()
)
trafficSegMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficSegMemberList.setStatus("current")
_SecurityAAC_ObjectIdentity = ObjectIdentity
securityAAC = _SecurityAAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 3),
    _AacAuthParamAttempt_Type()
)
aacAuthParamAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAuthParamAttempt.setStatus("current")
_AacAPAuthMethodGroup_ObjectIdentity = ObjectIdentity
aacAPAuthMethodGroup = _AacAPAuthMethodGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 4)
)
_AacAPLoginMethod_ObjectIdentity = ObjectIdentity
aacAPLoginMethod = _AacAPLoginMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 4, 1)
)


class _AacAPTelnetLoginMethod_Type(Integer32):
    """Custom type aacAPTelnetLoginMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPTelnetLoginMethod_Type.__name__ = "Integer32"
_AacAPTelnetLoginMethod_Object = MibScalar
aacAPTelnetLoginMethod = _AacAPTelnetLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 4, 1, 2),
    _AacAPTelnetLoginMethod_Type()
)
aacAPTelnetLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPTelnetLoginMethod.setStatus("current")


class _AacAPHttpLoginMethod_Type(Integer32):
    """Custom type aacAPHttpLoginMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPHttpLoginMethod_Type.__name__ = "Integer32"
_AacAPHttpLoginMethod_Object = MibScalar
aacAPHttpLoginMethod = _AacAPHttpLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 4, 1, 4),
    _AacAPHttpLoginMethod_Type()
)
aacAPHttpLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPHttpLoginMethod.setStatus("current")
_AacAPEnableMethod_ObjectIdentity = ObjectIdentity
aacAPEnableMethod = _AacAPEnableMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 4, 2)
)


class _AacAPTelnetEnableMethod_Type(Integer32):
    """Custom type aacAPTelnetEnableMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPTelnetEnableMethod_Type.__name__ = "Integer32"
_AacAPTelnetEnableMethod_Object = MibScalar
aacAPTelnetEnableMethod = _AacAPTelnetEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 4, 2, 2),
    _AacAPTelnetEnableMethod_Type()
)
aacAPTelnetEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPTelnetEnableMethod.setStatus("current")


class _AacAPHttpEnableMethod_Type(Integer32):
    """Custom type aacAPHttpEnableMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacAPHttpEnableMethod_Type.__name__ = "Integer32"
_AacAPHttpEnableMethod_Object = MibScalar
aacAPHttpEnableMethod = _AacAPHttpEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 4, 2, 4),
    _AacAPHttpEnableMethod_Type()
)
aacAPHttpEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacAPHttpEnableMethod.setStatus("current")
_AacServerGroupTable_Object = MibTable
aacServerGroupTable = _AacServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 5)
)
if mibBuilder.loadTexts:
    aacServerGroupTable.setStatus("current")
_AacServerGroupEntry_Object = MibTableRow
aacServerGroupEntry = _AacServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 5, 1)
)
aacServerGroupEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aacServerGroupIndex"),
)
if mibBuilder.loadTexts:
    aacServerGroupEntry.setStatus("current")


class _AacServerGroupIndex_Type(Integer32):
    """Custom type aacServerGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9),
    )


_AacServerGroupIndex_Type.__name__ = "Integer32"
_AacServerGroupIndex_Object = MibTableColumn
aacServerGroupIndex = _AacServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 5, 1, 1),
    _AacServerGroupIndex_Type()
)
aacServerGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacServerGroupIndex.setStatus("current")


class _AacServerGroupName_Type(OctetString):
    """Custom type aacServerGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacServerGroupName_Type.__name__ = "OctetString"
_AacServerGroupName_Object = MibTableColumn
aacServerGroupName = _AacServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 5, 1, 2),
    _AacServerGroupName_Type()
)
aacServerGroupName.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 5, 1, 3),
    _AacServersInGroup_Type()
)
aacServersInGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServersInGroup.setStatus("current")
_AacServerGroupRowStatus_Type = RowStatus
_AacServerGroupRowStatus_Object = MibTableColumn
aacServerGroupRowStatus = _AacServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 5, 1, 4),
    _AacServerGroupRowStatus_Type()
)
aacServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacServerGroupRowStatus.setStatus("current")
_AacServerInfoTable_Object = MibTable
aacServerInfoTable = _AacServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7)
)
if mibBuilder.loadTexts:
    aacServerInfoTable.setStatus("current")
_AacServerInfoEntry_Object = MibTableRow
aacServerInfoEntry = _AacServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1)
)
aacServerInfoEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aacServerIndex"),
)
if mibBuilder.loadTexts:
    aacServerInfoEntry.setStatus("current")


class _AacServerIndex_Type(Integer32):
    """Custom type aacServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AacServerIndex_Type.__name__ = "Integer32"
_AacServerIndex_Object = MibTableColumn
aacServerIndex = _AacServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 1),
    _AacServerIndex_Type()
)
aacServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacServerIndex.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 2),
    _AacServerIPType_Type()
)
aacServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerIPType.setStatus("current")
_AacServerIPAddr_Type = Ipv6Address
_AacServerIPAddr_Object = MibTableColumn
aacServerIPAddr = _AacServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 3),
    _AacServerIPAddr_Type()
)
aacServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerIPAddr.setStatus("current")
_AacServerInterfaceName_Type = OctetString
_AacServerInterfaceName_Object = MibTableColumn
aacServerInterfaceName = _AacServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 4),
    _AacServerInterfaceName_Type()
)
aacServerInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacServerInterfaceName.setStatus("current")


class _AacServerAuthProtocol_Type(Integer32):
    """Custom type aacServerAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 2),
          ("tacacsPlus", 1))
    )


_AacServerAuthProtocol_Type.__name__ = "Integer32"
_AacServerAuthProtocol_Object = MibTableColumn
aacServerAuthProtocol = _AacServerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 5),
    _AacServerAuthProtocol_Type()
)
aacServerAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerAuthProtocol.setStatus("current")


class _AacServerAuthPort_Type(Integer32):
    """Custom type aacServerAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AacServerAuthPort_Type.__name__ = "Integer32"
_AacServerAuthPort_Object = MibTableColumn
aacServerAuthPort = _AacServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 6),
    _AacServerAuthPort_Type()
)
aacServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerAuthPort.setStatus("current")


class _AacServerAuthKey_Type(OctetString):
    """Custom type aacServerAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_AacServerAuthKey_Type.__name__ = "OctetString"
_AacServerAuthKey_Object = MibTableColumn
aacServerAuthKey = _AacServerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 9),
    _AacServerRetryCount_Type()
)
aacServerRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacServerRetryCount.setStatus("current")
_AacServerRowStatus_Type = RowStatus
_AacServerRowStatus_Object = MibTableColumn
aacServerRowStatus = _AacServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 7, 1, 10),
    _AacServerRowStatus_Type()
)
aacServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacServerRowStatus.setStatus("current")
_AacLoginMethodListTable_Object = MibTable
aacLoginMethodListTable = _AacLoginMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8)
)
if mibBuilder.loadTexts:
    aacLoginMethodListTable.setStatus("current")
_AacLoginMethodListEntry_Object = MibTableRow
aacLoginMethodListEntry = _AacLoginMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1)
)
aacLoginMethodListEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aacLoginMethodListIndex"),
)
if mibBuilder.loadTexts:
    aacLoginMethodListEntry.setStatus("current")


class _AacLoginMethodListIndex_Type(Integer32):
    """Custom type aacLoginMethodListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacLoginMethodListIndex_Type.__name__ = "Integer32"
_AacLoginMethodListIndex_Object = MibTableColumn
aacLoginMethodListIndex = _AacLoginMethodListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1, 1),
    _AacLoginMethodListIndex_Type()
)
aacLoginMethodListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacLoginMethodListIndex.setStatus("current")


class _AacLoginMethodListName_Type(OctetString):
    """Custom type aacLoginMethodListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacLoginMethodListName_Type.__name__ = "OctetString"
_AacLoginMethodListName_Object = MibTableColumn
aacLoginMethodListName = _AacLoginMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1, 2),
    _AacLoginMethodListName_Type()
)
aacLoginMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethodListName.setStatus("current")


class _AacLoginMethod1_Type(Integer32):
    """Custom type aacLoginMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacLoginMethod1_Type.__name__ = "Integer32"
_AacLoginMethod1_Object = MibTableColumn
aacLoginMethod1 = _AacLoginMethod1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1, 3),
    _AacLoginMethod1_Type()
)
aacLoginMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod1.setStatus("current")


class _AacLoginMethod2_Type(Integer32):
    """Custom type aacLoginMethod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacLoginMethod2_Type.__name__ = "Integer32"
_AacLoginMethod2_Object = MibTableColumn
aacLoginMethod2 = _AacLoginMethod2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1, 4),
    _AacLoginMethod2_Type()
)
aacLoginMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod2.setStatus("current")


class _AacLoginMethod3_Type(Integer32):
    """Custom type aacLoginMethod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacLoginMethod3_Type.__name__ = "Integer32"
_AacLoginMethod3_Object = MibTableColumn
aacLoginMethod3 = _AacLoginMethod3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1, 5),
    _AacLoginMethod3_Type()
)
aacLoginMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod3.setStatus("current")


class _AacLoginMethod4_Type(Integer32):
    """Custom type aacLoginMethod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacLoginMethod4_Type.__name__ = "Integer32"
_AacLoginMethod4_Object = MibTableColumn
aacLoginMethod4 = _AacLoginMethod4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1, 6),
    _AacLoginMethod4_Type()
)
aacLoginMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLoginMethod4.setStatus("current")
_AacLoginMethodListRowStatus_Type = RowStatus
_AacLoginMethodListRowStatus_Object = MibTableColumn
aacLoginMethodListRowStatus = _AacLoginMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 8, 1, 7),
    _AacLoginMethodListRowStatus_Type()
)
aacLoginMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacLoginMethodListRowStatus.setStatus("current")
_AacEnableMethodListTable_Object = MibTable
aacEnableMethodListTable = _AacEnableMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9)
)
if mibBuilder.loadTexts:
    aacEnableMethodListTable.setStatus("current")
_AacEnableMethodListEntry_Object = MibTableRow
aacEnableMethodListEntry = _AacEnableMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1)
)
aacEnableMethodListEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aacEnableMethodListIndex"),
)
if mibBuilder.loadTexts:
    aacEnableMethodListEntry.setStatus("current")


class _AacEnableMethodListIndex_Type(Integer32):
    """Custom type aacEnableMethodListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AacEnableMethodListIndex_Type.__name__ = "Integer32"
_AacEnableMethodListIndex_Object = MibTableColumn
aacEnableMethodListIndex = _AacEnableMethodListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1, 1),
    _AacEnableMethodListIndex_Type()
)
aacEnableMethodListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacEnableMethodListIndex.setStatus("current")


class _AacEnableMethodListName_Type(OctetString):
    """Custom type aacEnableMethodListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacEnableMethodListName_Type.__name__ = "OctetString"
_AacEnableMethodListName_Object = MibTableColumn
aacEnableMethodListName = _AacEnableMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1, 2),
    _AacEnableMethodListName_Type()
)
aacEnableMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethodListName.setStatus("current")


class _AacEnableMethod1_Type(Integer32):
    """Custom type aacEnableMethod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacEnableMethod1_Type.__name__ = "Integer32"
_AacEnableMethod1_Object = MibTableColumn
aacEnableMethod1 = _AacEnableMethod1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1, 3),
    _AacEnableMethod1_Type()
)
aacEnableMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod1.setStatus("current")


class _AacEnableMethod2_Type(Integer32):
    """Custom type aacEnableMethod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacEnableMethod2_Type.__name__ = "Integer32"
_AacEnableMethod2_Object = MibTableColumn
aacEnableMethod2 = _AacEnableMethod2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1, 4),
    _AacEnableMethod2_Type()
)
aacEnableMethod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod2.setStatus("current")


class _AacEnableMethod3_Type(Integer32):
    """Custom type aacEnableMethod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacEnableMethod3_Type.__name__ = "Integer32"
_AacEnableMethod3_Object = MibTableColumn
aacEnableMethod3 = _AacEnableMethod3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1, 5),
    _AacEnableMethod3_Type()
)
aacEnableMethod3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod3.setStatus("current")


class _AacEnableMethod4_Type(Integer32):
    """Custom type aacEnableMethod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("none", -1),
          ("radius", 2),
          ("tacacsPlus", 1))
    )


_AacEnableMethod4_Type.__name__ = "Integer32"
_AacEnableMethod4_Object = MibTableColumn
aacEnableMethod4 = _AacEnableMethod4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1, 6),
    _AacEnableMethod4_Type()
)
aacEnableMethod4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacEnableMethod4.setStatus("current")
_AacEnableMethodListRowStatus_Type = RowStatus
_AacEnableMethodListRowStatus_Object = MibTableColumn
aacEnableMethodListRowStatus = _AacEnableMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 9, 1, 7),
    _AacEnableMethodListRowStatus_Type()
)
aacEnableMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aacEnableMethodListRowStatus.setStatus("current")


class _AacLocalEnablePassword_Type(DisplayString):
    """Custom type aacLocalEnablePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AacLocalEnablePassword_Type.__name__ = "DisplayString"
_AacLocalEnablePassword_Object = MibScalar
aacLocalEnablePassword = _AacLocalEnablePassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 14, 11, 10),
    _AacLocalEnablePassword_Type()
)
aacLocalEnablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aacLocalEnablePassword.setStatus("current")
_CompanyACLGroup_ObjectIdentity = ObjectIdentity
companyACLGroup = _CompanyACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15)
)
_AclProfile_ObjectIdentity = ObjectIdentity
aclProfile = _AclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1)
)
_Ipv4aclProfileTable_Object = MibTable
ipv4aclProfileTable = _Ipv4aclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    ipv4aclProfileTable.setStatus("obsolete")
_Ipv4aclProfileEntry_Object = MibTableRow
ipv4aclProfileEntry = _Ipv4aclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1)
)
ipv4aclProfileEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "ipv4aclProfileNo"),
)
if mibBuilder.loadTexts:
    ipv4aclProfileEntry.setStatus("obsolete")


class _Ipv4aclProfileNo_Type(Integer32):
    """Custom type ipv4aclProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_Ipv4aclProfileNo_Type.__name__ = "Integer32"
_Ipv4aclProfileNo_Object = MibTableColumn
ipv4aclProfileNo = _Ipv4aclProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 1),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2))
    )


_Ipv4aclProfileType_Type.__name__ = "Integer32"
_Ipv4aclProfileType_Object = MibTableColumn
ipv4aclProfileType = _Ipv4aclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 3),
    _Ipv4aclProfileRuleCount_Type()
)
ipv4aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4aclProfileRuleCount.setStatus("obsolete")
_Ipv4aclProfileMask_Type = OctetString
_Ipv4aclProfileMask_Object = MibTableColumn
ipv4aclProfileMask = _Ipv4aclProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 4),
    _Ipv4aclProfileMask_Type()
)
ipv4aclProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileMask.setStatus("obsolete")
_Ipv4aclProfileDstMacAddrMask_Type = MacAddress
_Ipv4aclProfileDstMacAddrMask_Object = MibTableColumn
ipv4aclProfileDstMacAddrMask = _Ipv4aclProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 5),
    _Ipv4aclProfileDstMacAddrMask_Type()
)
ipv4aclProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileDstMacAddrMask.setStatus("obsolete")
_Ipv4aclProfileSrcMacAddrMask_Type = MacAddress
_Ipv4aclProfileSrcMacAddrMask_Object = MibTableColumn
ipv4aclProfileSrcMacAddrMask = _Ipv4aclProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 6),
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
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("ipMask", 255),
          ("none", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_Ipv4aclProfileIPProtocol_Type.__name__ = "Integer32"
_Ipv4aclProfileIPProtocol_Object = MibTableColumn
ipv4aclProfileIPProtocol = _Ipv4aclProfileIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 7),
    _Ipv4aclProfileIPProtocol_Type()
)
ipv4aclProfileIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileIPProtocol.setStatus("obsolete")


class _Ipv4aclProfileIPProtocolMask_Type(OctetString):
    """Custom type ipv4aclProfileIPProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_Ipv4aclProfileIPProtocolMask_Object = MibTableColumn
ipv4aclProfileIPProtocolMask = _Ipv4aclProfileIPProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 8),
    _Ipv4aclProfileIPProtocolMask_Type()
)
ipv4aclProfileIPProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileIPProtocolMask.setStatus("obsolete")


class _Ipv4aclProfileDstIpAddrMask_Type(IpAddress):
    """Custom type ipv4aclProfileDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Ipv4aclProfileDstIpAddrMask_Object = MibTableColumn
ipv4aclProfileDstIpAddrMask = _Ipv4aclProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 12),
    _Ipv4aclProfileSrcPortMask_Type()
)
ipv4aclProfileSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4aclProfileSrcPortMask.setStatus("obsolete")
_Ipv4aclProfileStatus_Type = RowStatus
_Ipv4aclProfileStatus_Object = MibTableColumn
ipv4aclProfileStatus = _Ipv4aclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 1, 1, 28),
    _Ipv4aclProfileStatus_Type()
)
ipv4aclProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4aclProfileStatus.setStatus("obsolete")
_AclProfileTable_Object = MibTable
aclProfileTable = _AclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    aclProfileTable.setStatus("current")
_AclProfileEntry_Object = MibTableRow
aclProfileEntry = _AclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1)
)
aclProfileEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aclProfileNo"),
)
if mibBuilder.loadTexts:
    aclProfileEntry.setStatus("current")


class _AclProfileNo_Type(Integer32):
    """Custom type aclProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_AclProfileNo_Type.__name__ = "Integer32"
_AclProfileNo_Object = MibTableColumn
aclProfileNo = _AclProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 1),
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3v4", 2),
          ("l3v6", 11))
    )


_AclProfileType_Type.__name__ = "Integer32"
_AclProfileType_Object = MibTableColumn
aclProfileType = _AclProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 3),
    _AclProfileRuleCount_Type()
)
aclProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclProfileRuleCount.setStatus("current")
_AclProfileMask_Type = OctetString
_AclProfileMask_Object = MibTableColumn
aclProfileMask = _AclProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 4),
    _AclProfileMask_Type()
)
aclProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileMask.setStatus("current")
_AclProfileDstMacAddrMask_Type = MacAddress
_AclProfileDstMacAddrMask_Object = MibTableColumn
aclProfileDstMacAddrMask = _AclProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 5),
    _AclProfileDstMacAddrMask_Type()
)
aclProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileDstMacAddrMask.setStatus("current")
_AclProfileSrcMacAddrMask_Type = MacAddress
_AclProfileSrcMacAddrMask_Object = MibTableColumn
aclProfileSrcMacAddrMask = _AclProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 6),
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("ipMask", 255),
          ("none", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_AclProfileIPProtocol_Type.__name__ = "Integer32"
_AclProfileIPProtocol_Object = MibTableColumn
aclProfileIPProtocol = _AclProfileIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 7),
    _AclProfileIPProtocol_Type()
)
aclProfileIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileIPProtocol.setStatus("current")


class _AclProfileIPProtocolMask_Type(OctetString):
    """Custom type aclProfileIPProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_AclProfileIPProtocolMask_Object = MibTableColumn
aclProfileIPProtocolMask = _AclProfileIPProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 8),
    _AclProfileIPProtocolMask_Type()
)
aclProfileIPProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileIPProtocolMask.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 14),
    _AclProfileSrcPortMask_Type()
)
aclProfileSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclProfileSrcPortMask.setStatus("current")
_AclProfileStatus_Type = RowStatus
_AclProfileStatus_Object = MibTableColumn
aclProfileStatus = _AclProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 1, 2, 1, 30),
    _AclProfileStatus_Type()
)
aclProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclProfileStatus.setStatus("current")
_AclL2Rule_ObjectIdentity = ObjectIdentity
aclL2Rule = _AclL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2)
)
_AclL2RuleTable_Object = MibTable
aclL2RuleTable = _AclL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    aclL2RuleTable.setStatus("current")
_AclL2RuleEntry_Object = MibTableRow
aclL2RuleEntry = _AclL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1)
)
aclL2RuleEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aclL2ProfileID"),
    (0, "DGS-1100-06ME-AX", "aclL2AccessID"),
)
if mibBuilder.loadTexts:
    aclL2RuleEntry.setStatus("current")


class _AclL2AccessID_Type(Integer32):
    """Custom type aclL2AccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_AclL2AccessID_Type.__name__ = "Integer32"
_AclL2AccessID_Object = MibTableColumn
aclL2AccessID = _AclL2AccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 1),
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
        ValueRangeConstraint(1, 150),
    )


_AclL2ProfileID_Type.__name__ = "Integer32"
_AclL2ProfileID_Object = MibTableColumn
aclL2ProfileID = _AclL2ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 3),
    _AclL2RuleEtherType_Type()
)
aclL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleEtherType.setStatus("current")
_AclL2RuleDstMacAddr_Type = MacAddress
_AclL2RuleDstMacAddr_Object = MibTableColumn
aclL2RuleDstMacAddr = _AclL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 4),
    _AclL2RuleDstMacAddr_Type()
)
aclL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddr.setStatus("current")
_AclL2RuleSrcMacAddr_Type = MacAddress
_AclL2RuleSrcMacAddr_Object = MibTableColumn
aclL2RuleSrcMacAddr = _AclL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 7),
    _AclL2Rule1pPriority_Type()
)
aclL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2Rule1pPriority.setStatus("current")
_AclL2RuleDstMacAddrMask_Type = MacAddress
_AclL2RuleDstMacAddrMask_Object = MibTableColumn
aclL2RuleDstMacAddrMask = _AclL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 8),
    _AclL2RuleDstMacAddrMask_Type()
)
aclL2RuleDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleDstMacAddrMask.setStatus("current")
_AclL2RuleSrcMacAddrMask_Type = MacAddress
_AclL2RuleSrcMacAddrMask_Object = MibTableColumn
aclL2RuleSrcMacAddrMask = _AclL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 9),
    _AclL2RuleSrcMacAddrMask_Type()
)
aclL2RuleSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL2RuleSrcMacAddrMask.setStatus("current")
_AclL2RuleInPortList_Type = PortList
_AclL2RuleInPortList_Object = MibTableColumn
aclL2RuleInPortList = _AclL2RuleInPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 10),
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
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2),
          ("rateLimit", 4),
          ("replaceDSCP", 5))
    )


_AclL2RuleAction_Type.__name__ = "Integer32"
_AclL2RuleAction_Object = MibTableColumn
aclL2RuleAction = _AclL2RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 11),
    _AclL2RuleAction_Type()
)
aclL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleAction.setStatus("current")
_AclL2RuleRateLimit_Type = Unsigned32
_AclL2RuleRateLimit_Object = MibTableColumn
aclL2RuleRateLimit = _AclL2RuleRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 12),
    _AclL2RuleRateLimit_Type()
)
aclL2RuleRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleRateLimit.setStatus("current")


class _AclL2RuleReplaceDSCP_Type(Integer32):
    """Custom type aclL2RuleReplaceDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL2RuleReplaceDSCP_Type.__name__ = "Integer32"
_AclL2RuleReplaceDSCP_Object = MibTableColumn
aclL2RuleReplaceDSCP = _AclL2RuleReplaceDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 13),
    _AclL2RuleReplaceDSCP_Type()
)
aclL2RuleReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleReplaceDSCP.setStatus("current")


class _AclL2RuleNonIPFilterOnlyState_Type(Integer32):
    """Custom type aclL2RuleNonIPFilterOnlyState based on Integer32"""
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


_AclL2RuleNonIPFilterOnlyState_Type.__name__ = "Integer32"
_AclL2RuleNonIPFilterOnlyState_Object = MibTableColumn
aclL2RuleNonIPFilterOnlyState = _AclL2RuleNonIPFilterOnlyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 15),
    _AclL2RuleNonIPFilterOnlyState_Type()
)
aclL2RuleNonIPFilterOnlyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL2RuleNonIPFilterOnlyState.setStatus("current")
_AclL2RuleStatus_Type = RowStatus
_AclL2RuleStatus_Object = MibTableColumn
aclL2RuleStatus = _AclL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 2, 1, 1, 99),
    _AclL2RuleStatus_Type()
)
aclL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL2RuleStatus.setStatus("current")
_AclL3Rule_ObjectIdentity = ObjectIdentity
aclL3Rule = _AclL3Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3)
)
_AclL3RuleTable_Object = MibTable
aclL3RuleTable = _AclL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    aclL3RuleTable.setStatus("current")
_AclL3RuleEntry_Object = MibTableRow
aclL3RuleEntry = _AclL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1)
)
aclL3RuleEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aclL3RuleProfileNo"),
    (0, "DGS-1100-06ME-AX", "aclL3RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclL3RuleEntry.setStatus("current")


class _AclL3RuleAccessID_Type(Integer32):
    """Custom type aclL3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_AclL3RuleAccessID_Type.__name__ = "Integer32"
_AclL3RuleAccessID_Object = MibTableColumn
aclL3RuleAccessID = _AclL3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 1),
    _AclL3RuleAccessID_Type()
)
aclL3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleAccessID.setStatus("current")


class _AclL3RuleProfileNo_Type(Integer32):
    """Custom type aclL3RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_AclL3RuleProfileNo_Type.__name__ = "Integer32"
_AclL3RuleProfileNo_Object = MibTableColumn
aclL3RuleProfileNo = _AclL3RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 3),
    _AclL3RuleProtocol_Type()
)
aclL3RuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleProtocol.setStatus("current")


class _AclL3RuleProtocolMask_Type(OctetString):
    """Custom type aclL3RuleProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_AclL3RuleProtocolMask_Object = MibTableColumn
aclL3RuleProtocolMask = _AclL3RuleProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 4),
    _AclL3RuleProtocolMask_Type()
)
aclL3RuleProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleProtocolMask.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 12),
    _AclL3RuleTcpUdpSrcPort_Type()
)
aclL3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpSrcPort.setStatus("current")
_AclL3RuleTcpUdpDstPortMask_Type = OctetString
_AclL3RuleTcpUdpDstPortMask_Object = MibTableColumn
aclL3RuleTcpUdpDstPortMask = _AclL3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 13),
    _AclL3RuleTcpUdpDstPortMask_Type()
)
aclL3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclL3RuleTcpUdpDstPortMask.setStatus("current")
_AclL3RuleTcpUdpSrcPortMask_Type = OctetString
_AclL3RuleTcpUdpSrcPortMask_Object = MibTableColumn
aclL3RuleTcpUdpSrcPortMask = _AclL3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 14),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpAckBit_Type.__name__ = "Integer32"
_AclL3RuleTcpAckBit_Object = MibTableColumn
aclL3RuleTcpAckBit = _AclL3RuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 15),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpRstBit_Type.__name__ = "Integer32"
_AclL3RuleTcpRstBit_Object = MibTableColumn
aclL3RuleTcpRstBit = _AclL3RuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 16),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpUrgBit_Type.__name__ = "Integer32"
_AclL3RuleTcpUrgBit_Object = MibTableColumn
aclL3RuleTcpUrgBit = _AclL3RuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 17),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpPshBit_Type.__name__ = "Integer32"
_AclL3RuleTcpPshBit_Object = MibTableColumn
aclL3RuleTcpPshBit = _AclL3RuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 18),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpSynBit_Type.__name__ = "Integer32"
_AclL3RuleTcpSynBit_Object = MibTableColumn
aclL3RuleTcpSynBit = _AclL3RuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 19),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_AclL3RuleTcpFinBit_Type.__name__ = "Integer32"
_AclL3RuleTcpFinBit_Object = MibTableColumn
aclL3RuleTcpFinBit = _AclL3RuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 21),
    _AclL3RuleDscp_Type()
)
aclL3RuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleDscp.setStatus("current")


class _AclL3RuleTos_Type(Integer32):
    """Custom type aclL3RuleTos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclL3RuleTos_Type.__name__ = "Integer32"
_AclL3RuleTos_Object = MibTableColumn
aclL3RuleTos = _AclL3RuleTos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 22),
    _AclL3RuleTos_Type()
)
aclL3RuleTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleTos.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 23),
    _AclL3RuleIgmpType_Type()
)
aclL3RuleIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleIgmpType.setStatus("current")
_AclL3RulePortList_Type = PortList
_AclL3RulePortList_Object = MibTableColumn
aclL3RulePortList = _AclL3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 24),
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
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2),
          ("rateLimit", 4),
          ("replaceDSCP", 5))
    )


_AclL3RuleAction_Type.__name__ = "Integer32"
_AclL3RuleAction_Object = MibTableColumn
aclL3RuleAction = _AclL3RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 25),
    _AclL3RuleAction_Type()
)
aclL3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleAction.setStatus("current")
_AclL3RuleRateLimit_Type = Unsigned32
_AclL3RuleRateLimit_Object = MibTableColumn
aclL3RuleRateLimit = _AclL3RuleRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 26),
    _AclL3RuleRateLimit_Type()
)
aclL3RuleRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleRateLimit.setStatus("current")


class _AclL3RuleReplaceDSCP_Type(Integer32):
    """Custom type aclL3RuleReplaceDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclL3RuleReplaceDSCP_Type.__name__ = "Integer32"
_AclL3RuleReplaceDSCP_Object = MibTableColumn
aclL3RuleReplaceDSCP = _AclL3RuleReplaceDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 27),
    _AclL3RuleReplaceDSCP_Type()
)
aclL3RuleReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclL3RuleReplaceDSCP.setStatus("current")
_AclL3RuleStatus_Type = RowStatus
_AclL3RuleStatus_Object = MibTableColumn
aclL3RuleStatus = _AclL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 1, 1, 29),
    _AclL3RuleStatus_Type()
)
aclL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclL3RuleStatus.setStatus("current")
_Aclv6L3RuleTable_Object = MibTable
aclv6L3RuleTable = _Aclv6L3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2)
)
if mibBuilder.loadTexts:
    aclv6L3RuleTable.setStatus("current")
_Aclv6L3RuleEntry_Object = MibTableRow
aclv6L3RuleEntry = _Aclv6L3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1)
)
aclv6L3RuleEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "aclv6L3RuleProfileNo"),
    (0, "DGS-1100-06ME-AX", "aclv6L3RuleAccessID"),
)
if mibBuilder.loadTexts:
    aclv6L3RuleEntry.setStatus("current")


class _Aclv6L3RuleAccessID_Type(Integer32):
    """Custom type aclv6L3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_Aclv6L3RuleAccessID_Type.__name__ = "Integer32"
_Aclv6L3RuleAccessID_Object = MibTableColumn
aclv6L3RuleAccessID = _Aclv6L3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 1),
    _Aclv6L3RuleAccessID_Type()
)
aclv6L3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleAccessID.setStatus("current")


class _Aclv6L3RuleProfileNo_Type(Integer32):
    """Custom type aclv6L3RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_Aclv6L3RuleProfileNo_Type.__name__ = "Integer32"
_Aclv6L3RuleProfileNo_Object = MibTableColumn
aclv6L3RuleProfileNo = _Aclv6L3RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 3),
    _Aclv6L3RuleProtocol_Type()
)
aclv6L3RuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleProtocol.setStatus("current")


class _Aclv6L3RuleProtocolMask_Type(OctetString):
    """Custom type aclv6L3RuleProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_Aclv6L3RuleProtocolMask_Object = MibTableColumn
aclv6L3RuleProtocolMask = _Aclv6L3RuleProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 4),
    _Aclv6L3RuleProtocolMask_Type()
)
aclv6L3RuleProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleProtocolMask.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 12),
    _Aclv6L3RuleTcpUdpSrcPort_Type()
)
aclv6L3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpUdpSrcPort.setStatus("current")
_Aclv6L3RuleTcpUdpDstPortMask_Type = OctetString
_Aclv6L3RuleTcpUdpDstPortMask_Object = MibTableColumn
aclv6L3RuleTcpUdpDstPortMask = _Aclv6L3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 13),
    _Aclv6L3RuleTcpUdpDstPortMask_Type()
)
aclv6L3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclv6L3RuleTcpUdpDstPortMask.setStatus("current")
_Aclv6L3RuleTcpUdpSrcPortMask_Type = OctetString
_Aclv6L3RuleTcpUdpSrcPortMask_Object = MibTableColumn
aclv6L3RuleTcpUdpSrcPortMask = _Aclv6L3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 14),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpAckBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpAckBit_Object = MibTableColumn
aclv6L3RuleTcpAckBit = _Aclv6L3RuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 15),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpRstBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpRstBit_Object = MibTableColumn
aclv6L3RuleTcpRstBit = _Aclv6L3RuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 16),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpUrgBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpUrgBit_Object = MibTableColumn
aclv6L3RuleTcpUrgBit = _Aclv6L3RuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 17),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpPshBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpPshBit_Object = MibTableColumn
aclv6L3RuleTcpPshBit = _Aclv6L3RuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 18),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpSynBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpSynBit_Object = MibTableColumn
aclv6L3RuleTcpSynBit = _Aclv6L3RuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 19),
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
        *(("dont-care", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_Aclv6L3RuleTcpFinBit_Type.__name__ = "Integer32"
_Aclv6L3RuleTcpFinBit_Object = MibTableColumn
aclv6L3RuleTcpFinBit = _Aclv6L3RuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 21),
    _Aclv6L3RuleTrafficClass_Type()
)
aclv6L3RuleTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleTrafficClass.setStatus("current")
_Aclv6L3RulePortList_Type = PortList
_Aclv6L3RulePortList_Object = MibTableColumn
aclv6L3RulePortList = _Aclv6L3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 23),
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
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2),
          ("rateLimit", 4),
          ("replaceDSCP", 5))
    )


_Aclv6L3RuleAction_Type.__name__ = "Integer32"
_Aclv6L3RuleAction_Object = MibTableColumn
aclv6L3RuleAction = _Aclv6L3RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 24),
    _Aclv6L3RuleAction_Type()
)
aclv6L3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleAction.setStatus("current")
_Aclv6L3RuleRateLimit_Type = Unsigned32
_Aclv6L3RuleRateLimit_Object = MibTableColumn
aclv6L3RuleRateLimit = _Aclv6L3RuleRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 25),
    _Aclv6L3RuleRateLimit_Type()
)
aclv6L3RuleRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleRateLimit.setStatus("current")


class _Aclv6L3RuleReplaceDSCP_Type(Integer32):
    """Custom type aclv6L3RuleReplaceDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_Aclv6L3RuleReplaceDSCP_Type.__name__ = "Integer32"
_Aclv6L3RuleReplaceDSCP_Object = MibTableColumn
aclv6L3RuleReplaceDSCP = _Aclv6L3RuleReplaceDSCP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 26),
    _Aclv6L3RuleReplaceDSCP_Type()
)
aclv6L3RuleReplaceDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclv6L3RuleReplaceDSCP.setStatus("current")
_Aclv6L3RuleStatus_Type = RowStatus
_Aclv6L3RuleStatus_Object = MibTableColumn
aclv6L3RuleStatus = _Aclv6L3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 15, 3, 2, 1, 28),
    _Aclv6L3RuleStatus_Type()
)
aclv6L3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclv6L3RuleStatus.setStatus("current")
_CompanySyslog_ObjectIdentity = ObjectIdentity
companySyslog = _CompanySyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16)
)
_SyslogSettingGroup_ObjectIdentity = ObjectIdentity
syslogSettingGroup = _SyslogSettingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 1)
)


class _SyslogEnable_Type(Integer32):
    """Custom type syslogEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SyslogEnable_Type.__name__ = "Integer32"
_SyslogEnable_Object = MibScalar
syslogEnable = _SyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 1, 3),
    _SyslogSaveMinutes_Type()
)
syslogSaveMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSaveMinutes.setStatus("current")
_SyslogServerGroup_ObjectIdentity = ObjectIdentity
syslogServerGroup = _SyslogServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3)
)
_SyslogServTable_Object = MibTable
syslogServTable = _SyslogServTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    syslogServTable.setStatus("current")
_SyslogServEntry_Object = MibTableRow
syslogServEntry = _SyslogServEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1)
)
syslogServEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "syslogServIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 1),
    _SyslogServIndex_Type()
)
syslogServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogServIndex.setStatus("current")


class _SyslogServAddrType_Type(Integer32):
    """Custom type syslogServAddrType based on Integer32"""
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 2),
    _SyslogServAddrType_Type()
)
syslogServAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServAddrType.setStatus("current")
_SyslogServAddr_Type = Ipv6Address
_SyslogServAddr_Object = MibTableColumn
syslogServAddr = _SyslogServAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 3),
    _SyslogServAddr_Type()
)
syslogServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServAddr.setStatus("current")
_SyslogServInterfaceName_Type = OctetString
_SyslogServInterfaceName_Object = MibTableColumn
syslogServInterfaceName = _SyslogServInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 4),
    _SyslogServInterfaceName_Type()
)
syslogServInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServInterfaceName.setStatus("current")


class _SyslogServSeverity_Type(Integer32):
    """Custom type syslogServSeverity based on Integer32"""
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
          ("information", 6),
          ("warning", 4))
    )


_SyslogServSeverity_Type.__name__ = "Integer32"
_SyslogServSeverity_Object = MibTableColumn
syslogServSeverity = _SyslogServSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 5),
    _SyslogServSeverity_Type()
)
syslogServSeverity.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 6),
    _SyslogServFacility_Type()
)
syslogServFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServFacility.setStatus("current")


class _SyslogServUDPport_Type(Integer32):
    """Custom type syslogServUDPport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 514),
        ValueRangeConstraint(6000, 65535),
    )


_SyslogServUDPport_Type.__name__ = "Integer32"
_SyslogServUDPport_Object = MibTableColumn
syslogServUDPport = _SyslogServUDPport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 7),
    _SyslogServUDPport_Type()
)
syslogServUDPport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServUDPport.setStatus("current")


class _SyslogServSrvStatus_Type(Integer32):
    """Custom type syslogServSrvStatus based on Integer32"""
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


_SyslogServSrvStatus_Type.__name__ = "Integer32"
_SyslogServSrvStatus_Object = MibTableColumn
syslogServSrvStatus = _SyslogServSrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 8),
    _SyslogServSrvStatus_Type()
)
syslogServSrvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServSrvStatus.setStatus("current")
_SyslogServSrvRowStatus_Type = RowStatus
_SyslogServSrvRowStatus_Object = MibTableColumn
syslogServSrvRowStatus = _SyslogServSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 16, 3, 1, 1, 9),
    _SyslogServSrvRowStatus_Type()
)
syslogServSrvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServSrvRowStatus.setStatus("current")
_CompanyLBD_ObjectIdentity = ObjectIdentity
companyLBD = _CompanyLBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 4),
    _SysLBDRecoverTime_Type()
)
sysLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLBDRecoverTime.setStatus("current")
_SysLBDCtrlTable_Object = MibTable
sysLBDCtrlTable = _SysLBDCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 5)
)
if mibBuilder.loadTexts:
    sysLBDCtrlTable.setStatus("current")
_SysLBDCtrlEntry_Object = MibTableRow
sysLBDCtrlEntry = _SysLBDCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 5, 1)
)
sysLBDCtrlEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "sysLBDCtrlIndex"),
)
if mibBuilder.loadTexts:
    sysLBDCtrlEntry.setStatus("current")


class _SysLBDCtrlIndex_Type(Integer32):
    """Custom type sysLBDCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SysLBDCtrlIndex_Type.__name__ = "Integer32"
_SysLBDCtrlIndex_Object = MibTableColumn
sysLBDCtrlIndex = _SysLBDCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 5, 1, 3),
    _SysLBDPortLoopStatus_Type()
)
sysLBDPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDPortLoopStatus.setStatus("current")
_SysLBDVlanLoopTable_Object = MibTable
sysLBDVlanLoopTable = _SysLBDVlanLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 6)
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopTable.setStatus("current")
_SysLBDVlanLoopEntry_Object = MibTableRow
sysLBDVlanLoopEntry = _SysLBDVlanLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 6, 1)
)
sysLBDVlanLoopEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "sysLBDVlanLoopIndex"),
)
if mibBuilder.loadTexts:
    sysLBDVlanLoopEntry.setStatus("current")


class _SysLBDVlanLoopIndex_Type(Integer32):
    """Custom type sysLBDVlanLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SysLBDVlanLoopIndex_Type.__name__ = "Integer32"
_SysLBDVlanLoopIndex_Object = MibTableColumn
sysLBDVlanLoopIndex = _SysLBDVlanLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 6, 1, 1),
    _SysLBDVlanLoopIndex_Type()
)
sysLBDVlanLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopIndex.setStatus("current")
_SysLBDVlanLoopPorts_Type = PortList
_SysLBDVlanLoopPorts_Object = MibTableColumn
sysLBDVlanLoopPorts = _SysLBDVlanLoopPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 17, 6, 1, 2),
    _SysLBDVlanLoopPorts_Type()
)
sysLBDVlanLoopPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLBDVlanLoopPorts.setStatus("current")
_CompanyMirror_ObjectIdentity = ObjectIdentity
companyMirror = _CompanyMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 18)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 18, 1),
    _SysMirrorStatus_Type()
)
sysMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorStatus.setStatus("current")
_SysMirrorTargetPort_Type = Integer32
_SysMirrorTargetPort_Object = MibScalar
sysMirrorTargetPort = _SysMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 18, 2),
    _SysMirrorTargetPort_Type()
)
sysMirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorTargetPort.setStatus("current")
_SysMirrorCtrlIngressMirroring_Type = PortList
_SysMirrorCtrlIngressMirroring_Object = MibScalar
sysMirrorCtrlIngressMirroring = _SysMirrorCtrlIngressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 18, 3),
    _SysMirrorCtrlIngressMirroring_Type()
)
sysMirrorCtrlIngressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlIngressMirroring.setStatus("current")
_SysMirrorCtrlEgressMirroring_Type = PortList
_SysMirrorCtrlEgressMirroring_Object = MibScalar
sysMirrorCtrlEgressMirroring = _SysMirrorCtrlEgressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 18, 4),
    _SysMirrorCtrlEgressMirroring_Type()
)
sysMirrorCtrlEgressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMirrorCtrlEgressMirroring.setStatus("current")
_CompanyStaticMcast_ObjectIdentity = ObjectIdentity
companyStaticMcast = _CompanyStaticMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19)
)
_StaticMcastTable_Object = MibTable
staticMcastTable = _StaticMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    staticMcastTable.setStatus("current")
_StaticMcastEntry_Object = MibTableRow
staticMcastEntry = _StaticMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19, 1, 1)
)
staticMcastEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "staticMcastVlanID"),
    (0, "DGS-1100-06ME-AX", "staticMcastMac"),
    (0, "DGS-1100-06ME-AX", "staticMcastEgressPorts"),
    (0, "DGS-1100-06ME-AX", "staticMcastIpAddr"),
)
if mibBuilder.loadTexts:
    staticMcastEntry.setStatus("current")


class _StaticMcastVlanID_Type(Integer32):
    """Custom type staticMcastVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_StaticMcastVlanID_Type.__name__ = "Integer32"
_StaticMcastVlanID_Object = MibTableColumn
staticMcastVlanID = _StaticMcastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19, 1, 1, 1),
    _StaticMcastVlanID_Type()
)
staticMcastVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastVlanID.setStatus("current")
_StaticMcastMac_Type = MacAddress
_StaticMcastMac_Object = MibTableColumn
staticMcastMac = _StaticMcastMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19, 1, 1, 2),
    _StaticMcastMac_Type()
)
staticMcastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastMac.setStatus("current")


class _StaticMcastEgressPorts_Type(PortList):
    """Custom type staticMcastEgressPorts based on PortList"""
    subtypeSpec = PortList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_StaticMcastEgressPorts_Type.__name__ = "PortList"
_StaticMcastEgressPorts_Object = MibTableColumn
staticMcastEgressPorts = _StaticMcastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19, 1, 1, 3),
    _StaticMcastEgressPorts_Type()
)
staticMcastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastEgressPorts.setStatus("current")
_StaticMcastIpAddr_Type = IpAddress
_StaticMcastIpAddr_Object = MibTableColumn
staticMcastIpAddr = _StaticMcastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19, 1, 1, 4),
    _StaticMcastIpAddr_Type()
)
staticMcastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticMcastIpAddr.setStatus("current")
_StaticMcastStatus_Type = RowStatus
_StaticMcastStatus_Object = MibTableColumn
staticMcastStatus = _StaticMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 19, 1, 1, 5),
    _StaticMcastStatus_Type()
)
staticMcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMcastStatus.setStatus("current")
_CompanySNTPSetting_ObjectIdentity = ObjectIdentity
companySNTPSetting = _CompanySNTPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20)
)
_SysSNTPServerTable_ObjectIdentity = ObjectIdentity
sysSNTPServerTable = _SysSNTPServerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17)
)
_SysSNTPTimeSeconds_Type = Integer32
_SysSNTPTimeSeconds_Object = MibScalar
sysSNTPTimeSeconds = _SysSNTPTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 1),
    _SysSNTPTimeSeconds_Type()
)
sysSNTPTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPTimeSeconds.setStatus("current")
_SysSNTPFirstServer_Type = Ipv6Address
_SysSNTPFirstServer_Object = MibScalar
sysSNTPFirstServer = _SysSNTPFirstServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 3),
    _SysSNTPFirstType_Type()
)
sysSNTPFirstType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstType.setStatus("current")
_SysSNTPFirstInterfaceName_Type = OctetString
_SysSNTPFirstInterfaceName_Object = MibScalar
sysSNTPFirstInterfaceName = _SysSNTPFirstInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 4),
    _SysSNTPFirstInterfaceName_Type()
)
sysSNTPFirstInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPFirstInterfaceName.setStatus("current")
_SysSNTPSecondServer_Type = Ipv6Address
_SysSNTPSecondServer_Object = MibScalar
sysSNTPSecondServer = _SysSNTPSecondServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 6),
    _SysSNTPSecondType_Type()
)
sysSNTPSecondType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondType.setStatus("current")
_SysSNTPSecondInterfaceName_Type = OctetString
_SysSNTPSecondInterfaceName_Object = MibScalar
sysSNTPSecondInterfaceName = _SysSNTPSecondInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 7),
    _SysSNTPSecondInterfaceName_Type()
)
sysSNTPSecondInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPSecondInterfaceName.setStatus("current")
_SysSNTPPollInterval_Type = Integer32
_SysSNTPPollInterval_Object = MibScalar
sysSNTPPollInterval = _SysSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 10),
    _SysSNTPDSTOffset_Type()
)
sysSNTPDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTOffset.setStatus("current")
_SysSNTPGMTMinutes_Type = Integer32
_SysSNTPGMTMinutes_Object = MibScalar
sysSNTPGMTMinutes = _SysSNTPGMTMinutes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 11),
    _SysSNTPGMTMinutes_Type()
)
sysSNTPGMTMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPGMTMinutes.setStatus("current")
_SysSNTPDSTStartMon_Type = Integer32
_SysSNTPDSTStartMon_Object = MibScalar
sysSNTPDSTStartMon = _SysSNTPDSTStartMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 12),
    _SysSNTPDSTStartMon_Type()
)
sysSNTPDSTStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMon.setStatus("current")
_SysSNTPDSTStartDay_Type = Integer32
_SysSNTPDSTStartDay_Object = MibScalar
sysSNTPDSTStartDay = _SysSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 13),
    _SysSNTPDSTStartDay_Type()
)
sysSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartDay.setStatus("current")
_SysSNTPDSTStartHour_Type = Integer32
_SysSNTPDSTStartHour_Object = MibScalar
sysSNTPDSTStartHour = _SysSNTPDSTStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 14),
    _SysSNTPDSTStartHour_Type()
)
sysSNTPDSTStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartHour.setStatus("current")
_SysSNTPDSTStartMin_Type = Integer32
_SysSNTPDSTStartMin_Object = MibScalar
sysSNTPDSTStartMin = _SysSNTPDSTStartMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 15),
    _SysSNTPDSTStartMin_Type()
)
sysSNTPDSTStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTStartMin.setStatus("current")
_SysSNTPDSTEndMon_Type = Integer32
_SysSNTPDSTEndMon_Object = MibScalar
sysSNTPDSTEndMon = _SysSNTPDSTEndMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 16),
    _SysSNTPDSTEndMon_Type()
)
sysSNTPDSTEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndMon.setStatus("current")
_SysSNTPDSTEndDay_Type = Integer32
_SysSNTPDSTEndDay_Object = MibScalar
sysSNTPDSTEndDay = _SysSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 17),
    _SysSNTPDSTEndDay_Type()
)
sysSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndDay.setStatus("current")
_SysSNTPDSTEndHour_Type = Integer32
_SysSNTPDSTEndHour_Object = MibScalar
sysSNTPDSTEndHour = _SysSNTPDSTEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 18),
    _SysSNTPDSTEndHour_Type()
)
sysSNTPDSTEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTEndHour.setStatus("current")
_SysSNTPDSTEndMin_Type = Integer32
_SysSNTPDSTEndMin_Object = MibScalar
sysSNTPDSTEndMin = _SysSNTPDSTEndMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 19),
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
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysSNTPDSTState_Type.__name__ = "Integer32"
_SysSNTPDSTState_Object = MibScalar
sysSNTPDSTState = _SysSNTPDSTState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 20),
    _SysSNTPDSTState_Type()
)
sysSNTPDSTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTState.setStatus("current")


class _SysSNTPDSTMethod_Type(Integer32):
    """Custom type sysSNTPDSTMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annual", 1),
          ("repeating", 2))
    )


_SysSNTPDSTMethod_Type.__name__ = "Integer32"
_SysSNTPDSTMethod_Object = MibScalar
sysSNTPDSTMethod = _SysSNTPDSTMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 30),
    _SysSNTPDSTMethod_Type()
)
sysSNTPDSTMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTMethod.setStatus("current")
_SysSNTPDSTRepeatStartMon_Type = Integer32
_SysSNTPDSTRepeatStartMon_Object = MibScalar
sysSNTPDSTRepeatStartMon = _SysSNTPDSTRepeatStartMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 31),
    _SysSNTPDSTRepeatStartMon_Type()
)
sysSNTPDSTRepeatStartMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatStartMon.setStatus("current")


class _SysSNTPDSTRepeatStartWeek_Type(Integer32):
    """Custom type sysSNTPDSTRepeatStartWeek based on Integer32"""
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
        *(("fifth", 5),
          ("first", 1),
          ("fourth", 4),
          ("last", 0),
          ("second", 2),
          ("third", 3))
    )


_SysSNTPDSTRepeatStartWeek_Type.__name__ = "Integer32"
_SysSNTPDSTRepeatStartWeek_Object = MibScalar
sysSNTPDSTRepeatStartWeek = _SysSNTPDSTRepeatStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 32),
    _SysSNTPDSTRepeatStartWeek_Type()
)
sysSNTPDSTRepeatStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatStartWeek.setStatus("current")


class _SysSNTPDSTRepeatStartWeekDay_Type(Integer32):
    """Custom type sysSNTPDSTRepeatStartWeekDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fri", 5),
          ("mon", 1),
          ("sat", 6),
          ("sun", 0),
          ("thu", 4),
          ("tue", 2),
          ("wed", 3))
    )


_SysSNTPDSTRepeatStartWeekDay_Type.__name__ = "Integer32"
_SysSNTPDSTRepeatStartWeekDay_Object = MibScalar
sysSNTPDSTRepeatStartWeekDay = _SysSNTPDSTRepeatStartWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 33),
    _SysSNTPDSTRepeatStartWeekDay_Type()
)
sysSNTPDSTRepeatStartWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatStartWeekDay.setStatus("current")
_SysSNTPDSTRepeatStartHour_Type = Integer32
_SysSNTPDSTRepeatStartHour_Object = MibScalar
sysSNTPDSTRepeatStartHour = _SysSNTPDSTRepeatStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 34),
    _SysSNTPDSTRepeatStartHour_Type()
)
sysSNTPDSTRepeatStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatStartHour.setStatus("current")
_SysSNTPDSTRepeatStartMin_Type = Integer32
_SysSNTPDSTRepeatStartMin_Object = MibScalar
sysSNTPDSTRepeatStartMin = _SysSNTPDSTRepeatStartMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 35),
    _SysSNTPDSTRepeatStartMin_Type()
)
sysSNTPDSTRepeatStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatStartMin.setStatus("current")
_SysSNTPDSTRepeatEndMon_Type = Integer32
_SysSNTPDSTRepeatEndMon_Object = MibScalar
sysSNTPDSTRepeatEndMon = _SysSNTPDSTRepeatEndMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 36),
    _SysSNTPDSTRepeatEndMon_Type()
)
sysSNTPDSTRepeatEndMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatEndMon.setStatus("current")


class _SysSNTPDSTRepeatEndWeek_Type(Integer32):
    """Custom type sysSNTPDSTRepeatEndWeek based on Integer32"""
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
        *(("fifth", 5),
          ("first", 1),
          ("fourth", 4),
          ("last", 0),
          ("second", 2),
          ("third", 3))
    )


_SysSNTPDSTRepeatEndWeek_Type.__name__ = "Integer32"
_SysSNTPDSTRepeatEndWeek_Object = MibScalar
sysSNTPDSTRepeatEndWeek = _SysSNTPDSTRepeatEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 37),
    _SysSNTPDSTRepeatEndWeek_Type()
)
sysSNTPDSTRepeatEndWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatEndWeek.setStatus("current")


class _SysSNTPDSTRepeatEndWeekDay_Type(Integer32):
    """Custom type sysSNTPDSTRepeatEndWeekDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fri", 5),
          ("mon", 1),
          ("sat", 6),
          ("sun", 0),
          ("thu", 4),
          ("tue", 2),
          ("wed", 3))
    )


_SysSNTPDSTRepeatEndWeekDay_Type.__name__ = "Integer32"
_SysSNTPDSTRepeatEndWeekDay_Object = MibScalar
sysSNTPDSTRepeatEndWeekDay = _SysSNTPDSTRepeatEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 38),
    _SysSNTPDSTRepeatEndWeekDay_Type()
)
sysSNTPDSTRepeatEndWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatEndWeekDay.setStatus("current")
_SysSNTPDSTRepeatEndHour_Type = Integer32
_SysSNTPDSTRepeatEndHour_Object = MibScalar
sysSNTPDSTRepeatEndHour = _SysSNTPDSTRepeatEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 39),
    _SysSNTPDSTRepeatEndHour_Type()
)
sysSNTPDSTRepeatEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatEndHour.setStatus("current")
_SysSNTPDSTRepeatEndMin_Type = Integer32
_SysSNTPDSTRepeatEndMin_Object = MibScalar
sysSNTPDSTRepeatEndMin = _SysSNTPDSTRepeatEndMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 20, 17, 40),
    _SysSNTPDSTRepeatEndMin_Type()
)
sysSNTPDSTRepeatEndMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSNTPDSTRepeatEndMin.setStatus("current")
_CompanyRMON_ObjectIdentity = ObjectIdentity
companyRMON = _CompanyRMON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 1),
    _RmonGlobalState_Type()
)
rmonGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonGlobalState.setStatus("current")
_RmonStatistics_ObjectIdentity = ObjectIdentity
rmonStatistics = _RmonStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 2)
)
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 2, 1)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 2, 1, 1)
)
rmonStatsEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "rmonStatsIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 2, 1, 1, 1),
    _RmonStatsIndex_Type()
)
rmonStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsIndex.setStatus("current")
_RmonStatsDataSource_Type = ObjectIdentifier
_RmonStatsDataSource_Object = MibTableColumn
rmonStatsDataSource = _RmonStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 2, 1, 1, 2),
    _RmonStatsDataSource_Type()
)
rmonStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsDataSource.setStatus("current")
_RmonStatsOwner_Type = OwnerString
_RmonStatsOwner_Object = MibTableColumn
rmonStatsOwner = _RmonStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 2, 1, 1, 3),
    _RmonStatsOwner_Type()
)
rmonStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsOwner.setStatus("current")
_RmonStatsStatus_Type = RmonStatus
_RmonStatsStatus_Object = MibTableColumn
rmonStatsStatus = _RmonStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 2, 1, 1, 4),
    _RmonStatsStatus_Type()
)
rmonStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonStatsStatus.setStatus("current")
_RmonHistory_ObjectIdentity = ObjectIdentity
rmonHistory = _RmonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3)
)
_RmonHistoryTable_Object = MibTable
rmonHistoryTable = _RmonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1)
)
if mibBuilder.loadTexts:
    rmonHistoryTable.setStatus("current")
_RmonHistoryEntry_Object = MibTableRow
rmonHistoryEntry = _RmonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1, 1)
)
rmonHistoryEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "rmonHistoryIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1, 1, 1),
    _RmonHistoryIndex_Type()
)
rmonHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonHistoryIndex.setStatus("current")
_RmonHistoryDataSource_Type = ObjectIdentifier
_RmonHistoryDataSource_Object = MibTableColumn
rmonHistoryDataSource = _RmonHistoryDataSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1, 1, 4),
    _RmonHistoryInterval_Type()
)
rmonHistoryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rmonHistoryInterval.setUnits("Seconds")
_RmonHistoryOwner_Type = OwnerString
_RmonHistoryOwner_Object = MibTableColumn
rmonHistoryOwner = _RmonHistoryOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1, 1, 5),
    _RmonHistoryOwner_Type()
)
rmonHistoryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryOwner.setStatus("current")
_RmonHistoryStatus_Type = RmonStatus
_RmonHistoryStatus_Object = MibTableColumn
rmonHistoryStatus = _RmonHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 3, 1, 1, 6),
    _RmonHistoryStatus_Type()
)
rmonHistoryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonHistoryStatus.setStatus("current")
_RmonAlarm_ObjectIdentity = ObjectIdentity
rmonAlarm = _RmonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4)
)
_RmonAlarmTable_Object = MibTable
rmonAlarmTable = _RmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1)
)
if mibBuilder.loadTexts:
    rmonAlarmTable.setStatus("current")
_RmonAlarmEntry_Object = MibTableRow
rmonAlarmEntry = _RmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1)
)
rmonAlarmEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "rmonAlarmIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 1),
    _RmonAlarmIndex_Type()
)
rmonAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAlarmIndex.setStatus("current")
_RmonAlarmInterval_Type = Integer32
_RmonAlarmInterval_Object = MibTableColumn
rmonAlarmInterval = _RmonAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 4),
    _RmonAlarmSampleType_Type()
)
rmonAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmSampleType.setStatus("current")
_RmonAlarmRisingThreshold_Type = Integer32
_RmonAlarmRisingThreshold_Object = MibTableColumn
rmonAlarmRisingThreshold = _RmonAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 5),
    _RmonAlarmRisingThreshold_Type()
)
rmonAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmRisingThreshold.setStatus("current")
_RmonAlarmFallingThreshold_Type = Integer32
_RmonAlarmFallingThreshold_Object = MibTableColumn
rmonAlarmFallingThreshold = _RmonAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 8),
    _RmonAlarmFallingEventIndex_Type()
)
rmonAlarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmFallingEventIndex.setStatus("current")
_RmonAlarmOwner_Type = OwnerString
_RmonAlarmOwner_Object = MibTableColumn
rmonAlarmOwner = _RmonAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 9),
    _RmonAlarmOwner_Type()
)
rmonAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmOwner.setStatus("current")
_RmonAlarmStatus_Type = RmonStatus
_RmonAlarmStatus_Object = MibTableColumn
rmonAlarmStatus = _RmonAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 4, 1, 1, 10),
    _RmonAlarmStatus_Type()
)
rmonAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonAlarmStatus.setStatus("current")
_RmonEvent_ObjectIdentity = ObjectIdentity
rmonEvent = _RmonEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5)
)
_RmonEventTable_Object = MibTable
rmonEventTable = _RmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1)
)
if mibBuilder.loadTexts:
    rmonEventTable.setStatus("current")
_RmonEventEntry_Object = MibTableRow
rmonEventEntry = _RmonEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1, 1)
)
rmonEventEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "rmonEventIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1, 1, 3),
    _RmonEventType_Type()
)
rmonEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventType.setStatus("current")


class _RmonEventCommunity_Type(OctetString):
    """Custom type rmonEventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RmonEventCommunity_Type.__name__ = "OctetString"
_RmonEventCommunity_Object = MibTableColumn
rmonEventCommunity = _RmonEventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1, 1, 4),
    _RmonEventCommunity_Type()
)
rmonEventCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventCommunity.setStatus("current")
_RmonEventOwner_Type = OwnerString
_RmonEventOwner_Object = MibTableColumn
rmonEventOwner = _RmonEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1, 1, 5),
    _RmonEventOwner_Type()
)
rmonEventOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventOwner.setStatus("current")
_RmonEventStatus_Type = RmonStatus
_RmonEventStatus_Object = MibTableColumn
rmonEventStatus = _RmonEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 22, 5, 1, 1, 6),
    _RmonEventStatus_Type()
)
rmonEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rmonEventStatus.setStatus("current")
_CompanyAuthGroup_ObjectIdentity = ObjectIdentity
companyAuthGroup = _CompanyAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23)
)
_SwAuthenCtrl_ObjectIdentity = ObjectIdentity
swAuthenCtrl = _SwAuthenCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 1, 1),
    _SwAuthStatus_Type()
)
swAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthStatus.setStatus("current")


class _SwAuthMode_Type(Integer32):
    """Custom type swAuthMode based on Integer32"""
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


_SwAuthMode_Type.__name__ = "Integer32"
_SwAuthMode_Object = MibScalar
swAuthMode = _SwAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 1, 2),
    _SwAuthMode_Type()
)
swAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthMode.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 1, 3),
    _AuthProtocol_Type()
)
authProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authProtocol.setStatus("current")


class _SwAuthCtrlPktFwdMode_Type(Integer32):
    """Custom type swAuthCtrlPktFwdMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authDropEap", 2),
          ("authForwardEap", 1))
    )


_SwAuthCtrlPktFwdMode_Type.__name__ = "Integer32"
_SwAuthCtrlPktFwdMode_Object = MibScalar
swAuthCtrlPktFwdMode = _SwAuthCtrlPktFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 1, 4),
    _SwAuthCtrlPktFwdMode_Type()
)
swAuthCtrlPktFwdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthCtrlPktFwdMode.setStatus("current")
_SwAuthPortAccessCtrl_ObjectIdentity = ObjectIdentity
swAuthPortAccessCtrl = _SwAuthPortAccessCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2)
)
_SwAuthPortAccessControlTable_Object = MibTable
swAuthPortAccessControlTable = _SwAuthPortAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlTable.setStatus("current")
_SwAuthPortAccessControlEntry_Object = MibTableRow
swAuthPortAccessControlEntry = _SwAuthPortAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1)
)
swAuthPortAccessControlEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "swAuthAuthConfigPortNumber"),
)
if mibBuilder.loadTexts:
    swAuthPortAccessControlEntry.setStatus("current")


class _SwAuthAuthConfigPortNumber_Type(Integer32):
    """Custom type swAuthAuthConfigPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SwAuthAuthConfigPortNumber_Type.__name__ = "Integer32"
_SwAuthAuthConfigPortNumber_Object = MibTableColumn
swAuthAuthConfigPortNumber = _SwAuthAuthConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 2, 1, 1, 11),
    _SwAuthAuthDirection_Type()
)
swAuthAuthDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthAuthDirection.setStatus("current")
_SwAuthUser_ObjectIdentity = ObjectIdentity
swAuthUser = _SwAuthUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 3)
)
_SwAuthUserTable_Object = MibTable
swAuthUserTable = _SwAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 3, 1)
)
if mibBuilder.loadTexts:
    swAuthUserTable.setStatus("current")
_SwAuthUserEntry_Object = MibTableRow
swAuthUserEntry = _SwAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 3, 1, 1)
)
swAuthUserEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "swAuthUserName"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 3, 1, 1, 2),
    _SwAuthUserPassword_Type()
)
swAuthUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthUserPassword.setStatus("current")
_SwAuthUserStatus_Type = RowStatus
_SwAuthUserStatus_Object = MibTableColumn
swAuthUserStatus = _SwAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 3, 1, 1, 3),
    _SwAuthUserStatus_Type()
)
swAuthUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthUserStatus.setStatus("current")
_SwAuthRadiusServer_ObjectIdentity = ObjectIdentity
swAuthRadiusServer = _SwAuthRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4)
)
_SwAuthRadiusServerTable_Object = MibTable
swAuthRadiusServerTable = _SwAuthRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2)
)
if mibBuilder.loadTexts:
    swAuthRadiusServerTable.setStatus("current")
_SwAuthRadiusServerEntry_Object = MibTableRow
swAuthRadiusServerEntry = _SwAuthRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1)
)
swAuthRadiusServerEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "swAuthRadiusServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 1),
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
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SwAuthRadiusIPType_Type.__name__ = "Integer32"
_SwAuthRadiusIPType_Object = MibTableColumn
swAuthRadiusIPType = _SwAuthRadiusIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 2),
    _SwAuthRadiusIPType_Type()
)
swAuthRadiusIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusIPType.setStatus("current")
_SwAuthRadiusServerAddress_Type = Ipv6Address
_SwAuthRadiusServerAddress_Object = MibTableColumn
swAuthRadiusServerAddress = _SwAuthRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 3),
    _SwAuthRadiusServerAddress_Type()
)
swAuthRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerAddress.setStatus("current")
_SwAuthRadiusServerInterfaceName_Type = OctetString
_SwAuthRadiusServerInterfaceName_Object = MibTableColumn
swAuthRadiusServerInterfaceName = _SwAuthRadiusServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 9),
    _SwAuthRadiusServerKey_Type()
)
swAuthRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthRadiusServerKey.setStatus("current")
_SwAuthRadiusServerStatus_Type = RowStatus
_SwAuthRadiusServerStatus_Object = MibTableColumn
swAuthRadiusServerStatus = _SwAuthRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 23, 4, 2, 1, 10),
    _SwAuthRadiusServerStatus_Type()
)
swAuthRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swAuthRadiusServerStatus.setStatus("current")
_CompanyGuestVlan_ObjectIdentity = ObjectIdentity
companyGuestVlan = _CompanyGuestVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 24)
)


class _GuestVlanName_Type(DisplayString):
    """Custom type guestVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GuestVlanName_Type.__name__ = "DisplayString"
_GuestVlanName_Object = MibScalar
guestVlanName = _GuestVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 24, 1),
    _GuestVlanName_Type()
)
guestVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guestVlanName.setStatus("current")
_GuestVlanPort_Type = PortList
_GuestVlanPort_Object = MibScalar
guestVlanPort = _GuestVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 24, 2),
    _GuestVlanPort_Type()
)
guestVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guestVlanPort.setStatus("current")


class _GuestVlanDelState_Type(Integer32):
    """Custom type guestVlanDelState based on Integer32"""
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


_GuestVlanDelState_Type.__name__ = "Integer32"
_GuestVlanDelState_Object = MibScalar
guestVlanDelState = _GuestVlanDelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 24, 3),
    _GuestVlanDelState_Type()
)
guestVlanDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    guestVlanDelState.setStatus("current")
_CompanyMacNotify_ObjectIdentity = ObjectIdentity
companyMacNotify = _CompanyMacNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25)
)


class _MacNotifyState_Type(Integer32):
    """Custom type macNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MacNotifyState_Type.__name__ = "Integer32"
_MacNotifyState_Object = MibScalar
macNotifyState = _MacNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 1),
    _MacNotifyState_Type()
)
macNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macNotifyState.setStatus("current")


class _MacNotifyInterval_Type(Integer32):
    """Custom type macNotifyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MacNotifyInterval_Type.__name__ = "Integer32"
_MacNotifyInterval_Object = MibScalar
macNotifyInterval = _MacNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 2),
    _MacNotifyInterval_Type()
)
macNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macNotifyInterval.setStatus("current")


class _MacNotifyHistorySize_Type(Integer32):
    """Custom type macNotifyHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_MacNotifyHistorySize_Type.__name__ = "Integer32"
_MacNotifyHistorySize_Object = MibScalar
macNotifyHistorySize = _MacNotifyHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 3),
    _MacNotifyHistorySize_Type()
)
macNotifyHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macNotifyHistorySize.setStatus("current")
_MacNotifyCtrlTable_Object = MibTable
macNotifyCtrlTable = _MacNotifyCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 4)
)
if mibBuilder.loadTexts:
    macNotifyCtrlTable.setStatus("current")
_MacNotifyCtrlEntry_Object = MibTableRow
macNotifyCtrlEntry = _MacNotifyCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 4, 1)
)
macNotifyCtrlEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "macNotifyCtrlIndex"),
)
if mibBuilder.loadTexts:
    macNotifyCtrlEntry.setStatus("current")


class _MacNotifyCtrlIndex_Type(Integer32):
    """Custom type macNotifyCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MacNotifyCtrlIndex_Type.__name__ = "Integer32"
_MacNotifyCtrlIndex_Object = MibTableColumn
macNotifyCtrlIndex = _MacNotifyCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 4, 1, 1),
    _MacNotifyCtrlIndex_Type()
)
macNotifyCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macNotifyCtrlIndex.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 4, 1, 2),
    _MacNotifyPortStatus_Type()
)
macNotifyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macNotifyPortStatus.setStatus("current")
_MacNotifyInfo_ObjectIdentity = ObjectIdentity
macNotifyInfo = _MacNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 5)
)


class _MacNotifyInfoDiscription_Type(OctetString):
    """Custom type macNotifyInfoDiscription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_MacNotifyInfoDiscription_Type.__name__ = "OctetString"
_MacNotifyInfoDiscription_Object = MibScalar
macNotifyInfoDiscription = _MacNotifyInfoDiscription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 25, 5, 1),
    _MacNotifyInfoDiscription_Type()
)
macNotifyInfoDiscription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    macNotifyInfoDiscription.setStatus("current")
_CompanyISMVLAN_ObjectIdentity = ObjectIdentity
companyISMVLAN = _CompanyISMVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27)
)


class _IgmpMulticastVlanStatus_Type(Integer32):
    """Custom type igmpMulticastVlanStatus based on Integer32"""
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


_IgmpMulticastVlanStatus_Type.__name__ = "Integer32"
_IgmpMulticastVlanStatus_Object = MibScalar
igmpMulticastVlanStatus = _IgmpMulticastVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 1),
    _IgmpMulticastVlanStatus_Type()
)
igmpMulticastVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMulticastVlanStatus.setStatus("current")
_MulticastVlanTable_Object = MibTable
multicastVlanTable = _MulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4)
)
if mibBuilder.loadTexts:
    multicastVlanTable.setStatus("current")
_MulticastVlanEntry_Object = MibTableRow
multicastVlanEntry = _MulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1)
)
multicastVlanEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "multicastVlanid"),
)
if mibBuilder.loadTexts:
    multicastVlanEntry.setStatus("current")


class _MulticastVlanid_Type(Integer32):
    """Custom type multicastVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_MulticastVlanid_Type.__name__ = "Integer32"
_MulticastVlanid_Object = MibTableColumn
multicastVlanid = _MulticastVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 1),
    _MulticastVlanid_Type()
)
multicastVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanid.setStatus("current")


class _MulticastVlanName_Type(DisplayString):
    """Custom type multicastVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MulticastVlanName_Type.__name__ = "DisplayString"
_MulticastVlanName_Object = MibTableColumn
multicastVlanName = _MulticastVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 2),
    _MulticastVlanName_Type()
)
multicastVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastVlanName.setStatus("current")
_MulticastVlanSourcePort_Type = PortList
_MulticastVlanSourcePort_Object = MibTableColumn
multicastVlanSourcePort = _MulticastVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 3),
    _MulticastVlanSourcePort_Type()
)
multicastVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVlanSourcePort.setStatus("current")
_MulticastVlanMemberPort_Type = PortList
_MulticastVlanMemberPort_Object = MibTableColumn
multicastVlanMemberPort = _MulticastVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 4),
    _MulticastVlanMemberPort_Type()
)
multicastVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVlanMemberPort.setStatus("current")
_MulticastVlanTagMemberPort_Type = PortList
_MulticastVlanTagMemberPort_Object = MibTableColumn
multicastVlanTagMemberPort = _MulticastVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 5),
    _MulticastVlanTagMemberPort_Type()
)
multicastVlanTagMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVlanTagMemberPort.setStatus("current")


class _MulticastVlanState_Type(Integer32):
    """Custom type multicastVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MulticastVlanState_Type.__name__ = "Integer32"
_MulticastVlanState_Object = MibTableColumn
multicastVlanState = _MulticastVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 6),
    _MulticastVlanState_Type()
)
multicastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVlanState.setStatus("current")
_MulticastVlanIgmpReplaceSourceIp_Type = IpAddress
_MulticastVlanIgmpReplaceSourceIp_Object = MibTableColumn
multicastVlanIgmpReplaceSourceIp = _MulticastVlanIgmpReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 7),
    _MulticastVlanIgmpReplaceSourceIp_Type()
)
multicastVlanIgmpReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVlanIgmpReplaceSourceIp.setStatus("current")
_MulticastVlanMldReplaceSourceIp_Type = Ipv6Address
_MulticastVlanMldReplaceSourceIp_Object = MibTableColumn
multicastVlanMldReplaceSourceIp = _MulticastVlanMldReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 8),
    _MulticastVlanMldReplaceSourceIp_Type()
)
multicastVlanMldReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVlanMldReplaceSourceIp.setStatus("current")
_MulticastVlanRowStatus_Type = RowStatus
_MulticastVlanRowStatus_Object = MibTableColumn
multicastVlanRowStatus = _MulticastVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 4, 1, 9),
    _MulticastVlanRowStatus_Type()
)
multicastVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastVlanRowStatus.setStatus("current")
_MulticastVlanGroupTable_Object = MibTable
multicastVlanGroupTable = _MulticastVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 5)
)
if mibBuilder.loadTexts:
    multicastVlanGroupTable.setStatus("current")
_MulticastVlanGroupEntry_Object = MibTableRow
multicastVlanGroupEntry = _MulticastVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 5, 1)
)
multicastVlanGroupEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "multicastVlanGroupVid"),
    (0, "DGS-1100-06ME-AX", "multicastVlanGroupIpType"),
    (0, "DGS-1100-06ME-AX", "multicastVlanGroupFromIp"),
    (0, "DGS-1100-06ME-AX", "multicastVlanGroupToIp"),
)
if mibBuilder.loadTexts:
    multicastVlanGroupEntry.setStatus("current")


class _MulticastVlanGroupVid_Type(Integer32):
    """Custom type multicastVlanGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MulticastVlanGroupVid_Type.__name__ = "Integer32"
_MulticastVlanGroupVid_Object = MibTableColumn
multicastVlanGroupVid = _MulticastVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 5, 1, 1),
    _MulticastVlanGroupVid_Type()
)
multicastVlanGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanGroupVid.setStatus("current")


class _MulticastVlanGroupIpType_Type(Integer32):
    """Custom type multicastVlanGroupIpType based on Integer32"""
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


_MulticastVlanGroupIpType_Type.__name__ = "Integer32"
_MulticastVlanGroupIpType_Object = MibTableColumn
multicastVlanGroupIpType = _MulticastVlanGroupIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 5, 1, 2),
    _MulticastVlanGroupIpType_Type()
)
multicastVlanGroupIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanGroupIpType.setStatus("current")
_MulticastVlanGroupFromIp_Type = Ipv6Address
_MulticastVlanGroupFromIp_Object = MibTableColumn
multicastVlanGroupFromIp = _MulticastVlanGroupFromIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 5, 1, 3),
    _MulticastVlanGroupFromIp_Type()
)
multicastVlanGroupFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanGroupFromIp.setStatus("current")
_MulticastVlanGroupToIp_Type = Ipv6Address
_MulticastVlanGroupToIp_Object = MibTableColumn
multicastVlanGroupToIp = _MulticastVlanGroupToIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 5, 1, 4),
    _MulticastVlanGroupToIp_Type()
)
multicastVlanGroupToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanGroupToIp.setStatus("current")
_MulticastVlanGroupStatus_Type = RowStatus
_MulticastVlanGroupStatus_Object = MibTableColumn
multicastVlanGroupStatus = _MulticastVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 27, 5, 1, 5),
    _MulticastVlanGroupStatus_Type()
)
multicastVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastVlanGroupStatus.setStatus("current")
_CompanyDHCPRelay_ObjectIdentity = ObjectIdentity
companyDHCPRelay = _CompanyDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28)
)
_DhcpBOOTPRelayControl_ObjectIdentity = ObjectIdentity
dhcpBOOTPRelayControl = _DhcpBOOTPRelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1)
)


class _DhcpBOOTPRelayState_Type(Integer32):
    """Custom type dhcpBOOTPRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DhcpBOOTPRelayState_Type.__name__ = "Integer32"
_DhcpBOOTPRelayState_Object = MibScalar
dhcpBOOTPRelayState = _DhcpBOOTPRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 1),
    _DhcpBOOTPRelayState_Type()
)
dhcpBOOTPRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayState.setStatus("current")


class _DhcpBOOTPRelayHopCount_Type(Integer32):
    """Custom type dhcpBOOTPRelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DhcpBOOTPRelayHopCount_Type.__name__ = "Integer32"
_DhcpBOOTPRelayHopCount_Object = MibScalar
dhcpBOOTPRelayHopCount = _DhcpBOOTPRelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 2),
    _DhcpBOOTPRelayHopCount_Type()
)
dhcpBOOTPRelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayHopCount.setStatus("current")


class _DhcpBOOTPRelayTimeThreshold_Type(Integer32):
    """Custom type dhcpBOOTPRelayTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpBOOTPRelayTimeThreshold_Type.__name__ = "Integer32"
_DhcpBOOTPRelayTimeThreshold_Object = MibScalar
dhcpBOOTPRelayTimeThreshold = _DhcpBOOTPRelayTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 3),
    _DhcpBOOTPRelayTimeThreshold_Type()
)
dhcpBOOTPRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayTimeThreshold.setStatus("current")
_DhcpBOOTPRelayEnablePortlist_Type = PortList
_DhcpBOOTPRelayEnablePortlist_Object = MibScalar
dhcpBOOTPRelayEnablePortlist = _DhcpBOOTPRelayEnablePortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 4),
    _DhcpBOOTPRelayEnablePortlist_Type()
)
dhcpBOOTPRelayEnablePortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayEnablePortlist.setStatus("current")
_DhcpRelayVlanTable_Object = MibTable
dhcpRelayVlanTable = _DhcpRelayVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 5)
)
if mibBuilder.loadTexts:
    dhcpRelayVlanTable.setStatus("current")
_DhcpRelayVlanTableEntry_Object = MibTableRow
dhcpRelayVlanTableEntry = _DhcpRelayVlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 5, 1)
)
dhcpRelayVlanTableEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "dhcpRelayVlanSettingsVLANID"),
)
if mibBuilder.loadTexts:
    dhcpRelayVlanTableEntry.setStatus("current")


class _DhcpRelayVlanSettingsVLANID_Type(Integer32):
    """Custom type dhcpRelayVlanSettingsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpRelayVlanSettingsVLANID_Type.__name__ = "Integer32"
_DhcpRelayVlanSettingsVLANID_Object = MibTableColumn
dhcpRelayVlanSettingsVLANID = _DhcpRelayVlanSettingsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 5, 1, 1),
    _DhcpRelayVlanSettingsVLANID_Type()
)
dhcpRelayVlanSettingsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayVlanSettingsVLANID.setStatus("current")


class _DhcpRelayVlanSettingsState_Type(Integer32):
    """Custom type dhcpRelayVlanSettingsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DhcpRelayVlanSettingsState_Type.__name__ = "Integer32"
_DhcpRelayVlanSettingsState_Object = MibTableColumn
dhcpRelayVlanSettingsState = _DhcpRelayVlanSettingsState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 1, 5, 1, 2),
    _DhcpRelayVlanSettingsState_Type()
)
dhcpRelayVlanSettingsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayVlanSettingsState.setStatus("current")
_DhcpBOOTPRelayManagement_ObjectIdentity = ObjectIdentity
dhcpBOOTPRelayManagement = _DhcpBOOTPRelayManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2)
)
_DhcpBOOTPRelayInterfaceSettingsTable_Object = MibTable
dhcpBOOTPRelayInterfaceSettingsTable = _DhcpBOOTPRelayInterfaceSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpBOOTPRelayInterfaceSettingsTable.setStatus("current")
_DhcpBOOTPRelayInterfaceSettingsEntry_Object = MibTableRow
dhcpBOOTPRelayInterfaceSettingsEntry = _DhcpBOOTPRelayInterfaceSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 1, 1)
)
dhcpBOOTPRelayInterfaceSettingsEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "dhcpBOOTPRelayInterface"),
    (0, "DGS-1100-06ME-AX", "dhcpBOOTPRelayServerIP"),
)
if mibBuilder.loadTexts:
    dhcpBOOTPRelayInterfaceSettingsEntry.setStatus("current")


class _DhcpBOOTPRelayInterface_Type(DisplayString):
    """Custom type dhcpBOOTPRelayInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DhcpBOOTPRelayInterface_Type.__name__ = "DisplayString"
_DhcpBOOTPRelayInterface_Object = MibTableColumn
dhcpBOOTPRelayInterface = _DhcpBOOTPRelayInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 1, 1, 1),
    _DhcpBOOTPRelayInterface_Type()
)
dhcpBOOTPRelayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayInterface.setStatus("current")
_DhcpBOOTPRelayServerIP_Type = IpAddress
_DhcpBOOTPRelayServerIP_Object = MibTableColumn
dhcpBOOTPRelayServerIP = _DhcpBOOTPRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 1, 1, 2),
    _DhcpBOOTPRelayServerIP_Type()
)
dhcpBOOTPRelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayServerIP.setStatus("current")
_DhcpBOOTPRelayInterfaceSettingsRowStatus_Type = RowStatus
_DhcpBOOTPRelayInterfaceSettingsRowStatus_Object = MibTableColumn
dhcpBOOTPRelayInterfaceSettingsRowStatus = _DhcpBOOTPRelayInterfaceSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 1, 1, 3),
    _DhcpBOOTPRelayInterfaceSettingsRowStatus_Type()
)
dhcpBOOTPRelayInterfaceSettingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayInterfaceSettingsRowStatus.setStatus("current")
_DhcpBOOTPRelayManagementOption82_ObjectIdentity = ObjectIdentity
dhcpBOOTPRelayManagementOption82 = _DhcpBOOTPRelayManagementOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 2)
)


class _DhcpBOOTPRelayOption82State_Type(Integer32):
    """Custom type dhcpBOOTPRelayOption82State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DhcpBOOTPRelayOption82State_Type.__name__ = "Integer32"
_DhcpBOOTPRelayOption82State_Object = MibScalar
dhcpBOOTPRelayOption82State = _DhcpBOOTPRelayOption82State_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 2, 1),
    _DhcpBOOTPRelayOption82State_Type()
)
dhcpBOOTPRelayOption82State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayOption82State.setStatus("current")


class _DhcpBOOTPRelayOption82CheckState_Type(Integer32):
    """Custom type dhcpBOOTPRelayOption82CheckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DhcpBOOTPRelayOption82CheckState_Type.__name__ = "Integer32"
_DhcpBOOTPRelayOption82CheckState_Object = MibScalar
dhcpBOOTPRelayOption82CheckState = _DhcpBOOTPRelayOption82CheckState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 2, 2),
    _DhcpBOOTPRelayOption82CheckState_Type()
)
dhcpBOOTPRelayOption82CheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayOption82CheckState.setStatus("current")


class _DhcpBOOTPRelayOption82Policy_Type(Integer32):
    """Custom type dhcpBOOTPRelayOption82Policy based on Integer32"""
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


_DhcpBOOTPRelayOption82Policy_Type.__name__ = "Integer32"
_DhcpBOOTPRelayOption82Policy_Object = MibScalar
dhcpBOOTPRelayOption82Policy = _DhcpBOOTPRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 2, 3),
    _DhcpBOOTPRelayOption82Policy_Type()
)
dhcpBOOTPRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayOption82Policy.setStatus("current")


class _DhcpBOOTPRelayOption82RemoteIDType_Type(Integer32):
    """Custom type dhcpBOOTPRelayOption82RemoteIDType based on Integer32"""
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


_DhcpBOOTPRelayOption82RemoteIDType_Type.__name__ = "Integer32"
_DhcpBOOTPRelayOption82RemoteIDType_Object = MibScalar
dhcpBOOTPRelayOption82RemoteIDType = _DhcpBOOTPRelayOption82RemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 2, 4),
    _DhcpBOOTPRelayOption82RemoteIDType_Type()
)
dhcpBOOTPRelayOption82RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayOption82RemoteIDType.setStatus("current")
_DhcpBOOTPRelayOption82RemoteID_Type = DisplayString
_DhcpBOOTPRelayOption82RemoteID_Object = MibScalar
dhcpBOOTPRelayOption82RemoteID = _DhcpBOOTPRelayOption82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 28, 2, 2, 5),
    _DhcpBOOTPRelayOption82RemoteID_Type()
)
dhcpBOOTPRelayOption82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpBOOTPRelayOption82RemoteID.setStatus("current")
_CompanyDHCPLocalRelay_ObjectIdentity = ObjectIdentity
companyDHCPLocalRelay = _CompanyDHCPLocalRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 29)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 29, 1),
    _DhcpLocalRelayGlobalState_Type()
)
dhcpLocalRelayGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelayGlobalState.setStatus("current")
_DhcpLocalRelayTable_Object = MibTable
dhcpLocalRelayTable = _DhcpLocalRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 29, 2)
)
if mibBuilder.loadTexts:
    dhcpLocalRelayTable.setStatus("current")
_DhcpLocalRelayTableEntry_Object = MibTableRow
dhcpLocalRelayTableEntry = _DhcpLocalRelayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 29, 2, 1)
)
dhcpLocalRelayTableEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "dhcpLocalRelaySettingsVLANID"),
)
if mibBuilder.loadTexts:
    dhcpLocalRelayTableEntry.setStatus("current")


class _DhcpLocalRelaySettingsVLANID_Type(Integer32):
    """Custom type dhcpLocalRelaySettingsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpLocalRelaySettingsVLANID_Type.__name__ = "Integer32"
_DhcpLocalRelaySettingsVLANID_Object = MibTableColumn
dhcpLocalRelaySettingsVLANID = _DhcpLocalRelaySettingsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 29, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 29, 2, 1, 2),
    _DhcpLocalRelaySettingsState_Type()
)
dhcpLocalRelaySettingsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelaySettingsState.setStatus("current")
_DhcpLocalRelayEnablePortlist_Type = PortList
_DhcpLocalRelayEnablePortlist_Object = MibScalar
dhcpLocalRelayEnablePortlist = _DhcpLocalRelayEnablePortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 29, 3),
    _DhcpLocalRelayEnablePortlist_Type()
)
dhcpLocalRelayEnablePortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLocalRelayEnablePortlist.setStatus("current")
_CompanyTrapSetting_ObjectIdentity = ObjectIdentity
companyTrapSetting = _CompanyTrapSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30)
)
_SysTrapIP_Type = IpAddress
_SysTrapIP_Object = MibScalar
sysTrapIP = _SysTrapIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30, 2),
    _SysTrapSystemEvent_Type()
)
sysTrapSystemEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapSystemEvent.setStatus("current")


class _SysTrapFiberPortEvent_Type(Integer32):
    """Custom type sysTrapFiberPortEvent based on Integer32"""
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


_SysTrapFiberPortEvent_Type.__name__ = "Integer32"
_SysTrapFiberPortEvent_Object = MibScalar
sysTrapFiberPortEvent = _SysTrapFiberPortEvent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30, 3),
    _SysTrapFiberPortEvent_Type()
)
sysTrapFiberPortEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapFiberPortEvent.setStatus("current")


class _SysTrapTwistedPortEvent_Type(Integer32):
    """Custom type sysTrapTwistedPortEvent based on Integer32"""
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


_SysTrapTwistedPortEvent_Type.__name__ = "Integer32"
_SysTrapTwistedPortEvent_Object = MibScalar
sysTrapTwistedPortEvent = _SysTrapTwistedPortEvent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30, 4),
    _SysTrapTwistedPortEvent_Type()
)
sysTrapTwistedPortEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapTwistedPortEvent.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30, 10),
    _SysTrapStatus_Type()
)
sysTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapStatus.setStatus("current")


class _SysTrapPortSecurity_Type(Integer32):
    """Custom type sysTrapPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysTrapPortSecurity_Type.__name__ = "Integer32"
_SysTrapPortSecurity_Object = MibScalar
sysTrapPortSecurity = _SysTrapPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30, 13),
    _SysTrapPortSecurity_Type()
)
sysTrapPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPortSecurity.setStatus("current")


class _SysTrapLBD_Type(Integer32):
    """Custom type sysTrapLBD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysTrapLBD_Type.__name__ = "Integer32"
_SysTrapLBD_Object = MibScalar
sysTrapLBD = _SysTrapLBD_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 30, 15),
    _SysTrapLBD_Type()
)
sysTrapLBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapLBD.setStatus("current")
_CompanyGreenSetting_ObjectIdentity = ObjectIdentity
companyGreenSetting = _CompanyGreenSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31)
)
_DlinkGreenLEDShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenLEDShutoff = _DlinkGreenLEDShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 1)
)
_DlinkGreenLEDShutoffPortList_Type = PortList
_DlinkGreenLEDShutoffPortList_Object = MibScalar
dlinkGreenLEDShutoffPortList = _DlinkGreenLEDShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 1, 4),
    _DlinkGreenLEDShutoffTimeProfile2_Type()
)
dlinkGreenLEDShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenLEDShutoffTimeProfile2.setStatus("current")
_DlinkGreenPortShutoff_ObjectIdentity = ObjectIdentity
dlinkGreenPortShutoff = _DlinkGreenPortShutoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 2)
)
_DlinkGreenPortShutoffPortList_Type = PortList
_DlinkGreenPortShutoffPortList_Object = MibScalar
dlinkGreenPortShutoffPortList = _DlinkGreenPortShutoffPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 2, 4),
    _DlinkGreenPortShutoffTimeProfile2_Type()
)
dlinkGreenPortShutoffTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenPortShutoffTimeProfile2.setStatus("current")
_DlinkGreenSystemHibernation_ObjectIdentity = ObjectIdentity
dlinkGreenSystemHibernation = _DlinkGreenSystemHibernation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 4, 3),
    _DlinkGreenSystemHibernationTimeProfile2_Type()
)
dlinkGreenSystemHibernationTimeProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkGreenSystemHibernationTimeProfile2.setStatus("current")


class _DlinkPowerSavCableLenDetectionState_Type(Integer32):
    """Custom type dlinkPowerSavCableLenDetectionState based on Integer32"""
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


_DlinkPowerSavCableLenDetectionState_Type.__name__ = "Integer32"
_DlinkPowerSavCableLenDetectionState_Object = MibScalar
dlinkPowerSavCableLenDetectionState = _DlinkPowerSavCableLenDetectionState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 31, 5),
    _DlinkPowerSavCableLenDetectionState_Type()
)
dlinkPowerSavCableLenDetectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinkPowerSavCableLenDetectionState.setStatus("current")
_CompanyLLDPSetting_ObjectIdentity = ObjectIdentity
companyLLDPSetting = _CompanyLLDPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 5),
    _DlinklldpTxDelay_Type()
)
dlinklldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpTxDelay.setStatus("current")
_DlinklldpConfigManAddrPortsTxEnable_Type = PortList
_DlinklldpConfigManAddrPortsTxEnable_Object = MibScalar
dlinklldpConfigManAddrPortsTxEnable = _DlinklldpConfigManAddrPortsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 6),
    _DlinklldpConfigManAddrPortsTxEnable_Type()
)
dlinklldpConfigManAddrPortsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlinklldpConfigManAddrPortsTxEnable.setStatus("current")
_LldpPortConfigTable_Object = MibTable
lldpPortConfigTable = _LldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 11)
)
if mibBuilder.loadTexts:
    lldpPortConfigTable.setStatus("current")
_LldpPortConfigEntry_Object = MibTableRow
lldpPortConfigEntry = _LldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 11, 1)
)
lldpPortConfigEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpPortConfigEntry.setStatus("current")
_LldpPortConfigPortNum_Type = LldpPortNumber
_LldpPortConfigPortNum_Object = MibTableColumn
lldpPortConfigPortNum = _LldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 11, 1, 1),
    _LldpPortConfigPortNum_Type()
)
lldpPortConfigPortNum.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 11, 1, 2),
    _LldpPortConfigAdminStatus_Type()
)
lldpPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigAdminStatus.setStatus("current")


class _LldpPortConfigNotificationEnable_Type(TruthValue):
    """Custom type lldpPortConfigNotificationEnable based on TruthValue"""


_LldpPortConfigNotificationEnable_Object = MibTableColumn
lldpPortConfigNotificationEnable = _LldpPortConfigNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 11, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 11, 1, 4),
    _LldpPortConfigTLVsTxEnable_Type()
)
lldpPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigTLVsTxEnable.setStatus("current")
_LldpXdot3Objects_ObjectIdentity = ObjectIdentity
lldpXdot3Objects = _LldpXdot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12)
)
_LldpXdot3Config_ObjectIdentity = ObjectIdentity
lldpXdot3Config = _LldpXdot3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 1)
)
_LldpXdot3PortConfigTable_Object = MibTable
lldpXdot3PortConfigTable = _LldpXdot3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTable.setStatus("current")
_LldpXdot3PortConfigEntry_Object = MibTableRow
lldpXdot3PortConfigEntry = _LldpXdot3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3PortConfigEntry.setStatus("current")


class _LldpXdot3PortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpXdot3PortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("linkAggregation", 2),
          ("macPhyConfigStatus", 0),
          ("maxFrameSize", 3),
          ("powerViaMDI", 1))
    )

_LldpXdot3PortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpXdot3PortConfigTLVsTxEnable_Object = MibTableColumn
lldpXdot3PortConfigTLVsTxEnable = _LldpXdot3PortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 1, 1, 1, 1),
    _LldpXdot3PortConfigTLVsTxEnable_Type()
)
lldpXdot3PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot3PortConfigTLVsTxEnable.setStatus("current")
_LldpXdot3LocalData_ObjectIdentity = ObjectIdentity
lldpXdot3LocalData = _LldpXdot3LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2)
)
_LldpXdot3LocPortTable_Object = MibTable
lldpXdot3LocPortTable = _LldpXdot3LocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortTable.setStatus("current")
_LldpXdot3LocPortEntry_Object = MibTableRow
lldpXdot3LocPortEntry = _LldpXdot3LocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 1, 1)
)
lldpXdot3LocPortEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3LocPortAutoNegSupported"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPortEntry.setStatus("current")
_LldpXdot3LocPortAutoNegSupported_Type = TruthValue
_LldpXdot3LocPortAutoNegSupported_Object = MibTableColumn
lldpXdot3LocPortAutoNegSupported = _LldpXdot3LocPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 1, 1, 1),
    _LldpXdot3LocPortAutoNegSupported_Type()
)
lldpXdot3LocPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortAutoNegSupported.setStatus("current")
_LldpXdot3LocPortAutoNegEnabled_Type = TruthValue
_LldpXdot3LocPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3LocPortAutoNegEnabled = _LldpXdot3LocPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 1, 1, 4),
    _LldpXdot3LocPortOperMauType_Type()
)
lldpXdot3LocPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPortOperMauType.setStatus("current")
_LldpXdot3LocPowerTable_Object = MibTable
lldpXdot3LocPowerTable = _LldpXdot3LocPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerTable.setStatus("current")
_LldpXdot3LocPowerEntry_Object = MibTableRow
lldpXdot3LocPowerEntry = _LldpXdot3LocPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2, 1)
)
lldpXdot3LocPowerEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3LocPowerPortClass"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocPowerEntry.setStatus("current")
_LldpXdot3LocPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3LocPowerPortClass_Object = MibTableColumn
lldpXdot3LocPowerPortClass = _LldpXdot3LocPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2, 1, 1),
    _LldpXdot3LocPowerPortClass_Type()
)
lldpXdot3LocPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPortClass.setStatus("current")
_LldpXdot3LocPowerMDISupported_Type = TruthValue
_LldpXdot3LocPowerMDISupported_Object = MibTableColumn
lldpXdot3LocPowerMDISupported = _LldpXdot3LocPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2, 1, 2),
    _LldpXdot3LocPowerMDISupported_Type()
)
lldpXdot3LocPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDISupported.setStatus("current")
_LldpXdot3LocPowerMDIEnabled_Type = TruthValue
_LldpXdot3LocPowerMDIEnabled_Object = MibTableColumn
lldpXdot3LocPowerMDIEnabled = _LldpXdot3LocPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2, 1, 3),
    _LldpXdot3LocPowerMDIEnabled_Type()
)
lldpXdot3LocPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerMDIEnabled.setStatus("current")
_LldpXdot3LocPowerPairControlable_Type = TruthValue
_LldpXdot3LocPowerPairControlable_Object = MibTableColumn
lldpXdot3LocPowerPairControlable = _LldpXdot3LocPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2, 1, 4),
    _LldpXdot3LocPowerPairControlable_Type()
)
lldpXdot3LocPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPairControlable.setStatus("current")


class _LldpXdot3LocPowerPairs_Type(Integer32):
    """Custom type lldpXdot3LocPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpXdot3LocPowerPairs_Type.__name__ = "Integer32"
_LldpXdot3LocPowerPairs_Object = MibTableColumn
lldpXdot3LocPowerPairs = _LldpXdot3LocPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2, 1, 5),
    _LldpXdot3LocPowerPairs_Type()
)
lldpXdot3LocPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerPairs.setStatus("current")


class _LldpXdot3LocPowerClass_Type(Integer32):
    """Custom type lldpXdot3LocPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpXdot3LocPowerClass_Type.__name__ = "Integer32"
_LldpXdot3LocPowerClass_Object = MibTableColumn
lldpXdot3LocPowerClass = _LldpXdot3LocPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 2, 1, 6),
    _LldpXdot3LocPowerClass_Type()
)
lldpXdot3LocPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocPowerClass.setStatus("current")
_LldpXdot3LocLinkAggTable_Object = MibTable
lldpXdot3LocLinkAggTable = _LldpXdot3LocLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggTable.setStatus("current")
_LldpXdot3LocLinkAggEntry_Object = MibTableRow
lldpXdot3LocLinkAggEntry = _LldpXdot3LocLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 3, 1)
)
lldpXdot3LocLinkAggEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3LocLinkAggStatus"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggEntry.setStatus("current")
_LldpXdot3LocLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3LocLinkAggStatus_Object = MibTableColumn
lldpXdot3LocLinkAggStatus = _LldpXdot3LocLinkAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 3, 1, 1),
    _LldpXdot3LocLinkAggStatus_Type()
)
lldpXdot3LocLinkAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggStatus.setStatus("current")


class _LldpXdot3LocLinkAggPortId_Type(Integer32):
    """Custom type lldpXdot3LocLinkAggPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot3LocLinkAggPortId_Type.__name__ = "Integer32"
_LldpXdot3LocLinkAggPortId_Object = MibTableColumn
lldpXdot3LocLinkAggPortId = _LldpXdot3LocLinkAggPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 3, 1, 2),
    _LldpXdot3LocLinkAggPortId_Type()
)
lldpXdot3LocLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocLinkAggPortId.setStatus("current")
_LldpXdot3LocMaxFrameSizeTable_Object = MibTable
lldpXdot3LocMaxFrameSizeTable = _LldpXdot3LocMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeTable.setStatus("current")
_LldpXdot3LocMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3LocMaxFrameSizeEntry = _LldpXdot3LocMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 4, 1)
)
lldpXdot3LocMaxFrameSizeEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3LocMaxFrameSize"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSizeEntry.setStatus("current")


class _LldpXdot3LocMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3LocMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3LocMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3LocMaxFrameSize_Object = MibTableColumn
lldpXdot3LocMaxFrameSize = _LldpXdot3LocMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 2, 4, 1, 1),
    _LldpXdot3LocMaxFrameSize_Type()
)
lldpXdot3LocMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3LocMaxFrameSize.setStatus("current")
_LldpXdot3RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot3RemoteData = _LldpXdot3RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3)
)
_LldpXdot3RemPortTable_Object = MibTable
lldpXdot3RemPortTable = _LldpXdot3RemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortTable.setStatus("current")
_LldpXdot3RemPortEntry_Object = MibTableRow
lldpXdot3RemPortEntry = _LldpXdot3RemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 1, 1)
)
lldpXdot3RemPortEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3RemPortAutoNegSupported"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPortEntry.setStatus("current")
_LldpXdot3RemPortAutoNegSupported_Type = TruthValue
_LldpXdot3RemPortAutoNegSupported_Object = MibTableColumn
lldpXdot3RemPortAutoNegSupported = _LldpXdot3RemPortAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 1, 1, 1),
    _LldpXdot3RemPortAutoNegSupported_Type()
)
lldpXdot3RemPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortAutoNegSupported.setStatus("current")
_LldpXdot3RemPortAutoNegEnabled_Type = TruthValue
_LldpXdot3RemPortAutoNegEnabled_Object = MibTableColumn
lldpXdot3RemPortAutoNegEnabled = _LldpXdot3RemPortAutoNegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 1, 1, 4),
    _LldpXdot3RemPortOperMauType_Type()
)
lldpXdot3RemPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPortOperMauType.setStatus("current")
_LldpXdot3RemPowerTable_Object = MibTable
lldpXdot3RemPowerTable = _LldpXdot3RemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerTable.setStatus("current")
_LldpXdot3RemPowerEntry_Object = MibTableRow
lldpXdot3RemPowerEntry = _LldpXdot3RemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2, 1)
)
lldpXdot3RemPowerEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3RemPowerPortClass"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemPowerEntry.setStatus("current")
_LldpXdot3RemPowerPortClass_Type = LldpPowerPortClass
_LldpXdot3RemPowerPortClass_Object = MibTableColumn
lldpXdot3RemPowerPortClass = _LldpXdot3RemPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2, 1, 1),
    _LldpXdot3RemPowerPortClass_Type()
)
lldpXdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerPortClass.setStatus("current")
_LldpXdot3RemPowerMDISupported_Type = TruthValue
_LldpXdot3RemPowerMDISupported_Object = MibTableColumn
lldpXdot3RemPowerMDISupported = _LldpXdot3RemPowerMDISupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2, 1, 2),
    _LldpXdot3RemPowerMDISupported_Type()
)
lldpXdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDISupported.setStatus("current")
_LldpXdot3RemPowerMDIEnabled_Type = TruthValue
_LldpXdot3RemPowerMDIEnabled_Object = MibTableColumn
lldpXdot3RemPowerMDIEnabled = _LldpXdot3RemPowerMDIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2, 1, 3),
    _LldpXdot3RemPowerMDIEnabled_Type()
)
lldpXdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerMDIEnabled.setStatus("current")
_LldpXdot3RemPowerPairControlable_Type = TruthValue
_LldpXdot3RemPowerPairControlable_Object = MibTableColumn
lldpXdot3RemPowerPairControlable = _LldpXdot3RemPowerPairControlable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 2, 1, 6),
    _LldpXdot3RemPowerClass_Type()
)
lldpXdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemPowerClass.setStatus("current")
_LldpXdot3RemLinkAggTable_Object = MibTable
lldpXdot3RemLinkAggTable = _LldpXdot3RemLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggTable.setStatus("current")
_LldpXdot3RemLinkAggEntry_Object = MibTableRow
lldpXdot3RemLinkAggEntry = _LldpXdot3RemLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 3, 1)
)
lldpXdot3RemLinkAggEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3RemLinkAggStatus"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggEntry.setStatus("current")
_LldpXdot3RemLinkAggStatus_Type = LldpLinkAggStatusMap
_LldpXdot3RemLinkAggStatus_Object = MibTableColumn
lldpXdot3RemLinkAggStatus = _LldpXdot3RemLinkAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 3, 1, 2),
    _LldpXdot3RemLinkAggPortId_Type()
)
lldpXdot3RemLinkAggPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemLinkAggPortId.setStatus("current")
_LldpXdot3RemMaxFrameSizeTable_Object = MibTable
lldpXdot3RemMaxFrameSizeTable = _LldpXdot3RemMaxFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeTable.setStatus("current")
_LldpXdot3RemMaxFrameSizeEntry_Object = MibTableRow
lldpXdot3RemMaxFrameSizeEntry = _LldpXdot3RemMaxFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 4, 1)
)
lldpXdot3RemMaxFrameSizeEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot3RemMaxFrameSize"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSizeEntry.setStatus("current")


class _LldpXdot3RemMaxFrameSize_Type(Integer32):
    """Custom type lldpXdot3RemMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpXdot3RemMaxFrameSize_Type.__name__ = "Integer32"
_LldpXdot3RemMaxFrameSize_Object = MibTableColumn
lldpXdot3RemMaxFrameSize = _LldpXdot3RemMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 12, 3, 4, 1, 1),
    _LldpXdot3RemMaxFrameSize_Type()
)
lldpXdot3RemMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot3RemMaxFrameSize.setStatus("current")
_LldpXdot1Objects_ObjectIdentity = ObjectIdentity
lldpXdot1Objects = _LldpXdot1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13)
)
_LldpXdot1Config_ObjectIdentity = ObjectIdentity
lldpXdot1Config = _LldpXdot1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1)
)
_LldpXdot1ConfigPortVlanTable_Object = MibTable
lldpXdot1ConfigPortVlanTable = _LldpXdot1ConfigPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTable.setStatus("current")
_LldpXdot1ConfigPortVlanEntry_Object = MibTableRow
lldpXdot1ConfigPortVlanEntry = _LldpXdot1ConfigPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanEntry.setStatus("current")


class _LldpXdot1ConfigPortVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigPortVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigPortVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigPortVlanTxEnable = _LldpXdot1ConfigPortVlanTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 1, 1, 1),
    _LldpXdot1ConfigPortVlanTxEnable_Type()
)
lldpXdot1ConfigPortVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigPortVlanTxEnable.setStatus("current")
_LldpXdot1ConfigVlanNameTable_Object = MibTable
lldpXdot1ConfigVlanNameTable = _LldpXdot1ConfigVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTable.setStatus("current")
_LldpXdot1ConfigVlanNameEntry_Object = MibTableRow
lldpXdot1ConfigVlanNameEntry = _LldpXdot1ConfigVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameEntry.setStatus("current")


class _LldpXdot1ConfigVlanNameTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigVlanNameTxEnable based on TruthValue"""


_LldpXdot1ConfigVlanNameTxEnable_Object = MibTableColumn
lldpXdot1ConfigVlanNameTxEnable = _LldpXdot1ConfigVlanNameTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 2, 1, 1),
    _LldpXdot1ConfigVlanNameTxEnable_Type()
)
lldpXdot1ConfigVlanNameTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigVlanNameTxEnable.setStatus("current")
_LldpXdot1ConfigProtoVlanTable_Object = MibTable
lldpXdot1ConfigProtoVlanTable = _LldpXdot1ConfigProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTable.setStatus("current")
_LldpXdot1ConfigProtoVlanEntry_Object = MibTableRow
lldpXdot1ConfigProtoVlanEntry = _LldpXdot1ConfigProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanEntry.setStatus("current")


class _LldpXdot1ConfigProtoVlanTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtoVlanTxEnable based on TruthValue"""


_LldpXdot1ConfigProtoVlanTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtoVlanTxEnable = _LldpXdot1ConfigProtoVlanTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 3, 1, 1),
    _LldpXdot1ConfigProtoVlanTxEnable_Type()
)
lldpXdot1ConfigProtoVlanTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtoVlanTxEnable.setStatus("current")
_LldpXdot1ConfigProtocolTable_Object = MibTable
lldpXdot1ConfigProtocolTable = _LldpXdot1ConfigProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTable.setStatus("current")
_LldpXdot1ConfigProtocolEntry_Object = MibTableRow
lldpXdot1ConfigProtocolEntry = _LldpXdot1ConfigProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolEntry.setStatus("current")


class _LldpXdot1ConfigProtocolTxEnable_Type(TruthValue):
    """Custom type lldpXdot1ConfigProtocolTxEnable based on TruthValue"""


_LldpXdot1ConfigProtocolTxEnable_Object = MibTableColumn
lldpXdot1ConfigProtocolTxEnable = _LldpXdot1ConfigProtocolTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 1, 4, 1, 1),
    _LldpXdot1ConfigProtocolTxEnable_Type()
)
lldpXdot1ConfigProtocolTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1ConfigProtocolTxEnable.setStatus("current")
_LldpXdot1LocalData_ObjectIdentity = ObjectIdentity
lldpXdot1LocalData = _LldpXdot1LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2)
)
_LldpXdot1LocTable_Object = MibTable
lldpXdot1LocTable = _LldpXdot1LocTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1LocTable.setStatus("current")
_LldpXdot1LocEntry_Object = MibTableRow
lldpXdot1LocEntry = _LldpXdot1LocEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 1, 1)
)
lldpXdot1LocEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1LocPortVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocEntry.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 1, 1, 1),
    _LldpXdot1LocPortVlanId_Type()
)
lldpXdot1LocPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocPortVlanId.setStatus("current")
_LldpXdot1LocProtoVlanTable_Object = MibTable
lldpXdot1LocProtoVlanTable = _LldpXdot1LocProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanTable.setStatus("current")
_LldpXdot1LocProtoVlanEntry_Object = MibTableRow
lldpXdot1LocProtoVlanEntry = _LldpXdot1LocProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 2, 1)
)
lldpXdot1LocProtoVlanEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1LocProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanEntry.setStatus("current")


class _LldpXdot1LocProtoVlanId_Type(Integer32):
    """Custom type lldpXdot1LocProtoVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_LldpXdot1LocProtoVlanId_Type.__name__ = "Integer32"
_LldpXdot1LocProtoVlanId_Object = MibTableColumn
lldpXdot1LocProtoVlanId = _LldpXdot1LocProtoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 2, 1, 1),
    _LldpXdot1LocProtoVlanId_Type()
)
lldpXdot1LocProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanId.setStatus("current")
_LldpXdot1LocProtoVlanSupported_Type = TruthValue
_LldpXdot1LocProtoVlanSupported_Object = MibTableColumn
lldpXdot1LocProtoVlanSupported = _LldpXdot1LocProtoVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 2, 1, 2),
    _LldpXdot1LocProtoVlanSupported_Type()
)
lldpXdot1LocProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanSupported.setStatus("current")
_LldpXdot1LocProtoVlanEnabled_Type = TruthValue
_LldpXdot1LocProtoVlanEnabled_Object = MibTableColumn
lldpXdot1LocProtoVlanEnabled = _LldpXdot1LocProtoVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 2, 1, 3),
    _LldpXdot1LocProtoVlanEnabled_Type()
)
lldpXdot1LocProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtoVlanEnabled.setStatus("current")
_LldpXdot1LocVlanNameTable_Object = MibTable
lldpXdot1LocVlanNameTable = _LldpXdot1LocVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameTable.setStatus("current")
_LldpXdot1LocVlanNameEntry_Object = MibTableRow
lldpXdot1LocVlanNameEntry = _LldpXdot1LocVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 3, 1)
)
lldpXdot1LocVlanNameEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1LocVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocVlanNameEntry.setStatus("current")
_LldpXdot1LocVlanId_Type = VlanId
_LldpXdot1LocVlanId_Object = MibTableColumn
lldpXdot1LocVlanId = _LldpXdot1LocVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 3, 1, 1),
    _LldpXdot1LocVlanId_Type()
)
lldpXdot1LocVlanId.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 3, 1, 2),
    _LldpXdot1LocVlanName_Type()
)
lldpXdot1LocVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocVlanName.setStatus("current")
_LldpXdot1LocProtocolTable_Object = MibTable
lldpXdot1LocProtocolTable = _LldpXdot1LocProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolTable.setStatus("current")
_LldpXdot1LocProtocolEntry_Object = MibTableRow
lldpXdot1LocProtocolEntry = _LldpXdot1LocProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 4, 1)
)
lldpXdot1LocProtocolEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1LocProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolEntry.setStatus("current")


class _LldpXdot1LocProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1LocProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1LocProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1LocProtocolIndex_Object = MibTableColumn
lldpXdot1LocProtocolIndex = _LldpXdot1LocProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 4, 1, 1),
    _LldpXdot1LocProtocolIndex_Type()
)
lldpXdot1LocProtocolIndex.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 2, 4, 1, 2),
    _LldpXdot1LocProtocolId_Type()
)
lldpXdot1LocProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1LocProtocolId.setStatus("current")
_LldpXdot1RemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1RemoteData = _LldpXdot1RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3)
)
_LldpXdot1RemTable_Object = MibTable
lldpXdot1RemTable = _LldpXdot1RemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1RemTable.setStatus("current")
_LldpXdot1RemEntry_Object = MibTableRow
lldpXdot1RemEntry = _LldpXdot1RemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 1, 1)
)
lldpXdot1RemEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1RemPortVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemEntry.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 1, 1, 1),
    _LldpXdot1RemPortVlanId_Type()
)
lldpXdot1RemPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemPortVlanId.setStatus("current")
_LldpXdot1RemProtoVlanTable_Object = MibTable
lldpXdot1RemProtoVlanTable = _LldpXdot1RemProtoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanTable.setStatus("current")
_LldpXdot1RemProtoVlanEntry_Object = MibTableRow
lldpXdot1RemProtoVlanEntry = _LldpXdot1RemProtoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 2, 1)
)
lldpXdot1RemProtoVlanEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1RemProtoVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEntry.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 2, 1, 1),
    _LldpXdot1RemProtoVlanId_Type()
)
lldpXdot1RemProtoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanId.setStatus("current")
_LldpXdot1RemProtoVlanSupported_Type = TruthValue
_LldpXdot1RemProtoVlanSupported_Object = MibTableColumn
lldpXdot1RemProtoVlanSupported = _LldpXdot1RemProtoVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 2, 1, 2),
    _LldpXdot1RemProtoVlanSupported_Type()
)
lldpXdot1RemProtoVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanSupported.setStatus("current")
_LldpXdot1RemProtoVlanEnabled_Type = TruthValue
_LldpXdot1RemProtoVlanEnabled_Object = MibTableColumn
lldpXdot1RemProtoVlanEnabled = _LldpXdot1RemProtoVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 2, 1, 3),
    _LldpXdot1RemProtoVlanEnabled_Type()
)
lldpXdot1RemProtoVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtoVlanEnabled.setStatus("current")
_LldpXdot1RemVlanNameTable_Object = MibTable
lldpXdot1RemVlanNameTable = _LldpXdot1RemVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameTable.setStatus("current")
_LldpXdot1RemVlanNameEntry_Object = MibTableRow
lldpXdot1RemVlanNameEntry = _LldpXdot1RemVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 3, 1)
)
lldpXdot1RemVlanNameEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1RemVlanId"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemVlanNameEntry.setStatus("current")
_LldpXdot1RemVlanId_Type = VlanId
_LldpXdot1RemVlanId_Object = MibTableColumn
lldpXdot1RemVlanId = _LldpXdot1RemVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 3, 1, 1),
    _LldpXdot1RemVlanId_Type()
)
lldpXdot1RemVlanId.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 3, 1, 2),
    _LldpXdot1RemVlanName_Type()
)
lldpXdot1RemVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemVlanName.setStatus("current")
_LldpXdot1RemProtocolTable_Object = MibTable
lldpXdot1RemProtocolTable = _LldpXdot1RemProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolTable.setStatus("current")
_LldpXdot1RemProtocolEntry_Object = MibTableRow
lldpXdot1RemProtocolEntry = _LldpXdot1RemProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 4, 1)
)
lldpXdot1RemProtocolEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "lldpXdot1RemProtocolIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolEntry.setStatus("current")


class _LldpXdot1RemProtocolIndex_Type(Integer32):
    """Custom type lldpXdot1RemProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpXdot1RemProtocolIndex_Type.__name__ = "Integer32"
_LldpXdot1RemProtocolIndex_Object = MibTableColumn
lldpXdot1RemProtocolIndex = _LldpXdot1RemProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 4, 1, 1),
    _LldpXdot1RemProtocolIndex_Type()
)
lldpXdot1RemProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolIndex.setStatus("current")


class _LldpXdot1RemProtocolId_Type(OctetString):
    """Custom type lldpXdot1RemProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LldpXdot1RemProtocolId_Type.__name__ = "OctetString"
_LldpXdot1RemProtocolId_Object = MibTableColumn
lldpXdot1RemProtocolId = _LldpXdot1RemProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 32, 13, 3, 4, 1, 2),
    _LldpXdot1RemProtocolId_Type()
)
lldpXdot1RemProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1RemProtocolId.setStatus("current")
_CompanyCPUInterfaceFilterGroup_ObjectIdentity = ObjectIdentity
companyCPUInterfaceFilterGroup = _CompanyCPUInterfaceFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33)
)
_CpuFilterProfile_ObjectIdentity = ObjectIdentity
cpuFilterProfile = _CpuFilterProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1)
)
_Ipv4cpuFilterProfileTable_Object = MibTable
ipv4cpuFilterProfileTable = _Ipv4cpuFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1)
)
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileTable.setStatus("current")
_Ipv4cpuFilterProfileEntry_Object = MibTableRow
ipv4cpuFilterProfileEntry = _Ipv4cpuFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1)
)
ipv4cpuFilterProfileEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "ipv4cpuFilterProfileNo"),
)
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileEntry.setStatus("current")


class _Ipv4cpuFilterProfileNo_Type(Integer32):
    """Custom type ipv4cpuFilterProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ipv4cpuFilterProfileNo_Type.__name__ = "Integer32"
_Ipv4cpuFilterProfileNo_Object = MibTableColumn
ipv4cpuFilterProfileNo = _Ipv4cpuFilterProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 1),
    _Ipv4cpuFilterProfileNo_Type()
)
ipv4cpuFilterProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileNo.setStatus("current")


class _Ipv4cpuFilterProfileType_Type(Integer32):
    """Custom type ipv4cpuFilterProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              11)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2),
          ("l3v6", 11))
    )


_Ipv4cpuFilterProfileType_Type.__name__ = "Integer32"
_Ipv4cpuFilterProfileType_Object = MibTableColumn
ipv4cpuFilterProfileType = _Ipv4cpuFilterProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 2),
    _Ipv4cpuFilterProfileType_Type()
)
ipv4cpuFilterProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileType.setStatus("current")


class _Ipv4cpuFilterProfileRuleCount_Type(Integer32):
    """Custom type ipv4cpuFilterProfileRuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv4cpuFilterProfileRuleCount_Type.__name__ = "Integer32"
_Ipv4cpuFilterProfileRuleCount_Object = MibTableColumn
ipv4cpuFilterProfileRuleCount = _Ipv4cpuFilterProfileRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 3),
    _Ipv4cpuFilterProfileRuleCount_Type()
)
ipv4cpuFilterProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileRuleCount.setStatus("current")
_Ipv4cpuFilterProfileMask_Type = OctetString
_Ipv4cpuFilterProfileMask_Object = MibTableColumn
ipv4cpuFilterProfileMask = _Ipv4cpuFilterProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 4),
    _Ipv4cpuFilterProfileMask_Type()
)
ipv4cpuFilterProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileMask.setStatus("current")
_Ipv4cpuFilterProfileDstMacAddrMask_Type = MacAddress
_Ipv4cpuFilterProfileDstMacAddrMask_Object = MibTableColumn
ipv4cpuFilterProfileDstMacAddrMask = _Ipv4cpuFilterProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 5),
    _Ipv4cpuFilterProfileDstMacAddrMask_Type()
)
ipv4cpuFilterProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileDstMacAddrMask.setStatus("current")
_Ipv4cpuFilterProfileSrcMacAddrMask_Type = MacAddress
_Ipv4cpuFilterProfileSrcMacAddrMask_Object = MibTableColumn
ipv4cpuFilterProfileSrcMacAddrMask = _Ipv4cpuFilterProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 6),
    _Ipv4cpuFilterProfileSrcMacAddrMask_Type()
)
ipv4cpuFilterProfileSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileSrcMacAddrMask.setStatus("current")


class _Ipv4cpuFilterProfileIPProtocol_Type(Integer32):
    """Custom type ipv4cpuFilterProfileIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("ipMask", 255),
          ("none", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_Ipv4cpuFilterProfileIPProtocol_Type.__name__ = "Integer32"
_Ipv4cpuFilterProfileIPProtocol_Object = MibTableColumn
ipv4cpuFilterProfileIPProtocol = _Ipv4cpuFilterProfileIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 7),
    _Ipv4cpuFilterProfileIPProtocol_Type()
)
ipv4cpuFilterProfileIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileIPProtocol.setStatus("current")


class _Ipv4cpuFilterProfileIPProtocolMask_Type(OctetString):
    """Custom type ipv4cpuFilterProfileIPProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_Ipv4cpuFilterProfileIPProtocolMask_Object = MibTableColumn
ipv4cpuFilterProfileIPProtocolMask = _Ipv4cpuFilterProfileIPProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 8),
    _Ipv4cpuFilterProfileIPProtocolMask_Type()
)
ipv4cpuFilterProfileIPProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileIPProtocolMask.setStatus("current")


class _Ipv4cpuFilterProfileDstIpAddrMask_Type(IpAddress):
    """Custom type ipv4cpuFilterProfileDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Ipv4cpuFilterProfileDstIpAddrMask_Object = MibTableColumn
ipv4cpuFilterProfileDstIpAddrMask = _Ipv4cpuFilterProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 9),
    _Ipv4cpuFilterProfileDstIpAddrMask_Type()
)
ipv4cpuFilterProfileDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileDstIpAddrMask.setStatus("current")


class _Ipv4cpuFilterProfileSrcIpAddrMask_Type(IpAddress):
    """Custom type ipv4cpuFilterProfileSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_Ipv4cpuFilterProfileSrcIpAddrMask_Object = MibTableColumn
ipv4cpuFilterProfileSrcIpAddrMask = _Ipv4cpuFilterProfileSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 10),
    _Ipv4cpuFilterProfileSrcIpAddrMask_Type()
)
ipv4cpuFilterProfileSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileSrcIpAddrMask.setStatus("current")


class _Ipv4cpuFilterProfileDstPortMask_Type(OctetString):
    """Custom type ipv4cpuFilterProfileDstPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_Ipv4cpuFilterProfileDstPortMask_Object = MibTableColumn
ipv4cpuFilterProfileDstPortMask = _Ipv4cpuFilterProfileDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 11),
    _Ipv4cpuFilterProfileDstPortMask_Type()
)
ipv4cpuFilterProfileDstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileDstPortMask.setStatus("current")


class _Ipv4cpuFilterProfileSrcPortMask_Type(OctetString):
    """Custom type ipv4cpuFilterProfileSrcPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_Ipv4cpuFilterProfileSrcPortMask_Object = MibTableColumn
ipv4cpuFilterProfileSrcPortMask = _Ipv4cpuFilterProfileSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 12),
    _Ipv4cpuFilterProfileSrcPortMask_Type()
)
ipv4cpuFilterProfileSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileSrcPortMask.setStatus("current")
_Ipv4cpuFilterProfileStatus_Type = RowStatus
_Ipv4cpuFilterProfileStatus_Object = MibTableColumn
ipv4cpuFilterProfileStatus = _Ipv4cpuFilterProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 1, 1, 15),
    _Ipv4cpuFilterProfileStatus_Type()
)
ipv4cpuFilterProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv4cpuFilterProfileStatus.setStatus("current")
_CpuFilterProfileTable_Object = MibTable
cpuFilterProfileTable = _CpuFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2)
)
if mibBuilder.loadTexts:
    cpuFilterProfileTable.setStatus("current")
_CpuFilterProfileEntry_Object = MibTableRow
cpuFilterProfileEntry = _CpuFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1)
)
cpuFilterProfileEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "cpuFilterProfileNo"),
)
if mibBuilder.loadTexts:
    cpuFilterProfileEntry.setStatus("current")


class _CpuFilterProfileNo_Type(Integer32):
    """Custom type cpuFilterProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuFilterProfileNo_Type.__name__ = "Integer32"
_CpuFilterProfileNo_Object = MibTableColumn
cpuFilterProfileNo = _CpuFilterProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 1),
    _CpuFilterProfileNo_Type()
)
cpuFilterProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterProfileNo.setStatus("current")


class _CpuFilterProfileType_Type(Integer32):
    """Custom type cpuFilterProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              11)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2),
          ("l3v6", 11))
    )


_CpuFilterProfileType_Type.__name__ = "Integer32"
_CpuFilterProfileType_Object = MibTableColumn
cpuFilterProfileType = _CpuFilterProfileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 2),
    _CpuFilterProfileType_Type()
)
cpuFilterProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileType.setStatus("current")


class _CpuFilterProfileRuleCount_Type(Integer32):
    """Custom type cpuFilterProfileRuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpuFilterProfileRuleCount_Type.__name__ = "Integer32"
_CpuFilterProfileRuleCount_Object = MibTableColumn
cpuFilterProfileRuleCount = _CpuFilterProfileRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 3),
    _CpuFilterProfileRuleCount_Type()
)
cpuFilterProfileRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterProfileRuleCount.setStatus("current")
_CpuFilterProfileMask_Type = OctetString
_CpuFilterProfileMask_Object = MibTableColumn
cpuFilterProfileMask = _CpuFilterProfileMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 4),
    _CpuFilterProfileMask_Type()
)
cpuFilterProfileMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileMask.setStatus("current")
_CpuFilterProfileDstMacAddrMask_Type = MacAddress
_CpuFilterProfileDstMacAddrMask_Object = MibTableColumn
cpuFilterProfileDstMacAddrMask = _CpuFilterProfileDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 5),
    _CpuFilterProfileDstMacAddrMask_Type()
)
cpuFilterProfileDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileDstMacAddrMask.setStatus("current")
_CpuFilterProfileSrcMacAddrMask_Type = MacAddress
_CpuFilterProfileSrcMacAddrMask_Object = MibTableColumn
cpuFilterProfileSrcMacAddrMask = _CpuFilterProfileSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 6),
    _CpuFilterProfileSrcMacAddrMask_Type()
)
cpuFilterProfileSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileSrcMacAddrMask.setStatus("current")


class _CpuFilterProfileIPProtocol_Type(Integer32):
    """Custom type cpuFilterProfileIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("ipMask", 255),
          ("none", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_CpuFilterProfileIPProtocol_Type.__name__ = "Integer32"
_CpuFilterProfileIPProtocol_Object = MibTableColumn
cpuFilterProfileIPProtocol = _CpuFilterProfileIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 7),
    _CpuFilterProfileIPProtocol_Type()
)
cpuFilterProfileIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileIPProtocol.setStatus("current")


class _CpuFilterProfileIPProtocolMask_Type(OctetString):
    """Custom type cpuFilterProfileIPProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_CpuFilterProfileIPProtocolMask_Object = MibTableColumn
cpuFilterProfileIPProtocolMask = _CpuFilterProfileIPProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 8),
    _CpuFilterProfileIPProtocolMask_Type()
)
cpuFilterProfileIPProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileIPProtocolMask.setStatus("current")


class _CpuFilterProfileDstIpAddrMaskType_Type(Integer32):
    """Custom type cpuFilterProfileDstIpAddrMaskType based on Integer32"""
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


_CpuFilterProfileDstIpAddrMaskType_Type.__name__ = "Integer32"
_CpuFilterProfileDstIpAddrMaskType_Object = MibTableColumn
cpuFilterProfileDstIpAddrMaskType = _CpuFilterProfileDstIpAddrMaskType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 9),
    _CpuFilterProfileDstIpAddrMaskType_Type()
)
cpuFilterProfileDstIpAddrMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileDstIpAddrMaskType.setStatus("current")


class _CpuFilterProfileDstIpAddrMask_Type(Ipv6Address):
    """Custom type cpuFilterProfileDstIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterProfileDstIpAddrMask_Object = MibTableColumn
cpuFilterProfileDstIpAddrMask = _CpuFilterProfileDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 10),
    _CpuFilterProfileDstIpAddrMask_Type()
)
cpuFilterProfileDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileDstIpAddrMask.setStatus("current")


class _CpuFilterProfileSrcIpAddrMaskType_Type(Integer32):
    """Custom type cpuFilterProfileSrcIpAddrMaskType based on Integer32"""
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


_CpuFilterProfileSrcIpAddrMaskType_Type.__name__ = "Integer32"
_CpuFilterProfileSrcIpAddrMaskType_Object = MibTableColumn
cpuFilterProfileSrcIpAddrMaskType = _CpuFilterProfileSrcIpAddrMaskType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 11),
    _CpuFilterProfileSrcIpAddrMaskType_Type()
)
cpuFilterProfileSrcIpAddrMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileSrcIpAddrMaskType.setStatus("current")


class _CpuFilterProfileSrcIpAddrMask_Type(Ipv6Address):
    """Custom type cpuFilterProfileSrcIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterProfileSrcIpAddrMask_Object = MibTableColumn
cpuFilterProfileSrcIpAddrMask = _CpuFilterProfileSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 12),
    _CpuFilterProfileSrcIpAddrMask_Type()
)
cpuFilterProfileSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileSrcIpAddrMask.setStatus("current")


class _CpuFilterProfileDstPortMask_Type(OctetString):
    """Custom type cpuFilterProfileDstPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_CpuFilterProfileDstPortMask_Object = MibTableColumn
cpuFilterProfileDstPortMask = _CpuFilterProfileDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 13),
    _CpuFilterProfileDstPortMask_Type()
)
cpuFilterProfileDstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileDstPortMask.setStatus("current")


class _CpuFilterProfileSrcPortMask_Type(OctetString):
    """Custom type cpuFilterProfileSrcPortMask based on OctetString"""
    defaultHexValue = "FFFF"


_CpuFilterProfileSrcPortMask_Object = MibTableColumn
cpuFilterProfileSrcPortMask = _CpuFilterProfileSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 14),
    _CpuFilterProfileSrcPortMask_Type()
)
cpuFilterProfileSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterProfileSrcPortMask.setStatus("current")
_CpuFilterProfileStatus_Type = RowStatus
_CpuFilterProfileStatus_Object = MibTableColumn
cpuFilterProfileStatus = _CpuFilterProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 1, 2, 1, 15),
    _CpuFilterProfileStatus_Type()
)
cpuFilterProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterProfileStatus.setStatus("current")
_CpuFilterL2Rule_ObjectIdentity = ObjectIdentity
cpuFilterL2Rule = _CpuFilterL2Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2)
)
_CpuFilterL2RuleTable_Object = MibTable
cpuFilterL2RuleTable = _CpuFilterL2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1)
)
if mibBuilder.loadTexts:
    cpuFilterL2RuleTable.setStatus("current")
_CpuFilterL2RuleEntry_Object = MibTableRow
cpuFilterL2RuleEntry = _CpuFilterL2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1)
)
cpuFilterL2RuleEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "cpuFilterL2ProfileID"),
    (0, "DGS-1100-06ME-AX", "cpuFilterL2AccessID"),
)
if mibBuilder.loadTexts:
    cpuFilterL2RuleEntry.setStatus("current")


class _CpuFilterL2ProfileID_Type(Integer32):
    """Custom type cpuFilterL2ProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuFilterL2ProfileID_Type.__name__ = "Integer32"
_CpuFilterL2ProfileID_Object = MibTableColumn
cpuFilterL2ProfileID = _CpuFilterL2ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 1),
    _CpuFilterL2ProfileID_Type()
)
cpuFilterL2ProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL2ProfileID.setStatus("current")


class _CpuFilterL2AccessID_Type(Integer32):
    """Custom type cpuFilterL2AccessID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CpuFilterL2AccessID_Type.__name__ = "Integer32"
_CpuFilterL2AccessID_Object = MibTableColumn
cpuFilterL2AccessID = _CpuFilterL2AccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 2),
    _CpuFilterL2AccessID_Type()
)
cpuFilterL2AccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL2AccessID.setStatus("current")


class _CpuFilterL2RuleEtherType_Type(Integer32):
    """Custom type cpuFilterL2RuleEtherType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1501, 65535),
    )


_CpuFilterL2RuleEtherType_Type.__name__ = "Integer32"
_CpuFilterL2RuleEtherType_Object = MibTableColumn
cpuFilterL2RuleEtherType = _CpuFilterL2RuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 3),
    _CpuFilterL2RuleEtherType_Type()
)
cpuFilterL2RuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleEtherType.setStatus("current")
_CpuFilterL2RuleDstMacAddr_Type = MacAddress
_CpuFilterL2RuleDstMacAddr_Object = MibTableColumn
cpuFilterL2RuleDstMacAddr = _CpuFilterL2RuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 4),
    _CpuFilterL2RuleDstMacAddr_Type()
)
cpuFilterL2RuleDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleDstMacAddr.setStatus("current")
_CpuFilterL2RuleSrcMacAddr_Type = MacAddress
_CpuFilterL2RuleSrcMacAddr_Object = MibTableColumn
cpuFilterL2RuleSrcMacAddr = _CpuFilterL2RuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 5),
    _CpuFilterL2RuleSrcMacAddr_Type()
)
cpuFilterL2RuleSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleSrcMacAddr.setStatus("current")


class _CpuFilterL2RuleVlanId_Type(Integer32):
    """Custom type cpuFilterL2RuleVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_CpuFilterL2RuleVlanId_Type.__name__ = "Integer32"
_CpuFilterL2RuleVlanId_Object = MibTableColumn
cpuFilterL2RuleVlanId = _CpuFilterL2RuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 6),
    _CpuFilterL2RuleVlanId_Type()
)
cpuFilterL2RuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleVlanId.setStatus("current")


class _CpuFilterL2Rule1pPriority_Type(Integer32):
    """Custom type cpuFilterL2Rule1pPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_CpuFilterL2Rule1pPriority_Type.__name__ = "Integer32"
_CpuFilterL2Rule1pPriority_Object = MibTableColumn
cpuFilterL2Rule1pPriority = _CpuFilterL2Rule1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 7),
    _CpuFilterL2Rule1pPriority_Type()
)
cpuFilterL2Rule1pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2Rule1pPriority.setStatus("current")
_CpuFilterL2RuleDstMacAddrMask_Type = MacAddress
_CpuFilterL2RuleDstMacAddrMask_Object = MibTableColumn
cpuFilterL2RuleDstMacAddrMask = _CpuFilterL2RuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 8),
    _CpuFilterL2RuleDstMacAddrMask_Type()
)
cpuFilterL2RuleDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL2RuleDstMacAddrMask.setStatus("current")
_CpuFilterL2RuleSrcMacAddrMask_Type = MacAddress
_CpuFilterL2RuleSrcMacAddrMask_Object = MibTableColumn
cpuFilterL2RuleSrcMacAddrMask = _CpuFilterL2RuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 9),
    _CpuFilterL2RuleSrcMacAddrMask_Type()
)
cpuFilterL2RuleSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL2RuleSrcMacAddrMask.setStatus("current")
_CpuFilterL2RuleInPortList_Type = PortList
_CpuFilterL2RuleInPortList_Object = MibTableColumn
cpuFilterL2RuleInPortList = _CpuFilterL2RuleInPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 10),
    _CpuFilterL2RuleInPortList_Type()
)
cpuFilterL2RuleInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleInPortList.setStatus("current")


class _CpuFilterL2RuleAction_Type(Integer32):
    """Custom type cpuFilterL2RuleAction based on Integer32"""
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


_CpuFilterL2RuleAction_Type.__name__ = "Integer32"
_CpuFilterL2RuleAction_Object = MibTableColumn
cpuFilterL2RuleAction = _CpuFilterL2RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 11),
    _CpuFilterL2RuleAction_Type()
)
cpuFilterL2RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL2RuleAction.setStatus("current")
_CpuFilterL2RuleStatus_Type = RowStatus
_CpuFilterL2RuleStatus_Object = MibTableColumn
cpuFilterL2RuleStatus = _CpuFilterL2RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 2, 1, 1, 14),
    _CpuFilterL2RuleStatus_Type()
)
cpuFilterL2RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL2RuleStatus.setStatus("current")
_CpuFilterL3Rule_ObjectIdentity = ObjectIdentity
cpuFilterL3Rule = _CpuFilterL3Rule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3)
)
_CpuFilterL3RuleTable_Object = MibTable
cpuFilterL3RuleTable = _CpuFilterL3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1)
)
if mibBuilder.loadTexts:
    cpuFilterL3RuleTable.setStatus("current")
_CpuFilterL3RuleEntry_Object = MibTableRow
cpuFilterL3RuleEntry = _CpuFilterL3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1)
)
cpuFilterL3RuleEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "cpuFilterL3RuleProfileNo"),
    (0, "DGS-1100-06ME-AX", "cpuFilterL3RuleAccessID"),
)
if mibBuilder.loadTexts:
    cpuFilterL3RuleEntry.setStatus("current")


class _CpuFilterL3RuleProfileNo_Type(Integer32):
    """Custom type cpuFilterL3RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CpuFilterL3RuleProfileNo_Type.__name__ = "Integer32"
_CpuFilterL3RuleProfileNo_Object = MibTableColumn
cpuFilterL3RuleProfileNo = _CpuFilterL3RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 1),
    _CpuFilterL3RuleProfileNo_Type()
)
cpuFilterL3RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleProfileNo.setStatus("current")


class _CpuFilterL3RuleAccessID_Type(Integer32):
    """Custom type cpuFilterL3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuFilterL3RuleAccessID_Type.__name__ = "Integer32"
_CpuFilterL3RuleAccessID_Object = MibTableColumn
cpuFilterL3RuleAccessID = _CpuFilterL3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 2),
    _CpuFilterL3RuleAccessID_Type()
)
cpuFilterL3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleAccessID.setStatus("current")


class _CpuFilterL3RuleProtocol_Type(Integer32):
    """Custom type cpuFilterL3RuleProtocol based on Integer32"""
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


_CpuFilterL3RuleProtocol_Type.__name__ = "Integer32"
_CpuFilterL3RuleProtocol_Object = MibTableColumn
cpuFilterL3RuleProtocol = _CpuFilterL3RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 3),
    _CpuFilterL3RuleProtocol_Type()
)
cpuFilterL3RuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleProtocol.setStatus("current")


class _CpuFilterL3RuleProtocolMask_Type(OctetString):
    """Custom type cpuFilterL3RuleProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_CpuFilterL3RuleProtocolMask_Object = MibTableColumn
cpuFilterL3RuleProtocolMask = _CpuFilterL3RuleProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 4),
    _CpuFilterL3RuleProtocolMask_Type()
)
cpuFilterL3RuleProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleProtocolMask.setStatus("current")


class _CpuFilterL3RuleICMPMessageType_Type(Integer32):
    """Custom type cpuFilterL3RuleICMPMessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CpuFilterL3RuleICMPMessageType_Type.__name__ = "Integer32"
_CpuFilterL3RuleICMPMessageType_Object = MibTableColumn
cpuFilterL3RuleICMPMessageType = _CpuFilterL3RuleICMPMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 5),
    _CpuFilterL3RuleICMPMessageType_Type()
)
cpuFilterL3RuleICMPMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleICMPMessageType.setStatus("current")


class _CpuFilterL3RuleICMPMessageCode_Type(Integer32):
    """Custom type cpuFilterL3RuleICMPMessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CpuFilterL3RuleICMPMessageCode_Type.__name__ = "Integer32"
_CpuFilterL3RuleICMPMessageCode_Object = MibTableColumn
cpuFilterL3RuleICMPMessageCode = _CpuFilterL3RuleICMPMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 6),
    _CpuFilterL3RuleICMPMessageCode_Type()
)
cpuFilterL3RuleICMPMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleICMPMessageCode.setStatus("current")


class _CpuFilterL3RuleDstIpAddr_Type(IpAddress):
    """Custom type cpuFilterL3RuleDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CpuFilterL3RuleDstIpAddr_Object = MibTableColumn
cpuFilterL3RuleDstIpAddr = _CpuFilterL3RuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 7),
    _CpuFilterL3RuleDstIpAddr_Type()
)
cpuFilterL3RuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleDstIpAddr.setStatus("current")


class _CpuFilterL3RuleSrcIpAddr_Type(IpAddress):
    """Custom type cpuFilterL3RuleSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CpuFilterL3RuleSrcIpAddr_Object = MibTableColumn
cpuFilterL3RuleSrcIpAddr = _CpuFilterL3RuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 8),
    _CpuFilterL3RuleSrcIpAddr_Type()
)
cpuFilterL3RuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleSrcIpAddr.setStatus("current")


class _CpuFilterL3RuleDstIpAddrMask_Type(IpAddress):
    """Custom type cpuFilterL3RuleDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterL3RuleDstIpAddrMask_Object = MibTableColumn
cpuFilterL3RuleDstIpAddrMask = _CpuFilterL3RuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 9),
    _CpuFilterL3RuleDstIpAddrMask_Type()
)
cpuFilterL3RuleDstIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleDstIpAddrMask.setStatus("current")


class _CpuFilterL3RuleSrcIpAddrMask_Type(IpAddress):
    """Custom type cpuFilterL3RuleSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterL3RuleSrcIpAddrMask_Object = MibTableColumn
cpuFilterL3RuleSrcIpAddrMask = _CpuFilterL3RuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 10),
    _CpuFilterL3RuleSrcIpAddrMask_Type()
)
cpuFilterL3RuleSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleSrcIpAddrMask.setStatus("current")


class _CpuFilterL3RuleTcpUdpDstPort_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CpuFilterL3RuleTcpUdpDstPort_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpUdpDstPort_Object = MibTableColumn
cpuFilterL3RuleTcpUdpDstPort = _CpuFilterL3RuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 11),
    _CpuFilterL3RuleTcpUdpDstPort_Type()
)
cpuFilterL3RuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpUdpDstPort.setStatus("current")


class _CpuFilterL3RuleTcpUdpSrcPort_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CpuFilterL3RuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpUdpSrcPort_Object = MibTableColumn
cpuFilterL3RuleTcpUdpSrcPort = _CpuFilterL3RuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 12),
    _CpuFilterL3RuleTcpUdpSrcPort_Type()
)
cpuFilterL3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpUdpSrcPort.setStatus("current")
_CpuFilterL3RuleTcpUdpDstPortMask_Type = OctetString
_CpuFilterL3RuleTcpUdpDstPortMask_Object = MibTableColumn
cpuFilterL3RuleTcpUdpDstPortMask = _CpuFilterL3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 13),
    _CpuFilterL3RuleTcpUdpDstPortMask_Type()
)
cpuFilterL3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpUdpDstPortMask.setStatus("current")
_CpuFilterL3RuleTcpUdpSrcPortMask_Type = OctetString
_CpuFilterL3RuleTcpUdpSrcPortMask_Object = MibTableColumn
cpuFilterL3RuleTcpUdpSrcPortMask = _CpuFilterL3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 14),
    _CpuFilterL3RuleTcpUdpSrcPortMask_Type()
)
cpuFilterL3RuleTcpUdpSrcPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpUdpSrcPortMask.setStatus("current")


class _CpuFilterL3RuleTcpAckBit_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpAckBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterL3RuleTcpAckBit_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpAckBit_Object = MibTableColumn
cpuFilterL3RuleTcpAckBit = _CpuFilterL3RuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 15),
    _CpuFilterL3RuleTcpAckBit_Type()
)
cpuFilterL3RuleTcpAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpAckBit.setStatus("current")


class _CpuFilterL3RuleTcpRstBit_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpRstBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterL3RuleTcpRstBit_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpRstBit_Object = MibTableColumn
cpuFilterL3RuleTcpRstBit = _CpuFilterL3RuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 16),
    _CpuFilterL3RuleTcpRstBit_Type()
)
cpuFilterL3RuleTcpRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpRstBit.setStatus("current")


class _CpuFilterL3RuleTcpUrgBit_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpUrgBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterL3RuleTcpUrgBit_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpUrgBit_Object = MibTableColumn
cpuFilterL3RuleTcpUrgBit = _CpuFilterL3RuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 17),
    _CpuFilterL3RuleTcpUrgBit_Type()
)
cpuFilterL3RuleTcpUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpUrgBit.setStatus("current")


class _CpuFilterL3RuleTcpPshBit_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpPshBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterL3RuleTcpPshBit_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpPshBit_Object = MibTableColumn
cpuFilterL3RuleTcpPshBit = _CpuFilterL3RuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 18),
    _CpuFilterL3RuleTcpPshBit_Type()
)
cpuFilterL3RuleTcpPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpPshBit.setStatus("current")


class _CpuFilterL3RuleTcpSynBit_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpSynBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterL3RuleTcpSynBit_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpSynBit_Object = MibTableColumn
cpuFilterL3RuleTcpSynBit = _CpuFilterL3RuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 19),
    _CpuFilterL3RuleTcpSynBit_Type()
)
cpuFilterL3RuleTcpSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpSynBit.setStatus("current")


class _CpuFilterL3RuleTcpFinBit_Type(Integer32):
    """Custom type cpuFilterL3RuleTcpFinBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterL3RuleTcpFinBit_Type.__name__ = "Integer32"
_CpuFilterL3RuleTcpFinBit_Object = MibTableColumn
cpuFilterL3RuleTcpFinBit = _CpuFilterL3RuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 20),
    _CpuFilterL3RuleTcpFinBit_Type()
)
cpuFilterL3RuleTcpFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleTcpFinBit.setStatus("current")


class _CpuFilterL3RuleDscp_Type(Integer32):
    """Custom type cpuFilterL3RuleDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_CpuFilterL3RuleDscp_Type.__name__ = "Integer32"
_CpuFilterL3RuleDscp_Object = MibTableColumn
cpuFilterL3RuleDscp = _CpuFilterL3RuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 21),
    _CpuFilterL3RuleDscp_Type()
)
cpuFilterL3RuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleDscp.setStatus("current")


class _CpuFilterL3RuleIgmpType_Type(Integer32):
    """Custom type cpuFilterL3RuleIgmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CpuFilterL3RuleIgmpType_Type.__name__ = "Integer32"
_CpuFilterL3RuleIgmpType_Object = MibTableColumn
cpuFilterL3RuleIgmpType = _CpuFilterL3RuleIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 22),
    _CpuFilterL3RuleIgmpType_Type()
)
cpuFilterL3RuleIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleIgmpType.setStatus("current")
_CpuFilterL3RulePortList_Type = PortList
_CpuFilterL3RulePortList_Object = MibTableColumn
cpuFilterL3RulePortList = _CpuFilterL3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 23),
    _CpuFilterL3RulePortList_Type()
)
cpuFilterL3RulePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RulePortList.setStatus("current")


class _CpuFilterL3RuleAction_Type(Integer32):
    """Custom type cpuFilterL3RuleAction based on Integer32"""
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


_CpuFilterL3RuleAction_Type.__name__ = "Integer32"
_CpuFilterL3RuleAction_Object = MibTableColumn
cpuFilterL3RuleAction = _CpuFilterL3RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 24),
    _CpuFilterL3RuleAction_Type()
)
cpuFilterL3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterL3RuleAction.setStatus("current")
_CpuFilterL3RuleStatus_Type = RowStatus
_CpuFilterL3RuleStatus_Object = MibTableColumn
cpuFilterL3RuleStatus = _CpuFilterL3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 1, 1, 27),
    _CpuFilterL3RuleStatus_Type()
)
cpuFilterL3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterL3RuleStatus.setStatus("current")
_CpuFilterv6L3RuleTable_Object = MibTable
cpuFilterv6L3RuleTable = _CpuFilterv6L3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2)
)
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTable.setStatus("current")
_CpuFilterv6L3RuleEntry_Object = MibTableRow
cpuFilterv6L3RuleEntry = _CpuFilterv6L3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1)
)
cpuFilterv6L3RuleEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "cpuFilterv6L3RuleProfileNo"),
    (0, "DGS-1100-06ME-AX", "cpuFilterv6L3RuleAccessID"),
)
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleEntry.setStatus("current")


class _CpuFilterv6L3RuleProfileNo_Type(Integer32):
    """Custom type cpuFilterv6L3RuleProfileNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CpuFilterv6L3RuleProfileNo_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleProfileNo_Object = MibTableColumn
cpuFilterv6L3RuleProfileNo = _CpuFilterv6L3RuleProfileNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 1),
    _CpuFilterv6L3RuleProfileNo_Type()
)
cpuFilterv6L3RuleProfileNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleProfileNo.setStatus("current")


class _CpuFilterv6L3RuleAccessID_Type(Integer32):
    """Custom type cpuFilterv6L3RuleAccessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CpuFilterv6L3RuleAccessID_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleAccessID_Object = MibTableColumn
cpuFilterv6L3RuleAccessID = _CpuFilterv6L3RuleAccessID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 2),
    _CpuFilterv6L3RuleAccessID_Type()
)
cpuFilterv6L3RuleAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleAccessID.setStatus("current")


class _CpuFilterv6L3RuleProtocol_Type(Integer32):
    """Custom type cpuFilterv6L3RuleProtocol based on Integer32"""
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


_CpuFilterv6L3RuleProtocol_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleProtocol_Object = MibTableColumn
cpuFilterv6L3RuleProtocol = _CpuFilterv6L3RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 3),
    _CpuFilterv6L3RuleProtocol_Type()
)
cpuFilterv6L3RuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleProtocol.setStatus("current")


class _CpuFilterv6L3RuleProtocolMask_Type(OctetString):
    """Custom type cpuFilterv6L3RuleProtocolMask based on OctetString"""
    defaultHexValue = "FF"


_CpuFilterv6L3RuleProtocolMask_Object = MibTableColumn
cpuFilterv6L3RuleProtocolMask = _CpuFilterv6L3RuleProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 4),
    _CpuFilterv6L3RuleProtocolMask_Type()
)
cpuFilterv6L3RuleProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleProtocolMask.setStatus("current")


class _CpuFilterv6L3RuleICMPMessageType_Type(Integer32):
    """Custom type cpuFilterv6L3RuleICMPMessageType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CpuFilterv6L3RuleICMPMessageType_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleICMPMessageType_Object = MibTableColumn
cpuFilterv6L3RuleICMPMessageType = _CpuFilterv6L3RuleICMPMessageType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 5),
    _CpuFilterv6L3RuleICMPMessageType_Type()
)
cpuFilterv6L3RuleICMPMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleICMPMessageType.setStatus("current")


class _CpuFilterv6L3RuleICMPMessageCode_Type(Integer32):
    """Custom type cpuFilterv6L3RuleICMPMessageCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CpuFilterv6L3RuleICMPMessageCode_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleICMPMessageCode_Object = MibTableColumn
cpuFilterv6L3RuleICMPMessageCode = _CpuFilterv6L3RuleICMPMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 6),
    _CpuFilterv6L3RuleICMPMessageCode_Type()
)
cpuFilterv6L3RuleICMPMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleICMPMessageCode.setStatus("current")


class _CpuFilterv6L3RuleDstIpAddr_Type(Ipv6Address):
    """Custom type cpuFilterv6L3RuleDstIpAddr based on Ipv6Address"""
    defaultHexValue = "00000000"


_CpuFilterv6L3RuleDstIpAddr_Object = MibTableColumn
cpuFilterv6L3RuleDstIpAddr = _CpuFilterv6L3RuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 7),
    _CpuFilterv6L3RuleDstIpAddr_Type()
)
cpuFilterv6L3RuleDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleDstIpAddr.setStatus("current")


class _CpuFilterv6L3RuleSrcIpAddr_Type(Ipv6Address):
    """Custom type cpuFilterv6L3RuleSrcIpAddr based on Ipv6Address"""
    defaultHexValue = "00000000"


_CpuFilterv6L3RuleSrcIpAddr_Object = MibTableColumn
cpuFilterv6L3RuleSrcIpAddr = _CpuFilterv6L3RuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 8),
    _CpuFilterv6L3RuleSrcIpAddr_Type()
)
cpuFilterv6L3RuleSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleSrcIpAddr.setStatus("current")


class _CpuFilterv6L3RuleDstIpAddrMask_Type(Ipv6Address):
    """Custom type cpuFilterv6L3RuleDstIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterv6L3RuleDstIpAddrMask_Object = MibTableColumn
cpuFilterv6L3RuleDstIpAddrMask = _CpuFilterv6L3RuleDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 9),
    _CpuFilterv6L3RuleDstIpAddrMask_Type()
)
cpuFilterv6L3RuleDstIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleDstIpAddrMask.setStatus("current")


class _CpuFilterv6L3RuleSrcIpAddrMask_Type(Ipv6Address):
    """Custom type cpuFilterv6L3RuleSrcIpAddrMask based on Ipv6Address"""
    defaultHexValue = "FFFFFFFF"


_CpuFilterv6L3RuleSrcIpAddrMask_Object = MibTableColumn
cpuFilterv6L3RuleSrcIpAddrMask = _CpuFilterv6L3RuleSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 10),
    _CpuFilterv6L3RuleSrcIpAddrMask_Type()
)
cpuFilterv6L3RuleSrcIpAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleSrcIpAddrMask.setStatus("current")


class _CpuFilterv6L3RuleTcpUdpDstPort_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CpuFilterv6L3RuleTcpUdpDstPort_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpUdpDstPort_Object = MibTableColumn
cpuFilterv6L3RuleTcpUdpDstPort = _CpuFilterv6L3RuleTcpUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 11),
    _CpuFilterv6L3RuleTcpUdpDstPort_Type()
)
cpuFilterv6L3RuleTcpUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpUdpDstPort.setStatus("current")


class _CpuFilterv6L3RuleTcpUdpSrcPort_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CpuFilterv6L3RuleTcpUdpSrcPort_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpUdpSrcPort_Object = MibTableColumn
cpuFilterv6L3RuleTcpUdpSrcPort = _CpuFilterv6L3RuleTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 12),
    _CpuFilterv6L3RuleTcpUdpSrcPort_Type()
)
cpuFilterv6L3RuleTcpUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpUdpSrcPort.setStatus("current")
_CpuFilterv6L3RuleTcpUdpDstPortMask_Type = OctetString
_CpuFilterv6L3RuleTcpUdpDstPortMask_Object = MibTableColumn
cpuFilterv6L3RuleTcpUdpDstPortMask = _CpuFilterv6L3RuleTcpUdpDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 13),
    _CpuFilterv6L3RuleTcpUdpDstPortMask_Type()
)
cpuFilterv6L3RuleTcpUdpDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpUdpDstPortMask.setStatus("current")
_CpuFilterv6L3RuleTcpUdpSrcPortMask_Type = OctetString
_CpuFilterv6L3RuleTcpUdpSrcPortMask_Object = MibTableColumn
cpuFilterv6L3RuleTcpUdpSrcPortMask = _CpuFilterv6L3RuleTcpUdpSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 14),
    _CpuFilterv6L3RuleTcpUdpSrcPortMask_Type()
)
cpuFilterv6L3RuleTcpUdpSrcPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpUdpSrcPortMask.setStatus("current")


class _CpuFilterv6L3RuleTcpAckBit_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpAckBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterv6L3RuleTcpAckBit_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpAckBit_Object = MibTableColumn
cpuFilterv6L3RuleTcpAckBit = _CpuFilterv6L3RuleTcpAckBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 15),
    _CpuFilterv6L3RuleTcpAckBit_Type()
)
cpuFilterv6L3RuleTcpAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpAckBit.setStatus("current")


class _CpuFilterv6L3RuleTcpRstBit_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpRstBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterv6L3RuleTcpRstBit_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpRstBit_Object = MibTableColumn
cpuFilterv6L3RuleTcpRstBit = _CpuFilterv6L3RuleTcpRstBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 16),
    _CpuFilterv6L3RuleTcpRstBit_Type()
)
cpuFilterv6L3RuleTcpRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpRstBit.setStatus("current")


class _CpuFilterv6L3RuleTcpUrgBit_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpUrgBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterv6L3RuleTcpUrgBit_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpUrgBit_Object = MibTableColumn
cpuFilterv6L3RuleTcpUrgBit = _CpuFilterv6L3RuleTcpUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 17),
    _CpuFilterv6L3RuleTcpUrgBit_Type()
)
cpuFilterv6L3RuleTcpUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpUrgBit.setStatus("current")


class _CpuFilterv6L3RuleTcpPshBit_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpPshBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterv6L3RuleTcpPshBit_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpPshBit_Object = MibTableColumn
cpuFilterv6L3RuleTcpPshBit = _CpuFilterv6L3RuleTcpPshBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 18),
    _CpuFilterv6L3RuleTcpPshBit_Type()
)
cpuFilterv6L3RuleTcpPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpPshBit.setStatus("current")


class _CpuFilterv6L3RuleTcpSynBit_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpSynBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterv6L3RuleTcpSynBit_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpSynBit_Object = MibTableColumn
cpuFilterv6L3RuleTcpSynBit = _CpuFilterv6L3RuleTcpSynBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 19),
    _CpuFilterv6L3RuleTcpSynBit_Type()
)
cpuFilterv6L3RuleTcpSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpSynBit.setStatus("current")


class _CpuFilterv6L3RuleTcpFinBit_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTcpFinBit based on Integer32"""
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
        *(("dontcare", -1),
          ("establish", 1),
          ("notEstablish", 2))
    )


_CpuFilterv6L3RuleTcpFinBit_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTcpFinBit_Object = MibTableColumn
cpuFilterv6L3RuleTcpFinBit = _CpuFilterv6L3RuleTcpFinBit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 20),
    _CpuFilterv6L3RuleTcpFinBit_Type()
)
cpuFilterv6L3RuleTcpFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTcpFinBit.setStatus("current")


class _CpuFilterv6L3RuleTrafficClass_Type(Integer32):
    """Custom type cpuFilterv6L3RuleTrafficClass based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_CpuFilterv6L3RuleTrafficClass_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleTrafficClass_Object = MibTableColumn
cpuFilterv6L3RuleTrafficClass = _CpuFilterv6L3RuleTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 21),
    _CpuFilterv6L3RuleTrafficClass_Type()
)
cpuFilterv6L3RuleTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleTrafficClass.setStatus("current")
_CpuFilterv6L3RulePortList_Type = PortList
_CpuFilterv6L3RulePortList_Object = MibTableColumn
cpuFilterv6L3RulePortList = _CpuFilterv6L3RulePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 22),
    _CpuFilterv6L3RulePortList_Type()
)
cpuFilterv6L3RulePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RulePortList.setStatus("current")


class _CpuFilterv6L3RuleAction_Type(Integer32):
    """Custom type cpuFilterv6L3RuleAction based on Integer32"""
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


_CpuFilterv6L3RuleAction_Type.__name__ = "Integer32"
_CpuFilterv6L3RuleAction_Object = MibTableColumn
cpuFilterv6L3RuleAction = _CpuFilterv6L3RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 23),
    _CpuFilterv6L3RuleAction_Type()
)
cpuFilterv6L3RuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleAction.setStatus("current")
_CpuFilterv6L3RuleStatus_Type = RowStatus
_CpuFilterv6L3RuleStatus_Object = MibTableColumn
cpuFilterv6L3RuleStatus = _CpuFilterv6L3RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 33, 3, 2, 1, 24),
    _CpuFilterv6L3RuleStatus_Type()
)
cpuFilterv6L3RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpuFilterv6L3RuleStatus.setStatus("current")
_CompanyCableDiagnostic_ObjectIdentity = ObjectIdentity
companyCableDiagnostic = _CompanyCableDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35)
)
_CableDiagTriggerIndex_Type = Integer32
_CableDiagTriggerIndex_Object = MibScalar
cableDiagTriggerIndex = _CableDiagTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 2),
    _CableDiagPair1TestResult_Type()
)
cableDiagPair1TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1TestResult.setStatus("current")
_CableDiagPair1FaultDistance_Type = Integer32
_CableDiagPair1FaultDistance_Object = MibScalar
cableDiagPair1FaultDistance = _CableDiagPair1FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 4),
    _CableDiagPair2TestResult_Type()
)
cableDiagPair2TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2TestResult.setStatus("current")
_CableDiagPair2FaultDistance_Type = Integer32
_CableDiagPair2FaultDistance_Object = MibScalar
cableDiagPair2FaultDistance = _CableDiagPair2FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 6),
    _CableDiagPair3TestResult_Type()
)
cableDiagPair3TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3TestResult.setStatus("current")
_CableDiagPair3FaultDistance_Type = Integer32
_CableDiagPair3FaultDistance_Object = MibScalar
cableDiagPair3FaultDistance = _CableDiagPair3FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 8),
    _CableDiagPair4TestResult_Type()
)
cableDiagPair4TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4TestResult.setStatus("current")
_CableDiagPair4FaultDistance_Type = Integer32
_CableDiagPair4FaultDistance_Object = MibScalar
cableDiagPair4FaultDistance = _CableDiagPair4FaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 35, 10),
    _CableDiagLengthinRange_Type()
)
cableDiagLengthinRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagLengthinRange.setStatus("current")
_CompanyQinQ_ObjectIdentity = ObjectIdentity
companyQinQ = _CompanyQinQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37)
)
_QinqSystem_ObjectIdentity = ObjectIdentity
qinqSystem = _QinqSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37, 1)
)


class _QinqGlobalStatus_Type(Integer32):
    """Custom type qinqGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QinqGlobalStatus_Type.__name__ = "Integer32"
_QinqGlobalStatus_Object = MibScalar
qinqGlobalStatus = _QinqGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37, 1, 1),
    _QinqGlobalStatus_Type()
)
qinqGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqGlobalStatus.setStatus("current")
_QinqTable_Object = MibTable
qinqTable = _QinqTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37, 1, 2)
)
if mibBuilder.loadTexts:
    qinqTable.setStatus("current")
_QinqEntry_Object = MibTableRow
qinqEntry = _QinqEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37, 1, 2, 1)
)
qinqEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "qinqIfIndex"),
)
if mibBuilder.loadTexts:
    qinqEntry.setStatus("current")
_QinqIfIndex_Type = InterfaceIndex
_QinqIfIndex_Object = MibTableColumn
qinqIfIndex = _QinqIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37, 1, 2, 1, 1),
    _QinqIfIndex_Type()
)
qinqIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qinqIfIndex.setStatus("current")


class _QinqRoleState_Type(Integer32):
    """Custom type qinqRoleState based on Integer32"""
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


_QinqRoleState_Type.__name__ = "Integer32"
_QinqRoleState_Object = MibTableColumn
qinqRoleState = _QinqRoleState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37, 1, 2, 1, 2),
    _QinqRoleState_Type()
)
qinqRoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqRoleState.setStatus("current")
_QinqOuterTPID_Type = Unsigned32
_QinqOuterTPID_Object = MibTableColumn
qinqOuterTPID = _QinqOuterTPID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 37, 1, 2, 1, 3),
    _QinqOuterTPID_Type()
)
qinqOuterTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqOuterTPID.setStatus("current")
_CompanyTimeRangeMgmt_ObjectIdentity = ObjectIdentity
companyTimeRangeMgmt = _CompanyTimeRangeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38)
)
_SwTimeRangeSettingTable_Object = MibTable
swTimeRangeSettingTable = _SwTimeRangeSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1)
)
if mibBuilder.loadTexts:
    swTimeRangeSettingTable.setStatus("current")
_SwTimeRangeSettingEntry_Object = MibTableRow
swTimeRangeSettingEntry = _SwTimeRangeSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1)
)
swTimeRangeSettingEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "swTimeRangeIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 3),
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


_SwTimeRangeStartYear_Type.__name__ = "Integer32"
_SwTimeRangeStartYear_Object = MibTableColumn
swTimeRangeStartYear = _SwTimeRangeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 8),
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


_SwTimeRangeEndYear_Type.__name__ = "Integer32"
_SwTimeRangeEndYear_Object = MibTableColumn
swTimeRangeEndYear = _SwTimeRangeEndYear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 20),
    _SwTimeRangeSunday_Type()
)
swTimeRangeSunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTimeRangeSunday.setStatus("current")
_SwTimeRangeRowStatus_Type = RowStatus
_SwTimeRangeRowStatus_Object = MibTableColumn
swTimeRangeRowStatus = _SwTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 38, 1, 1, 21),
    _SwTimeRangeRowStatus_Type()
)
swTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swTimeRangeRowStatus.setStatus("current")
_CompanyLimitIp_ObjectIdentity = ObjectIdentity
companyLimitIp = _CompanyLimitIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45)
)
_LimitIpMulticastProfileTable_Object = MibTable
limitIpMulticastProfileTable = _LimitIpMulticastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 1)
)
if mibBuilder.loadTexts:
    limitIpMulticastProfileTable.setStatus("current")
_LimitIpMulticastProfileEntry_Object = MibTableRow
limitIpMulticastProfileEntry = _LimitIpMulticastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 1, 1)
)
limitIpMulticastProfileEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "limitIpMulticastIPType"),
    (0, "DGS-1100-06ME-AX", "limitIpMulticastProfileID"),
)
if mibBuilder.loadTexts:
    limitIpMulticastProfileEntry.setStatus("current")


class _LimitIpMulticastIPType_Type(Integer32):
    """Custom type limitIpMulticastIPType based on Integer32"""
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


_LimitIpMulticastIPType_Type.__name__ = "Integer32"
_LimitIpMulticastIPType_Object = MibTableColumn
limitIpMulticastIPType = _LimitIpMulticastIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 1, 1, 1),
    _LimitIpMulticastIPType_Type()
)
limitIpMulticastIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastIPType.setStatus("current")


class _LimitIpMulticastProfileID_Type(Integer32):
    """Custom type limitIpMulticastProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_LimitIpMulticastProfileID_Type.__name__ = "Integer32"
_LimitIpMulticastProfileID_Object = MibTableColumn
limitIpMulticastProfileID = _LimitIpMulticastProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 1, 1, 2),
    _LimitIpMulticastProfileID_Type()
)
limitIpMulticastProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastProfileID.setStatus("current")


class _LimitIpMulticastProfileName_Type(DisplayString):
    """Custom type limitIpMulticastProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_LimitIpMulticastProfileName_Type.__name__ = "DisplayString"
_LimitIpMulticastProfileName_Object = MibTableColumn
limitIpMulticastProfileName = _LimitIpMulticastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 1, 1, 3),
    _LimitIpMulticastProfileName_Type()
)
limitIpMulticastProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastProfileName.setStatus("current")
_LimitIpMulticastProfileStatus_Type = RowStatus
_LimitIpMulticastProfileStatus_Object = MibTableColumn
limitIpMulticastProfileStatus = _LimitIpMulticastProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 1, 1, 4),
    _LimitIpMulticastProfileStatus_Type()
)
limitIpMulticastProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastProfileStatus.setStatus("current")
_LimitIpMulticastEntryTable_Object = MibTable
limitIpMulticastEntryTable = _LimitIpMulticastEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 2)
)
if mibBuilder.loadTexts:
    limitIpMulticastEntryTable.setStatus("current")
_LimitIpMulticastEntry_Object = MibTableRow
limitIpMulticastEntry = _LimitIpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 2, 1)
)
limitIpMulticastEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "limitIpMulticastEntryIPType"),
    (0, "DGS-1100-06ME-AX", "limitIpMulticastEntryProfileID"),
    (0, "DGS-1100-06ME-AX", "limitIpMulticaststartIpAddr"),
    (0, "DGS-1100-06ME-AX", "limitIpMulticastendIpAddr"),
)
if mibBuilder.loadTexts:
    limitIpMulticastEntry.setStatus("current")


class _LimitIpMulticastEntryIPType_Type(Integer32):
    """Custom type limitIpMulticastEntryIPType based on Integer32"""
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


_LimitIpMulticastEntryIPType_Type.__name__ = "Integer32"
_LimitIpMulticastEntryIPType_Object = MibTableColumn
limitIpMulticastEntryIPType = _LimitIpMulticastEntryIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 2, 1, 1),
    _LimitIpMulticastEntryIPType_Type()
)
limitIpMulticastEntryIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastEntryIPType.setStatus("current")


class _LimitIpMulticastEntryProfileID_Type(Integer32):
    """Custom type limitIpMulticastEntryProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_LimitIpMulticastEntryProfileID_Type.__name__ = "Integer32"
_LimitIpMulticastEntryProfileID_Object = MibTableColumn
limitIpMulticastEntryProfileID = _LimitIpMulticastEntryProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 2, 1, 2),
    _LimitIpMulticastEntryProfileID_Type()
)
limitIpMulticastEntryProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastEntryProfileID.setStatus("current")


class _LimitIpMulticaststartIpAddr_Type(DisplayString):
    """Custom type limitIpMulticaststartIpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LimitIpMulticaststartIpAddr_Type.__name__ = "DisplayString"
_LimitIpMulticaststartIpAddr_Object = MibTableColumn
limitIpMulticaststartIpAddr = _LimitIpMulticaststartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 2, 1, 3),
    _LimitIpMulticaststartIpAddr_Type()
)
limitIpMulticaststartIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticaststartIpAddr.setStatus("current")


class _LimitIpMulticastendIpAddr_Type(DisplayString):
    """Custom type limitIpMulticastendIpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LimitIpMulticastendIpAddr_Type.__name__ = "DisplayString"
_LimitIpMulticastendIpAddr_Object = MibTableColumn
limitIpMulticastendIpAddr = _LimitIpMulticastendIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 2, 1, 4),
    _LimitIpMulticastendIpAddr_Type()
)
limitIpMulticastendIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastendIpAddr.setStatus("current")
_LimitIpMulticastStatus_Type = RowStatus
_LimitIpMulticastStatus_Object = MibTableColumn
limitIpMulticastStatus = _LimitIpMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 2, 1, 5),
    _LimitIpMulticastStatus_Type()
)
limitIpMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastStatus.setStatus("current")
_LimitIpMulticastPortTable_Object = MibTable
limitIpMulticastPortTable = _LimitIpMulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 3)
)
if mibBuilder.loadTexts:
    limitIpMulticastPortTable.setStatus("current")
_LimitIpMulticastPortEntry_Object = MibTableRow
limitIpMulticastPortEntry = _LimitIpMulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 3, 1)
)
limitIpMulticastPortEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "limitIpMulticastPortIPType"),
    (0, "DGS-1100-06ME-AX", "limitIpMulticastPortID"),
)
if mibBuilder.loadTexts:
    limitIpMulticastPortEntry.setStatus("current")


class _LimitIpMulticastPortIPType_Type(Integer32):
    """Custom type limitIpMulticastPortIPType based on Integer32"""
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


_LimitIpMulticastPortIPType_Type.__name__ = "Integer32"
_LimitIpMulticastPortIPType_Object = MibTableColumn
limitIpMulticastPortIPType = _LimitIpMulticastPortIPType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 3, 1, 1),
    _LimitIpMulticastPortIPType_Type()
)
limitIpMulticastPortIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastPortIPType.setStatus("current")


class _LimitIpMulticastPortID_Type(Integer32):
    """Custom type limitIpMulticastPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_LimitIpMulticastPortID_Type.__name__ = "Integer32"
_LimitIpMulticastPortID_Object = MibTableColumn
limitIpMulticastPortID = _LimitIpMulticastPortID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 3, 1, 2),
    _LimitIpMulticastPortID_Type()
)
limitIpMulticastPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitIpMulticastPortID.setStatus("current")


class _LimitIpMulticastPortState_Type(Integer32):
    """Custom type limitIpMulticastPortState based on Integer32"""
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


_LimitIpMulticastPortState_Type.__name__ = "Integer32"
_LimitIpMulticastPortState_Object = MibTableColumn
limitIpMulticastPortState = _LimitIpMulticastPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 3, 1, 3),
    _LimitIpMulticastPortState_Type()
)
limitIpMulticastPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastPortState.setStatus("current")
_LimitIpMulticastPortProfileID_Type = PortList
_LimitIpMulticastPortProfileID_Object = MibTableColumn
limitIpMulticastPortProfileID = _LimitIpMulticastPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 3, 1, 4),
    _LimitIpMulticastPortProfileID_Type()
)
limitIpMulticastPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastPortProfileID.setStatus("current")


class _LimitIpMulticastPortMaxGrp_Type(Integer32):
    """Custom type limitIpMulticastPortMaxGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LimitIpMulticastPortMaxGrp_Type.__name__ = "Integer32"
_LimitIpMulticastPortMaxGrp_Object = MibTableColumn
limitIpMulticastPortMaxGrp = _LimitIpMulticastPortMaxGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 45, 3, 1, 5),
    _LimitIpMulticastPortMaxGrp_Type()
)
limitIpMulticastPortMaxGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitIpMulticastPortMaxGrp.setStatus("current")
_CompanyMulticastFilter_ObjectIdentity = ObjectIdentity
companyMulticastFilter = _CompanyMulticastFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 49)
)
_McastFilterPortTable_Object = MibTable
mcastFilterPortTable = _McastFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 49, 1)
)
if mibBuilder.loadTexts:
    mcastFilterPortTable.setStatus("current")
_McastFilterPortEntry_Object = MibTableRow
mcastFilterPortEntry = _McastFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 49, 1, 1)
)
mcastFilterPortEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "mcastFilterPortIndex"),
)
if mibBuilder.loadTexts:
    mcastFilterPortEntry.setStatus("current")


class _McastFilterPortIndex_Type(Integer32):
    """Custom type mcastFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_McastFilterPortIndex_Type.__name__ = "Integer32"
_McastFilterPortIndex_Object = MibTableColumn
mcastFilterPortIndex = _McastFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 49, 1, 1, 1),
    _McastFilterPortIndex_Type()
)
mcastFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcastFilterPortIndex.setStatus("current")


class _McastFilterPortType_Type(Integer32):
    """Custom type mcastFilterPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("forward", 1))
    )


_McastFilterPortType_Type.__name__ = "Integer32"
_McastFilterPortType_Object = MibTableColumn
mcastFilterPortType = _McastFilterPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 49, 1, 1, 2),
    _McastFilterPortType_Type()
)
mcastFilterPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastFilterPortType.setStatus("current")
_CompanyNeighbor_ObjectIdentity = ObjectIdentity
companyNeighbor = _CompanyNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50)
)
_NeighborTable_Object = MibTable
neighborTable = _NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1)
)
if mibBuilder.loadTexts:
    neighborTable.setStatus("current")
_NeighborEntry_Object = MibTableRow
neighborEntry = _NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1)
)
neighborEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "neighborIfindex"),
    (0, "DGS-1100-06ME-AX", "neighborIPv6Addr"),
    (0, "DGS-1100-06ME-AX", "neighborMACAddr"),
)
if mibBuilder.loadTexts:
    neighborEntry.setStatus("current")


class _NeighborIfindex_Type(Integer32):
    """Custom type neighborIfindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NeighborIfindex_Type.__name__ = "Integer32"
_NeighborIfindex_Object = MibTableColumn
neighborIfindex = _NeighborIfindex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1, 1),
    _NeighborIfindex_Type()
)
neighborIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIfindex.setStatus("current")
_NeighborIPv6Addr_Type = Ipv6Address
_NeighborIPv6Addr_Object = MibTableColumn
neighborIPv6Addr = _NeighborIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1, 2),
    _NeighborIPv6Addr_Type()
)
neighborIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIPv6Addr.setStatus("current")
_NeighborMACAddr_Type = MacAddress
_NeighborMACAddr_Object = MibTableColumn
neighborMACAddr = _NeighborMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1, 5),
    _NeighborCacheState_Type()
)
neighborCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborCacheState.setStatus("current")


class _NeighborActiveStatus_Type(Integer32):
    """Custom type neighborActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_NeighborActiveStatus_Type.__name__ = "Integer32"
_NeighborActiveStatus_Object = MibTableColumn
neighborActiveStatus = _NeighborActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1, 6),
    _NeighborActiveStatus_Type()
)
neighborActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborActiveStatus.setStatus("current")
_NeighborRowStatus_Type = RowStatus
_NeighborRowStatus_Object = MibTableColumn
neighborRowStatus = _NeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 50, 1, 1, 7),
    _NeighborRowStatus_Type()
)
neighborRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neighborRowStatus.setStatus("current")
_CompanyEoam_ObjectIdentity = ObjectIdentity
companyEoam = _CompanyEoam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51)
)
_EoamSystem_ObjectIdentity = ObjectIdentity
eoamSystem = _EoamSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1)
)
_EoamTable_Object = MibTable
eoamTable = _EoamTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2)
)
if mibBuilder.loadTexts:
    eoamTable.setStatus("current")
_EoamEntry_Object = MibTableRow
eoamEntry = _EoamEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1)
)
eoamEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "eoamIfIndex"),
)
if mibBuilder.loadTexts:
    eoamEntry.setStatus("current")
_EoamIfIndex_Type = InterfaceIndex
_EoamIfIndex_Object = MibTableColumn
eoamIfIndex = _EoamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1, 5),
    _EoamRemoteLoopback_Type()
)
eoamRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamRemoteLoopback.setStatus("current")


class _EoamDyingGaspEnable_Type(Integer32):
    """Custom type eoamDyingGaspEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EoamDyingGaspEnable_Type.__name__ = "Integer32"
_EoamDyingGaspEnable_Object = MibTableColumn
eoamDyingGaspEnable = _EoamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1, 6),
    _EoamDyingGaspEnable_Type()
)
eoamDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamDyingGaspEnable.setStatus("current")


class _EoamCriticalEventEnable_Type(Integer32):
    """Custom type eoamCriticalEventEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EoamCriticalEventEnable_Type.__name__ = "Integer32"
_EoamCriticalEventEnable_Object = MibTableColumn
eoamCriticalEventEnable = _EoamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 1, 2, 1, 7),
    _EoamCriticalEventEnable_Type()
)
eoamCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoamCriticalEventEnable.setStatus("current")
_EoamLinkMonitor_ObjectIdentity = ObjectIdentity
eoamLinkMonitor = _EoamLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2)
)
_EoamLinkMonitorTable_Object = MibTable
eoamLinkMonitorTable = _EoamLinkMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1)
)
if mibBuilder.loadTexts:
    eoamLinkMonitorTable.setStatus("current")
_EoamLinkMonitorEntry_Object = MibTableRow
eoamLinkMonitorEntry = _EoamLinkMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1)
)
eoamLinkMonitorEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "eoamLinkMonitorIfIndex"),
)
if mibBuilder.loadTexts:
    eoamLinkMonitorEntry.setStatus("current")
_EoamLinkMonitorIfIndex_Type = InterfaceIndex
_EoamLinkMonitorIfIndex_Object = MibTableColumn
eoamLinkMonitorIfIndex = _EoamLinkMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 2),
    _ErrorSymbolNotifyState_Type()
)
errorSymbolNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorSymbolNotifyState.setStatus("current")
_ErrorSymbolThreshold_Type = Unsigned32
_ErrorSymbolThreshold_Object = MibTableColumn
errorSymbolThreshold = _ErrorSymbolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 3),
    _ErrorSymbolThreshold_Type()
)
errorSymbolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorSymbolThreshold.setStatus("current")
_ErrorSymbolWindow_Type = Unsigned32
_ErrorSymbolWindow_Object = MibTableColumn
errorSymbolWindow = _ErrorSymbolWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 5),
    _ErrorFrameNotifyState_Type()
)
errorFrameNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameNotifyState.setStatus("current")
_ErrorFrameThreshold_Type = Unsigned32
_ErrorFrameThreshold_Object = MibTableColumn
errorFrameThreshold = _ErrorFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 6),
    _ErrorFrameThreshold_Type()
)
errorFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameThreshold.setStatus("current")
_ErrorFrameWindow_Type = Unsigned32
_ErrorFrameWindow_Object = MibTableColumn
errorFrameWindow = _ErrorFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 8),
    _ErrorFrameSecondsNotifyState_Type()
)
errorFrameSecondsNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameSecondsNotifyState.setStatus("current")
_ErrorFrameSecondsThreshold_Type = Unsigned32
_ErrorFrameSecondsThreshold_Object = MibTableColumn
errorFrameSecondsThreshold = _ErrorFrameSecondsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 9),
    _ErrorFrameSecondsThreshold_Type()
)
errorFrameSecondsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFrameSecondsThreshold.setStatus("current")
_ErrorFrameSecondsWindow_Type = Unsigned32
_ErrorFrameSecondsWindow_Object = MibTableColumn
errorFrameSecondsWindow = _ErrorFrameSecondsWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 11),
    _ErrorFramePeriodNotifyState_Type()
)
errorFramePeriodNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFramePeriodNotifyState.setStatus("current")
_ErrorFramePeriodThreshold_Type = Unsigned32
_ErrorFramePeriodThreshold_Object = MibTableColumn
errorFramePeriodThreshold = _ErrorFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 12),
    _ErrorFramePeriodThreshold_Type()
)
errorFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFramePeriodThreshold.setStatus("current")
_ErrorFramePeriodWindow_Type = Unsigned32
_ErrorFramePeriodWindow_Object = MibTableColumn
errorFramePeriodWindow = _ErrorFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 51, 2, 1, 1, 13),
    _ErrorFramePeriodWindow_Type()
)
errorFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorFramePeriodWindow.setStatus("current")
_CompanyDuld_ObjectIdentity = ObjectIdentity
companyDuld = _CompanyDuld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52)
)
_DuldSystem_ObjectIdentity = ObjectIdentity
duldSystem = _DuldSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1)
)
_DuldTable_Object = MibTable
duldTable = _DuldTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1)
)
if mibBuilder.loadTexts:
    duldTable.setStatus("current")
_DuldEntry_Object = MibTableRow
duldEntry = _DuldEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1, 1)
)
duldEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "duldIfIndex"),
)
if mibBuilder.loadTexts:
    duldEntry.setStatus("current")
_DuldIfIndex_Type = InterfaceIndex
_DuldIfIndex_Object = MibTableColumn
duldIfIndex = _DuldIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1, 1, 1),
    _DuldIfIndex_Type()
)
duldIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duldIfIndex.setStatus("current")


class _DuldState_Type(Integer32):
    """Custom type duldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1, 1, 3),
    _DuldOperState_Type()
)
duldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duldOperState.setStatus("current")


class _DuldMode_Type(Integer32):
    """Custom type duldMode based on Integer32"""
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1, 1, 4),
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
          ("unknow", 1))
    )


_DuldLinkStatus_Type.__name__ = "Integer32"
_DuldLinkStatus_Object = MibTableColumn
duldLinkStatus = _DuldLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 52, 1, 1, 1, 6),
    _DuldDiscoveryTime_Type()
)
duldDiscoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duldDiscoveryTime.setStatus("current")
_CompanyDHCPv6Relay_ObjectIdentity = ObjectIdentity
companyDHCPv6Relay = _CompanyDHCPv6Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86)
)
_Dhcpv6RelayControl_ObjectIdentity = ObjectIdentity
dhcpv6RelayControl = _Dhcpv6RelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 1, 1),
    _Dhcpv6RelayState_Type()
)
dhcpv6RelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayState.setStatus("current")


class _Dhcpv6RelayHopCount_Type(Integer32):
    """Custom type dhcpv6RelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dhcpv6RelayHopCount_Type.__name__ = "Integer32"
_Dhcpv6RelayHopCount_Object = MibScalar
dhcpv6RelayHopCount = _Dhcpv6RelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 1, 2),
    _Dhcpv6RelayHopCount_Type()
)
dhcpv6RelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayHopCount.setStatus("current")
_Dhcpv6RelayManagement_ObjectIdentity = ObjectIdentity
dhcpv6RelayManagement = _Dhcpv6RelayManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 2)
)
_Dhcpv6RelayInterfaceSettingsTable_Object = MibTable
dhcpv6RelayInterfaceSettingsTable = _Dhcpv6RelayInterfaceSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpv6RelayInterfaceSettingsTable.setStatus("current")
_Dhcpv6RelayInterfaceSettingsEntry_Object = MibTableRow
dhcpv6RelayInterfaceSettingsEntry = _Dhcpv6RelayInterfaceSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 2, 1, 1)
)
dhcpv6RelayInterfaceSettingsEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "dhcpv6RelayInterface"),
    (0, "DGS-1100-06ME-AX", "dhcpv6RelayServerIP"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 2, 1, 1, 1),
    _Dhcpv6RelayInterface_Type()
)
dhcpv6RelayInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6RelayInterface.setStatus("current")
_Dhcpv6RelayServerIP_Type = Ipv6Address
_Dhcpv6RelayServerIP_Object = MibTableColumn
dhcpv6RelayServerIP = _Dhcpv6RelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 2, 1, 1, 2),
    _Dhcpv6RelayServerIP_Type()
)
dhcpv6RelayServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6RelayServerIP.setStatus("current")
_Dhcpv6RelayInterfaceSettingsRowStatus_Type = RowStatus
_Dhcpv6RelayInterfaceSettingsRowStatus_Object = MibTableColumn
dhcpv6RelayInterfaceSettingsRowStatus = _Dhcpv6RelayInterfaceSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 2, 1, 1, 99),
    _Dhcpv6RelayInterfaceSettingsRowStatus_Type()
)
dhcpv6RelayInterfaceSettingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpv6RelayInterfaceSettingsRowStatus.setStatus("current")
_Dhcpv6RelayOption37_ObjectIdentity = ObjectIdentity
dhcpv6RelayOption37 = _Dhcpv6RelayOption37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 3, 2),
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
        *(("cid-with-user-define", 1),
          ("default", 0),
          ("user-define", 2))
    )


_Dhcpv6RelayOption37RemoteIDType_Type.__name__ = "Integer32"
_Dhcpv6RelayOption37RemoteIDType_Object = MibScalar
dhcpv6RelayOption37RemoteIDType = _Dhcpv6RelayOption37RemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 3, 3),
    _Dhcpv6RelayOption37RemoteIDType_Type()
)
dhcpv6RelayOption37RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37RemoteIDType.setStatus("current")
_Dhcpv6RelayOption37RemoteID_Type = DisplayString
_Dhcpv6RelayOption37RemoteID_Object = MibScalar
dhcpv6RelayOption37RemoteID = _Dhcpv6RelayOption37RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 86, 3, 4),
    _Dhcpv6RelayOption37RemoteID_Type()
)
dhcpv6RelayOption37RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpv6RelayOption37RemoteID.setStatus("current")
_CompanyMldsGroup_ObjectIdentity = ObjectIdentity
companyMldsGroup = _CompanyMldsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88)
)
_MldsSystem_ObjectIdentity = ObjectIdentity
mldsSystem = _MldsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 1, 7),
    _MldsQueryMaxResponseTime_Type()
)
mldsQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsQueryMaxResponseTime.setStatus("current")
_MldsVlan_ObjectIdentity = ObjectIdentity
mldsVlan = _MldsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3)
)
_MldsVlanRouterTable_Object = MibTable
mldsVlanRouterTable = _MldsVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 3)
)
if mibBuilder.loadTexts:
    mldsVlanRouterTable.setStatus("current")
_MldsVlanRouterEntry_Object = MibTableRow
mldsVlanRouterEntry = _MldsVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 3, 1)
)
mldsVlanRouterEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "mldsVlanRouterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 3, 1, 1),
    _MldsVlanRouterVlanId_Type()
)
mldsVlanRouterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanRouterVlanId.setStatus("current")
_MldsVlanRouterPortList_Type = PortList
_MldsVlanRouterPortList_Object = MibTableColumn
mldsVlanRouterPortList = _MldsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 3, 1, 2),
    _MldsVlanRouterPortList_Type()
)
mldsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanRouterPortList.setStatus("current")
_MldsVlanFilterTable_Object = MibTable
mldsVlanFilterTable = _MldsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4)
)
if mibBuilder.loadTexts:
    mldsVlanFilterTable.setStatus("current")
_MldsVlanFilterEntry_Object = MibTableRow
mldsVlanFilterEntry = _MldsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1)
)
mldsVlanFilterEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "mldsVlanFilterVlanId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1, 5),
    _MldsVlanQueryInterval_Type()
)
mldsVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanQueryInterval.setStatus("current")
_MldsVlanRtrPortList_Type = PortList
_MldsVlanRtrPortList_Object = MibTableColumn
mldsVlanRtrPortList = _MldsVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 4, 1, 8),
    _MldsVlanFastLeave_Type()
)
mldsVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldsVlanFastLeave.setStatus("current")
_MldsVlanMulticastGroupTable_Object = MibTable
mldsVlanMulticastGroupTable = _MldsVlanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 5)
)
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupTable.setStatus("current")
_MldsVlanMulticastGroupEntry_Object = MibTableRow
mldsVlanMulticastGroupEntry = _MldsVlanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 5, 1)
)
mldsVlanMulticastGroupEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "mldsVlanMulticastGroupVlanId"),
    (0, "DGS-1100-06ME-AX", "mldsVlanMulticastGroupIpAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 5, 1, 1),
    _MldsVlanMulticastGroupVlanId_Type()
)
mldsVlanMulticastGroupVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupVlanId.setStatus("current")
_MldsVlanMulticastGroupIpAddress_Type = InetAddress
_MldsVlanMulticastGroupIpAddress_Object = MibTableColumn
mldsVlanMulticastGroupIpAddress = _MldsVlanMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 5, 1, 2),
    _MldsVlanMulticastGroupIpAddress_Type()
)
mldsVlanMulticastGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupIpAddress.setStatus("current")
_MldsVlanMulticastGroupMacAddress_Type = MacAddress
_MldsVlanMulticastGroupMacAddress_Object = MibTableColumn
mldsVlanMulticastGroupMacAddress = _MldsVlanMulticastGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 5, 1, 3),
    _MldsVlanMulticastGroupMacAddress_Type()
)
mldsVlanMulticastGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupMacAddress.setStatus("current")
_MldsVlanMulticastGroupPortList_Type = PortList
_MldsVlanMulticastGroupPortList_Object = MibTableColumn
mldsVlanMulticastGroupPortList = _MldsVlanMulticastGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 3, 5, 1, 4),
    _MldsVlanMulticastGroupPortList_Type()
)
mldsVlanMulticastGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsVlanMulticastGroupPortList.setStatus("current")
_MldsHost_ObjectIdentity = ObjectIdentity
mldsHost = _MldsHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 4)
)
_MldsHostTable_Object = MibTable
mldsHostTable = _MldsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 4, 1)
)
if mibBuilder.loadTexts:
    mldsHostTable.setStatus("current")
_MldsHostEntry_Object = MibTableRow
mldsHostEntry = _MldsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 4, 1, 1)
)
mldsHostEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "mldsHostTableVLANID"),
    (0, "DGS-1100-06ME-AX", "mldsHostTableGroupAddress"),
    (0, "DGS-1100-06ME-AX", "mldsHostTablePort"),
    (0, "DGS-1100-06ME-AX", "mldsHostTableHostIPAddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 4, 1, 1, 1),
    _MldsHostTableVLANID_Type()
)
mldsHostTableVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTableVLANID.setStatus("current")
_MldsHostTableGroupAddress_Type = Ipv6Address
_MldsHostTableGroupAddress_Object = MibTableColumn
mldsHostTableGroupAddress = _MldsHostTableGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 4, 1, 1, 2),
    _MldsHostTableGroupAddress_Type()
)
mldsHostTableGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTableGroupAddress.setStatus("current")


class _MldsHostTablePort_Type(Integer32):
    """Custom type mldsHostTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MldsHostTablePort_Type.__name__ = "Integer32"
_MldsHostTablePort_Object = MibTableColumn
mldsHostTablePort = _MldsHostTablePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 4, 1, 1, 3),
    _MldsHostTablePort_Type()
)
mldsHostTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTablePort.setStatus("current")
_MldsHostTableHostIPAddress_Type = Ipv6Address
_MldsHostTableHostIPAddress_Object = MibTableColumn
mldsHostTableHostIPAddress = _MldsHostTableHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 88, 4, 1, 1, 4),
    _MldsHostTableHostIPAddress_Type()
)
mldsHostTableHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsHostTableHostIPAddress.setStatus("current")
_CompanyPPPoE_ObjectIdentity = ObjectIdentity
companyPPPoE = _CompanyPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98)
)


class _PppoeGlobalState_Type(Integer32):
    """Custom type pppoeGlobalState based on Integer32"""
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


_PppoeGlobalState_Type.__name__ = "Integer32"
_PppoeGlobalState_Object = MibScalar
pppoeGlobalState = _PppoeGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 1),
    _PppoeGlobalState_Type()
)
pppoeGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeGlobalState.setStatus("current")
_PppoePortTable_Object = MibTable
pppoePortTable = _PppoePortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2)
)
if mibBuilder.loadTexts:
    pppoePortTable.setStatus("current")
_PppoePortEntry_Object = MibTableRow
pppoePortEntry = _PppoePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1)
)
pppoePortEntry.setIndexNames(
    (0, "DGS-1100-06ME-AX", "pppoePortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1, 1),
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
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PppoePortState_Type.__name__ = "Integer32"
_PppoePortState_Object = MibTableColumn
pppoePortState = _PppoePortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1, 2),
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
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("mac", 1),
          ("udf", 2),
          ("vendor2", 3),
          ("vendor3", 4))
    )


_PppoePortCircuitIDType_Type.__name__ = "Integer32"
_PppoePortCircuitIDType_Object = MibTableColumn
pppoePortCircuitIDType = _PppoePortCircuitIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1, 4),
    _PppoePortUDFString_Type()
)
pppoePortUDFString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortUDFString.setStatus("current")


class _PppoePortCircuitIDVendor3String_Type(DisplayString):
    """Custom type pppoePortCircuitIDVendor3String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppoePortCircuitIDVendor3String_Type.__name__ = "DisplayString"
_PppoePortCircuitIDVendor3String_Object = MibTableColumn
pppoePortCircuitIDVendor3String = _PppoePortCircuitIDVendor3String_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1, 5),
    _PppoePortCircuitIDVendor3String_Type()
)
pppoePortCircuitIDVendor3String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortCircuitIDVendor3String.setStatus("current")


class _PppoePortRemoteIDType_Type(Integer32):
    """Custom type pppoePortRemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("vendor2", 1),
          ("vendor3", 2))
    )


_PppoePortRemoteIDType_Type.__name__ = "Integer32"
_PppoePortRemoteIDType_Object = MibTableColumn
pppoePortRemoteIDType = _PppoePortRemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1, 6),
    _PppoePortRemoteIDType_Type()
)
pppoePortRemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortRemoteIDType.setStatus("current")


class _PppoePortRemoteIDVendor3String_Type(DisplayString):
    """Custom type pppoePortRemoteIDVendor3String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppoePortRemoteIDVendor3String_Type.__name__ = "DisplayString"
_PppoePortRemoteIDVendor3String_Object = MibTableColumn
pppoePortRemoteIDVendor3String = _PppoePortRemoteIDVendor3String_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 98, 2, 1, 7),
    _PppoePortRemoteIDVendor3String_Type()
)
pppoePortRemoteIDVendor3String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortRemoteIDVendor3String.setStatus("current")
_CompanyAgentBasicInfo_ObjectIdentity = ObjectIdentity
companyAgentBasicInfo = _CompanyAgentBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100)
)
_AgentCPUutilization_ObjectIdentity = ObjectIdentity
agentCPUutilization = _AgentCPUutilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 1)
)
_AgentCPUutilizationIn5sec_Type = Integer32
_AgentCPUutilizationIn5sec_Object = MibScalar
agentCPUutilizationIn5sec = _AgentCPUutilizationIn5sec_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 1, 1),
    _AgentCPUutilizationIn5sec_Type()
)
agentCPUutilizationIn5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCPUutilizationIn5sec.setStatus("current")
_AgentCPUutilizationIn1min_Type = Integer32
_AgentCPUutilizationIn1min_Object = MibScalar
agentCPUutilizationIn1min = _AgentCPUutilizationIn1min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 1, 2),
    _AgentCPUutilizationIn1min_Type()
)
agentCPUutilizationIn1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCPUutilizationIn1min.setStatus("current")
_AgentCPUutilizationIn5min_Type = Integer32
_AgentCPUutilizationIn5min_Object = MibScalar
agentCPUutilizationIn5min = _AgentCPUutilizationIn5min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 1, 3),
    _AgentCPUutilizationIn5min_Type()
)
agentCPUutilizationIn5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCPUutilizationIn5min.setStatus("current")
_AgentMEMutilization_ObjectIdentity = ObjectIdentity
agentMEMutilization = _AgentMEMutilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 2)
)
_AgentMEMutilizationIn5sec_Type = Integer32
_AgentMEMutilizationIn5sec_Object = MibScalar
agentMEMutilizationIn5sec = _AgentMEMutilizationIn5sec_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 2, 1),
    _AgentMEMutilizationIn5sec_Type()
)
agentMEMutilizationIn5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMEMutilizationIn5sec.setStatus("current")
_AgentMEMutilizationIn1min_Type = Integer32
_AgentMEMutilizationIn1min_Object = MibScalar
agentMEMutilizationIn1min = _AgentMEMutilizationIn1min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 2, 2),
    _AgentMEMutilizationIn1min_Type()
)
agentMEMutilizationIn1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMEMutilizationIn1min.setStatus("current")
_AgentMEMutilizationIn5min_Type = Integer32
_AgentMEMutilizationIn5min_Object = MibScalar
agentMEMutilizationIn5min = _AgentMEMutilizationIn5min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 100, 2, 3),
    _AgentMEMutilizationIn5min_Type()
)
agentMEMutilizationIn5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMEMutilizationIn5min.setStatus("current")
_CompanyTraps_ObjectIdentity = ObjectIdentity
companyTraps = _CompanyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0)
)
dot1dBasePortEntry.registerAugmentions(
    ("DGS-1100-06ME-AX",
     "dot1qVlanPortEntry")
)
dot1qVlanPortEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions(
    ("DGS-1100-06ME-AX",
     "lldpXdot3PortConfigEntry")
)
lldpXdot3PortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpPortConfigEntry.registerAugmentions(
    ("DGS-1100-06ME-AX",
     "lldpXdot1ConfigPortVlanEntry")
)
lldpXdot1ConfigPortVlanEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpXdot1LocVlanNameEntry.registerAugmentions(
    ("DGS-1100-06ME-AX",
     "lldpXdot1ConfigVlanNameEntry")
)
lldpXdot1ConfigVlanNameEntry.setIndexNames(*lldpXdot1LocVlanNameEntry.getIndexNames())
lldpXdot1LocProtoVlanEntry.registerAugmentions(
    ("DGS-1100-06ME-AX",
     "lldpXdot1ConfigProtoVlanEntry")
)
lldpXdot1ConfigProtoVlanEntry.setIndexNames(*lldpXdot1LocProtoVlanEntry.getIndexNames())
lldpXdot1LocProtocolEntry.registerAugmentions(
    ("DGS-1100-06ME-AX",
     "lldpXdot1ConfigProtocolEntry")
)
lldpXdot1ConfigProtocolEntry.setIndexNames(*lldpXdot1LocProtocolEntry.getIndexNames())

# Managed Objects groups


# Notification objects

snmpTrapSNMPAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 1)
)
if mibBuilder.loadTexts:
    snmpTrapSNMPAuthentication.setStatus(
        "current"
    )

snmpTrapColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 2)
)
if mibBuilder.loadTexts:
    snmpTrapColdStart.setStatus(
        "current"
    )

snmpTrapWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 3)
)
if mibBuilder.loadTexts:
    snmpTrapWarmStart.setStatus(
        "current"
    )

snmpTrapCopperLinkUpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 4)
)
if mibBuilder.loadTexts:
    snmpTrapCopperLinkUpDown.setStatus(
        "current"
    )

snmpTrapRSTPStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 5)
)
if mibBuilder.loadTexts:
    snmpTrapRSTPStateChange.setStatus(
        "current"
    )

snmpTrapFirmUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 6)
)
if mibBuilder.loadTexts:
    snmpTrapFirmUpgrade.setStatus(
        "current"
    )

snmpTrapPortSecurity = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 12)
)
if mibBuilder.loadTexts:
    snmpTrapPortSecurity.setStatus(
        "current"
    )

snmpTrapLBD = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 14)
)
if mibBuilder.loadTexts:
    snmpTrapLBD.setStatus(
        "current"
    )

macNotificatiotn = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 17)
)
if mibBuilder.loadTexts:
    macNotificatiotn.setStatus(
        "current"
    )

duplicateIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 21)
)
if mibBuilder.loadTexts:
    duplicateIP.setStatus(
        "current"
    )

trafficControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 22)
)
if mibBuilder.loadTexts:
    trafficControl.setStatus(
        "current"
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 23)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )

newRootBrgaddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 24)
)
if mibBuilder.loadTexts:
    newRootBrgaddress.setStatus(
        "current"
    )

newRootOlddesignatedroot = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 25)
)
if mibBuilder.loadTexts:
    newRootOlddesignatedroot.setStatus(
        "current"
    )

newRootMSTibridgeregionalroot = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 134, 1, 1, 120, 0, 26)
)
if mibBuilder.loadTexts:
    newRootMSTibridgeregionalroot.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-1100-06ME-AX",
    **{"VlanIndex": VlanIndex,
       "PortList": PortList,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "LldpManAddress": LldpManAddress,
       "OwnerString": OwnerString,
       "RmonStatus": RmonStatus,
       "Ipv6Address": Ipv6Address,
       "LldpPortNumber": LldpPortNumber,
       "LldpPowerPortClass": LldpPowerPortClass,
       "LldpLinkAggStatusMap": LldpLinkAggStatusMap,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DGS1100SeriesProd": dlink_DGS1100SeriesProd,
       "dgs-1100-06ME": dgs_1100_06ME,
       "dgs-1100-06ME-A1": dgs_1100_06ME_A1,
       "companySystem": companySystem,
       "sysSwitchName": sysSwitchName,
       "sysHardwareVersion": sysHardwareVersion,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysLoginTimeoutInterval": sysLoginTimeoutInterval,
       "sysLocationName": sysLocationName,
       "sysGroupInterval": sysGroupInterval,
       "sysSafeGuardEnable": sysSafeGuardEnable,
       "sysRestart": sysRestart,
       "sysSave": sysSave,
       "sysJumboFrameEnable": sysJumboFrameEnable,
       "sysPortCtrlTable": sysPortCtrlTable,
       "sysPortCtrlEntry": sysPortCtrlEntry,
       "sysPortCtrlIndex": sysPortCtrlIndex,
       "sysPortCtrlMediumType": sysPortCtrlMediumType,
       "sysPortCtrlSpeed": sysPortCtrlSpeed,
       "sysPortCtrlOperStatus": sysPortCtrlOperStatus,
       "sysPortCtrlMDI": sysPortCtrlMDI,
       "sysPortCtrlFlowControl": sysPortCtrlFlowControl,
       "sysPortCtrlFlowControlOper": sysPortCtrlFlowControlOper,
       "sysPortCtrlType": sysPortCtrlType,
       "sysPortCtrlCapability": sysPortCtrlCapability,
       "sysPortDescriptionTable": sysPortDescriptionTable,
       "sysPortDescriptionEntry": sysPortDescriptionEntry,
       "sysPortDescIndex": sysPortDescIndex,
       "sysPortDescMediumType": sysPortDescMediumType,
       "sysPortDescString": sysPortDescString,
       "sysPortErrTable": sysPortErrTable,
       "sysPortErrEntry": sysPortErrEntry,
       "sysPortErrPortIndex": sysPortErrPortIndex,
       "sysPortErrPortState": sysPortErrPortState,
       "sysPortErrPortStatus": sysPortErrPortStatus,
       "sysPortErrPortReason": sysPortErrPortReason,
       "sysDhcpAutoConfiguration": sysDhcpAutoConfiguration,
       "sysWebState": sysWebState,
       "sysWebPortNumber": sysWebPortNumber,
       "sysARPAgingTime": sysARPAgingTime,
       "sysMACAgingTime": sysMACAgingTime,
       "telnetsettingManagementOnOff": telnetsettingManagementOnOff,
       "telnetUDPPort": telnetUDPPort,
       "autoRefreshConfiguration": autoRefreshConfiguration,
       "floodfdbOnOff": floodfdbOnOff,
       "sysContactName": sysContactName,
       "sysCommandLogging": sysCommandLogging,
       "sysSerialNumber": sysSerialNumber,
       "sysDhcpAutoImage": sysDhcpAutoImage,
       "sysBootupConfigID": sysBootupConfigID,
       "sysBootupImage": sysBootupImage,
       "companyIpifGroup": companyIpifGroup,
       "ipifSupportV4V6Info": ipifSupportV4V6Info,
       "sysIpAddrCfgMode": sysIpAddrCfgMode,
       "sysIpAddr": sysIpAddr,
       "sysIpSubnetMask": sysIpSubnetMask,
       "sysGateway": sysGateway,
       "dhcpOption12Status": dhcpOption12Status,
       "dhcpOption12HostName": dhcpOption12HostName,
       "ipifName": ipifName,
       "ipifVLANname": ipifVLANname,
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
       "dhcpRetryCount": dhcpRetryCount,
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
       "snmpV3TrapColdStart": snmpV3TrapColdStart,
       "snmpV3TrapWarmStart": snmpV3TrapWarmStart,
       "snmpV3TrapLinkUpDown": snmpV3TrapLinkUpDown,
       "snmpV3TrapPortSecurity": snmpV3TrapPortSecurity,
       "snmpV3TrapLBD": snmpV3TrapLBD,
       "companyDot1qVlanGroup": companyDot1qVlanGroup,
       "dot1qVlanManagementOnOff": dot1qVlanManagementOnOff,
       "dot1qVlanManagementid": dot1qVlanManagementid,
       "dot1qVlanAsyOnOff": dot1qVlanAsyOnOff,
       "dot1qVlanTable": dot1qVlanTable,
       "dot1qVlanEntry": dot1qVlanEntry,
       "dot1qVlanName": dot1qVlanName,
       "dot1qVlanEgressPorts": dot1qVlanEgressPorts,
       "dot1qVlanForbiddenPorts": dot1qVlanForbiddenPorts,
       "dot1qVlanUntaggedPorts": dot1qVlanUntaggedPorts,
       "dot1qVlanRowStatus": dot1qVlanRowStatus,
       "dot1qVlanPortTable": dot1qVlanPortTable,
       "dot1qVlanPortEntry": dot1qVlanPortEntry,
       "dot1qVlanPvid": dot1qVlanPvid,
       "dot1qVlanPVIDAutoAssignOnOff": dot1qVlanPVIDAutoAssignOnOff,
       "companyStaticMAC": companyStaticMAC,
       "staticDisableAutoLearn": staticDisableAutoLearn,
       "staticAutoLearningList": staticAutoLearningList,
       "staticTable": staticTable,
       "staticEntry": staticEntry,
       "staticVlanID": staticVlanID,
       "staticMac": staticMac,
       "staticPort": staticPort,
       "staticStatus": staticStatus,
       "autoFdbTable": autoFdbTable,
       "autoFdbEntry": autoFdbEntry,
       "autoFdbIPAddress": autoFdbIPAddress,
       "autoFdbVlanID": autoFdbVlanID,
       "autoFdbMacAddress": autoFdbMacAddress,
       "autoFdbPort": autoFdbPort,
       "autoFdbTimeStamp": autoFdbTimeStamp,
       "autoFdbStatus": autoFdbStatus,
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
       "igsAccessAuth": igsAccessAuth,
       "igsAccessAuthTable": igsAccessAuthTable,
       "igsAccessAuthEntry": igsAccessAuthEntry,
       "igsAccessAuthPortIndex": igsAccessAuthPortIndex,
       "igsAccessAuthState": igsAccessAuthState,
       "igsHost": igsHost,
       "igsHostTable": igsHostTable,
       "igsHostEntry": igsHostEntry,
       "igsHostTableVLANID": igsHostTableVLANID,
       "igsHostTableGroupAddress": igsHostTableGroupAddress,
       "igsHostTablePort": igsHostTablePort,
       "igsHostTableHostIPAddress": igsHostTableHostIPAddress,
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
       "qosAclPrioritySettings": qosAclPrioritySettings,
       "aclQosTable": aclQosTable,
       "aclQosEntry": aclQosEntry,
       "aclQosIndex": aclQosIndex,
       "aclQosType": aclQosType,
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
       "bandwidthEffecTxThreshold": bandwidthEffecTxThreshold,
       "bandwidthEffecRxThreshold": bandwidthEffecRxThreshold,
       "trafficCtrlSettings": trafficCtrlSettings,
       "trafficCtrlTrap": trafficCtrlTrap,
       "trafficCtrlTable": trafficCtrlTable,
       "trafficCtrlEntry": trafficCtrlEntry,
       "trafficCtrlIndex": trafficCtrlIndex,
       "trafficCtrlActionMode": trafficCtrlActionMode,
       "trafficCtrlType": trafficCtrlType,
       "trafficCtrlThreshold": trafficCtrlThreshold,
       "trafficCtrlCountDown": trafficCtrlCountDown,
       "trafficCtrlTimeInterval": trafficCtrlTimeInterval,
       "trafficCtrlAutoRecoverTime": trafficCtrlAutoRecoverTime,
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
       "portSecLockAddrMode": portSecLockAddrMode,
       "portSecFDBPermanentTable": portSecFDBPermanentTable,
       "portSecFDBPermanentEntry": portSecFDBPermanentEntry,
       "portSecFDBPermIndex": portSecFDBPermIndex,
       "portSecFDBPermVlanID": portSecFDBPermVlanID,
       "portSecFDBPermMac": portSecFDBPermMac,
       "portSecFDBPermPort": portSecFDBPermPort,
       "securityTrafficSeg": securityTrafficSeg,
       "trafficSegTable": trafficSegTable,
       "trafficSegEntry": trafficSegEntry,
       "trafficSegIfIndex": trafficSegIfIndex,
       "trafficSegMemberList": trafficSegMemberList,
       "securityAAC": securityAAC,
       "aacAuthenAdminState": aacAuthenAdminState,
       "aacAuthParamResponseTimeout": aacAuthParamResponseTimeout,
       "aacAuthParamAttempt": aacAuthParamAttempt,
       "aacAPAuthMethodGroup": aacAPAuthMethodGroup,
       "aacAPLoginMethod": aacAPLoginMethod,
       "aacAPTelnetLoginMethod": aacAPTelnetLoginMethod,
       "aacAPHttpLoginMethod": aacAPHttpLoginMethod,
       "aacAPEnableMethod": aacAPEnableMethod,
       "aacAPTelnetEnableMethod": aacAPTelnetEnableMethod,
       "aacAPHttpEnableMethod": aacAPHttpEnableMethod,
       "aacServerGroupTable": aacServerGroupTable,
       "aacServerGroupEntry": aacServerGroupEntry,
       "aacServerGroupIndex": aacServerGroupIndex,
       "aacServerGroupName": aacServerGroupName,
       "aacServersInGroup": aacServersInGroup,
       "aacServerGroupRowStatus": aacServerGroupRowStatus,
       "aacServerInfoTable": aacServerInfoTable,
       "aacServerInfoEntry": aacServerInfoEntry,
       "aacServerIndex": aacServerIndex,
       "aacServerIPType": aacServerIPType,
       "aacServerIPAddr": aacServerIPAddr,
       "aacServerInterfaceName": aacServerInterfaceName,
       "aacServerAuthProtocol": aacServerAuthProtocol,
       "aacServerAuthPort": aacServerAuthPort,
       "aacServerAuthKey": aacServerAuthKey,
       "aacServerTimeout": aacServerTimeout,
       "aacServerRetryCount": aacServerRetryCount,
       "aacServerRowStatus": aacServerRowStatus,
       "aacLoginMethodListTable": aacLoginMethodListTable,
       "aacLoginMethodListEntry": aacLoginMethodListEntry,
       "aacLoginMethodListIndex": aacLoginMethodListIndex,
       "aacLoginMethodListName": aacLoginMethodListName,
       "aacLoginMethod1": aacLoginMethod1,
       "aacLoginMethod2": aacLoginMethod2,
       "aacLoginMethod3": aacLoginMethod3,
       "aacLoginMethod4": aacLoginMethod4,
       "aacLoginMethodListRowStatus": aacLoginMethodListRowStatus,
       "aacEnableMethodListTable": aacEnableMethodListTable,
       "aacEnableMethodListEntry": aacEnableMethodListEntry,
       "aacEnableMethodListIndex": aacEnableMethodListIndex,
       "aacEnableMethodListName": aacEnableMethodListName,
       "aacEnableMethod1": aacEnableMethod1,
       "aacEnableMethod2": aacEnableMethod2,
       "aacEnableMethod3": aacEnableMethod3,
       "aacEnableMethod4": aacEnableMethod4,
       "aacEnableMethodListRowStatus": aacEnableMethodListRowStatus,
       "aacLocalEnablePassword": aacLocalEnablePassword,
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
       "ipv4aclProfileIPProtocolMask": ipv4aclProfileIPProtocolMask,
       "ipv4aclProfileDstIpAddrMask": ipv4aclProfileDstIpAddrMask,
       "ipv4aclProfileSrcIpAddrMask": ipv4aclProfileSrcIpAddrMask,
       "ipv4aclProfileDstPortMask": ipv4aclProfileDstPortMask,
       "ipv4aclProfileSrcPortMask": ipv4aclProfileSrcPortMask,
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
       "aclProfileIPProtocolMask": aclProfileIPProtocolMask,
       "aclProfileDstIpAddrMaskType": aclProfileDstIpAddrMaskType,
       "aclProfileDstIpAddrMask": aclProfileDstIpAddrMask,
       "aclProfileSrcIpAddrMaskType": aclProfileSrcIpAddrMaskType,
       "aclProfileSrcIpAddrMask": aclProfileSrcIpAddrMask,
       "aclProfileDstPortMask": aclProfileDstPortMask,
       "aclProfileSrcPortMask": aclProfileSrcPortMask,
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
       "aclL2RuleRateLimit": aclL2RuleRateLimit,
       "aclL2RuleReplaceDSCP": aclL2RuleReplaceDSCP,
       "aclL2RuleNonIPFilterOnlyState": aclL2RuleNonIPFilterOnlyState,
       "aclL2RuleStatus": aclL2RuleStatus,
       "aclL3Rule": aclL3Rule,
       "aclL3RuleTable": aclL3RuleTable,
       "aclL3RuleEntry": aclL3RuleEntry,
       "aclL3RuleAccessID": aclL3RuleAccessID,
       "aclL3RuleProfileNo": aclL3RuleProfileNo,
       "aclL3RuleProtocol": aclL3RuleProtocol,
       "aclL3RuleProtocolMask": aclL3RuleProtocolMask,
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
       "aclL3RuleTos": aclL3RuleTos,
       "aclL3RuleIgmpType": aclL3RuleIgmpType,
       "aclL3RulePortList": aclL3RulePortList,
       "aclL3RuleAction": aclL3RuleAction,
       "aclL3RuleRateLimit": aclL3RuleRateLimit,
       "aclL3RuleReplaceDSCP": aclL3RuleReplaceDSCP,
       "aclL3RuleStatus": aclL3RuleStatus,
       "aclv6L3RuleTable": aclv6L3RuleTable,
       "aclv6L3RuleEntry": aclv6L3RuleEntry,
       "aclv6L3RuleAccessID": aclv6L3RuleAccessID,
       "aclv6L3RuleProfileNo": aclv6L3RuleProfileNo,
       "aclv6L3RuleProtocol": aclv6L3RuleProtocol,
       "aclv6L3RuleProtocolMask": aclv6L3RuleProtocolMask,
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
       "aclv6L3RuleRateLimit": aclv6L3RuleRateLimit,
       "aclv6L3RuleReplaceDSCP": aclv6L3RuleReplaceDSCP,
       "aclv6L3RuleStatus": aclv6L3RuleStatus,
       "companySyslog": companySyslog,
       "syslogSettingGroup": syslogSettingGroup,
       "syslogEnable": syslogEnable,
       "syslogSaveMode": syslogSaveMode,
       "syslogSaveMinutes": syslogSaveMinutes,
       "syslogServerGroup": syslogServerGroup,
       "syslogServTable": syslogServTable,
       "syslogServEntry": syslogServEntry,
       "syslogServIndex": syslogServIndex,
       "syslogServAddrType": syslogServAddrType,
       "syslogServAddr": syslogServAddr,
       "syslogServInterfaceName": syslogServInterfaceName,
       "syslogServSeverity": syslogServSeverity,
       "syslogServFacility": syslogServFacility,
       "syslogServUDPport": syslogServUDPport,
       "syslogServSrvStatus": syslogServSrvStatus,
       "syslogServSrvRowStatus": syslogServSrvRowStatus,
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
       "companyStaticMcast": companyStaticMcast,
       "staticMcastTable": staticMcastTable,
       "staticMcastEntry": staticMcastEntry,
       "staticMcastVlanID": staticMcastVlanID,
       "staticMcastMac": staticMcastMac,
       "staticMcastEgressPorts": staticMcastEgressPorts,
       "staticMcastIpAddr": staticMcastIpAddr,
       "staticMcastStatus": staticMcastStatus,
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
       "sysSNTPDSTMethod": sysSNTPDSTMethod,
       "sysSNTPDSTRepeatStartMon": sysSNTPDSTRepeatStartMon,
       "sysSNTPDSTRepeatStartWeek": sysSNTPDSTRepeatStartWeek,
       "sysSNTPDSTRepeatStartWeekDay": sysSNTPDSTRepeatStartWeekDay,
       "sysSNTPDSTRepeatStartHour": sysSNTPDSTRepeatStartHour,
       "sysSNTPDSTRepeatStartMin": sysSNTPDSTRepeatStartMin,
       "sysSNTPDSTRepeatEndMon": sysSNTPDSTRepeatEndMon,
       "sysSNTPDSTRepeatEndWeek": sysSNTPDSTRepeatEndWeek,
       "sysSNTPDSTRepeatEndWeekDay": sysSNTPDSTRepeatEndWeekDay,
       "sysSNTPDSTRepeatEndHour": sysSNTPDSTRepeatEndHour,
       "sysSNTPDSTRepeatEndMin": sysSNTPDSTRepeatEndMin,
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
       "swAuthMode": swAuthMode,
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
       "companyGuestVlan": companyGuestVlan,
       "guestVlanName": guestVlanName,
       "guestVlanPort": guestVlanPort,
       "guestVlanDelState": guestVlanDelState,
       "companyMacNotify": companyMacNotify,
       "macNotifyState": macNotifyState,
       "macNotifyInterval": macNotifyInterval,
       "macNotifyHistorySize": macNotifyHistorySize,
       "macNotifyCtrlTable": macNotifyCtrlTable,
       "macNotifyCtrlEntry": macNotifyCtrlEntry,
       "macNotifyCtrlIndex": macNotifyCtrlIndex,
       "macNotifyPortStatus": macNotifyPortStatus,
       "macNotifyInfo": macNotifyInfo,
       "macNotifyInfoDiscription": macNotifyInfoDiscription,
       "companyISMVLAN": companyISMVLAN,
       "igmpMulticastVlanStatus": igmpMulticastVlanStatus,
       "multicastVlanTable": multicastVlanTable,
       "multicastVlanEntry": multicastVlanEntry,
       "multicastVlanid": multicastVlanid,
       "multicastVlanName": multicastVlanName,
       "multicastVlanSourcePort": multicastVlanSourcePort,
       "multicastVlanMemberPort": multicastVlanMemberPort,
       "multicastVlanTagMemberPort": multicastVlanTagMemberPort,
       "multicastVlanState": multicastVlanState,
       "multicastVlanIgmpReplaceSourceIp": multicastVlanIgmpReplaceSourceIp,
       "multicastVlanMldReplaceSourceIp": multicastVlanMldReplaceSourceIp,
       "multicastVlanRowStatus": multicastVlanRowStatus,
       "multicastVlanGroupTable": multicastVlanGroupTable,
       "multicastVlanGroupEntry": multicastVlanGroupEntry,
       "multicastVlanGroupVid": multicastVlanGroupVid,
       "multicastVlanGroupIpType": multicastVlanGroupIpType,
       "multicastVlanGroupFromIp": multicastVlanGroupFromIp,
       "multicastVlanGroupToIp": multicastVlanGroupToIp,
       "multicastVlanGroupStatus": multicastVlanGroupStatus,
       "companyDHCPRelay": companyDHCPRelay,
       "dhcpBOOTPRelayControl": dhcpBOOTPRelayControl,
       "dhcpBOOTPRelayState": dhcpBOOTPRelayState,
       "dhcpBOOTPRelayHopCount": dhcpBOOTPRelayHopCount,
       "dhcpBOOTPRelayTimeThreshold": dhcpBOOTPRelayTimeThreshold,
       "dhcpBOOTPRelayEnablePortlist": dhcpBOOTPRelayEnablePortlist,
       "dhcpRelayVlanTable": dhcpRelayVlanTable,
       "dhcpRelayVlanTableEntry": dhcpRelayVlanTableEntry,
       "dhcpRelayVlanSettingsVLANID": dhcpRelayVlanSettingsVLANID,
       "dhcpRelayVlanSettingsState": dhcpRelayVlanSettingsState,
       "dhcpBOOTPRelayManagement": dhcpBOOTPRelayManagement,
       "dhcpBOOTPRelayInterfaceSettingsTable": dhcpBOOTPRelayInterfaceSettingsTable,
       "dhcpBOOTPRelayInterfaceSettingsEntry": dhcpBOOTPRelayInterfaceSettingsEntry,
       "dhcpBOOTPRelayInterface": dhcpBOOTPRelayInterface,
       "dhcpBOOTPRelayServerIP": dhcpBOOTPRelayServerIP,
       "dhcpBOOTPRelayInterfaceSettingsRowStatus": dhcpBOOTPRelayInterfaceSettingsRowStatus,
       "dhcpBOOTPRelayManagementOption82": dhcpBOOTPRelayManagementOption82,
       "dhcpBOOTPRelayOption82State": dhcpBOOTPRelayOption82State,
       "dhcpBOOTPRelayOption82CheckState": dhcpBOOTPRelayOption82CheckState,
       "dhcpBOOTPRelayOption82Policy": dhcpBOOTPRelayOption82Policy,
       "dhcpBOOTPRelayOption82RemoteIDType": dhcpBOOTPRelayOption82RemoteIDType,
       "dhcpBOOTPRelayOption82RemoteID": dhcpBOOTPRelayOption82RemoteID,
       "companyDHCPLocalRelay": companyDHCPLocalRelay,
       "dhcpLocalRelayGlobalState": dhcpLocalRelayGlobalState,
       "dhcpLocalRelayTable": dhcpLocalRelayTable,
       "dhcpLocalRelayTableEntry": dhcpLocalRelayTableEntry,
       "dhcpLocalRelaySettingsVLANID": dhcpLocalRelaySettingsVLANID,
       "dhcpLocalRelaySettingsState": dhcpLocalRelaySettingsState,
       "dhcpLocalRelayEnablePortlist": dhcpLocalRelayEnablePortlist,
       "companyTrapSetting": companyTrapSetting,
       "sysTrapIP": sysTrapIP,
       "sysTrapSystemEvent": sysTrapSystemEvent,
       "sysTrapFiberPortEvent": sysTrapFiberPortEvent,
       "sysTrapTwistedPortEvent": sysTrapTwistedPortEvent,
       "sysTrapStatus": sysTrapStatus,
       "sysTrapPortSecurity": sysTrapPortSecurity,
       "sysTrapLBD": sysTrapLBD,
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
       "dlinkPowerSavCableLenDetectionState": dlinkPowerSavCableLenDetectionState,
       "companyLLDPSetting": companyLLDPSetting,
       "dlinklldpState": dlinklldpState,
       "dlinklldpMsgHoldMultiplier": dlinklldpMsgHoldMultiplier,
       "dlinklldpMsgTxInterval": dlinklldpMsgTxInterval,
       "dlinklldpReinitDelay": dlinklldpReinitDelay,
       "dlinklldpTxDelay": dlinklldpTxDelay,
       "dlinklldpConfigManAddrPortsTxEnable": dlinklldpConfigManAddrPortsTxEnable,
       "lldpPortConfigTable": lldpPortConfigTable,
       "lldpPortConfigEntry": lldpPortConfigEntry,
       "lldpPortConfigPortNum": lldpPortConfigPortNum,
       "lldpPortConfigAdminStatus": lldpPortConfigAdminStatus,
       "lldpPortConfigNotificationEnable": lldpPortConfigNotificationEnable,
       "lldpPortConfigTLVsTxEnable": lldpPortConfigTLVsTxEnable,
       "lldpXdot3Objects": lldpXdot3Objects,
       "lldpXdot3Config": lldpXdot3Config,
       "lldpXdot3PortConfigTable": lldpXdot3PortConfigTable,
       "lldpXdot3PortConfigEntry": lldpXdot3PortConfigEntry,
       "lldpXdot3PortConfigTLVsTxEnable": lldpXdot3PortConfigTLVsTxEnable,
       "lldpXdot3LocalData": lldpXdot3LocalData,
       "lldpXdot3LocPortTable": lldpXdot3LocPortTable,
       "lldpXdot3LocPortEntry": lldpXdot3LocPortEntry,
       "lldpXdot3LocPortAutoNegSupported": lldpXdot3LocPortAutoNegSupported,
       "lldpXdot3LocPortAutoNegEnabled": lldpXdot3LocPortAutoNegEnabled,
       "lldpXdot3LocPortAutoNegAdvertisedCap": lldpXdot3LocPortAutoNegAdvertisedCap,
       "lldpXdot3LocPortOperMauType": lldpXdot3LocPortOperMauType,
       "lldpXdot3LocPowerTable": lldpXdot3LocPowerTable,
       "lldpXdot3LocPowerEntry": lldpXdot3LocPowerEntry,
       "lldpXdot3LocPowerPortClass": lldpXdot3LocPowerPortClass,
       "lldpXdot3LocPowerMDISupported": lldpXdot3LocPowerMDISupported,
       "lldpXdot3LocPowerMDIEnabled": lldpXdot3LocPowerMDIEnabled,
       "lldpXdot3LocPowerPairControlable": lldpXdot3LocPowerPairControlable,
       "lldpXdot3LocPowerPairs": lldpXdot3LocPowerPairs,
       "lldpXdot3LocPowerClass": lldpXdot3LocPowerClass,
       "lldpXdot3LocLinkAggTable": lldpXdot3LocLinkAggTable,
       "lldpXdot3LocLinkAggEntry": lldpXdot3LocLinkAggEntry,
       "lldpXdot3LocLinkAggStatus": lldpXdot3LocLinkAggStatus,
       "lldpXdot3LocLinkAggPortId": lldpXdot3LocLinkAggPortId,
       "lldpXdot3LocMaxFrameSizeTable": lldpXdot3LocMaxFrameSizeTable,
       "lldpXdot3LocMaxFrameSizeEntry": lldpXdot3LocMaxFrameSizeEntry,
       "lldpXdot3LocMaxFrameSize": lldpXdot3LocMaxFrameSize,
       "lldpXdot3RemoteData": lldpXdot3RemoteData,
       "lldpXdot3RemPortTable": lldpXdot3RemPortTable,
       "lldpXdot3RemPortEntry": lldpXdot3RemPortEntry,
       "lldpXdot3RemPortAutoNegSupported": lldpXdot3RemPortAutoNegSupported,
       "lldpXdot3RemPortAutoNegEnabled": lldpXdot3RemPortAutoNegEnabled,
       "lldpXdot3RemPortAutoNegAdvertisedCap": lldpXdot3RemPortAutoNegAdvertisedCap,
       "lldpXdot3RemPortOperMauType": lldpXdot3RemPortOperMauType,
       "lldpXdot3RemPowerTable": lldpXdot3RemPowerTable,
       "lldpXdot3RemPowerEntry": lldpXdot3RemPowerEntry,
       "lldpXdot3RemPowerPortClass": lldpXdot3RemPowerPortClass,
       "lldpXdot3RemPowerMDISupported": lldpXdot3RemPowerMDISupported,
       "lldpXdot3RemPowerMDIEnabled": lldpXdot3RemPowerMDIEnabled,
       "lldpXdot3RemPowerPairControlable": lldpXdot3RemPowerPairControlable,
       "lldpXdot3RemPowerPairs": lldpXdot3RemPowerPairs,
       "lldpXdot3RemPowerClass": lldpXdot3RemPowerClass,
       "lldpXdot3RemLinkAggTable": lldpXdot3RemLinkAggTable,
       "lldpXdot3RemLinkAggEntry": lldpXdot3RemLinkAggEntry,
       "lldpXdot3RemLinkAggStatus": lldpXdot3RemLinkAggStatus,
       "lldpXdot3RemLinkAggPortId": lldpXdot3RemLinkAggPortId,
       "lldpXdot3RemMaxFrameSizeTable": lldpXdot3RemMaxFrameSizeTable,
       "lldpXdot3RemMaxFrameSizeEntry": lldpXdot3RemMaxFrameSizeEntry,
       "lldpXdot3RemMaxFrameSize": lldpXdot3RemMaxFrameSize,
       "lldpXdot1Objects": lldpXdot1Objects,
       "lldpXdot1Config": lldpXdot1Config,
       "lldpXdot1ConfigPortVlanTable": lldpXdot1ConfigPortVlanTable,
       "lldpXdot1ConfigPortVlanEntry": lldpXdot1ConfigPortVlanEntry,
       "lldpXdot1ConfigPortVlanTxEnable": lldpXdot1ConfigPortVlanTxEnable,
       "lldpXdot1ConfigVlanNameTable": lldpXdot1ConfigVlanNameTable,
       "lldpXdot1ConfigVlanNameEntry": lldpXdot1ConfigVlanNameEntry,
       "lldpXdot1ConfigVlanNameTxEnable": lldpXdot1ConfigVlanNameTxEnable,
       "lldpXdot1ConfigProtoVlanTable": lldpXdot1ConfigProtoVlanTable,
       "lldpXdot1ConfigProtoVlanEntry": lldpXdot1ConfigProtoVlanEntry,
       "lldpXdot1ConfigProtoVlanTxEnable": lldpXdot1ConfigProtoVlanTxEnable,
       "lldpXdot1ConfigProtocolTable": lldpXdot1ConfigProtocolTable,
       "lldpXdot1ConfigProtocolEntry": lldpXdot1ConfigProtocolEntry,
       "lldpXdot1ConfigProtocolTxEnable": lldpXdot1ConfigProtocolTxEnable,
       "lldpXdot1LocalData": lldpXdot1LocalData,
       "lldpXdot1LocTable": lldpXdot1LocTable,
       "lldpXdot1LocEntry": lldpXdot1LocEntry,
       "lldpXdot1LocPortVlanId": lldpXdot1LocPortVlanId,
       "lldpXdot1LocProtoVlanTable": lldpXdot1LocProtoVlanTable,
       "lldpXdot1LocProtoVlanEntry": lldpXdot1LocProtoVlanEntry,
       "lldpXdot1LocProtoVlanId": lldpXdot1LocProtoVlanId,
       "lldpXdot1LocProtoVlanSupported": lldpXdot1LocProtoVlanSupported,
       "lldpXdot1LocProtoVlanEnabled": lldpXdot1LocProtoVlanEnabled,
       "lldpXdot1LocVlanNameTable": lldpXdot1LocVlanNameTable,
       "lldpXdot1LocVlanNameEntry": lldpXdot1LocVlanNameEntry,
       "lldpXdot1LocVlanId": lldpXdot1LocVlanId,
       "lldpXdot1LocVlanName": lldpXdot1LocVlanName,
       "lldpXdot1LocProtocolTable": lldpXdot1LocProtocolTable,
       "lldpXdot1LocProtocolEntry": lldpXdot1LocProtocolEntry,
       "lldpXdot1LocProtocolIndex": lldpXdot1LocProtocolIndex,
       "lldpXdot1LocProtocolId": lldpXdot1LocProtocolId,
       "lldpXdot1RemoteData": lldpXdot1RemoteData,
       "lldpXdot1RemTable": lldpXdot1RemTable,
       "lldpXdot1RemEntry": lldpXdot1RemEntry,
       "lldpXdot1RemPortVlanId": lldpXdot1RemPortVlanId,
       "lldpXdot1RemProtoVlanTable": lldpXdot1RemProtoVlanTable,
       "lldpXdot1RemProtoVlanEntry": lldpXdot1RemProtoVlanEntry,
       "lldpXdot1RemProtoVlanId": lldpXdot1RemProtoVlanId,
       "lldpXdot1RemProtoVlanSupported": lldpXdot1RemProtoVlanSupported,
       "lldpXdot1RemProtoVlanEnabled": lldpXdot1RemProtoVlanEnabled,
       "lldpXdot1RemVlanNameTable": lldpXdot1RemVlanNameTable,
       "lldpXdot1RemVlanNameEntry": lldpXdot1RemVlanNameEntry,
       "lldpXdot1RemVlanId": lldpXdot1RemVlanId,
       "lldpXdot1RemVlanName": lldpXdot1RemVlanName,
       "lldpXdot1RemProtocolTable": lldpXdot1RemProtocolTable,
       "lldpXdot1RemProtocolEntry": lldpXdot1RemProtocolEntry,
       "lldpXdot1RemProtocolIndex": lldpXdot1RemProtocolIndex,
       "lldpXdot1RemProtocolId": lldpXdot1RemProtocolId,
       "companyCPUInterfaceFilterGroup": companyCPUInterfaceFilterGroup,
       "cpuFilterProfile": cpuFilterProfile,
       "ipv4cpuFilterProfileTable": ipv4cpuFilterProfileTable,
       "ipv4cpuFilterProfileEntry": ipv4cpuFilterProfileEntry,
       "ipv4cpuFilterProfileNo": ipv4cpuFilterProfileNo,
       "ipv4cpuFilterProfileType": ipv4cpuFilterProfileType,
       "ipv4cpuFilterProfileRuleCount": ipv4cpuFilterProfileRuleCount,
       "ipv4cpuFilterProfileMask": ipv4cpuFilterProfileMask,
       "ipv4cpuFilterProfileDstMacAddrMask": ipv4cpuFilterProfileDstMacAddrMask,
       "ipv4cpuFilterProfileSrcMacAddrMask": ipv4cpuFilterProfileSrcMacAddrMask,
       "ipv4cpuFilterProfileIPProtocol": ipv4cpuFilterProfileIPProtocol,
       "ipv4cpuFilterProfileIPProtocolMask": ipv4cpuFilterProfileIPProtocolMask,
       "ipv4cpuFilterProfileDstIpAddrMask": ipv4cpuFilterProfileDstIpAddrMask,
       "ipv4cpuFilterProfileSrcIpAddrMask": ipv4cpuFilterProfileSrcIpAddrMask,
       "ipv4cpuFilterProfileDstPortMask": ipv4cpuFilterProfileDstPortMask,
       "ipv4cpuFilterProfileSrcPortMask": ipv4cpuFilterProfileSrcPortMask,
       "ipv4cpuFilterProfileStatus": ipv4cpuFilterProfileStatus,
       "cpuFilterProfileTable": cpuFilterProfileTable,
       "cpuFilterProfileEntry": cpuFilterProfileEntry,
       "cpuFilterProfileNo": cpuFilterProfileNo,
       "cpuFilterProfileType": cpuFilterProfileType,
       "cpuFilterProfileRuleCount": cpuFilterProfileRuleCount,
       "cpuFilterProfileMask": cpuFilterProfileMask,
       "cpuFilterProfileDstMacAddrMask": cpuFilterProfileDstMacAddrMask,
       "cpuFilterProfileSrcMacAddrMask": cpuFilterProfileSrcMacAddrMask,
       "cpuFilterProfileIPProtocol": cpuFilterProfileIPProtocol,
       "cpuFilterProfileIPProtocolMask": cpuFilterProfileIPProtocolMask,
       "cpuFilterProfileDstIpAddrMaskType": cpuFilterProfileDstIpAddrMaskType,
       "cpuFilterProfileDstIpAddrMask": cpuFilterProfileDstIpAddrMask,
       "cpuFilterProfileSrcIpAddrMaskType": cpuFilterProfileSrcIpAddrMaskType,
       "cpuFilterProfileSrcIpAddrMask": cpuFilterProfileSrcIpAddrMask,
       "cpuFilterProfileDstPortMask": cpuFilterProfileDstPortMask,
       "cpuFilterProfileSrcPortMask": cpuFilterProfileSrcPortMask,
       "cpuFilterProfileStatus": cpuFilterProfileStatus,
       "cpuFilterL2Rule": cpuFilterL2Rule,
       "cpuFilterL2RuleTable": cpuFilterL2RuleTable,
       "cpuFilterL2RuleEntry": cpuFilterL2RuleEntry,
       "cpuFilterL2ProfileID": cpuFilterL2ProfileID,
       "cpuFilterL2AccessID": cpuFilterL2AccessID,
       "cpuFilterL2RuleEtherType": cpuFilterL2RuleEtherType,
       "cpuFilterL2RuleDstMacAddr": cpuFilterL2RuleDstMacAddr,
       "cpuFilterL2RuleSrcMacAddr": cpuFilterL2RuleSrcMacAddr,
       "cpuFilterL2RuleVlanId": cpuFilterL2RuleVlanId,
       "cpuFilterL2Rule1pPriority": cpuFilterL2Rule1pPriority,
       "cpuFilterL2RuleDstMacAddrMask": cpuFilterL2RuleDstMacAddrMask,
       "cpuFilterL2RuleSrcMacAddrMask": cpuFilterL2RuleSrcMacAddrMask,
       "cpuFilterL2RuleInPortList": cpuFilterL2RuleInPortList,
       "cpuFilterL2RuleAction": cpuFilterL2RuleAction,
       "cpuFilterL2RuleStatus": cpuFilterL2RuleStatus,
       "cpuFilterL3Rule": cpuFilterL3Rule,
       "cpuFilterL3RuleTable": cpuFilterL3RuleTable,
       "cpuFilterL3RuleEntry": cpuFilterL3RuleEntry,
       "cpuFilterL3RuleProfileNo": cpuFilterL3RuleProfileNo,
       "cpuFilterL3RuleAccessID": cpuFilterL3RuleAccessID,
       "cpuFilterL3RuleProtocol": cpuFilterL3RuleProtocol,
       "cpuFilterL3RuleProtocolMask": cpuFilterL3RuleProtocolMask,
       "cpuFilterL3RuleICMPMessageType": cpuFilterL3RuleICMPMessageType,
       "cpuFilterL3RuleICMPMessageCode": cpuFilterL3RuleICMPMessageCode,
       "cpuFilterL3RuleDstIpAddr": cpuFilterL3RuleDstIpAddr,
       "cpuFilterL3RuleSrcIpAddr": cpuFilterL3RuleSrcIpAddr,
       "cpuFilterL3RuleDstIpAddrMask": cpuFilterL3RuleDstIpAddrMask,
       "cpuFilterL3RuleSrcIpAddrMask": cpuFilterL3RuleSrcIpAddrMask,
       "cpuFilterL3RuleTcpUdpDstPort": cpuFilterL3RuleTcpUdpDstPort,
       "cpuFilterL3RuleTcpUdpSrcPort": cpuFilterL3RuleTcpUdpSrcPort,
       "cpuFilterL3RuleTcpUdpDstPortMask": cpuFilterL3RuleTcpUdpDstPortMask,
       "cpuFilterL3RuleTcpUdpSrcPortMask": cpuFilterL3RuleTcpUdpSrcPortMask,
       "cpuFilterL3RuleTcpAckBit": cpuFilterL3RuleTcpAckBit,
       "cpuFilterL3RuleTcpRstBit": cpuFilterL3RuleTcpRstBit,
       "cpuFilterL3RuleTcpUrgBit": cpuFilterL3RuleTcpUrgBit,
       "cpuFilterL3RuleTcpPshBit": cpuFilterL3RuleTcpPshBit,
       "cpuFilterL3RuleTcpSynBit": cpuFilterL3RuleTcpSynBit,
       "cpuFilterL3RuleTcpFinBit": cpuFilterL3RuleTcpFinBit,
       "cpuFilterL3RuleDscp": cpuFilterL3RuleDscp,
       "cpuFilterL3RuleIgmpType": cpuFilterL3RuleIgmpType,
       "cpuFilterL3RulePortList": cpuFilterL3RulePortList,
       "cpuFilterL3RuleAction": cpuFilterL3RuleAction,
       "cpuFilterL3RuleStatus": cpuFilterL3RuleStatus,
       "cpuFilterv6L3RuleTable": cpuFilterv6L3RuleTable,
       "cpuFilterv6L3RuleEntry": cpuFilterv6L3RuleEntry,
       "cpuFilterv6L3RuleProfileNo": cpuFilterv6L3RuleProfileNo,
       "cpuFilterv6L3RuleAccessID": cpuFilterv6L3RuleAccessID,
       "cpuFilterv6L3RuleProtocol": cpuFilterv6L3RuleProtocol,
       "cpuFilterv6L3RuleProtocolMask": cpuFilterv6L3RuleProtocolMask,
       "cpuFilterv6L3RuleICMPMessageType": cpuFilterv6L3RuleICMPMessageType,
       "cpuFilterv6L3RuleICMPMessageCode": cpuFilterv6L3RuleICMPMessageCode,
       "cpuFilterv6L3RuleDstIpAddr": cpuFilterv6L3RuleDstIpAddr,
       "cpuFilterv6L3RuleSrcIpAddr": cpuFilterv6L3RuleSrcIpAddr,
       "cpuFilterv6L3RuleDstIpAddrMask": cpuFilterv6L3RuleDstIpAddrMask,
       "cpuFilterv6L3RuleSrcIpAddrMask": cpuFilterv6L3RuleSrcIpAddrMask,
       "cpuFilterv6L3RuleTcpUdpDstPort": cpuFilterv6L3RuleTcpUdpDstPort,
       "cpuFilterv6L3RuleTcpUdpSrcPort": cpuFilterv6L3RuleTcpUdpSrcPort,
       "cpuFilterv6L3RuleTcpUdpDstPortMask": cpuFilterv6L3RuleTcpUdpDstPortMask,
       "cpuFilterv6L3RuleTcpUdpSrcPortMask": cpuFilterv6L3RuleTcpUdpSrcPortMask,
       "cpuFilterv6L3RuleTcpAckBit": cpuFilterv6L3RuleTcpAckBit,
       "cpuFilterv6L3RuleTcpRstBit": cpuFilterv6L3RuleTcpRstBit,
       "cpuFilterv6L3RuleTcpUrgBit": cpuFilterv6L3RuleTcpUrgBit,
       "cpuFilterv6L3RuleTcpPshBit": cpuFilterv6L3RuleTcpPshBit,
       "cpuFilterv6L3RuleTcpSynBit": cpuFilterv6L3RuleTcpSynBit,
       "cpuFilterv6L3RuleTcpFinBit": cpuFilterv6L3RuleTcpFinBit,
       "cpuFilterv6L3RuleTrafficClass": cpuFilterv6L3RuleTrafficClass,
       "cpuFilterv6L3RulePortList": cpuFilterv6L3RulePortList,
       "cpuFilterv6L3RuleAction": cpuFilterv6L3RuleAction,
       "cpuFilterv6L3RuleStatus": cpuFilterv6L3RuleStatus,
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
       "companyQinQ": companyQinQ,
       "qinqSystem": qinqSystem,
       "qinqGlobalStatus": qinqGlobalStatus,
       "qinqTable": qinqTable,
       "qinqEntry": qinqEntry,
       "qinqIfIndex": qinqIfIndex,
       "qinqRoleState": qinqRoleState,
       "qinqOuterTPID": qinqOuterTPID,
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
       "companyLimitIp": companyLimitIp,
       "limitIpMulticastProfileTable": limitIpMulticastProfileTable,
       "limitIpMulticastProfileEntry": limitIpMulticastProfileEntry,
       "limitIpMulticastIPType": limitIpMulticastIPType,
       "limitIpMulticastProfileID": limitIpMulticastProfileID,
       "limitIpMulticastProfileName": limitIpMulticastProfileName,
       "limitIpMulticastProfileStatus": limitIpMulticastProfileStatus,
       "limitIpMulticastEntryTable": limitIpMulticastEntryTable,
       "limitIpMulticastEntry": limitIpMulticastEntry,
       "limitIpMulticastEntryIPType": limitIpMulticastEntryIPType,
       "limitIpMulticastEntryProfileID": limitIpMulticastEntryProfileID,
       "limitIpMulticaststartIpAddr": limitIpMulticaststartIpAddr,
       "limitIpMulticastendIpAddr": limitIpMulticastendIpAddr,
       "limitIpMulticastStatus": limitIpMulticastStatus,
       "limitIpMulticastPortTable": limitIpMulticastPortTable,
       "limitIpMulticastPortEntry": limitIpMulticastPortEntry,
       "limitIpMulticastPortIPType": limitIpMulticastPortIPType,
       "limitIpMulticastPortID": limitIpMulticastPortID,
       "limitIpMulticastPortState": limitIpMulticastPortState,
       "limitIpMulticastPortProfileID": limitIpMulticastPortProfileID,
       "limitIpMulticastPortMaxGrp": limitIpMulticastPortMaxGrp,
       "companyMulticastFilter": companyMulticastFilter,
       "mcastFilterPortTable": mcastFilterPortTable,
       "mcastFilterPortEntry": mcastFilterPortEntry,
       "mcastFilterPortIndex": mcastFilterPortIndex,
       "mcastFilterPortType": mcastFilterPortType,
       "companyNeighbor": companyNeighbor,
       "neighborTable": neighborTable,
       "neighborEntry": neighborEntry,
       "neighborIfindex": neighborIfindex,
       "neighborIPv6Addr": neighborIPv6Addr,
       "neighborMACAddr": neighborMACAddr,
       "neighborType": neighborType,
       "neighborCacheState": neighborCacheState,
       "neighborActiveStatus": neighborActiveStatus,
       "neighborRowStatus": neighborRowStatus,
       "companyEoam": companyEoam,
       "eoamSystem": eoamSystem,
       "eoamTable": eoamTable,
       "eoamEntry": eoamEntry,
       "eoamIfIndex": eoamIfIndex,
       "eoamState": eoamState,
       "eoamMode": eoamMode,
       "eoamReceivedRemoteLoopback": eoamReceivedRemoteLoopback,
       "eoamRemoteLoopback": eoamRemoteLoopback,
       "eoamDyingGaspEnable": eoamDyingGaspEnable,
       "eoamCriticalEventEnable": eoamCriticalEventEnable,
       "eoamLinkMonitor": eoamLinkMonitor,
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
       "companyDuld": companyDuld,
       "duldSystem": duldSystem,
       "duldTable": duldTable,
       "duldEntry": duldEntry,
       "duldIfIndex": duldIfIndex,
       "duldState": duldState,
       "duldOperState": duldOperState,
       "duldMode": duldMode,
       "duldLinkStatus": duldLinkStatus,
       "duldDiscoveryTime": duldDiscoveryTime,
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
       "mldsHost": mldsHost,
       "mldsHostTable": mldsHostTable,
       "mldsHostEntry": mldsHostEntry,
       "mldsHostTableVLANID": mldsHostTableVLANID,
       "mldsHostTableGroupAddress": mldsHostTableGroupAddress,
       "mldsHostTablePort": mldsHostTablePort,
       "mldsHostTableHostIPAddress": mldsHostTableHostIPAddress,
       "companyPPPoE": companyPPPoE,
       "pppoeGlobalState": pppoeGlobalState,
       "pppoePortTable": pppoePortTable,
       "pppoePortEntry": pppoePortEntry,
       "pppoePortIndex": pppoePortIndex,
       "pppoePortState": pppoePortState,
       "pppoePortCircuitIDType": pppoePortCircuitIDType,
       "pppoePortUDFString": pppoePortUDFString,
       "pppoePortCircuitIDVendor3String": pppoePortCircuitIDVendor3String,
       "pppoePortRemoteIDType": pppoePortRemoteIDType,
       "pppoePortRemoteIDVendor3String": pppoePortRemoteIDVendor3String,
       "companyAgentBasicInfo": companyAgentBasicInfo,
       "agentCPUutilization": agentCPUutilization,
       "agentCPUutilizationIn5sec": agentCPUutilizationIn5sec,
       "agentCPUutilizationIn1min": agentCPUutilizationIn1min,
       "agentCPUutilizationIn5min": agentCPUutilizationIn5min,
       "agentMEMutilization": agentMEMutilization,
       "agentMEMutilizationIn5sec": agentMEMutilizationIn5sec,
       "agentMEMutilizationIn1min": agentMEMutilizationIn1min,
       "agentMEMutilizationIn5min": agentMEMutilizationIn5min,
       "companyTraps": companyTraps,
       "traps": traps,
       "snmpTrapSNMPAuthentication": snmpTrapSNMPAuthentication,
       "snmpTrapColdStart": snmpTrapColdStart,
       "snmpTrapWarmStart": snmpTrapWarmStart,
       "snmpTrapCopperLinkUpDown": snmpTrapCopperLinkUpDown,
       "snmpTrapRSTPStateChange": snmpTrapRSTPStateChange,
       "snmpTrapFirmUpgrade": snmpTrapFirmUpgrade,
       "snmpTrapPortSecurity": snmpTrapPortSecurity,
       "snmpTrapLBD": snmpTrapLBD,
       "macNotificatiotn": macNotificatiotn,
       "duplicateIP": duplicateIP,
       "trafficControl": trafficControl,
       "topologyChange": topologyChange,
       "newRootBrgaddress": newRootBrgaddress,
       "newRootOlddesignatedroot": newRootOlddesignatedroot,
       "newRootMSTibridgeregionalroot": newRootMSTibridgeregionalroot}
)
